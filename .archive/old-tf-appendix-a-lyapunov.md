# Appendix A: Lyapunov Stability Analysis for Adaptive Tempo

**Epistemic status**: The setup and assumptions are *definitions*. Propositions A.1–A.3 and Corollary A.3.1 are *derived* — they follow from the assumptions via standard Lyapunov theory. The assumptions themselves (sector condition, bounded disturbance) are *empirical claims* about the qualitative behavior of real correction dynamics. Proposition A.4 is a *sketch* whose rigorous treatment requires specifying structural adaptation dynamics not yet available in TFT.

## Motivation

TF-11 derives the persistence threshold ($\mathcal{T} \gt \rho/\Vert\delta_{\text{critical}}\Vert$) and steady-state mismatch ($\Vert\delta\Vert_{ss} = \rho/\mathcal{T}$) from a specific linear ODE hypothesis:

*[Hypothesis (from TF-11)]*
$$\frac{d\Vert\delta\Vert}{dt} = -\mathcal{T} \cdot \Vert\delta\Vert + \rho$$

This is explicitly labeled in TF-11 as a first-order approximation. The linear form yields clean closed-form results but commits to a specific functional relationship between mismatch magnitude and correction rate. As noted in TF-11 Open Question #1, the true correction dynamics are almost certainly nonlinear — exhibiting saturation at large mismatch, threshold effects near zero, and structural breakdown when the model class is exhausted.

A Lyapunov approach[^khalil2002] proves persistence and stability under much weaker assumptions: any correction dynamics satisfying qualitative monotonicity properties. The results below are strictly more general than TF-11's linear analysis — the linear case is recovered as a special case where the sector bounds coincide.

### What This Analysis Illuminates

1. **Persistence without linearity.** The persistence threshold becomes a theorem about general dynamics, not about one specific ODE.

2. **Stability margin / shock tolerance.** How much sudden environmental change an agent can absorb before divergence — a basin-of-attraction characterization richer than the linear analysis provides.

3. **Adversarial destabilization as formal instability.** "Getting inside the opponent's loop" as a Lyapunov instability result: one agent drives the other's state out of its basin of attraction.

4. **Structural adaptation trigger from dynamics.** When the correction function's sector condition breaks down, the Lyapunov function stops decreasing — a dynamical signal that parametric adaptation has exhausted the model class (connecting to TF-10).

5. **Effects spiral as positive-feedback instability.** Boyd's cascading disorientation derived from coupled Lyapunov dynamics rather than asserted as qualitative observation.

### What This Analysis Does NOT Illuminate

1. **Quantitative steady-state values.** Lyapunov gives *bounds*, not exact values. We get "$\Vert\delta\Vert$ is bounded by $R^\ast$" but not "$\Vert\delta\Vert \to \rho/\mathcal{T}$ exactly." The linear analysis (TF-11) remains necessary for quantitative predictions.

2. **Convergence rates.** Standard Lyapunov tells you stable/unstable, not how fast. Exponential stability results exist but require additional assumptions that effectively recover the linear case.

3. **Optimal gain structure.** Lyapunov is about dynamics, not about what the control law should look like. The uncertainty ratio principle ($\eta^\ast = U_M/(U_M + U_o)$, TF-06) comes from estimation theory, not stability theory. These are complementary, not competing.

4. **Exploration-exploitation balance.** The CIY-integrated policy objective (TF-07 or TF-08) is a decision-theoretic question, not a stability question. Lyapunov might give a *constraint* on policy (don't let mismatch leave the basin), but not the *optimal* policy.

5. **Model sufficiency.** The information bottleneck (TF-03) and sufficient statistic framework (TF-10) are information-theoretic. Lyapunov adds nothing to them directly — though the *consequences* of sufficiency (how fast mismatch decays) are exactly what Lyapunov analyzes.

6. **Causal structure.** TF-02's causality grounding is about the temporal ordering of events and Pearl's hierarchy — prior to and independent of dynamical stability.

---

## Setup

Let $\delta(t) \in \mathbb{R}^n$ be the mismatch vector — the difference between the model's predictions and reality across $n$ observable dimensions. The vector treatment connects to the tensor-tempo extension flagged in TF-11 Open Question #4.

The mismatch dynamics are:

*[Definition (Dynamics Setup)]*
$$\frac{d\delta}{dt} = -F(\mathcal{T}, \delta) + w(t)$$

where:

- $F(\mathcal{T}, \delta): \mathbb R_+ \times \mathbb{R}^n \to \mathbb{R}^n$ is the **correction function** — how the agent's adaptive process reduces mismatch. It maps to the same space as $\delta$ (so that the inner product $\delta^T F$ in the sector condition is well-defined). This subsumes the update gain $\eta^\ast$, event rate $\nu$, and the structure of the update rule (TF-06).
- $w(t)$ is the **disturbance** — new mismatch introduced by environmental change, with $\Vertw(t)\Vert \leq \rho$ (bounded disturbance rate).

The linear case from TF-11 has $F(\mathcal{T}, \delta) = \mathcal{T} \cdot \delta$.

## Assumptions on $F$

We require only qualitative properties, not a specific functional form:

### (A1) Zero Correction at Zero Mismatch

*[Assumption A1]*
$$F(\mathcal{T}, 0) = 0$$

No correction is applied when the model perfectly matches reality.

### (A2) Monotone Correction *(Sector Condition)*

There exist $\alpha, \beta \gt 0$ with $0 \lt \alpha \leq \beta$ such that (following the sector-condition framework of Lur'e[^lure1957]):

*[Assumption A2]*
$$\alpha \Vert\delta\Vert^2 \leq \delta^T F(\mathcal{T}, \delta) \leq \beta \Vert\delta\Vert^2 \quad \forall \delta$$

The correction function always points "inward" (reducing mismatch), and its magnitude is bounded above and below relative to $\Vert\delta\Vert^2$. The linear case has $\alpha = \beta = \mathcal{T}$. A saturating correction has $\alpha$ decreasing for large $\Vert\delta\Vert$. A threshold correction has $\alpha = 0$ for small $\Vert\delta\Vert$.

For the main results, we use the weaker local form:

### (A2') Local Sector Condition

There exists a region $\mathcal B_R = \{\delta : \Vert\delta\Vert \leq R\}$ and $\alpha \gt 0$ such that:

*[Assumption A2' (sector-condition)]*
$$\delta^T F(\mathcal{T}, \delta) \geq \alpha \Vert\delta\Vert^2 \quad \forall \delta \in \mathcal{B}_R$$

This allows the correction to break down outside $\mathcal B_R$ — the structural adaptation regime of TF-10.

### (A3) Tempo Monotonicity

For fixed $\delta$, $\delta^T F(\mathcal{T}, \delta)$ is monotone increasing in $\mathcal{T}$. Higher tempo means faster correction.

**Connection to TFT parameters.** The sector parameter $\alpha$ is determined by the adaptive tempo $\mathcal{T}$ and the structure of the correction function. In the linear case, $\alpha = \mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$. In nonlinear cases, $\alpha$ represents the *worst-case* correction efficiency within the valid region — the minimum ratio of correction power to mismatch magnitude. The radius $R$ represents the model class capacity: how large a mismatch can grow before the correction mechanism fails (i.e., before the sector condition ceases to hold), at which point structural adaptation (TF-10) becomes necessary.

## Candidate Lyapunov Function

*[Definition (Lyapunov Candidate)]*
$$V(\delta) = \frac{1}{2}\Vert\delta\Vert^2$$

This is the simplest choice: positive definite, radially unbounded, continuously differentiable. Its level sets $V = c$ are spheres of radius $\sqrt{2c}$ in mismatch space.

---

## Proposition A.1: Bounded Mismatch (Single Agent)

**Statement.** Under (A1), (A2'), (A3), with bounded disturbance $\Vertw(t)\Vert \leq \rho$, the mismatch $\delta(t)$ is **ultimately bounded**: there exists $R^\ast \gt 0$ such that $\Vert\delta(t)\Vert \leq R^\ast$ for all sufficiently large $t$, provided $R^\ast \lt R$ (the ultimately bounded region fits within the sector-condition region).

**Proof.**

Compute $\dot{V}$ along trajectories:

*[Derived (Proof Step)]*
$$\dot{V} = \delta^T \dot{\delta} = \delta^T[-F(\mathcal{T}, \delta) + w(t)]$$ *[Derived (Proof Step)]*
$$= -\delta^T F(\mathcal{T}, \delta) + \delta^T w(t)$$

By (A2'): $\delta^T F(\mathcal{T}, \delta) \geq \alpha\Vert\delta\Vert^2$

By Cauchy-Schwarz: $\delta^T w(t) \leq \Vert\delta\Vert \cdot \Vertw(t)\Vert \leq \rho\Vert\delta\Vert$

Therefore:

*[Derived (Proof Step)]*
$$\dot{V} \leq -\alpha\Vert\delta\Vert^2 + \rho\Vert\delta\Vert = -\Vert\delta\Vert(\alpha\Vert\delta\Vert - \rho)$$

$\dot{V} \lt 0$ whenever $\Vert\delta\Vert \gt \rho/\alpha$.

Define $R^\ast = \rho/\alpha$. Outside the ball $\mathcal B_{R^\ast}$, the Lyapunov function is strictly decreasing, so trajectories are driven inward. Any trajectory entering $\mathcal B_{R^\ast}$ remains in a neighborhood of it (with possible oscillation at the boundary due to the disturbance).

The agent persists iff $R^\ast \lt R$, i.e., iff $\rho/\alpha \lt R$, i.e., iff $\alpha \gt \rho/R$. $\square$

**Interpretation.** The ultimately bounded region has radius $R^\ast = \rho/\alpha$. In the linear case, $\alpha = \mathcal{T}$, recovering TF-11's steady-state result $R^\ast = \rho/\mathcal{T}$ exactly. But Proposition A.1 holds for *any* correction function satisfying the sector condition, not just the linear one.

**The persistence threshold, generalized.** The agent persists (mismatch remains bounded within the model class capacity) iff $\rho/\alpha \lt R$. If the correction function breaks down (A2' fails) before $R^\ast$ is reached, the agent may diverge. This IS TF-10's structural adaptation trigger: when $\rho/\alpha \gt R$ (the environment demands more correction than the model class can provide), parametric adaptation fails and structural change is required.

**Note on the bounded-disturbance assumption.** Proposition A.1 requires $\Vertw(t)\Vert \leq \rho$ — that disturbance magnitude has a finite upper bound. This is appropriate for the typical operating regime of most adaptive systems, but excludes heavy-tailed (e.g., power-law distributed) environmental shocks where $\Vertw(t)\Vert$ can exceed any finite bound with non-negligible probability. Financial crises, ecological catastrophes, and strategic surprise are examples where the bounded-disturbance assumption may be violated. For such environments, stochastic Lyapunov methods — input-to-state stability in probability (ISSp), martingale-based stability, or moment bounds on stochastic Lyapunov functions — would be needed to characterize persistence in a probabilistic rather than deterministic sense. The bounded case gives worst-case guarantees for the typical regime; extreme tail events are better understood as triggers for structural adaptation (TF-10) rather than as disturbances to be absorbed parametrically.

---

## Proposition A.2: Stability Margin (Adaptive Reserve)

**Statement.** Under the conditions of A.1, the agent can tolerate a sudden increase in disturbance rate of:

*[Derived (adaptive-reserve)]*
$$\Delta\rho^* = \alpha R - \rho$$

without mismatch diverging (where $R$ is the radius of the sector-condition region from A2'). Beyond this, $R^\ast$ exceeds $R$ and the correction function may fail.

**Proof.** After a shock, the new disturbance rate is $\rho + \Delta\rho$. The new ultimately bounded radius is $(\rho + \Delta\rho)/\alpha$. This remains within the valid region iff $(\rho + \Delta\rho)/\alpha \leq R$, i.e., $\Delta\rho \leq \alpha R - \rho$. $\square$

**Interpretation.** $\Delta\rho^\ast$ is the agent's **adaptive reserve** — how much additional environmental volatility it can absorb before its model breaks down. This is a single number characterizing an agent's robustness to shock:

- An agent operating well below capacity ($\rho \ll \alpha R$) has a large reserve — it is **robust**.
- An agent near its limit ($\rho \approx \alpha R$) has a small reserve — it is **fragile**.

### Domain Instances

| Domain | Large $\Delta\rho^\ast$ (robust) | Small $\Delta\rho^\ast$ (fragile) |
|--------|-------------------------------|-------------------------------|
| Control | Kalman filter on slow target | Same filter on erratic target |
| Biology | Organism in stable niche | Same organism under climate change |
| Organization | Well-capitalized firm, stable market | Startup in volatile market |
| Military | Force with operational depth | Force at culmination point |

---

## Proposition A.3: Adversarial Destabilization

**Statement.** When two agents $A$ and $B$ are coupled such that $A$'s actions contribute to $B$'s disturbance rate, Agent $A$ can drive Agent $B$ outside $B$'s invariant region — causing $B$'s correction mechanism to break down — when $A$'s effective disruption exceeds $B$'s adaptive reserve.

**Setup.** Let both agents satisfy (A1), (A2'), (A3) with respective parameters $(\alpha_A, R_A, \rho_{A,\text{base}})$ and $(\alpha_B, R_B, \rho_{B,\text{base}})$. The coupling:

*[Assumption (Coupling Model)]*
$$\rho_B = \rho_{B,\text{base}} + \gamma_A \cdot \mathcal{T}_A$$

where $\gamma_A \gt 0$ represents the effectiveness of $A$'s actions at disrupting $B$'s environment. (This factor depends on coupling strength, observability, and action impact — the factors in TF-01's coupling spectrum.)

**Note on decoupling assumption.** This coupling model treats $\mathcal T_A$ as an exogenous parameter shaping $B$'s disturbance bound, rather than modeling the fully coupled dynamical system where both agents' mismatch states co-evolve (i.e., $w_B(t) = f(\delta_A(t), \delta_B(t), \ldots)$). The analysis therefore characterizes the *destabilization threshold* — the conditions under which $A$ *can* push $B$ past its stability boundary — rather than the full transient dynamics of the coupled system. This is a worst-case bound (treating $A$ as operating at its steady-state tempo, the most favorable case for $A$). A full coupled Lyapunov analysis with a joint function $V(\delta_A, \delta_B)$ would capture mutual feedback effects but requires specifying how each agent's mismatch state affects the other's disturbance in real time — an extension noted in TF-11 Open Question #2.

**Proof sketch.**

$B$'s ultimately bounded radius under coupled dynamics is:

*[Derived (Proof Step)]*
$$R^*_B = \frac{\rho_{B,\text{base}} + \gamma_A \cdot \mathcal{T}_A}{\alpha_B}$$

$B$ diverges (exits its sector-condition region) when $R^\ast_B \gt R_B$, i.e., when:

*[Derived (Proof Step)]*
$$\gamma_A \cdot \mathcal{T}_A \gt \alpha_B R_B - \rho_{B,\text{base}} = \Delta\rho^*_B$$

That is:

*[Derived (Proof Step)]*
$$\mathcal{T}_A \gt \frac{\Delta\rho^*_B}{\gamma_A}$$

Symmetrically, $B$ destabilizes $A$ when:

*[Derived (Proof Step)]*
$$\mathcal{T}_B \gt \frac{\Delta\rho^*_A}{\gamma_B}$$

The adversarial outcome depends on whether either agent can push the other past its stability limit. $\square$

**Interpretation.** "Getting inside the opponent's OODA loop" has a precise Lyapunov characterization: Agent $A$ destabilizes Agent $B$ when $A$'s tempo, multiplied by coupling effectiveness, exceeds $B$'s adaptive reserve $\Delta\rho^\ast_B$. This is richer than TF-11's linear steady-state coupled scaling law (under coupling-dominant disturbance, $\Vert\delta_B\Vert/\Vert\delta_A\Vert \approx (\gamma_A/\gamma_B)(\mathcal T_A/\mathcal T_B)^2$) because it captures:

- **Asymmetric coupling** ($\gamma_A \neq \gamma_B$): an agent with lower tempo but higher coupling effectiveness can still win.
- **Finite reserves**: an agent with very high $\mathcal{T}$ but operating near its model-class limit ($\Delta\rho^\ast$ small) is vulnerable despite high tempo.
- **Structural collapse**: when $R^\ast_B \gt R_B$, the failure mode is not merely "large mismatch" but "correction mechanism breakdown" — connecting to TF-10's structural adaptation requirement.

The linear analysis in TF-11 gives the steady-state ratio — a clean quantitative result. Proposition A.3 gives the qualitative result: under what conditions does $B$ *fail entirely*, not merely fall behind. The linear analysis tells you the score; the Lyapunov analysis tells you when the game is over.

---

## Corollary A.3.1: The Effects Spiral

**Statement.** When Agent $B$ is driven past its stability boundary ($R^\ast_B \gt R_B$), and $B$'s degrading model causes $B$'s actions to become erratic in a way that increases $A$'s coupling effectiveness ($\gamma_A$ increases with $\Vert\delta_B\Vert$), the result is a positive-feedback Lyapunov instability.

**Mechanism.** Once $B$ exits $\mathcal B_{R_B}$:

*[Discussion — Mechanism Schematic]*
$$\Vert\delta_B\Vert \uparrow \;\Rightarrow\; B\text{'s actions become erratic} \;\Rightarrow\; \gamma_A \uparrow \;\Rightarrow\; \rho_B \uparrow \;\Rightarrow\; \Vert\delta_B\Vert \uparrow$$

With $\gamma_A$ now an increasing function of $\Vert\delta_B\Vert$, the disturbance term in $B$'s dynamics grows superlinearly. $\dot V_B \gt 0$ and increasing — mismatch accelerates away from the stability region.

**Interpretation.** This is Boyd's **effects spiral** — cascading disorientation of the slower adversary — derived here from Lyapunov instability with positive-feedback coupling rather than asserted as qualitative military doctrine. The spiral terminates only when $B$ undergoes structural adaptation (TF-10 — changing the model class, reorganizing command structure, adopting fundamentally new doctrine) or ceases to function as an adaptive agent entirely.

---

## Proposition A.4: Multi-Timescale Stability (Sketch)

**Status**: This is a *sketch*, not a complete result. Making it rigorous requires specifying the dynamics of deeper adaptive levels more precisely than TFT currently provides. The framework and approach are presented here as a guide for future development.

### The General $N$-Timescale System

The temporal nesting in TF-11 creates a coupled multi-timescale system with $N$ levels. Singular perturbation theory provides tools to analyze such systems. Define a hierarchy of state variables:

*[Definition (State Hierarchy)]*
$$x^{(1)}, \; x^{(2)}, \; \ldots, \; x^{(N)}$$

where $x^{(1)}$ is the fastest (e.g., mismatch at the reactive/parametric level) and $x^{(N)}$ is the slowest (e.g., architectural or meta-structural state). The coupled dynamics:

*[Formulation (A.4 Sketch)]*
$$\dot{x}^{(k)} = \frac{1}{\epsilon_k} \, G^{(k)}\!\left(x^{(1)}, \ldots, x^{(N)}\right) + w^{(k)}(t)$$

where $\epsilon_1 \ll \epsilon_2 \ll \cdots \ll \epsilon_N$ encode the timescale separation and each $G^{(k)}$ may depend on the states at all levels (since each level operates on the output of the levels below and is parameterized by the levels above).

### The Two-Timescale Special Case

The simplest nontrivial instance has $N = 2$:

- Fast state $x^{(1)} = \delta$ (mismatch under parametric adaptation)
- Slow state $x^{(2)} = \mathcal{M}$ (model class, changing on a structural timescale)

*[Formulation (A.4 Sketch)]*
$$\dot{x}^{(1)} = -F(\mathcal{T}, x^{(1)}; x^{(2)}) + w(t) \quad \text{(fast: parametric adaptation)}$$
*[Formulation (A.4 Sketch)]*
$$\dot{x}^{(2)} = \epsilon \, G(x^{(1)}, x^{(2)}) \quad \text{(slow: structural adaptation)}$$

where $\epsilon \ll 1$ reflects the timescale separation (structural dynamics evolve on a much slower timescale) and $F$ depends on $x^{(2)}$ (the correction function is determined by the current model class).

### Sketch of Approach (General Case)

The standard singular perturbation result (Tikhonov's theorem, generalized) applies layer by layer: if level $k$ is stable for each fixed configuration of the slower levels $k+1, \ldots, N$ (each level has a stable attractor given the levels above it), and each successive slow manifold is itself stable, then the composite $N$-level system is stable.

TF-11's convergence constraint $\nu_{n+1} \ll \nu_n$ is the condition ensuring sufficient timescale separation at each boundary — i.e., $\epsilon_k / \epsilon_{k+1} \ll 1$ for each $k$. When this separation is violated between any adjacent pair, the faster level's transients contaminate the slower level's dynamics, potentially destabilizing the composite system.

### What's Missing for a Full Result

The dynamics $G^{(k)}$ for levels deeper than parametric adaptation are not yet specified in TFT. TF-10 gives the *trigger condition* for structural change (persistent residual patterns indicating model class inadequacy) but not the *dynamics* of how change at deeper levels proceeds. Specifying these would require theories of how agents search over model classes, modify their own architecture, or restructure their adaptive mechanisms — open problems in RL (architecture search, meta-learning), biology (evolutionary dynamics, developmental plasticity), and organizational theory (institutional change).

The sketch suggests that TF-11's convergence constraint is not merely a heuristic but a formal condition for composite stability across arbitrarily many timescales; making this precise awaits better specification of the deeper-level dynamics.

**Note on applicability to LLM systems.** LLMs will likely involve many parallel adaptive processes — pretraining (slowest), fine-tuning, LoRA-style online adaptation, in-context learning, retrieval/RAG updates, tool-use feedback, and within-generation attention dynamics — without clean boundaries between "parametric" and "structural." The $N$-timescale framework accommodates this naturally: each mechanism operates at its characteristic rate, and the stability analysis requires only that adjacent timescales be sufficiently separated, regardless of how many levels exist or how they are labeled.

---

## Summary of Results

| Result | What it proves | Assumptions | Linear case recovery |
|--------|---------------|-------------|---------------------|
| **A.1** (Bounded Mismatch) | Mismatch ultimately bounded by $R^\ast = \rho/\alpha$ | (A1), (A2'), bounded $\rho$ | $\alpha = \mathcal{T}$ gives $R^\ast = \rho/\mathcal{T}$ (Prop 11.1) |
| **A.2** (Stability Margin) | Adaptive reserve $\Delta\rho^\ast = \alpha R - \rho$ | Same as A.1 | $R \to \infty$ for linear (always stable if $\mathcal{T} \gt 0$) |
| **A.3** (Adversarial) | $A$ destabilizes $B$ when $\gamma_A \mathcal T_A \gt \Delta\rho^\ast_B$ | Both agents satisfy A.1; linear coupling | Consistent with TF-11 coupled scaling and gives explicit instability threshold |
| **A.3.1** (Effects Spiral) | Positive-feedback instability post-destabilization | $\gamma_A$ increasing in $\Vert\delta_B\Vert$ | Not present in linear analysis |
| **A.4** (Multi-Timescale) | *Sketch*: $N$-level timescale separation → composite stability | $\epsilon_k / \epsilon_{k+1} \ll 1$; each level stable given slower levels | Recovers convergence constraint $\nu_{n+1} \ll \nu_n$ |

**Key value of the Lyapunov approach.** The persistence threshold and adversarial results are no longer contingent on the linear hypothesis. They hold for any correction dynamics satisfying the sector condition — a mild qualitative assumption that says "correction points inward and is proportional (within bounds) to mismatch." This is a significant epistemic upgrade: from *hypothesis-dependent* to *robust under qualitative assumptions*.

---

[^khalil2002]: Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.). Prentice Hall. Chapters 4 (Lyapunov stability), 9 (input-output stability), 14 (singular perturbations).
[^sontag1989]: Sontag, E. D. (1989). "Smooth stabilization implies coprime factorization." *IEEE Trans. Automatic Control*, 34(4), 435–443. Introduced input-to-state stability (ISS).
[^lure1957]: Lur'e, A. I. (1957). *Some Nonlinear Problems in the Theory of Automatic Control*. Original sector-condition framework for absolute stability.
