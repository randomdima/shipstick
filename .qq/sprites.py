"""
Cut a generated frame into sprites, keep and use them, and trace a sprite to the prompt that made it.

Art is generated with the remotegen skill, several assets to a frame, drawn on a transparent background and asked in
words. A frame is scratch in .tmp/gen/; what is kept is each asset's cut variant, under raw_assets/ at the path its
sprite has under assets/, with the record of the frame it came from and the pictures that frame was asked from — so
every sprite traces back to its first prompt. The rules are raw_assets/index.md.

    qq sprites cut devices_a-v1                     every drawing found, in the record's `cells` order
    qq sprites cut devices_a-v1 --grid=3x3          the same, split by the sheet's grid where drawings touch
    qq sprites mask devices_a-v1 oxygen_generator   the frame with that drawing transparent, for a remotegen --mask redo
    qq sprites keep devices_a-v1 oxygen_generator food_farm --at=ship/devices --score=4
    qq sprites use oxygen_generator-v1 --px=128     the variant becomes the game's sprite, longest side 128 px
    qq sprites reinstall                            every installed sprite made again from the variant and at the size
                                                    its .src.json records, and its model and textures exported again,
                                                    as `use` writes them now; or those named
    qq sprites trace oxygen_generator               sprite -> variant -> frame -> prompt and inputs
    qq sprites cost oxygen_generator                its share of every billed frame that asked for it, attempts and all
    qq sprites cost                                 every installed sprite's cost, dearest first, and the whole spend
    qq sprites check                                every image under assets/ traces, or is on the legacy list, every
                                                    kept frame is on the spend ledger (_spend.py), and every kept
                                                    texture, part and model is catalogued (_catalog.py)
    qq sprites catalog                              an entry begun for every kept asset lacking one; what is incomplete
    qq sprites catalog tex_a tex_b --kind=face --sets=galley --fits=top --tags=worktop,steel
                                                    those fields set on each (--add-sets, --add-tags add to a list)
    qq sprites rename tex_bench_top tex_worktop_grey
                                                    an asset renamed everywhere it is kept, worn and installed; its
                                                    cost history follows it (raw_assets/_renamed.jsonl)

A drawing is a connected patch of the frame's alpha, patches closer than `JOIN_PX` read as one. They are matched to
`cells` in reading order: rows top to bottom, each row left to right. A frame whose count differs is refused, with the
count found: the eye decides whether the brief or the cut is wrong.

A variant may also be a model's render (`qq shapes keep`): its row names the model and the texture variants it wore in
place of a frame, and `trace` and `check` follow each texture to its own prompt.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import time
from pathlib import Path

import _sim
from common import cli, paths

#: What a call may take: `check` reads every record, `cut` labels a whole frame.
TIMEOUT_S = 120

GEN = Path(".tmp/gen")
FRAMES, INPUTS, INDEX, CUTS = GEN / "frames", GEN / "inputs", GEN / "index.jsonl", GEN / "cuts"
RAW, ASSETS = Path("raw_assets"), Path("assets")
KEPT_FRAMES, KEPT_INPUTS = RAW / "_frames", RAW / "_inputs"
LEGACY = RAW / "legacy.txt"
VARIANTS = "variants.jsonl"
SOURCE = ".src.json"
IMAGES = (".png", ".webp")
#: What the page is given (a sprite, a model's texture): lossy WebP at this quality, its alpha exact. As PNG a page's
#: art is six times the bytes, and a generated picture's grain is past what the eye tells apart at this.
SPRITE = ".webp"
WEBP_QUALITY = 90
#: The stylesheet's own art (`PAGE_ART`) at this: it repeats and slices it, and below this the coder smooths a tile's
#: inside more than the edge it wraps to, a seam `qq fit` finds (GAM-14).
PAGE_ART_QUALITY = 100
#: A model's texture (`TEXTURES`) at this: the floor lights it, shades it and shows it smaller than it is.
TEXTURE_QUALITY = 70
TEXTURES = Path("assets/textures")
#: A device as the game draws it (GAM-10): its model's triangles, beside its sprite (_shapes_mesh).
MESH = ".mesh.json"
#: The page's own art — housings, plates, keys, the sky — shown flat as rendered, never in the floor's scene: a model's
#: render installed here gets no mesh beside it.
PAGE_ART = Path("assets/app/web")
CUT_RECORD = "_cuts.json"

#: Above this alpha a pixel is paint; below it, the glow a model leaves round a drawing on a transparent background.
CUT_ALPHA = 64
#: The cell a frame is labelled in, and how near two patches of paint may be and still be one drawing.
BLOCK_PX = 4
JOIN_PX = 12
#: A patch smaller than this is dust the model left, not a drawing.
DUST_PX = 400
#: Of a grid cut: a patch with at least this share of its paint in one cell belongs to that cell whole (`--whole`).
MOSTLY = 0.85
#: How far past a drawing's box a mask reaches, so a redo has room to draw it differently.
MASK_PAD_PX = 8

ASSET_ID = re.compile(r"^[a-z0-9_]+$")
FRAME_ID = re.compile(r"^[a-z0-9_]+-v\d+$")


def main():
    a = parse_args()
    base = _sim.root()
    if a.action == "cost":
        import _spend

        return _spend.report(base, [asset_id(r) for r in a.refs], a.limit)
    if a.action == "check":
        import _catalog
        import _spend

        problems = audit(base) + _spend.problems(base) + _catalog.problems(base)
        for problem in problems[: a.limit or None]:
            print(problem)
        print(f"{len(problems)} problem(s)" if problems
              else "every image under assets/ traces to its prompt, every kept asset is catalogued")
        return 1 if problems else 0
    if a.action == "catalog":
        return catalog(base, [asset_id(r) for r in a.refs], a)
    if a.action == "reinstall":
        return reinstall(base, [asset_id(r) for r in a.refs])
    if a.action == "rename":
        import _rename

        if len(a.refs) != 2:
            cli.fail("rename wants the asset's id and its new one")
        return _rename.rename(base, asset_id(a.refs[0]), asset_id(a.refs[1]))
    if not a.refs:
        cli.fail(f"{a.action} wants a frame, variant or asset id")
    if a.action == "cut":
        return cut(base, frame_id(a.refs[0]), a.grid, a.whole)
    if a.action == "mask":
        return mask(base, frame_id(a.refs[0]), [asset_id(r) for r in a.refs[1:]])
    if a.action == "keep":
        if a.at is None:
            cli.fail("keep wants --at, the folder under assets/ the sprites will have")
        return keep(base, frame_id(a.refs[0]), [asset_id(r) for r in a.refs[1:]], a.at, a.score)
    if a.action == "use":
        return use(base, frame_id(a.refs[0]), a.px)
    return trace(base, asset_id(a.refs[0]))


def cut(base: Path, frame: str, grid: tuple[int, int] | None, whole: float = MOSTLY) -> int:
    """
    Every drawing of a frame, matched to its record's cells, cropped whole into .tmp/gen/cuts/<frame>/: by the gaps
    between drawings, or by the sheet's `grid` (across, down) when drawings touch across a cell's edge.
    """
    import numpy as np
    from PIL import Image, ImageDraw

    record = frame_record(base, frame)
    cells = record.get("cells")
    if not cells:
        cli.fail(f"{frame}'s record names no cells: ask it with remotegen --cells")
    image = Image.open(base / record["file"]).convert("RGBA")
    pixels = np.asarray(image)
    if grid:
        found = grid_drawings(pixels[..., 3], *grid, whole)
        boxes, owned = [box for box, _ in found], [mask for _, mask in found]
    else:
        boxes, owned = drawings(pixels[..., 3]), None
    out = base / CUTS / frame
    out.mkdir(parents=True, exist_ok=True)
    overlay = image.copy()
    draw = ImageDraw.Draw(overlay)
    if len(boxes) != len(cells):
        for n, (x, y, w, h) in enumerate(boxes, 1):
            draw.rectangle([x, y, x + w - 1, y + h - 1], outline=(255, 0, 0, 255), width=2)
            draw.text((x + 4, y + 4), str(n), fill=(255, 0, 0, 255))
            print(f"  {n:<3} {w}x{h} at {x},{y}")
        overlay.save(out / "_overlay.png")
        cli.fail(f"{frame}: {len(boxes)} drawings found, {len(cells)} cells asked — the boxes are numbered on "
                 f"{_sim.rel(base, out)}/_overlay.png")

    named = {}
    for n, (ident, (x, y, w, h)) in enumerate(zip(cells, boxes)):
        # A grid cut's box may reach into a neighbour's paint; only its own drawing is kept.
        own = image if owned is None else Image.fromarray(np.where(owned[n][..., None], pixels, 0).astype(np.uint8))
        own.crop((x, y, x + w, y + h)).save(out / f"{ident}.png")
        draw.rectangle([x, y, x + w - 1, y + h - 1], outline=(255, 0, 0, 255), width=2)
        draw.text((x + 4, y + 4), ident, fill=(255, 0, 0, 255))
        named[ident] = [x, y, w, h]
        print(f"  {ident:<28} {w}x{h} at {x},{y}")
    overlay.save(out / "_overlay.png")
    (out / CUT_RECORD).write_text(json.dumps({"frame": frame, "grid": list(grid) if grid else None, "boxes": named},
                                             indent=2), encoding="utf-8")
    print(f"{len(named)} cut into {_sim.rel(base, out)}/ — read _overlay.png before keeping any")
    return 0


def drawings(alpha) -> list[tuple[int, int, int, int]]:
    """
    The frame's drawings as pixel boxes (x, y, w, h), in reading order. Labelled on a grid of BLOCK_PX cells grown by
    JOIN_PX, so a drawing whose parts do not touch is still one; each box is then measured on the paint itself.
    """
    import numpy as np

    solid = alpha > CUT_ALPHA
    height, width = solid.shape
    rows, columns = -(-height // BLOCK_PX), -(-width // BLOCK_PX)
    padded = np.zeros((rows * BLOCK_PX, columns * BLOCK_PX), bool)
    padded[:height, :width] = solid
    coarse = padded.reshape(rows, BLOCK_PX, columns, BLOCK_PX).any(axis=(1, 3))

    grown = coarse.copy()
    for _ in range(max(1, JOIN_PX // BLOCK_PX)):
        step = grown.copy()
        step[1:] |= grown[:-1]
        step[:-1] |= grown[1:]
        step[:, 1:] |= grown[:, :-1]
        step[:, :-1] |= grown[:, 1:]
        grown = step

    labels = np.zeros(grown.shape, np.int32)
    count = 0
    for y, x in zip(*np.nonzero(grown)):
        if labels[y, x]:
            continue
        count += 1
        labels[y, x] = count
        pending = [(y, x)]
        while pending:
            cy, cx = pending.pop()
            for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
                if 0 <= ny < rows and 0 <= nx < columns and grown[ny, nx] and not labels[ny, nx]:
                    labels[ny, nx] = count
                    pending.append((ny, nx))

    boxes = []
    for label in range(1, count + 1):
        mine = np.repeat(np.repeat((labels == label) & coarse, BLOCK_PX, 0), BLOCK_PX, 1)[:height, :width] & solid
        if mine.sum() < DUST_PX:
            continue
        ys, xs = np.nonzero(mine)
        boxes.append((int(xs.min()), int(ys.min()), int(xs.max() - xs.min() + 1), int(ys.max() - ys.min() + 1)))
    return reading_order(boxes)


def grid_drawings(alpha, across: int, down: int, whole: float = MOSTLY) -> list[tuple[tuple[int, int, int, int], object]]:
    """
    The frame's drawings by the sheet's own grid, `across` by `down` cells in reading order: a patch of paint with at
    least `whole` of it in one cell goes whole to that cell, so a drawing that overflows its cell stays whole, and any
    other patch — two drawings touching across a cell's edge — is split along that edge. Each is (box, mask of its
    paint). A sheet of drawings taller than their cells wants a lower `whole`.
    """
    import numpy as np

    solid = alpha > CUT_ALPHA
    height, width = solid.shape
    rows, columns = -(-height // BLOCK_PX), -(-width // BLOCK_PX)
    padded = np.zeros((rows * BLOCK_PX, columns * BLOCK_PX), bool)
    padded[:height, :width] = solid
    coarse = padded.reshape(rows, BLOCK_PX, columns, BLOCK_PX).any(axis=(1, 3))
    ys, xs = np.mgrid[0:rows, 0:columns] * BLOCK_PX
    cell_of = (np.minimum(ys * down // height, down - 1) * across + np.minimum(xs * across // width, across - 1))

    labels = patches(coarse)
    owner = np.full(coarse.shape, -1, np.int32)
    for label in range(1, int(labels.max()) + 1):
        mine = labels == label
        cells, counts = np.unique(cell_of[mine], return_counts=True)
        owner[mine] = cells[counts.argmax()] if counts.max() >= whole * counts.sum() else cell_of[mine]

    found = []
    for cell in range(across * down):
        mine = np.repeat(np.repeat(owner == cell, BLOCK_PX, 0), BLOCK_PX, 1)[:height, :width] & solid
        if mine.sum() < DUST_PX:
            continue
        ys_, xs_ = np.nonzero(mine)
        box = (int(xs_.min()), int(ys_.min()), int(xs_.max() - xs_.min() + 1), int(ys_.max() - ys_.min() + 1))
        found.append((box, mine))
    return found


def patches(blocks):
    """The connected patches of a block grid, each its own label, 0 where there is no paint."""
    import numpy as np

    labels = np.zeros(blocks.shape, np.int32)
    count = 0
    rows, columns = blocks.shape
    for y, x in zip(*np.nonzero(blocks)):
        if labels[y, x]:
            continue
        count += 1
        labels[y, x] = count
        pending = [(y, x)]
        while pending:
            cy, cx = pending.pop()
            for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
                if 0 <= ny < rows and 0 <= nx < columns and blocks[ny, nx] and not labels[ny, nx]:
                    labels[ny, nx] = count
                    pending.append((ny, nx))
    return labels


def reading_order(boxes: list[tuple[int, int, int, int]]) -> list[tuple[int, int, int, int]]:
    """Rows top to bottom, each left to right: a box whose middle sits inside a row's height is in that row."""
    rows: list[list[tuple[int, int, int, int]]] = []
    for box in sorted(boxes, key=lambda b: b[1] + b[3] / 2):
        middle = box[1] + box[3] / 2
        if rows and min(b[1] for b in rows[-1]) <= middle <= max(b[1] + b[3] for b in rows[-1]):
            rows[-1].append(box)
        else:
            rows.append([box])
    return [box for row in rows for box in sorted(row)]


def mask(base: Path, frame: str, idents: list[str]) -> int:
    """The frame with those drawings' boxes transparent: the --mask a remotegen redo of them is asked with."""
    from PIL import Image

    if not idents:
        cli.fail("mask wants the ids of the drawings to redo")
    boxes = cut_boxes(base, frame, idents)
    image = Image.open(base / frame_record(base, frame)["file"]).convert("RGBA")
    alpha = image.getchannel("A").point(lambda _: 255)
    for x, y, w, h in boxes.values():
        alpha.paste(0, (max(0, x - MASK_PAD_PX), max(0, y - MASK_PAD_PX), x + w + MASK_PAD_PX, y + h + MASK_PAD_PX))
    out = base / CUTS / frame / f"_mask_{'_'.join(idents)}.png"
    Image.merge("RGBA", (*Image.new("RGB", image.size).split(), alpha)).save(out)
    print(_sim.rel(base, out))
    return 0


def keep(base: Path, frame: str, idents: list[str], at: str, score: int) -> int:
    """Each cut kept as its asset's next variant, with the frame's record and every picture it was asked from."""
    if not idents:
        cli.fail("keep wants the ids of the drawings worth keeping")
    folder = asset_folder(base, at)
    # An asset's variants all live in one folder, or `use` cannot tell which is meant.
    for ident in idents:
        elsewhere = [p.parent for p in (base / RAW).rglob(f"{ident}/{VARIANTS}") if p.parent != base / RAW / folder / ident]
        if elsewhere:
            cli.fail(f"{ident} is kept under {_sim.rel(base, elsewhere[0])}: keep it --at that folder")
    boxes = cut_boxes(base, frame, idents)
    grid = json.loads((base / CUTS / frame / CUT_RECORD).read_text(encoding="utf-8")).get("grid")
    for ident in idents:
        home = base / RAW / folder / ident
        home.mkdir(parents=True, exist_ok=True)
        version = 1
        while (home / f"{ident}-v{version}.png").exists():
            version += 1
        variant = f"{ident}-v{version}"
        shutil.copyfile(base / CUTS / frame / f"{ident}.png", home / f"{variant}.png")
        with (home / VARIANTS).open("a", encoding="utf-8") as rows:
            rows.write(json.dumps({"variant": variant, "frame": frame, "box": boxes[ident], "grid": grid, "score": score,
                                   "status": "candidate", "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}) + "\n")
        print(f"  kept {_sim.rel(base, home / variant)}.png")
    keep_lineage(base, frame)
    import _catalog

    textures = RAW / folder == _catalog.TEXTURES
    begun = [ident for ident in idents if textures and begin_entry(base, base / RAW / folder / ident)]
    if begun:
        print(f"catalogue them: qq sprites catalog {' '.join(begun)} --kind=… --sets=… --material=… --fits=… "
              f"--tags=… (qq sprites check fails until each is complete)")
    return 0


def catalog(base: Path, idents: list[str], a) -> int:
    """
    The catalogue's entries begun where missing, then the fields asked set on each id named; with no ids, every kept
    asset lacking an entry gets one begun. Prints what is still incomplete.
    """
    import _catalog

    folders = {f.name: f for f in _catalog.wanted(base)}
    if not idents:
        begun = [f.name for f in folders.values() if begin_entry(base, f)]
        print(f"{len(begun)} entr{'y' if len(begun) == 1 else 'ies'} begun" + (f": {', '.join(begun)}" if begun else ""))
    unknown = [i for i in idents if i not in folders]
    if unknown:
        cli.fail(f"not a kept texture, part or model: {', '.join(unknown)}")
    for ident in idents:
        begin_entry(base, folders[ident])
        path = folders[ident] / _catalog.ENTRY
        entry = json.loads(path.read_text(encoding="utf-8"))
        for key in ("about", "kind", "material"):
            if getattr(a, key) is not None:
                entry[key] = getattr(a, key)
        for key in ("sets", "fits", "tags"):
            if getattr(a, key) is not None:
                entry[key] = listed(getattr(a, key))
        for key in ("sets", "tags"):
            if getattr(a, f"add_{key}") is not None:
                entry[key] = list(dict.fromkeys(entry.get(key, []) + listed(getattr(a, f"add_{key}"))))
        _catalog.write(base, folders[ident].relative_to(base), entry)
    problems = _catalog.problems(base)
    if idents:
        problems = [p for p in problems if any(f"/{i}/" in p or p.startswith(f"{folders[i].relative_to(base)}:")
                                               for i in idents)]
    for problem in problems[: a.limit or None]:
        print(problem)
    print(f"{len(problems)} incomplete" if problems else "catalogued")
    return 1 if problems else 0


def listed(value: str) -> list[str]:
    return [v.strip() for v in value.split(",") if v.strip()]


def begin_entry(base: Path, folder: Path) -> bool:
    """
    An entry begun for a kept asset that has none: its about from the brief line its first variant was asked with, or
    from its model's about; a part's or a model's kind. False when it has one.
    """
    import _catalog

    if (folder / _catalog.ENTRY).is_file():
        return False
    rows = read_rows(folder / VARIANTS)
    entry: dict = {"about": "", "sets": [], "tags": []}
    kind = _catalog.kind_of(base, folder)
    if kind:
        entry["kind"] = kind
    modelled = next((r for r in reversed(rows) if "model" in r), None)
    if modelled:
        about = json.loads((base / modelled["model"]).read_text(encoding="utf-8")).get("about", "")
        entry["about"] = re.sub(r"^A part:\s*", "", about)
    elif rows:
        names = _catalog.renamed(base)
        record = frame_record(base, rows[0]["frame"])
        record = record | {"cells": [names.get(c, c) for c in record.get("cells") or []]}
        entry["about"] = _catalog.brief_lines(record).get(folder.name, "")
    _catalog.write(base, folder.relative_to(base), entry)
    return True


def keep_lineage(base: Path, frame: str) -> None:
    """The frame's record into raw_assets/_frames/, its inputs into _inputs/, and the same for any frame it was edited from."""
    pending, seen = [frame], set()
    while pending:
        ident = pending.pop()
        if ident in seen:
            continue
        seen.add(ident)
        record = frame_record(base, ident)
        (base / KEPT_FRAMES).mkdir(parents=True, exist_ok=True)
        (base / KEPT_FRAMES / f"{ident}.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
        for given in record.get("inputs", []):
            name = f"{given['sha']}.{given['ext']}"
            kept = base / KEPT_INPUTS / name
            if not kept.exists():
                kept.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(base / INPUTS / name, kept)
            if given.get("frame"):
                pending.append(given["frame"])


def use(base: Path, variant: str, px: int) -> int:
    """A kept variant made the game's sprite under assets/, with the .src.json that traces it."""
    from PIL import Image

    found = sorted((base / RAW).rglob(f"{variant}.png"))
    if len(found) != 1:
        cli.fail(f"{len(found)} kept variants named {variant}: expected one under {RAW}/")
    picture = found[0]
    ident = variant.rsplit("-v", 1)[0]
    folder = picture.parent.parent.relative_to(base / RAW)
    sprite = base / ASSETS / folder / f"{ident}{SPRITE}"

    image = Image.open(picture)
    if px:
        scale = px / max(image.size)
        image = image.resize((max(1, round(image.width * scale)), max(1, round(image.height * scale))),
                             Image.Resampling.LANCZOS)
    install(base, image, sprite, picture)

    rows = picture.parent / VARIANTS
    marked, used = [], None
    for row in read_rows(rows):
        row["status"] = "used" if row["variant"] == variant else ("candidate" if row["status"] == "used" else row["status"])
        used = row if row["variant"] == variant else used
        marked.append(json.dumps(row))
    rows.write_text("\n".join(marked) + "\n", encoding="utf-8")
    print(f"{_sim.rel(base, sprite)} {image.width}x{image.height} from {variant}")
    mesh = sprite.with_name(f"{ident}{MESH}")
    if used and "model" in used and not sprite.resolve().is_relative_to((base / PAGE_ART).resolve()):
        import _shapes_mesh

        written = _shapes_mesh.export(base, used, sprite)
        print(f"{_sim.rel(base, written[0])}, the model the game draws, and {len(written) - 2} texture(s) under "
              f"{_shapes_mesh.TEXTURES}/")
    elif mesh.is_file():
        mesh.unlink()
        mesh.with_suffix("").with_suffix(".mesh.bin").unlink(missing_ok=True)
    return 0


def save_for_page(image, path: Path) -> None:
    """`image` written as the page is given it (`SPRITE`), at the quality of where it is drawn."""
    path.parent.mkdir(parents=True, exist_ok=True)
    under = lambda folder: path.resolve().is_relative_to((_sim.root() / folder).resolve())
    quality = PAGE_ART_QUALITY if under(PAGE_ART) else TEXTURE_QUALITY if under(TEXTURES) else WEBP_QUALITY
    image.convert("RGBA").save(path, "WEBP", quality=quality, alpha_quality=100, method=6)


def install(base: Path, image, sprite: Path, picture: Path) -> None:
    """`image`, made from the kept variant `picture`, as the sprite at `sprite`, with the .src.json that traces it."""
    save_for_page(image, sprite)
    for older in IMAGES:
        if older != SPRITE:
            sprite.with_suffix(older).unlink(missing_ok=True)
    sprite.with_name(f"{sprite.stem}{SOURCE}").write_text(json.dumps(
        {"variant": _sim.rel(base, picture), "px": list(image.size)}, indent=2) + "\n", encoding="utf-8")


def reinstall(base: Path, idents: list[str]) -> int:
    """
    Every installed sprite, or those of `idents`, made again from its variant at the size its .src.json records, and
    the model the game draws beside one exported again with its textures — what a change to how `use` writes either
    needs.
    """
    from PIL import Image
    import _shapes_mesh

    sources = [s for s in sorted((base / ASSETS).rglob(f"*{SOURCE}"))
               if (not idents or s.name[: -len(SOURCE)] in idents) and "px" in json.loads(s.read_text(encoding="utf-8"))]
    if idents and len(sources) != len(idents):
        cli.fail(f"{len(sources)} installed sprites for {len(idents)} ids")
    models = 0
    for source in sources:
        named = json.loads(source.read_text(encoding="utf-8"))
        picture = base / named["variant"]
        image = Image.open(picture)
        if list(image.size) != named["px"]:
            image = image.resize(tuple(named["px"]), Image.Resampling.LANCZOS)
        sprite = source.with_name(source.name[: -len(SOURCE)] + SPRITE)
        install(base, image, sprite, picture)
        if sprite.with_name(sprite.stem + MESH).is_file():
            row = next(r for r in read_rows(picture.parent / VARIANTS) if r["variant"] == picture.stem)
            _shapes_mesh.export(base, row, sprite)
            models += 1
    print(f"{len(sources)} sprite(s) made again as {SPRITE}, {models} with the model the game draws")
    return 0


def trace(base: Path, ident: str) -> int:
    """Sprite, variant, frame, and the frame's prompt and inputs — and any frame it was edited from, the same way."""
    sources = sorted((base / ASSETS).rglob(f"{ident}{SOURCE}"))
    if not sources:
        cli.fail(f"no {ident}{SOURCE} under {ASSETS}/")
    source = json.loads(sources[0].read_text(encoding="utf-8"))
    print(f"sprite   {_sim.rel(base, sources[0].with_name(ident + SPRITE))}  {source.get('px')}")
    trace_variant(base, base / source["variant"], "", set())
    return 0


def trace_variant(base: Path, picture: Path, indent: str, shown: set[str]) -> None:
    """
    A variant and where it came from: a cut's frames back to the first prompt, or a model render's every texture.
    A frame already `shown` is named, not printed again.
    """
    row = next((r for r in read_rows(picture.parent / VARIANTS) if r["variant"] == picture.stem), None)
    if row is None:
        cli.fail(f"{_sim.rel(base, picture)} is in no {VARIANTS}")
    if "model" in row:
        print(f"{indent}variant  {_sim.rel(base, picture)}  score {row['score']}, {row['status']}, "
              f"{row['view']} view at {row['cellPx']} px a cell")
        print(f"{indent}model    {row['model']}")
        for part in row.get("parts", []):
            print(f"{indent}part     {part}")
        for texture in row["textures"]:
            trace_variant(base, base / texture, indent + "  ", shown)
        return
    print(f"{indent}variant  {_sim.rel(base, picture)}  score {row['score']}, {row['status']}, box {row['box']}")
    frame = row["frame"]
    while frame:
        if frame in shown:
            print(f"{indent}frame    {frame}  (above)")
            return
        shown.add(frame)
        record = json.loads((base / KEPT_FRAMES / f"{frame}.json").read_text(encoding="utf-8"))
        print(f"{indent}frame    {frame}  {record['op']} {record['model']} {json.dumps(record.get('settings'))} "
              f"${record.get('costUsd')}")
        print(f"{indent}prompt   {record['prompt']}")
        parent = None
        for given in record.get("inputs", []):
            print(f"{indent}input    {given['role']}: {KEPT_INPUTS}/{given['sha']}.{given['ext']}  (was {given['was']})")
            parent = given.get("frame") or parent
        frame = parent


def audit(base: Path) -> list[str]:
    """
    Every image under assets/ that traces to nothing: no .src.json and not on the legacy list, a .src.json naming a
    variant that is gone, a variant no record lists, a record whose frame or inputs were not kept. `qq checks` runs it.
    """
    legacy = set()
    if (base / LEGACY).is_file():
        legacy = {line.strip() for line in (base / LEGACY).read_text(encoding="utf-8").splitlines()
                  if line.strip() and not line.startswith("#")}
    problems = []
    for image in sorted(p for p in (base / ASSETS).rglob("*") if p.suffix in IMAGES):
        where = _sim.rel(base, image)
        source = image.with_name(image.stem + SOURCE)
        if not source.is_file():
            if where not in legacy:
                problems.append(f"{where}: no {source.name} and not on {LEGACY}")
            continue
        problems += variant_problems(base, where, base / json.loads(source.read_text(encoding="utf-8"))["variant"])
    for found in sorted((base / ASSETS).rglob(f"*{MESH}")):
        where, mesh = _sim.rel(base, found), json.loads(found.read_text(encoding="utf-8"))
        problems += variant_problems(base, where, base / mesh["variant"])
        if not found.with_name(mesh["bin"]).is_file():
            problems.append(f"{where}: its triangles {mesh['bin']} are gone")
        problems += [f"{where}: its texture {t} is gone" for t in {look["texture"] for look in mesh["looks"]}
                     if not (base / t).is_file()]
    return problems


def variant_problems(base: Path, where: str, picture: Path) -> list[str]:
    """What breaks one variant's trace: the variant itself, its row, then its frame's lineage or its model's textures."""
    if not picture.is_file():
        return [f"{where}: its variant {_sim.rel(base, picture)} is gone"]
    row = next((r for r in read_rows(picture.parent / VARIANTS) if r["variant"] == picture.stem), None)
    if row is None:
        return [f"{where}: {picture.stem} is in no {VARIANTS}"]
    if "model" not in row:
        return lineage_problems(base, where, row["frame"])
    found = [] if (base / row["model"]).is_file() else [f"{where}: its model {row['model']} is gone"]
    found += [f"{where}: its part {part} is gone" for part in row.get("parts", []) if not (base / part).is_file()]
    for texture in row["textures"]:
        found += variant_problems(base, where, base / texture)
    return found


def lineage_problems(base: Path, where: str, frame: str) -> list[str]:
    """What is missing from one frame's kept lineage, and its parents'."""
    record_path = base / KEPT_FRAMES / f"{frame}.json"
    if not record_path.is_file():
        return [f"{where}: frame {frame} has no record under {KEPT_FRAMES}/"]
    found = []
    for given in json.loads(record_path.read_text(encoding="utf-8")).get("inputs", []):
        if not (base / KEPT_INPUTS / f"{given['sha']}.{given['ext']}").is_file():
            found.append(f"{where}: input {given['sha']} of {frame} is not under {KEPT_INPUTS}/")
        if given.get("frame"):
            found += lineage_problems(base, where, given["frame"])
    return found


def frame_record(base: Path, frame: str) -> dict:
    """A frame's record, newest first: the scratch index, then the kept records."""
    if (base / INDEX).is_file():
        for line in reversed((base / INDEX).read_text(encoding="utf-8").splitlines()):
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if record.get("id") == frame:
                return record
    kept = base / KEPT_FRAMES / f"{frame}.json"
    if kept.is_file():
        return json.loads(kept.read_text(encoding="utf-8"))
    cli.fail(f"no record of frame {frame} in {INDEX} or {KEPT_FRAMES}/")


def cut_boxes(base: Path, frame: str, idents: list[str]) -> dict[str, list[int]]:
    """The boxes `cut` found for those ids; the frame is cut first or refused."""
    record = base / CUTS / frame / CUT_RECORD
    if not record.is_file():
        cli.fail(f"{frame} is not cut yet: qq sprites cut {frame}")
    boxes = json.loads(record.read_text(encoding="utf-8"))["boxes"]
    missing = [ident for ident in idents if ident not in boxes]
    if missing:
        cli.fail(f"{frame} drew no {', '.join(missing)}; it drew {', '.join(boxes)}")
    return {ident: boxes[ident] for ident in idents}


def read_rows(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def asset_folder(base: Path, at: str) -> Path:
    """`--at` as a folder under assets/, refused if it climbs out."""
    target = paths.resolve_in_root(base / ASSETS / at, base / ASSETS)
    return target.relative_to(base / ASSETS)


def asset_id(value: str) -> str:
    if not ASSET_ID.match(value):
        cli.fail(f"{value!r} is not an asset id (lowercase, digits, underscores)")
    return value


def frame_id(value: str) -> str:
    if not FRAME_ID.match(value):
        cli.fail(f"{value!r} is not a frame or variant id like devices_a-v1")
    return value


def parse_args():
    parser = argparse.ArgumentParser(
        prog="qq sprites",
        description="Cut a generated frame into sprites, keep and use them, and trace a sprite to its prompt.",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("action", choices=["cut", "mask", "keep", "use", "reinstall", "trace", "cost", "check", "catalog",
                                           "rename"],
                        help="what to do (the module's docstring has one line of each)")
    parser.add_argument("refs", nargs="*",
                        help="a frame id then asset ids (cut, mask, keep), a variant id (use), an asset id (trace), "
                             "asset ids or none (reinstall, cost, catalog), an asset id and its new id (rename)")
    parser.add_argument("--kind", default=None, metavar="KIND",
                        help="of catalog: material, face or decal for a texture (_catalog.KINDS)")
    parser.add_argument("--sets", default=None, metavar="A,B", help="of catalog: the sets, replacing any")
    parser.add_argument("--add-sets", default=None, metavar="A,B", help="of catalog: sets added to those it has")
    parser.add_argument("--material", default=None, metavar="WORD", help="of catalog: a texture's material")
    parser.add_argument("--fits", default=None, metavar="A,B",
                        help="of catalog: the faces a texture is for, e.g. top,front,door,side,trim,any")
    parser.add_argument("--tags", default=None, metavar="A,B", help="of catalog: search words, replacing any")
    parser.add_argument("--add-tags", default=None, metavar="A,B", help="of catalog: search words added")
    parser.add_argument("--about", default=None, metavar="TEXT", help="of catalog: what it is, in plain words")
    parser.add_argument("--at", default=None, metavar="PATH",
                        help="of keep, the folder under assets/ the sprites will have, e.g. ship/devices")
    parser.add_argument("--score", type=int, default=3, choices=range(6), metavar="0-5",
                        help="of keep, how good the drawing is")
    parser.add_argument("--px", type=cli.counting, default=0, metavar="INT",
                        help="of use, the sprite's longest side in pixels (0 = as cut)")
    parser.add_argument("--limit", type=cli.counting, default=40, metavar="INT",
                        help="of check, max problems to print; of cost, max sprites (0 = no limit)")
    parser.add_argument("--grid", type=grid_type, default=None, metavar="CxR",
                        help="of cut, the sheet's grid, e.g. 3x3: drawings that touch across a cell's edge are split "
                             "along it, each patch of paint going to the cell holding most of it")
    parser.add_argument("--whole", type=share_type, default=MOSTLY, metavar="0-1",
                        help="of a grid cut, the share of a patch's paint in one cell that keeps it whole there; lower "
                             "it for drawings that overflow their cells")
    return parser.parse_args()


def share_type(value: str) -> float:
    share = float(value)
    if not 0.5 < share <= 1:
        raise argparse.ArgumentTypeError(f"expected a share above 0.5 and at most 1: got {value!r}")
    return share


def grid_type(value: str) -> tuple[int, int]:
    if not (m := re.fullmatch(r"([1-9]\d*)x([1-9]\d*)", value)):
        raise argparse.ArgumentTypeError(f"expected columns x rows, like 3x3: got {value!r}")
    return int(m[1]), int(m[2])


if __name__ == "__main__":
    cli.entry(main)
