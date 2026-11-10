# Decision log — the cross-cutting decisions

Why the project as a whole is shaped this way. A decision belonging to one slice lives in that slice's own log; only
decisions still binding are here, and a superseded one is deleted rather than annotated.

## 2026-11-05 — the game looks and speaks as used-future company hardware

The owner, in as many words: "Design the UX in a “used future” cassette-futurist style. Interfaces should feel like
heavy 1970s-80s industrial hardware built by an indifferent corporation: monochrome green or amber phosphor text on
black CRT screens with scanlines and glow, wide uppercase sans-serif and monospace type, vector wireframe graphics, and
dense, bureaucratic readouts full of codes and serial numbers. Physical framing should be chunky and worn, using
off-white plastic, gunmetal and matte black surfaces with hazard yellow-black stripes, visible bolts, toggle switches
and simple pictogram warning icons, with red reserved strictly for alerts. Every element should read as utilitarian,
cold and functional rather than polished or friendly, so the player feels like an employee operating company equipment
rather than a consumer using a product." — and that agents respect it in "all designed assets, ux/ui, lore and flavour
text", names and captions included. So GAM-8, at `P2`, and [style.md](style.md) as how it is kept.

The owner chose, when asked, to rename every item and device and rewrite every codex line in one pass rather than as
each subsection is next touched. The how is the assistant's: a device is a model designation and its established noun
phrase, an item inventory nomenclature (noun first, qualifiers after), so an item that names a device names the
phrase and a model can change alone. Green phosphor is the screen and amber the caution, so red stays the alert alone.
The Company, Consolidated Orbital Freight, and its silence between capsules are lore the assistant wrote to give the
voice something to speak from; GAM-3 is its in-world reason.

## 2026-11-05 — everything drawn is generated: floor tiles, devices, interfaces, screens

The owner, in as many words: "Out of screen its as I said - dark yellow\yellow\orange to gray\black, with occasional
stripes. Like a heavy duty machinery. That applies for metal parts. And glass is reiforced blue-green tint. etc
Ceramic is well regular ceramic. Fabrics are bulky, 'warm' ( in style, not color ). In general colors are a bit dull
and muted."; "Each asset is displayed as 2d sprite asset with or without animations. Camera is tilted a bit, so it
looks pseudo 3d. Real camera cannot be tilted or controlled by player"; "Technically everything is a device, except
floor. Even doors and walls."; "When oppened each device shows a draggable window with device controls. The window
itself represents stylistic flat version of the device. With buttons, controls, dials, gauges, diginal screens....
Not everything is a digital screen - basic controls can be just mechanical buttons. Even prefered, to keep screens
for special sections or high tech devices. This means that we need a dedicated visual asset for each machine
interface. Potentially some common intefaces can be shared. And props like buttons - known reusable catalog.";
"we dont want to draw assets with pure code like css or svg. They should be generated and then can or not be
stylized with css"; "human fits one grid cell. With some space around. Heavy door is also one cell. [...] Largest
item can be 3x3"; and "All on-screen icons should match its vibes but can be colored". The screens as they are stay.
So GAM-9 to GAM-11, at `P2`, and [style.md](style.md)'s "What is drawn, and how" and "Art".

Then, on seeing the first art: "Dont do 'fake' gauges or controls on the interface. Each should be placed later and
only when its needed." and "current devices are tilted too much - fix it." So GAM-11 says an interface shows no
control that does nothing, the panels are plain housings with every control a prop the page places, and the camera is
written as about 15–20° from straight down; every device and interface sheet was drawn again.

Then: "note that capsule is a living quaters also. And its a space station/ ship. There will be no drilling or
excavating ground for example. So even tho it is a heavy machinery - not that heavy. And operated by a single
operator. So its a smaller, more automated, compact variants. Also that capsule is a living quortes, so it can be
dirty but not that dirty." So GAM-12, at `P2`; the lore's "a work station, not a home" became both, and the
devices, walls, deck and interface panels were drawn again as compact, kept equipment.

Then, on walls laid as trim round the floor: "There is a missed requirement wall is a device 1x1 same as door", and
then "Actually some props can be 1x2 1x3". So GAM-10 says each is a device on the floor's cells, 1×1 and some 1×2 or
1×3. The how is the assistant's (SHP-7): every capsule is walled on its edge cells, and the floor grew from 10 to 12
cells so the room inside stays 10 across. At first two neighbours stood two walls back to back; the owner: "walls
should be shared and not duplicated". So SHP-8, at `P2`: two neighbours' facing edges are the same cells of the ship,
each one wall section standing in both capsules, as a door already was one door in both.

The image settings — Sunburst at quality low, transparent, nine or more to a sheet, three attempts — were confirmed by
the owner ("Good.") when shown with the plan of sheets. A floor tile is asked to fill its cell edge to edge on the
transparent canvas, so its sheet keeps those settings.

## 2026-11-09 — the floor is one 3D scene the player turns

The owner, in as many words: "use full 3d in the game", with its own WebGL2 renderer, no third-party file (WEB-9
kept); then "lets go full 3d with rotation on client on hold ctrl + mouse" and "no more static images". Asked how free
the camera is, the owner chose "Turn and tilt": ctrl and a horizontal drag turn it round the middle of the view through
a full turn, a vertical drag tilts it from nearly straight down to about 30° over the floor, a plain drag still pans,
and it stays where it is left. Asked what stands for a device with no model, "Plain crate until modelled": a box of
its footprint built from kept textures, clickable and named as before, the rest modelled in later batches. Then "nice
let players zoom and rotate the map": the wheel, or a two-finger pinch, brings the camera nearer or further about the
point under it, and the right button turns it as ctrl does. So GAM-10 says the whole floor is drawn in 3D and the
camera is the player's to turn, tilt and zoom. Then "lets make wall higher": the height is the assistant's, three of
the kit's panels, 1.5 m — below the tallest device and a person, so the starting camera still sees over the wall
before it — with a panel's fitting only on the top one, and the door stretched to the wall's height.

The how is the assistant's. `qq sprites use` writes a model's triangles and textures beside its sprite
(`.qq/_shapes_mesh.py`); the crate is a kept part like any other (`any_crate`). The page draws one scene
(`scene.js`): the deck's plates, the wall kit's caps and panels on blocks a cell square, the door's leaf and lintel on
them, every device's model, lit by the renderer's own passes — sun, one shadow map for the whole floor, occlusion,
outlines — under a camera in perspective. What a click hits is read back from the picture; a device's lamp and a
door's tag are laid on the page where the camera puts them, as the windows and their leaders are.

## 2026-11-09 — every asset is a 3D model

The owner, in as many words: "p0 rule - all our assets are now 3D", and asked which assets, "Everything" — every image
under `assets/`, interface panels, props and space backgrounds included. So GAM-13, at `P0`. Asked which camera the
renders take, the owner kept the game's: GAM-10's device camera at 18°, so the drawn sprites' steeper angle is no
longer a goal. The first twenty devices in name order, the wall and door kit aside, are modelled and installed in the
game first; the rest is the gap [index.md](index.md#known-gaps) names.

## 2026-11-09 — an asset may be a model of simple shapes, textured with generated swatches

The owner, in as many words: "Lets introduce new asset generation tooling - generate 3D asset. This requres agent to
define 3D shape and texture it. Textures are to be generated with existing 2D image generations tooling ( with
potential extension ). 3D shapes should be simple enought for agent to define correctly. Shape = Box, shpere ...
other primitives -, collection of shapes. Consider using minimal shapes and better texturing instead of detailed
shapes." So `qq shapes` and the [shapegen](../.claude/skills/shapegen/SKILL.md) skill. GAM-9 holds as the owner set
it: a render's every pixel is a generated swatch's, placed and lit, and nothing in it is painted by code; a flat colour
is not a texture the model format offers. The swatch sheet keeps remotegen's shape — model, settings, nine to a sheet,
three attempts — and one sheet textures a model or a family. The how is the assistant's: orthographic rendering so a
view is exact, a grid cell one metre square as the deck tiles were briefed, the device camera at 18° (GAM-10's "about
15–20°"), and a kept render tracing through its model to each texture's prompt.

## 2026-11-10 — a generated image is never stretched

The owner, in as many words: "we should not stretch generated images - it looks bad. We can resize them, but without
stretching. This applies to all elements - labels, menus, buttons, etc. You can generate new images if needed. Or
repeat pattern ( generated images must allow this )". Asked, the owner set it at `P2`, extended it to a model's
textures ("Yes, models too"), and chose for the device interfaces a kit of parts over one picture a device. So GAM-14,
at `P2`. The how is the assistant's: a frame, plate or key is cut into end pieces drawn at their own proportions and a
middle made to repeat; a device's panel is assembled from its paint family's kit — corners, edge strips and face that
tile, a nameplate and a key bay placed whole — modelled with `qq shapes` like any asset (GAM-13).

## 2026-11-05 — the working tooling comes from traffic-dotnet, cut to what applies

The owner asked for this project to keep the tooling and helpers of traffic-dotnet usable and to stand on its own. What
came over is what is not about traffic: the rule register and its checks (`qq req`, `qq doclint`, the rung ladder),
code navigation (`qq outline`, `qq unused`), document moves (`qq relink-docs`, `qq relink-apply`), the tiered suite
(`qq tests`, `qq checks`, `Tier`, `Priority`, `TierTests`), the page photographed headless (`qq web`), a slow line for
multiplayer (`qq line`), and the art pipeline (the remotegen skill, `qq sprites`, the provenance rules). `qq sprites` is
a new minimal tool and not a copy: the original's cut is bound to cars, walkers and ground surfaces. `qq web` is cut to
build, run the game's host, photograph and the input gestures; its join, admin, profiling and caption were the town's.

## 2026-11-05 — the game, the host and the suite are projects; the client is none

The game is a project of its own (`src/shipstick.csproj`) compiling every slice but the shell's, so the suite references
it without a host. The host is a project in its slice (`src/app/host/`); the client is plain files the host copies
(WEB-9). Every project's `bin/` and `obj/` are redirected to the root, so a slice folder holds only what was written.

## 2026-11-05 — the game slices are items, devices, ship, in that order

The demo needs things on a floor that hold items and turn some into others. Items and slots know nothing of who holds
them, so they are the lowest game slice; devices hold inventories, so they sit above; the ship holds both, the doors
and the clock. A device's item kinds are a rule in `devices/`, its amounts and interval are figures on `GameConfig`, so
`core/` stays below every game slice.

## 2026-11-05 — the page is photographed off a Debug build by default

`qq web` builds the host in Debug, which is seconds; `--release` publishes it. A slow-paced, event-based game (GAM-7)
has no frame rate to judge in an edit loop, so the fast build is the default.

## 2026-11-05 — the owner's band is P0 to P2

The owner asked that requirements they stated explicitly be kept apart from those the assistant created or implied
along the way, so that an assumed rule is never high priority: `P0`, `P1` and `P2` are the owner's, `P3`–`P9` the
assistant's ([priority.md](priority.md)). `P2` was the assistant's game-wide rung; every assistant rule moved down one
rung (`P2` became `P3`, and so on), with the instrument and detail rungs merged at `P9`. The readme's rules (GAM) and
the other former `P2` rules went to `P3` with the rest: they are the assistant's restatement until the owner names a
rung. The first `P2` granted is DEV-2, the owner's words on recycling.

## 2026-11-10 — kept art is catalogued by set and kind, and reuse is a soft limit

The owner asked that agents not generate an asset where a kept one fits, and not wear one texture everywhere either:
"we need to keep some middle ground", with context — "mug from kitchen set != mug from other" — and the catalogue
"clear, contains metadata and searchable". On sets: "set is abstract term of assets with similar style and function
… its more of a reuse concept", not one set to a model. On the limit: "i dont want to lock specific cap as p0, we can
test and see how it works and change it if its better". On names: "you can rename anything you want, current assets
are just demo for now".

So every kept texture, part and model has an entry (`asset.json`: about, kind, sets, tags, a texture's material and
faces), the sets are [raw_assets/sets.md](../raw_assets/sets.md), and `qq shapes library` searches them
([raw_assets/index.md](../raw_assets/index.md#the-catalogue)). The how is the assistant's: reuse is governed by kind —
a material is free, a face or a decal is recognised so has a soft cap of wearers, a part is placed wherever it is the
same object — and by set only as a note, never a refusal. The caps are a trial at the assistant's rung, tuned by
looking at the floor. Ids name what an asset is (`tex_drawers_yellow`, not `tex_bench_drawers`), renamed by
`qq sprites rename` so the ledger, which is never edited, still resolves through `raw_assets/_renamed.jsonl`.
