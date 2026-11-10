# Heat & Cooling — `thm`

What keeps the cabin warm and the power plant cool. Rock wool, aerogel and foil are pressed into insulation; coil wire
and ceramic become heater elements and heaters; salt hydrate, paraffin and iron powder are filled into heat packs;
glycol, ammonia and slush are mixed into coolant, piped through heat pipes, exchangers and radiators. Heaters and
insulation sit in life support (`cabin.heat` an hour at a time), packs are spent there once, and the coolant charges and
radiators go through the service hatch to the grid. Worn insulation crumbles back into fluff, burnt-out heaters are
stripped, spent packs and coolant are recharged.

## Devices

| id | device | role | cells |
|---|---|---|---|
| thm.coolantmixer | TH120 Coolant Mixer | atmos | 2x1 |
| thm.heaterbench | TH240 Heater Bench | atmos | 2x2 |
| thm.insulationpress | TH360 Insulation Press | atmos | 2x2 |
| thm.packfiller | TH80 Heat Pack Filler | atmos | 2x1 |
| thm.pipeforge | TH500 Heat Pipe Forge | power | 2x2 |
| thm.exchangerbay | TH900 Exchanger Bay | power | 3x2 |

## Items

| id | item | use | decays |
|---|---|---|---|
| thm-001 | Coolant, Cabin | — | — |
| thm-002 | Heat Pack, Instant | cabin.heat +6, leaves 1 scr-002 | — |
| thm-003 | Batt, Insulation | cabin.heat +1/h | 720 h → thm-012 |
| thm-004 | Element, Heater | — | — |
| thm-005 | Exchanger, Heat | fits any.lifesupport | 1440 h → scr-004 |
| thm-006 | Heat Pipe | — | — |
| thm-007 | Radiator, Panel | — | — |
| thm-008 | Paste, Thermal | — | — |
| thm-009 | Heater, Space | cabin.heat +2/h | 480 h → thm-013 |
| thm-010 | Heat Pack, Reusable | cabin.heat +8, leaves 1 thm-011 | — |
| thm-011 | Heat Pack, Spent | — | — |
| thm-012 | Insulation, Crumbled | — | — |
| thm-013 | Heater, Burnt Out | — | — |
| thm-014 | Coolant, Spent | — | — |
| thm-015 | Fluff, Rock Wool | — | — |
| thm-016 | Mat, Rock Wool | — | — |
| thm-017 | Batt, Glass Wool | cabin.heat +1/h | 960 h → thm-012 |
| thm-018 | Aerogel, Silica | — | — |
| thm-019 | Sheet, Aerogel | — | — |
| thm-020 | Blanket, Aerogel | cabin.heat +2/h | 720 h → thm-012 |
| thm-021 | Foil, Laminated | — | — |
| thm-022 | Insulation, Multi Layer | cabin.heat +2/h | 960 h → thm-012 |
| thm-023 | Panel, Insulation, Wall | cabin.heat +2/h | 1440 h → thm-012 |
| thm-024 | Fill, Cavity Insulation | cabin.heat +2/h | 1440 h → thm-012 |
| thm-025 | Sleeve, Insulating | — | — |
| thm-026 | Lagging, Pipe | cabin.heat +1/h | 720 h → thm-012 |
| thm-027 | Film, Window Insulation | cabin.heat +1/h | 240 h → scr-002 |
| thm-028 | Seal, Draught, Door | cabin.heat +1/h | 480 h → scr-002 |
| thm-029 | Excluder, Draught | cabin.heat +1/h | 360 h → scr-005 |
| thm-030 | Panel, Reflective | cabin.heat +1/h | 720 h → scr-001 |
| thm-031 | Sheet, Survival, Foil | cabin.heat +4, leaves 1 scr-002 | — |
| thm-032 | Curtain, Thermal | cabin.heat +1/h, stress -1/h | 480 h → scr-005 |
| thm-033 | Slush, Ice | — | 24 h → wat-002 |
| thm-034 | Coolant, Slush | — | — |
| thm-035 | Glycol, Concentrated | — | — |
| thm-036 | Charge, Loop, Glycol | ship.grid +4, leaves 1 thm-014 | — |
| thm-037 | Charge, Loop, Ammonia | ship.grid +6, leaves 1 thm-014 | — |
| thm-038 | Coolant, Heavy Duty | — | — |
| thm-039 | Coolant, Cryogenic | — | — |
| thm-040 | Fluid, Coolant Flush | ship.grid +2, leaves 1 thm-014 | — |
| thm-041 | Cartridge, Coolant Reservoir | fits any.lifesupport | 720 h → pak-006 |
| thm-042 | Cartridge, Loop Top-Up | ship.grid +3, leaves 1 pak-006 | — |
| thm-043 | Blank, Pipe, Copper | — | — |
| thm-044 | Mesh, Wick | — | — |
| thm-045 | Wick, Sintered | — | — |
| thm-046 | Heat Pipe, Sealed | — | — |
| thm-047 | Heat Pipe, Loop | — | — |
| thm-048 | Spreader, Heat, Flat | — | — |
| thm-049 | Bundle, Heat Pipe | — | — |
| thm-050 | Stock, Fin, Aluminium | — | — |
| thm-051 | Fin, Radiator | — | — |
| thm-052 | Radiator, Honeycomb | — | — |
| thm-053 | Radiator Wing, Deployable | ship.grid +15 | — |
| thm-054 | Panel, Louver | ship.grid +5 | — |
| thm-055 | Exchanger, Plate | — | — |
| thm-056 | Exchanger, Shell and Tube | — | — |
| thm-057 | Exchanger, Cabin Air | fits any.lifesupport | 1440 h → scr-004 |
| thm-058 | Coil, Condensing | fits any.condenser | 1440 h → scr-001 |
| thm-059 | Plate, Cooling, Liquid | — | — |
| thm-060 | Assembly, Cooling Loop | ship.grid +12 | — |
| thm-061 | Exchanger, Heat, Reactor | ship.grid +15 | — |
| thm-062 | Wire, Heating Coil | — | — |
| thm-063 | Core, Heater | — | — |
| thm-064 | Thermostat, Heater | — | — |
| thm-065 | Heater, Radiant Panel | cabin.heat +3/h | 600 h → thm-013 |
| thm-066 | Heater, Convection | cabin.heat +3/h | 600 h → thm-013 |
| thm-067 | Mat, Floor Heating | cabin.heat +2/h | 720 h → thm-013 |
| thm-068 | Heater, Thermostatic | cabin.heat +4/h | 720 h → thm-013 |
| thm-069 | Element, Heating Pad | — | — |
| thm-070 | Element, Heater, Life Support | fits any.lifesupport | 960 h → thm-013 |
| thm-071 | Fan Coil, Life Support | fits any.lifesupport | 1440 h → mec-080 |
| thm-072 | Pump, Coolant, Life Support | fits any.lifesupport | 1440 h → mec-077 |
| thm-073 | Unit, Heat Recovery | cabin.heat +3/h | 1200 h → scr-004 |
| thm-074 | Loop, Waste Heat | cabin.heat +3/h | 1200 h → scr-004 |
| thm-075 | Collector, Solar Heat | cabin.heat +2/h | 960 h → scr-004 |
| thm-076 | Loop, Radiant Floor | cabin.heat +3/h | 1200 h → scr-004 |
| thm-077 | Core, Thermal, Habitat | cabin.heat +5/h | 1440 h → scr-004 |
| thm-078 | Fill, Paraffin | — | — |
| thm-079 | Fill, Salt Hydrate | — | — |
| thm-080 | Charge, Iron Powder | — | — |
| thm-081 | Casing, Heat Pack | — | — |
| thm-082 | Pack, Phase-Change | cabin.heat +10, leaves 1 thm-083 | — |
| thm-083 | Pack, Phase-Change, Spent | — | — |
| thm-084 | Tile, Wall, Phase-Change | cabin.heat +1/h | 960 h → thm-083 |
| thm-085 | Cell, Thermal Battery | cabin.heat +2/h | 480 h → scr-004 |
| thm-086 | Warmer, Hand | cabin.heat +3, stress -2, leaves 1 scr-002 | — |
| thm-087 | Pack, Cold, Gel | pain -8, leaves 1 thm-088 | — |
| thm-088 | Pack, Gel, Warm | — | — |
| thm-089 | Paddle, Coolant Mixer | fits thm.coolantmixer | 2000 h → scr-001 |
| thm-090 | Contactor, Heater Bench | fits thm.heaterbench | 1500 h → scr-003 |
| thm-091 | Platen, Insulation Press | fits thm.insulationpress | 2000 h → scr-001 |
| thm-092 | Nozzle, Heat Pack Filler | fits thm.packfiller | 1000 h → scr-004 |
| thm-093 | Die, Heat Pipe Forge | fits thm.pipeforge | 1500 h → scr-001 |
| thm-094 | Gasket, Tube Bundle | fits thm.exchangerbay | 1000 h → scr-002 |
| thm-095 | Kit, Coolant Mixer | installs thm.coolantmixer | — |
| thm-096 | Kit, Heater Bench | installs thm.heaterbench | — |
| thm-097 | Kit, Insulation Press | installs thm.insulationpress | — |
| thm-098 | Kit, Heat Pack Filler | installs thm.packfiller | — |
| thm-099 | Kit, Heat Pipe Forge | installs thm.pipeforge | — |
| thm-100 | Kit, Exchanger Bay | installs thm.exchangerbay | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| mix cabin coolant | thm.coolantmixer | 40 | 2 wat-001, 1 chm-032, 1 pwr-001 | 3 thm-001 | — |
| cut slush into coolant | thm.coolantmixer | 40 | 2 thm-034, 1 chm-018, 1 pwr-001 | 2 thm-001 | — |
| reclaim spent coolant | thm.coolantmixer | 60 | 3 thm-014, 1 chm-005, 1 pwr-001 | 2 thm-001, 1 san-001 | — |
| stir brine coolant | any.bench | 60 | 2 wat-002, 1 ing-002 | 1 thm-001 | — |
| freeze cold slush | thm.coolantmixer | 90 | 2 wat-002, 1 pwr-001 | 2 thm-033 | — |
| crush ice into slush | any.bench | 30 | 1 ore-002 | 1 thm-033 | — |
| mix slush coolant | thm.coolantmixer | 40 | 2 thm-033, 1 ing-002, 1 pwr-001 | 2 thm-034 | — |
| concentrate glycol | thm.coolantmixer | 60 | 2 chm-032, 1 wat-010, 1 pwr-001 | 2 thm-035 | — |
| charge a glycol loop canister | thm.coolantmixer | 50 | 2 thm-035, 1 thm-001, 1 pak-005 | 1 thm-036 | — |
| charge an ammonia loop canister | thm.coolantmixer | 50 | 2 chm-003, 1 thm-001, 1 pak-005, 1 pwr-001 | 1 thm-037 | — |
| blend heavy duty coolant | thm.coolantmixer | 60 | 2 thm-035, 1 pol-074, 1 pwr-001 | 2 thm-038 | — |
| chill cryo coolant | thm.coolantmixer | 90 | 2 thm-038, 1 gas-028, 1 pwr-001 | 1 thm-039 | — |
| mix coolant flush | thm.coolantmixer | 40 | 2 wat-010, 1 chm-055, 1 pwr-001 | 2 thm-040 | — |
| blend thermal paste | thm.coolantmixer | 45 | 1 pol-074, 1 cer-037, 1 pwr-001 | 3 thm-008 | — |
| knead thermal paste | any.bench | 30 | 1 pol-006, 1 met-061 | 1 thm-008 | — |
| fill a coolant reservoir cartridge | thm.packfiller | 60 | 2 thm-038, 1 pak-005, 1 pwr-001 | 1 thm-041 | — |
| fill a loop top-up cartridge | thm.packfiller | 40 | 1 thm-001, 1 pak-005, 1 pwr-001 | 1 thm-042 | — |
| spin rock wool | thm.insulationpress | 120 | 3 ore-001, 2 pwr-001 | 3 thm-015 | — |
| spin slag wool | thm.insulationpress | 90 | 2 met-010, 1 pwr-001 | 3 thm-015 | — |
| re-fluff crumbled insulation | thm.insulationpress | 60 | 2 thm-012, 1 pwr-001 | 2 thm-015 | — |
| press rock wool mat | thm.insulationpress | 40 | 3 thm-015, 1 pol-010, 1 pwr-001 | 2 thm-016 | — |
| wrap insulation batts | thm.insulationpress | 60 | 2 thm-016, 1 pol-002, 1 pwr-001 | 2 thm-003 | — |
| stuff a rag batt | any.bench | 45 | 3 scr-005, 1 pol-002 | 1 thm-003 | — |
| wrap glass wool batts | thm.insulationpress | 60 | 2 cer-025, 1 pol-002, 1 pwr-001 | 2 thm-017 | — |
| gel silica aerogel | thm.insulationpress | 120 | 2 ore-005, 1 chm-027, 1 chm-004, 2 pwr-001 | 1 thm-018 | — |
| lay aerogel sheet | thm.insulationpress | 90 | 2 thm-018, 1 fib-018, 1 pwr-001 | 2 thm-019 | — |
| sew an aerogel blanket | thm.insulationpress | 60 | 2 thm-019, 1 fib-059, 1 pwr-001 | 1 thm-020 | — |
| laminate foil layer | thm.insulationpress | 40 | 2 met-039, 1 pol-002, 1 pwr-001 | 3 thm-021 | — |
| stack multi layer insulation | thm.insulationpress | 90 | 3 thm-021, 1 thm-003, 1 pol-032, 1 pwr-001 | 1 thm-022 | — |
| press a wall insulation panel | thm.insulationpress | 120 | 2 thm-003, 1 cer-009, 1 pwr-001 | 1 thm-023 | — |
| blow cavity fill | thm.insulationpress | 60 | 3 thm-015, 1 scr-061, 1 pwr-001 | 1 thm-024 | — |
| form insulating sleeves | thm.insulationpress | 60 | 1 thm-016, 1 pol-002, 1 pwr-001 | 2 thm-025 | — |
| tape pipe lagging | any.bench | 40 | 2 thm-025, 1 pol-063 | 1 thm-026 | — |
| laminate window film | thm.insulationpress | 40 | 1 pol-031, 1 thm-021, 1 pwr-001 | 2 thm-027 | — |
| cut door draught seals | any.bench | 30 | 1 pol-003, 1 fib-005 | 2 thm-028 | — |
| roll a draught excluder | any.bench | 40 | 1 fib-085, 1 fib-004 | 1 thm-029 | — |
| press a reflective panel | thm.insulationpress | 90 | 2 thm-021, 1 cer-009, 1 pwr-001 | 1 thm-030 | — |
| cut foil survival sheets | thm.insulationpress | 30 | 2 thm-021, 1 pwr-001 | 2 thm-031 | — |
| line a thermal curtain | any.bench | 60 | 2 fib-058, 1 thm-021 | 1 thm-032 | — |
| draw heating coil wire | thm.heaterbench | 40 | 2 met-047, 1 pwr-001 | 3 thm-062 | — |
| wind heater elements | thm.heaterbench | 60 | 2 thm-062, 1 cer-002, 1 pwr-001 | 2 thm-004 | — |
| wind a heater element by hand | any.bench | 60 | 1 thm-062, 1 cer-035 | 1 thm-004 | — |
| strip a burnt-out heater | thm.heaterbench | 45 | 1 thm-013, 1 pwr-001 | 1 thm-062, 1 scr-004 | — |
| build a heater core | thm.heaterbench | 90 | 2 thm-004, 1 thm-008, 1 met-076, 1 pwr-001 | 1 thm-063 | — |
| wire a heater thermostat | any.bench | 45 | 1 lgt-008, 1 ecp-008 | 1 thm-064 | — |
| build a space heater | thm.heaterbench | 90 | 1 thm-004, 1 mec-009, 1 pol-045, 1 pwr-001 | 1 thm-009 | — |
| build a radiant panel heater | thm.heaterbench | 120 | 1 thm-063, 1 cer-009, 1 pwr-005, 1 pwr-001 | 1 thm-065 | — |
| build a convection heater | thm.heaterbench | 120 | 1 thm-063, 1 mec-009, 1 met-009, 1 pwr-001 | 1 thm-066 | — |
| lay a floor heating mat | thm.heaterbench | 120 | 2 thm-062, 1 pol-003, 1 pwr-005, 1 pwr-001 | 1 thm-067 | — |
| build a smart heater | thm.heaterbench | 150 | 1 thm-066, 1 thm-064, 1 ecp-007, 1 pwr-001 | 1 thm-068 | — |
| mould heating pad elements | thm.heaterbench | 60 | 1 thm-062, 1 pol-036, 1 pwr-001 | 2 thm-069 | — |
| build a life support heater element | thm.heaterbench | 60 | 2 thm-004, 1 met-005, 1 pwr-001 | 1 thm-070 | — |
| draw copper pipe blanks | thm.pipeforge | 60 | 2 met-053, 1 pwr-001 | 2 thm-043 | — |
| weave wick mesh | thm.pipeforge | 60 | 1 met-058, 1 pwr-001 | 2 thm-044 | — |
| sinter wicks | thm.pipeforge | 90 | 2 thm-044, 1 met-061, 1 pwr-001 | 2 thm-045 | — |
| charge heat pipes | thm.pipeforge | 60 | 2 thm-043, 1 thm-001, 1 pwr-001 | 2 thm-006 | — |
| crimp a crude heat pipe | any.bench | 90 | 1 met-053, 1 wat-003 | 1 thm-006 | — |
| seal heat pipes | thm.pipeforge | 90 | 2 thm-043, 1 thm-045, 1 thm-034, 1 pwr-001 | 2 thm-046 | — |
| loop a heat pipe | thm.pipeforge | 120 | 2 thm-046, 1 thm-006, 1 pwr-001 | 1 thm-047 | — |
| braze a flat heat spreader | thm.pipeforge | 90 | 1 met-037, 1 thm-045, 1 thm-008, 1 pwr-001 | 1 thm-048 | — |
| bundle heat pipes | thm.pipeforge | 150 | 3 thm-046, 1 thm-048, 1 pwr-001 | 1 thm-049 | — |
| roll fin stock | thm.pipeforge | 40 | 2 met-007, 1 pwr-001 | 3 thm-050 | — |
| stamp radiator fins | thm.pipeforge | 40 | 2 thm-050, 1 pwr-001 | 2 thm-051 | — |
| build a radiator panel | thm.exchangerbay | 90 | 4 thm-051, 1 thm-006, 1 pwr-001 | 1 thm-007 | — |
| rivet a crude radiator | any.bench | 120 | 2 met-007, 1 met-053 | 1 thm-007 | — |
| core a honeycomb radiator | thm.exchangerbay | 120 | 2 thm-007, 1 met-059, 1 pwr-001 | 1 thm-052 | — |
| build a deployable radiator wing | thm.exchangerbay | 150 | 2 thm-052, 1 thm-047, 1 mec-043, 1 pwr-001 | 1 thm-053 | — |
| build a louver panel | thm.exchangerbay | 90 | 2 thm-051, 1 mec-005, 1 pwr-001 | 1 thm-054 | — |
| stack a plate exchanger | thm.exchangerbay | 90 | 3 met-034, 1 pol-052, 1 pwr-001 | 1 thm-055 | — |
| tube a shell and tube exchanger | thm.exchangerbay | 120 | 1 thm-055, 2 thm-043, 1 pwr-001 | 1 thm-056 | — |
| build a heat exchanger | thm.exchangerbay | 90 | 2 thm-006, 1 thm-051, 1 pwr-001 | 1 thm-005 | — |
| plumb a plate exchanger | any.bench | 60 | 1 thm-055, 2 mec-013 | 1 thm-005 | — |
| build a cabin air exchanger | thm.exchangerbay | 150 | 1 thm-056, 1 mec-009, 1 pwr-001 | 1 thm-057 | — |
| wind a condensing coil | thm.exchangerbay | 90 | 2 thm-043, 1 thm-051, 1 pwr-001 | 1 thm-058 | — |
| build a liquid cooling plate | thm.exchangerbay | 90 | 1 thm-055, 1 thm-008, 1 pwr-001 | 1 thm-059 | — |
| assemble a cooling loop | thm.exchangerbay | 150 | 1 thm-039, 1 thm-047, 1 thm-059, 1 mec-008, 1 pwr-001 | 1 thm-060 | — |
| build a reactor heat exchanger | thm.exchangerbay | 180 | 1 thm-056, 1 thm-049, 2 thm-038, 1 pwr-001 | 1 thm-061 | — |
| build a life support fan coil | thm.exchangerbay | 90 | 1 mec-009, 1 thm-005, 1 pwr-001 | 1 thm-071 | — |
| build a life support coolant pump | thm.exchangerbay | 90 | 1 mec-008, 1 thm-001, 1 pwr-001 | 1 thm-072 | — |
| build a heat recovery unit | thm.exchangerbay | 180 | 1 thm-049, 1 thm-057, 1 pwr-001 | 1 thm-073 | — |
| build a waste heat loop | thm.exchangerbay | 150 | 1 thm-047, 1 thm-056, 1 pwr-001 | 1 thm-074 | — |
| build a solar heat collector | thm.exchangerbay | 120 | 1 thm-052, 1 cer-001, 1 thm-008, 1 pwr-001 | 1 thm-075 | — |
| lay a radiant floor loop | thm.exchangerbay | 150 | 1 thm-047, 1 thm-067, 1 pwr-001 | 1 thm-076 | — |
| build a habitat thermal core | thm.exchangerbay | 240 | 1 thm-074, 1 thm-068, 1 thm-022, 1 pwr-001 | 1 thm-077 | — |
| melt paraffin fill | thm.packfiller | 60 | 2 pol-067, 1 pwr-001 | 3 thm-078 | — |
| dissolve salt hydrate | thm.packfiller | 60 | 2 chm-060, 1 wat-001, 1 pwr-001 | 3 thm-079 | — |
| cook salt hydrate by hand | any.bench | 45 | 1 chm-029, 1 chm-012 | 1 thm-079 | — |
| mix iron powder charge | thm.packfiller | 30 | 2 met-060, 1 ing-002, 1 chm-005 | 4 thm-080 | — |
| seal heat pack casings | thm.packfiller | 30 | 1 pol-002, 1 pwr-001 | 4 thm-081 | — |
| fill instant heat packs | thm.packfiller | 30 | 1 thm-080, 1 thm-081, 1 pwr-001 | 2 thm-002 | — |
| bag an iron heat pack | any.bench | 30 | 1 met-060, 1 ing-002, 1 pak-029 | 1 thm-002 | — |
| fill a reusable heat pack | thm.packfiller | 60 | 1 thm-079, 1 thm-081, 1 pwr-001 | 1 thm-010 | — |
| recharge a spent heat pack | thm.packfiller | 45 | 1 thm-011, 1 pwr-001 | 1 thm-010 | — |
| boil a spent heat pack | any.bench | 30 | 1 thm-011, 1 wat-006 | 1 thm-010, 1 san-001 | — |
| fill a phase-change pack | thm.packfiller | 60 | 2 thm-078, 1 thm-081, 1 pwr-001 | 1 thm-082 | — |
| remelt a spent phase-change pack | thm.packfiller | 45 | 1 thm-083, 1 pwr-001 | 1 thm-082 | — |
| cast a phase-change wall tile | thm.packfiller | 90 | 3 thm-078, 1 cer-009, 1 pwr-001 | 1 thm-084 | — |
| build a thermal battery cell | thm.packfiller | 150 | 2 thm-079, 1 pwr-006, 1 thm-004, 1 pwr-001 | 1 thm-085 | — |
| fill hand warmers | thm.packfiller | 20 | 1 thm-080, 1 thm-081 | 2 thm-086 | — |
| fill a gel cold pack | thm.packfiller | 40 | 1 thm-001, 1 thm-081, 1 pwr-001 | 1 thm-087 | — |
| refreeze a gel pack | thm.packfiller | 30 | 1 thm-088, 1 pwr-001 | 1 thm-087 | — |
| forge a mixer paddle | any.bench | 60 | 1 met-034, 1 mec-006 | 1 thm-089 | — |
| wire a heater bench contactor | any.bench | 45 | 1 ecp-008, 1 met-006 | 1 thm-090 | — |
| grind a press platen | any.bench | 60 | 2 met-005 | 1 thm-091 | — |
| fit a pack fill nozzle | any.bench | 45 | 1 mec-049, 1 pol-008 | 1 thm-092 | — |
| cut a pipe forge die | any.bench | 90 | 1 met-030, 1 met-005 | 1 thm-093 | — |
| cut tube bundle gaskets | any.bench | 30 | 1 pol-052 | 2 thm-094 | — |
| crate a coolant mixer kit | any.bench | 120 | 1 fur-001, 1 thm-089, 1 mec-008 | 1 thm-095 | — |
| crate a heater bench kit | any.bench | 120 | 1 fur-001, 1 thm-090, 1 pwr-005 | 1 thm-096 | — |
| crate an insulation press kit | any.bench | 120 | 1 fur-001, 1 thm-091, 1 mec-043 | 1 thm-097 | — |
| crate a heat pack filler kit | any.bench | 120 | 1 fur-001, 1 thm-092, 1 mec-041 | 1 thm-098 | — |
| crate a heat pipe forge kit | any.bench | 120 | 1 fur-001, 1 thm-093, 1 thm-004 | 1 thm-099 | — |
| crate an exchanger bay kit | any.bench | 120 | 1 fur-001, 1 thm-094, 1 mec-040 | 1 thm-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| thm.coolantmixer | Mixes coolant from water, glycol, brine and slush, reclaims spent coolant, blends thermal paste and charges loop canisters for the grid. | PINK IS GLYCOL. BLUE IS AMMONIA. CLEAR IS A REPORTABLE INCIDENT. |
| thm.heaterbench | Draws coil wire and winds it into heater elements, cores and finished heaters, and strips burnt-out heaters. | Cabin heating is provisioned to the contractual minimum. Anything above is built here, at own cost. |
| thm.insulationpress | Spins rock wool and presses it, with aerogel and foil, into batts, panels, blankets, sleeves and film. | Platen alignment checked, rev 7. Wool in the bearings again. Cleared. |
| thm.packfiller | Fills heat packs, phase-change packs, cold packs, hand warmers and coolant cartridges, and recharges spent packs. | Heat packs are issued against a cold complaint. Cold complaints are issued against Form 80C. |
| thm.pipeforge | Draws copper pipe blanks, sinters wicks and seals them into heat pipes, spreaders, fin stock and radiator fins. | FORGE HOT. COPPER HOLDS HEAT LONGER THAN IT LOOKS. |
| thm.exchangerbay | Builds radiators, heat exchangers and cooling loops for life support and the grid. | Reactor waste heat is a Company asset. Its release into space is metered. Ref 9001/H. |
| thm-001 | Plain coolant for the cabin's loops, heat pipes and packs; the base of every coolant charge. | DO NOT DRINK. NOT EVEN WARM. |
| thm-002 | A single-use pack that releases a burst of warmth into the cabin when cracked. | Crack, shake, hold. Thermal comfort is not a contract term. |
| thm-003 | A wrapped batt of wool placed in life support that keeps the cabin warm until it crumbles. | Wall insulation is a station improvement. Improvements revert to the Company on transfer. |
| thm-004 | A wound heating element, the core part of every heater and several devices aboard. | Coil resistance measured, rev 2. Within band. Glows on test. |
| thm-005 | A heat exchanger fitted to life support that moves warmth between the air and the loops; wears into broken parts. | Swaps heat through a wall without contact. Standard procedure aboard. |
| thm-006 | A sealed tube that carries heat along its length, used in radiators, exchangers and loops. | HOT END MARKED RED. DO NOT GRIP. |
| thm-007 | A finned panel that sheds heat into space, cored into honeycomb radiators. | Mount facing away from the sun. Always. Proc 7 has no exceptions. |
| thm-008 | A conductive paste that bonds heaters and plates to what they warm or cool. | Apply a fingernail width. Not a thumb. Over-application is charged by the gram. |
| thm-009 | A small heater placed in life support that warms the cabin while it runs, until it burns out. | Do not dry garments on heater. Fire cost is deducted from the operator's account. |
| thm-010 | A salt hydrate pack that warms the cabin when clicked, and can be recharged. | Click, use, boil, click again. Cycle count not tracked. Wear is. |
| thm-011 | A crystallised heat pack, recharged in the filler or boiled for reuse. | Hard as rock and cold as a promise. Boil it. |
| thm-012 | Insulation crumbled with age, spun back into fluff by the insulation press. | Old walls, new fluff. Recycled content credited to the station. |
| thm-013 | A heater whose element has failed, stripped for coil wire and broken parts. | FAILED UNIT. TAG AND RETURN. DO NOT REPAIR IN PLACE. |
| thm-014 | Coolant gone dirty and tired in the loops, reclaimed by the coolant mixer. | Brown is not a coolant colour. Brown is a work order. Form 14B. |
| thm-015 | Loose wool spun from rock or slag, pressed into mats and blown into cavities. | Itches. Skin irritation is an accepted occupational condition. Ref 1500/W. |
| thm-016 | A pressed mat of rock wool, wrapped into batts or formed into sleeves. | Grey, scratchy, warm. Pick two. |
| thm-017 | A batt of glass wool placed in life support that keeps the cabin warm and outlasts rock wool. | GLASS FIBRE. GLOVES AND MASK. THEN A SECOND PAIR OF GLOVES. |
| thm-018 | A feather-light silica gel dried to foam, laid onto fibre as aerogel sheet. | Solid smoke. Fragile. Breakage is a write-off at operator cost. Notice 18/A. |
| thm-019 | Aerogel bonded to fibre, sewn into blankets and arctic sleeping bags. | Thin as paper, warm as a wall. Batch cut to template, rev 3. |
| thm-020 | A sewn aerogel blanket placed in life support that holds cabin heat in until it crumbles. | Lifts with one finger. Not to be lent. Not to be slept under. |
| thm-021 | A thin laminated foil, stacked into insulation and lined into curtains, film and survival sheets. | SHINY SIDE TOWARD HEAT SOURCE. |
| thm-022 | Many foil layers stacked over a batt, placed in life support to keep cabin heat in for a long time. | Twenty layers of almost nothing. Layer count audited, rev 1. |
| thm-023 | A pressed panel of batts and sandwich board that insulates a wall for a long time. | Fit once, forget for months. Inspection is scheduled anyway. Proc 23. |
| thm-024 | Blown fill that packs the wall cavities and keeps the cabin warm until it crumbles. | Fills gaps not on the drawings. The drawings are not to be amended. |
| thm-025 | A rock wool sleeve, taped into lagging for pipes. | Pipe jacket. Fitted, taped, forgotten. |
| thm-026 | Lagging placed around the cabin's pipes that stops them losing heat. | Uninsulated pipe is a heat loss. Heat loss is a cost. Cost is assigned. Ref 2600/L. |
| thm-027 | A film for viewports that keeps a little warmth in, until it peels into plastic scrap. | Stars unchanged through film. Feet marginally warmer. |
| thm-028 | A rubber strip that stops a cold draught at the door seam, until it wears into plastic scrap. | DO NOT OBSTRUCT DOOR SLOT. SEAL EDGE ONLY. |
| thm-029 | A rolled fabric excluder laid along a gap to keep cabin warmth in, until it wears into fabric scrap. | Every capsule names theirs. Naming of equipment is not approved. |
| thm-030 | A foil-faced panel that reflects cabin heat back in, until it wears into scrap metal. | Reflects heat. Also reflects the operator. Neither is improved. |
| thm-031 | A single-use foil sheet that holds warmth in during a cold emergency; leaves plastic scrap. | EMERGENCY USE. ONE PER OPERATOR. CRINKLES. NOT FOOD. |
| thm-032 | A foil-lined curtain that keeps the cabin warm and eases stress while it hangs. | Approved for cabin warmth. Psychological effects are incidental and unclaimed. |
| thm-033 | Crushed ice or frozen water, mixed into coolant before it melts back to raw water. | Use it or log it as a puddle. |
| thm-034 | Slush salted into a cold coolant, cut into cabin coolant or sealed into heat pipes. | Cold enough to sting, salty enough to stay liquid. Taste test discontinued, Proc 34. |
| thm-035 | Concentrated glycol for loop charges and heavy duty coolant. | TOXIC. SWEET SMELL. DO NOT TASTE. |
| thm-036 | A canister of glycol coolant charged into the grid's cooling loop through the hatch, steadying the grid. | Loop charges are credited to the grid, not the station. Thanks are not issued. |
| thm-037 | A canister of ammonia coolant that steadies the grid's cooling loop more strongly than glycol. | Open in the bay, not the bunk. Ammonia exposure is self-reported on Form 37A. |
| thm-038 | A thickened coolant for reservoir cartridges, cryogenic coolant and reactor exchangers. | Heavy drum. Lift with the legs. Back injury is not a covered condition. |
| thm-039 | Coolant chilled with liquid nitrogen, for cooling loops and shield coils. | CRYOGENIC. GLOVES. VISOR. NO EXCEPTIONS. |
| thm-040 | A flushing fluid that clears the grid's cooling loop of sludge. | Flush quarterly per Plant Maintenance Proc 40. Quarters are approximate. |
| thm-041 | A coolant reservoir cartridge fitted to life support that empties into a canister when used up. | Swap before the fans get loud. Loud fans are logged as a station fault. |
| thm-042 | A small cartridge of coolant that tops up the grid's cooling loop; leaves an empty canister. | Cartridge filled, sealed, weighed, rev 1. Weight within a few grams. |
| thm-043 | A drawn copper tube cut to length, made into heat pipes, exchangers and coils. | Copper is controlled stock. Offcuts are returned and weighed. Ref 4300/C. |
| thm-044 | A fine copper mesh, sintered into the wicks that line heat pipes. | Woven finer than the patience of the weaver. |
| thm-045 | A sintered wick that carries fluid back along a heat pipe. | DO NOT BEND. WICK DAMAGE IS NOT VISIBLE. |
| thm-046 | A wicked and sealed heat pipe, looped or bundled into larger heat movers. | Seal pressure tested, rev 2. Holds. Probably for longer than the contract. |
| thm-047 | A looped heat pipe for radiator wings, cooling loops, floor loops and waste heat loops. | Goes round and comes round. So does every work order. |
| thm-048 | A flat plate that spreads heat evenly, bundled with heat pipes. | Makes every hot spot everyone's hot spot. |
| thm-049 | A bundle of sealed heat pipes for heat recovery units and reactor exchangers. | Many pipes, one direction. Direction stencilled on casing. |
| thm-050 | Rolled aluminium stock, stamped into radiator fins. | SHARP EDGES. HANDLE WITH CUT GLOVES. |
| thm-051 | A stamped fin that sheds heat, built into radiators, exchangers and coils. | Bent fins reduce rejection by a measured amount. The amount is deducted. |
| thm-052 | A radiator cored with honeycomb, built into radiator wings and solar heat collectors. | Core bonded, rev 3. One cell crushed. Accepted as cosmetic. |
| thm-053 | A radiator wing fitted outside through the hatch that takes a large heat load off the power grid. | EXTERNAL DEPLOYMENT. HULL CREW ONLY. TETHER AT ALL TIMES. |
| thm-054 | A louvered radiator fitted through the hatch that opens and shuts to keep the grid's heat in balance. | Opens and shuts on its own schedule. Do not override. Notice 54/L. |
| thm-055 | A stack of plates that passes heat between two fluids; the start of most exchangers. | Hot side, cold side, thin steel between. Stamped which is which. Mostly. |
| thm-056 | A shell and tube exchanger for cabin air, waste heat and reactor exchangers. | Tubes inside a tube. Tube count verified on drawing 56, not in person. |
| thm-057 | A cabin air exchanger fitted to life support that warms incoming air with outgoing heat. | Exhaust air leaves its heat behind. It is not permitted to take it. |
| thm-058 | A cooling coil fitted to the moisture condenser that wrings water out of the cabin air. | Coil fins combed straight, rev 4. Condensate yield nominal. |
| thm-059 | A cold plate that pulls heat off electronics, built into cooling loops and computers. | COOLANT LINES PRESSURISED. ISOLATE BEFORE DISCONNECTION. |
| thm-060 | A complete cooling loop fitted to the grid through the hatch, steadying it greatly. | Primary plant cooling. Failure is not survivable. Install per Proc 60, all steps. |
| thm-061 | A large exchanger fitted through the hatch that carries reactor heat off the grid. | Between the crew and a very bad day. The Company has insured the ship. |
| thm-062 | Resistance wire drawn for heater elements, heating pads and floor mats. | Spool weight logged on issue and on return. Difference is explained. |
| thm-063 | A heater core of elements and a heat sink, built into panel and convection heaters. | All the warmth, none of the casing. Do not power uncased. |
| thm-064 | A thermostat that cuts a heater off at temperature, built into thermostatic heaters. | Factory set. Tamper seal fitted. Setpoint is not an operator decision. |
| thm-065 | A flat panel heater placed in life support that warms the cabin by radiating from the wall, until it burns out. | Warms bodies, not air. Stand in front during approved breaks. |
| thm-066 | A fan heater placed in life support that warms the cabin by moving warm air, until it burns out. | Hums, blows, warms. Fan bearing noise is within spec. Ref 6600/H. |
| thm-067 | A heated mat laid under the floor that warms the cabin from below, until it burns out. | UNDERFLOOR HEATING. DO NOT DRILL FLOOR. |
| thm-068 | A thermostat-controlled heater that warms the cabin well and wastes little, until it burns out. | Stops at setpoint. The setpoint is the Company's. Notice 68/T. |
| thm-069 | A small moulded heating element wired into heated blankets. | Low wattage. Moulded, tested, rev 1. Do not fold while live. |
| thm-070 | A heater element fitted to life support that keeps the cabin air warm, until it burns out. | When this fails, the operator knows before the alarm does. Log it anyway. |
| thm-071 | A fan coil fitted to life support that pushes warmed air through the cabin; wears into a burnt-out motor. | Noticed only when it stops. Stopping is a priority work order. |
| thm-072 | A coolant pump fitted to life support that circulates the cabin's coolant loop; wears into worn pump parts. | Impeller checked, rev 5. Cavitation noise noted. Not addressed. |
| thm-073 | A unit placed in life support that recovers heat from exhaust air and returns it to the cabin. | Nothing leaves the capsule without paying a heat toll. Toll is policy, Ref 7300/R. |
| thm-074 | A loop placed in life support that brings waste heat from machinery into the cabin. | Machinery heat reassigned to cabin heating. No cost saving is passed on. |
| thm-075 | A collector placed in life support that turns sunlight into cabin warmth. | Free heat. Cheap heat. Heat. Output depends on attitude. The ship's. |
| thm-076 | A loop laid under the floor that warms the cabin from below. | Warm floor, all shifts. Footwear remains mandatory. Proc 76. |
| thm-077 | A complete thermal core placed in life support that heats a capsule better than any other unit. | TOP GRADE CABIN HEATING. ISSUE BY ALLOCATION ONLY. |
| thm-078 | Melted paraffin, cast into phase-change packs and wall tiles. | Smells of candles. Open flame is prohibited aboard. Candles are prohibited aboard. |
| thm-079 | A salt hydrate solution for reusable heat packs and thermal battery cells. | Liquid until clicked. Clicking for amusement is wear. Ref 7900/S. |
| thm-080 | A mix of iron powder and salt that heats when exposed to air, for heat packs and hand warmers. | Rust, but useful. Keep sealed until required. |
| thm-081 | A sealed casing that heat packs, cold packs and hand warmers are filled into. | EMPTY CASING. FILL AT PACK FILLER ONLY. |
| thm-082 | A paraffin pack that releases a strong burst of warmth as it sets; remelted for reuse. | Melts in the filler, gives it back in the bunk. Recharge cycle logged. |
| thm-083 | A set phase-change pack or tile, remelted into a fresh pack by the filler. | Solid now. Return for remelt. Do not discard. |
| thm-084 | A paraffin wall tile that absorbs heat and releases it slowly, until it sets spent. | Wall tile, thermal. Fitted per Habitat Spec 84. Do not paint. |
| thm-085 | A cell of salt hydrate and a heater that stores warmth and releases it slowly into the cabin. | Charge at shift start. Draws grid power. Draw is metered. |
| thm-086 | A small single-use hand warmer that warms the hands and eases stress; leaves plastic scrap. | Hold during the conversations that cannot be had. |
| thm-087 | A chilled gel pack that eases pain once and comes off warm. | Ten minutes on, ten off. Injury report first. Proc 87 applies. |
| thm-088 | A gel pack warmed by use, refrozen in the filler for reuse. | Return for refreeze. Do not leave in bunk. |
| thm-089 | A replacement paddle fitted to the coolant mixer; wears into scrap metal. | Paddle welds inspected, rev 3. Bent slightly. Within tolerance. |
| thm-090 | A replacement contactor fitted to the heater bench that switches its power; wears into electronic scrap. | Click on, click off. When it stops clicking, swap it and log it. |
| thm-091 | A replacement platen fitted to the insulation press; wears into scrap metal. | HEAVY PART. TWO PERSONNEL. LIFTING POINTS MARKED. |
| thm-092 | A replacement fill nozzle fitted to the heat pack filler; wears into broken parts. | Wipe after every shift or it seals itself shut. Re-drilling is chargeable. |
| thm-093 | A replacement die fitted to the heat pipe forge; wears into scrap metal. | Die wear measured each run. Measurements kept. Nobody reads them. |
| thm-094 | A replacement gasket fitted to the exchanger bay that seals its tube bundles; wears into plastic scrap. | Small ring. Large leak if missing. Leak cost calculated on Form 94G. |
| thm-095 | A packed coolant mixer, ready to install. | COF THERMAL EQUIPMENT. UNPACK AT INSTALL SITE. |
| thm-096 | A packed heater bench, ready to install. | Recommended first build for cold stations. Recommendation does not imply supply. |
| thm-097 | A packed insulation press, ready to install. | Crate opened, platen intact, manual absent. Absence noted, rev 1. |
| thm-098 | A packed heat pack filler, ready to install. | Small kit. Dispatched under Thermal Order 98. Delivery not tracked. |
| thm-099 | A packed heat pipe forge, ready to install. | HEAVY. HOT IN SERVICE. BOLT TO DECK BEFORE FIRST USE. |
| thm-100 | A packed exchanger bay, ready to install. | Large footprint. Floor space is allocated, not requested. Ref 1000/X. |
