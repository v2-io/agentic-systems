---
slug: persistence-condition
type: theorem
status: exact (under sector-condition assumptions GA-2, GA-3)
depends:
  - adaptive-tempo
  - mismatch-signal
  - sector-condition-stability
---

# Persistence Condition

An agent maintains bounded mismatch — persists as a viable adaptive system — if
and only if its adaptive tempo exceeds the rate of environment change relative
to its tolerance threshold.

## Formal Expression

*[Derived (persistence-threshold, from sector-condition analysis)]*
$$\mathcal{T} > \frac{\rho}{\|\delta_{\text{critical}}\|}$$

where:
- $\mathcal{T}$ is the adaptive tempo: $\sum_k \nu^{(k)} \cdot \eta^{(k)*}$
  (#adaptive-tempo)
- $\rho$ is the rate of environment change (rate of new mismatch introduction)
- $\delta_{\text{critical}}$ is the maximum tolerable mismatch magnitude

**Assumptions.** Bounded disturbance ($\|w(t)\| \leq \rho$, GA-2) and sector
condition on the correction function (GA-3). See #sector-condition-stability
for the general nonlinear treatment from which this threshold emerges.

## Epistemic Status

The threshold's *existence* is *robust qualitative* — any monotone correction
function has a capacity limit; this holds across all correction functions tested
(linear, saturating, threshold, sigmoid). The quantitative form
$\mathcal{T} > \rho / \|\delta_{\text{critical}}\|$ is *exact* under the
sector-condition assumptions (GA-2, GA-3; Prop A.1). The linear ODE gives the
same threshold as a special case. The per-dimension extension is *empirically
exact* (matches AR(1) prediction to 4 significant figures in simulation) but
awaits formal derivation beyond the 1D case.

## Proof Sketch

From the sector-condition analysis (#sector-condition-stability):

1. The correction function $F(\mathcal{T}, \delta)$ satisfies the sector bound:
   $\delta^T F \geq \alpha \|\delta\|^2$ for $\|\delta\| \leq R$.
2. The Lyapunov function $V(\delta) = \frac{1}{2}\|\delta\|^2$ satisfies:
   $\dot{V} \leq -\alpha\|\delta\|^2 + \rho\|\delta\|$
3. This gives $\dot{V} < 0$ when $\|\delta\| > \rho/\alpha$.
4. Ultimate bound: $\|\delta\| \leq R^* = \rho/\alpha$.
5. The agent persists (mismatch stays bounded within tolerance) when
   $R^* < \|\delta_{\text{critical}}\|$, i.e., $\alpha > \rho/\|\delta_{\text{critical}}\|$.

The full proof is in Appendix A (Prop A.1). $\square$

## Discussion

**Below threshold.** When $\mathcal{T} \leq \rho / \|\delta_{\text{critical}}\|$,
mismatch is not merely large — it grows without effective bound (up to $R$, the
sector-condition region). The agent loses contact with reality. This is a
qualitative transition, not a gradual degradation.

**Adaptive reserve.** The quantity $\Delta\rho^* = \alpha R - \rho$ (Prop A.2)
measures how much additional disturbance the agent can absorb before persistence
fails. Positive reserve means the agent has margin; zero reserve means it is at
the threshold.

## Per-Dimension Extension

*[Derived (from simulation variant F — empirically exact)]*

For anisotropic systems (non-uniform $\rho$ or $\mathcal{T}$ across dimensions),
the scalar persistence condition is insufficient. Per-dimension:

$$\mathcal{T}_k > \frac{\rho_k}{\delta_{\text{critical},k}} \quad \text{for each dimension } k$$

The scalar condition overestimates by up to 72% in simulation. The weak
dimension is the bottleneck (84% of total mismatch in simulation). See
#per-dimension-persistence.

**Robustness**: The per-dimension condition matches discrete AR(1) prediction to
4 significant figures. The scalar overestimate is a consequence of Jensen's
inequality applied to the norm.

## Connections

The persistence condition appears in multiple downstream contexts:

- **Adversarial dynamics** (#adversarial-tempo-advantage): Superlinear tempo
  advantage arises because persistence is a threshold — pushing an adversary
  below it causes qualitative collapse. *This connection is developed and
  validated in #adversarial-tempo-advantage and simulation variants A–D.*

- **Structural adaptation** (#structural-adaptation-necessity): When model class
  fitness $\mathcal{F}(\mathcal{M}) < 1 - \varepsilon$, the effective $\alpha$
  in the sector condition shrinks, eventually violating persistence. *This
  connection is developed in #structural-adaptation-necessity.*

- **Software maintainability** (#code-quality-as-observation-infrastructure):
  *[Plausible]* A codebase may become "unmaintainable" when the development
  team's adaptive tempo falls below the rate of complexity accumulation. The
  vicious cycle would then be the persistence condition being violated through
  the agent's own prior actions degrading future $\mathcal{T}$ via $U_o$.
  *This connection is structurally motivated but not yet formally derived
  within ACT. It requires formalizing "complexity accumulation rate" as an
  instance of $\rho$.*
