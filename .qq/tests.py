"""
Run one or more tiers of the test suite, each in the configuration its answer is true in.

The suite is selected by `Tier` (src/tests/Tier.cs), not by folder, because cost does not follow the slice tree. A
tier is run when it is named, and naming several runs several. Nothing is implied by anything.

    qq tests                    unit                 after every edit
    qq tests all                every tier in ALL    before a commit
    qq tests --changed          whatever the working tree has moved, and nothing else
    qq tests --name=ShipGrid    one class or one case, while fixing it

A new tier is a constant on `Tier`, a row in `TIERS` here (and in `ALL` if it costs no money and needs nobody to
look at a picture), rows in `SELECT` for the paths that can move it, and a line in docs/verification.md.

**A run is light unless `--full` is given**: at a low priority and on half the cores, so the machine stays usable.

Output is the summary line per take; the whole of what the run saw is kept under .tmp/logs/.
"""

from __future__ import annotations

import argparse
import os
import time
from typing import NamedTuple

import _sim
from common import cli, git

#: What a call may take: a build and every tier in ALL.
TIMEOUT_S = 1800

#: The test project. The game assembly comes with it as a project reference.
TESTS = "src/tests/shipstick-tests.csproj"


class Take(NamedTuple):
    """One `dotnet test` run: a configuration, and the part of a tier whose answer is true in it."""

    #: The build configuration this take is run in.
    config: str
    #: What narrows the tier's trait to the tests this take is for, or nothing for all of them.
    narrow: str = ""
    #: Why this take is on its own, printed beside it so a split tier says what split it.
    why: str = ""


class Suite(NamedTuple):
    """A tier: the trait it is selected by, what it is for, and the runs it takes to answer it."""

    trait: str
    what: str
    takes: tuple[Take, ...]


#: Each tier and the runs it takes, cheapest first, so a broken build or unit test is reported before anything dearer.
#: Release unless a take needs Debug: it asserts the same things, faster.
TIERS = {
    "unit": Suite("Unit", "engine-free arithmetic over the game's own types", (Take("Release"),)),
}

#: What `all` means: everything that costs no money and needs nobody to look at a picture.
ALL = ["unit"]

#: What a change to a path can have moved, most reaching first — the first match wins. A path no row names is `unit`.
SELECT = [
    ("src/", ["unit"]),
]

#: The lowest rung on src/tests/Priority.cs, which is also `--upto`'s default: everything.
LAST_RUNG = 9

#: What `all` is allowed to cost, in seconds (docs/verification.md). Reported, never asserted.
BUDGET_S = 300

#: A working tree this far from HEAD is not an edit anybody is choosing a tier for.
SPRAWL = 60

#: One take's filter matched no test. Neither a pass nor a failure until every take has been asked.
MISSED = -1


def main():
    a = parse_args()
    base = _sim.root()
    chosen = pick(a.tiers + (from_the_tree(base) if a.changed else []))
    _sim.lighten(a.full)
    log = []
    began = time.monotonic()

    status = suite(base, chosen, log, name=a.name, upto=a.upto)

    _sim.write_log(base, "tests", "\n".join(log))
    print(budget(chosen, time.monotonic() - began))
    print(f"=== status {status}")
    return status


def suite(base, chosen: list[str], log: list[str], name=None, upto=LAST_RUNG) -> int:
    """
    Build what the chosen tiers need and take each of them. Separate from `main` because `qq checks` runs the same
    tiers, and a second way of running them is a second answer to what "the suite" means.
    """
    status = 0
    matched: dict[str, bool] = {}

    for config in ordered_configs(chosen):
        print(f"=== build ({config})")
        built = _sim.dotnet(base, "build", TESTS, "-c", config, *_sim.light_build())
        log.append(f"=== build ({config})\n" + built.stdout + built.stderr)
        if built.code != 0:
            _sim.show(built.stdout, r"error")
            return 1

        for tier in chosen:
            for take in [t for t in TIERS[tier].takes if t.config == config]:
                outcome = run(base, tier, take, name, upto, log)
                matched.setdefault(tier, False)
                matched[tier] = matched[tier] or outcome != MISSED
                status = (0 if outcome == MISSED else outcome) or status

    # One take missing a name is ordinary (a class lives in one tier); every take missing it names nothing.
    if matched and not any(matched.values()):
        print(f"=== no test in {', '.join(matched)} is named `{name}` — nothing ran")
        status = 1

    return status


def budget(chosen: list[str], tookS: float) -> str:
    """What the run cost against what `all` is allowed — a reading and not a gate."""
    spent = f"{int(tookS // 60)}m {tookS % 60:04.1f}s" if tookS >= 60 else f"{tookS:.1f}s"
    if _sim.light_cores():
        spent += f" (light: {_sim.light_cores()} of {os.cpu_count()} cores)"
    if not set(chosen) <= set(ALL):
        return f"=== took {spent}"

    left = BUDGET_S - tookS
    if left >= 0:
        return f"=== took {spent} of the suite's {BUDGET_S // 60:.0f}-minute budget, {left / 60:.1f} min spare"
    return (f"=== took {spent}, which is {-left:.0f}s OVER the suite's {BUDGET_S // 60:.0f}-minute budget — "
            "something is dropped or made cheaper, from the bottom of src/tests/Priority.cs")


def from_the_tree(base) -> list[str]:
    """The tiers the working tree's own changes can have moved, and the reason printed with them."""
    changed = [change.path for change in git.porcelain(git.status(base, "--untracked-files=all"))]
    if not changed:
        print("=== changed: nothing since HEAD — unit only")
        return []
    if len(changed) > SPRAWL:
        print(f"=== changed: {len(changed)} files, which is a tree and not an edit — running all")
        return ALL

    wanted, why = [], {}
    for path in changed:
        prefix, tiers = next(((prefix, tiers) for prefix, tiers in SELECT if path.startswith(prefix)), ("", ["unit"]))
        why[prefix or "elsewhere"] = why.get(prefix or "elsewhere", 0) + 1
        wanted.extend(tiers)
    where = ", ".join(f"{prefix} ({count})" for prefix, count in sorted(why.items(), key=lambda pair: -pair[1]))
    print(f"=== changed: {len(changed)} files — {where}")
    return wanted


def run(base, tier, take, name, upto, log):
    """One take of one tier, against the build already made for its configuration."""
    suite = TIERS[tier]
    cut = f", P0–P{upto}" if upto < LAST_RUNG else ""
    print(f"=== {tier} ({take.config}{cut}) — {take.why or suite.what}")

    # The run settings go last: everything after their `--` is one.
    argv = ["test", TESTS, "-c", take.config, "--no-build",
            "--filter", filter_for(suite.trait, take.narrow, name, upto), *_sim.light_test()]
    tested = _sim.dotnet(base, *argv)
    log.append(f"=== {tier} ({take.config})\n" + tested.stdout + tested.stderr)
    _sim.show(tested.stdout, r"error CS|^\s+(Failed|Error Message)|Failed!|Passed!|No test matches|Test Run Aborted")
    # `dotnet test` exits 0 when the filter matched nothing, which must never read as green.
    if "No test matches" in tested.stdout:
        return MISSED if name else 1
    return 0 if tested.code == 0 else 1


def filter_for(trait: str, narrow: str, name: str | None, upto: int) -> str:
    """
    The tier, cut down to the take, cut again at a rung when `--upto` was given, and narrowed by substring when
    `--name` was. The name is matched against the display name too, so one `[Theory]` case can be picked. The rung is
    spelled out, not compared: the filter has no ordering, so `P0–P3` is four alternatives.
    """
    named = f"(FullyQualifiedName~{name}|DisplayName~{name})" if name else ""
    rungs = "|".join(f"P=P{rung}" for rung in range(upto + 1)) if upto < LAST_RUNG else ""
    return "&".join(part for part in (f"Tier={trait}", narrow, f"({rungs})" if rungs else "", named) if part)


def pick(tiers: list[str]) -> list[str]:
    """The tiers to run, de-duplicated and back in cheapest-first order."""
    wanted = set()
    for tier in tiers or ["unit"]:
        wanted.update(ALL if tier == "all" else [tier])
    return [tier for tier in TIERS if tier in wanted]


def ordered_configs(chosen: list[str]) -> list[str]:
    """The configurations the chosen tiers need, each built once, cheapest tier's first."""
    configs = []
    for tier in chosen:
        for take in TIERS[tier].takes:
            if take.config not in configs:
                configs.append(take.config)
    return configs


def name_part(value: str) -> str:
    """An argparse `type` for `--name`: a word of a test's name, so it cannot widen the filter it is put into."""
    if not value.replace("_", "").replace(".", "").isalnum():
        raise argparse.ArgumentTypeError(f"{value!r} is not part of a test's name")
    return value


def parse_args():
    parser = argparse.ArgumentParser(
        prog="qq tests",
        description="Run one or more tiers of the test suite.",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("tiers", nargs="*", default=["unit"], choices=[*TIERS, "all"],
                        help="which tiers to run (src/tests/Tier.cs); 'all' is " + ", ".join(ALL))
    parser.add_argument("--changed", action="store_true",
                        help="add the tiers the working tree's own changes can have moved")
    parser.add_argument("--upto", type=int, default=LAST_RUNG, choices=range(LAST_RUNG + 1), metavar="RUNG",
                        help="run only P0 through this rung (src/tests/Priority.cs)")
    parser.add_argument("--name", type=name_part, default=None,
                        help="narrow a tier to the tests whose name contains this — a class, a method, "
                             "or one case of a [Theory] by its argument")
    parser.add_argument("--full", action="store_true",
                        help="take every core at normal priority, rather than the light run's half at a low one")
    return parser.parse_args()


if __name__ == "__main__":
    cli.entry(main)
