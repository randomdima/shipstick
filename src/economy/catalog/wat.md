# Water — `wat`

Every way a capsule has water. Ice is melted, regolith baked, urine and grey water reclaimed, fuel-cell and Sabatier
water caught, the cabin's damp wrung out; the raw water is settled, filtered, distilled, chlorinated or polished into
drinking water, and that is chilled, heated, mineralised, made sparkling and filled into bottles, pouches, jugs and
canteens. Drinking water goes stale back into raw water if it stands too long. Feedwater goes to the electrolyser, the
boilers, the farm and the coolant loops; brine, sludge, scale and tailings go on to chemistry, waste treatment and the
kilns. Also the spare parts and kits of the water works.

## Devices

| id | device | role | cells |
|---|---|---|---|
| wat.extractor | WR800 Regolith Water Extractor | mine | 2x2 |
| wat.melter | WR100 Ice Melter | hydro | 2x1 |
| wat.reclaimer | WR300 Urine Reclaimer | hydro | 2x2 |
| wat.still | WR400 Vapour Still | hydro | 2x2 |
| wat.purifier | WR200 Water Purifier | hydro | 2x1 |
| wat.mineralizer | WR210 Mineralizer | hydro | 1x1 |
| wat.dispenser | WR50 Hot and Cold Dispenser | hydro | 1x1 |
| wat.bottler | WR60 Water Bottler | hydro | 2x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| wat-001 | Water, Drinking | hydration +15, bladder +12, toxin -2 | 240 h → wat-002 |
| wat-002 | Water, Raw | hydration +10, bladder +12, toxin +4 | — |
| wat-003 | Water, Distilled | hydration +15, bladder +12, toxin -3 | — |
| wat-004 | Water, Bottled | hydration +25, bladder +18, toxin -2, leaves 1 pak-004 | — |
| wat-005 | Water, Pouched | hydration +20, bladder +15, toxin -2, leaves 1 pak-002 | — |
| wat-006 | Water, Hot | hydration +15, bladder +12, stress -2 | 2 h → wat-001 |
| wat-007 | Water, Chilled | hydration +15, bladder +12, fun +1 | 4 h → wat-001 |
| wat-008 | Water, Mineral | hydration +16, bladder +12, toxin -2, immunity +1 | 240 h → wat-002 |
| wat-009 | Water, Process | — | — |
| wat-010 | Water, Deionized | — | — |
| wat-011 | Brine, Still | — | — |
| wat-012 | Steam | — | 1 h → wat-031 |
| wat-013 | Ice, Cubed | hydration +5, bladder +4 | 6 h → wat-001 |
| wat-014 | Meltwater | — | 12 h → wat-002 |
| wat-015 | Distillate, Urine | — | — |
| wat-016 | Water, Reclaimed | hydration +14, bladder +12, stress +1 | 240 h → wat-002 |
| wat-017 | Brine, Urine | — | — |
| wat-018 | Water, Fuel Cell | — | — |
| wat-019 | Water, Sabatier | — | — |
| wat-020 | Water, Regolith | hydration +6, bladder +12, toxin +8 | — |
| wat-021 | Frost, Hull | — | 2 h → wat-014 |
| wat-022 | Water, Hard | — | — |
| wat-023 | Water, Brackish | hydration +6, bladder +12, toxin +5 | — |
| wat-024 | Water, Transpiration | — | — |
| wat-025 | Water, Filtered | hydration +12, bladder +12, toxin +1 | 120 h → wat-002 |
| wat-026 | Water, Chlorinated | hydration +14, bladder +12 | — |
| wat-027 | Water, Softened | — | — |
| wat-028 | Water, Ultrapure | — | — |
| wat-029 | Water, Sterile | hydration +15, bladder +12, toxin -3 | — |
| wat-030 | Water, Tablet Treated | hydration +14, bladder +12, toxin -1 | 240 h → wat-002 |
| wat-031 | Condensate, Steam | hydration +14, bladder +12, toxin -2 | 240 h → wat-002 |
| wat-032 | Brine, Still, Concentrated | — | — |
| wat-033 | Residue, Still | — | — |
| wat-034 | Sludge, Sediment | — | — |
| wat-035 | Scale Flakes, Boiler | — | — |
| wat-036 | Water, Backwash | — | 72 h → wat-037 |
| wat-037 | Water, Contaminated | hydration +8, bladder +12, toxin +10 | — |
| wat-038 | Water, Heavy | — | — |
| wat-039 | Tailings, Regolith | — | 720 h → ore-051 |
| wat-040 | Feedwater, Electrolysis | — | — |
| wat-041 | Feedwater, Boiler | — | — |
| wat-042 | Water, Irrigation | — | 168 h → san-006 |
| wat-043 | Feedwater, Coolant | — | — |
| wat-044 | Water, Wash | hygiene +10, leaves 1 san-001 | 72 h → san-001 |
| wat-045 | Water, Wash, Warm | hygiene +15, stress -2, leaves 1 san-001 | 2 h → wat-044 |
| wat-046 | Water, Sparkling | hydration +15, bladder +14, fun +1 | 24 h → wat-001 |
| wat-047 | Water, Alkaline | hydration +15, bladder +12, toxin -3 | — |
| wat-048 | Water, Mineral, Bottled | hydration +25, bladder +18, toxin -2, immunity +1, leaves 1 pak-004 | — |
| wat-049 | Water, Sparkling, Bottled | hydration +25, bladder +20, fun +2, leaves 1 pak-004 | — |
| wat-050 | Water, Distilled, Bottled | hydration +25, bladder +18, toxin -3, leaves 1 pak-004 | — |
| wat-051 | Sachet, Water, Emergency | hydration +10, bladder +8, leaves 1 pak-016 | — |
| wat-052 | Water, Mineral, Pouched | hydration +20, bladder +15, immunity +1, leaves 1 pak-002 | — |
| wat-053 | Water, Chilled, Pouched | hydration +20, bladder +15, fun +1, leaves 1 pak-002 | 12 h → wat-005 |
| wat-054 | Water, Warm, Pouched | hydration +20, bladder +15, stress -2, leaves 1 pak-002 | 6 h → wat-005 |
| wat-055 | Water, Sparkling, Pouched | hydration +20, bladder +16, fun +2, leaves 1 pak-002 | 72 h → wat-005 |
| wat-056 | Ice, Block | — | 48 h → wat-001 |
| wat-057 | Jug, Water, Empty | — | — |
| wat-058 | Jug, Water, Full | — | — |
| wat-059 | Bladder, Water, Empty | — | — |
| wat-060 | Bladder, Water, Full | — | — |
| wat-061 | Condensate, Humidity | — | — |
| wat-062 | Drum, Water, Full | — | — |
| wat-063 | Canteen, Empty | — | — |
| wat-064 | Canteen, Full | hydration +25, bladder +18, toxin -2, leaves 1 wat-063 | — |
| wat-065 | Flask, Vacuum, Empty | — | — |
| wat-066 | Flask, Vacuum, Hot Water | hydration +20, bladder +15, stress -3, leaves 1 wat-065 | — |
| wat-067 | Liner, Bladder | — | — |
| wat-068 | Pretreat Dose, Urine | — | — |
| wat-069 | Tablet, Descaler, Vapour Still | — | — |
| wat-070 | Cartridge, Mineral Dosing | fits wat.mineralizer | 500 h → wat-071 |
| wat-071 | Cartridge, Mineral, Empty | — | — |
| wat-072 | Auger, Regolith Water Extractor | fits wat.extractor | — |
| wat-073 | Trap, Regolith Water Extractor | fits wat.extractor | — |
| wat-074 | Heating Plate, Ice Melter | fits wat.melter | — |
| wat-075 | Intake Screen, Ice Melter | fits wat.melter | — |
| wat-076 | Centrifuge Drum, Urine Reclaimer | fits wat.reclaimer | — |
| wat-077 | Tube, Urine Reclaimer | fits wat.reclaimer | — |
| wat-078 | Condenser Coil, Vapour Still | fits wat.still | — |
| wat-079 | Evaporator Pan, Vapour Still | fits wat.still | — |
| wat-080 | Pump Head, Water Purifier | fits wat.purifier | — |
| wat-081 | Flow Valve, Water Purifier | fits wat.purifier | — |
| wat-082 | Mixing Chamber, Mineralizer | fits wat.mineralizer | — |
| wat-083 | Dosing Valve, Mineralizer | fits wat.mineralizer | — |
| wat-084 | Element, Hot and Cold Dispenser | fits wat.dispenser | — |
| wat-085 | Chiller, Hot and Cold Dispenser | fits wat.dispenser | — |
| wat-086 | Ice Tray, Hot and Cold Dispenser | fits wat.dispenser | — |
| wat-087 | Fill Nozzle, Water Bottler | fits wat.bottler | — |
| wat-088 | Capping Head, Water Bottler | fits wat.bottler | — |
| wat-089 | Fan, Moisture Condenser | fits any.condenser | — |
| wat-090 | Drip Tray, Moisture Condenser | fits any.condenser | — |
| wat-091 | Separator, Humidity | fits any.lifesupport | — |
| wat-092 | Gasket, Water Loop | fits any.lifesupport | — |
| wat-093 | Kit, Regolith Water Extractor | installs wat.extractor | — |
| wat-094 | Kit, Ice Melter | installs wat.melter | — |
| wat-095 | Kit, Urine Reclaimer | installs wat.reclaimer | — |
| wat-096 | Kit, Vapour Still | installs wat.still | — |
| wat-097 | Kit, Water Purifier | installs wat.purifier | — |
| wat-098 | Kit, Mineralizer | installs wat.mineralizer | — |
| wat-099 | Kit, Hot and Cold Dispenser | installs wat.dispenser | — |
| wat-100 | Kit, Water Bottler | installs wat.bottler | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| bake regolith water | wat.extractor | 240 | 4 ore-001, 2 pwr-001 | 2 wat-020, 3 wat-039 | — |
| bake comet dust | wat.extractor | 180 | 2 ore-035, 2 pwr-001 | 2 wat-022, 1 wat-039 | — |
| scrape vent frost | crew | 30 | — | 1 wat-021 | — |
| drain the humidity separator | any.lifesupport | 240 | — | 1 wat-061 | — |
| wring water from the plant rack | any.condenser | 180 | — | 1 wat-024 | — |
| melt water ice | wat.melter | 45 | 3 ore-002, 1 pwr-001 | 3 wat-002 | — |
| melt dirty ice | wat.melter | 60 | 3 ore-012, 1 pwr-001 | 3 wat-014, 1 wat-034 | — |
| melt brine ice | wat.melter | 60 | 2 ore-011, 1 pwr-001 | 2 wat-023 | — |
| melt hull frost | wat.melter | 20 | 3 wat-021, 1 pwr-001 | 3 wat-014 | — |
| settle meltwater | wat.melter | 60 | 3 wat-014 | 3 wat-002, 1 wat-034 | — |
| settle regolith water | wat.melter | 60 | 3 wat-020 | 2 wat-002, 1 wat-034 | — |
| reclaim urine | wat.reclaimer | 120 | 4 toi-001, 1 wat-068, 2 pwr-001 | 3 wat-015, 1 wat-017 | — |
| reclaim stale urine | wat.reclaimer | 150 | 4 toi-006, 1 wat-068, 2 pwr-001 | 2 wat-015, 2 wat-017 | — |
| spin brackish water | wat.reclaimer | 90 | 3 wat-023, 1 pwr-001 | 2 wat-016, 1 wat-011 | — |
| reclaim contaminated water | wat.reclaimer | 120 | 3 wat-037, 2 pwr-001 | 2 wat-016, 1 wat-034 | — |
| reclaim backwash water | wat.reclaimer | 90 | 3 wat-036, 1 pwr-001 | 2 wat-016, 1 wat-034 | — |
| mix urine pretreat | any.bench | 20 | 1 chm-001, 1 wat-009 | 4 wat-068 | — |
| distil raw water | wat.still | 90 | 3 wat-002, 2 pwr-001 | 2 wat-003, 1 wat-011 | — |
| distil urine distillate | wat.still | 60 | 3 wat-015, 1 pwr-001 | 2 wat-003, 1 wat-017 | — |
| raise steam | wat.still | 30 | 2 wat-002, 1 pwr-001 | 2 wat-012 | — |
| raise clean steam | wat.still | 20 | 2 wat-041, 1 pwr-001 | 3 wat-012 | — |
| concentrate still brine | wat.still | 120 | 3 wat-011, 2 pwr-001 | 1 wat-032, 1 wat-003 | — |
| dry urine brine | wat.still | 120 | 3 wat-017, 2 pwr-001 | 1 wat-015, 1 wat-033 | — |
| crystallise brine | wat.still | 180 | 2 wat-032, 2 pwr-001 | 1 ing-002, 1 wat-033 | — |
| distil heavy water | wat.still | 480 | 6 wat-003, 4 pwr-001 | 1 wat-038, 4 wat-031 | — |
| descale the still | wat.still | 30 | 1 wat-069 | 1 wat-035 | — |
| press descaler tablets | any.bench | 20 | 1 chm-065 | 3 wat-069 | — |
| dissolve boiler scale | any.bench | 20 | 2 wat-035, 1 chm-009 | 1 chm-018 | — |
| bag sediment sludge for treatment | crew | 10 | 2 wat-034 | 1 san-058 | — |
| bag still residue for treatment | crew | 10 | 2 wat-033 | 1 san-019 | — |
| filter raw water | wat.purifier | 60 | 4 wat-002, 1 pwr-001 | 4 wat-025, 1 wat-036 | — |
| sterilise filtered water | wat.purifier | 30 | 4 wat-025, 1 pwr-001 | 4 wat-001 | — |
| purify raw water | wat.purifier | 90 | 4 wat-002, 2 pwr-001 | 3 wat-001, 1 wat-036 | — |
| polish urine distillate | wat.purifier | 60 | 4 wat-015, 1 pwr-001 | 4 wat-001 | — |
| polish reclaimed water | wat.purifier | 45 | 3 wat-016, 1 pwr-001 | 3 wat-001 | — |
| polish fuel cell water | wat.purifier | 20 | 3 wat-018, 1 pwr-001 | 3 wat-001 | — |
| polish sabatier water | wat.purifier | 30 | 3 wat-019, 1 pwr-001 | 3 wat-001 | — |
| polish transpiration water | wat.purifier | 30 | 3 wat-024, 1 pwr-001 | 3 wat-001 | — |
| polish humidity condensate | wat.purifier | 30 | 3 wat-061, 1 pwr-001 | 3 wat-001 | — |
| treat with a purification tablet | crew | 30 | 4 wat-002, 1 fil-053 | 4 wat-030 | — |
| chlorinate water | wat.purifier | 20 | 4 wat-025, 1 chm-037 | 4 wat-026 | — |
| soften hard water | wat.purifier | 60 | 3 wat-022, 1 pwr-001 | 3 wat-027, 1 wat-011 | — |
| deionize distilled water | wat.purifier | 45 | 3 wat-003, 1 pwr-001 | 3 wat-010 | — |
| polish ultrapure water | wat.purifier | 90 | 3 wat-010, 2 pwr-001 | 2 wat-028 | — |
| sterilise ultrapure water | wat.purifier | 60 | 3 wat-028, 1 pwr-001 | 3 wat-029 | — |
| make electrolysis feedwater | wat.purifier | 30 | 3 wat-010, 1 pwr-001 | 3 wat-040 | — |
| make boiler feedwater | wat.purifier | 30 | 3 wat-027, 1 chm-055 | 3 wat-041 | — |
| make coolant feedwater | wat.purifier | 30 | 3 wat-003, 1 pwr-001 | 3 wat-043 | — |
| mix cabin coolant | any.bench | 20 | 2 wat-043, 1 thm-035 | 2 thm-001 | — |
| make process water | wat.purifier | 20 | 4 wat-025, 1 pwr-001 | 4 wat-009 | — |
| reuse treated grey water | wat.purifier | 30 | 4 san-004, 1 pwr-001 | 4 wat-009 | — |
| blend irrigation water | wat.purifier | 20 | 3 san-004, 1 wat-002, 1 pwr-001 | 4 wat-042 | — |
| draw wash water | wat.purifier | 15 | 3 wat-025, 1 pwr-001 | 3 wat-044 | — |
| draw wash water from grey water | wat.purifier | 20 | 3 san-004, 1 pwr-001 | 3 wat-044 | — |
| mineralise distilled water | wat.mineralizer | 30 | 4 wat-003, 1 pwr-001 | 4 wat-008 | — |
| mineralise fuel cell water | wat.mineralizer | 30 | 4 wat-018, 1 pwr-001 | 4 wat-008 | — |
| make alkaline water | wat.mineralizer | 30 | 3 wat-001, 1 chm-012, 1 pwr-001 | 3 wat-047 | — |
| carbonate water | wat.mineralizer | 15 | 4 wat-007, 1 gas-043 | 4 wat-046 | — |
| refill a mineral cartridge | wat.mineralizer | 30 | 1 wat-071, 1 chm-058, 1 chm-018 | 1 wat-070 | — |
| fill a new mineral cartridge | wat.mineralizer | 30 | 1 pak-023, 1 chm-058, 1 chm-018 | 1 wat-070 | — |
| heat water | wat.dispenser | 10 | 2 wat-001, 1 pwr-001 | 2 wat-006 | — |
| chill water | wat.dispenser | 15 | 2 wat-001, 1 pwr-001 | 2 wat-007 | — |
| freeze ice cubes | wat.dispenser | 60 | 2 wat-001, 1 pwr-001 | 4 wat-013 | — |
| freeze a water block | wat.dispenser | 120 | 4 wat-001, 2 pwr-001 | 1 wat-056 | — |
| warm wash water | wat.dispenser | 10 | 2 wat-044, 1 pwr-001 | 2 wat-045 | — |
| fill a hot water flask | wat.dispenser | 10 | 1 wat-065, 2 wat-001, 1 pwr-001 | 1 wat-066 | — |
| fill a canteen | crew | 2 | 1 wat-063, 2 wat-001 | 1 wat-064 | — |
| bottle water | wat.bottler | 20 | 2 wat-001, 1 pak-003, 1 pwr-001 | 1 wat-004 | — |
| bottle mineral water | wat.bottler | 20 | 2 wat-008, 1 pak-003, 1 pwr-001 | 1 wat-048 | — |
| bottle sparkling water | wat.bottler | 20 | 2 wat-046, 1 pak-003, 1 pwr-001 | 1 wat-049 | — |
| bottle distilled water | wat.bottler | 20 | 2 wat-003, 1 pak-003, 1 pwr-001 | 1 wat-050 | — |
| pouch water | wat.bottler | 15 | 2 wat-001, 1 pak-001, 1 pwr-001 | 1 wat-005 | — |
| pouch mineral water | wat.bottler | 15 | 2 wat-008, 1 pak-001, 1 pwr-001 | 1 wat-052 | — |
| pouch chilled water | wat.bottler | 15 | 2 wat-007, 1 pak-001, 1 pwr-001 | 1 wat-053 | — |
| pouch warm water | wat.bottler | 15 | 2 wat-006, 1 pak-001, 1 pwr-001 | 1 wat-054 | — |
| pouch sparkling water | wat.bottler | 15 | 2 wat-046, 1 pak-001, 1 pwr-001 | 1 wat-055 | — |
| seal emergency sachets | wat.bottler | 20 | 1 wat-026, 1 pak-015 | 1 wat-051 | — |
| fill a water jug | wat.bottler | 10 | 1 wat-057, 4 wat-001 | 1 wat-058 | — |
| fill a water bladder | wat.bottler | 10 | 1 wat-059, 6 wat-001 | 1 wat-060 | — |
| fill a water drum | wat.bottler | 15 | 1 pak-025, 10 wat-001 | 1 wat-062 | — |
| pour out a water jug | crew | 5 | 1 wat-058 | 4 wat-001, 1 wat-057 | — |
| drain a water bladder | crew | 5 | 1 wat-060 | 6 wat-001, 1 wat-059 | — |
| drain a water drum | crew | 10 | 1 wat-062 | 10 wat-001, 1 pak-026 | — |
| mould a water jug | any.bench | 30 | 2 pol-035 | 1 wat-057 | — |
| cut a bladder liner | any.bench | 30 | 1 pol-031 | 1 wat-067 | — |
| sew a water bladder | any.bench | 40 | 1 wat-067, 1 fib-012, 1 pak-047 | 1 wat-059 | — |
| make a canteen | any.bench | 40 | 1 met-007, 1 pak-043 | 1 wat-063 | — |
| make a vacuum flask | any.bench | 45 | 1 met-034, 1 pak-050 | 1 wat-065 | — |
| make an extractor heating auger | any.bench | 90 | 1 met-008, 1 thm-004 | 1 wat-072 | — |
| make an extractor vapour trap | any.bench | 60 | 1 met-053, 1 thm-058 | 1 wat-073 | — |
| make a melter heating plate | any.bench | 60 | 1 met-005, 1 thm-004 | 1 wat-074 | — |
| make a melter intake screen | any.bench | 30 | 1 met-057 | 1 wat-075 | — |
| make a reclaimer centrifuge drum | any.bench | 90 | 1 met-034, 1 mec-010 | 1 wat-076 | — |
| make a reclaimer peristaltic tube | any.bench | 20 | 1 pol-037 | 1 wat-077 | — |
| make a still condenser coil | any.bench | 60 | 2 met-053 | 1 wat-078 | — |
| make a still evaporator pan | any.bench | 60 | 1 met-034 | 1 wat-079 | — |
| make a purifier pump head | any.bench | 60 | 1 mec-008, 1 pol-009 | 1 wat-080 | — |
| make a purifier flow valve | any.bench | 30 | 1 mec-007, 1 lgt-046 | 1 wat-081 | — |
| make a mineralizer mixing chamber | any.bench | 45 | 1 met-056, 1 mec-022 | 1 wat-082 | — |
| make a mineralizer dosing valve | any.bench | 30 | 1 mec-034 | 1 wat-083 | — |
| make a dispenser heating element | any.bench | 30 | 1 met-047, 1 cer-035 | 1 wat-084 | — |
| make a dispenser chiller coil | any.bench | 45 | 1 thm-058, 1 mec-042 | 1 wat-085 | — |
| mould a dispenser ice tray | any.bench | 20 | 1 pol-036 | 1 wat-086 | — |
| make a bottler fill nozzle | any.bench | 30 | 1 met-049 | 1 wat-087 | — |
| make a bottler capping head | any.bench | 45 | 1 met-049, 1 mec-005 | 1 wat-088 | — |
| make a condenser fan | any.bench | 30 | 1 mec-009, 1 pol-009 | 1 wat-089 | — |
| make a condenser drip tray | any.bench | 20 | 1 met-007 | 1 wat-090 | — |
| make a humidity separator | any.bench | 90 | 1 thm-058, 1 mec-008, 1 pol-055 | 1 wat-091 | — |
| cut water loop gaskets | any.bench | 15 | 1 pol-052 | 2 wat-092 | — |
| pack a regolith water extractor kit | any.bench | 120 | 1 fur-001, 1 wat-072, 1 wat-073, 1 mec-010 | 1 wat-093 | — |
| pack an ice melter kit | any.bench | 120 | 1 fur-001, 1 wat-074, 1 wat-075, 1 met-034 | 1 wat-094 | — |
| pack a urine reclaimer kit | any.bench | 120 | 1 fur-001, 1 wat-076, 1 wat-077, 1 mec-041 | 1 wat-095 | — |
| pack a vapour still kit | any.bench | 120 | 1 fur-001, 1 wat-078, 1 wat-079, 1 thm-004 | 1 wat-096 | — |
| pack a water purifier kit | any.bench | 120 | 1 fur-001, 1 wat-080, 1 wat-081, 1 lgt-021 | 1 wat-097 | — |
| pack a mineralizer kit | any.bench | 120 | 1 fur-001, 1 wat-082, 1 wat-083 | 1 wat-098 | — |
| pack a hot and cold dispenser kit | any.bench | 120 | 1 fur-001, 1 wat-084, 1 wat-085 | 1 wat-099 | — |
| pack a water bottler kit | any.bench | 120 | 1 fur-001, 1 wat-087, 1 wat-088, 1 ecp-010 | 1 wat-100 | — |
| ice a sprain with a water block | crew | 20 | 1 wat-056 | 3 wat-001 | pain -10 |
| rework tailings into regolith | wat.extractor | 60 | 4 wat-039, 1 pwr-001 | 3 ore-051 | — |

## Codex

| id | about | flavour |
|---|---|---|
| wat.extractor | Bakes water out of regolith and comet dust, and reworks the tailings it leaves. | HOT ROCK. DO NOT OPEN HOPPER WHILE AUGER TURNS. |
| wat.melter | Melts ice into raw water; the first device a capsule needs for water. | Ice is Company stock until melted. Water is Company stock after. |
| wat.reclaimer | Spins urine and dirty water back into distillate and reclaimed water, leaving brine or sludge. | Yesterday's tea is tomorrow's tea. Do not think about the middle part. |
| wat.still | Distils water, raises steam, concentrates and dries brines, and makes heavy water. | Coil descaled, seals replaced, rev 15. Output purity nominal. |
| wat.purifier | Filters, sterilises, chlorinates and polishes water into drinking, washing and feedwater grades. | Log turbidity at the start of every shift on Form 21W. Unlogged water is not potable. |
| wat.mineralizer | Adds minerals or carbonation to water and refills its own dosing cartridges. | MINERAL DOSING UNIT. CARTRIDGE IN USE. DO NOT BYPASS. |
| wat.dispenser | Heats, chills and freezes drinking water, and warms wash water. | LEFT HOT. RIGHT COLD. SCALD RISK. |
| wat.bottler | Bottles, pouches and seals water, and fills jugs, bladders and drums. | Bottled water leaving the station is recorded. Its destination is not. |
| wat-001 | Water clean enough to drink, cook and wash with; left standing, it goes stale into raw water. | Potable water is metered per operator. Consumption above allowance is reviewed. |
| wat-002 | Unpurified water from melted ice or settling; drinkable at a cost, far better purified. | NON POTABLE. TREAT BEFORE USE. |
| wat-003 | Pure distilled water that keeps; the base for mineral, coolant, lab and medical water. | Conductivity checked, reading near zero. Passed, rev 3. |
| wat-004 | Drinking water capped in a bottle that keeps; leaves an empty bottle. | Closest thing to money aboard. The slot takes it either way. |
| wat-005 | Drinking water sealed in a pouch that keeps; leaves an empty pouch. | SQUEEZE TO DRINK. RETURN POUCH. |
| wat-006 | Heated drinking water that calms, for tea, instant food and washing; cools soon. | Draw hot water into insulated vessels only, Proc 801. Scalds are reported on Form 4H. |
| wat-007 | Cold drinking water, slightly refreshing, and the start of sparkling water; warms back soon. | Drink it before the cabin takes the cold back. |
| wat-008 | Water with minerals added back; keeps a while and slightly supports immunity. | Mineral content complies with Company drinking guidance. Taste is not regulated. |
| wat-009 | Filtered or reused grey water for mashing, pulping and other work that is not drinking. | PROCESS WATER. NOT FOR DRINKING. |
| wat-010 | Distilled water stripped of ions, for feedwater, coolant and ultrapure water. | AGGRESSIVE TO METALS. STAINLESS OR PLASTIC LINES ONLY. |
| wat-011 | Salty leftover of distilling and softening; concentrated into salt or used to regenerate resin. | Route still brine to the evaporator. Drain disposal requires Form 22B. |
| wat-012 | Steam raised in the still, for activating charcoal; it condenses back to water fast. | LIVE STEAM. INVISIBLE. KEEP HANDS CLEAR OF VALVES. |
| wat-013 | Frozen drinking water for cold drinks; melts back to water soon. | Ice is issued for medical and catering use. Recreational ice is at station discretion. |
| wat-014 | Muddy water from dirty ice or frost; settled before it turns raw. | Let it stand. The mud goes down. Mostly. |
| wat-015 | Water recovered from urine, polished or distilled into drinking water. | Recovered water meets potable standard after treatment. Its origin is not shown at the tap. |
| wat-016 | Water spun back from brackish or dirty water; drinkable, though unpleasant to drink. | Meets standard. Smell within tolerance. Tolerance revised, rev 7. |
| wat-017 | The concentrated leftover of urine reclaiming, dried in the still or crystallised for treatment. | WASTE BRINE. GLOVES REQUIRED. NO SKIN CONTACT. |
| wat-018 | Pure water from the fuel cells, ready to polish or mineralise. | Purity high, temperature warm. Released to purifier line. |
| wat-019 | Water made by the methane reactor from carbon dioxide and hydrogen. | Made from exhaled air. The air was ours, so the water is too. |
| wat-020 | Gritty, toxic water baked from regolith; drinkable in a pinch, better settled. | HIGH SEDIMENT. HIGH TOXIN. SETTLE AND TREAT. |
| wat-021 | Frost scraped from the vents; it soon thaws into meltwater. | Scrape with plastic tools only. Metal scrapers mark the vent, Proc 812. |
| wat-022 | Mineral-heavy water baked from comet dust, softened before use. | Leaves white rings on everything. The rings outlast the cups. |
| wat-023 | Salty water melted from brine ice; spun in the reclaimer before drinking. | SALINE. RECLAIM BEFORE DRINKING. |
| wat-024 | Water wrung from the plant rack's damp air, polished to drink. | Plant transpiration is a Company water source and is recovered in full. |
| wat-025 | Raw water through the filters; next sterilised, chlorinated, or drawn for washing and process. | Filtered, not sterile. Do not mistake one for the other. Rev 2. |
| wat-026 | Filtered water dosed with chlorine; it keeps, and fills emergency sachets. | Smells of chlorine. Nobody aboard remembers water smelling of anything else. |
| wat-027 | Hard water stripped of scale, for boiler feedwater and the dishwasher softener. | SOFTENED. FOR PLANT USE. NOT FOR DRINKING. |
| wat-028 | Polished deionized water, for sterile water and concentrating peroxide. | Draw into certified vessels only. Uncertified vessels contaminate the batch, Proc 820. |
| wat-029 | Ultrapure water sterilised for culture work, the clean bench and medical use. | STERILE. OPEN AT CLEAN BENCH ONLY. |
| wat-030 | Raw water treated by hand with a purification tablet; safe enough to drink. | Allow full contact time before drinking, Proc 803. Tablets are not a filter. |
| wat-031 | Water condensed back from steam; drinkable and fairly clean. | Condensate recovered, temperature falling. Fit for polishing. |
| wat-032 | Thickened still brine, crystallised into salt. | Salt recovered from brine is credited to the galley line at standard rate. |
| wat-033 | Dried residue of brines, bagged for waste treatment. | RESIDUE. BAG AND TAG. DO NOT TASTE. |
| wat-034 | Mud settled out of meltwater and dirty water, bagged for waste treatment. | The bucket under the melter is never empty. Nobody remembers it empty. |
| wat-035 | Scale freed from the still when it is descaled; dissolved into calcium chloride. | Scale removed in flakes. Thickness noted. Descale interval shortened. |
| wat-036 | Dirty water flushed from filters; washes filter media, or is reclaimed before it fouls. | Reclaim backwash within three days or it is reclassified as contaminated, Proc 805. |
| wat-037 | Fouled, toxic water; reclaimed, or used to leach regolith. | CONTAMINATED. DO NOT DRINK. DO NOT WASH. |
| wat-038 | Water rich in heavy hydrogen, distilled slowly and split for deuterium. | Heavy water is a controlled material. Each litre is accounted for. |
| wat-039 | Baked rock left by water extraction; reworked or weathered into regolith fines. | Dry, grey, and it gets into the bunk somehow. |
| wat-040 | Deionized water ready for the electrolyser to split into oxygen and hydrogen. | ELECTROLYSER FEED ONLY. PURITY CRITICAL. |
| wat-041 | Softened water dosed against scale, for raising clean steam. | Dosing confirmed, hardness low. Released to still. |
| wat-042 | Grey water blended with raw water for the farm; goes stale if left. | Irrigation water is drawn against the farm allocation. Personal use is a disciplinary matter. |
| wat-043 | Distilled water for mixing cabin coolant. | COOLANT FEED. NOT FOR DRINKING. DO NOT DILUTE. |
| wat-044 | Water for washing the body and filter media; leaves grey water, and fouls if kept. | Wash water is used once and drained to grey. Reuse requires Form 30G. |
| wat-045 | Warmed wash water, cleaner and calmer to wash with; cools back soon. | Warm wash, once a shift if the power holds. Nearest thing to rest. |
| wat-046 | Chilled water carbonated with a cartridge, for sodas and spritzers; goes flat soon. | Carbonation is a discretionary use of carbon dioxide stock. Discretion is reviewed. |
| wat-047 | Drinking water with bicarbonate added; it keeps, and eases toxin slightly. | Bicarbonate dosed, alkalinity in range. Claimed benefits not verified. |
| wat-048 | Mineral water capped in a bottle that keeps; leaves an empty bottle. | MINERAL WATER. CAPPED AT STATION. RETURN BOTTLE. |
| wat-049 | Sparkling water capped in a bottle that holds its fizz; leaves an empty bottle. | PRESSURISED. OPEN SLOWLY. POINT AWAY FROM CONSOLE. |
| wat-050 | Distilled water capped in a bottle that keeps; leaves an empty bottle. | Flat, pure, and the safest thing to send through the slot. |
| wat-051 | A small sealed sachet of chlorinated water, packed into ration packs and grab bags. | Sachets are counted at every audit. Missing sachets are deducted at emergency rates. |
| wat-052 | Mineral water sealed in a pouch that keeps; leaves an empty pouch. | Pouch sealed, mineral dose confirmed. Lot 0218. |
| wat-053 | Chilled water in a pouch; it warms into a plain water pouch. | Cold for half a shift. Drink it in the first half. |
| wat-054 | Warm, calming water in a pouch; it cools into a plain water pouch. | Hold it in both hands before drinking. The warmth is the point. |
| wat-055 | Sparkling water in a pouch; it goes flat into a plain water pouch. | CARBONATED. POUCH MAY SWELL. DO NOT PUNCTURE. |
| wat-056 | A block of ice for icing a sprain; melts back into drinking water. | Wrap in cloth before applying to injury, Proc 830. Direct contact is a second injury. |
| wat-057 | An empty moulded jug for carrying drinking water. | POTABLE WATER ONLY. NO OTHER FLUIDS. |
| wat-058 | A jug of drinking water to carry or pass on, poured out when needed. | Both hands. The deck does not tilt, but carry it as if it does. |
| wat-059 | An empty sewn water bladder, filled at the bottler. | Seams pressure tested. Leak at corner. Patched, rev 2. |
| wat-060 | A bladder of drinking water to carry, drained when needed. | Water bladders are for transport. Storage in quarters is not permitted. |
| wat-061 | Water drained from the life support humidity separator, polished to drink. | The whole capsule's breath, collected in a tray. Polish it twice. |
| wat-062 | A drum of drinking water for bulk storage and trade; drains to an empty drum. | HEAVY. ROLL, DO NOT LIFT. CRUSH HAZARD. |
| wat-063 | An empty aluminium canteen for drinking water. | Dented, serviceable. Dents logged at issue. New dents are chargeable. |
| wat-064 | A canteen of drinking water; leaves the canteen when drunk. | Personnel on rounds carry a full canteen. This is policy, not a suggestion. |
| wat-065 | An empty insulated flask for carrying hot water. | INSULATED. HOT CONTENTS. CAP TIGHT. |
| wat-066 | A flask of hot, calming water; leaves the flask when drunk. | Unscrew slowly. The steam comes first, then whatever comfort is left. |
| wat-067 | Cut barrier film, sewn into a water bladder. | Cut to template W12. Off-template liners leak at the seam, Proc 840. |
| wat-068 | An acid dose added to urine before it is reclaimed or processed. | ACID. ADD TO URINE BEFORE PROCESSING. NEVER AFTER. |
| wat-069 | A citric tablet that descales the vapour still, freeing boiler scale. | Tablet dropped, fizz observed, scale released. Logged. |
| wat-070 | The dosing cartridge of the mineralizer; it empties with use and is refilled. | Cartridges are refilled, not replaced. Replacement requests are declined. |
| wat-071 | A spent mineral cartridge, refilled at the mineralizer. | EMPTY. RETURN FOR REFILL. DO NOT DISCARD. |
| wat-072 | A spare heated auger for the regolith water extractor. | Flights worn, heater sound. Replace at next service, rev 4. |
| wat-073 | A spare vapour trap for the regolith water extractor. | Catches the steam the auger drives off. Clear it or the capsule fogs. |
| wat-074 | A spare heating plate for the ice melter. | HOT SURFACE WHEN FITTED. ISOLATE BEFORE HANDLING. |
| wat-075 | A spare intake screen for the ice melter. | Clear the screen of gravel each shift, Proc 806. A blocked screen is a melter fault. |
| wat-076 | A spare centrifuge drum for the urine reclaimer. | HIGH SPEED PART. BALANCE BEFORE FITTING. |
| wat-077 | A spare peristaltic tube for the urine reclaimer. | Squeezed every minute of every shift. It is not the only one. |
| wat-078 | A spare copper condenser coil for the vapour still. | Copper is a recoverable material. Worn coils are returned, not binned. |
| wat-079 | A spare evaporator pan for the vapour still. | Pan scaled to limit. Descaled twice. Replaced, rev 9. |
| wat-080 | A spare pump head for the water purifier. | SPARE PART. PURIFIER PUMP. FLOW ARROW TO OUTLET. |
| wat-081 | A spare flow valve for the water purifier. | Open, closed or stuck. Stuck is the usual one. |
| wat-082 | A spare mixing chamber for the mineralizer. | Flush the chamber with distilled water before first use, Proc 815. |
| wat-083 | A spare dosing valve for the mineralizer. | Dose rate set to spec. Tea tastes of chalk. Spec stands. |
| wat-084 | A spare heating element for the hot and cold dispenser. | ISOLATE POWER. ELEMENT RETAINS HEAT. |
| wat-085 | A spare chiller coil for the hot and cold dispenser. | Chilled water is a comfort service and the first service suspended under load. |
| wat-086 | A spare silicone ice tray for the hot and cold dispenser. | Twist, pop, done. The one part aboard that never fails. |
| wat-087 | A spare fill nozzle for the water bottler. | Fill to the line. Overfill is waste, underfill is fraud, Proc 850. |
| wat-088 | A spare capping head for the water bottler. | Torque checked, caps tight, one stripped. Within tolerance. |
| wat-089 | A spare fan for the moisture condenser. | ROTATING BLADES. GUARD ON BEFORE POWER. |
| wat-090 | A spare drip tray for the moisture condenser. | Empty it before it spills. It always spills on the cot side. |
| wat-091 | A spare humidity separator for life support, the part that drains condensate. | Life support parts are fitted by the station operator. Failure is attributed accordingly. |
| wat-092 | A spare gasket for the life support water loop. | SMALL PART. LARGE LEAK IF OMITTED. |
| wat-093 | A crated kit that installs a regolith water extractor. | MINING EQUIPMENT. COF WATER WORKS. HEAVY. |
| wat-094 | A crated kit that installs an ice melter. | The ice melter is a standard first installation. Water supply is the station's duty thereafter. |
| wat-095 | A crated kit that installs a urine reclaimer. | Nobody wants to unpack it. Everybody wants it running. |
| wat-096 | A crated kit that installs a vapour still. | Coil intact, pan clean, seals present. Accepted at the hatch. |
| wat-097 | A crated kit that installs a water purifier. | Commission per Manual 21. First output is drained, not drunk. |
| wat-098 | A crated kit that installs a mineralizer. | CARTRIDGE NOT INCLUDED. REQUISITION SEPARATELY. |
| wat-099 | A crated kit that installs a hot and cold dispenser. | Installation entitles the station to hot water within its power budget. |
| wat-100 | A crated kit that installs a water bottler. | BOTTLING EQUIPMENT. FOOD GRADE. KEEP SEALED UNTIL INSTALLED. |
