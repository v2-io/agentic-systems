# Deriving Purposeful Agency from First Principles (v2)

**Status**: Clean rewrite from the v1 spike's Part 11.8 skeleton, incorporating all Codex review corrections. The v1 spike (spike-purposeful-agent-derivation.md) preserves the exploratory reasoning; this document is the tightened result.

**Date**: 2026-03-09 **Authors**: Joseph Wecker + Claude Opus 4.6

**Methodological discipline**: Every step is either *derived* (mathematical necessity) or an explicit *scope narrowing* (restriction with justification). Scope narrowings mark divergence points for alternative theories — clearly labeled unexplored paths.

---

## 0. Starting Point: Section I Agents

AAD Section I (from TFT) gives us an agent with complete state M_t, observations o_t, actions a_t, mismatch δ_t, gain η*, tempo T, and the persistence condition. The agent tracks reality. It may act effectively (TF-07), but its policy π(M_t) serves no declared purpose — the "value" term in TF-08's policy objective is a placeholder with no formal content.

**The question**: What minimal formal extension makes the agent *purposeful*, and what structure must that extension have?

---

## 1. The Complete Agent State

### 1.1 Lifting the state (Formulation)

TF-03 defines M_t as the agent's complete internal state. To introduce purpose, we must either embed it in M_t (making M_t do double duty) or lift the complete state.

We lift. Define the **complete agent state**:

*[Formulation]*
$$X_t = (M_t, G_t)$$

where:
- $M_t \in \mathcal{M}$ — the **epistemic substate**: compressed beliefs about reality (TF-03, unchanged)
- $G_t \in \mathcal{G}$ — the **purposeful substate**: what the agent wants and (to whatever degree internalized) how it plans to get it

TF-03's completeness claims now apply to $X_t$. Section I agents have $G_t = \emptyset$ — the purposeful substate is empty, and $X_t$ reduces to $M_t$.

### 1.2 Update dynamics

In TFT's event-driven form (TF-04):

*[Derived (from TF-02 temporal axiom + TF-03 completeness on X_t)]*

The policy:
$$a_t = \pi(X_t) = \pi(M_t, G_t)$$

On event $e_\tau$:
$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$$
$$G_{\tau^+} = f_G(G_{\tau^-}, M_{\tau^+}, e_\tau)$$

Between events (autonomous evolution — deliberation, planning):
$$\dot{M} = g_M(M)$$
$$\dot{G} = g_G(G, M)$$

**Key structural property**: $f_M$ has no $G_t$ dependence. $f_G$ depends on $M_t$. This is the **directed separation** of update functions. It holds because observations arrive from the environment, which doesn't know or care about the agent's goals.

**Closed-loop trajectory**: $M_t$'s trajectory DOES depend on $G_t$, because $\pi(M_t, G_t)$ determines $a_t$, which affects future observations. The directed separation is about the *update functions*, not the *trajectories*.

**No separate "feedback" term**: $G_t$'s update sources are $(G_{\tau^-}, M_{\tau^+}, e_\tau)$. No additional "feedback_t" is needed — $M_{\tau^+}$ already encodes the agent's updated understanding of reality (including progress toward goals), and $e_\tau$ is the raw event. If $X_t$ is truly complete, everything the agent can know is in $(M_t, G_t)$ plus the incoming event.

---

## 2. Introducing Purpose: O_t Fills the Gap in TF-08

### 2.1 The existing gap

TF-08's unified policy objective:
$$\pi^*(M_t) = \arg\max_a \left[\mathbb{E}[\text{value}(a) \mid M_t] + \lambda(M_t) \cdot \text{CIY}(a; M_t)\right]$$

The "value" term is an unexplained placeholder. TFT acknowledges this — it says the structural form of the trade-off is identified but the value function is domain-specific and not derived within TFT.

### 2.2 O_t as the value parametrization (Definition)

*[Definition (objective)]*

$O_t$ is the component of $G_t$ that parametrizes the value function.
It gives formal content to TF-08's "value" term:

$$\text{value}(a \mid M_t) = \mathbb{E}[V_{O_t}(\tau) \mid M_t, a]$$

where $V_{O_t}: \text{trajectories} \to \mathbb{R}$ is the **induced value functional** — a scalar measure of how well a trajectory satisfies the objective.

### 2.3 Objective representations (ordered by expressiveness)

$O_t$ can take multiple forms, all unified by the induced $V_{O_t}$:

| $O_t$ representation | $V_{O_t}(\tau)$ | Example |
|---|---|---|
| Point target $r \in S$ | $-\Verts_T - r\|$ | PID setpoint |
| Target region $R \subseteq S$ | $\mathbb{1}[s_T \in R]$ | "reach any safe state" |
| Constraint set $\{g_i(s) \leq 0\}$ | $-\sum \max(0, g_i(s_t))$ | "don't violate SLA" |
| Utility $U: S \to \mathbb{R}$ | $\sum_t \gamma^t U(s_t)$ | RL reward |
| Trajectory functional $J$ | $J(\tau)$ | "migrate with zero downtime" |

The **trajectory functional** is the most general: it evaluates the entire path, not just the endpoint. Reference signals, utilities, and constraints are special cases. This handles path-dependent objectives ("ship this feature without breaking auth") that point targets cannot express.

**Type stability**: Regardless of $O_t$'s internal form, the interface to the rest of the theory is always $V_{O_t}: \text{trajectories} \to \mathbb{R}$. This gives a uniform type for objective evaluation.

---

## 3. Strategy as an Independent Dimension

### 3.1 Objective ≠ strategy (Definitional observation)

$O_t$ specifies *what* the agent wants (the evaluation criterion).
But it says nothing about *how* to achieve it. Two agents with identical $O_t$ may pursue radically different approaches.

**Strategy** ($\Sigma_t$) is the component of $G_t$ that represents the agent's theory of *how* its actions produce progress toward $O_t$.

The distinction is not dynamic (it doesn't follow from timescale separation) — it is **ontological**: "what to want" and "how to get it" are different kinds of information that answer different questions and are evaluated by different criteria.

$G_t$ decomposes:
$$G_t = (O_t, \Sigma_t)$$

### 3.2 Strategy representations (ordered by expressiveness)

| $\Sigma_t$ form | What it encodes | Example |
|---|---|---|
| None (reactive) | $\pi$ is implicit in $M_t$ | PID controller, reflex |
| Cached policy | Learned mapping $s \to a$ | Trained RL agent in exploitation |
| Subgoal sequence | Waypoints with ordering | Project plan, recipe |
| Causal DAG | Action-outcome chains with confidences | Military campaign, complex software feature |

### 3.3 When does the agent need richer Σ_t?

A reactive agent ($\Sigma_t = \emptyset$) works when:
- The mapping from actions to $V_{O_t}$ improvement is approximately monotone (greedy on the objective gradient works)
- The environment has no prerequisite structure (no "do A before B")
- A single action step suffices (no causal chains)

When any of these fail, the agent needs a richer $\Sigma_t$. This is the **purposeful analog of TF-10**: just as $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$ triggers M_t structural adaptation, inadequacy of $\Sigma_t$'s representation for the environment's causal complexity triggers strategy structural adaptation.

---

## 4. The Causal Hierarchy and Level 2 Access

### 4.1 The causal hierarchy theorem (Mathematical fact)

Pearl's causal hierarchy (Bareinboim et al. 2022): the three levels (association, intervention, counterfactual) form a strict hierarchy. Level 2 quantities cannot in general be computed from Level 1 data alone.

### 4.2 Consequence for purposeful agents

Selecting actions based on consequences requires evaluating $\mathbb{E}[V_{O_t}(\tau) \mid M_t, do(a)]$ — an interventional query. This requires Level 2 *knowledge*: the agent must know (or learn) how its actions causally affect outcomes.

*[Scope Narrowing]*

We restrict to agents that must acquire or refine Level 2 knowledge during operation — as opposed to agents with pre-compiled Level 2 knowledge (PID controllers, hardcoded policies) where the designer did the causal reasoning at design time.

**Justification**: Pre-compiled controllers are purposeful but their causal structure is externally supplied. The interesting case — and the one relevant to AI agents, organizations, and adaptive systems generally — is agents that must learn the causal structure of their environment through interaction.

### 4.3 The feedback loop provides access to interventional data

*[Derived (from TF-02 + temporal ordering)]*

An agent embedded in the feedback loop generates interventional data by construction:
1. The agent selects $a_t$ (TF-07)
2. $a_t$ causally affects the environment (TF-01)
3. $o_{t+1}$ arrives after $a_t$ (temporal ordering, TF-02)
4. The mismatch $\delta_t$ conditioned on $a_t$ carries interventional information

The loop provides **access to interventional data**, which the agent can use to build Level 2 knowledge. This is true regardless of the agent's internal architecture — a transformer, a Bayesian network, or a lookup table all receive the same interventional data from the loop.

**Precision**: "Access to interventional data" is weaker than "achieves Level 2 reasoning." The loop provides the *data*; whether the agent *exploits* it for Level 2 reasoning depends on its update mechanism and model class. A Kalman filter with LQR has access to interventional data but doesn't exploit it (separation principle — TF-02 notes this). The claim is about data availability, not reasoning capacity.

### 4.4 LLM training data as causal priors

*[Discussion — not derived]*

LLMs trained on natural language absorb causal priors from causally-structured text ("if you drop the glass, it breaks"). This is not automatically-identified interventional structure — text corpora mix experimental results, observational reports, speculation, and fiction. The causal content is *noisy prior knowledge* from a mixed provenance of sources, not clean interventional data.

The information bottleneck (TF-03) predicts that the model retains whatever structure has predictive power, and causal structure does have predictive power for language. But the epistemic status of the absorbed causal knowledge is *prior* (plausible, not verified), not *derived* (from the agent's own interventions).

An LLM in the feedback loop has both: causal priors from training AND access to interventional data from the loop. The priors accelerate learning; the loop provides ground-truth verification.

---

## 5. The Cost Inequality for Explicit Strategy

### 5.1 Two modes of purposeful action

An agent with Level 2 data access (from the loop) can pursue $O_t$ in two ways:

**Loop-based (model-free)**: Act, observe consequences, adjust.
Level 2 knowledge is acquired implicitly through repeated act-observe cycles. Cost: real actions, real time, real consequences.

**Model-based (explicit $\Sigma_t$)**: Build an internal model of action-outcome causal structure. Evaluate actions through mental simulation ("what would happen if I do(X)?"). Cost: computation, model maintenance, model inaccuracy.

### 5.2 The cost inequality (Derived via #post-temporal-optimality)

*[Derived]*

The agent benefits from maintaining an explicit $\Sigma_t$ when:

$$C_{\text{plan}}(\Sigma_t) + C_{\text{maintain}}(\Sigma_t) \lt C_{\text{explore}}(\text{loop-only}) + C_{\text{repair}}(\text{loop-only})$$

where:
- $C_{\text{plan}}$: cost of constructing and querying $\Sigma_t$ (deliberation — TF-09)
- $C_{\text{maintain}}$: cost of keeping $\Sigma_t$ current as conditions change
- $C_{\text{explore}}$: cost of discovering action consequences through physical trial-and-error
- $C_{\text{repair}}$: cost of reversing failed actions

When this inequality holds, explicit $\Sigma_t$ is **temporally optimal** ( #post-temporal-optimality): it achieves the same Level 2 knowledge in less time. The temporal optimality axiom then selects for agents with explicit strategy representation.

**What this makes precise**: TF-07's action fluency concept and TF-09's deliberation cost are now load-bearing for the purposeful layer. The agent invests in explicit $\Sigma_t$ exactly when planning (deliberation) is cheaper than experimentation (action + repair). This is a concrete inequality, not a scope-narrowing appeal.

**When loop-only wins**: In environments where actions are cheap, consequences are immediate, failure is reversible, and the environment is stationary during exploration, the RHS is small and explicit $\Sigma_t$ may not be worth maintaining. Model-free RL in fast simulators is the canonical case. These agents are purposeful but out of scope for the explicit-strategy analysis.

---

## 6. Properties of Multi-Step Strategies

For agents with explicit $\Sigma_t$ (per Section 5), what properties does $\Sigma_t$ exhibit?

### 6.1 Additive log-confidence in causal chains (Derived)

Consider a causal chain of $n$ steps, where step $i$ succeeds with conditional probability $P(E_i \mid E_{\lti})$:

*[Derived]*
$$\log P(\text{chain}) = \sum_{i=1}^{n} \log P(E_i \mid E_{\lti})$$

Since each term is non-positive, chain confidence decays monotonically with depth. The rate of decay depends on the conditional probabilities.

**Special case**: When steps are independent with uniform probability $p$: $P(\text{chain}) = p^n$, giving exponential decay. This is the simplest case, not the general result.

**Robust qualitative conclusion**: Longer causal chains are less confident than shorter ones, all else equal. This creates structural pressure toward:
- Short chains (simple strategies) where feasible
- Parallel paths (fallback options if a link fails)
- High-confidence links (investing in certainty at critical steps)
- Monitoring (detecting link failure early to trigger replanning)

These are *mathematical consequences*, not design recommendations.

### 6.2 Combination semantics (Scope narrowing)

When multiple causal paths converge on a single outcome, how do their contributions combine?

*[Scope Narrowing]*

We restrict to environments where causal combination is approximately conjunctive (AND: all parents required) or disjunctive (OR: any parent sufficient), without strong interaction effects.

**Justification**: This restriction converged across three independent formalism attempts (track-a-intent-dag/). It captures the dominant structure in most strategic/planning domains. The excluded case — environments with strong complementarity, substitutability, or interaction effects between causes — would require richer combination rules (general CPTs, interaction terms). This is a tractability restriction, not a claim about all environments.

Under this restriction, the strategy DAG has AND/OR nodes with single-parameter edges (confidence weight $p_{ij} \in [0,1]$).

---

## 7. Three Mismatch Types

With $X_t = (M_t, G_t)$ and $G_t = (O_t, \Sigma_t)$, three distinct kinds of discrepancy arise:

### 7.1 δ_epistemic: Reality model error

$$\delta_{\text{epistemic}} = o_t - \hat{o}_t$$

Unchanged from Section I. The agent's predictions about reality don't match observations. **Update source**: observations. **Timescale**: fastest. **Correction**: gain-weighted model update (TF-06).

### 7.2 δ_objective: Goal-satisfaction gap

$$\delta_{\text{objective}} = V_{O_t}^* - \mathbb{E}[V_{O_t}(\tau) \mid M_t, \pi]$$

The gap between the best achievable objective value and the expected value under the current policy and model. This is **regret** relative to the objective.

**Precision requirements** (from Codex review):
- $V_{O_t}^\ast$ is defined as $\sup_{\pi' \in \Pi} \mathbb{E}[V_{O_t}(\tau) \mid M_t, \pi']$ over a specified policy class $\Pi$ and horizon $N_h$
- This parallels TF-10's operational sufficiency $S_\Pi$ (which also uses finite horizon and policy class)
- $\delta_{\text{objective}}$ being large is *normal* — it's why the agent is acting. The pathology is *unchanging* $\delta_O$ despite sustained action.

### 7.3 δ_strategic: Strategy calibration residual

$$\delta_{\text{strategic}} = \mathbb{E}[\text{progress} \mid \Sigma_t, M_t, a_{1:t}] - \text{observed progress}$$

The strategy predicts that executing its plan should produce progress toward $O_t$ at a certain rate. The calibration residual measures the systematic deviation between predicted and observed step outcomes.

**This is a second-order inference**: $\delta_{\text{strategic}}$ cannot be computed from a single observation. It requires accumulating evidence over multiple action cycles that the strategy's predictions are systematically miscalibrated.

**Conditioning matters** (from Codex review): $\delta_\Sigma$ should be conditioned on $O_t$ and execution fidelity. Otherwise it conflates:
- Bad strategy (the plan is wrong)
- Bad execution (the agent didn't follow the plan)
- Wrong objective calibration (the progress metric doesn't match $O_t$)

### 7.4 Resolution ordering (Derived)

$\delta_{\text{epistemic}}$ must be resolved before $\delta_{\text{strategic}}$ is meaningful.

**Argument**: $\delta_{\text{strategic}}$ requires evaluating whether the strategy's predictions match reality. This evaluation uses $M_t$. If $M_t$ is inaccurate ($\delta_{\text{epistemic}}$ is large), the evaluation itself is unreliable — the apparent lack of progress might be a measurement error, not a strategy failure.

More fundamentally: G_t's effective complexity is bounded by M_t's evaluative capacity. An agent with poor $S(M_t)$ cannot meaningfully evaluate a complex $\Sigma_t$ because it can't observe which edges are intact. The strategy's *evaluable* complexity is:

$$\text{effective\-complexity}(\Sigma_t) \leq f(S(M_t))$$

**Resolution ordering**:
1. Reduce $\delta_{\text{epistemic}}$ (understand reality — Orient)
2. Evaluate $\delta_{\text{objective}}$ (assess goal-state gap)
3. Evaluate $\delta_{\text{strategic}}$ (assess strategy effectiveness)
4. If $\delta_{\text{strategic}}$ high: revise $\Sigma_t$
5. If persistent across $\Sigma_t$ revisions: revise $O_t$

This IS the **orient cascade**, derived from the logical dependency between mismatch types rather than assumed as a design pattern.

---

## 8. Directed Separation (Derived)

Restated precisely with the X_t formulation:

**The epistemic update function $f_M$ is $G_t$-independent**:
$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$$ No $G_t$ term. Observations arrive from the environment, which doesn't know the agent's goals. How the agent *interprets* the observation (through $f_M$) depends on $M_t$ and the event, not on what the agent wants.

**The purposeful update function $f_G$ depends on $M_t$**:
$$G_{\tau^+} = f_G(G_{\tau^-}, M_{\tau^+}, e_\tau)$$ Strategy evaluation requires the reality model. Goal revision may be triggered by what $M_t$ reveals about feasibility.

**Action couples all three**:
$$a_t = \pi(M_t, G_t)$$ Actions depend on both substates. Actions affect the environment, which changes future observations, which update $M_t$.

**The precise claim**: $f_M$ is independent of $G_t$. The closed-loop *trajectory* of $M_t$ depends on $G_t$ through $\pi \to a_t \to o_{t+1}$. This is conditional independence of the update function given action and observation, not unconditional dynamical independence.

---

## 9. Strategy Persistence (Proposed Theorem Schema)

### 9.1 The structural parallel

$M_t$ has a persistence condition: $\mathcal{T} \gt \rho / \Vert\delta_{\text{critical}}\Vert$.
The sector-condition mathematics (Appendix A) that proves this depends on:
- A mismatch state (δ)
- A correction function $F$ satisfying the sector condition
- Bounded disturbance $\Vertw(t)\Vert \leq \rho$

None of these are specific to the epistemic substate. If we can define analogous objects for $\Sigma_t$, the same mathematics applies.

### 9.2 What's needed for a full theorem

*[Proposed Theorem Schema]*

**If** strategic update dynamics satisfy:
- (SA1) Zero correction at zero strategic mismatch
- (SA2') Local sector condition on the strategic correction function
- Bounded strategic disturbance $\Vert\rho_\Sigma\Vert \leq \rho_{\Sigma,\text{max}}$

**Then** strategy persists iff $\alpha_\Sigma \gt \rho_\Sigma / R_\Sigma$.

**What's missing** (genuine future work):
1. **Strategic mismatch state**: What is the "δ" for $\Sigma_t$?
   Candidate: the calibration residual from §7.3, aggregated across all strategy edges.
2. **Strategic correction function**: How does $\Sigma_t$ update in response to strategic mismatch? Candidate: edge confidence revision via the gain principle, but this needs formalization.
3. **Strategic disturbance**: What introduces new strategic mismatch?
   Candidate: environmental changes that invalidate causal links (requirements change, resources become unavailable, adversary acts).
4. **Sector condition verification**: Does the strategic correction function actually satisfy the sector condition? This depends on the specific update rule, which isn't yet defined formally.

Until these are defined, strategy persistence is a *schema* — "if the assumptions hold, the conclusion follows" — not a *theorem*.

---

## 10. Summary: Derived vs. Scope-Narrowed

**Derived** (mathematical necessity):
1. Complete state lifts to $X_t = (M_t, G_t)$ — from TF-03 completeness
2. $O_t$ parametrizes TF-08's value term — fills an acknowledged gap
3. $O_t$ (what) and $\Sigma_t$ (how) are ontologically distinct — different kinds of information answering different questions
4. Causal hierarchy theorem: Level 2 knowledge is needed for purposeful action based on consequences
5. The feedback loop provides access to interventional data (TF-02)
6. Cost inequality: explicit $\Sigma_t$ is temporally optimal when $C_{\text{plan}} + C_{\text{maintain}} \lt C_{\text{explore}} + C_{\text{repair}}$
7. Additive log-confidence: chain confidence decays monotonically with depth ($p^n$ is the independent-uniform special case)
8. Directed separation: $f_M$ is $G_t$-independent; coupling through action channel only
9. Three mismatch types from the $X_t = (M_t, (O_t, \Sigma_t))$ structure, with resolution ordering from logical dependency
10. Orient cascade: derived from the mismatch resolution ordering
11. $\Sigma_t$ evaluable complexity bounded by $M_t$ capacity

**Scope narrowings** (explicit restrictions):
A. Agents that must learn Level 2 knowledge during operation (excludes
   pre-compiled controllers)
B. AND/OR environments with approximately conjunctive/disjunctive
   causal combination (excludes strong interaction effects)

**Proposed theorem schema** (awaiting formalization):
- Strategy persistence condition (§9)

**Promoted from scope narrowing to derived** (compared to v1):
- The O_t/Σ_t split is now *definitional* (ontologically distinct information types), not a scope narrowing for timescale-separated agents. Timescale separation (ν_O ≪ ν_Σ for many agents) is a further *empirical observation* about dynamics, applicable as an additional scope narrowing when analyzing specific agent populations.
- The need for explicit $\Sigma_t$ is now derived from a *cost inequality* via temporal optimality, not a scope-narrowing appeal.

---

## 11. Implications for Theory Structure

### 11.1 Proposed Section II ordering

1. $X_t = (M_t, G_t)$ — Formulation (§1)
2. $O_t$ as value parametrization — Definition (§2)
3. Objective representations and $V_{O_t}$ — Definition (§2.3)
4. $\Sigma_t$ as independent dimension — Definition (§3)
5. Strategy representations — Definition (§3.2)
6. Causal hierarchy theorem + scope to learning agents — Derived + Scope (§4)
7. Feedback loop provides interventional data access — Derived (§4.3)
8. Cost inequality for explicit $\Sigma_t$ — Derived (§5)
9. Additive log-confidence — Derived (§6.1)
10. Scope: AND/OR environments — Scope (§6.2)
11. Strategy DAG formalism — Definition
12. Directed separation — Derived (§8)
13. Three mismatch types — Derived (§7)
14. Orient cascade — Derived (§7.4)
15. Strategy persistence — Proposed theorem schema (§9)

### 11.2 What changed from v1

- State completeness resolved: $X_t = (M_t, G_t)$ with clean recursion
- O_t/Σ_t split moved EARLY (ontological, not dynamic)
- O_t given as parametrization of TF-08's value term (not from scratch)
- $V_{O_t}$: trajectory functional gives type-stable interface
- Level 2 claim weakened to "access to interventional data"
- LLM training data qualified as "causal priors, not identified structure"
- Cost inequality replaces scope-narrowing for explicit Σ_t
- p^n replaced with additive log-confidence as the general result
- Directed separation stated precisely (f_M independent, trajectory not)
- Strategy persistence downgraded to proposed theorem schema
- Timescale separation (ν_O ≪ ν_Σ) removed from the derivation chain — available as an additional scope narrowing but not load-bearing

### 11.3 What's still open

- Strategic error state, correction function, and disturbance class (needed for §9 to become a theorem)
- Edge update rule formalization (gain principle applied to strategy edges — plausible but not independently validated)
- DAG acyclicity (assumed, not derived — real control loops are cyclic;
  acyclicity holds after time-unrolling)
- Cognitive cost of maintaining $\Sigma_t$ (no β analog yet for the strategy information bottleneck)
- Edge identifiability in confounded domains (resolved in software where genuine interventions are available; open in general)
- Whether "agents modifying their own observation channels" (code quality as observation infrastructure) is general enough for Section I or properly belongs in Section IV
