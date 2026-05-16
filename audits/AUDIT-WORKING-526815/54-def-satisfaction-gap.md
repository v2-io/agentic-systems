# 54 - def-satisfaction-gap

Source: `01-aat-core/src/def-satisfaction-gap.md`

## First-pass understanding

This segment defines objective attainability `A_O` as the supremum of value over an available policy class, current model, and horizon. The satisfaction gap is then `V_O^min - A_O`: positive means the threshold is not reachable under the current measurement setup; non-positive means the objective is attainable in that setup.

The segment is careful about the important qualifiers. The gap is not truth about the world; it is a belief-relative, policy-class-relative, horizon-relative, scalarization-relative diagnostic. A positive gap can mean infeasible objective, too-narrow policy class, too-short horizon, bad model, or jointly infeasible objectives. Objective revision is therefore last in the diagnostic order, not the first response.

## Diagram attempt

The clearest diagram is a value line: the best attainable value `A_O` sits somewhere relative to the threshold `V_O^min`. The signed distance from `A_O` to the threshold is the satisfaction gap. I added the C1/C2/C3 convention stack as a side panel because the same objective can look unattainable locally and attainable under a stronger continuation convention.

## Findings and watches

- Watch: this segment inherits the C1/C2/C3 monotonicity claim from `def-value-object`. My earlier concern remains: C2 receding-horizon monotonicity over C1 is not automatic unless the shorter-horizon replanning objective is aligned with the full evaluated horizon or has a safe fallback/full-horizon comparison.
- Watch: `A_O` is a supremum. Wording such as "best policy" should not imply an attainable maximizer unless compactness/continuity or an argmax convention is supplied.
- Watch: the diagnostic is only as good as `V_O^min`. Utility objectives without a natural threshold require an explicit threshold choice, which can dominate the resulting sign of the gap.
- Watch: the active-inference comparison is conceptual positioning. The local AAT definition does not depend on that contrast.

## Local verdict

The definition itself is strong and appropriately qualified. The main open issue is inherited convention hierarchy mathematics, not the satisfaction-gap quantity.
