# 82 - result-unity-closure-mapping

Source: `01-aat-core/src/result-unity-closure-mapping.md`

## First-pass understanding

This segment is the proof home for the claim that unity dimensions do not directly predict closure defect as a point value; they parametrize a rate-distortion surface. The strongest contribution is the two-axis structure: content unity and update-rule homogeneity both affect how aggressively sub-agent state can be compressed without closure error.

The linear-Gaussian examples are helpful, especially the heterogeneous-gain Kalman case. But the result inherits metric issues from `def-unity-dimensions`, and some statements need tighter boundary conditions around projection invariance, perfect correlation, and scope-route handling.

## Diagram attempt

I drew the result as a surface where projection dimension, content unity, and structural unity jointly determine achievable closure defect. The diagram marks two guards: metric normalization from the previous segment and exactness conditions for the linear-Gaussian cases.

## Findings and watches

- F151 candidate: the segment opens by conditioning on `scope-composite-agent` via four routes including C-iv, but the Working Notes say scope is satisfied via "three disjunctive routes" and exclude the strategic-equilibrium route. This repeats the C-iv typing drift and should be made consistent.
- F152 candidate: the result inherits F146: if `U_M` is not normalized into `[0,1]`, the claimed monotone rate-distortion surface in `U_M` has an unstable axis. Fixing `U_M` is prerequisite to using these formulas quantitatively.
- F153 soft candidate: the observation-closure closed form `epsilon_o^2 = sigma_o^2(1-rho)/2` depends on the error norm convention. Under the standard orthonormal plus/minus projection, discarded residual variance is `sigma_o^2(1-rho)`; the extra `/2` is a per-coordinate or averaging convention that should be stated.
- F154 candidate: the state-closure section first states `epsilon_x=0` for linear-Gaussian micro-dynamics with consistent projections, then clarifies exactness requires the projection range to be invariant under the dynamics matrix. The invariance condition is not optional; "consistent projections" alone do not imply zero state closure.
- F155 soft candidate: the two-axis section says `Delta K != 0` gives `epsilon_x > 0` even at perfect content correlation. In degenerate perfect-correlation cases the residual bracket can vanish depending on observation/noise structure. The claim should be scoped to nondegenerate correlated-but-not-collapsed cases or state the positivity conditions for `S_- - C_{+-}^2/S_+`.
- F156 soft candidate: monotonicity in `U_f` is only as good as the still-open operator-distance definition of `U_f`. For arbitrary update rules, the structural axis is currently a worked-example insight, not a general metric theorem.
- Watch: the representability-versus-optimality distinction is again well stated and should remain central.

## Local verdict

The rate-distortion framing is the right conceptual model. The exact claims should be narrowed to their linear-Gaussian/norm/invariance conditions, and the inherited unity metrics need repair before the general surface can be used as quantitative machinery.
