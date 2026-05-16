# 48 - norm-explicit-strategy-condition

Source: `01-aat-core/src/norm-explicit-strategy-condition.md`

## First-pass understanding

This segment gives a simple design inequality: maintain an explicit strategy when planning plus maintenance costs are lower than exploration plus repair costs, assuming the two approaches produce roughly equivalent non-temporal outcomes. It is not framed as a theorem; it is a normative criterion for when explicit `Sigma_t` is worth the tempo/cost burden.

The most important qualification is already in the text: if model-based planning and loop-based exploration produce different final value, risk, reversibility, or model-error profiles, the scalar cost comparison is insufficient. Then the decision needs expected regret or richer analysis rather than a simple threshold.

## Diagram attempt

The diagram is a balance with a gate. The inequality only applies after the equivalence precondition is satisfied and after costs are put into a common unit. If the gate fails, the flow goes to a richer risk/regret analysis. This captures the segment's useful modesty.

## Findings and watches

- Soft candidate: the epistemic section says explicit `Sigma_t` inherits biases of `M_t`, while loop-based learning does not. Direct exploration can still be biased by policy selection, partial observability, confounding, update rules, and the model used to interpret observations. The contrast should be "planning inherits model bias differently" rather than "loop learning does not."
- Soft candidate: the normative grounding says the preference for persistence margin is hard to argue against. Earlier continuity-stance work says some agents are task-terminal, indifferent, or negotiated about continuation. The criterion is compelling for agents whose objectives require ongoing persistence, but it should not override the objective's stance toward continuation.
- Watch: the segment grounds the criterion in `result-persistence-condition`, but that segment is not declared as a dependency. This may be acceptable if Discussion dependencies are not tracked, but the grounding is substantive.
- Watch: all costs need common units and expected/risk-adjusted treatment. Irreversible damage and heavy-tailed repair costs will not be well represented by a static scalar inequality unless the cost measure already embeds risk.

## Local verdict

The inequality is useful as a design heuristic and is honest about its preconditions. The main edits should prevent it from implying that exploration is unbiased or that persistence margin is universally terminally valuable.
