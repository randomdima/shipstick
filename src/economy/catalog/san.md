# Waste Treatment — `san`

Where every waste stream is made safe and comes back as something useful: grey water from washing, food scraps and
spoiled food from the galley and the table, and the body waste `toi` carries in. Grey water is settled, filtered and
disinfected back toward `wat`; urine, and the brine `wat` leaves reclaiming it, is pasteurised, stripped of ammonia
and crystallised into urea and salts; scraps, faeces
and sludge are hot-composted, digested into biogas and digestate, pressed, limed or burned to ash. The goods leave as
sanitised feedstock for `soi`'s fertilizers (compost, humanure, digestate, biosolids, urea, phosphate ash, biochar),
treated water for `wat`, and heat from biogas for the cabin. Left untreated, waste only turns worse: stale, rotting,
mouldering.

## Devices

| id | device | role | cells |
|---|---|---|---|
| san.reclaimer | RT200 Grey Water Reclaimer | sanit | 2x2 |
| san.urineproc | RT210 Urine Nutrient Extractor | sanit | 2x1 |
| san.digester | RT400 Anaerobic Digester | sanit | 2x2 |
| san.composter | RT310 Composter | sanit | 2x2 |
| san.press | RT520 Sludge Press | sanit | 2x1 |
| san.pelletizer | RT530 Biosolids Pelletizer | sanit | 2x1 |
| san.burner | RT600 Biogas Burner | sanit | 1x1 |
| san.incinerator | RT900 Waste Incinerator | sanit | 2x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| san-001 | Water, Grey | — | 72 h → san-006 |
| san-002 | Scraps, Food | — | 72 h → san-003 |
| san-003 | Food, Spoiled | — | 168 h → san-007 |
| san-004 | Water, Grey, Treated | — | 168 h → san-006 |
| san-005 | Compost, Sanitised | — | — |
| san-006 | Water, Grey, Stale | — | — |
| san-007 | Slop, Rotting | — | 336 h → san-075 |
| san-008 | Biogas, Raw | — | — |
| san-009 | Biosolids, Treated | — | — |
| san-010 | Digestate | — | — |
| san-011 | Urine, Stripped | — | — |
| san-012 | Urea, Crystalline | — | — |
| san-013 | Water, Grey, Settled | — | 48 h → san-006 |
| san-014 | Water, Grey, Filtered | — | 96 h → san-006 |
| san-015 | Water, Grey, Disinfected | — | 168 h → san-006 |
| san-016 | Water, Grey, Greasy | — | 48 h → san-006 |
| san-017 | Backwash, Grey Water | — | 48 h → san-006 |
| san-018 | Brine, Reject, Grey Water | — | — |
| san-019 | Sludge, Grey Water | — | — |
| san-020 | Culture, Activated Sludge | — | 168 h → san-019 |
| san-021 | Water, Washdown | cabin.clean +5, leaves 1 san-001 | 168 h → san-006 |
| san-022 | Skim, Grease | — | 120 h → san-023 |
| san-023 | Fatberg | — | — |
| san-024 | Grease, Rendered | — | — |
| san-025 | Urine, Pretreated | — | — |
| san-026 | Cake, Septage | — | — |
| san-027 | Urine, Pasteurised | — | — |
| san-028 | Mother Liquor, Urea | — | — |
| san-029 | Cake, Salt, Brine | — | — |
| san-030 | Water, Ammonia, Stripped | — | — |
| san-031 | Sulfate, Ammonium | — | — |
| san-032 | Mash, Scrap | — | 48 h → san-007 |
| san-033 | Mix, Wet Waste | — | 72 h → san-007 |
| san-034 | Scraps, Food, Dried | — | — |
| san-035 | Feed, Scrap, Pasteurised | — | — |
| san-036 | Liquor, Scrap Press | — | 48 h → san-007 |
| san-037 | Caddy, Scrap | — | — |
| san-038 | Caddy, Scrap, Full | — | 96 h → san-039 |
| san-039 | Caddy, Scrap, Fouled | — | — |
| san-040 | Mix, Compost Pile | — | — |
| san-041 | Compost, Hot | — | — |
| san-042 | Starter, Compost | — | 336 h |
| san-043 | Humanure, Cured | — | — |
| san-044 | Cake, Faeces, Hygienised | — | — |
| san-045 | Brick, Compost | — | — |
| san-046 | Slurry, Digester Feed | — | 72 h → san-007 |
| san-047 | Inoculum, Digester | — | 336 h → san-019 |
| san-048 | Scum, Digester | — | — |
| san-049 | Grit, Digester | — | — |
| san-050 | Fibre, Digestate | — | — |
| san-051 | Biogas, Scrubbed | — | — |
| san-052 | Biomethane | — | — |
| san-053 | Condensate, Biogas | — | — |
| san-054 | Media, Biogas Scrubber | — | — |
| san-055 | Media, Biogas Scrubber, Spent | — | — |
| san-056 | Canister, Biogas | — | — |
| san-057 | Cartridge, Biogas Heater | cabin.heat +6, cabin.co2 +2, leaves 1 pak-006 | — |
| san-058 | Cake, Sludge | — | — |
| san-059 | Filtrate, Sludge Press | — | 48 h → san-006 |
| san-060 | Biosolids, Dried | — | — |
| san-061 | Pellet, Biosolid | — | — |
| san-062 | Sludge, Limed | — | — |
| san-063 | Sludge, Sterilised | — | — |
| san-064 | Biochar, Sludge | — | — |
| san-065 | Ash, Waste Incinerator | — | — |
| san-066 | Ash, Phosphate | — | — |
| san-067 | Clinker, Waste Incinerator | — | — |
| san-068 | Water, Flue Scrubber | — | — |
| san-069 | Bag, Clinical Waste | — | — |
| san-070 | Block, Odour, Treatment | cabin.clean +1/h | 240 h → san-071 |
| san-071 | Block, Odour, Spent | — | — |
| san-072 | Media, Odour Biofilter | cabin.clean +1/h | 336 h → san-073 |
| san-073 | Media, Odour Biofilter, Spent | — | — |
| san-074 | Insert, Grease Trap | cabin.clean +1/h | 120 h → san-022 |
| san-075 | Refuse, Mouldering | — | — |
| san-076 | Pack, Compost Heat | cabin.heat +4, leaves 1 san-041 | — |
| san-077 | Membrane, Grey Water Reclaimer | fits san.reclaimer, leaves 1 fil-016 | — |
| san-078 | Pump Seal, Grey Water Reclaimer | fits san.reclaimer, leaves 1 scr-002 | — |
| san-079 | Packing, Ammonia Stripper | fits san.urineproc, leaves 1 cer-086 | — |
| san-080 | Heater, Crystallizer | fits san.urineproc, leaves 1 scr-004 | — |
| san-081 | Mixer Blade, Anaerobic Digester | fits san.digester, leaves 1 scr-001 | — |
| san-082 | Gas Valve, Anaerobic Digester | fits san.digester, leaves 1 scr-004 | — |
| san-083 | Auger, Composter | fits san.composter, leaves 1 scr-001 | — |
| san-084 | Fan, Aerator, Composter | fits san.composter, leaves 1 scr-004 | — |
| san-085 | Filter Cloth, Sludge Press | fits san.press, leaves 1 scr-005 | — |
| san-086 | Platen, Sludge Press | fits san.press, leaves 1 scr-001 | — |
| san-087 | Die, Biosolids Pelletizer | fits san.pelletizer, leaves 1 scr-001 | — |
| san-088 | Roller, Biosolids Pelletizer | fits san.pelletizer, leaves 1 scr-001 | — |
| san-089 | Nozzle, Biogas Burner | fits san.burner, leaves 1 scr-001 | — |
| san-090 | Igniter, Biogas Burner | fits san.burner, leaves 1 scr-003 | — |
| san-091 | Grate, Waste Incinerator | fits san.incinerator, leaves 1 scr-001 | — |
| san-092 | Refractory, Waste Incinerator | fits san.incinerator, leaves 1 cer-086 | — |
| san-093 | Kit, Grey Water Reclaimer | installs san.reclaimer | — |
| san-094 | Kit, Urine Nutrient Extractor | installs san.urineproc | — |
| san-095 | Kit, Anaerobic Digester | installs san.digester | — |
| san-096 | Kit, Composter | installs san.composter | — |
| san-097 | Kit, Sludge Press | installs san.press | — |
| san-098 | Kit, Biosolids Pelletizer | installs san.pelletizer | — |
| san-099 | Kit, Biogas Burner | installs san.burner | — |
| san-100 | Kit, Waste Incinerator | installs san.incinerator | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| settle grey water | san.reclaimer | 60 | 4 san-001, 1 pwr-001 | 3 san-013, 1 san-022 | — |
| let grey water stand | any.bench | 240 | 3 san-001 | 2 san-013, 1 san-019 | — |
| settle backwash water | san.reclaimer | 60 | 3 san-017, 1 pwr-001 | 2 san-013, 1 san-019 | — |
| revive stale grey water | san.reclaimer | 120 | 3 san-006, 1 san-020, 1 pwr-001 | 2 san-013, 1 san-019 | — |
| sand filter grey water | san.reclaimer | 60 | 3 san-013, 1 fil-035, 1 pwr-001 | 3 san-014, 1 san-017, 1 fil-036 | — |
| treat grey water with activated sludge | san.reclaimer | 120 | 4 san-013, 1 san-020, 1 pwr-001 | 3 san-014, 1 san-019 | — |
| grow activated sludge | san.reclaimer | 180 | 2 san-019, 1 san-013, 1 pwr-001 | 2 san-020 | — |
| ultrafilter grey water | san.reclaimer | 90 | 3 san-014, 1 fil-049, 1 pwr-001 | 3 san-015, 1 fil-050 | — |
| chlorinate grey water | san.reclaimer | 30 | 3 san-014, 1 chm-037, 1 pwr-001 | 3 san-015 | — |
| shine ultraviolet on grey water | san.reclaimer | 45 | 3 san-014, 2 pwr-001 | 2 san-015 | — |
| polish disinfected water with carbon | san.reclaimer | 90 | 3 san-015, 1 fil-013, 1 pwr-001 | 3 san-004, 1 fil-014 | — |
| reverse osmose disinfected water | san.reclaimer | 120 | 4 san-015, 1 pwr-001 | 3 san-004, 1 san-018 | — |
| release treated water to the tanks | san.reclaimer | 30 | 2 san-004, 1 pwr-001 | 2 wat-002 | — |
| run treated water to the farm | crew | 10 | 2 san-004 | 2 wat-042 | — |
| mix washdown water | san.reclaimer | 15 | 2 san-014, 1 chm-037 | 3 san-021 | — |
| wring washdown water by hand | crew | 10 | 2 san-013 | 1 san-021 | — |
| return condensate to the reclaimer | san.reclaimer | 15 | 2 san-053 | 1 san-013 | — |
| return press filtrate | san.reclaimer | 30 | 3 san-059, 1 pwr-001 | 2 san-013, 1 san-019 | — |
| settle flue scrubber water | san.reclaimer | 60 | 3 san-068, 1 chm-017 | 2 san-013, 1 san-058 | — |
| skim greasy water | san.press | 45 | 3 san-016, 1 pwr-001 | 2 san-022, 2 san-013 | — |
| render grease skim | san.press | 90 | 3 san-022, 1 pwr-001 | 2 san-024, 1 san-019 | — |
| break up a fatberg | san.press | 120 | 2 san-023, 1 chm-002, 1 pwr-001 | 1 san-024, 1 san-058 | — |
| render used frying oil | san.press | 60 | 2 ing-042, 1 pwr-001 | 2 san-024 | — |
| pack a grease trap insert | san.press | 30 | 1 fil-037, 1 met-057 | 1 san-074 | — |
| pasteurise urine | san.urineproc | 60 | 4 toi-001, 1 pwr-001 | 4 san-027 | — |
| pasteurise stored urine | san.urineproc | 45 | 4 toi-017, 1 pwr-001 | 4 san-027 | — |
| pasteurise diverted urine | san.urineproc | 45 | 4 toi-013, 1 pwr-001 | 4 san-027 | — |
| acidify stale urine | san.urineproc | 60 | 4 toi-006, 1 chm-001, 1 pwr-001 | 3 san-025 | cabin.clean +2 |
| dose urine with pretreat | san.urineproc | 30 | 4 toi-001, 1 wat-068 | 4 san-025 | — |
| dilute urine for the farm | san.urineproc | 30 | 2 san-027, 2 wat-002 | 3 soi-004 | — |
| strip ammonia from urine | san.urineproc | 90 | 4 san-027, 1 chm-002, 1 pwr-001 | 3 san-011, 1 san-030 | — |
| strip ammonia from pretreated urine | san.urineproc | 90 | 4 san-025, 1 chm-017, 1 pwr-001 | 3 san-011, 1 san-030 | — |
| concentrate stripped urine | san.urineproc | 120 | 4 san-011, 2 pwr-001 | 2 wat-015, 1 san-028 | — |
| absorb ammonia into acid | san.urineproc | 60 | 3 san-030, 1 chm-001, 1 pwr-001 | 2 san-031 | — |
| distil ammonia | san.urineproc | 90 | 3 san-030, 1 pwr-001 | 1 chm-003 | — |
| crystallise urea | san.urineproc | 120 | 4 san-027, 2 pwr-001 | 1 san-012, 2 san-028 | — |
| crystallise urine brine | san.urineproc | 120 | 3 wat-017, 1 pwr-001 | 1 san-012, 1 san-029 | — |
| dry mother liquor | san.urineproc | 90 | 3 san-028, 1 pwr-001 | 1 san-029 | — |
| evaporate reject brine | san.urineproc | 120 | 3 san-018, 2 pwr-001 | 1 san-029 | — |
| dissolve urine scale | san.urineproc | 45 | 2 toi-011, 1 chm-029 | 1 san-029, 1 san-028 | — |
| leach potash from salt cake | san.urineproc | 60 | 2 san-029, 1 wat-002 | 1 soi-007, 1 san-018 | — |
| blend nitrogen salts | san.pelletizer | 60 | 2 san-012, 1 san-031, 1 pwr-001 | 2 soi-005 | — |
| mash food scraps | san.composter | 30 | 3 san-002, 1 pwr-001 | 3 san-032 | — |
| mash scraps by hand | crew | 20 | 2 san-002 | 1 san-032 | — |
| mash spoiled food | san.composter | 30 | 3 san-003, 1 pwr-001 | 2 san-032 | cabin.clean +2 |
| fill the scrap caddy | crew | 5 | 1 san-037, 3 san-002 | 1 san-038 | cabin.clean +1 |
| empty the scrap caddy | san.composter | 10 | 1 san-038 | 1 san-037, 3 san-032 | — |
| scrub a fouled caddy | crew | 20 | 1 san-039, 1 cln-008 | 1 san-037, 2 san-003 | hygiene -3 |
| fit a lid to a caddy | any.bench | 30 | 1 pol-015, 1 pol-009 | 1 san-037 | — |
| dry food scraps | san.composter | 120 | 4 san-002, 2 pwr-001 | 2 san-034 | — |
| pasteurise scrap feed | san.composter | 60 | 3 san-032, 1 pwr-001 | 2 san-035 | — |
| grind dried scraps into feed | san.composter | 30 | 2 san-034 | 2 san-035 | — |
| mix insect feed | san.composter | 30 | 2 san-035, 1 grn-010 | 2 prt-016 | — |
| press food scraps | san.press | 45 | 4 san-032, 1 pwr-001 | 2 san-036, 2 san-040 | — |
| build a compost pile | san.composter | 60 | 2 san-032, 1 toi-053, 1 grn-009 | 3 san-040 | — |
| heap compost by hand | crew | 60 | 4 san-032, 1 toi-053 | 2 san-040 | — |
| build a humanure pile | san.composter | 60 | 3 toi-015, 1 grn-009 | 3 san-040 | — |
| add dry faeces to the pile | san.composter | 60 | 2 toi-014, 2 san-032 | 3 san-040 | — |
| pile compostable bags | san.composter | 60 | 2 toi-038, 1 toi-053 | 3 san-040 | — |
| pile digestate fibre | san.composter | 30 | 2 san-050, 2 san-032 | 3 san-040 | — |
| pile spent biofilter media | san.composter | 30 | 2 san-073, 2 san-032 | 3 san-040 | — |
| pile floor sweepings | san.composter | 30 | 3 cln-012, 2 san-032 | 3 san-040 | — |
| pile hair and lint | san.composter | 30 | 2 hyg-030, 2 cln-020, 2 san-032 | 3 san-040 | — |
| pile rotten rags | san.composter | 30 | 2 scr-076, 2 san-032 | 3 san-040 | — |
| hot compost with starter | san.composter | 360 | 4 san-040, 1 san-042, 1 pwr-001 | 3 san-041 | — |
| hot compost slowly | san.composter | 720 | 4 san-040, 1 pwr-001 | 2 san-041 | — |
| keep back compost starter | san.composter | 30 | 1 san-041 | 2 san-042 | — |
| culture compost starter | san.composter | 120 | 1 san-005, 1 bio-065, 1 grn-010 | 3 san-042 | — |
| cure compost | san.composter | 720 | 3 san-041 | 3 san-005 | — |
| cure humanure | san.composter | 720 | 4 toi-015, 1 san-042 | 3 san-043 | — |
| blend humanure for the garden | san.composter | 60 | 2 san-043, 1 san-005 | 3 soi-002 | — |
| hygienise dry faeces | san.composter | 240 | 3 toi-014, 2 pwr-001 | 2 san-044 | — |
| dry vacuum pucks | san.composter | 180 | 3 toi-016, 2 pwr-001 | 2 san-044 | — |
| bag hot compost for warmth | san.composter | 20 | 1 san-041, 1 thm-081 | 1 san-076 | — |
| pack biofilter media | san.composter | 60 | 2 san-005, 1 soi-042 | 2 san-072 | — |
| charge sludge biochar | san.composter | 60 | 2 san-064, 1 san-010 | 2 soi-044 | — |
| press compost bricks | san.press | 45 | 3 san-005, 1 pwr-001 | 2 san-045 | — |
| soak a compost brick | crew | 10 | 1 san-045, 1 wat-002 | 2 san-005 | — |
| mix wet waste | san.digester | 20 | 2 san-032, 2 toi-018 | 4 san-033 | — |
| open waste bags into the digester | san.digester | 20 | 3 toi-005 | 3 san-033, 1 scr-002 | — |
| open treated bags into the digester | san.digester | 20 | 3 toi-039 | 3 san-033, 1 scr-002 | — |
| open double bags into the digester | san.digester | 20 | 2 toi-040 | 2 san-033, 1 scr-002 | — |
| make digester feed | san.digester | 30 | 3 san-033, 1 pwr-001 | 3 san-046 | — |
| feed the digester press liquor | san.digester | 30 | 3 san-036, 1 toi-018 | 3 san-046 | — |
| feed the digester septic water | san.digester | 30 | 3 toi-010, 1 san-032 | 3 san-046 | — |
| feed the digester rotting slop | san.digester | 30 | 3 san-007, 1 wat-002 | 3 san-046 | cabin.clean +2 |
| feed the digester mouldering refuse | san.digester | 45 | 2 san-075, 1 wat-002 | 2 san-046 | cabin.clean +2 |
| seed digester inoculum | san.digester | 240 | 2 san-019, 1 bio-067 | 2 san-047 | — |
| grow inoculum from slurry | san.digester | 480 | 3 san-046 | 1 san-047 | — |
| digest slurry | san.digester | 480 | 4 san-046, 1 san-047, 1 pwr-001 | 3 san-008, 3 san-010, 1 san-048, 1 san-049 | — |
| digest slurry slowly | san.digester | 720 | 4 san-046, 1 pwr-001 | 2 san-008, 3 san-010, 1 san-048 | — |
| pack scrubber media | san.digester | 30 | 2 met-060, 1 fil-021 | 2 san-054 | — |
| regenerate scrubber media | san.digester | 60 | 2 san-055, 1 gas-001 | 1 san-054, 1 ore-080 | — |
| scrub biogas | san.digester | 60 | 3 san-008, 1 san-054, 1 pwr-001 | 2 san-051, 1 san-055, 1 san-053 | — |
| upgrade biogas | san.digester | 90 | 3 san-051, 1 pwr-001 | 2 san-052, 1 gas-002 | — |
| bottle biogas | san.digester | 30 | 2 san-051, 1 pak-006 | 1 san-056 | — |
| bottle biogas in a welded canister | san.digester | 60 | 2 san-051, 1 met-007, 1 pwr-001 | 1 san-056 | — |
| bottle biomethane | san.digester | 30 | 2 san-052, 1 pak-006, 1 pwr-001 | 1 gas-013 | — |
| feed biomethane to the gas line | san.digester | 30 | 2 san-052 | 2 gas-010 | — |
| separate digestate | san.press | 60 | 3 san-010, 1 pwr-001 | 2 san-050, 2 san-059 | — |
| skim digester scum | san.press | 60 | 2 san-048 | 1 san-022, 1 san-058 | — |
| wash digester grit | san.press | 30 | 3 san-049, 1 wat-002 | 2 ore-050, 1 san-013 | — |
| burn raw biogas | san.burner | 60 | 2 san-008 | 1 gas-002 | cabin.heat +6 |
| burn scrubbed biogas | san.burner | 60 | 2 san-051 | 1 gas-002, 1 san-053 | cabin.heat +10 |
| burn a biogas canister | san.burner | 90 | 1 san-056 | 1 pak-006, 1 gas-002 | cabin.heat +12 |
| fill a biogas heater cartridge | san.burner | 20 | 1 san-056 | 1 san-057 | — |
| boil water over biogas | san.burner | 30 | 1 san-008, 2 wat-002 | 2 wat-001 | — |
| burn rendered grease | san.burner | 60 | 2 san-024 | 1 gas-002 | cabin.heat +8 |
| burn biosolid pellets | san.burner | 60 | 3 san-061 | 1 san-065 | cabin.heat +6 |
| burn faeces cake | san.burner | 60 | 2 san-044 | 1 san-065 | cabin.heat +5 |
| press reclaimer sludge | san.press | 60 | 3 san-019, 1 pwr-001 | 1 san-058, 2 san-059 | — |
| press tank slurry | san.press | 60 | 3 toi-018, 1 pwr-001 | 1 san-026, 2 san-059 | — |
| press septic water | san.press | 90 | 4 toi-010, 1 pwr-001 | 1 san-026, 3 san-059 | cabin.clean +2 |
| press putrid waste | san.press | 90 | 3 toi-007, 1 pwr-001 | 1 san-026, 1 san-059 | cabin.clean +3 |
| lime toxic faecal sludge | san.press | 90 | 3 toi-012, 1 chm-017 | 2 san-062 | cabin.clean +3 |
| press water works sludge | san.press | 60 | 3 wat-034, 1 pwr-001 | 1 san-058, 1 wat-002 | — |
| press filter sludge cake | san.press | 30 | 2 fil-043 | 1 san-058 | — |
| lime sludge cake | san.press | 60 | 2 san-058, 1 chm-016 | 2 san-062 | — |
| lime septage cake | san.press | 60 | 2 san-026, 1 chm-016 | 2 san-062 | — |
| sterilise limed sludge | san.press | 120 | 2 san-062, 2 pwr-001 | 2 san-063 | — |
| steam sterilise sludge | san.press | 180 | 2 san-058, 3 pwr-001 | 2 san-063 | — |
| air dry sludge cake | crew | 720 | 3 san-058 | 1 san-060 | — |
| dry sterilised sludge | san.pelletizer | 180 | 3 san-063, 2 pwr-001 | 2 san-060 | — |
| treat biosolids | san.pelletizer | 120 | 3 san-060, 1 chm-017, 1 pwr-001 | 3 san-009 | — |
| pellet biosolids | san.pelletizer | 60 | 3 san-009, 1 pwr-001 | 3 san-061 | — |
| pellet faeces cake | san.pelletizer | 60 | 3 san-044, 1 pwr-001 | 2 san-061 | — |
| acidulate phosphate ash | san.pelletizer | 90 | 2 san-066, 1 chm-001 | 2 soi-006 | — |
| char dried biosolids | san.incinerator | 120 | 3 san-060, 2 pwr-001 | 2 san-064 | — |
| press odour blocks | san.press | 45 | 2 san-064, 1 fil-023 | 2 san-070 | — |
| bake spent odour blocks | san.incinerator | 60 | 3 san-071, 1 pwr-001 | 2 san-070 | — |
| incinerate waste bales | san.incinerator | 120 | 2 toi-029, 2 pwr-001 | 1 san-065, 1 san-068 | cabin.heat +4 |
| incinerate gelled waste | san.incinerator | 90 | 2 toi-036, 2 toi-050, 2 pwr-001 | 1 san-065, 1 san-068 | cabin.heat +3 |
| incinerate leaking bags | san.incinerator | 90 | 3 toi-008, 2 pwr-001 | 1 san-065, 1 san-068 | cabin.clean +5 |
| incinerate sick bags | san.incinerator | 60 | 3 toi-034, 1 pwr-001 | 1 san-065 | cabin.clean +2 |
| incinerate putrid waste | san.incinerator | 120 | 3 toi-007, 2 pwr-001 | 1 san-065, 1 san-068 | cabin.clean +3 |
| incinerate toxic sludge | san.incinerator | 120 | 2 toi-012, 2 pwr-001 | 1 san-065, 1 san-068 | cabin.clean +3 |
| incinerate mouldering refuse | san.incinerator | 90 | 3 san-075, 2 pwr-001 | 1 san-065 | cabin.clean +3 |
| bag clinical waste | crew | 10 | 2 sup-046, 1 sup-047, 1 toi-004 | 1 san-069 | — |
| incinerate clinical waste | san.incinerator | 90 | 2 san-069, 1 pwr-001 | 1 san-065, 1 san-067 | — |
| incinerate soiled dressings | san.incinerator | 60 | 2 sup-043, 2 sup-044, 1 pwr-001 | 1 san-065 | — |
| incinerate biosolid pellets for phosphate | san.incinerator | 120 | 3 san-061, 2 pwr-001 | 2 san-066 | cabin.heat +4 |
| sift incinerator ash | crew | 20 | 3 san-065 | 1 san-066, 1 san-067 | — |
| build a reclaimer membrane | any.bench | 60 | 1 fil-015, 1 pol-052 | 1 san-077 | — |
| cut reclaimer pump seals | any.bench | 30 | 1 pol-054, 1 pol-009 | 2 san-078 | — |
| fire ammonia stripper packing | any.bench | 45 | 1 cer-045 | 1 san-079 | — |
| build a crystallizer heater | any.bench | 45 | 1 thm-004, 1 met-056 | 1 san-080 | — |
| build a digester mixer blade | any.bench | 45 | 1 met-034, 1 mec-006 | 1 san-081 | — |
| build a digester gas valve | any.bench | 30 | 1 mec-007, 1 pol-009 | 1 san-082 | — |
| build a composter auger | any.bench | 60 | 1 met-008, 1 met-009 | 1 san-083 | — |
| build a composter aerator fan | any.bench | 45 | 1 mec-009, 1 met-057 | 1 san-084 | — |
| sew a press filter cloth | any.bench | 30 | 2 fib-008 | 1 san-085 | — |
| cut a sludge press platen | any.bench | 60 | 2 met-005 | 1 san-086 | — |
| grind a pelletizer die | any.bench | 60 | 1 met-030 | 1 san-087 | — |
| build a pelletizer roller | any.bench | 60 | 1 met-008, 1 mec-004 | 1 san-088 | — |
| turn burner nozzles | any.bench | 30 | 1 met-051 | 2 san-089 | — |
| build a burner igniter | any.bench | 30 | 1 cer-035, 1 met-047 | 1 san-090 | — |
| cast an incinerator grate | any.bench | 60 | 2 met-021 | 1 san-091 | — |
| cut incinerator refractory bricks | any.bench | 30 | 1 cer-042, 1 cer-006 | 2 san-092 | — |
| assemble a grey water reclaimer kit | any.bench | 150 | 1 fur-001, 1 san-077, 1 san-078, 1 mec-008 | 1 san-093 | — |
| assemble a urine nutrient extractor kit | any.bench | 120 | 1 fur-001, 1 san-079, 1 san-080, 1 mec-039 | 1 san-094 | — |
| assemble an anaerobic digester kit | any.bench | 150 | 1 fur-001, 1 san-081, 1 san-082, 2 met-009 | 1 san-095 | — |
| assemble a composter kit | any.bench | 120 | 1 fur-001, 1 san-083, 1 san-084 | 1 san-096 | — |
| assemble a sludge press kit | any.bench | 120 | 1 fur-001, 1 san-085, 1 san-086, 1 mec-043 | 1 san-097 | — |
| assemble a biosolids pelletizer kit | any.bench | 120 | 1 fur-001, 1 san-087, 1 san-088, 1 mec-010 | 1 san-098 | — |
| assemble a biogas burner kit | any.bench | 90 | 1 fur-001, 1 san-089, 1 san-090 | 1 san-099 | — |
| assemble a waste incinerator kit | any.bench | 150 | 1 fur-001, 1 san-091, 1 san-092, 1 mec-009 | 1 san-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| san.reclaimer | Settles, filters and disinfects grey water until it can return to the tanks or the farm. | All water aboard is reclaimed water. Operators are reminded of this at every wash. |
| san.urineproc | Pasteurises urine and separates it into ammonia, urea and salts for the farm's fertilizers. | NUTRIENTS IN. NUTRIENTS OUT. DO NOT OPEN HATCH UNDER PRESSURE. |
| san.digester | A sealed tank in which microbes turn slurry and slop into biogas and digestate. | Vents audibly during night cycle. Normal. Do not log as a fault. Ref 4004/D. |
| san.composter | Mashes scraps, builds piles and hot-composts them into sanitised compost, starter and feed. | Pile core temperature checked, nominal, rev 9. Operator nose also checked. Also nominal. |
| san.press | Presses water out of sludge, scraps and grease, and limes or sterilises the solids left. | Log, third shift: press jammed on a fatberg. Fatberg prevailed. Clearance pending. |
| san.pelletizer | Dries and treats biosolids and rolls them into pellets and fertilizer blends. | Pellet output is farm stock. Diversion to heating requires Form 53B. |
| san.burner | Burns biogas, grease and dried waste for cabin heat and boiling water. | Heat from waste is billed at the same rate as heat from the grid. |
| san.incinerator | Burns what cannot be recovered down to ash, clinker and scrubber water. | FINAL DISPOSAL POINT. NO RETRIEVAL. CHECK POCKETS. |
| san-001 | Used water from washing and cleaning; it turns stale if not treated soon. | Grey water discharge per operator is recorded and compared with the fleet mean. |
| san-002 | Peelings, crusts and leftovers from the galley and the table, for composting or mashing. | Leftovers indicate over-issue. Rations will be adjusted to match. |
| san-003 | Food gone off, mashed for the composter before it rots further. | Spoilage is reported on Form 27B within one shift. Proc 114 applies. |
| san-004 | Grey water fully treated, fit to return to the tanks or the farm. | Meets potable standard 3 on release. Nobody volunteers to test it first. |
| san-005 | Cured, pathogen-free compost from which the farm's growth media are made. | Plate to pile to plant to plate. Logged at each step, Proc 210. |
| san-006 | Grey water left too long, recovered only with culture and settling. | Smells of a locker nobody has opened since launch. |
| san-007 | Spoiled food gone wet and foul, fed to the digester before it moulders. | DO NOT OPEN INDOORS. ALL SPACES ABOARD ARE INDOORS. |
| san-008 | Unscrubbed gas from the digester, burned for heat or scrubbed for cleaner use. | FLAMMABLE GAS. HYDROGEN SULPHIDE PRESENT. NO OPEN FLAME OUTSIDE BURNER. |
| san-009 | Dried biosolids treated safe, ready to roll into pellets. | Certified harmless on Form 9H. Signature on Form 9H illegible. |
| san-010 | The wet nutrient-rich remains of digestion, used by the farm and the bio lab. | Digester output is reclassified from waste to feedstock on exit. Value assigned accordingly. |
| san-011 | Pasteurised urine with its ammonia removed, ready to concentrate into water and brine. | Halfway between waste and resource. Status reviewed per batch. |
| san-012 | Urea crystallised from urine, dissolved or granulated into nitrogen fertilizer. | White, clean, and on record as recovered operator output. |
| san-013 | Grey water with grease and grit settled out; the first stage of every treatment. | Stage 1 of 5. Do not skip stages to meet quota. |
| san-014 | Settled grey water passed through a filter, ready to disinfect or mix as washdown water. | Clearer. Not yet cleared for use. |
| san-015 | Filtered grey water with pathogens killed, ready for a final polish. | Disinfection batch logged. Residual chlorine within limits, rev 2. |
| san-016 | Dishwater heavy with fat, skimmed before it settles in the pipes. | Grease in drain lines is traced to source. Source is billed for rodding. |
| san-017 | Water flushed back through a sand filter, settled again to recover it. | What the filter caught, returned. Settle and try again. |
| san-018 | Salty reject water left by reverse osmosis, evaporated down to salt cake. | Too salty to keep, too valuable to vent. Venting brine is prohibited, Ref 1801/B. |
| san-019 | Solids settled out of grey water, pressed or grown into fresh sludge culture. | Bottom of the barrel. Collected anyway. |
| san-020 | A living sludge culture that consumes the dirt in grey water. | LIVE CULTURE. DO NOT CHLORINATE. DO NOT STARVE. |
| san-021 | Disinfected water for mopping a cabin floor; it drains back as grey water. | Floor washdown on schedule C. Schedule C posted beside schedule B, which is void. |
| san-022 | Fat skimmed from greasy water, rendered soon before it sets into a fatberg. | Left a week, it sets. Left a month, it requires a work order. |
| san-023 | A hardened mass of grease and waste, broken up with lye in the sludge press. | Every ship has one. Naming it is discouraged by memo. |
| san-024 | Clean rendered fat, burned for heat or boiled into soap. | Last cycle's frying oil. Next cycle's soap. Same tin, relabelled. |
| san-025 | Urine dosed with acid or pretreat so it stays stable for ammonia stripping. | Pretreated. The urine, not the operator. |
| san-026 | Pressed solids from septic water and tank slurry, limed to make them safe. | Classified as cake for inventory purposes only. |
| san-027 | Heat-treated urine, safe to dilute for the farm or to strip and crystallise. | Farm-grade nitrogen. The farm has not been told where from. |
| san-028 | The liquor left after urea crystallises, dried down to salt cake. | What the crystals rejected. Dry it down, Proc 28. |
| san-029 | Mixed salts dried from brine, leached for potash. | SALT CAKE. NOT TABLE SALT. NOT FOR GALLEY USE. |
| san-030 | Water carrying stripped ammonia, absorbed into acid or distilled off. | Open valve slowly. Eye wash station is at the other end of the module. |
| san-031 | Ammonia captured in acid as crystals, granulated into nitrogen fertilizer. | Batch assay attached. Nitrogen content nominal, sulphur content also nominal. |
| san-032 | Food scraps mashed to pulp; the base of compost, digester feed and insect feed. | Pulped scraps are allocated by Sanitation. Compost, digester or insects, in that order. |
| san-033 | Scraps and slurry mixed for the digester; it rots fast if left. | Stir. Do not inhale while stirring. |
| san-034 | Food scraps dried hard so they keep, ground into feed. | Dried scraps keep. Wet scraps generate paperwork. |
| san-035 | Food scraps heat-treated safe for feeding insects. | Insect stock has filed no complaints. Insect stock is the model workforce. |
| san-036 | Liquid pressed out of food scraps, used as digester feed; it rots quickly. | Collect in a sealed jug. Open jugs are a sanitation finding. |
| san-037 | A lidded bin that holds food scraps until the composter can take them. | LID DOWN. ALWAYS LID DOWN. |
| san-038 | A scrap caddy full of scraps, emptied into the composter before it fouls. | Full means now. Shift end is not now. |
| san-039 | A scrap caddy left full too long, scrubbed clean before reuse. | Someone forgot. The rota shows who. The rota is not consulted. |
| san-040 | Mixed scraps, waste and bulking material piled ready for hot composting. | Greens, browns, and contents not itemised. Itemisation not required, Memo 40/C. |
| san-041 | A compost pile working hot, cured into compost, kept back as starter or bagged for warmth. | CORE TEMPERATURE HIGH. DO NOT SIT ON PILE. |
| san-042 | Live compost kept back to start new piles faster; it dies if left too long. | Keep a portion back. A cold start costs a week. A week costs the station. |
| san-043 | Human waste composted long and slow until safe for growing beds. | Cured to pathogen standard 5. Standard 5 is the one with the long wait. |
| san-044 | Dry faeces heat-treated safe, burned for heat or pressed into pellets. | Fuel grade D. Fuel is fuel. Do not overthink it. |
| san-045 | Compost pressed into a dense brick that stores and transfers easily; it is soaked before use. | Fits the door slot. Most useful things are measured by that. |
| san-046 | Slurry prepared for the digester; it rots if it waits. | Feed within the shift. Digester uptime is monitored remotely. |
| san-047 | A live microbe culture that starts and speeds digestion. | Keep a jar back. A cold digester takes a week to resume. Ref 4700/D. |
| san-048 | The scum layer floating in the digester, skimmed into grease and sludge. | Skim at low agitation. High agitation remixes the problem. |
| san-049 | Sand and grit settled in the digester, washed back into mineral grit. | Grit in the digester traced to regolith in the diet. Diet unchanged. |
| san-050 | The fibrous fraction of digestate, piled with compost. | Good for the pile. Ruinous for footwear. Footwear is not reissued. |
| san-051 | Biogas with its sulphur removed; it burns cleaner, and is bottled or upgraded. | Sulphur under limit, rev 5. Smell remains. Smell is not measured. |
| san-052 | Biogas upgraded to near-pure methane for the ship's gas lines. | Graded to line standard. Credited to the station at the line rate, less handling. |
| san-053 | Water condensed out of biogas, returned to the grey water reclaimer. | Drain condensate trap daily. A full trap stops the line. |
| san-054 | Iron-packed media that removes sulphur from biogas. | Iron oxide media, Type 2. Regenerate when spent. Do not discard. |
| san-055 | Scrubber media saturated with sulphur, regenerated with oxygen. | MAY SELF HEAT ON EXPOSURE TO AIR. STORE SEALED. |
| san-056 | A canister of scrubbed biogas, burned or used to fill heater cartridges. | FLAMMABLE. KEEP UPRIGHT. KEEP AWAY FROM IGNITION SOURCES. |
| san-057 | A small biogas cartridge that warms a cabin at a cost in carbon dioxide; it leaves an empty canister. | Warm hands or clean air. The Company provides the choice. |
| san-058 | Dewatered sludge pressed into cake, then limed, sterilised or dried. | Cake moisture under limit. Press cloth inspected. Cloth has opinions. Tag 5803. |
| san-059 | Water pressed out of sludge and digestate, returned to the reclaimer before it stales. | Back to stage 1. Everything aboard returns to stage 1. |
| san-060 | Sludge dried hard, treated into biosolids or charred. | Dry enough to stack. Do not stack near intakes. |
| san-061 | A pellet of treated biosolids, burned for heat or used as slow-release fertilizer. | Small enough to forget its origin. Records do not forget. |
| san-062 | Sludge mixed with lime to kill what lives in it, sterilised next. | CAUSTIC. GLOVES AND GOGGLES. LIME BURNS ARE NOT COVERED. |
| san-063 | Sludge sterilised by heat, dried on into biosolids. | Sterility confirmed by sample. Sample confirmed by nobody. |
| san-064 | Sludge charred into porous carbon, charged for soil or pressed into odour blocks. | Carbon content high. Value assigned on Form 64C. |
| san-065 | Ash from the waste incinerator, sifted for phosphate or leached for lye. | Sift before disposal. Phosphate does not grow on the ship's account. |
| san-066 | Phosphate-rich ash, acidulated or ground into fertilizer. | Phosphorus is finite aboard. Every gram is tracked. Ref 6600/P. |
| san-067 | Glassy lumps left in the waste incinerator, crushed for salvage. | Hard, ugly, recoverable. Logged for salvage regardless of appearance. |
| san-068 | Water from the incinerator's flue scrubber, settled with lime. | ACIDIC. DO NOT ROUTE TO GREY WATER WITHOUT SETTLING. |
| san-069 | A sealed bag of used dressings and gloves bound for the incinerator. | CLINICAL WASTE. DO NOT OPEN. DO NOT REUSE. INCINERATE ONLY. |
| san-070 | A charcoal block that keeps a treatment cabin's air fresher while it lasts. | Issued to sanitation stations. Other stations may requisition one on Form 70A. |
| san-071 | An odour block saturated in use, baked to be used again. | Saturated. Bake to restore. Do not bake in the galley oven. |
| san-072 | Compost-based filter media that cleans the air of a working cabin. | Live media. Keep moist. Dry media is reported as station negligence. |
| san-073 | Exhausted biofilter media, piled back into compost. | Retired to the compost pile. Service record closed. |
| san-074 | A trap that catches grease from drains and keeps the cabin cleaner; it fills into grease skim. | Saves the pipes. Costs one unpleasant task. Task assigned to the station. |
| san-075 | Slop left to moulder, digested or burned before it fouls the cabin. | Found behind the press. Not entered in any log. Burned with the log. |
| san-076 | A bag of hot compost that warms a cabin as it cools, leaving hot compost. | Heat recovered from waste is credited to the Company energy account. |
| san-077 | A replacement filter membrane fitted to the grey water reclaimer. | Membrane fouled at 60 percent. Swapped. Inspector's initials illegible. |
| san-078 | A replacement pump seal fitted to the grey water reclaimer; it wears into plastic scrap. | Small ring. Large puddle on failure. Puddles are billed by area. |
| san-079 | Ceramic packing for the urine nutrient extractor's ammonia stripper. | Ceramic saddles, size 25 mm. Breakage in transit is normal and charged anyway. |
| san-080 | A replacement heater fitted to the urine nutrient extractor's crystallizer; it wears into broken parts. | No heat, no crystals. Element tested, rev 4. Element now warm. Also tested. |
| san-081 | A replacement mixer blade fitted to the anaerobic digester; it wears into metal scrap. | Blade pitted at tips. Mixing nominal. Smell nominal. Tag 8101. |
| san-082 | A replacement gas valve fitted to the anaerobic digester; it wears into broken parts. | PRESSURE RELIEF. DO NOT OBSTRUCT. DO NOT STAND IN LINE OF VENT. |
| san-083 | A replacement auger fitted to the composter to turn the pile; it wears into metal scrap. | Turns the pile. Replaces an operator with a fork. The fork is still issued. |
| san-084 | A replacement aerator fan fitted to the composter; it wears into broken parts. | Aerobic composting requires air. Air is metered. Ref 8400/A. |
| san-085 | A replacement filter cloth fitted to the sludge press; it wears into fabric scraps. | Woven tight. Washing between batches is not provisioned. |
| san-086 | A replacement steel platen fitted to the sludge press; it wears into metal scrap. | Flat steel, ground true. Dropped once, no longer true. Tag 8606. |
| san-087 | A replacement pellet die fitted to the biosolids pelletizer; it wears into metal scrap. | Bore 6 mm. Worn dies make larger pellets. Larger pellets are not better pellets. |
| san-088 | A replacement press roller fitted to the biosolids pelletizer; it wears into metal scrap. | KEEP HANDS CLEAR OF ROLLER NIP. |
| san-089 | A replacement nozzle fitted to the biogas burner; it wears into metal scrap. | Clean weekly. A sooted nozzle burns yellow. Yellow is reported. |
| san-090 | A replacement spark igniter fitted to the biogas burner; it wears into electronic scrap. | Three clicks then light. Four clicks, purge before retrying. Proc 90. |
| san-091 | A replacement cast grate fitted to the waste incinerator; it wears into metal scrap. | Grate warped, still seated, rev 12. Replace when it drops through. |
| san-092 | Replacement refractory brick for the waste incinerator's lining; it wears into ceramic shards. | Holds the fire in. Holds nothing else in. |
| san-093 | A crated kit that installs a grey water reclaimer. | Water self-sufficiency does not alter the station's water allocation. |
| san-094 | A crated kit that installs a urine nutrient extractor. | Gloves are not included. Gloves are strongly advised. Procurement noted the contradiction. |
| san-095 | A crated kit that installs an anaerobic digester. | Microbes not included. Microbes ship separately, live, on Form 95M. |
| san-096 | A crated kit that installs a composter. | Compost output becomes Company growing stock on completion. |
| san-097 | A crated kit that installs a sludge press. | CRATE HEAVY. PLATEN INSIDE. TWO OPERATORS REQUIRED. ONE PROVIDED. |
| san-098 | A crated kit that installs a biosolids pelletizer. | Commissioning test: one batch of pellets. Pellets are to be kept as evidence. |
| san-099 | A crated kit that installs a biogas burner. | Open flame in a sealed hull. Approved under Exemption 12, pending review. |
| san-100 | A crated kit that installs a waste incinerator. | For waste that has failed every other process. Installation is likewise a last resort. |
