# Device interfaces — what the wording did

**Retired.** These panels stretched to their windows; GAM-14 replaced them with the console kit's housings
(`raw_assets/app/web/kit/`), one a paint, read off these panels' colours. Kept for what each wording did.

Briefs: `.tmp/gen/briefs/ui_*.txt`. `ui_a` is asked with the devices' style picture; `ui_b` to `ui_f` with a style
picture of four `ui_a` panels and "match its panel layout".

- **v1 drew each machine's controls** — dials, gauges, toggles, valves, screens — in a top strip. The owner ruled them
  out: no control that does nothing (GAM-11). Unused.
- **v2 is a plain housing** (score 4, all 54): "a thick heavy-duty outer frame in that machine's own paint and
  materials, bolted at the corners; a narrow band along the top holding only a blank riveted nameplate at its left;
  below it one large plain flat recessed face of dark grey steel, empty", then the long list "Draw NO controls of any
  kind: no buttons, no dials, no gauges, no switches, no levers, no knobs, no valves, no wheels, no lamps, no screens,
  no sight glasses, no pictograms, no meters. Red appears nowhere." Not one control came back.
- **v3 is the same housing, compact and kept** (`cui_a` from the devices' style picture, `cui_b`–`cui_f` from
  `ui_style_v3.png` with "Match image 1's panel layout, frame thickness and nameplate band exactly"; score 4, all 54):
  "a sturdy outer frame about a twelfth of the panel's width… a band along the top about a fifth of the panel's
  height", "light wear", "empty and clean". No control came back.
- **v4 adds a key bay, drawn to a layout guide, and is kept** (`tui_a`–`tui_f`, score 4, all 54, each sheet first
  time): the window's help and close keys had nowhere drawn to sit. Image 1 is a 3×3 guide in flat grey blocks
  (`raw_assets/_inputs/eefd46f5a5d484d4.png`), "take from it exactly the grid, each panel's outline and proportions…
  and the position and size of the nameplate and of the key bay. Take none of its flat grey colours"; image 2 is that
  sheet's nine v3 panels laid in the same grid, "keep each panel's own paint, materials, trim… and change only its
  layout". The bay: "a small recessed dark steel bay holding two empty square sockets side by side… nothing in them,
  no button caps, no symbols". Paint, trim and stripes came back panel for panel; no control came back.
- The guide's layout, which the stylesheet slices by: the top band 29% of the height, the frame 8.5% at each side and
  14% at the foot; the nameplate from 12% to 44% across, 6% to 23% down; the bay from 70.5% to 89.5% across, 5% to
  24% down, two sockets 7% wide in it. The model drifts the bay by up to 2% of the width (~8 px), too far for a key
  to sit in a socket by a fixed offset, so a tool (since retired) measured every panel's bay beside them. On
  dark or striped bands its box can sit 3–5 px off vertically (`ui_any_solarstrip`, `ui_ore_tether`); on the thin-rim
  `tui_c` panels it boxes the two sockets rather than the rim, which centres the keys the same.
