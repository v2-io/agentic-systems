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

$F$ satisfies the **local sector condition** for $\|\delta\| \leq R$:

$$\delta^T F(\mathcal{T}, \delta) \geq \alpha \|\delta\|^2$$

where $\alpha > 0$ is the worst-case correction efficiency within the valid region of radius $R$ (the model class capacity). Disturbance is bounded: $\|w(t)\| \leq \rho$.

*[Derived (bounded-mismatch, from Lyapunov analysis)]*

The mismatch $\delta(t)$ is ultimately bounded by $R^* = \rho / \alpha$. The agent persists (avoids divergence) iff:

$$\alpha > \frac{\rho}{R}$$

*[Derived (adaptive-reserve)]*

The agent's capacity to absorb additional disturbance before mismatch exceeds the valid region:

$$\Delta\rho^* = \alpha R - \rho$$

### Derivation

1. Lyapunov function $V(\delta) = \frac{1}{2}\|\delta\|^2$.
2. $\dot{V} = \delta^T(-F + w) \leq -\alpha\|\delta\|^2 + \rho\|\delta\|$.
3. $\dot{V} < 0$ when $\|\delta\| > \rho/\alpha$, giving ultimate bound $R^* = \rho/\alpha$.
4. Persistence requires $R^* < R$, i.e., $\alpha > \rho/R$. $\square$

Full derivation in #sector-condition-derivation (Props A.1, A.2).

## Epistemic Status

These results are *exact* consequences of standard Lyapunov stability theory under the sector condition and bounded disturbance assumptions. They replace the linear ODE ($\dot{\delta} = -\mathcal{T}\delta + \rho$) with a rigorous nonlinear foundation. The linear ODE is recovered as a special case where $F(\mathcal{T}, \delta) = \mathcal{T}\delta$ and $\alpha = \mathcal{T}$.

## Discussion

**Why the sector condition.** The linear ODE assumes correction scales linearly with mismatch forever. Real adaptive systems saturate, exhibit thresholding, or break down when the model class is exhausted. The sector condition captures the minimal structural requirement: the correction must point in the right direction with at least baseline efficiency $\alpha$.

**Generalizing the persistence threshold.** In the linear case, $\alpha = \mathcal{T}$ (adaptive tempo). The general result $\alpha > \rho/R$ proves the persistence threshold ( #persistence-condition) is a structural necessity of any bounded-correction system, not an artifact of the linear approximation.

**Connection to structural adaptation.** When $\rho/\alpha > R$, disturbance exceeds the model class's capacity. The sector condition fails — this is the dynamical trigger for structural adaptation ( #structural-adaptation-necessity), requiring a new model class with larger valid radius $R'$ or better efficiency $\alpha'$.