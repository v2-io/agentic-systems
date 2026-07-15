---
slug: mechanical-review
schema_version: 1
term: mechanical review
name: Mechanical Review
brief: "Gate 3: verifies linter, cross-references, notation, and math rendering pass — different cognitive mode from Gate 2. Produces stage: format-clean."
layer: framing-vocabulary
status: canon
tags: [process_vocabulary]
seq: 13
subgroup: Gates
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [format-clean, content-review, notes-disposition]
aliases: [gate 3]
do_not_confuse: [content-review, notes-disposition]
---

Mechanical review is Gate 3 in the segment promotion workflow — separate from Gate 2 (content review) by design, because they require different cognitive modes. Passing Gate 3 advances a segment from `claims-verified` to `format-clean`.

The gate checklist:
- `bin/lint-md` passes with no errors
- All `#slug-name` cross-references resolve to existing files
- Notation matches NOTATION.md
- Math renders correctly in both GitHub and Obsidian (observing the compatibility notes in FORMAT.md)
- Document cadence matches the template (frontmatter → title → summary → formal expression → epistemic status → discussion → findings → working notes)
- Equation-level tags are present and correct for each equation

The sequencing is intentional: content correctness (Gate 2) before mechanical polish (Gate 3),
because it wastes effort to clean a segment that will be returned to draft when a content issue is found. A `format-clean` segment is ready for Gate 4 (Working Notes disposition).

See [`FORMAT.md`](../../FORMAT.md) §Gate 3.
