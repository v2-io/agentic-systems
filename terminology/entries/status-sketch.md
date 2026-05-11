---
slug: status-sketch
schema_version: 1
term: status-sketch
name: Sketch (epistemic status)
brief: "An epistemic status: direction identified but formalization incomplete — the segment is actively in progress."
layer: framing-vocabulary
status: canon
tags: [epistemic_vocabulary]
seq: 8
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [discussion-grade, type-sketch, draft]
aliases: [sketch]
do_not_confuse: [discussion-grade, type-sketch]
---

`status: sketch` indicates that the direction of the claim is identified — the framework's
structure points toward this claim — but the formalization is not yet complete. Unlike
`discussion-grade` (which indicates argumentative but non-formal work that may be complete in
its argumentative character), `status: sketch` indicates *unfinished* work where rigor remains
to be achieved.

The slug `status-sketch` distinguishes this as a frontmatter *status* value from
[`type-sketch`](type-sketch.md), which is a *segment type* value. A segment with `type: sketch`
and `status: sketch` is at the bottom of both axes: it describes a direction (type) that is not
yet formalized (status). As work progresses, the status advances (toward `heuristic`, `conditional`,
or `exact`) while the type might change (toward `result`, `derived`, or `formulation`).

A segment at `status: sketch` cannot advance through the promotion gates — it cannot pass
Gate 2 (content review) because there is not yet enough formal content to review. The discipline
is making the incompleteness visible rather than letting partly-done claims silently masquerade
as established ones.

Defined in [`FORMAT.md`](../../FORMAT.md) §`status` — epistemic strength.
