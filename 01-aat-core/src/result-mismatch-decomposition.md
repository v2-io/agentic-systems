---
slug: result-mismatch-decomposition
type: result
status: exact
depends:
  - def-mismatch-signal
  - def-observation-function
  - def-action-transition
  - form-agent-model
  - scope-adaptive-system
stage: claims-verified
---

# Result: Mismatch Decomposition

The first named *result* of the volume. The expected squared mismatch $\mathbb{E}[\Vert\delta_t\Vert^2]$ decomposes cleanly into two additive parts: a **reducible model-error term** (the difference between the model's predictive mean $\hat o_t$ and the true conditional mean $\bar o_t = \mathbb{E}[o_t \mid \Omega_t, a_{t-1}]$) and an **irreducible observation-noise term** (the conditional variance of the observation channel itself, given environment state and action). The result is the bias-variance decomposition applied to the prediction problem; the cross-term vanishes under the fresh-noise global assumption GA-1 (observation noise conditionally independent of the past chronica given current environment state and action), which is the standard assumption in state-space models. The model can improve the first term; the second is a property of the channel.

The conceptual stakes of this seemingly mechanical decomposition are large. The result establishes that prediction error is *structurally persistent* in any realistic adaptive regime — there is a floor below which mismatch cannot be driven by any amount of better modeling, because that floor is set by the observation channel itself. Deterministic, noiseless, perfectly-specified systems are limiting edge cases, not the typical adaptive regime. The total expected squared mismatch is therefore strictly positive whenever either observation noise is non-degenerate or the model's predictive mean is misspecified — and both typically hold.

The decomposition has direct operational consequences picked up downstream. An agent that tries to eliminate *all* mismatch — including the irreducible noise floor — will overfit, adjusting its model to explain noise and degrading future predictions. The update-gain construct #emp-update-gain implicitly separates signal from noise by weighting observations in proportion to their informativeness, but the irreducible-floor fact is what makes the gain question meaningful at all. The decomposition also clarifies the relationship to #def-model-sufficiency: when $S(M_t) \lt 1$, the model has lost predictive information relative to the full history; under an alignment assumption (the lost information affects the one-step conditional mean) this implies positive model error in the decomposition.

## Formal Expression

*[Derived (result-mismatch-decomposition)]*

For any agent-environment pair within AAT's scope ( #scope-adaptive-system), when observation noise is non-degenerate or the model's predictive mean is misspecified:

$$\mathbb{E}[\Vert\delta_t\Vert^2] = \underbrace{\mathbb{E}[\Vert\hat{o}_t - \bar{o}_t\Vert^2]}_{\text{model error (reducible)}} + \underbrace{\mathbb{E}[\text{Var}(o_t \mid \Omega_t, a_{t-1})]}_{\text{observation noise (irreducible)}} \gt 0$$

where $\bar o_t = \mathbb{E}[o_t \mid \Omega_t, a_{t-1}]$ is the true conditional mean.

### Derivation

1. By #scope-adaptive-system, $H(\Omega_t \mid \mathcal C_t) \gt 0$ — residual uncertainty persists.
2. By #form-agent-model, the model generates predictions $\hat o_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$.
3. Decompose mismatch into model error and noise. The cross-term vanishes by the fresh-noise assumption (GA-1): $\varepsilon_t$ is conditionally independent of $\mathcal C_{t-1}$ given $(\Omega_t, a_{t-1})$. Condition on $(\Omega_t, a_{t-1}, \mathcal C_{t-1})$; then both $\bar o_t$ and $\hat o_t$ are fixed, and $\mathbb{E}[o_t - \bar o_t \mid \Omega_t, a_{t-1}, \mathcal C_{t-1}] = \mathbb{E}[o_t - \bar o_t \mid \Omega_t, a_{t-1}] = 0$ by definition of $\bar o_t$ and GA-1. The outer expectation gives zero. This is orthogonality (uncorrelated), not independence.
4. Term (ii) is positive when observation noise is non-degenerate. Term (i) is positive when the model's predictive mean differs from the true conditional mean. Either suffices.

## Epistemic Status

*Exact* under the fresh-noise assumption (observation noise $\varepsilon_t$ conditionally independent of history given current state and action). This is the standard assumption in state-space models — noise is a property of the observation channel at the moment of observation. The decomposition is a mathematical identity (bias-variance decomposition applied to the prediction problem). The positivity of $\mathbb{E}[\Vert\delta_t\Vert^2]$ follows from either condition; both hold simultaneously in typical settings.

## Discussion

**Reducible vs. irreducible.** An agent that tries to eliminate *all* mismatch — including irreducible noise — will overfit: adjusting its model to explain noise, degrading future predictions. The update gain ( #emp-update-gain) implicitly separates signal from noise by weighting observations in proportion to their informativeness.

**Connection to model sufficiency.** When $S(M_t) \lt 1$ ( #def-model-sufficiency), the model has lost predictive information relative to the full history. Under an alignment assumption (the lost information affects the one-step conditional mean), this implies positive model error (term i). Without that alignment assumption, insufficiency still implies positive regret under proper scoring rules but not necessarily positive one-step mean error.

**Mismatch is structurally persistent.** In realistic AAT regimes, mismatch signals persist — they can be reduced but not eliminated when observation noise is non-degenerate. Deterministic, noiseless, perfectly specified systems are limiting edge cases, not the typical adaptive regime.
