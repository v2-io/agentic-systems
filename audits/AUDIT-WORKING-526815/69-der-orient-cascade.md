# 69 - der-orient-cascade

Source: `01-aat-core/src/der-orient-cascade.md`

## First-pass understanding

This segment turns epistrophe into an ordered diagnostic cascade for actuated agents. The order is sensible: update `M_t`, compute attainability, compute control regret, inspect strategy calibration and causal sufficiency, and only then revise the objective. The best part is that objective revision is explicitly last, after model error, policy-class limitations, continuation convention, and strategy structure have been checked.

The segment also does a good job separating plan-level calibration, edge-level localization, and L0-to-L1 causal-sufficiency escalation. The proof status is mixed: the ordering is largely dependency-forced, while the content of step 4 depends on strategy-persistence and edge-dynamics proof homes that are later in the outline.

## Diagram attempt

I drew the cascade as a staircase with two layers: the logical ordering is the spine, while the right-hand annotations show the varying strength of the diagnostic content. This captures the segment's main value without flattening all steps into "exact."

## Findings and watches

- F83 candidate: step 4a treats `delta_s = hat P_Sigma - Phi` as the default operational calibration signal, but `Phi` is the independence-model plan value at true edge parameters. True edge parameters are not directly available to the agent; the segment needs to distinguish the proof target from an empirical/convergence proxy.
- F84 candidate: step 4c's trigger depends on "persistent `delta_s approx 0`" plus persistent negative plan residuals. If `delta_s` is proof-level rather than computable, the trigger needs an observable substitute such as stabilized edge credences plus residual statistics.
- Watch: the cascade's convention hierarchy repeats the C1/C2/C3 monotonicity claim; the earlier C2 receding-horizon monotonicity concern remains active.
- Watch: step 4c inherits the causal-insufficiency detector's joint-observability and sign/model-class caveats. A null covariance test is not evidence of L0 sufficiency unless preconditions hold.
- Watch: the segment's "ordering exact" claim is stronger than the content guarantees. The order is exact as a dependency graph; timing, thresholds, and step-4 diagnostics remain conditional or discussion-grade.

## Local verdict

The cascade is a strong organizing device. It should distinguish exact dependency order from the operational estimators used inside each diagnostic step.
