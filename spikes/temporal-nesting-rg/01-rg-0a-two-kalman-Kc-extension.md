# RG-0a: Two-Kalman Closure Defect under Timescale Ratio $K_c > 1$

**Status**: in progress — Case B (heterogeneous steady state) derived; Case A (homogeneous transient) and the iterated-coarse-graining test are open.
**Date opened**: 2026-05-09
**Depends on**: `00-brief.md`, `spikes/spike-composition-correlated-kalman.md`, `#form-composition-closure`, `#example-kalman`, `#der-temporal-nesting`.

**Goal**. Test the load-bearing prediction of the RG framing (`00-brief.md` §4): that under coarse-graining flow $K_c \to \infty$, AAT's closure defect $\varepsilon^*$ behaves as RG-flow distance from a fixed point. Specifically, that homogeneous (fixed-point-respecting) sub-agent collections sit at $\varepsilon^* = 0$ for all $K_c$, and that heterogeneity perturbs away from the fixed point in a way whose $K_c$-dependence is structurally informative.

---

## 1. Setup

Two scalar Kalman filters, possibly heterogeneous in their steady-state parameters, observe components of a bivariate random walk. Notation follows `spikes/spike-composition-correlated-kalman.md` §1–§2 except where heterogeneity demands $i$-indexed parameters.

### 1.1 Environment

State $(\omega_{1,t}, \omega_{2,t})$ evolving as

$$\begin{pmatrix} \omega_{1,t+1} \\ \omega_{2,t+1} \end{pmatrix} = \begin{pmatrix} \omega_{1,t} \\ \omega_{2,t} \end{pmatrix} + \begin{pmatrix} w_{1,t} \\ w_{2,t} \end{pmatrix}, \qquad w_t \sim \mathcal{N}(0, Q)$$

with $Q = \text{diag}(q_1, q_2)$. (We take $\rho_{\text{corr}} = 0$ to isolate the heterogeneity effect; the cross-correlated case adds the $C_{+-}$ term and is a follow-up.)

Agent $i$ observes $o_{i,t} = \omega_{i,t} + v_{i,t}$ with $v_{i,t} \sim \mathcal{N}(0, r_i)$, mutually independent across $i$ and $t$.

### 1.2 Micro-dynamics (steady state)

Each agent runs an independent scalar Kalman filter and reaches its own steady-state gain $K_i^*$:

$$P_i^* = \frac{-q_i + \sqrt{q_i^2 + 4 q_i r_i}}{2}, \qquad K_i^* = \frac{P_i^* + q_i}{P_i^* + q_i + r_i}$$

Heterogeneity: in general $K_1^* \neq K_2^*$ when $q_1/r_1 \neq q_2/r_2$ (the per-agent SNRs differ). Define $\lambda_i = 1 - K_i^*$, the per-agent persistence factor. Both $\lambda_i \in (0, 1)$.

Micro-update at steady state:

$$\hat\omega_{i, t+1} = \lambda_i \hat\omega_{i, t} + K_i^* o_{i, t+1}$$

### 1.3 Macro-projection ($\Lambda_x$ and $\Lambda_o$)

We use the **sum-projection** that genuinely reduces dimension (satisfying (P3) of `#form-composition-closure`):

$$\Lambda_x : \mathbb{R}^2 \to \mathbb{R}, \quad \Lambda_x(\hat\omega_1, \hat\omega_2) = \frac{\hat\omega_1 + \hat\omega_2}{\sqrt 2} \equiv X_c$$

The orthogonal direction (in the null space of $\Lambda_x$) is

$$X_- \equiv \frac{\hat\omega_1 - \hat\omega_2}{\sqrt 2}$$

so $\hat\omega_1 = (X_c + X_-)/\sqrt 2$ and $\hat\omega_2 = (X_c - X_-)/\sqrt 2$. The pair $(X_c, X_-)$ is an orthonormal rotation of $(\hat\omega_1, \hat\omega_2)$.

For the observation aggregation $\Lambda_o : \mathbb{R}^{2 K_c} \to \mathbb{R}$, we restrict to **linear combinations of the observation window** of the form

$$\Lambda_o(o^{(1)}, \ldots, o^{(K_c)}) = \sum_{k=0}^{K_c - 1} c_k \cdot \frac{o_{1, mK_c - k} + o_{2, mK_c - k}}{\sqrt 2}$$

i.e., aggregations that respect the $1 \leftrightarrow 2$ symmetry of the projection. Asymmetric aggregations could in principle access $X_-$-direction information, but only at the cost of breaking $\Lambda_x$'s symmetry — we treat them as a separate case in §6.

### 1.4 Admissible macro-dynamics

The macro-update has the AAT-shape required by (A1)–(A4) of `#form-composition-closure`. For Kalman-style linear correction:

$$f_c(X_{c, m-1}, o_{c, m}) = \mu_c X_{c, m-1} + (1 - \mu_c) o_{c, m}$$

where $\mu_c \in [0, 1)$ is the macro-persistence factor, $1 - \mu_c$ is the macro-gain on the aggregated observation, and $o_{c, m} = \Lambda_o(\cdot)$. The macro-state space is one-dimensional, the macro-update is linear-Gaussian, and the macro-mismatch $\delta_c = o_c - X_c$ is well-defined.

This is admissible: linear correction with positive gain satisfies (A4) (sector-bounded with $\alpha_c = 1 - \mu_c$); the mismatch is well-defined per (A2); the macro-tempo is $\mathcal T_c = 1 \cdot (1 - \mu_c) = 1 - \mu_c$ per (A3); the AAT-form is preserved per (A1).

### 1.5 The closure defect (per-macro-step)

Per `#form-composition-closure` §2, the per-macro-step state-component closure defect is

$$\varepsilon_x = \mathbb{E}\big[\, \big| \Lambda_x(X_{\text{micro}, m K_c}) - f_c(\Lambda_x(X_{\text{micro}, (m-1)K_c}),\, \Lambda_o(\cdot)) \big| \,\big]$$

We minimize over $\mu_c$ and the aggregation weights $\{c_k\}$ to obtain $\varepsilon^*$.

---

## 2. Case B — Heterogeneous gains, steady state

This is the most direct test of the RG framing. Both filters in their own steady states, with $K_1^* \neq K_2^*$. We derive $\varepsilon^*(K_c)$ in closed form.

### 2.1 Micro-evolution over a macro-window

Iterating the steady-state micro-update $K_c$ times:

$$\hat\omega_{i, mK_c} = \lambda_i^{K_c}\, \hat\omega_{i, (m-1)K_c} + K_i^* \sum_{k=0}^{K_c - 1} \lambda_i^k\, o_{i, mK_c - k}$$

*[Definition (per-agent $K_c$-step kernel)]* Each agent's $K_c$-step update has memory factor $\lambda_i^{K_c}$ on the previous macro-boundary state, and weights its observation window with the geometric series $\{K_i^* \lambda_i^k\}_{k=0}^{K_c - 1}$.

### 2.2 Rotation to the macro/orthogonal basis

For any pair of coefficients $(a_1, a_2)$ acting on $(\hat\omega_1, \hat\omega_2)$:

$$\frac{1}{\sqrt 2}(a_1 \hat\omega_1 + a_2 \hat\omega_2) = \bar a\, X_c + \tilde a\, X_-$$

where $\bar a = (a_1 + a_2)/2$ (symmetric average) and $\tilde a = (a_1 - a_2)/2$ (anti-symmetric difference).

Apply this to the memory term with $(a_1, a_2) = (\lambda_1^{K_c}, \lambda_2^{K_c})$:

$$\frac{1}{\sqrt 2}\big[\lambda_1^{K_c} \hat\omega_{1, (m-1)K_c} + \lambda_2^{K_c} \hat\omega_{2, (m-1)K_c}\big] = \bar\lambda_{K_c} X_{c, (m-1)K_c} + \tilde\lambda_{K_c} X_{-, (m-1)K_c}$$

where

$$\bar\lambda_{K_c} \equiv \frac{\lambda_1^{K_c} + \lambda_2^{K_c}}{2}, \qquad \tilde\lambda_{K_c} \equiv \frac{\lambda_1^{K_c} - \lambda_2^{K_c}}{2}$$

Apply the same rotation to the observation term. For each lag $k$, the coefficient on $(o_{1, mK_c - k}, o_{2, mK_c - k})$ is $(K_1^* \lambda_1^k, K_2^* \lambda_2^k)$. Define

$$\overline{K\lambda^k} \equiv \frac{K_1^* \lambda_1^k + K_2^* \lambda_2^k}{2}, \qquad \widetilde{K\lambda^k} \equiv \frac{K_1^* \lambda_1^k - K_2^* \lambda_2^k}{2}$$

Then the obs-term contribution is

$$\sum_{k=0}^{K_c - 1}\Big[ \overline{K\lambda^k}\, O_{c, mK_c - k} + \widetilde{K\lambda^k}\, O_{-, mK_c - k} \Big]$$

with $O_c = (o_1 + o_2)/\sqrt 2$ and $O_- = (o_1 - o_2)/\sqrt 2$.

### 2.3 Decomposition of the true macro-update

Combining 2.1 and 2.2:

$$X_{c, mK_c} = \underbrace{\bar\lambda_{K_c} X_{c, (m-1)K_c} + \sum_{k=0}^{K_c - 1} \overline{K\lambda^k}\, O_{c, mK_c - k}}_{\text{symmetric / accessible to } f_c} + \underbrace{\tilde\lambda_{K_c} X_{-, (m-1)K_c} + \sum_{k=0}^{K_c - 1} \widetilde{K\lambda^k}\, O_{-, mK_c - k}}_{\text{anti-symmetric / inaccessible to } f_c \text{ under symmetric } \Lambda_o}$$

The first bracket lies in the column space of $(X_{c, (m-1)K_c}, O_{c, \cdot})$ — the macro-update can match it exactly with the optimal choice of $\mu_c$ and $\{c_k\}$. The second bracket lies in the **orthogonal direction $X_-$**, which the macro-state cannot represent and the symmetric $\Lambda_o$ cannot access.

### 2.4 Optimal symmetric macro-update

*[Derived (best-symmetric-macro)]* The macro-update that minimizes $\varepsilon_x^2$ within the symmetric class chooses

$$\mu_c^* = \bar\lambda_{K_c}, \qquad c_k^* = \overline{K\lambda^k} \text{ for } k = 0, 1, \ldots, K_c - 1$$

i.e., it averages the per-agent kernels coordinate-by-coordinate. The leftover error is **exactly the anti-symmetric component**:

$$X_{c, mK_c} - f_c(X_{c, (m-1)K_c}, \Lambda_o(\cdot))\Big|_{\text{optimal}} = \tilde\lambda_{K_c} X_{-, (m-1)K_c} + \sum_{k=0}^{K_c - 1} \widetilde{K\lambda^k}\, O_{-, mK_c - k}$$

This is the closure defect (in absolute terms, before taking expectations).

### 2.5 Closed-form $\varepsilon^*(K_c)$

Taking expectations: $X_-$ at steady state has variance $V_-$ (computed below); $O_-$ has variance $V_{O_-} = V_- + (r_1 + r_2)/2 - \text{cross terms}$. Under our setup with $\rho_\text{corr} = 0$ and uncorrelated observation noises, the residuals at different lags decouple. Working out the second moment:

$$\boxed{\varepsilon_x^{*2}(K_c) = \tilde\lambda_{K_c}^2 \cdot V_- + \sum_{k=0}^{K_c - 1} \widetilde{K\lambda^k}^2 \cdot V_{O_-, k}}$$

with explicit factors:

- $\tilde\lambda_{K_c} = (\lambda_1^{K_c} - \lambda_2^{K_c})/2$
- $\widetilde{K\lambda^k} = (K_1^* \lambda_1^k - K_2^* \lambda_2^k)/2$
- $V_- = \mathrm{Var}(X_-)$ — steady-state variance of the orthogonal estimator difference
- $V_{O_-, k} = \mathrm{Var}(O_{-, mK_c - k})$ — observation-window difference variance at lag $k$

The second sum involves observation-noise terms that decay with $\lambda_i^k$. For the leading $K_c$-dependence, the first term dominates when both filters have similar $V_-$ contributions.

### 2.6 Behavior in $K_c$

The key quantity is $\tilde\lambda_{K_c}^2$:

- **At $K_c = 1$**: $\tilde\lambda_1 = (\lambda_1 - \lambda_2)/2 = -(\Delta K^*/2)$, where $\Delta K^* = K_1^* - K_2^*$. Then $\tilde\lambda_1^2 = (\Delta K^*/2)^2$. This recovers the $K_c = 1$ formula in `#form-composition-closure` Working Notes: $\varepsilon_x^2 \propto (\Delta K^*/2)^2$.
- **At $K_c \to \infty$**: both $\lambda_i^{K_c} \to 0$ since $\lambda_i \in (0, 1)$. Hence $\tilde\lambda_{K_c} \to 0$. The defect goes to zero.
- **Asymptotic rate**: assuming WLOG $\lambda_1 > \lambda_2$ (the larger memory factor / smaller gain dominates),
  $$\tilde\lambda_{K_c} = \frac{\lambda_1^{K_c} - \lambda_2^{K_c}}{2} \sim \frac{\lambda_1^{K_c}}{2} \quad \text{as } K_c \to \infty$$
  so the closure defect decays at rate $\lambda_1^{K_c} = (1 - K_\text{min}^*)^{K_c}$ — the **slower filter's persistence factor**.

### 2.7 Verdict for Case B

*[Result (heterogeneous-Kc-flow)]* The heterogeneous-gain closure defect under the symmetric sum-projection satisfies

$$\varepsilon_x^*(K_c) = O\big( (1 - K_\text{min}^*)^{K_c} \big) \to 0 \text{ as } K_c \to \infty$$

with leading coefficient set by the per-agent gain difference and the orthogonal-direction variance.

**This is the central RG-0a result.** Heterogeneity *does* flow to zero under coarse-graining, contrary to the brief's first-cut prediction that heterogeneity would be a relevant operator. The structural mismatch is **irrelevant** in the strict RG sense — the AAT fixed point is attractive even from heterogeneous starts.

---

## 3. Reading the result against the RG framing

### 3.1 What this confirms

- The AAT fixed point ($\varepsilon^* = 0$, perfect closure) is a **stable attractor** under $K_c$-flow on this case. Sufficient timescale separation absorbs structural heterogeneity (within this admissibility-and-symmetry class).
- The flow has a definite **rate**: $(1 - K_\text{min}^*)^{K_c}$, set by the *slower* sub-agent's persistence factor. This is a non-trivial structural prediction. It says: composition closure is rate-limited by the slowest sub-agent's adaptation, not by the average. (Connects naturally to weakest-link composition results; cf. `#form-composition-closure` weakest-link bound and `#deriv-critical-mass-composition`.)
- The **mechanism of the residual** is structural: the leftover error lives in the projection's null space ($X_-$), which the symmetric macro-update cannot access. This is recognizably the *information-discarded-by-projection* picture.

### 3.2 What this disconfirms (or refines)

The brief's first-cut prediction was a sharp irrelevant/relevant separation: transient defects flow to zero (irrelevant), structural defects persist (relevant). **That sharp dichotomy is wrong, at least for this case.** Both transient and structural defects flow to zero under sufficient $K_c$.

This forces a refinement of what "RG fixed point" means here:
- It is a fixed point in the form-preservation sense (AAT shape preserved under $\Lambda$).
- It is not yet shown to admit relevant operators in the classical RG sense (perturbations that grow under flow).
- The flow may be *globally attracting* on the cases tested so far, which is a stronger statement than classical RG (where one expects a critical surface separating basins).

### 3.3 What would actually be relevant

Candidates for genuinely relevant operators (perturbations that resist $K_c$-flow):

1. **World non-stationarity at timescale $\sim K_c$.** If $\omega_t$ itself drifts on the macro-timescale, no aggregation can summarize the window — this would survive $K_c \to \infty$. (Outside Case B's stationary setup.)
2. **Asymmetric $\Lambda_o$**. Allowing observation aggregations that access $X_-$-direction information reduces $\varepsilon^*$ further but breaks the symmetry that defined the projection — *not* the same operation at higher scale. This may be a marker of non-self-similarity.
3. **Purposeful sub-state ($G_t$).** Case B is $M_t$-only. Strategy-DAG sub-agents with different objectives produce structural mismatches in the goal direction, where the projection's "averaging" is more delicate. The Beta-Bernoulli case in `spikes/spike-composition-correlated-kalman.md` Part 2 has $\varepsilon^* > 0$ at $K_c = 1$; whether it remains $> 0$ under $K_c$-flow is the natural follow-up.
4. **Coupling structure that scales with $N$**. The two-agent case may be too simple to expose RG-relevant operators; many-agent systems with non-trivial coupling topology may show fixed-point structure that two-agent collapses.
5. **Iterated coarse-graining.** The proper RG test is to apply $\Lambda$ repeatedly: composite-of-composites and check whether parameters flow to a fixed point or run away. The single-step test in this section is a special case.

---

## 4. Open: Case A (homogeneous, transient initial conditions)

Brief: With $K_1^* = K_2^* = K^*$ but the inner gain $K_t$ not yet at $K^*$ (transient covariance $P_t \neq P^*$), the macro-update using fixed $K_c = K^*$ incurs an error from the gain mismatch $(K_t - K^*)$. The inner gain converges geometrically with rate $\lambda_K = (1 - K^*)^2 = r^2/(P^* + q + r)^2$ (linearization of the Riccati at $P^*$).

Predicted form: $\varepsilon_x^{*2}(K_c) \sim (1 - K^*)^{4 K_c}$ — *square* of Case B's rate, since the gain residual itself decays geometrically and the closure defect is its square.

This case adds the singular-perturbation flavor explicitly (fast inner state — gain — equilibrates within the macro-window). Quantifying it precisely requires tracking the joint evolution of $\hat\omega_t$ and $P_t$, which makes the closure-defect calculation longer but not harder.

**Decision**: defer to `01a-rg-0a-case-A-transient.md` if Case B alone is insufficient for the RG-0 verdict.

---

## 5. Open: Iterated coarse-graining (the actual RG test)

The single-step calculation in §2 establishes that *one* coarse-graining step brings $\varepsilon^*$ toward zero. The *RG flow* test is iterative:

1. Take two Kalman filters at level 0 with parameters $(K_1^{*(0)}, K_2^{*(0)})$.
2. Form the composite at level 1, with macro-parameter $\mu_c^{*(1)} = \bar\lambda_{K_c}^{(0)}$, equivalently $K_c^{*(1)} = 1 - \bar\lambda_{K_c}^{(0)}$.
3. Take two such composites and form the meta-composite at level 2.
4. Iterate. Does $K_c^{*(n)}$ converge as $n \to \infty$? To what?

This is the substantive RG test — checks whether AAT-shape is preserved under *repeated* coarse-graining and whether parameters reach a fixed point. The single-step result is necessary but not sufficient.

If parameters flow to a fixed point: AAT is RG-fixed-point in the strong sense. If they flow to a degenerate point (e.g., $K_c^{*(n)} \to 0$, all sub-agents become passive): AAT-shape is preserved but the *content* degenerates under flow — useful for the framing but with caveats.

**Decision**: spike this as `01b-rg-0a-iterated-coarse-graining.md` once Case B's interpretation is settled. This may be the most informative test; possibly worth promoting ahead of Case A.

---

## 6. Open: Asymmetric $\Lambda_o$ and the role of symmetry

§1.3 restricted $\Lambda_o$ to symmetric aggregations. An asymmetric aggregation could include $X_-$-direction information and reduce $\varepsilon^*$ further at $K_c = 1$ (the formula in `#form-composition-closure` Working Notes includes a $C_{+-}^2/S_+$ term from this optimization). Two questions:

1. Is the asymmetric optimum still AAT-shaped at the macro level? (May break some required symmetry of the macro-form.)
2. Does the asymmetric form's $K_c$-dependence differ from the symmetric form's? Both should still vanish as $K_c \to \infty$, but the rates may differ.

This is not central to the RG-0 verdict and can be deferred.

---

## 7. Honest tier and self-review

**Tier**: Derived (Case B closed form, conditional on the Gaussian / linear / steady-state setup and the symmetric-$\Lambda_o$ restriction).

**Self-check, three lenses**:
- *Wisdom*: The result resolves the original "stranded at zero-timescale-separation" audit gap, at least for this case. The mechanism (information lost to the projection's null space) is the right one. The framing's first-cut prediction was wrong but the corrected reading (globally attractive AAT fixed point) is more interesting.
- *Strength*: The derivation uses standard linear-Gaussian Kalman algebra. Edge cases handled: $K_c = 1$ recovers the existing Working-Notes formula; $K_c \to \infty$ limit is clean. The symmetric-$\Lambda_o$ restriction is documented as a scope constraint, not glossed.
- *Beauty*: The decomposition into symmetric (accessible) + anti-symmetric (orthogonal-direction-only) makes the closure mechanism visible: the residual lives in the projection's null space, which the macro-update structurally cannot access.

**What I'm uncertain about**:
- Whether the global attractor reading actually holds beyond linear-Gaussian. Non-Gaussian / non-linear sub-agents (Beta-Bernoulli strategy edges, gradient-based learners on non-convex losses) may exhibit different flow behavior.
- Whether the iterated-coarse-graining test (§5) gives a non-trivial fixed point or degenerate flow.
- Whether the symmetric-$\Lambda_o$ restriction is structurally required by AAT-shape preservation or merely a convenient scope choice.

**Next moves** (in order of expected information value):
1. **Iterated coarse-graining (§5)**. Most directly tests "AAT as RG fixed point." Tractable in this setup.
2. **Beta-Bernoulli strategy variant** (extending Part 2 of `spikes/spike-composition-correlated-kalman.md`). Tests whether $G_t$-side heterogeneity exhibits the same global-attractor behavior, or whether goal-direction structural mismatches resist $K_c$-flow.
3. **Case A (transient)** as supporting evidence for the singular-perturbation reading.

The verdict-document (`99-verdict.md`) will integrate this with the prior-art findings (`02-prior-art-rg-ib-fep.md`, in progress).
