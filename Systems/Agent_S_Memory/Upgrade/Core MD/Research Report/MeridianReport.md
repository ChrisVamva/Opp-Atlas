# MeridianReport — Project Summary
*Generated: April 2026*
*Source: Full read of MeridianSignal vault (CHIP.md, INDEX.md, ActiveWork.md, IdeaFrontier.md, Projects/, Knowledge/AgenticSystems.md)*

---

## 1. What This Project Is

MeridianSignal is the research and build system of **ChrisVamva** — an independent researcher, builder, and system architect working at the intersection of agentic AI systems, developer tooling, and practical software products.

The project has two interlocking dimensions:

- **The Pipeline** — an 8-stage AI agent system that transforms raw ideas into validated, designed, and planned software products
- **The Memory System** — a compressed, git-native markdown vault that serves as persistent context for the pipeline and all sub-projects

The pipeline is the central unlock. All other projects, tooling decisions, and optimization work are explicitly blocked or sequenced behind it.

---

## 2. The MeridianSignal Pipeline

### Architecture

```
Stage 1  Brainstormer    →  8 raw ideas from constraints
Stage 2  Evaluator       →  3 survivors (hard filter)
Stage 3  Web Researcher  →  market-validated brief per survivor
Stage 4  Variation       →  3–5 distinct variants per survivor
Stage 5  Synthesis       →  1 superior synthesized concept (not a blend — a new thing)
Stage 6  Designer        →  design.md (UI/UX spec)
Stage 7  Planner         →  plan.md (implementation plan)
Stage 8  Executor        →  builds via Aider integration
```

### Core Design Principles

**Specialist agents, not generalists.** Each stage has one explicit job and NOT-DO rules that prevent scope creep. Brainstormer does not evaluate. Evaluator does not research. Synthesis does not pick a winner — it forges a new concept from the best elements of all variants.

**Structured handoffs.** Every stage output is typed JSON or structured markdown. No free-text passing between agents.

**Load-on-need memory.** Agents receive CHIP.md + only the file relevant to their stage + the previous agent's structured output. Context windows stay lean.

**No framework.** LangGraph, AutoGen, and CrewAI were all evaluated and rejected. Custom agent orchestration only — the pipeline's fixed, known structure made frameworks fight the architecture more than help it.

### Current Status

| Stage | Status |
|-------|--------|
| Brainstormer prompt | ✅ Drafted |
| Evaluator prompt | ✅ Drafted |
| Web Researcher prompt | ✅ Drafted |
| Variation prompt | ✅ Drafted |
| Synthesis prompt | ✅ Drafted |
| Designer prompt | ✅ Drafted |
| Planner prompt | ✅ Drafted |
| Executor (Aider integration) | 🔄 In Progress |
| End-to-end test run | ❌ Not done |
| DSPy optimization layer | ⏸ Blocked — needs training data |

**Active blockers:**
- design.md output format needs standardization before Designer → Planner handoff works reliably
- Aider `--architect --message` flag integration needs testing for non-interactive Executor mode
- No end-to-end run has been completed yet

---

## 3. Sovereign Tech Stack

| Layer | Tool | Notes |
|-------|------|-------|
| Routing | LiteLLM | Adopted. Not switching. |
| Synthesis model | Claude Sonnet | Primary reasoning model |
| Code model | DeepSeek V3 / V3.2 | Aider architect mode backend |
| Draft/free model | Qwen 2.5 (7B, 72B) | Zero-cost via Together AI free tier |
| Local runtime | Ollama | Sovereignty, sensitive data, DSPy runs |
| Observability | Arize Phoenix (local) | Free, local, adopted |
| Coding agent | Aider architect mode | Primary build tool |
| Memory | This repo (git-native markdown) | Source of truth |

**Locked decisions (do not relitigate):**
- No Electron — 150MB RAM baseline rejected across all tools
- LiteLLM as router — final
- Arize Phoenix for observability — final
- No framework for the pipeline — custom orchestration only
- DSPy paused until pipeline ships and generates training data

---

## 4. Active Projects (Priority Order)

| # | Project | Status | Description |
|---|---------|--------|-------------|
| 1 | **MeridianSignal Pipeline** | 🔥 Active | Core. Ship v1. Everything else waits. |
| 2 | **FocusFlow** | 🔥 Active | Pomodoro tracker — adding AI task decomposer + session summarizer |
| 3 | **DoodleScribe** | 🔥 Active | Enhancement phase — intent-first input before conversion |
| 4 | **DSPy Mission** | ⏸ Paused | Phases 1–4 complete. Resumes after pipeline ships. |
| 5 | **ShadyClause Detector** | 📋 Plan ready | Contract transparency tool. Build not started. |
| 6 | **Keyword Sleuth** | 🔍 Research | Common Crawl language mining tool. Research validated. |
| 7 | **Dev's Memory** | 🔍 Evaluating | Decision needed: Tauri vs web app. |
| 8 | **Prompt CLI** | 📋 Plan ready | CLI prompt management tool. Build not started. |

### FocusFlow (Active Detail)
Functional Pomodoro app (TypeScript + React + Zustand). Enhancement phase adds:
- AI task decomposer via Qwen 2.5 72B (on-demand)
- Session summarizer via Qwen 2.5 7B (auto, post-Pomodoro)
- Weekly focus score via Claude Sonnet (once/week)
- Hidden power features via keyboard shortcuts: focus intensity mode, task carry-forward, session export

### ShadyClause (Plan Ready)
Contract clause transparency detector. Open question before build: 5 user interviews needed to confirm whether people actually want to understand contracts before signing, or just sign anyway.

---

## 5. Memory System

### Architecture

The vault was restructured in **April 2026** — compressed from 221 files across fragmented folders into 15 clean, purposeful files.

```
CHIP.md           Master context — always load first (~4KB)
INDEX.md          Navigation map — load order and file descriptions
Identity.md       Research identity, terrain, core themes
ActiveWork.md     Current investigations, weekly priorities, blocked items
IdeaFrontier.md   Open questions, speculative ideas, retired concepts
Protocols.md      Memory update rules, compression protocols, anti-repetition
Knowledge/        3 distilled knowledge files
Projects/         8 project files (one per project)
Agents/           8 agent prompt files
```

### What Was Archived

The following were removed in the April 2026 restructuring:
- `Context Organisation/` — 80+ fragmented files → compressed into Knowledge/ + Projects/
- `MeridianSignal_S_Memory/` — 140+ files → compressed into 15 clean files
- `Pending Update/` — staging folders committed and cleared
- Loose root files — consolidated into appropriate files

All knowledge preserved. Nothing lost — only compressed.

---

## 6. Knowledge Foundations (AgenticSystems.md)

### Framework Decision Matrix

| Framework | Best For | Avoid When |
|-----------|----------|-----------|
| LangGraph | Complex stateful workflows, cycles, human-in-loop | Simple linear pipelines |
| AutoGen | Multi-agent conversation loops | Deterministic output ordering required |
| CrewAI | Role-based teams, quick setup | Fine-grained state control needed |
| DSPy | Prompt optimization, pipeline compilation | Human-readable prompts required at all times |
| **Custom** | Full control, fixed architecture | Framework already solves 80%+ of needs |

**Ruling principle:** Use a framework if it solves 80%+ of orchestration needs out of the box. Build custom if the framework fights the architecture.

### Agent Memory Patterns

Three patterns govern all MeridianSignal agent work:

**Load-on-Need** — agents receive only CHIP.md + stage-relevant file + previous structured output. No full vault dump.

**Compression-Before-Storage** — no agent stores raw output. Core decision/insight is extracted, conversational scaffolding stripped, then written to the correct memory section.

**Anti-Drift** — every agent prompt explicitly states what it must NOT do, preventing scope creep across stage boundaries.

---

## 7. Idea Frontier Snapshot

### Open Questions (Unresolved)

- What is the right grain size for an agent stage? (Gut: one stage = one judgment call)
- Can Stage 5 Synthesis be reliably automated, or does it always regress to safe middle ground?
- At what workload volume does self-hosted Ollama become cheaper than API calls?
- Is there a real market for "contract transparency before signing"? (ShadyClause premise)

### Speculative Ideas (Not Yet Evaluated)

- **Pipeline Replay** — record every run, replay with different models for systematic comparison
- **Agent Debate Mode** — two Evaluators with opposing criteria, synthesized output
- **Memory Diff Tool** — CLI that visualizes what changed between vault versions
- **Sovereign Benchmark** — quantify the quality cost of going fully local (Ollama vs API)

### Retired Concepts

| Idea | Reason |
|------|--------|
| Electron shell | 150MB RAM baseline — unjustifiable |
| LangGraph for pipeline | Fights the architecture |
| AutoGen for debate | Non-deterministic output ordering |
| Proprietary vector DB | Vendor lock-in, no local option |
| Chrome extension for ShadyClause | Phase 3 only — don't build before Phase 1 API validated |

---

## 8. Immediate Next Actions

**This week (priority order):**

1. **Standardize design.md format** — define sections (Overview, Components, Interactions, State Management, API Requirements) and update the Designer prompt → unblocks the Designer → Planner handoff
2. **Build Aider Executor integration** — test `aider --architect --message "$(cat plan.md)" --no-auto-commits`
3. **Run full end-to-end pipeline on one test idea** — first live fire
4. **FocusFlow task decomposer** — implement Qwen 2.5 72B integration for task breakdown
5. **DoodleScribe intent templates** — add intent context input + 5 template options

**Unblocking sequence:**
```
Pipeline v1 ships
    → 10 pipeline runs collected
    → DSPy Phase 5 resumes
    → ShadyClause / Keyword Sleuth / PromptCLI build decisions
```

---

## 9. Project Health Assessment

**Strengths:**
- Architecture is fully designed and documented. All 8 agent prompts drafted.
- Memory system is clean, compressed, and maintainable (15 files vs 221).
- Locked decisions are genuinely locked — no framework churn.
- Sovereign stack is coherent and cost-efficient (free tier for 90% of inference).

**Risks:**
- No end-to-end run yet. Stage integration assumptions are untested.
- design.md format gap is a known blocker on the critical path.
- Together AI free tier limits unconfirmed — FocusFlow and PromptCLI both depend on it.
- DSPy optimization layer has no training data until pipeline runs at scale.

**Signal for completion:** The pipeline is ready to run as soon as the Executor integration is complete and design.md format is standardized. Both are in-progress, not blocked on external factors.

---

*End of MeridianReport. Update after first successful end-to-end pipeline run.*
