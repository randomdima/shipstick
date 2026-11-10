"""
The asset catalogue: what each kept texture, part and model is, so an agent finds what is kept before it briefs
anything new, and reuses it where it belongs. The rules are raw_assets/index.md, "The catalogue".

Each catalogued asset's folder holds `asset.json` beside its variants:

    {"about": "...", "kind": "face", "sets": ["galley"], "material": "steel", "fits": ["top"], "tags": ["worktop"]}

`about` says what it is in plain words, `kind` how it is reused (KINDS), `sets` the families of style and function it
belongs to (raw_assets/sets.md), `tags` the other words someone looking for it would use; a texture also names its
`material` and the faces it `fits`. The entry describes the asset, not a version of it, and is edited freely.

Stdlib only: remotegen imports it to warn of a near match before a sheet is billed.
"""

from __future__ import annotations

import json
import math
import re
import time
from pathlib import Path

RAW = Path("raw_assets")
TEXTURES, PARTS = RAW / "textures", RAW / "parts"
ENTRY = "asset.json"
SETS = RAW / "sets.md"
RENAMED = RAW / "_renamed.jsonl"
VARIANTS = "variants.jsonl"

#: How each kind is reused. A material tiles and repeats unnoticed; a face is a whole face's picture and is recognised
#: wherever it appears again; a decal is a small fitted mark (a vent, a gauge, a label); a part is a small model placed
#: by others; a device is a model the game installs.
TEXTURE_KINDS = ("material", "face", "decal")
MODEL_KINDS = ("part", "device")
KINDS = TEXTURE_KINDS + MODEL_KINDS
#: How many models may wear one picture, or place one part, before `qq shapes` names it as worn too widely. A trial
#: value, tuned by looking at the floor (raw_assets/index.md); a material has no limit.
WEARERS_SOFT_CAP = {"face": 3, "decal": 6, "part": 6}

FIELDS = {"about": str, "kind": str, "sets": list, "tags": list, "material": str, "fits": list}
SET_ROW = re.compile(r"^\|\s*`(?P<id>[a-z0-9_]+)`\s*\|\s*(?P<about>.+?)\s*\|\s*$")
CELL_LINE = re.compile(r"^\s*(?P<n>\d+)\.\s+(?P<line>.+)$")
PROPORTION = re.compile(r"^(square|(twice|\w+ times) as (wide|tall) as (tall|wide|\w+))\s*[.:]\s*", re.IGNORECASE)
WORD = re.compile(r"[a-z0-9]+")
#: Words every brief and entry uses, so they say nothing about which asset is meant.
STOP = set("""a an and the of to in on at by for with from into its it is as or but than then this that these those
each every one two three four five six seven eight nine all any no not nothing only also again same very more most
seen face faces straight down up left right top bottom edge edges side sides square wide tall twice half times swatch
swatches filling fills fill touching plain faint fine dull slightly small large long short thin thick narrow broad
evenly even soft repeating repeat whole rest outside inside round along across over under behind between near
middle centre center corner corners fully transparent""".split())
#: Of `near`: the share of a new brief line's weight an entry must cover to be named before billing.
NEAR_SHARE = 0.45


def entries(base: Path) -> dict[str, dict]:
    """Every catalogued asset by id: its entry, and `folder`, where it is kept."""
    found = {}
    for path in sorted((base / RAW).rglob(ENTRY)):
        try:
            entry = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            entry = {"error": str(e)}
        found[path.parent.name] = entry | {"id": path.parent.name, "folder": path.parent.relative_to(base).as_posix()}
    return found


def sets(base: Path) -> dict[str, str]:
    """The sets raw_assets/sets.md defines: id, and its line of style and function."""
    path = base / SETS
    if not path.is_file():
        return {}
    return {m["id"]: m["about"] for line in path.read_text(encoding="utf-8").splitlines() if (m := SET_ROW.match(line))}


def wanted(base: Path) -> list[Path]:
    """
    Every kept folder that must have an entry: each texture, each part, and each asset kept as a model's render. A
    drawing kept before GAM-13 is not catalogued; its model will be.
    """
    found = set()
    for rows in (base / RAW).rglob(VARIANTS):
        folder = rows.parent
        if folder.parent in (base / TEXTURES, base / PARTS) or '"model"' in rows.read_text(encoding="utf-8"):
            found.add(folder)
    return sorted(found)


def kind_of(base: Path, folder: Path) -> str | None:
    """The kind an entry is not free to differ from: a part, a device, or one of the textures' kinds."""
    if folder.parent == base / PARTS:
        return "part"
    if folder.parent == base / TEXTURES:
        return None
    return "device"


def problems(base: Path) -> list[str]:
    """Every kept asset without a complete entry, an entry that is malformed, and a set nothing defines."""
    known, found = sets(base), entries(base)
    out = [] if known else [f"{SETS}: no sets defined"]
    for folder in wanted(base):
        where = folder.relative_to(base).as_posix()
        entry = found.get(folder.name)
        if entry is None or entry.get("folder") != where:
            out.append(f"{where}: no {ENTRY} — qq sprites catalog {folder.name} --kind … --sets … --tags …")
            continue
        out += [f"{where}/{ENTRY}: {p}" for p in entry_problems(entry, kind_of(base, folder), known)]
    return out


def entry_problems(entry: dict, kind: str | None, known: dict[str, str]) -> list[str]:
    if "error" in entry:
        return [entry["error"]]
    out = [f"unknown field {k}" for k in entry if k not in FIELDS and k not in ("id", "folder")]
    out += [f"{k} is not a {t.__name__}" for k, t in FIELDS.items() if k in entry and not isinstance(entry[k], t)]
    if out:
        return out
    texture = kind is None
    if not entry.get("about"):
        out.append("no about")
    if entry.get("kind") not in (TEXTURE_KINDS if texture else (kind,)):
        out.append(f"kind is {entry.get('kind')!r}; it is {' or '.join(TEXTURE_KINDS if texture else (kind,))}")
    if not entry.get("sets"):
        out.append("no sets")
    out += [f"set {s!r} is not in {SETS}" for s in entry.get("sets", []) if s not in known]
    if texture:
        out += [f"no {k}" for k in ("material", "fits") if not entry.get(k)]
    else:
        out += [f"{k} is for a texture" for k in ("material", "fits") if k in entry]
    return out


def write(base: Path, folder: Path, entry: dict) -> Path:
    """The entry into `folder`, fields in a fixed order so a diff shows only what changed."""
    path = base / folder / ENTRY
    ordered = {k: entry[k] for k in FIELDS if k in entry}
    path.write_text(json.dumps(ordered, indent=1) + "\n", encoding="utf-8")
    return path


def brief_lines(record: dict) -> dict[str, str]:
    """
    Each cell's own line of a frame's brief, by the cell's asset id: the numbered list in reading order, less the
    proportion it opens with ("Square.", "Twice as wide as tall:"), which the picture itself states.
    """
    numbered = {int(m["n"]): PROPORTION.sub("", m["line"]) for line in (record.get("prompt") or "").splitlines()
                if (m := CELL_LINE.match(line))}
    return {cell: numbered[n] for n, cell in enumerate(record.get("cells") or [], 1) if n in numbered}


def renamed(base: Path) -> dict[str, str]:
    """Each id an asset was once kept under and the id it has now, chains followed."""
    path = base / RENAMED
    pairs = {}
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                row = json.loads(line)
                pairs[row["from"]] = row["to"]
    resolved = {}
    for old in pairs:
        new, seen = pairs[old], {old}
        while new in pairs and new not in seen:
            seen.add(new)
            new = pairs[new]
        resolved[old] = new
    return resolved


def record_rename(base: Path, old: str, new: str) -> None:
    with (base / RENAMED).open("a", encoding="utf-8") as rows:
        rows.write(json.dumps({"from": old, "to": new, "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}) + "\n")


def words(text: str) -> list[str]:
    """Content words, lowercased, a plural's s dropped so `drawers` finds `drawer`."""
    out = []
    for w in WORD.findall(text.lower().replace("_", " ")):
        if w in STOP or len(w) < 3 or w.isdigit():
            continue
        out.append(w[:-1] if len(w) > 3 and w.endswith("s") and not w.endswith("ss") else w)
    return out


def labels(entry: dict) -> set[str]:
    """The words an entry is filed under: its id, kind, sets, material, fits and tags — not its about."""
    return set(words(" ".join([entry["id"], entry.get("kind", ""), entry.get("material", ""),
                               *entry.get("sets", []), *entry.get("fits", []), *entry.get("tags", [])])))


def search(found: dict[str, dict], query: str, set_: str | None = None, kind: str | None = None,
           fits: str | None = None) -> list[tuple[float, dict]]:
    """
    The entries the filters keep, ranked by the query: a word an entry is filed under counts three, a word of its
    about one, a word that only starts one of them half that — each times how rare the word is in the catalogue, so
    `steel` ranks little and `worktop` much. No query keeps every entry, by id.
    """
    kept = [e for e in found.values()
            if (set_ is None or set_ in e.get("sets", [])) and (kind is None or e.get("kind") == kind)
            and (fits is None or fits in e.get("fits", []))]
    asked = words(query)
    if not asked:
        return [(0.0, e) for e in sorted(kept, key=lambda e: e["id"])]
    bags = {e["id"]: (labels(e), set(words(e.get("about", "")))) for e in found.values()}
    rarity = {w: math.log((1 + len(bags)) / (1 + sum(w in f or w in a for f, a in bags.values()))) + 1 for w in asked}
    ranked = []
    for e in kept:
        filed, about = bags[e["id"]]
        score = 0.0
        for w in asked:
            if w in filed:
                score += 3 * rarity[w]
            elif w in about:
                score += rarity[w]
            elif any(f.startswith(w) for f in filed):
                score += 1.5 * rarity[w]
            elif any(a.startswith(w) for a in about):
                score += 0.5 * rarity[w]
        if score:
            ranked.append((score, e))
    return sorted(ranked, key=lambda r: (-r[0], r[1]["id"]))


def near(found: dict[str, dict], line: str, skip: set[str] = frozenset()) -> list[tuple[float, dict]]:
    """
    The entries a new brief line may be asking for again: each word weighted by how rare it is across the catalogue,
    an entry's score the share of the line's weight it covers. Named, not refused: a near match can be a new thing.
    """
    pool = [e for e in found.values() if e["id"] not in skip]
    if not pool:
        return []
    bags = {e["id"]: labels(e) | set(words(e.get("about", ""))) for e in pool}
    asked = set(words(line))
    weight = {w: math.log((1 + len(pool)) / (1 + sum(w in b for b in bags.values()))) + 1 for w in asked}
    total = sum(weight.values())
    if not total:
        return []
    scored = [(sum(weight[w] for w in asked & bags[e["id"]]) / total, e) for e in pool]
    return sorted([s for s in scored if s[0] >= NEAR_SHARE], key=lambda s: -s[0])
