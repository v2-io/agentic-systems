---
slug: result-adversarial-tempo-advantage
type: result
status: conditional
depends:
  - hyp-mismatch-dynamics
  - der-adversarial-destabilization
  - result-persistence-condition
stage: draft
---

# Result: Adversarial Tempo Advantage

Under adversarial coupling where one agent's actions contribute to the other's disturbance rate, the steady-state mismatch ratio scales superlinearly with the tempo ratio.

## Formal Expression

*[Derived (adversarial-tempo-advantage, from sector-persistence-template + adversarial-destabilization coupling model)]*

**Setup.** Two agents $A, B$ with adaptive tempos $\mathcal T_A, \mathcal T_B$, each instantiating #result-sector-persistence-template with linear correction ($\alpha = \mathcal{T}$). The adversarial coupling of #der-adversarial-destabilization enters each agent's effective disturbance:

$$\rho_A^{\text{eff}} = \rho_{\text{base}} + \gamma_B \cdot \mathcal{T}_B, \qquad \rho_B^{\text{eff}} = \rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A$$

with $\gamma_A, \gamma_B \gt 0$ coupling effectivenesses and $\rho_{\text{base}}$ the shared background rate (asymmetric $\rho_{\text{base}}$ generalizes straightforwardly).

### Model D: Deterministic coupling, $b = 2$

*[Result (adversarial-tempo-advantage, Model D)]*

The template's Model D conclusion $\lVert\delta\rVert_{ss} = \rho^{\text{eff}}/\mathcal{T}$ (linear case, $\alpha = \mathcal{T}$) applied to both agents and ratioed:

$$\frac{\lVert\delta_B\rVert_{ss}}{\lVert\delta_A\rVert_{ss}} = \frac{(\rho_{\text{base}} + \gamma_A \mathcal{T}_A)\,\mathcal{T}_A}{(\rho_{\text{base}} + \gamma_B \mathcal{T}_B)\,\mathcal{T}_B}$$

In the coupling-dominant limit ($\gamma \mathcal{T} \gg \rho_{\text{base}}$) with symmetric coupling ($\gamma_A = \gamma_B$):

$$\frac{\lVert\delta_B\rVert_{ss}}{\lVert\delta_A\rVert_{ss}} \to \left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^2$$

The exponent is $b = 2$: a **squared** tempo advantage. A 2:1 tempo ratio yields a 4:1 mismatch ratio. The faster agent both (a) corrects its own mismatch faster and (b) generates disturbance for the opponent faster — the two effects compound rather than add. $\square$

### Model S: Stochastic coupling, $b = 3/2$

*[Derived (stochastic-tempo-advantage, from sector-persistence-template Model S + coupling)]*

Under Model S the coupling enters the noise scale: $\sigma_B^{\text{eff}} = \sigma_{\text{base}} + \gamma_A \mathcal T_A$. Adversary tempo increases unpredictability, not systematic direction. The template's Model S steady state $\lVert\delta\rVert_{\text{rms}} = \sigma/\sqrt{2\mathcal{T}}$ (linear $\alpha = \mathcal{T}$, scalar $n = 1$) applied to both agents:

$$\frac{\lVert\delta_B\rVert_{\text{rms}}}{\lVert\delta_A\rVert_{\text{rms}}} = \frac{(\sigma_{\text{base}} + \gamma_A \mathcal{T}_A)\sqrt{\mathcal{T}_A}}{(\sigma_{\text{base}} + \gamma_B \mathcal{T}_B)\sqrt{\mathcal{T}_B}}$$

In the coupling-dominant, symmetric limit:

$$\frac{\lVert\delta_B\rVert_{\text{rms}}}{\lVert\delta_A\rVert_{\text{rms}}} \to \left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^{3/2}$$

The exponent is $b = 3/2$. $\square$

**Why 3/2, not 2.** The half-power difference between the template's Model D ($1/\alpha$) and Model S ($1/\sqrt{\alpha}$) scalings propagates through the ratio. Numerator contributes $\mathcal T_A^1$ from the coupling; denominator contributes $\mathcal T_B^{1/2}$ from noise averaging; combined with the $A$-side $1/\mathcal T_A^{1/2}$ gives $\mathcal T_A^{3/2}/\mathcal T_B^{3/2}$.

### Summary of Regime-Dependent Exponents

| Regime | Coupling type | Dominance | Exponent $b$ | Source |
|:---|:---|:---|:---:|:---|
| 1 | Deterministic drift (Model D) | Coupling-dominant | $2$ | Derived above |
| 2 | Stochastic noise (Model S) | Coupling-dominant | $3/2$ | Derived above |
| 3 | Either | Non-coupling-dominant | $\to 1$ (det.) or $\to 1/2$ (stoch.) | Asymptotic limit |

**Regime 3 (non-coupling-dominant).** When $\rho_{\text{base}} \gtrsim \gamma \cdot \mathcal{T}$ (or $\sigma_{\text{base}} \gtrsim \gamma \cdot \mathcal{T}$), the base disturbance dominates and the coupling terms become a perturbation. The mismatch ratio degrades toward $\mathcal T_A / \mathcal T_B$ (linear, $b = 1$) for Model D, or toward $(\mathcal T_A / \mathcal T_B)^{1/2}$ for Model S.

The simulation validation across all three regimes is in #result-adversarial-exponent-regimes.

## Epistemic Status

Both coupling-dominant exponents are *exact* conditional on their respective disturbance models. The squared law ($b = 2$) is *exact* under Model D (deterministic bounded disturbance, GA-2) with coupling-dominant conditions. The $3/2$ law ($b = 3/2$) is *exact* under Model S (stochastic disturbance, GA-2S) with coupling-dominant conditions, derived from the $1/\sqrt{\alpha}$ steady-state scaling (Prop A.1S in #deriv-sector-condition). Both derivations are straightforward algebra from the respective steady-state formulas and the coupling model. The coupling model itself is an *assumption* — the same one used in #der-adversarial-destabilization.

The non-coupling-dominant limits ($b \to 1$ for Model D, $b \to 1/2$ for Model S) are derived asymptotically. The smooth transition between regimes is confirmed by simulation ( #result-adversarial-exponent-regimes) but the interpolation formula is empirical. The transition between regimes is smooth, not sharp.

Max attainable: exact conditional on the disturbance model and coupling model. The result is as strong as its assumptions; no additional work changes the epistemic status without changing the dynamical model.

## Discussion

**Superlinearity is the key result.** The naive expectation — twice as fast yields twice the advantage — is wrong under adversarial coupling. The mechanism is that the faster agent both (a) corrects its own mismatch faster and (b) generates disturbance for the opponent faster. These two effects multiply, producing the squared exponent. Speed advantage is not additive; it compounds.

**Relationship to #der-adversarial-destabilization.** The steady-state mismatch ratio quantifies how much worse the slower agent does *while both agents persist*. The destabilization threshold ( #der-adversarial-destabilization) marks where the slower agent fails entirely — its correction mechanism breaks down. Below the threshold, this segment's mismatch ratio applies. Above it, #der-adversarial-destabilization's Lyapunov divergence takes over. The two results are complementary: this one gives the score; that one gives the game-ending condition.

**Regime dependence is operationally significant.** Whether an adversary's tempo increase produces systematic drift (positional maneuvering, API changes, doctrinal initiative) or unpredictable noise (feints, randomized attacks, market volatility) determines the scaling law. The distinction is not academic — $b = 2$ vs. $b = 3/2$ means a 3:1 tempo ratio yields 9:1 vs. 5.2:1 mismatch ratio. The model predicts that consistent, directional pressure is more effective per unit of tempo than unpredictable disruption.

**Formal analog of OODA-loop observations.** The squared scaling is consistent with Boyd's observation that getting inside the opponent's decision cycle has disproportionate effects. The theory identifies a specific mechanism (multiplicative interaction of correction speed and disturbance generation) and a specific condition (coupling-dominant regime) under which this disproportionality holds. Whether this mechanism is the dominant one in actual adversarial interactions is an empirical question, not a mathematical one.

## Working Notes

- **Channel-independence assumption.** The tempo ratio $\mathcal T_A / \mathcal T_B$ uses scalar tempo, which inherits the channel-independence assumption from #def-adaptive-tempo. When either agent's observation channels are correlated, the additive formula overcounts their tempo, inflating or deflating the ratio and the derived mismatch advantage. The superlinear exponents ($b = 2$, $b = 3/2$) are exact given the scalar tempos; the caveat concerns whether the scalar tempos themselves are accurate.
- The analysis treats each agent's tempo as exogenous — $\mathcal T_A$ does not change in response to $B$'s actions and vice versa. A fully coupled analysis where both agents' mismatch states co-evolve simultaneously (joint Lyapunov function over $(\delta_A, \delta_B)$) is the open extension. The decoupled result is a worst-case bound for the slower agent: in practice, the faster agent may divert adaptive capacity to generating disturbance rather than correcting its own mismatch, creating a self-limiting effect.
- The stochastic exponent ($b = 3/2$) is now derived from both the AR(1) stationary variance (discrete) and the Itô-Lyapunov analysis (continuous, Prop A.1S). The continuous-time analog (Ornstein-Uhlenbeck) gives the same scaling, confirming the asymptotic-scaling claim is the fluid-limit value. The 0.019 gap between the simulation $b = 1.481$ and the asymptotic $b = 3/2$ is *not pure numerical noise*: it is consistent with a derivable finite-$\nu$ correction factor (proportional to $\sqrt{(2c_{\min} - \eta^\ast_A c_{\max}^2)/(2c_{\min} - \eta^\ast_B c_{\max}^2)}$ when $\eta^\ast_A \gt \eta^\ast_B$) that arises because the discrete steady-state variance carries the $O(\eta^\ast c_{\max}^2/c_{\min}^2) = O(c_{\max}^2/(c_{\min}^2 \nu))$ gap from #deriv-discrete-sector-condition. In the fluid limit ($\nu \to \infty$, $\eta^\ast \to 0$ at fixed $\mathcal T$), the correction factor approaches 1 and the asymptotic $b = 3/2$ is recovered exactly. The two models (D and S) are unified by the common sector-condition framework with different disturbance assumptions (GA-2 vs. GA-2S).
- Asymmetric coupling ($\gamma_A \neq \gamma_B$) appears as a multiplicative prefactor $\gamma_A / \gamma_B$ that shifts the mismatch ratio without changing the exponent. An agent with lower tempo but higher coupling effectiveness ($\gamma$) can partially compensate — but the squared dependence on tempo dominates for large tempo ratios.
