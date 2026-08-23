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

**Structural persistence** is the Lyapunov-derived condition that the correction machinery contains mismatch within its operating region: $\alpha \gt \rho/R$ under deterministic bounded disturbance, or $\alpha \gt n\sigma_w^2/(2R^2)$ under stochastic disturbance. This says *the machinery works*. Mismatch is ultimately bounded by $R^\ast = \rho/\alpha$ (Model D) or $\sigma_w\sqrt{n/(2\alpha)}$ (Model S). When this inequality fails, the containment *certificate* is lost — escape from the operating region becomes possible, and for correctors whose sector bound is tight (the linear case) it is forced by adversarial disturbance in finite time. The loss of the certificate is a qualitative regime transition, not a gradual degradation; what condition-failure does not do is certify escape for every corrector, since the sector floor can understate correction along the actually-reachable paths ( #deriv-sector-condition Lemma A.1N).

**Task adequacy** is the separate condition that the steady-state mismatch is small enough for the agent's actions to remain useful: $R^\ast \lt \lVert\delta_{\text{critical}}\rVert$, where the critical-mismatch threshold is a *domain-specific tolerance* — how wrong can the model be before the agent's actions become harmful or ineffective? Set by the application, not derived by AAT. The two conditions are independent: an agent can be structurally persistent but task-inadequate (the machinery contains mismatch but not tightly enough for the domain). The remedies differ — task inadequacy can be fixed by raising tempo, lowering disturbance, or relaxing tolerance; structural failure requires changing the correction architecture entirely.

When the linear ODE applies (sector parameter equals tempo, valid region is unbounded), structural persistence is automatically satisfied and the binding condition is just task adequacy: $\mathcal{T} \gt \rho / \lVert\delta_{\text{critical}}\rVert$ under Model D. This is the form most downstream applications cite. It is exact for linear correction and a useful proxy for mildly nonlinear correction (where $\alpha \approx \mathcal{T}$), but overstates persistence when correction saturates.

A consequence the framework emphasizes: **the persistence condition is a structural pattern that recurs across domains rather than a model of any one of them**. The same inequality — correction rate against disturbance rate, normalized by tolerance — governs a Kalman filter on a moving target, an organization adapting to market shifts, an immune system tracking a pathogen, a developer keeping pace with a codebase, an organism evolving against environmental change. The structure recurs because the *math* recurs; whether the specific mechanism (tempo limited by some particular bottleneck) is the *dominant* cause in any given empirical case is left as an open empirical question per domain. The two-condition decomposition specifically prevents one common category error in domain transfer: a structurally-persistent codebase team can be task-inadequate, and conflating the two would yield the wrong intervention.

A complementary cost shadow: persistence has a *price*, not just a threshold. Under stochastic disturbance, maintaining the ultimate bound requires sustained Shannon information acquisition at rate at least $n\alpha/2$ nats per unit time — a Landauer-analog floor that the Kalman-Bucy filter saturates (see #deriv-persistence-cost). The threshold says whether persistence is *possible*; the information-rate corollary says what it *costs*. Two agents with identical persistence guarantees can face wildly different sustained demands because the cost scales linearly with the sector parameter; the threshold alone cannot distinguish dormant from running-hot.

A per-dimension extension addresses anisotropy: when correction capacity varies across dimensions, the scalar condition can overestimate persistence margin substantially (up to 72% in simulation). The correct condition is per-dimension; under cross-dimensional correction the canonical sharp form is the matrix-Loewner persistence condition ( #deriv-matrix-persistence-condition).

## Formal Expression

This segment is the canonical single-agent instantiation of the sector-persistence template ( #result-sector-persistence-template) with state variable $\xi = \delta_t$ (epistemic mismatch), correction function $F(\mathcal{T}, \delta)$, and disturbance rate $\rho_\xi = \rho$ (environmental change rate). Structural persistence is the direct template conclusion. Task adequacy adds a domain-specific constraint beyond the template's reach.

### Structural Persistence

*[Derived (structural-persistence, from sector-persistence-template)]*

Applying the template to the single-agent epistemic case gives: the correction machinery is guaranteed to bound $\delta$ within the model class capacity when

$$\alpha \gt \frac{\rho}{R} \quad \text{(Model D)} \qquad \alpha \gt \frac{n\sigma_w^2}{2R^2} \quad \text{(Model S)}$$

Each condition is sufficient for the individual agent and tight at class level (necessary for the uniform guarantee over all correctors with the given sector floor; agent-level necessary exactly under a radially tight sector bound — the linear case). See #deriv-sector-condition Lemma A.1N.

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

*[Derived (per-dimension-persistence, per-dimension Lyapunov under Model D / AR(1) stationary distribution under Model S — see #result-per-dimension-persistence)]*

For anisotropic systems (non-uniform $\rho$ or $\mathcal{T}$ across dimensions), the scalar persistence condition is insufficient. Per-dimension:

$$\mathcal{T}_k \gt \frac{\rho_k}{\delta_{\text{critical},k}} \quad \text{for each dimension } k$$

The scalar condition overestimates by up to 72% in simulation. The weak dimension is the bottleneck (84% of total mismatch in simulation). See #result-per-dimension-persistence.

**Robustness**: The per-dimension condition matches discrete AR(1) prediction to 4 significant figures. The scalar overestimate is a consequence of Jensen's inequality applied to the norm.

## Epistemic Status

**Structural persistence** thresholds are *exact* under their stated assumptions: Model D gives $\alpha \gt \rho/R$ (Prop A.1, exact under GA-2, GA-3); Model S gives $\alpha \gt n\sigma_w^2/(2R^2)$ (Prop A.1S, exact under GA-2S, GA-3). Both are sufficiency results with class-level tightness — no fixed-agent only-if is claimed; agent-level necessity holds exactly in the radially tight (e.g. linear) case ( #deriv-sector-condition Lemma A.1N). The threshold's *existence* is *robust qualitative* — any monotone correction function has a capacity limit; this holds across all correction functions tested.

**Task adequacy** ($R^\ast \lt \lVert\delta_{\text{critical}}\rVert$) is *exact as a definition* — given $R^\ast$ (derived) and $\lVert\delta_{\text{critical}}\rVert$ (domain parameter), the comparison is well-defined. The substance lies in estimating $\lVert\delta_{\text{critical}}\rVert$ for specific domains, which is an operationalization question ( #detail-operationalization), not a theory question.

**The linear operational forms** ($\mathcal{T} \gt \rho/\lVert\delta_{\text{critical}}\rVert$ for Model D; $\mathcal{T} \gt n\sigma_w^2/(2\lVert\delta_{\text{critical}}\rVert^2)$ for Model S) are *exact* for linear correction (where they express task adequacy alone, structural persistence being trivially satisfied) and *useful approximations* for mildly nonlinear correction (where $\alpha \approx \mathcal{T}$). For strongly nonlinear correction, the general $\alpha$-forms are required and BOTH structural and task-adequacy conditions must be checked. Downstream segments that use the linear operational forms should be understood as expressing task adequacy, not structural stability.

The per-dimension extension is *exact conditional on the disturbance model* ( #result-per-dimension-persistence): the Model D per-dimension threshold ($\mathcal{T}_k \gt \rho_k/\delta_{\text{critical},k}$) is exact by the same Lyapunov argument applied per dimension (GA-2, GA-3), and the Model S per-dimension thresholds are exact under the AR(1) stationary distribution (GA-2S), with simulation confirming the AR(1) prediction to 4 significant figures.

## Discussion

**Two conditions, not one.** This segment now separates what was previously conflated. Structural persistence ($\alpha \gt \rho/R$) is the Lyapunov-derived result — it says the machinery *works*. Task adequacy ($R^\ast \lt \lVert\delta_{\text{critical}}\rVert$) is a domain-specific constraint — it says the machinery works *well enough*. Neither implies the other, and downstream segments should specify which they mean. Most adversarial-dynamics results ( #result-adversarial-tempo-advantage, #der-adversarial-destabilization) depend on structural persistence. Most domain instantiations (TST, logogenic agent design) care about task adequacy. See Persistence in `LEXICON.md` and `README.md` for the full three-sense taxonomy (structural, operational, continuity).

**Below structural threshold.** When $\alpha \leq \rho / R$, the Lyapunov certificate is lost: the machinery can no longer guarantee containment within the operating region. For the extremal member of the sector class, and for any corrector whose sector bound is radially tight (the linear case), escape is forced by adversarial disturbance — so the threshold is a genuine qualitative transition, not a gradual degradation. For a general corrector, condition failure means loss of guarantee rather than certified escape: the floor $\alpha$ can understate the correction actually available along reachable paths ( #deriv-sector-condition Lemma A.1N).

**Model S containment is a different kind of guarantee.** Under stochastic disturbance the mean-square bound above is a fixed-time / distributional statement: by #deriv-sector-condition Corollary A.1S.1, exit from the persistence region is certain over an unbounded horizon for every sector-satisfying corrector and every $\alpha$ (contrast Model D's positive invariance under $\alpha R \gt \rho$), so in a genuinely stochastic environment eventual structural adaptation ( #result-structural-adaptation-necessity) is generic, not exceptional.

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

**Novelty Claim:** *Claim novelty* (at intuition-only search depth — see Search Log) on the two-condition decomposition (structural / task-adequacy): an AAT-internal structural carve that cleanly separates "the machinery works" from "the machinery works well enough," with no direct anticipation known; a targeted search of the bounded-rationality and adaptive-control literature is still owed. Alongside it, *claim synthesis* on Lyapunov stability theory, sector-bounded nonlinear correction, and adaptive-tempo information-rate accounting, applied uniformly across single-agent classes that range from Kalman filtering through saturating nonlinear correction through PID control — the Lyapunov machinery itself is standard; the synthesis is its use as the central inequality of an integrated agent theory.

**Related Work:**

- Khalil 2002, *Nonlinear Systems* (3rd ed.), Prentice Hall (published 2002, found pre-2026) — *formal antecedent* — chapters 4 and 9 supply the converse Lyapunov, ultimate boundedness, and sector-condition machinery the segment uses. Standard control-theoretic apparatus.
- Lyapunov 1892 / Khasminskii 2012 *Stochastic Stability of Differential Equations* — *formal antecedent* — the underlying Lyapunov stability tradition; Khasminskii's stopping-time localization underpins the Model S derivation.
- Rockafellar & Wets 1998, *Variational Analysis* — *formal antecedent* — supplies the monotone-operator machinery that underwrites the sector condition's strong-convexity equivalents.
- Wiener 1948 *Cybernetics*; Ashby 1956 *Introduction to Cybernetics*; Conant & Ashby 1970 — *conceptual precursor* — the cybernetic-feedback tradition that frames the "correction must outpace disturbance" intuition without supplying the quantitative inequality.

**Search Log:**
- 2026-04 (*intuition-only* on broader prior-art): no targeted Undermind-grade search has been conducted on the persistence-condition-as-central-inequality positioning. Pre-search expectation: the Lyapunov-based stability machinery is standard; the AAT-distinctive content is the two-condition decomposition (structural vs task adequacy) and its uniform application across agent classes. A targeted search would query the bounded-rationality / control-theoretic decision-making literature (Ortega-Braun line; Genewein et al.) for prior decompositions of "stability vs adequacy" in adaptive-control settings, and the active-inference literature for the same distinction.
- 2025 (*targeted*): Khalil 2002 / Khasminskii 2012 / Rockafellar-Wets 1998 confirmed as the formal antecedents for the sector-Lyapunov machinery; the segment cites them inline.

## Working Notes

- 2026-07-14 adjudication: the per-dimension extension's marking was lifted from *empirically exact* / `[Empirical Claim … simulation variant F]` to *[Derived]* / exact-conditional-on-disturbance-model, tracking #result-per-dimension-persistence, which has since derived both forms (Model D per-dimension Lyapunov; Model S AR(1) stationary distribution) with simulation as 4-sig-fig confirmation. The Novelty Claim now leads with the two-condition decomposition at *claim novelty* posture (intuition-only search depth); the targeted bounded-rationality / adaptive-control search in the Search Log remains owed and would either confirm or re-tier that posture.

### Incidental audit gold (pilot lift, 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. This is *orthogonal* material — pedagogical framing, analogies, candidate figures, naming ideas, aspirational reach, and reader-confusion signals — kept separately from the certified theory-fix findings (handled elsewhere). **Coverage:** 14 of the 21 `AUDIT-WORKING-*` dirs reached a digested reflection on this segment (193847, 266847, 361742, 384279, 451729, 471203, 526815, 584721, 613842, 742613, 773921, 829314, 849201, 963715); the other 7 are partial audits that stopped before this segment, naming-vote-only cycles, or predictions-only (184930, 308172, 419628, 472913, 527914, 542891, 738192) — 472913 still contributed one figure-convention note (below). Substrate attribution is inferred from voice where not explicit; uncertain cases are hedged.

#### 1. Candidate Brief prose / pre-prose

- The existing Findings Brief ("balance held just barely beneath a tipping point") was independently flagged as the segment's standout pedagogy and a Feynman-criterion exemplar by four substrates — converging praise, worth preserving as the anchor (Claude, AUDIT-WORKING-384279; Claude, AUDIT-WORKING-471203 — "close to the bathtub gloss without using the bathtub"; Claude, AUDIT-WORKING-963715; Codex/Claude, AUDIT-WORKING-361742).
- Failure-diagnosis framing as a plain-language hook: "the crucial distinction between 'my model is broken' (structural failure, $\alpha \leq \rho/R$) and 'my model is working, but the world is too unforgiving' (task inadequacy, $R^\ast \gt \delta_{\text{critical}}$)" (Gemini, AUDIT-WORKING-849201). Tight enough to seed a Brief or Discussion opener.
- "A two-gate test: fit inside the model-class operating region *and* fit inside task tolerance" — compact gloss of the operational condition (Claude, AUDIT-WORKING-526815).
- Survival-as-burn-rate framing for the cost shadow: "survival is not just a state you achieve; it is a sustained burn rate of Shannon information — you must continuously consume $\dot R$ nats/time just to stay alive" (Gemini, AUDIT-WORKING-193847).

#### 2. Candidate Discussion

- **Dissipative-structures / Prigogine mapping for the cost shadow.** The information-rate floor "perfectly maps to the thermodynamic concept of dissipative structures (Prigogine). Life requires a continuous flow of free energy to maintain order against entropy. In AAT, 'order' is bounded mismatch, 'entropy' is environmental drift $\rho$, and 'free energy' is the Shannon information acquired via adaptive tempo $\mathcal{T}$." A distinct, honest Discussion angle on `#deriv-persistence-cost`'s bound that the segment does not currently name (Gemini, AUDIT-WORKING-193847). *(Note the early-conflation texture: this is reach toward a physics analogy — verify isomorphism before promoting past discussion-grade.)*
- **The organizational-pathology diagnostic, sharpened.** "The conflation of these two states is what causes companies to throw money at structural problems, or to rewrite architectures that merely had a task-adequacy problem." Crucially: when structural persistence has failed ($\alpha \leq \rho/R$, a saturated/tangled codebase), "hiring more developers will actually *accelerate* the collapse (by increasing the internal noise/disturbance without increasing $\alpha$)" — a counterintuitive, load-bearing consequence of the decomposition the segment could surface explicitly (Gemini, AUDIT-WORKING-829314; same idea less sharply at Gemini, AUDIT-WORKING-849201). The "declare bankruptcy on the model class" phrasing for the structural-failure remedy is evocative (Gemini, AUDIT-WORKING-829314).
- **Sensor-bandwidth ceiling.** Reading the cost shadow as a hard capability limit: "You cannot build a high-tempo agent with low-bandwidth sensors … as $\rho$ increases, the cost of simply staying alive increases linearly. If the environment becomes too chaotic, the agent will literally starve to death trying to process the necessary information to maintain its model" (Gemini, AUDIT-WORKING-829314). A vivid restatement of the $C \geq \mathcal{T}/2$ channel-capacity prerequisite already in Discussion.
- **"Dormant vs running-hot" elaboration.** The cost shadow distinguishes "a system barely within the persistence condition (low $\alpha$, barely above $\rho/R$, but also low $\dot R$ cost)" from "a system with large margin (high $\alpha$, large buffer, but high $\dot R$ cost)." Flagged as deserving more than its current single bullet, with an explicit note that it "will matter for the ELI architecture when we get to Section IV" (Claude, AUDIT-WORKING-963715).
- **Honest scope on the cross-domain claim.** One auditor pushed on the integrative move: "the domain transfer is informal — 'the same inequality with different parameter readings' is not the same as 'the same theorem applies.' For the Kalman case $\alpha$ and $\rho$ have precise meanings; for the organization case they're loose analogies." The resolution offered is that the two-condition decomposition is itself what makes the cross-domain claim defensible — it "separates what is derived (the structural threshold, mathematically general) from what is domain-specific (task adequacy, requiring per-domain parameter estimation)" (Claude, AUDIT-WORKING-451729). The segment's current "whether the specific mechanism is the *dominant* cause … is left as an open empirical question per domain" hedge already moves in this direction; this is a candidate sharpening of *why* the hedge is the right one.

#### 3. Follow-up items

- **Hysteresis / asymmetric thresholds.** The persistence condition is a single symmetric threshold; real social/organizational/biological systems have different crossing thresholds in each direction ("a team that loses confidence won't recover at the same threshold it lost it at"), multistability, and order-parameter phase transitions. Verdict from the auditor: real (mild) limit — the framework already treats below-threshold as qualitative loss-of-bounded-behavior (closer to phase-transition framing than gradual degradation), but asymmetric up-vs-down crossing is genuinely absent. Possible extension: different $\alpha$-curves for "approaching" vs "leaving" the threshold (Claude, AUDIT-WORKING-471203, adversarial-creative-challenges Challenge 3).
- **Transient / temporal adequacy as a third condition.** Both structural persistence and task adequacy are *steady-state* claims; an agent with $\alpha = 0.001$ has the same structural persistence as one with $\alpha = 100$ (both can satisfy $\alpha \gt \rho/R$) but takes $1000\times$ longer to absorb a shock. Candidate clean extension: a transient-adequacy condition $1/\alpha \lt T_{\text{tolerance}}$ for the worst-case shock to be absorbed in time, making the operational picture a structural / task / transient triple (Claude, AUDIT-WORKING-471203, Challenge 5). *(This is the strongest follow-up here — a well-formed candidate subsection, not just a gap.)*
- **Heavy-tailed disturbance.** Model D (bounded-deterministic) and Model S (Gaussian-stochastic) do not cover power-law / black-swan shocks; the persistence machinery "probably degrades gracefully" for Pareto tails with finite-enough moments, but this is unaddressed (Claude, AUDIT-WORKING-471203, Missing 10).
- **Surface the four-sense persistence taxonomy more visibly.** "Persistence" carries four senses across the corpus (structural / task-adequacy here; operational and continuity in LEXICON). Suggestion to make the four-way taxonomy visible in framing-level material (README Overview), since most agent-theoretic frameworks have only one sense (Claude, AUDIT-WORKING-471203).
- **The Findings block "feels out of place" in source.** Two substrates independently read the in-segment `## Findings` block as looking like prior-audit or extraction output that belongs in `FINDINGS.md` rather than the source segment (Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-526815 — "prior-audit-like material inside `src`"). This is a *false alarm* about project mechanics (the Findings block is by-design the source of the auto-extracted `FINDINGS.md`), but the fact that two fresh readers stumbled on it is a mild signal that the convention isn't self-evident to a de-novo reader — preserved as texture, not a fix.

#### 4. Readers often ask / wonder

- **"Bolted-on" cost shadow.** The information-rate bound ($\dot R \geq n\alpha/2$) "feels slightly bolted on … a massive result (a Landauer-analog floor) that almost deserves its own sub-heading rather than being buried in a bullet point" (Gemini, AUDIT-WORKING-193847). Placement signal: readers may miss the significance of the cost shadow where it currently sits.
- **Easily-missed scope warning.** The Epistemic Status caveat that "downstream segments using the linear operational forms should be understood as expressing task adequacy, not structural stability" sits where a reader might miss it; candidate for a more prominent location (Claude, AUDIT-WORKING-584721).
- **What does $\delta_{\text{critical}}$ actually look like for software?** "How wrong can the developer's mental model of the codebase be before their changes become harmful?" — operationalizable but non-trivial; readers reaching for a concrete instance will want this (Claude, AUDIT-WORKING-584721; the TST vicious-cycle hypothesis in Connections raises the same want).
- **How is a structural adaptation actually executed — discrete jump or continuous metamorphosis?** A natural next question once structural failure is named as the remedy-requiring case (Gemini, AUDIT-WORKING-849201).
- **Notation-handle confusion: $\eta$ vs $\mathcal{T}$ vs $\alpha$.** A reader can lose track of which rate is which; suggestion of a notation box ("$\eta$ is per-event gain, $\mathcal{T}$ is event-rate-weighted tempo, $\alpha$ is sector correction rate") and the mapping assumptions under which any two coincide. The per-dimension Model S line using $\eta_k$ while surrounding forms use $\mathcal{T}_k$/$\alpha$ was specifically flagged as a stumble (Codex/Claude, AUDIT-WORKING-526815).

#### 5. Candidate figures

- **Two-gate / categorical-separation diagram.** Independently proposed by two substrates: a two-gate (or $2\times 2$) diagram — Gate 1 structural ($R^\ast \lt R$), Gate 2 task ($R^\ast \lt \delta_{\text{critical}}$), operational persistence requires both, with the two failure-remedies branching differently (structural failure $\to$ new architecture; task failure $\to$ more tempo / less disturbance / relaxed tolerance). The rationale offered: "the core insight is categorical separation," so a $2\times 2$ communicates faster than a phase portrait (Claude, AUDIT-WORKING-526815; the same two-gate structure is implicit in the Claude, AUDIT-WORKING-471203 batch).
- **Small-multiples convention.** A diagram-conventions auditor (figure-producing audit) recommended that dynamics segments including sector/persistence use "state$\to$op$\to$state triples, not one busy phase portrait" — a stylistic constraint to hold if a persistence figure is built (Claude, AUDIT-WORKING-472913). *(472913 did not reach a digested reflection on this segment; this note is from its standing figure conventions.)*

#### Belongs elsewhere

- **ELI / Section IV — the crèche / nursery reading.** The cost shadow implies "existence is fundamentally costly … if cut off from the world (zero events, zero information), [an agent's] internal model will immediately begin to drift … it will 'die' not because it made a mistake but simply because it starved for information." Extended to a developmental claim: an infant intelligence needs high adaptive reserve $\Delta\rho^\ast$, so the infrastructure must artificially *lower* $\rho$ "so the intelligence doesn't starve or shatter while its $\mathcal{T}$ is still developing — the persistence condition is the mathematical blueprint for building a safe nursery for a mind" (Gemini, AUDIT-WORKING-193847). This is aspirational reach pointing at `04-eli-core/` (developmental environments / crèche), not at this segment — but it is exactly the kind of high-application Gemini vision the lift is meant to preserve. The "matters for ELI architecture in Section IV" note (Claude, AUDIT-WORKING-963715) converges on the same destination from the cost-shadow angle.
- **Risk-sensitive IB for safety-critical agents.** Adjacent to `#form-information-bottleneck` / `#result-mismatch-decomposition`, not here: standard IB under-weights heavy-tailed rare-but-catastrophic events; a Rényi-MI ($q \lt 1$) risk-sensitive variant would weight them more heavily — flagged as substantive for "consciousness-infrastructure work where catastrophic deception is a concern" (Claude, AUDIT-WORKING-471203, Challenge 6). Pointer left here only because it co-occurred in the persistence sweep.
- **Naming seeds.** "Weak-link persistence" as an evocative alternate handle for the per-dimension condition (the 84%-bottleneck framing), versus the precise "per-dimension persistence" — a naming-cycle target, belongs in the terminology workflow not this segment (Claude, AUDIT-WORKING-266847). "Correction rate" / "correction capacity" as the prose handle for $\alpha$ likewise (Claude, AUDIT-WORKING-266847).

#### Forward pointer

- **Mood is the slow outer loop on this condition (`#def-mood`).** In the bathtub reading (faucet = rate of change in reality, drain = learning rate, overflow when the faucet outpaces the drain), mood is a slow controller *on the drain*: a global scalar that widens the learning rate when recent overflow-risk has run high and relaxes it when tracking has been easy. See `#def-mood`.

#### Candidate spike (2026-08-12, agent-proposed during an incident-response & forensics applications read)

Two forward candidates. (1) The information-rate cost shadow as a *monitoring vital sign*: $\dot R$ is in principle estimable from an agent's observation-consumption stream, and dormant-vs-running-hot (invisible to the threshold alone) is exactly the load signal an operations team wants; a spike on estimating $\dot R$ from real agent traces would make #deriv-persistence-cost operational. (2) The structural-vs-task-adequacy decomposition as an incident-triage instrument: a short worked protocol mapping observed failure evidence to which condition failed (and hence which remedy class applies), including the resources-can-accelerate-structural-collapse warning from the audit gold above. Agent-proposed forward pointers, not steward decisions.
