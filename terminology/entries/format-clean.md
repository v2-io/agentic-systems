---
slug: format-clean
schema_version: 1
term: format-clean
name: Format-Clean
brief: "A segment stage: all mechanical checks pass — linter, cross-references, notation, math rendering — reached by passing Gate 3."
layer: framing-vocabulary
status: canon
tags: [process_vocabulary]
seq: 5
subgroup: Stages
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [claims-verified, candidate, mechanical-review]
aliases: []
do_not_confuse: [claims-verified, candidate]
---

`stage: format-clean` indicates that the segment has passed Gate 3 (mechanical review): `bin/lint-md`
passes, all `#slug-name` cross-references resolve to existing files, notation matches NOTATION.md,
math renders correctly in GitHub and Obsidian, the document cadence matches the template, and
equation-level tags are present and correct.

Mechanical review is intentionally separate from content review (Gate 2) — they require different
cognitive modes. Gate 3 operates on a segment that is already known to be content-correct;
it ensures that the format is also clean before the segment is considered a candidate.

`format-clean` is the penultimate stage. The final gate (Gate 4, Working Notes disposition)
advances the segment to `candidate`.

Defined in [`FORMAT.md`](../../FORMAT.md) §`stage` — development process state, and §Gate 3.
