---
slug: orient-cascade
type: derived
status: conditional
depends:
  - directed-separation
  - mismatch-signal
  - satisfaction-gap
  - control-regret
  - strategic-calibration
stage: draft
---

# Derived: Orient Cascade

For actuated agents, epistrophe (the corrective phase of the cycle) expands into a multi-step cascade. The resolution order is forced by information dependency: epistemic update first, then attainability assessment, then strategy evaluation, then (if needed) objective revision. Each step's input depends on the output of prior steps. The ordering is not a design choice — it's a consequence of which quantities require which others.

## Formal Expression

*[Derived (orient-cascade, from information dependency between mismatch types)]*

1. **Reduce $\delta_{\text{epistemic}}$** — understand reality.
   Update $M_t$ via #mismatch-signal and #update-gain. Prerequisite for all purposeful evaluation, because $M_t$ appears in every subsequent formula.

2. **Evaluate $\delta_{\text{sat}}$** — is the goal achievable?
   Compute $A_O(M_t; \Pi, N_h)$ using the updated $M_t$. Requires adequate $M_t$ to assess attainability ( #satisfaction-gap).

3. **Evaluate $\delta_{\text{regret}}$** — is the policy suboptimal?
   Compare $A_O$ to $V_O(M_t, \pi_{\text{current}}; N_h)$ ( #control-regret). This step applies regardless of $\delta_{\text{sat}}$'s sign — the 2×2 diagnostic ( #control-regret) requires both quantities to distinguish four cases:
   - $\delta_{\text{sat}} \leq 0$, $\delta_{\text{regret}} \approx 0$: **success** — goal attainable, policy near-optimal.
   - $\delta_{\text{sat}} \leq 0$, $\delta_{\text{regret}} \gg 0$: **strategy problem** — goal attainable, policy poor → revise $\Sigma_t$.
   - $\delta_{\text{sat}} \gt 0$, $\delta_{\text{regret}} \gg 0$: **both** — goal hard AND strategy weak → revise $\Sigma_t$ first (cheaper than revising $O_t$), then reassess $\delta_{\text{sat}}$.
   - $\delta_{\text{sat}} \gt 0$, $\delta_{\text{regret}} \approx 0$: **capability limit** — already doing the best available; proceed to step 5.

4. **If $\delta_{\text{regret}}$ high, evaluate $\delta_{\text{strategic}}$** — is the plan's causal model wrong?
   Examine edge residuals. Requires adequate $M_t$ and evidence of suboptimal execution ( #strategic-calibration). **Note:** $\delta_{\text{strategic}}$ is the operational diagnostic the cascade uses, but its persistence is open — the strategic persistence proof ( #strategy-persistence-schema) covers plan-confidence error $\delta_s$, not $\delta_{\text{strategic}}$ (which requires credit-assignment machinery). The cascade's step 4 is therefore grounded in a discussion-grade quantity, even though the ordering of step 4 relative to the other steps is derived.

5. **If $\delta_{\text{sat}} \gt 0$ persists across $\Sigma_t$ revisions** — revise $O_t$.
   The cascade's ordering ensures objective revision is the last resort, not the first response to unmet goals. The agent reaches this step only in the capability-limit quadrant ($\delta_{\text{sat}} \gt 0$, $\delta_{\text{regret}} \approx 0$), or after strategy revision fails to close the gap.

**Derivation.** Each step's input depends on prior steps' outputs:
- You cannot evaluate strategy quality with a broken reality model (step 3 requires step 1)
- You cannot distinguish "locally bad strategy" from "locally unattainable goal" without both $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ (step 3 requires step 2)
- You should not revise the objective until you've verified that improving $\Sigma_t$ cannot close the gap (step 5 requires steps 3-4)

The ordering is forced by information dependency.

**Convention hierarchy and diagnostic power.** The 2×2 diagnostic and the inferences drawn from it are relative to the continuation convention in the value object ( #value-object), which defines a hierarchy of three conventions with a proved monotonicity result.

Under **C1** (one-step improvement, canonical default), $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ are one-step-improvement quantities. A multi-step recoverable objective may appear locally unattainable ($\delta_{\text{sat}} \gt 0$) because continuation is frozen at $\pi_{\text{current}}$. The "capability limit" quadrant ($\delta_{\text{sat}} \gt 0$, $\delta_{\text{regret}} \approx 0$) means *locally stuck* — the agent may be globally recoverable but cannot see the recovery path from one-step analysis.

Under **C2** (receding-horizon, $N_r$-step replanning), the diagnostics capture multi-step recovery potential. An objective that appeared unattainable under C1 may show $\delta_{\text{sat}}^{\text{RH}} \leq 0$ because replanning reveals a viable path. The "capability limit" quadrant means *stuck with $N_r$-step replanning* — stronger evidence of genuine difficulty.

Under **C3** (Bellman), the diagnostics are global. $\delta_{\text{sat}}^{\text{B}} \gt 0$ means the goal is genuinely infeasible given $(M_t, \Pi, N_h)$ — no policy can achieve it. The "capability limit" quadrant is a definitive diagnosis: the agent is optimally pursuing an infeasible goal (modulo model error in $M_t$). This is the inference the cascade was designed to support; C1 and C2 provide progressively weaker versions of it.

The monotonicity ( #value-object): $\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$. Every "unattainable" diagnosis under C3 persists under C1 and C2. A C1 "unattainable" diagnosis may be overturned by C2 or C3 (the goal is reachable with replanning or globally optimal play). The cascade's *ordering* is convention-independent (forced by information dependency). The *inferential force* at each step scales with the convention: C1 gives local heuristics, C2 gives moderate-horizon diagnostics, C3 gives global conclusions.

## Epistemic Status

The cascade **ordering** is *exact*: it is a logical consequence of which quantities appear in which formulas. Steps 1-2 (epistemic update, attainability assessment) rest on well-typed quantities ( #mismatch-signal, #satisfaction-gap) and exact derivation. Steps 3-5 (control regret, strategic calibration, objective revision) depend on #strategic-calibration, which is discussion-grade — the credit-assignment problem and execution-fidelity requirement are acknowledged but unresolved ( #strategic-calibration, Epistemic Status). The ordering of all five steps is forced by information dependency (each step's input depends on prior steps' output). The *content* of steps 3-5 — what exactly the agent computes and whether the quantities are estimable in practice — inherits strategic-calibration's discussion-grade status. What is NOT derived is the *timing* — how long the agent should spend on each step before proceeding.

The **convention hierarchy** ( #value-object) is *exact*: the three conventions (C1, C2, C3) are definitions, and the monotonicity result is a direct consequence of "better continuation policy yields higher expected value." The diagnostic implications table states what each convention's quantities mean by construction. The cascade's inferential force at steps 2-5 scales with the convention but the ordering is convention-independent.

## Discussion

**$G_t$ complexity bounded by $M_t$ capacity.** $\Sigma_t$'s evaluable complexity is bounded by $M_t$'s ability to observe which strategy edges are intact. An agent with poor model sufficiency ($S(M_t) \ll 1$) cannot meaningfully evaluate a complex $\Sigma_t$ — the strategic calibration residual requires adequate $M_t$ to distinguish "edge prediction wrong" from "observation too noisy to tell."

This creates a **virtuous cycle**: better $M_t$ → richer evaluable $\Sigma_t$ → better-directed action → faster $M_t$ improvement. And a **vicious one**: degraded $M_t$ → forced strategy simplification → cruder action → further $M_t$ degradation. The vicious cycle is the strategic analog of the death spiral described in the persistence condition ( #persistence-condition) — the agent loses the capacity to maintain complex plans, which reduces the quality of its actions, which further degrades its model.

**Connection to Boyd's OODA.** The orient cascade is the formal analog of Boyd's "Orient" — not just model updating, but the structured interaction between reality-understanding and strategy. Boyd's insight was that Orient is the critical step, not Decide. The cascade provides a mathematical mechanism consistent with this insight: Orient resolves the information dependencies that make Decide meaningful. An agent that skips to Decide (strategy revision) without adequate Orient (model update + attainability assessment) will revise its strategy based on stale or incorrect beliefs. Whether the dependency structure in the cascade captures the actual cognitive process Boyd described is an empirical question.

**Timescale structure.** The cascade implies a natural timescale ordering for the different update types:

$$\nu_{\text{epistemic}} \gg \nu_{\text{edge-update}} \gg \nu_{\gamma\text{-reclassify}} \gg \nu_{\text{prune/graft}} \gg \nu_{O\text{-revision}}$$

Weight updates are frequent (every observation). Combination-type reclassification is rare (needs strong structural evidence). Pruning/grafting is rarer still (abandon or create causal hypotheses). Objective revision is rarest (change what you want, not how you get it). This ordering is an empirical observation for many agent populations, consistent with the cascade but not derived from it.

## Working Notes

- The cascade as stated is sequential. In practice, agents may run steps in partial overlap — beginning to assess $\delta_{\text{sat}}$ before $M_t$ is fully updated, or revising edges while still processing observations. The cascade describes the *logical* dependency, not the *temporal* scheduling. An agent that parallelizes steps must still respect the dependencies (don't finalize strategy revision using a stale $M_t$).
- The resource allocation question (how much of the agent's tempo budget to spend on each step) is open and may be domain-dependent. In fast-changing environments, the agent may need to truncate early steps to keep up. In stable environments, the agent can spend more time on deep strategic evaluation.
- The virtuous/vicious cycle between $M_t$ quality and $\Sigma_t$ evaluable complexity is structurally motivated but not formally derived. Formalizing it would require a coupled dynamics model — possibly an extension of the persistence framework to the $(M_t, \Sigma_t)$ pair.
- **Strategy-maintenance status (updated).** The cascade's ORDERING is exact — forced by information dependency. The cascade's CONTENT for steps 3-5 has progressed: #credit-assignment-boundary characterizes the tractable/intractable boundary and establishes that persistence does not require credit assignment (Prop B.5); #strategic-dynamics-derivation verifies sector conditions for four topologies; #edge-update-via-gain has a default signal function candidate (gradient-based, satisfying directional fidelity). What remains domain-specific: the choice of signal function implementation, execution-fidelity monitoring, and handling of correlated failures (where $\hat P_\Sigma$ overestimates — #strategy-dag). The theory now provides the structural requirements and a default scheme; specific implementations are engineering, parallel to how the gain principle provides $\eta^\ast$ while Kalman/TD-learning/etc. are implementations.
