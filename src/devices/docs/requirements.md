# Requirements — devices

The devices on a capsule's floor and their cycles. Each rule carries a rung
([../../../docs/priority.md](../../../docs/priority.md)).

**DEV-1** `P6` A device runs one of its catalogue ways at a time and cycles once per that way's time. With every tool
and input of the way on hand and room for every output, it takes the inputs and makes the outputs, keeping the tools;
otherwise it takes nothing and says why — starved or full.

**DEV-2** `P2` Recycling is how the ship runs: devices feed each other in loops, and what is used comes back to be used
again. No loop gives back all it takes, so the ship also lives on what comes in from outside — material harvested or
salvaged — and on a finite stock it set out with, which nothing can make and only recycling stretches.

**DEV-3** `P6` Every capsule has a life support. A capsule whose life support starved on its last cycle is failing, and
the ship is kept going while none is.

**DEV-4** `P6` The way a device runs lays out its slots: a run for each tool, then each input, then each output, each
taking only its item — a configured fewest for an input and an output, and enough stacks for one cycle's count — then
closed slots that take nothing. A cycle counts an item across its own run and fills each output's run in order.

**DEV-5** `P6` A player chooses the way a device they reach runs, from every way the catalogue gives it. The choice
restarts its wait, a cycle due under the old way never runs, and what the old way left in its slots stays, to be taken
out by hand.
