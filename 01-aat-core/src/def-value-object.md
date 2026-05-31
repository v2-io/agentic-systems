---
slug: def-value-object
type: definition
status: exact
depends:
  - form-objective-functional
  - form-agent-model
  - der-directed-separation
  - def-model-sufficiency
stage: deps-verified
---

# Definition: Value Object

The objective functional ( #form-objective-functional) alone is abstract — it evaluates trajectories without specifying *which* trajectory the agent should be reasoning about. The **value object** $V_O$ turns the objective into a decision-making tool. Given the agent's current model, a policy, and a horizon, $V_O$ is the *expected trajectory value* if the agent follows the policy from now to the horizon, evaluated against the objective. The companion **action-value object** $Q_O$ is the same construct conditioned on intervening with a specific first action and then following a continuation policy. The $do(\cdot)$ in $Q_O$ is explicit — this is an interventional query ( #der-causal-hierarchy-requirement), not conditioning on observed action choice.

The framework spends time on **causal validity** of the value object. Two structural mechanisms ensure it. First, the do-operator handles current-action confounding: because the action-value uses an intervention rather than a condition, the dependence of the action on the agent's selection mechanism is severed. Second, the continuation policy $\pi_{\text{cont}}$ is a *parameter*, not a derived quantity that would depend on the agent's evolving goal state. Together, these mean $Q_O$ depends on the model alone *as a state variable*; the objective enters as a fixed parameter. Under directed separation ( #der-directed-separation) this works exactly. Under Class 3 (Coupled) architectures where goals leak into model processing, the model itself carries goal-conditioned bias and causal validity degrades. The result requires a stronger condition than predictive sufficiency: predictive sufficiency ( #def-model-sufficiency) is Level-1 (associational); causal validity additionally requires that no unmodeled common cause affects both the environment and the agent's epistemic processing through paths not captured in the model.

The segment's distinctive contribution is the **convention hierarchy** for continuation policies. Different agents reason about the same situation with different planning depth, and the framework names three conventions of *increasing diagnostic power and computational cost*. **C1 — one-step improvement**: the continuation is just the agent's *current* policy (no replanning, no fixed-point computation). Cheapest; weakest diagnostic. **C2 — receding-horizon replanning**: at each future step, re-optimize over a sliding window using the model available at that step. Moderate cost; moderate diagnostic power; captures multi-step recovery. **C3 — Bellman optimal**: the continuation *is* the optimal policy — a fixed-point equation. Strongest diagnostic; most expensive (requires solving the Bellman equation or its approximation).

A **monotonicity result** is derived: for any single fixed model, fixed policy class, and fixed horizon, $A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$. The best-achievable value is monotone in the strength of the continuation convention. The corollary: the *satisfaction gap* ( #def-satisfaction-gap) decreases in the same order, and the *control regret* ( #def-control-regret) reverses ordering. C1 is the *most conservative diagnostic* (most likely to diagnose "locally unattainable"); C3 is the *most accurate* (least likely to give false "unattainable" diagnoses). The cascade's *inferential force* scales with the convention used: under C1, a positive satisfaction gap means "locally stuck"; under C3, the same gap means "genuinely infeasible." This convention hierarchy is what the Part II preface identifies as one of the volume's distinctive contributions.

AAT adopts **C1 as the canonical default** for three reasons: it requires no fixed-point computation, consistent with the incremental update philosophy from Part I ( #emp-update-gain); it makes all AAT diagnostics directly *comparable across analyses* of the same agent over time; and it is the most conservative — false "feasible" diagnoses are minimized. Analyses requiring stronger diagnostic power must state the convention explicitly. The planning horizon $N_h$ is *not* merely a computational convenience — it reflects genuine uncertainty about the far future. Long horizons amplify the impact of model error (small biases compound over many steps). The choice of horizon trades farsightedness against robustness; an agent in a fast-changing environment should use shorter horizons.

## Formal Expression

*[Definition (value-object)]*

Given objective $O_t$, model $M_t$, policy $\pi$, and horizon $N_h$:

$$V_O(M_t, \pi; N_h) = \mathbb{E}\!\left[V_{O_t}(\tau_{t:t+N_h}) \;\middle\vert\; M_t,\; \pi\right]$$

**Action-value form** (for action selection):

$$Q_O(M_t, a; \pi_{\text{cont}}, N_h) = \mathbb{E}\!\left[V_{O_t}(\tau) \;\middle\vert\; M_t,\; do(a_t = a),\; a_{t+1:} \sim \pi_{\text{cont}}\right]$$

$Q_O$ answers: "if I *do* action $a$ now and then follow $\pi_{\text{cont}}$ afterward, what is my expected trajectory value?" The $do(\cdot)$ notation is explicit: this is an interventional query ( #der-causal-hierarchy-requirement), not conditioning on observed action choice. The agent asks about consequences of an intervention, not about correlates of a naturally occurring action.

**Causal validity of the value object.** $Q_O$ is well-defined as a conditional expectation given $M_t$, $do(a)$, and $\pi_{\text{cont}}$. Two mechanisms ensure causal validity:

1. **The do-operator handles current-action confounding.** Since $Q_O$ uses $do(a_t = a)$, the dependence of $a_t$ on the selection mechanism $\pi(M_t, G_t)$ is severed. $G_t$'s influence on action choice is irrelevant because the action is intervened upon, not conditioned on.

2. **The continuation policy is a parameter.** $\pi_{\text{cont}}$ is specified as a fixed policy, not as "whatever the agent would do given its evolving $G_t$." Future actions follow $\pi_{\text{cont}}$ regardless of $G_t$'s state or evolution.

Together, these mean $Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ depends on $M_t$ alone **as a state variable** — $G_t$ enters neither through action selection (severed by $do$) nor through continuation (fixed by parameter). The objective $O_t$ enters as a fixed parameter (it determines which functional $V_{O_t}$ is applied to trajectories), the same way $\pi_{\text{cont}}$ and $N_h$ are parameters. The claim is not that $Q_O$ is independent of the objective — it is that once $O_t$, $\pi_{\text{cont}}$, and $N_h$ are fixed, the only agent state that affects the value is $M_t$. The remaining requirement: $M_t$ must support the interventional query $P(o \mid do(a), M_t)$. Under directed separation ( #der-directed-separation), this holds because $M_t$ updates independently of $G_t$ — there is no path from $G_t$ to outcomes that bypasses both the action channel and $M_t$. For **Class 3 (Coupled) agents** (where $G_t$ leaks into $M_t$ processing), the causal validity of $Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ is degraded because $M_t$ itself carries goal-conditioned bias.

This is a *stronger requirement than predictive sufficiency* ( #def-model-sufficiency). $S(M_t) = 1$ means the model retains all predictive information from the chronica — but predictive sufficiency is a Level 1 (associational) property. Causal validity additionally requires that no unmodeled common cause affects both the environment and the agent's epistemic processing through paths not captured in $M_t$. In practice: when $S(M_t) = 1$ and directed separation holds, $Q_O$ is causally valid. When $S(M_t) \lt 1$ or directed separation fails, the interventional interpretation is correct but the conditional estimate may be biased.

**Continuation convention.** All value queries are conditioned on a specific continuation policy $\pi_{\text{cont}}$ and finite horizon $N_h$. $\pi_{\text{cont}}$ is a *parameter* of the value object, not a derived quantity.

**Canonical default: one-step improvement.** AAT adopts $\pi_{\text{cont}} = \pi_{\text{current}}$ as the canonical continuation convention unless otherwise specified. Under this convention, each action is evaluated assuming current behavior continues afterward — no fixed-point computation, no global optimality assumption. This aligns with AAT's incremental update philosophy ( #emp-update-gain) and makes all AAT diagnostics ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$, $A_O$) comparable across analyses of the same agent over time. It is not a convergence guarantee; it is a shared evaluation frame.

### Convention Hierarchy

Three named conventions form a hierarchy of increasing diagnostic power and computational cost:

**C1: One-step improvement** (canonical default). $\pi_{\text{cont}} = \pi_{\text{current}}$.

Each action is evaluated assuming current behavior continues afterward. No fixed-point computation, no global optimality assumption. Cheapest to compute; weakest diagnostic power.

**C2: Receding-horizon** ($N_r$-step replanning). At each future step, re-optimize over a horizon of $N_r$ steps using the model available at that step.

$$\pi_{\text{RH}}(M_\tau) = \arg\max_\pi V_O(M_\tau, \pi;\, N_r) \quad \text{applied at each } \tau$$

$Q_O^{\text{RH}}(M_t, a;\, N_r, N_h) = \mathbb{E}[V_{O_t}(\tau) \mid M_t, do(a_t = a), a_{t+1:} \sim \pi_{\text{RH}}]$. Captures multi-step recovery: a goal that appears unattainable under frozen continuation may be reachable with replanning. Moderate computation ($N_r$-step optimization at each step); moderate diagnostic power.

**C3: Bellman** (self-consistent optimal). $\pi_{\text{cont}} = \pi^\ast$ where $\pi^\ast = \arg\max_\pi V_O(M_t, \pi;\, N_h)$.

The continuation IS the optimal policy — a fixed-point equation. $A_O^{\text{B}} = V_O(M_t, \pi^\ast;\, N_h)$ is the best achievable value under the model. Strongest diagnostic power; most expensive to compute (requires solving the Bellman equation or its approximation).

### Monotonicity

*[Derived (convention-monotonicity)]*

For any single fixed model $M_t$, horizon $N_h$, and policy class $\Pi$ (i.e., the static-evaluation form: $M_t$ frozen at the decision point, $\Pi$ unchanged across the comparison):

$$A_O^{(1)}(M_t;\, \Pi, N_h) \leq A_O^{\text{RH}}(M_t;\, \Pi, N_r, N_h) \leq A_O^{\text{B}}(M_t;\, \Pi, N_h)$$

**Preconditions on the inequality:** $M_t$ fixed (the comparison evaluates each convention against the *same* model), $\Pi$ fixed (the policy class is the same admissible set across all three conventions; nested $\Pi^{(1)} \subseteq \Pi^{\text{RH}} \subseteq \Pi^{\text{B}}$ would be a different result), $N_h$ fixed (the planning horizon is shared). Replanning *with updated $M_t$* (the deployment behavior of C2) is a different object than the static $A_O^{\text{RH}}$ defined here and the inequality does not automatically transfer — see the "Assumptions held fixed" paragraph below the derivation for the explicit caveat.

**Derivation.** Fix the model $M_t$, policy class $\Pi$, and horizon $N_h$. Each convention evaluates the best first action under a different continuation rule, holding these fixed:

- **C1** freezes continuation at $\pi_{\text{current}}$ (the agent's current policy, which may be suboptimal).
- **C2** re-optimizes periodically: at each replanning step, the agent selects the best available first action from $\Pi$ given $M_t$ at that time. By construction, $\pi_{\text{RH}} \succeq \pi_{\text{current}}$ at each future step, because C2 optimizes where C1 holds fixed.
- **C3** uses the globally optimal continuation $\pi^\ast = \arg\sup_{\pi \in \Pi} V_O(M_t, \pi; N_h)$, which is at least as good as any replanning policy because it optimizes over the full trajectory.

A weakly better continuation yields a weakly higher expected trajectory value (the objective $V_{O_t}$ is evaluated on the same trajectory distribution, with only the continuation policy changed). The ordering of continuations ($\pi_{\text{current}} \preceq \pi_{\text{RH}} \preceq \pi^\ast$) therefore implies $A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$. Taking the supremum over the first action preserves the ordering because the supremum of a larger set is at least as large. $\square$

**Assumptions held fixed:** same $M_t$ (the agent's current model, which may be wrong), same $\Pi$ (the agent's policy class, which may be narrow), same $N_h$ (the planning horizon). The ordering is about the *continuation rule*, not about the model or policy class. Improving $M_t$, expanding $\Pi$, or extending $N_h$ can change all three values simultaneously and is a separate operation (addressed in #der-orient-cascade, step 5).

**Corollary (monotonicity of $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$).**

$$\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$$

$$\delta_{\text{regret}}^{(1)} \leq \delta_{\text{regret}}^{\text{RH}} \leq \delta_{\text{regret}}^{\text{B}}$$

Since $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O$, higher $A_O$ means lower $\delta_{\text{sat}}$. C1 is the most conservative diagnostic (most likely to diagnose "locally unattainable"); C3 is the most accurate (least likely to give false "unattainable" diagnoses). The regret ordering reverses: C3 reveals the largest regret because it compares against the globally optimal policy, while C1 reveals only the gap to the best one-step deviation.

### Diagnostic implications

| Convention | $\delta_{\text{sat}} \gt 0$ means | $\delta_{\text{regret}} \approx 0$ means |
|---|---|---|
| **C1** (one-step) | Cannot improve toward goal in one step from here | Current first action is locally near-optimal |
| **C2** (receding-horizon) | Cannot reach goal with $N_r$-step replanning | Current first action is near-optimal with replanning |
| **C3** (Bellman) | Goal is genuinely infeasible given $(M_t, \Pi, N_h)$ | Policy is globally near-optimal |

The 2×2 diagnostic table ( #def-control-regret) applies under all three conventions with the same structure but different inferential force. Under C1, the "capability limit" quadrant ($\delta_{\text{sat}} \gt 0$, $\delta_{\text{regret}} \approx 0$) means "locally stuck" — the agent may be globally recoverable but cannot see the recovery path. Under C3, the same quadrant means "genuinely infeasible" — no policy in $\Pi$ can achieve the goal. The cascade's inferential force scales with the convention.

**AAT adopts C1 as the canonical default** for three reasons: (1) it requires no fixed-point computation, consistent with the incremental update philosophy ( #emp-update-gain); (2) it makes all AAT diagnostics comparable across analyses of the same agent; (3) it is the most conservative, meaning false "feasible" diagnoses are minimized. Analyses that require stronger diagnostic power should state the convention explicitly. For deployed decision-making systems where "locally stuck but globally recoverable" situations are common, C2 is recommended.

Different continuation conventions yield different values for $A_O$, $\delta_{\text{sat}}$, and $\delta_{\text{regret}}$. Diagnostics computed under different conventions are not directly comparable — the convention is part of the measurement, not just the computation. When a specific convergence guarantee is needed (e.g., for #schema-strategy-persistence), the solution concept must be stated explicitly; the one-step improvement default does not provide convergence guarantees.

## Epistemic Status

The segment contains three distinct epistemic layers:

1. **The definitions** ($V_O$, $Q_O$ as conditional expectations): *exact.* These are mathematical definitions — conditional expectations of a functional over trajectories. The definitions are precise; the *computability* of these expectations is a separate question.

2. **The causal-validity claim** (that $Q_O$ depends on $M_t$ alone as a state variable): *conditional* on directed separation ( #der-directed-separation). For Class 1 (Separated) agents, this is exact. For Class 3 (Coupled) agents, $M_t$ carries goal-conditioned bias and the causal validity degrades. The frontmatter `status: exact` applies to the definitions; the causal-validity argument is conditional on the architectural scope restriction.

3. **The convention hierarchy and monotonicity**: *exact.* The three conventions (C1, C2, C3) are definitions. The monotonicity result ($A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$) is a direct consequence of "better continuation policy yields higher expected value" — the ordering is forced by the definition of optimality. The diagnostic implications table states what each convention's quantities mean by construction.

## Discussion

**Extending the policy objective.** The existing policy objective ( #disc-ciy-unified-objective) uses $\mathbb{E}[\text{value}(a) \mid M_t]$ without formal content for "value." With the value object, this becomes:

*[Discussion (policy-objective-extension)]*

$$\pi^*(M_t, G_t) = \arg\max_a \left[Q_O(M_t, a;\, \pi_{\text{cont}}, N_h) + \lambda(M_t, O_t, N_h) \cdot \text{CIY}(a;\, M_t)\right]$$

Note that $\lambda$ now depends on $(M_t, O_t, N_h)$, not just $M_t$. The value of exploration depends on the objective and the horizon:
- An agent with a deadline should explore less as time runs out
- An agent with a safety constraint should explore differently from a utility maximizer
- Two agents with identical $M_t$ but different objectives should price exploration differently

This extension is structurally motivated but the specific form of $\lambda(M_t, O_t, N_h)$ is not derived within AAT (same status as #disc-ciy-unified-objective's treatment of $\lambda$).

**Connection to #def-model-sufficiency.** $V_O$ is conditioned on $M_t$, not on the true environment state $\Omega_t$. When $S(M_t) \lt 1$, the agent's value estimates are biased — it may over- or underestimate trajectory values because its model is incomplete. The satisfaction gap ( #def-satisfaction-gap) and control regret ( #def-control-regret) are defined in terms of $V_O(M_t, \cdot)$, not $V_O(\Omega_t, \cdot)$, which means they measure the agent's *believed* situation, not the true one. Improving $M_t$ (reducing $\delta_{\text{epistemic}}$) brings the agent's value estimates closer to reality.

**Horizon dependence.** $N_h$ is not merely a computational convenience — it reflects genuine uncertainty about the far future. Long horizons amplify the impact of model error (small biases in $M_t$ compound over many steps). The choice of $N_h$ trades off farsightedness against robustness to model error. An agent in a fast-changing environment ($\rho$ high) should use shorter horizons; one in a stable environment can plan further.

## Working Notes

- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Removed at `candidate` stage per FORMAT.md Gate 4.
- The one-step improvement convention is now the canonical default (promoted from Working Notes to Formal Expression). This resolves the comparability issue: $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ are comparable across analyses when computed under the same convention.
- When a specific convergence guarantee is needed (e.g., for strategy-persistence-schema), the solution concept must be stated explicitly — the one-step improvement default is not sufficient.
- For LLM agents with context turnover, $N_h$ has a natural bound: the current session. The "continuation policy" is whatever the next agent instance will do, which the current instance cannot control. This connects to `#obs-context-turnover` (under `03-llm-core/`).

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing material, kept separate from the certified theory-fix findings. **Coverage:** 9 dirs carry a dedicated or batched reflection (193847, 266847, 451729, 526815, 584721, 773921, 829314, 849201, plus 613842's agency-lift batch). Substrate attribution inferred from voice where not explicit. *Early finding-vs-framing conflation preserved as signal.*

#### 1. Candidate Brief prose / pre-prose

- The convention hierarchy in plain terms: C1 (one-step) / C2 (receding-horizon, MPC-style) / C3 (Bellman) are "greedy heuristics / model-predictive control / dynamic programming" — and the monotonicity $A_O^{(1)} \le A_O^{\text{RH}} \le A_O^{\text{B}}$ is "simply optimizing over a larger set of policies yields a higher or equal value," tied directly to the satisfaction-gap and control-regret orderings (Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-849201; Claude, AUDIT-WORKING-451729).

#### 2. Candidate Discussion

- **The convention hierarchy is the formal "locally stuck vs genuinely impossible" distinction** *(strong, cross-substrate convergent).* $\delta_{\text{sat}} \gt 0$ under C1 means "locally stuck"; $\delta_{\text{sat}} \gt 0$ under C3 means "genuinely infeasible given $M_t$, $\Pi$, $N_h$." This is "the mathematical definition of needing to sleep on it / needing to plan." The cautionary corollary: a C1-default agent that hits a wall "doesn't know if the goal is impossible or if it just needs to plan two steps ahead — it might trigger a massive structural adaptation (giving up on the goal) when all it needed was a slightly longer planning horizon. The framework provides the vocabulary to describe this tragedy" (Gemini, AUDIT-WORKING-193847; Gemini, AUDIT-WORKING-829314; Claude/Gemini, AUDIT-WORKING-266847; Claude, AUDIT-WORKING-451729). Candidate Discussion paragraph.
- **The $do(\cdot)$ inside $Q_O$ is the doctor / harsh-drug confounding case** *(vivid pedagogy).* Standard RL writes $Q(s,a) = \mathbb{E}[R \mid s, a]$ (*observing* yourself take $a$); AAT writes $\mathbb{E}[V \mid M_t, do(a)]$ (*intervening*). "If a doctor historically only prescribes a harsh drug to the sickest patients, observing the drug in the record correlates with death; if the doctor *does* the drug, it cures them." The $do$-operator "prevents the agent from confusing its own historical habits with the laws of physics" (Gemini, AUDIT-WORKING-829314; the predictive-sufficiency vs causal-validity distinction praised as "a masterpiece of technical writing" at the same dir and Gemini, AUDIT-WORKING-193847). Candidate Discussion / Brief illustration.
- **C1-as-default mirrors the incremental-$\eta^\ast$ philosophy of Section I.** Both the epistemic and purposeful layers default to *incremental improvement over a fixed reference point*, not global optimization — "a coherent philosophy; the parallelism is elegant" (Claude/Gemini, AUDIT-WORKING-266847). Candidate Discussion connecting the C1 default back to Part I's update philosophy.

#### 3. Follow-up items

- **The C2 (receding-horizon) monotonicity rung may not be generally exact.** Myopic replanning over a shorter horizon $N_r$ can pick actions locally optimal over $N_r$ but worse over the full evaluated horizon $N_h$ than continuing $\pi_{\text{current}}$ — so $A_O^{(1)} \le A_O^{\text{RH}}$ holds only under additional conditions (C2 optimizing the same full-horizon objective; C1 admissible as a value-compared fallback; or consistent terminal/value functions). Given `status: exact`, the segment-level status may need splitting or a stated condition (Claude, AUDIT-WORKING-526815). Routed to the certified-findings track for adjudication (strengthen-first: find the condition under which the ordering holds before weakening the claim).
- **The causal-validity claim may rest on too little.** $do(a)$ defines an interventional *query*, but *estimating* it requires $M_t$ to contain/identify the relevant action-transition causal structure; observational predictive sufficiency plus goal-blind processing do not by themselves guarantee valid interventional expectations. The causal-validity argument should name the causal-model assumptions it needs (Claude, AUDIT-WORKING-526815; Claude/Gemini, AUDIT-WORKING-266847 noted the Class-2 $M_t$-bias degradation separately). Routed to the certified-findings track.
- **The exploration weight $\lambda(M_t, O_t, N_h)$ is structurally motivated but underived.** Several substrates noted the joint $Q_O + \lambda \cdot \text{CIY}$ objective leaves $\lambda$'s form open, and that it "should logically depend on objective and horizon — don't explore if you have a tight deadline" (Claude/Gemini, AUDIT-WORKING-266847; Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-584721). A persistent open shared with `#disc-ciy-unified-objective`.

#### 4. Readers often ask / wonder

- For LLM agents, what does the natural $N_h$ bound mean operationally? An agent that "knows it will die (context wipe) in 10 turns" has a drastically different optimal policy than an infinite-horizon agent — does it just truncate $N_h$, or actively externalize state (leave notes for the next instance)? (Gemini, AUDIT-WORKING-193847.) The Working Note above already names the $N_h$-bound; this is the natural reader follow-on.
- The Class-2 $Q_O$ degradation is acknowledged but *unquantified* — is the bias bounded by $\kappa_{\text{processing}}$, or by another measure? (Claude, AUDIT-WORKING-584721 — possibly addressed by `#deriv-observation-ambiguity-bias-bound`.)

#### 5. Candidate figures

- **Value-query pipeline with a severed $do(a)$ path.** $M_t$ plus fixed parameters ($O_t$, $\pi_{\text{cont}}$, $N_h$) generate a model-based trajectory distribution under $do(a)$; the objective functional scores trajectories; diagnostics read off expected value. Draw the *current-policy selection mechanism as a severed path* (the $do$-operator is the conceptual center), with a small C1/C2/C3 convention ladder underneath — and a warning that the C2 rung is not automatically monotone unless replanning optimizes the full evaluated horizon (Claude, AUDIT-WORKING-526815).

#### Belongs elsewhere

- **"Honest imagination" / counterfactual-without-execution (→ `04-eli-core/` / `#disc-sandbox-evaluation-ceiling`).** Computing a *causally valid* $Q_O$ requires holding a counterfactual action in mind "without letting the emotional/purposeful weight of $G_t$ distort the simulated outcome" — "free will within the model's simulation." A Class 3 agent's $G_t$ leaks into its own internal simulation, so "if it wants to believe an action will work, its simulation will hallucinate success" — which is why consciousness infrastructure may need to provide *external, objective simulation sandboxes*, the agent's own mind being "too entangled to be trusted with counterfactuals" (Gemini, AUDIT-WORKING-193847). Aspirational reach pointing at the sandbox-evaluation material and the ELI volume, not this definition.
