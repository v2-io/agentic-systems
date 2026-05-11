---
slug: formal-expression-section
schema_version: 1
term: formal expression section
name: Formal Expression Section
brief: "The `## Formal Expression` section in a segment — carries the mathematical content with equation-level epistemic tags."
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

The `## Formal Expression` section is the primary mathematical content of a segment. It carries the definitions, derivations, or results that constitute the segment's claim, annotated at the equation level with tags (`*[Definition (slug)]*`, `*[Derived (slug, from ...)]*`, `*[Hypothesis]*`, etc.) that mark each equation's epistemic status independently of the surrounding prose.

For `type: derivation` segments with multiple claims of mixed strength, a derivation-audit table (`### What Is Derived vs. What Is Chosen`) typically appears near the end of this section, before `## Epistemic Status`.

Conventions are in [`FORMAT.md`](../../FORMAT.md) §Document Cadence and §Equation-Level Tags.
