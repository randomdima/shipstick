# Walls and doors as trim — what the wording did

**None of these is in use.** A wall and a door became 1×1 devices on the floor's edge cells (GAM-10, SHP-7), drawn
as blocks under `raw_assets/devices/` (`any_wall*`, `any_door*`; [../../devices/prompting.md](../../devices/prompting.md)).
What follows is what drew walls as thin trim round a floor: `walls_a-v1` (score 5), earlier `dev_f` and `cdev_f`.

- **v1, "a wall running toward the camera", failed**: side walls and side doors came out facing the camera, and the
  four "outer corners" as one inward V four times (score 2, unused).
- **Say what the camera sees of each wall, once, before the cells**: "looking toward the back of the room. So a
  wall's top edge always shows as a thick dark yellow cap; the back wall also shows its inner face toward the camera,
  foreshortened; the side walls and the front wall show only their top cap and no face". Back, side and front pieces
  then came out as three different views of one wall.
- **A door is one cell** when said so: "A door is one cell wide: a single heavy door a person walks through", and
  "1 cell wide, as tall as the back wall". A side or front door "seen from above: the wall's cap broken by a heavy
  hazard-striped door frame, the closed slab's top a thick steel bar across the gap"; open, "the gap between the frame
  posts empty".
- **Corners by which caps meet**: "the back wall's left end, its top cap turning down toward the camera into a side
  wall's cap, an L shape"; "a side wall's cap coming down from the top meeting the front wall's cap going right".
- A wall of the operator's things came out by naming them: a padded jacket on a hook, a taped-up photo, a fold-down
  shelf with a mug.
- **The pieces do not quite share a scale**, so the stylesheet fits them: installed at 96 px on the longest side, the
  back wall is 64 px high, a side cap 22 px wide and the front cap 21 px; a back corner's face is 54 px and its cap 19
  px, so it is drawn 1.185 times larger; a front corner's caps are 18 and 24 px, so it is stretched to meet both.
- Doors in the back wall (`door_h_*`) are kept under `devices/`, every other piece here.
