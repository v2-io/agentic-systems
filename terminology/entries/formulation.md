---
slug: formulation
schema_version: 1
term: formulation
name: Formulation
brief: "A segment type: representational or modeling choice — this form is motivated but alternatives exist."
layer: framing-vocabulary
status: canon
tags: [segment_types]
seq: 4
subgroup: Core Claim Types
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [definition, derived, result, postulate]
aliases: []
do_not_confuse: [derived]
---

A `type: formulation` segment makes a representational or modeling choice — how to mathematically
express something where multiple forms would be compatible with the prior objects. The form chosen
is motivated by parsimony, domain fit, or downstream tractability, not by mathematical necessity.

The key epistemic difference between `formulation` and `derived`: a derived claim follows uniquely
from its premises (only one form fits the prior objects); a formulation acknowledges that at least
one alternative exists and explains why this form is the better choice. Epistemic triage question 2
("what competing formulation would also fit?") distinguishes these — if the answer is "none," the
segment is `derived`; if the answer is "at least one," it is `formulation`.

Most definitions that involve a representational choice (e.g., how to encode agent state, what
structure to assign the strategy) should be typed `formulation` rather than `definition`.

Equation-level tags on formulation equations use `*[Formulation]*`.

Defined in [`FORMAT.md`](../../FORMAT.md) §`type` — what kind of claim.
