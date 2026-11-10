"""
Build the game, run the suite, check the citations, the art's provenance, the model rules and the page's art.

The standard build-and-test route, so a check does not need approving every time it is run. The suite is
`qq tests all`'s and is run through it rather than copied. The citations are what nothing else checks: a doc comment
naming a rule that was renumbered compiles, passes and misleads (`qq doclint` is the whole report). The provenance is
the other: every image under assets/ traces to the prompt that made it, or is on the legacy list
(`qq sprites check` is the whole report). The model rules are the third: what `qq shapes` refuses in a model — one
item inside another, an item resting on nothing, a picture stretched (GAM-14) — proved on fixtures, so a change to the tool cannot loosen it unseen (`qq shapes selftest`).
The page's art is the fourth: no image the stylesheet places is stretched, and none it repeats shows a seam (GAM-14;
`qq fit` is the whole report).

What is printed is the few lines worth reading; what the run saw is kept whole under .tmp/logs/.
"""

from __future__ import annotations

import argparse

import _docs
import _sim
import sprites
import tests
from common import cli

#: What a call may take: a build, the suite and two scans.
TIMEOUT_S = 1800

#: The document whose ID map the families are checked against, as `qq doclint` checks it.
MAP = "docs/index.md"


def main():
    a = parse_args()
    base = _sim.root()
    log = []
    _sim.lighten(a.full)

    print("=== build")
    built = _sim.dotnet(base, "build", _sim.MARKER, *_sim.light_build())
    log.append("=== build\n" + built.stdout + built.stderr)
    _sim.show(built.stdout, r"error|warning CS|Build succeeded|Build FAILED")
    if built.code != 0:
        # Never run the suite against the last good assembly: the results would look real.
        _sim.write_log(base, "checks", "\n".join(log))
        print("=== status 1 (build failed)")
        return 1

    status = tests.suite(base, tests.ALL, log)
    status = citations(base) or status
    status = provenance(base) or status
    status = model_rules() or status
    status = page_art(base) or status

    _sim.write_log(base, "checks", "\n".join(log))
    print(f"=== status {status}")
    return status


def citations(base):
    """The rules against the code that cites them; the whole report is `qq doclint`."""
    found = _docs.audit(base, MAP)
    if found.sound:
        print(f"=== citations ok ({len(found.defined)} rules, "
              f"{sum(len(sites) for sites in found.cited.values())} citations)")
        return 0

    print(f"=== citations: {len(found.twice)} stated twice, {len(found.dangling)} cited by code and "
          f"stated nowhere, {len(found.unmapped)} families off the map, {len(found.unrunged)} with no "
          f"rung — qq doclint says which")
    return 1


def provenance(base):
    """
    Every image under assets/ traces to its prompt or is on the legacy list, and every kept texture, part and model
    is catalogued; the whole report is `qq sprites check`.
    """
    import _catalog

    problems = sprites.audit(base) + _catalog.problems(base)
    print(f"=== provenance: {len(problems)} problem(s) — qq sprites check says which" if problems
          else "=== provenance ok")
    return 1 if problems else 0


def model_rules():
    """The rules `qq shapes` holds a model to still hold; the whole report is `qq shapes selftest`."""
    import _shapes_selftest

    failed = _shapes_selftest.run()
    print(f"=== model rules: {len(failed)} broken — qq shapes selftest says which" if failed else "=== model rules ok")
    return 1 if failed else 0


def page_art(base):
    """The page shows every image at its own proportions and repeats only what tiles (GAM-14); the whole report is
    `qq fit`."""
    import fit

    found = fit.audit(base, base / fit.STYLE)
    print(f"=== page art: {len(found)} stretched or seamed — qq fit says which" if found else "=== page art ok")
    return 1 if found else 0


def parse_args():
    parser = argparse.ArgumentParser(
        prog="qq checks",
        description="Build the game, run the suite, check the citations, the art's provenance, the model rules and the page's art.",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--full", action="store_true",
                        help="build and test on every core at normal priority, rather than light (qq tests --help)")
    return parser.parse_args()


if __name__ == "__main__":
    cli.entry(main)
