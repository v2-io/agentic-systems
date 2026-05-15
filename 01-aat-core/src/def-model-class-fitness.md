---
slug: def-model-class-fitness
type: definition
status: axiomatic
depends:
  - def-model-sufficiency
stage: deps-verified
---

# Definition: Model Class Fitness

The best achievable sufficiency within a model class. When no model in the class can adequately represent reality, the agent faces a structural limitation that no amount of parameter tuning can resolve.

## Formal Expression

*[Definition (model-class-fitness)]*

$$\mathcal{F}(\mathcal{M}) = \sup_{M \in \mathcal{M}} S(M)$$

where $\mathcal{M}$ is the model class — the set of all models the agent can represent given its current architecture, parameterization, or capacity.

**Structural inadequacy condition:**

$$\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$$

When this holds, no model $M \in \mathcal{M}$ achieves sufficiency above $1 - \varepsilon$. The gap is structural: it cannot be closed by better parameter estimation, more data, or longer training within the current class. This is the trigger for structural change ( #result-structural-adaptation-necessity).

## Epistemic Status

This is *definitional* — it names the supremum of sufficiency over a model class. The definition itself is straightforward. The substantive claim about what happens when $\mathcal{F}(\mathcal{M})$ is low — that parametric updates cannot close the mismatch floor and structural adaptation becomes necessary — is developed in #result-structural-adaptation-necessity.

## Discussion

**Model class vs. model instance.** $S(M_t)$ measures a specific model's sufficiency at time $t$. $\mathcal{F}(\mathcal{M})$ measures the ceiling of the entire class. A low $S(M_t)$ might mean the agent needs more learning (parameter update). A low $\mathcal{F}(\mathcal{M})$ means the agent needs a different kind of model (structural change). The distinction parallels bias vs. variance: class fitness is about bias; instance sufficiency reflects both bias and estimation quality.

**Detecting low class fitness.** The agent cannot directly compute $\mathcal{F}(\mathcal{M})$ — it would need to search over all models in the class. Instead, persistent mismatch despite adequate learning (high gain, sufficient data, converged parameters) is the observable signature. This connects to the mismatch floor in #result-structural-adaptation-necessity.
