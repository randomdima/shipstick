"""
Stand a slow line between a player's page and a served game: delay, jitter and stalls, both ways.

Multiplayer is judged by how it reads over a real line, and `tc netem` wants root while the browser's own throttling
does not reach a WebSocket. This is a localhost TCP relay instead: every chunk is held for the one-way delay and a
jitter drawn for it, in order — a TCP stream is never reordered — and now and then a direction is stalled outright,
which is what a lost segment and its retransmit look like to the other end. Point the server at `--to`, the page at
`--listen`; it runs for `--seconds` and says what it carried.

**`--kbps` narrows the line**: each direction is one bottleneck every connection of it shares — a page's socket and
its fetches alike, as a phone's downlink is — sent a segment at a time at that rate, with `--buffer-kb` queued in
front of it as a router's buffer is. Past that the relay stops reading, and its sockets' receive buffers are kept small,
so what the line cannot carry backs up into the server's own socket rather than into the relay. `--narrow-after`
stands a page up on the open line first.
"""

import argparse
import asyncio
import random
import socket
import time

from common import cli

#: What a call may take: the longest relay a run is watched through.
TIMEOUT_S = 3600

CHUNK = 64 * 1024

#: What a narrowed line sends at a time: an Ethernet segment's payload, so connections sharing it interleave.
SEGMENT = 1448

#: A narrowed line's receive buffers, kernel's and the stream's: little enough that the server's socket holds the backlog.
NARROW_RECEIVE_BYTES = 8 * 1024


def main():
    a = parse_args()
    return asyncio.run(relay(a))


def parse_args():
    parser = argparse.ArgumentParser(
        prog="qq line",
        description="Stand a slow line between a player's page and a served game: delay, jitter and stalls, both ways.",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--listen", type=port, default=8744, help="the localhost port the page joins on")
    parser.add_argument("--to", type=port, default=8740, help="the localhost port the game is served on")
    parser.add_argument("--delay-ms", type=millis, default=50.0, help="each way's delay; a round trip is twice it")
    parser.add_argument("--jitter-ms", type=millis, default=0.0, help="up to this much more, drawn afresh for each chunk")
    parser.add_argument("--stall-ms", type=millis, default=0.0, help="how long a stall holds a direction")
    parser.add_argument("--stalls-per-min", type=millis, default=0.0, help="how many stalls a direction takes a minute, at random")
    parser.add_argument("--kbps", type=rate, default=0.0,
                        help="each direction's rate in kilobits a second, shared by every connection; 0 for no limit")
    parser.add_argument("--buffer-kb", type=rate, default=64.0,
                        help="of --kbps, the kilobytes queued in front of each direction's line before it stops reading")
    parser.add_argument("--narrow-after", type=rate, default=0.0,
                        help="of --kbps, the seconds the line runs unlimited first: a page stood at full speed, then squeezed")
    parser.add_argument("--seconds", type=cli.counting, default=600, help="how long to relay before stopping")
    parser.add_argument("--seed", type=cli.counting, default=1, help="the draws' seed, so a run can be taken again")
    return parser.parse_args()


def port(text: str) -> int:
    value = int(text)
    if not 1024 <= value <= 65535:
        raise argparse.ArgumentTypeError(f"{value} is not a port from 1024 to 65535")
    return value


def millis(text: str) -> float:
    value = float(text)
    if not 0.0 <= value <= 10_000.0:
        raise argparse.ArgumentTypeError(f"{value} is not from 0 to 10000")
    return value


def rate(text: str) -> float:
    value = float(text)
    if not 0.0 <= value <= 1_000_000.0:
        raise argparse.ArgumentTypeError(f"{value} is not from 0 to 1000000")
    return value


class Bottleneck:
    """One direction's narrow line, every connection of it queued in front of it in the order it was read."""

    def __init__(self, kbps: float, buffer_kb: float, from_s: float):
        self.bytes_per_s = kbps * 1000.0 / 8.0
        self.buffer_bytes = buffer_kb * 1024.0
        self.from_s = from_s
        self.busy_until = 0.0
        self.most_queued = 0.0

    @property
    def narrow(self) -> bool:
        return self.bytes_per_s > 0.0 and time.monotonic() >= self.from_s

    def queued(self, now: float) -> float:
        return max(0.0, self.busy_until - now) * self.bytes_per_s

    async def room(self):
        """Back once the queue in front of the line is under its buffer."""
        while (over := self.queued(time.monotonic()) - self.buffer_bytes) > 0.0:
            await asyncio.sleep(over / self.bytes_per_s)

    def sent_at(self, now: float, size: int) -> float:
        """When a chunk read at ``now`` has left the line: after everything queued before it, at the line's rate."""
        if not self.narrow:
            return now
        self.busy_until = max(now, self.busy_until) + size / self.bytes_per_s
        self.most_queued = max(self.most_queued, self.queued(now))
        return self.busy_until


class Way:
    """One direction of one connection: what it carried and how often it was stalled."""

    def __init__(self, name: str, a, rng: random.Random, line: Bottleneck):
        self.name, self.a, self.rng, self.line = name, a, rng, line
        self.bytes = self.chunks = self.stalls = 0
        self.released = 0.0
        self.last = None

    def release_at(self, now: float) -> float:
        """When a chunk read at ``now`` goes on: its delay, a stall drawn for the time since the last, and never before the last."""
        held = now + (self.a.delay_ms + self.rng.uniform(0.0, self.a.jitter_ms)) / 1000.0
        since = 0.0 if self.last is None else now - self.last
        stall_chance = self.a.stalls_per_min / 60.0 * since
        self.last = now
        if self.a.stall_ms > 0.0 and self.rng.random() < stall_chance:
            self.stalls += 1
            held += self.a.stall_ms / 1000.0
        self.released = max(self.released, held)
        return self.released


async def carry(reader, writer, way: Way):
    queue: asyncio.Queue = asyncio.Queue()

    async def deliver():
        while (item := await queue.get()) is not None:
            at, data = item
            await asyncio.sleep(max(0.0, at - time.monotonic()))
            writer.write(data)
            await writer.drain()
        writer.close()

    delivering = asyncio.create_task(deliver())
    line = way.line
    try:
        while True:
            if line.narrow:
                await line.room()
            if not (data := await reader.read(SEGMENT if line.narrow else CHUNK)):
                break
            way.bytes += len(data)
            way.chunks += 1
            await queue.put((way.release_at(line.sent_at(time.monotonic(), len(data))), data))
    except (ConnectionError, OSError):
        pass
    await queue.put(None)
    await delivering


async def relay(a) -> int:
    rng = random.Random(a.seed)
    ways: list[Way] = []
    narrow_from = time.monotonic() + a.narrow_after
    uplink, downlink = Bottleneck(a.kbps, a.buffer_kb, narrow_from), Bottleneck(a.kbps, a.buffer_kb, narrow_from)
    narrow = a.kbps > 0.0
    limit = NARROW_RECEIVE_BYTES if narrow else 2 ** 16

    async def joined(page_reader, page_writer):
        try:
            town = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            town.setblocking(False)
            if narrow:
                town.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, NARROW_RECEIVE_BYTES)
            await asyncio.get_running_loop().sock_connect(town, ("127.0.0.1", a.to))
            town_reader, town_writer = await asyncio.open_connection(sock=town, limit=limit)
        except OSError:
            page_writer.close()
            return
        up, down = Way("page → town", a, rng, uplink), Way("town → page", a, rng, downlink)
        ways.extend([up, down])
        await asyncio.gather(carry(page_reader, town_writer, up), carry(town_reader, page_writer, down),
                             return_exceptions=True)

    server = await asyncio.start_server(joined, "127.0.0.1", a.listen, limit=limit)
    after = f" after {a.narrow_after:g} s" if a.narrow_after > 0.0 else ""
    line = f", {a.kbps:g} kbit/s each way behind {a.buffer_kb:g} KiB{after}" if narrow else ""
    print(f"relaying 127.0.0.1:{a.listen} → 127.0.0.1:{a.to} for {a.seconds} s: {a.delay_ms:g} ms each way, "
          f"+0–{a.jitter_ms:g} ms, {a.stalls_per_min:g} stalls of {a.stall_ms:g} ms a minute{line}", flush=True)
    async with server:
        await asyncio.sleep(a.seconds)

    for way in ways:
        if way.chunks:
            print(f"  {way.name}: {way.chunks} chunks, {way.bytes / 1024:.0f} KiB, {way.stalls} stalls")
    if narrow:
        print(f"  the most queued in front of the line: {uplink.most_queued / 1024:.1f} KiB up, "
              f"{downlink.most_queued / 1024:.1f} KiB down")
    return 0


if __name__ == "__main__":
    cli.entry(main)
