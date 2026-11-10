import { $, hooks, drawShip, begin, busy } from './cabin.js'
import { line, nowS, open, send } from './host.js'
import { loaded } from './codex.js'
import { patch, setText } from './dom.js'

/** What a player is told: their own floor and doors, never who is beyond a door (WEB-7, WEB-1). */
const LOOK = {
  heading: 'Assigned capsule',
  where: 'assigned capsule',
  beyond: () => 'adjacent capsule',
  shared: () => 'Shared with the adjacent capsule. Items left here may be taken from the other side, and the reverse.',
};

/** Seats the page's player at `seatText` ("column,row"); the host says if there is no such seat. */
export function startPlayer(seatText) {
  sit(frame => frame.seat);
  open(`seat=${encodeURIComponent(seatText)}`, () => busy() || hooks.draw(), refused);
  $('hint').textContent = 'Click a fixture or a door to open its panel. Drag items between open panels; drag the deck to '
    + 'pan, with the right button or ctrl held to turn and tilt it; the wheel zooms. Esc closes the top panel. ? or right-click on an item opens the codex. Adjacent capsules are known only by '
    + 'what passes the doors.';
}

const CLOCK_DIGITS = 7;

/** The ship's time as the header's readout prints it: whole seconds, zero-padded to a fixed width. */
export const clockText = () => `ship time ${String(Math.floor(nowS())).padStart(CLOCK_DIGITS, '0')} s`;

/** The line is closed: the page keeps what it last drew, and says why. */
export function refused(reason) {
  hooks.draw = () => {};
  $('status').textContent = reason;
  $('status').className = 'alarm';
}

/**
 * Draws the page as a seated player sees it, the seat being `seatOf(frame)` (a SeatView): how a player's page runs, and
 * how the admin plays a seat. What it does is sent from the seat the host has this line at.
 */
export function sit(seatOf) {
  begin();
  document.body.className = 'player';
  patch($('controls'), '');
  Object.assign(hooks, {
    draw: () => drawSeat(seatOf),
    move: (from, fromSlot, to, toSlot) => send('move', { from, fromSlot, to, toSlot }),
    select: (inventory, way) => send('select', { inventory, way }),
    slotClicked: null,
    escape: () => false,
    editing: () => false,
    reach() {},
  });
  hooks.draw();
}

function drawSeat(seatOf) {
  if (!line.frame || !loaded()) return;
  const { columns, rows, cabin, fogged } = seatOf(line.frame);
  setText($('clock'), clockText());
  setText($('status'), cabin.failing ? 'life support starved: capsule failing' : 'life support nominal');
  $('status').classList.toggle('alarm', Boolean(cabin.failing));
  drawShip({ columns, rows, heading: LOOK.heading, rooms: [{ cabin, look: LOOK }], fogged, focus: cabin.at });
}
