---
modified: 2026-04-23T02:52:27+03:00
---
# 8 Candidate Ideas for Serious Evaluation — April 2026

---

## Idea 1: **Attestation Layer**

**Core Thesis**
A lightweight credential infrastructure that lets individuals prove *what they've actually built or shipped* — not what degrees they hold — creating a verifiable, portable professional record that employers trust more than résumés.

**Problem**
The job market is now flooded with LLM-assisted portfolios, AI-generated code samples, and fabricated project histories. Recruiters cannot distinguish genuine builders from synthetic candidates. Credentials (degrees, certs) predate this problem and don't solve it. GitHub activity is gameable. LinkedIn is noise.

**Solution**
A timestamped, multi-signal attestation system: pull commit-level data, deployment logs, real user metrics, and peer co-signatures from verifiable on-chain or signed-hash records. Candidates get a portable "build record" that's structurally hard to fake because it requires consistent, corroborating signals over time — not a single artifact.

**Why Now**
The 2025–2026 hiring collapse in tech created a massive signal crisis. Hiring managers are getting hundreds of indistinguishable applications. Companies are already piloting "take-home builds watched by proctoring software" — which is both invasive and weak. The structural demand for a better signal exists right now.

**Strategic Edge**
The value compounds: the longer a builder maintains a verified record, the harder it is for a newcomer to fake equivalent standing. This creates a legitimate moat around authentic builders and a high-trust hiring channel that self-cleans over time.

**Zero-Cost Lever**
GitHub OAuth + Vercel/Netlify deployment webhooks + a hashed timestamp log stored on Arweave or Ceramic. Peer co-signatures via email-verified cryptographic sign. All open-source. No blockchain fees at meaningful scale for the early product.

---

## Idea 2: **Dark Pattern Auditor-as-a-Service**

**Core Thesis**
A compliance SaaS that automatically detects, classifies, and reports dark patterns in digital interfaces — sold to legal and compliance teams at enterprises facing EU and US regulatory exposure right now.

**Problem**
The EU Digital Services Act (DSA), the FTC's 2024 dark pattern enforcement actions, and California's forthcoming regulations have created a real legal liability for UI manipulation — but most companies have no systematic way to audit their own products. They rely on manual QA or outside counsel, both of which are slow and expensive.

**Solution**
A crawler + vision model pipeline that ingests a URL, maps the user flow, classifies detected patterns against a regulatory taxonomy (confirm-shaming, forced continuity, roach motel, etc.), produces an audit report with severity levels and regulatory citation, and flags changes between versions. Sold as a compliance audit subscription, not a UX tool.

**Why Now**
DSA enforcement actions started landing in 2025. The FTC fined multiple companies. Legal teams are now *actively looking* for this and have budget. The regulatory surface expanded faster than the tooling.

**Strategic Edge**
Framing this as legal compliance — not UX improvement — changes the buyer entirely. You're not competing with UX tools; you're competing with outside counsel billing $600/hour. The value proposition is defensible on cost alone.

**Zero-Cost Lever**
Playwright for crawling, open-source vision model (LLaVA or Moondream) for UI classification, a curated taxonomy built from public regulatory guidance documents. Wrap in a Next.js front-end on Vercel free tier. Report generation via a Markdown-to-PDF pipeline.

---

## Idea 3: **Fractional Inference Broker**

**Core Thesis**
A routing layer that lets small companies and indie developers dynamically arbitrage inference costs across open-source and commercial model providers in real time — cutting AI operating costs by 40–70% without touching application code.

**Problem**
In 2026, most companies are running LLM-backed products and spending $5,000–$50,000/month on inference. OpenAI, Anthropic, and Google have different pricing, latency, and capability profiles — and these shift constantly. No developer has time to continuously re-route by task type. They pick one provider and overpay.

**Solution**
A drop-in proxy endpoint that accepts standard OpenAI-spec requests, classifies the task complexity in <50ms using a tiny local classifier, and routes to the cheapest adequate model for that task type — GPT-4o for complex reasoning, Mistral for summarization, Gemini Flash for extraction, a local Ollama instance for scratchpad tasks. Billing is consolidated and the savings are shown live.

**Why Now**
The open-source model ecosystem hit parity on many tasks in late 2025. Llama 4, Mistral Large, and Gemini Flash are all genuinely competitive for large subsets of tasks. The arbitrage window is real and measurable today in a way it wasn't in 2023.

**Strategic Edge**
Switching cost is near-zero for the customer (one API endpoint change), but the value is immediate and quantifiable. Cost savings show up on the first bill. This is a budget-line-item save, not a vision sale.

**Zero-Cost Lever**
LiteLLM for the routing layer (open-source, production-grade), a tiny BERT classifier fine-tuned on task types, Cloudflare Workers for the proxy edge, Supabase free tier for usage tracking. Full stack deployable under $0/month at early user volumes.

---

## Idea 4: **Local-First Enterprise Memory**

**Core Thesis**
A self-hosted knowledge graph that gives enterprise teams a queryable, persistent memory layer across all internal tools — Slack, Notion, Jira, email, docs — without any data leaving the company's infrastructure.

**Problem**
Enterprises want LLM-powered knowledge retrieval but cannot send their internal communications and documents to external APIs. The "private AI" solutions that exist are either cloud-hosted (contradicting the requirement), require a $500K+ on-prem enterprise deal, or are so complex to deploy they stall in procurement. The mid-market (50–500 employees) has no viable option.

**Solution**
A Docker-deployable appliance: installs in 20 minutes, connects to internal tools via OAuth, builds a vector graph locally using an embedded model (Nomic or similar), and exposes a query interface. No data leaves. No cloud dependency after install. Priced on seat count, invoiced annually, sold to IT managers.

**Why Now**
On-device and edge inference became genuinely viable in 2025–2026. You can run a useful embedding model on a standard 16GB RAM server. The enterprise data sovereignty conversation shifted from "nice to have" to "required by legal" in the EU and increasingly in regulated US industries.

**Strategic Edge**
The "no data leaves" constraint is not a limitation — it's the product. It bypasses the procurement objection that kills every cloud AI tool in enterprise. Sales cycle collapses from 6 months to 3 weeks because legal doesn't need to approve a data processing agreement.

**Zero-Cost Lever**
Ollama + Nomic Embed for local embedding, LanceDB or Chroma for vector storage, LlamaIndex for graph construction, FastAPI backend, Next.js UI. Entire stack is open-source. Cost to build: compute time and integration work.

---

## Idea 5: **Synthetic Cohort Engine**

**Core Thesis**
A product analytics tool that generates statistically valid synthetic user cohorts from aggregate behavioral data, letting product teams run segmentation analysis and experiment design without accessing any real user PII.

**Problem**
GDPR and CCPA enforcement tightened significantly in 2025. Product teams at mid-size companies have had analytics access restricted by their own legal teams — because querying raw user data creates compliance exposure. The result: PMs are making decisions with less data than they had in 2019. Real experimentation is stalling.

**Solution**
Ingest anonymized event streams (no raw IDs, no PII), fit a generative model to the behavioral distributions, produce synthetic cohorts that preserve the statistical properties without containing real users, and expose a standard analytics interface on top. Legal can approve synthetic data access where they'd block raw access.

**Why Now**
Differential privacy and synthetic data generation research matured enough in 2024–2025 to be production-usable without a PhD team. The regulatory pressure that creates the demand is also now acute — not theoretical.

**Strategic Edge**
This isn't a privacy tool sold to privacy officers. It's a productivity tool sold to product managers and growth teams who are actively frustrated right now. That's a shorter sales cycle and a clearer ROI narrative.

**Zero-Cost Lever**
SDV (Synthetic Data Vault) library for generation, PostHog open-source for the analytics layer, DuckDB for in-memory analytics, Streamlit for the initial UI. Total infrastructure cost near zero at early scale.

---

## Idea 6: **Contract Asymmetry Scanner**

**Core Thesis**
A tool that parses standard commercial contracts and surfaces the specific clauses where one party has structurally more risk, fewer exits, or hidden liability — designed for founders and small business operators who can't afford legal review on every agreement.

**Problem**
Founders and operators sign vendor contracts, SaaS agreements, partnership terms, and employment agreements under time pressure without proper review. They systematically accept unfavorable terms — auto-renewal traps, unilateral pricing change clauses, IP assignment overreach, uncapped liability — because reviewing each contract costs $400–$1,200 in legal fees and takes days. The information asymmetry is extreme.

**Solution**
Upload a contract PDF, get back: a plain-English summary of the top 5 risk asymmetries, specific clause references, severity ratings, and suggested negotiation counters. Not legal advice — clause-level structural analysis. Priced at $20–$50 per scan or $99/month subscription for founders and operators.

**Why Now**
Document-parsing models in 2025–2026 can handle legal clause structure with high fidelity. More importantly, the volume of SaaS vendor contracts that startups sign has exploded — the average 20-person startup now manages 40+ vendor agreements. The problem density is higher than ever.

**Strategic Edge**
The competitive set is either full legal review ($$$) or AI chat with a contract pasted in (no structured output, no persistence, no trust). A purpose-built structured analysis tool with consistent output format and audit trail is a different category.

**Zero-Cost Lever**
Marker or PyMuPDF for PDF parsing, a fine-tuned or prompted open-source LLM for clause classification, a curated risk taxonomy built from public legal databases. Hosted on Railway or Fly.io free tier. Under $50/month to run at early user volumes.

---

## Idea 7: **Asynchronous Expert Network**

**Core Thesis**
A marketplace where verified domain experts answer high-stakes questions in structured written form — not 30-minute Zoom calls — creating a searchable, reusable knowledge asset the buyer owns permanently.

**Problem**
Expert networks (GLG, Tegus, AlphaSights) sell expensive one-hour phone calls that produce no durable artifact. The buyer takes notes, knowledge dissipates, and the next team member has to buy another call. Meanwhile, serious practitioners have deep knowledge but hate calendar-driven consulting. Both sides are underserved by the call format.

**Solution**
Experts answer structured question sets asynchronously within 48 hours. Answers are formatted, searchable, and owned by the buyer. Buyers can follow up in threads. Answers can be re-licensed to future buyers at a discount, giving experts residual income. The platform builds a proprietary knowledge corpus over time.

**Why Now**
Remote async work norms normalized during 2020–2024 and are now entrenched. More critically, the LLM wave created a new class of questions that can't be answered by models — questions requiring current, specific, situated practitioner knowledge. Buyers are hitting this wall repeatedly and looking for an alternative.

**Strategic Edge**
Every answer produced increases the value of the corpus. The marketplace has compounding supply-side value unlike call-based expert networks where every engagement is a one-time event. The business model has a library dimension the incumbents don't.

**Zero-Cost Lever**
Stripe for payments, Supabase for auth and data, a Next.js front-end. Expert verification via LinkedIn OAuth + credential cross-check. No proprietary infrastructure needed. Initial supply can be seeded by inviting practitioners with existing audiences who want monetization without scheduling overhead.

---

## Idea 8: **Regulatory Delta Feed**

**Core Thesis**
A structured, machine-readable feed of regulatory changes — parsed from primary sources, classified by industry and jurisdiction, and delivered as actionable deltas — sold to compliance teams who currently track this manually.

**Problem**
Compliance officers at financial, healthcare, and legal-adjacent companies track regulatory changes by subscribing to PDF newsletters, manually reading Federal Register entries, and relying on expensive regulatory intelligence vendors ($20K–$100K/year contracts). The manual reading is slow, the expensive vendors are overbuilt for most buyers, and nothing in between produces structured, filterable, actionable output.

**Solution**
A crawler that ingests primary regulatory sources (SEC, FDA, FTC, CFPB, EBA, FCA, etc.) daily, parses new guidance and rule changes, classifies them by industry/topic/jurisdiction, diffs them against prior versions, and publishes a structured feed — JSON API + email digest + Slack integration. Priced at $500–$2,000/month depending on jurisdiction coverage.

**Why Now**
The regulatory output volume from US and EU agencies accelerated sharply in 2024–2026 as AI governance frameworks, data protection enforcement, and financial sector re-regulation all converged. The volume problem is acute. Manual tracking is visibly failing.

**Strategic Edge**
Regulatory intelligence is a B2B workflow product with high switching costs once integrated into a compliance team's process. The data moat builds as the diff history grows — historical regulatory context becomes a proprietary asset no new entrant can replicate quickly.

**Zero-Cost Lever**
Scrapy or Playwright for crawling public regulatory sources (all primary sources are publicly accessible), spaCy + a classification model for parsing, PostgreSQL for diff storage, FastAPI for the API layer, Resend for email digests. Early version buildable for under $100/month in infrastructure.

---

---

# Final Section

## Top 3 by Raw Strategic Potential

**#1 — Fractional Inference Broker (Idea 3)**
Sits directly in the cost center of every company running LLM products, delivers quantifiable savings on the first bill, and requires one API endpoint change to adopt — the combination of zero switching cost and immediate ROI is rare.
*Main risk: the major providers could build routing natively into their own pricing tiers, commoditizing the arbitrage layer.*

**#2 — Local-First Enterprise Memory (Idea 4)**
Solves a procurement-blocking problem (data sovereignty) that is structural and regulatory, not just a preference — which means the competitive moat is the compliance argument, not just the product quality.
*Main risk: a well-funded competitor (Glean, Notion, Microsoft Copilot) ships a credible on-prem option and absorbs the market before the product reaches scale.*

**#3 — Regulatory Delta Feed (Idea 8)**
Compliance is a non-discretionary spend category, the data is publicly accessible, and the value compounds as historical diff coverage grows — making this a durable asset business disguised as a feed product.
*Main risk: the target buyers are conservative and slow to adopt new vendors, making sales cycles long and CAC high relative to early revenue.*

---

## Single Most Build-Worthy Candidate Right Now

**Fractional Inference Broker** — it can be prototyped in a weekend using LiteLLM, the value is immediately measurable in dollars, and it addresses a pain point that every technical founder and engineering team is actively complaining about today.