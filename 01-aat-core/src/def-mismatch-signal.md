---
slug: def-mismatch-signal
type: definition
status: axiomatic
depends:
  - form-agent-model
  - def-observation-function
  - def-action-transition
stage: deps-verified
---

# Definition: Mismatch Signal

Names the signal that drives every adaptive update — the formal expression of *aporia* (productive perplexity). The **mismatch signal** is $\delta_t = o_t - \hat{o}_t$, the difference between the actual observation and the model's prediction conditioned on the prior state and prior action. A more general version for probabilistic models is the **score-function mismatch** $\tilde\delta_t = \nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$, which points in the direction the model should move to increase the likelihood of what actually occurred. The prediction-error form lives in observation space $\mathcal{O}$; the score-function form lives in the tangent space $T_M\mathcal{M}$. Under Gaussian models the two coincide up to scaling.

This is *definitional* rather than substantive: given any model that predicts (see #form-agent-model) and any observation that arrives (see #def-observation-function), their difference exists. The mismatch signal is not an additional assumption but a consequence of having a predictive model in an uncertain world.

A genuinely important conceptual point is surfaced in Discussion: **zero mismatch does not necessarily indicate model adequacy**. A near-zero $\delta_t$ can mean (a) the model genuinely reflects reality — desirable; (b) the agent is only observing aspects its model already explains while remaining ignorant of aspects where the model is wrong — confirmation bias; or (c) the observation channel is too noisy to detect model errors — an architectural limitation. Only (a) is desirable. An agent without aporia has stopped adapting — but silence can mean peace, or it can mean deafness. This ambiguity is what motivates active testing later in the framework: deliberately choosing actions that generate informative mismatch, the basis of #def-causal-information-yield.

A scaling note is preserved for the dynamics that come later: when $\delta_t$ is in physical units, its magnitude entering the mismatch dynamics should be understood as a Mahalanobis distance $\Vert\delta_t\Vert_\Sigma$ against the observation noise covariance — mapping physical prediction error to dimensionless surprise-equivalent units.

## Formal Expression

*[Definition (mismatch-signal)]*

Given model $M_{t-1}$ and prior action $a_{t-1}$, the model generates a prediction:

$$\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$$

The **mismatch signal** (prediction error):

$$\delta_t = o_t - \hat{o}_t$$

This is the primary definition, used in the mismatch dynamics ( #result-persistence-condition, #result-sector-condition-stability) and in the decomposition ( #result-mismatch-decomposition).

For models with probabilistic predictions, the mismatch generalizes to the **score-function mismatch**:

*[Definition (score-mismatch)]*

$$\tilde{\delta}_t = \nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$$

which points in the direction the model should move to increase the likelihood of the actual observation. $\tilde{\delta}_t$ lives in the tangent space $T_M\mathcal{M}$, while $\delta_t$ lives in observation space $\mathcal{O}$. Under Gaussian models, they coincide up to scaling.

## Epistemic Status

This is *definitional*. Given any model that predicts ( #form-agent-model) and any observation that arrives ( #def-observation-function), their difference exists. The mismatch signal is not an additional assumption but a consequence of having a predictive model in an uncertain world. The score-function form is the natural generalization when $\mathcal{O}$ is not a vector space or when the model's predictive distribution is the natural object.

## Discussion

**Units and normalization.** When $\delta_t$ is in physical units (meters, dollars), the $\Vert\delta\Vert$ that enters the mismatch dynamics should be understood as the Mahalanobis distance: $\Vert\delta_t\Vert_\Sigma = \sqrt{\delta_t^T \Sigma^{-1} \delta_t}$ where $\Sigma$ is the observation noise covariance. This maps physical prediction error to dimensionless surprise-equivalent units.

**The zero-aporia ambiguity.** $\delta_t \approx 0$ does NOT necessarily indicate model adequacy. It may mean: (a) the model genuinely reflects reality — *desirable*; (b) the agent is only observing aspects its model already explains, while remaining ignorant of aspects where the model is wrong — *confirmation bias*; or (c) the observation channel is too noisy to detect model errors — *architectural limitation*. Only (a) is desirable. An agent without aporia is an agent that has stopped adapting — but silence can mean peace or deafness. This ambiguity is why active testing — choosing actions to generate informative aporia — can be valuable (see #def-causal-information-yield for the CIY framework).

**The mismatch transform.** The update rule ( #emp-update-gain) writes $M_t = M_{t-1} + \eta \cdot g(\delta_t)$, where the transform $g$ maps from $\delta_t$'s space to the model's update space: $g: \mathcal{O} \to T_M\mathcal{M}$ for prediction errors; $g: T_M\mathcal{M} \to T_M\mathcal{M}$ for score-function mismatches.
