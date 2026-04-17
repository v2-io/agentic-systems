---
slug: worked-example-bandit
type: worked-example
status: conditional
depends:
  - scope-condition
  - causal-structure
  - agent-model
  - model-sufficiency
  - mismatch-signal
  - update-gain
  - causal-information-yield
  - adaptive-tempo
  - persistence-condition
stage: draft
---

# Worked-example: Worked Example — Nonstationary Bandit (RL Domain)

AAD's conceptual architecture applies beyond the conjugate-Bayesian regime. The mapping here is *approximate* — it shows that AAD's concepts organize RL phenomena, but the quantitative relationships are structural analogies, not derivations. Where the mapping is exact versus approximate is marked explicitly.

## System

A $k$-armed bandit ($k = 4$) with slowly drifting reward means:

*[Formulation]*

$$\mu_i(t+1) = \mu_i(t) + w_i(t), \quad w_i(t) \sim \mathcal{N}(0, q), \quad q = 0.01$$

- Observation: Pulling arm $a_t = i$ yields reward $r_t = \mu_i(t) + \varepsilon_t$, $\varepsilon_t \sim \mathcal{N}(0, \sigma^2)$, $\sigma^2 = 1.0$.
- Event rate: $\nu = 1$ pull per step.
- Agent: Q-learning with fixed learning rate $\alpha$ and UCB action selection.

## Chain Instantiation

### Scope ( #scope-condition)

*Mapping: exact.*

$\Omega_t = (\mu_1(t), \ldots, \mu_4(t))$ — not directly observable. $\mathcal{A} = \{1, 2, 3, 4\}$. Residual uncertainty persists: means drift continuously, rewards are noisy, and only one arm is observed per step.

### Causal Structure ( #causal-structure) + CIY ( #causal-information-yield)

*Mapping: exact for causal ordering; approximate for CIY formula.*

The action (arm choice) temporally precedes the reward observation. Under the Gaussian reward model, CIY for arm $i$:

*[Discussion — Bandit CIY, Gaussian Case]*

$$\text{CIY}(i;\, M_{t-1}) = \frac{1}{2\sigma^2} \mathbb{E}_{j \sim q}\!\left[(\hat{\mu}_i - \hat{\mu}_j)^2\right]$$

This measures how *distinctive* arm $i$'s predicted reward is relative to alternatives — distinctiveness of predictions, not uncertainty about predictions. A proper uncertainty-aware CIY would require maintaining posterior variances per arm, which the basic Q-learning model does not track.

### Model ( #agent-model) and Sufficiency ( #model-sufficiency)

*Mapping: exact structural mapping; the model is deliberately impoverished.*

$$M_t = (\hat{\mu}_1, \ldots, \hat{\mu}_4,\; n_1, \ldots, n_4)$$

Model sufficiency $S(M_t) \lt 1$ for two reasons: (1) No drift tracking — the model treats reward means as stationary. (2) No uncertainty representation — unlike a Bayesian agent that would maintain posterior variances.

### Mismatch ( #mismatch-signal)

*Mapping: exact.*

$$\delta_t = r_t - \hat{\mu}_{a_t}$$

Decomposes exactly: $\mathbb{E}[\delta_t^2] = (\hat{\mu}_{a_t} - \mu_{a_t}(t))^2 + \sigma^2$.

### Update Gain ( #update-gain)

*Mapping: approximate. This is where the bandit agent is most deficient relative to AAD-optimal behavior.*

The Q-learning update

$$\hat{\mu}_{a_t} \leftarrow \hat{\mu}_{a_t} + \alpha \cdot \delta_t$$

uses a **degenerate constant gain**. It does not adapt to the agent's current uncertainty state.

**Optimal gain via effective window.** A fixed $\alpha$ is equivalent to exponential discounting with effective window $W = (1 - \alpha)/\alpha$. The per-arm model uncertainty balances estimation variance and drift-induced bias:

$$U_M \approx \frac{\sigma^2}{W} + q \cdot W$$

The optimal window $W^\ast = \sigma / \sqrt{q} = 10$ gives $\alpha^\ast \approx 0.091$, $U_M \approx 0.2$, and:

$$\eta^* = \frac{U_M}{U_M + U_o} = \frac{0.2}{1.2} \approx 0.167$$

The discrepancy between $\alpha^\ast$ and $\eta^\ast$ arises because $\alpha$ operates on raw prediction errors while $\eta^\ast$ accounts for the full uncertainty structure. The two converge when the model properly tracks its own uncertainty.

### Exploration ( #causal-information-yield)

*Mapping: approximate structural analogy.*

UCB: $a_t = \arg\max_i [\hat{\mu}_i + c\sqrt{\ln t / n_i}]$

| AAD component | UCB analog | Quality |
|---------------|-----------|---------|
| $\mathbb{E}[\text{value}(a) \mid M_t]$ | $\hat{\mu}_i$ | Exact |
| $\lambda(M_t) \cdot \mathbb{E}[\text{CIY}(a)]$ | $c\sqrt{\ln t / n_i}$ | Approximate |

UCB captures the CIY structure (rarely-visited arms are more informative) but depends on visit count, not observation content.

### Tempo + Persistence ( #adaptive-tempo, #persistence-condition)

*Mapping: approximate.*

**Per-arm tempo.** With approximately uniform exploration, each arm sampled at rate $\nu/k = 1/4$:

$$\mathcal{T}_i = \frac{\nu}{k} \cdot \alpha = 0.25 \times 0.091 = 0.023 \;\text{step}^{-1}$$

**Per-arm drift rate:** $\rho_i = \sqrt{q} = 0.1 \;\text{reward units} \cdot \text{step}^{-1}$.

**Persistence check:** $\mathcal T_i = 0.023$ vs $\rho_i = 0.1$ — **fails**. Per-arm correction tempo is too low relative to drift. The agent cannot keep all arms' estimates current under uniform exploration.

**Interpretation.** This is expected and informative. AAD diagnoses exactly why: with 4 arms and one pull per step, each arm is visited too infrequently to track its drifting mean. Two remedies:

1. **Increase $\eta^\ast$** (raise $\alpha$): Extract more per observation, but increase steady-state noise.
2. **Concentrate $\nu$**: Abandon uniform exploration. Focus pulls on a subset, increasing per-arm $\nu/k_{\text{active}}$. This is exactly what a good UCB policy does.

With focused exploration ($k_{\text{active}} = 2$, $\alpha = 0.2$): $\mathcal T_i = 0.5 \times 0.2 = 0.1$ — barely meets the threshold. The fundamental tension: with limited pulls and significant drift, the agent must accept either failing to track some arms or using high $\alpha$ that introduces noise.

**Aggregate failure.** $\mathcal{T} = \nu \cdot \alpha = 0.091$ vs $\rho = k \cdot \sqrt{q} = 0.4$. The agent's total adaptive capacity is outpaced by total environmental drift — a regime where model-based approaches (Bayesian bandits, Kalman bandit filters) with higher effective $\eta^\ast$ have a structural advantage.

## Mapping Quality Summary

| AAD Concept | Bandit Mapping | Status |
|-------------|---------------|--------|
| Scope | Exact | Definitional |
| Causal structure | Exact | Structural |
| CIY | Approximate | Model lacks uncertainty representation |
| Model ($M_t$) | Exact | Definitional |
| Model sufficiency ($S \lt 1$) | Exact | Q-learner demonstrably insufficient |
| Mismatch ($\delta_t$) | Exact | Standard prediction error |
| Gain ($\alpha$ as degenerate $\eta^\ast$) | Approximate | Fixed, does not adapt |
| Exploration (UCB as approximate CIY) | Approximate | Structural analogy |
| Tempo ($\mathcal{T} = (\nu/k) \cdot \alpha$ per arm) | Approximate | Assumes uniform allocation |
| Persistence condition | Exact (qualitative) | Threshold structure is robust |

## Epistemic Status

This is a *structural mapping*, not a derivation. The mapping is *exact* for scope, causal ordering, model compression, and mismatch. It is *approximate* for gain, exploration, and tempo — precisely because the Q-learner does not represent its own uncertainty, which is what #update-gain requires for optimal behavior. The gap between the Q-learner's fixed $\alpha$ and the AAD-optimal adaptive $\eta^\ast$ is precisely the gap between a fixed-gain PID controller and a Kalman filter.

The mapping status is *conditional* because the quantitative relationships depend on the Gaussian reward model and specific parameterization. The qualitative conclusions (persistence failure under uniform exploration, the concentration-vs-noise tradeoff) should be robust.

## Working Notes

- The per-arm analysis is a natural instance of the per-dimension tempo decomposition ( #per-dimension-persistence): each arm is an independent mismatch dimension with its own $\mathcal T_i$ and $\rho_i$. The aggregate tempo overstates effective adaptation along any individual arm's dimension — exactly the failure mode that the scalar-to-tensor generalization captures.
- A Bayesian bandit (maintaining per-arm posteriors with exponential discounting) would achieve higher #model-sufficiency by representing its own uncertainty, yielding an adaptive $\eta^\ast$ that matches the AAD-optimal form. Comparing Q-learner vs Bayesian bandit performance under nonstationarity is a direct test of #update-gain's structural claim.
- Reward-unit and surprise-unit formulations coincide up to normalization by $\sigma^2$. For this example ($\sigma = 1$), they are identical.

*(Descended from TFT Appendix D.)*
