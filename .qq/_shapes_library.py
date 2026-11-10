"""
The library `qq shapes library` shows, read before anything new is modelled or briefed: the catalogue of every kept
texture, part and model (_catalog.py), searched by words and filtered by set, kind and face, with who wears or places
each — so a model reuses what is kept wherever it is the same thing in the same role, and a sheet's cells go only to
what nothing kept can be.

    qq shapes library                         the sets and what each holds, and the reuse notes
    qq shapes library steel worktop           the catalogue ranked by those words
    qq shapes library --set=galley --kind=face
                                              every listing also writes `--out` (a page of thumbnails, all fields)
                                              and .tmp/shapes/library.png, a contact sheet of what it lists

Reuse is counted on the models as they stand — each id's installed version, else its newest kept, else its draft —
and named, never refused: a face or a decal worn by more models than its kind's soft cap, a face, decal or part worn
outside every set its model is in, a model in no set, and what nothing wears.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

import _catalog
import _shapes_view
import _sim
import _spend
import sprites

OUT = _shapes_view.OUT / "library.md"
SHEET = _shapes_view.OUT / "library.png"
#: Of the contact sheet: a picture's square, and how many to a row.
THUMB_PX = 200
ACROSS = 6
#: Of a search on stdout: how many rows, and how much of an about each shows (`--out` has all of both).
SHOWN = 25
ABOUT_CHARS = 90
VERSION = re.compile(r"-v(\d+)\.model\.json$")


def library(base: Path, query: str, in_set: str | None, kind: str | None, fits: str | None, out: Path | None) -> int:
    found = _catalog.entries(base)
    known = _catalog.sets(base)
    if in_set and in_set not in known:
        print(f"no set {in_set!r}; the sets are {', '.join(known)}")
        return 1
    standing = current(base)
    worn, placed = usage(standing)
    listed = _catalog.search(found, query, in_set, kind, fits)
    browsing = not (query.strip() or in_set or kind or fits)
    if browsing:
        print_sets(found, known)
        notes = reuse_notes(found, standing, worn, placed, installed=set(_spend.installed(base)))
        print(f"reuse — {len(notes)} note(s); a cap is a trial value (_catalog.WEARERS_SOFT_CAP), a note a question")
        for note in notes:
            print(f"  {note}")
    else:
        print(f"{len(listed)} match(es)" + (f", the first {SHOWN}" if len(listed) > SHOWN else ""))
        for _, entry in listed[:SHOWN]:
            print("  " + row(entry, worn, placed))
    page = base / (out or OUT)
    write_page(base, page, listed, worn, placed, known)
    contact_sheet(base, [e for _, e in listed], worn, placed, base / SHEET)
    print(f"{len(listed)} listed in {_sim.rel(base, page)}; read {_sim.rel(base, base / SHEET)} — search: "
          "qq shapes library WORDS [--set=…] [--kind=…] [--fits=…]")
    missing = _catalog.problems(base)
    if missing:
        print(f"{len(missing)} kept asset(s) not catalogued: qq sprites catalog")
    return 0


def current(base: Path, every: dict[str, dict] | None = None) -> dict[str, dict]:
    """
    Each model id's standing version, by file: the installed one, else the newest kept, else its draft; of `every`
    (`_shapes_view.models`) when the caller has them loaded.
    """
    every = _shapes_view.models(_shapes_view.loaded(base)) if every is None else every
    used = {r["model"] for rows in (base / sprites.RAW).rglob(sprites.VARIANTS) for r in sprites.read_rows(rows)
            if r.get("status") == "used" and "model" in r}
    best: dict[str, tuple] = {}
    for file, model in every.items():
        version = VERSION.search(file)
        rank = (0, 0) if file in used else (1, -int(version[1])) if version else (2, 0)
        if model["id"] not in best or rank < best[model["id"]][0]:
            best[model["id"]] = (rank, file, model)
    return {file: model for _, file, model in best.values()}


def usage(standing: dict[str, dict]) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    """
    Each texture and the models wearing it themselves, and each part and the models placing it. A placed part's
    textures are the part's own wear, counted once, on the part.
    """
    worn: dict[str, set[str]] = {}
    placed: dict[str, set[str]] = {}
    for model in standing.values():
        for name, texture in model["textures"].items():
            if "." not in name:
                worn.setdefault(_spend.texture_id(texture["src"]), set()).add(model["id"])
        for sub in model["subs"].values():
            placed.setdefault(sub["id"], set()).add(model["id"])
    return worn, placed


def sets_of(model: dict, found: dict[str, dict]) -> set[str]:
    """A model's sets: its own `sets`, else its catalogue entry's."""
    return set(model.get("sets") or found.get(model["id"], {}).get("sets", []))


def reuse_notes(found: dict[str, dict], standing: dict[str, dict], worn: dict[str, set[str]],
                placed: dict[str, set[str]], only: str | None = None, installed: set[str] = frozenset()) -> list[str]:
    """
    What reuse is worth a second look; of one model's wear alone when `only` names it. An `installed` asset is used
    by the game itself (the plain crate), so is never worn by nothing.
    """
    notes = []
    for ident, users in sorted(worn.items()) + sorted(placed.items()):
        entry = found.get(ident, {})
        cap = _catalog.WEARERS_SOFT_CAP.get(entry.get("kind"))
        if cap and len(users) > cap and (only is None or only in users):
            notes.append(f"{ident} ({entry['kind']}) is worn by {len(users)} models, past {cap}: "
                         f"{', '.join(sorted(users))}")
    for model in sorted(standing.values(), key=lambda m: m["id"]):
        if only is not None and model["id"] != only:
            continue
        mine = sets_of(model, found)
        if not mine:
            notes.append(f"{model['id']} is in no set: give its model `sets`, or its {_catalog.ENTRY}")
            continue
        uses = {_spend.texture_id(t["src"]) for n, t in model["textures"].items() if "." not in n}
        uses |= {sub["id"] for sub in model["subs"].values()}
        for ident in sorted(uses):
            entry = found.get(ident)
            if entry and entry.get("kind") in ("face", "decal", "part") and not mine & set(entry.get("sets", [])):
                notes.append(f"{model['id']} ({', '.join(sorted(mine))}) wears {ident}, a {entry['kind']} of "
                             f"{', '.join(entry.get('sets', []))}: reuse across sets, or a set to add")
    if only is None:
        for ident, entry in sorted(found.items()):
            if (entry.get("kind") in _catalog.TEXTURE_KINDS + ("part",) and ident not in worn and ident not in placed
                    and ident not in installed):
                notes.append(f"{ident} ({entry.get('kind')}) is worn by nothing")
    return notes


def print_sets(found: dict[str, dict], known: dict[str, str]) -> None:
    print(f"sets — {_catalog.SETS}")
    for ident, about in known.items():
        members = [e for e in found.values() if ident in e.get("sets", [])]
        kinds = {k: sum(e.get("kind") == k for e in members) for k in _catalog.KINDS}
        held = ", ".join(f"{n} {k}" for k, n in kinds.items() if n)
        print(f"  {ident:<14} {len(members):>3}  {held or 'empty'}\n  {'':<14}      {about}")


def use_of(entry: dict, worn: dict[str, set[str]], placed: dict[str, set[str]]) -> str:
    if entry.get("kind") in _catalog.MODEL_KINDS:
        n = len(placed.get(entry["id"], ()))
        return f"placed {n}" if entry["kind"] == "part" else ""
    cap = _catalog.WEARERS_SOFT_CAP.get(entry.get("kind"))
    return f"worn {len(worn.get(entry['id'], ()))}" + (f"/{cap}" if cap else "")


def row(entry: dict, worn: dict[str, set[str]], placed: dict[str, set[str]]) -> str:
    about = entry.get("about", "")
    about = about if len(about) <= ABOUT_CHARS else about[: ABOUT_CHARS - 1] + "…"
    return (f"{entry['id']:<24} {entry.get('kind', '?'):<8} {','.join(entry.get('sets', [])):<22} "
            f"{','.join(entry.get('fits', [])) or '-':<12} {use_of(entry, worn, placed):<10} {about}")


def picture(base: Path, entry: dict) -> Path | None:
    """The variant that stands for the asset: its used one, else its newest."""
    folder = base / entry["folder"]
    rows = sprites.read_rows(folder / sprites.VARIANTS)
    if not rows:
        return None
    chosen = next((r for r in rows if r.get("status") == "used"), rows[-1])
    return folder / f"{chosen['variant']}.png"


def write_page(base: Path, page: Path, listed: list[tuple[float, dict]], worn: dict[str, set[str]],
               placed: dict[str, set[str]], known: dict[str, str]) -> None:
    """The listing as a markdown page, every field, each asset's picture beside it."""
    lines = ["# Asset library", "", f"Sets: {_catalog.SETS}. Made by `qq shapes library`; scratch.", "",
             "| | id | kind | sets | fits | material | use | tags | about |", "|---|---|---|---|---|---|---|---|---|"]
    for _, e in listed:
        shown = picture(base, e)
        image = f"<img src=\"{Path(os.path.relpath(shown, page.parent)).as_posix()}\" width=\"72\">" if shown else ""
        users = sorted(worn.get(e["id"], set()) | placed.get(e["id"], set()))
        cells = [image, f"`{e['id']}`", e.get("kind", ""), ", ".join(e.get("sets", [])), ", ".join(e.get("fits", [])),
                 e.get("material", ""), use_of(e, worn, placed) + (f": {', '.join(users)}" if users else ""),
                 ", ".join(e.get("tags", [])), e.get("about", "")]
        lines.append("| " + " | ".join(c.replace("|", "/") for c in cells) + " |")
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text("\n".join(lines) + "\n", encoding="utf-8")


def contact_sheet(base: Path, listed: list[dict], worn: dict[str, set[str]], placed: dict[str, set[str]],
                  out: Path) -> None:
    from PIL import Image, ImageDraw

    shown = [(p, e) for e in listed if (p := picture(base, e)) and p.is_file()]
    sheet = Image.new("RGB", (ACROSS * THUMB_PX, max(1, -(-len(shown) // ACROSS)) * (THUMB_PX + 30)), (40, 40, 40))
    draw = ImageDraw.Draw(sheet)
    for n, (path, entry) in enumerate(shown):
        x, y = n % ACROSS * THUMB_PX, n // ACROSS * (THUMB_PX + 30)
        with Image.open(path) as image:
            thumb = image.convert("RGBA")
        thumb.thumbnail((THUMB_PX - 8, THUMB_PX - 8))
        sheet.paste(thumb, (x + 4, y + 4), thumb)
        draw.text((x + 4, y + THUMB_PX - 2), entry["id"], fill=(230, 200, 90))
        draw.text((x + 4, y + THUMB_PX + 11), f"{entry.get('kind', '?')} {use_of(entry, worn, placed)}",
                  fill=(160, 160, 160))
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)
