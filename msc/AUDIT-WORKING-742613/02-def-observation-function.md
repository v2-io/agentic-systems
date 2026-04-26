# 02 — def-observation-function

Dependencies checked: `def-agent-environment` already read.

## Reflection

This segment formalizes observations as $o_t=h(\Omega_t,a_{t-1},\varepsilon_t)$ and makes action-dependent observation possible.
The prediction was correct: active sensing is built in immediately.

Status looks mostly appropriate as definitional, but one phrase may be scope-narrowing in a way the rest of the framework might not intend: "The agent knows neither $h$ nor the distribution of $\varepsilon_t$ exactly."
If taken literally as constitutive, this excludes common control / filtering cases where the observation operator or noise model is specified well enough for exact Kalman analysis.
The framework may intend "the agent lacks direct access to $\Omega_t$ and may have model uncertainty over $h$ or noise"; this segment says something stronger.

This is not yet a finding because later segments may relax it or treat known-$h$ cases as idealized instantiations inside the broader lossy-observation boundary.
I will watch especially `example-kalman`, `result-mismatch-decomposition`, and `emp-update-gain`.

Cross-segment consistency so far: no contradiction with `def-agent-environment`; this segment depends on the primitive information-loss boundary cleanly.
It also references a missing TST segment in Discussion; since this is explanatory and not formal dependency, I am not treating it as a dependency problem.

What this enables: prediction error can be defined against observations whose distribution depends on prior actions, so causal/interventional structure can later emerge from the loop rather than being bolted on.

Prediction for next segment: `def-action-transition` should specify $\Omega_{t+1}\sim T(\cdot\mid\Omega_t,a_t)$.
I will watch whether action effect is mandatory or optional, because that will clarify the passive-adaptive-system concern from segment 01.

Running report watch items:
- Possible over-strong epistemic opacity: unknown $h$ and unknown noise distribution may conflict with known-observation-model examples.
- Adaptive-system breadth vs primitive action-effect requirement remains open.
