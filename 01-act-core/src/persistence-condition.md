---
slug: persistence-condition
type: result
status: exact
depends:
  - adaptive-tempo
  - mismatch-signal
  - sector-condition-stability
---

# Result: Persistence Condition

An agent maintains bounded mismatch — persists as a viable adaptive system — if and only if its correction efficiency exceeds the rate of environment change relative to its model class capacity.

## Formal Expression

*[Derived (persistence-threshold, from sector-condition analysis)]*

**General form (nonlinear):**

$$\alpha \gt \frac{\rho}{R}$$

where:
- $\alpha$ is the worst-case correction efficiency (the sector-condition lower bound on the correction function — see #sector-condition-stability)
- $\rho$ is the rate of environment change (rate of new mismatch introduction, GA-2: $\Vert w(t)\Vert \leq \rho$)
- $R$ is the model class capacity (radius of the region where the sector condition holds)

The ultimately bounded mismatch is $R^\ast = \rho / \alpha$, and persistence requires $R^\ast \lt R$.

**Linear operational form:**

$$\mathcal{T} \gt \frac{\rho}{\Vert\delta_{\text{critical}}\Vert}$$

In the linear case ($F(\mathcal{T}, \delta) = \mathcal{T} \cdot \delta$), $\alpha = \mathcal{T}$ exactly and $R \to \infty$. The critical mismatch $\Vert\delta_{\text{critical}}\Vert$ then replaces $R$ as the effective bound — the agent persists when steady-state mismatch $\rho / \mathcal{T}$ stays below the tolerance threshold. This is the form used throughout the theory as the operational persistence condition. It is exact for linear correction and a useful proxy for mildly nonlinear correction (where $\alpha \approx \mathcal{T}$), but it overstates the persistence margin when the correction function saturates at large mismatch.

**The relationship between $\alpha$ and $\mathcal{T}$:** For all correction functions tested in simulation (linear, saturating, sigmoid, threshold, structural breakdown), $\alpha$ is monotone increasing in $\mathcal{T}$ — higher tempo always improves correction efficiency. The quantitative relationship varies: for a saturating function with capacity $R$, $\alpha \approx \mathcal{T} / 2$ (worst case at the capacity boundary); for sigmoid (tanh), $\alpha \approx 0.76 \cdot \mathcal{T}$. The qualitative conclusion — "faster adaptation improves persistence" — holds for all correction function classes.

**Assumptions.** Bounded disturbance (GA-2) and sector condition on the correction function (GA-3). See #sector-condition-stability for the general nonlinear treatment from which this threshold emerges.

### Derivation

From #sector-condition-stability (Prop A.1 in #sector-condition-derivation): under the sector condition and bounded disturbance, mismatch is ultimately bounded by $R^\ast = \rho/\alpha$, and the agent persists iff $R^\ast \lt R$, i.e., $\alpha \gt \rho/R$.

In the linear case, $\alpha = \mathcal{T}$ and the relevant bound is $\Vert\delta_{\text{critical}}\Vert$ rather than $R$ (which is infinite), giving $\mathcal{T} \gt \rho / \Vert\delta_{\text{critical}}\Vert$. $\square$

### Per-Dimension Extension

*[Empirical Claim (per-dimension-persistence, from simulation variant F)]*

For anisotropic systems (non-uniform $\rho$ or $\mathcal{T}$ across dimensions), the scalar persistence condition is insufficient. Per-dimension:

$$\mathcal{T}_k \gt \frac{\rho_k}{\delta_{\text{critical},k}} \quad \text{for each dimension } k$$

The scalar condition overestimates by up to 72% in simulation. The weak dimension is the bottleneck (84% of total mismatch in simulation). See #per-dimension-persistence.

**Robustness**: The per-dimension condition matches discrete AR(1) prediction to 4 significant figures. The scalar overestimate is a consequence of Jensen's inequality applied to the norm.

## Epistemic Status

The threshold's *existence* is *robust qualitative* — any monotone correction function has a capacity limit; this holds across all correction functions tested (linear, saturating, threshold, sigmoid). The general form $\alpha \gt \rho / R$ is *exact* under the sector-condition assumptions (GA-2, GA-3; Prop A.1). The linear operational form $\mathcal{T} \gt \rho / \Vert\delta_{\text{critical}}\Vert$ is *exact* for linear correction (where $\alpha = \mathcal{T}$) and a *useful approximation* for mildly nonlinear correction. For strongly nonlinear correction (saturating, threshold, breakdown), the general $\alpha$-form is required — $\mathcal{T}$ overestimates $\alpha$ and the linear form overstates the persistence margin. Downstream segments that use $\mathcal{T} \gt \rho / \Vert\delta_{\text{critical}}\Vert$ should be understood as using the linear operational form; the qualitative conclusions hold because $\alpha$ is monotone in $\mathcal{T}$. The per-dimension extension is *empirically exact* (matches AR(1) prediction to 4 significant figures in simulation) but awaits formal derivation beyond the 1D case.

## Discussion

**This is structural persistence.** The persistence condition formalizes *structural persistence* (see Persistence in `LEXICON.md`) — whether the correction machinery's capacity can outpace the disturbance rate. It does not address *operational persistence* (whether the agent is currently near the boundary $R$, which is governed by the adaptive reserve $\Delta\rho^\ast$) or *continuity persistence* (whether the agent maintains coherent identity through time). A system can satisfy $\alpha > \rho/R$ and still be operationally fragile or have zero continuity. These are independent dimensions requiring independent analysis.

**Below threshold.** When $\alpha \leq \rho / R$ (or in the linear case, $\mathcal{T} \leq \rho / \Vert\delta_{\text{critical}}\Vert$), mismatch is not merely large — it grows without effective bound (up to $R$, the sector-condition region). The agent loses contact with reality. This is a qualitative transition, not a gradual degradation.

**$\delta_{\text{critical}}$ and $R$ are domain parameters, not theory outputs.** The theory derives the *existence* of a persistence threshold and its *form* (ratio of correction to disturbance). But the specific values of $\delta_{\text{critical}}$ (how much mismatch is tolerable) and $R$ (the model class capacity) are set by the application domain, not derived by ACT. $\delta_{\text{critical}}$ encodes "how wrong can the model be before the agent's actions become harmful or ineffective?" — this depends on the stakes, the action space, and the environment's forgiveness. $R$ encodes "how large a mismatch can the correction function handle before it saturates or breaks down?" — this depends on the model class and the correction architecture. See #operationalization for guidance on estimating these quantities in specific domains.

**Adaptive reserve.** The quantity $\Delta\rho^\ast = \alpha R - \rho$ (Prop A.2) measures how much additional disturbance the agent can absorb before persistence fails. Positive reserve means the agent has margin; zero reserve means it is at the threshold.

### Connections

The persistence condition appears in multiple downstream contexts:

- **Adversarial dynamics** ( #adversarial-tempo-advantage): Superlinear tempo advantage arises because persistence is a threshold — pushing an adversary below it causes qualitative collapse. *This connection is developed and validated in #adversarial-tempo-advantage and simulation variants A-D.*

- **Structural adaptation** ( #structural-adaptation-necessity): When model class fitness $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$, the effective $\alpha$ in the sector condition shrinks, eventually violating persistence. *This connection is developed in #structural-adaptation-necessity.*

- **Software maintainability** ( #code-quality-as-observation-infrastructure — cross-component reference, see `02-tst-core/`): *[Discussion]* A codebase may become "unmaintainable" when the development team's adaptive tempo falls below the rate of complexity accumulation. The vicious cycle would then be the persistence condition being violated through the agent's own prior actions degrading future $\mathcal{T}$ via $U_o$. *This connection is structurally motivated but not yet formally derived within ACT. It requires formalizing "complexity accumulation rate" as an instance of $\rho$.*
