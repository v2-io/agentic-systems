---
slug: sector-condition
schema_version: 1
term: sector condition
name: Sector condition
brief: Nonlinear correction guarantee enabling Lyapunov stability analysis.
layer: prose-symbol
status: canon
tags: [structural_concepts]
source_type: mathematical
primary_source: 01-aat-core/src/deriv-sector-condition.md
first_asf_mention: 01-aat-core/src/deriv-sector-condition.md
see_also: [directed-separation, adaptive-tempo, adaptive-reserve]
aliases: []
do_not_confuse: []
---

A nonlinearity bound — the correction map sits inside a sector cone — under
which Lyapunov stability of the adaptive loop can be established without
linearizing. Adopted from control theory and made primary in AAD over the
linear-ODE pedagogy: the sector framing covers the saturating, asymmetric, and
piecewise correction laws that real adaptive systems use, while still admitting
clean persistence guarantees.

Derived in
[`#deriv-sector-condition`](../../01-aat-core/src/deriv-sector-condition.md);
the stability result built on it lives at
[`#result-sector-condition-stability`](../../01-aat-core/src/result-sector-condition-stability.md).
