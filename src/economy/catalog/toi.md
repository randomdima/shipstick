# Toilet & Body Waste — `toi`

What the crew member leaves at the toilet, and everything that catches, carries and holds it until sanitation takes it:
urine and solid waste from the universal toilet or a better one (composting, urine-diverting, bidet, vacuum), the paper,
bags, jugs, canisters and totes they go into, the litters and tank chemicals that keep them, and the toilets' own parts
and kits. Body waste left too long turns worse (stale, putrid, leaking, septic); all of it, fresh or foul, goes on to
`san` to be made into water, compost, biogas and fertilizer.

## Devices

| id | device | role | cells |
|---|---|---|---|
| toi.compostloo | LV100 Composting Toilet | sanit | 1x1 |
| toi.divertloo | LV120 Urine Diverting Toilet | sanit | 1x1 |
| toi.bidet | LV140 Bidet Toilet | sanit | 1x1 |
| toi.vacloo | LV160 Vacuum Toilet | sanit | 1x1 |
| toi.tank | LV300 Waste Holding Tank | sanit | 1x2 |
| toi.bagger | LV410 Waste Bag Sealer | sanit | 1x1 |
| toi.tissue | LV520 Tissue Roller | sanit | 2x1 |
| toi.chemmix | LV600 Toilet Chemical Mixer | sanit | 1x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| toi-001 | Urine | — | 48 h → toi-006 |
| toi-002 | Waste, Solid | — | 72 h → toi-007 |
| toi-003 | Paper, Toilet | — | — |
| toi-004 | Bag, Waste | — | — |
| toi-005 | Bag, Waste, Filled | — | 168 h → toi-008 |
| toi-006 | Urine, Stale | — | 336 h → toi-011 |
| toi-007 | Waste, Putrid | — | 240 h → toi-012 |
| toi-008 | Bag, Waste, Leaking | — | 168 h → toi-007 |
| toi-009 | Water, Black | — | 48 h → toi-010 |
| toi-010 | Water, Black, Septic | — | — |
| toi-011 | Scale, Urine | — | — |
| toi-012 | Sludge, Faecal, Toxic | — | — |
| toi-013 | Urine, Diverted | — | 96 h → toi-006 |
| toi-014 | Faeces, Dry | — | — |
| toi-015 | Mix, Toilet Compost | — | — |
| toi-016 | Puck, Waste, Compacted | — | — |
| toi-017 | Urine, Stored | — | — |
| toi-018 | Slurry, Tank | — | 120 h → toi-010 |
| toi-019 | Jug, Urine | — | — |
| toi-020 | Jug, Urine, Filled | — | 96 h → toi-021 |
| toi-021 | Jug, Urine, Reeking | — | — |
| toi-022 | Pouch, Urine, Sealed | — | 168 h → toi-006 |
| toi-023 | Canister, Waste | — | — |
| toi-024 | Canister, Waste, Filled | — | 240 h → toi-025 |
| toi-025 | Canister, Waste, Swollen | — | — |
| toi-026 | Tote, Waste | — | — |
| toi-027 | Tote, Waste, Full | — | 336 h → toi-028 |
| toi-028 | Tote, Waste, Fouled | — | — |
| toi-029 | Bale, Waste | — | 504 h → toi-008 |
| toi-030 | Bedpan | — | — |
| toi-031 | Bedpan, Filled | — | 24 h → toi-032 |
| toi-032 | Bedpan, Fouled | — | — |
| toi-033 | Bag, Sick | — | — |
| toi-034 | Bag, Sick, Filled | — | 72 h → toi-008 |
| toi-035 | Bag, Waste, Gelling | — | — |
| toi-036 | Bag, Waste, Gelling, Filled | — | 336 h → toi-008 |
| toi-037 | Bag, Waste, Compostable | — | — |
| toi-038 | Bag, Waste, Compostable, Filled | — | 120 h → toi-008 |
| toi-039 | Bag, Waste, Treated | — | 336 h → toi-008 |
| toi-040 | Waste, Double Bagged | — | 504 h → toi-008 |
| toi-041 | Roll, Waste Bag | — | — |
| toi-042 | Film, Waste Bag | — | — |
| toi-043 | Brief, Absorbent | bladder -100, hygiene -10, leaves 1 toi-044 | — |
| toi-044 | Brief, Absorbent, Soiled | — | 48 h → toi-007 |
| toi-045 | Sanitary Product, Used | — | 48 h → toi-007 |
| toi-046 | Cup, Sample | — | — |
| toi-047 | Sample, Urine | — | 24 h → toi-006 |
| toi-048 | Sample, Stool | — | 24 h → toi-007 |
| toi-049 | Powder, Urine Gelling | — | — |
| toi-050 | Urine, Gelled | — | — |
| toi-051 | Tablet, Holding Tank | — | — |
| toi-052 | Sachet, Composting Enzyme | — | 720 h |
| toi-053 | Litter, Toilet Cover | — | — |
| toi-054 | Litter, Fibre, Shredded | — | — |
| toi-055 | Litter, Toilet, Charcoal | — | — |
| toi-056 | Pulp, Paper | — | — |
| toi-057 | Roll, Tissue, Parent | — | — |
| toi-058 | Paper, Toilet, Soft | — | — |
| toi-059 | Paper, Toilet, Recycled | — | — |
| toi-060 | Tissue, Toilet, Moist | — | 240 h → toi-003 |
| toi-061 | Cover, Toilet Seat | hygiene +2 | — |
| toi-062 | Deodorizer, Toilet Bowl | cabin.clean +4 | — |
| toi-063 | Spray, Toilet Deodorizer | cabin.clean +3, leaves 1 pak-028 | — |
| toi-064 | Gel, Toilet Freshener | cabin.clean +1/h | 168 h |
| toi-065 | Screen, Urinal | cabin.clean +1/h | 240 h → scr-002 |
| toi-066 | Filter, Toilet Odour | cabin.clean +1/h | 240 h → toi-067 |
| toi-067 | Filter, Toilet Odour, Spent | — | — |
| toi-068 | Seat, Toilet, Padded | stress -1/h | 720 h → toi-069 |
| toi-069 | Seat, Toilet, Cracked | — | — |
| toi-070 | Curtain, Toilet Privacy | stress -1/h | 600 h → scr-005 |
| toi-071 | Bottle, Hand Bidet | — | 300 h → scr-002 |
| toi-072 | Seat, Toilet | fits any.toilet, leaves 1 toi-069 | — |
| toi-073 | Ring, Toilet Seal | fits any.toilet, leaves 1 scr-002 | — |
| toi-074 | Valve, Toilet Flush | fits any.toilet, leaves 1 scr-004 | — |
| toi-075 | Fan, Toilet Vent | fits any.toilet, leaves 1 scr-004 | — |
| toi-076 | Drum, Composting Toilet | fits toi.compostloo, leaves 1 scr-001 | — |
| toi-077 | Crank, Composting Toilet | fits toi.compostloo, leaves 1 scr-001 | — |
| toi-078 | Insert, Urine Diverting Toilet | fits toi.divertloo, leaves 1 scr-002 | — |
| toi-079 | Hose, Urine Diverting Toilet | fits toi.divertloo, leaves 1 scr-002 | — |
| toi-080 | Nozzle, Bidet Toilet | fits toi.bidet, leaves 1 scr-001 | — |
| toi-081 | Heater, Bidet Toilet | fits toi.bidet, leaves 1 scr-004 | — |
| toi-082 | Pump, Vacuum Toilet | fits toi.vacloo, leaves 1 scr-004 | — |
| toi-083 | Valve, Vacuum Toilet | fits toi.vacloo, leaves 1 scr-004 | — |
| toi-084 | Liner, Waste Holding Tank | fits toi.tank, leaves 1 scr-002 | — |
| toi-085 | Float, Waste Holding Tank | fits toi.tank, leaves 1 scr-003 | — |
| toi-086 | Heat Bar, Waste Bag Sealer | fits toi.bagger, leaves 1 scr-001 | — |
| toi-087 | Roller, Waste Bag Sealer | fits toi.bagger, leaves 1 scr-004 | — |
| toi-088 | Drum, Tissue Roller | fits toi.tissue, leaves 1 scr-001 | — |
| toi-089 | Blade, Cutter, Tissue Roller | fits toi.tissue, leaves 1 scr-001 | — |
| toi-090 | Paddle, Toilet Chemical Mixer | fits toi.chemmix, leaves 1 scr-001 | — |
| toi-091 | Diaphragm, Dosing Pump | fits toi.chemmix, leaves 1 scr-002 | — |
| toi-092 | Kit, Composting Toilet | installs toi.compostloo | — |
| toi-093 | Kit, Urine Diverting Toilet | installs toi.divertloo | — |
| toi-094 | Kit, Bidet Toilet | installs toi.bidet | — |
| toi-095 | Kit, Vacuum Toilet | installs toi.vacloo | — |
| toi-096 | Kit, Waste Holding Tank | installs toi.tank | — |
| toi-097 | Kit, Waste Bag Sealer | installs toi.bagger | — |
| toi-098 | Kit, Tissue Roller | installs toi.tissue | — |
| toi-099 | Kit, Toilet Chemical Mixer | installs toi.chemmix | — |
| toi-100 | Pack, Toilet Paper | — | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| urinate in the diverting toilet | toi.divertloo | 2 | — | 1 toi-013 | bladder -100 |
| defecate in the diverting toilet | toi.divertloo | 8 | 1 toi-003 | 1 toi-014 | bowel -100, stress -1 |
| defecate with recycled paper | toi.divertloo | 8 | 1 toi-059 | 1 toi-014 | bowel -100, hygiene -2 |
| urinate in the composting toilet | toi.compostloo | 2 | — | 1 toi-001 | bladder -100 |
| use the composting toilet | toi.compostloo | 8 | 1 toi-003, 1 toi-053 | 1 toi-015 | bowel -100, cabin.clean +1 |
| use the composting toilet with fibre litter | toi.compostloo | 8 | 1 toi-003, 1 toi-054 | 1 toi-015 | bowel -100, cabin.clean +1 |
| use the composting toilet with charcoal litter | toi.compostloo | 8 | 1 toi-003, 1 toi-055 | 1 toi-015 | bowel -100, cabin.clean +3 |
| use the composting toilet with enzyme | toi.compostloo | 8 | 1 toi-003, 1 toi-053, 1 toi-052 | 1 toi-015 | bowel -100, cabin.clean +2 |
| use the composting toilet with moist tissue | toi.compostloo | 8 | 1 toi-060, 1 toi-053 | 1 toi-015 | bowel -100, hygiene +4 |
| cover tank waste with litter | toi.compostloo | 30 | 2 toi-002, 1 toi-053 | 2 toi-015 | — |
| use the bidet toilet | toi.bidet | 10 | 1 wat-001, 1 pwr-001 | 1 toi-009 | bowel -100, hygiene +8 |
| urinate at the bidet toilet | toi.bidet | 3 | 1 wat-002 | 1 toi-009 | bladder -100, hygiene +2 |
| take a warm bidet wash | toi.bidet | 10 | 1 wat-006, 1 toi-058 | 1 toi-009 | bowel -100, hygiene +12, stress -2 |
| use the vacuum toilet | toi.vacloo | 6 | 1 toi-003, 1 pwr-001 | 1 toi-016 | bowel -100, cabin.clean +1 |
| use the vacuum toilet with soft paper | toi.vacloo | 6 | 1 toi-058, 1 pwr-001 | 1 toi-016 | bowel -100, stress -2, cabin.clean +1 |
| urinate in the vacuum toilet | toi.vacloo | 1 | 1 pwr-001 | 1 toi-001 | bladder -100, hygiene +2 |
| compact tank waste | toi.vacloo | 30 | 3 toi-002, 1 toi-004, 1 pwr-001 | 1 toi-016 | — |
| relieve into a waste bag | crew | 10 | 1 toi-004, 1 toi-003 | 1 toi-005 | bowel -100, hygiene -5 |
| relieve into a gelling bag | crew | 10 | 1 toi-035 | 1 toi-036 | bowel -100, bladder -100, hygiene -5 |
| relieve into a compostable bag | crew | 10 | 1 toi-037, 1 toi-003 | 1 toi-038 | bowel -100, hygiene -5 |
| urinate into a jug | crew | 3 | 1 toi-019 | 1 toi-020 | bladder -100 |
| urinate into a pouch | crew | 3 | 1 pak-002 | 1 toi-022 | bladder -100 |
| urinate into a film pouch | crew | 3 | 1 toi-042 | 1 toi-022 | bladder -100 |
| use the bedpan | crew | 10 | 1 toi-030, 1 toi-003 | 1 toi-031 | bowel -100, bladder -100 |
| be sick into a bag | crew | 5 | 1 toi-033 | 1 toi-034 | toxin -8, satiety -15 |
| give a urine sample | crew | 3 | 1 toi-046 | 1 toi-047 | bladder -100 |
| give a stool sample | crew | 8 | 1 toi-046, 1 toi-003 | 1 toi-048 | bowel -100 |
| test a urine sample | crew | 5 | 1 toi-047, 1 sup-018 | 1 sup-047, 1 toi-001 | — |
| test a stool sample | crew | 10 | 1 toi-048, 1 sup-017 | 1 sup-047, 1 toi-002 | — |
| bag tank waste | toi.bagger | 15 | 2 toi-002, 1 toi-004, 1 pwr-001 | 1 toi-005 | — |
| double bag waste | toi.bagger | 10 | 1 toi-005, 1 toi-004, 1 pwr-001 | 1 toi-040 | — |
| rebag a leaking bag | crew | 15 | 1 toi-008, 1 toi-004 | 1 toi-005 | hygiene -5, cabin.clean +2 |
| dose a waste bag | crew | 5 | 1 toi-005, 1 toi-051 | 1 toi-039 | — |
| bag a soiled brief | crew | 5 | 1 toi-044, 1 toi-004 | 1 toi-005 | cabin.clean +1 |
| bag sanitary waste | crew | 5 | 2 toi-045, 1 toi-004 | 1 toi-005 | cabin.clean +1 |
| blow waste bag film | toi.bagger | 60 | 2 pol-001, 1 pwr-001 | 3 toi-042 | — |
| seal waste bags | toi.bagger | 30 | 1 toi-042, 1 pwr-001 | 4 toi-004 | — |
| seal bags from recycled film | toi.bagger | 30 | 2 scr-058, 1 pwr-001 | 4 toi-004 | — |
| fold a bag from plastic film | any.bench | 20 | 1 pol-002 | 2 toi-004 | — |
| roll waste bags | toi.bagger | 30 | 2 toi-042, 1 pwr-001 | 1 toi-041 | — |
| unroll waste bags | crew | 2 | 1 toi-041 | 8 toi-004 | — |
| seal gelling bags | toi.bagger | 30 | 2 toi-004, 1 toi-049, 1 pwr-001 | 2 toi-035 | — |
| press compostable bags | toi.bagger | 45 | 2 toi-056, 1 pwr-001 | 3 toi-037 | — |
| seal sick bags | toi.bagger | 20 | 1 toi-042, 1 pwr-001 | 4 toi-033 | — |
| sew absorbent briefs | toi.bagger | 45 | 1 hyg-029, 1 pol-002, 1 pwr-001 | 2 toi-043 | — |
| bale waste bags | toi.bagger | 30 | 4 toi-005, 1 toi-042, 1 pwr-001 | 1 toi-029 | — |
| load the waste tote | crew | 10 | 1 toi-026, 3 toi-005 | 1 toi-027 | cabin.clean +2 |
| unload the waste tote | crew | 10 | 1 toi-027 | 3 toi-005, 1 toi-026 | — |
| scrub a fouled tote | crew | 30 | 1 toi-028, 1 cln-008 | 1 toi-026, 2 toi-008 | hygiene -5 |
| fit a lid to a tote bin | any.bench | 30 | 1 pak-033, 1 pol-009 | 1 toi-026 | — |
| build a tote from recycled sheet | any.bench | 45 | 2 scr-055, 1 pol-009 | 1 toi-026 | — |
| fill a waste canister | toi.tank | 20 | 1 toi-023, 3 toi-002, 1 pwr-001 | 1 toi-024 | — |
| drain a waste canister | toi.tank | 30 | 1 toi-024, 1 pwr-001 | 1 toi-023, 2 toi-018 | — |
| vent a swollen canister | toi.tank | 30 | 1 toi-025, 1 pwr-001 | 1 toi-023, 2 toi-012 | cabin.clean -5 |
| fit a seal to a canister | any.bench | 30 | 1 pak-006, 1 pol-009 | 1 toi-023 | — |
| weld a waste canister | any.bench | 60 | 1 met-007, 1 pol-009 | 1 toi-023 | — |
| empty a urine jug | toi.tank | 10 | 1 toi-020 | 1 toi-019, 1 toi-017 | — |
| rinse a reeking jug | crew | 15 | 1 toi-021, 1 wat-002 | 1 toi-019, 1 toi-006 | cabin.clean -2 |
| fit a funnel to a bottle | any.bench | 20 | 1 pak-004, 1 pol-008 | 1 toi-019 | — |
| empty a urine pouch | toi.tank | 5 | 1 toi-022 | 1 toi-017, 1 pak-002 | — |
| store urine | toi.tank | 120 | 4 toi-001, 1 pwr-001 | 4 toi-017 | — |
| store diverted urine | toi.tank | 120 | 4 toi-013 | 4 toi-017 | — |
| hold black water | toi.tank | 60 | 3 toi-009, 1 toi-051 | 3 toi-018 | — |
| settle septic water | toi.tank | 120 | 3 toi-010, 1 toi-051, 1 pwr-001 | 2 toi-018 | cabin.clean +2 |
| empty the bedpan | crew | 10 | 1 toi-031 | 1 toi-030, 1 toi-002, 1 toi-001 | hygiene -3 |
| scrub a fouled bedpan | crew | 20 | 1 toi-032, 1 cln-008 | 1 toi-030, 1 toi-007 | hygiene -3 |
| shape a bedpan | any.bench | 45 | 2 pol-015 | 1 toi-030 | — |
| shape a bedpan from recycled sheet | any.bench | 45 | 2 scr-055 | 1 toi-030 | — |
| gel urine | crew | 5 | 2 toi-001, 1 toi-049 | 1 toi-050 | — |
| gel stale urine | crew | 5 | 2 toi-006, 1 toi-049 | 1 toi-050 | cabin.clean +2 |
| mix urine gelling powder | toi.chemmix | 60 | 1 pol-001, 1 chm-002, 1 pwr-001 | 4 toi-049 | — |
| press holding tank tablets | toi.chemmix | 60 | 1 chm-037, 1 chm-012, 1 pwr-001 | 4 toi-051 | — |
| culture composting enzyme | toi.chemmix | 90 | 1 bio-065, 1 grn-010, 1 pwr-001 | 3 toi-052 | — |
| chop straw litter | toi.chemmix | 30 | 2 grn-009, 1 pwr-001 | 3 toi-053 | — |
| dry coffee grounds for litter | crew | 15 | 2 bev-029 | 1 toi-053 | — |
| shred fibre litter | toi.chemmix | 30 | 2 scr-005, 1 pwr-001 | 3 toi-054 | — |
| shred lint litter | toi.chemmix | 30 | 3 cln-020, 1 pwr-001 | 2 toi-054 | — |
| mix charcoal litter | toi.chemmix | 30 | 2 toi-053, 1 fil-021, 1 pwr-001 | 3 toi-055 | — |
| mix bowl deodorizer | toi.chemmix | 45 | 1 chm-012, 1 hyg-018, 1 pwr-001 | 3 toi-062 | — |
| fill deodorizer spray | toi.chemmix | 30 | 1 hyg-018, 1 chm-004, 1 pak-027 | 1 toi-063 | — |
| fill deodorizer spray in a moulded bottle | toi.chemmix | 45 | 1 hyg-018, 1 chm-004, 1 pol-015, 1 pwr-001 | 1 toi-063 | — |
| pour freshener gel | toi.chemmix | 45 | 1 pol-021, 1 hyg-018, 1 pwr-001 | 2 toi-064 | — |
| mould urinal screens | toi.chemmix | 45 | 1 pol-015, 1 hyg-018, 1 pwr-001 | 2 toi-065 | — |
| mould sample cups | toi.chemmix | 30 | 1 pol-015, 1 pwr-001 | 6 toi-046 | — |
| pack a toilet odour filter | toi.chemmix | 45 | 1 fil-076, 1 fil-037, 1 pwr-001 | 1 toi-066 | — |
| recharge a toilet odour filter | toi.chemmix | 60 | 1 toi-067, 1 fil-021, 1 pwr-001 | 1 toi-066 | — |
| pad a toilet seat | any.bench | 60 | 1 toi-072, 1 pol-051, 1 fib-004 | 1 toi-068 | — |
| glue a cracked seat | any.bench | 30 | 1 toi-069, 1 pol-060 | 1 toi-072 | — |
| sew a privacy curtain | any.bench | 60 | 2 fib-067, 1 fib-010 | 1 toi-070 | — |
| mould a hand bidet bottle | any.bench | 20 | 1 pol-015, 1 pol-008 | 1 toi-071 | — |
| pulp fabric scraps | toi.tissue | 60 | 2 scr-005, 2 wat-002, 1 pwr-001 | 3 toi-056 | — |
| pulp cartons | toi.tissue | 60 | 2 pak-086, 1 wat-002, 1 pwr-001 | 3 toi-056 | — |
| pulp straw | toi.tissue | 90 | 3 grn-009, 2 wat-002, 1 pwr-001 | 3 toi-056 | — |
| press a parent roll | toi.tissue | 90 | 3 toi-056, 1 pwr-001 | 1 toi-057 | — |
| cut toilet paper | toi.tissue | 30 | 1 toi-057, 1 pwr-001 | 8 toi-003 | — |
| cut toilet paper by hand | any.bench | 30 | 1 toi-057 | 4 toi-003 | — |
| cut soft toilet paper | toi.tissue | 45 | 1 toi-057, 1 hyg-028, 1 pwr-001 | 6 toi-058 | — |
| press recycled paper by hand | any.bench | 60 | 2 toi-056 | 3 toi-059 | — |
| moisten toilet tissue | toi.tissue | 30 | 2 toi-003, 1 wat-001, 1 hyg-028 | 2 toi-060 | — |
| cut seat covers | toi.tissue | 30 | 1 toi-057, 1 pwr-001 | 10 toi-061 | — |
| wrap a toilet paper pack | toi.tissue | 15 | 6 toi-003, 1 pol-002 | 1 toi-100 | — |
| open a toilet paper pack | crew | 1 | 1 toi-100 | 6 toi-003 | — |
| mould a toilet seat | any.bench | 45 | 2 pol-015 | 1 toi-072 | — |
| cut toilet seal rings | any.bench | 20 | 1 pol-003 | 2 toi-073 | — |
| build a toilet flush valve | any.bench | 45 | 1 mec-007, 1 pol-009 | 1 toi-074 | — |
| build a toilet vent fan | any.bench | 45 | 1 mec-009, 1 pol-045 | 1 toi-075 | — |
| roll a compost toilet drum | any.bench | 90 | 2 met-009, 1 mec-004 | 1 toi-076 | — |
| bend a compost toilet crank | any.bench | 45 | 1 met-008, 1 mec-004 | 1 toi-077 | — |
| mould a diverter bowl insert | any.bench | 45 | 2 pol-015 | 1 toi-078 | — |
| fit a urine diverter hose | any.bench | 20 | 1 pol-008, 1 mec-014 | 1 toi-079 | — |
| fit a diverter hose from recycled tubing | any.bench | 20 | 1 scr-057, 1 mec-014 | 1 toi-079 | — |
| build a bidet nozzle | any.bench | 30 | 1 mec-049, 1 met-056 | 1 toi-080 | — |
| build a bidet water heater | any.bench | 60 | 1 thm-004, 1 met-056 | 1 toi-081 | — |
| build a vacuum toilet pump | any.bench | 60 | 1 mec-039, 1 mec-010 | 1 toi-082 | — |
| build a vacuum toilet valve | any.bench | 45 | 1 mec-033, 1 pol-009 | 1 toi-083 | — |
| cut a holding tank liner | any.bench | 60 | 2 pol-036 | 1 toi-084 | — |
| build a tank level float | any.bench | 30 | 1 pol-015, 1 met-008 | 1 toi-085 | — |
| build a bag sealer heat bar | any.bench | 45 | 1 met-047, 1 met-042 | 1 toi-086 | — |
| build a bag sealer roller | any.bench | 45 | 1 pol-003, 1 met-008 | 1 toi-087 | — |
| roll a tissue roller drum | any.bench | 90 | 1 met-056, 1 mec-004 | 1 toi-088 | — |
| grind tissue cutter blades | any.bench | 45 | 1 met-042 | 2 toi-089 | — |
| build a chemical mixer paddle | any.bench | 45 | 1 met-049, 1 met-034 | 1 toi-090 | — |
| cut dosing pump diaphragms | any.bench | 30 | 1 pol-055 | 2 toi-091 | — |
| assemble a composting toilet kit | any.bench | 120 | 1 fur-001, 1 toi-076, 1 toi-072, 1 mec-009 | 1 toi-092 | — |
| assemble a urine diverting toilet kit | any.bench | 120 | 1 fur-001, 1 toi-078, 1 toi-079, 1 toi-074 | 1 toi-093 | — |
| assemble a bidet toilet kit | any.bench | 120 | 1 fur-001, 1 toi-080, 1 toi-081, 1 toi-072 | 1 toi-094 | — |
| assemble a vacuum toilet kit | any.bench | 120 | 1 fur-001, 1 toi-082, 1 toi-083, 1 toi-072 | 1 toi-095 | — |
| assemble a holding tank kit | any.bench | 120 | 1 fur-001, 1 toi-084, 1 toi-085, 2 met-009 | 1 toi-096 | — |
| assemble a waste bag sealer kit | any.bench | 120 | 1 fur-001, 1 toi-086, 1 toi-087, 1 mec-010 | 1 toi-097 | — |
| assemble a tissue roller kit | any.bench | 120 | 1 fur-001, 1 toi-088, 1 toi-089, 1 mec-010 | 1 toi-098 | — |
| assemble a toilet chemical mixer kit | any.bench | 120 | 1 fur-001, 1 toi-090, 1 toi-091, 1 mec-039 | 1 toi-099 | — |

## Codex

| id | about | flavour |
|---|---|---|
| toi.compostloo | A dry toilet that covers waste with litter into a compost mix for the composter. | Crank five turns after each use. Turns are counted by the drum. Ref 5520/T. |
| toi.divertloo | A toilet that keeps urine and faeces apart, leaving clean urine and dry faeces. | FRONT: LIQUID. REAR: SOLID. SEE DIAGRAM. DIAGRAM IS ON THE LID. |
| toi.bidet | A toilet that washes as it flushes for better hygiene, leaving black water behind. | Warm water use is metered per visit. Meter readings are not disputed. |
| toi.vacloo | A powered toilet that draws waste away by suction and compacts it into pucks. | Seat seal before actuation. Proc 7 is printed on the bulkhead for a reason. |
| toi.tank | Holds and drains waste canisters, jugs and pouches, and stores urine and black water for sanitation. | Level float checked, liner intact, rev 11. Smell noted, not actionable. |
| toi.bagger | Blows plastic film and seals it into waste bags, gelling bags, sick bags and bales. | Every bag leaving the station is sealed here. Unsealed bags are refused at the slot. |
| toi.tissue | Pulps scraps, cartons and straw into paper, and cuts toilet paper, seat covers and moist tissue. | Paper output is rationed at source. Excess rolls are reallocated without notice. |
| toi.chemmix | Mixes litters, tank tablets, gelling powder, enzymes and deodorizers for the toilets. | IRRITANT. VENTILATE BEFORE OPENING HOPPER. COF SANITARY DIVISION. |
| toi-001 | Fresh urine; it goes stale if left, and treated it yields water and fertilizer. | Urine is reclaimable Company material. Discharge outside approved fixtures is waste of stock. |
| toi-002 | Solid body waste, to be bagged, composted or tanked before it turns putrid. | Everyone makes it. The rota says who moves it. |
| toi-003 | Plain toilet paper for using the toilet cleanly. | Issue: per visit, per policy. Policy sheet count under review since launch. |
| toi-004 | An empty waste bag for relieving into or for bagging tank waste. | CARRY ONE AT ALL TIMES. FIXTURE FAILURE IS NOT AN EXCUSE. |
| toi-005 | A sealed bag of waste bound for sanitation before it begins to leak. | Knot twice. Leaks traced to a station are billed to that station. |
| toi-006 | Urine left too long; still reclaimable, but it scales pipework if left further. | Ammonia level noted on Form 3U. Operator nose not a calibrated instrument. |
| toi-007 | Body waste that has putrefied, pressed or burnt by sanitation. | Detected before it is seen. Report it before it is reported. |
| toi-008 | A waste bag that has begun to leak, to be rebagged or burnt promptly. | GLOVES. DOUBLE GLOVES. THEN REBAG. |
| toi-009 | Flush water from the bidet toilet, held in the tank before it goes septic. | Classified as water for tank accounting purposes only. |
| toi-010 | Black water gone septic, settled in the tank or fed to the digester. | Septic events are logged against the station. Three events trigger an inspection. |
| toi-011 | Hard mineral scale left by long-stale urine, dissolved back by sanitation. | Pipe bore down eleven percent. Descale at next service. Tag 2207. |
| toi-012 | Toxic sludge from rotted waste, limed or burnt by sanitation. | BIOHAZARD. DO NOT OPEN. DO NOT VENT INTO CABIN. |
| toi-013 | Clean urine from the diverting toilet, ready for pasteurising or storage. | Separated at source. Credited to the station as recovered feedstock, Ref 8812/U. |
| toi-014 | Dried faeces from the diverting toilet, composted or hygienised by sanitation. | Drier than expected. Still not a topic for the door slot. |
| toi-015 | Waste and cover litter from the composting toilet, piled and cured into compost. | Feedstock grade C. Upgraded to soil on cure. Nobody upgrades the operator. |
| toi-016 | A compacted puck of waste from the vacuum toilet, dried by the composter. | Stackable. Do not stack in living space. Proc 19. |
| toi-017 | Urine held in the tank for later pasteurising. | Tank inventory is audited monthly. Discrepancies are assumed evaporated, then billed. |
| toi-018 | Settled slurry from the holding tank, sent to the digester or the sludge press. | Pump at low speed. High speed coats the bulkhead. Ask the last operator. |
| toi-019 | An empty jug for urinating into where no toilet is at hand. | LABEL CLEARLY. NOT FOR DRINKING WATER. EVER. |
| toi-020 | A filled urine jug, emptied into the holding tank before it reeks. | Lid torque per Proc 7 annex C. Tighter than that, actually. |
| toi-021 | A urine jug left too long, rinsed out to be used again. | No longer a container. Now a warning. |
| toi-022 | A sealed pouch of urine, emptied into the holding tank before it goes stale. | Pouch stock is shared with food service. Do not return unrinsed. |
| toi-023 | An empty rigid waste canister, filled at the holding tank. | Canisters are serialised. Lost canisters are deducted at cost. SN 4410 0021. |
| toi-024 | A filled waste canister, drained at the holding tank before it swells. | HEAVY. LIFT WITH LEGS. TWO-HAND CARRY. |
| toi-025 | A canister swollen with gas from rotting waste, vented with care at the holding tank. | Do not shake. Do not drop. Do not stand in line with the valve. |
| toi-026 | An empty lidded tote for carrying waste bags to sanitation. | Tote rota posted on the panel. The rota has not been updated since launch. |
| toi-027 | A tote full of waste bags, to be unloaded before it fouls. | Full totes are not to be left at the door slot overnight. Ref 6633/W. |
| toi-028 | A tote fouled by leaking bags, scrubbed with disinfectant for reuse. | Everyone believes it is somebody else's turn. It is yours. |
| toi-029 | A bale of waste bags pressed together for the incinerator. | Bale density per drawing 404. Loose bales are rebaled at the sender's cost. |
| toi-030 | A bedpan for an operator too ill to reach the toilet. | Sick leave is unpaid. Bedpans are provided at no charge. |
| toi-031 | A used bedpan, to be emptied promptly. | Empty within the hour. Medbay logs the hour. |
| toi-032 | A bedpan left too long, scrubbed with disinfectant for reuse. | Should have been emptied an hour ago. Nobody wrote down by whom. |
| toi-033 | An empty sealed sick bag kept ready for nausea. | Low gravity nausea is a known condition. Cleanup is the operator's own. |
| toi-034 | A filled sick bag, burnt by sanitation. | Better in the bag than on the bulkhead. Bulkhead cleaning is chargeable. |
| toi-035 | A waste bag lined with gelling powder that takes both kinds of waste at once. | EMERGENCY USE. ONE PER OPERATOR PER EVENT. |
| toi-036 | A filled gelling bag, burnt by sanitation. | Gelled, sealed, logged under contingency use. Form 2G. |
| toi-037 | A waste bag pressed from pulp that goes onto the compost pile with its contents. | Bag and contents rot at the same rate. One of few fair arrangements aboard. |
| toi-038 | A filled compostable bag, piled with the compost. | Direct to heap. No unpacking. No exceptions. |
| toi-039 | A waste bag dosed with a tank tablet so it keeps longer before sanitation. | Treatment buys time, not forgiveness. Collection schedule unchanged. |
| toi-040 | A waste bag sealed inside a second bag so it keeps longer before sanitation. | Double bagging is required where single bagging has failed. It has. |
| toi-041 | A roll of waste bags, torn off as needed. | Tear along the perforation. The perforation is advisory. |
| toi-042 | Blown plastic film, sealed into waste bags, sick bags, pouches and bales. | Gauge 40 micron. Thinner film was trialled once. Once. |
| toi-043 | An absorbent brief worn where no toilet can be reached; it takes up urine. | Issued for long shifts. Shift length is not negotiable. Briefs are. |
| toi-044 | A used absorbent brief, to be bagged before it putrefies. | Off, bagged, logged. In that order. |
| toi-045 | A used sanitary product, to be bagged before it putrefies. | Bag it, bin it. No form is required. A rare mercy. |
| toi-046 | A small lidded cup for giving urine or stool samples for testing. | FILL TO LINE. NOT PAST LINE. LID ON BEFORE TRANSPORT. |
| toi-047 | A urine sample, tested with a strip before it goes stale. | Samples are processed in order received. Order received is not order given. |
| toi-048 | A stool sample, tested with a strip before it putrefies. | Results are filed with the operator's health record. The record is Company property. |
| toi-049 | A polymer powder that sets urine into gel, used in gelling bags and absorbent cores. | Do not inhale. Do not add water to the tin. Proc 88. |
| toi-050 | Urine set into a spill-proof gel, burnt by sanitation. | Wobbles. Does not spill. Acceptable. |
| toi-051 | A tablet that keeps waste bags and tank water from turning septic. | One tablet per load. Doubling the dose doubles the cost, not the time. |
| toi-052 | A sachet of composting enzyme that speeds the toilet's compost; it loses strength over time. | Live culture. Use before date. The date is on the fold that tears off. |
| toi-053 | Chopped straw or dried grounds for covering waste in the composting toilet. | One scoop per visit. Scoop size Type 1. Do not improvise scoops. |
| toi-054 | Shredded fibre and lint for covering waste in the composting toilet. | Last cycle's laundry, this cycle's litter. Nothing aboard is wasted twice. |
| toi-055 | Cover litter mixed with charcoal that covers waste and absorbs its odour. | Charcoal stock is shared with filtration. Filtration has priority. |
| toi-056 | Wet pulp from scraps, cartons and straw, pressed into paper and bags. | Grey, wet, plentiful. The only thing aboard that is. |
| toi-057 | A large pressed roll of paper, cut down into toilet paper and seat covers. | PARENT ROLL. NOT FOR DIRECT USE. CUT BEFORE ISSUE. |
| toi-058 | A softer toilet paper that makes a toilet visit less unpleasant. | Soft grade is a morale allocation. Allocation reviewed against output. |
| toi-059 | Coarse paper pressed from pulp by hand; a poor but cheap toilet paper. | Meets minimum standard 2. There is no standard 1. |
| toi-060 | Moist tissue for a cleaner toilet visit; it dries out into plain paper if left. | Reseal the packet. Dried tissue is reclassified and issued as standard. |
| toi-061 | A paper seat cover that adds slight hygiene to a toilet visit. | Single operator per fixture. Covers issued regardless. Policy is policy. |
| toi-062 | A deodorizer dropped into the bowl that freshens the cabin once. | Turns the water blue. Blue is the colour of compliance. |
| toi-063 | A deodorizer spray that freshens the cabin once and leaves an empty spray bottle. | Two sprays. Air scrubbers flag a third as contamination. |
| toi-064 | A scented gel that keeps the cabin fresh while it slowly evaporates. | Fights a losing battle on a fixed budget. Relatable. |
| toi-065 | A scented screen set in the toilet that keeps the cabin cleaner; it wears into plastic scrap. | AIM HERE. |
| toi-066 | A charcoal filter on the toilet vent that keeps the cabin cleaner; it is recharged when spent. | Last barrier between toilet and bunk. Replace on schedule, Form 66F. |
| toi-067 | A toilet odour filter that has stopped working, recharged with fresh charcoal. | Spent. Everyone in the cabin already knows. |
| toi-068 | A padded toilet seat that makes sitting calmer; it cracks with wear. | Padding is not standard issue. Retention is tolerated pending audit. |
| toi-069 | A cracked toilet seat, glued to make a plain seat again. | Pinches. Glue it before it files a grievance on your behalf. |
| toi-070 | A curtain hung round the toilet that gives some privacy and calm; it wears into fabric scraps. | Privacy is not provisioned under the operating contract. Curtains are tolerated. |
| toi-071 | A squeeze bottle for rinsing clean at the toilet; it wears into plastic scrap. | Point first. Squeeze second. Proc 7 annex D, illustrated. |
| toi-072 | A spare toilet seat fitted to any toilet; it cracks when worn out. | Moulded to Company standard seat, one size. Complaints to Form 72S. |
| toi-073 | A spare seal ring fitted at a toilet's base to stop it leaking. | Small ring. Large consequence. Inspect each service. Tag 1180. |
| toi-074 | A spare flush valve fitted to any toilet; it wears into broken parts. | When this fails the deck finds out first. |
| toi-075 | A spare vent fan fitted to any toilet to clear its air; it wears into broken parts. | Duty cycle: continuous. Rated: intermittent. Running anyway. |
| toi-076 | A spare mixing drum fitted to the composting toilet; it wears into metal scrap. | Drum rotation logged. Reverse rotation voids warranty. |
| toi-077 | A spare drum crank fitted to the composting toilet; it wears into metal scrap. | Five turns after every use. Six, if the last operator only did four. |
| toi-078 | A spare bowl insert that separates urine from faeces in the urine diverting toilet. | Moulded divider, Type 2. Type 1 divided poorly. |
| toi-079 | A spare hose that carries urine away from the urine diverting toilet. | Check for kinks weekly. A kinked hose fills the bowl. |
| toi-080 | A spare washing nozzle fitted to the bidet toilet; it wears into metal scrap. | Descale monthly. Nozzle angle factory set. Do not adjust. |
| toi-081 | A spare water heater fitted to the bidet toilet; it wears into broken parts. | Heater element 230 V. Cold wash is a fault, not a feature. Report it. |
| toi-082 | A spare suction pump fitted to the vacuum toilet; it wears into broken parts. | Pump whine rising. Replace before failure. Inspector's initials illegible. |
| toi-083 | A spare flap valve fitted to the vacuum toilet; it wears into broken parts. | Closes so the line stays on its own side. Keep it that way. |
| toi-084 | A spare tank liner fitted to the waste holding tank; it wears into plastic scrap. | Fit liner before filling. Fitting after filling is not covered by Proc 30. |
| toi-085 | A spare level float fitted to the waste holding tank to show how full it is. | Rises with the level. Sticks at three quarters. Tap the housing. |
| toi-086 | A spare heat bar fitted to the waste bag sealer; it wears into metal scrap. | HOT BAR. SEALS FILM. SEALS SKIN. |
| toi-087 | A spare pinch roller fitted to the waste bag sealer; it wears into broken parts. | Rubber glazed, grip reduced, rev 3. Bags still sealed. Mostly. |
| toi-088 | A spare pressing drum fitted to the tissue roller; it wears into metal scrap. | Drum surface ground to finish 4. Fingerprints reduce it to finish 2. |
| toi-089 | A spare cutter blade fitted to the tissue roller; it wears into metal scrap. | SHARP. CUTS PAPER. CUTS OPERATORS. GUARD BEFORE SERVICE. |
| toi-090 | A spare mixing paddle fitted to the toilet chemical mixer; it wears into metal scrap. | Paddle pitted, still turning. Next one may not be. Tag 0090. |
| toi-091 | A spare dosing pump diaphragm fitted to the toilet chemical mixer; it wears into plastic scrap. | Dose accuracy depends on diaphragm age. Age is not recorded. |
| toi-092 | A crated kit that installs a composting toilet. | Installation reduces reliance on station fixtures. Reliance is noted, not rewarded. |
| toi-093 | A crated kit that installs a urine diverting toilet. | Two outlets, one seat, one manual. Manual missing pages four to nine. |
| toi-094 | A crated kit that installs a bidet toilet. | Classed as sanitary equipment, not comfort equipment, for tariff purposes. |
| toi-095 | A crated kit that installs a vacuum toilet. | High draw unit. Grid load to be declared on Form 14P before first use. |
| toi-096 | A crated kit that installs a waste holding tank. | Tank capacity is the station's responsibility once installed. So is overflow. |
| toi-097 | A crated kit that installs a waste bag sealer. | CRATE CONTAINS HEATING ELEMENT. DO NOT STORE AGAINST FILM. |
| toi-098 | A crated kit that installs a tissue roller. | Station paper self-sufficiency is encouraged. Ration levels remain unchanged. |
| toi-099 | A crated kit that installs a toilet chemical mixer. | Ships with no chemicals. Chemicals ship with no mixer. Procurement logic. |
| toi-100 | A wrapped pack of toilet paper rolls, opened as needed. | Packs are counted at each reassignment. Short packs follow the operator. |
