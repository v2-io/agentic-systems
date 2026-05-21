# Appendix — Details (group 6)


## Derivation: Fisher-Whitened Edge Update Under Correlated Evidence

- **Slug**: `deriv-fisher-whitened-update-rule`
- **Type**: derivation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `disc-credit-assignment-boundary`, `deriv-edge-update-natural-parameter`, `der-gain-sector-bridge`, `disc-additive-coordinate-forcing`, `scope-agent-identity`

Under L1'/L2 correlated-evidence regimes, the default log-odds edge-update (from `#deriv-edge-update-natural-parameter`) retains correct *direction* — the angle between log-odds gradient and natural gradient never exceeds $45°$ at finite correlation $\rho$, so B1 directional fidelity ( #der-gain-sector-bridge) is never actively violated — but its *magnitude alignment* degrades by a factor $\sqrt{1-r^2}$ in the sector constant. The Fisher-whitened correction restores sharp B1 on the Fisher-weighted inner product. Under the (PI) parameterization-invariance axiom named in `#scope-agent-identity` and promoted to a primary instance of `#disc-additive-coordinate-forcing` via Čencov 1982, Fisher whitening is **AAT-internally derivable** rather than externally imported. The result adds sub-scope $\alpha_3$ (correlated evidence + Fisher-whitened update + Bayesian coherence → A2' derived) to the A2' partition and composes cleanly with the meta-gain machinery of `#deriv-adaptive-gain-dynamics` (Fisher whitening is a special case of meta-gain with $K_t = \mathbf I^{-1}(\lambda_t)$).

### Angle characterization under L1' correlation

*[Derived (angle-bound-finite-correlation)]*

For a block-correlated two-edge evidential model (soft-facilitator Prop B.7 parameterization), the Fisher information matrix has off-diagonal entry

$$r = \frac{\theta_C(1-\theta_C)\Delta_1 \Delta_2}{\sigma_1 \sigma_2} \in [-1, 1],$$

where $\theta_C$ is the latent-cause probability, $\Delta_j = p_{j\mid C} - p_{j\mid \neg C}$ is the separability gap, and $\sigma_j$ is the marginal-edge standard deviation. The Euclidean angle between the log-odds update direction and the natural-gradient direction (at single-edge plan residual) satisfies

$$\theta_{\text{LO-NG}} = \arccos\frac{1}{\sqrt{1 + r^2}} \leq 45° \quad \text{for all } r \in [-1, 1].$$

The log-odds update **never flips sign** under any finite correlation — B1 is never actively violated, only degraded in magnitude. Under the operational claim that "the default signal function needs validation under correlated failures," the finding is: **the default direction is preserved; only magnitude alignment degrades**. The sector constant in B1 degrades by a factor $\sqrt{1-r^2}$ under Euclidean B1; the Fisher-weighted B1 recovers the unperturbed sector constant.

### Fisher-whitened update rule

*[Definition (Fisher-whitened-update)]*

In log-odds coordinates $\lambda \in \mathbb R^{\lvert E\rvert}$ with Fisher information $\mathbf I(\lambda)$, the Fisher-whitened edge update is

$$T_{\text{FW}}(\lambda) = \lambda - \eta_{\text{edge}} \cdot \mathbf I^{-1}(\lambda) \cdot \mathbf J \cdot (\hat P_\Sigma(\sigma(\lambda)) - y_G)$$

(compared to the Euclidean log-odds update $T_{\text{edge}}(\lambda) = \lambda + \eta_{\text{edge}} \cdot \text{diag}(\iota) \cdot \mathbf J(y_G - \hat P_\Sigma)/\lVert\mathbf J\rVert^2$). The Fisher-weighted inner product $\langle a, b\rangle_\mathbf I = a^T \mathbf I^{-1} b$ makes the update's directional fidelity invariant under reparameterization of the natural-parameter coordinate.

### Two AAT-internal axiom paths

*[Derived (Fisher-whitening-from-B1-parameterization-invariance)]*

**Path A (B1-parameterization-invariance).** Require B1 directional fidelity to be *parameterization-invariant* in the sense of `#scope-agent-identity`'s (PI) axiom: the theorems about sub-scope α derivation in `#der-gain-sector-bridge` should not depend on arbitrary coordinate choices for $M_t$'s natural parameters. Under (PI), B1 sub-scope α partition is coordinate-invariant iff the inner product defining the directional-fidelity condition is the Fisher metric (Čencov 1982 uniqueness theorem under (PI); extended by Ay-Jost-Lê-Schwachhöfer 2017). The Fisher-weighted inner product is therefore *forced* by (PI), and the Fisher-whitened update is the AAT-internally derived correction direction for directional-fidelity preservation across parameterizations.

**Path B (Lyapunov-coordinate-matching via adjacent-family classification).** In the adjacent-family framing of `#disc-additive-coordinate-forcing`, the Lyapunov coordinate is *matched* (not forced) to the sector condition. For natural-gradient updates, the canonical Lyapunov is Fisher-weighted (Amari 1998, "Natural gradient works efficiently in learning," *Neural Computation* 10); this matches the geometry of the update operator. The two paths converge on the same Fisher-weighted result; Path A forces it via axiomatics, Path B confirms it via adjacent-family coordinate-matching.

Under L0 (no correlation), $r = 0$ and $\mathbf I$ is diagonal — Fisher whitening is vacuous (reduces to the existing Euclidean log-odds update). The axioms pick out Fisher whitening *uniquely* only under L1'/L2 (correlated evidence) regimes; they are vacuously satisfied under L0.

### New sub-scope $\alpha_3$

*[Derived (sub-scope-alpha-3)]*

Correlated-evidence + Fisher-whitened update + Bayesian coherence yields A2' *derived*:

$$(T_{\text{FW}}(\lambda) - \lambda^\ast)^T \mathbf I(\lambda^\ast)^{-1}(\lambda - \lambda^\ast) \geq \beta \lVert\lambda - \lambda^\ast\rVert_\mathbf{I}^2 \quad \text{with } \beta = \eta_{\text{edge}} \mu$$

on the Fisher-metric sector region around the fixed point $\lambda^\ast = \text{logit}(\theta^\ast)$. The directional-fidelity proof of `#der-gain-sector-bridge` carries over with $\kappa(\mathbf I)$ as Euclidean-transfer penalty — structurally identical to the Kalman case's $(P^-)^{-1}$-norm weighted-norm treatment. The Kalman case in `#der-gain-sector-bridge`'s Verified Instances is a special case of Fisher-weighted sector.

Sub-scope $\alpha_3$ extends the refinement introduced by `#deriv-adaptive-gain-dynamics`:
- **Sub-scope $\alpha_1$**: fixed-gain, independent evidence (Euclidean B1 applies; the existing A2' partition).
- **Sub-scope $\alpha_2$**: adaptive-gain, independent evidence (meta-gain conditions (MG-1)–(MG-4) per `#deriv-adaptive-gain-dynamics`).
- **Sub-scope $\alpha_3$**: fixed-gain, correlated evidence (Fisher-whitened update; this segment).

Additional composition: adaptive-gain + correlated-evidence (sub-scope $\alpha_4$) would compose `#deriv-adaptive-gain-dynamics` meta-gain machinery with Fisher whitening at the primary state; open.

### Connection to meta-gain as special case

*[Derived (Fisher-whitening-as-special-meta-gain)]*

The Fisher-whitened update is a meta-gain law in the sense of `#deriv-adaptive-gain-dynamics` with $K_t = \mathbf I^{-1}(\lambda_t)$ — a *degenerate* special case where the meta-gain is a deterministic function of the primary state rather than an independently learned variable. All four meta-gain conditions (MG-1)–(MG-4) are satisfied trivially:
- (MG-1) Meta-gain sector: $\mathbf I^{-1}$ is symmetric-positive-definite on the interior of the natural-parameter domain.
- (MG-2) Meta-gain bounded: $\lVert\mathbf I^{-1}\rVert$ bounded on compact natural-parameter subsets.
- (MG-3) Smoothness: $\mathbf I^{-1}$ depends smoothly on $\lambda$ for exponential families.
- (MG-4) Primary-meta coupling bounded: $\mathbf I^{-1}$'s state-derivative in the drift direction is bounded for exponential families.

This hands `#deriv-adaptive-gain-dynamics` a **concrete second instance** of derivable meta-gain alongside adaptive-Kalman-with-Mehra-estimator (its primary instance). The machinery of meta-gain composition via `#result-sector-persistence-template` (augmented-state Lyapunov) applies directly.

### L2 regime: candidate third `#disc-identifiability-floor` instance or strengthening of Instance 2

*[Hypothesis (L2-latent-floor)]*

Under L2-latent regimes (unobservable correlation structure beyond what Fisher information can resolve), Fisher whitening fails: the correlation sub-block of Fisher is rank-deficient (Cramér-Rao floor on unobservable parameters). This parallels `#disc-identifiability-floor` Instance 2's L1'-unobservable-$C$ Fisher-rank-1 obstruction — potentially a new L2 instance, or potentially a generalization of Instance 2 to higher correlation orders. Open whether these are distinct floors or a single unified obstruction.

L2-degenerate (perfect correlation, $r \to 1$) is a *structural* collapse — it requires DAG repair (edge merging) rather than update repair. This sits outside the Fisher-whitening framework.

---



## Derivation: Fisher-Local Update Gain

- **Slug**: `deriv-fisher-local-update-gain`
- **Type**: derivation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `emp-update-gain`, `def-mismatch-signal`, `def-observation-function`, `scope-agent-identity`, `disc-additive-coordinate-forcing`, `deriv-fisher-whitened-update-rule`, `deriv-adaptive-gain-dynamics`

Under the **Fisher-local invariance regime** — smooth log-likelihood admitting non-degenerate local quadratic expansion at the current model parameter, with single-step update at first order in the step size — the natural-gradient Bayesian posterior mean shift has the form $\Delta\theta = K \cdot \tilde\nabla$ with **gain operator** $K = (H_M + H_L)^{-1} H_L$ and **scalar collapse** $\eta^\ast = U_M/(U_M + U_o)$ along the natural-gradient direction in the commuting / shared-eigenbasis case (always in 1-D; under (PI)/Čencov in the natural-gradient direction in higher dimensions). The result derives the form `#emp-update-gain` carries as an empirical claim, places it in the Fisher-local regime as exact, and recovers linear-Gaussian (Kalman) and conjugate-Bayesian instances as cases where the local quadratic expansion is globally exact. Companion at the model-parameter-update layer to `#deriv-fisher-whitened-update-rule`'s edge-update derivation: that segment derives update *direction* under correlated evidence; this segment derives update *magnitude* under the Fisher-local regime. Both share the (PI) parameterization-invariance axiom from `#scope-agent-identity` and Čencov 1982 uniqueness as AAT-internal forcing for the Fisher metric.

### Setup — Fisher-local quadratic regime

*[Definition (Fisher-local regime, conditions (R1)–(R3))]*

Let $\theta \in \mathbb R^d$ parameterize the agent's model and $\theta_t$ be the current point estimate (mode of the prior $\pi_0$, or center of expansion). Three regime conditions:

- **(R1) Smooth log-likelihood admitting non-degenerate local quadratic expansion.** $\log \pi_0$ and $\log p(o \mid \cdot)$ are $C^3$ in a neighborhood of $\theta_t$, with prior precision $H_M := -\nabla^2 \log \pi_0(\theta_t)$ and observed information $H_L := -\nabla^2 \log p(o \mid \theta) \big|_{\theta_t}$ satisfying $H_M + H_L \succ 0$ (joint positive-definiteness; see §"Boundary admissibility" for why this is weaker than $H_M \succ 0$ and $H_L \succ 0$ both).
- **(R2) First-order-in-step-size regime.** The posterior update $\Delta\theta = \theta_{t+1} - \theta_t$ is small enough that $O(\lVert\Delta\theta\rVert^3)$ terms in the quadratic expansion are negligible compared to the quadratic terms.
- **(R3) Bayesian-coherent update.** $\theta_{t+1}$ is taken to be a coordinate of the posterior $p(\theta \mid o) \propto \pi_0(\theta) \cdot p(o \mid \theta)$ — mean, mode, or natural-parameter (they coincide for Gaussian posteriors, which is what the quadratic expansion produces).

Under (R1)–(R3), the local log-posterior is

$$\log p(\theta \mid o) = \mathrm{const} + s^T(\theta - \theta_t) - \tfrac{1}{2}(\theta - \theta_t)^T (H_M + H_L)(\theta - \theta_t) + O(\lVert\theta - \theta_t\rVert^3),$$

where $s := \nabla_\theta \log p(o \mid \theta) \big|_{\theta_t}$ is the score. The posterior is approximately $\mathcal N(\theta^\star, (H_M + H_L)^{-1})$ with mean shift

*[Derived (posterior-mean-shift)]*

$$\theta^\star - \theta_t = (H_M + H_L)^{-1} s.$$

The AAT-vocabulary correspondences are

$$U_M := H_M^{-1}, \qquad U_o := H_L^{-1}$$

— model uncertainty is the inverse prior precision, observation uncertainty is the inverse Fisher / inverse observed information (Cramér-Rao floor on what the observation pins down). The matrix forms generalize `#emp-update-gain`'s scalar $U_M, U_o$ in the natural way.

### Gain decomposition on the natural-gradient direction

*[Definition (natural gradient at the current point)]*

The **natural gradient** of the log-likelihood at $\theta_t$ in the Fisher metric is

$$\tilde\nabla \log p(o \mid \theta_t) := \mathcal I(\theta_t)^{-1} s.$$

For a single observation in the Fisher-local regime, $\mathcal I(\theta_t) = H_L$ up to the observed-vs-expected information distinction (standard under (R1)+regularity); the derivations below use $H_L$ directly as the Fisher.

*[Derived (gain-decomposition)]*

Rewriting the posterior mean shift in the natural-gradient direction:

$$\Delta\theta = (H_M + H_L)^{-1} s = (H_M + H_L)^{-1} H_L \cdot (H_L^{-1} s) = K \cdot \tilde\nabla,$$

with **gain operator**

$$\boxed{\;K := (H_M + H_L)^{-1} H_L.\;}$$

The matrix-valued $K$ is the natural object. The scalar collapse follows in the commuting / shared-eigenbasis case (always in 1-D; under (PI)/Čencov along the natural-gradient direction in higher dimensions): eigenvalues of $K$ are

$$\eta^\ast_i = \frac{h_{L,i}}{h_{M,i} + h_{L,i}} = \frac{1/u_{o,i}}{1/u_{M,i} + 1/u_{o,i}} = \frac{u_{M,i}}{u_{M,i} + u_{o,i}}$$

per coordinate, collapsing to the scalar

$$\boxed{\;\eta^\ast = \frac{U_M}{U_M + U_o}\;}$$

— the form `#emp-update-gain` carries, derived from the Fisher-local quadratic expansion of prior and likelihood and applied to the natural-gradient direction.

### Boundary admissibility — improper-prior and degenerate-likelihood directions

*[Derived (admissibility-of-degenerate-curvature)]*

The gain operator $K = (H_M + H_L)^{-1} H_L$ is well-defined whenever $H_M + H_L \succ 0$ — not necessarily when both $H_M$ and $H_L$ are individually positive-definite. This admits **degenerate-likelihood directions** (observation uninformative along some coordinates, $H_L$ rank-deficient): $K$'s eigenvalue along those directions is $0$, $u_{o,i} \to \infty$, $\eta^\ast_i \to 0$, no update along that direction — *trust the prior where the observation says nothing*. It also admits **improper-prior directions** (degenerate prior, $H_M = 0$ along some coordinate) when $H_L$ pins the direction: $\eta^\ast_i \to 1$ along uninformative-prior directions where the observation is informative — *trust the observation where the prior says nothing*, the maximum-likelihood limit.

The minimal regime condition is $H_M + H_L \succ 0$, with $U_M/(U_M + U_o)$ defined per-eigendirection by the appropriate limit. This corresponds to standard improper-prior admissibility in Bayesian inference and to standard observation-non-identifiability admissibility in maximum-likelihood estimation.

### Recovery of linear-Gaussian and conjugate-Bayesian cases

*[Derived (global-exactness-special-cases)]*

When the quadratic expansion in (R1) holds *globally* — not just locally — the derivation gives $\eta^\ast$ without any expansion error. Two canonical cases:

- **Linear-Gaussian (Kalman).** Prior $\mathcal N(\theta_t, U_M)$, likelihood $\mathcal N(o; H \theta, U_o)$ with linear observation operator $H$: the log-posterior is exactly quadratic. The scalar Kalman gain $K = U_M H^T (H U_M H^T + U_o)^{-1}$ collapses to $\eta^\ast = U_M/(U_M + U_o)$ in the scalar case (Kalman 1960; Bishop 2006 §3.3). Exact globally.
- **Conjugate Bayesian (Beta-Bernoulli, Dirichlet-multinomial, Gaussian-Gaussian, exponential-family natural-parameter conjugacy).** Natural-gradient VI is the exact posterior update at step size $1$ for conjugate families (Khan-Lin 2017 conjugate-computation variational inference). The Fisher-local expansion is globally exact in natural-parameter coordinates; $\eta^\ast = U_M/(U_M + U_o)$ holds exactly with $U_M, U_o$ read from the conjugate sufficient-statistic precision counts.

For general smooth models, the natural-gradient invariance theorem of Amari 1998 guarantees that the natural gradient is parameterization-invariant; the Fisher-local quadratic expansion is the order at which the natural gradient and the exact posterior agree to first order in step size.

---



## Derivation: Matrix-Loewner Persistence Condition

- **Slug**: `deriv-matrix-persistence-condition`
- **Type**: derivation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `def-adaptive-tempo`, `def-mismatch-signal`, `deriv-fisher-local-update-gain`, `result-persistence-condition`, `result-per-dimension-persistence`, `result-sector-persistence-template`

Under matrix adaptive tempo $\mathcal{T}$ from `#def-adaptive-tempo`'s Tensor extension (per-channel primitive $K^{(k)} = (H_M + H_L^{(k)})^{-1} H_L^{(k)}$ from `#deriv-fisher-local-update-gain`) and matrix disturbance covariance $\Sigma_w$, the operational persistence condition lifts from scalar to matrix-Loewner form: the agent persists iff $\mathcal{T}$ is Hurwitz (structural persistence) and the stationary covariance $\Sigma_\infty$ — solving the continuous Lyapunov equation $\mathcal{T}\Sigma_\infty + \Sigma_\infty\mathcal{T}^T = \Sigma_w$ — is strictly Loewner-dominated by the diagonal of squared per-direction critical thresholds $D_\delta := \mathrm{diag}(\delta_{\text{critical},k}^2)$. The matrix-Loewner condition $\Sigma_\infty \prec D_\delta$ recovers `#result-persistence-condition`'s scalar Model S form as the isotropic special case and `#result-per-dimension-persistence`'s per-coordinate form as the diagonal special case. Crucially, when $\mathcal{T}$ has off-diagonal entries that misalign with the coordinate basis — the generic situation under cross-dimensional correction — the per-coordinate condition is *unsafe*: it can declare persistence on systems whose stationary mismatch will exceed task-adequacy along the diagonal direction. The matrix-Loewner form is the canonical anisotropic persistence condition; per-coordinate is its diagonal-$\mathcal{T}$-axis-aligned-$D_\delta$ special case, sharp where the coordinate basis happens to be the correction-machinery's eigenbasis and unsafe outside it.

### Setup — Model S with matrix correction

*[Definition (matrix-Model-S-mismatch-dynamics)]*

Consider linear stochastic mismatch dynamics

$$d\delta_t \;=\; -\mathcal{T}\, \delta_t \, dt \;+\; \Sigma_w^{1/2}\, dW_t$$

with $\delta_t \in \mathbb{R}^d$, matrix adaptive tempo $\mathcal{T} \in \mathbb{R}^{d \times d}$, disturbance covariance $\Sigma_w \succ 0$, and standard $d$-dimensional Brownian $W_t$. Per `#def-adaptive-tempo`'s Tensor extension, $\mathcal{T} = \sum_k \nu^{(k)} K^{(k)}$ aggregates the per-channel matrix gain operators from `#deriv-fisher-local-update-gain`.

### Stationary covariance — continuous Lyapunov equation

*[Derived (stationary-covariance, exact under Hurwitz $\mathcal{T}$ and $\Sigma_w \succ 0$)]*

The stationary distribution of the linear stochastic dynamics is Gaussian $\mathcal{N}(0, \Sigma_\infty)$, with $\Sigma_\infty$ the unique positive-definite solution of the **continuous Lyapunov equation**

$$\boxed{\;\mathcal{T}\, \Sigma_\infty \;+\; \Sigma_\infty\, \mathcal{T}^T \;=\; \Sigma_w.\;}$$

Existence and uniqueness of $\Sigma_\infty \succ 0$ are equivalent to $\mathcal{T}$ being **Hurwitz** — all eigenvalues having strictly positive real part. The closed-form integral representation is

$$\Sigma_\infty \;=\; \int_0^\infty e^{-\mathcal{T} t}\, \Sigma_w\, e^{-\mathcal{T}^T t}\, dt.$$

When $\mathcal{T}$ is symmetric and commutes with $\Sigma_w$, the solution simplifies to $\Sigma_\infty = \tfrac{1}{2}\mathcal{T}^{-1}\Sigma_w$. Otherwise the integral form (or any standard Lyapunov-equation solver) gives the stationary covariance.

### The matrix-Loewner persistence condition

*[Derived (matrix-persistence-loewner-Model-S)]*

The agent persists operationally iff:

**(MP-1) Structural persistence.** $\mathcal{T}$ is Hurwitz — equivalently, $\Sigma_\infty$ exists as the unique positive-definite solution of the Lyapunov equation. This is the matrix analog of `#result-persistence-condition`'s structural condition $\alpha > 0$ (Hurwitz reduces to $\mathcal{T}_0 > 0$ in the scalar case).

**(MP-2) Matrix-Loewner task adequacy.**

$$\boxed{\;\Sigma_\infty \;\prec\; D_\delta \;:=\; \mathrm{diag}\!\big(\delta_{\text{critical},k}^2\big)\;}$$

with $\prec$ the strict Loewner (positive-definite) order: $D_\delta - \Sigma_\infty \succ 0$. The stationary mismatch ellipsoid is contained strictly inside the per-direction critical-threshold ellipsoid.

The two conditions are independent in the same sense as `#result-persistence-condition`'s structural-vs-task-adequacy split: (MP-1) is a property of the correction machinery alone; (MP-2) adds the domain-specific bound on per-direction tolerable mismatch.

### Three equivalent restatements

The Loewner condition (MP-2) admits three equivalent forms:

**(MP-2a) Per-direction.** For every unit direction $\hat v \in \mathbb{R}^d$:

$$\hat v^T \Sigma_\infty \hat v \;<\; \hat v^T D_\delta \hat v \;=\; \sum_k v_k^2\, \delta_{\text{critical},k}^2.$$

The projected stationary variance along $\hat v$ must be less than the direction-projected squared threshold along the same direction.

**(MP-2b) Spectral.** The generalized eigenvalue problem $\Sigma_\infty x = \lambda D_\delta x$ satisfies $\lambda_{\max} < 1$, equivalently

$$\lambda_{\max}\!\big(D_\delta^{-1/2}\Sigma_\infty D_\delta^{-1/2}\big) \;<\; 1.$$

The principal eigenvector identifies the *worst direction*; the eigenvalue's distance from $1$ is the worst-direction safety margin.

**(MP-2c) Ellipsoid containment.** The stationary noise ellipsoid $\{x : x^T \Sigma_\infty^{-1} x \le 1\}$ is contained strictly inside the threshold ellipsoid $\{x : x^T D_\delta^{-1} x \le 1\}$.

The three are mathematically equivalent under standard matrix-analysis (Horn & Johnson 2013, §4.6 and §7). (MP-2a) is cleanest for hand reasoning, (MP-2b) for computation (single generalized-eigenvalue solve), (MP-2c) for geometric intuition.

### Recovery of existing AAT persistence forms

| Special case | (MP-2) reduces to | Matches |
|---|---|---|
| Isotropic ($\mathcal{T} = \mathcal{T}_0 I$, $\Sigma_w = \sigma_w^2 I$, $\delta_{\text{critical}} = \delta_0 \mathbf{1}$) | $\sigma_w^2 / (2\mathcal{T}_0) < \delta_0^2$, i.e., $\mathcal{T}_0 > \sigma_w^2 / (2\delta_0^2)$ | Scalar Model S form, `#result-persistence-condition` |
| Diagonal $\mathcal{T}, \Sigma_w$ in the coordinate basis of $D_\delta$ | $\sigma_{w,k}^2 / (2\mathcal{T}_{kk}) < \delta_{\text{critical},k}^2$ per coordinate $k$ | Per-coordinate Model S RMS, `#result-per-dimension-persistence` |
| Symmetric $\mathcal{T}$ commuting with $\Sigma_w$, general $D_\delta$ | Per-eigendirection inequality in $\mathcal{T}$'s eigenbasis, with direction-projected thresholds | New content recovered from the matrix form — extends per-coordinate to non-axis-aligned $\mathcal{T}$ |

The third row is the content `#result-per-dimension-persistence` does not currently carry: when $\mathcal{T}$ and $\Sigma_w$ share an eigenbasis that is *not* the coordinate basis of $D_\delta$, the per-coordinate form misses the right direction-projected thresholds and the matrix-Loewner form handles them correctly.

### Where per-coordinate is unsafe — a constructive counterexample

The deeper structural question: is the matrix-Loewner form merely a generalization that agrees with per-coordinate in all real cases, or is it *strictly sharper* — does there exist a regime where per-coordinate says PASS but matrix-Loewner correctly says FAIL? The construction below establishes the latter: the per-coordinate form is **unsafe** under cross-dimensional correction.

**Construction.** Take $d = 2$, $\Sigma_w = I$, and

$$\mathcal{T} \;=\; \begin{pmatrix} 1 & -0.9 \\ -0.9 & 1 \end{pmatrix}.$$

This $\mathcal{T}$ is symmetric positive-definite with eigenvalues $1.9$ (along $(1, -1)/\sqrt{2}$) and $0.1$ (along $(1, 1)/\sqrt{2}$) — strongly anisotropic correction, with the $(1, 1)$ direction the weak axis. Per-coordinate naive reading of "diagonal of $\mathcal{T}$" sees uniform $\mathcal{T}_{11} = \mathcal{T}_{22} = 1$ and concludes correction is uniform at rate $1$ on each coordinate.

**Stationary covariance.** Since $\mathcal{T}$ is symmetric, $\Sigma_\infty = \tfrac{1}{2}\mathcal{T}^{-1}\Sigma_w = \tfrac{1}{2}\mathcal{T}^{-1}$. Direct computation:

$$\Sigma_\infty \;=\; \frac{1}{0.38}\begin{pmatrix} 1 & 0.9 \\ 0.9 & 1 \end{pmatrix} \;\approx\; \begin{pmatrix} 2.63 & 2.37 \\ 2.37 & 2.63 \end{pmatrix},$$

with eigenvalues $5.00$ along $(1, 1)/\sqrt{2}$ and $0.26$ along $(1, -1)/\sqrt{2}$.

**Set $\delta_{\text{critical}} = (1.7, 1.7)$**, so $D_\delta = 2.89\, I$.

- *Per-coordinate check (`#result-per-dimension-persistence` form):* per-coordinate stationary variance is $\Sigma_{\infty,kk} = 2.63 < 2.89 = \delta_{\text{critical},k}^2$ for each $k$. **Per-coordinate says PASS.** ✓
- *Matrix-Loewner check (MP-2 here):* worst-direction projected variance is $\lambda_{\max}(\Sigma_\infty) = 5.00$ along $(1, 1)/\sqrt{2}$. Direction-projected squared threshold along the same direction is $\hat v^T D_\delta \hat v = 2.89$. The condition $5.00 < 2.89$ fails. Equivalently, $\lambda_{\max}(D_\delta^{-1/2}\Sigma_\infty D_\delta^{-1/2}) = 5.00 / 2.89 \approx 1.73 > 1$. **Matrix-Loewner says FAIL.** ✗

**Conclusion.** Per-coordinate gives a false-pass. The agent will routinely produce mismatch vectors with RMS magnitude $\sqrt{5.00} = 2.24$ along the $(1, 1)/\sqrt{2}$ direction, exceeding the direction-projected threshold of $\sqrt{2.89} = 1.70$ on that direction. The per-coordinate analysis missed the diagonal direction because each coordinate alone stays within $\delta_{\text{critical},k} = 1.7$ — the failure is *only* visible at the matrix-Loewner level. Cross-dimensional correction (the off-diagonal entries of $\mathcal{T}$) is what creates the diagonal-direction concentration that per-coordinate cannot detect.

---



## Derivation: Linear Matrix Inequality Form of the Causal-IB Survival Bound

- **Slug**: `deriv-causal-ib-lmi`
- **Type**: derivation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `deriv-causal-ib-exploration`, `form-information-bottleneck`, `def-pearl-causal-hierarchy`, `result-persistence-condition`, `deriv-fisher-whitened-update-rule`, `def-adaptive-tempo`

In `#deriv-causal-ib-exploration`, the survival-imperative exploration drive was derived in scalar form: bound $\mathbb E_\pi[U_o(a)] \le U_o^{\max}$ to keep the agent's mismatch within survivable bounds. The scalar bound admits a "blank wall" attack — actions that minimize $U_o$ in a subspace orthogonal to the drift (e.g., observing a constant signal uncorrelated with the environmental drift) satisfy the survival math without probing the drifting coordinates, and the agent's prediction in those subspaces diverges unboundedly. This segment lifts the survival constraint to a Linear Matrix Inequality on the Fisher Information Matrix, replacing the scalar shadow price with a positive-semidefinite matrix Lagrange multiplier $\Lambda$ that distinguishes by direction, not just by magnitude.

### Multidimensional mismatch dynamics

*[Definition (multidim-mismatch)]*

The mismatch state $\delta_t \in \mathbb R^n$ evolves under linear-Gaussian dynamics with action-dependent observation noise:

$$\delta_{t+1} = (I - K_t H)\delta_t + w_t - K_t v_t(a_t)$$

where $w_t \sim \mathcal N(0, Q_\rho)$ is the environmental drift, $v_t \sim \mathcal N(0, R_o(a_t))$ is the observation noise for action $a_t$, and the optimal Kalman gain is $K_t = P_t H^T(H P_t H^T + R_o(a_t))^{-1}$ with $P_t$ the agent's prior uncertainty covariance.

The steady-state mismatch covariance $\Sigma_\delta$ satisfies the discrete-time algebraic Riccati equation. *Survival* requires the spectral bound

$$\lambda_{\max}(\Sigma_\delta) \lt R^2$$

— the matrix lift of the scalar bound $R^\ast \lt R$ from `#result-persistence-condition`.

### Fisher Information Matrix as matrix CIY

*[Definition (matrix-ciy)]*

For the linear-Gaussian observation model, the action-conditional Fisher Information Matrix is

$$\mathcal I_o(a) = H^T R_o(a)^{-1} H.$$

Where the scalar formulation in `#disc-ciy-unified-objective` defined CIY as a surrogate satisfying $\text{CIY}(a) \propto 1/U_o(a)$, the multidimensional formulation identifies CIY directly with the action-conditional FIM. The CIY-$U_o$ surrogate-mapping layer of approximation in the scalar derivation is removed at this layer; the residual CIY-vs-EIG concern (FIM equals EIG-rate only under Gaussian-linear conditions) persists as before.

The information-form Kalman update is additive in the FIM:

$$P_{t+1\mid t+1}^{-1} = P_{t+1\mid t}^{-1} + \mathcal I_o(a_t),$$

where $P_{t+1\mid t} = A P_t A^T + Q_w$ is the prediction step that absorbs process noise. The simplification $P_{t+1}^{-1} = P_t^{-1} + \mathcal I_o(a_t)$ used in some passes refers to the information-update step alone; the full step adds the prediction contribution. The two coincide once the analysis is in steady state.

### LMI survival constraint

*[Derived (lmi-survival)]*

The discrete-time algebraic Riccati equation admits a stabilizing steady-state solution with $\lambda_{\max}(\Sigma_\delta) \lt R^2$ if and only if the action policy $\pi$ provides Fisher information that dominates the unstabilizable modes of the system drift. Specifically, the policy must satisfy the Linear Matrix Inequality

$$\mathbb E_{a \sim \pi}[\mathcal I_o(a)] \succeq \mathcal I_{\min}(Q_\rho, A, R^2)$$

where $\mathcal I_{\min}$ is the symmetric positive-definite lower bound on the FIM required to keep the steady-state covariance's largest eigenvalue below $R^2$. The closed form for $\mathcal I_{\min}$ as a function of $(Q_\rho, A, R^2)$ is given by the steady-state DARE condition — standard control-theory machinery (Boyd, Ghaoui, Feron & Balakrishnan 1994 Ch. 3–5; Anderson & Moore 1979). AAT's contribution at this layer is the framing: $\mathcal I_{\min}$ enters as the *survival-imperative* Fisher-information floor, not as a controller-design parameter.

### Tensor Lagrangian

*[Derived (tensor-lagrangian)]*

The agent maximizes pragmatic value under the LMI constraint:

$$\max_\pi\, \mathbb E_\pi[Q_O(a)] \quad \text{s.t.} \quad \mathbb E_\pi[\mathcal I_o(a)] \succeq \mathcal I_{\min}.$$

The Lagrangian for a matrix-inequality-constrained problem uses a positive-semidefinite matrix Lagrange multiplier $\Lambda \succeq 0$:

$$\mathcal L(\pi, \Lambda) = \mathbb E_\pi[Q_O(a)] + \text{Tr}\!\left( \Lambda \cdot \left( \mathbb E_\pi[\mathcal I_o(a)] - \mathcal I_{\min} \right) \right).$$

KKT conditions are primal feasibility ($\mathbb E_\pi[\mathcal I_o(a)] \succeq \mathcal I_{\min}$), dual feasibility ($\Lambda \succeq 0$), and complementary slackness ($\text{Tr}(\Lambda \cdot (\mathbb E_\pi[\mathcal I_o(a)] - \mathcal I_{\min})) = 0$). The optimal action selection rule is

$$a_t \in \arg\max_a \left[\, Q_O(a) + \text{Tr}\!\left(\Lambda \cdot \mathcal I_o(a)\right) \,\right].$$

The trace inner-product $\text{Tr}(\Lambda \cdot \mathcal I_o(a))$ is the **matrix exploration bonus** — the multidimensional analog of $\lambda_{\text{surv}} \cdot \text{CIY}(a)$ from the scalar derivation.

### Resolution of the blank-wall attack

*[Derived (blank-wall-resolution)]*

By complementary slackness, $\Lambda$ has support only in eigendirections where the LMI constraint binds — i.e., directions where the agent's accumulated FIM sits at the threshold $\mathcal I_{\min}$. In non-drifting eigendirections of $Q_\rho$, $\mathcal I_{\min}$ contributes zero (no information needed there to survive), so $\Lambda$ has zero weight in those directions.

For a blank-wall action — high $\mathcal I_o(a)$ in a non-drifting eigendirection — the trace product $\text{Tr}(\Lambda \cdot \mathcal I_o(a))$ evaluates to zero: the action's FIM eigenvalues lie outside $\Lambda$'s support. The agent receives no exploration bonus for the blank-wall action, even though the action would satisfy the scalar magnitude bound. **The matrix Lagrangian distinguishes by direction, not just by magnitude**, mathematically forbidding the trivial-exploration solutions that the scalar form admitted.

### Scalar reduction

*[Derived (scalar-recovery)]*

In the 1D case, $H$ and $R_o(a)$ are scalars, $\mathcal I_o(a) = R_o(a)^{-1}$, and the LMI degenerates to the scalar inequality $\mathbb E_\pi[R_o(a)^{-1}] \geq \mathcal I_{\min}$ which, with $\mathcal I_{\min}^{-1} = U_o^{\max}$, recovers the scalar survival constraint of `#deriv-causal-ib-exploration`. The matrix multiplier $\Lambda$ collapses to a scalar shadow price coinciding with $\lambda_{\text{surv}}$, and the matrix exploration bonus reduces to $\lambda_{\text{surv}} \cdot \text{CIY}(a)$. The multidimensional derivation is structurally consistent with — and properly subsumes — the scalar one.

### Tragedy of the Confident Agent — matrix form

*[Derived (matrix-confidence-tragedy)]*

As the agent's prior covariance $P_t$ shrinks in a particular eigendirection $v$, the agent's confidence in that direction grows. If $v$ also has support in $Q_\rho$ (a drifting eigendirection), the survival LMI requires $\mathcal I_{\min}$ to grow along $v$ to compensate — a confident agent in a drifting direction must source information specifically along that direction, because its low $P_t$ in $v$ means its update gain is small there and slow to absorb new information. By complementary slackness, the matrix shadow price $\Lambda$ develops a large principal eigenvalue along $v$, forcing the agent to choose actions whose $\mathcal I_o(a)$ has large support on $v$. The qualitative tragedy survives the lift: confident agents in drifting worlds are mathematically forced to probe the drifting eigendirections specifically, not just to minimize scalar noise.

---
