# The economy — needs, stats, ways and the resource tree

What a crew member needs to stay alive, what the ship needs to keep flying, and the ways that make and end everything
both use. The items themselves are the catalogue under [../catalog/](../catalog/sections.md), one file a subsection;
the tree they form is [resource-tree.md](resource-tree.md), generated from it by `qq economy`. The rules the catalogue
keeps are [requirements.md](requirements.md).

## Where the game stands

The game reads this catalogue (ECO-13): every item can sit in a slot, every device stands on a floor and runs whichever
of its ways its player chooses (DEV-5), and the codex shows all of it (WEB-3). The starter ship lays each capsule with
the universal fixtures and four devices of one role. What is **not yet aboard** is everything that moves a stat: using
an item, a way's `gives`, the needs' drift, decay and wear, fitting a part and installing a kit, and the ways the crew
runs by hand ([../../../docs/tech-debt.md](../../../docs/tech-debt.md)). The design below is what those will do.

It replaced a demo of four items and five devices, whose lessons still stand: cycles of seconds want a player clicking
every few seconds where an idle game wants minutes to hours; a single producer with a thin margin is a single point of
failure; a need that costs nothing when unmet is no need; four items leave nothing to decide; and a chain where nothing
wears out and nothing is left over runs forever once built.

## The crew member's needs

Every capsule holds one crew member. Each need is a meter from 0 to 100 that moves by itself and is moved back by
using an item or running a way. **Health at 0 is death.** The figures are a proposal for `GameConfig` and none is in
the code yet; the scale an item or a way moves each stat by is the `typical` column of
[../catalog/sections.md](../catalog/sections.md#stats).

| Need | Stat | Moves by itself, an hour | Met by | At the bad end |
|---|---|---|---|---|
| eat | `satiety` | −4 (empty after 25 h) | food: sprouts, rations, meals, snacks | at 0, health −4/h |
| drink | `hydration` | −6 (empty after 17 h) | water, drinks, juicy food | at 0, health −8/h |
| sleep | `rest` | −3 awake | sleeping on the cot; bedding and sleep aids add to it | at 0, falls asleep where they stand; stress +5/h |
| urinate | `bladder` | +5, and what is drunk | the toilet, a waste bag | at 100, an accident: hygiene −40, `cabin.clean` −20, stress +10, urine on the floor |
| defecate | `bowel` | +2, and what is eaten | the toilet with paper, a waste bag | at 100, the same, worse |
| wash | `hygiene` | −2 | the washbasin, soap, a shower, wipes | at 0, immunity −3/h, stress +2/h |
| exercise | `fitness` | −0.5 (bone and muscle in low gravity) | exercise gear and workouts | at 0, health −1/h, pain +1/h |
| medication | `immunity` | falls with poor hygiene and spoiled food | vitamins, vaccines, medicine | at 0, an illness: health −2/h until cured |
| medication | `pain` | rises with injury, poor fitness, poor sleep | painkillers, balms, first aid | at 100, health −2/h |
| medication | `health` | +1 while every need is fine | first aid, medicine | at 0, death |
| relaxation | `stress` | +1, more in a dark, cold, dirty or foul cabin | tea, scents, music, a soak, plants, a brew | at 100, every device the crew member runs works at half |
| recreation | `fun` | −2 awake | games, crafts, books, music, notes from neighbours | at 0, stress +3/h |
| — | `dose` | rises with cabin radiation | radioprotectants, shielding | above 80, health −5/h |
| — | `toxin` | rises in foul air and from spoiled or raw food | detox, clean water | above 80, health −5/h |

**The body is a way, too.** What is eaten fills `bowel` and what is drunk fills `bladder`; the toilet empties them and
makes urine and solid waste into its tank, which the capsule passes on to sanitation or watches fill. So the toilet is
a need with an input (toilet paper), an output (waste) and a device, like everything else.

**Death.** What a crew member's death does — the seat lost, the capsule left to the AI, a new crew member woken from
cryo — is the owner's call ([../../../docs/tech-debt.md](../../../docs/tech-debt.md)).

## The cabin and the ship

**The cabin's air is shared by the crew member and the plants in it.** Its stats move with the life support's inputs,
not with the crew member's own:

| Stat | Kept by | Lost to |
|---|---|---|
| `cabin.o2` | oxygen, canisters, the algae jar, houseplants | breathing (≈ 0.84 kg a crew-day), fires |
| `cabin.co2` | lowered by scrubbers, filters, plants | breathing, fires, combustion devices |
| `cabin.heat` | heaters, heat packs, insulation | the hull radiating, coolers |
| `cabin.pressure` | nitrogen, breathing mix, seals | leaks, breaches |
| `cabin.light` | lamps and panels, which burn out | darkness; low light raises stress and stops plants |
| `cabin.clean` | cleaning, mops, cleaning bots | crew use, spills, accidents, waste left on the floor |

**The ship's stats are everyone's.** No capsule keeps one alone, and the ship is lost when any reaches 0:

| Stat | Kept by | Lost to |
|---|---|---|
| `ship.hull` | hull plates, patches, sealants | micrometeoroids, a fixed fall a day |
| `ship.shield` | shield emitters, deflector coils, capacitors | radiation storms, debris |
| `ship.thrust` | fuel, propulsion parts | burns, which spend it |
| `ship.course` | navigation, star charts, course plots | drift, a fixed fall a day |
| `ship.grid` | power distribution parts, regulators | load on the grid, faults |
| `ship.data` | computing parts, data cards | wear of storage |

**The goal is distance.** The ship advances while `ship.thrust` and `ship.course` are both above half, and the run's
score is how far it gets before it is lost.

## Sections and subsections

The catalogue is **twelve sections**, each a need or what the needs stand on, divided into **fifty subsections of a
hundred items**: Food holds growth media, seeds, grains, vegetables, fruit, proteins, kitchen basics, cooked meals,
rations and snacks, from soil to a served plate. The list, with what each subsection covers, is
[../catalog/sections.md](../catalog/sections.md#subsections). A subsection is what an item *is*; the role of the
device that makes it is who *makes* it, and one subsection's goods may come from several roles.

## Items

An item is one of:

- **a resource** — has no use; it exists to be taken by a way;
- **a consumable** — its use moves stats once, when it is used at the fixture that takes it; it may leave something
  behind, as a meal leaves a dirty dish and food scraps;
- **a durable** — its use is a rate (`/h`) that holds while it is in use where it belongs, without the crew's time:
  clothing while worn, a blanket on the cot while the crew member sleeps, a plant, lamp or shelf placed in the cabin, a
  cleaning bot running itself, until it decays;
- **a tool** — has no use of its own; a way **needs** it, and the way gives what it is for: a deck of cards is needed by
  `play cards`, which spends half an hour of the crew member's and gives fun (ECO-11);
- **a spare part** — `fits` a device: the device runs while a part sits fitted, and stops when it has worn out;
- **a kit** — `installs` a device: put on free floor, it becomes that device.

**Doing things costs the crew member's time; having things does not replace it.** A rate on a dice set would count
every hour it sat on a shelf, and two sets would count twice, so owning would beat playing. As a tool, the dice give
fun only while the crew member plays, and the hours a crew member has in a day bound how much any tool gives. What a
durable gives is bounded the same way by where it belongs: a cot holds one mattress, one blanket and one pillow, and a
cabin's floor and walls only so many plants and shelves.

**Decay** is an item's own end: fresh food spoils into spoiled food, a medicine expires, a blanket wears into dirty
laundry, a lamp burns out. A durable decays while in use, a tool while a way that needs it runs, and a spare part while
fitted — a filter wears into a spent filter, a deck of cards into loose cards — anything else on the shelf. A stable
good keeps.

## Ways: made N ways, ended M ways

There is no research tree. **A way** is something run — by a device, a universal fixture or the crew's own hands — that
takes some items, makes others and may move stats as it runs:

| By | Example |
|---|---|
| a device | the water works distils raw water into drinking water; the galley cooks a meal |
| a universal fixture | the condenser wrings raw water from the air; the cot gives rest; the toilet takes toilet paper and makes solid waste |
| the crew | wiping the floor by hand; knitting a scarf |

An item is **made** by every way that makes it, every use that leaves it and every decay that becomes it; it is
**ended** by every way that takes it, its own use and its own decay (ECO-7). Drinking water, for one, is boiled on the
workbench from condensed water, distilled at the water works, melted from ice, reclaimed from urine and grey water —
and ended by drinking, washing, cooking, brewing and the farm. A basic good has several ways in and many out; a
specialised one may have one of each.

**Waste closes the loop.** What a crew member eats and drinks comes back as urine, solid waste, grey water and food
scraps; worn things come back as dirty laundry, broken parts and scrap. Those are the raw inputs of sanitation and
salvage, which feed water, compost and metal back to everyone. A capsule that does not pass its waste on fills its
toilet tank and its floor, and `cabin.clean` falls.

**Recycling is how the ship runs, and it is never whole** (DEV-2, the owner's). Every loop loses something on the way
round (ECO-9), so the ship also lives on what comes in from outside:

- **harvest and salvage** — ways that take nothing: mining, ice, the condenser, the solar strip, the salvage claw, the
  crew's own body;
- **the ship's stock** — what it set out with and nothing can make, aboard in a finite amount and stretched only by
  reclaiming it from its own used forms ([../catalog/sections.md](../catalog/sections.md#stock), ECO-10). The gene
  vault is one: every seed and culture line starts from it, and seed saved back from a harvest keeps a line going.

Every item is reached by some run of ways from those (ECO-8). An item's **depth** is the fewest rounds of ways from
them to it, derived by `qq economy`: water condensed from the air is 1, a cooked meal perhaps 6.

## Roles: which capsule makes what

**A device belongs to a role**, and a capsule's role is the set of devices its floor was laid with. Seventeen roles
make the whole economy, listed in [../catalog/sections.md](../catalog/sections.md#roles); a ship of fewer capsules
than roles is short of some and must do without, or lay a second role on a floor with room for it. Every capsule also
has the universal fixtures ([../catalog/any.md](../catalog/any.md)): a workbench, a cot, a toilet, a washbasin, a mess
table, life support, a locker, and the slow survival devices.

### Reach: how many hands an item takes

An item's **reach** is the fewest roles, other than its maker's, among the devices of any chain of ways that makes it
from nothing (ECO-4). It is derived by `qq economy`, never authored:

| Reach | Means |
|---|---|
| **solo** (0) | the capsule makes it alone, from its own raw inputs |
| **pair** (1) | one other role's goods come through a door |
| **trio** (2) | two other roles |
| **crew** (3+) | it takes the ship: goods relayed through capsules that do not border the maker |

Reach counts the whole chain, so it climbs fast: power is in most chains. **Door reach** counts only the roles whose
goods a way takes straight in — the neighbours its capsule actually trades with — and is the measure of how much one
way asks of the doors. On a ship that lays one role a capsule, reach is the least number of other capsules an item
depends on, and a reach above the number of the maker's neighbours means goods must be relayed. **Every need has a
solo-reach floor and a crew-reach ceiling**: water can be had from one's own condenser, badly; a proper meal takes a
farm, a galley and a bio lab.

## Balance

**What a thing costs is its work-minutes**: the fewest, over every way that makes it, of the way's minutes plus what
its inputs cost and the share of each tool's life one run wears away, shared among what one run makes. What a use
leaves — waste, a dirty dish — is free; what an item decays into costs what the item did, since it had to be had. `qq economy` derives it
for every item and reports how many points of each stat a work-minute of each source buys, so a source that is far
cheaper or far dearer than its peers stands out.

The levers, each to be authored on `GameConfig` once the catalogue is loaded by the game:

- **Need rates** — the needs table above. A crew-day takes about 96 points of satiety and 144 of hydration.
- **Way minutes** — minutes to hours, so a chain set up in the evening runs through the night. Raw extraction and
  growing are slow; assembly is quicker and dearer in inputs.
- **Stack size and door slots** — what a door holds bounds what one trade carries, and so how often neighbours must
  meet.
- **Wear** — how many runs a device lasts on one spare part, so that every chain needs a trickle of parts from the
  fabricators.
- **Decay** — how fast food spoils and durables wear, which makes preserves a real choice over fresh meals and keeps
  laundry and bedding flowing.

**The balance targets**, which `qq economy` checks against the catalogue:

1. Every floor stat has a solo-reach source, so an isolated crew member survives a while, badly.
2. Every crew and cabin stat has sources that take other capsules, and for a floor stat a better one, so cooperation
   pays.
3. Every ship stat is kept only by goods that take more than one role, so no capsule keeps the ship alone.
4. Every item is made and ended at least one way, and is reached from harvest, salvage or the ship's stock.
5. No loop gives back all it takes — not yet checked: items carry no mass to weigh a loop by.
