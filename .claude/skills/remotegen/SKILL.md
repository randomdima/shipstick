---
name: remotegen
description: Generate and edit images through OpenRouter for this project's art — the texture swatches 3D models wear (every game asset is a model, GAM-13 P0, made with the shapegen skill), and mockups — always in the game's used-future style (docs/style.md) — GPT Image 2.5 Sunburst at quality low, transparent background, unless the owner says otherwise; at least nine to a sheet, three attempts a sheet. A generation's shape (model, settings, how many calls an asset takes) is never changed without asking the owner first. Billed per image. The only image generator; local models are not used. Use for any image: texture sheets, swatches, mockups, "generate an image", "generate textures", "edit that image", "another version".
---

# remotegen

**No sprite is drawn to be installed any more**: every asset the game shows is a 3D model's render (GAM-13, `P0`) —
the [shapegen](../shapegen/SKILL.md) skill. A sheet here is the swatches models wear, or a mockup.

`.claude/skills/remotegen/remotegen.py` asks OpenRouter's Image API for one frame per call, on the owner's settings.
Each frame goes to `.tmp/gen/frames/<name>-v<N>.png` (transparent, every pixel under alpha 16 cleared to transparent
black — the glow the model leaves round each drawing) with one record in `.tmp/gen/index.jsonl`: the exact prompt,
model, settings sent, cost, the asset ids it draws (`--cells`) and every picture sent as `inputs`, each copied to
`.tmp/gen/inputs/<sha>.<ext>` as it was when sent. Its cost and cells also go on `raw_assets/_spend.jsonl`, committed,
so a frame nothing was kept from still counts after `.tmp/` is wiped. Cutting, keeping and installing are
`qq sprites`'s; `qq sprites cost <id>` is an asset's share of every frame that asked for it, attempts and all.
`openrouter.py` beside it is the bare client (key, catalogue, billed request).

## Commands

```bash
R=.claude/skills/remotegen/remotegen.py
$R gen "PROMPT" --cells IDS.json --name STEM [--aspect 3:2]
$R edit --image REF [--image REF ...] -p "PROMPT" [--cells IDS.json] [--mask M.png] [--name STEM] [--aspect 3:2]
$R credit            # spent / left on the key
$R list | show ID
```

`REF` is a path, a frame id (`devices_a-v2`) or a name (its newest frame). Output paths print one per line; settings,
usage, time and cost go to stderr. The model's own `supported_parameters` decide what is sent. A 429 is retried after
30, 60 and 90 s; a dropped reply to a POST is not, since the frame may already be billed.

`--mask M.png` is a PNG of image 1's size whose transparent area is what gets replaced; every pixel outside it stays
byte-identical. Make it with `qq sprites mask FRAME IDS`. The `video` command exists in the script and is asked of the
owner before any use.

## The owner's rules for a run

These were the owner's in the project this tooling came from; they hold here until the owner changes them.

- **A generation's shape is the owner's, and is never changed to get a result**: the model, every setting sent
  (quality, background, aspect), and how many generations one asset is made from. Another model, setting, a second
  call for the same asset or a pre/post pass is asked first and generated only on a yes — never "one trial to see".
  Only the brief's wording, a `--mask` redo and the attempts the cap allows are yours.
- **What is kept is used, never asked again.** Before a brief, search `qq shapes library` for each cell (the catalogue
  of kept textures, parts and models; [raw_assets/index.md](../../../raw_assets/index.md#the-catalogue)): a cell goes
  only to what nothing kept can be, or to a face or decal past its soft cap. The script refuses, before billing, a
  cell whose id is kept already, under its name or a former one — except one kept from this sheet's own earlier
  attempt or from the frame a `--mask` redo edits; another generation of a kept asset is `--again=ID,…`, on the
  owner's word only. It prints `near: <cell> reads N% like kept <id>` for a cell's line that matches a kept entry:
  stop, and either wear the kept one or say in the brief how the new one differs.
- **Name a cell for what it is, not what it is first made for**: `tex_drawers_yellow`, not `tex_bench_drawers` — it
  will be worn by other models. Keeping it, catalogue it (`qq sprites catalog`): `qq sprites check` fails until its
  kind, sets, material, fits and tags are filled.
- **Defaults**: `openai/gpt-image-2.5-sunburst`, quality `low`, background `transparent`. `--model`, `--quality`,
  `--background`, `--past-cap` and `--again` are for the owner's word only. A sheet is `--aspect 3:2` (1536×1024).
- **At least nine assets to a frame**, 3×3; smaller assets more to a sheet. Never a frame of one: a lone asset drifts
  from its set's palette and costs most of a sheet.
- **Every brief is in the game's style** (GAM-8 to GAM-11): read [docs/style.md](../../../docs/style.md)'s "What is
  drawn, and how" and "Art" and say them in the brief — 1970s–80s used-future heavy-duty machinery, metal in dull dark
  yellow, yellow and orange over grey and black with occasional hazard stripes, glass reinforced and blue-green,
  ceramic plain, fabric bulky and padded, green phosphor screens, muted colours, red only on a fault lamp, no legible
  text, no real brand. A device is compact, automated equipment one operator runs in a capsule that is also their
  home in space — not heavy plant, nothing that digs — worn but kept, never grimy (GAM-12). A swatch is a flat face of
  one material, seen straight on; a human is one cell. A frame that drifts from any of it is a defect a redo fixes.
- **Get it in one go.** Before v1, read the family's `prompting.md` under `raw_assets/` and write the brief to avoid
  its recorded faults. A v2 needs a real defect a kept cell cannot carry; a v3 a stronger reason still.
- **Three attempts per generation at most** (one `--name`): v1, v2, v3, a mask redo included. The script refuses a
  fourth before it is billed. Not good after three: stop and report — the frames' paths, what is wrong cell by cell,
  what each attempt changed, the spend.
- **Between attempts, `Read` the frame** and judge every drawing: the thing asked for, its proportions, the style
  asked, no text, no corruption, the grid kept so `cut` can tell which is which. Few wrong → `--mask` redo on the frame
  itself (image 1, nothing else sent); most wrong → a whole re-roll with a line naming each fault.

Sunburst at low is ~15 s a 3×3 sheet, and as billed (`_spend.jsonl`): ~$0.008 a `gen`, ~$0.0095 an `edit` whose
image 1 is a small sprite, ~$0.021 one whose image 1 is full size — the picture sent is most of an edit's price.

## From frame to the game

A frame is scratch; what goes into git is each asset's cut with the record of how it was made
([raw_assets/index.md](../../../raw_assets/index.md) is the whole rule).

```bash
# 1. read the family's raw_assets/<path>/prompting.md, if any; write the brief to .tmp/gen/briefs/<sheet>.txt —
#    the grid, the style line from docs/style.md "Art", then each cell in reading order: what material it is, seen
#    straight on, filling its cell edge to edge, "no frame, no text"; the ids in that order as one JSON list,
#    .tmp/gen/briefs/<sheet>.cells.json
$R gen "$(cat .tmp/gen/briefs/tex_a.txt)" --cells .tmp/gen/briefs/tex_a.cells.json --aspect 3:2 --name tex_a
qq sprites cut tex_a-v1                          # drawings found in the cells' order; read _overlay.png
qq sprites mask tex_a-v1 steel_panel             # the --mask for a redo of that drawing
# keeping a swatch and wearing it on a model is the shapegen skill's
# 2. the set's lesson into raw_assets/<path>/prompting.md, citing the variants
```

Once the style is set, later sheets are `edit` with a style picture as the only image: finished art from the game,
none of it an asset the frame draws.

A sheet of texture swatches for a model is the same generation with another subject; the
[shapegen](../shapegen/SKILL.md) skill has its brief and the rest of the way to a sprite.

## Key and money

The key is read from `OPENROUTER_API_KEY` or `~/.qq/openrouter.key`; nothing about it is in the project and it is
never printed. Every frame is a billed request. A 401/402/403 is the key's or the account's: report it and stop. Run
`credit` before a long series.

## Rules

- **Never** `cat`, `base64` or otherwise read image bytes into context; `Read` the PNG to judge it.
- Refine with `edit` on the previous version and the same `--name`, so the lineage is in `inputs`.
- Name a sheet for its set (`devices_a`), lowercase with underscores.

## Reporting back

Path, a one-line description, the attempt it took, and the cost: the frame's, and from `qq sprites cost <ids>` each asset's
all-time cost with its retries, and its current variant's.
