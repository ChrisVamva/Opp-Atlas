-- Active opportunities with weak evidence
SELECT opportunity_id, title, stage,
       evidence_strength, key_assumption, next_action
FROM opportunities
WHERE stage NOT IN ('rejected', 'deferred', 'superseded')
ORDER BY evidence_strength ASC, updated_at ASC;

-- Opportunities with no recorded experiment
SELECT o.opportunity_id, o.title, o.stage
FROM opportunities o
LEFT JOIN experiments e ON e.opportunity_id = o.opportunity_id
WHERE e.experiment_id IS NULL
  AND o.stage IN ('evaluating', 'validating');

-- Capability intersections worth inspecting
SELECT o.title, o.learning_value, o.access,
       o.evidence_strength, o.next_action
FROM opportunities o
WHERE o.stage IN ('candidate', 'researching', 'evaluating')
ORDER BY o.learning_value DESC, o.evidence_strength DESC;
