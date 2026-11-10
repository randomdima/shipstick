# Textures — what the wording did

Swatches for models (the [shapegen](../../.claude/skills/shapegen/SKILL.md) skill), never installed themselves.

- **Nine swatches came out right in one go** (`walltex_a-v1`, score 4, an `edit` with `smooth_style.png` as image 1):
  "A sheet of 9 separate flat material swatches for texturing simple 3D game models, each swatch a flat rectangle seen
  exactly face on, with no perspective, no depth, no cast shadow and no outline, evenly lit", each "fills its
  rectangle edge to edge with square corners". Every asked proportion held — square, "twice as wide as tall", "four
  times as wide as tall" — and the decals (`tex_vent`, `tex_hatch`) came with the plain margin asked.
- **"Repeating" gave even surfaces** with no rim, but **the pipe swatch (`tex_pipe-v1`) has its roundness painted in**,
  lighter across its middle: on a cylinder that is lit twice. Ask a pipe as "flat painted steel, evenly lit, no
  roundness, no highlight".
- Cut swatches are small (about 280 px a cell of a 3×3 sheet) and keep a dark hairline at their edges: `insetPct` 3–8
  crops it. One metre of wall at 256 px a cell is near a swatch's own size.
- **A proportion asked with a drawing in it drifts toward 2:1** (`galleytex_a-v1`, draft): the drawer front asked "four
  times as wide as tall" came 2.4:1, the cutting board asked "half again as wide as tall" came 2:1; the plain
  surfaces kept square. Size the part to the swatch as cut rather than re-roll for it.
- Pictures of things laid in a container (utensils in a drawer, mince in a dish) came out whole and clean, with the
  container's rim at the edges as asked — a cheap way to fill a part with detail no shape carries.
- **The asset's own sprite as image 1 gave nine for nine in one go** (`benchtex_a-v1`, score 4, an `edit` with
  `assets/devices/any_bench.png` alone): "Image 1 is the workbench these swatches texture: match its colours, paints,
  materials and wear exactly, and take each swatch's surface from the matching part of it. Do not draw the bench
  itself, and nothing in perspective". Palette, wear and parts (bolted top rim, drawer frame, tool tray) came from the
  sprite; nothing came in perspective.
- **A swatch per large visible face, with its detail drawn in**, read as the sprite; generic materials
  (`galleytex_a` steel and yellow on every face) read as a grey box. The top as one picture with its rim and corner
  bolts, the drawers as a bank in their frame, the tray full of tools, a motor's top with its vent: repeating
  materials are only for sides, ends and small parts.
- **Group a long run of small parts into one 2:1 swatch and repeat the part**: three columns of two drawers asked as
  "two drawers stacked, in a thin frame round all edges and between them", twice as wide as tall — came 1.7:1, still
  drawn whole; the 4:1 single drawer drifts further.
- **"Repeating" swatches still keep a darker rim** (`tex_yellow_enamel-v1`): tiled, it drew a cross on a 0.2 m
  wheel-guard end. `qq shapes` now cross-fades every tiled texture's edges, so no re-roll is needed for it.
- **Repeating materials carry across models; large plain pictures do not** (`any_galley_table` draft): its yellow
  body and its steel swapped for `tex_wall_cap-v1` and `tex_bare_steel-v1` rendered the same, but its plain steel top
  did not — `tex_bare_steel` tiled over 2 × 1 m showed its repeat as blotches, fitted it stretched its brushing coarse.
  Brief a material once, repeating, for the whole family; brief a large face's own picture per model.
- **A sheet half for the model and half for its family held** (`tabletex_a-v1`, nine for nine, sprite as image 1):
  "swatches 1 to 6 texture image 1 … swatches 7 to 9 are materials of the same capsule that are not in it" — the six
  took the sprite's colours, the three (`tex_ceramic_white`, `tex_orange_enamel`, `tex_glass_wired`) the style line's.
- **Both proportions drifted toward 2:1 again**: "three times as wide as tall" came 2.3:1 (`tex_table_top`), and
  "four times as wide as three" came 1.9:1 (`tex_tray_floor`) — a narrow ask drifts wider as a wide one drifts
  narrower. Ask 2:1 or square, and size the part to the cut. A swatch wider than its grid cell is split by a
  `--grid` cut: `--whole=0.7` keeps it whole.
- **Bolts are allowed on device swatches** (style.md's Metal); "NO bolts" is the wall kit's line
  ([devices/prompting.md](../devices/prompting.md)).
- `any_wall_segment-v1` (score 3) wore `tex_wall_cap`, `tex_wall_face`, `tex_trim_dark`, `tex_pipe`,
  `tex_kick_strip`, `tex_vent`.
