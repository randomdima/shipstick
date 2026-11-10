"""
Build the game's host, run it, and take a picture of its client's page running.

The page is the only renderer, so the only way to look at the game without a person sitting there is to drive a
browser. This builds the host (which copies the client it serves), runs it on localhost, opens a headless Chromium at it,
waits, optionally clicks, presses or drags, and photographs the page over the DevTools protocol. What the page says on
its console is printed as it is said, with the second it was said in.

**Serving is the host's, never this tool's** (HST-1, HST-2): the host is the game's own .NET head, and this only starts
and stops it.

    qq web                                  build the host, and say how to run it
    qq web --serve                          build and run the host until interrupted
    qq web --shot .tmp/web/page.png         build, run the host, photograph after --seconds, stop it all
    qq web --shot F --click 640,400         clicking there first, in CSS pixels of the page; repeat for more
                                            clicks, made in order (open two windows, then drag between them)
    qq web --shot F --query '?admin'        the page at that query: which view it opens
    qq web --shot F --key KeyE             pressing that key first, by its KeyboardEvent.code
    qq web --shot F --drag 100,100:400,300  a mouse drag from A to B (a finger with --device): an item moved
                                            between grids, or the floor panned
    qq web --shot F --device 390,844        as a handset sees it: a phone's points at a phone's pixel ratio
    qq web --shot F --device 390,844 --finger 150,400:150,300 --finger 250,400:250,500
                                            fingers put down in turn and moved together: a twist, a pinch
    qq web --shot F --line 150              every request and socket 150 ms slower a round trip
    qq web --shot F --release               the published host rather than the Debug build
    qq web --shot F --frames --drag A:B --drag-steps 120
                                            a two-second drag, its frames timed: the gaps between them, those the
                                            display missed, and Chrome's style, layout and script time over it
    qq web --shot F --frames --after 5 --software
                                            the page's frames over 5 s untouched, drawn in software: the
                                            weakest GPU a player may have
    qq web --shot F --frames --after 5 --cpu 6
                                            the same with the page's thread six times slower: a weak machine
    qq web --shot F --profile --after 5     the page's busiest functions over 5 s untouched, by their own time
    qq web --shot F --load                  what the page loaded, by kind, and holds: its JS heap, its elements, and
                                            what WebGL was asked to keep on the GPU, texture by texture
    qq web --shot F --load --profile        the same, and its busiest functions while loading
    qq web --shot F --heap                  what the JS heap holds once loaded, by the function that allocated it
    qq web --shot F --warm --eval JS       the page loaded twice, its cache kept: what a returning player asks for
    qq web --shot F --page .tmp/shapes/viewer.html
                                            a page of the project opened from disk, not the game's: no build, no
                                            host; the gestures and --query work the same, and the page may fetch
                                            and import its neighbours (the demo's site, DEM-1)
    qq web --shot F --mutations 3         count the page's DOM changes over 3 s first, by where: a page drawing
                                            only what changed (WEB-10) adds and removes no node between frames

**Debug by default**: a build is seconds, which is what an edit loop wants; `--release` publishes the host as it ships.
Each shot runs a host of its own, so it starts on a new starter ship.

**A running host serves the client's files as the last build copied them**, and runs the C# it started with: after a
change to C#, start it again.

**The browser runs headless** (Chromium's new headless mode, on the GPU through ANGLE over Vulkan), so no window opens
on anybody's desktop; `--headed` opens a real one for a person to watch. It wants a Chromium of its own on PATH
(`sudo dnf install -y chromium`): a Chromium already running ignores the debugging port a second invocation asks for.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import shutil
import socket
import struct
import subprocess
import threading
import time
import urllib.request
from pathlib import Path

import _sim
from common import cli, paths

#: What a call may take: a publish, a browser, and `--seconds` of the page running in front of it.
TIMEOUT_S = 900

#: Where a build and a publish lay the host, and what it is run as.
DEBUG_HOST = "bin/shipstick.host/Debug/net11.0"
RELEASE_HOST = "bin/shipstick.host/Release/net11.0/publish"
HOST_DLL = "shipstick-host.dll"

#: What the host says once it takes requests.
LISTENING = "Now listening on:"

#: How long a stopped host is given to finish before it is killed.
STOP_S = 10.0

#: Browsers that speak the DevTools protocol, most likely first, looked for on PATH.
BROWSERS = ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable")
INSTALL = "sudo dnf install -y chromium"

#: What a driven browser is told so it opens a page instead of asking somebody to agree to something.
FLAGS = ("--test-type", "--no-first-run", "--no-default-browser-check", "--disable-fre",
         "--disable-search-engine-choice-screen")

#: Headless on the GPU: left alone, headless Chromium draws WebGL in software at a few frames a second.
HEADLESS = ("--headless=new", "--use-angle=vulkan", "--enable-features=Vulkan")

#: Headless in software (SwiftShader, on the CPU): the weakest GPU a player may have, for timing what the page draws.
SOFTWARE = ("--headless=new", "--use-angle=swiftshader", "--enable-unsafe-swiftshader")

#: A page opened from disk may fetch and import its neighbours there, as a static site does from its server: a page's
#: modules and JSON otherwise fail as cross-origin from a file.
FROM_DISK = ("--allow-file-access-from-files",)

#: A real window under XWayland, where Chromium paces its own frames even when covered.
HEADED = ("--ozone-platform=x11",)

#: How many moves a drag is drawn in, a frame apart, so the page reads a stroke and not one jump.
DRAG_STEPS = 16

#: What a handset reports when `--device` names no ratio.
HANDSET_RATIO = 3.0

#: When the page was told to navigate, so every console line carries how far into the load it was said.
navigated = 0.0


def main():
    a = parse_args()
    base = _sim.root()
    if a.finger and not a.device:
        cli.fail("--finger wants --device: a page without one is not touched")
    if a.page:
        if not a.shot:
            cli.fail("--page wants --shot")
        return shoot(base, None, a)
    if not a.no_build and not build(base, a.release):
        return 1

    folder = base / (RELEASE_HOST if a.release else DEBUG_HOST)
    if not (folder / HOST_DLL).is_file():
        cli.fail(f"no host at {_sim.rel(base, folder)}: run without --no-build")

    if a.shot:
        return shoot(base, folder, a)
    if a.serve:
        return serve_until_interrupted(base, folder, a.port)

    print(f"the host is at {_sim.rel(base, folder)}; run it with `dotnet {_sim.rel(base, folder / HOST_DLL)}` "
          f"or `qq web --serve`, then open http://localhost:{a.port}/")
    return 0


def build(base: Path, release: bool) -> bool:
    """The host and the page it serves: built in Debug (seconds), or published in Release."""
    step, config = ("publish", "Release") if release else ("build", "Debug")
    print(f"=== {step} ({config})")
    result = _sim.dotnet(base, step, _sim.HOST, "-c", config, "-v", "q", "--nologo")
    if result.code != 0:
        _sim.show(result.stdout + result.stderr, r"error", limit=12)
        _sim.write_log(base, "web", result.stdout + result.stderr)
        return False
    return True


def start_host(folder: Path, port: int) -> subprocess.Popen:
    """The host on this port, handed back once it takes requests; its output is the caller's to read or drain."""
    host = subprocess.Popen(["dotnet", HOST_DLL, "--urls", f"http://localhost:{port}"], cwd=folder,
                            stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                            encoding="utf-8", errors="replace")
    said = []
    for line in host.stdout:
        said.append(line)
        if LISTENING in line:
            return host
    print("".join(said[-12:]), end="")
    cli.fail(f"the host stopped before it listened on {port} (exit {host.wait()})")


def stop_host(host: subprocess.Popen):
    """Asked to stop, as ctrl-c does, then killed if it has not."""
    host.terminate()
    try:
        host.wait(STOP_S)
    except subprocess.TimeoutExpired:
        host.kill()


def serve_until_interrupted(base: Path, folder: Path, port: int) -> int:
    host = start_host(folder, port)
    # Flushed: this line is how anything else knows the page is up, and a pipe is block-buffered.
    print(f"serving {_sim.rel(base, folder)} at http://localhost:{port}/ — ctrl-c to stop", flush=True)
    try:
        for line in host.stdout:
            print(line, end="", flush=True)
        return host.wait()
    except KeyboardInterrupt:
        return 0
    finally:
        stop_host(host)


def shoot(base: Path, folder: Path | None, a) -> int:
    """
    Run the host, open a browser at the page, wait in real seconds, act, photograph, and put it all away. With no
    host `folder`, the page is `--page`, a file of the project opened from disk.
    """
    command = next((found for name in BROWSERS if (found := shutil.which(name))), None)
    if command is None:
        cli.fail(f"no browser found: looked for {', '.join(BROWSERS)} on PATH. Install one with `{INSTALL}`")

    out = paths.resolve_in_root(base / a.shot, base)
    out.parent.mkdir(parents=True, exist_ok=True)
    if folder is None:
        page = paths.resolve_in_root(base / a.page, base)
        if not page.is_file():
            cli.fail(f"no page at {_sim.rel(base, page)}")
        host, url = None, page.as_uri() + (a.query or "")
    else:
        host, url = start_host(folder, a.port), f"http://localhost:{a.port}/{a.query or ''}"
        # Drained, or the host blocks once its pipe fills.
        threading.Thread(target=host.stdout.read, daemon=True).start()

    # Kept between runs: a fresh profile is a browser that has agreed to nothing and shows its welcome every time.
    profile = base / ".tmp" / "web-profile"
    profile.mkdir(parents=True, exist_ok=True)
    browser = subprocess.Popen(
        [command, *FLAGS, *(HEADED if a.headed else SOFTWARE if a.software else HEADLESS),
         *(FROM_DISK if folder is None else ()),
         f"--user-data-dir={profile}",
         f"--remote-debugging-port={a.debug_port}", f"--window-size={a.width},{a.height}", "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        capture(wait_for_page(a.debug_port), url, out, a)
        print(f"{_sim.rel(base, out)} written after {a.seconds:g} s")
        return 0
    finally:
        shut_down(a.debug_port, browser)
        if host:
            stop_host(host)


def capture(page: dict, url: str, out: Path, a):
    """Navigate, let the page run for real seconds, act, then photograph it."""
    global navigated
    sock = connect(page["webSocketDebuggerUrl"])
    ask(sock, "Runtime.enable")
    # What the browser says itself: a file that would not load is said here, not on the page's console.
    ask(sock, "Log.enable")
    # As a first visit: the profile is kept between runs, and with it whatever an older host let it cache. A warm one
    # is the page loaded once with the cache off, then again with it on: a returning player's.
    ask(sock, "Network.enable")
    ask(sock, "Network.setCacheDisabled", {"cacheDisabled": True})
    if a.warm:
        ask(sock, "Network.setCacheDisabled", {"cacheDisabled": False})
        ask(sock, "Network.clearBrowserCache")
        ask(sock, "Page.navigate", {"url": url})
        ask(sock, "Page.bringToFront")
        settle(sock, a.seconds)
        print(f"   loaded once, cache kept, for {a.seconds:g} s")

    # Before the navigate: a page reads its viewport and pixel ratio at start-up.
    if a.device:
        pretend(sock, a.device)
    if a.cpu > 1:
        ask(sock, "Emulation.setCPUThrottlingRate", {"rate": a.cpu})
        print(f"   the page's thread slowed {a.cpu:g} times")
    if a.line:
        ask(sock, "Network.emulateNetworkConditions",
            {"offline": False, "latency": a.line, "downloadThroughput": -1, "uploadThroughput": -1})
        print(f"   the page's line slowed by {a.line:g} ms a round trip")

    if a.load:
        ask(sock, "Performance.enable")
        ask(sock, "Page.enable")
        ask(sock, "Page.addScriptToEvaluateOnNewDocument", {"source": GPU_COUNT_JS})
        if a.profile:
            start_profile(sock)
    if a.heap:
        ask(sock, "HeapProfiler.enable")
        ask(sock, "HeapProfiler.startSampling", {"samplingInterval": HEAP_INTERVAL_BYTES})
    navigated = time.time()
    ask(sock, "Page.navigate", {"url": url})
    # A window that is not in front is not painted, and a page that is not painted runs no frame.
    ask(sock, "Page.bringToFront")
    settle(sock, a.seconds)
    if a.load:
        report_weight(sock)
        if a.profile:
            report_profile(sock)
    if a.heap:
        report_heap(sock)

    if a.frames:
        start_frames(sock)
    if a.profile and not a.load:
        start_profile(sock)
    for point in a.click:
        press(sock, point)
    if a.key:
        type_key(sock, a.key)
    if a.drag:
        drag(sock, a.drag, finger=bool(a.device), steps=a.drag_steps, held=a.hold, button=a.button)
    if a.finger:
        fingers(sock, a.finger, a.drag_steps)
    for spec in a.wheel:
        wheel(sock, spec)
    if a.after and (a.click or a.key or a.drag or a.finger or a.wheel or a.frames or a.profile):
        settle(sock, a.after)
    if a.frames:
        report_frames(sock)
    if a.profile and not a.load:
        report_profile(sock)
    if a.mutations:
        count_mutations(sock, a.mutations)
    for expression in a.eval:
        answer = ask(sock, "Runtime.evaluate", {"expression": expression, "returnByValue": True, "awaitPromise": True})
        result = answer.get("result", {})
        value = result.get("exceptionDetails", {}).get("text") or json.dumps(result.get("result", {}).get("value"))
        print(f"   {expression}  →  {value}")

    sock.settimeout(120.0)
    shot = ask(sock, "Page.captureScreenshot")
    if "result" not in shot:
        raise SystemExit(f"the browser refused the screenshot: {json.dumps(shot.get('error', shot))}")
    out.write_bytes(base64.b64decode(shot["result"]["data"]))


def fingers(sock: socket.socket, paths: list[str], steps: int):
    """
    Fingers put down one after another, as a hand does, then moved together each from its first point to its second,
    `steps` times a frame apart, and lifted: two make a pinch, a twist or a two-finger drag.
    """
    ends = [tuple(at(p) for p in path.split(":")) for path in paths]

    def points(along: float) -> list[dict]:
        return [{"id": i, "x": a["x"] + (b["x"] - a["x"]) * along, "y": a["y"] + (b["y"] - a["y"]) * along}
                for i, (a, b) in enumerate(ends)]

    for count in range(1, len(ends) + 1):
        ask(sock, "Input.dispatchTouchEvent", {"type": "touchStart", "touchPoints": points(0)[:count]})
    for step in range(1, steps + 1):
        ask(sock, "Input.dispatchTouchEvent", {"type": "touchMove", "touchPoints": points(step / steps)})
        time.sleep(1.0 / 60.0)
    ask(sock, "Input.dispatchTouchEvent", {"type": "touchEnd", "touchPoints": []})
    print(f"   {len(ends)} fingers moved: {', '.join(paths)}")
    settle(sock, 1.0)


def press(sock: socket.socket, point: str):
    """A left click at a point of the page, in CSS pixels: moved there first, so the pointer has entered the page."""
    where = at(point)
    for event in ({"type": "mouseMoved", "button": "none", "buttons": 0},
                  {"type": "mousePressed", "button": "left", "buttons": 1, "clickCount": 1},
                  {"type": "mouseReleased", "button": "left", "buttons": 0, "clickCount": 1}):
        ask(sock, "Input.dispatchMouseEvent", {**where, **event})
    print(f"   clicked {where['x']:.0f},{where['y']:.0f}")
    settle(sock, 1.0)


def type_key(sock: socket.socket, code: str):
    """One key pressed and let go, named by its `KeyboardEvent.code` (`KeyE`, `Escape`, `Digit1`)."""
    letter = code[3:] if code.startswith("Key") and len(code) == 4 else None
    named = {"code": code, "key": letter.lower() if letter else code}
    if letter:
        named["windowsVirtualKeyCode"] = ord(letter)
    for kind in ("keyDown", "keyUp"):
        ask(sock, "Input.dispatchKeyEvent", {"type": kind, **named})
    print(f"   pressed {code}")
    settle(sock, 1.0)


#: CDP's modifier bits, for a drag made with a key held (`--hold`).
MODIFIERS = {"alt": 1, "ctrl": 2, "meta": 4, "shift": 8}


#: CDP's `buttons` bit for each mouse button a drag can be made with.
BUTTONS = {"left": 1, "right": 2, "middle": 4}


def wheel(sock: socket.socket, spec: str):
    """The mouse wheel turned at a point: `X,Y,DY` in CSS pixels, DY above 0 toward the user (zooming out)."""
    x, y, dy = (float(v) for v in spec.split(","))
    ask(sock, "Input.dispatchMouseEvent", {"type": "mouseWheel", "x": x, "y": y, "deltaX": 0, "deltaY": dy})
    print(f"   wheeled {dy:+g} px at {x:.0f},{y:.0f}")


def drag(sock: socket.socket, path: str, finger: bool, steps: int, held: str | None = None, button: str = "left"):
    """
    A mouse button — or, as a handset, a finger — held from one point to another, in CSS pixels, moved `steps` times
    a frame apart, and let go; with `held` (ctrl, shift, alt, meta) down throughout.
    """
    start, _, end = path.partition(":")
    begin, finish = at(start), at(end)
    modifiers = MODIFIERS[held] if held else 0

    def hold(phase: str, point: dict):
        if finger:
            kind = {"down": "touchStart", "move": "touchMove", "up": "touchEnd"}[phase]
            ask(sock, "Input.dispatchTouchEvent", {"type": kind, "touchPoints": [] if phase == "up" else [point],
                                                   "modifiers": modifiers})
            return
        kind = {"down": "mousePressed", "move": "mouseMoved", "up": "mouseReleased"}[phase]
        ask(sock, "Input.dispatchMouseEvent", {**point, "type": kind, "button": button,
                                               "buttons": 0 if phase == "up" else BUTTONS[button],
                                               "clickCount": 1, "modifiers": modifiers})

    if not finger:
        ask(sock, "Input.dispatchMouseEvent", {**begin, "type": "mouseMoved", "button": "none", "buttons": 0})
    started = time.time()
    hold("down", begin)
    for step in range(1, steps + 1):
        along = step / steps
        hold("move", {"x": begin["x"] + (finish["x"] - begin["x"]) * along,
                      "y": begin["y"] + (finish["y"] - begin["y"]) * along})
        time.sleep(1.0 / 60.0)
    hold("up", finish)
    print(f"   {'swiped' if finger else 'dragged'} {begin['x']:.0f},{begin['y']:.0f} to {finish['x']:.0f},{finish['y']:.0f} "
          f"in {steps} moves, {time.time() - started:.2f} s (a frame a move is {steps / 60:.2f} s)")
    settle(sock, 1.0)


#: Counts every DOM change for `MS` milliseconds, by the nearest ancestor with an id: nodes added and removed,
#: attributes and text changed. A page that rebuilds a part (WEB-10) shows as added and removed nodes every tick.
MUTATIONS_JS = """new Promise(done => {
  const by = {};
  const where = node => {
    for (let el = node.nodeType === 1 ? node : node.parentElement; el; el = el.parentElement) if (el.id) return '#' + el.id;
    return 'document';
  };
  const watch = new MutationObserver(list => {
    for (const m of list) {
      const c = by[where(m.target)] ??= { added: 0, removed: 0, attributes: 0, text: 0, names: {} };
      if (m.type === 'childList') { c.added += m.addedNodes.length; c.removed += m.removedNodes.length; }
      else if (m.type === 'attributes') {
        c.attributes++;
        const name = `${m.target.className || m.target.tagName.toLowerCase()} ${m.attributeName}`;
        c.names[name] = (c.names[name] ?? 0) + 1;
      } else c.text++;
    }
  });
  watch.observe(document.documentElement, { subtree: true, childList: true, attributes: true, characterData: true });
  setTimeout(() => { watch.disconnect(); done(by); }, MS);
})"""


#: Records the gap before every frame the page draws, until `__framesStop` is set.
FRAMES_JS = """(() => {
  window.__frames = []; window.__framesStop = false;
  let last = performance.now();
  const tick = t => { __frames.push(t - last); last = t; if (!__framesStop) requestAnimationFrame(tick); };
  requestAnimationFrame(tick);
})()"""

#: What Chrome counts of the page's own work, read before and after the gestures.
METRICS = ("TaskDuration", "ScriptDuration", "RecalcStyleDuration", "RecalcStyleCount", "LayoutDuration", "LayoutCount")

#: A frame this much longer than the display's is one the display missed.
MISSED_FRAME_SHARE = 1.5

_metrics_before: dict = {}


def start_frames(sock: socket.socket):
    """Starts counting the page's frames and Chrome's work, for the gestures that follow."""
    global _metrics_before
    ask(sock, "Performance.enable")
    _metrics_before = metrics(sock)
    ask(sock, "Runtime.evaluate", {"expression": FRAMES_JS})


def metrics(sock: socket.socket) -> dict:
    answer = ask(sock, "Performance.getMetrics")
    return {m["name"]: m["value"] for m in answer.get("result", {}).get("metrics", []) if m["name"] in METRICS}


def report_frames(sock: socket.socket):
    """The frames drawn over the gestures — their gaps, and those the display missed — and what Chrome spent on them."""
    answer = ask(sock, "Runtime.evaluate", {"expression": "__framesStop = true, __frames.slice(1)", "returnByValue": True})
    gaps = sorted(answer.get("result", {}).get("result", {}).get("value") or [])
    after = metrics(sock)
    if gaps:
        display = gaps[len(gaps) // 10]
        missed = sum(1 for g in gaps if g > display * MISSED_FRAME_SHARE)
        pick = lambda share: gaps[min(len(gaps) - 1, int(len(gaps) * share))]
        print(f"   frames: {len(gaps)} over {sum(gaps) / 1000:.1f} s, display {display:.1f} ms; gap median "
              f"{pick(.5):.1f}, p95 {pick(.95):.1f}, max {gaps[-1]:.1f} ms; {missed} missed")
    else:
        print("   frames: none drawn")
    spent = {name: after.get(name, 0) - _metrics_before.get(name, 0) for name in METRICS}
    print(f"   work: task {spent['TaskDuration'] * 1000:.0f} ms, script {spent['ScriptDuration'] * 1000:.0f} ms, "
          f"style {spent['RecalcStyleDuration'] * 1000:.0f} ms ×{spent['RecalcStyleCount']:.0f}, "
          f"layout {spent['LayoutDuration'] * 1000:.0f} ms ×{spent['LayoutCount']:.0f}")


#: How often the profiler samples the page's thread, and how many of its busiest functions are named.
PROFILE_INTERVAL_US = 200
PROFILE_TOP = 15


def start_profile(sock: socket.socket):
    ask(sock, "Profiler.enable")
    ask(sock, "Profiler.setSamplingInterval", {"interval": PROFILE_INTERVAL_US})
    ask(sock, "Profiler.start")


#: What a page asked for, by kind (count, bytes over the line, bytes decoded), and what it holds once running.
WEIGHT_JS = """(() => {
  const kinds = {};
  for (const r of performance.getEntriesByType('resource')) {
    const kind = new URL(r.name).pathname.split('.').pop();
    const k = kinds[kind] ??= [0, 0, 0];
    k[0]++; k[1] += r.transferSize; k[2] += r.decodedBodySize;
  }
  const gpu = window.__gpu && { ...__gpu.sum(), canvas: [...document.querySelectorAll('canvas')]
    .reduce((bytes, c) => bytes + c.width * c.height * 4 * 2, 0) };
  return { kinds, heap: performance.memory.usedJSHeapSize, nodes: document.getElementsByTagName('*').length, gpu };
})()"""

#: Run in the page before its own scripts: counts what WebGL is asked to hold, texture by texture and buffer by
#: buffer, as their sizes and formats say — what the GPU holds for the page, less the driver's own padding.
GPU_COUNT_JS = """(() => {
  const P = WebGL2RenderingContext.prototype, held = new Map();
  const BYTES = { 0x8058: 4, 0x81A6: 4, 0x81A5: 2, 0x88F0: 4, 0x8CAC: 4, 0x881A: 8, 0x8814: 16, 0x8229: 1, 0x822B: 2,
    0x8236: 4, 0x822E: 4, 0x8D7C: 4, 0x1908: 4, 0x1907: 3 };
  const bound = { unit: 0, textures: new Map(), buffers: new Map() };
  const wrap = (name, after) => { const was = P[name]; P[name] = function (...a) { const r = was.apply(this, a); after.call(this, a, r); return r; }; };
  const size = (key, kind, bytes) => key && held.set(key, { kind, bytes });
  wrap('activeTexture', ([unit]) => bound.unit = unit);
  wrap('bindTexture', ([, t]) => bound.textures.set(bound.unit, t));
  wrap('bindBuffer', ([target, b]) => bound.buffers.set(target, b));
  wrap('texStorage2D', ([, levels, format, w, h]) => {
    let bytes = 0;
    for (let l = 0; l < levels; l++) bytes += Math.max(1, w >> l) * Math.max(1, h >> l) * (BYTES[format] ?? 4);
    size(bound.textures.get(bound.unit), 'texture', bytes);
  });
  wrap('texImage2D', (a) => {
    if (a[1] !== 0) return;
    const source = a.length === 6 ? a[5] : null;
    const [w, h] = source ? [source.width, source.height] : [a[3], a[4]];
    size(bound.textures.get(bound.unit), 'texture', w * h * (BYTES[a[2]] ?? 4));
  });
  wrap('generateMipmap', () => { const t = held.get(bound.textures.get(bound.unit)); if (t) t.bytes = Math.round(t.bytes * 4 / 3); });
  wrap('bufferData', ([target, data]) => size(bound.buffers.get(target), 'buffer', typeof data === 'number' ? data : data.byteLength));
  wrap('deleteTexture', ([t]) => held.delete(t));
  wrap('deleteBuffer', ([b]) => held.delete(b));
  window.__gpu = { held, sum() {
    const s = { textures: 0, texturesCount: 0, buffers: 0, buffersCount: 0, largest: [] };
    for (const { kind, bytes } of held.values()) { s[kind + 's'] += bytes; s[kind + 'sCount']++; }
    s.largest = [...held.values()].filter(h => h.kind === 'texture').map(h => h.bytes).sort((a, b) => b - a).slice(0, 6);
    return s;
  } };
})()"""


def report_weight(sock: socket.socket):
    """What the page loaded and holds after --seconds, and the work its thread did to get there."""
    weight = ask(sock, "Runtime.evaluate", {"expression": WEIGHT_JS, "returnByValue": True})
    weight = weight.get("result", {}).get("result", {}).get("value") or {}
    kinds = sorted(weight.get("kinds", {}).items(), key=lambda kind: -kind[1][2])
    over, held = sum(k[1] for _, k in kinds), sum(k[2] for _, k in kinds)
    print(f"   load: {over / 1e3:.0f} kB over the line, {held / 1e3:.0f} kB decoded; JS heap "
          f"{weight.get('heap', 0) / 1e6:.1f} MB; {weight.get('nodes', 0)} elements")
    for kind, (count, line, decoded) in kinds:
        print(f"     {kind:>6} ×{count:<4} {line / 1e3:8.0f} kB over the line {decoded / 1e3:8.0f} kB decoded")
    if gpu := weight.get("gpu"):
        print(f"   GPU: {(gpu['textures'] + gpu['buffers'] + gpu['canvas']) / 1e6:.1f} MB — textures "
              f"{gpu['textures'] / 1e6:.1f} MB ×{gpu['texturesCount']} (largest "
              f"{', '.join(f'{b / 1e6:.1f}' for b in gpu['largest'])}), buffers {gpu['buffers'] / 1e6:.1f} MB "
              f"×{gpu['buffersCount']}, canvases {gpu['canvas'] / 1e6:.1f} MB")
    spent = metrics(sock)
    print(f"   work: task {spent.get('TaskDuration', 0) * 1000:.0f} ms, script {spent.get('ScriptDuration', 0) * 1000:.0f} ms, "
          f"style {spent.get('RecalcStyleDuration', 0) * 1000:.0f} ms, layout {spent.get('LayoutDuration', 0) * 1000:.0f} ms")


def report_profile(sock: socket.socket):
    """The page's busiest functions over the gestures and --after, by the time spent in each itself."""
    sock.settimeout(60.0)
    profile = ask(sock, "Profiler.stop").get("result", {}).get("profile")
    if not profile:
        print("   profile: none taken")
        return
    nodes = {n["id"]: n["callFrame"] for n in profile["nodes"]}
    spent: dict = {}
    for node, delta_us in zip(profile["samples"], profile["timeDeltas"]):
        frame = nodes[node]
        where = f"{frame['functionName'] or '(anonymous)'} {Path(frame['url']).name or ''}:{frame['lineNumber'] + 1}"
        spent[where] = spent.get(where, 0) + delta_us
    total = sum(spent.values()) or 1
    print(f"   profile: {total / 1e6:.1f} s sampled; by self time:")
    for where, us in sorted(spent.items(), key=lambda item: -item[1])[:PROFILE_TOP]:
        print(f"     {us / 1000:8.1f} ms {us / total:6.1%}  {where}")


#: Bytes between the heap profiler's samples: fine enough that an object the page keeps is seen, coarse enough to run.
HEAP_INTERVAL_BYTES = 4096
HEAP_TOP = 15


def report_heap(sock: socket.socket):
    """What the page's JS heap holds after --seconds, after a collection: live bytes by the function that allocated
    them, its own and with what it called."""
    sock.settimeout(60.0)
    ask(sock, "HeapProfiler.collectGarbage")
    profile = ask(sock, "HeapProfiler.stopSampling").get("result", {}).get("profile")
    if not profile:
        print("   heap: none sampled")
        return
    own: dict = {}
    under: dict = {}

    def walk(node: dict, above: frozenset) -> int:
        frame = node["callFrame"]
        where = f"{frame['functionName'] or '(anonymous)'} {Path(frame['url']).name or ''}:{frame['lineNumber'] + 1}"
        bytes_ = node["selfSize"] + sum(walk(child, above | {where}) for child in node["children"])
        own[where] = own.get(where, 0) + node["selfSize"]
        if where not in above:
            under[where] = under.get(where, 0) + bytes_
        return bytes_

    total = walk(profile["head"], frozenset()) or 1
    print(f"   heap: {total / 1e6:.1f} MB live, sampled; by allocating function, own and with what it called:")
    for where, bytes_ in sorted(own.items(), key=lambda item: -item[1])[:HEAP_TOP]:
        print(f"     {bytes_ / 1e6:6.2f} MB own {under[where] / 1e6:6.2f} MB under  {where}")


#: How many of the attributes changed most a place's line names: element (its class) and attribute.
ATTRIBUTES_NAMED = 4


def count_mutations(sock: socket.socket, seconds: float):
    """What the page changes in its DOM over `seconds` of running, untouched, by where it changes."""
    sock.settimeout(seconds + 30.0)
    answer = ask(sock, "Runtime.evaluate", {"expression": MUTATIONS_JS.replace("MS", str(int(seconds * 1000))),
                                            "awaitPromise": True, "returnByValue": True})
    by = answer.get("result", {}).get("result", {}).get("value")
    if by is None:
        print(f"   mutations not counted: {json.dumps(answer.get('result', answer))[:200]}")
        return
    print(f"   DOM changes over {seconds:g} s:{'' if by else ' none'}")
    for where, c in sorted(by.items(), key=lambda kv: -(kv[1]["added"] + kv[1]["removed"] + kv[1]["attributes"] + kv[1]["text"])):
        names = ", ".join(f"{name} ×{n}" for name, n in sorted(c["names"].items(), key=lambda kv: -kv[1])[:ATTRIBUTES_NAMED])
        print(f"     {where:<12} +{c['added']} -{c['removed']} nodes, {c['attributes']} attributes, {c['text']} text"
              + (f" — {names}" if names else ""))


def pretend(sock: socket.socket, device: str):
    """A handset's viewport and pixel ratio, `W,H[,DPR]`, and a finger, so `pointer: coarse` matches."""
    said = device.split(",")
    width, height = int(said[0]), int(said[1])
    ratio = float(said[2]) if len(said) > 2 else HANDSET_RATIO
    ask(sock, "Emulation.setDeviceMetricsOverride",
        {"width": width, "height": height, "deviceScaleFactor": ratio, "mobile": True})
    ask(sock, "Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 2})
    print(f"   pretending to be {width}x{height} points at {ratio:g}x, with a finger")


def at(point: str) -> dict:
    x, _, y = point.partition(",")
    return {"x": float(x), "y": float(y)}


def settle(sock: socket.socket, seconds: float):
    """Let the page run, listening the whole time: what it says just after being touched is the most worth reading."""
    sock.settimeout(1.0)
    until = time.time() + seconds
    while time.time() < until:
        try:
            report(receive(sock))
        except (socket.timeout, TimeoutError):
            continue


def report(message: dict):
    """What the page says about itself, which is the whole of what a failed shot has to go on."""
    since = f"{time.time() - navigated:5.1f}s" if navigated else "     "
    method = message.get("method")
    if method == "Runtime.consoleAPICalled":
        said = " ".join(str(argument["value"]) for argument in message["params"].get("args", []) if "value" in argument)
        print(f"   {since} page: {said}", flush=True)
    elif method == "Runtime.exceptionThrown":
        detail = message["params"]["exceptionDetails"]
        print(f"   {since} page threw: {detail.get('text')} {detail.get('exception', {}).get('description', '')}",
              flush=True)
    elif method == "Log.entryAdded" and message["params"]["entry"]["level"] in ("error", "warning"):
        entry = message["params"]["entry"]
        print(f"   {since} browser {entry['level']}: {entry['text']} {entry.get('url', '')}", flush=True)
    elif method == "Inspector.targetCrashed":
        print(f"   {since} the page crashed", flush=True)


_asked = 0


def ask(sock: socket.socket, method: str, params: dict | None = None) -> dict:
    """One DevTools request and its answer, reporting whatever the page says on the way."""
    global _asked
    _asked += 1
    if sock.gettimeout() is None or sock.gettimeout() < 30.0:
        sock.settimeout(30.0)
    send(sock, {"id": _asked, "method": method, **({"params": params} if params else {})})
    while True:
        message = receive(sock)
        if message.get("id") == _asked:
            return message
        report(message)


def wait_for_page(port: int, seconds: float = 30.0) -> dict:
    until = time.time() + seconds
    while time.time() < until:
        try:
            listed = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list").read())
            page = next((p for p in listed if p["type"] == "page"), None)
            if page:
                return page
        except Exception:
            pass
        time.sleep(0.5)
    cli.fail(f"the browser never opened its debugging port {port}")


def shut_down(port: int, launcher: subprocess.Popen):
    """Close the browser over the protocol — killing what was launched leaves a sandboxed one standing — then the launcher."""
    try:
        listed = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{port}/json/version").read())
        sock = connect(listed["webSocketDebuggerUrl"])
        sock.settimeout(10.0)
        send(sock, {"id": 0, "method": "Browser.close"})
        try:
            receive(sock)
        except (socket.timeout, TimeoutError, EOFError):
            pass
        sock.close()
    except Exception as trouble:
        print(f"   the browser would not close over the protocol ({trouble}); killing what was launched")
    launcher.terminate()


def connect(url: str) -> socket.socket:
    """A WebSocket, by hand: a handshake and a masked frame header are not worth a dependency."""
    hostport, path = url.split("://", 1)[1].split("/", 1)
    host, port = hostport.split(":")
    sock = socket.create_connection((host, int(port)))
    key = base64.b64encode(os.urandom(16)).decode()
    sock.sendall((f"GET /{path} HTTP/1.1\r\nHost: {hostport}\r\nUpgrade: websocket\r\n"
                  f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n").encode())
    head = b""
    while b"\r\n\r\n" not in head:
        head += sock.recv(1)
    return sock


def send(sock: socket.socket, message: dict):
    payload = json.dumps(message).encode()
    header = bytearray([0x81])
    length = len(payload)
    if length < 126:
        header.append(0x80 | length)
    elif length < (1 << 16):
        header.append(0x80 | 126)
        header += struct.pack(">H", length)
    else:
        header.append(0x80 | 127)
        header += struct.pack(">Q", length)
    mask = os.urandom(4)
    header += mask
    sock.sendall(bytes(header) + bytes(b ^ mask[i % 4] for i, b in enumerate(payload)))


def receive(sock: socket.socket) -> dict:
    while True:
        first, second = exactly(sock, 2)
        length = second & 0x7F
        if length == 126:
            length = struct.unpack(">H", exactly(sock, 2))[0]
        elif length == 127:
            length = struct.unpack(">Q", exactly(sock, 8))[0]
        payload = exactly(sock, length)
        if first & 0x0F == 1:
            return json.loads(payload)


def exactly(sock: socket.socket, count: int) -> bytes:
    buffer = b""
    while len(buffer) < count:
        chunk = sock.recv(count - len(buffer))
        if not chunk:
            raise EOFError("the browser closed its debugging connection")
        buffer += chunk
    return buffer


def point_type(value: str) -> str:
    """An argparse `type` for `X,Y`."""
    x, _, y = value.partition(",")
    try:
        float(x), float(y)
    except ValueError:
        raise argparse.ArgumentTypeError(f"expected X,Y: got {value!r}")
    return value


def drag_type(value: str) -> str:
    """An argparse `type` for `X,Y:X,Y`."""
    start, _, end = value.partition(":")
    point_type(start), point_type(end)
    return value


def device_type(value: str) -> str:
    """An argparse `type` for `W,H[,DPR]`."""
    said = value.split(",")
    try:
        if len(said) not in (2, 3) or int(said[0]) <= 0 or int(said[1]) <= 0 or (len(said) == 3 and float(said[2]) <= 0):
            raise ValueError
    except ValueError:
        raise argparse.ArgumentTypeError(f"expected W,H or W,H,DPR: got {value!r}")
    return value


def key_type(value: str) -> str:
    """An argparse `type` for a `KeyboardEvent.code`: letters and digits only."""
    if not value.isalnum():
        raise argparse.ArgumentTypeError(f"expected a KeyboardEvent.code like KeyE: got {value!r}")
    return value


def query_type(value: str) -> str:
    if not value.startswith("?"):
        raise argparse.ArgumentTypeError(f"a query starts with '?', got '{value}'")
    return value


def seconds_type(value: str) -> float:
    seconds = float(value)
    if not 0 <= seconds <= 600:
        raise argparse.ArgumentTypeError(f"expected 0 to 600 seconds: got {value!r}")
    return seconds


def port_type(value: str) -> int:
    port = int(value)
    if not 1024 <= port <= 65535:
        raise argparse.ArgumentTypeError(f"expected a port from 1024 to 65535: got {value!r}")
    return port


def parse_args():
    parser = argparse.ArgumentParser(
        prog="qq web",
        description="Build the game's host and page, run the host, and take a picture of the page running.",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--shot", metavar="FILE", help="write a picture of the running page here (under the project)")
    parser.add_argument("--page", metavar="FILE",
                        help="photograph this page of the project, opened from disk, instead of the game's: no build, "
                             "no host (a tool's page under .tmp/)")
    parser.add_argument("--serve", action="store_true", help="run the host until interrupted")
    parser.add_argument("--release", action="store_true", help="publish in Release rather than build in Debug")
    parser.add_argument("--no-build", action="store_true", help="use the host already built or published")
    parser.add_argument("--query", type=query_type, default=None, metavar="?QUERY",
                        help="what follows the page's address, e.g. '?admin' or '?seat=2,1'")
    parser.add_argument("--seconds", type=seconds_type, default=5.0, help="how long the page runs before anything")
    parser.add_argument("--click", type=point_type, metavar="X,Y", action="append", default=[],
                        help="click here before the picture; repeat for several clicks, made in order")
    parser.add_argument("--key", type=key_type, metavar="CODE", help="press this key before the picture, after a click")
    parser.add_argument("--drag", type=drag_type, metavar="X,Y:X,Y", help="drag the mouse (a finger with --device) from A to B, after a key")
    parser.add_argument("--finger", type=drag_type, metavar="X,Y:X,Y", action="append", default=[],
                        help="with --device, a finger from A to B after the drag; repeat for each finger, all moved "
                             "together (two: a pinch, a twist, a two-finger drag)")
    parser.add_argument("--button", choices=sorted(BUTTONS), default="left", help="the mouse button a drag is made with")
    parser.add_argument("--wheel", metavar="X,Y,DY", action="append", default=[],
                        help="turn the mouse wheel at X,Y by DY pixels after the drag (below 0 away from the user); "
                             "repeat for several")
    parser.add_argument("--hold", choices=sorted(MODIFIERS), default=None,
                        help="hold this key down through the drag, e.g. ctrl to turn the floor's camera")
    parser.add_argument("--drag-steps", type=cli.counting, default=DRAG_STEPS, help="moves a drag is made in, a frame apart")
    parser.add_argument("--after", type=seconds_type, default=0.0, help="seconds the page runs after the gestures")
    parser.add_argument("--frames", action="store_true",
                        help="over the gestures and --after, time the page's frames and count Chrome's style, layout "
                             "and script work; with no gesture, the page running untouched")
    parser.add_argument("--software", action="store_true",
                        help="draw WebGL in software (SwiftShader), the weakest GPU a player may have, for timing")
    parser.add_argument("--profile", action="store_true",
                        help="over the gestures and --after, sample the page's thread and name its busiest functions")
    parser.add_argument("--load", action="store_true",
                        help="after --seconds, report what the page loaded and holds and the work its load took; "
                             "with --profile, sample its thread from the navigation instead")
    parser.add_argument("--heap", action="store_true",
                        help="from the navigation to --seconds, sample the JS heap's allocations, and name what still "
                             "holds them after a collection, by the function that made them")
    parser.add_argument("--cpu", type=float, default=1.0, metavar="N",
                        help="run the page's thread N times slower, as a weak machine does (Chrome's CPU throttling)")
    parser.add_argument("--warm", action="store_true",
                        help="as a returning visit: the page loaded once first, and its cache kept for the second")
    parser.add_argument("--mutations", type=seconds_type, default=0.0, metavar="SECONDS",
                        help="before the picture, count what the page changes in its DOM this long, by where (WEB-10)")
    parser.add_argument("--eval", metavar="JS", action="append", default=[],
                        help="before the picture, evaluate this in the page and print its value (a promise awaited); "
                             "repeat for several")
    parser.add_argument("--device", type=device_type, metavar="W,H[,DPR]", help="as a handset of that size sees it")
    parser.add_argument("--line", type=seconds_type, metavar="MS", help="every request this many ms slower (0-600)")
    parser.add_argument("--width", type=cli.counting, default=1280, help="the browser window's width")
    parser.add_argument("--height", type=cli.counting, default=800, help="the browser window's height")
    parser.add_argument("--port", type=port_type, default=8730, help="the port the host listens on")
    parser.add_argument("--debug-port", type=port_type, default=9230, help="the browser's DevTools port")
    parser.add_argument("--headed", action="store_true", help="open a real window, for a person to watch")
    return parser.parse_args()


if __name__ == "__main__":
    cli.entry(main)
