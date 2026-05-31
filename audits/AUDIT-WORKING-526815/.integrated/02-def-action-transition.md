# 02 - def-action-transition

Segment: `01-aat-core/src/def-action-transition.md`
Dependencies: `def-agent-environment` - satisfied.
Status observed: `type: definition`, `status: axiomatic`, `stage: deps-verified`.

## Reflection

This segment closes the action half of the loop by making environmental change conditional on agent action through an unknown transition kernel. The key local move is "Markov by breadth": `Omega_t` is not claimed to be a small empirical state but the sufficient world-side state after absorbing enough history. That protects the transition equation from being a fragile Markov assumption, though it also makes `Omega` very large and mostly inaccessible by definition.

Two small tensions surfaced. First, the segment forward-references `def-observation-function` and `h` before the outline walk reaches it; that does not break the definition of action transition, but it does make the discussion lean on an immediately downstream sibling. Second, the sentence "If the agent knew T exactly, action selection would reduce to optimization over a known function" sounds slightly too clean because optimization also requires an objective/value functional and tractability assumptions. I am treating this as a watch item, not a finding: the segment's real claim is just transition opacity.

## Prompt pass

Predictions vs evidence: I predicted a transition relation/kernel with no objective machinery. That mostly held. The unexpected part was the explicit "Markov-of-Omega" discussion, which is helpful and likely important later.

Cross-segment consistency: consistent with the first segment's action channel. Forward reference to `def-observation-function` is local and tolerable but worth watching as a style/dependency pattern.

Math verification: not applicable beyond checking that the transition-kernel notation matches the prose. It does.

Direction next: `def-observation-function` should define the observation channel `h`, probably as a stochastic or noisy map from `Omega_t` to observations. It should make lossy access precise enough that later mismatch decomposition can separate model error from observation noise.

Errors to watch: treating "unknown T" as sufficient for purposeful planning without objective definitions; conflating unknown transition with stochastic transition; using Markov-of-Omega to hide all real structure while still wanting tractable claims later.

What I would change: soften "action selection would reduce to optimization over a known function" to "the transition-uncertainty component of action selection would disappear; objective and tractability issues may remain." This is currently editorial.

Curiosity: whether later segments ever need a smaller operational state than `Omega`; if all world history can be absorbed into `Omega`, external Markovity is formally free but practical estimation shifts entirely into observation/model sufficiency.

New knowledge enabled: the loop now has a world-update side: `a_t` is not merely emitted, it changes the distribution over future `Omega`.

Audit process change: add a watch item for forward references that function as undeclared dependencies.

Running outline change: add a possible "known T implies optimization" precision note under rescinded/candidate observations if it recurs.

Value feel: medium-high. It is straightforward, but the Markov-by-breadth move is a reusable modeling defense.

## Diagram thought

The picture should add a hidden transition kernel between two world states: the agent chooses `a_t`, but the actual map from `Omega_t` to `Omega_{t+1}` is opaque. The visual should separate the real world-side sufficient-state transition from the agent's model of it, which is intentionally missing at this point.
