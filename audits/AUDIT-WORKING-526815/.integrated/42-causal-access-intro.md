# 42 - causal-access-intro

Source: `01-aat-core/src/causal-access-intro.md`

## First-pass understanding

This chapter intro connects the value object to causal access. `Q_O` requires an interventional quantity, `P(o | do(a), M_t)`, and the intro argues that an adaptive agent's own loop supplies Level-2-character data: the agent acts, the world responds, and the action/consequence pair is not just a passive association. The chapter then immediately qualifies this with admissibility regimes, confounding, delayed effects, partial observability, and on-policy selection bias.

The strongest conceptual contribution is the distinction between having action-coupled experience and having identified causal effects. The loop gives the agent a substrate from which causal knowledge can be learned, but positive feedback can also launder confounded wins into confident false models because on-policy success removes the mismatch pressure that would otherwise trigger revision.

## Diagram attempt

The clearest diagram is a three-layer loop. At the physical layer, the action really changes the world. At the data layer, the logged pair has intervention character. At the identification layer, hidden state, policy selection, delayed outcomes, and partial observability decide whether that data estimates the desired `do(a)` query. This prevents the diagram from collapsing "the agent acted" into "the causal effect is identified."

## Findings and watches

- Candidate finding: the intro sometimes overstates the loop-as-Level-2 claim. An executed action is an intervention in the world, but on-policy action-outcome logs are not automatically clean samples of `P(o | do(a))` for planning. If the policy depends on latent state that also affects outcomes, the action is selected by a confounded mechanism even though it causally precedes the observation. The text should distinguish physical intervention, interventional-character data, and identifiable interventional distribution.
- Candidate finding: the intro uses the older scalar unified objective with `lambda(M_t)`, while `def-value-object` just updated the structurally motivated extension to `lambda(M_t, O_t, N_h)`. The intro may intentionally be previewing the older CIY form, but it should either adopt the newer parameterization or label the displayed equation as the pre-value-object shorthand.
- Watch: the positive-confounded-win story is plausible and useful, but it depends on gain dynamics, on-policy sampling, and the absence of disconfirming interventions. Later proof-bearing segments should state those conditions rather than relying on the narrative alone.
- Watch: the pre-compiled/learning-agent distinction narrows Section II after earlier segments used thermostats/PID controllers as examples of reactive strategies and indifferent continuity. Final audit should track whether this is a clean scope split or another agent/adaptive-system vocabulary drift.

## Local verdict

The chapter intro has the right cautionary instincts: action-coupled data is powerful, but not magic. The most important tightening is terminological. "Level-2 engine" should mean the loop can generate interventions, not that ordinary on-policy logs already solve causal identification.
