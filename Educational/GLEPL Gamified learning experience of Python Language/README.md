# Byte — a code-driven pet bot 🐣

You write real Python. Your pet follows it. That's the whole idea.

Byte is a browser game that teaches Python by making your code the pet's
brain: one `tick(state)` function, called every turn of the game. Start with
a single `move("east")`, end up writing heuristic bot logic in an arena.

## Status

**Scaffold only — no code yet.** See `docs/roadmap.md` for the build order.

## How it will work (one paragraph)

A deterministic TypeScript engine owns the world; player Python runs in a
Pyodide web worker and returns exactly one action per tick (`move`, `grab`,
`rest`). A watchdog turns runaway code (`while True:`) into a game mechanic
instead of a frozen page: Byte "falls asleep," the worker respawns, the
world continues. Quest goals use randomized seeds, so hardcoded answers
don't pass.

## Project layout

```
README.md          <- you are here
docs/
  design.md        architecture: engine/worker contract, tick model
  roadmap.md       milestones, verification plan, out-of-scope list
src/
  engine/          deterministic grid world (TypeScript, no DOM)
  py/              Pyodide worker, Python helpers, tick bridge
  ui/              editor wiring, canvas renderer, quest flow
```

## Verification promise

Every step of the build ends with the files checked on disk (`ls` / line
counts / read-back) before moving on — no more 26-minute silent gaps.
