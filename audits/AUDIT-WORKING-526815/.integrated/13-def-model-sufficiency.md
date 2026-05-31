# 13 - def-model-sufficiency

Segment: `01-aat-core/src/def-model-sufficiency.md`
Dependencies: `form-agent-model`, `form-information-bottleneck`, `def-action-transition` - satisfied.
Status observed: `type: definition`, `status: axiomatic`, `stage: deps-verified`.

## Reflection

This definition is strong. `S(M_t)` is not generic model quality; it is the fraction of full-history predictive information retained by the compressed model, conditional on future actions. The well-definedness clause is important and well-placed: if the history has no predictive information about future observations, sufficiency is undefined rather than vacuously perfect.

The discussion is also careful in the right ways. It distinguishes sufficiency from truth, predictive Level-1 adequacy from causal Level-2 validity, and trajectory-relative sufficiency from state-class claims. My main update is that F3 matters because this ratio can support either deterministic `M_t = phi(C_t)` or stochastic IB-style encoders, but the surrounding notation has not yet made that choice explicit. The definition itself is not the problem.

## Prompt pass

Predictions vs evidence: I expected a retained-predictive-information ratio. The actual formula is better than a naive `I(M;Y)/I(C;Y)` because it measures residual predictive information in the full history beyond `M`.

Cross-segment consistency: consistent with `form-agent-model` and `form-information-bottleneck`. It inherits policy-relativity from the IB segment and explicitly names it. No new contradiction.

Math verification: checked the shape mentally. If `M` is a function or Markov-kernel compression of `C`, then the residual conditional mutual information is bounded by the denominator under the appropriate Markov condition, giving the intended range. I did not run numerical examples.

Direction next: `def-model-class-fitness` should take a supremum over model class. I will watch whether the class ranges over states, mappings, architectures, or parameterized families, because the distinction matters for structural adaptation.

Errors to watch: downstream use of `S=1` as truth or causal validity; denominator-zero regimes being ignored; policy/trajectory relativity disappearing from later summaries.

What I would change: no immediate change. If F3 is fixed by making `phi` a kernel, this segment may need one phrase saying `M_t` may be a realized draw/state from the encoder.

Curiosity: whether "future observations given future actions" is too observation-centered for agents whose objective depends on latent environment states that are never observed. The segment is honest that it is predictive, not causal/truth.

New knowledge enabled: there is now a measurable compression defect: the predictive information that the full chronica still has after conditioning on the model.

Audit process change: when later segments say "model is sufficient," check whether they mean predictive, causal, truth-tracking, or task-sufficient.

Running outline change: add sufficiency/truth/causality distinction to watch list.

Value feel: high. This is a precise enough definition to prevent several common overclaims if downstream segments preserve its caveats.

## Diagram thought

The clearest diagram is an information bar: full chronica predictive information is a denominator; the model captures one portion and the residual `I(C;Y|M,A)` is the lost portion. Sufficiency is one minus the residual fraction.
