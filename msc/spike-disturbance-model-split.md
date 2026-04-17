# Spike: Disturbance Model Split — Deterministic vs. Stochastic

**Status**: Exploratory — working through the consequences of splitting AAD's single disturbance parameter into two distinct models (bounded-deterministic and stochastic zero-mean), deriving the correct results for each, and showing how the split propagates through persistence, adversarial coupling, per-dimension analysis, and operationalization.

**Date**: 2026-04-01

**Motivation**: AAD's mismatch dynamics use a single disturbance term $w(t)$ with bound $\|w(t)\| \leq \rho$, but the theory already contains two incompatible scaling laws:

- Deterministic: $\|\delta\|_{ss} = \rho/\alpha$, adversarial exponent $b = 2$
- Stochastic: $\|\delta\|_{ss} \sim \sigma_w/\sqrt{2\alpha}$, adversarial exponent $b = 3/2$

The `#adversarial-exponent-regimes` segment identifies these as distinct regimes. The `#per-dimension-persistence` segment explicitly notes it mixes deterministic threshold notation with stochastic AR(1) formal expressions. The mismatch ODE (`#mismatch-dynamics`) is ambiguous about what $\rho$ means. This spike resolves the ambiguity by treating the two models as first-class alternatives within the sector-condition framework, deriving each result cleanly, and showing where the current segments conflate the two.

---

## 1. Two Disturbance Models

Both models start from the same dynamics:

$$\frac{d\delta}{dt} = -F(\mathcal{T}, \delta) + w(t)$$

with the same sector condition (GA-3): $\delta^T F(\mathcal{T}, \delta) \geq \alpha \|\delta\|^2$ for $\|\delta\| \leq R$. The models differ only in what they assume about $w(t)$.

### Model D (Deterministic Bounded)

*[Assumption (GA-2, current)]*

$$\|w(t)\| \leq \rho_{\det} \quad \text{for all } t$$

No distributional assumption. The disturbance is arbitrary (possibly adversarial) but norm-bounded. This is the current GA-2.

### Model S (Stochastic Zero-Mean)

*[Assumption (GA-2S, new)]*

$$w(t) \text{ is a stochastic process with } \mathbb{E}[w(t)] = 0, \quad \mathbb{E}[\|w(t)\|^2] = \sigma_w^2$$

Specifically, $w(t)$ is taken as white noise (formally: the increments $w(t)\,dt$ are the differential of a Wiener process scaled by $\sigma_w$). The SDE form is:

$$d\delta = -F(\mathcal{T}, \delta)\,dt + \sigma_w\,dW_t$$

where $W_t$ is a standard Wiener process.

**Why two models, not one.** These are not approximations to each other. They capture structurally different environments:

- **Model D**: the environment changes persistently and directionally. An adversary who maneuvers, an API that drifts, a climate that shifts. The worst case is a disturbance that points consistently against the agent's correction.
- **Model S**: the environment fluctuates unpredictably around a stable mean. Market noise, sensor noise, random perturbations. The disturbance has no preferred direction; its effect accumulates as a random walk.

The `#adversarial-exponent-regimes` segment's domain examples (military maneuvering = drift, market volatility = noise) are exactly this distinction. Making it formal resolves the ambiguity rather than patching it.

---

## 2. Persistence Condition Under Each Model

### 2.1 Model D: Deterministic Persistence (Current Result, Unchanged)

This is Proposition A.1 from `#sector-condition-derivation`, reproduced for reference.

**Lyapunov function:** $V(\delta) = \frac{1}{2}\|\delta\|^2$.

**Derivative along trajectories:**

$$\dot{V} = \delta^T(-F + w) \leq -\alpha\|\delta\|^2 + \rho_{\det}\|\delta\|$$

by (GA-3) and Cauchy-Schwarz.

$\dot{V} < 0$ when $\|\delta\| > \rho_{\det}/\alpha$.

**Result (Model D):**

$$R^*_D = \frac{\rho_{\det}}{\alpha}$$

**Persistence:** $\alpha > \rho_{\det}/R$, i.e., $R^*_D < R$. $\square$

This is exact under (GA-2) + (GA-3). No change needed.

### 2.2 Model S: Stochastic Persistence

The stochastic case requires Itô calculus. The Lyapunov function is the same: $V(\delta) = \frac{1}{2}\|\delta\|^2$.

**Itô's formula** applied to $V(\delta)$ along the SDE $d\delta = -F\,dt + \sigma_w\,dW_t$:

$$dV = \delta^T(-F)\,dt + \delta^T \sigma_w\,dW_t + \frac{1}{2}\sigma_w^2 n\,dt$$

where $n = \dim(\delta)$ (the trace of the diffusion's quadratic variation: $\frac{1}{2}\text{tr}(\sigma_w^2 I_n) = \frac{n}{2}\sigma_w^2$).

Taking expectations (the Itô integral has zero expectation):

$$\frac{d}{dt}\mathbb{E}[V] = \mathbb{E}[\delta^T(-F)] + \frac{n}{2}\sigma_w^2$$

By (GA-3): $\delta^T F \geq \alpha\|\delta\|^2 = 2\alpha V$, so:

$$\frac{d}{dt}\mathbb{E}[V] \leq -2\alpha\,\mathbb{E}[V] + \frac{n}{2}\sigma_w^2$$

This is a linear ODE in $\mathbb{E}[V]$. The steady state:

$$\mathbb{E}[V]_{ss} = \frac{n\sigma_w^2}{4\alpha}$$

Since $V = \frac{1}{2}\|\delta\|^2$, the steady-state mean-square mismatch is:

$$\mathbb{E}[\|\delta\|^2]_{ss} = \frac{n\sigma_w^2}{2\alpha}$$

and the RMS mismatch (the natural scalar summary) is:

$$\|\delta\|_{\text{rms}} = \sqrt{\mathbb{E}[\|\delta\|^2]_{ss}} = \sigma_w\sqrt{\frac{n}{2\alpha}}$$

**For a scalar system ($n = 1$):**

$$\|\delta\|_{\text{rms}} = \frac{\sigma_w}{\sqrt{2\alpha}}$$

This is the $\sigma_w/\sqrt{\alpha}$ scaling that `#adversarial-exponent-regimes` reports — now derived, not empirical.

**Result (Model S, steady-state bound):**

$$R^*_S = \sigma_w\sqrt{\frac{n}{2\alpha}}$$

(interpreting $R^*_S$ as the RMS steady-state mismatch, the natural analog of the deterministic $R^*_D$).

**Persistence (Model S):** The agent persists (in the sense that $R^*_S < R$) iff:

$$\alpha > \frac{n\sigma_w^2}{2R^2}$$

Or equivalently, for the scalar case:

$$\alpha > \frac{\sigma_w^2}{2R^2}$$

**Comparison:**

| | Model D | Model S |
|---|---|---|
| Steady-state mismatch | $\rho_{\det}/\alpha$ | $\sigma_w\sqrt{n/(2\alpha)}$ |
| Scaling with correction | $\propto 1/\alpha$ | $\propto 1/\sqrt{\alpha}$ |
| Persistence condition | $\alpha > \rho_{\det}/R$ | $\alpha > n\sigma_w^2/(2R^2)$ |

**The key difference is the scaling with $\alpha$: deterministic disturbance gives $1/\alpha$; stochastic gives $1/\sqrt{\alpha}$.** Doubling the correction efficiency halves the deterministic steady-state mismatch but only reduces the stochastic steady-state by a factor of $\sqrt{2} \approx 1.41$. Correction is less effective against noise than against drift — this is the fundamental reason the adversarial exponents differ.

### 2.3 Stochastic Persistence as a Probability Bound

The RMS bound above is a mean-square result. For a probabilistic persistence guarantee (the agent stays within $R$ with probability $\geq 1 - \epsilon$), we need a tail bound. Using the supermartingale approach:

Define $Z(t) = e^{2\alpha t}V(\delta(t))$. By Itô's formula:

$$dZ = e^{2\alpha t}\left[2\alpha V + dV\right] = e^{2\alpha t}\left[\frac{n}{2}\sigma_w^2\,dt + \delta^T\sigma_w\,dW_t + (2\alpha V - \delta^T F)\,dt\right]$$

Since $\delta^T F \geq \alpha\|\delta\|^2 = 2\alpha V$, the last term is $\leq 0$. So:

$$dZ \leq e^{2\alpha t}\frac{n}{2}\sigma_w^2\,dt + e^{2\alpha t}\delta^T\sigma_w\,dW_t$$

Taking expectations (dropping the martingale term):

$$\mathbb{E}[Z(t)] \leq Z(0) + \frac{n\sigma_w^2}{4\alpha}(e^{2\alpha t} - 1)$$

Therefore:

$$\mathbb{E}[V(\delta(t))] \leq V(\delta(0))e^{-2\alpha t} + \frac{n\sigma_w^2}{4\alpha}$$

This gives exponential convergence of $\mathbb{E}[V]$ to the steady state $n\sigma_w^2/(4\alpha)$, confirming the mean-square result. For the tail bound, apply Markov's inequality at steady state:

$$P(\|\delta\| > R) = P(\|\delta\|^2 > R^2) \leq \frac{\mathbb{E}[\|\delta\|^2]_{ss}}{R^2} = \frac{n\sigma_w^2}{2\alpha R^2}$$

So the agent stays within $R$ with probability $\geq 1 - \epsilon$ provided:

$$\alpha \geq \frac{n\sigma_w^2}{2\epsilon R^2}$$

For $\epsilon = 0.05$ (95% probability), this requires $\alpha \geq 10 n\sigma_w^2/R^2$, which is 10x the mean-square persistence condition. This makes sense: Model D gives a hard guarantee (never exceeds $R^*_D$); Model S gives a probabilistic guarantee (exceeds $R^*_S$ sometimes, stays within $R$ with high probability).

**Remark.** Markov's inequality gives a loose bound. For Gaussian or sub-Gaussian processes, exponential concentration (e.g., via the moment-generating function of $V$) would give tighter results. The Ornstein-Uhlenbeck process (the linear case of Model S) has a Gaussian stationary distribution, so exact tail probabilities are available. The Markov bound is the general one that holds under (GA-3) alone.

---

## 3. Adversarial Exponent Under Each Model

### 3.1 Model D: Exponent $b = 2$ (Current Result, Derived)

From `#adversarial-tempo-advantage`, reproduced for clarity.

**Coupling model:** $\rho_B = \rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A$ (deterministic drift coupling).

**Steady state (Model D):** $\|\delta\|_{ss} = \rho/\alpha$. In the linear case, $\alpha = \mathcal{T}$.

$$\|\delta_B\|_{ss} = \frac{\rho_{\text{base}} + \gamma_A \mathcal{T}_A}{\mathcal{T}_B}$$

**Coupling-dominant limit** ($\gamma \mathcal{T} \gg \rho_{\text{base}}$, symmetric coupling $\gamma_A = \gamma_B$):

$$\frac{\|\delta_B\|_{ss}}{\|\delta_A\|_{ss}} = \frac{\gamma_A \mathcal{T}_A / \mathcal{T}_B}{\gamma_B \mathcal{T}_B / \mathcal{T}_A} = \frac{\gamma_A}{\gamma_B}\left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^2 \to \left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^2$$

**Exponent: $b = 2$.** $\square$

### 3.2 Model S: Exponent $b = 3/2$ (New Derivation)

**Coupling model (stochastic):** $\sigma_B = \sigma_{\text{base}} + \gamma_A \cdot \mathcal{T}_A$ (noise-scale coupling: the adversary's tempo increases the unpredictability of disturbances to $B$, not their systematic direction).

**Steady state (Model S, scalar $n = 1$, linear $\alpha = \mathcal{T}$):**

$$\|\delta\|_{\text{rms}} = \frac{\sigma}{\sqrt{2\mathcal{T}}}$$

Substituting the coupled noise scales:

$$\|\delta_B\|_{\text{rms}} = \frac{\sigma_{\text{base}} + \gamma_A \mathcal{T}_A}{\sqrt{2\mathcal{T}_B}}, \qquad \|\delta_A\|_{\text{rms}} = \frac{\sigma_{\text{base}} + \gamma_B \mathcal{T}_B}{\sqrt{2\mathcal{T}_A}}$$

Taking the ratio:

$$\frac{\|\delta_B\|_{\text{rms}}}{\|\delta_A\|_{\text{rms}}} = \frac{(\sigma_{\text{base}} + \gamma_A \mathcal{T}_A)\sqrt{\mathcal{T}_A}}{(\sigma_{\text{base}} + \gamma_B \mathcal{T}_B)\sqrt{\mathcal{T}_B}}$$

**Coupling-dominant limit** ($\gamma \mathcal{T} \gg \sigma_{\text{base}}$, symmetric coupling):

$$\frac{\|\delta_B\|_{\text{rms}}}{\|\delta_A\|_{\text{rms}}} \to \frac{\gamma_A \mathcal{T}_A \sqrt{\mathcal{T}_A}}{\gamma_B \mathcal{T}_B \sqrt{\mathcal{T}_B}} = \frac{\gamma_A}{\gamma_B} \cdot \left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^{3/2}$$

**Exponent: $b = 3/2$.** $\square$

**Why 3/2, not 2.** The $1/\sqrt{\alpha}$ scaling of Model S (vs. $1/\alpha$ for Model D) removes one power from the denominator. The numerator contributes one power of $\mathcal{T}_A$ from the coupling; the denominator contributes $\sqrt{\mathcal{T}_B}$ from the noise averaging. Net: $\mathcal{T}_A^1 \cdot \mathcal{T}_A^{1/2} / \mathcal{T}_B^{1/2+1} = (\mathcal{T}_A/\mathcal{T}_B)^{3/2}$.

More precisely: the denominator contributes $\mathcal{T}_B^{1/2}$ from the steady-state formula (not $\mathcal{T}_B^1$ as in Model D). Combine with the coupling numerator ($\mathcal{T}_A$) and the $A$-side denominator ($1/\mathcal{T}_A^{1/2}$), and you get $\mathcal{T}_A^{3/2} / \mathcal{T}_B^{3/2}$.

### 3.3 Regime 3: Non-Coupling-Dominant Degradation

When $\rho_{\text{base}}$ (or $\sigma_{\text{base}}$) is comparable to the coupling term, the base disturbance acts as a floor. In the limit $\rho_{\text{base}} \gg \gamma \mathcal{T}$, the coupling becomes a perturbation and the mismatch ratio is dominated by the $\mathcal{T}_A/\mathcal{T}_B$ (or $\sqrt{\mathcal{T}_A/\mathcal{T}_B}$) factor from the agent's own correction, giving:

| Regime | Model D | Model S |
|---|---|---|
| Coupling-dominant | $b = 2$ | $b = 3/2$ |
| Non-coupling-dominant | $b \to 1$ | $b \to 1/2$ |

The transition is smooth and parameterized by $\gamma\mathcal{T}/\rho_{\text{base}}$ (or $\gamma\mathcal{T}/\sigma_{\text{base}}$). This matches the simulation table in `#adversarial-exponent-regimes` exactly.

**Summary.** The exponent is:

$$b = b_{\text{coupling}} + b_{\text{correction}} - 1$$

where $b_{\text{coupling}} = 1$ (from the coupling numerator, same for both models) and $b_{\text{correction}} = 1$ (Model D) or $1/2$ (Model S). In the coupling-dominant limit, $b = 1 + b_{\text{correction}}$. In the non-coupling-dominant limit, $b \to b_{\text{correction}}$.

---

## 4. Per-Dimension Persistence Under Each Model

### 4.1 Model D: Per-Dimension Deterministic

For a $d$-dimensional system with diagonal correction $F_k(\delta_k) = \alpha_k \delta_k$ and per-dimension bounded disturbance $|w_k(t)| \leq \rho_k$:

$$|\delta_k|_{ss} = \frac{\rho_k}{\alpha_k}$$

Persistence on dimension $k$: $\alpha_k > \rho_k / R_k$.

In the linear operational form: $\mathcal{T}_k > \rho_k / \delta_{\text{critical},k}$.

This is the deterministic per-dimension threshold stated in `#per-dimension-persistence`'s summary. It is exact under Model D.

### 4.2 Model S: Per-Dimension Stochastic (AR(1))

This is what the formal expression in `#per-dimension-persistence` actually derives. For the discrete AR(1) process:

$$\delta_{k,t+1} = (1 - \eta_k)\delta_{k,t} + w_{k,t}, \quad w_{k,t} \sim N(0, \rho_k^2)$$

The stationary variance (for $|1 - \eta_k| < 1$, i.e., $0 < \eta_k < 2$):

$$\text{Var}[\delta_k] = \frac{\rho_k^2}{1 - (1 - \eta_k)^2} = \frac{\rho_k^2}{2\eta_k - \eta_k^2}$$

For small $\eta_k$: $\text{Var}[\delta_k] \approx \rho_k^2 / (2\eta_k)$.

Since $\delta_k$ is Gaussian at stationarity, $|\delta_k|$ is half-normal:

$$\mathbb{E}[|\delta_k|] = \sqrt{\text{Var}[\delta_k]} \cdot \sqrt{2/\pi} = \frac{\rho_k}{\sqrt{2\eta_k - \eta_k^2}} \cdot \sqrt{2/\pi}$$

This is precisely the formula in the `#per-dimension-persistence` formal expression. For small $\eta_k$:

$$\mathbb{E}[|\delta_k|] \approx \frac{\rho_k}{\sqrt{2\eta_k}} \cdot \sqrt{2/\pi}$$

**Persistence (Model S, per-dimension):** The condition $\mathbb{E}[|\delta_k|] < \delta_{\text{critical},k}$ gives:

$$\eta_k > \frac{\rho_k^2}{\pi \cdot \delta_{\text{critical},k}^2}$$

(using the small-$\eta_k$ approximation and solving).

Or as a probability bound: $P(|\delta_k| > \delta_{\text{critical},k}) < \epsilon$ requires (from the Gaussian tail):

$$\frac{\delta_{\text{critical},k}}{\sqrt{\rho_k^2/(2\eta_k)}} > z_{1-\epsilon}$$

i.e., $\eta_k > \rho_k^2 \cdot z_{1-\epsilon}^2 / (2\delta_{\text{critical},k}^2)$, where $z_{1-\epsilon}$ is the Gaussian quantile.

### 4.3 The Regime-Mixing Diagnosis

The `#per-dimension-persistence` segment has exactly the conflict identified above:

- **Summary/threshold**: states $\mathcal{T}_k > \rho_k / \delta_{\text{critical},k}$ — this is the **Model D** condition.
- **Formal expression**: derives $\mathbb{E}[|\delta_k|] = \rho_k/\sqrt{2\eta_k - \eta_k^2} \cdot \sqrt{2/\pi}$ — this is the **Model S** result (from AR(1) stationarity).

These are not the same. The Model D threshold is linear in $\rho_k$; the Model S steady-state is $\rho_k/\sqrt{\eta_k}$, not $\rho_k/\eta_k$. The 4-significant-figure simulation match validates the Model S formula (because the simulation uses Gaussian noise, i.e., Model S). The deterministic threshold in the summary is stated by analogy, not derived from the stochastic model.

**Resolution:** The per-dimension segment should present both:

1. **Model D per-dimension:** $\alpha_k > \rho_k/R_k$ (or operationally $\mathcal{T}_k > \rho_k/\delta_{\text{critical},k}$). This is the deterministic worst-case bound — exact under bounded disturbance.

2. **Model S per-dimension:** $\eta_k > c \cdot \rho_k^2/\delta_{\text{critical},k}^2$ where $c$ depends on the probability guarantee. This is the stochastic result — exact for Gaussian (AR(1)) disturbance.

The qualitative conclusion is the same for both: the weak dimension is the bottleneck. The quantitative forms differ because of the $1/\alpha$ vs. $1/\sqrt{\alpha}$ scaling.

---

## 5. Continuous-Time Connection: Ornstein-Uhlenbeck

The linear case of Model S (i.e., $F(\mathcal{T}, \delta) = \mathcal{T}\delta$) is the Ornstein-Uhlenbeck process:

$$d\delta = -\mathcal{T}\delta\,dt + \sigma_w\,dW_t$$

This has a well-known stationary distribution: $\delta \sim N(0, \sigma_w^2/(2\mathcal{T}))$.

The discrete AR(1) process $\delta_{t+1} = (1 - \eta)\delta_t + w_t$ is the Euler-Maruyama discretization of the OU process, with $\eta = \mathcal{T}\Delta t$ and $\rho = \sigma_w\sqrt{\Delta t}$. The stationary variance of the AR(1) is $\rho^2/(2\eta - \eta^2)$, which for small $\eta$ gives $\rho^2/(2\eta) = \sigma_w^2\Delta t/(2\mathcal{T}\Delta t) = \sigma_w^2/(2\mathcal{T})$, matching the OU result exactly.

This confirms that the discrete AR(1) simulations and the continuous stochastic Lyapunov analysis give the same scaling — the $1/\sqrt{\alpha}$ result is not a discretization artifact.

---

## 6. Summary: How the Split Propagates

| Segment | Current State | Model D (deterministic) | Model S (stochastic) |
|---|---|---|---|
| `#mismatch-dynamics` | Single $\rho$, ambiguous | $\|\delta\|_{ss} = \rho_{\det}/\mathcal{T}$ | $\|\delta\|_{\text{rms}} = \sigma_w/\sqrt{2\mathcal{T}}$ |
| `#sector-condition-stability` | Derives $R^* = \rho/\alpha$ under GA-2 | Unchanged | Add stochastic result: $R^*_S = \sigma_w\sqrt{n/(2\alpha)}$ |
| `#sector-condition-derivation` | Props A.1, A.2 under bounded disturbance | Unchanged | Add Prop A.1S (stochastic Lyapunov) |
| `#persistence-condition` | $\alpha > \rho/R$ | Unchanged | $\alpha > n\sigma_w^2/(2R^2)$ |
| `#adversarial-tempo-advantage` | Derives $b = 2$, notes $b = 3/2$ as empirical | Unchanged | Derive $b = 3/2$ from Model S |
| `#adversarial-exponent-regimes` | Empirical regime table | Label as Model D | Label as Model S; derivations now available |
| `#per-dimension-persistence` | Mixes deterministic threshold with stochastic formula | State D threshold cleanly | State S formula cleanly; resolve regime-mixing note |
| `#adversarial-destabilization` | Deterministic coupling only | Unchanged | Discuss stochastic extension (probabilistic destabilization) |
| `#simulation-results` | Notes the two regimes post-hoc | Frame as Model D validation | Frame as Model S validation |
| `NOTATION.md` | GA-2 only | Keep as GA-2 | Add GA-2S |

---

## 7. Proposed Segment Modifications

### 7.1 `NOTATION.md`: Add GA-2S

Add to Global Assumptions table:

> | GA-2S | **Stochastic disturbance.** $w(t)$ is zero-mean with $\mathbb{E}[\|w(t)\|^2] = \sigma_w^2$. | `#sector-condition-stability` (stochastic variant), `#persistence-condition` |

### 7.2 `#mismatch-dynamics`: Split the steady state

The Discussion section already notes the stochastic exponent. The change is to the formal expression: add a parallel steady-state for Model S next to the existing (Model D) one:

> **Steady state (stochastic, $d\delta = -\mathcal{T}\delta\,dt + \sigma_w\,dW_t$):**
>
> $$\|\delta\|_{\text{rms}} = \frac{\sigma_w}{\sqrt{2\mathcal{T}}}$$
>
> Steady-state mismatch scales as the square root of the disturbance-to-correction ratio, not the ratio itself.

Label the existing steady state as "deterministic" explicitly.

### 7.3 `#sector-condition-stability` and `#sector-condition-derivation`: Add Proposition A.1S

Add a stochastic counterpart to Prop A.1:

> **Proposition A.1S (Stochastic Bounded Mismatch).** Under (A1), (A2'), (A3), with stochastic disturbance (GA-2S), the mismatch $\delta(t)$ satisfies $\mathbb{E}[\|\delta(t)\|^2] \leq \|\delta(0)\|^2 e^{-2\alpha t} + n\sigma_w^2/(2\alpha)$ for all $t$. The agent persists in the mean-square sense iff $\alpha > n\sigma_w^2/(2R^2)$.

The derivation is the stochastic Lyapunov argument from Section 2.2 of this spike.

### 7.4 `#persistence-condition`: Present both forms

Add a "Stochastic form" subsection parallel to the current linear operational form:

> **Stochastic operational form (Model S):** Under GA-2S with linear correction,
>
> $$\mathcal{T} > \frac{n\sigma_w^2}{2R^2}$$
>
> The per-dimension version: $\eta_k > c \cdot \rho_k^2/\delta_{\text{critical},k}^2$.

### 7.5 `#adversarial-tempo-advantage`: Derive $b = 3/2$

Replace "the stochastic case is not yet derived from the stochastic mismatch dynamics in full generality" (Working Notes) with the derivation from Section 3.2 above. Move it into the formal expression as a second case.

### 7.6 `#adversarial-exponent-regimes`: Upgrade epistemic status

Change "empirical" to "exact conditional on disturbance model" for the regime 1 and regime 2 exponents. Both are now derived:

- Regime 1 ($b = 2$): from Model D steady state + coupling model.
- Regime 2 ($b = 3/2$): from Model S steady state + coupling model.

Regime 3 (non-coupling-dominant) remains empirical in the sense that the smooth interpolation is observed, though the asymptotic limits ($b \to 1$ and $b \to 1/2$) are derived.

### 7.7 `#per-dimension-persistence`: Resolve regime mixing

The epistemic status section already identifies the problem. The fix:

1. Rename the summary threshold to "deterministic per-dimension persistence" and label it (Model D).
2. Label the AR(1) formal expression as "stochastic per-dimension steady state" (Model S).
3. State clearly that the 4-significant-figure match validates Model S, not Model D.
4. Derive the stochastic persistence threshold: $\eta_k > \rho_k^2/(c \cdot \delta_{\text{critical},k}^2)$ where $c$ depends on the tolerance.

This resolves the "regime mixing" note in the epistemic status.

---

## 8. What This Does NOT Resolve

1. **Which model is appropriate for a given domain.** This is always an empirical question. The theory provides both tools; the user must assess whether their environment is better modeled as persistent drift or zero-mean noise. Mixed environments use the interpolation from `#adversarial-exponent-regimes` Variant B.

2. **Heavy-tailed disturbances.** Both Model D and Model S assume bounded second moments (or bounded $\|w\|$ for Model D). Financial crises, strategic surprise, and ecological catastrophe involve heavy tails. These require separate treatment (e.g., stable distributions, input-to-state stability in probability with moment conditions relaxed).

3. **Time-correlated disturbances.** Model S assumes white noise ($w(t)$ uncorrelated across time). Colored noise (e.g., Ornstein-Uhlenbeck disturbance, where the disturbance itself has persistence) would change the scaling — the steady-state mismatch depends on the disturbance autocorrelation time. This is a natural extension but not addressed here.

4. **The nonlinear stochastic case in full generality.** The Itô-Lyapunov argument in Section 2.2 holds for any sector-bounded $F$, giving the $\mathbb{E}[V]$ bound. But the distributional characterization (Gaussian stationary distribution, exact tail bounds) only holds for the linear (OU) case. For nonlinear $F$, the mean-square bound is all we get without additional assumptions on the correction function's structure.

5. **The coupled stochastic Lyapunov analysis.** `#adversarial-destabilization` uses a one-sided Lyapunov argument (treats $\mathcal{T}_A$ as exogenous). The stochastic version of this (probabilistic destabilization: "Agent $A$ can push Agent $B$ above $R_B$ with probability $\geq 1 - \epsilon$") is not worked out here.

---

## 9. Assessment

**Effort required.** The modifications to existing segments are mostly labeling and restructuring, not new mathematics. The only new mathematical content is:

- Prop A.1S (stochastic Lyapunov) — standard Itô-Lyapunov, about 10 lines of derivation.
- The $b = 3/2$ derivation — straightforward substitution once the Model S steady state is in place.
- The stochastic per-dimension persistence threshold — follows from the AR(1) stationarity formula already in the segment.

**Epistemic upgrade.** The split resolves the largest internal inconsistency in Section I. The `#adversarial-exponent-regimes` observation becomes a derived result. The `#per-dimension-persistence` regime-mixing note is resolved. The `#mismatch-dynamics` ambiguity about $\rho$ is eliminated.

**What stays the same.** The sector-condition framework, the deterministic persistence condition, the adversarial destabilization threshold, the effects spiral, the adaptive reserve, the $\alpha$/$\mathcal{T}$ relationship — all unchanged. Model D is the current theory; Model S is an addition, not a replacement.

---

## 10. Recommended Promotion Order

1. **Add GA-2S to `NOTATION.md`** — one line, unblocks everything.
2. **Add Prop A.1S to `#sector-condition-derivation`** — the mathematical foundation.
3. **Update `#sector-condition-stability` summary** — to reference both D and S results.
4. **Update `#mismatch-dynamics`** — split the steady state, label the existing as deterministic.
5. **Update `#persistence-condition`** — add stochastic form.
6. **Derive $b = 3/2$ in `#adversarial-tempo-advantage`** — upgrade from empirical to derived.
7. **Upgrade `#adversarial-exponent-regimes`** — label regimes as Model D/S, upgrade epistemic status.
8. **Resolve `#per-dimension-persistence`** — fix regime mixing.
9. **Update `#simulation-results`** — frame Model D/S validation explicitly.

Steps 1-3 are foundational. Steps 4-8 are consequences. Step 9 is editorial.
