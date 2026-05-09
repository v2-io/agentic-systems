---
slug: directed-separation
schema_version: 1
term: directed separation
name: Directed separation
brief: $M_t$ dynamics independent of $G_t$ (conditional on processing topology).
layer: prose-symbol
status: canon
tags: [structural_concepts]
source_type: asf
primary_source: 01-aad-core/src/der-directed-separation.md
first_asf_mention: 01-aad-core/src/der-directed-separation.md
see_also: [actuated-agent, orient-cascade, sector-condition, class-coercion, wrapping-regime]
aliases: []
do_not_confuse: []
---

The structural backbone of Section II: the epistemic update $f_M$ is
*goal-blind* (does not take $G_t$ as an argument), the purposeful update $f_G$
*depends on* the updated $M_t$, and only the policy couples all substates. The
asymmetry is not a parametric quantity to be tuned — it is an architectural
property of the agent. Modular agents satisfy it by construction; fully merged
architectures (e.g. goal-conditioned LLMs) violate it by construction; partially
modular cases sit in between.

Derived in
[`#der-directed-separation`](../../01-aad-core/src/der-directed-separation.md);
the meta-architectural status (separation-by-construction vs. as-approximation)
lives at
[`#disc-separability-pattern`](../../01-aad-core/src/disc-separability-pattern.md).
