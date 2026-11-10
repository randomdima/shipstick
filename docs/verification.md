# Verification

**A claim is checked at the cheapest tier that can answer it.** The tiers are `Tier` on every test class
([tests/Tier.cs](../src/tests/Tier.cs)); `qq tests` turns a tier into a filter and a build.

| Tier | Asks its question of | Run |
|---|---|---|
| `unit` | the game's own types, engine-free: no page, no server, no clock | `qq tests` — after every edit |
| a picture | the page in a headless browser | `qq web --shot .tmp/web/<name>.png` — after a change that draws; not in the suite |
| frame time | the page under a gesture | `qq web --shot … --frames --drag A:B --drag-steps 120` — after a change to what moves (WEB-11): frames missed, and the page thread's style, layout and script time |
| DOM churn | the page left running, untouched | `qq web --shot … --mutations 3` — after a change to how the page draws (WEB-10): between frames no node is added or removed |

`qq tests all` is every tier that costs no money and needs nobody to look at a picture; it has five minutes and
prints what it spent of them. `qq checks` is the build, `all`, the citations, the art's provenance and the model rules `qq shapes` holds (proved on
fixtures by `qq shapes selftest`) — before a commit.

## Rules

**VER-1** `P3` A test states one exact behaviour or one stated requirement, and fails for nothing else.

**VER-2** `P3` Every test class carries one `Tier` and one `Priority` (`TierTests`).

**VER-3** `P5` A derivation written out twice, a drawn shape checked against the field it was drawn from, an index
asserted to be in range and `count > 0` are not tests.
