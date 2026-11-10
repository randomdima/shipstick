# Navigation & Data — `nav`

What keeps the heading true and the ship's computers stocked. Ink and sheets are pressed into charts, ephemeris tables
and burn plans that go stale with time; rotors, gimbals, lenses, dishes and beacons become gyros, star trackers, radar
and lidar; firmware, operating images and storage cards are written and racked into the ship's computer cores. Charts,
plots and instruments raise `ship.course` and the data goods `ship.data`, all at the service hatch. The large ones take
chips, sensors, optics and metal from many subsections; stale plots and corrupted cards come back to be pulped or wiped.

## Devices

| id | device | role | cells |
|---|---|---|---|
| nav.chartpress | NV120 Chart Press | helm | 2x1 |
| nav.plotter | NV240 Course Plotter | helm | 2x2 |
| nav.gyrobench | NV310 Gyro Bench | helm | 2x2 |
| nav.sensorbay | NV450 Sensor Mast Bay | helm | 3x2 |
| nav.corebay | NV600 Core Integration Bay | elec | 3x2 |
| nav.coderoom | NV75C Firmware Lab | elec | 2x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| nav-001 | Chart, Star | ship.course +4 | 2000 h → nav-030 |
| nav-002 | Plot, Course | ship.course +5 | 240 h → nav-031 |
| nav-003 | Card, Data | ship.data +5 | 2000 h → nav-086 |
| nav-004 | Module, Core | ship.data +20 | — |
| nav-005 | Tracker, Star | ship.course +15 | — |
| nav-006 | Sheet, Chart | — | — |
| nav-007 | Ink, Plotting | — | — |
| nav-008 | Table, Ephemeris | — | 720 h → nav-032 |
| nav-009 | Card, Data, Blank | — | — |
| nav-010 | Firmware, Navigation | — | — |
| nav-011 | Map, Sector | ship.course +1 | 2000 h → nav-030 |
| nav-012 | Folio, Chart | ship.course +3 | 2000 h → nav-030 |
| nav-013 | Card, Ephemeris | ship.course +3 | 720 h → nav-032 |
| nav-014 | Card, Star Catalogue | — | — |
| nav-015 | Overlay, Plot | — | — |
| nav-016 | Card, Waypoint | ship.course +1 | 240 h → nav-031 |
| nav-017 | Sheet, Burn Plan | — | — |
| nav-018 | Plan, Burn, Course Correction | ship.course +6 | 240 h → nav-031 |
| nav-019 | Plan, Correction, Fine | ship.course +4 | 240 h → nav-031 |
| nav-020 | Plan, Turn, Emergency | ship.course +10 | 120 h → nav-031 |
| nav-021 | Table, Orbit Transfer | ship.course +5 | 720 h → nav-032 |
| nav-022 | Plan, Gravity Assist | ship.course +15 | 240 h → nav-031 |
| nav-023 | Report, Drift | ship.course +1 | 240 h → nav-031 |
| nav-024 | Log, Star Fix | ship.course +2 | — |
| nav-025 | Ledger, Course | ship.course +3 | — |
| nav-026 | Handbook, Navigator | ship.course +3 | — |
| nav-027 | Pack, Survey Data | ship.course +4, ship.data +2 | — |
| nav-028 | Pack, Survey, Deep | ship.course +8, ship.data +4 | — |
| nav-029 | Atlas, Navigator, Master | ship.course +20 | — |
| nav-030 | Chart, Star, Outdated | — | — |
| nav-031 | Plot, Course, Stale | — | — |
| nav-032 | Table, Ephemeris, Stale | — | — |
| nav-033 | Wheel, Gyro Rotor | — | — |
| nav-034 | Ring, Gyro Gimbal | — | — |
| nav-035 | Motor, Gyro Spin | — | — |
| nav-036 | Damper, Gyro Vibration | — | — |
| nav-037 | Stack, Accelerometer | — | — |
| nav-038 | Compass, Gyro | ship.course +6 | — |
| nav-039 | Stabilizer, Gyro | ship.course +10 | — |
| nav-040 | Unit, Inertial | ship.course +12 | — |
| nav-041 | Lens, Star Tracker | — | — |
| nav-042 | Head, Star Tracker Camera | — | — |
| nav-043 | Wheel, Reaction | ship.course +8 | — |
| nav-044 | Waveguide, Radar | — | — |
| nav-045 | Array, Radar Antenna | — | — |
| nav-046 | Dish, Radar | — | — |
| nav-047 | Transceiver, Radar | — | — |
| nav-048 | Unit, Radar | ship.course +10 | — |
| nav-049 | Head, Lidar Optics | — | — |
| nav-050 | Module, Lidar Laser | — | — |
| nav-051 | Unit, Lidar | ship.course +10 | — |
| nav-052 | Pinger, Proximity | ship.course +3 | — |
| nav-053 | Housing, Beacon | — | — |
| nav-054 | Transmitter, Beacon | — | — |
| nav-055 | Beacon, Nav | ship.course +5 | — |
| nav-056 | Beacon, Relay | ship.course +8, ship.data +2 | — |
| nav-057 | Movement, Chronometer | — | — |
| nav-058 | Chronometer | ship.course +4 | — |
| nav-059 | Sextant, Optical | ship.course +5 | — |
| nav-060 | Mirror, Horizon | — | — |
| nav-061 | Compass, Hand | ship.course +1 | — |
| nav-062 | Pencil, Navigator | — | — |
| nav-063 | Notebook, Navigator | ship.course +1 | — |
| nav-064 | Image, Bootloader | — | — |
| nav-065 | Image, Kernel | — | — |
| nav-066 | Library, Driver | — | — |
| nav-067 | Image, Operating System | ship.data +15 | — |
| nav-068 | Engine, Database | ship.data +8 | — |
| nav-069 | Codec, Compression | ship.data +6 | — |
| nav-070 | Suite, Diagnostics | ship.data +6 | — |
| nav-071 | Stack, Network | ship.data +6 | — |
| nav-072 | Image, Backup | ship.data +6 | — |
| nav-073 | Card, Boot ROM | ship.data +2 | — |
| nav-074 | Card, Telemetry | ship.data +3 | — |
| nav-075 | Card, Archive | ship.data +5 | — |
| nav-076 | Module, Log Recorder | ship.data +8 | — |
| nav-077 | Module, Flight Recorder | ship.data +8 | — |
| nav-078 | Array, Storage | ship.data +12 | — |
| nav-079 | Cluster, Mass Storage | ship.data +20 | — |
| nav-080 | Board, Network Switch | ship.data +8 | — |
| nav-081 | Controller, Ship Bus | ship.data +15 | — |
| nav-082 | Node, Cluster | ship.data +20 | — |
| nav-083 | Rack, Compute | ship.data +18 | — |
| nav-084 | Module, Core, Redundant | ship.data +18 | — |
| nav-085 | Controller, Autonomic | ship.data +25 | — |
| nav-086 | Card, Data, Corrupted | — | — |
| nav-087 | Computer, Nav | ship.course +10, ship.data +5 | — |
| nav-088 | Unit, Bridge Terminal | ship.data +3 | — |
| nav-089 | Roller, Chart Press | fits nav.chartpress | 800 h → scr-004 |
| nav-090 | Head, Plotter Stylus | fits nav.plotter | 500 h → scr-004 |
| nav-091 | Jig, Gyro Bench | fits nav.gyrobench | 1000 h → scr-001 |
| nav-092 | Fan, Sensor Bay Cooling | fits nav.sensorbay | 800 h → mec-080 |
| nav-093 | Guide, Rack Slot | fits nav.corebay | 1500 h → scr-004 |
| nav-094 | Probe, Firmware Debug | fits nav.coderoom | 800 h → scr-003 |
| nav-095 | Kit, Chart Press | installs nav.chartpress | — |
| nav-096 | Kit, Course Plotter | installs nav.plotter | — |
| nav-097 | Kit, Gyro Bench | installs nav.gyrobench | — |
| nav-098 | Kit, Sensor Mast Bay | installs nav.sensorbay | — |
| nav-099 | Kit, Core Integration Bay | installs nav.corebay | — |
| nav-100 | Kit, Firmware Lab | installs nav.coderoom | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| press a star chart | nav.chartpress | 120 | 2 nav-006, 1 nav-007, 1 nav-014, 1 pwr-001 | 1 nav-001 | — |
| sketch a star chart from the window | any.bench | 240 | 3 nav-006, 1 nav-062 | 1 nav-001 | — |
| plot a course | nav.plotter | 120 | 1 nav-001, 1 nav-015, 1 nav-008, 1 pwr-001 | 1 nav-002 | — |
| reckon a course by hand | any.bench | 180 | 2 nav-006, 1 nav-062, 1 nav-024 | 1 nav-002 | — |
| write a data card | nav.coderoom | 40 | 1 nav-009, 1 pwr-001 | 1 nav-003 | — |
| rack a core module | nav.corebay | 180 | 1 ecp-069, 1 nav-067, 1 cer-083, 1 pwr-001 | 1 nav-004 | — |
| build a core module from a board computer | nav.corebay | 200 | 1 ecp-052, 2 ecp-009, 1 nav-065, 1 ecp-067, 1 pwr-001 | 1 nav-004 | — |
| build a star tracker | nav.gyrobench | 200 | 1 nav-042, 1 nav-014, 1 ecp-014, 1 nav-036, 1 pwr-001 | 1 nav-005 | — |
| mount a camera star tracker | nav.sensorbay | 240 | 1 lgt-036, 1 nav-041, 1 ecp-052, 1 nav-014, 1 pwr-001 | 1 nav-005 | — |
| press chart sheets from pulp | nav.chartpress | 40 | 2 pak-086, 1 pwr-001 | 4 nav-006 | — |
| press chart sheets on film | nav.chartpress | 40 | 1 pol-002, 1 pwr-001 | 3 nav-006 | — |
| pulp stale course plots | nav.chartpress | 40 | 2 nav-031, 1 wat-009, 1 pwr-001 | 2 nav-006 | — |
| pulp stale ephemeris tables | nav.chartpress | 40 | 2 nav-032, 1 wat-009, 1 pwr-001 | 2 nav-006 | — |
| pulp an outdated star chart | nav.chartpress | 30 | 1 nav-030, 1 wat-009, 1 pwr-001 | 1 nav-006 | — |
| mix plotting ink | nav.chartpress | 30 | 1 chm-046, 1 chm-041, 1 pwr-001 | 4 nav-007 | — |
| stir soot into plotting ink | any.bench | 30 | 1 chm-041, 1 wat-001 | 1 nav-007 | — |
| tabulate ephemerides | nav.chartpress | 90 | 2 nav-006, 1 nav-007, 1 pwr-001 | 2 nav-008 | — |
| mould blank data cards | nav.coderoom | 60 | 1 ecp-039, 1 pol-045, 1 met-040, 1 pwr-001 | 2 nav-009 | — |
| wipe a corrupted data card | nav.coderoom | 30 | 1 nav-086, 1 pwr-001 | 1 nav-009 | — |
| discard a corrupted data card | crew | 5 | 1 nav-086 | 1 scr-003 | — |
| flash navigation firmware | nav.coderoom | 90 | 1 ecp-040, 1 nav-008, 1 pwr-001 | 1 nav-010 | — |
| print sector maps | nav.chartpress | 50 | 2 nav-006, 1 nav-007, 1 pwr-001 | 2 nav-011 | — |
| bind a chart folio | nav.chartpress | 60 | 1 nav-001, 2 nav-011, 1 pak-057, 1 pwr-001 | 1 nav-012 | — |
| cut ephemeris cards | nav.chartpress | 60 | 1 nav-008, 1 pak-057, 1 pwr-001 | 2 nav-013 | — |
| print star catalogue cards | nav.chartpress | 80 | 1 nav-006, 1 nav-007, 1 pak-067, 1 pwr-001 | 2 nav-014 | — |
| etch plot overlays | nav.plotter | 60 | 1 pol-034, 1 nav-007, 1 pwr-001 | 2 nav-015 | — |
| print waypoint cards | nav.chartpress | 40 | 1 nav-006, 1 nav-007, 1 pwr-001 | 4 nav-016 | — |
| rule burn plan sheets | nav.plotter | 40 | 2 nav-006, 1 nav-007, 1 pwr-001 | 3 nav-017 | — |
| plan a course correction burn | nav.plotter | 140 | 2 nav-017, 1 nav-008, 1 nav-002, 1 pwr-001 | 1 nav-018 | — |
| plan a fine correction | nav.plotter | 100 | 2 nav-017, 1 nav-015, 1 pwr-001 | 1 nav-019 | — |
| plan an emergency turn | nav.plotter | 180 | 1 nav-018, 1 nav-023, 1 nav-013, 1 pwr-001 | 1 nav-020 | — |
| compute an orbit transfer table | nav.plotter | 130 | 1 nav-008, 1 nav-017, 1 nav-013, 1 pwr-001 | 1 nav-021 | — |
| plan a gravity assist | nav.plotter | 240 | 1 nav-021, 1 nav-018, 1 nav-027, 1 ecp-014, 1 pwr-001 | 1 nav-022 | — |
| write drift reports | nav.plotter | 60 | 1 nav-006, 1 nav-024, 1 pwr-001 | 2 nav-023 | — |
| log star fixes | nav.chartpress | 70 | 2 nav-006, 1 nav-007, 1 pwr-001 | 2 nav-024 | — |
| bind a course ledger | nav.chartpress | 90 | 2 nav-024, 1 fib-008, 1 pwr-001 | 1 nav-025 | — |
| bind a navigator handbook | nav.chartpress | 120 | 1 nav-025, 1 nav-012, 1 pak-057, 1 pwr-001 | 1 nav-026 | — |
| record a survey data pack | nav.coderoom | 120 | 1 nav-009, 1 nav-024, 1 ecp-047, 1 pwr-001 | 1 nav-027 | — |
| record a deep survey pack | nav.coderoom | 200 | 2 nav-027, 1 lgt-036, 1 nav-009, 1 pwr-001 | 1 nav-028 | — |
| compile a master navigator atlas | nav.plotter | 300 | 1 nav-026, 1 nav-020, 1 nav-028, 1 nav-012, 1 pwr-001 | 1 nav-029 | — |
| turn gyro rotor wheels | nav.gyrobench | 70 | 1 met-026, 1 mec-004, 1 pwr-001 | 2 nav-033 | — |
| turn gyro gimbal rings | nav.gyrobench | 60 | 1 met-055, 2 mec-004, 1 pwr-001 | 2 nav-034 | — |
| build a gyro spin motor | nav.gyrobench | 100 | 1 mec-024, 1 mec-025, 1 nav-033, 1 pwr-001 | 1 nav-035 | — |
| make gyro vibration dampers | nav.gyrobench | 40 | 1 pol-003, 1 mec-045, 1 pwr-001 | 2 nav-036 | — |
| stack accelerometers | nav.gyrobench | 120 | 3 lgt-053, 1 ecp-047, 1 nav-036, 1 pwr-001 | 1 nav-037 | — |
| build a gyro compass | nav.gyrobench | 150 | 1 nav-035, 1 nav-034, 1 ecp-007, 1 pwr-001 | 1 nav-038 | — |
| build a gyro stabilizer | nav.gyrobench | 180 | 1 nav-038, 1 nav-034, 1 nav-036, 1 pwr-001 | 1 nav-039 | — |
| build an inertial unit | nav.gyrobench | 220 | 1 nav-038, 1 nav-037, 1 ecp-014, 1 pwr-001 | 1 nav-040 | — |
| grind a star tracker lens | nav.sensorbay | 90 | 1 cer-021, 1 lgt-006, 1 pwr-001 | 1 nav-041 | — |
| build a star tracker camera head | nav.sensorbay | 120 | 1 lgt-035, 1 nav-041, 1 ecp-007, 1 pwr-001 | 1 nav-042 | — |
| build a reaction wheel | nav.gyrobench | 150 | 1 nav-033, 1 mec-010, 1 ecp-046, 1 pwr-001 | 1 nav-043 | — |
| draw radar waveguides | nav.sensorbay | 60 | 1 met-053, 1 pwr-001 | 2 nav-044 | — |
| build a radar antenna array | nav.sensorbay | 90 | 2 met-006, 1 nav-044, 1 ecp-033, 1 pwr-001 | 1 nav-045 | — |
| form a radar dish | nav.sensorbay | 120 | 1 met-007, 1 cer-073, 1 nav-044, 1 pwr-001 | 1 nav-046 | — |
| build a radar transceiver | nav.sensorbay | 140 | 1 ecp-062, 1 ecp-061, 1 nav-045, 1 pwr-001 | 1 nav-047 | — |
| build a radar unit | nav.sensorbay | 200 | 1 nav-046, 1 nav-047, 1 ecp-007, 1 pwr-001 | 1 nav-048 | — |
| build a lidar optics head | nav.sensorbay | 100 | 1 lgt-031, 1 lgt-029, 1 lgt-007, 1 pwr-001 | 1 nav-049 | — |
| build a lidar laser module | nav.sensorbay | 120 | 2 lgt-033, 1 ecp-063, 1 pwr-001 | 1 nav-050 | — |
| build a lidar unit | nav.sensorbay | 200 | 1 nav-049, 1 nav-050, 1 ecp-007, 1 cer-083, 1 pwr-001 | 1 nav-051 | — |
| build proximity pingers | nav.sensorbay | 80 | 1 nav-044, 1 ecp-061, 1 lgt-054, 1 pwr-001 | 2 nav-052 | — |
| make beacon housings | nav.sensorbay | 50 | 1 pol-045, 1 met-007, 1 pwr-001 | 2 nav-053 | — |
| build a beacon transmitter | nav.sensorbay | 100 | 1 ecp-061, 1 ecp-013, 1 met-006, 1 pwr-001 | 1 nav-054 | — |
| build a nav beacon | nav.sensorbay | 140 | 1 nav-053, 1 nav-054, 1 pwr-006, 1 lgt-054, 1 pwr-001 | 1 nav-055 | — |
| build a relay beacon | nav.sensorbay | 200 | 1 nav-055, 1 nav-054, 1 ecp-050, 1 pwr-001 | 1 nav-056 | — |
| build chronometer movements | nav.gyrobench | 60 | 1 ecp-013, 1 ecp-060, 1 mec-003, 1 pwr-001 | 2 nav-057 | — |
| case a chronometer | nav.gyrobench | 120 | 1 nav-057, 1 cer-016, 1 met-034, 1 pwr-001 | 1 nav-058 | — |
| build an optical sextant | nav.gyrobench | 150 | 2 nav-060, 1 met-036, 1 lgt-006, 1 pwr-001 | 1 nav-059 | — |
| cut horizon mirrors | nav.sensorbay | 60 | 1 cer-024, 1 pwr-001 | 2 nav-060 | — |
| make a hand compass | any.bench | 40 | 1 met-077, 1 pol-045, 1 cer-001 | 1 nav-061 | — |
| make navigator pencils | any.bench | 20 | 1 ore-074, 1 pak-057 | 4 nav-062 | — |
| bind a navigator notebook | any.bench | 30 | 2 nav-006, 1 nav-062 | 1 nav-063 | — |
| flash a bootloader image | nav.coderoom | 60 | 1 nav-009, 1 ecp-040, 1 pwr-001 | 1 nav-064 | — |
| build a kernel image | nav.coderoom | 90 | 1 nav-064, 1 nav-009, 1 pwr-001 | 1 nav-065 | — |
| build a driver library | nav.coderoom | 90 | 1 nav-064, 1 nav-009, 1 ecp-047, 1 pwr-001 | 1 nav-066 | — |
| build an operating system image | nav.coderoom | 200 | 1 nav-065, 1 nav-066, 1 nav-069, 1 pwr-001 | 1 nav-067 | — |
| build a database engine | nav.coderoom | 140 | 1 nav-065, 1 nav-066, 1 nav-009, 1 pwr-001 | 1 nav-068 | — |
| build a compression codec | nav.coderoom | 120 | 1 nav-066, 1 nav-009, 1 pwr-001 | 1 nav-069 | — |
| build a diagnostics suite | nav.coderoom | 130 | 1 nav-065, 1 ecp-047, 1 pwr-001 | 1 nav-070 | — |
| build a network stack | nav.coderoom | 140 | 1 nav-066, 1 ecp-050, 1 pwr-001 | 1 nav-071 | — |
| write a backup image | nav.coderoom | 120 | 1 nav-075, 1 nav-065, 1 pwr-001 | 1 nav-072 | — |
| burn a boot rom card | nav.coderoom | 50 | 1 nav-064, 1 ecp-040, 1 pwr-001 | 1 nav-073 | — |
| write a telemetry card | nav.coderoom | 60 | 1 nav-009, 1 ecp-047, 1 pwr-001 | 1 nav-074 | — |
| build an archive card | nav.corebay | 90 | 2 nav-009, 1 ecp-009, 1 pwr-001 | 1 nav-075 | — |
| build a log recorder module | nav.corebay | 130 | 1 nav-074, 1 ecp-054, 1 cer-083, 1 pwr-001 | 1 nav-076 | — |
| build a flight recorder module | nav.corebay | 150 | 1 nav-075, 1 nav-074, 1 met-034, 1 pwr-001 | 1 nav-077 | — |
| rack a storage array | nav.corebay | 170 | 3 nav-075, 1 ecp-068, 1 ecp-067, 1 pwr-001 | 1 nav-078 | — |
| rack a mass storage cluster | nav.corebay | 240 | 1 nav-078, 1 nav-076, 1 nav-004, 1 pwr-001 | 1 nav-079 | — |
| build a network switch board | nav.corebay | 150 | 2 ecp-050, 1 ecp-051, 1 nav-071, 1 pwr-001 | 1 nav-080 | — |
| build a ship bus controller | nav.corebay | 200 | 1 nav-080, 1 nav-071, 1 pwr-016, 1 nav-004, 1 pwr-001 | 1 nav-081 | — |
| rack a cluster node | nav.corebay | 220 | 1 nav-004, 1 nav-078, 1 nav-080, 1 pwr-001 | 1 nav-082 | — |
| rack a compute rack | nav.corebay | 240 | 2 ecp-069, 1 nav-068, 1 thm-059, 1 pwr-001 | 1 nav-083 | — |
| pair a redundant core module | nav.corebay | 240 | 2 nav-004, 1 ecp-045, 1 pwr-001 | 1 nav-084 | — |
| build an autonomic controller | nav.corebay | 300 | 1 nav-084, 1 nav-068, 1 nav-070, 1 ecp-014, 1 pwr-001 | 1 nav-085 | — |
| build a nav computer | nav.plotter | 240 | 1 nav-004, 1 nav-010, 1 nav-040, 1 ecp-041, 1 pwr-001 | 1 nav-087 | — |
| build a bridge terminal unit | nav.corebay | 120 | 1 ecp-041, 1 ecp-042, 1 ecp-052, 1 cer-083, 1 pwr-001 | 1 nav-088 | — |
| make a chart press roller | any.bench | 60 | 1 pol-003, 1 met-008 | 1 nav-089 | — |
| make a plotter stylus head | any.bench | 40 | 1 met-049, 1 pol-047 | 1 nav-090 | — |
| make a gyro bench jig | any.bench | 60 | 1 met-005, 1 mec-005 | 1 nav-091 | — |
| wire a sensor bay cooling fan | any.bench | 60 | 1 mec-009, 1 pwr-005 | 1 nav-092 | — |
| bend rack slot guides | any.bench | 40 | 1 met-007, 1 pol-047 | 2 nav-093 | — |
| wire a firmware debug probe | any.bench | 60 | 1 ecp-007, 1 ecp-016 | 1 nav-094 | — |
| assemble a chart press kit | any.bench | 120 | 1 fur-001, 1 nav-089, 1 mec-010 | 1 nav-095 | — |
| assemble a course plotter kit | any.bench | 160 | 1 fur-001, 1 nav-090, 1 ecp-052, 1 ecp-041 | 1 nav-096 | — |
| assemble a gyro bench kit | any.bench | 120 | 1 fur-001, 1 nav-091, 1 mec-010 | 1 nav-097 | — |
| assemble a sensor mast bay kit | any.bench | 180 | 2 fur-001, 1 nav-092, 1 lgt-036 | 1 nav-098 | — |
| assemble a core integration bay kit | any.bench | 180 | 2 fur-001, 1 nav-093, 1 ecp-068 | 1 nav-099 | — |
| assemble a firmware lab kit | any.bench | 120 | 1 fur-001, 1 nav-094, 1 ecp-052 | 1 nav-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| nav.chartpress | Press that prints chart sheet into charts, maps, tables and cards, binds folios and ledgers, and pulps stale paper. | Paper stock is metered. Unpulped waste is charged to the station. Ref 2207/N. |
| nav.plotter | Plotting table that draws courses and burn plans, compiles the atlas and assembles the nav computer. | Stylus calibrated, rev 9. Drift within tolerance. Tolerance revised upward. |
| nav.gyrobench | Isolated bench for building gyros, inertial units, reaction wheels, star trackers, chronometers and sextants. | DO NOT LEAN ON BENCH WHILE ROTOR IS SPINNING. |
| nav.sensorbay | Bay for building radar, lidar, beacons, pingers and star tracker optics. | Every eye on the hull was built in here. None of them look inward. |
| nav.corebay | Rack bay that integrates core modules, storage, cluster nodes and controllers for the ship's computers. | CABLE TRAYS ARE NOT WALKWAYS. COF PROPERTY. |
| nav.coderoom | Bench for writing data cards, firmware and the software images run by the ship's computers. | Untested images are not to be racked. Proc 318 applies. Proc 318 is under revision. |
| nav-001 | Printed star chart that keeps the ship's heading true when delivered at the service hatch; dates over time. | Chart valid until superseded. Supersession is not announced. Bulletin 77/S. |
| nav-002 | Plotted course that keeps the heading true when delivered; goes stale quickly. | Plotted at first watch, wrong by third. Hand it in anyway. |
| nav-003 | Written data card that feeds the ship's computers; corrupts with age. | Unlabelled cards are wiped without review. Ref 5530/D. |
| nav-004 | Racked computer core that feeds the ship's data and forms the base of larger racks. | CORE MODULE. NOT FIELD SERVICEABLE. RETURN TO DEPOT. |
| nav-005 | Camera instrument that fixes the heading by star positions. | Boresight checked, rev 4. Lens cap removed. Lens cap lost. |
| nav-006 | Blank sheet for charts, tables, plans and notebooks; pulped back from stale paper. | Sheets are issued by count. Return the count. Form 61C. |
| nav-007 | Ink for charts, maps, cards and plans. | NOT FOR MARKING BULKHEADS. SEE NOTICE 12. |
| nav-008 | Tabulated forecast of body positions, used for plots, burns and firmware; goes stale. | Check the issue date before use. Expired tables go to pulp. Proc 205. |
| nav-009 | Empty card for data, software images and survey packs. | Blank cards remain COF property after writing. And before. |
| nav-010 | Firmware built from an ephemeris table and loaded into the nav computer. | Build 4.1.7. Checksum matched on the second attempt. |
| nav-011 | Printed map of nearby space that improves the heading slightly. | Mostly empty. Accurate about that, at least. |
| nav-012 | Bound folio of a star chart and sector maps, used for handbooks and the atlas. | Covers are carton board per cost directive 9/22. |
| nav-013 | Pocket card cut from an ephemeris table, used for turns and transfers; goes stale. | POCKET SIZE. DO NOT LAUNDER. |
| nav-014 | Reference card of catalogued stars, needed for charts and star trackers. | Every star has a number. None has a name. Same as the crew. |
| nav-015 | Clear etched overlay for plotting courses and corrections. | Align registration marks before tracing. Misregistration is reported on Form 40A. |
| nav-016 | Card marking a waypoint that improves the heading slightly; goes stale quickly. | Waypoints are set by the route office. Operators do not choose waypoints. |
| nav-017 | Ruled sheet for planning engine burns and orbit transfers. | Print run 0412. Rule spacing nonstandard. Accepted. |
| nav-018 | Planned engine burn that corrects the heading; goes stale quickly. | Fuel spent on uncorrected drift is charged to the watch on duty. Ref 3318/B. |
| nav-019 | Planned small trim to the heading; goes stale quickly. | A nudge, not a shove. The shove is scheduled for next week. |
| nav-020 | Plan for a sharp turn that improves the heading greatly but goes stale soonest of all. | SECURE LOOSE ITEMS BEFORE EXECUTION. |
| nav-021 | Table for changing orbit, also used to plan a gravity assist; goes stale. | Transfer windows listed in ship time. Proc 72 governs conversion. |
| nav-022 | Plan for a slingshot past a passing body; among the strongest heading goods, though short-lived. | Momentum borrowed from celestial bodies is not reimbursed. Legal confirms. |
| nav-023 | Record of how far the ship has drifted, used in emergency turn plans. | Position uncertain. Filed anyway. Everything is filed anyway. |
| nav-024 | Log of star sightings that improves the heading and feeds ledgers, reports and surveys. | Entries countersigned by watch officer. Watch officer position vacant. |
| nav-025 | Bound book of star fixes that keeps the heading true. | Ledgers are audited annually. Missing pages are deducted per page. |
| nav-026 | Bound handbook of a course ledger and chart folio, used for the heading and the master atlas. | Chapter 1: check the gyros. Chapter 2: see Chapter 1. |
| nav-027 | Recorded survey card that improves both the heading and the ship's data. | SURVEY DATA. COF PROPRIETARY. NOT FOR RESALE. |
| nav-028 | Larger survey with camera data that improves the heading and the data further. | Findings beyond contract scope are property of the Company. Ref 8802/S. |
| nav-029 | Bound atlas of handbook, folio, turn plan and survey; the strongest heading good. | NO BEVERAGES WITHIN 2 M OF ATLAS. |
| nav-030 | Star chart past its date, pulped back into chart sheet. | Superseded charts are not to be used for navigation, wrapping or insulation. |
| nav-031 | Course plot or burn plan past its time, pulped back into chart sheet. | Yesterday's way home. Pulp it before someone follows it. |
| nav-032 | Out-of-date ephemeris table or card, pulped back into chart sheet. | Expired. Stamped twice. Still in circulation. |
| nav-033 | Balanced rotor for gyro spin motors and reaction wheels. | BALANCED ROTOR. DROPPED UNITS ARE SCRAP. |
| nav-034 | Ring that lets a gyro turn freely, used in compasses and stabilizers. | Bearing play within limits. Limits attached. Limits smudged. |
| nav-035 | Motor that spins the rotor of a gyro compass. | Whine rises for an hour, then holds. So does the headache. |
| nav-036 | Rubber damper that isolates star trackers, stabilizers and accelerometers from vibration. | Dampers are replaced on schedule, not on complaint. Schedule 14. |
| nav-037 | Stacked accelerometers for the inertial unit. | Zeroed at bench, rev 3. Do not zero again without authority. |
| nav-038 | Spinning compass that keeps the heading true and forms the base of steadier gyros. | ALLOW 30 MIN SPIN UP BEFORE READING. |
| nav-039 | Damped gyro that holds the heading steadier. | Heading deviation beyond tolerance is logged against the duty station. |
| nav-040 | Gyro and accelerometer unit that keeps the heading and forms part of the nav computer. | Knows where the ship is without looking. Nobody asks it where the ship is going. |
| nav-041 | Ground lens for star tracker cameras. | OPTICAL SURFACE. NO FINGERS. NO BREATH. |
| nav-042 | Camera head of a star tracker. | Dark frame passed. Hot pixels mapped, count 14. |
| nav-043 | Heavy flywheel that turns the ship without propellant. | Attitude changes by reaction wheel are preferred. Propellant is billed. |
| nav-044 | Metal duct that guides radar waves in antennas, dishes and pingers. | RF HAZARD. DO NOT LOOK INTO OPEN END. |
| nav-045 | Antenna array for the radar transceiver. | Element faults are logged on Form 88K. Three faults per array are acceptable. |
| nav-046 | Formed dish reflector for the radar unit. | THIS SIDE OUTBOARD. |
| nav-047 | Transmitter and receiver at the heart of the radar unit. | Shouts into the dark all shift. Mostly the dark keeps quiet. |
| nav-048 | Complete radar that keeps the heading clear of hazards. | Collision liability rests with the station that failed to detect. Ref 6120/R. |
| nav-049 | Lens, mirror and photodiode assembly for the lidar unit. | Alignment verified, rev 2. Mirror replaced. Old mirror missing. |
| nav-050 | Paired laser diodes for the lidar unit. | LASER RADIATION. AVOID EYE EXPOSURE. CLASS 4. |
| nav-051 | Complete lidar that keeps the heading true near hazards. | Lidar returns are retained for audit. Operators may not view raw returns. |
| nav-052 | Small sounder that warns of nearby objects. | Ping, ping, ping. The fourth ping means move. |
| nav-053 | Sealed housing for a nav beacon. | COF BEACON. TAMPERING IS A CONTRACT OFFENCE. |
| nav-054 | Transmitter for nav and relay beacons. | Output tested into dummy load. Nobody answered. As expected. |
| nav-055 | Beacon that improves the heading and forms the base of a relay beacon. | Beacon identifies the vessel by registry, not by crew. Notice 31. |
| nav-056 | Beacon that relays signals, improving the heading and the data. | Repeats what it hears and adds nothing. Promoted twice. |
| nav-057 | Precision clockwork for a chronometer. | Rate checked over 72 h. Gain within allowance. |
| nav-058 | Cased chronometer that keeps time for navigation. | Ship time is Company time. Discrepancies are resolved in the Company's favour. |
| nav-059 | Sextant that fixes the heading by measuring star angles. | Three sightings per fix. Record all three. Proc 9 predates the ship. |
| nav-060 | Cut mirror for optical sextants. | Named for a horizon nobody aboard has seen. |
| nav-061 | Simple magnetic hand compass that improves the heading slightly. | Points at the drive coils. Useful if lost in the drive. |
| nav-062 | Graphite pencil for hand-drawn charts, plots and notebooks. | Pencils issued one per quarter. Shavings are recoverable carbon. |
| nav-063 | Notebook of chart sheet that improves the heading slightly. | PROPERTY OF COF. CONTENTS ALSO PROPERTY OF COF. |
| nav-064 | First code a computer runs, and the base of kernels, drivers and boot cards. | Signed, rev 11. Signing key location unknown. |
| nav-065 | Operating system core used for system images, database engines, diagnostics and backups. | Kernel faults are reported on Form 12P. Reporting does not restart the kernel. |
| nav-066 | Code that lets computers address their hardware. | Supports every device aboard except the one in front of it. |
| nav-067 | Full operating system that feeds the data and is racked into core modules. | BOOT ONLY ON APPROVED HARDWARE. |
| nav-068 | Software that stores and retrieves the ship's records, used in compute racks and controllers. | All records are retained indefinitely. Deletion requests are also recorded. |
| nav-069 | Software that packs data small, used in operating system images. | Ratio verified on test set 3. Test set 3 also compressed. |
| nav-070 | Software that checks the ship's systems, used in autonomic controllers. | All green. Run it again. Still green. Worry. |
| nav-071 | Software for the ship's network, used in switch boards and bus controllers. | Inter-capsule voice traffic is not provisioned. Packets only. |
| nav-072 | Full backup image that feeds the ship's data. | Back up weekly. Verify monthly. Restore never, by preference. Proc 51. |
| nav-073 | Card holding boot code that adds slightly to the data. | RECOVERY MEDIA. KEEP IN SLOT 0. |
| nav-074 | Card of telemetry readings, also used in log and flight recorders. | Telemetry includes station activity. Operators are reminded of this. |
| nav-075 | Dense archive card for backups, recorders and storage arrays. | Retention class 7. Wipe date to be advised. |
| nav-076 | Module that records the ship's logs. | Remembers what the watch would rather forget. |
| nav-077 | Hardened recorder of the ship's flight data. | FLIGHT RECORDER. DO NOT OPEN. RECOVER INTACT. |
| nav-078 | Racked archive cards that store a large share of the ship's data. | Fans nominal. Hum nominal. Smell under investigation. |
| nav-079 | Large storage rack that feeds the ship's data strongly. | Storage is allocated by contract tier. Station tier: minimum. |
| nav-080 | Board that links the ship's computers. | Carries every message aboard. Not one of them is the crew's. |
| nav-081 | Controller of the ship's data bus. | BUS MASTER. DO NOT POWER CYCLE UNDER LOAD. |
| nav-082 | Racked node of core module, storage array and switch board. | Nodes are interchangeable. The Company values interchangeability. |
| nav-083 | Cooled rack of computers running a database engine. | Inlet temperature high. Ticket raised. Ticket queue also high. |
| nav-084 | Two core modules paired so one survives the failure of the other. | One fails, the other carries on. Same policy as staffing. |
| nav-085 | Self-running control system of the ship; the strongest data good. | Autonomic systems reduce the need for operator judgement. Review pending. |
| nav-086 | Data card gone bad, wiped back to blank or discarded as electronic scrap. | CORRUPT. DO NOT READ. DO NOT TRUST. |
| nav-087 | Navigation computer that improves both the heading and the data. | Verify its output by hand before execution. Proc 2 is older than the computer. |
| nav-088 | Bridge terminal that adds slightly to the ship's data. | Green text, black glass. The cursor waits longer than anyone. |
| nav-089 | Spare roller for the chart press. | Replace at first streak. Streaks are reported on Form 18R. |
| nav-090 | Spare stylus head for the course plotter. | STYLUS TIP. DO NOT TEST ON SKIN. |
| nav-091 | Spare holding jig for the gyro bench. | Jig is calibrated at the depot. Field adjustment voids calibration. |
| nav-092 | Spare cooling fan for the sensor mast bay; burns out into a dead motor. | Listen for it. The silence is the fault. |
| nav-093 | Spare slot guide for the core integration bay. | Bent guide replaced. Bent guide retained for inventory. |
| nav-094 | Spare debug probe for the firmware lab. | Finds the fault. Fixing it is a separate requisition. |
| nav-095 | Packed kit that installs a chart press. | ASSEMBLE AT STATION. INSTRUCTIONS ENCLOSED. PAGE 4 MISSING. |
| nav-096 | Packed kit that installs a course plotter. | Destination not included. Destinations are assigned. Ref 1101/K. |
| nav-097 | Packed kit that installs a gyro bench. | THIS SIDE UP. HANDLE AS ROTATING EQUIPMENT. |
| nav-098 | Packed kit that installs a sensor mast bay. | Crate inspected, seal intact, one bolt short. Bolt on back order. |
| nav-099 | Packed kit that installs a core integration bay. | Installation hours are logged as productive time, subject to review. |
| nav-100 | Packed kit that installs a firmware lab. | Ships with known faults. The list of known faults ships separately. |
