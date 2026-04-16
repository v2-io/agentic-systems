---
slug: sector-condition-derivation
type: derivation
status: exact
depends:
  - adaptive-tempo
  - mismatch-signal
stage: claims-verified
---

# Derivation: Sector Condition Stability — Lyapunov Derivation

Complete Lyapunov derivations of bounded mismatch and adaptive reserve for the sector-condition results stated in #sector-condition-stability.

## Motivation

#mismatch-dynamics hypothesizes the linear ODE $d\Vert\delta\Vert/dt = -\mathcal{T}\Vert\delta\Vert + \rho$ as a first-order approximation. The linear form yields clean closed-form results but commits to a specific functional relationship between mismatch magnitude and correction rate. True correction dynamics are almost certainly nonlinear — exhibiting saturation at large mismatch, threshold effects near zero, and structural breakdown when the model class is exhausted.

A Lyapunov approach proves persistence and stability under much weaker assumptions: any correction dynamics satisfying qualitative monotonicity properties (the sector condition). The results below are strictly more general — the linear case is recovered where the sector bounds coincide.

## Setup

Let $\delta(t) \in \mathbb{R}^n$ be the mismatch vector — the difference between the model's predictions and reality across $n$ observable dimensions. The vector treatment connects to per-dimension tempo analysis ( #per-dimension-persistence).

The mismatch dynamics are:

*[Definition (Dynamics Setup)]*

$$\frac{d\delta}{dt} = -F(\mathcal{T}, \delta) + w(t)$$

where:

- $F(\mathcal{T}, \delta): \mathbb R_+ \times \mathbb{R}^n \to \mathbb{R}^n$ is the **correction function** — how the agent's adaptive process reduces mismatch. It maps to the same space as $\delta$ (so that the inner product $\delta^T F$ in the sector condition is well-defined). This subsumes the update gain $\eta^\ast$ ( #update-gain), event rate $\nu$, and the structure of the update rule.
- $w(t)$ is the **disturbance** — new mismatch introduced by environmental change, with $\Vertw(t)\Vert \leq \rho$ (bounded disturbance rate).

The linear case from #mismatch-dynamics has $F(\mathcal{T}, \delta) = \mathcal{T} \cdot \delta$.

## Assumptions on $F$

We require only qualitative properties, not a specific functional form:

### (A1) Zero Correction at Zero Mismatch

*[Assumption A1]*

$$F(\mathcal{T}, 0) = 0$$

No correction is applied when the model perfectly matches reality.

### (A2') Local Sector Condition

There exists a region $\mathcal B_R = \{\delta : \Vert\delta\Vert \leq R\}$ and $\alpha \gt 0$ such that (following the sector-condition framework of Lur'e[^lure1957]):

*[Assumption A2' (sector-condition)]*

$$\delta^T F(\mathcal{T}, \delta) \geq \alpha \Vert\delta\Vert^2 \quad \forall \delta \in \mathcal{B}_R$$

The correction function always points "inward" (reducing mismatch), and its magnitude is bounded below relative to $\Vert\delta\Vert^2$. The linear case has $\alpha = \mathcal{T}$. A saturating correction has $\alpha$ decreasing for large $\Vert\delta\Vert$. A threshold correction has $\alpha = 0$ for small $\Vert\delta\Vert$.

The local form allows the correction to break down outside $\mathcal B_R$ — the structural adaptation regime of #structural-adaptation-necessity.

**Grounding of GA-3.** The sector condition (A2') is not an irreducible assumption for well-designed agents. #gain-sector-bridge shows that gain-based updating ( #update-gain) with directional fidelity produces correction functions satisfying A2', with $\alpha = \eta^\ast \cdot c_{\min}$. For gradient-based agents, A2' is equivalent to local strong convexity of the loss function, with $\alpha = \eta \cdot \mu$ where $\mu$ is the strong convexity modulus. The Lyapunov proofs below are unchanged — they operate downstream of A2' regardless of whether it is assumed or derived.

### (A3) Tempo Monotonicity

For fixed $\delta$, $\delta^T F(\mathcal{T}, \delta)$ is monotone increasing in $\mathcal{T}$. Higher tempo means faster correction.

**Connection to ACT parameters.** The sector parameter $\alpha$ is determined by the adaptive tempo $\mathcal{T}$ ( #adaptive-tempo) and the structure of the correction function. In the linear case, $\alpha = \mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$. In nonlinear cases, $\alpha$ represents the *worst-case* correction efficiency within the valid region — the minimum ratio of correction power to mismatch magnitude. The radius $R$ represents the model class capacity: how large a mismatch can grow before the correction mechanism fails (i.e., before the sector condition ceases to hold), at which point structural adaptation ( #structural-adaptation-necessity) becomes necessary.

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

**Initial condition requirement.** The result requires the trajectory to start inside $\mathcal B_R$ (or to be brought inside by some external mechanism). A trajectory starting outside $\mathcal B_R$ is not covered — the sector condition does not hold there, and the correction function may fail to reduce mismatch. This is precisely the structural adaptation regime of #structural-adaptation-necessity: an agent whose mismatch exceeds $R$ has exhausted its model class capacity and needs structural change to re-enter the region where parametric correction works.

The agent persists (from within $\mathcal B_R$) iff $R^\ast \lt R$, i.e., iff $\alpha \gt \rho/R$. $\square$

**Interpretation.** The ultimately bounded region has radius $R^\ast = \rho/\alpha$. In the linear case, $\alpha = \mathcal{T}$, recovering #persistence-condition's steady-state result $R^\ast = \rho/\mathcal{T}$ exactly. But Proposition A.1 holds for *any* correction function satisfying the sector condition, not just the linear one.

**The persistence threshold, generalized.** The agent persists (mismatch remains bounded within the model class capacity) iff $\rho/\alpha \lt R$. If the correction function breaks down (A2' fails) before $R^\ast$ is reached, the agent may diverge. This IS #structural-adaptation-necessity's trigger: when $\rho/\alpha \gt R$ (the environment demands more correction than the model class can provide), parametric adaptation fails and structural change is required.

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

**Statement.** Under (A1), (A2'), (A3), with stochastic disturbance (GA-2S: $w(t)$ is zero-mean with $\mathbb{E}[\lVert w(t)\rVert^2] = \sigma_w^2$), the mismatch $\delta(t)$ satisfies:

*[Derived (stochastic-bounded-mismatch, from Itô-Lyapunov analysis)]*

$$\mathbb{E}[\lVert\delta(t)\rVert^2] \leq \lVert\delta(0)\rVert^2 e^{-2\alpha t} + \frac{n\sigma_w^2}{2\alpha}$$

for all $t$, where $n = \dim(\delta)$. The agent persists in the mean-square sense iff:

$$\alpha > \frac{n\sigma_w^2}{2R^2}$$

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

$$R^*_S \;=\; \lVert\delta\rVert_{\text{rms}} = \sigma_w\sqrt{\frac{n}{2\alpha}}$$

Persistence requires $R^*_S < R$, giving $\alpha > n\sigma_w^2 / (2R^2)$. $\square$

**Interpretation.** Model D (Prop A.1) gives $R^* = \rho/\alpha$, scaling as $1/\alpha$. Model S gives $R^*_S = \sigma_w\sqrt{n/(2\alpha)}$, scaling as $1/\sqrt{\alpha}$. Doubling the correction efficiency halves the deterministic steady-state mismatch but only reduces the stochastic steady-state by a factor of $\sqrt{2} \approx 1.41$. Correction is less effective against noise than against drift. This difference in scaling propagates into the adversarial exponent regimes ( #adversarial-exponent-regimes): $b = 2$ under Model D, $b = 3/2$ under Model S.

**Tail bound.** At steady state, Markov's inequality gives $P(\lVert\delta\rVert > R) \leq n\sigma_w^2/(2\alpha R^2)$. The agent stays within $R$ with probability $\geq 1 - \epsilon$ provided $\alpha \geq n\sigma_w^2/(2\epsilon R^2)$. For the linear case (Ornstein-Uhlenbeck), the stationary distribution is Gaussian and exact tail probabilities are available. The Markov bound is the general result holding under (A2') alone.

## Summary of Results

| Result | What it proves | Assumptions | Linear case recovery |
|--------|---------------|-------------|---------------------|
| **A.1** (Bounded Mismatch) | $R^\ast = \rho/\alpha$ | (A1), (A2'), bounded $\rho$ (GA-2) | $\alpha = \mathcal{T}$ gives $R^\ast = \rho/\mathcal{T}$ |
| **A.1S** (Stochastic Bounded Mismatch) | $R^*_S = \sigma_w\sqrt{n/(2\alpha)}$ | (A1), (A2'), stochastic $w$ (GA-2S) | $\alpha = \mathcal{T}$ gives $R^*_S = \sigma_w\sqrt{n/(2\mathcal{T})}$ |
| **A.2** (Stability Margin) | $\Delta\rho^\ast = \alpha R - \rho$ | Same as A.1 | $R \to \infty$ for linear (always stable if $\mathcal{T} \gt 0$) |

## Epistemic Status

The setup and assumptions are *definitions* — they specify what we mean by "correction function" and "disturbance." Propositions A.1 and A.2 are *exact* — they follow from the assumptions via standard Lyapunov theory (Khalil 2002[^khalil2002], Chapters 4 and 9). Proposition A.1S is *exact* under an implicit strengthening of A2': the Ito-Lyapunov proof uses the sector bound on the entire trajectory, but the Wiener process can push $\delta$ outside $\mathcal B_R$ where the local sector condition does not hold. The proof is valid when A2' holds in a sufficiently large region (or globally), or when a stopping-time argument bounds the contribution of excursions. For practical purposes the tail bound (Markov inequality) quantifies the excursion probability and the gap is higher-order when $R^*_S \ll R$. This is a standard subtlety in applied stochastic Lyapunov theory, not specific to ACT. The assumptions themselves (sector condition, bounded disturbance) are *empirical claims* about the qualitative behavior of real correction dynamics. The sector-condition framework originates with Lur'e (1957); the Lyapunov stability results are standard. The application to adaptive agents under the ACT framework is new but the mathematics is not.

## Discussion

**Key value.** The persistence threshold and adaptive reserve are no longer contingent on the linear hypothesis in #mismatch-dynamics. They hold for any correction dynamics satisfying the sector condition — a mild qualitative assumption that says "correction points inward with at least baseline efficiency $\alpha$." This is a significant epistemic upgrade: from *hypothesis-dependent* to *robust under qualitative assumptions*.

**What the proofs do NOT illuminate.** (1) Quantitative steady-state values — Lyapunov gives *bounds*, not exact values; the linear analysis remains necessary for quantitative predictions. (2) Convergence rates — standard Lyapunov tells you stable/unstable, not how fast. (3) Optimal gain structure — #update-gain comes from estimation theory, not stability theory. (4) Model sufficiency — the #information-bottleneck framework is information-theoretic, complementary to but independent of stability analysis.

**Two disturbance models.** Proposition A.1 assumes bounded disturbance (GA-2: $\lVert w(t)\rVert \leq \rho$); Proposition A.1S assumes stochastic disturbance (GA-2S: $\mathbb{E}[\lVert w(t)\rVert^2] = \sigma_w^2$). These are not approximations to each other — they capture structurally different environments. Model D (bounded) covers persistent directional change: an adversary who maneuvers, an API that drifts, a climate that shifts. Model S (stochastic) covers unpredictable fluctuations around a stable mean: market noise, sensor noise, random perturbations. The choice of model is an empirical question for each domain; the theory provides both tools. Neither model handles heavy-tailed environmental shocks (financial crises, ecological catastrophes, strategic surprise) where $\lVert w(t)\rVert$ can exceed any finite bound with non-negligible probability. Extreme tail events are better understood as triggers for structural adaptation ( #structural-adaptation-necessity) rather than disturbances to be absorbed parametrically.

## Working Notes

- The adversarial extension (Prop A.3, coupled agents) and effects spiral (Cor A.3.1) are in #adversarial-destabilization. The multi-timescale sketch (A.4) is in #multi-timescale-stability.
- The vector treatment of $\delta(t) \in \mathbb{R}^n$ connects directly to per-dimension tempo analysis ( #per-dimension-persistence). Each dimension can have different effective $\alpha_k$ values, and the weakest dimension determines overall persistence — a tensor generalization of the scalar results here.
- A global sector condition (A2 without the local restriction to $\mathcal B_R$) would give global stability, making $\Delta\rho^\ast$ infinite — the agent could absorb any finite disturbance shock. But this requires the correction function to work perfectly at arbitrary mismatch magnitudes, which is unrealistic for any finite model class. The local form (A2') is the honest one.

---

[^khalil2002]: Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.). Prentice Hall. Chapters 4 (Lyapunov stability), 9 (input-output stability).
[^lure1957]: Lur'e, A. I. (1957). *Some Nonlinear Problems in the Theory of Automatic Control*. Original sector-condition framework for absolute stability.

*(Descended from TFT Appendix A, Props A.1–A.2.)*
