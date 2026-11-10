# Decision log — the client

Why the page is shaped as it is. Only decisions still binding are here.

## 2026-11-05 — the client is plain JS and CSS, served as written

The owner, in as many words: "ok p1 - client is using pure JS + css. ( we can use all the latest major browser features )
/ no js build pipeline, no tooling / as thin as fast as possible", and then "no tooling - meaning no css or js bundlers,
not no tooling at all". So WEB-9, at `P1`.

The client is `wwwroot/`: `index.html`, `style.css` and ES modules, each the file the browser runs. It has no project;
the host's build copies the folder beside the host as it is (HST-3). `index.html` preloads every module and the codex,
so they are asked for at once rather than as each import is read. What the browser downloads is some 20 KB of page and
the codex, compressed; no .NET runtime goes to the browser.

## 2026-11-05 — the page is generated art placed by CSS; only screens are drawn

GAM-8 to GAM-11 ([../../../../docs/style.md](../../../../docs/style.md)). The stylesheet draws no asset: the housings
are the generated heavy panel frame nine-sliced as a border image, the header a gunmetal plate over a hazard strip,
titles and the footer's note label plates, buttons the plastic key sliced to take any label and swapped for its
pressed image, lamps, sockets and the codex and close keys the generated props. Screens — the header's readout, the
admin's map, the codex's page, a device's cycle and state, the inputs — keep the CRT the stylesheet draws: black
glass, phosphor, scanlines, framed by the generated bezel.

The capsule is no longer a screen. The owner: "lets try to make pattern less repeatable. So it does not look like
individual block. Same for floor". So its floor is laid in steel plates of several sizes, one to six cells, chosen by
the cells' place so the floor is the same every draw (`art.js` `deckOf`); each cell is the tile that draws its plate's
edges where the plate ends and plain steel where it runs on, turned to fit, and each plate is tinted a little apart
from its neighbours. The wall caps and panels run on the same way, a plate seam one cell in a few. Each device is its sprite standing on its
footprint and rising above it, a lower row drawn over a higher. The walls and doors are devices on the edge cells
(SHP-7). The owner, on the first walls: "All walls should be of the same heigh. We can chose lower heigh, so its
overlaping less. And side doors more visually distinct from a wall."; "Also more props on their 'roof'"; "remore that
other shown perimeter that is outside the grid"; and "If there are props that expected to connect to neibhor props -
we should respect those. So random pipes dont end nowhere". Then, on things laid on the tops and a door drawn face on: "There are now random items on top." "Door is too flat. Its
like a painting." "Lets try to build walls from parts. Side panes amd the door. And a cap on top. That we can connect
how we wany". So a wall cell is built from a kit (`art.js` `structureLook`): a cap chosen by which neighbours are wall
and turned to fit — post, end, straight, corner, tee, cross — raised by a low front panel on each edge no wall
continues past. Walls alone have a camera of their own ("we can keep this for walls only"); first a little west, then
("Lets try making wallg tilt outside the room") one over the middle of the room, so the stylesheet draws each wall cell
as a 3D block under a perspective, every wall leans out, and a face turned from the camera is not drawn. Every wall
is one height and any layout joins. Once neighbours shared their walls (SHP-8, "walls should be shared and not
duplicated"), the ship became one floor: each capsule laid a cell short of the last one's end, a shared cell drawn
once, and one camera for every wall, standing over the middle of the view and following it as the floor pans — a
camera a room could not give a wall that two rooms share. Each wall is a 3D block of its own — a straight run of them
one block (2026-11-09) — so the page orders them: the
owner, on faces showing through caps at a junction, "lets make sure we render wall in correct order, so that
overlapping happens properly". Every wall is one height and leans away from the camera, so of two that overlap the
nearer stands between the camera and the further; walls are drawn nearer over further, ordered again as the camera
moves. What stands on the floor is drawn over the walls behind it, its sprites rising over them, but not over a wall
the camera is beyond: that one leans in over the capsule's floor, and the owner saw "deviced bein rendered on top of the
walls" there. So a capsule's devices are drawn in one band of the walls' order (2026-11-09), under its walls on each
side the camera is beyond and over the rest, the devices' own lower-row-over-higher kept inside the band. Then: "Lets not use bolted plates
because they still add blockiness. And improve doors", and "Are doors not build as walls? From parts? Do it". So no
cap, panel or deck plate carries a bolt, and a door's cell is a wall like its neighbours with the door's parts laid on
it: a hazard-striped lintel across its cap, the watertight door within the face its passage runs through, leaning
with it and kept below the cap ("Doors are flat dont fit the wall tilt", "They also should fit there and dont overlap
with roof cap") — on each face its passage runs through, so the room sees it on its inner face — open while its window is, and a hazard sill on the floor just inside. Its
tag of what it holds hangs below it, over everything. Nothing stands on a cap. The floor has no housing round it: its
walls are its edge.

A device's window is one block, the device's own interface panel with no title bar over it ("It all should be a
single interface block. You can drag it by any part that is not interactive in other ways"), nine-sliced so its frame
and nameplate band keep their shape while the empty face stretches to hold the controls. Its name is stamped on the
panel's blank nameplate; its help and close keys sit in a bay of two sockets drawn into the band's right ("Lets try
to align buttons properly on it. Potentially give image gen a template"), so every panel is generated to one layout
guide, and its code and where it stands are tagged on the foot. The band stretches with the window, so the page lays
the panel's own top-right corner back over it at the band's scale, and seats the keys on each panel's measured bay
(`qq panels`): the model draws the bay a few pixels apart from panel to panel. The panel draws no control (GAM-11): every slot, readout and choice on it is the page's,
there because the device has it. A device with no panel of its own takes its storage's or its role's shared one. What exists the page
learns from the host's `assets.json`, so it asks for no image that is not there; a device with a model is drawn from it
in the floor's scene (`scene.js`, the project log's "the floor is one 3D scene the player turns"), and one without
stands as the plain crate.

No system ships a wide face, so the labels' face is Michroma (SIL Open Font License), downloaded once with the owner's
leave from google/fonts at a pinned commit, kept under `assets/app/web/fonts/` and served by the host beside the client
(HST-3); its `.src.json` names the address, commit and hash. Readouts stay in the system's monospace. An item's chip
is still a tag in one of twelve industrial colours, none of them red, until items have art of their own. Every id is
printed upper case as a stock code beside its name. A player's page names no capsule — its own is "assigned", the one
beyond a door "adjacent" — so no code in it says where on the ship it is (WEB-1); only the fogged walls round it do.

## 2026-11-05 — one page, two views: the player's and the admin's, chosen by the address

`?seat=column,row` (the first seat when none is named) is a player's page, `?admin` the admin's (WEB-7, WEB-8). They
share one floor and its windows (`cabin.js`) and differ in what they are sent and what a click on a slot does. **What
a player is not told is not sent**: the host sends a player's line a `SeatView` — their own cabin, and of every other
capsule only the cells its walls and doors stand on, and no door naming the capsule beyond — so a page cannot show
what it was never given. The admin's edit is an action the host runs (`Vessel.Set`, SHP-6), checked like any other.
The admin plays a seat by drawing the cabins it is sent as that seat's player is shown them.

Both draw the whole ship, every capsule at its place in the grid; the owner: "lets continue walls for other sections
of the ship / player have fog of war and can only see walls shaded. / admin can see all rooms". Asked how much, the
owner chose the whole ship for a player — so a player learns where their capsule stands, and WEB-1 says so — and WEB-7
reworded as "A basic player sees only their own room; of the rest of the ship, its walls alone, shaded (fog of war)"
("Yes, that wording"); for the admin, every room drawn at full size, which took the place of the ship's map ("Whole
ship drawn, scrolls"). The admin enters a capsule by clicking in it, since a move is still made from the capsule
entered.

The floor is sized so the view's capsule fits it, centred, and is panned by dragging it; the owner: "his room should
fit the screen by default. We dont need scrollbars - we should be able to drag the map with mouse or touch". So the
cell is worked out by the stylesheet against the floor's own size (container units), on any screen, and the ship is
placed by the cell held at the view's middle rather than scrolled: the corner capsule centres like any other, and the
view stops at the ship's edge. A press that drags the floor opens nothing; one that does not is a click.

Round the ship is space; the owner: "now drop outer background and replace it with stars in space". So the page's
backdrop is generated patches of sky (`assets/app/web/space/`) lightened together, standing still while the floor
pans, and the black plating tile it replaced is gone. A fogged capsule is its deck, walls and shut doors, darkened,
and nothing standing on its floor; the owner, on its first floor of plating: "backgroun on rooms with fog is not
correct … show real floor". So WEB-7 says walls and floors. Its deck is laid from its door cells as any capsule's is,
so a player is sent nothing more for it.

## 2026-11-05 — the page draws the frame it was last sent, and acts by sending

The page holds no game type and runs no rule (HST-4). `host.js` keeps the last frame the host sent — a player's
`cabin` or the admin's `ship`, with the ship's time and rate — and sends each move, way chosen or edit as an action
the host answers. The page draws the view from the frame on each frame and on a timer, telling the time on from the
frame's own; a slow-paced game (GAM-7) has no frame rate to defend, and a move shows once the host has run it.

## 2026-11-09 — a draw changes only what changed

The page rewrote the floor, its windows and their leaders whole on every tick, four times a second, frame or no frame.
The owner, in as many words: "All DOM changes must be adaptive/reactive on actual changes. NEVER recreate whole dom."
So WEB-10, at `P2`.

Each view still writes what it shows as HTML — one way to say it, read as it is drawn — and `dom.js` brings the live
page to it in place: `reconcile` keeps the floor's elements by key (a deck cell or a wall by its cell on the ship, a
fixture, a door's tag or a window by its inventory) and passes over any whose HTML is unchanged without parsing it;
`patch` brings a window's, the editor's or the codex's contents to theirs, writing only the attributes, text and
children that differ. Between frames the floor is not even worked out — nothing it shows can have moved — and a
window's countdown is all a tick writes. A kept node is the one the pointer, a hover or a field's focus already holds,
so a field being typed in keeps what is typed. The leaders keep a line and a dot a window and move them. No framework:
WEB-9 asks for the thinnest page, and this is some hundred lines.

## 2026-11-09 — what moves, moves at the display's rate; a straight run of wall is one block

The owner, in as many words: "Lets improve this, performance wise. Conside if we can do walls transorm as blocks
instead of indivisual transformed cells. If this affect performance. We want dragging and animations to use display
natural refresh rate". So WEB-11, at `P2`.

Measured with `qq web --frames` on the admin's page, a two-second pan: the page's thread spent 3.3 s of it working,
1.9 s of that restyling. The view's cell was an inherited custom property set on the ship, so every pan move restyled
all of its two thousand elements; it is registered not to inherit, and the walls' camera is aimed by the stylesheet
from the same two properties, so nothing reads the page's geometry back mid-pan. That brought the pan to 1.3 s; with
the walls hidden it was 0.4 s, and of the rest the walls' planes were most and their reordering about a third.

So a straight run of wall — two or more plain wall cells in a line, no door, corner, tee or end among them — is one
block: its cap and its two long faces are each one plane carrying each cell's piece of the kit as a background of its
own, so a capsule's edge is a few blocks rather than ten cells of three planes each, and the camera turns and orders a
third as many. Doors and junctions stay a cell each. The picture is the same to the pixel but for the hairline seams
between cells, now gone. A run is still a cell at a time to the pointer — what each opens, and what its leader points
at — but it lights as one when hovered or open. Walls are drawn at their rank by nearness, so only a wall that passes
another is written. The pan now costs the page's thread 0.6 s of the two.

What follows the pointer — the floor, a window, a dragged item — records where the pointer is on each event and is
drawn once a display frame (`dom.js` `inFrame`), and a window or an item moves by its translate alone, laying nothing
out. A device's cycle bar is an animation in ship time played at the ship's rate, so the browser fills it every frame
off the page's thread, where it stepped with each quarter-second tick.

## 2026-11-05 — what a fixture holds is behind a click, in a window of its own

The floor shows only what stands on it, and whether each device runs (a lamp). A fixture's or a door's slots, and a
device's recipe, state and next cycle, are in a window opened by clicking it — as a person walks up to a machine and
opens its panel — so the floor stays readable and what a player knows is what they chose to look at. Several windows
may be open, since a move is between two of them; each opens beside its fixture where it covers no other window, moves
by a press on any part of it that is not a control, and is tied to its fixture by a line, so a window dragged away still says what it shows. Windows are
the page's alone: opening, moving and closing one asks nothing of the host.

## 2026-11-05 — the codex is a window of the page, drawn from the game's own data

The owner, in as many words: "on each device menu there is a help icon opening codex on the page related to that
device"; "there should be a record per each game item, device mechanics"; "if an item is referenced in some codex pages
- it should be a link to open its codex page"; "item/device page should contain its short description, some lower font
flavour text and all linked recipes"; "codex should keep track of page navigation so users can go back and forth";
"it should be draggable as any other window"; and "codex must be always up to date. There cannot be items that are not
in the codex". So WEB-3 to WEB-6, at `P2`.

The owner offered an iframe and preferred something in sync with the game, so the codex is a window of the page itself
(`codex.js`), not a frame: a device window's `?` and any `data-go` link anywhere open it, and it can come to show what
the floor holds. Its words and data are one JSON the host makes once (`codex.json`, a `CodexBook`), built from the
catalogue the game was compiled with and from `GameConfig`, so a page cannot say other than the ship does. It keeps its
own history (back, forward, Alt+arrows); the floor's windows are brought up to date every tick and the codex only on a navigation,
so a page read is not scrolled away under the reader.
