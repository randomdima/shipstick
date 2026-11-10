"""
`qq sprites rename OLD NEW`: an asset given a new id everywhere it is kept, worn, placed and installed, so a name can
say what the asset is rather than what it was first made for.

Moved: its folder under raw_assets/ and every file in it named for it, and every file under assets/ made from it — a
sprite, its .src.json and mesh, a texture as a face wears it. Rewritten: each reference to it in the kept rows and
models, the drafts under .tmp/shapes/, the installed .src.json and meshes, and the family notes (prompting.md). Left as
they were: the spend ledger and the kept frames' records, which say what was asked at the time — raw_assets/_renamed.jsonl
maps the old id to the new for them (_catalog.renamed).

Refused: a new id something already has, and an id the game's code names (src/), which a rename here would break.
"""

from __future__ import annotations

import re
from pathlib import Path

import _catalog
import _sim
import sprites
from common import cli

#: Where references to an asset are rewritten, as globs under the project.
REWRITTEN = ("raw_assets/**/variants.jsonl", "raw_assets/**/*.model.json", "raw_assets/**/prompting.md",
             ".tmp/shapes/*.json", "assets/**/*.src.json", "assets/**/*.mesh.json")
#: The game's code, which names some assets (the plain crate a device without a model stands as).
CODE = ("src/**/*.cs", "src/**/*.js", "src/**/*.css", "src/**/*.html")


def reference(ident: str) -> re.Pattern:
    """The id where it names the asset: a path's folder or file, a variant, a quoted id — not a longer id it starts."""
    return re.compile(rf"(?<![A-Za-z0-9_]){re.escape(ident)}(?=-v\d|/|\.(?:png|webp|src|mesh|model)\b|[\"`])")


def rename(base: Path, old: str, new: str) -> int:
    homes = [p.parent for p in (base / sprites.RAW).rglob(f"{old}/{sprites.VARIANTS}")]
    if len(homes) != 1:
        cli.fail(f"{len(homes)} kept assets named {old}: expected one under {sprites.RAW}/")
    home = homes[0]
    target = home.with_name(new)
    taken = [p for p in (base / sprites.RAW).rglob(new) if p.is_dir()] + list((base / sprites.ASSETS).rglob(f"{new}.*"))
    if taken:
        cli.fail(f"{new} is taken: {_sim.rel(base, taken[0])}")
    cited = [f"{_sim.rel(base, p)}:{n}" for glob in CODE for p in sorted(base.glob(glob))
             for n, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1)
             if re.search(rf"(?<![A-Za-z0-9_]){re.escape(old)}(?![A-Za-z0-9_])", line)]
    if cited:
        cli.fail(f"the game's code names {old}: {', '.join(cited[:5])} — rename it there in the same change, by hand")

    pattern = reference(old)
    rewritten = 0
    for glob in REWRITTEN:
        for path in sorted(base.glob(glob)):
            text = path.read_text(encoding="utf-8")
            changed = pattern.sub(new, text)
            if changed != text:
                path.write_text(changed, encoding="utf-8")
                rewritten += 1

    home.rename(target)
    moved = [f for f in sorted(target.iterdir()) if f.name.startswith(f"{old}-v") or f.name.startswith(f"{old}.")]
    installed = [f for f in sorted((base / sprites.ASSETS).rglob(f"{old}*"))
                 if f.name.startswith(f"{old}-v") or f.name.startswith(f"{old}.")]
    for f in moved + installed:
        f.rename(f.with_name(new + f.name[len(old):]))
    _catalog.record_rename(base, old, new)
    print(f"{_sim.rel(base, home)} → {_sim.rel(base, target)}: {len(moved)} kept file(s), {len(installed)} installed "
          f"file(s) renamed, {rewritten} file(s) rewritten; the ledger reads it as {new} ({_catalog.RENAMED})")
    mentioned = [_sim.rel(base, p) for glob in ("docs/**/*.md", ".claude/**/*.md", "src/**/*.md") for p in base.glob(glob)
                 if re.search(rf"(?<![A-Za-z0-9_]){re.escape(old)}(?![A-Za-z0-9_])", p.read_text(encoding="utf-8"))]
    if mentioned:
        print(f"documents that still say {old}: {', '.join(sorted(mentioned))}")
    return 0
