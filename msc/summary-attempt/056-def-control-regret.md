# Control Regret (definition — exact)

The second of the two orthogonal diagnostic quantities, completing the diagnostic split. **Control regret** is the gap between the best available value (objective attainability) and the value achieved by the agent's *current* policy. It is always non-negative by construction — the current policy cannot outperform the best in its class. When it is near zero, the agent is doing the best it can within its current model, policy class, and horizon. When it is large, there is room for improvement *without* changing the objective — the signal for strategy revision.

The diagnostic power emerges when satisfaction gap and control regret are read **together as a 2×2 cell map**:

|                                  | Goal attainable (sat-gap ≤ 0)            | Goal unmet (sat-gap > 0)                                                |
|----------------------------------|------------------------------------------|------------------------------------------------------------------------|
| Policy near-optimal (regret ≈ 0) | **Success**: goal achievable, policy good | **Capability limit**: optimally pursuing an unmet goal → check model, policy class, horizon, then consider revising objective |
| Policy suboptimal (regret > 0)   | **Strategy problem**: goal achievable, policy poor → revise strategy | **Both**: goal hard AND strategy weak → revise strategy first, then reassess |

Each cell prescribes a different corrective action. This is what makes the orient cascade (Chapter 5) *actionable*.

The framework names the **key insight** motivating the split: control regret can be *zero* while the agent is *optimally failing* — pursuing a goal that's beyond its reach, with no strategy improvement available. A single goal-distance signal could not distinguish this case from "bad strategy, achievable goal." The first warrants strategy revision; the second warrants goal revision (only after ruling out model, policy-class, and horizon inadequacy). Without the orthogonal split, the agent cannot tell these apart and may waste effort optimizing a strategy that is already near-optimal for an infeasible goal — or, conversely, may abandon a feasible goal because its strategy is weak.

Like the satisfaction gap, control regret is *convention-relative*: under the canonical one-step convention it reveals only the gap between the current first action and the best one-step deviation (a policy "locally near-optimal" under C1 may be globally suboptimal); under the Bellman convention it reveals the full gap to globally optimal. The framework recommends C2 (receding-horizon) for strategy revision as the most useful convention — captures recoverable suboptimality without requiring full Bellman solutions. Control regret is also where the *specific corrections* to make in the strategy come from: when regret is high, the *strategic-calibration residual* (defined in the next chapter) localizes the regret to specific parts of the strategy DAG — which edges to revise, which branches to prune, which alternatives to add.
