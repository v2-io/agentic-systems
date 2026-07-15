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
primary_source: 01-aat-core/src/der-directed-separation.md
first_asf_mention: 01-aat-core/src/der-directed-separation.md
see_also: [actuated-agent, orient-cascade, sector-condition, class-coercion, wrapping-regime, goal-update-coupling-class, separated, partial, coupled]
aliases: []
do_not_confuse: []
---

The structural backbone of Part II: the epistemic update $f_M$ is
*goal-blind* (does not take $G_t$ as an argument), the purposeful update $f_G$
*depends on* the updated $M_t$, and only the policy couples all substates. The asymmetry is not a parametric quantity to be tuned — it is an architectural property of the agent. Class 1 (Separated) agents satisfy it by construction;
Class 3 (Coupled) architectures (e.g. goal-conditioned LLMs) violate it by construction; Class 2 (Partial) cases have bounded, computable residual coupling in between.

The three-value [Goal-Update Coupling Class](goal-update-coupling-class.md) axis
(Separated / Partial / Coupled) names these architectural positions as properties rather than positional labels.

Derived in
[`#der-directed-separation`](../../01-aat-core/src/der-directed-separation.md);
the meta-architectural status (separation-by-construction vs. as-approximation)
lives at
[`#disc-separability-pattern`](../../01-aat-core/src/disc-separability-pattern.md).
