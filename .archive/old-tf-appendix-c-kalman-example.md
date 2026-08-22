# Appendix C: Worked Example — 1D Active Tracking (Kalman Domain)

**Epistemic status**: This appendix is a worked instantiation. Every TFT quantity has an exact Kalman-filter counterpart, making this a *validation* of the formal chain rather than an approximate mapping. All quantities are computable in closed form.

## Purpose

This example instantiates the full TFT chain — TF-01 through Appendix A — in a single coherent system with explicit measurable quantities at each step. The system is minimal but includes both action-conditioned sensing and online model updating.

## System: 1D active tracking with selectable sensor mode

The agent tracks scalar state $x_t$ and chooses sensor mode $a_t \in \{L, H\}$:

- Dynamics: $x_{t+1} = x_t + v_t$, $v_t \sim \mathcal{N}(0, q)$, $q = 0.25$
- Observation: $y_t = x_t + n_t^{(a_t)}$
- Low mode noise: $r_L = 9$
- High mode noise: $r_H = 1$
- Event rate: $\nu = 5 \text{ Hz}$
- High mode has higher energy cost

## C.1 TF-01 (Scope)

*Mapping status: exact.*

- $\Omega_t = x_t$ is partially observed via noisy channel.
- $\mathcal{A} = \{L, H\}$ is non-empty and causally affects observation quality (action-dependent observation function, TF-01).
- Residual uncertainty persists ($H(\Omega_t \mid \mathcal C_t) \gt 0$) due to process and sensor noise.

## C.2 TF-02 (Causal Structure) + TF-08 (CIY)

*Mapping status: exact.*

Action precedes observation and changes $P(y_t \mid do(a_t))$ through $r_{a_t}$.
Using low mode as comparator action ($q(a') = \mathbf{1}[a' = L]$) — equivalent to the policy-induced default convention (TF-08) in this binary-action case — the canonical CIY is the interventional KL divergence:

*[Worked Quantity]*
$$\text{CIY}(H) = D_{\mathrm{KL}}\!\big(P(y \mid do(H)) \,\Vert\, P(y \mid do(L))\big)$$
$$= \frac{1}{2}\left[\log\!\left(\frac{P^- + r_L}{P^- + r_H}\right) + \frac{P^- + r_H}{P^- + r_L} - 1\right]$$

With $P^- = 4.25$, this gives:
$$\text{CIY}(H) = \frac{1}{2}\left[\log\!\left(\frac{13.25}{5.25}\right) + \frac{5.25}{13.25} - 1\right] \approx 0.161 \text{ nats}$$

## C.3 TF-03 (Model)

*Mapping status: exact.*

Model state $M_t = (\hat x_{t|t}, P_{t|t})$ is a compression of interaction history with recursive update.

## C.4 TF-04 (Event-Driven Dynamics)

Each sensor read is an observation event; updates occur asynchronously at $\nu = 5 \text{ Hz}$.

## C.5 TF-05 (Mismatch)

*Mapping status: exact.*

Innovation:

*[Worked Quantity]*
$$\delta_t = y_t - \hat{x}_{t|t-1}$$

## C.6 TF-06 (Update Gain)

*Mapping status: exact.*

Scalar Kalman gain:

*[Worked Quantity]*
$$K_t = \frac{P^-_t}{P^-_t + r_{a_t}}$$

With $P^- = 4.25$:

- $K(H) = 4.25 / 5.25 \approx 0.810$
- $K(L) = 4.25 / 13.25 \approx 0.321$

Exact TF-06 uncertainty ratio mapping:
- $U_M = P^-_t$
- $U_o = r_{a_t}$
- $\eta^\ast = K_t$

## C.7 TF-07 and TF-08 (Action Selection + Exploration)

Use policy objective:

*[Worked Objective]*
$$a_t^* = \arg\max_a \left[\mathbb{E}[\text{value}(a)\mid M_t] + \lambda_t \, \mathbb{E}[\text{CIY}(a)\mid M_t]\right]$$

When uncertainty is high ($P^-$ large), $\lambda_t$ and the CIY term favor high mode $H$.
As uncertainty falls, policy shifts toward low-cost $L$.

## C.8 TF-09 (Deliberation Threshold)

Suppose a planning pause of $\Delta\tau = 0.5 \text{ s}$, with measured local pause drift:

*[Measured]*
$$\rho_{\text{delib}} = 0.40 \;\text{surprise/s}$$

Cost during pause: $\rho_{\text{delib}} \cdot \Delta\tau = 0.20$ surprise units.
If $\Vert\delta_{\text{post}}\Vert = 0.70$, deliberation is worthwhile when (Proposition 9.1):

*[Threshold]*
$$\Delta\eta^*(0.5)\cdot 0.70 \gt 0.20 \;\Longrightarrow\; \Delta\eta^*(0.5) \gt 0.286$$

If expected gain improvement is below $0.286$, act immediately.

## C.9 TF-10 (Structural Adaptation Trigger)

Assume maneuvering regime change introduces sustained residual autocorrelation and mismatch floor.
If estimated valid radius drops to $R = 0.08$ while current bound radius is $R^\ast = \rho/\alpha = 0.12$, parametric adaptation is no longer adequate ($R^\ast \gt R$), triggering model-class change (for example constant-velocity → constant-acceleration process model).

## C.10 TF-11 (Tempo + Persistence)

Using action mix $70\% H, 30\% L$:

*[Worked Quantity]*
$$\bar{\eta}^* = 0.7(0.810) + 0.3(0.321) = 0.663$$ *[Worked Quantity]*
$$\mathcal{T} = \nu \bar{\eta}^* = 5 \cdot 0.663 = 3.315 \;\text{s}^{-1}$$

With $\rho = 0.18 \text{ surprise/s}$ and $\Vert\delta_{\text{critical}}\Vert = 1$, persistence condition holds:

*[Check]*
$$\mathcal{T} \gt \frac{\rho}{\Vert\delta_{\text{critical}}\Vert} \;\;\Rightarrow\;\; 3.315 \gt 0.18$$

## C.11 Appendix A (Lyapunov Robustness Mapping)

From data, suppose conservative estimates:

- $\alpha = 2.6 \text{ s}^{-1}$
- $R = 1.4$
- $\rho = 0.18$

Then:

*[Worked Bounds]*
$$R^* = \frac{\rho}{\alpha} = \frac{0.18}{2.6} \approx 0.069 \lt R$$ *[Worked Reserve]*
$$\Delta\rho^* = \alpha R - \rho = 2.6(1.4) - 0.18 = 3.46$$

Interpretation:

- The agent is comfortably within its invariant region.
- It has substantial adaptive reserve to absorb additional disturbance before structural failure.

This completes one explicit path from TF-01 through Appendix A with measurable quantities at each step.

## Summary: Mapping Quality

| TFT Concept | Kalman Mapping | Status |
|-------------|---------------|--------|
| Scope | Exact | Definitional |
| Causal structure + CIY | Exact | Closed-form KL |
| Model ($M_t$ as sufficient statistic) | Exact | Kalman state + covariance |
| Mismatch ($\delta_t$ = innovation) | Exact | Standard Kalman innovation |
| Gain ($\eta^\ast = K_t$) | Exact | Kalman gain IS uncertainty ratio |
| Tempo ($\mathcal{T} = \nu \bar{\eta}^\ast$) | Exact | Closed-form |
| Persistence condition | Exact | Linear ODE solution |
| Lyapunov bounds ($R^\ast$, $\Delta\rho^\ast$) | Exact | From estimated sector parameters |
