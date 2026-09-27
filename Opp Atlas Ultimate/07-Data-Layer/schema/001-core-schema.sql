-- Opp Atlas Ultimate: minimal analytical schema
CREATE TABLE IF NOT EXISTS entities (
    entity_id VARCHAR PRIMARY KEY,
    entity_type VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    status VARCHAR,
    note_path VARCHAR,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    confidence DOUBLE
);

CREATE TABLE IF NOT EXISTS relationships (
    relationship_id VARCHAR PRIMARY KEY,
    source_entity_id VARCHAR NOT NULL,
    relationship_type VARCHAR NOT NULL,
    target_entity_id VARCHAR NOT NULL,
    confidence DOUBLE,
    evidence_status VARCHAR,
    source_claim_id VARCHAR
);

CREATE TABLE IF NOT EXISTS sources (
    source_id VARCHAR PRIMARY KEY,
    title VARCHAR NOT NULL,
    source_type VARCHAR,
    locator VARCHAR,
    publisher VARCHAR,
    published_at DATE,
    accessed_at DATE,
    reliability VARCHAR
);

CREATE TABLE IF NOT EXISTS claims (
    claim_id VARCHAR PRIMARY KEY,
    claim_text VARCHAR NOT NULL,
    claim_type VARCHAR NOT NULL,
    confidence DOUBLE,
    status VARCHAR,
    source_id VARCHAR,
    entity_id VARCHAR,
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS opportunities (
    opportunity_id VARCHAR PRIMARY KEY,
    title VARCHAR NOT NULL,
    problem_entity_id VARCHAR,
    stage VARCHAR NOT NULL,
    mechanism VARCHAR,
    strategic_fit DOUBLE,
    access DOUBLE,
    value_potential DOUBLE,
    validation_cost DOUBLE,
    risk DOUBLE,
    learning_value DOUBLE,
    evidence_strength DOUBLE,
    key_assumption VARCHAR,
    next_action VARCHAR,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS experiments (
    experiment_id VARCHAR PRIMARY KEY,
    opportunity_id VARCHAR NOT NULL,
    hypothesis VARCHAR NOT NULL,
    method VARCHAR,
    success_signal VARCHAR,
    kill_signal VARCHAR,
    status VARCHAR,
    result VARCHAR,
    decision_impact VARCHAR,
    completed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS decisions (
    decision_id VARCHAR PRIMARY KEY,
    opportunity_id VARCHAR,
    decision VARCHAR NOT NULL,
    rationale VARCHAR,
    evidence_ids VARCHAR[],
    decided_at TIMESTAMP
);
