# Requirements — the game as a whole

The rules that belong to no single slice. Each states a relation and carries a rung ([priority.md](priority.md)).
A rule about one feature is that feature's own `docs/requirements.md`.

## GAM — the game

These are the owner's design as written in [../readme.md](../readme.md), stated one a line. They carry assistant
rungs until the owner grants any of them `P0` or `P1` ([tech-debt.md](tech-debt.md)).

**GAM-1** `P3` The ship is a grid of capsules, and each capsule is controlled by one player or by the AI.

**GAM-2** `P3` A capsule is joined to at most four neighbouring capsules, one a side, and interacts directly with
those alone.

**GAM-3** `P3` Players never communicate directly: what passes between two capsules passes through the 3×3 door slots
between them, as items shared and dragged.

**GAM-4** `P3` A capsule is an N×N grid of cells, with a door to each neighbouring capsule.

**GAM-5** `P3` A player holds no personal inventory: every item is in a container or a device placed on a capsule's
grid, and is opened and dragged from there.

**GAM-6** `P3` A device may sit on a capsule's grid or be placed on it, may hold an inventory and actions of its own,
and produces resources by consuming others on an interval.

**GAM-7** `P3` The game is event-based: its state changes when an event happens — a player's action, a device's
interval elapsing.

## The look and the voice

**GAM-8** `P2` Everything a player sees or reads — the interface, the art, names, captions, lore and flavour — is in
the used-future, cassette-futurist style of [style.md](style.md): heavy, worn 1970s–80s company hardware, monochrome
phosphor screens, red for alerts alone, so the player feels like an employee operating company equipment.

**GAM-9** `P2` Every asset the game shows is a generated image; CSS and SVG may place, size and tint one, and draw
only a screen's text, never an asset.

**GAM-10** `P2` Everything on a capsule's floor but the floor itself is a device — doors and walls included, each a
device standing on the floor's cells, 1×1 and some 1×2 or 1×3 — the whole floor drawn in 3D, no picture of it drawn
ahead: each device its model (one with no model yet a plain crate on its footprint), seen by a camera that starts tilted a
little from straight down and that the player turns, tilts and zooms with the mouse (or a pinch); a human one cell tall,
nothing larger than 3×3 cells.

**GAM-11** `P2` Every device has an interface: a draggable window drawn as a flat, stylised front of that device, built
from a shared catalogue of props, with mechanical controls by preference and a screen only where a device is special
or high-tech. It shows no control, gauge or readout that does nothing: each is placed from the props when the device
has it.

**GAM-12** `P2` A capsule is one operator's work station and living quarters aboard a ship in space: its devices are
compact, automated equipment one person runs — industrial, not heavy plant; nothing digs or drills ground — and it
is lived in, worn but kept, never filthy.

**GAM-13** `P0` Every asset the game shows is a render of a 3D model — a few textured shapes whose textures are
generated (GAM-9), rendered from the game's cameras: devices, walls and doors, the floor, interface panels, their
props and the space beyond alike.

**GAM-14** `P2` A generated image is shown at its own proportions — resized, never stretched — on every element of the
page (panels, frames, plates, labels, keys, menus, trim) and on every face of a model. An element longer or larger
than its image repeats a part made to tile, or takes an image of its own made to its size.
