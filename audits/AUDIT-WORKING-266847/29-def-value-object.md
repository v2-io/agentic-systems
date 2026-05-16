# Reflection: def-value-object

## What the segment does

Develops the value object V_O(M_t, π; N_h) = E[V_{O_t}(τ) | M_t, π] and its action-value form Q_O using the do-operator. Introduces the three-convention hierarchy (C1: one-step improvement, C2: receding-horizon, C3: Bellman) with the monotonicity result A_O^(1) ≤ A_O^RH ≤ A_O^B. Adopts C1 as the canonical default.

## The causal validity argument

Two mechanisms ensure causal validity of Q_O:
1. do-operator severs the dependence on G_t through action selection
2. π_cont is a fixed parameter, not derived from evolving G_t

Together, Q_O depends on M_t alone as a state variable (conditional on fixed O_t, π_cont, N_h). This is stronger than predictive sufficiency (Level 1 associational) — causal validity additionally requires no unmodeled common cause.

For Class 2 agents: M_t carries goal-conditioned bias, degrading causal validity. The spike reference is explicit.

## The convention hierarchy monotonicity

The monotonicity derivation is clean: better continuation policy → weakly higher expected trajectory value. The ordering of continuations (current ≤ receding-horizon ≤ optimal) forces the ordering of A_O values. The diagnostic implications follow: C1 is most conservative (may diagnose "locally stuck" when globally recoverable); C3 is most powerful (diagnoses "genuinely infeasible" given M_t, Π, N_h).

The corollary on δ_sat and δ_regret is exact: δ_sat ordering reverses (higher A_O → lower δ_sat), δ_regret ordering follows A_O direction (C3 reveals largest regret because it compares against globally optimal policy).

## Naming targets surfaced

The segment introduces "value object," "action-value form," "convention hierarchy" (C1/C2/C3), "one-step improvement" as canonical default. These are likely in the tracker.

The λ(M_t, O_t, N_h) exploration weighting is mentioned as structurally motivated but not derived — this is an open naming target if the concept gets a name.

## Wandering thoughts

The C1 canonical default connects back to the incremental update philosophy (η* in emp-update-gain): the agent doesn't optimize globally, it improves incrementally. This is a coherent philosophy: both the epistemic and the purposeful layers default to incremental improvement over fixed reference points, not global optimization. The parallelism is elegant.

The LLM context turnover note: N_h has a natural bound in the current session. The continuation policy is whatever the next instance will do, which the current instance cannot control. This is the formal basis for why LLM agents should be skeptical of long-horizon plans.

How valuable: 8/10 for load-bearing (the convention hierarchy and its monotonicity is a genuine contribution), 7/10 for surprise (the λ(M_t, O_t, N_h) extension is non-obvious — exploration pricing should depend on the objective and horizon).
