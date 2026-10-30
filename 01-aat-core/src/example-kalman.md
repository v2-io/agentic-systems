---
slug: example-kalman
type: worked-example
status: exact
depends:
  - scope-adaptive-system
  - post-causal-structure
  - form-agent-model
  - def-mismatch-signal
  - emp-update-gain
  - def-causal-information-yield
  - der-deliberation-cost
  - result-structural-adaptation-necessity
  - def-adaptive-tempo
  - result-persistence-condition
  - result-sector-condition-stability
  - der-gain-sector-bridge
stage: draft
---

# Worked Example: 1D Active Tracking (Kalman Domain)

Every AAT quantity has an exact Kalman-filter counterpart. This is a *validation* of the formal chain — all quantities are computable in closed form.

This is AAT's **calibration on a problem with known exact answers**. AAT's contribution in the Kalman instance is not adding new results to Kalman theory; it is *embedding Kalman in a more general framework that handles the same primitives across non-linear, non-Gaussian, and non-fully-observable agent classes*, with the Kalman case as the special case where everything reduces to closed-form. The mismatch is the innovation; the optimal gain coincides with the Kalman gain (the uncertainty-ratio formula equals the Kalman gain in the linear-Gaussian case); the sector parameter equals tempo via #der-gain-sector-bridge; the persistence condition reduces to observability plus detectability. Where AAT predicts what Kalman theory says, the framework is minimally correct; where AAT predicts beyond Kalman scope (non-linear, non-Gaussian, partial observability, multi-agent), the framework's reach extends past Kalman's. The Kalman instance is the anchor point that grounds the abstract machinery in a familiar concrete case.

## System

The agent tracks scalar state $x_t$ and chooses sensor mode $a_t \in \{L, H\}$:

- Dynamics: $x_{t+1} = x_t + v_t$, $v_t \sim \mathcal{N}(0, q)$, $q = 0.25$
- Observation: $y_t = x_t + n_t^{(a_t)}$
- Low mode noise: $r_L = 9$; High mode noise: $r_H = 1$
- Event rate: $\nu = 5 \text{ Hz}$
- High mode has higher energy cost

## Chain Instantiation

### Scope ( #scope-adaptive-system)

*Mapping: exact.*

$\Omega_t = x_t$ is partially observed via a noisy channel, and the law ($q$, $r_L$, $r_H$, the random-walk form) is known, so the typed target is $S_t = x_t$: uncertainty of the state type. Because the state is a random walk, what is seen later still bears on it, so the future stream carries positive information about $x_t$ at every $t$ under either sensor mode (item (b) of #scope-adaptive-system with $A = C = 1$). The posterior variance converges to a positive steady state, so the warrant is standing. $\mathcal{A} = \{L, H\}$ is non-empty and causally affects observation quality.

### Causal Structure ( #post-causal-structure) + CIY ( #def-causal-information-yield)

*Mapping: exact.*

Action precedes observation and changes $P(y_t \mid do(a_t))$ through $r_{a_t}$. Using low mode as comparator action, the CIY is the interventional KL divergence:

*[Worked Quantity]*

$$\text{CIY}(H) = D_{\mathrm{KL}}\!\big(P(y \mid do(H)) \,\Vert\, P(y \mid do(L))\big)$$

$$= \frac{1}{2}\left[\log\!\left(\frac{P^- + r_L}{P^- + r_H}\right) + \frac{P^- + r_H}{P^- + r_L} - 1\right]$$

With $P^- = 4.25$: $\text{CIY}(H) \approx 0.161 \text{ nats}$.

### Model ( #form-agent-model)

*Mapping: exact.*

Model state $M_t = (\hat x_{t\vert t}, P_{t\vert t})$ — a compression of interaction history with recursive update.

### Mismatch ( #def-mismatch-signal)

*Mapping: exact.*

The mismatch signal is the Kalman innovation:

$$\delta_t = y_t - \hat{x}_{t\vert t-1}$$

The estimation error is $e_t = x_t - \hat x_{t\vert t-1}$, and the innovation is the estimation error plus the channel noise, $\delta_t = e_t + n_t^{(a_t)}$, so $\mathbb{E}[\delta_t^2] = P^-_t + r_{a_t}$. The agent sees $\delta_t$ and never sees $e_t$. The persistence bounds below are about $e_t$.

### Update Gain ( #emp-update-gain)

*Mapping: exact.*

Scalar Kalman gain:

$$K_t = \frac{P^-_t}{P^-_t + r_{a_t}}$$

With $P^- = 4.25$: $K(H) \approx 0.810$, $K(L) \approx 0.321$.

The exact uncertainty ratio mapping: $U_M = P^-_t$, $U_o = r_{a_t}$, $\eta^\ast = K_t$.

### Exploration ( #def-causal-information-yield)

*[Worked Objective]*

$$a_t^* = \arg\max_a \left[\mathbb{E}[\text{value}(a)\mid M_t] + \lambda_t \, \mathbb{E}[\text{CIY}(a)\mid M_t]\right]$$

When uncertainty is high ($P^-$ large), CIY term favors high mode. As uncertainty falls, policy shifts toward low-cost $L$.

### Deliberation Threshold ( #der-deliberation-cost)

Suppose a planning pause of $\Delta\tau = 0.5 \text{ s}$, with measured $\rho_{\text{delib}} = 0.40 \;\text{surprise/s}$.

Cost during pause: $0.20$ surprise units. If $\Vert\delta_{\text{post}}\Vert = 0.70$, deliberation is worthwhile when:

$$\Delta\eta^*(0.5)\cdot 0.70 \gt 0.20 \;\Longrightarrow\; \Delta\eta^*(0.5) \gt 0.286$$

### Structural Adaptation ( #result-structural-adaptation-necessity)

Assume maneuvering regime change introduces sustained residual autocorrelation and mismatch floor. If estimated valid radius drops to $R = 0.08$ while $R^\ast = \rho/\alpha = 0.12$, parametric adaptation is no longer adequate ($R^\ast \gt R$), triggering model-class change (e.g., constant-velocity → constant-acceleration process model).

### Tempo + Persistence ( #def-adaptive-tempo, #result-persistence-condition)

Using action mix $70\% H, 30\% L$:

$$\bar{\eta}^* = 0.7(0.810) + 0.3(0.321) = 0.663$$

$$\mathcal{T} = \nu \bar{\eta}^* = 5 \cdot 0.663 = 3.315 \;\text{s}^{-1}$$

This system's disturbance is stochastic (a random walk observed through Gaussian noise), so the persistence question is the Model S one, worked in closed form below rather than through the Model D ratio $\rho/\mathcal{T}$.

### Lyapunov Bounds ( #result-sector-condition-stability, #der-gain-sector-bridge)

*Mapping: exact (derived, not estimated).*

By #der-gain-sector-bridge, the correction of the estimation error is exactly linear, $F(e) = Ke$, so the sector parameter is $\alpha = K$ per observation and $\alpha = \nu \bar K = \mathcal{T}$ in continuous time ($3.315\ \text{s}^{-1}$ for the mix above). The disturbance on $e$ has two parts: the random walk adds variance $q$ per step, and the update feeds in the share $K^2 r$ of the channel noise ( #deriv-sector-condition, Setup). Per step $e_{t+1} = (1 - K_t)e_t - K_t n_t + v_t$.

*Steady state, high mode throughout ($r = r_H = 1$).* The Riccati equation gives $P^- = 0.640$, $K_{ss} = 0.390$, $P = 0.390$:

| Object | RMS |
|---|---|
| Estimation error after update, $\sqrt{P}$ | $0.62$ |
| Estimation error before update, $\sqrt{P^-}$ | $0.80$ |
| Innovation, $\sqrt{P^- + r_H}$ | $1.28$ |

*The lag/noise trade-off, in one line.* For a gain $K$ held fixed, the prior error variance is

$$V(K) = \frac{q + K^2 r}{1 - (1 - K)^2}$$

At $K = 0.39$ (the Kalman gain) it is $0.640$. At $K = 0.81$, a gain held at its early transient value, it is $0.940$. At $K = 0.15$ it is $0.982$. The error is smallest at the Kalman gain: a larger gain removes lag faster and injects more channel noise.

*Task adequacy.* With $\Vert\delta_{\text{critical}}\Vert = 1$ read on the estimation error, the agent is adequate ($0.62 \lt 1$ after update, $0.80$ before). Read on the innovation, the condition could never hold, since the innovation's RMS is at least $\sqrt{r_H} = 1$ whatever the gain. That is the distinction #def-mismatch-signal draws.

*The region of validity.* With model-class capacity $R = 1.4$ (a domain parameter), the prior error is Gaussian with standard deviation $0.80$, so at any given time it lies outside $\mathcal B_R$ with probability $0.08$. Under Model S the region is a typical scale, not a wall ( #deriv-sector-condition, Prop A.1S and Corollary A.1S.1).

## Mapping Quality Summary

| AAT Concept | Kalman Mapping | Status |
|-------------|---------------|--------|
| Scope | Exact | Definitional |
| Causal structure + CIY | Exact | Closed-form KL |
| Model ($M_t$ as sufficient statistic) | Exact | Kalman state + covariance |
| Mismatch ($\delta_t$ = innovation; estimation error $e_t$) | Exact | Standard Kalman innovation; $\delta_t = e_t + n_t$ |
| Gain ($\eta^\ast = K_t$) | Exact | Kalman gain IS uncertainty ratio |
| Tempo ($\mathcal{T} = \nu \bar{\eta}^\ast$) | Exact | Closed-form |
| Persistence condition | Exact | Model S, closed form on the estimation error |
| Sector parameter ($\alpha = \mathcal{T}$) | Exact | Derived from Kalman gain via #der-gain-sector-bridge |
| Lyapunov bounds | Exact | Steady-state error variance from the Riccati equation; minimized at the Kalman gain |

## Epistemic Status

This is a *worked instantiation*, not a theoretical claim. Every mapping is exact — the Kalman domain is the canonical case where AAT's formal chain has closed-form realizations. The example validates that the formal chain is internally consistent and instantiable.

## Working Notes

- This example uses a 1D system. The tensor-tempo extension ( #result-per-dimension-persistence) becomes visible only in multi-dimensional tracking where different state dimensions have different observability.
- The structural adaptation trigger (constant-velocity → constant-acceleration) is manufactured for the example. A more natural test would be a real tracking system with genuine regime changes.
- The Kalman filter is provably optimal for the linear-Gaussian case. Every AAT quantity has not just an analog but the *exact optimal* value. This makes it the strongest validation but also the easiest — the real test is non-Kalman domains (see #example-bandit).
