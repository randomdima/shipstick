// The ship's floor in 3D (GAM-10, GAM-13): every deck plate, wall, door and device a textured model in one scene,
// drawn live in WebGL2 with the renderer's passes (.qq/_shapes_render.py) — sun, shadow map, occlusion, outlines —
// from a camera the player turns, tilts and zooms (cabin.js) round the middle of the view. A device is its
// model as `qq sprites use` wrote it (assets/<path>/<id>.mesh.json, .qq/_shapes_mesh.py), or the plain crate stretched
// to its footprint until it has one; walls and doors are the kit's caps and panels on blocks a cell square; the deck is
// its plates. What the pointer is over is read back from the picture (`pick`); where a thing stands on the page comes
// from the camera (`rectOf`, `pointOf`), for the windows, leaders, lamps and tags laid over it.
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
const WALL_HIGH_M = WALL_COURSE_M * WALL_COURSES;
const LAID_M = .003;
// The kit's pieces and the deck's tiles are cut with a dark fringe: this share of each edge is left off.
const JOIN_INSET = (1 - 1 / 1.04) / 2;
const DECK_INSET = (1 - 1 / 1.12) / 2;
// The deck and the caps are drawn darker than they are lit, as the stylesheet drew them; a fogged capsule darker still.
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
const TALLEST_M = 3;
// The stand-in for a device with no model of its own: the crate, stretched to its footprint.
const CRATE = 'assets/parts/any_crate.mesh.json';

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
let queued = false;

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

/** Whether `path` names a model of a device (its own) the scene can draw. */
export const hasModel = path => metas.has(path);

/**
 * What the floor shows: `cells` of deck ({ column, row, src, deg, tint, fog, at }), `walls` ({ column, row, cap,
 * capDeg, faces: [{ side, src }], lintel, lintelAcross, leaf, id, at, title, fog }) and `devices` ({ column, row,
 * columns, rows, mesh, id, at, title }), each at its ship cell; `id` is what a click opens, `at` the capsule it is in.
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
    return { path, offset, scale, thing: thing(d.id, d.at, d.title, [offset, [d.column + d.columns, -d.row, height]]), tint: 1 };
  });
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

/** The box on the page round what opens `id`, as a DOMRect-like; null when nothing in view does. */
export function rectOf(id) {
  const boxes = scene?.things.filter(t => t && t.id === id).map(t => t.box) ?? [];
  const points = boxes.flatMap(([lo, hi]) => [0, 1, 2, 3, 4, 5, 6, 7]
    .map(i => pointOf([(i & 1 ? hi : lo)[0], (i & 2 ? hi : lo)[1], (i & 4 ? hi : lo)[2]]))).filter(Boolean);
  if (!points.length) return null;
  const left = Math.min(...points.map(p => p.x)), right = Math.max(...points.map(p => p.x));
  const top = Math.min(...points.map(p => p.y)), bottom = Math.max(...points.map(p => p.y));
  return { left, right, top, bottom, width: right - left, height: bottom - top, x: left, y: top };
}

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

function request() {
  if (queued) return;
  queued = true;
  requestAnimationFrame(() => {
    queued = false;
    draw();
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
function meshOf(path) {
  const known = meshes.get(path);
  if (known && !(known instanceof Promise)) return known;
  if (!known) meshes.set(path, (async () => {
    const meta = metas.get(path) ?? await (await fetch(path)).json();
    const bin = await (await fetch(path.slice(0, path.lastIndexOf('/') + 1) + meta.bin)).arrayBuffer();
    const vao = gl.createVertexArray();
    gl.bindVertexArray(vao);
    for (const [location, name, size, type, normalized] of [[0, 'P', 3, gl.FLOAT, false], [1, 'N', 3, gl.BYTE, true],
      [2, 'UV', 2, gl.FLOAT, false], [3, 'order', 1, gl.UNSIGNED_SHORT, false]]) {
      const { offset, length, type: kind } = meta.layout[name];
      const Typed = { float32: Float32Array, int8: Int8Array, uint16: Uint16Array }[kind];
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

/** Each thing's draws: the statics, then every device as its model's looks, each with its own place and stretch. */
function drawScene(u, forSun) {
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
    const mesh = meshOf(d.path);
    if (!mesh) {
      complete = false;
      continue;
    }
    gl.bindVertexArray(mesh.vao);
    gl.uniform3fv(u.uOffset, d.offset);
    gl.uniform3fv(u.uScale, d.scale);
    gl.vertexAttrib1f(4, d.thing);
    gl.vertexAttrib1f(5, d.tint);
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
  const [lo, hi] = scene.extent;
  const corners = [0, 1, 2, 3, 4, 5, 6, 7].map(i => [(i & 1 ? hi : lo)[0], (i & 2 ? hi : lo)[1], (i & 4 ? hi : lo)[2]]);
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
  return { key: scene.key, map, size, matrix, depth, complete };
}

function draw() {
  if (!scene || !canvas || !drawable() || !canvas.clientWidth) return;
  const width = Math.round(canvas.clientWidth * devicePixelRatio), height = Math.round(canvas.clientHeight * devicePixelRatio);
  if (canvas.width !== width || canvas.height !== height) Object.assign(canvas, { width, height });
  scene.statics ??= buildStatics(scene.description, scene.cellThings, scene.wallThings);
  if (!sun || sun.key !== scene.key || !sun.complete) sun = sunMap();
  const t = targetsFor(width, height);

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
    uPxPerMetre: t.size[1] / (2 * Math.tan(FOV_DEG * Math.PI / 360)), uSunDepth: sun.depth, uAmbient: light.ambient,
    uKeep: light.shadowKeep, uLift: light.shadowLiftM, uBias: light.shadowBiasM, uAoStrength: light.aoStrength,
    uAoMargin: light.aoMarginM, uEdgeM: light.edgeM, uEdgeShade: light.edgeShade, uFoldCos: light.foldCos,
    uFoldLight: light.foldLight, uHoverLight: HOVER_LIGHT,
  };
  for (const [name, v] of Object.entries(scalars)) gl.uniform1f(u[name], v);
  gl.drawArrays(gl.TRIANGLES, 0, 3);

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

// Each vertex: its place in its model (aP) put in the world (uScale, then uOffset), nudged toward the eye by its part's
// order; its normal turned as the stretch turns it.
const G_VERTEX = `#version 300 es
layout(location = 0) in vec3 aP;
layout(location = 1) in vec3 aN;
layout(location = 2) in vec2 aUV;
layout(location = 3) in float aOrder;
layout(location = 4) in float aThing;
layout(location = 5) in float aTint;
uniform mat4 uMatrix;
uniform vec3 uOffset, uScale, uEye;
uniform float uOrderM;
out vec3 vN, vWorld;
out vec2 vUV;
flat out float vThing;
out float vTint;
void main() {
  vec3 p = aP * uScale + uOffset;
  p += normalize(uEye - p) * aOrder * uOrderM;
  gl_Position = uMatrix * vec4(p, 1.);
  vN = aN / uScale;
  vWorld = p;
  vUV = aUV;
  vThing = aThing;
  vTint = aTint;
}`;

// A face turned from the eye is not drawn, as the renderer culls it; a little past edge-on still is, so a round part's
// interpolated normal opens no gap along its outline.
const G_FRAGMENT = `#version 300 es
precision highp float;
in vec3 vN, vWorld;
in vec2 vUV;
flat in float vThing;
in float vTint;
uniform sampler2D uTex;
uniform float uShade, uCutAlpha;
uniform bool uCutout;
uniform vec3 uEye;
layout(location = 0) out vec4 oAlbedo;
layout(location = 1) out vec4 oNormal;
layout(location = 2) out vec4 oThing;
void main() {
  vec3 n = normalize(vN);
  if (dot(n, normalize(uEye - vWorld)) < -.2) discard;
  vec4 t = texture(uTex, vUV);
  if (uCutout && t.a < uCutAlpha) discard;
  oAlbedo = vec4(t.rgb * uShade * vTint, 1.);
  oNormal = vec4(n * .5 + .5, 1.);
  uint id = uint(vThing + .5);
  oThing = vec4(float(id & 255u), float((id >> 8) & 255u), float((id >> 16) & 255u), 255.) / 255.;
}`;

const SUN_VERTEX = `#version 300 es
layout(location = 0) in vec3 aP;
layout(location = 2) in vec2 aUV;
uniform mat4 uMatrix;
uniform vec3 uOffset, uScale;
out vec2 vUV;
void main() {
  gl_Position = uMatrix * vec4(aP * uScale + uOffset, 1.);
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
// is open, ringed.
const LIGHT_FRAGMENT = `#version 300 es
precision highp float;
uniform sampler2D uAlbedo, uNormal, uDepthTex, uShadowTex, uThingTex;
uniform mat4 uInverse, uSunMatrix;
uniform vec3 uEye, uSun, uAmber;
uniform vec2 uShadowSize, uAoRadii;
uniform float uPxPerMetre, uSunDepth, uAmbient, uKeep, uLift, uBias, uAoStrength, uAoMargin, uEdgeM, uEdgeShade,
              uFoldCos, uFoldLight, uHoverLight;
uniform int uAoDirs, uStep, uGlowPx, uHover;
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

  vec3 q = P + n * uLift;
  vec4 s = uSunMatrix * vec4(q, 1.);
  vec2 st = (s.xy * .5 + .5) * uShadowSize;
  float qz = s.z * .5 + .5 - uBias / uSunDepth;
  float reached = 0.;
  for (int dy = -1; dy <= 1; dy++)
    for (int dx = -1; dx <= 1; dx++) {
      ivec2 c = clamp(ivec2(floor(st)) + ivec2(dx, dy), ivec2(0), ivec2(uShadowSize) - 1);
      reached += texelFetch(uShadowTex, c, 0).r >= qz ? 1. : 0.;
    }
  float sunlit = reached / 9.;

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
  float toSun = dot(n, uSun);
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
  vec3 c = texelFetch(uAlbedo, p, 0).rgb * light * edge * (me == uHover && me > 0 ? uHoverLight : 1.);
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
