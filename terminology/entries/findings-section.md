---
slug: findings-section
schema_version: 1
term: findings section
name: Findings Section
brief: "The optional `## Findings` section in a segment — curated catalog entries for contributions worth surfacing externally; drives auto-generation of root `FINDINGS.md`."
layer: framing-vocabulary
status: canon
tags: [segment_structure]
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [epistemic-status-section, discussion-section, working-notes-section]
aliases: []
do_not_confuse: []
---

The `## Findings` section is optional and exists to surface distinctive contributions into the curated catalog at root-level `FINDINGS.md`. Most segments do not carry one — that is the correct default. A Findings section is appropriate for segments whose contribution a thoughtful external reader would identify as part of what makes the framework interesting on its own merits: a result, a recognition, a partition, a synthesis, a domain transfer, a no-go, an architectural commitment.

Each Finding is introduced by a `### {Finding name}` sub-heading and carries five fields in fixed order: **Brief** (plain-language paragraph; Feynman-criterion aspiration), **Impact** (what the finding unlocks or forces), **Novelty Claim** (claim posture + substance), **Related Work** (prior-art landscape), and **Search Log** (dated disclosure of search depth).

The `bin/extract-findings` script walks component OUTLINE.md files, extracts all Findings sections, and emits both `FINDINGS.md` and a condensed `_findings-summary.md` partial for the README.

Full schema and field-by-field guidance are in [`FORMAT.md`](../../FORMAT.md) §Findings.
