# Canonical Ontology

## Opportunity-world entities

- Problem
- Opportunity
- Industry
- Workflow
- Technology
- Market actor
- Capability
- Constraint
- Emerging change
- Company or alternative

## Person entities

- Person
- Interest
- Experience
- Demonstrated capability
- Learning objective
- Preference
- Personal constraint
- Evidence of capability

## Action and epistemic entities

- Source
- Observation
- Claim
- Hypothesis
- Research question
- Experiment
- Result
- Decision
- Artifact

## Key relationships

`problem —occurs_in→ workflow`
`workflow —belongs_to→ industry`
`opportunity —addresses→ problem`
`opportunity —requires→ capability`
`person —has_evidence_for→ capability`
`person —faces→ constraint`
`opportunity —intersects_with→ person`
`intersection —creates→ capability_gap`
`claim —supported_by→ source`
`experiment —tests→ hypothesis`
`decision —acts_on→ opportunity`

## Epistemic rule

Every important assertion is typed as fact, source-based claim, inference, assumption, or unknown.
