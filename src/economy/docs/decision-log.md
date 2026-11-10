# Decision log — the economy

Why the item catalogue is shaped this way. Only decisions still binding are here.

## 2026-11-05 — five thousand items, as data in Markdown tables

The owner asked for fifty logical groups of a hundred items each, fitting a crew member's and a ship's needs, with the
devices and chains that make them. That is far past what `GameConfig` can hold readably, and content rather than a
tuning figure. So the catalogue is data, one Markdown table set a subsection under `catalog/`, read by `qq economy`
and by the game (ECO-13). `GameConfig` keeps the figures that tune the whole catalogue (need decay,
wear, stack size); a way's own amounts and minutes stay in its row, as a sprite's prompt stays in its frame record. The
resource tree is generated from the tables, never written beside them, so it cannot drift.

## 2026-11-05 — sections of subsections, named by the need they serve

The owner asked for the needs — eat, drink, sleep, the toilet, medication, relaxation, recreation — to be the major
sections, each divided into subsections holding everything of that need from raw to final, without raising the total.
So the fifty groups became fifty subsections of a hundred items in twelve sections, and the industrial groups were
merged (ores with ice, metals' neighbours, parts with tools) to make room for sleep aids, the toilet, cleaning,
relaxation, plants, arts, books and exercise. A subsection is what an item *is*; a device's role is who *makes* it, and
a subsection's devices may be of more than one role.

## 2026-11-05 — items are made and ended many ways, not by one recipe each

The owner asked that an item be "produced N ways and consumed M ways — by a device, a human, or on its own via decay"
rather than sit in a research tree. So a recipe became a **way**: a device, a universal fixture or the crew's hands
taking some items and making others, and giving stats as it runs (sleep, the toilet, a shower). An item is made by any
way that makes it, by a use that leaves it, by a decay that becomes it; it is ended by any way that takes it, its own
use or its own decay (ECO-7). That retired the one-recipe rule, the tier ordering and the rule that every item has a
use (1, 2 and 3 of the family): ways loop — urine is reclaimed into the water that is drunk into urine — so a tier
cannot order them. What the tiers guarded, that nothing exists only by feeding itself, is now that every item is
reached from what comes in from outside (ECO-8). Depth (the rounds of ways from outside), reach and cost are fixpoints
over the ways, derived by `qq economy` and never authored (ECO-4).

## 2026-11-05 — recycling is the ship's core, never whole, and some stock is finite

The owner, in as many words: "loops are absolutely possible, recycling is how whole ship system should operate, not
100%, but in core essence; we still need to harvest some external materials or salvage", and "a chain can absolutely
not start from nothing, like some rare recyclables that are of limited supply and can never be produced". So DEV-2,
which had forbidden loops among devices so that every chain started at a device taking nothing, was rewritten to say
that, at `P2`: a direction the owner set ([../../../docs/priority.md](../../../docs/priority.md)). The catalogue's
consequences are the assistant's, at `P3`: every item is reached from harvest, salvage or the ship's stock (ECO-8);
no loop gives back all it takes (ECO-9); and the stock is a table of items nothing outside makes (ECO-10), the gene
vault the first of them. Its two ways from nothing were deleted, so seed and culture lines start from the vault and are
kept by saving seed back. ECO-9 is not checked yet: items carry no mass, and counting units round a loop confounds
power, catalysts and reusable things like dishes with material.

## 2026-11-05 — the game reads the catalogue's own files

The owner, asked what the codex should hold: "We dont need non-game codex. Add all items ingame. And codex must be
always up to date. There cannot be items that are not in the codex." So ECO-13, at `P2`: the catalogue's Markdown files
are compiled into the game and read by `Catalogue` at start, rather than turned into C# or a generated data file a step
could forget to refresh. The reader trusts what `qq economy` checks and fails on a cell it cannot read. Each item's and
device's codex words — a sentence of what it is, a line of flavour — are a `## Codex` table in its own file (ECO-12),
beside the rows they describe, never repeating a number those rows hold.

## 2026-11-05 — what the crew does something with is a tool, not a rate

A review of the catalogue found about 640 durables with a rate counted for every hour of their life, used or not: a
dice set made from one piece of scrap gave 5000 fun, and two gave 10 000. Owning had replaced doing, durables
outscored every one-shot source of their stat by orders of magnitude, and the crew member's own hours — the scarcest
thing an idle game has — cost nothing. So ways gained a `needs` column: tools at hand while the way runs, kept after
it, wearing only meanwhile. What the crew plays, reads, exercises, washes, cleans or treats with became a tool needed
by a way that gives the stat once a run (ECO-11); a rate stayed only on what works without the crew's time — worn, on
the cot, placed in the cabin, a machine running itself. Tools also take catalysts and reusable gear out of loops,
where a take-and-make-back would have muddled ECO-9's count.

## 2026-11-05 — any subsection may take any item

The first catalogue let a group take only another group's ten anchors, which kept fifty groups writable apart and made
them stand in for what they could not name (lead smelted from broken parts). The items were written first and the ways
second, every subsection's items in hand, so the anchors were dropped: a way names whatever it really takes. A short
list of pinned items — power, water, oxygen, the body's waste, dishes, scrap, containers — was fixed first so that the
items' own `leaves` and `decays` could name them before the rest existed.

## 2026-11-05 — a universal floor keeps a lone capsule alive, badly

Nearly every good takes power or water from another role, so without help no capsule could keep any need alone, and
one absent neighbour would kill. The universal fixtures (`catalog/any.md`) run slow, poor ways to power, water, oxygen,
sprouts, heat, sleep, the toilet and a wash, so a capsule cut off survives long enough for the ship to notice — and
every better source takes other capsules (ECO-5). The fixtures make the subsections' own items, so a capsule's
condensed water is the same Raw Water a water works makes faster.
