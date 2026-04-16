---
slug: persistence-condition
type: result
status: exact
depends:
  - adaptive-tempo
  - mismatch-signal
  - sector-condition-stability
stage: claims-verified
---

# Result: Persistence Condition

An agent persists when two independent conditions hold: the correction machinery can contain mismatch within its operating region (*structural persistence*), and the resulting steady-state mismatch is small enough for the agent's actions to remain adequate (*task adequacy*).

## Formal Expression

### Structural Persistence

*[Derived (structural-persistence, from sector-condition analysis)]*

The correction machinery contains mismatch within its operating region:

**Model D** (deterministic bounded disturbance, GA-2):

$$\alpha \gt \frac{\rho}{R}$$

**Model S** (stochastic disturbance, GA-2S):

$$\alpha > \frac{n\sigma_w^2}{2R^2}$$

where:
- $\alpha$ is the worst-case correction efficiency (the sector-condition lower bound — see #sector-condition-stability)
- $\rho$ is the disturbance bound (GA-2: $\lVert w(t)\rVert \leq \rho$); $\sigma_w^2 = \mathbb{E}[\lVert w(t)\rVert^2]$ for Model S
- $R$ is the model class capacity (radius of the region where the sector condition holds)
- $n = \dim(\delta)$

Structural persistence is about the *machinery*, not the task. It says "the correction dynamics can keep mismatch bounded within the region where the Lyapunov guarantee holds." It is a property of the agent's adaptive architecture, not of its goals or domain. The ultimately bounded mismatch is $R^\ast = \rho / \alpha$ (Model D) or $R^*_S = \sigma_w\sqrt{n/(2\alpha)}$ (Model S), and structural persistence requires $R^\ast \lt R$.

**In the linear case** ($F(\mathcal{T}, \delta) = \mathcal{T} \cdot \delta$), $\alpha = \mathcal{T}$ exactly and $R \to \infty$. Structural persistence is then satisfied trivially — any agent with $\mathcal{T} \gt 0$ is structurally persistent under linear correction. This is why the "linear operational form" below exists: when structural persistence is free, the binding constraint is task adequacy.

### Task Adequacy

*[Definition (task-adequacy)]*

The steady-state mismatch is small enough for the agent's actions to remain acceptable:

$$R^\ast \lt \lVert\delta_{\text{critical}}\rVert$$

where $\lVert\delta_{\text{critical}}\rVert$ is a domain-specific tolerance threshold — "how wrong can the model be before the agent's actions become harmful or ineffective?" This is set by the application domain, not derived by ACT.

**Task adequacy is a separate condition from structural persistence.** An agent can be structurally persistent ($R^\ast \lt R$) but task-inadequate ($R^\ast \gt \lVert\delta_{\text{critical}}\rVert$) — the machinery contains mismatch, but not tightly enough for the domain's needs. Conversely, when $\lVert\delta_{\text{critical}}\rVert \lt R$ (the domain's tolerance is stricter than the model class capacity), task adequacy is the binding constraint.

### Operational Persistence Condition

*[Derived (operational-persistence, conjunction of structural persistence + task adequacy)]*

The agent persists operationally when BOTH conditions hold. In the nonlinear case with $\lVert\delta_{\text{critical}}\rVert \lt R$, the binding condition is:

$$\alpha \gt \frac{\rho}{\lVert\delta_{\text{critical}}\rVert} \quad \text{(Model D)} \qquad \alpha > \frac{n\sigma_w^2}{2\lVert\delta_{\text{critical}}\rVert^2} \quad \text{(Model S)}$$

These are the same as the structural conditions with $R$ replaced by $\lVert\delta_{\text{critical}}\rVert$, because when $\lVert\delta_{\text{critical}}\rVert \lt R$, task adequacy is stricter.

**Linear operational forms:** In the linear case ($\alpha = \mathcal{T}$, $R \to \infty$), structural persistence is trivially satisfied and the operational condition reduces to task adequacy alone:

$$\mathcal{T} \gt \frac{\rho}{\lVert\delta_{\text{critical}}\rVert} \quad \text{(Model D)} \qquad \mathcal{T} > \frac{n\sigma_w^2}{2\lVert\delta_{\text{critical}}\rVert^2} \quad \text{(Model S)}$$

These are the forms used throughout the theory as the operational persistence condition. They are exact for linear correction and useful proxies for mildly nonlinear correction (where $\alpha \approx \mathcal{T}$), but they overstate the persistence margin when the correction function saturates, because they omit the structural constraint ($\alpha \gt \rho/R$) that becomes binding when $R$ is finite.

**Per-dimension (Model S):** $\eta_k > c \cdot \rho_k^2 / \delta_{\text{critical},k}^2$ where $c$ depends on the probability guarantee. See #per-dimension-persistence.

### Common Properties

**The relationship between $\alpha$ and $\mathcal{T}$:** #gain-sector-bridge shows that for agents with directional fidelity, $\alpha = \eta^\ast \cdot c_{\min}$ where $c_{\min}$ is the worst-case directional fidelity. For linear correction (Kalman, Beta-Bernoulli), $\alpha = \mathcal{T}$ exactly. For gradient descent on strongly convex losses, $\alpha = \eta \cdot \mu$ where $\mu$ is the strong convexity modulus — monotone in $\eta$ (and hence in $\mathcal{T}$) for fixed loss landscape. For nonlinear correction tested in simulation (saturating, sigmoid, threshold), $\alpha$ remains monotone increasing in $\mathcal{T}$: for a saturating function with capacity $R$, $\alpha \approx \mathcal{T} / 2$ (worst case at the capacity boundary); for sigmoid (tanh), $\alpha \approx 0.76 \cdot \mathcal{T}$. The qualitative conclusion — "faster adaptation improves persistence" — is structurally grounded for the important cases and empirically confirmed for all correction function classes tested.

**Assumptions.** The Model D threshold assumes bounded disturbance (GA-2) and sector condition (GA-3). The Model S threshold assumes stochastic disturbance (GA-2S) and the same sector condition (GA-3). See #sector-condition-stability for the general nonlinear treatment from which both thresholds emerge.

### Derivation

**Structural (Model D):** From Prop A.1 in #sector-condition-derivation: under the sector condition and bounded disturbance, mismatch is ultimately bounded by $R^\ast = \rho/\alpha$. The agent is structurally persistent iff $R^\ast \lt R$, i.e., $\alpha \gt \rho/R$. $\square$

**Structural (Model S):** From Prop A.1S in #sector-condition-derivation: under the sector condition and stochastic disturbance, the RMS mismatch converges to $\sigma_w\sqrt{n/(2\alpha)}$. Structurally persistent (mean-square) iff $\alpha > n\sigma_w^2/(2R^2)$. $\square$

**Operational:** Structural persistence gives $R^\ast$. Task adequacy requires $R^\ast \lt \lVert\delta_{\text{critical}}\rVert$. Combined: $\alpha \gt \rho/\min(R, \lVert\delta_{\text{critical}}\rVert)$. In the linear case $R \to \infty$, so $\min(R, \lVert\delta_{\text{critical}}\rVert) = \lVert\delta_{\text{critical}}\rVert$. $\square$

### Per-Dimension Extension

*[Empirical Claim (per-dimension-persistence, from simulation variant F)]*

For anisotropic systems (non-uniform $\rho$ or $\mathcal{T}$ across dimensions), the scalar persistence condition is insufficient. Per-dimension:

$$\mathcal{T}_k \gt \frac{\rho_k}{\delta_{\text{critical},k}} \quad \text{for each dimension } k$$

The scalar condition overestimates by up to 72% in simulation. The weak dimension is the bottleneck (84% of total mismatch in simulation). See #per-dimension-persistence.

**Robustness**: The per-dimension condition matches discrete AR(1) prediction to 4 significant figures. The scalar overestimate is a consequence of Jensen's inequality applied to the norm.

## Epistemic Status

**Structural persistence** thresholds are *exact* under their stated assumptions: Model D gives $\alpha > \rho/R$ (Prop A.1, exact under GA-2, GA-3); Model S gives $\alpha > n\sigma_w^2/(2R^2)$ (Prop A.1S, exact under GA-2S, GA-3). The threshold's *existence* is *robust qualitative* — any monotone correction function has a capacity limit; this holds across all correction functions tested.

**Task adequacy** ($R^\ast < \lVert\delta_{\text{critical}}\rVert$) is *exact as a definition* — given $R^\ast$ (derived) and $\lVert\delta_{\text{critical}}\rVert$ (domain parameter), the comparison is well-defined. The substance lies in estimating $\lVert\delta_{\text{critical}}\rVert$ for specific domains, which is an operationalization question ( #operationalization), not a theory question.

**The linear operational forms** ($\mathcal{T} > \rho/\lVert\delta_{\text{critical}}\rVert$ for Model D; $\mathcal{T} > n\sigma_w^2/(2\lVert\delta_{\text{critical}}\rVert^2)$ for Model S) are *exact* for linear correction (where they express task adequacy alone, structural persistence being trivially satisfied) and *useful approximations* for mildly nonlinear correction (where $\alpha \approx \mathcal{T}$). For strongly nonlinear correction, the general $\alpha$-forms are required and BOTH structural and task-adequacy conditions must be checked. Downstream segments that use the linear operational forms should be understood as expressing task adequacy, not structural stability.

The per-dimension extension is *empirically exact* for Model S (matches AR(1) prediction to 4 significant figures in simulation); the Model D per-dimension threshold ($\mathcal{T}_k > \rho_k/\delta_{\text{critical},k}$) is exact by the same Lyapunov argument applied per dimension.

## Discussion

**Two conditions, not one.** This segment now separates what was previously conflated. Structural persistence ($\alpha > \rho/R$) is the Lyapunov-derived result — it says the machinery *works*. Task adequacy ($R^\ast < \lVert\delta_{\text{critical}}\rVert$) is a domain-specific constraint — it says the machinery works *well enough*. Neither implies the other, and downstream segments should specify which they mean. Most adversarial-dynamics results ( #adversarial-tempo-advantage, #adversarial-destabilization) depend on structural persistence. Most domain instantiations (TST, logogenic agent design) care about task adequacy. See Persistence in `LEXICON.md` and `README.md` for the full three-sense taxonomy (structural, operational, continuity).

**Below structural threshold.** When $\alpha \leq \rho / R$, mismatch is not merely large — it grows without effective bound (up to $R$, the sector-condition region). The correction machinery is overwhelmed. This is a qualitative transition, not a gradual degradation.

**Below task-adequacy threshold.** When $R^\ast > \lVert\delta_{\text{critical}}\rVert$ but $R^\ast < R$, the system is structurally stable but performing unacceptably. Mismatch is bounded but too large for the domain. The remedy is different from structural failure: increase $\mathcal{T}$ (faster or better correction), decrease $\rho$ (reduce environmental volatility), or relax $\lVert\delta_{\text{critical}}\rVert$ (accept more mismatch). Structural failure requires changing the correction architecture entirely ( #structural-adaptation-necessity).

**$\delta_{\text{critical}}$ and $R$ are domain parameters, not theory outputs.** The theory derives the *existence* of persistence thresholds and their *form* (ratio of correction to disturbance). But the specific values are set by the application domain: $\delta_{\text{critical}}$ encodes "how wrong can the model be before the agent's actions become harmful or ineffective?" — this depends on the stakes, the action space, and the environment's forgiveness. $R$ encodes "how large a mismatch can the correction function handle before it saturates or breaks down?" — this depends on the model class and the correction architecture. See #operationalization for guidance on estimating these quantities in specific domains.

**Channel independence and scalar tempo.** The linear operational forms use scalar $\mathcal{T}$, which inherits the channel-independence assumption from #adaptive-tempo: the additive formula overcounts when observation channels are correlated. In anisotropic systems the scalar condition also overestimates margins — up to 72% in simulation (see #adaptive-tempo, scalar vs. vector tempo). Where precision matters, the per-dimension condition ($\mathcal{T}_k > \rho_k / \delta_{\text{critical},k}$) should be used instead.

**Adaptive reserve.** The quantity $\Delta\rho^\ast = \alpha R - \rho$ (Prop A.2) measures how much additional disturbance the agent can absorb before persistence fails. Positive reserve means the agent has margin; zero reserve means it is at the threshold.

### Connections

The persistence condition appears in multiple downstream contexts:

- **Adversarial dynamics** ( #adversarial-tempo-advantage): Superlinear tempo advantage arises because persistence is a threshold — pushing an adversary below it causes qualitative collapse. *This connection is developed and validated in #adversarial-tempo-advantage and simulation variants A-D.*

- **Structural adaptation** ( #structural-adaptation-necessity): When model class fitness $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$, the effective $\alpha$ in the sector condition shrinks, eventually violating persistence. *This connection is developed in #structural-adaptation-necessity.*

- **Software maintainability** ( #code-quality-as-observation-infrastructure — cross-component reference, see `02-tst-core/`): *[Discussion]* A codebase may become "unmaintainable" when the development team's adaptive tempo falls below the rate of complexity accumulation. The vicious cycle would then be the persistence condition being violated through the agent's own prior actions degrading future $\mathcal{T}$ via $U_o$. *This connection is structurally motivated but not yet formally derived within ACT. It requires formalizing "complexity accumulation rate" as an instance of $\rho$.*
