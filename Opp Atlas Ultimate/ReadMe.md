# Opp Atlas Ultimate

Opp Atlas Ultimate is the repository and Obsidian vault for an evidence-backed opportunity database.

Its purpose is to model the relationship between:

- real-world problems and unmet needs;
- industries, workflows, technologies, and changing conditions;
- opportunities and their required capabilities;
- a person's interests, experience, capabilities, and constraints;
- research evidence, experiments, decisions, and learning paths.

## Core idea

> Identify viable intersections between an evolving person model and an evolving opportunity world, then convert promising intersections into testable capability-acquisition or execution paths.

## Core loop

`Observe → Normalize → Research → Formulate → Evaluate → Validate → Decide → Learn`

## Repository structure

- `00-Index` — navigation and project entry points.
- `01-Operating-Model` — architecture, ontology, lifecycle, and rules.
- `01-Project-State` — north star, current state, architecture, decisions, experiments, and open questions.
- `02-Opportunity-World` — problems, opportunities, industries, workflows, capabilities, and technology.
- `03-Person-Atlas` — the evidence-backed personal capability graph.
- `04-Evidence-and-Research` — sources, claims, research questions, and syntheses.
- `05-Validation-and-Experiments` — experiments that reduce uncertainty.
- `06-Decisions-and-Portfolio` — selection, deferral, rejection, and sequencing.
- `07-Data-Layer` — DuckDB schemas, queries, and analytical design.
- `08-Templates` — reusable note templates.
- `99-Archive-and-Migration` — migration notes and superseded material.

## Data architecture

Obsidian is the human-readable knowledge layer. DuckDB is the structured analytical layer. pandas may be used for transformation, inspection, scoring, and reporting.

The intended data flow is:

`Markdown / research / experiments → normalized records → evidence links → opportunity analysis → decisions`

## Working principles

1. Preserve provenance for important claims and relationships.
2. Separate facts, source-based claims, inferences, assumptions, and unknowns.
3. Do not score or promote an opportunity without recording its evidence and uncertainty.
4. Use experiments to test assumptions before making large commitments.
5. Keep the Person Atlas and Opportunity World connected but conceptually distinct.
6. Treat decisions and failed experiments as valuable project data.

## First implementation target

Build a small, queryable opportunity dataset containing problems, workflows, capabilities, opportunities, evidence claims, experiments, and decisions. Use it to test whether the system can identify a plausible person–opportunity intersection and explain the capability gap between them.
