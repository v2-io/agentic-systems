# 68 - impl-strategy-dynamics

Source: `01-aat-core/src/impl-strategy-dynamics.md`

## First-pass understanding

This chapter-end discussion synthesizes strategy dynamics into several cross-segment stories: forgetting and detection latency, causal-insufficiency no-go plus escape, observability dominance and depth penalties, adaptive-gain/variational refinements, and a unified non-stationary RL convergence narrative. It is intentionally a map of compositions rather than a single derivation.

The map is useful, but it inherits and sometimes amplifies unresolved issues from the home segments. It also depends heavily on appendix/proof homes not yet read in this AAT order. Under the current protocol, proof credit for those parts stays deferred.

## Diagram attempt

I represented the segment as a synthesis hub with three classes of inputs: already-read local claims, unresolved local caveats, and deferred appendix/proof homes. The point is to preserve the map while preventing its strongest claims from laundering future proof obligations into the current chapter.

## Findings and watches

- F78 candidate: the segment states the forgetting prerequisite as `(1-lambda) > rho_Sigma/R_Sigma`, even though `schema-strategy-persistence` now foregrounds an exact form and my F72 questions the denominator convention. This chapter-end synthesis should not revert to the simplified bound without qualification.
- F79 candidate: the no-go boundary routes are numbered as S1-S5 but do not match the S1-S5 scope conditions in `der-causal-insufficiency-detection`. There, S1-S5 are conditions of the no-go; here, S1-S5 are described as escape routes with different content. This creates avoidable reference ambiguity.
- F80 candidate: the segment says joint sibling observability under exploration is available to every AAT agent within agency scope via loop-Level-2 access. The home segment explicitly treats joint sibling observability as a precondition and lists domains where it can be unavailable. Loop intervention alone does not guarantee joint observability.
- F81 candidate: the segment repeats the observability-investment claim that instrumentation improves `alpha_Sigma` whenever `theta_1 > 1/2`; this inherits F53's formula concern.
- F82 candidate: the unified RL convergence paragraph says strategic-tempo machinery is verified across "linear chain, balanced tree, unbalanced tree, full DAG with feedback"; the local schema segment described verified cases as single edge, two-edge AND observable/unobservable, two-arm OR, and mixed L1 augmented DAG. If the former list comes from a NeurIPS proof home, it needs a clear source label.
- Watch: adaptive-gain, variational-sector, Bretagnolle-Huber, and coordinate-forcing claims are future appendix/proof-home material in this outline. They may be correct, but this pass has not reached them.

## Local verdict

As a chapter-end synthesis, the segment is valuable but too assertive in places. It should explicitly distinguish already-established AAT-core results, unresolved local caveats, and deferred appendix-backed claims.
