# Tools 3 — Research Intelligence Summary
_Compiled from 15 files. April 2026. All research dated April 14–16, 2026._
_Source folder: Code/Tools 3/_

---

## WHAT TOOLS 3 IS

The most current intelligence layer in the vault — filed April 14–16, 2026.
Unlike Tools/ (older overviews) and Tools 2/ (pricing, benchmarks, strategic frameworks),
Tools 3 is structured as formal audits: each file is an architect-grade technical brief
with live evidence citations, screenshots verified, and explicit Orange Tomato verdicts.

Eight distinct decision categories covered:
IDE selection · VS Code extension selection · Terminal agent selection ·
Model price-to-performance · Free model directory · Platform audits (Kestra, Mastra, Dify) ·
Specific model audit (Elephant Alpha) · Stack updates + product advisor blueprint

---

## 1. IDE AUDIT: KIRO vs. WINDSURF

**File:** ARCHITECT BRIEFING Kiro IDE vs. Windsurf IDE.md

### The fundamental split
- **Kiro:** "Define first, then execute." Spec-driven, auditable, AWS-grade structure
- **Windsurf:** "Flow first, then remember." Context-aware, velocity-optimized

### Kiro's differentiating architecture
Three-document spec system stored at `.kiro/specs/{feature}/`:
- `requirements.md` → user stories in EARS notation
- `design.md` → technical architecture and sequence diagrams
- `tasks.md` → implementation checklist

Steering files: markdown documents encoding project knowledge, version-controlled,
team-shared, live in the repo. Every engineer gets identical AI behavior.

Agent Hooks: file system event triggers running agent tasks without user initiation.
`fileEdited` → auto-generate tests on save. `fileCreated`, `fileDeleted`, `agentStop`.
This is ambient intelligence — acts in the background while you code forward.

"Powers" = MCP server + steering file + hook bundled as a reusable agentic capability.
Powers Hub (preview): marketplace for sharing Powers across teams.

### Windsurf's differentiating architecture
Cascade: indexes entire codebase, maintains "shared timeline" of all developer actions,
correlates terminal errors with source code causally (not just textually).

SWE-1.6 model: $0.30/$1.50 per 1M in/out. Also routes to Claude Opus 4.6, Sonnet 4.6,
GPT-5.4, Kimi K2.5. "Diagnostic Certainty" confirmed NOT a documented feature.

Memory system: Automatic Memories (AI-generated, opaque, stored in proprietary metadata)
vs. User-Defined Rules (`.windsurf/rules/` — Git-trackable). The Memories system
is the trust gap for auditability-focused workflows.

### Hardware reality (16GB RAM / 1GB VRAM constrained)
- Kiro CLI: ~0.3 GB → fits alongside Dify + Ollama ✅
- Windsurf IDE: ~1.8 GB (Cascade indexer) → tight ⚠️
- Kiro IDE standard: ~1.5 GB → fits ✅

### Orange Tomato verdict
**Primary: Kiro (with CLI mode for constrained hardware)**
Rationale: spec system IS the audit trail; steering files ARE governance;
Powers are the correct abstraction for research tools; CLI wins hardware constraint.

**Use Windsurf for:** rapid prototyping, when Figma/Jira one-click matters today,
collaborative sessions where velocity > structure.

**Hybrid workflow:**
Phase 1 → Kiro (architecture definition, specs)
Phase 2 → Windsurf (exploratory experiments, prototype fast)
Phase 3 → Kiro CLI + Kestra (production pipeline, deterministic, auditable)

---

## 2. WINDSURF FREE TIER: THE REAL NUMBERS

**File:** 👑 The Crown Belongs to Windsurf👑.md

### Confirmed free tier limits (April 2026, new system)
- **25 premium prompt credits/month** — not 10/day as previously reported
- After quota exhausted: unlimited SWE-1 (Cascade Base) and free models (Kimi K2.5 etc.)
- Tab autocomplete: unlimited on all plans
- Each "session" = 1 prompt regardless of internal tool calls

### Free tier comparison table
| Plan | Premium prompts | Autocomplete | Free model fallback |
|---|---|---|---|
| Windsurf Free | 25/month | Unlimited | ✅ Yes — unlimited SWE-1 |
| Cursor Hobby | 50/month (slow) | 2,000/month | ❌ None |
| GitHub Copilot Free | 50/month | 2,000/month | ❌ None |

### Why Windsurf wins on free tier
Windsurf gives fewer premium prompts but never hard-locks you out.
After 25 credits: drop to SWE-1 / Kimi K2.5 and continue indefinitely.
Cursor/Copilot cut you off entirely at the cap.

Windsurf's competitive advantage = B2B enterprise wing subsidizes free tier
to starve out Cursor (which relies on individual $20/month subs).
Proprietary SWE-1 model costs Windsurf near zero to serve.

### Orange Tomato verdict
For 1GB VRAM setup: Windsurf is the absolute king for daily coding.
Never fully locked out. Multi-file agentic editing on cloud servers.
Watch out for Flex Credits upsell prompt when premium credits run out — ignore it.


---

## 3. VS CODE EXTENSION AUDIT: ROO CODE vs. KILO CODE

**File:** WATCHDOG BRIEFING Kilo Code vs. Roo Code.md

### Roo Code: four-mode architecture
| Mode | Tools permitted | Assign to model |
|---|---|---|
| Code | All (read/write/terminal/MCP/browser) | Heavy model |
| Architect | Read-only + markdown write | Heavy model |
| Ask | Read-only — no writes, no terminal | FREE model (Gemma 4 31B) |
| Debug | Read + targeted write + terminal | Heavy model |
| Orchestrator | Task delegation only | FREE model |
| Custom | User-defined | Any |

Boomerang pattern: each subtask runs in its own isolated context window.
Orchestrator receives only the SUMMARY of each subtask result, not the full transcript.
Context never bloats in the parent session. Assign cheap model to Code subtasks.

Sticky model assignment: last model per mode is remembered on switch-back.
Accidentally burning expensive model on Ask queries is prevented architecturally.

DeepSeek cache optimization: stable `.roo/rules-{mode}/` files don't change between requests
→ 90% cache discount ($0.028/M vs $0.28/M cache miss) maximized automatically.

### Kilo Code: platform-level agent manager
Agent Manager runs isolated Git worktrees — multiple agents on same codebase in parallel
without filesystem conflicts. True parallel execution (Roo is sequential via Orchestrator).

Compaction system: threshold-based (configurable ~80%), produces structured summary:
Goals / Discoveries / Accomplishments / Modified Files.
Structured format is more reliable for smaller models than prose summaries.

CRITICAL WARNING for small models: compaction quality depends on the model used
for summarization. Assign DeepSeek V3.2 for compaction even if using Gemma elsewhere.

Kilo Gateway: platform account encouraged. BYOK works but some gateway features
require balance. Less sovereign than Roo for pure BYOK setups.

### MCP stability comparison
- Roo Code: battle-tested for local stdio MCP (Firecrawl + SQLite). Community consensus.
- Kilo Code: MCP Hub, OAuth support, Enterprise admin controls. Restart edge cases with
  local stdio servers still reported (being fixed as of April 2026).

### Orange Tomato verdict
**Winner for sovereign BYOK stack: Roo Code**

Rationale: pure BYOK (no platform account), .roo/ rules are Git-trackable plain files,
local MCP stability is best-in-class, DeepSeek cache optimization maximized.

**When Kilo wins:** parallel autonomous agents, 24h+ background research sessions
requiring structured compaction, teams needing enterprise admin controls,
when OAuth MCP flows required (Google Drive, Jira OAuth).

### Recommended model routing for Orange Tomato stack
```
Ask mode:         Gemma 4 31B free → $0.00
Orchestrator:     Gemma 4 31B free → $0.00
Code/Research:    DeepSeek V3.2   → $0.64/1M
Architect:        Claude Opus 4.6 → $30/1M (use sparingly)
MCP:              Firecrawl stdio + SQLite stdio (local, sovereign)
```
Estimated daily cost for 1 research session: ~$0.43

---

## 4. TERMINAL AGENT AUDIT: CLAUDE CODE vs. OPENCODE

**File:** TERMINAL AGENT BRIEFING Claude Code vs. OpenCode.md

### Why Claude Code fails with free models (confirmed April 2026)
Claude Code expects Anthropic's `tool_use` JSON schema. Gemma 4 31B and other
non-Anthropic models return tool calls in a slightly different format.
Claude Code cannot parse the response → 400 errors and session crashes.

Additional failure modes:
- Beta headers (`context-management-2025-06-27`) injected by Claude Code, rejected by OpenRouter
- Background tasks attempt to call `claude-haiku-4-5` explicitly (hardcoded model name)
- Tool definition overflow: full built-in tool suite sent every request; degrades 31B models

Even with all mitigations (`DISABLE_EXPERIMENTAL_BETAS=true`, routing proxy), Claude Code
with free models is "works until it doesn't" — elevated crash risk on subagents,
long tool chains, or context management features.

**This is architectural, not a config issue. Cannot be fixed by environment variables.**

### Why OpenCode works with free models
Uses Vercel AI SDK as model abstraction layer.
SDK handles tool call format normalization, header stripping, response parsing.
The agentic loop is provider-neutral. OpenRouter works first-class.

OpenCode `opencode.json` config: `"bash": "ask"` is static and Git-tracked.
Claude Code's Shift+Tab mode cycling can drift during a long session — no config persistence.

Compaction: structured 5-heading brief (Task / Completed / Current State / Next Steps /
Key Findings). More reliable for 31B models than Claude Code's prose summaries.
Configurable output limits: `search_result_limit: 50`, `bash_output_limit: 500`,
`file_read_limit: 200` — Claude Code has no equivalent per-tool-class caps.

### Orange Tomato verdict
**Winner for 1GB VRAM sovereign stack: OpenCode — decisive, not close**

**Hybrid use case for Claude Code:** Claude Code is excellent when paired with
native Claude models (Pro subscription or Anthropic API). Use Claude Code for Claude,
use OpenCode for free models via OpenRouter.

---

## 5. CODING MODEL AUDIT: PRICE-TO-PERFORMANCE

**File:** Coding Model Audit — Price-to-Performance Analysis.md
All prices verified from live OpenRouter screenshots, April 15, 2026.

### Full pricing + benchmark table

| Model | Input $/1M | Output $/1M | Combined | SWE-bench | LiveCodeBench v6 |
|---|---|---|---|---|---|
| Claude Opus 4.6 | $5.00 | $25.00 | $30.00 | ~81% | — |
| Claude Sonnet 4.6 | $3.00 | $15.00 | $18.00 | ~79% | — |
| GPT-5.4 | $2.50 | $15.00 | $17.50 | ~80% | — |
| MiniMax M2.7 | $0.30 | $1.20 | $1.50 | ~80% | ~72% |
| DeepSeek V3.2 | $0.26 | $0.38 | $0.64 | ~68% | ~60% |
| Gemma 4 31B FREE | $0.00 | $0.00 | $0.00 | ~71% | **80.0%** |
| Gemma 4 31B paid | $0.13 | $0.38 | $0.51 | ~71% | ~80% |
| GPT-5.4 Nano | $0.20 | $1.25 | $1.45 | ~63% | ~55% |

### Key findings
- Gemma 4 31B scores 80% on LiveCodeBench v6 — higher than DeepSeek V3.2 (60%)
  and matching or exceeding models at $1.50/1M. The free model beats paid models
  on the least-gameable coding benchmark.
- MiniMax M2.7 at $1.50/1M: first model that materially outperforms Gemma on SWE-bench
  (80% vs 71%) while costing 12x less than GPT-5.4.
- Claude Opus 4.6: 47x more expensive than MiniMax M2.7 for a ~1% SWE-bench improvement.
  Only justified for enterprise/client billing where failed refactor cost > API cost.
- Free tier hard limit: 20 req/min, daily token caps. Heavy agentic loops hit this.

### Recommended tiered routing
| Task | Model | Cost |
|---|---|---|
| Occasional coding, quick questions | Gemma 4 31B free | $0 |
| Daily dev work, sustained pipelines | DeepSeek V3.2 | ~$2–8/month |
| Complex multi-file refactors | MiniMax M2.7 | ~$5–20/month |
| Critical/client work, long autonomous | Claude Opus 4.6 | ~$30–100+/month |


---

## 6. FREE MODEL DIRECTORY (April 16, 2026)

**File:** FREE MODEL SELECTION REPORT_OpenRouter $0.00 Tier.md
Live-queried from `openrouter.ai/models?order=pricing&max_price=0` on 2026-04-16.

### Verified free models (all $0.00 in/out)

| Model | Context | Architecture | Notable |
|---|---|---|---|
| **Nemotron 3 Super 120B** | **1M** | 120B Mamba-Transformer MoE | Best for Architect role |
| **Qwen3 Coder 480B** | 262K (ext. 1M) | 480B MoE (A35B active) | Best for coding tasks |
| Gemma 4 31B | 262K | 30.7B Dense | Primary working model |
| Gemma 4 26B A4B | 262K | 26B MoE | Near-Gemma quality |
| Hermes 3 405B | 128K | 405B Dense | Large context reasoning |
| Llama 3.3 70B | 64K | 70B Dense | Stable fallback |
| GPT-OSS 120B | 128K | 120B OpenAI open-weights | OSS-class quality |
| Elephant Alpha | 262K | 100B suspected MoE | See separate audit below |
| MiniMax M2.5 | 192K | MoE | — |
| GLM 4.5 Air | 128K | MoE + Thinking mode | Thinking capability free |
| Gemma 3 27B | 128K | 27B Dense | Previous gen |

Rate limit: 20 requests/min, 200 requests/day per model (all free tier).

### Role assignments (free-only stack)
| Role | Model | Reason |
|---|---|---|
| Architect / planning | Nemotron 3 Super 120B | 1M context, reasoning trace, structured output |
| Coding tasks | Qwen3 Coder 480B | 480B MoE specifically tuned for code |
| General working model | Gemma 4 31B | 80% LiveCodeBench, 262K context |
| Rapid scouting / Ask mode | Gemma 3 27B or Llama 3.3 70B | Lower latency |

---

## 7. ELEPHANT ALPHA MODEL AUDIT

**File:** openrouter elephant-alpha Model Viability Audit.md

**Identity:** Proprietary stealth model released April 13, 2026 by an anonymous lab
via OpenRouter's own namespace (`openrouter/`). No model card, no training lineage,
no open weights. Suspected MoE based on speed-to-parameter ratio.

**Specs:**
- Context: 262K tokens | Output cap: 32K tokens
- Parameters: 100B (self-reported) | Suspected MoE architecture
- Pricing: $0.00 (currently free)
- Throughput: ~87 t/s average, burst up to ~1,000 t/s
- Data logging: ⚠️ ACTIVE — OpenRouter logs prompts for this model
- Function calling: ✅ | Structured output: ✅ | Prompt caching: ✅

**Verdict:** Do not use for sensitive research, competitive intelligence, or
proprietary project data. The active data logging policy makes it unsuitable
for Orange Tomato operational use. Suitable only for benign public-data tasks
where logging is acceptable.

---

## 8. PLATFORM AUDITS

### Kestra 2.0
**File:** Kestra 2.0 — Lead Architect Technical Audit.md

$25M Series A (RTP Global, March 2026). 30,000+ organizations. 2B+ workflows in 2025.
Reference clients: Apple, Toyota, JPMorgan Chase, BHP.
Current stable: Kestra 1.3 LTS (March 3, 2026).

**Kestra 2.0 four architectural changes (in development, not yet released):**
1. Re-architected queue: pluggable backends (JDBC/Kafka/Redis/AMQP) independent of DB
2. Database as single source of truth: queue carries routing signals only (not full payloads)
3. Workers now speak gRPC: fully stateless workers, no DB port exposure required,
   mTLS + service mesh, cross-region deployments now possible
4. Output extraction: large task outputs stored in S3/GCS/blob rather than inline in DB

Kestra vs. Temporal vs. LangGraph state model:
- Kestra: DB as source of truth, configurable durability
- Temporal: event sourcing, full history replay
- LangGraph: pluggable checkpointing snapshots

### Mastra TypeScript Framework
**File:** Mastra TypeScript Framework Comprehensive Technical Briefing.md

$22M Series A (Spark Capital, April 9, 2026). 23,000+ GitHub stars. 1.0 stable January 2026.
Used at: Brex, Marsh McLennan, Indeed, MongoDB, Workday, Salesforce, Replit.

Built on Vercel AI SDK. TypeScript-native. Supports all major model providers.
Agent Editor (April 8, 2026): edit agent instructions at runtime without redeployment.

Four-tier memory system:
- Observational Memory: long-horizon, multi-session (Observer + Reflector background agents)
- Working Memory: active reasoning state (key-value in context window)
- Episodic Memory: task/session-level history
- Semantic Memory: vector RAG store

Workflow engine: graph-based DAG with `.branch()`, `.parallel()`, `.pipe()`,
human-in-the-loop via `suspend()` / `respondToToolSuspension()`.

### Dify Platform
**File:** Dify Platform Audit.md

v1.13.x (April 2026). 130,000+ GitHub stars. $30M Pre-A ($180M valuation, March 2026).
1.4M machine deployments. Enterprise clients: Maersk, ETS, Novartis, Anker.

Critical distinction: Dify is NOT a Kestra competitor.
Kestra = infrastructure orchestration as code.
Dify = visual LLMOps platform / AI application builder with Backend-as-a-Service model.

Chatflow vs. Workflow:
- Chatflow: stateful, multi-turn memory, streaming mid-flow via Answer nodes
- Workflow: stateless, fresh context per run, single End node output, API/schedule triggered

Parallel execution: 10 branches max, 3 nesting levels, 60–70% latency reduction
for 3 simultaneous LLM calls. Variable scoping: branches can only read pre-split variables
(not siblings). Use pre-split node for shared data.

---

## 9. STACK UPDATES & MODELS

### MiMo-V2-Flash + OpenClaw April 2026 stack
**File:** MiMo-V2-Flash+OpenClaw (v2026.4.7).md

Orange Tomato top-tier stack as of April 2026:
| Tool | Status | Role |
|---|---|---|
| OpenClaw v2026.4.7 | PLATINUM | Local Agentic OS + Tool Hub. Active Memory plugin. |
| PydanticAI | PLATINUM | Type-safe agents, schema validation for research data |
| MiMo-V2-Flash | GOLD | 309B total / 15B active per token, 150 t/s, agentic tool-use |
| Mastra | GOLD | TypeScript agent runtime ("FastAPI of agents") |
| LangGraph | GOLD | Multi-agent orchestration for complex stateful loops |

OpenClaw v2026.4.7 Active Memory Plugin: dedicated memory sub-agent pulls relevant
past context before main reply. Eliminates manual context-loading.

Recommended workflow: OpenClaw (orchestration) → PydanticAI (validation) → Claude Code
(final creative execution for stylistic authenticity).

### Antigravity model selection
**File:** Antigravity🧠 Model Selection for Advanced Information Gathering.md

For Advanced Information Gathering tasks:
| Step | Model | Goal |
|---|---|---|
| Scouting | Gemini 3 Flash | Identify 20+ URLs, broad queries, low cost |
| Deep Dive | Claude Sonnet 4.6 | Navigate JS-heavy sites, bypass walls, extract |
| Synthesis | Gemini 3.1 Pro (2M ctx) | Combine all findings into structured report |

Use Opus 4.6 when agent "gets lost" — Thinking mode self-corrects navigation errors.

---

## 10. ADDITIONAL FILES

### AI Solution Factory (duplicate from Tools 2)
**File:** 🔄 The Shift From Building AI Solutions to Building AI Solution Factories.md
Same document as in Tools 2. Summary in Code vault `_OPENCLAW/06_TOOLS2_RESEARCH.md`.

### Product Advisor Chatbot Blueprint
**File:** A concrete, minimal blueprint for a product-advisor chatbot.md
Minimal RAG chatbot blueprint:
1. Web widget → POST /advice endpoint
2. Embed query → vector search (pgvector/Pinecone/Qdrant, k=5–10)
3. Fetch pricing API (cached per product/region)
4. Prompt LLM with retrieved docs + pricing → structured JSON response
5. Return cards/tables/pros-cons to widget

### Composio + Dify + SmolAgents + OpenClaw
**File:** Composio+ Dify+SmolAgents+ OpenClaw+Vercel.md
Earlier stack evaluation (April 2, 2026 — predates most Tools 3 files).
SmolAgents: ~1,000-line library, code-first (agents write/execute Python), spinnable
at massive scale, zero heavy cloud dependency.
Composio: 500+ pre-built tools with native MCP, safe external integrations.

---

## KEY NUMBERS FROM TOOLS 3

| Fact | Value |
|---|---|
| Windsurf free premium prompts | 25/month (not 10/day) |
| Kiro CLI RAM footprint | ~0.3 GB |
| Roo Code Ask mode daily cost (Gemma free) | $0.00 |
| Estimated daily research session cost (Roo config) | ~$0.43 |
| Kestra production organizations | 30,000+ |
| Kestra 2025 workflow executions | 2 billion+ |
| Mastra GitHub stars | 23,000+ |
| Dify GitHub stars | 130,000+ |
| Dify machine deployments | 1.4M |
| MiMo-V2-Flash active parameters | 15B / 309B total |
| MiMo-V2-Flash throughput | 150 tokens/sec |
| Free tier request limit (OpenRouter) | 20 req/min, 200/day per model |
| Elephant Alpha throughput | ~87 t/s avg, ~1,000 t/s burst |
| Nemotron 3 Super 120B context | 1M tokens FREE |
| Qwen3 Coder 480B active parameters | 35B / 480B total |
