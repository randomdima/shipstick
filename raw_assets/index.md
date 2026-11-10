# raw_assets

**Where every image the game uses came from, kept so it can be asked for again, adjusted, or compared with what else
was made for the same asset.** Nothing here is read by the build: a sprite under `assets/` is made from a variant here.

Art is generated with the [remotegen](../.claude/skills/remotegen/SKILL.md) skill, nine or more assets to a frame,
asked in words on a transparent background, and cut, kept and installed with `qq sprites`. Every brief is in the
game's used-future style ([../docs/style.md](../docs/style.md#art), GAM-8), and a drawing that drifts from it is
scored down and not used.

## What lives where

```
.tmp/gen/                          scratch, never committed
  briefs/<sheet>.txt               the prompt a frame was asked with, and <sheet>.cells.json, the ids it draws in order
  frames/<name>-vN.png             every frame (a whole sheet), and its record in index.jsonl
  inputs/<sha>.<ext>               every picture a frame was sent, by content
  cuts/<frame>/<id>.png            each drawing taken whole; _overlay.png boxes each, _mask_<ids>.png a redo's mask

raw_assets/                        committed
  <path under assets/>/<id>/       one folder per asset, at the path its sprite has under assets/
    <id>-vN.png                    a kept variant: one drawing of a frame, at the frame's resolution
    variants.jsonl                 per variant: frame, box, score 0-5, used | candidate
  <family path>/prompting.md       what wording worked and what failed for a family, citing variants
  _frames/<frame>.json             the record of every frame a kept variant came from, and its parents'
  _inputs/<sha>.<ext>              the pictures those frames were asked from
  _spend.jsonl                     every billed call, kept or not: frame, model, cost, the cells it asked
  legacy.txt                       images under assets/ that trace to nothing yet

assets/<path>/<id>.png             the sprite, and <id>.src.json beside it: the variant it was made from, its size
assets/<path>/<id>.mesh.json       of a render of a model, the model as the page draws it live (GAM-10): its variant,
assets/<path>/<id>.mesh.bin        its looks and light; its triangles; written by `use` with the textures it wears
assets/textures/<texture>.webp     each as a face wears it, inset and made seamless, its .src.json naming its variant
```

`qq sprites trace <id>` prints the chain from a sprite to its first prompt; `qq sprites cost <id>` what it cost — all time
(its share of every frame that asked for it, and a render's textures', retries priced apart), its current variant's
alone, and which textures it shares with other models — and `qq sprites cost` every installed sprite's, the reusable
textures and the project's whole spend.

Every asset is a model (GAM-13, `P0`; the [shapegen](../.claude/skills/shapegen/SKILL.md) skill): a few textured shapes
rendered by `qq shapes` from the game's camera. Its textures are swatches generated, cut and kept like any drawing,
under `raw_assets/textures/`, and never installed themselves; the kept render is a variant whose record names its
model and the texture variants it wore where a cut names its frame. A small thing that stands on more than one model —
a jug, a motor — is a part: a model of its own, kept under `raw_assets/parts/` and placed by each model that has it.

```
raw_assets/textures/<id>/<id>-vN.png          a kept swatch, with variants.jsonl, as any variant
raw_assets/parts/<id>/<id>-vN.model.json      a kept part, and <id>-vN.png its picture; never installed
raw_assets/<path>/<id>/<id>-vN.png            a kept render
raw_assets/<path>/<id>/<id>-vN.model.json     the model it was rendered from, as it was
.tmp/shapes/<id>.json, <id>/<view>.png        a draft model and its views, scratch
```

A file under `assets/` that was not generated — a font — carries a `.src.json` too, naming where it was downloaded
from (address, commit, hash) and its licence, kept beside it.

## Rules

1. **Every image under `assets/` has a `.src.json` beside it or is on `legacy.txt`.** `qq sprites check` (inside
   `qq checks`) fails otherwise. Nothing is ever added to the legacy list.
2. **A sheet is never committed; its kept drawings are**, with the frame's record and inputs (`qq sprites keep`).
3. **What is kept is never edited or renamed.** A new attempt is a new version; a variant a `.src.json` names is never
   deleted.
4. **Every frame says which asset each drawing is**: its record lists the ids in the brief's order (remotegen
   `--cells`), and `cut` matches the drawings to them in reading order.
5. **Each kept variant gets its score when it is judged**, and the lesson of a set goes into its family's
   `prompting.md` in the same change. That file is read before the family's next brief.
6. **A cut is reproducible**: the same frame and record give the same variant, and `use` the same sprite.
7. **A render is reproducible**: its kept model, its kept textures, and the view and size its record names give the
   same variant. A model is kept only when every texture it wears and every part it places is kept.
8. **Every billed call is on `_spend.jsonl`**, written as it is billed and never edited: an attempt nothing was kept
   from is a cost too. `qq sprites check` fails on a kept frame the ledger lacks.
9. **What is kept is used before anything is generated.** `qq shapes library` lists the kept textures and parts; a
   model wears and places them wherever they are the same thing in the same role. remotegen refuses, before billing,
   a cell already kept, but for its own sheet's retry or `--mask` redo; another generation of it is the owner's word
   (`--again`).
