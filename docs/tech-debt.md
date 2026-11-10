# Tech debt

**What is known to be wrong, unmeasured or waiting in what is built, and left so.** Each entry says where it is, what
it costs and what closes it; one fixed is deleted, not struck through. **An entry marked _owner_ waits on a ruling** and
is not closed without one. **_tool_** is a fault or a gap in a `qq` tool, closed in `.qq/`.

## Waiting on the owner

- **The readme's rules carry assistant rungs** (_owner_): `GAM-1`…`GAM-7` ([requirements.md](requirements.md)) are the
  owner's design, stated at `P3` because a rung in the owner's band is granted, never inferred. Closed by the owner
  naming which are `P0`, `P1` or `P2`.
- **The readme's first line names a wasm project** (_owner_): "This is a Dotnet 11 wasm html project." is the owner's
  text, and the client is now plain JS and CSS (WEB-9) with no .NET in the browser. Closed by the owner rewording it.
- **The art's scale** (_owner_): there is no grid a sprite is drawn to, so `qq sprites use --px` is chosen by hand per
  asset — 96 px a cell of footprint width for the devices, as cut for interfaces, props and trim. Closed by a figure on
  `GameConfig` (a capsule cell in pixels) that `use` reads.

- **The model-rendered wall segment is installed and nothing draws it** (_owner_): `assets/devices/any_wall_segment.png`
  (`qq shapes`' first render, from `raw_assets/devices/any_wall_segment/`) proves the chain from model to prompt; the
  page builds walls from the kit's cap and panel pictures under its own camera (`art.js` `structureLook`). Closed by the
  owner choosing whether walls take model renders — the `top` and `front` views of a model are a cap and a panel in
  the kit's frame — or the sprite is removed.

- **A model is drawn by two renderers** (_owner_): `qq shapes` lights its views in Python (`.qq/_shapes_render.py`),
  the game lights the same mesh in WebGL (`src/app/web/wwwroot/scene.js`), kept alike only by the constants each
  `.mesh.json` carries. A change to one pass that misses the other makes the views an agent reviews differ from what a
  player sees. Closed by the owner choosing whether `qq shapes` photographs `scene.js` headless (`qq web`) — one
  renderer, deterministic on one Chromium build only — or keeps both.

- **What an AI capsule does** (_owner_): GAM-1 names it and nothing plays one ([index.md](index.md#known-gaps)).
  Closed by the owner saying how much an AI capsule co-operates — a placeholder that feeds its own devices, or a full
  neighbour that trades through doors.
- **The game's content is the assistant's** (_owner_): the catalogue the game now runs on
  ([economy/](../src/economy/docs/design.md)) — its twelve sections and fifty subsections, seventeen roles, stats and
  need rates — is a proposal, as are the starter ship's floors ([StarterShip](../src/ship/StarterShip.cs): the universal
  fixtures and four devices of one role a capsule) and life support as the ship's measure of "going" (DEV-3). Closed by
  the owner accepting or changing the sections, roles, stats and the starter ship.
- **What death does** (_owner_): the design has a crew member die when health reaches 0
  ([economy/design.md](../src/economy/docs/design.md#the-crew-members-needs)), and leaves open whether the seat is lost,
  goes to the AI, or wakes a new crew member. Closed by the owner's ruling.

- **Only slots and ways are aboard** ([economy/design.md](../src/economy/docs/design.md#where-the-game-stands)): the
  game holds every item, device and way and runs ways on devices, but nothing moves a stat — no item is used (eaten,
  drunk, worn), a way's `gives` does nothing, there are no needs, no decay, no tool wear, no `fits` or `installs`, and
  the crew's ways by hand are run by nobody. The codex describes all of them, and its Items page says they are ahead of
  the ship. Life support "failing" (DEV-3) means only that its first way, the heater, had no power. Closed by the crew's
  stats and needs on `GameConfig`, a use as a player's act at the fixture that takes it, decay and wear on the clock, and
  the crew's ways run from the floor.
- **A device's way list is one dropdown** ([cabin.js](../src/app/web/wwwroot/cabin.js)): the workbench runs 986 ways,
  all in one `<select>` rebuilt with the window every redraw, which is slow to read and to scroll. Closed by a searchable
  picker, or by choosing the way from the device's codex page with the window it was opened from.
- **No loop is checked for loss** ([economy/requirements.md](../src/economy/docs/requirements.md)): ECO-9 says no loop
  of ways gives back all it takes, and nothing measures it. Items carry no mass, and counting units round a loop
  confounds power, catalysts and reusable goods (dishes, tools) with material, so a loop the agents wrote as "4 urine
  → 4 water" passes unseen. Closed by a mass (or a recyclable fraction) on the material items and a `qq economy` check
  that no loop returns at least what it took.
- **The catalogue's data has slips the checks cannot see** ([economy/catalog/](../src/economy/catalog/sections.md)),
  found by the agents writing the codex words:
  - **Likely wrong ids:** `sew a bathrobe` (clo) takes Hair Clippings, `char willow sticks` (art) a Hungry Cricket Song
    Box, `wind a deflector coil from twin coils` (shd) takes `shd-005` rather than `shd-028`, `grow eggplant` takes
    Tomato Seed, and `extract phenol from coal tar` takes Carbon Rock.
  - **Containers made or lost:** prs's freeze ways turn one zip bag into three that come back; `seal ration packs with an
    absorber` and `cook pickle relish` likewise; `seal an emergency ration pack` loses the bar's pouch.
  - **A way on a device that does not fit it:** noodle cakes fried on a dehydrator, crepes on a biscuit oven, a bonsai
    pot fired on the care bench, brews fermented on the bottler.
  - **Names that say otherwise:** cln-042 Worn Mop Head is a worn mop, Ginger Syrup holds no ginger, the Cedar Scent
    Block no cedar, `rlx.blender` is an Aroma Still, Hull Frost comes from a vent.
  - **Near twins across files:** plush stuffing (fun, rlx), toy springs (fun, rlx), dried citrus peel and lemon zest
    (frt, ing), plastic pellets (pol, scr), rubber crumb (pol, scr), printing filament (pol, scr).
  - **Spare parts by two conventions:** some wear into scrap as they decay, others leave scrap when used and never
    decay.

  Each costs a wrong page in the codex and a chain that reads oddly. Closed by a pass over the list, and a twin-name
  check in `qq economy audit` that matches by stem, not only by plural.
- **Storage is not modelled** ([economy/pak.md](../src/economy/catalog/pak.md)): a cool box, a crate or a pallet holds
  goods, slows their decay or stacks them for a door trade, and the catalogue has no column for any of that, so storage
  stands in with a `cabin.clean` rate, as a tidy cabin. Closed by a container's capacity and its decay factor in the
  catalogue (or on `GameConfig`, by kind), read by the game's slots.
- **The ship's stock is one item** ([economy/sections.md](../src/economy/catalog/sections.md#stock)): only the gene
  vault is stock; the rare recyclables the owner described have no items yet (candidates: catalysts, rare metals,
  reactor fuel, all still mined or made).
  Closed by the owner naming what the ship set out with, and their making ways cut to reclaim ways alone.

- **The mine digs, and nothing may** (_owner_, GAM-12, [economy/ore.md](../src/economy/catalog/ore.md)): `ore.drill`
  (XM200 Mining Drill) "drills ore seams and mineral beds out of the regolith stores", `ore.scoop` scoops regolith and
  `ore.tether` hauls asteroids in, while the owner said "There will be no drilling or excavating ground". Their
  sprites are drawn as sealed intake units at a hull port; their names, codex words and ways still dig. Closed by the
  owner saying how raw matter comes aboard — delivered stock, salvage, tethered rubble fed through a port — and `ore`'s
  devices renamed and reworded to it.
- **`docs/p0-stats.md` is a draft outside the index** (_owner_): the owner's "Core Stats" — every item must move a core
  stat, directly or not — stops mid-sentence, its ship stats empty, and states a rule with no ID or rung, so nothing
  cites or checks it. Closed by the owner finishing it and saying its rung, its rule moved into `GAM` or `ECO`.
- **Who is the admin, and who sits where** (_owner_): `?admin` opens the admin's line to anyone who types it, and its
  edits make items and its rate runs every player's time (SHP-6, WEB-8); `?seat=` seats anyone anywhere, and two pages
  may sit one seat. The host checks what each line may do, but not who opened it. Closed by the owner saying how a
  client proves it is the admin or a seat's player, and whether a seat takes one player.

## Left short

- **Olive housings wear grey** (GAM-14, [kit/paints.json](../assets/app/web/kit/paints.json)): `any_cot`,
  `any_sprouter`, `soi_compostbin`, `toi_compostloo` and `veg_sprouter` wore olive panels before the kit; no olive
  enamel swatch is kept, so the stylesheet gives `olive` the grey housing, and `fil_kiln`'s rust went to orange.
  Closed by an olive (and a rust) enamel swatch on the next remotegen sheet (about $0.002 a cell), a `ui_panel_olive`
  modelled as the shapegen skill's "The page's art" says, and its rule in `style.css`.
- **The housings are plainer than the panels they replaced**: one paint, a recessed face and four bolts, where the
  generated panels carried two-tone bands, hazard corners and wear of their own. Closed by more of the kit — corner
  brackets, a two-tone band, worn paint swatches — each kept inside the slices or made to repeat.
- **`qq fit` reads one rule at a time** (_tool_, `.qq/fit.py`): a rule giving a background image or a border image's
  source alone takes its size, slices and repeat from another, so it is passed over (`ui_key_down`, the pressed key, is
  never measured; its slicing is `ui_key_up`'s). Images placed by the page's scripts in a `style` attribute are not
  read at all. Closed by the check following the cascade, or measuring every kit image against the one slicing its
  family shares.
- **The placeholder crate's top is stretched** (GAM-14, `raw_assets/parts/any_crate/any_crate-v1.model.json`): its
  body's 0.9 × 0.9 m top wears `tex_top_steel_rimmed` (1.95:1), drawn 1.95× too tall; a crop would cut its rim. Until
  it has a square riveted steel top, `qq shapes keep` refuses the crate, and the installed `assets/parts/any_crate`
  keeps the stretch on its top, its grey panels (`tileM 0.6` on a 1.07:1 swatch) and its label plate (0.4 × 0.13 m on
  a 2.08:1 picture). Closed by one square cell ($0.002), then the crate re-kept with `"panel"` `tileM [0.6, null]` and
  the label plate 0.192 m high, and installed.

- **Items have no art** (GAM-9, [style.css](../src/app/web/wwwroot/style.css) `.chip`): an item in a slot is a tag the
  stylesheet draws — two letters on its section's colour — not a generated image. Five thousand items is some 560
  sheets at nine a sheet. Closed by icons for the items aboard the starter ship first, then by section, each chip its
  image with the count over it.
- **The art is full-size PNG** (WEB-9): a starter floor asks some 1–2 MB of device sprites, interface panels and trim.
  Closed by serving WebP (or lossy PNG) at the size drawn, made by `qq sprites use`.

- **One steel top is worn by five models** ([catalogue](../raw_assets/index.md#the-catalogue)):
  `tex_top_steel_rimmed`, the bench's top, is also the top of `any_cot`, `any_crate`, `any_lifesupport` and
  `cln_dishwasher`, past the face cap of 3, and reads as one object cloned across the floor. `tex_vent` (9 wearers)
  and `tex_label_plate` (7) are past the decal cap of 6. Closed by own top swatches for the cot, the life support and
  the dishwasher on their next sheet (about $0.002 a cell), and by looking at the floor to settle whether a vent or a
  label is Company issue that may repeat — `qq shapes library` lists every such note.
- **Two kept swatches nothing wears**: `tex_handwheel` (the backed handwheel, superseded by `tex_handwheel_cutout` on
  `any_hatch`) and `tex_wall_cap_worn` (the worn wall cap the kit never laid). Cost $0.0045, nothing drawn. Closed by a
  model that wears them, or by the owner's word to delete them.
- **Two lamp props nothing draws** (`assets/app/web/props/lamp_off.png`, `lamp_amber.png`): the page's lamp over each
  running device was their wearer, and a device's lamps are its model's now (WEB-12); the header's status lamp wears
  `lamp_green` and `lamp_red` alone. Closed by a window's prop wearing them, or by deleting them with their `.src.json`.
- **Every wall and door is 1×1** (GAM-10, [Vessel.Enclose](../src/ship/Vessel.cs)): the owner said some are 1×2 or
  1×3, and the catalogue has only `any.wall` and `any.door`, each one cell. Which pieces run longer — a wide door, a
  wall with a window, a long service panel — is unsaid (_owner_). Closed by those entries in `any.md`, their sprites,
  and `Enclose` laying them along an edge where they fit.
- **The west-camera kit pieces are installed and unused** (`any_side_panel*`, `any_panel_trim`, `any_door_edge_*` under
  `assets/devices/`): the leaning walls use none of them. They cost a few hundred KB in `assets/` and nothing at run
  time. Closed by deleting them with their `.src.json`, the raw variants kept.
- **Floor and wall tiles turn their light with them** ([art.js](../src/app/web/wwwroot/art.js) `deckOf`,
  `structureLook`): one tile per set of edges is drawn and turned to fit, so a turned tile's bevels are lit from
  another side than the top left, and two tiles of one plate differ a shade where they meet. Closed by each turn drawn
  as its own tile, lit from the top left.

- **The ship lives in the host's memory** ([ServedShip](../src/app/host/ServedShip.cs)): a host started again lays a
  new starter ship, and every move made on the last one is gone. Closed by the host saving the ship and laying it from
  the save.
- **A move shows once the host has run it** ([cabin.js](../src/app/web/wwwroot/cabin.js)): a dragged item springs back
  to its slot until the frame that moved it comes, a round trip later; on a slow line that reads as a refusal. Closed by
  the page holding a dragged item where it was dropped, marked as waiting, until the answer.
## Untested

- **The socket is checked by eye** ([Client](../src/app/host/Client.cs)): which actions a player's line refuses, a
  frame sent only on a change, and the newest frame replacing one unsent are shown by `qq web` pictures, not tests. The
  views a seat is sent are tested (`CabinViewTests`). Closed by a test driving `Client` over an in-memory socket.
- **What a live part shows is checked by eye** ([cabin.js](../src/app/web/wwwroot/cabin.js) `signalsOf`,
  [scene.js](../src/app/web/wwwroot/scene.js) `liveFrame`): the shares a gauge reads and the colour a lamp takes are
  seen in `qq web` pictures, not tested; the page has no test runner (WEB-9). Closed by the signals moved to a module a
  headless check can call with a frame and read back.

## Unmeasured

- **Every frame re-describes the whole floor** ([cabin.js](../src/app/web/wwwroot/cabin.js) `drawFloor`,
  [scene.js](../src/app/web/wwwroot/scene.js) `setScene`): a frame that changes anything — a count in one slot — has
  the page lay out every deck cell, wall and device again and compare it with the last as one JSON string, before the
  scene finds nothing to rebuild. On the admin's page that is nine capsules' worth. Its cost on a slow machine is
  unmeasured. Closed by timing it, and describing the floor only when what stands on it changed.
- **Live parts redraw the scene every frame while ship time runs** ([scene.js](../src/app/web/wwwroot/scene.js)
  `draw`, `movedBox`): the costly passes are drawn only over the box round what moved, but that is one box round every
  moving part, so on the admin's overview of nine capsules it is most of the picture, every display frame. A zoomed
  device holds 60 frames a second on this machine's GPU; a weak one is unmeasured. Closed by timing it there, and by a
  box per moving part, or a lower rate for a part too small to see move.
- **The starter ship's balance** ([GameConfig](../src/core/config/GameConfig.cs) `Devices`, `Starter`): a way's
  catalogue minute is one ship second, each device starts with three cycles' worth of what it runs on, and chests start
  empty — all set by hand. Whether a capsule can keep its life support powered from its own solar strip, and how much
  handling that takes, is unknown. Closed by a headless run of the starter ship that reports each item's made-vs-spent
  rate.
- **The catalogue's balance is static** ([economy/](../src/economy/docs/resource-tree.md)): `qq economy` compares
  each consumable's points a work-minute with its peers, but no ship has run on it, so whether a crew of N keeps every
  need with its roles' devices, and how many door trades a day that takes, is unknown. Closed by a headless run over the
  catalogue that reports each need's made-vs-spent rate for a ship of N capsules.
- **The catalogue's numbers are untuned** ([economy/resource-tree.md](../src/economy/docs/resource-tree.md#balance-flags)):
  921 sources (items used, ways run) sit four times off their stat's median points a work-minute. Deep chains make
  some goods cost thousands of work-minutes, so a stat's median rounds to 0.00 (`cabin.o2` one-shots), while an ambient
  durable's lifetime points (rate × decay hours) dwarf any one-shot's: an oil painting's 16 000 stress against a soak's
  12. What bounds a durable in play is the slots of where it belongs, which the valuation does not know. 3817 of 5000
  items are made one way only; the common goods have two to seven. Closed by a tuning pass that brings each stat's
  sources within the factor, against need, decay and way rates on `GameConfig`, and a durable valued over a day in its
  slot rather than its life.

## Tools

- **The `qq` tools are not in git** (_tool_): `.qq/` is ignored by the machine's global gitignore
  (`~/.config/git/ignore`), as the qq contract wants, so a clone of this repository on another machine has none of
  them. Closed by the owner choosing to commit `.qq/` (a `!.qq/` line in `.gitignore`) or to keep it per machine.
- **The catalogue page shows live parts at rest** (_tool_, `.qq/_shapes_viewer.html`): a model's lamps, needles and
  bars are drawn as modelled; only `qq shapes render` lists them (`live N:`) and only the game moves them. Closed by
  the model tab listing each live part, with a control to drive its signal.
- **`qq web` has no caption** (_tool_): a picture carries no stamp of what it shows or when, which traffic's captioned
  shots did. Closed once the page says its own state on the console for `qq web` to stamp.
- **No profiler** (_tool_): traffic's `qq prof` (perf over a running process) was not ported; nothing here runs long
  enough to profile yet.
- **`any_wall_segment-v1`'s kept model has its cap and kick strip sunk into its core** (_tool_): kept before
  `qq shapes` checked overlaps, so the viewer lists two on it; the draft in `.tmp/shapes/` groups them. Costs nothing
  drawn — the render is right. Closed by keeping `any_wall_segment` again from the draft.
- **The catalogue's soft caps are guesses** (_tool_): `_catalog.WEARERS_SOFT_CAP` — a face 3, a decal 6, a part 6 —
  was set before any floor was judged against it; the owner asked for it tested and tuned, not fixed. Closed by a look
  at a floor of the installed devices, each note of `qq shapes library` judged by eye, and the caps moved to match.
- **The near-match is words, not pictures** (_tool_): remotegen's `near:` warning scores a cell's brief line against
  the catalogue's abouts and tags (`_catalog.near`), so a kept swatch described in other words is missed, and an
  entry's about written loosely matches too much. Closed, if misses show, by comparing the frame's cut against the
  kept pictures as well.
- **`any_washbasin-v4`'s kept model has four items resting on nothing** (_tool_): its mirror, cup bracket, cup and
  toothbrushes, kept before `qq shapes` checked floating items. Costs nothing drawn while v4 is not installed. Closed
  by keeping `any_washbasin` again from a draft that hangs them on the wall.
- **Installed meshes predate the tool's last changes** (_tool_): every `assets/devices/*.mesh.json` and
  `assets/textures/*-seamless.webp` was exported before `qq shapes` gained facets sized to each radius, dome mapping
  and a contrast-keeping seamless blend; they change only when `qq sprites use` installs them again. Costs faded bands
  where a tiled texture repeats, on the floor the player sees. Closed by `qq sprites use` again for each installed
  model render.
- **The floor's 3D scene is a first cut** (`src/app/web/wwwroot/scene.js`): what the pointer is over is read back
  from the picture at once (`readPixels`), which stalls the GPU a moment each move over the floor; one shadow map
  covers the whole ship, so a large ship's shadows coarsen; faces turned from the camera are culled by pixel where
  `qq shapes` culls by triangle; the triangles (`.mesh.bin`, 2.4 MB for twenty) go uncompressed, the host compressing
  no `application/octet-stream`; and a device's lamp and a door's tag are page elements laid over the scene, not in
  it. Costs a hitch on a slow GPU, soft shadows when zoomed on a big ship, a slower first load. Closed by an
  asynchronous read-back (a pixel buffer and a fence), a shadow map fitted to the view, triangle culling exported
  with the mesh, and the triangles quantized or compressed.
- **The spend ledger misses calls that brought no image** (_tool_): remotegen writes `raw_assets/_spend.jsonl` with
  a frame's record, so a refusal or a dropped reply that was still billed is on neither, and the 72 calls before the
  ledger were filled in from `.tmp/gen/index.jsonl` as it stood (2026-11-09), whatever an earlier wipe removed. The
  total can read low against `remotegen.py credit`. Closed by remotegen writing a ledger line for every billed
  response, image or not.