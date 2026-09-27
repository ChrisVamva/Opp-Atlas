# DuckDB Architecture

## Role

DuckDB is the durable analytical state layer. Obsidian remains the narrative and human-editable layer. pandas performs transformation, inspection, scoring, and report preparation.

## Three layers

1. **Raw** — extracted Markdown, frontmatter, links, sources, observations, and run logs.
2. **Analytical** — normalized entities, relationships, claims, scores, metrics, and views.
3. **Decision** — selected opportunities, experiments, learning paths, and recorded decisions.

## Recommended tables

`entities`, `relationships`, `sources`, `claims`, `opportunities`, `opportunity_scores`, `research_questions`, `experiments`, `experiment_results`, `person_attributes`, `capability_gaps`, `decisions`, `artifacts`, `ingestion_runs`.

## Data rule

Do not store only a final score. Store the dimensions, evidence references, uncertainty, scoring date, and decision rationale that produced it.

## Exchange format

`Markdown / JSON → raw Parquet → DuckDB views → pandas transformations → reports / graph exports`
