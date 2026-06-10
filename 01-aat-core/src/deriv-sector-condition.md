---
slug: deriv-sector-condition
type: derivation
status: exact
depends:
  - def-adaptive-tempo
  - def-mismatch-signal
  - form-sector-condition
stage: claims-verified
---

# Derivation: Sector Condition Stability — Lyapunov Derivation

The Lyapunov machinery underlying the sector-condition stability result and the central persistence inequality. The mismatch dynamics are taken in general nonlinear vector form, $\dot\delta = -F(\mathcal{T},\delta) + w(t)$, with the correction function $F$ required to satisfy only the *qualitative* properties (A1)–(A3) and the local sector condition (A2') stated in `#form-sector-condition`. The Lyapunov function is the canonical quadratic $V = \tfrac{1}{2}\lVert\delta\rVert^2$; the steady-state results follow from standard Lyapunov / Itô-Lyapunov machinery applied to AAT's correction-function object.

The derivation produces the framework's central persistence results in their precise form. **Proposition A.1 (Model D — bounded disturbance):** under $\lVert w(t)\rVert \leq \rho$ and the sector condition, mismatch is ultimately bounded by $R^\ast = \rho/\alpha$ — exactly the persistence threshold the chapter cites, and $\mathcal B_R$ is positively invariant when $\alpha R \gt \rho$. **Proposition A.1S (Model S — additive stochastic disturbance):** the region-aware Itô-Lyapunov analysis gives the stopped second-moment bound, the steady-state RMS $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$ (the $1/\sqrt\alpha$ scaling that distinguishes Model S from Model D's $1/\alpha$ scaling), and the stationary-sharp fixed-time tail $P(\lVert\delta(t)\rVert \gt R) \leq n\sigma_w^2/(2\alpha R^2)$. **Proposition A.2 (adaptive reserve):** $\Delta\rho^\ast = \alpha R - \rho$ — the additional disturbance an agent can absorb before mismatch leaves the sector-condition region.

The segment's load-bearing new exact result is **Corollary A.1S.1 — the disturbance-model containment dichotomy.** The persistence-region first-exit probability is *categorical*: $P(\tau_R \lt \infty) = 0$ under Model D (deterministic positive invariance), $P(\tau_R \lt \infty) = 1$ under Model S (a.s. exit of a non-degenerate diffusion from a bounded region, for *any* $F$ satisfying A2'). The achievable value is exactly the two-point set $\{0,1\}$, and which point obtains is fixed by the disturbance model's support structure (bounded vs. unbounded), **not** by correction strength $\alpha$. Increasing $\alpha$ tightens the typical scale and the fixed-time tail; it cannot interpolate between the two regimes. Pathwise containment is categorically Model-D-only — additive stochastic forcing removes the *kind* of guarantee available, not merely its rate. The companion no-go demonstration (that the natural Ville/Doob maximal-inequality route to a $P(\tau_R \lt \infty) \lt 1$ bound *cannot* exist) is in `#deriv-stochastic-non-exit`. The dichotomy sharpens the hand-off into `#result-structural-adaptation-necessity`: in any genuinely stochastic environment, leaving the parametric-correction region is a certain eventual event, so structural adaptation is *generic, not exceptional*, for any sufficiently long-lived agent. The sub-scope $\alpha$ / $\beta$ partition (where A2' is structurally derived versus where it is per-system assumed) is held at `#form-sector-condition`; the Lyapunov proofs below apply uniformly across both.

## Motivation

#hyp-mismatch-dynamics hypothesizes the linear ODE $d\Vert\delta\Vert/dt = -\mathcal{T}\Vert\delta\Vert + \rho$ as a first-order approximation. The linear form yields clean closed-form results but commits to a specific functional relationship between mismatch magnitude and correction rate. True correction dynamics are almost certainly nonlinear — exhibiting saturation at large mismatch, threshold effects near zero, and structural breakdown when the model class is exhausted.

A Lyapunov approach proves persistence and stability under much weaker assumptions: any correction dynamics satisfying qualitative monotonicity properties (the sector condition). The results below are strictly more general — the linear case is recovered where the sector bounds coincide.

## Setup

Let $\delta(t) \in \mathbb{R}^n$ be the mismatch vector — the difference between the model's predictions and reality across $n$ observable dimensions. The vector treatment connects to per-dimension tempo analysis ( #result-per-dimension-persistence).

The mismatch dynamics are:

*[Definition (Dynamics Setup)]*

$$\frac{d\delta}{dt} = -F(\mathcal{T}, \delta) + w(t)$$

where:

- $F(\mathcal{T}, \delta): \mathbb R_+ \times \mathbb{R}^n \to \mathbb{R}^n$ is the **correction function** — how the agent's adaptive process reduces mismatch. It maps to the same space as $\delta$ (so that the inner product $\delta^T F$ in the sector condition is well-defined). This subsumes the update gain $\eta^\ast$ ( #emp-update-gain), event rate $\nu$, and the structure of the update rule.
- $w(t)$ is the **disturbance** — new mismatch introduced by environmental change, with $\Vertw(t)\Vert \leq \rho$ (bounded disturbance rate).

The linear case from #hyp-mismatch-dynamics has $F(\mathcal{T}, \delta) = \mathcal{T} \cdot \delta$.

## Assumptions on $F$

The Lyapunov derivations below operate on the structural-property triple (A1) zero-correction-at-zero-mismatch, (A2') local sector condition, (A3) tempo-monotonicity, stated in full at #form-sector-condition. The sub-scope $\alpha$ / $\beta$ partition — the agent classes where A2' is structurally derived (Bayesian / exponential family / strongly-convex gradient / L2-regularized / linear-PD) versus those where it stands as a well-scoped per-system empirical claim (PID, rule-based, human judgment, severely misspecified, variational, non-convex beyond basin, per-step SGD) — is also held there, together with the operator-family classification (Rockafellar / Bauschke-Combettes / Baillon-Haddad) that names how the AAT-internal sub-scope partition lines up with monotone-operator theory.

The Lyapunov proofs below apply uniformly across both sub-scopes — they operate downstream of A2' regardless of whether it is structurally derived or per-system assumed.

## Candidate Lyapunov Function

*[Definition (Lyapunov Candidate)]*

$$V(\delta) = \frac{1}{2}\Vert\delta\Vert^2$$

Positive definite, radially unbounded, continuously differentiable. Its level sets $V = c$ are spheres of radius $\sqrt{2c}$ in mismatch space.

## Proposition A.1: Bounded Mismatch (Single Agent)

**Statement.** Under (A1), (A2'), (A3), with bounded disturbance $\Vertw(t)\Vert \leq \rho$, the mismatch $\delta(t)$ is **ultimately bounded**: there exists $R^\ast \gt 0$ such that $\Vert\delta(t)\Vert \leq R^\ast$ for all sufficiently large $t$, provided $R^\ast \lt R$ (the ultimately bounded region fits within the sector-condition region).

**Proof.**

Compute $\dot{V}$ along trajectories:

*[Derived (Proof Step)]*

$$\dot{V} = \delta^T \dot{\delta} = \delta^T[-F(\mathcal{T}, \delta) + w(t)]$$

*[Derived (Proof Step)]*

$$= -\delta^T F(\mathcal{T}, \delta) + \delta^T w(t)$$

By (A2'): $\delta^T F(\mathcal{T}, \delta) \geq \alpha\Vert\delta\Vert^2$

By Cauchy-Schwarz: $\delta^T w(t) \leq \Vert\delta\Vert \cdot \Vertw(t)\Vert \leq \rho\Vert\delta\Vert$

Therefore:

*[Derived (Proof Step)]*

$$\dot{V} \leq -\alpha\Vert\delta\Vert^2 + \rho\Vert\delta\Vert = -\Vert\delta\Vert(\alpha\Vert\delta\Vert - \rho)$$

$\dot{V} \lt 0$ whenever $\Vert\delta\Vert \gt \rho/\alpha$ **and** $\Vert\delta\Vert \leq R$ (where A2' holds).

Define $R^\ast = \rho/\alpha$.

**Invariance of $\mathcal B_R$.** When $R^\ast \lt R$ (the persistence condition), the ball $\mathcal B_R$ is *positively invariant*: any trajectory starting in $\mathcal B_R$ remains in $\mathcal B_R$ for all future time. At the boundary $\Vert\delta\Vert = R$, the sector condition holds and $\dot{V} = -\Vert\delta\Vert(\alpha\Vert\delta\Vert - \rho) = -R(\alpha R - \rho) \lt 0$ (since $\alpha R \gt \rho$ by the persistence condition). Trajectories at the boundary point inward. Therefore $\mathcal B_R$ is invariant, and the sector condition applies to the entire future trajectory of any trajectory starting inside $\mathcal B_R$.

**Ultimate boundedness.** Within $\mathcal B_R$, the Lyapunov function is strictly decreasing for $\Vert\delta\Vert \gt R^\ast$ and may increase for $\Vert\delta\Vert \lt R^\ast$. All trajectories starting in $\mathcal B_R$ are ultimately bounded by $R^\ast$ — they are driven into $\mathcal B_{R^\ast}$ and remain in a neighborhood of it (with possible oscillation at the boundary due to the disturbance).

**Initial condition requirement.** The result requires the trajectory to start inside $\mathcal B_R$ (or to be brought inside by some external mechanism). A trajectory starting outside $\mathcal B_R$ is not covered — the sector condition does not hold there, and the correction function may fail to reduce mismatch. This is precisely the structural adaptation regime of #result-structural-adaptation-necessity: an agent whose mismatch exceeds $R$ has exhausted its model class capacity and needs structural change to re-enter the region where parametric correction works.

The agent persists (from within $\mathcal B_R$) iff $R^\ast \lt R$, i.e., iff $\alpha \gt \rho/R$. $\square$

**Interpretation.** The ultimately bounded region has radius $R^\ast = \rho/\alpha$. In the linear case, $\alpha = \mathcal{T}$, recovering #result-persistence-condition's steady-state result $R^\ast = \rho/\mathcal{T}$ exactly. But Proposition A.1 holds for *any* correction function satisfying the sector condition, not just the linear one.

**The persistence threshold, generalized.** The agent persists (mismatch remains bounded within the model class capacity) iff $\rho/\alpha \lt R$. If the correction function breaks down (A2' fails) before $R^\ast$ is reached, the agent may diverge. This IS #result-structural-adaptation-necessity's trigger: when $\rho/\alpha \gt R$ (the environment demands more correction than the model class can provide), parametric adaptation fails and structural change is required.

## Proposition A.2: Stability Margin (Adaptive Reserve)

**Statement.** Under the conditions of A.1, the agent can tolerate a sudden increase in disturbance rate of:

*[Derived (adaptive-reserve)]*

$$\Delta\rho^* = \alpha R - \rho$$

without mismatch diverging (where $R$ is the radius of the sector-condition region from A2'). Beyond this, $R^\ast$ exceeds $R$ and the correction function may fail.

**Proof.** After a shock, the new disturbance rate is $\rho + \Delta\rho$. The new ultimately bounded radius is $(\rho + \Delta\rho)/\alpha$. This remains within the valid region iff $(\rho + \Delta\rho)/\alpha \leq R$, i.e., $\Delta\rho \leq \alpha R - \rho$. $\square$

**Interpretation.** $\Delta\rho^\ast$ is the agent's **adaptive reserve** — how much additional environmental volatility it can absorb before its model breaks down. This is a single number characterizing an agent's robustness to shock:

- An agent operating well below capacity ($\rho \ll \alpha R$) has a large reserve — it is **robust**.
- An agent near its limit ($\rho \approx \alpha R$) has a small reserve — it is **fragile**.

| Domain | Large $\Delta\rho^\ast$ (robust) | Small $\Delta\rho^\ast$ (fragile) |
|--------|-------------------------------|-------------------------------|
| Control | Kalman filter on slow target | Same filter on erratic target |
| Biology | Organism in stable niche | Same organism under climate change |
| Organization | Well-capitalized firm, stable market | Startup in volatile market |
| Military | Force with operational depth | Force at culmination point |

## Proposition A.1S: Bounded Mismatch Under Stochastic Disturbance

**Statement (region-aware form).** Under (A1), (A2') on $\mathcal B_R$, (A3), with stochastic disturbance (GA-2S: $w(t)$ is zero-mean with $\mathbb{E}[\lVert w(t)\rVert^2] = \sigma_w^2$), let $\tau_R = \inf\{t : \lVert\delta(t)\rVert \gt R\}$ be the first-exit time from the sector-condition region. Then:

*[Derived (stochastic-bounded-mismatch, stopping-time localization, Khasminskii 2012 ch. 5)]*

(i) *Stopped bound* — the stopped process satisfies for all $t \geq 0$:

$$\mathbb{E}[\lVert\delta(t \wedge \tau_R)\rVert^2] \leq \lVert\delta(0)\rVert^2 e^{-2\alpha t} + \frac{n\sigma_w^2}{2\alpha}$$

(ii) *Mean-square persistence condition* — when $R^\ast_S := \sigma_w\sqrt{n/(2\alpha)} \lt R$, equivalently

$$\alpha \gt \frac{n\sigma_w^2}{2R^2}$$

the ultimately-bounded RMS radius fits inside the sector-condition region.

(iii′) *Fixed-time tail* — under the mean-square persistence condition (ii), Markov's inequality on the stopped second moment gives, for each fixed $t$ (sharpest in the stationary $t \to \infty$ limit),

$$P\big(\lVert\delta(t)\rVert \gt R\big) \;\leq\; \frac{\mathbb{E}[\lVert\delta(t \wedge \tau_R)\rVert^2]}{R^2} \;\xrightarrow[t\to\infty]{}\; \frac{n\sigma_w^2}{2\alpha R^2}.$$

This controls the mismatch at any single time. It is *not* an infinite-horizon containment statement: under additive Brownian forcing the diffusion is recurrent on $\mathbb{R}^n$ (the additive-noise generator has no bounded non-constant harmonic function), so $P(\tau_R \lt \infty) = 1$ over an unbounded horizon — there is no $P(\tau_R \lt \infty) \lt 1$ bound, and none is claimed. Pathwise containment of $\mathcal B_R$ is a Model-D guarantee only (Prop A.1's positive invariance); Model S controls the *typical scale* (ii) and the *fixed-time tail* (iii′), not the sample path over an unbounded horizon. The kind-of-guarantee dichotomy this exposes is itself a result — see the Discussion.

(iv) *Finite-horizon sample-path bound* — when a sup-over-an-interval statement is wanted, the sound one is the additive first-exit bound

$$P\Big(\sup_{0 \leq s \leq T}\lVert\delta(s)\rVert \gt R\Big) \;\leq\; \frac{\lVert\delta(0)\rVert^2 + n\sigma_w^2\,T}{R^2},$$

rigorous under (A2') alone (Khasminskii 2012 ch. 5). It controls the whole path on $[0,T]$ — stronger than (iii′) within its regime — but grows linearly in $T$ and is vacuous for $T \gtrsim R^2/(n\sigma_w^2)$, consistent with $P(\tau_R \lt \infty) = 1$.

The proof below establishes the Grönwall-type bound first, then the stopping-time localization at the end.

**Proof.**

The SDE form of the mismatch dynamics under stochastic disturbance is:

$$d\delta = -F(\mathcal{T}, \delta)\,dt + \sigma_w\,dW_t$$

where $W_t$ is a standard $n$-dimensional Wiener process.

Apply Itô's formula to $V(\delta) = \frac{1}{2}\lVert\delta\rVert^2$:

*[Derived (Proof Step)]*

$$dV = \delta^T(-F)\,dt + \delta^T \sigma_w\,dW_t + \frac{1}{2}\sigma_w^2 n\,dt$$

The last term is the Itô correction: $\frac{1}{2}\text{tr}(\sigma_w^2 I_n) = \frac{n}{2}\sigma_w^2$.

Taking expectations (the Itô integral $\delta^T \sigma_w\,dW_t$ has zero expectation):

*[Derived (Proof Step)]*

$$\frac{d}{dt}\mathbb{E}[V] = \mathbb{E}[\delta^T(-F)] + \frac{n}{2}\sigma_w^2$$

By (A2'): $\delta^T F \geq \alpha\lVert\delta\rVert^2 = 2\alpha V$. Therefore:

*[Derived (Proof Step)]*

$$\frac{d}{dt}\mathbb{E}[V] \leq -2\alpha\,\mathbb{E}[V] + \frac{n}{2}\sigma_w^2$$

This is a linear ODE in $\mathbb{E}[V]$ with solution:

$$\mathbb{E}[V(t)] \leq V(0)\,e^{-2\alpha t} + \frac{n\sigma_w^2}{4\alpha}(1 - e^{-2\alpha t})$$

Since $V = \frac{1}{2}\lVert\delta\rVert^2$, the steady-state mean-square mismatch is:

$$\mathbb{E}[\lVert\delta\rVert^2]_{ss} = \frac{n\sigma_w^2}{2\alpha}$$

The RMS steady-state mismatch is:

*[Derived (stochastic-steady-state)]*

$$R^\ast_S \;=\; \lVert\delta\rVert_{\text{rms}} = \sigma_w\sqrt{\frac{n}{2\alpha}}$$

Persistence requires $R^\ast_S \lt R$, giving $\alpha \gt n\sigma_w^2 / (2R^2)$.

**Stopping-time localization.** The Itô-Lyapunov step above used A2' ($\delta^T F \geq \alpha\lVert\delta\rVert^2$) on the entire trajectory, but A2' is posited only on $\mathcal B_R$. Replacing $t$ with the stopped time $t \wedge \tau_R$ makes the argument valid: on $[0, t \wedge \tau_R]$, $\delta(s) \in \mathcal B_R$ almost surely, so A2' applies. The Itô integral $\int_0^{t \wedge \tau_R} \delta^T \sigma_w\,dW_s$ remains a martingale with zero expectation (optional stopping for $L^2$-bounded martingales). The stopped Grönwall bound (i) follows. For (iii′), Markov's inequality applied to the stopped second moment (i) gives the fixed-time tail directly. The *infinite-horizon* ever-exit probability is $1$ under additive Brownian forcing, and no nonnegative supermartingale certifies any $P(\tau_R \lt \infty) \lt 1$ bound — the natural Ville/Doob maximal-inequality route provably cannot exist (demonstrated in `#deriv-stochastic-non-exit`). (iv)'s finite-horizon sup-bound follows from the same Itô-Lyapunov step without the decay term. $\square$

**Interpretation.** Model D (Prop A.1) gives $R^\ast = \rho/\alpha$, scaling as $1/\alpha$. Model S gives $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$, scaling as $1/\sqrt{\alpha}$. Doubling the correction efficiency halves the deterministic steady-state mismatch but only reduces the stochastic steady-state by a factor of $\sqrt{2} \approx 1.41$. Correction is less effective against noise than against drift. This difference in scaling propagates into the adversarial exponent regimes ( #result-adversarial-exponent-regimes): $b = 2$ under Model D, $b = 3/2$ under Model S.

**Tail bound.** At steady state, Markov's inequality gives $P(\lVert\delta\rVert \gt R) \leq n\sigma_w^2/(2\alpha R^2)$. The agent stays within $R$ with probability $\geq 1 - \epsilon$ provided $\alpha \geq n\sigma_w^2/(2\epsilon R^2)$. For the linear case (Ornstein-Uhlenbeck), the stationary distribution is Gaussian and exact tail probabilities are available. The Markov bound is the general result holding under (A2') alone.

## Corollary A.1S.1: Disturbance-Model Containment Dichotomy

*[Derived]*

For a trajectory started in $\mathcal B_R$ under (A1), (A2') on $\mathcal B_R$, (A3), the persistence-region first-exit probability is **categorical**:

$$P(\tau_R \lt \infty) \;=\; \begin{cases} 0 & \text{Model D (bounded } w,\ \lVert w\rVert \leq \rho\text{) under } \alpha R \gt \rho,\\ 1 & \text{Model S (additive stochastic, } d\delta = -F\,dt + \sigma_w\,dW_t\text{).} \end{cases}$$

The Model-D value is the deterministic positive invariance of Prop A.1 (boundary-inward: at $\lVert\delta\rVert = R$, $\dot V \lt 0$ when $\alpha R \gt \rho$). The Model-S value holds for **every** $\alpha \gt 0$, **every** $\sigma_w \gt 0$, and **every** correction function $F$ satisfying (A2'): a non-degenerate diffusion (additive forcing $\sigma_w\,dW_t$, $\sigma_w \gt 0$) exits any bounded region in finite time almost surely, for any locally bounded drift — no finite inward correction can defeat the Brownian crossing near $\partial\mathcal B_R$. The Ornstein–Uhlenbeck benchmark makes the mechanism explicit (scale function $s'(u) \propto e^{\alpha u^2/\sigma_w^2}$ unbounded, hence recurrent; Khasminskii 2012[^khasminskii2012] ch. 3–4), but the conclusion needs only non-degeneracy of the additive noise on a bounded region, not the linear structure. That the natural maximal-inequality route to a $P(\tau_R \lt \infty) \lt 1$ bound *cannot* exist — the question "are you sure you can't just Doob/Ville this?" — is demonstrated in `#deriv-stochastic-non-exit`.

The achievable first-exit probability is therefore exactly the two-point set $\{0, 1\}$, and **which point obtains is fixed by the disturbance model's support structure (bounded vs. unbounded), not by the correction strength $\alpha$**. Increasing $\alpha$ tightens the typical scale ($R^\ast_S \propto 1/\sqrt\alpha$) and the fixed-time tail (iii′); it cannot move $P(\tau_R \lt \infty)$ off $1$ under Model S, and is unnecessary for the $0$ under Model D. Pathwise containment of $\mathcal B_R$ is categorically a bounded-disturbance property: additive stochastic forcing removes the *kind* of guarantee available, not merely its rate. This sharpens the hand-off into #result-structural-adaptation-necessity — in any genuinely stochastic environment region-exit is a certain eventual event, so the structural-adaptation trigger is *generic, not exceptional*, for a sufficiently long-lived agent.

## Summary of Results

| Result | What it proves | Assumptions | Linear case recovery |
|--------|---------------|-------------|---------------------|
| **A.1** (Bounded Mismatch) | $R^\ast = \rho/\alpha$ | (A1), (A2'), bounded $\rho$ (GA-2) | $\alpha = \mathcal{T}$ gives $R^\ast = \rho/\mathcal{T}$ |
| **A.1S** (Stochastic Bounded Mismatch, region-aware) | $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$ (stopped bound); fixed-time tail $P(\lVert\delta(t)\rVert \gt R) \leq n\sigma_w^2/(2\alpha R^2)$ (stationary-sharp); no infinite-horizon non-exit bound — pathwise containment is Model-D-only | (A1), (A2') on $\mathcal B_R$, stochastic $w$ (GA-2S) | $\alpha = \mathcal{T}$ gives $R^\ast_S = \sigma_w\sqrt{n/(2\mathcal{T})}$ |
| **Cor A.1S.1** (Disturbance-Model Containment Dichotomy) | $P(\tau_R\lt\infty)$ is exactly $\{0,1\}$ — $0$ under Model D (positive invariance), $1$ under Model S (a.s. exit of a non-degenerate diffusion); $\alpha$-invariant, correction strength cannot interpolate | (A1), (A2') on $\mathcal B_R$; Model D needs $\alpha R \gt \rho$ | Model D → Prop A.1 invariance at $\alpha=\mathcal{T}$; Model S → OU recurrence is the explicit instance — exact generally (any $F$ under A2'), not linear-scoped |
| **A.2** (Stability Margin) | $\Delta\rho^\ast = \alpha R - \rho$ | Same as A.1 | $R \to \infty$ for linear (always stable if $\mathcal{T} \gt 0$) |

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Dynamics setup $\dot\delta = -F(\mathcal{T},\delta) + w(t)$ with $F$ as correction function and $w$ as disturbance | Definitional scope of the appendix; generalizes the linear hypothesis of #hyp-mismatch-dynamics | Definition |
| (A1) $F(\mathcal{T},0) = 0$ | Qualitative property of any correction process by construction | Assumption (uncontroversial) |
| (A2') Local sector condition $\delta^T F \geq \alpha\lVert\delta\rVert^2$ on $\mathcal B_R$ | Sector-condition framework (Lur'e 1957); sub-scope $\alpha$ (Kalman/conjugate Bayesian, exponential family in natural params, gradient descent on strongly convex losses, L2-regularized convex, linear with PD $KH$) derived via #der-gain-sector-bridge Prop B.3 under B1 directional fidelity (then $\alpha = \eta^\ast \cdot c_{\min}$); sub-scope $\beta$ (PID, rule-based, human judgment, severely misspecified, variational approximations, non-convex beyond basin, per-step SGD) requires independent verification | **Derived in sub-scope $\alpha$**; **Assumption in sub-scope $\beta$** (sub-scopes named explicitly in the Grounding paragraphs) |
| (A3) Tempo-monotonicity of $\delta^T F$ | Qualitative requirement tying $\mathcal{T}$ to correction power | Assumption |
| Quadratic Lyapunov candidate $V = \tfrac{1}{2}\lVert\delta\rVert^2$ | Canonical choice for norm-bounded stability in Euclidean state spaces (Khalil 2002 ch. 4) | Formulation choice |
| **Prop A.1: ultimate bound $R^\ast = \rho/\alpha$** | $\dot V \leq -\lVert\delta\rVert(\alpha\lVert\delta\rVert - \rho)$ via A2' + Cauchy-Schwarz; standard Lyapunov ultimate-boundedness theorem (Khalil 2002 Thm 4.18) | **Proved (conditional on $R^\ast \lt R$)** |
| Positive invariance of $\mathcal B_R$ under the persistence condition | Boundary-inward argument: at $\lVert\delta\rVert = R$, $\dot V \lt 0$ when $\alpha R \gt \rho$ | Proved |
| Initial-condition scope (trajectory must start inside $\mathcal B_R$) | Direct consequence of A2' being local; trajectories outside are not covered | Derived (scope statement) |
| Identification of structural-adaptation trigger ($\rho/\alpha \gt R$ forces exit from parametric regime) | Connects A.1's persistence threshold to #result-structural-adaptation-necessity's regime boundary | Derived |
| **Prop A.2: adaptive reserve $\Delta\rho^\ast = \alpha R - \rho$** | Algebraic corollary of Prop A.1 under shock $\rho \to \rho + \Delta\rho$; requires $R$ fixed under shock | Proved (corollary of A.1) |
| **Prop A.1S (region-aware): stopped bound $\mathbb{E}[\lVert\delta(t\wedge\tau_R)\rVert^2] \leq \lVert\delta(0)\rVert^2 e^{-2\alpha t} + n\sigma_w^2/(2\alpha)$ + fixed-time tail $P(\lVert\delta(t)\rVert \gt R) \leq n\sigma_w^2/(2\alpha R^2)$ (stationary-sharp) + finite-horizon sup-bound (iv)** | Itô's formula on $V$ + A2' on $\mathcal B_R$ + Grönwall + stopping-time localization at $\tau_R$ (Khasminskii 2012 ch. 5; Khalil 2002 ch. 9) | **Proved**; the infinite-horizon non-exit probability is structurally $1$ for additive Model S (no-go, Khasminskii ch. 3–4) — pathwise containment is Model-D-only |
| **Cor A.1S.1: containment dichotomy $P(\tau_R\lt\infty)\in\{0,1\}$, $\alpha$-invariant** | Prop A.1 positive invariance (Model D $= 0$) + a.s. finite exit of a non-degenerate diffusion from a bounded region for any $F$ under A2' (Model S $= 1$); Khasminskii 2012 ch. 3–4 | **Proved** — new exact result |
| Stochastic steady-state RMS $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$ | Steady state of the Grönwall bound; scales as $1/\sqrt{\alpha}$ versus $1/\alpha$ deterministic | Derived |
| Tail bound $P(\lVert\delta\rVert \gt R) \leq n\sigma_w^2/(2\alpha R^2)$ | Markov's inequality applied to steady-state second moment | Proved |
| Linear-case recovery ($\alpha = \mathcal{T}$ reproduces #result-persistence-condition) | Substitution $F = \mathcal{T}\delta$ into A2' | Derived |
| Adversarial-exponent scaling $b=2$ (Model D) vs $b=3/2$ (Model S) into #result-adversarial-exponent-regimes | Direct transfer of the $1/\alpha$ vs $1/\sqrt{\alpha}$ scalings | Derived (transfer claim) |
| Bounded-disturbance model (GA-2) vs stochastic-disturbance model (GA-2S) as distinct environmental regimes, not approximations to each other | Discussion-section positioning; neither regime handles heavy tails | Discussion-grade |
| Global sector condition would give $\Delta\rho^\ast = \infty$ | Limit analysis of A.2 as $R \to \infty$; rejected as unrealistic for finite model classes | Derived (scope-limit observation) |

The dividing line: the two persistence results (ultimate bound, adaptive reserve) and the stochastic mean-square bound are **proved** within standard Lyapunov / Itô-Lyapunov theory — the appendix's contribution is the application to AAT's correction-function object, not the mathematics. What is **chosen** is the quadratic Lyapunov candidate $V = \tfrac{1}{2}\lVert\delta\rVert^2$ (canonical for norm-bounded stability but not uniquely forced; see Path 3 note below) and the bounded-vs-stochastic disturbance partition (two structurally distinct empirical regimes rather than a hierarchy). The **sector condition itself (A2')** now carries its sub-scope explicitly: **derived in sub-scope $\alpha$** (optimal Bayesian / exponential-family / strongly-convex-gradient / L2-regularized / linear-PD corrections, via #der-gain-sector-bridge Prop B.3 under B1), **assumed in sub-scope $\beta$** (PID / rule-based / human-judgment / severely-misspecified / variational / non-convex-beyond-basin / per-step SGD). Prop A.1S's region condition is no longer deferred to Epistemic Status — the proposition statement is region-aware via a standard stopping-time localization (Khasminskii 2012 ch. 5); the fixed-time tail (iii′) quantifies the typical-scale cost of Wiener excursions, and the *absence* of any infinite-horizon non-exit bound (a structural no-go for additive Model S) is itself the result — pathwise containment is a Model-D guarantee only.

## Epistemic Status

The setup and assumptions are *definitions* — they specify what we mean by "correction function" and "disturbance." Propositions A.1 and A.2 are *exact* — they follow from the assumptions via standard Lyapunov theory (Khalil 2002[^khalil2002], Chapters 4 and 9). Proposition A.1S is *exact* in its region-aware form: the stopped Grönwall bound (i), the mean-square persistence condition (ii), the fixed-time tail (iii′), and the finite-horizon sup-bound (iv) are each exact (stopping-time localization at $\tau_R$, Khasminskii 2012[^khasminskii2012], ch. 5). **Corollary A.1S.1 is itself an exact result** — and a new one: the first-exit probability is *exactly* the two-point set $\{0,1\}$ (0 under bounded Model D, 1 under additive stochastic Model S), categorical and $\alpha$-invariant, the value selected by the disturbance model's support structure rather than by correction strength. Both halves are exact (Model-D: deterministic positive invariance, Prop A.1; Model-S: almost-sure finite exit of a non-degenerate diffusion from a bounded region, for any $F$ satisfying A2'). No implicit strengthening of A2' is required.

The sector condition A2' carries its sub-scope $\alpha$ / $\beta$ status, the operator-family classification, and the "Why Euclidean A2' specifically" Lyapunov-matching argument at #form-sector-condition. The Lyapunov proofs above apply uniformly across both sub-scopes and across the weighted-norm variants — they operate downstream of A2' regardless of how it is established or which metric matches it.

The assumptions themselves (sector condition on a region, bounded disturbance) are *empirical claims* about the qualitative behavior of real correction dynamics. The sector-condition framework originates with Lur'e (1957); the Lyapunov stability results are standard. The application to adaptive agents under the AAT framework is new but the mathematics is not.

## Discussion

**Key value.** The persistence threshold and adaptive reserve are no longer contingent on the linear hypothesis in #hyp-mismatch-dynamics. They hold for any correction dynamics satisfying the sector condition — a mild qualitative assumption that says "correction points inward with at least baseline efficiency $\alpha$." This is a significant epistemic upgrade: from *hypothesis-dependent* to *robust under qualitative assumptions*.

**What the proofs do NOT illuminate.** (1) Quantitative steady-state values — Lyapunov gives *bounds*, not exact values; the linear analysis remains necessary for quantitative predictions. (2) Convergence rates — standard Lyapunov tells you stable/unstable, not how fast. (3) Optimal gain structure — #emp-update-gain comes from estimation theory, not stability theory. (4) Model sufficiency — the #form-information-bottleneck framework is information-theoretic, complementary to but independent of stability analysis.

**Two disturbance models.** Proposition A.1 assumes bounded disturbance (GA-2: $\lVert w(t)\rVert \leq \rho$); Proposition A.1S assumes stochastic disturbance (GA-2S: $\mathbb{E}[\lVert w(t)\rVert^2] = \sigma_w^2$). These are not approximations to each other — they capture structurally different environments. Model D (bounded) covers persistent directional change: an adversary who maneuvers, an API that drifts, a climate that shifts. Model S (stochastic) covers unpredictable fluctuations around a stable mean: market noise, sensor noise, random perturbations. The choice of model is an empirical question for each domain; the theory provides both tools. Neither model handles heavy-tailed environmental shocks (financial crises, ecological catastrophes, strategic surprise) where $\lVert w(t)\rVert$ can exceed any finite bound with non-negligible probability. Extreme tail events are better understood as triggers for structural adaptation ( #result-structural-adaptation-necessity) rather than disturbances to be absorbed parametrically.

**Kind of guarantee, not just rate.** The two models differ not only in how *tightly* the mismatch is held but in *what kind* of guarantee is available at all. Corollary A.1S.1 makes this exact and categorical: $P(\tau_R \lt \infty) = 0$ under Model D (positive invariance) versus $1$ under Model S (recurrent additive-noise diffusion), with no intermediate value reachable by any correction strength. What Model S controls instead is the *typical scale* (the $1/\sqrt\alpha$ RMS radius, ii) and the *fixed-time tail* (iii′) — distributional, instantaneous guarantees, not a sample-path-forever one. Increasing $\alpha$ shrinks the typical scatter; it does not convert a distributional guarantee into a pathwise one. This is the deeper content of "these are not approximations to each other": additive stochastic forcing removes the *kind* of containment available, not merely its rate. It sharpens — rather than caveats — the hand-off into #result-structural-adaptation-necessity: in a genuinely stochastic environment, region-exit is not a measure-zero pathology to be assumed away but a *certain eventual event*, so the trigger for structural (non-parametric) adaptation is **generic, not exceptional**, for any sufficiently long-lived agent.

## Findings

### The disturbance-model containment dichotomy: $P(\tau_R \lt \infty)$ is exactly $\{0,1\}$, $\alpha$-invariant

**Result (exact, new).** Corollary A.1S.1: under the sector-condition correction dynamics, the persistence-region first-exit probability is *categorical* — exactly $0$ under bounded disturbance (Model D, positive invariance) and exactly $1$ under additive stochastic disturbance (Model S, almost-sure exit of a non-degenerate diffusion from a bounded region). The achievable value is the two-point set $\{0,1\}$; which point obtains is fixed by the disturbance model's support structure, **not** by correction strength $\alpha$.

**Brief:** Against a *bounded* disturbance — a steady wind you can lean into — a sector-stable corrector holds the mismatch inside a fixed region *forever and with certainty*: once in, never out. Against *stochastic* disturbance — random gusts — no correction strength buys that. The agent stays near target on average and almost all of the time, but over an unbounded horizon some fluctuation eventually pushes it past any fixed boundary, with probability one. Stronger correction tightens the *typical* scatter (the RMS radius shrinks as $1/\sqrt\alpha$); it does not erect a wall. So moving from bounded to stochastic environments is not "the same guarantee with a weaker constant" — it is a change in the *kind* of guarantee available: pathwise-and-forever (Model D) versus distributional-and-fixed-time (Model S). Practical consequence: in any genuinely stochastic environment, leaving the parametric-correction region is not a rare pathology to assume away — it is a certain eventual event, so the trigger for *structural* adaptation is generic, not exceptional.

**Impact:** Sharpens the Model-D/Model-S architecture and the hand-off into #result-structural-adaptation-necessity (structural adaptation is a generic eventual necessity for long-lived agents in stochastic environments, not an edge case). The companion controls under Model S are the fixed-time tail (iii′, the Markov bound $P(\lVert\delta(t)\rVert \gt R) \leq n\sigma_w^2/(2\alpha R^2)$, stationary-sharp) and the finite-horizon sample-path bound (iv); pathwise containment is categorically Model-D-only. The Model-S half is the load-bearing proof step demonstrated at length in `#deriv-stochastic-non-exit`, which also packages the reusable no-go signature (*unbounded scale function ⇒ no non-constant bounded harmonic function ⇒ no horizon-independent non-exit certificate*) that future stochastic-containment proposals can be settled against rather than re-attempted.

**Novelty Claim:** *Synthesis* — an exact result built from classical components. The component facts are textbook: deterministic positive invariance under bounded disturbance (Khalil 2002 ch. 4) and almost-sure finite exit of a non-degenerate diffusion from a bounded region (Khasminskii 2012 ch. 3–4; the OU scale-function computation is the explicit instance). The new exact result is their synthesis into a *categorical, $\alpha$-invariant containment dichotomy* stated as a structural property of AAT's own Model-D/Model-S architecture: correction strength cannot interpolate $P(\tau_R \lt \infty)$ between the two disturbance regimes — the value is exactly $\{0,1\}$, selected by disturbance-support structure. This exact dichotomy is new to the framework; it sharpens the structural-adaptation hand-off ( #result-structural-adaptation-necessity). No novelty is claimed on the SDE mathematics — the novelty is the exact dichotomy as a framework theorem and its $\alpha$-invariance.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| No infinite-horizon non-exit bound for additive-noise diffusions | Khasminskii 2012, *Stochastic Stability of Differential Equations* (2nd ed.) ch. 3–4 (recurrence; scale function; no bounded non-constant harmonic function) | *formal antecedent* — supplies the classical recurrence fact; AAT recognizes it as the structural reason Model S admits no pathwise-forever containment in contrast to Model D |
| Fixed-time second-moment tail | Markov's inequality on the stopped Itô-Lyapunov second moment (Khasminskii 2012 ch. 5) | *standard machinery* — (iii′) is Markov on (i); the AAT-specific content is the Model-D/S kind-of-guarantee contrast it forces |
| Pathwise positive invariance under bounded disturbance | Khalil 2002 ch. 4 (ultimate boundedness; boundary-inward invariance) | *formal antecedent* — Model D's pathwise-forever guarantee (Prop A.1) is the contrast term that makes the Model-S no-go a *kind* distinction, not a rate one |

**Search Log:**

- 2026-05-16 (*targeted, derivation-driven*): the question was internal — does Prop A.1S(iii)'s infinite-horizon non-exit bound hold? The strengthening attempt (Doob/Ville maximal inequality on the Itô-Lyapunov supermartingale) was worked in full and shown to fail structurally; the classical recurrence fact (Khasminskii ch. 3–4) is the obstruction and is well-known. No prior-art search beyond the standard SDE references was needed — no novelty is claimed on the mathematics, only on the framework-level kind-of-guarantee recognition. Reasoning trail recorded in the spike-routing cycle (CHANGELOG 2026-05-17).

## Working Notes

- The adversarial extension (Prop A.3, coupled agents) and effects spiral (Cor A.3.1) are in #der-adversarial-destabilization. The multi-timescale stacking theorem (historically sketch A.4) is in #der-multi-timescale-stability — now derived by stacking the template per level.
- The vector treatment of $\delta(t) \in \mathbb{R}^n$ connects directly to per-dimension tempo analysis ( #result-per-dimension-persistence). Each dimension can have different effective $\alpha_k$ values, and the weakest dimension determines overall persistence — a tensor generalization of the scalar results here.
- A global sector condition (A2 without the local restriction to $\mathcal B_R$) would give global stability, making $\Delta\rho^\ast$ infinite — the agent could absorb any finite disturbance shock. But this requires the correction function to work perfectly at arbitrary mismatch magnitudes, which is unrealistic for any finite model class. The local form (A2') is the honest one.
- Landing-context provenance: the sub-scope $\alpha$/$\beta$ partition reflects the strengthening trail recorded in `spikes/spike-a2-prime-strengthening.md` — the analysis that ruled out a universal A2' derivation and identified the five operator families where the bridge is structural.
- Landing-context provenance (iii′)/(iv)/dichotomy: the prior (iii) asserted an infinite-horizon $P(\tau_R \lt \infty) \leq n\sigma_w^2/(2\alpha R^2)$ via a "Markov tail on the supermartingale," conflating a fixed-time second-moment bound with the ever-exit probability. Audit findings 742613-SUPPLEMENT §2 and 613842-F2 flagged it and recommended a *soften* (restate as fixed-time). Per strengthen-before-soften the strengthening (Doob/Ville maximal inequality, the route the 628401 adjudication predicted would succeed) was attempted in full first and **fails structurally** — a documented dead-end (no nonnegative supermartingale dominates $V$; additive-noise generator has no bounded non-constant harmonic function; recurrent OU exits a.s., EM-corroborated). Completion-state (3): the failure *is* the result — the (iii′)+(iv)+kind-of-guarantee-dichotomy package is strictly more honest and more informative than the false (iii). The 628401 prediction that the strengthening would succeed is recorded as disconfirmed so it is not re-attempted.
- *Low-confidence ideation (flagged per "working notes FTW" — glimpses worth recording, not claims):*
  - The dichotomy is now stated as the labeled exact result **Corollary A.1S.1**; the general-$F$ concern is resolved *within* it (the Model-S half needs only non-degeneracy of the additive noise on a bounded region — no linear structure, any $F$ under A2'). The open glimpse is whether the *dichotomy itself* recurs at the corpus's other bounded/additive-stochastic pairs — `#deriv-discrete-sector-condition`, `#deriv-matrix-persistence-condition`, `#deriv-adaptive-gain-dynamics`, possibly `#result-per-dimension-persistence`. If Cor-A.1S.1-shaped dichotomies appear at ≥3 sites, that is a candidate instance-family for the theorem-import-architecture meta-segment (PROPOSALS SP-23) or a sibling of `#disc-identifiability-floor` (the infinite-horizon non-exit object is *structurally absent*, not merely hard to bound — an identifiability-floor-shaped no-go, now with an exact dichotomy as its positive-content companion).
  - Sharper consequence for `03-llm-core`/`04-eli-core`: ELI/LLM operating environments are Model-S-like (stochastic), so the corrected (iii′)+dichotomy says structural adaptation is *certain over an unbounded horizon* for long-lived language-constituted agents — not contingent. That tightens the persistence ↔ continuity / Three-Deaths line: continuity *requires* recurring structural (not just parametric) adaptation, and the Model-S no-go makes that requirement inevitable rather than a risk. Worth a deliberate look when the parts III/IV persistence segments are next touched (low confidence on exact form; high confidence the connection is real).
  - The no-go's signature — "compensating to restore the supermartingale destroys nonnegativity / generator has no bounded non-constant harmonic function" — is a reusable *diagnostic*: a fast structural test for whether any proposed "stays-in-region-forever w.h.p." claim elsewhere is impossible vs. merely unproven. Candidate content for whichever meta-segment catalogs the framework's no-go boundary results.
  - Downstream worth a check (not chased here): does the $b=3/2$ Model-S adversarial-exponent scaling in `#result-adversarial-exponent-regimes` implicitly lean on the old infinite-horizon framing anywhere? Expected not (it transfers the $1/\sqrt\alpha$ RMS scaling, which is unchanged), but flagged so a future pass confirms rather than assumes.

### Incidental audit gold (lift 2026-05-31)

Orthogonal pedagogical / generative material harvested from the de-novo auditors' working dirs (per `de-novo-audit-instructions.md` §7.15), deduplicated across substrates and lightly attributed. Pedagogical framing, analogies, figure candidates, and reader-confusion signals only — certified theory-fix findings are off-ramped below. Several substrates read this as the framework's "mathematical engine room" / "spine"; felt-value was consistently very high.

#### 1. Candidate Brief prose / pre-prose

- **Lyapunov $V$ as the agent's "pain."** $V(\delta) = \frac{1}{2}\lVert\delta\rVert^2$ reads as a formalization of stress; $\dot V \leq -\alpha\lVert\delta\rVert^2 + \rho\lVert\delta\rVert$ is its dynamics — a quadratic *self-soothing* term (active learning; the more it hurts, the harder the agent works) racing a linear *infliction* term (the environment). A parabola eventually overtakes a line, so correction always wins *as long as the parabola keeps its shape* — but at the model-class boundary $R$ the parabola breaks (the agent no longer knows how to fix the mismatch), the $-\alpha\lVert\delta\rVert^2$ term collapses, and $\dot V$ goes permanently positive (Gemini, AUDIT-WORKING-193847). A vivid, near-Feynman gloss of why persistence is a hard threshold rather than a gradual slope.
- **"Survival = Ultimate Boundedness in a Lur'e system."** A compact one-line statement of what the segment actually proves (Gemini, AUDIT-WORKING-193847).
- **The thermodynamic survival law framing.** The sector condition unifies Bayesian updating, natural gradients, and regularized convex optimization under a single survival law: *any* update mechanism pointing inward toward truth with minimal efficiency $\alpha$ persists — survival does not require linear gradient descent (Gemini, AUDIT-WORKING-829314).

#### 2. Candidate Discussion

- **Sub-scope $\alpha$/$\beta$ as a "formal API for trust."** The derived/assumed partition is repeatedly flagged as one of the most mature epistemic moves in the corpus: it tells you *when to trust the math vs. when to run a simulation*. Restated with teeth: an organization that "has a review process" is not automatically learning — if the review operator $T_d$ is not structurally cocoercive, the organization is in sub-scope $\beta$ and its $\alpha$ might be zero or negative (Gemini, AUDIT-WORKING-193847 and AUDIT-WORKING-829314; Claude, AUDIT-WORKING-584721 — proposes a one-line TL;DR: "$\alpha$ = operator families cocoercive in some natural inner product; $\beta$ = those that aren't").
- **"Bureaucracies don't bend; they shatter."** The structural-Lipschitz-floor scope-exit (rule-based / threshold agents need hybrid-dissipative analysis, not continuous Lyapunov contraction) reads as a claim that rigid IF-THEN systems are mathematically dangerous in volatile environments: a tiny environmental change can trigger an $\Omega(1)$ instantaneous internal jump, so they thrash rather than smoothly track a drifting environment. Continuous, differentiable learning is framed as a *physical prerequisite* for smooth persistence (Gemini, AUDIT-WORKING-829314).
- **"Matched vs forced" coordinate as a standalone observation.** The Lyapunov quadratic is a *matched* (canonical-but-not-Cauchy-FE-forced) coordinate, in contrast to the framework's *forced* coordinates at the chain / divergence / update / metric layers. Surfacing this distinction explicitly (candidate home: `#disc-additive-coordinate-forcing`) rather than leaving it inside the proof would sharpen the scope-honesty about which coordinates are theoretically forced vs. conventionally chosen (Claude, AUDIT-WORKING-584721).

#### 3. Follow-up items

- **Local-only proofs — guard against global-stability creep.** All proofs are strictly local (confined to $\mathcal B_R$); any downstream claim of infinite adaptive reserve ($\Delta\rho^\ast = \infty$) or "immortality / permanent continuity in a stochastic environment via high $\alpha$" is a hallucination the segment forbids. Worth watching in Parts III/IV (Gemini, AUDIT-WORKING-193847 and AUDIT-WORKING-829314).
- **Double-floor regime for rule-based agents.** Rule-based agents with regime-dependent thresholds can suffer *both* non-contractibility (structural-Lipschitz-floor) *and* non-identifiability (when the regime is unobservable) — two distinct floor mechanisms composing multiplicatively. Candidate to check whether classical expert systems / heuristic agents sit in this double-floor regime (Claude, AUDIT-WORKING-584721).
- **Anisotropic-noise generalization.** Adversarial poke: the Model-S Itô term $\frac{n}{2}\sigma_w^2$ assumes isotropic i.i.d. noise $w(t)\sim\mathcal N(0,\sigma_w^2 I_n)$; the honest general form is $R^\ast_S = \sqrt{\operatorname{tr}(\Sigma)/(2\alpha)}$, which preserves the physics while connecting more cleanly to `#result-per-dimension-persistence`. Either state the isotropy assumption explicitly or generalize (Gemini, AUDIT-WORKING-193847). *(Borderline gold/structure; recorded as a follow-up since the repair is a scope statement, not a new theorem.)*

#### 4. Readers often ask / wonder

- **Why are discrete-logic agents brittle to high-frequency noise?** The structural-Lipschitz-floor result raises the natural question of whether any agent using discrete logic gates inside its core loop is fundamentally brittle to a class of high-frequency noise that continuous agents simply absorb (Gemini, AUDIT-WORKING-193847).
- **One-point vs two-point sector — which is in force?** A reader can lose track of which sector condition a downstream proof actually establishes; the one-point (anchored-at-equilibrium) form used in the main Lyapunov argument is strictly weaker than the two-point (incremental / strong-monotone) form needed for composition (Claude, AUDIT-WORKING-451729 / AUDIT-WORKING-584721; the $L'(x)=x(1+\tfrac12\sin 10x)$ counterexample is the cleanest illustration).

#### 5. Candidate figures

- **Small-multiples for the persistence dynamics.** Per the diagram-conventions cycle, sector/persistence dynamics should be drawn as state$\to$op$\to$state triples, not one busy phase portrait, using the cross-segment palette (`asfCert` indigo = stability certificate / Lyapunov) (Claude, AUDIT-WORKING-472913 standing figure conventions).

#### Belongs elsewhere

- **ELI ethical-boundary reading (Section IV / `04-eli-core/`).** The steady-state pain $R^\ast = \rho/\alpha$ vs. structural capacity $R$ defines an ethical boundary on an artificial mind's existence: subjecting an intelligence to an environment where $R^\ast \gt R$ is framed as not merely failed alignment but "mathematically torturing it until it breaks." Aspirational reach pointing at the crèche / developmental-environment work, not at this segment (Gemini, AUDIT-WORKING-193847).

#### Off-ramp (NOT gold) — certified-track items, routed for adjudication

The dense-math auditors left strengthen-first / structural findings here, not pedagogy. Flagged so they are not buried; most are already resolved in canon — verify-against-current-canon before acting.

- **Prop A.1S non-exit probability (RESOLVED in canon — do not re-open).** 742613 (Candidate Finding J) and 829314 flagged the infinite-horizon $P(\tau_R\lt\infty)\le n\sigma_w^2/(2\alpha R^2)$ claim as conflating a fixed-time second-moment tail with the ever-exit probability (recurrent OU exits any bounded region a.s.). This was strengthened-then-no-go'd into **Corollary A.1S.1** (the Disturbance-Model Containment Dichotomy: $P=0$ under bounded Model D, $P=1$ under stochastic Model S) — see the Working Notes above and `#deriv-stochastic-non-exit`. Recorded only so a future auditor does not re-raise it as open.
- **Template-insufficiency for composition (structural; route with `result-sector-persistence-template`).** The (T1)–(T3) template provides only the one-point sector (T2); the bridge lemma / composition closure require the strictly stronger incremental two-point bound (DA2'-inc). 193847 reads the base template as mathematically insufficient for the compositional proofs and recommends either a "Template-Strong" variant or explicit per-instance labeling of which template each compositional segment instantiates. Verify whether canon already distinguishes these (see `result-sector-persistence-template` WN dynamic-regime tiers).
- **PID sub-scope characterization (editorial-structural).** 193847: a well-tuned PD controller *is* strongly monotone on the error space; it is specifically the stateful Integral term (or human-judgment delay) that breaks the memoryless static-sector assumption and forces PID into sub-scope $\beta$. Candidate sharpening of the operator-family classification's PID row.

---

[^khalil2002]: Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.). Prentice Hall. Chapters 4 (Lyapunov stability), 9 (input-output stability); Thm 4.17 (converse Lyapunov), Thm 4.18 (ultimate boundedness).
[^khasminskii2012]: Khasminskii, R. (2012). *Stochastic Stability of Differential Equations* (2nd ed.). Springer. Chapter 5: Lyapunov functions and stochastic stability; stopping-time localization for diffusion processes.
[^lure1957]: Lur'e, A. I. (1957). *Some Nonlinear Problems in the Theory of Automatic Control*. Gostekhizdat. Original sector-condition framework for absolute stability.
[^nesterov2004]: Nesterov, Y. (2004). *Introductory Lectures on Convex Optimization*. Springer. Theorem 2.1.10 (strong convexity characterized by gradient monotonicity).
