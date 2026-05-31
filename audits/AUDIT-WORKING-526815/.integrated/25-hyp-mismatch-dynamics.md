# 25 - hyp-mismatch-dynamics

Segment: `01-aat-core/src/hyp-mismatch-dynamics.md`
Dependencies: `def-adaptive-tempo`, `def-mismatch-signal`, `deriv-sector-condition` - first two satisfied; `deriv-sector-condition` not yet reached in outline order.
Status observed: `type: hypothesis`, `status: heuristic`, `stage: deps-verified`.

## Reflection

This hypothesis confirms that tempo is being used as a correction-rate coefficient in a first-order mismatch ODE. That makes the previous tempo wording clearer: operationally, `T` is the rate at which mismatch is corrected, not necessarily bits of information per second. The segment is appropriately marked heuristic and explicitly defers nonlinear guarantees to the sector-condition framework.

The main mathematical caveat is the deterministic disturbance steady state. The segment labels Model D as deterministic bounded disturbance `||w(t)|| <= rho`, then sets the derivative to zero and writes `||delta||_ss = rho/T`. For arbitrary bounded time-varying disturbance, this is an ultimate bound or worst-case/constant-aligned disturbance equilibrium, not an exact steady state. The stochastic OU result is more precisely scoped and the `1/sqrt(T)` distinction is useful.

## Prompt pass

Predictions vs evidence: I expected `d delta/dt = -T delta + rho` and the persistence threshold preview. The segment gives deterministic, stochastic, and transient cases plus the discrete-to-continuous bridge.

Cross-segment consistency: consistent with `def-adaptive-tempo` if tempo is correction rate. It depends on a later sector derivation, so the local linear hypothesis is doing preview work until that proof is reached.

Math verification: the constant-disturbance scalar ODE solution is correct. The stochastic scalar OU RMS formula `sigma_w/sqrt(2T)` is correct. For bounded nonconstant disturbances, equality should be replaced by `limsup ||delta|| <= rho/T` under the linear stable system.

Direction next: this chapter likely has a checkpoint after mismatch dynamics; if not, the next segment should start the persistence/stability formal results and test whether it carries these Model D/S distinctions forward.

Errors to watch: treating deterministic upper bounds as exact steady states; using scalar norm dynamics where vector direction and anisotropic tensor tempo matter; squared adversarial law depending on coupling-dominant and deterministic-drift assumptions.

What I would change: state Model D as "constant or worst-case bounded disturbance" for equality, and use an ultimate-bound inequality for general bounded disturbances.

Curiosity: the discrete-to-continuous bridge is strong if the cited derivation holds; I will need to check whether `eta*c_max << 1` is carried into downstream continuous claims.

New knowledge enabled: deterministic drift and stochastic noise lead to different persistence scaling: `1/T` versus `1/sqrt(T)`.

Audit process change: the diagram should be a balance with two output laws, not a single threshold picture.

Value feel: high as a heuristic map; exactness depends on later sector/discrete derivations.

## Diagram thought

A compact diagram can show mismatch as a reservoir: disturbance fills it at rate `rho`, tempo drains it proportionally to current mismatch. Two side panels should show the different steady-state scaling for bounded drift and stochastic noise, because that difference is the segment's most useful refinement.
