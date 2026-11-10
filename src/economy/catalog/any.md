# The universal fixtures — `any`

Every capsule has these, whatever its role ([../docs/design.md](../docs/design.md#roles-which-capsule-makes-what)).
Some are the survival floor: slow, poor ways to the goods a capsule cut off from every neighbour lives on, for a while
(ECO-5). The rest are where the crew member sleeps, eats, washes and relieves, and where items are used. A universal
fixture has no role, so a way it runs takes the roles of its inputs alone. The fixtures make no items of their own:
what they make is the subsections'.

## Devices

| id | device | role | cells | does |
|---|---|---|---|---|
| any.bench | HX10 Workbench | any | 2x1 | hand assembly: small, slow ways any capsule can run |
| any.solarstrip | HX40 Solar Strip | any | 1x1 | a trickle of power from the window |
| any.condenser | HX200 Moisture Condenser | any | 1x1 | wrings water out of the cabin air |
| any.algaejar | HX12 Algae Jar | any | 1x1 | a jar of algae on the windowsill: a little oxygen, a little less carbon dioxide |
| any.sprouter | HX15 Sprout Tray | any | 1x1 | sprouts from the capsule's emergency seed tin |
| any.table | HX30 Mess Table | any | 2x1 | eats, drinks and takes medicine: the crew's stats |
| any.cot | HX6 Cot | any | 2x1 | sleep; holds bedding, whose rates hold while it lies there |
| any.toilet | HX9 Toilet | any | 1x1 | urinate and defecate; its tank holds what is left until it is passed on |
| any.washbasin | HX8 Washbasin | any | 1x1 | washing, and the hygiene items used there |
| any.lifesupport | HX500 Life Support | any | 2x2 | the cabin's stats: air, heat, light, clean |
| any.locker | HX3 Locker | any | 1x1 | holds what is worn, whose rates hold while it is there |
| any.chest | HX4 Chest | any | 2x1 | holds anything |
| any.hatch | HX70 Service Hatch | any | 1x1 | the ship's stats: what goes into the hull, drive, shields and computers |
| any.wall | HX1 Bulkhead Section | any | 1x1 | one cell of the capsule's wall; holds nothing |
| any.door | HX2 Bulkhead Door | any | 1x1 | the door to a neighbour, in the wall: its slots are the only way between capsules |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| catch sunlight | any.solarstrip | 60 | — | 1 pwr-001 | — |
| condense water | any.condenser | 120 | — | 1 wat-002 | — |
| boil water | any.bench | 20 | 2 wat-002, 1 pwr-001 | 2 wat-001 | — |
| grow algae | any.algaejar | 180 | — | — | cabin.o2 +3, cabin.co2 -3 |
| sprout seeds | any.sprouter | 240 | 1 wat-001 | 1 veg-001 | — |
| sleep | any.cot | 480 | — | — | rest +40 |
| nap | any.cot | 90 | — | — | rest +8 |
| urinate | any.toilet | 2 | — | 1 toi-001 | bladder -100 |
| defecate | any.toilet | 8 | 1 toi-003 | 1 toi-002 | bowel -100 |
| defecate without paper | any.toilet | 8 | — | 1 toi-002 | bowel -100, hygiene -10 |
| wash | any.washbasin | 10 | 2 wat-001 | 2 san-001 | hygiene +15 |
| wash with soap | any.washbasin | 10 | 2 wat-001, 1 hyg-001 | 2 san-001 | hygiene +30 |
| run the heater | any.lifesupport | 30 | 1 pwr-001 | — | cabin.heat +4 |
| wipe the floor | crew | 15 | — | — | cabin.clean +3, hygiene -2 |

## Codex

| id | about | flavour |
|---|---|---|
| any.bench | A fixed workbench for slow hand work: boiling water, grinding by hand, and assembling parts and kits. | Surface burn, origin unreported. Logged as pre-existing. Inspected, rev 4. |
| any.solarstrip | A strip of cells along the window that trickles power into the capsule. | KEEP GLASS CLEAN. OUTPUT NOT GUARANTEED. COF PROPERTY. |
| any.condenser | Draws moisture from the cabin air as raw water, a little at a time. | Own breath, back in a cup. Boil it first. |
| any.algaejar | A jar of algae on the windowsill that adds a little oxygen and absorbs a little carbon dioxide. | Algae culture is Company stock. Loss of culture through neglect is deducted at cost. Ref 2208/A. |
| any.sprouter | A tray that turns the capsule's emergency seed tin and drinking water into sprouts. | Emergency provision only. Sprouts do not constitute a meal under Schedule 4. |
| any.table | The station where meals, drinks and medicine are taken. | Twelve tallies scratched into the edge, then nothing. Nobody counts past twelve. |
| any.cot | A narrow bunk for sleeping and napping; bedding laid on it keeps working while it lies there. | Cot length meets standard operator height per Spec 9C. Operators outside spec are not provisioned. |
| any.toilet | Receives urine and solid waste and holds them in its tank until they are passed on. | TANK CONTENTS REMAIN COF PROPERTY. DO NOT TAMPER. |
| any.washbasin | A small basin for washing, with or without soap, and for using hygiene items. | Grey water is returned at end of shift. Unreturned volume is logged on Form 19W. |
| any.lifesupport | The capsule's environmental unit, which keeps the cabin's air, heat, light and cleanliness in order. | AUDIBLE HUM IS NORMAL. SILENCE IS NOT. REPORT SILENCE. |
| any.locker | Holds worn clothing, which keeps working while it is stored there. | Lockers are not fitted with locks. Personal privacy is not a provisioned service. |
| any.chest | A plain storage chest that holds any item. | Audit: one chest, contents unverified, faint odour of cabbage. Audit closed. |
| any.hatch | The service hatch where parts and supplies are fed into the ship's hull, drive, shields and computers. | All hatch transfers are logged against the operator's account. Proc 301 applies. |
| any.wall | One cell of the capsule's bulkhead, bolted to the frame; it holds nothing and has no service point. | DO NOT DRILL, HANG OR FIX TO BULKHEAD. Operators continue to. |
| any.door | The bulkhead door to an adjacent capsule; its slot rack is the one sanctioned transfer between stations. | Door stays sealed. Rack is shared. Items left in the rack are deemed transferred. Proc 12 applies. |
