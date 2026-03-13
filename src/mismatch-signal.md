---
slug: mismatch-signal
type: definition
status: axiomatic
depends:
  - agent-model
  - observation-function
---

# Definition: Mismatch Signal

The discrepancy between the model's prediction and the actual observation — the fundamental error signal that drives all adaptation.

## Formal Expression

*[Definition (mismatch-signal)]*

Given model $M_{t-1}$ and prior action $a_{t-1}$, the model generates a prediction:

$$\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$$

The **mismatch signal** (prediction error):

$$\delta_t = o_t - \hat{o}_t$$

This is the primary definition, used in the mismatch dynamics ( #persistence-condition, #sector-condition-stability) and in the decomposition ( #mismatch-decomposition).

For models with probabilistic predictions, the mismatch generalizes to the **score-function mismatch**:

*[Definition (score-mismatch)]*

$$\tilde{\delta}_t = -\nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$$

which points in the direction the model should move to increase the likelihood of the actual observation. $\tilde{\delta}_t$ lives in the tangent space $T_M\mathcal{M}$, while $\delta_t$ lives in observation space $\mathcal{O}$. Under Gaussian models, they coincide up to scaling.

## Epistemic Status

This is *definitional*. Given any model that predicts ( #agent-model) and any observation that arrives ( #observation-function), their difference exists. The mismatch signal is not an additional assumption but a consequence of having a predictive model in an uncertain world. The score-function form is the natural generalization when $\mathcal{O}$ is not a vector space or when the model's predictive distribution is the natural object.

## Discussion

**Units and normalization.** When $\delta_t$ is in physical units (meters, dollars), the $\Vert\delta\Vert$ that enters the mismatch dynamics should be understood as the Mahalanobis distance: $\Vert\delta_t\Vert_\Sigma = \sqrt{\delta_t^T \Sigma^{-1} \delta_t}$ where $\Sigma$ is the observation noise covariance. This maps physical prediction error to dimensionless surprise-equivalent units.

**The zero-mismatch ambiguity.** $\delta_t \approx 0$ does NOT necessarily indicate model adequacy. It may mean: (a) the model genuinely reflects reality — *desirable*; (b) the agent is only observing aspects its model already explains, while remaining ignorant of aspects where the model is wrong — *confirmation bias*; or (c) the observation channel is too noisy to detect model errors — *architectural limitation*. Only (a) is desirable. This ambiguity is why active testing — choosing actions to generate informative mismatch signals — can be valuable (see #causal-information-yield for the CIY framework).

**The mismatch transform.** TF-06's update rule writes $M_t = M_{t-1} + \eta \cdot g(\delta_t)$, where the transform $g$ maps from $\delta_t$'s space to the model's update space: $g: \mathcal{O} \to T_M\mathcal{M}$ for prediction errors; $g: T_M\mathcal{M} \to T_M\mathcal{M}$ for score-function mismatches.
