# Radiation & Toxin Treatment — `rad`

What keeps dose and toxin down. Iodide, Prussian blue, chelators, clay and binders are swallowed or injected and take
the dose or the poison down at once; lead, boron and water become aprons, vests, liners and wall panels that hold a
small rate while worn or fitted. Badges and counters tell the crew how bad it is. Worn garments come back contaminated
and the decon station strips them to scrap lead; wipes, runoff and spent resin are sealed into `pak`'s drums as
radwaste and passed out through the hatch.

## Devices

| id | device | role | cells |
|---|---|---|---|
| rad.chemlab | RP300 Isotope Chemlab | med | 2x2 |
| rad.filler | RP120 Dose Filler | med | 2x1 |
| rad.caster | RP450 Lead Caster | med | 2x2 |
| rad.loom | RP220 Shield Loom | med | 2x1 |
| rad.assembler | RP150 Detector Bench | med | 2x1 |
| rad.decon | RP80 Decon Station | med | 2x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| rad-001 | Tablet, Potassium Iodide | dose -10, leaves 1 pak-018 | 2160 h → med-049 |
| rad-002 | Badge, Dosimeter | stress -0.5/h | 720 h → rad-049 |
| rad-003 | Apron, Lead | dose -2/h | 720 h → rad-046 |
| rad-004 | Blanket, Radiation Shield | dose -2/h, cabin.heat +1/h | 1000 h → rad-046 |
| rad-005 | Capsule, Prussian Blue | dose -15, toxin -5, bowel +5, leaves 1 pak-018 | 2160 h → med-049 |
| rad-006 | Ampoule, Chelation | dose -40, toxin -20, pain +5, fitness -5, leaves 1 pak-020 | 1080 h → med-051 |
| rad-007 | Wipe, Decon | dose -5, hygiene +3, leaves 1 rad-047 | — |
| rad-008 | Counter, Geiger | stress -1/h | 2000 h → scr-003 |
| rad-009 | Drink Mix, Detox | toxin -15, hydration +8, bladder +8, leaves 1 pak-016 | 2160 h → med-049 |
| rad-010 | Shot, Radioprotectant | dose -35, toxin +5, pain +3, leaves 1 sup-045 | 1080 h → med-051 |
| rad-011 | Tablet, Chelator, Heavy Metal | toxin -20, fitness -2, leaves 1 pak-018 | 2160 h → med-049 |
| rad-012 | Tablet, Radioprotectant | dose -20, toxin +5, satiety -5, leaves 1 pak-018 | 2160 h → med-049 |
| rad-013 | Capsule, Antioxidant | dose -5, immunity +3, leaves 1 pak-018 | 1440 h → med-049 |
| rad-014 | Tablet, Marrow Support | dose -8, immunity +10, leaves 1 pak-018 | 1440 h → med-049 |
| rad-015 | Tablet, Radiation Sickness | toxin -8, health +5, pain -3, leaves 1 pak-018 | 1440 h → med-049 |
| rad-016 | Syrup, Iodide | dose -8, leaves 1 pak-004 | 1440 h → med-050 |
| rad-017 | Pack, Cesium Purge | dose -25, toxin -10, bowel +10, leaves 1 pak-016 | 2160 h → med-049 |
| rad-018 | Foam, Decon | dose -8, cabin.clean +5, leaves 1 rad-048 | — |
| rad-019 | Gel, Decon Shower | dose -10, hygiene +10, leaves 1 rad-048 | — |
| rad-020 | Cream, Skin Shield | dose -6, hygiene +2, leaves 1 pak-012 | 1440 h → med-052 |
| rad-021 | Drink, Chelation | dose -12, toxin -10, hydration +5, bladder +5, leaves 1 pak-004 | 720 h → med-050 |
| rad-022 | Sachet, Toxin Binder | toxin -10, bowel +5, leaves 1 pak-016 | 2160 h → med-049 |
| rad-023 | Kit, Storm | dose -30, stress -10, leaves 1 pak-018, leaves 1 rad-047 | — |
| rad-024 | Kit, Decon, Emergency | dose -20, hygiene +10, leaves 2 rad-047, leaves 1 rad-048 | — |
| rad-025 | Pack, Decon Wipe, Hand | dose -12, hygiene +6, leaves 2 rad-047 | — |
| rad-026 | Drink, Detox, Bentonite | toxin -12, bowel +5, hydration +5, bladder +5, leaves 1 pak-004 | — |
| rad-027 | Collar, Thyroid | dose -1/h | 1000 h → rad-046 |
| rad-028 | Vest, Lead | dose -3/h, fitness -0.5/h | 720 h → rad-046 |
| rad-029 | Cap, Shielded | dose -1/h | 720 h → rad-046 |
| rad-030 | Gloves, Shielded | dose -1/h | 500 h → rad-046 |
| rad-031 | Suit, Radiation | dose -5/h, fitness -1/h, stress +1/h | 500 h → rad-046 |
| rad-032 | Overalls, Hazmat | dose -1/h, toxin -1/h | 240 h → rad-046 |
| rad-033 | Mask, Respirator | toxin -1/h | 336 h → rad-046 |
| rad-034 | Liner, Sleep Pod, Shielded | dose -2/h, rest +1/h | 1500 h → rad-046 |
| rad-035 | Pillow, Shielded | dose -1/h, rest +0.5/h | 1000 h → rad-046 |
| rad-036 | Panel, Water Wall | dose -2/h | 2000 h → scr-004 |
| rad-037 | Panel, Wall, Borated | dose -3/h | 2000 h → scr-004 |
| rad-038 | Pane, Window, Leaded | dose -2/h, cabin.light +1/h | 3000 h → scr-004 |
| rad-039 | Panel, Storm Shelter | dose -5/h | 2000 h → scr-004 |
| rad-040 | Mat, Floor Shield | dose -1/h | 1500 h → scr-004 |
| rad-041 | Liner, Locker, Shielded | dose -1/h | 1500 h → scr-004 |
| rad-042 | Visor, Cosmic Ray | dose -1/h | 1000 h → rad-046 |
| rad-043 | Dosimeter, Pocket | stress -1/h | 1500 h → scr-003 |
| rad-044 | Monitor, Radiation, Area | stress -2/h | 2000 h → scr-003 |
| rad-045 | Curtain, Bunk, Lead | dose -2/h, stress -0.5/h | 1500 h → rad-046 |
| rad-046 | Garment, Shield, Contaminated | — | — |
| rad-047 | Wipe, Contaminated | — | — |
| rad-048 | Runoff, Contaminated | — | — |
| rad-049 | Badge, Dosimeter, Spent | — | — |
| rad-050 | Lead, Scrap | — | — |
| rad-051 | Resin, Decon, Spent | — | — |
| rad-052 | Gel, Decon, Hand | dose -4, hygiene +4, leaves 1 pak-012 | — |
| rad-053 | Drum, Radwaste, Sealed | — | — |
| rad-054 | Powder, Ferric Pigment | — | — |
| rad-055 | Pigment, Prussian Blue | — | — |
| rad-056 | Base, Chelator | — | — |
| rad-057 | Binder, Cesium | — | — |
| rad-058 | Concentrate, Antioxidant | — | 720 h |
| rad-059 | Base, Marrow Support | — | — |
| rad-060 | Base, Radioprotectant | — | — |
| rad-061 | Base, Detox Mix | — | — |
| rad-062 | Solution, Decon | — | — |
| rad-063 | Resin, Decon Ion | — | — |
| rad-064 | Base, Shield Gel | — | — |
| rad-065 | Shot, Lead, Shielding | — | — |
| rad-066 | Foil, Lead Shielding | — | — |
| rad-067 | Plate, Lead Shield | — | — |
| rad-068 | Laminate, Lead Rubber | — | — |
| rad-069 | Frit, Boron | — | — |
| rad-070 | Compound, Borated | — | — |
| rad-071 | Sheet, Shield, Borated | — | — |
| rad-072 | Foam, Neutron Shield | — | — |
| rad-073 | Glass, Viewing, Leaded | — | — |
| rad-074 | Fabric, Shield, Base | — | — |
| rad-075 | Thread, Shield | — | — |
| rad-076 | Weave, Shield, Reflective | — | — |
| rad-077 | Shell, Shield Panel | — | — |
| rad-078 | Bladder, Water Wall | — | — |
| rad-079 | Film, Dosimeter | — | — |
| rad-080 | Casing, Dosimeter Badge | — | — |
| rad-081 | Tube, Geiger | — | — |
| rad-082 | Crystal, Scintillator | — | — |
| rad-083 | Circuit, Radiation Detector | — | — |
| rad-084 | Housing, Geiger Counter | — | — |
| rad-085 | Buzzer, Dose Alarm | — | — |
| rad-086 | Strap, Lead Apron | — | — |
| rad-087 | Substrate, Decon Wipe | — | — |
| rad-088 | Cartridge, Respirator | — | — |
| rad-089 | Seal, Pump, Isotope Chemlab | fits rad.chemlab | 1000 h → scr-004 |
| rad-090 | Set, Piston, Dose Filler | fits rad.filler | 1500 h → scr-001 |
| rad-091 | Liner, Crucible, Lead Caster | fits rad.caster | 720 h → scr-004 |
| rad-092 | Shuttle, Shield Loom | fits rad.loom | 2000 h → scr-001 |
| rad-093 | Fixture, Detector Bench | fits rad.assembler | 2000 h → scr-001 |
| rad-094 | Spray Head, Decon Station | fits rad.decon | 1000 h → scr-004 |
| rad-095 | Kit, Isotope Chemlab | installs rad.chemlab | — |
| rad-096 | Kit, Dose Filler | installs rad.filler | — |
| rad-097 | Kit, Lead Caster | installs rad.caster | — |
| rad-098 | Kit, Shield Loom | installs rad.loom | — |
| rad-099 | Kit, Detector Bench | installs rad.assembler | — |
| rad-100 | Kit, Decon Station | installs rad.decon | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| precipitate ferric pigment | rad.chemlab | 60 | 1 chm-026, 1 pwr-001 | 2 rad-054 | — |
| dissolve iron for pigment | rad.chemlab | 90 | 1 met-060, 1 chm-009, 1 pwr-001 | 2 rad-054 | — |
| precipitate prussian blue | rad.chemlab | 120 | 1 rad-054, 1 chm-002, 1 pwr-001 | 1 rad-055 | — |
| dilute chelator base | rad.chemlab | 60 | 1 chm-063, 1 wat-003, 1 pwr-001 | 2 rad-056 | — |
| bind cesium binder | rad.chemlab | 90 | 1 rad-055, 1 rad-056, 1 pwr-001 | 2 rad-057 | — |
| extract citrus antioxidants | rad.chemlab | 90 | 2 frt-060, 1 chm-004, 1 pwr-001 | 1 rad-058 | — |
| fortify antioxidants | rad.chemlab | 60 | 1 med-071, 1 chm-065, 1 pwr-001 | 1 rad-058 | — |
| blend marrow support base | rad.chemlab | 60 | 1 rad-058, 1 med-073, 1 pwr-001 | 1 rad-059 | — |
| synthesise radioprotectant | rad.chemlab | 150 | 1 chm-003, 1 chm-022, 1 chm-035, 1 pwr-001 | 1 rad-060 | — |
| blend detox mix base | rad.chemlab | 45 | 1 med-074, 1 ore-075, 1 pwr-001 | 2 rad-061 | — |
| mix decon solution | rad.chemlab | 45 | 1 chm-063, 1 chm-061, 2 wat-001, 1 pwr-001 | 2 rad-062 | — |
| sulfonate decon resin | rad.chemlab | 120 | 1 pol-026, 1 chm-001, 1 pwr-001 | 2 rad-063 | — |
| blend shield gel base | rad.chemlab | 45 | 1 chm-064, 1 chm-059, 1 pwr-001 | 2 rad-064 | — |
| cast lead shot | rad.caster | 60 | 1 met-012, 1 pwr-001 | 4 rad-065 | — |
| recast scrap lead into shot | rad.caster | 60 | 1 rad-050, 1 pwr-001 | 2 rad-065 | — |
| roll lead foil | rad.caster | 60 | 1 met-012, 1 pwr-001 | 3 rad-066 | — |
| cut lead sheet into foil | any.bench | 30 | 1 met-041 | 2 rad-066 | — |
| cast lead shield plate | rad.caster | 90 | 1 met-012, 1 pwr-001 | 1 rad-067 | — |
| recast scrap lead into plate | rad.caster | 90 | 2 rad-050, 1 pwr-001 | 1 rad-067 | — |
| laminate lead rubber | rad.caster | 60 | 1 rad-065, 1 pol-003, 1 pwr-001 | 2 rad-068 | — |
| grind borosilicate frit | rad.chemlab | 60 | 1 cer-014, 1 pwr-001 | 2 rad-069 | — |
| compound borated plastic | rad.chemlab | 90 | 1 rad-069, 1 pol-001, 1 pwr-001 | 2 rad-070 | — |
| press borated sheet | rad.caster | 90 | 2 rad-070, 1 pwr-001 | 1 rad-071 | — |
| foam neutron shield | rad.chemlab | 90 | 1 rad-070, 1 pol-012, 1 pwr-001 | 1 rad-072 | — |
| melt leaded glass | rad.caster | 120 | 1 cer-001, 1 chm-075, 1 pwr-001 | 1 rad-073 | — |
| coat shield fabric | rad.loom | 60 | 1 fib-004, 1 rad-070, 1 pwr-001 | 1 rad-074 | — |
| spin shield thread | rad.loom | 45 | 1 fib-003, 1 rad-066, 1 pwr-001 | 2 rad-075 | — |
| weave reflective shield | rad.loom | 60 | 1 fib-072, 1 rad-075, 1 pwr-001 | 1 rad-076 | — |
| press shield panel shell | rad.caster | 60 | 1 met-007, 1 pwr-001 | 1 rad-077 | — |
| cut fibreglass panel shell | any.bench | 45 | 1 cer-005 | 1 rad-077 | — |
| seal water wall bladder | rad.loom | 45 | 1 pol-031, 1 pwr-001 | 1 rad-078 | — |
| repurpose a water bladder | any.bench | 20 | 1 wat-059 | 1 rad-078 | — |
| coat dosimeter film | rad.chemlab | 45 | 1 pol-002, 1 chm-049, 1 pwr-001 | 4 rad-079 | — |
| mould badge casings | rad.assembler | 30 | 1 pol-015, 1 pwr-001 | 4 rad-080 | — |
| fill geiger tube | rad.assembler | 90 | 1 cer-019, 1 met-006, 1 gas-014, 1 pwr-001 | 1 rad-081 | — |
| grow scintillator crystal | rad.chemlab | 240 | 1 chm-039, 1 chm-002, 1 pwr-001 | 1 rad-082 | — |
| solder detector circuit | rad.assembler | 60 | 1 ecp-005, 1 ecp-061, 1 pwr-001 | 1 rad-083 | — |
| mould counter housing | rad.assembler | 30 | 1 pol-018, 1 pwr-001 | 1 rad-084 | — |
| wire dose alarm buzzer | rad.assembler | 30 | 1 ecp-044, 1 ecp-060 | 1 rad-085 | — |
| sew apron straps | rad.loom | 30 | 1 fib-012, 1 mec-046 | 2 rad-086 | — |
| cut wipe substrate | rad.loom | 30 | 1 fib-068, 1 pwr-001 | 6 rad-087 | — |
| tear rag wipe substrate | any.bench | 20 | 2 scr-005 | 2 rad-087 | — |
| pack respirator cartridge | rad.assembler | 30 | 1 chm-005, 1 pol-015 | 1 rad-088 | — |
| press iodide tablets | rad.filler | 60 | 1 chm-040, 1 med-083, 2 pak-017, 1 pwr-001 | 2 rad-001 | — |
| assemble dosimeter badge | rad.assembler | 20 | 1 rad-080, 1 rad-079 | 1 rad-002 | — |
| read and refill a badge | rad.assembler | 20 | 1 rad-049, 1 rad-079 | 1 rad-002 | stress -2 |
| sew lead apron | rad.loom | 90 | 2 rad-068, 1 rad-086, 1 pwr-001 | 1 rad-003 | — |
| quilt radiation blanket | rad.loom | 90 | 1 rad-074, 1 rad-066, 1 fib-011, 1 pwr-001 | 1 rad-004 | — |
| fill prussian blue capsules | rad.filler | 60 | 1 rad-055, 2 med-084, 2 pak-017, 1 pwr-001 | 2 rad-005 | — |
| seal chelation ampoules | rad.filler | 60 | 1 rad-056, 1 med-087, 1 pak-019, 1 pwr-001 | 1 rad-006 | — |
| soak decon wipes | rad.decon | 20 | 1 rad-087, 1 rad-062 | 4 rad-007 | — |
| assemble geiger counter | rad.assembler | 90 | 1 rad-081, 1 rad-083, 1 rad-084, 1 rad-085 | 1 rad-008 | — |
| pack detox drink mix | rad.filler | 30 | 1 rad-061, 1 ing-003, 2 pak-015 | 2 rad-009 | — |
| load radioprotectant shot | rad.filler | 45 | 1 rad-060, 1 sup-084, 1 sup-075, 1 med-087 | 1 rad-010 | — |
| press chelator tablets | rad.filler | 60 | 1 rad-056, 1 med-083, 2 pak-017, 1 pwr-001 | 2 rad-011 | — |
| press radioprotectant tablets | rad.filler | 60 | 1 rad-060, 1 med-083, 2 pak-017, 1 pwr-001 | 2 rad-012 | — |
| fill antioxidant capsules | rad.filler | 60 | 1 rad-058, 2 med-084, 2 pak-017, 1 pwr-001 | 2 rad-013 | — |
| press marrow support tablets | rad.filler | 60 | 1 rad-059, 1 med-083, 2 pak-017, 1 pwr-001 | 2 rad-014 | — |
| press radiation sickness tablets | rad.filler | 60 | 1 med-070, 1 rad-058, 1 med-083, 2 pak-017, 1 pwr-001 | 2 rad-015 | — |
| compound iodide syrup | rad.chemlab | 30 | 1 chm-040, 1 med-085, 1 pak-003 | 1 rad-016 | — |
| pack cesium purge | rad.filler | 30 | 1 rad-057, 1 rad-061, 2 pak-015 | 2 rad-017 | — |
| foam decon solution | rad.decon | 20 | 2 rad-062, 1 chm-061, 1 pwr-001 | 2 rad-018 | — |
| blend decon shower gel | rad.chemlab | 30 | 1 rad-062, 1 hyg-001 | 1 rad-019 | — |
| tube skin shield cream | rad.chemlab | 30 | 1 rad-064, 1 pak-011 | 1 rad-020 | — |
| bottle chelation drink | rad.chemlab | 30 | 1 rad-056, 1 med-085, 1 pak-003 | 1 rad-021 | — |
| pack toxin binder sachets | rad.filler | 20 | 1 rad-061, 2 pak-015 | 2 rad-022 | — |
| pack storm kit | rad.assembler | 20 | 1 rad-012, 1 rad-001, 1 rad-007, 1 pak-029 | 1 rad-023 | — |
| pack emergency decon kit | rad.assembler | 20 | 2 rad-007, 1 rad-019, 1 rad-018 | 1 rad-024 | — |
| pack hand decon wipes | rad.decon | 20 | 2 rad-087, 1 rad-062 | 1 rad-025 | — |
| bottle bentonite drink | rad.chemlab | 20 | 1 ore-075, 1 wat-003, 1 pak-003 | 1 rad-026 | — |
| stir clay into water | crew | 10 | 1 ore-009, 1 wat-001, 1 pak-003 | 1 rad-026 | — |
| sew thyroid collar | rad.loom | 45 | 1 rad-068, 1 rad-086 | 1 rad-027 | — |
| sew lead vest | rad.loom | 120 | 3 rad-068, 1 rad-086, 1 rad-075, 1 pwr-001 | 1 rad-028 | — |
| sew shielded cap | rad.loom | 45 | 1 rad-076, 1 rad-066 | 1 rad-029 | — |
| sew shielded gloves | rad.loom | 45 | 1 rad-068, 1 rad-075 | 1 rad-030 | — |
| sew radiation suit | rad.loom | 240 | 4 rad-068, 2 rad-074, 1 rad-073, 1 pwr-001 | 1 rad-031 | — |
| sew hazmat overalls | rad.loom | 90 | 2 fib-067, 1 rad-074, 1 pwr-001 | 1 rad-032 | — |
| assemble respirator mask | rad.assembler | 30 | 1 rad-088, 1 pol-036, 1 fib-012 | 1 rad-033 | — |
| line sleep pod | rad.loom | 90 | 2 rad-074, 1 rad-072, 1 pwr-001 | 1 rad-034 | — |
| sew shielded pillow | rad.loom | 45 | 1 rad-074, 1 rad-065, 1 fib-018 | 1 rad-035 | — |
| fill water wall panel | any.bench | 60 | 1 rad-077, 1 rad-078, 4 wat-002 | 1 rad-036 | — |
| build borated wall panel | rad.caster | 90 | 1 rad-077, 1 rad-071, 1 rad-072, 1 pwr-001 | 1 rad-037 | — |
| frame leaded window pane | rad.caster | 60 | 1 rad-073, 1 rad-077 | 1 rad-038 | — |
| build storm shelter panel | rad.caster | 120 | 1 rad-036, 1 rad-037, 1 rad-067, 1 pwr-001 | 1 rad-039 | — |
| sew floor shield mat | rad.loom | 45 | 1 rad-068, 1 pol-003 | 1 rad-040 | — |
| line locker | rad.loom | 45 | 1 rad-066, 1 rad-074 | 1 rad-041 | — |
| fit cosmic ray visor | rad.assembler | 45 | 1 rad-073, 1 rad-076 | 1 rad-042 | — |
| assemble pocket dosimeter | rad.assembler | 60 | 1 rad-083, 1 rad-082, 1 rad-085, 1 pwr-001 | 1 rad-043 | — |
| assemble area monitor | rad.assembler | 120 | 1 rad-081, 1 rad-083, 1 ecp-041, 1 rad-085, 1 pwr-001 | 1 rad-044 | — |
| sew lead bunk curtain | rad.loom | 60 | 1 rad-068, 1 fib-060 | 1 rad-045 | — |
| tube decon hand gel | rad.chemlab | 20 | 1 rad-062, 1 chm-064, 1 pak-011 | 1 rad-052 | — |
| take a decon shower | rad.decon | 15 | 2 wat-001, 1 rad-062 | 2 rad-048 | dose -15, hygiene +10 |
| strip contaminated garment | rad.decon | 60 | 1 rad-046, 2 wat-001, 1 rad-062 | 1 rad-050, 1 scr-005, 1 rad-048 | — |
| drum contaminated wipes | rad.decon | 20 | 6 rad-047, 1 pak-026 | 1 rad-053 | — |
| filter decon runoff | rad.decon | 60 | 4 rad-048, 1 rad-063, 1 pwr-001 | 1 rad-051, 3 san-001 | — |
| drum spent resin | rad.decon | 20 | 4 rad-051, 1 pak-026 | 1 rad-053 | — |
| jettison radwaste drum | any.hatch | 20 | 1 rad-053 | — | dose -2 |
| make chemlab pump seal | any.bench | 30 | 1 pol-052, 1 mec-016 | 1 rad-089 | — |
| make filler piston set | any.bench | 60 | 1 met-049, 1 pol-048 | 1 rad-090 | — |
| make crucible liner | any.bench | 45 | 1 cer-040 | 1 rad-091 | — |
| carve loom shuttle | any.bench | 45 | 1 met-051 | 1 rad-092 | — |
| make detector bench fixture | any.bench | 45 | 1 met-007, 1 mec-017 | 1 rad-093 | — |
| make decon spray head | any.bench | 30 | 1 mec-049, 1 pol-037 | 1 rad-094 | — |
| build isotope chemlab kit | any.bench | 180 | 1 fur-001, 1 rad-089, 1 mec-008, 2 mec-001 | 1 rad-095 | — |
| build dose filler kit | any.bench | 120 | 1 fur-001, 1 rad-090, 1 mec-043, 2 mec-001 | 1 rad-096 | — |
| build lead caster kit | any.bench | 180 | 1 fur-001, 1 rad-091, 1 lgt-040, 2 mec-001 | 1 rad-097 | — |
| build shield loom kit | any.bench | 120 | 1 fur-001, 1 rad-092, 1 mec-010, 2 mec-001 | 1 rad-098 | — |
| build detector bench kit | any.bench | 120 | 1 fur-001, 1 rad-093, 1 ecp-010, 2 mec-001 | 1 rad-099 | — |
| build decon station kit | any.bench | 120 | 1 fur-001, 1 rad-094, 1 mec-039, 2 mec-001 | 1 rad-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| rad.chemlab | Bench lab that makes the pigments, chelators, binders and shielding compounds every radiation remedy starts from. | LABEL ALL VESSELS. BLUE IS MEDICINE. BLUE IS ALSO PIGMENT. LABEL ALL VESSELS. |
| rad.filler | Presses tablets, fills capsules and ampoules, and packs sachets and shots from the chemlab's bases. | Fill counts are reconciled against base drawn. Variance is investigated. Ref 7120/D. |
| rad.caster | Melts lead, boron and glass into shot, foil, plates, sheet, leaded panes and shielding wall panels. | Hot lead has no friends. Wear the gloves. |
| rad.loom | Weaves and sews lead and borated cloth into aprons, vests, suits, curtains, caps and liners. | Shuttle tension checked, rev 6. Leaded thread jams below line speed. |
| rad.assembler | Builds badges, counters, monitors and respirators, and packs the storm and decon kits. | Log: counter clicked. Counter is meant to click. Panic withdrawn. |
| rad.decon | Showers contaminated crew, strips hot garments, soaks wipes, filters runoff and drums radwaste for the hatch. | Strip, scrub, rinse, repeat. Dignity is not a decontamination step. Proc 90. |
| rad-001 | Tablet that fills the thyroid with stable iodine to bring dose down; the first remedy taken in a storm. | Take before the storm, not after. Late intake is recorded as operator negligence. |
| rad-002 | Worn badge whose film records dose; a known reading calms the wearer, and a spent badge is refilled. | WEAR ON CHEST. NOT IN POCKET. NOT IN MOUTH. |
| rad-003 | Heavy lead-rubber apron that keeps dose down while worn; returns contaminated when worn out. | Heavier than it looks. Lighter than the alternative. |
| rad-004 | Quilted shield blanket that keeps dose down and the cabin warmer while in use. | Lead side out. Orientation disputes are not a maintenance matter. Ref 3381/B. |
| rad-005 | Capsule of Prussian blue that binds cesium in the gut, lowering dose and some toxin; hard on the bowels. | Discoloured waste is an expected effect. Do not file a medical report. |
| rad-006 | Strong injected chelator that pulls dose and toxin down hard, but hurts and leaves the body weaker. | The cure that feels like the disease, only shorter. |
| rad-007 | Solution-soaked wipe that scrubs contamination off the skin; the used wipe is radwaste. | WIPE OUTWARD. NEVER BACK. FOLD, BAG, DRUM. |
| rad-008 | Handheld counter whose clicks show how hot things are; eases worry while carried. | Clicks mean counts. Silence means batteries. |
| rad-009 | Powdered drink that flushes toxin and hydrates, with a trip to the toilet after. | Mix with one bottle of drinking water only. Proc 63. Taste is not a fault condition. |
| rad-010 | Injection that cuts dose sharply at the cost of a little toxin and a sore arm. | Administer upper arm. Record lot number on Form 48R before disposal of sharps. |
| rad-011 | Tablet that binds heavy metals and draws toxin out, leaving the taker a little weaker. | Foundry personnel report hands washed. Bloodwork disagrees. |
| rad-012 | Tablet that cuts dose well but adds some toxin and dulls the appetite. | Ration reductions due to suppressed appetite are not refunded. Ref 0915/F. |
| rad-013 | Capsule of citrus or vitamin antioxidants that trims dose a little and supports immunity. | Grown in the orchard, bottled in medbay, swallowed on schedule. |
| rad-014 | Tablet that helps bone marrow recover after exposure, easing dose and raising immunity. | ONE DAILY AFTER EXPOSURE. DO NOT EXCEED STATED COURSE. |
| rad-015 | Tablet for illness after a heavy dose: settles toxin and pain and restores some health. | Sickness following a missed shelter call is not covered by the medical allowance. |
| rad-016 | Bottled iodine syrup, gentler than the tablet, that brings dose down. | Label says cherry flavour. Nobody aboard remembers cherries. |
| rad-017 | Strong binder pack that purges cesium and toxin from the gut, with a heavy toilet cost. | Clear the schedule. Clear the route to the toilet. |
| rad-018 | Spray foam that lifts contamination off cabin surfaces, lowering dose and cleaning the floor. | Apply, dwell, wipe. Dwell time per Proc 77. Do not shorten to meet quota. |
| rad-019 | Soap blended with decon solution that washes contamination off the body. | Lather twice after reactor-side duty. Three times if the badge went dark. |
| rad-020 | Barrier cream that keeps contamination off the skin and lowers dose a little. | Smells like engine grease. Works better than it. |
| rad-021 | Bottled chelator drink that lowers dose and toxin and adds some water. | SIP. DO NOT GULP. RETURN BOTTLE FOR REUSE. |
| rad-022 | Powder sachet that binds poisons in the gut so they pass out. | What goes in bad comes out bound. |
| rad-023 | Shelter pack of tablets and a wipe, opened when a radiation storm hits; protects and calms. | Kit is opened on storm signal only. Early opening is charged as consumption. |
| rad-024 | Wipes, foam and gel packed together for a fast full-body clean after contamination. | BREAK SEAL IN CASE OF CONTAMINATION. REPORT SEAL BREAK. |
| rad-025 | Pack of decon wipes for a quick clean of hands and face. | Pocket size. One wipe is never enough. Operator's note, pencil. |
| rad-026 | Clay stirred into water that binds toxin in the gut; drinkable. | Mud with ambitions. |
| rad-027 | Lead collar that shields the throat while worn. | Collar strap restitched, rev 3. Itch reported, not actioned. |
| rad-028 | Heavy lead vest that keeps dose well down while worn, but tires the wearer. | Fatigue from mandated shielding is not grounds for reduced output. Ref 4402/V. |
| rad-029 | Cap lined with lead foil and reflective weave that shields the head while worn. | Yes, it is a foil hat. Yes, it works. |
| rad-030 | Lead-rubber gloves for handling hot material. | Five fingers in, five fingers out. Count them. |
| rad-031 | Full shielding suit for the worst work: strong protection, but tiring and stressful to wear. | SUIT CHECK BEFORE ENTRY. TWO PERSONNEL. NO EXCEPTIONS. |
| rad-032 | Coated overalls that keep contamination and toxin off while worn; wear out quickly. | Remove before eating, before sleep, before the door slot. Proc 19. |
| rad-033 | Mask with a filter cartridge that keeps toxin out of the lungs while worn. | If it can be smelled, the seal is not sealed. |
| rad-034 | Shield-cloth and foam liner for the sleep pod that cuts dose and aids rest. | Rest periods are dose-accounted. The liner improves the figures. Ref 1077/S. |
| rad-035 | Pillow weighted with lead shot that shields the head and aids rest. | Hard as a brick. Sleeps like one, too. |
| rad-036 | Wall panel filled with raw water that absorbs radiation where it is fitted. | WATER SHIELD. NOT POTABLE. DO NOT TAP. |
| rad-037 | Wall panel of borated sheet and neutron foam that cuts dose where it is fitted. | Fitted, torqued, inspected, rev 2. Bolt four replaced with bolt of unknown origin. |
| rad-038 | Leaded glass pane that lets light into the cabin and keeps radiation out. | Window allocation is a privilege of the contract grade. Do not remove covers. |
| rad-039 | Water, boron and lead in one heavy panel: the strongest shielding wall a cabin can fit. | Enough of these make a shelter. Too few make an argument. |
| rad-040 | Lead-rubber floor mat that keeps dose down from below. | Deck plating meets minimum specification. Mats are supplementary. Ref 2264/D. |
| rad-041 | Lead-foil liner that keeps a locker's contents from adding to the cabin's dose. | HOT STORAGE. KEEP SHUT. LOG CONTENTS ON DOOR. |
| rad-042 | Leaded glass visor that shields the eyes and face while worn. | Sparks seen with the eyes shut: visor down. Then report it. |
| rad-043 | Electronic dosimeter with an alarm, carried on the body to reassure the wearer. | Alarm threshold set at the factory. Adjustment by personnel voids calibration. |
| rad-044 | Fixed monitor that watches the cabin's radiation and calms everyone in it. | Green lamp: nominal. No lamp: check the fuse before assuming nominal. |
| rad-045 | Lead-rubber curtain around the bunk that cuts dose and eases sleep. | Draw it, and for one rest period the sky is somebody else's problem. |
| rad-046 | Worn-out shield garment, too hot to wear; stripped at the decon station for its lead. | CONTAMINATED. DO NOT WEAR. DO NOT FOLD. DECON ONLY. |
| rad-047 | Used decon wipe, drummed as radwaste. | Bag it. Drum it. Do not count it twice. |
| rad-048 | Water from decon showers and stripping; filtered through resin back to grey water. | Not for drinking. Not once. Not if rationed. |
| rad-049 | Badge whose film is used up; read and refilled at the detector bench. | Readings are Company records. Personnel may request a copy on Form 88B. |
| rad-050 | Lead stripped from spent garments; recast into shot or plate. | Lead never retires. It is reassigned. |
| rad-051 | Resin loaded with what it filtered from decon runoff; drummed as radwaste. | SPENT RESIN. RADWASTE. DRUM WITHIN ONE SHIFT. |
| rad-052 | Squeeze-tube gel for a quick clean of contamination off the hands. | Rub until dry. Then rub again. |
| rad-053 | Drum of contaminated wipes or spent resin, sealed to be jettisoned through the hatch. | Jettison is logged against the station of origin. Ref 9001/J. |
| rad-054 | Iron pigment precipitated in the chemlab; the first step toward Prussian blue. | Rust with a career. |
| rad-055 | Deep blue iron pigment that binds cesium; filled into capsules and made into binder. | Medical grade. Not for marking, painting or graffiti. Proc 4 applies. |
| rad-056 | Diluted chelating agent; the base for ampoules, tablets, drinks and cesium binder. | Batch 211 assayed, within limits. Container lid cross-threaded. |
| rad-057 | Prussian blue bound with chelator, packed into cesium purge packs. | Holds on to cesium and never lets go. |
| rad-058 | Antioxidant concentrate from citrus or vitamins, for capsules and marrow support; does not keep. | USE FRESH. DATE ON MAKING. DISCARD STALE STOCK. |
| rad-059 | Antioxidant blended with medicine, pressed into marrow support tablets. | Base for the bones. Tablet yield logged on Form 14M. |
| rad-060 | Synthesised compound pressed into radioprotectant tablets and loaded into shots. | Long synthesis. Interrupting a run forfeits the batch and the power drawn. |
| rad-061 | Clay and medicine blend that becomes drink mixes, binder sachets and purge packs. | Mostly clay. The ratio is a Company formulation and is not disclosed. |
| rad-062 | Cleaning solution behind every wipe, foam, gel and decon shower. | Smells of nothing. That is how it is known to be working. |
| rad-063 | Ion-exchange resin that filters contamination out of decon runoff. | Replace on saturation. Saturated resin is radwaste. Proc 58. |
| rad-064 | Barrier gel base for skin shield cream and decon hand gel. | Slippery, sticky and on every requisition. |
| rad-065 | Small cast lead pellets that weight pillows and load lead rubber. | DO NOT INGEST. MEDBAY CANNOT REVERSE THIS. |
| rad-066 | Thin lead foil for thread, blankets, caps and locker liners. | Thin enough to fold, thick enough to matter. |
| rad-067 | Cast lead plate; the heavy layer of a storm shelter panel. | TWO PERSONNEL LIFT. CRUSH HAZARD. |
| rad-068 | Lead-loaded rubber sheet for aprons, vests, gloves, mats and curtains. | Laminate offcuts are tracked by weight. Shortfall is deducted at lead price. |
| rad-069 | Ground borosilicate glass; the boron in borated plastic. | Glass powder. Mask on. Proc 33. |
| rad-070 | Boron-loaded plastic that absorbs neutrons; pressed, foamed or coated into shielding. | Boron in plastic, plastic in everything. |
| rad-071 | Pressed borated sheet for shielding wall panels. | NEUTRON SHIELD. THIS SIDE TOWARD HULL. |
| rad-072 | Light borated foam that fills wall panels and sleep pod liners. | Density checked, lot 64. Two voids found, filled with tape. |
| rad-073 | Glass melted with lead, for window panes, visors and suit faceplates. | Looks clear. Weighs like a promise. |
| rad-074 | Cloth coated with borated compound, sewn into blankets, suits, liners and pillows. | Coating weight audited per roll. Thin rolls are returned at operator cost. |
| rad-075 | Thread spun with lead foil, for stitching shield garments and weaving reflective cloth. | Sew with it and the needle gets heavier. |
| rad-076 | Woven reflective cloth for shielded caps and visors. | SHINY SIDE OUT. |
| rad-077 | Empty metal or fibreglass frame in which every shielding panel and window is built. | A wall waiting for an assignment. |
| rad-078 | Sealed bladder that holds the water in a water wall panel. | Fill slowly. Bleed the air. Log fill volume on Form 36W. |
| rad-079 | Film that darkens with dose, slotted into badges. | It remembers what the wearer would rather not. |
| rad-080 | Moulded casing that holds a badge's film. | Clip, film, close. Casing serial must match the wearer log. |
| rad-081 | Gas-filled tube that clicks as radiation passes; the core of counters and monitors. | Each click is a particle that found the tube instead of the operator. |
| rad-082 | Crystal that flashes when struck by radiation; the sensor of a pocket dosimeter. | FRAGILE. HYGROSCOPIC. KEEP SEALED UNTIL FITTED. |
| rad-083 | Board that turns clicks and flashes into a dose reading. | Board passed bench test, rev 5. One trace repaired with wire. |
| rad-084 | Moulded case for a Geiger counter. | Drop tested. Mostly. |
| rad-085 | Small buzzer that warns when dose climbs; fitted to counters and monitors. | Silencing a dose alarm by tape or padding is a dismissible offence. Ref 6600/A. |
| rad-086 | Sewn strap and buckle that holds heavy shield garments on. | Buckle it. Lead slides. |
| rad-087 | Cut cloth or torn rags waiting to be soaked into decon wipes. | Old socks, new purpose. Reclaimed fabric is Company property. |
| rad-088 | Filter cartridge packed for a respirator mask. | REPLACE WHEN AIR CAN BE TASTED. |
| rad-089 | Spare pump seal for the isotope chemlab; wears into broken parts. | Drips mean it is time. Drips on the floor mean it was time. |
| rad-090 | Spare pistons for the dose filler; wear into scrap metal. | Piston wear measured, rev 8. Within limit by a fingernail. |
| rad-091 | Ceramic liner for the lead caster's crucible; the heat wears it fast. | Cracks are a schedule, not a surprise. |
| rad-092 | Metal shuttle that carries thread across the shield loom; wears into scrap. | Back and forth. A full contract term of it. |
| rad-093 | Jig that holds parts steady on the detector bench; wears into scrap. | Fixture alignment checked monthly. Record on Form 51F or assume misaligned. |
| rad-094 | Spray nozzle for the decon station; wears into broken parts. | Scale clogs it. Vinegar helps. So does swearing. |
| rad-095 | Flat-packed kit that installs an isotope chemlab. | Some assembly required. Some chemistry also required. |
| rad-096 | Flat-packed kit that installs a dose filler. | Instructions in the lid. Lid in the bin. |
| rad-097 | Flat-packed kit that installs a lead caster. | INSTALL BENEATH EXTRACT VENT. FUME HAZARD. |
| rad-098 | Flat-packed kit that installs a shield loom. | Thread not included. Requisition separately. Ref 3115/L. |
| rad-099 | Flat-packed kit that installs a detector bench. | First the bench, then the counters, then the calm. |
| rad-100 | Flat-packed kit that installs a decon station. | Installation is required before first exposure. Late installation voids cover. |
