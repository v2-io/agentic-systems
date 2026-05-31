# 17 - form-event-driven-dynamics

Segment: `01-aat-core/src/form-event-driven-dynamics.md`
Dependencies: `post-causal-structure`, `def-observation-function`, `def-action-transition`, `form-agent-model` - satisfied.
Status observed: `type: formulation`, `status: robust-qualitative`, `stage: deps-verified`.

## Reflection

This segment does the needed bridge from ordinal chronica/update notation to wall-clock heterogeneous interaction. The move from synchronized ticks to typed events is coherent and useful: observations and action completions can arrive on different channels, with different rates, and the discrete-time update becomes a special case instead of the default ontology.

The sharpest issue is in "event information content." The displayed formula, `I(e_tau; Omega_tau | M_{tau^-})`, is mutual information: an expected dependence between a random event variable and environment state, conditioned on the pre-event model. The prose then treats it as realized event surprise: an event already predicted carries little information, a surprising event carries much. That is usually pointwise information, Bayesian information gain, or surprisal, not mutual information. This may be fixable by saying the formula is expected information content for an event channel/type, while realized event content is `D_KL(p(Omega | M, e) || p(Omega | M))` or pointwise mutual information.

## Prompt pass

Predictions vs evidence: I expected event times, pre/post update notation, multi-rate channels, and a bridge to tempo. The segment delivered all of these, though it defines the event stream more than the actual update function.

Cross-segment consistency: it respects `def-chronica` by keeping events temporally ordered while adding metric timestamps `tau`. It also fits `post-causal-structure` by separating observation arrivals from action completions. The notation uses nondecreasing time, so simultaneous events are allowed, but no tie-breaking or batching convention is given yet.

Math verification: the effective tempo equation is plausible as a first additive channel model, but it imports `eta^{(k)*}` and `def-adaptive-tempo` before those definitions are read. The event-information formula is the main math concern: mutual information is an average channel quantity, not an observed event's realized surprise.

Direction next: later mismatch and gain segments should clarify whether `I(e_tau)` is expected informativeness, prediction error magnitude, posterior information gain, or some blend.

Errors to watch: treating raw event rate as adaptive capacity without cost/correlation/saturation; assuming channel contributions add independently; using event-level MI language where realized surprisal is intended.

What I would change: rename the displayed quantity to expected event-channel information, or replace the event-specific definition with Bayesian information gain for a realized event.

Curiosity: the action-completion event is a good modeling choice because it prevents actions from being treated as instantaneous. I want to see whether later update equations preserve pending actions/in-flight latency.

New knowledge enabled: adaptive tempo is starting to look like "quality-adjusted information arrival rate," not merely reaction speed.

Audit process change: the diagram survey pushed me away from a generic timeline and toward a merger diagram: channels enter a rate/value bottleneck, then become tempo.

Value feel: high. This segment makes the chapter's wall-clock bridge explicit, and it reveals a concrete information-theory wording issue.

## Diagram thought

The structure is multi-source asynchronous flow into a scalar capacity measure. The best compact visual is a set of colored channel lanes feeding an event stream, then a bottleneck where rate `nu` and information/gain `eta` multiply before summing into tempo. The diagram should make the distinction between "realized event" and "expected channel contribution" visible, because that is where the segment's main ambiguity lives.
