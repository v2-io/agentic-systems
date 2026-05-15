---
slug: result
schema_version: 1
term: result
name: Result
brief: "A segment type: formally stated claim backed by a complete derivation."
layer: framing-vocabulary
status: canon
tags: [segment_types]
seq: 6
subgroup: Core Claim Types
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [derived, derivation, corollary, postulate]
aliases: []
do_not_confuse: [derived]
---

A `type: result` segment is a formally stated claim — the equivalent of what other frameworks call
a "theorem" — that is backed by a detailed derivation. The derivation typically lives in a
companion `type: derivation` segment that the result segment depends on.

The label "result" (rather than "theorem") reflects AAT's epistemic character: AAT is a theoretical
framework using existing mathematics, not a pure-mathematics unification project. Using "result"
avoids overclaiming foundational mathematical originality where the framework is integrating,
applying, or extending existing tools.

Named equation-level tags use `*[Result (slug)]*` when referencing a result inline.

Defined in [`FORMAT.md`](../../FORMAT.md) §`type` — what kind of claim (see also the "Why these
labels" note in that section).
