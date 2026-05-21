---
slug: def-model-class-fitness
type: definition
status: axiomatic
depends:
  - def-model-sufficiency
stage: deps-verified
---

# Definition: Model Class Fitness

Where model sufficiency ( #def-model-sufficiency) measures how well a *specific* model retains the chronica's predictive information, **model class fitness** $\mathcal{F}(\mathcal{M})$ measures the *ceiling* — the supremum of sufficiency over every model in the agent's representational class $\mathcal{M}$. The pair formalizes a distinction the framework will soon make load-bearing: a low instance sufficiency might mean the agent needs more learning (parameter update); a low class fitness means no amount of better parameter estimation, more data, or longer training within the current class will close the gap — the agent needs a different *kind* of model entirely. The parallel to bias vs. variance in statistical learning is exact: class fitness is about bias (what the class can in principle represent); instance sufficiency reflects both bias and estimation quality.

The structural-inadequacy condition $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$ is the trigger this definition sets up for use later. When it holds, the gap from full predictive sufficiency cannot be closed parametrically. That is the precise hypothesis under which #result-structural-adaptation-necessity arrives in Chapter 4 — when class fitness is too low, the agent must change *what kind of model* it is. An important operational point: the agent cannot directly compute its class fitness (that would require searching over all models in $\mathcal{M}$). What it can observe is the *signature* — persistent mismatch despite adequate learning (high gain, sufficient data, converged parameters). When the floor doesn't go down with more work, the floor is structural.

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
