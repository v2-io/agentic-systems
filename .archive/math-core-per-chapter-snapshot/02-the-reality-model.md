# The Reality Model


## Formulation: The Reality Model

- **Slug**: `form-agent-model`
- **Type**: formulation
- **Status**: robust-qualitative
- **Stage**: deps-verified
- **Depends**: `def-agent-environment`, `def-observation-function`, `def-chronica`

The agent's compressed representation of how the world works, mapping interaction history to model space. $M_t$ is the substrate of prolepsis — the model from which predictions are generated and against which observations are compared. This is a formulation choice — we commit to analyzing the agent as having a complete state $M_t$ that subsumes all retained information from its history.

*[Formulation (agent-model)]*

$$M_t = \phi(\mathcal{C}_t)$$

where:
- $\phi: \mathcal{C}^\ast \to \mathcal{M}$ maps interaction history to model space $\mathcal{M}$
- $\mathcal C_t = (o_1, a_1, \ldots, o_t)$ is the chronica ( #def-chronica) — the complete record of agent-environment interaction
- $\mathcal{M}$ is the space of possible models the agent can hold

The mapping $\phi$ is a many-to-one compression: multiple distinct histories may produce the same model state. This is not a deficiency — it is the essential function of the model: retaining what matters and discarding what does not.

---



## Formulation: Information Bottleneck

- **Slug**: `form-information-bottleneck`
- **Type**: formulation
- **Status**: exact
- **Stage**: draft
- **Depends**: `form-agent-model`, `def-action-transition`

Optimal model compression balances retained history against predictive power; the information bottleneck objective provides a principled framework for understanding this trade-off.

*[Formulation (IB-objective)]*

$$\phi^* = \arg\min_{\phi} \left[ I(M_t;\, \mathcal{C}_t) - \beta \cdot I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty}) \right]$$

where:
- $I(M_t;\, \mathcal{C}_t)$ is the compression cost — how much of the interaction history the model retains
- $I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty})$ is the predictive power — how much the model tells the agent about future observations given future actions
- $\beta \gt 0$ is the trade-off parameter controlling the compression-prediction balance

**Dependence on volatility (The $\beta$ vs $\rho$ distinction).** It is tempting to claim that the trade-off parameter $\beta$ must be actively lowered by the agent in highly volatile environments (high $\rho$) to favor aggressive compression. However, this is a double-counting error. The environment's volatility already natively degrades the mutual information $I(\mathcal{C}_t; o_{t+1:\infty})$ — old history mathematically loses its predictive power as $\rho$ increases. The optimal $\phi^\ast$ will automatically discard this useless old information even if the agent's preference parameter $\beta$ remains completely constant. 

Therefore, adjusting $\beta$ reflects changes in the agent's *internal cost of memory* or *computational capacity*, not changes in environmental volatility. The agent adapts its *actions* in response to $\rho$ (by increasing exploration to survive, see `#deriv-causal-ib-exploration`), but the optimal IB representation adapts to $\rho$ natively through the joint probability distribution.

---



## Definition: Model Sufficiency

- **Slug**: `def-model-sufficiency`
- **Type**: definition
- **Status**: axiomatic
- **Stage**: deps-verified
- **Depends**: `form-agent-model`, `form-information-bottleneck`, `def-action-transition`

The fraction of predictive information the model retains relative to the full interaction history; $S = 1$ means the model is a sufficient statistic for prediction, $S \lt 1$ means predictive information has been lost.

*[Definition (model-sufficiency)]*

$$S(M_t) = 1 - \frac{I(\mathcal{C}_t;\, o_{t+1:\infty} \mid M_t,\, a_{t:\infty})}{I(\mathcal{C}_t;\, o_{t+1:\infty} \mid a_{t:\infty})}$$

where:
- The numerator $I(\mathcal C_t;\, o_{t+1:\infty} \mid M_t,\, a_{t:\infty})$ is the predictive information that the full history $\mathcal C_t$ carries about the future *beyond* what $M_t$ already captures — the information lost by compression
- The denominator $I(\mathcal C_t;\, o_{t+1:\infty} \mid a_{t:\infty})$ is the total predictive information in the full history

**Well-definedness.** $S(M_t)$ is defined when $I(\mathcal{C}_t;\, o_{t+1:\infty} \mid a_{t:\infty}) \gt 0$ — when the chronica carries some predictive information about future observations beyond what the action sequence alone supplies. When the denominator vanishes (saturated-noise environments, prediction-vacuous regimes, fully iid observations independent of history), $S(M_t)$ is undefined: predictive sufficiency is a property *of a prediction task*, and there is no prediction task to be sufficient for. Downstream constructs that build on $S$ — #def-model-class-fitness and #result-structural-adaptation-necessity — inherit the same scope and are correspondingly inapplicable in predictively-vacuous regimes.

**Boundary values** (assuming the well-definedness clause holds):
- $S(M_t) = 1$: $M_t$ is a sufficient statistic — it captures all predictive information in $\mathcal C_t$. Knowing the full history beyond $M_t$ adds nothing.
- $S(M_t) = 0$: $M_t$ retains no predictive information. The model is useless for prediction.
- $0 \lt S(M_t) \lt 1$: partial sufficiency — some predictive information is retained, some lost.

---



## Definition: Model Class Fitness

- **Slug**: `def-model-class-fitness`
- **Type**: definition
- **Status**: axiomatic
- **Stage**: deps-verified
- **Depends**: `def-model-sufficiency`

The best achievable sufficiency within a model class. When no model in the class can adequately represent reality, the agent faces a structural limitation that no amount of parameter tuning can resolve.

*[Definition (model-class-fitness)]*

$$\mathcal{F}(\mathcal{M}) = \sup_{M \in \mathcal{M}} S(M)$$

where $\mathcal{M}$ is the model class — the set of all models the agent can represent given its current architecture, parameterization, or capacity.

**Structural inadequacy condition:**

$$\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$$

When this holds, no model $M \in \mathcal{M}$ achieves sufficiency above $1 - \varepsilon$. The gap is structural: it cannot be closed by better parameter estimation, more data, or longer training within the current class. This is the trigger for structural change ( #result-structural-adaptation-necessity).

---
