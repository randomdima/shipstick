import { hooks, busy } from './cabin.js'
import { startAdmin } from './admin.js'
import { startPlayer } from './player.js'
import { loadCodex } from './codex.js'
import { loadArt } from './art.js'
import { loadScene } from './scene.js'

// How often the page redraws between frames, for the clock and a cycle's progress; the ship's own pace is the host's.
const REDRAW_MS = 250;
// The seat a player's page takes when its address names none.
const FIRST_SEAT = '0,0';

// Fetched while the line opens (index.html preloads it): every name the floor shows is the codex's, so a frame that
// comes first waits for it.
const codex = fetch('codex.json').then(answer => answer.json());
const art = fetch('assets.json').then(answer => answer.json());
const bays = fetch('assets/app/web/interfaces/bays.json').then(answer => answer.json());

// `?admin` is the admin's page; anything else is a player's, at `?seat=column,row`.
const query = new URLSearchParams(location.search);
if (query.has('admin')) startAdmin();
else startPlayer(query.get('seat') ?? FIRST_SEAT);

loadArt(await art, await bays);
await loadScene(await art);
loadCodex(await codex);
hooks.draw();
setInterval(() => busy() || hooks.draw(), REDRAW_MS);
