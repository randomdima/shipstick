# Style — the used future

**The player is an employee operating company equipment, not a consumer using a product.** Everything a player sees
or reads — the interface, the art, names, captions, the codex, lore and flavour — is heavy 1970s–80s industrial
hardware built by an indifferent corporation: utilitarian, cold, functional and worn, never polished or friendly
(GAM-8), and everything drawn is a generated image (GAM-9 to GAM-11). The owner's words are quoted in [decision-log.md](decision-log.md); this page is how they are kept.

Read it before writing anything a player meets: a caption, a codex line, a name, a stylesheet rule, an image brief.

## Lore

What the voice speaks from. The facts here are the assistant's, kept until the owner changes them.

- **The Company** is Consolidated Orbital Freight — "the Company", `COF` on a stencil. It owns the ship, every device,
  every item, the air and the operator's time. It addresses no one by name.
- **The ship** is a COF modular capsule carrier: a grid of identical capsules bolted together, each crewed by one
  contract **operator**. A capsule is the operator's work station and living quarters both: they work, eat, wash and
  sleep in it (GAM-12).
- **The ship is in space.** There is no ground: nothing digs, drills or excavates. What comes aboard comes through a
  hull port, already loose.
- **Operators do not talk.** Voice traffic between capsules is not provisioned under the operating contract; the door
  slot is the only sanctioned transfer between stations (GAM-3). Notes, tags and tokens passed through it are the
  operators' own workaround, which the Company tolerates and does not support.
- **The Company's voice** is policy, liability, schedule and cost. It never thanks, never apologises sincerely,
  never jokes on purpose; it reminds, notifies, deducts and reassigns.
- **The operators' voice** is tired, dry and practical: scrawled on a panel, written in a log, passed on as a rule of
  thumb. Black humour, sparingly; never cheerful.
- **A code never says what a player may not know.** No capsule number or neighbour identity reaches a player's view,
  however bureaucratic it would look; where their capsule stands shows only as the ship's walls drawn round it
  (WEB-1).

## Names

Names are the catalogue's ([../src/economy/catalog/sections.md](../src/economy/catalog/sections.md)) and the page
shows them upper case. Every name is unique across the catalogue, at most 32 characters, holds no `|`, and **never
puts a capital, a hyphen and a digit together** — the citation checker reads `AB-12` as a rule's ID; write `AB12`,
`Mk II`, `Type 2`.

**A device is a model designation and what it is**: `<model> <noun phrase>`. The model is two to four capitals and
one to four digits, a trailing capital or `Mk II` allowed — `HX200 Moisture Condenser`, `WB2 Workbench`,
`AG40C Berry Bed`. The noun phrase is plain words, the device's established name; the model is what the Company
stamps on it. The devices of one subsection share a letter series, the way one product line does.

**An item is inventory nomenclature**: `<noun>, <qualifier>[, <qualifier>]`, the thing first and what kind after —
`Water, Drinking`, `Peel, Citrus`, `Bag, Waste, Filled`. A thing with nothing to tell it from its kin stays one noun:
`Oxygen`, `Urine`. A specification is a qualifier: `Grade B`, `Type 2`, `Mk II`, a metric size `2 mm`. An item that
names a device names its noun phrase and never its model — `Kit, Workbench`, `Cell, Solar Strip` — so a device's
model can change alone.

No brand names, no real company, no praise: never `premium`, `deluxe`, `cosy`, `tasty`, `fun`. A way stays a short
lower-case verb phrase (`boil water`); the page shows it upper case.

## Captions and copy

The page's own words — headings, labels, buttons, states, hints, notes.

- **Labels are nouns and codes**, upper case by the stylesheet: `CYCLE`, `NEXT CYCLE`, `OUTPUT FULL`, `STATION`. The
  source writes them lower case, so the stylesheet alone decides.
- **Copy is terse and impersonal.** The imperative for instructions, the passive for facts: "Drag items between open
  panels." "Transfer refused." No "you're", no "please", no "oops", no exclamation mark, no emoji.
- **States are the machine's words**: running, idle, input short, output full, refused, nominal, failing.
- **Codes are printed, not hidden**: an item or a device shows its id upper case beside its name, as a stock code.
- **Times and quantities carry their metric unit**, upper case on the page: `120 S`, `45 MIN`, `72 H`.

## Codex words

Every item and device has two (ECO-12), written in the subsection's `## Codex` table.

**`about`** — one plain sentence in the register of an operating manual: impersonal, present tense, what it is and
what it is for. No joke, no figure (the codex reads those off the tables), no second person.

**`flavour`** — one line, at most about 110 characters, in one of these voices; a subsection mixes them, the Company's
the most often:

| Voice | Reads like |
|---|---|
| Stencil or label | `DO NOT VENT INTO CABIN. COF PROPERTY.` |
| Company notice | `Replacement of lost units is deducted at cost. Ref 4471/C.` |
| Procedure or form | `Report spoilage on Form 27B within one shift. Proc 114 applies.` |
| Maintenance tag | `Inspected, passed, rev 7. Inspector's initials illegible.` |
| Operator's note | `Still smells of the last operator. So does everything.` |

Form, procedure, revision and serial numbers are invented freely and look official — `Form 27B`, `Proc 114`,
`Rev 7`, `SN 0447 1121`, `Ref 4471/C` — under the same never-a-capital-hyphen-digit rule as names. No `|`.

## What is drawn, and how

**Everything drawn is a generated image** (GAM-9). CSS and SVG place, size, crop and tint images and lay out text;
they never draw an asset — no bolt, stripe, button or frame painted in gradients. The one thing the stylesheet draws
is a screen's content: phosphor text on black glass.

**The floor is one 3D scene, its camera starting tilted a little from straight down** (GAM-10) — 18° — so a device's
top fills most of what is seen and a narrow strip of its front face shows; the player turns it round the middle of the
view, tilts it toward the floor and zooms it in to a single device, and every side of a device and a wall can come
into view, close. Every device is a model (a plain crate until it has one); the walls, doors and deck are the kit's pictures on
blocks and plates. Briefs and models are judged from the starting camera, and nothing a turn shows may be left
unmodelled — a back face is drawn like a front. **A human fits one grid cell with room around it**; a heavy door is one
cell; nothing is larger than 3×3 cells. Size on the grid is approximate — what a device's interface and inventory hold matters more.

There are four kinds of asset:

| Kind | What it is |
|---|---|
| **Floor tile** | The deck the capsule stands on, in enough variants to cover a floor without visible repeats |
| **Device** | Everything on the floor that is not the floor — fixtures, machines, storage, **doors and walls**, each standing on floor cells, a wall or a door 1×1 and some 1×2 or 1×3 (GAM-10). Its model in the floor's scene, or the plain crate until it has one. A wall is built from a kit of parts that join in any layout: a cap on top chosen by which neighbours are wall, a panel on each face no wall continues past, stacked three high, a fitting on the top one alone, every wall the same height — below a person's, so the camera sees over it; nothing stands on a cap, and nothing carries a bolt. A door is a wall cell with the door's parts laid on it: a lintel across the cap, a heavy watertight door on the face it opens through, a hazard sill on the floor inside |
| **Device interface** | The draggable window a device opens (GAM-11): a flat, stylised front of that device — a plain housing in the device's paint, its name on a plate in the band and its keys in a key bay, sliced round whatever it holds and never stretched (GAM-14), and **no control drawn on it**. Every button, dial, gauge, lamp or screen is a prop placed on it by the page, and only where the device has that control in the game. Mechanical controls by preference; a screen only for a special section or a high-tech device. Devices alike may share one |
| **Screen** | A CRT section inside an interface, or the codex: black glass and phosphor text, drawn by the stylesheet, framed by a generated bezel |

**Props** are the reusable catalogue every interface is built from: push buttons, keys, toggles, rotary knobs,
lamps, gauges, slot sockets, close and help buttons, bezels, label plates, bolts and hazard trim — each a generated
image with its states (up, pressed, on, off).

## Interface

The page is a console of Company hardware. Its colours are the tokens on `:root` in
[style.css](../src/app/web/wwwroot/style.css); a rule uses a token, never a raw colour.

- **Screens are CRTs**: black glass, monochrome green phosphor text with a soft glow, faint scanlines. Amber is
  caution — something being edited, something to watch. **Red is an alert and nothing else**: a device starved or
  full, a refused move, a failing capsule.
- **Icons on a screen** keep its vibe — simple pictograms, scanlined and glowing — and may take a colour where one
  colour alone would be hard to read.
- **Off the screens is heavy-duty machinery**: the housings, frames and keys are the generated props.
- **Round the ship is space**: the page's backdrop is a generated sky, muted and cold as through thick glass — small
  points of light, a dull haze, a far galaxy; no neon, no planets, no ships.
- **Type**: wide upper-case sans for labels and headings — Michroma, served by the host from `assets/` — and the
  system's monospace for readouts and body text. Nothing is fetched from outside the host (WEB-9).
- **Motion is mechanical or none**: a lamp lights, a bar fills, a cursor blinks. Nothing bounces or eases in.
- **Controls look like controls**: toggle and push buttons with a pressed state, not links dressed as pills.

## Art

Generated images keep one world (the [remotegen](../.claude/skills/remotegen/SKILL.md) skill's briefs carry it).
Colours are a little dull and muted throughout.

**Compact, automated, one operator's** (GAM-12). A device is industrial equipment sized for a cabin and run by one
person — a self-contained unit with its works boxed in, a hopper or a hatch where things go in — not heavy plant: no
excavator arms, rigs, chimneys or wheelbarrows. **Lived in, kept**: scuffs, worn edges, chipped paint, tape and a
replaced panel, and the odd personal touch where someone lives; no grime, rust, oil pools, soot or litter.

| Material | Looks like |
|---|---|
| **Metal** | heavy-duty machinery, compact: dark yellow, yellow and orange paint over grey and black steel, with occasional hazard stripes; bolts, rivets, vents, worn edges |
| **Glass** | reinforced, with a blue-green tint; wired or laminated |
| **Ceramic** | plain ceramic: off-white, glazed or matt |
| **Fabric** | bulky, padded and quilted, warm in style (not in colour): canvas, webbing, felt |
| **Plastic** | worn off-white or grey moulding |

- Screens and indicator windows glow green phosphor on black; lamps are green, amber or — for a fault only — red.
- No legible text in an image: a stencil is a mark, not a word.
- Pictograms are single-colour, in the manner of industrial safety signs.

## Never

Rounded friendly bubbles, pastel or candy colours, glossy gradients, glass blur, neon cyberpunk pink and blue, cute
mascots or faces on machines, marketing cheer, emoji, a real brand or company, red as decoration, and anything that
would make the player feel like a customer. Heavy plant, ground works and filth: a capsule is a small, kept home.
