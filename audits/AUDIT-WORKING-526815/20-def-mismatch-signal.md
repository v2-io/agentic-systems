# 20 - def-mismatch-signal

Segment: `01-aat-core/src/def-mismatch-signal.md`
Dependencies: `form-agent-model`, `def-observation-function`, `def-action-transition` - satisfied.
Status observed: `type: definition`, `status: axiomatic`, `stage: deps-verified`; prose epistemic status says definitional.

## Reflection

The definition is straightforward and useful: prediction from the current model/action, observed datum, residual mismatch, and a score-function generalization when raw observation subtraction is not the natural object. The "zero-aporia ambiguity" is especially strong because it prevents small error from being misread as model adequacy; silence can come from fit, biased sampling, or noisy channels.

Two precision issues are worth carrying forward. First, the metadata says `status: axiomatic`, while the epistemic status says the mismatch is definitional. That is not a mathematical problem, but it weakens the status taxonomy. Second, "under Gaussian models, they coincide up to scaling" is only generally true when the differentiated model coordinate corresponds to the predictive mean, or after the appropriate Jacobian/metric mapping. A Gaussian likelihood score with respect to arbitrary model parameters is `J^T Sigma^{-1}(o-mu)`, not just the residual scaled.

## Prompt pass

Predictions vs evidence: I expected a residual definition and maybe a normalized/error-space version. The segment provides raw residual, score mismatch, Mahalanobis normalization, and the active-testing motivation.

Cross-segment consistency: consistent with `form-agent-model` and `def-observation-function`. It reverts to discrete `t` notation after event-driven `tau`, but that is acceptable as the special synchronized case unless later formulas mix the two without a bridge.

Math verification: residual mismatch is standard. Score mismatch is standard as a gradient of log likelihood. The tangent-space statement is good, but the Gaussian coincidence should be qualified by parameterization and metric.

Direction next: `result-mismatch-decomposition` should separate true model error from observation noise, and ideally preserve the zero-aporia ambiguity rather than collapsing all residuals into model failure.

Errors to watch: treating low mismatch as truth; treating score mismatch as interchangeable with observation residual without a transform; using future stability/persistence results before their definitions.

What I would change: set status to `definitional` or make the epistemic wording match `axiomatic`; qualify the Gaussian sentence with "for Gaussian observations parameterized by predictive mean."

Curiosity: the transform `g` is doing important type-conversion work. It may deserve more prominence because it is the bridge from observation error to model update.

New knowledge enabled: mismatch has two spaces in play: observation space and model tangent space. Many later claims will need to preserve that distinction.

Audit process change: the diagram should foreground type conversion: residual lives in observation space, score/update direction lives in tangent space, and zero residual has three interpretations.

Value feel: high. This is a crisp definition with a real caveat built in.

## Diagram thought

The right visual is a two-space map. Prediction and observation meet in observation space to form `delta`; `g` or the score transform maps that into the model tangent space. A side branch from `delta approx 0` should split into adequate model, biased sampling, and noisy channel, because that is the conceptual guardrail the segment contributes.
