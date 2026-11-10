// How the page changes what it shows (WEB-10): never by rebuilding it. Every view still writes what it shows as HTML,
// and these bring the live nodes to it in place — nothing whose HTML is unchanged is touched, and of what changed only
// the attributes, text and children that differ are written. A node kept is the node a pointer, a focus or a hover
// already holds.

// The HTML each element was last brought to, so an unchanged one is passed over without parsing it.
const lastHtml = new WeakMap();
// Each keyed parent's children by key: { el, html }.
const keyed = new WeakMap();
const template = document.createElement('template');
// What setStyle last wrote on each element, by property: compared as written, since the browser reads a value back
// in its own spelling. Forgotten when a morph rewrites the element's style whole.
const written = new WeakMap();

/** `html` as nodes, in a fragment the next parse empties. */
function parse(html) {
  template.innerHTML = html;
  return template.content;
}

/** Brings `el`'s children to `html`; says whether anything changed. */
export function patch(el, html) {
  if (lastHtml.get(el) === html) return false;
  lastHtml.set(el, html);
  morphChildren(el, parse(html));
  return true;
}

/**
 * Brings `parent`'s children to `entries` — [key, html] pairs, each html one element, in order — keeping the element of
 * every key it already has; says whether anything changed. The parent holds nothing but these.
 */
export function reconcile(parent, entries) {
  if (!keyed.has(parent)) keyed.set(parent, new Map());
  const was = keyed.get(parent), now = new Map();
  const fresh = entries.filter(([key, html]) => was.get(key)?.html !== html);
  // Every element new or changed this draw, parsed together: one parse, not one an element.
  const parsed = [...parse(fresh.map(([, html]) => html).join('')).children];
  let i = 0;
  for (const [key, html] of entries) {
    const node = was.get(key);
    if (node?.html === html) {
      now.set(key, node);
      continue;
    }
    const next = parsed[i++];
    if (node && node.el.nodeName === next.nodeName) {
      morph(node.el, next);
      now.set(key, { el: node.el, html });
    } else now.set(key, { el: next, html });
  }
  // What left goes before anything is placed, so what stays is not moved round it: a moved node loses its focus.
  for (const [key, { el }] of was) if (now.get(key)?.el !== el) el.remove();
  let before = parent.firstChild, moved = false;
  for (const { el } of now.values()) {
    if (el === before) before = before.nextSibling;
    else {
      parent.insertBefore(el, before);
      moved = true;
    }
  }
  keyed.set(parent, now);
  return moved || fresh.length > 0 || was.size !== now.size;
}

/**
 * Sets each of `values` on `el`'s style — a property or a `--custom` one — that differs from what it holds; says
 * whether any did.
 */
export function setStyle(el, values) {
  if (!written.has(el)) written.set(el, new Map());
  const was = written.get(el);
  let changed = false;
  for (const [name, value] of Object.entries(values)) {
    const text = String(value);
    if (was.get(name) === text) continue;
    if (name.startsWith('--')) el.style.setProperty(name, text);
    else el.style[name] = text;
    was.set(name, text);
    changed = true;
  }
  return changed;
}

/** Sets each of `values` as an attribute of `el` that differs from what it holds. */
export function setAttributes(el, values) {
  for (const [name, value] of Object.entries(values)) {
    const text = String(value);
    if (el.getAttribute(name) !== text) el.setAttribute(name, text);
  }
}

// What is to be done before the next frame is drawn, each once.
const beforeFrame = new Set();

/**
 * Runs `work` once before the display's next frame, however often it is asked for until then: what follows the
 * pointer is drawn at the display's own rate (WEB-11), never once an event.
 */
export function inFrame(work) {
  if (!beforeFrame.size) requestAnimationFrame(() => {
    const due = [...beforeFrame];
    beforeFrame.clear();
    for (const run of due) run();
  });
  beforeFrame.add(work);
}

/** Sets `el`'s text, if it differs: in the text node it already holds, where it holds only one. */
export function setText(el, text) {
  if (el.textContent === text) return;
  if (el.childNodes.length === 1 && el.firstChild.nodeType === Node.TEXT_NODE) el.firstChild.nodeValue = text;
  else el.textContent = text;
}

/** Brings `from` to `to`, an element of the same name: its attributes, then its children. */
function morph(from, to) {
  if (from.getAttribute('style') !== to.getAttribute('style')) written.delete(from);
  for (const { name } of [...from.attributes]) if (!to.hasAttribute(name)) from.removeAttribute(name);
  for (const { name, value } of to.attributes) if (from.getAttribute(name) !== value) from.setAttribute(name, value);
  // A field's value and an option's choice are its own once used; the attribute alone no longer moves them. A field
  // in use is left as its user has it.
  if (from instanceof HTMLInputElement && from !== document.activeElement && from.value !== to.value) from.value = to.value;
  if (from instanceof HTMLOptionElement) from.selected = to.hasAttribute('selected');
  morphChildren(from, to);
}

function morphChildren(from, to) {
  const was = [...from.childNodes], now = [...to.childNodes];
  now.forEach((node, i) => {
    const old = was[i];
    if (!old) from.append(node);
    else if (old.nodeType !== node.nodeType || old.nodeName !== node.nodeName) old.replaceWith(node);
    else if (old.nodeType !== Node.ELEMENT_NODE) {
      if (old.nodeValue !== node.nodeValue) old.nodeValue = node.nodeValue;
    } else morph(old, node);
  });
  for (const old of was.slice(now.length)) old.remove();
}
