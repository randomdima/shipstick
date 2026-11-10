# Requirements — the host

What serves the game and runs it. Each rule carries a rung ([../../../../docs/priority.md](../../../../docs/priority.md)).

**HST-3** `P0` The game is always client–server: the .NET 11 host runs all of the game's logic and hosts its assets.

**HST-4** `P0` A client only displays what its player can see, and sends its player's actions to the host.

**HST-1** `P2` Hosting the game is part of the game's runtime: what serves the page is the game's own .NET host, built
and shipped with it.

**HST-2** `P2` The `qq` tools are design time only. Nothing the game runs on is one, and none of them is published.
