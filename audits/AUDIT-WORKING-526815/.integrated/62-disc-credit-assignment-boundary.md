# 62 - disc-credit-assignment-boundary

Source: `01-aat-core/src/disc-credit-assignment-boundary.md`

## First-pass understanding

This segment characterizes credit assignment as a boundary problem rather than pretending to solve it. It separates tractable cases with observable intermediates from hard cases where exact per-edge attribution is computationally or information-theoretically blocked. The important positive claim is modest and useful: many persistence guarantees operate at plan level and do not require exact edge-level attribution.

The default gradient signal is the most delicate part. It projects the plan-level residual through the plan-value Jacobian in log-odds coordinates and discounts by identifiability. That is a plausible Level-1 approximate signal, but it should be framed as plan-error-reducing, not as guaranteeing each edge's update points toward that edge's true credence in general.

## Diagram attempt

The diagram shows one scalar plan residual being projected onto several edge coordinates. If all edge errors are aligned, this works as a rough per-edge signal. If edge errors have mixed signs, the same residual sign is broadcast through all positive Jacobian components, so at least some edge-local directions can be wrong.

## Findings and watches

- F60 candidate: the segment claims the gradient signal satisfies per-edge directional fidelity for monotone AND/OR DAGs because `J_k >= 0`. A single plan-level residual has one sign; if one edge is overestimated and another is underestimated, broadcasting that residual through nonnegative `J_k` cannot point every edge toward its own truth. The claim is defensible for plan-level error reduction or aligned-error regimes, not general per-edge truth.
- F61 candidate: moving the default gradient update to log-odds prevents probability-domain escape, but the update still divides by `||J||^2`. When `||J||` is near zero, the update can become arbitrarily large in log-odds; when it is zero, it is undefined. The old boundedness failure is transformed, not fully eliminated, unless damping or a support condition is added.
- F62 candidate: the segment repeats the "causally insufficient DAG systematically overestimates success" claim. As noted earlier, correlation bias sign depends on topology; OR-style redundancy with positive covariance is optimistic, while AND prerequisites can be conservative.
- Watch: the #P-hardness argument is at sketch level, as the segment says. The compactness of representing weighted-threshold games in the allowed AND/OR strategy formalism should be explicit before promotion.
- Watch: the segment depends on appendix/home segments that are much later in the AAT outline (`deriv-edge-credence-dynamics`, `deriv-edge-update-natural-parameter`) for several core claims. Under this pass, their proof credit remains deferred.
- Watch: the working note references pending audits and spikes; I have not read those under the current protocol.

## Local verdict

The boundary taxonomy is valuable. The default gradient signal should be presented as a practical Level-1 projection with plan-level directional value, not as a general solution to per-edge directional fidelity.
