# Lighting & Sensors — `lgt`

Lamps, grow lights, sensors and optics. Glass is blown into envelopes, tubes and ampoules, filaments wound, LEDs
mounted on strips, and reflectors, lenses and diffusers ground and polished; lamps and panels are assembled from them,
and sensing elements are mounted and calibrated into probes and sensors. A lamp holds `cabin.light` while it sits in
its fixture and burns out in the end: a bulb or tube into one to be reclaimed here, an LED lamp into e-waste. Grow
lights go to the farms, sensors to every device that measures and to the fixtures that wear them, and lenses and laser
diodes to the bridge.

## Devices

| id | device | role | cells |
|---|---|---|---|
| lgt.glassline | LX110 Bulb Glass Line | elec | 2x2 |
| lgt.ledline | LX220 LED Line | elec | 2x2 |
| lgt.lampbay | LX500 Lamp Assembly Bay | elec | 3x2 |
| lgt.optics | LX40 Optics Bench | elec | 2x1 |
| lgt.sensorlab | LX700 Sensor Lab | elec | 2x1 |
| lgt.calstation | LX750 Calibration Station | elec | 2x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| lgt-001 | Bulb, Lamp | cabin.light +2/h | 400 h → lgt-075 |
| lgt-002 | Strip, LED | — | — |
| lgt-003 | Light, Grow | cabin.light +4/h | 2000 h → scr-003 |
| lgt-004 | Panel, Light | cabin.light +3/h | 3000 h → scr-003 |
| lgt-005 | Flashlight | cabin.light +1/h | 300 h → scr-004 |
| lgt-006 | Lens, Glass | — | — |
| lgt-007 | Photodiode | — | — |
| lgt-008 | Probe, Temperature | — | — |
| lgt-009 | Sensor, Pressure | — | — |
| lgt-010 | Sensor, Gas | — | — |
| lgt-011 | Envelope, Glass | — | — |
| lgt-012 | Filament, Tungsten | — | — |
| lgt-013 | Cap, Lamp | — | — |
| lgt-014 | Phosphor, Lamp | — | — |
| lgt-015 | Phosphor, Full Spectrum | — | — |
| lgt-016 | Reflector, Polished | — | — |
| lgt-017 | Sheet, Diffuser | — | — |
| lgt-018 | Heat Sink, Lamp | — | — |
| lgt-019 | Cap, LED Lens | — | — |
| lgt-020 | Strip, LED Carrier | — | — |
| lgt-021 | Tube, UV | — | — |
| lgt-022 | Cover, Glass, Frosted | — | — |
| lgt-023 | Housing, Reflector | — | — |
| lgt-024 | Guide, Light | — | — |
| lgt-025 | Frame, Panel | — | — |
| lgt-026 | Fill, Chemlight | — | — |
| lgt-027 | Ampoule, Glass | — | — |
| lgt-028 | Fibre, Optical | — | — |
| lgt-029 | Mirror, Optical | — | — |
| lgt-030 | Prism | — | — |
| lgt-031 | Lens, Spot Beam | — | — |
| lgt-032 | Lens, Fresnel | — | — |
| lgt-033 | Diode, Laser | — | — |
| lgt-034 | Socket, Lamp | — | — |
| lgt-035 | Chip, Image Sensor | — | — |
| lgt-036 | Module, Camera | — | — |
| lgt-037 | Sensor, Infrared | — | — |
| lgt-038 | Element, Sensing | — | — |
| lgt-039 | Cell, Diaphragm | — | — |
| lgt-040 | Thermocouple | — | — |
| lgt-041 | Gauge, Strain | — | — |
| lgt-042 | Cell, Load | — | — |
| lgt-043 | Sensor, Hall | — | — |
| lgt-044 | Sensor, Light | — | — |
| lgt-045 | Sensor, Motion | — | — |
| lgt-046 | Sensor, Flow | — | — |
| lgt-047 | Sensor, Level | — | — |
| lgt-048 | Sensor, Humidity | — | — |
| lgt-049 | Sensor, Carbon Dioxide | — | — |
| lgt-050 | Sensor, Oxygen | — | — |
| lgt-051 | Sensor, Smoke | — | — |
| lgt-052 | Capsule, Microphone | — | — |
| lgt-053 | Accelerometer | — | — |
| lgt-054 | Lamp, Indicator | — | — |
| lgt-055 | Lamp, Night | cabin.light +1/h | 1500 h → lgt-075 |
| lgt-056 | Lamp, Reading | cabin.light +2/h | 800 h → lgt-075 |
| lgt-057 | Lamp, Ceiling | cabin.light +3/h | 1000 h → lgt-075 |
| lgt-058 | Lamp, Ceiling, LED | cabin.light +3/h | 3000 h → scr-003 |
| lgt-059 | Light, Strip | cabin.light +2/h | 3000 h → scr-003 |
| lgt-060 | Sconce, Wall | cabin.light +2/h | 1000 h → lgt-075 |
| lgt-061 | Lamp, Task | cabin.light +2/h | 1500 h → scr-003 |
| lgt-062 | Floodlight | cabin.light +5/h | 1000 h → scr-003 |
| lgt-063 | Panel, Daylight | cabin.light +4/h, stress -1/h | 3000 h → scr-003 |
| lgt-064 | Lantern, Battery | cabin.light +2/h | 200 h → scr-004 |
| lgt-065 | Lamp, Head | cabin.light +1/h | 400 h → scr-004 |
| lgt-066 | Orb, Mood Light | cabin.light +1/h, stress -1/h | 2000 h → scr-003 |
| lgt-067 | Lamp, Pendant | cabin.light +2/h | 1000 h → lgt-075 |
| lgt-068 | Lamp, Sun | cabin.light +3/h, stress -1/h | 1500 h → lgt-076 |
| lgt-069 | Lamp, UV Sterilizer | cabin.clean +2/h | 800 h → lgt-076 |
| lgt-070 | Panel, Germicidal | cabin.clean +3/h | 1200 h → lgt-076 |
| lgt-071 | Array, Grow Light | cabin.light +6/h | 2000 h → scr-003 |
| lgt-072 | Light, Seedling Rack | cabin.light +3/h | 2000 h → scr-003 |
| lgt-073 | Strip, Plant Lamp | cabin.light +2/h | 2500 h → scr-003 |
| lgt-074 | Lamp, Grow, Sodium | cabin.light +5/h | 800 h → lgt-075 |
| lgt-075 | Bulb, Lamp, Burnt Out | — | — |
| lgt-076 | Tube, UV, Burnt Out | — | — |
| lgt-077 | Stick, Glow | cabin.light +4, leaves 1 scr-002 | 2000 h → scr-002 |
| lgt-078 | Stick, Glow, Long Burn | cabin.light +8, leaves 1 scr-002 | 2000 h → scr-002 |
| lgt-079 | Wand, Emergency Light | cabin.light +12, leaves 1 scr-002 | 3000 h → scr-002 |
| lgt-080 | Pack, Cabin Air Sensor | fits any.lifesupport, leaves 1 scr-003 | — |
| lgt-081 | Probe, Condenser Level | fits any.condenser, leaves 1 scr-003 | — |
| lgt-082 | Cell, Washbasin Flow | fits any.washbasin, leaves 1 scr-003 | — |
| lgt-083 | Sensor, Toilet Tank | fits any.toilet, leaves 1 scr-003 | — |
| lgt-084 | Cell, Solar Strip Light | fits any.solarstrip, leaves 1 scr-003 | — |
| lgt-085 | Sensor, Algae Jar Light | fits any.algaejar, leaves 1 scr-003 | — |
| lgt-086 | Detector, Hatch Leak | fits any.hatch, leaves 1 scr-003 | — |
| lgt-087 | Probe, Sprouter Moisture | fits any.sprouter, leaves 1 scr-003 | — |
| lgt-088 | Loupe, Magnifier | fits any.bench, fits lgt.optics | 5000 h → scr-004 |
| lgt-089 | Crucible, Bulb Glass Line | fits lgt.glassline, leaves 1 scr-004 | — |
| lgt-090 | Nozzle, LED Placer | fits lgt.ledline, leaves 1 scr-004 | — |
| lgt-091 | Jig, Lamp Assembly Bay | fits lgt.lampbay, leaves 1 scr-004 | — |
| lgt-092 | Pad, Optics Polishing | fits lgt.optics, leaves 1 scr-005 | — |
| lgt-093 | Set, Sensor Lab Probe | fits lgt.sensorlab, leaves 1 scr-004 | — |
| lgt-094 | Cell, Calibration Gas | fits lgt.calstation, leaves 1 scr-004 | — |
| lgt-095 | Kit, Bulb Glass Line | installs lgt.glassline | — |
| lgt-096 | Kit, LED Line | installs lgt.ledline | — |
| lgt-097 | Kit, Lamp Assembly Bay | installs lgt.lampbay | — |
| lgt-098 | Kit, Optics Bench | installs lgt.optics | — |
| lgt-099 | Kit, Sensor Lab | installs lgt.sensorlab | — |
| lgt-100 | Kit, Calibration Station | installs lgt.calstation | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| blow bulb envelopes | lgt.glassline | 60 | 1 cer-014, 1 pwr-001 | 6 lgt-011 | — |
| blow envelopes from cullet | lgt.glassline | 60 | 2 cer-010, 1 pwr-001 | 4 lgt-011 | — |
| reclaim burnt out bulbs | lgt.glassline | 60 | 4 lgt-075, 1 pwr-001 | 1 cer-010, 1 scr-001 | — |
| coat lamp phosphor | lgt.glassline | 45 | 1 cer-050, 1 chm-034 | 4 lgt-014 | — |
| blend full spectrum phosphor | lgt.glassline | 45 | 2 lgt-014, 1 chm-076 | 2 lgt-015 | — |
| draw uv tubes | lgt.glassline | 90 | 1 cer-013, 1 lgt-014, 1 gas-014, 1 pol-076, 1 pwr-001 | 2 lgt-021 | — |
| reclaim burnt out uv tubes | lgt.glassline | 60 | 3 lgt-076, 1 pwr-001 | 1 cer-010, 1 lgt-014 | — |
| seal glass ampoules | lgt.glassline | 30 | 1 cer-019, 1 pwr-001 | 8 lgt-027 | — |
| frost glass covers | lgt.glassline | 45 | 1 cer-014, 1 chm-009, 1 pwr-001 | 4 lgt-022 | — |
| fill a calibration gas cell | lgt.glassline | 30 | 1 lgt-027, 1 gas-002 | 1 lgt-094 | — |
| cast a glass line crucible | any.bench | 60 | 1 cer-038 | 1 lgt-089 | — |
| wind lamp filaments | lgt.lampbay | 30 | 1 met-047, 1 pwr-001 | 8 lgt-012 | — |
| stamp lamp caps | lgt.lampbay | 30 | 1 met-036, 1 pwr-001 | 8 lgt-013 | — |
| make lamp sockets | lgt.lampbay | 30 | 1 pol-049, 1 met-036, 1 pwr-001 | 4 lgt-034 | — |
| assemble lamp bulbs | lgt.lampbay | 45 | 2 lgt-011, 2 lgt-012, 2 lgt-013, 1 gas-014, 1 pwr-001 | 2 lgt-001 | — |
| refill a burnt out bulb | any.bench | 90 | 1 lgt-075, 1 lgt-012, 1 gas-003 | 1 lgt-001 | — |
| assemble a night lamp | lgt.lampbay | 45 | 1 lgt-001, 1 lgt-022, 1 lgt-034, 1 lgt-045 | 1 lgt-055 | — |
| assemble a reading lamp | lgt.lampbay | 45 | 1 lgt-001, 1 lgt-031, 1 lgt-034, 1 mec-015 | 1 lgt-056 | — |
| assemble a ceiling lamp | lgt.lampbay | 45 | 2 lgt-001, 1 lgt-022, 1 lgt-034 | 1 lgt-057 | — |
| assemble a wall sconce | lgt.lampbay | 45 | 1 lgt-001, 1 lgt-022, 1 lgt-034, 1 ecp-072 | 1 lgt-060 | — |
| assemble a pendant lamp | lgt.lampbay | 45 | 1 lgt-001, 1 lgt-023, 1 lgt-034 | 1 lgt-067 | — |
| assemble a sodium grow lamp | lgt.lampbay | 60 | 1 lgt-011, 1 lgt-012, 1 ore-025, 1 gas-025, 1 lgt-016 | 1 lgt-074 | — |
| assemble a flashlight | lgt.lampbay | 45 | 1 lgt-019, 1 ecp-011, 1 pol-045, 1 pwr-002, 1 pol-060 | 1 lgt-005 | — |
| assemble a battery lantern | lgt.lampbay | 45 | 1 lgt-001, 1 lgt-022, 1 ecp-049, 1 pwr-002 | 1 lgt-064 | — |
| assemble a head lamp | lgt.lampbay | 45 | 1 lgt-031, 1 ecp-011, 1 pwr-023, 1 fib-006 | 1 lgt-065 | — |
| assemble a uv sterilizer lamp | lgt.lampbay | 60 | 1 lgt-021, 1 ecp-048, 1 pol-045 | 1 lgt-069 | — |
| assemble a germicidal panel | lgt.lampbay | 60 | 2 lgt-021, 1 lgt-025, 1 ecp-048 | 1 lgt-070 | — |
| assemble a sun lamp | lgt.lampbay | 60 | 1 lgt-021, 1 lgt-015, 1 lgt-016, 1 ecp-048 | 1 lgt-068 | — |
| assemble a floodlight | lgt.lampbay | 60 | 2 lgt-002, 1 lgt-023, 1 lgt-018, 1 ecp-048 | 1 lgt-062 | — |
| assemble a task lamp | lgt.lampbay | 45 | 1 lgt-002, 1 lgt-018, 1 ecp-072, 1 mec-015 | 1 lgt-061 | — |
| mix chemlight fill | lgt.lampbay | 30 | 1 chm-007, 1 chm-047 | 4 lgt-026 | — |
| fill glow sticks | lgt.lampbay | 20 | 1 lgt-026, 2 lgt-027, 1 pol-008 | 4 lgt-077 | — |
| fill long burn glow sticks | lgt.lampbay | 30 | 2 lgt-026, 1 lgt-027, 1 pol-008 | 2 lgt-078 | — |
| assemble an emergency light wand | lgt.lampbay | 30 | 2 lgt-026, 1 lgt-027, 1 pol-033 | 1 lgt-079 | — |
| make a lamp bay jig | any.bench | 60 | 1 met-005, 2 mec-001 | 1 lgt-091 | — |
| print led carrier strips | lgt.ledline | 45 | 1 met-040, 1 pol-032, 1 pwr-001 | 4 lgt-020 | — |
| cut carrier strips from flex circuit | lgt.ledline | 20 | 1 ecp-034 | 2 lgt-020 | — |
| mould led lens caps | lgt.ledline | 30 | 1 pol-033, 1 pwr-001 | 10 lgt-019 | — |
| mount led strips | lgt.ledline | 45 | 1 lgt-020, 4 ecp-011, 1 ecp-018, 1 pwr-001 | 2 lgt-002 | — |
| solder an led strip by hand | any.bench | 120 | 1 lgt-020, 4 ecp-011, 1 ecp-017 | 1 lgt-002 | — |
| mount indicator lamps | lgt.ledline | 20 | 4 ecp-011, 4 lgt-019 | 4 lgt-054 | — |
| assemble an led ceiling lamp | lgt.ledline | 45 | 1 lgt-002, 1 lgt-017, 1 lgt-018, 1 ecp-048 | 1 lgt-058 | — |
| assemble a strip light | lgt.ledline | 30 | 1 lgt-002, 1 lgt-017 | 1 lgt-059 | — |
| assemble a light panel | lgt.ledline | 60 | 2 lgt-002, 1 lgt-024, 1 lgt-017, 1 lgt-025, 1 ecp-048 | 1 lgt-004 | — |
| assemble a daylight panel | lgt.ledline | 60 | 1 lgt-004, 1 lgt-015, 1 lgt-028, 1 ecp-047 | 1 lgt-063 | — |
| assemble a mood light orb | lgt.ledline | 45 | 1 lgt-002, 1 lgt-022, 1 ecp-007 | 1 lgt-066 | — |
| assemble a grow light | lgt.ledline | 60 | 2 lgt-002, 1 lgt-015, 1 lgt-018, 1 ecp-048 | 1 lgt-003 | — |
| assemble a grow light array | lgt.ledline | 90 | 4 lgt-002, 2 lgt-015, 1 lgt-025, 1 lgt-018, 1 ecp-048 | 1 lgt-071 | — |
| assemble a seedling rack light | lgt.ledline | 60 | 2 lgt-002, 1 lgt-015, 1 lgt-025 | 1 lgt-072 | — |
| assemble a plant lamp strip | lgt.ledline | 30 | 1 lgt-002, 1 lgt-015 | 1 lgt-073 | — |
| turn led placer nozzles | any.bench | 45 | 1 met-034, 1 pol-009 | 2 lgt-090 | — |
| grind lenses | lgt.optics | 60 | 1 cer-022, 1 pwr-001 | 2 lgt-006 | — |
| grind a lens by hand | any.bench | 240 | 1 cer-022, 1 ore-082 | 1 lgt-006 | — |
| grind spot beam lenses | lgt.optics | 60 | 1 cer-022, 1 pwr-001 | 1 lgt-031 | — |
| press fresnel lenses | lgt.optics | 45 | 1 pol-034, 1 pwr-001 | 2 lgt-032 | — |
| grind prisms | lgt.optics | 90 | 1 cer-021, 1 pwr-001 | 2 lgt-030 | — |
| cut optical mirrors | lgt.optics | 45 | 1 cer-024, 1 pwr-001 | 2 lgt-029 | — |
| clad optical fibre | lgt.optics | 45 | 1 cer-026, 1 pol-042, 1 pwr-001 | 4 lgt-028 | — |
| polish reflectors | lgt.optics | 45 | 1 met-007, 1 pwr-001 | 2 lgt-016 | — |
| form reflector housings | lgt.optics | 45 | 1 lgt-016, 1 met-007, 1 pwr-001 | 1 lgt-023 | — |
| press diffuser sheets | lgt.optics | 30 | 1 pol-033, 1 pol-029, 1 pwr-001 | 4 lgt-017 | — |
| cut light guides | lgt.optics | 30 | 1 pol-034, 1 pwr-001 | 2 lgt-024 | — |
| bend panel frames | lgt.optics | 30 | 1 met-007, 1 pwr-001 | 2 lgt-025 | — |
| cut lamp heat sinks | lgt.optics | 30 | 1 met-076, 1 pwr-001 | 4 lgt-018 | — |
| mount a magnifier loupe | lgt.optics | 30 | 1 lgt-006, 1 pol-045 | 1 lgt-088 | — |
| cut optics polishing pads | lgt.optics | 20 | 1 fib-005, 1 ore-082 | 2 lgt-092 | — |
| bond laser diodes | lgt.sensorlab | 90 | 1 ecp-022, 1 lgt-029, 1 ecp-026, 1 pwr-001 | 4 lgt-033 | — |
| bond photodiodes | lgt.sensorlab | 60 | 1 ecp-022, 1 ecp-026, 1 pwr-001 | 8 lgt-007 | — |
| fire sensing elements | lgt.sensorlab | 60 | 1 chm-059, 1 cer-038, 1 pwr-001 | 6 lgt-038 | — |
| make diaphragm cells | lgt.sensorlab | 45 | 1 pol-055, 1 met-034, 1 pwr-001 | 4 lgt-039 | — |
| weld thermocouples | lgt.sensorlab | 30 | 1 met-047, 1 met-006, 1 pwr-001 | 6 lgt-040 | — |
| lay strain gauges | lgt.sensorlab | 45 | 1 pol-032, 1 met-047, 1 pwr-001 | 8 lgt-041 | — |
| bond image sensor chips | lgt.sensorlab | 90 | 1 ecp-023, 1 ecp-026, 1 pwr-001 | 4 lgt-035 | — |
| bond hall sensors | lgt.sensorlab | 45 | 1 ecp-022, 1 ecp-026, 1 pwr-001 | 6 lgt-043 | — |
| etch accelerometers | lgt.sensorlab | 90 | 1 ecp-023, 1 ecp-062, 1 pwr-001 | 2 lgt-053 | — |
| make temperature probes | lgt.sensorlab | 30 | 1 lgt-040, 1 pol-040, 1 ecp-016 | 2 lgt-008 | — |
| make a thermistor probe by hand | any.bench | 30 | 1 ecp-057, 1 pol-040 | 1 lgt-008 | — |
| assemble pressure sensors | lgt.sensorlab | 45 | 1 lgt-039, 1 lgt-041, 1 ecp-061 | 2 lgt-009 | — |
| assemble gas sensors | lgt.sensorlab | 45 | 1 lgt-038, 1 ecp-061 | 2 lgt-010 | — |
| assemble a co2 sensor | lgt.sensorlab | 60 | 1 lgt-037, 1 lgt-029, 1 ecp-062 | 1 lgt-049 | — |
| assemble an oxygen sensor | lgt.sensorlab | 60 | 1 lgt-038, 1 cer-038, 1 ecp-061 | 1 lgt-050 | — |
| make humidity sensors | lgt.sensorlab | 30 | 1 pol-032, 1 ecp-002 | 4 lgt-048 | — |
| assemble smoke sensors | lgt.sensorlab | 30 | 1 lgt-007, 1 ecp-011, 1 pol-045 | 2 lgt-051 | — |
| assemble infrared sensors | lgt.sensorlab | 30 | 1 lgt-007, 1 lgt-006 | 2 lgt-037 | — |
| assemble light sensors | lgt.sensorlab | 20 | 1 lgt-007, 1 lgt-019 | 4 lgt-044 | — |
| assemble motion sensors | lgt.sensorlab | 30 | 1 lgt-037, 1 lgt-032, 1 ecp-061 | 2 lgt-045 | — |
| assemble a flow sensor | lgt.sensorlab | 30 | 1 lgt-043, 1 mec-022, 1 pol-045 | 1 lgt-046 | — |
| make level sensors | lgt.sensorlab | 30 | 1 met-034, 1 ecp-062 | 2 lgt-047 | — |
| assemble a load cell | lgt.sensorlab | 45 | 2 lgt-041, 1 met-008, 1 ecp-061 | 1 lgt-042 | — |
| make microphone capsules | lgt.sensorlab | 30 | 1 pol-032, 1 met-077, 1 ecp-061 | 4 lgt-052 | — |
| assemble a camera module | lgt.sensorlab | 60 | 1 lgt-035, 1 lgt-006, 1 ecp-005 | 1 lgt-036 | — |
| make a sensor lab probe set | lgt.sensorlab | 30 | 1 lgt-040, 1 pol-040 | 1 lgt-093 | — |
| calibrate a cabin air sensor pack | lgt.calstation | 60 | 1 lgt-049, 1 lgt-050, 1 lgt-048, 1 lgt-051, 1 ecp-047 | 1 lgt-080 | — |
| calibrate a condenser level probe | lgt.calstation | 30 | 1 lgt-047, 1 lgt-008 | 1 lgt-081 | — |
| calibrate a washbasin flow cell | lgt.calstation | 30 | 1 lgt-046, 1 ecp-061 | 1 lgt-082 | — |
| calibrate a toilet tank sensor | lgt.calstation | 30 | 1 lgt-047, 1 lgt-010 | 1 lgt-083 | — |
| calibrate a solar strip light cell | lgt.calstation | 30 | 1 lgt-044, 1 lgt-007 | 1 lgt-084 | — |
| calibrate an algae jar light sensor | lgt.calstation | 30 | 1 lgt-044, 1 lgt-049 | 1 lgt-085 | — |
| calibrate a hatch leak detector | lgt.calstation | 30 | 1 lgt-009, 1 lgt-052, 1 lgt-053 | 1 lgt-086 | — |
| calibrate a sprouter moisture probe | lgt.calstation | 30 | 1 lgt-048, 1 lgt-008 | 1 lgt-087 | — |
| pack a bulb glass line kit | lgt.lampbay | 180 | 1 met-074, 1 lgt-089, 1 ecp-010, 1 lgt-054, 1 pak-063 | 1 lgt-095 | — |
| pack an led line kit | lgt.lampbay | 180 | 1 cer-083, 1 lgt-090, 1 ecp-010, 1 lgt-042, 1 pak-062 | 1 lgt-096 | — |
| pack a lamp assembly bay kit | lgt.lampbay | 180 | 1 met-074, 1 lgt-091, 1 ecp-010, 1 lgt-054, 1 pak-061 | 1 lgt-097 | — |
| pack an optics bench kit | lgt.lampbay | 150 | 1 met-074, 1 lgt-092, 1 lgt-030, 1 mec-010, 1 pak-062 | 1 lgt-098 | — |
| pack a sensor lab kit | lgt.lampbay | 150 | 1 cer-083, 1 lgt-093, 1 ecp-047, 1 lgt-033, 1 pak-063 | 1 lgt-099 | — |
| pack a calibration station kit | lgt.lampbay | 150 | 1 cer-083, 1 lgt-094, 1 lgt-036, 1 ecp-010, 1 pak-061 | 1 lgt-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| lgt.glassline | Blows bulb envelopes, tubes and ampoules, coats phosphor, and melts burnt-out bulbs and tubes back into cullet. | MOLTEN GLASS. FACE SHIELD REQUIRED. COF HOT WORK AREA. |
| lgt.ledline | Prints carrier strips, moulds lens caps and mounts LEDs into strips, panels, ceiling lamps and grow lights. | Placement accuracy audited monthly. Misplaced diodes are counted against the station. |
| lgt.lampbay | Winds filaments, stamps caps and assembles bulbs, lamps, flashlights and glow sticks, and packs this subsection's kits. | Stencilled above the bench: IF IT LIGHTS, IT SHIPS. Nobody stencilled what happens if not. |
| lgt.optics | Grinds lenses, prisms and mirrors, polishes reflectors, and cuts diffusers, light guides, frames and heat sinks. | Polishing compound is metered. Polish to specification, not to satisfaction. Proc 73. |
| lgt.sensorlab | Bonds photodiodes, laser diodes and image sensor chips, and builds the probes and sensors the ship measures with. | Every alarm aboard was built here. Complaints about alarms are forwarded here. |
| lgt.calstation | Calibrates loose sensors into the spare probes and sensor packs that fit the universal fixtures. | Reference standard checked, rev 14. Reference for the reference not supplied. |
| lgt-001 | Plain glass bulb that lights the cabin while fitted, then burns out into a bulb that can be refilled. | Bulb allocation is one per fixture per quarter. Darkness beyond allocation is unbilled. |
| lgt-002 | Strip of mounted LEDs, the light source inside panels, grow lights and most modern lamps. | CUT ONLY AT MARKED POINTS. DO NOT CUT ACROSS COPPER. |
| lgt-003 | LED light with full spectrum phosphor that lights a cabin and goes into the farm bed kits. | Crop schedules assume uninterrupted grow light. Interruptions are deducted from yield credit. |
| lgt-004 | Flat LED panel that lights the cabin evenly for a long time; the base of the daylight panel. | Uniform illumination, Grade B. Corner dimmer than centre. Within Grade B. |
| lgt-005 | Small hand light: dim and short-lived, ending as broken parts. | Check flashlight function at shift start. A blackout is not the time to find out. |
| lgt-006 | Ground glass lens for loupes, infrared sensors, cameras, sextants and star trackers. | HANDLE BY EDGES ONLY. OPTICAL SURFACE. |
| lgt-007 | Light-sensing chip at the heart of light, smoke and infrared sensors and lidar heads. | Sees in the dark better than the operator. The Company has noted the comparison. |
| lgt-008 | Sheathed probe that reads heat, used by heaters, thermometers, sprinklers and many kits. | Reads warm, rev 2. Second probe also reads warm. Cabin presumed warm. |
| lgt-009 | Reads gas pressure; fitted to canister gauges, pressure loss alarms and engine controllers. | A twitching needle is normal. A still needle is a Form 50P, filed at once. |
| lgt-010 | Detects stray gases; built into leak alarms, sniffer drones and toilet tank sensors. | Detects it before the operator does, and files fewer complaints. |
| lgt-011 | Blown glass bulb shell awaiting a filament and a cap. | FRAGILE. GLASS. PACK UPRIGHT. BREAKAGE IN STORES IS CHARGED. |
| lgt-012 | Coil of tungsten wire that glows inside a bulb; also refills a burnt-out bulb. | Coil pitch checked under loupe. Loupe due for replacement. Pitch accepted. |
| lgt-013 | Stamped metal base by which a bulb screws into its socket. | Clockwise to fit. Proc 1 of the lighting manual. It is a short manual. |
| lgt-014 | Phosphor that coats UV tubes and is blended into full spectrum phosphor. | Do not inhale powder. Glowing residue on hands is reportable. |
| lgt-015 | Blended phosphor that makes LEDs shine like daylight, for grow lights and daylight panels. | Approximates natural daylight. Natural daylight is not provided under the contract. |
| lgt-016 | Mirrored metal reflector that directs a lamp's light where it is needed. | Reflectivity tested, rev 5. Dent in lower quadrant. Light goes elsewhere there. |
| lgt-017 | Frosted plastic sheet that softens LED glare in panels, ceiling lamps and strip lights. | Glare reduction meets the minimum visual comfort standard. Minimum is the standard. |
| lgt-018 | Finned metal block that keeps LEDs and lamps from overheating. | HOT SURFACE. WARM IS NORMAL. GLOWING IS NOT. |
| lgt-019 | Tiny moulded cap over an LED, for indicator lamps, light sensors and flashlights. | Spilled a tray of these in the last shake. Still finding them with bare feet. |
| lgt-020 | Thin printed strip on which LEDs are mounted. | Copper side up. Orientation errors are scrapped at the operator's expense. |
| lgt-021 | Gas-filled phosphor tube that emits ultraviolet, used in sterilizers, germicidal panels and sun lamps. | ULTRAVIOLET. DO NOT VIEW TUBE DIRECTLY. EYE PROTECTION REQUIRED. |
| lgt-022 | Frosted glass shade for night lamps, ceiling lamps, sconces, lanterns and mood light orbs. | Frosting reduces glare and conceals dust accumulation. Both are approved outcomes. |
| lgt-023 | Metal housing around a reflector, for pendant lamps, floodlights and the galley. | Fitted over the galley stove, rev 1. Reason for location not recorded. |
| lgt-024 | Clear plastic plate that spreads light across a panel. | Edge-lit. Edges chipped in transit. Light leaks noted, accepted. |
| lgt-025 | Bent metal frame that holds light panels, arrays and seedling racks. | Frame squareness checked by diagonal. Diagonals differ. Frame fitted with force. |
| lgt-026 | Two-part chemical mix that glows when a stick is bent. | NOT A BEVERAGE. INGESTION HAS OCCURRED. DO NOT REPEAT. |
| lgt-027 | Small sealed glass vial for glow sticks, light wands and calibration gas cells. | Ampoules are sealed by count. Count discrepancies go to Form 9A, in triplicate. |
| lgt-028 | Clad glass fibre that carries light, used in daylight panels. | Minimum bend radius applies. Kinked fibre transmits nothing but regret. |
| lgt-029 | Precision mirror for laser diodes, carbon dioxide sensors and lidar heads. | Gloves only. One fingerprint costs a shift of polishing. Ref 4407/O. |
| lgt-030 | Ground glass prism, packed into optics bench kits. | Splits light into colours. Colour use in the cabin remains restricted by Notice 31. |
| lgt-031 | Focusing lens for reading lamps, head lamps, lidar heads and the library. | Aim at the work surface. Aiming at personnel is a conduct matter. |
| lgt-032 | Flat ringed plastic lens for motion sensors and shield projector lenses. | Ringed face down. Dust in the rings reduces range. Clean dry. Proc 8. |
| lgt-033 | Tiny laser chip for lidar modules and sensor lab kits. | LASER RADIATION. CLASS 3. AVOID EXPOSURE TO BEAM. |
| lgt-034 | Socket a bulb screws into; every bulb lamp and floor lamp stand needs one. | Isolate power before reaching in. Shock incidents are self-reported on Form 3S. |
| lgt-035 | Chip that converts light into images, for camera modules and star tracker heads. | Images captured remain Company records. Personal images are not supported. |
| lgt-036 | Small camera for drones, medical scanners, star trackers and survey packs. | Camera footage is reviewed at random. Review frequency is not disclosed. |
| lgt-037 | Senses heat at a distance, for motion, carbon dioxide and storm warning sensors and medical scanners. | Detects body heat. Body heat is logged as occupancy. Occupancy is logged as work. |
| lgt-038 | Fired ceramic element that reacts to gases, for gas and oxygen sensors. | Fired, aged, matched to batch card. Batch card handwritten. Mostly legible. |
| lgt-039 | Thin flexing membrane cell at the heart of a pressure sensor. | DIAPHRAGM. DO NOT PRESS. DO NOT TEST BY BLOWING. |
| lgt-040 | Two welded wires that read temperature; used in probes, thermometers and probe sets. | Polarity marked by colour. Colour chart issued separately. Not issued. |
| lgt-041 | Foil gauge that reads stretch, for pressure sensors, load cells and strain plates. | Measures what the hull is putting up with. Personnel are measured elsewhere. |
| lgt-042 | Cell that measures force, used in impact sensors and LED line kits. | Overload marked on body. Overloaded cells read high forever after. Rev 3. |
| lgt-043 | Magnetic sensor chip that counts the turns inside a flow sensor. | Keep magnets away. Magnets are not issued, so this is a reminder about contraband. |
| lgt-044 | Reads light level; used in solar strip light cells and algae jar sensors. | Detects day. Day is defined by the Company clock, not by this sensor. |
| lgt-045 | Switches a light on when movement is detected, as in the night lamp. | Timeout set to minimum. Personnel who remain still remain in the dark. |
| lgt-046 | Measures liquid flowing through a pipe, for washbasins, blenders and throttle valves. | Flow data feeds water billing. Tampering is detected by the same sensor. |
| lgt-047 | Reports how full a tank is, for condensers and toilets. | FULL, EMPTY, FAULT. NO OTHER STATES ARE REPORTED. |
| lgt-048 | Reads moisture in air or soil, for cabin air sensor packs and sprouter probes. | Cabin sweats, sensor records. Records are not acted on below threshold. |
| lgt-049 | Measures carbon dioxide in the cabin air, for cabin air packs and algae jar sensors. | When it alarms, stop work and check the scrubber. Stopping work is logged, not penalised. |
| lgt-050 | Measures oxygen in the air, for cabin air sensor packs and the gas works. | Oxygen is supplied at contract level. Readings below it go to Form 11X, urgently. |
| lgt-051 | Detects smoke early, for cabin air sensor packs and smoke detectors. | Burnt ration triggers it. Every alarm is logged. Every log is read. Eventually. |
| lgt-052 | Tiny microphone that listens for the hiss of a leaking hatch. | Tuned to hull frequencies only. Voice pickup is incidental and retained. |
| lgt-053 | Senses movement and shock, for hatch leak detectors and accelerometer stacks. | Records every impact. Impacts caused by personnel are attributed. |
| lgt-054 | Small LED telltale that shows a device is on, used in beacons, pingers and kits. | GREEN: RUN. AMBER: WATCH. RED: STOP AND REPORT. |
| lgt-055 | Dim lamp with a motion sensor that lights the cabin faintly through the night. | Sufficient for the walk to the toilet. Not intended for anything else. Notice 14. |
| lgt-056 | Hinged bulb lamp that lights the cabin for reading and close work. | Reading material is limited to Company manuals. The lamp does not check. |
| lgt-057 | The cabin's main bulb fixture; burns out into bulbs to refill. | Changed it standing on the chest. Everyone does. The chest lid shows it. |
| lgt-058 | LED ceiling lamp that outlasts the bulb kind by far and ends as e-waste. | Lower running cost per lumen. The saving is retained by the Company. |
| lgt-059 | Plain LED strip behind a diffuser that gives a steady light. | Run along the floor rail. Cabin appears larger. Cabin is not larger. |
| lgt-060 | Switched wall lamp behind frosted glass. | Mount level. Off-level fixtures are corrected at inspection and charged. |
| lgt-061 | Hinged, switched LED lamp for close work. | Arm spring weak, rev 2. Lamp droops onto the work. Taped in place. |
| lgt-062 | Bright LED flood that lights a cabin intensely. | WORK LIGHT. NOT FOR REST PERIODS. DO NOT AIM AT BUNK. |
| lgt-063 | Panel tuned to daylight that lights the cabin and eases stress. | Issued under the wellbeing programme. Wellbeing is assessed quarterly, by output. |
| lgt-064 | Portable battery bulb lantern; short-lived, ending as broken parts. | Grabbed it in the last blackout. Uncharged. Charged it after. Typical. |
| lgt-065 | Strapped lamp for hands-free light; dim and short-lived. | Look down to work. Looking up at a colleague is a glare incident. Proc 41. |
| lgt-066 | Softly glowing orb that gives a little light and eases stress. | Colour cycle limited to amber and green. Other colours were withdrawn as distracting. |
| lgt-067 | Hanging bulb lamp in a reflector housing. | Swings when the drive burns. Better than the bulletin for knowing when. |
| lgt-068 | Ultraviolet and full spectrum lamp that lights the cabin and eases stress. | Daily exposure capped by timer. Additional sun is not budgeted. Ref 0600/S. |
| lgt-069 | UV tube lamp that keeps the cabin cleaner while it burns. | VACATE AREA DURING CYCLE. UV EXPOSURE HAZARD. |
| lgt-070 | Panel of UV tubes that keeps the cabin cleaner than the sterilizer lamp does. | Leave the cabin while it runs. The panel does not distinguish germs from personnel. |
| lgt-071 | Large farm light used by berry, leafy green, fruiting vegetable and vine kits. | Highest single power draw on the farm deck. Every hour is metered. Proc 220. |
| lgt-072 | Rack light for seedlings, used by propagation bench kits. | Seedling losses under this light are reported on Form 13G with photographs. |
| lgt-073 | Slim grow strip for herb towers and plant shelves. | Herbs grown under Company light are Company herbs. Ref 2140/H. |
| lgt-074 | Orange sodium lamp for dwarf orchards and warm groves; burns out into a bulb. | Everything is orange under it. Colour inspection of fruit is done elsewhere. |
| lgt-075 | Dead bulb, refilled at the bench or melted down for cullet. | Dead bulbs are returned for reclaim. Bulbs found in waste bins are traced. |
| lgt-076 | Dead UV tube, reclaimed into cullet and phosphor. | CONTAINS PHOSPHOR AND GAS. DO NOT BREAK. RETURN TO GLASS LINE. |
| lgt-077 | Single-use chemical light that lights the cabin for a while once bent and shaken. | Bend, shake, wait. Spent sticks are counted against the emergency allowance. |
| lgt-078 | Larger glow stick that gives more light before it fades. | Rated for one rest period. The rest period is shorter than it looks. |
| lgt-079 | Brightest chemical light, for blackouts and emergencies. | EMERGENCY USE ONLY. BREAK SEAL IN DARKNESS. LOG USE ON FORM 0E. |
| lgt-080 | Spare sensor pack for life support; wears out into e-waste. | Air quality data is transmitted continuously. Air quality is not guaranteed. |
| lgt-081 | Spare probe for the condenser that reports how full its tank is. | Probe swapped, rev 1. Tank reads full when empty. Swapped again, rev 2. |
| lgt-082 | Spare flow sensor for the washbasin. | Every drop is counted. The count is sent upward. Nothing comes back down. |
| lgt-083 | Spare level and gas sensor for the toilet tank. | Fitting is a station task. Gloves are issued for it. Two pairs, recommended. |
| lgt-084 | Spare light sensor for the solar strip. | Tells the strip where the light is. Light is where the Company placed it. |
| lgt-085 | Spare sensor for the algae jar that reads light and carbon dioxide. | Jar readings within band. Jar colour also within band, approximately. |
| lgt-086 | Spare pressure, sound and shock sensor for the service hatch. | HATCH LEAK DETECTOR. A HISS IS AN ALERT. EVACUATE, THEN REPORT. |
| lgt-087 | Spare moisture probe for the sprouter. | Damp, not drowned. Drowned trays are written off under Proc 19. |
| lgt-088 | Mounted lens that fits the workbench or the optics bench and wears out slowly. | Scratched across centre. Look through the edge. Works fine at the edge. |
| lgt-089 | Ceramic crucible, the spare part of the bulb glass line. | Cool slowly. Thermal shock cracks it. Cracked crucibles are not reissued. Ref 9020/C. |
| lgt-090 | Spare pick-and-place nozzle for the LED line. | Tip clogged with lens caps, rev 4. Cleared with a pin. Pin not approved. |
| lgt-091 | Spare holding jig for the lamp assembly bay. | Jig holds the lamp. Operator holds the jig. Proc 70 calls this efficient. |
| lgt-092 | Spare polishing pad for the optics bench. | Grit grade stamped on back, Grade 4. Use the right side up. |
| lgt-093 | Spare probe set for the sensor lab. | Test probes are themselves tested. Testing of that testing is scheduled for review. |
| lgt-094 | Sealed ampoule of carbon dioxide, the spare reference for the calibration station. | REFERENCE GAS. DO NOT OPEN. DO NOT SUBSTITUTE CABIN AIR. |
| lgt-095 | Packed kit that installs a bulb glass line. | Some assembly required. Some glassblowing also required. Training not included. |
| lgt-096 | Packed kit that installs an LED line. | Packing list attached. Packing list describes a different kit. Contents correct. |
| lgt-097 | Packed kit that installs a lamp assembly bay. | Install under existing light. Kit contains no light for its own installation. |
| lgt-098 | Packed kit that installs an optics bench. | Prism included. Prism is accounted for at commissioning. Keep it. |
| lgt-099 | Packed kit that installs a sensor lab. | Everything a lab needs except clean hands. Hands are the station's to supply. |
| lgt-100 | Packed kit that installs a calibration station. | Factory calibrated. Recalibrate on install per Proc 5. Factory calibration is a formality. |
