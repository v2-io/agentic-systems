# 29 - result-sector-condition-stability

Segment: `01-aat-core/src/result-sector-condition-stability.md`
Dependencies: `def-adaptive-tempo`, `def-mismatch-signal`, `deriv-sector-condition`, `result-sector-persistence-template` - first two satisfied; proof/template dependencies not yet reached in outline order.
Status observed: `type: result`, `status: exact`, `stage: claims-verified`.

## Reflection

This result makes the persistence theorem structurally clear: mismatch dynamics are `dot(delta) = -F(T,delta)+w`; if the correction function points inward with sector efficiency `alpha`, bounded disturbance produces an ultimate bound `rho/alpha`, and persistence requires that bound to fit inside the valid region `R`. The structural-versus-task distinction from the intro is preserved: this is about keeping mismatch inside the model class region, not necessarily being accurate enough for a task.

Two notation issues matter. First, the prior bridge question remains: this segment says the linear case `F = T delta` gives `alpha = T`, but the gain-bridge grounding is still stated as `alpha = eta*c_min`. Since `T=nu eta`, the event-rate factor is still missing unless `F` or `c_min` is already time-normalized. Second, Model S says `E||w(t)||^2 = sigma_w^2` but then gives RMS `sigma_w sqrt(n/(2alpha))`; that formula matches per-coordinate isotropic diffusion amplitude `sigma_w`, not a total vector second moment equal to `sigma_w^2`.

## Prompt pass

Predictions vs evidence: I expected a sector Lyapunov result and persistence inequality. The segment gives both Model D and Model S forms.

Cross-segment consistency: consistent with mismatch dynamics and the persistence intro. It sharpens the earlier deterministic bounded-disturbance issue by using "ultimately bounded by" rather than exact steady state, which is the better formulation.

Math verification: Model D ultimate bound `rho/alpha` is standard under the sector inequality. Model S scaling is plausible for isotropic OU noise but the disturbance notation must define whether `sigma_w` is scalar per dimension or vector-total.

Direction next: `result-persistence-condition` should state the operational threshold and may reveal whether it uses `alpha`, `T`, or both.

Errors to watch: silently replacing `alpha` with `T` outside the linear/time-normalized case; carrying stochastic RMS formulas with inconsistent noise conventions; treating structural persistence as task adequacy.

What I would change: add a sentence: "Here `alpha` is a continuous-time correction rate; for event-driven gain updates, `alpha = nu eta*c_min` unless `F` has already absorbed event rate." Also define Model S noise as `ddelta = -F dt + sigma_w dW_t` with `sigma_w` per coordinate or as a covariance trace.

Curiosity: this segment rescues the deterministic bounded case from the prior heuristic by using an ultimate bound.

New knowledge enabled: the sector result is the actual persistence core; the linear ODE is just the globally linear special case.

Audit process change: the diagram should show the outer validity region `R`, inner ultimate bound `rho/alpha`, and the separate alpha-normalization warning.

Value feel: high, with two important notation fixes needed.

## Diagram thought

The natural diagram is concentric regions in mismatch space: the model-class validity ball `R`, the ultimate bound ball `rho/alpha`, and inward arrows satisfying the sector condition. A side label should explicitly mark `alpha` as a rate and ask where event frequency enters.
