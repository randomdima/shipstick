# Medical Supplies — `sup`

The hardware of care: bandages, dressings, splints, syringes, infusion bags, test strips and the kits that bundle them.
Cotton, film, latex and metal become wadding, barrels, needles and strip cards; those are cut, moulded, coated and
assembled into one-use supplies. Splints, slings, braces, casts and masks work while worn; the scanner and the
thermometer are instruments a check needs, worn only in use. Almost everything is used once and leaves a soiled or
spent form — bandages are sterilised back into service, splints remade; sharps fill sharps containers and the rest goes
through the clinical waste bin into sanitation's clinical waste bags.

## Devices

| id | device | role | cells |
|---|---|---|---|
| sup.dresser | MSD20 Dressing Station | med | 2x1 |
| sup.moulder | MSD40 Moulding Press | med | 2x1 |
| sup.steriliser | MSD60 Sterilising Chamber | med | 2x2 |
| sup.assembler | MSD80 Kit Assembler | med | 2x2 |
| sup.coater | MSD12 Test Strip Coater | med | 1x1 |
| sup.wastebin | MSD5 Clinical Waste Bin | med | 1x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| sup-001 | Bandage, Cloth | health +8, pain -3, leaves 1 sup-043 | — |
| sup-002 | Pad, Gauze | health +5, leaves 1 sup-044 | — |
| sup-003 | Plaster, Adhesive | health +3, leaves 1 sup-044 | — |
| sup-004 | Splint, Limb | health +1/h, pain -1/h | 240 h → sup-051 |
| sup-005 | Syringe, Unfilled | — | — |
| sup-006 | Kit, First Aid | health +10, pain -10, leaves 1 sup-043, leaves 1 sup-044 | — |
| sup-007 | Strip, Test, Glucose | stress -2, leaves 1 sup-047 | 2160 h → sup-047 |
| sup-008 | Gloves, Surgical | — | — |
| sup-009 | Bag, Infusion, Saline | hydration +20, health +5, bladder +15, leaves 1 sup-048 | 2160 h → med-050 |
| sup-010 | Kit, Surgery | health +40, pain +15, leaves 1 sup-044, leaves 1 sup-045, leaves 1 sup-046, leaves 1 sup-053 | — |
| sup-011 | Dressing, Sterile | health +10, leaves 1 sup-044 | — |
| sup-012 | Wrap, Elastic | pain -1/h | 240 h → scr-005 |
| sup-013 | Dressing, Burn | health +10, pain -10, leaves 1 sup-044 | — |
| sup-014 | Kit, Suture | health +12, pain +5, leaves 1 sup-045, leaves 1 sup-044 | — |
| sup-015 | Pack, Cold, Instant | pain -8, leaves 1 sup-049 | — |
| sup-016 | Wipe, Antiseptic | health +3, immunity +2, leaves 1 sup-044 | — |
| sup-017 | Strip, Test, Infection | stress -2, leaves 1 sup-047 | 2160 h → sup-047 |
| sup-018 | Strip, Test, Urine | stress -1, leaves 1 sup-047 | 2160 h → sup-047 |
| sup-019 | Strip, Test, Toxin | stress -2, leaves 1 sup-047 | 2160 h → sup-047 |
| sup-020 | Strip, Test, Water | — | 2160 h → sup-047 |
| sup-021 | Sling, Arm | pain -1/h | 336 h → scr-005 |
| sup-022 | Cast, Plaster | health +2/h, pain -1/h, fitness -1/h | 336 h → sup-050 |
| sup-023 | Brace, Knee | pain -1.5/h | 1000 h → scr-004 |
| sup-024 | Brace, Neck | pain -2/h | 500 h → scr-004 |
| sup-025 | Mask, Face, Surgical | immunity +1/h | 24 h → sup-052 |
| sup-026 | Syringe, Saline, Pre-filled | hydration +5, health +3, leaves 1 sup-045 | 2160 h → med-051 |
| sup-027 | Auto-Injector, Pain | pain -50, fitness -3, leaves 1 sup-045 | 1080 h → med-051 |
| sup-028 | Auto-Injector, Antidote | toxin -35, pain +3, leaves 1 sup-045 | 1080 h → med-051 |
| sup-029 | Auto-Injector, Sedative | stress -35, fitness -8, fun -8, leaves 1 sup-045 | 1080 h → med-051 |
| sup-030 | Bag, Infusion, Glucose | satiety +15, health +5, bladder +10, leaves 1 sup-048 | 1440 h → med-050 |
| sup-031 | Bag, Infusion, Electrolyte | hydration +25, toxin -5, bladder +15, leaves 1 sup-048 | 2160 h → med-050 |
| sup-032 | Bag, Infusion, Detox | toxin -30, hydration +10, bladder +15, leaves 1 sup-048 | 1440 h → med-050 |
| sup-033 | Kit, Trauma | health +30, pain -20, leaves 1 sup-043, leaves 1 sup-045 | — |
| sup-034 | Kit, Burn | health +20, pain -20, leaves 1 sup-044 | — |
| sup-035 | Kit, Fracture | health +10, pain -15, leaves 1 sup-004, leaves 1 sup-043 | — |
| sup-036 | Pod, Eyewash | health +3, pain -3, hygiene +3, leaves 1 scr-002 | — |
| sup-037 | Strips, Wound Closure | health +6, leaves 1 sup-044 | — |
| sup-038 | Tourniquet | health +15, pain +10, leaves 1 sup-043 | — |
| sup-039 | Scanner, Medical | — | 300 h → scr-003 |
| sup-040 | Thermometer, Digital | — | 200 h → scr-003 |
| sup-041 | Strip, Wound Packing | health +8, pain +3, leaves 1 sup-044 | — |
| sup-042 | Patch, Blister | pain -3, health +2, leaves 1 sup-044 | — |
| sup-043 | Bandage, Soiled | — | — |
| sup-044 | Dressing, Soiled | — | — |
| sup-045 | Sharps, Used | — | — |
| sup-046 | Gloves, Used | — | — |
| sup-047 | Strip, Test, Spent | — | — |
| sup-048 | Bag, Infusion, Empty | — | — |
| sup-049 | Pack, Cold, Spent | — | — |
| sup-050 | Cast, Plaster, Spent | — | — |
| sup-051 | Splint, Worn | — | — |
| sup-052 | Mask, Face, Used | — | — |
| sup-053 | Set, Instrument, Used | — | — |
| sup-054 | Container, Sharps | — | — |
| sup-055 | Container, Sharps, Full | — | — |
| sup-056 | Dressing, Hydrocolloid | health +12, leaves 1 sup-044 | — |
| sup-057 | Brace, Ankle | pain -1.5/h | 720 h → scr-005 |
| sup-058 | Stocking, Compression | pain -0.5/h | 500 h → scr-005 |
| sup-059 | Sachet, Burn Gel | pain -12, health +4, leaves 1 pak-016 | 1440 h → med-050 |
| sup-060 | Bag, Trauma, Emergency | health +40, pain -30, leaves 2 sup-043, leaves 1 sup-045, leaves 1 sup-046 | — |
| sup-061 | Underpad, Absorbent | hygiene +5, leaves 1 sup-044 | — |
| sup-062 | Splint, Finger | pain -1/h | 168 h → sup-051 |
| sup-063 | Kit, Test, Diagnostic | stress -5, leaves 3 sup-047 | 2160 h → sup-047 |
| sup-064 | Stapler, Skin | health +10, pain +8, leaves 1 sup-045 | — |
| sup-065 | Pad, Eye, Medical | health +3, pain -2, leaves 1 sup-044 | — |
| sup-066 | Bandage, Pressure | health +12, pain -3, leaves 1 sup-043 | — |
| sup-067 | Set, Instrument, Surgical | — | — |
| sup-068 | Wadding, Cotton, Absorbent | — | — |
| sup-069 | Roll, Gauze Cloth | — | — |
| sup-070 | Webbing, Elastic, Medical | — | — |
| sup-071 | Roll, Tape, Medical | — | — |
| sup-072 | Powder, Plaster of Paris | — | — |
| sup-073 | Roll, Cast Padding | — | — |
| sup-074 | Barrel, Syringe | — | — |
| sup-075 | Needle, Hypodermic | — | — |
| sup-076 | Thread, Suture | — | — |
| sup-077 | Needle, Suture, Curved | — | — |
| sup-078 | Film, Infusion Bag | — | — |
| sup-079 | Tubing, Infusion Drip | — | — |
| sup-080 | Latex, Glove | — | — |
| sup-081 | Card, Strip Backing | — | — |
| sup-082 | Pad, Reagent | — | — |
| sup-083 | Reagent, Indicator | — | 720 h |
| sup-084 | Body, Auto-Injector | — | — |
| sup-085 | Salt, Cold Pack | — | — |
| sup-086 | Case, First Aid | — | — |
| sup-087 | Drape, Surgical | — | — |
| sup-088 | Lancet | — | — |
| sup-089 | Blade, Dressing Cutter | fits sup.dresser | 1000 h → scr-001 |
| sup-090 | Die, Splint Moulding | fits sup.moulder | 2000 h → scr-001 |
| sup-091 | Element, Sterilising Chamber | fits sup.steriliser | 1500 h → scr-004 |
| sup-092 | Jig, Kit Assembler | fits sup.assembler | 2000 h → scr-001 |
| sup-093 | Roller, Test Strip Coater | fits sup.coater | 1000 h → scr-004 |
| sup-094 | Seal, Clinical Waste Bin | fits sup.wastebin | 720 h → scr-002 |
| sup-095 | Kit, Dressing Station | installs sup.dresser | — |
| sup-096 | Kit, Moulding Press, Medical | installs sup.moulder | — |
| sup-097 | Kit, Sterilising Chamber | installs sup.steriliser | — |
| sup-098 | Kit, Kit Assembler | installs sup.assembler | — |
| sup-099 | Kit, Test Strip Coater | installs sup.coater | — |
| sup-100 | Kit, Clinical Waste Bin | installs sup.wastebin | — |

## Ways

| way | by | min | needs | takes | makes | gives |
|---|---|---|---|---|---|---|
| card cotton wadding | sup.dresser | 40 | — | 2 fib-015, 1 pwr-001 | 2 sup-068 | — |
| pick rag wadding | any.bench | 45 | — | 2 scr-005 | 1 sup-068 | — |
| weave gauze roll | sup.dresser | 60 | — | 2 fib-002, 1 pwr-001 | 2 sup-069 | — |
| cut muslin gauze | sup.dresser | 30 | — | 1 fib-064, 1 pwr-001 | 2 sup-069 | — |
| knit elastic webbing | sup.dresser | 60 | — | 1 fib-029, 1 fib-002, 1 pwr-001 | 2 sup-070 | — |
| coat medical tape | sup.dresser | 40 | — | 1 pol-002, 1 pol-022, 1 pwr-001 | 2 sup-071 | — |
| calcine plaster of paris | sup.steriliser | 90 | — | 2 ore-072, 1 pwr-001 | 2 sup-072 | — |
| roll cast padding | sup.dresser | 30 | — | 1 fib-018, 1 pwr-001 | 2 sup-073 | — |
| mould syringe barrels | sup.moulder | 40 | — | 1 pol-015, 1 pwr-001 | 4 sup-074 | — |
| grind hypodermic needles | sup.moulder | 60 | — | 1 met-056, 1 pwr-001 | 6 sup-075 | — |
| sterilise suture thread | sup.steriliser | 40 | — | 1 fib-003, 1 pwr-001 | 4 sup-076 | — |
| bend suture needles | sup.moulder | 40 | — | 1 met-045, 1 pwr-001 | 6 sup-077 | — |
| extrude infusion bag film | sup.moulder | 60 | — | 1 pol-017, 1 pol-028, 1 pwr-001 | 2 sup-078 | — |
| cut silicone drip tubing | sup.moulder | 30 | — | 1 pol-037, 1 pwr-001 | 3 sup-079 | — |
| cut plastic drip tubing | any.bench | 30 | — | 1 pol-008 | 2 sup-079 | — |
| compound glove latex | sup.moulder | 60 | — | 1 pol-022, 1 chm-034, 1 pwr-001 | 2 sup-080 | — |
| cut strip backing cards | sup.coater | 30 | — | 1 pol-035, 1 pwr-001 | 6 sup-081 | — |
| punch reagent pads | sup.coater | 30 | — | 1 sup-068, 1 pwr-001 | 4 sup-082 | — |
| mix indicator reagent | sup.coater | 30 | — | 1 chm-049, 1 wat-003 | 2 sup-083 | — |
| mould auto-injector bodies | sup.moulder | 60 | — | 1 pol-018, 1 mec-005, 1 pwr-001 | 2 sup-084 | — |
| dissolve cold pack salt | any.bench | 20 | — | 1 chm-019 | 2 sup-085 | — |
| dry spent cold packs | sup.steriliser | 60 | — | 2 sup-049, 1 pwr-001 | 1 sup-085, 1 scr-002 | — |
| mould first aid cases | sup.moulder | 40 | — | 1 pol-015, 1 pwr-001 | 1 sup-086 | — |
| hinge a first aid case | any.bench | 40 | — | 1 pol-035, 1 mec-015 | 1 sup-086 | — |
| cut surgical drapes | sup.dresser | 30 | — | 1 fib-054, 1 pwr-001 | 2 sup-087 | — |
| grind lancets | sup.moulder | 40 | — | 1 met-045, 1 pol-015, 1 pwr-001 | 6 sup-088 | — |
| assemble syringes | sup.assembler | 30 | — | 1 sup-074, 1 sup-075, 1 pwr-001 | 1 sup-005 | — |
| dip surgical gloves | sup.moulder | 40 | — | 1 sup-080, 1 pwr-001 | 2 sup-008 | — |
| forge instrument set | sup.assembler | 120 | — | 2 met-034, 1 met-049, 1 pwr-001 | 1 sup-067 | — |
| sterilise used instruments | sup.steriliser | 60 | — | 1 sup-053, 1 wat-003, 1 pwr-001 | 1 sup-067 | — |
| mould sharps containers | sup.moulder | 40 | — | 1 pol-015, 1 pwr-001 | 2 sup-054 | — |
| roll bandages | sup.dresser | 30 | — | 1 sup-069, 1 sup-070, 1 pwr-001 | 3 sup-001 | — |
| launder soiled bandages | sup.steriliser | 60 | — | 2 sup-043, 2 wat-001, 1 hyg-001, 1 pwr-001 | 2 sup-001, 2 san-001 | — |
| tear rag bandages | crew | 15 | — | 2 scr-005 | 1 sup-001 | — |
| fold gauze pads | sup.dresser | 30 | — | 1 sup-069, 1 sup-068, 1 pwr-001 | 3 sup-002 | — |
| cut adhesive plasters | sup.dresser | 30 | — | 1 sup-071, 1 sup-068, 1 pwr-001 | 4 sup-003 | — |
| mould splints | sup.moulder | 40 | — | 1 pol-035, 1 sup-073, 1 pwr-001 | 2 sup-004 | — |
| resterilise worn splint | sup.steriliser | 40 | — | 1 sup-051, 1 wat-001, 1 pwr-001 | 1 sup-004, 1 san-001 | — |
| bend an aluminium splint | any.bench | 30 | — | 1 met-007, 1 fib-082 | 1 sup-004 | — |
| pack first aid kit | sup.assembler | 30 | — | 1 sup-086, 2 sup-001, 2 sup-002, 1 sup-016, 1 sup-008 | 1 sup-006 | — |
| coat glucose strips | sup.coater | 30 | — | 1 sup-081, 1 sup-082, 1 sup-083, 1 ing-003, 1 pwr-001 | 4 sup-007 | — |
| assemble saline infusion bag | sup.assembler | 45 | — | 1 sup-078, 1 sup-079, 2 med-087, 1 pwr-001 | 1 sup-009 | — |
| pack surgery kit | sup.assembler | 90 | — | 1 sup-067, 1 sup-087, 1 sup-008, 1 sup-005, 1 sup-076, 1 sup-077, 1 med-012 | 1 sup-010 | — |
| fold gauze dressings | sup.dresser | 30 | — | 1 sup-068, 1 sup-069, 1 pwr-001 | 2 sup-011 | — |
| sterilise gauze pads | sup.steriliser | 30 | — | 2 sup-002, 1 pwr-001 | 2 sup-011 | — |
| cut elastic wrap | sup.dresser | 20 | — | 2 sup-070 | 1 sup-012 | — |
| make burn dressing | sup.dresser | 30 | — | 1 sup-011, 1 med-080 | 1 sup-013 | — |
| pack suture kit | sup.assembler | 30 | — | 2 sup-076, 1 sup-077, 1 sup-016 | 1 sup-014 | — |
| seal instant cold packs | sup.moulder | 30 | — | 1 sup-085, 1 wat-001, 1 pol-002 | 1 sup-015 | — |
| soak antiseptic wipes | sup.dresser | 20 | — | 1 sup-068, 1 med-081 | 4 sup-016 | — |
| coat infection strips | sup.coater | 30 | — | 1 sup-081, 1 sup-082, 1 sup-083, 1 bio-010, 1 pwr-001 | 4 sup-017 | — |
| coat urine strips | sup.coater | 30 | — | 1 sup-081, 1 sup-082, 1 sup-083, 1 pwr-001 | 4 sup-018 | — |
| coat toxin strips | sup.coater | 30 | — | 1 sup-081, 1 sup-082, 1 sup-083, 1 chm-048, 1 pwr-001 | 4 sup-019 | — |
| coat water strips | sup.coater | 30 | — | 1 sup-081, 1 sup-082, 1 chm-049, 1 pwr-001 | 4 sup-020 | — |
| test the water supply | crew | 5 | — | 1 sup-020 | 1 sup-047 | stress -2 |
| check for fever | crew | 10 | 1 sup-040 | 1 sup-017 | 1 sup-047 | stress -6, immunity +2 |
| run a body scan | crew | 20 | 1 sup-039 | 1 pwr-001 | — | health +4, stress -8 |
| sew arm sling | sup.dresser | 30 | — | 1 fib-054, 1 fib-012 | 1 sup-021 | — |
| knot a rag sling | crew | 10 | — | 2 scr-005 | 1 sup-021 | — |
| set a plaster cast | sup.dresser | 45 | — | 2 sup-072, 1 sup-073, 1 wat-001 | 1 sup-022 | pain +5 |
| assemble knee brace | sup.assembler | 60 | — | 1 sup-070, 1 pol-051, 1 met-008 | 1 sup-023 | — |
| mould neck brace | sup.moulder | 60 | — | 1 pol-051, 1 pol-035, 1 pwr-001 | 1 sup-024 | — |
| sew face masks | sup.dresser | 30 | — | 1 fib-068, 1 fib-029, 1 pwr-001 | 4 sup-025 | — |
| fill saline syringes | sup.assembler | 20 | — | 1 sup-005, 1 med-087 | 1 sup-026 | — |
| load pain auto-injector | sup.assembler | 30 | — | 1 sup-084, 1 sup-075, 1 med-060, 1 med-087 | 1 sup-027 | — |
| load antidote auto-injector | sup.assembler | 30 | — | 1 sup-084, 1 sup-075, 1 med-076, 1 med-087 | 1 sup-028 | — |
| load sedative auto-injector | sup.assembler | 30 | — | 1 sup-084, 1 sup-075, 1 med-062, 1 med-087 | 1 sup-029 | — |
| assemble glucose infusion bag | sup.assembler | 45 | — | 1 sup-078, 1 sup-079, 1 med-087, 1 ing-003, 1 pwr-001 | 1 sup-030 | — |
| assemble electrolyte infusion bag | sup.assembler | 45 | — | 1 sup-078, 1 sup-079, 1 med-087, 1 med-013, 1 pwr-001 | 1 sup-031 | — |
| assemble detox infusion bag | sup.assembler | 45 | — | 1 sup-078, 1 sup-079, 1 med-087, 1 med-076, 1 pwr-001 | 1 sup-032 | — |
| pack trauma kit | sup.assembler | 45 | — | 1 sup-086, 1 sup-066, 1 sup-038, 1 sup-041, 1 sup-008 | 1 sup-033 | — |
| pack burn kit | sup.assembler | 30 | — | 1 sup-086, 2 sup-013, 1 sup-059 | 1 sup-034 | — |
| pack fracture kit | sup.assembler | 30 | — | 1 sup-086, 1 sup-004, 2 sup-001, 1 med-001 | 1 sup-035 | — |
| seal eyewash pods | sup.moulder | 30 | — | 1 med-087, 1 pol-002, 1 pwr-001 | 2 sup-036 | — |
| cut wound closure strips | sup.dresser | 20 | — | 1 sup-071, 1 pol-002 | 4 sup-037 | — |
| sew tourniquet | sup.dresser | 30 | — | 1 fib-012, 1 mec-046 | 1 sup-038 | — |
| assemble medical scanner | sup.assembler | 180 | — | 1 ecp-052, 1 lgt-036, 1 lgt-037, 1 ecp-041, 1 pwr-001 | 1 sup-039 | — |
| assemble digital thermometer | sup.assembler | 60 | — | 1 lgt-008, 1 ecp-007, 1 ecp-070 | 1 sup-040 | — |
| soak wound packing strips | sup.dresser | 20 | — | 1 sup-069, 1 med-081 | 2 sup-041 | — |
| cut blister patches | sup.dresser | 20 | — | 1 sup-071, 1 pol-036 | 4 sup-042 | — |
| cast hydrocolloid dressings | sup.dresser | 40 | — | 1 pol-036, 1 bio-068, 1 pwr-001 | 2 sup-056 | — |
| sew ankle brace | sup.dresser | 40 | — | 1 sup-070, 1 fib-082 | 1 sup-057 | — |
| knit compression stocking | sup.dresser | 60 | — | 2 fib-029, 1 fib-002, 1 pwr-001 | 1 sup-058 | — |
| fill burn gel sachets | sup.assembler | 20 | — | 1 med-080, 1 med-086, 1 pak-015 | 1 sup-059 | — |
| pack emergency trauma bag | sup.assembler | 60 | — | 1 sup-033, 1 sup-006, 1 sup-027, 1 pak-032 | 1 sup-060 | — |
| make absorbent underpads | sup.dresser | 30 | — | 2 sup-068, 1 pol-002 | 2 sup-061 | — |
| cut finger splints | sup.moulder | 30 | — | 1 met-007, 1 sup-073 | 4 sup-062 | — |
| pack diagnostic test kit | sup.assembler | 20 | — | 1 sup-007, 1 sup-017, 1 sup-018, 1 sup-088 | 1 sup-063 | — |
| assemble skin stapler | sup.assembler | 60 | — | 1 pol-018, 1 met-045, 1 mec-005 | 1 sup-064 | — |
| cut eye pads | sup.dresser | 20 | — | 1 sup-068, 1 sup-071 | 4 sup-065 | — |
| make pressure bandage | sup.dresser | 20 | — | 1 sup-001, 1 sup-002 | 1 sup-066 | — |
| bag soiled bandages | sup.wastebin | 10 | — | 3 sup-043 | 1 san-069 | — |
| bag soiled dressings | sup.wastebin | 10 | — | 4 sup-044 | 1 san-069 | — |
| bag used gloves | sup.wastebin | 10 | — | 4 sup-046 | 1 san-069 | — |
| bag spent test strips | sup.wastebin | 10 | — | 6 sup-047 | 1 san-069 | — |
| crush empty infusion bags | sup.wastebin | 10 | — | 2 sup-048 | 1 scr-002 | — |
| bag spent plaster cast | sup.wastebin | 10 | — | 1 sup-050 | 1 san-069 | — |
| bag used face masks | sup.wastebin | 10 | — | 6 sup-052 | 1 san-069 | — |
| fill sharps container | sup.wastebin | 10 | — | 1 sup-054, 6 sup-045 | 1 sup-055 | — |
| autoclave full sharps container | sup.steriliser | 90 | — | 1 sup-055, 1 pwr-001 | 1 scr-001, 1 scr-002 | — |
| make dressing cutter blade | any.bench | 45 | — | 1 met-042 | 1 sup-089 | — |
| make splint moulding die | any.bench | 90 | — | 1 met-005 | 1 sup-090 | — |
| make steriliser heating element | any.bench | 60 | — | 1 met-047, 1 cer-038 | 1 sup-091 | — |
| make kit assembler jig | any.bench | 45 | — | 1 met-007, 1 mec-017 | 1 sup-092 | — |
| make strip coater roller | any.bench | 45 | — | 1 pol-003, 1 mec-006 | 1 sup-093 | — |
| cut waste bin lid seal | any.bench | 20 | — | 1 pol-052 | 1 sup-094 | — |
| build dressing station kit | any.bench | 120 | — | 1 fur-001, 1 sup-089, 1 mec-010, 2 mec-001 | 1 sup-095 | — |
| build moulding press kit | any.bench | 120 | — | 1 fur-001, 1 sup-090, 1 mec-043, 2 mec-001 | 1 sup-096 | — |
| build sterilising chamber kit | any.bench | 150 | — | 1 fur-001, 1 sup-091, 1 lgt-008, 2 mec-001 | 1 sup-097 | — |
| build kit assembler kit | any.bench | 150 | — | 1 fur-001, 1 sup-092, 1 ecp-010, 2 mec-001 | 1 sup-098 | — |
| build test strip coater kit | any.bench | 120 | — | 1 fur-001, 1 sup-093, 1 mec-041, 2 mec-001 | 1 sup-099 | — |
| build clinical waste bin kit | any.bench | 60 | — | 1 fur-001, 1 sup-094, 1 mec-046, 2 mec-001 | 1 sup-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| sup.dresser | Cards wadding, weaves gauze and cuts, rolls and sews bandages, dressings, slings and masks. | KEEP HANDS CLEAR OF CUTTER HEAD. COF MEDICAL DIVISION. |
| sup.moulder | Moulds syringe barrels, splints, braces, cases and sharps containers, and grinds needles and lancets. | Press output is Company stock. Unlogged splints are treated as pilferage. Ref 2203/M. |
| sup.steriliser | Sterilises dressings, instruments, bandages and splints for reuse, calcines plaster and autoclaves full sharps containers. | Door gasket replaced, rev 4. Cycle log unreadable before shift 300. |
| sup.assembler | Assembles syringes, infusion bags, auto-injectors, instrument sets and every kind of medical kit. | Pack it right. Someone opens it on the worst shift they will ever work. |
| sup.coater | Coats reagent onto backing cards to make test strips. | Calibrate against reference card weekly. Record drift on Form 61C. |
| sup.wastebin | Bags clinical waste for sanitation and fills sharps containers. | CLINICAL WASTE. NO HANDS IN BIN. RED LID ONLY. |
| sup-001 | Cloth bandage for binding a wound; laundered and returned to service after use. | Bandages are issued, not owned. Return soiled units for laundering. Ref 1180/B. |
| sup-002 | Gauze pad for covering a small wound. | Press, hold, count to a hundred. Then count again. |
| sup-003 | Adhesive plaster for small cuts. | Most frequently logged medical procedure on the carrier. Usage audited quarterly. |
| sup-004 | Limb splint that holds a broken bone still while worn; wears out with use. | Do not move it. Do not scratch under it. Do not ask how long. |
| sup-005 | Unfilled syringe for loading with saline or packing into a surgery kit. | SINGLE USE. ONE OPERATOR. ONE NEEDLE. DO NOT RECAP. |
| sup-006 | Case of bandages, pads, a wipe and gloves for minor cuts and knocks. | One kit per capsule. Missing kits are replaced at operator cost. Ref 4410/K. |
| sup-007 | Test strip that reads blood sugar; a clear result eases worry. | Prick, dab, wait. Read against chart G. Discard per Proc 207. |
| sup-008 | Disposable gloves packed into first aid, surgery and trauma kits. | GLOVES BEFORE BLOOD. NO EXCEPTIONS. |
| sup-009 | Bag of saline dripped into a vein to rehydrate a crew member. | For operators unable to drink. Not a substitute for the scheduled water ration. |
| sup-010 | Instruments, drapes and an anaesthetic for surgery; heals the most and hurts on the way. | Nobody wants to open this. Everybody checks it is still there. |
| sup-011 | Sterile dressing for a deeper wound. | Sterility lot 88, passed. Seal intact at packing. |
| sup-012 | Elastic wrap that eases a sprain while worn; frays into fabric scrap. | Wrap the ankle. File the incident report later, or never. |
| sup-013 | Aloe-soaked dressing for burns. | Galley burns are recorded as operator error. Ref 3307/G. |
| sup-014 | Thread, needle and a wipe for stitching a cut closed; heals well but stings. | Hold still. This will hurt. Then it will not. |
| sup-015 | Pack that turns cold when squeezed, for bruises and sprains. | SQUEEZE TO ACTIVATE. DO NOT INGEST CONTENTS. |
| sup-016 | Single antiseptic wipe for cleaning a wound. | Wipe first, dress second. Proc 118, step 2. |
| sup-017 | Test strip that checks for infection; taken with the thermometer in a fever check. | Any colour but blue: report to medical on Form 30D within one shift. |
| sup-018 | Test strip that checks urine for disorder. | Read it. Then stop thinking about it. |
| sup-019 | Test strip that checks the body for toxins. | Toxin exposure on duty is reviewed for liability before any claim is heard. |
| sup-020 | Test strip that checks the capsule's water supply. | Test the supply each shift. Log the result on Form 12W before drinking. |
| sup-021 | Sling that rests an injured arm while worn. | Operators in slings retain full duty schedules. Output targets unchanged. |
| sup-022 | Plaster cast that heals a fracture while worn and keeps the limb idle. | Sign it. Tradition. Nobody remembers whose. |
| sup-023 | Brace that eases a bad knee while worn; long-lasting. | Hinge play within tolerance. Reissued, third wearer. |
| sup-024 | Brace that holds the neck still and eases pain while worn. | FACE FORWARD. DO NOT ADJUST STRAPS WHILE WORN. |
| sup-025 | Mask that helps keep illness out while worn; spent quickly. | Masks are mandatory when any operator coughs. Compliance is logged. |
| sup-026 | Syringe of saline, filled and ready for use. | Filled lot 412. Discard after expiry stamp. |
| sup-027 | Spring-loaded injector of strong painkiller for emergencies; leaves the body weak. | Thigh, press, hold. Record time of use on Form 9P. |
| sup-028 | Spring-loaded injector of antidote for poisoning. | INJECT THROUGH SUIT FABRIC. DO NOT HESITATE. |
| sup-029 | Spring-loaded sedative for a crew member in crisis; leaves the patient dull and slow. | Use is reported to Personnel. Repeated use is reviewed against contract. |
| sup-030 | Sugar drip that feeds a crew member unable to eat. | Dinner, intravenous. Tastes the same as the galley. |
| sup-031 | Electrolyte drip that rehydrates and helps clear toxins. | Issued for medical need only. Recreational rehydration is not a covered use. |
| sup-032 | Drip that flushes toxins from the blood. | Patient supine for full infusion. Record volume on Form 44T. |
| sup-033 | Case for severe bleeding: pressure bandage, tourniquet, packing and gloves. | TRAUMA. STOP THE BLEED. ALL ELSE WAITS. |
| sup-034 | Case of burn dressings and burn gel. | Cool, cover, report. Proc 160 governs galley fires. |
| sup-035 | Splint, bandages and a painkiller for a broken bone; the splint stays on. | Hear a crack, grab this. Questions after. |
| sup-036 | Sealed pod of saline for flushing an eye. | EYEWASH. TILT HEAD. SQUEEZE ONCE. |
| sup-037 | Adhesive strips that pull a cut closed without stitches. | Approved in place of sutures for minor wounds. Wound length per chart W. |
| sup-038 | Strap that stops severe bleeding from a limb; painful. | Note time applied on the strap tag. Report to medical. Proc 22. |
| sup-039 | Handheld scanner needed for a body scan; wears out into electronic scrap. | Calibrated, rev 11. Battery door held with tape. |
| sup-040 | Thermometer needed for a fever check; wears out into electronic scrap. | ORAL USE. NO TALKING DURING READING. |
| sup-041 | Antiseptic gauze for packing a deep wound; stings. | Pack it tight. Apologise later, if at all. |
| sup-042 | Patch that cushions a friction blister. | Standard-issue boots are not a recognised cause of injury. Ref 5012/F. |
| sup-043 | Used bandage; laundered back into service or bagged as clinical waste. | SOILED. LAUNDER OR BAG. DO NOT STORE. |
| sup-044 | Used dressing or plaster, bound for the clinical waste bin. | Bag at once. Clinical waste never shares a slot with food. Proc 31. |
| sup-045 | Used needles and blades, collected in a sharps container. | SHARPS. NEVER RECAP. NEVER HAND OVER. |
| sup-046 | Used gloves, bound for the clinical waste bin. | Peel inside out. Bin. Wash anyway. |
| sup-047 | Used test strip, bound for the clinical waste bin. | Results are recorded before disposal. Unrecorded strips count as unused stock. |
| sup-048 | Empty infusion bag; crushed for plastic scrap. | Drained, flattened, logged. Scrap value credited to the Company. |
| sup-049 | Used cold pack; dried to recover the salt. | Warm now. The salt in it is worth keeping. |
| sup-050 | Cast removed after healing; bagged as clinical waste. | Off it comes. The signatures go in the bin with it. |
| sup-051 | Splint worn out with use; resterilised for another patient. | Resterilised, cycle 5. Previous wearer unrecorded. |
| sup-052 | Used face mask, bound for the clinical waste bin. | USED MASK. BIN IT. DO NOT POCKET. |
| sup-053 | Surgical instruments after use; sterilised back into a set. | Count every instrument back in. Shortfall reported on Form 70S. |
| sup-054 | Empty container for used sharps. | FILL TO LINE ONLY. SEAL WHEN FULL. |
| sup-055 | Full sharps container; autoclaved to recover metal and plastic scrap. | Overfilled containers are a reportable incident. Ref 6631/S. |
| sup-056 | Gel dressing that keeps a wound moist and heals it well. | Leave it on. It is working, whatever it looks like. |
| sup-057 | Brace that eases a sprained ankle while worn. | Strap stitching resewn, rev 2. Issue to any foot size. |
| sup-058 | Stocking that eases swollen legs while worn; long-lasting. | Fluid shift in low gravity is an expected condition and is not compensable. |
| sup-059 | Sachet of gel for burns. | BURN GEL. TEAR AT NOTCH. EXTERNAL USE ONLY. |
| sup-060 | Full emergency bag: trauma kit, first aid kit and a pain injector. | Seal breaks are logged. Restock is charged to the station that opened it. |
| sup-061 | Pad that keeps a patient and bedding clean. | Dignity, issued by the square. |
| sup-062 | Small splint for a broken finger, worn until it wears out. | Tape to the adjacent finger. Report reduced keying speed on Form 15K. |
| sup-063 | Set of test strips and a lancet for a full health check. | Health checks are compulsory. Unfit results are forwarded to Contracts. |
| sup-064 | Stapler that closes a cut fast; painful. | Click, click, done. Do not watch it happen. |
| sup-065 | Pad that covers and rests an injured eye. | Sterile until opened. Sterility not guaranteed after. Inspected, rev 1. |
| sup-066 | Bandage and pad that press on a bleeding wound. | PRESS HARD. HOLD. DO NOT LIFT TO LOOK. |
| sup-067 | Sterile set of surgical instruments for a surgery kit. | Instrument sets are serial-tracked. Set SN 0318 5506 remains unaccounted for. |
| sup-068 | Cotton wadding for pads, dressings, wipes and reagent pads. | White, fibrous, found in every corner of medbay. |
| sup-069 | Roll of gauze for bandages, pads and packing. | GAUZE. KEEP DRY. KEEP SEALED. |
| sup-070 | Elastic webbing for bandages, wraps and braces. | Stretch test passed, lot 37. Recovery slow but acceptable. |
| sup-071 | Adhesive tape for plasters and closure strips. | Sticks to everything but the wound. |
| sup-072 | Powdered plaster for setting casts. | PLASTER POWDER. AVOID INHALATION. KEEP LID ON. |
| sup-073 | Soft padding laid under casts and splints. | Padding is consumable stock. Reuse between patients is not authorised. |
| sup-074 | Plastic barrel for assembling a syringe. | Moulded batch 19. Flash trimmed by hand. |
| sup-075 | Fine needle for syringes and auto-injectors. | Sharp end goes in. Not in the thumb, ideally. |
| sup-076 | Sterile thread for sutures. | Open in the sterile field only. Proc 141 applies. |
| sup-077 | Curved needle for stitching. | SHARP. CURVED. COUNT BEFORE AND AFTER USE. |
| sup-078 | Medical film for making infusion bags. | Film offcuts are reclaimable stock. Do not bin. Ref 2290/P. |
| sup-079 | Tubing for infusion drip lines. | Run it straight, no kinks. Prime before connection per Proc 52. |
| sup-080 | Latex compound for dipping surgical gloves. | Smells like rubber because it is. |
| sup-081 | Backing card for test strips. | Card stock, batch 7. Cut true to template. |
| sup-082 | Reagent pad punched from wadding for test strips. | Pad yield per unit of wadding is monitored. Shortfalls are investigated. |
| sup-083 | Indicator reagent for coating test strips; loses strength on the shelf. | REAGENT. DATE ON MIXING. DISCARD WHEN EXPIRED. |
| sup-084 | Plastic body for an auto-injector. | SPRING LOADED. DO NOT DISASSEMBLE. |
| sup-085 | Salt for filling cold packs; recovered from spent packs. | Dry spent packs before recovery. Salt yield logged on Form 8R. |
| sup-086 | Empty case for packing medical kits. | Green cross, hinged lid. The hinge goes first. |
| sup-087 | Sterile drape for surgery. | STERILE SIDE UP. DO NOT REUSE. |
| sup-088 | Small lancet for drawing a drop of blood. | Lancets are counted on issue and on disposal. Discrepancies are deducted. |
| sup-089 | Replacement cutter blade for the dressing station. | Blade swapped, shift 140. Old blade sent to scrap. |
| sup-090 | Replacement splint moulding die for the moulding press. | Dies are Company tooling. Unauthorised profiles void the press warranty. |
| sup-091 | Replacement heating element for the sterilising chamber. | HOT SURFACE. ISOLATE POWER BEFORE SERVICE. |
| sup-092 | Replacement jig for the kit assembler. | Jig squared, rev 3. Locating pin worn, still in service. |
| sup-093 | Replacement roller for the test strip coater. | Replace roller when coating streaks. Log the change on Form 23C. |
| sup-094 | Replacement lid seal for the clinical waste bin. | Keeps the smell in. Mostly. |
| sup-095 | Kit that installs a dressing station. | Installation by the operator is a condition of contract. No fitter is provided. |
| sup-096 | Kit that installs a moulding press for medical supplies. | MEDICAL DIVISION. HEAVY. LIFT WITH TWO PERSONNEL. |
| sup-097 | Kit that installs a sterilising chamber. | Factory test passed, rev 9. Door seal shipped separately. |
| sup-098 | Kit that installs a kit assembler. | A kit for making kits. Somebody signed for this. |
| sup-099 | Kit that installs a test strip coater. | Coater output is subject to quality audit. Failed lots are not credited. |
| sup-100 | Kit that installs a clinical waste bin. | The bin nobody wants to empty. Somebody will be assigned. |
