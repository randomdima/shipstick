# Requirement priority

**Every requirement says whose it is.** A rule states a relation; a priority states what bending it costs, and — at
the top of the ladder — who has to be asked. It is written as a backticked rung directly after the ID:

```
**GAM-2** `P3` A capsule is joined to at most four neighbouring capsules …
```

## Why the scale exists

The documents are mostly written by an assistant, and read back later nothing distinguishes a rule the owner asked
for from one the assistant inferred and then cited as though it had been handed down. **The rung is the record of
where a rule came from**, so a rule can be weighed without anyone remembering the conversation it was written in.

## The ladder

**`P0`, `P1` and `P2` are the owner's: requirements the owner stated, in as many words. `P3`–`P9` are the
assistant's: created, implied or assumed along the way.** The top three rungs record authority; the rest record
consequence. So an assumed rule can never outrank a stated one.

| Rung | Whose | What bending it costs |
|---|---|---|
| `P0` | the owner, stated explicitly as binding | Nothing bends it. It changes only when the owner asks; an assistant that finds it inconvenient reports the conflict and stops. |
| `P1` | the owner, stated softly | Bent only at a genuine edge case, in a fixture or a test, and the bend is written in the nearest `decision-log.md`. |
| `P2` | the owner, stated as a direction | The owner said what the game is to do and left the how open. The how is the assistant's; the direction bends only when the owner agrees, and the conflict is reported first. |
| `P3` | the assistant | A game-wide rule, or its direct consequence. Bending it is a change to [goals.md](goals.md) first. |
| `P4` | the assistant | The game's state stops being sound — an item lost or duplicated, an event applied twice. |
| `P5` | the assistant | Two answers to one question: a second representation, a figure in two places, a derived figure authored. |
| `P6` | the assistant | A device or an AI capsule does not do its job. |
| `P7` | the assistant | The ship is laid or drawn wrong. |
| `P8` | the assistant | The player's hands: opening, dragging, acting, the interface. |
| `P9` | the assistant | An instrument lies, a detail, or a preference that could have gone the other way. |

**A rule that could be argued into two assistant rungs takes the lower-numbered one. A rule may never be argued into
`P0`, `P1` or `P2`** — those are granted, not deduced. A rule the assistant wrote from the owner's design (the readme)
is the assistant's until the owner names its rung.

## Two ladders spelled the same way

`P0`–`P9` also names the test ladder ([tests/Priority.cs](../src/tests/Priority.cs)), which asks *what is the ship if
this test is wrong?* A requirement carries a rung; a test class carries a rung; neither is read off the other.

## How a rung is granted, changed and checked

- **The owner grants `P0`, `P1` and `P2` by saying so**, in as many words. Nothing else grants them. Where the
  owner's words set a direction without naming a rung, the rule is `P2`, and the decision log quotes the words.
- **A rung is never inferred upward**, and moving a rule out of the owner's band needs the owner as much as moving it
  in.
- **A promotion rewrites the marker in place**; why is the nearest `decision-log.md`.
- **`qq doclint` fails on a rule with no rung.** `qq req <ID>` prints the rung with the statement; `qq req --rungs`
  lists the owner's band, held nowhere else.

## Where a conflict goes

**A `P0` the code does not meet is reported, not quietly reinterpreted**, and named in
[index.md](index.md#known-gaps) until it closes.
