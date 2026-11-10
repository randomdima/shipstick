# The catalogue — sections, subsections, roles and stats

The index of the item catalogue. What it all means is [../docs/design.md](../docs/design.md); the rules it keeps are
[../docs/requirements.md](../docs/requirements.md). `qq economy` reads every table here and in the subsection files, so
a table's columns are its schema.

## How a subsection file reads

One file a subsection, named by its code: `wat.md` holds the subsection `wat`. It has three tables.

**Devices** — `| id | device | role | cells |`. The id is `<sub>.<name>`, lower case; the role is one of the roles
below, and one the subsection lists; cells are columns by rows, `2x1`. The universal fixtures are [any.md](any.md).

**Items** — `| id | item | use | decays |`, a hundred rows, `<sub>-001` to `<sub>-100`:

| Column | Holds |
|---|---|
| `use` | what the crew member gets from it, comma-separated: `satiety +25`, `bowel +8` once; `rest +2/h` while it is in use where it belongs (a durable: worn, on the cot, placed in the cabin); `leaves 1 cln-001` when used; `fits wat.melter` (a spare part); `installs wat.melter` (a kit); or `—`, as a resource or a tool has |
| `decays` | `72 h` (it is gone), `72 h → san-003` (it becomes that), or `—` (it keeps). A durable's hours count while it is in use, a tool's while a way that needs it runs, a spare part's while it is fitted (each wears into what it becomes), anything else's on the shelf |

**Ways** — `| way | by | min | needs | takes | makes | gives |`, every way an item is made, ended or a need is met:

| Column | Holds |
|---|---|
| `way` | a few words: `melt ice`, `urinate`, `bake bread` |
| `by` | a device of this file, a universal fixture `any.<name>`, or `crew` — by hand, anywhere |
| `min` | minutes one run takes |
| `needs` | tools: `1 fun-002`, at hand while the way runs and kept after it, or `—`. A table that needs none may leave the column out |
| `takes` | `2 grn-004, 1 pwr-001`, or `—` |
| `makes` | `1 grn-010, 1 san-002`, or `—`; a way may make several things |
| `gives` | what one run does to a stat, `rest +40, stress -5`, or `—`; a way makes or gives something |

**Codex** — `| id | about | flavour |`, a row for every device and every item of the file, devices first: what the
game's codex shows on its page (ECO-12).

| Column | Holds |
|---|---|
| `about` | one plain sentence in an operating manual's register: what it is and what it is for, as a player needs to know it — never its numbers, which the codex reads off the tables |
| `flavour` | one line in the Company's voice or a worn operator's — a stencil, a notice, a form, a maintenance tag, a scrawled note — shown small under it |

A way may need, take, make or leave any item of any subsection. An item is **made** by a way that makes it, a use that
leaves it or a decay that becomes it; it is **ended** by a way that takes it, its own use or its own decay (ECO-7). **A
thing the crew does something with is a tool, never a rate** (ECO-11): a deck of cards is needed by `play cards`, which
gives the fun; a blanket on the cot is a durable, `rest +2/h`. Names and
codex words keep [../../../docs/style.md](../../../docs/style.md) (GAM-8): a device is a model designation and its noun
phrase, `HX200 Moisture Condenser`; an item is inventory nomenclature, `Water, Drinking`. Names are unique across the
catalogue: never an upper-case letter, a hyphen and a digit together (write `B12`, `U235`, `Mk II`), which the
citation checker reads as a rule's ID. `qq economy words` sets names and codex words from JSON without retyping a row.

## Sections

| section | name | the need it serves |
|---|---|---|
| food | Div 01 Provisions | operator nutrition: satiety, from growth medium to a served meal |
| drink | Div 02 Potables | operator fluids: hydration, and the issued drinks that relax |
| air | Div 03 Atmosphere & Climate | respiration and heat: the cabin's air and temperature |
| sleep | Div 04 Rest | operator rest |
| toilet | Div 05 Sanitation & Hygiene | waste, washing, a clean cabin, and where the waste goes |
| medicine | Div 06 Medical | health, pain, immunity, dose and toxin |
| relax | Div 07 Stress Control | operator stress |
| recreation | Div 08 Recreation & Morale | morale, fitness, and the notes that pass through doors |
| clothing | Div 09 Garments | warmth and comfort worn on the body |
| materials | Div 10 Materials & Power | what everything aboard is made of, and the power that runs it |
| parts | Div 11 Parts & Fixtures | what devices are built and repaired from |
| ship | Div 12 Vessel Systems | the carrier's own systems |

## Subsections

| sub | name | section | roles | covers |
|---|---|---|---|---|
| soi | Growth Media & Nutrients | food | agri | soil, hydroponic solution, fertilizer from compost and urine, substrates, plant care |
| bio | Seeds, Starters & Cultures | food | bio, agri | seeds, cuttings, spores, yeast, starter cultures, insect and fish breeding stock |
| grn | Grains & Staples | food | agri, galley | wheat, rice, potatoes, beans: harvested, threshed, milled into flour, meal and dough |
| veg | Vegetables & Greens | food | agri | sprouts, leaves, roots, mushrooms: fresh, washed, chopped |
| frt | Fruit & Berries | food | agri | berries, dwarf citrus, melons: fresh, pressed, dried |
| prt | Proteins | food | bio, agri | insects, eggs, algae protein, cultured meat, tofu, aquaponic fish |
| ing | Galley Stores | food | galley | oil, salt, sugar, spices, sauces, stock, butter, cheese |
| mel | Cooked Meals | food | galley | hot meals, served on a clean dish: the highest satiety |
| prs | Rations & Preserves | food | galley, cargo | canned, dried, pouched and emergency food that keeps |
| snk | Snacks & Confectionery | food | galley | biscuits, chocolate, candy, crisps: low satiety, some morale |
| wat | Water | drink | hydro, mine | water raw to drinking, every way it is had: condensed, melted, reclaimed, distilled |
| bev | Beverages | drink | galley | tea, coffee, juice, milk, broth, electrolyte drinks |
| brw | Brews & Ferments | drink | bio, galley | beer, wine, cider, kombucha, spirits: less stress, some toxin |
| gas | Air & Gases | air | atmos | oxygen, nitrogen, carbon dioxide, breathing mix, canisters |
| fil | Filters & Scrubbers | air | atmos, hydro | air and water filters, scrubber beds, membranes, and their spent forms |
| thm | Heat & Cooling | air | atmos, power | heaters, coolant, insulation, heat packs |
| bed | Beds & Bedding | sleep | quarter | mattresses, pillows, blankets, sheets: rest while they lie on the cot |
| slp | Sleep Aids | sleep | quarter, med | eye masks, earplugs, sleepwear, white-noise boxes, sleep tea, melatonin |
| toi | Toilet & Body Waste | toilet | sanit | urine, solid waste, toilet paper, waste bags, toilets and their parts |
| san | Waste Treatment | toilet | sanit | grey water, food scraps, spoiled food and body waste made into water, compost, biogas and fertilizer |
| hyg | Personal Hygiene | toilet | sanit, quarter | soap, shampoo, toothpaste, razors, towels, wipes, showers |
| cln | Cleaning & Laundry | toilet | sanit | dishes, laundry, detergents, mops, cleaning bots: a clean cabin |
| med | Medicines | medicine | med, chem | painkillers, antibiotics, vitamins, sedatives, antivirals, ointments |
| sup | Medical Supplies | medicine | med | bandages, splints, syringes, first-aid kits, test strips |
| rad | Radiation & Toxin Treatment | medicine | med | radioprotectants, chelators, detox, dosimeters, shielding garments |
| rlx | Stress Relief | relax | quarter | scents, massage oil, warm soaks, meditation mats, stress balls, music boxes |
| grd | Ornamental Plants & Animals | relax | agri, bio | houseplants, bonsai, terrariums, aquarium fish: living stock that calms and freshens the air |
| fun | Games & Pastimes | recreation | quarter, fab | cards, board games, puzzles, dice, model kits |
| art | Arts, Crafts & Music | recreation | quarter | paints, sketchbooks, knitting, instruments, sheet music |
| lib | Books & Media | recreation | elec, quarter | books, films, music, game cartridges, readers |
| fit | Exercise | recreation | quarter, fab | treadmill, bands, weights, rowing machine and their parts: fitness |
| sig | Notes, Tokens & Signals | recreation | helm, quarter | notes, request tags, gifts, tokens passed through doors: the only traffic between capsules |
| fib | Fibres & Textiles | clothing | quarter, chem | fibres, yarn, thread, fabric |
| clo | Garments & Wearables | clothing | quarter | jumpsuits, socks, thermal layers, slippers; worn into dirty laundry |
| ore | Ores, Ice & Regolith | materials | mine | ores, water ice, volatiles, regolith |
| pwr | Power & Cabling | materials | power | power, cells, batteries, cables, panels, reactor parts: `ship.grid` |
| met | Metals & Alloys | materials | smelt | ingots, sheet, wire, alloys |
| cer | Ceramics, Glass & Composites | materials | smelt | glass, ceramic, fibre composites, structural panels |
| chm | Chemicals | materials | chem | acids, bases, salts, solvents, reagents |
| pol | Polymers, Seals & Lubricants | materials | chem | plastics, rubber, sealants, lubricants, resins |
| scr | Salvage & Recycling | materials | sanit, smelt | scrap, broken parts, e-waste, sorted and reclaimed into feedstock |
| pak | Containers & Packaging | materials | cargo | pouches, bottles, canisters, crates: filled, emptied, washed and filled again |
| mec | Mechanical Parts & Tools | parts | fab | gears, bearings, pumps, valves, hand tools; spare parts that fit devices |
| ecp | Electronics & Computing | parts | elec | components, boards, chips, computers, data storage |
| lgt | Lighting & Sensors | parts | elec | lamps, grow lights, sensors, optics: `cabin.light` |
| fur | Furniture & Device Kits | parts | cargo, fab | kits that install devices, furniture |
| hul | Hull, Repair & Safety | ship | fab | hull plates, patches, sealant, fire suppression, emergency gear: `ship.hull` |
| nav | Navigation & Data | ship | helm, elec | charts, course plots, gyros, star trackers, ship computers: `ship.course`, `ship.data` |
| shd | Shields & Deflection | ship | helm | shield emitters, deflector coils, capacitors: `ship.shield` |
| prp | Propulsion & Fuel | ship | drive | fuel, propellant, thrusters, nozzles: `ship.thrust` |

## Pinned items

The goods most ways take or leave, fixed here so every subsection can name them. Each is the item its subsection file
holds at that id.

| id | item |
|---|---|
| pwr-001 | Power, Grid |
| wat-001 | Water, Drinking |
| wat-002 | Water, Raw |
| gas-001 | Oxygen |
| gas-002 | Carbon Dioxide |
| veg-001 | Sprouts |
| toi-001 | Urine |
| toi-002 | Waste, Solid |
| toi-003 | Paper, Toilet |
| toi-004 | Bag, Waste |
| toi-005 | Bag, Waste, Filled |
| san-001 | Water, Grey |
| san-002 | Scraps, Food |
| san-003 | Food, Spoiled |
| hyg-001 | Soap |
| cln-001 | Dish, Dirty |
| cln-002 | Dish, Clean |
| cln-003 | Laundry, Dirty |
| scr-001 | Scrap, Metal |
| scr-002 | Scrap, Plastic |
| scr-003 | Scrap, Electronic |
| scr-004 | Parts, Broken |
| scr-005 | Scrap, Fabric |
| pak-001 | Pouch, New |
| pak-002 | Pouch, Empty |
| pak-003 | Bottle, Clean |
| pak-004 | Bottle, Empty |
| pak-005 | Canister, Serviced |
| pak-006 | Canister, Empty |

## Stock

What the ship set out with that nothing can make: a finite supply aboard at launch, stretched only by reclaiming it
from its own used forms, and never wholly (ECO-10). How much of each is aboard is a figure for `GameConfig`.

| id | item |
|---|---|
| bio-001 | Sample, Gene Vault |

## Roles

| role | name |
|---|---|
| mine | Extraction Station |
| power | Power Plant |
| hydro | Water Works |
| atmos | Atmosphere Control |
| agri | Hydroponic Farm |
| bio | Bio Lab |
| galley | Galley |
| med | Medbay |
| sanit | Sanitation |
| quarter | Crew Quarters |
| smelt | Foundry |
| chem | Chem Lab |
| fab | Fabrication Shop |
| elec | Electronics Shop |
| helm | Bridge |
| drive | Engine Room |
| cargo | Stores |

## Stats

`better` says which way a stat is helped: an item that keeps `stress` low lowers it, `stress -10`. `floor` marks the
needs whose lack kills soonest, which a capsule can keep alone from the universal fixtures ([any.md](any.md)), badly
(ECO-5). `typical` is the scale a use or a run moves it by.

| stat | of | better | floor | typical | means |
|---|---|---|---|---|---|
| health | crew | higher | no | first aid +10, surgery kit +40 | operator viability; the operator is lost at 0 |
| satiety | crew | higher | yes | sprouts +4, snack +8, ration +20, meal +35 | nutritional state |
| hydration | crew | higher | yes | sip +5, cup +15, bottle +25 | fluid state |
| rest | crew | higher | yes | nap +10, a night on a bare cot +40; bedding +1/h to +4/h | rest state |
| bladder | crew | lower | no | a drink +10 to +20; urinating -100 | urinary load |
| bowel | crew | lower | no | a snack +3, a meal +10; the toilet -100 | bowel load |
| hygiene | crew | higher | no | wipe +8, wash +15, shower +40 | personal hygiene |
| fitness | crew | higher | no | stretch +5, a workout +20 | bone and muscle retained in low gravity |
| immunity | crew | higher | no | vitamins +5, vaccine +40 | resistance to illness |
| pain | crew | lower | no | balm -10, painkiller -30, nerve block -60 | pain level |
| stress | crew | lower | no | tea -5, music -10, a long soak -25; a brew -15 | strain; at 100 every device the operator runs works at half rate |
| fun | crew | higher | no | a puzzle +10, a game night +30 | morale: freedom from boredom |
| dose | crew | lower | no | iodine tablet -10, chelation -40 | accumulated radiation |
| toxin | crew | lower | no | clean water -2, detox -30; spoiled food +10 | accumulated toxins |
| cabin.o2 | cabin | higher | yes | algae jar +3, canister +15 | cabin oxygen |
| cabin.co2 | cabin | lower | yes | algae jar -3, scrubber bed -20 | cabin carbon dioxide |
| cabin.heat | cabin | higher | yes | heater run +4, heat pack +6 | cabin temperature |
| cabin.pressure | cabin | higher | no | nitrogen +10, a seal patch +5 | cabin pressure retained |
| cabin.light | cabin | higher | no | lamp +2/h | light to work and grow by |
| cabin.clean | cabin | higher | no | wipe-down +5, mop +15 | floor cleanliness |
| ship.hull | ship | higher | no | patch +2, hull plate +10 | hull integrity |
| ship.shield | ship | higher | no | capacitor +5, emitter +20 | protection from radiation and debris |
| ship.thrust | ship | higher | no | fuel cell +5, thruster +20 | drive output |
| ship.course | ship | higher | no | course plot +5, star tracker +15 | heading accuracy |
| ship.grid | ship | higher | no | breaker +5, regulator +15 | power grid stability |
| ship.data | ship | higher | no | data card +5, core module +20 | computer working storage |
