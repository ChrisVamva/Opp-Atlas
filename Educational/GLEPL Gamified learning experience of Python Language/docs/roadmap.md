# Roadmap

## Milestones (de-risk the crux first)

1. **Worker hello-tick** — static shell + Pyodide worker loads, returns one
   action for a hardcoded state. *The risky part dies or survives here.*
2. **Engine + renderer** — deterministic grid world, canvas renderer, run
   loop with fixed code.
3. **Editor + bridge** — CodeMirror editor wired to the tick bridge; runtime
   errors shown as friendly cards with line numbers; watchdog verified by
   deliberately hanging a tick.
4. **Quests** — quest data + multi-seed runner + progression (localStorage).
   Quest 1: edit `move("east")` to reach a gem.
5. **Sandbox + verification pass** — goal-less playground; end-to-end checks.

## Verification (each milestone)

- `tsc --noEmit` clean.
- Unit tests for world determinism and quest predicates.
- Playwright against the real surface: load → Quest 1 → `while True:` makes
  Byte faint → recovery → sandbox reachable.

## Out of scope (next slices, not v1)

- Memory dungeons / mastery ledger (SM-2 scheduling)
- Ghost battles & PvP arena
- Accounts, server, multiplayer
- AI mentor, narrative/lore, mobile-native
- Real-Python transfer glossary UI

## Known tradeoffs

- **Pyodide cold load (~10 MB):** incubation-egg loading screen; measured
  during verification.
- **Watchdog vs interrupt-buffer:** coarse but robust; diegetic framing.
- **Audience:** copy written for kids ~9–13 per positioning; changing it is a
  copy-level task, not an architecture one.
