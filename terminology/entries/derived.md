---
slug: derived
schema_version: 1
term: derived
name: Derived
brief: "A segment type: logical consequence of prior claims under stated assumptions — only one form fits."
layer: framing-vocabulary
status: canon
tags: [segment_types]
seq: 5
subgroup: Core Claim Types
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [result, derivation, formulation, corollary]
aliases: []
do_not_confuse: [formulation, result]
---

A `type: derived` segment states a logical consequence of prior claims. The claim follows
necessarily from the prior objects — epistemic triage question 2 ("what competing formulation
would also fit?") should answer "none" for a `derived` segment. If alternatives exist, the
segment is better typed `formulation`.

The distinction between `derived` and `result` is one of documentation depth: a `derived` segment
states that the claim follows from prior claims, while a `result` segment additionally contains
a complete formal derivation (typically in a companion `derivation` segment) and is formally stated
with full conditions. Short logical consequences that don't warrant their own derivation document are
typed `derived`; major claims that anchor the theory are typed `result`.

Equation-level tags on derived claims use `*[Derived (slug, from ...)]*` or
`*[Derived (Conditional on ...)]*`.

Defined in [`FORMAT.md`](../../FORMAT.md) §`type` — what kind of claim.
