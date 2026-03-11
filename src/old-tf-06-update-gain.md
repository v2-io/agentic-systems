# TF-06: The Update Gain (Derived + Empirical Claim)

The model incorporates mismatch signals through an **update gain** that determines how much each observation shifts the model — the *epistrophe* phase of the adaptive loop (TF-00), in which the model turns toward reality. The optimal gain balances model uncertainty against observation uncertainty.

## The Update Rule

In its general additive form:

*[Formulation]*
$$M_t = M_{t-1} + \eta(M_{t-1}) \cdot g(\delta_t)$$

where:
- $\eta$: the **update gain** — a scalar, vector, or matrix determining how much to adjust. The gain depends on the model state (specifically on $U_M$) but typically not on the current observation $o_t$ — it is computed *before* the observation arrives. (Exception: in some non-Gaussian or quasi-Newton methods, the gain may additionally depend on $o_t$; in such cases write $\eta(M_{t-1}, o_t)$.)
- $g$: the **mismatch transform** — a function mapping raw mismatch to the appropriate update direction. Its domain and codomain depend on which mismatch definition is in use (TF-05): for prediction errors $\delta_t \in \mathcal{O}$, $g: \mathcal{O} \to T_M\mathcal{M}$ maps from observation space to the model's tangent space; for score-function mismatches $\tilde{\delta}_t \in T_M\mathcal{M}$, $g: T_M\mathcal{M} \to T_M\mathcal{M}$ is an operator on the tangent space (e.g., the inverse Fisher information matrix for natural gradients, or the identity for vanilla gradient descent). In the linear case (Kalman), $g$ is the observation-to-state mapping $H^T$.

**Representation note.** The additive form is stated in a *representation space* appropriate to the model. For models whose native update is multiplicative — most notably Bayesian posteriors, where $P(\theta \mid D) \propto P(D \mid \theta) P(\theta)$ — the additive rule operates in a transformed space (e.g., log-probability or natural parameter space) where multiplication becomes addition. Similarly, models on constrained manifolds (probability simplices, rotation groups) require the update to be projected or retracted onto the manifold. The claim is not that all updates are literally additive in the model's native parameterization, but that they have the structural form "current state + gain × transformed mismatch" in an appropriate coordinate system. The Kalman and conjugate-Bayesian cases are exactly additive in their natural coordinates; neural network gradient descent is additive in weight space; the general case requires identifying the correct representation layer.

In the event-driven formulation (TF-04), this becomes channel-specific:

*[Formulation]*
$$M_{\tau^+} = M_{\tau^-} + \eta^{(k)}(M_{\tau^-}) \cdot g^{(k)}(\delta^{(k)}_\tau)$$

## Uncertainty Definitions

*[Definition (model-uncertainty)]*
$$U_M = \text{Var}_{M_{t-1}}[\hat{o}_t \mid a_{t-1}]$$

**Model uncertainty** ($U_M$): the variance (or appropriate dispersion measure) of the model's predictive distribution over the observed quantity. In the Kalman case, $U_M = P_{t|t-1}$ (prior predictive variance); in conjugate Bayesian models, $U_M$ is the posterior predictive variance; in ensemble methods, $U_M = \text{Var}_i[\hat{o}_t^{(i)}]$ across ensemble members. The definition is precise for linear-Gaussian systems (where variance fully characterizes uncertainty) and approximate for non-Gaussian systems (where variance captures second-moment uncertainty but not distributional shape). For non-parametric models, $U_M$ must be approximated — see Open Question #1.

*[Definition (observation-uncertainty)]*
$$U_o = \text{Var}[\varepsilon_t]$$

**Observation uncertainty** ($U_o$): the variance (or dispersion) of the observation noise $\varepsilon_t$ under the TF-01 observation model. In multi-channel systems (TF-04), each channel has its own $U_o^{(k)}$. When $h$ is action-dependent (TF-01), $U_o$ may vary with $a_{t-1}$ — this is exactly the sensor-selection scenario where different actions yield different observation quality.

## The Optimal Gain

**Claim** (Empirical — validated exactly in some domains, approximately in others):

The optimal update gain has the structural form:

*[Empirical Claim (uncertainty-ratio)]*
$$\eta^* = \frac{U_M}{U_M + U_o}$$

**Scope of claim.** The claim is that the *structural form* — a ratio of uncertainties — is universal. The scalar expression above is the simplest instantiation, exact when uncertainties are well-defined scalars (Kalman, conjugate Bayesian). For systems where $U_M$ is not naturally a scalar (neural networks, non-parametric models), the principle generalizes: the optimal gain is higher when the model is more uncertain relative to the observation, lower otherwise. The specific functional form may be a matrix (Kalman gain), per-parameter adaptive step size (Adam), or approximated heuristically. When $\eta^*$ is used as a scalar in the mismatch dynamics (TF-11, Appendix A), it represents the effective scalar projection along the mismatch direction — see TF-00, "Scalar reduction of gain and tempo." See Open Questions for the non-parametric case.

### Interpretation

- When $U_M \gg U_o$ (model is uncertain, observations reliable): $\eta^* \to 1$. Trust the observation; shift the model substantially.
- When $U_M \ll U_o$ (model is confident, observations noisy): $\eta^* \to 0$. Trust the model; discount the observation.
- When $U_M \approx U_o$: $\eta^* \approx 0.5$. Weight model and observation equally.

This is the **uncertainty ratio principle**: new information should be weighted in proportion to the relative reliability of the source versus the existing model.

## Domain Validation

### Kalman filter[^kalman1960] *(exact)*

*[Domain Instantiation — Exact]*
$$K_t = P_{t|t-1} H^T (H P_{t|t-1} H^T + R)^{-1}$$

In the scalar case: $K_t = \frac{p_{t|t-1}}{p_{t|t-1} + r}$ where $p$ is state variance (model uncertainty) and $r$ is measurement noise variance (observation uncertainty). This is exactly $\frac{U_M}{U_M + U_o}$. The matrix form is the natural generalization to multiple dimensions.

**Status: Exact instantiation.** ✓

### Bayesian posterior *(exact in conjugate families)*

For an exponential family with conjugate prior[^bernardo1994] of effective sample size $\kappa$ (prior strength), after observing $n$ data points:

*[Domain Instantiation — Exact (Conjugate Families)]*
$$\theta_{\text{posterior}} = \frac{n}{n + \kappa} \cdot \bar{\theta}_{\text{data}} + \frac{\kappa}{n + \kappa} \cdot \theta_{\text{prior}}$$

The *cumulative* weight on all data vs. the prior, $\frac{n}{n+\kappa}$, increases as data accumulates. But the *incremental* weight of one new datum — the analog of the per-step gain $\eta^*$ — is $\frac{1}{n+\kappa}$, which *decreases* as data accumulates. This is consistent with the gain dynamics below: as the model becomes more certain ($U_M$ shrinks), each new observation shifts the posterior less. The Bayesian case validates both the structural form (uncertainty ratio) and the convergence dynamics ($\eta^* \to 0$).

**Status: Exact instantiation** (for conjugate families). ✓

### Reinforcement learning *(approximate)*

Standard TD update: $Q(s,a) \leftarrow Q(s,a) + \alpha[\delta_t]$

The fixed learning rate $\alpha$ is a **degenerate gain** — not adapted to uncertainty. This is a known limitation. Methods that approximate the optimal gain:
- **Bayesian RL**: maintains posterior over $Q$; update weight adapts to uncertainty
- **UCB / Thompson sampling**: exploration bonus proportional to uncertainty
- **Adaptive optimizers** (Adam, RMSProp): approximate second-order information to adapt step sizes per-parameter

The fixed-$\alpha$ case can be understood as a *constant approximation* of the optimal gain — effective when the uncertainty ratio is roughly stable, suboptimal when it varies.

**Status: Approximate instantiation.** The structure holds; basic RL uses a degenerate form; advanced methods converge toward the optimal form. ✓

### PID control *(loose mapping)*

PID gains $(K_p, K_i, K_d)$ are typically fixed at design time. Auto-tuning methods (Ziegler-Nichols, relay feedback) estimate plant characteristics to set gains — effectively estimating the uncertainty ratio once at calibration. Adaptive PID and Model Predictive Control (MPC) adjust gains online, moving toward the full adaptive framework.

**Status: Simplified instantiation.** PID fixes $\eta$ at design time; MPC is the richer control-theoretic instantiation. ✓

## Gain Dynamics

The optimal gain changes over time following predictable patterns:

**Convergence**: As the model accumulates information, $U_M$ decreases, so $\eta^* \to 0$. The model becomes increasingly resistant to individual observations. This IS:
- Kalman filter convergence ($P_t \to$ steady state $\Rightarrow K_t \to$ steady state)
- Bayesian posterior concentration
- RL learning rate annealing

**Reset after structural change**: When the environment changes in ways the model cannot track incrementally ($\mathcal{M}$ is wrong; see TF-10), $U_M$ should spike — the model "admits" its uncertainty. The gain increases, enabling rapid re-learning. This is:
- Kalman filter with adaptive process noise
- Bayesian changepoint detection
- RL with learned learning rates

An agent whose gain does NOT reset after structural change will continue trusting a stale model — the analog of Boyd's "incestuous amplification" and the cause of brittle failure in non-stationary environments.

## Overfitting as Gain Miscalibration

From TF-05's decomposition:

*[Derived (from TF-05)]*
$$\mathbb{E}[\|\delta_t\|^2] = \text{model error}^2 + \text{irreducible noise}^2$$

An agent with $\eta$ too high will adjust its model to explain observation noise, increasing model error on future predictions. An agent with $\eta$ too low will fail to correct genuine model errors.

The optimal gain implicitly separates signal from noise by weighting observations in proportion to their informativeness — exactly what $U_M/(U_M + U_o)$ achieves when $U_o$ includes the irreducible noise.

## Connection to Causal Information Yield

The gain determines how much the agent learns from each observation. But not all observations are equally informative — observations that are causally downstream of the agent's actions carry interventional information (CIY, TF-08) that action-independent observations do not. When the agent acts and then observes, the mismatch signal $\delta_t$ conditioned on the agent's action $a_{t-1}$ is an *interventional* signal. The optimal gain for such signals should, in principle, give more weight to high-CIY observations (those that reveal causal structure) than to low-CIY observations (those that reveal only correlations). The current formulation captures this implicitly — higher CIY typically manifests as higher $U_M$ along the causal dimensions — but making the connection explicit is deferred to the unified policy objective (TF-08). Note that CIY is well-defined and estimable when the agent generates interventional data through action variation (Regime A in TF-08's admissibility framework); under observational data only (Regime B), the CIY-gain connection requires additional causal assumptions.

## Overall Assessment

The uncertainty ratio principle is the theory's strongest cross-domain bridge after the mismatch signal itself. It is exact for Kalman filters and conjugate Bayesian models, structurally correct for RL and adaptive control, and conceptually applicable to organizational and biological adaptation. Confidence that the *structural form* (ratio of uncertainties) is universal: ~75%. Confidence that the *scalar* expression is more than a useful approximation in high-dimensional / non-parametric settings: ~40%. The principle is most powerful as a design criterion (your gain should approximate this ratio) and a diagnostic tool (if your gain doesn't, you're either over- or under-correcting).

**Simulation validation.** Numerical experiments (ACT Track B, Variant E) empirically validated the uncertainty ratio principle under observation noise. In a discrete-time tracking task with stochastic process noise and varying observation noise levels, the Riccati-optimal gain ($\eta^* = U_M / (U_M + U_o)$) reduced steady-state mismatch by 52% compared to a fixed gain when observation noise was moderate ($\sigma_{\text{obs}} = 0.5 \times q_{\text{env}}$). The optimal gain also proved critical in the adversarial setting: under heavy observation noise, the optimal gain preserved more than double the adversarial tempo advantage exponent (0.40 vs. 0.18) compared to a fixed gain. The empirical minimum of the gain-vs-mismatch curve matched the Riccati prediction across the full noise sweep, confirming that the uncertainty ratio form is not merely a design heuristic but the quantitatively correct gain schedule for this class of problems.

## Open Questions

1. **Non-parametric models**: For neural networks and other models without a well-defined scalar "model uncertainty," how should $U_M$ be computed? Ensemble methods, dropout-based uncertainty, and Bayesian neural networks are all approximations. Is there a principled general definition? (*Confidence this can be resolved: ~50%*)

2. **Matrix vs. scalar gain**: In high-dimensional systems, the gain is a matrix (Kalman) or per-parameter (Adam[^kingma2015]), not a scalar. The uncertainty ratio principle holds per-dimension, but the cross-dimensional structure (covariance) adds complexity. Is the scalar formulation a useful simplification or does it lose essential structure? (*The scalar captures the principle; the matrix captures the full optimization. Both are valid at their level of description.*)

---

[^kalman1960]: Kalman, R. E. (1960). "A new approach to linear filtering and prediction problems." *J. Basic Engineering (ASME)*, 82(1), 35–45.
[^bernardo1994]: Bernardo, J. M. & Smith, A. F. M. (1994). *Bayesian Theory*. Wiley.
[^kingma2015]: Kingma, D. P. & Ba, J. (2015). "Adam: A Method for Stochastic Optimization." *Proc. ICLR*.
[^amari1998]: Amari, S. (1998). "Natural gradient works efficiently in learning." *Neural Computation*, 10(2), 251–276.
