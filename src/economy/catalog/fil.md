# Filters & Scrubbers — `fil`

What keeps the air and the water clean, and what it wears into. Charcoal is burnt and activated, zeolite pelleted into
sieve beads, amines, hydroxide and soda lime granulated, resin beads cast, membranes and hollow fibres drawn, fibre
pleated into HEPA media; all of it packed into housings as scrubber beds, canisters, cartridges, membranes and mats.
Air filters and beds sit in life support and hold `cabin.co2` or `cabin.clean` until they saturate or clog; water
cartridges and membranes fit the purifier, reclaimer, melter and electrolyser. Every one wears into a spent form:
zeolite and amine beds, silica gel and sieve beds are baked back to work, resin regenerated with brine, carbon
reactivated, mats and screens washed; hydroxide, soda lime and catalyst go to `chm`, sludge and dust to `san`, dead
housings to salvage.

## Devices

| id | device | role | cells |
|---|---|---|---|
| fil.kiln | FL110 Charcoal Kiln | hydro | 2x2 |
| fil.resinvat | FL220 Resin Vat | hydro | 2x1 |
| fil.caster | FL330 Membrane Caster | hydro | 2x2 |
| fil.packer | FL440 Cartridge Packer | hydro | 2x1 |
| fil.washer | FL550 Filter Washer | hydro | 2x1 |
| fil.pleater | FL260 Filter Pleater | atmos | 2x1 |
| fil.regenerator | FL700 Bed Regenerator | atmos | 2x2 |

## Items

| id | item | use | decays |
|---|---|---|---|
| fil-001 | Bed, Scrubber, Zeolite | cabin.co2 -2/h | 12 h → fil-002 |
| fil-002 | Bed, Zeolite, Saturated | — | — |
| fil-003 | Bed, Scrubber, Amine | cabin.co2 -3/h | 12 h → fil-004 |
| fil-004 | Bed, Amine, Saturated | — | — |
| fil-005 | Canister, Lithium Hydroxide | cabin.co2 -20, leaves 1 fil-006 | — |
| fil-006 | Canister, Hydroxide, Spent | — | — |
| fil-007 | Filter, HEPA, Cabin | cabin.clean +1/h | 240 h → fil-008 |
| fil-008 | Filter, HEPA, Clogged | — | — |
| fil-009 | Filter, Odour, Charcoal | cabin.clean +1/h | 168 h → fil-010 |
| fil-010 | Filter, Charcoal, Spent | — | — |
| fil-011 | Cartridge, Water, Sediment | fits wat.purifier | 240 h → fil-012 |
| fil-012 | Cartridge, Sediment, Clogged | — | — |
| fil-013 | Cartridge, Water, Carbon | fits wat.purifier | 240 h → fil-014 |
| fil-014 | Cartridge, Water, Carbon, Spent | — | — |
| fil-015 | Membrane, Reverse Osmosis | fits wat.reclaimer | 720 h → fil-016 |
| fil-016 | Membrane, Osmosis, Fouled | — | — |
| fil-017 | Cartridge, Ion Exchange | fits wat.purifier | 240 h → fil-018 |
| fil-018 | Cartridge, Ion Exchange, Spent | — | — |
| fil-019 | Canister, Soda Lime | cabin.co2 -15, leaves 1 fil-020 | — |
| fil-020 | Canister, Soda Lime, Spent | — | — |
| fil-021 | Charcoal | — | — |
| fil-022 | Carbon, Activated, Spent | — | — |
| fil-023 | Powder, Zeolite | — | — |
| fil-024 | Pellets, Zeolite | — | — |
| fil-025 | Beads, Molecular Sieve | — | — |
| fil-026 | Beads, Amine Sorbent | — | — |
| fil-027 | Granules, Lithium Hydroxide | — | — |
| fil-028 | Granules, Soda Lime | — | — |
| fil-029 | Soda Lime, Spent | — | — |
| fil-030 | Granules, Hydroxide, Spent | — | — |
| fil-031 | Beads, Ion Exchange Resin | — | — |
| fil-032 | Beads, Resin, Spent | — | — |
| fil-033 | Beads, Silica Gel | — | — |
| fil-034 | Silica Gel, Saturated | — | — |
| fil-035 | Sand, Filter | — | — |
| fil-036 | Sand, Filter, Fouled | — | — |
| fil-037 | Mat, Filter Fibre | — | — |
| fil-038 | Paper, Filter, Pleated | — | — |
| fil-039 | Dope, Membrane | — | — |
| fil-040 | Sheet, Membrane, Cast | — | — |
| fil-041 | Bundle, Hollow Fibre | — | — |
| fil-042 | Housing, Filter, Empty | — | — |
| fil-043 | Cake, Filter Sludge | — | — |
| fil-044 | Dust, Cabin, Captured | — | — |
| fil-045 | Mat, Prefilter, Life Support | fits any.lifesupport | 168 h → fil-046 |
| fil-046 | Mat, Prefilter, Clogged | — | — |
| fil-047 | Screen, Moisture Condenser | fits any.condenser | 240 h → fil-048 |
| fil-048 | Screen, Dust, Clogged | — | — |
| fil-049 | Ultrafilter, Urine Reclaimer | fits wat.reclaimer | 480 h → fil-050 |
| fil-050 | Ultrafilter, Fouled | — | — |
| fil-051 | Straw, Filter | — | — |
| fil-052 | Straw, Filter, Used | — | — |
| fil-053 | Tablet, Water Purification | — | — |
| fil-054 | Mask, Dust | toxin -3, leaves 1 fil-055 | — |
| fil-055 | Mask, Dust, Used | — | — |
| fil-056 | Sachet, Odour Absorber | cabin.clean +3, leaves 1 fil-057 | — |
| fil-057 | Sachet, Odour, Spent | — | — |
| fil-058 | Bed, Catalytic Oxidiser | cabin.clean +1/h | 336 h → fil-059 |
| fil-059 | Catalyst, Oxidiser, Spent | — | — |
| fil-060 | Bed, Ammonia Sorbent | cabin.clean +1/h | 168 h → fil-061 |
| fil-061 | Sorbent, Ammonia, Saturated | — | — |
| fil-062 | Filter, Air, Electrostatic | cabin.clean +2/h | 720 h → fil-063 |
| fil-063 | Filter, Electrostatic, Dirty | — | — |
| fil-064 | Curtain, Scrubber | cabin.co2 -1/h | 72 h → fil-065 |
| fil-065 | Curtain, Scrubber, Saturated | — | — |
| fil-066 | Sock, Filter, Meltwater | fits wat.melter | 120 h → fil-067 |
| fil-067 | Sock, Filter, Clogged | — | — |
| fil-068 | Insert, Tap Filter | fits any.washbasin | 240 h → fil-069 |
| fil-069 | Filter, Tap, Spent | — | — |
| fil-070 | Bed, Sieve, Gas Separator | fits gas.separator | 720 h → fil-071 |
| fil-071 | Bed, Sieve, Saturated | — | — |
| fil-072 | Pack, Sand Filter | fits wat.purifier | 480 h → fil-036 |
| fil-073 | Roll, HEPA Media | — | — |
| fil-074 | Mesh, Membrane Support | — | — |
| fil-075 | Ring, Gasket, Filter | — | — |
| fil-076 | Pellets, Activated Carbon | — | — |
| fil-077 | Cloth, Activated Carbon | — | — |
| fil-078 | Polisher, Water Electrolyser | fits gas.electrolyser | 480 h → fil-079 |
| fil-079 | Polisher, Feed, Exhausted | — | — |
| fil-080 | Filter, Canister Compressor | fits gas.compressor | 480 h → fil-081 |
| fil-081 | Filter, Intake, Clogged | — | — |
| fil-082 | Retort, Charcoal Kiln | fits fil.kiln | — |
| fil-083 | Coil, Heating, Charcoal Kiln | fits fil.kiln | — |
| fil-084 | Stirrer, Resin Vat | fits fil.resinvat | — |
| fil-085 | Doctor Blade, Membrane Caster | fits fil.caster | — |
| fil-086 | Belt, Membrane Caster | fits fil.caster | — |
| fil-087 | Ram, Cartridge Packer | fits fil.packer | — |
| fil-088 | Spray Bar, Filter Washer | fits fil.washer | — |
| fil-089 | Pump, Backwash, Filter Washer | fits fil.washer | — |
| fil-090 | Fold Bar, Filter Pleater | fits fil.pleater | — |
| fil-091 | Glue Head, Filter Pleater | fits fil.pleater | — |
| fil-092 | Coil, Heater, Bed Regenerator | fits fil.regenerator | — |
| fil-093 | Pump, Vacuum, Bed Regenerator | fits fil.regenerator | — |
| fil-094 | Kit, Charcoal Kiln | installs fil.kiln | — |
| fil-095 | Kit, Resin Vat | installs fil.resinvat | — |
| fil-096 | Kit, Membrane Caster | installs fil.caster | — |
| fil-097 | Kit, Cartridge Packer | installs fil.packer | — |
| fil-098 | Kit, Filter Washer | installs fil.washer | — |
| fil-099 | Kit, Filter Pleater | installs fil.pleater | — |
| fil-100 | Kit, Bed Regenerator | installs fil.regenerator | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| char crop straw | fil.kiln | 240 | 3 grn-009, 1 pwr-001 | 2 fil-021, 1 gas-002 | — |
| press pyrolysis carbon | fil.kiln | 60 | 2 gas-024, 1 pwr-001 | 1 fil-021 | — |
| activate charcoal | fil.kiln | 120 | 2 fil-021, 1 wat-012, 2 pwr-001 | 2 chm-005 | — |
| reactivate spent carbon | fil.kiln | 120 | 2 fil-022, 1 wat-012, 2 pwr-001 | 2 chm-005 | — |
| pellet activated carbon | fil.kiln | 60 | 2 chm-005, 1 pol-025, 1 pwr-001 | 2 fil-076 | — |
| char carbon cloth | fil.kiln | 180 | 1 fib-004, 1 wat-012, 2 pwr-001 | 1 fil-077 | — |
| calcine zeolite powder | fil.kiln | 120 | 2 ore-009, 1 chm-027, 1 chm-002, 2 pwr-001 | 2 fil-023 | — |
| pellet zeolite | fil.kiln | 90 | 3 fil-023, 1 pwr-001 | 3 fil-024 | — |
| fire molecular sieve beads | fil.kiln | 120 | 3 fil-024, 2 pwr-001 | 2 fil-025 | — |
| burn off a spent oxidiser bed | fil.kiln | 180 | 1 fil-059, 2 pwr-001 | 1 fil-058 | — |
| polymerise ion exchange resin | fil.resinvat | 120 | 2 pol-001, 1 chm-001, 2 pwr-001 | 3 fil-031 | — |
| regenerate spent resin with brine | fil.resinvat | 60 | 3 fil-032, 2 wat-011 | 3 fil-031, 1 chm-086 | — |
| bead silica gel | fil.resinvat | 30 | 2 chm-028, 1 pwr-001 | 2 fil-033 | — |
| coat amine sorbent beads | fil.resinvat | 120 | 2 fil-033, 1 chm-003, 1 pwr-001 | 2 fil-026 | — |
| granulate lithium hydroxide | fil.resinvat | 60 | 2 chm-013, 1 pwr-001 | 2 fil-027 | — |
| granulate soda lime | fil.resinvat | 60 | 2 chm-017, 1 chm-002, 1 pwr-001 | 3 fil-028 | — |
| recover lithium from spent granules | fil.resinvat | 120 | 2 fil-030, 1 pwr-001 | 2 chm-014 | — |
| slake spent soda lime | fil.resinvat | 60 | 2 fil-029, 1 wat-009 | 1 chm-011 | — |
| press purification tablets | fil.resinvat | 30 | 1 chm-039, 1 pwr-001 | 6 fil-053 | — |
| mix membrane dope | fil.caster | 60 | 2 pol-018, 1 chm-033 | 2 fil-039 | — |
| cast membrane sheet | fil.caster | 90 | 2 fil-039, 1 fil-074, 1 pwr-001 | 2 fil-040, 1 chm-084 | — |
| spin hollow fibres | fil.caster | 120 | 2 fil-039, 1 pwr-001 | 1 fil-041, 1 chm-084 | — |
| roll a reverse osmosis membrane | fil.caster | 90 | 2 fil-040, 1 fil-042, 1 pwr-001 | 1 fil-015 | — |
| bundle a reclaimer ultrafilter | fil.caster | 60 | 1 fil-041, 1 fil-042, 1 pwr-001 | 1 fil-049 | — |
| make empty filter housings | fil.packer | 30 | 1 pol-045, 1 fil-075 | 1 fil-042 | — |
| cut filter gasket rings | fil.packer | 15 | 1 pol-052 | 4 fil-075 | — |
| pack a zeolite scrubber bed | fil.packer | 45 | 3 fil-025, 1 fil-042 | 1 fil-001 | — |
| pack an amine scrubber bed | fil.packer | 45 | 3 fil-026, 1 fil-042 | 1 fil-003 | — |
| pack a lithium hydroxide canister | fil.packer | 30 | 3 fil-027, 1 pak-005 | 1 fil-005 | — |
| pack a soda lime canister | fil.packer | 30 | 3 fil-028, 1 pak-005 | 1 fil-019 | — |
| pack a sediment water cartridge | fil.packer | 30 | 2 fil-035, 1 fil-042 | 1 fil-011 | — |
| pack a carbon water cartridge | fil.packer | 30 | 2 fil-076, 1 fil-042 | 1 fil-013 | — |
| pack an ion exchange cartridge | fil.packer | 30 | 2 fil-031, 1 fil-042 | 1 fil-017 | — |
| pack an electrolyser feed polisher | fil.packer | 30 | 2 fil-031, 1 fil-042 | 1 fil-078 | — |
| pack a sand filter pack | fil.packer | 30 | 3 fil-035, 1 met-057 | 1 fil-072 | — |
| pack a charcoal odour filter | fil.packer | 30 | 2 fil-076, 1 fil-037 | 1 fil-009 | — |
| pack an ammonia sorbent bed | fil.packer | 45 | 2 fil-024, 1 chm-001, 1 fil-042 | 1 fil-060 | — |
| pack a separator sieve bed | fil.packer | 45 | 3 fil-025, 1 fil-042 | 1 fil-070 | — |
| pack a catalytic oxidiser bed | fil.packer | 45 | 1 chm-077, 1 fil-042 | 1 fil-058 | — |
| fill odour absorber sachets | fil.packer | 15 | 1 fil-076, 2 pak-015 | 2 fil-056 | — |
| make filter straws | fil.packer | 30 | 1 fil-076, 1 fil-041, 1 pol-008 | 2 fil-051 | — |
| lay filter fibre mat | fil.pleater | 60 | 2 cer-003, 1 pwr-001 | 2 fil-037 | — |
| roll hepa media | fil.pleater | 60 | 2 cer-025, 1 pol-062, 1 pwr-001 | 1 fil-073 | — |
| pleat hepa media | fil.pleater | 45 | 1 fil-073, 1 pwr-001 | 2 fil-038 | — |
| cut membrane support mesh | fil.pleater | 20 | 1 fib-073 | 2 fil-074 | — |
| build a cabin hepa filter | fil.pleater | 45 | 2 fil-038, 1 fil-042, 1 fil-075 | 1 fil-007 | — |
| build an electrostatic air filter | fil.pleater | 60 | 1 fil-037, 1 met-058, 1 ecp-010, 1 fil-042 | 1 fil-062 | — |
| cut life support prefilter mats | fil.pleater | 20 | 1 fil-037 | 2 fil-045 | — |
| cut condenser dust screens | fil.pleater | 20 | 1 met-057, 1 fil-037 | 2 fil-047 | — |
| sew meltwater filter socks | fil.pleater | 20 | 1 fib-005 | 2 fil-066 | — |
| make a tap filter insert | fil.pleater | 20 | 1 fil-076, 1 fil-037, 1 fil-042 | 1 fil-068 | — |
| make a compressor intake filter | fil.pleater | 20 | 1 fil-037, 1 fil-075 | 1 fil-080 | — |
| soak a scrubber curtain | fil.pleater | 45 | 1 fib-004, 2 fil-027 | 1 fil-064 | — |
| make dust masks | fil.pleater | 20 | 1 fil-077, 1 fib-006 | 3 fil-054 | — |
| grade filter sand | fil.washer | 30 | 3 ore-050, 2 wat-002 | 3 fil-035, 1 wat-036 | — |
| backwash fouled sand | fil.washer | 30 | 3 fil-036, 2 wat-002 | 3 fil-035, 1 fil-043, 1 wat-036 | — |
| wash clogged prefilter mats | fil.washer | 30 | 2 fil-046, 2 wat-044 | 2 fil-045, 1 fil-044, 2 wat-036 | — |
| wash clogged dust screens | fil.washer | 30 | 2 fil-048, 2 wat-044 | 2 fil-047, 1 fil-044, 2 wat-036 | — |
| wash a dirty electrostatic filter | fil.washer | 30 | 1 fil-063, 2 wat-044 | 1 fil-062, 1 fil-044, 2 wat-036 | — |
| wash clogged filter socks | fil.washer | 20 | 2 fil-067, 2 wat-044 | 2 fil-066, 1 fil-043, 2 wat-036 | — |
| clean a fouled osmosis membrane | fil.washer | 60 | 1 fil-016, 1 chm-065, 2 wat-001 | 1 fil-015, 2 wat-036 | — |
| clean a fouled ultrafilter | fil.washer | 60 | 1 fil-050, 1 chm-037, 2 wat-001 | 1 fil-049, 2 wat-036 | — |
| empty clogged sediment cartridges | fil.washer | 20 | 2 fil-012 | 2 fil-042, 1 fil-036 | — |
| empty spent carbon water cartridges | fil.washer | 20 | 2 fil-014 | 2 fil-042, 1 fil-022 | — |
| empty exhausted ion exchange cartridges | fil.washer | 20 | 2 fil-018 | 2 fil-042, 2 fil-032 | — |
| empty an exhausted feed polisher | fil.washer | 20 | 1 fil-079 | 1 fil-042, 1 fil-032 | — |
| empty spent charcoal filters | fil.washer | 20 | 2 fil-010 | 1 fil-022, 1 scr-005 | — |
| empty spent hydroxide canisters | fil.washer | 20 | 2 fil-006 | 2 pak-006, 2 fil-030 | — |
| empty spent soda lime canisters | fil.washer | 20 | 2 fil-020 | 2 pak-006, 2 fil-029 | — |
| strip clogged hepa filters | fil.washer | 20 | 2 fil-008 | 2 fil-042, 1 fil-044 | — |
| strip clogged intake filters | fil.washer | 20 | 2 fil-081 | 2 fil-075, 1 fil-044 | — |
| strip spent tap filters | fil.washer | 20 | 2 fil-069 | 1 fil-022, 1 scr-002 | — |
| strip used filter straws | fil.washer | 20 | 3 fil-052 | 1 fil-022, 1 scr-002 | — |
| empty spent odour sachets | fil.washer | 15 | 4 fil-057 | 2 fil-022, 4 pak-016 | — |
| strip a saturated scrubber curtain | fil.washer | 20 | 1 fil-065 | 1 fil-030, 1 scr-005 | — |
| slurry captured cabin dust | fil.washer | 20 | 3 fil-044, 1 wat-002 | 1 fil-043 | — |
| bag filter sludge for treatment | crew | 10 | 2 fil-043 | 1 san-058 | — |
| bin used dust masks | crew | 5 | 4 fil-055 | 1 scr-005 | — |
| drink through a filter straw | crew | 5 | 2 wat-002, 1 fil-051 | 1 fil-052 | hydration +10, bladder +10 |
| bake out a saturated zeolite bed | fil.regenerator | 120 | 1 fil-002, 2 pwr-001 | 1 fil-001, 2 gas-002 | — |
| bake out a saturated amine bed | fil.regenerator | 90 | 1 fil-004, 2 pwr-001 | 1 fil-003, 2 gas-002 | — |
| bake out a saturated sieve bed | fil.regenerator | 120 | 1 fil-071, 2 pwr-001 | 1 fil-070, 1 gas-002 | — |
| dry saturated silica gel | fil.regenerator | 60 | 3 fil-034, 1 pwr-001 | 3 fil-033, 1 wat-002 | — |
| strip a saturated ammonia sorbent | fil.regenerator | 90 | 1 fil-061, 1 pwr-001 | 1 fil-060, 1 chm-003 | — |
| make a kiln retort | any.bench | 90 | 1 met-034, 1 cer-006 | 1 fil-082 | — |
| make a kiln heating coil | any.bench | 45 | 1 met-047, 1 cer-035 | 1 fil-083 | — |
| make a resin vat stirrer | any.bench | 45 | 1 met-049, 1 mec-010 | 1 fil-084 | — |
| grind a caster doctor blade | any.bench | 45 | 1 met-034 | 1 fil-085 | — |
| make a casting belt | any.bench | 45 | 1 pol-036, 1 fib-012 | 1 fil-086 | — |
| make a packer press ram | any.bench | 60 | 1 met-008, 1 mec-043 | 1 fil-087 | — |
| make a filter washer spray bar | any.bench | 30 | 1 met-056, 2 mec-049 | 1 fil-088 | — |
| make a washer backwash pump | any.bench | 45 | 1 mec-008, 1 pol-009 | 1 fil-089 | — |
| make a pleater fold bar | any.bench | 30 | 1 met-008, 1 met-042 | 1 fil-090 | — |
| make a pleater glue head | any.bench | 30 | 1 thm-004, 1 mec-049 | 1 fil-091 | — |
| make a regenerator heater coil | any.bench | 45 | 1 met-047, 1 cer-035 | 1 fil-092 | — |
| make a regenerator vacuum pump | any.bench | 45 | 1 mec-039, 1 pol-009 | 1 fil-093 | — |
| pack a charcoal kiln kit | any.bench | 120 | 1 fur-001, 1 fil-082, 1 fil-083, 1 cer-006 | 1 fil-094 | — |
| pack a resin vat kit | any.bench | 90 | 1 fur-001, 1 fil-084, 1 met-034 | 1 fil-095 | — |
| pack a membrane caster kit | any.bench | 120 | 1 fur-001, 1 fil-085, 1 fil-086 | 1 fil-096 | — |
| pack a cartridge packer kit | any.bench | 90 | 1 fur-001, 1 fil-087 | 1 fil-097 | — |
| pack a filter washer kit | any.bench | 90 | 1 fur-001, 1 fil-088, 1 fil-089 | 1 fil-098 | — |
| pack a filter pleater kit | any.bench | 90 | 1 fur-001, 1 fil-090, 1 fil-091 | 1 fil-099 | — |
| pack a bed regenerator kit | any.bench | 120 | 1 fur-001, 1 fil-092, 1 fil-093 | 1 fil-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| fil.kiln | Chars straw into charcoal, activates and reactivates carbon, chars carbon cloth, fires zeolite into sieve beads and burns off spent oxidiser beds. | KILN HOT. CO HAZARD. VENT TO LIFE SUPPORT BEFORE OPENING. |
| fil.resinvat | Casts ion exchange resin, silica gel and sorbent granules, presses purification tablets and regenerates spent resin with brine. | Stir clockwise. Nobody remembers why. Nobody risks finding out. |
| fil.caster | Mixes membrane dope, casts membrane sheets and spins hollow fibres, then rolls them into osmosis membranes and ultrafilters. | Belt tension set, rev 6. Blade gap checked with feeler gauge. Feeler gauge missing since. |
| fil.packer | Packs media into housings as scrubber beds, canisters, water cartridges, sachets and straws, and makes housings and gaskets. | Cartridge output is counted per shift. Shortfall is carried to the next shift. Ref 4400/C. |
| fil.washer | Backwashes mats, screens, socks and sand, cleans membranes, and empties spent cartridges and canisters for their housings. | Wash water is not drinking water at any stage. Proc 55 applies to the bucket as well. |
| fil.pleater | Lays fibre mat and pleats HEPA media, then builds air filters, prefilters, screens, socks, curtains and masks. | GLUE HEAD HOT. FOLD BAR CRUSH POINT. GLOVES ON. |
| fil.regenerator | Bakes saturated scrubber and sieve beds back to work, dries silica gel and strips ammonia from sorbent. | Beds are regenerated, not replaced. Replacement is a cost centre. Notice 700/R. |
| fil-001 | A zeolite bed placed in life support that draws carbon dioxide from the cabin air until it saturates. | Carbon dioxide removal is a station duty. Headaches are not a valid excuse. Ref 0101/Z. |
| fil-002 | A zeolite bed full of carbon dioxide, baked out in the bed regenerator for reuse. | SATURATED. RETURN TO REGENERATOR. DO NOT DISCARD. |
| fil-003 | An amine bed placed in life support that scrubs carbon dioxide faster than zeolite, until it saturates. | Higher grade bed. Issued on merit. Merit is not defined. |
| fil-004 | An amine bed loaded with carbon dioxide, baked clean in the bed regenerator. | RETURN TO ATMOS. NOT TO THE BIN. |
| fil-005 | A single-use canister that absorbs a large amount of carbon dioxide at once, for emergencies; leaves a spent canister. | Open when the headache starts. Not when the shouting starts. Proc 5E. |
| fil-006 | A spent hydroxide canister, emptied for the canister and the spent granules. | Emptied, logged, returned. Granule weight recorded for recovery, rev 2. |
| fil-007 | A pleated filter placed in life support that keeps the cabin air clean of dust until it clogs. | Particulate capture is not reported to the operator. The operator would not want it reported. |
| fil-008 | A clogged HEPA filter, stripped for its housing and the captured dust. | CLOGGED. HANDLE WITH MASK. STRIP AT FILTER WASHER. |
| fil-009 | A charcoal filter placed in life support that removes smells from the cabin air. | Odour complaints between stations cannot be routed. Install this instead. Notice 09/D. |
| fil-010 | A charcoal filter that has stopped absorbing, emptied so the carbon can be reactivated. | Smells of everything it stopped. Opened with care, rev 1. |
| fil-011 | A sand cartridge fitted to the water purifier that catches grit and sediment. | First stage. Grit goes no further. Grit is logged. |
| fil-012 | A sediment cartridge choked with silt, emptied for the housing and the fouled sand. | Shake it. Hear the regolith. Then stop shaking it. |
| fil-013 | A carbon cartridge fitted to the water purifier that strips taste and organics from water. | Makes reclaimed water taste like water. Origin of water not to be discussed. Ref 1313. |
| fil-014 | A water cartridge with its carbon used up, emptied so the carbon can be reactivated. | Housing reusable. Carbon reactivatable. Nothing is thrown away here. |
| fil-015 | A rolled membrane fitted to the urine reclaimer that passes water and holds back salts and dirt. | PRESSURE SIDE MARKED. INSTALL ARROW TO FLOW. |
| fil-016 | An osmosis membrane fouled with scale and film, restored by a chemical wash. | Flow down by half. Report within the shift on Form 16F. Patience down by more. |
| fil-017 | A resin cartridge fitted to the water purifier that exchanges hard minerals out of water. | Soft water reduces scale on Company plumbing. Operator benefit is secondary. |
| fil-018 | An exhausted ion exchange cartridge, emptied for its housing and resin. | Exhausted. Empty and regenerate. Do not refit. |
| fil-019 | A single-use canister that absorbs carbon dioxide when the scrubbers fall behind; weaker and cheaper than hydroxide. | Budget alternative, approved by Procurement. Procurement does not breathe this air. |
| fil-020 | A used soda lime canister, emptied for the canister and the spent granules. | Warm for an hour after use. Chemical reaction. Not a malfunction. Proc 20. |
| fil-021 | Charred straw or pressed carbon, the raw stock of activated carbon, litter and odour fillings. | Black hands are working hands. Wash before handling food. |
| fil-022 | Activated carbon that has absorbed its fill, reactivated with steam in the charcoal kiln. | RETURN FOR REACTIVATION. CARBON IS NOT CONSUMABLE. |
| fil-023 | Fine zeolite calcined from clay, pressed into pellets or odour blocks. | Looks like flour. Is not flour. Incident 2318 refers. |
| fil-024 | Pressed zeolite pellets, fired into sieve beads or packed into ammonia beds. | Little grey pills for a large grey ship. |
| fil-025 | Fired molecular sieve beads that hold carbon dioxide; the filling of zeolite and separator beds. | Sieves molecules. Does not sieve rumours. Rumours are a separate department. |
| fil-026 | Silica beads coated with amine, the filling of amine scrubber beds. | SKIN IRRITANT. HANDLE WITH GLOVES. |
| fil-027 | Lithium hydroxide granules for canisters and scrubber curtains. | Keep dry. Keep sealed. Keep counted. Lithium is a controlled stock, Ref 2700/L. |
| fil-028 | Soda lime granules, packed into canisters that absorb carbon dioxide. | Issued by the scoop. Scoop issued once. Replacement scoop on Form 28S. |
| fil-029 | Soda lime spent on carbon dioxide, slaked back into a useful chemical. | Chalk, more or less. Recorded as feedstock, not waste. |
| fil-030 | Lithium hydroxide granules gone to carbonate, from which the lithium can be recovered. | There is lithium in there still. The Company would like it back. |
| fil-031 | Ion exchange resin beads, the filling of water cartridges and electrolyser feed polishers. | Small amber beads. Spilled beads are a slip hazard and a stock loss. |
| fil-032 | Resin beads loaded with minerals, regenerated by a brine soak. | Soak in salt to make it release salt. Procedure 32 does not explain it either. |
| fil-033 | Drying beads that pull moisture from compressed air, and the core of amine sorbent beads. | DO NOT EAT. PRINTED IN SIX LANGUAGES AND ONE DIAGRAM. |
| fil-034 | Silica gel soaked through with water, dried in the bed regenerator for reuse. | Cloudy beads. Bake until clear. Recover the water, Proc 34. |
| fil-035 | Graded sand that strains grit from water in cartridges, packs and grey water beds. | Ground from rock outside to clean water inside. Freight cost absorbed by the station. |
| fil-036 | Filter sand clogged with silt and sludge, backwashed for reuse. | Brown, damp, destined for the washer. |
| fil-037 | A fibre mat cut into prefilters, screens, odour filters and other filter parts. | STOCK MATERIAL. CUT TO TEMPLATE. RETURN OFFCUTS. |
| fil-038 | Pleated HEPA paper, framed into a cabin HEPA filter. | More surface area than the hull, folded into a box. Pleat count verified, rev 3. |
| fil-039 | A dissolved polymer dope, cast into membrane sheets or spun into hollow fibres. | Solvent fumes. Ventilate. Headaches are not a reportable injury. Ref 3900/F. |
| fil-040 | A cast membrane sheet on support mesh, rolled into a reverse osmosis membrane. | Hold to light: no holes. Hold to water: all holes. Both results pass. |
| fil-041 | A bundle of hollow fibres for ultrafilters and filter straws. | Fibre count per bundle is not verifiable. It is accepted on trust. Rare, here. |
| fil-042 | A blank filter housing, packed with media into beds and cartridges, and emptied for reuse. | Housings outlive filters. Some outlive contracts. Serial stamped on base. |
| fil-043 | Wet sludge washed out of filters, bagged and sent on to waste treatment. | BIOHAZARD POSSIBLE. BAG AND TAG FOR TREATMENT. |
| fil-044 | Dust beaten out of air filters and screens, slurried into sludge. | Mostly skin. Do not think about whose. |
| fil-045 | A coarse mat fitted to life support that guards it from lint and dust. | Change before life support requests it. Life support does not request twice. |
| fil-046 | A prefilter mat thick with lint, washed for reuse. | Lint, hair and one fibre of unknown origin. Origin not investigated. |
| fil-047 | A fine screen fitted to the moisture condenser that keeps dust off its coils. | Clean screen, more water. Water yield is audited. Ref 4700/W. |
| fil-048 | A condenser dust screen caked with dust, washed for reuse. | Frosted with lint. Not the festive kind. No kind is festive here. |
| fil-049 | A hollow fibre filter fitted to the urine reclaimer that stops bacteria and fine particles. | STERILE BARRIER. DO NOT TOUCH FIBRE FACE. |
| fil-050 | An ultrafilter fouled with film, restored by a chemical wash. | Smells of the reclaimer's worst day. Clean within one shift, Proc 50. |
| fil-051 | A personal straw that makes raw water safe to sip straight from the source. | Emergency issue. Use when the purifier fails. The purifier will fail. |
| fil-052 | A used filter straw, stripped for its carbon and plastic. | One good drink in it. Drink taken. Return for stripping. |
| fil-053 | An iodine tablet that makes raw water drinkable, slowly and with an aftertaste. | Drop. Wait. Drink. Grimace. Taste complaints to Form 53T. |
| fil-054 | A carbon dust mask worn to keep fine particles and fumes out of the lungs, reducing toxin. | MASK REQUIRED IN FOUNDRY, KILN AND WASHER AREAS. |
| fil-055 | A used dust mask, binned with others for fabric scrap. | Grey outside, pink inside. That is the correct way round. |
| fil-056 | A small carbon sachet that freshens a stale cabin when opened. | Hang near the source. Do not name the source in the log. |
| fil-057 | A spent odour sachet, emptied for its carbon and the pouch. | Full of what is no longer smelled. Empty at the filter washer. |
| fil-058 | A catalyst bed placed in life support that burns trace gases out of the cabin air. | Trace contaminant control is a contract obligation. The bed meets it. Ref 5800/T. |
| fil-059 | A catalyst bed fouled with deposits, burnt clean in the charcoal kiln. | Glazed over, rev 4. Into the kiln. Out again, rev 5. |
| fil-060 | A zeolite bed placed in life support that draws ammonia out of the cabin air. | Keeps the toilet's output out of the bunk's air. Mostly. |
| fil-061 | A saturated ammonia bed; the bed regenerator strips the ammonia back out as feedstock. | Odour in, feedstock out. Recovery credited to Chemicals. Notice 61/A. |
| fil-062 | A charged filter placed in life support that pulls dust from the cabin air, and is washed for reuse. | CHARGED PLATES. ISOLATE BEFORE HANDLING. |
| fil-063 | An electrostatic filter furred with dust, washed for reuse. | Still charged. Still filthy. Discharge, then wash. |
| fil-064 | A hanging curtain soaked in hydroxide that takes up a little carbon dioxide while it hangs. | Low-budget scrubbing. Approved for stations without a scrubber bed. Proc 64. |
| fil-065 | A saturated scrubber curtain, stripped for spent granules and fabric scrap. | Stiff as card. Taken down, logged, stripped. |
| fil-066 | A cloth sock fitted to the ice melter that catches grit from the meltwater. | Regolith stays in the sock. Water goes in the tank. Sock goes in the washer. |
| fil-067 | A meltwater sock clogged with grit, washed for reuse. | Heavy with what was melted. Weight logged as recovered solids. |
| fil-068 | A carbon insert fitted to the washbasin tap that freshens the water it runs. | Small, cheap, and the first thing anyone misses. Ref 6800/T. |
| fil-069 | A tap filter with its carbon used up, stripped for carbon and plastic. | Tap tastes of tap again. Change insert. |
| fil-070 | A molecular sieve bed fitted to the gas separator that splits air into its gases. | Passes oxygen, holds nitrogen, plays no favourites. Ideal Company conduct. |
| fil-071 | A saturated separator sieve bed, baked out for reuse. | Saturated, not dead. Regenerator queue, slot three. |
| fil-072 | A boxed sand pack fitted to the water purifier that wears into fouled sand. | SAND MEDIA. INSTALL FLOW ARROW DOWN. |
| fil-073 | A roll of fine glass fibre media, pleated into HEPA paper. | Glass fibre. Do not handle bare. Itching is not a reportable injury. |
| fil-074 | A woven mesh that holds a membrane flat while it is cast. | The membrane gets the credit. The mesh does the holding. Familiar arrangement. |
| fil-075 | A rubber ring that seals a filter in its housing so nothing bypasses the media. | Leaks go round the filter, never through. Seal checked, rev 1. |
| fil-076 | Pelleted activated carbon, packed into water cartridges, odour filters, sachets, tap inserts and straws. | More surface inside than outside. Bulk density per Media Spec 76. |
| fil-077 | Charred woven cloth that adsorbs fumes, sewn into dust masks. | BLACK CLOTH. ADSORBENT. STORE SEALED. |
| fil-078 | A resin cartridge fitted to the water electrolyser that strips the last minerals from its feedwater. | Impure feed shortens electrolyser life. Electrolyser life is billed. Ref 7800/E. |
| fil-079 | An exhausted feed polisher, emptied for its housing and resin. | Polished its last litre. Return for emptying. |
| fil-080 | An intake filter fitted to the canister compressor that keeps dust out of it. | Protects a machine valued above the capsule it sits in. Valuation on file. |
| fil-081 | A clogged compressor intake filter, stripped for its gasket rings and dust. | Clogged. Compressor wheezing. Swap now, log after. |
| fil-082 | A replacement retort fitted to the charcoal kiln. | Heat it, seal it, leave it alone. Weld seam checked, rev 2. |
| fil-083 | A replacement heating coil fitted to the charcoal kiln. | Orange when working, black when not. Not a substitute for the meter. |
| fil-084 | A replacement stirrer fitted to the resin vat. | If it stops, the resin sets. Set resin is charged to the station. Notice 84/S. |
| fil-085 | A replacement doctor blade fitted to the membrane caster, spreading dope to an even film. | BLADE EDGE. DO NOT WIPE BY HAND. |
| fil-086 | A replacement casting belt fitted to the membrane caster, carrying cast membrane through it. | Round and round, sheet after sheet. Tracking adjusted, rev 3. |
| fil-087 | A replacement press ram fitted to the cartridge packer. | Packs firm. Packs to spec. Packs fingers too, if offered. |
| fil-088 | A replacement spray bar fitted to the filter washer. | Blocked jets mean dirty mats. Clear with wire, not with teeth. |
| fil-089 | A replacement backwash pump fitted to the filter washer. | Pushes water the wrong way, on purpose. Impeller replaced, rev 2. |
| fil-090 | A replacement fold bar fitted to the filter pleater. | Crease. Crease. Crease. Crease. Shift ends. |
| fil-091 | A replacement glue head fitted to the filter pleater. | HOT END. MARKED HOT. IT IS HOT. |
| fil-092 | A replacement heater coil fitted to the bed regenerator. | No heat, no bake-out, no breathing. Hold one spare per Atmos Directive 92. |
| fil-093 | A replacement vacuum pump fitted to the bed regenerator. | Pulls the gas out so the bed can work again. Oil changed, rev 4. |
| fil-094 | A packed charcoal kiln, ready to install. | Assembly: two hours. Smell: permanent. Neither is compensated. |
| fil-095 | A packed resin vat, ready to install. | COF HYDRO EQUIPMENT. LIFT FROM BASE ONLY. |
| fil-096 | A packed membrane caster, ready to install. | Unpack in a clean area. Clean area to be provided by the operator. |
| fil-097 | A packed cartridge packer, ready to install. | Dispatched under Filtration Order 97. Bolts counted twice. Still one short. |
| fil-098 | A packed filter washer, ready to install. | Drain fitting included. Use the drain fitting. Floor damage is billed. |
| fil-099 | A packed filter pleater, ready to install. | CRATE CONTAINS SHARP EDGES AND HOT PARTS ONCE ASSEMBLED. |
| fil-100 | A packed bed regenerator, ready to install. | Turns a stock of beds into a supply of them. Supply is the station's duty. |
