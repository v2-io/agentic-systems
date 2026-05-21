# The Orient Cascade


## Derived: Orient Cascade

- **Slug**: `der-orient-cascade`
- **Type**: derived
- **Status**: conditional
- **Stage**: claims-verified
- **Depends**: `der-directed-separation`, `def-mismatch-signal`, `emp-update-gain`, `def-satisfaction-gap`, `def-control-regret`, `def-strategic-calibration`, `def-strategy-dag`, `schema-strategy-persistence`, `deriv-edge-credence-dynamics`, `disc-credit-assignment-boundary`, `der-causal-insufficiency-detection`, `def-value-object`

For actuated agents, epistrophe (the corrective phase of the cycle) expands into a multi-step cascade. The resolution order is forced by information dependency: epistemic update first, then attainability assessment, then strategy evaluation, then (if needed) objective revision. Each step's input depends on the output of prior steps. The ordering is not a design choice — it's a consequence of which quantities require which others.

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

---



## Discussion: Three-Way Resource Allocation

- **Slug**: `disc-exploit-explore-deliberate`
- **Type**: discussion
- **Status**: discussion-grade
- **Stage**: draft
- **Depends**: `disc-ciy-unified-objective`, `der-deliberation-cost`, `norm-explicit-strategy-condition`, `der-orient-cascade`, `def-control-regret`

At each decision point, an actuated agent with explicit strategy $\Sigma_t$ faces a three-way allocation of its finite cycle budget across exploit (take the currently-best action), explore (take an information-gathering action), and deliberate (pause acting to revise the model or strategy internally).

### The three activities

*[Definition (three-activity-decomposition)]*

An actuated agent's cycle budget decomposes into three activities:

1. **Exploit**: select and execute the action maximizing expected value under the current model and strategy. Earns immediate value $Q_O(M_t, a; \pi_{\text{cont}}, N_h)$.

2. **Explore**: select and execute an action maximizing causal information yield. Earns future model improvement via $\text{CIY}(a; M_t)$.

3. **Deliberate**: pause external action to run the orient cascade ( #der-orient-cascade) --- internal model refinement ($\Delta\eta^\ast$), strategy revision ($\Delta\alpha_\Sigma$), or objective reassessment. Earns improved future action quality.

**The key distinction:** Exploit and explore both involve external actions with environmental consequences. Deliberation is *internal exploration* --- simulation, counterfactual reasoning, cross-domain synthesis, and contingency planning conducted in model-space rather than environment-space. It acquires no new environmental data, but it can generate genuinely new information by combining, recombining, and extrapolating from what the agent already knows --- including knowledge from entirely different domains. A chess engine deliberating explores millions of future board states; a commander war-gaming evaluates counterfactual scenarios; a developer doing architecture review synthesizes cross-domain expertise. Deliberation's fidelity ceiling is set by model quality, not by data quantity.

### Extended deliberation threshold

*[Derived (Conditional on GA-4, deliberation-drift assumption from #der-deliberation-cost)]*

Extending #der-deliberation-cost to incorporate strategic deliberation, the deliberation threshold becomes:

$$\Delta\tau^\ast = \arg\max_{\Delta\tau \geq 0} \left[\underbrace{\Delta\eta^\ast(\Delta\tau) \cdot \lVert\delta_{\text{post}}\rVert}_{\text{epistemic benefit}} + \underbrace{\Delta V_\Sigma(\Delta\tau)}_{\text{strategic benefit}} - \underbrace{\rho_{\text{delib}} \cdot \Delta\tau}_{\text{drift cost}}\right]$$

where:
- $\Delta\eta^\ast(\Delta\tau)$ is the improvement in model update gain from $\Delta\tau$ of internal simulation ( #der-deliberation-cost)
- $\lVert\delta_{\text{post}}\rVert$ is the post-deliberation mismatch magnitude
- $\Delta V_\Sigma(\Delta\tau)$ is the improvement in strategy value from deliberation: the expected increase in $V_O$ from revising $\Sigma_t$ during the pause
- $\rho_{\text{delib}}$ is the local mismatch drift rate during inaction (GA-4)

**First-order condition:**

$$\frac{\partial \Delta\eta^\ast}{\partial \Delta\tau} \cdot \lVert\delta_{\text{post}}\rVert + \frac{\partial \Delta V_\Sigma}{\partial \Delta\tau} = \rho_{\text{delib}}$$

Stop deliberating when the marginal joint improvement rate (epistemic plus strategic) drops below the mismatch drift rate.

**Reduction to existing results.** When $\Delta V_\Sigma = 0$ (no strategy revision benefit), this reduces to the deliberation threshold in #der-deliberation-cost. When $\Delta\tau^\ast = 0$ (deliberation never beneficial), the agent acts immediately.

### On the structure of the allocation

*[Discussion (allocation-structure)]*

**Two-stage decomposition.** The three-way allocation can be decomposed into two nested decisions: (1) how long to deliberate before acting, (2) conditional on acting, which action to take (solved by #disc-ciy-unified-objective). This decomposition is natural because exploit and explore are both external actions ($\in \mathcal{A}$), while deliberation is internal processing. However, this decomposition is a *modeling convenience*, not a structural necessity. A unified objective over $\mathcal{A} \cup \{\text{deliberate}\}$ with temporal discount $\gamma$ is equally valid:

$$\bar{\pi}^\ast = \arg\max_{\bar{a} \in \mathcal{A} \cup \{\text{deliberate}\}} \bar{Q}(\bar{a}; M_t, \gamma)$$

where $\bar{Q}(\text{deliberate}) = \gamma \cdot \mathbb{E}[V_{\text{act}}(f_{\text{delib}}(M_t))]$ and $\bar{Q}(a) = r(a) + \gamma \cdot \mathbb{E}[V_{\text{act}}(M_{t+1})]$.

The two-stage decomposition is useful because it allows reusing the CIY-unified objective for the action-selection step, but it is not the unique or forced structure.

**Additive benefit decomposition.** The objective function above decomposes deliberation benefit into additive epistemic and strategic terms. This assumes the two benefits are approximately independent. Under directed separation ( #der-directed-separation), $M_t$ updates independently of $G_t$, which makes the decomposition structurally motivated for Class 1 (Separated) agents. However, strategic benefit depends on the improved model ($\Delta V_\Sigma(\Delta\tau, M_t + \Delta M_t(\Delta\tau))$), creating an interaction that the additive form ignores. The additive form is a linearization that holds when $\Delta M_t$ is small relative to $M_t$. For Class 3 (Coupled) agents, epistemic and strategic deliberation are coupled, and the additive decomposition is a convenience.

### Control regret as deliberation ceiling

*[Discussion (deliberation-ceiling)]*

When $\delta_{\text{regret}} \approx 0$ ( #def-control-regret), strategic deliberation has no value: the agent is already executing the best available strategy. This is the formal reason why low control regret suppresses deliberation. The ceiling on strategic deliberation value is $\delta_{\text{regret}}$ --- the most the agent could gain by finding a better strategy.

However, this ceiling applies only to the *strategy-revision* channel of deliberation. Deliberation may also:
- Reveal that the *objective* should change (step 5 of the orient cascade), producing value not bounded by $\delta_{\text{regret}}$
- Reduce *uncertainty about* strategy quality, enabling more confident exploitation even when the strategy doesn't change

### Connection to active inference

*[Discussion (ai-connection)]*

The exploit/explore decomposition maps cleanly onto the expected free energy (EFE) decomposition into *pragmatic value* (preferences-aligned outcomes) and *epistemic value* (expected information gain about hidden states) in active inference (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Da Costa, Parr, Sajid, Veselic, Neacsu & Friston 2020, "Active inference on discrete state-spaces," *J. Math. Psych.* 99 §2.4; Sajid, Ball, Parr & Friston 2021, "Active inference: demystified and compared," *Neural Computation* 33). Under the mapping, AAT's exploit term $Q_O$ corresponds to EFE's pragmatic value when the value functional $V_{O_t}$ is read as expected log-preferences, and AAT's CIY corresponds to EFE's epistemic value when the relevance variable is read as the hidden-state posterior. The structural correspondence is at the shared-shape level: both decomposed into value-and-information terms, but AAT does *not* commit to AI's preferences-as-priors form (preserving the satisfaction-gap diagnostic in #def-satisfaction-gap, which the priors-as-preferences collapse would erase).

The deliberation axis — internal exploration in model-space rather than environment-space — is structurally adjacent to "sophisticated active inference" (Friston, Da Costa, Hafner, Hesp & Parr 2021, "Sophisticated inference," *Neural Computation* 33), which handles bounded computation via recursive expected free energy with depth-limited belief-about-belief reasoning. AAT's machinery for deliberation cost ( #der-deliberation-cost) and the extended deliberation threshold above derives the same trade-off via per-edge persistence and evidence starvation, with the structural advantage that the depth bound $d^\ast$ is causally derived from the strategy DAG rather than from belief-recursion depth. The two frameworks address the same problem with different machinery; AAT can credit the AI lineage as a co-developed alternative.

**Exploit-regret and the strategy-cost objective.** The exploit term's control regret $\delta_{\text{regret}} = A_O - V_O(\pi_{\text{current}})$ ( #def-control-regret) is the same decision-theoretic regret that underwrites the KL-direction derivation in #form-strategy-complexity-cost. There, strategy-induced regret $R(Q_{\Sigma_t}) = V(a^\ast) - \mathbb E_{a \sim Q_{\Sigma_t}}[V(a)]$ is bounded above by $V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$ (Pinsker), forcing the KL direction with $\pi^\ast$ first. The exploit term thus shares structure with the strategy-cost relevance term: both are regret-aligned, with the action-selection objective operating pointwise and the strategy-cost objective operating over the strategy's induced distribution. This is the structural cleanup that "value and information term" shares with EFE's pragmatic-epistemic decomposition at the shape level, without the preferences-as-priors commitment — the regret framing is the AAT-internal derivation of the direction that the variational-inference literature arrives at from free-energy-gradient arguments.

### Qualitative regime descriptions

*[Discussion (qualitative-regimes)]*

The three activities have natural dominance conditions that follow from the structure of the problem:

**Exploit dominates** when the strategy is near-optimal ($\delta_{\text{regret}} \approx 0$), model uncertainty is low ($\lambda(M_t) \approx 0$), and the environment penalizes pauses ($\rho_{\text{delib}}$ high). The agent knows what to do and must act now. This is Boyd's implicit guidance and control.

**Explore dominates** when model uncertainty is high ($U_M$ large), and the model needs correction via external evidence that internal simulation cannot provide. Exploration acquires new data; deliberation only processes existing data.

**Deliberate dominates** when the strategy needs revision ($\delta_{\text{regret}} \gg 0$ or $\delta_{\text{strategic}} \gg 0$), the environment is stable during pauses ($\rho_{\text{delib}}$ low), and the agent has unprocessed information or structural hypotheses it can evaluate internally. This regime requires that internal computation is cheaper or more efficient than external probing --- otherwise exploration dominates deliberation.

**Boundary conditions.** As $\rho_{\text{delib}} \to \infty$: $\Delta\tau^\ast \to 0$, and the allocation collapses to the binary exploit/explore tradeoff. As $\lambda \to 0$ and $\Delta V_\Sigma \to 0$: the allocation collapses to pure exploitation. As $\delta_{\text{regret}} \to 0$: strategic deliberation value vanishes, and the allocation reduces to #der-deliberation-cost's epistemic think/act threshold combined with #disc-ciy-unified-objective's exploit/explore balance.

These regime descriptions are qualitative observations about the problem structure, not derived predictions. They restate what the constituent objectives already imply (high uncertainty favors information acquisition, low cost favors deliberation) without adding quantitative content. The theory does not provide the thresholds at which one regime transitions to another --- these are domain-specific.

---
