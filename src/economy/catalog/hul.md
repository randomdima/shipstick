# Hull, Repair & Safety — `hul`

Everything that keeps the skin on and the crew alive when it fails. Metal sheet is pressed into skins, stringers and
plates, riveted and welded into braces, frames and whole hull sections, sealed with gaskets, putty and tape, and glazed
into viewports; the large parts are slow, take many subsections' goods, and raise `ship.hull` at the service hatch.
Beside them sits the emergency gear: extinguishers, fire blankets, masks, oxygen canisters and candles, breach plugs and
patches that keep the crew's health and the cabin's air and pressure through a fire or a breach, and the repair drones
that mend the hull while they last. Spent canisters go back to Stores; worn drones and detectors go to salvage.

## Devices

| id | device | role | cells |
|---|---|---|---|
| hul.pressbrake | HR400 Press Brake | fab | 3x2 |
| hul.welder | HR520 Welding Jig | fab | 2x2 |
| hul.molder | HR310 Seal Molder | fab | 2x2 |
| hul.glazer | HR270 Glazing Bench | fab | 2x1 |
| hul.safetybench | HR100 Safety Gear Bench | fab | 2x1 |
| hul.dronebay | HR900 Repair Drone Bay | fab | 3x2 |

## Items

| id | item | use | decays |
|---|---|---|---|
| hul-001 | Plate, Hull | ship.hull +10 | — |
| hul-002 | Sheet, Hull Patch | ship.hull +2 | — |
| hul-003 | Cartridge, Hull Sealant | ship.hull +2, cabin.pressure +2, leaves 1 pak-024 | 720 h → scr-002 |
| hul-004 | Kit, Breach Patch | ship.hull +3, cabin.pressure +8 | — |
| hul-005 | Extinguisher, Fire | health +4, stress -5, leaves 1 pak-006 | — |
| hul-006 | Canister, Oxygen, Emergency | cabin.o2 +20, leaves 1 pak-006 | — |
| hul-007 | Rivet, Hull | — | — |
| hul-008 | Rod, Hull Weld | — | — |
| hul-009 | Blank, Skin | — | — |
| hul-010 | Gasket, Hull Door | — | — |
| hul-011 | Brace, Hull | ship.hull +6 | — |
| hul-012 | Stringer, Hull | — | — |
| hul-013 | Ring, Hull Frame | — | — |
| hul-014 | Strip, Blind Rivet | — | — |
| hul-015 | Panel, Skin, Riveted | ship.hull +8 | — |
| hul-016 | Plate, Bumper | — | — |
| hul-017 | Layer, Whipple | ship.hull +6, ship.shield +1 | — |
| hul-018 | Shield, Whipple, Double | ship.hull +12, ship.shield +3 | — |
| hul-019 | Block, Foam Filler, Hull | — | — |
| hul-020 | Panel, Hull, Foam Filled | ship.hull +5 | — |
| hul-021 | Patch, Hull, Adhesive | ship.hull +2 | 720 h → scr-002 |
| hul-022 | Plug, Pressure, Emergency | cabin.pressure +5 | — |
| hul-023 | Patch, Self Sealing | ship.hull +3, cabin.pressure +3 | — |
| hul-024 | Tape, Hull | ship.hull +1, cabin.pressure +1 | — |
| hul-025 | Putty Stick, Hull | — | — |
| hul-026 | Sealer, Epoxy Seam | ship.hull +2, cabin.pressure +2, leaves 1 pak-012 | 720 h → scr-002 |
| hul-027 | Tape, Pressure Seal | cabin.pressure +2 | — |
| hul-028 | Blank, Hull Gasket | — | — |
| hul-029 | Strip, Window Seal | — | — |
| hul-030 | Ring, Port Seal | — | — |
| hul-031 | Frame, Hull Window | — | — |
| hul-032 | Glass, Viewport | — | — |
| hul-033 | Viewport, Glazed | cabin.light +3/h | 2000 h → hul-035 |
| hul-034 | Window, Radiation | cabin.light +2/h, dose -1/h | 2000 h → hul-035 |
| hul-035 | Viewport, Crazed | — | — |
| hul-036 | Hinge Pair, Hatch | — | — |
| hul-037 | Ring, Hatch Latch | — | — |
| hul-038 | Leaf, Hatch Door | — | — |
| hul-039 | Wheel, Hatch | — | — |
| hul-040 | Kit, Hatch Rebuild | fits any.hatch | 2000 h → scr-004 |
| hul-041 | Handle, Dogging | fits any.hatch | 3000 h → scr-001 |
| hul-042 | Set, Airlock Seal | fits any.hatch | 1500 h → scr-074 |
| hul-043 | Brace, Hull Corner | — | — |
| hul-044 | Brace, Truss, Assembled | ship.hull +8 | — |
| hul-045 | Section, Hull Frame | ship.hull +12 | — |
| hul-046 | Plate, Pressure Bulkhead | ship.hull +8, cabin.pressure +3 | — |
| hul-047 | Section, Bulkhead | ship.hull +14 | — |
| hul-048 | Beam, Hull Keel | ship.hull +15 | — |
| hul-049 | Segment, Hull | ship.hull +18 | — |
| hul-050 | Unit, Hull Section | ship.hull +30 | — |
| hul-051 | Plate, Hull Doubler | ship.hull +6 | — |
| hul-052 | Liner, Hull Spall | ship.hull +5 | — |
| hul-053 | Stopper, Crack | ship.hull +1 | — |
| hul-054 | Strap, Crack Arrest | ship.hull +4 | — |
| hul-055 | Brace, Hull, Titanium | ship.hull +10 | — |
| hul-056 | Paste, Welding Flux | — | — |
| hul-057 | Cartridge, Hull Coating | ship.hull +4, leaves 1 pak-024 | 720 h → scr-002 |
| hul-058 | Kit, Repair Drone Bay | installs hul.dronebay | — |
| hul-059 | Foam, Suppressant | — | — |
| hul-060 | Powder, Dry Chemical | — | — |
| hul-061 | Extinguisher, Foam | health +5, stress -6, leaves 1 pak-006 | — |
| hul-062 | Extinguisher, Dry Powder | health +4, stress -5, toxin +2, leaves 1 pak-006 | — |
| hul-063 | Blanket, Fire | health +5, stress -4, leaves 1 scr-005 | — |
| hul-064 | Cloth, Fire, Glass Fibre | — | — |
| hul-065 | Detector, Smoke, Cabin | stress -1/h | 2000 h → scr-003 |
| hul-066 | Alarm, Gas Leak, Cabin | stress -1/h | 2000 h → scr-003 |
| hul-067 | Alarm, Pressure Loss | stress -1/h | 2000 h → scr-003 |
| hul-068 | Sprinkler, Fire Suppression | stress -2/h | 1500 h → scr-004 |
| hul-069 | Mask, Emergency | toxin -8, leaves 1 hul-071 | — |
| hul-070 | Hood, Escape | toxin -12, health +2, leaves 1 scr-002 | — |
| hul-071 | Cartridge, Mask, Spent | — | — |
| hul-072 | Cartridge, Mask Filter | — | — |
| hul-073 | Candle, Oxygen | cabin.o2 +15, cabin.heat +2, leaves 1 gas-056 | — |
| hul-074 | Bag, Air, Emergency | cabin.pressure +10, leaves 1 scr-002 | — |
| hul-075 | Plug, Breach, Inflatable | cabin.pressure +12, ship.hull +1 | — |
| hul-076 | Plate, Breach | ship.hull +5, cabin.pressure +10 | — |
| hul-077 | Kit, Breach, Rapid | ship.hull +6, cabin.pressure +15 | — |
| hul-078 | Spray, Leak Tracer | cabin.pressure +2, leaves 1 pak-022 | — |
| hul-079 | Harness, Safety | stress -1/h | 1500 h → scr-005 |
| hul-080 | Pouch, Shelter, Emergency | cabin.o2 +10, cabin.heat +6, cabin.pressure +6, leaves 1 scr-002 | — |
| hul-081 | Bag, Grab, Emergency | cabin.o2 +10, toxin -6, stress -5, leaves 1 scr-005 | — |
| hul-082 | Chassis, Crawler | — | — |
| hul-083 | Wheel, Crawler, Magnetic | — | — |
| hul-084 | Arm, Drone Repair | — | — |
| hul-085 | Crawler, Hull | ship.hull +1/h | 600 h → scr-003 |
| hul-086 | Walker, Hull | ship.hull +2/h | 800 h → scr-003 |
| hul-087 | Drone, Hull Inspection | ship.hull +1/h | 600 h → scr-003 |
| hul-088 | Bot, Welding Arm | ship.hull +3/h | 600 h → scr-003 |
| hul-089 | Drone, Leak Sniffer | ship.hull +1/h, cabin.pressure +1/h | 600 h → scr-003 |
| hul-090 | Die, Press Brake | fits hul.pressbrake | 800 h → scr-001 |
| hul-091 | Tip, Electrode, Welding Jig | fits hul.welder | 400 h → scr-001 |
| hul-092 | Insert, Seal Mould | fits hul.molder | 800 h → scr-001 |
| hul-093 | Wheel, Glazing | fits hul.glazer | 500 h → scr-004 |
| hul-094 | Head, Extinguisher Fill | fits hul.safetybench | 800 h → scr-004 |
| hul-095 | Rail, Gantry, Repair Drone Bay | fits hul.dronebay | 1500 h → scr-004 |
| hul-096 | Kit, Press Brake | installs hul.pressbrake | — |
| hul-097 | Kit, Welding Jig | installs hul.welder | — |
| hul-098 | Kit, Seal Molder | installs hul.molder | — |
| hul-099 | Kit, Glazing Bench | installs hul.glazer | — |
| hul-100 | Kit, Safety Gear Bench | installs hul.safetybench | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| press a hull plate | hul.pressbrake | 120 | 2 met-005, 1 cer-009, 2 hul-007, 1 pwr-001 | 1 hul-001 | — |
| press a titanium hull plate | hul.pressbrake | 150 | 1 met-035, 2 hul-009, 2 hul-007, 1 pwr-001 | 1 hul-001 | — |
| rivet scrap plate into a hull plate | any.bench | 240 | 3 scr-063, 4 hul-007, 1 met-078 | 1 hul-001 | — |
| cut hull patch sheets | hul.pressbrake | 40 | 1 met-009, 1 pol-010, 1 pwr-001 | 3 hul-002 | — |
| tape a scrap patch sheet | any.bench | 60 | 1 scr-063, 1 pol-056, 1 hul-056 | 1 hul-002 | — |
| fill a sealant cartridge | hul.molder | 45 | 1 pol-004, 1 chm-027, 1 pak-023, 1 pwr-001 | 1 hul-003 | — |
| bag a breach patch kit | hul.molder | 60 | 2 hul-021, 1 hul-022, 1 hul-003, 1 pak-029 | 1 hul-004 | — |
| pack a breach patch kit | hul.safetybench | 60 | 2 hul-002, 1 pol-058, 1 hul-024, 1 pak-029 | 1 hul-004 | — |
| fill a fire extinguisher | hul.safetybench | 60 | 2 hul-060, 1 pak-005, 1 gas-003, 1 pwr-001 | 1 hul-005 | — |
| valve a carbon dioxide extinguisher | any.bench | 30 | 1 gas-011, 1 pak-046 | 1 hul-005 | — |
| fill an emergency oxygen canister | hul.safetybench | 40 | 2 gas-001, 1 pak-005, 1 pak-046, 1 pwr-001 | 1 hul-006 | — |
| fit a quick valve to an oxygen canister | any.bench | 20 | 1 gas-005, 1 pak-046 | 1 hul-006 | — |
| head hull rivets | hul.pressbrake | 20 | 1 met-068, 1 pwr-001 | 8 hul-007 | — |
| cut hull rivets from scrap rod | any.bench | 40 | 1 scr-062 | 4 hul-007 | — |
| coat hull weld rods | hul.welder | 30 | 1 met-078, 1 hul-056, 1 pwr-001 | 4 hul-008 | — |
| press skin blanks | hul.pressbrake | 45 | 1 met-007, 1 pwr-001 | 3 hul-009 | — |
| flatten scrap plate into skin blanks | hul.pressbrake | 60 | 2 scr-063, 1 pwr-001 | 2 hul-009 | — |
| cut hull door gaskets | hul.molder | 30 | 1 pol-052, 1 pwr-001 | 2 hul-010 | — |
| cut a gasket from rubber sheet | any.bench | 40 | 1 pol-003 | 1 hul-010 | — |
| weld a hull brace | hul.welder | 90 | 2 met-008, 2 hul-008, 1 pwr-001 | 1 hul-011 | — |
| press hull stringers | hul.pressbrake | 60 | 1 met-042, 1 hul-009, 1 pwr-001 | 2 hul-012 | — |
| roll a hull frame ring | hul.pressbrake | 90 | 2 hul-012, 1 hul-009, 4 hul-007, 1 pwr-001 | 1 hul-013 | — |
| load blind rivet strips | hul.pressbrake | 20 | 4 mec-019, 1 met-042, 1 pwr-001 | 2 hul-014 | — |
| rivet a skin panel | hul.pressbrake | 90 | 2 hul-009, 2 hul-014, 1 hul-012, 1 pwr-001 | 1 hul-015 | — |
| press a bumper plate | hul.pressbrake | 60 | 1 met-007, 1 met-059, 1 pwr-001 | 1 hul-016 | — |
| layer a whipple shield | hul.pressbrake | 150 | 2 hul-016, 1 fib-066, 1 pwr-001 | 1 hul-017 | — |
| stack a double whipple shield | hul.pressbrake | 180 | 2 hul-017, 1 cer-057, 1 hul-011, 1 pwr-001 | 1 hul-018 | — |
| foam filler blocks | hul.molder | 60 | 1 pol-027, 1 pwr-001 | 2 hul-019 | — |
| bond a foam filled panel | hul.molder | 90 | 1 hul-019, 1 cer-065, 2 hul-009, 1 pol-010, 1 pwr-001 | 1 hul-020 | — |
| glue adhesive hull patches | hul.molder | 40 | 1 hul-002, 1 pol-010, 1 pwr-001 | 2 hul-021 | — |
| mould emergency pressure plugs | hul.molder | 30 | 1 pol-003, 1 pol-051, 1 pwr-001 | 3 hul-022 | — |
| stuff a plug from offcuts | any.bench | 30 | 1 pol-085, 1 scr-020 | 1 hul-022 | — |
| mould self sealing patches | hul.molder | 45 | 1 pol-003, 1 pol-059, 1 hul-002, 1 pwr-001 | 2 hul-023 | — |
| laminate hull tape | hul.molder | 20 | 1 pol-056, 1 met-039, 1 pwr-001 | 4 hul-024 | — |
| roll hull putty sticks | hul.molder | 30 | 1 pol-059, 1 ore-051, 1 pwr-001 | 3 hul-025 | — |
| tube an epoxy seam sealer | hul.molder | 40 | 2 hul-025, 1 pol-024, 1 pak-011, 1 pwr-001 | 1 hul-026 | — |
| slit pressure seal tape | hul.molder | 20 | 1 pol-056, 1 pwr-001 | 3 hul-027 | — |
| wrap insulating tape as seal tape | any.bench | 20 | 1 pol-063 | 1 hul-027 | — |
| mould gasket blanks | hul.molder | 30 | 1 pol-022, 1 pwr-001 | 3 hul-028 | — |
| mould gasket blanks from rubber crumb | hul.molder | 30 | 2 scr-075, 1 pwr-001 | 2 hul-028 | — |
| cut window seal strips | hul.molder | 25 | 1 hul-028, 1 pol-004, 1 pwr-001 | 3 hul-029 | — |
| mould port seal rings | hul.molder | 30 | 1 hul-028, 1 pol-076, 1 pwr-001 | 2 hul-030 | — |
| weld a hull window frame | hul.welder | 60 | 1 met-049, 1 hul-008, 1 pwr-001 | 1 hul-031 | — |
| laminate viewport glass | hul.glazer | 120 | 1 cer-017, 1 pol-033, 1 pwr-001 | 1 hul-032 | — |
| glaze a viewport | hul.glazer | 120 | 1 hul-032, 1 hul-031, 1 hul-029, 1 pwr-001 | 1 hul-033 | — |
| glaze a radiation window | hul.glazer | 180 | 1 hul-032, 1 cer-015, 1 hul-031, 1 hul-030, 1 pwr-001 | 1 hul-034 | — |
| reglaze a crazed viewport | hul.glazer | 90 | 1 hul-035, 1 hul-032, 1 hul-029, 1 pwr-001 | 1 hul-033, 1 scr-017 | — |
| strip a crazed viewport | any.bench | 30 | 1 hul-035 | 1 hul-031, 1 scr-017 | — |
| weld hatch hinge pairs | hul.welder | 60 | 2 met-008, 2 mec-004, 1 pol-006, 1 pwr-001 | 2 hul-036 | — |
| weld a hatch latch ring | hul.welder | 60 | 1 hul-036, 1 mec-046, 1 met-049, 1 pwr-001 | 1 hul-037 | — |
| press a hatch door leaf | hul.pressbrake | 120 | 1 hul-013, 1 hul-009, 1 hul-010, 1 pwr-001 | 1 hul-038 | — |
| weld a hatch wheel | hul.welder | 60 | 1 met-008, 1 mec-006, 1 pwr-001 | 1 hul-039 | — |
| build a hatch rebuild kit | hul.welder | 150 | 1 hul-038, 1 hul-037, 1 hul-010, 1 pwr-001 | 1 hul-040 | — |
| weld a dogging handle | hul.welder | 60 | 1 hul-039, 1 mec-005, 2 hul-007, 1 pwr-001 | 1 hul-041 | — |
| mould an airlock seal set | hul.molder | 60 | 2 hul-010, 1 hul-030, 1 pol-076, 1 pwr-001 | 1 hul-042 | — |
| weld hull corner braces | hul.welder | 60 | 1 cer-081, 1 met-008, 1 hul-008, 1 pwr-001 | 2 hul-043 | — |
| weld a truss brace assembly | hul.welder | 120 | 2 hul-043, 1 hul-011, 1 cer-080, 1 pwr-001 | 1 hul-044 | — |
| weld a hull frame section | hul.welder | 180 | 2 hul-043, 1 hul-013, 2 hul-012, 1 pwr-001 | 1 hul-045 | — |
| press a pressure bulkhead plate | hul.pressbrake | 120 | 1 hul-001, 1 cer-075, 1 hul-010, 1 pwr-001 | 1 hul-046 | — |
| weld a bulkhead section | hul.welder | 200 | 1 hul-046, 2 hul-043, 1 cer-078, 1 pwr-001 | 1 hul-047 | — |
| weld a hull keel beam | hul.welder | 240 | 1 cer-079, 2 hul-044, 1 hul-013, 1 pwr-001 | 1 hul-048 | — |
| join a hull segment | hul.welder | 300 | 1 hul-045, 1 hul-015, 1 hul-020, 2 pwr-001 | 1 hul-049 | — |
| join a hull section unit | hul.welder | 480 | 1 hul-049, 1 hul-047, 1 hul-018, 1 hul-048, 1 ecp-047, 2 pwr-001 | 1 hul-050 | — |
| press a hull doubler plate | hul.pressbrake | 75 | 1 met-005, 1 hul-009, 4 hul-007, 1 pwr-001 | 1 hul-051 | — |
| lay up a hull spall liner | hul.molder | 90 | 2 fib-066, 1 pol-007, 1 pwr-001 | 1 hul-052 | — |
| mould crack stoppers | hul.molder | 20 | 1 pol-059, 1 met-039, 1 pwr-001 | 4 hul-053 | — |
| rivet a crack arrest strap | hul.pressbrake | 60 | 1 hul-053, 2 hul-014, 1 hul-012, 1 pwr-001 | 1 hul-054 | — |
| weld a titanium hull brace | hul.welder | 150 | 2 met-050, 2 hul-008, 1 hul-011, 1 hul-056, 1 pwr-001 | 1 hul-055 | — |
| mix welding flux paste | hul.welder | 30 | 1 chm-051, 1 pol-064, 1 pwr-001 | 3 hul-056 | — |
| fill a hull coating cartridge | hul.molder | 60 | 1 pol-007, 1 chm-043, 1 pak-023, 1 pwr-001 | 1 hul-057 | — |
| assemble a repair drone bay kit | any.bench | 150 | 1 fur-001, 1 hul-095, 1 mec-043, 1 ecp-046 | 1 hul-058 | — |
| mix suppressant foam | hul.safetybench | 40 | 2 wat-009, 1 chm-061, 1 pwr-001 | 3 hul-059 | — |
| blend dry chemical powder | hul.safetybench | 60 | 1 chm-022, 1 chm-003, 1 pwr-001 | 3 hul-060 | — |
| grind bicarbonate into extinguisher powder | any.bench | 30 | 2 chm-012 | 1 hul-060 | — |
| fill a foam extinguisher | hul.safetybench | 60 | 2 hul-059, 1 pak-005, 1 gas-003, 1 pwr-001 | 1 hul-061 | — |
| fill a dry powder extinguisher | hul.safetybench | 60 | 3 hul-060, 1 pak-005, 1 gas-006, 1 pwr-001 | 1 hul-062, 1 pak-006 | — |
| sew a fire blanket | hul.safetybench | 60 | 2 hul-064, 1 pol-036, 1 pwr-001 | 1 hul-063 | — |
| coat glass fibre fire cloth | hul.safetybench | 60 | 2 cer-061, 1 pol-021, 1 pwr-001 | 2 hul-064 | — |
| build a cabin smoke detector | hul.safetybench | 60 | 1 lgt-051, 1 pol-045, 1 pwr-023, 1 pwr-001 | 1 hul-065 | — |
| build a cabin gas leak alarm | hul.safetybench | 60 | 1 lgt-010, 1 pol-045, 1 ecp-044, 1 pwr-001 | 1 hul-066 | — |
| build a pressure loss alarm | hul.safetybench | 60 | 1 lgt-009, 1 pol-045, 1 ecp-044, 1 pwr-001 | 1 hul-067 | — |
| build a fire suppression sprinkler | hul.safetybench | 90 | 1 hul-061, 1 lgt-008, 1 mec-049, 1 pwr-001 | 1 hul-068 | — |
| build an emergency mask | hul.safetybench | 40 | 1 hul-072, 1 pol-036, 1 fib-006, 1 pwr-001 | 1 hul-069 | — |
| build an escape hood | hul.safetybench | 60 | 1 hul-064, 1 hul-072, 1 pol-002, 1 pwr-001 | 1 hul-070 | — |
| refill a spent mask cartridge | hul.safetybench | 30 | 1 hul-071, 1 fil-076, 1 pwr-001 | 1 hul-072, 1 fil-022 | — |
| discard a spent mask cartridge | crew | 2 | 1 hul-071 | 1 scr-002 | — |
| pack mask filter cartridges | hul.safetybench | 40 | 1 fil-076, 1 fil-037, 1 pol-045, 1 pwr-001 | 2 hul-072 | — |
| press an oxygen candle | hul.safetybench | 60 | 1 gas-051, 1 gas-053, 1 met-043, 1 pwr-001 | 1 hul-073 | — |
| fill an emergency air bag | hul.safetybench | 40 | 1 gas-006, 1 pol-031, 1 pwr-001 | 1 hul-074, 1 pak-006 | — |
| mould an inflatable breach plug | hul.molder | 60 | 1 pol-003, 1 gas-003, 1 pol-004, 1 pwr-001 | 1 hul-075 | — |
| press a breach plate | hul.pressbrake | 90 | 1 hul-002, 1 hul-010, 1 pol-058, 1 pwr-001 | 1 hul-076 | — |
| pack a rapid breach kit | hul.safetybench | 90 | 1 hul-076, 1 hul-075, 1 hul-004, 1 pak-032 | 1 hul-077 | — |
| fill leak tracer spray | hul.safetybench | 30 | 1 gas-038, 2 pak-021, 1 pwr-001 | 2 hul-078, 1 pak-006 | — |
| sew a safety harness | hul.safetybench | 60 | 2 fib-070, 1 mec-046, 1 pwr-001 | 1 hul-079 | — |
| pack an emergency shelter pouch | hul.safetybench | 90 | 1 thm-031, 1 hul-073, 1 pol-031, 1 pwr-001 | 1 hul-080 | — |
| pack an emergency grab bag | hul.safetybench | 60 | 1 hul-069, 1 hul-006, 1 wat-051, 1 pak-032 | 1 hul-081 | — |
| build a crawler chassis | hul.dronebay | 120 | 1 cer-083, 2 mec-048, 1 mec-010, 1 pwr-001 | 1 hul-082 | — |
| make magnetic crawler wheels | hul.dronebay | 60 | 1 met-077, 1 pol-003, 1 mec-004, 1 pwr-001 | 2 hul-083 | — |
| build a drone repair arm | hul.dronebay | 90 | 1 mec-043, 1 mec-010, 1 met-050, 1 pwr-001 | 1 hul-084 | — |
| build a hull crawler | hul.dronebay | 180 | 1 hul-082, 1 ecp-052, 1 pwr-006, 1 lgt-036, 1 pwr-001 | 1 hul-085 | — |
| build a hull walker | hul.dronebay | 200 | 1 hul-082, 2 hul-083, 1 ecp-052, 1 pwr-006, 1 pwr-001 | 1 hul-086 | — |
| build a hull inspection drone | hul.dronebay | 180 | 1 cer-083, 1 mec-009, 1 lgt-036, 1 ecp-052, 1 pwr-006 | 1 hul-087 | — |
| build a welding arm bot | hul.dronebay | 240 | 1 hul-082, 1 hul-084, 2 hul-008, 1 ecp-046, 1 pwr-006 | 1 hul-088 | — |
| build a leak sniffer drone | hul.dronebay | 200 | 1 hul-082, 1 lgt-010, 1 ecp-052, 1 pwr-006 | 1 hul-089 | — |
| cut a press brake die | any.bench | 90 | 1 met-030, 1 met-005 | 1 hul-090 | — |
| make welder electrode tips | any.bench | 40 | 1 met-003, 1 cer-038 | 2 hul-091 | — |
| cut a seal mould insert | any.bench | 90 | 1 met-030, 1 pol-074 | 1 hul-092 | — |
| bond a glazing wheel | any.bench | 60 | 1 cer-039, 1 met-007, 1 pol-010 | 1 hul-093 | — |
| turn an extinguisher fill head | any.bench | 60 | 1 met-051, 1 pol-009 | 1 hul-094 | — |
| build a drone bay gantry rail | any.bench | 90 | 1 cer-078, 1 mec-030 | 1 hul-095 | — |
| assemble a press brake kit | any.bench | 180 | 2 fur-001, 1 hul-090, 1 mec-043, 1 met-005 | 1 hul-096 | — |
| assemble a welding jig kit | any.bench | 150 | 1 fur-001, 1 hul-091, 1 pwr-016, 1 mec-007 | 1 hul-097 | — |
| assemble a seal molder kit | any.bench | 150 | 1 fur-001, 1 hul-092, 1 thm-004, 1 mec-040 | 1 hul-098 | — |
| assemble a glazing bench kit | any.bench | 120 | 1 fur-001, 1 hul-093, 1 mec-010 | 1 hul-099 | — |
| assemble a safety gear bench kit | any.bench | 120 | 1 fur-001, 1 hul-094, 1 mec-042 | 1 hul-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| hul.pressbrake | Presses metal into hull plates, skins, stringers, rings, rivets, hatch doors and whipple layers. | CRUSH HAZARD. LIGHT CURTAIN MUST BE CLEAR BEFORE STROKE. |
| hul.welder | Welds braces, frames, hatch parts and the large hull sections. | Arc flash causes eye injury. Eye injury is not covered for operators without goggles on file. |
| hul.molder | Moulds gaskets, plugs, patches, tapes, putty and the sealant and coating cartridges. | Every seal aboard was cured here. Cure times are fixed. Rushing them is logged. |
| hul.glazer | Laminates viewport glass, glazes viewports and radiation windows, and reglazes crazed viewports. | Polish both faces. Inspection is from the cabin side only. Outboard is on trust. |
| hul.safetybench | Fills extinguishers and oxygen canisters, and builds masks, alarms, breach kits and grab bags. | Safety equipment is a Company asset. Use in a non-emergency is investigated. Ref 9110/S. |
| hul.dronebay | Builds the crawlers, walkers and drones that repair the hull from outside. | Drones do the outboard work. Operators are not rated for vacuum. Drones are cheaper. |
| hul-001 | Pressed, riveted plate that raises hull integrity when passed through the service hatch. | STRUCTURAL PART. HULL GRADE. DO NOT DRILL, CUT OR STAND ON. |
| hul-002 | Thin sheet for patching the hull, and the base of adhesive and self-sealing patches. | Temporary repair only. A permanent repair is scheduled. Schedule not attached. |
| hul-003 | Cartridge of sealant that repairs the hull and holds pressure; spoils on the shelf. | Apply in one bead. Smooth with tool, not finger. Sealant does not come off fingers. |
| hul-004 | Bag of patches, plug and sealant that closes a breach and holds cabin pressure. | Instructions printed on outside. Read before the breach. Reading during is slower. |
| hul-005 | Extinguisher that puts out a fire, sparing health and nerves; leaves an empty canister. | PULL PIN. AIM AT BASE OF FIRE. SQUEEZE. SWEEP. |
| hul-006 | Canister of oxygen vented into the cabin when the air fails. | Emergency oxygen is billed per canister opened. The bill is deferred until after. |
| hul-007 | Headed rivet that holds hull plates, rings and handles together. | Rivet count per plate is specified. Missing rivets are counted by inspection drone. |
| hul-008 | Flux-coated rod for welding braces, frames and window frames. | Keep dry. Damp rods give porous welds. Porous welds leak. Proc 120. |
| hul-009 | Pressed metal sheet for skins, stringers, plates, hatch doors and emitter housings. | Gauge stamped in corner, Grade 2. Corner trimmed off. Gauge assumed. |
| hul-010 | Rubber gasket that seals hatch doors, airlocks, bulkheads and shield seals. | Inspect for cracks each cycle. A cracked gasket is a hatch that is merely closed. |
| hul-011 | Welded brace that strengthens the hull and goes into heavier braces and shields. | Load path verified on drawing. Drawing verified by the person who drew it. |
| hul-012 | Long pressed rib that stiffens skins, frame rings and sections. | Stringer spacing fixed by design. Adding stringers for comfort is not authorised. |
| hul-013 | Rolled ring that shapes hatch doors, frame sections and keel beams. | Roundness checked at four points, rev 6. Fifth point would have failed. |
| hul-014 | Strip of blind rivets for skin panels and crack arrest straps. | For joints reachable from one side. Most of the hull is. |
| hul-015 | Riveted skin panel that raises hull integrity and goes into hull segments. | Hull panels are serialised. SN 4410 2207. Location of fitting is not disclosed. |
| hul-016 | Thin outer plate that breaks up debris; layered into whipple shields. | Sacrificial plate. It is expected to be destroyed. It is still inventoried. |
| hul-017 | Spaced bumper layer that guards the hull and adds a little to the shield. | DEBRIS SHIELD. SPACING IS CRITICAL. DO NOT COMPRESS LAYERS. |
| hul-018 | Two whipple layers on a brace, guarding hull and shield better than one. | Two layers rated against debris class C. Debris is not informed of its class. |
| hul-019 | Foam block that fills hull panels. | Between the cabin and vacuum: one panel, this foam, one panel. |
| hul-020 | Foam-cored panel that raises hull integrity and goes into hull segments. | Low mass, high stiffness. Damage tolerance under review since rev 3. |
| hul-021 | Glue-backed patch for small holes; goes into breach patch kits and dries out on the shelf. | Peel, apply, press for a slow count of thirty. Count is not optional. |
| hul-022 | Rubber plug that holds pressure in a small breach. | Insert firmly. Report the breach afterwards. Afterwards is a matter of minutes. Proc 1B. |
| hul-023 | Patch that seals itself over a leak, repairing hull and air together. | APPLY OVER LEAK. STAND CLEAR WHILE IT CURES. |
| hul-024 | Metal-backed tape for small hull leaks, and part of a breach patch kit. | A hiss means tape. A continued hiss means more tape, then a Form 8L. |
| hul-025 | Stick of hull putty, tubed into epoxy seam sealer. | Knead until uniform colour. Hands complain before the putty is ready. |
| hul-026 | Tube of epoxy that repairs seams and holds pressure; dries out on the shelf. | Pot life is short. Mixed epoxy left to cure in the tube is charged as waste. |
| hul-027 | Tape that holds back a little cabin pressure. | For the hiss only just audible. Audible hisses are reported regardless. |
| hul-028 | Moulded rubber blank, cut into window seal strips and port seal rings. | Cut to template. Templates are not to be traced from old gaskets. They are. |
| hul-029 | Seal strip for glazing viewports. | Glass and frame expand at different rates. This strip absorbs the disagreement. |
| hul-030 | Sealing ring for radiation windows and airlock seal sets. | Seat evenly. A pinched ring leaks slowly, then at once. Rev 4 note. |
| hul-031 | Welded frame that holds viewport glass; recovered when a crazed viewport is stripped. | The frame outlasts the glass, and the operator. It is reused accordingly. |
| hul-032 | Laminated glass for viewports and radiation windows. | PRESSURE GLASS. HANDLE BY EDGES. DO NOT SCRATCH OUTER FACE. |
| hul-033 | Glazed viewport that lights the cabin; crazes with age. | The view is provided for illumination. Its content is not part of the contract. |
| hul-034 | Shielded window that lights the cabin and reduces the operator's radiation dose. | Dose reduction is calculated per operator. Results are held in the operator's file. |
| hul-035 | Clouded viewport, reglazed or stripped for its frame. | Crazing first noted rev 1. Spreading, rev 5. Reglaze requested, rev 6. Pending. |
| hul-036 | Welded hinge pair for a hatch latch ring. | Heavy hinges for a heavy door. Grease monthly. Grease is rationed quarterly. |
| hul-037 | Latching ring of a hatch, for hatch rebuild kits and service hatch kits. | Turn until it clunks. No clunk, no seal. Proc 2, hatches. |
| hul-038 | Pressed, gasketed hatch door for hatch rebuild kits and service hatch kits. | PRESSURE DOOR. KEEP CLEAR OF SWING. NEVER BLOCK OPEN. |
| hul-039 | Welded hand wheel, the grip of a dogging handle. | Direction arrows worn off. Clockwise to close. Probably. Check the latch. |
| hul-040 | Spare door, latch ring and gasket for the service hatch. | Rebuild when the hatch sighs. Sighing hatches are a priority two fault. |
| hul-041 | Spare handle that dogs the service hatch shut. | Dog fully down. Partly dogged hatches have been the subject of Notice 1. |
| hul-042 | Spare seal set for the service hatch; wears into rubber scrap. | The difference between a hatch and a hole is this set. Fit with care, rev 9. |
| hul-043 | Ceramic and steel corner brace for trusses, frames and bulkheads. | Corners crack first. Corner braces are therefore inspected first. Proc 44. |
| hul-044 | Welded truss that raises hull integrity and goes into keel beams. | Triangulated for rigidity. Rigidity is the hull's only approved quality. |
| hul-045 | Welded frame section that raises hull integrity and goes into hull segments. | Section number stencilled inside flange. Section location withheld per policy. |
| hul-046 | Gasketed bulkhead plate that strengthens the hull and holds pressure. | Holds when the next compartment fails. Which compartment is not a station concern. |
| hul-047 | Welded bulkhead that raises hull integrity and goes into hull section units. | COMPARTMENT BOUNDARY. DO NOT BREACH FOR CABLE RUNS. |
| hul-048 | Long beam of trusses that strongly raises hull integrity. | Primary structure. Defects are a fleet notice. Fleet notices carry names. |
| hul-049 | Joined segment of frame, skin and foam that greatly raises hull integrity. | Built from six subsections' output. Credited to the station that ships it. |
| hul-050 | Largest hull good: a whole section that raises hull integrity most of all. | One deck of work through one hatch. Throughput recorded. Effort not recorded. |
| hul-051 | Doubled plate riveted over a weak spot in the hull. | Fitted over a weak spot. The weak spot remains on the register. |
| hul-052 | Aramid liner that catches fragments inside the hull. | Catches fragments that pass the hull. Operators behind it are a secondary benefit. |
| hul-053 | Small moulded stopper that halts a crack; goes into crack arrest straps. | Drill crack tip, fit stopper, mark date. Unmarked cracks are assumed new. |
| hul-054 | Riveted strap across a crack that strengthens the hull. | Crack length logged before strapping. Growth after strapping is a Form 54K. |
| hul-055 | Titanium brace that strongly raises hull integrity. | High-value alloy. Offcuts are returned by mass. Shortfall is deducted. |
| hul-056 | Flux for weld rods, scrap patch sheets and titanium welds. | Fumes on heating. Use extraction. Extraction fan noise is not a fault. |
| hul-057 | Cartridge of protective hull coating; dries out on the shelf. | One coat now costs less than one plate later. Finance has confirmed this. |
| hul-058 | Packed kit that installs a repair drone bay. | Assembled by personnel for drones. Drones are not consulted on layout. |
| hul-059 | Fire suppressant foam for foam extinguishers. | Smothers fire and everything near it. Clean-up time is not counted as work. |
| hul-060 | Extinguisher powder for fire extinguishers and dry powder extinguishers. | IRRITANT. DO NOT INHALE. KEEP CONTAINER SEALED. |
| hul-061 | Foam extinguisher that puts out a fire; also the core of a sprinkler. | For fires water would spread. Inspection tag punched, rev 11. Gauge in green. |
| hul-062 | Powder extinguisher that puts out a fire but leaves some toxin in the air. | Effective on all fire classes. Residue effective on all operators. Ventilate. |
| hul-063 | Fireproof blanket that smothers a fire; leaves fabric scraps. | PULL TAPES DOWN SHARPLY. COVER FIRE. HOLD. DO NOT LIFT TO CHECK. |
| hul-064 | Fireproof glass fibre cloth for fire blankets and escape hoods. | Does not burn. Does itch. Itching is not a recognised injury. Ref 6464/C. |
| hul-065 | Detector that eases stress while it watches for smoke; ends as e-waste. | Removal of detector to silence it is a disciplinary matter. The toast is not. |
| hul-066 | Alarm that eases stress while it watches for gas leaks. | Test monthly. The test tone is the same as the real one. Act on both. |
| hul-067 | Alarm that eases stress while it watches for falling pressure. | If it sounds, leave the drink. Leave everything. Proc 0 overrides all others. |
| hul-068 | Heat-triggered sprinkler that eases stress while it guards the cabin. | Do not hang items from sprinkler head. Do not paint sprinkler head. Notice 18. |
| hul-069 | Filter mask that clears toxin from the breath; leaves a spent mask cartridge. | SEAL MASK. THEN BREATHE. NOT THE OTHER WAY ROUND. |
| hul-070 | Fireproof hood with a filter that clears toxin and spares health. | Over head, pull tight, walk out. Where to walk to is shown on the posted plan. |
| hul-071 | Used mask filter cartridge, refilled or discarded. | Contains what was not breathed. Dispose per Proc 71. Do not sniff to check. |
| hul-072 | Carbon filter cartridge for emergency masks and escape hoods. | Shelf date on seal. Use before date. After date, use anyway and report. |
| hul-073 | Chemical candle that releases oxygen and a little heat; leaves its casing. | STRIKE. SET DOWN ON NON-FLAMMABLE SURFACE. DO NOT HOLD. BURNS HOT. |
| hul-074 | Bag of nitrogen that restores cabin pressure quickly. | Release when ears pop. Ear discomfort is the approved pressure indicator. |
| hul-075 | Inflatable plug that holds a lot of pressure and repairs the hull a little. | Expands to fit most holes. Holes larger than most go to Proc 0. |
| hul-076 | Gasketed plate that closes a breach and holds pressure. | Bolt on before the next breath. Torque values are on the reverse, at leisure. |
| hul-077 | Breach plate, plug and patch kit in one bag, the most effective fix for a breach. | Grab, open, plate, plug, seal. Then fill out Form 77R. Then sit down. |
| hul-078 | Spray that shows where air is leaking so the leak can be sealed. | Spray. Watch the drift. Where it goes is the leak. Where it goes next is the report. |
| hul-079 | Webbing harness that eases stress while it is kept in the cabin. | CLIP IN BEFORE MANOEUVRE. CHECK BUCKLE. CHECK AGAIN. |
| hul-080 | Pouch that provides air, heat and pressure to ride out a cabin failure. | Enter, seal, wait. Rescue response time is not specified under the contract. |
| hul-081 | Bag of mask, oxygen and water that sees an operator through a crisis. | Stow under the bunk. Contents checked monthly. Missing water is invoiced. |
| hul-082 | Drone chassis for crawlers, walkers, welding bots and sniffer drones. | Chassis serial must be logged before wheels or legs are fitted. Proc 82. |
| hul-083 | Magnetic wheel that grips the hull, for hull walkers. | STRONG MAGNET. KEEP FROM INSTRUMENTS, CARDS AND FINGERS. |
| hul-084 | Robot arm for the welding arm bot. | Reach envelope exceeds a hand's. Pinch force exceeds it too. Keep clear. |
| hul-085 | Camera crawler that keeps repairing the hull while it works; wears into e-waste. | Works outboard so personnel need not. Personnel are reminded they need not. |
| hul-086 | Magnetic-wheeled crawler that repairs the hull faster than the hull crawler. | Heard on the hull at night. It does not stop for rest periods. Nobody asked it to. |
| hul-087 | Camera drone that keeps repairing the hull while it lasts. | Every crack it sees is reported upward. So is every station it passes. |
| hul-088 | Welding robot, the fastest of the drones at repairing the hull. | Flicker at the viewport is the bot at work. Do not look directly. Return to rest. |
| hul-089 | Drone that detects leaks, repairing the hull and holding pressure. | Detects leaks by trace gas. Detects unauthorised cooking by the same means. |
| hul-090 | Spare die for the press brake; wears into metal scrap. | Die angle stamped on side. Wear changes the angle. The stamp stays the same. |
| hul-091 | Spare electrode tip for the welding jig; wears quickly. | Dress tip every fifty welds. Count is kept by the jig, not by memory. |
| hul-092 | Spare mould insert for the seal molder. | Cavity profile matches drawing rev 12. Gaskets in service match rev 9. |
| hul-093 | Spare polishing wheel for the glazing bench. | Balanced, rev 2. Slight wobble at speed. Polishes slightly unevenly. Accepted. |
| hul-094 | Spare fill head for the safety gear bench. | Fills extinguishers that are hoped never to be used. Hope is not a stores item. |
| hul-095 | Spare gantry rail for the repair drone bay, and part of its kit. | The drones ride it. Personnel maintain it. That is the arrangement. |
| hul-096 | Packed kit that installs a press brake. | GROSS MASS EXCEEDS ONE-PERSON LIFT. MECHANICAL AID REQUIRED. |
| hul-097 | Packed kit that installs a welding jig. | Gas supply connected by station personnel. Leak test before first arc. Proc 97. |
| hul-098 | Packed kit that installs a seal molder. | Heater and pump inside. Commissioning cure run is billed as production. |
| hul-099 | Packed kit that installs a glazing bench. | FRAGILE. THIS WAY UP. BREAKAGE IN TRANSIT IS THE RECEIVER'S PROBLEM. |
| hul-100 | Packed kit that installs a safety gear bench. | Ships with one of each safety item for reference. Reference items are not for use. |
