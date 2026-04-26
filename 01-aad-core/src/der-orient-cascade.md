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
  - deriv-strategic-dynamics
  - disc-credit-assignment-boundary
  - der-causal-insufficiency-detection
  - def-value-object
stage: claims-verified
---

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

   **(4a) Plan-level calibration (default within-L0).** Evaluate plan-confidence error $\delta_s = \hat P_\Sigma - \Phi$ — the gap between the agent's plan-confidence score and the independence-model plan value at true edge parameters. $\delta_s$ is credit-assignment-free (requires only status propagation), and its persistence is proved ( #schema-strategy-persistence, Prop B.5 in #deriv-strategic-dynamics). This is the cheapest operational signal, but its persistence guarantee is within the **independence model (L0)** of the Correlation Hierarchy ( #def-strategy-dag): $\delta_s \to 0$ means $\hat P_\Sigma$ has converged to $\Phi$, not to actual plan success probability. When the DAG is causally insufficient, $\Phi$ itself is a biased target. Step 4c checks whether this is the binding regime.

   **(4b) Edge-level localization (when credit assignment is available).** When sufficient observability and attribution quality exist (Level 1+ per #disc-credit-assignment-boundary), the agent can compute per-edge residuals $\delta_{\text{strategic}}$ ( #def-strategic-calibration) to localize which edges need revision. $\delta_{\text{strategic}}$ provides finer-grained diagnostics but its persistence is open and it requires the credit-assignment machinery that $\delta_s$ avoids. Step 4b is optional — it improves diagnostic resolution but is not required for the cascade's corrective function.

   **(4c) Causal-sufficiency check (L0→L1 escalation).** If persistent $\delta_s \approx 0$ coincides with persistent negative plan-outcome residuals ($y_G \lt \hat P_\Sigma$ on average, after edge credences have converged), this is evidence that the DAG is causally insufficient and L0 calibration is converging to a biased target. The diagnostic is pairwise sibling covariance under an augmented test ( #der-causal-insufficiency-detection): positive covariance among sibling edges, at timescales where each edge's individual credence has stabilized, localizes where a latent common cause is missing. When the signal for L1 augmentation is present, step 4c directs the agent to add common-cause nodes ( #def-strategy-dag Correlation Hierarchy) *before* escalating via 5a–5d. Running the cascade's exploitation recommendations under L0 when the signal for L1 is present compounds miscalibration — the agent acts confidently on a model whose own residual structure is telling it the model is wrong.

   *Practical sensitivity.* Step 4c is the unique broadly-available L0→L1 diagnostic ( #der-causal-insufficiency-detection no-go), but its effective power depends on signal-to-noise: small samples, weak common-cause effects, or noisy residuals can produce false negatives, and edge-credence drift can mimic sibling covariance. The convergence framing — "after edge credences have converged" — is a precondition, not a guarantee: in non-stationary environments where per-edge credences keep drifting, the trigger may never cleanly fire and L1 augmentation should be considered the default rather than gated on 4c's signal ( #def-strategy-dag Correlation Hierarchy). Formal preconditions (joint observability, per-edge credence stabilization, approximate stationarity over the test window) and detection scope live in #der-causal-insufficiency-detection; consult them before treating a 4c null as evidence of L0 sufficiency.

5. **If $\delta_{\text{sat}} \gt 0$ persists** — escalate before revising $O_t$.

   **Under C1 (the canonical default), $\delta_{\text{sat}} \gt 0$ means *locally stuck*, not *globally infeasible*** ( #def-value-object). Before concluding the objective is wrong, the agent should check whether the gap reflects a limitation of the current analysis rather than genuine infeasibility:

   **(5a)** Check whether $M_t$ correction changes the feasibility assessment — a wrong model may make an achievable goal appear unattainable.

   **(5b)** Check whether a richer policy class $\Pi$ would close the gap — structural $\Sigma_t$ adaptation (expanding the strategy space, not just revising edge credences). This includes L1 augmentation of the strategy DAG ( #def-strategy-dag Correlation Hierarchy): if step 4c detected causal insufficiency, adding common-cause nodes here is the structural repair.

   **(5c)** Check whether convention escalation reveals recovery paths — evaluating under C2 (receding-horizon) may show $\delta_{\text{sat}}^{\text{RH}} \leq 0$ for a goal that appeared unattainable under C1.

   **(5d)** If $\delta_{\text{sat}} \gt 0$ persists across $M_t$ correction, $\Pi$ expansion (including L1 augmentation), and convention escalation — **revise $O_t$**.

   The cascade's ordering ensures objective revision is the last resort, not the first response to unmet goals. The agent reaches step 5d only after exhausting the alternatives that the satisfaction-gap disambiguation table ( #def-satisfaction-gap) identifies: wrong $M_t$, narrow $\Pi$, short $N_h$, and only then genuinely infeasible goal.

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

The cascade **ordering** is *exact*: it is a logical consequence of which quantities appear in which formulas. Steps 1-2 (epistemic update, attainability assessment) rest on well-typed quantities ( #def-mismatch-signal, #def-satisfaction-gap) and exact derivation. Step 3 (control regret) is exact ( #def-control-regret). Step 4a (plan-level calibration via $\delta_s$) is grounded in a proved quantity — the sector condition transfers to $\delta_s$ (Prop B.5 in #deriv-strategic-dynamics) — but the formal guarantee is *within the L0 independence model*: $\delta_s \to 0$ means convergence to $\Phi$, which equals actual plan success only when the DAG is causally sufficient. Step 4b (per-edge localization via $\delta_{\text{strategic}}$) inherits strategic-calibration's discussion-grade status — the credit-assignment problem and execution-fidelity requirement are acknowledged but unresolved ( #def-strategic-calibration, Epistemic Status). Step 4c (causal-sufficiency check) is the mechanism for exiting L0 when L1 is the binding regime; it is *robust-qualitative* — the diagnostic logic is sound ( #der-causal-insufficiency-detection), but sensitivity depends on how cleanly the agent can separate sibling-covariance signal from edge-credence noise at convergence. Step 5's escalation substeps (5a-5c) are derived from the satisfaction-gap disambiguation table ( #def-satisfaction-gap); step 5d (objective revision) is the residual case after alternatives are exhausted. The ordering of all steps is forced by information dependency (each step's input depends on prior steps' output). What is NOT derived is the *timing* — how long the agent should spend on each step before proceeding, and how long $\delta_s \approx 0$ must persist before 4c's signal is trusted.

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
- **Strategy-maintenance status (updated).** The cascade's ORDERING is exact — forced by information dependency. The cascade's CONTENT for steps 3-5 has progressed: #disc-credit-assignment-boundary characterizes the tractable/intractable boundary and establishes that persistence does not require credit assignment (Prop B.5); #deriv-strategic-dynamics verifies sector conditions for four topologies; #hyp-edge-update-via-gain has a default signal function candidate (gradient-based, satisfying directional fidelity). What remains domain-specific: the choice of signal function implementation, execution-fidelity monitoring, and handling of correlated failures (where $\hat P_\Sigma$ overestimates — #def-strategy-dag). The theory now provides the structural requirements and a default scheme; specific implementations are engineering, parallel to how the gain principle provides $\eta^\ast$ while Kalman/TD-learning/etc. are implementations.
