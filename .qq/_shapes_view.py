"""
The data `qq shapes` writes for its viewer page, the asset catalogue: every catalogued asset with its use, history and
billing (_shapes_catalog.py), and every model as the page draws it with everything known about it — the textures it
wears and the prompt each came from, its parts as written, where it was kept and installed, its renders, and what it
cost (_spend.py).

The page (`_shapes_viewer.html`, copied to .tmp/shapes/viewer.html) is opened from disk. It loads viewer-data.js, then
reads viewer-stamp.js every second and loads the data again when the stamp moves, so any write here reaches an open
page. The data describes every model; what is heavy — a model's triangles, each texture's picture — is a script of
its own under viewer-cache/, named by its content, written once and loaded only when the page shows that model.
Textures go in as data URIs, since WebGL refuses a picture read from another file; everything the page only shows is
linked by its path relative to the page.
"""

from __future__ import annotations

import base64
import hashlib
import io
import json
import math
import shutil
import time
from pathlib import Path

import _shapes
import _shapes_mesh
import _sim
import _spend
import sprites
from common import cli

OUT = Path(".tmp/shapes")
PAGE, DATA, STAMP, CACHE = "viewer.html", "viewer-data.js", "viewer-stamp.js", "viewer-cache"
TEMPLATE = Path(__file__).with_name("_shapes_viewer.html")
MODEL_SUFFIX = ".model.json"


def default_models(base: Path) -> list[Path]:
    """Every draft under .tmp/shapes/ and every kept model under raw_assets/."""
    return sorted((base / OUT).glob("*.json")) + sorted((base / sprites.RAW).rglob(f"*{MODEL_SUFFIX}"))


def loaded(base: Path, sources: list[Path] | None = None) -> dict[str, dict | Exception]:
    """
    Every draft and kept model, by its file, or the `sources` named: the model, or why it failed to load. The
    failures are the viewer's to report; `models` leaves them out.
    """
    found = {}
    for source in default_models(base) if sources is None else sources:
        try:
            found[_sim.rel(base, source)] = _shapes.load_model(base, source)
        except (cli.Failure, OSError) as e:
            found[_sim.rel(base, source)] = e
    return found


def models(found: dict[str, dict | Exception]) -> dict[str, dict]:
    """Of `loaded`, the models that load."""
    return {file: model for file, model in found.items() if isinstance(model, dict)}


def wearers(models: dict[str, dict]) -> dict[str, list[tuple[str, str]]]:
    """
    Each texture picture, by path, and each model wearing it as (model id, texture name in it): a part's own file is
    no wearer while another model places it — the placing model wears its textures, as `<part>.<name>`.
    """
    parts = {src for model in models.values() for src in model["subs"]}
    worn: dict[str, set[tuple[str, str]]] = {}
    for file, model in models.items():
        if file in parts:
            continue
        for name, texture in model["textures"].items():
            worn.setdefault(texture["src"], set()).add((model["id"], name))
    return {src: sorted(found) for src, found in worn.items()}


def write(base: Path, sources: list[Path], reads: dict[Path, list[Path]], focus: Path | None = None) -> list[dict]:
    """
    The page, its data and the stamp an open page watches; `reads` learns the files each model reads. The data is
    every model and the catalogue (_shapes_catalog.py); `focus` is a model just rendered or kept, which an open page
    turns to. What viewer-cache/ holds that the data no longer names is deleted.
    """
    import _shapes_catalog

    out = base / OUT
    cache = out / CACHE
    cache.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(TEMPLATE, out / PAGE)
    every = loaded(base)
    named = {_sim.rel(base, s): s for s in sources}
    found = {file: every[file] for file in named if file in every} | loaded(base, [s for f, s in named.items()
                                                                                    if f not in every])
    spend = _spend.spend(base)
    used: set[str] = set()
    entries = [entry(base, named[file], found[file], reads, spend, used) for file in named]
    for stale in cache.iterdir():
        if stale.name not in used:
            stale.unlink()
    stamp = time.time()
    sun = [c / math.hypot(*_shapes.LIGHT) for c in _shapes.LIGHT]
    data = {"stamp": stamp, "models": entries, "views": _shapes.VIEWS, "sun": sun, "ambient": _shapes.AMBIENT,
            "cutoutAlpha": _shapes.CUTOUT_ALPHA, "catalog": _shapes_catalog.data(base, every, spend, url),
            "focus": _sim.rel(base, focus) if focus else None}
    (out / DATA).write_text(f"shapesData({json.dumps(data, separators=(',', ':'))});\n", encoding="utf-8")
    (out / STAMP).write_text(f"shapesStamp({stamp});\n", encoding="utf-8")
    return entries


def entry(base: Path, source: Path, model: dict | Exception, reads: dict[Path, list[Path]], spend: tuple,
          used: set[str]) -> dict:
    """
    One model as the page draws and describes it, and its cost from `spend` (`_spend.spend`); or the file and why
    it failed. Its triangles and pictures are written to the cache if not there already, and named into `used`.
    """
    import numpy as np

    found = {"file": _sim.rel(base, source)}
    try:
        if isinstance(model, Exception):
            raise model
        text = source.read_text(encoding="utf-8")
        reads[source] = model["files"] + [base / _spend.SPEND]
        triangles = _shapes.build(model)
        frame = _shapes.bounds(model)
    except (cli.Failure, OSError) as e:
        return found | {"error": str(e)}

    names = list(model["textures"])
    images, looks, index, remap = {}, [], {}, []
    for look in triangles["looks"]:
        image = picture_script(base, model, look["tex"], used)
        images[image["key"]] = image["src"]
        key = (image["key"], look["tileM"] is not None, look["shade"], look["cutout"])
        if key not in index:
            index[key] = len(looks)
            looks.append({"image": key[0], "wrap": key[1], "shade": key[2], "cutout": key[3],
                          "tex": names.index(look["tex"])})
        remap.append(index[key])
    turns = np.array([look["turn"] for look in triangles["looks"]])[triangles["look"]]
    geometry = geometry_script(base, {
        "P": triangles["P"].astype(np.float32), "N": triangles["N"].astype(np.float32),
        "UV": _shapes_mesh.turned_uv(triangles["UV"], turns).astype(np.float32),
        "look": np.array(remap, np.uint16)[triangles["look"]], "part": triangles["order"].astype(np.uint16)}, used)
    lo, hi = _shapes.extent(triangles)
    newest = max(f.stat().st_mtime for f in model["files"])
    frames: dict[str, dict] = {}
    return found | {
        "id": model["id"], "about": model.get("about", ""), "source": text,
        "extent": [lo.round(4).tolist(), hi.round(4).tolist()],
        "bounds": [c.tolist() for c in frame] if frame else None,
        "parts": triangles["labels"], "specs": [spec_of(s) for s in triangles["specs"]],
        "overlaps": _shapes.overlaps(triangles), "floating": _shapes.floating(triangles, model),
        "stretched": _shapes.stretched(triangles, model),
        "looks": looks, "images": images, "geometry": geometry, "triangles": len(triangles["P"]),
        "textures": [texture_info(base, model, name, triangles, frames) for name in names],
        "frames": frames, "kept": kept_info(base, model["id"]), "renders": renders(base, model["id"], newest),
        "cost": _spend.model_cost(base, model["id"], [t["src"] for t in model["textures"].values()], spend),
    }


def picture_script(base: Path, model: dict, name: str, used: set[str]) -> dict:
    """
    The texture `name` as a script under the cache that hands the page its data URI, written only if no picture of
    the same identity (`_shapes.Pictures.identity`) is there: its key and its path from the page.
    """
    key = "i-" + hashlib.sha1(repr(model["images"].identity(name)).encode()).hexdigest()[:20]
    path = base / OUT / CACHE / f"{key}.js"
    if not path.is_file():
        uri = data_uri(model["images"][name])
        path.write_text(f"shapesImage({json.dumps(key)},{json.dumps(uri)});\n", encoding="utf-8")
    used.add(path.name)
    return {"key": key, "src": f"{CACHE}/{path.name}"}


def geometry_script(base: Path, arrays: dict, used: set[str]) -> dict:
    """
    A model's triangles as a script under the cache that hands the page each array, base64 of its bytes, named by
    their content so an unchanged model is written and loaded once: its key and its path from the page.
    """
    blob = hashlib.sha1()
    for name, array in arrays.items():
        blob.update(name.encode() + str(array.dtype).encode() + array.tobytes())
    key = "g-" + blob.hexdigest()[:20]
    path = base / OUT / CACHE / f"{key}.js"
    if not path.is_file():
        encoded = {name: {"type": str(array.dtype), "b64": base64.b64encode(array.tobytes()).decode("ascii")}
                   for name, array in arrays.items()}
        path.write_text(f"shapesGeometry({json.dumps(key)},{json.dumps(encoded)});\n", encoding="utf-8")
    used.add(path.name)
    return {"key": key, "src": f"{CACHE}/{path.name}"}


def spec_of(part: dict) -> dict:
    """A part as written, a group's own parts left out: they are listed as parts of their own."""
    return {k: v for k, v in part.items() if k != "parts"}


def texture_info(base: Path, model: dict, name: str, triangles: dict, frames: dict) -> dict:
    """What one texture is, where its picture came from, and which faces wear it and how."""
    from PIL import Image

    texture = model["textures"][name]
    picture = base / texture["src"]
    with Image.open(picture) as image:
        size = list(image.size)
    used = [{"part": look["part"], "face": look["face"], "turnDeg": look["turn"], "tileM": look["tileM"],
             "shade": round(look["shade"], 3)} for look in triangles["looks"] if look["tex"] == name]
    return {"name": name, "asset": _spend.texture_id(texture["src"]), "src": texture["src"], "url": url(base, picture),
            "px": size,
            "insetPct": texture.get("insetPct", 0), "tileM": texture.get("tileM"), "cutout": bool(texture.get("cutout")),
            "used": used, "from": provenance(base, picture, frames)}


def provenance(base: Path, picture: Path, frames: dict) -> dict:
    """
    Where a texture's picture came from: a kept variant's row, or a cut still in scratch; and the frame either was cut
    from, into `frames`, with the cell it drew.
    """
    rel = _sim.rel(base, picture)
    found: dict = {}
    if rel.startswith(f"{sprites.RAW}/"):
        row = next((r for r in sprites.read_rows(picture.parent / sprites.VARIANTS) if r["variant"] == picture.stem),
                   None)
        if row is None:
            return {"kind": "kept picture in no variants.jsonl"}
        found = {"kind": "kept", "variant": row["variant"], "score": row["score"], "status": row["status"],
                 "frame": row.get("frame")}
    elif rel.startswith(f"{sprites.CUTS}/"):
        found = {"kind": "draft cut, not kept", "frame": picture.parent.name}
    else:
        return {"kind": "not generated: traces to nothing"}
    frame = found.get("frame")
    if frame and frame not in frames:
        try:
            record = sprites.frame_record(base, frame)
        except cli.Failure:
            record = None
        frames[frame] = {"op": record["op"], "model": record["model"], "settings": record.get("settings"),
                         "costUsd": record.get("costUsd"), "prompt": record["prompt"], "cells": record.get("cells"),
                         "inputs": [f"{i['role']}: {i['was']}" for i in record.get("inputs", [])]} if record else None
    record = frames.get(frame) if frame else None
    if record and record.get("cells") and picture.stem.rsplit("-v", 1)[0] in record["cells"]:
        found["cell"] = record["cells"].index(picture.stem.rsplit("-v", 1)[0]) + 1
    return found


def kept_info(base: Path, ident: str) -> list[dict]:
    """Every kept render of this id: its row, its picture, and the sprite under assets/ it was installed as, if any."""
    kept = []
    for rows in sorted((base / sprites.RAW).rglob(f"{ident}/{sprites.VARIANTS}")):
        installed = {}
        for source in (base / sprites.ASSETS).rglob(f"{ident}{sprites.SOURCE}"):
            named = json.loads(source.read_text(encoding="utf-8"))
            sprite = source.with_name(f"{ident}{sprites.SPRITE}")
            installed[named["variant"]] = {"path": _sim.rel(base, sprite), "url": url(base, sprite), "px": named.get("px")}
        for row in sprites.read_rows(rows):
            picture = rows.parent / f"{row['variant']}.png"
            kept.append({"variant": row["variant"], "score": row["score"], "status": row["status"],
                         "view": row.get("view"), "cellPx": row.get("cellPx"), "model": row.get("model"),
                         "ts": row.get("ts"), "url": url(base, picture),
                         "installed": installed.get(_sim.rel(base, picture))})
    return kept


def renders(base: Path, ident: str, newest: float) -> list[dict]:
    """The views last rendered into .tmp/shapes/<id>/, each marked stale if the model or a texture changed since."""
    folder = base / OUT / ident
    if not folder.is_dir():
        return []
    return [{"view": p.stem, "url": url(base, p), "stale": p.stat().st_mtime < newest}
            for p in sorted(folder.glob("*.png"), key=lambda p: (p.stem != "_views", p.stem))]


def url(base: Path, path: Path) -> str:
    """A file's address from the page, with its time so a changed picture is fetched again."""
    return f"../../{_sim.rel(base, path)}?{int(path.stat().st_mtime)}"


def data_uri(picture) -> str:
    """The picture as the game's page gets it: WebP at the mesh export's quality, its alpha exact."""
    from PIL import Image

    buffer = io.BytesIO()
    Image.fromarray((picture.clip(0, 1) * 255).round().astype("uint8"), "RGBA").save(
        buffer, "WEBP", quality=sprites.WEBP_QUALITY, alpha_quality=100)
    return "data:image/webp;base64," + base64.b64encode(buffer.getvalue()).decode("ascii")
