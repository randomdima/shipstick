"""
A kept model as the game draws it live (GAM-10): its triangles, the textures they wear and the light they are lit by,
written beside its sprite when `qq sprites use` installs a render of it. The client draws them with the renderer's own
passes in the floor's scene (src/app/web/wwwroot/scene.js), so what the page shows is what `qq shapes render` shows.

    assets/devices/<id>.mesh.json   what it is: its variant, frame, looks and their textures, the light, the layout of
    assets/devices/<id>.mesh.bin    its triangles, unrolled: positions and texture coordinates (float32), normals
                                    (int8, of 127), each vertex's part order (uint16) and, with live parts, which one
                                    it is (uint8, from 1; 0 none), each described under `live` in the .mesh.json
    assets/textures/<variant>[-i<inset>|-i<across>x<down>][-seamless].webp  each texture as a face wears it, inset cropped and, when it is
                                    tiled, made seamless; its .src.json names the kept variant it was made from

A face's turn is in its texture coordinates, so one picture serves every turn of it.
"""

from __future__ import annotations

import json
from pathlib import Path

import _shapes
import _shapes_render
import _sim
import sprites

TEXTURES = Path("assets/textures")
MESH_SUFFIX = ".mesh.json"
#: A normal's components are stored as int8 of this.
NORMAL_UNIT = 127


def export(base: Path, row: dict, sprite: Path) -> list[Path]:
    """The kept model a variant's `row` names, written beside its `sprite`: the mesh and every texture it wears."""
    import numpy as np

    model = _shapes.load_model(base, base / row["model"])
    triangles = _shapes.build(model)
    lo, hi = _shapes.bounds(model) or _shapes.extent(triangles)
    written, looks, index = [], [], {}
    remap = []
    for look in triangles["looks"]:
        texture = texture_asset(base, model, look["tex"], written)
        key = (texture, look["tileM"] is not None, round(look["shade"], 4), look["cutout"])
        if key not in index:
            index[key] = len(looks)
            looks.append({"texture": texture, "wrap": key[1], "shade": key[2], "cutout": key[3]})
        remap.append(index[key])
    turns = np.array([look["turn"] for look in triangles["looks"]])[triangles["look"]]
    UV = turned_uv(triangles["UV"], turns)
    count = len(triangles["P"])
    order = np.repeat(triangles["order"], 3).astype(np.uint16)
    look = np.array(remap, dtype=np.uint16)[triangles["look"]]
    # Grouped by what they wear, so each look is one draw; the part order keeps coplanar faces as the file has them.
    by_look = np.argsort(look, kind="stable")
    arrays = {
        "P": triangles["P"][by_look].astype(np.float32).reshape(-1),
        "UV": UV[by_look].astype(np.float32).reshape(-1),
        "N": np.round(triangles["N"][by_look] * NORMAL_UNIT).clip(-NORMAL_UNIT, NORMAL_UNIT).astype(np.int8).reshape(-1),
        "order": order.reshape(count, 3)[by_look].reshape(-1),
    }
    if triangles["lives"]:
        arrays["live"] = np.repeat(triangles["live"], 3).astype(np.uint8).reshape(count, 3)[by_look].reshape(-1)
    layout, blob, offset = {}, bytearray(), 0
    for name, array in arrays.items():
        offset = -(-offset // 4) * 4
        blob.extend(bytes(offset - len(blob)))
        layout[name] = {"offset": offset, "type": str(array.dtype), "length": len(array)}
        blob.extend(array.tobytes())
        offset = len(blob)
    sorted_looks = look[by_look]
    draws = [[int(k), int(np.searchsorted(sorted_looks, k)), int((sorted_looks == k).sum())]
             for k in np.unique(sorted_looks)]
    stem = sprite.with_suffix("")
    stem.with_suffix(".mesh.bin").write_bytes(bytes(blob))
    mesh = {
        "variant": sprite_variant(sprite), "model": row["model"],
        "boundsM": [lo.round(4).tolist(), hi.round(4).tolist()], "triangles": count,
        "bin": stem.with_suffix(".mesh.bin").name, "layout": layout, "looks": looks,
        "draws": draws, "light": light(),
    }
    if triangles["lives"]:
        mesh["live"] = triangles["lives"]
    stem.with_suffix(MESH_SUFFIX).write_text(json.dumps(mesh, indent=1) + "\n", encoding="utf-8")
    return [stem.with_suffix(MESH_SUFFIX), stem.with_suffix(".mesh.bin"), *written]


def sprite_variant(sprite: Path) -> str:
    """The kept render the mesh came with, as its sprite's .src.json names it, so `qq sprites check` traces both."""
    return json.loads(sprite.with_name(sprite.stem + ".src.json").read_text(encoding="utf-8"))["variant"]


def texture_asset(base: Path, model: dict, name: str, written: list[Path]) -> str:
    """The texture `name` as the model's faces wear it, written under assets/textures/ once; its path from the root."""
    from PIL import Image
    import numpy as np

    texture = model["textures"][name]
    across, down = _shapes.inset_pct(texture, name)
    inset = across if across == down else [across, down]
    seamless = "tileM" in texture
    stem = (Path(texture["src"]).stem + (f"-i{across:g}" if across == down else f"-i{across:g}x{down:g}")
            * bool(across or down) + ("-seamless" if seamless else ""))
    path = base / TEXTURES / f"{stem}{sprites.SPRITE}"
    if path not in written:
        picture = (model["images"][name].clip(0, 1) * 255).round().astype(np.uint8)
        sprites.save_for_page(Image.fromarray(picture, "RGBA"), path)
        path.with_name(f"{stem}.src.json").write_text(json.dumps(
            {"variant": texture["src"], "insetPct": inset, "seamless": seamless}, indent=2) + "\n", encoding="utf-8")
        written.append(path)
    return _sim.rel(base, path)


def turned_uv(UV, turns):
    """
    Each vertex's place on the unturned picture: a face turned `turn` degrees clockwise samples its turned picture at
    (u, v), which is the unturned one at these (`_shapes.turned` turns by np.rot90).
    """
    import numpy as np

    u, v = UV[..., 0], UV[..., 1]
    t = (turns % 360)[:, None]
    return np.stack([np.select([t == 90, t == 180, t == 270], [v, 1 - u, 1 - v], u),
                     np.select([t == 90, t == 180, t == 270], [1 - u, 1 - v, u], v)], axis=-1)


def light() -> dict:
    """How the renderer lights a model, for the client to light it the same."""
    import numpy as np

    sun = np.array(_shapes.LIGHT) / np.linalg.norm(_shapes.LIGHT)
    r = _shapes_render
    return {"sun": sun.round(6).tolist(), "ambient": _shapes.AMBIENT, "tiltDeg": _shapes.TILT_DEG,
            "shadowPxM": r.SHADOW_PX_M, "shadowBiasM": r.SHADOW_BIAS_M, "shadowLiftM": r.SHADOW_LIFT_M,
            "shadowKeep": r.SHADOW_KEEP, "aoRadiiM": list(r.AO_RADII_M), "aoDirections": r.AO_DIRECTIONS,
            "aoMarginM": r.AO_MARGIN_M, "aoStrength": r.AO_STRENGTH, "edgeM": r.EDGE_M, "edgeShade": r.EDGE_SHADE,
            "foldCos": r.FOLD_COS, "foldLight": r.FOLD_LIGHT, "grazeCos": r.GRAZE_COS,
            "deckShadowMax": r.DECK_SHADOW_MAX, "deckFadeM": r.DECK_FADE_M, "cutoutAlpha": _shapes.CUTOUT_ALPHA,
            "supersample": r.SUPERSAMPLE}
