# 04 — scope-adaptive-system

Dependencies checked: declared dependencies `def-agent-environment` and `def-observation-function` already read.

## Reflection

This segment immediately tests the prediction from segments 01-03.
It explicitly broadens AAD's outer scope to passive Bayesian learners and Kalman filters "with or without control inputs", and says action narrows later to agency.
That is conceptually right for the framework, but it conflicts with the primitive `def-agent-environment` definition if "Agent" there is literal: that segment required actions that affect $\Omega$.

The segment also uses $\mathcal C_t$ in its formal scope condition:

$$H(\Omega_t \mid \mathcal C_t) \gt 0$$

But `def-chronica`, which defines $\mathcal C_t$, appears later in the OUTLINE and is not declared in `depends:`.
This is more than a reading discomfort: the formal expression is not well-typed from declared priors alone.
Because the dependency is not declared, the explicit downstream-dependency check did not fire before reading, but Gate 1's missing-dependency rule would catch it.

Candidate finding A:
`scope-adaptive-system` uses undefined $\mathcal C_t$ and should either depend on an upstream chronica definition or avoid $\mathcal C_t$ until after `def-chronica`.
This looks like an OUTLINE/order problem or missing-dependency problem.

Candidate finding B:
`scope-adaptive-system` formally defines $\mathcal S_\text{adaptive}$ over `(Agent, Ω)` while its prose includes passive observers and nominal agents outside action-causal agency.
If `Agent` inherits `def-agent-environment`'s action-affecting condition, passive observers do not fit.
Potential repair: introduce a more neutral "system/environment" primitive for Section I or weaken `def-agent-environment` so action channel can be absent / degenerate until `scope-agency`.

Math/status: `status: axiomatic` is fine for scope-setting.
The strong claim "This is sufficient for ... all of Section I's adaptive dynamics" is forward-looking and may be overbroad if later Section I claims require action, model update, or gain assumptions beyond observation + uncertainty.
I will revisit after reading those segments.

What this enables: a clean adaptation-before-agency hierarchy.
This is one of the framework's important structural moves; fixing the primitive terminology would make it stronger.

Prediction for next segment: `scope-agency` should add `|\mathcal A|\ge 2` and an interventional contrast condition.
I will check whether it depends on `def-action-transition` and whether it resolves the passive/nominal distinction cleanly.

Running report update:
- Candidate finding: hidden downstream dependency on `def-chronica`.
- Candidate finding: adaptive-scope formal object uses action-capable `Agent` while admitting passive observers.
