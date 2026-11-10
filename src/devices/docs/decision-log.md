# Decision log — devices

Why devices work as they do. Only decisions still binding are here.

## 2026-11-05 — a device is a catalogue device running one of its ways

With every catalogue item in the game (ECO-13), the demo's five devices and their recipe `switch` went: a device is
one of the catalogue's, and runs whichever of its ways the player chooses (DEV-5). One way at a time keeps a device's
window one machine to read — tools, inputs, outputs — and makes the choice a player's decision rather than a device
guessing which of its inputs to spend. The inventory is as long as the device's largest layout, so a choice only
refilters it: nothing is moved or destroyed by choosing, and what the old way left is the player's to take out. A
choice restarts the wait and drops the cycle due under the old way, by a generation count the clock checks, so the
same choices at the same times give the same ship (SHP-3). A fixture with no ways only holds things, as a chest does.
