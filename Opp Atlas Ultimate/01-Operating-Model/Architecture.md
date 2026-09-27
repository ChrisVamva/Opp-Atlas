# Architecture

## System boundary

Opp Atlas Ultimate has four connected layers:

1. **Opportunity World** — external economic reality: problems, industries, workflows, technologies, capabilities, constraints, and opportunities.
2. **Person Atlas** — the person’s interests, experience, capabilities, constraints, preferences, learning history, and evidence.
3. **Evidence and Action** — sources, claims, research questions, experiments, observations, and decisions.
4. **Data Layer** — DuckDB tables, pandas transformations, reports, and graph exports.

## Central relationship

`Person Atlas + Opportunity World → Intersection → Capability Gap → Experiment or Learning Path → Evidence → Profile Update`

## Data flow

`Markdown / web / interviews / experiments → observations → normalized entities → evidence links → opportunity records → decisions`

## Separation of concerns

- A **problem** is an observed unmet need.
- An **opportunity** is a structured, testable response to a problem in a context.
- A **career hypothesis** is an opportunity-person intersection.
- An **experiment** tests an assumption; it does not prove a business.
- A **decision** records what changed and why.

## Database principle

Never score an opportunity without preserving the evidence, assumptions, uncertainty, and next test behind the score.
