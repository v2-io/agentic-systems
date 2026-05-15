---
slug: operational-persistence
schema_version: 1
term: operational persistence
name: Operational
notation: "$\\Delta\\rho^\\ast = \\alpha R - \\rho$"
brief: Whether the agent is currently within the guaranteed region — adaptive reserve $\Delta\rho^\ast = \alpha R - \rho$.
layer: prose-symbol
status: canon
tags: [continuity]
subgroup: "Persistence"
source_type: asf
primary_source: 01-aat-core/src/result-persistence-condition.md
first_asf_mention: 01-aat-core/src/result-persistence-condition.md
see_also: [structural-persistence, continuity, adaptive-reserve]
aliases: []
do_not_confuse: []
---

The operational sense of persistence: whether the agent is currently *inside*
the region in which structural persistence guarantees bounded mismatch. Indexed
by the [adaptive reserve](adaptive-reserve.md) $\Delta\rho^\ast = \alpha R -
\rho$ — how much disturbance increase can be absorbed before the structural
guarantee fails.

Stated alongside structural persistence in
[`#result-persistence-condition`](../../01-aat-core/src/result-persistence-condition.md).
