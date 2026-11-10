# Goals

**What shipstick is for.** A slow-paced multiplayer browser game in which each player runs one capsule of a large
space ship, and the ship works only if the capsules' players manage to work together without ever talking directly.
The design as the owner wrote it is [../readme.md](../readme.md); its rules, one by one, are
[requirements.md](requirements.md).

## The game

- **The goal is to keep the ship going and functional.** Every capsule is responsible for some aspect of a ship
  function — food, oxygen, power, navigation — and no capsule can keep its function up alone.
- **Communication is the core concept.** A player meets only the capsules on its four sides, and what passes between
  two of them passes through the door slots between them (GAM-2, GAM-3). Coordinating a whole ship through that is
  the game.
- **Everything a player owns is on the floor.** There is no personal inventory: items live in containers and devices
  on the capsule's grid, opened and dragged between (GAM-5).
- **Slow and event-based.** The game moves on events — an item dragged, a device's interval elapsing (GAM-7).

## The technology

- **Always client–server** (HST-3, HST-4, `P0`): a .NET 11 host runs all of the game and hosts its assets; a browser
  page is a client that shows what its player can see and sends their actions. The game's own types are engine-free and
  testable without a page or a host.
- **C# on .NET 11 in the host; plain JS and CSS in the browser** (WEB-9, `P1`): no bundler and no build step for the
  client, every feature the latest major browsers have, as thin and as fast as it can be.

## Engineering rules

None stated yet. A rule the owner states about how the code must be built (allocation, determinism, what crosses
into JavaScript) goes here with its rung, and gets a gate in `src/tests/gates/`.
