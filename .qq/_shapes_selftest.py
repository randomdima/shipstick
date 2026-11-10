"""
The rules `qq shapes` holds a model to, each proved on a model built in memory, so a change to the tool that loosens
one fails `qq checks` instead of letting the next model through. `qq shapes selftest` prints them.

A rule here is one the shapegen skill states (.claude/skills/shapegen/SKILL.md, "Textures", "Getting it right", "Parts"
and "Live parts").
"""

from __future__ import annotations

import _shapes
from common import cli


def box(name: str, at: list[float], size: list[float]) -> dict:
    return {"shape": "box", "name": name, "atM": at, "sizeM": size, "tex": "t"}


#: The fixtures' pictures and their pixels after inset: `t` square, `wide` twice as wide as tall.
PICTURE_PX = {"t": (512, 512), "cup.t": (512, 512), "gauge.t": (512, 512), "wide": (1024, 512)}


def model(parts: list[dict], subs: dict | None = None) -> dict:
    images = _shapes.Pictures()
    images.sizes |= PICTURE_PX
    return {"id": "fixture", "textures": {name: {"src": "fixture"} for name in PICTURE_PX}, "parts": parts,
            "subs": subs or {}, "images": images}


TOP = box("table top", [1, 0.35, 0.475], [2, 0.7, 0.05])
PLANK = box("plank", [0.5, 0.5, 0.25], [0.4, 0.1, 0.5]) | {"rotDeg": [0, 0, 45]}
CUP = {"id": "cup", "parts": [{"shape": "group", "name": "cup", "parts": [
    {"shape": "cylinder", "name": "body", "atM": [0, 0, 0.05], "radiusM": 0.04, "lengthM": 0.1, "tex": "t"},
    box("handle", [0.045, 0, 0.05], [0.02, 0.01, 0.06])]}]}

#: Each case: what it shows, the model, how many overlaps the check must find.
CASES = [
    ("a table top run into the seat behind it is one thing inside another",
     model([TOP, box("seat cushion", [1, 0.81, 0.46], [1.76, 0.3, 0.08])]), 1),
    ("a seat standing clear of the table is not",
     model([TOP, box("seat cushion", [1, 0.85, 0.46], [1.76, 0.28, 0.08])]), 0),
    ("a tray resting on the top only touches it",
     model([TOP, box("tray", [0.4, 0.3, 0.515], [0.46, 0.25, 0.03])]), 0),
    ("a decal 2 mm off its face only touches it",
     model([box("wall", [0.5, 0.5, 0.25], [1, 0.84, 0.44]), box("vent", [0.5, 0.075, 0.2], [0.3, 0.012, 0.14])]), 0),
    ("a handle sunk into its body in one group is one assembly",
     model([{"shape": "group", "name": "mug", "parts": [
         {"shape": "cylinder", "name": "body", "atM": [0, 0, 0.05], "radiusM": 0.05, "lengthM": 0.1, "tex": "t"},
         box("arm", [0.06, 0, 0.05], [0.03, 0.01, 0.01])]}]), 0),
    ("the same handle as a separate item is inside the body",
     model([{"shape": "cylinder", "name": "body", "atM": [0, 0, 0.05], "radiusM": 0.05, "lengthM": 0.1, "tex": "t"},
            box("arm", [0.06, 0, 0.05], [0.03, 0.01, 0.01])]), 1),
    ("a placed part's own joins are its own, and it may stand on the table",
     model([TOP, {"shape": "model", "name": "cup", "src": "cup.json", "atM": [1.5, 0.3, 0.5]}], {"cup.json": CUP}), 0),
    ("a placed part sunk into the table is inside it, each of its pieces named",
     model([TOP, {"shape": "model", "name": "cup", "src": "cup.json", "atM": [1.5, 0.3, 0.46]}], {"cup.json": CUP}), 2),
    ("a box beside a plank set at 45° is judged by the plank, not the square round it",
     model([PLANK, box("block", [0.62, 0.38, 0.25], [0.1, 0.1, 0.1])]), 0),
    ("the same box moved onto the plank is inside it",
     model([PLANK, box("block", [0.55, 0.45, 0.25], [0.1, 0.1, 0.1])]), 1),
]

STAND = box("stand", [0.5, 0.5, 0.4], [0.4, 0.4, 0.8])
MIRROR = box("mirror", [0.5, 0.985, 1.1], [0.4, 0.03, 0.3])

#: Each case: what it shows, the model, the items the floating check must name.
FLOATING_CASES = [
    ("a cup on the table, the table on the deck: nothing floats",
     model([TOP | {"atM": [1, 0.35, 0.025]}, box("cup", [1, 0.35, 0.1], [0.08, 0.08, 0.1])]), []),
    ("a cup a centimetre over the table floats",
     model([TOP | {"atM": [1, 0.35, 0.025]}, box("cup", [1, 0.35, 0.11], [0.08, 0.08, 0.1])]), ["parts[1] (cup)"]),
    ("a box leaning on the side of another stands",
     model([STAND, box("gauge", [0.75, 0.5, 0.6], [0.1, 0.1, 0.1])]), []),
    ("a mirror against the back of the footprint hangs on the wall",
     model([STAND, MIRROR]) | {"boundsM": [[0, 0, 0], [1, 1, 1.3]]}, []),
    ("the same mirror a centimetre short of the wall floats",
     model([STAND, MIRROR | {"atM": [0.5, 0.975, 1.1]}]) | {"boundsM": [[0, 0, 0], [1, 1, 1.3]]}, ["parts[1] (mirror)"]),
    ("without boundsM there is no wall to hang on",
     model([STAND, MIRROR]), ["parts[1] (mirror)"]),
    ("a bevelled box left open below still stands on the deck",
     model([box("crate", [0.5, 0.5, 0.2], [0.4, 0.4, 0.4]) | {"bevelM": 0.02, "faces": {"*": "t", "bottom": None}}]),
     []),
    ("a cup resting only on a floating shelf floats with it",
     model([box("shelf", [0.5, 0.5, 1], [0.3, 0.2, 0.02]), box("cup", [0.5, 0.5, 1.06], [0.08, 0.08, 0.1])]),
     ["parts[0] (shelf)", "parts[1] (cup)"]),
]


NEEDLE = {"shape": "group", "name": "needle", "atM": [0.5, 0.5, 0.5], "rotDeg": [0, 0, 90],
          "live": {"as": "needle", "show": "input", "facing": "up"},
          "parts": [box("pointer", [0, 0.05, 0], [0.01, 0.1, 0.002])]}
GAUGE = {"id": "gauge", "parts": [NEEDLE | {"atM": [0, 0, 0]}]}

#: Each case: what it shows, the model, its live parts as (as, show), or a word of the error that refuses it.
LIVE_CASES = [
    ("a needle on a turned group turns about its own facing, round the group's origin",
     model([NEEDLE]), [("needle", "input")]),
    ("a lamp repeated is one lamp; a needle repeated is one each",
     model([box("lamp", [0.1, 0.1, 0.1], [0.05, 0.05, 0.05]) | {"live": {"as": "lamp", "show": "state"},
                                                                  "repeat": {"count": 3, "stepM": [0.1, 0, 0]}},
            NEEDLE | {"repeat": {"count": 2, "stepM": [0.2, 0, 0]}}]),
     [("lamp", "state"), ("needle", "input"), ("needle", "input")]),
    ("a placed part's needle shows what the placing model says",
     model([{"shape": "model", "name": "gauge", "src": "gauge.json", "atM": [0.5, 0.5, 0.5], "live": {"show": "cycle"}}],
           {"gauge.json": GAUGE}), [("needle", "cycle")]),
    ("a lamp shows a state, not a share", model([box("lamp", [0, 0, 0], [0.1, 0.1, 0.1]) | {"live": {"as": "lamp",
                                                                                                   "show": "input"}}]),
     "shows"),
    ("a live part inside another is refused",
     model([{"shape": "group", "name": "panel", "live": {"as": "glow", "show": "run"}, "parts": [NEEDLE]}]), "inside"),
    ("a fill wants the way it grows", model([box("bar", [0, 0, 0], [0.4, 0.05, 0.01]) | {"live": {"as": "fill",
                                                                                                  "show": "held"}}]),
     "toward"),
    ("a stroke wants how far it travels", model([box("arm", [0, 0, 0], [0.2, 0.05, 0.05]) | {"live": {
        "as": "stroke", "show": "run", "toward": "north", "periodS": 2}}]), "strokeM"),
]


def quad(size: list[float], face) -> dict:
    return {"shape": "quad", "name": "panel", "atM": [0.5, 0, 0.5], "sizeM": size, "faces": {"face": face}}


def board(depth_m: float) -> dict:
    return box("board", [0.5, 0.5, 0.1], [0.4, depth_m, 0.2]) | {"tex": "wide"}


#: A mug's side: 0.06 m round, so 0.377 m about and 0.1 m along.
MUG_SIDE = {"shape": "cylinder", "name": "mug", "atM": [0.5, 0.5, 0.05], "radiusM": 0.06, "lengthM": 0.1}

#: Each case: what it shows, the model, the faces the stretch check must name as (part, face) (GAM-14).
STRETCH_CASES = [
    ("a square picture fitted on a square face keeps its proportions", model([quad([0.5, 0.5], "t")]), []),
    ("a square picture fitted on a face twice as wide is stretched", model([quad([1, 0.5], "t")]),
     [("parts[0] (panel)", "face")]),
    ("a wide picture turned a quarter fits a tall face", model([quad([0.5, 1], {"tex": "wide", "turnDeg": 90})]), []),
    ("tiled at the picture's proportions it keeps them on any face",
     model([quad([1, 0.3], {"tex": "wide", "tileM": [0.4, 0.2]})]), []),
    ("a square tileM on a wide picture stretches it", model([quad([1, 1], {"tex": "wide", "tileM": 0.5})]),
     [("parts[0] (panel)", "face")]),
    ("tileM down null takes the picture's proportions", model([quad([1, 1], {"tex": "wide", "tileM": [0.5, None]})]),
     []),
    ("a side tiled once round and once along is stretched",
     model([MUG_SIDE | {"faces": {"side": {"tex": "t", "tileM": [0.377, 0.1]}, "ends": "t"}}]),
     [("parts[0] (mug)", "side")]),
    ("a side tiled once round, down null, keeps the picture's proportions",
     model([MUG_SIDE | {"faces": {"side": {"tex": "t", "tileM": [0.377, None]}, "ends": "t"}}]), []),
    ("a decal's 4 mm edges are edges, not faces that show a picture", model([board(0.004)]), []),
    ("a board's 2 cm edges wearing its picture fitted are stretched", model([board(0.02)]),
     [("parts[0] (board)", f) for f in ("east", "west", "top", "bottom")]),
]


CRATE = box("crate", [0.5, 0.5, 0.2], [0.6, 0.4, 0.4])
DRUM = {"shape": "cylinder", "name": "drum", "atM": [0.5, 0.5, 0.3], "radiusM": 0.25, "lengthM": 0.6, "tex": "t"}

#: Each case: what it shows, the part, the most triangles it may take (ROUND_STEPS_MOST holds the cost).
ROUND_CASES = [
    ("a box rounded 1 cm, a step to each half arc", CRATE | {"roundM": 0.01}, 108),
    ("a box rounded 5 cm, at most two", CRATE | {"roundM": 0.05}, 300),
    ("a box rounded past its half-size, all round on that axis", CRATE | {"roundM": 0.5}, 300),
    ("a slab rounded along z, its top a rounded rectangle", CRATE | {"roundM": 0.08, "roundAlong": "z"}, 80),
    ("a slab rounded along x on a part turned about z", CRATE | {"roundM": 0.03, "roundAlong": "x",
                                                                 "rotDeg": [0, 0, 30]}, 80),
    ("a slab rounded along z to its half-depth, its ends half discs", CRATE | {"roundM": 0.5, "roundAlong": "z"}, 80),
    ("a drum with rounded rims", DRUM | {"roundM": 0.04}, None),
    ("a drum rounded past half its length", DRUM | {"roundM": 0.25, "lengthM": 0.3}, None),
]


def round_found(part: dict, most: int | None) -> list[str]:
    """
    What is wrong with a rounded part's triangles: a gap (an edge of a triangle not shared by exactly two), an extent
    other than the sharp part's, a normal not of unit length or turned inward, or more triangles than `most`.
    """
    import numpy as np

    rounded, sharp = (_shapes.build(model([p])) for p in (part, {k: v for k, v in part.items()
                                                                if k not in ("roundM", "roundAlong")}))
    P, N = rounded["P"], rounded["N"]
    found = []
    corners = np.round(P, 6)
    edges: dict = {}
    for tri in corners:
        for a, b in ((0, 1), (1, 2), (2, 0)):
            key = tuple(sorted((tuple(tri[a]), tuple(tri[b]))))
            if key[0] != key[1]:
                edges[key] = edges.get(key, 0) + 1
    open_edges = sum(1 for c in edges.values() if c != 2)
    if open_edges:
        found.append(f"{open_edges} edge(s) not shared by two triangles")
    extent = [np.ptp(t["P"].reshape(-1, 3), axis=0) for t in (rounded, sharp)]
    if not np.allclose(*extent, atol=1e-6):
        found.append(f"extent {extent[0].round(4)}, the sharp part's {extent[1].round(4)}")
    if not np.allclose(np.linalg.norm(N, axis=2), 1, atol=1e-6):
        found.append("a normal not of unit length")
    centre = P.reshape(-1, 3).mean(axis=0)
    if ((P - centre) * N).sum(axis=2).min() < -1e-9:
        found.append("a normal turned inward")
    if most is not None and len(P) > most:
        found.append(f"{len(P)} triangles, past {most}")
    return found


def count() -> int:
    return len(CASES) + len(FLOATING_CASES) + len(LIVE_CASES) + len(STRETCH_CASES) + len(ROUND_CASES)


def run() -> list[str]:
    """Each case that does not hold, with what was found."""
    failed = []
    for what, fixture, expected in CASES:
        found = _shapes.overlaps(_shapes.build(fixture))
        if len(found) != expected:
            failed.append(f"{what}: {len(found)} overlap(s) found, {expected} expected — "
                          + "; ".join(" × ".join(o["parts"]) for o in found))
    for what, fixture, expected in FLOATING_CASES:
        found = _shapes.floating(_shapes.build(fixture), fixture)
        if found != expected:
            failed.append(f"{what}: floating {found}, {expected} expected")
    for what, fixture, expected in LIVE_CASES:
        try:
            lives = _shapes.build(fixture)["lives"]
            found = [(e["as"], e["show"]) for e in lives]
        except cli.Failure as e:
            found = str(e)
        if isinstance(expected, str) and not (isinstance(found, str) and expected in found) or \
                not isinstance(expected, str) and found != expected:
            failed.append(f"{what}: {found}, {expected!r} expected")
    for what, fixture, expected in STRETCH_CASES:
        found = sorted((s["part"], s["face"]) for s in _shapes.stretched(_shapes.build(fixture), fixture))
        if found != sorted(expected):
            failed.append(f"{what}: stretched {found}, {sorted(expected)} expected")
    for what, part, most in ROUND_CASES:
        found = round_found(part, most)
        if found:
            failed.append(f"{what}: {'; '.join(found)}")
    turned = _shapes.build(model([NEEDLE]))["lives"][0]
    if turned["axis"] != [0.0, 0.0, 1.0] or turned["pivotM"] != [0.5, 0.5, 0.5]:
        failed.append(f"a turned needle's axis and pivot: {turned['axis']} round {turned['pivotM']}, up round its origin "
                      f"expected")
    return failed
