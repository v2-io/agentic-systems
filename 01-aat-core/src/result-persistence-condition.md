---
slug: result-persistence-condition
type: result
status: exact
depends:
  - def-adaptive-tempo
  - def-mismatch-signal
  - result-sector-condition-stability
  - result-sector-persistence-template
stage: claims-verified
---

# Result: Persistence Condition

This is the volume's **central inequality** in its operational form. The segment's headline contribution is the *two-condition decomposition*: persistence is not one threshold but two, with different mechanisms and different remedies.

**Structural persistence** is the Lyapunov-derived condition that the correction machinery contains mismatch within its operating region: $\alpha \gt \rho/R$ under deterministic bounded disturbance, or $\alpha \gt n\sigma_w^2/(2R^2)$ under stochastic disturbance. This says *the machinery works*. Mismatch is ultimately bounded by $R^\ast = \rho/\alpha$ (Model D) or $\sigma_w\sqrt{n/(2\alpha)}$ (Model S). When this inequality fails, mismatch grows without effective bound (up to the sector-region edge) — a qualitative regime transition, not a gradual degradation.

**Task adequacy** is the separate condition that the steady-state mismatch is small enough for the agent's actions to remain useful: $R^\ast \lt \lVert\delta_{\text{critical}}\rVert$, where the critical-mismatch threshold is a *domain-specific tolerance* — how wrong can the model be before the agent's actions become harmful or ineffective? Set by the application, not derived by AAT. The two conditions are independent: an agent can be structurally persistent but task-inadequate (the machinery contains mismatch but not tightly enough for the domain). The remedies differ — task inadequacy can be fixed by raising tempo, lowering disturbance, or relaxing tolerance; structural failure requires changing the correction architecture entirely.

When the linear ODE applies (sector parameter equals tempo, valid region is unbounded), structural persistence is automatically satisfied and the binding condition is just task adequacy: $\mathcal{T} \gt \rho / \lVert\delta_{\text{critical}}\rVert$ under Model D. This is the form most downstream applications cite. It is exact for linear correction and a useful proxy for mildly nonlinear correction (where $\alpha \approx \mathcal{T}$), but overstates persistence when correction saturates.

A consequence the framework emphasizes: **the persistence condition is a structural pattern that recurs across domains rather than a model of any one of them**. The same inequality — correction rate against disturbance rate, normalized by tolerance — governs a Kalman filter on a moving target, an organization adapting to market shifts, an immune system tracking a pathogen, a developer keeping pace with a codebase, an organism evolving against environmental change. The structure recurs because the *math* recurs; whether the specific mechanism (tempo limited by some particular bottleneck) is the *dominant* cause in any given empirical case is left as an open empirical question per domain. The two-condition decomposition specifically prevents one common category error in domain transfer: a structurally-persistent codebase team can be task-inadequate, and conflating the two would yield the wrong intervention.

A complementary cost shadow: persistence has a *price*, not just a threshold. Under stochastic disturbance, maintaining the ultimate bound requires sustained Shannon information acquisition at rate at least $n\alpha/2$ nats per unit time — a Landauer-analog floor that the Kalman-Bucy filter saturates (see #deriv-persistence-cost). The threshold says whether persistence is *possible*; the information-rate corollary says what it *costs*. Two agents with identical persistence guarantees can face wildly different sustained demands because the cost scales linearly with the sector parameter; the threshold alone cannot distinguish dormant from running-hot.

A per-dimension extension addresses anisotropy: when correction capacity varies across dimensions, the scalar condition can overestimate persistence margin substantially (up to 72% in simulation). The correct condition is per-dimension; under cross-dimensional correction the canonical sharp form is the matrix-Loewner persistence condition ( #deriv-matrix-persistence-condition).

## Formal Expression

This segment is the canonical single-agent instantiation of the sector-persistence template ( #result-sector-persistence-template) with state variable $\xi = \delta_t$ (epistemic mismatch), correction function $F(\mathcal{T}, \delta)$, and disturbance rate $\rho_\xi = \rho$ (environmental change rate). Structural persistence is the direct template conclusion. Task adequacy adds a domain-specific constraint beyond the template's reach.

### Structural Persistence

*[Derived (structural-persistence, from sector-persistence-template)]*

Applying the template to the single-agent epistemic case gives: the correction machinery bounds $\delta$ within the model class capacity iff

$$\alpha \gt \frac{\rho}{R} \quad \text{(Model D)} \qquad \alpha \gt \frac{n\sigma_w^2}{2R^2} \quad \text{(Model S)}$$

with ultimate bound $R^\ast = \rho/\alpha$ (Model D) or $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$ (Model S). See #result-sector-condition-stability for how (T1)–(T3) are verified in this instantiation, and #deriv-sector-condition for the proof. Structural persistence is a property of the adaptive architecture — the machinery's ability to contain mismatch — not of the task.

**Linear case.** When $F(\mathcal{T}, \delta) = \mathcal{T}\delta$, $\alpha = \mathcal{T}$ and $R \to \infty$, so structural persistence is trivially satisfied whenever $\mathcal{T} \gt 0$. The binding constraint then becomes task adequacy (below).

### Task Adequacy

*[Definition (task-adequacy)]*

The steady-state mismatch is small enough for the agent's actions to remain acceptable:

$$R^\ast \lt \lVert\delta_{\text{critical}}\rVert$$

where $\lVert\delta_{\text{critical}}\rVert$ is a domain-specific tolerance threshold — "how wrong can the model be before the agent's actions become harmful or ineffective?" This is set by the application domain, not derived by AAT.

**Task adequacy is a separate condition from structural persistence.** An agent can be structurally persistent ($R^\ast \lt R$) but task-inadequate ($R^\ast \gt \lVert\delta_{\text{critical}}\rVert$) — the machinery contains mismatch, but not tightly enough for the domain's needs. Conversely, when $\lVert\delta_{\text{critical}}\rVert \lt R$ (the domain's tolerance is stricter than the model class capacity), task adequacy is the binding constraint.

### Operational Persistence Condition

*[Derived (operational-persistence, conjunction of structural persistence + task adequacy)]*

The agent persists operationally when BOTH conditions hold. In the nonlinear case with $\lVert\delta_{\text{critical}}\rVert \lt R$, the binding condition is:

$$\alpha \gt \frac{\rho}{\lVert\delta_{\text{critical}}\rVert} \quad \text{(Model D)} \qquad \alpha \gt \frac{n\sigma_w^2}{2\lVert\delta_{\text{critical}}\rVert^2} \quad \text{(Model S)}$$

These are the same as the structural conditions with $R$ replaced by $\lVert\delta_{\text{critical}}\rVert$, because when $\lVert\delta_{\text{critical}}\rVert \lt R$, task adequacy is stricter.

**Linear operational forms:** In the linear case ($\alpha = \mathcal{T}$, $R \to \infty$), structural persistence is trivially satisfied and the operational condition reduces to task adequacy alone:

$$\mathcal{T} \gt \frac{\rho}{\lVert\delta_{\text{critical}}\rVert} \quad \text{(Model D)} \qquad \mathcal{T} \gt \frac{n\sigma_w^2}{2\lVert\delta_{\text{critical}}\rVert^2} \quad \text{(Model S)}$$

These are the forms used throughout the theory as the operational persistence condition. They are exact for linear correction and useful proxies for mildly nonlinear correction (where $\alpha \approx \mathcal{T}$), but they overstate the persistence margin when the correction function saturates, because they omit the structural constraint ($\alpha \gt \rho/R$) that becomes binding when $R$ is finite.

**Per-dimension (Model S):** $\eta_k \gt c \cdot \rho_k^2 / \delta_{\text{critical},k}^2$ where $c$ depends on the probability guarantee. See #result-per-dimension-persistence.

### The relationship between $\alpha$ and $\mathcal{T}$

#der-gain-sector-bridge shows that for agents with directional fidelity, $\alpha = \eta^\ast \cdot c_{\min}$ where $c_{\min}$ is the worst-case directional fidelity. For linear correction (Kalman, Beta-Bernoulli), $\alpha = \mathcal{T}$ exactly. For gradient descent on strongly convex losses, $\alpha = \eta \cdot \mu$ where $\mu$ is the strong convexity modulus — monotone in $\eta$ (and hence in $\mathcal{T}$) for fixed loss landscape. For nonlinear correction tested in simulation (saturating, sigmoid, threshold), $\alpha$ remains monotone increasing in $\mathcal{T}$: for a saturating function with capacity $R$, $\alpha \approx \mathcal{T}/2$ (worst case at the capacity boundary); for sigmoid (tanh), $\alpha \approx 0.76 \cdot \mathcal{T}$. The qualitative conclusion — "faster adaptation improves persistence" — is structurally grounded for the important cases and empirically confirmed for all correction function classes tested.

### Per-Dimension Extension

*[Empirical Claim (per-dimension-persistence, from simulation variant F)]*

For anisotropic systems (non-uniform $\rho$ or $\mathcal{T}$ across dimensions), the scalar persistence condition is insufficient. Per-dimension:

$$\mathcal{T}_k \gt \frac{\rho_k}{\delta_{\text{critical},k}} \quad \text{for each dimension } k$$

The scalar condition overestimates by up to 72% in simulation. The weak dimension is the bottleneck (84% of total mismatch in simulation). See #result-per-dimension-persistence.

**Robustness**: The per-dimension condition matches discrete AR(1) prediction to 4 significant figures. The scalar overestimate is a consequence of Jensen's inequality applied to the norm.

## Epistemic Status

**Structural persistence** thresholds are *exact* under their stated assumptions: Model D gives $\alpha \gt \rho/R$ (Prop A.1, exact under GA-2, GA-3); Model S gives $\alpha \gt n\sigma_w^2/(2R^2)$ (Prop A.1S, exact under GA-2S, GA-3). The threshold's *existence* is *robust qualitative* — any monotone correction function has a capacity limit; this holds across all correction functions tested.

**Task adequacy** ($R^\ast \lt \lVert\delta_{\text{critical}}\rVert$) is *exact as a definition* — given $R^\ast$ (derived) and $\lVert\delta_{\text{critical}}\rVert$ (domain parameter), the comparison is well-defined. The substance lies in estimating $\lVert\delta_{\text{critical}}\rVert$ for specific domains, which is an operationalization question ( #detail-operationalization), not a theory question.

**The linear operational forms** ($\mathcal{T} \gt \rho/\lVert\delta_{\text{critical}}\rVert$ for Model D; $\mathcal{T} \gt n\sigma_w^2/(2\lVert\delta_{\text{critical}}\rVert^2)$ for Model S) are *exact* for linear correction (where they express task adequacy alone, structural persistence being trivially satisfied) and *useful approximations* for mildly nonlinear correction (where $\alpha \approx \mathcal{T}$). For strongly nonlinear correction, the general $\alpha$-forms are required and BOTH structural and task-adequacy conditions must be checked. Downstream segments that use the linear operational forms should be understood as expressing task adequacy, not structural stability.

The per-dimension extension is *empirically exact* for Model S (matches AR(1) prediction to 4 significant figures in simulation); the Model D per-dimension threshold ($\mathcal{T}_k \gt \rho_k/\delta_{\text{critical},k}$) is exact by the same Lyapunov argument applied per dimension.

## Discussion

**Two conditions, not one.** This segment now separates what was previously conflated. Structural persistence ($\alpha \gt \rho/R$) is the Lyapunov-derived result — it says the machinery *works*. Task adequacy ($R^\ast \lt \lVert\delta_{\text{critical}}\rVert$) is a domain-specific constraint — it says the machinery works *well enough*. Neither implies the other, and downstream segments should specify which they mean. Most adversarial-dynamics results ( #result-adversarial-tempo-advantage, #der-adversarial-destabilization) depend on structural persistence. Most domain instantiations (TST, logogenic agent design) care about task adequacy. See Persistence in `LEXICON.md` and `README.md` for the full three-sense taxonomy (structural, operational, continuity).

**Below structural threshold.** When $\alpha \leq \rho / R$, mismatch is not merely large — it grows without effective bound (up to $R$, the sector-condition region). The correction machinery is overwhelmed. This is a qualitative transition, not a gradual degradation.

**Below task-adequacy threshold.** When $R^\ast \gt \lVert\delta_{\text{critical}}\rVert$ but $R^\ast \lt R$, the system is structurally stable but performing unacceptably. Mismatch is bounded but too large for the domain. The remedy is different from structural failure: increase $\mathcal{T}$ (faster or better correction), decrease $\rho$ (reduce environmental volatility), or relax $\lVert\delta_{\text{critical}}\rVert$ (accept more mismatch). Structural failure requires changing the correction architecture entirely ( #result-structural-adaptation-necessity).

**$\delta_{\text{critical}}$ and $R$ are domain parameters, not theory outputs.** The theory derives the *existence* of persistence thresholds and their *form* (ratio of correction to disturbance). But the specific values are set by the application domain: $\delta_{\text{critical}}$ encodes "how wrong can the model be before the agent's actions become harmful or ineffective?" — this depends on the stakes, the action space, and the environment's forgiveness. $R$ encodes "how large a mismatch can the correction function handle before it saturates or breaks down?" — this depends on the model class and the correction architecture. See #detail-operationalization for guidance on estimating these quantities in specific domains.

**Channel independence and scalar tempo.** The linear operational forms use scalar $\mathcal{T}$, which inherits the channel-independence assumption from #def-adaptive-tempo: the additive formula overcounts when observation channels are correlated. In anisotropic systems the scalar condition also overestimates margins — up to 72% in simulation (see #def-adaptive-tempo, scalar vs. vector tempo). Where precision matters, the per-dimension condition ($\mathcal{T}_k \gt \rho_k / \delta_{\text{critical},k}$) should be used instead — and under cross-dimensional correction (off-diagonal $\mathcal{T}$ in the coordinate basis of $D_\delta = \mathrm{diag}(\delta_{\text{critical},k}^2)$), the matrix-Loewner form $\Sigma_\infty \prec D_\delta$ ( #deriv-matrix-persistence-condition) is canonical: per-coordinate is unsafe in that regime (gives a false-pass on persistence), while matrix-Loewner reads persistence correctly off the worst direction whether or not it aligns with a coordinate axis.

**Adaptive reserve.** The quantity $\Delta\rho^\ast = \alpha R - \rho$ (Prop A.2) measures how much additional disturbance the agent can absorb before persistence fails. Positive reserve means the agent has margin; zero reserve means it is at the threshold.

**Persistence has a cost, not just a threshold.** The inequality above says mismatch is bounded; it does not say what rate of effort the agent expends to hold that bound. #deriv-persistence-cost establishes the complementary *information-rate* bound: under Model S with Gaussian-OU signal, the sustained Shannon information rate the agent must acquire from observations to maintain the ultimate bound satisfies $\dot R \geq n\alpha/2$ nats/time — a Landauer-analog floor that Kalman-Bucy saturates. The corollary is a channel-capacity prerequisite $C \geq \mathcal{T}/2$ that the threshold condition alone does not name. Two agents with identical persistence guarantees can face wildly different sustained demands because the cost scales linearly with $\alpha$; the threshold alone cannot distinguish dormant from running-hot.

### Connections

The persistence condition appears in multiple downstream contexts:

- **Adversarial dynamics** ( #result-adversarial-tempo-advantage): Superlinear tempo advantage arises because persistence is a threshold — pushing an adversary below it causes qualitative collapse. *This connection is developed and validated in #result-adversarial-tempo-advantage and simulation variants A-D.*

- **Structural adaptation** ( #result-structural-adaptation-necessity): When model class fitness $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$, the effective $\alpha$ in the sector condition shrinks, eventually violating persistence. *This connection is developed in #result-structural-adaptation-necessity.*

- **Software maintainability** ( #der-code-quality-as-observation-infrastructure — cross-component reference, see `02-tst-core/`): *[Discussion]* A codebase may become "unmaintainable" when the development team's adaptive tempo falls below the rate of complexity accumulation. The vicious cycle would then be the persistence condition being violated through the agent's own prior actions degrading future $\mathcal{T}$ via $U_o$. *This connection is structurally motivated but not yet formally derived within AAT. It requires formalizing "complexity accumulation rate" as an instance of $\rho$.*

## Findings

### The Persistence Condition with Structural / Task-Adequacy Decomposition

**Brief:** An adaptive system persists when its correction speed beats the rate at which its world is changing, relative to how forgiving the world is. Below this threshold the system doesn't merely degrade — it loses bounded behavior, the way a balance held just barely beneath a tipping point is qualitatively different from one well above it. The same inequality, with different inputs, governs whether a Kalman filter tracks a moving target, whether a development team keeps a codebase maintainable, and whether an organization keeps up with strategic change. The threshold itself decomposes into two distinct conditions — *structural persistence* (the machinery's correction rate can outpace disturbance) and *task adequacy* (the resulting steady-state mismatch is small enough for what the agent is trying to do). Conflating the two leads to category errors in domain transfer.

**Impact:** This is the framework's central inequality and the load-bearing connection between control-theoretic Lyapunov stability analysis and the broader question of when any adaptive system — thermostat, software team, immune system, RL agent — can maintain coherent function under change. The two-condition decomposition is itself non-obvious and consequential: prior work that conflated "the machinery works" with "the machinery works well enough" produced category errors in domain transfer (a structurally persistent codebase team can be task-inadequate; the remedies differ). The complementary information-rate bound from `#deriv-persistence-cost` ($\dot R \geq n\alpha/2$) shows the threshold has a sustained-cost shadow: two agents with identical persistence guarantees can face wildly different sustained demands.

**Novelty Claim:** *Claim synthesis* on Lyapunov stability theory, sector-bounded nonlinear correction, and adaptive-tempo information-rate accounting, applied uniformly across single-agent classes that range from Kalman filtering through saturating nonlinear correction through PID control. The Lyapunov machinery itself is standard; the synthesis is its use as the central inequality of an integrated agent theory, with the two-condition decomposition (structural / task-adequacy) as the AAT-internal contribution that cleanly separates "the machinery works" from "the machinery works well enough."

**Related Work:**

- Khalil 2002, *Nonlinear Systems* (3rd ed.), Prentice Hall (published 2002, found pre-2026) — *formal antecedent* — chapters 4 and 9 supply the converse Lyapunov, ultimate boundedness, and sector-condition machinery the segment uses. Standard control-theoretic apparatus.
- Lyapunov 1892 / Khasminskii 2012 *Stochastic Stability of Differential Equations* — *formal antecedent* — the underlying Lyapunov stability tradition; Khasminskii's stopping-time localization underpins the Model S derivation.
- Rockafellar & Wets 1998, *Variational Analysis* — *formal antecedent* — supplies the monotone-operator machinery that underwrites the sector condition's strong-convexity equivalents.
- Wiener 1948 *Cybernetics*; Ashby 1956 *Introduction to Cybernetics*; Conant & Ashby 1970 — *conceptual precursor* — the cybernetic-feedback tradition that frames the "correction must outpace disturbance" intuition without supplying the quantitative inequality.

**Search Log:**
- 2026-04 (*intuition-only* on broader prior-art): no targeted Undermind-grade search has been conducted on the persistence-condition-as-central-inequality positioning. Pre-search expectation: the Lyapunov-based stability machinery is standard; the AAT-distinctive content is the two-condition decomposition (structural vs task adequacy) and its uniform application across agent classes. A targeted search would query the bounded-rationality / control-theoretic decision-making literature (Ortega-Braun line; Genewein et al.) for prior decompositions of "stability vs adequacy" in adaptive-control settings, and the active-inference literature for the same distinction.
- 2025 (*targeted*): Khalil 2002 / Khasminskii 2012 / Rockafellar-Wets 1998 confirmed as the formal antecedents for the sector-Lyapunov machinery; the segment cites them inline.
