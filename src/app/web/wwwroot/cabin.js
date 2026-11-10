// The ship's floor and the windows opened on it: what the player's page and the admin's both draw. Which seat a move
// is made from, and what a click on a slot does, are the view's, handed in through `hooks`. What a fixture or an item
// is called, and every way a device can run, are the codex's.

import { nameOf, codeOf, roleOf, waysOf, way, chipLook, go, openCodex, effectText } from './codex.js'
import { meshOf, structureLook, paintOf, doorPaint, deckOf, doorGaugeOf } from './art.js'
import {
  PITCH, WALL_HIGH_M, ZOOM, aim, camera, deckAt, drawable, pick, rectOf, sceneCanvas, setLive, setMarks, setScene,
} from './scene.js'
import { line, nowS, send } from './host.js'
import { $, esc, inFrame, keepInside, patch, reconcile, setAttributes, setStyle, setText } from './dom.js'

// How far the pointer travels before a press on an item is a drag.
const DRAG_START_PX = 4;
// A new window opens this far right of what was clicked, and is kept this far inside the page.
const WINDOW_OFFSET_PX = 12;
const WINDOW_MARGIN_PX = 8;
const CHEST_SLOTS_ACROSS = 4;
// What on a window does something of its own when pressed; a press anywhere else drags the window.
const CONTROLS = 'button, select, input, label, a, .slot';

const STATE = { NotYet: 'standby', Ran: 'running', Starved: 'input short', Full: 'output full' };

// windows: inventory id → { x, y, z } of each open window, in page pixels. press: a pointer held down on a slot.
// view: the ship's { column, row }, in fractional cells, held at the middle of the floor's view; null until the view's
// first draw centres its capsule. pan: a pointer held down on the floor; panned: whether the last one dragged it, so
// its release opens nothing. pointsAsked, pointsShown: the last read of what the pointer is over asked for, and shown.
const ui = { windows: new Map(), topZ: 1, press: null, grip: null, view: null, pan: null, panned: false, pointsAsked: 0,
  pointsShown: 0 };

/**
 * What the view in charge does: `draw()` redraws the page, `slotClicked(slot)` takes a click on a slot that was not a
 * drag, `escape()` closes something of its own first and says whether it did, `editing(id, slot)` says whether a slot is
 * the one being edited, `reach(at)` takes a click on the capsule at `at` before what it opens. A drag and a way chosen
 * are sent from the seat the host has the line at, whichever view is in charge.
 */
export const hooks = {
  draw() {}, slotClicked: null, escape: () => false, editing: () => false, reach() {},
};

/**
 * Whether something is held, so a redraw would pull it out from under it: an item, a window or the floor by the
 * pointer, or a device's way list, open.
 */
export const busy = () => Boolean(ui.press || ui.grip || ui.pan || document.activeElement?.matches('#windows select'));

export function closeAll() {
  ui.windows.clear();
}

/** Starts a view: its first draw centres the floor on the capsule it is in. */
export function begin() {
  closeAll();
  ui.view = null;
  floorFrom = null;
}

/**
 * Draws the ship's floor, `columns` × `rows` capsules, and the windows open on it. Each of `rooms` is lit: a CabinView
 * and the `look` that names it — `where` in a fixture window's title, `beyond(door)` in a door window's title and
 * `shared(door)` under its slots. Each of `fogged` ({ at, walls }) is drawn as its deck and walls alone, shaded
 * (WEB-7). `heading` is over the floor; `focus` is where the view is, centred on its first draw.
 *
 * The ship is one floor: neighbours share the cells of the wall between them (SHP-8), so each capsule starts a cell
 * short of the last one's end, and a shared cell is drawn once — by a lit room before a fogged one.
 */
export function drawShip({ columns, rows, heading, rooms, fogged, focus }) {
  const windowsChanged = drawWindows(rooms);
  runCycles();
  const from = { frame: line.frame, heading, open: [...ui.windows.keys()].join() };
  if (floorFrom && Object.keys(from).every(k => from[k] === floorFrom[k])) {
    if (windowsChanged) inFrame(drawLeaders);
    return;
  }
  floorFrom = from;
  drawFloor({ columns, rows, heading, rooms, fogged, focus });
  inFrame(drawLeaders);
}

// What the floor was last drawn from — the frame, the heading and the windows open — so a draw between frames passes
// it over: nothing else it shows can have moved.
let floorFrom = null;

/**
 * The floor in 3D (scene.js): its deck, walls, doors and devices handed to the scene, and what each lit device and
 * door shows on its live parts — its lamps, gauges and bars.
 */
function drawFloor({ columns, rows, heading, rooms, fogged, focus }) {
  const n = rooms[0].cabin.cellsAcross, stride = n - 1;
  const across = columns * stride + 1, down = rows * stride + 1;
  const originOf = at => ({ column: at.column * stride, row: at.row * stride });
  const places = [...rooms.map(r => ({ ...foggedOf(r.cabin), room: r })), ...fogged];
  const walls = new Set(places.flatMap(p => p.walls.map(w => cellKey(originOf(p.at), w.area))));
  const floorOf = { n, walls, isWall: (column, row) => walls.has(`${column},${row}`), laid: new Set(), built: new Set() };
  const scene = { cells: [], walls: [], devices: [], parts: [] };
  for (const p of places) placeOn(scene, p, originOf(p.at), floorOf);
  Object.assign(ship, { across, down, cells: n });
  ui.view ??= { column: focus.column * stride + n / 2, row: focus.row * stride + n / 2 };
  const title = floorParts();
  setText(title, heading);
  setScene(scene);
  setLive(new Map(rooms.flatMap(({ cabin }) => [...cabin.fixtures, ...cabin.doors]).map(f => [f.inventory.id, signalsOf(f)])),
    () => ({ nowS: nowS(), rate: line.frame?.rate ?? 0 }));
  setMarks({ hover: ui.hover?.thing ?? 0, open: [...ui.windows.keys()] });
  showView();
}

/**
 * What a fixture's or a door's live parts show (scene.js setLive): whether it runs, how its last cycle ended, whether
 * it is short of the next, its cycle, and how full it is — of its inputs the emptiest, of its outputs the fullest, and
 * of all its slots, each as a share of what they hold at most.
 */
function signalsOf(f) {
  const { slots, stackMost } = f.inventory;
  const share = (from, to) => to > from ? slots.slice(from, to).reduce((sum, s) => sum + s.count, 0) / ((to - from) * stackMost) : 0;
  const shares = use => (f.layout ?? []).filter(g => g.use === use).map(g => share(g.from, g.to));
  const inputs = shares('Input'), outputs = shares('Output');
  return {
    runs: runs(f), last: f.last, short: Boolean(f.shortOf), cycleFromS: f.dueS - f.cycleS, cycleS: f.cycleS,
    input: inputs.length ? Math.min(...inputs) : 0, output: outputs.length ? Math.max(...outputs) : 0,
    held: share(0, slots.length),
  };
}

// The ship's size, in cells across and down, and a capsule's, as the last draw found them.
const ship = { across: 0, down: 0, cells: 0 };

/**
 * The floor's heading and its scene, made on the first draw and kept; the heading returned. A browser with no WebGL2
 * has no floor to draw, and says so where it would be.
 */
function floorParts() {
  const floor = $('floor');
  if (!floor.childElementCount) {
    const scene = drawable() ? sceneCanvas() : Object.assign(document.createElement('p'), {
      className: 'no-scene', textContent: 'floor display offline: this terminal lacks WebGL2',
    });
    floor.append(document.createElement('h2'), scene);
  }
  return floor.querySelector('h2');
}

/**
 * Drags the floor under a held pointer: the ship's cell at the middle of the view follows it, kept on the ship so the
 * ship never leaves the view; with ctrl held or by the right button, turns the camera round it instead (`ui.pan.turn`).
 */
function pan(e) {
  const { x, y, from, turn } = ui.pan;
  ui.pan.last = { x: e.clientX, y: e.clientY };
  const dx = e.clientX - x, dy = e.clientY - y;
  if (!ui.pan.moved && Math.hypot(dx, dy) < DRAG_START_PX) return;
  if (!ui.pan.moved) document.body.classList.add(turn ? 'turning' : 'panning');
  ui.pan.moved = true;
  if (turn) {
    ui.turn = {
      ...ui.turn,
      yaw: (turn.yaw + dx * TURN_DEG_PER_PX) % 360,
      pitch: clamp(turn.pitch + dy * TILT_DEG_PER_PX, PITCH.least, PITCH.most),
    };
  } else {
    const { metresPerPx, ahead, right } = camera();
    const east = (-dx * right[0] + dy * ahead[0]) * metresPerPx, north = (-dx * right[1] + dy * ahead[1]) * metresPerPx;
    ui.view = { column: clamp(from.column + east, 0, ship.across), row: clamp(from.row - north, 0, ship.down) };
  }
  inFrame(showView);
}

// How far the camera turns, and tilts, for a pixel of a turning drag.
const TURN_DEG_PER_PX = .4;
const TILT_DEG_PER_PX = .25;

/** Aims the scene's camera at the ship's cell `ui.view`, turned and tilted as `ui.turn` says, and follows it. */
function showView() {
  aim({ ...ui.view, ...ui.turn, cells: ship.cells });
  drawLeaders();
}

const clamp = (value, least, most) => Math.min(most, Math.max(least, value));

/** A lit cabin as fog shows it: where it is, and its walls and doors alone. */
export const foggedOf = cabin => ({ at: cabin.at, walls: cabin.fixtures.filter(f => STRUCTURE.has(f.kind)) });

// Each open window's leader, by its inventory id: { line, dot }.
const leaders = new Map();
const LEADER_DOT_PX = 3.5;
const SVG = 'http://www.w3.org/2000/svg';

/** A line from each open window to the fixture or door it shows, between their nearest edges. */
function drawLeaders() {
  const ends = new Map();
  for (const id of ui.windows.keys()) {
    const win = document.querySelector(`[data-win="${id}"]`);
    const a = rectOf(id);
    if (!win || !a) continue;
    const b = win.getBoundingClientRect();
    ends.set(id, { from: nearest(a, centre(b)), to: nearest(b, centre(a)) });
  }
  for (const [id, { line, dot }] of leaders) if (!ends.has(id)) {
    line.remove();
    dot.remove();
    leaders.delete(id);
  }
  for (const [id, { from, to }] of ends) {
    if (!leaders.has(id)) {
      const leader = { line: document.createElementNS(SVG, 'line'), dot: document.createElementNS(SVG, 'circle') };
      leader.dot.setAttribute('r', LEADER_DOT_PX);
      $('leaders').append(leader.line, leader.dot);
      leaders.set(id, leader);
    }
    const { line, dot } = leaders.get(id);
    setAttributes(line, { x1: from.x, y1: from.y, x2: to.x, y2: to.y });
    setAttributes(dot, { cx: from.x, cy: from.y });
  }
}

const centre = r => ({ x: (r.left + r.right) / 2, y: (r.top + r.bottom) / 2 });
const nearest = (r, p) => ({ x: Math.min(r.right, Math.max(r.left, p.x)), y: Math.min(r.bottom, Math.max(r.top, p.y)) });

/** A cell's key on the ship's floor: a capsule's own cell `area` from the capsule's `origin`. */
const cellKey = (origin, area) => `${origin.column + area.column},${origin.row + area.row}`;

/**
 * One capsule's part of the ship's floor, from its `origin` there, put in the `scene` (scene.js setScene): its deck but
 * under its walls, each cell not yet `laid` by a neighbour; its walls and doors not yet `built`; and — lit — what stands
 * on it, and on the cap of each of its doors, along its inner edge, the gauge of how full the door is. Lit, everything
 * on it says which capsule it is in (`at`); fogged (WEB-7), every door is shut and nothing answers the pointer.
 */
function placeOn(scene, { at, walls, room }, origin, { n, walls: wallCells, isWall, laid, built }) {
  const lit = room ? at : null;
  const fog = !room;
  const claim = (taken, key) => !taken.has(key) && Boolean(taken.add(key));
  deckOf(n, walls.filter(w => w.kind === DOOR).map(w => w.area)).forEach(({ src, deg, tint }, i) => {
    const area = { column: i % n, row: Math.floor(i / n) }, key = cellKey(origin, area);
    if (wallCells.has(key) || !claim(laid, key)) return;
    scene.cells.push({ column: origin.column + area.column, row: origin.row + area.row, src, deg, tint, fog, at: lit });
  });
  const doors = new Map(room?.cabin.doors.map(d => [d.inventory.id, d]));
  for (const w of walls.filter(w => claim(built, cellKey(origin, w.area)))) {
    const column = origin.column + w.area.column, row = origin.row + w.area.row;
    const door = room && doors.get(w.inventory.id);
    const look = structureLook(column, row, isWall,
      w.kind === DOOR ? { open: Boolean(room) && ui.windows.has(w.inventory.id) } : null);
    const title = !room ? '' : door ? `door ${door.side.toLowerCase()}, ${room.look.beyond(door)}` : nameOf(w.kind);
    scene.walls.push({ column, row, ...look, id: room ? w.inventory.id : null, at: lit, title, fog });
    const gauge = door && doorGaugeOf();
    if (gauge) {
      const [east, north] = INWARD[door.side];
      scene.parts.push({ mesh: gauge, id: w.inventory.id, at: lit, title, turnDeg: east ? 90 : 0,
        atM: [column + CELL_MIDDLE + east * GAUGE_INSET_M, -row - CELL_MIDDLE + north * GAUGE_INSET_M, WALL_HIGH_M] });
    }
  }
  for (const f of room?.cabin.fixtures ?? []) {
    if (STRUCTURE.has(f.kind)) continue;
    const { columns, rows } = f.area;
    const column = origin.column + f.area.column, row = origin.row + f.area.row;
    scene.devices.push({ column, row, columns, rows, mesh: meshOf(f.kind), id: f.inventory.id, at: lit,
      title: nameOf(f.kind) });
  }
}

const DOOR = 'any.door';
const STRUCTURE = new Set(['any.wall', DOOR]);
const CELL_MIDDLE = .5;
// A door's gauge lies along its cap this far in from the middle, toward the room it is in: [east, north] by the wall
// the door is in. It runs along the wall, turned for an east or a west one.
const INWARD = { North: [0, -1], South: [0, 1], East: [-1, 0], West: [1, 0] };
const GAUGE_INSET_M = .36;

const runs = f => f.way != null;
const held = inventory => inventory.slots.reduce((sum, s) => sum + s.count, 0);

/**
 * Every open window the lit rooms hold, by its inventory id — what is not open is not written; `help` is the codex page
 * its `?` opens (WEB-4).
 */
function openable(rooms) {
  const things = new Map();
  for (const { cabin, look } of rooms) {
    for (const f of cabin.fixtures) if (ui.windows.has(f.inventory.id))
      things.set(f.inventory.id, runs(f) ? deviceWindow(f, look) : holderWindow(f));
    for (const d of cabin.doors) if (ui.windows.has(d.inventory.id)) things.set(d.inventory.id, doorWindow(d, look));
  }
  return things;
}

/**
 * The open windows the lit rooms can show, each kept from draw to draw: its panel is its shell, where it stands is set
 * on that, and what it shows is brought up to date inside it. Says whether any changed.
 */
function drawWindows(rooms) {
  const things = openable(rooms);
  const shown = [...ui.windows].filter(([id]) => things.has(id));
  const host = $('windows');
  let changed = reconcile(host, shown.map(([id]) => [id, windowShell(id, things.get(id).paint)]));
  for (const [id, w] of shown) {
    const el = host.querySelector(`:scope > [data-win="${id}"]`);
    changed = placeWindow(el, w) || changed;
    changed = setStyle(el, { zIndex: w.z }) || changed;
    changed = patch(el, windowInner(id, things.get(id))) || changed;
  }
  return changed;
}

// Each cycle bar's animation, and the cycle and rate it was started for.
const cycles = new WeakMap();

/**
 * Runs each open device's cycle bar as an animation in ship time — a ship second a thousand of its milliseconds,
 * played at the ship's rate — so the browser fills it at the display's own rate (WEB-11), off the page's thread, and the page
 * starts one again only for a new cycle or a new rate.
 */
function runCycles() {
  const rate = line.frame?.rate ?? 0;
  for (const bar of document.querySelectorAll('#windows .bar i')) {
    const fromS = Number(bar.dataset.cycleFromS), cycleS = Number(bar.dataset.cycleS);
    const key = `${fromS} ${cycleS} ${rate}`;
    if (cycles.get(bar)?.key === key) continue;
    cycles.get(bar)?.animation.cancel();
    const animation = bar.animate([{ transform: 'scaleX(0)' }, { transform: 'scaleX(1)' }],
      { duration: cycleS * MS_PER_S, fill: 'both' });
    animation.currentTime = (nowS() - fromS) * MS_PER_S;
    animation.playbackRate = rate;
    cycles.set(bar, { key, animation });
  }
}

const MS_PER_S = 1000;

const windowShell = (id, paint) => `<div class="window" data-win="${id}" data-paint="${paint}"></div>`;

const windowInner = (id, { title, where, help, body }) => `<span class="nameplate">${esc(title)}</span>
  <div class="bay"><button class="key-manual" data-go="${help}" title="codex record">?</button>
  <button class="key-close" data-close="${id}" title="close">×</button></div>
  <span class="foot-tag">${where}</span>
  <div class="body">${body}</div>`;

const USE = { Tool: 'tool', Input: 'in', Output: 'out' };

/**
 * A device's window: the way it runs, chosen from every way it can, and its slots as that way lays them out — a row a
 * tool, an input and an output, each slot taking only its item — then its state.
 */
function deviceWindow(f, look) {
  const w = way(f.way);
  const rows = use => f.layout.filter(g => g.use === use)
    .map(g => slotRow(f.inventory, g.from, g.to, `${g.count} ${go(`item:${g.item}`, nameOf(g.item))}${use === 'Tool' ? ', kept' : ' a cycle'}`)).join('');
  const column = use => rows(use) ? `<div class="io"><h3>${USE[use]}</h3>${rows(use)}</div>` : '';
  const closed = f.layout.find(g => g.use === 'Closed');
  const left = closed && f.inventory.slots.slice(closed.from, closed.to).some(s => s.count)
    ? `<div class="labelled"><h3>residue, previous procedure</h3>${slotRow(f.inventory, closed.from, closed.to, 'remove by hand')}</div>` : '';
  const now = nowS();
  const gives = w.gives.map(effectText).join(', ');
  const short = f.shortOf ? `, short: ${go(`item:${f.shortOf}`, nameOf(f.shortOf))}` : '';
  const choices = waysOf(f.kind).map(k => `<option value="${k}"${k === f.way ? ' selected' : ''}>${esc(way(k).name)}</option>`).join('');
  return {
    title: nameOf(f.kind), where: `${codeOf(f.kind)}· ${look.where}`, help: `device:${f.kind}`,
    paint: paintOf(f.kind, roleOf(f.kind), false),
    body: `<label class="pick">procedure <select data-way="${f.inventory.id}">${choices}</select></label>
      <div class="machine">
      ${column('Tool')}${column('Input') || '<div class="io"><h3>in</h3><div class="none">no input</div></div>'}
      <div class="process"><span class="arrow">→</span><div class="bar"><i data-cycle-from-s="${f.dueS - f.cycleS}" data-cycle-s="${
        f.cycleS}"></i></div>
        <small>cycle ${f.cycleS} s</small></div>
      ${column('Output') || `<div class="io"><h3>out</h3><div class="none">${gives || 'no output'}</div></div>`}</div>${left}
      <dl class="form">
        <dt>last cycle</dt><dd class="state ${f.last}">${STATE[f.last]}</dd>
        ${gives ? `<dt>effect</dt><dd>${gives}</dd>` : ''}
        <dt>next cycle</dt><dd>t−${Math.max(0, f.dueS - now).toFixed(0)} s${short}</dd>
      </dl>`,
  };
}

/** A fixture that runs no way only holds things: a chest, a locker. */
function holderWindow(f) {
  return {
    title: nameOf(f.kind), where: `${codeOf(f.kind)}· ${held(f.inventory)} units held`, help: `device:${f.kind}`,
    paint: paintOf(f.kind, roleOf(f.kind), true),
    body: slotGrid(f.inventory, CHEST_SLOTS_ACROSS),
  };
}

function doorWindow(d, look) {
  return {
    title: `door ${d.side.toLowerCase()}`, where: look.beyond(d), help: 'page:doors', paint: doorPaint(),
    body: `${slotGrid(d.inventory, Math.round(Math.sqrt(d.inventory.slots.length)))}
      <p class="note">${look.shared(d)}</p>`,
  };
}

function slotGrid(inventory, across) {
  const slots = inventory.slots.map((s, i) => slotHtml(inventory, i)).join('');
  return `<div class="slots" style="grid-template-columns: repeat(${across}, var(--slot-px))">${slots}</div>`;
}

function slotRow(inventory, from, to, caption) {
  let slots = '';
  for (let i = from; i < to; i++) slots += slotHtml(inventory, i);
  return `<div class="labelled"><div class="row">${slots}</div><small>${caption}</small></div>`;
}

/**
 * One slot, carrying its filter as `data-accepts` ("*" for universal, else the items it takes by hand, "" for none) so a
 * drag can show which slots would refuse what it holds; the game's own `Move` is still what decides.
 */
function slotHtml(inventory, i) {
  const s = inventory.slots[i];
  const accepts = s.universal ? '*' : s.accepts.join(' ');
  const wanted = !s.universal && s.accepts.length === 1 ? s.accepts[0] : null;
  const wants = wanted ? ` wants" style="--tag: ${chipLook(wanted).tag}` : '';
  const inside = s.count ? chipHtml(s.item, s.count) : wanted ? chipLook(wanted).label : s.universal || s.accepts.length ? '' : 'out';
  const editing = hooks.editing(inventory.id, i) ? ' editing' : '';
  const title = s.count ? nameOf(s.item) : wanted ? `for ${nameOf(wanted)}` : '';
  return `<div class="slot${s.accepts.length || s.universal ? '' : ' out'}${editing}${wants}" data-inv="${inventory.id}"
    data-slot="${i}" data-accepts="${accepts}" title="${esc(title)}">${inside}</div>`;
}

/** An item's chip: its letters on its section's tag colour, and the count. A right-click opens its codex page. */
export function chipHtml(item, count) {
  const { label, tag } = chipLook(item);
  return `<div class="chip" style="--tag: ${tag}" data-item="${item}">${label}<em>${count}</em></div>`;
}

const accepts = (slot, item) => slot.dataset.accepts === '*' || slot.dataset.accepts.split(' ').includes(item);

/** Opens the window of `id` beside `near`, the box on the page round what was clicked. */
function open(id, near) {
  ui.windows.set(id, { x: near.right + WINDOW_OFFSET_PX, y: near.top, z: ++ui.topZ });
  hooks.draw();
  place(id, near);
}

/**
 * Puts a new window beside what opened it — right, left, below, above — at the first spot that is on the page and
 * covers no other open window; failing that, the first spot on the page.
 */
function place(id, near) {
  const w = ui.windows.get(id);
  const el = document.querySelector(`[data-win="${id}"]`);
  const width = el.offsetWidth, height = el.offsetHeight;
  const spots = [
    { x: near.right + WINDOW_OFFSET_PX, y: near.top },
    { x: near.left - width - WINDOW_OFFSET_PX, y: near.top },
    { x: near.left, y: near.bottom + WINDOW_OFFSET_PX },
    { x: near.left, y: near.top - height - WINDOW_OFFSET_PX },
  ];
  const onPage = s => s.x >= WINDOW_MARGIN_PX && s.y >= WINDOW_MARGIN_PX
    && s.x + width <= innerWidth - WINDOW_MARGIN_PX && s.y + height <= innerHeight - WINDOW_MARGIN_PX;
  const others = [...document.querySelectorAll('.window')].filter(o => o !== el).map(o => o.getBoundingClientRect());
  const clear = s => others.every(o => s.x >= o.right || s.x + width <= o.left || s.y >= o.bottom || s.y + height <= o.top);
  const spot = spots.find(s => onPage(s) && clear(s)) ?? spots.find(onPage) ?? spots[0];
  Object.assign(w, spot);
  keepOnPage(id);
}

/** Moves a window back inside the page if it spills over an edge, once its size is known. */
function keepOnPage(id) {
  const w = ui.windows.get(id);
  const el = document.querySelector(`[data-win="${id}"]`);
  if (!w || !el) return;
  Object.assign(w, keepInside(el, w.x, w.y, WINDOW_MARGIN_PX));
  placeWindow(el, w);
  inFrame(drawLeaders);
}

function raise(el) {
  const w = ui.windows.get(Number(el.dataset.win));
  if (!w || w.z === ui.topZ) return;
  w.z = ++ui.topZ;
  setStyle(el, { zIndex: w.z });
}

document.addEventListener('click', e => {
  if (ui.panned) return void (ui.panned = false);
  const close = e.target.closest('[data-close]');
  if (close) {
    ui.windows.delete(Number(close.dataset.close));
    return hooks.draw();
  }
  if (e.target.closest('#floor canvas')) pick(e.clientX, e.clientY).then(clicked);
});

/** A click on the floor, on `hit` (scene.js `pick`): opens what it is on, or closes it if open. */
function clicked(hit) {
  if (!hit) return;
  if (hit.at) hooks.reach(hit.at);
  if (hit.id == null) return;
  if (ui.windows.has(hit.id)) {
    ui.windows.delete(hit.id);
    hooks.draw();
  } else open(hit.id, rectOf(hit.id));
}

document.addEventListener('change', e => {
  const choice = e.target.closest('#windows [data-way]');
  if (!choice) return;
  send('select', { inventory: Number(choice.dataset.way), way: Number(choice.value) });
  choice.blur();
  hooks.draw();
});

document.addEventListener('contextmenu', e => {
  // The right button turns the floor's camera: it opens no menu there.
  if (e.target.closest('#floor')) return void e.preventDefault();
  const chip = e.target.closest('[data-item]');
  if (!chip) return;
  e.preventDefault();
  openCodex(`item:${chip.dataset.item}`);
});

document.addEventListener('keydown', e => {
  if (e.key !== 'Escape' || hooks.escape() || !ui.windows.size) return;
  const [top] = [...ui.windows].reduce((a, b) => (b[1].z > a[1].z ? b : a));
  ui.windows.delete(top);
  hooks.draw();
});

document.addEventListener('pointerdown', e => {
  ui.panned = false;
  if (ui.view && e.target.closest('#floor') && pinchStarts(e)) return;
  if (!ui.pan && ui.view && (e.button === 0 || e.button === 2) && e.target.closest('#floor')) {
    const turn = e.ctrlKey || e.button === 2 ? { ...camera() } : null;
    ui.pan = { id: e.pointerId, x: e.clientX, y: e.clientY, from: ui.view, turn, moved: false };
    if (turn) e.preventDefault();
    return;
  }
  const win = e.target.closest('#windows > .window');
  if (win) raise(win);
  const slot = e.target.closest('.slot');
  if (slot) {
    const chip = slot.querySelector('.chip');
    ui.press = { inv: Number(slot.dataset.inv), slot: Number(slot.dataset.slot), x: e.clientX, y: e.clientY, el: slot, chip, ghost: null };
    return e.preventDefault();
  }
  if (win && !e.target.closest(CONTROLS)) {
    const w = ui.windows.get(Number(win.dataset.win));
    ui.grip = { el: win, w, dx: e.clientX - w.x, dy: e.clientY - w.y };
    e.preventDefault();
  }
});

// A pointer event only records where the pointer is; what follows it is drawn in the next frame (inFrame).
document.addEventListener('pointermove', e => {
  if (ui.pinch?.at.has(e.pointerId)) return pinch(e);
  if (ui.pan) return void (e.pointerId === ui.pan.id && pan(e));
  if (ui.grip) {
    const { w, dx, dy } = ui.grip;
    w.x = e.clientX - dx;
    w.y = e.clientY - dy;
    return inFrame(moveGripped);
  }
  const press = ui.press;
  if (!press && e.target.closest?.('#floor canvas')) {
    ui.pointer = { clientX: e.clientX, clientY: e.clientY };
    return inFrame(pointAt);
  }
  if (!press?.chip) return;
  if (!press.ghost) {
    if (Math.hypot(e.clientX - press.x, e.clientY - press.y) < DRAG_START_PX) return;
    press.ghost = press.chip.cloneNode(true);
    press.ghost.classList.add('ghost');
    document.body.append(press.ghost);
    press.half = { x: press.ghost.offsetWidth / 2, y: press.ghost.offsetHeight / 2 };
    document.querySelectorAll('.slot').forEach(s => s.classList.toggle('refuses', !accepts(s, press.chip.dataset.item)));
  }
  press.at = { clientX: e.clientX, clientY: e.clientY };
  inFrame(moveGhost);
});

/**
 * Lights what the pointer is over on the floor, and names it as a title does: read from the picture without waiting on
 * it, so an answer older than one already shown is passed over.
 */
function pointAt() {
  if (!ui.pointer || ui.pan) return;
  const asked = ++ui.pointsAsked;
  pick(ui.pointer.clientX, ui.pointer.clientY).then(hit => {
    if (asked < ui.pointsShown || ui.pan) return;
    ui.pointsShown = asked;
    showPointed(hit);
  });
}

function showPointed(hit) {
  const thing = hit?.id != null || hit?.title ? hit.thing : 0;
  if ((ui.hover?.thing ?? 0) === thing) return;
  ui.hover = thing ? hit : null;
  const canvas = $('floor').querySelector('canvas');
  canvas.title = ui.hover?.title ?? '';
  canvas.classList.toggle('pointing', Boolean(ui.hover?.id != null));
  setMarks({ hover: thing, open: [...ui.windows.keys()] });
}

function moveGripped() {
  if (!ui.grip) return;
  placeWindow(ui.grip.el, ui.grip.w);
  drawLeaders();
}

/** Moves the dragged item's ghost to the pointer, and marks the slot under it. */
function moveGhost() {
  const press = ui.press;
  if (!press?.ghost) return;
  setStyle(press.ghost, { translate: `${press.at.clientX - press.half.x}px ${press.at.clientY - press.half.y}px` });
  const under = slotUnder(press.at);
  if (under === press.target) return;
  press.target?.classList.remove('target');
  under?.classList.add('target');
  press.target = under;
}

/** Puts a window where its `w` says, as a move of its layer alone: nothing is laid out again. */
const placeWindow = (el, w) => setStyle(el, { translate: `${w.x}px ${w.y}px` });

/** Lets go of the floor; a release that dragged it is not a click on what it ends over. */
function release(e) {
  if (e.pointerId !== ui.pan.id) return;
  ui.panned = ui.pan.moved;
  ui.pan = null;
  document.body.classList.remove('panning', 'turning');
}

document.addEventListener('pointercancel', e => {
  if (ui.pinch?.at.has(e.pointerId)) return unpinch();
  if (ui.pan) release(e);
});

document.addEventListener('pointerup', e => {
  if (ui.pinch?.at.has(e.pointerId)) return unpinch();
  if (ui.pan) return release(e);
  if (ui.grip) {
    keepOnPage(Number(ui.grip.el.dataset.win));
    ui.grip = null;
    return;
  }
  const press = ui.press;
  if (!press) return;
  ui.press = null;
  press.ghost?.remove();
  press.target?.classList.remove('target');
  const onto = press.ghost && slotUnder(e);
  if (onto) send('move', { from: press.inv, fromSlot: press.slot, to: Number(onto.dataset.inv), toSlot: Number(onto.dataset.slot) });
  else if (!press.ghost) hooks.slotClicked?.(press.el);
  hooks.draw();
});

function slotUnder({ clientX, clientY }) {
  return document.elementFromPoint(clientX, clientY)?.closest('.slot') ?? null;
}

// The camera is fitted to the floor, so a new size moves everything the lamps, tags and leaders were laid on.
addEventListener('resize', () => inFrame(showView));

// The wheel brings the camera nearer or further; not over a window, whose own content it scrolls.
document.addEventListener('wheel', e => {
  if (!ui.view || !e.target.closest('#floor')) return;
  e.preventDefault();
  const px = e.deltaY * (e.deltaMode === WheelEvent.DOM_DELTA_LINE ? WHEEL_LINE_PX : 1);
  zoomAt(e.clientX, e.clientY, Math.exp(-px * ZOOM_PER_PX));
}, { passive: false });

// How much nearer the camera comes for a pixel of wheel, and the pixels a wheel's line is.
const ZOOM_PER_PX = .0015;
const WHEEL_LINE_PX = 16;

/**
 * Brings the camera `factor` times nearer, within its range, keeping the point of the deck under the page's
 * `clientX`, `clientY` where it is, so the floor closes in on what is pointed at.
 */
function zoomAt(clientX, clientY, factor) {
  const before = deckAt(clientX, clientY);
  const zoom = clamp((ui.turn?.zoom ?? ZOOM.start) * factor, ZOOM.least, ZOOM.most);
  ui.turn = { ...ui.turn, zoom };
  aim({ ...ui.view, ...ui.turn, cells: ship.cells });
  const after = deckAt(clientX, clientY);
  if (before && after) ui.view = {
    column: clamp(ui.view.column + before.column - after.column, 0, ship.across),
    row: clamp(ui.view.row + before.row - after.row, 0, ship.down),
  };
  inFrame(showView);
}

/**
 * A second finger down on the floor while one pans it starts a pinch: from then the two fingers' spread zooms the
 * camera, about the point between them, their twist turns it so the floor follows the fingers round, and the point
 * between them moved up or down tilts it as a turning drag does; neither pans. Says whether it started one.
 */
function pinchStarts(e) {
  if (e.pointerType !== 'touch' || !ui.pan || ui.pan.id === e.pointerId) return false;
  const at = new Map([[ui.pan.id, { x: ui.pan.last?.x ?? ui.pan.x, y: ui.pan.last?.y ?? ui.pan.y }],
    [e.pointerId, { x: e.clientX, y: e.clientY }]]);
  ui.pan = null;
  ui.pinch = { at, spread: spreadOf(at), angle: angleOf(at), middle: middleOf(at) };
  document.body.classList.add('turning');
  return true;
}

function pinch(e) {
  ui.pinch.at.set(e.pointerId, { x: e.clientX, y: e.clientY });
  const spread = spreadOf(ui.pinch.at), angle = angleOf(ui.pinch.at), middle = middleOf(ui.pinch.at);
  const { yaw, pitch } = camera();
  // The camera turned clockwise turns the floor the other way on the page.
  const twistDeg = ((angle - ui.pinch.angle) * 180 / Math.PI + 540) % 360 - 180;
  ui.turn = {
    ...ui.turn,
    yaw: (yaw - twistDeg + 360) % 360,
    pitch: clamp(pitch + (middle.y - ui.pinch.middle.y) * TILT_DEG_PER_PX, PITCH.least, PITCH.most),
  };
  zoomAt(middle.x, middle.y, spread / ui.pinch.spread);
  Object.assign(ui.pinch, { spread, angle, middle });
}

/** Ends a pinch: what it ends over is not clicked. */
function unpinch() {
  ui.pinch = null;
  ui.panned = true;
  document.body.classList.remove('turning');
}

const angleOf = at => {
  const [a, b] = [...at.values()];
  return Math.atan2(b.y - a.y, b.x - a.x);
};

const middleOf = at => {
  const [a, b] = [...at.values()];
  return { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };
};

const spreadOf = at => {
  const [a, b] = [...at.values()];
  return Math.max(Math.hypot(a.x - b.x, a.y - b.y), 1);
};
