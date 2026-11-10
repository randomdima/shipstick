# Decision log — the client

Why the page is shaped as it is. Only decisions still binding are here.

## 2026-11-05 — the client is plain JS and CSS, served as written

The owner, in as many words: "ok p1 - client is using pure JS + css. ( we can use all the latest major browser features )
/ no js build pipeline, no tooling / as thin as fast as possible", and then "no tooling - meaning no css or js bundlers,
not no tooling at all". So WEB-9, at `P1`.

The client is `wwwroot/`: `index.html`, `style.css` and ES modules, each the file the browser runs. It has no project;
the host's build copies the folder beside the host as it is (HST-3). `index.html` preloads every module and the codex,
so they are asked for at once rather than as each import is read. What the browser downloads is the page's own files,
the codex, compressed, and the art; no .NET runtime goes to the browser.

## 2026-11-05 — the page is generated art placed by CSS; only screens are drawn

GAM-8 to GAM-11 ([../../../../docs/style.md](../../../../docs/style.md)). The stylesheet draws no asset: the housings,
the header's dark steel over its hazard strip, the label plates of titles and tags, the keys and the screens' bezels
are the console kit (`assets/app/web/kit/`), the lamps, sockets and the codex and close keys the generated props.
Screens — the header's readout, the codex's page, a device's cycle and state, the inputs — keep the CRT the stylesheet
draws: black glass, phosphor, scanlines, framed by the kit's bezel.

The kit is models' renders (GAM-13), never stretched (GAM-14, the project log's 2026-11-10): a tile repeats whole, a
sliced piece keeps its ends whole and repeats its middle, every side at one scale, so a plate or a key is as long as
its label and a housing as large as what it holds. Each is modelled for it: whatever must not repeat — a bolt, a
corner, a shadow — lies inside its slices, and each repeated stretch is whole periods of its textures (the shapegen
skill's "The page's art"). `qq fit`, in `qq checks`, holds the stylesheet to it.

The capsule is no longer a screen. The owner: "lets try to make pattern less repeatable. So it does not look like
individual block. Same for floor". So its floor is laid in steel plates of several sizes, one to six cells, chosen by
the cells' place so the floor is the same every draw (`art.js` `deckOf`); each cell is the tile that draws its plate's
edges where the plate ends and plain steel where it runs on, turned to fit, and each plate is tinted a little apart
from its neighbours. The wall caps and panels run on the same way, a plate seam one cell in a few. The walls and doors
are devices on the edge cells (SHP-7). The owner, on the first walls: "All walls should be of the same heigh. We can
chose lower heigh, so its overlaping less. And side doors more visually distinct from a wall."; "Also more props on
their 'roof'"; "remore that other shown perimeter that is outside the grid"; and "If there are props that expected to
connect to neibhor props - we should respect those. So random pipes dont end nowhere". Then, on things laid on the
tops and a door drawn face on: "There are now random items on top." "Door is too flat. Its like a painting." "Lets try
to build walls from parts. Side panes amd the door. And a cap on top. That we can connect how we wany". So a wall cell
is built from a kit (`art.js` `structureLook`): a cap chosen by which neighbours are wall and turned to fit — post,
end, straight, corner, tee, cross — over a panel on each edge no wall continues past. Every wall is one height and any
layout joins. Once neighbours shared their walls (SHP-8, "walls should be shared and not duplicated"), the ship became
one floor: each capsule laid a cell short of the last one's end, a shared cell drawn once. Then: "Lets not use bolted
plates because they still add blockiness. And improve doors", and "Are doors not build as walls? From parts? Do it".
So no cap, panel or deck plate carries a bolt, and a door's cell is a wall like its neighbours with the door's parts
laid on it: a hazard-striped lintel across its cap, the watertight door within each face its passage runs through,
kept below the cap ("They also should fit there and dont overlap with roof cap"), open while its window is, and a
hazard sill on the floor just inside. Its tag of what it holds hangs below it, over everything. Nothing stands on a
cap. The floor has no housing round it: its walls are its edge. How it is all drawn — one 3D scene the player turns —
is the project log's (2026-11-09).

A device's window is one block, a housing with no title bar over it ("It all should be a single interface block. You
can drag it by any part that is not interactive in other ways"): a band, side and foot frames and a recessed face,
sliced round whatever the window holds. The owner chose a kit over a picture a device, so a housing is one of a few
paints (`kit/paints.json`, each device's read off the panel it wore before, so the paints the owner saw stay), and a
device with no paint of its own takes its storage's or its role's shared one. Its name is on a plate in the band, as
long as the name; its help and close keys sit in the key bay, a prop of its own drawn whole at the band's right ("Lets
try to align buttons properly on it"), so each key sits in its socket on every housing; its code and where it stands
are tagged on the foot. The housing draws no control (GAM-11): every slot, readout and choice on it is the page's,
there because the device has it. The codex and the slot editor are windows in housings too, their title and keys in
the band. What exists the page
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
camera is fitted to the floor's own size (`scene.js` `FIT`), on any screen, and aimed at the cell held at the view's
middle rather than scrolled: the corner capsule centres like any other, and the view stops at the ship's edge. A press that drags the floor opens nothing; one that does not is a click.

Round the ship is space; the owner: "now drop outer background and replace it with stars in space". So the page's
backdrop is generated patches of sky (`assets/app/web/space/`) lightened together, standing still while the floor
pans, and the black plating tile it replaced is gone. A fogged capsule is its deck, walls and shut doors, darkened,
and nothing standing on its floor; the owner, on its first floor of plating: "backgroun on rooms with fog is not
correct … show real floor". So WEB-7 says walls and floors. Its deck is laid from its door cells as any capsule's is,
so a player is sent nothing more for it.

## 2026-11-05 — the page draws the frame it was last sent, and acts by sending

The page holds no game type and runs no rule (HST-4). `host.js` keeps the last frame the host sent — a player's
`seat` or the admin's `ship`, with the ship's time and rate — and sends each move, way chosen or edit as an action
the host answers. The page draws the view from the frame on each frame and on a timer, telling the time on from the
frame's own; a slow-paced game (GAM-7) has no frame rate to defend, and a move shows once the host has run it.

## 2026-11-09 — a draw changes only what changed

The page rewrote the floor, its windows and their leaders whole on every tick, four times a second, frame or no frame.
The owner, in as many words: "All DOM changes must be adaptive/reactive on actual changes. NEVER recreate whole dom."
So WEB-10, at `P2`.

Each view still writes what it shows as HTML — one way to say it, read as it is drawn — and `dom.js` brings the live
page to it in place: `reconcile` keeps the elements laid over the floor and the windows by key (a device's lamp, a
door's tag or a window by its inventory) and passes over any whose HTML is unchanged without parsing it;
`patch` brings a window's, the editor's or the codex's contents to theirs, writing only the attributes, text and
children that differ. Between frames the floor is not even worked out — nothing it shows can have moved — and a
window's countdown is all a tick writes. A kept node is the one the pointer, a hover or a field's focus already holds,
so a field being typed in keeps what is typed. The leaders keep a line and a dot a window and move them. No framework:
WEB-9 asks for the thinnest page, and this is some hundred lines.

## 2026-11-09 — what moves, moves at the display's rate

The owner, in as many words: "Lets improve this, performance wise. Conside if we can do walls transorm as blocks
instead of indivisual transformed cells. If this affect performance. We want dragging and animations to use display
natural refresh rate". So WEB-11, at `P2`.

What follows the pointer — the floor, a window, the codex, a dragged item — records where the pointer is on each event
and is drawn once a display frame (`dom.js` `inFrame`), and a window or an item moves by its translate alone, laying
nothing out. A device's cycle bar is an animation in ship time played at the ship's rate, so the browser fills it every frame
off the page's thread, where it stepped with each quarter-second tick.

## 2026-11-10 — a device shows its state on its own model, in the scene

The owner, in as many words: "lets make some elements on devices more functional and add them animations. Line
indicators, gauges, lamps - so they actually do usefull work and not just sit there. Right now we have a few html
elements added not in 3D - we dont want that. Everything should be in-game - in the actuall 3D space". So WEB-12, at
`P2`.

The lamp laid over each running device and the tag under each door, both page elements, are gone. A model's part
can be live (the shapegen skill's "Live parts"): a lamp, a glowing screen, a needle, a filling bar, a turning drum,
each showing one of its device's signals — how it runs, its cycle, how full its inputs, outputs or slots are — which
the page works out from the frame it was sent and the ship's clock, so the host sends nothing more than a slot's
stack limit. A door's gauge is the level bar part laid on its cap. What turns is modelled to turn: a fan grille is a flat picture,
so a fan's blades and guard are a part laid over its round middle, the picture's frame and bolts left round it. Each part is driven in the shaders (`scene.js`) —
moved by a matrix, toned and made to glow — so the models stay one draw a texture, and while one moves the costly
passes are drawn over the box round what moved alone, the rest of the frame kept. Windows and their leaders stay on
the page: they are the operator's panels, not the ship.

## 2026-11-05 — what a fixture holds is behind a click, in a window of its own

The floor shows only what stands on it, and whether each device runs. A fixture's or a door's slots, and a
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
