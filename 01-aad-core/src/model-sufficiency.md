---
slug: model-sufficiency
type: definition
status: axiomatic
depends:
  - agent-model
  - information-bottleneck
stage: deps-verified
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

**Sufficiency is predictive, not causal.** $S(M_t)$ measures retained *predictive* information — a Level 1 (associational) property. It does not by itself guarantee that $M_t$ supports Level 2 (interventional) queries such as $P(o \mid do(a), M_t)$. The causal validity of value computations conditioned on $M_t$ requires an additional condition: that $M_t$ satisfies the backdoor criterion with respect to the agent's actions (see #value-object). For agents whose actions are deterministic functions of $M_t$ (standard in ACT: $a_t = \pi(M_t, G_t)$), $S(M_t) = 1$ is nearly sufficient for causal validity — the remaining requirement is that no unmodeled external factor influences both action selection and outcomes. But predictive sufficiency alone does not collapse the distinction between Level 1 and Level 2 that #causal-hierarchy-requirement establishes.

**Policy-relativity.** The conditioning on $a_{t:\infty}$ makes $S(M_t)$ implicitly policy-relative: different policies generate different future action sequences, which changes which future observations are relevant and therefore what "predictive information" means. A model that is sufficient under a conservative policy may be insufficient under an aggressive one (the aggressive policy visits states the model cannot predict). This policy-relativity is inherent in any predictive sufficiency measure — it is not an artifact of the formulation. When comparing sufficiency values, the generating policy must be held constant or specified. #value-object's continuation-policy convention ($\pi_{\text{cont}}$) provides the required specification for value computations; the same convention should be understood as implicit here.
