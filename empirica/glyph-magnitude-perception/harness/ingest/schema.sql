-- glyph-magnitude-perception: derived index over the append-only JSONL truth.
-- The database is DISPOSABLE — rebuildable at any time via ingest.py; nothing
-- lives here that is not derivable from data/. psql-18 (PostgreSQL 18) target.

CREATE EXTENSION IF NOT EXISTS vector;

-- Every pass-1 / phase-1.5 record, whole document preserved; typed columns are
-- conveniences extracted from doc, never the source of truth.
CREATE TABLE IF NOT EXISTS survey_records (
    id              text PRIMARY KEY,          -- fated id
    surveyor        text NOT NULL,             -- file basename
    layer           text NOT NULL,             -- 'pass1' | 'capture-correction'
    record_type     text,                      -- sequence/negative/meta/morph/...
    schema_version  text,
    source_span     text,
    glyphs          text,                      -- surveyor's written linearization
    lineage         text,                      -- NON-ANALYTICAL metadata (Joseph 2026-08-25): never condition analyses on this
    felt_strength_verbatim   text,
    felt_immediacy_verbatim  text,
    note_verbatim   text,
    doc             jsonb NOT NULL,            -- the full record, verbatim
    embedding       vector(1024)               -- future: feature-correlate program; NULL until computed
);

CREATE INDEX IF NOT EXISTS survey_records_surveyor_idx ON survey_records (surveyor);
CREATE INDEX IF NOT EXISTS survey_records_type_idx     ON survey_records (record_type);
CREATE INDEX IF NOT EXISTS survey_records_doc_idx      ON survey_records USING gin (doc);

-- Revision arcs, one row per link (a record's revises list unnested).
CREATE OR REPLACE VIEW revision_arcs AS
SELECT r.id AS from_id, r.surveyor, r.layer,
       l->>'id'            AS to_id,
       l->>'revision_kind' AS revision_kind,
       l->>'revises_span'  AS revises_span
FROM survey_records r,
     jsonb_array_elements(CASE jsonb_typeof(r.doc->'revises')
                          WHEN 'array' THEN r.doc->'revises' ELSE '[]'::jsonb END) AS l;

-- Per-glyph occurrence map (codepoints unnested) for cross-surveyor overlap work.
CREATE OR REPLACE VIEW glyph_occurrences AS
SELECT r.id, r.surveyor, r.record_type, cp.value #>> '{}' AS codepoint
FROM survey_records r,
     jsonb_array_elements(CASE jsonb_typeof(r.doc->'codepoints')
                          WHEN 'array' THEN r.doc->'codepoints' ELSE '[]'::jsonb END) AS cp;
