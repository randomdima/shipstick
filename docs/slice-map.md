# The slice map

**A feature is a folder, and everything about it lives in that folder** — its code, its `docs/`, its requirements,
its decisions, its tests (mirrored under `src/tests/`), its art (mirrored under `assets/`).

**All the code is under `src/`**, and a slice is named by its path within it — `ship/` is `src/ship/`.

## The tiers

From the bottom up: **a slice may know about the rows before its own and never the rows after it**, and there are no
cycles.

| Tier | Slices | May know about |
|---|---|---|
| **Kernel** | `core/` — config | Nothing else in the project |
| **Content** | `economy/` — the item catalogue, as data under `catalog/` compiled into the game, and its reader | Nothing: its files are read by it alone |
| **Game** | `items/` — items, slots, inventories; `devices/` — devices running catalogue ways; `ship/` — capsules, doors, the clock, the starter ship; `codex/` — the player's book of everything the game holds | core, economy, and each other in that order: `codex/` knows `economy/`, `ship/` knows `devices/` and `items/`, `devices/` knows `items/` |
| **Shell** | `app/web/` — the client, plain JS and CSS in `wwwroot/` with no project (WEB-9); `app/host/` — the game's host, running the game and serving the client (HST-3) | `app/host/` everything before it, and `app/web/` only as the files it serves; `app/web/` only the frames the host sends it (HST-4) |
| **Workshop** | `tests/` | Everything |

Where a lower slice needs something a higher one has, hand over the *data* and not the type.

## Projects

| Project | Compiles |
|---|---|
| `src/shipstick.csproj` | every slice except the shell and the tests — engine-free, testable without a host |
| `src/app/host/shipstick.host.csproj` | the game's host; references the game, and copies the client's files beside it |
| `src/tests/shipstick-tests.csproj` | the suite; references the game and the host |

The client is no project: its files are what the browser runs.

Every project's `bin/` and `obj/` are at the root, one folder a project ([Directory.Build.props](../Directory.Build.props)).
