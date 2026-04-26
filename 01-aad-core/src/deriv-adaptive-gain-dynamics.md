---
slug: deriv-adaptive-gain-dynamics
type: derivation
status: conditional
depends:
  - emp-update-gain
  - der-gain-sector-bridge
  - deriv-gain-sector
  - deriv-sector-condition
  - result-sector-condition-stability
  - result-sector-persistence-template
  - der-recursive-update
stage: draft
---

# Derivation: Adaptive-Gain Dynamics — A2' Under a Learning Gain

AAD's gain structure ( #emp-update-gain, #der-gain-sector-bridge) derives the optimal gain $\eta^\ast$ per regime — the gain is a function of the noise model, chosen to minimize one-step mismatch variance. Real adaptive agents often *learn the noise model itself* (adaptive Kalman), *switch regimes* (IMM), *adapt step-size online* (RMSProp / Adam), or *optimize gain across tasks* (MAML). The gain becomes a state variable with its own update dynamics. The question is whether the sector-persistence machinery extends to this case, and where inside the A2' sub-scope partition adaptive gain sits. The result: sub-scope $\alpha$ splits into $\alpha_1$ (fixed-gain per Prop B.3) and $\alpha_2$ (adaptive-gain under four derivable conditions named (MG-1)–(MG-4)), with sub-scope $\beta$ catching the rest. The two-timescale argument is an augmented-state Lyapunov composition (standard Khalil Thm 4.18), not a Tikhonov reduction — the primary and meta-gain sector conditions compose rather than one being eliminated.

## Formal Expression

### Augmented-state setup

Treat the gain $K_t$ as state. Define $\tilde K_t = K_t - K^\ast$ (error relative to a target optimal gain, specified per case: Riccati-steady-state for adaptive Kalman, EMA-fixed-point for RMSProp, etc.). The augmented state is $z_t = (\delta_t, \tilde K_t)$. Primary and meta-gain dynamics:

$$\dot\delta = -F(\delta; K^\ast + \tilde K) + w(t), \qquad \dot{\tilde K} = -\Phi(\tilde K, \delta) + v(t)$$

where $F$ is the primary correction function (depending on the current gain via its argument), $\Phi$ is the gain-update contraction, $w$ is primary-channel disturbance, $v$ is gain-channel disturbance (estimator noise, innovation variability, etc.).

### Meta-gain sector conditions (MG-1)–(MG-4)

*[Formulation (meta-gain-conditions, extend A2' to adaptive-gain setting)]*

**(MG-1) Primary sector floor under bounded gain error.** There exist $\underline\alpha \gt 0$ and $r_K \gt 0$ such that for all $\lVert\tilde K\rVert \leq r_K$ and $\lVert\delta\rVert \leq R$:

$$\delta^T F(\delta; K^\ast + \tilde K) \geq \underline\alpha \lVert\delta\rVert^2$$

— A2' uniform in the gain-error ball. The sector floor is preserved across the gain-state range the meta-learner visits.

**(MG-2) Meta-gain sector condition.** The gain-update map $\Phi$ satisfies (T1) (zero at $\tilde K = 0$) and a local sector bound:

$$\tilde K^T \Phi(\tilde K, \delta) \geq \alpha_K \lVert\tilde K\rVert^2 \quad \text{for } \lVert\tilde K\rVert \leq r_K, \text{ uniformly in } \lVert\delta\rVert \leq R$$

with $\alpha_K \gt 0$. This is a sector condition in the gain-error state — the adaptive-gain analog of A2' itself.

**(MG-3) Timescale separation.** $\alpha_K \ll \underline\alpha$. The gain adapts slower than the primary state contracts. This is #der-temporal-nesting's convergence constraint transcribed onto Lyapunov decay rates instead of event rates.

**(MG-4) Coupling boundedness.** The gain-channel disturbance $v(t)$ has bounded contribution from the primary state:

$$\mathbb E[\lVert v(t)\rVert^2 \mid \delta] \leq \sigma_{K,0}^2 + c_v \lVert\delta\rVert^2$$

for some $c_v \geq 0$. (MG-4) with $c_v = 0$ is clean two-timescale decoupling; $c_v \gt 0$ is $\delta$-coupled meta-gain disturbance (RMSProp near minimizer), requiring fixed-point closure.

### Composed persistence result

*[Derived (augmented-state-persistence, from sector-persistence-template applied twice with coupling)]*

Under (MG-1)–(MG-4), the augmented state $z = (\delta, \tilde K)$ is ultimately bounded in mean square. The Lyapunov candidate $V(z) = \tfrac{1}{2}\lVert\delta\rVert^2 + \tfrac{c}{2}\lVert\tilde K\rVert^2$ for appropriate weight $c$ satisfies, along trajectories:

$$\dot V \leq -\underline\alpha \lVert\delta\rVert^2 - c\alpha_K \lVert\tilde K\rVert^2 + \rho\lVert\delta\rVert + c(\sigma_{K,0} + \sqrt{c_v}\lVert\delta\rVert)\lVert\tilde K\rVert$$

Complete-the-square on the cross term (requires $c\sqrt{c_v}$ small compared to $\underline\alpha \cdot c\alpha_K$, i.e., (MG-3) timescale separation plus (MG-4) coupling smallness):

$$\dot V \leq -\tfrac{\underline\alpha}{2}\lVert\delta\rVert^2 - \tfrac{c\alpha_K}{2}\lVert\tilde K\rVert^2 + \frac{\rho^2}{2\underline\alpha} + \frac{c\sigma_{K,0}^2}{2\alpha_K}$$

Standard Lyapunov ultimate-boundedness (Khalil 2002 Thm 4.18) applied to the augmented state gives the composed persistence bound. Both $\delta$ and $\tilde K$ are ultimately bounded with explicit bounds in $(\underline\alpha, \alpha_K, \rho, \sigma_{K,0}, c_v)$. $\square$

### A2' sub-scope partition: $\alpha_1$ / $\alpha_2$ / $\beta$

*[Formulation (sub-scope-refinement)]*

The adaptive-gain analysis refines #deriv-sector-condition's A2' sub-scope partition into three tiers:

**Sub-scope $\alpha_1$ — fixed-gain, A2' derived.** #der-gain-sector-bridge Prop B.3's current scope: the gain $K$ is treated as a static function of fixed noise model parameters. A2' is derived from B1 directional fidelity. Covers Kalman with known $(Q, R)$, conjugate-Bayesian updates, exponential-family MLE, linear correction with PD $KH$, strongly-convex-gradient fixed-step-size.

**Sub-scope $\alpha_2$ — adaptive-gain, A2' derived through augmented-state Lyapunov.** When (MG-1)–(MG-4) hold with all four conditions derivable from the update-rule structure:

- Adaptive Kalman with Mehra-type innovation-based $(Q, R)$ estimator under timescale separation
- RMSProp/Adam with strongly-convex loss, large $\beta$ (slow EMA), and coupling-smallness; AMSGrad fix (Reddi et al. 2018) structurally a meta-gain repair preserving (MG-1)
- Any adaptive-gain scheme admitting a clean (MG-1)–(MG-4) derivation from the update rule

For these, A2' is derived at the augmented-state level, not merely assumed. Setting $\tilde K \equiv 0$ recovers sub-scope $\alpha_1$ cleanly.

**Sub-scope $\beta$ — A2' assumed (possibly under scope narrowing).** When any of (MG-1)–(MG-4) must be assumed per-agent rather than derived. Concrete instances:

- MAML outer loop: meta-loss non-convex even under per-task convexity (Fallah et al. 2020), so (MG-2) cannot be derived from per-task structure. Inner loop is $\alpha_1$; outer loop is $\beta$.
- IMM regime transitions: (MG-1) fails uniformly in time during posterior-reconcentration windows of duration $\tau_{\text{IMM}}$. Between-transition regime is $\alpha_2$; across-transition window is $\beta$ (scope narrowing via dwell-time + impulsive-disturbance absorption).
- Adam without AMSGrad on ill-conditioned problems: (MG-1) fails under aggressive-$\beta$ + small-gradient-noise (Reddi et al. 2018 counterexample).
- Rule-based / PID / human-judgment adaptive gains: no structural argument for either (MG-1) or (MG-2); both must be assumed.

This refinement preserves the existing A2' sub-scope $\alpha$ as a specialization ($\alpha_1$) and identifies a derivable adaptive-gain extension ($\alpha_2$) with honest fallback to $\beta$ when the derivability conditions fail.

### Structured cases

*[Derivation (case-adaptive-kalman-alpha2)]*

**Case A — Adaptive Kalman with Mehra estimator.** Scalar linear-Gaussian setting with unknown $(Q^\ast, R^\ast)$. The innovation-based Mehra estimator (Mehra 1970, 1972; Dunik et al. 2021 for identifiability) yields $\hat Q_t, \hat R_t$ from a sliding-window autocorrelation of the innovation sequence. For window length $N$, the gain-update map to first order in $\tilde K$ is a scalar Ornstein-Uhlenbeck process:

$$\tilde K_{t+1} = (1 - \lambda_N) \tilde K_t + \lambda_N \eta_t^{\text{inn}}$$

with $\lambda_N \asymp 1/N$ (contraction rate set by window length) and $\eta^{\text{inn}}$ zero-mean innovation noise with variance $O(1/N)$. This is itself an instance of #result-sector-persistence-template with:

- (T1): $\Phi_K(0) = 0$ — when gain is optimal, estimator returns optimal in expectation.
- (T2): $\tilde K \cdot \Phi_K(\tilde K) = \lambda_N \tilde K^2$, so $\alpha_K = \lambda_N$.
- (T3-S): bounded stochastic disturbance on the gain channel.

Prop A.1S applied to the meta-gain channel gives $R^\ast_{S,K} \asymp 1/\sqrt N$ — the classical Mehra asymptotic rate, now derived from (MG-2). Primary sector floor is preserved: $\underline\alpha = K^\ast - \lvert\tilde K\rvert_{\max}$ via triangle. Composed persistence via augmented-state Lyapunov gives $O(1/\sqrt N)$ degradation from the fixed-gain case. **This case is derived at sub-scope $\alpha_2$.**

Under Mehra non-identifiability (rank-deficient transform matrix; see Zagrobelny-Rawlings 2015, Dunik et al. 2021), (MG-2) fails structurally — an instance of the #disc-identifiability-floor pattern on the meta-gain channel.

*[Derivation (case-rmsprop-alpha2-conditional)]*

**Case B — RMSProp on strongly-convex loss.** The per-step effective step is $\eta_t^{\text{eff}} = \eta_t/(\sqrt{v_t} + \varepsilon)$ where $v_t = \beta v_{t-1} + (1-\beta)\hat g_t^2$ tracks the second moment. Near the minimizer, $\mathbb E[\hat g_t^2] \to \lVert\nabla L\rVert^2 + \sigma_g^2$. Writing $\tilde v_t = v_t - \mathbb E[\hat g_t^2]$:

$$\tilde v_{t+1} = \beta \tilde v_t + (1-\beta)(\hat g_t^2 - \mathbb E[\hat g_t^2]) + \beta(\mathbb E[\hat g_{t-1}^2] - \mathbb E[\hat g_t^2])$$

The first two terms give (MG-2) with $\alpha_v = 1 - \beta$ and $\sigma_v^2 \asymp (1-\beta)^2 \text{Var}(\hat g_t^2)$. The third is $\delta$-coupled: $\mathbb E[\hat g_t^2]$ depends on $\delta$ through $\lVert\nabla L\rVert^2$, giving $c_v \gt 0$ in (MG-4).

Composed persistence under design conditions $\beta$ close to 1 (slow EMA) and $\lambda_{\max}(H) \cdot R^\ast_S \ll \sqrt{\sigma_g^2}$ (coupling smallness): fixed-point closure between primary $R^\ast_S$ and meta-gain $R_v$ yields existence of a stable equilibrium. Sub-scope $\alpha_2$ under design conditions.

Outside those conditions (aggressive $\beta$ + ill-conditioning + small gradient noise — Reddi et al. 2018's Adam counterexample), fixed-point iteration diverges. **AMSGrad's monotonicity on $v_t$ is structurally a meta-gain repair that restores (MG-1) by construction** — preserving sub-scope $\alpha_2$ by forcing a condition (MG-1) the vanilla algorithm would violate.

*[Sketch (case-imm-alpha2-plus-dwelltime)]*

**Case C — IMM / regime-switching Kalman.** Mixture of $M$ Kalman filters with Markov-transition posterior over regimes. Between regime transitions, the posterior concentrates on the true regime and the effective gain approaches the regime-conditional optimum: sub-scope $\alpha_2$ in the steady portion with Mehra-style derivation. Across regime transitions, posterior re-concentration takes $\tau_{\text{IMM}} \asymp 1/(1-p)$ observations (self-loop probability $p$); during this window (MG-1) fails uniformly in time — the gain can be aligned with the wrong regime. Scope narrowing via dwell-time + impulsive-disturbance absorption: regime stable for $T_{\text{dwell}} \gg \tau_{\text{IMM}}$, transient mismatch bounded by counting-argument. Sub-scope $\alpha_2$ between-transition; $\beta$ across-transition.

*[Classification (case-maml-mixed)]*

**Case D — MAML inner-outer structure.** Inner loop (per-task adaptation with $k$ gradient steps) — sub-scope $\alpha_1$ from Prop B.4 under per-task convexity. Outer loop (meta-parameter update via gradient on meta-loss $\sum_i L_i(\theta_i'(\theta))$) — Fallah et al. 2020's convergence analysis shows the meta-loss is non-convex even under per-task convexity because of the non-linearity of inner-loop updates in $\theta$. (MG-2) is not derivable from per-task structure. Outer loop is $\beta$ — A2' assumed per basin.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Augmented-state setup $z = (\delta, \tilde K)$ with coupled sector dynamics | Definitional reformulation extending #der-recursive-update + #emp-update-gain | Formulation choice |
| (MG-1) primary sector floor under bounded gain error | Derived in Cases A and B via triangle / $\varepsilon$-floor arguments | Derived (per case, conditional on regularity) |
| (MG-2) meta-gain sector condition | Derived in Cases A (Mehra OU) and B (EMA second-moment) from estimator structure | Derived (per named case) |
| (MG-3) timescale separation $\alpha_K \ll \underline\alpha$ | Design condition on estimator window / EMA rate; Lyapunov decay-rate transcription of #der-temporal-nesting | Formulation (design condition; violations dissolve composition) |
| (MG-4) coupling boundedness of gain-channel disturbance | Decoupled ($c_v = 0$) in Case A; $\delta$-coupled ($c_v \gt 0$) in Case B with fixed-point closure | Derived (per case) |
| Composed augmented-state persistence under (MG-1)–(MG-4) | Quadratic Lyapunov on $z$ + Khalil 2002 Thm 4.18 ultimate-boundedness | Derived (conditional on MG-1 through MG-4) |
| Sub-scope refinement $\alpha_1$ / $\alpha_2$ / $\beta$ | Extension of current #deriv-sector-condition $\alpha/\beta$ partition | Formulation (classification) |
| $\alpha_2$ reduces to $\alpha_1$ under $\tilde K \equiv 0$ | Direct substitution into augmented-state setup | Proved |
| Case A (adaptive Kalman): sub-scope $\alpha_2$ under identifiability + window-length timescale separation | Mehra OU-form of estimator + Prop A.1S | Derived |
| Case B (RMSProp): sub-scope $\alpha_2$ under design conditions; $\beta$ otherwise; AMSGrad as meta-gain repair | EMA second-moment derivation + fixed-point closure + Reddi et al. 2018 counterexample | Derived (conditional); AMSGrad framing is discussion |
| Case C (IMM): sub-scope $\alpha_2$ between-transition + $\beta$ across-transition via dwell-time | Posterior re-concentration + impulsive-disturbance absorption | Sketch |
| Case D (MAML): inner-loop $\alpha_1$ + outer-loop $\beta$ | Fallah et al. 2020 meta-loss non-convexity | Classification (not derivation) |
| Mehra non-identifiability as meta-gain #disc-identifiability-floor instance | Rank-deficient transform matrix blocks (MG-2) derivation | Discussion (candidate floor instance) |

## Epistemic Status

*Conditional.* Max attainable: *derived* for the composed persistence result under (MG-1)–(MG-4); *exact* for Case A (adaptive Kalman) under Mehra identifiability; *conditional* for Case B (RMSProp) under design conditions; *sketch / classification* for Cases C (IMM) and D (MAML).

The core claim — that (MG-1)–(MG-4) together give an augmented-state sector-persistence result via standard Khalil Thm 4.18 — is a clean application of two-timescale Lyapunov analysis to the gain-as-state formulation. The mathematical core is textbook (vector Lyapunov, augmented-state dissipation, completing-the-square on cross terms). The contribution is the AAD-framing: (i) naming the four conditions that make adaptive gain composable with sector-persistence, (ii) identifying which adaptive-gain schemes satisfy all four from update-rule structure (Cases A, B-design) and which require assumption (Cases C-transition, D-outer, rule-based), and (iii) refining the A2' sub-scope partition into $\alpha_1$/$\alpha_2$/$\beta$ as a principled extension rather than overhaul.

**Imported machinery, acknowledged.** The underlying techniques — two-timescale stochastic approximation (Borkar 1997, 2008), adaptive filtering (Mehra 1970–72; Mohamed-Schwarz 1999; Dunik et al. 2021), MRAC stability theory (Narendra-Annaswamy 1989; Ioannou-Sun 1996), non-convex meta-learning convergence (Fallah et al. 2020; Ji-Yang-Liang 2022) — are standard in control theory and ML. AAD's value-add here is the integration: connecting these techniques to #result-sector-persistence-template via the augmented-state Lyapunov composition, and producing a sub-scope partition that matches AAD's scope-honesty architecture rather than importing the techniques' native terminology. The existing sub-scope $\alpha$ / $\beta$ partition from #deriv-sector-condition becomes $\alpha_1$ / $\alpha_2$ / $\beta$, with $\alpha_2$ labeling the newly-derivable adaptive-gain region.

**What this does not establish:**

- Convergence rates beyond ultimate-boundedness (the bound gives stability, not speed).
- Behavior under (MG-3) violation — fast-adapting gain on a slow primary state — which is structurally different (the composite system becomes singular-perturbation pathological, not sector-persistent).
- Rigorous fixed-point closure for the Case-B $\delta$-coupled case; the qualitative argument is clear but quantitative bounds on when the closure exists are per-problem.
- Composition at the multi-agent level — the augmented-state Lyapunov is for a single adaptive agent; team adaptive-gain (simultaneous meta-learning across agents) is beyond scope.

## Discussion

**Resolving Epistemic Opacity.** In `#def-observation-function`, the agent is structurally forbidden from knowing the true noise distribution $\varepsilon_t$. Yet the optimal gain `#emp-update-gain` requires knowing $U_o$. The adaptive Kalman filter with an innovation-based estimator (e.g., Mehra 1970) resolves this. The agent computes the autocorrelation of its observable mismatch sequence (innovations): $\iota_t = o_t - \hat{o}_t$. Because the innovation statistics are observable, the agent can estimate $U_o$ (and $U_M$) purely from its own history $\mathcal{C}_t$, satisfying both the opacity axiom and the optimality requirement. The error in this estimation ($\tilde K$) is exactly what the meta-gain sector condition (MG-2) bounds.

**Why this is not a singular-perturbation reduction.** Singular perturbation theory (Tikhonov 1952; Khalil 2002 Ch. 11) replaces fast dynamics with their quasi-steady-state manifold — the fast variable is *eliminated* in the slow reduction. The augmented-state analysis here does something different: it *keeps both states* and bounds their joint persistence via a weighted Lyapunov. Tikhonov gives "the fast variable tracks its slow manifold up to $O(\epsilon)$"; template-composition gives "each level's state is ultimately bounded with coupling-amplified disturbance" — the persistence-flavored statement aligned with AAD's other persistence results. They answer different questions; both are useful; neither replaces the other. #sketch-multi-timescale-stability's current sketch leans toward the Tikhonov framing; this segment adds the template-composition framing as an alternative.

**Three timescale patterns in AAD.** #sketch-multi-timescale-stability distinguishes model-class (slow) and parametric (fast) timescales. This segment introduces a *third* pattern: gain-parameter timescale, sitting between parametric-correction (fastest) and model-class (slowest). Adaptive gain is a different two-timescale pattern from structural adaptation — the gain is a parameter of the update rule, not of the model class. The convergence constraint $\nu_{n+1} \ll \nu_n$ from #der-temporal-nesting translates in this segment to $\alpha_K \ll \underline\alpha$ on Lyapunov decay rates, which is the (MG-3) condition.

**Meta-gain scope-honesty failure modes.**
- *Identifiability failures* on the meta-gain channel (Mehra non-identifiability) are instances of the #disc-identifiability-floor pattern: a structural no-go (non-identifiability) on the meta-gain channel blocks the sub-scope $\alpha_2$ derivation. AMSGrad as a meta-gain repair is the constructive complement — an added structural condition (monotonicity on $v_t$) that restores (MG-1) and keeps the adaptive scheme in $\alpha_2$.
- *Non-convex meta-losses* (MAML outer loop) put the outer loop in sub-scope $\beta$: A2' must be assumed within a basin, not derived from the meta-loss's global structure. This is the honest scope-narrowing posture — different from saying "it works" or "it doesn't" without qualification.
- *Regime transitions* (IMM across switches) violate (MG-1) uniformly in time during posterior re-concentration windows. Repair via dwell-time is clean but significant scope narrowing.

**Connection to #schema-strategy-persistence's $\alpha_\Sigma = 1/(n+1)$.** The strategy-edge persistence condition has $\alpha_\Sigma$ decaying with experience — this is adaptive gain of a specific form, where the gain (effective update rate per edge) is a function of accumulated pseudo-count. Without forgetting, $\alpha_\Sigma \to 0$ and (MG-1) fails asymptotically. #schema-strategy-persistence's forgetting prerequisite $(1-\lambda) \gt \rho_\Sigma/R_\Sigma$ is precisely the condition that keeps strategy-edge adaptation in sub-scope $\alpha_2$ rather than letting it fall to $\beta$ as $n$ grows.

**Relation to catastrophic forgetting via EWC.** Elastic Weight Consolidation (Kirkpatrick et al. 2017) introduces a per-parameter stability-weighted update: gain is scaled by inverse Fisher information of prior tasks. In AAD vocabulary, EWC is a tensor-valued adaptive gain with stability weighting, distinct from the scalar adaptive-gain case treated here but fitting the same augmented-state framework with (MG-1)–(MG-4) reinterpreted per-parameter. Adapting the present derivation to EWC would tensorize the Lyapunov argument — a natural but not-yet-executed extension.

## Working Notes

- **Identifiability as meta-gain obstruction.** Mehra non-identifiability for certain system structures (Dunik et al. 2021) is an instance of #disc-identifiability-floor on the meta-gain channel — a structural no-go blocking (MG-2) derivation. Candidate for explicit cross-reference in #disc-identifiability-floor's §"Adjacent Floors" as a fourth derived instance (after F1 CHT no-go, F13 Cramér-Rao mixture-identifiability, and Regime II-b misspecification-cost from #der-interaction-channel-classification).
- **Rate-specific results.** The composed persistence result is a bound, not a rate. Can the $1/\sqrt N$ rate of Mehra-adaptive-Kalman be derived rigorously from the augmented-state Lyapunov? Classical Mehra asymptotics give it directly; deriving it from (MG-1)–(MG-4) would confirm the framework's completeness.
- **Adversarial adaptive-gain.** If the environment adversarially varies $K^\ast$ (hostile regime-switching cadence), dwell-time repair of Case C fails. Adversarial-tempo-advantage analog at the meta-gain level: faster meta-gain tracking beats faster environmental regime switching iff $\alpha_K T_{\text{dwell}}$ exceeds the transition rate. Not derived here; adjacent spike.
- **Discrete-time form.** Everything above is continuous-time. Discrete-time version involves the Lipschitz bound of #deriv-discrete-sector-condition on both $F$ and $\Phi$. Extension is mechanical but deferred.
- **Relationship to #schema-strategy-persistence time-varying $\alpha$.** #schema-strategy-persistence's $\alpha_\Sigma = 1/(n+1)$ decay is a concrete instance of adaptive-gain dynamics where (MG-1) fails asymptotically without forgetting. Worth re-reading that segment through the $\alpha_2$ lens; the forgetting prerequisite is the specific move that keeps strategic adaptation in $\alpha_2$ as $n$ grows.
- **Template-composition as general technique.** The augmented-state weighted-Lyapunov argument is a general two-timescale composition technique for #result-sector-persistence-template. It composes two template instances with a cross-coupling bound. A generalization to three or more timescales (inner loop + outer loop + meta-meta-loop, or fast + gain + slow + structural) would give a chain-composition form; not derived here but structurally available.
- **AMSGrad as $\alpha_2$-preserving meta-gain repair.** Characterizing AMSGrad as "enforce (MG-1) by construction" is a clean AAD-framing of a pragmatically-motivated algorithm. Worth noting as an example of adaptive-gain schemes being AAD-classifiable by which of (MG-1)–(MG-4) they structurally ensure vs leave to luck.
