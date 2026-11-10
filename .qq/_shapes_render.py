"""
How `qq shapes` draws a model: orthographic and z-buffered, each pixel its face's texture sampled bilinearly, then lit
in a pass of its own from what every pixel shows — its colour, normal and depth. Deterministic: the same model and
textures give the same picture.

`sun` light is what a sprite is kept with, drawn the way the game's drawings are: each face lit by its normal; shadowed
where the sun is blocked (a shadow map cast from the sun); darkened where nearer surfaces crowd it (ambient occlusion
read off the depth buffer); a dark line where one surface passes in front of another or ends against nothing, and a
light one along a convex fold turned to the sun. A model with `boundsM` stands on a deck nothing draws but its
shadows: inside the footprint they fall as translucent dark, so a sprite stands on the game's floor rather than
floating over it. `plain` is the faces lit by their normals alone; `flat` is the textures as they are.

The game draws its floor with these passes and these constants (src/app/web/wwwroot/scene.js), which reach it in
each installed `.mesh.json` (_shapes_mesh.light): change one and `qq sprites use` the devices again.
"""

from __future__ import annotations

import math

import _shapes

#: Edges are antialiased by rendering this many times larger and averaging down.
SUPERSAMPLE = 3
#: A triangle's texture is a blend of the two mipmap levels either side of its texel size; nearer the finer than this
#: share, the finer alone, which the eye does not tell apart and costs one lookup less.
LEVEL_BLEND_MIN = 0.1
#: Of the shadow map: its pixels a metre, a depth margin, and how far a surface point is lifted along its normal
#: before it is looked up — together more than a decal's 1–5 mm, so a decal never shadows its own face.
SHADOW_PX_M = 400
SHADOW_BIAS_M = 0.004
SHADOW_LIFT_M = 0.006
#: Of the sun's light, the share a shadowed face still gets — sky and what the room throws back.
SHADOW_KEEP = 0.35
#: Ambient occlusion: the rings round each pixel it looks in, the directions on each ring, how much nearer than its own
#: surface's plane a neighbour must stand to count, and the darkest it makes a pixel.
AO_RADII_M = (0.02, 0.06)
AO_DIRECTIONS = 8
AO_MARGIN_M = 0.003
AO_STRENGTH = 0.5
#: A neighbour this much nearer than a pixel's own plane is a surface passing in front: the line is drawn on the far
#: side, this dark, one output pixel wide.
EDGE_M = 0.015
EDGE_SHADE = 0.6
#: Two neighbours whose normals are further apart than this cosine are a fold; a convex one is lit along the side the
#: sun favours, this much.
FOLD_COS = 0.6
FOLD_LIGHT = 1.2
#: A face seen this edge-on or more is treated as seen at this cosine, so its plane's slope stays finite.
GRAZE_COS = 0.15
#: On the deck: the deepest a shadow falls (as alpha), and the fade toward the footprint's edge, where the next cell's
#: floor begins.
DECK_SHADOW_MAX = 0.6
DECK_FADE_M = 0.06
#: Of `parts` light: the hues its parts take, as a share of the colour wheel, red left out for the alert colour —
#: a part in an overlap or floating — and the least of a part that must show, in output pixels, to be numbered.
PARTS_HUE_FROM, PARTS_HUE_TO = 0.08, 0.92
PARTS_ALERT = (1.0, 0.12, 0.12)
PARTS_LABEL_MIN_PX = 60


def render_all(triangles: dict, model: dict, views: dict[str, tuple[float, float]], cell_px: int, light: str,
               workers: int = 1, alert=frozenset()) -> dict:
    """
    Each of `views`, by name, as `render` draws it: the sun's shadow map built once for all of them, and the views
    drawn in up to `workers` processes.
    """
    shadow = shadow_map(triangles, model) if light == "sun" else None
    if workers <= 1 or len(views) <= 1:
        return {name: render(triangles, model, angles, cell_px, light, shadow, alert)
                for name, angles in views.items()}
    from concurrent.futures import ProcessPoolExecutor

    with ProcessPoolExecutor(min(workers, len(views))) as pool:
        futures = {name: pool.submit(render, triangles, model, angles, cell_px, light, shadow, alert)
                   for name, angles in views.items()}
        return {name: future.result() for name, future in futures.items()}


def render(triangles: dict, model: dict, angles: tuple[float, float], cell_px: int, light: str, shadow=None,
           alert=frozenset()):
    """
    One view from (azimuth, elevation) as in `_shapes.VIEWS`. Framed on the model's `boundsM` when it has one, so every
    view of a kit keeps one frame, with a margin — none when its `frame` is `exact`; else cropped to what is drawn. `shadow` is the model's `shadow_map`, built here
    when not given. `parts` light draws each part in a colour of its own, numbered by its order, the parts in `alert`
    red.

    <remarks>The picture's `info["screen"]` places it: the camera's `right` and `up` in model space, its pixels a
    metre, and the screen point (x0, y0) in metres at its top-left corner, x along `right` and y down `up`.</remarks>
    """
    import numpy as np
    from PIL import Image

    azimuth, elevation = (math.radians(d) for d in angles)
    toward = np.array([math.cos(elevation) * math.sin(azimuth), -math.cos(elevation) * math.cos(azimuth),
                       math.sin(elevation)])
    right = np.array([math.cos(azimuth), math.sin(azimuth), 0.0])
    up = np.cross(toward, right)
    camera = {"toward": toward, "right": right, "up": up}

    P, N, UV, look, order = (triangles[k] for k in ("P", "N", "UV", "look", "order"))
    facing = (N @ toward).max(axis=1) > 0
    P, N, UV, look, order = P[facing], N[facing], UV[facing], look[facing], order[facing]
    sx, sy, depth = P @ right, -(P @ up), P @ toward + (order * _shapes.TIE_M)[:, None]

    frame = _shapes.bounds(model)
    if frame:
        lo, hi = frame
        corners = np.array([[x, y, z] for x in (lo[0], hi[0]) for y in (lo[1], hi[1]) for z in (lo[2], hi[2])])
        fx, fy = corners @ right, -(corners @ up)
    else:
        fx, fy = sx, sy
    scale = cell_px * SUPERSAMPLE
    pad = 2 * SUPERSAMPLE
    width = math.ceil((fx.max() - fx.min()) * scale / SUPERSAMPLE + 4) * SUPERSAMPLE
    height = math.ceil((fy.max() - fy.min()) * scale / SUPERSAMPLE + 4) * SUPERSAMPLE
    X = (sx - fx.min()) * scale + pad
    Y = (sy - fy.min()) * scale + pad
    camera |= {"scale": scale, "origin": (fx.min() - pad / scale, fy.min() - pad / scale)}

    buffers = {"albedo": np.zeros((height, width, 3), np.float32), "alpha": np.zeros((height, width), np.float32),
               "depth": np.full((height, width), -np.inf), "normal": np.zeros((height, width, 3), np.float32),
               "part": np.full((height, width), -1, np.int32)}
    textures = {}
    for t in np.argsort(look, kind="stable"):
        style = triangles["looks"][look[t]]
        key = (style["tex"], style["turn"])
        if key not in textures:
            textures[key] = mipmaps(_shapes.turned(model, *key))
        draw_triangle(X[t], Y[t], depth[t], N[t], UV[t], style, textures[key], buffers, order[t])

    if light == "parts":
        buffers["albedo"] = part_colours(len(triangles["labels"]), alert)[buffers["part"]]
    colour, alpha = buffers["albedo"], buffers["alpha"]
    if light == "sun" and shadow is None:
        shadow = shadow_map(triangles, model)
    if light != "flat":
        sun = np.array(_shapes.LIGHT) / np.linalg.norm(_shapes.LIGHT)
        colour, alpha = lit(buffers, camera, sun, frame if light == "sun" else None, shadow)

    # Averaged down premultiplied, so an edge fades to transparent rather than to black.
    h, w = height // SUPERSAMPLE, width // SUPERSAMPLE
    a = alpha.reshape(h, SUPERSAMPLE, w, SUPERSAMPLE).mean(axis=(1, 3))
    c = (colour * alpha[..., None]).reshape(h, SUPERSAMPLE, w, SUPERSAMPLE, 3).mean(axis=(1, 3))
    c = np.where(a[..., None] > 0, c / np.maximum(a[..., None], 1e-6), 0)
    picture = Image.fromarray((np.dstack([c, a]).clip(0, 1) * 255).round().astype(np.uint8), "RGBA")
    if light == "parts":
        label_parts(picture, buffers["part"])
    crop = (0, 0)
    if not frame:
        box = picture.getchannel("A").getbbox()
        crop = box[:2]
        picture = picture.crop(box)
    elif model.get("frame") == "exact":
        # The margin goes, and with it the outline drawn where the buffer cuts off what runs on past the frame.
        crop = (pad // SUPERSAMPLE,) * 2
        picture = picture.crop((*crop, crop[0] + round((fx.max() - fx.min()) * cell_px),
                                crop[1] + round((fy.max() - fy.min()) * cell_px)))
    picture.info["screen"] = {"right": right.round(9).tolist(), "up": up.round(9).tolist(), "pxM": cell_px,
                              "x0": float(fx.min() - 2 / cell_px + crop[0] / cell_px),
                              "y0": float(fy.min() - 2 / cell_px + crop[1] / cell_px)}
    return picture


def part_colours(count: int, alert) -> "np.ndarray":
    """
    A colour for each part, and one past them for nothing: hues a golden angle apart, none of them red, which is kept
    for the parts in `alert` — those in an overlap or floating.
    """
    import colorsys

    import numpy as np

    colours = []
    for k in range(count):
        if k in alert:
            colours.append(PARTS_ALERT)
            continue
        hue = (PARTS_HUE_FROM + (k * 0.381966) % 1 * (PARTS_HUE_TO - PARTS_HUE_FROM)) % 1
        colours.append(colorsys.hsv_to_rgb(hue, 0.45 + 0.2 * (k % 2), 0.95 - 0.15 * (k % 3)))
    return np.array([*colours, (0, 0, 0)], np.float32)


def label_parts(picture, part) -> None:
    """Each part's number written at the middle of what shows of it, if enough shows to read."""
    import numpy as np
    from PIL import ImageDraw

    draw = ImageDraw.Draw(picture)
    seen = part >= 0
    rows, cols = np.nonzero(seen)
    ids = part[seen]
    counts = np.bincount(ids)
    sum_x, sum_y = np.bincount(ids, cols), np.bincount(ids, rows)
    for k in np.nonzero(counts >= PARTS_LABEL_MIN_PX * SUPERSAMPLE ** 2)[0]:
        x, y = sum_x[k] / counts[k] / SUPERSAMPLE, sum_y[k] / counts[k] / SUPERSAMPLE
        draw.text((x, y), str(k), fill=(0, 0, 0, 255), anchor="mm", stroke_width=2, stroke_fill=(255, 255, 255, 255))


def lit(buffers, camera, sun, frame, shadow):
    """
    The colour and alpha of every pixel lit: by normal alone, or, given the `shadow_map`, with shadows, occlusion,
    edges and the deck.
    """
    import numpy as np

    solid = buffers["alpha"] > 0
    # Nothing's depth is far behind everything rather than -inf, so a difference of two is never nan.
    depth = np.where(solid, buffers["depth"], -1e3)
    normal = buffers["normal"].copy()
    deck = np.zeros_like(solid)
    if frame is not None and camera["toward"][2] > 0:
        deck, deck_depth, fade = deck_under(solid, camera, frame)
        depth[deck], normal[deck] = deck_depth[deck], (0, 0, 1)
    seen = solid | deck
    facing_sun = np.maximum(normal @ sun, 0)
    if shadow is None:
        light = _shapes.AMBIENT + (1 - _shapes.AMBIENT) * facing_sun
        return buffers["albedo"] * light[..., None], buffers["alpha"]

    world = positions(depth, camera)
    sunlit = np.ones(depth.shape, np.float32)
    sunlit[seen] = sun_reaches(shadow, world[seen] + normal[seen] * SHADOW_LIFT_M)
    slope = plane_slope(normal, camera)
    ao = occlusion(depth, slope, seen, camera["scale"])
    light = (_shapes.AMBIENT + (1 - _shapes.AMBIENT) * facing_sun * (SHADOW_KEEP + (1 - SHADOW_KEEP) * sunlit)) * ao
    colour = buffers["albedo"] * (light * edges(depth, normal, slope, solid, sun))[..., None]

    alpha = buffers["alpha"].copy()
    if deck.any():
        open_deck = _shapes.AMBIENT + (1 - _shapes.AMBIENT) * sun[2]
        dark = np.clip(1 - light / open_deck, 0, 1) * DECK_SHADOW_MAX * fade
        alpha[deck] = dark[deck]
        colour[deck] = 0
    return colour, alpha


def deck_under(solid, camera, frame):
    """The pixels where the floor of the footprint shows past the model, the floor's depth there, and its edge fade."""
    import numpy as np

    lo, hi = frame
    base = positions(np.zeros(solid.shape), camera)
    along = (lo[2] - base[..., 2]) / camera["toward"][2]
    floor = base + along[..., None] * camera["toward"]
    inside = np.minimum.reduce([floor[..., 0] - lo[0], hi[0] - floor[..., 0], floor[..., 1] - lo[1], hi[1] - floor[..., 1]])
    return (inside >= 0) & ~solid, along, np.clip(inside / DECK_FADE_M, 0, 1)


def positions(depth, camera):
    """Each pixel's point in model space, from where it lies on the picture and its depth."""
    import numpy as np

    height, width = depth.shape
    sx = (np.arange(width) + 0.5) / camera["scale"] + camera["origin"][0]
    sy = (np.arange(height) + 0.5) / camera["scale"] + camera["origin"][1]
    finite = np.where(np.isfinite(depth), depth, 0)
    return (sx[None, :, None] * camera["right"] - sy[:, None, None] * camera["up"]
            + finite[..., None] * camera["toward"])


def shadow_map(triangles, model) -> dict:
    """
    The model as the sun sees it: of each cell, the nearest surface toward the sun. It depends on no camera, so every
    view of a render shares one. A cutout face casts only where its picture is solid, as it is drawn.
    """
    import numpy as np

    sun = np.array(_shapes.LIGHT) / np.linalg.norm(_shapes.LIGHT)
    P, UV = triangles["P"], triangles["UV"]
    pictures = {}
    across = np.cross([0.0, 0.0, 1.0], sun)
    across /= np.linalg.norm(across)
    along = np.cross(sun, across)
    flat = P.reshape(-1, 3)
    low = np.array([flat @ across, flat @ along]).min(axis=1) - 2 / SHADOW_PX_M
    high = np.array([flat @ across, flat @ along]).max(axis=1) + 2 / SHADOW_PX_M
    size = np.ceil((high - low) * SHADOW_PX_M).astype(int) + 1
    nearest = np.full((size[1], size[0]), -np.inf)
    X, Y, Z = (P @ across - low[0]) * SHADOW_PX_M, (P @ along - low[1]) * SHADOW_PX_M, P @ sun
    for t in range(len(P)):
        region, hit, w = covered(X[t], Y[t], nearest.shape)
        if hit is None:
            continue
        style = triangles["looks"][triangles["look"][t]]
        if style["cutout"]:
            key = (style["tex"], style["turn"])
            if key not in pictures:
                pictures[key] = _shapes.turned(model, *key)
            u = (w[0] * UV[t, 0, 0] + w[1] * UV[t, 1, 0] + w[2] * UV[t, 2, 0])[hit]
            v = (w[0] * UV[t, 0, 1] + w[1] * UV[t, 1, 1] + w[2] * UV[t, 2, 1])[hit]
            hit[hit] = sample(pictures[key], u, v, wrap=style["tileM"] is not None)[:, 3] >= _shapes.CUTOUT_ALPHA
        z = w[0] * Z[t, 0] + w[1] * Z[t, 1] + w[2] * Z[t, 2]
        window = nearest[region]
        window[hit] = np.maximum(window[hit], z[hit])
    return {"sun": sun, "across": across, "along": along, "low": low, "nearest": nearest}


def sun_reaches(shadow: dict, points):
    """Of each point, the share of a 3×3 patch of the sun's shadow map with nothing nearer the sun than it."""
    import numpy as np

    across, along, low, nearest, sun = (shadow[k] for k in ("across", "along", "low", "nearest", "sun"))
    size = nearest.shape[::-1]
    qx = np.floor((points @ across - low[0]) * SHADOW_PX_M).astype(int)
    qy = np.floor((points @ along - low[1]) * SHADOW_PX_M).astype(int)
    qz = points @ sun + SHADOW_BIAS_M
    reached = np.zeros(len(points), np.float32)
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            iy, ix = np.clip(qy + dy, 0, size[1] - 1), np.clip(qx + dx, 0, size[0] - 1)
            reached += nearest[iy, ix] <= qz
    return reached / 9


def plane_slope(normal, camera):
    """How far a pixel's own surface moves in depth a pixel right and a pixel down: (d/dx, d/dy), each per pixel."""
    import numpy as np

    facing = np.maximum(normal @ camera["toward"], GRAZE_COS)
    return -(normal @ camera["right"]) / facing / camera["scale"], (normal @ camera["up"]) / facing / camera["scale"]


def shifted(image, dx: int, dy: int, fill):
    """out[y, x] is image[y + dy, x + dx], or `fill` past its edge."""
    import numpy as np

    out = np.full_like(image, fill)
    h, w = image.shape[:2]
    if abs(dx) >= w or abs(dy) >= h:
        return out
    out[max(-dy, 0):h - max(dy, 0), max(-dx, 0):w - max(dx, 0)] = \
        image[max(dy, 0):h - max(-dy, 0), max(dx, 0):w - max(-dx, 0)]
    return out


def occlusion(depth, slope, seen, scale):
    """1 where a pixel is open to the room, down to 1 - AO_STRENGTH where neighbours stand up round it."""
    import numpy as np

    blocked = np.zeros(depth.shape, np.float32)
    samples = 0
    for radius in AO_RADII_M:
        for k in range(AO_DIRECTIONS):
            angle = 2 * math.pi * (k + 0.5 * (radius == AO_RADII_M[-1])) / AO_DIRECTIONS
            dx, dy = round(math.cos(angle) * radius * scale), round(math.sin(angle) * radius * scale)
            rise = shifted(depth, dx, dy, -np.inf) - (depth + slope[0] * dx + slope[1] * dy)
            blocked += np.clip((rise - AO_MARGIN_M) / radius, 0, 1)
            samples += 1
    return np.where(seen, 1 - AO_STRENGTH * blocked / samples, 1)


def edges(depth, normal, slope, solid, sun):
    """A multiplier: EDGE_SHADE on the far side of an outline, FOLD_LIGHT along a convex fold's sunward side."""
    import numpy as np

    step = SUPERSAMPLE
    outline = np.zeros(depth.shape, bool)
    fold = np.zeros(depth.shape, bool)
    toward_sun = normal @ sun
    for dx, dy in ((step, 0), (-step, 0), (0, step), (0, -step)):
        other = shifted(solid, dx, dy, False)
        rise = shifted(depth, dx, dy, -np.inf) - (depth + slope[0] * dx + slope[1] * dy)
        outline |= solid & (~other | (rise > EDGE_M))
        bend = (normal * shifted(normal, dx, dy, 0)).sum(axis=-1)
        fold |= (solid & other & (bend < FOLD_COS) & (rise < 0) & (rise > -EDGE_M)
                 & (toward_sun > shifted(toward_sun, dx, dy, 0)))
    return np.where(outline, EDGE_SHADE, np.where(fold, FOLD_LIGHT, 1.0))


def mipmaps(picture) -> list:
    """The picture and each half of it down to a pixel, every level the 2×2 average of the one before."""
    levels = [picture]
    while min(levels[-1].shape[:2]) > 1:
        p = levels[-1]
        h, w = p.shape[0] // 2 * 2, p.shape[1] // 2 * 2
        levels.append(p[:h, :w].reshape(h // 2, 2, w // 2, 2, 4).mean(axis=(1, 3)))
    return levels


def covered(X, Y, shape):
    """The pixel window round a triangle, which of its pixels' centres it covers, and their barycentric weights."""
    import numpy as np

    height, width = shape
    left, right = max(int(X.min()), 0), min(int(math.ceil(X.max())), width - 1)
    top, bottom = max(int(Y.min()), 0), min(int(math.ceil(Y.max())), height - 1)
    area = (X[1] - X[0]) * (Y[2] - Y[0]) - (X[2] - X[0]) * (Y[1] - Y[0])
    if left > right or top > bottom or abs(area) < 1e-9:
        return None, None, None
    px, py = np.meshgrid(np.arange(left, right + 1) + 0.5, np.arange(top, bottom + 1) + 0.5)
    w0 = ((X[1] - px) * (Y[2] - py) - (X[2] - px) * (Y[1] - py)) / area
    w1 = ((X[2] - px) * (Y[0] - py) - (X[0] - px) * (Y[2] - py)) / area
    w2 = 1 - w0 - w1
    hit = (w0 >= -1e-6) & (w1 >= -1e-6) & (w2 >= -1e-6)
    if not hit.any():
        return None, None, None
    return (slice(top, bottom + 1), slice(left, right + 1)), hit, (w0, w1, w2)


def draw_triangle(X, Y, Z, N, UV, style, levels, buffers, part: int) -> None:
    import numpy as np

    region, hit, w = covered(X, Y, buffers["alpha"].shape)
    if hit is None:
        return
    z = w[0] * Z[0] + w[1] * Z[1] + w[2] * Z[2]
    window = buffers["depth"][region]
    hit &= z > window
    if not hit.any():
        return
    w0, w1, w2, z = w[0][hit], w[1][hit], w[2][hit], z[hit]
    # Orthographic, so a triangle's texture lies on it by one affine map: one blend of the two levels either side of a
    # texel to a (supersampled) pixel serves the whole of it.
    h0, wd0 = levels[0].shape[:2]
    area = abs((X[1] - X[0]) * (Y[2] - Y[0]) - (X[2] - X[0]) * (Y[1] - Y[0]))
    texels = abs((UV[1, 0] - UV[0, 0]) * (UV[2, 1] - UV[0, 1]) - (UV[2, 0] - UV[0, 0]) * (UV[1, 1] - UV[0, 1])) * h0 * wd0
    level = min(max(math.log2(max(texels / area, 1e-12)) / 2, 0), len(levels) - 1)
    u = w0 * UV[0, 0] + w1 * UV[1, 0] + w2 * UV[2, 0]
    v = w0 * UV[0, 1] + w1 * UV[1, 1] + w2 * UV[2, 1]
    wrap = style["tileM"] is not None
    finer, coarser = int(level), min(int(level) + 1, len(levels) - 1)
    texel = sample(levels[finer], u, v, wrap)
    if (blend := level - finer) > LEVEL_BLEND_MIN and coarser != finer:
        texel = texel * (1 - blend) + sample(levels[coarser], u, v, wrap) * blend
    if style["cutout"]:
        keep = texel[:, 3] >= _shapes.CUTOUT_ALPHA
        if not keep.any():
            return
        rows, cols = np.nonzero(hit)
        hit = np.zeros_like(hit)
        hit[rows[keep], cols[keep]] = True
        w0, w1, w2, z, texel = w0[keep], w1[keep], w2[keep], z[keep], texel[keep]
    normal = w0[:, None] * N[0] + w1[:, None] * N[1] + w2[:, None] * N[2]
    normal /= np.maximum(np.linalg.norm(normal, axis=1, keepdims=True), 1e-9)
    buffers["albedo"][region][hit] = texel[:, :3] * style["shade"]
    buffers["normal"][region][hit] = normal
    buffers["alpha"][region][hit] = 1
    buffers["part"][region][hit] = part
    window[hit] = z


def sample(texture, u, v, wrap: bool):
    """Bilinear; a tiled texture wraps at its edges, a fitted one holds its edge."""
    import numpy as np

    h, w = texture.shape[:2]
    x, y = u * w - 0.5, v * h - 0.5
    x0, y0 = np.floor(x).astype(int), np.floor(y).astype(int)
    fx, fy = (x - x0)[:, None], (y - y0)[:, None]
    if wrap:
        x0, y0 = x0 % w, y0 % h
        x1, y1 = (x0 + 1) % w, (y0 + 1) % h
    else:
        x0, x1 = np.clip(x0, 0, w - 1), np.clip(x0 + 1, 0, w - 1)
        y0, y1 = np.clip(y0, 0, h - 1), np.clip(y0 + 1, 0, h - 1)
    return (texture[y0, x0] * (1 - fx) * (1 - fy) + texture[y0, x1] * fx * (1 - fy)
            + texture[y1, x0] * (1 - fx) * fy + texture[y1, x1] * fx * fy)
