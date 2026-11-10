# Air & Gases — `gas`

The cabin's breath. Oxygen and hydrogen are split from feedwater; carbon dioxide caught by the scrubbers and hydrogen
are run through the Sabatier reactor into methane and water, or pyrolysed into syngas, acetylene and carbon; frosts and
volatile ices from `ore` are sublimed and separated into nitrogen, argon, helium, xenon and the rest, or liquefied.
Gases are blended into breathing mixes and compressed into canisters, reserve tanks and dewars, and chlorate and
superoxide are pressed into oxygen candles. All of it is used at life support for `cabin.o2` and `cabin.pressure`;
canisters leave an empty canister, candles a burnt casing. Bulk gases and canisters go on to the drive, the foundry,
the hull's fire and leak gear, the fuel cells, the drinks that fizz and the medbay.

## Devices

| id | device | role | cells |
|---|---|---|---|
| gas.electrolyser | AT100 Water Electrolyser | atmos | 2x2 |
| gas.sabatier | AT220 Sabatier Reactor | atmos | 2x2 |
| gas.sublimator | AT310 Volatiles Sublimator | atmos | 2x1 |
| gas.separator | AT400 Gas Separator | atmos | 2x2 |
| gas.blender | AT150 Gas Blender | atmos | 2x1 |
| gas.compressor | AT520 Canister Compressor | atmos | 2x1 |
| gas.candlepress | AT60 Oxygen Candle Press | atmos | 2x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| gas-001 | Oxygen | cabin.o2 +5 | — |
| gas-002 | Carbon Dioxide | — | — |
| gas-003 | Nitrogen | cabin.pressure +10 | — |
| gas-004 | Hydrogen | — | — |
| gas-005 | Canister, Oxygen | cabin.o2 +15, leaves 1 pak-006 | — |
| gas-006 | Canister, Nitrogen | cabin.pressure +15, leaves 1 pak-006 | — |
| gas-007 | Mix, Breathing | cabin.o2 +4, cabin.pressure +6 | — |
| gas-008 | Canister, Breathing Mix | cabin.o2 +12, cabin.pressure +12, leaves 1 pak-006 | — |
| gas-009 | Candle, Oxygen, Chlorate | cabin.o2 +12, cabin.heat +2, leaves 1 gas-056 | — |
| gas-010 | Methane | — | — |
| gas-011 | Canister, Carbon Dioxide | — | — |
| gas-012 | Canister, Hydrogen | — | — |
| gas-013 | Canister, Methane | — | — |
| gas-014 | Argon | — | — |
| gas-015 | Helium | — | — |
| gas-016 | Canister, Argon | — | — |
| gas-017 | Canister, Helium | — | — |
| gas-018 | Gas, Volatile, Raw | — | — |
| gas-019 | Mix, Sabatier Feed | — | — |
| gas-020 | Syngas | — | — |
| gas-021 | Carbon Monoxide | — | — |
| gas-022 | Acetylene | — | — |
| gas-023 | Canister, Acetylene | — | — |
| gas-024 | Carbon, Pyrolysis | — | — |
| gas-025 | Xenon | — | — |
| gas-026 | Canister, Xenon | — | — |
| gas-027 | Oxygen, Liquid | — | 72 h → gas-001 |
| gas-028 | Nitrogen, Liquid | — | 72 h → gas-003 |
| gas-029 | Methane, Liquid | — | 120 h → gas-010 |
| gas-030 | Mix, Heliox | cabin.o2 +4, cabin.pressure +6 | — |
| gas-031 | Mix, Oxygen Rich | cabin.o2 +8, cabin.pressure +3 | — |
| gas-032 | Mix, Nitrogen Rich | cabin.o2 +2, cabin.pressure +9 | — |
| gas-033 | Canister, Heliox | cabin.o2 +10, cabin.pressure +12, leaves 1 pak-006 | — |
| gas-034 | Canister, Repressurisation | cabin.pressure +25, cabin.o2 +5, leaves 1 pak-006 | — |
| gas-035 | Oxygen, Medical | — | — |
| gas-036 | Canister, Oxygen, Medical | health +5, stress -3, leaves 1 pak-006 | — |
| gas-037 | Canister, Nitrous Oxide | pain -20, stress -5, fun +3, leaves 1 pak-006 | — |
| gas-038 | Canister, Leak Tracer | — | — |
| gas-039 | Gas, Inert | — | — |
| gas-040 | Canister, Inert Gas | — | — |
| gas-041 | Gas, Shielding | — | — |
| gas-042 | Canister, Shielding Gas | — | — |
| gas-043 | Cartridge, Carbonation | — | — |
| gas-044 | Canister, Oxygen, Trickle | cabin.o2 +1/h | 24 h → pak-006 |
| gas-045 | Canister, Nitrogen, Trickle | cabin.pressure +1/h | 24 h → pak-006 |
| gas-046 | Tank, Reserve, Oxygen | cabin.o2 +2/h | 48 h → gas-047 |
| gas-047 | Tank, Reserve, Empty | — | — |
| gas-048 | Tank, Reserve, Pressure | cabin.pressure +2/h | 48 h → gas-047 |
| gas-049 | Dewar, Liquid Oxygen | cabin.o2 +3/h | 72 h → gas-050 |
| gas-050 | Dewar, Empty | — | — |
| gas-051 | Mix, Candle, Chlorate | — | — |
| gas-052 | Powder, Candle Fuel | — | — |
| gas-053 | Cap, Igniter, Candle | — | — |
| gas-054 | Candle, Oxygen, Large | cabin.o2 +25, cabin.heat +4, leaves 1 gas-056 | — |
| gas-055 | Candle, Oxygen, Slow Burn | cabin.o2 +1/h, cabin.heat +1/h | 12 h → gas-056 |
| gas-056 | Casing, Candle, Burnt | — | — |
| gas-057 | Pellets, Superoxide | — | — |
| gas-058 | Canister, Superoxide | cabin.o2 +10, cabin.co2 -8, leaves 1 gas-059 | — |
| gas-059 | Canister, Superoxide, Spent | — | — |
| gas-060 | Ozone | — | 2 h → gas-001 |
| gas-061 | Neon | — | — |
| gas-062 | Krypton | — | — |
| gas-063 | Deuterium | — | — |
| gas-064 | Dregs, Sublimator | — | — |
| gas-065 | Canister, Oxygen Bar | cabin.o2 +2, stress -5, fun +3, leaves 1 pak-006 | — |
| gas-066 | Balloon, Helium | stress -1/h | 120 h → scr-002 |
| gas-067 | Cartridge, Hydrogen, Fuel Cell | ship.grid +3, leaves 1 pak-024, leaves 1 wat-018 | — |
| gas-068 | Tank, Reserve, Breathing Mix | cabin.o2 +1/h, cabin.pressure +1/h | 48 h → gas-047 |
| gas-069 | Air, Compressed | — | — |
| gas-070 | Canister, Neon | — | — |
| gas-071 | Canister, Calibration Gas | — | — |
| gas-072 | Pellets, Catalyst, Sabatier | fits gas.sabatier | 720 h → gas-073 |
| gas-073 | Catalyst, Sabatier, Spent | — | — |
| gas-074 | Membrane, Water Electrolyser | fits gas.electrolyser | 1000 h → scr-002 |
| gas-075 | Electrodes, Water Electrolyser | fits gas.electrolyser | — |
| gas-076 | Heater, Sabatier Reactor | fits gas.sabatier | — |
| gas-077 | Water Trap, Sabatier Reactor | fits gas.sabatier | — |
| gas-078 | Hotplate, Volatiles Sublimator | fits gas.sublimator | — |
| gas-079 | Cold Trap, Volatiles Sublimator | fits gas.sublimator | — |
| gas-080 | Head, Cold, Gas Separator | fits gas.separator | — |
| gas-081 | Valve, Expansion, Gas Separator | fits gas.separator | — |
| gas-082 | Valve, Mixing, Gas Blender | fits gas.blender | — |
| gas-083 | Meter, Flow, Gas Blender | fits gas.blender | — |
| gas-084 | Piston Set, Canister Compressor | fits gas.compressor | — |
| gas-085 | Valve, Canister Fill | fits gas.compressor | — |
| gas-086 | Gauge, Pressure, Canister | fits gas.compressor | — |
| gas-087 | Mould, Oxygen Candle Press | fits gas.candlepress | — |
| gas-088 | Ram, Oxygen Candle Press | fits gas.candlepress | — |
| gas-089 | Regulator, Oxygen | fits any.lifesupport | — |
| gas-090 | Valve, Pressure Relief | fits any.lifesupport | — |
| gas-091 | Manifold, Gas, Life Support | fits any.lifesupport | — |
| gas-092 | Hose, Gas, Life Support | fits any.lifesupport | — |
| gas-093 | Valve, Check, Life Support | fits any.lifesupport | — |
| gas-094 | Kit, Water Electrolyser | installs gas.electrolyser | — |
| gas-095 | Kit, Sabatier Reactor | installs gas.sabatier | — |
| gas-096 | Kit, Volatiles Sublimator | installs gas.sublimator | — |
| gas-097 | Kit, Gas Separator | installs gas.separator | — |
| gas-098 | Kit, Gas Blender | installs gas.blender | — |
| gas-099 | Kit, Canister Compressor | installs gas.compressor | — |
| gas-100 | Kit, Oxygen Candle Press | installs gas.candlepress | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| bottle algae oxygen | any.algaejar | 360 | 1 wat-002 | 1 gas-001 | — |
| draw off cabin carbon dioxide | any.lifesupport | 120 | 1 pwr-001 | 1 gas-002 | cabin.co2 -2 |
| split feedwater | gas.electrolyser | 60 | 2 wat-040, 2 pwr-001 | 2 gas-001, 2 gas-004 | — |
| split drinking water | gas.electrolyser | 90 | 3 wat-001, 3 pwr-001 | 2 gas-001, 2 gas-004 | — |
| split heavy water | gas.electrolyser | 120 | 1 wat-038, 2 pwr-001 | 1 gas-063, 1 gas-001 | — |
| make ozone | gas.electrolyser | 30 | 2 gas-001, 1 pwr-001 | 1 gas-060 | — |
| run a sabatier batch | gas.sabatier | 120 | 1 gas-019, 1 pwr-001 | 1 gas-010, 2 wat-019 | — |
| reform syngas | gas.sabatier | 90 | 1 gas-020, 2 gas-004, 1 pwr-001 | 1 gas-010, 1 wat-019 | — |
| pyrolyse methane | gas.sabatier | 120 | 2 gas-010, 2 pwr-001 | 1 gas-022, 1 gas-024, 2 gas-004 | — |
| reduce carbon dioxide to carbon | gas.sabatier | 180 | 1 gas-002, 2 gas-004, 2 pwr-001 | 1 gas-024, 2 wat-019 | — |
| regenerate sabatier catalyst | gas.sabatier | 120 | 2 gas-073, 1 gas-004, 1 pwr-001 | 1 gas-072 | — |
| sublime dry ice | gas.sublimator | 30 | 2 ore-036, 1 pwr-001 | 2 gas-002 | — |
| sublime nitrogen frost | gas.sublimator | 45 | 2 ore-038, 1 pwr-001 | 3 gas-003 | — |
| sublime argon frost | gas.sublimator | 45 | 2 ore-044, 1 pwr-001 | 2 gas-014 | — |
| sublime xenon frost | gas.sublimator | 60 | 2 ore-045, 1 pwr-001 | 1 gas-025 | — |
| sublime methane ice | gas.sublimator | 45 | 2 ore-040, 1 pwr-001 | 2 gas-010 | — |
| sublime carbon monoxide ice | gas.sublimator | 45 | 2 ore-041, 1 pwr-001 | 2 gas-021 | — |
| sublime hydrogen slush | gas.sublimator | 30 | 2 ore-046, 1 pwr-001 | 3 gas-004 | — |
| outgas comet dust | gas.sublimator | 120 | 3 ore-035, 2 pwr-001 | 2 gas-018, 1 gas-064 | — |
| bake sublimator dregs | gas.sublimator | 60 | 3 gas-064, 1 pwr-001 | 2 ore-051 | — |
| separate volatile gas | gas.separator | 120 | 3 gas-018, 2 pwr-001 | 1 gas-003, 1 gas-002, 1 gas-014, 1 gas-015 | — |
| separate trace noble gases | gas.separator | 180 | 4 gas-018, 3 pwr-001 | 1 gas-061, 1 gas-062, 1 gas-025, 2 gas-003 | — |
| separate oxygen frost | gas.separator | 60 | 2 ore-037, 1 pwr-001 | 3 gas-001 | — |
| separate biogas | gas.separator | 90 | 2 san-008, 1 pwr-001 | 1 gas-010, 1 gas-002 | — |
| liquefy oxygen | gas.separator | 90 | 3 gas-001, 2 pwr-001 | 2 gas-027 | — |
| liquefy nitrogen | gas.separator | 90 | 3 gas-003, 2 pwr-001 | 2 gas-028 | — |
| liquefy methane | gas.separator | 90 | 3 gas-010, 2 pwr-001 | 2 gas-029 | — |
| blend breathing mix | gas.blender | 30 | 1 gas-001, 2 gas-003, 1 pwr-001 | 2 gas-007 | — |
| blend heliox | gas.blender | 30 | 1 gas-001, 1 gas-015, 1 pwr-001 | 2 gas-030 | — |
| blend oxygen rich mix | gas.blender | 30 | 2 gas-001, 1 gas-003, 1 pwr-001 | 2 gas-031 | — |
| blend nitrogen rich mix | gas.blender | 30 | 1 gas-001, 3 gas-003, 1 pwr-001 | 3 gas-032 | — |
| purify medical oxygen | gas.blender | 45 | 3 gas-001, 1 pwr-001 | 2 gas-035 | — |
| blend inert gas | gas.blender | 30 | 2 gas-014, 1 gas-003, 1 pwr-001 | 3 gas-039 | — |
| blend krypton into inert gas | gas.blender | 30 | 1 gas-062, 1 gas-014, 1 pwr-001 | 2 gas-039 | — |
| blend shielding gas | gas.blender | 30 | 2 gas-014, 1 gas-002, 1 pwr-001 | 3 gas-041 | — |
| blend sabatier feed | gas.blender | 20 | 1 gas-002, 2 gas-004, 1 pwr-001 | 1 gas-019 | — |
| blend syngas | gas.blender | 20 | 1 gas-021, 1 gas-004, 1 pwr-001 | 1 gas-020 | — |
| blend calibration gas | gas.blender | 30 | 1 gas-070, 1 gas-001, 1 gas-003 | 1 gas-071 | — |
| compress shop air | gas.compressor | 30 | 1 gas-001, 2 gas-003, 1 fil-033, 1 pwr-001 | 3 gas-069, 1 fil-034 | — |
| fill an oxygen canister | gas.compressor | 30 | 3 gas-001, 1 pak-005, 1 pwr-001 | 1 gas-005 | — |
| fill an oxygen canister from liquid | gas.compressor | 20 | 2 gas-027, 1 pak-005 | 1 gas-005 | — |
| fill a nitrogen canister | gas.compressor | 30 | 2 gas-003, 1 pak-005, 1 pwr-001 | 1 gas-006 | — |
| fill a breathing mix canister | gas.compressor | 30 | 3 gas-007, 1 pak-005, 1 pwr-001 | 1 gas-008 | — |
| fill a carbon dioxide canister | gas.compressor | 30 | 3 gas-002, 1 pak-005, 1 pwr-001 | 1 gas-011 | — |
| fill a hydrogen canister | gas.compressor | 30 | 3 gas-004, 1 pak-005, 1 pwr-001 | 1 gas-012 | — |
| fill a methane canister | gas.compressor | 30 | 3 gas-010, 1 pak-005, 1 pwr-001 | 1 gas-013 | — |
| fill an argon canister | gas.compressor | 30 | 2 gas-014, 1 pak-005, 1 pwr-001 | 1 gas-016 | — |
| fill a helium canister | gas.compressor | 30 | 2 gas-015, 1 pak-005, 1 pwr-001 | 1 gas-017 | — |
| fill an acetylene canister | gas.compressor | 30 | 2 gas-022, 1 pak-005, 1 pwr-001 | 1 gas-023 | — |
| fill a xenon canister | gas.compressor | 30 | 2 gas-025, 1 pak-005, 1 pwr-001 | 1 gas-026 | — |
| fill a neon canister | gas.compressor | 30 | 2 gas-061, 1 pak-005, 1 pwr-001 | 1 gas-070 | — |
| fill a heliox canister | gas.compressor | 30 | 3 gas-030, 1 pak-005, 1 pwr-001 | 1 gas-033 | — |
| fill a repressurisation canister | gas.compressor | 45 | 2 gas-032, 2 gas-003, 1 pak-005, 1 pwr-001 | 1 gas-034 | — |
| fill a medical oxygen canister | gas.compressor | 30 | 2 gas-035, 1 pak-005, 1 pwr-001 | 1 gas-036 | — |
| fill a nitrous oxide canister | gas.compressor | 30 | 2 prp-033, 1 pak-005, 1 pwr-001 | 1 gas-037 | — |
| fill a leak tracer canister | gas.compressor | 20 | 1 gas-015, 1 gas-003, 1 pak-005 | 1 gas-038 | — |
| fill an inert gas canister | gas.compressor | 30 | 3 gas-039, 1 pak-005, 1 pwr-001 | 1 gas-040 | — |
| fill a shielding gas canister | gas.compressor | 30 | 3 gas-041, 1 pak-005, 1 pwr-001 | 1 gas-042 | — |
| fill an oxygen bar canister | gas.compressor | 20 | 2 gas-001, 1 veg-072, 1 pak-005 | 1 gas-065 | — |
| fill a trickle oxygen canister | gas.compressor | 20 | 2 gas-001, 1 pak-005 | 1 gas-044 | — |
| fill a trickle nitrogen canister | gas.compressor | 20 | 2 gas-003, 1 pak-005 | 1 gas-045 | — |
| decant carbonation cartridges | gas.compressor | 20 | 1 gas-011 | 4 gas-043, 1 pak-006 | — |
| decant fuel cell cartridges | gas.compressor | 20 | 1 gas-012, 2 pak-023 | 2 gas-067, 1 pak-006 | — |
| charge an oxygen reserve tank | gas.compressor | 60 | 8 gas-001, 1 gas-047, 2 pwr-001 | 1 gas-046 | — |
| charge a pressure reserve tank | gas.compressor | 60 | 6 gas-003, 1 gas-047, 2 pwr-001 | 1 gas-048 | — |
| charge a breathing mix reserve tank | gas.compressor | 60 | 6 gas-007, 1 gas-047, 2 pwr-001 | 1 gas-068 | — |
| fill a liquid oxygen dewar | gas.compressor | 30 | 3 gas-027, 1 gas-050 | 1 gas-049 | — |
| mix chlorate candle mix | gas.candlepress | 30 | 2 chm-038, 1 pwr-001 | 3 gas-051 | — |
| grind candle fuel powder | gas.candlepress | 30 | 1 met-060, 1 pwr-001 | 2 gas-052 | — |
| make candle igniter caps | gas.candlepress | 20 | 1 met-039, 1 chm-023 | 4 gas-053 | — |
| press oxygen candles | gas.candlepress | 45 | 2 gas-051, 1 gas-052, 2 gas-053, 1 met-043, 1 pwr-001 | 2 gas-009 | — |
| press a large oxygen candle | gas.candlepress | 60 | 4 gas-051, 2 gas-052, 1 gas-053, 1 met-043, 1 pwr-001 | 1 gas-054 | — |
| press a slow oxygen candle | gas.candlepress | 60 | 2 gas-051, 1 gas-052, 1 gas-053, 1 met-043, 1 pwr-001 | 1 gas-055 | — |
| press superoxide pellets | gas.candlepress | 45 | 2 chm-015, 1 gas-001, 2 pwr-001 | 2 gas-057 | — |
| pack a superoxide canister | gas.candlepress | 30 | 3 gas-057, 1 pak-005 | 1 gas-058 | — |
| empty a spent superoxide canister | gas.candlepress | 20 | 1 gas-059 | 1 pak-006, 1 chm-015 | — |
| strip burnt candle casings | any.bench | 15 | 2 gas-056 | 1 scr-001 | — |
| calibrate life support sensors | any.lifesupport | 15 | 1 gas-071 | 1 pak-006 | cabin.o2 +2, cabin.co2 -2 |
| purge a smouldering duct | any.lifesupport | 10 | 1 gas-040 | 1 pak-006 | cabin.clean +4, cabin.pressure +4 |
| bleed argon into the cabin | any.lifesupport | 10 | 1 gas-016 | 1 pak-006 | cabin.pressure +6 |
| trace a cabin leak | crew | 30 | 1 gas-038 | 1 pak-006 | cabin.pressure +4 |
| blow dust out of the vents | crew | 15 | 1 gas-069 | — | cabin.clean +3 |
| fill helium balloons | crew | 10 | 1 gas-017, 1 pol-002 | 4 gas-066, 1 pak-006 | — |
| weld a hull seam with acetylene | any.bench | 60 | 1 gas-023, 1 met-078, 1 pwr-001 | 1 pak-006 | ship.hull +3 |
| weld a hull plate under shielding gas | any.bench | 60 | 1 gas-042, 1 met-078, 1 pwr-001 | 1 pak-006 | ship.hull +3 |
| feed xenon to the drive | any.hatch | 30 | 1 gas-026 | 1 pak-006 | ship.thrust +3 |
| feed methane to the drive | any.hatch | 30 | 1 gas-013 | 1 pak-006 | ship.thrust +3 |
| feed deuterium to the reactor | any.hatch | 30 | 2 gas-063 | — | ship.grid +4 |
| build a reserve tank | any.bench | 90 | 1 pak-055, 1 mec-007 | 1 gas-047 | — |
| build a dewar | any.bench | 90 | 1 met-034, 1 cer-057 | 1 gas-050 | — |
| make sabatier catalyst pellets | any.bench | 60 | 1 chm-078, 1 chm-077 | 2 gas-072 | — |
| make an electrolyser cell membrane | any.bench | 60 | 1 pol-032 | 1 gas-074 | — |
| make an electrolyser electrode stack | any.bench | 90 | 1 met-014, 1 met-035 | 1 gas-075 | — |
| make a sabatier reactor heater | any.bench | 60 | 1 thm-004, 1 met-056 | 1 gas-076 | — |
| make a sabatier water trap | any.bench | 60 | 1 thm-058, 1 met-056 | 1 gas-077 | — |
| make a sublimator heater plate | any.bench | 60 | 1 met-005, 1 thm-004 | 1 gas-078 | — |
| make a sublimator cold trap | any.bench | 60 | 1 met-053, 1 thm-058 | 1 gas-079 | — |
| make a separator cold head | any.bench | 90 | 1 mec-042, 1 thm-005 | 1 gas-080 | — |
| make a separator expansion valve | any.bench | 45 | 1 mec-035, 1 met-049 | 1 gas-081 | — |
| make a blender mixing valve | any.bench | 45 | 1 mec-034, 1 met-073 | 1 gas-082 | — |
| make a blender flow meter | any.bench | 45 | 1 lgt-046, 1 met-053 | 1 gas-083 | — |
| make a compressor piston set | any.bench | 90 | 1 met-008, 1 pol-009, 1 mec-026 | 1 gas-084 | — |
| make a canister fill valve | any.bench | 30 | 1 pak-046, 1 mec-007 | 1 gas-085 | — |
| make a canister pressure gauge | any.bench | 30 | 1 lgt-009, 1 met-075 | 1 gas-086 | — |
| make a candle press mould | any.bench | 60 | 1 met-005 | 1 gas-087 | — |
| make a candle press ram | any.bench | 60 | 1 met-008, 1 mec-043 | 1 gas-088 | — |
| make an oxygen regulator | any.bench | 45 | 1 mec-035, 1 lgt-050 | 1 gas-089 | — |
| make a pressure relief valve | any.bench | 30 | 1 mec-036, 1 pol-009 | 1 gas-090 | — |
| make a life support gas manifold | any.bench | 60 | 1 met-075, 2 mec-007 | 1 gas-091 | — |
| make a life support gas hose | any.bench | 20 | 1 pol-039, 1 mec-014 | 1 gas-092 | — |
| make a life support check valve | any.bench | 30 | 1 mec-033, 1 pol-009 | 1 gas-093 | — |
| pack a water electrolyser kit | any.bench | 120 | 1 fur-001, 1 gas-074, 1 gas-075, 1 ecp-010 | 1 gas-094 | — |
| pack a sabatier reactor kit | any.bench | 120 | 1 fur-001, 1 gas-072, 1 gas-076, 1 gas-077 | 1 gas-095 | — |
| pack a volatiles sublimator kit | any.bench | 120 | 1 fur-001, 1 gas-078, 1 gas-079 | 1 gas-096 | — |
| pack a gas separator kit | any.bench | 120 | 1 fur-001, 1 gas-080, 1 gas-081, 1 fil-070 | 1 gas-097 | — |
| pack a gas blender kit | any.bench | 120 | 1 fur-001, 1 gas-082, 1 gas-083 | 1 gas-098 | — |
| pack a canister compressor kit | any.bench | 120 | 1 fur-001, 1 gas-084, 1 gas-085, 1 gas-086 | 1 gas-099 | — |
| pack an oxygen candle press kit | any.bench | 120 | 1 fur-001, 1 gas-087, 1 gas-088 | 1 gas-100 | — |
| shock the cabin air with ozone | crew | 10 | 1 gas-060 | 1 gas-001 | cabin.clean +5, toxin +2 |

## Codex

| id | about | flavour |
|---|---|---|
| gas.electrolyser | Splits feedwater or drinking water into oxygen and hydrogen, heavy water into deuterium, and charges oxygen into ozone. | Breathable air is supplied under the operating contract. Its cost is deducted under the same. Ref 1001/O. |
| gas.sabatier | Turns carbon dioxide and hydrogen into methane and water, cracks methane, reduces carbon dioxide to carbon, and regenerates its catalyst. | HOT SURFACES. FLAMMABLE GAS. NO OPEN FLAME WITHIN 2 M. |
| gas.sublimator | Warms frosts and volatile ices into gas, outgases comet dust, and bakes the dregs. | Ice goes in silent and comes out hissing. Do not put an ear to it. |
| gas.separator | Splits volatile gas into its parts, separates biogas and oxygen frost, and liquefies oxygen, nitrogen and methane. | Cold head serviced, rev 11. Frost on the casing is normal. Frost on the operator is not. |
| gas.blender | Blends breathing mixes, inert, shielding, feed and calibration gases, and purifies medical oxygen. | Mix ratios are set by Atmospherics Spec 150. Operator adjustment is logged and reviewed. |
| gas.compressor | Fills canisters and cartridges, charges reserve tanks, fills dewars and compresses shop air. | HIGH PRESSURE. INSPECT CANISTER BEFORE FILL. STAND CLEAR OF VALVE. |
| gas.candlepress | Presses oxygen candles and superoxide pellets, packs superoxide canisters, and mixes candle fuel and igniter caps. | Emergency oxygen is a Company courtesy. Use outside an emergency is billed. Notice 60/E. |
| gas-001 | Bulk oxygen for the cabin's air; it also feeds furnaces, chemistry and every breathing mix. | Air quota per operator per shift is fixed. Exertion beyond quota is at own expense. Ref 0001/A. |
| gas-002 | Carbon dioxide drawn from the cabin, ferments and ices; feed for the methane reactor and canisters. | Exhaled gas remains Company property and is recovered accordingly. |
| gas-003 | Bulk nitrogen that holds the cabin's pressure up; also used in mixes and safety gear. | Most of the air. None of the credit. |
| gas-004 | Hydrogen split from water, for the methane reactor, fuel cells and chemistry. | FLAMMABLE. LEAKS THROUGH FITTINGS. CHECK SEALS EACH SHIFT. |
| gas-005 | Compressed oxygen released into the cabin; leaves an empty canister. | Keep one by the bunk. Inventory says no. Keep one anyway. |
| gas-006 | Compressed nitrogen to raise cabin pressure, or to charge extinguishers and air bags; leaves an empty canister. | Pressure on demand. Demand is monitored. Ref 0606/N. |
| gas-007 | Oxygen and nitrogen blended like cabin air; raises both oxygen and pressure. | Tastes of nothing. Nothing is the specification. |
| gas-008 | Compressed breathing mix; raises oxygen and pressure and leaves an empty canister. | AIR. COMPRESSED. COF ATMOSPHERICS DIVISION. |
| gas-009 | A chlorate candle that burns to release oxygen and some heat; leaves a burnt casing. | Pull cap. Step back. Do not hold while burning. Proc 9 applies. |
| gas-010 | Methane from the reactor, ices and biogas; for the drive, plastics and chemistry. | Fuel from exhaled breath. Operators are reminded they are part of the supply chain. |
| gas-011 | Compressed carbon dioxide, decanted into carbonation cartridges or used in extinguishers. | Canister tested, rev 4. Stencil worn. Contents confirmed by smell. Not recommended. |
| gas-012 | Compressed hydrogen for fuel cell cartridges and propellant. | NO SPARKS. NO EXCEPTIONS. NO REPLACEMENT CAPSULE. |
| gas-013 | Compressed methane, fed to the drive through a hatch. | Propellant contributions are credited to the ship, not the station. Ref 1300/T. |
| gas-014 | Argon from frost and volatiles, for shielding and inert gas, lamps and atomising metal. | Does nothing. That is the job. |
| gas-015 | Helium from volatiles, for heliox, leak tracing, liquefying and balloons. | Rationed gas. Voice alteration is not an authorised use. Notice 15/H. |
| gas-016 | Compressed argon, bled into the cabin to raise pressure. | INERT. ASPHYXIANT IN QUANTITY. BLEED SLOWLY. |
| gas-017 | Compressed helium for filling balloons. | Recreational issue, one per quarter. Second canister requires Form 17R. |
| gas-018 | Mixed gas outgassed from comet dust, separated into its parts. | A bit of everything. None of it useful until sorted. |
| gas-019 | Carbon dioxide and hydrogen blended to feed the methane reactor. | FEED GAS. NOT BREATHABLE. REACTOR USE ONLY. |
| gas-020 | Carbon monoxide and hydrogen; reformed into methane, or refined into oils and methanol. | Toxic and flammable at once. Efficient, in its way. |
| gas-021 | A toxic gas sublimed from ice, blended into syngas or used in chemistry. | NO SMELL. NO COLOUR. DETECTOR MUST BE ARMED. |
| gas-022 | Gas cracked from methane, filled into canisters for welding. | Hottest flame aboard. Burns per shift are reported on Form 22W. |
| gas-023 | Compressed acetylene for welding hull seams. | Valve cap fitted, rev 2. Store upright. Previous canister did not. |
| gas-024 | Carbon left from cracking methane or reducing carbon dioxide; pressed into filter carbon. | Soot that cleans the air. Recovered, weighed and credited. Ref 2400/C. |
| gas-025 | Rare xenon from frost and volatiles; drive propellant and lamp fill. | Accounted by the gram. Discrepancies by the milligram. |
| gas-026 | Compressed xenon, fed to the drive through a hatch. | HIGH VALUE CARGO. TAMPER SEAL MUST BE INTACT. |
| gas-027 | Oxygen liquefied for dense storage and dewars; it boils back to gas if kept. | Pale blue and in a hurry to leave. Boil-off losses are charged to the station. |
| gas-028 | Nitrogen liquefied for cryogenic coolant and densifying fuel; it boils back to gas if kept. | CRYOGENIC. GLOVES AND VISOR. NO BARE SKIN. |
| gas-029 | Methane liquefied for propellant; it boils back to gas if kept. | Fuel at its most compact and least patient. |
| gas-030 | Oxygen and helium blended for breathing; raises oxygen and pressure. | Speech distortion while breathing heliox is not grounds for a report. Ref 3000/X. |
| gas-031 | A breathing mix heavy on oxygen, to freshen a stale cabin. | Head clears. Fire risk rises. Both are noted. |
| gas-032 | A breathing mix heavy on nitrogen, mostly for pressure. | For a cabin that feels thin. Approved per Atmos Proc 32. |
| gas-033 | Compressed heliox; raises oxygen and pressure and leaves an empty canister. | Canister hydro tested, rev 6. Stamp in date. Barely. |
| gas-034 | A large charge of gas to refill a leaking cabin, mostly pressure; leaves an empty canister. | USE AFTER LEAK IS SEALED. NOT BEFORE. READ THIS TWICE. |
| gas-035 | Purified oxygen for medical canisters. | Cleaner than cabin air. Cabin air meets standard. Ref 3500/M. |
| gas-036 | Pure oxygen breathed to restore health and ease stress; leaves an empty canister. | Medical issue only. Breathing it for comfort is a misuse of medical stock. Notice 36/M. |
| gas-037 | Nitrous oxide breathed to kill pain, ease stress and lift morale; leaves an empty canister. | Analgesic. Laughter is a side effect and is not to be recorded as morale. |
| gas-038 | Helium and nitrogen tracer gas for finding cabin leaks. | Where it hisses, it leaks. Where it does not, check again. |
| gas-039 | Argon blended with nitrogen or krypton, for purging fires. | Smothers fire. Also smothers personnel. Evacuate before discharge. |
| gas-040 | Inert gas released at life support to purge a smouldering duct; leaves an empty canister. | FIRE SUPPRESSION. BREAK SEAL ONLY ON ALARM. |
| gas-041 | Argon and carbon dioxide blended for welding. | Keeps the weld clean. Welder's lungs are a separate matter. |
| gas-042 | Shielding gas for welding hull plates; leaves an empty canister. | Hull welding is a certified task. Certificate held by the station, not the operator. |
| gas-043 | A small carbon dioxide cartridge for sparkling water and sparkling wine. | Single use. Refill attempts void the cartridge and the eyebrows. |
| gas-044 | A canister that bleeds oxygen slowly into the cabin until it is empty. | Valve set to trickle, rev 3. Set and forget. Do not forget. |
| gas-045 | A canister that bleeds nitrogen slowly into the cabin until it is empty. | SLOW RELEASE. DO NOT OPEN VALVE FURTHER. |
| gas-046 | A large tank that feeds oxygen steadily until it runs empty. | Reserve air bridges gaps in supply. Gaps in supply are not acknowledged. |
| gas-047 | An empty reserve tank, recharged with oxygen, nitrogen or breathing mix. | Hollow, heavy and waiting. Return for recharge, Form 47T. |
| gas-048 | A large tank that feeds nitrogen steadily to hold cabin pressure. | Holds the cabin up, quietly. Pressure loss is the station's to explain. |
| gas-049 | A dewar of liquid oxygen that feeds the cabin steadily as it boils off. | VENTED CONTAINER. DO NOT SEAL. DO NOT LAY FLAT. |
| gas-050 | An insulated empty dewar, refilled with liquid oxygen. | Cold even when empty. Vacuum jacket checked, rev 8. |
| gas-051 | Sodium chlorate mix, the oxygen source of a candle. | OXIDISER. KEEP FROM FUEL POWDER UNTIL PRESSING. |
| gas-052 | Iron powder that burns to drive an oxygen candle. | Keep dry, keep apart, keep counted. Proc 52. |
| gas-053 | A cap that lights an oxygen candle. | Strike once. Firmly. Second strikes are logged as faults. |
| gas-054 | A large oxygen candle that releases more oxygen and heat; leaves a burnt casing. | Issued for major atmosphere loss. Minor loss does not qualify. Ref 5400/O. |
| gas-055 | A candle that gives oxygen and heat slowly, burning down to a casing. | Lasts the watch. The watch lasts longer. |
| gas-056 | The spent shell of an oxygen candle, stripped for scrap metal. | HOT AFTER USE. RETURN TO SCRAP. DEPOSIT NOT REFUNDED. |
| gas-057 | Pellets that release oxygen and take up carbon dioxide, packed into canisters. | Reacts with moisture. Including the moisture in hands. |
| gas-058 | Releases oxygen and scrubs carbon dioxide from the cabin; leaves a spent canister. | Two functions, one canister, one charge. Efficiency noted by Procurement. |
| gas-059 | A used superoxide canister, emptied back into a canister and hydroxide. | CAUSTIC RESIDUE. EMPTY AT CANDLE PRESS ONLY. |
| gas-060 | Oxygen charged into ozone to shock the cabin air clean; it fades back to oxygen. | Smells of a thunderstorm. No operator present has seen one. |
| gas-061 | Neon from trace noble gases, filled into canisters for calibration gas. | Trace yield. Every litre is accounted against the separator's quota. |
| gas-062 | Krypton from trace noble gases, blended into inert gas. | Rare, heavy, inert. An ideal employee. |
| gas-063 | Heavy hydrogen split from heavy water, fed to the reactor through a hatch. | REACTOR FEED. CONTROLLED ISOTOPE. SIGN FOR EACH UNIT. |
| gas-064 | Grit left from outgassing comet dust, baked into regolith fines. | Comet dust, back to plain dust. Swept, bagged, weighed. |
| gas-065 | Mint-scented oxygen breathed for recreation and calm; leaves an empty canister. | Scented air is a recreational product and is not counted toward air quota. |
| gas-066 | A balloon that floats in the cabin easing stress, until it sags into plastic scrap. | Tied to the bunk until it gives up. Everything here does. |
| gas-067 | A hydrogen cartridge run in the fuel cells for grid power; leaves its cartridge and water. | Power with water as a byproduct. Both metered. Ref 6700/P. |
| gas-068 | A large tank that feeds breathing mix steadily, for both oxygen and pressure. | Regulator set, rev 5. Steady output. Steady is the most that is promised. |
| gas-069 | Dried, compressed shop air for blowing dust out of vents, or bottled for thrust. | POINT AWAY FROM FACE. POINT AWAY FROM PERSONNEL. |
| gas-070 | Compressed neon, blended into calibration gas. | Low demand item. Stocked per Inventory Directive 70 regardless. |
| gas-071 | A known gas mix for calibrating life support's sensors. | Calibrate monthly. Uncalibrated readings are the operator's responsibility. |
| gas-072 | The Sabatier reactor's catalyst bed; it wears out into spent catalyst and is regenerated. | Nickel does the work. The Company takes the credit. Standard arrangement. |
| gas-073 | Worn catalyst, regenerated with hydrogen in the Sabatier reactor. | Spent, not scrapped. Regeneration is mandatory, Proc 73. |
| gas-074 | A replacement cell membrane fitted to the water electrolyser; wears into plastic scrap. | Thin as paper. Handle by the edges. Fingerprints shorten service life. |
| gas-075 | A replacement electrode stack fitted to the water electrolyser. | Stack torqued to spec, rev 4. Corrosion on plate 3. Within tolerance. |
| gas-076 | A replacement heater fitted to the Sabatier reactor. | HEATING ELEMENT. ISOLATE POWER BEFORE REMOVAL. |
| gas-077 | A replacement water trap fitted to the Sabatier reactor. | Trap drained, seal replaced, rev 2. Drained water reclaimed. Every drop counts. |
| gas-078 | A replacement heater plate fitted to the volatiles sublimator. | Warm enough to wake the ice. Not enough to warm the operator. |
| gas-079 | A replacement cold trap fitted to the volatiles sublimator. | Replacement parts are issued against a failed part. No failed part, no issue. Ref 7900. |
| gas-080 | A replacement cold head fitted to the gas separator. | COLDEST POINT ON STATION. DO NOT TOUCH. DO NOT LICK. |
| gas-081 | A replacement expansion valve fitted to the gas separator. | Valve seat lapped, rev 3. Hiss reduced. Not eliminated. |
| gas-082 | A replacement mixing valve fitted to the gas blender. | Proportion is everything. Deviation is a breathing problem. |
| gas-083 | A replacement flow meter fitted to the gas blender. | Meter readings are the official record. Operator perception is not. |
| gas-084 | A replacement piston set fitted to the canister compressor. | Thump, thump, hiss. If the hiss comes first, call it in. |
| gas-085 | A replacement canister fill valve fitted to the canister compressor. | ONE WAY VALVE. ARROW SHOWS FLOW. |
| gas-086 | A replacement canister pressure gauge fitted to the canister compressor. | Needle in the green. Glass cracked, rev 1. Needle still in the green. |
| gas-087 | A replacement mould fitted to the oxygen candle press. | Mould dimensions per Emergency Supply Spec 87. Do not modify. |
| gas-088 | A replacement ram fitted to the oxygen candle press. | PINCH POINT. KEEP HANDS CLEAR DURING STROKE. |
| gas-089 | A replacement oxygen regulator fitted to life support. | Too much is as bad as too little. The regulator decides which. |
| gas-090 | A replacement pressure relief valve fitted to life support. | Lets go so the cabin does not. Tested on install, rev 1. |
| gas-091 | A replacement gas manifold fitted to life support. | Every breath passes through here. Every breath is metered here. |
| gas-092 | A replacement gas hose fitted to life support. | Check the clamps. Then check them again. Then log the check. |
| gas-093 | A replacement check valve fitted to life support. | ONE WAY ONLY. FLOW ARROW TOWARD CABIN. |
| gas-094 | A packed water electrolyser, ready to install. | Life support equipment. Priority installation, at the station's own time. |
| gas-095 | A packed Sabatier reactor, ready to install. | Crate seal intact, catalyst sealed, rev 1. Assembly instructions in another crate. |
| gas-096 | A packed volatiles sublimator, ready to install. | COF ATMOSPHERICS. THIS WAY UP. SERIAL ON LID. |
| gas-097 | A packed gas separator, ready to install. | Supplied under Atmospherics Order 97. Supply does not imply priority. |
| gas-098 | A packed gas blender, ready to install. | Unpacked, checked, one hose short. Hose borrowed from elsewhere. Do not ask where. |
| gas-099 | A packed canister compressor, ready to install. | PRESSURE EQUIPMENT. INSTALL ON BOLTED FOOTING ONLY. |
| gas-100 | A packed oxygen candle press, ready to install. | Emergency oxygen production is delegated to stations. Liability is delegated with it. |
