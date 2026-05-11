---
slug: adaptive-reserve
schema_version: 1
term: adaptive reserve
name: Adaptive reserve
notation: "$\\Delta\\rho^\\ast$"
brief: Shock tolerance — how much disturbance increase before persistence fails.
layer: prose-symbol
status: canon
tags: [core_quantities]
source_type: asf
primary_source: 01-aad-core/src/result-persistence-condition.md
first_asf_mention: 01-aad-core/src/result-persistence-condition.md
see_also: [structural-persistence, operational-persistence, adaptive-tempo, sector-condition]
aliases: []
do_not_confuse: []
---

The headroom between currently observed disturbance and the maximum the
correction machinery can absorb while still satisfying the persistence
condition: $\Delta\rho^\ast = \alpha R - \rho$. Operational state lies *inside*
the structural guarantee when the reserve is positive; agents track the reserve
to anticipate when persistence is about to fail.

Stated alongside the persistence condition in
[`#result-persistence-condition`](../../01-aad-core/src/result-persistence-condition.md).
