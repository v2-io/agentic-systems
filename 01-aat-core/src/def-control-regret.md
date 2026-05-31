---
slug: def-control-regret
type: definition
status: exact
depends:
  - def-value-object
  - def-satisfaction-gap
stage: draft
---

# Definition: Control Regret

The second of two orthogonal diagnostic quantities, completing the diagnostic split with #def-satisfaction-gap. **Control regret** $\delta_{\text{regret}}$ is the gap between the best available value (objective attainability $A_O$) and the value achieved by the agent's *current* policy. It is always non-negative by construction — the current policy cannot outperform the best in its class. Near zero means the agent is doing the best it can within its current model, policy class, and horizon; large means there is room for improvement *without* changing the objective — the signal for strategy revision.

The diagnostic power emerges when satisfaction gap and control regret are read **together as a 2×2 cell map** (full table in Discussion): each cell of `goal-attainable × policy-near-optimal` prescribes a different corrective action — success, strategy-revision, capability-limit (consider objective revision after $M_t/\Pi/N_h$ checks), or both-strategy-and-goal. This is what makes the orient cascade ( #der-orient-cascade) *actionable*: each cell routes revision pressure to a different substate. The key insight motivating the split is that $\delta_{\text{regret}}$ can be *near zero* while the agent is *optimally failing* — pursuing a goal beyond its reach with no strategy improvement available; a single goal-distance signal could not distinguish this from "bad strategy, achievable goal."

Like the satisfaction gap, control regret is **convention-relative**: under C1 (one-step) it reveals only the gap between the current first action and the best one-step deviation (a policy "locally near-optimal" under C1 may be globally suboptimal); under C3 (Bellman) it reveals the full gap to the globally optimal policy. C2 (receding-horizon) is often the most useful convention for strategy revision — captures recoverable suboptimality without requiring full Bellman solutions. Control regret is also where the *specific corrections* come from: when $\delta_{\text{regret}}$ is high, the strategic calibration residual ( #def-strategic-calibration) localizes the regret to specific parts of the strategy DAG.

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

**Bounded control regret as a finite-passivity diagnostic (Cheung-Piliouras-Tao 2021).** Cheung, Piliouras & Tao (2021, *Online Optimization in Games via Control Theory: Connecting Regret, Passivity and Poincaré Recurrence*, arXiv:2106.04748) prove (Theorem 8) that any finitely-passive learning dynamic guarantees constant regret. Read contrapositively: bounded control regret growth is an observable signature that the agent's update operator has finite-passive structure (sits in the certificate-cone interior per `#result-certificate-existence`); unbounded growth in control regret indicates the update is not finitely-passive — potentially escaping the certificate's interior into the no-certificate regime where the persistence machinery does not apply. The bridge is *qualitative only*: CPT's storage function $L$ (on cumulative-payoff space) and AAT's certificate $V(e) = e^\top \mathcal{M} e$ (on strategy-error space) have different functional forms and live on different state spaces — the structural identification "finite passivity ⟺ certificate-interior regime" survives at the level of regimes, not at the level of identifying $L$ with $V$.

## Working Notes

- **Cross-reference to NeurIPS Paper 2.** Together with `#def-satisfaction-gap`, this segment is **Component 1** of NeurIPS 2026 Paper 2's composition theorem ("A Unified Convergence Theory for Non-Stationary Reinforcement Learning", `~/src/neurips/02-unified-convergence-rl/`, §4 Theorem 4.1). The two-gap orthogonality is what gives the composed regret bound a principled coordinate for "is the binding pressure on goal-feasibility or on policy-quality?" Sibling segment `#def-satisfaction-gap` carries the matching cross-reference. See `msc/neurips-back-integration-2026-05-08.md` §1 Paper 2.
