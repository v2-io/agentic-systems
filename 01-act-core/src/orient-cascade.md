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
---

# Derived: Orient Cascade

For actuated agents, epistrophe (the corrective phase of the cycle) expands into a multi-step cascade. The resolution order is forced by information dependency: epistemic update first, then attainability assessment, then strategy evaluation, then (if needed) objective revision. Each step's input depends on the output of prior steps. The ordering is not a design choice — it's a consequence of which quantities require which others.

## Formal Expression

*[Derived (orient-cascade, from information dependency between mismatch types)]*

1. **Reduce $\delta_{\text{epistemic}}$** — understand reality.
   Update $M_t$ via #mismatch-signal and #update-gain. Prerequisite for all purposeful evaluation, because $M_t$ appears in every subsequent formula.

2. **Evaluate $\delta_{\text{sat}}$** — is the goal achievable?
   Compute $A_O(M_t; \Pi, N_h)$ using the updated $M_t$. Requires adequate $M_t$ to assess attainability ( #satisfaction-gap).

3. **If feasible ($\delta_{\text{sat}} \leq 0$), evaluate $\delta_{\text{regret}}$** — is the policy suboptimal?
   Compare $A_O$ to $V_O(M_t, \pi_{\text{current}}; N_h)$. Requires both adequate $M_t$ and meaningful $A_O$ ( #control-regret).

4. **If $\delta_{\text{regret}}$ high, evaluate $\delta_{\text{strategic}}$** — is the plan's causal model wrong?
   Examine edge residuals. Requires adequate $M_t$, feasible $O_t$, and evidence of suboptimal execution ( #strategic-calibration).

5. **If $\delta_{\text{sat}} \gt 0$ persists across $\Sigma_t$ revisions** — revise $O_t$.
   The cascade's ordering ensures objective revision is the last resort, not the first response to unmet goals.

**Derivation.** Each step's input depends on prior steps' outputs:
- You cannot evaluate strategy quality with a broken reality model (step 3 requires step 1)
- You cannot distinguish bad strategy from infeasible goal without evaluating attainability first (step 4 requires step 2)
- You should not revise the objective until you've verified that improving $\Sigma_t$ cannot close the gap (step 5 requires steps 3-4)

The ordering is forced by information dependency.

## Epistemic Status

The cascade **ordering** is *exact*: it is a logical consequence of which quantities appear in which formulas. Steps 1-2 (epistemic update, attainability assessment) rest on well-typed quantities ( #mismatch-signal, #satisfaction-gap) and exact derivation. Steps 3-5 (control regret, strategic calibration, objective revision) depend on #strategic-calibration, which is discussion-grade — the credit-assignment problem and execution-fidelity requirement are acknowledged but unresolved ( #strategic-calibration, Epistemic Status). The ordering of all five steps is forced by information dependency (each step's input depends on prior steps' output). The *content* of steps 3-5 — what exactly the agent computes and whether the quantities are estimable in practice — inherits strategic-calibration's discussion-grade status. What is NOT derived is the *timing* — how long the agent should spend on each step before proceeding.

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
- **The strategy-maintenance loop is the least closed part of Section II.** Steps 3-5 depend on machinery that has multiple open pieces: the signal function in #edge-update-via-gain is undefined, credit assignment in #strategic-calibration is unresolved, execution fidelity monitoring is assumed but not formalized, and the plan-confidence score ( #strategy-dag) systematically overestimates under correlated failures. The cascade's ORDERING is exact; the cascade's CONTENT for strategy revision is an architectural sketch, not an operational specification. This is the honest state: the theory identifies what information dependencies must be respected but does not yet specify how the strategy-revision computations work in practice.
