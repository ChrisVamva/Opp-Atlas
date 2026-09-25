---
modified: 2026-04-25T20:56:24+03:00
---
# Browse Web UI Prompt Templates

*For research, discovery, and synthesis workflows*

  

---

  

## 🔍 Discovery & Triage

  

### 1. Broad Topic Discovery

```

Goal: Identify the most relevant, high-signal sources on [TOPIC] in 2026.

  

Task:

- Scan the top 10-15 results for [TOPIC] on Google/Bing/DuckDuckGo.

- Extract the title, URL, snippet, and date for each result.

- Classify each result by source type:

  - Official documentation

  - Vendor blog / announcement

  - Community forum / Q&A

  - Research paper / arXiv

  - News / press release

  - Tutorial / guide

- Identify 3-5 sources that are most likely to contain primary or high-signal information.

- Summarize the key themes and gaps across the results.

  

Output format:

```markdown

## Discovery Summary: [TOPIC]

  

### Top Sources

| # | Title | URL | Source Type | Date | Key Theme |

|---|-------|-----|-------------|------|-----------|

  

### Key Themes

- [Theme 1]

- [Theme 2]

- [Theme 3]

  

### Gaps & Next Steps

- [Gap 1] → [Next step]

- [Gap 2] → [Next step]

```

```

  

---

  

### 2. Competitor / Landscape Scan

```

Goal: Map the competitive landscape for [PRODUCT/CATEGORY] in 2026.

  

Task:

- Search for "[PRODUCT/CATEGORY] alternatives", "[PRODUCT/CATEGORY] vs", "best [PRODUCT/CATEGORY] 2026".

- Extract the top 10-15 results.

- For each result, extract:

  - Product name

  - URL

  - Tagline / positioning

  - Key features (bullet list)

  - Pricing model (if available)

  - Strengths and weaknesses (from snippet or page)

- Identify the top 3-5 competitors and 2-3 adjacent categories.

- Summarize the differentiation landscape.

  

Output format:

```markdown

## Competitive Landscape: [PRODUCT/CATEGORY]

  

### Top Competitors

| # | Product | URL | Tagline | Key Features | Pricing | Strengths | Weaknesses |

|---|---------|-----|---------|--------------|---------|-----------|------------|

  

### Differentiation Map

- [Competitor A] → [Positioning]

- [Competitor B] → [Positioning]

- [Adjacent Category] → [Why it matters]

  

### Opportunities

- [Opportunity 1]

- [Opportunity 2]

```

```

  

---

  

## 📊 Extraction & Analysis

  

### 3. Deep Page Extraction (Research Papers, Docs, Blogs)

```

Goal: Extract all key facts, claims, numbers, and quotes from a single page.

  

Task:

- Read the page thoroughly.

- Extract:

  - Title, URL, date, author

  - Core thesis or claim

  - Key facts (bullet list)

  - Numbers and metrics (with units)

  - Quotes (verbatim, with context)

  - Methodology (if research)

  - Limitations or caveats

  - Relevant visuals or diagrams (describe)

  - Why it matters for [TOPIC]

- Summarize the page in 3-5 bullet points.

- Identify any contradictions or open questions.

  

Output format:

```markdown

## Extraction: [PAGE TITLE]

  

### Metadata

- **URL**: [URL]

- **Date**: [DATE]

- **Author**: [AUTHOR]

  

### Core Thesis

[One sentence]

  

### Key Facts

- [Fact 1]

- [Fact 2]

- [Fact 3]

  

### Numbers & Metrics

| Metric | Value | Unit | Context |

|--------|-------|------|---------|

  

### Quotes

> [Quote 1] — [Context]

  

### Methodology

[Brief description]

  

### Limitations / Caveats

- [Limitation 1]

- [Limitation 2]

  

### Why It Matters

- [Reason 1]

- [Reason 2]

  

### Open Questions

- [Question 1]

- [Question 2]

```

```

  

---

  

### 4. Comparative Analysis (Multiple Pages)

```

Goal: Compare 3-5 sources on a specific dimension (e.g., features, pricing, claims).

  

Task:

- Extract the relevant dimension from each source (e.g., features, pricing, methodology, claims).

- Normalize the data into a consistent format.

- Identify similarities, differences, and contradictions.

- Highlight the strongest evidence and the weakest.

- Summarize the comparative landscape.

  

Output format:

```markdown

## Comparative Analysis: [DIMENSION]

  

### Sources Compared

| Source | Dimension 1 | Dimension 2 | Dimension 3 | Dimension 4 |

|--------|-------------|-------------|-------------|-------------|

  

### Similarities

- [Similarity 1]

- [Similarity 2]

  

### Differences

- [Difference 1]

- [Difference 2]

  

### Contradictions

- [Contradiction 1] vs [Contradiction 2]

  

### Strongest Evidence

- [Source A] → [Why it’s strong]

  

### Weakest Evidence

- [Source B] → [Why it’s weak]

  

### Synthesis

[One paragraph summarizing the landscape]

```

```

  

---

  

## 🧠 Synthesis & Reasoning

  

### 5. Thesis Generation

```

Goal: Generate a defensible thesis from a set of extracted sources.

  

Task:

- Review the extracted sources for [TOPIC].

- Identify the core claims and evidence.

- Identify contradictions or open questions.

- Generate a thesis that:

  - Is specific and non-trivial

  - Is supported by evidence

  - Addresses contradictions

  - Has operational or strategic implications

- State the thesis in one sentence.

- Support it with 3-5 bullet points of evidence.

- Identify the strongest counter-evidence.

- State the implications for [AUDIENCE].

  

Output format:

```markdown

## Thesis: [TOPIC]

  

### Thesis Statement

[One sentence]

  

### Evidence

- [Evidence 1]

- [Evidence 2]

- [Evidence 3]

  

### Counter-Evidence

- [Counter 1]

  

### Implications for [AUDIENCE]

- [Implication 1]

- [Implication 2]

```

```

  

---

  

### 6. Watchdog Evaluation

```

Goal: Evaluate a tool or platform against Orange Tomato criteria.

  

Task:

- Review the tool’s documentation, claims, and community feedback.

- Evaluate against:

  - Self-hostable: Can core intelligence stay on-premises?

  - API-first: Built for machine-to-machine orchestration?

  - Scalable: Handles high-concurrency agentic bursts?

  - Governance: Does it have policy enforcement or safety features?

  - Cost: Transparent pricing or open-source?

- Assign a Tomato Score (1-10) based on structural disruption, deployability, and fit.

- Write a one-paragraph verdict.

  

Output format:

```markdown

## TITLE: [Tool] — Tomato Score: [X]/10

STATUS: [Active | Legacy | Dead]

CATEGORY: [Email | Social | Browser | Logic | AI-Agents | Workflow]

  

[THE PROBLEM] — legacy system, its maintenance tax

[THE SHIFT] — architectural distinction, not feature list

[TECH DNA] — 3-6 tags

[VERDICT] — one cold paragraph

  

TOMATO SCORE: [X]/10 — [HIGH SIGNAL | WATCH | LEGACY | DEAD]

```

```

  

---

  

## 🔄 Workflow Integration

  

### 7. Research SOP (Daily Use)

```

Goal: Run the daily research SOP for Orange Tomato.

  

Task:

1. **Topic Triage**: Choose 1 primary and 1 backup topic.

2. **Cheap Discovery**: Use free models to scan the topic.

3. **Source Improvement**: Use Exa or Firecrawl to improve sources.

4. **Extraction**: Extract 3-5 primary sources.

5. **Synthesis**: Build a research pack.

6. **Handoff**: Prepare for Claude.

  

Prompt for each step:

```

**Step 1: Topic Triage**

- Working title: [TITLE]

- Why it matters now: [WHY]

- Who is affected: [WHO]

- Likely thesis: [THESIS]

- Known unknowns: [UNKNOWNS]

- Risk of hype: [RISK]

- Expected source difficulty: [DIFFICULTY]

  

**Step 2: Cheap Discovery**

- Use Gemma 4 31B (free) to scan the topic.

- Extract: key players, dates, claims, metrics, initial source list.

  

**Step 3: Source Improvement**

- Use Exa to find overlooked technical posts, hidden documentation, credible niche commentary.

- Shortlist 3-5 pages for extraction.

  

**Step 4: Extraction**

- Use Firecrawl to extract the shortlisted pages.

- Record: URL, source type, date, key claims, relevant numbers, quote candidates, why it matters.

  

**Step 5: Synthesis**

- Normalize findings into the standard template.

- Include: core thesis, evidence table, timeline, contradictions, visual opportunities, suggested angle.

  

**Step 6: Handoff**

- Prepare the research pack for Claude.

- Include: clean pack, writing brief, article shape, style constraints.

```

```

  

---

  

### 8. Browser Use Escalation

```

Goal: Extract content behind interactive flows or dynamic pages.

  

Task:

- Identify the specific information needed (e.g., pricing table, benchmark results, model comparison).

- Navigate to the page and interact as needed (click, scroll, select).

- Extract the exact data or text.

- Summarize the extracted data in a structured format.

  

Prompt:

```

**Page**: [URL]

**Goal**: Extract [SPECIFIC DATA]

**Steps**:

1. Navigate to [URL]

2. [INTERACTION STEPS, e.g., "Click the 'Pricing' tab"]

3. Extract [SPECIFIC DATA]

4. Summarize in a structured format.

  

**Output**:

```markdown

## Extraction: [PAGE TITLE] — [SPECIFIC DATA]

  

### Metadata

- **URL**: [URL]

- **Interaction Steps**: [STEPS]

  

### Extracted Data

[STRUCTURED DATA]

  

### Summary

[SUMMARY]

```

```

  

---

  

## 📌 Tips for Effective Use

  

1. **Be specific**: The more precise your prompt, the better the extraction.

2. **Use templates**: Copy-paste and adapt these templates for your use case.

3. **Iterate**: If the first extraction is noisy, refine the prompt and try again.

4. **Combine tools**: Use discovery → extraction → synthesis in sequence.

5. **Cite sources**: Always include URLs and dates for traceability.

6. **Flag uncertainty**: Mark contradictions, open questions, and weak evidence clearly.

  

---

  

## 🚀 Quick Start

  

1. Copy the template you need.

2. Replace placeholders (e.g., [TOPIC], [URL]).

3. Paste into Browse Web UI.

4. Run, review, and iterate.

  

---

  

*Last updated: 2026-04-25*