# Decision log — the host

Why the game is run and served as it is. Only decisions still binding are here.

## 2026-11-05 — the game is always client–server

The owner, in as many words: "P0 requiremnt - the game is always client - server / with dotnet 11 host running all the
logic and hosting assets / clients only display what they can see and send actions to the server / basic player can
only see its own room, so the scope is very clean / admin can see more and do special actions". So HST-3 and HST-4 here,
and WEB-7 and WEB-8 in the client's requirements, all at `P0`.

One ship is the host's (`ServedShip`), and every client is a view onto it from one seat: a player's from their room,
the admin's from the whole ship. A client holds no game type and runs no rule, so what it is not shown it does not
have. The client's WEB-1 and WEB-2 are the assistant's detail of WEB-7 and WEB-8 and keep their own rungs.

## 2026-11-05 — one socket a client, sent its view when it changes

A client opens one WebSocket at `/play?seat=column,row` or `/play?admin`; the host decides from the query which client
it is and refuses a seat with no capsule. The connection is the seat: an action names no seat, so a player cannot act
from another's. The admin's actions (`enter`, `rate`, `set`) are refused on a player's socket.

The clock advances the ship every `HostFigures.TickS`, and after each advance and each action every client's view is
made again and sent only if it changed. The ship's time is not in a view but in the frame around it, with the rate, so
an idle ship sends nothing and a client tells the time on itself. Every touch of the ship is under one lock, so the
game's types stay single-threaded. A slow client is sent the newest frame, never a queue (`Client`), and the socket is
compressed: a view is repetitive JSON with nothing secret beside what the client sent.

Plain WebSockets rather than SignalR: the browser and ASP.NET Core both have them built in, so the client needs no
library (WEB-9) and the host no package.

## 2026-11-05 — the game is served by a .NET host of its own

The owner, in as many words: "hosting the game is runtime"; "qq tools are design time only". So HST-1 and HST-2, at
`P2`. On 2026-11-10, with the repository pushed to its public GitHub remote, the owner: "Push everything non tmp" — so
`.qq/` is tracked and public, and HST-2 keeps the tools out of what ships, not out of the repository. Until then the page was served by a Python server inside `qq web`, which was design-time
tooling standing in for runtime.

The host is an ASP.NET Core project (`shipstick.host.csproj`) referencing the game. The client's files are copied beside
it as written (`client/`) and served as static files, each revalidated on every load, so a new build is never served
stale; JS and CSS changed under a running host are served once a build has copied them, and C# changes need the host
started again. Responses are compressed, a model's triangles and the font too; the codex, most of what a client
downloads, is compressed once at start at Brotli's smallest and answered "not modified" to a client that holds it
(`ServedJson`). It is sent in two (`CodexJson`): the book every page needs for its names and ways, and the items' and
devices' words — prose, more than half its bytes compressed — which only the codex's window shows and asks for when it
first opens.

The art is the exception to revalidating, as it is most of the requests a page makes and a reload asked again for
each over HTTP/1.1. `assets.json` (`AssetList`) gives each file under `assets/` a version, a hash of its bytes, and
the page asks for a file at it (`?v=`); what one such address holds never changes, so it is kept a year without
asking (`HostFigures.VersionedKeptS`), and a new build's file is a new address. `assets.json` itself is revalidated,
and carries every model's `.mesh.json` whole, so the page asks for a model's triangles and textures together, as soon
as the floor stands it, rather than a round trip apart. The page's own files, and what the stylesheet names, stay revalidated: they
would need a build step to carry versions (WEB-9). Its port is `appsettings.json`'s, overridden
by `--urls`. `qq web` builds it, starts and stops it, and photographs the page it serves; VS Code's launches run it
under the debugger.
