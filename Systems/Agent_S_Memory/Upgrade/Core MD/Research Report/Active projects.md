# Summary and Evaluation: Repo Project Reports

*Generated: April 25, 2026*

---

## Overview

This archive contains **6 actual software projects** — not concepts, but built or build-ready codebases. Unlike the "Ideas" folder (research/specification only), these repositories contain working applications, active development logs, and implementation details. Total: **33 files** documenting real code across desktop apps, web apps, CLI tools, and browser-based instruments.

---

## Project Inventory

| # | Project | Category | Files | Status | Built? |
|---|---------|----------|-------|--------|--------|
| 1 | Agent Audit Trail (AAT) | AI Compliance / DevTool | 9 | Design + Plan complete, 6-phase build ready | 🔲 Not built |
| 2 | Dev's Memory | Desktop Productivity | 6 | Built and verified, needs performance fixes | ✅ Built |
| 3 | Doodle Scribe | Creative Web App | 7 | Built + enhanced, multiple phases complete | ✅ Built |
| 4 | FocusFlow | Task Management | 7 | Core built, features specified, hidden logic exposed | ✅ Built |
| 5 | Prompt CLI / Aider Qwen | CLI / DevTool | 3 | Build plan complete, ready to implement | 🔲 Not built |
| 6 | 🎹 Small Piano | Browser Instrument | 1 | Phase 3 complete, 16/16 checks passed | ✅ Built |

**Built ratio: 4/6 (67%)** — significantly higher execution rate than the Ideas archive.

---

## Individual Project Summaries

### 1. Agent Audit Trail (AAT)
**What:** EU AI Act compliance evidence pipeline — tamper-evident audit trails for high-risk AI systems.

**Target Users:** Organizations deploying high-risk AI systems requiring Article 12/26 compliance.

**Core Differentiator:** HMAC-SHA256 chained audit records with regulatory-grade evidence export, not just observability.

**Key Documents:**
- `design.md` — 10 sections: 35-field schema, compliance mapping (18 EU AI Act requirements), tamper-evidence spec
- `plan.md` — 6 phases, 51 tasks, critical path of 17 tasks
- `Overall Verdict.md` — Expert audit found 6 gaps that would block developers (all fixable)

**Critical Gaps Identified:**
- `verify_chain()` signature incompatible with key rotation
- LangGraph checkpoint ≠ agent_start/agent_end mapping error
- `session_chain_heads` UPDATE permission creates integrity gap
- PII tokenization reverse-mapping unspecified
- Archive chain verification procedure missing

**Verdict:** Structurally solid. Fix 6 gaps before handoff to implementation. GDPR exposure in hosted tier needs decision before any customer data touches servers.

---

### 2. Dev's Memory
**What:** Desktop command cheatsheet and snippet manager with unique MCP (Model Context Protocol) integration.

**Stack:** Electron + React + Vite, local-first `data.json` storage.

**Verified Built Features:**
- CRUD for categories and commands
- Persistent storage (survives restart)
- Per-category styling (color + font picker)
- Notebook (ruled paper modal per category)
- Tree view canvas with drag-and-drop
- Global search `Ctrl+Shift+M` (floating spotlight window)
- Import/Export JSON
- **AI Inbox via MCP** — agents can push commands programmatically
- Game Boy widget (live CPU + RAM, collapsible)

**Performance Issues (Known):**
- `systeminformation` library causes fan noise (CPU sampling to measure CPU)
- Electron baseline ~150MB RAM
- Dev mode (`npm run start`) runs Vite + Electron simultaneously
- File watcher loop on `data.json` can trigger write → fire → re-render cycles

**Differentiation vs. Market:**
- **MCP server integration** — no competitor does this
- Visual identity: warm paper aesthetic, Caveat font, Game Boy widget
- Local-first, private, fast

**Verdict:** Real product with genuine identity. Performance fixes identified but not implemented. Architecture needs hardening before expansion.

---

### 3. Doodle Scribe
**What:** Web-based drawing/sketching application with AI refinement, layers, and project management.

**Stack:** React 19 + TypeScript + Vite + Tailwind CSS + Canvas API

**Implemented Features (from Big Pickle report):**
- Drawing tools: pen, highlighter, line, rect, circle, text, eraser
- Color picker, opacity slider, brush size
- Undo/redo (10 states) → **Enhanced to full redo stack**
- AI refinement
- PNG/JPEG export → **SVG export added**
- LocalStorage persistence → **Named projects with thumbnails added**
- Keyboard shortcuts → **Full customization system added**
- Layer system (in development)
- **Color history** (8 recent colors)

**Phase 3 Additions:**
- Real-time chord detection (20 chord templates)
- Root detection via pitch-class set matching
- Live chord name display
- Note name sub-display

**Verdict:** Actively enhanced application with 4 major features added (redo, color history, named projects, keyboard customization). The "Big Pickle report" documents systematic feature implementation.

---

### 4. FocusFlow
**What:** Pomodoro-based task management with Kanban board.

**Stack:** React + TypeScript (strict mode), `@hello-pangea/dnd`, recharts

**Confirmed Built:**
- Core task list with status, priority, due dates
- Kanban board view (Todo → In Progress → Completed)
- Dark mode / light mode toggle
- Basic analytics
- localStorage persistence

**Hidden Features Problem:** Business logic exists in `taskService` but has no UI:
- Due date input in forms (types exist, not utilised)
- Category input in forms (types exist, not utilised)
- Focus metrics on cards (`pomodorosCompleted`, `totalFocusTime` tracked but not displayed)
- Export/Import JSON (service likely exists, no UI)

**Fully Specified But Not Built:**
- Drag-and-drop Kanban (library selected, code written in design doc)
- Sub-task management
- Archive system
- Browser notifications
- Advanced analytics / heatmaps
- Category manager
- Reminder service
- Storage migration system

**Verdict:** Real working app with Kanban and dark mode live. Hidden features plan is highest-value next action — four UI additions surface logic already written. Everything else is specification.

---

### 5. Prompt CLI (The Aider Qwen Project)
**What:** Python CLI tool for local-first, version-controlled prompt engineering using Alibaba Cloud Qwen models.

**Stack:** Python + Click + Jinja2 + GitPython + requests

**Architecture:**
- **qwen3-coder-plus** → Architect Model (planning, design)
- **qwen3-coder-turbo** → Editor Model (code implementation)
- **qwen3.5-plus** → Backup/Utility Model

**Planned Features:**
- Template management (`~/.prompt-cli/templates/`)
- Variable injection (`{{variable_name}}` syntax)
- Model selection via CLI flag
- API interaction with Alibaba Cloud Model Studio
- Automatic Git initialization for version control
- Local-first: all data stored locally

**Project Structure:**
```
prompt-cli/
├── prompt_cli.py          # Main CLI entry
├── config.py              # Config and API keys
├── template_manager.py    # Template and variable management
├── api_client.py          # Alibaba Cloud API
├── utils.py               # Git helpers
├── requirements.txt
└── README.md
```

**Verdict:** Complete build plan with model orchestration strategy. Not yet implemented. Ready for Phase 1 (architect prompt) → Phase 2 (editor execution).

---

### 6. 🎹 Small Piano
**What:** Zero-dependency browser-based musical instrument.

**Stack:** Vanilla HTML/CSS/JS, Web Audio API, Web MIDI API

**Phase 1 — Core Audio Engine:**
- Oscillator + gain node per key
- Attack/release envelope (8ms/300ms)
- 2 octaves (C4–B5)
- Mouse/touch drag-to-glide
- Keyboard shortcuts: `A W S E D F T G Y H U J K O L`
- Web MIDI API with live device detection

**Phase 2 — Zen UI:**
- Warm `#f8f4f0` palette, system fonts
- Hamburger → slide-in settings panel
- Volume slider + sustain checkbox
- BEM class names, smooth transitions
- Active key glow (peach for white, amber for black)

**Phase 3 — Chord Discovery:**
- Real-time chord detection (20 templates)
- Root detection via pitch-class set matching
- Works through inversions
- Live chord name display
- Note name sub-display
- Flash animation on chord change

**Deliverable:** `index.html` — 534 lines, ~19 KB, zero dependencies

**Verdict:** Complete, polished browser instrument. All 3 phases finished, 16/16 checks passed. Ready for use or further enhancement.

---

## Cross-Cutting Analysis

### Common Technical Patterns

| Pattern | Projects Using It | Notes |
|---------|-------------------|-------|
| Local-first storage | Dev's Memory, Doodle Scribe, FocusFlow, Prompt CLI | Consistent privacy-first, no-cloud preference |
| React + TypeScript | Doodle Scribe, FocusFlow, Dev's Memory | Strict mode, modern hooks patterns |
| Electron for desktop | Dev's Memory | Heavy (150MB RAM baseline); Tauri migration considered |
| Python CLI | Prompt CLI, Agent Audit Trail | Click for CLI, Jinja2 for templating |
| Web Audio/MIDI APIs | Small Piano | Browser-native, zero dependencies |
| MCP integration | Dev's Memory | Unique superpower — no competitor has this |
| EU AI Act compliance | Agent Audit Trail | Regulatory deadline tailwind (Aug 2026) |

### Build Status Patterns

**Category 1: Fully Built and Working (4 projects)**
- Small Piano — complete instrument
- Doodle Scribe — enhanced drawing app
- Dev's Memory — desktop snippet manager with MCP
- FocusFlow — core app live, hidden features need UI

**Category 2: Design Complete, Build Ready (2 projects)**
- Agent Audit Trail — 51 tasks specified, 6 gaps need fixing
- Prompt CLI — model orchestration strategy, ready to execute

### Performance Debt

| Project | Issue | Severity | Fix Status |
|---------|-------|----------|------------|
| Dev's Memory | `systeminformation` CPU sampling | Medium | Identified, not implemented |
| Dev's Memory | Electron RAM baseline (~150MB) | Acceptable | No fix (architectural) |
| Dev's Memory | File watcher write loops | Low | Debounce fix identified |
| FocusFlow | Hidden logic without UI | N/A | Logic exists, UI needed |

### Differentiation Analysis

| Project | Unique Element | Defensibility |
|---------|---------------|-------------|
| Dev's Memory | MCP server integration (agents read/write cheatsheet) | High — no competitor has this |
| Small Piano | Zero-dependency, 19KB single file | Medium — easy to clone, but complete |
| Agent Audit Trail | HMAC-SHA256 chain + EU AI Act field mapping | Medium — spec is public, implementation matters |
| Doodle Scribe | AI refinement layer | Low — many drawing apps adding AI |
| Prompt CLI | Multi-model orchestration (architect/editor/utility) | Medium — pattern is replicable |
| FocusFlow | Hidden features already in codebase | N/A — just needs UI exposure |

---

## Recommendations

### Immediate Actions (Next 7 Days)

1. **Agent Audit Trail:** Fix 6 blocking gaps before any implementation begins:
   - `verify_chain()` signature → `key_lookup: Callable[[str], bytes]`
   - LangGraph checkpoint mapping → separate event type
   - CrewAI spec → add non-LangChain fallback
   - `session_chain_heads` → `SECURITY DEFINER` function
   - PII tokenization → mapping storage spec
   - Archive verification → JSONL verification procedure

2. **FocusFlow:** Surface the 4 hidden features — add UI for:
   - Due date input in task forms
   - Category input in forms
   - Focus metrics display (`pomodorosCompleted`, `totalFocusTime`)
   - Export/Import JSON buttons
   *All logic already exists in `taskService`.*

3. **Dev's Memory:** Replace `systeminformation` with Node's built-in `os` module to eliminate fan noise.

### Medium-Term Priorities (Next 30 Days)

4. **Prompt CLI:** Execute the 3-phase build using Aider with the Qwen model strike force:
   - Phase 1: Architect prompt generates task list
   - Phase 2: Editor model implements
   - Phase 3: Advanced prompt engineering features

5. **Doodle Scribe:** Consider SVG export enhancement and layer system completion.

6. **FocusFlow:** Implement drag-and-drop Kanban (library selected, design complete).

### Kill / Defer Decisions

- **Dev's Memory → Tauri migration:** Evaluate but do not execute unless performance complaints persist after `systeminformation` fix.
- **Agent Audit Trail hosted tier:** Defer GDPR compliance decisions until SDK core is built and tested.

---

## Comparison with Ideas Archive

| Dimension | Ideas Archive | Repo Project Reports |
|-----------|--------------|----------------------|
| Project count | 6 | 6 |
| Files | 27 | 33 |
| Built ratio | 0% | 67% |
| Avg. maturity | Research/spec | Working code + specs |
| Technical debt | None (no code) | Identified, documented |
| Next action | "Start building" | "Fix gaps / surface features" |
| Strongest project | Shady Clause Detector (build-ready) | Dev's Memory (built + unique MCP) |

---

## Document Statistics

| Metric | Value |
|--------|-------|
| Total projects | 6 |
| Total files | 33 |
| Built and working | 4 |
| Design complete, unbuilt | 2 |
| Desktop apps | 1 (Dev's Memory) |
| Web apps | 4 (Doodle Scribe, FocusFlow, Small Piano, AAT hosted tier) |
| CLI tools | 1 (Prompt CLI) |
| Unique superpowers | 1 (MCP integration in Dev's Memory) |

---

## Conclusion

This archive represents a **significantly higher execution rate** than the Ideas folder. Four of six projects are built and working; two are build-ready with complete specifications.

**Strongest immediate value:**
1. **FocusFlow** — surface 4 hidden features (1–2 days of UI work, high impact)
2. **Dev's Memory** — fix performance (1 hour, high daily quality of life)
3. **Small Piano** — complete, can be shipped or enhanced freely

**Strongest strategic value:**
1. **Agent Audit Trail** — EU AI Act deadline (Aug 2026) creates time-boxed opportunity
2. **Prompt CLI** — model orchestration pattern could generalize to other projects

The pattern here is different from Ideas: less research, more implementation logs, active bug tracking, and clearer next actions tied to specific code changes.

---

*End of Summary and Evaluation*
