# Reflection: def-strategy-dag

## What the segment does

Defines Σ_t = (V_t, E_t, p_t, γ_t): a DAG with probabilistic edges and AND/OR combination semantics. Acyclicity is derived from temporal ordering (not assumed). The Correlation Hierarchy (L0/L1/L1'/L2) characterizes when the independence-assuming AND/OR propagation is correct.

## The key insight: causal sufficiency → edge independence

Edge independence is NOT a separate assumption — it's a consequence of causal sufficiency (all common causes represented as nodes in the graph). The CMC theorem (#deriv-graph-structure-uniqueness) proves: causal sufficiency → exogenous independence → Markov factorization → correct AND/OR propagation. When the DAG is causally insufficient (the dominant real-world case), edge outcomes are correlated and the independence model is biased.

Direction of bias:
- AND-nodes: independence model underestimates (conservative)
- OR-nodes: independence model OVERESTIMATES (optimistic — more dangerous)

OR-dominated roots (multiple alternative paths) produce systematic overconfidence in plan success. This is the dominant practical case.

## The Correlation Hierarchy (L0/L1/L1'/L2)

The four-level hierarchy is the most technically sophisticated part of the segment:
- L0 (independence): correct when DAG is causally sufficient. Tractable O(|V|+|E|).
- L1 (strict prerequisites): add common-cause nodes as AND-prerequisites. Correct when θ_child|¬C ≈ 0.
- L1' (mixture form): split into two conditional sub-DAGs weighted by P(C). Correct when C is observable. Identifiability-OBSTRUCTED when C is unobservable (Fisher rank-1; Cramér-Rao floor).
- L2 (full correlation): exponential — mathematical ideal only.

The L1 vs L1' distinction is the key practical decision: strict prerequisite (C being absent makes children fail) → factor above as AND-prerequisite. Soft facilitator (C being absent reduces but doesn't eliminate child success) → use mixture form, verify C observability.

## Naming targets surfaced

The Correlation Hierarchy (L0/L1/L1'/L2) — is this named in the tracker?
"Plan-confidence score" P̂_Σ
"Causal efficacy estimate" for edge credence
"Strategy self-assessment"
The L1 "factor above the correlation" construction principle

Looking for these in the tracker...

## The identifiability obstruction under unobservable common cause

"Not open but structurally refuted" — when C is unobservable and a soft facilitator, L1' fails by the Cramér-Rao floor. The agent must either augment C-observability, run multi-child joint observations, or fall back to L0-on-marginals. This is an identifiability-floor instance (meta-pattern #disc-identifiability-floor).

## Single-parameter edge convergence

The single-parameter edge (p_ij, not (p_ij, θ_ij)) came from convergence across three independent formalism attempts. The Noisy-OR and WEIGHTED alternatives were rejected. This is a strong convergence signal.

## Acyclicity derivation

Clean and elegant: each node has temporal position τ_i > t, edges require τ_i < τ_j, a cycle would require τ_i < τ_j < ... < τ_i, which is impossible for a real-valued time index. Iteration ("try A, fail, try A again") is modeled as distinct time-indexed attempts — the apparent cycle unfolds as a linear chain.

## Wandering thoughts

The "depth penalty on calibration" insight is important: deeper edges are tested less often (only when all upstream edges succeed), so their calibration converges slower — evidence starvation. AND strategies with deep chains face double penalty: lower confidence AND slower convergence. This creates structural pressure toward shallow observable strategies.

The terminal alignment error (achieve terminals, but V_O(τ) < V_O_min) is flagged as potentially deserving its own diagnostic signal (δ_align) alongside δ_sat, δ_regret, δ_strategic. Whether to formalize it is open. The segent notes it's "detectable only through experience, not through a priori analysis."

How valuable: 10/10 for load-bearing (this is the strategy DAG definition — the core formal object of Section II), 9/10 for surprise (the Correlation Hierarchy is more developed than I expected; the L1/L1' distinction is a real contribution).
