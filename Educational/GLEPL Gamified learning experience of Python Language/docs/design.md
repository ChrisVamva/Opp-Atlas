# Design — Byte

## Governing decision

**The engine owns the world; player code is a stateless function.**

- Deterministic TypeScript engine, seedable RNG, applies one action per tick.
- Player Python runs in a Pyodide web worker: `tick(state)` → one action.
- State is serialized to plain JSON strings between the two worlds.
- `bot.memory` (a Python dict) is the only thing that persists between ticks.

## The tick contract

```python
def tick(state):          # state: plain dict from JSON
    ...
    return move("east")   # or grab(), rest(), or a direction string
```

- Engine serializes world → JSON string → worker.
- Worker parses, runs player code, returns an action.
- Engine validates and applies it. Invalid actions are ignored safely.

## Runaway code as game physics

Per-tick watchdog (500 ms, generous; normal ticks < 5 ms). On overrun:

1. Terminate the worker.
2. Respawn Pyodide (cached, seconds).
3. Restore world + `bot.memory` snapshot (taken after every tick).
4. Show "Byte used too many brain-cycles and fell asleep."

No SharedArrayBuffer / interrupt-buffer in v1 — that needs COOP/COEP
headers and breaks `file://`. Terminate-and-respawn works everywhere and is
made diegetic. Upgrade path noted, not built.

## Determinism

All world randomness comes from an episode seed. Consequences: free replays,
fair multi-seed quest verification (hardcoded answers fail), and ghost
battles later for free.

## Quests as data

Each quest is a declarative object: `{ id, prompt, starter, worldSpec,
goals[] (engine predicates), tickCap, hint }`. Progression = all seeds pass.
Per-quest code saved to localStorage. No accounts, no server in v1.
