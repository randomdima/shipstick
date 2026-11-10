This is a Dotnet 11 wasm html project.
This is a slow pacing multiplayer game where each player controls a small capsule of a large space ship.
Ship consists of a grid of capsules each controlled either by player or ai.
Capsules are connecte to max of 4 neibhor similar capsules and can only interact directly with them.
Core concept is the need to communicate with each other to make the ship functonal.
This is the event based brower web game.
Each capsule is responsible of some aspect of a ship function.
Each capsule is NxN grid cells with doors connection to other capsules.
There are devices than are or can be placed on that grid.
Each deviced can produce some resources consuming other resources.
Basic example is food farm, oxigen generator, navigation, etc...
Players dont have personal inventory - its all placed in their grid furninure instead - like chestes and deviced.
Players can open and drag items from their inventories and do actions.
Each device can have inventory of its own and actions of its own.
Example - oxigen generator needs electricity and some consumable to operate with some interval.
Players cannot communicate directly, only with 3x3 door slops to share and drag items.
The main goal is too keep ship going and functional.

## Build and run

Needs the .NET SDK `global.json` names, Python 3 with Pillow and numpy (the tools), and Chromium on PATH for pictures
(`sudo dnf install -y chromium`).

```
dotnet build shipstick.slnx
dotnet run --project src/app/host        # the game's host: the page at http://localhost:8730/
qq tests                                 # the unit tier, after every edit
qq web --shot .tmp/web/page.png          # the host run and its page photographed in a headless browser
qq checks                                # build, suite, citations, art provenance — before a commit
dotnet run --project src/app/demo -- .tmp/demo-site                        # the demo's static site, no host
qq web --page .tmp/demo-site/index.html --shot .tmp/web/demo.png           # the demo photographed from disk
```

The demo (DEM-1) is deployed to GitHub Pages from `main` by `.github/workflows/demo.yml`: the page playing back the
host's recorded frames in a loop, every action but the admin's `enter` refused.

`?admin` opens the admin's page, `?seat=column,row` a player's; every page open on a host plays its one ship. In VS
Code, the launch configurations `web: admin` and `web: player` build the host, run it under the debugger and open the
page in Chromium. The client's JS and CSS are served as a build copies them, so a change to them is a build and a
reload; a change to C# is a new run of the host.

## What it is made of

| Path | Holds |
|---|---|
| `src/shipstick.csproj` | the game, engine-free: every slice except the shell (`app/`) and the tests |
| `src/app/web/` | the client: plain JS and CSS in `wwwroot/`, served as written |
| `src/app/host/` | the game's host: runs the game and serves the client (client–server, `P0`) |
| `src/tests/` | the suite, mirroring `src/` |
| `docs/` | what belongs to no single slice — [docs/index.md](docs/index.md) |
| `assets/`, `raw_assets/` | the game's images, and where each came from — [raw_assets/index.md](raw_assets/index.md) |
| `.qq/` | the project's `qq` tools: `qq --help` lists them |
| `.claude/skills/shapegen/` | every asset as a 3D model of simple shapes, rendered by `qq shapes` (GAM-13) |
| `.claude/skills/remotegen/` | image generation through OpenRouter: the textures the models wear |

How work is done here is [CLAUDE.md](CLAUDE.md).