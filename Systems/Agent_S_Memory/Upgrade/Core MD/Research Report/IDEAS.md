# Summary and Evaluation: Ideas Archive

*Generated: April 25, 2026*

---

## Overview

This archive contains **6 distinct product ideas** spanning AI tooling, contract analysis, and operational intelligence. All projects are at the research/specification phase—no code has been built or deployed. Each idea has been documented with varying depth, from market research briefs to fully specified build plans with starter code.

---

## Project Inventory

| # | Project | Category | Files | Status |
|---|---------|----------|-------|--------|
| 1 | Agent Forensics & Rollback | AI Safety / DevTool | 2 | Research complete, ready to pursue |
| 2 | Clause Mirror | Legal Tech / B2B SaaS | 2 | Concept defined, needs validation |
| 3 | Keyword Sleuth | Market Intelligence | 9 | Fully specified, 5-week build plan |
| 4 | Memory Spine | AI Infrastructure | 2 | Concept defined, needs focus |
| 5 | Shadow Price | Operational Analytics | 3 | Research complete, needs vertical focus |
| 6 | Shady Clause Detector | Legal Tech / Consumer | 7 | Build-ready, code written |

---

## Individual Project Summaries

### 1. Agent Forensics & Rollback
**Thesis:** A local-first SDK providing forensics capture and atomic rollback for AI agent failures.

**Target Users:** Solo developers running Claude Code, Cursor, browser-use agents unsupervised.

**Core Differentiator:** One-command rollback after agent destruction—no competitor offers state-level recovery.

**Key Documents:**
- Market research brief (260 lines) citing real incidents: Replit DB wipe (July 2025), Amazon Kiro 13-hour outage (Dec 2025), Claude Code `rm -rf` incidents
- EU AI Act Article 12 compliance positioning (6-month log retention requirement, Aug 2026 deadline)

**Verdict:** Pursue with scope constraint. Real gap exists; competitive moat is thin (Langfuse could add rollback). Best wedge: freelancer accountability via tamper-evident session reports.

---

### 2. Clause Mirror
**Thesis:** An adversarial reading layer for contracts—exposing hidden downside, not summarizing text.

**Target Users:** Freelancers, SMB operators, procurement-adjacent non-lawyers, job seekers.

**Core Differentiator:** Reads "from your side, not theirs"—hostile forensic framing vs. neutral summarization.

**Key Documents:**
- Core thesis and problem definition (176 lines)
- Research brief on market validation and production hypotheses

**Validation Questions Outstanding:**
- Which document categories create strongest urgency/frequency?
- Is willingness to pay driven by financial risk, time savings, or peace of mind?
- What output format earns trust: scorecards, clause cards, escalation recommendations?

**Verdict:** Strong narrative, unproven defensible edge. Risk: collapses into "ChatGPT but for contracts." Needs sharper mechanism and entry point before building.

---

### 3. Keyword Sleuth
**Thesis:** A cross-platform search engine for reviews and comments with sentiment + trend analysis.

**Target Users:** Small business owners, market researchers, PR/marketing agencies.

**Core Differentiator:** No existing tool combines cross-platform keyword search with sentiment analysis and trend tracking at consumer pricing.

**Key Documents:**
- Summary report (238 lines)
- No-scraping data strategy using Hugging Face datasets (`yelp_polarity`, `amazon_polarity`)
- Common Crawl + Apache Spark scale path (1.97 billion pages, 75.53 TiB)
- Market evaluation and 5-phase build plan

**Technical Decisions:**
- v1: Zero-scraping using Hugging Face datasets (cost: $0)
- v2: Common Crawl + Spark for production scale
- Sentiment: TextBlob → VADER → fine-tuned BERT progression

**Verdict:** Genuine product gap, clear zero-cost v1 path, credible scale architecture. Next action: write code, not more documentation.

---

### 4. Memory Spine
**Thesis:** A persistent context layer maintaining continuity across projects, sessions, and AI systems.

**Target Users:** Solo researchers, founder-operators, human+AI workflow builders, creative professionals.

**Core Differentiator:** Decides what must stay "live" vs. compressed/archived—selective orientation, not storage.

**Key Documents:**
- Core thesis and validation questions (235 lines)
- Research brief on production hypotheses

**Validation Questions Outstanding:**
- Which users feel context fragmentation as budget line vs. abstract annoyance?
- Do users want one spine across all tools, or scoped per domain?
- How much trust is lost when memory systems infer too much?
- Willingness to pay for continuity infrastructure vs. manual composition?

**Verdict:** Strong narrative, foundational gap if real. Biggest risk: category blur into "better notes" or "better AI memory." Needs sharper structural distinction.

---

### 5. Shadow Price
**Thesis:** Analytics layer quantifying hidden economic cost in workflows—"counterfactual cost" (what should have happened vs. what did).

**Target Users:** Operations leaders, CFOs, process/transformation teams, AI/automation leads.

**Core Differentiator:** Converts operational events into economic signals, not dashboards.

**Key Documents:**
- Core thesis and production hypotheses (362 lines)
- Research brief on market validation
- Domain-specific vertical analysis

**Production Hypotheses:**
- Path A: Analytics layer overlay on existing systems
- Path B: Embedded workflow instrumentation (SDK)
- Path C: Domain-specific vertical (e.g., software development workflows)

**Verdict:** Addresses real structural blind spot (unmeasured economic loss). Strongest risk: model produces "precise but ungrounded" outputs, eroding trust. Needs vertical focus before building.

---

### 6. Shady Clause Detector
**Thesis:** Contract analysis tool reading like a hostile lawyer—"how could this be used against me?"

**Target Users:** Freelancers, renters, employees, small business owners signing agreements in real-time.

**Core Differentiator:** Three-layer architecture: API engine + web interface + mobile guardian (OCR camera → instant Shady Score).

**Key Documents:**
- Summary report (244 lines)
- Full tech stack specification
- Build plan with ready-to-run code
- Commercial launch plan
- Open-source tools research

**Technical Stack:** FastAPI, pdfplumber, python-docx, Tesseract OCR, LiteLLM, Streamlit (prototype) → React (production), PWA + Capacitor (mobile)

**Verdict:** Most complete idea in the archive. Build plan fully specified, starter code documented, 5-week MVP timeline. Risk: legal/liability boundaries, unauthorized practice of law concerns. Next action: run the three setup commands and test adversarial prompt on real contracts.

---

## Cross-Cutting Analysis

### Common Patterns

| Pattern | Observed In | Implication |
|---------|-------------|-------------|
| Adversarial framing | Clause Mirror, Shady Clause Detector | Sharp positioning, but risks overpromising on AI legal accuracy |
| Local-first / privacy-first | Agent Forensics, Shady Clause (OCR client-side) | Response to growing distrust of cloud AI, GDPR concerns |
| No/low-scraping v1 | Keyword Sleuth (Hugging Face), Agent Forensics (SQLite) | Strategic risk mitigation for solo operators with limited legal budget |
| EU AI Act tailwind | Agent Forensics (Article 12) | Time-boxed regulatory opportunity (Aug 2026 deadline) |
| Open-source stack preference | All 6 projects | Consistent constraint: $0–$30/month infrastructure, no VC funding |

### Category Overlap

**Clause Mirror** and **Shady Clause Detector** occupy similar territory (contract analysis). Key differences:
- Clause Mirror: broader adversarial reading layer, less defined product shape
- Shady Clause Detector: specific "Legal Adversary" persona, mobile-first use case, build-ready

**Recommendation:** Consolidate or differentiate sharply. Shady Clause Detector is further along and has clearer distribution (camera → OCR → score).

### Technical Debt Patterns

All projects share a preference for:
- FastAPI backend (lightweight, async)
- SQLite for local storage (zero config)
- Streamlit for prototypes (no frontend expertise needed)
- Fly.io / Vercel for hosting (cheap, developer-friendly)
- LiteLLM for LLM routing (provider flexibility)

This creates optionality but also homogeneity—none leverage unique technical moats.

---

## Strategic Evaluation

### Highest Readiness to Build

| Rank | Project | Rationale |
|------|---------|-----------|
| 1 | Shady Clause Detector | Code written, build plan complete, 5-week MVP |
| 2 | Keyword Sleuth | Zero-cost v1 path, clear data strategy, 5-week timeline |
| 3 | Agent Forensics & Rollback | Real gap documented, EU AI Act deadline, but competitive moat thin |

### Highest Risk of Market Collapse

| Rank | Project | Risk |
|------|---------|------|
| 1 | Clause Mirror | Collapses into "ChatGPT but for contracts" without sharp mechanism |
| 2 | Memory Spine | Category blur—indistinguishable from "better notes" or "better AI memory" |
| 3 | Shadow Price | Model produces untrustworthy outputs; "interesting but unusable" |

### Strongest Hidden Opportunity

- **Agent Forensics:** Freelancer accountability angle (tamper-evident session reports) is sharper wedge than enterprise observability.
- **Shadow Price:** AI inefficiency niche (prompt loops, validation overhead) is high-growth, underserved.
- **Keyword Sleuth:** Common Crawl + Spark architecture could generalize beyond reviews to other unstructured data verticals.

---

## Recommendations

### Immediate Actions (Next 30 Days)

1. **Shady Clause Detector:** Run the three setup commands, test adversarial prompt on 5 real contracts, validate red/yellow flag accuracy.

2. **Keyword Sleuth:** Load `yelp_polarity` from Hugging Face, build FastAPI endpoint, validate sentiment model on subset.

3. **Agent Forensics:** Waitlist or pre-sales conversation to validate $29/month willingness to pay vs. Langfuse + manual git snapshots.

### Deferred / Kill Decisions

- **Clause Mirror:** Merge concept into Shady Clause Detector or park until distinct mechanism emerges. Do not build separately.

- **Memory Spine:** Park pending clearer structural distinction from note systems and assistant memory. Needs validation question answers first.

- **Shadow Price:** Select one vertical (recommend: AI inefficiency or software development workflows), build narrow MVP, validate economic translation credibility before generalizing.

### Portfolio Balance

Current spread: 2 legal tech, 2 AI infrastructure/safety, 1 market intelligence, 1 operational analytics.

Overlap risk: Clause Mirror / Shady Clause Detector. Consider:
- Option A: Kill Clause Mirror, double down on Shady Clause Detector's mobile-first immediacy
- Option B: Merge—Clause Mirror becomes enterprise/SMB layer, Shady Clause becomes consumer/freelancer layer

---

## Document Statistics

| Metric | Value |
|--------|-------|
| Total ideas | 6 |
| Total files | 27 |
| Research-only (no build plan) | 2 (Clause Mirror, Memory Spine) |
| Build-ready (code written) | 2 (Keyword Sleuth, Shady Clause Detector) |
| Estimated total words | ~15,000 |
| Date range | April 23–25, 2026 |

---

## Conclusion

This archive represents **5–8 weeks of focused research** yielding 2 build-ready products, 2 strong concepts needing validation, and 2 at risk of category collapse. The pattern suggests a bias toward specification over execution—consistent next action across all projects is "stop researching, start building."

Strongest immediate bet: **Shady Clause Detector** (sharpest concept, most complete documentation, code ready to run).
Strongest strategic bet: **Agent Forensics & Rollback** (regulatory tailwind, real pain documented, but requires speed before Langfuse/AgentOps fill gap).

---

*End of Summary and Evaluation*
