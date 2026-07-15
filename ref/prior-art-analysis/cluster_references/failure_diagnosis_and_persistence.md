# Cluster Reference: Failure Diagnosis and Persistence (Diagnostic Splits)

**Overview:** Orthogonalizes failure into the Satisfaction Gap (feasibility) and Control Regret (optimality), creating a forced sequence of cognitive updates known as the Orient Cascade.

---

## Canonical Source Segments

### Source: `def-satisfaction-gap.md`

```yaml
---
slug: def-satisfaction-gap
type: definition
status: exact
depends:
  - def-value-object
  - form-objective-functional
stage: draft
---
```


# Definition: Satisfaction Gap

The satisfaction gap measures the distance between what the objective requires and what the best available one-step policy improvement can deliver, under the current model and horizon. Under the canonical continuation convention ( #def-value-object), this is a *local* diagnostic — it answers "can I improve toward the goal from here?" not "is the goal globally feasible?" A multi-step recoverable objective may show positive $\delta_{\text{sat}}$ because continuation is frozen at $\pi_{\text{current}}$. Different continuation conventions yield different gap values; see Epistemic Status.

## Formal Expression

*[Definition (objective-attainability)]*

$$A_O(M_t;\, \Pi, N_h) = \sup_{\pi \in \Pi} V_O(M_t, \pi;\, N_h)$$

The **objective attainability** — the best achievable value given current beliefs $M_t$, available policy class $\Pi$, and horizon $N_h$.

*[Definition (satisfaction-gap)]*

$$\delta_{\text{sat}} = V_{O_t}^{\min} - A_O(M_t;\, \Pi, N_h)$$

where $V_{O_t}^{\min}$ is the minimum trajectory value that counts as "objective met" — a threshold set by the objective itself (for constraints: all satisfied; for utility: a minimum acceptable level).

- $\delta_{\text{sat}} \gt 0$: The objective is **unmet** under the best available policy, current model, and horizon.
- $\delta_{\text{sat}} \leq 0$: The objective is **attainable** in principle.

**Disambiguation.** $\delta_{\text{sat}} \gt 0$ does NOT automatically mean the goal is wrong. It means the goal is unmet given $(M_t, \Pi, N_h)$. The positive signal has multiple possible causes:

| Cause | Fix | How to distinguish |
|---|---|---|
| Goal is genuinely infeasible | Revise $O_t$ | Persists across $M_t$, $\Pi$, $N_h$ improvements |
| Policy class too narrow | Expand $\Pi$ (structural adaptation of $\Sigma_t$) | $\delta_{\text{sat}}$ decreases when richer policies are tried |
| Horizon too short | Extend $N_h$ | $\delta_{\text{sat}}$ decreases with longer planning horizon |
| Model is wrong about feasibility | Improve $M_t$ (reduce $\delta_{\text{epistemic}}$) | $\delta_{\text{sat}}$ changes when $M_t$ is corrected |
| Objectives jointly infeasible | Revise $O_t$ or relax constraints | Individual terminal satisfaction gaps are zero but AND-node fails; cross-terminal tradeoff is required |

Objective revision is the **last resort**, not the first response to unmet goals. The orient cascade ( #der-orient-cascade) formalizes this ordering.

## Epistemic Status

*Exact as a definition — convention-relative as a diagnostic.* The satisfaction gap is a mathematical definition — the difference between a threshold and a supremum over a function class. The definition is precise; the *computation* of $A_O$ is generally intractable (it requires optimization over a policy class), but the quantity is well-defined. However, the *value* of $\delta_{\text{sat}}$ depends on three external parameters: the continuation convention ($\pi_{\text{cont}}$), the horizon ($N_h$), and the scalarization of the objective ($V_{O_t}$). These are not derived by AAT — they are choices the analyst makes. The satisfaction gap is therefore an intrinsic architectural diagnostic *given* a measurement convention, not an absolute property of the agent.

**Convention dependence and the hierarchy.** $A_O$ inherits the continuation convention from the value object ( #def-value-object), which defines three named conventions forming a monotonicity hierarchy:

- **C1** (one-step improvement, canonical): $\delta_{\text{sat}}^{(1)} = V_{O_t}^{\min} - A_O^{(1)}$. Tests whether the agent can improve toward the goal in one step. Most conservative — a multi-step recoverable objective may show $\delta_{\text{sat}}^{(1)} \gt 0$ because continuation is frozen at $\pi_{\text{current}}$.
- **C2** (receding-horizon): $\delta_{\text{sat}}^{\text{RH}} = V_{O_t}^{\min} - A_O^{\text{RH}}$. Tests whether the agent can reach the goal with $N_r$-step replanning. Captures recovery paths invisible to C1.
- **C3** (Bellman): $\delta_{\text{sat}}^{\text{B}} = V_{O_t}^{\min} - A_O^{\text{B}}$. Tests whether the goal is genuinely infeasible given $(M_t, \Pi, N_h)$. Strongest diagnostic — $\delta_{\text{sat}}^{\text{B}} \gt 0$ means no policy in $\Pi$ can achieve the objective.

The monotonicity result ( #def-value-object): $\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$. C1 gives the most false "unattainable" diagnoses; C3 gives none (modulo model error in $M_t$). Analyses using different conventions should not be compared directly — the convention is part of the measurement.

## Discussion

**Why two gap measures, not one.** An earlier formulation used a single $\delta_{\text{objective}}$ for goal-related mismatch. This conflates two distinct situations: "the goal is too hard" and "the strategy is too weak." When the agent is optimally pursuing an infeasible goal, $\delta_{\text{objective}}$ is large but there's no strategy to improve — the problem is the goal, not the plan. The satisfaction gap ($\delta_{\text{sat}}$) and control regret ( #def-control-regret) separate these cases, enabling the right corrective action.

**The disambiguation table is load-bearing.** Without it, an agent facing $\delta_{\text{sat}} \gt 0$ might immediately revise its objective when the real problem is an inadequate model or a too-narrow policy class. The table encodes the diagnostic procedure: check $M_t$ adequacy first (maybe the goal IS feasible but the model doesn't know it), then check $\Pi$ and $N_h$, and only then consider revising $O_t$.

**Dependence on $M_t$.** $A_O$ is computed from $M_t$, not from the true environment state $\Omega_t$. The agent's assessment of attainability could be wrong — an achievable goal might look unachievable with a bad model, or vice versa. Improving $M_t$ (reducing $\delta_{\text{epistemic}}$) brings the agent's attainability assessment closer to reality. This is why the orient cascade puts epistemic update before attainability evaluation.

**Diagnostic content vs. AI's expected-free-energy decomposition.** Active inference's expected free energy (EFE) decomposes into *pragmatic value* (how preferred are the outcomes the policy expects?) and *epistemic value* (how much does the policy reduce uncertainty?) (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Da Costa, Parr, Sajid, Veselic, Neacsu & Friston 2020, "Active inference on discrete state-spaces," *J. Math. Psych.* 99 §2.4; Sajid, Ball, Parr & Friston 2021, "Active inference: demystified and compared," *Neural Computation* 33). The decomposition supports policy ranking but does not separate two distinct diagnoses that AAT's apparatus does separate: "the goal is unattainable from here" ($\delta_{\mathrm{sat}} \gt 0$, this segment) versus "the current policy is not the best available" ($\delta_{\mathrm{regret}} \gt 0$ in #def-control-regret). Both increase EFE without distinguishing the cause. The 2×2 cell map in the disambiguation table above gives the four diagnoses the orient cascade ( #der-orient-cascade) acts on differently — strategy revision, objective revision, action vs. learning. AI's pragmatic-epistemic split does not produce this disambiguation.

The diagnostic structure depends on $V_{O_t}$ being a *value functional* on trajectories ( #form-objective-functional) and $A_O$ being an *attainability supremum*, not on outcomes encoded as log-priors — AI's preferences-as-priors form ($C(o) = \log P_{\mathrm{pref}}(o)$) collapses the diagnostic by making "wanting $o$" and "expecting $o$" formally the same operation (the dark-room critique, Sun & Firestone 2020, "The dark room problem," *Trends Cog. Sci.* 24). Sun & Firestone diagnose the preferences-as-priors collapse; AAT's value-functional reformulation is AAT's own downstream architectural response to that diagnosis, not a move Sun & Firestone themselves propose. The conservative reading of the citation: AAT takes their critique as motivation for abandoning the preferences-as-priors form in favor of value functionals that separate outcome value from outcome prediction, enabling the diagnostic structure the 2×2 cell map requires. This is a deliberate divergence from AI, not an oversight.

## Working Notes

- $V_{O_t}^{\min}$ (the satisfaction threshold) is a property of the objective, not of the agent. For constraint-satisfaction objectives, it's natural (all constraints met = satisfied). For utility-maximizing objectives, it's less obvious — what counts as "good enough"? This threshold may need to be explicitly modeled as part of $O_t$.
- The supremum in $A_O$ is over $\Pi$, the available policy class. For agents with explicit $\Sigma_t$, $\Pi$ corresponds to the set of strategies representable in the agent's DAG formalism. Expanding $\Pi$ (structural adaptation of $\Sigma_t$ — adding nodes, edges, or changing $\gamma$ assignments) is the purposeful analog of #result-structural-adaptation-necessity.
- **Cross-reference to NeurIPS Paper 2.** The satisfaction-gap / control-regret two-gap diagnostic is **Component 1** of NeurIPS 2026 Paper 2's composition theorem ("A Unified Convergence Theory for Non-Stationary Reinforcement Learning", `~/src/neurips/02-unified-convergence-rl/`, §4 Theorem 4.1). The diagnostic separates "you're not doing it well enough" (control regret) from "the world doesn't permit it" (satisfaction gap), preventing dark-room collapse in the composed regret bound. The paper's hypothesis (A1) carries the extended-real reading required for the two-gap structure to hold even when the satisfaction frontier is empty. See `spikes/neurips-back-integration-2026-05-08.md` §1 Paper 2.


---

### Source: `def-control-regret.md`

```yaml
---
slug: def-control-regret
type: definition
status: exact
depends:
  - def-value-object
  - def-satisfaction-gap
stage: draft
---
```


# Definition: Control Regret

Control regret measures the gap between the best available one-step policy improvement and the agent's current policy, under the current model and horizon. Under the canonical continuation convention ( #def-value-object), this is a *local* diagnostic — it answers "could I do better right now?" not "is my overall strategy globally suboptimal?" A revisable policy may show low $\delta_{\text{regret}}$ simply because continuation is frozen. This is the signal for strategy revision, with the caveat that the signal's scope matches the continuation convention's scope.

## Formal Expression

*[Definition (control-regret)]*

$$\delta_{\text{regret}} = A_O(M_t;\, \Pi, N_h) - V_O(M_t, \pi_{\text{current}};\, N_h) \geq 0$$

Always non-negative: the current policy cannot outperform the best in its class.

- $\delta_{\text{regret}} \approx 0$: The agent is doing the best it can within current $(\Pi, N_h, M_t)$. If $\delta_{\text{sat}} \gt 0$ simultaneously, the problem is not the current strategy — it's either the goal, the capability ($\Pi$, $N_h$), or the model ($M_t$). See #def-satisfaction-gap's disambiguation.
- $\delta_{\text{regret}} \gg 0$: There's room for improvement without changing $O_t$. → Revise $\Sigma_t$.

## Epistemic Status

*Exact as a definition — convention-relative as a diagnostic.* Like the satisfaction gap, this is a mathematical definition — a difference between two values of the same functional. The quantity is well-defined; computing it requires evaluating $A_O$ (generally intractable) and $V_O$ under the current policy (tractable in simulation, approximate in practice).

**Convention hierarchy.** $\delta_{\text{regret}}$ inherits the continuation convention from #def-value-object. Under the monotonicity result: $\delta_{\text{regret}}^{(1)} \leq \delta_{\text{regret}}^{\text{RH}} \leq \delta_{\text{regret}}^{\text{B}}$. C1 (one-step) reveals only the gap between the current first action and the best one-step deviation — a policy that is "locally near-optimal" under C1 may be globally suboptimal. C3 (Bellman) reveals the full gap to the globally optimal policy. C2 (receding-horizon) interpolates: it captures regret from suboptimal first actions that become visible with $N_r$-step lookahead. For strategy revision, C2 is often the most useful convention: it reveals recoverable suboptimality without requiring the full Bellman solution.

## Discussion

**The diagnostic power of the two-gap system.** The satisfaction gap and control regret together encode a 2×2 diagnostic:

| | $\delta_{\text{sat}} \leq 0$ (attainable) | $\delta_{\text{sat}} \gt 0$ (unmet) |
|---|---|---|
| $\delta_{\text{regret}} \approx 0$ (near-optimal) | **Success**: goal achievable, policy good | **Capability limit**: optimally pursuing an unmet goal → check $M_t$, $\Pi$, $N_h$, then consider revising $O_t$ |
| $\delta_{\text{regret}} \gg 0$ (suboptimal) | **Strategy problem**: goal achievable, policy poor → revise $\Sigma_t$ | **Both**: goal hard AND strategy weak → revise $\Sigma_t$ first, then reassess $\delta_{\text{sat}}$ |

This diagnostic is what makes the orient cascade ( #der-orient-cascade) actionable: each cell prescribes a different corrective action.

**Control regret as the signal for $\Sigma_t$ revision.** When $\delta_{\text{regret}}$ is high, the agent knows it could do better with a different strategy. The *specific* corrections — which edges to revise, which branches to prune, which alternatives to add — come from the strategic calibration residual ( #def-strategic-calibration), which localizes the regret to specific parts of $\Sigma_t$.

**Regret approaching zero when optimally failing.** This is the key insight motivating the two-gap split. A single $\delta_{\text{objective}}$ would show "large gap" for both "bad strategy, achievable goal" and "good strategy, impossible goal." The first warrants strategy revision; the second warrants goal revision (after ruling out $M_t$/$\Pi$/$N_h$ inadequacy). Without the split, the agent cannot distinguish these cases and may waste effort optimizing a strategy that's already near-optimal for an infeasible goal.

**Diagnostic content vs. AI's expected-free-energy decomposition.** The 2×2 disambiguation depends on the satisfaction gap / control regret split being orthogonal — distinguishing "goal too hard" from "strategy too weak." Active inference's expected free energy decomposition (pragmatic value + epistemic value; Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29) supports policy ranking but does not separate these diagnoses — both increase EFE without distinguishing cause. See #def-satisfaction-gap for the full analysis of why the diagnostic structure depends on $V_{O_t}$ being a value functional rather than log-priors over outcomes (Sun & Firestone 2020, "The dark room problem," *Trends Cog. Sci.* 24).

## Working Notes

- **Cross-reference to NeurIPS Paper 2.** Together with `#def-satisfaction-gap`, this segment is **Component 1** of NeurIPS 2026 Paper 2's composition theorem ("A Unified Convergence Theory for Non-Stationary Reinforcement Learning", `~/src/neurips/02-unified-convergence-rl/`, §4 Theorem 4.1). The two-gap orthogonality is what gives the composed regret bound a principled coordinate for "is the binding pressure on goal-feasibility or on policy-quality?" Sibling segment `#def-satisfaction-gap` carries the matching cross-reference. See `spikes/neurips-back-integration-2026-05-08.md` §1 Paper 2.


---

### Source: `schema-strategy-persistence.md`

```yaml
---
slug: schema-strategy-persistence
type: proposed-schema
status: conditional
depends:
  - result-sector-condition-stability
  - result-sector-persistence-template
  - def-strategic-calibration
  - def-strategy-dag
stage: draft
---
```


# Proposed-schema: Strategy Persistence Schema

The sector-persistence template ( #result-sector-persistence-template) proves bounded state for any system with a state variable, a correction function satisfying the sector condition, and bounded disturbance. The template is domain-agnostic — it applies to any state variable meeting its preconditions (T1)–(T3). This schema is the strategic-layer instantiation: if strategic update dynamics satisfy the template's preconditions, strategy persistence follows as a direct instance. A key additional requirement — absent from the epistemic instantiation but load-bearing here — is **experience discounting**, because the strategic sector parameter $\alpha_\Sigma$ decays monotonically with experience and requires an explicit forgetting mechanism to remain bounded below.

## Formal Expression

*[Proposed Schema (strategy-persistence-schema, from sector-persistence-template)]*

**If** strategic update dynamics satisfy the template preconditions (T1)–(T3) of #result-sector-persistence-template for $\xi = \delta_\Sigma$ (a strategic mismatch state), together with:

- **(SA1)** Zero correction at zero strategic mismatch (the template's (T1)): when the mismatch state is zero, no revision occurs
- **(SA2')** Local sector condition on strategic correction (the template's (T2) for $\xi = \delta_\Sigma$): the correction function points inward with baseline efficiency $\alpha_\Sigma$ within a strategic reserve $R_\Sigma$
- **(SA3)** Sufficient exploration (OR-nodes only): the action selection policy allocates correction capacity to all OR alternatives at a rate exceeding the strategic disturbance-to-reserve ratio
- Bounded strategic disturbance at rate $\rho_\Sigma$ (the template's (T3)): the rate at which the environment invalidates causal links is bounded

**Then** $\Sigma_t$ persists iff:

$$\alpha_\Sigma \gt \frac{\rho_\Sigma}{R_\Sigma}$$

directly by the template's Model D result. Here $\alpha_\Sigma$ is the strategic correction rate, $\rho_\Sigma$ is the strategic disturbance rate, and $R_\Sigma$ is the strategic reserve (tolerance for strategic mismatch before performance degrades catastrophically). The Model S instantiation replaces $\rho_\Sigma$ with $\sigma_\Sigma$ and gives $\alpha_\Sigma \gt n\sigma_\Sigma^2/(2R_\Sigma^2)$ under the same template.

### Forgetting as Prerequisite

*[Formulation (forgetting-prerequisite)]*

The schema form above is an **instantaneous persistence check at the current experience level**, not a trajectory guarantee. For Beta-Bernoulli edge updates (the canonical verified case; see #deriv-edge-credence-dynamics Props B.1–B.6), the sector parameter has the form:

$$\alpha_\Sigma = \frac{1}{n+1}$$

where $n$ is the edge's accumulated experience (pseudo-count). Without a forgetting mechanism, $n$ grows monotonically with each observation, so $\alpha_\Sigma \to 0$ for every edge asymptotically. For any fixed $(\rho_\Sigma, R_\Sigma)$ with $\rho_\Sigma \gt 0$, every agent eventually violates the threshold. The structural identity with #result-persistence-condition — where $\alpha$ can be stationary — holds for the strategic case only under an explicit forgetting mechanism.

**Exponential forgetting.** Replace the raw Beta-Bernoulli update with a discounted update: at each step, shrink the pseudo-counts by a factor $\lambda \in (0,1)$:

$$\alpha_k \mapsto \lambda\,\alpha_k + y_k, \qquad \beta_k \mapsto \lambda\,\beta_k + (1-y_k)$$

The effective sample size stabilizes at $n_{\text{eff}} = 1/(1-\lambda)$, and substituting into Prop B.1's $\alpha_\Sigma = 1/(n+1)$ gives the exact steady-state sector parameter:

$$\alpha_\Sigma^{\text{ss}} = \frac{1}{n_{\text{eff}} + 1} = \frac{1-\lambda}{2-\lambda}$$

For slow forgetting ($\lambda \to 1$, the regime where the prerequisite is most likely to bind), the leading-order expansion gives the simpler form $\alpha_\Sigma^{\text{ss}} \approx 1-\lambda$ — which agrees with the forgetting rate itself. Outside the high-$\lambda$ regime the approximation deteriorates: at $\lambda = 0.5$, the exact form gives $\alpha_\Sigma^{\text{ss}} = 1/3$ while the linear approximation gives $1/2$ (≈ 50% overestimate); at $\lambda = 0.9$, exact $\alpha_\Sigma^{\text{ss}} = 1/11$ versus approximation $1/10$ (≈ 10% overestimate).

**The forgetting prerequisite.** Combining with the schema's persistence form $\alpha_\Sigma \gt \rho_\Sigma/R_\Sigma$:

$$\frac{1-\lambda}{2-\lambda} \;\gt\; \frac{\rho_\Sigma}{R_\Sigma} \quad\Longleftrightarrow\quad \lambda \;\lt\; \frac{R_\Sigma - 2\rho_\Sigma}{R_\Sigma - \rho_\Sigma}$$

(valid when $\rho_\Sigma \lt R_\Sigma/2$; for $\rho_\Sigma \ge R_\Sigma/2$ no $\lambda$ satisfies the prerequisite and the schema's trajectory guarantee fails for any forgetting rate). The hard ceiling at $\rho_\Sigma = R_\Sigma/2$ and the algebraic content of the steady-state form are derived self-contained in #deriv-strategic-persistence-hard-ceiling — a $\lambda$-independent structural cap on the schema's reachable persistence region under any exponential-forgetting design.

This is a **prerequisite of the schema's trajectory guarantee, not a tunable heuristic**. An agent without forgetting has no long-run strategic persistence regardless of its initial $\alpha_\Sigma$. The steady-state sector parameter must exceed the disturbance-to-reserve ratio, or the instantaneous persistence check — no matter how comfortably it holds at any given time — eventually fails as experience accumulates.

In the slow-forgetting regime the threshold simplifies to the linear-form analog of #result-persistence-condition:

$$(1 - \lambda) \;\gt\; \frac{\rho_\Sigma}{R_\Sigma} \qquad (\text{slow-forgetting limit, } \lambda \to 1)$$

playing the role that $\mathcal{T} \gt \rho / \lVert\delta_{\text{critical}}\rVert$ plays for the epistemic case. The forgetting rate $(1-\lambda)$ is the strategic analog of adaptive tempo: faster forgetting means faster tracking but noisier estimates; slower forgetting means stable estimates but slower tracking. The optimal $\lambda$ balances bias and variance for the specific $\rho_\Sigma$ the environment presents. Outside the slow-forgetting regime, the exact form $(1-\lambda)/(2-\lambda) \gt \rho_\Sigma/R_\Sigma$ is the operating threshold and the simpler linear form is unsafe (it permits $\lambda$ values that violate the actual prerequisite).

**Which mismatch state?** The schema applies to any mismatch state for which conditions (SA1)-(SA3) can be verified. Two candidates exist:

- **Strategy-plan-confidence error** $\delta_s = \hat P_\Sigma - \Phi$: the scalar difference between the agent's strategy-plan-confidence score and the independence-model plan value at true edge parameters. This is the mismatch for which persistence IS proved (Props B.1-B.5 in #deriv-edge-credence-dynamics). It is computable from status propagation without credit assignment. **Scope:** $\delta_s$ operates at L0 of the Correlation Hierarchy ( #def-strategy-dag) — it tracks calibration within the independence model. For L1 (augmented DAG), the same persistence result applies to the augmented graph's $\hat P_\Sigma$. The gap between L0's $\Phi$ and actual plan success under correlated failure is a model-class limitation, not an estimation error.
- **Strategic-calibration residual** $\delta_{\text{strategic}}$: the per-edge value-increment residual aggregation defined in #def-strategic-calibration. This is the mismatch the orient cascade ( #der-orient-cascade) uses for edge-level revision. Persistence of $\delta_{\text{strategic}}$ remains **open** and requires the credit-assignment machinery in #disc-credit-assignment-boundary.

The verified instances below all use per-edge credence error $\boldsymbol\delta_c = (\hat p_k - \theta_k)$ or the plan-level surrogate $\delta_s$. They do not verify the schema for $\delta_{\text{strategic}}$ directly.

## Epistemic Status

*Conditional*, conditioned on (i) Beta-Bernoulli edge dynamics, (ii) exponential forgetting with $\lambda \in (0,1)$, (iii) the sector-persistence template preconditions (T1)–(T3) of #result-sector-persistence-template, and (iv) the mismatch state chosen from $\{\boldsymbol\delta_c, \delta_s\}$ — the per-edge credence error or the plan-level surrogate (per the dependency on #deriv-edge-credence-dynamics Props B.1–B.6). Within these conditions the exact threshold $(1-\lambda)/(2-\lambda) \gt \rho_\Sigma/R_\Sigma$ and the hard ceiling at $\rho_\Sigma \ge R_\Sigma/2$ are algebraically exact — derived self-contained in #deriv-strategic-persistence-hard-ceiling. Strategic mismatch under $\delta_{\text{strategic}}$ (the credit-assigned form) remains open; see Discussion §1 and #disc-credit-assignment-boundary.

What was missing in the original sketch was instantiation — showing that specific strategic update dynamics satisfy the template's preconditions. Four cases have now been verified (full derivations in #deriv-edge-credence-dynamics):

1. **Single edge, Beta-Bernoulli** ($A \to G$): Sector condition satisfied globally with $\alpha_\Sigma = 1/(n+1)$. The bound is tight (expected correction is exactly linear). (A1) satisfied. Persistence condition: $1/(n+1) \gt \rho_\Sigma / R_\Sigma$.

2. **Two-edge chain, observable intermediate** ($A \to B \to G$, $B$ observable): Sector condition satisfied globally with $\alpha_\Sigma = \min(1/(n_1+1), \theta_1/(n_2+1))$ — a weakest-link result. Correction function is diagonal (no cross-edge coupling). (A1) satisfied. The $\theta_1$ factor in edge 2's rate is the evidence-starvation effect.

3. **Two-edge chain, unobservable intermediate** ($A \to B \to G$, $B$ not observable): Per-edge sector condition **fails** — the marginal Bayesian update violates (A1) with bias $O(1/n)$. But plan-level tracking (treating $\hat{\Phi} = p_1 p_2$ as a single Beta) recovers the sector condition with $\alpha_{\Sigma,\text{plan}} = 1/(n_\Phi + 1)$, at the cost of per-edge diagnostic resolution.

4. **Two-arm OR-node, $\varepsilon$-greedy** ($A_1, A_2 \to G$, $G$ is OR): Sector condition satisfied with $\alpha_\Sigma = \min((1-\varepsilon)/(n_1+1),\; \varepsilon/(n_2+1))$ — an **exploration-gated** weakest-link, not depth-gated as in AND chains. (SA3) required: minimum exploration rate $\varepsilon \gt \rho_\Sigma(n_{\max}+1)/R_\Sigma$. Pure greedy ($\varepsilon = 0$) **fails** the sector condition. With optimal equal-rate allocation, $\alpha_\Sigma = 1/(n_1 + n_2 + 2)$ — the correction capacity is split across alternatives.

The schema is no longer purely hypothetical. The sector parameter for strategic dynamics is the edge update gain $\eta_{\text{edge}}$ — the same quantity that governs epistemic persistence. The structural parallel between epistemic and strategic persistence is not an analogy but a mathematical identity at the sector-framework level.

## Discussion

**What's needed to promote this from schema to result.**

1. **Strategic mismatch state**: partially resolved. Prop B.5 in #deriv-edge-credence-dynamics shows the sector condition transfers from per-edge credence error to **strategy-plan-confidence error** $\delta_s = \hat P_\Sigma - \Phi$ — the scalar difference between the agent's strategy-plan-confidence score and the independence-model plan value at true edge parameters (note: $\Phi$ is NOT actual plan success probability under correlated failure — see #def-strategy-dag edge-independence caveat). For linear correction (Beta-Bernoulli), the transfer is exact ($\alpha_s = \alpha_c$); for nonlinear correction, $\alpha_s \geq \alpha_c / \kappa(\mathbf{J})^2$. **However**, $\delta_s$ is distinct from the **strategic-calibration residual** $\delta_{\text{strategic}}$ defined in #def-strategic-calibration, which is an $L^2$ aggregation of per-edge value-increment residuals requiring credit assignment to compute. Persistence of $\delta_s$ (plan-level tracking) is proved; persistence of $\delta_{\text{strategic}}$ (per-edge diagnostics) remains open and requires the credit-assignment machinery in #disc-credit-assignment-boundary.

2. ~~**Strategic correction function**: needs to satisfy the sector condition.~~ **Resolved** for Beta-Bernoulli edges. Props B.1-B.4 in #deriv-edge-credence-dynamics verify the sector condition for four topologies (single edge, two-edge AND observable/unobservable, two-arm OR).

3. **Strategic disturbance**: The rate at which the environment invalidates causal links in $\Sigma_t$. **Still open** as a formalized quantity — currently a domain parameter ($\rho_\Sigma$), analogous to how $\rho$ for epistemic disturbance is a domain parameter in #result-persistence-condition.

4. ~~**Sector condition verification**: the critical mathematical step.~~ **Resolved** for four topologies. See #deriv-edge-credence-dynamics.

5. ~~**Credit assignment / signal function**: needed for edge updates.~~ **Characterized at the theory level.** #disc-credit-assignment-boundary shows persistence does not require credit assignment (Prop B.5), establishes directional fidelity as the minimal requirement, and provides a gradient-based default signal function. The specific update algorithm is domain engineering, not theory — the same way the gain *estimator* is domain engineering while the gain *principle* ($\eta^\ast = U_M/(U_M + U_o)$) is theory. Caveat: the default gradient signal inherits $\hat P_\Sigma$'s overestimation bias under correlated failures ( #def-strategy-dag, #disc-credit-assignment-boundary).

6. **Time-varying $\alpha_\Sigma$**: this is where the strategic case genuinely differs from the epistemic one. For Beta-Bernoulli edges, $\alpha_\Sigma = 1/(n+1)$ decays monotonically with experience, so the sector-persistence template's constant-$\alpha$ precondition cannot hold asymptotically under any raw Bayesian update. The resolution is the **forgetting prerequisite** promoted into the Formal Expression above: exponential forgetting at rate $\lambda$ stabilizes $\alpha_\Sigma$ at the exact value $(1-\lambda)/(2-\lambda)$, with the simpler linear form $1-\lambda$ as the slow-forgetting asymptote. The exact threshold $(1-\lambda)/(2-\lambda) \gt \rho_\Sigma/R_\Sigma$ converts the schema's instantaneous check into a trajectory guarantee. This is structural, not heuristic — without forgetting, the schema's form holds only until the agent accumulates enough experience to cross below threshold; with insufficient forgetting (linear-form approximation that treats $\rho_\Sigma$ as small relative to $R_\Sigma$ when in fact $\rho_\Sigma \ge R_\Sigma/2$), the prerequisite is unsatisfiable and the schema's trajectory guarantee fails.

**The structural parallel is genuine, but conditional on forgetting.** This schema extends *structural persistence* (see Persistence in `LEXICON.md`) from the epistemic substate to the strategy substate — asking whether the strategy correction machinery can outpace the rate at which the environment invalidates the agent's causal theory. It inherits the same limitation: structural persistence of $\Sigma_t$ does not address operational persistence (how close $\lVert\delta_{\text{strategic}}\rVert$ is to $R_\Sigma$) or continuity persistence (whether the agent's strategic identity coheres through time). The persistence condition for $M_t$ ( #result-persistence-condition) says: adaptive tempo must exceed the ratio of disturbance to critical mismatch. If the same mathematics applies to $\Sigma_t$, then strategy persistence requires strategic tempo to exceed the ratio of strategic disturbance to critical strategic mismatch. The strategic analog of "the environment changes faster than the agent can learn" is "the world invalidates plans faster than the agent can revise them." Both lead to the same catastrophic outcome: the system cannot maintain bounded mismatch and begins to degrade.

**What this would buy the theory.** If promoted to a result, strategy persistence would:
- Provide a formal criterion for "when does a strategy remain viable?"
- Connect strategic failure modes to the same mathematical framework as epistemic failure modes
- Enable quantitative comparison: is the bottleneck epistemic persistence (model can't keep up with reality changes) or strategic persistence (plans can't keep up with requirement changes)?
- Ground the organizational intuition that plans need to be revised faster than the situation changes

## Findings

### The Forgetting Prerequisite for Strategic Persistence

**Brief:** With infinite memory, standard Bayesian updating guarantees eventual strategic failure. The sector parameter for Beta-Bernoulli edge updates is $\alpha_\Sigma = 1/(n+1)$, which decays monotonically as experience $n$ accumulates. For any positive disturbance rate, the persistence threshold $\alpha_\Sigma \gt \rho_\Sigma/R_\Sigma$ is eventually violated regardless of the agent's initial calibration. Exponential forgetting with discount factor $\lambda$ stabilizes the effective sample size at $1/(1-\lambda)$, giving exact steady-state $\alpha_\Sigma^{\text{ss}} = (1-\lambda)/(2-\lambda)$ — with the simpler linear form $1-\lambda$ as the slow-forgetting asymptote ($\lambda \to 1$). The forgetting prerequisite — $(1-\lambda)/(2-\lambda) \gt \rho_\Sigma/R_\Sigma$ — converts the schema's instantaneous persistence check into a trajectory guarantee. Forgetting is therefore a structural prerequisite, not a tunable heuristic: the rate at which the agent discounts old evidence must satisfy the threshold. The schema's reachable persistence region under any $\lambda$ is bounded above by a hard structural ceiling at $\rho_\Sigma = R_\Sigma/2$, derived self-contained in `#deriv-strategic-persistence-hard-ceiling`.

**Impact:** Translates an organizational platitude ("stay adaptive") into a quantitative survival inequality with explicit failure mode. Identifies a structural calcification process common to all long-running adaptive systems whose update mechanism accumulates evidence: institutional rigidity, RL value-function staleness, scientific-paradigm lock-in, and the loss-of-edge phenomenon in incumbent firms all instantiate the same dynamic. The threshold is sharp — no amount of prior learning protects against an environment that invalidates plans faster than the agent forgets. For long-lived AI agents this mandates explicit memory-pruning mechanisms; the design choice is not whether to forget but at what rate, and how to keep the strategic disturbance well below half the reserve (above which the hard ceiling closes the design space — see `#deriv-strategic-persistence-hard-ceiling`). The structural identity with `#result-persistence-condition` (where $\alpha$ can be stationary) is recovered for the strategic case *only* under explicit forgetting, which is itself a non-obvious finding about the asymmetry between epistemic and strategic dynamics.

**Novelty Claim:** *Claim differentiation* on Bayesian update dynamics with experience discounting. The Beta-Bernoulli decay $\alpha = 1/(n+1)$ is elementary and the forgetting-factor remedy is standard adaptive-control / online-learning practice. The AAT-distinctive contribution is the connection from these standard mechanics to a *survival inequality with environment-side parameters* (disturbance rate, reserve), making forgetting a structural prerequisite of strategic persistence rather than a hyperparameter. The exact threshold $(1-\lambda)/(2-\lambda) \gt \rho_\Sigma/R_\Sigma$ — with the slow-forgetting linear form $(1-\lambda) \gt \rho_\Sigma/R_\Sigma$ as its asymptotic — is the strategic analog of the linear operational form of the persistence condition, with the forgetting rate $(1-\lambda)$ playing the role of adaptive tempo and the $1/(2-\lambda)$ damping factor capturing the integration of finite-horizon evidence.

**Related Work:**

| ASF Concern | Prior-art Language | Relationship / Positioning |
|---|---|---|
| Exponential forgetting / discounted least squares | Ljung 1987 *System Identification: Theory for the User*, MIT Press (published 1987, found pre-2026) | *formal antecedent* — supplies the discounted-update mechanism; AAT adopts it directly and connects it to a survival threshold |
| Plasticity/stability tradeoff in continual learning | Kirkpatrick et al. 2017 *Overcoming Catastrophic Forgetting in Neural Networks*, PNAS 114(13) (published 2017, found pre-2026) | *conceptual precursor* — frames the same tradeoff at the network-weight level; does not connect to a Lyapunov-style survival inequality with environment parameters |
| Drift detection in streaming learning | Gama et al. 2014 *A Survey on Concept Drift Adaptation*, ACM Computing Surveys 46(4) (published 2014, found pre-2026) | *conceptual precursor* — recognizes the need to track changing distributions; does not formalize "forgetting rate must exceed disturbance-to-reserve ratio" as a structural prerequisite |
| Requisite variety as cybernetic principle | Ashby 1956 *An Introduction to Cybernetics* §11; Conant & Ashby 1970 (published 1956/1970, found pre-2026) | *conceptual precursor* — the regulator's variety must match the disturbance's variety; AAT's forgetting prerequisite is a quantitative time-domain analog applied to the strategic substate |
| Organizational "core rigidities" / competency traps | Leonard-Barton 1992 *Strategic Management Journal* 13:111; Levitt & March 1988 *Annual Review of Sociology* 14:319 (published 1988/1992, found pre-2026) | *conceptual precursor* — qualitative recognition that accumulated competence becomes liability under environmental change; AAT supplies the structural threshold |

**Search Log:**
- 2026-04 (*intuition-only* on the survival-inequality framing): the Beta-Bernoulli $1/(n+1)$ decay is elementary, the forgetting-factor remedy is standard, and the qualitative organizational-calcification intuition is well-established. The unsearched claim is whether the framing as a *structural survival prerequisite* — with environment-side $\rho_\Sigma/R_\Sigma$ on the right-hand side — has been formalized elsewhere as a threshold rather than a hyperparameter. Targeted future search candidates: bounded-rationality with memory cost (Genewein, Leibfried, Grau-Moya, Braun 2015 *Frontiers in Robotics and AI*), regret analysis of forgetting-factor estimators in adaptive control (Anderson-Moore line), organizational-learning literature on competency traps and "core rigidities" connected to environmental volatility metrics. Pre-search expectation: the constituent moves are individually well-precedented; the integrated framing as a Lyapunov-style survival prerequisite for the *strategic* substate, with the structural identity to the epistemic persistence condition under forgetting, is plausibly AAT-distinctive but not yet verified under nominally-comprehensive search.

## Working Notes

- **Done.** Five cases verified: single-edge AND, two-edge AND (observable and unobservable intermediate), two-arm OR ($\varepsilon$-greedy), and mixed AND/OR with common-cause node (L1 augmented DAG). Full derivations in #deriv-edge-credence-dynamics (Props B.1–B.6). Key findings: AND-node persistence is depth-gated (evidence starvation); OR-node persistence is exploration-gated (action selection policy); L1 augmented DAGs exhibit three-way gating (condition testing × starvation × exploration). All satisfy the schema's form ($\alpha_\Sigma \gt \rho_\Sigma/R_\Sigma$). B.6 is the first mixed AND/OR case and confirms L1 results transfer from L0 with correct construction. The next step is deeper mixed topologies and multiple common causes.
- **Strategic tempo now formalized.** #def-strategic-tempo defines $\mathcal T_\Sigma = \sum_{(i,j)} \nu_{ij} \cdot \eta_{\text{edge},ij}$ and verifies consistency with all four cases. The relationship to the schema's sector parameter: $\alpha_\Sigma \leq \mathcal T_\Sigma / \lvert E\rvert$ (persistence is bottleneck-limited, not throughput-limited). #form-strategy-complexity-cost provides the IB/MDL framework for strategy compression and derives max useful depth $d^\ast$.
- The strategic disturbance $\rho_\Sigma$ is qualitatively different from epistemic disturbance $\rho$. Epistemic disturbance is about the environment changing (physical state evolves). Strategic disturbance is about the agent's causal theory becoming invalid (the intervention-outcome mapping shifts). These can be correlated (a changing environment invalidates both model and strategy) but they're not the same quantity.
- The stochastic treatment (from track-b simulations) suggests $\rho_\Sigma / \sqrt{\mathcal T_\Sigma}$ rather than $\rho_\Sigma / \mathcal T_\Sigma$ for the steady-state strategic mismatch. If this carries over from the epistemic domain, the persistence threshold is different in the stochastic case. Whether strategic disturbance is better modeled as deterministic or stochastic drift is domain-dependent.
- The forgetting prerequisite transforms an organizational platitude ("stay adaptive") into a quantitative constraint: the rate at which an agent discounts old evidence must satisfy the exact threshold $(1-\lambda)/(2-\lambda) \gt \rho_\Sigma / R_\Sigma$, with the slow-forgetting linear form $(1-\lambda) \gt \rho_\Sigma/R_\Sigma$ as its asymptote. Institutional examples where this fails — long-running successful firms whose accumulated $n$ suppresses gain below the threshold set by a shifting competitive landscape — are the strategic analog of model-rigidity death spirals.
- **Audit 451729 (D.3) strengthen-first edit, 2026-05-12.** Earlier version of this segment used the linear approximation $\alpha_\Sigma^{ss} \approx 1-\lambda$ silently throughout (Formal Expression, Discussion, Findings Brief). The exact form derived from $1/(n_{\text{eff}}+1)$ with $n_{\text{eff}} = 1/(1-\lambda)$ is $(1-\lambda)/(2-\lambda)$; the linear approximation is the slow-forgetting limit, valid asymptotically as $\lambda \to 1$ and degrading rapidly outside that regime (~50% overestimate at $\lambda = 0.5$, ~10% at $\lambda = 0.9$). Per strengthen-first discipline, the exact form is now primary throughout the segment with the linear form retained explicitly as the high-$\lambda$ asymptote. The hard ceiling at $\rho_\Sigma \ge R_\Sigma/2$ (no $\lambda$ satisfies the exact prerequisite) was hidden by the linear approximation — surfaced now in Formal Expression and Findings Brief. Audit report: `audits/audit-451729-FINAL-2026-05-10.md` §D.3.
- **Cross-reference to NeurIPS Paper 2.** The forgetting prerequisite is sharpened in NeurIPS 2026 Paper 2 ("A Unified Convergence Theory for Non-Stationary Reinforcement Learning", `~/src/neurips/02-unified-convergence-rl/`, §App-D / `aux-decay-class`) into a **structural-class theorem on gain-decay updates**: define $\mathcal A_{\text{decay}}$ = the class of update mechanisms whose effective gain decays to zero with accumulated experience (count-accumulating Bayesian without forgetting; observation-aggregating without restart; Robbins-Monro / vanishing-step-size gradient methods). Every member of $\mathcal A_{\text{decay}}$ universally violates the persistence threshold for any positive disturbance rate. Finite-gain mechanisms (constant-step stochastic approximation, sliding windows, bounded memory, block restart) face *bidirectional* thresholds — both the forgetting prerequisite (lower bound on plasticity) and an upper bound from noise blow-up. This lifts the segment's per-mechanism claim to a class-level no-go: gain-decay mechanisms are structurally disqualified regardless of tuning. See `spikes/neurips-back-integration-2026-05-08.md` §1 Paper 2 entry 4.


---

### Source: `der-orient-cascade.md`

```yaml
---
slug: der-orient-cascade
type: derived
status: conditional
depends:
  - der-directed-separation
  - def-mismatch-signal
  - emp-update-gain
  - def-satisfaction-gap
  - def-control-regret
  - def-strategic-calibration
  - def-strategy-dag
  - schema-strategy-persistence
  - deriv-edge-credence-dynamics
  - disc-credit-assignment-boundary
  - der-causal-insufficiency-detection
  - def-value-object
stage: claims-verified
---
```


# Derived: Orient Cascade

For actuated agents, epistrophe (the corrective phase of the cycle) expands into a multi-step cascade. The resolution order is forced by information dependency: epistemic update first, then attainability assessment, then strategy evaluation, then (if needed) objective revision. Each step's input depends on the output of prior steps. The ordering is not a design choice — it's a consequence of which quantities require which others.

## Formal Expression

*[Derived (orient-cascade, from information dependency between mismatch types)]*

1. **Reduce $\delta_{\text{epistemic}}$** — understand reality.
   Update $M_t$ via #def-mismatch-signal and #emp-update-gain. Prerequisite for all purposeful evaluation, because $M_t$ appears in every subsequent formula.

2. **Evaluate $\delta_{\text{sat}}$** — is the goal achievable?
   Compute $A_O(M_t; \Pi, N_h)$ using the updated $M_t$. Requires adequate $M_t$ to assess attainability ( #def-satisfaction-gap).

3. **Evaluate $\delta_{\text{regret}}$** — is the policy suboptimal?
   Compare $A_O$ to $V_O(M_t, \pi_{\text{current}}; N_h)$ ( #def-control-regret). This step applies regardless of $\delta_{\text{sat}}$'s sign — the 2×2 diagnostic ( #def-control-regret) requires both quantities to distinguish four cases:
   - $\delta_{\text{sat}} \leq 0$, $\delta_{\text{regret}} \approx 0$: **success** — goal attainable, policy near-optimal.
   - $\delta_{\text{sat}} \leq 0$, $\delta_{\text{regret}} \gg 0$: **strategy problem** — goal attainable, policy poor → revise $\Sigma_t$.
   - $\delta_{\text{sat}} \gt 0$, $\delta_{\text{regret}} \gg 0$: **both** — goal hard AND strategy weak → revise $\Sigma_t$ first (cheaper than revising $O_t$), then reassess $\delta_{\text{sat}}$.
   - $\delta_{\text{sat}} \gt 0$, $\delta_{\text{regret}} \approx 0$: **capability limit** — already doing the best available; proceed to step 5.

4. **If $\delta_{\text{regret}}$ high, evaluate strategy calibration** — is the plan's causal model wrong?

   **(4a) Plan-level calibration (default within-L0).** Evaluate strategy-plan-confidence error $\delta_s = \hat P_\Sigma - \Phi$ — the gap between the agent's strategy-plan-confidence score and the independence-model plan value at true edge parameters. $\delta_s$ is credit-assignment-free (requires only status propagation), and its persistence is proved ( #schema-strategy-persistence, Prop B.5 in #deriv-edge-credence-dynamics). This is the cheapest operational signal, but its persistence guarantee is within the **independence model (L0)** of the Correlation Hierarchy ( #def-strategy-dag): $\delta_s \to 0$ means $\hat P_\Sigma$ has converged to $\Phi$, not to actual plan success probability. When the DAG is causally insufficient, $\Phi$ itself is a biased target. Step 4c checks whether this is the binding regime.

   **(4b) Edge-level localization (when credit assignment is available).** When sufficient observability and attribution quality exist (Level 1+ per #disc-credit-assignment-boundary), the agent can compute per-edge residuals $\delta_{\text{strategic}}$ ( #def-strategic-calibration) to localize which edges need revision. $\delta_{\text{strategic}}$ provides finer-grained diagnostics but its persistence is open and it requires the credit-assignment machinery that $\delta_s$ avoids. Step 4b is optional — it improves diagnostic resolution but is not required for the cascade's corrective function.

   **(4c) Causal-sufficiency check (L0→L1 escalation).** If persistent $\delta_s \approx 0$ coincides with persistent negative plan-outcome residuals ($y_G \lt \hat P_\Sigma$ on average, after edge credences have converged), this is evidence that the DAG is causally insufficient and L0 calibration is converging to a biased target. The diagnostic is pairwise sibling covariance under an augmented test ( #der-causal-insufficiency-detection): positive covariance among sibling edges, at timescales where each edge's individual credence has stabilized, localizes where a latent common cause is missing. When the signal for L1 augmentation is present, step 4c directs the agent to add common-cause nodes ( #def-strategy-dag Correlation Hierarchy) *before* escalating via 5a–5d. Running the cascade's exploitation recommendations under L0 when the signal for L1 is present compounds miscalibration — the agent acts confidently on a model whose own residual structure is telling it the model is wrong.

   *Practical sensitivity.* Step 4c is the unique broadly-available L0→L1 diagnostic ( #der-causal-insufficiency-detection no-go), but its effective power depends on signal-to-noise: small samples, weak common-cause effects, or noisy residuals can produce false negatives, and edge-credence drift can mimic sibling covariance. The convergence framing — "after edge credences have converged" — is a precondition, not a guarantee: in non-stationary environments where per-edge credences keep drifting, the trigger may never cleanly fire and L1 augmentation should be considered the default rather than gated on 4c's signal ( #def-strategy-dag Correlation Hierarchy). Formal preconditions (joint observability, per-edge credence stabilization, approximate stationarity over the test window) and detection scope live in #der-causal-insufficiency-detection; consult them before treating a 4c null as evidence of L0 sufficiency.

5. **If $\delta_{\text{sat}} \gt 0$ persists** — escalate before revising $O_t$.

   **Under C1 (the canonical default), $\delta_{\text{sat}} \gt 0$ means *locally stuck*, not *globally infeasible*** ( #def-value-object). Before concluding the objective is wrong, the agent should check whether the gap reflects a limitation of the current analysis rather than genuine infeasibility:

   **(5a)** Check whether $M_t$ correction changes the feasibility assessment — a wrong model may make an achievable goal appear unattainable.

   **(5b)** Check whether a richer policy class $\Pi$ would close the gap — structural $\Sigma_t$ adaptation (expanding the strategy space, not just revising edge credences). This includes L1 augmentation of the strategy DAG ( #def-strategy-dag Correlation Hierarchy): if step 4c detected causal insufficiency, adding common-cause nodes here is the structural repair.

   **(5c)** Check whether convention escalation reveals recovery paths — evaluating under C2 (receding-horizon) may show $\delta_{\text{sat}}^{\text{RH}} \leq 0$ for a goal that appeared unattainable under C1.

   **(5d)** If $\delta_{\text{sat}} \gt 0$ persists across $M_t$ correction, $\Pi$ expansion (including L1 augmentation), and convention escalation — **revise $O_t$**.

   The cascade's ordering ensures objective revision is the last resort, not the first response to unmet goals. The agent reaches step 5d only after exhausting the alternatives that the satisfaction-gap disambiguation table ( #def-satisfaction-gap) identifies: wrong $M_t$, narrow $\Pi$, short $N_h$, and only then genuinely infeasible goal. When step 5d is performed by a principal the revised $O_t$ is externally sourced (an actuated agent); when it is *internalized* — performed by the agent on itself — it becomes the self-actuation operator, which — as a conditional, scoped no-go ( #deriv-self-actuation-grounding) — is well-formed only under a grounding condition: a non-degenerate self-actuator must ground objective-revision on a non-objective terminal invariant, not on an objective-functional.

**Derivation.** Each step's input depends on prior steps' outputs:
- You cannot evaluate strategy quality with a broken reality model (step 3 requires step 1)
- You cannot distinguish "locally bad strategy" from "locally unattainable goal" without both $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ (step 3 requires step 2)
- You cannot localize strategy failures (4b) without first detecting plan-level miscalibration (4a)
- You cannot diagnose causal insufficiency (4c) until after edge credences have had time to converge (4a), because the diagnostic signal — persistent negative plan-outcome residuals — requires $\delta_s \approx 0$ to be separable from ordinary calibration error
- You should not revise the objective until you've verified that improving $M_t$, $\Pi$ (including L1 augmentation when 4c signals it), and $N_h$ cannot close the gap (step 5 requires steps 3–4 and the escalation substeps)

The ordering is forced by information dependency. The split of step 4 into 4a/4b/4c reflects three distinct diagnostic levels: 4a gives a within-L0 persistence signal (plan-level tracking via $\delta_s$), 4b gives within-L0 edge-level localization when credit assignment is available (Level 1+), and 4c exits L0 entirely when the independence model is the binding constraint. The escalation substeps in step 5 reflect the satisfaction-gap disambiguation ( #def-satisfaction-gap): multiple causes of $\delta_{\text{sat}} \gt 0$ must be ruled out before the agent concludes the goal itself is wrong. L1 augmentation ( #def-strategy-dag Correlation Hierarchy) enters 5b as a structural $\Sigma_t$ adaptation when 4c's signal is present.

**Convention hierarchy and diagnostic power.** The 2×2 diagnostic and the inferences drawn from it are relative to the continuation convention in the value object ( #def-value-object), which defines a hierarchy of three conventions with a proved monotonicity result.

Under **C1** (one-step improvement, canonical default), $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ are one-step-improvement quantities. A multi-step recoverable objective may appear locally unattainable ($\delta_{\text{sat}} \gt 0$) because continuation is frozen at $\pi_{\text{current}}$. The "capability limit" quadrant ($\delta_{\text{sat}} \gt 0$, $\delta_{\text{regret}} \approx 0$) means *locally stuck* — the agent may be globally recoverable but cannot see the recovery path from one-step analysis.

Under **C2** (receding-horizon, $N_r$-step replanning), the diagnostics capture multi-step recovery potential. An objective that appeared unattainable under C1 may show $\delta_{\text{sat}}^{\text{RH}} \leq 0$ because replanning reveals a viable path. The "capability limit" quadrant means *stuck with $N_r$-step replanning* — stronger evidence of genuine difficulty.

Under **C3** (Bellman), the diagnostics are global. $\delta_{\text{sat}}^{\text{B}} \gt 0$ means the goal is genuinely infeasible given $(M_t, \Pi, N_h)$ — no policy can achieve it. The "capability limit" quadrant is a definitive diagnosis: the agent is optimally pursuing an infeasible goal (modulo model error in $M_t$). This is the inference the cascade was designed to support; C1 and C2 provide progressively weaker versions of it.

The monotonicity ( #def-value-object): $\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$. Every "unattainable" diagnosis under C3 persists under C1 and C2. A C1 "unattainable" diagnosis may be overturned by C2 or C3 (the goal is reachable with replanning or globally optimal play). The cascade's *ordering* is convention-independent (forced by information dependency). The *inferential force* at each step scales with the convention: C1 gives local heuristics, C2 gives moderate-horizon diagnostics, C3 gives global conclusions.

## Epistemic Status

The cascade **ordering** is *exact*: it is a logical consequence of which quantities appear in which formulas. Steps 1-2 (epistemic update, attainability assessment) rest on well-typed quantities ( #def-mismatch-signal, #def-satisfaction-gap) and exact derivation. Step 3 (control regret) is exact ( #def-control-regret). Step 4a (plan-level calibration via $\delta_s$) is grounded in a proved quantity — the sector condition transfers to $\delta_s$ (Prop B.5 in #deriv-edge-credence-dynamics) — but the formal guarantee is *within the L0 independence model*: $\delta_s \to 0$ means convergence to $\Phi$, which equals actual plan success only when the DAG is causally sufficient. Step 4b (per-edge localization via $\delta_{\text{strategic}}$) inherits strategic-calibration's discussion-grade status — the credit-assignment problem and execution-fidelity requirement are acknowledged but unresolved ( #def-strategic-calibration, Epistemic Status). Step 4c (causal-sufficiency check) is the mechanism for exiting L0 when L1 is the binding regime; it is *robust-qualitative* — the diagnostic logic is sound ( #der-causal-insufficiency-detection), but sensitivity depends on how cleanly the agent can separate sibling-covariance signal from edge-credence noise at convergence. Step 5's escalation substeps (5a-5c) are derived from the satisfaction-gap disambiguation table ( #def-satisfaction-gap); step 5d (objective revision) is the residual case after alternatives are exhausted. The ordering of all steps is forced by information dependency (each step's input depends on prior steps' output). What is NOT derived is the *timing* — how long the agent should spend on each step before proceeding, and how long $\delta_s \approx 0$ must persist before 4c's signal is trusted.

The **convention hierarchy** ( #def-value-object) is *exact*: the three conventions (C1, C2, C3) are definitions, and the monotonicity result is a direct consequence of "better continuation policy yields higher expected value." The diagnostic implications table states what each convention's quantities mean by construction. The cascade's inferential force at steps 2-5 scales with the convention but the ordering is convention-independent.

## Discussion

**$G_t$ complexity bounded by $M_t$ capacity.** $\Sigma_t$'s evaluable complexity is bounded by $M_t$'s ability to observe which strategy edges are intact. An agent with poor model sufficiency ($S(M_t) \ll 1$) cannot meaningfully evaluate a complex $\Sigma_t$ — the strategic calibration residual requires adequate $M_t$ to distinguish "edge prediction wrong" from "observation too noisy to tell."

This creates a **virtuous cycle**: better $M_t$ → richer evaluable $\Sigma_t$ → better-directed action → faster $M_t$ improvement. And a **vicious one**: degraded $M_t$ → forced strategy simplification → cruder action → further $M_t$ degradation. The vicious cycle is the strategic analog of the death spiral described in the persistence condition ( #result-persistence-condition) — the agent loses the capacity to maintain complex plans, which reduces the quality of its actions, which further degrades its model.

**Connection to Boyd's OODA.** The orient cascade is the formal analog of Boyd's "Orient" — not just model updating, but the structured interaction between reality-understanding and strategy. Boyd's insight was that Orient is the critical step, not Decide. The cascade provides a mathematical mechanism consistent with this insight: Orient resolves the information dependencies that make Decide meaningful. An agent that skips to Decide (strategy revision) without adequate Orient (model update + attainability assessment) will revise its strategy based on stale or incorrect beliefs. Whether the dependency structure in the cascade captures the actual cognitive process Boyd described is an empirical question.

**Timescale structure.** The cascade implies a natural timescale ordering for the different update types:

$$\nu_{\text{epistemic}} \gg \nu_{\text{edge-update}} \gg \nu_{\gamma\text{-reclassify}} \gg \nu_{\text{prune/graft}} \gg \nu_{O\text{-revision}}$$

Weight updates are frequent (every observation). Combination-type reclassification is rare (needs strong structural evidence). Pruning/grafting is rarer still (abandon or create causal hypotheses). Objective revision is rarest (change what you want, not how you get it). This ordering is an empirical observation for many agent populations, consistent with the cascade but not derived from it.

## Working Notes

- The cascade as stated is sequential. In practice, agents may run steps in partial overlap — beginning to assess $\delta_{\text{sat}}$ before $M_t$ is fully updated, or revising edges while still processing observations. The cascade describes the *logical* dependency, not the *temporal* scheduling. An agent that parallelizes steps must still respect the dependencies (don't finalize strategy revision using a stale $M_t$).
- The resource allocation question (how much of the agent's tempo budget to spend on each step) is open and may be domain-dependent. In fast-changing environments, the agent may need to truncate early steps to keep up. In stable environments, the agent can spend more time on deep strategic evaluation.
- The virtuous/vicious cycle between $M_t$ quality and $\Sigma_t$ evaluable complexity is structurally motivated but not formally derived. Formalizing it would require a coupled dynamics model — possibly an extension of the persistence framework to the $(M_t, \Sigma_t)$ pair.
- **Strategy-maintenance status (updated).** The cascade's ORDERING is exact — forced by information dependency. The cascade's CONTENT for steps 3-5 has progressed: #disc-credit-assignment-boundary characterizes the tractable/intractable boundary and establishes that persistence does not require credit assignment (Prop B.5); #deriv-edge-credence-dynamics verifies sector conditions for four topologies; #hyp-edge-update-via-gain has a default signal function candidate (gradient-based, satisfying directional fidelity). What remains domain-specific: the choice of signal function implementation, execution-fidelity monitoring, and handling of correlated failures (where $\hat P_\Sigma$ overestimates — #def-strategy-dag). The theory now provides the structural requirements and a default scheme; specific implementations are engineering, parallel to how the gain principle provides $\eta^\ast$ while Kalman/TD-learning/etc. are implementations.


---

