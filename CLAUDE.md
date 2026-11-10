# shipstick — working agreement

A slow-paced multiplayer browser game: each player runs one capsule of a large space ship, and the ship works only if
the capsules manage to cooperate without ever talking directly. C# on .NET 11, always client–server: the host runs the
whole game, a browser page only shows what its player sees and sends actions (HST-3, HST-4), in plain JS and CSS with
no bundler (WEB-9). What it is for
is [docs/goals.md](docs/goals.md); the owner's design is [readme.md](readme.md); every document is indexed by
[docs/index.md](docs/index.md).

## Everything is a vertical slice

**A feature is a folder, and everything about that feature lives in it** — its code, its `docs/`, its requirements,
its decisions, and its art at the matching path under `assets/`.

- **Code** is under `src/`, a slice named by its path within it — `ship/` is `src/ship/`. A dependency points **down**
  the tiers in [docs/slice-map.md](docs/slice-map.md), never up, and there are no cycles. Where a lower slice needs
  something a higher one has, hand over the *data* and not the type.
- **Tests.** `src/tests/` mirrors the tree it tests, folder for folder.
- **Docs.** A rule about one feature is that feature's `docs/requirements.md`. Only what belongs to no single slice goes
  in [docs/](docs/index.md).
- **Decisions.** The nearest `decision-log.md` — the slice's own where the decision is the slice's.
- **Assets.** `assets/` mirrors the code tree. **Every image traces to the prompt that made it**: a `.src.json` beside
  it names the variant kept under `raw_assets/`, whose frame record holds the prompt, model and inputs. **Every asset
  is a 3D model's render (GAM-13, `P0`)**: the shapegen skill and `qq shapes`, its textures generated with the
  remotegen skill; cut, keep and install with `qq sprites`; the rules are [raw_assets/index.md](raw_assets/index.md).
  **A generation's shape is the owner's** (remotegen's core rule): its model, its settings, and how many generations one
  asset is made from. Anything else is asked first and generated only on a yes. **What is kept is used before anything
  is generated**: `qq shapes library` lists the kept textures and 3D parts, and remotegen refuses a cell already kept.
- **Numbers.** On `GameConfig` ([core/config](src/core/config/GameConfig.cs)), authored in the nested groups and derived
  on the root. **A literal in behaviour code is a defect.** What is authored is a raw term; a derived figure may be
  printed and compared, never authored and back-solved into a primitive.

**Everything a player meets is used-future company hardware** (GAM-8, `P2`): the interface, the art, every name,
caption, codex line, lore and flavour keep [docs/style.md](docs/style.md) — monochrome phosphor screens in worn,
bolted housings, codes and serials, the cold voice of Consolidated Orbital Freight; red is an alert and nothing else.
Read it before writing a caption, a name, a codex line, a stylesheet rule or an image brief.

**Nothing grows past being readable.** A document that has to cover eight things is eight documents and an index, and
the same is true of a type. A slice's `docs/` gets an `index.md` only once it holds more than two documents.

## Which document to open first

| Doing | Read |
|---|---|
| Anything, before the first edit | this file, then [docs/goals.md](docs/goals.md) |
| Working on one feature | that feature's own `docs/`, found from [docs/index.md](docs/index.md) |
| Changing what the game *does* | the rule that owns it — `qq req <ID>` |
| Adding a file, or wondering where something goes | [docs/slice-map.md](docs/slice-map.md) |
| Changing a number | `GameConfig`, never a literal at the call site |
| Writing anything a player sees — UI, CSS, a name, a caption, codex words, lore, an image brief | [docs/style.md](docs/style.md) |
| Deciding how a change gets checked | [docs/verification.md](docs/verification.md) |
| Asking "why is it like this?" | the nearest `decision-log.md` — never the code, which carries no history |
| Finding an issue you are not fixing now, or fixing one | [docs/tech-debt.md](docs/tech-debt.md) — written in, or deleted from, in the same change |
| Understanding how one type works | that type's XML docs. There is no second description of it anywhere |
| Opening a file you have not read | `qq outline <file>` first — the members and their line ranges, so the read is a range |
| Weighing a rule against a change | its rung, and [docs/priority.md](docs/priority.md) — `P0` is not yours to trade |
| Building, running | [readme.md](readme.md) |

## Where the documentation lives, and why there is so little of it

**The code is the documentation.** Types carry `<summary>` and `<remarks>`, and a gotcha, an invariant or an external
constraint belongs on the type that has it. What is written down is only what the code cannot state.

1. **A rule states a relation; a number is data.**
2. **History lives in a `decision-log.md` and nowhere else.** A superseded decision is deleted, not annotated.
3. **No requirement ID is ever renumbered**, and a retired number is never reused. The code cites them.
4. **Nothing about this project is remembered anywhere else.** No assistant memories, no private notes. Write a finding
   into the document or the doc comment that owns it, at the moment it is learned.
5. **Every rule carries a rung** — `**GAM-2** `P3` …` ([docs/priority.md](docs/priority.md)). `qq doclint` fails on a
   rule that carries none.

## Whose rule it is

**`P0`–`P2` are the owner's, stated in as many words; `P3`–`P9` are yours — created, implied or assumed.**

- **`P0` bends for nothing.** Find one inconvenient and you report the conflict and stop.
- **`P1` bends at a genuine edge case or in a fixture**, and the bend goes in the nearest `decision-log.md`.
- **`P2` is a direction the owner set**: the how is yours, the direction bends only when the owner agrees.
- **Nothing is ever argued upward into `P0`–`P2`.** They are granted by the owner saying so, in as many words, and
  the decision log quotes the words. A rule you wrote is yours however sure you are of it.
- **A `P0` the code does not meet is a gap named in [docs/index.md](docs/index.md#known-gaps)**, not a rule reworded.

**Debt is written down the moment it is known.** Every issue found and not fixed in the same piece of work goes into
[docs/tech-debt.md](docs/tech-debt.md) before the work is reported — a failing test, a deferred cleanup, a question
waiting on the owner (_owner_). Each entry says where it is, what it costs and what closes it; one fixed is deleted.

## Verification

**A claim is checked at the cheapest tier that can answer it.** **A test states one exact behaviour or one stated
requirement and fails for nothing else** (VER-1). Every test class carries a `Tier` and a `Priority` trait
([tests/Tier.cs](src/tests/Tier.cs), [tests/Priority.cs](src/tests/Priority.cs)); `TierTests` fails a class missing either.

| Ran | After |
|---|---|
| `qq tests` | **every edit** |
| `qq tests --changed` | an edit worth more than the unit tier — it names the tiers the tree's changes can have moved |
| `qq tests all` | before a commit |
| `qq checks` | before a commit: build, `all`, citations, art provenance, the model rules `qq shapes` holds |
| `qq web --shot .tmp/web/<name>.png` | a change that draws — then `Read` the picture |

**Run the tier the change can have moved, never the whole suite by habit**, and wait for a test run rather than
backgrounding and polling it. **A run leaves the machine usable**: `qq tests` and `qq checks` are light by default (low
priority, half the cores); `--full` is for when asked.

**Never open a browser by hand to look at something `qq web --shot` can answer**, and **no tool opens a window on the
owner's desktop**: `qq web` drives Chromium headless; `--headed` is for when the owner asks to watch.

## House rules

- **Edit with the file tools**, not `sed`/`python3` one-liners. Shell text processing is read-only inspection.
- **Work stays in the local repository.** Nothing is published: no artifacts, no hosted documents or pages
  (`.claude/settings.json` denies those tools). A page to look at is written to `.tmp/` and pictured headless.
- **Scratch goes in `.tmp/`**, gitignored and wiped without asking — never the system temp directory or a per-session
  scratchpad.
- **Metric units, and the unit is part of the name** — `…M`, `…S`, `…Px`.
- **Prefer moving code to deleting it**, and commit before a change large enough to want an undo.
- **A rule is cited by ID and the citation is checked**: `qq doclint` (inside `qq checks`) fails when a cited ID
  resolves to nothing; `qq req <ID>` looks one up.
- **The `qq` tools are this project's, in `.qq/`**; extend or fix one rather than routing around it. They are design
  time only: nothing the game runs on is one, and none is published (HST-2).
