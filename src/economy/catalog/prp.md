# Propulsion & Fuel — `prp`

The engine room's stock and hardware. Gases are liquefied into cryogenic fuel and oxidizer that boil off within days,
chemicals are blended into storable and hypergolic propellants, and binder, powder and prill are cast into solid
grains; the filler packs them into cartridges, tanks and mass bags that raise `ship.thrust` at the service hatch and
leave an empty canister or pouch for Stores. The machining cell and assembly bay turn metal, ceramics and electronics
into nozzles, chambers, pumps and grids, and those into whole engines and thrusters: the largest goods of the ship,
slow, and made only from many subsections' parts. Spent motor casings come back to be refilled.

## Devices

| id | device | role | cells |
|---|---|---|---|
| prp.liquefier | PX400 Cryo Liquefier | drive | 2x2 |
| prp.blender | PX220 Propellant Blender | drive | 2x2 |
| prp.caster | PX310 Grain Caster | drive | 2x2 |
| prp.filler | PX150 Cartridge Filler | drive | 2x1 |
| prp.mill | PX800 Machining Cell | drive | 3x2 |
| prp.assembly | PX900 Engine Assembly Bay | drive | 3x2 |

## Items

| id | item | use | decays |
|---|---|---|---|
| prp-001 | Cartridge, Propellant | ship.thrust +5, leaves 1 pak-006 | — |
| prp-002 | Thruster, Chemical | ship.thrust +20 | — |
| prp-003 | Hydrogen, Liquid | — | 72 h |
| prp-004 | Oxidizer, Liquid Oxygen | — | 120 h |
| prp-005 | Methane, Fuel Grade | — | — |
| prp-006 | Hydrazine | — | — |
| prp-007 | Xenon, Propellant Grade | — | — |
| prp-008 | Nozzle, Thruster | — | — |
| prp-009 | Chamber, Combustion | — | — |
| prp-010 | Tank, Propellant | — | — |
| prp-011 | Hydrogen, Slush | — | 48 h → prp-003 |
| prp-012 | Methane, Densified | — | 96 h → prp-005 |
| prp-013 | Helium, Pressurant, Liquid | — | 48 h |
| prp-014 | Ammonia, Propellant Grade | — | — |
| prp-015 | Methanol, Fuel Grade | — | — |
| prp-016 | Kerosene, Fuel Grade | — | — |
| prp-017 | Nitrogen Tetroxide | — | — |
| prp-018 | Methylhydrazine | — | — |
| prp-019 | Blend, Monoprop | — | — |
| prp-020 | Peroxide, High Test | — | 720 h |
| prp-021 | Blend, Kerolox | — | 120 h → prp-016 |
| prp-022 | Blend, Methalox | — | 120 h → prp-005 |
| prp-023 | Blend, Hydrolox | — | 72 h |
| prp-024 | Blend, Hypergolic | — | — |
| prp-025 | Blend, Rocket Fuel | — | — |
| prp-026 | Binder, Propellant | — | — |
| prp-027 | Powder, Aluminium Fuel | — | — |
| prp-028 | Prill, Oxidizer | — | — |
| prp-029 | Mix, Solid Propellant | — | — |
| prp-030 | Grain, Solid Rocket | — | — |
| prp-031 | Charge, Igniter | — | — |
| prp-032 | Grain, Hybrid Fuel | — | — |
| prp-033 | Nitrous Oxide, Oxidizer Grade | — | — |
| prp-034 | Propellant, Ionic Liquid | — | — |
| prp-035 | Stabilizer, Fuel | — | — |
| prp-036 | Blend, Monoprop, Stabilized | — | — |
| prp-037 | Tank, Xenon | ship.thrust +6, leaves 1 pak-006 | — |
| prp-038 | Canister, Argon Propellant | ship.thrust +4, leaves 1 pak-006 | — |
| prp-039 | Bag, Reaction Mass | ship.thrust +2, leaves 1 pak-002 | — |
| prp-040 | Bag, Ice Mass | ship.thrust +2, leaves 1 pak-002 | — |
| prp-041 | Bag, Water Propellant | ship.thrust +3, leaves 1 pak-002 | — |
| prp-042 | Tank, Monoprop, Hydrazine | ship.thrust +5, leaves 1 pak-006 | — |
| prp-043 | Tank, Monoprop, Peroxide | ship.thrust +4, leaves 1 pak-006 | 720 h → pak-006 |
| prp-044 | Cartridge, Methalox | ship.thrust +7, leaves 1 pak-006 | — |
| prp-045 | Cartridge, Hydrolox | ship.thrust +8, leaves 1 pak-006 | 240 h → pak-006 |
| prp-046 | Cartridge, Kerolox | ship.thrust +7, leaves 1 pak-006 | — |
| prp-047 | Cartridge, Hypergolic | ship.thrust +9, leaves 1 pak-006 | — |
| prp-048 | Cartridge, Deep Cryo | ship.thrust +10, leaves 1 pak-006 | 120 h → pak-006 |
| prp-049 | Cartridge, Electrospray | ship.thrust +5, leaves 1 pak-006 | — |
| prp-050 | Tank, Monoprop, Stabilized | ship.thrust +7, leaves 1 pak-006 | — |
| prp-051 | Cartridge, Solid Rocket | ship.thrust +7, leaves 1 pak-006 | — |
| prp-052 | Bottle, Cold Gas | ship.thrust +3, leaves 1 pak-006 | — |
| prp-053 | Bottle, Thrust, Emergency | ship.thrust +3, leaves 1 scr-004 | — |
| prp-054 | Segment, Booster | ship.thrust +6 | — |
| prp-055 | Pack, Hybrid Motor | ship.thrust +6, leaves 1 pak-006 | — |
| prp-056 | Insert, Throat | — | — |
| prp-057 | Bell, Nozzle | — | — |
| prp-058 | Extension, Nozzle | — | — |
| prp-059 | Jacket, Nozzle Cooling | — | — |
| prp-060 | Liner, Chamber | — | — |
| prp-061 | Plate, Injector | — | — |
| prp-062 | Injector, Fuel | — | — |
| prp-063 | Igniter, Engine Spark | — | — |
| prp-064 | Line, Propellant Feed | — | — |
| prp-065 | Manifold, Propellant | — | — |
| prp-066 | Impeller, Turbopump | — | — |
| prp-067 | Blade Set, Turbine | — | — |
| prp-068 | Turbopump | — | — |
| prp-069 | Valve, Propellant Check | — | — |
| prp-070 | Valve, Throttle | — | — |
| prp-071 | Dome, Tank | — | — |
| prp-072 | Barrel, Tank | — | — |
| prp-073 | Mount, Gimbal | — | — |
| prp-074 | Grid, Ion | — | — |
| prp-075 | Cathode, Hollow | — | — |
| prp-076 | Channel, Hall | — | — |
| prp-077 | Unit, Engine Control | — | — |
| prp-078 | Nozzle, Regenerative | ship.thrust +12 | — |
| prp-079 | Engine, Pressure Fed | ship.thrust +15 | — |
| prp-080 | Engine, Pump Fed | ship.thrust +20 | — |
| prp-081 | Engine, Staged Combustion | ship.thrust +30 | — |
| prp-082 | Thruster, Hall | ship.thrust +15 | — |
| prp-083 | Thruster, Ion | ship.thrust +20 | — |
| prp-084 | Thruster, Monoprop | ship.thrust +8 | — |
| prp-085 | Thruster, RCS | ship.thrust +2, ship.course +4 | — |
| prp-086 | Motor, Solid | ship.thrust +12, leaves 1 prp-087 | — |
| prp-087 | Casing, Motor, Spent | — | — |
| prp-088 | Cluster, Thruster | ship.thrust +25 | — |
| prp-089 | Seal, Liquefier Cryo | fits prp.liquefier | 600 h → scr-074 |
| prp-090 | Vane Set, Mixing | fits prp.blender | 1000 h → scr-001 |
| prp-091 | Mould, Grain Casting | fits prp.caster | 800 h → scr-001 |
| prp-092 | Nozzle, Fuel Fill | fits prp.filler | 800 h → scr-004 |
| prp-093 | Cutter Set, Mill | fits prp.mill | 400 h → scr-001 |
| prp-094 | Pin Set, Assembly Jig | fits prp.assembly | 1200 h → scr-001 |
| prp-095 | Kit, Cryo Liquefier | installs prp.liquefier | — |
| prp-096 | Kit, Propellant Blender | installs prp.blender | — |
| prp-097 | Kit, Grain Caster | installs prp.caster | — |
| prp-098 | Kit, Cartridge Filler | installs prp.filler | — |
| prp-099 | Kit, Machining Cell | installs prp.mill | — |
| prp-100 | Kit, Engine Assembly Bay | installs prp.assembly | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| fill a rocket fuel cartridge | prp.filler | 60 | 2 prp-025, 1 pak-005, 1 pwr-001 | 1 prp-001 | — |
| fill an ammonia cartridge | prp.filler | 60 | 2 prp-014, 1 pak-005, 1 pwr-001 | 1 prp-001 | — |
| pour a methanol cartridge by hand | any.bench | 90 | 2 prp-015, 1 pak-005 | 1 prp-001 | — |
| assemble a chemical thruster | prp.assembly | 200 | 1 prp-008, 1 prp-009, 1 prp-062, 1 prp-063, 1 prp-064, 1 pwr-001 | 1 prp-002 | — |
| assemble a throttled thruster | prp.assembly | 180 | 1 prp-008, 1 prp-009, 1 prp-062, 1 prp-070, 1 pwr-001 | 1 prp-002 | — |
| liquefy hydrogen | prp.liquefier | 90 | 3 gas-004, 2 pwr-001 | 3 prp-003 | — |
| decant a hydrogen canister | prp.liquefier | 60 | 1 gas-012, 1 pwr-001 | 1 prp-003, 1 pak-006 | — |
| liquefy oxygen | prp.liquefier | 80 | 3 gas-001, 2 pwr-001 | 3 prp-004 | — |
| subcool liquid oxygen | prp.liquefier | 30 | 1 gas-027, 1 pwr-001 | 1 prp-004 | — |
| liquefy methane | prp.liquefier | 80 | 3 gas-010, 1 pwr-001 | 3 prp-005 | — |
| condition liquid methane | prp.liquefier | 30 | 1 gas-029, 1 pwr-001 | 1 prp-005 | — |
| synthesise hydrazine with hypochlorite | prp.blender | 100 | 2 chm-003, 1 chm-037, 1 pwr-001 | 2 prp-006 | — |
| synthesise hydrazine with peroxide | prp.blender | 120 | 2 chm-003, 1 chm-007, 1 pwr-001 | 2 prp-006 | — |
| condense xenon propellant | prp.liquefier | 100 | 2 gas-025, 1 pwr-001 | 2 prp-007 | — |
| decant a xenon canister | prp.liquefier | 60 | 1 gas-026, 1 pwr-001 | 1 prp-007, 1 pak-006 | — |
| mill a thruster nozzle | prp.mill | 120 | 1 prp-057, 1 prp-059, 1 pwr-001 | 1 prp-008 | — |
| machine a solid nozzle | prp.mill | 150 | 1 met-027, 1 prp-056, 1 pwr-001 | 1 prp-008 | — |
| mill a combustion chamber | prp.mill | 140 | 1 prp-060, 1 met-027, 1 prp-059, 1 pwr-001 | 1 prp-009 | — |
| weld a steel combustion chamber | prp.mill | 160 | 2 met-026, 1 cer-047, 1 pwr-001 | 1 prp-009 | — |
| assemble a propellant tank | prp.assembly | 140 | 2 prp-071, 1 prp-072, 1 prp-069, 1 pwr-001 | 1 prp-010 | — |
| convert a drum into a propellant tank | prp.assembly | 120 | 1 pak-025, 1 thm-022, 1 prp-069, 1 pwr-001 | 1 prp-010 | — |
| slush hydrogen | prp.liquefier | 120 | 2 prp-003, 1 prp-013, 2 pwr-001 | 2 prp-011 | — |
| densify methane | prp.liquefier | 110 | 2 prp-005, 1 gas-028, 1 pwr-001 | 2 prp-012 | — |
| liquefy helium | prp.liquefier | 90 | 3 gas-015, 2 pwr-001 | 2 prp-013 | — |
| blend ammonia propellant | prp.blender | 50 | 2 chm-003, 1 pwr-001 | 2 prp-014 | — |
| melt ammonia ice | prp.liquefier | 60 | 2 ore-039, 1 pwr-001 | 2 prp-014 | — |
| blend methanol fuel | prp.blender | 50 | 2 chm-010, 1 pwr-001 | 2 prp-015 | — |
| melt methanol ice | prp.liquefier | 60 | 2 ore-043, 1 pwr-001 | 1 prp-015 | — |
| blend kerosene fuel | prp.blender | 80 | 2 pol-064, 1 chm-077, 1 pwr-001 | 2 prp-016 | — |
| make nitrogen tetroxide | prp.blender | 70 | 2 chm-008, 1 gas-001, 1 pwr-001 | 2 prp-017 | — |
| methylate hydrazine | prp.blender | 110 | 2 prp-006, 1 chm-010, 1 pwr-001 | 2 prp-018 | — |
| blend monoprop | prp.blender | 100 | 2 prp-006, 1 chm-019, 1 pwr-001 | 2 prp-019 | — |
| concentrate peroxide | prp.blender | 80 | 2 chm-007, 1 wat-028, 1 pwr-001 | 2 prp-020 | — |
| blend kerolox | prp.blender | 90 | 1 prp-016, 1 prp-004, 1 pwr-001 | 2 prp-021 | — |
| blend methalox | prp.blender | 90 | 1 prp-005, 1 prp-004, 1 pwr-001 | 2 prp-022 | — |
| blend hydrolox | prp.blender | 90 | 1 prp-003, 1 prp-004, 1 pwr-001 | 2 prp-023 | — |
| blend hypergolics | prp.blender | 120 | 1 prp-018, 1 prp-017, 1 pwr-001 | 2 prp-024 | — |
| blend rocket fuel | prp.blender | 120 | 1 prp-005, 1 prp-006, 1 prp-004, 1 pwr-001 | 2 prp-025 | — |
| mix propellant binder | prp.caster | 80 | 1 pol-027, 1 pol-028, 1 pwr-001 | 3 prp-026 | — |
| passivate aluminium fuel powder | prp.caster | 60 | 1 met-062, 1 pwr-001 | 2 prp-027 | — |
| prill ammonium nitrate | prp.caster | 70 | 2 chm-019, 1 pwr-001 | 3 prp-028 | — |
| prill potassium nitrate | prp.caster | 70 | 2 chm-023, 1 pwr-001 | 2 prp-028 | — |
| mix solid propellant | prp.caster | 110 | 2 prp-028, 1 prp-027, 1 prp-026, 1 pwr-001 | 2 prp-029 | — |
| cast a solid rocket grain | prp.caster | 140 | 2 prp-029, 1 pwr-001 | 1 prp-030 | — |
| press igniter charges | prp.caster | 60 | 1 prp-027, 1 chm-023, 1 ore-081, 1 pwr-001 | 3 prp-031 | — |
| cast hybrid fuel grains | prp.caster | 110 | 1 pol-067, 1 prp-027, 1 prp-026, 1 pwr-001 | 2 prp-032 | — |
| decompose nitrate into nitrous oxide | prp.blender | 70 | 1 chm-019, 1 pwr-001 | 2 prp-033 | — |
| decant a nitrous oxide canister | prp.liquefier | 40 | 1 gas-037, 1 pwr-001 | 1 prp-033, 1 pak-006 | — |
| blend ionic liquid propellant | prp.blender | 90 | 1 chm-003, 1 chm-008, 1 chm-032, 1 pwr-001 | 2 prp-034 | — |
| mix fuel stabilizer | prp.blender | 60 | 1 chm-035, 1 chm-063, 1 pwr-001 | 3 prp-035 | — |
| stabilize monoprop | prp.blender | 100 | 2 prp-019, 1 prp-035, 1 pwr-001 | 2 prp-036 | — |
| fill a xenon tank | prp.filler | 60 | 2 prp-007, 1 pak-005, 1 pwr-001 | 1 prp-037 | — |
| fill an argon propellant canister | prp.filler | 50 | 2 gas-014, 1 pak-005, 1 pwr-001 | 1 prp-038 | — |
| bag gravel reaction mass | prp.filler | 40 | 3 ore-049, 1 pak-001, 1 pwr-001 | 1 prp-039 | — |
| bag asteroid rubble by hand | any.bench | 60 | 3 ore-034, 1 pak-001, 1 met-045 | 1 prp-039 | — |
| bag dirty ice mass | prp.filler | 40 | 3 ore-012, 1 pak-001, 1 pwr-001 | 1 prp-040 | — |
| bag water propellant | prp.filler | 40 | 3 wat-009, 1 pak-001, 1 pwr-001 | 1 prp-041 | — |
| fill a hydrazine monoprop tank | prp.filler | 60 | 2 prp-006, 1 pak-005, 1 pwr-001 | 1 prp-042 | — |
| fill a peroxide monoprop tank | prp.filler | 60 | 2 prp-020, 1 pak-005, 1 pwr-001 | 1 prp-043 | — |
| fill a methalox cartridge | prp.filler | 70 | 2 prp-022, 1 pak-005, 1 pwr-001 | 1 prp-044 | — |
| fill a hydrolox cartridge | prp.filler | 70 | 2 prp-023, 1 pak-005, 1 pwr-001 | 1 prp-045 | — |
| fill a kerolox cartridge | prp.filler | 70 | 2 prp-021, 1 pak-005, 1 pwr-001 | 1 prp-046 | — |
| fill a hypergolic cartridge | prp.filler | 80 | 2 prp-024, 1 pak-005, 1 pwr-001 | 1 prp-047 | — |
| fill a deep cryo cartridge | prp.filler | 90 | 1 prp-011, 1 prp-012, 1 pak-005, 1 pwr-001 | 1 prp-048 | — |
| fill an electrospray cartridge | prp.filler | 60 | 2 prp-034, 1 pak-005, 1 pwr-001 | 1 prp-049 | — |
| fill a stabilized monoprop tank | prp.filler | 70 | 2 prp-036, 1 pak-005, 1 pwr-001 | 1 prp-050 | — |
| load a solid rocket cartridge | prp.filler | 80 | 1 prp-030, 1 prp-031, 1 pak-005, 1 pwr-001 | 1 prp-051 | — |
| fill a cold gas bottle | prp.filler | 40 | 2 gas-003, 1 pak-005, 1 pwr-001 | 1 prp-052 | — |
| bottle compressed air for thrust | any.bench | 30 | 1 gas-069, 1 pak-005 | 1 prp-052 | — |
| rig an emergency thrust bottle | any.bench | 60 | 1 prp-008, 1 prp-042 | 1 prp-053 | — |
| cast a booster segment | prp.caster | 150 | 2 prp-029, 1 cer-071, 1 prp-031, 1 pwr-001 | 1 prp-054 | — |
| pack a hybrid motor | prp.caster | 130 | 1 prp-032, 1 prp-033, 1 pak-005, 1 pwr-001 | 1 prp-055 | — |
| grind throat inserts | prp.mill | 70 | 1 cer-040, 1 pwr-001 | 2 prp-056 | — |
| spin a nozzle bell | prp.mill | 90 | 1 met-034, 1 prp-056, 1 pwr-001 | 1 prp-057 | — |
| lay up a nozzle extension | prp.mill | 100 | 1 cer-041, 1 met-035, 1 pwr-001 | 1 prp-058 | — |
| braze a nozzle cooling jacket | prp.mill | 100 | 2 met-053, 1 met-037, 1 pwr-001 | 1 prp-059 | — |
| line a combustion chamber | prp.mill | 90 | 1 cer-047, 1 met-037, 1 pwr-001 | 1 prp-060 | — |
| drill an injector plate | prp.mill | 100 | 1 met-026, 1 pwr-001 | 1 prp-061 | — |
| build a fuel injector | prp.mill | 120 | 1 prp-061, 1 mec-034, 1 pwr-001 | 1 prp-062 | — |
| build engine spark igniters | prp.assembly | 60 | 1 ecp-063, 1 cer-035, 1 met-006, 1 pwr-001 | 2 prp-063 | — |
| bend propellant feed lines | prp.mill | 60 | 2 met-056, 1 mec-013, 1 pwr-001 | 2 prp-064 | — |
| weld a propellant manifold | prp.mill | 100 | 2 prp-064, 1 met-073, 1 pwr-001 | 1 prp-065 | — |
| mill a turbopump impeller | prp.mill | 100 | 1 met-027, 1 pwr-001 | 1 prp-066 | — |
| mill a turbine blade set | prp.mill | 100 | 1 met-025, 1 pwr-001 | 1 prp-067 | — |
| assemble a turbopump | prp.assembly | 160 | 1 prp-066, 1 prp-067, 1 met-072, 1 mec-029, 1 pwr-001 | 1 prp-068 | — |
| machine propellant check valves | prp.mill | 60 | 1 mec-033, 1 met-049, 1 pwr-001 | 2 prp-069 | — |
| build a throttle valve | prp.assembly | 120 | 1 mec-034, 1 mec-035, 1 lgt-046, 1 pwr-001 | 1 prp-070 | — |
| spin a tank dome | prp.mill | 100 | 1 met-038, 1 pwr-001 | 1 prp-071 | — |
| wrap a tank barrel | prp.mill | 100 | 1 met-038, 1 cer-062, 1 pwr-001 | 1 prp-072 | — |
| build a gimbal mount | prp.assembly | 120 | 2 mec-004, 1 mec-043, 1 met-050, 1 pwr-001 | 1 prp-073 | — |
| cut a carbon ion grid | prp.mill | 150 | 1 cer-060, 1 pol-025, 1 pwr-001 | 1 prp-074 | — |
| machine hollow cathodes | prp.mill | 90 | 1 met-050, 1 chm-076, 1 pwr-001 | 2 prp-075 | — |
| machine a hall channel | prp.mill | 100 | 1 cer-038, 1 pwr-001 | 1 prp-076 | — |
| build an engine control unit | prp.assembly | 180 | 1 ecp-010, 1 lgt-009, 1 pwr-016, 1 pwr-001 | 1 prp-077 | — |
| assemble a regenerative nozzle | prp.assembly | 180 | 1 prp-008, 1 prp-058, 1 prp-059, 1 pwr-001 | 1 prp-078 | — |
| assemble a pressure fed engine | prp.assembly | 200 | 1 prp-002, 1 prp-010, 1 prp-065, 1 pwr-001 | 1 prp-079 | — |
| assemble a pump fed engine | prp.assembly | 240 | 1 prp-002, 1 prp-068, 1 prp-065, 1 prp-077, 1 pwr-001 | 1 prp-080 | — |
| assemble a staged combustion engine | prp.assembly | 360 | 1 prp-080, 1 prp-068, 1 prp-078, 1 prp-073, 1 pwr-001 | 1 prp-081 | — |
| assemble a hall thruster | prp.assembly | 180 | 1 prp-076, 1 shd-005, 1 prp-075, 1 ecp-045, 1 pwr-001 | 1 prp-082 | — |
| assemble an ion thruster | prp.assembly | 240 | 2 prp-074, 1 prp-075, 1 prp-077, 1 ecp-045, 1 pwr-001 | 1 prp-083 | — |
| assemble a monoprop thruster | prp.assembly | 130 | 1 prp-008, 1 chm-077, 1 mec-034, 1 pwr-001 | 1 prp-084 | — |
| assemble rcs thrusters | prp.assembly | 120 | 1 prp-056, 1 mec-034, 1 prp-069, 1 pwr-001 | 2 prp-085 | — |
| cast a solid motor | prp.caster | 150 | 1 prp-030, 1 prp-008, 1 cer-071, 1 pwr-001 | 1 prp-086 | — |
| reload a spent motor casing | prp.caster | 120 | 1 prp-087, 1 prp-030, 1 prp-031, 1 pwr-001 | 1 prp-086 | — |
| scrap a spent motor casing | any.bench | 30 | 1 prp-087 | 1 scr-001 | — |
| cluster thrusters | prp.assembly | 300 | 3 prp-002, 1 prp-073, 1 prp-077, 1 prp-010, 1 pwr-001 | 1 prp-088 | — |
| cut a liquefier cryo seal | any.bench | 60 | 1 pol-057, 1 met-049 | 1 prp-089 | — |
| cut a mixing vane set | any.bench | 60 | 1 met-034, 1 mec-006 | 1 prp-090 | — |
| make a grain casting mould | any.bench | 90 | 1 met-055, 1 pol-074 | 1 prp-091 | — |
| fit a fuel fill nozzle | any.bench | 60 | 1 met-051, 1 mec-007 | 1 prp-092 | — |
| grind a mill cutter set | any.bench | 90 | 1 met-030, 1 cer-039 | 1 prp-093 | — |
| turn an assembly jig pin set | any.bench | 60 | 1 met-008, 1 mec-018 | 1 prp-094 | — |
| assemble a cryo liquefier kit | any.bench | 180 | 2 fur-001, 1 prp-089, 1 mec-042, 1 thm-055 | 1 prp-095 | — |
| assemble a propellant blender kit | any.bench | 150 | 1 fur-001, 1 prp-090, 1 mec-010, 1 pak-025 | 1 prp-096 | — |
| assemble a grain caster kit | any.bench | 150 | 1 fur-001, 1 prp-091, 1 mec-043 | 1 prp-097 | — |
| assemble a cartridge filler kit | any.bench | 120 | 1 fur-001, 1 prp-092, 1 mec-040 | 1 prp-098 | — |
| assemble a machining cell kit | any.bench | 200 | 2 fur-001, 1 prp-093, 1 mec-010, 1 ecp-046 | 1 prp-099 | — |
| assemble an engine assembly bay kit | any.bench | 200 | 2 fur-001, 1 prp-094, 1 mec-043, 1 mec-012 | 1 prp-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| prp.liquefier | Plant that liquefies hydrogen, oxygen, methane, helium and xenon, melts volatile ices and decants canisters. | CRYOGENIC. FACE SHIELD AND GLOVES BEYOND THIS LINE. |
| prp.blender | Blender that mixes fuels, oxidizers, hypergolics, monopropellants and the drive's ready blends. | Spills are charged by volume and by cleanup hour. Ref 4402/P. |
| prp.caster | Caster that forms solid propellant into grains, boosters, igniters and solid motors, and reloads spent casings. | Pour, cure, inspect, sign. Unsigned grains are not issued. Proc 77. |
| prp.filler | Filling station that charges cartridges, tanks, bottles and mass bags with propellant for the service hatch. | Fill weight verified. Scale last certified some time ago. |
| prp.mill | Machining cell for nozzles, chambers, injectors, pump parts, valves, tank shells and ion thruster parts. | EYE PROTECTION REQUIRED. LOOSE SLEEVES PROHIBITED. |
| prp.assembly | Bay that assembles thrusters, engines, turbopumps, tanks and engine controllers. | Every engine aboard was bolted together here. The plaque names the Company. |
| prp-001 | Filled canister of fuel that raises the ship's thrust and leaves an empty canister. | Empty canisters are returned to Stores. Unreturned canisters are billed. |
| prp-002 | Thruster of nozzle, chamber and injector that raises thrust strongly and forms the base of engines. | EXHAUST HAZARD. KEEP CLEAR OF NOZZLE PLANE. |
| prp-003 | Cryogenic fuel that boils off quickly, used in hydrolox, slush hydrogen and rocket fuel. | Transfer within the hour. Boil-off is logged as operator loss. Proc 19. |
| prp-004 | Cryogenic oxidizer for kerolox, methalox, hydrolox and rocket fuel; boils off. | OXIDIZER. NO GREASE. NO OIL. NO EXCEPTIONS. |
| prp-005 | Liquefied methane, a fuel that keeps, used in methalox and rocket fuel. | Purity sampled at fill. Sample bottle reused. |
| prp-006 | Storable fuel for monoprop tanks, and the base of hypergolics and rocket fuel. | TOXIC. CARCINOGEN. FULL SUIT REQUIRED. |
| prp-007 | Condensed xenon that fills xenon tanks. | Xenon is a controlled stock. Every gram is reconciled monthly. |
| prp-008 | Milled nozzle for thrusters, solid motors and emergency thrust bottles. | Throat bore within tolerance. Exit lip dented. Accepted. |
| prp-009 | Chamber in which propellant burns inside a thruster. | PRESSURE VESSEL. DO NOT WELD WITHOUT AUTHORITY. |
| prp-010 | Tank for pressure fed engines and thruster clusters. | Proof test before first fill. Form 52T, signed and witnessed. |
| prp-011 | Half-frozen hydrogen for deep cryo cartridges; warms back into liquid hydrogen. | Stir it and it melts. Leave it and it melts. |
| prp-012 | Supercooled methane for deep cryo cartridges; warms back into fuel-grade methane. | Density checked at fill. Reading falls hourly. As designed. |
| prp-013 | Liquid helium that chills hydrogen into slush; boils away fast. | COLDEST STOCK ABOARD. NO BARE SKIN CONTACT. |
| prp-014 | Simple storable propellant for cartridges. | The smell outlasts the shift. The cartridge does not. |
| prp-015 | Methanol for cartridges filled by hand. | POISON. NOT FOR CONSUMPTION. FLAME INVISIBLE IN LIGHT. |
| prp-016 | Storable fuel blended with liquid oxygen into kerolox. | Kerosene is legacy stock. Legacy stock is not reordered. |
| prp-017 | Storable oxidizer for hypergolic blends. | ORANGE VAPOUR INDICATES LEAK. EVACUATE AND REPORT. |
| prp-018 | Hydrazine-derived fuel for hypergolic blends. | Drum resealed after sampling. Seal integrity assumed. |
| prp-019 | Hydrazine monopropellant, stabilized before it goes into tanks. | Do not store unstabilized beyond one shift. Proc 66 refers. |
| prp-020 | Concentrated hydrogen peroxide for monoprop tanks; slowly breaks down. | OXIDIZER. CLEAN TOOLS ONLY. ORGANICS PROHIBITED. |
| prp-021 | Kerosene and liquid oxygen ready for cartridges; the oxygen boils off, leaving kerosene. | Blends are filled on the shift they are mixed. Carryover is waste. |
| prp-022 | Methane and liquid oxygen ready for cartridges; the oxygen boils off, leaving methane. | Boils off by the hour. Fill first, paperwork after. |
| prp-023 | Hydrogen and liquid oxygen ready for cartridges; boils off entirely. | Mixed 0600. Gone by 0900. Logged as transferred. |
| prp-024 | Self-igniting blend for hypergolic cartridges. | IGNITES ON CONTACT. KEEP COMPONENTS SEGREGATED. |
| prp-025 | Mixed fuel and oxidizer blend for propellant cartridges. | Blend ratios are set by the depot. Station adjustments are not recognised. |
| prp-026 | Rubbery binder for solid propellant and hybrid fuel grains. | Viscosity checked by stirring stick. Stick retained as reference. |
| prp-027 | Passivated aluminium powder for solid propellant, igniters and hybrid grains. | COMBUSTIBLE DUST. NO SPARKS. NO SWEEPING. |
| prp-028 | Nitrate prill for solid propellant. | Prill is weighed in and weighed out. The difference is investigated. |
| prp-029 | Mixed solid propellant, cast into grains and booster segments. | Cast within pot life. Expired mix is burned off under Proc 203. |
| prp-030 | Cast grain for solid rocket cartridges and solid motors. | Radiographed for voids. Two found. Within allowance of three. |
| prp-031 | Small charge that lights solid motors, cartridges and boosters. | EXPLOSIVE. STORE APART FROM GRAINS. |
| prp-032 | Wax fuel grain burned with nitrous oxide in a hybrid motor. | Candle wax with a work order. |
| prp-033 | Oxidizer for hybrid motors, also decanted from gas canisters. | Recreational use is a breach of contract. Ref 3307/N. |
| prp-034 | Salt-based ionic liquid for electrospray cartridges. | Conductivity in range. Container labelled twice. Labels disagree. |
| prp-035 | Additive that keeps monopropellant from breaking down. | One measure per drum. Measures are issued, not improvised. Proc 58. |
| prp-036 | Monopropellant treated to keep, for stabilized monoprop tanks. | Stabilized stock may be held for audit inspection at any time. |
| prp-037 | Canister of xenon that raises thrust. | XENON. HIGH VALUE. SIGN OUT REQUIRED. |
| prp-038 | Canister of argon that adds a little thrust. | Argon is the economy option. The Company prefers the economy option. |
| prp-039 | Pouch of gravel expelled for thrust; leaves an empty pouch. | Gravel out the back. Physics accepts the cheapest mass available. |
| prp-040 | Pouch of dirty ice spent as reaction mass; leaves an empty pouch. | KEEP FROZEN UNTIL EXPELLED. |
| prp-041 | Pouch of process water spent as reaction mass; leaves an empty pouch. | Water expelled as propellant is not available for drinking. Notice 11. |
| prp-042 | Tank of hydrazine that raises thrust, and part of an emergency thrust bottle. | HYDRAZINE. VENT OUTBOARD ONLY. |
| prp-043 | Peroxide tank that raises thrust but breaks down to an empty canister on the shelf. | Fill date stamped on lid. Lid swapped. Date unknown. |
| prp-044 | Cartridge of methalox for thrust. | Methalox is the standard issue cartridge. Standard issue is not a compliment. |
| prp-045 | Hydrolox cartridge with strong thrust that boils off to an empty canister on the shelf. | Deliver to the hatch on the shift filled. Proc 24. |
| prp-046 | Cartridge of kerolox for thrust. | Old fuel, old design, still in the catalogue. Like most of the crew. |
| prp-047 | Hypergolic cartridge with strong thrust that keeps. | SELF IGNITING. NO IGNITER REQUIRED. NO MISTAKES PERMITTED. |
| prp-048 | Strongest cartridge, of slush hydrogen and densified methane, but it warms off quickly. | Deep cryo stock is not to be held. Holding is charged at boil-off rate. |
| prp-049 | Cartridge of ionic liquid propellant for thrust. | Emitter needles inspected under loupe. Loupe cracked. |
| prp-050 | Stabilized monoprop tank for good thrust that keeps. | SHELF STABLE. ROTATE STOCK ANYWAY. |
| prp-051 | Solid grain and igniter in a canister, for thrust. | Arm only at the hatch. Arming elsewhere is reported on Form 13S. |
| prp-052 | Bottle of nitrogen or air that adds a little thrust. | Barely a push. Enough to log a delta. |
| prp-053 | Hydrazine tank fitted with a nozzle, rigged for thrust in an emergency; leaves broken parts. | Improvised devices are not approved. Their thrust is nonetheless recorded. |
| prp-054 | Cast solid booster segment for thrust. | SEGMENT. ORIENT ARROW TOWARD NOZZLE. |
| prp-055 | Wax fuel grain and nitrous oxide in a canister, for thrust. | Valve leak check passed. Faint smell noted. Smell passed. |
| prp-056 | Ceramic insert for nozzle throats, nozzle bells and RCS thrusters. | Insert erosion is normal wear. Normal wear is the station's cost. |
| prp-057 | Spun bell that shapes the exhaust of a thruster nozzle. | DO NOT STRIKE. CONTOUR CRITICAL. |
| prp-058 | Composite extension for regenerative nozzles. | Adds length to the nozzle and a line to the requisition. |
| prp-059 | Brazed jacket that cools nozzles and combustion chambers. | Braze joints leak tested. One joint weeps. Within allowance. |
| prp-060 | Ceramic liner for combustion chambers. | Inspect liner after every tenth firing. Proc 102. Cracks are photographed. |
| prp-061 | Drilled plate built into a fuel injector. | Hole count per plate is audited. Missing holes are a production deduction. |
| prp-062 | Injector that sprays propellant into a thruster's combustion chamber. | PRECISION ORIFICES. DO NOT CLEAR WITH WIRE. |
| prp-063 | Spark igniter for chemical thrusters. | Spark gap set. Spark observed. Operator startled. Noted. |
| prp-064 | Bent pipe that carries propellant, welded into manifolds. | NO KINKS. MINIMUM BEND RADIUS STAMPED ON PIPE. |
| prp-065 | Manifold that feeds pressure fed and pump fed engines. | Pressure test each branch separately. Proc 81. Record every reading, even the bad ones. |
| prp-066 | Milled impeller for turbopumps. | Impellers are balanced to depot standard. Field balancing is not recognised. |
| prp-067 | Turbine blades that drive a turbopump. | Blades counted, weighed, matched. Spare blade missing from set. |
| prp-068 | Pump that drives propellant into the large engines. | ROTATING MACHINERY. LOCK OUT BEFORE SERVICE. |
| prp-069 | One-way valve for propellant tanks and RCS thrusters. | One way only. Like the contract. |
| prp-070 | Metered valve for throttled thrusters. | Stroke calibrated. Stiff at mid travel. Lubricated. Still stiff. |
| prp-071 | Spun dome that closes a propellant tank. | PRESSURE BOUNDARY. NO DRILLING. |
| prp-072 | Wrapped barrel section for propellant tanks. | Wrap tension is recorded per metre. Records support warranty claims. None are honoured. |
| prp-073 | Swivel mount for staged combustion engines and thruster clusters. | Range of motion verified to stops. Stops replaced. Not reverified. |
| prp-074 | Carbon grid that accelerates ions in an ion thruster. | HIGH VOLTAGE GRID. DO NOT TOUCH. DO NOT BREATHE ON. |
| prp-075 | Cathode for hall and ion thrusters. | Cathode life is guaranteed to the hour stated. The hour is not stated. |
| prp-076 | Ceramic channel for the hall thruster. | Erosion measured at exit. Erosion within forecast. Forecast optimistic. |
| prp-077 | Electronic controller for pump fed engines, ion thrusters and thruster clusters. | Do not override. Override requests are filed on Form 90X and declined. |
| prp-078 | Cooled, extended nozzle that raises thrust and is used in staged combustion engines. | Runs fuel through its own walls to survive. Familiar method. |
| prp-079 | Simple engine fed by tank pressure, for strong thrust. | Approved for service. Approval is not an endorsement. |
| prp-080 | Turbopump-fed engine with strong thrust, and the base of a staged combustion engine. | ENGINE. COF PROPERTY. SN 0811 4402. |
| prp-081 | Staged, gimballed engine giving the most thrust of any single part. | Hot fire passed. Bay ceiling repainted. Second coat pending. |
| prp-082 | Electric thruster that drives ions through a magnetic channel. | Quiet. Patient. Arrives on a timescale the contract does not cover. |
| prp-083 | Electric thruster with ion grids, for strong, steady thrust. | Ion propulsion is efficient. Efficiency is the Company's only stated value. |
| prp-084 | Catalyst thruster for monopropellant. | CATALYST BED. PREHEAT BEFORE FIRING. |
| prp-085 | Small attitude thruster that adds to both thrust and heading. | Pulse test, 50 firings. 49 confirmed. One presumed. |
| prp-086 | Cast solid motor for thrust; leaves a spent casing to reload. | ONCE IGNITED CANNOT BE SHUT DOWN. |
| prp-087 | Empty solid motor casing, reloaded at the grain caster or scrapped. | Casings are reloaded up to their rated count. The count is scratched on the case. |
| prp-088 | Several thrusters on one gimbal mount and tank, for the most thrust of all. | All units fire together or none fire. Proc 300. Partial firing is a fault. |
| prp-089 | Spare cryo seal for the cryo liquefier; wears into rubber scrap. | Seal hardened at cold. Replaced warm. Will harden again. |
| prp-090 | Spare mixing vane set for the propellant blender. | SHARP EDGES. NOT FOR STIRRING BY HAND. |
| prp-091 | Spare casting mould for the grain caster. | Moulds are numbered. Grains cast in an unnumbered mould are rejected. |
| prp-092 | Spare fill nozzle for the cartridge filler. | Drips after shutoff. Every one of them drips. |
| prp-093 | Spare cutter set for the machining cell; wears quickly. | Change cutters at first chatter. Log the change. Proc 93. |
| prp-094 | Spare pin set for the engine assembly bay jig. | Pins gauged go and no go. Three went where they should not. |
| prp-095 | Packed kit that installs a cryo liquefier. | UNPACK AT ROOM TEMPERATURE. SURFACES COLD AFTER COMMISSIONING. |
| prp-096 | Packed kit that installs a propellant blender. | Smoking is prohibited aboard. This notice is attached for completeness. |
| prp-097 | Packed kit that installs a grain caster. | Moulds packed separately. Separate crate not located. |
| prp-098 | Packed kit that installs a cartridge filler. | Commission with water before propellant. Proc 12. Drain the water after. |
| prp-099 | Packed kit that installs a machining cell. | Heavy, sharp, precise. Two out of three are the operator's problem. |
| prp-100 | Packed kit that installs an engine assembly bay. | Engine output credited to the station is subject to Company adjustment. |
