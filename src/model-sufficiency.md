---
slug: model-sufficiency
type: definition
status: exact
depends:
  - agent-model
  - information-bottleneck
---

# Definition: Model Sufficiency

The fraction of predictive information the model retains relative to the full interaction history; $S = 1$ means the model is a sufficient statistic for prediction, $S \lt 1$ means predictive information has been lost.

## Formal Expression

*[Definition (model-sufficiency)]*

$$S(M_t) = 1 - \frac{I(\mathcal{C}_t;\, o_{t+1:\infty} \mid M_t,\, a_{t:\infty})}{I(\mathcal{C}_t;\, o_{t+1:\infty} \mid a_{t:\infty})}$$

where:
- The numerator $I(\mathcal C_t;\, o_{t+1:\infty} \mid M_t,\, a_{t:\infty})$ is the predictive information that the full history $\mathcal C_t$ carries about the future *beyond* what $M_t$ already captures — the information lost by compression
- The denominator $I(\mathcal C_t;\, o_{t+1:\infty} \mid a_{t:\infty})$ is the total predictive information in the full history

**Boundary values:**
- $S(M_t) = 1$: $M_t$ is a sufficient statistic — it captures all predictive information in $\mathcal C_t$. Knowing the full history beyond $M_t$ adds nothing.
- $S(M_t) = 0$: $M_t$ retains no predictive information. The model is useless for prediction.
- $0 \lt S(M_t) \lt 1$: partial sufficiency — some predictive information is retained, some lost.

## Epistemic Status

This is *definitional* — it names and formalizes a quantity. The definition is well-grounded in information theory (conditional mutual information ratios are standard). No substantive claim is made here about what value $S(M_t)$ takes or what happens when it is low; those claims belong to #model-class-fitness and #structural-adaptation-necessity.

## Discussion

**Sufficiency is relative to the prediction task.** $S(M_t)$ measures sufficiency for predicting future observations given future actions. A model that is sufficient for one prediction horizon may be insufficient for another. The infinite-horizon formulation ($o_{t+1:\infty}$) is the most demanding; practical sufficiency over finite horizons may be easier to achieve.

**Sufficiency vs. accuracy.** A model can be sufficient ($S = 1$) while being wrong in absolute terms — if the full history is also wrong (e.g., systematically biased observations). Sufficiency measures information retention, not truth. The mismatch signal ( #mismatch-signal) measures accuracy; sufficiency measures completeness of compression.
