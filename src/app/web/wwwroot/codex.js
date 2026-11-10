// The codex: a page for every item and device the game holds and for how the ship works (WEB-3, WEB-5), in one window
// that keeps its own history and is dragged by its title bar (WEB-6). Its words and data are the game's own
// (`codex.json`, which the host makes from what it runs, fetched once), so nothing here can fall behind the ship. A link anywhere on the page —
// `data-go="item:wat-001"` — opens its page here.

import { $, esc, inFrame, keepInside, patch, setStyle } from './dom.js'

// A long list shows this many before a "show all".
const LIST_FIRST = 40;
// The search lists at most this many hits.
const SEARCH_MOST = 60;
// The window opens this far in from the page's right edge and below its header.
const OPEN_INSET_PX = 24;
const MARGIN_PX = 8;

const book = {
  data: null,
  items: new Map(), devices: new Map(), subs: new Map(), sections: new Map(), roles: new Map(), stats: new Map(),
  pages: new Map(),
  // item id → way indices that make, take or need it; device id → the ways it runs.
  madeBy: new Map(), takenBy: new Map(), neededBy: new Map(), waysBy: new Map(),
  // item id → items whose use leaves it, items that decay into it; device id → parts that fit, kits that install it.
  leftBy: new Map(), decayOf: new Map(), fittedBy: new Map(), installedBy: new Map(),
};

// history: the targets read, `at` the one shown. more: the lists opened past their first LIST_FIRST.
const view = { open: false, x: 0, y: 0, history: [], at: -1, more: new Set(), query: '', grip: null };

const push = (map, key, value) => (map.get(key) ?? map.set(key, []).get(key)).push(value);

/** Takes the game's codex (a CodexBook) and indexes it both ways: what makes, takes and needs each item. */
export function loadCodex(data) {
  book.data = data;
  for (const i of data.items) book.items.set(i.id, i);
  for (const d of data.devices) book.devices.set(d.id, d);
  for (const s of data.subsections) book.subs.set(s.code, s);
  for (const s of data.sections) book.sections.set(s.id, s);
  for (const r of data.roles) book.roles.set(r.id, r);
  for (const s of data.stats) book.stats.set(s.id, s);
  for (const p of data.pages) book.pages.set(p.slug, p);
  data.ways.forEach((w, k) => {
    for (const c of w.makes) push(book.madeBy, c.item, k);
    for (const c of w.takes) push(book.takenBy, c.item, k);
    for (const c of w.needs) push(book.neededBy, c.item, k);
    push(book.waysBy, w.by, k);
  });
  for (const i of data.items) {
    for (const c of i.leaves) push(book.leftBy, c.item, i.id);
    if (i.decaysTo) push(book.decayOf, i.decaysTo, i.id);
    for (const d of i.fits) push(book.fittedBy, d, i.id);
    for (const d of i.installs) push(book.installedBy, d, i.id);
  }
}

/** Whether the codex has come, so names can be looked up. */
export const loaded = () => book.data !== null;

/** What the game calls an item or a device, by its id. */
export const nameOf = id => book.items.get(id)?.name ?? book.devices.get(id)?.name ?? id;

/** A device's role, by its id. */
export const roleOf = id => book.devices.get(id)?.role;

/** The ways a device runs, as indices into the codex's ways, in the order the game holds them. */
export const waysOf = deviceId => book.waysBy.get(deviceId) ?? [];

export const way = k => book.data.ways[k];

// The stylesheet's item tag colours, `--tag-0` on: one a section, round again past the last.
const TAGS = 12;

/** How an item's chip looks: up to two letters of its name, and its section's tag colour, as a CSS value. */
export function chipLook(id) {
  const item = book.items.get(id);
  if (!item) return { label: '?', tag: 'var(--tag-9)' };
  const words = item.name.split(/[\s,]+/).filter(Boolean);
  const label = (words.length > 1 ? words[0][0] + words[1][0] : item.name.slice(0, 2)).toUpperCase();
  const at = book.data.sections.findIndex(s => s.id === book.subs.get(item.sub)?.section);
  return { label, tag: `var(--tag-${Math.max(0, at) % TAGS})` };
}

/** An id printed as the stock code it reads as on a tag. */
export const codeOf = id => `<span class="code">${esc(id.toUpperCase())}</span>`;

/** Every item whose id or name holds `query`, lower-cased and trimmed by the caller. */
export const itemsMatching = q => book.data.items.filter(i => i.id.includes(q) || i.name.toLowerCase().includes(q));

/** A link to a codex page. */
export const go = (target, words) => `<a class="go" data-go="${esc(target)}">${esc(words)}</a>`;
const coded = (target, id) => `<a class="go" data-go="${esc(target)}">${codeOf(id)}${esc(nameOf(id))}</a>`;
const itemLink = id => coded(`item:${id}`, id);
const deviceLink = id => id === book.data.byHand ? 'operator, by hand' : coded(`device:${id}`, id);
const subLink = u => `<a class="go" data-go="sub:${esc(u.code)}">${codeOf(u.code)}${esc(u.name)}</a>`;

/** Opens the codex at `target` ("item:wat-001", "device:any.chest", "page:doors", or "home"). */
export function openCodex(target = 'home') {
  if (!view.open) {
    view.open = true;
    view.x = innerWidth - $('codex').offsetWidth - OPEN_INSET_PX;
    view.y = document.querySelector('header').getBoundingClientRect().bottom + MARGIN_PX;
  }
  if (view.history[view.at] !== target) {
    view.history = view.history.slice(0, view.at + 1).concat(target);
    view.at = view.history.length - 1;
  }
  draw();
}

function step(by) {
  const to = view.at + by;
  if (to < 0 || to >= view.history.length) return;
  view.at = to;
  draw();
}

function close() {
  view.open = false;
  $('codex').hidden = true;
}

function draw() {
  const el = $('codex');
  const target = view.history[view.at] ?? 'home';
  const { title, body } = page(target);
  el.hidden = false;
  patch(el, `<div class="titlebar" data-codex-grip>
      <button data-codex-step="-1" title="back (Alt ←)"${view.at > 0 ? '' : ' disabled'}>←</button>
      <button data-codex-step="1" title="forward (Alt →)"${view.at < view.history.length - 1 ? '' : ' disabled'}>→</button>
      <button data-go="home" title="index">⌂</button>
      <b>${esc(title)}</b><span>codex · ops manual rev 7</span>
      <button data-codex-close title="close">×</button></div>
    <div class="search"><input type="search" placeholder="query: name or stock code" value="${esc(view.query)}"
      data-codex-find></div>
    <div class="body">${body}</div>`);
  el.querySelector('.body').scrollTop = 0;
  keepOnPage();
}

function keepOnPage() {
  Object.assign(view, keepInside($('codex'), view.x, view.y, MARGIN_PX));
  place();
}

/** Puts the codex where `view` says, as a move of its layer alone (WEB-11). */
const place = () => setStyle($('codex'), { translate: `${view.x}px ${view.y}px` });

function page(target) {
  const colon = target.indexOf(':');
  const [kind, id] = colon < 0 ? [target, ''] : [target.slice(0, colon), target.slice(colon + 1)];
  const draw = { home, item: itemPage, device: devicePage, page: textPage, section: sectionPage, sub: subPage,
    role: rolePage, stat: statPage, find: findPage }[kind];
  return draw?.(id) ?? { title: 'no record', body: `<p class="note">No codex record for ${esc(target)}.</p>` };
}

function home() {
  const sections = book.data.sections.map(s => `<li>${go(`section:${s.id}`, s.name)} <small>${esc(s.serves)}</small><br>
    ${book.data.subsections.filter(u => u.section === s.id).map(subLink).join(' · ')}</li>`).join('');
  const pages = book.data.pages.map(p => go(`page:${p.slug}`, p.title)).join(' · ');
  return {
    title: 'Index',
    body: `<p>${pages}</p>
      <h3>Catalogue</h3><ul class="plain">${sections}</ul>
      <h3>Roles</h3><p>${book.data.roles.map(r => go(`role:${r.id}`, r.name)).join(' · ')}</p>
      <h3>Stats</h3><p>${book.data.stats.map(s => go(`stat:${s.id}`, s.id)).join(' · ')}</p>`,
  };
}

/** One of the codex's own pages: paragraphs and lists, its links and figures filled in. */
function textPage(slug) {
  const p = book.pages.get(slug);
  if (!p) return null;
  const html = p.text.split(/\n\s*\n/).map(block => {
    const lines = block.split('\n');
    if (lines.every(l => l.startsWith('- '))) return `<ul>${lines.map(l => `<li>${inline(l.slice(2))}</li>`).join('')}</ul>`;
    return `<p>${inline(lines.join(' '))}</p>`;
  }).join('');
  const extra = slug === 'stats' ? `<p>${book.data.stats.map(s => go(`stat:${s.id}`, s.id)).join(' · ')}</p>`
    : slug === 'roles' ? `<p>${book.data.roles.map(r => go(`role:${r.id}`, r.name)).join(' · ')}</p>` : '';
  return { title: p.title, body: html + extra };
}

function inline(text) {
  return esc(text)
    .replace(/\[\[([a-z]+):([^\]|]+)(?:\|([^\]]*))?\]\]/g, (_, kind, id, words) => go(`${kind}:${id}`, words ?? nameOf(id)))
    .replace(/\{([A-Za-z]+)\}/g, (m, name) => name in book.data.figures ? String(book.data.figures[name]) : m)
    .replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>');
}

/** What kind an item is, as the catalogue's tables imply it. */
function kindOf(i) {
  if (i.installs.length) return 'kit';
  if (i.fits.length) return 'spare part';
  if (i.effects.some(e => e.perHour)) return 'durable';
  if (i.effects.length) return 'consumable';
  return book.neededBy.has(i.id) ? 'tool' : 'resource';
}

const signed = n => (n > 0 ? '+' : '') + n;

/** A stat effect as printed: `cabin.o2 +2`. */
export const effectText = e => `${e.stat} ${signed(e.amount)}`;
const statLink = (e, perHour) => go(`stat:${e.stat}`, `${effectText(e)}${perHour ? '/h' : ''}`);

function itemPage(id) {
  const i = book.items.get(id);
  if (!i) return null;
  const sub = book.subs.get(i.sub);
  const facts = [];
  if (i.effects.length) facts.push(['use', i.effects.map(e => statLink(e, e.perHour)).join(', ')]);
  if (i.leaves.length) facts.push(['leaves', i.leaves.map(c => `${c.count} × ${itemLink(c.item)}`).join(', ')]);
  if (i.fits.length) facts.push(['fits', i.fits.map(deviceLink).join(', ')]);
  if (i.installs.length) facts.push(['installs', i.installs.map(deviceLink).join(', ')]);
  facts.push(['shelf life', i.decayH == null ? 'indefinite' : `${i.decayH} h${i.decaysTo ? `, then becomes ${itemLink(i.decaysTo)}` : ', then is gone'}`]);
  const made = [
    ...(book.madeBy.get(id) ?? []).map(wayHtml),
    ...(book.leftBy.get(id) ?? []).map(src => `<li>residue of ${itemLink(src)} when used</li>`),
    ...(book.decayOf.get(id) ?? []).map(src => `<li>${itemLink(src)}, decayed</li>`),
  ];
  const used = (book.takenBy.get(id) ?? []).map(wayHtml);
  const tool = (book.neededBy.get(id) ?? []).map(wayHtml);
  return {
    title: i.name,
    body: `${head(i.id, sub, kindOf(i), i.words)}${factsHtml(facts)}
      ${list(`made:${id}`, `Sources · ${made.length}`, made, 'No procedure aboard produces it.')}
      ${list(`used:${id}`, `Consumed by · ${used.length}`, used, '')}
      ${list(`tool:${id}`, `Tool for · ${tool.length}`, tool, '')}`,
  };
}

function devicePage(id) {
  const d = book.devices.get(id);
  if (!d) return null;
  const sub = book.subs.get(id.slice(0, id.indexOf('.')));
  const universal = d.role === sub?.code || !book.roles.has(d.role);
  const facts = [
    ['role', universal ? `standard issue, every capsule — ${go('page:capsule', 'the capsule')}` : go(`role:${d.role}`, book.roles.get(d.role).name)],
    ['footprint', `${d.columns} × ${d.rows} cells`],
  ];
  const parts = book.fittedBy.get(id) ?? [], kits = book.installedBy.get(id) ?? [];
  if (parts.length) facts.push(['spare parts', parts.map(itemLink).join(', ')]);
  if (kits.length) facts.push(['installed from', kits.map(itemLink).join(', ')]);
  const ways = waysOf(id).map(wayHtml);
  const none = `Runs no procedure; storage only — ${go('page:storage', 'chests and lockers')}.`;
  return {
    title: d.name,
    body: `${head(d.id, sub, 'device', d.words)}${factsHtml(facts)}
      ${list(`ways:${id}`, `Procedures · ${ways.length}`, ways, none)}
      <p class="note">Procedure selection and cycles: ${go('page:devices', 'devices and ways')}.</p>`,
  };
}

function head(id, sub, kind, words) {
  const where = sub ? `${go(`sub:${sub.code}`, sub.name)} · ${go(`section:${sub.section}`, book.sections.get(sub.section)?.name ?? sub.section)}`
    : go('page:capsule', 'standard issue');
  return `<div class="where">stock code <code>${esc(id.toUpperCase())}</code> · ${where} · class <span class="kind">${esc(kind)}</span></div>
    <p class="about">${esc(words.about)}</p><p class="flavour">${esc(words.flavour)}</p>`;
}

const factsHtml = facts => `<dl class="form">${facts.map(([k, v]) => `<dt>${k}</dt><dd>${v}</dd>`).join('')}</dl>`;

/** A titled list, its first LIST_FIRST rows unless opened past them. */
function list(key, title, rows, empty) {
  if (!rows.length) return empty ? `<h3>${title}</h3><p class="note">${empty}</p>` : '';
  const shown = view.more.has(key) ? rows : rows.slice(0, LIST_FIRST);
  const more = rows.length > shown.length ? `<li><a class="go" data-codex-more="${esc(key)}">list all ${rows.length}</a></li>` : '';
  return `<h3>${title}</h3><ul class="ways">${shown.join('')}${more}</ul>`;
}

const counted = list => list.map(c => `${c.count} × ${itemLink(c.item)}`).join(', ');

/** One way: who runs it and how long, what it needs, takes, makes and gives. */
function wayHtml(k) {
  const w = book.data.ways[k];
  const seconds = w.minutes * book.data.figures.cycleSPerWayMinute;
  const gives = w.gives.map(e => statLink(e, false)).join(', ');
  const flow = [
    w.needs.length ? `<span class="tag">tool</span> ${counted(w.needs)}` : '',
    `${w.takes.length ? counted(w.takes) : '<span class="tag">no input</span>'} <span class="arrow">→</span> `
      + (w.makes.length ? counted(w.makes) : '<span class="tag">no output</span>'),
    gives ? `<span class="tag">effect</span> ${gives}` : '',
  ].filter(Boolean).join('<br>');
  return `<li class="way"><b>${esc(w.name)}</b> <small>${deviceLink(w.by)} · ${w.minutes} min (${seconds} s aboard)</small>
    <div>${flow}</div></li>`;
}

function sectionPage(id) {
  const s = book.sections.get(id);
  if (!s) return null;
  const subs = book.data.subsections.filter(u => u.section === id)
    .map(u => `<li>${subLink(u)} <small>${esc(u.covers)}</small></li>`).join('');
  return { title: s.name, body: `<p class="about">${esc(s.serves)}</p><ul class="plain">${subs}</ul>` };
}

function subPage(code) {
  const s = book.subs.get(code);
  if (!s) return null;
  const devices = book.data.devices.filter(d => d.id.startsWith(`${code}.`)).map(d => `<li>${deviceLink(d.id)}</li>`);
  const items = book.data.items.filter(i => i.sub === code)
    .map(i => `<li>${itemLink(i.id)} <small>${esc(kindOf(i))}</small></li>`);
  return {
    title: s.name,
    body: `<div class="where">${go(`section:${s.section}`, book.sections.get(s.section)?.name ?? s.section)} · produced by
        ${s.roles.map(r => go(`role:${r}`, book.roles.get(r)?.name ?? r)).join(', ')}</div>
      <p class="about">${esc(s.covers)}</p>
      ${list(`devices:${code}`, 'Devices', devices, 'None.')}${list(`items:${code}`, 'Items', items, 'None.')}`,
  };
}

function rolePage(id) {
  const r = book.roles.get(id);
  if (!r) return null;
  const devices = book.data.devices.filter(d => d.role === id).map(d => `<li>${deviceLink(d.id)} <small>${esc(d.words.about)}</small></li>`);
  return { title: r.name, body: `<p class="note">${go('page:roles', 'Role assignment')}.</p>${list(`role:${id}`, 'Devices', devices, 'None.')}` };
}

function statPage(id) {
  const s = book.stats.get(id);
  if (!s) return null;
  const items = book.data.items.filter(i => i.effects.some(e => e.stat === id))
    .map(i => `<li>${itemLink(i.id)} <small>${i.effects.filter(e => e.stat === id).map(e => signed(e.amount) + (e.perHour ? '/h' : '')).join(', ')}</small></li>`);
  const ways = book.data.ways.map((w, k) => w.gives.some(e => e.stat === id) ? k : -1).filter(k => k >= 0).map(wayHtml);
  const better = s.higherIsBetter ? 'higher is better' : 'lower is better';
  return {
    title: s.id,
    body: `<div class="where">metric of the ${esc(s.of)} · ${better} · ${go('page:stats', 'needs and stats')}</div>
      <p class="about">${esc(s.means)}</p><p class="flavour">reference values: ${esc(s.typical)}</p>
      ${list(`stat-items:${id}`, `Items affecting · ${items.length}`, items, '')}
      ${list(`stat-ways:${id}`, `Procedures affecting · ${ways.length}`, ways, '')}`,
  };
}

function findPage(query) {
  const q = query.trim().toLowerCase();
  if (!q) return home();
  const hits = [
    ...book.data.pages.filter(p => p.title.toLowerCase().includes(q)).map(p => `<li>${go(`page:${p.slug}`, p.title)} <small>page</small></li>`),
    ...book.data.devices.filter(d => d.id.includes(q) || d.name.toLowerCase().includes(q)).map(d => `<li>${deviceLink(d.id)} <small>device</small></li>`),
    ...itemsMatching(q).map(i => `<li>${itemLink(i.id)} <small>${esc(kindOf(i))}</small></li>`),
  ];
  const shown = hits.slice(0, SEARCH_MOST);
  return {
    title: `Query “${query}”`,
    body: shown.length ? `<ul class="plain">${shown.join('')}</ul>${hits.length > shown.length ? `<p class="note">${hits.length - shown.length} more records. Narrow the query.</p>` : ''}`
      : '<p class="note">No record matches. Query part of a name, "water", or a stock code, "wat-002".</p>',
  };
}

document.addEventListener('click', e => {
  const link = e.target.closest('[data-go]');
  if (link) {
    e.preventDefault();
    return openCodex(link.dataset.go);
  }
  if (!e.target.closest('#codex')) return;
  const stepBy = e.target.closest('[data-codex-step]');
  if (stepBy) return step(Number(stepBy.dataset.codexStep));
  if (e.target.closest('[data-codex-close]')) return close();
  const more = e.target.closest('[data-codex-more]');
  if (more) {
    view.more.add(more.dataset.codexMore);
    draw();
  }
});

document.addEventListener('input', e => {
  if (!e.target.matches('[data-codex-find]')) return;
  view.query = e.target.value;
  const target = `find:${view.query}`;
  // Typing refines the one search page rather than stacking a page a keystroke.
  if (!view.history[view.at]?.startsWith('find:')) return openCodex(target);
  view.history[view.at] = target;
  draw();
});

// Esc closes the codex before anything else; Alt+← and Alt+→ step through its history.
document.addEventListener('keydown', e => {
  if (!view.open) return;
  if (e.key === 'Escape') {
    close();
    e.stopImmediatePropagation();
  } else if (e.altKey && (e.key === 'ArrowLeft' || e.key === 'ArrowRight')) {
    step(e.key === 'ArrowLeft' ? -1 : 1);
    e.preventDefault();
  }
}, true);

document.addEventListener('pointerdown', e => {
  const grip = e.target.closest('[data-codex-grip]');
  if (!grip || e.target.closest('button')) return;
  view.grip = { dx: e.clientX - view.x, dy: e.clientY - view.y };
  e.preventDefault();
});

document.addEventListener('pointermove', e => {
  if (!view.grip) return;
  view.x = e.clientX - view.grip.dx;
  view.y = e.clientY - view.grip.dy;
  inFrame(place);
});

document.addEventListener('pointerup', () => {
  if (!view.grip) return;
  view.grip = null;
  keepOnPage();
});

addEventListener('resize', () => view.open && keepOnPage());
