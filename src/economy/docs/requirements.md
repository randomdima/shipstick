# Requirements — the economy

The rules the item catalogue keeps ([design.md](design.md), [../catalog/sections.md](../catalog/sections.md)). Each
rule carries a rung ([../../../docs/priority.md](../../../docs/priority.md)); ECO-13 is held by the game reading the
catalogue's own files ([../Catalogue.cs](../Catalogue.cs)); `qq economy` checks every other one of them but
ECO-9 ([../../../docs/tech-debt.md](../../../docs/tech-debt.md)), and ECO-11 only where a way needs an item that has a
use of its own or a rate raises `fun` or `fitness`: whether the crew spends time on a thing is read by a person, with
`qq economy audit <sub>` listing the rates.

The numbering has gaps: the one-recipe, tier-ordered catalogue's rules 1 to 3 were retired when items came to be made
and ended many ways ([decision-log.md](decision-log.md)).

**ECO-4** `P7` An item's reach is the fewest roles, other than its maker's, among the devices of any chain of ways that
makes it from what comes in from outside, and is derived, never authored.

**ECO-5** `P7` Every crew and cabin stat has a source that takes other capsules; one whose lack kills soonest (a
floor stat) also has a source a capsule makes alone, and a better source that takes other capsules.

**ECO-6** `P8` Every ship stat is kept only by items and ways that take more than one role to make or run.

**ECO-7** `P6` Every item is made at least one way — a way makes it, a use leaves it, an item decays into it, or it is
the ship's stock — and ended at least one way — a way takes it, it is used, or it decays.

**ECO-8** `P3` Every item is reached by some run of ways from what comes in from outside: ways that take nothing
(harvest, salvage, the crew's body) and the ship's stock (DEV-2).

**ECO-9** `P3` No loop of ways gives back as much as it takes, so no loop alone keeps the ship (DEV-2).

**ECO-10** `P3` An item of the ship's stock is made from nothing outside it: aboard at launch in a finite amount, it is
made again only by ways that reclaim it from its own used forms, and fewer of it each time (DEV-2).

**ECO-11** `P6` What the crew member does something with — plays, reads, exercises, washes, cleans or treats with — is
a tool: a way needs it, spends the crew member's minutes, and gives what it is for. A rate (`/h`) is only for what works
without the crew's time, by being where it belongs: worn, on the cot, placed in the cabin, or a machine running itself;
and no rate raises `fun` or `fitness`, which only doing gives.

**ECO-12** `P3` Every item and every device has its codex words — what it is, and a line of flavour — so nothing the
game holds is missing from the codex (WEB-3).

**ECO-13** `P2` Every item, device and way of the catalogue is in the game, as the catalogue writes it.
