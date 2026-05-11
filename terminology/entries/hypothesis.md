---
slug: hypothesis
schema_version: 1
term: hypothesis
name: Hypothesis
brief: "A segment type: structurally motivated claim that needs empirical or formal validation."
layer: framing-vocabulary
status: canon
tags: [segment_types]
seq: 9
subgroup: Empirical and Interpretive
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [type-empirical, observation, normative, derived]
aliases: []
do_not_confuse: [type-empirical, derived]
---

A `type: hypothesis` segment states a claim that is structurally motivated by the framework's
prior objects but has not yet been derived formally or validated empirically. The claim is offered
for test — it is specific enough to be falsifiable, and the framework's structure makes it
plausible, but the epistemic work of confirming it remains.

Equation-level tags use `*[Hypothesis]*` to mark hypothesis equations inline.

The segment's `status:` field for a hypothesis is typically `conditional` or `heuristic` rather
than `exact` — the structural motivation does not constitute a derivation. A hypothesis that has
been validated becomes `empirical`; a hypothesis whose formal derivation is completed becomes
`derived` or `result` (and the `type:` field changes accordingly).

Defined in [`FORMAT.md`](../../FORMAT.md) §`type` — what kind of claim.
