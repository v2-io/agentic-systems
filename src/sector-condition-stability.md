---
slug: sector-condition-stability
type: result
status: exact
depends:
  - adaptive-tempo
  - mismatch-signal
  - sector-condition-derivation
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

The mismatch $\delta(t)$ is ultimately bounded by $R^\ast = \rho / \alpha$. The agent persists (avoids divergence) iff:

$$\alpha \gt \frac{\rho}{R}$$

*[Derived (adaptive-reserve)]*

The agent's capacity to absorb additional disturbance before mismatch exceeds the valid region:

$$\Delta\rho^* = \alpha R - \rho$$

### Derivation

1. Lyapunov function $V(\delta) = \frac{1}{2}\Vert\delta\Vert^2$.
2. $\dot{V} = \delta^T(-F + w) \leq -\alpha\Vert\delta\Vert^2 + \rho\Vert\delta\Vert$.
3. $\dot{V} \lt 0$ when $\Vert\delta\Vert \gt \rho/\alpha$, giving ultimate bound $R^\ast = \rho/\alpha$.
4. Persistence requires $R^\ast \lt R$, i.e., $\alpha \gt \rho/R$. $\square$

Full derivation in #sector-condition-derivation (Props A.1, A.2).

## Epistemic Status

These results are *exact* consequences of standard Lyapunov stability theory under the sector condition and bounded disturbance assumptions. They replace the linear ODE ($\dot{\delta} = -\mathcal{T}\delta + \rho$) with a rigorous nonlinear foundation. The linear ODE is recovered as a special case where $F(\mathcal{T}, \delta) = \mathcal{T}\delta$ and $\alpha = \mathcal{T}$.

## Discussion

**Why the sector condition.** The linear ODE assumes correction scales linearly with mismatch forever. Real adaptive systems saturate, exhibit thresholding, or break down when the model class is exhausted. The sector condition captures the minimal structural requirement: the correction must point in the right direction with at least baseline efficiency $\alpha$.

**Generalizing the persistence threshold.** In the linear case, $\alpha = \mathcal{T}$ (adaptive tempo). The general result $\alpha \gt \rho/R$ proves the persistence threshold ( #persistence-condition) is a structural necessity of any bounded-correction system, not an artifact of the linear approximation.

**Connection to structural adaptation.** When $\rho/\alpha \gt R$, disturbance exceeds the model class's capacity. The sector condition fails — this is the dynamical trigger for structural adaptation ( #structural-adaptation-necessity), requiring a new model class with larger valid radius $R'$ or better efficiency $\alpha'$.