# Cleaning & Laundry — `cln`

A clean cabin: dishes, cookware and cutlery washed back for the galley and the table; dirty laundry washed, dried and
pressed into `cln-004` Clean Laundry Bundle, which the makers of garments, bedding and towels take back as raw; the
detergents and cleaners those take and that raise `cabin.clean`; mops, brushes, sponges, rags and the hand vacuum, the
tools the crew member's own cleaning needs and wears out in use (ECO-11); and the cleaning bots, built in the bot bay and
kept in the dock, that run themselves and hold `cabin.clean` up by the hour. Left too long, dirty things turn worse:
crusted dishes, mildewed laundry. Washing leaves `san-001` Grey Water; worn tools go to `scr`.

## Devices

| id | device | role | cells |
|---|---|---|---|
| cln.dishwasher | JN100 Dishwasher | sanit | 2x1 |
| cln.washer | JN210 Washing Machine | sanit | 1x1 |
| cln.dryer | JN220 Tumble Dryer | sanit | 1x1 |
| cln.press | JN230 Linen Press | sanit | 2x1 |
| cln.mixer | JN300 Detergent Mixer | sanit | 2x1 |
| cln.botbay | JN500 Cleaning Bot Bay | sanit | 2x2 |
| cln.botdock | JN510 Bot Dock | sanit | 1x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| cln-001 | Dish, Dirty | — | 48 h → cln-013 |
| cln-002 | Dish, Clean | — | — |
| cln-003 | Laundry, Dirty | — | 240 h → cln-014 |
| cln-004 | Laundry, Clean, Bundled | — | — |
| cln-005 | Soap, Dish | — | — |
| cln-006 | Detergent, Laundry | — | — |
| cln-007 | Cleaner, Floor | cabin.clean +10, leaves 1 san-001 | — |
| cln-008 | Disinfectant | cabin.clean +12, leaves 1 san-001 | — |
| cln-009 | Mop | — | 200 h → cln-042 |
| cln-010 | Bot, Cleaning | cabin.clean +3/h | 1500 h → cln-072 |
| cln-011 | Laundry, Wet | — | 24 h → cln-014 |
| cln-012 | Sweepings, Floor | — | — |
| cln-013 | Dish, Crusted | — | — |
| cln-014 | Laundry, Mildewed | — | — |
| cln-015 | Cookpot, Dirty | — | 48 h → cln-016 |
| cln-016 | Cookpot, Crusted | — | — |
| cln-017 | Cookpot, Clean | — | — |
| cln-018 | Mug, Dirty | — | — |
| cln-019 | Mug, Clean | — | — |
| cln-020 | Lint, Dryer | — | — |
| cln-021 | Laundry, Dry | — | — |
| cln-022 | Soda, Washing | — | — |
| cln-023 | Concentrate, Enzyme | — | — |
| cln-024 | Solution, Bleach | — | 720 h |
| cln-025 | Rinse Aid, Dishwasher | — | — |
| cln-026 | Softener, Fabric | — | — |
| cln-027 | Remover, Stain | — | — |
| cln-028 | Pods, Laundry | — | — |
| cln-029 | Tablet, Dishwasher | — | — |
| cln-030 | Powder, Scouring | cabin.clean +8, leaves 1 san-001 | — |
| cln-031 | Cleaner, Glass | cabin.clean +5 | — |
| cln-032 | Spray, Surface | cabin.clean +8 | — |
| cln-033 | Descaler | cabin.clean +6, leaves 1 san-001 | — |
| cln-034 | Degreaser | cabin.clean +8, leaves 1 san-001 | — |
| cln-035 | Cleaner, Drain | cabin.clean +6, leaves 1 san-001 | — |
| cln-036 | Cleaner, Toilet Bowl | cabin.clean +8, leaves 1 san-001 | — |
| cln-037 | Remover, Mould | cabin.clean +10 | — |
| cln-038 | Wipes, Disinfecting | cabin.clean +6, leaves 1 hyg-011 | — |
| cln-039 | Cleaner, Vinegar | cabin.clean +6 | — |
| cln-040 | Neutralizer, Odour | cabin.clean +5 | — |
| cln-041 | Head, Mop | — | — |
| cln-042 | Head, Mop, Worn | — | — |
| cln-043 | Bucket, Mop | — | 1000 h → scr-002 |
| cln-044 | Brush, Scrub | — | 300 h → scr-002 |
| cln-045 | Brush, Toilet | — | 300 h → scr-002 |
| cln-046 | Sponge, Cleaning | — | 40 h → cln-047 |
| cln-047 | Sponge, Cleaning, Worn | — | — |
| cln-048 | Pad, Scouring | — | 40 h → scr-002 |
| cln-049 | Cloth, Cleaning | — | 60 h → cln-003 |
| cln-050 | Rag, Cleaning | — | 40 h → cln-073 |
| cln-051 | Squeegee | — | 500 h → scr-002 |
| cln-052 | Set, Dustpan and Brush | — | 500 h → scr-002 |
| cln-053 | Vacuum, Hand | — | 400 h → scr-003 |
| cln-054 | Bot, Mopping | cabin.clean +4/h | 1500 h → scr-004 |
| cln-055 | Bot, Dust Sweeper | cabin.clean +2/h | 1200 h → scr-004 |
| cln-056 | Bot, Window Cleaning | cabin.clean +2/h, cabin.light +1/h | 1200 h → scr-004 |
| cln-057 | Bot, Duct Cleaner | cabin.clean +2/h, cabin.co2 -1/h | 1200 h → scr-004 |
| cln-058 | Bot, Waste Collector | cabin.clean +3/h | 1200 h → scr-004 |
| cln-059 | Bot, Cleaning, Mk II | cabin.clean +6/h | 2000 h → scr-004 |
| cln-060 | Chassis, Cleaning Bot | — | — |
| cln-061 | Roller, Brush, Bot | — | — |
| cln-062 | Brush, Side, Bot | — | — |
| cln-063 | Module, Vacuum, Bot | — | — |
| cln-064 | Module, Mop, Bot | — | — |
| cln-065 | Pad, Mop, Bot | — | — |
| cln-066 | Bin, Dust, Bot | — | — |
| cln-067 | Battery, Cleaning Bot | — | — |
| cln-068 | Controller, Cleaning Bot | — | — |
| cln-069 | Ring, Bumper, Bot | — | — |
| cln-070 | Wheel, Drive, Bot | — | — |
| cln-071 | Arm, Squeegee, Bot | — | — |
| cln-072 | Bot, Cleaning, Worn | — | — |
| cln-073 | Rags, Soiled | — | — |
| cln-074 | Cutlery, Dirty | — | — |
| cln-075 | Cutlery, Clean | — | — |
| cln-076 | Salt, Dishwasher | — | — |
| cln-077 | Sanitizer, Laundry | — | — |
| cln-078 | Pack, Deep Clean | cabin.clean +25, leaves 1 san-001 | — |
| cln-079 | Sachet, Air Freshener | cabin.clean +1/h | 336 h |
| cln-080 | Spray Arm, Dishwasher | fits cln.dishwasher, leaves 1 scr-001 | — |
| cln-081 | Pump, Dishwasher | fits cln.dishwasher, leaves 1 scr-004 | — |
| cln-082 | Drum Bearing, Washing Machine | fits cln.washer, leaves 1 scr-004 | — |
| cln-083 | Door Seal, Washing Machine | fits cln.washer, leaves 1 scr-002 | — |
| cln-084 | Heating Element, Tumble Dryer | fits cln.dryer, leaves 1 scr-004 | — |
| cln-085 | Lint Screen, Tumble Dryer | fits cln.dryer, leaves 1 scr-001 | — |
| cln-086 | Plate, Linen Press | fits cln.press, leaves 1 scr-001 | — |
| cln-087 | Pad, Linen Press | fits cln.press, leaves 1 scr-005 | — |
| cln-088 | Paddle, Detergent Mixer | fits cln.mixer, leaves 1 scr-001 | — |
| cln-089 | Dosing Valve, Detergent Mixer | fits cln.mixer, leaves 1 scr-004 | — |
| cln-090 | Jig, Cleaning Bot Bay | fits cln.botbay, leaves 1 scr-001 | — |
| cln-091 | Gripper, Cleaning Bot Bay | fits cln.botbay, leaves 1 scr-004 | — |
| cln-092 | Charge Contacts, Bot Dock | fits cln.botdock, leaves 1 scr-003 | — |
| cln-093 | Evacuation Fan, Bot Dock | fits cln.botdock, leaves 1 scr-004 | — |
| cln-094 | Kit, Dishwasher | installs cln.dishwasher | — |
| cln-095 | Kit, Washing Machine | installs cln.washer | — |
| cln-096 | Kit, Tumble Dryer | installs cln.dryer | — |
| cln-097 | Kit, Linen Press | installs cln.press | — |
| cln-098 | Kit, Detergent Mixer | installs cln.mixer | — |
| cln-099 | Kit, Cleaning Bot Bay | installs cln.botbay | — |
| cln-100 | Kit, Bot Dock | installs cln.botdock | — |

## Ways

| way | by | min | needs | takes | makes | gives |
|---|---|---|---|---|---|---|
| wash dishes by hand | any.washbasin | 15 | 1 cln-046 | 3 cln-001, 1 wat-001, 1 cln-005 | 3 cln-002, 1 san-016 | — |
| rinse dishes without soap | any.washbasin | 15 | — | 2 cln-001, 1 wat-001 | 2 cln-002, 1 san-001 | — |
| run the dishwasher | cln.dishwasher | 60 | — | 6 cln-001, 1 cln-029, 2 wat-001, 1 pwr-001 | 6 cln-002, 2 san-016 | — |
| run the dishwasher with rinse aid | cln.dishwasher | 60 | — | 6 cln-001, 1 cln-005, 1 cln-025, 2 wat-001, 1 pwr-001 | 6 cln-002, 2 san-016 | — |
| run the dishwasher on treated water | cln.dishwasher | 60 | — | 6 cln-001, 1 cln-029, 2 san-004, 1 pwr-001 | 6 cln-002, 2 san-016 | — |
| soak crusted dishes | cln.dishwasher | 90 | — | 4 cln-013, 1 cln-034, 2 wat-001, 1 pwr-001 | 4 cln-002, 2 san-016 | — |
| scrub a crusted dish by hand | any.washbasin | 20 | 1 cln-048 | 2 cln-013, 1 cln-030, 1 wat-001 | 2 cln-002, 1 san-016 | — |
| wash cookpots | cln.dishwasher | 60 | — | 3 cln-015, 1 cln-029, 2 wat-001, 1 pwr-001 | 3 cln-017, 2 san-016 | — |
| scour a crusted cookpot | any.washbasin | 30 | 1 cln-048 | 1 cln-016, 1 cln-030, 1 wat-001 | 1 cln-017, 1 san-016 | — |
| wash mugs and cutlery | cln.dishwasher | 45 | — | 4 cln-018, 4 cln-074, 1 cln-029, 2 wat-001, 1 pwr-001 | 4 cln-019, 4 cln-075, 1 san-016 | — |
| rinse a mug | any.washbasin | 5 | — | 1 cln-018, 1 wat-001 | 1 cln-019, 1 san-001 | — |
| wash cutlery by hand | any.washbasin | 10 | 1 cln-046 | 4 cln-074, 1 wat-001, 1 cln-005 | 4 cln-075, 1 san-016 | — |
| regenerate the dishwasher softener | cln.dishwasher | 30 | — | 1 cln-076, 2 wat-002 | 2 wat-027 | — |
| boil water in a cookpot | any.bench | 20 | — | 1 cln-017, 2 wat-002, 1 pwr-001 | 2 wat-001, 1 cln-015 | — |
| drink hot water from a mug | any.table | 10 | — | 1 cln-019, 1 wat-006 | 1 cln-018 | hydration +15, bladder +12, stress -3 |
| eat stew with cutlery | any.table | 20 | — | 1 mel-003, 1 cln-002, 1 cln-075 | 1 cln-001, 1 cln-074, 1 san-002 | satiety +35, bowel +10, stress -2 |
| shape clean dishes | any.bench | 30 | — | 1 cer-031 | 2 cln-002 | — |
| mould clean dishes | any.bench | 20 | — | 1 pol-015 | 2 cln-002 | — |
| press a cookpot | any.bench | 60 | — | 1 met-034 | 1 cln-017 | — |
| shape mugs | any.bench | 20 | — | 1 cer-031 | 2 cln-019 | — |
| stamp cutlery | any.bench | 30 | — | 1 met-034 | 4 cln-075 | — |
| wash laundry by hand | any.washbasin | 45 | — | 3 cln-003, 2 wat-001, 1 hyg-001 | 3 cln-011, 2 san-001 | — |
| machine wash laundry | cln.washer | 60 | — | 6 cln-003, 1 cln-006, 3 wat-001, 1 pwr-001 | 6 cln-011, 3 san-001 | — |
| machine wash with pods | cln.washer | 60 | — | 6 cln-003, 1 cln-028, 3 wat-001, 1 pwr-001 | 6 cln-011, 3 san-001 | — |
| machine wash on treated water | cln.washer | 60 | — | 6 cln-003, 1 cln-006, 3 san-004, 1 pwr-001 | 6 cln-011, 3 san-001 | — |
| treat stains and wash | cln.washer | 60 | — | 4 cln-003, 1 cln-027, 1 cln-006, 2 wat-001, 1 pwr-001 | 4 cln-011, 2 san-001 | — |
| bleach whites | cln.washer | 60 | — | 4 cln-003, 1 cln-024, 2 wat-001, 1 pwr-001 | 4 cln-011, 2 san-001 | — |
| rewash mildewed laundry | cln.washer | 90 | — | 4 cln-014, 1 cln-077, 1 cln-006, 3 wat-001, 1 pwr-001 | 4 cln-011, 3 san-001 | — |
| wash soiled rags | cln.washer | 45 | — | 4 cln-073, 1 cln-006, 2 wat-001, 1 pwr-001 | 4 cln-050, 2 san-001 | — |
| tumble dry laundry | cln.dryer | 60 | — | 6 cln-011, 2 pwr-001 | 6 cln-021, 1 cln-020 | — |
| hang laundry to dry | crew | 20 | — | 3 cln-011 | 3 cln-021 | — |
| press laundry | cln.press | 30 | — | 6 cln-021, 1 pwr-001 | 2 cln-004 | — |
| fold laundry by hand | crew | 20 | — | 3 cln-021 | 1 cln-004 | — |
| bake washing soda | cln.mixer | 60 | — | 2 chm-012, 1 pwr-001 | 2 cln-022 | — |
| brew enzyme concentrate | cln.mixer | 120 | — | 2 san-032, 1 bio-009, 1 pwr-001 | 2 cln-023 | — |
| mix bleach solution | cln.mixer | 30 | — | 1 chm-037, 2 wat-001 | 3 cln-024 | — |
| mix peroxide bleach | cln.mixer | 30 | — | 1 chm-007, 2 wat-001 | 3 cln-024 | — |
| mix rinse aid | cln.mixer | 30 | — | 1 chm-065, 1 chm-061, 1 wat-001 | 3 cln-025 | — |
| mix fabric softener | cln.mixer | 30 | — | 1 chm-061, 1 hyg-019, 1 hyg-018 | 3 cln-026 | — |
| use vinegar as softener | any.bench | 10 | — | 1 ing-009 | 1 cln-026 | — |
| mix stain remover | cln.mixer | 30 | — | 1 cln-023, 1 chm-007, 1 pwr-001 | 3 cln-027 | — |
| mix laundry detergent | cln.mixer | 60 | — | 1 chm-061, 1 cln-022, 1 cln-023, 1 pwr-001 | 4 cln-006 | — |
| grate soap into detergent | any.bench | 30 | — | 1 hyg-001, 1 cln-022 | 2 cln-006 | — |
| wrap laundry pods | cln.mixer | 45 | — | 2 cln-006, 1 cln-026, 1 pol-002 | 4 cln-028 | — |
| mix laundry sanitizer | cln.mixer | 30 | — | 1 chm-007, 1 chm-029, 1 wat-001 | 3 cln-077 | — |
| mix dish soap | cln.mixer | 30 | — | 1 chm-061, 1 hyg-019, 1 wat-001 | 4 cln-005 | — |
| dissolve soap into dish soap | any.bench | 20 | — | 1 hyg-001, 1 wat-001 | 1 cln-005 | — |
| press dishwasher tablets | cln.mixer | 45 | — | 1 cln-022, 1 cln-023, 1 chm-065 | 6 cln-029 | — |
| grade dishwasher salt | cln.mixer | 20 | — | 1 ore-025 | 3 cln-076 | — |
| mix floor cleaner | cln.mixer | 30 | — | 1 chm-061, 1 hyg-018, 2 wat-001 | 4 cln-007 | — |
| dissolve soap into floor cleaner | any.bench | 10 | — | 1 hyg-001, 1 wat-001 | 1 cln-007 | — |
| mix disinfectant | cln.mixer | 30 | — | 1 chm-037, 1 chm-061, 2 wat-001 | 4 cln-008 | — |
| dilute alcohol disinfectant | any.bench | 10 | — | 1 chm-034, 1 wat-001 | 2 cln-008 | — |
| mix scouring powder | cln.mixer | 30 | — | 1 ore-052, 1 cln-022 | 3 cln-030 | — |
| mix scouring powder from reclaimed grit | cln.mixer | 30 | — | 1 scr-054, 1 cln-022 | 3 cln-030 | — |
| mix glass cleaner | cln.mixer | 20 | — | 1 chm-034, 2 wat-001 | 4 cln-031 | — |
| mix surface spray | cln.mixer | 20 | — | 1 cln-008, 1 cln-007 | 3 cln-032 | — |
| mix descaler | cln.mixer | 20 | — | 1 chm-065, 2 wat-001 | 3 cln-033 | — |
| dilute descaler solution | cln.mixer | 20 | — | 1 chm-053, 1 wat-001 | 3 cln-033 | — |
| mix degreaser | cln.mixer | 30 | — | 1 chm-054, 1 chm-061, 1 wat-001 | 4 cln-034 | — |
| mix enzyme degreaser | cln.mixer | 30 | — | 1 cln-022, 1 cln-023 | 2 cln-034 | — |
| mix drain cleaner | cln.mixer | 20 | — | 1 chm-002, 1 wat-001 | 3 cln-035 | — |
| mix enzyme drain cleaner | cln.mixer | 20 | — | 1 cln-023, 1 wat-001 | 2 cln-035 | — |
| mix toilet bowl cleaner | cln.mixer | 20 | — | 1 chm-009, 1 chm-061 | 4 cln-036 | — |
| mix citric toilet cleaner | cln.mixer | 20 | — | 1 chm-065, 1 cln-022 | 3 cln-036 | — |
| mix mould remover | cln.mixer | 20 | — | 1 cln-024, 1 chm-061 | 3 cln-037 | — |
| pack disinfecting wipes | cln.mixer | 30 | — | 3 hyg-027, 1 cln-008, 1 pol-002 | 6 cln-038 | — |
| mix vinegar cleaner | any.bench | 10 | — | 1 ing-009, 1 wat-001 | 2 cln-039 | — |
| dilute acetic cleaner | cln.mixer | 20 | — | 1 chm-029, 2 wat-001 | 4 cln-039 | — |
| mix odour neutralizer | cln.mixer | 30 | — | 1 chm-012, 1 hyg-018, 1 wat-001 | 3 cln-040 | — |
| pack a deep clean pack | cln.mixer | 30 | — | 1 cln-007, 1 cln-008, 1 cln-030, 1 cln-031 | 1 cln-078 | — |
| fill air freshener sachets | cln.mixer | 20 | — | 1 fil-021, 1 hyg-018, 1 fib-064 | 2 cln-079 | — |
| mop the floor | crew | 20 | 1 cln-009, 1 cln-043 | 1 cln-007, 1 wat-001 | 1 san-001 | cabin.clean +15 |
| mop with disinfectant | crew | 25 | 1 cln-009, 1 cln-043 | 1 cln-008, 1 wat-001 | 1 san-001 | cabin.clean +18, immunity +1 |
| scrub the floor | crew | 30 | 1 cln-044, 1 cln-043 | 1 cln-030, 1 wat-001 | 1 san-001 | cabin.clean +14 |
| wipe down with vinegar | crew | 15 | 1 cln-049 | 1 cln-039, 1 wat-001 | 1 san-001 | cabin.clean +8 |
| wipe down with a rag | crew | 15 | 1 cln-050 | 1 cln-039, 1 wat-001 | 1 san-001 | cabin.clean +6 |
| squeegee the walls and window | crew | 15 | 1 cln-051 | 1 cln-031 | — | cabin.clean +6, cabin.light +1 |
| sweep the floor | crew | 15 | 1 cln-052 | — | 1 cln-012 | cabin.clean +5 |
| vacuum the cabin | crew | 20 | 1 cln-053 | 1 pwr-001 | 1 cln-012 | cabin.clean +10 |
| scrub the toilet | any.toilet | 15 | 1 cln-045 | 1 cln-036, 1 wat-001 | 1 san-001 | cabin.clean +10 |
| descale the basin | any.washbasin | 20 | 1 cln-046 | 1 cln-033, 1 wat-001 | 1 san-001 | cabin.clean +8 |
| empty the bot dust bins | cln.botdock | 10 | — | 1 pwr-001 | 1 cln-012 | cabin.clean +3 |
| run the bots a shift | cln.botdock | 120 | — | 2 pwr-001 | 1 cln-012 | cabin.clean +6 |
| refurbish a worn cleaning bot | cln.botdock | 90 | — | 1 cln-072, 1 cln-061, 1 cln-067, 1 pwr-001 | 1 cln-010, 1 scr-004 | — |
| strip a worn cleaning bot | cln.botbay | 60 | — | 1 cln-072 | 1 cln-060, 1 scr-003, 1 scr-004 | — |
| mould a bot chassis | cln.botbay | 60 | — | 1 pol-045, 1 met-007 | 1 cln-060 | — |
| build bot brush rollers | cln.botbay | 30 | — | 1 fib-003, 1 pol-015, 1 mec-006 | 2 cln-061 | — |
| tuft bot side brushes | cln.botbay | 20 | — | 1 fib-003, 1 pol-015 | 3 cln-062 | — |
| build a bot vacuum module | cln.botbay | 60 | — | 1 mec-009, 1 cln-066, 1 fil-037 | 1 cln-063 | — |
| build a bot mop module | cln.botbay | 60 | — | 1 mec-039, 1 cln-065, 1 pol-008 | 1 cln-064 | — |
| cut bot mop pads | cln.botbay | 20 | — | 1 fib-068 | 4 cln-065 | — |
| mould bot dust bins | cln.botbay | 20 | — | 1 pol-015 | 2 cln-066 | — |
| mould bot dust bins from recycled sheet | cln.botbay | 20 | — | 1 scr-055 | 2 cln-066 | — |
| pack a cleaning bot battery | cln.botbay | 45 | — | 2 pwr-002, 1 pol-045 | 1 cln-067 | — |
| flash a cleaning bot controller | cln.botbay | 60 | — | 1 ecp-010, 1 ecp-007 | 1 cln-068 | — |
| wire a controller from salvaged chips | cln.botbay | 90 | — | 2 scr-038, 1 scr-037, 1 pwr-001 | 1 cln-068 | — |
| build a bot bumper ring | cln.botbay | 30 | — | 1 pol-003, 1 mec-005 | 1 cln-069 | — |
| build a bot drive wheel | cln.botbay | 30 | — | 1 mec-010, 1 pol-003 | 1 cln-070 | — |
| build a bot squeegee arm | cln.botbay | 30 | — | 1 pol-003, 1 mec-043 | 1 cln-071 | — |
| assemble a cleaning bot | cln.botbay | 120 | — | 1 cln-060, 2 cln-070, 1 cln-061, 1 cln-063, 1 cln-067, 1 cln-068 | 1 cln-010 | — |
| assemble a mopping bot | cln.botbay | 120 | — | 1 cln-060, 2 cln-070, 1 cln-064, 1 cln-067, 1 cln-068 | 1 cln-054 | — |
| assemble a dust sweeper bot | cln.botbay | 120 | — | 1 cln-060, 2 cln-070, 2 cln-062, 1 cln-067, 1 cln-068 | 1 cln-055 | — |
| assemble a window cleaning bot | cln.botbay | 120 | — | 1 cln-060, 1 cln-071, 1 cln-065, 1 cln-067, 1 cln-068 | 1 cln-056 | — |
| assemble a duct cleaner bot | cln.botbay | 120 | — | 1 cln-060, 1 cln-061, 1 cln-063, 1 cln-067, 1 cln-068 | 1 cln-057 | — |
| assemble a waste collector bot | cln.botbay | 120 | — | 1 cln-060, 2 cln-070, 1 cln-066, 1 cln-067, 1 cln-068 | 1 cln-058 | — |
| upgrade to a pro cleaning bot | cln.botbay | 150 | — | 1 cln-010, 1 cln-064, 1 cln-069, 1 cln-067 | 1 cln-059 | — |
| sew a mop head | any.bench | 20 | — | 1 fib-068 | 1 cln-041 | — |
| knot a mop head from rag strips | any.bench | 20 | — | 3 scr-070 | 1 cln-041 | — |
| fit a mop | any.bench | 30 | — | 1 cln-041, 1 met-055 | 1 cln-009 | — |
| rehead a worn mop | any.bench | 10 | — | 1 cln-042, 1 cln-041 | 1 cln-009, 1 scr-005 | — |
| mould a mop bucket | any.bench | 30 | — | 2 pol-015 | 1 cln-043 | — |
| build a mop bucket from recycled plastic | any.bench | 30 | — | 1 scr-055, 1 scr-056 | 1 cln-043 | — |
| tuft a scrub brush | any.bench | 20 | — | 1 pol-015, 1 fib-003 | 1 cln-044 | — |
| tuft a scrub brush on a recycled rod | any.bench | 20 | — | 1 scr-056, 1 fib-003 | 1 cln-044 | — |
| tuft a toilet brush | any.bench | 20 | — | 1 pol-015, 1 fib-003 | 1 cln-045 | — |
| cut sponges | any.bench | 15 | — | 1 pol-012 | 4 cln-046 | — |
| roll scouring pads | any.bench | 15 | — | 1 met-080 | 2 cln-048 | — |
| bond scouring pads from reclaimed grit | any.bench | 15 | — | 1 scr-054, 1 fib-005 | 2 cln-048 | — |
| hem cleaning cloths | any.bench | 20 | — | 1 fib-068 | 3 cln-049 | — |
| cut cleaning rags | any.bench | 15 | — | 2 scr-005 | 2 cln-050 | — |
| build a squeegee | any.bench | 20 | — | 1 pol-003, 1 met-055 | 1 cln-051 | — |
| build a dustpan and brush | any.bench | 20 | — | 1 pol-015, 1 fib-003 | 1 cln-052 | — |
| build a hand vacuum | any.bench | 60 | — | 1 mec-009, 1 cln-067, 1 pol-045 | 1 cln-053 | — |
| build a dishwasher spray arm | any.bench | 30 | — | 1 met-056, 1 mec-049 | 1 cln-080 | — |
| build a dishwasher pump | any.bench | 45 | — | 1 mec-008, 1 pol-009 | 1 cln-081 | — |
| seat a washer drum bearing | any.bench | 30 | — | 1 mec-004, 1 pol-054 | 1 cln-082 | — |
| cut washer door seals | any.bench | 20 | — | 1 pol-003 | 2 cln-083 | — |
| wind a dryer heating element | any.bench | 45 | — | 1 met-047, 1 cer-035 | 1 cln-084 | — |
| cut dryer lint screens | any.bench | 20 | — | 1 met-057 | 2 cln-085 | — |
| build a linen press plate | any.bench | 45 | — | 1 met-007, 1 met-047 | 1 cln-086 | — |
| sew a linen press pad | any.bench | 20 | — | 1 fib-005, 1 fib-008 | 1 cln-087 | — |
| bend a detergent mixer paddle | any.bench | 30 | — | 1 met-049 | 1 cln-088 | — |
| build a detergent dosing valve | any.bench | 30 | — | 1 mec-007, 1 pol-009 | 1 cln-089 | — |
| build a bot bay assembly jig | any.bench | 45 | — | 1 met-005, 1 mec-001 | 1 cln-090 | — |
| build a bot bay gripper | any.bench | 45 | — | 1 mec-043, 1 pol-003 | 1 cln-091 | — |
| cut bot dock charge contacts | any.bench | 30 | — | 1 met-037, 1 mec-005 | 2 cln-092 | — |
| build a bot dock evacuation fan | any.bench | 30 | — | 1 mec-009, 1 fil-037 | 1 cln-093 | — |
| assemble a dishwasher kit | any.bench | 120 | — | 1 fur-001, 1 cln-080, 1 cln-081, 1 met-034 | 1 cln-094 | — |
| assemble a washing machine kit | any.bench | 120 | — | 1 fur-001, 1 cln-082, 1 cln-083, 1 mec-010 | 1 cln-095 | — |
| assemble a tumble dryer kit | any.bench | 120 | — | 1 fur-001, 1 cln-084, 1 cln-085, 1 mec-009 | 1 cln-096 | — |
| assemble a linen press kit | any.bench | 90 | — | 1 fur-001, 1 cln-086, 1 cln-087 | 1 cln-097 | — |
| assemble a detergent mixer kit | any.bench | 120 | — | 1 fur-001, 1 cln-088, 1 cln-089, 1 met-034 | 1 cln-098 | — |
| assemble a cleaning bot bay kit | any.bench | 150 | — | 1 fur-001, 1 cln-090, 1 cln-091, 1 cln-068 | 1 cln-099 | — |
| assemble a bot dock kit | any.bench | 120 | — | 1 fur-001, 1 cln-092, 1 cln-093, 1 pwr-005 | 1 cln-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| cln.dishwasher | Washes dishes, cookpots, mugs and cutlery in bulk, and softens its own water. | Galley throughput depends on this unit. Downtime is charged to the station that caused it. |
| cln.washer | Washes dirty laundry, rags and mildewed loads into wet laundry. | One load per station per day. Overloading voids the drum bearing and the operator's excuse. |
| cln.dryer | Tumbles wet laundry dry and catches lint for carding, composting and litter. | CLEAN LINT SCREEN BEFORE EVERY LOAD. LINT FIRES ARE NOT ACCIDENTS. |
| cln.press | Presses dry laundry into clean bundles, returned as raw stock for bedding, towels and garments. | Creases to Company standard fold 3. Fold 3 is printed on the lid. |
| cln.mixer | Mixes detergents, cleaners, softeners and dishwasher tablets from chemicals and soap. | DO NOT MIX CHLORINE AND AMMONIA. MIXER HAS NO INTERLOCK. NEITHER DO LUNGS. |
| cln.botbay | Builds cleaning bots and their modules, and strips worn bots for parts. | Automated cleaning reduces operator hours. Operator hours are reassigned, not reduced. |
| cln.botdock | Charges and empties the cleaning bots, runs them for a shift and refurbishes worn ones. | Contacts cleaned, fan cleared, rev 7. One bot refused to dock. Logged. |
| cln-001 | A dish after a meal; it crusts over unless washed soon. | Dishes are galley inventory. Unreturned dishes are charged to the last station that held them. |
| cln-002 | A washed dish, ready to serve a meal on. | NO CLEAN DISH, NO HOT MEAL. GALLEY RULE 1. |
| cln-003 | Worn clothes, towels and linen awaiting washing; it mildews if left too long. | All garments end here. Operators too, eventually, in the form of a coverall. |
| cln-004 | Washed, dried and pressed laundry, ready to be made into bedding, towels or garments again. | Bundles are weighed on issue and on return. The difference is the operator's. |
| cln-005 | Liquid soap for washing dishes by hand or with rinse aid. | Cuts grease. Measure by the cap. The cap is the ration. |
| cln-006 | Detergent for the washing machine. | One scoop. Two scoops is a foam incident. Foam incidents require Form 6F. |
| cln-007 | A cleaner for mopping floors that raises cabin cleanliness. | Lemon scent, Type 4. No lemons were involved. |
| cln-008 | A strong disinfectant for surfaces and floors. | Kills most of everything. The remainder is monitored. |
| cln-009 | A floor mop used with a bucket; its head wears out with use. | Every station is issued one. Every station claims it was never issued. |
| cln-010 | A small bot that keeps a cabin floor clean while it runs; it wears out over time. | Naming of Company equipment is prohibited. All bots have names. |
| cln-011 | Laundry fresh from the wash, dried quickly before it mildews. | Hang within the hour. Mildew is faster than the rota. |
| cln-012 | Dust, crumbs and fluff swept up from the floor, sent to the compost pile. | Composition: skin, crumbs, fibre, regolith. Mostly skin. |
| cln-013 | A dish left dirty too long, cleaned by soaking or scouring. | Residue age estimated at three cycles. Responsibility estimated at one station. |
| cln-014 | Laundry left too long and mildewed, cleaned by a sanitising rewash. | BIOLOGICAL GROWTH. DO NOT SHAKE OUT IN CABIN. |
| cln-015 | A cookpot after cooking; it crusts over unless washed soon. | Soak while warm. Cold soaking takes twice the water and twice the time. |
| cln-016 | A cookpot gone hard and crusted, scoured clean. | Crust depth noted. Scouring pad allocation is not increased for neglect. |
| cln-017 | A washed cookpot, ready for the galley. | Galley property. Do not use for chemical mixing. It has been done. |
| cln-018 | A mug after a drink, rinsed for the next one. | Rinse your own. No mug service is provisioned. |
| cln-019 | A clean mug, ready for hot water, tea or coffee. | All mugs are identical by specification. Somebody's is still somebody's. |
| cln-020 | Lint caught by the tumble dryer, carded into fibre, composted or shredded into litter. | FLAMMABLE. EMPTY SCREEN AFTER EACH LOAD. STORE IN LIDDED BIN. |
| cln-021 | Dried laundry, folded or pressed into a clean bundle. | Warm from the drum. The warmest thing most operators handle all cycle. |
| cln-022 | A cleaning soda baked from salts; the base of detergents and scouring powder. | Sodium carbonate, technical grade. Irritant. Cheap. Everywhere. |
| cln-023 | Enzymes brewed from scraps that break down stains and grease. | Live product. Store cool. Cool storage is not provisioned. Use fast. |
| cln-024 | Bleach for whitening laundry and killing mould; it loses strength over time. | Use within date. Expired bleach is still billed as bleach. |
| cln-025 | A rinse additive that helps the dishwasher leave dishes free of spots. | Spot-free dishes are a galley standard. Spotted dishes are a galley finding. |
| cln-026 | A fabric softener for laundry pods. | Classed as non-essential. Issued anyway after the static incidents. Ref 2600/S. |
| cln-027 | A stain treatment for heavily soiled laundry. | Stains on issued garments are recorded at return. Treat before return. |
| cln-028 | Detergent and softener sealed in pre-measured pods. | NOT FOOD. KEEP SEALED. DO NOT BITE. |
| cln-029 | A pressed tablet of detergent for one dishwasher run. | One tablet per run. Half tablets are not a recognised dose. |
| cln-030 | A gritty powder for scouring crusted pots and floors. | Abrasive. Scratches finish. Finish is Company property. Use sparingly. |
| cln-031 | A spray cleaner for windows and walls that keeps a cabin bright. | Clean viewports reduce lamp hours. Lamp hours are billed. |
| cln-032 | A quick all-purpose spray for surfaces. | Spray, wipe, file inspection as passed. |
| cln-033 | An acid cleaner that strips scale from basins and pipes. | ACID. GLOVES REQUIRED. RINSE SURFACES AFTER USE. |
| cln-034 | A strong cleaner for grease, also used to soak crusted dishes. | Galley grease budget is fixed. Degreaser allocation follows it. |
| cln-035 | A caustic cleaner that clears blocked drains. | Pour, wait, listen. No sound after ten minutes means Form 35D. |
| cln-036 | A cleaner for scrubbing the toilet. | Fixture cleaning is a standing duty. It does not rotate. |
| cln-037 | A cleaner that kills mould on walls and seals. | Cabin humidity is within contract. Mould growth is the operator's to remove. |
| cln-038 | Disinfectant wipes for a quick surface clean, leaving a used wipe. | Wipe every handle. Handles are swabbed at random. Proc 38. |
| cln-039 | A mild vinegar cleaner for wipe-downs. | Galley vinegar, diluted. The galley is aware and not pleased. |
| cln-040 | A spray that clears bad odours from a cabin. | Use after sanitation work. Odour complaints cannot be filed across stations. |
| cln-041 | A replacement mop head fitted to a mop. | Heads are exchanged one for one. No worn head, no new head. |
| cln-042 | A mop worn out with use, made usable again with a new head. | Strands remaining: insufficient. Inspector's initials illegible. |
| cln-043 | A mop bucket; a tool that lasts a long time. | Wheel squeak is within tolerance. Tolerance was set by the manufacturer. |
| cln-044 | A stiff brush for scrubbing floors. | Bristle wear indicates effort. Effort is not otherwise recorded. |
| cln-045 | A brush for cleaning the toilet. | FIXTURE USE ONLY. NOT TO BE PASSED THROUGH THE DOOR SLOT. |
| cln-046 | A sponge for dishes and basins; it wears out quickly. | Wring dry after use. A wet sponge is a culture medium. |
| cln-047 | A sponge worn through, shredded for salvage. | Retire before it establishes a colony. Colonies require a report. |
| cln-048 | A steel pad for scouring crusted dishes and pots; it wears out. | Steel wool, grade 2. Gentle on nothing. |
| cln-049 | A cloth for wiping down surfaces; it is laundered after use. | Colour coded by use. All cloths are grey. The code is unenforced. |
| cln-050 | A rag cut from scraps for wipe-downs; it soils with use. | Last cycle's shirt. Reclassified. Form 50R not required for rags. |
| cln-051 | A squeegee for wiping walls and windows clear. | Pull top to bottom. Bottom to top is noted on technique review. |
| cln-052 | A dustpan and brush for sweeping the floor. | No moving parts. Still has a service interval. Tag 0052. |
| cln-053 | A battery hand vacuum that cleans faster than sweeping; it wears into electronic scrap. | Empty after use. Recovered small items are logged as found property. |
| cln-054 | A bot that mops the cabin floor while it runs; it wears into broken parts. | WET FLOOR. BOT OPERATING. DO NOT STEP ON BOT. |
| cln-055 | A bot that sweeps dust from the cabin floor and corners; it wears into broken parts. | Corner coverage 94 percent. The remaining six are the operator's. |
| cln-056 | A bot that cleans windows and walls, keeping the cabin brighter; it wears into broken parts. | Viewport cleaning only. Bot is not authorised to look out. |
| cln-057 | A bot that cleans the air ducts, keeping cabin air slightly fresher; it wears into broken parts. | Operates inside ducts. Retrieval from ducts is an operator task. |
| cln-058 | A bot that gathers loose waste around the cabin; it wears into broken parts. | Collects waste. Does not distinguish waste from belongings. Secure belongings. |
| cln-059 | An upgraded cleaning bot that cleans better than any other bot; it wears into broken parts. | Mk II upgrade raises output. Output targets are raised to match. |
| cln-060 | The empty shell of a cleaning bot, ready for modules. | Chassis serialised at moulding. SN 0060 1104. Lost chassis are deducted. |
| cln-061 | A spinning brush roller for a cleaning bot. | Hair tangles are the leading cause of failure. Hair is not regulated. |
| cln-062 | A side brush that sweeps corners for a dust sweeper bot. | Reaches the corners the rota does not. |
| cln-063 | A vacuum module for a cleaning bot. | Suction tested, nominal, rev 2. Filter fitted backwards on first assembly. Corrected. |
| cln-064 | A mopping module for a cleaning bot. | Water draw per hour is charged to the station running the bot. |
| cln-065 | A cloth pad for a bot's mop or window cleaner. | Swap pads each shift. Pads are not to be wrung by hand into the basin. |
| cln-066 | A bin that holds what a bot collects. | EMPTY BEFORE FULL. A FULL BIN STOPS THE BOT. |
| cln-067 | A battery pack for a cleaning bot or a hand vacuum. | Charge cycles counted. Packs past cycle limit are recalled, not replaced. |
| cln-068 | The control board of a cleaning bot. | Loaded with every station floor plan. Uses one. Firmware Rev 14. |
| cln-069 | A bumper ring that lets a bot strike obstacles without damage. | Bump, turn, retry. The bot has more patience than procurement. |
| cln-070 | A drive wheel for a cleaning bot. | Tracks straight within two degrees. Deck plating does not. |
| cln-071 | A squeegee arm for a window cleaning bot. | Arm reach fixed. Upper viewport corners remain the operator's. |
| cln-072 | A worn-out cleaning bot, refurbished or stripped for parts. | End of service. Strip for parts. Name plate, if any, to be removed. |
| cln-073 | Rags dirtied by cleaning, washed for reuse. | Wash, wring, reissue. Rags have no end of service. |
| cln-074 | Cutlery after a meal, washed for the next one. | Cutlery is counted at each meal. Missing spoons are pursued. |
| cln-075 | Clean cutlery for eating meals. | Stamped COF. Stamped cutlery remains Company property in the mouth. |
| cln-076 | Salt that regenerates the dishwasher's water softener. | DISHWASHER SALT. NOT FOR FOOD. TASTE TESTS ARE NOT REQUIRED. |
| cln-077 | A sanitizer for rewashing mildewed laundry. | Kills mildew. Fades colour. Colour is not a garment specification. |
| cln-078 | A bundle of cleaners for a thorough top-to-bottom cabin clean. | Issued before inspection. Inspection dates are not disclosed. Keep one. |
| cln-079 | A sachet that freshens a cabin's air while it lasts. | Masks odour. Does not remove it. Scrubbers do that, on schedule. |
| cln-080 | A replacement spray arm fitted to the dishwasher; it wears into metal scrap. | Jets blocked, cleared, rev 3. Bits of last cycle's stew recovered. |
| cln-081 | A replacement pump fitted to the dishwasher; it wears into broken parts. | No pump, no wash. No wash, no dishes. No dishes, no meals. Order early. |
| cln-082 | A replacement drum bearing fitted to the washing machine; it wears into broken parts. | Rumble on spin indicates bearing wear. Rumble has been noted for some time. |
| cln-083 | A replacement door seal fitted to the washing machine; it wears into plastic scrap. | A failed seal floods the deck. Floods are billed by the litre. |
| cln-084 | A replacement heating element fitted to the tumble dryer; it wears into broken parts. | Element 2 kW. Grid draw declared on Form 84P. Undeclared draw is trip-tested. |
| cln-085 | A replacement lint screen fitted to the tumble dryer; it wears into metal scrap. | Mesh torn at corner. Lint bypassing. Replace before ignition. Tag 0085. |
| cln-086 | A replacement heated plate fitted to the linen press; it wears into metal scrap. | HOT PLATE. DO NOT PRESS ANYTHING BUT LINEN. |
| cln-087 | A replacement press pad fitted to the linen press; it wears into fabric scraps. | Scorch marks on pad: four. Acceptable count: five. |
| cln-088 | A replacement mixing paddle fitted to the detergent mixer; it wears into metal scrap. | Corrosion at weld. Turning. For now. Inspector's initials smudged. |
| cln-089 | A replacement dosing valve fitted to the detergent mixer; it wears into broken parts. | Dose accuracy plus or minus five percent. The minus is always the operator's batch. |
| cln-090 | A replacement assembly jig fitted to the cleaning bot bay; it wears into metal scrap. | Holds the chassis square during assembly. Squareness checked at rev 5. |
| cln-091 | A replacement gripper fitted to the cleaning bot bay; it wears into broken parts. | PINCH POINT. GRIPPER DOES NOT SENSE FINGERS. |
| cln-092 | Replacement charge contacts fitted to the bot dock; they wear into electronic scrap. | Contacts pitted. Bots dock twice to charge once. Replace. Tag 0092. |
| cln-093 | A replacement fan fitted to the bot dock that empties bot bins into the dock; it wears into broken parts. | Fan noise during evacuation is normal. Fan noise between evacuations is not. |
| cln-094 | A crated kit that installs a dishwasher. | Installation does not change the station's dish allocation. |
| cln-095 | A crated kit that installs a washing machine. | CRATE CONTAINS DRUM. HEAVY. LIFT FROM BASE. |
| cln-096 | A crated kit that installs a tumble dryer. | High-draw unit. Grid load declaration required before first run, Form 96P. |
| cln-097 | A crated kit that installs a linen press. | Pressed linen improves inspection outcomes. Outcomes are not otherwise improved. |
| cln-098 | A crated kit that installs a detergent mixer. | Ships without chemicals. Chemicals are drawn from station stock at standard rate. |
| cln-099 | A crated kit that installs a cleaning bot bay. | Bot production is authorised. Bot naming is not. See Memo 10/B. |
| cln-100 | A crated kit that installs a bot dock. | Dock capacity is fixed. Bots in excess of capacity wait on the floor. |
