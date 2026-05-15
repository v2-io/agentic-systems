---
slug: credit-assignment-boundary
schema_version: 1
term: credit assignment boundary
name: Credit Assignment Boundary
notation:
brief: The boundary between tractable and intractable attribution of outcomes to strategy DAG edges — solvable when intermediates are observable, #P-hard in the general partially-observable case.
layer: framing-vocabulary
status: canon
tags: [structural_concepts, core_quantities]
source_type: asf
primary_source: 01-aat-core/src/disc-credit-assignment-boundary.md
first_asf_mention: 01-aat-core/src/disc-credit-assignment-boundary.md
see_also: [strategy-dag, strategic-tempo, strategy-persistence]
aliases: []
do_not_confuse: []
---

AAD's version of the temporal credit assignment problem applied to strategy DAGs: given an
observed outcome at the root (and possibly some intermediate nodes), produce per-edge signals
that drive credences toward truth. The segment characterizes the structure of this problem
rather than solving it.

**Tractable cases**: all intermediates observable (each edge updates from its own data);
binary outcomes with independent edges in a linear chain (plan-level fallback recovers when
intermediates are hidden); tree DAGs with observable leaves (belief propagation is exact).

**Three independent intractability barriers** in the general case:
1. **#P-hardness**: exact per-edge attribution is as hard as computing Shapley values for
   monotone Boolean functions — #P-complete in general.
2. **Information-theoretic underdetermination**: with fewer observable nodes than edges,
   some directions in $\boldsymbol\theta$-space are fundamentally unresolvable from data.
3. **Posterior correlation barrier**: any factored (per-edge independent) posterior discards
   the correlation introduced by failures at multi-parent nodes — coupled corrections are
   inherent to the problem.

**The key result**: three guarantees hold *without* solving credit assignment — plan-level
persistence (Prop B.5), the diagnostic framework (satisfaction gap, control regret), and
observability-dominance (which edges can receive informative signals at all). The design
requirement for any credit-assignment scheme is **directional fidelity**: expected corrections
must point toward true credences. This is sufficient for persistence; optimality is not required.

The primary practical insight: credit assignment is an **observability design problem**, not
an algorithm design problem. Strategies with observable intermediates (instrumented plans,
OKRs, staged rollouts) sidestep the intractability entirely.

Discussed in [`#disc-credit-assignment-boundary`](../../01-aat-core/src/disc-credit-assignment-boundary.md).
