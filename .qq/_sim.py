"""
Shared bones of this project's build-time tools. Private: the leading `_` keeps it out of the `qq --help` registry.

Finding the project, building and running it through the SDK, lightening a run, keeping the last ten full logs of a
kind, and cutting a long build log down to the few lines worth reading. One copy, so the tools cannot drift apart.

`proc.run` captures a child instead of `tee`-ing it, so a long run prints nothing until it ends — `stream` is the one
that prints as it goes. The full log is still written, and it is the thing to read when the summary is not enough.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import time
from pathlib import Path

from common import paths, proc
from common.cli import fail

#: The project root, taken from this file rather than from the working directory, so a caller standing in another
#: checkout cannot point the tools at it. Not resolved: a git worktree reaching these tools through a link is its own root.
ROOT = Path(__file__).absolute().parent.parent

#: What tells this project apart from any other checkout, and what a whole build is given.
MARKER = "shipstick.slnx"

#: The game, engine-free; the host that runs it and serves the client (whose JS and CSS have no project).
GAME = "src/shipstick.csproj"
HOST = "src/app/host/shipstick.host.csproj"

#: A user-local SDK install: where an SDK newer than the system's package is put (`dotnet-install.sh`).
USER_DOTNET = Path.home() / ".dotnet"


def use_pinned_sdk():
    """
    `global.json` names the SDK; where only the user-local install has it, that install is put first on PATH and made
    the runtime's root, so `dotnet` and every child of it find it. Nothing changes where the pinned SDK is not there
    either — the build's own message then says which one is wanted.
    """
    try:
        pinned = json.loads((ROOT / "global.json").read_text(encoding="utf-8"))["sdk"]["version"]
    except (OSError, ValueError, KeyError):
        return
    if not (USER_DOTNET / "sdk" / pinned).is_dir():
        return
    os.environ["PATH"] = f"{USER_DOTNET}{os.pathsep}{os.environ.get('PATH', '')}"
    os.environ["DOTNET_ROOT"] = str(USER_DOTNET)


use_pinned_sdk()


def root() -> Path:
    """The project root, refusing a directory that is not this project."""
    if not (ROOT / MARKER).is_file():
        fail(f"not the shipstick project: no {MARKER} in {paths.display(ROOT)}")
    return ROOT


def rel(base: Path, path: Path) -> str:
    """A path as this project prints one: relative to the root."""
    return str(path.relative_to(base)).replace("\\", "/")


def dotnet(base: Path, *argv: str) -> proc.Result:
    """
    The SDK, in the project. `check=False` on purpose: a failed build and a failing test are both answers the caller
    handles itself, and neither is a reason to raise past the summary it was about to print.
    """
    return proc.run([*memory_cap(), "dotnet", *argv], cwd=base, check=False)


def memory_cap() -> list[str]:
    """
    What holds a light run's SDK, and every child it starts, to a share of the machine's memory, past which the kernel
    kills the run and not the desktop around it — or nothing for a full run. Set by `lighten` (`QQ_MEMORY_MAX`).
    """
    most = os.environ.get("QQ_MEMORY_MAX")
    if not most:
        return []
    return ["systemd-run", "--user", "--scope", "--quiet", "-p", f"MemoryMax={most}", "-p", "MemorySwapMax=0", "--"]


#: A light run's share of the cores (one in this many) and its niceness: the default, so a run leaves the machine usable.
LIGHT_SHARE = 2
LIGHT_NICE = 10

#: The most memory a light run may take before the kernel kills it rather than the desktop.
LIGHT_MEMORY = "14G"

#: How many cores a light run takes, or None for a full one; set once by `lighten`.
_light_cores: int | None = None


def lighten(full: bool) -> None:
    """
    A light run, unless `full`: this process and every child at a low priority, the build and xUnit held to a share of
    the cores. Children inherit both through the environment and the niceness, so every tool that builds or runs the
    game calls this once before it.
    """
    global _light_cores
    if full:
        return
    _light_cores = max(1, (os.cpu_count() or LIGHT_SHARE) // LIGHT_SHARE)
    os.setpriority(os.PRIO_PROCESS, 0, LIGHT_NICE)
    os.environ["DOTNET_PROCESSOR_COUNT"] = str(_light_cores)
    os.environ.setdefault("QQ_MEMORY_MAX", LIGHT_MEMORY)


def light_cores() -> int | None:
    """The cores a light run takes, or None for a full one."""
    return _light_cores


def light_build() -> list[str]:
    """What holds a build to the light share of the cores, or nothing for a full run."""
    return [f"-maxcpucount:{_light_cores}"] if _light_cores else []


def light_test() -> list[str]:
    """What holds xUnit's parallel classes to the light share, as a run setting after `--`, or nothing."""
    return ["--", f"xUnit.MaxParallelThreads={_light_cores}"] if _light_cores else []


def stream(base: Path, *argv: str) -> proc.Result:
    """
    The SDK, in the project, its output printed line by line as it comes and handed back whole: for a run somebody is
    watching while it goes. stderr is folded into stdout, in the order the two were written.
    """
    child = subprocess.Popen([*memory_cap(), "dotnet", *argv], cwd=base, stdin=subprocess.DEVNULL,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8",
                             errors="replace")
    lines = []
    for line in child.stdout:
        print(line, end="", flush=True)
        lines.append(line)
    return proc.Result(child.wait(), "".join(lines), "")


#: How many full logs of one kind are kept under .tmp/logs/.
KEEP_LOGS = 10


def write_log(base: Path, kind: str, text: str) -> Path:
    """
    Keep the whole of a run's output, not the grep of it: a failure usually explains itself in the lines the summary
    drops. The last `KEEP_LOGS` of each kind are kept; the rest go.
    """
    logs = base / ".tmp" / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    for stale in sorted(logs.glob(f"{kind}-*.log"), key=lambda f: f.stat().st_mtime, reverse=True)[KEEP_LOGS - 1 :]:
        stale.unlink()
    path = logs / f"{kind}-{time.strftime('%Y%m%d-%H%M%S')}.log"
    path.write_text(text, encoding="utf-8", errors="replace")
    print(f"=== full output {rel(base, path)} ({path.stat().st_size // 1024} KiB)")
    return path


def show(text: str, pattern: str, limit: int = 0) -> list[str]:
    """The lines of a run worth reading, printed and returned. `limit` 0 prints all of them."""
    hits = [line for line in text.splitlines() if re.search(pattern, line)]
    for line in hits[: limit or None]:
        print(line)
    return hits
