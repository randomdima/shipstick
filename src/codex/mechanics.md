# The codex — how the ship works

The codex's own pages, beside one for every item and device of the catalogue. Each `## slug: Title` is a page.
`[[kind:id]]` or `[[kind:id|words]]` links to another page — `item:`, `device:`, `page:`, `section:`, `sub:`, `role:`,
`stat:` — and `{name}` is a figure the game runs on, filled in from its configuration so the page never goes stale.
`CodexBook` reads this file; a test fails on a link or a figure that names nothing. Its words keep
[../../docs/style.md](../../docs/style.md): the Company's operating manual, issued to its operators.

## start: Codex, operations manual

Consolidated Orbital Freight operations manual, issued to capsule personnel. Every item, device and procedure aboard
has a record here. A linked name opens its record; **back** and **forward** step through the records read, and the
query finds any record by name or stock code.

The **?** on a device panel opens that device's record: what it is, every procedure it runs, and what each procedure
needs, takes and makes. From there, every item leads to each procedure that produces, consumes or uses it as a tool.

Begin with [[page:capsule|the capsule]], then [[page:devices|devices and procedures]] and [[page:doors|doors]].
Familiarity with this manual is a condition of the operating contract.

## capsule: The capsule

The operator is assigned one capsule of a modular carrier: a square floor {cellsAcross} cells on a side, the fixtures
bolted to it, and a door in each wall that joins another capsule. The operator's own fixtures and doors are within
reach; nothing else is.

Every capsule carries the same standard-issue fixtures — [[device:any.lifesupport|life support]], a
[[device:any.bench|workbench]], a [[device:any.cot|cot]], a [[device:any.toilet|toilet]], a
[[device:any.chest|chest]] and the rest — and up to {roleDevicesMost} devices of its assigned [[page:roles|role]], which
no adjacent capsule shares.

Click a fixture to open its panel. Drag items between open panels. **Esc** closes the top panel.

## devices: Devices and procedures

A device runs one **procedure** at a time — a recipe: items it **needs** as tools and keeps, items it **takes** and
spends, items it **makes**. The operator selects the procedure on the device's panel. Every procedure a device can run
is listed on its record.

The procedure lays out the device's slots: a row for each tool, each input and each output, each slot accepting only
its item. An input has at least {slotsPerInput} slots and an output at least {outputSlots}; slots the procedure does not
use are closed, and residue a previous procedure left in them may be removed by hand.

A procedure takes its rated minutes aboard at {cycleSPerWayMinute} ship seconds a minute. When a cycle comes, a device
with every tool and input present, and room for every output, takes the inputs and makes the outputs. Otherwise it
takes nothing and its lamp shows red: **input short** when something was missing, **output full** when an output had
no room. Selecting another procedure restarts the cycle.

Some procedures are run **by hand**, anywhere, by the operator; no device runs those.

## slots: Slots and stacks

A slot holds one kind of item, at most {stackMost} units. A stack dragged onto an empty slot or the same kind moves as
much as fits; onto another kind, the two swap. A slot may refuse a transfer: a device input accepts only its item, and
an output accepts nothing — it is filled by the device and emptied by hand.

## doors: Doors

A door is a square of {doorSlots} slots in the wall between two capsules, reachable from both sides. Items left in it
may be taken by the adjacent operator, and the reverse. Voice traffic between capsules is not provisioned under the
operating contract: the door is the only sanctioned transfer, and the adjacent operator is known only by what passes
through it.

## storage: Chests and lockers

A fixture that runs no procedure is storage only: {chestSlots} slots that accept anything, as the
[[device:any.chest|chest]] and the [[device:any.locker|locker]].

## life-support: Life support

[[device:any.lifesupport|Life support]] keeps the cabin habitable. While it is starved the capsule is **failing**, and
the carrier is operational only while no capsule is. Keep it supplied. Failure is logged against the station.

## roles: Roles

A role is the trade a capsule's floor was fitted for: farm, water works, foundry, bridge and the rest. One role's
devices make what others need, so goods pass from role to role through doors, and no capsule supplies itself alone.
Each role's record lists its devices. Role assignment is not open to review.

## items: Items

Every item is one of a few classes:

- a **resource**, which procedures take and make;
- a **consumable**, used once for its effect, sometimes leaving residue — a meal leaves a dirty dish;
- a **durable**, which gives a small effect every hour while it is in place — worn, on the cot, fitted in the cabin;
- a **tool**, which a procedure needs and keeps, wearing out with use;
- a **spare part**, which fits a device, and a **kit**, which installs one.

Many items **decay**: food spoils, medicine expires, a tool wears into something worse. An item's record states its
shelf life and what it becomes.

At this revision items move through slots and devices only; eating, drinking, wear, decay and the operator's needs are
documented here ahead of the systems that will enforce them.

## stats: Needs and stats

The operator's needs, the cabin's air and the carrier's systems are each a metric that drifts on its own and is
restored by using items and running procedures. Each metric's record lists what moves it. Metrics are monitored.

## recycling: Recycling and the outside

Recycling is how the carrier runs: what is used returns to be used again — water reclaimed, waste composted, scrap
smelted. No loop returns all it takes, so the carrier also depends on what is harvested or salvaged outside, and on a
finite stock it departed with, which nothing aboard can make and only recycling stretches, as the
[[item:bio-001|gene vault]]. Losses are recorded.
