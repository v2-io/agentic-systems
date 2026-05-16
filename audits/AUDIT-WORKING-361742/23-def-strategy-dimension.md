# Reflection: def-strategy-dimension

**Segment:** `#def-strategy-dimension`

## What this does

Decomposes G_t = (O_t, Σ_t):
- O_t: evaluation ("Is this trajectory satisfactory?")
- Σ_t: guidance ("Which action sequence produces a satisfactory trajectory?")

Key: this is a definitional split, not a timescale or dynamic claim. O_t and Σ_t answer different questions and carry different kinds of information.

Four levels of strategy representation:
1. None (reactive) — thermostat, reflex
2. Cached policy — trained RL policy
3. Subgoal sequence — navigation, recipe
4. Causal DAG — military plan, software project

## Naming relevance

Row for "strategy dimension" — The naming question is whether "strategy dimension" is the right name. The segment defines the split G_t = (O_t, Σ_t). "Strategy dimension" names the Σ_t component. But the segment defines BOTH components as parts of G_t.

Actually, the segment is ABOUT the G_t = (O_t, Σ_t) split — the "strategy dimension" of G_t. This is what the segment names: the strategy dimension alongside the objective dimension. The name is correct.

"Strategy-objective split" or "purposeful state decomposition" would be alternatives. But "strategy dimension" names the structural claim: there IS a strategy dimension to G_t, separate from the objective dimension. Both are named; the segment is about introducing and defining Σ_t in particular.

## Key terms from this segment

**Σ_t (strategy)**: The formal symbol. Row 10 in tracker.

**Causal DAG strategy**: The highest level of strategy representation. Named.

**G_t = (O_t, Σ_t) split**: Already voted in row 105 (G_t = (O_t, Σ_t)). This confirms the split is the core architectural claim.

**Timescale ordering**: ν_M ≫ ν_Σ ≫ ν_O — an empirical observation, explicitly not derived.

**Commitment state (D_t/I_t)**: Mentioned in Working Notes as open question for Section III. Not yet a formal term.

## What's excellent here

The type-error resolution is important: the old "δ_goal = G_t - M_t" formulation was a type error (cannot subtract a graph from a vector). The satisfaction gap and control regret replace this with properly typed gap measures. This is exactly the kind of mathematical hygiene that makes a theory sound.

The independence of O_t and Σ_t richness has architectural implications: you can upgrade the strategy engine without changing the objective representation, and vice versa. Chess example: simple O_t (win), complex Σ_t (opening theory, tactics, endgame).
