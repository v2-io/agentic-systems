# 03 - def-observation-function

Segment: `01-aat-core/src/def-observation-function.md`
Dependencies: `def-agent-environment`, `def-action-transition` - satisfied.
Status observed: `type: definition`, `status: axiomatic`, `stage: deps-verified`.

## Reflection

This segment completes the minimal loop: the world has a transition kernel affected by action, and the agent receives observations through a lossy channel that can itself depend on the prior action. The action-dependence is a useful detail because it opens active perception without needing purpose yet; an adaptive system can choose where to look before it has a rich objective theory.

The surprising strengthening is epistemic opacity of the observation mechanism itself: the agent knows neither `h` nor the noise distribution exactly. Partial observability alone does not require unknown observation laws; a Kalman filter often assumes known observation matrix/noise covariance while still maintaining a belief/model because `Omega_t` is not directly observed. This may be intentional if AAT is specifically about adaptive learning under model uncertainty, but it may be too narrow if AAT later wants to include known-sensor partial-observation control as an exact instantiation. I am not calling this a finding yet because later scope segments may split "adaptive" from "pre-compiled controller" more carefully.

## Prompt pass

Predictions vs evidence: I expected a lossy/noisy map from environment to observation. I did not predict the strong "unknown h and unknown noise distribution" constitutive clause.

Cross-segment consistency: consistent with `def-agent-environment`'s information-loss boundary and with `def-action-transition`'s transition opacity. It introduces a cross-component reference to TST (`obs-software-epistemic-properties`) that I will not follow under the modified prompt.

Math verification: no computation. Formal notation is clear, though "lossy" is asserted in prose rather than formalized as non-injectivity, entropy reduction, or information loss conditional on action/noise.

Direction next: `def-chronica` should define complete interaction history, likely including observations, actions, and maybe internal states. I expect it to become the raw material for `M_t` compression.

Errors to watch: overnarrowing AAT scope by requiring unknown `h`/noise rather than merely inaccessible `Omega`; later examples using known observation models without reconciling this definition; treating lossy/noisy as interchangeable when they have different formal meanings.

What I would change: distinguish "lossy mediated observation is constitutive" from "unknown observation mechanism is the learning/adaptation sub-scope." That split may already be downstream, so hold the candidate.

Curiosity: whether the Kalman worked example later assumes known `H`, `R`, or learns them. If it assumes known observation covariance, this segment's constitutive opacity language will need nuance.

New knowledge enabled: active perception is now in scope because observations can depend on prior action. That will matter for causal information yield and exploration.

Audit process change: create a specific watch item: known-model POMDP/Kalman compatibility with `transition opacity` and `epistemic opacity`.

Running outline change: add possible "opacity too strong" candidate.

Value feel: high. A lot of downstream scope hangs on exactly how strong this opacity condition is.

## Diagram thought

The picture needs to show observation as a many-to-one/noisy aperture from `Omega_t` to `o_t`, with the previous action steering the aperture. The important mental model is not a camera simply pointed at the world, but an action-conditioned sensor whose mapping is itself uncertain to the agent.
