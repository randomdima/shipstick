# Electronics & Computing — `ecp`

Components, boards, chips, computers and data storage. Passives are rolled from film, foil and paste; wafers are
doped, etched and diced into logic and memory dies, and packaged into chips; boards are pressed, pasted and reflowed
into controllers, drivers and supplies, then built into computers and flashed with firmware. Boards and chips go to
every device that switches, senses or lights; memory cards and drives keep the ship's `ship.data`; a personal terminal
is a tool (ECO-11), giving fun only for the minutes played on it; a faulty board or computer comes back to be mended, or
goes out as e-waste.

## Devices

| id | device | role | cells |
|---|---|---|---|
| ecp.passives | CX100 Passive Component Line | elec | 2x2 |
| ecp.waferfab | CX800 Wafer Fab | elec | 3x2 |
| ecp.packager | CX420 Chip Packager | elec | 2x2 |
| ecp.boardpress | CX300 Board Press | elec | 3x2 |
| ecp.reflow | CX250 Reflow Oven | elec | 2x1 |
| ecp.assembly | CX900 Computer Assembly Bay | elec | 3x2 |
| ecp.flasher | CX12 Firmware Flasher | elec | 1x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| ecp-001 | Resistor | — | — |
| ecp-002 | Capacitor | — | — |
| ecp-003 | Diode | — | — |
| ecp-004 | Transistor | — | — |
| ecp-005 | Board, Circuit, Bare | — | — |
| ecp-006 | Circuit, Integrated | — | — |
| ecp-007 | Microcontroller | — | — |
| ecp-008 | Relay, Signal | — | — |
| ecp-009 | Chip, Memory | — | — |
| ecp-010 | Board, Controller | — | — |
| ecp-011 | Diode, Light Emitting | — | — |
| ecp-012 | Inductor | — | — |
| ecp-013 | Oscillator, Crystal | — | — |
| ecp-014 | Processor | — | — |
| ecp-015 | Connector, Board | — | — |
| ecp-016 | Cable, Ribbon | — | — |
| ecp-017 | Wire, Solder | — | — |
| ecp-018 | Paste, Solder | — | 720 h |
| ecp-019 | Paste, Flux | — | — |
| ecp-020 | Laminate, Copper Clad | — | — |
| ecp-021 | Wafer, Polished | — | — |
| ecp-022 | Wafer, Doped | — | — |
| ecp-023 | Wafer, Etched | — | — |
| ecp-024 | Die, Logic | — | — |
| ecp-025 | Die, Memory | — | — |
| ecp-026 | Frame, Lead | — | — |
| ecp-027 | Wire, Bond | — | — |
| ecp-028 | Photoresist | — | 500 h |
| ecp-029 | Slurry, Dielectric | — | — |
| ecp-030 | Film Stock, Carbon | — | — |
| ecp-031 | Electrolyte, Capacitor | — | 1000 h |
| ecp-032 | Foil, Capacitor | — | — |
| ecp-033 | Board, Multilayer | — | — |
| ecp-034 | Circuit, Flexible | — | — |
| ecp-035 | Module, Power Transistor | — | — |
| ecp-036 | Bridge, Rectifier | — | — |
| ecp-037 | Chip, Linear Regulator | — | — |
| ecp-038 | Fuse, Board | — | — |
| ecp-039 | Chip, Flash | — | — |
| ecp-040 | Chip, Firmware | — | — |
| ecp-041 | Panel, Display | — | — |
| ecp-042 | Keypad | — | — |
| ecp-043 | Screen, Touch | — | — |
| ecp-044 | Module, Speaker | — | — |
| ecp-045 | Supply, Power | — | — |
| ecp-046 | Board, Motor Driver | — | — |
| ecp-047 | Board, Sensor Interface | — | — |
| ecp-048 | Board, Lamp Driver | — | — |
| ecp-049 | Board, Charge Controller | — | — |
| ecp-050 | Card, Network | — | — |
| ecp-051 | Switch, Network | — | — |
| ecp-052 | Computer, Single Board | — | — |
| ecp-053 | Card, Memory | ship.data +5 | — |
| ecp-054 | Drive, Solid State | ship.data +10 | — |
| ecp-055 | Module, Storage Array | ship.data +20 | — |
| ecp-056 | Terminal, Personal | — | 3000 h → ecp-083 |
| ecp-057 | Thermistor | — | — |
| ecp-058 | Varistor | — | — |
| ecp-059 | Optocoupler | — | — |
| ecp-060 | Chip, Timer | — | — |
| ecp-061 | Chip, Amplifier | — | — |
| ecp-062 | Chip, Signal Converter | — | — |
| ecp-063 | Chip, Gate Driver | — | — |
| ecp-064 | Chip, Power Controller | — | — |
| ecp-065 | Chip, Display Driver | — | — |
| ecp-066 | Heat Sink, Chip | — | — |
| ecp-067 | Case, Computer | — | — |
| ecp-068 | Board, Backplane | — | — |
| ecp-069 | Blade, Server | — | — |
| ecp-070 | Board, Indicator | — | — |
| ecp-071 | Board, Clock | — | — |
| ecp-072 | Switch, Toggle | — | — |
| ecp-073 | Board, Climate Controller | fits any.lifesupport, leaves 1 ecp-082 | — |
| ecp-074 | Card, Hatch Control | fits any.hatch, leaves 1 scr-003 | — |
| ecp-075 | Regulator, Solar Strip | fits any.solarstrip, leaves 1 scr-003 | — |
| ecp-076 | Board, Condenser Control | fits any.condenser, leaves 1 ecp-082 | — |
| ecp-077 | Iron, Soldering | fits any.bench, fits ecp.reflow | 2000 h → scr-004 |
| ecp-078 | Multimeter | fits any.bench | 4000 h → scr-004 |
| ecp-079 | Probe, Logic | fits ecp.flasher | 3000 h → scr-004 |
| ecp-080 | Oscilloscope | fits ecp.assembly | 5000 h → scr-004 |
| ecp-081 | Pump, Desoldering | fits any.bench | 2000 h → scr-004 |
| ecp-082 | Board, Circuit, Faulty | — | — |
| ecp-083 | Computer, Faulty | — | — |
| ecp-084 | Wafer, Rejected | — | — |
| ecp-085 | Dross, Solder | — | — |
| ecp-086 | Etch Bath, Spent | — | — |
| ecp-087 | Nozzle, Component Pick | fits ecp.passives, leaves 1 scr-004 | — |
| ecp-088 | Set, Etch Mask | fits ecp.waferfab, leaves 1 scr-004 | — |
| ecp-089 | Capillary, Bonding | fits ecp.packager, leaves 1 scr-004 | — |
| ecp-090 | Plate, Board Press | fits ecp.boardpress, leaves 1 scr-001 | — |
| ecp-091 | Panel, Reflow Heater | fits ecp.reflow, leaves 1 scr-004 | — |
| ecp-092 | Driver, Bay Assembly | fits ecp.assembly, leaves 1 scr-004 | — |
| ecp-093 | Head, Programming Pogo | fits ecp.flasher, leaves 1 scr-003 | — |
| ecp-094 | Kit, Passive Component Line | installs ecp.passives | — |
| ecp-095 | Kit, Wafer Fab | installs ecp.waferfab | — |
| ecp-096 | Kit, Chip Packager | installs ecp.packager | — |
| ecp-097 | Kit, Board Press | installs ecp.boardpress | — |
| ecp-098 | Kit, Reflow Oven | installs ecp.reflow | — |
| ecp-099 | Kit, Computer Assembly Bay | installs ecp.assembly | — |
| ecp-100 | Kit, Firmware Flasher | installs ecp.flasher | — |

## Ways

| way | by | min | needs | takes | makes | gives |
|---|---|---|---|---|---|---|
| roll carbon film stock | ecp.passives | 60 | — | 1 chm-041, 1 cer-038, 1 pwr-001 | 4 ecp-030 | — |
| make resistors | ecp.passives | 45 | — | 1 ecp-030, 1 met-006, 1 pwr-001 | 10 ecp-001 | — |
| desolder board scrap | any.bench | 60 | — | 1 scr-035 | 2 ecp-001, 1 ecp-002, 1 ecp-085 | — |
| test salvaged capacitors | any.bench | 30 | — | 1 scr-039 | 2 ecp-002 | — |
| etch capacitor foil | ecp.passives | 45 | — | 1 met-039, 1 chm-009, 1 pwr-001 | 4 ecp-032 | — |
| mix capacitor electrolyte | ecp.passives | 30 | — | 1 chm-032, 1 chm-062 | 3 ecp-031 | — |
| wind electrolytic capacitors | ecp.passives | 45 | — | 1 ecp-032, 1 ecp-031, 1 pwr-001 | 8 ecp-002 | — |
| mix dielectric slurry | ecp.passives | 30 | — | 1 cer-037, 1 chm-034 | 3 ecp-029 | — |
| fire ceramic capacitors | ecp.passives | 60 | — | 1 ecp-029, 1 met-006, 1 pwr-001 | 6 ecp-002 | — |
| wind inductors | ecp.passives | 45 | — | 1 met-006, 1 pwr-075, 1 pwr-001 | 4 ecp-012 | — |
| fire thermistors | ecp.passives | 45 | — | 1 chm-073, 1 met-006, 1 pwr-001 | 6 ecp-057 | — |
| fire varistors | ecp.passives | 45 | — | 1 chm-059, 1 met-006, 1 pwr-001 | 6 ecp-058 | — |
| make board fuses | ecp.passives | 30 | — | 1 pwr-062, 1 cer-019, 1 pwr-001 | 8 ecp-038 | — |
| make toggle switches | ecp.passives | 30 | — | 1 met-051, 1 pol-045, 1 pwr-001 | 4 ecp-072 | — |
| cut crystal oscillators | ecp.passives | 60 | — | 1 cer-053, 1 met-006, 1 pwr-001 | 4 ecp-013 | — |
| wind signal relays | ecp.passives | 45 | — | 1 met-006, 1 mec-005, 1 pol-045, 1 pwr-001 | 4 ecp-008 | — |
| wind speaker modules | ecp.passives | 45 | — | 1 met-077, 1 met-006, 1 pol-002, 1 pwr-001 | 2 ecp-044 | — |
| polish wafers | ecp.waferfab | 120 | — | 1 cer-004, 1 ore-082, 1 pwr-001 | 4 ecp-021, 1 ecp-084 | — |
| repolish rejected wafers | ecp.waferfab | 90 | — | 2 ecp-084, 1 ore-082, 1 pwr-001 | 1 ecp-021 | — |
| mix photoresist | ecp.waferfab | 30 | — | 1 pol-025, 1 chm-033 | 3 ecp-028 | — |
| dope wafers | ecp.waferfab | 120 | — | 2 ecp-021, 1 chm-022, 1 pwr-001 | 2 ecp-022 | — |
| etch wafers | ecp.waferfab | 90 | — | 2 ecp-022, 1 ecp-028, 1 chm-052, 1 pwr-001 | 2 ecp-023, 1 ecp-086 | — |
| dice logic dies | ecp.waferfab | 60 | — | 1 ecp-023, 1 pwr-001 | 6 ecp-024, 1 ecp-084 | — |
| dice memory dies | ecp.waferfab | 60 | — | 1 ecp-023, 1 pwr-001 | 6 ecp-025, 1 ecp-084 | — |
| dice discrete devices | ecp.waferfab | 60 | — | 1 ecp-022, 1 pwr-001 | 8 ecp-003, 8 ecp-004 | — |
| grow light emitting dies | ecp.waferfab | 90 | — | 1 ecp-022, 1 chm-076, 1 pwr-001 | 8 ecp-011 | — |
| reclaim etch bath | ecp.waferfab | 60 | — | 2 ecp-086, 1 pwr-001 | 1 chm-052, 1 scr-008 | — |
| make an etch mask set | ecp.waferfab | 90 | — | 1 cer-021, 1 ecp-028, 1 pwr-001 | 1 ecp-088 | — |
| stamp lead frames | ecp.packager | 30 | — | 1 met-037, 1 pwr-001 | 10 ecp-026 | — |
| draw bond wire | ecp.packager | 30 | — | 1 met-006, 1 pwr-001 | 10 ecp-027 | — |
| stamp chip heat sinks | ecp.packager | 30 | — | 1 met-076, 1 pwr-001 | 4 ecp-066 | — |
| package integrated circuits | ecp.packager | 60 | — | 2 ecp-024, 2 ecp-026, 1 ecp-027, 1 pol-007 | 2 ecp-006 | — |
| pick salvaged chips | any.bench | 60 | — | 1 scr-038 | 1 ecp-006, 1 ecp-009 | — |
| package memory chips | ecp.packager | 60 | — | 2 ecp-025, 2 ecp-026, 1 ecp-027, 1 pol-007 | 2 ecp-009 | — |
| package microcontrollers | ecp.packager | 60 | — | 1 ecp-024, 1 ecp-025, 1 ecp-026, 1 ecp-027, 1 pol-007 | 1 ecp-007 | — |
| package a processor | ecp.packager | 90 | — | 3 ecp-024, 1 ecp-066, 1 ecp-026, 1 ecp-027 | 1 ecp-014 | — |
| package flash chips | ecp.packager | 60 | — | 2 ecp-025, 1 ecp-026, 1 pol-007 | 2 ecp-039 | — |
| package analog chips | ecp.packager | 60 | — | 2 ecp-024, 2 ecp-026, 1 ecp-027, 1 pol-007 | 1 ecp-060, 1 ecp-061, 1 ecp-062 | — |
| package power chips | ecp.packager | 60 | — | 2 ecp-024, 1 ecp-026, 1 ecp-066 | 1 ecp-063, 1 ecp-064, 1 ecp-037 | — |
| package display drivers | ecp.packager | 60 | — | 1 ecp-024, 1 ecp-026, 1 pol-007 | 2 ecp-065 | — |
| package optocouplers | ecp.packager | 45 | — | 1 ecp-011, 1 ecp-004, 1 ecp-026, 1 pol-007 | 2 ecp-059 | — |
| build a power transistor module | ecp.packager | 60 | — | 4 ecp-004, 1 ecp-066, 1 cer-038 | 1 ecp-035 | — |
| package rectifier bridges | ecp.packager | 45 | — | 4 ecp-003, 1 ecp-026, 1 pol-007 | 2 ecp-036 | — |
| grind bonding capillaries | ecp.packager | 60 | — | 1 cer-038, 1 pwr-001 | 4 ecp-089 | — |
| press copper clad laminate | ecp.boardpress | 60 | — | 1 cer-068, 1 met-040, 1 pwr-001 | 2 ecp-020 | — |
| laminate phenolic board | ecp.boardpress | 90 | — | 1 pol-025, 1 cer-061, 1 met-040, 1 pwr-001 | 2 ecp-020 | — |
| etch circuit boards | ecp.boardpress | 60 | — | 1 ecp-020, 1 ecp-028, 1 chm-052, 1 pwr-001 | 4 ecp-005, 1 ecp-086 | — |
| etch a board by hand | any.bench | 180 | — | 1 ecp-020, 1 chm-026 | 1 ecp-005 | — |
| press multilayer boards | ecp.boardpress | 90 | — | 2 ecp-005, 1 pol-007, 1 pwr-001 | 1 ecp-033 | — |
| etch flexible circuits | ecp.boardpress | 60 | — | 1 pol-032, 1 met-040, 1 chm-052, 1 pwr-001 | 4 ecp-034, 1 ecp-086 | — |
| stamp board connectors | ecp.boardpress | 30 | — | 1 met-036, 1 pol-078, 1 pwr-001 | 6 ecp-015 | — |
| clean salvaged connectors | any.bench | 30 | — | 1 scr-037 | 2 ecp-015 | — |
| make ribbon cable | ecp.boardpress | 45 | — | 1 met-006, 1 pol-042, 1 pwr-001 | 4 ecp-016 | — |
| press a backplane board | ecp.boardpress | 60 | — | 1 ecp-033, 4 ecp-015, 1 pwr-001 | 1 ecp-068 | — |
| machine a board press plate | any.bench | 90 | — | 1 met-009 | 1 ecp-090 | — |
| mix flux paste | ecp.reflow | 20 | — | 1 chm-051, 1 pol-067 | 4 ecp-019 | — |
| mix solder paste | ecp.reflow | 20 | — | 1 met-032, 1 ecp-019 | 4 ecp-018 | — |
| draw solder wire | ecp.reflow | 30 | — | 1 met-032, 1 chm-051, 1 pwr-001 | 4 ecp-017 | — |
| refine solder dross | ecp.reflow | 60 | — | 3 ecp-085, 1 pwr-001 | 1 met-032 | — |
| reflow controller boards | ecp.reflow | 45 | — | 1 ecp-005, 1 ecp-040, 4 ecp-001, 2 ecp-002, 1 ecp-018, 1 pwr-001 | 1 ecp-010, 1 ecp-085 | — |
| hand-solder a controller board | any.bench | 120 | — | 1 ecp-005, 1 ecp-040, 2 ecp-001, 1 ecp-017 | 1 ecp-010 | — |
| repair faulty boards | ecp.reflow | 60 | — | 2 ecp-082, 1 ecp-017, 1 ecp-001, 1 ecp-002 | 1 ecp-010, 1 scr-003 | — |
| reflow a power supply unit | ecp.reflow | 60 | — | 1 ecp-005, 1 ecp-036, 1 ecp-012, 1 ecp-038, 1 pol-048, 1 ecp-018 | 1 ecp-045 | — |
| reflow motor driver boards | ecp.reflow | 45 | — | 1 ecp-005, 1 ecp-063, 1 ecp-035, 1 ecp-018 | 1 ecp-046 | — |
| reflow sensor interface boards | ecp.reflow | 45 | — | 1 ecp-005, 1 ecp-062, 1 ecp-061, 1 ecp-018 | 1 ecp-047 | — |
| reflow lamp driver boards | ecp.reflow | 45 | — | 1 ecp-005, 1 ecp-064, 1 ecp-012, 1 ecp-018 | 2 ecp-048 | — |
| reflow charge controller boards | ecp.reflow | 45 | — | 1 ecp-005, 1 ecp-064, 1 ecp-035, 1 ecp-018 | 1 ecp-049 | — |
| reflow indicator boards | ecp.reflow | 30 | — | 1 ecp-005, 4 ecp-011, 2 ecp-001, 1 ecp-018 | 2 ecp-070 | — |
| reflow clock boards | ecp.reflow | 45 | — | 1 ecp-005, 1 ecp-013, 1 ecp-060, 1 ecp-018 | 1 ecp-071 | — |
| reflow network cards | ecp.reflow | 45 | — | 1 ecp-005, 1 ecp-007, 1 ecp-059, 1 ecp-018 | 1 ecp-050 | — |
| reflow keypads | ecp.reflow | 30 | — | 1 pol-003, 1 ecp-005, 1 ecp-015, 1 ecp-006 | 2 ecp-042 | — |
| reflow solar strip regulators | ecp.reflow | 30 | — | 1 ecp-005, 1 ecp-037, 1 ecp-003, 1 ecp-018 | 2 ecp-075 | — |
| make a reflow heater panel | any.bench | 60 | — | 1 met-047, 1 cer-035 | 1 ecp-091 | — |
| assemble a display panel | ecp.assembly | 90 | — | 1 cer-016, 1 ecp-065, 1 ecp-011, 1 ecp-034 | 1 ecp-041 | — |
| refit a salvaged display | any.bench | 60 | — | 1 scr-040, 1 ecp-016 | 1 ecp-041 | — |
| laminate a touch screen | ecp.assembly | 60 | — | 1 ecp-041, 1 ecp-034, 1 ecp-062 | 1 ecp-043 | — |
| build a computer case | ecp.assembly | 60 | — | 1 met-007, 1 pol-045, 1 mec-009 | 1 ecp-067 | — |
| assemble a network switch | ecp.assembly | 60 | — | 1 ecp-033, 2 ecp-050, 1 ecp-045 | 1 ecp-051 | — |
| assemble a single board computer | ecp.assembly | 90 | — | 1 ecp-033, 1 ecp-014, 2 ecp-009, 1 ecp-071 | 1 ecp-052 | — |
| assemble memory cards | ecp.assembly | 45 | — | 2 ecp-039, 1 ecp-005, 1 pol-045 | 2 ecp-053 | — |
| assemble a solid state drive | ecp.assembly | 60 | — | 4 ecp-039, 1 ecp-007, 1 ecp-033 | 1 ecp-054 | — |
| build a server blade | ecp.assembly | 120 | — | 1 ecp-033, 2 ecp-014, 4 ecp-009, 1 ecp-045 | 1 ecp-069 | — |
| build a storage array module | ecp.assembly | 180 | — | 4 ecp-054, 1 ecp-068, 1 ecp-069, 1 ecp-051, 1 ecp-067 | 1 ecp-055 | — |
| build a personal terminal | ecp.assembly | 120 | — | 1 ecp-052, 1 ecp-041, 1 ecp-042, 1 ecp-044, 1 ecp-067, 1 ecp-016 | 1 ecp-056 | — |
| play games on the personal terminal | crew | 60 | 1 ecp-056 | 1 pwr-001 | — | fun +28, stress -5 |
| repair a faulty computer | ecp.assembly | 90 | — | 1 ecp-083, 1 ecp-010, 1 ecp-009 | 1 ecp-056, 1 ecp-082 | — |
| strip a faulty computer | any.bench | 30 | — | 1 ecp-083 | 1 scr-003, 1 scr-001 | — |
| assemble a climate controller board | ecp.assembly | 45 | — | 1 ecp-010, 1 ecp-057, 1 ecp-008 | 1 ecp-073 | — |
| assemble a hatch control card | ecp.assembly | 45 | — | 1 ecp-010, 1 ecp-008, 1 ecp-070 | 1 ecp-074 | — |
| assemble a condenser control board | ecp.assembly | 45 | — | 1 ecp-010, 1 ecp-058 | 1 ecp-076 | — |
| build a soldering iron | ecp.assembly | 45 | — | 1 met-047, 1 pol-045, 1 ecp-057 | 1 ecp-077 | — |
| build a multimeter | ecp.assembly | 60 | — | 1 ecp-062, 1 ecp-041, 1 pol-045 | 1 ecp-078 | — |
| build a logic probe | ecp.assembly | 45 | — | 1 ecp-061, 1 ecp-011, 1 pol-045 | 1 ecp-079 | — |
| build an oscilloscope | ecp.assembly | 120 | — | 1 ecp-062, 1 ecp-041, 1 ecp-014 | 1 ecp-080 | — |
| make a desoldering pump | any.bench | 30 | — | 1 mec-005, 1 pol-008 | 1 ecp-081 | — |
| make a bay assembly driver | ecp.assembly | 60 | — | 1 mec-010, 1 ecp-046 | 1 ecp-092 | — |
| turn component pick nozzles | any.bench | 45 | — | 1 met-034, 1 pol-009 | 2 ecp-087 | — |
| flash firmware chips | ecp.flasher | 20 | — | 1 ecp-007, 1 pwr-001 | 1 ecp-040 | — |
| make a programming pogo head | ecp.flasher | 45 | — | 1 met-036, 1 mec-005, 1 ecp-005 | 1 ecp-093 | — |
| pack a passive line kit | ecp.assembly | 180 | — | 1 cer-083, 1 ecp-087, 1 ecp-010, 1 mec-043, 1 pak-061 | 1 ecp-094 | — |
| pack a wafer fab kit | ecp.assembly | 240 | — | 1 cer-083, 1 ecp-088, 1 ecp-052, 1 mec-042, 1 pak-034, 1 pak-070 | 1 ecp-095 | — |
| pack a chip packager kit | ecp.assembly | 180 | — | 1 cer-083, 1 ecp-089, 1 ecp-010, 1 mec-043, 1 pak-034 | 1 ecp-096 | — |
| pack a board press kit | ecp.assembly | 180 | — | 1 met-074, 1 ecp-090, 1 ecp-010, 1 mec-012, 1 pak-060 | 1 ecp-097 | — |
| pack a reflow oven kit | ecp.assembly | 150 | — | 1 cer-083, 1 ecp-091, 1 ecp-010, 1 mec-009, 1 pak-061 | 1 ecp-098 | — |
| pack a computer assembly bay kit | ecp.assembly | 180 | — | 1 cer-083, 1 ecp-092, 1 ecp-043, 1 ecp-052, 1 pak-061 | 1 ecp-099 | — |
| pack a firmware flasher kit | ecp.assembly | 120 | — | 1 cer-083, 1 ecp-093, 1 ecp-052, 1 ecp-016, 1 pak-034, 1 pak-070 | 1 ecp-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| ecp.passives | Makes resistors, capacitors, inductors, relays, fuses, switches, crystals and speakers. | Component yield is reported per shift. Low yield is reported per operator. |
| ecp.waferfab | Polishes, dopes, etches and dices wafers into logic and memory dies, diodes, transistors and light-emitting dies. | CLEAN AREA. PERSONNEL ARE THE PRIMARY CONTAMINANT. GOWN UP. |
| ecp.packager | Packages bare dies into chips, processors and power modules, and makes lead frames, bond wire and heat sinks. | Bond head aligned, rev 11. Drift observed after lunch. Lunch not identified as cause. |
| ecp.boardpress | Presses and etches laminate into circuit boards, multilayer boards, flexible circuits, connectors and ribbon cable. | Etchant is a controlled substance. Usage is reconciled against output. Ref 7720/E. |
| ecp.reflow | Solders components onto boards to make controllers, drivers and power supplies, and mixes solder and flux. | Heat profile is locked. Profile key held off-station. Do not request it. |
| ecp.assembly | Builds displays, computers, storage, terminals, test gear and control cards, and packs electronics kits. | STATIC SENSITIVE AREA. WRIST STRAP ON BEFORE CONTACT. |
| ecp.flasher | Flashes firmware onto microcontrollers. | Do not interrupt power during write. Interrupted units are charged to the station. |
| ecp-001 | Basic component that limits current, for controller and indicator boards. | Colour code chart taped inside panel door. Two bands faded. Guess within tolerance. |
| ecp-002 | Component that stores charge to smooth power on controller boards and sensors. | OBSERVE POLARITY. REVERSED PARTS VENT WITHOUT WARNING. |
| ecp-003 | One-way component for rectifier bridges and solar strip regulators. | Current flows one way only. Policy on most other matters is similar. |
| ecp-004 | Switching component for power modules and optocouplers. | Standard switching part, Type 2. Substitutes approved only by Form 40T. |
| ecp-005 | Bare etched board on which controllers, drivers and other electronics are built. | Handle by edges. Fingerprints on copper are logged as contamination. |
| ecp-006 | General-purpose chip for keypads and print heads. | Part marking under magnification only. Magnifier issued one per three stations. |
| ecp-007 | Small programmable chip that runs heaters, timers, bots and toys, and is flashed into firmware chips. | Blank units carry no instructions. The Company finds this restful. |
| ecp-008 | Electrically switched contact for thermostats, valves, hatches and lamps. | Contact chatter heard on energise, rev 3. Monitored. Still chattering. |
| ecp-009 | Working memory for computers, readers and archive cards. | Data held in Company memory is Company data. Proc 500, records. |
| ecp-010 | Programmed control board at the heart of most machine kits and control cards. | Firmware revision on sticker. Sticker revision older than firmware. |
| ecp-011 | Light-emitting chip for lamps, indicators, strips and sensors. | GREEN: NOMINAL. AMBER: CAUTION. RED: FILE A REPORT. |
| ecp-012 | Wound coil that smooths power in power supplies and lamp drivers. | Hums at line frequency. Humming is not a fault. Notice 8, noise. |
| ecp-013 | Quartz crystal that keeps time for clocks, beacons and tuners. | Ship time is Company time. All clocks are set to it. Disputes are not entertained. |
| ecp-014 | Main computing chip for computers, navigation, trackers and controllers. | Overclocking voids the unit and the operator's bonus. Ref 1041/X. |
| ecp-015 | Plug that joins boards, readers and backplanes. | Seat fully until latched. Half-seated connectors are the leading cause of Form 77. |
| ecp-016 | Flat multi-wire cable linking displays, probes and terminals. | Red stripe to pin 1. Do not fold. Folded once, failed once. |
| ecp-017 | Flux-cored wire for hand soldering and repairs. | Heat the joint, not the solder. Read it on the reel every time. Still forget. |
| ecp-018 | Paste spread on boards before reflow; it spoils if kept too long. | STORE COLD. DATE OF OPENING ON LID. DISCARD AFTER EXPIRY. |
| ecp-019 | Cleaning paste mixed into solder paste. | Fumes are within exposure limits. Limits are posted. The fan is not. |
| ecp-020 | Copper-faced board stock, etched into circuit boards. | Sheet size standard, Grade A. Grade A stock substituted with Grade C. Noted. |
| ecp-021 | Mirror-smooth wafer, ready for doping. | Do not look into the wafer. The wafer records nothing. The Company does. |
| ecp-022 | Wafer doped for etching, discrete devices, light-emitting dies and sensor chips. | Dopant handling: Proc 61. Spill handling: Proc 62. Read 62 first. |
| ecp-023 | Patterned wafer, diced into logic and memory dies or sensor chips. | Etched wafers are high value stock. Breakage is deducted at full yield value. |
| ecp-024 | Bare logic die, packaged into chips and processors. | BARE DIE. TWEEZERS ONLY. NO BREATHING ON TRAY. |
| ecp-025 | Bare memory die, packaged into memory chips, flash chips and microcontrollers. | Dropped one. Searched the deck with a lamp for an hour. Logged as yield loss. |
| ecp-026 | Stamped frame a die is mounted in, for chips and sensor chips. | Frames issued on a strip of ten. Strip count reconciled at shift end. |
| ecp-027 | Fine wire that bonds dies to their frames. | Wire diameter below visible threshold. Spool weighed in lieu of inspection. |
| ecp-028 | Light-sensitive coating for etching wafers, boards and masks; it spoils if kept long. | LIGHT SENSITIVE. OPEN UNDER AMBER LAMP ONLY. |
| ecp-029 | Ceramic slurry, fired into capacitors. | Stir before use. Settled slurry produces settled capacitors. Rev 2. |
| ecp-030 | Coated carbon film, cut into resistors. | Film resistance tested per roll. One roll tested per batch. Batch passed. |
| ecp-031 | Liquid for wound capacitors and capacitor cells; it spoils with age. | Corrosive. Wipe spills at once. Spill wipes are issued. Burns are not covered. |
| ecp-032 | Etched foil, wound into electrolytic capacitors. | Do not crease. Creased foil is scrap. Scrap is weighed and attributed. |
| ecp-033 | Stacked board for computers, drives, network switches and radar arrays. | Inner layers not inspectable after pressing. Assume correct. Proc 88, trust. |
| ecp-034 | Thin bendable circuit for displays, touch screens and lamp strips. | MINIMUM BEND RADIUS ON DRAWING. DO NOT CREASE. |
| ecp-035 | High-current switch for motor drivers, chargers, regulators and inverters. | Heat sink compound applied, rev 1. Thermal reading high. Compound reapplied, rev 2. |
| ecp-036 | Converts alternating current into direct current, for power supplies and quench protectors. | Output polarity marked on body. Marking is the only documentation provided. |
| ecp-037 | Steadies voltage for solar strip and grid regulators. | Runs warm. Warm is normal. Hot is a Form 12R. |
| ecp-038 | Small fuse that protects power supplies. | Replace only with same rating. Wire, foil and coins are not fuses. Notice 3. |
| ecp-039 | Storage chip for memory cards, drives, media cards and game cartridges. | Write cycles are finite. The Company has budgeted for exactly enough of them. |
| ecp-040 | Flashed microcontroller that holds a controller's program, for boards and navigation. | Firmware is licensed, not sold. Reverse engineering is a breach of contract. |
| ecp-041 | Screen for terminals, scanners, monitors and navigation. | Burn-in from the shift roster visible on screen. Roster has since changed. |
| ecp-042 | Button pad for terminals and consoles. | Keys 0 and ENTER worn blank. Operators have adapted. |
| ecp-043 | Touch-sensitive display, built into the computer assembly bay. | Clean with approved wipe only. Sleeves are not approved wipes. |
| ecp-044 | Small speaker for terminals, alarms and sound players. | Alarm tones are fixed by standard. Custom tones are disabled at flash. |
| ecp-045 | Converts ship power for computers, network switches, thrusters and labs. | HIGH VOLTAGE INSIDE. NO USER SERVICEABLE PARTS. ALL USERS ARE PERSONNEL. |
| ecp-046 | Drives motors in machine kits, drones, massagers and reaction wheels. | Driver output tested at no load. Load testing is the field's responsibility. |
| ecp-047 | Reads sensors for panels, alarms, hull sections and survey kits. | Sensor data is forwarded to the Company. Forwarding cannot be disabled. |
| ecp-048 | Powers lamps, light panels and sterilizers. | Dimming range limited at flash to conserve power. Notice 22, lighting. |
| ecp-049 | Manages battery charging for packs, lanterns and shields. | Charge cut off at full. Overriding the cut-off is the last thing some operators did. |
| ecp-050 | Network card that links a device to the ship's network. | Device traffic only. Voice traffic between stations is not provisioned. Proc 1. |
| ecp-051 | Joins network cards into a ship network. | All traffic passes through Company switching. All traffic is retained. |
| ecp-052 | Complete small computer for terminals, drones, scanners and archives. | Asset tag on underside. Removal of asset tag is reported automatically. |
| ecp-053 | Plug-in storage that adds to the ship's data. | Label every card. Unlabelled cards are wiped at audit without review. |
| ecp-054 | Drive that adds more to the ship's data than a card, used in archives and log recorders. | LOG MEDIA. COF RECORDS. DO NOT ERASE, REFORMAT OR REUSE. |
| ecp-055 | Rack of drives and servers that adds the most to the ship's data. | Retention schedule: permanent. Deletion requests: Form 99Z, never processed. |
| ecp-056 | Personal computer for playing games, which gives fun and eases stress; it fails eventually. | Recreational use logged and deducted from rest allowance. Ref 3300/G. |
| ecp-057 | Temperature-sensing part for probes, soldering irons and climate controller boards. | Reads two degrees low, rev 6. Climate set two degrees high to match. |
| ecp-058 | Surge protector for condenser boards and quench protectors. | Sacrificial part. Sacrifice is expected and budgeted. |
| ecp-059 | Light-linked isolator for network cards. | Signal crosses the gap by light only. No direct contact. Like the stations. |
| ecp-060 | Timing chip for clocks, timers, lamps and alarms. | Shift timers are synchronised fleet-wide. Personal timers are not. |
| ecp-061 | Boosts weak signals for sensors, speakers and detectors. | GAIN SET AT FACTORY. DO NOT ADJUST TRIM POT. |
| ecp-062 | Converts analog signals into data, for sensors, meters and screens. | Every reading is a number. Every number is reviewed. Eventually. |
| ecp-063 | Drives power switches in motor boards, lasers and igniters. | Dead time set conservatively. Dead time is the only kind the Company endorses. |
| ecp-064 | Controls power in lamp drivers and charge controllers. | Power allocation follows Company priority. Cabin comfort is priority nine. |
| ecp-065 | Drives the pixels of displays and e-paper. | Dead pixel count within tolerance, rev 4. Tolerance is twelve. Count is eleven. |
| ecp-066 | Metal fins that cool processors and power chips. | HOT SURFACE. FINS SHARP. DO NOT USE AS HAND WARMER. |
| ecp-067 | Fan-cooled housing for terminals, servers and core modules. | Case screws are security pattern. Driver held off-station. Proc 404, access. |
| ecp-068 | Board that links racked modules in storage arrays and core bays. | Slot 7 unused since commissioning. Nobody knows what it was for. |
| ecp-069 | Rack computer for storage arrays and the core bay. | Uptime is a performance metric. Reboots are justified in writing. |
| ecp-070 | Board of status lamps for thermometers and status displays. | Lamp test daily. A lamp that does not light is reported as a lamp, not a fault. |
| ecp-071 | Timekeeping board for computers and wall clocks. | Clock drift corrected nightly from Company time signal. Personal time is not kept. |
| ecp-072 | Panel toggle switch for lamps and timers. | Up is on. Except on panels fitted before rev 4. Check the label. |
| ecp-073 | Control board that restores the life support unit's controls, leaving a faulty board. | Setpoint is fixed by contract. Cabin temperature complaints go to Form 6C. |
| ecp-074 | Control card that restores a hatch's controls. | HATCH CONTROL. LOCK OUT BEFORE REPLACEMENT. |
| ecp-075 | Regulator that restores a solar strip's regulation. | Output capped at rated figure. Surplus light is not recognised as income. |
| ecp-076 | Control board that restores a condenser's controls, leaving a faulty board. | Board swapped, rev 2. Condenser drips again. Old board in the e-waste bin, labelled. |
| ecp-077 | Soldering tool for the bench or reflow oven; wears out into broken parts. | Hold by handle. Return to stand. The stand is not optional. Proc 6. |
| ecp-078 | Bench meter for checking circuits. | Leads frayed at the tip. Readings trusted anyway. No alternative issued. |
| ecp-079 | Probe that checks signals at the firmware flasher. | HIGH, LOW, OR FLOATING. FLOATING IS A FAULT. |
| ecp-080 | Signal scope for the computer assembly bay. | Calibration sticker expired. Waveforms appear plausible. Accepted. |
| ecp-081 | Hand pump that removes molten solder from joints at the bench. | Empty solder chamber after use. Full chambers spray on the next stroke. |
| ecp-082 | Failed board, repaired into a controller board or stripped for chips. | Fault tag attached. Fault description: does not work. Diagnosis pending. |
| ecp-083 | Failed personal terminal, repaired, stripped or sorted for parts. | Power cycled twice per Proc 1. Still faulty. Return to assembly bay. |
| ecp-084 | Off-spec wafer or dicing loss, repolished into a fresh wafer. | REJECT. DO NOT PROCESS. ROUTE TO REPOLISH. |
| ecp-085 | Skimmed solder waste, refined back into solder. | Dross is recoverable metal. Disposal of dross as waste is a stores offence. |
| ecp-086 | Used etchant, reclaimed for fresh etchant and copper. | SPENT ETCHANT. CORROSIVE. COPPER BEARING. DO NOT DRAIN. |
| ecp-087 | Spare pick nozzle that repairs a passive component line. | Vacuum tip worn oval. Parts placed at an angle. Replace. |
| ecp-088 | Spare etch masks that repair a wafer fab. | One particle on a mask ruins every wafer after it. Inspect. Inspect again. |
| ecp-089 | Spare bonding capillary that repairs a chip packager. | Ceramic tip. Fragile. Replacement interval set by Company, not by wear. |
| ecp-090 | Spare press plate that repairs a board press. | Flatness verified, rev 3. Verification tool is the plate itself. |
| ecp-091 | Spare heater panel that repairs a reflow oven. | No glow, no flow. Panel replaced hot by previous shift. Burn noted on file. |
| ecp-092 | Spare screw driver unit that repairs a computer assembly bay. | Torque limited to protect boards. Boards are dearer than operators. Ref 0002/B. |
| ecp-093 | Spare pogo pin head that repairs a firmware flasher. | Spring pins wear with each contact. Contacts counted by flasher, not by personnel. |
| ecp-094 | Crated parts that install a passive component line. | Contents rattle in transit. Rattle is within shipping tolerance. |
| ecp-095 | Crated parts that install a wafer fab. | OPEN IN CLEAN AIR ONLY. DESICCANT INSIDE. DO NOT EAT. |
| ecp-096 | Crated parts that install a chip packager. | Static bag inside static bag inside crate. Each layer signed for separately. |
| ecp-097 | Crated parts that install a board press. | Heavy plate inside. Two-person lift. Second person not supplied. |
| ecp-098 | Crated parts that install a reflow oven. | Run one empty cycle before first batch. Proc 21. Empty cycles are billed as power. |
| ecp-099 | Crated parts that install a computer assembly bay. | Built in one bay, shipped to another. Neither bay is told where. |
| ecp-100 | Crated parts that install a firmware flasher. | Ships with bootloader, licence card and a notice that the licence is revocable. |
