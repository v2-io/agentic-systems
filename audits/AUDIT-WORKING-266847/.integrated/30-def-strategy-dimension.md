# Reflection: def-strategy-dimension

## What the segment does

Decomposes G_t = (O_t, Σ_t): objective (evaluation — "how good is this trajectory?") vs strategy (guidance — "how do I produce a good trajectory?"). The split is definitional, not dynamic or timescale-based. Both axes vary independently: simple O_t with complex Σ_t (chess), complex O_t with simple Σ_t (multi-objective optimizer with gradient descent).

## The type-error correction

The critical repair: earlier formulations used δ_goal = G_t - M_t as goal mismatch. When Σ_t is a DAG, this is a type error — you cannot subtract a graph from a state vector. The satisfaction gap and control regret (which I haven't read yet) replace this with properly typed gap measures. This is a genuine architectural improvement.

## The strategy representation hierarchy

Four levels: none (reactive), cached policy, subgoal sequence, causal DAG. The trigger for moving up: when greedy optimization on Q_O fails because the environment has non-convex landscapes, prerequisite structure, or multi-step causal chains. This is the purposeful analog of structural-adaptation-necessity: inadequacy of the current Σ_t representation for the environment's causal complexity.

## The update-source distinction

O_t updates from external sources (assigned, discovered, revised); Σ_t updates from internal deliberation (cascade, evidence). This is a deeper distinction than just timescale — it's about information provenance. Strategy knowledge comes from the agent's deliberation and causal reasoning; objective knowledge comes from the principal-agent relation or discovery.

## The D_t/I_t commitment split (Working Notes)

The formalism doesn't distinguish "considering" (OR branch in Σ_t) from "committed" (resources allocated). This is flagged as potentially load-bearing in multi-agent settings. In Section III, shared desire vs shared commitment is a different concept from shared objectives.

## Naming targets

"Strategy dimension" is the segment name. "Causal DAG" for the richest Σ_t form. "Evaluation/guidance" as the O_t/Σ_t descriptive pair.

How valuable: 7/10 for surprise (the type-error correction is important), 9/10 for load-bearing (this is the G_t decomposition that everything downstream depends on).
