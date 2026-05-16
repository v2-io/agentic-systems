# Reflection: def-strategy-dag

**Segment:** `#def-strategy-dag`

## What this does

Defines Σ_t = (V_t, E_t, p_t, γ_t) — the probabilistic causal DAG with AND/OR semantics.

Key architectural choices:
- Acyclicity: DERIVED from temporal ordering, not assumed (causes precede effects)
- Markov factorization: PROVED under causal sufficiency via CMC theorem
- AND/OR parameterization: CHOSEN (parsimony + convergence across 3 formalism attempts)
- Single-parameter edges: CHOSEN over (p, θ) two-parameter form

The Correlation Hierarchy is the key practical addition:
- L0 (Independence): AND/OR as-is — tractable but systematically overestimates when DAG is causally insufficient
- L1 (Augmented DAG, strict prerequisites): common-cause nodes factored above the correlation they create — exact for strict prerequisites
- L1' (Mixture form, soft facilitators): conditional sub-DAGs weighted by P(C) — requires C observable
- L2 (Full correlation): exponential in common-cause states — mathematical ideal only

Plan-confidence score: P̂_Σ = s_v_root — the DAG's own answer to "will this plan work?" Correct only when DAG is causally sufficient.

## Naming relevance

Multiple rows affected by this segment:

**Row for "strategy DAG"**: This IS the defining segment. "Strategy DAG" is exactly right — Σ_t is a DAG, it's the strategy. The subject-noun is correct.

**Correlation Hierarchy**: Named concept in this segment. L0/L1/L1'/L2 form a named taxonomy. Need to check tracker.

**Plan-confidence score**: Named quantity P̂_Σ. Whether in tracker...

**Causal efficacy estimate**: Named for edge semantics p_ij. Whether in tracker...

**Evidence starvation effect**: Named effect: deeper edges are tested only when all upstream edges succeed. Attenuated correction rate.

## What's excellent here

The distinction between derived structure (DAG from temporal ordering + CMC theorem) and chosen parameterization (AND/OR + single parameter) is architecturally crucial and explicitly stated. "What remains a formulation choice is the parameterization within the DAG structure."

The Correlation Hierarchy is now first-class in the Formal Expression. The relationship between causal sufficiency, edge independence, and P̂_Σ accuracy is grounded by the CMC theorem. This is a significant technical addition.

The terminal alignment error concept (Working Notes) is important: when the agent achieves terminal conditions but V_{O_t}(τ) < V_min, the well-formedness belief was wrong. Named as a potential diagnostic signal δ_align. Currently open whether to formalize.

The evidence starvation effect: deeper edges face double penalty (lower aggregate confidence AND slower convergence). This reinforces structural pressure toward shallow, observable strategies.
