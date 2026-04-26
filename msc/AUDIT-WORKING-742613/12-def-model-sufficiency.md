# 12 — def-model-sufficiency

Dependencies checked: `form-agent-model` and `form-information-bottleneck` already read.

## Reflection

The predicted ratio appears:

$$S(M_t)=1-\frac{I(\mathcal C_t;o_{t+1:\infty}\mid M_t,a_{t:\infty})}{I(\mathcal C_t;o_{t+1:\infty}\mid a_{t:\infty})}.$$

Given $M_t=\phi(\mathcal C_t)$, the chain-rule reading is sound: retained predictive information plus residual predictive information beyond $M_t$ decomposes the full history's predictive information.

Math edge case:
The denominator can be zero when the full chronica contains no predictive information about future observations under the conditioned action sequence.
Then $S$ is undefined, not 0 or 1.
This matters for degenerate environments, saturated observation noise, or iid observations.
The README has a "true but uninteresting" corner for saturated noise; this segment should probably name the denominator-positive condition or define a convention for zero denominator.

Candidate finding E (low/medium unless downstream relies on boundary values universally):
`def-model-sufficiency` states boundary values for $S$ without a caveat that $I(\mathcal C_t;o_{t+1:\infty}\mid a_{t:\infty})>0$.
Repair is simple: add a well-definedness condition and convention for the no-predictive-information case.

Status: definitional/axiomatic is appropriate if the well-definedness caveat is added.

Substantive nuance:
The Discussion says predictive sufficiency is not causal sufficiency, which is important.
The claim that $S(M_t)=1$ is "nearly sufficient" for causal validity for deterministic-action agents still needs care.
If hidden variables influence outcomes and are not represented in $M_t$, $S=1$ relative to observed future may not satisfy interventional adjustment.
The segment does name the remaining no-unmodeled-common-cause condition, so this is probably adequate.

What this enables:
Model quality can now be separated from model-class quality and from current mismatch.
This is useful: an agent can retain all available predictive information and still be wrong because the observation channel is biased or the model class is inadequate.

Prediction for next segment:
`def-model-class-fitness` should define the best achievable $S$ over $\mathcal M$.
I will watch whether it inherits the denominator-zero issue and whether it distinguishes model class limitations from data limitations.

Running report update:
- Candidate low/medium finding: missing denominator-positive condition for model sufficiency.
