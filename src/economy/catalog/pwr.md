# Power & Cabling — `pwr`

`pwr-001` Power, the unit of energy most ways take, and everything that makes, stores and carries it. The reactor burns
fuel slugs, the solar array and the fuel cell stack make power without them, and the charging bay stores it in cells and
batteries that run down on the shelf, are recharged, and at last go dead to recycling. Wire from the foundry (`met`) is
insulated into cable, leads and harnesses and wound into coils that every device kit takes; fuses, breakers, regulators, panels
and transformers go into the grid at the service hatch for `ship.grid`, and the fuse, breaker or regulator they replace
comes back blown, tripped or burnt, to be reset or scrapped. Spent fuel and spent rods are sealed into casks and left
to cool.

## Devices

| id | device | role | cells |
|---|---|---|---|
| pwr.reactor | PG900 Fission Reactor | power | 3x2 |
| pwr.solararray | PG310 Solar Array | power | 3x2 |
| pwr.fuelstack | PG240 Fuel Cell Stack | power | 2x2 |
| pwr.charger | PG55 Charging Bay | power | 2x1 |
| pwr.cellline | PG120 Cell Line | power | 2x2 |
| pwr.cableline | PG140 Cable and Coil Line | power | 2x1 |
| pwr.switchbench | PG160 Switchgear Bench | power | 2x2 |

## Items

| id | item | use | decays |
|---|---|---|---|
| pwr-001 | Power, Grid | — | — |
| pwr-002 | Cell, Charged | — | 720 h → pwr-003 |
| pwr-003 | Cell, Spent | — | 480 h → pwr-004 |
| pwr-004 | Cell, Dead | — | — |
| pwr-005 | Cable, Insulated | — | — |
| pwr-006 | Pack, Battery | — | 1440 h → pwr-007 |
| pwr-007 | Pack, Battery, Spent | — | 720 h → scr-003 |
| pwr-008 | Fuse | ship.grid +2, leaves 1 pwr-011 | — |
| pwr-009 | Breaker | ship.grid +5, leaves 1 pwr-012 | — |
| pwr-010 | Regulator, Grid | ship.grid +15, leaves 1 pwr-013 | — |
| pwr-011 | Fuse, Blown | — | — |
| pwr-012 | Breaker, Tripped | — | — |
| pwr-013 | Regulator, Grid, Burnt | — | — |
| pwr-014 | Cable, Power | — | — |
| pwr-015 | Lead, Power | — | — |
| pwr-016 | Harness, Wiring | — | — |
| pwr-017 | Box, Junction | — | — |
| pwr-018 | Relay | — | — |
| pwr-019 | Panel, Solar | — | — |
| pwr-020 | Slug, Fuel | — | — |
| pwr-021 | Slug, Fuel, Spent | — | — |
| pwr-022 | Coil, Transformer | — | — |
| pwr-023 | Cell, Button | — | 2000 h → pwr-004 |
| pwr-024 | Battery, Lead Acid | — | 720 h → pwr-025 |
| pwr-025 | Battery, Lead Acid, Flat | — | 480 h → scr-003 |
| pwr-026 | Electrode, Carbon | — | — |
| pwr-027 | Plate, Anode, Zinc | — | — |
| pwr-028 | Powder, Cathode, Lithium | — | — |
| pwr-029 | Plate, Cathode, Nickel | — | — |
| pwr-030 | Plate, Grid, Lead | — | — |
| pwr-031 | Paste, Cell Electrolyte | — | — |
| pwr-032 | Film, Cell Separator | — | — |
| pwr-033 | Casing, Cell | — | — |
| pwr-034 | Casing, Battery Pack | — | — |
| pwr-035 | Pellet, Fuel, Uranium | — | — |
| pwr-036 | Uranium Oxide, Enriched | — | — |
| pwr-037 | Uranium, Depleted | — | — |
| pwr-038 | Tube, Slug Cladding | — | — |
| pwr-039 | Cask, Fuel | — | — |
| pwr-040 | Cask, Fuel, Sealed | — | 2000 h |
| pwr-041 | Rod, Control, Spent | — | — |
| pwr-042 | Cell, Photovoltaic | — | — |
| pwr-043 | String, Solar Cell | — | — |
| pwr-044 | Tile, Solar, Degraded | — | — |
| pwr-045 | Controller, Charge | — | — |
| pwr-046 | Inverter, Power | ship.grid +6 | — |
| pwr-047 | Wire, Winding, Enamelled | — | — |
| pwr-048 | Cable, Shielded | — | — |
| pwr-049 | Cable, Trunk, Armoured | ship.grid +8, leaves 1 pwr-050 | — |
| pwr-050 | Cable, Scrap | — | — |
| pwr-051 | Gland, Cable | — | — |
| pwr-052 | Sleeve, Heat Shrink | — | — |
| pwr-053 | Block, Terminal | — | — |
| pwr-054 | Bar, Bus | — | — |
| pwr-055 | Clamp, Cable | — | — |
| pwr-056 | Terminal, Crimp | — | — |
| pwr-057 | Tape, Insulating, Mica | — | — |
| pwr-058 | Splice, Cable | ship.grid +3 | — |
| pwr-059 | Strap, Ground | ship.grid +1 | — |
| pwr-060 | Bus, Distribution | ship.grid +6 | — |
| pwr-061 | Contact Set, Breaker | — | — |
| pwr-062 | Wire, Fuse | — | — |
| pwr-063 | Contactor | — | — |
| pwr-064 | Arrester, Surge | ship.grid +4 | — |
| pwr-065 | Transformer, Isolation | ship.grid +8 | — |
| pwr-066 | Transformer, Step-Down | ship.grid +6 | — |
| pwr-067 | Switch, Transfer | ship.grid +6 | — |
| pwr-068 | Panel, Power Distribution | ship.grid +10 | — |
| pwr-069 | Balancer, Load | ship.grid +12 | — |
| pwr-070 | Corrector, Phase | ship.grid +10 | — |
| pwr-071 | Interrupter, Arc Fault | ship.grid +8 | — |
| pwr-072 | Battery Bank, Reserve | ship.grid +12 | — |
| pwr-073 | Stabilizer, Grid | ship.grid +20 | — |
| pwr-074 | Core, Regulator | — | — |
| pwr-075 | Core, Ferrite | — | — |
| pwr-076 | Coil, Inductor | — | — |
| pwr-077 | Supercapacitor | — | — |
| pwr-078 | Enclosure, Panel | — | — |
| pwr-079 | Coil, Generator | — | — |
| pwr-080 | Resistor, Shunt | — | — |
| pwr-081 | Plate, Bipolar | — | — |
| pwr-082 | Module, Thermoelectric | — | — |
| pwr-083 | Rod, Control | fits pwr.reactor | 1200 h → pwr-041 |
| pwr-084 | Block, Neutron Moderator | fits pwr.reactor | 2000 h → scr-004 |
| pwr-085 | Seal, Reactor Coolant | fits pwr.reactor | 600 h → scr-002 |
| pwr-086 | Tile, Solar Array | fits pwr.solararray | 1200 h → pwr-044 |
| pwr-087 | Cell, Solar Strip | fits any.solarstrip | 1200 h → pwr-044 |
| pwr-088 | Membrane, Fuel Cell | fits pwr.fuelstack | 500 h → scr-002 |
| pwr-089 | Plate, Catalyst | fits pwr.fuelstack | 800 h → scr-001 |
| pwr-090 | Contact Set, Charger | fits pwr.charger | 600 h → scr-001 |
| pwr-091 | Die, Cell Press | fits pwr.cellline | 800 h → scr-004 |
| pwr-092 | Die, Cable Extruder | fits pwr.cableline | 800 h → scr-004 |
| pwr-093 | Tip, Soldering, Bench | fits pwr.switchbench | 300 h → scr-001 |
| pwr-094 | Kit, Fission Reactor | installs pwr.reactor | — |
| pwr-095 | Kit, Solar Array | installs pwr.solararray | — |
| pwr-096 | Kit, Fuel Cell Stack | installs pwr.fuelstack | — |
| pwr-097 | Kit, Charging Bay | installs pwr.charger | — |
| pwr-098 | Kit, Cell Line | installs pwr.cellline | — |
| pwr-099 | Kit, Cable and Coil Line | installs pwr.cableline | — |
| pwr-100 | Kit, Switchgear Bench | installs pwr.switchbench | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| burn a fuel slug | pwr.reactor | 480 | 1 pwr-020 | 20 pwr-001, 1 pwr-021 | — |
| run the solar array | pwr.solararray | 60 | — | 4 pwr-001 | — |
| run the fuel cell stack | pwr.fuelstack | 60 | 2 gas-004, 1 gas-001 | 3 pwr-001, 1 wat-018 | — |
| run a hydrogen cartridge | pwr.fuelstack | 60 | 1 gas-067, 1 gas-001 | 3 pwr-001, 1 wat-018, 1 pak-006 | — |
| discharge a cell | pwr.charger | 30 | 1 pwr-002 | 2 pwr-001, 1 pwr-003 | — |
| discharge a battery pack | pwr.charger | 60 | 1 pwr-006 | 8 pwr-001, 1 pwr-007 | — |
| discharge a lead acid battery | pwr.charger | 60 | 1 pwr-024 | 5 pwr-001, 1 pwr-025 | — |
| charge a cell | pwr.charger | 120 | 1 pwr-003, 3 pwr-001 | 1 pwr-002 | — |
| charge a battery pack | pwr.charger | 240 | 1 pwr-007, 10 pwr-001 | 1 pwr-006 | — |
| charge a lead acid battery | pwr.charger | 180 | 1 pwr-025, 6 pwr-001 | 1 pwr-024 | — |
| assemble zinc carbon cells | pwr.cellline | 60 | 1 pwr-033, 1 pwr-027, 1 pwr-026, 1 pwr-031, 1 pwr-032, 1 pwr-001 | 2 pwr-002 | — |
| assemble nickel zinc cells | pwr.cellline | 60 | 1 pwr-033, 1 pwr-029, 1 pwr-027, 1 chm-050, 1 pwr-032, 1 pwr-001 | 2 pwr-002 | — |
| assemble lithium cells | pwr.cellline | 60 | 1 pwr-033, 1 pwr-028, 1 pwr-026, 1 chm-050, 1 pwr-032, 1 pwr-001 | 3 pwr-002 | — |
| press button cells | pwr.cellline | 30 | 1 met-043, 1 pwr-027, 1 chm-072, 1 pwr-001 | 4 pwr-023 | — |
| pack a battery pack | pwr.cellline | 90 | 6 pwr-002, 1 pwr-034, 1 ecp-049 | 1 pwr-006 | — |
| build a lead acid battery | pwr.cellline | 90 | 3 pwr-030, 1 chm-050, 1 pwr-034 | 1 pwr-024 | — |
| press carbon electrodes | pwr.cellline | 30 | 2 ore-074, 1 pwr-001 | 3 pwr-026 | — |
| press briquette electrodes | pwr.cellline | 30 | 2 ore-081, 1 pwr-001 | 2 pwr-026 | — |
| cut zinc anode plates | pwr.cellline | 30 | 1 met-015, 1 pwr-001 | 3 pwr-027 | — |
| mix lithium cathode powder | pwr.cellline | 60 | 1 chm-014, 1 chm-073, 1 pwr-001 | 2 pwr-028 | — |
| mix lithium cathode from hydroxide | pwr.cellline | 60 | 1 chm-013, 1 chm-073, 1 pwr-001 | 2 pwr-028 | — |
| paste nickel cathode plates | pwr.cellline | 45 | 1 chm-074, 1 met-064, 1 pwr-001 | 2 pwr-029 | — |
| paste lead grid plates | pwr.cellline | 45 | 1 met-012, 1 chm-075, 1 pwr-001 | 2 pwr-030 | — |
| mix cell electrolyte paste | pwr.cellline | 30 | 1 chm-071, 1 chm-059, 1 chm-072, 1 wat-003 | 3 pwr-031 | — |
| cut cell separator film | pwr.cellline | 20 | 1 pol-002 | 3 pwr-032 | — |
| draw cell casings from tinplate | pwr.cellline | 30 | 1 met-043, 1 pwr-001 | 4 pwr-033 | — |
| draw cell casings from steel | pwr.cellline | 30 | 1 met-009, 1 pwr-001 | 3 pwr-033 | — |
| fit a battery pack casing | pwr.cellline | 45 | 1 pol-045, 1 pwr-056 | 1 pwr-034 | — |
| strip dead cells | pwr.cellline | 60 | 3 pwr-004, 1 pwr-001 | 1 scr-041, 1 scr-001 | — |
| make a supercapacitor | pwr.cellline | 60 | 1 chm-005, 1 met-039, 1 chm-050 | 2 pwr-077 | — |
| bank reserve batteries | pwr.cellline | 120 | 2 pwr-006, 1 pwr-045, 1 pwr-016 | 1 pwr-072 | — |
| enrich uranium | pwr.reactor | 240 | 3 ore-064, 4 pwr-001 | 1 pwr-036, 2 pwr-037 | — |
| press fuel pellets | pwr.reactor | 120 | 1 pwr-036, 1 pwr-001 | 3 pwr-035 | — |
| draw slug cladding | pwr.reactor | 60 | 1 met-054, 1 pwr-001 | 2 pwr-038 | — |
| load a fuel slug | pwr.reactor | 90 | 3 pwr-035, 1 pwr-038 | 1 pwr-020 | — |
| build a fuel cask | pwr.reactor | 120 | 2 met-005, 1 pwr-037, 2 met-066 | 1 pwr-039 | — |
| cask spent fuel | pwr.reactor | 60 | 2 pwr-021, 1 pwr-039 | 1 pwr-040 | — |
| cask spent control rods | pwr.reactor | 60 | 2 pwr-041, 1 pwr-039 | 1 pwr-040 | — |
| make a control rod | pwr.reactor | 120 | 1 met-056, 1 chm-076, 1 pwr-001 | 1 pwr-083 | — |
| press a moderator block | pwr.reactor | 120 | 3 ore-074, 1 chm-036, 2 pwr-001 | 1 pwr-084 | — |
| make a reactor coolant seal | any.bench | 30 | 1 pol-009, 1 met-034 | 1 pwr-085 | — |
| print photovoltaic cells | pwr.solararray | 60 | 1 cer-052, 1 met-032, 1 pwr-001 | 3 pwr-042 | — |
| refurbish salvaged solar cells | pwr.solararray | 60 | 2 scr-049, 1 pwr-001 | 1 pwr-042 | — |
| solder a solar cell string | pwr.solararray | 45 | 4 pwr-042, 1 met-032 | 1 pwr-043 | — |
| frame a solar panel | pwr.solararray | 90 | 2 pwr-043, 1 cer-016, 1 met-055 | 1 pwr-019 | — |
| glaze a solar array tile | pwr.solararray | 60 | 1 pwr-043, 1 cer-016 | 1 pwr-086 | — |
| refurbish degraded tiles | pwr.solararray | 60 | 2 pwr-044, 1 cer-016, 1 pwr-001 | 1 pwr-086 | — |
| glaze solar strip cells | pwr.solararray | 60 | 1 pwr-043, 1 cer-016 | 2 pwr-087 | — |
| glaze a solar strip cell by hand | any.bench | 45 | 1 pwr-043, 1 cer-001 | 1 pwr-087 | — |
| stack bipolar plates | pwr.fuelstack | 45 | 1 met-034, 1 ore-074, 1 pwr-001 | 2 pwr-081 | — |
| coat a catalyst plate | pwr.fuelstack | 60 | 1 pwr-081, 1 chm-078, 1 pwr-001 | 1 pwr-089 | — |
| cast fuel cell membranes | pwr.fuelstack | 45 | 1 pol-032, 1 pwr-001 | 2 pwr-088 | — |
| insulate cable by hand | any.bench | 60 | 1 met-006, 1 pol-063 | 1 pwr-005 | — |
| extrude insulated cable | pwr.cableline | 45 | 2 met-006, 1 pol-042, 1 pwr-001 | 3 pwr-005 | — |
| extrude power cable | pwr.cableline | 60 | 3 met-046, 1 pol-042, 1 pwr-001 | 2 pwr-014 | — |
| make power leads | pwr.cableline | 30 | 1 pwr-005, 1 pwr-056, 1 pol-048 | 2 pwr-015 | — |
| loom a wiring harness | pwr.cableline | 60 | 3 pwr-005, 2 pwr-056, 1 pwr-052, 1 pwr-055 | 1 pwr-016 | — |
| enamel winding wire | pwr.cableline | 30 | 2 met-006, 1 pol-007, 1 pwr-001 | 3 pwr-047 | — |
| braid shielded cable | pwr.cableline | 60 | 2 pwr-005, 1 met-058, 1 pol-042, 1 pwr-001 | 2 pwr-048 | — |
| armour trunk cable | pwr.cableline | 90 | 2 pwr-014, 1 met-045, 1 pwr-051, 1 pwr-001 | 1 pwr-049 | — |
| strip scrap cable | pwr.cableline | 30 | 2 pwr-050, 1 pwr-001 | 1 scr-033, 1 scr-034 | — |
| cut heat shrink sleeves | pwr.cableline | 20 | 1 pol-040 | 4 pwr-052 | — |
| lay mica insulating tape | pwr.cableline | 30 | 2 ore-076, 1 cer-061 | 3 pwr-057 | — |
| draw fuse wire | pwr.cableline | 30 | 1 met-032, 1 pwr-001 | 4 pwr-062 | — |
| draw fuse wire from ingots | pwr.cableline | 45 | 1 met-013, 1 met-012, 1 pwr-001 | 6 pwr-062 | — |
| press ferrite cores | pwr.cableline | 45 | 1 met-060, 1 chm-072, 1 pwr-001 | 2 pwr-075 | — |
| wind a transformer coil | pwr.cableline | 60 | 2 pwr-047, 1 pwr-075, 1 pwr-001 | 1 pwr-022 | — |
| wind inductor coils | pwr.cableline | 30 | 1 pwr-047, 1 pwr-075, 1 pwr-001 | 2 pwr-076 | — |
| wind a generator coil | pwr.cableline | 90 | 3 pwr-047, 1 met-077, 1 pwr-001 | 1 pwr-079 | — |
| build an isolation transformer | pwr.cableline | 120 | 2 pwr-022, 1 pwr-057, 1 pwr-078, 1 pwr-001 | 1 pwr-065 | — |
| build a step-down transformer | pwr.cableline | 90 | 1 pwr-022, 1 pwr-076, 1 pwr-053, 1 pwr-001 | 1 pwr-066 | — |
| turn cable glands | pwr.switchbench | 30 | 1 met-051, 1 pol-048 | 3 pwr-051 | — |
| make terminal blocks | pwr.switchbench | 30 | 1 met-051, 1 pol-049 | 3 pwr-053 | — |
| cut bus bars | pwr.switchbench | 45 | 1 met-037, 1 pwr-001 | 2 pwr-054 | — |
| stamp cable clamps | pwr.switchbench | 20 | 1 met-042, 1 pwr-001 | 4 pwr-055 | — |
| stamp crimp terminals | pwr.switchbench | 20 | 1 met-036, 1 pwr-001 | 6 pwr-056 | — |
| splice a cable | pwr.switchbench | 20 | 1 pwr-005, 2 pwr-056, 1 pwr-052 | 1 pwr-058 | — |
| braid ground straps | pwr.switchbench | 20 | 1 met-058, 1 pwr-056 | 2 pwr-059 | — |
| build a distribution bus | pwr.switchbench | 90 | 3 pwr-054, 1 pwr-053, 1 pwr-057, 1 pwr-001 | 1 pwr-060 | — |
| build a junction box | pwr.switchbench | 45 | 1 pwr-053, 1 pol-045, 2 pwr-051 | 1 pwr-017 | — |
| make a fuse by hand | any.bench | 30 | 1 pwr-062, 1 cer-035 | 1 pwr-008 | — |
| make fuses | pwr.switchbench | 20 | 1 pwr-062, 1 cer-071, 1 pwr-056 | 2 pwr-008 | — |
| rewire a blown fuse by hand | any.bench | 20 | 1 pwr-011, 1 pwr-062 | 1 pwr-008 | — |
| rewire blown fuses | pwr.switchbench | 15 | 2 pwr-011, 1 pwr-062 | 2 pwr-008 | — |
| sinter breaker contacts | pwr.switchbench | 30 | 1 met-036, 1 met-061, 1 pwr-001 | 2 pwr-061 | — |
| assemble a breaker | pwr.switchbench | 60 | 1 pwr-061, 1 met-048, 1 pol-045, 1 pwr-001 | 1 pwr-009 | — |
| reset a tripped breaker | pwr.switchbench | 30 | 1 pwr-012, 1 pwr-061 | 1 pwr-009 | — |
| wind relays | pwr.switchbench | 45 | 1 pwr-047, 1 met-048, 1 pwr-061 | 2 pwr-018 | — |
| build a contactor | pwr.switchbench | 60 | 2 pwr-018, 1 pwr-054, 1 pol-045 | 1 pwr-063 | — |
| build a surge arrester | pwr.switchbench | 45 | 1 cer-035, 1 chm-059, 1 pwr-056 | 1 pwr-064 | — |
| cut shunt resistors | pwr.switchbench | 20 | 1 met-047 | 4 pwr-080 | — |
| rivet a panel enclosure | pwr.switchbench | 60 | 2 met-033, 4 met-068 | 1 pwr-078 | — |
| build a regulator core | pwr.switchbench | 90 | 1 pwr-022, 1 ecp-035, 1 met-076 | 1 pwr-074 | — |
| build a grid regulator | pwr.switchbench | 120 | 1 pwr-074, 1 ecp-037, 1 pwr-080, 1 pwr-078 | 1 pwr-010 | — |
| refurbish a burnt grid regulator | pwr.switchbench | 90 | 1 pwr-013, 1 ecp-035, 1 pwr-080 | 1 pwr-010 | — |
| strip a burnt grid regulator | pwr.switchbench | 30 | 1 pwr-013 | 1 scr-035, 1 scr-001 | — |
| build a power inverter | pwr.switchbench | 120 | 1 ecp-035, 1 pwr-022, 1 met-076, 1 ecp-010 | 1 pwr-046 | — |
| build a charge controller | pwr.switchbench | 60 | 1 ecp-049, 1 cer-053, 1 pwr-053 | 1 pwr-045 | — |
| build a transfer switch | pwr.switchbench | 90 | 2 pwr-063, 1 ecp-007 | 1 pwr-067 | — |
| build a distribution panel | pwr.switchbench | 150 | 1 pwr-078, 1 pwr-060, 2 pwr-009, 1 cer-068 | 1 pwr-068 | — |
| build a load balancer | pwr.switchbench | 150 | 2 pwr-063, 1 ecp-010, 1 pwr-076, 1 pwr-048 | 1 pwr-069 | — |
| build a phase corrector | pwr.switchbench | 120 | 2 pwr-077, 1 pwr-076, 1 ecp-063 | 1 pwr-070 | — |
| build an arc fault interrupter | pwr.switchbench | 90 | 1 pwr-009, 1 ecp-047 | 1 pwr-071 | — |
| build a grid stabilizer | pwr.switchbench | 240 | 1 pwr-074, 2 pwr-077, 1 cer-026, 1 ecp-052 | 1 pwr-073 | — |
| build thermoelectric modules | pwr.switchbench | 60 | 1 cer-038, 1 met-037, 1 ore-074, 1 pwr-001 | 2 pwr-082 | — |
| sinter a charger contact set | pwr.switchbench | 30 | 1 met-061, 1 met-052, 1 pwr-001 | 1 pwr-090 | — |
| grind a cell press die | any.bench | 60 | 1 met-030 | 1 pwr-091 | — |
| grind a cable extruder die | any.bench | 60 | 1 met-030, 1 ore-079 | 1 pwr-092 | — |
| file soldering tips | any.bench | 30 | 1 met-003, 1 met-001 | 4 pwr-093 | — |
| assemble a fission reactor | any.bench | 240 | 1 pwr-083, 1 pwr-084, 2 met-041, 1 cer-041, 1 pwr-079, 1 cer-015 | 1 pwr-094 | — |
| assemble a solar array | any.bench | 240 | 4 pwr-019, 1 pwr-086, 1 pwr-045, 1 cer-080, 1 cer-024 | 1 pwr-095 | — |
| assemble a fuel cell stack | any.bench | 240 | 1 pwr-088, 1 pwr-089, 4 pwr-081, 1 cer-057, 1 chm-032, 1 pwr-082 | 1 pwr-096 | — |
| assemble a charging bay | any.bench | 180 | 1 pwr-090, 1 ecp-045, 1 pwr-015, 1 pwr-022 | 1 pwr-097 | — |
| assemble a cell line | any.bench | 180 | 1 pwr-091, 1 met-074, 1 mec-043 | 1 pwr-098 | — |
| assemble a cable and coil line | any.bench | 180 | 1 pwr-092, 1 met-074, 1 mec-010 | 1 pwr-099 | — |
| assemble a switchgear bench | any.bench | 180 | 1 pwr-093, 1 cer-083, 1 cer-075, 1 pwr-017 | 1 pwr-100 | — |
| jettison a sealed fuel cask | any.hatch | 15 | 1 pwr-040 | — | dose -5 |

## Codex

| id | about | flavour |
|---|---|---|
| pwr.reactor | Fission reactor that burns fuel slugs for grid power; also enriches uranium and produces fuel slugs, control rods and casks. | RADIATION AREA. AUTHORISED PERSONNEL ONLY. COF PROPERTY. |
| pwr.solararray | Array that generates power from sunlight without fuel; also prints, strings and glazes solar cells. | Array angle is set by the Company. Unauthorised adjustment is logged. Ref 2210/S. |
| pwr.fuelstack | Stack that combines hydrogen and oxygen into power and clean water; also produces its own plates and membranes. | Product water is not certified for drinking until processed. Proc 61 applies. |
| pwr.charger | Bay that charges spent cells and batteries from the grid and discharges full ones back into power. | CHARGED LEFT. FLAT RIGHT. DO NOT MIX. |
| pwr.cellline | Line that builds cells, batteries, button cells and supercapacitors, with the electrodes and casings they need. | Line output is audited per shift. Shortfall is entered against the operating station. |
| pwr.cableline | Line that insulates wire into cable and harnesses, winds coils and transformers, and draws fuse wire. | Spool tension checked, rev 4. Extruder die replaced twice this quarter. |
| pwr.switchbench | Bench that builds and repairs fuses, breakers, regulators, panels and the other grid equipment the ship runs on. | Iron left hot again. Somebody is going to lose a hand, and it will be logged as negligence. |
| pwr-001 | Electrical energy consumed by nearly every device and way aboard, generated by reactor, array, fuel cells, solar strips and cells. | Consumption is metered per station and reviewed at contract renewal. |
| pwr-002 | Full rechargeable cell that powers small equipment and packs into batteries; it self-discharges slowly on the shelf. | Shaking a cell does not restore charge. Notice 88 refers. |
| pwr-003 | Discharged cell awaiting the charging bay; left too long it goes dead. | Charge it now or bury it later. |
| pwr-004 | Cell that no longer holds charge, stripped for black mass and scrap. | DEAD CELLS TO RECYCLING. NOT TO BULKHEAD VOIDS. |
| pwr-005 | Insulated copper wire for leads, harnesses, splices and the wiring of most equipment. | Colour code per Proc 302. The green conductor is not to be discussed. |
| pwr-006 | Pack of cells for drones, beacons and shields, or for discharge into power; it runs down slowly on the shelf. | Lift with the legs. Back injuries are not covered under the operating contract. |
| pwr-007 | Discharged battery pack, recharged in the charging bay or, left too long, lost to electronic scrap. | Recharge within shelf limit. Packs lost to neglect are charged to the station. |
| pwr-008 | Fuse fitted into the grid at the service hatch to strengthen it; in time it blows and returns. | Sacrificial component. Replace like for like. Form 19F. |
| pwr-009 | Resettable switch fitted into the grid; it trips in service and returns for resetting. | Tripped. Reset. Tripped. Reset. Third time, read the load sheet. |
| pwr-010 | Regulator that strongly reinforces the ship's grid; it burns out in service and returns for refurbishing. | Tested under load, passed, rev 11. Faint whine within tolerance. |
| pwr-011 | Fuse returned from the grid after overload, rewired with fuse wire into a serviceable one. | BLOWN. RETURN TO BENCH. DO NOT REFIT. |
| pwr-012 | Breaker returned from the grid, reset with fresh contacts. | Reset logs are reviewed. Excessive trips are attributed to the last station that drew load. |
| pwr-013 | Regulator burnt out in service, refurbished at the bench or stripped for scrap. | Smells like the shift nobody filed a report on. |
| pwr-014 | Heavy aluminium cable, armoured into trunk cable for the grid. | Minimum bend radius applies. Kinked cable is scrapped at the operator's cost. |
| pwr-015 | Short cable with crimped ends, used to connect charging bays. | Two ends, one job. Both ends are COF property. |
| pwr-016 | Loomed bundle of cable required by every large device kit and coil array. | Harness to drawing H22. Deviations require Form 40W, countersigned. |
| pwr-017 | Sealed box where cables meet, for kilns and switchgear benches. | LABEL ALL CIRCUITS. UNLABELLED BOXES WILL BE CONDEMNED. |
| pwr-018 | Small coil-driven switch, built into contactors. | Click once is on. Anything else, tag it out. |
| pwr-019 | Framed solar cell strings behind tempered glass, the main part of a solar array. | Wipe dust weekly. Cleaning time is not billable. Notice 503. |
| pwr-020 | Clad uranium pellets, burnt in the reactor for a large yield of power. | HANDLE WITH TONGS. FISSILE. COF PROPERTY. |
| pwr-021 | Burnt-out fuel, still hot, sealed into a fuel cask for disposal. | Spent fuel remains Company property until jettisoned. Ref 7713/R. |
| pwr-022 | Copper winding on a ferrite core, for transformers, regulators, inverters and charging bays. | Turns counted, insulation tested, rev 3. Counter reset twice. |
| pwr-023 | Small single-use cell for smoke detectors and head lamps; it lasts long, then dies. | Always under the bunk. Never in the drawer. |
| pwr-024 | Heavy rechargeable battery, discharged for power; it runs flat on the shelf over time. | CORROSIVE. KEEP UPRIGHT. DO NOT STACK ABOVE SHOULDER HEIGHT. |
| pwr-025 | Run-down lead acid battery, recharged in the bay or smelted once it degrades to electronic scrap. | Acid spills are reported on Form 66A before cleaning, not after. |
| pwr-026 | Pressed carbon rod, the electrode of zinc carbon and lithium cells. | Brittle. Dropped electrodes are scrap and counted as such. |
| pwr-027 | Cut zinc plate, the negative side of zinc carbon, nickel zinc and button cells. | NEGATIVE. MARK FACE DOWN. |
| pwr-028 | Lithium and cobalt oxide powder for the cathode of lithium cells. | Controlled material. Weigh in, weigh out. Discrepancies are investigated. |
| pwr-029 | Nickel-pasted plate, the positive side of nickel zinc cells. | Paste even, cure full, rev 2. Operator signed in the wrong box. |
| pwr-030 | Lead grid pasted with lead oxide, stacked into lead acid batteries. | TOXIC DUST. GLOVES AND MASK. WASH BEFORE MEALS. |
| pwr-031 | Salt and oxide paste that fills zinc carbon cells. | Not food. This has been tested by somebody already. |
| pwr-032 | Thin plastic film that keeps a cell's plates from touching. | Thinnest wall aboard, and it holds. Mostly. |
| pwr-033 | Drawn metal can in which every rechargeable cell is built. | Dented casings are rejected at inspection. Proc 140 applies. |
| pwr-034 | Plastic shell with terminals for battery packs, lead acid batteries and capacitor banks. | DO NOT PRY OPEN. NO SERVICEABLE PARTS INSIDE. |
| pwr-035 | Pressed enriched uranium, loaded into slug cladding. | Every pellet is numbered. Every number is accounted for. Ref 0091/U. |
| pwr-036 | Yellowcake enriched in the reactor, pressed into fuel pellets. | FISSILE MATERIAL. TWO-PERSON RULE WAIVED FOR SINGLE-OPERATOR STATIONS. |
| pwr-037 | Dense leftover of enrichment, used as shielding in fuel casks. | Retained for shielding. Disposal is not budgeted. |
| pwr-038 | Steel tube that seals fuel pellets into a slug. | Weld seam inspected, passed, rev 9. Seam looked fine from here. |
| pwr-039 | Empty shielded cask for spent fuel and spent control rods. | Rated for longer than the contract of whoever fills it. |
| pwr-040 | Cask of spent fuel or rods, left to cool and finally jettisoned through the hatch. | JETTISON VIA HATCH ONLY. DO NOT OPEN. DO NOT STORE IN SLEEPING AREA. |
| pwr-041 | Worn reactor control rod, sealed into a cask. | End of service life. Cask within one shift. Form 12R. |
| pwr-042 | Single solar cell, printed or refurbished, soldered into strings. | Cracked cells are binned, not soldered. The bin is checked. |
| pwr-043 | Soldered photovoltaic cells, framed into panels or glazed into tiles and strip cells. | Solder joints checked, 4 of 4, rev 6. Tester out of calibration. |
| pwr-044 | Worn-out solar tile or strip cell, refurbished or salvaged for cells. | Output below spec. Refurbish or salvage. Do not leave fitted. |
| pwr-045 | Board that prevents batteries from overcharging, built into solar arrays and reserve banks. | Firmware revision locked by the Company. Do not reflash. |
| pwr-046 | Grid equipment fitted at the service hatch to reinforce the ship's grid. | HIGH VOLTAGE. ISOLATE BEFORE OPENING. CAPACITORS HOLD CHARGE. |
| pwr-047 | Thin coated copper wire for coils, transformers, relays and generators. | Kilometres in every motor, and every metre is on the stock sheet. |
| pwr-048 | Braided cable that excludes electrical noise, built into load balancers. | Ground the braid at one end only. Proc 77, para 3. |
| pwr-049 | Heavy armoured cable laid into the grid; worn out, it returns as scrap cable. | MAIN TRUNK. STEP OVER, NOT ON. |
| pwr-050 | Old cable returned from the grid, stripped for copper and plastic. | Still has copper in it. Always has copper in it. |
| pwr-051 | Brass seal where a cable passes through a box wall. | Torque to spec. Hand tight is not a spec. Notice 214. |
| pwr-052 | Plastic sleeve shrunk over a splice or harness joint. | Use the heat gun, not the lighter. The lighter is logged. |
| pwr-053 | Brass and plastic block in which wires are clamped together. | One conductor per clamp. Two is a fire report. |
| pwr-054 | Thick copper strip that carries heavy current in buses, contactors and capacitor banks. | REMOVE RINGS AND WATCHES BEFORE WORK. |
| pwr-055 | Small steel clamp that holds cable to a frame. | Loose cable is a trip hazard. Trips are reported on Form 3T. |
| pwr-056 | Brass end crimped onto a wire, for leads, harnesses, fuses and splices. | Crimp, tug, log. Failed tug is a reject. |
| pwr-057 | Heat-resistant mica on glass cloth, wrapped into transformers and buses. | Does not burn. Does not care. |
| pwr-058 | Repaired joint in the ship's cabling, fitted into the grid at the service hatch. | Temporary repair. Temporary per the Company means until it fails. |
| pwr-059 | Braided copper strap that gives the grid a safe path to ground. | GROUND BEFORE TOUCHING. GROUND AFTER TOUCHING. |
| pwr-060 | Copper bars on a terminal block that feed the grid; the core of every distribution panel. | Bolts torqued, insulation checked, rev 5. Tag faded, rewritten in pen. |
| pwr-061 | Sintered brass and copper contacts for breakers and relays. | Pitted contacts are replaced as a set. Partial sets are not issued. |
| pwr-062 | Thin wire that melts on overload, for making and rewiring fuses. | Rated wire only. Substitution with paper clips is a dismissible offence. |
| pwr-063 | Heavy relay-driven switch, for transfer switches and load balancers. | One clunk means on. Two clunks means file a fault. |
| pwr-064 | Grid equipment that diverts voltage spikes, fitted at the service hatch. | Surge events are recorded. Downtime is not compensated. Ref 3390/G. |
| pwr-065 | Grid equipment that keeps circuits electrically separate, fitted at the service hatch. | ISOLATION BARRIER. DO NOT BRIDGE. |
| pwr-066 | Grid equipment that steps voltage down for cabin circuits, fitted at the service hatch. | Primary side is not for operator access. Secondary side is barely. |
| pwr-067 | Grid equipment that changes over supplies when one fails, fitted at the service hatch. | Changeover tested, 0.4 s, rev 8. Lights flickered. Within spec. |
| pwr-068 | Breaker panel fitted into the grid at the service hatch. | Circuit schedule to be posted inside the door. Missing schedules are reported on Form 71D. |
| pwr-069 | Grid equipment that spreads demand across circuits, fitted at the service hatch. | Load is allocated by the Company. Requests for more are not processed. |
| pwr-070 | Grid equipment that smooths the grid's waveform, fitted at the service hatch. | Hum changed pitch after fitting. Nobody knows if that is good. |
| pwr-071 | Grid equipment that cuts a circuit before an arc becomes a fire, fitted at the service hatch. | Fires prevented are not recorded. Fires not prevented are. |
| pwr-072 | Banked battery packs fitted into the grid as backup power. | RESERVE SUPPLY. NOT FOR ROUTINE LOAD. |
| pwr-073 | Heaviest grid equipment, capacitors and a regulator core under fibre optic control, fitted at the service hatch. | Loss of this unit is a ship-level event. Report immediately on Form 1A. |
| pwr-074 | Coil and control assembly at the heart of grid regulators and grid stabilizers. | Swap only with grid isolated. Isolation is confirmed in writing. |
| pwr-075 | Pressed iron oxide core for transformer and inductor coils. | Chipped cores are rejected. Glued cores are rejected and noted. |
| pwr-076 | Small wound coil for transformers, load balancers, phase correctors and shield coils. | Inductance checked, passed, rev 2. Meter borrowed from the next shift. |
| pwr-077 | Fast-charging energy store for phase correctors, grid stabilizers and shield capacitors. | STORED CHARGE. SHORT TERMINALS BEFORE HANDLING. |
| pwr-078 | Riveted steel box for grid regulators, transformers and distribution panels. | Rattles until fully bolted. Then rattles less. |
| pwr-079 | Large coil wound around a magnet, the core of a fission reactor kit. | Winding count certified by the line. Certificate not supplied. |
| pwr-080 | Cut nichrome resistor that lets a regulator measure current. | Do not trim to fit. Value is set at the bench. Proc 205. |
| pwr-081 | Stainless and graphite plate stacked in fuel cells and coated into catalyst plates. | Orientation marked on edge. Stacked backwards it still fits, which is the problem. |
| pwr-082 | Ceramic and copper module that turns a heat difference into power, built into fuel cell stacks. | HOT SIDE. COLD SIDE. DO NOT REVERSE. |
| pwr-083 | Rare earth rod that controls the reactor; a spare part that wears into a spent rod. | Rod insertion is not optional. Withdrawal beyond schedule is reported. |
| pwr-084 | Graphite block that slows the reactor's neutrons; a spare part. | Replace at scheduled interval. Interval set by procurement, not physics. |
| pwr-085 | Gasket that keeps the reactor's coolant contained; a spare part. | Small seal. Large liability. Inspect at every shift change. |
| pwr-086 | Glazed solar cell string fitted to the solar array; it wears into a degraded tile. | Clean glazing with approved cloth only. Sleeve wiping is noted. |
| pwr-087 | Glazed solar cell for a cabin's window solar strip; it wears into a degraded tile. | Window strip output is credited to the Company, not the station. |
| pwr-088 | Thin plastic membrane at the heart of the fuel cell stack; a spare part. | Handle by the edges. Fingerprints shorten service life. Notice 47. |
| pwr-089 | Nickel-coated bipolar plate for the fuel cell stack; a spare part. | Catalyst is not consumed. The plate is. Replace on schedule. |
| pwr-090 | Sintered contacts for the charging bay; a spare part. | Burnished, refitted, rev 4. Arc marks noted, not explained. |
| pwr-091 | Tool steel die for the cell line; a spare part. | Presses can after can and remembers none of them. |
| pwr-092 | Gem-edged die for the cable and coil line; a spare part. | Die wear is measured, not guessed. Gauge in drawer 3. |
| pwr-093 | Copper tip for the switchgear bench's iron; a spare part. | Tin before use. Untinned tips are consumed early and charged as misuse. |
| pwr-094 | Kit of parts that installs a fission reactor. | Installation manual enclosed, 400 pages. Page 212 missing. |
| pwr-095 | Kit of parts that installs a solar array. | CONTENTS FRAGILE. GLASS. THIS SIDE TOWARD SUN. |
| pwr-096 | Kit of parts that installs a fuel cell stack. | Stack order per diagram 6. Diagram 6 is on the lid, upside down. |
| pwr-097 | Kit of parts that installs a charging bay. | Crate is reusable and must be returned. Ref 5502/K. |
| pwr-098 | Kit of parts that installs a cell line. | A factory in a box. The box is also inventoried. |
| pwr-099 | Kit of parts that installs a cable and coil line. | Unspool slowly. Spring-loaded drum. Injuries on Form 9I. |
| pwr-100 | Kit of parts that installs a switchgear bench. | Packed hot from the line. Mind the iron, even in the crate. |
