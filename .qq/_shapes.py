"""
The model `qq shapes` renders and views: read and checked from JSON, and built into triangles in model space.

The format is the shapegen skill's (.claude/skills/shapegen/SKILL.md). Space is metres: x east, y north, z up, origin
at the footprint's south-west corner on the deck; a grid cell is one metre square, as the deck tiles were briefed.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

import _sim
import sprites
from common import cli, paths

#: The device camera (GAM-10): tilted a little from straight down, "about 15–20°" (docs/style.md).
TILT_DEG = 18
#: Each view as (azimuth, elevation) in degrees: azimuth 0 is a camera south of the model looking north, growing
#: toward east; elevation is above the horizon. `device` is the game's; the rest are for checking the shape.
VIEWS = {"iso": (-45, 35), "rear": (135, 35), "device": (0, 90 - TILT_DEG), "top": (0, 90), "front": (0, 0),
         "side": (90, 0)}
#: Toward the light: above, a little west and south — the "lighting from the top left" every brief asks, as the device
#: camera sees it. A face turned from it keeps AMBIENT of its texture's brightness.
LIGHT = (-0.4, -0.35, 0.85)
AMBIENT = 0.5
#: Of a cutout texture, below this alpha the face is a hole.
CUTOUT_ALPHA = 0.5
#: Where two faces lie in one plane the later part in the model shows: each part stands this much nearer the camera
#: than the one before it. Small enough that no real gap is crossed, large enough to beat rounding.
TIE_M = 1e-6
#: Two parts of separate items may share this much and still only touch: a decal's millimetres off its face, a cut's
#: rounding. Deeper, one is drawn inside the other (`overlaps`).
TOUCH_M = 0.003
#: Of a tiled texture, the share of its width and of its height at each edge cross-faded to meet the opposite edge.
#: Under a half, so the rolled copy's own seam stays in the part shown unmixed.
SEAM_SHARE = 0.25
#: Facets round a cylinder or a sphere: as many as keep each facet within FACET_SAG_M of the true curve, a multiple of
#: four so a silhouette seen square-on is symmetric, between the bounds. A sphere has half as many rings.
FACET_SAG_M = 0.0005
SEGMENTS_MIN, SEGMENTS_MAX = 8, 64
#: Of a box's `bevelM`, the most it may take: this share of its smallest half-size, so a thin plate keeps a flat face.
BEVEL_SHARE = 0.5
#: A rounded edge (`roundM`) is drawn in facets each within ROUND_SAG_M of its arc, and a face's half of the arc in at
#: most ROUND_STEPS_MOST of them: its normals are smooth, so the light reads round whatever the count, and only the
#: outline shows the facets. A millimetre is about half a pixel of a 1080-pixel page at the floor camera's nearest
#: (scene.js ZOOM.most, a ten-cell capsule); two steps keep a box at 300 triangles and a 5 cm radius within it.
ROUND_SAG_M = 0.001
ROUND_STEPS_MOST = 2
AXES = {"x": 0, "y": 1, "z": 2}
#: How far a face may stretch the picture it shows (GAM-14) — the region's proportion over the picture's, either way —
#: and still be its own proportions: a cut asked square comes out up to 4–5% off it (the kept ones 0.96–1.05), and an
#: inset rounds to whole pixels. Under it a round bolt does not read as oval.
STRETCH_MOST = 0.05
#: A face narrower than this is an edge — a decal's depth, a plate's rim: across it a picture is a line of its colour
#: whose proportions nothing can see, so `stretched` passes it.
EDGE_M = 0.01

#: Each box face: its outward normal, and the texture's right and up as seen from outside.
BOX_FACES = {
    "south": ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
    "north": ((0, 1, 0), (-1, 0, 0), (0, 0, 1)),
    "east": ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    "west": ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
    "top": ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
    "bottom": ((0, 0, -1), (1, 0, 0), (0, -1, 0)),
}
FACING = {"south": "south", "north": "north", "east": "east", "west": "west", "up": "top", "down": "bottom"}
SHAPE_KEYS = {
    "box": {"atM", "sizeM", "bevelM", "roundM", "roundAlong"},
    "cylinder": {"atM", "radiusM", "radiusEndM", "lengthM", "axis", "roundM"},
    "sphere": {"atM", "radiusM", "sizeM", "half"},
    "quad": {"atM", "sizeM", "facing"},
    "group": {"atM", "parts", "bevelM", "roundM", "roundAlong"},
    "model": {"atM", "src"},
}
SHAPE_FACES = {"box": set(BOX_FACES), "cylinder": {"side", "ends"}, "sphere": {"surface"}, "quad": {"face"}}
PART_KEYS = {"shape", "name", "rotDeg", "repeat", "tex", "faces", "shade", "live"}
#: What a part shows of its device in the game (`live`): each way of showing, and the device's signals it can show —
#: `state` running / short / fault / off, `run` whether it runs, `fault` whether it starved or is full, and the shares
#: 0–1 `cycle` (of the cycle under way), `input`, `output` and `held` (of what its slots hold at most). The page drives
#: them (src/app/web/wwwroot/scene.js); a render, a sprite and the catalogue show each as modelled.
SHARES = {"cycle", "input", "output", "held"}
LIVE = {"lamp": {"state", "run", "fault"}, "glow": {"run"}, "needle": SHARES, "fill": SHARES, "spin": {"run"},
        "stroke": {"run"}}
#: The keys each way takes: a needle turns about `facing` (the way its dial faces), clockwise as seen from it, from
#: the reading 0 it is modelled at by `sweepDeg` at 1, round `pivotM` (from the part's centre); a fill lights from its
#: far end `toward` the way it grows, in `steps` if it has them; a spin turns about `facing` at `degPerS`; a stroke
#: travels `strokeM` `toward` and back every `periodS`, at an even pace.
LIVE_KEYS = {"lamp": {"as", "show"}, "glow": {"as", "show"}, "needle": {"as", "show", "facing", "sweepDeg", "pivotM"},
             "fill": {"as", "show", "toward", "steps"}, "spin": {"as", "show", "facing", "degPerS", "pivotM"},
             "stroke": {"as", "show", "toward", "strokeM", "periodS"}}
NEEDLE_SWEEP_DEG = 270
DIRECTIONS = {"east": (1, 0, 0), "west": (-1, 0, 0), "north": (0, 1, 0), "south": (0, -1, 0), "up": (0, 0, 1),
              "down": (0, 0, -1)}
#: The most live parts a model has: the page's arrays of them are this long (scene.js LIVE_MAX).
LIVE_MOST = 12
MODEL_KEYS = {"id", "about", "sets", "boundsM", "frame", "textures", "parts"}
#: `frame` values: `exact` frames a render on `boundsM` and nothing round it — a tile or a slice the page repeats.
FRAMES = {"exact"}
#: `repeats: true` — the picture, inset cropped, already meets itself at its edges (a stripe cropped to whole periods):
#: tiled as it is, since the cross-fade (`seamless`) would lay its rolled copy half a picture out of step.
TEXTURE_KEYS = {"src", "insetPct", "tileM", "cutout", "repeats"}
FACE_KEYS = {"tex", "turnDeg", "tileM", "shade"}


def load_model(base: Path, source: Path, within: tuple[Path, ...] = ()) -> dict:
    """
    The model read and checked: every key known, every texture found and loaded (`images`, inset already cropped),
    `files`, the model and every file it reads, and `subs`, each model a `model` part places, by its `src`.

    <remarks>A placed model's textures join this one's named `<its id>.<name>`, so two models' `steel` never meet;
    `within` is the chain of models placing this one, and a model placing itself is refused.</remarks>
    """
    if source.resolve() in within:
        cli.fail(f"{_sim.rel(base, source)} places itself, through {' → '.join(_sim.rel(base, w) for w in within)}")
    try:
        model = json.loads(source.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        cli.fail(f"{_sim.rel(base, source)}: {e}")
    strict(model, MODEL_KEYS, "the model")
    for key in ("id", "textures", "parts"):
        if key not in model:
            cli.fail(f"the model has no {key!r}")
    sprites.asset_id(model["id"])
    if "frame" in model and (model["frame"] not in FRAMES or "boundsM" not in model):
        cli.fail(f"frame is one of {sorted(FRAMES)}, and needs boundsM")
    if not (isinstance(model.get("sets", []), list) and all(isinstance(s, str) for s in model.get("sets", []))):
        cli.fail("sets is not a list of set ids (raw_assets/sets.md)")
    model["images"], model["files"] = Pictures(), [source]
    for name, texture in model["textures"].items():
        texture = {"src": texture} if isinstance(texture, str) else texture
        strict(texture, TEXTURE_KEYS, f"texture {name}")
        model["textures"][name] = texture
        picture = paths.resolve_in_root(base / texture["src"], base)
        if not picture.is_file():
            cli.fail(f"texture {name}: no picture at {texture['src']}")
        model["files"].append(picture)
        if not isinstance(texture.get("repeats", False), bool):
            cli.fail(f"texture {name}: repeats is true or false")
        model["images"].sources[name] = (picture, inset_pct(texture, name),
                                         "tileM" in texture and not texture.get("repeats"))
    model["subs"], named = {}, {}
    for src in placed(model["parts"]):
        if src in model["subs"]:
            continue
        sub = load_model(base, paths.resolve_in_root(base / src, base), (*within, source.resolve()))
        if named.setdefault(sub["id"], src) != src:
            cli.fail(f"{named[sub['id']]} and {src} are both {sub['id']!r}: one model places one version of a part")
        for name, texture in sub["textures"].items():
            model["textures"][f"{sub['id']}.{name}"] = texture
            model["images"].sources[f"{sub['id']}.{name}"] = sub["images"].sources[name]
        model["subs"] |= sub["subs"] | {src: sub}
        model["files"] += sub["files"]
    return model


def placed(parts) -> list[str]:
    """The `src` of every `model` part, groups searched, a placed model's own parts not."""
    found = []
    for part in parts if isinstance(parts, list) else []:
        if not isinstance(part, dict):
            continue
        if part.get("shape") == "model":
            if not isinstance(part.get("src"), str):
                cli.fail(f"a model part ({part.get('name', 'unnamed')}) wants src, the model file it places")
            found.append(part["src"])
        elif part.get("shape") == "group":
            found += placed(part.get("parts"))
    return found


#: Every picture read this run, by (file, its mtime, inset, tiled): models sharing a texture read it once.
_READ: dict[tuple, object] = {}


class Pictures(dict):
    """
    A model's texture pictures by name, as float RGBA arrays: inset cropped, and made `seamless` when tiled.

    <remarks>Each is read only when first asked for, so loading a model to list or check it opens no picture.
    `sources` holds what each name is read from: (file, insetPct as (across, down), tiled); `sizes` each one's pixels
    after its inset, read from its header when first asked (`size`).</remarks>
    """

    def __init__(self):
        super().__init__()
        self.sources: dict[str, tuple[Path, tuple[float, float], bool]] = {}
        self.sizes: dict[str, tuple[int, int]] = {}

    def size(self, name: str) -> tuple[int, int]:
        """The picture's width and height in pixels, its inset cropped off."""
        if name not in self.sizes:
            from PIL import Image

            picture, inset, _ = self.sources[name]
            with Image.open(picture) as image:
                self.sizes[name] = inset_size(image.size, inset)
        return self.sizes[name]

    def __missing__(self, name: str):
        key = self.identity(name)
        if key not in _READ:
            _READ[key] = read_picture(*self.sources[name])
        self[name] = _READ[key]
        return self[name]

    def identity(self, name: str) -> tuple:
        """What the picture `name` is made from: the same identity is the same pixels."""
        picture, inset, tiled = self.sources[name]
        return str(picture), picture.stat().st_mtime_ns, inset, tiled


def inset_pct(texture: dict, name: str) -> tuple[float, float]:
    """A texture's `insetPct` as (off each side, off top and bottom): one number is both."""
    inset = texture.get("insetPct", 0)
    if isinstance(inset, (int, float)):
        inset = [inset, inset]
    if not (isinstance(inset, list) and len(inset) == 2 and all(isinstance(v, (int, float)) and 0 <= v < 50
                                                                 for v in inset)):
        cli.fail(f"texture {name}: insetPct wants a number, or [across, down], each 0 to under 50")
    return inset[0], inset[1]


def inset_px(size: tuple[int, int], inset: tuple[float, float]) -> tuple[int, int]:
    """Of a picture `size` pixels, how many its inset crops off each side and off top and bottom."""
    return round(size[0] * inset[0] / 100), round(size[1] * inset[1] / 100)


def inset_size(size: tuple[int, int], inset: tuple[float, float]) -> tuple[int, int]:
    dx, dy = inset_px(size, inset)
    return size[0] - 2 * dx, size[1] - 2 * dy


def read_picture(picture: Path, inset: tuple[float, float], tiled: bool):
    import numpy as np
    from PIL import Image

    image = Image.open(picture).convert("RGBA")
    dx, dy = inset_px(image.size, inset)
    image = np.asarray(image.crop((dx, dy, image.width - dx, image.height - dy)), dtype=np.float32) / 255
    return seamless(image) if tiled else image


def seamless(image, share: float = SEAM_SHARE):
    """
    The picture made to meet itself at every edge: along each axis in turn, its outer `share` cross-fades into a copy
    of itself rolled by half, whose own seam falls in the middle where the picture shows unmixed. A generated
    "repeating" swatch never quite repeats — its edges keep a rim or a shift in tone, a cross wherever it tiles.

    <remarks>A plain average of two unrelated pictures is flatter than either — to 1/√2 of the contrast along an
    edge, half in a corner — and shows as a grid of faded bands where it tiles. The blend is variance-preserving, and
    each colour channel is then given back the original's exact histogram (Heitz and Neyret, "High-Performance
    By-Example Noise using a Histogram-Preserving Blending Operator", 2018). Alpha is blended plainly.</remarks>
    """
    import numpy as np

    colour, alpha = image[..., :3], image[..., 3:]
    mean = colour.mean(axis=(0, 1))
    for axis in (1, 0):
        n = image.shape[axis]
        index = np.arange(n) + 0.5
        weight = np.clip(np.minimum(index, n - index) / (n * share), 0, 1)
        weight = weight.reshape([-1, 1, 1] if axis == 0 else [1, -1, 1])
        spread = np.sqrt(weight ** 2 + (1 - weight) ** 2)
        colour = mean + (weight * (colour - mean) + (1 - weight) * (np.roll(colour, n // 2, axis=axis) - mean)) / spread
        alpha = weight * alpha + (1 - weight) * np.roll(alpha, n // 2, axis=axis)
    matched = np.empty_like(colour)
    for c in range(3):
        flat = np.empty(colour[..., c].size, np.float32)
        flat[np.argsort(colour[..., c], axis=None, kind="stable")] = np.sort(image[..., c], axis=None)
        matched[..., c] = flat.reshape(colour.shape[:2])
    return np.concatenate([matched, alpha], axis=-1).astype(np.float32)


def turned(model: dict, name: str, turn: int):
    """A texture's picture as a face turned `turn` degrees clockwise wears it."""
    import numpy as np

    return np.rot90(model["images"][name], k=-turn // 90)


def strict(node, allowed: set[str], where: str) -> None:
    if not isinstance(node, dict):
        cli.fail(f"{where} is not an object")
    unknown = set(node) - allowed
    if unknown:
        cli.fail(f"{where}: unknown {', '.join(sorted(unknown))}; known are {', '.join(sorted(allowed))}")


def build(model: dict) -> dict:
    """
    Every part's triangles in model space: positions P, normals N, texture coordinates UV, which face-look each wears
    (`look`, into `looks`, each naming its face and part), and which part it is (`order`, into `labels` and `specs`,
    the part as written, and `frames`, its box turned with it as (centre, axes, half-size)) — a part later in the
    file is a higher one. `live` is the live part each triangle is (into `lives`, from 1; 0 for none): what it shows,
    in model space, with `boxM` round it as modelled and, of a fill, `spanM` — how far along its axis it reaches.
    """
    import numpy as np

    looks, labels, specs, items, frames, lives, batches = [], [], [], [], [], [], []
    walk(model, model["parts"], np.eye(4),
         {"tex": None, "shade": 1.0, "ns": "", "item": None, "edge": {}, "live": 0, "show": None}, looks,
         (labels, specs, items, frames, lives), batches, "parts")
    if not batches:
        cli.fail("the model draws nothing")
    triangles = {"P": np.concatenate([b[0] for b in batches]), "N": np.concatenate([b[1] for b in batches]),
                 "UV": np.concatenate([b[2] for b in batches]),
                 "look": np.concatenate([np.full(len(b[0]), b[3]) for b in batches]),
                 "order": np.concatenate([np.full(len(b[0]), b[4]) for b in batches]),
                 "live": np.concatenate([np.full(len(b[0]), b[5]) for b in batches]), "lives": lives, "looks": looks,
                 "labels": labels, "specs": specs, "items": items, "frames": frames}
    for n, element in enumerate(lives, 1):
        P = triangles["P"][triangles["live"] == n].reshape(-1, 3)
        if not len(P):
            cli.fail(f"{element['part']}: a live part that draws nothing")
        element["boxM"] = [P.min(axis=0).round(4).tolist(), P.max(axis=0).round(4).tolist()]
        if element["as"] == "fill":
            along = P @ np.array(element["axis"])
            element["spanM"] = [round(float(along.min()), 4), round(float(along.max()), 4)]
    return triangles


def live_element(live: dict, show: str | None, matrix, here: str, lives: list) -> int:
    """
    The live part `live` declares, placed by `matrix`, added to `lives`: its number there, from 1. `show`, when a
    group or a placed model round it says so, is what it shows instead of its own.
    """
    import numpy as np

    kind = live.get("as")
    if kind not in LIVE:
        cli.fail(f"{here}: live as {kind!r}; known are {', '.join(LIVE)}")
    strict(live, LIVE_KEYS[kind], f"{here} live")
    show = show or live.get("show")
    if show not in LIVE[kind]:
        cli.fail(f"{here}: a live {kind} shows {', '.join(sorted(LIVE[kind]))}, not {show!r}")
    if len(lives) == LIVE_MOST:
        cli.fail(f"{here}: a model has at most {LIVE_MOST} live parts")
    element = {"as": kind, "show": show, "part": here}
    key = {"needle": "facing", "spin": "facing", "fill": "toward", "stroke": "toward"}.get(kind)
    if key:
        if live.get(key) not in DIRECTIONS:
            cli.fail(f"{here}: a live {kind} wants {key}, one of {', '.join(DIRECTIONS)}")
        element["axis"] = (matrix[:3, :3] @ np.array(DIRECTIONS[live[key]], dtype=float)).round(6).tolist()
    if kind in ("needle", "spin"):
        pivot = matrix @ np.array([*vector(live.get("pivotM", [0, 0, 0]), here, "pivotM"), 1.0])
        element["pivotM"] = pivot[:3].round(5).tolist()
    if kind == "needle":
        element["sweepDeg"] = live.get("sweepDeg", NEEDLE_SWEEP_DEG)
        if not isinstance(element["sweepDeg"], (int, float)):
            cli.fail(f"{here}: sweepDeg is not a number")
    if kind == "spin":
        element["degPerS"] = live.get("degPerS")
        if not isinstance(element["degPerS"], (int, float)) or not element["degPerS"]:
            cli.fail(f"{here}: a live spin wants degPerS, a number not 0")
    if kind == "stroke":
        for k in ("strokeM", "periodS"):
            element[k] = positive(live, k, here)
    if "steps" in live:
        if not isinstance(live["steps"], int) or live["steps"] < 1:
            cli.fail(f"{here}: steps wants a whole number above 0")
        element["steps"] = live["steps"]
    lives.append(element)
    return len(lives)


def overlaps(triangles: dict) -> list[dict]:
    """
    Every two parts of separate items whose boxes cross deeper than TOUCH_M on all three axes: one drawn inside the
    other. An item is a top-level part — a group or a placed model with everything in it — so a handle sunk into its
    mug is one assembly, and a table run into the seat behind it is two things in one place.

    <remarks>Measured on each part's own box, turned with it (`frames`), so a part set at 45° is not judged by the
    larger square round it: exact for boxes, a little generous round a cylinder or a sphere, so a rounded part
    reported is checked by eye. `depthM` is how far the two parts' model-space boxes cross on x, y and z.</remarks>
    """
    import numpy as np

    boxes = part_boxes(triangles)
    found = []
    for a in boxes:
        for b in boxes:
            if a >= b or triangles["items"][a] == triangles["items"][b]:
                continue
            depth = np.minimum(boxes[a][1], boxes[b][1]) - np.maximum(boxes[a][0], boxes[b][0])
            if (depth > TOUCH_M).all() and turned_depth(triangles["frames"][a], triangles["frames"][b]) > TOUCH_M:
                found.append({"parts": [triangles["labels"][a], triangles["labels"][b]],
                              "depthM": depth.round(3).tolist()})
    return found


def turned_depth(a, b) -> float:
    """
    How deep two turned boxes, each (centre, axes, half-size), cross: the least overlap over every axis that could
    separate them (each box's three, and the cross of each pair) — at or under 0 they are apart.
    """
    import numpy as np

    (ca, ra, ha), (cb, rb, hb) = a, b
    between = cb - ca
    candidates = [*ra.T, *rb.T, *(np.cross(x, y) for x in ra.T for y in rb.T)]
    least = np.inf
    for axis in candidates:
        length = np.linalg.norm(axis)
        if length < 1e-9:
            continue
        axis = axis / length
        reach = np.abs(ra.T @ axis) @ ha + np.abs(rb.T @ axis) @ hb
        least = min(least, reach - abs(between @ axis))
    return float(least)


def floating(triangles: dict, model: dict) -> list[str]:
    """
    Every item resting on nothing, in file order: not on the deck, not on or against an item that is, and not against
    the back of the footprint — `boundsM`'s north face, the wall a device stands with its back to. A mug in mid-air, a
    mirror with no wall behind it, a shelf holding up nothing but itself.

    <remarks>Measured on the parts' boxes as `overlaps` is: two parts of separate items touch when they come within
    TOUCH_M on one axis and cross on the other two — one stands on, or leans against, the other.</remarks>
    """
    boxes, items = part_boxes(triangles), triangles["items"]
    frame = bounds(model)
    deck_m, wall_m = (frame[0][2], frame[1][1]) if frame else (0.0, None)
    held = {items[o] for o, (lo, hi) in boxes.items()
            if lo[2] <= deck_m + TOUCH_M or (wall_m is not None and hi[1] >= wall_m - TOUCH_M)}
    grew = True
    while grew:
        grew = False
        for a in boxes:
            if items[a] not in held and any(items[b] in held and touching(boxes[a], boxes[b]) for b in boxes):
                held.add(items[a])
                grew = True
    return list(dict.fromkeys(items[o] for o in boxes if items[o] not in held))


def touching(a, b) -> bool:
    import numpy as np

    gaps = np.maximum(a[0] - b[1], b[0] - a[1])
    return gaps.max() <= TOUCH_M and np.sort(gaps)[1] < 0


def part_boxes(triangles: dict) -> dict:
    """
    Each part's box in model space, (low, high) corners, by its `order`: round the whole shape, its undrawn faces
    too, so a part left open below still stands on what it stands on.
    """
    import numpy as np

    boxes = {}
    for o in np.unique(triangles["order"]):
        centre, axes, half = triangles["frames"][o]
        reach = np.abs(axes) @ half
        boxes[o] = (centre - reach, centre + reach)
    return boxes


def walk(model, parts, parent, inherited, looks, named, batches, where) -> None:
    import numpy as np

    if not isinstance(parts, list):
        cli.fail(f"{where} is not a list")
    for n, part in enumerate(parts):
        here = f"{where}[{n}]" + (f" ({part['name']})" if isinstance(part, dict) and "name" in part else "")
        shape = part.get("shape") if isinstance(part, dict) else None
        if shape not in SHAPE_KEYS:
            cli.fail(f"{here}: shape is {shape!r}; known are {', '.join(SHAPE_KEYS)}")
        strict(part, PART_KEYS | SHAPE_KEYS[shape], here)
        own = {"tex": part.get("tex", inherited["tex"]), "shade": inherited["shade"] * part.get("shade", 1.0),
               "ns": inherited["ns"], "item": inherited["item"], "edge": edge(part, inherited["edge"], here),
               "live": inherited["live"], "show": inherited["show"]}
        if shape == "model" and ({"tex", "faces"} & set(part)):
            cli.fail(f"{here}: a placed model wears its own textures; tex and faces are not for it")
        live = part.get("live")
        if live is not None:
            if not isinstance(live, dict):
                cli.fail(f"{here}: live is not an object")
            if "as" not in live:
                if set(live) != {"show"} or shape not in ("group", "model"):
                    cli.fail(f"{here}: a live with no as is a group's or a placed model's, and says only what the "
                             f"live parts in it show: {{\"show\": …}}")
                own["show"] = inherited["show"] or live["show"]
            elif inherited["live"]:
                cli.fail(f"{here}: a live part inside another, {named[4][inherited['live'] - 1]['part']}")
        repeat = part.get("repeat", {"count": 1, "stepM": [0, 0, 0]})
        strict(repeat, {"count", "stepM"}, f"{here} repeat")
        count = repeat.get("count", 1)
        shared = 0
        for i in range(count):
            at = np.array(vector(part.get("atM", [0, 0, 0]), here, "atM")) + i * np.array(repeat.get("stepM", [0, 0, 0]))
            matrix = parent @ translation(at) @ rotation(part.get("rotDeg", [0, 0, 0]))
            label = here + (f" #{i + 1}" if count > 1 else "")
            item = inherited["item"] or label
            element = own["live"]
            if live is not None and "as" in live:
                # A lamp, a glow or a fill is one however many times it repeats; each copy of what moves is its own.
                turns = live["as"] in ("needle", "spin", "stroke")
                if turns or not shared:
                    shared = live_element(live, own["show"], matrix, label if turns else here, named[4])
                element = shared
            if shape == "group":
                walk(model, part.get("parts"), matrix, own | {"item": item, "live": element}, looks, named, batches,
                     label + ".parts")
                continue
            if shape == "model":
                sub = model["subs"][part["src"]]
                walk(model, sub["parts"], matrix,
                     {"tex": None, "shade": own["shade"], "ns": f"{own['ns']}{sub['id']}.", "item": item,
                      "edge": {}, "live": element, "show": own["show"]}, looks, named, batches,
                     f"{label} <{sub['id']}>.parts")
                continue
            labels, specs, items, frames, _ = named
            order = len(labels)
            labels.append(label)
            items.append(item)
            specs.append(part | {"atWorldM": matrix[:3, 3].round(4).tolist()})
            faces = primitive(shape, {k: v for k, v in part.items() if k not in EDGE_KEYS} | own["edge"], here)
            local = np.concatenate([P.reshape(-1, 3) for P, _, _ in faces.values()])
            lo, hi = local.min(axis=0), local.max(axis=0)
            frames.append((matrix[:3, :3] @ ((lo + hi) / 2) + matrix[:3, 3], matrix[:3, :3], (hi - lo) / 2))
            for face, (P, N, UV) in faces.items():
                look = face_look(model, part, face, own, here)
                if look is None:
                    continue
                look["spanM"] = fitted_span(UV)
                UV = UV["m"] / np.array(look["tileM"]) if look["tileM"] is not None else UV["fit"]
                looks.append(look | {"face": face, "part": order})
                batches.append((P @ matrix[:3, :3].T + matrix[:3, 3], N @ matrix[:3, :3].T, UV, len(looks) - 1, order,
                                element))


EDGE_KEYS = ("bevelM", "roundM", "roundAlong")


def edge(part: dict, inherited: dict, here: str) -> dict:
    """
    How a part's edges are finished: its own `bevelM` or `roundM` (with `roundAlong`), else its group's — a part
    giving either replaces both. A group's pass to its boxes; a cylinder's `roundM` is its own alone.
    """
    own = {k: part[k] for k in EDGE_KEYS if k in part}
    if "bevelM" in own and "roundM" in own:
        cli.fail(f"{here}: an edge is bevelled or rounded, not both: bevelM or roundM")
    if "roundAlong" in own and "roundM" not in own:
        cli.fail(f"{here}: roundAlong says which edges roundM rounds, and there is no roundM")
    if part.get("shape") == "cylinder":
        return own
    return own if ("bevelM" in own or "roundM" in own) else inherited


def face_look(model, part, face, own, here) -> dict | None:
    """What one face wears: a texture by name, turned and tiled, shaded; None for a face left undrawn."""
    faces = part.get("faces", {})
    if faces and not isinstance(faces, dict):
        cli.fail(f"{here}: faces is not an object")
    shape = part["shape"]
    unknown = set(faces) - SHAPE_FACES[shape] - {"*"}
    if unknown:
        cli.fail(f"{here}: a {shape} has no face {', '.join(sorted(unknown))}; "
                 f"it has {', '.join(sorted(SHAPE_FACES[shape]))}")
    spec = faces.get(face, faces.get("*", own["tex"])) if faces else own["tex"]
    if spec is None:
        if face in faces:
            return None
        cli.fail(f"{here}: its {face} face has no texture (tex, or faces.{face} / faces.*)")
    spec = {"tex": spec} if isinstance(spec, str) else spec
    strict(spec, FACE_KEYS, f"{here} face {face}")
    name = f"{own['ns']}{spec.get('tex')}"
    if name not in model["textures"]:
        cli.fail(f"{here}: no texture {name!r}; the model has {', '.join(model['textures'])}")
    turn = spec.get("turnDeg", 0)
    if turn % 90:
        cli.fail(f"{here} face {face}: turnDeg {turn} is not a multiple of 90")
    tile = spec.get("tileM", model["textures"][name].get("tileM"))
    if tile is not None:
        tile = tile_m(tile, lambda: shown_aspect(model, name, turn), f"{here} face {face}")
    return {"tex": name, "turn": turn % 360, "tileM": tile, "shade": own["shade"] * spec.get("shade", 1.0),
            "cutout": bool(model["textures"][name].get("cutout"))}


def tile_m(tile, aspect, where: str) -> list[float]:
    """
    A `tileM` as [across, down] metres: a number is both; an axis given as null is derived from the other so one repeat
    keeps the picture's proportions, `aspect()` (its width over its height as the face wears it).
    """
    if isinstance(tile, (int, float)) and tile > 0:
        return [tile, tile]
    given = [isinstance(v, (int, float)) and v > 0 for v in tile] if isinstance(tile, list) and len(tile) == 2 else []
    if given == [True, True]:
        return tile
    if given == [True, False] and tile[1] is None:
        return [tile[0], tile[0] / aspect()]
    if given == [False, True] and tile[0] is None:
        return [tile[1] * aspect(), tile[1]]
    cli.fail(f"{where}: tileM wants metres above 0 — a number, [across, down], or one of them and null for the other "
             f"to keep the picture's proportions")


def shown_aspect(model: dict, name: str, turn: int) -> float:
    """The texture's width over its height as a face turned `turn` degrees wears it: its inset cropped off."""
    width, height = model["images"].size(name)
    return height / width if turn % 180 else width / height


def fitted_span(UV) -> list[float] | None:
    """
    The metres across and down a face that one fitting of its picture spans, from its texture coordinates; None for a
    face too thin to have both. A whole sphere's is its equator by pole to pole, where its picture is least squeezed.
    """
    fit, metres = UV["fit"].reshape(-1, 2), UV["m"].reshape(-1, 2)
    spread = fit.max(axis=0) - fit.min(axis=0)
    if (spread <= 1e-9).any():
        return None
    span = (metres.max(axis=0) - metres.min(axis=0)) / spread
    return None if (span <= 1e-9).any() else span.tolist()


def stretched(triangles: dict, model: dict) -> list[dict]:
    """
    Every face showing its picture at other than the picture's own proportions (GAM-14), past STRETCH_MOST, a part's
    repeats as one: the region one fitting or one repeat covers on the face (`regionM`, across and down, after
    `turnDeg`) against the picture's pixels after `insetPct`. `ratio` is the region's proportion over the picture's —
    above 1 the picture is drawn wider than it is.

    <remarks>A whole sphere is measured at its equator: toward its poles every picture gathers to a point, which no
    proportion avoids. A face under EDGE_M across is passed; one wider, however thin, is not — a board's edge wearing
    a fitted picture shows it squeezed into a strip, where a `tileM` with one axis null shows a plain corner of it at
    its own proportions.</remarks>
    """
    found, seen = [], set()
    for look in triangles["looks"]:
        label = re.sub(r" #\d+", "", triangles["labels"][look["part"]])
        if (label, look["face"]) in seen:
            continue
        seen.add((label, look["face"]))
        if look["spanM"] is None or min(look["spanM"]) < EDGE_M:
            continue
        region = look["tileM"] or look["spanM"]
        picture = shown_aspect(model, look["tex"], look["turn"])
        ratio = region[0] / region[1] / picture
        if max(ratio, 1 / ratio) - 1 > STRETCH_MOST:
            found.append({"part": label, "face": look["face"], "tex": look["tex"], "tiled": look["tileM"] is not None,
                          "regionM": [round(v, 3) for v in region], "pictureAspect": round(picture, 3),
                          "ratio": round(ratio, 3)})
    return found


def vector(value, here, key, size=3) -> list[float]:
    if not (isinstance(value, list) and len(value) == size and all(isinstance(v, (int, float)) for v in value)):
        cli.fail(f"{here}: {key} is not a list of {size} numbers")
    return value


def positive(part, key, here) -> float:
    value = part.get(key)
    if not isinstance(value, (int, float)) or value <= 0:
        cli.fail(f"{here}: {key} wants a number above 0")
    return value


def bounds(model: dict):
    """The model's `boundsM` as (low, high) corners, or None."""
    import numpy as np

    if "boundsM" not in model:
        return None
    if not (isinstance(model["boundsM"], list) and len(model["boundsM"]) == 2):
        cli.fail("boundsM is not two corners")
    return tuple(np.array(vector(c, "boundsM", "corner")) for c in model["boundsM"])


def primitive(shape, part, here) -> dict:
    """
    Each face of the shape, centred on its own origin, as (P, N, UV) triangle arrays; UV holds `fit` (0..1 over the
    face) and `m` (metres along it).
    """
    import numpy as np

    if shape == "box":
        half = np.array(vector(part.get("sizeM"), here, "sizeM")) / 2
        bevel = not_negative(part, "bevelM", here)
        bevel = min(bevel, BEVEL_SHARE * half.min())
        if bevel > 0:
            return {face: bevelled(half, bevel, n, r, up) for face, (n, r, up) in BOX_FACES.items()}
        radii = round_radii(half, not_negative(part, "roundM", here), part.get("roundAlong"), here)
        if radii.any():
            return {face: rounded(half, radii, n, r, up) for face, (n, r, up) in BOX_FACES.items()}
        return {face: planar(np.array(n) * half, n, r, up, abs(np.dot(r, half)), abs(np.dot(up, half)))
                for face, (n, r, up) in BOX_FACES.items()}
    if shape == "quad":
        facing = part.get("facing", "south")
        if facing not in FACING:
            cli.fail(f"{here}: facing is {facing!r}; known are {', '.join(FACING)}")
        n, r, up = BOX_FACES[FACING[facing]]
        width, height = vector(part.get("sizeM"), here, "sizeM", 2)
        return {"face": planar(np.zeros(3), n, r, up, width / 2, height / 2)}
    if shape == "cylinder":
        radius = positive(part, "radiusM", here)
        radius_end = part.get("radiusEndM", radius)
        length = positive(part, "lengthM", here)
        rim = not_negative(part, "roundM", here)
        if rim and radius_end != radius:
            cli.fail(f"{here}: roundM rounds the rims of a straight cylinder; this one tapers (radiusEndM)")
        faces = cylinder(radius, radius_end, length, segments(max(radius, radius_end)), min(rim, radius, length / 2))
        axis = part.get("axis", "z")
        turn = {"z": np.eye(3), "x": rotation([0, 90, 0])[:3, :3], "y": rotation([-90, 0, 0])[:3, :3]}.get(axis)
        if turn is None:
            cli.fail(f"{here}: axis is {axis!r}; known are x, y, z")
        return {face: (P @ turn.T, N @ turn.T, UV) for face, (P, N, UV) in faces.items()}
    if "sizeM" in part:
        radii = np.array(vector(part["sizeM"], here, "sizeM")) / 2
    else:
        radii = np.full(3, positive(part, "radiusM", here))
    return {"surface": sphere(radii, bool(part.get("half")), segments(radii.max()))}


def not_negative(part, key, here) -> float:
    value = part.get(key) or 0
    if not isinstance(value, (int, float)) or value < 0:
        cli.fail(f"{here}: {key} wants a number of 0 or more")
    return value


def round_radii(half, radius: float, along: str | None, here: str):
    """
    How far a rounded box's corners are drawn in along x, y and z: `radius` on every axis, or with `along` on the two
    across it alone — the edges running along that axis rounded, the faces across it flat with rounded corners. Each is
    at most the smallest half-size it rounds, where the arcs of two edges meet and the face between them is all round.
    """
    import numpy as np

    if along is not None and along not in AXES:
        cli.fail(f"{here}: roundAlong is {along!r}; known are {', '.join(AXES)}")
    rounds = np.ones(3, bool)
    if along is not None:
        rounds[AXES[along]] = False
    return np.where(rounds, min(radius, half[rounds].min()), 0.0)


def round_steps(radius_m: float) -> int:
    """Facets in a face's half of a rounded edge's quarter arc: each within ROUND_SAG_M of it, at most ROUND_STEPS_MOST."""
    if radius_m <= ROUND_SAG_M:
        return 1
    facet = 2 * math.acos(1 - ROUND_SAG_M / radius_m)
    return min(max(math.ceil(math.pi / 4 / facet), 1), ROUND_STEPS_MOST)


def segments(radius_m: float) -> int:
    """Facets round a circle of this radius: each within FACET_SAG_M of it (`FACET_SAG_M`)."""
    if radius_m <= FACET_SAG_M:
        return SEGMENTS_MIN
    count = math.pi / math.acos(1 - FACET_SAG_M / radius_m)
    return int(min(max(math.ceil(count / 4) * 4, SEGMENTS_MIN), SEGMENTS_MAX))


def bevelled(half, bevel, n, r, up):
    """
    One face of a box with its edges chamfered by `bevel`: the face's flat middle and its half of every chamfer
    round it — to the chamfer's midline along an edge, to the corner triangle's centre at a corner — so six faces
    close the box and each wears its own texture over all it owns.

    <remarks>The texture lies as on the unbevelled face, each point at the face's own coordinates before the
    chamfer turns it, so a picture runs on round its edge unsqueezed. Each strip and corner is flat, lit by the
    chamfer's own normal.</remarks>
    """
    import numpy as np

    n, r, up = (np.array(v, dtype=float) for v in (n, r, up))
    h_n, h_r, h_up = abs(n @ half), abs(r @ half), abs(up @ half)
    xs = [-h_r, -(h_r - bevel), h_r - bevel, h_r]
    ys = [-h_up, -(h_up - bevel), h_up - bevel, h_up]

    def point(i: int, j: int):
        """Grid corner (i, j) of xs × ys, set on the chamfered box."""
        out_x, out_y = i in (0, 3), j in (0, 3)
        sx, sy = (1 if i == 3 else -1), (1 if j == 3 else -1)
        if out_x and out_y:
            x, y, d = sx * (h_r - 2 * bevel / 3), sy * (h_up - 2 * bevel / 3), 2 * bevel / 3
        elif out_x:
            x, y, d = sx * (h_r - bevel / 2), ys[j], bevel / 2
        elif out_y:
            x, y, d = xs[i], sy * (h_up - bevel / 2), bevel / 2
        else:
            x, y, d = xs[i], ys[j], 0.0
        return n * (h_n - d) + r * x + up * y

    P, N, fit, metres = [], [], [], []
    for i in range(3):
        for j in range(3):
            corners = [(i, j + 1), (i + 1, j + 1), (i + 1, j), (i, j)]
            normal = n + (i - 1) * r + (j - 1) * up
            normal /= np.linalg.norm(normal)
            quad = np.array([point(a, b) for a, b in corners])
            grid = np.array([[xs[a], ys[b]] for a, b in corners])
            for tri in ((0, 1, 2), (0, 2, 3)):
                P.append(quad[list(tri)])
                N.append(np.tile(normal, (3, 1)))
                fit.append(np.stack([(grid[list(tri), 0] + h_r) / (2 * h_r), (h_up - grid[list(tri), 1]) / (2 * h_up)], 1))
                metres.append(np.stack([grid[list(tri), 0], -grid[list(tri), 1]], 1))
    return np.array(P), np.array(N), {"fit": np.array(fit), "m": np.array(metres)}


def rounded(half, radii, n, r, up):
    """
    One face of a box with its edges rounded, `radii` the corner's inset along x, y and z: the face's flat middle and
    its half of each rounded edge round it, so six faces close the box with no gap.

    <remarks>A point on a face's half of an edge is the inner corner pushed out along the direction `n + tan(a)·r +
    tan(b)·up` — a turn of `a` across one edge and `b` across the other, up to 45° each — so two faces meeting on an
    edge's midline, and three at a corner, share every vertex there. Normals are that direction, smooth across the
    arc. A face across the axis left sharp (`roundAlong`) stays flat, its corners cut round to meet the arcs of the
    sides. The texture lies as on the unrounded face: along an arc each point at its turn's share of the radius past
    the inner corner, so the picture runs on to the edge's midline as on a bevel; on a flat face at the point's place.
    </remarks>
    """
    import numpy as np

    n, r, up = (np.array(v, dtype=float) for v in (n, r, up))
    h_n, h_r, h_up = abs(n @ half), abs(r @ half), abs(up @ half)
    reach_n, reach_r, reach_up = abs(n @ radii), abs(r @ radii), abs(up @ radii)

    def stations(h: float, reach: float) -> list[tuple[float, float]]:
        """Across the face along one axis: each vertex column as (inner coordinate, turn in radians)."""
        if reach <= 0:
            return [(-h, 0.0), (h, 0.0)]
        steps, inner = round_steps(reach), h - reach
        arc = [math.pi / 4 * s / steps for s in range(1, steps + 1)]
        middle = [(-inner, 0.0)] + ([(inner, 0.0)] if inner > 0 else [])
        return [(-inner, -a) for a in reversed(arc)] + middle + [(inner, a) for a in arc]

    def unrolled(inner: float, turn: float, reach: float) -> float:
        return inner + reach * turn / (math.pi / 4)

    across, down = stations(h_r, reach_r), stations(h_up, reach_up)
    P, N, place = [], [], []
    for x, a in across:
        for y, b in down:
            ta, tb = math.tan(a), math.tan(b)
            if reach_n > 0:
                d = n + ta * r + tb * up
                d /= np.linalg.norm(d)
                P.append(n * (h_n - reach_n) + r * x + up * y + radii * d)
                N.append(d)
                place.append((unrolled(x, a, reach_r), unrolled(y, b, reach_up)))
            else:
                most = max(abs(ta), abs(tb))
                out = np.array([ta, tb]) * (most * reach_r / math.hypot(ta, tb)) if most else np.zeros(2)
                P.append(n * h_n + r * (x + out[0]) + up * (y + out[1]))
                N.append(n)
                place.append((x + out[0], y + out[1]))
    columns, rows = len(across), len(down)
    if reach_n > 0:
        tris = [t for i in range(columns - 1) for j in range(rows - 1)
                for t in (((i * rows + j + 1), (i + 1) * rows + j + 1, (i + 1) * rows + j),
                          ((i * rows + j + 1), (i + 1) * rows + j, i * rows + j))]
    else:
        # Flat, and convex: a fan from its middle to its outline, not the grid, whose inner cells are one plane.
        outline = ([(i, 0) for i in range(columns)] + [(columns - 1, j) for j in range(1, rows)]
                   + [(i, rows - 1) for i in range(columns - 2, -1, -1)] + [(0, j) for j in range(rows - 2, 0, -1)])
        ring = [i * rows + j for i, j in outline]
        middle = len(P)
        P.append(n * h_n)
        N.append(n)
        place.append((0.0, 0.0))
        tris = [(middle, ring[s], ring[(s + 1) % len(ring)]) for s in range(len(ring))]
    place = np.array(place)
    fit = np.stack([(place[:, 0] + h_r) / (2 * h_r), (h_up - place[:, 1]) / (2 * h_up)], axis=1)
    metres = np.stack([place[:, 0], -place[:, 1]], axis=1)
    return mesh(np.array(P), np.array(N), fit, metres, tris)


def planar(centre, n, r, up, half_r, half_up):
    import numpy as np

    n, r, up = (np.array(v, dtype=float) for v in (n, r, up))
    corners = np.array([centre - r * half_r + up * half_up, centre + r * half_r + up * half_up,
                        centre + r * half_r - up * half_up, centre - r * half_r - up * half_up])
    fit = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float)
    metres = np.stack([corners @ r, -(corners @ up)], axis=1)
    return mesh(corners, np.tile(n, (4, 1)), fit, metres, [(0, 1, 2), (0, 2, 3)])


def cylinder(r0: float, r1: float, length: float, count: int, rim: float = 0.0) -> dict:
    """
    Round the z axis in `count` facets, from radius r0 at the foot to r1 at the head; the side's texture starts
    facing south. `rim` rounds both rims of a straight one by that radius.

    <remarks>Built ring by ring along its profile. A rounded rim's quarter arc is split at 45°: the side owns the half
    turned outward, each end the half turned along the axis, and each wears its picture as on the sharp cylinder — the
    side's down the whole length, an end's across the whole diameter — each point at its turn's share of the radius
    past the arc's start. Normals are smooth round the arc.</remarks>
    """
    import numpy as np

    theta = np.linspace(0, 2 * np.pi, count + 1)
    around = np.stack([np.sin(theta), -np.cos(theta), np.zeros_like(theta)], axis=1)
    k = count + 1
    taper = np.array([length, r0 - r1]) / math.hypot(length, r0 - r1)
    steps = round_steps(rim)
    turns = [math.pi / 4 * s / steps for s in range(2 * steps + 1)] if rim else []

    def arc(turn: float, sign: int) -> tuple:
        """A rim's point `turn` from the end's normal toward the side, as (ρ, z, normal ρ, normal z)."""
        return (r1 - rim + rim * math.sin(turn), sign * (length / 2 - rim + rim * math.cos(turn)),
                math.sin(turn), sign * math.cos(turn))

    # The side, head first: (ρ, z, normal ρ, normal z, metres down from the head).
    if rim:
        reach = lambda turn: length / 2 - rim + rim * (math.pi / 2 - turn) / (math.pi / 4)
        head = [arc(t, 1) + (length / 2 - reach(t),) for t in turns if t >= math.pi / 4]
        # Rounded to half its length, the two rims' arcs meet at the middle, which is one ring, not two.
        foot = head[:-1] if rim >= length / 2 else head
        profile = head + [(rho, -z, n_rho, -n_z, length - m) for rho, z, n_rho, n_z, m in reversed(foot)]
    else:
        profile = [(r1, length / 2, *taper, 0.0), (r0, -length / 2, *taper, length)]
    arc_m = theta * (r0 + r1) / 2
    P = np.concatenate([around * rho + [0, 0, z] for rho, z, _, _, _ in profile])
    N = np.concatenate([around * n_rho + [0, 0, n_z] for _, _, n_rho, n_z, _ in profile])
    fit = np.concatenate([np.stack([theta / (2 * np.pi), np.full_like(theta, m / length)], 1) for *_, m in profile])
    metres = np.concatenate([np.stack([arc_m, np.full_like(theta, m)], 1) for *_, m in profile])
    tris = [t for j in range(len(profile) - 1) for i in range(count)
            for t in ((j * k + i, j * k + i + 1, (j + 1) * k + i + 1), (j * k + i, (j + 1) * k + i + 1, (j + 1) * k + i))]
    faces = {"side": mesh(P, N, fit, metres, tris)}
    P, N, fit, metres, tris = [], [], [], [], []
    for radius, sign in ((r1, 1), (r0, -1)):
        if radius <= 0:
            continue
        # Each ring of the end from its middle out: (ρ, z, normal ρ, normal z, ρ its picture is laid at).
        rings = ([arc(t, sign) + (radius - rim + rim * t / (math.pi / 4),) for t in turns if t <= math.pi / 4]
                 if rim else [(radius, sign * length / 2, 0.0, sign, radius)])
        if rim >= radius:
            rings = rings[1:]  # the arc starts at the middle, which is the fan's own
        start = sum(len(p) for p in P)
        z = sign * length / 2
        P.append(np.concatenate([[[0, 0, z]]] + [around[:-1] * rho + [0, 0, zr] for rho, zr, _, _, _ in rings]))
        N.append(np.concatenate([[[0, 0, sign]]] + [around[:-1] * n_rho + [0, 0, n_z] for _, _, n_rho, n_z, _ in rings]))
        flat = np.concatenate([[[0, 0]]] + [around[:-1, :2] * laid for *_, laid in rings]) * [sign, -1]
        fit.append(0.5 + flat / (2 * radius))
        metres.append(flat)
        tris += [(start, start + 1 + i, start + 1 + (i + 1) % count) for i in range(count)]
        for j in range(len(rings) - 1):
            a, b = start + 1 + j * count, start + 1 + (j + 1) * count
            tris += [t for i in range(count)
                     for t in ((a + i, b + i, b + (i + 1) % count), (a + i, b + (i + 1) % count, a + (i + 1) % count))]
    if P:
        faces["ends"] = mesh(*(np.concatenate(v) for v in (P, N, fit, metres)), tris)
    return faces


def sphere(radii, half: bool, count: int):
    """
    Latitude by longitude, `count` facets round; `half` is the dome above the equator alone, open below.

    <remarks>A whole sphere's texture runs round it and from pole to pole, gathered to a point at each. A dome is
    seen from above, where that point would be its middle: its texture lies on it as on a box's top, north up,
    pressed straight down onto it.</remarks>
    """
    import numpy as np

    rings = count // 2
    theta = np.linspace(0, 2 * np.pi, count + 1)
    phi = np.linspace(0, np.pi / 2 if half else np.pi, (rings // 2 if half else rings) + 1)
    t, p = np.meshgrid(theta, phi)
    unit = np.stack([np.sin(p) * np.sin(t), -np.sin(p) * np.cos(t), np.cos(p)], axis=-1).reshape(-1, 3)
    P = unit * radii
    N = unit / radii
    N /= np.linalg.norm(N, axis=1, keepdims=True)
    if half:
        fit = np.stack([0.5 + unit[:, 0] / 2, 0.5 - unit[:, 1] / 2], axis=1)
        metres = np.stack([P[:, 0], -P[:, 1]], axis=1)
    else:
        fit = np.stack([t.ravel() / (2 * np.pi), p.ravel() / phi[-1]], axis=1)
        metres = np.stack([t.ravel() * radii[0], p.ravel() * radii[2]], axis=1)
    k = count + 1
    tris = [tri for j in range(len(phi) - 1) for i in range(count)
            for tri in ((j * k + i, j * k + i + 1, (j + 1) * k + i + 1), (j * k + i, (j + 1) * k + i + 1, (j + 1) * k + i))]
    return mesh(P, N, fit, metres, tris)


def mesh(P, N, fit, metres, tris):
    """Indexed vertices unrolled into per-triangle arrays."""
    import numpy as np

    index = np.array(tris)
    return P[index], N[index], {"fit": fit[index], "m": metres[index]}


def translation(at):
    import numpy as np

    matrix = np.eye(4)
    matrix[:3, 3] = at
    return matrix


def rotation(degrees):
    """About x, then y, then z, each counter-clockwise looking down its axis toward the origin."""
    import numpy as np

    x, y, z = (math.radians(d) for d in degrees)
    rx = np.array([[1, 0, 0], [0, math.cos(x), -math.sin(x)], [0, math.sin(x), math.cos(x)]])
    ry = np.array([[math.cos(y), 0, math.sin(y)], [0, 1, 0], [-math.sin(y), 0, math.cos(y)]])
    rz = np.array([[math.cos(z), -math.sin(z), 0], [math.sin(z), math.cos(z), 0], [0, 0, 1]])
    matrix = np.eye(4)
    matrix[:3, :3] = rz @ ry @ rx
    return matrix


def extent(triangles):
    P = triangles["P"].reshape(-1, 3)
    return P.min(axis=0), P.max(axis=0)
