---
slug: implementation-time
schema_version: 1
term: implementation time
name: Implementation time
notation: "$t_{\\text{impl}}$"
brief: Time from first surviving modification to feature completion.
layer: prose-symbol
status: weak
tags: [core_quantities]
source_type: asf
primary_source: 02-tst-core/src/def-implementation-time.md
first_asf_mention: 02-tst-core/src/def-implementation-time.md
see_also: [coherence-coupling, atomic-changeset]
aliases: []
do_not_confuse: []
---

One half of the dual-optimization decomposition of total feature time:
$\text{time}(F) = t_{\text{comp}}(F,S) + t_{\text{impl}}(F,S)$. Covers writing, modifying, local testing, and addressing issues found during implementation — everything after the comprehension phase ends. The split routes optimization interventions cleanly: comprehension time is reduced by proximity and coherence; implementation time is reduced by interface clarity and tooling.

Citability is borderline — "implementation time" is widely used in software engineering but TST's specific decomposition boundary is not yet standalone-citable. Status `weak` reflects this.

See [`#def-implementation-time`](../../02-tst-core/src/def-implementation-time.md).
