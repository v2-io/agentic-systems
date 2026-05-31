# 50 - strategy-structure-intro

Source: `01-aat-core/src/strategy-structure-intro.md`

## First-pass understanding

This chapter intro commits the strategy layer to a probabilistic causal DAG with AND/OR semantics and then previews the diagnostic split: satisfaction gap asks whether the best available policy can reach the objective threshold, while control regret asks whether the current policy is leaving value unused. The split is the point: "goal too hard" and "strategy too weak" require different remedies.

The intro also previews two structural supports. Chain confidence decays multiplicatively with depth, which makes deep plans fragile. Causal insufficiency in strategy graphs is handled explicitly through a correlation hierarchy, because hidden shared causes break naive AND/OR propagation and make redundancy look stronger than it is.

## Diagram attempt

The clearest diagram is the 2x2 diagnostic split. One axis is satisfaction gap, the other is control regret. The cells prescribe different next moves: continue, revise strategy, revise strategy then re-check attainability, or recognize a capability limit. This diagram directly captures why the two-signal formulation is better than a single goal-distance signal.

## Findings and watches

- Candidate finding: the intro says acyclicity is not chosen because it falls out of temporal ordering. That is true for time-indexed event tokens, but not for reusable event types, retry loops, maintenance cycles, feedback plans, or strategies with repeated subgoals unless the graph is explicitly unrolled in time. The DAG claim should state the time-unrolled/event-token condition.
- Watch: the Causal Markov property is said to be forced under causal sufficiency, while the same intro emphasizes that real strategy graphs often have latent common causes. The later correlation hierarchy needs to carry the burden of what remains exact under insufficiency.
- Watch: the 2x2 prescriptions are model-relative and convention-relative. `A_O` inherits the value-object convention (C1/C2/C3), current model limits, and policy class. Later diagnostics should keep those qualifiers visible.
- Watch: chain-confidence decay is elementary for a specified chain factorization, but "deep strategies are exponentially fragile" depends on probabilities staying below 1 and not being offset by redundancy, replanning, or correlation-aware structure.

## Local verdict

The chapter map is strong and the diagnostic split is promising. The main tightening needed at intro level is to state the representation conditions: strategy DAGs are acyclic when nodes are temporally situated event tokens or the cyclic policy/plan structure has been unrolled.
