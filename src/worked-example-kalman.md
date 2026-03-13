---
slug: worked-example-kalman
type: worked-example
status: exact
depends:
  - scope-condition
  - causal-structure
  - agent-model
  - mismatch-signal
  - update-gain
  - causal-information-yield
  - deliberation-cost
  - structural-adaptation-necessity
  - adaptive-tempo
  - persistence-condition
  - sector-condition-stability
---

# Worked-example: Worked Example — 1D Active Tracking (Kalman Domain)

Every ACT quantity has an exact Kalman-filter counterpart. This is a *validation* of the formal chain — all quantities are computable in closed form.

## System

The agent tracks scalar state $x_t$ and chooses sensor mode $a_t \in \{L, H\}$:

- Dynamics: $x_{t+1} = x_t + v_t$, $v_t \sim \mathcal{N}(0, q)$, $q = 0.25$
- Observation: $y_t = x_t + n_t^{(a_t)}$
- Low mode noise: $r_L = 9$; High mode noise: $r_H = 1$
- Event rate: $\nu = 5 \text{ Hz}$
- High mode has higher energy cost

## Chain Instantiation

### Scope ( #scope-condition)

*Mapping: exact.*

$\Omega_t = x_t$ is partially observed via noisy channel. $\mathcal{A} = \{L, H\}$ is non-empty and causally affects observation quality. Residual uncertainty persists due to process and sensor noise.

### Causal Structure ( #causal-structure) + CIY ( #causal-information-yield)

*Mapping: exact.*

Action precedes observation and changes $P(y_t \mid do(a_t))$ through $r_{a_t}$. Using low mode as comparator action, the CIY is the interventional KL divergence:

*[Worked Quantity]*

$$\text{CIY}(H) = D_{\mathrm{KL}}\!\big(P(y \mid do(H)) \,\Vert\, P(y \mid do(L))\big)$$

$$= \frac{1}{2}\left[\log\!\left(\frac{P^- + r_L}{P^- + r_H}\right) + \frac{P^- + r_H}{P^- + r_L} - 1\right]$$

With $P^- = 4.25$: $\text{CIY}(H) \approx 0.161 \text{ nats}$.

### Model ( #agent-model)

*Mapping: exact.*

Model state $M_t = (\hat{x}_{t|t}, P_{t|t})$ — a compression of interaction history with recursive update.

### Mismatch ( #mismatch-signal)

*Mapping: exact.*

$$\delta_t = y_t - \hat{x}_{t|t-1}$$

### Update Gain ( #update-gain)

*Mapping: exact.*

Scalar Kalman gain:

$$K_t = \frac{P^-_t}{P^-_t + r_{a_t}}$$

With $P^- = 4.25$: $K(H) \approx 0.810$, $K(L) \approx 0.321$.

The exact uncertainty ratio mapping: $U_M = P^-_t$, $U_o = r_{a_t}$, $\eta^\ast = K_t$.

### Exploration ( #causal-information-yield)

*[Worked Objective]*

$$a_t^* = \arg\max_a \left[\mathbb{E}[\text{value}(a)\mid M_t] + \lambda_t \, \mathbb{E}[\text{CIY}(a)\mid M_t]\right]$$

When uncertainty is high ($P^-$ large), CIY term favors high mode. As uncertainty falls, policy shifts toward low-cost $L$.

### Deliberation Threshold ( #deliberation-cost)

Suppose a planning pause of $\Delta\tau = 0.5 \text{ s}$, with measured $\rho_{\text{delib}} = 0.40 \;\text{surprise/s}$.

Cost during pause: $0.20$ surprise units. If $\Vert\delta_{\text{post}}\Vert = 0.70$, deliberation is worthwhile when:

$$\Delta\eta^*(0.5)\cdot 0.70 \gt 0.20 \;\Longrightarrow\; \Delta\eta^*(0.5) \gt 0.286$$

### Structural Adaptation ( #structural-adaptation-necessity)

Assume maneuvering regime change introduces sustained residual autocorrelation and mismatch floor. If estimated valid radius drops to $R = 0.08$ while $R^\ast = \rho/\alpha = 0.12$, parametric adaptation is no longer adequate ($R^\ast \gt R$), triggering model-class change (e.g., constant-velocity → constant-acceleration process model).

### Tempo + Persistence ( #adaptive-tempo, #persistence-condition)

Using action mix $70\% H, 30\% L$:

$$\bar{\eta}^* = 0.7(0.810) + 0.3(0.321) = 0.663$$

$$\mathcal{T} = \nu \bar{\eta}^* = 5 \cdot 0.663 = 3.315 \;\text{s}^{-1}$$

With $\rho = 0.18 \text{ surprise/s}$ and $\Vert\delta_{\text{critical}}\Vert = 1$:

$$\mathcal{T} \gt \frac{\rho}{\Vert\delta_{\text{critical}}\Vert} \;\;\Rightarrow\;\; 3.315 \gt 0.18 \;\checkmark$$

### Lyapunov Bounds ( #sector-condition-stability)

From data: $\alpha = 2.6 \text{ s}^{-1}$, $R = 1.4$, $\rho = 0.18$.

$$R^* = \frac{\rho}{\alpha} = \frac{0.18}{2.6} \approx 0.069 \lt R$$

$$\Delta\rho^* = \alpha R - \rho = 2.6(1.4) - 0.18 = 3.46$$

The agent is comfortably within its invariant region with substantial adaptive reserve.

## Mapping Quality Summary

| ACT Concept | Kalman Mapping | Status |
|-------------|---------------|--------|
| Scope | Exact | Definitional |
| Causal structure + CIY | Exact | Closed-form KL |
| Model ($M_t$ as sufficient statistic) | Exact | Kalman state + covariance |
| Mismatch ($\delta_t$ = innovation) | Exact | Standard Kalman innovation |
| Gain ($\eta^\ast = K_t$) | Exact | Kalman gain IS uncertainty ratio |
| Tempo ($\mathcal{T} = \nu \bar{\eta}^\ast$) | Exact | Closed-form |
| Persistence condition | Exact | Linear ODE solution |
| Lyapunov bounds ($R^\ast$, $\Delta\rho^\ast$) | Exact | From estimated sector parameters |

## Epistemic Status

This is a *worked instantiation*, not a theoretical claim. Every mapping is exact — the Kalman domain is the canonical case where ACT's formal chain has closed-form realizations. The example validates that the formal chain is internally consistent and instantiable.

## Working Notes

- This example uses a 1D system. The tensor-tempo extension ( #per-dimension-persistence) becomes visible only in multi-dimensional tracking where different state dimensions have different observability.
- The structural adaptation trigger (constant-velocity → constant-acceleration) is manufactured for the example. A more natural test would be a real tracking system with genuine regime changes.
- The Kalman filter is provably optimal for the linear-Gaussian case. Every TFT/ACT quantity has not just an analog but the *exact optimal* value. This makes it the strongest validation but also the easiest — the real test is non-Kalman domains (see #worked-example-bandit).

*(Descended from TFT Appendix C.)*
