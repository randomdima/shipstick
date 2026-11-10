# Requirements — the client

What each page shows, and to whom. Each rule carries a rung ([../../../../docs/priority.md](../../../../docs/priority.md)).
A page is a client: it shows what the host sends it and runs none of the game (HST-3, HST-4).

**WEB-7** `P0` A basic player sees only their own room; of the rest of the ship, its walls and floors alone, shaded
(fog of war).

**WEB-8** `P0` The admin sees more than a player, and has special actions.

**WEB-9** `P1` The client is pure JS and CSS, on every feature the latest major browsers have, with no JS or CSS
bundler or build step, and as thin and as fast as it can be.

**WEB-10** `P2` The page changes only what changed: a draw brings what it shows up to date in place, writing only what
differs, and never rebuilds the page or a whole part of it.

**WEB-11** `P2` What moves on the page — whatever follows the pointer, and every animation — moves at the display's
own refresh rate.

**WEB-12** `P2` What the floor shows of the ship is in the 3D scene, on the models: a device's lamps, gauges, indicators
and screens show how it runs and what it holds, working and moving as it does; nothing is laid over the floor as an
element of the page.

**WEB-1** `P5` What WEB-7 is: a player's page shows their own capsule — its floor, its fixtures, the doors in its walls
and what each holds — and the clock, in its place among every other capsule's walls, doors and deck, shaded. Of another
capsule nothing else: not what stands on its floor, not what its doors hold, and no name or code for the capsule beyond
a door (GAM-3).

**WEB-2** `P7` What WEB-8 is: the admin's page shows every capsule's floor and all it holds, each door naming the
capsule beyond; enters any one by a click, to move items as that capsule's player would; edits any slot (SHP-6), runs
or stops ship time, and plays the entered capsule's seat as its player sees it.

## The codex

**WEB-3** `P2` The codex holds a page for every item and every device the game holds, and pages on how the ship works.
It is built from what the game holds, so it is always up to date, and no item the game holds is missing from it.

**WEB-4** `P2` Every device's window has a help button that opens the codex at that device's page.

**WEB-5** `P2` An item's or a device's page shows a short description, flavour text in a smaller type, and every way
that makes, uses or needs the item, or that the device runs. Every item or device a codex page names is a link to its
own page.

**WEB-6** `P2` The codex keeps the pages a player has read, so they step back and forth through them, and it is a
window dragged like any other.
