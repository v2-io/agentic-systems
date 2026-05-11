---
slug: type-discussion
schema_version: 1
term: type-discussion
name: Discussion (segment type)
brief: "A segment type: conceptual or normative claim used for interpretation — the entire segment is discursive."
layer: framing-vocabulary
status: canon
tags: [segment_types]
seq: 14
subgroup: Structural and Discursive
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [discussion-section, aside, type-sketch]
aliases: [discussion]
do_not_confuse: [discussion-section]
---

A `type: discussion` segment is one whose *entire purpose* is conceptual or normative: it
interprets, connects, or frames claims rather than introducing new definitions, derivations, or
empirical findings. The label is for segments that are wholly discursive — as opposed to the
`## Discussion` section (see [`discussion-section`](discussion-section.md)) that appears within
every segment as the interpretive layer of an otherwise formal claim.

The slug `type-discussion` distinguishes this segment type from the structural section `## Discussion`.
In practice, a `type: discussion` segment might characterize an architectural pattern across
multiple other segments, explore the framework's philosophical underpinnings, or name a
meta-pattern that emerges from several formal results.

Discussion-grade claims must still pass Gate 2's epistemic check: every explanatory claim must
either follow from the formalism or be labeled as hypothesis. "Sounds insightful" is not a
sufficient basis.

Equation-level tags use `*[Discussion]*` to mark discussion-grade equations inline.

Defined in [`FORMAT.md`](../../FORMAT.md) §`type` — what kind of claim.
