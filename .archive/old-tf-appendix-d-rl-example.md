# Appendix D: Worked Example — Nonstationary Bandit (RL Domain)

**Epistemic status**: This appendix is a structural mapping. TFT maps exactly to Kalman/linear-Gaussian systems ([Appendix C](Appendix-C-Kalman-Example.md)); the mapping here is *approximate* — it shows that TFT's conceptual architecture applies beyond the conjugate-Bayesian regime, but the quantitative relationships are structural analogies, not derivations. Where the mapping is exact versus approximate is marked explicitly.

## Purpose

Appendix C demonstrates TFT end-to-end in a Kalman (linear-Gaussian) domain where every quantity has a closed-form expression. This appendix demonstrates the same chain — TF-01 through TF-11 — in a **non-Kalman, non-Gaussian** domain: a nonstationary multi-armed bandit solved with Q-learning and UCB exploration. The goal is to show that TFT's concepts (mismatch, gain, CIY, tempo, persistence) organize RL phenomena in a useful way, even when the exact uncertainty-ratio optimality of TF-06 does not hold.

## Setup

A $k$-armed bandit ($k = 4$) with slowly drifting reward means. At each step the agent selects one arm and receives a noisy reward.

- **True reward means**: $\mu_i(t)$ for $i \in \{1, \ldots, 4\}$, evolving as independent random walks:

*[Formulation]*
$$\mu_i(t+1) = \mu_i(t) + w_i(t), \quad w_i(t) \sim \mathcal{N}(0, q), \quad q = 0.01$$

- **Observation model**: Pulling arm $a_t = i$ yields reward $r_t = \mu_i(t) + \varepsilon_t$, $\varepsilon_t \sim \mathcal{N}(0, \sigma^2)$, $\sigma^2 = 1.0$.
- **Event rate**: $\nu = 1$ pull per step.
- **Agent**: Q-learning with fixed learning rate $\alpha$ and UCB action selection.

## D.1 TF-01 (Scope)

*Mapping status: exact.*

- **Environment state**: $\Omega_t = (\mu_1(t), \ldots, \mu_4(t))$ --- the vector of true reward means. Not directly observable.
- **Observation space**: $\mathcal{O} = \mathbb{R}$ --- a scalar reward, observed only for the chosen arm.
- **Action space**: $\mathcal{A} = \{1, 2, 3, 4\}$.
- **Residual uncertainty**: $H(\Omega_t \mid \mathcal C_t) \gt 0$ because (a) each arm's mean drifts continuously (process noise $q$), (b) rewards are noisy ($\sigma^2 = 1$), and (c) only one arm is observed per step, leaving three arms entirely unobserved. The system is squarely within $\mathcal S_{\text{TFT}}$.

## D.2 TF-02 (Causal Structure) + TF-08 (CIY)

*Mapping status: exact for causal ordering; approximate for CIY formula.*

The action (arm choice) temporally precedes the reward observation. Selecting arm $i$ generates *interventional* information about arm $i$'s reward distribution that cannot be obtained passively --- the agent must pull to observe.

**CIY in the bandit case.** Using the policy-induced reference distribution (default convention), where $q(\cdot \mid M_{t-1})$ is the agent's current action distribution:

*[Discussion --- Bandit CIY]*
$$\text{CIY}(a = i;\, M_{t-1}) = \mathbb{E}_{j \sim q}\!\left[D_{\mathrm{KL}}\!\left(P(r \mid do(a{=}i), M_{t-1}) \,\Vert\, P(r \mid do(a{=}j), M_{t-1})\right)\right]$$

Under the Gaussian reward model, $P(r \mid do(a{=}i), M_{t-1}) = \mathcal{N}(\hat{\mu}_i, \sigma^2)$, so the KL divergence between arms $i$ and $j$ reduces to:

$$D_{\mathrm{KL}} = \frac{(\hat{\mu}_i - \hat{\mu}_j)^2}{2\sigma^2}$$

Thus CIY for arm $i$ is:

*[Discussion --- Bandit CIY, Gaussian Case]*
$$\text{CIY}(i;\, M_{t-1}) = \frac{1}{2\sigma^2} \mathbb{E}_{j \sim q}\!\left[(\hat{\mu}_i - \hat{\mu}_j)^2\right]$$

This measures how *distinctive* arm $i$'s predicted reward is relative to the alternatives the agent would typically select. An arm with an unusual estimated mean has high CIY --- pulling it is informative because the outcome will look different from what other arms would produce.

**Key observation**: This CIY formula captures distinctiveness of *predictions*, not *uncertainty* about predictions. A proper uncertainty-aware CIY would require maintaining posterior variances per arm, which the basic Q-learning model does not track. This is a consequence of model insufficiency (D.3 below).

## D.3 TF-03 (Model)

*Mapping status: exact structural mapping; the model is deliberately impoverished.*

The Q-learning agent maintains:

*[Formulation]*
$$M_t = (\hat{\mu}_1, \ldots, \hat{\mu}_4,\; n_1, \ldots, n_4)$$

where $\hat{\mu}_i$ is the running estimate of arm $i$'s mean reward and $n_i$ is the visit count. This is a compression $\phi(\mathcal C_t)$ of the interaction history --- a lossy one that retains only per-arm sample means and counts.

**Model sufficiency**: $S(M_t) \lt 1$ for two reasons:

1. **No drift tracking.** The model treats reward means as stationary. It does not represent the random-walk dynamics $\mu_i(t+1) = \mu_i(t) + w_i$, so historical observations are weighted equally regardless of recency. This means the model cannot predict *changes* in reward means.
2. **No uncertainty representation.** Unlike a Bayesian agent that would maintain posterior variances, the Q-learner's $M_t$ has no explicit representation of its own uncertainty $U_M$.

A Bayesian agent maintaining per-arm posteriors $\mathcal{N}(\hat{\mu}_i, \sigma_i^2)$ with exponential discounting would achieve higher $S$.

## D.4 TF-05 (Mismatch)

*Mapping status: exact.*

When the agent pulls arm $a_t$ and receives reward $r_t$:

*[Definition --- Bandit Mismatch]*
$$\delta_t = r_t - \hat{\mu}_{a_t}$$

This is the prediction error for the chosen arm --- the standard TF-05 mismatch signal. It decomposes exactly per Proposition 5.1:

$$\mathbb{E}[\delta_t^2] = \underbrace{(\hat{\mu}_{a_t} - \mu_{a_t}(t))^2}_{\text{model error (reducible)}} + \underbrace{\sigma^2}_{\text{observation noise (irreducible)}}$$

The model error term grows over time for unvisited arms (due to drift $q$) and shrinks after visits (due to updates). The noise term $\sigma^2 = 1$ is a property of the observation channel.

## D.5 TF-06 (Gain)

*Mapping status: approximate. This is where the bandit agent is most deficient relative to TFT-optimal behavior.*

The Q-learning update is:

*[Formulation]*
$$\hat{\mu}_{a_t} \leftarrow \hat{\mu}_{a_t} + \alpha \cdot \delta_t$$

The fixed learning rate $\alpha$ is a **degenerate constant gain** --- the RL analog of a PID controller's fixed gains. It does not adapt to the agent's current uncertainty state. In TFT terms, a fixed $\alpha$ implicitly assumes $U_M / (U_M + U_o)$ is constant over time, which is false whenever the agent's uncertainty changes (as it does after each observation and between observations due to drift).

**TFT-optimal gain via effective window.** A fixed $\alpha$ is equivalent to exponential discounting of past observations with effective window $W = (1 - \alpha)/\alpha$, or equivalently $\alpha = 1/(W + 1)$. Within this exponential-weighting scheme, the per-arm model uncertainty after many visits is approximately:

*[Discussion --- Effective Window Uncertainty]*
$$U_M \approx \frac{\sigma^2}{W} + q \cdot W$$

The first term is estimation variance (decreases with window size); the second is drift-induced bias (increases with window size). The optimal window balances these:

$$W^* = \sigma / \sqrt{q} = 1.0 / \sqrt{0.01} = 10$$

giving:

$$\alpha^* = \frac{1}{W^* + 1} = \frac{1}{11} \approx 0.091$$

At this optimal point, $U_M \approx 2\sigma\sqrt{q} = 0.2$, and the TFT uncertainty ratio gives:

$$\eta^* = \frac{U_M}{U_M + U_o} = \frac{0.2}{0.2 + 1.0} = \frac{1}{6} \approx 0.167$$

**Discrepancy.** The optimal $\alpha^\ast \approx 0.091$ from the window analysis differs from the TFT $\eta^\ast \approx 0.167$ because $\alpha$ operates on raw prediction errors while $\eta^\ast$ accounts for the full uncertainty structure. The two converge when the model properly tracks its own uncertainty. The fixed-$\alpha$ Q-learner is only TFT-optimal in the narrow sense that $\alpha = 1/(W^\ast + 1)$ minimizes steady-state MSE for the right $W^\ast$ matching the drift rate --- but it achieves this optimality *accidentally*, without representing $U_M$ or $U_o$ explicitly.

## D.6 TF-08 (Exploration)

*Mapping status: approximate structural analogy.*

The UCB action-selection rule is:

*[Formulation]*
$$a_t = \arg\max_i \left[\hat{\mu}_i + c\sqrt{\frac{\ln t}{n_i}}\right]$$

Compare this to TFT's unified policy objective (TF-08):

$$\pi^*(M_t) = \arg\max_a \left[\mathbb{E}[\text{value}(a) \mid M_t] + \lambda(M_t) \cdot \mathbb{E}[\text{CIY}(a) \mid M_t]\right]$$

The structural analogy:

| TFT component | UCB analog | Mapping quality |
|---------------|-----------|-----------------|
| $\mathbb{E}[\text{value}(a) \mid M_t]$ | $\hat{\mu}_i$ | Exact |
| $\lambda(M_t) \cdot \mathbb{E}[\text{CIY}(a)]$ | $c\sqrt{\ln t / n_i}$ | Approximate |

The UCB bonus $c\sqrt{\ln t / n_i}$ serves as an approximate $\lambda \cdot \text{CIY}$. When $n_i$ is small, arm $i$ is rarely visited, so pulling it is highly informative (high CIY). As $n_i$ grows, additional pulls become less informative (diminishing CIY). The UCB bonus captures this structure: it is large when $n_i$ is small and decays as $n_i$ increases.

**Limitations of the analogy.** The UCB bonus depends on visit count $n_i$ but not on the *content* of past observations. Two arms with the same $n_i$ get the same bonus regardless of how surprising their past rewards have been. A CIY-informed exploration bonus would additionally account for the information content of future pulls, which depends on the agent's current model uncertainty --- information the Q-learning model does not track (D.3).

## D.7 TF-11 (Tempo + Persistence)

*Mapping status: approximate. The structural claims hold; specific numerical values are illustrative.*

**Per-arm adaptive tempo.** With $k = 4$ arms and approximately uniform exploration, each arm is sampled at average rate $\nu / k = 1/4$ pulls per step. The per-arm gain is $\eta^\ast \approx \alpha$. So the per-arm correction tempo is:

*[Discussion --- Per-Arm Tempo]*
$$\mathcal{T}_i = \frac{\nu}{k} \cdot \alpha = \frac{1}{4} \cdot \alpha$$

With $\alpha = 0.091$ (the optimal value from D.5):

$$\mathcal{T}_i = 0.25 \times 0.091 = 0.023 \; \text{step}^{-1}$$

**Environment drift rate.** Each arm's mean drifts with variance $q = 0.01$ per step. In this example, mismatch is measured in **reward units** (not surprise units), which is a simplification — the reward-unit and surprise-unit formulations coincide up to normalization by observation noise $\sigma^2$ (see TF-05, "Bridge from physical to surprise units"). In reward units, the per-arm drift rate is $\sqrt{q}$ (standard deviation of the random walk increment per step):

*[Discussion — Per-Arm Drift Rate]*
$$\rho_i = \sqrt{q} = 0.1 \; \text{reward units} \cdot \text{step}^{-1}$$

In surprise-equivalent (Mahalanobis) units, this would be $\rho_i^{\text{surprise}} = \sqrt{q}/\sigma = 0.1$, which happens to equal the reward-unit value because $\sigma = 1$ in this example. For systems where $\sigma \neq 1$, the normalization matters.

**Persistence condition.** Per-arm persistence requires $\mathcal T_i \gt \rho_i / \Vert\delta_{\text{critical}}\Vert$. Taking $\Vert\delta_{\text{critical}}\Vert = 1$ (mismatch of one standard deviation of reward noise as the functional threshold, consistent with the reward-unit convention):

$$\mathcal{T}_i = 0.023 \quad \text{vs.} \quad \rho_i = 0.1$$

This *fails* the persistence condition: $0.023 \lt 0.1$. The per-arm correction tempo is too low relative to the drift rate. The agent cannot keep all arms' estimates current under uniform exploration.

**Interpretation.** This is expected and informative. A nonstationary 4-armed bandit with this parameterization is a *hard* problem for a Q-learner with uniform exploration. The persistence failure diagnoses exactly why: with 4 arms and one pull per step, each arm is visited too infrequently to track its drifting mean. TFT prescribes two remedies:

1. **Increase $\eta^\ast$** (raise $\alpha$): Use a larger learning rate to extract more information per observation. But this increases steady-state noise (overfitting to observation noise).
2. **Concentrate $\nu$**: Abandon uniform exploration. Focus pulls on a subset of arms, increasing per-arm $\nu/k_{\text{active}}$ above the persistence threshold. This is exactly what a good UCB policy does --- it does not explore uniformly but concentrates visits on promising or uncertain arms, effectively reducing $k_{\text{active}}$.

**With focused exploration** ($k_{\text{active}} = 2$ arms receiving most visits):

$$\mathcal{T}_i = \frac{\nu}{k_{\text{active}}} \cdot \alpha = \frac{1}{2} \times 0.091 = 0.046$$

Still below $\rho_i = 0.1$. Raising $\alpha$ to $0.2$ (shorter window $W = 4$, accepting more noise):

$$\mathcal{T}_i = 0.5 \times 0.2 = 0.1$$

This barely meets the threshold. The TFT framework reveals the fundamental tension: with limited pulls and significant drift, the agent must accept either (a) failing to track some arms (letting their estimates go stale) or (b) using a high $\alpha$ that introduces noise.

**Aggregate tempo.** The system-level tempo (across all arms) is:

$$\mathcal{T} = \nu \cdot \alpha = 1 \times 0.091 = 0.091$$

The aggregate drift rate is $\rho = k \cdot \sqrt{q} = 4 \times 0.1 = 0.4$. Aggregate persistence ($\mathcal{T} \gt \rho$) also fails: $0.091 \lt 0.4$. The agent's total adaptive capacity is fundamentally outpaced by the total environmental drift across all arms. This is a regime where model-based approaches (Bayesian bandits, Kalman bandit filters) with their higher effective $\eta^\ast$ have a structural advantage, consistent with TF-06's observation that advanced RL methods converge toward the TFT-optimal gain form.

## Summary: Mapping Quality

| TFT Concept | Bandit Mapping | Status |
|-------------|---------------|--------|
| Scope ($\Omega_t$, $\mathcal{A}$, residual uncertainty) | Exact | Definitional |
| Causal structure (action precedes observation) | Exact | Structural |
| CIY (informative actions) | Approximate | Model lacks uncertainty representation |
| Model ($M_t$ as compressed history) | Exact | Definitional |
| Model sufficiency ($S \lt 1$) | Exact | Q-learner demonstrably insufficient |
| Mismatch ($\delta_t = r_t - \hat{\mu}_{a_t}$) | Exact | Standard prediction error |
| Gain ($\alpha$ as degenerate $\eta^\ast$) | Approximate | Fixed $\alpha$ does not adapt to uncertainty |
| Exploration (UCB as approximate CIY) | Approximate | Structural analogy; not derived from CIY |
| Tempo ($\mathcal{T} = (\nu/k) \cdot \alpha$ per arm) | Approximate | Assumes uniform allocation |
| Persistence condition | Exact (qualitative) | Threshold structure is robust (Appendix A) |

The nonstationary bandit demonstrates that TFT's conceptual chain applies outside the Kalman regime, but also reveals where the exact quantitative results break down: the uncertainty ratio principle (TF-06) requires the model to represent its own uncertainty, which the Q-learner does not. The gap between the Q-learner's fixed $\alpha$ and the TFT-optimal adaptive $\eta^\ast$ is precisely the gap between a degenerate constant gain and the full uncertainty-ratio form --- the same gap that separates a fixed-gain PID controller from a Kalman filter.

**Note on tensor tempo (TF-11 Open Question #4).** The per-arm analysis in C.7 is a natural instance of the per-dimension tempo decomposition: each arm is an independent mismatch dimension with its own $\mathcal T_i$ and $\rho_i$. The persistence condition must hold per-dimension ($\mathcal T_i \gt \rho_i$), not merely in aggregate. The aggregate tempo $\mathcal{T} = \nu \cdot \alpha$ overstates the agent's effective adaptation along any individual arm's dimension --- exactly the failure mode that the scalar-to-tensor generalization is designed to capture.
