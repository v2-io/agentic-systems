---
slug: emp-update-gain
type: empirical
status: robust-qualitative
depends:
  - def-mismatch-signal
  - def-observation-function
stage: claims-verified
---

# Empirical: Update Gain

The optimal weight an agent assigns to new observations when updating its model — the rate of *epistrophe* (turning toward reality). How much the agent should trust the incoming observation versus its own prior understanding.

## Formal Expression

*[Empirical Claim (uncertainty-ratio-principle)]*

$$\eta^* = \frac{U_M}{U_M + U_o}$$

where:
- $\eta^\ast$ is the optimal update gain (proportion of mismatch used to correct the model)
- $U_M$ is model uncertainty (predictive variance or entropy)
- $U_o$ is irreducible observation noise

The update rule takes the form:

*[Formulation]*

$$M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$$

where $\delta_t$ is the mismatch ( #def-mismatch-signal) and $g(\cdot)$ is a correction mapping from observation space to model update space.

## Epistemic Status

*Derived* under the **Fisher-local invariance regime** ( #deriv-fisher-local-update-gain): for any smooth log-likelihood admitting non-degenerate local quadratic expansion, the natural-gradient Bayesian posterior mean shift at first order in the step size is exactly $\Delta\theta = K \cdot \tilde\nabla$ with gain operator $K = (H_M + H_L)^{-1} H_L$ and scalar collapse $\eta^\ast = U_M/(U_M + U_o)$ along the natural-gradient direction (always in 1-D; under (PI)/Čencov in higher dimensions). Linear-Gaussian (Kalman) and conjugate-Bayesian instances are cases where the local quadratic expansion is *globally* exact, so the form holds without truncation. For general smooth models, the natural-gradient invariance theorem of Amari 1998 guarantees the form is exact at the local-tangent-plane Pythagorean projection level.

Outside the Fisher-local regime — non-quadratic losses, non-conjugate priors, structurally non-Gaussian uncertainty (heavy tails, multimodality) — the dependence is *robust qualitative*: the **direction** is preserved (gain rises with model uncertainty, falls with observation noise) and the first-order form is recovered locally; what need not hold is global quantitative fidelity. The qualitative direction is the load-bearing claim for downstream tempo and persistence machinery; the Fisher-local exact form is the load-bearing claim for the Kalman, conjugate, and natural-gradient instantiations.

## Discussion

**Limiting behavior.** When $U_M \gg U_o$ (high model uncertainty — e.g., after initialization or structural adaptation), $\eta^\ast \to 1$: trust the observation. When $U_M \ll U_o$ (confident model, noisy channel), $\eta^\ast \to 0$: trust the model. The gain determines how strongly the agent corrects toward reality on each update.

**Resolving Epistemic Opacity.** The optimal gain equation requires the agent to know $U_o$, which seems to violate the epistemic opacity axiom established in `#def-observation-function` (the agent does not know the true noise distribution $\varepsilon_t$). This tension is resolved dynamically: the agent *estimates* $U_o$ (and $U_M$) from the observable statistics of its own mismatch sequence (innovations), treating the gain itself as an endogenous state variable. See `#deriv-adaptive-gain-dynamics` for the proof of how this meta-adaptation maintains Lyapunov stability without violating opacity.

**Gain collapse — epistrophe failure.** When the agent incorrectly estimates $U_M \to 0$ (spurious confidence) or $U_o \to \infty$ (spurious distrust of sensors), $\eta^\ast \to 0$ and epistrophe ceases. Aporia still arrives — the mismatch signal is still generated — but the agent no longer turns toward it. Mismatches are ignored, producing confirmation bias or a decoupled reality model. The cycle runs but the corrective phase is hollow.

**Multi-dimensional generalization.** In vector-valued systems, $U_M$ and $U_o$ are covariance matrices and $\eta^\ast$ becomes a gain matrix (as in the Kalman filter). The scalar form captures the essential structure.

**Connection to adaptive tempo.** The update gain is one factor in the agent's adaptive tempo ( #def-adaptive-tempo): $\mathcal{T} = \nu \cdot \eta^\ast$. Frequent aisthesis (high $\nu$) is useless if epistrophe extracts no information (low $\eta^\ast$). Gain measures the *quality* of the cycle's corrective phase; event rate measures its *speed*.

**Gain dynamics.** The optimal gain changes over time following predictable patterns:

- *Convergence*: As the model accumulates information, $U_M$ decreases, so $\eta^\ast \to 0$. The model becomes increasingly resistant to individual observations. This IS Kalman filter convergence, Bayesian posterior concentration, and RL learning rate annealing.
- *Reset after structural change*: When the environment changes in ways the model cannot track incrementally ( #result-structural-adaptation-necessity), $U_M$ should spike — the model "admits" its uncertainty. The gain increases, enabling rapid re-learning. An agent whose gain does NOT reset after structural change will continue trusting a stale model — Boyd's "incestuous amplification" and the cause of brittle failure in non-stationary environments.

**Overfitting as gain miscalibration.** From #result-mismatch-decomposition: $\mathbb{E}[\Vert\delta_t\Vert^2]$ = model error + irreducible noise. An agent with $\eta$ too high adjusts its model to explain observation noise, increasing model error on future predictions. An agent with $\eta$ too low fails to correct genuine model errors. The optimal gain implicitly separates signal from noise by weighting observations in proportion to their informativeness — exactly what $U_M/(U_M + U_o)$ achieves when $U_o$ captures the irreducible noise.

**Representation note.** The additive form operates in a *representation space* appropriate to the model. For Bayesian posteriors (where update is multiplicative: $P(\theta \mid D) \propto P(D \mid \theta) P(\theta)$), the additive rule operates in log-probability or natural parameter space. For models on constrained manifolds (probability simplices, rotation groups), the update must be projected onto the manifold. The claim is not that all updates are literally additive in native parameterization, but that they have the structure "current state + gain × transformed mismatch" in an appropriate coordinate system.

**Domain validation:**

| Domain | Gain form | Mapping quality |
|--------|-----------|-----------------|
| Kalman filter | $K_t = P_{t\Vertt-1} H^T (H P_{t\Vertt-1} H^T + R)^{-1}$ | **Exact.** Scalar case is exactly $U_M/(U_M + U_o)$. |
| Conjugate Bayesian | Posterior weight $n/(n + \kappa)$ cumulative; incremental $1/(n + \kappa)$ | **Exact** for conjugate families. Incremental gain decreases as data accumulates. |
| RL (Q-learning) | Fixed learning rate $\alpha$ | **Approximate.** $\alpha$ is a degenerate constant gain — does not adapt to uncertainty. Advanced methods (Bayesian RL, Adam) converge toward the optimal form. |
| PID control | Fixed gains $(K_p, K_i, K_d)$ | **Simplified.** Gains set at design time. Adaptive PID and MPC move toward the full framework. |
| Software developer | Implicit trust weighting of information sources | **Structural analogy.** New developer (high $U_M$) trusts observations heavily; experienced developer (low $U_M$) trusts their model. Gain reset after major refactoring. |

**Simulation validation.** Numerical experiments (track-b, Variant E) validated the uncertainty ratio principle under observation noise. Riccati-optimal gain reduced steady-state mismatch by 52% compared to fixed gain when observation noise was moderate. The optimal gain also proved critical in adversarial settings: under heavy observation noise, optimal gain preserved more than double the adversarial tempo advantage exponent (0.40 vs 0.18) compared to fixed gain.

**Open questions:**

1. *Non-parametric models*: For neural networks without well-defined scalar $U_M$, how should it be computed? Ensemble methods, dropout-based uncertainty, and Bayesian neural networks are all approximations.
2. *Matrix vs scalar gain*: In high-dimensional systems, the gain is a matrix (Kalman) or per-parameter (Adam). The cross-dimensional structure (covariance) adds complexity. The scalar captures the principle; the matrix captures the full optimization.