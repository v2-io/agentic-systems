# Reflection: result-structural-adaptation-necessity

**Segment:** `#result-structural-adaptation-necessity`

## What this does

Conditional result: When model class fitness F(ℳ) < 1 - ε, no parametric adaptation within ℳ can close the mismatch floor. The agent must change its model class, not just its parameters.

Epistemic status: Conditional on alignment assumption (step 2 → step 3 requires that lost predictive information affects the one-step conditional mean, not just higher moments). Without the alignment assumption, the conclusion holds for proper-scoring regret instead.

Key structural concepts:
- Structural adaptation as structural persistence failure (the effective α shrinks, not because disturbance increased, but because the correction function loses capacity to point inward)
- Three observable symptoms of model class inadequacy (persistent irreducible mismatch, gain collapse without performance, systematic mismatch patterns)
- Structural overfitting as the opposite failure: information bottleneck diagnostic
- Mechanisms: decomposition-recombination, expansion, compression, grafting
- Miller's neutral variation mechanism (extreme transition motif in coevolving automata)

## Naming relevance

Row 293 (structural adaptation necessity) — let me check what the tracker says. The key question: is "structural adaptation necessity" the right name?

"Structural adaptation necessity" names the result by what it proves — the necessity of structural (vs. parametric) adaptation. This is correct. The result IS about when structural adaptation becomes necessary. "Model class sufficiency" would name the threshold condition rather than the result.

"Structural change necessity" would be a rename. Less precise: "change" is weaker than "adaptation."

## New naming targets surfaced

**Model class fitness F(ℳ)**: The quantitative fitness measure for a model class. Whether this is in the tracker...

**Structural overfitting**: Named failure mode (too expressive model class). Distinct from structural underfitting (inadequate model class). Row in tracker?

**Neutral variation**: Miller's mechanism for structural change in coevolving systems. The "extreme transition motif" is a named mechanism. Row in tracker?

**Latent structural diversity**: "variation in agent architectures that is invisible to current performance but consequential under regime change." Named concept.

**Systematic mismatch patterns**: One of three diagnostic symptoms. This is a named observation.

## What's excellent here

The bidirectionality of structural adaptation is philosophically important: structural adaptation can mean either expansion (too constrained) or compression (too expressive). The information bottleneck diagnostic for the compression case is correct and important.

The Miller neutral variation mechanism is well-integrated: it's adopted as prior work (Miller 2022, *Ex Machina*) and connected to the framework's own structural adaptation result. The concept of latent structural diversity is surfaced as an open formalization problem for Section III.

The connection between structural adaptation and deliberation cost is explicitly marked as "an informal analogy, not a consequence" — this is good epistemic discipline.
