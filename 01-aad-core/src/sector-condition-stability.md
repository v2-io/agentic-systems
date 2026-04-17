---
slug: sector-condition-stability
type: result
status: exact
depends:
  - adaptive-tempo
  - mismatch-signal
  - sector-condition-derivation
stage: claims-verified
---

# Result: Sector Condition Stability

An agent's mismatch remains bounded if its correction function satisfies a sector condition (points inward with at least baseline efficiency) and the effective correction strength exceeds the environmental disturbance rate.

## Formal Expression

Let $\delta(t) \in \mathbb{R}^n$ be the vector of model-reality mismatches. The mismatch dynamics:

*[Formulation]*

$$\frac{d\delta}{dt} = -F(\mathcal{T}, \delta) + w(t)$$

where $F$ is a (possibly nonlinear) correction function and $w(t)$ is environmental disturbance.

*[Assumption (sector-condition)]*

$F$ satisfies the **local sector condition** for $\Vert\delta\Vert \leq R$:

$$\delta^T F(\mathcal{T}, \delta) \geq \alpha \Vert\delta\Vert^2$$

where $\alpha \gt 0$ is the worst-case correction efficiency within the valid region of radius $R$ (the model class capacity). Disturbance is bounded: $\Vert w(t)\Vert \leq \rho$.

*[Derived (bounded-mismatch, from Lyapunov analysis)]*

**Model D (deterministic bounded disturbance, GA-2).** The mismatch $\delta(t)$ is ultimately bounded by $R^\ast = \rho / \alpha$. The agent persists (avoids divergence) iff:

$$\alpha \gt \frac{\rho}{R}$$

**Model S (stochastic disturbance, GA-2S).** Under stochastic zero-mean disturbance with $\mathbb{E}[\lVert w(t)\rVert^2] = \sigma_w^2$, the steady-state RMS mismatch is:

$$R^*_S = \sigma_w\sqrt{\frac{n}{2\alpha}}$$

where $n = \dim(\delta)$. The agent persists in the mean-square sense iff $\alpha > n\sigma_w^2/(2R^2)$. The key difference: Model D scales as $1/\alpha$; Model S scales as $1/\sqrt{\alpha}$. See Prop A.1S in #sector-condition-derivation.

*[Derived (adaptive-reserve)]*

The agent's capacity to absorb additional disturbance before mismatch exceeds the valid region:

$$\Delta\rho^* = \alpha R - \rho$$

### Derivation

1. Lyapunov function $V(\delta) = \frac{1}{2}\Vert\delta\Vert^2$.
2. $\dot{V} = \delta^T(-F + w) \leq -\alpha\Vert\delta\Vert^2 + \rho\Vert\delta\Vert$.
3. $\dot{V} \lt 0$ when $\Vert\delta\Vert \gt \rho/\alpha$, giving ultimate bound $R^\ast = \rho/\alpha$.
4. Persistence requires $R^\ast \lt R$, i.e., $\alpha \gt \rho/R$. $\square$

Full derivation in #sector-condition-derivation (Props A.1, A.1S, A.2).

## Epistemic Status

The Model D results ($R^* = \rho/\alpha$, persistence iff $\alpha > \rho/R$) are *exact* consequences of standard Lyapunov stability theory under the sector condition and bounded disturbance assumptions (GA-2, GA-3). The Model S results ($R^*_S = \sigma_w\sqrt{n/(2\alpha)}$, persistence iff $\alpha > n\sigma_w^2/(2R^2)$) are *exact* consequences of Itô-Lyapunov analysis under the sector condition and stochastic disturbance assumptions (GA-2S, GA-3). Both replace the linear ODE ($\dot{\delta} = -\mathcal{T}\delta + \rho$) with a rigorous nonlinear foundation. The linear ODE is recovered as a special case where $F(\mathcal{T}, \delta) = \mathcal{T}\delta$ and $\alpha = \mathcal{T}$. Which disturbance model applies is a domain question, not a theory question.

## Discussion

**Why the sector condition.** The linear ODE assumes correction scales linearly with mismatch forever. Real adaptive systems saturate, exhibit thresholding, or break down when the model class is exhausted. The sector condition captures the minimal structural requirement: the correction must point in the right direction with at least baseline efficiency $\alpha$.

**Generalizing the persistence threshold.** In the linear case, $\alpha = \mathcal{T}$ (adaptive tempo). The general result $\alpha \gt \rho/R$ proves the persistence threshold ( #persistence-condition) is a structural necessity of any bounded-correction system, not an artifact of the linear approximation. Like the persistence condition itself, this result addresses *structural persistence* — the machinery's capacity to bound mismatch — not operational persistence (current proximity to $R$) or continuity persistence (identity through time). See Persistence in `LEXICON.md` for the full disambiguation.

**Connection to structural adaptation.** When $\rho/\alpha \gt R$, disturbance exceeds the model class's capacity. The sector condition fails — this is the dynamical trigger for structural adaptation ( #structural-adaptation-necessity), requiring a new model class with larger valid radius $R'$ or better efficiency $\alpha'$.