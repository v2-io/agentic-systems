---
slug: spike-matrix-persistence-condition
type: spike
status: working
date: 2026-05-12
related_segments:
  - result-persistence-condition
  - result-per-dimension-persistence
  - def-adaptive-tempo
  - deriv-fisher-local-update-gain
  - result-sector-persistence-template
  - result-sector-condition-stability
related_findings:
  - aad-1-tensor-tempo-promotion (post-2026-05-12 AAD-1 follow-on)
related_spikes:
  - spike-fisher-local-update-gain-derivation (provides matrix gain primitive K)
---

# Spike: Matrix-Loewner Persistence Condition

**Trigger.** AAD-1 follow-on after the 2026-05-12 cycle. `#def-adaptive-tempo` now carries a Tensor extension sub-block citing the matrix gain operator $K = (H_M + H_L)^{-1} H_L$ from `#deriv-fisher-local-update-gain`. The per-direction primitive is in place; downstream summary results — `#result-persistence-condition`, `#result-per-dimension-persistence`, the adversarial-tempo result, the composition machinery — still read scalar and inherit a `scalar / isotropic / nonredundant-channel scope` tag. `#result-per-dimension-persistence` Working Notes line 130 has flagged the open question explicitly: *"The diagonal-correction assumption is restrictive. Real agents may have cross-dimensional correction (fixing one thing improves another). Off-diagonal correction terms would couple the dimensions and change the analysis. Whether the weak-dimension bottleneck persists under coupled correction is an open question."*

**Strengthening posture.** First attempt: derive the full matrix-Loewner persistence condition for Model S under general (not-necessarily-diagonal, not-necessarily-commuting) $\mathcal{T}$ and $\Sigma_w$, with per-direction critical thresholds $\delta_{\text{critical}}$ encoded as $D_\delta = \mathrm{diag}(\delta_{\text{critical},k}^2)$. Recover scalar and per-coordinate forms as special cases. Establish whether the matrix form is *strictly* sharper than per-coordinate, or merely a generalization that agrees with per-coordinate in all real cases.

**Outcome: succeed beyond claim.** The matrix-Loewner persistence condition lifts cleanly from the scalar Lyapunov machinery; recovers all three existing forms (scalar, per-coordinate Model D, per-coordinate Model S) as special cases; and **is strictly sharper** than per-coordinate when $\mathcal{T}$ has off-diagonal components that misalign with the per-coordinate threshold basis. A constructive 2D counterexample (§4) demonstrates that the per-coordinate condition can say PASS while the matrix-Loewner condition correctly says FAIL — i.e., the per-coordinate form is not merely incomplete in such regimes, it is **unsafe** (gives a false-pass on the persistence question). This closes the open question in `#result-per-dimension-persistence` Working Notes and establishes the matrix-Loewner form as the canonical anisotropic persistence condition; the per-coordinate form is the diagonal-$\mathcal{T}$, diagonal-$\Sigma_w$, axis-aligned-$D_\delta$ special case.

---

## 1. Setup — Model S with matrix correction and matrix disturbance

Consider the multivariate stochastic mismatch dynamics

$$d\delta_t \;=\; -\mathcal{T}\, \delta_t \, dt \;+\; \Sigma_w^{1/2}\, dW_t,$$

where:

- $\delta_t \in \mathbb{R}^d$ is the mismatch state vector.
- $\mathcal{T} \in \mathbb{R}^{d \times d}$ is the **matrix adaptive tempo** of `#def-adaptive-tempo`'s Tensor extension. Per `#deriv-fisher-local-update-gain`, $\mathcal{T} = \sum_k \nu^{(k)} K^{(k)}$ with $K^{(k)} = (H_M + H_L^{(k)})^{-1} H_L^{(k)}$ on each observation channel. The matrix tempo is positive-stable (Hurwitz: all eigenvalues have positive real part) under the assumption that the correction machinery genuinely contracts in every direction — the natural-gradient direction is the canonical reference, but the matrix object is the load-bearing one.
- $\Sigma_w \in \mathbb{R}^{d \times d}$ is the **disturbance covariance** (positive-definite). Anisotropic disturbance is handled here directly; the off-diagonal entries encode cross-coordinate disturbance correlation (e.g., one source affecting multiple coordinates simultaneously).
- $W_t$ is standard multidimensional Brownian motion.
- Per-direction critical thresholds $\delta_{\text{critical}} \in \mathbb{R}^d_+$ encode the per-coordinate task-adequacy tolerances. Their squared diagonal $D_\delta := \mathrm{diag}(\delta_{\text{critical},k}^2)$ is the load-bearing matrix object in the persistence condition (§3).

This is the Model S of `#result-persistence-condition` lifted to the matrix case: scalar $\mathcal{T}$ and $\sigma_w^2$ become matrices, the per-coordinate critical threshold becomes a diagonal matrix $D_\delta$, and the analysis runs in the Loewner (positive-semidefinite) order rather than scalar inequality.

The same lift is available for Model D (deterministic-bounded disturbance with $\|w_t\| \le \rho$ in some norm); it produces a matrix-set inclusion condition rather than a Loewner inequality. The Model D matrix lift is more straightforward (no Lyapunov equation needed); we treat Model S as the primary case because (i) it is the case where the per-coordinate form has nontrivial structure, (ii) the simulation validation of `#result-per-dimension-persistence` was on Model S, and (iii) it is the form most operational AAD work uses. Model D matrix lift sketched in §7 as a follow-on.

## 2. Stationary covariance — the continuous Lyapunov equation

The stationary distribution of the linear stochastic mismatch dynamics is Gaussian $\mathcal{N}(0, \Sigma_\infty)$, with stationary covariance $\Sigma_\infty$ satisfying the **continuous Lyapunov equation**

$$\boxed{\;\mathcal{T}\, \Sigma_\infty \;+\; \Sigma_\infty\, \mathcal{T}^T \;=\; \Sigma_w.\;}$$

*[Derived (stationary-Lyapunov-equation), standard Itô analysis]*

**Existence and uniqueness.** $\Sigma_\infty \succ 0$ exists and is unique iff $\mathcal{T}$ is Hurwitz, i.e., all eigenvalues of $\mathcal{T}$ have strictly positive real part. The closed-form solution under Hurwitz-$\mathcal{T}$ is

$$\Sigma_\infty \;=\; \int_0^\infty e^{-\mathcal{T} t}\, \Sigma_w\, e^{-\mathcal{T}^T t}\, dt.$$

**Special cases that match existing scalar / per-coordinate AAD forms.**

- **Symmetric $\mathcal{T}$ with $[\mathcal{T}, \Sigma_w] = 0$** (commuting): $\Sigma_\infty = \tfrac{1}{2}\mathcal{T}^{-1}\Sigma_w$. In the eigenbasis of $\mathcal{T}$, $\Sigma_\infty$ is diagonal with entries $\sigma_{w,k}^2/(2\lambda_k(\mathcal{T}))$.
- **Diagonal $\mathcal{T}$ and diagonal $\Sigma_w$** (decoupled coordinates): $\Sigma_\infty$ is diagonal with entries $\sigma_{w,k}^2/(2\mathcal{T}_{kk})$. This is the `#result-per-dimension-persistence` Model S form per-coordinate.
- **Isotropic $\mathcal{T} = \mathcal{T}_0 I$, $\Sigma_w = \sigma_w^2 I$** (scalar Model S): $\Sigma_\infty = (\sigma_w^2/(2\mathcal{T}_0)) I$; trace $= n\sigma_w^2/(2\mathcal{T}_0)$, matching `#result-persistence-condition` scalar Model S form per coordinate.

The non-commuting general case (asymmetric $\mathcal{T}$, or $\mathcal{T}$ and $\Sigma_w$ with different eigenbases) is the regime where the matrix-Loewner condition becomes strictly sharper than per-coordinate. §4 carries the counterexample.

## 3. The matrix-Loewner persistence condition

*[Derived (matrix-persistence-loewner-Model-S, from stationary-Lyapunov-equation + per-direction task adequacy)]*

The agent persists operationally iff:

(MP-1) **Structural persistence.** $\mathcal{T}$ is Hurwitz — equivalently, $\Sigma_\infty$ exists as the unique positive-definite solution of the continuous Lyapunov equation.

(MP-2) **Matrix-Loewner task adequacy.**

$$\boxed{\;\Sigma_\infty \;\prec\; D_\delta\;} \quad\quad\text{where } D_\delta := \mathrm{diag}(\delta_{\text{critical},k}^2),$$

with $\prec$ the strict Loewner (positive-definite) order: $D_\delta - \Sigma_\infty \succ 0$.

The two conditions are independent in the same sense as `#result-persistence-condition`'s structural-vs-task-adequacy split: structural persistence is a property of the correction machinery alone (does $\Sigma_\infty$ exist?); task adequacy is the domain-specific bound on per-direction tolerable mismatch.

### Equivalent forms

The Loewner condition (MP-2) admits three equivalent restatements, each with a different operational reading:

**(MP-2a) Per-direction.** For every unit direction $\hat v \in \mathbb{R}^d$:

$$\hat v^T \Sigma_\infty \hat v \;<\; \hat v^T D_\delta \hat v \;=\; \sum_k v_k^2 \,\delta_{\text{critical},k}^2.$$

The projected stationary variance along $\hat v$ must be less than the direction-projected squared threshold.

**(MP-2b) Spectral.** The generalized eigenvalue problem $\Sigma_\infty x = \lambda D_\delta x$ has $\lambda_{\max} < 1$, equivalently

$$\lambda_{\max}\!\left( D_\delta^{-1/2} \Sigma_\infty D_\delta^{-1/2} \right) \;<\; 1.$$

The "worst direction" is the eigenvector achieving this maximum; the eigenvalue is the *persistence-margin slack* (1 minus this max is the worst-direction safety margin).

**(MP-2c) Ellipsoid containment.** The stationary noise covariance ellipsoid $\{ x : x^T \Sigma_\infty^{-1} x \le 1 \}$ is contained strictly inside the critical-threshold ellipsoid $\{ x : x^T D_\delta^{-1} x \le 1 \}$.

These three are mathematically equivalent; (MP-2a) is the cleanest for hand reasoning, (MP-2b) is the cleanest for computation (single generalized-eigenvalue solve), (MP-2c) is the cleanest geometric picture.

### Recovery of existing AAD forms

The matrix-Loewner condition (MP-2) reduces to the scalar and per-coordinate forms as advertised:

| Special case | (MP-2) reduces to | Matches |
|---|---|---|
| Isotropic ($\mathcal{T} = \mathcal{T}_0 I$, $\Sigma_w = \sigma_w^2 I$, $\delta_{\text{critical}} = \delta_0 \mathbf{1}$) | $\sigma_w^2 / (2\mathcal{T}_0) < \delta_0^2$, i.e., $\mathcal{T}_0 > \sigma_w^2 / (2\delta_0^2)$ | Scalar Model S, `#result-persistence-condition` |
| Diagonal $\mathcal{T}, \Sigma_w$ with general $D_\delta$ | $\sigma_{w,k}^2 / (2\mathcal{T}_{kk}) < \delta_{\text{critical},k}^2$ for each $k$ | Per-coordinate Model S RMS form, `#result-per-dimension-persistence` line 48 |
| Symmetric $\mathcal{T}$ commuting with $\Sigma_w$, general $D_\delta$ | $\sigma_{w,(k)}^2 / (2\lambda_k(\mathcal{T})) < (\delta_{\text{critical}}^{(k)})^2$ per eigenvector of $\mathcal{T}$, where $\delta_{\text{critical}}^{(k)} = $ direction-projected threshold along $\mathcal{T}$'s $k$-th eigenvector | Per-eigendirection Model S — **new content**, recovered from the matrix form |

The third row is content `#result-per-dimension-persistence` does not currently carry: when $\mathcal{T}$ and $\Sigma_w$ are symmetric and commuting but their shared eigenbasis is *not* the coordinate basis, the per-coordinate form misses the right direction-projected thresholds. The matrix-Loewner form handles it correctly.

## 4. Where matrix-Loewner is strictly sharper — a constructive counterexample

The interesting question: is there a regime where the per-coordinate condition `#result-per-dimension-persistence` says PASS while the matrix-Loewner condition correctly says FAIL? If yes, the per-coordinate form is not merely incomplete — it is *unsafe*, giving a false-pass on the persistence question.

**Construction.** Take $d = 2$, $\Sigma_w = I$, and

$$\mathcal{T} \;=\; \begin{pmatrix} 1 & -0.9 \\ -0.9 & 1 \end{pmatrix}.$$

This $\mathcal{T}$ is symmetric, positive-definite (eigenvalues $1 + 0.9 = 1.9$ and $1 - 0.9 = 0.1$), and decidedly anisotropic — strong contraction along the $(1, -1)$ direction (eigenvalue $1.9$), weak contraction along the $(1, 1)$ direction (eigenvalue $0.1$). The per-coordinate "diagonal of $\mathcal{T}$" naive reading sees $\mathcal{T}_{11} = \mathcal{T}_{22} = 1$ and concludes the correction is uniform at rate $1$ on each coordinate.

**Stationary covariance.** Since $\mathcal{T}$ is symmetric, $\Sigma_\infty = \tfrac{1}{2}\mathcal{T}^{-1}\Sigma_w = \tfrac{1}{2}\mathcal{T}^{-1}$. Computing:

$$\mathcal{T}^{-1} \;=\; \frac{1}{\det \mathcal{T}}\begin{pmatrix} 1 & 0.9 \\ 0.9 & 1 \end{pmatrix} \;=\; \frac{1}{0.19}\begin{pmatrix} 1 & 0.9 \\ 0.9 & 1 \end{pmatrix} \;\approx\; \begin{pmatrix} 5.26 & 4.74 \\ 4.74 & 5.26 \end{pmatrix}.$$

So

$$\Sigma_\infty \;=\; \tfrac{1}{2}\mathcal{T}^{-1} \;\approx\; \begin{pmatrix} 2.63 & 2.37 \\ 2.37 & 2.63 \end{pmatrix},$$

with eigenvalues $2.63 + 2.37 = 5.00$ along $(1,1)/\sqrt{2}$ and $2.63 - 2.37 = 0.26$ along $(1,-1)/\sqrt{2}$. The "bad direction" — the direction in which the stationary mismatch is largest — is $(1,1)/\sqrt{2}$, the direction $\mathcal{T}$ contracts weakly.

**Set $\delta_{\text{critical}} = (1.7,\, 1.7)$**, so $D_\delta = \mathrm{diag}(2.89, 2.89) = 2.89\, I$.

- **Per-coordinate check (`#result-per-dimension-persistence` form)**: the per-coordinate stationary variance is $\Sigma_{\infty,11} = \Sigma_{\infty,22} = 2.63$. The per-coordinate task-adequacy condition $\Sigma_{\infty,kk} < \delta_{\text{critical},k}^2$ asks $2.63 < 2.89$ for each coordinate — both hold. **Per-coordinate says PASS.** ✓

- **Matrix-Loewner check (this segment's MP-2 form)**: the worst-direction projected stationary variance is $\lambda_{\max}(\Sigma_\infty) = 5.00$ along $(1,1)/\sqrt{2}$. The direction-projected squared threshold along $(1,1)/\sqrt{2}$ is $\hat v^T D_\delta \hat v = (1/2)(2.89) + (1/2)(2.89) = 2.89$. The condition $5.00 < 2.89$ **fails**. Equivalently, $\lambda_{\max}(D_\delta^{-1/2}\Sigma_\infty D_\delta^{-1/2}) = 5.00 / 2.89 \approx 1.73 > 1$. **Matrix-Loewner says FAIL.** ✗

**Conclusion.** The per-coordinate form is unsafe in this regime: it declares persistence on a system whose stationary mismatch will exceed task-adequacy along the $(1,1)$ diagonal direction. The agent will routinely produce mismatch vectors with $\delta \approx (1.6, 1.6)$ — each coordinate within its per-coordinate threshold of $1.7$, but the joint magnitude $\|(1.6, 1.6)\| = 2.26$ along the diagonal direction exceeds the diagonal-direction threshold $\|(1.7, 1.7)\|/\sqrt{2} \cdot \sqrt{2} = 1.7\sqrt{2}/\sqrt{2}$... wait let me reread. The direction-projected threshold along $(1,1)/\sqrt{2}$ is $\sqrt{\hat v^T D_\delta \hat v} = \sqrt{2.89} = 1.70$. The direction-projected stationary RMS along $(1,1)/\sqrt{2}$ is $\sqrt{\lambda_{\max}(\Sigma_\infty)} = \sqrt{5.00} = 2.24$. So along the diagonal direction the agent's RMS mismatch is 2.24, exceeding the direction-projected threshold of 1.70. The agent fails persistence on the bad direction; the per-coordinate form misses it.

**Structural takeaway.** The per-coordinate form is sharp when the matrix tempo $\mathcal{T}$ is diagonal *in the same coordinate basis* as the critical thresholds $D_\delta$. When $\mathcal{T}$ has off-diagonal entries — which is the natural case for AAD-5's matrix gain operator $K = (H_M + H_L)^{-1} H_L$ whenever prior and likelihood do not share an eigenbasis — the per-coordinate form can be unsafe, and the matrix-Loewner form (MP-2) is the canonical persistence condition.

## 5. Composition with existing AAD machinery

### 5.1 Recovery of `#result-persistence-condition`

In the linear scalar case ($\mathcal{T} = \mathcal{T}_0$, $\Sigma_w = \sigma_w^2$, $D_\delta = \delta_0^2$), (MP-2) becomes $\sigma_w^2 / (2\mathcal{T}_0) < \delta_0^2$, equivalently $\mathcal{T}_0 > \sigma_w^2/(2\delta_0^2)$. This matches `#result-persistence-condition` Model S linear operational form per coordinate, recovered exactly.

### 5.2 Recovery of `#result-per-dimension-persistence`

In the diagonal case ($\mathcal{T}, \Sigma_w$ both diagonal in the same basis as $D_\delta$), (MP-2) decomposes per-coordinate: $\sigma_{w,k}^2/(2\mathcal{T}_k) < \delta_{\text{critical},k}^2$, matching `#result-per-dimension-persistence` Model S RMS form exactly. The weak-dimension bottleneck argument from `#result-per-dimension-persistence` Discussion is the diagonal-case instantiation of the matrix-Loewner form's "$\lambda_{\max}$ is the worst-direction safety bound" structural argument.

### 5.3 Cross-reference to `#deriv-fisher-local-update-gain`

The matrix gain operator $K = (H_M + H_L)^{-1} H_L$ from `#deriv-fisher-local-update-gain` is the per-channel primitive that aggregates into $\mathcal{T} = \sum_k \nu^{(k)} K^{(k)}$. The matrix-Loewner persistence condition (MP-2) reads the persistence question off the *aggregate* matrix tempo $\mathcal{T}$, with $\Sigma_w$ encoding the disturbance covariance independent of the agent's correction machinery. The Fisher-local invariance regime is what makes $K$ the right per-channel primitive; the matrix-Loewner condition is what reads persistence off the aggregate.

### 5.4 Information-rate cost extension

`#deriv-persistence-cost` derives the scalar information-rate cost $\dot R \ge n\alpha/2$ for sustaining the ultimate bound under scalar Model S. The matrix-Loewner generalization is straightforward: under matrix tempo $\mathcal{T}$ and matrix disturbance $\Sigma_w$, the sustained information-rate floor is

$$\dot R \;\ge\; \tfrac{1}{2}\, \mathrm{Tr}(\mathcal{T}) \;=\; \tfrac{1}{2}\, \sum_k \lambda_k(\mathcal{T}),$$

— each eigendirection contributes its own $\lambda_k/2$ to the information-rate floor, summing to the trace. The scalar form is the isotropic special case ($\mathcal{T} = \mathcal{T}_0 I$ gives $\mathrm{Tr}(\mathcal{T}) = n \mathcal{T}_0$, matching $\dot R \ge n\alpha/2$). This extension follows by per-eigendirection application of the scalar derivation in `#deriv-persistence-cost`. Worth a follow-on cross-reference Working Note in that segment.

### 5.5 Composition results

The matrix-Loewner form composes naturally with `#form-composition-closure` and `#der-team-persistence`: composite stationary covariance $\Sigma_\infty^{c}$ solves the Lyapunov equation with composite $\mathcal{T}^c$ and $\Sigma_w^c$; the composite Loewner condition $\Sigma_\infty^{c} \prec D_\delta^{c}$ governs persistence at the composite level. Promoting `#der-team-persistence` and `#deriv-critical-mass-composition` to invoke the matrix form directly is a separate cycle item — the per-direction primitive lands here; downstream composition promotion is follow-on work flagged in TODO.

### 5.6 Adversarial extension

The matrix form sharpens `#result-adversarial-tempo-advantage`: an adversary's worst-case targeting strategy in matrix-Loewner terms is to maximize $\lambda_{\max}(D_\delta^{-1/2}\Sigma_w^{\text{adv}} D_\delta^{-1/2} / \mathcal{T}_{\text{effective}})$ where the adversary controls $\Sigma_w^{\text{adv}}$ (the disturbance allocation across directions). The scalar adversarial-advantage exponent generalizes to a matrix-eigenvalue-ratio exponent. Promotion of the adversarial result to the matrix form is follow-on work.

## 6. Epistemic audit

| Claim | Source | Strength |
|---|---|---|
| Stationary covariance solves continuous Lyapunov equation | Itô calculus + linear-SDE stationary analysis (Karatzas-Shreve 1991 §5.6; Khasminskii 2012) | Standard (exact under Hurwitz $\mathcal{T}$) |
| Existence and uniqueness of $\Sigma_\infty \succ 0$ iff $\mathcal{T}$ Hurwitz | Lyapunov stability theory (Bellman 1960 *Introduction to Matrix Analysis* §8.3; Khalil 2002 §4) | Standard |
| Matrix-Loewner task adequacy $\Sigma_\infty \prec D_\delta$ as the canonical persistence condition | This segment's derivation + reduction to existing scalar / per-coordinate forms | Derived (exact under Model S + Hurwitz $\mathcal{T}$ + positive-definite $\Sigma_w$ + diagonal $D_\delta$) |
| Equivalent forms (MP-2a) per-direction, (MP-2b) generalized eigenvalue, (MP-2c) ellipsoid containment | Standard matrix-analysis equivalences (Horn-Johnson 2013 *Matrix Analysis* 2nd ed. §7) | Standard |
| Recovery of scalar / per-coordinate forms | Special-case substitution (§5.1, §5.2) | Derived (exact) |
| Counterexample showing per-coordinate is unsafe under off-diagonal $\mathcal{T}$ (§4) | Constructive 2D example with $\mathcal{T} = \begin{pmatrix}1 & -0.9 \\ -0.9 & 1\end{pmatrix}$ | Derived (explicit numerical computation) |
| Information-rate cost extension $\dot R \ge \tfrac{1}{2}\mathrm{Tr}(\mathcal{T})$ | Per-eigendirection application of `#deriv-persistence-cost` scalar derivation | Sketch (would warrant full derivation if it becomes load-bearing) |
| Composition extension | Mechanical lift of `#form-composition-closure` to matrix-Lyapunov | Sketch (full promotion of composition results is separate cycle) |
| Adversarial extension | Worst-case Loewner spectral argument | Sketch (full promotion of `#result-adversarial-tempo-advantage` is separate cycle) |

**Honest obstructions:**

- **(O1) Hurwitz assumption.** The derivation requires $\mathcal{T}$ Hurwitz (positive-real-part eigenvalues). For non-Hurwitz $\mathcal{T}$, there is no stationary distribution; the question is whether the agent can be brought to Hurwitz by tuning (a question about correction-machinery design, not persistence). This matches the scalar case's $\alpha > 0$ requirement.

- **(O2) Linear dynamics assumption.** The derivation is for the linear case. The nonlinear analog — under sector-bounded $F(\mathcal{T}, \delta)$ with $\delta^T F \ge \alpha \delta^T \delta$ — gives a matrix-sector form $\delta^T F + F^T \delta \succeq 2\alpha I$, which composes with the matrix-Lyapunov machinery via `#deriv-sector-condition`'s template lift. Full matrix-sector treatment is a follow-on; the scalar sector condition's results extend uniformly.

- **(O3) Off-diagonal disturbance.** $\Sigma_w$ with off-diagonal entries is handled directly by the Lyapunov equation — no additional structure needed. The only assumption is $\Sigma_w \succeq 0$ (positive-semidefinite), which is standard for any covariance.

- **(O4) Connection to ultimate-bound machinery.** Under the sector-persistence template `#result-sector-persistence-template`, the scalar ultimate bound is $R^\ast = \rho/\alpha$. The matrix analog is the stationary covariance $\Sigma_\infty$ from the Lyapunov equation. The connection is exact in the linear case; the nonlinear analog is the matrix-sector inequality (O2).

## 7. Sketches of related lifts (out of scope but flagged)

- **Model D matrix lift.** Under deterministic bounded disturbance $\|w_t\| \le \rho$ in a quadratic norm $\|w\|_{M}^2 := w^T M w$ for some $M \succ 0$, the ultimate bound is the ellipsoid $\{ \delta : \delta^T P \delta \le V^\ast \}$ where $P$ solves a continuous Lyapunov-type inequality and $V^\ast$ scales with $\rho^2$. The matrix-Loewner task adequacy is $\{ \delta^T P \delta \le V^\ast \} \subset \{ \delta : \delta^T D_\delta^{-1} \delta \le 1 \}$, i.e., the ultimate-bound ellipsoid is contained in the threshold ellipsoid. Computationally a linear matrix inequality (LMI); follow-on if Model D matrix work becomes load-bearing.

- **Adaptive-gain matrix dynamics.** The adaptive-Kalman-with-Mehra-estimator case from `#deriv-adaptive-gain-dynamics` lifts to matrix $\mathcal{T}_t$ that itself is a state variable. The persistence question becomes a *joint* condition on (primary state, meta-gain state) covariance — augmented-state matrix-Lyapunov machinery. `#deriv-adaptive-gain-dynamics`'s two-timescale composition (Khalil Thm 4.18) extends to matrix coupling directly.

- **Variational matrix form.** Under variational compression `#deriv-variational-sector-condition`'s $\mathrm{KL}(q\|p) \le \varepsilon$, the matrix tempo degrades by an ε-dependent Pinsker factor. Composes with the matrix-Loewner form to give an ε-fidelity matrix persistence condition.

## 8. Promotion recommendation

**Status: succeed-beyond-claim** — the matrix-Loewner persistence condition lifts cleanly, recovers all existing forms as special cases, and is **strictly sharper** than per-coordinate (the §4 counterexample establishes the false-pass risk for per-coordinate). The per-coordinate form's "diagonal-correction assumption is restrictive" Working Note in `#result-per-dimension-persistence` is now closed: the matrix-Loewner form is the canonical anisotropic persistence condition; the per-coordinate form is its diagonal-$\mathcal{T}$-diagonal-$\Sigma_w$-axis-aligned-$D_\delta$ special case.

**Recommended landing:**

1. **New appendix segment `#deriv-matrix-persistence-condition`.** Carries the derivation of §1–§3, the counterexample of §4, the recovery of existing forms from §5.1–§5.2, the cross-reference to `#deriv-fisher-local-update-gain` from §5.3, and an honest scope statement covering the open extensions of §5.4–§5.6 and §7.

2. **Working Note on `#result-persistence-condition`** announcing the matrix lift: scalar form is the isotropic special case; matrix form via `#deriv-matrix-persistence-condition`; the structural-vs-task-adequacy decomposition transfers directly (Hurwitz $\mathcal{T}$ for structural; Loewner $\Sigma_\infty \prec D_\delta$ for task adequacy).

3. **Working Note on `#result-per-dimension-persistence`** closing the open question at line 130: the matrix-Loewner form generalizes per-coordinate to the off-diagonal-$\mathcal{T}$ case; per-coordinate is unsafe (false-pass risk) under cross-dimensional correction; the matrix-Loewner form is the canonical condition.

4. **OUTLINE.md row** in the AAD Appendix section, alongside `#deriv-fisher-local-update-gain` and `#result-sector-persistence-template`.

5. **Cross-references in `#def-adaptive-tempo`** Tensor extension and **`#deriv-fisher-local-update-gain`** Working Notes naming the matrix-Loewner persistence condition as the consumer of the matrix gain primitive.

**Not promoted (out of scope for this cycle):**

- Matrix sector condition / nonlinear correction (§7 sketch).
- Model D matrix lift (§7 sketch).
- Adaptive-gain matrix dynamics (§7 sketch).
- Variational matrix form (§7 sketch).
- Promotion of `#result-adversarial-tempo-advantage` to matrix form (§5.6).
- Promotion of composition results (`#form-composition-closure`, `#der-team-persistence`, `#deriv-critical-mass-composition`) to matrix form (§5.5).
- Information-rate cost matrix extension (§5.4 sketch — could promote if `#deriv-persistence-cost` author judges it ready).

These follow-on items remain as open promotion targets in `TODO.md` Group (b) under the AAD-1 downstream-tensor-tempo-promotion entry.

## 9. References

- Bellman, R. (1960). *Introduction to Matrix Analysis*. McGraw-Hill. §8.3 (Lyapunov stability for matrices).
- Horn, R. A. & Johnson, C. R. (2013). *Matrix Analysis* (2nd ed.). Cambridge University Press. §4.6 (positive definite matrices, Loewner order), §7 (generalized eigenvalue problems).
- Karatzas, I. & Shreve, S. E. (1991). *Brownian Motion and Stochastic Calculus* (2nd ed.). Springer. §5.6 (linear SDEs and stationary distributions).
- Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.). Prentice Hall. §4 (Lyapunov stability), §9 (perturbations and ultimate boundedness).
- Khasminskii, R. (2012). *Stochastic Stability of Differential Equations* (2nd ed.). Springer.
- Lancaster, P. & Tismenetsky, M. (1985). *The Theory of Matrices* (2nd ed.). Academic Press. §13 (matrix equations including Lyapunov equation).

**AAD segments:**

- `#def-adaptive-tempo` — Tensor extension sub-block; matrix tempo $\mathcal{T}$ as $\sum_k \nu^{(k)} K^{(k)}$
- `#deriv-fisher-local-update-gain` — matrix gain operator $K = (H_M+H_L)^{-1}H_L$ as the per-channel primitive
- `#result-persistence-condition` — scalar Model S form, the special case of (MP-2) for isotropic $\mathcal{T}, \Sigma_w, D_\delta$
- `#result-per-dimension-persistence` — diagonal Model S form, the special case of (MP-2) for diagonal-in-coordinate-basis $\mathcal{T}, \Sigma_w$ and axis-aligned $D_\delta$
- `#result-sector-persistence-template` — the (T1)-(T3) template under which this segment's matrix-Loewner result reads as the linear-case template instantiation
- `#deriv-persistence-cost` — scalar information-rate cost $\dot R \ge n\alpha/2$, matrix extension in §5.4
- `#deriv-sector-condition` — nonlinear matrix-sector extension (O2)
- `#deriv-adaptive-gain-dynamics` — adaptive-meta-gain matrix extension (§7)

## Working Notes

- **Discrete-time analog.** The continuous Lyapunov equation $\mathcal{T}\Sigma + \Sigma\mathcal{T}^T = \Sigma_w$ has a discrete-time analog $\Sigma_\infty - A \Sigma_\infty A^T = \Sigma_w$ where $A = I - \eta \mathcal{T}$ for step size $\eta$. The matrix-Loewner condition's discrete form is the same — $\Sigma_\infty \prec D_\delta$ — with $\Sigma_\infty$ solving the discrete-Stein equation. Mechanical; not separately derived here.

- **Non-symmetric $\mathcal{T}$.** Asymmetric $\mathcal{T}$ (e.g., $\mathcal{T} = \begin{pmatrix} 2 & -1 \\ 1 & 0.5 \end{pmatrix}$ from working notes) is handled directly by the Lyapunov equation; the stationary covariance is asymmetric in its eigenbasis but the matrix-Loewner form (MP-2) reads off PSD-dominance regardless. The eigenvalue-of-$\mathcal{T}$ reading becomes more delicate (Jordan blocks, complex eigenvalues) but the stationary covariance result is unaffected.

- **Connection to the `#disc-separability-pattern` and `#disc-additive-coordinate-forcing` meta-segments.** The matrix-Loewner form sits naturally in M2 (separability) — it cleanly separates the structural condition (Hurwitz $\mathcal{T}$) from task adequacy (Loewner $\Sigma_\infty \prec D_\delta$). It also has a (PI)/Čencov reading: the Fisher metric provides a coordinate-invariant inner product, and the matrix-Loewner condition can be written in the Fisher metric without changing its content — though the diagonal $D_\delta$ is an axis-aligned object naturally living in the coordinate basis, so the Fisher-metric reading would require a paired transformation of $D_\delta$.

- **Why the §4 counterexample is the load-bearing content.** Without the counterexample, the matrix-Loewner form would read as "a generalization that happens to agree with per-coordinate in all real cases." The §4 example shows it does NOT always agree — there are real-shape $\mathcal{T}$ matrices (anisotropic + off-coordinate-eigenbasis) for which per-coordinate gives a false-pass. This shifts the matrix-Loewner form from "interesting generalization" to "the safe condition; per-coordinate is unsafe in this regime." The promotion recommendation hinges on this distinction.

- **What would strengthen further (open work).** (i) The non-Hurwitz boundary case (eigenvalue exactly on the imaginary axis) and how persistence degrades smoothly at the boundary; (ii) the matrix-sector nonlinear extension (O2) with rigorous matrix-Lyapunov bounds for non-quadratic Lyapunov functions; (iii) empirical validation on a 2D / 3D simulation matching the §4 counterexample's parameters to confirm the predicted false-pass behaviour of per-coordinate. None of these is blocking for the segment landing.
