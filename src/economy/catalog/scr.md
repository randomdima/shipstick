# Salvage & Recycling — `scr`

Where the ship's worn and broken things come back as feedstock. Scrap metal, plastic scrap, e-waste, broken parts and
fabric scraps — left by every subsection's spent goods, or hauled in from hull and wreck by the salvage claw — are
sorted, shredded, stripped, baled, melted and drawn into regrind, pellets, filament, ingots, reclaimed copper and
precious metal, cullet and fibre. The reclaimed goods go to `met`, `pol`, `cer`, `fib` and `ecp` as cheaper inputs; the
salvaged motors, bearings and fasteners go to whoever mends a device. Left unsorted, some scrap turns worse: batteries
leak, iron rusts, rags rot.

## Devices

| id | device | role | cells |
|---|---|---|---|
| scr.salvager | SV900 Salvage Claw | sanit | 3x2 |
| scr.sorter | SV210 Sorting Table | sanit | 2x2 |
| scr.shredder | SV330 Plastic Shredder | sanit | 2x1 |
| scr.stripper | SV140 Wire Stripper | sanit | 2x1 |
| scr.baler | SV450 Scrap Baler | sanit | 2x1 |
| scr.furnace | SV620 Scrap Furnace | smelt | 2x2 |
| scr.extruder | SV180 Filament Extruder | smelt | 2x1 |
| scr.glassmill | SV270 Cullet Mill | smelt | 2x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| scr-001 | Scrap, Metal | — | — |
| scr-002 | Scrap, Plastic | — | — |
| scr-003 | Scrap, Electronic | — | — |
| scr-004 | Parts, Broken | — | — |
| scr-005 | Scrap, Fabric | — | 1440 h → scr-076 |
| scr-006 | Regrind, Plastic | — | — |
| scr-007 | Ingot, Scrap | — | — |
| scr-008 | Copper, Reclaimed | — | — |
| scr-009 | Filament, Recycled | — | — |
| scr-010 | Cullet, Glass, Recycled | — | — |
| scr-011 | Pellets, Plastic, Recycled | — | — |
| scr-012 | Fibre, Shoddy | — | — |
| scr-013 | Refuse, Mixed | — | — |
| scr-014 | Battery, Spent | — | 720 h → scr-015 |
| scr-015 | Battery, Leaking | — | — |
| scr-016 | Flakes, Hull | — | — |
| scr-017 | Shards, Glass | — | — |
| scr-018 | Tangle, Wire | — | — |
| scr-019 | Scrap, Cable | — | — |
| scr-020 | Offcuts, Foam | — | — |
| scr-021 | Jar, Bolt | — | — |
| scr-022 | Scrap, Ferrous | — | 2000 h → scr-024 |
| scr-023 | Scrap, Non-Ferrous | — | — |
| scr-024 | Scrap, Rusted | — | — |
| scr-025 | Plastic, Contaminated | — | — |
| scr-026 | Flakes, Plastic, Washed | — | — |
| scr-027 | Plastic, Shredded | — | — |
| scr-028 | Aluminium, Reclaimed | — | — |
| scr-029 | Iron, Reclaimed | — | — |
| scr-030 | Steel, Reclaimed | — | — |
| scr-031 | Solder, Reclaimed | — | — |
| scr-032 | Brass, Reclaimed | — | — |
| scr-033 | Wire, Copper, Stripped | — | — |
| scr-034 | Shreds, Wire Insulation | — | — |
| scr-035 | Scrap, Circuit Board | — | — |
| scr-036 | Scrap, Electronic, Shredded | — | — |
| scr-037 | Connectors, Salvaged | — | — |
| scr-038 | Chips, Salvaged | — | — |
| scr-039 | Capacitors, Salvaged | — | — |
| scr-040 | Displays, Salvaged | — | — |
| scr-041 | Black Mass, Battery | — | — |
| scr-042 | Concentrate, Precious Metal | — | — |
| scr-043 | Precious Metal, Reclaimed | — | — |
| scr-044 | Motor, Salvaged | — | — |
| scr-045 | Bearing, Salvaged | — | — |
| scr-046 | Fasteners, Salvaged | — | — |
| scr-047 | Gears, Salvaged | — | — |
| scr-048 | Valve, Salvaged | — | — |
| scr-049 | Cell, Solar, Salvaged | — | — |
| scr-050 | Powder, Cullet | — | — |
| scr-051 | Beads, Glass, Cullet | — | — |
| scr-052 | Rod, Glass, Fused | — | — |
| scr-053 | Bundle, Glass Fibre | — | — |
| scr-054 | Grit, Abrasive, Reclaimed | — | — |
| scr-055 | Sheet, Plastic, Recycled | — | — |
| scr-056 | Rod, Plastic, Recycled | — | — |
| scr-057 | Tubing, Recycled | — | — |
| scr-058 | Film, Bag, Recycled | — | — |
| scr-059 | Spool, Filament, Recycled | — | — |
| scr-060 | Crumb, Foam, Salvaged | — | — |
| scr-061 | Fill, Insulating Foam | — | — |
| scr-062 | Rod, Steel, Scrap | — | — |
| scr-063 | Plate, Steel, Scrap | — | — |
| scr-064 | Bale, Scrap, Compacted | — | — |
| scr-065 | Bale, Plastic | — | — |
| scr-066 | Bale, Textile | — | — |
| scr-067 | Block, Ballast | — | — |
| scr-068 | Dross, Furnace | — | — |
| scr-069 | Slag, Furnace | — | — |
| scr-070 | Strips, Rag, Torn | — | — |
| scr-071 | Rope, Rag | — | — |
| scr-072 | Rug, Rag | stress -1/h | 600 h → scr-005 |
| scr-073 | Mat, Floor, Felt | cabin.clean +1/h | 720 h → scr-005 |
| scr-074 | Scrap, Rubber | — | — |
| scr-075 | Rubber, Devulcanised | — | — |
| scr-076 | Rags, Rotten | — | — |
| scr-077 | Jaw, Salvage Claw | fits scr.salvager, leaves 1 scr-001 | — |
| scr-078 | Cable, Salvage Claw | fits scr.salvager, leaves 1 scr-001 | — |
| scr-079 | Belt, Sorter | fits scr.sorter, leaves 1 scr-074 | — |
| scr-080 | Drum, Sorter Magnet | fits scr.sorter, leaves 1 scr-004 | — |
| scr-081 | Blade Set, Shredder | fits scr.shredder, leaves 1 scr-001 | — |
| scr-082 | Screen, Shredder | fits scr.shredder, leaves 1 scr-001 | — |
| scr-083 | Die, Stripper | fits scr.stripper, leaves 1 scr-001 | — |
| scr-084 | Roller, Stripper Feed | fits scr.stripper, leaves 1 scr-074 | — |
| scr-085 | Seal, Baler Ram | fits scr.baler, leaves 1 scr-074 | — |
| scr-086 | Platen, Baler | fits scr.baler, leaves 1 scr-001 | — |
| scr-087 | Liner, Furnace | fits scr.furnace, leaves 1 cer-086 | — |
| scr-088 | Crucible, Furnace | fits scr.furnace, leaves 1 cer-086 | — |
| scr-089 | Nozzle, Extruder | fits scr.extruder, leaves 1 scr-001 | — |
| scr-090 | Screw, Filament Extruder | fits scr.extruder, leaves 1 scr-001 | — |
| scr-091 | Roller, Cullet Mill | fits scr.glassmill, leaves 1 scr-001 | — |
| scr-092 | Sieve, Cullet Mill | fits scr.glassmill, leaves 1 scr-001 | — |
| scr-093 | Kit, Salvage Claw | installs scr.salvager | — |
| scr-094 | Kit, Sorting Table | installs scr.sorter | — |
| scr-095 | Kit, Plastic Shredder | installs scr.shredder | — |
| scr-096 | Kit, Wire Stripper | installs scr.stripper | — |
| scr-097 | Kit, Scrap Baler | installs scr.baler | — |
| scr-098 | Kit, Scrap Furnace | installs scr.furnace | — |
| scr-099 | Kit, Filament Extruder | installs scr.extruder | — |
| scr-100 | Kit, Cullet Mill | installs scr.glassmill | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| salvage hull scrap | scr.salvager | 240 | 1 pwr-001 | 2 scr-001, 1 scr-016 | — |
| salvage wreck debris | scr.salvager | 360 | 2 pwr-001 | 1 scr-004, 1 scr-003, 1 scr-018, 1 scr-019 | — |
| comb the debris field | scr.salvager | 300 | 1 pwr-001 | 1 scr-017, 1 scr-020, 1 scr-021, 1 scr-002 | — |
| gather mixed refuse | crew | 15 | — | 1 scr-013 | cabin.clean +3 |
| sort mixed refuse | scr.sorter | 30 | 4 scr-013, 1 pwr-001 | 1 scr-001, 1 scr-002, 1 scr-005, 1 scr-025 | — |
| sort refuse by hand | crew | 45 | 3 scr-013 | 1 scr-002, 1 scr-004 | — |
| sort scrap metal | scr.sorter | 30 | 4 scr-001, 1 pwr-001 | 2 scr-022, 2 scr-023 | — |
| sort scrap with a magnet by hand | any.bench | 60 | 3 scr-001 | 1 scr-022, 1 scr-023 | — |
| tear down broken parts | scr.sorter | 45 | 3 scr-004, 1 pwr-001 | 1 scr-045, 1 scr-046, 1 scr-022, 1 scr-002 | — |
| strip motors from broken parts | scr.sorter | 60 | 4 scr-004, 1 pwr-001 | 1 scr-044, 1 scr-047, 1 scr-023 | — |
| pull valves from broken parts | scr.sorter | 45 | 3 scr-004, 1 pwr-001 | 1 scr-048, 1 scr-074, 1 scr-022 | — |
| tear down parts by hand | any.bench | 60 | 2 scr-004 | 1 scr-046, 1 scr-001 | — |
| tear down worn pumps | scr.sorter | 45 | 2 mec-077, 1 pwr-001 | 1 scr-048, 1 scr-022, 1 scr-074 | — |
| sort worn bearings | scr.sorter | 20 | 3 mec-078 | 1 scr-045, 1 scr-022 | — |
| strip a burnt out motor | scr.stripper | 45 | 1 mec-080, 1 pwr-001 | 1 scr-033, 1 scr-022 | — |
| shred worn drive belts | scr.shredder | 30 | 3 mec-079, 1 pwr-001 | 2 scr-074 | — |
| collect rubber offcuts | scr.sorter | 15 | 3 pol-085 | 2 scr-074 | — |
| sort the bolt jar | scr.sorter | 20 | 2 scr-021 | 3 scr-046 | — |
| sort e-waste | scr.sorter | 45 | 3 scr-003, 1 pwr-001 | 1 scr-035, 1 scr-014, 1 scr-040, 1 scr-019 | — |
| take apart e-waste by hand | any.bench | 60 | 2 scr-003 | 1 scr-035, 1 scr-019 | — |
| sort faulty computers | scr.sorter | 45 | 2 ecp-083 | 2 scr-035, 1 scr-040, 1 scr-044 | — |
| pull chips from faulty boards | scr.stripper | 45 | 2 ecp-082, 1 pwr-001 | 2 scr-038, 1 scr-039, 1 scr-037 | — |
| desolder board scrap | scr.stripper | 60 | 3 scr-035, 1 pwr-001 | 2 scr-038, 1 scr-039, 1 scr-037, 1 scr-031 | — |
| shred board scrap | scr.shredder | 45 | 3 scr-035, 1 pwr-001 | 3 scr-036 | — |
| smelt shredded e-waste | scr.furnace | 120 | 4 scr-036, 2 pwr-001 | 1 scr-042, 2 scr-008, 1 scr-068 | — |
| refine precious metal | scr.furnace | 120 | 2 scr-042, 1 chm-008, 1 pwr-001 | 1 scr-043, 1 chm-082 | — |
| collect dead cells | scr.sorter | 15 | 3 pwr-004 | 1 scr-014 | — |
| collect spent battery packs | scr.sorter | 20 | 1 pwr-007 | 2 scr-014 | — |
| smelt a flat lead acid battery | scr.furnace | 90 | 1 pwr-025, 1 pwr-001 | 1 met-012, 1 chm-082 | — |
| crush spent batteries | scr.shredder | 60 | 3 scr-014, 1 pwr-001 | 2 scr-041, 1 scr-023, 1 scr-002 | — |
| neutralise leaking batteries | scr.shredder | 60 | 2 scr-015, 1 chm-012, 1 pwr-001 | 1 scr-041, 1 scr-023 | cabin.clean +3 |
| leach battery black mass | scr.furnace | 120 | 3 scr-041, 1 chm-001, 1 pwr-001 | 1 chm-014, 1 chm-074, 1 chm-082 | — |
| strip a wire tangle | scr.stripper | 30 | 2 scr-018, 1 pwr-001 | 2 scr-033, 1 scr-034 | — |
| strip cable scrap | scr.stripper | 45 | 2 scr-019, 1 pwr-001 | 2 scr-033, 2 scr-034 | — |
| strip scrap power cable | scr.stripper | 45 | 2 pwr-050, 1 pwr-001 | 2 scr-033, 1 scr-034 | — |
| strip wire by hand | any.bench | 60 | 2 scr-019 | 1 scr-033, 1 scr-034 | — |
| shred cable insulation | scr.shredder | 30 | 3 scr-034, 1 pwr-001 | 2 scr-027 | — |
| melt stripped copper | scr.furnace | 60 | 3 scr-033, 1 pwr-001 | 2 scr-008 | — |
| melt scrap metal | scr.furnace | 90 | 4 scr-001, 1 pwr-001 | 2 scr-007, 1 scr-069 | — |
| melt ferrous scrap | scr.furnace | 90 | 3 scr-022, 1 pwr-001 | 2 scr-029, 1 scr-069 | — |
| melt rusted scrap | scr.furnace | 120 | 4 scr-024, 1 ore-081, 2 pwr-001 | 2 scr-029, 1 scr-069 | — |
| wire brush rusted scrap | any.bench | 60 | 3 scr-024 | 2 scr-022, 1 met-081 | — |
| blast rusted scrap with grit | scr.sorter | 30 | 3 scr-024, 1 scr-054, 1 pwr-001 | 3 scr-022 | — |
| melt hull flakes | scr.furnace | 90 | 4 scr-016, 1 pwr-001 | 2 scr-028, 1 scr-068 | — |
| melt non-ferrous scrap | scr.furnace | 90 | 3 scr-023, 1 pwr-001 | 1 scr-028, 1 scr-008, 1 scr-068 | — |
| alloy reclaimed steel | scr.furnace | 90 | 2 scr-029, 1 scr-007, 1 ore-081, 1 pwr-001 | 2 scr-030 | — |
| refine scrap ingots into steel | scr.furnace | 90 | 3 scr-007, 1 ore-081, 1 pwr-001 | 2 scr-030 | — |
| alloy reclaimed brass | scr.furnace | 60 | 2 scr-008, 1 met-015, 1 pwr-001 | 2 scr-032 | — |
| recover solder from dross | scr.furnace | 45 | 2 ecp-085, 1 pwr-001 | 2 scr-031 | — |
| cast reclaimed iron ingots | scr.furnace | 60 | 2 scr-029, 1 pwr-001 | 2 met-001 | — |
| cast reclaimed aluminium ingots | scr.furnace | 60 | 2 scr-028, 1 pwr-001 | 2 met-004 | — |
| cast reclaimed steel ingots | scr.furnace | 60 | 2 scr-030, 1 pwr-001 | 2 met-002 | — |
| cast reclaimed brass ingots | scr.furnace | 60 | 2 scr-032, 1 pwr-001 | 2 met-022 | — |
| draw reclaimed solder wire | scr.extruder | 30 | 1 scr-031, 1 pwr-001 | 2 ecp-017 | — |
| draw bond wire from precious metal | scr.extruder | 45 | 1 scr-043, 1 pwr-001 | 4 ecp-027 | — |
| roll scrap plate | scr.furnace | 90 | 2 scr-030, 1 pwr-001 | 2 scr-063 | — |
| draw scrap steel rod | scr.furnace | 90 | 2 scr-030, 1 pwr-001 | 3 scr-062 | — |
| reclaim aluminium from dross | scr.furnace | 90 | 3 scr-068, 1 pwr-001 | 1 scr-028, 1 scr-069 | — |
| reclaim aluminium from foundry dross | scr.furnace | 90 | 3 met-082, 1 pwr-001 | 1 scr-028, 1 scr-068 | — |
| crush furnace slag | scr.glassmill | 60 | 3 scr-069, 1 pwr-001 | 2 scr-054 | — |
| crush incinerator clinker | scr.glassmill | 60 | 3 san-067, 1 pwr-001 | 2 scr-054 | — |
| bale scrap metal | scr.baler | 30 | 4 scr-001, 1 pwr-001 | 1 scr-064 | — |
| bale plastic scrap | scr.baler | 30 | 4 scr-002, 1 pwr-001 | 1 scr-065 | — |
| bale fabric scraps | scr.baler | 30 | 4 scr-005, 1 pwr-001 | 1 scr-066 | — |
| melt a scrap bale | scr.furnace | 120 | 1 scr-064, 2 pwr-001 | 3 scr-007, 1 scr-069 | — |
| cast a ballast block | scr.furnace | 60 | 1 scr-064, 1 pwr-001 | 1 scr-067 | — |
| remelt a ballast block | scr.furnace | 90 | 1 scr-067, 1 pwr-001 | 2 scr-007 | — |
| shred a plastic bale | scr.shredder | 60 | 1 scr-065, 1 pwr-001 | 4 scr-027 | — |
| open a textile bale | scr.shredder | 60 | 1 scr-066, 1 pwr-001 | 4 scr-012 | — |
| wash and flake plastic | scr.shredder | 45 | 3 scr-002, 1 wat-002, 1 pwr-001 | 3 scr-026, 1 san-001 | — |
| wash contaminated plastic | scr.shredder | 60 | 3 scr-025, 2 wat-002, 1 cln-005, 1 pwr-001 | 2 scr-026, 2 san-016 | — |
| shred plastic scrap | scr.shredder | 30 | 3 scr-002, 1 pwr-001 | 3 scr-027 | — |
| cut plastic scrap by hand | any.bench | 45 | 2 scr-002 | 2 scr-027 | — |
| shred a cracked toilet seat | scr.shredder | 20 | 1 toi-069, 1 pwr-001 | 2 scr-027 | — |
| grind shredded plastic | scr.shredder | 30 | 3 scr-027, 1 pwr-001 | 3 scr-006 | — |
| grind washed flakes | scr.shredder | 30 | 3 scr-026, 1 pwr-001 | 3 scr-006 | — |
| pelletize regrind | scr.extruder | 60 | 3 scr-006, 1 pwr-001 | 3 scr-011 | — |
| extrude recycled filament | scr.extruder | 60 | 2 scr-011, 1 pwr-001 | 2 scr-009 | — |
| extrude filament from regrind | scr.extruder | 90 | 3 scr-006, 1 pwr-001 | 2 scr-009 | — |
| spool recycled filament | scr.extruder | 20 | 3 scr-009 | 1 scr-059 | — |
| rewind a spool as printing filament | scr.extruder | 20 | 1 scr-059 | 3 pol-011 | — |
| extrude recycled sheet | scr.extruder | 60 | 3 scr-011, 1 pwr-001 | 2 scr-055 | — |
| extrude recycled rod | scr.extruder | 60 | 2 scr-011, 1 pwr-001 | 3 scr-056 | — |
| extrude recycled tubing | scr.extruder | 60 | 2 scr-011, 1 pwr-001 | 2 scr-057 | — |
| blow recycled bag film | scr.extruder | 45 | 2 scr-011, 1 pwr-001 | 3 scr-058 | — |
| grind rubber scrap | scr.shredder | 45 | 3 scr-074, 1 pwr-001 | 3 pol-023 | — |
| devulcanise rubber | scr.extruder | 90 | 3 scr-074, 1 pol-064, 1 pwr-001 | 2 scr-075 | — |
| press devulcanised rubber into sheet | scr.extruder | 60 | 2 scr-075, 1 pwr-001 | 1 pol-003 | — |
| shred foam offcuts | scr.shredder | 30 | 3 scr-020, 1 pwr-001 | 3 scr-060 | — |
| shred worn sponges | scr.shredder | 30 | 4 cln-047, 1 pwr-001 | 2 scr-060 | — |
| blow insulating foam fill | scr.shredder | 30 | 3 scr-060, 1 pwr-001 | 2 scr-061 | — |
| bag cavity insulation fill | scr.baler | 20 | 3 scr-061 | 1 thm-024 | — |
| tear rag strips | scr.sorter | 20 | 2 scr-005 | 3 scr-070 | — |
| tear rags by hand | crew | 20 | 1 scr-005 | 2 scr-070 | — |
| garnet fabric scraps | scr.shredder | 45 | 3 scr-005, 1 pwr-001 | 3 scr-012 | — |
| shred used wipes | scr.shredder | 30 | 4 hyg-011, 1 pwr-001 | 2 scr-012 | — |
| shred dried wipes | scr.shredder | 30 | 4 hyg-015, 1 pwr-001 | 2 scr-012 | — |
| card shoddy into rag fibre | scr.shredder | 30 | 3 scr-012, 1 pwr-001 | 2 fib-016 | — |
| needle felt a floor mat | scr.baler | 45 | 3 scr-012, 1 pwr-001 | 1 scr-073 | — |
| braid rag rope | any.bench | 30 | 3 scr-070 | 1 scr-071 | — |
| coil a rag rug | any.bench | 120 | 3 scr-071 | 1 scr-072 | — |
| collect cracked jars | scr.sorter | 15 | 2 pak-082 | 2 scr-017 | — |
| break up burnt out bulbs | scr.sorter | 20 | 3 lgt-075, 1 pwr-001 | 1 scr-017, 1 scr-023 | — |
| mill glass shards | scr.glassmill | 45 | 3 scr-017, 1 pwr-001 | 3 scr-010 | — |
| crush glass by hand | any.bench | 60 | 2 scr-017 | 1 scr-010 | — |
| mill cullet powder | scr.glassmill | 45 | 3 scr-010, 1 pwr-001 | 3 scr-050 | — |
| batch recycled cullet | scr.glassmill | 30 | 3 scr-010, 1 ore-005 | 2 cer-011 | — |
| fire cullet beads | scr.glassmill | 60 | 2 scr-050, 1 pwr-001 | 3 scr-051 | — |
| bag glass bead fill | scr.glassmill | 20 | 3 scr-051 | 1 bed-018 | — |
| draw fused glass rod | scr.glassmill | 60 | 3 scr-010, 2 pwr-001 | 2 scr-052 | — |
| spin glass fibre | scr.glassmill | 60 | 2 scr-052, 1 pwr-001 | 2 scr-053 | — |
| felt glass fibre into filter mat | scr.baler | 30 | 2 scr-053, 1 pwr-001 | 2 fil-037 | — |
| grind cullet into grit | scr.glassmill | 30 | 3 scr-050, 1 pwr-001 | 3 scr-054 | — |
| clean salvaged connectors | scr.stripper | 30 | 3 scr-037, 1 pwr-001 | 2 ecp-015 | — |
| test salvaged chips | scr.stripper | 45 | 3 scr-038, 1 pwr-001 | 1 ecp-006, 1 scr-003 | — |
| test salvaged capacitors | scr.stripper | 30 | 3 scr-039, 1 pwr-001 | 2 ecp-002 | — |
| refit a salvaged display | scr.stripper | 60 | 2 scr-040, 1 pwr-001 | 1 ecp-041, 1 scr-017 | — |
| rewind a salvaged motor | scr.stripper | 60 | 2 scr-044, 1 met-006 | 1 mec-010 | — |
| regrease salvaged bearings | any.bench | 20 | 2 scr-045, 1 pol-006 | 2 mec-004 | — |
| sort salvaged fasteners | scr.sorter | 15 | 4 scr-046 | 2 mec-001, 2 mec-002 | — |
| dress salvaged gears | any.bench | 20 | 2 scr-047, 1 pol-006 | 2 mec-003 | — |
| reseat a salvaged valve | any.bench | 30 | 2 scr-048, 1 pol-009 | 1 mec-007 | — |
| salvage degraded solar tiles | scr.stripper | 45 | 2 pwr-044, 1 pwr-001 | 2 scr-049, 1 scr-017 | — |
| string salvaged solar cells | any.bench | 45 | 4 scr-049, 1 scr-031 | 1 pwr-043 | — |
| build a salvage claw jaw | any.bench | 60 | 2 scr-063, 1 mec-001 | 1 scr-077 | — |
| lay a salvage claw cable | any.bench | 30 | 2 met-045 | 1 scr-078 | — |
| splice a sorter belt | any.bench | 30 | 1 pol-003, 1 fib-012 | 1 scr-079 | — |
| build a sorter magnet drum | any.bench | 45 | 1 met-077, 1 met-056 | 1 scr-080 | — |
| grind a shredder blade set | any.bench | 60 | 1 met-030 | 1 scr-081 | — |
| cut a shredder screen | any.bench | 30 | 1 met-057 | 1 scr-082 | — |
| grind stripper dies | any.bench | 45 | 1 met-030 | 2 scr-083 | — |
| build a stripper feed roller | any.bench | 30 | 1 pol-003, 1 scr-062 | 1 scr-084 | — |
| cut baler ram seals | any.bench | 20 | 1 pol-054 | 2 scr-085 | — |
| cut a baler platen | any.bench | 45 | 2 scr-063 | 1 scr-086 | — |
| line a scrap furnace | any.bench | 60 | 2 cer-006 | 1 scr-087 | — |
| fire a graphite crucible | any.bench | 45 | 1 ore-031, 1 ore-009 | 1 scr-088 | — |
| turn extruder nozzles | any.bench | 30 | 1 met-051 | 2 scr-089 | — |
| turn a filament extruder screw | any.bench | 60 | 1 met-049, 1 met-030 | 1 scr-090 | — |
| cast a cullet mill roller | any.bench | 60 | 1 met-021, 1 mec-004 | 1 scr-091 | — |
| cut a cullet mill sieve | any.bench | 20 | 1 met-057 | 1 scr-092 | — |
| assemble a salvage claw kit | any.bench | 150 | 1 fur-001, 1 scr-077, 1 scr-078, 1 mec-010 | 1 scr-093 | — |
| assemble a sorting table kit | any.bench | 90 | 1 fur-001, 1 scr-079, 1 scr-080 | 1 scr-094 | — |
| assemble a plastic shredder kit | any.bench | 120 | 1 fur-001, 1 scr-081, 1 scr-082, 1 mec-010 | 1 scr-095 | — |
| assemble a wire stripper kit | any.bench | 90 | 1 fur-001, 1 scr-083, 1 scr-084 | 1 scr-096 | — |
| assemble a scrap baler kit | any.bench | 120 | 1 fur-001, 1 scr-085, 1 scr-086, 1 mec-043 | 1 scr-097 | — |
| assemble a scrap furnace kit | any.bench | 150 | 1 fur-001, 1 scr-087, 1 scr-088, 1 cer-042 | 1 scr-098 | — |
| assemble a filament extruder kit | any.bench | 120 | 1 fur-001, 1 scr-089, 1 scr-090, 1 thm-004 | 1 scr-099 | — |
| assemble a cullet mill kit | any.bench | 120 | 1 fur-001, 1 scr-091, 1 scr-092, 1 mec-010 | 1 scr-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| scr.salvager | Claw that reaches outside the hull to recover scrap, hull flakes, electronic scrap and wreck debris. | All recovered material is COF property on contact. Ref 9000/S. |
| scr.sorter | Table that sorts refuse, scrap metal, broken parts and electronic scrap into usable streams and salvaged parts. | Metal left, plastic right, unknown in the middle. Unknowns are reported. |
| scr.shredder | Shredder that cuts, washes and grinds plastic, rubber, foam, cloth and batteries into flakes, crumb and fibre. | KEEP HANDS OUT OF HOPPER. USE PUSH STICK. COF PROPERTY. |
| scr.stripper | Stripper that removes cable insulation for copper, and pulls, tests and refits salvaged chips, displays and motors. | Feed cable, not sleeves. Sleeve entanglements are logged as operator error. |
| scr.baler | Baler that presses loose scrap, plastic and fabric into bales, and felts fibre into mats. | Ram pressure checked, passed, rev 6. Hydraulic weep under platen noted. |
| scr.furnace | Furnace that melts scrap into reclaimed metal, ingots, plate, rod and ballast, and refines electronic scrap and battery mass. | Everything melts eventually. Fume extraction to be on before charging. Proc 620. |
| scr.extruder | Extruder that turns regrind into pellets, filament, sheet, rod, tubing and film, and devulcanises rubber. | Recycled content output is reported upward and praised by nobody. |
| scr.glassmill | Mill that crushes glass and slag into cullet, powder, beads, rod, fibre and abrasive grit. | SILICA DUST. RESPIRATOR REQUIRED. LID CLOSED WHEN RUNNING. |
| scr-001 | Mixed metal waste left by worn goods throughout the ship, sorted, baled or melted back into metal. | One station's junk is the furnace's feedstock. Weigh in at the sorter. |
| scr-002 | Mixed plastic waste, shredded, washed, baled or reground into pellets. | There is no away. Only the shredder. Notice 2. |
| scr-003 | Dead electronics, sorted or dismantled for boards, cable, batteries and screens. | Contains recoverable value. Disposal outside the sorter is a recovery loss. Ref 0303/E. |
| scr-004 | Worn-out mechanical parts, torn down for bearings, fasteners, gears, motors and valves. | Not broken. Disassembled in advance. |
| scr-005 | Cloth offcuts and old clothing, reused for rags, stuffing, wipes and bandages; left too long, they rot. | Every rag was a uniform once. Some are still being worn. |
| scr-006 | Ground plastic, ready to pelletize or extrude into filament. | Mixed colours permitted. Mixed polymers are not. Proc 66. |
| scr-007 | Rough mixed-metal ingot, refined into steel or remelted. | COMPOSITION UNKNOWN. NOT FOR STRUCTURAL USE UNTIL REFINED. |
| scr-008 | Copper recovered from wire and electronic scrap, for refined copper, chemistry and brass. | Every wire comes home. Recovery rate posted weekly. |
| scr-009 | Strand drawn from recycled plastic, spooled for printing or spun into thread. | Diameter variance within tolerance. Tolerance widened for recycled stock, rev 2. |
| scr-010 | Crushed clean glass, remelted, batched, milled or drawn into rod. | The jar dropped last week is a window now. Breakage still invoiced. |
| scr-011 | Pellets made from regrind, extruded into filament, sheet, rod, tubing and film. | Grade C stock. Suitable for non-critical items. All items are non-critical until they fail. |
| scr-012 | Fibre torn from old cloth, carded into rag fibre or felted into floor mats. | Shoddy by name. Approved for issue regardless. |
| scr-013 | Unsorted rubbish swept up around the cabin, awaiting the sorting table. | Collected by the operator. Sorted by the operator. Notice 13. |
| scr-014 | Dead battery for crushing into black mass; left too long, it starts to leak. | Collect before leakage. Leaked batteries are a cleaning charge. |
| scr-015 | Corroded battery that must be neutralised before crushing; dealing with it cleans the cabin. | CORROSIVE LEAK. DO NOT HANDLE BARE. NEUTRALISE FIRST. |
| scr-016 | Metal flakes scraped from the hull, melted into reclaimed aluminium. | Hull material loss is tracked. Recovery offsets it, on paper. |
| scr-017 | Broken glass gathered for milling into cullet. | Sweep with a brush, never a hand. Hand sweeping is noted at the medical station. |
| scr-018 | Knotted salvaged wire, stripped for its copper. | Do not untangle. Strip. Untangling is not a billable task. |
| scr-019 | Old cable, stripped by machine or by hand for copper and insulation. | Cut, strip, melt, draw, cut again. Cycle count unknown. |
| scr-020 | Foam scraps, shredded into crumb or bonded into mats and plugs. | Soft waste is still waste. Bin by type. |
| scr-021 | Jar of mixed salvaged fasteners awaiting sorting. | Every workshop has one. No requisition exists for it. It persists. |
| scr-022 | Iron and steel scrap, melted into reclaimed iron; left lying, it rusts. | Melt before it rusts. Rusted stock is downgraded at receipt. |
| scr-023 | Aluminium, copper and other non-magnetic scrap, melted into reclaimed metal. | The magnet ignores it. The audit does not. |
| scr-024 | Corroded iron scrap, brushed or blasted clean, or melted down with flux. | Corrosion through neglect is charged to the storing station. Notice 24. |
| scr-025 | Dirty plastic waste that must be washed before it can be reused. | CONTENTS UNKNOWN. WASH BEFORE PROCESSING. GLOVES. |
| scr-026 | Clean plastic flakes, ready to grind into regrind. | Wash water tested, passed, rev 1. Colour of wash water not recorded. |
| scr-027 | Coarse plastic shred, ground into regrind. | Halfway between waste and resource. Counted as resource. |
| scr-028 | Aluminium recovered from hull flakes, scrap and dross, cast into ingots or remelted. | Third service life. Fatigue history not recorded. |
| scr-029 | Iron recovered from ferrous scrap, cast into ingots or alloyed into steel. | Old iron, new stock code. |
| scr-030 | Steel made from reclaimed iron and scrap, cast into ingots or rolled into plate and rod. | Indistinguishable from new steel, per Company specification. Nobody checks. |
| scr-031 | Solder recovered from boards and dross, drawn into wire or used to string solar cells. | Lead content variable. Use in non-galley equipment only. |
| scr-032 | Brass alloyed from reclaimed copper, cast into ingots. | Zinc ratio estimated, rev 2. Estimate signed off as measured. |
| scr-033 | Bare copper from stripped cable and motors, melted or redrawn into wire. | HIGH-VALUE SCRAP. WEIGH AND LOG BEFORE STORAGE. |
| scr-034 | Plastic stripped off cable, shredded for regrind. | The peel, not the fruit. Bin it anyway. |
| scr-035 | Dead circuit boards, desoldered for parts or shredded for metal. | Trace gold content. Boards are not to leave the scrap line. Ref 3535/B. |
| scr-036 | Shredded electronics, smelted for copper and precious metal. | Fine dust, toxic, valuable. All three are logged. |
| scr-037 | Connectors pulled from boards, cleaned into usable board connectors. | Wiggle test passed, rev 1. Most of them. |
| scr-038 | Chips pulled from boards; testing shows which still work. | UNTESTED. DO NOT FIT UNTIL TESTED. |
| scr-039 | Capacitors pulled from boards, tested back into service. | Discharge before handling. Reject any with bulging tops. Proc 39. |
| scr-040 | Screens pulled from dead electronics, refitted as working display panels. | Previous image burnt in. Content is not to be discussed. |
| scr-041 | Crushed battery internals, leached for metal salts. | TOXIC. HEAVY METALS. SEALED DRUM ONLY. |
| scr-042 | Metal-rich residue from smelting electronic scrap, refined into precious metal. | Two-signature custody. Single-operator stations sign twice. |
| scr-043 | Precious metal refined from electronic scrap, drawn into bond wire. | Worth more than the operator by weight. Audited more often, too. |
| scr-044 | Motor pulled from broken parts or computers, rewound into a gear motor. | Turns on test, rev 3. Brushes worn. Rewind before refit. |
| scr-045 | Bearing pulled from broken parts, regreased into a working ball bearing. | Spin by hand. If it grinds, it is scrap. Proc 45. |
| scr-046 | Bolts and nuts sorted from broken parts and jars, ready for reuse. | Count twice. Odd sizes go back in the jar. |
| scr-047 | Gears pulled from broken parts, dressed into usable spur gears. | A chipped tooth is still a tooth, per the salvage schedule. |
| scr-048 | Valve pulled from broken parts or pumps, reseated into a working ball valve. | Turns once, sticks twice. Reseat before reuse. |
| scr-049 | Cells recovered from worn solar tiles, strung, refurbished or refined. | Output degraded. Credited at reduced rate. Ref 4904/S. |
| scr-050 | Finely milled glass, fired into beads or ground into grit. | Do not sneeze near the mill. Dust mask on rack 1. |
| scr-051 | Small glass beads used as weighted fill for bedding and calming goods. | Fill weight per bag set by Company standard, rev 2. Comfort not specified. |
| scr-052 | Glass rod drawn from cullet, spun into fibre. | Snap test optional. Gloves not. |
| scr-053 | Glass fibre, felted into filter mat. | SKIN IRRITANT. HANDLE IN SLEEVES. |
| scr-054 | Grit crushed from slag, clinker and glass, for blasting, scouring and honing. | Grit size mixed. Sieve before honing work. Proc 54. |
| scr-055 | Sheet from recycled pellets, made into totes, buckets, bedpans, bins and board. | Grey only. Colour is not a stock option. |
| scr-056 | Rod from recycled pellets, made into brush handles, buckets and game sticks. | Not a weapon. Misuse is recorded under Notice 56. |
| scr-057 | Tubing from recycled pellets, fitted as a toilet diverter hose. | Odour acceptable at fitting. Re-inspect at next cycle. |
| scr-058 | Film from recycled pellets, sealed into waste bags. | Bags for the bags. Recovery loop closed, per audit. |
| scr-059 | Wound spool of recycled filament, rewound as printing filament. | RETURN EMPTY SPOOL. DEPOSIT DEDUCTED IF NOT RETURNED. |
| scr-060 | Shredded foam, blown into insulating fill or stuffed into pads. | Lumpy. Warm. Approved for padding at reduced grade. |
| scr-061 | Loose foam crumb, bagged or blown into cavities as insulation. | Fill every gap. Heat loss through unfilled cavities is metered. |
| scr-062 | Rough steel rod from reclaimed steel, for rivets, rail strip and rollers. | Straightness not guaranteed. Straighten at bench. Proc 62. |
| scr-063 | Rough steel plate from reclaimed steel, for hull patches, skins and machine parts. | A patch made of patches. Thickness measured at three points, rev 2. |
| scr-064 | Pressed block of scrap metal, melted down or cast into ballast. | Stackable. Mostly. Stack no higher than two. Notice 64. |
| scr-065 | Pressed block of plastic scrap, shredded when the line is ready. | BALE UNDER TENSION. CUT STRAPS FROM THE SIDE. |
| scr-066 | Pressed block of fabric scraps, opened into shoddy fibre. | Contents: socks, mostly. Inventoried as textile, mixed. |
| scr-067 | Dense cast scrap that stores metal compactly, remelted or cut into weight plates. | Lift with the legs. Back injuries are self-reported on Form 67B. |
| scr-068 | Oxide skimmed off molten metal, reclaimed for aluminium. | Skim, cool, bin. Hot dross in a plastic bin is a fire report. |
| scr-069 | Glassy furnace waste, crushed into abrasive grit. | Even the waste has a job. So does the operator. |
| scr-070 | Strips torn from fabric scraps, for rope, mops, cover cloth, stuffing and yarn. | Tear with the grain. Torn against it, strips are short-measured. |
| scr-071 | Rope braided from rag strips, coiled into rugs. | NOT RATED FOR LOAD. NOT FOR CLIMBING. NOT FOR RESTRAINT. |
| scr-072 | Coiled rag rug that slowly eases stress while placed, and wears back into scraps. | Pattern unofficial. Tolerated under the cabin furnishing allowance. |
| scr-073 | Needle-felted mat that keeps the cabin cleaner while placed, and wears back into scraps. | Wipe boots. Cabin cleanliness is inspected without notice. |
| scr-074 | Worn belts, seals and offcuts, ground, devulcanised or reclaimed into rubber. | The bounce is gone. The rubber is still on the ledger. |
| scr-075 | Rubber made workable again, pressed into sheet or moulded into gaskets. | Uncured and very sticky. Clean tools before it sets on them. |
| scr-076 | Fabric scraps gone bad, fit only for the compost pile. | Should have been torn sooner. Loss charged to the holding station. |
| scr-077 | Spare jaw that repairs a salvage claw. | Grips anything. Releases on command, usually. |
| scr-078 | Spare cable that repairs a salvage claw. | Inspect for broken strands every deployment. A parted cable loses the claw. |
| scr-079 | Spare belt that repairs a sorting table. | Tracking adjusted, rev 5. Belt still drifts left. |
| scr-080 | Spare magnet drum that repairs a sorting table. | STRONG MAGNET. KEEP TOOLS CLEAR. |
| scr-081 | Spare blades that repair a plastic shredder. | Sharp side out. Every time. Blade changes are a two-glove task. |
| scr-082 | Spare screen that repairs a plastic shredder. | Oversize flakes indicate a torn screen. Replace, do not patch. |
| scr-083 | Spare die that repairs a wire stripper. | Cuts the jacket, spares the copper, when set correctly. Proc 83. |
| scr-084 | Spare roller that repairs a wire stripper. | Feeds the cable, not the sleeve. Roll sleeves up. |
| scr-085 | Spare seal that repairs a scrap baler. | Oil under the baler means this has failed. Report before the slip, not after. |
| scr-086 | Spare platen that repairs a scrap baler. | Flat, heavy, unforgiving. Two-operator lift. Notice 1 applies again. |
| scr-087 | Spare refractory lining that repairs a scrap furnace. | Only the liner stands between molten metal and the deck. Inspect every heat. |
| scr-088 | Spare graphite crucible that repairs a scrap furnace. | Preheat before charging. Cracked crucibles are attributed to cold starts. |
| scr-089 | Spare nozzle that repairs a filament extruder. | Clean hot, never cold. Cold cleaning breaks the tip. Ref 8908/N. |
| scr-090 | Spare screw that repairs a filament extruder. | Flight wear measured, passed, rev 3. Measured with the wrong gauge. |
| scr-091 | Spare roller that repairs a cullet mill. | Crush, do not shatter. Gap setting on the plate. |
| scr-092 | Spare sieve that repairs a cullet mill. | Fines through, chunks back. Torn mesh passes chunks. Check weekly. |
| scr-093 | Crated parts that install a salvage claw. | Deployment outside the hull per Proc 900. Read it before first reach. |
| scr-094 | Crated parts that install a sorting table. | Refuse supplied by every other station. Indefinitely. |
| scr-095 | Crated parts that install a plastic shredder. | BLADE BOX SEALED. DO NOT OPEN UNTIL UNIT IS BOLTED DOWN. |
| scr-096 | Crated parts that install a wire stripper. | Install before the cable backlog exceeds the bay. It already has. |
| scr-097 | Crated parts that install a scrap baler. | Bolt down before first compression. Ref 9700/B. |
| scr-098 | Crated parts that install a scrap furnace. | Line before lighting. Unlined furnaces are a hull breach in waiting. |
| scr-099 | Crated parts that install a filament extruder. | First spool out is always off-spec. Regrind it. |
| scr-100 | Crated parts that install a cullet mill. | Sweep the bay before installing. The irony is noted and not actioned. |
