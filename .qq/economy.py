"""
Check the item catalogue against its rules, and draw the resource tree it makes.

The catalogue is src/economy/catalog/: sections.md holds the sections, subsections, pinned items, roles and stats, and
each `<sub>.md` a subsection's devices, its hundred items and its ways, as Markdown tables whose header row names their
columns. `check` holds it to the ECO rules (src/economy/docs/requirements.md); narrowed to one subsection it accepts a
pinned item of a subsection not yet written, so one file can be checked before the rest exist. `item` prints every way
one item is made, ended and needed by. `audit` counts what the rules allow and a review would not. `tree` writes the
generated resource-tree.md and resource-map.svg beside the design; `explore` writes a page to browse every item in.

An item is made by the ways that make it, the uses that leave it and the decays that become it, and ended by the ways
that take it, its own use and its own decay; a tool is needed by ways and kept. Depth, reach and cost are derived here
and nowhere else (ECO-4), each as a fixpoint over the ways, because ways loop: waste comes back as water and compost.
"""

from __future__ import annotations

import argparse
import html
import json
import math
import re
import statistics
from dataclasses import dataclass, field
from pathlib import Path

import _sim
from common import cli, paths

#: What a call may take: reading five thousand items and their ways, and writing the tree.
TIMEOUT_S = 120

CATALOG = "src/economy/catalog"
INDEX = "sections.md"
DOCS = "src/economy/docs"
TREE_MD = f"{DOCS}/resource-tree.md"
TREE_SVG = f"{DOCS}/resource-map.svg"

ITEMS_PER_SUB = 100
CREW = "crew"
#: The universal fixtures' file and role: every capsule has them, so they count as no role.
UNIVERSAL = "any"
REACH_NAMES = ["solo", "pair", "trio", "crew"]
#: A durable that never decays is valued as if it lasted this long.
DEFAULT_LIFE_H = 24
#: A tool that never wears out is costed as if it lasted this long in use.
TOOL_LIFE_H = 1000
#: Stats no rate may help: only a way the crew spends minutes on gives them (ECO-11).
DOING_ONLY = ("fun", "fitness")
#: A source this many times cheaper or dearer than its stat's median, a work-minute, is flagged.
OUTLIER_FACTOR = 4
#: An arrow on the map needs at least this many way inputs between two subsections.
MAP_EDGE_LEAST = 3
#: The map's columns, shallow to deep, and the arrows into each subsection: its biggest suppliers.
MAP_COLUMNS = 7
MAP_SUPPLIERS = 2
#: The universal input, left off the diagrams: an arrow from it would reach every box.
POWER = "pwr-001"
#: Each node's arrows in the section and role diagrams: its few biggest suppliers.
DIAGRAM_SUPPLIERS = 3
#: Ways and ends listed for each pinned item in the tree.
FLOW_SHOWN = 6

ID = re.compile(r"^(?P<sub>[a-z]{3})-(?P<n>\d{3})$")
DEVICE_ID = re.compile(r"^(?P<sub>[a-z]{3})\.[a-z0-9]+$")
SUB = re.compile(r"^[a-z]{3}$")
COUNTED = re.compile(r"^(?P<count>\d+) (?P<id>[a-z]{3}-\d{3})$")
EFFECT = re.compile(r"^(?P<stat>[a-z][a-z0-9.]*) (?P<amount>[+-]\d+(?:\.\d+)?)(?P<rate>/h)?$")
LEAVES = re.compile(r"^leaves (?P<count>\d+) (?P<id>[a-z]{3}-\d{3})$")
POINTS_AT = re.compile(r"^(?P<verb>fits|installs) (?P<device>[a-z]{3}\.[a-z0-9]+)$")
DECAYS = re.compile(r"^(?P<h>\d+(?:\.\d+)?) h(?: → (?P<into>[a-z]{3}-\d{3}))?$")
CELLS = re.compile(r"^\d+x\d+$")
#: What the citation checker would read as a rule's ID (docs/../.qq/_docs.py CITATION).
CITES = re.compile(r"(?<![A-Za-z0-9])[A-Z]{1,4}-[0-9]")
BLANK = {"", "—", "-"}


@dataclass
class Item:
    id: str
    name: str
    effects: list[tuple[str, float, bool]]
    leaves: list[tuple[int, str]]
    fits: list[str]
    installs: list[str]
    decay_h: float | None
    decays_to: str | None
    where: str
    use: str

    @property
    def sub(self) -> str:
        return self.id[:3]

    @property
    def has_use(self) -> bool:
        return bool(self.effects or self.fits or self.installs)

    @property
    def kind(self) -> str:
        if self.installs:
            return "kit"
        if self.fits:
            return "part"
        if any(rate for *_, rate in self.effects):
            return "durable"
        return "consumable" if self.effects else "resource"


@dataclass
class Way:
    name: str
    by: str
    minutes: float
    #: Tools: at hand while the way runs and kept after it, their wear clock running meanwhile.
    needs: list[tuple[int, str]]
    takes: list[tuple[int, str]]
    makes: list[tuple[int, str]]
    gives: list[tuple[str, float]]
    where: str
    sub: str

    @property
    def label(self) -> str:
        return f"{self.name} ({self.by})"

    @property
    def inputs(self) -> list[tuple[int, str]]:
        """What must be had to run it: what it needs and what it takes."""
        return self.needs + self.takes


@dataclass
class Device:
    id: str
    name: str
    role: str
    cells: str


@dataclass
class Sub:
    name: str
    section: str
    roles: list[str]


@dataclass
class Catalogue:
    roles: dict[str, str] = field(default_factory=dict)
    #: stat → (whose: crew, cabin, ship; +1 or -1, the way that helps it; whether a capsule must keep it alone)
    stats: dict[str, tuple[str, int, bool]] = field(default_factory=dict)
    sections: dict[str, str] = field(default_factory=dict)
    subs: dict[str, Sub] = field(default_factory=dict)
    pinned: dict[str, str] = field(default_factory=dict)
    #: What the ship set out with and nothing makes (ECO-10): id → name.
    stock: dict[str, str] = field(default_factory=dict)
    devices: dict[str, Device] = field(default_factory=dict)
    items: dict[str, Item] = field(default_factory=dict)
    #: The codex's words for each item and device (ECO-12): id → (about, flavour, where).
    codex: dict[str, tuple[str, str, str]] = field(default_factory=dict)
    ways: list[Way] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)
    problems: list[tuple[str, str]] = field(default_factory=list)

    def warn(self, sub: str, message: str):
        self.problems.append((sub, message))

    def role(self, way: Way) -> str | None:
        device = self.devices.get(way.by)
        return None if device is None or device.role == UNIVERSAL else device.role

    def known(self, item_id: str) -> bool:
        return item_id in self.items or (item_id in self.pinned and item_id[:3] in self.missing)


def main():
    a = parse_args()
    base = _sim.root()
    cat = load(base)
    if a.action == "check":
        return check(cat, a.ref, a.limit)
    if a.action == "item":
        return show_item(cat, a.ref, a.limit)
    if a.action == "list":
        return list_items(cat, a.ref)
    if a.action == "tree":
        return write_tree(base, cat)
    if a.action == "audit":
        return audit(cat, a.ref, a.limit)
    if a.action == "words":
        return set_words(base, cat, paths.resolve_in_root(a.words, base))
    return write_explorer(base, cat, paths.resolve_in_root(a.out, base))


def parse_args():
    parser = argparse.ArgumentParser(
        prog="qq economy",
        description="Check the item catalogue against its rules, and draw the resource tree it makes.",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("action", nargs="?", default="check",
                        choices=["check", "item", "list", "audit", "tree", "explore", "words"],
                        help="check: the ECO rules, for the catalogue or one subsection; item: every way one item is "
                             "made and ended; list: one subsection's devices and items, a line each, or every "
                             "subsection's; audit: what the rules allow and a review would not — dead ends, "
                             "pass-throughs, dominated ways, twin names — for the catalogue or one subsection; tree: "
                             "write resource-tree.md and resource-map.svg; explore: write the browsing page; words: "
                             "set names and codex words from --words, leaving every other cell as it is")
    parser.add_argument("ref", nargs="?", type=ref_type,
                        help="check, list: a subsection code, `wat`; item: an item id, `wat-002`")
    parser.add_argument("--limit", type=cli.counting, default=40, metavar="INT",
                        help="problems to print, or the depth of an item's cheapest chain (0 = no limit)")
    parser.add_argument("--out", default=".tmp/economy/explorer.html", help="explore: where the page is written")
    parser.add_argument("--words", default=".tmp/words",
                        help="words: a JSON file, or a folder of them, each {id: {name, about, flavour}}, any field "
                             "left out kept")
    return parser.parse_args()


def ref_type(value: str) -> str:
    if not (SUB.match(value) or ID.match(value)):
        raise argparse.ArgumentTypeError(f"expected a subsection code like wat or an item id like wat-002: got {value!r}")
    return value


# ---- setting words

#: Per table heading: the column each word sets. The pinned and stock tables in sections.md follow the item's name.
WORD_COLUMNS = {"devices": {"device": "name"}, "items": {"item": "name"}, "pinned items": {"item": "name"},
                "stock": {"item": "name"}, "codex": {"about": "about", "flavour": "flavour"}}


def set_words(base: Path, cat: Catalogue, source: Path) -> int:
    """Sets the names and codex words `source` gives, row by row in place, so no way, use or decay is retyped."""
    files = sorted(source.glob("*.json")) if source.is_dir() else [source]
    words: dict[str, dict[str, str]] = {}
    refused = 0
    for f in files:
        for ref, fields in json.loads(f.read_text(encoding="utf-8")).items():
            if ref not in cat.items and ref not in cat.devices:
                print(f"{f.name}: {ref} is no item or device")
                refused += 1
                continue
            for key, text in fields.items():
                text = " ".join(str(text).split())
                if key not in ("name", "about", "flavour") or not text or "|" in text or CITES.search(text):
                    print(f"{f.name}: {ref}.{key} {text!r} refused: an unknown field, blank, a `|`, or a rule's ID")
                    refused += 1
                    continue
                words.setdefault(ref, {})[key] = text
    changed = 0
    for path in sorted((base / CATALOG).glob("*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        heading, header, edits = "", None, 0
        for n, line in enumerate(lines):
            if line.startswith("## "):
                heading, header = line[3:].strip().lower(), None
                continue
            if not line.startswith("|"):
                header = None
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if header is None:
                header = [c.lower() for c in cells]
                continue
            columns = WORD_COLUMNS.get(heading)
            given = words.get(cells[0]) if columns and header[0] == "id" else None
            if not given:
                continue
            for column, key in columns.items():
                if key in given and column in header:
                    cells[header.index(column)] = given[key]
            if (row := "| " + " | ".join(cells) + " |") != line:
                lines[n], edits = row, edits + 1
        if edits:
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            print(f"{path.relative_to(base)}: {edits} rows")
            changed += edits
    print(f"{changed} rows set from {len(files)} file(s), {refused} refused")
    return 1 if refused else 0


# ---- reading


def tables(path: Path) -> dict[str, list[tuple[int, dict[str, str]]]]:
    """Every Markdown table in a file, under the `##` heading above it, each row its cells by header and its line."""
    found: dict[str, list[tuple[int, dict[str, str]]]] = {}
    heading, header = "", None
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("## "):
            heading, header = line[3:].strip().lower(), None
            continue
        if not line.startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = [c.lower() for c in cells]
        elif not set("".join(cells)) <= set("-: "):
            found.setdefault(heading, []).append((n, dict(zip(header, cells))))
    return found


def load(base: Path) -> Catalogue:
    cat = Catalogue()
    index = tables(base / CATALOG / INDEX)
    for _, r in index.get("roles", []):
        cat.roles[r["role"]] = r["name"]
    for _, r in index.get("stats", []):
        cat.stats[r["stat"]] = (r["of"], -1 if r["better"] == "lower" else 1, r["floor"] == "yes")
    for _, r in index.get("sections", []):
        cat.sections[r["section"]] = r["name"]
    for _, r in index.get("subsections", []):
        cat.subs[r["sub"]] = Sub(r["name"], r["section"], split(r["roles"]))
    for _, r in index.get("pinned items", []):
        cat.pinned[r["id"]] = r["item"]
    for _, r in index.get("stock", []):
        cat.stock[r["id"]] = r["item"]
    if not (cat.roles and cat.stats and cat.sections and cat.subs and cat.pinned):
        cli.fail(f"{CATALOG}/{INDEX} lacks one of its tables: sections, subsections, pinned items, roles, stats")

    read_sub(cat, UNIVERSAL, base / CATALOG / f"{UNIVERSAL}.md", f"{CATALOG}/{UNIVERSAL}.md")
    for code in cat.subs:
        path = base / CATALOG / f"{code}.md"
        if not path.is_file():
            cat.missing.append(code)
            continue
        read_sub(cat, code, path, _sim.rel(base, path))
    return cat


def read_sub(cat: Catalogue, code: str, path: Path, rel: str):
    found = tables(path)
    for n, r in found.get("devices", []):
        device = Device(r.get("id", ""), r.get("device", ""), r.get("role", ""), r.get("cells", ""))
        m = DEVICE_ID.match(device.id)
        if not m or m["sub"] != code:
            cat.warn(code, f"{rel}:{n}: device id {device.id!r} is not {code}.<name>")
        if code == UNIVERSAL:
            if device.role != UNIVERSAL:
                cat.warn(code, f"{rel}:{n}: device {device.id} is universal, so its role is {UNIVERSAL}")
        elif device.role not in cat.roles:
            cat.warn(code, f"{rel}:{n}: device {device.id} has no such role {device.role!r}")
        elif device.role not in cat.subs[code].roles:
            cat.warn(code, f"{rel}:{n}: device {device.id} is {device.role}, not one of {code}'s roles "
                           f"({', '.join(cat.subs[code].roles)})")
        if not CELLS.match(device.cells):
            cat.warn(code, f"{rel}:{n}: device {device.id} cells {device.cells!r} is not <columns>x<rows>")
        cat.devices[device.id] = device

    rows = found.get("items", [])
    if code != UNIVERSAL and len(rows) != ITEMS_PER_SUB:
        cat.warn(code, f"{rel}: {len(rows)} items, not {ITEMS_PER_SUB}")
    for i, (n, r) in enumerate(rows, 1):
        where = f"{rel}:{n}"
        try:
            item = parse_item(r, where)
        except ValueError as e:
            cat.warn(code, f"{where}: {e}")
            continue
        if item.id != f"{code}-{i:03d}":
            cat.warn(code, f"{where}: id {item.id} where {code}-{i:03d} was due")
        if item.id in cat.items:
            cat.warn(code, f"{where}: {item.id} twice")
        cat.items[item.id] = item

    for n, r in found.get("ways", []):
        where = f"{rel}:{n}"
        try:
            cat.ways.append(parse_way(r, where, code))
        except ValueError as e:
            cat.warn(code, f"{where}: {e}")

    for n, r in found.get("codex", []):
        ref = r.get("id", "")
        if ref in cat.codex:
            cat.warn(code, f"{rel}:{n}: codex row for {ref} twice")
        cat.codex[ref] = (r.get("about", ""), r.get("flavour", ""), f"{rel}:{n}")


def parse_item(r: dict[str, str], where: str) -> Item:
    effects, leaves, fits, installs = [], [], [], []
    for token in split(r.get("use", "")):
        if m := EFFECT.match(token):
            effects.append((m["stat"], float(m["amount"]), bool(m["rate"])))
        elif m := LEAVES.match(token):
            leaves.append((int(m["count"]), m["id"]))
        elif m := POINTS_AT.match(token):
            (fits if m["verb"] == "fits" else installs).append(m["device"])
        else:
            raise ValueError(f"use {token!r} is none of: <stat> +N, <stat> +N/h, leaves N <id>, fits <device>, "
                             "installs <device>")
    decay_h, decays_to = None, None
    if (cell := r.get("decays", "").strip()) not in BLANK:
        m = DECAYS.match(cell)
        if not m:
            raise ValueError(f"decays {cell!r} is not `N h` or `N h → <id>`")
        decay_h, decays_to = float(m["h"]), m["into"]
    return Item(r.get("id", ""), r.get("item", ""), effects, leaves, fits, installs, decay_h, decays_to, where,
                r.get("use", ""))


def parse_way(r: dict[str, str], where: str, code: str) -> Way:
    gives = []
    for token in split(r.get("gives", "")):
        m = EFFECT.match(token)
        if not m or m["rate"]:
            raise ValueError(f"gives {token!r} is not `<stat> +N`")
        gives.append((m["stat"], float(m["amount"])))
    try:
        minutes = float(r["min"])
    except (KeyError, ValueError):
        raise ValueError(f"min {r.get('min')!r} is not a number of minutes") from None
    return Way(r.get("way", ""), r.get("by", ""), minutes, counted(r.get("needs", ""), "needs"),
               counted(r.get("takes", ""), "takes"), counted(r.get("makes", ""), "makes"), gives, where, code)


def split(cell: str) -> list[str]:
    return [] if cell.strip() in BLANK else [t.strip() for t in cell.split(",") if t.strip()]


def counted(cell: str, what: str) -> list[tuple[int, str]]:
    found = []
    for token in split(cell):
        m = COUNTED.match(token)
        if not m:
            raise ValueError(f"{what} {token!r} is not `<count> <id>`")
        found.append((int(m["count"]), m["id"]))
    return found


# ---- checking


def check(cat: Catalogue, only: str | None, limit: int) -> int:
    if only and not SUB.match(only):
        cli.fail(f"check narrows to a subsection code, not {only!r}")
    if only and only not in cat.subs and only != UNIVERSAL:
        cli.fail(f"no subsection {only!r} in {CATALOG}/{INDEX}")
    if only in cat.missing:
        cli.fail(f"subsection {only} has no file: {CATALOG}/{only}.md")
    for item in cat.items.values():
        if not only or item.sub == only:
            check_item(cat, item)
    for way in cat.ways:
        if not only or way.sub == only:
            check_way(cat, way)
    check_devices(cat, only)
    check_names(cat)
    check_codex(cat, only)
    whole = not only and not cat.missing
    if whole:
        check_whole(cat)
    elif not only:
        cat.warn("", f"{len(cat.missing)} subsections have no file yet: {', '.join(cat.missing)}")

    shown = [m for s, m in cat.problems if not only or s in (only, "")]
    for message in shown[: limit or None]:
        print(message)
    if limit and len(shown) > limit:
        print(f"… {len(shown) - limit} more (--limit=0 for all)")
    scope = f"subsection {only}" if only else "the catalogue"
    items = [i for i in cat.items.values() if not only or i.sub == only]
    ways = [w for w in cat.ways if not only or w.sub == only]
    print(f"{scope}: {len(items)} items, {len(ways)} ways, {len(shown)} problems"
          + ("" if whole else " (partial: whole-catalogue rules not run)"))
    if whole and not shown:
        d = derive(cat)
        print("made: " + spread(d.made, items) + "; ended: " + spread(d.ended, items))
        print("reach: " + ", ".join(f"{REACH_NAMES[k]} {v}" for k, v in sorted(histogram(d.reach, items).items())))
    return 1 if shown else 0


def check_item(cat: Catalogue, item: Item):
    def warn(message):
        cat.warn(item.sub, f"{item.where}: {item.id} {message}")

    if not item.name:
        warn("has no name")
    if CITES.search(item.name):
        warn(f"name {item.name!r} reads as a rule's ID: write B12, U235, Mk II")
    for table, names in (("pinned", cat.pinned), ("stock", cat.stock)):
        if item.id in names and item.name != names[item.id]:
            warn(f"is {table} as {names[item.id]!r} in {INDEX}, here {item.name!r}")
    for stat, amount, rate in item.effects:
        if stat not in cat.stats:
            warn(f"uses {stat!r}, which is no stat in {INDEX}")
        elif rate and stat in DOING_ONLY and amount * cat.stats[stat][1] > 0:
            warn(f"raises {stat} by the hour: only doing gives {stat}, so a thing that helps it is a tool (ECO-11)")
    for _, left in item.leaves:
        if not cat.known(left):
            warn(f"leaves {left}, which is no item" + unwritten(cat, left))
    if item.decays_to and not cat.known(item.decays_to):
        warn(f"decays to {item.decays_to}, which is no item" + unwritten(cat, item.decays_to))
    if item.decays_to == item.id:
        warn("decays into itself")
    for device in item.fits + item.installs:
        if device not in cat.devices and device[:3] not in cat.missing:
            warn(f"fits or installs {device}, which is no device")


def check_way(cat: Catalogue, way: Way):
    def warn(message):
        cat.warn(way.sub, f"{way.where}: way {way.name!r} {message}")

    if not way.name:
        warn("has no name")
    if way.by != CREW and (way.by not in cat.devices or way.by.split(".")[0] not in (way.sub, UNIVERSAL)):
        warn(f"is run by {way.by!r}, which is neither a device of {way.sub}, a universal fixture nor {CREW}")
    if way.minutes <= 0:
        warn("takes no time: min is above 0")
    if not (way.makes or way.gives):
        warn("makes nothing and gives nothing")
    for count, ref in way.needs + way.takes + way.makes:
        if count <= 0:
            warn(f"counts {count} of {ref}")
        if not cat.known(ref):
            warn(f"names {ref}, which is no item" + unwritten(cat, ref))
    if {r for _, r in way.takes} & {r for _, r in way.makes}:
        warn("takes what it makes")
    if {r for _, r in way.needs} & {r for _, r in way.takes + way.makes}:
        warn("needs what it takes or makes: a tool is kept, neither spent nor made")
    for _, ref in way.needs:
        if (tool := cat.items.get(ref)) and tool.has_use:
            warn(f"needs {ref}, which has a use of its own: a tool is used by the ways that need it (ECO-11)")
    for stat, _ in way.gives:
        if stat not in cat.stats:
            warn(f"gives {stat!r}, which is no stat in {INDEX}")


def unwritten(cat: Catalogue, ref: str) -> str:
    return f" ({ref[:3]} is not written yet and {ref} is not pinned)" if ref[:3] in cat.missing else ""


def check_devices(cat: Catalogue, only: str | None):
    run = {w.by for w in cat.ways}
    with_ways = {w.sub for w in cat.ways}
    for device in cat.devices.values():
        sub = device.id.split(".")[0]
        if sub != UNIVERSAL and sub in with_ways and (not only or sub == only) and device.id not in run:
            cat.warn(sub, f"device {device.id} runs no way")


def check_codex(cat: Catalogue, only: str | None):
    """Every item and device has its codex words, and every codex row names one of its own file's (ECO-12)."""
    for ref in [*cat.items, *cat.devices]:
        sub = ref[:3]
        if only and sub != only:
            continue
        where = cat.items[ref].where if ref in cat.items else f"{CATALOG}/{sub}.md"
        about, flavour, _ = cat.codex.get(ref, ("", "", ""))
        if not about.strip() or about in BLANK:
            cat.warn(sub, f"{where}: {ref} has no codex `about` (ECO-12)")
        if not flavour.strip() or flavour in BLANK:
            cat.warn(sub, f"{where}: {ref} has no codex `flavour` (ECO-12)")
        for text in (about, flavour):
            if CITES.search(text):
                cat.warn(sub, f"{where}: {ref}'s codex words read as a rule's ID: write B12, U235, Mk II")
            if "|" in text:
                cat.warn(sub, f"{where}: {ref}'s codex words hold a `|`")
    for ref, (_, _, where) in cat.codex.items():
        if (not only or ref[:3] == only) and ref not in cat.items and ref not in cat.devices:
            cat.warn(ref[:3], f"{where}: codex row for {ref}, which is no item or device of the catalogue")
        elif not where.startswith(f"{CATALOG}/{ref[:3]}.md"):
            cat.warn(ref[:3], f"{where}: codex row for {ref} belongs in {CATALOG}/{ref[:3]}.md")


def check_names(cat: Catalogue):
    named: dict[str, Item] = {}
    for item in cat.items.values():
        if (twin := named.setdefault(item.name.lower(), item)) is not item:
            cat.warn(item.sub, f"{item.where}: {item.id} has the name of {twin.id}, {item.name!r}")


def check_whole(cat: Catalogue):
    d = derive(cat)
    for ref in cat.stock:
        if ref not in cat.items:
            cat.warn("", f"{INDEX}: stock {ref} is no item")
    outside = d.reached(seeded=False)
    for item in cat.items.values():
        if not d.made[item.id] and item.id not in cat.stock:
            cat.warn(item.sub, f"{item.where}: {item.id} {item.name} is made no way: no way makes it, no use leaves "
                               "it, nothing decays into it, and it is no stock (ECO-7)")
        if not d.ended[item.id]:
            cat.warn(item.sub, f"{item.where}: {item.id} {item.name} is ended no way: no way takes it, it has no use "
                               "and no decay (ECO-7)")
        elif item.id not in d.depth:
            cat.warn(item.sub, f"{item.where}: {item.id} {item.name} is reached from nothing that comes in from "
                               "outside: every way to it takes something no way or stock reaches (ECO-8)")
        if item.id in cat.stock and item.id in outside:
            cat.warn(item.sub, f"{item.where}: {item.id} {item.name} is stock, yet ways make it from what comes in "
                               "from outside (ECO-10)")
    for stat, (of, _, floor) in cat.stats.items():
        sources = d.sources(stat)
        if of in ("crew", "cabin"):
            solo = [s.value for s in sources if s.reach == 0]
            shared = [s.value for s in sources if s.reach > 0]
            if not shared:
                cat.warn("", f"stat {stat}: no source that takes other capsules (ECO-5)")
            elif floor and not solo:
                cat.warn("", f"stat {stat}: a floor stat with no source a capsule makes alone (ECO-5)")
            elif floor and max(shared) <= max(solo):
                cat.warn("", f"stat {stat}: nothing that takes other capsules beats the best solo source (ECO-5)")
        if of == "ship":
            if not sources:
                cat.warn("", f"stat {stat}: nothing keeps it (ECO-6)")
            for s in sources:
                if len(s.roles) < 2:
                    cat.warn(s.sub, f"{s.where}: {s.label} keeps {stat} but takes one role alone (ECO-6)")


# ---- deriving


@dataclass
class Source:
    """One thing that helps a stat: an item used, or a way run."""
    label: str
    where: str
    sub: str
    value: float
    reach: int
    roles: frozenset[str]
    cost: float
    durable: bool


class Derived:
    """
    What the ways make of the items: how each is made and ended, and its depth, reach and cost. Each is a fixpoint
    over every way at once, because a way's inputs may be made further along a loop.
    """

    def __init__(self, cat: Catalogue):
        self.cat = cat
        #: item → the ways that make it, the items whose use leaves it, the items that decay into it
        self.made: dict[str, list[Way | Item]] = {i: [] for i in cat.items}
        #: item → the ways that take it, and itself where its use or its decay ends it
        self.ended: dict[str, list[Way | Item]] = {i: [] for i in cat.items}
        #: item → the ways that need it as a tool
        self.needed: dict[str, list[Way]] = {i: [] for i in cat.items}
        for way in cat.ways:
            for _, ref in way.makes:
                self.made.setdefault(ref, []).append(way)
            for _, ref in way.takes:
                self.ended.setdefault(ref, []).append(way)
            for _, ref in way.needs:
                self.needed.setdefault(ref, []).append(way)
        for item in cat.items.values():
            for _, ref in item.leaves:
                self.made.setdefault(ref, []).append(item)
            if item.decays_to:
                self.made.setdefault(item.decays_to, []).append(item)
            if item.has_use or item.decay_h is not None:
                self.ended[item.id].append(item)
        self.depth = self._depth()
        self.chain = self._chains()
        self.cost = self._costs()
        self.reach = {i: len(roles - {maker}) for i, (roles, maker) in self.chain.items()}

    def leftovers(self, item: Item) -> list[str]:
        return [ref for _, ref in item.leaves] + ([item.decays_to] if item.decays_to else [])

    def kind(self, item: Item) -> str:
        return "tool" if item.kind == "resource" and self.needed.get(item.id) else item.kind

    def _depth(self) -> dict[str, int]:
        return self.reached(seeded=True)

    def reached(self, seeded: bool) -> dict[str, int]:
        """
        The fewest rounds of ways from what comes in from outside to each item — ways that take nothing, and the
        ship's stock when `seeded` — at depth 0; an item no round reaches is absent (ECO-8).
        """
        depth: dict[str, int] = {ref: 0 for ref in self.cat.stock} if seeded else {}
        pending = list(self.cat.ways)
        r = 0
        while True:
            r += 1
            fresh = []
            for way in pending:
                if all(ref in depth for _, ref in way.inputs):
                    fresh += [ref for _, ref in way.makes]
            fresh += [ref for i in depth if i in self.cat.items for ref in self.leftovers(self.cat.items[i])]
            pending = [w for w in pending if not all(ref in depth for _, ref in w.inputs)]
            new = [ref for ref in fresh if ref not in depth]
            if not new:
                return depth
            for ref in new:
                depth[ref] = r

    def roles_of_way(self, way: Way) -> frozenset[str] | None:
        found = set() if self.cat.role(way) is None else {self.cat.role(way)}
        for _, ref in way.inputs:
            if ref not in self.chain:
                return None
            found |= self.chain[ref][0]
        return frozenset(found)

    def _chains(self) -> dict[str, tuple[frozenset[str], str | None]]:
        """
        Each item's fewest-roles way: the roles among its devices down to nothing, and the role of the device that
        makes it. Fewest other roles wins, then fewest roles in all. A leftover takes the roles of what left it.
        """
        self.chain: dict[str, tuple[frozenset[str], str | None]] = {ref: (frozenset(), None) for ref in self.cat.stock}

        def better(ref, roles, maker):
            old = self.chain.get(ref)
            new_key = (len(roles - {maker}), len(roles))
            if old is None or new_key < (len(old[0] - {old[1]}), len(old[0])):
                self.chain[ref] = (roles, maker)
                return True
            return False

        changed = True
        while changed:
            changed = False
            for way in self.cat.ways:
                roles = self.roles_of_way(way)
                if roles is not None:
                    for _, ref in way.makes:
                        changed |= better(ref, roles, self.cat.role(way))
            for i, (roles, _) in list(self.chain.items()):
                if i in self.cat.items:
                    for ref in self.leftovers(self.cat.items[i]):
                        changed |= better(ref, roles, None)
        return self.chain

    def way_cost(self, way: Way) -> float:
        """Its minutes, what it takes, and the share of each tool's life one run wears away."""
        worn = sum(n * self.cost.get(ref, math.inf) * way.minutes / 60 / self.life_h(ref) for n, ref in way.needs)
        return way.minutes + worn + sum(n * self.cost.get(ref, math.inf) for n, ref in way.takes)

    def life_h(self, ref: str) -> float:
        item = self.cat.items.get(ref)
        return item.decay_h if item and item.decay_h else TOOL_LIFE_H

    def _costs(self) -> dict[str, float]:
        """
        Work-minutes: a way's time plus its inputs' cost, shared among what one run makes. What a use leaves and the
        ship's stock are free; what an item decays into costs what the item did, since it has to be had first.
        """
        self.cost: dict[str, float] = {ref: 0.0 for ref in self.cat.stock}
        for item in self.cat.items.values():
            for _, ref in item.leaves:
                self.cost[ref] = 0.0
        decaying = [i for i in self.cat.items.values() if i.decays_to]
        for _ in range(len(self.cat.items) + 1):
            changed = False
            for way in self.cat.ways:
                made = sum(n for n, _ in way.makes)
                c = self.way_cost(way)
                if not made or c == math.inf:
                    continue
                for _, ref in way.makes:
                    if c / made < self.cost.get(ref, math.inf) - 1e-9:
                        self.cost[ref] = c / made
                        changed = True
            for item in decaying:
                c = self.cost.get(item.id, math.inf)
                if c < self.cost.get(item.decays_to, math.inf) - 1e-9:
                    self.cost[item.decays_to] = c
                    changed = True
            if not changed:
                break
        return self.cost

    def door_reach(self, way: Way) -> int:
        """The other roles whose goods the way takes or needs straight in — whom its capsule trades with — at fewest."""
        own = self.cat.role(way)
        open_ = []
        for _, ref in way.inputs:
            makers = {self.cat.role(w) for w in self.made.get(ref, []) if isinstance(w, Way)}
            if any(not isinstance(w, Way) for w in self.made.get(ref, [])):
                makers.add(None)
            if makers and not ({None, own} & makers):
                open_.append(makers)
        chosen = 0
        while open_:
            pick = max({r for m in open_ for r in m}, key=lambda r: sum(r in m for m in open_))
            open_ = [m for m in open_ if pick not in m]
            chosen += 1
        return chosen

    def item_door_reach(self, item_id: str) -> int:
        ways = [w for w in self.made.get(item_id, []) if isinstance(w, Way)]
        if len(ways) < len(self.made.get(item_id, [])) or not ways:
            return 0
        return min(self.door_reach(w) for w in ways)

    def sources(self, stat: str) -> list[Source]:
        better = self.cat.stats[stat][1]
        found = []
        for item in self.cat.items.values():
            value = 0.0
            for s, amount, rate in item.effects:
                if s == stat and amount * better > 0:
                    value += abs(amount) * ((item.decay_h or DEFAULT_LIFE_H) if rate else 1)
            if value > 0 and item.id in self.chain:
                found.append(Source(f"{item.id} {item.name}", item.where, item.sub, value, self.reach[item.id],
                                    self.chain[item.id][0], self.cost.get(item.id, math.inf), item.kind == "durable"))
        for way in self.cat.ways:
            value = sum(abs(a) for s, a in way.gives if s == stat and a * better > 0)
            roles = self.roles_of_way(way)
            if value > 0 and roles is not None:
                found.append(Source(f"way {way.label}", way.where, way.sub, value,
                                    len(roles - {self.cat.role(way)}), roles, self.way_cost(way), False))
        return found


def derive(cat: Catalogue) -> Derived:
    if "_derived" not in cat.__dict__:
        cat.__dict__["_derived"] = Derived(cat)
    return cat.__dict__["_derived"]


def histogram(measure: dict[str, int], items: list[Item]) -> dict[int, int]:
    counts: dict[int, int] = {}
    for item in items:
        if item.id in measure:
            k = min(measure[item.id], len(REACH_NAMES) - 1)
            counts[k] = counts.get(k, 0) + 1
    return counts


def spread(ways: dict[str, list], items: list[Item]) -> str:
    """How many items have one way, two, three, four or more."""
    counts = [0] * 5
    for item in items:
        counts[min(len(ways.get(item.id, [])), 4)] += 1
    return ", ".join(f"{label} {counts[k]}" for k, label in enumerate(["none", "1", "2", "3", "4+"]) if counts[k])


# ---- the audit


def audit(cat: Catalogue, only: str | None, limit: int) -> int:
    """What every rule allows and a review would not: each finding counted, and its first few named."""
    if only and not SUB.match(only):
        cli.fail(f"audit narrows to a subsection code, not {only!r}")
    d = derive(cat)
    mine = [i for i in cat.items.values() if not only or i.sub == only]
    ways = [w for w in cat.ways if not only or w.sub == only]
    takers = {i: [w for w in d.ended[i] if isinstance(w, Way)] for i in cat.items}
    makers = {i: [w for w in d.made[i] if isinstance(w, Way)] for i in cat.items}
    findings: list[tuple[str, list[str]]] = []

    findings.append(("dead end — no use, and no way takes or needs it: it exists only to decay",
                     [f"{i.id} {i.name}" for i in mine if not i.has_use and not takers[i.id] and not d.needed[i.id]]))
    findings.append(("pass-through — no use, made by one way and taken by one way, each of one item",
                     [f"{i.id} {i.name}: {makers[i.id][0].name} → {takers[i.id][0].name}" for i in mine
                      if not i.has_use and len(d.made[i.id]) == 1 and len(takers[i.id]) == 1 and makers[i.id]
                      and len(makers[i.id][0].makes) == 1
                      and len([r for _, r in takers[i.id][0].takes if r != POWER]) == 1]))
    findings.append(("dominated — another way by the same hands makes as much of the same from less, no slower",
                     [f"{b.label} by {a.name!r} ({b.where})" for a, b in dominated(cat, ways)]))
    findings.append(("twin names — one thing, written twice", twins(mine if only else list(cat.items.values()))))
    findings.append(("rate on a tool — a durable some way also needs: the rate pays twice (ECO-11)",
                     [f"{i.id} {i.name}" for i in mine if i.kind == "durable" and d.needed[i.id]]))
    if only:
        findings.append(("rates — every durable, to read against ECO-11: does it work without the crew's time?",
                         [f"{i.id} {i.name}: {i.use}" for i in mine if i.kind == "durable"]))

    parts = [i for i in mine if i.fits or i.installs]
    by_hand = [w for w in ways if w.makes and all(cat.items.get(r) and (cat.items[r].fits or cat.items[r].installs)
                                                  for _, r in w.makes) and cat.role(w) is None]
    devices = [x for x in cat.devices.values() if x.role != UNIVERSAL and (not only or x.id.startswith(only + "."))]
    runs = {x.id: sum(1 for w in cat.ways if w.by == x.id) for x in devices}
    bench = [w for w in ways if cat.role(w) is None]
    kinds = histogram_by(d.kind(i) for i in mine)
    print(f"{len(mine)} items, {len(ways)} ways, {len(devices)} devices; "
          + ", ".join(f"{k} {n}" for k, n in sorted(kinds.items())))
    print(f"parts and kits: {len(parts)} items ({len(parts) * 100 // max(len(mine), 1)} %), "
          f"{len(by_hand)} of their ways on the bench or by hand")
    print(f"ways by no role (bench, fixtures, crew): {len(bench)} ({len(bench) * 100 // max(len(ways), 1)} %)")
    print("ways a device runs: " + ", ".join(f"{k} {v}" for k, v in sorted(histogram_of(runs.values()).items())))
    for title, names in findings:
        print(f"{title}: {len(names)}")
        for line in names[: limit or None]:
            print("  " + line)
        if limit and len(names) > limit:
            print(f"  … {len(names) - limit} more")
    return 0


def histogram_of(values) -> dict[int, int]:
    return histogram_by(min(v, 9) for v in values)


def histogram_by(keys) -> dict:
    counts: dict = {}
    for k in keys:
        counts[k] = counts.get(k, 0) + 1
    return counts


def dominated(cat: Catalogue, ways: list[Way]) -> list[tuple[Way, Way]]:
    """
    (a, b) where b makes no item a does not, needs and takes at least what a does, is no faster and gives nothing a does
    not.
    """
    by_made: dict[tuple, list[Way]] = {}
    for w in cat.ways:
        by_made.setdefault((cat.role(w), frozenset(r for _, r in w.makes)), []).append(w)
    found = []
    for b in ways:
        for a in by_made[(cat.role(b), frozenset(r for _, r in b.makes))]:
            if a is b or a.minutes > b.minutes:
                continue
            ta, tb, ma, mb = dict((r, n) for n, r in a.inputs), dict((r, n) for n, r in b.inputs), \
                dict((r, n) for n, r in a.makes), dict((r, n) for n, r in b.makes)
            if all(tb.get(r, 0) >= n for r, n in ta.items()) and all(ma[r] >= n for r, n in mb.items()) \
                    and dict(a.gives) == dict(b.gives) and (ta, ma, a.minutes) != (tb, mb, b.minutes):
                found.append((a, b))
                break
    return found


def twins(items: list[Item]) -> list[str]:
    """Names alike once case, spaces, hyphens and a plural s are set aside."""
    def key(n: str) -> str:
        return re.sub(r"(ies|es|s)\b", "", n.lower()).replace(" ", "").replace("-", "")
    groups: dict[str, list[Item]] = {}
    for i in items:
        groups.setdefault(key(i.name), []).append(i)
    return [", ".join(f"{i.id} {i.name}" for i in g) for g in groups.values() if len(g) > 1]


# ---- one item


def list_items(cat: Catalogue, only: str | None) -> int:
    """A line a device and an item: what a way may name, without reading the files."""
    if only and not SUB.match(only):
        cli.fail(f"list narrows to a subsection code, not {only!r}")
    for code, sub in cat.subs.items():
        if only and code != only:
            continue
        print(f"## {code} {sub.name} ({sub.section})" + (" — not written" if code in cat.missing else ""))
        for device in cat.devices.values():
            if device.id.split(".")[0] == code:
                print(f"{device.id} {device.name} [{device.role}]")
        for item in cat.items.values():
            if item.sub == code:
                print(f"{item.id} {item.name}" + ("" if item.use in BLANK else f" — {item.use}"))
    return 0


def show_item(cat: Catalogue, ref: str | None, depth: int) -> int:
    if not ref or ref not in cat.items:
        cli.fail(f"no item {ref!r} in {CATALOG}: give an id like wat-002")
    d = derive(cat)
    item = cat.items[ref]
    roles = d.chain.get(ref, (frozenset(), None))[0]
    print(f"{item.id} {item.name} — {d.kind(item)}, depth {d.depth.get(ref, '—')}, "
          f"{REACH_NAMES[min(d.reach.get(ref, 0), 3)]} reach ({', '.join(sorted(roles)) or 'no role'}), "
          f"{d.cost.get(ref, math.inf):.0f} work-min, {item.where}")
    if item.use not in BLANK:
        print(f"use: {item.use}")
    if item.decay_h is not None:
        print(f"decays: {item.decay_h:g} h" + (f" → {name(cat, item.decays_to)}" if item.decays_to else ""))
    if ref in cat.stock:
        print("the ship's stock: aboard at launch, finite, and made from nothing outside it")
    print(f"made {len(d.made[ref])} ways:")
    for line in describe(cat, d.made[ref], ref, made=True):
        print("  " + line)
    print(f"ended {len(d.ended[ref])} ways:")
    for line in describe(cat, d.ended[ref], ref, made=False):
        print("  " + line)
    if d.needed[ref]:
        print(f"needed by {len(d.needed[ref])} ways:")
        for way in d.needed[ref]:
            print("  " + way_text(cat, way))
    print("cheapest chain:")
    for line in chain(cat, d, ref, depth or 12):
        print("  " + line)
    return 0


def name(cat: Catalogue, ref: str) -> str:
    return f"{ref} {cat.items[ref].name}" if ref in cat.items else ref


def way_text(cat: Catalogue, way: Way) -> str:
    takes = ", ".join(f"{n} {name(cat, r)}" for n, r in way.takes) or "nothing"
    makes = ", ".join(f"{n} {name(cat, r)}" for n, r in way.makes)
    gives = ", ".join(f"{s} {a:+g}" for s, a in way.gives)
    needs = ", ".join(f"{n} {name(cat, r)}" for n, r in way.needs)
    return (f"{way.label}, {way.minutes:g} min" + (f", with {needs}" if needs else "") + f": {takes} → "
            + "; ".join(p for p in (makes, gives) if p))


def describe(cat: Catalogue, sources: list[Way | Item], ref: str, made: bool) -> list[str]:
    lines = []
    for s in sources:
        if isinstance(s, Way):
            lines.append(way_text(cat, s))
        elif s.id == ref:
            lines.append("; ".join(p for p in ("used: " + s.use if s.has_use else "",
                                                f"decays after {s.decay_h:g} h" if s.decay_h is not None else "") if p))
        elif made and s.decays_to == ref:
            lines.append(f"decay of {s.id} {s.name}, after {s.decay_h:g} h")
        else:
            lines.append(f"left by using {s.id} {s.name}")
    return lines


def chain(cat: Catalogue, d: Derived, ref: str, depth: int, count: int = 1, indent: str = "",
          seen: set | None = None, tool: bool = False) -> list[str]:
    """
    The item by its cheapest way and that way's tools and inputs, down to nothing; an item already drawn is named
    only.
    """
    seen = set() if seen is None else seen
    ways = [w for w in d.made.get(ref, []) if isinstance(w, Way)]
    best = min(ways, key=d.way_cost, default=None)
    via = "a leftover" if best is None else f"{best.label}, {best.minutes:g} min"
    again = ref in seen and best is not None and best.inputs
    lines = [f"{indent}{count} × {name(cat, ref)}" + (" (tool)" if tool else "") + f" ← {via}"
             + (" — above" if again else "")]
    seen.add(ref)
    if best is None or again or depth <= 1:
        return lines
    for n, needed in best.needs:
        lines += chain(cat, d, needed, depth - 1, n, indent + "  ", seen, tool=True)
    for n, taken in best.takes:
        lines += chain(cat, d, taken, depth - 1, n, indent + "  ", seen)
    return lines


# ---- the tree


def write_tree(base: Path, cat: Catalogue) -> int:
    if cat.missing:
        cli.fail(f"{len(cat.missing)} subsections have no file yet: {', '.join(cat.missing)}")
    (base / TREE_MD).write_text(tree_markdown(cat), encoding="utf-8")
    (base / TREE_SVG).write_text(sub_map(cat), encoding="utf-8")
    print(f"wrote {TREE_MD} and {TREE_SVG}")
    return 0


def sub_edges(cat: Catalogue, without: str | None = None) -> dict[tuple[str, str], int]:
    """How many way inputs cross from one subsection into another's items, leaving out the item `without`."""
    edges: dict[tuple[str, str], int] = {}
    for way in cat.ways:
        into = {ref[:3] for _, ref in way.makes}
        for _, taken in way.inputs:
            for dst in into - {taken[:3]}:
                if taken != without:
                    edges[(taken[:3], dst)] = edges.get((taken[:3], dst), 0) + 1
    return edges


def folded(edges: dict[tuple[str, str], int], key) -> dict[tuple[str, str], int]:
    out: dict[tuple[str, str], int] = {}
    for (src, dst), n in edges.items():
        a, b = key(src), key(dst)
        if a and b and a != b:
            out[(a, b)] = out.get((a, b), 0) + n
    return out


def role_edges(cat: Catalogue) -> dict[tuple[str, str], int]:
    """How many way inputs pass from a role's devices to another role's devices, by each item's commonest maker."""
    maker: dict[str, str] = {}
    for way in cat.ways:
        role = cat.role(way)
        for _, ref in way.makes:
            if role and ref != POWER:
                maker.setdefault(ref, role)
    edges: dict[tuple[str, str], int] = {}
    for way in cat.ways:
        dst = cat.role(way)
        for _, ref in way.inputs:
            src = maker.get(ref)
            if src and dst and src != dst:
                edges[(src, dst)] = edges.get((src, dst), 0) + 1
    return edges


def flowchart(nodes: dict[str, str], edges: dict[tuple[str, str], int]) -> list[str]:
    out = ["```mermaid", "flowchart LR"] + [f"  {k}[\"{v}\"]" for k, v in nodes.items()]
    for node in nodes:
        into = sorted(((n, src) for (src, dst), n in edges.items() if dst == node), reverse=True)[:DIAGRAM_SUPPLIERS]
        out += [f"  {src} -->|{n}| {node}" for n, src in into]
    return out + ["```"]


def tree_markdown(cat: Catalogue) -> str:
    d = derive(cat)
    items = list(cat.items.values())
    devices = [x for x in cat.devices.values() if x.role != UNIVERSAL]
    out = [
        "# The resource tree",
        "",
        f"Generated by `qq economy tree` from the catalogue ([../catalog/sections.md](../catalog/sections.md)); edit "
        f"the catalogue, never this file. What it means is [design.md](design.md). Every item can be browsed with "
        f"`qq economy explore`, and one printed with `qq economy item <id>`.",
        "",
        f"**{len(items)} items** in {len(cat.subs)} subsections of {len(cat.sections)} sections, made and ended by "
        f"**{len(cat.ways)} ways** on {len(devices)} devices across {len(cat.roles)} roles, the universal fixtures and "
        f"the crew's own hands.",
        "",
        "- **Made**, the ways an item is had — made by a way, left by a use, decayed into: " + spread(d.made, items) + ".",
        "- **Ended**, the ways it goes — taken by a way, used, decayed: " + spread(d.ended, items) + ".",
        "- **Reach**, the fewest other roles any way to it takes, down to nothing: "
        + ", ".join(f"{REACH_NAMES[k]} {v}" for k, v in sorted(histogram(d.reach, items).items())) + ".",
        "- **Door reach**, the fewest other roles whose goods a way to it takes straight in — the neighbours it trades "
        "with: " + ", ".join(f"{REACH_NAMES[k]} {v}" for k, v in sorted(histogram(
            {i.id: d.item_door_reach(i.id) for i in items}, items).items())) + ".",
        "",
        "## How the sections feed each other",
        "",
        f"Each section and its {DIAGRAM_SUPPLIERS} biggest suppliers; an arrow's number is how many way inputs cross it. "
        f"Power ({POWER}), which most ways take, is left off.",
        "",
        *flowchart(cat.sections, folded(sub_edges(cat, POWER), lambda s: cat.subs[s].section if s in cat.subs else None)),
        "",
        "## How the roles feed each other",
        "",
        f"Each role — a capsule, on a ship that lays one role a capsule — and its {DIAGRAM_SUPPLIERS} biggest suppliers, "
        "by the role that most often makes each input.",
        "",
        *flowchart(cat.roles, role_edges(cat)),
        "",
        "## The subsections, shallow to deep",
        "",
        f"The subsections in {MAP_COLUMNS} columns by their items' mean depth — the rounds of ways from nothing — coloured "
        f"by section, each with arrows from its {MAP_SUPPLIERS} biggest suppliers (at least {MAP_EDGE_LEAST} way inputs; "
        f"dashed where the supplier sits further right). Power is left off.",
        "",
        "![The subsections by depth](resource-map.svg)",
        "",
        "## The subsections",
        "",
        "| subsection | section | ways | made 1 · 2 · 3 · 4+ | ended 1 · 2 · 3 · 4+ | reach: solo · pair · trio · crew "
        "| takes most from |",
        "|---|---|---|---|---|---|---|",
    ]
    edges = sub_edges(cat)
    for code, sub in cat.subs.items():
        mine = [i for i in items if i.sub == code]
        ways = sum(1 for w in cat.ways if w.sub == code)
        made = " · ".join(str(sum(1 for i in mine if min(len(d.made[i.id]), 4) == k)) for k in range(1, 5))
        ended = " · ".join(str(sum(1 for i in mine if min(len(d.ended[i.id]), 4) == k)) for k in range(1, 5))
        h = histogram(d.reach, mine)
        suppliers = sorted(((n, src) for (src, dst), n in edges.items() if dst == code), reverse=True)[:4]
        out.append(f"| [{code}](../catalog/{code}.md) {sub.name} | {sub.section} | {ways} | {made} | {ended} | "
                   + " · ".join(str(h.get(k, 0)) for k in range(len(REACH_NAMES))) + " | "
                   + ", ".join(f"{src} {n}" for n, src in suppliers) + " |")

    out += ["", "## How the common goods flow", "",
            f"Each pinned item ([../catalog/sections.md](../catalog/sections.md#pinned-items)): every way it is made and "
            f"ended, counted, and the first {FLOW_SHOWN} of each.", ""]
    for ref in cat.pinned:
        if ref not in cat.items:
            continue
        out += [f"### {ref} {cat.items[ref].name}", "",
                f"Made {len(d.made[ref])} ways, ended {len(d.ended[ref])} ways.", "", "| made by | ended by |", "|---|---|"]
        made = describe(cat, d.made[ref], ref, True)[:FLOW_SHOWN]
        ended = describe(cat, d.ended[ref], ref, False)[:FLOW_SHOWN]
        for k in range(max(len(made), len(ended))):
            cell = [(made[k] if k < len(made) else ""), (ended[k] if k < len(ended) else "")]
            out.append("| " + " | ".join(c.replace("|", "/") for c in cell) + " |")
        out.append("")

    out += ["## Where each stat comes from", "",
            "The best source of each stat at each reach — an item used or a way run: what it gives, its work-minutes, "
            "and what a work-minute buys. A durable's points are its rate over its life.", ""]
    for stat in cat.stats:
        sources = d.sources(stat)
        out += [f"### `{stat}`", "", f"{len(sources)} sources.", ""]
        if not sources:
            continue
        out += ["| reach | best source | points | work-min | points a work-min |", "|---|---|---|---|---|"]
        for k, label in enumerate(REACH_NAMES):
            at = [s for s in sources if min(s.reach, len(REACH_NAMES) - 1) == k]
            if at:
                s = max(at, key=lambda x: x.value)
                out.append(f"| {label} ({len(at)}) | {s.label} | {s.value:g} | {s.cost:.0f} | "
                           f"{s.value / s.cost if s.cost else 0:.2f} |")
        out.append("")

    out += ["## The chains behind the crew's needs", "",
            "Each need's best item, by its cheapest way down to nothing: `count × item ← way (by), minutes`.", ""]
    for stat, (of, *_) in cat.stats.items():
        best = max((s for s in d.sources(stat) if not s.label.startswith("way ")), key=lambda s: s.value, default=None)
        if of == "crew" and best:
            out += [f"### `{stat}` — {best.label}", "", "```", *chain(cat, d, best.label[:7], 12), "```", ""]

    out += ["## Balance flags", "",
            f"Sources {OUTLIER_FACTOR}× cheaper or dearer, a point, than their stat's median of their kind.", ""]
    flagged = outliers(cat, d)
    out += ["| source | stat | points a work-min | stat's median |", "|---|---|---|---|"] if flagged else ["None."]
    out += [f"| {s.label} | {stat} | {r:.2f} | {m:.2f} |" for s, stat, r, m in flagged]
    return "\n".join(out) + "\n"


def outliers(cat: Catalogue, d: Derived) -> list[tuple[Source, str, float, float]]:
    """Each stat's sources against their own kind's median: a durable's life-long points are no peer of a one-shot's."""
    flagged = []
    for stat in cat.stats:
        for durable in (False, True):
            rates = [(s, s.value / s.cost) for s in d.sources(stat) if 0 < s.cost < math.inf and s.durable == durable]
            if len(rates) < 3:
                continue
            median = statistics.median(r for _, r in rates)
            kind = f"{stat} ({'durable' if durable else 'one-shot'})"
            flagged += [(s, kind, r, median) for s, r in rates
                        if r > median * OUTLIER_FACTOR or r < median / OUTLIER_FACTOR]
    return sorted(flagged, key=lambda f: -max(f[2] / f[3], f[3] / f[2]))


def colours(keys) -> dict[str, str]:
    keys = list(keys)
    return {k: f"hsl({round(i * 360 / len(keys))}, 55%, 48%)" for i, k in enumerate(keys)}


def sub_map(cat: Catalogue) -> str:
    """
    The subsections as boxes in even columns, shallow to deep by their items' mean depth, each with arrows from its
    biggest suppliers, coloured by the supplier's section. Power, which most ways take, would be an arrow into every
    box, so it is left off.
    """
    d = derive(cat)
    col_w, box_w, box_h, gap, margin = 214, 176, 30, 10, 40
    tint = colours(cat.sections)
    order = list(cat.sections)
    mean = {code: statistics.mean([d.depth.get(i.id, 0) for i in cat.items.values() if i.sub == code] or [0])
            for code in cat.subs}
    ranked = sorted(cat.subs, key=mean.get)
    per_column = math.ceil(len(ranked) / MAP_COLUMNS)
    columns = [ranked[k:k + per_column] for k in range(0, len(ranked), per_column)]
    at: dict[str, tuple[float, float]] = {}
    for c, codes in enumerate(columns):
        codes.sort(key=lambda code: order.index(cat.subs[code].section))
        for k, code in enumerate(codes):
            at[code] = (margin + c * col_w, margin + 30 + k * (box_h + gap))
    width = margin * 2 + len(columns) * col_w - (col_w - box_w)
    legend_y = margin + 30 + per_column * (box_h + gap) + 20
    height = legend_y + math.ceil(len(cat.sections) / 6) * 22 + margin

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" '
           'font-family="sans-serif" font-size="12">',
           f'<rect width="{width}" height="{height}" fill="#fbfaf7"/>']
    for c, codes in enumerate(columns):
        low, high = min(mean[x] for x in codes), max(mean[x] for x in codes)
        svg.append(f'<text x="{margin + c * col_w + box_w / 2}" y="{margin}" text-anchor="middle" fill="#555">'
                   f'mean depth {low:.1f}–{high:.1f}</text>')
    edges = sub_edges(cat, without=POWER)
    drawn = []
    for dst in cat.subs:
        into = sorted(((n, src) for (src, t), n in edges.items() if t == dst and n >= MAP_EDGE_LEAST and src in at),
                      reverse=True)
        drawn += [(n, src, dst) for n, src in into[:MAP_SUPPLIERS]]
    for n, src, dst in sorted(drawn):
        (x1, y1), (x2, y2) = at[src], at[dst]
        y1, y2 = y1 + box_h / 2, y2 + box_h / 2
        forward = x2 > x1
        x1, x2 = (x1 + box_w, x2) if forward else (x1, x2 + box_w)
        bend = max(50, abs(x2 - x1) / 2) * (1 if forward else -1)
        svg.append(f'<path d="M{x1},{y1} C{x1 + bend},{y1} {x2 - bend},{y2} {x2},{y2}" fill="none" '
                   f'stroke="{tint[cat.subs[src].section]}" stroke-opacity="{0.5 if forward else 0.2}" '
                   f'stroke-width="{1 + math.log2(n):.1f}"' + ("" if forward else ' stroke-dasharray="5 4"') + "/>")
    for code, (x, y) in at.items():
        sub = cat.subs[code]
        svg.append(f'<rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" rx="5" fill="{tint[sub.section]}"/>'
                   f'<text x="{x + 7}" y="{y + 20}" fill="#fff"><tspan font-weight="bold">{code}</tspan> '
                   f'{html.escape(sub.name[:23])}</text>')
    for k, (section, title) in enumerate(cat.sections.items()):
        x, y = margin + (k % 6) * 170, legend_y + (k // 6) * 22
        svg.append(f'<rect x="{x}" y="{y - 10}" width="12" height="12" rx="2" fill="{tint[section]}"/>'
                   f'<text x="{x + 18}" y="{y}" fill="#333">{html.escape(title)}</text>')
    svg.append("</svg>")
    return "\n".join(svg) + "\n"


# ---- the explorer


def write_explorer(base: Path, cat: Catalogue, out: Path) -> int:
    if cat.missing:
        cli.fail(f"{len(cat.missing)} subsections have no file yet: {', '.join(cat.missing)}")
    d = derive(cat)
    template = base / ".qq" / "_economy_page.html"
    data = {
        "roles": cat.roles,
        "sections": cat.sections,
        "subs": {c: {"name": s.name, "section": s.section} for c, s in cat.subs.items()},
        "devices": {x.id: {"name": x.name, "role": x.role} for x in cat.devices.values()},
        "toolLifeH": TOOL_LIFE_H,
        "items": [{"id": i.id, "name": i.name, "kind": d.kind(i), "stock": i.id in cat.stock, "use": "" if i.use in BLANK else i.use,
                   "decayH": i.decay_h, "decaysTo": i.decays_to, "depth": d.depth.get(i.id),
                   "reach": d.reach.get(i.id), "doorReach": d.item_door_reach(i.id),
                   "roles": sorted(d.chain.get(i.id, (frozenset(), None))[0]),
                   "cost": None if d.cost.get(i.id, math.inf) == math.inf else round(d.cost[i.id], 1)}
                  for i in cat.items.values()],
        "ways": [{"name": w.name, "by": w.by, "min": w.minutes, "needs": w.needs, "takes": w.takes, "makes": w.makes,
                  "gives": [f"{s} {a:+g}" for s, a in w.gives]} for w in cat.ways],
    }
    page = template.read_text(encoding="utf-8").replace("/*DATA*/null", json.dumps(data, separators=(",", ":")))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"wrote {_sim.rel(base, out)} ({len(page) // 1024} KiB)")
    return 0


if __name__ == "__main__":
    cli.entry(main)
