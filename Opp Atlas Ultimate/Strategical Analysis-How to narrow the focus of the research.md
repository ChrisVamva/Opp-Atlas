# Strategic Analysis — How to Narrow the Focus of the Research

## Purpose

Opp Atlas should not begin by trying to map the entire economy. The first research phase should create a small, coherent, evidence-backed dataset that is useful enough to reveal relationships between problems, workflows, actors, capabilities, and opportunities.

The objective is not maximum coverage. The objective is to discover whether the database can produce better opportunity hypotheses than unstructured brainstorming.

## Strategic principle

> Narrow the research space by selecting a tractable opportunity environment, not by prematurely selecting one final business idea.

A good first research domain is:

- narrow enough to investigate deeply;
- broad enough to contain several related problems;
- accessible through public evidence or reachable people;
- connected to the user's capabilities or learning goals;
- capable of producing multiple opportunity hypotheses;
- small enough to model in DuckDB and Obsidian manually.

## The narrowing sequence

```text
Opportunity world
→ Research domain
→ Industry or workflow family
→ Actor and problem cluster
→ Specific workflow
→ Evidence-backed problem
→ Opportunity hypothesis
→ Validation experiment
```
## 1. Choose a research domain

Start with a domain where at least three of the following are true:

- the researcher has repeated access to information;
- the researcher understands some of the vocabulary;
- the domain contains visible workflow friction;
- the domain is undergoing technological or regulatory change;
- problems are documented in public sources;
- small organizations appear underserved;
- the domain connects to capabilities the researcher can develop;
- useful experiments can be run without large capital.

Avoid choosing a domain only because it is fashionable, large, or technically interesting.

### Candidate domains

Use a short list of three to five candidates. For example:

- industrial maintenance and automation;
- research and knowledge workflows;
- small business operations;
- AI-enabled professional services;
- clinical or regulated AI workflows.

Do not research all candidates at once. Compare them first.

## 2. Score candidate domains

Use a simple 1–5 scale:

| Criterion | Question |
|---|---|
| Access | Can evidence or participants be reached? |
| Problem density | Are recurring problems visible? |
| Evidence quality | Are credible sources available? |
| User fit | Does the domain connect to current capabilities or goals? |
| Experimentability | Can small tests be run? |
| Learning value | Will the research build useful capabilities? |
| Data richness | Can entities and relationships be structured? |
| Focus cost | How difficult is it to understand? |

Prefer domains with high access, evidence quality, experimentability, and learning value. Penalize domains that require inaccessible credentials, proprietary data, or large capital before the first test.
## 3. Select a problem cluster, not a single idea

After selecting a domain, identify a cluster of related problems. A useful cluster has a shared:

- actor;
- workflow;
- information flow;
- technology boundary;
- regulatory obligation;
- cost or failure mode;
- capability gap.

For example, instead of researching "AI in industry," research:

> How small industrial organizations handle equipment troubleshooting, maintenance records, technician handoffs, and training when information is fragmented.

This is specific enough to investigate but broad enough to reveal multiple opportunities.

## 4. Narrow around a workflow

Represent the workflow as:

```text
Input → Decision → Action → Handoff → Record → Verification → Output
```

Then ask:

- Where is information copied manually?
- Where does work wait for another person?
- Where does responsibility become unclear?
- Where is the same diagnosis repeated?
- Where is evidence lost?
- Where is a spreadsheet or messaging app used as an unofficial system?
- Where does a new technology create a new monitoring, verification, or governance burden?

The best initial research target is usually a workflow with visible friction and reachable evidence.

## 5. Define the research boundary

Before collecting sources, write a boundary statement:

> This research investigates [workflow/problem cluster] among [actors] in [domain/geography], focusing on [specific uncertainty], during [time period]. It does not attempt to map [excluded areas].

A boundary is successful when it prevents unrelated research from entering the first dataset.
## 6. Select research questions by decision impact

Do not ask, "What can I learn about this industry?"

Ask:

> What could I discover that would cause me to continue, change, or stop investigating this opportunity space?

Rank questions using:

```text
Decision impact × uncertainty × cheapness of learning
```

Prioritize questions about:

1. whether the problem actually occurs;
2. who experiences it and who pays for it;
3. how often it occurs;
4. how costly the current workaround is;
5. what alternatives already exist;
6. why those alternatives are insufficient;
7. what access route exists;
8. what capability or credential is required;
9. what the cheapest credible test would be.

Do not spend the first research cycle on broad market-size estimates, polished competitor maps, or technical architecture unless they affect an immediate decision.

## 7. Use a source hierarchy

For the first batch, prefer:

1. direct observation or interview;
2. official documentation and regulations;
3. procurement specifications and job descriptions;
4. maintenance, incident, and troubleshooting material;
5. customer complaints and product reviews;
6. company case studies;
7. expert analysis;
8. general commentary.

A source is useful only when it supports a specific claim. Store the claim, source, passage or precise paraphrase, confidence, and limitation.
## 8. Convert research into a first batch

The first batch should be deliberately small:

- one research domain;
- one to three related workflows;
- two to four actor groups;
- ten to fifteen problem records;
- five to ten workflow records;
- five or fewer opportunity hypotheses;
- one evidence ledger;
- three to five validation experiments.

Every opportunity must connect to at least one problem. Every problem must connect to an actor, workflow, and evidence state. Every experiment must test a named assumption.

Do not create a separate opportunity record for every interesting observation. Keep observations raw until repeated evidence or a meaningful pattern justifies promotion.

## Promotion rules

### Observation → Problem candidate

Promote when:

- the observation is specific;
- the affected actor is known;
- the context is recorded;
- the source or direct observation is preserved.

### Problem candidate → Problem record

Promote when:

- recurrence is plausible or documented;
- the current workaround is visible;
- the consequence is meaningful;
- the problem is distinguishable from general inconvenience.

### Problem → Opportunity hypothesis

Promote when:

- a possible mechanism can be described;
- the target actor is identifiable;
- an entry point is plausible;
- the key assumption can be tested cheaply.
## 9. Stopping rules

Stop expanding the first batch when:

- the main actors and workflows are represented;
- new sources mostly repeat existing claims;
- the same problem patterns appear across independent sources;
- the strongest uncertainties have research questions;
- each opportunity has a next experiment;
- additional breadth is no longer changing the model;
- the dataset can be reviewed manually without losing provenance.

Stop or defer a research direction when:

- evidence shows the problem is rare or low consequence;
- access depends on unavailable credentials or proprietary data;
- existing alternatives appear adequate;
- the opportunity requires capital or distribution unavailable to the researcher;
- research is becoming a collection of interesting facts without decision impact.

## 10. The first research sprint

### Sprint 1 — Orientation

Select three candidate domains and score them.

### Sprint 2 — Boundary

Choose one domain, define its actor groups, and map two or three workflows.

### Sprint 3 — Evidence

Collect sources using problem, workflow, workaround, cost, alternative, and failure-mode queries.

### Sprint 4 — Normalization

Create problem, workflow, actor, industry, technology, capability, and evidence records.

### Sprint 5 — Opportunity formation

Generate no more than five opportunity hypotheses from the strongest problem clusters.

### Sprint 6 — Validation

Choose the three cheapest credible experiments and record the decision each experiment will influence.

## Final strategic test

The first research batch is successful if it can answer:

> Which recurring problems exist in this focused domain, who experiences them, what workarounds are used, what evidence supports them, and which opportunity hypotheses deserve a real-world test?

If the dataset cannot answer that question, narrow the domain further before collecting more sources.
