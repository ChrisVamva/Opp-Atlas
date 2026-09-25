# Tools — Master Summary
*Compiled: April 28, 2026*
*Covers: Tools (How to Build an Agent), Tools 2, Tools 3, Tools 4, Tools 5*

---

## What This Folder Is

The `Tools/` folder is the **top-level index of the research intelligence lineage** for agentic infrastructure in the Code vault. It holds five sequential research layers — from foundational architectural philosophy through live market intelligence — each one building on the last. Collectively they form a complete operational playbook for the sovereign AI stack.

---

## Files at a Glance

| File | Source Layer | Focus |
|------|-------------|-------|
| `06_TOOLS2_RESEARCH.md` | Tools 2 | API pricing, OpenRouter leaderboard, strategic frameworks, browser agents, coding agent benchmarks |
| `Comprehensive Summary of 🕵️How to build an agent.md` | Tools (original) | Agent architecture philosophy, observability, routing, token discipline, spec-driven execution |
| `Tools 3 — Research Intelligence Summary.md` | Tools 3 | IDE audits, VS Code extensions, terminal agents, model price-to-performance, free model directory, platform audits |
| `Tools 4.md` | Tools 4 | Sovereign stack design, Agno, Qwen ecosystem, memory/RAG, prompt optimization, Obsidian workflows |
| `Tools 5.md` | Tools 5 | April 2026 landscape scout: rustyhand, Pydantic AI, Reasonix, multi-agent framework comparison, production readiness |

---

## Layer-by-Layer Summary

---

### Layer 0 — How to Build an Agent (Foundational)

The original philosophy layer. Not a tool list — a systems engineering doctrine.

**Core thesis:** Agent quality comes from architecture, not smarter models. A sovereign agent must be planned, observable, routed, token-disciplined, extensible, and resilient.

**Architectural blueprint:**
1. Planner model — decomposition, design, strategy
2. Executor/editor model — edits, commands, implementation
3. Adaptive router — task-to-model matching
4. Telemetry stack — traces, latency, token usage, failures
5. State/memory tools — durable knowledge without prompt bloat
6. Tool integrations — filesystem, shell, APIs, workflow automations

**Key infrastructure picks:**
- **Arize Phoenix** — tracing and observability layer, used like a debugger for agent systems
- **LiteLLM** — unified proxy, model aliasing, fallback routing, budget controls
- **Aider architect mode** — planner/executor separation in practice
- **RouteLLM / Adaptive Broker** — intelligent routing by difficulty, quota, latency
- **Self-healing router** — adapts under provider throttling, avoids hard failures

**Six design lessons:**
1. Don't build an agent as one giant prompt
2. Measure everything (latency, tokens, failures, routing)
3. Separate intelligence from execution
4. Optimize for failure recovery
5. Favor modular tools over monoliths
6. Treat token budget as architecture

---

### Layer 2 — Market Intelligence (Tools 2)

Filed April 2026. The pricing, benchmarks, and strategic frameworks layer.

**API pricing hierarchy (April 2026):**

| Tier | Models | Combined $/1M |
|------|--------|--------------|
| No-budget | Claude Opus 4.6, o3 | $30–50 |
| Balanced flagship | Sonnet 4.6, Gemini 2.5 Pro, GPT-4.1, DeepSeek V4 | $1.50–18 |
| Cost-effective | Gemini 2.5 Flash, DeepSeek V4 cached, Haiku 4.5 | $0.40–7.50 |
| Open-source | Llama 4, Mistral Small 3.2 | $0.17–0.80 |

**DeepSeek hidden discounts (critical for batch workflows):**
- Cache hit discount: 90% off input ($0.03/1M vs $0.30/1M)
- Off-peak discount: 50% off everything (~11 PM–7 AM Beijing time)
- Combined effect: 75–90% cost reduction for stable-prefix batch workflows

**OpenRouter market shift (April 2026):**
- Chinese providers now hold 51.2% of weekly token volume
- Open-weight models: 46% of all tokens
- Tool call rate: <5% → >25% in 12 months (1 in 4 API calls is now agentic)
- 50% of all output tokens are internal reasoning tokens — this category didn't exist 13 months ago
- MiMo-V2-Pro (Xiaomi): went viral as anonymous "Hunter Alpha," revealed as 1T parameter MoE, now #1 on OpenRouter

**Strategic frameworks:**
- **70:2 Model Arbitrage**: 80% of results at 2% cost. Nvidia proof case: 685 curated training examples turned an 8B model from 14% → 96% accuracy at 98% cost reduction.
- **AI Solution Factory**: shift from building solutions to building infrastructure that produces infinite solutions. Four-layer architecture: State (SQLite) → Sensor (Steel) → Logic (Agent-TARS) → Orchestration (n8n).

**Browser agent stack:**
- Steel (infrastructure/proxy layer) + Browser-Use (LLM-to-DOM middleware) covers 90% of tasks
- UI-TARS (vision, pixel-level, ByteDance): for the 10% of tasks with no API and no scrapeable DOM
- Skyvern (9/10): vision-language navigation by semantic intent, near-zero CSS maintenance
- Firecrawl (9/10): turns any URL into clean LLM-ready Markdown

**Coding agent benchmarks (arXiv:2602.08915):**
OpenAI Codex 79.9% → Cursor 74.4% → Claude Code 72.6% → Devin 68.0% = Copilot 68.0%

Kimi K2 + OpenHands: 4.33B tokens burned in production — the real signal of adoption.

---

### Layer 3 — Architect-Grade Audits (Tools 3)

Filed April 14–16, 2026. Formal audits with live evidence citations and explicit Orange Tomato verdicts.

**IDE Audit — Kiro vs. Windsurf:**
- Kiro: "Define first, then execute." Spec system (requirements → design → tasks), steering files version-controlled in repo, Agent Hooks (file event triggers), Powers = MCP + steering + hook bundled. CLI mode: ~0.3 GB RAM.
- Windsurf: "Flow first, then remember." Cascade indexes entire codebase, causal error correlation, SWE-1.6 model ($0.30/$1.50/1M). Free tier: 25 premium prompts/month + unlimited SWE-1 fallback (never locks out — wins over Cursor/Copilot).
- **OT Verdict:** Kiro primary (audit trail built-in, governance via steering files); Windsurf for rapid prototyping. Hybrid: Kiro for architecture → Windsurf for experiments → Kiro CLI + Kestra for production.

**VS Code Extension Audit — Roo Code vs. Kilo Code:**
- Roo Code: 6-mode architecture (Code/Architect/Ask/Debug/Orchestrator/Custom), Boomerang pattern (subtasks in isolated context windows, only summary returned to parent), sticky model assignment per mode, DeepSeek cache optimization maximized via stable `.roo/rules/` files.
- Kilo Code: parallel Agent Manager via Git worktrees, structured compaction (Goals/Discoveries/Accomplishments/Modified Files), OAuth MCP support. More platform-dependent.
- **OT Verdict:** Roo Code wins for sovereign BYOK stack (pure BYOK, Git-trackable rules, best local MCP stability). Kilo Code wins for parallel 24h+ autonomous sessions.

**Recommended daily cost config (Roo Code):**
Ask/Orchestrator = Gemma 4 31B free ($0.00) | Code = DeepSeek V3.2 ($0.64/1M) | Architect = Claude Opus 4.6 (sparingly) | ~$0.43/day per research session.

**Terminal Agent Audit — Claude Code vs. OpenCode:**
- Claude Code fails with free models architecturally (Anthropic `tool_use` schema mismatch with non-Anthropic models, hardcoded beta headers, hardcoded model names). Cannot be fixed with environment variables.
- OpenCode: Vercel AI SDK normalizes tool call formats across providers. Provider-neutral agentic loop. Configurable per-tool output limits. Structured 5-heading compaction.
- **OT Verdict:** OpenCode decisive winner for free-model sovereign stack. Use Claude Code only with native Anthropic API/Pro.

**Coding Model Price-to-Performance (April 15, 2026):**

| Model | Combined $/1M | SWE-bench | LiveCodeBench v6 |
|-------|--------------|-----------|-----------------|
| Claude Opus 4.6 | $30.00 | ~81% | — |
| MiniMax M2.7 | $1.50 | ~80% | ~72% |
| DeepSeek V3.2 | $0.64 | ~68% | ~60% |
| Gemma 4 31B | $0.00 | ~71% | **80%** |

Gemma 4 31B free scores higher on LiveCodeBench v6 than any paid model under $1.50. MiniMax M2.7 at $1.50 is the first model worth paying for above Gemma.

**Free Model Directory (OpenRouter, April 16, 2026):**
- Nemotron 3 Super 120B: 1M context FREE — best for Architect role
- Qwen3 Coder 480B: 262K context FREE — best for coding tasks
- Gemma 4 31B: primary working model
- Rate limits: 20 req/min, 200 req/day per model

**Platform Audits:**
- **Kestra 2.0**: $25M Series A, 30K+ orgs, 2B+ workflows/2025. Kestra 2.0 (in development): pluggable queue backends, gRPC workers, mTLS, S3/blob output extraction. Not a Dify competitor — infrastructure orchestration as code.
- **Mastra 1.0**: $22M Series A, 23K GitHub stars. TypeScript-native, Vercel AI SDK, 4-tier memory (Observational/Working/Episodic/Semantic), graph-based DAG workflows with human-in-the-loop suspend/resume.
- **Dify v1.13**: $30M Pre-A ($180M valuation), 130K GitHub stars, 1.4M machine deployments. Visual LLMOps platform, NOT Kestra competitor. Chatflow (stateful, multi-turn) vs. Workflow (stateless, API-triggered). 10-branch parallel execution, 60–70% latency reduction.

---

### Layer 4 — Sovereign Stack Design (Tools 4)

Filed April 2026. Design dossier for a personal sovereign AI operating environment.

**Core philosophy:** Build modular, Windows-friendly, local-first AI infrastructure. Treat models as swappable components. Route by cognitive difficulty.

**Three-role model mapping:**
- Terminal executor / hands: `qwen3-coder-flash` (cheap, fast)
- Architect / brain: `qwen3-coder-480b-a35b-instruct` (large, capable)
- Failsafe / deep reasoner: `qwen3-235b-a22b-thinking` or `qvq-max` (reserved for hard problems)

**Strongly favored tools:**
- **Agno** (formerly Phidata): lightest agent orchestrator — minimal RAM, fast instantiation, Windows-stable, native SQLite, no LangChain bloat. Core adoption candidate for sovereign local stack.
- **Mem0**: durable memory and personalization layer. Injects only relevant memories, reduces prompt bloat. Considered essential for evolving from one-off prompts to a long-term AI peer.
- **LiteLLM + Arize Phoenix**: local routing and observability stack. ~200MB total RAM, detailed trace/token logging, budget guardrails, latency-based routing. The sovereign operations baseline.
- **Aider architect mode**: planner/executor split. DeepSeek-V3.2 as architect model even under low RPM — deliberate, high-value prompts only.
- **n8n**: connective automation tissue.
- **NotebookLM**: multimodal synthesis layer over personal knowledge bases. Brand/style checker via reverse-RAG editing. Recommended for vault synthesis and audio review.

**Prompt optimization stack:**
MLflow (evaluation/versioning) + TextGrad (iterative prompt mutation) + LiteLLM (routing). DSPy powerful but expensive at compile time. PromptWizard: too heavy, skip.

**Memory integration log (claude-mem):** Successfully connected to Claude Code, Gemini CLI, OpenClaw, Windsurf, Codex CLI, Cursor. Partial failures: OpenCode (build artifact missing), Antigravity (corrupt JSON). Cross-tool memory is feasible, operational polish varies.

---

### Layer 5 — Production Landscape (Tools 5)

Filed April 28, 2026. LUX scout batch: production readiness signals, deep-evidence tool files, comparative analyses.

**Top 3 for sovereign stack (LUX synthesis):**
1. **rustyhand** — execution layer. Rust-native Agent OS, one binary ~32MB, 117K LOC, 1,400+ tests. 37 agents, 40 templates, 26 LLM providers, 37 channel adapters, MCP + A2A, credential vault (AES-256-GCM), RBAC, audit trail. Telegram-first: autonomous agents push results without prompting.
2. **Activepieces** — orchestration layer. ~400 MCP servers, AI Agents + workflow automation, direct n8n competitor, more MCP-native.
3. **Reasonix** — reliability layer. DeepSeek-native agent CLI, MIT-licensed, ~30× cheaper than Claude Code, 94.4% cache hit, Tool-Call Repair for malformed DeepSeek output, edit-as-SEARCH/REPLACE with `/apply` gate.

**Also covered in depth:** Pydantic AI (type-safe, FastAPI-for-GenAI), Pi/OpenClaw (minimal 4-tool agent philosophy, branching sessions, software building software).

**Multi-agent framework quick verdict:**
LangGraph (complex stateful) | AutoGen (adaptive conversational) | CrewAI (role-based hierarchical) | OpenAI Swarm (lightweight prototyping) | LangChain (modular single-agent)

**April 2026 macro signals:** governance is table stakes; cost observability is a product category; 370 new AI papers in cs.AI in one day; open-weight models at 46% of all OpenRouter tokens.

---

## Cross-Layer Patterns

These themes recur across all five layers:

| Pattern | First Appeared | Status |
|---------|---------------|--------|
| Planner/executor split | Layer 0 | Confirmed best practice — Aider, Kiro, Reasonix all implement it |
| LiteLLM as routing backbone | Layer 0 | Adopted — foundational across stack |
| Arize Phoenix for observability | Layer 0 | Confirmed — first-mover with real backing (Tools 5 Tier 2) |
| DeepSeek cache economics | Layer 2 | Critical — 90% input discount, Reasonix built around it |
| Free models viable at Tier 1 | Layer 3 | Confirmed — Gemma 4 31B beats paid models on LiveCodeBench |
| Roo Code as sovereign VS Code extension | Layer 3 | Adopted — Boomerang, sticky modes, BYOK |
| OpenCode over Claude Code for free models | Layer 3 | Decisive — architectural incompatibility confirmed |
| Agno as lightweight orchestrator | Layer 4 | Adopt — fastest, lightest, Windows-stable |
| rustyhand as production Agent OS | Layer 5 | High conviction — strongest production signal in corpus |
| MCP as the connective protocol | Layer 3–5 | Ubiquitous — all serious tools now MCP-native |

---

## Recommended Stack (Full Picture)

Synthesized from all five layers, weighted toward sovereign, local-first, token-conscious operation:

| Layer | Tool | Role |
|-------|------|------|
| Execution OS | rustyhand | Autonomous agents, Telegram push, Rust reliability |
| Agent framework | Agno | Lightweight orchestration, local RAG, no bloat |
| Orchestration | Activepieces / n8n | Workflow automation, ~400 MCP servers |
| VS Code extension | Roo Code | BYOK, Boomerang context isolation, DeepSeek cache optimization |
| Terminal agent | OpenCode | Free model compatibility, provider-neutral, structured compaction |
| Model routing | LiteLLM | Unified proxy, fallback, budget controls |
| Observability | Arize Phoenix | Tracing, token counts, latency, failure analysis |
| Memory | Mem0 | Durable preferences, anti-bloat injection |
| Coding CLI | Reasonix | DeepSeek-native, 30× cheaper, Tool-Call Repair |
| IDE | Kiro (primary) / Windsurf (prototyping) | Spec-driven vs. velocity-optimized |
| Synthesis layer | NotebookLM | Vault cross-referencing, audio review, style checking |
| Planning model | Claude Opus 4.6 | Sparingly — architecture and critical decisions only |
| Working model | DeepSeek V3.2 | Daily sustained pipelines, ~$2–8/month |
| Free tier | Gemma 4 31B / Qwen3 Coder 480B | Ask mode, scouting, boilerplate |

---

## Key Numbers Across the Corpus

| Fact | Value |
|------|-------|
| Real cost spread (GPT-4 to Mistral Small) | 150× |
| Nvidia fine-tuning proof: training examples needed | 685 |
| Nvidia fine-tuning proof: cost reduction achieved | 98% |
| Browser Use 2.0 accuracy (beats all frontier LLMs) | 83.3% |
| Chinese model share of OpenRouter traffic | 51.2% |
| Current tool call rate on OpenRouter | 25% (was <5% 12 months ago) |
| Output tokens that are internal reasoning | 50% |
| Gemma 4 31B LiveCodeBench v6 score | 80% FREE |
| Reasonix cache hit rate vs generic harness | 94.4% vs 46.6% |
| rustyhand codebase | 117K LOC, 1,400+ tests, ~32MB binary |
| Kestra production organizations | 30,000+ |
| Dify machine deployments | 1.4M |
| arXiv cs.AI papers in one day (Apr 28) | 370 |
| DeepSeek cache discount | 90% off input |
| DeepSeek off-peak discount | 50% off everything |
