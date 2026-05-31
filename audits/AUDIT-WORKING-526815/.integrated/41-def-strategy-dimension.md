# 41 - def-strategy-dimension

Source: `01-aat-core/src/def-strategy-dimension.md`

## First-pass understanding

This segment decomposes purposeful state as `G_t = (O_t, Sigma_t)`: objective evaluates trajectories, while strategy guides action sequences that might satisfy the objective. The distinction is typed rather than temporal: `O_t` answers "how good is this trajectory?", and `Sigma_t` answers "how do I produce one?" Strategy can be absent/reactive, cached, sequential, or DAG-like.

The strongest part is the independence of richness. A simple objective can require a complex strategy, and a complex objective can be paired with a simple strategy engine. That prevents a single "goal complexity" axis from conflating what the agent wants with how much procedural or causal structure it has for achieving it.

## Diagram attempt

The natural picture is a two-axis map: objective richness on one axis and strategy richness on the other. Examples then land in different quadrants: chess has simple objective/complex strategy; multi-objective gradient descent has complex objective/simple strategy; a thermostat is simple on both. This diagram is useful because it makes the claimed independence visually immediate.

## Findings and watches

- Soft candidate: the decomposition is clean as an analytical factorization, but some agents do not maintain `O_t` and `Sigma_t` as internally identifiable state. A reactive controller or end-to-end learned policy may have an objective in the training/deployment sense and a strategy in the analyst's interpretation, without storing separable objective and guidance components. The segment should distinguish internal representation from ascribed decomposition.
- Watch: the table says objective update source is external while strategy update source is internal. Earlier continuity/self-actuation discussion allows objective revision by the agent, so this should be read as typical provenance rather than a structural rule.
- Watch: the discussion uses `Q_O` from `def-value-object`, but that segment is not in the declared dependencies. The definition itself does not need `Q_O`, so this may be acceptable if dependency metadata tracks only formal dependencies.
- Watch: resource costs, commitment state, and strategy compression are acknowledged as open. Later strategy-DAG claims should not silently rely on them as already modeled.

## Local verdict

The objective/strategy distinction is a good type split and should reduce later category errors. The main qualification is representational: for many agents this is a useful decomposition of purposeful function, not necessarily a literal inspectable pair of internal variables.
