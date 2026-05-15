---
slug: derivation
schema_version: 1
term: derivation
name: Derivation
brief: "A segment type: a complete formal derivation backing a result or derived claim."
layer: framing-vocabulary
status: canon
tags: [segment_types]
seq: 8
subgroup: Core Claim Types
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [result, derived, corollary]
aliases: []
do_not_confuse: [result, derived]
---

A `type: derivation` segment is the formal derivation document — the step-by-step argument — that
backs a `result` or `derived` segment. Separating derivation from result allows the theory's claim
structure (what follows from what) to be navigable without requiring readers to wade through every
algebraic manipulation.

`derivation` segments are the recommended home for derivation-heavy content that supports a
main-section claim: regret-bound derivations, Fisher-information calculations, sector-condition
algebra, Cramér-Rao floor calculations, and similar material. They often carry a derivation-audit
table (`### What Is Derived vs. What Is Chosen`) near the end of the Formal Expression section.

The label "derivation" (rather than "proof") avoids overclaiming mathematical inevitability where
AAT is applying or adapting existing mathematics to a new domain.

Defined in [`FORMAT.md`](../../FORMAT.md) §`type` — what kind of claim (see also the "Why these
labels" note) and §Derivation-audit table.
