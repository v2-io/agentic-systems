---
slug: notes-disposition
schema_version: 1
term: notes disposition
name: Notes Disposition
brief: "Gate 4: every Working Notes item resolved — incorporated, deferred, or promoted. Produces stage: candidate."
layer: framing-vocabulary
status: canon
tags: [process_vocabulary]
seq: 14
subgroup: Gates
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [candidate, mechanical-review, working-notes-section]
aliases: [gate 4]
do_not_confuse: [mechanical-review]
---

Notes disposition is Gate 4 in the segment promotion workflow — the final gate, advancing a segment from `format-clean` to `candidate`. A segment with unresolved Working Notes cannot advance.

Every item in `## Working Notes` must be explicitly resolved in one of three ways:
1. **Resolved** — the answer is incorporated into the segment's Formal Expression or Discussion. Delete the note.
2. **Deferred** — the question is real but out of scope for this segment. Move it to `TODO.md` (concrete open work) or a spike document (exploratory), with rationale. Delete the note from the segment.
3. **Promoted** — the question warrants its own segment or is a known gap in the outline. Add a cross-reference and delete the note.

The completion criterion is simple: the `## Working Notes` section is empty or absent. The segment says what it means to say — no unresolved threads, no deferred promises that haven't been handed off, no open questions that a reader would need to know about to evaluate the claim.

See [`FORMAT.md`](../../FORMAT.md) §Gate 4.
