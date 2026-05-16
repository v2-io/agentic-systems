# 66 - schema-strategy-persistence

Source: `01-aat-core/src/schema-strategy-persistence.md`

## First-pass understanding

This segment instantiates the sector-persistence template for strategy dynamics and makes the key strategic-layer distinction: ordinary accumulating Bayesian edge updates lose plasticity because `1/(n+1)` decays with experience. Long-run strategic persistence therefore needs finite effective memory, discounting, restart, or some equivalent nonzero-gain mechanism.

The conceptual claim is strong. The exact forgetting formula is the part that needs the most care. The segment states the discounted update as "shrink pseudo-counts by `lambda`, then add the new observation"; with that update ordering, the steady-state denominator used by the new observation appears to be `1/(1-lambda)`, giving gain `1-lambda`, not `(1-lambda)/(2-lambda)`. The segment's hard ceiling at `rho/R >= 1/2` depends entirely on the latter convention.

## Diagram attempt

I represented the two possible conventions as a small timing diagram. If the gain is computed after discounting and adding the current sample, the denominator is the post-discount-plus-sample count. If the gain is computed against the previous steady-state count plus one, the segment's formula appears. The segment needs to state which timing convention Prop B.1 is being applied to.

## Findings and watches

- F72 candidate: the exact forgetting prerequisite may be off by an update-order convention. The segment defines discounted counts by `alpha <- lambda alpha + y`, `beta <- lambda beta + (1-y)`, which yields steady total count `n_ss=1/(1-lambda)`. If the current observation's mean-update denominator is the post-discount-plus-sample count, the gain is `1/n_ss = 1-lambda`, not `(1-lambda)/(2-lambda)`. The claimed hard ceiling at `rho >= R/2` disappears under the `1-lambda` convention.
- F73 candidate: the two-arm OR persistence condition names a minimum exploration rate `epsilon > rho(n_max+1)/R`, but the greedy arm also needs enough allocation: `(1-epsilon)/(n_1+1) > rho/R`. The admissible interval has both a lower and an upper bound unless the greedy arm's threshold is otherwise guaranteed.
- Watch: the schema's general persistence proof depends on `result-sector-persistence-template` and `deriv-edge-credence-dynamics`, which are not yet read in this AAT order. Local status as sketch is appropriate.
- Watch: "iff" language should stay tied to the template model and its assumptions; outside verified topologies, the schema is not yet a full necessity-and-sufficiency theorem.
- Watch: the segment cleanly separates `delta_s` plan-confidence persistence from `delta_strategic` per-edge value-residual persistence. That distinction should be preserved in the orient cascade.

## Local verdict

The finite-gain prerequisite is likely one of the most important strategy-dynamics ideas so far. The exact threshold and hard ceiling need a convention audit before being treated as a finding.
