---
slug: der-interaction-channel-classification
type: derived
status: conditional
depends:
  - def-observation-function
  - def-mismatch-signal
  - result-mismatch-decomposition
  - emp-update-gain
  - def-adaptive-tempo
  - def-model-class-fitness
  - result-structural-adaptation-necessity
  - result-persistence-condition
  - result-sector-persistence-template
  - der-adversarial-destabilization
  - der-directed-separation
  - disc-credit-assignment-boundary
stage: draft
---

# Derived: Interaction-Channel Classification (Recipient-Side)

The same signal from agent $A$ lands on recipient $B$ as one of four qualitatively different things — informative update, magnitude-shock, structural-shock, or ambient noise — determined by three independent boundary conditions stated entirely in $B$'s existing AAT quantities. The emitter-side collapse of this variation into a scalar $\gamma_A \mathcal T_A$ loses information that is load-bearing: the recipient's repair path depends on which regime the event falls into, and "more tempo" vs "different model class" address structurally different failure modes. This is the **anti-collapse** discipline ( #disc-anti-collapse) at the composition layer — the scalar collapse hides exactly the regime distinction that routes to opposite repairs.

Two event-level quantities enter the classification and *must not be conflated*: the **magnitude** of the event in $B$'s observation space (how large a perturbation it produces in mismatch on arrival), and the **information content** of the event conditional on $B$'s prior. A large-magnitude already-predicted event has large magnitude but small information content; a tiny-magnitude structurally novel event has small magnitude but large information content. Three independent boundaries — sector-region, model-class, observability-floor — partition events into four regimes. **Regime I (informative update)**: within sector, representable in the model class, above the observability floor — the good case. **Regime II-a (magnitude shock)**: event magnitude exceeds the sector region — too large for the correction mechanism; the repair is more bandwidth or tempo. **Regime II-b (structural shock)**: within sector but information content exceeds the model class — the class lacks representational capacity; the repair is *structural adaptation* (a different model class), and more tempo does not help. **Regime III (ambient erosion)**: below the observability floor — each event individually small enough to be processed but the cognitive overhead accumulates; the repair is *infrastructure-level filtering* before signals reach the agent.

The central methodological move: **the emitter sees a scalar; the recipient sees a regime**. Most multi-agent frameworks treat coupling as a single coefficient (the emitter-side view); the classification names what that coefficient hides — events of identical scalar magnitude can sit in any of the four regimes, with structurally different repairs. The Regime-III ambient-erosion case is the framework's structural reason that DDoS-of-low-priority-alerts is a real attack rather than just inconvenience: not because individual events are significant but because processing them consumes tempo that should go to actual work. For LLM-agent infrastructure this maps directly — push Regime-III filtering *below* the model level into wrapper or system infrastructure rather than processing every event at the model layer. The recipient-side decomposition also surfaces an adversarial move the scalar emitter formulation cannot express, treated in Discussion: *Regime-I-with-adversarial-content* — exploiting $B$'s openness to informative updates by injecting sign-chosen misinformation on the log-odds signal.

## Formal Expression

### Setup and Notation

Two purposeful agents $A$ and $B$ coupled through a shared environment. $A$'s praxis produces an event $e_\tau^A$ that enters $B$'s observation channel. On $B$'s side the event is processed by the standard AAT machinery: $h_B$ maps the $A$-induced environment state to observation $o_\tau^B$ ( #def-observation-function); mismatch is $\delta_\tau^B = o_\tau^B - \hat o_\tau^B$; update absorbs $\delta_\tau^B$ with gain $\eta_B^\ast = U_{M,B}/(U_{M,B} + U_{o,B})$ ( #emp-update-gain).

Two event-level quantities enter the classification and must not be conflated:

- $\lVert e_\tau^A\rVert_B$ — the **magnitude** of the event in $B$'s observation space (how large a perturbation it produces in $\delta_\tau^B$ on arrival).
- $\mathcal{I}(e_\tau^A)$ — the **information content** of the event conditional on $B$'s prior, formally $I(e_\tau^A; \Omega \mid M_{B,\tau^-})$ per NOTATION.md's event-information quantity. A large-magnitude already-predicted event has large $\lVert e\rVert$ but small $\mathcal{I}$; a tiny-magnitude structurally novel event has small $\lVert e\rVert$ but large $\mathcal{I}$.

Let $\mathcal{F}(\mathcal M_B)$ denote $B$'s model-class fitness ( #def-model-class-fitness), and $\mathcal I_{\max}(\mathcal M_B)$ the maximum per-event information content representable within the class (see Working Notes for the cleaner sufficient-statistics-span formulation).

### Classification Boundaries

*[Definition (regime-boundaries)]*

Event $e_\tau^A$ arriving at $B$ falls into one of four regimes, determined by three independent boundary conditions:

**Regime I (Informative update)** when all three hold:

$$\text{(I-a)} \quad \lVert e_\tau^A\rVert_B \leq R_B \qquad \text{(within sector-condition region)}$$

$$\text{(I-b)} \quad \mathcal{I}(e_\tau^A) \leq \mathcal{F}(\mathcal{M}_B) \cdot \mathcal{I}_{\max}(\mathcal{M}_B) \qquad \text{(representable within model class)}$$

$$\text{(I-c)} \quad \mathcal{I}(e_\tau^A) \cdot \nu^{(k)} \geq U_{o,B}^{(k)} \cdot c_\text{floor} \qquad \text{(above observability floor)}$$

where $k$ is the arrival channel, $\nu^{(k)}$ its event rate, and $c_\text{floor}$ a detection-theory constant controlling the false-alarm tolerance.

**Regime II-a (Magnitude-shock destabilization)** when (I-a) fails:

$$\lVert e_\tau^A\rVert_B \gt R_B$$

The event exits $B$'s sector-condition region on arrival. $B$'s correction function does not point inward strongly enough to discharge the mismatch before the next event; under sustained rate $\nu \gtrsim \alpha_B$, destabilization proceeds per #der-adversarial-destabilization.

**Regime II-b (Structural-shock destabilization)** when (I-a) holds but (I-b) fails:

$$\lVert e_\tau^A\rVert_B \leq R_B, \qquad \mathcal{I}(e_\tau^A) \gt \mathcal{F}(\mathcal{M}_B) \cdot \mathcal{I}_{\max}(\mathcal{M}_B)$$

The event's information content exceeds what $B$'s model class can represent. By #result-structural-adaptation-necessity, parametric update within $\mathcal M_B$ cannot close the mismatch; residuals retain systematic structure. Repair requires structural adaptation (a different model class), not more bandwidth.

**Regime III (Ambient noise / slow erosion)** when (I-a) and (I-b) hold but (I-c) fails:

$$\lVert e_\tau^A\rVert_B \leq R_B, \qquad \mathcal{I}(e_\tau^A) \leq \mathcal{F}(\mathcal{M}_B) \cdot \mathcal{I}_{\max}(\mathcal{M}_B), \qquad \mathcal{I}(e_\tau^A) \cdot \nu^{(k)} \lt U_{o,B}^{(k)} \cdot c_\text{floor}$$

The event is representable and within capacity but its information content sits below the observability floor. It contributes to $\delta_B$'s variance (enters Model S as part of $\sigma_{w,B}^2$) without triggering a usable update; $B$'s adaptive reserve $\Delta\rho_B^\ast$ slowly drains.

### Three Independent Boundaries

The three boundary conditions are structurally independent, each stated in quantities AAT already carries:

| Boundary | AAT quantities | Failure mode |
|---|---|---|
| (I-a) / (II-a): sector-region | $\lVert e\rVert_B$, $R_B$ (from #def-model-class-fitness / #result-sector-persistence-template) | *magnitude* — more capacity cures |
| (I-b) / (II-b): model-class | $\mathcal{I}(e)$, $\mathcal{F}(\mathcal M_B)$, $\mathcal I_{\max}(\mathcal M_B)$ | *class* — structural adaptation cures |
| (I-c) / (III): observability | $\mathcal{I}(e)$, $\nu^{(k)}_B$, $U_{o,B}^{(k)}$ (from #obs-gated-tempo-advantage) | *rate* — lower observation noise or higher event rate cures |

No new ad-hoc thresholds are introduced. $\mathcal I_{\max}(\mathcal M_B)$ is the only new symbol; see Working Notes for its cleaner sufficient-statistics-span formulation.

### Regime-Typed Disturbance Decomposition

*[Derived (regime-typed-rho-eff, from regime-boundaries + sector-persistence-template)]*

Under a stream of events $\{e_\tau^A\}$, $B$'s **regime-typed effective disturbance** rate decomposes into regime-typed contributions:

$$\rho_B^{\text{eff}} = \underbrace{\sum_{e \in \text{II-a}} \lVert e\rVert_B \cdot \nu_e}_{\text{magnitude disturbance}} \;+\; \underbrace{\text{floor}(\mathcal{M}_B) \cdot \sum_{e \in \text{II-b}} \nu_e}_{\text{structural mismatch floor}} \;+\; \underbrace{\sum_{e \in \text{III}} \sigma_e^2 \cdot \nu_e}_{\text{ambient variance}} \;-\; \underbrace{\sum_{e \in \text{I}} \iota_B(e)\,\mathcal{I}(e) \cdot \nu_e}_{\text{informative correction}}$$

The Regime-I term is **negative**: informative events reduce $B$'s effective disturbance rate, not increase it. This generalizes #der-team-persistence's cooperative-action term $-\gamma^{\text{coop}}\mathcal T_j$: a cooperative event is precisely a Regime-I event from an aligned emitter, and the sign flip in the emitter-side decomposition falls out of the regime assignment on the recipient side. Adversarial events land in Regimes II-a/II-b; ambient-noise events in Regime III.

The emitter-side formulation $\gamma_A \mathcal T_A \to \rho_B^{\text{eff}}$ compresses the regime-typed sum into a single scalar, losing (i) the sign of cooperative coupling, (ii) the magnitude vs structural distinction in destabilization, and (iii) the observability-floor loss to Regime III.

### Structured Derivation — Kalman-over-Kalman

*[Derivation (Kalman-over-Kalman, from regime-boundaries + update-gain)]*

For a concrete check, take $B$ as a Kalman filter on a scalar linear-Gaussian state with model class $\mathcal M_B = \{\theta \in [\theta_{\min}, \theta_{\max}]\}$, process noise $q$, observation noise $r$, sector parameter $\alpha_B = \eta_B^\ast = P_{\text{pred}}/(P_{\text{pred}} + r)$. $B$'s sector-region radius is $R_B = \sqrt{q/(1-\theta_{\max}^2)}$ (stationary standard deviation at the class edge).

$A$'s emitted perturbation $\xi_A$ enters $B$'s innovation as $\delta_\tau^B = \xi_A + \varepsilon_\tau + (\omega_\tau - \hat\omega_\tau)$. Four canonical distributions for $\xi_A$ partition the classification:

**Case 1 — Small-variance Gaussian $\xi_A \sim \mathcal{N}(0, s^2)$, $s^2 \ll r$ (expected Regime III).** $\mathcal{I}(\xi_A) \approx s^2/(2r \ln 2)$ nats — small. (I-a) holds ($s \ll R_B$); (I-b) holds (Gaussian-within-Gaussian); (I-c) fails because $\mathcal{I}(\xi_A) \lt U_{o,B} \cdot c_\text{floor}$. Result: Regime III. Derived consequence — the contribution to $\rho_B^{\text{eff}}$ is through $\sigma_{w,B}^2$; adaptive reserve drains by $\sum_e \eta_B^{\ast 2} s_e^2 \cdot \nu_e$.

**Case 2 — Moderate Gaussian $\xi_A \sim \mathcal{N}(\mu, s^2)$, $\mu \ll R_B$, $s^2 \sim r$ (expected Regime I).** $\mathcal{I}(\xi_A) = \tfrac{1}{2}\log(1 + (s^2 + \mu^2)/r)$ — substantial. All three (I-a)/(I-b)/(I-c) hold. Result: Regime I. Standard Kalman update; $M_B$ refines; Regime-I term contributes negatively to $\rho_B^{\text{eff}}$.

**Case 3 — Binary kick $\xi_A \in \{\pm\Delta\}$ with $\Delta \gt R_B$ (expected Regime II-a).** (I-a) fails by construction. The Kalman update $\hat x^+ = \hat x^- + \eta^\ast \Delta$ undershoots by $(1-\eta^\ast)\Delta$ per event. If events arrive at rate $\nu \gtrsim \alpha_B$, lag accumulates and $\alpha_B R_B \gt \rho_B^{\text{eff}}$ is violated. Result: Regime II-a — destabilization per #der-adversarial-destabilization. Notice: the signal is *within* the model class (Gaussian handles $\pm\Delta$ mathematically), but correction cannot discharge it fast enough.

**Case 4 — Heavy-tailed $\xi_A$ with $\mathbb{E}[\xi_A^2] \sim r$ but kurtosis $\kappa \to \infty$ (expected Regime II-b).** Mean contribution is fine; the problem is the distribution shape. The Kalman filter — Gaussian-optimal — mis-gains: too aggressive for small events, too conservative for genuine large ones. The per-event KL gap $D_{\text{KL}}(P_\text{true} \Vert P_{\mathcal M_B}) \gt 0$ for any heavy-tailed $P_\text{true}$ against Gaussian. By #def-model-class-fitness, $\mathcal{F}(\mathcal M_B) \lt 1 - \varepsilon$ with $\varepsilon$ lower-bounded by the KL gap; by #result-structural-adaptation-necessity, no parametric update within $\mathcal M_B$ closes the mismatch. Result: Regime II-b — residuals retain non-Gaussian structure (visible in kurtosis tests); repair requires expanding the model class (e.g., Student-$t$ observation model), not more Kalman tuning.

Each case lands where the classification predicts. The derivation transfers to any recipient architecture in which the underlying AAT quantities are well-defined — this is the scope inherited from #result-sector-persistence-template + #def-model-class-fitness + #def-adaptive-tempo.

### Recovery of Emitter-Side Results

*[Derived (emitter-side-recovery)]*

Each existing emitter-side result is a restriction of the four-regime decomposition:

- **#der-adversarial-destabilization** is Regime II-a integrated over a tempo-proportional event stream. The magnitude-shock sub-regime corresponds directly; the structural-shock II-b subcase is implicit in that segment, collapsed into "adaptive reserve exceeded" but here made explicit.
- **#result-adversarial-tempo-advantage** — superlinear tempo scaling follows from the sector-persistence template's $1/\alpha$ (Model D) vs $1/\sqrt\alpha$ (Model S) applied to Regime II events. The $b$-exponent drops toward zero in the high-$U_{o,B}$ limit because the fraction of $A$'s events landing in Regime II drops (more fall into Regime III).
- **#obs-gated-tempo-advantage** is the recipient-side expression of boundary (I-c): high $U_{o,B}$ pushes events into Regime III where they add to variance without contributing to destabilization.
- **#hyp-symbiogenic-composition** corresponds to asymmetric classification: host's signals to endosymbiont contain high-$\mathcal{I}$ structure the endosymbiont's class cannot initially represent (Regime II-b for the endosymbiont, forcing structural adaptation toward the host's class); endosymbiont's signals to the host land in Regime I (host absorbs endosymbiont's accumulated structure). Consolidation is the fixed-point where both streams are Regime I.
- **Cooperative signaling** (in #der-team-persistence) — Regime-I events from aligned emitters contribute negatively to $\rho_B^{\text{eff}}$ via the cooperative-action term. The communication-tempo $\nu_{ji}^{\text{comm}} \cdot \eta_{ji}^\ast$ is the rate of Regime-I events times the recipient's informative gain.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Three independent boundaries (sector-region / model-class / observability) | Import from #def-model-class-fitness + #result-sector-persistence-template + #obs-gated-tempo-advantage | Formulation choice (three-way partition; coarser / finer alternatives possible) |
| Four-regime partition (I / II-a / II-b / III) | The three boundaries yield four boundary-state combinations; only four are non-degenerate | Derived from the boundary structure |
| (I-a) / (II-a) boundary at $R_B$ | #result-sector-persistence-template's sector-region radius | Derived |
| (I-b) / (II-b) boundary at $\mathcal{F}(\mathcal M_B) \cdot \mathcal I_{\max}$ | #def-model-class-fitness + class-capacity normalization | Formulation (the $\mathcal I_{\max}$ normalization is heuristic; sufficient-statistics-span form is cleaner — see Working Notes) |
| (I-c) / (III) boundary at $U_{o,B} \cdot c_\text{floor}$ | #obs-gated-tempo-advantage + detection-theory threshold | Formulation ($c_\text{floor}$ is a detection-power parameter) |
| Regime-typed $\rho_B^{\text{eff}}$ decomposition with negative Regime-I term | Aggregation over event stream using regime classification | Derived (the sign of the Regime-I term is structural, not a choice) |
| Kalman-over-Kalman four-case derivation | Direct application of Kalman gain + sector + KL-gap + SNR analyses | Proved (for the stated case) |
| Recovery of #der-adversarial-destabilization, #hyp-symbiogenic-composition, #obs-gated-tempo-advantage, #der-team-persistence as restrictions | Each emitter-side result is exhibited as a per-regime special case | Derived |
| Non-Gaussian Case 4 derivation (heavy-tailed → II-b via KL gap) | Informal argument grounded in robust-filtering literature (Huber, Masreliez) | Discussion-grade (rigorous version requires per-family KL computation) |
| Class 2 (Partial) approximation with $\kappa_{\text{processing}}$ degradation | Transfer from Class 1 (Separated) with goal-blind-update failure | Formulation (qualitative); exact form requires spelling out the goal-contamination coupling |

## Epistemic Status

*Conditional.* Max attainable: *derived* for the classification structure in Class 1 (Separated) architectures; *exact* for the Kalman-over-Kalman worked case in sub-scope $\alpha$; *robust qualitative* for general sub-scope $\beta$ recipients.

The three boundaries are structurally independent and each is stated in an existing AAT quantity, so the four-regime partition is not ad-hoc; it is forced by the structure of the quantities already in the theory. Within Class 1 (Separated; goal-blind epistemic update per #der-directed-separation) and sub-scope $\alpha$ recipients (Kalman / conjugate-Bayesian / exponential-family / strongly-convex-gradient / linear-PD), the Kalman-over-Kalman derivation transfers with A2' derived per #der-gain-sector-bridge, and each case yields the predicted regime by direct substitution. In sub-scope $\beta$ (PID / rule-based / human-judgment), the classification's form transfers but boundary (I-a) requires per-instantiation verification of the sector bound, inheriting from #result-sector-persistence-template's sub-scope $\beta$ caveat.

**Scope limits.** Class 3 (Coupled) recipients are out of formal scope: the coupled epistemic-purposeful update violates #der-directed-separation, so the regime assignment cannot be cleanly computed against $M_B$ alone. This is `03-llm-core/` territory. Class 2 (Partial) recipients inherit with degradation proportional to $\kappa_{\text{processing}}$: the Regime-I update may be goal-contaminated, and Regime II-b may be misdiagnosed as II-a or III under goal-blind-update failure. Per-event classification is singular-trajectory-indexed by #scope-agent-identity; aggregation over event streams is deferred to #result-sector-persistence-template.

**What the classification does not claim.** (i) It does not determine *semantic content*: knowing an event is Regime I tells you $B$ will update, not *what* $B$ will believe afterward — that lives in #disc-credit-assignment-boundary's default signal function. (ii) It does not make the four regimes sharp in practice: real recipients' sector regions and class capacities have estimation uncertainty, so borderline events oscillate across boundaries under parameter noise. (iii) It does not replace #result-sector-persistence-template's temporal aggregation; it provides the per-event regime label that feeds into the aggregate disturbance bound.

## Discussion

**Complement, not replacement, of the emitter-side segments.** #der-adversarial-destabilization, #result-adversarial-tempo-advantage, #obs-gated-tempo-advantage, #hyp-symbiogenic-composition, and #der-team-persistence each describe what happens when $A$'s praxis couples into $B$. They collapse the variation into a scalar increment on $B$'s effective disturbance rate. The recipient-side classification decomposes that increment into regime-typed contributions with (importantly) a **signed** Regime-I component. The five emitter-side segments are recovered as restrictions — the classification provides the pattern-recognizer to match the emitter-side optimizer.

**Why II-a vs II-b matters.** Both destabilization regimes manifest as "adaptive reserve exceeded" in the emitter-side view. But the repairs are different: magnitude-shock (II-a) calls for more bandwidth — larger $R_B$, higher $\alpha_B$, faster tempo; structural-shock (II-b) calls for a different model class — an expansion, grafting, or compression in the sense of #result-structural-adaptation-necessity. An organization running rapid-response incident drills against a bureaucratic-process adversary faces II-a and responds with more capacity; the same organization hit by a technology-regime change faces II-b and responds with restructuring. The two produce similar pain signals but admit opposite cures. Collapsing them confuses diagnosis.

**Pairing with #adversarial-edge-targeting (Part III GAP).** The classification provides the recipient-side pattern-recognizer; the emitter-side question — which of $B$'s strategy edges are most valuable for $A$ to attack — provides the adversary-optimization complement. The two compose: the emitter chooses which edge to target; the classification determines what happens at that edge. A particularly sharp move the classification makes visible but the emitter-side formulation hides: the **Regime-I-with-adversarial-content attack** — an emitter who can control the content $y_G$ fed into $B$'s default log-odds signal function (per #disc-credit-assignment-boundary) can choose the sign of $(y_G - \hat P_\Sigma)$ to push $\lambda_k$ in the direction that degrades $\Sigma_B$ most. This is not a destabilizing attack (which lands in Regime II); it is an *informational* attack that exploits $B$'s openness to Regime-I updates to inject misinformation. The emitter-side formulation, which represents coupling as a scalar $\gamma_A$, cannot express the sign lever; the recipient-side decomposition does. The value is maximized at edges with large plan-sensitivity $J_k$ and moderate credence $p_k$ — exactly the edges load-bearing for $\Sigma_B$.

**Agent opacity and the emitter-side regime distribution.** Hafez et al. (2026)'s agent opacity $H_b^B = H(S, A \mid S')$ is primarily *emitter-side*: it gates $A$'s ability to model which of $B$'s regimes a given signal will land in. As $H_b^B \to 0$ the emitter can target specific regimes adversarially; as $H_b^B \to \infty$ the emitter's signals distribute across regimes and the targeting advantage collapses. Formally, $\gamma_A^{\text{effective}} = \gamma_A^{\text{max}} \cdot f(H_b^B)$ with $f$ monotonically decreasing. This is the dual of #obs-gated-tempo-advantage's story: where observation-gates-advantage says the emitter's advantage degrades when its observations of the *environment* are noisy, opacity says the advantage degrades when its observations of *$B$* are noisy. Cooperative signaling is the mirror: low $H_b^B$ (legibility) enables aligned emitters to target signals into $B$'s Regime I. This is #hyp-auftragstaktik-principle's recipient-side translation: shared objectives give $A$ a better model of $B$'s prior and model class, which lets $A$ produce signals that land in $B$'s informative regime.

**Organizational reception intuition.** The four regimes correspond to a familiar organizational diagnostic: (Regime I) *heard* — the organization updated on the relevant edges of its $\Sigma_\text{org}$; (II-a) *shattered by shock* — signal was too large/fast, the organization's correction bandwidth was exceeded; (II-b) *couldn't hear* — signal required reorganization beyond the organization's structural capacity, matching Cohen & Levinthal's (1990) absorptive-capacity framing; (III) *absorbed as fatigue* — signal drained $\Delta\rho^\ast$ without producing structural change, the "death by a thousand memos" pattern. The cross-domain instantiation is cleanest where $\mathcal{F}(\mathcal M_B)$ maps to absorptive capacity and $U_{o,B}$ to communication-channel quality.

**Future meta-segment candidate.** The recipient-side classification is the *signal-reception* complement to #result-sector-persistence-template's *persistence-under-disturbance* structure. If a future pattern emerges elsewhere (e.g., consolidation dynamics classifying inputs, or a more general theory of inter-agent coupling) a meta-segment `#signal-reception-pattern` could name the recipient-classification shape. Premature at this stage; log as speculation.

## Working Notes

- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Scope-limits paragraph updated (Class 2 fully-merged → Class 3 Coupled; Class 3 partially-modular → Class 2 Partial). What-Is-Derived table updated (Class 3 approximation → Class 2 Partial approximation). The four-regime classification (I / II-a / II-b / III) is recipient-side signal-processing vocabulary — unaffected by the GUC rename. Removed at `candidate` stage per FORMAT.md Gate 4.

- **$\mathcal I_{\max}(\mathcal M_B)$ — replace with sufficient-statistics-span.** The boundary (I-b) uses $\mathcal{F}(\mathcal M_B) \cdot \mathcal I_{\max}(\mathcal M_B)$ as the class's representational ceiling on per-event information. The cleaner formulation: (I-b) holds iff the event's sufficient statistics for prediction lie in the span of $\mathcal M_B$'s sufficient statistics. For parametric families (exponential families, Gaussian) the explicit form is routine; for non-parametric classes it requires the projection-to-class formalism of #form-information-bottleneck. Worth refining at the next candidacy review.
- **Four regimes vs finer splits.** The partition is the *coarsest* useful split where each regime has a distinct AAT-machinery response. Regime I could split into within-observability / within-calibration (point update vs structural refinement) as a fifth-regime refinement; Regime II-a could split by transient vs sustained dynamics. These duplicate the structural-adaptation hierarchy and are not pursued here.
- **Heavy-tailed derivation rigorization.** The Case-4 argument is informal; a rigorous version would compute the effective Kalman gain under heavy-tailed observation misspecification and show residuals retain signal. This is the robust-filtering territory (Huber, Masreliez) and is standard; the classification does not depend on a specific non-Gaussian family, just on the KL gap being nonzero.
- **Regime II-b as candidate #disc-identifiability-floor Instance 3.** Under a sustained Regime II-b stream, $B$'s $\rho_B^{\text{eff}}$ degrades at a rate lower-bounded by the KL gap between $\mathcal M_B$ and the true event distribution — a quantitative misspecification-cost floor. This is adjacent to #disc-identifiability-floor's "Misspecification-cost quantification" open extension. Worth a focused spike to formalize.
- **Connection to active inference.** Regime II-b corresponds to high-surprise events that exceed the agent's generative model — what AI calls "novel generative context." The classification avoids AI's variational-free-energy-as-master commitment (per the spike-routing cycle, CHANGELOG 2026-05-17); it uses only the information-theoretic content of $\mathcal{I}(e)$, not the variational machinery.
- **Next spike candidates.** (1) Formalize the $f(H_b^B)$ emitter-side-effect function — tighten the qualitative $\gamma_A \propto f(H_b^B)$ into a derived form (tracked: `TODO.md` "Queued spike work"; cross-referenced in `spikes/PROPOSED.md` Reserved/owned-elsewhere). (2) Formalize Regime II-b misspecification-cost as a structural result ( #disc-identifiability-floor Instance 3 candidate) (tracked: `TODO.md` identifiability-floor queued-spike cluster; same cross-reference). (3) **Resolved — no longer a candidate.** The `#adversarial-edge-targeting` arg-max *is* formally solved in canon: #der-agent-opacity derives it as the 16-cell emitter-recipient composition (a Derived arg-max; the previously-reserved Section-III GAP is filled), with *this* segment supplying the recipient-side four-regime classification that pairs with the emitter side. Scope per #der-agent-opacity Epistemic Status: closed-form under sub-scope-$\alpha$ coupling; general non-convex coupling is per-case optimization, a noted scope caveat, not an open derivation.
