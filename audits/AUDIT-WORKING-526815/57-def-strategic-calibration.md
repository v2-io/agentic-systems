# 57 - def-strategic-calibration

Source: `01-aat-core/src/def-strategic-calibration.md`

## First-pass understanding

This segment defines a strategy-layer calibration residual: for each active edge in `Sigma_t`, compare the value increment predicted by the strategy to the observed value increment, then aggregate weighted squared residuals. Its intended role is to localize control regret: not merely "strategy is poor," but "these edge predictions are where the strategy is miscalibrated."

The segment is unusually honest about the hard part. Edge residuals are only meaningful when the edge was traversed, the model makes observed value changes meaningful, and the agent actually followed the plan. For multi-parent nodes, the observed value change may be a joint effect, so assigning it to a particular edge requires extra credit-assignment machinery. Without that, the residual remains useful as an aggregate alarm but not as a precise edge-revision target.

## Diagram attempt

The natural diagram is a calibration gate. Strategy produces a predicted edge value increment; execution and observation produce a realized change; before subtraction is interpretable, the signal has to pass through execution-fidelity and credit-assignment gates. If either gate fails, the same numerical residual can mean several different things.

## Findings and watches

- F47 candidate: the segment depends only on `def-strategy-dag` and `def-value-object`, but its discussion makes load-bearing use of future or undeclared homes: `schema-strategy-persistence`, `deriv-edge-credence-dynamics`, `disc-credit-assignment-boundary`, and `hyp-edge-update-via-gain`. The local definition is discussion-grade, but the persistence and correction claims need those dependencies exposed or clearly marked as forward references.
- Watch: edge-level localization is conditional on solved credit assignment. For multi-parent AND/OR nodes, `r_ij` may measure joint prediction error rather than the error of edge `(i,j)`.
- Watch: the "Phi overestimates actual success under correlated failure" line repeats the earlier F44 topology issue. OR redundancy with positive correlation is optimistic; AND prerequisites can become conservative under the same sign of covariance.
- Watch: the residual compares a strategy-predicted scalar value increment with an observed value change. The text recognizes the type issue, but downstream uses should not forget that the observed change is already a model/objective-mediated attribution, not raw reality.

## Local verdict

The segment is good as a diagnostic sketch and candid about its unresolved machinery. Its final status should stay discussion-grade unless the credit-assignment and edge-update proof homes are pulled into the formal dependency chain.
