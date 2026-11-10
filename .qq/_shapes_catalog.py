"""
The catalogue as the viewer page shows it (_shapes_view.py writes it into viewer-data.js beside the models): every
catalogued asset (_catalog.py) with its pictures, every kept variant, who wears or places it, the reuse notes about
it, what it cost and every billed call behind that; the drafts not kept yet; the frames' prompts; the project's
ledger. The page filters and searches it itself.
"""

from __future__ import annotations

from pathlib import Path

import _catalog
import _shapes_library
import _shapes_view
import _sim
import _spend
import sprites
from common import cli


def data(base: Path, every: dict[str, dict | Exception], spent: tuple, url) -> dict:
    """
    `every` is `_shapes_view.loaded`, `spent` `_spend.spend`, and `url` how the page addresses a file
    (`_shapes_view.url`).
    """
    found = _catalog.entries(base)
    loaded = {f: m for f, m in every.items() if isinstance(m, dict)}
    standing = _shapes_library.current(base, loaded)
    worn, placed = _shapes_library.usage(standing)
    installed = set(_spend.installed(base))
    notes = _shapes_library.reuse_notes(found, standing, worn, placed, installed=installed)
    standing_file = {m["id"]: f for f, m in standing.items()}
    former: dict[str, list[str]] = {}
    for old, new in _catalog.renamed(base).items():
        former.setdefault(new, []).append(old)

    drafts: dict[str, list[str]] = {}
    for file, model in every.items():
        if file.startswith(f"{_shapes_view.OUT}/") and isinstance(model, dict):
            drafts.setdefault(model["id"], []).append(file)

    entries = []
    for ident, entry in sorted(found.items()):
        folder = base / entry["folder"]
        variants = [variant(base, folder, row, url) for row in sprites.read_rows(folder / sprites.VARIANTS)]
        shown = next((v for v in variants if v["status"] == "used"), variants[-1] if variants else None)
        users = sorted(worn.get(ident, set()) | placed.get(ident, set()))
        entries.append({k: v for k, v in entry.items() if k != "error"} | {
            "problems": _catalog.entry_problems(entry, _catalog.kind_of(base, folder), _catalog.sets(base)),
            "picture": shown and shown.get("url"), "px": shown and shown.get("px"),
            "variants": variants, "standing": standing_file.get(ident), "users": users,
            "cap": _catalog.WEARERS_SOFT_CAP.get(entry.get("kind")), "installed": ident in installed,
            "formerly": former.get(ident, []), "drafts": drafts.get(ident, []),
            "cost": cost(base, ident, entry, shown, standing.get(standing_file.get(ident)), spent),
        })
    kept = {e["id"] for e in entries}
    for file, model in sorted(every.items()):
        if not file.startswith(f"{_shapes_view.OUT}/") or (isinstance(model, dict) and model["id"] in kept):
            continue
        entries.append(draft(base, file, model, spent))
    return {"sets": [{"id": k, "about": v} for k, v in _catalog.sets(base).items()], "entries": entries,
            "notes": notes, "frames": frames(base, entries), "billing": billing(base, spent),
            "caps": _catalog.WEARERS_SOFT_CAP}


def variant(base: Path, folder: Path, row: dict, url) -> dict:
    """One kept variant as the page lists it: its row, its picture, its size."""
    from PIL import Image

    picture = folder / f"{row['variant']}.png"
    found = {k: row.get(k) for k in ("variant", "score", "status", "ts", "frame", "model", "view", "cellPx")}
    if picture.is_file():
        with Image.open(picture) as image:
            found |= {"url": url(base, picture), "px": list(image.size)}
    return found


def cost(base: Path, ident: str, entry: dict, shown: dict | None, model: dict | None, spent: tuple) -> dict:
    """
    The asset's figures (_spend.cost): a model's from the version installed, else the one standing; a texture's from
    the frame its shown variant was cut from.
    """
    if entry.get("kind") in _catalog.MODEL_KINDS:
        if _spend.installed_row(base, ident):
            return _spend.sprite_cost(base, ident, spent)
        if model is not None:
            return _spend.model_cost(base, ident, [t["src"] for t in model["textures"].values()], spent)
    return _spend.cost(ident, [], shown and shown.get("frame"), spent)


def draft(base: Path, file: str, model: dict | Exception, spent: tuple) -> dict:
    """A model under .tmp/shapes/ that nothing is kept as yet: listed so a render in progress can be looked at."""
    if isinstance(model, Exception):
        return {"id": Path(file).stem, "kind": "draft", "about": "", "sets": [], "tags": [], "standing": file,
                "error": str(model), "variants": [], "users": [], "formerly": []}
    return {"id": model["id"], "kind": "draft", "about": model.get("about", ""), "sets": model.get("sets", []),
            "tags": [], "standing": file, "variants": [], "users": [], "formerly": [],
            "cost": _spend.model_cost(base, model["id"], [t["src"] for t in model["textures"].values()], spent)}


def frames(base: Path, entries: list[dict]) -> dict[str, dict]:
    """The record of every frame an entry's cost names: what was asked, of what, with what, and what it cost."""
    wanted = {r["frame"] for e in entries for c in [e.get("cost") or {}]
              for r in c.get("frames", []) + [f for t in c.get("textures", []) for f in t["frames"]]}
    out = {}
    for frame in sorted(wanted):
        try:
            record = sprites.frame_record(base, frame)
        except cli.Failure:
            continue
        out[frame] = {"ts": record.get("ts"), "op": record.get("op"), "model": record.get("model"),
                      "settings": record.get("settings"), "costUsd": record.get("costUsd"),
                      "prompt": record.get("prompt"), "cells": record.get("cells"),
                      "inputs": [f"{i['role']}: {i['was']}" for i in record.get("inputs", [])]}
    return out


def billing(base: Path, spent: tuple) -> dict:
    """The project's ledger and totals, every call newest first with what was kept from it (_spend.billing)."""
    whole = _spend.billing(base, spent)
    return {k: whole[k] for k in ("calls", "spentUsd", "installedUsd", "retryUsd", "idleUsd")} | {
        "ledger": _sim.rel(base, base / _spend.SPEND)}
