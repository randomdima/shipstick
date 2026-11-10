# Documents — index

**Documents are sliced the way the code is.** Anything about one feature lives in that feature's own `docs/`; only
what belongs to no single slice is here. How work is done is [../CLAUDE.md](../CLAUDE.md); what the game is and how to
run it is [../readme.md](../readme.md).

## Cross-cutting

| Document | Holds |
|---|---|
| [goals.md](goals.md) | What the game is for, and the engineering rules once the owner states any |
| [priority.md](priority.md) | The rung every rule carries: `P0`–`P2` the owner's, `P3`–`P9` the assistant's |
| [requirements.md](requirements.md) | The rules that belong to no slice: `GAM` |
| [style.md](style.md) | The used-future look and voice (GAM-8): lore, names, captions, codex words, the interface, the art |
| [verification.md](verification.md) | The tiers, how a change is checked: `VER` |
| [slice-map.md](slice-map.md) | The slices, the projects, which way a dependency may point |
| [decision-log.md](decision-log.md) | Why the cross-cutting rules and the layout read as they do |
| [tech-debt.md](tech-debt.md) | What is known wrong, unmeasured or waiting on the owner, and what closes each |
| [../raw_assets/index.md](../raw_assets/index.md) | Where every image came from, the rules that keep it traceable, and the catalogue reuse is searched in |
| [../raw_assets/sets.md](../raw_assets/sets.md) | The asset sets: families alike in style and function, a reuse hint |

## The slices

| Slice | Holds |
|---|---|
| [core/](../src/core/) | `GameConfig`: every number the game runs on |
| [economy/](../src/economy/docs/design.md) | The crew's needs, the item catalogue (12 sections, 50 subsections × 100 items, made and ended many ways) the game reads, its roles and resource tree |
| [items/](../src/items/) | Items, slots and inventories; a player's drag |
| [devices/](../src/devices/) | Devices, the catalogue way each runs, and their cycles |
| [ship/](../src/ship/) | Capsules, doors, the clock, the starter ship |
| [codex/](../src/codex/mechanics.md) | The codex's book: every item and device, and the pages on how the ship works |
| [app/web/](../src/app/web/) | The client, plain JS and CSS: the player's page, the admin's, and the codex window |
| [app/host/](../src/app/host/docs/requirements.md) | The game's host: runs the game and serves its assets (client–server, `P0`) |

A slice's `docs/requirements.md` and `docs/decision-log.md` are made when it has its first rule or decision.

## Where each requirement ID lives

| Family | Document |
|---|---|
| `GAM-` | [requirements.md](requirements.md) — the game as a whole |
| `VER-` | [verification.md](verification.md) — how a change is checked |
| `ECO-` | [economy/](../src/economy/docs/requirements.md) — the item catalogue |
| `ITM-` | [items/](../src/items/docs/requirements.md) — items and slots |
| `DEV-` | [devices/](../src/devices/docs/requirements.md) — devices |
| `SHP-` | [ship/](../src/ship/docs/requirements.md) — capsules, doors, the clock |
| `WEB-` | [app/web/](../src/app/web/docs/requirements.md) — what the client is, what the player's and the admin's pages show, and the codex |
| `HST-` | [app/host/](../src/app/host/docs/requirements.md) — what runs and serves the game, and what a client is |

`qq req` prints this map off the documents themselves; `qq doclint` fails on a family this table does not name.

## Known gaps

- **Most assets are still drawings.** GAM-13 makes every asset a 3D model's render. On the floor, every device without
  a `.mesh.json` under `assets/devices/` stands as the plain crate until modelled — most of the starter ship's and all
  the rest of the catalogue's; the walls, doors and deck are blocks and plates wearing the kit's drawn
  pictures, not models of their own. On the page, the console kit — window housings, plates, keys, bezels, trim — and
  the repeating star fields are renders; the far galaxy, the nebulae and the star cluster, and the props (lamps,
  sockets, the manual and close keys) are still drawings, shown flat.
  `qq sprites check` traces each; a sprite whose variant has no `model` in its row is one still to model
  ([shapegen](../.claude/skills/shapegen/SKILL.md)).

- **There is no AI.** GAM-1 gives a capsule nobody holds to the AI; nothing plays one yet, so an empty seat's devices
  run but nobody moves its items ([tech-debt.md](tech-debt.md)).
