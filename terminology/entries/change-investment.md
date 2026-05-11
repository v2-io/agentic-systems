---
slug: change-investment
schema_version: 1
term: change investment
name: Change investment
notation: ""
brief: Accept higher upfront implementation cost when amortized savings across expected future changes exceed it.
layer: framing-vocabulary
status: weak
tags: [structural_concepts]
source_type: asf
primary_source: 02-tst-core/src/der-change-investment.md
first_asf_mention: 02-tst-core/src/der-change-investment.md
see_also: [temporal-optimality, coherence-coupling]
aliases: []
do_not_confuse: []
---

The pairwise decision rule derived from dual-optimization: choose the costlier
implementation now when the upfront delta is less than the expected number of
future features times the per-feature savings. Formally: accept extra cost $X$
now over $Y$ per future change when $X < \hat{n}_{\text{future}} \times Y$.

Citability is borderline — the term is specific to TST's amortization framing
but is not yet standalone-citable. Status `weak` reflects this.

See [`#der-change-investment`](../../02-tst-core/src/der-change-investment.md).
