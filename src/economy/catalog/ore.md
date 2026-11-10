# Ores, Ice & Regolith — `ore`

Everything the mine takes raw from the regolith stores, the tethered asteroids and the ice around the ship: regolith,
metal ores, industrial minerals, water ice and the frosts of volatiles. The drill, scoop, tether and cryo trap bring
them in; the crusher grinds them, the separator floats ores into concentrates and the leach vat dissolves what floats
badly. Concentrates go to the foundry (`met`), sand, clay and ground minerals to glass and ceramics (`cer`), salts,
sulfur and brine to the chem lab (`chm`), phosphate and potash to the farm (`soi`), and ice to water and air. Ice and
frost do not keep: left out they melt into raw water or sublime into gas. Tailings, residue and spent liquor go on to
recycling and the chem lab.

## Devices

| id | device | role | cells |
|---|---|---|---|
| ore.drill | XM200 Mining Drill | mine | 2x2 |
| ore.scoop | XM15 Regolith Scoop | mine | 2x1 |
| ore.tether | XM900 Asteroid Tether | mine | 3x2 |
| ore.coldtrap | XM40 Cryo Trap | mine | 2x1 |
| ore.crusher | XM55 Jaw Crusher | mine | 2x2 |
| ore.separator | XM60 Flotation Separator | mine | 2x2 |
| ore.leacher | XM70 Leach Vat | mine | 2x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| ore-001 | Regolith | — | — |
| ore-002 | Ice, Water | — | 48 h → wat-002 |
| ore-003 | Ore, Iron | — | — |
| ore-004 | Ore, Copper | — | — |
| ore-005 | Sand, Silica | — | — |
| ore-006 | Bauxite | — | — |
| ore-007 | Rock, Carbon | — | — |
| ore-008 | Crust, Sulfur | — | — |
| ore-009 | Clay | — | — |
| ore-010 | Limestone | — | — |
| ore-011 | Ice, Brine | — | 72 h → ore-048 |
| ore-012 | Ice, Dirty | — | 72 h → wat-002 |
| ore-013 | Ore, Lead | — | — |
| ore-014 | Ore, Tin | — | — |
| ore-015 | Ore, Nickel | — | — |
| ore-016 | Ore, Zinc | — | — |
| ore-017 | Ilmenite | — | — |
| ore-018 | Chromite | — | — |
| ore-019 | Ore, Cobalt | — | — |
| ore-020 | Nodules, Manganese | — | — |
| ore-021 | Magnesite | — | — |
| ore-022 | Spodumene | — | — |
| ore-023 | Ore, Rare Earth | — | — |
| ore-024 | Ore, Uranium | — | — |
| ore-025 | Salt, Rock | — | — |
| ore-026 | Gypsum | — | — |
| ore-027 | Rock, Phosphate | — | — |
| ore-028 | Ore, Potash | — | — |
| ore-029 | Quartz, Crystal | — | — |
| ore-030 | Feldspar | — | — |
| ore-031 | Graphite, Flake | — | — |
| ore-032 | Schist, Mica | — | — |
| ore-033 | Gem Cluster, Raw | — | — |
| ore-034 | Rubble, Asteroid | — | — |
| ore-035 | Dust, Comet | — | — |
| ore-036 | Ice, Dry | — | 24 h → gas-002 |
| ore-037 | Frost, Oxygen | — | 12 h → gas-001 |
| ore-038 | Frost, Nitrogen | — | 24 h |
| ore-039 | Ice, Ammonia | — | 72 h → chm-003 |
| ore-040 | Ice, Methane | — | 24 h |
| ore-041 | Ice, Carbon Monoxide | — | 24 h |
| ore-042 | Frost, Sulfur Dioxide | — | 72 h |
| ore-043 | Ice, Methanol | — | 96 h → chm-010 |
| ore-044 | Frost, Argon | — | 24 h |
| ore-045 | Frost, Xenon | — | 48 h |
| ore-046 | Slush, Hydrogen | — | 12 h |
| ore-047 | Helium3, Trace | — | 240 h → gas-015 |
| ore-048 | Brine, Mineral | — | — |
| ore-049 | Gravel, Crushed | — | — |
| ore-050 | Sand, Fine | — | — |
| ore-051 | Regolith, Fines | — | — |
| ore-052 | Limestone, Crushed | — | — |
| ore-053 | Concentrate, Iron | — | — |
| ore-054 | Concentrate, Copper | — | — |
| ore-055 | Concentrate, Lead | — | — |
| ore-056 | Concentrate, Tin | — | — |
| ore-057 | Concentrate, Zinc | — | — |
| ore-058 | Concentrate, Nickel | — | — |
| ore-059 | Concentrate, Titanium | — | — |
| ore-060 | Concentrate, Chromite | — | — |
| ore-061 | Concentrate, Cobalt | — | — |
| ore-062 | Concentrate, Manganese | — | — |
| ore-063 | Concentrate, Rare Earth | — | — |
| ore-064 | Yellowcake | — | — |
| ore-065 | Brine, Lithium | — | — |
| ore-066 | Bauxite, Ground | — | — |
| ore-067 | Magnesite, Ground | — | — |
| ore-068 | Quartz, Ground | — | — |
| ore-069 | Feldspar, Ground | — | — |
| ore-070 | Phosphate, Ground | — | — |
| ore-071 | Potash, Ground | — | — |
| ore-072 | Gypsum, Ground | — | — |
| ore-073 | Salt, Rock, Ground | — | — |
| ore-074 | Graphite, Powder | — | — |
| ore-075 | Clay, Pulverised | — | — |
| ore-076 | Mica, Flake | — | — |
| ore-077 | Rubble, Sorted | — | — |
| ore-078 | Gems, Sorted | — | — |
| ore-079 | Blank, Gem | — | — |
| ore-080 | Sulfur, Refined | — | — |
| ore-081 | Briquette, Carbon | — | — |
| ore-082 | Grit, Abrasive | — | — |
| ore-083 | Tailings, Mine | — | — |
| ore-084 | Residue, Leach | — | — |
| ore-085 | Liquor, Leach, Spent | — | — |
| ore-086 | Drill Bit, Worn | — | — |
| ore-087 | Drill Bit, Mining | fits ore.drill | 240 h → ore-086 |
| ore-088 | Blade, Regolith Scoop | fits ore.scoop | 400 h → scr-004 |
| ore-089 | Cable Spool, Tether | fits ore.tether | 600 h → scr-004 |
| ore-090 | Plate, Cryo Trap | fits ore.coldtrap | 600 h → scr-004 |
| ore-091 | Jaw Plate, Crusher | fits ore.crusher | 300 h → scr-004 |
| ore-092 | Impeller, Flotation | fits ore.separator | 400 h → scr-004 |
| ore-093 | Liner, Leach Vat | fits ore.leacher | 400 h → scr-002 |
| ore-094 | Kit, Mining Drill | installs ore.drill | — |
| ore-095 | Kit, Regolith Scoop | installs ore.scoop | — |
| ore-096 | Kit, Asteroid Tether | installs ore.tether | — |
| ore-097 | Kit, Cryo Trap | installs ore.coldtrap | — |
| ore-098 | Kit, Jaw Crusher | installs ore.crusher | — |
| ore-099 | Kit, Flotation Separator | installs ore.separator | — |
| ore-100 | Kit, Leach Vat | installs ore.leacher | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| dig regolith by hand | crew | 60 | — | 1 ore-001 | fitness +2 |
| chip hull ice by hand | crew | 60 | — | 1 ore-002 | fitness +2 |
| scoop regolith | ore.scoop | 90 | 1 pwr-001 | 4 ore-001 | — |
| scoop sand and clay | ore.scoop | 90 | 1 pwr-001 | 3 ore-005, 1 ore-009 | — |
| scoop comet ice | ore.scoop | 120 | 1 pwr-001 | 3 ore-012, 1 ore-035 | — |
| core water ice | ore.drill | 120 | 1 pwr-001 | 3 ore-002 | — |
| core brine ice | ore.drill | 120 | 1 pwr-001 | 2 ore-011 | — |
| drill iron seam | ore.drill | 180 | 1 pwr-001 | 3 ore-003, 1 ore-007 | — |
| drill copper seam | ore.drill | 180 | 1 pwr-001 | 2 ore-004, 1 ore-008 | — |
| drill bauxite bed | ore.drill | 180 | 1 pwr-001 | 3 ore-006, 1 ore-009 | — |
| drill limestone bed | ore.drill | 150 | 1 pwr-001 | 3 ore-010, 1 ore-026 | — |
| drill lead and zinc seam | ore.drill | 180 | 1 pwr-001 | 2 ore-013, 2 ore-016 | — |
| drill tin seam | ore.drill | 180 | 1 pwr-001 | 2 ore-014, 1 ore-029 | — |
| drill nickel seam | ore.drill | 180 | 1 pwr-001 | 2 ore-015, 1 ore-019 | — |
| drill evaporite bed | ore.drill | 150 | 1 pwr-001 | 2 ore-025, 1 ore-028, 1 ore-021 | — |
| drill phosphate bed | ore.drill | 150 | 1 pwr-001 | 2 ore-027, 1 ore-026 | — |
| drill pegmatite | ore.drill | 180 | 1 pwr-001 | 2 ore-030, 1 ore-032, 1 ore-022 | — |
| drill graphite seam | ore.drill | 180 | 1 pwr-001 | 2 ore-031, 1 ore-007 | — |
| tow a metal asteroid | ore.tether | 360 | 2 pwr-001 | 2 ore-034, 1 ore-017, 1 ore-018 | — |
| tow a rare asteroid | ore.tether | 480 | 2 pwr-001 | 1 ore-023, 1 ore-024, 1 ore-033 | — |
| sweep manganese nodules | ore.tether | 360 | 2 pwr-001 | 3 ore-020, 1 ore-019 | — |
| trap carbon frosts | ore.coldtrap | 180 | 1 pwr-001 | 2 ore-036, 1 ore-041 | — |
| trap air frosts | ore.coldtrap | 180 | 1 pwr-001 | 2 ore-038, 1 ore-037 | — |
| trap ammonia and methane | ore.coldtrap | 180 | 1 pwr-001 | 2 ore-039, 2 ore-040 | — |
| trap sulfur and methanol frost | ore.coldtrap | 180 | 1 pwr-001 | 1 ore-042, 2 ore-043 | — |
| trap noble frosts | ore.coldtrap | 240 | 1 pwr-001 | 2 ore-044, 1 ore-045 | — |
| trap hydrogen slush | ore.coldtrap | 240 | 2 pwr-001 | 2 ore-046 | — |
| bake regolith volatiles | ore.coldtrap | 240 | 4 ore-001, 2 pwr-001 | 1 ore-047, 2 ore-051 | — |
| melt brine ice | ore.leacher | 60 | 2 ore-011, 1 pwr-001 | 2 ore-048 | — |
| evaporate brine | ore.leacher | 120 | 3 ore-048, 1 pwr-001 | 1 ore-025, 1 wat-002 | — |
| crush regolith | ore.crusher | 30 | 3 ore-001, 1 pwr-001 | 2 ore-049, 1 ore-051 | — |
| grind silica sand | ore.crusher | 30 | 2 ore-005, 1 pwr-001 | 2 ore-050 | — |
| grind gravel to sand | ore.crusher | 30 | 2 ore-049, 1 pwr-001 | 1 ore-050 | — |
| crush limestone | ore.crusher | 30 | 2 ore-010, 1 pwr-001 | 2 ore-052 | — |
| sift comet dust | ore.separator | 45 | 3 ore-035, 1 pwr-001 | 2 ore-051, 1 ore-074 | — |
| sort asteroid rubble | ore.separator | 60 | 3 ore-034, 1 pwr-001 | 1 ore-077, 1 ore-003, 1 ore-083 | — |
| crush sorted rubble | ore.crusher | 45 | 2 ore-077, 1 pwr-001 | 1 ore-053, 1 ore-058 | — |
| pull iron from regolith fines | ore.separator | 60 | 3 ore-051, 1 pwr-001 | 1 ore-053, 1 ore-083 | — |
| float iron | ore.separator | 60 | 3 ore-003, 1 wat-002, 1 pwr-001 | 2 ore-053, 1 ore-083 | — |
| float copper | ore.separator | 60 | 3 ore-004, 1 wat-002, 1 pwr-001 | 2 ore-054, 1 ore-083 | — |
| float lead | ore.separator | 60 | 3 ore-013, 1 wat-002, 1 pwr-001 | 2 ore-055, 1 ore-083 | — |
| float tin | ore.separator | 60 | 3 ore-014, 1 wat-002, 1 pwr-001 | 2 ore-056, 1 ore-083 | — |
| float zinc | ore.separator | 60 | 3 ore-016, 1 wat-002, 1 pwr-001 | 2 ore-057, 1 ore-083 | — |
| float nickel | ore.separator | 60 | 3 ore-015, 1 wat-002, 1 pwr-001 | 2 ore-058, 1 ore-083 | — |
| float ilmenite | ore.separator | 90 | 3 ore-017, 1 wat-002, 1 pwr-001 | 2 ore-059, 1 ore-083 | — |
| float chromite | ore.separator | 60 | 3 ore-018, 1 wat-002, 1 pwr-001 | 2 ore-060, 1 ore-083 | — |
| float cobalt | ore.separator | 90 | 3 ore-019, 1 wat-002, 1 pwr-001 | 1 ore-061, 1 ore-083 | — |
| float manganese | ore.separator | 60 | 3 ore-020, 1 wat-002, 1 pwr-001 | 2 ore-062, 1 ore-083 | — |
| leach rare earths | ore.leacher | 120 | 3 ore-023, 1 chm-009, 1 pwr-001 | 1 ore-063, 1 ore-084, 1 ore-085 | — |
| leach uranium | ore.leacher | 120 | 3 ore-024, 1 chm-001, 1 pwr-001 | 1 ore-064, 1 ore-084, 1 ore-085 | — |
| leach lithium | ore.leacher | 90 | 3 ore-022, 1 chm-001, 1 pwr-001 | 2 ore-065, 1 ore-084 | — |
| refine sulfur | ore.leacher | 60 | 3 ore-008, 1 pwr-001 | 2 ore-080, 1 ore-084 | — |
| grind bauxite | ore.crusher | 40 | 2 ore-006, 1 pwr-001 | 2 ore-066 | — |
| grind magnesite | ore.crusher | 40 | 2 ore-021, 1 pwr-001 | 2 ore-067 | — |
| grind quartz | ore.crusher | 40 | 2 ore-029, 1 pwr-001 | 2 ore-068 | — |
| grind feldspar | ore.crusher | 40 | 2 ore-030, 1 pwr-001 | 2 ore-069 | — |
| grind phosphate | ore.crusher | 40 | 2 ore-027, 1 pwr-001 | 2 ore-070 | — |
| grind potash | ore.crusher | 40 | 2 ore-028, 1 pwr-001 | 2 ore-071 | — |
| grind gypsum | ore.crusher | 40 | 2 ore-026, 1 pwr-001 | 2 ore-072 | — |
| grind rock salt | ore.crusher | 40 | 2 ore-025, 1 pwr-001 | 2 ore-073 | — |
| grind graphite | ore.crusher | 40 | 2 ore-031, 1 pwr-001 | 2 ore-074 | — |
| pulverise clay | ore.crusher | 30 | 2 ore-009, 1 pwr-001 | 2 ore-075 | — |
| split mica schist | ore.crusher | 40 | 2 ore-032, 1 pwr-001 | 2 ore-076, 1 ore-083 | — |
| press carbon briquettes | ore.crusher | 60 | 3 ore-007, 1 pwr-001 | 2 ore-081 | — |
| grind abrasive grit | ore.crusher | 40 | 2 ore-068, 1 ore-007, 1 pwr-001 | 2 ore-082 | — |
| sort raw gems | ore.separator | 60 | 2 ore-033, 1 pwr-001 | 1 ore-078, 1 ore-083 | — |
| saw gem blanks | ore.crusher | 90 | 1 ore-078, 1 ore-082, 1 pwr-001 | 2 ore-079 | — |
| regrind a drill bit | ore.crusher | 60 | 1 ore-086, 1 ore-079, 1 pwr-001 | 1 ore-087 | — |
| make a drill bit | any.bench | 60 | 1 met-030, 1 ore-079 | 1 ore-087 | — |
| make a scoop blade | any.bench | 45 | 1 met-005, 1 mec-001 | 1 ore-088 | — |
| wind a tether cable spool | any.bench | 90 | 1 cer-059, 1 cer-064 | 1 ore-089 | — |
| braze a cold trap plate | any.bench | 60 | 1 met-037, 1 met-053, 1 met-079 | 1 ore-090 | — |
| cast a crusher jaw plate | any.bench | 60 | 1 met-030, 1 met-019 | 1 ore-091 | — |
| fit a flotation impeller | any.bench | 45 | 1 mec-022, 1 pol-003 | 1 ore-092 | — |
| weld a leach vat liner | any.bench | 45 | 2 pol-035 | 1 ore-093 | — |
| assemble a mining drill | any.bench | 240 | 1 ore-087, 1 met-074, 1 mec-010, 2 met-067, 1 pwr-016 | 1 ore-094 | — |
| assemble a regolith scoop | any.bench | 180 | 1 ore-088, 1 met-074, 1 mec-010 | 1 ore-095 | — |
| assemble an asteroid tether | any.bench | 240 | 1 ore-089, 1 met-074, 1 mec-012, 2 met-078 | 1 ore-096 | — |
| assemble a cryo trap | any.bench | 180 | 1 ore-090, 1 cer-055, 1 cer-066, 1 mec-042 | 1 ore-097 | — |
| assemble a jaw crusher | any.bench | 180 | 1 ore-091, 1 met-074, 2 met-071, 2 cer-044, 1 mec-010 | 1 ore-098 | — |
| assemble a flotation separator | any.bench | 180 | 1 ore-092, 1 cer-022, 1 mec-008, 1 met-054 | 1 ore-099 | — |
| assemble a leach vat | any.bench | 150 | 1 ore-093, 1 mec-008, 1 mec-007 | 1 ore-100 | — |
| draw helium3 off the cold trap | ore.coldtrap | 30 | 3 ore-047, 1 pwr-001 | 3 gas-015 | — |

## Codex

| id | about | flavour |
|---|---|---|
| ore.drill | Cores ice and drills ore seams and mineral beds out of the regolith stores; the main extraction unit. | Mind the bit. The bit does not mind the operator. |
| ore.scoop | Scoops loose regolith, sand, clay and comet ice; the cheapest way to fill the mine bins. | A shovel with a power bill. Bill forwarded to the station. |
| ore.tether | Snares passing asteroids and nodule swarms and tows them in for rare ores, rubble and gems. | Capture events are logged against the ship's mass budget. Unlogged rocks remain unlogged. Ref 9001/T. |
| ore.coldtrap | Freezes volatile frosts and ices out of the cold outside and bakes helium traces out of regolith. | CRYOGENIC SURFACE. NO BARE SKIN CONTACT. |
| ore.crusher | Crushes and grinds rock, ore and minerals into gravel, sand and powders; also regrinds drill bits and saws gems. | Feed it rocks. Keep it from fingers. In that order. |
| ore.separator | Floats metal ores in water into concentrates, sorts rubble and gems and sifts dust, leaving tailings. | FROTH IS PROFIT. SKIM GENTLY. |
| ore.leacher | Dissolves rare earths, uranium and lithium out of ore with acid, melts and boils brine, and refines sulfur. | Acid exposure is covered under Clause 17 once per contract. Make it count. |
| ore-001 | Loose grey rock and dust from the regolith stores; crushed, melted to glass, baked for water or mixed into soil. | There is always more regolith. That is the problem with regolith. |
| ore-002 | Frozen water cored from the ice field or chipped off the hull; melts into raw water if left out. | Hull ice removal requires a permit. Permits are issued after removal, by custom. |
| ore-003 | Rust-red rock from an iron seam, floated into concentrate or smelted crudely straight to iron. | The ship's skeleton, still in the rock. |
| ore-004 | Green-streaked rock from a copper seam, floated into concentrate for the foundry. | Every cable on this deck started out like this. |
| ore-005 | Pale scooped sand for glass batch, ground finer or set into aerogel. | Never enough in the bin. Always enough in the boots. |
| ore-006 | Reddish clay rock, ground for aluminium, alumina, alum and refractory brick. | Grade C bauxite. Grades A and B were not available at launch. |
| ore-007 | Black carbon-bearing rock used as smelting fuel and reducer and as stock for briquettes, carbon black and activated carbon. | Burns slow, stains everything. Do not complain about it near the foundry. |
| ore-008 | Yellow sulfur-laced crust from copper seams, refined in the leach vat into pure sulfur. | Odour is a known property of the material and not grounds for a complaint. Notice 88. |
| ore-009 | Fine sticky earth for ceramic slip, pots, putty and grow pebbles, or ground dry in the jaw crusher. | Used for figurines. Also for sealing, by engineers who call it something else. |
| ore-010 | Pale sedimentary rock, crushed for flux and glass batch or burnt to quicklime. | The furnace's quiet partner. |
| ore-011 | Salty ice cored from the brine layers; melts into mineral brine if left out. | Licked once. Only once. |
| ore-012 | Comet ice full of grit, melted for raw water or bagged as reaction mass for the drive. | Mostly water. Remainder unclassified. Filter per Proc 21 before any use. |
| ore-013 | Heavy grey ore from lead and zinc seams, floated into lead concentrate. | TOXIC DUST. WASH HANDS BEFORE EATING. |
| ore-014 | Dark tin-bearing rock, floated into concentrate for solder, bronze and tinplate. | No tin, no solder. No solder, no anything. |
| ore-015 | Greenish ore found with cobalt, floated into nickel concentrate for stainless steel and cells. | Bright, once it stops being a rock. |
| ore-016 | Pale ore found beside lead, floated into concentrate for brass, galvanising and cells. | Zinc keeps steel from rotting. Steel does not say thank you either. |
| ore-017 | Black titanium mineral towed in on metal asteroids, floated into titanium concentrate. | Looks like coal. Valued like a hull plate. Inventoried like both. |
| ore-018 | Dark chromium mineral towed in on metal asteroids, floated into concentrate for stainless steel and pigment. | Stainless starts here. Nothing about it is stainless yet. |
| ore-019 | Scarce ore from nickel seams and nodule fields, floated into cobalt concentrate. | Yield shortfalls must be explained on Form 33Y within one shift. |
| ore-020 | Lumpy nodules swept up by the asteroid tether, floated into concentrate or roasted for manganese dioxide. | Known on deck as space potatoes. Not edible. Notice repeated for a reason. |
| ore-021 | White mineral from evaporite beds, ground for magnesium metal and salts. | Chalky on the fingers. Fierce in the furnace. |
| ore-022 | Pale lithium mineral from pegmatite, leached with acid into lithium brine. | Every charged cell aboard started in this rock. |
| ore-023 | Scarce ore from rare asteroids, leached into concentrate for magnets, optics and catalysts. | STRATEGIC MATERIAL. WEIGH IN, WEIGH OUT. |
| ore-024 | Mildly radioactive ore from rare asteroids, leached into yellowcake for reactor fuel. | STORE AWAY FROM BUNKS. AND FOOD. |
| ore-025 | Salt crystals from evaporite beds and boiled brine, ground for the chem lab, dishwashers and lamps. | Salt rations unaffected by mine output. Ref 1201/N. |
| ore-026 | Soft white mineral found with limestone and phosphate, ground for plaster, soil and porous ceramic. | Soft enough to scratch with a fingernail. Somebody always checks. |
| ore-027 | Grey rock rich in phosphorus, ground for phosphoric acid and fertilizer. | Tomatoes, pending. |
| ore-028 | Pinkish salt ore from evaporite beds, ground for potassium chemicals and fertilizer. | Priority allocation to the farm under Schedule 6. The chem lab disputes Schedule 6. |
| ore-029 | Clear crystal found with tin, ground for silica or grown into quartz wafers. | Retention of specimens for personal display is not permitted. Proc 77. |
| ore-030 | Pinkish mineral from pegmatite, ground for slip, enamel and porcelain. | Porcelain's backbone. |
| ore-031 | Soft black mineral from graphite seams, ground to powder, wrapped into pencils or fired into crucibles. | Writes on everything. Including the operator. |
| ore-032 | Glittering layered rock from pegmatite, split into mica flakes. | Glitters under the work lamp. Glitter has no assigned value. |
| ore-033 | Crystal-studded rock from rare asteroids, sorted for gems that become cutting blanks. | Industrial use only. Not jewellery. Inventory checks are unannounced. |
| ore-034 | Broken metal-rich rock towed in by the asteroid tether, sorted for ore or bagged as reaction mass. | Rocks caught. Rocks kept. |
| ore-035 | Fine dark dust scooped with comet ice, outgassed, baked for water or sifted for fines and graphite. | Older than the ship, older than the sun. Ends up in the sieve. |
| ore-036 | Frozen carbon dioxide from the cryo trap; sublimes quickly into gas if left out. | SUBLIMES TO CARBON DIOXIDE. DO NOT STORE IN CABIN. |
| ore-037 | Pale blue frozen oxygen separated for cabin air; boils off into oxygen quickly. | The bluest thing aboard. And the shortest-lived. |
| ore-038 | Frozen nitrogen, sublimed into gas; boils away and is lost if left out. | Keep cold or write off. Write-offs on Form 9N. |
| ore-039 | Frozen ammonia, melted for propellant work; thaws into ammonia if left out. | The eyes report it before the sensor does. |
| ore-040 | Frozen methane, sublimed into gas; vanishes if left out. | FLAMMABLE. NO OPEN FLAME WITHIN THE BAY. |
| ore-041 | Frozen carbon monoxide, sublimed into gas; boils away and is lost if left out. | No smell, no colour, no second chances. |
| ore-042 | Frozen sulfur dioxide, absorbed into sulfuric acid or made into sodium sulfite; boils away if left out. | Acid on ice. |
| ore-043 | Frozen methanol, melted for propellant; thaws into methanol if left out. | NOT A DRINK. NOT ON ANY OCCASION. |
| ore-044 | Frozen argon, sublimed into inert gas; boils away and is lost if left out. | Does nothing. That is the point. |
| ore-045 | Scarce frozen xenon, sublimed into gas; boils away and is lost if left out. | Losses of xenon exceeding tolerance are deducted from the station bonus. There is no bonus. |
| ore-046 | Barely frozen hydrogen, sublimed into gas; boils off very fast if left out. | Already gone. |
| ore-047 | Trace of helium baked out of regolith and drawn off the cryo trap; keeps a long while. | A bin of regolith for a breath of it. Ratio approved by Engineering, rev 2. |
| ore-048 | Salty water melted from brine ice, electrolysed, boiled for salt or blown for iodine. | Seawater from a sea nobody aboard has seen. |
| ore-049 | Crushed regolith, ground to sand, spun into basalt fibre, cast into tiles or bagged as reaction mass. | The ship's universal filler. |
| ore-050 | Sand ground fine for glass batch, casting moulds, flux, filters and water glass. | Gets into the bearings, the bread and the bunks. |
| ore-051 | Powdery dust from crushing regolith, fired into bricks and tiles, melted to glass or worked for iron. | RESPIRATORY HAZARD. MASK BEFORE SWEEPING. |
| ore-052 | Crushed limestone for smelting flux, glass batch, quicklime, soda and chalk. | Chalk for the board, flux for the furnace. Same bucket. |
| ore-053 | Iron ore floated rich, smelted into iron or roasted to red oxide pigment. | Rust with a work order. |
| ore-054 | Copper ore floated rich, smelted into copper or leached into copper sulfate. | Wire, eventually. |
| ore-055 | Lead ore floated rich, smelted into lead or roasted to lead oxide. | Heavy work, heavy bucket. Lead exposure log on Form 82B. |
| ore-056 | Tin ore floated rich, ready for the smelting furnace. | Solder, first draft. |
| ore-057 | Zinc ore floated rich, smelted into zinc or roasted to zinc oxide. | Assay passed, rev 1. Assayer's sample not returned. |
| ore-058 | Nickel ore floated rich, smelted into nickel or leached into nickel sulfate. | Stainless, eventually. |
| ore-059 | Ilmenite floated rich, smelted to titanium or made into titanium white pigment. | Hull brace or a coat of paint. Allocation decided above station level. |
| ore-060 | Chromite floated rich, reduced to chromium or fired into chrome yellow. | Shine and yellow paint from the same black sand. |
| ore-061 | Cobalt ore floated rich, smelted to cobalt or roasted to cobalt oxide. | Small yield. Every grain weighed. Weights reported weekly. |
| ore-062 | Manganese floated rich, smelted to ferromanganese or electrolysed into manganese dioxide. | Makes steel springy and cells lively. |
| ore-063 | Rare earths leached out with acid, calcined to rare earth oxide. | Allocation by Company priority list. List revised without notice. |
| ore-064 | Uranium oxide leached from ore, enriched in the reactor bay for fuel. | RADIOACTIVE. NOT FOOD. DRUM SEAL MUST BE INTACT. |
| ore-065 | Lithium-rich liquor from leached spodumene, made into lithium carbonate or hydroxide. | Batteries in a bucket. |
| ore-066 | Bauxite ground fine for aluminium, alumina, alum and refractory brick. | Red dust on every glove in the foundry. |
| ore-067 | Magnesite ground fine for magnesium metal, salts, grip chalk and soil. | Diversion to grip chalk is approved at low priority. Smelting takes precedence. |
| ore-068 | Quartz ground fine for fused silica, polysilicon, silicon carbide and abrasive grit. | Every chip aboard started as this dust. |
| ore-069 | Feldspar ground fine for ceramic slip, enamel and porcelain insulators. | Fired, it rings when tapped. |
| ore-070 | Phosphate ground fine for phosphoric acid and farm fertilizer. | Bread, two steps removed. |
| ore-071 | Potash ground fine for caustic potash, potassium salts, alum and fertilizer. | Plants eat it. The lab eats it. Nobody else should. |
| ore-072 | Gypsum ground fine for porous ceramic, plaster casts and soil. | Casts for broken arms. Pots for broken plants. |
| ore-073 | Rock salt ground fine for the electrolysis cell, soda, chlorate and salt cake. | Half the chem lab starts with a scoop of this. |
| ore-074 | Fine black graphite for electrodes, moderator blocks, carbon fibre, motor brushes and pencils. | Slippery, smudged, inside every machine aboard. |
| ore-075 | Clay ground dry for slip, refractory brick, kiln wash, casting moulds and modelling clay. | Add water. Add patience. Patience not stocked. |
| ore-076 | Thin heat-resistant sheets split from schist, laid into insulating tape or expanded into vermiculite. | Held to the lamp, the deck turns amber. |
| ore-077 | Metal-rich selection of asteroid rubble, crushed into iron and nickel concentrate. | The good rocks. |
| ore-078 | Gem crystals picked from raw clusters, sawn into gem blanks. | Count verified by two operators. Station has one. Count verified twice. |
| ore-079 | Sawn gem for the cutting edges of drill bits and extruder dies. | Cutting stock. Ornamental use is misappropriation. Policy 19. |
| ore-080 | Pure yellow sulfur for acids, thiosulfate, rubber curing and lubricants. | Rubber cures, acid gets made, everyone holds their breath. |
| ore-081 | Pressed carbon block that fuels and reduces nearly every smelt and makes electrodes and polysilicon. | No briquettes, no foundry. |
| ore-082 | Hard grit from quartz and carbon for grinding wheels, polishing, and sawing gems and wafers. | Polishes anything. Fingerprints included. |
| ore-083 | Waste rock left after separating ore, fired with clay into regolith brick. | Nothing aboard is waste. Some things are pending reassignment. |
| ore-084 | Spent solids from the leach vat, roasted down to tailings. | CHEMICAL RESIDUE. DOUBLE GLOVE. |
| ore-085 | Used acid liquor from leaching, neutralised with lime in the chem lab. | Neutralise before disposal. No exceptions. Proc 140. |
| ore-086 | Drill bit blunted by use, reground with a gem blank. | Not scrap. Tired. |
| ore-087 | Gem-tipped tool steel bit, the wearing part of the mining drill; wears into a worn bit. | Bit changed, rev 12. Hours logged. Hours disputed. |
| ore-088 | Steel edge for the regolith scoop; a spare part that wears into broken parts. | Every edge goes dull. Carry a spare. |
| ore-089 | Basalt and aramid line for the asteroid tether; a spare part that wears into broken parts. | If the cable sings, let go. |
| ore-090 | Brazed copper plate for the cryo trap; a spare part that wears into broken parts. | Frost grows on it like moss on a stone. |
| ore-091 | Hardened steel jaw for the jaw crusher; a spare part that wears into broken parts. | Bites rocks for a living. |
| ore-092 | Rotating paddle for the flotation separator; a spare part that wears into broken parts. | ROTATING PART. SLEEVES CLEAR. |
| ore-093 | Plastic lining for the leach vat; a spare part that wears into plastic scrap. | The only thing between acid and deck. Inspect each shift. Proc 141. |
| ore-094 | Kit of parts that installs a mining drill. | Some assembly required. Most assembly, in practice. |
| ore-095 | Kit of parts that installs a regolith scoop. | First tool of every new mine. Issued last, by policy. |
| ore-096 | Kit of parts that installs an asteroid tether. | Fishing gear for rocks. |
| ore-097 | Kit of parts that installs a cryo trap. | UNPACK IN COLD BAY ONLY. |
| ore-098 | Kit of parts that installs a jaw crusher. | Bolt it down, then bolt it down again. Torque values on Sheet 4. |
| ore-099 | Kit of parts that installs a flotation separator. | Bubbles not included. |
| ore-100 | Kit of parts that installs a leach vat. | Read the acid card before unboxing. Acknowledge on Form 5A. |
