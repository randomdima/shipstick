// The ship's floor in 3D (GAM-10, GAM-13): every deck plate, wall, door and device a textured model in one scene,
// drawn live in WebGL2 with the renderer's passes (.qq/_shapes_render.py) — sun, shadow map, occlusion, outlines —
// from a camera the player turns, tilts and zooms (cabin.js) round the middle of the view. A device is its
// model as `qq sprites use` wrote it (assets/<path>/<id>.mesh.json, .qq/_shapes_mesh.py), or the plain crate stretched
// to its footprint until it has one; walls and doors are the kit's caps and panels on blocks a cell square; the deck is
// its plates. What the pointer is over is read back from the picture (`pick`); where a thing stands on the page comes
// from the camera (`rectOf`, `pointOf`), for the windows and their leaders.
//
// A model's live parts (`live` in its .mesh.json, .qq/_shapes.py LIVE) show their device as it runs (`setLive`, WEB-12): a
// lamp lights, a screen glows, a needle swings, a bar fills, a fan turns, an arm travels to and fro. While one moves the scene is drawn every
// display frame (WEB-11), its costly passes only over what moved.
//
// World space is the ship's, in metres, a cell a metre: x east from its west edge, y north from its north edge (so
// every row is below 0), z up from the deck.

// The camera's field of view, up the picture; the capsule it is fitted to fills this share of the shorter side.
const FOV_DEG = 35;
const FIT = 1 / .9;
// Its tilt from the horizon: the device camera's 18° from straight down to start; the player's range.
export const PITCH = { start: 72, least: 30, most: 89.5 };
// How near it comes, as a share of the fitted distance's reciprocal: 1 fits a capsule; out to a few, in to a device.
export const ZOOM = { start: 1, least: .35, most: 5 };
// A wall stands in courses, each one panel of the kit high, and its fitting (a vent, a porthole) only on the top one;
// how far each piece of the kit lies off what it covers.
const WALL_COURSE_M = .5;
const WALL_COURSES = 3;
export const WALL_HIGH_M = WALL_COURSE_M * WALL_COURSES;
const LAID_M = .003;
// The kit's pieces and the deck's tiles are cut with a dark fringe: this share of each edge is left off.
const JOIN_INSET = (1 - 1 / 1.04) / 2;
const DECK_INSET = (1 - 1 / 1.12) / 2;
// The deck and the caps are drawn darker than they are lit; a fogged capsule darker still.
const DECK_TONE = .85;
const CAP_TONE = .85;
const FOG_TONE = .4;
// A door is drawn wider than its picture, a broad bulkhead door, across this share of the cell; its lintel this share.
const LEAF_WIDE = .8;
const LINTEL_SPAN = .9;
// A pointed-at thing is drawn this much lighter; an open one ringed in amber this many output pixels wide.
const HOVER_LIGHT = 1.15;
const GLOW_PX = 2;
const AMBER = [.95, .66, .18];
// The most open things ringed at once.
const OPEN_MAX = 16;
// A later part in a model stands this much nearer the camera than the one before, so of two faces in one plane the
// later shows (the renderer's TIE_M, coarser for a depth buffer's precision: see `aim`'s near plane).
const ORDER_M = 3e-5;
// The shadow map's largest side, and what stands taller than a wall, for its extent.
const SHADOW_MAX_PX = 4096;
// The shadow map's pixels read round a point's own, each way: its shadow's edge is softened over them.
const SHADOW_KERNEL_PX = 1;
const TALLEST_M = 3;
// The stand-in for a device with no model of its own: the crate, stretched to its footprint.
const CRATE = 'assets/parts/any_crate.mesh.json';
// The live parts one model has at most: the shaders' arrays are this long (.qq/_shapes.py LIVE_MOST).
const LIVE_MAX = 12;
// How each way of showing draws its picture: as modelled (what turns), multiplied by its tone (a glow, a fill), or its
// coloured part — a lamp's lens, not its rim — in the tone's colour, as bright as the picture is there.
const MODE = { needle: 0, spin: 0, stroke: 0, glow: 1, fill: 1, lamp: 2 };
// What moves from where the sun's map has it casts no shadow if it is small (a needle, an arm) — a large one (a panel
// tracking the sun) casts the shadow of where it was modelled; what spins turns in its own outline.
const UNSHADOWED = new Set(['needle', 'stroke']);
const SHADOWED_FROM_M = .2;
const castsNone = e => UNSHADOWED.has(e.as) && Math.max(...e.boxM[1].map((v, i) => v - e.boxM[0][i])) < SHADOWED_FROM_M;
// A tone is [r, g, b, glow]. A lamp is green, amber for caution, red for a fault alone (docs/style.md), or dark; a glow
// and a fill's lit steps are their picture lit, the rest dimmed.
const LAMP = { running: [.42, 1, .5, 1], short: [...AMBER, 1], fault: [1, .25, .18, 1], off: [.2, .23, .21, 0] };
const LIT = [1, 1, 1, 1], DIMMED = [.3, .3, .3, 0];
// What glows is drawn this much brighter than its picture, unshaded, and lights the pixels round it this far and this
// much.
const GLOW_GAIN = 1.3;
const HALO_PX = 3;
const HALO = .45;
// A fault lamp blinks this many times a second; a needle swings at an even pace, this share of its sweep a second.
const BLINK_HZ = 1;
const NEEDLE_PER_S = .5;
// A partial draw is widened this far round what moved, for the outlines, occlusion and halo measured across it.
const MOVED_PAD_PX = 24;

const metas = new Map();      // mesh path → its .mesh.json
const meshes = new Map();     // mesh path → { meta, vao } once loaded, or a Promise
const textures = new Map();   // picture path → { texture, aspect } once loaded, or a Promise
let gl, shaders, samplers, canvas, light;
let scene = null;             // what setScene was last given, built: { key, things, statics, devices, extent }
let sun = null;               // the shadow map for scene.key
let targets = null;           // the pictures each pass draws into, at one size
const marks = { hover: 0, open: [] };
const view = { target: [0, 0, 0], yaw: 0, pitch: PITCH.start, zoom: ZOOM.start, cells: 10, matrix: null, inverse: null,
  eye: null };
// What each device's live parts show (setLive): its signals by inventory id, and the ship's clock; each needle's reading
// as shown and each spin's angle, by device and part, kept across scenes; when the last frame was drawn.
const live = { byId: new Map(), clock: () => ({ nowS: 0, rate: 0 }), shown: new Map(), lastMs: 0, moving: false };
// queued: a frame is asked for; whole: it must draw everything, not only what moved.
let queued = false, whole = true;

/** Reads every model the host serves (its .mesh.json alone; its triangles and textures load when first drawn). */
export async function loadScene(paths) {
  await Promise.all(paths.filter(p => p.endsWith('.mesh.json')).map(async p => metas.set(p, await (await fetch(p)).json())));
  light = metas.get(CRATE)?.light ?? metas.values().next().value?.light;
}

/** Whether this page can draw the floor: WebGL2, and the models' light. */
export const drawable = () => Boolean(light && context());

/** The floor's canvas, made once and kept: it follows its box's size. */
export function sceneCanvas() {
  if (canvas) return canvas;
  context();
  canvas = gl.canvas;
  canvas.className = 'scene';
  new ResizeObserver(() => {
    aim({});
    request();
  }).observe(canvas);
  return canvas;
}

function context() {
  if (gl !== undefined) return gl;
  gl = document.createElement('canvas').getContext('webgl2', { antialias: false, alpha: true, premultipliedAlpha: false }) ?? null;
  if (!gl) return gl;
  shaders = {
    gbuffer: program(G_VERTEX, G_FRAGMENT), sun: program(SUN_VERTEX, SUN_FRAGMENT),
    light: program(FULL_VERTEX, LIGHT_FRAGMENT), resolve: program(FULL_VERTEX, RESOLVE_FRAGMENT),
  };
  samplers = { true: sampler(gl.REPEAT), false: sampler(gl.CLAMP_TO_EDGE) };
  return gl;
}

/**
 * What the floor shows: `cells` of deck ({ column, row, src, deg, tint, fog, at }), `walls` ({ column, row, cap,
 * capDeg, faces: [{ side, src }], lintel, lintelAcross, leaf, id, at, title, fog }), `devices` ({ column, row,
 * columns, rows, mesh, id, at, title }), each at its ship cell, and `parts` ({ mesh, atM, turnDeg, id, at, title }), a
 * model set down at a point of the world turned clockwise; `id` is what a click opens, `at` the capsule it is in.
 * Built again only when it changed.
 */
export function setScene(description) {
  const key = JSON.stringify(description);
  if (scene?.key === key) return;
  const things = [null];
  const thing = (id, at, title, box) => things.push({ id, at, title, box }) - 1;
  const devices = description.devices.map(d => {
    const path = d.mesh ?? CRATE;
    const height = metas.get(path)?.boundsM[1][2] ?? 1;
    const offset = [d.column, -(d.row + d.rows), 0];
    const scale = d.mesh ? [1, 1, 1] : [d.columns, d.rows, 1];
    return { path, offset, scale, turn: turned(0), id: d.id,
      thing: thing(d.id, d.at, d.title, [offset, [d.column + d.columns, -d.row, height]]) };
  });
  for (const p of description.parts ?? []) {
    const meta = metas.get(p.mesh);
    if (!meta) continue;
    const turn = turned(p.turnDeg);
    const corners = cornersOf(meta.boundsM).map(c => apply(turn, c).map((v, i) => v + p.atM[i]));
    const box = [0, 1].map(end => [0, 1, 2].map(i => (end ? Math.max : Math.min)(...corners.map(c => c[i]))));
    devices.push({ path: p.mesh, offset: p.atM, scale: [1, 1, 1], turn, id: p.id, thing: thing(p.id, p.at, p.title, box) });
  }
  scene = { key, description, things, devices, statics: null, extent: extentOf(description) };
  scene.wallThings = description.walls.map(w => w.id != null || w.at
    ? thing(w.id, w.at, w.title, [[w.column, -(w.row + 1), 0], [w.column + 1, -w.row, WALL_HIGH_M]]) : 0);
  scene.cellThings = description.cells.map(c => c.at ? thing(null, c.at, '', [[c.column, -(c.row + 1), 0], [c.column + 1, -c.row, 0]]) : 0);
  sun = null;
  request();
}

const extentOf = ({ cells, walls }) => {
  const all = [...cells, ...walls];
  return [[Math.min(...all.map(c => c.column)), -Math.max(...all.map(c => c.row)) - 1, 0],
    [Math.max(...all.map(c => c.column)) + 1, -Math.min(...all.map(c => c.row)), TALLEST_M]];
};

/** What is pointed at — the `thing` `pick` named, lit — and what is `open`, by inventory id, ringed. */
export function setMarks({ hover = 0, open = [] }) {
  const ids = scene ? scene.things.flatMap((t, i) => t && t.id != null && open.includes(t.id) ? [i] : []) : [];
  const next = { hover, open: ids.slice(0, OPEN_MAX) };
  if (next.hover === marks.hover && `${next.open}` === `${marks.open}`) return;
  Object.assign(marks, next);
  request();
}

/**
 * What each thing's live parts show, by inventory id: `{ runs, last, short, cycleFromS, cycleS, input, output, held }`
 * — whether it runs a way, how its last cycle ended (a CycleOutcome), whether it is short of the next, when the cycle
 * under way began and how long it is, in ship seconds, and the shares 0–1 of what its slots hold at most. `clock()`
 * is the ship's `{ nowS, rate }`.
 */
export function setLive(byId, clock) {
  live.byId = byId;
  live.clock = clock;
  request();
}

/**
 * Aims the camera: at the ship's cell `column`, `row` (fractional, on the deck), from `yaw` degrees clockwise of north
 * and `pitch` above the horizon, as far off as fits `cells` in the view, `zoom` times nearer. What is left out is kept.
 */
export function aim({ column, row, yaw, pitch, zoom, cells }) {
  if (column != null) view.target = [column, -row, 0];
  if (yaw != null) view.yaw = yaw;
  if (pitch != null) view.pitch = Math.min(PITCH.most, Math.max(PITCH.least, pitch));
  if (zoom != null) view.zoom = Math.min(ZOOM.most, Math.max(ZOOM.least, zoom));
  if (cells != null) view.cells = cells;
  const w = canvas?.clientWidth || 1, h = canvas?.clientHeight || 1;
  const tan = Math.tan(FOV_DEG * Math.PI / 360), aspect = w / h;
  const distance = view.cells * FIT / 2 / tan / Math.min(1, aspect) / view.zoom;
  const yawR = view.yaw * Math.PI / 180, pitchR = view.pitch * Math.PI / 180;
  const ahead = [Math.sin(yawR), Math.cos(yawR), 0];
  view.eye = [view.target[0] - ahead[0] * Math.cos(pitchR) * distance, view.target[1] - ahead[1] * Math.cos(pitchR) * distance,
    Math.sin(pitchR) * distance];
  const reach = Math.hypot(...(scene ? scene.extent[1].map((v, i) => v - scene.extent[0][i]) : [30, 30, 3]));
  // As far out as nothing can stand nearer, for the depth buffer's precision: ORDER_M must stay above it.
  const near = Math.max(.5, (view.eye[2] - TALLEST_M) * Math.sin(pitchR) / 2), far = distance + reach;
  view.matrix = multiply(perspective(FOV_DEG * Math.PI / 180, aspect, near, far), lookAt(view.eye, view.target, [0, 0, 1]));
  view.inverse = invert(view.matrix);
  view.metresPerPx = 2 * distance * tan / h;
  view.ahead = ahead;
  view.right = [Math.cos(yawR), -Math.sin(yawR), 0];
  request();
}

/**
 * The camera as cabin.js keeps it: its yaw, pitch and zoom, and metres of deck a page pixel spans at the middle of the
 * view.
 */
export const camera = () => ({ yaw: view.yaw, pitch: view.pitch, zoom: view.zoom, metresPerPx: view.metresPerPx,
  ahead: view.ahead, right: view.right });

/** The point of the deck under a point of the page, as the ship's { column, row }; null where it meets no deck. */
export function deckAt(clientX, clientY) {
  if (!canvas || !view.inverse) return null;
  const r = canvas.getBoundingClientRect();
  const x = (clientX - r.left) / r.width * 2 - 1, y = 1 - (clientY - r.top) / r.height * 2;
  const unproject = z => {
    const m = view.inverse, v = [x, y, z, 1];
    const out = [0, 1, 2, 3].map(i => m[i] * v[0] + m[4 + i] * v[1] + m[8 + i] * v[2] + m[12 + i] * v[3]);
    return out.slice(0, 3).map(c => c / out[3]);
  };
  const near = unproject(-1), far = unproject(1);
  if (near[2] === far[2]) return null;
  const t = near[2] / (near[2] - far[2]);
  if (t < 0) return null;
  return { column: near[0] + (far[0] - near[0]) * t, row: -(near[1] + (far[1] - near[1]) * t) };
}

/** Where a point of the world is on the page, or null behind the camera. */
export function pointOf([x, y, z]) {
  if (!canvas || !view.matrix) return null;
  const m = view.matrix;
  const cw = m[3] * x + m[7] * y + m[11] * z + m[15];
  if (cw <= 0) return null;
  const cx = (m[0] * x + m[4] * y + m[8] * z + m[12]) / cw, cy = (m[1] * x + m[5] * y + m[9] * z + m[13]) / cw;
  const r = canvas.getBoundingClientRect();
  return { x: r.left + (cx * .5 + .5) * r.width, y: r.top + (.5 - cy * .5) * r.height };
}

/** The box on the page round what opens `id`, `{ left, right, top, bottom }`; null when nothing in view does. */
export function rectOf(id) {
  const boxes = scene?.things.filter(t => t && t.id === id).map(t => t.box) ?? [];
  const points = boxes.flatMap(box => cornersOf(box).map(pointOf)).filter(Boolean);
  if (!points.length) return null;
  const [left, right] = range(points.map(p => p.x)), [top, bottom] = range(points.map(p => p.y));
  return { left, right, top, bottom };
}

/** The eight corners of the box `[lo, hi]`. */
const cornersOf = ([lo, hi]) => [0, 1, 2, 3, 4, 5, 6, 7].map(i => [(i & 1 ? hi : lo)[0], (i & 2 ? hi : lo)[1], (i & 4 ? hi : lo)[2]]);

/** What is drawn at a point of the page: { id, at, title } of a thing, or null over the bare deck of fog or space. */
export function pick(clientX, clientY) {
  if (!targets || !scene) return null;
  const r = canvas.getBoundingClientRect();
  const x = Math.floor((clientX - r.left) / r.width * targets.size[0]);
  const y = Math.floor((1 - (clientY - r.top) / r.height) * targets.size[1]);
  if (x < 0 || y < 0 || x >= targets.size[0] || y >= targets.size[1]) return null;
  gl.bindFramebuffer(gl.READ_FRAMEBUFFER, targets.gbuffer);
  gl.readBuffer(gl.COLOR_ATTACHMENT2);
  const px = new Uint8Array(4);
  gl.readPixels(x, y, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, px);
  gl.bindFramebuffer(gl.READ_FRAMEBUFFER, null);
  const n = px[0] | px[1] << 8 | px[2] << 16;
  return n ? { thing: n, ...scene.things[n] } : null;
}

/**
 * Asks for a frame: of everything, or — `everything` false — of what moves alone, if nothing else asks for more. The
 * animation tick: while a live part moves, the frame after is asked for at once, whatever this one's draw did, so the
 * parts move every display frame (WEB-11) and stop asking once none moves; `setLive` starts it again.
 */
function request(everything = true) {
  whole ||= everything;
  if (queued) return;
  queued = true;
  requestAnimationFrame(ms => {
    queued = false;
    try {
      draw(ms);
    } finally {
      if (live.moving) request(false);
    }
  });
}

function sampler(wrap) {
  const s = gl.createSampler();
  gl.samplerParameteri(s, gl.TEXTURE_WRAP_S, wrap);
  gl.samplerParameteri(s, gl.TEXTURE_WRAP_T, wrap);
  gl.samplerParameteri(s, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR);
  gl.samplerParameteri(s, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
  return s;
}

function program(vertex, fragment) {
  const p = gl.createProgram();
  for (const [type, source] of [[gl.VERTEX_SHADER, vertex], [gl.FRAGMENT_SHADER, fragment]]) {
    const s = gl.createShader(type);
    gl.shaderSource(s, source);
    gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s));
    gl.attachShader(p, s);
  }
  gl.linkProgram(p);
  if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p));
  const uniforms = {};
  for (let i = 0; i < gl.getProgramParameter(p, gl.ACTIVE_UNIFORMS); i++) {
    const { name } = gl.getActiveUniform(p, i);
    uniforms[name.replace(/\[0\]$/, '')] = gl.getUniformLocation(p, name);
  }
  return { p, u: uniforms };
}

/** A picture as a texture, once; null until it has loaded, when the scene is drawn again. */
function textureOf(src) {
  const known = textures.get(src);
  if (known && !(known instanceof Promise)) return known;
  if (!known) textures.set(src, (async () => {
    const image = new Image();
    image.src = src;
    await image.decode();
    const t = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, t);
    gl.pixelStorei(gl.UNPACK_COLORSPACE_CONVERSION_WEBGL, gl.NONE);
    gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, false);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA8, gl.RGBA, gl.UNSIGNED_BYTE, image);
    gl.generateMipmap(gl.TEXTURE_2D);
    textures.set(src, { texture: t, aspect: image.naturalWidth / image.naturalHeight });
    if (scene) scene.statics = null;
    sun = null;
    request();
  })());
  return null;
}

/** A model's triangles on the card, once; null until they have loaded, when the scene is drawn again. */
function loadedMesh(path) {
  const known = meshes.get(path);
  if (known && !(known instanceof Promise)) return known;
  if (!known) meshes.set(path, (async () => {
    const meta = metas.get(path) ?? await (await fetch(path)).json();
    const bin = await (await fetch(path.slice(0, path.lastIndexOf('/') + 1) + meta.bin)).arrayBuffer();
    const vao = gl.createVertexArray();
    gl.bindVertexArray(vao);
    for (const [location, name, size, type, normalized] of [[0, 'P', 3, gl.FLOAT, false], [1, 'N', 3, gl.BYTE, true],
      [2, 'UV', 2, gl.FLOAT, false], [3, 'order', 1, gl.UNSIGNED_SHORT, false], [6, 'live', 1, gl.UNSIGNED_BYTE, false]]) {
      if (!meta.layout[name]) continue;
      const { offset, length, type: kind } = meta.layout[name];
      const Typed = { float32: Float32Array, int8: Int8Array, uint16: Uint16Array, uint8: Uint8Array }[kind];
      attribute(location, new Typed(bin, offset, length), size, type, normalized);
    }
    gl.bindVertexArray(null);
    meshes.set(path, { meta, vao });
    sun = null;
    request();
  })());
  return null;
}

function attribute(location, data, size, type, normalized) {
  gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer());
  gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW);
  gl.enableVertexAttribArray(location);
  gl.vertexAttribPointer(location, size, type, normalized, 0, 0);
}

/**
 * The deck, walls and doors as one set of triangles, grouped by picture, each vertex carrying the thing it is and its
 * tone; null while a lintel's picture, whose shape it takes, is still loading.
 */
function buildStatics({ cells, walls }, cellThings, wallThings) {
  const groups = new Map();
  const group = (src, cutout) => {
    if (!groups.has(src)) groups.set(src, { src, cutout, P: [], N: [], UV: [], thing: [], tint: [] });
    return groups.get(src);
  };
  // A quad's corners top-left, top-right, bottom-right, bottom-left as its picture is seen; `turn` quarter turns
  // clockwise of the picture on it.
  const quad = (g, corners, normal, thing, tint, [u0, v0, u1, v1] = [0, 0, 1, 1], turn = 0) => {
    const uv = [[u0, v0], [u1, v0], [u1, v1], [u0, v1]];
    const at = i => corners[(i + turn) % 4];
    for (const i of [0, 1, 2, 0, 2, 3]) {
      g.P.push(...at(i));
      g.N.push(...normal);
      g.UV.push(...uv[i]);
      g.thing.push(thing);
      g.tint.push(tint);
    }
  };
  const flat = (column, row, z, inset = 0) => {
    const [w, e, n, s] = [column + inset, column + 1 - inset, -row - inset, -row - 1 + inset];
    return [[w, n, z], [e, n, z], [e, s, z], [w, s, z]];
  };
  cells.forEach((c, i) => quad(group(c.src), flat(c.column, c.row, 0), [0, 0, 1], cellThings[i],
    DECK_TONE * c.tint * (c.fog ? FOG_TONE : 1), [DECK_INSET, DECK_INSET, 1 - DECK_INSET, 1 - DECK_INSET], c.deg / 90));
  for (const [i, w] of walls.entries()) {
    const tone = w.fog ? FOG_TONE : 1, thing = wallThings[i];
    quad(group(w.cap), flat(w.column, w.row, WALL_HIGH_M), [0, 0, 1], thing, CAP_TONE * tone,
      [JOIN_INSET, JOIN_INSET, 1 - JOIN_INSET, 1 - JOIN_INSET], w.capDeg / 90);
    for (const { side, src, plain } of w.faces) {
      for (let course = 0; course < WALL_COURSES; course++) {
        const [corners, normal] = face(w.column, w.row, side, 0, 1, 0, course * WALL_COURSE_M, (course + 1) * WALL_COURSE_M);
        quad(group(course === WALL_COURSES - 1 ? src : plain), corners, normal, thing, tone, [JOIN_INSET, 0, 1 - JOIN_INSET, 1]);
      }
      if (w.leaf) {
        const [leaf, n] = face(w.column, w.row, side, (1 - LEAF_WIDE) / 2, (1 + LEAF_WIDE) / 2, LAID_M);
        quad(group(w.leaf, true), leaf, n, thing, tone);
      }
    }
    if (w.lintel) {
      const picture = textureOf(w.lintel);
      if (!picture) return null;
      const [wide, deep] = w.lintelAcross ? [LINTEL_SPAN, LINTEL_SPAN / picture.aspect] : [LINTEL_SPAN * picture.aspect, LINTEL_SPAN];
      const x = w.column + .5, y = -w.row - .5, z = WALL_HIGH_M + LAID_M;
      quad(group(w.lintel, true), [[x - wide / 2, y + deep / 2, z], [x + wide / 2, y + deep / 2, z],
        [x + wide / 2, y - deep / 2, z], [x - wide / 2, y - deep / 2, z]], [0, 0, 1], thing, tone);
    }
  }
  const all = [...groups.values()];
  const vao = gl.createVertexArray();
  gl.bindVertexArray(vao);
  attribute(0, new Float32Array(all.flatMap(g => g.P)), 3, gl.FLOAT, false);
  attribute(1, new Float32Array(all.flatMap(g => g.N)), 3, gl.FLOAT, false);
  attribute(2, new Float32Array(all.flatMap(g => g.UV)), 2, gl.FLOAT, false);
  attribute(4, new Float32Array(all.flatMap(g => g.thing)), 1, gl.FLOAT, false);
  attribute(5, new Float32Array(all.flatMap(g => g.tint)), 1, gl.FLOAT, false);
  gl.bindVertexArray(null);
  let first = 0;
  const draws = all.map(g => {
    const count = g.P.length / 3;
    const d = { src: g.src, cutout: Boolean(g.cutout), first, count };
    first += count;
    return d;
  });
  return { vao, draws };
}

/**
 * A wall cell's face on `side`, standing from `lowM` to `highM` (the deck to the wall's top), between shares `from` and
 * `to` of its width as seen from outside and `out` metres off it: its corners top-left first, and its normal.
 */
function face(column, row, side, from, to, out, lowM = 0, highM = WALL_HIGH_M) {
  const n = -row, s = -row - 1, w = column, e = column + 1;
  const [a, b, normal] = {
    south: [[w, s - out], [e, s - out], [0, -1, 0]], north: [[e, n + out], [w, n + out], [0, 1, 0]],
    east: [[e + out, s], [e + out, n], [1, 0, 0]], west: [[w - out, n], [w - out, s], [-1, 0, 0]],
  }[side];
  const along = t => [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t];
  const [l, r] = [along(from), along(to)];
  return [[[...l, highM], [...r, highM], [...r, lowM], [...l, lowM]], normal];
}

/**
 * Each thing's draws: the statics, then every device as its model's looks, each with its own place, turn and stretch,
 * and its live parts as they stand (`liveFrame`). The sun's map is drawn once for a scene, so what swings casts nothing.
 */
function drawScene(u, forSun) {
  gl.vertexAttrib1f(6, 0);
  gl.uniformMatrix3fv(u.uTurn, false, turned(0));
  if (scene.statics) {
    gl.uniform3fv(u.uOffset, [0, 0, 0]);
    gl.uniform3fv(u.uScale, [1, 1, 1]);
    gl.vertexAttrib1f(3, 0);
    gl.bindVertexArray(scene.statics.vao);
    for (const d of scene.statics.draws) {
      const picture = textureOf(d.src);
      if (!picture) continue;
      bindPicture(u, picture.texture, false, d.cutout, 1);
      gl.drawArrays(gl.TRIANGLES, d.first, d.count);
    }
  }
  let complete = true;
  for (const d of scene.devices) {
    const mesh = loadedMesh(d.path);
    if (!mesh) {
      complete = false;
      continue;
    }
    gl.bindVertexArray(mesh.vao);
    gl.uniform3fv(u.uOffset, d.offset);
    gl.uniform3fv(u.uScale, d.scale);
    gl.uniformMatrix3fv(u.uTurn, false, d.turn);
    gl.vertexAttrib1f(4, d.thing);
    gl.vertexAttrib1f(5, 1);
    if (forSun) gl.uniform1i(u.uSwings, (mesh.meta.live ?? []).reduce((bits, e, i) => castsNone(e) ? bits | 1 << i : bits, 0));
    else if (d.live) {
      gl.uniformMatrix4fv(u.uLiveMove, false, d.live.move);
      gl.uniform4fv(u.uLiveOn, d.live.on);
      gl.uniform4fv(u.uLiveOff, d.live.off);
      gl.uniform4fv(u.uLiveSplit, d.live.split);
      gl.uniform1iv(u.uLiveMode, d.live.mode);
    }
    const folder = d.path.slice(0, d.path.lastIndexOf('/') + 1);
    for (const [look, first, count] of mesh.meta.draws) {
      const l = mesh.meta.looks[look];
      const picture = textureOf(l.texture.startsWith('assets/') ? l.texture : folder + l.texture);
      if (!picture) {
        complete = false;
        continue;
      }
      bindPicture(u, picture.texture, l.wrap, l.cutout, l.shade);
      gl.drawArrays(gl.TRIANGLES, first * 3, count * 3);
    }
  }
  gl.bindVertexArray(null);
  gl.bindSampler(0, null);
  return complete || !forSun;
}

function bindPicture(u, texture, wrap, cutout, shade) {
  gl.activeTexture(gl.TEXTURE0);
  gl.bindTexture(gl.TEXTURE_2D, texture);
  gl.bindSampler(0, samplers[wrap]);
  gl.uniform1i(u.uTex, 0);
  gl.uniform1i(u.uCutout, cutout ? 1 : 0);
  gl.uniform1f(u.uCutAlpha, light.cutoutAlpha);
  if (u.uShade) gl.uniform1f(u.uShade, shade);
}

/** The pictures each pass draws into, made again when the canvas changes size. */
function targetsFor(width, height) {
  const ss = devicePixelRatio >= 2 ? 1 : 2;
  const size = [width * ss, height * ss];
  if (targets && `${targets.size}` === `${size}`) return targets;
  if (targets) {
    [targets.albedo, targets.normal, targets.thing, targets.depth, targets.lit].forEach(t => gl.deleteTexture(t));
    gl.deleteFramebuffer(targets.gbuffer);
    gl.deleteFramebuffer(targets.light);
  }
  const t = { size, ss, albedo: colour(size), normal: colour(size), thing: colour(size), depth: depthTexture(size), lit: colour(size) };
  t.gbuffer = framebuffer([t.albedo, t.normal, t.thing], t.depth);
  t.light = framebuffer([t.lit], null);
  targets = t;
  return t;
}

function framebuffer(colours, depth) {
  const f = gl.createFramebuffer();
  gl.bindFramebuffer(gl.FRAMEBUFFER, f);
  colours.forEach((c, i) => gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0 + i, gl.TEXTURE_2D, c, 0));
  if (depth) gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.DEPTH_ATTACHMENT, gl.TEXTURE_2D, depth, 0);
  gl.drawBuffers(colours.length ? colours.map((_, i) => gl.COLOR_ATTACHMENT0 + i) : [gl.NONE]);
  return f;
}

const colour = size => storage(gl.RGBA8, size);
const depthTexture = size => storage(gl.DEPTH_COMPONENT24, size);

function storage(format, [w, h]) {
  const t = gl.createTexture();
  gl.bindTexture(gl.TEXTURE_2D, t);
  gl.texStorage2D(gl.TEXTURE_2D, 1, format, w, h);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
  return t;
}

/** The sun's view of the whole scene, as depth: drawn again only when the scene or what it has loaded changes. */
function sunMap() {
  const s = light.sun, across = unit(cross([0, 0, 1], s)), along = cross(s, across);
  const corners = cornersOf(scene.extent);
  const [a0, a1] = range(corners.map(c => dot(c, across))), [b0, b1] = range(corners.map(c => dot(c, along)));
  const [s0, s1] = range(corners.map(c => dot(c, s)));
  const pxM = Math.min(light.shadowPxM, Math.min(SHADOW_MAX_PX, gl.getParameter(gl.MAX_TEXTURE_SIZE)) / Math.max(a1 - a0, b1 - b0));
  const size = [Math.ceil((a1 - a0) * pxM) + 2, Math.ceil((b1 - b0) * pxM) + 2];
  const depth = s1 - s0;
  // World to the map's clip space: across and along to x and y, nearer the sun to lower depth.
  const matrix = new Float32Array([
    2 / (a1 - a0) * across[0], 2 / (b1 - b0) * along[0], -2 / depth * s[0], 0,
    2 / (a1 - a0) * across[1], 2 / (b1 - b0) * along[1], -2 / depth * s[1], 0,
    2 / (a1 - a0) * across[2], 2 / (b1 - b0) * along[2], -2 / depth * s[2], 0,
    -2 * a0 / (a1 - a0) - 1, -2 * b0 / (b1 - b0) - 1, 2 * s0 / depth + 1, 1,
  ]);
  if (sun?.map) gl.deleteTexture(sun.map);
  const map = depthTexture(size);
  const f = framebuffer([], map);
  gl.viewport(0, 0, ...size);
  gl.enable(gl.DEPTH_TEST);
  gl.clear(gl.DEPTH_BUFFER_BIT);
  const { p, u } = shaders.sun;
  gl.useProgram(p);
  gl.uniformMatrix4fv(u.uMatrix, false, matrix);
  const complete = drawScene(u, true);
  gl.deleteFramebuffer(f);
  return { key: scene.key, map, size, matrix, depth, texelM: 1 / pxM, complete };
}

/**
 * Draws a frame at `ms` (the display's clock): everything, or — when only live parts moved since the last — the
 * costly passes over the box round them alone, the rest of the picture kept from the frame before.
 */
function draw(ms) {
  if (!scene || !canvas || !drawable() || !canvas.clientWidth) return;
  const width = Math.round(canvas.clientWidth * devicePixelRatio), height = Math.round(canvas.clientHeight * devicePixelRatio);
  if (canvas.width !== width || canvas.height !== height) Object.assign(canvas, { width, height });
  if (!scene.statics) {
    scene.statics = buildStatics(scene.description, scene.cellThings, scene.wallThings);
    whole = true;
  }
  if (!sun || sun.key !== scene.key || !sun.complete) {
    sun = sunMap();
    whole = true;
  }
  const before = targets, t = targetsFor(width, height);
  if (t !== before) whole = true;
  const moved = liveFrame(ms);
  live.moving = moved.length > 0;
  const box = whole ? null : movedBox(moved, t);
  if (!whole && !box) return;
  whole = false;
  if (box) {
    gl.enable(gl.SCISSOR_TEST);
    gl.scissor(...box);
  }

  gl.bindFramebuffer(gl.FRAMEBUFFER, t.gbuffer);
  gl.viewport(0, 0, ...t.size);
  gl.clearColor(0, 0, 0, 0);
  gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
  gl.enable(gl.DEPTH_TEST);
  let { p, u } = shaders.gbuffer;
  gl.useProgram(p);
  gl.uniformMatrix4fv(u.uMatrix, false, view.matrix);
  gl.uniform3fv(u.uEye, view.eye);
  gl.uniform1f(u.uOrderM, ORDER_M);
  drawScene(u, false);

  gl.bindFramebuffer(gl.FRAMEBUFFER, t.light);
  gl.disable(gl.DEPTH_TEST);
  ({ p, u } = shaders.light);
  gl.useProgram(p);
  [[t.albedo, 'uAlbedo'], [t.normal, 'uNormal'], [t.depth, 'uDepthTex'], [sun.map, 'uShadowTex'], [t.thing, 'uThingTex']]
    .forEach(([texture, name], i) => {
      gl.activeTexture(gl.TEXTURE0 + i);
      gl.bindTexture(gl.TEXTURE_2D, texture);
      gl.uniform1i(u[name], i);
    });
  gl.uniformMatrix4fv(u.uInverse, false, view.inverse);
  gl.uniformMatrix4fv(u.uSunMatrix, false, sun.matrix);
  gl.uniform3fv(u.uEye, view.eye);
  gl.uniform3fv(u.uSun, light.sun);
  gl.uniform3fv(u.uAmber, AMBER);
  gl.uniform2fv(u.uShadowSize, sun.size);
  gl.uniform2fv(u.uAoRadii, light.aoRadiiM);
  gl.uniform1i(u.uAoDirs, light.aoDirections);
  gl.uniform1i(u.uStep, t.ss);
  gl.uniform1i(u.uGlowPx, GLOW_PX * t.ss);
  gl.uniform1i(u.uHover, marks.hover);
  gl.uniform1iv(u.uOpen, Int32Array.from({ length: OPEN_MAX }, (_, i) => marks.open[i] ?? -1));
  const scalars = {
    uPxPerMetre: t.size[1] / (2 * Math.tan(FOV_DEG * Math.PI / 360)), uSunDepth: sun.depth, uShadowTexelM: sun.texelM, uAmbient: light.ambient,
    uKeep: light.shadowKeep, uLift: light.shadowLiftM, uBias: light.shadowBiasM, uAoStrength: light.aoStrength,
    uAoMargin: light.aoMarginM, uEdgeM: light.edgeM, uEdgeShade: light.edgeShade, uFoldCos: light.foldCos,
    uFoldLight: light.foldLight, uHoverLight: HOVER_LIGHT, uGlowGain: GLOW_GAIN, uHalo: HALO,
  };
  for (const [name, v] of Object.entries(scalars)) gl.uniform1f(u[name], v);
  gl.uniform1i(u.uHaloPx, HALO_PX * t.ss);
  gl.drawArrays(gl.TRIANGLES, 0, 3);
  gl.disable(gl.SCISSOR_TEST);

  gl.bindFramebuffer(gl.FRAMEBUFFER, null);
  gl.viewport(0, 0, width, height);
  gl.clear(gl.COLOR_BUFFER_BIT);
  ({ p, u } = shaders.resolve);
  gl.useProgram(p);
  gl.activeTexture(gl.TEXTURE0);
  gl.bindTexture(gl.TEXTURE_2D, t.lit);
  gl.uniform1i(u.uLit, 0);
  gl.uniform1i(u.uSS, t.ss);
  gl.drawArrays(gl.TRIANGLES, 0, 3);
}

/**
 * Sets every device's live parts as they stand at `ms` (`d.live`, the shaders' arrays) from what `setLive` was last
 * told, and says what moves of its own — a needle swinging, a cycle filling, a fan turning, a fault blinking — as the
 * corners of the world box each sweeps, so the frame after is asked for while any does.
 */
function liveFrame(ms) {
  const { nowS, rate } = live.clock();
  const dtS = live.lastMs ? Math.min((ms - live.lastMs) / MS_PER_S, LONGEST_STEP_S) : 0;
  live.lastMs = ms;
  const blinkOn = Math.floor(ms / MS_PER_S * BLINK_HZ * 2) % 2 === 0;
  const moved = [];
  for (const d of scene.devices) {
    const mesh = meshes.get(d.path);
    const parts = mesh && !(mesh instanceof Promise) ? mesh.meta.live : null;
    if (!parts) {
      d.live = null;
      continue;
    }
    const s = live.byId.get(d.id);
    const ticking = Boolean(s?.runs) && rate > 0;
    const fault = s?.last === 'Starved' || s?.last === 'Full';
    const running = ticking && !fault;
    const share = show => !s ? 0 : clamp01(show === 'cycle' ? (s.runs && s.cycleS ? (nowS - s.cycleFromS) / s.cycleS : 0) : s[show] ?? 0);
    const l = d.live ??= { move: new Float32Array(16 * LIVE_MAX), on: new Float32Array(4 * LIVE_MAX),
      off: new Float32Array(4 * LIVE_MAX), split: new Float32Array(4 * LIVE_MAX), mode: new Int32Array(LIVE_MAX) };
    parts.forEach((e, i) => {
      const key = `${d.id} ${d.path} ${i}`;
      let move = IDENTITY, on = LIT, split = ALWAYS, moves = false;
      if (e.as === 'lamp') {
        const tone = e.show === 'run' ? (running ? 'running' : 'off') : fault ? (blinkOn ? 'fault' : 'off')
          : s?.short && s.runs ? 'short' : e.show === 'state' && running ? 'running' : 'off';
        on = LAMP[tone];
        moves = fault && e.show !== 'run';
      } else if (e.as === 'glow') {
        on = running ? LIT : DIMMED;
      } else if (e.as === 'fill') {
        const v = e.steps ? Math.floor(share(e.show) * e.steps + 1e-6) / e.steps : share(e.show);
        const [lo, hi] = e.spanM;
        split = [...e.axis, v <= 0 ? lo - 1 : v >= 1 ? hi + 1 : lo + v * (hi - lo)];
        moves = e.show === 'cycle' && ticking;
      } else if (e.as === 'needle') {
        const target = share(e.show), was = live.shown.get(key) ?? target;
        const reading = was + Math.sign(target - was) * Math.min(Math.abs(target - was), NEEDLE_PER_S * dtS);
        live.shown.set(key, reading);
        move = turnAbout(e.pivotM, e.axis, -reading * e.sweepDeg);
        moves = reading !== target || (e.show === 'cycle' && ticking);
      } else if (e.as === 'spin') {
        const angle = ((live.shown.get(key) ?? 0) + (running ? e.degPerS * dtS : 0)) % 360;
        live.shown.set(key, angle);
        move = turnAbout(e.pivotM, e.axis, -angle);
        moves = running;
      } else if (e.as === 'stroke') {
        const phase = ((live.shown.get(key) ?? 0) + (running ? dtS / e.periodS : 0)) % 1;
        live.shown.set(key, phase);
        const out = (1 - Math.abs(1 - 2 * phase)) * e.strokeM;
        move = new Float32Array([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, ...e.axis.map(v => v * out), 1]);
        moves = running;
      }
      l.move.set(move, 16 * i);
      l.on.set(on, 4 * i);
      l.off.set(DIMMED, 4 * i);
      l.split.set(split, 4 * i);
      l.mode[i] = MODE[e.as];
      if (moves) moved.push(sweptCorners(d, e));
    });
  }
  return moved;
}

const MS_PER_S = 1000;
// A frame after a pause moves what turns on by no more than this, so nothing jumps.
const LONGEST_STEP_S = .1;
const IDENTITY = new Float32Array([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]);
// A split every point of a part is on the lit side of.
const ALWAYS = [0, 0, 0, 1];
const clamp01 = v => Math.min(1, Math.max(0, v));

/** The world corners of the box a live part of device `d` stays in: what turns, as far round its pivot as it reaches. */
function sweptCorners(d, e) {
  let box = e.boxM;
  if (e.pivotM) {
    const reach = Math.max(...cornersOf(e.boxM).map(c => Math.hypot(...c.map((v, i) => v - e.pivotM[i]))));
    box = [e.pivotM.map(v => v - reach), e.pivotM.map(v => v + reach)];
  } else if (e.strokeM) {
    const far = e.boxM.map(c => c.map((v, i) => v + e.axis[i] * e.strokeM));
    box = [0, 1].map(end => [0, 1, 2].map(i => (end ? Math.max : Math.min)(e.boxM[end][i], far[end][i])));
  }
  return cornersOf(box).map(c => apply(d.turn, c.map((v, i) => v * d.scale[i])).map((v, i) => v + d.offset[i]));
}

/**
 * The box on the targets round every point of `moved`, `[x, y, width, height]`, widened by the reach of what is
 * measured across a pixel; null when none of it is in view, the whole picture when some is behind the eye.
 */
function movedBox(moved, t) {
  const [w, h] = t.size, m = view.matrix;
  let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity, nearest = Infinity;
  for (const [x, y, z] of moved.flat()) {
    const cw = m[3] * x + m[7] * y + m[11] * z + m[15];
    if (cw <= 0) return [0, 0, w, h];
    const px = ((m[0] * x + m[4] * y + m[8] * z + m[12]) / cw * .5 + .5) * w;
    const py = ((m[1] * x + m[5] * y + m[9] * z + m[13]) / cw * .5 + .5) * h;
    [x0, x1, y0, y1] = [Math.min(x0, px), Math.max(x1, px), Math.min(y0, py), Math.max(y1, py)];
    nearest = Math.min(nearest, Math.hypot(x - view.eye[0], y - view.eye[1], z - view.eye[2]));
  }
  if (!moved.length) return null;
  const pxPerMetre = h / (2 * Math.tan(FOV_DEG * Math.PI / 360)) / nearest;
  const pad = MOVED_PAD_PX * t.ss + Math.max(...light.aoRadiiM) * 4 * pxPerMetre;
  const [left, bottom] = [Math.max(0, Math.floor(x0 - pad)), Math.max(0, Math.floor(y0 - pad))];
  const [right, top] = [Math.min(w, Math.ceil(x1 + pad)), Math.min(h, Math.ceil(y1 + pad))];
  return right > left && top > bottom ? [left, bottom, right - left, top - bottom] : null;
}

/** A turn of `deg` about the axis `[x, y, z]` (a unit vector) through `pivot`, counter-clockwise seen from its tip. */
function turnAbout(pivot, [x, y, z], deg) {
  const a = deg * Math.PI / 180, c = Math.cos(a), s = Math.sin(a), k = 1 - c;
  const r = [c + x * x * k, y * x * k + z * s, z * x * k - y * s, x * y * k - z * s, c + y * y * k, z * y * k + x * s,
    x * z * k + y * s, y * z * k - x * s, c + z * z * k];
  const moved = apply(r, pivot);
  return new Float32Array([...r.slice(0, 3), 0, ...r.slice(3, 6), 0, ...r.slice(6), 0,
    pivot[0] - moved[0], pivot[1] - moved[1], pivot[2] - moved[2], 1]);
}

/** A turn about the vertical of `deg` clockwise seen from above, as a 3×3 matrix. */
function turned(deg) {
  const a = -deg * Math.PI / 180, c = Math.cos(a), s = Math.sin(a);
  return new Float32Array([c, s, 0, -s, c, 0, 0, 0, 1]);
}

/** A 3×3 column-major matrix `m` times the vector `v`. */
const apply = (m, v) => [0, 1, 2].map(i => m[i] * v[0] + m[3 + i] * v[1] + m[6 + i] * v[2]);

const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
const unit = a => a.map(v => v / Math.hypot(...a));
const range = values => [Math.min(...values), Math.max(...values)];

// 4×4 matrices, column-major as WebGL takes them.
function perspective(fovy, aspect, near, far) {
  const f = 1 / Math.tan(fovy / 2);
  return new Float32Array([f / aspect, 0, 0, 0, 0, f, 0, 0, 0, 0, (far + near) / (near - far), -1,
    0, 0, 2 * far * near / (near - far), 0]);
}

function lookAt(eye, target, up) {
  const z = unit(eye.map((v, i) => v - target[i])), x = unit(cross(up, z)), y = cross(z, x);
  return new Float32Array([x[0], y[0], z[0], 0, x[1], y[1], z[1], 0, x[2], y[2], z[2], 0,
    -dot(x, eye), -dot(y, eye), -dot(z, eye), 1]);
}

function multiply(a, b) {
  const out = new Float32Array(16);
  for (let c = 0; c < 4; c++)
    for (let r = 0; r < 4; r++) out[c * 4 + r] = a[r] * b[c * 4] + a[4 + r] * b[c * 4 + 1] + a[8 + r] * b[c * 4 + 2] + a[12 + r] * b[c * 4 + 3];
  return out;
}

function invert(m) {
  const inv = new Float32Array(16);
  const [a00, a01, a02, a03, a10, a11, a12, a13, a20, a21, a22, a23, a30, a31, a32, a33] = m;
  const b00 = a00 * a11 - a01 * a10, b01 = a00 * a12 - a02 * a10, b02 = a00 * a13 - a03 * a10, b03 = a01 * a12 - a02 * a11;
  const b04 = a01 * a13 - a03 * a11, b05 = a02 * a13 - a03 * a12, b06 = a20 * a31 - a21 * a30, b07 = a20 * a32 - a22 * a30;
  const b08 = a20 * a33 - a23 * a30, b09 = a21 * a32 - a22 * a31, b10 = a21 * a33 - a23 * a31, b11 = a22 * a33 - a23 * a32;
  const det = 1 / (b00 * b11 - b01 * b10 + b02 * b09 + b03 * b08 - b04 * b07 + b05 * b06);
  inv.set([
    (a11 * b11 - a12 * b10 + a13 * b09) * det, (a02 * b10 - a01 * b11 - a03 * b09) * det,
    (a31 * b05 - a32 * b04 + a33 * b03) * det, (a22 * b04 - a21 * b05 - a23 * b03) * det,
    (a12 * b08 - a10 * b11 - a13 * b07) * det, (a00 * b11 - a02 * b08 + a03 * b07) * det,
    (a32 * b02 - a30 * b05 - a33 * b01) * det, (a20 * b05 - a22 * b02 + a23 * b01) * det,
    (a10 * b10 - a11 * b08 + a13 * b06) * det, (a01 * b08 - a00 * b10 - a03 * b06) * det,
    (a30 * b04 - a31 * b02 + a33 * b00) * det, (a21 * b02 - a20 * b04 - a23 * b00) * det,
    (a11 * b07 - a10 * b09 - a12 * b06) * det, (a00 * b09 - a01 * b07 + a02 * b06) * det,
    (a31 * b01 - a30 * b03 - a32 * b00) * det, (a20 * b03 - a21 * b01 + a22 * b00) * det,
  ]);
  return inv;
}

// Each vertex: its place in its model (aP) moved as its live part stands (aLive, from 1), put in the world (uScale,
// uTurn, then uOffset), nudged toward the eye by its part's order; its normal turned as the stretch turns it.
const G_VERTEX = `#version 300 es
layout(location = 0) in vec3 aP;
layout(location = 1) in vec3 aN;
layout(location = 2) in vec2 aUV;
layout(location = 3) in float aOrder;
layout(location = 4) in float aThing;
layout(location = 5) in float aTint;
layout(location = 6) in float aLive;
uniform mat4 uMatrix;
uniform mat4 uLiveMove[${LIVE_MAX}];
uniform mat3 uTurn;
uniform vec3 uOffset, uScale, uEye;
uniform float uOrderM;
out vec3 vN, vWorld, vModel;
out vec2 vUV;
flat out float vThing;
flat out int vLive;
out float vTint;
void main() {
  vLive = int(aLive + .5);
  vec3 m = aP, n = aN;
  if (vLive > 0) {
    m = (uLiveMove[vLive - 1] * vec4(aP, 1.)).xyz;
    n = mat3(uLiveMove[vLive - 1]) * aN;
  }
  vec3 p = uTurn * (m * uScale) + uOffset;
  p += normalize(uEye - p) * aOrder * uOrderM;
  gl_Position = uMatrix * vec4(p, 1.);
  vN = uTurn * (n / uScale);
  vWorld = p;
  vModel = aP;
  vUV = aUV;
  vThing = aThing;
  vTint = aTint;
}`;

// A face turned from the eye is not drawn, as the renderer culls it; a little past edge-on still is, so a round part's
// interpolated normal opens no gap along its outline. A live part takes its tone — uLiveOn on the lit side of its
// split (a fill's reach along its axis), uLiveOff past it — as its MODE says; how much it glows goes out in the
// albedo's alpha.
const G_FRAGMENT = `#version 300 es
precision highp float;
in vec3 vN, vWorld, vModel;
in vec2 vUV;
flat in float vThing;
flat in int vLive;
in float vTint;
uniform sampler2D uTex;
uniform float uShade, uCutAlpha;
uniform bool uCutout;
uniform vec3 uEye;
uniform vec4 uLiveOn[${LIVE_MAX}], uLiveOff[${LIVE_MAX}], uLiveSplit[${LIVE_MAX}];
uniform int uLiveMode[${LIVE_MAX}];
layout(location = 0) out vec4 oAlbedo;
layout(location = 1) out vec4 oNormal;
layout(location = 2) out vec4 oThing;
void main() {
  vec3 n = normalize(vN);
  if (dot(n, normalize(uEye - vWorld)) < -.2) discard;
  vec4 t = texture(uTex, vUV);
  if (uCutout && t.a < uCutAlpha) discard;
  vec3 c = t.rgb;
  float glow = 0.;
  int mode = vLive > 0 ? uLiveMode[vLive - 1] : 0;
  if (mode > 0) {
    vec4 split = uLiveSplit[vLive - 1];
    vec4 tone = dot(vModel, split.xyz) <= split.w ? uLiveOn[vLive - 1] : uLiveOff[vLive - 1];
    float most = max(c.r, max(c.g, c.b));
    float lens = mode == 2 ? smoothstep(.08, .25, most - min(c.r, min(c.g, c.b))) : 1.;
    c = mix(c, (mode == 2 ? vec3(min(1., most * 1.4)) : c) * tone.rgb, lens);
    glow = tone.a * lens;
  }
  oAlbedo = vec4(c * mix(uShade * vTint, 1., glow), glow);
  oNormal = vec4(n * .5 + .5, 1.);
  uint id = uint(vThing + .5);
  oThing = vec4(float(id & 255u), float((id >> 8) & 255u), float((id >> 16) & 255u), 255.) / 255.;
}`;

// A live part that swings (uSwings, a bit each) is left out: the map is drawn once for a scene.
const SUN_VERTEX = `#version 300 es
layout(location = 0) in vec3 aP;
layout(location = 2) in vec2 aUV;
layout(location = 6) in float aLive;
uniform mat4 uMatrix;
uniform mat3 uTurn;
uniform vec3 uOffset, uScale;
uniform int uSwings;
out vec2 vUV;
void main() {
  int live = int(aLive + .5);
  gl_Position = live > 0 && ((uSwings >> (live - 1)) & 1) == 1 ? vec4(2., 2., 2., 1.)
    : uMatrix * vec4(uTurn * (aP * uScale) + uOffset, 1.);
  vUV = aUV;
}`;

// A cutout face casts only where its picture is solid.
const SUN_FRAGMENT = `#version 300 es
precision highp float;
in vec2 vUV;
uniform sampler2D uTex;
uniform bool uCutout;
uniform float uCutAlpha;
void main() {
  if (uCutout && texture(uTex, vUV).a < uCutAlpha) discard;
}`;

const FULL_VERTEX = `#version 300 es
void main() {
  gl_Position = vec4(gl_VertexID == 1 ? 3. : -1., gl_VertexID == 2 ? 3. : -1., 0., 1.);
}`;

// The renderer's light pass (_shapes_render.lit) for a camera in perspective: the sun by the normal and its shadow map;
// ambient occlusion and the outlines measured as how far a neighbour stands off a pixel's own plane, the neighbours
// taken as far apart on the page as the renderer's radii are at that distance; then what is pointed at, lit, and what
// is open, ringed. What glows (the albedo's alpha) is lit by itself, and lights the pixels round it.
const LIGHT_FRAGMENT = `#version 300 es
precision highp float;
uniform sampler2D uAlbedo, uNormal, uDepthTex, uShadowTex, uThingTex;
uniform mat4 uInverse, uSunMatrix;
uniform vec3 uEye, uSun, uAmber;
uniform vec2 uShadowSize, uAoRadii;
uniform float uPxPerMetre, uSunDepth, uShadowTexelM, uAmbient, uKeep, uLift, uBias, uAoStrength, uAoMargin, uEdgeM, uEdgeShade,
              uFoldCos, uFoldLight, uHoverLight, uGlowGain, uHalo;
uniform int uAoDirs, uStep, uGlowPx, uHover, uHaloPx;
uniform int uOpen[${OPEN_MAX}];
out vec4 oColour;
ivec2 size;

bool inside(ivec2 p) { return all(greaterThanEqual(p, ivec2(0))) && all(lessThan(p, size)); }
float depthOf(ivec2 p) { return inside(p) ? texelFetch(uDepthTex, p, 0).r : 1.; }
vec3 worldAt(ivec2 p, float z) {
  vec4 w = uInverse * vec4((vec2(p) + .5) / vec2(size) * 2. - 1., z * 2. - 1., 1.);
  return w.xyz / w.w;
}
int thingAt(ivec2 p) {
  vec4 t = texelFetch(uThingTex, p, 0) * 255. + .5;
  return int(t.r) + int(t.g) * 256 + int(t.b) * 65536;
}
bool isOpen(int id) {
  for (int i = 0; i < ${OPEN_MAX}; i++) if (uOpen[i] == id && id > 0) return true;
  return false;
}
void main() {
  size = textureSize(uDepthTex, 0);
  ivec2 p = ivec2(gl_FragCoord.xy);
  float z = texelFetch(uDepthTex, p, 0).r;
  int me = thingAt(p);
  vec4 ring = vec4(0.);
  if (!isOpen(me))
    for (int y = -uGlowPx; y <= uGlowPx; y += max(uGlowPx / 2, 1))
      for (int x = -uGlowPx; x <= uGlowPx; x += max(uGlowPx / 2, 1)) {
        ivec2 q = p + ivec2(x, y);
        if (inside(q) && isOpen(thingAt(q))) ring = vec4(uAmber, .85);
      }
  if (z >= 1.) { oColour = ring; return; }
  vec3 P = worldAt(p, z);
  vec3 n = normalize(texelFetch(uNormal, p, 0).xyz * 2. - 1.);
  float pxPerM = uPxPerMetre / distance(P, uEye);

  float toSun = dot(n, uSun);
  // A map pixel holds its surface's depth at the pixel's centre, and a plane slanted off the sun departs from that by
  // the slant's tangent a metre across; lifted that far times the slant's sine along its normal, a point clears its
  // own plane out to the farthest centre read. The renderer's fixed lift alone holds only at its own pixels a metre.
  float slant = sqrt(max(0., 1. - toSun * toSun));
  float reachM = (float(${SHADOW_KERNEL_PX}) + .5) * sqrt(2.) * uShadowTexelM;
  vec3 q = P + n * (uLift + reachM * slant);
  vec4 s = uSunMatrix * vec4(q, 1.);
  vec2 st = (s.xy * .5 + .5) * uShadowSize;
  float qz = s.z * .5 + .5 - uBias / uSunDepth;
  float reached = 0.;
  for (int dy = -${SHADOW_KERNEL_PX}; dy <= ${SHADOW_KERNEL_PX}; dy++)
    for (int dx = -${SHADOW_KERNEL_PX}; dx <= ${SHADOW_KERNEL_PX}; dx++) {
      ivec2 c = clamp(ivec2(floor(st)) + ivec2(dx, dy), ivec2(0), ivec2(uShadowSize) - 1);
      reached += texelFetch(uShadowTex, c, 0).r >= qz ? 1. : 0.;
    }
  float sunlit = reached / float((2 * ${SHADOW_KERNEL_PX} + 1) * (2 * ${SHADOW_KERNEL_PX} + 1));

  float blocked = 0.;
  int samples = 0;
  for (int r = 0; r < 2; r++)
    for (int k = 0; k < uAoDirs; k++) {
      float radius = uAoRadii[r];
      float a = 6.2831853 * (float(k) + (r == 1 ? .5 : 0.)) / float(uAoDirs);
      ivec2 o = ivec2(round(vec2(cos(a), sin(a)) * radius * pxPerM));
      samples++;
      float zn = depthOf(p + o);
      if (zn >= 1.) continue;
      vec3 d = worldAt(p + o, zn) - P;
      if (length(d) < 4. * radius) blocked += clamp((dot(d, n) - uAoMargin) / radius, 0., 1.);
    }
  float ao = 1. - uAoStrength * blocked / float(samples);

  bool outline = false, fold = false;
  ivec2 steps[4] = ivec2[4](ivec2(uStep, 0), ivec2(-uStep, 0), ivec2(0, uStep), ivec2(0, -uStep));
  for (int i = 0; i < 4; i++) {
    ivec2 o = p + steps[i];
    float zn = depthOf(o);
    if (zn >= 1.) { outline = true; continue; }
    float rise = dot(worldAt(o, zn) - P, n);
    outline = outline || rise > uEdgeM;
    vec3 m = normalize(texelFetch(uNormal, o, 0).xyz * 2. - 1.);
    fold = fold || (dot(n, m) < uFoldCos && rise < 0. && rise > -uEdgeM && toSun > dot(m, uSun));
  }
  float edge = outline ? uEdgeShade : fold ? uFoldLight : 1.;

  float light = (uAmbient + (1. - uAmbient) * max(toSun, 0.) * (uKeep + (1. - uKeep) * sunlit)) * ao;
  vec4 albedo = texelFetch(uAlbedo, p, 0);
  vec3 c = albedo.rgb * mix(light, uGlowGain, albedo.a) * edge * (me == uHover && me > 0 ? uHoverLight : 1.);
  vec3 halo = vec3(0.);
  for (int k = 0; k < 8; k++) {
    float a = .7853982 * float(k);
    vec4 near = texelFetch(uAlbedo, clamp(p + ivec2(round(vec2(cos(a), sin(a)) * float(uHaloPx))), ivec2(0), size - 1), 0);
    halo += near.rgb * near.a;
  }
  c += halo * uHalo / 8.;
  oColour = vec4(mix(c, ring.rgb, ring.a), 1.);
}`;

// Averaged down premultiplied, so an edge fades to space rather than to black.
const RESOLVE_FRAGMENT = `#version 300 es
precision highp float;
uniform sampler2D uLit;
uniform int uSS;
out vec4 oColour;
void main() {
  ivec2 p = ivec2(gl_FragCoord.xy) * uSS;
  vec3 c = vec3(0.);
  float a = 0.;
  for (int y = 0; y < uSS; y++)
    for (int x = 0; x < uSS; x++) {
      vec4 t = texelFetch(uLit, p + ivec2(x, y), 0);
      c += t.rgb * t.a;
      a += t.a;
    }
  oColour = a > 0. ? vec4(c / a, a / float(uSS * uSS)) : vec4(0.);
}`;
