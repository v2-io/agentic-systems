# 03 — def-action-transition

Dependencies checked: `def-agent-environment` already read.

## Reflection

This segment closes the loop with $\Omega_{t+1}\sim T(\cdot\mid\Omega_t,a_t)$ and explicitly says actions affect the environment.
It confirms the concern from segment 01: the primitive "agent" definition is action-coupled, not merely observing.

The epistemic-opacity wording repeats the strong form from observations: "The agent does not know $T$ exactly."
This may be intended to exclude solved known-plant control from AAD's nontrivial scope, which matches README orientation.
But it creates a future compatibility question for examples or results that use known transition/measurement models as exact mathematical instantiations.
The framework can resolve this by distinguishing the analyst's known model from the agent's residual uncertainty, or by treating known-model cases as limiting cases that validate the math without being central AAD cases.

Cross-segment consistency: clean with `def-agent-environment` and `def-observation-function`; possible tension with the orientation claim that Section I spans passive Bayesian learners and Kalman filters "with or without control inputs."
That tension is not from segment text alone yet; it becomes current-src relevant only if `scope-adaptive-system` admits systems whose actions do not affect $\Omega$ or whose transition model is known.

Math verification: no substantive math beyond typing.

What this enables: action can become data-generating intervention, giving a route to Pearl Level 2 later.

Prediction for next segment: `scope-adaptive-system` should either broaden beyond action-capable agents or define the adaptive scope under the same action-coupled primitive.
I will treat this as the first real test of whether "adaptive system" and "agent" are intentionally separated.

Report outline watch item strengthened:
- Primitive AAD loop currently requires action-affecting transition and unknown $T$; check against adaptive-scope inclusions.
