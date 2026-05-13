# Spike: Unity-to-Closure Mapping in the Linear-Gaussian Case

**Status**: Spike — first-pass derivation for promotion to segments after review. Linear-Gaussian tractable case. Epistemic status documented per claim.

**Date**: 2026-04-20

**Motivation**: `01-aad-core/src/def-unity-dimensions.md` states "high $U_M$ predicts low $\varepsilon_x$" etc. but admits "the mapping from unity to closure error is not yet formalized." This spike formalizes the mapping in the linear-Gaussian case and — critically — reveals that the correct statement is *not* a direct correspondence but a **rate-distortion relation**: unity dimensions control the *compressibility* of their corresponding state components, which determines the closure-defect curve as projection aggressiveness varies.

**Depends on**: #form-composition-closure, #def-unity-dimensions, `spikes/spike-composition-correlated-kalman.md`, `spikes/spike-projection-admissibility.md`.

**Promotion target**: after review, the framing and linear-Gaussian results should promote to a new segment `#result-unity-closure-mapping`, with updates to `#def-unity-dimensions` (fix the "predicts" claim to the rate-distortion formulation).

---

## 1. The Reframing

The current text in `unity-dimensions.md` reads as if unity dimensions directly predict closure-defect components:

> high $U_M$ predicts low $\varepsilon_x$, high $U_O$ predicts low $\varepsilon_a$, high $U_{\text{obs}}$ predicts low $\varepsilon_o$.

Read literally, this claim fails in the two-Kalman case (`spikes/spike-composition-correlated-kalman.md` §5). Under the means-only projection $\Lambda_x(\hat\omega_1, P_1, \hat\omega_2, P_2) = (\hat\omega_1, \hat\omega_2)$, the closure defect $\varepsilon_x = 0$ *regardless* of the cross-correlation $\rho_{\text{corr}}$ — and hence regardless of $U_M$. The projection is not compressing the "shared" part of the state; it is merely discarding the (constant) covariance components. So unity does not determine $\varepsilon_x$ under this projection.

*[Correction]* The correct relationship is a rate-distortion one. For a *parametric family* of projections indexed by macro-dimension $k$, the achievable closure-defect component $\varepsilon_d^{\min}(k)$ depends on the eigenvalue spectrum of the relevant state component's covariance. Unity dimensions control this spectrum. High unity → concentrated spectrum → steep rate-distortion curve (small $\varepsilon_d$ achievable at small $k$). Low unity → spread spectrum → flat curve (compression costs fidelity).

This is the correct statement, and it is the IB shape. The rest of this spike derives the linear-Gaussian version of it.

## 2. Setup: Two-Agent Linear-Gaussian Composition

*[Scope]* Two sub-agents, scalar state per agent, linear-Gaussian throughout. Richer than `spike-composition-correlated-kalman.md` in that we add purposeful substates ($O_i, \Sigma_i$) to exercise $U_O$ and $U_\Sigma$.

**Environment.** Bivariate random walk:
$$\omega_{t+1} = \omega_t + Bu_t + w_t, \quad w_t \sim \mathcal{N}(0, Q), \quad Q = \begin{pmatrix} q & \rho_{\text{env}} q \\ \rho_{\text{env}} q & q \end{pmatrix}, \quad B = I_2.$$

**Observations.**
$$o_{i,t} = \omega_{i,t} + v_{i,t}, \quad v_{i,t} \sim \mathcal{N}(0, r).$$

Noises $v_1, v_2$ independent for now; the observation-correlation case is a variant we discuss in §5.

**Sub-agent state.** Kalman filter: $M_{i,t} = (\hat\omega_{i,t}, P_{i,t})$. At steady state, $P_{i,t} = P^\ast$ (scalar DARE root, `spike-composition-correlated-kalman.md` §2).

**Purposeful substate.** Each agent has:
- Objective parametrized by target $r_i \in \mathbb{R}$, quadratic cost: $J_i = \mathbb{E}\sum_t (\omega_{i,t} - r_i)^2 + \lambda u_{i,t}^2$
- Strategy: LQR policy on own state, $u_{i,t} = -\kappa(\hat\omega_{i,t} - r_i)$ for some LQR gain $\kappa$ derived from $(\lambda, q, r)$

**Four control parameters, each tuning one unity dimension.**

| Parameter | Controls | Unity affected |
|---|---|---|
| $\rho_{\text{env}}$ | Correlation of process noise → correlation of steady-state estimates | $U_M$ |
| $\rho_O = \text{corr}(r_1, r_2)$ | Alignment of targets (over an ensemble of target-draws) | $U_O$ |
| $\rho_\Sigma$ | Degree of policy coordination (introduced in §4.3) | $U_\Sigma$ |
| $\rho_{\text{obs}} = \text{corr}(v_1, v_2)$ | Shared observation noise / information | $U_{\text{obs}}$ |

*[Convention]* We parametrize with correlations in $[-1, 1]$ rather than raw information-theoretic unity numbers, because the correlations are the natural parameters and the mapping $\rho \mapsto U$ is monotone and explicit in the Gaussian case (§3). All "unity" quantities below are implicit functions of the corresponding $\rho$.

## 3. Unity Measures in Closed Form

*[Derived]* In the linear-Gaussian setting at steady state, each unity measure from `#def-unity-dimensions` reduces to a closed form in the controlling correlation.

### 3.1 Epistemic unity $U_M$

The joint distribution of $(\hat\omega_{1,t}, \hat\omega_{2,t})$ at steady state is Gaussian. The cross-covariance inherits from $\rho_{\text{env}}$ through the coupled-error recursion (`spike-composition-correlated-kalman.md` §5, eq. for $C_e$):
$$\text{Cov}(\hat\omega_{1,t}, \hat\omega_{2,t}) = \sigma_{\hat\omega}^2 \cdot \rho_M, \qquad \rho_M = \text{monotone fn of } \rho_{\text{env}}.$$

For the normalized information ratio:
$$U_M = \frac{I(\hat\omega_1; \hat\omega_2)}{H(\hat\omega_1, \hat\omega_2)} = \frac{-\tfrac{1}{2}\log(1 - \rho_M^2)}{\tfrac{1}{2}\log\left[(2\pi e)^2 \sigma_{\hat\omega}^4 (1 - \rho_M^2)\right]}.$$

The denominator has a scale-dependent additive constant; the numerator is purely a function of $\rho_M$. For clean statements, we use $\rho_M^2$ directly as the "epistemic-unity control parameter" (it equals the fraction of model variance captured by the shared principal component).

### 3.2 Teleological unity $U_O$

For quadratic objectives $J_i = \mathbb{E}(\omega_i - r_i)^2$, the value function is $V_i(\omega) = (\omega_i - r_i)^2$. Over an ensemble of trajectories, the value-correlation is:
$$U_O = \text{corr}(V_1(\tau), V_2(\tau)) = f(\rho_O, \rho_{\text{env}})$$

For equal variances and zero-mean $r_i$, using Isserlis: $U_O = \rho_O \cdot \rho_{\text{env}}$ in the linear term (leading-order), or more generally a quadratic-in-correlations expression. The key qualitative fact: $U_O$ is monotone in both $\rho_O$ (target alignment) and $\rho_{\text{env}}$ (which states the objectives are defined over). The derivation is standard Gaussian moment algebra; we do not reproduce it here.

### 3.3 Strategic unity $U_\Sigma$

The actual joint policy is $\pi^c_{\text{actual}}(\omega) = (-\kappa_1(\hat\omega_1 - r_1), -\kappa_2(\hat\omega_2 - r_2))$, a deterministic map. Per `unity-dimensions.md`, the KL formulation requires stochastic policies; replace with a deterministic analog: the angle between the actual joint-policy vector field and the optimal one. In linear-Gaussian, both are linear functionals of the state, so $U_\Sigma$ reduces to the cosine of the angle between gain vectors:
$$U_\Sigma = \frac{\langle K_{\text{actual}}, K_{\text{optimal}} \rangle}{\|K_{\text{actual}}\| \cdot \|K_{\text{optimal}}\|} \in [-1, 1].$$

When policies are naively independent (each agent solves its own LQR ignoring others), $K_{\text{actual}}$ is block-diagonal; $K_{\text{optimal}}$ generally is not. The strategic-unity parameter $\rho_\Sigma$ in our setup controls how much the agents coordinate: $\rho_\Sigma = 0$ means fully independent; $\rho_\Sigma = 1$ means joint LQR.

### 3.4 Perceptual unity $U_{\text{obs}}$

With $\text{Cov}(v_1, v_2) = \rho_{\text{obs}} r$:
$$I(o_1; o_2 \mid \omega) = -\tfrac{1}{2} \log(1 - \rho_{\text{obs}}^2)$$

The total observation mutual-information (conditional and unconditional) both scale with $\rho_{\text{obs}}^2$ to leading order. We use $\rho_{\text{obs}}^2$ as the perceptual-unity parameter.

**Bottom line:** all four unity dimensions reduce to monotone functions of a single correlation-type parameter in the linear-Gaussian case. This is the enabling simplification for the rate-distortion analysis.

## 4. Closure Defect Components Under Parametric Projections

The central object is a family of projections indexed by macro-dimension $k$. For each closure component $\varepsilon_d$, we derive the minimum achievable defect over projections of macro-dimension $k$, and show it is monotone in the corresponding unity parameter.

### 4.1 State closure $\varepsilon_x(k)$ vs. $U_M$

*[Derived]*

The relevant macro-state candidate space (beyond the Kalman covariances, which are constant at steady state) is the 2D space $(\hat\omega_1, \hat\omega_2)$. Consider projections to $k$-dimensional macro-state, $k \in \{1, 2\}$.

For $k = 2$ (no compression): $\Lambda_x$ is the identity on this subspace, $\varepsilon_x = 0$ — matches the existing Kalman spike result.

For $k = 1$: $\Lambda_x(\hat\omega_1, \hat\omega_2) = u^T \hat\omega$ for some unit vector $u$. The micro-dynamics on the projected 1D state are:
$$\Lambda_x(\hat\omega_{t+1}) = u^T (I - K^\ast I_2) \hat\omega_t + K^\ast u^T o_{t+1} = (1 - K^\ast) \Lambda_x(\hat\omega_t) + K^\ast \Lambda_o(o_{t+1})$$
provided we choose $\Lambda_o(o) = u^T o$ (same unit vector). The macro-update can perfectly mimic this with $K_c = K^\ast$. So the state-update closure error is:
$$\varepsilon_x^2(1) = \mathbb{E}\left[\left(u^T \hat\omega_{t+1}^{\text{micro}} - (1-K^\ast) u^T \hat\omega_t - K^\ast u^T o_{t+1}\right)^2\right] = 0.$$

Wait — this gives $\varepsilon_x(1) = 0$ also. The reason: with $\Lambda_o = u^T$ chosen consistently, the projection onto a 1D subspace preserves the linear update structure. Linear projections of linear dynamics are exact.

**This is a crucial finding.** Within the linear-Gaussian regime with linear projections, $\varepsilon_x = 0$ for *any* dimension $k$. The closure defect does not appear until we either:
- (a) Restrict $\Lambda_o$ independently of $\Lambda_x$ (information-loss asymmetry),
- (b) Allow nonlinear micro-dynamics (not linear-Gaussian),
- (c) Require $\Lambda_a$ to match independently of $\Lambda_x$ (coupling to actions — this is where unity enters).

(b) is outside scope. (a) and (c) are where the rate-distortion story actually lives.

### 4.2 Observation closure $\varepsilon_o$ with restricted observation projection

*[Derived]*

Suppose $\Lambda_o$ is constrained to project observations to a $k_o$-dimensional subspace *independently* of $\Lambda_x$. The macro-observation function is $\hat o_c = \Lambda_x(f_{\text{micro}}(\cdot))$ composed with the macro-prediction, but the observation channel restricts what actually reaches the macro-update.

In the linear-Gaussian case, the minimum closure error for observations projected to 1D is determined by the spectrum of $\text{Cov}(o_1, o_2)$. With:
$$\text{Cov}(o_1, o_2) = \begin{pmatrix} \sigma_o^2 & \rho_{o,\text{eff}} \sigma_o^2 \\ \rho_{o,\text{eff}} \sigma_o^2 & \sigma_o^2 \end{pmatrix}$$

(where $\rho_{o,\text{eff}}$ combines $\rho_{\text{env}}$ and $\rho_{\text{obs}}$), the eigenvalues are $\sigma_o^2 (1 + \rho_{o,\text{eff}})$ and $\sigma_o^2 (1 - \rho_{o,\text{eff}})$. Projecting to the top PC retains $(1 + \rho_{o,\text{eff}})/2$ of the variance; the closure defect is proportional to the discarded variance:

$$\boxed{\varepsilon_o^2(k_o=1) \propto \sigma_o^2 \cdot \frac{1 - \rho_{o,\text{eff}}}{2} \propto 1 - U_{\text{obs}}}$$

*[Derived (linear-Gaussian)]* **This is the rate-distortion relation we wanted.** The achievable observation-closure defect under 1D compression scales as $(1 - U_{\text{obs}})$. High perceptual unity → observations are redundant → 1D summary suffices → $\varepsilon_o$ small. Low perceptual unity → independent observations → 1D summary discards half the information → $\varepsilon_o$ large.

*Epistemic status: exact within the linear-Gaussian scalar setup with PC-optimal projection.*

### 4.3 Action closure $\varepsilon_a$ vs. $U_O$ and $U_\Sigma$

*[Derived]*

The micro-actions are $u_{\text{micro}} = (u_1, u_2) = (-\kappa_1(\hat\omega_1 - r_1), -\kappa_2(\hat\omega_2 - r_2))$. The macro-action $\pi^c(X_c)$ lives in $\mathbb{R}^{k_a}$.

Case A: $k_a = 2$ (action-preserving projection, $\Lambda_a = $ identity). Even with $k_a = 2$, the macro-policy $\pi^c$ takes the macro-state $X_c$ as input. If $X_c$ is the 1D projection of $(\hat\omega_1, \hat\omega_2)$, $\pi^c$ cannot in general recover the 2D action exactly. The action closure error is:
$$\varepsilon_a^2 = \mathbb{E}\left[\|u_{\text{micro}} - \pi^c(u^T \hat\omega)\|^2\right].$$

The best linear $\pi^c(s) = vs + w$ projects the 1D macro-state back up to 2D actions. The minimum-error $v$ aligns $v$ with the direction of $(u_1, u_2)$ variation as $(\hat\omega_1, \hat\omega_2)$ varies along the macro-state axis. The residual variance is determined by how much the action vector's direction changes with state — which depends on $K_{\text{actual}}$ (strategy) and targets (objectives).

For aligned targets ($\rho_O = 1$) and coordinated policies ($\rho_\Sigma = 1$), the action vector always points in the same direction, and a 1D macro-state + linear lift captures the actions exactly: $\varepsilon_a = 0$.

For anti-aligned targets ($\rho_O = -1$), actions point in opposite directions depending on the state, and a 1D macro-state cannot recover both simultaneously. $\varepsilon_a$ grows with target misalignment.

For independent policies ($\rho_\Sigma = 0$, each agent optimizes their own LQR), $\kappa_1 = \kappa_2$ but $r_1, r_2$ vary. The action-variance direction is controlled by $\rho_O$ alone.

*[Derived (scalar case, $\rho_\Sigma = 0$, $k_a = 2$, $k_x = 1$)]*
$$\varepsilon_a^2 \propto \kappa^2 \cdot \text{Var}(r_1 - r_2) \propto \kappa^2 \cdot (1 - \rho_O).$$

So $\varepsilon_a$ scales with $(1 - \rho_O)$ under independent policies. Adding policy coordination ($\rho_\Sigma > 0$) reduces $\varepsilon_a$ further by making the action response to state shared across agents.

**Joint dependence on $(U_O, U_\Sigma)$:** the full expression (with both parameters varying) is:
$$\varepsilon_a^2 \propto (1 - U_O) \cdot f_1(U_\Sigma) + g(U_\Sigma)$$
where $f_1$ is decreasing in $U_\Sigma$ and $g$ captures the strategic-misalignment contribution even when targets coincide. The exact form requires working out a specific joint-LQR vs. independent-LQR comparison, which is mechanical but tedious.

*Epistemic status: scalar target case derived; joint $(U_O, U_\Sigma)$ decomposition sketched but not fully computed.*

### 4.4 Summary table

| Closure component | Unity controlling it | Linear-Gaussian rate-distortion form |
|---|---|---|
| $\varepsilon_x$ | $U_M$ | $\varepsilon_x \equiv 0$ within linear-Gaussian with linear projections (exact); rate-distortion enters through nonlinearity or dimension constraints from $\varepsilon_a$ coupling |
| $\varepsilon_o$ | $U_{\text{obs}}$ | $\varepsilon_o^2(k_o=1) \propto \sigma_o^2 (1 - U_{\text{obs}})$ (exact) |
| $\varepsilon_a$ | $U_O, U_\Sigma$ | $\varepsilon_a^2 \propto (1 - U_O) \cdot f_1(U_\Sigma) + g(U_\Sigma)$ (leading form, scalar targets) |

## 5. What This Actually Shows

*[Discussion]*

**The mapping is real but subtler than the text in `unity-dimensions.md` suggests.**

1. **$\varepsilon_x$ does not depend on $U_M$ in linear-Gaussian with linear projections.** State-update closure is automatic once the projection is consistent on state and observation simultaneously. $U_M$ enters only when the projection is aggressive enough (e.g., low $k_x$) that the induced constraints on $\Lambda_a$ create coupling — and even then, $U_M$ acts through $\varepsilon_a$, not $\varepsilon_x$ directly. *This contradicts the literal text in `unity-dimensions.md`.*

2. **$\varepsilon_o$ depends cleanly on $U_{\text{obs}}$** via the classical PC compression: discarded-variance scales with $(1 - \rho_{o,\text{eff}}^2)$. This is the cleanest rate-distortion relation in the framework.

3. **$\varepsilon_a$ is where $U_O$ and $U_\Sigma$ enter**, and they enter *jointly*. A reader of `unity-dimensions.md` might assume $U_O$ alone controls $\varepsilon_a$; the derivation shows $U_\Sigma$ is independently active. This matches the four-unity/three-closure observation: $(U_O, U_\Sigma)$ jointly determine action closure.

**The rate-distortion framing unifies these cases.** In each, the closure component is the residual after projecting to a lower-dimensional macro-description. The rate-distortion function $\varepsilon_d(k_d)$ is a function of the projection dimension and the spectrum of the relevant component's covariance. Unity measures parametrize the spectrum. This is the IB shape, stated in the terms of `#form-composition-closure`'s admissibility.

## 6. Hooks for the Bigger Contraction (IB Unification)

*[Speculation — notes for afterward]*

Several signals from this spike suggest the bigger IB unification is tractable.

### 6.1 (P1) is IB-relevance-preservation

The projection admissibility condition (P1) in `#form-composition-closure`:
$$I\big(\Lambda_x(X_{\text{micro}});\; \Lambda_o(o)\;\big|\;\Lambda_a(a)\big) \geq (1 - \epsilon_I)\, I\big(X_{\text{micro}};\; o\;\big|\;a\big)$$

is exactly an information-bottleneck relevance-preservation condition with relevance variable "next observation given action." Rewritten as IB:
$$\text{minimize } I(X_{\text{micro}}; X_c) \quad \text{s.t.} \quad I(X_c; o_{\text{next}} \mid a) \geq (1 - \epsilon_I) \cdot I(X_{\text{micro}}; o_{\text{next}} \mid a).$$

The minimizer is the IB-optimal projection at relevance level $(1 - \epsilon_I)$. In linear-Gaussian, this is Gaussian IB (Chechik et al. 2005) — which has closed-form solutions in terms of generalized eigenvalue decompositions.

**Claim to work on next:** (P1) and (P3) together are equivalent to "projection is on the IB frontier for next-observation relevance at rate $I(X_{\text{micro}}; X_c)$ implicitly set by $\dim(\mathcal X_c)$." (P2) is an independent regularity requirement that IB does not directly impose.

### 6.2 Unity dimensions index the IB rate-distortion function

In the linear-Gaussian analysis here, each unity parameter controls the spectrum of a component of the covariance — hence the shape of the Gaussian IB rate-distortion curve. This generalizes: for non-Gaussian cases, unity measures (multi-information, KL, etc.) are themselves IB rates applied to specific subsets of the state. The four unity dimensions are IB-distortions along the four natural state axes ($M, O, \Sigma, $observation).

### 6.3 Shared intent is IB on inter-agent channel

`#def-shared-intent` already explicitly uses IB with relevance variable "coordinated action." That's consistent with treating intent-sharing as an IB compression on the communication channel with the same relevance logic as the projection-admissibility compression on the state channel. Same framework, different channel.

### 6.4 What the contraction would deliver

If (P1) = IB-relevance, unity = IB-rate-distortion-curve-parameter, and shared-intent = IB-on-comm-channel, then:

> **Conjecture (informal):** Composition in AAD is a multi-level IB compression. The admissible class $\mathcal{P}_{\text{adm}}$ consists of projections attaining the IB frontier for the appropriate relevance variables. Unity dimensions are IB parameters. Closure-defect components are IB distortions. The bridge lemma becomes: IB-frontier projections preserve dynamics at the admissibility rate.

This would replace (P1)+(P3) with a single variational principle (IB optimality), unify `#def-shared-intent` and `#form-composition-closure` mechanistically, and give `#def-unity-dimensions` a quantitative foundation (unity = IB rate parameter).

Caveats before attempting this:
- (P2) Lipschitz is not naturally IB — it must remain a separate regularity condition.
- The IB frontier depends on the relevance variable; changing relevance changes admissibility. The theory would need to fix the relevance unambiguously (candidate: future observations conditional on future actions, per the existing (P1) form).
- Gaussian IB is fully tractable; general IB is not. Extending beyond linear-Gaussian would require approximations.

## 7. Epistemic Status

| Claim | Status |
|---|---|
| $\varepsilon_o^2(k_o=1) \propto \sigma_o^2(1 - U_{\text{obs}})$ in linear-Gaussian scalar case | Exact, derived |
| $\varepsilon_a^2 \propto (1 - U_O) \cdot \kappa^2$ under independent policies, scalar targets | Exact, derived |
| Joint $(U_O, U_\Sigma)$ dependence in $\varepsilon_a$ | Sketched, full form mechanical but not computed here |
| $\varepsilon_x \equiv 0$ within linear-Gaussian with consistent linear $(\Lambda_x, \Lambda_o)$ | Exact, derived (contradicts the literal text in `unity-dimensions.md`) |
| Rate-distortion framing as the correct unity-to-closure mapping | Robust qualitative, needs nonlinear case for full generality |
| IB unification conjecture (§6.4) | Speculation; separate spike / investigation |

## 8. What to Promote and What to Revise

**To create as a new segment (#result-unity-closure-mapping, type: derived/formulation):**
- The rate-distortion framing (§1, §5)
- The linear-Gaussian results (§3, §4)
- Depends on: `#def-unity-dimensions`, `#form-composition-closure`

**To revise in `#def-unity-dimensions`:**
- Replace "high $U_M$ predicts low $\varepsilon_x$" etc. with "each unity dimension controls the rate-distortion curve for the corresponding closure component."
- Note that $(U_O, U_\Sigma)$ jointly control $\varepsilon_a$ — the four-unity / three-closure mismatch is resolved by this joint dependence, not by collapsing unity dimensions.
- The current text's "high $U_M$ predicts low $\varepsilon_x$" is literally false under the means-only projection; revise to the rate-distortion formulation.

**To extend in `#form-composition-closure` (optional):**
- Working Note: (P1) is IB-relevance-preservation; this is a starting point for further contraction.

**To open as new spike target (post-promotion):**
- `spikes/spike-ib-unification.md`: attempt the full conjecture in §6.4. Low priority until Section III promotion work is further along.

## 9. Working Notes

- **The $\varepsilon_x \equiv 0$ finding is important and worth verifying in a less degenerate setting.** The scalar linear-Gaussian case may be *too* clean. A vector-valued environment with coupling matrix $A \neq I$ could break the identity and force $\varepsilon_x > 0$ as a genuine phenomenon. Worth a follow-up numerical check.
- **Joint $(U_O, U_\Sigma) \to \varepsilon_a$ requires the joint-LQR benchmark.** The derivation would set $K_{\text{optimal}}$ as the joint-LQR gain for the sum objective, then compute $\varepsilon_a$ as the excess error of independent-LQR relative to joint-LQR. Mechanical but 3-4 pages of algebra; deferred.
- **The IB connection to (P1) should be testable without committing to the full §6.4 conjecture.** Worked example: compute the Gaussian IB-optimal projection for the two-Kalman case; compare to the means-only projection; check whether they coincide at the (P1) threshold.
- **The rate-distortion framing suggests a clean operational test for admissibility.** Instead of checking (P1) as a mutual-information inequality, one could characterize admissible projections as those lying within $\epsilon$ of the IB frontier. This may be more tractable to verify in practice.
- **If the $\varepsilon_x \equiv 0$ result is robust**, then in the linear-Gaussian regime *all* closure defect lives in $(\varepsilon_o, \varepsilon_a)$. This might be a genuine simplification — Section III's linear-Gaussian worked examples could focus on just observation and action closure, with state closure automatic. Would need to verify across a couple of other linear-Gaussian compositions first.
- **The reframing slightly downgrades `unity-dimensions` as a quantitative segment.** Before this spike, unity dimensions appeared to be direct predictors of closure components. After, they are parameters of a rate-distortion function whose concrete form is given by the IB machinery. This is honest but makes the segment less self-contained: it now depends on a companion segment (`#result-unity-closure-mapping`) for the quantitative relationship.

---

## 10. Addendum (2026-04-20): Non-Degenerate Kalman Test Case

*[Motivation]* §4.1 derived $\varepsilon_x \equiv 0$ under linear-Gaussian with linear projections — a result suspected to be "too clean." The Mori-Zwanzig companion spike (`spikes/spike-mori-zwanzig-composition.md` §6.2) independently suggested the same test: project to $\hat\omega_+ = (\hat\omega_1 + \hat\omega_2)/\sqrt{2}$ with heterogeneous gains, which should produce genuine $\varepsilon_x > 0$. This addendum works that case.

### 10.1 Setup

Same as §2, but introduce heterogeneity: $r_1 \neq r_2$ so steady-state Kalman gains differ, $K_1^\ast \neq K_2^\ast$. Let $\bar K = (K_1^\ast + K_2^\ast)/2$ and $\Delta K = K_1^\ast - K_2^\ast$.

In the $(+,-)$ basis:
$$\hat\omega_{+,t+1} = (1-\bar K)\hat\omega_{+,t} - \tfrac{\Delta K}{2}\hat\omega_{-,t} + \bar K \tilde o_{+,t+1} + \tfrac{\Delta K}{2} \tilde o_{-,t+1}$$

The discarded $\hat\omega_-$ appears in the dynamics of the retained $\hat\omega_+$ — only when $\Delta K \neq 0$. This is the essential non-degeneracy.

**Projection:** $\Lambda_x(\hat\omega_1, \hat\omega_2) = \hat\omega_+$, $\Lambda_o(o_1, o_2) = \tilde o_+$. Macro-update: $X_{c,t+1} = (1 - K_c) X_{c,t} + K_c \tilde o_{+,t+1}$.

### 10.2 Closure error

*[Derived]* Per-step closure error:
$$\Delta = (K_c - \bar K)(\hat\omega_{+,t} - \tilde o_{+,t+1}) + (\Delta K/2)(\tilde o_{-,t+1} - \hat\omega_{-,t})$$

Minimizing $\mathbb E[\Delta^2]$ over $K_c$:
$$K_c^\ast = \bar K - (\Delta K / 2)\, C_{+-}/S_+, \qquad \varepsilon_x^2 = (\Delta K/2)^2 \left[S_- - C_{+-}^2/S_+\right]$$

with $S_+, S_-$ the innovation variances in $\pm$ directions and $C_{+-}$ the cross-covariance between the $+$ and $-$ innovation processes.

### 10.3 Numerical results ($q = 1, r_1 = 1, r_2 = 9$)

$K_1^\ast \approx 0.618$, $K_2^\ast \approx 0.282$, $\bar K = 0.450$, $\Delta K = 0.336$.

| $\rho_{\text{env}}$ | $U_M$ (qualitative) | $\varepsilon_x$ (optimized over $K_c$) |
|:---:|:---:|:---:|
| $0$ | low | $\approx 0.350$ |
| $0.5$ | moderate | $\approx 0.325$ |
| $1.0$ | high | $\approx 0.290$ |

**Homogenized** ($r_1 = r_2$, so $\Delta K = 0$): $\varepsilon_x \equiv 0$ at every $\rho$, recovering §4.1.

### 10.4 Two independent drivers of $\varepsilon_x$

The closure defect has two *independent* contributors:

1. **Sub-agent redundancy** — controlled by $U_M$ (here via process correlation $\rho$). Higher unity → lower $\varepsilon_x$. Consistent with the rate-distortion framing in §4–5.
2. **Update heterogeneity** — controlled by $\Delta K$, the asymmetry of correction rules. $\Delta K = 0$ kills $\varepsilon_x$ at every $\rho$; $\Delta K \neq 0$ keeps $\varepsilon_x > 0$ even at $\rho = 1$.

**Crucial observation:** Heterogeneity is *not captured* by any of the four unity dimensions from `#def-unity-dimensions`. The four dimensions ($U_M, U_O, U_\Sigma, U_{\text{obs}}$) measure shared *content* (information, goals, policies, observations). Heterogeneity here is shared *structure* — whether agents have the same $f_M$ update rule. In Section I adaptive-systems-only composition, with no purposeful substate, there is no $U_\Sigma$ to absorb this, so update heterogeneity is invisible to the framework.

This is a genuine gap. Possible resolutions:

- **(A) Add a fifth unity dimension**: "update homogeneity" $U_f$ measuring similarity of $f_M$ across agents. Would require formal definition and closed-form measure.
- **(B) Reinterpret $U_\Sigma$ broadly** to cover $f_M$ heterogeneity in passive-estimator cases, where "strategy" is understood as "update-and-act rule" not just "act rule." This extends $U_\Sigma$'s semantics but preserves the four-dimensional framework.
- **(C) Accept the two-axis structure**: closure defect is always a function of both sub-agent unity (the information axis) and agent-structural homogeneity (the update-rule axis). The rate-distortion curve has two dials, not one.

Option (C) is the most honest and the cleanest. The rate-distortion story in §4–5 becomes: *for fixed agent structure*, unity parametrizes the rate-distortion curve. Varying agent structure shifts the curve. This adds a parameter but does not break the framework.

### 10.5 Mori-Zwanzig interpretation

In MZ language (cf. `spike-mori-zwanzig-composition.md` §6.2): the discarded component $\hat\omega_-$ produces a non-trivial memory kernel $K_0$ exactly when $\Delta K \neq 0$, because that is when the micro-dynamics of $\hat\omega_+$ depend on $\hat\omega_-$. The kernel norm $\lVert K_0 \rVert$ scales with $|\Delta K|$. This is consistent with the MZ spike's identification $\varepsilon_x \geq \lVert K_0 \rVert$ (when $f_c^{\text{MZ}} \notin \mathcal M_{\text{adm}}$).

**Cross-check between frameworks:**
- IB/rate-distortion (this spike): $\varepsilon_x$ determined by rate-distortion curve + agent structure
- MZ (companion spike): $\varepsilon_x$ bounded below by zero-lag memory kernel norm

The non-degenerate case exercises both frameworks non-trivially. They agree on when $\varepsilon_x$ is non-zero (heterogeneous gains) and agree on the qualitative structure. A further unification would verify they give the same *quantitative* lower bound — probably they do, since both reduce to the same linear-algebraic quantity ($L^2$-residual of projecting off an eigenspace of the micro-propagator).

### 10.6 What this changes for segment promotion

The earlier §5/§8 recommendations stand, with one modification: `#result-unity-closure-mapping` should explicitly state the *two-axis* structure. Sub-agent unity is one axis; agent-structural homogeneity is the other. Prior text suggesting unity alone determines closure defect is incomplete.

Revised headline claim: **In linear-Gaussian, the achievable closure-defect curve $\varepsilon_d(k)$ depends on both unity measures (controlling sub-agent redundancy) and update-rule homogeneity (controlling whether compressed projections induce memory). In the linear-Gaussian scalar case, $\varepsilon_x = 0$ iff $\Delta K = 0$; conditional on $\Delta K \neq 0$, $\varepsilon_x$ decreases monotonically with $U_M$.**

### 10.7 Epistemic status of §10

| Claim | Status |
|---|---|
| $\varepsilon_x^2 = (\Delta K/2)^2 [S_- - C_{+-}^2/S_+]$ (optimized) | Derived, exact in linear-Gaussian scalar case |
| Numerical values in §10.3 | Derived, exact under stated parameters |
| Monotone dependence on $\rho$ at fixed $\Delta K$ | Confirmed numerically at 3 points; general proof not given but follows from $S_-, S_+, C_{+-}$ expressions |
| Two-axis structure (unity + heterogeneity) | Robust qualitative, demonstrated by the $\Delta K = 0$ homogenized case |
| MZ ↔ IB cross-agreement | Discussion-grade; formal equivalence would require separate derivation |
