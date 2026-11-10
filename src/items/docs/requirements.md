# Requirements — items

Items, the slots they sit in, and a player's drag between slots. Each rule carries a rung
([../../../docs/priority.md](../../../docs/priority.md)).

**ITM-1** `P4` Moving items between slots conserves them: what leaves one slot arrives in another, and no item is made
or lost except by a device's cycle or an admin's edit (SHP-6).

**ITM-2** `P4` A slot holds one kind of item, at most the configured stack of it.

**ITM-3** `P8` A drag onto an empty slot or the same kind moves as many as fit and leaves the rest; onto another kind
it swaps the two stacks; it does nothing if either slot would refuse what it receives.

**ITM-4** `P8` Every slot has a filter: the items it accepts by hand. A slot is universal unless the fixture that owns
it sets a filter, so a chest's and a door's slots take anything; a filter binds a player's move, never the slot's owner.
