---
slug: claims-verified
schema_version: 1
term: claims-verified
name: Claims-Verified
brief: "A segment stage: content reviewed — derivations valid, labels accurate, no known issues with formal expressions — reached by passing Gate 2."
layer: framing-vocabulary
status: canon
tags: [process_vocabulary]
seq: 4
subgroup: Stages
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [deps-verified, format-clean, content-review]
aliases: []
do_not_confuse: [deps-verified, format-clean]
---

`stage: claims-verified` indicates that the segment has passed Gate 2 (content review): the
derivations are valid, the `type:` and `status:` labels accurately reflect the actual epistemic
strength, no known issues exist with formal expressions, and Discussion-section claims have been
subjected to the same epistemic scrutiny as Formal Expression derivations.

Gate 2 is the substantive gate — the one that evaluates whether the segment's claims are honest
and correct. It applies the three epistemic triage questions: what prior objects make this claim
well-typed; what competing formulation would also fit; what observation would falsify this claim.
A mismatch found at Gate 2 returns the segment to `draft` with a specific note.

`claims-verified` is a prerequisite for `format-clean` (Gate 3). Content correctness must be
established before mechanical polish is applied — it wastes effort to clean a segment that will
be returned to draft when an error is found.

Defined in [`FORMAT.md`](../../FORMAT.md) §`stage` — development process state, and §Gate 2.
