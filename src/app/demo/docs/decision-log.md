# Decision log — the demo

Why the demo is made as it is. Only decisions still binding are here.

## 2026-11-10 — a serverless demo, published to GitHub Pages

The owner asked for a pipeline to build and deploy GitHub Pages; told Pages cannot run the host HST-3 requires, the
owner, in as many words: "Create a serverless demo app. It dont need to run logic, just mock some state". So DEM-1, at
`P2`. The demo is not the game: HST-3 and HST-4 still bind the game, and the demo runs no game logic anywhere.

**The mocked state is the host's own recording.** At build time `shipstick-demo` lays the starter ship in the host's
`ServedShip`, stops ship time, and keeps the frame each of the host's clients would send: a player's at every seat,
the admin's entered in every capsule. The page is the client unchanged; `demo.js` replaces its socket before it opens
and plays those frames back, so the demo can never drift from what the host shows and holds no copy of a rule. An
admin's `enter` is answered with that capsule's frame; every other action is refused, as nothing runs to take it.

`.github/workflows/demo.yml` builds and tests on every push and pull request, writes the site, and deploys it to Pages
from `main`.
