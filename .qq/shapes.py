"""
Render a model of simple textured shapes into sprites from the game's cameras, view it in a page, and keep a render.

A device, a wall or a prop drawn as a model: a few boxes, cylinders, spheres and flat quads, each face wearing a
texture cut from a remotegen sheet, so the detail lives in the generated textures and the geometry stays simple
enough to write by hand. The model is JSON; its format and the workflow are the shapegen skill
(.claude/skills/shapegen/SKILL.md), its reading and building _shapes.py. Rendering is orthographic and deterministic:
the same model and textures give the same picture.

    qq shapes render .tmp/shapes/any_wall.json                  every view into .tmp/shapes/any_wall/, and _views.png
    qq shapes render MODEL --view=device --cell-px=128          one view
    qq shapes render MODEL --view=device --tilt-deg=55          and beside it a `tilt` view, to set against a drawing
    qq shapes render MODEL --tilt-deg=60 --against=SPRITE.png   the drawing itself on the sheet, scaled to that view
    qq shapes render MODEL --light=parts                        each part coloured and numbered, the faulty ones red
    qq shapes view                                              the viewer follows every save, for up to an hour
    qq shapes view MODEL --once                                 that model alone, written once
    qq shapes keep MODEL --at=devices --view=device --score=4   that render kept as the asset's next variant, with its model
    qq sprites use any_wall-v1 --px=128                         then installed like any variant
    qq shapes library                                           the catalogue's sets and the reuse notes: read before
                                                                a new model or sheet (_shapes_library.py)
    qq shapes library glass tank --kind=material                the catalogue searched, and a contact sheet of it
    qq shapes selftest                                          the rules a model is held to, proved (in qq checks)

One item never stands inside another, and none rests on nothing: every render prints the overlaps between top-level
parts and the items floating, and keep refuses a model with either; what is built into something is grouped with it
(_shapes.overlaps, _shapes.floating). Every face shows its picture at the picture's own proportions (GAM-14): render
prints each face that stretches it, and keep refuses one (_shapes.stretched).

Renders are lit as the game's drawings are — shadowed, occluded, outlined, standing on their deck (_shapes_render).
The views are drawn in parallel, on half the cores; the sheet sets them three to a row, each elevation with a ruler
in metres.

The viewer is .tmp/shapes/viewer.html, opened from disk and kept open: nothing is served. Every render and keep writes
its data again (every draft and kept model), and an open page follows; `view` is for following hand edits. It draws
the triangles this tool builds, so it cannot disagree with a render about the shape (_shapes_view.py).

A kept render's row in variants.jsonl names its model and the texture variants it wore where a cut names its frame, so
`qq sprites trace` and `check` follow every texture to its prompt. A model is kept only when every texture it wears is
a kept variant under raw_assets/.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import time
from pathlib import Path

import _shapes
import _shapes_render
import _shapes_view
import _sim
import sprites
from common import cli, paths

#: What a call may take: `view` watching for its hour; a render is seconds.
TIMEOUT_S = 3600

OUT = _shapes_view.OUT
MODEL_SUFFIX = _shapes_view.MODEL_SUFFIX
#: How often `view` looks at the models' and textures' files, and how long it watches: it stops itself just inside
#: the tool's budget rather than be killed at it.
WATCH_S = 0.5
WATCH_FOR_S = TIMEOUT_S - 30
#: The views sheet: views to a row — few enough that a read, which shrinks a picture past about 2000 px, keeps
#: their pixels — and its spacing, colours and ruler, a tick a decimetre and a number every half metre.
SHEET_COLUMNS = 3
SHEET_GAP_PX, SHEET_LABEL_PX, SHEET_RULER_PX = 16, 14, 30
SHEET_BACKGROUND, SHEET_INK = (58, 58, 58, 255), (220, 220, 220, 255)
SHEET_TICK_M, SHEET_MARK_M = 0.1, 0.5


def main():
    a = parse_args()
    base = _sim.root()
    if a.action == "library":
        import _shapes_library

        out = paths.resolve_in_root(a.out, base).relative_to(base) if a.out else None
        return _shapes_library.library(base, " ".join(a.models), a.in_set, a.kind, a.fits, out)
    if a.action == "selftest":
        import _shapes_selftest

        failed = _shapes_selftest.run()
        for line in failed:
            print(f"  FAIL {line}")
        print(f"{_shapes_selftest.count() - len(failed)} of {_shapes_selftest.count()} model rules hold")
        return 1 if failed else 0
    sources = [model_file(base, m) for m in a.models]
    if a.action == "view":
        return view(base, sources, not a.once)
    if len(sources) != 1:
        cli.fail(f"{a.action} wants one model")
    model = _shapes.load_model(base, sources[0])
    angles = dict(_shapes.VIEWS)
    if a.tilt_deg is not None:
        angles["tilt"] = (0, 90 - a.tilt_deg)
    if a.action == "render":
        views = list(angles) if a.view == "all" else [a.view, *(["tilt"] if a.tilt_deg is not None else [])]
        code = render_views(base, model, views, a, angles)
    else:
        if a.tilt_deg is not None or a.against:
            cli.fail("--tilt-deg and --against are for comparing a render with a drawing; keep renders the game's own "
                     "cameras")
        if a.light == "parts":
            cli.fail("parts light is for reading a model; keep a lit render")
        if a.view == "all":
            cli.fail("keep wants one --view")
        if a.at is None:
            cli.fail("keep wants --at, the folder under assets/ the sprite will have, e.g. devices")
        code = keep(base, sources[0], model, a)
    refresh_viewer(base, sources[0])
    return code


def refresh_viewer(base: Path, source: Path) -> None:
    """The viewer's data written again, so a page left open turns to what was just rendered or kept."""
    found = _shapes_view.default_models(base)
    known = source.resolve() in {f.resolve() for f in found}
    _shapes_view.write(base, found if known else [source, *found], {}, focus=source)
    print(f"viewer: {_sim.rel(base, base / OUT / _shapes_view.PAGE)}")


def model_file(base: Path, value: str) -> Path:
    source = paths.resolve_in_root(value, base)
    if not source.is_file():
        cli.fail(f"no model at {_sim.rel(base, source)}")
    return source


def render_views(base: Path, model: dict, views: list[str], a, angles: dict) -> int:
    from PIL import Image

    triangles = _shapes.build(model)
    out = base / OUT / model["id"]
    out.mkdir(parents=True, exist_ok=True)
    overlaps, floating = _shapes.overlaps(triangles), _shapes.floating(triangles, model)
    alert = {k for k, label in enumerate(triangles["labels"])
             if any(label in o["parts"] for o in overlaps)
             or any(triangles["items"][k] == item for item in floating)}
    rendered = _shapes_render.render_all(triangles, model, {v: angles[v] for v in views}, a.cell_px, a.light,
                                         workers(), alert)
    suffix = "-parts" if a.light == "parts" else ""
    for view_name, picture in rendered.items():
        picture.save(out / f"{view_name}{suffix}.png")
        print(f"  {view_name:<7} {picture.width}x{picture.height}  {_sim.rel(base, out / view_name)}{suffix}.png")
    if a.against:
        sprite = paths.resolve_in_root(a.against, base)
        if not sprite.is_file():
            cli.fail(f"--against: no picture at {_sim.rel(base, sprite)}")
        beside = rendered.get("tilt") or rendered.get("device") or next(iter(rendered.values()))
        with Image.open(sprite) as image:
            image = image.convert("RGBA")
            rendered["sprite"] = image.resize((beside.width, round(image.height * beside.width / image.width)),
                                              Image.Resampling.LANCZOS)
    lo, hi = _shapes.extent(triangles)
    print(f"{len(triangles['P'])} triangles, {', '.join(f'{d} {l:.3f}..{h:.3f} m' for d, l, h in zip('xyz', lo, hi))}")
    print_overlaps(overlaps)
    print_floating(floating)
    print_stretched(_shapes.stretched(triangles, model))
    print_reuse(base, model)
    for n, element in enumerate(triangles["lives"], 1):
        print(f"live {n}: {element['as']} shows {element['show']}  {element['part']}")
    if a.light == "parts":
        print("parts: " + "; ".join(f"{k} {label}" for k, label in enumerate(triangles["labels"])))
    if len(rendered) > 1:
        sheet(rendered).save(out / f"_views{suffix}.png")
        print(f"read {_sim.rel(base, out)}/_views{suffix}.png")
    return 0


def workers() -> int:
    """Processes a render draws its views in: half the cores, so the machine stays usable."""
    import os

    return max(1, (os.cpu_count() or 2) // 2)


def sheet(pictures: dict):
    """
    The views on one sheet, SHEET_COLUMNS to a row so a read keeps their pixels; each named, and an elevation — a view
    looking straight along a model axis — given a ruler in metres along its foot and its left side.
    """
    from PIL import Image, ImageDraw

    names = list(pictures)
    rows = [names[i:i + SHEET_COLUMNS] for i in range(0, len(names), SHEET_COLUMNS)]
    cell_w = [max(pictures[r[c]].width for r in rows if c < len(r)) + SHEET_RULER_PX + SHEET_GAP_PX
              for c in range(min(SHEET_COLUMNS, len(names)))]
    cell_h = [max(pictures[n].height for n in r) + SHEET_RULER_PX + SHEET_LABEL_PX + SHEET_GAP_PX for r in rows]
    page = Image.new("RGBA", (sum(cell_w) + SHEET_GAP_PX, sum(cell_h) + SHEET_GAP_PX), SHEET_BACKGROUND)
    draw = ImageDraw.Draw(page)
    y = SHEET_GAP_PX
    for r, row in enumerate(rows):
        x = SHEET_GAP_PX
        for c, name in enumerate(row):
            picture = pictures[name]
            at = (x + SHEET_RULER_PX, y)
            page.alpha_composite(picture, at)
            ruler(draw, picture, at)
            draw.text((at[0], y + picture.height + SHEET_RULER_PX + 2), name, fill=SHEET_INK)
            x += cell_w[c]
        y += cell_h[r]
    return page


def ruler(draw, picture, at: tuple[int, int]) -> None:
    """Ticks every SHEET_TICK_M along an elevation's foot and left side, numbered every SHEET_MARK_M, in model metres."""
    screen = picture.info.get("screen")
    if not screen:
        return
    for edge, direction in (("foot", screen["right"]), ("side", screen["up"])):
        axis = [k for k, v in enumerate(direction) if abs(v) > 1 - 1e-6]
        if not axis:
            return
        sign = round(direction[axis[0]])
        if edge == "foot":
            start, length, origin = screen["x0"], picture.width, at[0]
        else:
            start, length, origin = -screen["y0"] - picture.height / screen["pxM"], picture.height, at[1]
        first = math.ceil(start / SHEET_TICK_M - 1e-6)
        last = math.floor((start + length / screen["pxM"]) / SHEET_TICK_M + 1e-6)
        for k in range(first, last + 1):
            mark = abs(k * SHEET_TICK_M / SHEET_MARK_M - round(k * SHEET_TICK_M / SHEET_MARK_M)) < 1e-6
            size = 8 if mark else 4
            offset = (k * SHEET_TICK_M - start) * screen["pxM"]
            value = f"{k * SHEET_TICK_M * sign:g}" if mark else None
            if edge == "foot":
                px, py = origin + offset, at[1] + picture.height
                draw.line([(px, py), (px, py + size)], fill=SHEET_INK)
                if value:
                    draw.text((px + 2, py + 6), value, fill=SHEET_INK)
            else:
                py = origin + picture.height - offset
                draw.line([(at[0] - size, py), (at[0], py)], fill=SHEET_INK)
                if value:
                    draw.text((at[0] - SHEET_RULER_PX + 1, py - 12), value, fill=SHEET_INK)


def print_overlaps(found: list[dict]) -> None:
    if not found:
        return
    print(f"{len(found)} overlap(s): one item drawn inside another — move it to stand on or beside the other, or put "
          "both in one group if one is built into the other")
    for o in found:
        print(f"  {o['parts'][0]}  ×  {o['parts'][1]}  ({' × '.join(f'{d:.3f}' for d in o['depthM'])} m)")


def print_floating(found: list[str]) -> None:
    if not found:
        return
    print(f"{len(found)} floating: resting on nothing — stand it on the deck or on another item, against one, or "
          "against the back of the footprint (boundsM's north face, the wall behind)")
    for item in found:
        print(f"  {item}")


def print_stretched(found: list[dict]) -> None:
    if not found:
        return
    print(f"{len(found)} stretched (GAM-14): a face showing its picture past {_shapes.STRETCH_MOST:.0%} off the "
          "picture's proportions — tile it with tileM [across, null], crop it with insetPct [across, down], size the "
          "face to it, or give it a picture of its own")
    for s in found:
        how = f"tileM {s['regionM']}" if s["tiled"] else f"fitted on {s['regionM']} m"
        print(f"  {s['part']} {s['face']}: {s['tex']} {s['pictureAspect']:g}:1, {how}, drawn "
              f"{s['ratio'] if s['ratio'] >= 1 else 1 / s['ratio']:.2f}× too {'wide' if s['ratio'] >= 1 else 'tall'}")


def print_reuse(base: Path, model: dict) -> None:
    """The reuse notes on this model's wear, counted with it standing in for its id (_shapes_library)."""
    import _catalog
    import _shapes_library

    found = _catalog.entries(base)
    unknown = [s for s in model.get("sets", []) if s not in _catalog.sets(base)]
    if unknown:
        print(f"sets not in {_catalog.SETS}: {', '.join(unknown)}")
    standing = {f: m for f, m in _shapes_library.current(base).items() if m["id"] != model["id"]}
    standing["(this render)"] = model
    worn, placed = _shapes_library.usage(standing)
    for note in _shapes_library.reuse_notes(found, standing, worn, placed, only=model["id"]):
        print(f"reuse: {note}")


def catalogue_model(base: Path, home: Path, model: dict, kind: str) -> None:
    """The kept model's entry: its about and its sets written from the model, the rest kept; refused without sets."""
    import _catalog

    path = home / _catalog.ENTRY
    entry = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {"tags": []}
    entry["sets"] = model.get("sets") or entry.get("sets") or []
    if not entry["sets"]:
        cli.fail(f"{model['id']} is in no set: give the model \"sets\" from {_catalog.SETS} (the families it draws "
                 f"from), so the library can tell its reuse")
    unknown = [s for s in entry["sets"] if s not in _catalog.sets(base)]
    if unknown:
        cli.fail(f"sets not in {_catalog.SETS}: {', '.join(unknown)}")
    entry |= {"about": re.sub(r"^A part:\s*", "", model.get("about") or entry.get("about", "")), "kind": kind}
    _catalog.write(base, home.relative_to(base), entry)


def keep(base: Path, source: Path, model: dict, a) -> int:
    """The render kept as the asset's next variant beside a copy of its model, every texture a kept variant."""
    triangles = _shapes.build(model)
    if found := _shapes.overlaps(triangles):
        print_overlaps(found)
        cli.fail("a model with one item inside another is not kept")
    if found := _shapes.floating(triangles, model):
        print_floating(found)
        cli.fail("a model with an item resting on nothing is not kept")
    if found := _shapes.stretched(triangles, model):
        print_stretched(found)
        cli.fail("a model with a picture stretched is not kept (GAM-14)")
    worn = []
    for name, texture in model["textures"].items():
        picture = base / texture["src"]
        if not picture.resolve().is_relative_to((base / sprites.RAW).resolve()):
            cli.fail(f"texture {name} is {texture['src']}: keep it with qq sprites keep and point the model at the "
                     f"kept variant under {sprites.RAW}/")
        if not any(r["variant"] == picture.stem for r in sprites.read_rows(picture.parent / sprites.VARIANTS)):
            cli.fail(f"texture {name}, {texture['src']}, is in no {sprites.VARIANTS}")
        worn.append(_sim.rel(base, picture))
    for src in model["subs"]:
        if not any(r.get("model") == src for r in sprites.read_rows((base / src).parent / sprites.VARIANTS)):
            cli.fail(f"part {src} is not kept: qq shapes keep it --at=parts --view=iso, and place the kept "
                     f"{MODEL_SUFFIX} under {sprites.RAW}/parts/")
    ident = sprites.asset_id(a.ident or model["id"])
    folder = sprites.asset_folder(base, a.at)
    home = base / sprites.RAW / folder / ident
    elsewhere = [p.parent for p in (base / sprites.RAW).rglob(f"{ident}/{sprites.VARIANTS}") if p.parent != home]
    if elsewhere:
        cli.fail(f"{ident} is kept under {_sim.rel(base, elsewhere[0])}: keep it --at that folder")
    home.mkdir(parents=True, exist_ok=True)
    catalogue_model(base, home, model, "part" if folder.as_posix() == "parts" else "device")
    version = 1
    while (home / f"{ident}-v{version}.png").exists():
        version += 1
    variant = f"{ident}-v{version}"
    _shapes_render.render(triangles, model, _shapes.VIEWS[a.view], a.cell_px, a.light).save(
        home / f"{variant}.png")
    shutil.copyfile(source, home / f"{variant}{MODEL_SUFFIX}")
    with (home / sprites.VARIANTS).open("a", encoding="utf-8") as rows:
        rows.write(json.dumps({"variant": variant, "model": _sim.rel(base, home / f"{variant}{MODEL_SUFFIX}"),
                               "view": a.view, "cellPx": a.cell_px, "light": a.light, "textures": worn,
                               "parts": list(model["subs"]),
                               "score": a.score, "status": "candidate", "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}) + "\n")
    print(f"  kept {_sim.rel(base, home / variant)}.png and its model")
    return 0


def catalogue_files(base: Path) -> list[Path]:
    """What the catalogue is read from, beside the models: each entry, each variants list, the sets, the renames."""
    import _catalog

    raw = base / sprites.RAW
    return sorted([*raw.rglob(_catalog.ENTRY), *raw.rglob(sprites.VARIANTS), base / _catalog.SETS,
                   base / _catalog.RENAMED])


def view(base: Path, sources: list[Path], watch: bool) -> int:
    """
    The viewer's data: the models named, else every draft and kept model, and the catalogue. Watching, it is written
    again whenever a model, a texture it reads or the catalogue changes, and an open page follows; it stops itself
    after WATCH_FOR_S.
    """
    print(f"viewer: {_sim.rel(base, base / OUT / _shapes_view.PAGE)} — open it in a browser and leave it open"
          + (", ctrl-c to stop watching" if watch else ""), flush=True)
    reads: dict[Path, list[Path]] = {}
    seen, until = None, time.monotonic() + WATCH_FOR_S
    try:
        while True:
            found = sources or _shapes_view.default_models(base)
            stamp = [(f, f.stat().st_mtime_ns if f.is_file() else 0)
                     for f in [*(f for s in found for f in reads.get(s, [s])), *catalogue_files(base)]]
            if stamp != seen:
                entries = _shapes_view.write(base, found, reads)
                failed = [e for e in entries if "error" in e]
                print(f"{time.strftime('%H:%M:%S')} {len(entries)} model(s)"
                      + "".join(f"\n  {e['file']}: {e['error']}" for e in failed), flush=True)
                seen = [(f, f.stat().st_mtime_ns if f.is_file() else 0)
                        for f in [*(f for s in found for f in reads.get(s, [s])), *catalogue_files(base)]]
            if not watch:
                return 1 if failed else 0
            if time.monotonic() > until:
                print(f"stopped watching after {WATCH_FOR_S // 60} min: run it again to go on")
                return 0
            time.sleep(WATCH_S)
    except KeyboardInterrupt:
        return 0


def parse_args():
    parser = argparse.ArgumentParser(
        prog="qq shapes",
        description="Render a model of simple textured shapes into sprites, view it in a page, and keep a render.",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("action", choices=["render", "view", "keep", "library", "selftest"],
                        help="render: views into .tmp/shapes/<id>/; view: the viewer page; keep: one view as the "
                             "asset's next variant; library: every kept texture and part, who uses it, and a contact "
                             "sheet; selftest: the rules a model is held to, each proved on a fixture")
    parser.add_argument("models", nargs="*",
                        help="the model's JSON file, inside the project; view takes several, or none for every one; "
                             "of library, the words searched for")
    parser.add_argument("--set", dest="in_set", default=None, metavar="SET",
                        help="of library, only that set's (raw_assets/sets.md)")
    parser.add_argument("--kind", default=None, choices=["material", "face", "decal", "part", "device"],
                        help="of library, only that kind")
    parser.add_argument("--fits", default=None, metavar="FACE", help="of library, only textures for that face")
    parser.add_argument("--out", default=None, metavar="MD",
                        help="of library, the page it writes (default .tmp/shapes/library.md)")
    parser.add_argument("--view", default="all", choices=[*_shapes.VIEWS, "all"],
                        help="which camera: device is the game's (GAM-10), the rest check the shape; keep wants one")
    parser.add_argument("--tilt-deg", type=float, default=None, metavar="DEG",
                        help="of render, one more view, `tilt`: the device camera at this tilt from straight down, to "
                             "compare a render with a drawing made from another angle; never kept")
    parser.add_argument("--cell-px", type=cli.counting, default=256, metavar="INT",
                        help="pixels a metre (one grid cell) spans")
    parser.add_argument("--light", default="sun", choices=["sun", "plain", "flat", "parts"],
                        help="sun: lit, shadowed, occluded and outlined, standing on its deck (_shapes_render); plain: "
                             "each face lit by its normal alone; flat: the textures as they are; parts: each part a "
                             "colour of its own and numbered, those overlapping or floating red (render only, into "
                             "<view>-parts.png)")
    parser.add_argument("--against", default=None, metavar="PNG",
                        help="of render, a drawing to set beside the views on the sheet, scaled to the width of the "
                             "tilt view, else the device view")
    parser.add_argument("--once", action="store_true",
                        help="of view, write the data once rather than follow every save for up to an hour")
    parser.add_argument("--at", default=None, metavar="PATH",
                        help="of keep, the folder under assets/ the sprite will have, e.g. devices")
    parser.add_argument("--id", dest="ident", default=None, metavar="ID",
                        help="of keep, the asset id when it is not the model's own, e.g. one view of a kit")
    parser.add_argument("--score", type=int, default=3, choices=range(6), metavar="0-5",
                        help="of keep, how good the render is")
    return parser.parse_args()


if __name__ == "__main__":
    cli.entry(main)
