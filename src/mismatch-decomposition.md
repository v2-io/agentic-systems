---
slug: mismatch-decomposition
type: result
status: exact
depends:
  - mismatch-signal
  - observation-function
  - agent-model
---

# Result: Mismatch Decomposition

Expected squared mismatch decomposes into reducible model error and irreducible observation noise. The model can improve the first term; the second is a property of the channel.

## Formal Expression

*[Derived (mismatch-decomposition, Prop 5.1 from TFT)]*

For any agent-environment pair within ACT's scope ( #scope-condition), when observation noise is non-degenerate or the model's predictive mean is misspecified:

$$\mathbb{E}[\Vert\delta_t\Vert^2] = \underbrace{\mathbb{E}[\Vert\hat{o}_t - \bar{o}_t\Vert^2]}_{\text{model error (reducible)}} + \underbrace{\mathbb{E}[\text{Var}(o_t \mid \Omega_t, a_{t-1})]}_{\text{observation noise (irreducible)}} \gt 0$$

where $\bar o_t = \mathbb{E}[o_t \mid \Omega_t, a_{t-1}]$ is the true conditional mean.

### Derivation

1. By #scope-condition, $H(\Omega_t \mid \mathcal C_t) \gt 0$ — residual uncertainty persists.
2. By #agent-model, the model generates predictions $\hat o_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$.
3. Decompose mismatch into model error and noise. The cross-term vanishes by the fresh-noise assumption: $\varepsilon_t$ is conditionally independent of $\mathcal C_{t-1}$ given $(\Omega_t, a_{t-1})$. Condition on $(\Omega_t, a_{t-1})$; then $\bar o_t - \hat o_t$ is fixed and $\mathbb{E}[o_t - \bar o_t \mid \Omega_t, a_{t-1}] = 0$ by definition of $\bar o_t$. The outer expectation gives zero. This is orthogonality (uncorrelated), not independence.
4. Term (ii) is positive when observation noise is non-degenerate. Term (i) is positive when the model's predictive mean differs from the true conditional mean. Either suffices.

## Epistemic Status

*Exact* under the fresh-noise assumption (observation noise $\varepsilon_t$ conditionally independent of history given current state and action). This is the standard assumption in state-space models — noise is a property of the observation channel at the moment of observation. The decomposition is a mathematical identity (bias-variance decomposition applied to the prediction problem). The positivity of $\mathbb{E}[\Vert\delta_t\Vert^2]$ follows from either condition; both hold simultaneously in typical settings.

## Discussion

**Reducible vs. irreducible.** An agent that tries to eliminate *all* mismatch — including irreducible noise — will overfit: adjusting its model to explain noise, degrading future predictions. The update gain ( #update-gain) implicitly separates signal from noise by weighting observations in proportion to their informativeness.

**Connection to model sufficiency.** When $S(M_t) \lt 1$ ( #model-sufficiency), the model has lost predictive information relative to the full history. Under an alignment assumption (the lost information affects the one-step conditional mean), this implies positive model error (term i). Without that alignment assumption, insufficiency still implies positive regret under proper scoring rules but not necessarily positive one-step mean error.

**Mismatch is structurally persistent.** In realistic ACT regimes, mismatch signals persist — they can be reduced but not eliminated when observation noise is non-degenerate. Deterministic, noiseless, perfectly specified systems are limiting edge cases, not the typical adaptive regime.
