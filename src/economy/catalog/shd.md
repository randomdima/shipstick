# Shields & Deflection — `shd`

What keeps radiation storms and debris off the ship. Wire is wound into coils and cryo-jacketed, foil and film are
rolled into capacitors, frit and resin are fired into ablative tiles, blanks are ground into projector lenses, and cord
is knotted into debris nets; the field lab joins them into emitters, nodes and generators. Each raises `ship.shield` at
the service hatch, the large ones only from many subsections' metals, glass, polymers and electronics. Spent capacitors
and burnt-out emitter heads come back to be recharged and rebuilt. A few panels and screens stay in the cabin and lower
the crew's `dose` while they stand.

## Devices

| id | device | role | cells |
|---|---|---|---|
| shd.coilwinder | DF20 Shield Coil Winder | helm | 2x2 |
| shd.capshop | DF35 Capacitor Shop | helm | 2x1 |
| shd.tilekiln | DF40K Tile Kiln | helm | 2x2 |
| shd.lensworks | DF55 Lens Works | helm | 2x1 |
| shd.fieldlab | DF90 Field Lab | helm | 3x2 |
| shd.netloom | DF12 Net Loom | helm | 2x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| shd-001 | Emitter, Shield | ship.shield +20, leaves 1 shd-064 | — |
| shd-002 | Coil, Deflector | ship.shield +8 | — |
| shd-003 | Tile, Ablative | ship.shield +2 | — |
| shd-004 | Capacitor, Shield | ship.shield +5, leaves 1 shd-042 | — |
| shd-005 | Coil, Magnetic, Shield | — | — |
| shd-006 | Net, Debris | ship.shield +3 | — |
| shd-007 | Lens, Shield Projector | ship.shield +4 | — |
| shd-008 | Generator, Field | ship.shield +18 | — |
| shd-009 | Window, Plasma | ship.shield +12 | — |
| shd-010 | Sensor, Impact | ship.shield +2 | — |
| shd-011 | Foil, Lead, Shield Grade | — | — |
| shd-012 | Frit, Glass, Borated | — | — |
| shd-013 | Resin, Ablative | — | — |
| shd-014 | Blank, Ablative Tile | — | — |
| shd-015 | Tile, Ablative, Heavy | ship.shield +4 | — |
| shd-016 | Panel, Tile, Layered | ship.shield +8 | — |
| shd-017 | Mat, Shield, Bonded | ship.shield +3 | — |
| shd-018 | Adhesive, Tile | — | 720 h → scr-002 |
| shd-019 | Coating, Ablative, Spray | ship.shield +1, leaves 1 pak-022 | — |
| shd-020 | Panel, Aegis | ship.shield +10 | — |
| shd-021 | Wire, Coil, Cooled | — | — |
| shd-022 | Former, Coil | — | — |
| shd-023 | Coil, Wound, Shield | — | — |
| shd-024 | Stack, Iron Core | — | — |
| shd-025 | Jacket, Coil Cryo | — | — |
| shd-026 | Protector, Quench | — | — |
| shd-027 | Wrap, Coil Insulation | — | — |
| shd-028 | Pair, Coil, Twin | ship.shield +6 | — |
| shd-029 | Array, Field Coil | ship.shield +10 | — |
| shd-030 | Wick, Static Discharge | ship.shield +1 | — |
| shd-031 | Spool, Coil, Cryo | ship.shield +3 | — |
| shd-032 | Bottle, Mag Flux | ship.shield +3 | — |
| shd-033 | Film, Dielectric | — | — |
| shd-034 | Roll, Capacitor Foil | — | — |
| shd-035 | Cell, Capacitor, Rolled | — | — |
| shd-036 | Housing, Capacitor | — | — |
| shd-037 | Cap Set, Capacitor Terminal | — | — |
| shd-038 | Stack, Capacitor Bank | ship.shield +15, leaves 3 shd-042 | — |
| shd-039 | Pack, Shield Cell | ship.shield +4 | — |
| shd-040 | Pack, Shield, Standby | ship.shield +8 | — |
| shd-041 | Jar, Charge Reservoir | ship.shield +2 | — |
| shd-042 | Capacitor, Shield, Depleted | — | — |
| shd-043 | Blank, Lens, Fused | — | — |
| shd-044 | Lens, Shield, Ground | — | — |
| shd-045 | Coating, Antiflare | — | — |
| shd-046 | Lens, Shield, Coated | — | — |
| shd-047 | Ring, Focusing | — | — |
| shd-048 | Barrel, Lens | — | — |
| shd-049 | Paste, Lens Polish | — | — |
| shd-050 | Ring, Lens Seat | — | — |
| shd-051 | Lens, Projector, Wide | ship.shield +8 | — |
| shd-052 | Pane, Plasma Glass | — | — |
| shd-053 | Plate, Field Emitter | — | — |
| shd-054 | Cell, Plasma Gas | — | — |
| shd-055 | Board, Field Stabilizer | — | — |
| shd-056 | Mesh, Containment | ship.shield +6 | — |
| shd-057 | Node, Shield | ship.shield +10 | — |
| shd-058 | Cell, Shield, Local | ship.shield +6 | — |
| shd-059 | Housing, Emitter | — | — |
| shd-060 | Card, Emitter Control | ship.shield +4 | — |
| shd-061 | Pack, Shield Booster | ship.shield +15 | — |
| shd-062 | Card, Emitter Calibration | ship.shield +5 | — |
| shd-063 | Cell, Storm, Emergency | ship.shield +20 | — |
| shd-064 | Head, Emitter, Burnt Out | — | — |
| shd-065 | Cord, Net, Aramid | — | — |
| shd-066 | Ring, Net Knot | — | — |
| shd-067 | Cable, Edge, Weighted | — | — |
| shd-068 | Net, Debris, Heavy | ship.shield +6 | — |
| shd-069 | Net, Capture | ship.shield +10 | — |
| shd-070 | Patch, Net Repair | ship.shield +2 | — |
| shd-071 | Pickup, Piezo | — | — |
| shd-072 | Plate, Strain | — | — |
| shd-073 | Amplifier, Sensor | — | — |
| shd-074 | Counter, Micrometeoroid | ship.shield +4 | — |
| shd-075 | Sensor, Storm Warning | ship.shield +3 | — |
| shd-076 | Net, Impact Sensor | ship.shield +10 | — |
| shd-077 | Lamp, Shield Status | cabin.light +1/h, stress -1/h | 1500 h → scr-003 |
| shd-078 | Tile, Wall, Lead | dose -1/h | 1500 h → scr-001 |
| shd-079 | Panel, Wall, Boron | dose -1/h | 2000 h → scr-004 |
| shd-080 | Screen, Bunk, Radiation | dose -2/h | 1500 h → scr-004 |
| shd-081 | Curtain, Radiation, Cabin | dose -1/h | 1200 h → scr-005 |
| shd-082 | Pane, Radiation Shade | dose -1/h, cabin.light +1/h | 2000 h → scr-004 |
| shd-083 | Pad, Solar Flare Shelter | dose -2/h, rest +1/h | 1500 h → scr-004 |
| shd-084 | Plate, Wall, Ablative | dose -1/h | 2000 h → scr-004 |
| shd-085 | Seal, Hatch Shield | fits any.hatch | 1500 h → scr-074 |
| shd-086 | Tape, Coil, Superconducting | — | — |
| shd-087 | Tuner, Shield Harmonic | ship.shield +3 | — |
| shd-088 | Baffle, Radiation Storm | ship.shield +6 | — |
| shd-089 | Spindle, Winding | fits shd.coilwinder | 800 h → scr-001 |
| shd-090 | Plate, Capacitor Press | fits shd.capshop | 1000 h → scr-001 |
| shd-091 | Element, Kiln Heating | fits shd.tilekiln | 600 h → scr-004 |
| shd-092 | Wheel, Lens Polishing | fits shd.lensworks | 400 h → scr-004 |
| shd-093 | Seal, Field Lab Vacuum | fits shd.fieldlab | 600 h → scr-074 |
| shd-094 | Shuttle, Net Loom | fits shd.netloom | 1000 h → scr-001 |
| shd-095 | Kit, Shield Coil Winder | installs shd.coilwinder | — |
| shd-096 | Kit, Capacitor Shop | installs shd.capshop | — |
| shd-097 | Kit, Tile Kiln | installs shd.tilekiln | — |
| shd-098 | Kit, Lens Works | installs shd.lensworks | — |
| shd-099 | Kit, Field Lab | installs shd.fieldlab | — |
| shd-100 | Kit, Net Loom | installs shd.netloom | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| assemble a shield emitter | shd.fieldlab | 240 | 1 shd-059, 1 shd-002, 1 shd-007, 1 shd-060, 1 shd-004, 1 pwr-001 | 1 shd-001 | — |
| rebuild a burnt out emitter head | shd.fieldlab | 180 | 1 shd-064, 1 shd-053, 1 shd-007, 1 shd-004, 1 pwr-001 | 1 shd-001 | — |
| strip a burnt out emitter head | any.bench | 40 | 1 shd-064 | 1 scr-003, 1 scr-001 | — |
| wind a deflector coil | shd.coilwinder | 200 | 1 shd-005, 1 shd-031, 1 shd-026, 1 pwr-001 | 1 shd-002 | — |
| wind a deflector coil from twin coils | shd.coilwinder | 240 | 2 shd-005, 1 shd-025, 1 shd-026, 1 pwr-016, 1 pwr-001 | 1 shd-002 | — |
| fire ablative tiles | shd.tilekiln | 60 | 1 shd-014, 1 shd-013, 1 pwr-001 | 2 shd-003 | — |
| face a thermal tile with adhesive | shd.tilekiln | 60 | 1 cer-048, 1 shd-018, 1 pwr-001 | 1 shd-003 | — |
| glue an ablative tile by hand | any.bench | 90 | 1 cer-002, 1 pol-007 | 1 shd-003 | — |
| assemble a shield capacitor | shd.capshop | 120 | 2 shd-035, 1 shd-036, 1 shd-037, 1 pwr-001 | 1 shd-004 | — |
| bank supercapacitors into a shield capacitor | shd.capshop | 90 | 2 pwr-077, 1 shd-036, 1 pwr-001 | 1 shd-004 | — |
| recharge a depleted capacitor | shd.capshop | 60 | 1 shd-042, 2 pwr-001 | 1 shd-004 | — |
| scrap a depleted capacitor | any.bench | 20 | 1 shd-042 | 1 scr-003 | — |
| wind a shield magnetic coil | shd.coilwinder | 90 | 1 shd-023, 1 shd-024, 1 pwr-001 | 1 shd-005 | — |
| core an inductor coil | shd.coilwinder | 90 | 1 pwr-076, 1 shd-024, 1 shd-027, 1 pwr-001 | 1 shd-005 | — |
| hand wind a magnetic coil | any.bench | 120 | 3 met-006, 1 met-001 | 1 shd-005 | — |
| knot a debris net | shd.netloom | 100 | 3 shd-065, 2 shd-066, 1 pwr-001 | 1 shd-006 | — |
| lash a debris net from rope and mesh | any.bench | 180 | 2 fib-071, 1 met-057 | 1 shd-006 | — |
| mount a shield projector lens | shd.lensworks | 150 | 1 shd-046, 1 shd-048, 1 pwr-001 | 1 shd-007 | — |
| barrel a fresnel projector lens | shd.lensworks | 180 | 1 lgt-032, 1 shd-045, 1 shd-048, 1 pwr-001 | 1 shd-007 | — |
| build a field generator | shd.fieldlab | 240 | 1 shd-002, 1 shd-029, 1 shd-056, 1 nav-004, 1 pwr-001 | 1 shd-008 | — |
| build a plasma window | shd.fieldlab | 240 | 1 shd-052, 2 shd-054, 1 shd-007, 1 shd-056, 1 pwr-001 | 1 shd-009 | — |
| build an impact sensor | shd.fieldlab | 100 | 1 shd-073, 1 pol-045, 1 pwr-001 | 1 shd-010 | — |
| wire a load cell impact sensor | shd.fieldlab | 90 | 1 lgt-042, 1 ecp-047, 1 met-007, 1 pwr-001 | 1 shd-010 | — |
| roll shield lead foil | shd.tilekiln | 40 | 1 met-041, 1 pwr-001 | 3 shd-011 | — |
| grind borated glass frit | shd.tilekiln | 40 | 1 cer-014, 1 pwr-001 | 3 shd-012 | — |
| mix ablative resin | shd.tilekiln | 50 | 1 pol-025, 1 shd-012, 1 pwr-001 | 2 shd-013 | — |
| press ablative tile blanks | shd.tilekiln | 50 | 1 cer-002, 1 shd-012, 1 pwr-001 | 2 shd-014 | — |
| fire a heavy ablative tile | shd.tilekiln | 100 | 2 shd-003, 1 cer-041, 1 pwr-001 | 1 shd-015 | — |
| layer a tile panel | shd.tilekiln | 140 | 2 shd-015, 1 cer-009, 1 shd-018, 1 pwr-001 | 1 shd-016 | — |
| bond a shield mat | shd.tilekiln | 90 | 1 shd-003, 1 fib-066, 1 shd-018, 1 pwr-001 | 1 shd-017 | — |
| mix tile adhesive | shd.tilekiln | 40 | 1 pol-010, 1 cer-037, 1 pwr-001 | 3 shd-018 | — |
| can ablative spray coating | shd.tilekiln | 50 | 1 shd-013, 1 pak-021, 1 pwr-001 | 1 shd-019 | — |
| build an aegis panel | shd.tilekiln | 160 | 1 shd-015, 1 shd-079, 1 cer-075, 1 pwr-001 | 1 shd-020 | — |
| enamel cooled coil wire | shd.coilwinder | 50 | 2 met-006, 1 pol-042, 1 pwr-001 | 3 shd-021 | — |
| respool winding wire | shd.coilwinder | 30 | 2 pwr-047, 1 pwr-001 | 3 shd-021 | — |
| cut coil formers | shd.coilwinder | 50 | 1 cer-071, 1 pwr-001 | 2 shd-022 | — |
| wind shield coils | shd.coilwinder | 70 | 1 shd-021, 1 shd-022, 1 shd-027, 1 pwr-001 | 2 shd-023 | — |
| stack iron cores | shd.coilwinder | 50 | 2 met-009, 1 pwr-001 | 2 shd-024 | — |
| jacket a coil for cryo | shd.coilwinder | 100 | 1 thm-019, 1 met-056, 1 thm-039, 1 pwr-001 | 1 shd-025 | — |
| build a quench protector | shd.coilwinder | 90 | 1 ecp-036, 1 ecp-058, 1 shd-021, 1 pwr-001 | 1 shd-026 | — |
| slit coil insulation wrap | shd.coilwinder | 30 | 1 pol-032, 1 pwr-001 | 3 shd-027 | — |
| pair twin coils | shd.coilwinder | 130 | 2 shd-005, 1 shd-026, 1 pwr-001 | 1 shd-028 | — |
| array field coils | shd.coilwinder | 150 | 3 shd-005, 1 shd-025, 1 pwr-016, 1 pwr-001 | 1 shd-029 | — |
| braid static discharge wicks | shd.coilwinder | 40 | 1 cer-007, 1 met-006, 1 pwr-001 | 2 shd-030 | — |
| wind a cryo coil spool | shd.coilwinder | 120 | 2 shd-086, 1 shd-025, 1 shd-022, 1 pwr-001 | 1 shd-031 | — |
| bottle magnetic flux | shd.coilwinder | 70 | 1 shd-023, 1 cer-029, 1 pwr-001 | 1 shd-032 | — |
| cast dielectric film | shd.capshop | 60 | 1 pol-032, 1 pwr-001 | 2 shd-033 | — |
| roll capacitor foil | shd.capshop | 40 | 1 met-039, 1 pwr-001 | 2 shd-034 | — |
| roll capacitor cells | shd.capshop | 80 | 1 shd-033, 1 shd-034, 1 ecp-031, 1 pwr-001 | 2 shd-035 | — |
| make capacitor housings | shd.capshop | 60 | 1 met-055, 1 pol-009, 1 pwr-001 | 2 shd-036 | — |
| stamp terminal cap sets | shd.capshop | 30 | 1 met-037, 1 pwr-001 | 3 shd-037 | — |
| stack a capacitor bank | shd.capshop | 200 | 3 shd-004, 1 pwr-054, 1 pwr-034, 1 pwr-001 | 1 shd-038 | — |
| pack a shield cell | shd.capshop | 110 | 1 shd-035, 1 pwr-006, 1 shd-036, 1 pwr-001 | 1 shd-039 | — |
| pack a standby shield pack | shd.capshop | 160 | 1 shd-039, 1 shd-004, 1 ecp-049, 1 pwr-001 | 1 shd-040 | — |
| fill a charge reservoir jar | shd.capshop | 90 | 1 shd-035, 1 pak-009, 1 shd-037, 1 pwr-001 | 1 shd-041 | — |
| fuse lens blanks | shd.lensworks | 60 | 1 cer-013, 1 pwr-001 | 2 shd-043 | — |
| grind a shield lens | shd.lensworks | 80 | 1 shd-043, 1 shd-049, 1 pwr-001 | 1 shd-044 | — |
| mix antiflare coating | shd.lensworks | 40 | 1 chm-058, 1 chm-034, 1 pwr-001 | 3 shd-045 | — |
| coat a shield lens | shd.lensworks | 60 | 1 shd-044, 1 shd-045, 1 pwr-001 | 1 shd-046 | — |
| turn focusing rings | shd.lensworks | 60 | 1 met-027, 1 pwr-001 | 2 shd-047 | — |
| assemble a lens barrel | shd.lensworks | 90 | 1 shd-047, 1 shd-050, 1 met-055, 1 pwr-001 | 1 shd-048 | — |
| mix lens polish paste | shd.lensworks | 40 | 1 cer-039, 1 pol-064, 1 pwr-001 | 3 shd-049 | — |
| turn lens seat rings | shd.lensworks | 40 | 1 met-051, 1 pol-009, 1 pwr-001 | 2 shd-050 | — |
| build a wide projector lens | shd.lensworks | 200 | 1 shd-007, 1 shd-046, 1 shd-048, 1 pwr-001 | 1 shd-051 | — |
| coat a plasma glass pane | shd.lensworks | 140 | 1 cer-055, 1 shd-045, 1 pwr-001 | 1 shd-052 | — |
| plate a field emitter | shd.fieldlab | 130 | 1 met-035, 1 shd-005, 1 pwr-001 | 1 shd-053 | — |
| fill plasma gas cells | shd.fieldlab | 60 | 1 gas-014, 1 cer-019, 1 pwr-001 | 2 shd-054 | — |
| build a field stabilizer board | shd.fieldlab | 130 | 1 ecp-007, 1 ecp-035, 1 cer-068, 1 pwr-001 | 1 shd-055 | — |
| weave a containment mesh | shd.fieldlab | 200 | 1 shd-053, 1 shd-055, 1 met-058, 1 pwr-001 | 1 shd-056 | — |
| build a shield node | shd.fieldlab | 180 | 1 shd-004, 1 shd-053, 1 shd-010, 1 shd-055, 1 pwr-001 | 1 shd-057 | — |
| build a local shield cell | shd.fieldlab | 180 | 1 shd-004, 1 shd-023, 1 shd-055, 1 pwr-001 | 1 shd-058 | — |
| build an emitter housing | shd.fieldlab | 120 | 1 cer-083, 1 hul-009, 1 shd-026, 1 pwr-001 | 1 shd-059 | — |
| flash an emitter control card | shd.fieldlab | 140 | 1 shd-055, 1 ecp-040, 1 pwr-001 | 1 shd-060 | — |
| pack a shield booster | shd.fieldlab | 220 | 1 shd-057, 1 shd-058, 1 shd-060, 1 pwr-001 | 1 shd-061 | — |
| calibrate an emitter card | shd.fieldlab | 150 | 1 shd-060, 1 nav-009, 1 pwr-001 | 1 shd-062 | — |
| build an emergency storm cell | shd.fieldlab | 240 | 1 shd-057, 1 shd-074, 1 shd-038, 1 pwr-001 | 1 shd-063 | — |
| twist aramid net cord | shd.netloom | 60 | 2 fib-030, 1 pwr-001 | 3 shd-065 | — |
| turn net knot rings | shd.netloom | 40 | 1 met-050, 1 pwr-001 | 4 shd-066 | — |
| weight an edge cable | shd.netloom | 60 | 1 shd-065, 1 met-066, 1 pwr-001 | 1 shd-067 | — |
| knot a heavy debris net | shd.netloom | 120 | 2 shd-006, 1 shd-067, 1 pwr-001 | 1 shd-068 | — |
| knot a capture net | shd.netloom | 180 | 1 shd-068, 2 shd-067, 1 shd-066, 1 pwr-001 | 1 shd-069 | — |
| knot net repair patches | shd.netloom | 40 | 1 shd-065, 1 shd-066, 1 pwr-001 | 2 shd-070 | — |
| cut piezo pickups | shd.fieldlab | 50 | 1 cer-053, 1 met-006, 1 pwr-001 | 2 shd-071 | — |
| bond strain plates | shd.fieldlab | 50 | 1 lgt-041, 1 met-007, 1 pwr-001 | 2 shd-072 | — |
| build sensor amplifiers | shd.fieldlab | 80 | 1 shd-071, 1 shd-072, 1 ecp-061, 1 pwr-001 | 2 shd-073 | — |
| build a micrometeoroid counter | shd.fieldlab | 140 | 1 shd-010, 1 ecp-007, 1 shd-073, 1 pwr-001 | 1 shd-074 | — |
| build a storm warning sensor | shd.fieldlab | 120 | 1 shd-073, 1 lgt-037, 1 ecp-007, 1 pwr-001 | 1 shd-075 | — |
| net impact sensors | shd.fieldlab | 200 | 1 shd-074, 1 shd-075, 2 shd-010, 1 ecp-014, 1 pwr-001 | 1 shd-076 | — |
| build a shield status lamp | shd.fieldlab | 60 | 1 ecp-070, 1 pol-045, 1 pwr-001 | 1 shd-077 | — |
| fire lead wall tiles | shd.tilekiln | 50 | 1 shd-011, 1 cer-002, 1 shd-018, 1 pwr-001 | 2 shd-078 | — |
| fire a boron wall panel | shd.tilekiln | 80 | 1 shd-012, 1 cer-005, 1 pwr-001 | 1 shd-079 | — |
| build a radiation bunk screen | shd.tilekiln | 100 | 1 shd-079, 1 shd-011, 1 fib-008, 1 pwr-001 | 1 shd-080 | — |
| sew a cabin radiation curtain | shd.netloom | 80 | 1 fib-008, 1 shd-011, 1 pwr-001 | 1 shd-081 | — |
| coat a radiation shade pane | shd.lensworks | 100 | 1 cer-015, 1 shd-045, 1 pwr-001 | 1 shd-082 | — |
| build a solar flare shelter pad | shd.tilekiln | 100 | 1 shd-079, 1 shd-078, 1 fur-006, 1 pwr-001 | 1 shd-083 | — |
| fire an ablative wall plate | shd.tilekiln | 100 | 1 shd-003, 1 cer-005, 1 pwr-001 | 1 shd-084 | — |
| line hatch shield seals | shd.tilekiln | 60 | 1 hul-010, 1 shd-011, 1 pwr-001 | 2 shd-085 | — |
| tape superconducting coil | shd.coilwinder | 90 | 1 met-040, 1 chm-076, 1 pwr-001 | 2 shd-086 | — |
| build a shield harmonic tuner | shd.fieldlab | 120 | 1 shd-055, 1 ecp-013, 1 pwr-001 | 1 shd-087 | — |
| build a radiation storm baffle | shd.fieldlab | 160 | 2 shd-011, 1 shd-016, 1 shd-005, 1 pwr-001 | 1 shd-088 | — |
| turn a winding spindle | any.bench | 60 | 1 mec-006, 1 mec-004 | 1 shd-089 | — |
| cut a capacitor press plate | any.bench | 40 | 1 met-005, 1 mec-001 | 1 shd-090 | — |
| wind a kiln heating element | any.bench | 50 | 1 met-047, 1 cer-035 | 1 shd-091 | — |
| bond a lens polishing wheel | any.bench | 50 | 1 cer-039, 1 fib-005 | 1 shd-092 | — |
| grease field lab vacuum seals | any.bench | 40 | 1 pol-009, 1 pol-076 | 2 shd-093 | — |
| carve a net loom shuttle | any.bench | 50 | 1 met-008, 1 mec-005 | 1 shd-094 | — |
| assemble a shield coil winder kit | any.bench | 150 | 1 fur-001, 1 shd-089, 1 mec-010 | 1 shd-095 | — |
| assemble a capacitor shop kit | any.bench | 120 | 1 fur-001, 1 shd-090, 1 mec-043 | 1 shd-096 | — |
| assemble a tile kiln kit | any.bench | 120 | 1 fur-001, 1 shd-091, 2 cer-042 | 1 shd-097 | — |
| assemble a lens works kit | any.bench | 120 | 1 fur-001, 1 shd-092, 1 mec-010 | 1 shd-098 | — |
| assemble a field lab kit | any.bench | 180 | 2 fur-001, 1 shd-093, 1 mec-042, 1 ecp-045 | 1 shd-099 | — |
| assemble a net loom kit | any.bench | 120 | 1 fur-001, 1 shd-094, 1 mec-011 | 1 shd-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| shd.coilwinder | Winding machine for magnetic and deflector coils, coil arrays, cryo jackets and quench protectors. | Tension set, rev 5. Turns counted by machine. Machine counted twice. |
| shd.capshop | Shop that rolls capacitor cells, builds capacitors and banks, and recharges depleted capacitors. | DISCHARGE BEFORE TOUCHING. GROUND STRAP MANDATORY. |
| shd.tilekiln | Kiln that fires ablative tiles and panels, and the lead and boron tiles that shield the cabin. | HOT SURFACE. DO NOT DRY GARMENTS ON KILN. |
| shd.lensworks | Shop that grinds, coats and barrels projector lenses, and coats plasma glass and shade panes. | Lens breakage is charged at replacement cost plus handling. Ref 2290/L. |
| shd.fieldlab | Lab that builds emitters, field generators, shield nodes, plasma windows and impact sensors. | Makes the ship's armour. The lab itself is not armoured. |
| shd.netloom | Loom that knots debris nets from aramid cord and sews radiation curtains. | Knot count per square metre per Spec 61. Short counts are rewoven. |
| shd-001 | Core shield good that raises the ship's shield and leaves a burnt-out head to rebuild. | Emitter heads are rebuilt, not replaced. Replacement is not budgeted. |
| shd-002 | Wound coil that bends charged particles away; used in emitters and field generators. | STRONG MAGNETIC FIELD. REMOVE TOOLS AND IMPLANTS. |
| shd-003 | Tile that burns away in place of the hull; a small shield. | Burns so the hull does not. The hull is valued higher. |
| shd-004 | Stored charge for the shield; leaves a depleted capacitor to recharge. | Charged, tested, sealed. Do not short terminals to confirm. |
| shd-005 | Cored magnetic coil, the base of deflectors, coil arrays, emitter plates and hall thrusters. | Coils are numbered and tracked. Unaccounted coils are investigated. |
| shd-006 | Knotted net that catches small debris. | Report holes on Form 73N after each pass. Holes do not wait for forms. |
| shd-007 | Mounted lens that focuses the shield; also used in emitters and plasma windows. | OPTICAL ASSEMBLY. DO NOT REMOVE CAP IN DUST. |
| shd-008 | Large field unit of coils, mesh and a computer core that raises the shield strongly. | STAND CLEAR 2 M WHILE ENERGISED. |
| shd-009 | Pane of contained plasma that shields strongly. | Not a window. Requisitions call it one. |
| shd-010 | Sensor that registers debris strikes, used in shield nodes, counters and sensor nets. | Sensitivity set high per bulletin 40. False alarms logged and ignored. |
| shd-011 | Rolled lead foil for wall tiles, screens, curtains, seals and storm baffles. | LEAD. WASH HANDS BEFORE MEALS. |
| shd-012 | Ground boron glass for ablative resin, tile blanks and wall panels. | Frit dust is not a respiratory hazard per Company assessment 19. |
| shd-013 | Resin that chars away under heat, used in ablative tiles and spray coating. | Smells of burnt toast while curing. Nobody aboard has had toast. |
| shd-014 | Pressed blank fired into ablative tiles. | Green state. Do not stack more than six. |
| shd-015 | Thicker ablative tile that shields better; used in tile panels and aegis panels. | STORM FACE. MOUNT THIS SIDE OUT. |
| shd-016 | Panel of heavy ablative tiles that raises the shield well, and part of a storm baffle. | Panel mass is charged to the station's mass allowance. |
| shd-017 | Flexible aramid mat faced with ablative tile. | Flex tested 400 cycles. Cracked at 401. Passed. |
| shd-018 | Adhesive for tiles, panels and mats; dries out on the shelf. | RESEAL AFTER USE. SHELF LIFE LIMITED. |
| shd-019 | Can of ablative coating that adds a small shield and leaves the empty can. | Apply to thin areas only. Overspray is logged as waste. Proc 233. |
| shd-020 | Heavy panel of tile and boron that shields strongly. | Somebody in an office named it. Somebody else mounts it. |
| shd-021 | Enamelled wire for coils and quench protectors. | Enamel continuity checked on a 1 m sample. Remaining length assumed. |
| shd-022 | Ceramic former that coils are wound on. | CERAMIC. DO NOT DROP. DO NOT REPAIR. |
| shd-023 | Wound coil cored into magnetic coils, flux bottles and local shield cells. | Round and round, all shift. The coil gets somewhere. |
| shd-024 | Stack of iron laminations for coil cores. | Iron is accounted by mass. Shortfalls are deducted by mass. |
| shd-025 | Aerogel cryo jacket that keeps coils cold. | CRYOGENIC. INSULATED GLOVES REQUIRED. |
| shd-026 | Circuit that protects a cold coil when it warms suddenly; used in deflectors and emitter housings. | Trip threshold verified. Last trip unexplained. Filed. |
| shd-027 | Insulating film wrapped around coils. | Overlap each turn by half. Proc 88. Gaps are arcs waiting to happen. |
| shd-028 | Two paired magnetic coils that raise the shield. | MATCHED PAIR. DO NOT SEPARATE. |
| shd-029 | Array of cooled coils that raises the shield and is used in field generators. | Array output is reported per coil. Underperforming coils are reassigned. |
| shd-030 | Braided wick that bleeds static charge off the hull. | Grounds the ship. Nothing grounds the crew. |
| shd-031 | Superconducting spool for deflector coils; a small shield on its own. | Kept cold since winding. Warm-up voids warranty. Warranty not issued. |
| shd-032 | Glass dome of contained magnetic flux that adds to the shield. | MAGNETIC CONTAINMENT. DO NOT INVERT. |
| shd-033 | Cast film that separates capacitor foils. | Thickness gauged at three points. Fourth point not gauged. |
| shd-034 | Metal foil for capacitor cells. | Foil offcuts are recoverable. Discarded offcuts are traced. |
| shd-035 | Rolled cell of foil and film for capacitors, shield cells and reservoir jars. | MAY HOLD CHARGE. SHORT BEFORE HANDLING. |
| shd-036 | Housing for capacitors and shield cells. | Seam welded, leak tested, stamped. Stamp upside down. |
| shd-037 | Set of terminal caps for capacitors and reservoir jars. | RED POSITIVE. BLACK NEGATIVE. NO EXCEPTIONS. |
| shd-038 | Bank of shield capacitors that raises the shield strongly and leaves depleted capacitors. | Bank discharge events are reported within one shift. Form 31D, three copies. |
| shd-039 | Battery-backed cell pack for the shield. | State of charge nominal. Nominal redefined in rev 6. |
| shd-040 | Reserve pack for the shield. | Deploy only on storm warning. Unauthorised deployment is charged. Proc 140. |
| shd-041 | Jar of stored charge that adds a small shield. | LIVE CHARGE. KEEP UPRIGHT. KEEP AWAY FROM WET HANDS. |
| shd-042 | Spent shield capacitor, recharged at the capacitor shop or scrapped as electronic scrap. | Depleted units remain on station inventory until recharged or written off. |
| shd-043 | Fused glass blank ground into shield lenses. | Bubble count acceptable. Acceptable revised, rev 3. |
| shd-044 | Ground lens awaiting coating before it is mounted. | UNCOATED. STORE IN DARK. |
| shd-045 | Antiglare coating for lenses, plasma glass and shade panes. | Coating stock is issued by area coated. Waste is measured. |
| shd-046 | Coated lens ready to mount in a projector lens. | Coating even. Smudge outside clear aperture. Passed. |
| shd-047 | Turned ring for lens barrels. | Turn slowly. Fast turns end in a requisition. |
| shd-048 | Barrel that holds projector lenses in alignment. | ALIGNMENT CRITICAL. DO NOT USE AS LEVER. |
| shd-049 | Polishing paste for grinding shield lenses. | Apply sparingly. One tube per forty lenses. Proc 47. |
| shd-050 | Ring that seats a lens in its barrel. | Thread checked by gauge. Gauge itself overdue for check. |
| shd-051 | Doubled projector lens that throws a wider shield. | Wider coverage does not alter station liability. Notice 52. |
| shd-052 | Coated glass for the plasma window. | FRAGILE. GLASS. COF PROPERTY. |
| shd-053 | Plated emitter for shield nodes, containment mesh and rebuilt emitters. | Plating thickness within spec at edges. Centre not measured. |
| shd-054 | Sealed cell of argon for the plasma window. | PRESSURISED ARGON. DO NOT PUNCTURE. |
| shd-055 | Board that keeps the field steady, used in nodes, cells, cards and tuners. | Field wobble is logged automatically. Logs are reviewed at contract renewal. |
| shd-056 | Woven mesh that holds the field and raises the shield. | Woven by hand, inspected by eye, trusted by necessity. |
| shd-057 | Node of capacitor, emitter plate, sensor and stabilizer board that raises the shield. | One node of many. Serial ground off. Reissued SN 2214 0093. |
| shd-058 | Small self-contained shield cell. | Covers a small patch of hull. Pick the patch carefully. |
| shd-059 | Housing of a shield emitter. | HIGH VOLTAGE INSIDE. NO OPERATOR SERVICEABLE PARTS. |
| shd-060 | Flashed card that controls emitters; a small shield on its own. | Firmware rev 14. Rev 13 recalled. Rev 12 still in service. |
| shd-061 | Pack of shield node, cell and control card that boosts the shield strongly. | Booster use is reserved for declared storms. Undeclared storms are not recognised. |
| shd-062 | Calibrated control card that raises the shield more than an uncalibrated one. | Recalibrate after every storm. Form 66E, signed by calibrating personnel. |
| shd-063 | Storm cell of shield node, counter and capacitor bank; the strongest shield good. | EMERGENCY USE ONLY. BREAK SEAL. LOG BREAK. |
| shd-064 | Spent emitter head, rebuilt at the field lab or stripped for scrap. | Burnt heads are returned, not discarded. Count them. Ref 7713/E. |
| shd-065 | Twisted aramid cord for nets, edge cables and patches. | Break load tested on one sample in fifty. |
| shd-066 | Metal ring fitted at the knots of a net. | Count them twice. They roll under everything. |
| shd-067 | Weighted cable along the edge of heavy and capture nets. | WEIGHTED. LIFT WITH TWO PERSONNEL. |
| shd-068 | Doubled debris net with a weighted edge that catches more debris. | Debris recovered by net is Company salvage. Salvage is not shared. |
| shd-069 | Largest net, which catches debris best. | Deployed, recovered, patched, redeployed. Count 9. |
| shd-070 | Knotted patch that mends a net and adds a small shield. | Patch holes larger than a fist. Smaller holes are logged. Proc 160. |
| shd-071 | Crystal pickup that registers impacts, for sensor amplifiers. | SENSITIVE ELEMENT. DO NOT TAP TO TEST. |
| shd-072 | Metal plate with strain gauges, for sensor amplifiers. | Zero offset noted. Offset assumed permanent. |
| shd-073 | Amplifier for impact sensors, counters and storm warning sensors. | Turns a whisper into a report. Nobody reads the report. |
| shd-074 | Counter that tallies debris hits for the shield. | Impact counts are compiled quarterly. Hull wear is the operator's concern. |
| shd-075 | Infrared sensor that warns of radiation storms. | On alarm, proceed to shelter pad. Log the alarm afterwards. Proc 1. |
| shd-076 | Network of impact sensors that raises the shield. | Coverage 94 percent. Missing 6 percent under review. |
| shd-077 | Cabin lamp that shows the shield's state, giving a little light and calm. | GREEN NOMINAL. AMBER STANDBY. RED SHELTER. |
| shd-078 | Lead tile that lowers the crew's radiation dose while it stands in the cabin. | Shielding is issued at regulation minimum. Additional shielding is self-funded. |
| shd-079 | Boron panel that lowers radiation dose, and part of screens, pads and aegis panels. | Neutron count at bunk reduced. Count still above zero. |
| shd-080 | Screen by the bunk that lowers radiation dose well. | Shields the head end of the bunk. Feet are at operator discretion. |
| shd-081 | Lead-lined curtain that lowers radiation dose. | LEAD LINED. DO NOT USE AS BLANKET. |
| shd-082 | Coated pane that admits light but lowers radiation dose. | View ports are a privilege of contract grade C and above. |
| shd-083 | Shielded pad that lowers radiation dose well and aids rest. | During flare alert, lie flat on pad. Remain until all clear. Proc 9A. |
| shd-084 | Ablative plate on the cabin wall that lowers radiation dose. | Fitted over previous plate. Previous plate not removed. |
| shd-085 | Spare lead-lined seal for the service hatch; wears into rubber scrap. | REPLACE AT FIRST CRACK. HATCH SEALS ARE COUNTED. |
| shd-086 | Superconducting tape for cryo coil spools. | Critical current verified per batch. Batch size: one roll. |
| shd-087 | Tuner that holds the shield field in tune. | Tune by ear when the readout fails. It fails. |
| shd-088 | Baffle of lead foil, tile panel and coil against radiation storms. | Exposure beyond baffle rating is classed as an act of nature. Not covered. |
| shd-089 | Spare winding spindle for the shield coil winder. | Runout checked. Runout present. Runout accepted. |
| shd-090 | Spare press plate for the capacitor shop. | HEAVY. TWO HANDS. KEEP FINGERS CLEAR OF PLATEN. |
| shd-091 | Spare heating element for the tile kiln. | Glows orange when working. Stays dark when not. Check before reaching in. |
| shd-092 | Spare polishing wheel for the lens works. | Dress the wheel each shift. Undressed wheels scratch. Proc 31. |
| shd-093 | Spare vacuum seal for the field lab; wears into rubber scrap. | Vacuum is a Company resource. Leaks are metered. |
| shd-094 | Spare shuttle for the net loom. | Shuttle worn at nose. Nose reshaped. Shuttle reissued. |
| shd-095 | Packed kit that installs a shield coil winder. | WIRE NOT INCLUDED. SEE REQUISITION 4. |
| shd-096 | Packed kit that installs a capacitor shop. | Shipped discharged. Residual charge is the receiving station's responsibility. |
| shd-097 | Packed kit that installs a tile kiln. | UNPACK BEFORE FIRING. |
| shd-098 | Packed kit that installs a lens works. | Packed in foam. Foam to be returned. Foam is counted. |
| shd-099 | Packed kit that installs a field lab. | Installation constitutes acceptance of the field lab as delivered. Ref 0099/F. |
| shd-100 | Packed kit that installs a net loom. | The loom arrives in pieces. The pieces arrive tangled. |
