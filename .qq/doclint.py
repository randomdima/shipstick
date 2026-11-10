"""
Check the rules and the doc comments against what they cite: nothing stated twice, nothing cited
that is not there.

A comment cites a rule by ID and a type by cref, and no compiler checks either — the build
generates no XML documentation, so a renamed rule and a renamed member both leave citations
pointing at nothing. Five questions, asked of the documents and the source themselves:

    stated twice       two documents claim the same ID — one of them is a copy, and copies drift
    cited by code      a doc comment cites a rule no document states: a typo, or a rule that went
    outside the map    a family docs/index.md never names, so nothing points a reader at it
    carries no rung    a rule that does not say whose it is (docs/priority.md)
    cref names nothing a doc comment cites a member its type does not have (_crefs)

Exit 1 if any of the five has an answer. A rule the code has no reason to cite is normal and only counted.

`--build` asks the compiler a sixth: whether every doc comment of the game is well-formed XML, sits on a member,
names only parameters the member has and cites only members that resolve. A build of each game project with its
documentation file on, into a folder of its own, so it is asked for by name.
"""

from __future__ import annotations

import argparse
import re

import _crefs
import _docs
import _sim
from common import cli

#: The document that maps a family to the document stating it (docs/index.md, "Where each requirement ID lives").
MAP = "docs/index.md"

#: What `--build` may take: a build of each game project. The scan alone is a second.
TIMEOUT_S = 600

#: Where the documented builds land, so the ordinary one is left alone.
BUILD_OUT = ".tmp/doclint-build"

#: Badly formed XML, a param tag naming nothing, one named twice, a cref that resolves to nothing, a
#: cref the compiler cannot parse, a doc comment on no member, a paramref naming nothing.
MALFORMED = re.compile(r"(?P<path>[^\s(]+\.cs)\((?P<line>\d+),\d+\): warning "
                       r"(?P<code>CS157[0-24]|CS1584|CS1587|CS1734): "
                       r"(?P<text>[^\[]+)")


def main():
    a = parse_args()
    base = _sim.root()
    if not (base / MAP).is_file():
        cli.fail(f"no {MAP} to check the families against")

    found = _docs.audit(base, MAP)
    crefs, dangling = _crefs.scan(base)

    report("rules stated twice", found.twice, a.limit, lambda sites: ", ".join(str(site) for site in sites))
    report("cited by code, but no document states it", found.dangling, a.limit, describe)
    report("stated without a rung — see docs/priority.md", found.unrunged, a.limit, describe)
    report("cited by a doc comment, but its type has no such member", dangling, a.limit, describe, key=str)
    if found.unmapped:
        print(f"\nfamilies {MAP} does not name ({len(found.unmapped)}):")
        for prefix, where in sorted(found.unmapped.items()):
            print(f"  {prefix:<6} stated in {where}")

    if a.prose:
        report("named only in prose", found.prose_only, a.limit, describe)

    malformed = compiled(base) if a.build else None
    if malformed:
        sites = sorted((code, site) for code, found in malformed.items() for site in found)
        print(f"\ndoc comments the compiler cannot read ({len(sites)}):")
        for code, site in sites[: a.limit or None]:
            print(f"  {code:<10} {site}  {site.text[:72]}")
        if a.limit and len(sites) > a.limit:
            print(f"  … {len(sites) - a.limit} more (--limit=0 for all)")

    uncited = [ident for ident in found.defined if ident not in found.cited]
    print(f"\n{len(found.defined)} rules, {sum(len(sites) for sites in found.cited.values())} citations, "
          f"{len(uncited)} rules nothing cites, {len(found.prose_only)} numbers named only in prose")
    print(f"{crefs} crefs, {len(dangling)} of them naming nothing")
    if malformed is not None:
        print(f"{sum(len(sites) for sites in malformed.values())} doc comments the compiler cannot read")
    print(rungs(found.defined))
    return 0 if found.sound and not dangling and not malformed else 1


def compiled(base) -> dict[str, list[_docs.Site]]:
    """Each game project built with its documentation file on, and every malformed doc comment it warned about."""
    text = ""
    for project in (_sim.GAME, _sim.HOST):
        out = f"{BUILD_OUT}/{project.rsplit('/', 1)[-1].removesuffix('.csproj')}"
        built = _sim.dotnet(base, "build", project, "-c", "Release", "-p:GenerateDocumentationFile=true",
                            "-p:NoWarn=CS1591", "-o", out, "-v", "q", "--nologo",
                            # An up-to-date build compiles nothing and so warns about nothing.
                            "--no-incremental")
        if built.code != 0:
            cli.fail(f"the documented build of {project} failed — "
                     f"{_sim.write_log(base, 'doclint', built.stdout + built.stderr)}")
        text += built.stdout + built.stderr

    found: dict[str, list[_docs.Site]] = {}
    seen: set[tuple[str, int, str]] = set()
    for match in MALFORMED.finditer(text):
        path = _sim.rel(base, (base / match.group("path")).resolve())
        number = int(match.group("line"))
        said = match.group("text").strip()
        if (path, number, said) in seen:
            continue
        seen.add((path, number, said))
        found.setdefault(match.group("code"), []).append(_docs.Site(path, number, said))
    return found


def rungs(defined: dict[str, list]) -> str:
    """How the rules are spread over the ladder, owner's band first — the shape of the register."""
    counted: dict[str, int] = {}
    for sites in defined.values():
        for site in sites:
            counted[site.rung or "—"] = counted.get(site.rung or "—", 0) + 1
    owned = sum(counted.get(rung, 0) for rung in _docs.OWNER_RUNGS)
    spread = "  ".join(f"{rung} {counted[rung]}" for rung in sorted(counted))
    return f"{owned} of them the owner's ({'/'.join(_docs.OWNER_RUNGS)}).  {spread}"


def report(title: str, hits: dict[str, list], limit: int, detail, key=_docs.sort_key) -> None:
    """One question's answers, or its silence."""
    if not hits:
        return
    print(f"\n{title} ({len(hits)}):")
    for ident in sorted(hits, key=key)[: limit or None]:
        print(f"  {ident:<10} {detail(hits[ident])}")
    if limit and len(hits) > limit:
        print(f"  … {len(hits) - limit} more (--limit=0 for all)")


def describe(sites: list) -> str:
    """Where a citation is, and the line it sits on — enough to fix it without opening the file."""
    first = sites[0]
    more = f" (+{len(sites) - 1} more)" if len(sites) > 1 else ""
    return f"{first}{more}  {first.text[:72]}"


def parse_args():
    parser = argparse.ArgumentParser(
        prog="qq doclint",
        description="Check that every rule is stated once, and that every citation — a rule ID or a "
                    "doc comment's cref — resolves.",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--limit", type=cli.counting, default=20, metavar="INT",
                        help="max rows per question (0 = no limit)")
    parser.add_argument("--prose", action="store_true",
                        help="list the numbers named only in prose, and where — a retirement being "
                             "explained, or an ID that has lost its statement")
    parser.add_argument("--build", action="store_true",
                        help="also build the game with its documentation file on and report every doc "
                             "comment that is not well-formed XML, names a parameter it does not have or "
                             "cites a member that does not resolve (tests' own comments are not in it)")
    return parser.parse_args()


if __name__ == "__main__":
    cli.entry(main)
