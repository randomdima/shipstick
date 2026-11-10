"""
What the art cost. Every billed call is a line of `raw_assets/_spend.jsonl`, appended by remotegen as it is billed and
committed, so an attempt nothing was kept from still counts after `.tmp/` is wiped.

A frame's cost is shared evenly by the cells it asked. Of an asset, three figures:

- **all time** — its share of every frame that asked for it (each attempt of a sheet, each sheet it was briefed in
  again) and, of a model, of every frame that asked for a texture it wears; the retries among them priced apart.
- **current** — only the frames the variant as it stands came from: a drawing's one frame, or the frame each texture
  a model wears was cut from.
- **reusable** — a texture worn by more than one model (each model's standing version, `_shapes_library.current`):
  its current cost split evenly between them, the asset's `amortizedUsd`.

`qq sprites cost` prints them; `qq shapes`' catalogue page shows them on every asset's billing tab.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import _sim
import sprites

SPEND = sprites.RAW / "_spend.jsonl"
ATTEMPT = re.compile(r"^(?P<sheet>.+)-v(?P<n>\d+)$")


def ledger(base: Path) -> list[dict]:
    """
    Every billed call, oldest first, each with the sheet it was asked under and which attempt of it it was; its cells
    by the ids their assets have now, so a renamed asset keeps its history (the ledger itself is never edited).
    """
    import _catalog

    names = _catalog.renamed(base)
    return [row | dict(zip(("sheet", "attempt"), attempt(row["frame"])))
            | {"cells": [names.get(c, c) for c in row.get("cells") or []]} for row in sprites.read_rows(base / SPEND)]


def attempt(frame: str) -> tuple[str, int]:
    """remotegen numbers a sheet's frames from 1: every one past the first is a retry."""
    m = ATTEMPT.match(frame)
    return (m["sheet"], int(m["n"])) if m else (frame, 1)


def kept_by_frame(base: Path) -> dict[str, list[dict]]:
    """Every kept variant cut from each frame: its asset, variant and status."""
    kept: dict[str, list[dict]] = {}
    for rows in (base / sprites.RAW).rglob(sprites.VARIANTS):
        for row in sprites.read_rows(rows):
            if row.get("frame"):
                kept.setdefault(row["frame"], []).append(
                    {"asset": rows.parent.name, "variant": row["variant"], "status": row["status"]})
    return kept


def wearers(base: Path, models: dict[str, dict] | None = None) -> dict[str, list[str]]:
    """
    Each texture and the ids of the models wearing it, a placed part's through the model placing it; of each model's
    standing version (`_shapes_library.current`), or of `models` when the caller has them chosen.
    """
    import _shapes_library
    import _shapes_view

    if models is None:
        models = _shapes_library.current(base)
    worn: dict[str, set[str]] = {}
    for src, found in _shapes_view.wearers(models).items():
        worn.setdefault(texture_id(src), set()).update(ident for ident, _ in found)
    return {t: sorted(ids) for t, ids in worn.items()}


def spend(base: Path, models: dict[str, dict] | None = None) -> tuple[list[dict], dict, dict]:
    """What every figure here is worked from: the ledger, what was kept of each frame, who wears each texture."""
    return ledger(base), kept_by_frame(base), wearers(base, models)


def share(row: dict) -> float:
    cells = row.get("cells") or []
    return (row.get("costUsd") or 0) / len(cells) if cells else 0.0


def history(ident: str, rows: list[dict], kept: dict[str, list[dict]]) -> list[dict]:
    """Each billed frame that asked for the asset, with its share and what was kept of the asset from it."""
    return [row | {"shareUsd": share(row), "kept": [k for k in kept.get(row["frame"], []) if k["asset"] == ident]}
            for row in rows if ident in (row.get("cells") or [])]


def texture_id(src: str) -> str:
    """The asset a texture's picture is a variant or a draft cut of."""
    return re.sub(r"-v\d+$", "", Path(src).stem)


def picture_frame(base: Path, src: str) -> str | None:
    """The frame a kept variant or a draft cut was cut from."""
    picture = base / src
    if _sim.rel(base, picture).startswith(f"{sprites.CUTS}/"):
        return picture.parent.name
    row = next((r for r in sprites.read_rows(picture.parent / sprites.VARIANTS) if r["variant"] == picture.stem), None)
    return row.get("frame") if row else None


def cost(ident: str, pieces: list[tuple[str, str | None]], drawn_from: str | None, spent: tuple) -> dict:
    """
    The asset's all-time, current and amortized cost. `pieces` are a model's textures, each with the frame its worn
    picture was cut from; `drawn_from` is the frame a drawing's current variant was cut from.
    """
    rows, kept, worn = spent
    own = history(ident, rows, kept)
    textures = []
    for texture, frame in dict.fromkeys(pieces):
        frames = history(texture, rows, kept)
        now = sum(r["shareUsd"] for r in frames if r["frame"] == frame)
        wearing = sorted(set(worn.get(texture, [])) | {ident})
        textures.append({"texture": texture, "frames": frames, "allTimeUsd": sum(r["shareUsd"] for r in frames),
                         "frame": frame, "currentUsd": now, "wornBy": wearing, "amortizedUsd": now / len(wearing)})
    every = own + [r for t in textures for r in t["frames"]]
    retried = [r for r in every if r["attempt"] > 1]
    drawn = sum(r["shareUsd"] for r in own if r["frame"] == drawn_from)
    return {"asset": ident, "drawnFrom": drawn_from, "frames": own, "textures": textures,
            "allTimeUsd": sum(r["shareUsd"] for r in every), "count": len(every),
            "retries": len(retried), "retryUsd": sum(r["shareUsd"] for r in retried),
            "ownUsd": sum(r["shareUsd"] for r in own),
            "currentUsd": drawn + sum(t["currentUsd"] for t in textures),
            "amortizedUsd": drawn + sum(t["amortizedUsd"] for t in textures),
            "reused": [t["texture"] for t in textures if len(t["wornBy"]) > 1]}


def model_cost(base: Path, ident: str, srcs: list[str], spent: tuple) -> dict:
    return cost(ident, [(texture_id(s), picture_frame(base, s)) for s in srcs], None, spent)


def sprite_cost(base: Path, ident: str, spent: tuple) -> dict:
    """An installed sprite's cost: its current variant a drawing, or a render and the textures it wore."""
    row = installed_row(base, ident)
    if row and "model" in row:
        return model_cost(base, ident, row.get("textures", []), spent) | {"variant": row["variant"]}
    return cost(ident, [], row.get("frame") if row else None, spent) | {"variant": row["variant"] if row else None}


def installed_row(base: Path, ident: str) -> dict | None:
    """The variants.jsonl row of the variant the sprite under assets/ was made from."""
    for source in (base / sprites.ASSETS).rglob(f"{ident}{sprites.SOURCE}"):
        variant = json.loads(source.read_text(encoding="utf-8")).get("variant")
        if variant:
            picture = base / variant
            return next((r for r in sprites.read_rows(picture.parent / sprites.VARIANTS)
                         if r["variant"] == picture.stem), None)
    return None


def installed(base: Path) -> list[str]:
    """Every sprite under assets/ made from a kept variant."""
    return sorted({p.name[: -len(sprites.SOURCE)] for p in (base / sprites.ASSETS).rglob(f"*{sprites.SOURCE}")
                   if "variant" in json.loads(p.read_text(encoding="utf-8"))})


def billing(base: Path, spent: tuple | None = None) -> dict:
    """
    The project's whole spend: every call (newest first, with what was kept from it), every installed sprite's cost,
    and every texture more than one model wears.
    """
    spent = spent or spend(base)
    rows, kept, worn = spent
    assets = sorted((sprite_cost(base, i, spent) for i in installed(base)), key=lambda a: -a["allTimeUsd"])
    used = {r["frame"] for a in assets for r in a["frames"] + [f for t in a["textures"] for f in t["frames"]]}
    calls = [row | {"kept": kept.get(row["frame"], []), "forInstalled": row["frame"] in used} for row in reversed(rows)]
    reusable = [{"texture": t, "wornBy": ids, "allTimeUsd": sum(r["shareUsd"] for r in history(t, rows, kept))}
                for t, ids in sorted(worn.items()) if len(ids) > 1]
    return {"ledger": str(SPEND), "calls": calls, "assets": assets, "reusable": reusable,
            "spentUsd": sum(r.get("costUsd") or 0 for r in rows),
            "installedUsd": sum(a["amortizedUsd"] for a in assets),
            "retryUsd": sum(r.get("costUsd") or 0 for r in rows if r["attempt"] > 1),
            "idleUsd": sum(r.get("costUsd") or 0 for r in calls if not r["forInstalled"])}


def report(base: Path, idents: list[str], limit: int) -> int:
    if not (base / SPEND).is_file():
        print(f"no {_sim.rel(base, base / SPEND)} yet")
        return 0
    spent = spend(base)
    if not idents:
        whole = billing(base, spent)
        print(f"  {'asset':<34} {'all time':>9} {'retries':>15} {'current':>9}")
        for a in whole["assets"][: limit or None]:
            print(f"  {a['asset']:<34} ${a['allTimeUsd']:.4f} {a['retries']:>3} ${a['retryUsd']:.4f}   "
                  f"${a['currentUsd']:.4f}")
        print(f"project: {len(whole['calls'])} billed call(s), ${whole['spentUsd']:.4f}; installed art as it stands "
              f"${whole['installedUsd']:.4f} (shared textures split); retries ${whole['retryUsd']:.4f}; calls for "
              f"nothing installed ${whole['idleUsd']:.4f}")
        for t in whole["reusable"]:
            print(f"  reusable {t['texture']:<24} ${t['allTimeUsd']:.4f}  worn by {', '.join(t['wornBy'])}")
        return 0
    for ident in idents:
        print_one(sprite_cost(base, ident, spent))
    return 0


def print_one(c: dict) -> None:
    what = f"installed from {c['variant']}" if c.get("variant") else "not installed"
    print(f"{c['asset']}  ({what})")
    print(f"  all time  ${c['allTimeUsd']:.4f}  {c['count']} frame(s); {c['retries']} retries, ${c['retryUsd']:.4f}")
    print(f"  current   ${c['currentUsd']:.4f}" + (f"  from {c['drawnFrom']}" if c["drawnFrom"] else "")
          + (f"; ${c['amortizedUsd']:.4f} with reused textures split" if c["reused"] else ""))
    print_frames(c["frames"], "    ")
    for t in c["textures"]:
        print(f"  texture {t['texture']}  current ${t['currentUsd']:.4f} from {t['frame']}, all time "
              f"${t['allTimeUsd']:.4f}" + (f"; reused, worn by {', '.join(t['wornBy'])}" if len(t["wornBy"]) > 1 else ""))
        print_frames(t["frames"], "    ")
    if not c["count"]:
        print("  no billed frame asked for it: legacy, or not generated")


def print_frames(frames: list[dict], indent: str) -> None:
    for r in frames:
        kept = ", ".join(f"{k['variant']} ({k['status']})" for k in r["kept"]) or "nothing kept"
        tried = f"retry {r['attempt'] - 1}" if r["attempt"] > 1 else "first try"
        print(f"{indent}{r['ts']}  {r['frame']:<16} {tried:<9} ${r['shareUsd']:.4f} of ${r['costUsd']:.4f} "
              f"/{len(r['cells'])}  {kept}")


def problems(base: Path) -> list[str]:
    """A kept frame the ledger has no line for: its cost would be missing from every total."""
    billed = {r["frame"] for r in sprites.read_rows(base / SPEND)}
    return [f"{sprites.KEPT_FRAMES}/{p.name}: frame {p.stem} has no line in {SPEND}"
            for p in sorted((base / sprites.KEPT_FRAMES).glob("*.json")) if p.stem not in billed]
