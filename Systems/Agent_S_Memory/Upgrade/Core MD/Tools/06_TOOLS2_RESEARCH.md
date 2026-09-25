# Tools 2 — Research Intelligence Summary
_For OpenClaw agent context. Compiled: 2026-04-09. All files dated April 2026._
_Source folder: Code/Tools 2/ (17 files)_

## What Tools 2 is

The most recent research layer in the Code vault. Unlike the older Tools/ folder
(tool evaluations and overviews), Tools 2 is intelligence-grade: sourced benchmarks,
pricing tables with real numbers, strategic frameworks, and deployment tactics.
Filed in the last two weeks. This is the current operational picture.

---

## 1. API PRICING LANDSCAPE (March-April 2026)

### Four-tier model hierarchy

**Tier 1 — No-budget-constraints (agent-heavy)**
- Claude Opus 4.6: $5/$25 per 1M in/out | 1M context | ~72-78% SWE-bench
- o3 (OpenAI): $10/$40 | 200K context | ~95% HumanEval

**Tier 2 — Balanced flagship (best value for quality)**
- Claude Sonnet 4.6: $3/$15 | 1M context | 59-72.7% SWE-bench
- Gemini 2.5 Pro: $1.25/$10 | 1M context | 84% SWE-bench
- GPT-4.1: $2/$8 | 1M context | 90% HumanEval
- DeepSeek V4: $0.30/$0.50 | 1M context | 81% SWE-bench ← cost king

**Tier 3 — Cost-effective workhorse**
- Gemini 2.5 Flash: $0.30/$2.50 | fastest cheap option
- DeepSeek V4 cached: $0.03/$0.50 ← near-free for stable-prefix workflows
- GPT-4.1 mini: $0.40/$1.60
- Gemini 2.5 Flash-Lite: $0.10/$0.40 ← absolute cheapest 1M context
- Claude Haiku 4.5: $1.00/$5.00 | 200K context

**Tier 4 — Open source / specialized**
- Llama 4 Maverick: $0.20/$0.60 | 10M context
- Llama 4 Scout: $0.11/$0.34 | 10M context
- Mistral Small 3.2: $0.06/$0.18 | 128K ← lowest cost simple tasks

### DeepSeek hidden discounts (critical for batch workflows)

**Cache hit discount — 90% off input**
- Stable system prompt + tool schema tokens billed at $0.03/1M (not $0.30)
- Any workflow with consistent prefixes benefits immediately
- Example: 1,800-token system prompt → effective input cost drops from $0.30 to $0.12/1M

**Off-peak discount — 50% off everything**
- Hours: ~11 PM – 7 AM Beijing time (UTC+8)
- Standard $0.30 → $0.15 | Cache hit $0.03 → $0.015 | Output $0.50 → $0.25
- Combined effect: 75-90% cost reduction for batch workflows

### Real-world cost examples

RAG pipeline (1,000 queries/day, 80% cache hit):
- Monthly with caching: $27.66
- Monthly without caching: $122.50
- Savings: 77%

Agent workload (10M tokens/day, DeepSeek optimized):
- DeepSeek V4: $80.40/month
- GPT-4o equivalent: ~$450/month
- Claude Opus 4.5 equivalent: ~$900/month
- DeepSeek is 82-91% cheaper

### Browser Use benchmark (600,000+ tasks tested)

| Model | Accuracy | Cost |
|---|---|---|
| BU 2.0 (Cloud) | 83.3% | $0.60/$3.50 per 1M |
| BU 1.0 (Cloud) | 74.7% | $0.20/$2.00 per 1M |
| Claude Opus 4.6 | 62.0% | $5/$25 per 1M |
| Gemini 3 Pro | 59.3% | ~$2/$12 per 1M |
| GPT-5 | 52.4% | Unknown |

Key finding: Purpose-built BU 2.0 beats every frontier LLM by 16-30 points
while being cheaper. Domain-specific beats general-purpose.

### API migration (zero friction)
All major Chinese models (DeepSeek, Qwen, Kimi, GLM) use OpenAI-compatible APIs.
Change only base_url and api_key. Zero code changes.

---

## 2. OPENROUTER LEADERBOARD (April 2026)

### Current top 10 by weekly token volume

| Rank | Model | Provider | Weekly Tokens | Note |
|---|---|---|---|---|
| #1 | MiMo-V2-Pro | Xiaomi | 4.65T | "Hunter Alpha" story |
| #2 | Claude Sonnet 4.6 | Anthropic | 2.18T | Enterprise coding standard |
| #3 | MiniMax M2.7 | MiniMax | 1.92T | Open-sourcing this week |
| #4 | DeepSeek V3.2 | DeepSeek | 1.22T | 90% GPT-5.4 quality at 1/50th cost |
| #5 | Qwen 3.6 Plus | Alibaba | 1.10T | Free preview — use now |
| #6 | Claude Opus 4.6 | Anthropic | 1.01T | Premium reasoning |
| #7 | GPT-5.4 | OpenAI | 0.98T | Dropped from dominance |
| #9 | Kimi K2 | Moonshot | 0.74T | Coding focus |

### Provider market share (weekly tokens)
- Xiaomi: 22.3% (came from nowhere in March 2026)
- Anthropic: 15.4% (down from ~25%)
- Chinese providers total: 51.2% — more than half of all traffic
- Open-weight models: 46% of all tokens
- OpenAI: 8.1% (dramatic fall)

### The MiMo-V2-Pro "Hunter Alpha" story
March 11: Anonymous model appears on OpenRouter as "Hunter Alpha." No branding. $0.30/M.
Within a week: processing 500B tokens/day. Everyone assumes DeepSeek.
March 18: Xiaomi reveals it's MiMo-V2-Pro — 1T total parameters, 42B active (MoE).
Result: first model to exceed 3T tokens/week. Proved: developers follow
performance-per-dollar, not logos.

### What to test now (free or cheap)
- Qwen 3.6 Plus: free preview, hits 1T tokens in first day, use before pricing activates
- MiMo-V2-Pro: $0.30/M, 78% SWE-bench (near Sonnet 4.6 at 67% of price)
- MiniMax M2.7: open-sourcing this week, strong for software engineering tasks

### What's declining
- OpenAI GPT-5.4: dropped to #7 (expensive, cheaper alternatives good enough)
- xAI Grok: lost 16.6% share in two weeks (Dec 2025)

### The Exacto endpoints (key architecture insight)
OpenRouter discovered: same model weights hosted by different providers produce
different tool call rates. Their response: "Exacto" routing pools that only send
agentic workloads to providers benchmarked for tool call accuracy.
Inference environment is NOT neutral — provider choice affects agent reliability.

### Tool call rate trend
<5% of API calls → >25% in 12 months. One in four API calls is now an agentic action.
Agent-specialized models (MiniMax M2): 80%+ tool call rates.
50% of all output tokens are now internal reasoning tokens (chain-of-thought).
This category didn't exist 13 months ago.

### Free tier survival kit (OpenRouter)

Stable model priority order:
1. google/gemma-3-27b-it:free (Google infra = stable)
2. meta-llama/llama-3.3-70b-instruct:free (less congestion)
3. mistral/codestral-2501:free (code-optimized)
4. qwen/qwen3-coder:free (powerful but volatile — use off-peak only)

Best reliability windows (UTC):
- 02:00-06:00: Americas night — best
- 06:00-10:00: Europe early — good
- 14:00-18:00: US/EU overlap — worst
- 22:00-02:00: Asia late — good

429 handling: wait 60-90 seconds before retry, switch models, stop at ~800/1000 daily calls.
PowerShell rotation functions documented in "The Free Tier Survival Kit" file.

---

## 3. STRATEGIC FRAMEWORKS

### The 70:2 Model Arbitrage Thesis

Core insight: achieve 80% of results at 2% of the cost, add 20% human creativity to close gap.
Real cost spread: GPT-4 ($30/1M) to Mistral Small ($0.20/1M) = 150x — not 70x.
Thesis is conservative.

Nvidia proof case (most important data point):
- Task: routing agent for employee support queries
- 70B model: 96% accuracy (baseline)
- 8B model without fine-tuning: 14% accuracy (useless)
- 8B model after 685 curated training examples: 96% accuracy
- 1B model after same fine-tuning: 94% accuracy at 98% cost reduction
- Latency improvement: 70x faster

The flywheel:
1. Deploy frontier model → collect production data (successes AND failures)
2. Curate ~500-1000 failure/correction pairs
3. Fine-tune 1B-8B model on those examples
4. Accuracy jumps from ~80% → 95%+, cost drops 98%
5. Each client adds to training data → marginal cost per new client → $0

Business model example (100M tokens/month):
- Client currently paying GPT-4 rate: $3,000/month
- Your service price: $500/month (83% savings to client)
- Your raw cost (budget models): $50/month
- Your gross margin: 80%
- Scale to 100 clients: $50K revenue / $10K cost / $40K monthly profit

### AI Solution Factory model

Shift: from selling one solution → selling infrastructure that produces infinite solutions.

Live proof — Coforge "AI Mod Squads" (launched April 7, 2026):
- 130+ pre-built agents (banking, insurance, airline, engineering)
- Subscription pricing: fixed monthly fee, not per project or per hour
- Results: 70% reduction in loan origination cycle time, 50% faster underwriting
- Expert-in-the-loop validates at critical decision points

The four-layer architecture:
1. State Layer (The Vault): SQLite ledger — immutable data
2. Sensor Layer (The Eyes): Steel — browser API for agents
3. Logic Layer (The Brain): Agent-TARS — chain-of-thought reasoning
4. Orchestration Layer (The Conductor): n8n — scheduling and routing

Persistent compute requirement (serverless fails for AI):
- Serverless: 60s timeouts, stateless, no background workers — breaks agent workflows
- Solution: Render/Fly.io-style "serverful" platforms
  - 100-minute request timeouts
  - First-class background workers (run 24/7)
  - Postgres + pgvector + Redis integrated
  - Zero-config private networking

Markets identified as immediately actionable:
1. SMB agent server (Docker + OpenRouter) — 33M small businesses in US alone
2. Business formation automation (1 country) — $200B global legal services market
3. Agent usage monitoring dashboard — you already need this for yourself

---

## 4. BROWSER AGENTS & UI AUTOMATION

### The three-layer stack (canonical breakdown)

**Steel — "The Body" (Infrastructure Layer)**
- Open-source, self-hostable browser API
- Handles proxy rotation, session memory, anti-bot evasion
- No intelligence: provides safe, unblockable environment for AI to operate in
- Tomato Score: HIGH (self-hostable, API-first, parallel sessions)

**Browser-Use — "The Translator" (Middleware Layer)**
- Open-source LLM-to-web connector
- Reads HTML, translates natural language → DOM interactions
- Fast and cheap for standard web tasks (HTML reading is computationally cheap)
- Gold standard for web-task benchmarks
- Tomato Score: HIGH (modular, any LLM, open-source)

**UI-TARS (ByteDance) — "The Eyes and Hands" (Vision Layer)**
- Multimodal vision model — sees pixels, not HTML
- Outputs X/Y coordinates for mouse clicks
- Works on anything: web, desktop apps, PDFs, games — not limited to browsers
- Use for the 10% of tasks where apps refuse to be scraped or require desktop control
- Setup: WSL2 preferred over Docker on Windows (cleaner Linux env for CLI/Playwright)
- Docker option: full isolation via Xvfb/VNC, but complex to configure

**Usage rule:**
- Browser-Use + Steel: 90% of web research and automation
- UI-TARS: 10% — when an app has no API and can't be scraped

### Individual tool verdicts

**Skyvern — Tomato Score: 9/10 (Critical Disruption)**
- Vision-language model navigates by semantic intent, not CSS selectors
- "Find the discount field" works regardless of div vs span
- Reduces operational maintenance to near zero
- Category: Browser / AI Agents | Status: Emerging, high-growth

**Firecrawl — Tomato Score: 9/10 (Efficiency King)**
- Turns any website into clean LLM-ready Markdown
- Eliminates HTML noise problem entirely
- Agents get pure logic, not messy DOM

**Stagehand — Tomato Score: 8/10 (Structural)**
- AI-first automation library built on Playwright
- Natural language element finding: await page.act('Click the login button')
- Handles Wait and Retry logic that makes Selenium brittle

**Selenium — LEGACY / DO NOT BUILD ON**
- Detectable by Cloudflare and modern anti-bot shields
- Brittle: one CSS class change = dead script
- Maintenance tax: 80% of time spent fixing selectors

### Browser fingerprint evasion (production tactic)
For Cloudflare Turnstile + Radix UI (hashed CSS classes):

Strategy A (preferred): Network API interception
- Use page.on('response') to catch internal JSON APIs before DOM renders
- React SPAs fetch data from /api/v1/usage or /graphql on load
- Intercept JSON directly — bypasses DOM entirely, infinitely more stable

Strategy B (fallback): Semantic locators
- Use Playwright getByRole(), getByText() — A11y tree stable even when CSS mutates
- Never use CSS class selectors against Radix UI

Stealth setup: playwright-extra + puppeteer-extra-plugin-stealth
- Masks navigator.webdriver, mocks WebGL, fakes plugins
- Critical arg: --disable-blink-features=AutomationControlled

---

## 5. AUTONOMOUS CODING AGENTS

### Devin vs Cursor benchmark (primary sourced)

| Metric | Devin | Cursor | Source |
|---|---|---|---|
| PR merge rate | 67% (68% in aligned window) | 74.4% | arXiv:2602.08915 (MSR '26) |
| SWE-bench (older) | ~44% (2024, stale) | N/A | Cognition self-reported |
| SWE-bench (Claude Sonnet 4.5) | — | 77.2% | Anthropic |

Full ranking from arXiv paper (May-Jul 2025 window):
OpenAI Codex 79.9% → Cursor 74.4% → Claude Code 72.6% → Devin 68.0% = GitHub Copilot 68.0%

Warning: Cursor's dashboard "acceptance rate" (~81%) measures inline autocomplete
suggestions — a different metric entirely. The 74.4% is PR-level.

### Devin failure mode analysis (idlen.io, March 2026)

Full task category performance:
- Documentation: 85%
- Test writing: 82%
- Bug fixes (clear): 78%
- Code migration: 70%
- Small features (well-defined): 65%
- Refactoring: 45%
- Bug fixes (vague): 35%
- Small features (ambiguous): 25% ← 53-point drop from clear bugs
- New architecture: 15%

Root causes of ambiguous feature failure:
1. No objective "done" signal — can't verify completion
2. Specification dependency — needs concrete specs (component, colors, spacing)
3. Compounding inference errors — wrong assumption in step 1 breaks all downstream
4. Plan instability — mid-session plan revisions invalidate prior code

### Devin cost-per-valid-PR ($2.25/ACU, 67% merge rate)
- Simple bug fix (1 ACU): $3.36 per merged PR
- Small feature (2 ACUs): $6.72 per merged PR
- Complex feature (4 ACUs): $13.43 per merged PR
- Note: 33% failed PRs still consume full ACUs — hidden multiplier

### Devin vs OpenHands on persistence
- Devin PR Resuming (April 1, 2026): takes over existing PRs, but sessions restart fresh
- OpenHands: full event stream serialized to disk, Daytona sandbox = truly stateful
- Verdict: OpenHands has deeper, more programmatic persistence

### Kimi K2 + OpenHands pairing
Evidence: OpenHands burned 4.33B tokens with Kimi K2, OpenClaw added 1.5B — production scale.
Moonshot explicitly lists OpenHands as one of top 6 recommended coding agents.

Kimi K2-0905 specs:
- 32B activated parameters / 1T total (MoE)
- 256K context window
- Tool call reliability higher than Qwen3 Coder
- OpenRouter price: $0.40/$2.00 per 1M in/out
- SWE-bench Verified: 78.0% (vs Sonnet 4.6 at 79.6%, Opus 4.6 at 80.8%)
- Cost vs Sonnet: 67% cheaper

Configuration (OpenHands settings):
  model: "moonshotai/kimi-k2-0905"
  base_url: "https://openrouter.ai/api/v1"

### Kiro IDE (deep research brief, April 2026)

Status: Generally available since Nov 17, 2025. GovCloud launched Feb 18, 2026.
FedRAMP High: in pursuit (not authorized), est. 2027.

Enterprise results (verified):
- Rackspace: 52 weeks of work in 3 weeks (31+ global projects), 90% efficiency increase
- AWS Drug Discovery: 95% of business logic written by Kiro, 80+ hours saved

Key features:
- Spec-driven development (Requirements → Design → Task List → Coding)
- Agent Hooks: automation scripts that fire on file system events (saves, creations)
  - Stored at repo level — entire team gets automation on git checkout
  - Hook examples: README auto-updater, test generation, commit hygiene
- Auto mode: routes to Claude Sonnet 4.6 for complex, fast models for simple
- GovCloud: customer-managed encryption, regional data storage (US)

Weaknesses:
- Rigid pipeline kills momentum during rapid iteration
- Files sometimes fail to appear in context until IDE restart
- No published PR acceptance rate (vs Cursor's 72% autocomplete acceptance)
- ROI positive only for features >2 days; questionable for sub-1-day tasks

---

## 6. AGNOSTIC AGENT FRAMEWORKS (ranked)

| Framework | Agnosticism | Notes |
|---|---|---|
| OpenHands | ✅ LiteLLM (100+ models) | Most provider-flexible |
| LiteLLM | ✅ Universal proxy | Powers many agnostic platforms |
| LangChain/LangGraph | ✅ Nearly every provider | Swap models with minimal code changes |
| AutoGen (Microsoft) | ✅ OpenAI, Azure, Gemini, Mistral, Ollama | Multi-agent, flexible backends |
| CrewAI | ✅ Built on LangChain model layer | OpenAI, Anthropic, Gemini, Ollama, Groq |
| Haystack (deepset) | ✅ Many providers + local | Strong RAG, production deployable |
| Agno (ex-Phidata) | ✅ 23+ providers | Clean provider-switching API |
| Semantic Kernel (Microsoft) | ✅ OpenAI, Azure, Gemini, Ollama | Enterprise backing |

Rule: if a tool uses LiteLLM, it's inherently agnostic.

---

## 7. KEY NUMBERS TO REMEMBER

- 150x: cost spread GPT-4 to Mistral Small (real number, not your 70x estimate)
- 98%: cost reduction achieved by Nvidia with fine-tuned 1B model (not 80%)
- 685: curated training examples needed to close the accuracy gap (not thousands)
- 83.3%: Browser Use 2.0 accuracy on web tasks (beats all frontier LLMs)
- 51.2%: Chinese model share of OpenRouter weekly tokens (April 2026)
- 25%: tool call rate on OpenRouter (up from <5% 12 months ago)
- 50%: of all output tokens are now internal reasoning tokens
- 4.33B: tokens burned by OpenHands with Kimi K2 (production signal)
- 28.6M → 2.2B: active agent count forecast (2025 → 2030, IDC)
- $200B: global business formation legal services market (automation target)
