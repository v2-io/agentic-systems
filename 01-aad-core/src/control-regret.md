---
slug: control-regret
type: definition
status: exact
depends:
  - value-object
  - satisfaction-gap
stage: claims-verified
---

# Definition: Control Regret

Control regret measures the gap between the best available one-step policy improvement and the agent's current policy, under the current model and horizon. Under the canonical continuation convention ( #value-object), this is a *local* diagnostic — it answers "could I do better right now?" not "is my overall strategy globally suboptimal?" A revisable policy may show low δ_regret simply because continuation is frozen. This is the signal for strategy revision, with the caveat that the signal's scope matches the continuation convention's scope.

## Formal Expression

*[Definition (control-regret)]*

$$\delta_{\text{regret}} = A_O(M_t;\, \Pi, N_h) - V_O(M_t, \pi_{\text{current}};\, N_h) \geq 0$$

Always non-negative: the current policy cannot outperform the best in its class.

- $\delta_{\text{regret}} \approx 0$: The agent is doing the best it can within current $(\Pi, N_h, M_t)$. If $\delta_{\text{sat}} \gt 0$ simultaneously, the problem is not the current strategy — it's either the goal, the capability ($\Pi$, $N_h$), or the model ($M_t$). See #satisfaction-gap's disambiguation.
- $\delta_{\text{regret}} \gg 0$: There's room for improvement without changing $O_t$. → Revise $\Sigma_t$.

## Epistemic Status

*Exact as a definition — convention-relative as a diagnostic.* Like the satisfaction gap, this is a mathematical definition — a difference between two values of the same functional. The quantity is well-defined; computing it requires evaluating $A_O$ (generally intractable) and $V_O$ under the current policy (tractable in simulation, approximate in practice).

**Convention hierarchy.** $\delta_{\text{regret}}$ inherits the continuation convention from #value-object. Under the monotonicity result: $\delta_{\text{regret}}^{(1)} \leq \delta_{\text{regret}}^{\text{RH}} \leq \delta_{\text{regret}}^{\text{B}}$. C1 (one-step) reveals only the gap between the current first action and the best one-step deviation — a policy that is "locally near-optimal" under C1 may be globally suboptimal. C3 (Bellman) reveals the full gap to the globally optimal policy. C2 (receding-horizon) interpolates: it captures regret from suboptimal first actions that become visible with $N_r$-step lookahead. For strategy revision, C2 is often the most useful convention: it reveals recoverable suboptimality without requiring the full Bellman solution.

## Discussion

**The diagnostic power of the two-gap system.** The satisfaction gap and control regret together encode a 2×2 diagnostic:

| | $\delta_{\text{sat}} \leq 0$ (attainable) | $\delta_{\text{sat}} \gt 0$ (unmet) |
|---|---|---|
| $\delta_{\text{regret}} \approx 0$ (near-optimal) | **Success**: goal achievable, policy good | **Capability limit**: optimally pursuing an unmet goal → check $M_t$, $\Pi$, $N_h$, then consider revising $O_t$ |
| $\delta_{\text{regret}} \gg 0$ (suboptimal) | **Strategy problem**: goal achievable, policy poor → revise $\Sigma_t$ | **Both**: goal hard AND strategy weak → revise $\Sigma_t$ first, then reassess $\delta_{\text{sat}}$ |

This diagnostic is what makes the orient cascade ( #orient-cascade) actionable: each cell prescribes a different corrective action.

**Control regret as the signal for $\Sigma_t$ revision.** When $\delta_{\text{regret}}$ is high, the agent knows it could do better with a different strategy. The *specific* corrections — which edges to revise, which branches to prune, which alternatives to add — come from the strategic calibration residual ( #strategic-calibration), which localizes the regret to specific parts of $\Sigma_t$.

**Regret approaching zero when optimally failing.** This is the key insight motivating the two-gap split. A single $\delta_{\text{objective}}$ would show "large gap" for both "bad strategy, achievable goal" and "good strategy, impossible goal." The first warrants strategy revision; the second warrants goal revision (after ruling out $M_t$/$\Pi$/$N_h$ inadequacy). Without the split, the agent cannot distinguish these cases and may waste effort optimizing a strategy that's already near-optimal for an infeasible goal.
