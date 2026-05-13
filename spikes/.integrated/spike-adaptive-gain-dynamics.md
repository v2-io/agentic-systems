# Spike: Adaptive-Gain Dynamics — A2' Under a Learning Gain

**Date:** 2026-04-22
**Trigger:** Research question on whether adapting the update gain $K$ (adaptive Kalman, MRAC, RMSProp/Adam, IMM, MAML) extends or breaks the sector-condition machinery — and where, inside the A2' sub-scope $\alpha$ / $\beta$ partition, the adaptive-gain setting sits.
**Posture:** Real derivation. Strengthen-first, then soften honestly on obstruction.
**Status:** Draft. Three structured cases derived to completion or to a named obstruction; meta-gain scope condition identified in a derivable form for the well-behaved cases; naming recommendation below.

## 1. Problem statement

Stated inside AAD's current machinery, the adaptive-gain question is:

> Let the mismatch dynamics be $\dot\delta = -F(\mathcal T_t, \delta; K_t) + w(t)$, where $F$ is the correction function, $K_t \in \mathcal K$ is a *gain state* that the agent itself adapts based on past observations, and $\mathcal T_t$ encodes the instantaneous adaptive tempo. $K_t$ has its own update law $\dot K_t = \Phi(K_t, \delta, w, \ldots)$ — it is not an exogenous parameter but an endogenously-learned quantity.
>
> Under what conditions does the sector condition (A2') $\delta^T F(\mathcal T_t, \delta; K_t) \geq \alpha \lVert\delta\rVert^2$ continue to hold *with a time-uniform lower bound* $\alpha$, and the persistence conclusion of Prop A.1 / A.1S still follow?

Three sub-questions sharpen this.

**Q1 (scope).** When is adapting $K$ still inside sub-scope $\alpha$ (A2' derived from the update rule's structure via #der-gain-sector-bridge Prop B.3)? When does it push into sub-scope $\beta$ (A2' posited per-agent)?

**Q2 (meta-gain).** Is there a *meta-gain sector condition* — a sector-like condition on the $K$-dynamics themselves — that composes with the primary sector condition on $\delta$ to preserve Prop A.1 / A.1S?

**Q3 (timescale separation).** When does adaptive gain introduce a genuinely two-timescale problem, and when is it absorbable as a single-timescale nonlinearity on $F$? Is this a singular-perturbation problem (#sketch-multi-timescale-stability), or does it reduce to constant-$\alpha$ analysis in a larger state space?

The answer, derived below, is: (i) **sub-scope $\alpha$ is preserved whenever the gain-update map is sector-bounded around its optimal gain and the timescales separate cleanly**; (ii) **a meta-gain sector condition does exist for a characterized sub-class (adaptive Kalman with Mehra-type innovation-based estimator; strongly-convex-loss step-size adaptation around a basin); otherwise the adaptive-gain regime is sub-scope $\beta$ with A2' as an assumed effective-$\alpha$ bound**; (iii) **the two-timescale view is productive — not as a singular-perturbation reduction, but as the natural setting for composing two instances of `#result-sector-persistence-template`**.

## 2. Structural setup — the gain becomes state

The cleanest formalization treats $K_t$ as an additional state variable coupled to $\delta$. Define the augmented state $z_t = (\delta_t, \tilde K_t)$, where $\tilde K_t = K_t - K^\ast$ is the gain-estimation error relative to some target optimal gain $K^\ast$ (specified below for each case — Riccati-steady-state for Kalman, Nesterov-optimal for strongly-convex gradient, etc.). The dynamics become:

$$\dot\delta = -F(\delta; K^\ast + \tilde K) + w(t), \qquad \dot{\tilde K} = -\Phi(\tilde K, \delta, w) + v(t)$$

where $\Phi$ is the gain-update contraction (the gain estimator's correction toward $K^\ast$) and $v(t)$ is the effective disturbance entering the gain channel (estimator noise, innovation noise, etc.).

This decomposition is what makes the problem tractable: **adaptive gain is a coupled two-level persistence problem** with $\delta$ as the fast state (primary sector condition) and $\tilde K$ as the slow state (meta-gain sector condition). The coupling is through the argument $K^\ast + \tilde K$ in $F$.

Three things can go wrong:

- **(W1) Sector degradation.** $F(\delta; K^\ast + \tilde K)$ may fail the sector condition uniformly in $\tilde K$: for large $\lVert\tilde K\rVert$, the correction can point the wrong way or vanish.
- **(W2) Coupling amplification.** The $\tilde K$-dynamics may have $\delta$-dependent disturbance — $v(t)$ can grow with $\lVert\delta\rVert$ — so $\tilde K$ does not converge unless $\delta$ is already bounded.
- **(W3) Timescale inversion.** If $\tilde K$ adapts faster than $\delta$, the system is a fast-tracking-a-slow-moving-target problem where the gain chases per-step innovations, destabilizing $\delta$ (Adam without momentum, noisy-gradient regime; aggressive Mehra with small window).

The derivation below enumerates these obstructions case by case.

## 3. Case A — Adaptive Kalman filter with Mehra-type innovation-based Q/R estimator

### 3.1 Setup

Take the scalar linear-Gaussian setting of #deriv-gain-sector Prop B.1 with unknown $Q$ (process noise variance) and $R$ (observation noise variance). Let $K^\ast$ be the steady-state Kalman gain for the true $(Q^\ast, R^\ast)$. The innovation-based estimator (Mehra 1970, 1972; Mohamed & Schwarz 1999; treated as a rank-deficient-identifiability problem in Dunik et al. 2021 per the Zagrobelny PMC reference) produces $\hat Q_t, \hat R_t$ from a sliding-window autocorrelation of the innovation sequence, then feeds $K_t = K(\hat Q_t, \hat R_t)$ back into the Kalman update.

The innovation at time $t$ is $\iota_t = o_t - H \hat x_{t\mid t-1} = H e_{t\mid t-1} + \varepsilon_t$ where $e$ is the state-estimation error and $\varepsilon$ is the observation noise. In the scalar case, the primary sector condition is (Prop B.1):

$$e \cdot F(e; K) = K \cdot e^2, \quad \text{so} \quad \alpha(K) = K$$

in Euclidean form. The gain state is scalar: $\tilde K = K - K^\ast$.

### 3.2 Primary sector condition as a function of $\tilde K$

Scalar case, $K \in (0, 1)$: the sector bound is $\alpha(K) = K = K^\ast + \tilde K$. For the sector bound to be *uniform in time with a positive floor*, we need $K_t \geq \underline K > 0$ throughout. The innovation-based estimator yields $\hat Q_t, \hat R_t > 0$ (by construction — these are sample variances, projected if necessary), so $K_t \in (0, 1)$ is preserved. We can write

$$\alpha_{\text{eff}} = K^\ast - |\tilde K|_{\text{max}} \quad \text{(primary sector floor, Case A)}$$

provided $|\tilde K|_{\text{max}} < K^\ast$. This is the first meta-condition: **the gain estimator must not undershoot more than a bounded fraction of the optimal gain**.

### 3.3 Meta-gain dynamics — innovation-based estimator

Mehra's estimator uses $C_k = \mathbb E[\iota_t \iota_{t-k}^T]$ autocorrelations at lags $k = 0, 1, \ldots$, computed from a sliding window of length $N$. For a stable (not necessarily optimal) filter, these correlations are affine functions of $Q, R$ with a known transform matrix $\mathcal M(A, H, K)$ (Mehra 1970 eq. 8-10). Inverting this yields $\hat Q, \hat R$.

In expectation, the estimator is unbiased: $\mathbb E[\hat Q_t] \to Q^\ast$, $\mathbb E[\hat R_t] \to R^\ast$ as $N \to \infty$. Per-sample fluctuations scale as $O(1/\sqrt{N})$. The gain-update map, to first order in $\tilde K$:

$$\tilde K_{t+1} = (1 - \lambda_N) \tilde K_t + \lambda_N \eta_t^{\text{inn}}$$

where $\lambda_N$ is a contraction rate set by the window length ($\lambda_N \asymp 1/N$ for the raw estimator; modified via forgetting-factor variants) and $\eta_t^{\text{inn}}$ is zero-mean innovation noise with variance scaling as $O(1/N)$.

**This is a scalar Ornstein-Uhlenbeck process on $\tilde K$.** It is itself an instance of `#result-sector-persistence-template` with state $\xi = \tilde K$, correction $F_K(\tilde K) = \lambda_N \tilde K$, disturbance $v_t = \lambda_N \eta_t^{\text{inn}}$:

- **(T1)** $F_K(0) = 0$: when the gain is at optimal, the innovation-statistics estimate returns the optimal, in expectation.
- **(T2-meta)** $\tilde K \cdot F_K(\tilde K) = \lambda_N \tilde K^2$: **meta-gain sector bound $\alpha_K = \lambda_N$**.
- **(T3-S)** $\mathbb E[v_t^2] = \sigma_K^2 \asymp \lambda_N^2 / N$: bounded stochastic disturbance on the gain channel.

Prop A.1S gives steady-state gain-error RMS:

$$R^\ast_{S, K} = \sigma_K \sqrt{\frac{1}{2\alpha_K}} \asymp \sqrt{\frac{\lambda_N / N}{2}} \asymp \frac{1}{\sqrt{N}}$$

which matches the classical $O(1/\sqrt{N})$ rate of the Mehra estimator. The meta-gain sector condition is **derived**, not assumed, and quantitatively matches the known asymptotics.

### 3.4 Composed persistence — two-timescale version

With $\alpha_{\text{eff}} = K^\ast - |\tilde K|_{\text{max}}$ and mean-square $|\tilde K|_{\text{max}} \asymp R^\ast_{S,K}$, we can plug into Prop A.1S for the primary dynamics:

$$\mathbb E[e_t^2]_{ss} \leq \frac{\sigma_w^2}{2(K^\ast - R^\ast_{S,K})}$$

which reduces to the classical Prop A.1S result as $N \to \infty$ and the gain estimator becomes exact. The **degradation due to adaptive gain** is a shift in the effective $\alpha$ from $K^\ast$ to $K^\ast - R^\ast_{S,K}$, with the shift vanishing as $1/\sqrt{N}$.

**Timescale separation requirement.** The composed argument requires $\tilde K$ to be approximately stationary on the timescale of $e$'s transient — i.e., $\lambda_N \ll $ Kalman-filter contraction rate. For the raw Mehra estimator this holds automatically ($\lambda_N \asymp 1/N$ small by choice of $N$). For forgetting-factor variants with aggressive $\lambda$ (tracking regime-switching noise), timescale separation fails and the composed argument does not apply — the correct treatment is then (W3) below or Case C (IMM).

### 3.5 Verdict — Case A is sub-scope $\alpha$

Adaptive Kalman with innovation-based Q/R estimation under timescale separation ($\lambda_N \ll $ primary-contraction rate) is **inside sub-scope $\alpha$**: both the primary sector condition (Prop B.1) and the meta-gain sector condition (above) are derived from the update structure, not assumed. The composed persistence result is a clean application of `#result-sector-persistence-template` twice in sequence.

**What's derived:**
- Primary A2' with $\alpha_{\text{eff}} = K^\ast - |\tilde K|_{\text{max}}$ (from Prop B.1 + triangle).
- Meta-gain A2' with $\alpha_K = \lambda_N$ (from Mehra asymptotics + OU-form of estimator error).
- Composed persistence with $O(1/\sqrt{N})$ degradation (from two applications of Prop A.1S).

**What's assumed:**
- Timescale separation $\lambda_N \ll K^\ast$ (design condition on the estimator window).
- Identifiability of $(Q, R)$ from innovations — requires rank condition on Mehra's transform matrix $\mathcal M$ (see Zagrobelny & Rawlings 2015; Dunik et al. 2021 — the identifiability question is *not* trivial and is a subject of active research).

## 4. Case B — Adaptive step-size gradient descent (AdaGrad / RMSProp / Adam) on strongly convex loss

### 4.1 Setup

Agent updates via $M_{t+1} = M_t - \eta_t \cdot \hat g_t / (\sqrt{v_t} + \varepsilon)$ where $\hat g_t$ is the per-step stochastic gradient and $v_t$ is a running second-moment estimate (RMSProp: exponential moving average $v_t = \beta v_{t-1} + (1-\beta)\hat g_t^2$; AdaGrad: cumulative $v_t = \sum_{s \leq t} \hat g_s^2$).

In the #emp-update-gain representation, this is $\eta_t^{\text{eff}} = \eta_t / (\sqrt{v_t} + \varepsilon)$. The gain adapts per-coordinate; here we treat the scalar case. The target $K^\ast$ is the fixed step size that minimizes the asymptotic variance of the iterate in the limit of perfect second-moment knowledge, i.e., $\eta^\ast = \eta / \sqrt{\mathbb E[g^2]}$.

The loss $L$ is $\mu$-strongly convex with $L$-Lipschitz gradient. The primary correction function is $F(\delta; K) = K \nabla L(M^\ast + \delta)$, with $K$ the effective learning rate. Prop B.4 gives the primary sector condition: $\alpha(K) = K \mu$ for $\delta$ in the basin.

### 4.2 Primary sector condition under adaptive $K$

The per-step effective step is $\eta_t^{\text{eff}} = \eta_t / (\sqrt{v_t} + \varepsilon)$. In steady state around the minimizer, $v_t \to \mathbb E[\hat g_t^2] = \lVert\nabla L\rVert^2 + \sigma_g^2$, where $\sigma_g^2$ is the stochastic-gradient variance. Near the minimizer ($\nabla L \to 0$), $v_t \to \sigma_g^2$ — the step size approaches $\eta / \sigma_g$.

For the sector bound to hold uniformly, $K_t \geq \underline K > 0$; this is ensured by the $\varepsilon$ regularizer in the denominator. The floor is $\underline K = \eta / (\sqrt{v_{\max}} + \varepsilon)$ for any upper bound $v_{\max}$ on the second-moment estimate.

**Primary A2' holds uniformly** with $\alpha_{\text{eff}} = \underline K \mu$ (worst-case adaptive step size times strong-convexity modulus). This is weaker than the optimal-step-size bound $\alpha^\ast = \eta^\ast \mu$, and the gap is determined by the range of $v_t$ fluctuations.

### 4.3 Meta-gain dynamics — running second-moment estimator

RMSProp's $v$-update is a scalar first-order linear filter:

$$v_{t+1} = \beta v_t + (1-\beta) \hat g_t^2$$

Writing $\tilde v_t = v_t - \mathbb E[\hat g_t^2]$ (the deviation of the second-moment estimate from its expectation — which itself depends on $\delta$ near the minimizer!), the dynamics decompose:

$$\tilde v_{t+1} = \beta \tilde v_t + (1-\beta)(\hat g_t^2 - \mathbb E[\hat g_t^2]) + \beta(\mathbb E[\hat g_{t-1}^2] - \mathbb E[\hat g_t^2])$$

The first two terms form the familiar OU-type contraction on $\tilde v$: meta-gain sector bound $\alpha_v = 1 - \beta$ with stochastic disturbance variance $\sigma_v^2 \asymp (1-\beta)^2 \cdot \text{Var}(\hat g_t^2)$.

The **third term** is the critical obstruction: it reflects the fact that $\mathbb E[\hat g_t^2]$ is $\delta$-dependent. Near the minimizer, $\mathbb E[\hat g_t^2] \approx \sigma_g^2 + \lambda_{\max}(H)^2 \lVert\delta\rVert^2$. So the effective meta-gain disturbance picks up a $\delta$-coupled term:

$$v_{\text{meta-dist}}(t) \asymp (1-\beta)\sigma_v + \beta \cdot \lambda_{\max}(H)^2 \cdot \frac{d}{dt}\lVert\delta\rVert^2$$

This is **(W2) coupling amplification**: the gain-dynamics disturbance depends on the primary state.

### 4.4 Composed persistence — conditions for A2' preservation

Prop A.1S applied to the meta-gain equation with the $\delta$-coupled disturbance requires treating $\mathbb E[\lVert\delta\rVert^2]$ as a state-dependent disturbance intensity, which breaks the strict template. But a one-shot decoupling argument works:

**Step 1 (primary persistence, conditional on meta-gain bound).** Assume for now $\tilde v_t$ is ultimately bounded by some $R_v$. Then $\alpha_{\text{eff}} \geq \underline K \mu = (\eta / \sqrt{\mathbb E[\hat g^2] + R_v}) \cdot \mu$. Prop A.1S gives $R^\ast_S = \sigma_w\sqrt{n / (2\alpha_{\text{eff}})}$.

**Step 2 (meta-gain persistence, given primary bound).** With $\delta$ ultimately bounded by $R^\ast_S$, the $\delta$-dependent meta-disturbance is bounded: $\sigma_{v, \text{eff}}^2 \leq (1-\beta)^2 \text{Var}(\hat g^2) + \beta^2 \lambda_{\max}(H)^4 (R^\ast_S)^4$. Apply Prop A.1S to the meta-gain channel: $R_v \leq \sigma_{v, \text{eff}} / \sqrt{2(1-\beta)}$.

**Step 3 (closure condition).** The two inequalities couple: $R^\ast_S$ depends on $R_v$ (through $\alpha_{\text{eff}}$) and $R_v$ depends on $R^\ast_S$ (through the coupling term). Closure requires the composed fixed-point $(R^\ast_S, R_v)$ to exist and be small enough to fit inside both valid regions.

Under the design condition $\beta$ close to 1 (slow meta-gain — the EMA has long memory) and $\lambda_{\max}(H) \cdot R^\ast_S \ll \sqrt{\sigma_g^2}$ (the coupling term is small compared to the irreducible gradient-variance floor), the fixed point exists and is stable, and one can derive a composed persistence result. Under the opposite regime (aggressive $\beta$, small gradient noise, large $\lambda_{\max}$), the fixed-point iteration can diverge — which is the failure mode observed empirically in RMSProp/Adam on ill-conditioned problems (Reddi et al. 2018's counterexample is structurally this).

### 4.5 Verdict — Case B is sub-scope $\alpha$ *with scope-narrowing conditions*, sub-scope $\beta$ otherwise

Under the design conditions named in §4.4, adaptive step-size gradient descent on strongly-convex losses is sub-scope $\alpha$: the primary A2' is derived from Prop B.4 with $\alpha_{\text{eff}} = \underline K \mu$; the meta-gain A2' is derived from the EMA contraction with $\alpha_v = 1 - \beta$; the composed persistence follows from two applications of Prop A.1S plus a fixed-point closure condition.

Outside those conditions (aggressive $\beta$, ill-conditioning, small gradient noise), the $\delta$-coupled meta-gain disturbance can drive $\tilde v$ to a regime where the primary sector floor $\underline K$ degrades faster than the primary sector gives back, and A2' fails to hold uniformly — sub-scope $\beta$. Adam's AMSGrad fix (Reddi et al. 2018) is exactly a meta-gain repair: it enforces monotonicity on $v_t$ to preserve $\underline K$, restoring sub-scope $\alpha$ by construction.

**A sharper A2' sub-scope partition emerges:**

- **Sub-scope $\alpha_1$ (derived under fixed gain):** Prop B.4's original result.
- **Sub-scope $\alpha_2$ (derived under adaptive gain + timescale separation + coupling smallness):** Case A (adaptive Kalman) and Case B under design conditions. *A2' is still derived, but through a composed two-template argument.*
- **Sub-scope $\beta$ (A2' assumed):** Adaptive gain without timescale separation; adaptive gain with strong $\delta$-to-gain coupling; IMM in transient (see Case C); MAML in inner-outer regime without convexity (see Case D).

## 5. Case C — Interacting Multiple Models / regime-switching Kalman

### 5.1 Setup

Agent maintains $M$ models, each a Kalman filter with different $(Q^{(m)}, R^{(m)})$. At each step, a Bayesian mixing step reweights models by their innovation likelihood, then a switching update applies a Markov transition matrix on model probabilities. The effective gain is a probability-weighted mixture: $K_t = \sum_m \pi_t^{(m)} K^{(m)}$ where $\pi_t$ is the posterior-over-models.

The gain state is now $\tilde K_t = K_t - K^\ast(\text{regime}_t)$ — error relative to the *regime-conditional* optimal gain. Since regime itself changes, $K^\ast$ is piecewise-constant with jumps.

### 5.2 Structural obstruction — A2' uniform-in-time fails at regime transitions

The difficulty: at a regime-switch instant, $K^\ast$ jumps from $K^\ast_1$ to $K^\ast_2$. The IMM posterior $\pi_t$ has its own transient — it takes several observations to reconcentrate on the new true regime. During this transient, $K_t = \sum_m \pi_t^{(m)} K^{(m)}$ can sit near $K^\ast_1$ even though the true regime is 2. The primary sector product $\delta^T F$ is therefore computed with a *wrong* $K$, and the effective sector floor $\alpha$ can collapse toward zero (or go negative if $K^{(2)} \ll K^{(1)}$ — chasing a noisy regime in the wrong direction).

**This is genuinely a fail-mode for derived A2'.** The analog of directional fidelity B1 does not hold uniformly in time across regime transitions, because the agent's gain can be aligned with the wrong regime for a multi-step window.

**Quantifying the transient.** For a Markov transition matrix with self-loop probability $p$ and cross probability $1-p$, the posterior-reconcentration time is $\tau_{\text{IMM}} \asymp 1/(1-p)$ observations — the geometric mean dwell time. During this transient, $\alpha_t$ can be arbitrarily small; Prop A.1 does not apply.

### 5.3 Scope-narrowing repair — step-function disturbance + dwell-time condition

One way to recover a persistence result is to treat regime transitions as **impulsive disturbances** rather than gain failures. Fix a regime for a long interval $T_{\text{dwell}} \gg \tau_{\text{IMM}}$. During the steady portion (post-reconcentration), A2' holds with $\alpha \asymp K^\ast(\text{regime})$ and Prop A.1S gives persistence. The transient contributes an $O(\tau_{\text{IMM}})$ mismatch spike per transition, which can be absorbed into the effective $\rho$ (Model D) or $\sigma_w^2$ (Model S) by a counting argument.

**This is a clean result but a significant scope narrowing:** it requires a dwell-time condition on the regime process (each regime persists for $\gg \tau_{\text{IMM}}$) and treats regime switches as a disturbance model, not a gain model. Under this framing, IMM is sub-scope $\alpha$ in the *between-transition regime* and sub-scope $\beta$ (with explicit impulsive-disturbance bookkeeping) across transitions.

### 5.4 Verdict — Case C splits by regime

IMM is **not uniformly sub-scope $\alpha$**. It fractures:

- **Between-transition regime:** sub-scope $\alpha$ by reduction to fixed-gain Kalman for the dominant-mode $K^\ast$.
- **Across regime transitions:** sub-scope $\beta$, with A2' failing during the reconcentration window. The correct treatment is either (a) dwell-time + disturbance absorption (works if regime process is slow enough), or (b) honest posit that A2' does not hold on the $\tau_{\text{IMM}}$ transient and mismatch persistence is measured after transients decay.

This is the adaptive-gain analog of `#result-structural-adaptation-necessity`'s trigger: regime-transitions are structural events that temporarily exceed the sector-condition machinery.

## 6. Case D — MAML-style meta-learning (inner loop + outer loop)

### 6.1 Setup

MAML structures learning as nested: the inner loop adapts model parameters $\theta$ to task $\mathcal T_i$ via $k$ gradient steps with step size $\alpha$ (inner learning rate), yielding $\theta_i'$; the outer loop updates the initialization $\theta$ via gradient descent on the meta-loss $\sum_i L_i(\theta_i'(\theta))$ with step size $\beta$ (outer learning rate).

In the AAD correspondence: the inner loop is the primary adaptive process with update gain $\alpha$; the outer loop is a meta-gain update that modifies the *initialization* (effectively, the prior over model space), not the gain itself. This is a different structural shape from Cases A–C: the meta-learner's action is on the *starting point* for subsequent adaptation, not on the step-size of the current adaptation.

### 6.2 Two-timescale reading — the outer loop as $M_t$ re-specification

MAML is most naturally read in AAD as a meta-adaptation that adjusts the *model class specification* over tasks — very close to what `#result-structural-adaptation-necessity` contemplates, but continuous and differentiable rather than discrete class-switching. The inner loop is `#emp-update-gain` within a fixed model class; the outer loop moves the model class itself via gradient on meta-loss.

The primary sector condition (inner loop) holds for each task under the convex-loss assumption, exactly via Prop B.4: $\alpha = \alpha_{\text{inner}} \cdot \mu$.

The outer loop operates on $\theta$ via the meta-gradient $\nabla_\theta L_i(\theta_i'(\theta))$, which involves second-order terms through $\theta_i'$'s dependence on $\theta$. Strong convexity of the meta-loss in $\theta$ is not inherited from per-task convexity (Fallah et al. 2020's convergence results rely on weaker smoothness + stochastic-gradient conditions, not strong convexity).

### 6.3 Obstruction — meta-loss is generally non-convex

Per Fallah et al. 2020 ("On the convergence theory of gradient-based MAML"), the meta-loss is non-convex even when per-task losses are convex, because the inner-loop update is a non-linear function of $\theta$. Convergence is guaranteed only to a first-order stationary point; multi-step MAML has convergence *slower* for non-convex inner loops and faster for strongly-convex inner loops (Ji et al., *J. Mach. Learn. Res.*).

In AAD language: the **outer loop's primary sector condition fails globally**. It holds only within a basin of attraction — and the basin is typically smaller than the meta-loss landscape's rich structure. This places MAML's outer loop squarely in sub-scope $\beta$: A2' must be assumed locally, not derived from the meta-loss structure.

The inner loop (fixed-$\alpha$ inside the basin) is sub-scope $\alpha$. The composed system is sub-scope $\alpha \times \beta$: inner-loop sector condition is derived, outer-loop sector condition is assumed (or equivalently, A2' holds in a basin of the meta-loss landscape, with basin boundary being the structural-adaptation trigger for the meta-learner).

### 6.4 Verdict — Case D is sub-scope $\beta$ at the meta-level, sub-scope $\alpha$ at the task-level

MAML's formal status in AAD is that **its inner-outer structure matches `#sketch-multi-timescale-stability`'s two-timescale framework** with the *slow* state being $\theta$ (initialization / model class) and the *fast* state being per-task adaptation. Inner-loop A2' is derived (sub-scope $\alpha$) from Prop B.4. Outer-loop A2' must be assumed per basin, not derived (sub-scope $\beta$), because the meta-loss is non-convex even under per-task convexity.

## 7. The meta-gain sector condition — consolidated form

Across Cases A, B, and the clean part of C, a pattern emerges. Let the adaptive-gain setup be $\dot\delta = -F(\delta; K^\ast + \tilde K) + w(t)$, $\dot{\tilde K} = -\Phi(\tilde K, \delta) + v(t)$. The composed persistence result holds when:

**(MG-1) Primary sector floor under bounded gain error.** There exist $\underline\alpha > 0$ and $r_K > 0$ such that for all $\lVert\tilde K\rVert \leq r_K$ and $\lVert\delta\rVert \leq R$:

$$\delta^T F(\delta; K^\ast + \tilde K) \geq \underline\alpha \lVert\delta\rVert^2$$

This is A2' *uniform in the gain-error ball*. It is the honest statement of what adaptive gain requires: not that $\alpha$ is constant, but that the sector floor is preserved across the gain-state range the meta-learner visits.

**(MG-2) Meta-gain sector condition.** The gain-update map $\Phi$ satisfies $(T_1)$ (zero at $\tilde K = 0$) and a local sector condition in the gain state:

$$\tilde K^T \Phi(\tilde K, \delta) \geq \alpha_K \lVert\tilde K\rVert^2 \quad \text{for } \lVert\tilde K\rVert \leq r_K, \text{ uniformly in } \lVert\delta\rVert \leq R$$

with $\alpha_K > 0$. **This is the meta-gain scope condition** — the question asked in the spike brief.

**(MG-3) Timescale separation.** $\alpha_K \ll \underline\alpha$ (the gain adapts slower than the primary state contracts). This is the direct analog of `#der-temporal-nesting`'s $\nu_{n+1} \ll \nu_n$ convergence constraint, now stated on the Lyapunov decay rates rather than the event rates.

**(MG-4) Coupling boundedness.** The effective gain-channel disturbance $v(t)$ has bounded contribution from the primary state: $\mathbb E[\lVert v(t)\rVert^2 \mid \delta] \leq \sigma_{K,0}^2 + c_v \cdot \lVert\delta\rVert^2$ for some $c_v \geq 0$. (MG-4) with $c_v = 0$ is the clean two-timescale decoupling of Case A; $c_v > 0$ is Case B's RMSProp coupling, requiring the fixed-point closure of §4.4.

**Composed persistence result.** Under (MG-1)–(MG-4), the augmented-state persistence $\mathbb E[\lVert\delta\rVert^2 + c \lVert\tilde K\rVert^2]$ is ultimately bounded for an appropriate weight $c$, and the bounds degrade gracefully compared to the fixed-gain case. Where (MG-4) has $c_v = 0$, the degradation is a clean decomposition: primary + meta, each via `#result-sector-persistence-template`. Where $c_v > 0$, the degradation couples — solve by fixed-point as in §4.4.

**Proof sketch.** Define the Lyapunov candidate $V(z) = \tfrac12 \lVert\delta\rVert^2 + \tfrac{c}{2}\lVert\tilde K\rVert^2$ on the augmented state $z = (\delta, \tilde K)$. Compute $\dot V$ along trajectories:

$$\dot V = -\delta^T F(\delta; K^\ast + \tilde K) - c \tilde K^T \Phi(\tilde K, \delta) + \delta^T w + c \tilde K^T v$$

Apply (MG-1) to the first term, (MG-2) to the second, Cauchy-Schwarz and (MG-4) to the cross-disturbance terms:

$$\dot V \leq -\underline\alpha \lVert\delta\rVert^2 - c\alpha_K \lVert\tilde K\rVert^2 + \rho\lVert\delta\rVert + c(\sigma_{K,0} + \sqrt{c_v}\lVert\delta\rVert)\lVert\tilde K\rVert$$

Complete-the-square on the cross term (requires $c\sqrt{c_v}$ small compared to $\underline\alpha \cdot c\alpha_K$, which is (MG-3) timescale separation plus (MG-4) coupling smallness):

$$\dot V \leq -\tfrac{\underline\alpha}{2}\lVert\delta\rVert^2 - \tfrac{c\alpha_K}{2}\lVert\tilde K\rVert^2 + \rho^2/(2\underline\alpha) + c\sigma_{K,0}^2/(2\alpha_K)$$

Standard Lyapunov ultimate-boundedness (Khalil 2002 Thm 4.18). $\square$

**What this means for the A2' partition.** The augmented-state Lyapunov argument shows that (MG-1)–(MG-4) together give a sector-like condition on the augmented-state dynamics. Thus:

- If (MG-1), (MG-2), (MG-3), and (MG-4-decoupled or -bounded) all hold *structurally* from the update rule (as in Cases A and the design-condition regime of B), then adaptive-gain A2' is derived — sub-scope $\alpha_2$ (new label).
- If any of (MG-1)–(MG-4) must be assumed per-agent (as in the non-convex meta-loss of MAML, the regime-transitioning phase of IMM, or aggressive-$\beta$ RMSProp), the adaptive-gain system falls to sub-scope $\beta$ or a mixed $\alpha$/$\beta$ case as in MAML.

This is a constructive extension of the A2' sub-scope partition, not a replacement: sub-scope $\alpha_1$ (fixed-gain, per the current `#der-gain-sector-bridge` Prop B.3) continues to cover the well-studied cases; sub-scope $\alpha_2$ (adaptive-gain under MG-1–MG-4) names the adaptive setting where derivation still works; sub-scope $\beta$ catches the rest.

## 8. Relationship to `#sketch-multi-timescale-stability`

The adaptive-gain problem naturally sits inside `#sketch-multi-timescale-stability`'s two-timescale sketch, but with a sharpening. The existing segment treats the slow state as *model class* $\mathcal M$ (structural adaptation) and the fast state as *mismatch* $\delta$ (parametric adaptation). Adaptive gain is a *different* two-timescale pattern: the slow state is the *gain* (a parameter of the update rule, not of the model), and the fast state is the primary mismatch.

This suggests a refinement: `#sketch-multi-timescale-stability` should distinguish at least three timescale patterns:

1. **Model-class timescale** (slowest meaningful parametric timescale; structural-adaptation territory).
2. **Gain-parameter timescale** (the subject of this spike; between-events but slower than primary correction).
3. **Primary-correction timescale** (fastest; the canonical Prop A.1 setting).

The singular-perturbation framing in `#sketch-multi-timescale-stability` Eq. 1 becomes concrete: $\epsilon_k$ at each level is the contraction rate of the corresponding Lyapunov function, not a free parameter. The convergence constraint $\nu_{n+1} \ll \nu_n$ translates to $\alpha_{\text{slow}} \ll \alpha_{\text{fast}}$ on Lyapunov decay rates, matching the (MG-3) timescale-separation condition.

**However:** singular perturbation theory (Tikhonov 1952; Khalil 2002 ch. 11) is a *reduction* technique — it replaces the fast dynamics with their quasi-steady-state manifold. The spike's adaptive-gain analysis does not do this. Instead, it composes two `#result-sector-persistence-template` instances with an explicit cross-coupling bound. The two approaches are complementary: Tikhonov gives the "the fast state tracks its slow manifold up to $O(\epsilon)$" story; the template-composition gives the "each level's state is ultimately bounded with coupling-amplified disturbance" story, which is the persistence-flavored statement aligned with AAD's other persistence results.

**Recommendation:** `#sketch-multi-timescale-stability` gets an explicit note that AAD's preferred two-timescale composition is via `#result-sector-persistence-template` applied twice with an augmented-state Lyapunov function (§7 above), not via Tikhonov reduction. Singular perturbation is a reduction tool; template-composition is a persistence-bounding tool. They answer different questions.

## 9. What's derived vs what's assumed in this spike

| Claim | Source | Epistemic status |
|---|---|---|
| Adaptive-gain problem reformulates as augmented-state $z = (\delta, \tilde K)$ with coupled sector dynamics | §2 structural setup | Definitional reformulation |
| Meta-gain sector condition (MG-2) on $\Phi$ in the gain channel | §3.3 for Case A (innovation-based estimator); §4.3 for Case B (EMA second-moment estimator) | Derived from estimator structure in named cases |
| Primary-sector-floor-under-bounded-gain-error (MG-1) | §3.2 (scalar Kalman: $\alpha_{\text{eff}} = K^\ast - \lvert\tilde K\rvert$); §4.2 (strongly-convex gradient: $\alpha_{\text{eff}} \geq \underline K \mu$ via $\varepsilon$-floor) | Derived in Cases A and B under stated regularity |
| Composed-persistence augmented-state Lyapunov result under (MG-1)–(MG-4) | §7 proof sketch | Derived (conditional on MG-1 through MG-4) |
| (MG-3) timescale separation as AAD's $\nu_{n+1} \ll \nu_n$ analog on Lyapunov decay rates | §7 plus §8 discussion | Derived (via augmented-state Lyapunov cross-term closure) |
| Case-by-case classification of adaptive-Kalman, RMSProp, IMM, MAML in sub-scope $\alpha_1$ / $\alpha_2$ / $\beta$ | §§3–6 | Derived per case, conditional on named regularity |
| Refinement of A2' sub-scope partition: $\alpha_1$ (fixed-gain) / $\alpha_2$ (adaptive-gain under MG-1–MG-4) / $\beta$ (everything else) | §7 recommendation | Discussion-grade proposal for segment-level edit |
| `#sketch-multi-timescale-stability` should separate model-class / gain-parameter / primary-correction timescales | §8 | Discussion-grade proposal for segment-level edit |

### Epistemic honest obstructions identified

- **(Obstruction O1) Identifiability for Mehra's estimator.** The meta-gain dynamics in §3.3 assume the $(Q, R)$-from-innovations problem is identifiable. This is known to fail for certain system structures (Dunik et al. 2021). When identifiability fails, the meta-gain estimator does not contract to $\tilde K = 0$, and (MG-2) fails at its target — the adaptive-Kalman persistence result does not hold. This is an instance of the #disc-identifiability-floor pattern: a structural no-go (non-identifiability) on the meta-gain channel blocking adaptive sub-scope $\alpha$.
- **(Obstruction O2) Non-convex meta-loss (MAML).** The outer loop's A2' is assumed, not derived, because per-task convexity does not imply meta-loss convexity. Fallah et al. 2020's convergence analysis is in the stationary-point sense, not the sector-condition sense — and the two are structurally different. This is sub-scope $\beta$ status being honest, not a bug.
- **(Obstruction O3) $\delta$-to-gain coupling in RMSProp.** The $\delta$-dependent term in the effective gain-channel disturbance (§4.3's third term) breaks clean decoupling. The fixed-point closure works under smallness conditions but reduces to (MG-4) with $c_v > 0$ and requires separate verification per problem instance.
- **(Obstruction O4) IMM regime transitions.** A2' fails uniformly in time during IMM reconcentration windows; repair via dwell-time + impulsive-disturbance absorption is a significant scope narrowing. Sub-scope $\alpha$ between transitions; sub-scope $\beta$ across them.

None of the four obstructions is fatal to AAD — they are instances of the scope-honesty-as-architecture posture. Each says "here is where adaptive-gain derivation runs out of steam, and here is the narrower claim that remains."

## 10. Recommendations — where findings land

Three options, ranked:

### R1 (preferred) — New segment: `#deriv-adaptive-gain-dynamics` + minor edits to three existing segments

Create `01-aad-core/src/deriv-adaptive-gain-dynamics.md` as a derived/result segment stating:

1. The augmented-state setup (§2).
2. Conditions (MG-1)–(MG-4) as the sector-condition analog for adaptive gain.
3. The composed persistence result (§7) as a theorem, with a derivation table separating what's derived / assumed / chosen.
4. The four structured cases as worked instantiations (adaptive Kalman, RMSProp, IMM, MAML).
5. Sub-scope partition refinement: $\alpha_1$ / $\alpha_2$ / $\beta$.

Corresponding edits:

- **`#deriv-sector-condition`:** extend the sub-scope paragraph to mention $\alpha_2$ (adaptive-gain derivation) with pointer to the new segment; one-sentence note in the "What is derived vs. what is chosen" table.
- **`#der-gain-sector-bridge`:** one-paragraph Discussion note cross-referencing the adaptive-gain extension. No change to B1/B.3/B.4.
- **`#sketch-multi-timescale-stability`:** Working Notes entry naming the three timescale patterns (model-class / gain-parameter / primary-correction), with pointer to the new segment's §7–8.

This is the approach consistent with `feedback_math_lives_in_segments.md`: the math in this spike lands as a segment, not just as an appendix or working note.

### R2 — Appendix to `#der-gain-sector-bridge`

Fold §§2, 7 into a new "Adaptive-gain extension" §5 or §6 of `#der-gain-sector-bridge`, with Cases A-D as terse examples. No new segment file. Downside: bloats an already load-bearing segment with a separate pattern; the $\alpha_1$ / $\alpha_2$ distinction is harder to make visible when embedded.

### R3 — Sub-sub-scope of A2' in `#deriv-sector-condition`

Extend the existing A2' sub-scope partition to $\alpha_1$ / $\alpha_2$ / $\beta$ directly in the Assumptions section of `#deriv-sector-condition`, without a new segment. Downside: the augmented-state argument and the meta-gain conditions (MG-1)–(MG-4) are substantive new content that does not fit into a sub-scope-labeling paragraph.

**Recommendation: R1.** The adaptive-gain result is a proper extension of AAD's persistence machinery in the form of a new, composable theorem (§7). It deserves its own segment rather than a subordinate position inside an existing one. The segment's stage would be `draft` pending review; type `derived` (since (MG-1)–(MG-4) + Prop A.1 chains to a new result); status `conditional` (since the new sub-scope $\alpha_2$ is conditional on (MG-1)–(MG-4), each verifiable per case).

## 11. Answers to the spike's five research questions

1. **When does adapting $K$ remain inside sub-scope $\alpha$?** When (MG-1)–(MG-4) hold with all four conditions derivable from the update-rule structure (e.g., adaptive Kalman with Mehra estimator + identifiability + window long enough; RMSProp on strongly-convex loss with large-$\beta$ + coupling smallness + AMSGrad-style monotonicity repair). This is the newly-named **sub-scope $\alpha_2$**.

2. **When does it push into sub-scope $\beta$?** When any of (MG-1)–(MG-4) must be assumed per-agent. Concrete instances: non-convex meta-losses (MAML outer loop), regime-transition transients (IMM across switches), aggressive EMA without monotonicity repair (vanilla Adam on ill-conditioned problems), or violation of Mehra-style identifiability conditions.

3. **Is there a meta-gain sector condition?** Yes — (MG-2) in §7. It is a local sector condition on the gain-update map in the gain-error state $\tilde K$, with rate $\alpha_K$. It is derived for adaptive Kalman (rate $\asymp 1/N$ with window length $N$) and for RMSProp's second-moment EMA (rate $1 - \beta$). It is assumed for adversarial / non-convex / regime-transitioning meta-gains.

4. **Two-timescale singular perturbation?** No, not in the Tikhonov-reduction sense. The correct framing is **two applications of `#result-sector-persistence-template`** via an augmented-state Lyapunov function with cross-coupling bound (§7). Timescale separation enters as $\alpha_K \ll \underline\alpha$ on Lyapunov decay rates, which serves the role of Tikhonov's $\epsilon \to 0$ but without eliminating the fast variable — the persistence bound keeps both states and quantifies their coupling.

5. **Does the A2' sub-scope partition itself need revision?** Yes — refinement, not overhaul. The current $\alpha$ / $\beta$ split becomes $\alpha_1$ (fixed-gain, Prop B.3 via B1) / $\alpha_2$ (adaptive-gain, via (MG-1)–(MG-4) and augmented-state Lyapunov) / $\beta$ (everything else). This preserves all existing sub-scope $\alpha$ language as a specialization — adaptive-gain-preserved-as-$\alpha_2$ reduces to the original $\alpha_1$ by setting $\tilde K \equiv 0$.

## 12. Open questions after this spike

1. **Rate-specific results.** §7's composed persistence is a bound, not a rate. Can the $1/\sqrt{N}$ rate of Mehra-adaptive-Kalman be derived as a rate from §7's augmented-state Lyapunov, or is it external theorem?
2. **Identifiability as meta-gain fail-mode.** §9 Obstruction O1 suggests adaptive-gain has its own `#disc-identifiability-floor` instance: Mehra non-identifiability, or IMM unidentifiable-regime-process, blocks the $\alpha_2$ derivation. Worth a sharper statement co-located with or cross-referenced from `#disc-identifiability-floor`.
3. **Adversarial adaptive-gain.** If the environment adversarially varies $K^\ast$ (regime-switching under hostile cadence), the dwell-time repair of §5.3 fails. Is there an adversarial-tempo-advantage analog for the meta-gain level? (`#result-adversarial-tempo-advantage`'s argument structure looks like it transfers: faster meta-gain tracking beats faster environmental regime switching iff $\alpha_K T_{\text{dwell}} > $ transition rate. Not derived here; adjacent spike.)
4. **Discrete-time form.** Everything above is continuous-time. The discrete-time version involves the additional Lipschitz bound of `#deriv-discrete-sector-condition`, now on both $F$ and $\Phi$. Presumably an extension of §7 to discrete time exists; left for future work.
5. **Connection to `#schema-strategy-persistence` time-varying $\alpha$.** `#result-sector-persistence-template` Working Notes already flag time-varying $\alpha(t)$ as a candidate extension. Adaptive gain is one concrete source of time-varying $\alpha$. The $\alpha_\Sigma = 1/(n+1)$ decay in `#schema-strategy-persistence` (requiring experience discounting) is a related pattern — an adaptive gain that *does not* preserve (MG-1) without extra machinery. Re-reading that segment through the $\alpha_2$ lens could clarify why experience discounting is formally necessary.

## 13. References

**Adaptive Kalman / innovation-based estimation:**
- Mehra, R. K. (1970). "On the identification of variances and adaptive Kalman filtering," *IEEE Trans. Automatic Control* 15(2):175-184.
- Mehra, R. K. (1972). "Approaches to adaptive filtering," *IEEE Trans. Automatic Control* 17(5):693-698.
- Mohamed, A. H., & Schwarz, K. P. (1999). "Adaptive Kalman filtering for INS/GPS," *J. Geodesy* 73(4):193-203.
- Särkkä, S. (2013). *Bayesian Filtering and Smoothing*. Cambridge University Press. Ch. 12 (adaptive filters).
- Zagrobelny, M. A., & Rawlings, J. B. (2015). "Identifying the uncertainty structure using maximum likelihood estimation," American Control Conference. [stability-sensitive treatment]
- Dunik, J., Straka, O., Kost, O., Havlik, J. (2021). "On the identification of noise covariances and adaptive Kalman filtering: A new look at a 50 year-old problem," *Frontiers in Signal Processing*. [rank identifiability via minimal polynomial; see PMC8638515]

**Two-timescale stochastic approximation / adaptive step size:**
- Borkar, V. S. (1997). "Stochastic approximation with two time scales," *Systems & Control Letters* 29(5):291-294.
- Borkar, V. S. (2008). *Stochastic Approximation: A Dynamical Systems Viewpoint*. Cambridge University Press.
- Reddi, S. J., Kale, S., Kumar, S. (2018). "On the convergence of Adam and beyond," ICLR 2018. [AMSGrad correction]
- Li, X., & Orabona, F. (2019). "On the convergence of stochastic gradient descent with adaptive stepsizes," AISTATS.
- Défossez, A., Bottou, L., Bach, F., Usunier, N. (2022). "A simple convergence proof of Adam and Adagrad," TMLR.

**MRAC / Lyapunov adaptive control:**
- Narendra, K. S., & Annaswamy, A. M. (1989). *Stable Adaptive Systems*. Prentice Hall.
- Ioannou, P. A., & Sun, J. (1996). *Robust Adaptive Control*. Prentice Hall.
- Annaswamy, A. M., & Fradkov, A. L. (2021). "A historical perspective of adaptive control and learning," arXiv:2108.11336.

**Interacting multiple models:**
- Blom, H. A. P., & Bar-Shalom, Y. (1988). "The interacting multiple model algorithm for systems with Markovian switching coefficients," *IEEE Trans. Automatic Control* 33(8):780-783.
- Li, X. R., & Jilkov, V. P. (2005). "Survey of maneuvering target tracking. Part V: Multiple-model methods," *IEEE Trans. Aerospace and Electronic Systems* 41(4):1255-1321.

**MAML / meta-learning convergence:**
- Finn, C., Abbeel, P., Levine, S. (2017). "Model-agnostic meta-learning for fast adaptation of deep networks," ICML.
- Fallah, A., Mokhtari, A., Ozdaglar, A. (2020). "On the convergence theory of gradient-based model-agnostic meta-learning algorithms," AISTATS.
- Ji, K., Yang, J., Liang, Y. (2022). "Theoretical convergence of multi-step model-agnostic meta-learning," *J. Machine Learning Research* 23:1-41.

**AAD segments referenced:**
- `#emp-update-gain`, `#der-gain-sector-bridge`, `#deriv-gain-sector`, `#deriv-sector-condition`, `#result-sector-condition-stability`, `#result-sector-persistence-template`, `#sketch-multi-timescale-stability`, `#result-structural-adaptation-necessity`, `#result-persistence-condition`, `#schema-strategy-persistence`, `#result-adversarial-tempo-advantage`, `#disc-identifiability-floor`, `#der-temporal-nesting`, `#deriv-discrete-sector-condition`.

**Standard references (already in use):**
- Khalil, H. K. (2002). *Nonlinear Systems*, 3rd ed. Prentice Hall. Ch. 4 (Lyapunov), ch. 9 (input-output), ch. 11 (singular perturbation).
- Khasminskii, R. (2012). *Stochastic Stability of Differential Equations*, 2nd ed. Springer. Ch. 5 (stochastic Lyapunov / stopping-time localization).
- Nesterov, Y. (2004). *Introductory Lectures on Convex Optimization*. Springer. Thm 2.1.10.
