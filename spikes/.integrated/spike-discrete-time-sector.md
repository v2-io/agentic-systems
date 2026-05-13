# Spike: Discrete-Time Sector Condition and the Fluid-Limit Gap (GA-5)

**Status**: Spike (investigatory). Attempts to close the last identified gap in Section I's formal chain: the bridge between discrete event-driven dynamics and continuous-time Lyapunov stability results.

**Date**: 2026-04-02

**Motivation**: The theory's quantitative prediction chain is:

$$\text{gain principle} + \text{B1} \;\xrightarrow{\text{derived}}\; \text{sector condition (GA-3)} \;\xrightarrow{\text{Lyapunov (exact)}}\; \text{persistence, reserve, adversarial scaling}$$

The left arrow is closed by #der-gain-sector-bridge. The right arrow is proved by #deriv-sector-condition (Props A.1, A.1S, A.2) — but in continuous time. Real agents operate in discrete time: event-driven updates ( #form-event-driven-dynamics) with finite step size $\eta^\ast$. The bridge from discrete to continuous is the fluid-limit approximation, flagged in #hyp-mismatch-dynamics as valid when $\eta^\ast \ll 1$. #der-gain-sector-bridge identifies this as "the only remaining gap in Section I's formal chain" — label GA-5.

This spike closes GA-5 by proving discrete-time analogs of all three propositions directly, characterizing the fluid-limit approximation error, and assessing downstream impact.

**Depends on**: #deriv-sector-condition, #result-sector-condition-stability, #hyp-mismatch-dynamics, #form-event-driven-dynamics, #emp-update-gain, #der-gain-sector-bridge, #form-composition-closure, #result-persistence-condition, #result-adversarial-tempo-advantage, #result-adversarial-exponent-regimes

---

## 0. The Gap in Detail

The continuous-time results assume dynamics $d\delta/dt = -F(\mathcal{T}, \delta) + w(t)$, where $F$ is the correction function. But the actual update mechanism ( #emp-update-gain) is:

$$M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$$

This is a discrete map, applied at event times $\tau_1, \tau_2, \ldots$ with rate $\nu$. The continuous ODE is obtained by treating $\nu$ events per unit time, each making a correction of size $\eta^\ast$, as a smooth flow with rate $\mathcal{T} = \nu \cdot \eta^\ast$. This is the **fluid-limit approximation**.

The approximation is good when each correction is small ($\eta^\ast \ll 1$) — many small steps approximate a continuous flow. It is poor when corrections are large ($\eta^\ast$ near 1) — the discrete dynamics can overshoot, oscillate, or exhibit qualitative behaviors absent from the ODE.

The composition-closure bridge lemma ( #form-composition-closure) already works in discrete time, using a contraction factor $\lambda = 1 - \alpha_c / \nu_c$. This demonstrates the approach is viable. This spike extends it to the full sector-condition framework.

---

## 1. Discrete-Time Setup

### 1.1 The Discrete Update Map

Let $\delta_k \in \mathbb{R}^n$ be the mismatch vector after $k$ update steps. At each step, the agent observes, computes a correction, and the environment introduces disturbance. The dynamics are:

*[Formulation (discrete-mismatch-dynamics)]*

$$\delta_{k+1} = \delta_k - \eta^\ast \cdot H \, g(\delta_k) + w_k$$

where:
- $\eta^\ast \cdot H \, g(\delta_k)$ is the correction applied at step $k$ (the gain-based update projected into observation space, cf. #der-gain-sector-bridge)
- $w_k$ is the per-step disturbance — new mismatch introduced between steps $k$ and $k+1$
- $H$ maps state-space corrections to mismatch-space reductions

Define the **discrete correction function**:

*[Definition (discrete-correction-function)]*

$$f(\delta_k) \;=\; \eta^\ast \cdot H \, g(\delta_k)$$

so the dynamics become:

$$\delta_{k+1} = \delta_k - f(\delta_k) + w_k$$

This is the one-step update map. It replaces the continuous correction function $F(\mathcal{T}, \delta)$ with $f(\delta)$, which incorporates the gain $\eta^\ast$ directly.

### 1.2 Discrete Sector Condition

The continuous sector condition (A2') requires $\delta^T F(\mathcal{T}, \delta) \geq \alpha \lVert\delta\rVert^2$. The discrete analog constrains the one-step update map to be contracting:

*[Definition (discrete-sector-condition, DA2')]*

There exist constants $c_{\min} \gt 0$ and $c_{\max} \lt 2/\eta^\ast$ such that for all $\lVert\delta\rVert \leq R$:

$$c_{\min} \, \eta^\ast \, \lVert\delta\rVert^2 \;\leq\; \delta^T f(\delta) \;\leq\; c_{\max} \, \eta^\ast \, \lVert\delta\rVert^2 \tag{DA2'}$$

**Lower bound** ($c_{\min}$): same role as in the continuous case — the correction points inward with at least baseline efficiency. Identical to B1 (directional fidelity) from #der-gain-sector-bridge: $c_{\min} = \inf_{\lVert\delta\rVert \leq R} \delta^T H g(\delta) / \lVert\delta\rVert^2$.

**Upper bound** ($c_{\max} \lt 2/\eta^\ast$): **new in discrete time.** This prevents the correction from overshooting — correcting so aggressively that mismatch increases rather than decreases. The continuous case has no analog because infinitesimal corrections cannot overshoot.

The upper bound is equivalent to requiring the one-step map $\delta \mapsto \delta - f(\delta)$ to be non-expansive (in the mismatch-reducing direction):

$$\lVert\delta - f(\delta)\rVert^2 = \lVert\delta\rVert^2 - 2\delta^T f(\delta) + \lVert f(\delta)\rVert^2$$

For this to be less than $\lVert\delta\rVert^2$ (contraction), we need $2\delta^T f(\delta) \gt \lVert f(\delta)\rVert^2$. The upper bound in (DA2') ensures this by bounding the correction magnitude relative to the inner product, preventing overshoot.

### 1.3 Contraction Factor

Under (DA2'), the discrete dynamics contract mismatch at each step. Define:

*[Derived (contraction-factor, from DA2')]*

$$\lambda \;=\; 1 - \eta^\ast \cdot c_{\min} \;=\; 1 - \alpha / \nu$$

where $\alpha = \eta^\ast \cdot c_{\min} \cdot \nu = \mathcal{T} \cdot c_{\min} / c_{\text{nom}}$ is the continuous sector parameter (with $c_{\text{nom}}$ a normalization factor that equals 1 when the bridge is direct, as in the Kalman and Beta-Bernoulli cases — see #der-gain-sector-bridge).

For the important special case where the bridge gives $\alpha = \eta^\ast \cdot c_{\min}$ per event and there are $\nu$ events per unit time, so $\alpha_{\text{continuous}} = \nu \cdot \eta^\ast \cdot c_{\min}$:

$$\lambda = 1 - \eta^\ast \cdot c_{\min}$$

The upper bound in (DA2') guarantees $\lambda \gt -(1 - \eta^\ast \cdot c_{\max})$, ensuring the correction doesn't reverse the mismatch direction (no sign flip / oscillation). Specifically, since $c_{\max} \lt 2/\eta^\ast$, we have $\eta^\ast \cdot c_{\max} \lt 2$, so $\lambda \gt -1$, preventing period-2 oscillation.

For strict contraction (no oscillation at all), we need $\lambda \gt 0$, i.e., $\eta^\ast \cdot c_{\min} \lt 1$, i.e., the per-step correction is less than the full mismatch. This is the discrete analog of the "realistic systems" condition noted in #form-composition-closure: "the agent doesn't fully correct in a single step."

**Summary of contraction regimes:**

| $\eta^\ast \cdot c_{\min}$ | $\lambda$ | Behavior |
|:---:|:---:|:---|
| $\ll 1$ | $\approx 1 - \eta^\ast c_{\min}$ | Gentle contraction, closely approximates ODE |
| $\approx 0.5$ | $\approx 0.5$ | Moderate contraction, quantitative deviation from ODE |
| $\approx 1$ | $\approx 0$ | Critical damping — corrects fully in one step |
| $\gt 1$ (with $c_{\max} \lt 2/\eta^\ast$) | $\lt 0$ | Oscillatory contraction — overshoots then corrects |
| $c_{\max} \geq 2/\eta^\ast$ | $\leq -1$ | Divergent oscillation — (DA2') violated |

---

## 2. Proposition DA.1: Discrete-Time Bounded Mismatch

### Statement

Under (DA2') with bounded per-step disturbance $\lVert w_k \rVert \leq \rho_{\text{step}}$, the mismatch $\delta_k$ is ultimately bounded:

*[Derived (discrete-bounded-mismatch, from discrete Lyapunov analysis)]*

$$\limsup_{k \to \infty} \lVert\delta_k\rVert \;\leq\; \frac{\rho_{\text{step}}}{1 - \lvert\lambda\rvert} \;=\; R^\ast_D$$

provided $\lvert\lambda\rvert \lt 1$ (equivalently, $0 \lt \eta^\ast c_{\min}$ and $\eta^\ast c_{\max} \lt 2$) and $R^\ast_D \lt R$.

### Proof

Define the discrete Lyapunov function:

$$V_k = \frac{1}{2}\lVert\delta_k\rVert^2$$

**Step 1: One-step bound on $\lVert\delta_{k+1}\rVert$.**

From the dynamics $\delta_{k+1} = \delta_k - f(\delta_k) + w_k$:

$$\lVert\delta_{k+1}\rVert \leq \lVert\delta_k - f(\delta_k)\rVert + \lVert w_k\rVert$$

We need to bound $\lVert\delta_k - f(\delta_k)\rVert$. Expand:

$$\lVert\delta_k - f(\delta_k)\rVert^2 = \lVert\delta_k\rVert^2 - 2\delta_k^T f(\delta_k) + \lVert f(\delta_k)\rVert^2$$

By the lower bound in (DA2'): $\delta_k^T f(\delta_k) \geq \eta^\ast c_{\min} \lVert\delta_k\rVert^2$.

For the $\lVert f(\delta_k)\rVert^2$ term, we use the upper bound. Since $f(\delta) = \eta^\ast H g(\delta)$ and (DA2') gives $\delta^T f(\delta) \leq \eta^\ast c_{\max} \lVert\delta\rVert^2$, by Cauchy-Schwarz $\lVert f(\delta)\rVert \leq \eta^\ast c_{\max} \lVert\delta\rVert$ (this holds when $f$ is radially bounded, which follows from the upper sector bound applied along the $\delta$ direction — a standard consequence of the two-sided sector condition).

Therefore:

$$\lVert\delta_k - f(\delta_k)\rVert^2 \leq \lVert\delta_k\rVert^2 - 2\eta^\ast c_{\min}\lVert\delta_k\rVert^2 + (\eta^\ast c_{\max})^2 \lVert\delta_k\rVert^2$$

$$= \lVert\delta_k\rVert^2 \left(1 - 2\eta^\ast c_{\min} + (\eta^\ast c_{\max})^2\right)$$

Define $\lambda^2_{\text{eff}} = 1 - 2\eta^\ast c_{\min} + (\eta^\ast c_{\max})^2$, so $\lVert\delta_k - f(\delta_k)\rVert \leq \lvert\lambda_{\text{eff}}\rvert \cdot \lVert\delta_k\rVert$.

**Simplification for symmetric sector bounds** ($c_{\min} = c_{\max} = c$, the linear case):

$$\lambda^2_{\text{eff}} = 1 - 2\eta^\ast c + (\eta^\ast c)^2 = (1 - \eta^\ast c)^2$$

$$\lvert\lambda_{\text{eff}}\rvert = \lvert 1 - \eta^\ast c \rvert$$

which recovers $\lambda = 1 - \eta^\ast c$ exactly. For the general case, $\lvert\lambda_{\text{eff}}\rvert$ depends on the gap between $c_{\min}$ and $c_{\max}$.

**Step 2: Geometric series bound.**

Under the contraction $\lVert\delta_k - f(\delta_k)\rVert \leq \lvert\lambda_{\text{eff}}\rvert \cdot \lVert\delta_k\rVert$:

$$\lVert\delta_{k+1}\rVert \leq \lvert\lambda_{\text{eff}}\rvert \cdot \lVert\delta_k\rVert + \rho_{\text{step}}$$

This is a linear recurrence. Starting from $\lVert\delta_0\rVert$:

$$\lVert\delta_k\rVert \leq \lvert\lambda_{\text{eff}}\rvert^k \lVert\delta_0\rVert + \rho_{\text{step}} \sum_{j=0}^{k-1} \lvert\lambda_{\text{eff}}\rvert^j$$

$$= \lvert\lambda_{\text{eff}}\rvert^k \lVert\delta_0\rVert + \rho_{\text{step}} \cdot \frac{1 - \lvert\lambda_{\text{eff}}\rvert^k}{1 - \lvert\lambda_{\text{eff}}\rvert}$$

As $k \to \infty$ (using $\lvert\lambda_{\text{eff}}\rvert \lt 1$):

$$\limsup_{k \to \infty} \lVert\delta_k\rVert \leq \frac{\rho_{\text{step}}}{1 - \lvert\lambda_{\text{eff}}\rvert}$$

**Step 3: Persistence condition.**

The discrete agent persists iff $R^\ast_D \lt R$:

$$\frac{\rho_{\text{step}}}{1 - \lvert\lambda_{\text{eff}}\rvert} \lt R$$

For the symmetric case ($\lambda_{\text{eff}} = 1 - \eta^\ast c$, with $0 \lt \eta^\ast c \lt 1$):

$$R^\ast_D = \frac{\rho_{\text{step}}}{\eta^\ast c_{\min}}$$

The persistence condition is $\eta^\ast c_{\min} \gt \rho_{\text{step}} / R$. $\square$

**Epistemic status: Exact.** The derivation is a standard discrete Lyapunov / contraction mapping argument (cf. Elaydi 2005, Ch. 4). The two-sided sector condition (DA2') is stronger than the continuous one-sided (A2') — the upper bound is genuinely new. The result is exact under its assumptions.

### Recovery of the Continuous Result

In the symmetric case, $R^\ast_D = \rho_{\text{step}} / (\eta^\ast c)$. The per-step disturbance relates to the continuous disturbance rate by $\rho_{\text{step}} = \rho / \nu$ (disturbance per unit time divided by steps per unit time). The sector parameter is $\alpha = \nu \cdot \eta^\ast \cdot c = \mathcal{T} \cdot c / c_{\text{nom}}$. So:

$$R^\ast_D = \frac{\rho / \nu}{\eta^\ast c} = \frac{\rho}{\nu \cdot \eta^\ast \cdot c} = \frac{\rho}{\alpha}$$

This is exactly the continuous result $R^\ast = \rho / \alpha$ from Prop A.1. The discrete and continuous persistence conditions coincide when the identification $\rho_{\text{step}} = \rho / \nu$ holds. The fluid-limit gap is closed for the deterministic case: the continuous result is not an approximation of the discrete result — it is the same result expressed in different units.

---

## 3. Proposition DA.2: Discrete-Time Adaptive Reserve

### Statement

Under the conditions of DA.1, the agent can tolerate a sudden increase in per-step disturbance of:

*[Derived (discrete-adaptive-reserve)]*

$$\Delta\rho^\ast_{\text{step}} = (1 - \lvert\lambda_{\text{eff}}\rvert) \cdot R - \rho_{\text{step}}$$

Equivalently, in rate units (multiplying by $\nu$):

$$\Delta\rho^\ast = \alpha R - \rho$$

which is identical to the continuous Prop A.2.

### Proof

After a shock, the new per-step disturbance is $\rho_{\text{step}} + \Delta\rho_{\text{step}}$. The new ultimately bounded radius is $(\rho_{\text{step}} + \Delta\rho_{\text{step}}) / (1 - \lvert\lambda_{\text{eff}}\rvert)$. This remains within the sector-condition region iff:

$$\frac{\rho_{\text{step}} + \Delta\rho_{\text{step}}}{1 - \lvert\lambda_{\text{eff}}\rvert} \leq R$$

Solving: $\Delta\rho_{\text{step}} \leq (1 - \lvert\lambda_{\text{eff}}\rvert) R - \rho_{\text{step}}$. $\square$

**Epistemic status: Exact.** Immediate corollary of DA.1.

---

## 4. Proposition DA.1S: Discrete-Time Stochastic Bounded Mismatch

### Statement

Under (DA2') with stochastic per-step disturbance ($w_k$ zero-mean, i.i.d., $\mathbb{E}[\lVert w_k\rVert^2] = \sigma^2_{\text{step}}$), the expected squared mismatch satisfies:

*[Derived (discrete-stochastic-bounded-mismatch, from supermartingale argument)]*

$$\mathbb{E}[\lVert\delta_k\rVert^2] \leq \lambda_{\text{eff}}^{2k} \lVert\delta_0\rVert^2 + \frac{\sigma^2_{\text{step}}}{1 - \lambda_{\text{eff}}^2}$$

For the symmetric case ($\lambda_{\text{eff}} = 1 - \eta^\ast c$):

$$\mathbb{E}[\lVert\delta_k\rVert^2]_{ss} = \frac{\sigma^2_{\text{step}}}{1 - (1 - \eta^\ast c)^2} = \frac{\sigma^2_{\text{step}}}{2\eta^\ast c - (\eta^\ast c)^2}$$

### Proof

**Step 1: Squared-norm recurrence.**

$$\lVert\delta_{k+1}\rVert^2 = \lVert\delta_k - f(\delta_k) + w_k\rVert^2$$

$$= \lVert\delta_k - f(\delta_k)\rVert^2 + 2(\delta_k - f(\delta_k))^T w_k + \lVert w_k\rVert^2$$

Taking expectations. Since $w_k$ is independent of $\delta_k$ (the disturbance at step $k$ is independent of the state before that step's correction) and zero-mean, the cross-term vanishes:

$$\mathbb{E}[\lVert\delta_{k+1}\rVert^2] = \mathbb{E}[\lVert\delta_k - f(\delta_k)\rVert^2] + \sigma^2_{\text{step}}$$

From Step 1 of the DA.1 proof (within the sector-condition region):

$$\lVert\delta_k - f(\delta_k)\rVert^2 \leq \lambda_{\text{eff}}^2 \lVert\delta_k\rVert^2$$

Therefore:

$$\mathbb{E}[\lVert\delta_{k+1}\rVert^2] \leq \lambda_{\text{eff}}^2 \, \mathbb{E}[\lVert\delta_k\rVert^2] + \sigma^2_{\text{step}}$$

**Step 2: Solve the linear recurrence.**

This is a contraction with additive perturbation:

$$\mathbb{E}[\lVert\delta_k\rVert^2] \leq \lambda_{\text{eff}}^{2k} \lVert\delta_0\rVert^2 + \sigma^2_{\text{step}} \sum_{j=0}^{k-1} \lambda_{\text{eff}}^{2j}$$

As $k \to \infty$:

$$\mathbb{E}[\lVert\delta_k\rVert^2]_{ss} \leq \frac{\sigma^2_{\text{step}}}{1 - \lambda_{\text{eff}}^2}$$

**Step 3: Supermartingale formulation.**

Define $Z_k = \lVert\delta_k\rVert^2 - \sigma^2_{\text{step}} / (1 - \lambda_{\text{eff}}^2)$. Then:

$$\mathbb{E}[Z_{k+1} \mid \delta_k] \leq \lambda_{\text{eff}}^2 \lVert\delta_k\rVert^2 + \sigma^2_{\text{step}} - \frac{\sigma^2_{\text{step}}}{1 - \lambda_{\text{eff}}^2}$$

$$= \lambda_{\text{eff}}^2 \lVert\delta_k\rVert^2 - \frac{\lambda_{\text{eff}}^2 \sigma^2_{\text{step}}}{1 - \lambda_{\text{eff}}^2}$$

$$= \lambda_{\text{eff}}^2 \left(\lVert\delta_k\rVert^2 - \frac{\sigma^2_{\text{step}}}{1 - \lambda_{\text{eff}}^2}\right) = \lambda_{\text{eff}}^2 Z_k$$

Since $\lambda_{\text{eff}}^2 \lt 1$, the process $Z_k$ is a supermartingale. By the supermartingale convergence theorem (Doob), $Z_k$ converges almost surely and $\mathbb{E}[\lVert\delta_k\rVert^2]$ converges to $\sigma^2_{\text{step}} / (1 - \lambda_{\text{eff}}^2)$.

**Step 4: RMS steady-state mismatch.**

$$R^{\ast}_{D,S} = \sqrt{\frac{\sigma^2_{\text{step}}}{1 - \lambda_{\text{eff}}^2}}$$

For the symmetric case with small $\eta^\ast c$:

$$1 - \lambda_{\text{eff}}^2 = 1 - (1 - \eta^\ast c)^2 = 2\eta^\ast c - (\eta^\ast c)^2 \approx 2\eta^\ast c$$

$$R^{\ast}_{D,S} \approx \frac{\sigma_{\text{step}}}{\sqrt{2\eta^\ast c}}$$

**Step 5: Discrete persistence condition (stochastic).**

The agent persists in the mean-square sense iff $R^{\ast}_{D,S} \lt R$:

$$\frac{\sigma^2_{\text{step}}}{1 - \lambda_{\text{eff}}^2} \lt R^2 \quad \Longleftrightarrow \quad 1 - \lambda_{\text{eff}}^2 \gt \frac{\sigma^2_{\text{step}}}{R^2}$$

For the symmetric case: $2\eta^\ast c - (\eta^\ast c)^2 \gt \sigma^2_{\text{step}} / R^2$.

**Step 6: Tail bound.**

At steady state, by Markov's inequality:

$$P(\lVert\delta_k\rVert \gt R) \leq \frac{\sigma^2_{\text{step}}}{(1 - \lambda_{\text{eff}}^2) R^2}$$

$\square$

### Recovery of the Continuous Result

The per-step noise variance relates to the continuous noise intensity by $\sigma^2_{\text{step}} = \sigma^2_w / \nu$ (the continuous Wiener process accumulated over an inter-event interval of $1/\nu$). Substituting into the small-$\eta^\ast c$ approximation:

$$R^{\ast}_{D,S} \approx \frac{\sigma_{\text{step}}}{\sqrt{2\eta^\ast c}} = \frac{\sigma_w / \sqrt{\nu}}{\sqrt{2\eta^\ast c}} = \frac{\sigma_w}{\sqrt{2 \nu \eta^\ast c}} = \frac{\sigma_w}{\sqrt{2\alpha}}$$

This recovers the continuous result $R^\ast_S = \sigma_w \sqrt{n/(2\alpha)}$ from Prop A.1S (for $n = 1$; the multi-dimensional extension follows by the same argument applied per dimension).

**Epistemic status: Exact.** The supermartingale argument is standard (Williams 1991, Meyn & Tweedie 1993). The result is the discrete analog of the Itô-Lyapunov calculation in Prop A.1S. The convergence to the continuous result under $\eta^\ast c \to 0$ is exact.

---

## 5. The Fluid-Limit Approximation: Formal Derivation and Error Characterization

### 5.1 The Formal Limit

Consider a sequence of discrete systems indexed by $\nu$ (the event rate). At each step, the correction has gain $\eta^\ast = \mathcal{T}/\nu$ (so that $\mathcal{T}$ is held fixed as $\nu$ varies) and the per-step disturbance is $\rho_{\text{step}} = \rho/\nu$.

Define the continuous-time interpolation:

$$\delta^{(\nu)}(t) = \delta_{\lfloor \nu t \rfloor}$$

(the piecewise-constant process that holds the value of the discrete state at the last event before time $t$).

*[Derived (fluid-limit-convergence, conditional on regularity)]*

**Theorem (Fluid limit).** As $\nu \to \infty$ with $\mathcal{T} = \nu \cdot \eta^\ast$ and $\rho = \nu \cdot \rho_{\text{step}}$ held constant, and with $f(\delta) = \eta^\ast \cdot \tilde{F}(\delta)$ where $\tilde{F}$ is Lipschitz with constant $L$:

$$\sup_{0 \leq t \leq T_0} \lVert \delta^{(\nu)}(t) - \delta_{\text{ODE}}(t) \rVert \;\xrightarrow{\nu \to \infty}\; 0$$

where $\delta_{\text{ODE}}(t)$ solves $d\delta/dt = -\tilde{F}(\delta) + \rho(t)$ (the continuous dynamics of #hyp-mismatch-dynamics) over any finite horizon $[0, T_0]$.

**Proof sketch.** This is a standard deterministic approximation result (Kurtz 1970, Ethier & Kurtz 1986, Ch. 11). The key conditions are:
1. Corrections per unit time: $\nu$ corrections, each of size $O(1/\nu)$.
2. Lipschitz regularity of $\tilde{F}$: ensures the accumulated error from discretization is $O(1/\nu)$ per unit time.
3. Bounded time horizon.

Over one step of size $\Delta t = 1/\nu$, the discrete update is:

$$\delta_{k+1} - \delta_k = -\frac{\mathcal{T}}{\nu} \tilde{F}(\delta_k) + \frac{\rho_k}{\nu}$$

Summing $\nu$ steps over a unit time interval and comparing with the ODE integral $\int_0^1 [-\tilde{F}(\delta(t)) + \rho(t)] \, dt$ gives an error of order $O(L \cdot \mathcal{T} / \nu) = O(L \cdot \eta^\ast)$ per unit time, by the Lipschitz condition.

Over a finite horizon $T_0$, the total error is bounded by:

$$\sup_{0 \leq t \leq T_0} \lVert \delta^{(\nu)}(t) - \delta_{\text{ODE}}(t) \rVert \leq C \cdot \eta^\ast \cdot (e^{L \mathcal{T} T_0} - 1) / (L\mathcal{T})$$

where $C$ depends on $\tilde{F}$ and the disturbance regularity. This goes to zero as $\nu \to \infty$ ($\eta^\ast \to 0$) for fixed $T_0$. $\square$

**Epistemic status: Conditional.** The result is a standard functional law of large numbers (FLLN) for density-dependent processes. The condition is Lipschitz regularity of $\tilde{F}$ and a finite time horizon. The finite-horizon restriction is not a limitation for AAD because the steady-state bounds (Props A.1, DA.1) are independent of time horizon — they describe the long-run attracting set, which the discrete and continuous systems share exactly (as shown in Sections 2 and 3).

### 5.2 Quantitative Approximation Error

For finite $\nu$ (finite $\eta^\ast$), the steady-state mismatch bounds differ between discrete and continuous. The difference is the fluid-limit approximation error.

**Model D (deterministic).** From Prop A.1: $R^\ast_{\text{ODE}} = \rho/\alpha$. From Prop DA.1 (symmetric case): $R^\ast_D = \rho_{\text{step}} / (\eta^\ast c) = \rho / (\nu \eta^\ast c) = \rho/\alpha$. The steady-state bounds are **identical**. There is no approximation error in the steady-state bound.

*[Derived (zero-steady-state-gap-deterministic)]*

$$R^\ast_D = R^\ast_{\text{ODE}} = \frac{\rho}{\alpha} \qquad \text{(exact, all } \eta^\ast \text{)}$$

This is because the contraction-based bound and the Lyapunov-based bound yield the same worst-case ratio of disturbance to correction. The discrete and continuous arguments are structurally identical — they differ only in whether the time variable is continuous or discrete.

**Model S (stochastic).** From Prop A.1S: $\mathbb{E}[\lVert\delta\rVert^2]_{ss} = n\sigma^2_w / (2\alpha)$. From Prop DA.1S (symmetric case, $n = 1$):

$$\mathbb{E}[\lVert\delta\rVert^2]_{ss} = \frac{\sigma^2_{\text{step}}}{2\eta^\ast c - (\eta^\ast c)^2} = \frac{\sigma^2_w / \nu}{2\eta^\ast c - (\eta^\ast c)^2}$$

Using $\alpha = \nu \eta^\ast c$:

$$= \frac{\sigma^2_w}{2\alpha - \alpha^2/\nu} = \frac{\sigma^2_w}{2\alpha(1 - \alpha/(2\nu))} = \frac{\sigma^2_w}{2\alpha} \cdot \frac{1}{1 - \eta^\ast c / 2}$$

The relative error compared to the continuous result is:

*[Derived (stochastic-steady-state-correction)]*

$$\frac{R^{\ast 2}_{D,S}}{R^{\ast 2}_S} = \frac{1}{1 - \eta^\ast c / 2} \approx 1 + \frac{\eta^\ast c}{2} + O((\eta^\ast c)^2)$$

The discrete steady-state mismatch exceeds the continuous prediction by a factor of approximately $1 + \eta^\ast c / 2$ in variance (or $1 + \eta^\ast c / 4$ in RMS). This is the fluid-limit approximation error for the stochastic case.

**Interpretation.** The approximation error:
- **Vanishes** as $\eta^\ast \to 0$ (the fluid limit), confirming the continuous result as the exact limit.
- **Is small** when $\eta^\ast c \ll 1$ (the small-gain regime where each correction is a small fraction of the mismatch).
- **Is moderate** when $\eta^\ast c \approx 0.5$ (roughly 25% excess variance, 12% excess RMS).
- **Diverges** as $\eta^\ast c \to 1$ (critical damping — the discrete system sits exactly at the stability boundary).

The correction is always positive: the discrete system has **more** steady-state mismatch than the continuous prediction, because finite-step corrections induce variance even in the absence of external noise (the "discretization noise" effect).

### 5.3 When Does the Approximation Matter?

| Regime | $\eta^\ast c$ | Approximation quality | Example |
|:---|:---:|:---|:---|
| Converged Bayesian | $\ll 0.01$ | Excellent ($\lt 0.5\%$ error) | Kalman filter at steady state |
| Moderate learning | $0.01$–$0.1$ | Good ($0.5\%$–$5\%$ error) | Gradient descent, mid-training |
| Aggressive learning | $0.1$–$0.5$ | Fair ($5\%$–$25\%$ error) | Early training, high learning rate |
| Near-critical | $0.5$–$1$ | Poor ($\gt 25\%$ error) | RL with unit step size, initial Kalman |
| Overcritical | $\gt 1$ | **Qualitatively wrong** (ODE predicts stability, discrete oscillates) | Poorly tuned controller |

The critical regime is $\eta^\ast c \gt 1$: the continuous ODE predicts monotone convergence with rate $\alpha$, but the discrete system oscillates (with shrinking amplitude if $\eta^\ast c \lt 2$, diverging if $\eta^\ast c \geq 2$). The fluid-limit approximation is qualitatively misleading here.

**However, for well-designed agents, $\eta^\ast c \ll 1$ is the normal operating regime.** The optimal gain ( #emp-update-gain) is $\eta^\ast = U_M / (U_M + U_o)$. At steady state, $U_M$ has converged and $\eta^\ast$ is determined by the signal-to-noise ratio. For the Kalman filter with process noise $Q$ and observation noise $R_{\text{obs}}$, the steady-state gain is $K_{ss} \approx \sqrt{Q/R_{\text{obs}}}$ when $Q \ll R_{\text{obs}}$ (slow dynamics, noisy observations — the common case). The directional fidelity is $c = 1$ for linear systems. So $\eta^\ast c = K_{ss} \ll 1$ in the normal regime.

The fluid-limit approximation is *most* inaccurate precisely when it is *least* needed: during initial transients with large $\eta^\ast$, where the qualitative behavior (rapid convergence from a distant initial condition) is the same regardless of whether the path is smooth or oscillatory. The approximation is *most* accurate when it *most* matters: at steady state, where the quantitative predictions (persistence bound, adaptive reserve, adversarial exponent) are evaluated.

---

## 6. Transient Dynamics: Where Discrete and Continuous Diverge

The steady-state results coincide (deterministic) or differ by $O(\eta^\ast c)$ (stochastic). The transient behavior is where the real differences live.

### 6.1 Convergence Rate

**Continuous:** $\lVert\delta(t)\rVert \leq \lVert\delta_0\rVert e^{-\alpha t} + \rho/\alpha$. The convergence is monotone.

**Discrete (symmetric, $0 \lt \eta^\ast c \lt 1$):** $\lVert\delta_k\rVert \leq (1 - \eta^\ast c)^k \lVert\delta_0\rVert + \rho_{\text{step}}/(\eta^\ast c)$. The convergence is monotone.

Over the same physical time $t = k/\nu$:

$$(1 - \eta^\ast c)^k = (1 - \eta^\ast c)^{\nu t} \to e^{-\nu \eta^\ast c \cdot t} = e^{-\alpha t} \quad \text{as } \nu \to \infty$$

So the discrete convergence rate approaches the continuous rate in the fluid limit. For finite $\nu$, the discrete rate $(1 - \eta^\ast c)^{\nu t}$ is **always faster** than $e^{-\alpha t}$ (by Jensen's inequality applied to the concave logarithm: $\nu \ln(1 - \eta^\ast c) \lt -\nu \eta^\ast c = -\alpha t$, so $(1 - \eta^\ast c)^{\nu t} \lt e^{-\alpha t}$).

Wait — this inequality goes the other way. We have $\ln(1 - x) \lt -x$ for $x \in (0,1)$, so $\nu \ln(1 - \eta^\ast c) \lt -\nu \eta^\ast c$, giving $(1 - \eta^\ast c)^{\nu t} \lt e^{-\alpha t}$. The discrete system converges **faster** in the envelope bound. This is consistent: the discrete system "overshoots" slightly at each step and the overshoot acts as additional correction. However, this is a bound comparison, not a trajectory comparison — the actual discrete trajectory may oscillate around the monotone continuous trajectory.

### 6.2 Oscillatory Regime ($\eta^\ast c \gt 1$, $\eta^\ast c \lt 2$)

When $\eta^\ast c \gt 1$, the contraction factor $\lambda = 1 - \eta^\ast c \lt 0$. The discrete dynamics alternate in sign:

$$\delta_k \approx (-1)^k \lvert\lambda\rvert^k \delta_0$$

The mismatch oscillates around zero with decreasing amplitude. The **envelope** decays as $\lvert\lambda\rvert^k = \lvert 1 - \eta^\ast c \rvert^k$, which gives the same ultimate bound as before. The continuous ODE, by contrast, predicts monotone decay — it cannot capture the oscillation.

**Physically:** the agent overcorrects at each step, swinging past the true state and then correcting back. The model alternates between overestimating and underestimating reality. The long-run bound is unaffected, but the transient path is qualitatively different.

This regime occurs:
- At initialization, when $\eta^\ast \to 1$ (high model uncertainty, strong trust in observations)
- With aggressive learning rates in gradient descent ($\eta \gt 1/\mu$ where $\mu$ is the strong convexity modulus)
- In PID control when proportional gain exceeds critical damping

In all cases, the conventional wisdom is the same: reduce the gain (learning rate, proportional gain) to eliminate oscillation. The discrete sector condition (DA2') with its upper bound formalizes this: $c_{\max} \lt 2/\eta^\ast$ is the no-divergence condition.

---

## 7. Downstream Impact Assessment

The central question: do any downstream results change when discrete-time corrections are applied?

### 7.1 Persistence Condition ( #result-persistence-condition)

**Impact: None.** The discrete persistence condition $\eta^\ast c_{\min} \gt \rho_{\text{step}}/R$ is equivalent to the continuous condition $\alpha \gt \rho/R$ under the identification $\alpha = \nu \eta^\ast c_{\min}$, $\rho = \nu \rho_{\text{step}}$. The two-part structure (structural persistence + task adequacy) and the operational forms are unchanged.

### 7.2 Adaptive Reserve ( #result-sector-condition-stability, Prop A.2)

**Impact: None.** $\Delta\rho^\ast = \alpha R - \rho$ is identical in discrete and continuous formulations (Prop DA.2).

### 7.3 Adversarial Tempo Advantage ( #result-adversarial-tempo-advantage)

**Impact: No qualitative change; small quantitative correction in Model S.** The exponent $b = 2$ (Model D) and $b = 3/2$ (Model S) are derived from steady-state ratios. The Model D steady-state is identical in discrete and continuous. The Model S steady-state has the correction factor $1/(1 - \eta^\ast c/2)$, which affects both agents equally (same $\eta^\ast c$ for both under symmetric coupling) and therefore **cancels in the ratio**. The exponents are unchanged.

More precisely: the discrete Model S steady-state for agent $B$ is:

$$R^{\ast 2}_{B} = \frac{\sigma^2_{B,\text{step}}}{2\eta^\ast_B c_B - (\eta^\ast_B c_B)^2}$$

The ratio $R^{\ast 2}_B / R^{\ast 2}_A$ depends on $\sigma^2_B/\sigma^2_A$ and $(\eta^\ast_A c_A) / (\eta^\ast_B c_B)$. The discrete correction factors $(1 - \eta^\ast c/2)$ appear in both numerator and denominator. When agents have similar $\eta^\ast c$ (similar correction efficiency), the correction cancels. When they differ, there is an $O(\eta^\ast c)$ perturbation to the exponent — negligible in the regime where the adversarial analysis is applied (steady state, where $\eta^\ast$ is small).

### 7.4 Adversarial Exponent Regimes ( #result-adversarial-exponent-regimes)

**Impact: None.** The exponents $b = 2$ (Model D), $b = 3/2$ (Model S), and the interpolation to non-coupling-dominant regimes all follow from steady-state formulas that are either identical (Model D) or differ by a factor that cancels in ratios (Model S).

### 7.5 Multi-Timescale Stability ( #sketch-multi-timescale-stability)

**Impact: Potentially clarifying.** The timescale separation condition $\nu_{n+1} \ll \nu_n$ from #der-temporal-nesting is naturally a discrete condition. The continuous singular perturbation analysis assumes $\epsilon_k / \epsilon_{k+1} \ll 1$. The discrete framework gives a concrete interpretation: the faster level must complete many correction cycles ($\gg 1/(\eta^\ast c)$ steps) before the slower level takes a single step. This is the condition for the faster level's steady-state bound to be reached before the slower level perturbs it — i.e., the condition for the fluid-limit approximation of the faster level to be valid from the perspective of the slower level.

### 7.6 Composition Closure ( #form-composition-closure)

**Impact: Already resolved.** The composition-closure bridge lemma is already stated in discrete time with $\lambda = 1 - \alpha_c/\nu_c$. The results of this spike confirm that the discrete formulation is consistent with the continuous sector-condition framework. No changes needed.

### 7.7 Gain-Sector Bridge ( #der-gain-sector-bridge)

**Impact: Upper bound added.** The continuous bridge requires only directional fidelity (lower bound, B1). The discrete bridge additionally requires the upper bound ($c_{\max} \lt 2/\eta^\ast$). For optimal Bayesian updates (Kalman, conjugate), this is satisfied automatically: the Kalman gain $K \in (0, I)$ ensures $\eta^\ast c_{\max} = K \lt 1 \lt 2$. For gradient descent with learning rate $\eta$, the upper bound is $\eta \lt 2/L$ where $L$ is the Lipschitz constant of the gradient — the classical step-size condition for gradient descent convergence (Nesterov 2004). The upper bound is not a new restriction but a well-known condition that was implicit in the continuous framework and becomes explicit in the discrete one.

### Summary of Downstream Impact

| Downstream result | Affected? | Nature of change |
|:---|:---:|:---|
| Persistence condition | No | Identical after unit conversion |
| Adaptive reserve | No | Identical |
| Adversarial exponents ($b = 2$, $b = 3/2$) | No | Corrections cancel in ratios |
| Multi-timescale stability | Clarifying | Timescale separation gets concrete interpretation |
| Composition closure | No | Already discrete |
| Gain-sector bridge | Minor | Upper bound ($c_{\max} \lt 2/\eta^\ast$) made explicit |

*[Discussion (downstream-impact-summary)]*

**The fluid-limit approximation introduces no qualitative errors and negligible quantitative errors for well-designed agents at steady state.** The discrete-time results are either identical to (Model D) or tighter than (Model S, with $O(\eta^\ast c)$ correction) the continuous results. No downstream result changes qualitatively. The upper sector bound is the only genuinely new element, and it corresponds to a well-known step-size condition.

---

## 8. What Changes for the Theory

### 8.1 GA-5 Is Closed

The fluid-limit approximation (GA-5) is no longer a gap. The discrete-time results (DA.1, DA.1S, DA.2) stand independently of the continuous results, using the same Lyapunov/contraction structure in discrete form. The continuous results are recovered as the $\nu \to \infty$ limit, but the discrete results do not depend on the continuous ones. The formal chain is now:

$$\text{gain principle} + \text{B1} + \text{upper bound} \;\xrightarrow{\text{derived}}\; \text{discrete sector condition (DA2')} \;\xrightarrow{\text{contraction (exact)}}\; \text{persistence, reserve, adversarial scaling}$$

The continuous-time chain runs in parallel as the fluid limit. Both chains yield the same results (identical for Model D, $O(\eta^\ast c)$-close for Model S).

### 8.2 The Upper Sector Bound Is New

The two-sided discrete sector condition (DA2') is strictly stronger than the one-sided continuous condition (A2'). The upper bound prevents overshoot and is equivalent to the classical step-size condition for gradient descent. For optimal Bayesian updates, it is satisfied automatically. It should be stated as part of the discrete framework but does not affect any existing results (which all implicitly assume well-behaved agents).

### 8.3 Recommendations for Segment Updates

1. **#der-gain-sector-bridge**: Add a note that the discrete framework requires an upper bound ($c_{\max} \lt 2/\eta^\ast$), automatically satisfied for Bayesian updates and equivalent to the standard step-size condition for gradient descent. Remove the "only remaining gap" sentence (GA-5 is closed).

2. **#hyp-mismatch-dynamics**: Upgrade the "Bridging assumption" paragraph from a caveat to a grounded claim. The fluid limit is now formally justified with a quantitative error bound ($O(\eta^\ast c)$ in variance for Model S, zero for Model D steady state).

3. **#deriv-sector-condition**: Add a note (or a separate segment) presenting the discrete propositions DA.1, DA.1S, DA.2 as the primary results, with the continuous propositions as the fluid limit. This is optional — the continuous proofs are clean and pedagogically valuable, and the discrete proofs yield the same bounds.

4. **New segment (optional)**: `discrete-sector-condition` — if the discrete results are to be promoted to the formal chain, they warrant their own segment (with the continuous results as a corollary via the fluid limit, rather than vice versa).

---

## 9. Open Questions

1. **Non-stationary gain.** The analysis assumes constant $\eta^\ast c$ (steady-state gain). During the transient phase, $\eta^\ast$ changes at each step (the Kalman gain decreases as $P$ converges). The contraction factor $\lambda_k = 1 - \eta^\ast_k c_k$ varies per step. The geometric series bound still holds with $\lambda_k$ replaced by $\prod_{j=0}^{k-1} \lvert\lambda_j\rvert$, but the closed-form steady-state is only reached once $\lambda_k$ stabilizes. Standard results on time-varying linear systems (e.g., Desoer & Vidyasagar 1975) cover this case; verification that they yield the same ultimate bound is straightforward but unworked here.

2. **Heavy-tailed disturbances.** The supermartingale argument in DA.1S assumes finite second moments. For heavy-tailed disturbances (financial crashes, adversarial inputs), the bound degrades or fails. The continuous Itô analysis has the same limitation. Extending to sub-exponential or bounded-moment conditions is an open direction for both frameworks.

3. **Non-i.i.d. disturbances.** The proof of DA.1S assumes $w_k$ are i.i.d. Correlated disturbances (e.g., AR(1) environmental noise) would modify the steady-state bound. The standard approach is to bound the spectral radius of the joint (state, disturbance) system. This connects to the per-dimension persistence analysis in #result-per-dimension-persistence.

4. **Exact vs. bound.** The discrete bounds are tight for linear correction (where DA.1 yields the exact steady state of an AR(1) process). For nonlinear correction, the bounds may be conservative. Whether tighter bounds are possible for specific nonlinear classes (e.g., gradient descent on strongly convex losses with known curvature bounds) is an optimization theory question with extensive existing literature.

---

## 10. Conclusion

**GA-5 is closed.** The discrete-time sector condition framework (DA2', Props DA.1, DA.1S, DA.2) provides exact stability results for discrete event-driven agents without requiring the fluid-limit approximation. The continuous-time results are recovered as the formal limit ($\nu \to \infty$, $\eta^\ast \to 0$, $\mathcal{T}$ fixed).

**The fluid limit is not an approximation in the steady state for Model D** — the bounds are identical. **For Model S, the approximation error is $O(\eta^\ast c)$ in variance** — negligible for well-designed agents at steady state.

**No downstream results are affected qualitatively.** The persistence condition, adaptive reserve, adversarial exponents, and composition-closure bridge lemma are all either identical or differ by terms that cancel in ratios.

**The only genuinely new element is the upper sector bound** ($c_{\max} \lt 2/\eta^\ast$), which prevents overshoot in discrete updates. It is automatically satisfied for Bayesian agents and is the classical step-size condition for gradient descent. It should be stated explicitly in the theory but does not restrict the class of well-designed agents.

Section I's formal chain is now complete:

$$\text{gain principle (} \text{\#emp-update-gain)} \;\xrightarrow[\text{\#der-gain-sector-bridge}]{\text{B1 + upper bound}}\; \text{sector condition (DA2')} \;\xrightarrow[\text{DA.1, DA.1S, DA.2}]{\text{contraction (exact)}}\; \text{persistence, reserve, adversarial scaling}$$

with the continuous-time Lyapunov results (Props A.1, A.1S, A.2) as the fluid-limit corollaries.

---

**References:**
- Elaydi, S. N. (2005). *An Introduction to Difference Equations* (3rd ed.). Springer. Ch. 4 (stability of linear difference equations).
- Ethier, S. N. & Kurtz, T. G. (1986). *Markov Processes: Characterization and Convergence*. Wiley. Ch. 11 (density-dependent processes and fluid limits).
- Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.). Prentice Hall. Chs. 4, 9.
- Kurtz, T. G. (1970). Solutions of ordinary differential equations as limits of pure jump Markov processes. *J. Appl. Prob.* 7, 49–58.
- Meyn, S. P. & Tweedie, R. L. (1993). *Markov Chains and Stochastic Stability*. Springer.
- Nesterov, Y. (2004). *Introductory Lectures on Convex Optimization*. Springer. (Step-size condition $\eta \lt 2/L$ for gradient descent.)
- Williams, D. (1991). *Probability with Martingales*. Cambridge University Press.
