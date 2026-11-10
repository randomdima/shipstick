# Requirements — the ship

The capsules, the doors between them, and the clock that runs them. Each rule carries a rung
([../../../docs/priority.md](../../../docs/priority.md)).

**SHP-1** `P3` A player seated in a capsule reaches that capsule's fixtures and the doors in its walls, and nothing
else (GAM-2, GAM-3).

**SHP-2** `P3` A door's slots are one inventory, reached from both capsules it joins (GAM-3).

**SHP-3** `P4` The ship's state changes only by events (GAM-7): a player's move or choice of a device's way (DEV-5), an
admin's edit (SHP-6), or a device's cycle at its due time.
Cycles run in due order, ties in the order they were scheduled, each once, so the same moves at the same times give the
same ship however time is advanced.

**SHP-4** `P9` On the starter ship every capsule stands the universal fixtures and devices of one role, and no two
neighbouring capsules share a role.

**SHP-5** `P7` A fixture covers a rectangle of floor cells, its size the catalogue's for its device; the rectangle lies
wholly on the capsule's floor and shares no cell with another fixture.

**SHP-8** `P2` Neighbouring capsules share the wall between them: one wall, not two standing back to back.

**SHP-7** `P5` What SHP-8 is: a capsule is walled round on its floor's edge cells, and two neighbours' facing edges are
the same cells of the ship. Every edge cell holds a wall section, but for the middle cell of each edge with a
neighbour, which holds the door to it (GAM-10). A shared cell is one wall section, or the one door of SHP-2, standing on
both floors; nothing furnished stands on an edge cell.

**SHP-6** `P8` An admin may set any slot aboard to any count up to a stack of an item the slot may hold, from no seat:
a device's slot holds the one item its layout gives it (DEV-4), any other slot what its filter accepts (ITM-4).
