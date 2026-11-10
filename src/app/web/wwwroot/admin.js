import { $, hooks, drawShip, begin, closeAll, foggedOf, chipHtml, busy } from './cabin.js'
import { line, open, send } from './host.js'
import { sit, refused, clockText } from './player.js'
import { nameOf, allItems, loaded } from './codex.js'
import { patch, setStyle, setText } from './dom.js'

// The rates the admin may run ship time at, in ship seconds a real second.
const PAUSED_RATE = 0, PLAIN_RATE = 1, FAST_RATE = 10, FASTER_RATE = 100;
const RATES = [[PAUSED_RATE, 'halt'], [PLAIN_RATE, `×${PLAIN_RATE}`], [FAST_RATE, `×${FAST_RATE}`], [FASTER_RATE, `×${FASTER_RATE}`]];
// The slot editor opens this far below the slot it edits, and lists at most this many items a search finds.
const EDITOR_GAP_PX = 6;
const EDITOR_FINDS_MOST = 12;

// ship: the last frame's ShipView, its `entered` the capsule the host has this line in. editing: { id, slot, item,
// query, refused } of the slot edited.
const admin = { started: false, ship: null, editing: null };
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);
const same = (a, b) => a.column === b.column && a.row === b.row;

/** What the admin is told: where each capsule is and which is beyond each door (WEB-8, WEB-2). */
const look = at => ({
  where: `capsule ${at.column}·${at.row}`,
  beyond: d => `to capsule ${d.beyond.column}·${d.beyond.row}`,
  shared: d => `Shared with capsule ${d.beyond.column}·${d.beyond.row}. Items left here may be taken by its operator.`,
});

export function startAdmin() {
  admin.started = true;
  inspect();
  open('admin', () => busy() || hooks.draw(), refused);
}

/** Asks the host to enter the capsule at `at`, unless the line is in it: its moves are made from there. */
function enter(at) {
  if (admin.ship && same(admin.ship.entered, at)) return;
  closeAll();
  admin.editing = null;
  send('enter', at);
}

/** Inspects the ship: every capsule's floor lit, the entered one's seat making the moves, every slot open to an edit. */
function inspect() {
  begin();
  admin.editing = null;
  document.body.className = 'admin';
  patch($('controls'), RATES.map(([rate, label]) => `<button data-rate="${rate}">${label}</button>`).join('')
    + `<button data-play title="operate the entered capsule as its operator sees it">operate seat</button>`);
  setText($('hint'), 'Supervisor access. Click a capsule to enter it; drag the deck to pan, right-drag to turn, wheel to zoom. Drag items as its '
    + 'operator would; click a slot to set its contents. Esc closes the editor, then a panel.');
  Object.assign(hooks, {
    draw,
    move: (from, fromSlot, to, toSlot) => send('move', { from, fromSlot, to, toSlot }),
    select: (inventory, way) => send('select', { inventory, way }),
    slotClicked: edit,
    escape: closeEditor,
    editing: (id, slot) => admin.editing?.id === id && admin.editing.slot === slot,
    reach: enter,
  });
  draw();
}

/** Plays the entered capsule as its player would see it — the rest of the ship under fog — with a way back. */
function play() {
  const at = admin.ship.entered;
  sit(({ ship }) => ({
    columns: ship.columns, rows: ship.rows,
    cabin: ship.cabins.find(c => same(c.at, at)),
    fogged: ship.cabins.filter(c => !same(c.at, at)).map(foggedOf),
  }));
  patch($('controls'), '<button data-back>exit seat</button>');
  setText($('hint'), `Operating capsule ${at.column}·${at.row} as its operator sees it.`);
  $('editor').hidden = true;
}

function draw() {
  if (!line.frame || !loaded()) return;
  const ship = admin.ship = line.frame.ship;
  const all = ship.cabins.length, failing = ship.cabins.filter(c => c.failing).length;
  setText($('clock'), clockText());
  setText($('status'), failing ? `life support failing ${failing}/${all}` : `life support nominal ${all}/${all}`);
  $('status').classList.toggle('alarm', failing > 0);
  document.querySelectorAll('[data-rate]').forEach(b => b.classList.toggle('on', Number(b.dataset.rate) === line.frame.rate));
  const { entered } = ship;
  drawShip({
    columns: ship.columns, rows: ship.rows, heading: `Capsule ${entered.column}·${entered.row} entered`,
    rooms: ship.cabins.map(cabin => ({ cabin, look: look(cabin.at) })), fogged: [], focus: entered,
  });
  drawEditor();
}

function edit(slotEl) {
  const id = Number(slotEl.dataset.inv), slot = Number(slotEl.dataset.slot);
  const s = slotOf(id, slot);
  const one = mayHold(s)?.length === 1 ? mayHold(s)[0] : null;
  admin.editing = { id, slot, item: s.count ? s.item : one, query: '', refused: false };
}

/** Slot `slot` of inventory `id`, in whichever cabin holds it. */
function slotOf(id, slot) {
  return admin.ship.cabins.flatMap(c => [...c.fixtures, ...c.doors]).find(thing => thing.inventory.id === id)
    ?.inventory.slots[slot];
}

/**
 * What an edit may set a slot to, as the game's `Set` allows: a device slot its one item (none for a closed one), any
 * other its filter's — and null for a universal slot, which takes any item of the codex, found by a search.
 */
const mayHold = s => s.holds != null ? (s.holds ? [s.holds] : []) : s.universal ? null : s.accepts;

/** The items a universal slot's search finds, by name or id. */
function found(query) {
  const q = query.trim().toLowerCase();
  if (!q) return [];
  return allItems().filter(i => i.id.includes(q) || i.name.toLowerCase().includes(q)).slice(0, EDITOR_FINDS_MOST).map(i => i.id);
}

/**
 * The slot editor, under the slot it edits; closed once that slot's window is. A field being typed in keeps what is
 * typed, so a redraw does not take it from under the cursor.
 */
function drawEditor() {
  const el = $('editor');
  const e = admin.editing;
  const slotEl = e && document.querySelector(`#windows .slot[data-inv="${e.id}"][data-slot="${e.slot}"]`);
  if (!slotEl) {
    admin.editing = null;
    if (!el.hidden) el.hidden = true;
    return;
  }
  if (el.hidden) el.hidden = false;
  patch(el, editorHtml(e));
  const near = slotEl.getBoundingClientRect();
  setStyle(el, {
    left: `${Math.max(0, Math.min(near.left, innerWidth - el.offsetWidth))}px`,
    top: `${Math.max(0, Math.min(near.bottom + EDITOR_GAP_PX, innerHeight - el.offsetHeight))}px`,
  });
}

/** The editor: the items the slot may hold — found by a search for a universal slot — and its count. */
function editorHtml(e) {
  const s = slotOf(e.id, e.slot);
  const choices = mayHold(s) ?? found(e.query);
  const swatch = item => `<button class="swatch${item === e.item ? ' on' : ''}" data-edit-item="${item}"
    title="${esc(nameOf(item))}">${chipHtml(item, '')}<span>${esc(nameOf(item))}</span></button>`;
  const search = mayHold(s) ? '' : `<div class="row"><input type="search" class="find" placeholder="query: name or stock code"
    value="${esc(e.query)}" data-edit-find></div>`;
  const off = e.item ? '' : ' disabled';
  return `<div class="titlebar"><b>slot ${e.slot}</b><span>${s.count ? `${s.count} ${esc(nameOf(s.item))}` : 'empty'}</span>
      <button data-edit-close title="close">×</button></div>
    <div class="body">
      ${search}<div class="row picks">${choices.map(swatch).join('') || `<span class="note">${mayHold(s)
        ? 'slot accepts nothing' : e.query.trim() ? 'no record matches' : 'any item: query part of its name or stock code'}</span>`}</div>
      <div class="row">${e.item ? `setting ${esc(nameOf(e.item))}` : 'select an item'}</div>
      <div class="row"><button data-step="-1"${off}>−</button>
        <input type="number" min="0" max="${admin.ship.stackMost}" value="${s.count}" data-count${off}>
        <button data-step="1"${off}>+</button><button data-fill${off}>full</button><button data-empty>empty</button></div>
      ${e.refused ? '<p class="note alarm">edit refused</p>' : ''}
    </div>`;
}

/** Sets the edited slot to `count` of the editor's item, clamped to a stack. */
async function setCount(count) {
  const e = admin.editing;
  const clamped = Math.max(0, Math.min(admin.ship.stackMost, count));
  const taken = await send('set', { inventory: e.id, slot: e.slot, item: e.item ?? '', count: clamped });
  if (admin.editing !== e) return;
  e.refused = !taken;
  hooks.draw();
}

document.addEventListener('click', e => {
  if (!admin.started) return;
  if (e.target.closest('[data-play]')) return play();
  if (e.target.closest('[data-back]')) return inspect();
  const rate = e.target.closest('[data-rate]');
  if (rate) return send('rate', { rate: Number(rate.dataset.rate) });

  const edited = admin.editing;
  if (!edited) return;
  const s = slotOf(edited.id, edited.slot);
  const item = e.target.closest('[data-edit-item]');
  if (item) {
    edited.item = item.dataset.editItem;
    return setCount(Math.max(1, s.count));
  }
  const step = e.target.closest('[data-step]');
  if (step) return setCount(s.count + Number(step.dataset.step));
  if (e.target.closest('[data-fill]')) return setCount(admin.ship.stackMost);
  if (e.target.closest('[data-empty]')) return setCount(0);
  if (e.target.closest('[data-edit-close]')) closeEditor();
});

/** Closes the slot editor, saying whether it was open. */
function closeEditor() {
  if (!admin.editing) return false;
  admin.editing = null;
  draw();
  return true;
}

document.addEventListener('input', e => {
  if (!admin.editing || !e.target.matches('#editor [data-edit-find]')) return;
  admin.editing.query = e.target.value;
  patch($('editor'), editorHtml(admin.editing));
});

document.addEventListener('change', e => {
  if (admin.editing && e.target.matches('#editor [data-count]')) {
    setCount(Number(e.target.value));
    e.target.blur();
  }
});
