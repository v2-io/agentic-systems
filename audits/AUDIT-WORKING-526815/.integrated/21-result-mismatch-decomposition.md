# 21 - result-mismatch-decomposition

Segment: `01-aat-core/src/result-mismatch-decomposition.md`
Dependencies: `def-mismatch-signal`, `def-observation-function`, `def-action-transition`, `form-agent-model`, `scope-adaptive-system` - satisfied.
Status observed: `type: result`, `status: exact`, `stage: claims-verified`.

## Reflection

This is the expected bias/noise decomposition: the residual between observed and predicted observation splits into a reducible predictive-mean error and irreducible channel noise, with the cross-term zero under a fresh-noise condition. The segment is careful on two important points: orthogonality is enough, independence is not being overclaimed; and model insufficiency does not automatically imply one-step mean error unless the lost information aligns with that mean.

The main audit note is assumption provenance. The proof uses "fresh-noise assumption (GA-1)" as the condition that kills the cross-term, and the epistemic status makes exactness conditional on that assumption. But GA-1 is not in the dependency list I have seen for this segment. This may be a repository-wide assumption rather than a segment, but from local outline discipline the exact result depends on an assumption source outside the declared `depends`.

## Prompt pass

Predictions vs evidence: I expected model error plus observation noise. The segment gives that and adds useful caveats about overfitting noise and sufficiency alignment.

Cross-segment consistency: consistent with `def-mismatch-signal` and `def-observation-function`. It also preserves the zero-aporia caveat indirectly: irreducible noise and biased observation structure affect how mismatch should be interpreted.

Math verification: the identity is correct under the stated conditional zero-mean/fresh-noise assumption and Euclidean or trace-covariance interpretation for vector observations. The strict positivity condition is appropriately conditional: non-degenerate noise or misspecified predictive mean suffices.

Direction next: `emp-update-gain` should use this split to justify weighting observations by model uncertainty versus observation uncertainty without treating noise as learnable signal.

Errors to watch: exact claims silently depending on GA assumptions; later persistence claims treating residual uncertainty in `Omega` as sufficient for observation mismatch even when the observation function is insensitive to uncertain state components.

What I would change: add GA-1 or the relevant assumptions artifact to `depends`, or mark the assumption inline in the frontmatter/status.

Curiosity: this segment is one of the first places where the theory is explicit about alignment assumptions. That caveat discipline is worth preserving downstream.

New knowledge enabled: mismatch persistence in AAT is not "the model is always wrong"; it can be irreducible observation noise.

Audit process change: the diagram should be a vector decomposition with an orthogonality marker rather than a pipeline.

Value feel: high. It is compact, standard, and guarded against a common overinterpretation.

## Diagram thought

The clearest diagram is a Pythagorean split. Prediction `hat{o}` and true conditional mean `bar{o}` form the reducible leg; `bar{o}` to observation `o` forms the irreducible noise leg; their expected cross term is zero under GA-1. This visual should make overfitting leg two look like the wrong move.
