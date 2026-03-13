---
slug: adversarial-tempo-advantage
type: result
status: exact
depends:
  - mismatch-dynamics
  - adversarial-destabilization
  - persistence-condition
---

# Result: Adversarial Tempo Advantage

Under adversarial coupling where one agent's actions contribute to the other's disturbance rate, the steady-state mismatch ratio scales superlinearly with the tempo ratio.

## Formal Expression

*[Derived (adversarial-tempo-advantage, from mismatch-dynamics steady state and adversarial-destabilization coupling model)]*

**Setup.** Two agents $A$ and $B$ with adaptive tempos $\mathcal T_A$ and $\mathcal T_B$, coupled via the same model as #adversarial-destabilization:

$$\rho_A = \rho_{\text{base}} + \gamma_B \cdot \mathcal{T}_B, \qquad \rho_B = \rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A$$

where $\gamma_A, \gamma_B \gt 0$ are the coupling effectivenesses and $\rho_{\text{base}}$ is the background disturbance rate (taken equal for both agents for clarity; the asymmetric case is a straightforward generalization).

**Steady-state mismatch ratio.** From the linear mismatch dynamics ( #mismatch-dynamics), $\Vert\delta\Vert_{ss} = \rho / \mathcal{T}$. Substituting the coupled disturbance rates:

$$\Vert\delta_A\Vert_{ss} = \frac{\rho_{\text{base}} + \gamma_B \cdot \mathcal{T}_B}{\mathcal{T}_A}, \qquad \Vert\delta_B\Vert_{ss} = \frac{\rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A}{\mathcal{T}_B}$$

Taking the ratio:

$$\frac{\Vert\delta_B\Vert_{ss}}{\Vert\delta_A\Vert_{ss}} = \frac{\rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A}{\mathcal{T}_B} \cdot \frac{\mathcal{T}_A}{\rho_{\text{base}} + \gamma_B \cdot \mathcal{T}_B}$$

*[Result (adversarial-tempo-advantage)]*

$$\frac{\Vert\delta_B\Vert_{ss}}{\Vert\delta_A\Vert_{ss}} = \frac{(\rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A) \cdot \mathcal{T}_A}{(\rho_{\text{base}} + \gamma_B \cdot \mathcal{T}_B) \cdot \mathcal{T}_B}$$

### Coupling-Dominant Limit

In the coupling-dominant regime ($\gamma_A \cdot \mathcal T_A \gg \rho_{\text{base}}$ and $\gamma_B \cdot \mathcal T_B \gg \rho_{\text{base}}$), the base disturbance becomes negligible:

$$\frac{\Vert\delta_B\Vert_{ss}}{\Vert\delta_A\Vert_{ss}} \to \frac{\gamma_A \cdot \mathcal{T}_A^2}{\gamma_B \cdot \mathcal{T}_B^2} = \frac{\gamma_A}{\gamma_B} \cdot \left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^2$$

For symmetric coupling ($\gamma_A = \gamma_B$):

$$\frac{\Vert\delta_B\Vert_{ss}}{\Vert\delta_A\Vert_{ss}} \to \left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^2$$

The exponent is $b = 2$: a **squared** tempo advantage. A 2:1 tempo ratio yields a 4:1 mismatch ratio, not 2:1.

### Derivation

From #mismatch-dynamics, the steady-state condition $d\Vert\delta\Vert/dt = 0$ gives $\Vert\delta\Vert_{ss} = \rho / \mathcal{T}$.

1. Substitute the coupling model into $B$'s steady state: $\Vert\delta_B\Vert_{ss} = (\rho_{\text{base}} + \gamma_A \cdot \mathcal T_A) / \mathcal T_B$.

2. Substitute the coupling model into $A$'s steady state: $\Vert\delta_A\Vert_{ss} = (\rho_{\text{base}} + \gamma_B \cdot \mathcal T_B) / \mathcal T_A$.

3. Form the ratio:

$$\frac{\Vert\delta_B\Vert_{ss}}{\Vert\delta_A\Vert_{ss}} = \frac{(\rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A) / \mathcal{T}_B}{(\rho_{\text{base}} + \gamma_B \cdot \mathcal{T}_B) / \mathcal{T}_A} = \frac{(\rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A) \cdot \mathcal{T}_A}{(\rho_{\text{base}} + \gamma_B \cdot \mathcal{T}_B) \cdot \mathcal{T}_B}$$

4. In the coupling-dominant limit, $\rho_{\text{base}} \to 0$ relative to $\gamma \cdot \mathcal{T}$:

$$\frac{\Vert\delta_B\Vert_{ss}}{\Vert\delta_A\Vert_{ss}} \to \frac{\gamma_A \cdot \mathcal{T}_A \cdot \mathcal{T}_A}{\gamma_B \cdot \mathcal{T}_B \cdot \mathcal{T}_B} = \frac{\gamma_A}{\gamma_B} \cdot \left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^2$$

$\square$

### Regime-Dependent Exponents

The squared law ($b = 2$) holds under deterministic drift coupling and coupling-dominant conditions. The exponent varies by regime:

| Regime | Coupling type | Dominance | Exponent $b$ |
|:---|:---|:---|:---:|
| 1 | Deterministic drift | Coupling-dominant | $2$ |
| 2 | Stochastic noise | Coupling-dominant | $3/2$ |
| 3 | Either | Non-coupling-dominant | $\to 1$ (det.) or $\to 1/2$ (stoch.) |

**Regime 2 (stochastic).** When the adversarial coupling enters as zero-mean noise rather than persistent drift, the steady-state RMS mismatch scales as $\rho / \sqrt{\mathcal{T}}$ (because the stationary variance of the AR(1) process scales as $\rho^2 / \mathcal{T}$, and absolute deviation scales as the square root of variance). Substituting into the ratio yields $b = 3/2$ in the coupling-dominant limit.

**Regime 3 (non-coupling-dominant).** When $\rho_{\text{base}} \gtrsim \gamma \cdot \mathcal{T}$, the base disturbance dominates and the coupling terms become a perturbation. The mismatch ratio degrades toward $\mathcal T_A / \mathcal T_B$ (linear, $b = 1$) for deterministic dynamics, or toward $(\mathcal T_A / \mathcal T_B)^{1/2}$ for stochastic.

The simulation validation across all three regimes is in #adversarial-exponent-regimes.

## Epistemic Status

The squared law ($b = 2$) is *exact* under the linear mismatch dynamics ( #mismatch-dynamics) and the deterministic coupling-dominant conditions. The derivation is straightforward algebra from the steady-state formula and the coupling model. The coupling model itself is an *assumption* — the same one used in #adversarial-destabilization.

The regime-dependent exponents ($b = 3/2$ stochastic, $b \to 1$ non-coupling-dominant) are *empirical* — confirmed by simulation ( #adversarial-exponent-regimes, with the deterministic case matching at $b = 1.999$) and consistent with the analytical scaling arguments, but the stochastic case is not yet derived from the stochastic mismatch dynamics in full generality. The transition between regimes is smooth, not sharp.

Max attainable: exact conditional on the mismatch dynamics and coupling model. The result is as strong as its assumptions; no additional work changes the epistemic status without changing the dynamical model.

## Discussion

**Superlinearity is the key result.** The naive expectation — twice as fast yields twice the advantage — is wrong under adversarial coupling. The mechanism is that the faster agent both (a) corrects its own mismatch faster and (b) generates disturbance for the opponent faster. These two effects multiply, producing the squared exponent. Speed advantage is not additive; it compounds.

**Relationship to #adversarial-destabilization.** The steady-state mismatch ratio quantifies how much worse the slower agent does *while both agents persist*. The destabilization threshold ( #adversarial-destabilization) marks where the slower agent fails entirely — its correction mechanism breaks down. Below the threshold, this segment's mismatch ratio applies. Above it, #adversarial-destabilization's Lyapunov divergence takes over. The two results are complementary: this one gives the score; that one gives the game-ending condition.

**Regime dependence is operationally significant.** Whether an adversary's tempo increase produces systematic drift (positional maneuvering, API changes, doctrinal initiative) or unpredictable noise (feints, randomized attacks, market volatility) determines the scaling law. The distinction is not academic — $b = 2$ vs. $b = 3/2$ means a 3:1 tempo ratio yields 9:1 vs. 5.2:1 mismatch ratio. The model predicts that consistent, directional pressure is more effective per unit of tempo than unpredictable disruption.

**Formal analog of OODA-loop observations.** The squared scaling is consistent with Boyd's observation that getting inside the opponent's decision cycle has disproportionate effects. The theory identifies a specific mechanism (multiplicative interaction of correction speed and disturbance generation) and a specific condition (coupling-dominant regime) under which this disproportionality holds. Whether this mechanism is the dominant one in actual adversarial interactions is an empirical question, not a mathematical one.

## Working Notes

- The analysis treats each agent's tempo as exogenous — $\mathcal T_A$ does not change in response to $B$'s actions and vice versa. A fully coupled analysis where both agents' mismatch states co-evolve simultaneously (joint Lyapunov function over $(\delta_A, \delta_B)$) is the open extension. The decoupled result is a worst-case bound for the slower agent: in practice, the faster agent may divert adaptive capacity to generating disturbance rather than correcting its own mismatch, creating a self-limiting effect.
- The stochastic exponent ($b = 3/2$) is derived from the AR(1) stationary variance scaling, which is exact for the discrete process. The continuous-time analog (Ornstein-Uhlenbeck) gives the same scaling. A full derivation from the stochastic mismatch SDE would unify Regimes 1 and 2 under a single framework with drift and diffusion terms.
- Asymmetric coupling ($\gamma_A \neq \gamma_B$) appears as a multiplicative prefactor $\gamma_A / \gamma_B$ that shifts the mismatch ratio without changing the exponent. An agent with lower tempo but higher coupling effectiveness ($\gamma$) can partially compensate — but the squared dependence on tempo dominates for large tempo ratios.

*(Descended from TFT Corollary 11.2.)*
