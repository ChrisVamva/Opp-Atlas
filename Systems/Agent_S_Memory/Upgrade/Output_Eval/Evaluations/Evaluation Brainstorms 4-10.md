---
modified: 2026-04-23T03:46:01+03:00
---
## Evaluation Report — 7 Ideas

---

## SCORING TABLE

| # | Idea | Ambition | Zero-Cost | Market Gap | Clarity | Actionability | Cross-Industry | Avg | Verdict |
|---|------|----------|-----------|------------|---------|---------------|----------------|-----|---------|
| 1 | Sightline | 4 | **3** | 4 | 4 | 4 | 3 | 3.67 | **REJECTED** |
| 2 | Fractional Inference Broker | 4 | 4 | 4 | 5 | 5 | 4 | 4.33 | **SURVIVES** |
| 3 | Agent Session Replay | 4 | 4 | 4 | 5 | 5 | 4 | 4.33 | **SURVIVES** |
| 4 | EU AI Act Compliance OS | 4 | **3** | 4 | **3** | **3** | 4 | 3.50 | **REJECTED** |
| 5 | Agent Failure Observatory | 3 | 4 | **3** | **3** | **3** | 3 | 3.17 | **REJECTED** |
| 6 | Agent Audit Trail (AAT) | 5 | 4 | 5 | 5 | 5 | 5 | 4.83 | **SURVIVES** |
| 7 | Ephemeral SaaS Orchestrator | 5 | **3** | 4 | **3** | **2** | 5 | 3.67 | **REJECTED** |

---

## REJECTED IDEAS — EXACT FAILURE MODES

**Idea 1 — Sightline**
Failure mode: **not truly zero-cost / unclear mechanism**
Chrome's built-in AI APIs (Gemini Nano) are not production-stable across environments. WebGPU inference "before paint" is aspirational — classifying every media element pre-render adds blocking latency that breaks most sites. C2PA adoption remains thin; the tool degrades to guesswork without it. Zero-cost lever collapses under real traffic. The audience (people who hate AI slop) is real, but the technical claim is oversold.

**Idea 4 — EU AI Act Compliance OS**
Failure mode: **unclear mechanism + not actionable + not truly zero-cost**
"Plug-and-play OS that continuously scans AI systems" is a sentence, not a product. OpenFisca is a tax/benefit rule engine — citing it as the base for AI Act compliance reveals superficial research. "Auto-generate documentation" for a law with 85 articles and jurisdiction-specific guidance is a feature claim with no demonstrated path. The actual compliance mapping requires legal expertise that cannot be open-sourced away. Three hard threshold failures.

**Idea 5 — Agent Failure Observatory**
Failure mode: **weak gap + unclear mechanism + not actionable**
This is a research dataset, not a product. No coherent monetization, no demonstrated user motivation to submit failures, no mechanism to ensure submission quality. "Becomes the ground truth dataset" is a passive hope, not a strategy. Who pays? Who governs the taxonomy? Why submit? Zero commercial pull is established.

**Idea 7 — Ephemeral SaaS Orchestrator**
Failure mode: **unclear mechanism + not actionable + not truly zero-cost**
The ambition is real. The product is not. "Auto-generate, deploy, and tear down single-use internal tools" leaves entirely unresolved: database credential management, enterprise SSO, data governance, generation reliability, and failure states when the tool misbehaves mid-task. Vercel free tier is not enterprise infrastructure. Llama-3/DeepSeek generating reliable production-grade internal tooling for real enterprise data is a research problem, not a launch condition. The gap between the vision and a shippable V1 is 18+ months.

---

## TOP 3 SURVIVORS — RANKED

---

### **#1 — Agent Audit Trail (AAT) Compliance Layer**

**Why it survived:**
Every scored dimension is at ceiling or near it. The August 2026 EU AI Act enforcement cliff is a hard external forcing function — not a trend, not a maybe. The IETF draft standard published March 2026 creates a narrow window where the dominant implementation has not yet been locked in. The mechanism is precisely specified: hash-chained append-only log, defined fields, defined exports, defined compliance targets. This is not a vision pitch. It is an engineering spec with a deadline.

**Why stronger than the others:**
The others rely on user adoption curves or internal pain recognition. AAT relies on regulatory compulsion. Demand is mandatory, not optional. The compliance substrate framing also means every high-risk agent deployment becomes a distribution channel — the tool goes where the agents go.

**Main risk:**
A well-funded incumbent (IBM, ServiceNow, Datadog) or a YC batch company ships a compliant implementation first and captures enterprise procurement before the open-source version gains trust. The window is narrow for exactly the same reason it's compelling.

**Confidence level: High**

---

### **#2 — Fractional Inference Broker**

**Why it survived:**
Clarity and actionability are both at maximum. The value is immediately quantifiable — cost savings appear on the first bill. LiteLLM handles the routing scaffolding; the novel layer is the sub-50ms task classifier that makes routing decisions before the request hits any model. Switching cost for the customer is one API endpoint change. The business case is arithmetic, not persuasion.

**Why it's #2 and not #1:**
LiteLLM already implements significant routing logic. The task classifier is the moat, but it's a thin one — any serious team can replicate it in weeks. Pricing arbitrage also compresses over time as providers converge. The market gap is real today; it shrinks as model pricing standardizes.

**Main risk:**
OpenAI, Anthropic, or Google builds dynamic pricing tiers that eliminate the arbitrage natively. Or LiteLLM ships a better native classifier and renders the differentiation moot.

**Confidence level: Medium**

---

### **#3 — Agent Session Replay**

**Why it survived:**
The pain is acute and real. When a production agent behaves differently between runs, the debugging process is currently manual forensics. "FullStory for agents" is a precise analogy — it communicates the product in four words. The technical stack is genuinely zero-cost to deploy. Enterprise compliance angle adds a second buyer persona beyond individual developers.

**Why it's #3 and not #2:**
Langfuse, Langsmith, and Weights & Biases all have session capture capabilities. The "step-through diff against prior sessions" is the genuine differentiator — but it's a feature, not a moat. The market gap is narrower than it appears at first read.

**Main risk:**
Langfuse ships a diff feature. The window closes. This idea is most vulnerable to being absorbed by an adjacent tool with a head start.

**Confidence level: Medium**

---

## FINAL WINNER: Agent Audit Trail (AAT)

**Why this is the best candidate now:**
The enforcement cliff is not a market signal. It is a legal deadline with criminal and financial penalties. Every enterprise deploying agentic AI in EU jurisdictions between now and August 2026 has a compliance gap that cannot be closed with logging best practices. AAT closes it with a specific architecture aligned to a specific emerging standard. The demand is non-negotiable and the standard is new enough that the dominant implementation has not been written yet.

**What makes it stronger than #2:**
Fractional Inference Broker saves money. AAT prevents liability. In enterprise procurement, liability prevention outcompetes cost savings. AAT also has a clearer path to lock-in: once the audit trail is the system of record for regulatory evidence, replacing it requires re-auditing historical decisions. Switching cost is high by design.

**Primary strength: Timing + Market Gap**
Both are structural, not contingent on product quality or marketing. The enforcement cliff is fixed. The standard gap is real. A functional MVP shipped before August 2026 captures a market that must exist.

---

## FINAL CHALLENGE — WHICH TOP 3 IDEA MIGHT BE FALSE NOVELTY?

**Candidate: Agent Session Replay (#3)**

The "FullStory for agents" framing is compelling but may be naming a familiar pattern rather than describing a new mechanism. Langfuse already captures traces, token counts, tool inputs/outputs, latency, and model responses. Langsmith does session-level evaluation. The actual novel claim — step-through diff against prior sessions — is never demonstrated to be technically difficult to build or commercially validated as a top-priority pain. Most developers debugging agent failures today want better logs, not a diff viewer. The product may be a UI feature shipped on top of an existing observability tool, not a standalone company. The gap is real but may be a feature gap, not a market gap.

---

## PROMPT DIAGNOSIS

The brainstorm output is **mixed quality** — two strong ideas, three weak ones, two rejected on multiple criteria. The failure is not the prompt structure. The failure is **inconsistent source discipline in the brainstormer**.

| Dimension                    | Assessment                                                                                                                                                                                          |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Main failure mode            | Zero-cost lever is asserted, not validated                                                                                                                                                          |
| Evidence                     | Ideas 1, 4, 7 all claim zero-cost mechanisms that collapse under technical scrutiny (C2PA adoption, OpenFisca as AI compliance tool, Vercel free tier as enterprise infra)                          |
| Weakness produced            | Survives surface-level review but fails on mechanism inspection                                                                                                                                     |
| Minimum prompt change needed | Add one required field: **"Zero-cost lever stress test: name the exact failure condition of this lever at 1,000 active users"**                                                                     |
| Stronger replacement wording | Replace *"Zero-Cost Lever: [tool] for [function]"* with *"Zero-Cost Lever: [tool] handles [specific function]. It fails at [threshold] because [reason]. At that point the cost becomes [amount]."* |