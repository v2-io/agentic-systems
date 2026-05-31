# 35 - def-agent-spectrum

Segment: `01-aat-core/src/def-agent-spectrum.md`
Dependencies: `def-agent-environment`, `form-agent-model` - satisfied.
Status observed: `type: definition`, `status: axiomatic`, `stage: deps-verified`.

## Reflection

The spectrum is a useful Part II entry point. It separates model richness from objective richness and shows that Section II adds objectives/strategy without invalidating Part I's adaptive tracker machinery. The "continuum, not categories" caveat is important because low-end systems such as thermostats and PID controllers sit near boundaries rather than in clean bins.

This segment strongly reinforces the earlier F1 scope issue. It explicitly says passive trackers and passive Bayesian learners with no action choices are fully inside Section I's adaptive scope, while `def-agent-environment` originally defined an agent as producing actions that affect `Omega`. The fix still looks localized: broaden the base adaptive-system definition or reserve "agent" in that early definition for the narrower agency scope.

## Prompt pass

Predictions vs evidence: I expected the Part II lift to distinguish adaptive trackers from actuated agents. The 2x2 spectrum does that clearly.

Cross-segment consistency: consistent with `scope-adaptive-system` and `scope-agency`; inconsistent with the action-requiring phrasing of `def-agent-environment`.

Math verification: no math here. This is taxonomy/scope.

Direction next: `form-complete-agent-state` should formalize the lifted state `X_t=(M_t,G_t)` and clarify how objectives and strategy relate to `M_t`.

Errors to watch: treating quadrants as discrete ontological categories despite the continuum caveat; importing continuity stance into actuation rather than keeping it orthogonal.

What I would change: add a note near `def-agent-environment` or here saying "adaptive system" is broader than "agency" and may lack action channels.

Curiosity: the Hafez comparison may be useful, but I have not verified the 2026 reference or bridge simulations.

New knowledge enabled: Part II's formal term is "actuated agent"; continuity stance is orthogonal to actuation.

Audit process change: the diagram can simply be the 2x2 spectrum with a highlighted Section I/II boundary.

Value feel: high as taxonomy; it also confirms a live base-definition issue.

## Diagram thought

The obvious diagram is the 2x2 plane with model richness vertical and objective richness horizontal. Section I occupies the model-structured/no-objective region; Part II adds the model-structured/objective-structured region. The lower-left and upper-left edge cases should remain visibly continuous, not boxed as hard species.
