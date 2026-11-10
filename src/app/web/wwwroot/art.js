// Which generated art each thing on the page shows (GAM-9): a device's model and its interface, the wall kit's pieces
// and the floor's tiles, each a texture in the floor's scene (scene.js). The host lists what it serves (`assets.json`);
// a thing with no art of its own takes the shared art of its kind.

const DEVICES = 'assets/devices';
const FLOOR = 'assets/ship/floor';
// What every installed picture is (`qq sprites`).
const PICTURE = '.webp';

// A role's devices with no paint of their own take the shared one of the trade nearest theirs.
const GENERIC = {
  agri: 'agri', bio: 'agri', galley: 'agri',
  hydro: 'chem', atmos: 'chem', chem: 'chem', sanit: 'chem',
  power: 'power', drive: 'power', helm: 'power', elec: 'power',
  med: 'med',
};
const GENERIC_FALLBACK = 'fab';

// The deck's plates, in cells wide and deep, by how often each is laid where it fits.
const PLATES = [[2, 2], [2, 2], [3, 2], [2, 1], [1, 2], [3, 1], [1, 1]];
// Each tile is drawn for one set of plate edges (bits as the walls' links) and turned clockwise for the rest.
const DECK_TILES = {
  0: ['inner', 0],
  1: ['edge1', 0], 2: ['edge1', 90], 4: ['edge1', 180], 8: ['edge1', 270],
  9: ['edge2', 0], 3: ['edge2', 90], 6: ['edge2', 180], 12: ['edge2', 270],
  5: ['edge2op', 0], 10: ['edge2op', 90],
  13: ['edge3', 0], 11: ['edge3', 90], 7: ['edge3', 180], 14: ['edge3', 270],
  15: ['edge4', 0],
};
// One one-cell plate in this many is a fitting instead.
const FITTING_EVERY = 3;
const DECK_FITTINGS = ['drain', 'grating', 'cover'];
// Each plate's brightness against its neighbours', so plates read apart.
const PLATE_TINTS = [1, .94, 1.04, .97, 1.07, .91];
// Two large primes, so neighbouring cells take unrelated tiles.
const TILE_MIX_COLUMN = 73856093, TILE_MIX_ROW = 19349663;

const served = new Set();
// The paint each device's window housing wears (assets/app/web/kit/paints.json), by `<kind>` with its dot an
// underscore, or `storage`, `door` and `generic_<trade>` for the shared ones; the stylesheet maps a paint to its kit.
let paints = {};

/** Takes the host's list of served art (`assets.json`), and the windows' paints. */
export function loadArt({ files }, windowPaints) {
  for (const p of Object.keys(files)) served.add(p);
  paints = windowPaints;
}

const file = id => id.replace('.', '_');
const has = path => served.has(path);

/** A device's 3D model (GAM-10), or null when it has none yet and stands as the plain crate (scene.js). */
export function meshOf(kind) {
  const path = `${DEVICES}/${file(kind)}.mesh.json`;
  return has(path) ? path : null;
}

/** The gauge laid on a door's cap to show how full the door is: the level bar part's model, or null until installed. */
export const doorGaugeOf = () => has(DOOR_GAUGE) ? DOOR_GAUGE : null;
const DOOR_GAUGE = 'assets/parts/level_bar.mesh.json';

// A wall is built from the kit (raw_assets/devices/prompting.md), so any layout of wall cells joins: a cap on top
// chosen by which neighbours are wall too and turned to fit, and a front panel on every edge no wall continues past.
// Links are bits: north 1, east 2, south 4, west 8.
const NORTH = 1, EAST = 2, SOUTH = 4, WEST = 8;
const FACES = [[NORTH, 'north'], [EAST, 'east'], [SOUTH, 'south'], [WEST, 'west']];
// Each cap is drawn for one set of links and turned clockwise for the rest: the end joins east, the straight east
// and west, the corner east and south, the tee all but north.
const CAPS = {
  0: ['post', 0], [EAST]: ['end', 0], [SOUTH]: ['end', 90], [WEST]: ['end', 180], [NORTH]: ['end', 270],
  [EAST | WEST]: ['straight', 0], [NORTH | SOUTH]: ['straight', 90],
  [EAST | SOUTH]: ['corner', 0], [SOUTH | WEST]: ['corner', 90], [WEST | NORTH]: ['corner', 180], [NORTH | EAST]: ['corner', 270],
  [EAST | SOUTH | WEST]: ['tee', 0], [SOUTH | WEST | NORTH]: ['tee', 90], [WEST | NORTH | EAST]: ['tee', 180],
  [NORTH | EAST | SOUTH]: ['tee', 270], [NORTH | EAST | SOUTH | WEST]: ['cross', 0],
};
// A straight cap and a panel each break with a plate seam one cell in this many, so a run reads as a few long plates
// rather than a block a cell.
const SEAM_EVERY = 3;
// What a front panel or a straight cap carries now and then, by how often: the rest are plain or seamed.
const PANEL_FITTINGS = [[7, 'panel_vent'], [11, 'panel_hatch'], [13, 'panel_porthole'], [17, 'panel_intercom']];
const CAP_FITTINGS = [[5, 'cap_straight_worn'], [7, 'cap_straight_inspect']];
const mixOf = (column, row) => Math.abs((column * TILE_MIX_COLUMN) ^ (row * TILE_MIX_ROW));
const art = name => `${DEVICES}/any_${name}${PICTURE}`;
const seamed = (column, row) => mixOf(column, row) % SEAM_EVERY === 0;

function plainOf(column, row, fittings, seam, plain) {
  const mix = mixOf(column, row);
  for (const [every, piece] of fittings) if (mix % every === 0) return piece;
  return seamed(column, row) ? seam : plain;
}

/**
 * How a wall or door cell is drawn (GAM-10, SHP-7): its `cap` (turned `capDeg`) and its `faces`, a panel on each side
 * (`north`…`west`) where the cell beside is not wall — `src` with the cell's fitting, `plain` for the courses below it.
 * `isWall(column, row)` says which cells hold a wall or a door; `door` is this cell's, with whether it is open. A door's
 * cell is a wall like any other, with its parts laid on it: a `lintel` on the cap (`lintelAcross` when it runs across
 * the floor), and the door as a `leaf` on each face its passage runs through.
 */
export function structureLook(column, row, isWall, door) {
  const links = (isWall(column, row - 1) ? NORTH : 0) | (isWall(column + 1, row) ? EAST : 0)
    | (isWall(column, row + 1) ? SOUTH : 0) | (isWall(column - 1, row) ? WEST : 0);
  const state = door?.open ? 'open' : 'closed';
  const acrossFloor = !(links & (EAST | WEST)) && (links & (NORTH | SOUTH));
  let [cap, capDeg] = [`cap_${CAPS[links][0]}`, CAPS[links][1]];
  if (cap === 'cap_straight' && !door) cap = plainOf(column, row, CAP_FITTINGS, 'cap_straight_seam', cap);
  const panel = art(door ? 'panel' : plainOf(column, row, PANEL_FITTINGS, 'panel_seam', 'panel'));
  const faces = FACES.filter(([link]) => !(links & link)).map(([, side]) => ({ side, src: panel, plain: art('panel') }));
  const look = { cap: art(cap), capDeg, faces };
  if (!door) return look;
  return {
    ...look,
    lintel: art(acrossFloor ? `door_lintel_side_${state}` : `door_lintel_${state}`), lintelAcross: !acrossFloor,
    leaf: art(`door_leaf_${state}`),
  };
}

/** The paint of a device's window housing (GAM-11): its own, its storage's, or its role's shared one. */
export function paintOf(kind, role, holdsOnly) {
  if (paints[file(kind)]) return paints[file(kind)];
  if (kind === 'any.wall') return doorPaint();
  if (holdsOnly) return paints.storage;
  return paints[`generic_${GENERIC[role] ?? GENERIC_FALLBACK}`];
}

export const doorPaint = () => paints.door;

/**
 * The deck of a floor `across` cells square, cell by cell in reading order: laid in plates of several sizes, each cell
 * the tile that draws its plate's edges where the plate ends and plain steel where it runs on, turned (`deg`) to fit,
 * each plate a little lighter or darker than the next (`tint`). The same every draw, so the floor does not shimmer.
 * Inside each of the `doors` (cells on the floor's edge) lies a hazard-striped threshold, its sill toward the door.
 */
export function deckOf(across, doors = []) {
  const plateOf = new Array(across * across).fill(-1);
  const at = (column, row) => row * across + column;
  const free = (column, row) => column < across && row < across && plateOf[at(column, row)] < 0;
  let plates = 0;
  for (let row = 0; row < across; row++)
    for (let column = 0; column < across; column++) {
      if (!free(column, row)) continue;
      let [wide, deep] = PLATES[mixOf(column, row) % PLATES.length];
      while (wide > 1 && !free(column + wide - 1, row)) wide--;
      while (deep > 1 && ![...Array(wide).keys()].every(i => free(column + i, row + deep - 1))) deep--;
      for (let r = row; r < row + deep; r++) for (let c = column; c < column + wide; c++) plateOf[at(c, r)] = plates;
      plates++;
    }

  const same = (column, row, plate) => column >= 0 && row >= 0 && column < across && row < across
    && plateOf[at(column, row)] === plate;
  const last = across - 1;
  const thresholds = new Map(doors.map(({ column, row }) => row === 0 ? [at(column, 1), 0]
    : row === last ? [at(column, last - 1), 180] : column === 0 ? [at(1, row), 270] : [at(last - 1, row), 90]));
  return plateOf.map((plate, i) => {
    if (thresholds.has(i)) return { src: `${FLOOR}/deck_threshold${PICTURE}`, deg: thresholds.get(i), tint: 1 };
    const column = i % across, row = Math.floor(i / across);
    const edges = (same(column, row - 1, plate) ? 0 : NORTH) | (same(column + 1, row, plate) ? 0 : EAST)
      | (same(column, row + 1, plate) ? 0 : SOUTH) | (same(column - 1, row, plate) ? 0 : WEST);
    let [tile, deg] = DECK_TILES[edges];
    if (edges === (NORTH | EAST | SOUTH | WEST) && mixOf(column, row) % FITTING_EVERY === 0)
      tile = DECK_FITTINGS[mixOf(row, column) % DECK_FITTINGS.length];
    return { src: `${FLOOR}/deck_${tile}${PICTURE}`, deg, tint: PLATE_TINTS[plate % PLATE_TINTS.length] };
  });
}
