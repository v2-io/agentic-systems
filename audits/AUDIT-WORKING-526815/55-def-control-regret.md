# 55 - def-control-regret

Source: `01-aat-core/src/def-control-regret.md`

## First-pass understanding

This segment completes the two-gap diagnostic by defining control regret as the distance between the current policy value and the best attainable value inside the current policy class, model, horizon, and continuation convention. Satisfaction gap asks whether the threshold is reachable; control regret asks whether the current strategy is leaving reachable value on the table.

The diagnostic split is useful: near-zero regret with positive satisfaction gap points away from strategy tinkering and toward model, capability, horizon, or objective revision; large regret points toward revising `Sigma_t`. The local mathematical definition is straightforward, but its headline non-negativity depends on the current policy belonging to the same policy class optimized by `A_O`.

## Diagram attempt

The cleanest picture is a single value ladder with three markers: current policy value, best attainable value, and the satisfaction threshold. The control-regret interval lives between current and attainable; the satisfaction-gap interval lives between attainable and threshold. This makes the "strategy weak" vs. "goal/capability limit" distinction visible without another table.

## Findings and watches

- F45 candidate: `delta_regret >= 0` requires `pi_current in Pi` and the same model, horizon, objective, and continuation convention on both terms. If the admissible policy class excludes the current policy, or if `A_O` is computed under a different convention than `V_O(M_t, pi_current; N_h)`, the non-negativity statement no longer follows.
- Watch: this segment inherits the C1/C2/C3 convention monotonicity concern from `def-value-object`; the C2 receding-horizon regret ordering is not automatic without alignment, fallback, or full-horizon comparison assumptions.
- Watch: `delta_regret approx 0` is tolerance-relative. In practice the threshold will be dominated by approximation error in estimating `A_O` and `V_O`.
- Watch: high regret is evidence for strategy revision only after separating model error, value misspecification, policy-class mismatch, and computation/optimization error.

## Local verdict

The two-gap construction is conceptually strong and the definition is exact under the intended shared-class convention. The segment should state that convention explicitly where it claims non-negativity.
