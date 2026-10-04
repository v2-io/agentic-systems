# extracted/ — pass-1 survey extractions

One JSONL per survey (`schema_version` per record; target 0.7), records per `../SCHEMA-draft.md`. Fated ids per the schema §v0.7 recipe.

**`gen/` holds each extraction's generator script — the replayability and audit contract:** every JSONL is a pure function of (survey source, generator script); regenerating must reproduce it byte-identically, and the script is the durable record of every migrator judgment (segmentation, type calls, lineage scoping, verifier repairs). Auditing an extraction = reading its script against its source; amending one = editing the script and regenerating, never editing the JSONL. The scripts were authored by the migration agents (2026-08-25) and rescued here from session-scoped scratchpad — a placement decision the migrators correctly flagged rather than made unilaterally.

Note: `sonnet5-1.builder.py` sits beside its JSONL (its migrator staged both in-tree); the others' scripts are in `gen/`. Path references inside scripts may point at scratchpad copies of inputs — the survey sources in `../` are the canonical inputs.
