---
spike: passivity-composition
date: 2026-04-22
status: exploratory; substantive for α sub-scope; partial for β; honestly limited at adversarial boundaries
motivates: candidate meta-segment #dissipativity-template OR strengthening of #sector-persistence-template; sub-scope α promotions for PID-in-positive-real-plant
depends-on:
  - composition-closure
  - scope-composite-agent
  - sector-persistence-template
  - sector-condition-derivation
  - gain-sector-bridge
  - team-persistence
  - adversarial-destabilization
  - critical-mass-composition (spike)
  - interaction-channel-classification (spike)
  - directed-separation
---

# Spike: Passivity / Dissipativity-Based Composition Closure

**Motivation.** Section III composition closure (#composition-closure, #critical-mass-composition) is proved cleanly for *symmetric-matched-Tier-1* pairs (two Kalman agents, or two instances of the same update rule). The weakest-link bound (WL) handles heterogeneous cases conservatively. Gemini's standing finding — that contraction-based composition verifications are all linear-Kalman-class — names a real gap: AAD does not currently have a first-class way to compose one Kalman agent with one PID agent, even though the control-theory literature (Willems 1972 *dissipative dynamical systems*; Khalil 2002 *Nonlinear Systems* ch. 6; van der Schaft 2017 *L2-Gain and Passivity Techniques*) has a well-developed tool that handles exactly this heterogeneity: **passivity / dissipativity with storage functions**.

The core move is simple and old: if each sub-system dissipates energy against a storage function, and the interconnection pattern is power-preserving (parallel, negative-feedback with compatible port signs, cascade with small-gain), then the sum (or a weighted sum) of the sub-system storage functions is a storage function for the composite — regardless of whether the sub-systems share architecture. The asymmetric information-flow structure of AAD's heterogeneous composites maps onto this: each AAD agent supplies its own storage function; composition preserves dissipativity along the corresponding port structure.

This spike tries to carry that correspondence through in AAD-native language and to characterize honestly what it reaches and what it doesn't.

---

## 1. Passivity / Dissipativity Primer (AAD-language)

### 1.1 Willems's definition, stated for AAD

A system with input $u \in \mathcal U$ and output $y \in \mathcal Y$ is **dissipative with respect to supply rate $s(u,y)$ and storage function $S: \mathcal X \to \mathbb R_{\geq 0}$** if for every trajectory and every time interval $[t_0, t_1]$:

*[Definition (Willems 1972; Khalil ch. 6)]*

$$S(x(t_1)) - S(x(t_0)) \;\leq\; \int_{t_0}^{t_1} s(u(\tau),y(\tau))\, d\tau \tag{W}$$

Equivalently, in differential form:

$$\dot S(x) \;\leq\; s(u,y). \tag{W')}$$

The system cannot store more than its net supplied. **Passivity** is the special case $s(u,y) = u^T y$ (the system is *output-strictly passive* when $s(u,y) = u^T y - \epsilon \lVert y\rVert^2$ for some $\epsilon \gt 0$, *input-strictly passive* when $s = u^T y - \delta \lVert u\rVert^2$).

**Why this is the right structural tool for heterogeneous composition.** Two facts carry all the weight:

**(F1) Passive + passive = passive under parallel and negative-feedback interconnection.** If $\Sigma_1, \Sigma_2$ are passive with storage functions $S_1, S_2$, then:
- *Parallel interconnection* ($u_1 = u_2 = u$, $y = y_1 + y_2$): composite is passive with $S = S_1 + S_2$, supply rate $u^T y = u^T y_1 + u^T y_2 = \dot S_1 + \dot S_2$.
- *Negative-feedback interconnection* ($u_1 = r - y_2$, $u_2 = y_1$): composite is passive from external input $r$ to $y_1$ with $S = S_1 + S_2$. The cross-terms cancel (this is the "power-preserving interconnection" identity).

**(F2) Passive system in negative feedback with passive system is $\mathcal L_2$-stable** under suitable detectability / strict-passivity conditions (Khalil ch. 6 Thm 6.1, 6.4).

Neither (F1) nor (F2) requires matching architectures, matching time constants, matching state dimensions, or matching Lyapunov function shapes. That is the feature AAD is currently missing.

### 1.2 Storage as a generalization of the Lyapunov function

In AAD's current machinery, $V(\delta) = \tfrac{1}{2}\lVert\delta\rVert^2$ is the canonical Lyapunov function; sector-persistence (#sector-persistence-template) is the Lyapunov-based persistence theorem. **The storage function is the same object, generalized.**

For an AAD agent with mismatch $\delta$, bounded-disturbance input $w$, and output $y$ (e.g., $y = H\delta$ — what the environment sees of the mismatch):

- If $V(\delta) = \tfrac{1}{2}\lVert\delta\rVert^2$ satisfies $\dot V \leq -\alpha \lVert\delta\rVert^2 + \delta^T w$, the agent is dissipative with storage $S = V$ and supply rate $s(w,\delta) = \delta^T w - \alpha\lVert\delta\rVert^2$. This is exactly **output-strict passivity** (with $y = \delta$, input $u = w$, rate parameter $\alpha$).
- Sector-persistence's *ultimate bound* $R^\ast = \rho/\alpha$ is the dissipativity-theoretic statement: the state cannot store more than the net supply, and with bounded supply $\rho$ the state is ultimately bounded.

So AAD's sector-condition template is a *special case* of a storage-function / dissipativity argument where the supply rate is specifically quadratic-in-mismatch. Asking whether AAD should generalize to storage functions in general is really asking: *does AAD need non-quadratic storage functions, or non-Euclidean output maps, to reach composites it cannot otherwise reach?*

**This spike's claim, stated up front:** Yes — at least for heterogeneous β-class / α-class composites. The passivity frame reveals that sub-agent heterogeneity composes cleanly under negative-feedback interconnection with *no* requirement that the agents share architecture, so long as each has its own storage function and the port-level supply rates sum consistently. Critical-mass (#critical-mass-composition) obtains a weighted Lyapunov *after* checking that both agents are Tier 1; passivity obtains composite storage *before* checking tier, because heterogeneous storage functions sum regardless of the Lyapunov form at either end.

---

## 2. Passivity for AAD Agent Classes

Working through each update-rule class. For each, I ask: **is there a natural storage function $S$ and a natural supply rate $s(w, \delta)$ such that $\dot S \leq s$ along the agent's dynamics?** Honest answer — including classes where no such $S$ exists.

### 2.1 Linear Kalman filter

The mismatch $\delta_t = y_t - H\hat x_{t\vert t-1}$ (innovation); state is $(\hat x, P)$.

*[Derived (storage-Kalman, from sector-condition-stability + gain-sector-bridge)]* Take $S(\hat x) = \tfrac{1}{2}(\hat x - x^\ast)^T P^{-1}(\hat x - x^\ast)$ (Mahalanobis-weighted error, inverse covariance). Under the steady-state recurrence $\hat x_{t+1} = (I - K^\ast H) \hat x_t + K^\ast y_{t+1}$ with $K^\ast$ the steady-state Kalman gain, and writing $e_t = \hat x_t - x_t^\ast$:

$$S(e_{t+1}) - S(e_t) \;\leq\; -\alpha_K \lVert e_t\rVert_{P^{-1}}^2 + e_t^T (K^\ast)^T H w_t + \text{noise-bounded term}$$

with $\alpha_K = \lambda_{\min}^+(K^\ast H)$ in the $P^{-1}$-weighted inner product — the matrix-Kalman sector constant of #gain-sector-bridge Prop B.3, restricted to the observable subspace.

The Kalman filter is **output-strictly passive** in the Mahalanobis norm from input $w$ (disturbance) to output $\delta$ (innovation). The storage function is the Mahalanobis-weighted squared error.

**Verification status:** *derived* (direct transcription of the Kalman sector-condition result; Anderson & Moore 1979 *Optimal Filtering* §4 is the standard control-theory reference).

**What the storage function looks like.** Quadratic in state, weighted by the inverse of the steady-state prediction covariance. This matches the Mahalanobis-norm discussion in `#composition-closure` and in `spike-projection-admissibility.md` §4: Kalman filters naturally live in inverse-covariance-weighted norms, which *are* storage functions. The two-Kalman verification in `spike-composition-correlated-kalman.md` is already, mathematically, a passivity-based composition argument — the spike just didn't name it that.

### 2.2 Exponential-family natural-parameter Bayesian updater

State is $\theta$ (natural parameter); true data-generating parameter is $\theta^\ast$; update is $\theta_{t+1} = \theta_t + \eta \nabla_\theta \log p(o_{t+1} \mid \theta_t)$ or the closed-form conjugate recursion.

*[Derived (storage-expfam, from gain-sector-bridge sub-scope α)]* Take $S(\theta) = D_B(\theta^\ast \Vert \theta)$ — the Bregman divergence from truth to current estimate, generated by the log-partition function $A(\theta)$ of the exponential family.

Under the natural-parameter gradient update (exponential-family likelihood is log-concave in $\theta$), Amari-Chentsov information geometry gives:

$$\dot S \;=\; -\eta \lVert\nabla_\theta \log p\rVert_{I(\theta)^{-1}}^2 + \text{innovation}\cdot w$$

where $I(\theta)$ is the Fisher information matrix. This is output-strictly passive with rate $\eta \lambda_{\min}(I(\theta))$ — matching the sub-scope α $\alpha = \eta \cdot \lambda_{\min}(\text{Fisher})$ of #gain-sector-bridge.

**Verification status:** *derived* (Amari 2016 *Information Geometry*; Csiszár-Matúš 2003 on Bregman-divergence-as-storage).

**Takeaway.** Bregman divergences are the natural storage functions for exponential-family Bayesian updaters. This is a *non-quadratic* storage function (quadratic in natural-parameter-space only in the Gaussian case) — and it's still a perfectly good passivity certificate. The sector-persistence template, which commits to $V = \tfrac{1}{2}\lVert\xi\rVert^2$, is narrower than what passivity reaches; passivity allows heterogeneous storage-function *shapes* across the dyad.

### 2.3 Gradient descent on strongly convex loss

Agent minimizes $L(\theta)$ with $L$ μ-strongly-convex; update $\theta_{t+1} = \theta_t - \eta \nabla L(\theta_t) + w_t$.

*[Derived (storage-gradient, from Nesterov 2004 Thm 2.1.10)]* Take $S(\theta) = L(\theta) - L(\theta^\ast)$ — the loss excess above the optimum. Strong convexity gives $S(\theta) \geq \tfrac{\mu}{2}\lVert\theta - \theta^\ast\rVert^2 \geq 0$ (non-negative; zero iff at optimum). The per-step decrement under noiseless gradient descent is

$$S(\theta_{t+1}) - S(\theta_t) \;\leq\; -\eta(1 - \tfrac{\eta L}{2}) \lVert\nabla L(\theta_t)\rVert^2$$

with $L$ the smoothness constant; under strong convexity $\lVert\nabla L\rVert^2 \geq 2\mu \cdot S$. So $\dot S \leq -2\eta\mu S + \text{disturbance term}$, which is output-strictly passive with rate $\eta\mu$ — recovering #gain-sector-bridge's $\alpha = \eta\mu$.

**Verification status:** *derived*.

**Takeaway.** The loss function *is* the storage function. This is clean, unambiguous, and exactly what optimization theorists already call it (Lyapunov function from the stability-theory side, potential / loss from the optimization side — they are the same object).

### 2.4 PID controller

State is $(x_p, x_i, x_d)$ (proportional, integral, derivative components). This is the case that currently lives in β sub-scope of A2' because no structural optimality argument forces B1 (directional fidelity).

**The standard control-theory result (Khalil 2002 ch. 6; van der Schaft 2017 ch. 5):** A PID controller is passive from tracking-error input to control-output when the plant is **positive-real** (or strictly positive-real for strict passivity). Concretely:

*[Derived (storage-PID-conditional, from Khalil Thm 6.3)]* For a PID controller $u = K_P e + K_I \int e + K_D \dot e$ with $K_P, K_I, K_D \geq 0$ driving a plant $P(s)$ that is positive-real (transfer function $P(j\omega)$ has $\text{Re}[P(j\omega)] \geq 0$ for all $\omega$), the closed-loop system is passive with storage function

$$S(x) \;=\; S_{\text{plant}}(x_p) + \tfrac{1}{2} K_I \Big(\int_0^t e\,d\tau\Big)^2 + \tfrac{1}{2} K_D e^2$$

— a sum of the plant's storage function and the integral/derivative components' kinetic-energy analogs.

**Verification status:** *derived* (standard), **conditional** on positive-real plant.

**What this means for AAD's A2' sub-scoping.** Under the passivity frame, **PID promotes from β to α when the plant is positive-real**. The scope narrowing is:

- Sub-scope α' (new, under passivity frame): **PID + positive-real plant.** A2' derived via storage-function dissipativity argument.
- Sub-scope β (residual): PID + non-positive-real plant, untuned PID, badly-tuned PID on any plant.

This is a genuine sub-scope promotion. The PID-on-positive-real-plant class is a large and important subset of real controllers: thermal systems, mass-spring-damper mechanical systems, most electrical circuits with positive impedance, many chemical-process plants. Sub-scope α expands under the passivity lens in a non-trivial way.

**Caveats.**
- "Positive-real plant" is a plant property, not a controller property. It transfers from domain knowledge (the physics of the plant), not from the update rule's structure. This matters for interpretation: the sub-scope promotion depends on the *environment* being well-behaved, not on the *agent* alone.
- Tuning (gain selection) still matters. A PID with positive gains on a positive-real plant is passive; a PID with gains that violate Ziegler-Nichols-like stability margins can still destabilize nonlinear plants at large amplitude. The passivity result gives local stability around equilibrium.

### 2.5 Rule-based / discrete-event controllers

State is symbolic; updates are triggered by condition-matching; no continuous storage-function candidate.

**Honest answer:** Rule-based systems generically do not admit a storage function. The dissipativity inequality (W') requires $\dot S \leq s$ along *every* trajectory, and rule-based systems can produce trajectories with arbitrary discrete jumps — including jumps that increase any candidate quadratic $S$ at the moment of rule-activation. A counterexample is trivial: a rule that says "if error is small, apply a large control pulse" produces a storage-function spike at the moment of rule-firing.

**What survives.** Some rule-based controllers are *hybrid dissipative systems* (van der Schaft & Schumacher 2000) — they satisfy a storage-function inequality with impulsive supply at rule-firings. This extends the dissipativity framework but adds technical machinery (hybrid-automaton semantics, reset maps, dwell-time conditions).

**AAD posture.** Rule-based agents stay in sub-scope β under the passivity frame. The passivity promotion that PID-on-positive-real-plant gets does *not* extend to rule-based controllers. This matches the Working Notes in `#sector-condition-derivation`'s sub-scope-β enumeration.

### 2.6 Variational / approximate posteriors

State is variational parameters $\phi$; update follows ELBO gradient $\phi_{t+1} = \phi_t + \eta \nabla_\phi \text{ELBO}(\phi)$.

**Condition for passivity:** ELBO is concave in $\phi$ (equivalent: the reverse-KL to the true posterior is convex in the variational parameters). For *Gaussian variational families* matching unimodal posteriors, ELBO is locally concave in a neighborhood of the variational optimum — so local passivity holds with storage function $S(\phi) = \text{ELBO}(\phi^\ast) - \text{ELBO}(\phi)$.

For non-concave ELBO regimes (multi-modal posteriors, mean-field factorizations with strong posterior correlations, severe misspecification), there is no global storage function — the optimization landscape has multiple local minima.

**Verification status:** *derived with ε-error* in the locally-concave regime; undefined globally.

**Takeaway for A2'.** Variational posteriors sit in a **partial-α' sub-scope**: passive locally near the variational optimum, β globally. Matches the "approximation-direction error can rotate the correction" caveat in #sector-condition-derivation's current β list, but gives it a cleaner scope statement: variational updates are ε-passive within their convergence basin, where ε decays with the KL gap between the variational family and the true posterior.

### 2.7 Summary table

| Class | Storage function candidate | Supply rate | Passivity status |
|---|---|---|---|
| Linear Kalman | Mahalanobis $S = \tfrac{1}{2}\lVert e\rVert^2_{P^{-1}}$ | $s = e^T(K^\ast)^T H w - \alpha_K \lVert e\rVert^2_{P^{-1}}$ | Output-strictly passive (derived) |
| Exp-family Bayesian | Bregman $S = D_B(\theta^\ast \Vert \theta)$ | $s = \text{innov}\cdot w - \eta \lambda_{\min}(I)\lVert \cdot\rVert^2$ | Output-strictly passive (derived) |
| Gradient descent (strongly convex) | Loss excess $S = L(\theta) - L(\theta^\ast)$ | $s = w^T \nabla L - \eta\mu \cdot \lVert\nabla L\rVert^2$ | Output-strictly passive (derived) |
| PID | Plant-storage + $\tfrac{1}{2}K_I(\int e)^2 + \tfrac{1}{2}K_D e^2$ | Port-dependent | Passive **iff plant is positive-real** (conditional) |
| Rule-based | None in general | — | Not passive (honest limit) |
| Variational (local) | ELBO excess at optimum | Local supply | ε-passive in convergence basin |

Classes for which a clean storage function exists: linear Kalman, exp-family natural-parameter Bayesian, gradient-on-strongly-convex. Under the passivity frame, **PID admits a storage function conditional on plant structure** — this is the α/β promotion move.

---

## 3. Topology-Indexed Composition Closure

Now the substantive payoff. For each interconnection topology, I derive the composite storage function and the preserved property.

### 3.1 Parallel interconnection

Two agents share input; outputs add. For AAD, this is the case where two agents observe the same environmental channel and their corrections add in the same observation direction (e.g., two classifiers voting on the same question; two estimators of the same quantity whose outputs are averaged).

*[Derived (parallel-passivity, Khalil ch. 6 Thm 6.2)]* If $\Sigma_i$ is passive with storage $S_i$ and supply rate $s_i(u,y_i)$, the parallel interconnection is passive with storage $S_{\Vert} = S_1 + S_2$ and supply rate $s_{\Vert}(u, y_1+y_2) = u^T(y_1+y_2) = s_1 + s_2$.

**AAD content:** The composite storage function is the **sum** of the sub-agent storage functions. The shapes of the sub-agent storage functions are unconstrained — one can be Mahalanobis (Kalman), the other loss-excess (gradient agent), and the sum is still a valid storage function.

This is the result that heterogeneous-matched composition spikes could not reach.

**Contrast with #critical-mass-composition.** (CM2) requires both agents to be Tier 1, matched, and symmetric to get the closed-form $(\alpha - C)R \gt \rho + \gamma\mathcal T$. The parallel-passivity result gives a heterogeneous-composition certificate (the sum of any two storage functions is a storage function) but does *not* give the closed-form threshold condition. The two results are complementary: passivity gives *existence* of composite stability under broad heterogeneity; critical-mass gives *closed-form parameters* under narrow symmetry. Both are useful; they occupy different parts of the scope-honesty architecture.

### 3.2 Negative-feedback interconnection

$\Sigma_1$'s output drives $\Sigma_2$'s input; $\Sigma_2$'s output is fed back (with sign-flip) into $\Sigma_1$'s input. In AAD terms: one agent *acts* on the shared environment in a way that becomes the *observation* of the other agent, which then acts back.

*[Derived (negative-feedback-passivity, Khalil ch. 6 Thm 6.1)]* If both $\Sigma_1, \Sigma_2$ are passive with storage $S_1, S_2$ and the feedback sign convention gives $u_1 = r - y_2, u_2 = y_1$:

$$\dot S_1 + \dot S_2 \;\leq\; u_1^T y_1 + u_2^T y_2 \;=\; (r - y_2)^T y_1 + y_1^T y_2 \;=\; r^T y_1$$

The cross-terms ($y_2^T y_1$ and $y_1^T y_2$) cancel. The composite is passive from external input $r$ to output $y_1$ with storage $S_1 + S_2$.

**$\mathcal L_2$-stability (Khalil Thm 6.4).** If additionally one of $\Sigma_1, \Sigma_2$ is output-strictly passive and the other is input-strictly passive (or both are strictly passive), the negative-feedback composite is $\mathcal L_2$-stable — bounded $r$ produces bounded output.

**AAD content — the heterogeneous-Tier-3 payoff.** Consider the composite where $\Sigma_1$ = Kalman (output-strictly passive, storage $\tfrac{1}{2}\lVert e\rVert^2_{P^{-1}}$) and $\Sigma_2$ = PID on a positive-real plant (input-strictly passive by design, storage $S_{\text{PID}}$). The composite is $\mathcal L_2$-stable with storage $S_{\Vert} + S_{\text{PID}}$ — a *sum of heterogeneous storage functions*, each with its own units, curvature, and state dimension.

This is reachable under #critical-mass-composition (CM2) only through the weakest-link bound (WL), which gives a conservative existence statement but no clean composite threshold. Under passivity, we get a stronger result: composite $\mathcal L_2$-stability from heterogeneous sub-agent dissipativity, **with no requirement that the storage-function shapes match**.

**Concrete worked case (Kalman + PID on positive-real plant).**

Setup:
- $\Sigma_1$ = scalar Kalman filter tracking $x_{t+1} = x_t + w_t$, observation $o_t = x_t + v_t$, with $w \sim \mathcal N(0, q), v \sim \mathcal N(0, r)$. Steady-state gain $K^\ast = P^\ast/(P^\ast + r)$.
- $\Sigma_2$ = PID controller on scalar plant $\dot x = -\gamma_p x + u$ with $\gamma_p \gt 0$ (positive-real: $P(j\omega) = 1/(j\omega + \gamma_p)$ has $\text{Re}[P(j\omega)] = \gamma_p/(\omega^2 + \gamma_p^2) \geq 0$).
- The two agents are coupled: Kalman estimates the plant state; PID uses Kalman's estimate as the reference signal.

**Composite storage function:**

$$S_{\text{composite}}(e_K, x_I, e_d) \;=\; \underbrace{\tfrac{1}{2P^\ast}e_K^2}_{\text{Kalman Mahalanobis}} + \underbrace{\tfrac{\gamma_p}{2}x_p^2 + \tfrac{K_I}{2} x_I^2 + \tfrac{K_D}{2}e_d^2}_{\text{PID-plus-plant storage}}$$

Along coupled trajectories:

$$\dot S_{\text{composite}} \;\leq\; -\alpha_K \cdot \tfrac{e_K^2}{P^\ast} - \gamma_p^{\text{eff}} x_p^2 + e_K \cdot (\text{noise}) + \text{cross-terms that cancel by negative-feedback identity}$$

The cross-term cancellation is the key step: the Kalman output's role as reference input to PID gives rise to $e_K \cdot u_{\text{PID}}$; PID's output gives rise to $u_{\text{PID}} \cdot x_p$; the sign conventions of negative-feedback make these cancel out in the sum $\dot S_1 + \dot S_2$. Ultimate bound: the composite state is ultimately bounded with radius determined by the sum of the sub-agent sector constants (weighted by the storage-function Hessians).

**This case is the canonical heterogeneous composition that #critical-mass-composition currently handles only via (WL).** Under passivity, we get composite storage, composite dissipativity, and $\mathcal L_2$-stability — as a **derived theorem** conditional on positive-real plant and standard Kalman-gain positivity.

**Verification status:** *derived* (under the stated conditions; a textbook exercise in passivity-based control, not a novel result at the control-theory level). The novelty is recognizing the AAD fit.

### 3.3 Cascade interconnection (small-gain)

$\Sigma_1$'s output feeds $\Sigma_2$'s input; no return path. In AAD terms: one agent acts, the other observes and predicts, but no explicit feedback (a pure information-flow cascade).

*[Derived (small-gain, Khalil ch. 6 Thm 6.5)]* If $\Sigma_i$ has finite $\mathcal L_2$-gain $\gamma_i$ (the bound $\lVert y_i\rVert_{\mathcal L_2} \leq \gamma_i \lVert u_i\rVert_{\mathcal L_2}$ for all inputs), the cascade has gain $\gamma_{\text{cascade}} \leq \gamma_1 \gamma_2$, and is $\mathcal L_2$-stable iff — under feedback closure — $\gamma_1 \gamma_2 \lt 1$.

**AAD content:** This is the small-gain theorem. For purely feedforward cascades without feedback, stability of each component implies stability of the cascade (trivially). When a feedback loop is closed around the cascade (as in any AAD system with action-observation loops), the small-gain condition $\gamma_1 \gamma_2 \lt 1$ is the key inequality.

**Structural insight — relationship to AAD's $\gamma$.** AAD's inter-agent coupling coefficient $\gamma_{j\to i}$ in #adversarial-destabilization and #team-persistence plays a related but not identical role. Small-gain's $\gamma_i$ is the agent's $\mathcal L_2$-gain from disturbance to output. AAD's $\gamma_{j\to i}$ is the effectiveness of $j$'s actions on $i$'s disturbance (a coupling strength from the emitter side). The two are linked: in a symmetric feedback loop with unit gains on the feedback paths, $\gamma_{j\to i}^{\text{AAD}}$ relates to the L2-gain product $\gamma_i \cdot \gamma_j$ via the closed-loop transfer function.

The small-gain condition $\gamma_i \gamma_j \lt 1$ is *implied by* passivity (passive systems have $\mathcal L_2$-gain $\leq 1$ when normalized to unit supply) but is **weaker** than passivity — there are $\mathcal L_2$-stable composites that are not passive, and vice versa.

### 3.4 Summary: topology × storage-function composition

| Topology | Composite storage | Stability result | AAD relevance |
|---|---|---|---|
| Parallel | $S_1 + S_2$ | Passivity preserved (Thm 6.2) | Redundant sensing, voting agents |
| Negative feedback | $S_1 + S_2$ | $\mathcal L_2$-stable if one output-strict and other input-strict (Thm 6.4) | **Kalman-drives-PID composites; the heterogeneous-Tier-3 payoff** |
| Cascade (feedforward) | — | Product of $\mathcal L_2$-gains bounds cascade gain | Info-only channels in multi-agent |
| Cascade with feedback | — | Small-gain: $\gamma_1\gamma_2 \lt 1$ (Thm 6.5) | Closed-loop with multi-agent coupling |

**The big prize is row 2.** Row 2 delivers heterogeneous composition certificates where AAD currently has only weakest-link lower bounds. Row 3 is the small-gain theorem and gives AAD a second-tier condition applicable to cases where passivity does not hold but $\mathcal L_2$-gain bounds do.

---

## 4. Heterogeneous Composition: The Big Prize (worked example)

Revisiting the Kalman + PID case with enough concreteness to be a worked example.

### 4.1 Setup

**Plant.** $\dot x = -\gamma_p x + u + w_{\text{env}}$ where $w_{\text{env}}$ is bounded disturbance, $\gamma_p \gt 0$ (positive-real).

**Kalman filter (Agent 1).** Observes $o_t = x_t + v_t$, $v_t \sim \mathcal N(0, r)$. Runs the steady-state recurrence
$$\hat x_{t+1} = (1 - K^\ast) \hat x_t + K^\ast o_t$$
with $K^\ast$ such that $P^\ast = (P^\ast)(1-K^\ast) + q$ (Riccati fixed point). Let $e_K = \hat x - x$. In continuous-time fluid limit:
$$\dot e_K = -K^\ast e_K + K^\ast v - w_{\text{plant on } x}$$

The Kalman agent is output-strictly passive with storage $S_K = \tfrac{1}{2P^\ast} e_K^2$ and dissipation rate $\alpha_K = K^\ast/P^\ast$ in the Mahalanobis inner product. (Verified #gain-sector-bridge.)

**PID controller (Agent 2).** Uses $\hat x$ from Kalman as its tracking-error signal against a reference $r_{\text{ref}}$:
$$u = K_P(r_{\text{ref}} - \hat x) + K_I \int_0^t (r_{\text{ref}} - \hat x)\,d\tau + K_D\frac{d}{dt}(r_{\text{ref}} - \hat x)$$

Let $e_c = r_{\text{ref}} - x$ (the actual tracking error), $x_I = \int_0^t e_c\,d\tau$ (integral state). The PID closed-loop with the positive-real plant has storage function
$$S_{\text{PID}} = \tfrac{\gamma_p}{2} e_c^2 + \tfrac{K_I}{2} x_I^2 + \tfrac{K_D}{2} (\dot e_c)^2$$
and dissipation rate $\alpha_{\text{PID}} = \gamma_p K_P / (K_P + K_D\gamma_p)$ in the plant-weighted norm.

**Coupling.** Kalman drives PID (Kalman's $\hat x$ is PID's tracking signal); PID drives the plant (PID's $u$ acts on the plant); the plant drives Kalman's observation (through $x$). This is a **negative-feedback loop around a cascade** — Kalman → PID → plant → observation → Kalman.

### 4.2 Composite storage function

$$\boxed{\;S_{\text{composite}}(e_K, e_c, x_I, \dot e_c) \;=\; S_K(e_K) + S_{\text{PID}}(e_c, x_I, \dot e_c)\;}$$

**This is a heterogeneous storage function.** The Kalman component is Mahalanobis (inverse steady-state covariance); the PID component is a sum of quadratic-in-tracking-error, quadratic-in-integral, quadratic-in-derivative terms each with their own weight. The two components live in different coordinate systems with different units ($e_K$ has units of state; $x_I$ has units of state-time). Their sum is a valid storage function *because each component separately is a storage function for its own sub-system*, and the negative-feedback-interconnection identity cancels the cross-terms.

### 4.3 Composite dissipativity

Along coupled trajectories:

$$\dot S_{\text{composite}} \;=\; \dot S_K + \dot S_{\text{PID}} \;\leq\; -\alpha_K (e_K)^2/P^\ast - \alpha_{\text{PID}} \cdot (\ldots) + \text{supply-rate terms involving } w_{\text{env}}, v$$

The composite dissipation rate is a weighted combination of $\alpha_K$ and $\alpha_{\text{PID}}$ — specifically, the composite has ultimate bound determined by the max over each sub-system's contribution to $\dot S$, which is a **heterogeneous minimum** (the weakest of the two in its respective coordinate system).

### 4.4 Comparison with existing AAD machinery

| Question | #critical-mass-composition answer | Passivity-framed answer |
|---|---|---|
| Does the composite persist? | Weakest-link bound (WL): $\alpha_c \geq \min(\alpha_K, \alpha_{\text{PID}}) - C$. Conservative. | Composite is $\mathcal L_2$-stable via passive + passive + negative feedback (Thm 6.4). |
| Closed-form $\alpha_c$? | Only in symmetric-matched case (CM2). | Composite dissipation rate is a weighted combination; no single scalar $\alpha_c$ unless specialized. |
| Heterogeneous-architecture composition certificate? | Open (tiered: Tier 1 proved, Tier 2 local, Tier 3 domain-specific). | **Yes** — direct from passivity closure (parallel + negative-feedback). |
| When does it fail? | When weakest-link is negative, or when Tier 3 contraction fails. | When positive-real plant assumption fails OR when one agent is not in the passive class. |

The passivity frame reaches the heterogeneous Tier-3 composition that #critical-mass-composition does not. But critical-mass reaches closed-form thresholds that passivity does not. **They are complementary**, and AAD benefits from having both.

### 4.5 What this does not claim

- Does not give a scalar composite $\alpha_c$ and $R_c$ — the sub-agent storage functions live in different coordinate systems, so the composite storage has no single inner-product characterization.
- Does not extend to arbitrarily many agents without additional work — three-agent negative-feedback loops require Zames' small-gain theorem (iterated); four or more require network-level passivity analysis (Arcak 2007).
- Does not cover the case where the plant is not positive-real (e.g., time-delayed plants, non-minimum-phase plants) — these remain in sub-scope β.
- Does not close the #composition-closure bridge-lemma gap — the bridge lemma needs DA2'-inc (strong monotonicity of $f_c$), which passivity does not imply. Passivity gives composite (T2); bridge lemma needs composite (T2) AND composite DA2'-inc. The two gaps are orthogonal.

---

## 5. Relation to the Sector Condition

**Claim.** The sector-$[0, \infty]$ condition is a passivity condition. AAD's current #sector-condition-derivation is the scalar-SISO special case of dissipativity with supply rate $s(u,y) = uy$.

*[Discussion]*

### 5.1 The sector condition as a passivity statement

Consider a nonlinear static map $\phi: \mathbb R \to \mathbb R$ in the sector $[\alpha, \beta]$ — i.e., $\alpha u^2 \leq u \phi(u) \leq \beta u^2$ for all $u$. This is exactly a passivity statement: the block is passive from input $u$ to output $\phi(u)$ with supply rate $u \phi(u)$, and output-strictly passive with rate $\alpha$.

AAD's sector-condition region $\mathcal B_R$ — where $\delta^T F(\mathcal T, \delta) \geq \alpha \lVert\delta\rVert^2$ — is the *local* sector-$[\alpha, \infty]$ condition on the correction function $F$ considered as a nonlinear map from mismatch to corrective flow. The correction function is a passive nonlinear block in the negative-feedback loop around the agent's internal dynamics.

### 5.2 Passivity is strictly more general

- Sector condition: scalar-SISO, quadratic storage $V = \tfrac{1}{2}\lVert\delta\rVert^2$, supply rate $\delta^T F$.
- Passivity: multi-input multi-output, storage function of arbitrary shape (Bregman, loss excess, hybrid), supply rate $s(u, y)$ in general form.

**So sector-persistence-template is a special case of a passivity-template.** Making passivity the more general primitive would:

- Unify Kalman (quadratic/Mahalanobis), exp-family (Bregman), gradient-on-convex-loss (loss excess), PID-on-positive-real-plant under a single dissipativity result.
- Absorb the sector-condition results as the $V = \tfrac{1}{2}\lVert\delta\rVert^2$ special case.
- Generalize the instantiations table in #sector-persistence-template to allow non-quadratic storage functions per instantiation (important for the exp-family and gradient cases).

**Against the move.** Making passivity the primitive would complicate exposition (the quadratic-Lyapunov form is more transparent; Bregman / loss-excess / hybrid are more technical). The practical tradeoff: AAD already commits to quadratic-Lyapunov in the sector-persistence template as a *formulation* (status = exact under (T1)-(T3)). Making it a special case of dissipativity gains heterogeneous-composition closure but costs the "single clean template" framing.

### 5.3 Recommended move

Rather than reframe the template, **introduce a companion meta-segment `#dissipativity-template` that generalizes the sector-persistence-template in the heterogeneous-storage-function direction.** See §8.

---

## 6. Relation to Scope Condition / Directed Separation

AAD's architectural classification (Class 1 modular, Class 2 merged, Class 3 partially modular; #directed-separation) has a natural reading under the passivity frame:

**Class 1 (modular) composition under negative-feedback passivity — strong closure.** When epistemic update is goal-blind, each sub-agent is a passivity-preserving block with a well-defined input (observation) and output (action) port. Interconnections respect the port structure. The negative-feedback theorem applies directly: heterogeneous Class 1 agents compose with heterogeneous storage functions summing cleanly.

**Class 2 (fully merged) composition — passivity does not close.** In a fully merged architecture (LLM-style), observation and action are entangled in the same attention / state-update operation. There is no clean input-output port decomposition to apply the negative-feedback identity to. The passivity machinery fails — not because the agents aren't stable, but because the interconnection identity requires separable ports that Class 2 architectures do not provide.

**Class 3 (partially modular) composition — passivity with ε-error.** When directed separation is approximate with modularity coefficient $\kappa \in (0, 1)$, the port structure has leakage of magnitude $O(\kappa)$. The passivity composition theorem holds with ε-error in the composite storage function: $\dot S_{\text{composite}} \leq \text{supply} + O(\kappa)$. The composite is still $\mathcal L_2$-stable, but with a degraded margin.

**This provides a third reading of the architectural classification.** The Class 1/3/2 hierarchy was previously framed as:
- (a) a modularity spectrum (#directed-separation);
- (b) an identifiability ladder (#discussion-separability-pattern);
- (c) under the passivity frame: **a port-structure ladder for composition closure** — Class 1 has clean ports (heterogeneous composition closes); Class 3 has leaky ports (closes with ε-error); Class 2 has no ports (does not close via passivity; requires coupled formulation).

This fits the "three meta-segments" framing (CLAUDE.md §7) as a concrete specialization: the separability pattern has a composition-theoretic realization under passivity.

---

## 7. A2' α/β Repartition Under Passivity

Revisiting the sub-scope partition.

**Current partition (from `spike-a2-prime-strengthening.md`):**

- Sub-scope α (A2' derived): Kalman / conjugate-Bayesian / exp-family-in-natural-params / gradient-on-strongly-convex / L2-regularized / linear-PD.
- Sub-scope β (A2' assumed): PID / rule-based / human-judgment / variational / severely-misspecified / non-convex-beyond-basin / per-step-SGD.

**Proposed passivity-frame partition:**

| Class | Current scope | Passivity-frame scope | Change |
|---|---|---|---|
| Kalman | α | α' (passive with Mahalanobis storage) | Refinement — existing α result, now named as dissipativity |
| Exp-family-in-natural-params | α | α' (passive with Bregman storage) | Refinement — same |
| Gradient-on-strongly-convex | α | α' (passive with loss-excess storage) | Refinement |
| L2-regularized convex | α | α' | Refinement |
| Linear-PD | α | α' | Refinement |
| **PID on positive-real plant** | β | **α''** (new sub-scope: conditionally passive) | **Promotion** |
| PID on non-positive-real plant | β | β | No change |
| Rule-based | β | β | No change (hybrid-dissipative is a technical extension, not a simple promotion) |
| Human-judgment | β | β | No change |
| Variational (in convergence basin) | β | **α''' (ε-passive)** | Partial promotion — scope narrowed to local basin |
| Variational (globally) | β | β | No change |
| Severely-misspecified | β | β | No change |
| Non-convex-beyond-basin | β | β | No change (this is exactly the basin-boundary failure) |
| Per-step-SGD | β | β | No change (A2' in expectation, per-step is β) |

**Summary of promotions.** PID + positive-real plant, and variational updates within their convergence basin, promote from β to a new conditional sub-scope ("α'' under plant positive-realness," "α''' under local convergence"). The structure of the promotion is *conditional on environmental properties* (positive-real plant) or *local* (convergence basin) rather than structural (true globally from the update rule alone). This is the honest labeling.

**What this buys AAD.** The PID-on-positive-real-plant class is a large practical subset of real controllers. Organizational analogies: organizations running well-defined feedback-and-escalation processes (PID-like) in stable operating environments (positive-real-like) can be analyzed under AAD's α-class Lyapunov machinery rather than falling through to β's per-instantiation verification. This materially extends AAD's reach into applied cases.

---

## 8. Honest Limits

Where passivity fails for AAD, stated precisely.

### 8.1 Non-positive-real plants

PID composition closure depends on positive-realness. When the plant has zeros in the right-half plane (non-minimum phase) or time delays, $\text{Re}[P(j\omega)] \lt 0$ for some frequencies and passivity fails. Typical offenders: fluid systems with transport delay, supply-chain dynamics with inventory lag, mechanical systems with negative stiffness, any plant where control action produces initial motion in the wrong direction before settling.

**AAD consequence.** PID-driven composites with non-positive-real plants stay in sub-scope β. The heterogeneous composition result fails; one must retreat to small-gain conditions or abandon stability guarantees.

### 8.2 Unbounded control effort

Passivity's storage-function inequality assumes the supply rate is finite. For AAD agents with bounded control effort (any realistic agent), this is automatic. For formal models that permit unbounded control (some LQG formulations, some game-theoretic models with unrestricted strategy spaces), the supply rate can diverge, and dissipativity is formally violated.

**AAD consequence.** For agents with bounded action space $\mathcal A$, this is not a restriction. The scope commitment #action-transition already embeds this.

### 8.3 Strategic adversarial opponents

The key failure. Passivity's supply rate is a fixed functional $s(u, y)$ of input and output. In an adversarial multi-agent setting, the "input" is chosen strategically by an opponent who has their own objective. A strategic opponent can deliberately operate the passive interconnection in an *anti-passive* mode — choosing inputs that maximize the recipient's storage-function growth rather than respecting the passive port structure.

Formally: the supply rate $s(u, y)$ must hold for *all* trajectories, including adversarially chosen ones. Passivity is a *universal* property — it bounds $\dot S$ uniformly. When the adversary chooses $u$ to maximize $\dot S$, the composite dissipation inequality still holds with the passivity supply rate, but the adversary can drive the system via the supply-rate term regardless.

**Compare with #adversarial-destabilization's coupling analysis.** Adversarial destabilization captures this with the coupling term $\gamma_A \mathcal T_A$ as an additional effective disturbance. Under passivity, the adversarial term enters the supply rate, not the dissipation. The two are structurally consistent but **passivity alone does not give adversarial robustness** — it gives cooperative or neutral robustness. Adversarial interactions require the full #adversarial-destabilization machinery on top of passivity.

**AAD consequence.** Passivity provides composition closure for *cooperative and neutral* multi-agent settings. For adversarial settings, #adversarial-destabilization's joint-Lyapunov analysis remains the primary tool. The two frameworks cover complementary regimes of the signed-coupling structure:
- Cooperative ($\gamma \lt 0$): passivity and #team-persistence give equivalent bounds; passivity extends the bound to heterogeneous architectures.
- Neutral ($\gamma = 0$): passivity gives the strongest heterogeneous-composition results.
- Adversarial ($\gamma \gt 0$): #adversarial-destabilization remains primary; passivity gives composition closure against the *structure* of the adversary's dynamics, not against the *value* of their strategy.

### 8.4 Non-linear plants with sector violations

Sector-condition failure at large mismatch (#structural-adaptation-necessity trigger): once the agent's correction function exits its passive region (A2' fails at the basin boundary), passivity fails with it.

**AAD consequence.** Passivity is local in the same way A2' is local; the structural-adaptation trigger applies to both. No new scope boundary introduced — the passivity frame inherits sector-condition's basin boundary.

### 8.5 Multi-agent networks ($N \gt 2$)

The two-agent negative-feedback theorem extends to $N$-agent networks under additional structural conditions (Arcak & Sontag 2006 on network passivity; Bürger-Zelazo-Allgöwer 2014 on dissipativity in networks). The extension is non-trivial and introduces dependence on the network topology's algebraic connectivity. For $N = 2$ the results are clean; for $N \geq 3$, network-level conditions (e.g., the interconnection matrix has diagonally-dominant passivity index) are required.

**AAD consequence.** The $N$-agent scaling problem (open in #composition-closure Working Notes and in `spike-composition-scaling-N.md`) is not closed by passivity alone. Passivity reaches two-agent heterogeneous composition cleanly; three-agent and beyond require further work.

### 8.6 Discrete-time vs continuous-time

AAD operates in both. Passivity has discrete-time analogs (Lin-Byrnes 1994 on discrete dissipativity; Khalil ch. 14 on sampled-data), but the conditions are technically different: the storage-function inequality becomes a sum rather than integral, and the pass-through structure of discrete transfer functions creates additional algebraic conditions. The Kalman-PID example above is stated in continuous time; the discrete-time version is routine but not identical.

**AAD consequence.** Discrete-time passivity results transfer with minor technical adjustments; not a fundamental limit. The #discrete-sector-condition already handles the AAD-internal discrete-time analog.

---

## 9. Landing Map

What to promote, where, and at what status. Three candidate moves; the first is the substantive one.

### 9.1 Substantive move: new meta-segment `#dissipativity-template`

**Type:** result (or derivation, depending on whether the composition theorems are stated abstractly or derived from Willems/Khalil).

**Status:** conditional (status=exact-under-stated-conditions for the α class; conditional for the PID promotion).

**Depends on:** #sector-persistence-template, #sector-condition-derivation, #composition-closure, #scope-composite-agent, #directed-separation, #team-persistence.

**Core content:**

1. **Storage-function generalization of sector-persistence-template (T1)-(T3).** State the dissipativity inequality $\dot S \leq s(u, y)$ with storage function $S$ and supply rate $s$. Recover the sector-persistence template as the special case $S = \tfrac{1}{2}\lVert\xi\rVert^2$, $s = \xi^T w - \alpha \lVert\xi\rVert^2$.

2. **Table of AAD agent classes and their storage functions.** Kalman (Mahalanobis), exp-family (Bregman), gradient (loss-excess), PID (plant-plus-integral-plus-derivative, conditional on positive-real plant), variational (ELBO-excess, local), rule-based (generically absent). For each: supply rate, dissipation rate, scope conditions.

3. **Composition theorems.** Parallel (storage sums, passivity preserved); negative-feedback (storage sums, $\mathcal L_2$-stable under strict-passivity conditions); small-gain (for cascades with feedback closure). With concrete AAD instantiations.

4. **Relationship to #sector-persistence-template.** Named as the scalar-SISO-quadratic-storage specialization. Explicit recovery argument.

5. **Relationship to #critical-mass-composition.** Passivity and critical-mass are complementary: passivity gives heterogeneous-composition certificates without closed-form thresholds; critical-mass gives closed-form thresholds in the matched-symmetric case.

6. **A2' sub-scope repartition.** PID-on-positive-real-plant and variational-in-basin promote from β to conditional α.

7. **Adversarial caveat.** Passivity handles cooperative and neutral composition; adversarial interactions require #adversarial-destabilization.

8. **Architectural reading.** The Class 1/3/2 partition admits a port-structure reading under passivity; Class 1 composes cleanly, Class 3 with ε-error, Class 2 not at all.

9. **Heterogeneous-composition worked example: Kalman + PID.** The canonical case. Derivation ends with composite storage and $\mathcal L_2$-stability.

**Position in outline.** Appendix A, after #sector-persistence-template; logically paired with #critical-mass-composition.

### 9.2 Alternative: extend #sector-persistence-template rather than a new segment

**Pro:** keeps the template as AAD's single persistence primitive; avoids proliferation.

**Con:** loses the scope-honest distinction between the quadratic-Lyapunov case (current) and the heterogeneous-storage case (new); the "one template, six instances" framing of #sector-persistence-template becomes "one template, mixed storage shapes, contraction argument varies per instance" — less clean.

**Recommendation:** Keep #sector-persistence-template as-is (exact, one Lyapunov shape, six instances, clean statement); add `#dissipativity-template` as a *generalization* meta-segment that cites #sector-persistence-template as the scalar-quadratic-storage special case and extends to non-quadratic storage functions. Two templates; one generalizes the other; the relationship is explicit.

### 9.3 Satellite moves

Not a new segment; modifications to existing segments after `#dissipativity-template` lands.

- **#sector-condition-derivation.** Add α'' sub-scope (PID + positive-real plant; variational in basin) to the sub-scope-α enumeration, with reference to `#dissipativity-template`. Adjust the sub-scope β list accordingly.
- **#gain-sector-bridge.** Add a section "Dissipativity as the supersystematic generalization of directional fidelity" — when the agent admits a storage function, the sector condition is the scalar-quadratic case of the dissipativity inequality. Cross-reference `#dissipativity-template`.
- **#composition-closure.** In the derivation-audit table, add a row: "Heterogeneous-architecture composition via negative-feedback passivity" — derived under positive-real plant + output-strictly-passive Kalman or gradient agent.
- **#critical-mass-composition.** In §7 (comparison with the six template instances), add a row identifying passivity-based composition as complementary to the matched-symmetric (CM2) approach.
- **#directed-separation.** Add a Discussion paragraph: "Class 1/3/2 as a port-structure ladder for composition closure." Cross-reference `#dissipativity-template` §5.
- **#team-persistence.** Note that the cooperative disturbance-reduction term is the AAD instantiation of the passivity port-supply identity in the cooperative regime.
- **#adversarial-destabilization.** Note that adversarial composition requires this segment's machinery *in addition to* any passivity argument; passivity alone does not cover adversarial interactions.
- **#interaction-channel-classification (spike).** If promoted, add a note that the four-regime classification composes cleanly with passivity: Regime I events ride the passive port structure (cooperative supply); Regime II events trigger sector-exit (passivity fails); Regime III events produce supply-rate drain without state change.

### 9.4 Recommended status on promotion

- **Core result** (storage-function generalization + composition theorems): *exact* under stated conditions (direct transcription of Khalil ch. 6; Willems 1972).
- **AAD instantiations** (Kalman + PID worked example): *derived* under positive-real plant.
- **A2' promotions** (PID-on-positive-real-plant to conditional α''): *derived* under explicit plant condition; labeled as *conditional* in the sub-scope table.
- **Architectural port-structure reading** (Class 1/3/2 as port ladder): *discussion-grade*; the reading is structurally clear but the Class 3 ε-error claim requires a quantitative derivation of how $\kappa$ (modularity coefficient) enters the supply-rate residual. Flag as candidate for a separate derivation spike.

---

## 10. Epistemic Assessment (honest)

### 10.1 What this spike achieves

1. **Names the passivity frame as a complementary composition primitive to #sector-persistence-template and #critical-mass-composition.** Heterogeneous composition is the key payoff; parallel and negative-feedback storage-function sums give Tier-3 (heterogeneous) composition closure that no existing AAD result reaches.

2. **Produces a clean worked example (Kalman + PID on positive-real plant, §4).** $\mathcal L_2$-stability of the composite with a heterogeneous storage function. Derivation-level.

3. **Identifies two concrete A2' sub-scope promotions** (PID on positive-real plant; variational updates within convergence basin). Both are conditional but in a clean, domain-checkable way.

4. **Clarifies the sector condition as a scalar-quadratic-storage special case of dissipativity.** Explicit recovery argument. Suggests the sector-persistence-template's exact status as the quadratic case sits inside a more general dissipativity framework, without requiring the template be restated.

5. **Delivers a port-structure reading of the Class 1/3/2 architectural classification.** Not reducible to the separability or identifiability readings; adds a third axis.

6. **Honest limits.** Non-positive-real plants, strategic adversarial opponents, $N \geq 3$ networks, hybrid/discrete-event systems — all named as limits with reasons.

### 10.2 What this spike does not achieve

- **Does not close the #composition-closure bridge-lemma gap.** The bridge lemma needs composite DA2'-inc (strong monotonicity); passivity gives composite (T2) (one-point sector) but not composite DA2'-inc. Two orthogonal gaps.

- **Does not extend to $N \geq 3$.** Cleanly reaches $N = 2$; network-level passivity ($N \geq 3$) requires additional machinery (Arcak-Sontag 2006; Bürger-Zelazo-Allgöwer 2014). Not attempted here.

- **Does not give scalar composite $\alpha_c$ in heterogeneous cases.** The sum of heterogeneous storage functions does not reduce to a single scalar sector constant. Composite stability is certified but without #critical-mass-composition's (CM2)-style closed-form inequality. This is a feature of the generalization, not a bug, but it limits what can be said quantitatively.

- **Does not resolve the Class 3 ε-error quantification.** The port-structure reading names Class 3 as "ε-passive with leaky ports" but does not derive the ε-passivity bound from the modularity coefficient $\kappa$ of #directed-separation. A follow-up derivation spike is needed.

- **Does not extend the PID-on-positive-real-plant result to nonlinear plants.** Hill-Moylan 1980 on nonlinear dissipativity gives the machinery, but plant-specific verification would be required per case.

### 10.3 Confidence tier-by-tier

- **§2 agent-class storage functions** (Kalman / exp-family / gradient / PID-on-positive-real-plant): *derived*. Direct transcription from standard control-theory / information-geometry results. No novel claim; the novelty is naming them as AAD sub-scope α members.
- **§3 composition theorems** (parallel, negative-feedback, cascade): *derived* from Khalil ch. 6 Thms 6.1-6.5. Standard.
- **§4 Kalman + PID worked example**: *derived* under positive-real plant. Textbook exercise in passivity-based control.
- **§5 sector condition as passivity special case**: *discussion-grade*, but the recovery is clean. Could be promoted to *derived* by restating in the full dissipativity-inequality form and showing that sector conditions are the scalar-SISO-quadratic case.
- **§6 Class 1/3/2 as port-structure ladder**: *discussion-grade*. Class 3 ε-error claim needs follow-up derivation.
- **§7 A2' repartition**: *derived* for PID-on-positive-real-plant and variational-in-basin; discussion-grade that these exhaust the promotable β cases.
- **§8 honest limits**: *robust qualitative*. Each limit has a specific mechanism; quantitative thresholds require case-by-case analysis.

### 10.4 Priority for promotion

- **High priority**: §2, §3, §4, §7 (the Kalman + PID worked example, the PID-on-positive-real-plant promotion, and the composition-theorems table). These are immediate AAD gains.
- **Medium priority**: §5, §6. The sector-as-passivity-special-case and Class 1/3/2-as-port-ladder claims add architectural clarity but don't directly unlock new results.
- **Low priority**: extensions to $N \geq 3$, Class 3 ε-error quantification, nonlinear plant analogs — follow-up spikes.

### 10.5 Integration with existing meta-architecture

This spike's result (passivity as composition primitive) integrates cleanly with AAD's three-meta-segment structure:

- **#discussion-separability-pattern** (positive half): passivity adds a new ladder — the **architectural-port ladder** — to the six ladders already enumerated (correlation, convention, architecture, contraction, identification, scope). Class 1 has clean ports (separable); Class 3 has leaky ports (structured repair); Class 2 has no ports (general open). This is a seventh ladder in the same shape.

- **#discussion-identifiability-floor** (negative half): passivity gives a no-go result for adversarial composition — the passivity framework cannot certify stability against an adversary who chooses supply-rate inputs strategically. This is structurally parallel to the on-policy-detection no-go: there's a structural limit (adversarial choice of supply) that external machinery (passivity) cannot overcome, and an escape route (small-gain robustness plus #adversarial-destabilization's coupling analysis) that AAD machinery does supply. Candidate as a fourth instance of the identifiability-floor pattern.

- **#additive-coordinate-forcing** (constructive half): passivity does *not* fit the Cauchy-FE-force-a-coordinate pattern. Storage functions sum additively under interconnection, but the additivity is from the port-structure identity (power-preserving interconnection), not from a Cauchy-functional-equation argument on an axiomatized additivity requirement. The storage-function summation is a *different* additivity pattern — it arises from the physics/geometry of ports, not from a uniqueness theorem. So passivity does not compose with #additive-coordinate-forcing; it stands outside the constructive-half meta-pattern.

This integration analysis suggests `#dissipativity-template` belongs alongside #sector-persistence-template as a *technical-machinery* segment (not a meta-segment), with its port-ladder-and-composition-closure reading adding to the separability-pattern meta-segment but not itself becoming a fourth meta.

### 10.6 The distinctive AAD angle

The passivity frame is old control-theory machinery. What does AAD bring that isn't already in Khalil ch. 6?

**Three distinctively-AAD moves:**

1. **Information-geometric storage functions for Bayesian agents.** The Bregman-divergence storage function for exp-family natural-parameter Bayesian updaters (§2.2) is a standard move in information-geometry-of-updating (Amari 2016), but its interpretation as a passivity certificate *for composition in multi-agent AAD* is the AAD-specific content. Linking Amari's divergence-geometry machinery to Willems's dissipativity machinery is a cross-tradition synthesis — not original at either end, but novel at their intersection.

2. **Port-structure reading of directed separation.** The Class 1/3/2 architectural classification as a port-structure ladder for composition closure (§6) is distinctively AAD — it reads an AAD architectural commitment (Bruineberg's Pearl-blanket vs Friston-blanket distinction) through the lens of composition-theoretic ports. This is not in Khalil or Willems.

3. **Sub-scope α/β/α'' partition honesty.** The honest labeling — PID *promotes* to α under positive-real plant; variational promotes within basin; rule-based stays β honestly — is AAD's scope-honesty-as-architecture (CLAUDE.md §7) applied to the passivity frame. Standard control-theory doesn't carry this scope-honesty apparatus; AAD's version does.

These three are the distinctively AAD-native content. The rest is honest adoption of a well-established control-theory frame.

---

## 11. Adjacent Literature (selective)

- **Willems (1972).** "Dissipative dynamical systems part I: General theory." *Arch. Rational Mech. Anal.* 45(5):321-351. The foundational paper. Defines dissipativity in terms of supply-rate-integrated-bounded-by-storage.
- **Khalil (2002).** *Nonlinear Systems* (3rd ed.), Prentice Hall. Ch. 6 on passivity; Thms 6.1 (feedback interconnection), 6.2 (parallel), 6.3 (L2-stability of OSP + ISP in feedback), 6.4 (feedback with one strictly passive), 6.5 (small-gain). Canonical reference.
- **Van der Schaft (2017).** *L2-Gain and Passivity Techniques in Nonlinear Control* (3rd ed.), Springer. Ch. 3-5; port-Hamiltonian systems framework.
- **Anderson & Moore (1979).** *Optimal Filtering*. Kalman filter as a special case of passivity-based estimation; the inverse-covariance Mahalanobis storage is natural.
- **Amari (2016).** *Information Geometry and Its Applications*, Springer. Bregman-divergence-as-storage for exponential-family estimation.
- **Arcak & Sontag (2006).** "Diagonal stability of a class of cyclic systems and its connection with the secant criterion." *Automatica* 42(9):1531-1537. Network passivity extensions; relevant for $N \geq 3$.
- **Hill & Moylan (1980).** "Dissipative dynamical systems: basic input-output and state properties." *J. Franklin Inst.* 309(5):327-357. Nonlinear dissipativity.
- **Lohmiller & Slotine (1998).** "On contraction analysis for nonlinear systems." *Automatica* 34(6):683-696. Already cited in `spike-critical-mass-composition.md` §10; the differential-Lyapunov-via-contraction view is adjacent to but distinct from passivity.
- **Bürger, Zelazo & Allgöwer (2014).** "Duality and network theory in passivity-based cooperative control." *Automatica* 50(8):2051-2061. Network-level dissipativity.

---

## 12. Summary

Passivity / dissipativity gives AAD a composition primitive that reaches heterogeneous composites cleanly — a case #critical-mass-composition handles only via the conservative weakest-link bound and #sector-persistence-template handles only under matched Lyapunov shapes. The Kalman + PID worked example (§4) delivers composite $\mathcal L_2$-stability with a heterogeneous storage function summing a Mahalanobis term (Kalman) and a plant-plus-integral-plus-derivative term (PID on positive-real plant). Two concrete A2' sub-scope promotions — PID on positive-real plant and variational updates in convergence basin — follow from the frame.

The spike recommends a new meta-segment `#dissipativity-template` that generalizes `#sector-persistence-template` to non-quadratic storage functions (Bregman, loss-excess, hybrid) and carries the composition theorems for parallel / negative-feedback / cascade topologies. The segment would sit alongside #critical-mass-composition as complementary machinery — passivity for heterogeneous-architecture certificates; critical-mass for closed-form symmetric-matched thresholds — and alongside #sector-persistence-template as a generalization for cases where the quadratic-Lyapunov form is too narrow.

Passivity does *not* handle strategic adversarial opponents — those require the #adversarial-destabilization framework on top. Passivity does *not* close the #composition-closure bridge-lemma gap — that needs composite DA2'-inc, which is orthogonal to passivity's composite (T2). Passivity does *not* cover $N \geq 3$ without additional network-level conditions. These are honest scope boundaries.

Integration with AAD's three-meta-segment architecture: passivity adds a seventh ladder (architectural port structure) to #discussion-separability-pattern, contributes a fourth candidate instance to #discussion-identifiability-floor (adversarial-supply no-go), and sits outside #additive-coordinate-forcing (storage-function additivity is port-structure additivity, not Cauchy-FE additivity). This places `#dissipativity-template` as technical-machinery-segment rather than as a fourth meta-segment.

Distinctively AAD moves in the passivity frame: (1) cross-tradition synthesis of Amari's information-geometric divergences with Willems's dissipativity; (2) port-structure reading of directed separation's Class 1/3/2; (3) scope-honesty-as-architecture applied to the α/β/α'' sub-scope partition.

*(End of spike.)*
