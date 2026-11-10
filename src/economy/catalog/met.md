# Metals & Alloys — `met`

The foundry's metal line, from ore concentrate to stock. The furnace smelts concentrates from the mine (`ore`) with
carbon and limestone into ingots and leaves slag; ingots are alloyed into steel, brass, bronze and the specialty
alloys, rolled into sheet, plate and foil, drawn into wire, rod and tube, atomised into powder and cast or forged into
the blanks that parts (`mec`), cables (`pwr`), hull plates (`hul`) and every device kit start from. Slag, scale, dross,
swarf and offcuts are real leftovers that recycling (`scr`) and the kiln (`cer`) take back.

## Devices

| id | device | role | cells |
|---|---|---|---|
| met.furnace | FM800 Smelting Furnace | smelt | 3x2 |
| met.caster | FM420 Casting Station | smelt | 2x2 |
| met.mill | FM600 Rolling Mill | smelt | 3x2 |
| met.drawbench | FM210 Draw Bench | smelt | 2x1 |
| met.forge | FM750 Forge Press | smelt | 2x2 |
| met.atomiser | FM330 Powder Atomiser | smelt | 2x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| met-001 | Ingot, Iron | — | — |
| met-002 | Ingot, Steel | — | — |
| met-003 | Ingot, Copper | — | — |
| met-004 | Ingot, Aluminium | — | — |
| met-005 | Plate, Steel | — | — |
| met-006 | Wire, Copper | — | — |
| met-007 | Sheet, Aluminium | — | — |
| met-008 | Rod, Steel | — | — |
| met-009 | Sheet, Steel | — | — |
| met-010 | Slag | — | — |
| met-011 | Ingot, Titanium | — | — |
| met-012 | Ingot, Lead | — | — |
| met-013 | Ingot, Tin | — | — |
| met-014 | Ingot, Nickel | — | — |
| met-015 | Ingot, Zinc | — | — |
| met-016 | Ingot, Chromium | — | — |
| met-017 | Ingot, Magnesium | — | — |
| met-018 | Ingot, Cobalt | — | — |
| met-019 | Ferromanganese | — | — |
| met-020 | Metal, Rare Earth | — | — |
| met-021 | Ingot, Cast Iron | — | — |
| met-022 | Ingot, Brass | — | — |
| met-023 | Ingot, Bronze | — | — |
| met-024 | Ingot, Aluminium Alloy | — | — |
| met-025 | Ingot, Nichrome | — | — |
| met-026 | Ingot, Stainless Steel | — | — |
| met-027 | Ingot, Titanium Alloy | — | — |
| met-028 | Ingot, Magnet Alloy | — | — |
| met-029 | Ingot, Spring Steel | — | — |
| met-030 | Ingot, Tool Steel | — | — |
| met-031 | Ingot, Invar | — | — |
| met-032 | Solder, Tin | — | — |
| met-033 | Sheet, Steel, Galvanised | — | — |
| met-034 | Sheet, Stainless | — | — |
| met-035 | Sheet, Titanium | — | — |
| met-036 | Sheet, Brass | — | — |
| met-037 | Sheet, Copper | — | — |
| met-038 | Plate, Aluminium Alloy | — | — |
| met-039 | Foil, Aluminium | — | — |
| met-040 | Foil, Copper | — | — |
| met-041 | Sheet, Lead | — | — |
| met-042 | Strip, Steel | — | — |
| met-043 | Sheet, Tinplate | — | — |
| met-044 | Wire, Iron | — | — |
| met-045 | Wire, Steel | — | — |
| met-046 | Wire, Aluminium | — | — |
| met-047 | Wire, Nichrome | — | — |
| met-048 | Wire, Spring | — | — |
| met-049 | Rod, Stainless | — | — |
| met-050 | Rod, Titanium | — | — |
| met-051 | Rod, Brass | — | — |
| met-052 | Rod, Bronze | — | — |
| met-053 | Tube, Copper | — | — |
| met-054 | Tube, Steel | — | — |
| met-055 | Tube, Aluminium | — | — |
| met-056 | Tube, Stainless | — | — |
| met-057 | Mesh, Steel Wire | — | — |
| met-058 | Mesh, Copper | — | — |
| met-059 | Honeycomb, Aluminium | — | — |
| met-060 | Powder, Iron | — | — |
| met-061 | Powder, Copper | — | — |
| met-062 | Powder, Aluminium | — | — |
| met-063 | Powder, Titanium | — | — |
| met-064 | Powder, Nickel | — | — |
| met-065 | Mix, Sinter | — | — |
| met-066 | Shot, Lead | — | — |
| met-067 | Blank, Bolt | — | — |
| met-068 | Blank, Rivet | — | — |
| met-069 | Blank, Gear | — | — |
| met-070 | Blank, Bearing Race | — | — |
| met-071 | Blank, Bushing, Bronze | — | — |
| met-072 | Casting, Pump Housing | — | — |
| met-073 | Casting, Valve Body | — | — |
| met-074 | Casting, Machine Frame | — | — |
| met-075 | Casting, Pipe Fitting | — | — |
| met-076 | Blank, Heat Sink | — | — |
| met-077 | Blank, Magnet | — | — |
| met-078 | Rod, Welding | — | — |
| met-079 | Rod, Brazing | — | — |
| met-080 | Wool, Steel | — | 720 h → met-081 |
| met-081 | Scale, Mill | — | — |
| met-082 | Dross, Aluminium | — | — |
| met-083 | Swarf, Metal | — | — |
| met-084 | Offcuts, Steel | — | — |
| met-085 | Mould, Sand Casting | — | — |
| met-086 | Sand, Moulding, Burnt | — | — |
| met-087 | Roller, Mill, Worn | — | — |
| met-088 | Liner, Crucible | fits met.furnace | 400 h → cer-086 |
| met-089 | Element, Heating, Furnace | fits met.furnace | 600 h → scr-001 |
| met-090 | Insert, Caster Mould | fits met.caster | 600 h → scr-004 |
| met-091 | Roller, Mill | fits met.mill | 800 h → met-087 |
| met-092 | Die, Drawing | fits met.drawbench | 500 h → scr-004 |
| met-093 | Face, Anvil, Forge | fits met.forge | 1000 h → scr-001 |
| met-094 | Nozzle, Atomiser | fits met.atomiser | 400 h → scr-004 |
| met-095 | Kit, Smelting Furnace | installs met.furnace | — |
| met-096 | Kit, Casting Station | installs met.caster | — |
| met-097 | Kit, Rolling Mill | installs met.mill | — |
| met-098 | Kit, Draw Bench | installs met.drawbench | — |
| met-099 | Kit, Forge Press | installs met.forge | — |
| met-100 | Kit, Powder Atomiser | installs met.atomiser | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| smelt a bloom on the bench | any.bench | 240 | 3 ore-003, 2 ore-007, 2 pwr-001 | 1 met-001, 2 met-010 | — |
| smelt iron | met.furnace | 120 | 3 ore-053, 1 ore-081, 1 ore-052, 2 pwr-001 | 2 met-001, 1 met-010 | — |
| smelt raw iron ore | met.furnace | 150 | 4 ore-003, 2 ore-007, 2 pwr-001 | 1 met-001, 2 met-010 | — |
| remelt scrap metal | met.furnace | 90 | 3 scr-001, 1 pwr-001 | 2 met-001, 1 met-010 | — |
| refine scrap ingots | met.furnace | 90 | 2 scr-007, 1 gas-001, 1 pwr-001 | 1 met-002, 1 met-010 | — |
| blow steel | met.furnace | 90 | 2 met-001, 1 gas-001, 1 ore-081, 1 pwr-001 | 2 met-002, 1 met-010 | — |
| smelt copper | met.furnace | 120 | 3 ore-054, 1 ore-050, 2 pwr-001 | 2 met-003, 1 met-010 | — |
| refine reclaimed copper | met.furnace | 60 | 2 scr-008, 1 pwr-001 | 2 met-003 | — |
| smelt aluminium | met.furnace | 180 | 2 cer-037, 1 ore-081, 3 pwr-001 | 2 met-004, 1 met-082 | — |
| smelt ground bauxite | met.furnace | 240 | 4 ore-066, 1 ore-081, 4 pwr-001 | 1 met-004, 1 met-082, 1 met-010 | — |
| remelt reclaimed aluminium | met.furnace | 60 | 2 scr-028, 1 pwr-001 | 2 met-004, 1 met-082 | — |
| smelt titanium | met.furnace | 240 | 3 ore-059, 1 chm-006, 1 met-017, 3 pwr-001 | 1 met-011, 1 met-010 | — |
| smelt lead | met.furnace | 90 | 3 ore-055, 1 ore-081, 1 pwr-001 | 2 met-012, 1 met-010 | — |
| smelt tin | met.furnace | 90 | 3 ore-056, 1 ore-081, 1 pwr-001 | 2 met-013, 1 met-010 | — |
| smelt nickel | met.furnace | 120 | 3 ore-058, 1 ore-081, 2 pwr-001 | 2 met-014, 1 met-010 | — |
| smelt zinc | met.furnace | 90 | 3 ore-057, 1 ore-081, 1 pwr-001 | 2 met-015, 1 met-010 | — |
| reduce chromium | met.furnace | 120 | 3 ore-060, 1 met-062, 2 pwr-001 | 1 met-016, 1 met-010 | — |
| smelt magnesium | met.furnace | 180 | 3 ore-067, 1 ore-081, 3 pwr-001 | 1 met-017, 1 met-010 | — |
| smelt cobalt | met.furnace | 150 | 2 ore-061, 1 ore-081, 2 pwr-001 | 1 met-018, 1 met-010 | — |
| smelt ferromanganese | met.furnace | 120 | 2 ore-062, 1 ore-053, 1 ore-081, 2 pwr-001 | 2 met-019, 1 met-010 | — |
| reduce rare earth metal | met.furnace | 180 | 2 chm-076, 1 met-017, 3 pwr-001 | 1 met-020, 1 met-010 | — |
| reduce mill scale | met.furnace | 60 | 3 met-081, 1 ore-081, 1 pwr-001 | 1 met-001, 1 met-010 | — |
| reclaim aluminium dross | met.furnace | 60 | 3 met-082, 1 pwr-001 | 1 met-004, 1 met-010 | — |
| remelt swarf | met.furnace | 60 | 3 met-083, 1 pwr-001 | 1 met-002, 1 met-010 | — |
| remelt steel offcuts | met.furnace | 45 | 2 met-084, 1 pwr-001 | 1 met-002 | — |
| alloy brass | met.furnace | 60 | 2 met-003, 1 met-015, 1 pwr-001 | 2 met-022 | — |
| alloy bronze | met.furnace | 60 | 2 met-003, 1 met-013, 1 pwr-001 | 2 met-023 | — |
| alloy aluminium | met.furnace | 60 | 3 met-004, 1 met-017, 1 pwr-001 | 3 met-024 | — |
| alloy nichrome | met.furnace | 90 | 2 met-014, 1 met-016, 1 pwr-001 | 2 met-025 | — |
| alloy stainless steel | met.furnace | 120 | 2 met-002, 1 met-016, 1 met-014, 1 pwr-001 | 3 met-026 | — |
| alloy titanium | met.furnace | 150 | 2 met-011, 1 met-004, 2 pwr-001 | 2 met-027 | — |
| alloy magnet metal | met.furnace | 150 | 2 met-001, 1 met-020, 1 met-018, 2 pwr-001 | 2 met-028 | — |
| alloy spring steel | met.furnace | 90 | 2 met-002, 1 met-019, 1 pwr-001 | 2 met-029 | — |
| alloy tool steel | met.furnace | 150 | 2 met-002, 1 met-016, 1 met-018, 2 pwr-001 | 2 met-030 | — |
| alloy invar | met.furnace | 120 | 2 met-001, 1 met-014, 1 pwr-001 | 2 met-031 | — |
| cast iron pigs | met.caster | 60 | 2 met-001, 1 ore-081, 1 pwr-001 | 2 met-021 | — |
| cast tin solder | met.caster | 30 | 2 met-013, 1 met-012, 1 pwr-001 | 3 met-032 | — |
| recast reclaimed solder | met.caster | 30 | 2 scr-031, 1 pwr-001 | 2 met-032 | — |
| ram sand casting moulds | met.caster | 30 | 2 ore-050, 1 ore-075 | 2 met-085 | — |
| reclaim moulding sand | met.caster | 30 | 3 met-086, 1 pwr-001 | 2 ore-050 | — |
| cast pump housings | met.caster | 90 | 2 met-021, 1 met-085, 1 pwr-001 | 2 met-072, 1 met-086 | — |
| cast valve bodies | met.caster | 90 | 1 met-022, 1 met-021, 1 met-085, 1 pwr-001 | 2 met-073, 1 met-086 | — |
| cast a machine frame | met.caster | 150 | 3 met-021, 1 met-085, 2 pwr-001 | 1 met-074, 1 met-086 | — |
| cast pipe fittings | met.caster | 60 | 1 met-022, 1 met-085, 1 pwr-001 | 3 met-075, 1 met-086 | — |
| cast bronze bushings | met.caster | 60 | 1 met-023, 1 pwr-001 | 3 met-071 | — |
| cast magnet blanks | met.caster | 90 | 1 met-028, 1 pwr-001 | 2 met-077 | — |
| roll steel plate | met.mill | 60 | 2 met-002, 1 pwr-001 | 2 met-005 | — |
| roll steel sheet | met.mill | 45 | 1 met-002, 1 pwr-001 | 2 met-009 | — |
| roll aluminium sheet | met.mill | 45 | 1 met-004, 1 pwr-001 | 2 met-007 | — |
| galvanise steel sheet | met.mill | 60 | 2 met-009, 1 met-015, 1 chm-052, 1 pwr-001 | 2 met-033 | — |
| roll stainless sheet | met.mill | 60 | 1 met-026, 1 pwr-001 | 2 met-034 | — |
| roll titanium sheet | met.mill | 90 | 1 met-027, 1 pwr-001 | 1 met-035 | — |
| roll brass sheet | met.mill | 45 | 1 met-022, 1 pwr-001 | 2 met-036 | — |
| roll copper sheet | met.mill | 45 | 1 met-003, 1 pwr-001 | 2 met-037 | — |
| roll aluminium alloy plate | met.mill | 60 | 2 met-024, 1 pwr-001 | 2 met-038 | — |
| roll aluminium foil | met.mill | 30 | 1 met-007, 1 pwr-001 | 3 met-039 | — |
| roll copper foil | met.mill | 30 | 1 met-037, 1 pwr-001 | 3 met-040 | — |
| roll lead sheet | met.mill | 45 | 1 met-012, 1 pwr-001 | 2 met-041 | — |
| slit steel strip | met.mill | 30 | 1 met-009, 1 pwr-001 | 2 met-042 | — |
| tin steel sheet | met.mill | 60 | 1 met-009, 1 met-013, 1 chm-054, 1 pwr-001 | 2 met-043 | — |
| mill heat sink blanks | met.mill | 60 | 1 met-038, 1 pwr-001 | 2 met-076, 1 met-083 | — |
| bond aluminium honeycomb | met.mill | 90 | 2 met-039, 1 pol-007 | 1 met-059 | — |
| draw copper wire by hand | any.bench | 60 | 1 met-003 | 1 met-006 | fitness +2 |
| draw copper wire | met.drawbench | 45 | 1 met-003, 1 pwr-001 | 3 met-006 | — |
| redraw stripped copper | met.drawbench | 45 | 2 scr-033, 1 pwr-001 | 2 met-006 | — |
| draw iron wire | met.drawbench | 45 | 1 met-001, 1 pwr-001 | 3 met-044 | — |
| draw steel wire | met.drawbench | 45 | 1 met-002, 1 pwr-001 | 3 met-045 | — |
| draw aluminium wire | met.drawbench | 45 | 1 met-004, 1 pwr-001 | 3 met-046 | — |
| draw nichrome wire | met.drawbench | 45 | 1 met-025, 1 pwr-001 | 3 met-047 | — |
| draw spring wire | met.drawbench | 45 | 1 met-029, 1 pwr-001 | 3 met-048 | — |
| draw copper tube | met.drawbench | 60 | 1 met-037, 1 pwr-001 | 2 met-053 | — |
| draw steel tube | met.drawbench | 60 | 1 met-009, 1 pwr-001 | 2 met-054 | — |
| draw aluminium tube | met.drawbench | 60 | 1 met-007, 1 pwr-001 | 2 met-055 | — |
| draw stainless tube | met.drawbench | 60 | 1 met-034, 1 pwr-001 | 2 met-056 | — |
| weave steel wire mesh | met.drawbench | 60 | 3 met-045, 1 pwr-001 | 2 met-057 | — |
| weave copper mesh | met.drawbench | 60 | 3 met-006, 1 pwr-001 | 2 met-058 | — |
| draw welding rod | met.drawbench | 30 | 1 met-045, 1 chm-051 | 3 met-078 | — |
| draw brazing rod | met.drawbench | 30 | 1 met-022, 1 chm-051 | 3 met-079 | — |
| shave steel wool | met.drawbench | 30 | 1 met-045, 1 pwr-001 | 3 met-080 | — |
| forge steel rod | met.forge | 45 | 1 met-002, 1 pwr-001 | 2 met-008 | — |
| forge stainless rod | met.forge | 45 | 1 met-026, 1 pwr-001 | 2 met-049 | — |
| forge titanium rod | met.forge | 60 | 1 met-027, 1 pwr-001 | 1 met-050 | — |
| forge brass rod | met.forge | 45 | 1 met-022, 1 pwr-001 | 2 met-051 | — |
| forge bronze rod | met.forge | 45 | 1 met-023, 1 pwr-001 | 2 met-052 | — |
| head bolt blanks | met.forge | 45 | 1 met-008, 1 pwr-001 | 4 met-067, 1 met-083 | — |
| head rivet blanks | met.forge | 30 | 1 met-044, 1 pwr-001 | 4 met-068 | — |
| blank gears | met.forge | 60 | 1 met-005, 1 pwr-001 | 2 met-069, 1 met-084 | — |
| forge bearing races | met.forge | 90 | 1 met-030, 1 pwr-001 | 2 met-070, 1 met-083 | — |
| atomise iron | met.atomiser | 60 | 1 met-001, 1 pwr-001 | 3 met-060 | — |
| atomise copper | met.atomiser | 60 | 1 met-003, 1 pwr-001 | 3 met-061 | — |
| atomise aluminium | met.atomiser | 60 | 1 met-004, 1 pwr-001 | 3 met-062 | — |
| atomise titanium | met.atomiser | 90 | 1 met-011, 1 gas-014, 2 pwr-001 | 2 met-063 | — |
| atomise nickel | met.atomiser | 60 | 1 met-014, 1 pwr-001 | 3 met-064 | — |
| blend sinter mix | met.atomiser | 30 | 1 met-060, 1 met-063, 1 met-064 | 3 met-065 | — |
| drip lead shot | met.atomiser | 30 | 1 met-012, 1 pwr-001 | 3 met-066 | — |
| line a crucible | any.bench | 60 | 2 cer-006, 1 cer-050 | 1 met-088 | — |
| wind a furnace heating element | met.drawbench | 60 | 2 met-047, 1 cer-035 | 1 met-089 | — |
| cast a mould insert | met.caster | 90 | 2 met-021, 1 cer-006, 1 pwr-001 | 1 met-090 | — |
| forge a mill roller | met.forge | 150 | 2 met-030, 1 met-070, 2 pwr-001 | 1 met-091 | — |
| regrind a mill roller | met.forge | 90 | 1 met-087, 1 ore-082, 1 pwr-001 | 1 met-091 | — |
| sinter a drawing die | met.forge | 120 | 1 met-030, 1 met-065, 1 pwr-001 | 1 met-092 | — |
| forge an anvil face | met.forge | 150 | 2 met-030, 1 met-065, 2 pwr-001 | 1 met-093 | — |
| make an atomiser nozzle | met.forge | 90 | 1 met-050, 1 cer-038, 1 pwr-001 | 1 met-094 | — |
| assemble a smelting furnace | any.bench | 240 | 1 met-088, 1 met-089, 2 met-005, 4 cer-043, 1 pwr-016 | 1 met-095 | — |
| assemble a casting station | any.bench | 180 | 1 met-090, 1 met-074, 2 cer-058, 1 mec-010 | 1 met-096 | — |
| assemble a rolling mill | any.bench | 240 | 2 met-091, 1 met-074, 2 met-069, 2 met-052, 1 mec-012 | 1 met-097 | — |
| assemble a draw bench | any.bench | 180 | 1 met-092, 1 met-074, 1 mec-010 | 1 met-098 | — |
| assemble a forge press | any.bench | 240 | 1 met-093, 1 met-074, 1 mec-043, 2 met-078 | 1 met-099 | — |
| assemble a powder atomiser | any.bench | 180 | 1 met-094, 1 met-056, 1 mec-042, 1 cer-047 | 1 met-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| met.furnace | Furnace that smelts ore concentrates into ingots, remelts scrap and leftovers, and alloys steel, brass, bronze and specialty metals. | MOLTEN METAL. FACE SHIELD REQUIRED. COF PROPERTY. |
| met.caster | Station that pours iron, brass and alloys into sand moulds for housings, frames, fittings and blanks, and casts solder. | Pour slow. Stand back. Burns from splash are self-inflicted per Notice 310. |
| met.mill | Mill that rolls ingots into plate, sheet, foil and strip, and galvanises and tins steel sheet. | Ear protection is issued once per contract. Replacements are deducted. |
| met.drawbench | Bench that draws metal into wire, tube and rod, weaves mesh and winds heating elements. | Pull, do not push. The die sets the gauge, not the operator. |
| met.forge | Press that forms ingots into rods, bolts, rivets, gears and bearing races, and forges the foundry's tooling. | KEEP HANDS CLEAR OF RAM. TWO-HAND CONTROL MUST NOT BE BYPASSED. |
| met.atomiser | Atomiser that sprays molten metal into fine powders and lead shot, and blends sinter mix. | Respirator seal checked, passed, rev 3. Filter overdue, noted. |
| met-001 | Plain iron for steel, cast iron, invar, magnets, wire and powder. | Iron first, everything after. |
| met-002 | Steel for plate, sheet, rod, wire and the alloy steels. | Stock code stamped on the end face. Unstamped ingots are not accepted at stores. |
| met-003 | Pure copper for wire, sheet, brass, bronze and powder. | Copper is a controlled stock item. Weigh in, weigh out. Ref 1180/M. |
| met-004 | Light metal for sheet, wire, alloys and powder. | Light enough to lift. Lifting is still logged. |
| met-005 | Thick rolled steel for machine frames, tooling, gears, casks and furnace shells. | If in doubt, plate it. If plated, sign the stock sheet. |
| met-006 | Bare drawn copper for cable, coils, mesh and nearly every piece of electrical equipment. | Kilometres aboard. Every metre is on the inventory. |
| met-007 | Thin light sheet for fans, mounts, panels, foil and tube. | Bends easy, dents easier. Dented stock is downgraded. |
| met-008 | Forged round bar for bolts, handles, pistons and gym bars. | CUT TO LENGTH AT BENCH ONLY. NO FREEHAND GRINDING. |
| met-009 | Rolled sheet for stamping, cell casings, strip, tube and galvanising. | Sheet edges are sharp. Gloves are issued. Cuts are not compensated. |
| met-010 | Glassy waste from smelting, spun into slag wool or cast into tiles. | Waste is a resource until the Company says otherwise. Notice 22. |
| met-011 | Strong light metal for titanium alloy and titanium powder. | Hard won, hard worn, hard to account for. |
| met-012 | Soft heavy metal for solder, sheet, shot, oxide, battery plates and radiation shielding. | TOXIC. WASH HANDS. DO NOT CHEW. |
| met-013 | Soft metal for solder, bronze, tinplate and fuse wire. | Tin holds the ship together, one joint at a time. |
| met-014 | Nickel for stainless steel, nichrome, invar, powder and electrodes. | Alloying stock. Not for general issue. Requisition on Form 48N. |
| met-015 | Zinc for brass, galvanising, zinc oxide and cell anodes. | Sacrifices itself so the steel does not have to. Nobody else does. |
| met-016 | Hard bright metal alloyed into nichrome, stainless steel and tool steel. | Batch assayed, passed, rev 2. Assay sheet coffee-stained. |
| met-017 | Light reactive metal that reduces titanium and rare earths and alloys aluminium. | FLAMMABLE METAL. NO WATER ON FIRE. CLASS D EXTINGUISHER ONLY. |
| met-018 | Tough metal alloyed into magnets and tool steel. | Strategic stock. Usage above quota triggers review. Ref 6604/C. |
| met-019 | Iron and manganese alloy for spring steel and crusher jaws. | Makes steel tough enough to bite rock. Rock bites back. |
| met-020 | Rare metal reduced from its oxide, alloyed into magnets. | Every motor aboard turns on a handful of this. The handful is counted. |
| met-021 | Iron pig for casting housings, frames, valve bodies, weights and flywheels. | Heavy, brittle, honest. Drop one and both are true. |
| met-022 | Copper and zinc alloy for valves, fittings, sheet, rod and brazing rod. | Polishing is not a scheduled task. Tarnish is within spec. |
| met-023 | Copper and tin alloy for bushings, rod and bowls. | BRONZE. NOT FOR PERSONAL ITEMS. COF PROPERTY. |
| met-024 | Stronger aluminium alloy for plate, impellers and moulds. | Alloy grade stamped on top. Mixed grades are scrapped. Proc 230. |
| met-025 | Nickel and chromium alloy drawn into heating wire and turbine blades. | Glows red and keeps going. Unlike the night shift. |
| met-026 | Rustproof steel for sheet, rod, nozzles and drive parts. | Rust is somebody else's department. |
| met-027 | Strong, light alloy for sheet, rod, and drive and shield parts. | Issued against signature only. Lost units investigated. Form 11T. |
| met-028 | Iron, cobalt and rare earth alloy cast into magnet blanks. | Keep off the tool tray unless a search for every spanner is wanted. |
| met-029 | Springy steel drawn into spring wire. | Temper certified at the furnace. Certificate filed, location unknown. |
| met-030 | Hard steel for dies, bits, races, rollers, files and cutters. | The steel that cuts the steel. Signed out per shift. |
| met-031 | Iron and nickel alloy that barely expands with heat, for layup mould tools. | Dimensionally stable. The only thing aboard that is. |
| met-032 | Tin and lead alloy for joining wires, solar cells and circuit boards. | Lead content. Ventilate. Do not eat at the bench. Notice 92. |
| met-033 | Zinc-coated steel that resists rust, riveted into panel enclosures. | Do not weld galvanised. Fumes are a reportable exposure. |
| met-034 | Rolled stainless for kitchen equipment, lab kits, tubes and trays. | Wipes clean. Mostly. The rest is called patina on the form. |
| met-035 | Rolled titanium for electrodes, hull plates and drive nozzles. | Thickness gauged, 3 of 3 points, rev 5. Edge burred, accepted. |
| met-036 | Rolled brass for contacts, crimp terminals, hinges and latches. | Rings when struck. Striking stock is not a sanctioned activity. |
| met-037 | Rolled copper for foil, tube, bus bars and thermal parts. | COPPER STOCK. ISSUE BY WEIGHT. RETURN OFFCUTS. |
| met-038 | Thick alloy plate for heat sinks, tank shells and moulds. | Plate flatness within tolerance. Tolerance revised upward, rev 4. |
| met-039 | Thin foil for honeycomb, capacitors, blister packs and supercapacitors. | Foil is not for wrapping personal food. Notice 117 still applies. |
| met-040 | Thin copper for circuit boards and superconducting coils. | Tears if breathed on. Torn foil is logged as waste. |
| met-041 | Rolled lead for radiation shielding, foil and reactor kits. | SHIELDING MATERIAL. DO NOT REMOVE FROM REACTOR STOCK. |
| met-042 | Narrow steel for blades, rails, tines and straps. | Thin, sharp and in every toolbox. Count them back in. |
| met-043 | Tin-coated steel for cans, lids, button cells and oxygen candles. | Coating weight sampled per batch. Proc 188. Sample size: one. |
| met-044 | Soft wire for rivets, frames and plant ties. | Ties up tomatoes and holds up hulls. Same requisition form. |
| met-045 | Strong wire for mesh, strings, needles, welding rod and steel wool. | Wire under tension. Eye protection. Notice 64. |
| met-046 | Light wire for power cable and bonsai training. | Carries current and bends trees. Only one of those is budgeted. |
| met-047 | Heating wire for nearly every element, coil and heating pad aboard. | Resistance checked per reel, rev 6. Reel label replaced by hand. |
| met-048 | Springy wire for springs, relays, breakers and needles. | Uncoils without warning. Injuries on Form 9I. |
| met-049 | Rustproof rod for stirrers, blades, valves and paddles. | Stirs acid all shift without complaint. Set as the standard for personnel. |
| met-050 | Strong light rod for nozzles, hull braces, drone arms and drive parts. | Light in the hand, heavy in the logbook. |
| met-051 | Rod turned into nozzles, pegs, glands, cartridges and terminal blocks. | If it screws in, it started as this. |
| met-052 | Rod for worm gears, bells, rolling mills and charger contacts. | BRONZE BAR. NON-SPARKING. STORE DRY. |
| met-053 | Drawn tube for condensers, cold traps and coils. | Bend with the tool, not the knee. Kinked tube is scrap. |
| met-054 | Drawn tube for frames, rollers, racks, legs and slug cladding. | Wall thickness verified, passed, rev 2. One end crushed in transit. |
| met-055 | Light tube for flutes, rails, brushes and slats. | Hollow stock. Personal instruments made from it are confiscated. |
| met-056 | Rustproof tube for catalyst cartridges, stills, control rods and lab equipment. | Bore cleanliness certified. Do not look down it. Ref 3021/T. |
| met-057 | Woven steel mesh for racks, screens, filters and still packing. | Catches everything but water and rumour. |
| met-058 | Woven copper for shielded cable, ground straps, air filters and wicks. | Mesh count per spec. Spec not attached. Assumed correct. |
| met-059 | Bonded foil honeycomb, the light core of sandwich and hull panels. | CRUSHABLE CORE. DO NOT STAND ON. DO NOT STACK. |
| met-060 | Fine iron for sinter mix, catalysts, oxygen candles, absorbers and supplements. | Keep sealed. Rusts in cabin air. Cabin air is not adjusted for it. |
| met-061 | Fine copper sintered into contacts and wicks and mixed into pastes. | Fine powder. Mask required. Mask stock: see Notice 302. |
| met-062 | Fine aluminium for mirrors, chromium reduction and drive fuel. | COMBUSTIBLE DUST. NO SPARKS. NO OPEN FLAME. NO EXCEPTIONS. |
| met-063 | Fine titanium blended into sinter mix. | Expensive dust. Spills are swept, weighed and reported. |
| met-064 | Fine nickel for sinter mix and nickel cathode plates. | Sensitiser. Rash on contact is not a medical claim. Ref 7740/H. |
| met-065 | Blended metal powders pressed into drawing dies and anvil faces. | Blend ratio per sheet 12. Sheet 12 is the stained one. |
| met-066 | Small lead pellets that weight fuel casks and net edges. | Rattles like rain in a bucket. Nobody aboard remembers rain. |
| met-067 | Headed rod blank turned into bolts, or fitted directly into chassis and drills. | Half a bolt. Threads to follow, per schedule. |
| met-068 | Headed blank for rivets, hull rivets and panel enclosures. | Count by the hundred. Short boxes are charged to the receiver. |
| met-069 | Flat steel disc awaiting the cutting of its teeth. | No teeth yet. Tag says pending. Tag has said pending for some time. |
| met-070 | Forged tool steel ring, ground into bearing races or forged into mill rollers. | Hardness tested, passed, rev 7. Indent visible, as required. |
| met-071 | Cast bronze sleeve, the wear bearing of the jaw crusher. | Takes the grind so the shaft does not. Replace before the shaft notices. |
| met-072 | Cast iron shell for pumps and batch reactors. | Pressure tested at casting. Porosity within spec. Spec widened, rev 3. |
| met-073 | Cast brass and iron body for valves, regulators, stills and manifolds. | FLOW ARROW CAST IN. INSTALL WITH ARROW, NOT OPINION. |
| met-074 | Heavy cast iron frame on which most production device kits are built. | Two-operator lift. Single-operator stations: see Notice 1, reread. |
| met-075 | Cast brass fittings, turned into pipe fittings or built into manifolds, gauges and blending tanks. | Elbows, tees and the odd crooked thread. Return crooked threads on Form 30P. |
| met-076 | Milled alloy fins for chips, lamps, inverters, regulators and heaters. | Fins are sharp and bend easily. Straighten with the comb, not a thumb. |
| met-077 | Cast magnet for rotors, speakers, generators and toys. | STRONG MAGNET. KEEP CLEAR OF INSTRUMENTS AND PACEMAKERS. |
| met-078 | Flux-coated steel rod for welding hull seams and heavy kits. | Store dry. Damp rods crack welds. Cracked welds are attributed. |
| met-079 | Flux-coated brass rod for brazing cold trap plates. | Gentler than welding, kinder to copper, slower on the timesheet. |
| met-080 | Fine steel shavings rolled into scouring pads; in time it rusts into mill scale. | Scrubs pans and pipes. Rusts quietly in the drawer. |
| met-081 | Flaky iron oxide, reduced back to iron, dissolved into ferric chloride or roasted to red pigment. | Rust, collected on purpose and entered as recovered stock. |
| met-082 | Oxide skim from aluminium smelting, reclaimed for metal. | Skim, save, remelt. Discarded dross is a recovery shortfall. |
| met-083 | Curly shavings from machining, remelted into steel. | SHARP. SWEEP, DO NOT HAND-GATHER. |
| met-084 | Trimmed scraps of steel plate, remelted into steel. | Too small to use, too valuable to lose. Bin by weight. Ref 2290/O. |
| met-085 | Rammed sand mould for casting housings, valve bodies, frames and fittings. | Made to be broken. The only item aboard that is allowed to be. |
| met-086 | Sand left from a broken mould, reclaimed into fine sand. | Smells of hot foundry and a long shift. Reclaim, do not vent. |
| met-087 | Rolling mill roller worn in service, reground with grit. | Worn. Regrind or condemn. Regrind count on the end face: 4. |
| met-088 | Refractory lining for the smelting furnace; a spare part that wears into shards. | Inspect for cracks every pour. A cracked liner ends the shift early and badly. |
| met-089 | Nichrome element for the smelting furnace; a spare part. | Element replaced, rev 9. Old one still warm when bagged. |
| met-090 | Cast iron insert for the casting station; a spare part. | Shapes every pour, keeps none. Replace at wear mark. |
| met-091 | Forged roller for the rolling mill; wears into a worn roller. | Roll surface to be kept free of hand prints. Hands to be kept free of roll. |
| met-092 | Sintered die for the draw bench; a spare part. | Small hole, controlled tolerance. Do not enlarge with a file. |
| met-093 | Sintered striking face for the forge press; a spare part. | Face condition checked, passed, rev 12. Chip on edge, ignored. |
| met-094 | Titanium and ceramic nozzle for the powder atomiser; a spare part. | Clogs readily. Clearing with wire voids the part warranty. Notice 81. |
| met-095 | Kit of parts that installs a smelting furnace. | Contents: one furnace, unassembled. Instructions: one sheet, two-sided. |
| met-096 | Kit of parts that installs a casting station. | HEAVY. THIS WAY UP. COF FOUNDRY DIVISION. |
| met-097 | Kit of parts that installs a rolling mill. | Crate weight exceeds single-operator lift limit. Lift anyway, carefully. |
| met-098 | Kit of parts that installs a draw bench. | Packing list attached. Packing list incorrect. Contents complete. |
| met-099 | Kit of parts that installs a forge press. | Bolt to deck before first stroke. Unbolted presses walk. Ref 4402/F. |
| met-100 | Kit of parts that installs a powder atomiser. | Fine-dust equipment. Unpack in still air. |
