---
slug: deriv-matrix-persistence-condition
type: derivation
status: conditional
stage: draft
depends:
  - def-adaptive-tempo
  - def-mismatch-signal
  - deriv-fisher-local-update-gain
  - result-persistence-condition
  - result-per-dimension-persistence
  - result-sector-persistence-template
---

# Derivation: Matrix-Loewner Persistence Condition

Under matrix adaptive tempo $\mathcal{T}$ from `#def-adaptive-tempo`'s Tensor extension (per-channel primitive $K^{(k)} = (H_M + H_L^{(k)})^{-1} H_L^{(k)}$ from `#deriv-fisher-local-update-gain`) and matrix disturbance covariance $\Sigma_w$, the operational persistence condition lifts from scalar to matrix-Loewner form: the agent persists iff $\mathcal{T}$ is Hurwitz (structural persistence) and the stationary covariance $\Sigma_\infty$ — solving the continuous Lyapunov equation $\mathcal{T}\Sigma_\infty + \Sigma_\infty\mathcal{T}^T = \Sigma_w$ — is strictly Loewner-dominated by the diagonal of squared per-direction critical thresholds $D_\delta := \mathrm{diag}(\delta_{\text{critical},k}^2)$. The matrix-Loewner condition $\Sigma_\infty \prec D_\delta$ recovers `#result-persistence-condition`'s scalar Model S form as the isotropic special case and `#result-per-dimension-persistence`'s per-coordinate form as the diagonal special case. Crucially, when $\mathcal{T}$ has off-diagonal entries that misalign with the coordinate basis — the generic situation under cross-dimensional correction — the per-coordinate condition is *unsafe*: it can declare persistence on systems whose stationary mismatch will exceed task-adequacy along the diagonal direction. The matrix-Loewner form is the canonical anisotropic persistence condition; per-coordinate is its diagonal-$\mathcal{T}$-axis-aligned-$D_\delta$ special case, sharp where the coordinate basis happens to be the correction-machinery's eigenbasis and unsafe outside it.

## Formal Expression

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

**(MP-1) Structural persistence.** $\mathcal{T}$ is Hurwitz — equivalently, $\Sigma_\infty$ exists as the unique positive-definite solution of the Lyapunov equation. This is the matrix analog of `#result-persistence-condition`'s structural condition $\alpha \gt 0$ (Hurwitz reduces to $\mathcal T_0 \gt 0$ in the scalar case).

**(MP-2) Matrix-Loewner task adequacy.**

$$\boxed{\;\Sigma_\infty \;\prec\; D_\delta \;:=\; \mathrm{diag}\!\big(\delta_{\text{critical},k}^2\big)\;}$$

with $\prec$ the strict Loewner (positive-definite) order: $D_\delta - \Sigma_\infty \succ 0$. The stationary mismatch ellipsoid is contained strictly inside the per-direction critical-threshold ellipsoid.

The two conditions are independent in the same sense as `#result-persistence-condition`'s structural-vs-task-adequacy split: (MP-1) is a property of the correction machinery alone; (MP-2) adds the domain-specific bound on per-direction tolerable mismatch.

### Three equivalent restatements

The Loewner condition (MP-2) admits three equivalent forms:

**(MP-2a) Per-direction.** For every unit direction $\hat v \in \mathbb{R}^d$:

$$\hat v^T \Sigma_\infty \hat v \;\lt\; \hat v^T D_\delta \hat v \;=\; \sum_k v_k^2\, \delta_{\text{critical},k}^2.$$

The projected stationary variance along $\hat v$ must be less than the direction-projected squared threshold along the same direction.

**(MP-2b) Spectral.** The generalized eigenvalue problem $\Sigma_\infty x = \lambda D_\delta x$ satisfies $\lambda_{\max} \lt 1$, equivalently

$$\lambda_{\max}\!\big(D_\delta^{-1/2}\Sigma_\infty D_\delta^{-1/2}\big) \;\lt\; 1.$$

The principal eigenvector identifies the *worst direction*; the eigenvalue's distance from $1$ is the worst-direction safety margin.

**(MP-2c) Ellipsoid containment.** The stationary noise ellipsoid $\{x : x^T \Sigma_\infty^{-1} x \le 1\}$ is contained strictly inside the threshold ellipsoid $\{x : x^T D_\delta^{-1} x \le 1\}$.

The three are mathematically equivalent under standard matrix-analysis (Horn & Johnson 2013, §4.6 and §7). (MP-2a) is cleanest for hand reasoning, (MP-2b) for computation (single generalized-eigenvalue solve), (MP-2c) for geometric intuition.

### Recovery of existing AAT persistence forms

| Special case | (MP-2) reduces to | Matches |
|---|---|---|
| Isotropic ($\mathcal{T} = \mathcal T_0 I$, $\Sigma_w = \sigma_w^2 I$, $\delta_{\text{critical}} = \delta_0 \mathbf{1}$) | $\sigma_w^2 / (2\mathcal T_0) \lt \delta_0^2$, i.e., $\mathcal T_0 \gt \sigma_w^2 / (2\delta_0^2)$ | Scalar Model S form, `#result-persistence-condition` |
| Diagonal $\mathcal{T}, \Sigma_w$ in the coordinate basis of $D_\delta$ | $\sigma_{w,k}^2 / (2\mathcal T_{kk}) \lt \delta_{\text{critical},k}^2$ per coordinate $k$ | Per-coordinate Model S RMS, `#result-per-dimension-persistence` |
| Symmetric $\mathcal{T}$ commuting with $\Sigma_w$, general $D_\delta$ | Per-eigendirection inequality in $\mathcal{T}$'s eigenbasis, with direction-projected thresholds | New content recovered from the matrix form — extends per-coordinate to non-axis-aligned $\mathcal{T}$ |

The third row is the content `#result-per-dimension-persistence` does not currently carry: when $\mathcal{T}$ and $\Sigma_w$ share an eigenbasis that is *not* the coordinate basis of $D_\delta$, the per-coordinate form misses the right direction-projected thresholds and the matrix-Loewner form handles them correctly.

### Where per-coordinate is unsafe — a constructive counterexample

The deeper structural question: is the matrix-Loewner form merely a generalization that agrees with per-coordinate in all real cases, or is it *strictly sharper* — does there exist a regime where per-coordinate says PASS but matrix-Loewner correctly says FAIL? The construction below establishes the latter: the per-coordinate form is **unsafe** under cross-dimensional correction.

**Construction.** Take $d = 2$, $\Sigma_w = I$, and

$$\mathcal{T} \;=\; \begin{pmatrix} 1 & -0.9 \\ -0.9 & 1 \end{pmatrix}.$$

This $\mathcal{T}$ is symmetric positive-definite with eigenvalues $1.9$ (along $(1, -1)/\sqrt{2}$) and $0.1$ (along $(1, 1)/\sqrt{2}$) — strongly anisotropic correction, with the $(1, 1)$ direction the weak axis. Per-coordinate naive reading of "diagonal of $\mathcal{T}$" sees uniform $\mathcal T_{11} = \mathcal T_{22} = 1$ and concludes correction is uniform at rate $1$ on each coordinate.

**Stationary covariance.** Since $\mathcal{T}$ is symmetric, $\Sigma_\infty = \tfrac{1}{2}\mathcal{T}^{-1}\Sigma_w = \tfrac{1}{2}\mathcal{T}^{-1}$. Direct computation:

$$\Sigma_\infty \;=\; \frac{1}{0.38}\begin{pmatrix} 1 & 0.9 \\ 0.9 & 1 \end{pmatrix} \;\approx\; \begin{pmatrix} 2.63 & 2.37 \\ 2.37 & 2.63 \end{pmatrix},$$

with eigenvalues $5.00$ along $(1, 1)/\sqrt{2}$ and $0.26$ along $(1, -1)/\sqrt{2}$.

**Set $\delta_{\text{critical}} = (1.7, 1.7)$**, so $D_\delta = 2.89\, I$.

- *Per-coordinate check (`#result-per-dimension-persistence` form):* per-coordinate stationary variance is $\Sigma_{\infty,kk} = 2.63 \lt 2.89 = \delta_{\text{critical},k}^2$ for each $k$. **Per-coordinate says PASS.** ✓
- *Matrix-Loewner check (MP-2 here):* worst-direction projected variance is $\lambda_{\max}(\Sigma_\infty) = 5.00$ along $(1, 1)/\sqrt{2}$. Direction-projected squared threshold along the same direction is $\hat v^T D_\delta \hat v = 2.89$. The condition $5.00 \lt 2.89$ fails. Equivalently, $\lambda_{\max}(D_\delta^{-1/2}\Sigma_\infty D_\delta^{-1/2}) = 5.00 / 2.89 \approx 1.73 \gt 1$. **Matrix-Loewner says FAIL.** ✗

**Conclusion.** Per-coordinate gives a false-pass. The agent will routinely produce mismatch vectors with RMS magnitude $\sqrt{5.00} = 2.24$ along the $(1, 1)/\sqrt{2}$ direction, exceeding the direction-projected threshold of $\sqrt{2.89} = 1.70$ on that direction. The per-coordinate analysis missed the diagonal direction because each coordinate alone stays within $\delta_{\text{critical},k} = 1.7$ — the failure is *only* visible at the matrix-Loewner level. Cross-dimensional correction (the off-diagonal entries of $\mathcal{T}$) is what creates the diagonal-direction concentration that per-coordinate cannot detect.

## Epistemic Status

*Conditional.* Max attainable: *exact* under (i) Model S linear stochastic dynamics, (ii) Hurwitz matrix tempo $\mathcal{T}$, (iii) positive-definite disturbance covariance $\Sigma_w$, (iv) diagonal critical-threshold structure $D_\delta = \mathrm{diag}(\delta_{\text{critical},k}^2)$. The Lyapunov equation, the existence-iff-Hurwitz fact, and the matrix-Loewner equivalence forms are all standard from Bellman 1960 / Khalil 2002 / Horn-Johnson 2013; the AAT-distinctive content is the application to the persistence condition and the recognition that per-coordinate is strictly sharper-or-unsafe rather than uniformly sharper.

**What is load-bearing:**

- The matrix-Loewner form as the canonical anisotropic persistence condition, with scalar and per-coordinate forms as special cases recovered exactly.
- The strict-sharpness result via the §4 counterexample: per-coordinate gives a false-pass when $\mathcal{T}$ has off-diagonal entries that misalign with the coordinate basis. The per-coordinate form is not merely incomplete in this regime — it is unsafe.
- The three equivalent restatements (per-direction, spectral, ellipsoid-containment) with their different operational readings.
- The structural-vs-task-adequacy decomposition from `#result-persistence-condition` transfers directly: (MP-1) is the matrix structural condition (Hurwitz); (MP-2) is the matrix task adequacy (Loewner $\Sigma_\infty \prec D_\delta$). The two conditions remain independent — Hurwitz $\mathcal{T}$ does not imply $\Sigma_\infty \prec D_\delta$ for any particular $D_\delta$, and conversely.

**What is not established here:**

- The nonlinear matrix-sector extension. Under sector-bounded $F(\mathcal{T}, \delta)$ with $\delta^T F \succeq \alpha I$ in matrix-Loewner form, the matrix-Lyapunov machinery extends to give an ultimate-bound matrix; the linear case here is the template instantiation. Full matrix-sector treatment is follow-on work in `#deriv-sector-condition`.
- The Model D matrix lift. Under deterministic bounded disturbance $\Vertw_t\Vert_M \le \rho$ in a quadratic norm, the ultimate-bound becomes an ellipsoid containment problem (a linear matrix inequality). Mechanical lift; not derived here.
- The non-Hurwitz boundary behaviour (eigenvalue exactly on the imaginary axis). Outside Hurwitz, the linear analysis fails — no stationary distribution. This matches the scalar case's $\alpha \gt 0$ requirement.
- The promotion of `#result-adversarial-tempo-advantage` to matrix form. The matrix-Loewner form sharpens the adversarial result via worst-direction targeting (an adversary controlling $\Sigma_w^{\text{adv}}$ maximizes $\lambda_{\max}(D_\delta^{-1/2}\Sigma_w^{\text{adv}} \mathcal T_{\text{eff}}^{-1} D_\delta^{-1/2})$), but the full adversarial promotion is a separate cycle.
- The matrix extension of `#deriv-persistence-cost`'s information-rate floor. The natural lift is $\dot R \ge \tfrac{1}{2}\mathrm{Tr}(\mathcal{T})$ — per-eigendirection application of the scalar derivation. Worth a cross-reference Working Note in that segment if it becomes load-bearing; not derived here.

## Discussion

**Why the Loewner form is the natural matrix lift.** The Lyapunov equation $\mathcal{T}\Sigma_\infty + \Sigma_\infty\mathcal{T}^T = \Sigma_w$ is itself a matrix-Loewner statement: it says $\Sigma_\infty$ balances correction (via $\mathcal{T}$) against disturbance (via $\Sigma_w$) in the PSD ordering. The task-adequacy condition $\Sigma_\infty \prec D_\delta$ reads this balance against the threshold ellipsoid. The whole structure lives in the cone of positive-semidefinite matrices ordered by Loewner dominance; scalar persistence is its 1D shadow, per-coordinate persistence is its axis-aligned-diagonal shadow, and the matrix form is the load-bearing object the shadows project from.

**The structural-vs-task-adequacy decomposition transfers.** `#result-persistence-condition`'s split — structural persistence (machinery works) vs task adequacy (machinery works well enough) — survives intact in the matrix lift: Hurwitz $\mathcal{T}$ is the matrix structural condition; Loewner $\Sigma_\infty \prec D_\delta$ is the matrix task-adequacy condition. The two are independent; an agent can have Hurwitz $\mathcal{T}$ (correction works in every direction) but fail Loewner on the worst direction (correction is not fast enough on the weak axis for the per-direction threshold). The remedies are different: structural failure requires changing the correction architecture (`#result-structural-adaptation-necessity`); task-adequacy failure requires either increasing $\mathcal{T}$ on the weak direction, decreasing $\Sigma_w$ on the weak direction, or relaxing the threshold along that direction.

**The weak-direction-bottleneck argument transfers and sharpens.** `#result-per-dimension-persistence`'s key insight — the weak dimension is the bottleneck — generalizes to the weak *direction* in the matrix lift: the worst eigenvector of $\Sigma_\infty$ relative to $D_\delta$ is what gates persistence. When this eigenvector aligns with a coordinate axis, the per-coordinate analysis catches it. When it points off-axis — the generic situation under cross-dimensional correction — the per-coordinate analysis misses it. The §4 counterexample is the canonical illustration: the worst direction is $(1, 1)/\sqrt{2}$, off-axis from both coordinate directions; per-coordinate evaluates the wrong directions; matrix-Loewner evaluates the right ones.

**Cross-coordinate correction is the generic case under Fisher-local invariance.** The matrix gain operator $K = (H_M + H_L)^{-1} H_L$ from `#deriv-fisher-local-update-gain` is diagonal in the coordinate basis only when prior precision $H_M$ and observation Fisher $H_L$ share an eigenbasis aligned with the coordinate axes. In general — and certainly in the natural-gradient regime where the agent's parameterization is statistical-manifold-natural rather than user-chosen — they do not, and $K$ has off-diagonal entries. The matrix-Loewner condition becomes the canonical form for any Fisher-local-derived persistence analysis; the per-coordinate form is the exceptional case where prior, likelihood, and threshold all happen to share the coordinate axes.

**Cross-reference to existing AAT machinery.** The matrix-Loewner form composes with:

- `#result-sector-persistence-template` (T1)–(T3) as the linear-case template instantiation; the matrix sector inequality $\delta^T F + F^T \delta \succeq 2\alpha I$ would extend the matrix-Lyapunov result to nonlinear $F$ via the template's (T2) condition lifted to matrix form.
- `#deriv-sector-condition` Prop A.1S (the Lyapunov-stochastic derivation underlying `#result-persistence-condition`'s scalar form) — the matrix derivation here is the analog at the matrix-Lyapunov level.
- `#deriv-fisher-local-update-gain` (matrix gain $K$ as the per-channel primitive) and `#def-adaptive-tempo` (Tensor extension aggregating $\mathcal{T} = \sum_k \nu^{(k)} K^{(k)}$).

**On the scope tag downstream.** Until the broader promotion of `#result-persistence-condition`, `#result-adversarial-tempo-advantage`, `#form-composition-closure`, `#der-team-persistence`, `#deriv-critical-mass-composition` to invoke the matrix form directly, those segments continue to read scalar and inherit the "scalar / isotropic / nonredundant-channel scope" tag from `#def-adaptive-tempo`'s Epistemic Status. The per-direction primitive is in place; the downstream promotion is a follow-on cycle in `TODO.md`.

## Working Notes

- **Counterexample as load-bearing content.** Section 4's $\mathcal{T} = \begin{pmatrix}1 & -0.9 \\ -0.9 & 1\end{pmatrix}$ example is the segment's strongest content — it shifts the matrix-Loewner form from "interesting generalization" to "the safe condition; per-coordinate is unsafe under cross-dimensional correction." The example uses the smallest nontrivial dimension ($d = 2$), the simplest non-diagonal symmetric $\mathcal{T}$ structure, and isotropic disturbance / threshold parameters. Generalizations to $d \gt 2$, asymmetric $\mathcal{T}$, and anisotropic $\Sigma_w / D_\delta$ are mechanical; the qualitative phenomenon (off-diagonal correction → diagonal-direction variance concentration → per-coordinate false-pass) is robust.
- **Empirical validation.** A 2D simulation matching the §4 parameters would confirm the predicted false-pass behaviour of per-coordinate: run the linear SDE with $\mathcal{T}, \Sigma_w$ from §4 for $N$ steps; observe that the per-coordinate marginals stay within $\pm 1.7$ most of the time (per-coordinate "passes") while the diagonal-direction projection routinely exceeds $\pm 1.7$ (matrix-Loewner "fails"). Mechanical simulation; would land cleanly under `obs-section-i-validation-simulations` as a new variant.
- **Open work — nonlinear matrix-sector.** The matrix-Loewner form is derived for linear correction. The nonlinear matrix-sector lift would replace the Lyapunov equation with the matrix-sector inequality $F(\delta) + F(\delta)^T \succeq 2\alpha \delta\delta^T / \Vert\delta\Vert^2$ (or a matrix-sector form derived from a quadratic Lyapunov function). Composes with `#deriv-sector-condition`'s nonlinear scalar machinery via the matrix template; not derived here.
- **Open work — adversarial extension.** The adversarial advantage exponent in `#result-adversarial-tempo-advantage` lifts to a matrix-eigenvalue-ratio exponent: an adversary controlling $\Sigma_w^{\text{adv}}$ maximizes the bad-direction stationary variance via the matrix-Loewner form. Worth a follow-on derivation if `#result-adversarial-tempo-advantage` is promoted to matrix form.
- **Open work — composition lift.** Composite stationary covariance $\Sigma_\infty^c$ solves the Lyapunov equation with composite $\mathcal{T}^c$ and $\Sigma_w^c$ (aggregated from sub-agents); composite Loewner condition $\Sigma_\infty^c \prec D_\delta^c$ governs composite persistence. Promoting `#form-composition-closure`, `#der-team-persistence`, and `#deriv-critical-mass-composition` to invoke the matrix form is the natural next AAT-1 follow-on cycle.
- **Landing context.** Landed in the 2026-05-12 AAT-1 follow-on cycle (matrix-Loewner persistence, succeed-beyond-claim); see CHANGELOG 2026-05-12 (late). The load-bearing derivation and counterexample are above; the follow-on extensions (Model D matrix lift, adaptive-gain matrix dynamics, variational matrix form) are flagged in the "Open work" notes here and in TODO. Originating spike is absorbed archaeology, not a live reference.
