# 40 - def-value-object

Source: `01-aat-core/src/def-value-object.md`

## First-pass understanding

This segment turns the abstract objective functional into decision quantities. `V_O(M_t, pi; N_h)` is expected trajectory value under the agent's model, objective, continuation policy, and horizon. `Q_O(M_t, a; pi_cont, N_h)` is the interventional action-value form: force action `a` now with `do(a_t=a)`, then follow a specified continuation policy. The segment is careful that `O_t`, `pi_cont`, and `N_h` are parameters, while `M_t` is the state variable used for the query.

The segment then defines three continuation conventions: C1 one-step improvement with current policy continuation, C2 receding-horizon replanning, and C3 Bellman/global optimality. The convention is part of the measurement: satisfaction gap and control regret mean different things under C1, C2, and C3. This is a useful move, especially because it makes the conservative C1 default explicit rather than burying it inside later diagnostics.

## Diagram attempt

I used a value-query pipeline: `M_t` plus fixed parameters generate a model-based trajectory distribution under `do(a)`, the objective functional scores trajectories, and diagnostics read off expected value. I also drew the current-policy selection mechanism as a severed path, because the `do`-operator is the conceptual center of `Q_O`. A small convention ladder sits underneath, with a warning that the C2 rung is not automatically monotone unless the replanning objective is aligned with the full evaluated horizon.

## Findings and watches

- Candidate finding: the causal-validity claim is too strong if it rests on predictive sufficiency plus directed separation alone. The `do(a)` notation defines an interventional query, but estimating it requires that `M_t` contain or identify the relevant causal/action-transition structure. Observational predictive sufficiency and goal-blind processing do not by themselves guarantee valid interventional expectations.
- Candidate finding: the claimed monotonicity `A_O^(1) <= A_O^RH <= A_O^B` is not generally exact for receding-horizon control with a shorter replanning horizon `N_r`. Myopic replanning can choose actions that are locally optimal over `N_r` but worse for the full evaluated horizon `N_h` than continuing `pi_current`. The inequality holds only under additional conditions, such as C2 optimizing the same full-horizon objective, including C1 as an admissible fallback with value comparison on the full horizon, or having terminal/value functions that make the shorter-horizon replans consistent.
- Watch: frontmatter says `status: exact`, while the segment itself says definitions are exact, causal validity is conditional, and the convention hierarchy is exact. If monotonicity is weakened, the segment-level status should probably be split or downgraded.
- Watch: the formula treats `O_t` as a fixed parameter, which is fine locally, but since `O_t` is part of `G_t`, downstream text should not say the value object is independent of `G_t` without the same "holding objective fixed" qualification.

## Local verdict

The definitions of `V_O` and `Q_O` are useful and precise as definitions. The risky parts are theorem-like: causal validity needs explicit causal-model assumptions, and the receding-horizon rung of the convention hierarchy needs additional hypotheses before the monotonicity result is true.
