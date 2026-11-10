# Decision log — the demo

Why the demo is made as it is. Only decisions still binding are here.

## 2026-11-10 — a serverless demo, published to GitHub Pages

The owner asked for a pipeline to build and deploy GitHub Pages; told Pages cannot run the host HST-3 requires, the
owner, in as many words: "Create a serverless demo app. It dont need to run logic, just mock some state". So DEM-1, at
`P2`. The demo is not the game: HST-3 and HST-4 still bind the game, and the demo runs no game logic anywhere.

**The mocked state is the host's own recording.** At build time `shipstick-demo` lays the starter ship in the host's
`ServedShip` and advances it a host's tick at a time over `DemoFigures.RecordedS`, keeping each frame one of the
host's clients would send when its view changes: a player's at every seat, the admin's entered in every capsule. The
page is the client unchanged; `demo.js` replaces its socket before it opens and plays those frames back on the page's
clock, in a loop, so the floor animates as on a host — cycles fill, parts turn, stock runs down — and the demo can
never drift from what the host shows and holds no copy of a rule. At the loop's end the ship starts again from its
first frame. An admin's `enter` switches to that capsule's recording; every other action is refused, as nothing runs to
take it.

**Frames are kept as patches on the one before** (`FramePatch`): whole, the admin's frames over ten minutes are
hundreds of megabytes; patched, the recording is about 6 MB, 0.3 MB as served compressed.

`.github/workflows/demo.yml` builds and tests on every push and pull request, writes the site, and deploys it to Pages
from `main`.
