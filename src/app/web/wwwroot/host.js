// The line to the host (HST-4): one socket, a frame in whenever what this page is shown changes, and an action out for
// each thing its player does, answered with whether the game took it. The page runs none of the game: between frames
// it only tells the ship's time on from the last frame's time and rate.

const answers = new Map();
let socket = null, lastId = 0;

/** The last frame: `nowS` and `rate` of ship time, and `seat` (a player's) or `ship` (the admin's). */
export const line = { frame: null, atMs: 0 };

/** Ship seconds now, told on from the last frame at its rate. */
export const nowS = () => line.frame ? line.frame.nowS + (performance.now() - line.atMs) / 1000 * line.frame.rate : 0;

/**
 * Opens the line as `who` ("seat=1,1" or "admin"); `framed()` is called on each frame, `closed(reason)` once the line
 * is closed.
 */
export function open(who, framed, closed) {
  const url = new URL(`play?${who}`, location.href);
  url.protocol = url.protocol === 'https:' ? 'wss:' : 'ws:';
  socket = new WebSocket(url);
  socket.onmessage = e => {
    const message = JSON.parse(e.data);
    if ('re' in message) {
      answers.get(message.re)?.(message.ok);
      return answers.delete(message.re);
    }
    line.frame = message;
    line.atMs = performance.now();
    framed();
  };
  socket.onclose = e => closed(e.reason || 'link to host lost');
}

/** Sends the action `act` with its `fields`; resolves to whether the game took it. */
export function send(act, fields) {
  const id = ++lastId;
  socket.send(JSON.stringify({ id, act, ...fields }));
  return new Promise(resolve => answers.set(id, resolve));
}
