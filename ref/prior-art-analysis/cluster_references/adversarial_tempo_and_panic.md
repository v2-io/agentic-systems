# Cluster Reference: Adversarial Tempo and Panic (The Effects Spiral)

**Overview:** Formalizes adversarial encounters as coupled tracking loops, deriving superlinear scaling advantages for tempo and identifying the 'Effects Spiral' of panic via joint-Jacobian eigenvalue conditions.

---

## Canonical Source Segments

### Source: `cooperative-adversarial-intro.md`

```yaml
---
slug: cooperative-adversarial-intro
type: discussion
status: discussion-grade
depends:
  - hyp-communication-gain
  - def-unity-dimensions
stage: draft
---
```


# Chapter Introduction: Cooperative and Adversarial Coupling

Once composites exist, the question becomes how their members interact. This chapter develops the dynamics — cooperative coupling that helps allies, adversarial coupling that hurts opponents, and the four-regime classification of how an arriving event lands on its recipient — under a single signed-coupling structure. Cooperation and adversarial dynamics are not two theories; they are the same machinery with opposite signs.

The framing comes from the disturbance decomposition. The disturbance rate an agent faces decomposes into environment, adversarial, and cooperative components,

$$\rho_i = \rho_{i,\text{env}} + \sum_j \gamma_{j \to i}^{\text{adv}} \mathcal T_j - \sum_j \gamma_{j \to i}^{\text{coop}} \mathcal T_j$$

with $\gamma \gt 0$ in both cases, but opposite signs in the sum. Cooperative allies reduce agent $i$'s effective disturbance by acting in the shared environment — stabilizing resources, preempting threats, absorbing perturbations. Adversaries amplify it by acting against. The machinery is identical; the sign is what differs. This is the unification that "adversarial dynamics as a separate theory" misses, and it is one of the clearer cases of AAT's framework character: not many results, one principle applied with a sign flip.

Two physically distinct cooperative mechanisms compose under this structure, and the chapter is careful about distinguishing them. *Communication tempo*: allies *tell* agent $i$ things that improve its correction — the communication-tempo term that adds to $\mathcal T_i$ via #hyp-communication-gain. *Cooperative action*: allies *do* things that reduce the disturbance $i$ faces — the negative term in $\rho_i$ above. The two enter the persistence inequality at different points (one raising $\mathcal T$, the other lowering $\rho$) and warrant separate accounting. Counting a single ally-event in both would double-count its benefit. There is a useful concrete analogy: this is the mathematical difference between a consultant and an employee. A consultant boosts your tempo by telling you what's happening; if your $\alpha$ is too low to act on the information, the consultant doesn't save you — you'll just understand your failure more clearly. An employee lowers your effective disturbance by intercepting the volatility before it reaches your state. Communication and cooperative action are not interchangeable, and structurally failing agents need the second more than the first.

The adversarial side is where the famous results live. Under coupling-dominant deterministic disturbance — the canonical adversarial regime — the steady-state mismatch ratio between two agents scales as the *squared* tempo ratio:

$$\frac{\Vert\delta_B\Vert_{ss}}{\Vert\delta_A\Vert_{ss}} = \left(\frac{\mathcal T_A}{\mathcal T_B}\right)^2$$

The faster agent both corrects its own mismatch faster *and* generates disturbance for the slower agent faster. Speed advantage is multiplicative, not additive: a 2:1 tempo ratio yields a 4:1 mismatch ratio; a 3:1 ratio yields 9:1; a 10:1 ratio yields 100:1. This is the formal analog of Boyd's "getting inside the opponent's OODA loop" — it turns military intuition into physics. The math itself is not mysterious; it is just the steady-state formula applied to both sides and ratioed. But the consequence is sharp. The squared scaling means that a sufficiently large tempo asymmetry in a coupling-dominant regime is not a quantitative disadvantage but a regime change: at 100:1 mismatch ratio, the slower agent is almost certainly past its operating reserve $R$, which means structural collapse rather than degraded performance. Speed advantage in a coupled regime *compounds*, and the consequence is qualitatively different from what additive-intuition predicts. Under stochastic adversarial coupling the exponent drops from 2 to 3/2; under non-coupling-dominant base disturbance it approaches 1. The exponent depends on the regime — the chapter names them explicitly — but the regime where it is sharpest is also where it matters most.

There is a caveat in the other direction: speed without coupling is useless. The destabilization threshold from #der-adversarial-destabilization makes this explicit — if $A$'s coupling to $B$ is weak ($\gamma_A \to 0$), $A$ can have infinite tempo and still fail to destabilize $B$. Being fast in a vacuum doesn't accomplish anything; you have to be fast *and* coupled. The two are jointly required and neither suffices.

The effects spiral — the corollary in #der-adversarial-destabilization where $B$'s degrading model causes $B$'s actions to become erratic in ways that increase $A$'s coupling effectiveness — is the mathematics of panic. When an agent is pushed past its adaptive reserve, its corrections become unreliable, which makes it more legible to the adversary, which increases the disturbance, which pushes the agent further past reserve. The spiral terminates only when the agent undergoes structural adaptation (a different model class, a different mode of operation) or ceases to function as an adaptive agent entirely. The structural implication for any agent under sustained adversarial pressure is that resilience is not just high $\alpha$ or high $R$ — it is also having a mechanism to break the spiral before structural collapse, which usually means external intervention from outside the agent.

The other interesting move is the recipient-side decomposition. From the emitter's perspective, coupling is a single number — $\gamma_A \cdot \mathcal T_A$ — applied to the target's disturbance budget. From the recipient's perspective, that scalar collapses real structure. An arriving event from $A$ lands on $B$ as one of four qualitatively different things, determined by three independent boundary conditions in $B$'s existing AAT quantities. It might be a *Regime I informative update* (small enough to be absorbed, large enough to register, within $B$'s model class — the good case). It might be a *Regime II-a magnitude shock* (large enough to exit $B$'s sector region — the destabilizing-fast-events case). It might be a *Regime II-b structural shock* (within sector but outside $B$'s model class — the wrong-kind-of-event case, repairable only by structural adaptation rather than by faster correction). Or it might be a *Regime III ambient erosion* (below the observability floor — death by a thousand memos, where every event is small enough to be processed but the cognitive overhead of processing accumulates until the agent has no tempo left for real work; this is the formal version of why DDoS-of-low-priority-alerts is a real attack and not just inconvenience). Different regimes call for different repairs. Magnitude shocks call for more bandwidth; structural shocks call for a different model class; ambient erosion calls for better filtering, often at the infrastructure layer before signals reach the agent. Conflating them, which the scalar emitter view does, confuses diagnosis.

This is one of the chapter's load-bearing pedagogical moves. Most multi-agent frameworks treat "coupling" as a single coefficient. The recipient-side classification says: the coefficient is what the emitter cares about; the regime is what the recipient cares about; and they are not interchangeable for purposes of figuring out what to do.

The flow of the chapter: team persistence and the signed disturbance decomposition ( #der-team-persistence) → adversarial destabilization and the effects spiral ( #der-adversarial-destabilization) → the recipient-side four-regime classification ( #der-interaction-channel-classification) → the superlinear tempo advantage and its regime-dependent exponents ( #result-adversarial-tempo-advantage). Chapter 5 extends to symmetric strategic composition (equilibrium-convergence framing for partially-opposing objectives), agent opacity as the formal dual of observation quality, and the qualifications that gate when the superlinear advantage actually obtains.

## Working Notes

- This is a chapter-introduction segment; it bridges Chapter 3's quality/communication machinery to Chapter 4's dynamics under signed coupling. It carries no formal claim of its own.
- The "consultant vs employee" analogy comes from Gemini's first-encounter reaction to #der-team-persistence — it captures the communication-vs-cooperative-action distinction at the level of intuition where the math lands. The intro adopts it because the original abstract phrasing didn't convey why the distinction is load-bearing.
- The "regime change rather than quantitative disadvantage" framing of the $b=2$ scaling is the consequential corollary worth surfacing in the intro — most readers will hit the squared scaling and think "an order of magnitude" rather than "structural collapse." The intro pulls the corollary forward so it lands at the same time as the result.
- The "mathematics of panic" framing for the effects spiral is another Gemini observation worth keeping — it does in one phrase what a paragraph of formal commentary does less effectively.
- The "death by a thousand memos" framing for Regime III is concrete and load-bearing: the regime exists not because the events are individually significant but because processing them consumes tempo that should be going to actual work. This connects directly to logogenic-agent infrastructure design (PROPRIUM ASM, attention-management) where Regime III filtering at the infrastructure layer is operational.


---

### Source: `der-adversarial-destabilization.md`

```yaml
---
slug: der-adversarial-destabilization
type: derived
status: conditional
depends:
  - result-sector-condition-stability
  - deriv-sector-condition
  - result-sector-persistence-template
  - def-adaptive-tempo
stage: draft
---
```


# Derived: Adversarial Destabilization

When two agents are coupled such that one's praxis contributes to the other's disturbance rate, the faster agent can generate aporia in the target faster than the target's epistrophe can resolve it — driving the target outside its invariant region and causing the correction mechanism to break down entirely.

## Formal Expression

This segment is the sector-persistence template ( #result-sector-persistence-template) applied with coupling-amplified disturbance: $\rho_B = \rho_{B,\text{base}} + \gamma_A \mathcal T_A$ (Model D) or $\sigma_B = \sigma_{B,\text{base}} + \gamma_A \mathcal T_A$ (Model S). The destabilization threshold is the **negation** of the template's persistence condition for agent $B$: destabilization occurs precisely when the coupling-amplified disturbance violates $\alpha_B R_B \gt \rho_B$. Persistence and destabilization are the same inequality viewed in opposite directions. The superlinear adversarial scaling ( #result-adversarial-tempo-advantage) follows from the template's $1/\alpha$ (Model D) versus $1/\sqrt{\alpha}$ (Model S) scaling, not from separate derivation.

*[Derived (adversarial-destabilization, from sector-persistence-template)]*

**Setup.** Both agents satisfy the single-agent sector-persistence template ( #result-sector-persistence-template) with parameters $(\alpha_A, R_A)$ and $(\alpha_B, R_B)$. Coupling amplifies $B$'s effective disturbance rate by $\gamma_A \cdot \mathcal{T}_A$; destabilization is the negation of the template's persistence condition $\alpha_B R_B \gt \rho_B^{\text{eff}}$ for $B$. See #result-adversarial-exponent-regimes for regime taxonomy.

### Model D: deterministic drift coupling

*[Assumption (Coupling Model D)]* $\rho_B = \rho_{B,\text{base}} + \gamma_A \cdot \mathcal{T}_A$. The template's Model D conclusion $R_B^\ast = \rho_B/\alpha_B$ applied with the coupling model yields $B$'s destabilization threshold $R_B^\ast \gt R_B$:

$$\boxed{\;\mathcal{T}_A \;\gt\; \frac{\alpha_B R_B - \rho_{B,\text{base}}}{\gamma_A}\;} \quad \text{(Model D)}$$

Denote $\Delta\rho_B^\ast = \alpha_B R_B - \rho_{B,\text{base}}$, $B$'s adaptive reserve — the template's reserve quantity applied with the baseline disturbance. $\square$

### Model S: stochastic noise coupling

*[Assumption (Coupling Model S)]* $\sigma_B = \sigma_{B,\text{base}} + \gamma_A \cdot \mathcal{T}_A$ — the adversary's tempo increases unpredictability, not systematic direction. The template's Model S conclusion $R_B^\ast = \sigma_B \sqrt{n/(2\alpha_B)}$ (scalar $n = 1$) applied with the coupling yields the destabilization threshold:

$$\boxed{\;\mathcal{T}_A \;\gt\; \frac{R_B \sqrt{2\alpha_B} - \sigma_{B,\text{base}}}{\gamma_A}\;} \quad \text{(Model S)}$$

**Scaling difference.** The Model D threshold is linear in $\alpha_B$; the Model S threshold is linear in $\sqrt{\alpha_B}$ — the same $1/\alpha$ versus $1/\sqrt{\alpha}$ split the template gives for the two disturbance models, propagated through the destabilization negation. This is the direct origin of the $b = 2$ versus $b = 3/2$ exponent distinction in #result-adversarial-exponent-regimes, not a separate derivation. $\square$

### Unified view

Symmetrically, $B$ destabilizes $A$ when the analogous threshold on $\mathcal T_B$ is exceeded, using whichever model describes $A$'s disturbance. The adversarial outcome depends on whether either agent can push the other past its stability limit.

**Regime selection in practice.** Model D fits situations where adversarial action produces persistent positional shifts (military maneuvering, API changes propagating through dependents, doctrinal initiative). Model S fits situations where adversarial action produces unpredictable perturbations around a stationary level (feints, randomized probing, market volatility). Mixed cases are handled by decomposing the disturbance into drift and noise components and applying both bounds additively.

**Interpretation.** "Getting inside the opponent's OODA loop" has a precise Lyapunov characterization: Agent $A$ destabilizes Agent $B$ when $A$'s praxis, multiplied by coupling effectiveness, generates aporia in $B$ faster than $B$'s epistrophe can resolve it — specifically, when $A$'s tempo times coupling exceeds $B$'s adaptive reserve $\Delta\rho^\ast_B$. This captures:

- **Asymmetric coupling** ($\gamma_A \neq \gamma_B$): an agent with lower tempo but higher coupling effectiveness can still win.
- **Finite reserves**: an agent with very high $\mathcal{T}$ but operating near its model-class limit ($\Delta\rho^\ast$ small) is vulnerable despite high tempo.
- **Structural collapse**: when $R^\ast_B \gt R_B$, the failure mode is not merely "large mismatch" but "correction mechanism breakdown" — connecting to #result-structural-adaptation-necessity.

### Corollary: The Effects Spiral

When Agent $B$ is driven past its stability boundary ($R^\ast_B \gt R_B$), and $B$'s degrading model causes $B$'s actions to become erratic in a way that increases $A$'s coupling effectiveness ($\gamma_A$ increases with $\Vert\delta_B\Vert$), the result is a positive-feedback Lyapunov instability:

*[Discussion — Mechanism Schematic]*

$$\Vert\delta_B\Vert \uparrow \;\Rightarrow\; B\text{'s actions become erratic} \;\Rightarrow\; \gamma_A \uparrow \;\Rightarrow\; \rho_B \uparrow \;\Rightarrow\; \Vert\delta_B\Vert \uparrow$$

With $\gamma_A$ now an increasing function of $\Vert\delta_B\Vert$, the disturbance term in $B$'s dynamics grows superlinearly. $\dot{V}_B \gt 0$ and increasing — mismatch accelerates away from the stability region. The spiral terminates only when $B$ undergoes structural adaptation ( #result-structural-adaptation-necessity — changing the model class) or ceases to function as an adaptive agent entirely.

## Epistemic Status

Both Model D and Model S destabilization thresholds are *exact* under their respective coupling assumptions (which treat $\mathcal{T}_A$ as exogenous). The Model D threshold follows from the deterministic sector-condition steady state $R^\ast = \rho/\alpha$ (Prop A.1); the Model S threshold follows from the stochastic sector-condition steady state $R^\ast_S = \sigma\sqrt{n/(2\alpha)}$ (Prop A.1S). Both coupling models (additive to $\rho$ in Model D, additive to $\sigma$ in Model S) are *assumptions* — they decouple the agents rather than modeling the fully coupled dynamical system where both agents' mismatch states co-evolve. The analysis therefore characterizes the *destabilization threshold* (the conditions under which $A$ *can* push $B$ past its stability boundary) rather than the full transient dynamics. This is a worst-case bound, treating $A$ as operating at its steady-state tempo.

The effects spiral (corollary) is *discussion-grade* — the positive-feedback mechanism is qualitatively clear, but formalizing the $\gamma_A(\Vert\delta_B\Vert)$ functional form and proving instability under it requires specifying how an agent's degrading model affects its action quality, which the theory does not yet formalize.

A full coupled Lyapunov analysis with a joint function $V(\delta_A, \delta_B)$ would capture mutual feedback effects but requires specifying how each agent's mismatch state affects the other's disturbance in real time — an open extension.

## Discussion

**Destabilization vs. steady-state ratio.** The destabilization threshold is a failure of *structural persistence* (see Persistence in `LEXICON.md`) — the point where the correction machinery can no longer outpace the adversarially amplified disturbance. An adversary does not need to attack operational persistence (pushing the target near its boundary) or continuity persistence (disrupting identity) directly; destroying structural persistence is sufficient, because without it, operational persistence degrades to zero and the agent ceases to function regardless of its continuity stance. The linear analysis in #hyp-mismatch-dynamics gives the steady-state mismatch ratio under coupling: a quantitative result about how much worse $B$ does. This segment gives the qualitative result: under what conditions does $B$ *fail entirely*, not merely fall behind. The linear analysis tells you the score; the Lyapunov analysis tells you when the game is over.

**Connection to #result-adversarial-tempo-advantage.** The simulation results show the tempo advantage is superlinear (exponent $\approx 2$ in pure adversarial regimes). This Lyapunov result explains WHY: the destabilization threshold creates a phase transition — below it, $B$ persists (possibly with degraded performance); above it, $B$'s correction mechanism collapses entirely, and the effects spiral accelerates the collapse.

**Recipient-side refinement.** This segment's $\gamma_A \mathcal T_A$ scalar increment compresses a richer structure. Per #der-interaction-channel-classification, events arriving at $B$ fall into four regimes with three independent boundaries (sector-region / model-class / observability). This segment's destabilization story is the Regime II integration — specifically, the magnitude-shock sub-regime (II-a) where $\lVert e\rVert_B \gt R_B$. The structural-shock sub-regime (II-b), where the signal exceeds $B$'s *model-class capacity* regardless of magnitude, produces destabilization via a different mechanism (per #result-structural-adaptation-necessity's trigger condition at truth) and admits a different repair (structural adaptation, not more tempo). Both sub-regimes manifest as "adaptive reserve exceeded" in the scalar view, but the distinction is load-bearing for diagnosis and repair. The #der-interaction-channel-classification segment also surfaces an adversarial move this segment's formulation cannot express: *Regime-I-with-adversarial-content* — exploiting $B$'s openness to informative updates by injecting misinformation with adversarially-chosen sign on the log-odds signal. See #der-interaction-channel-classification Discussion for the full decomposition.

**Agent opacity and coupling effectiveness.** $\gamma_A$ is stated as a parameter but its determinants are not decomposed. One key factor is how *legible* or *opaque* the target agent $B$ is to the adversary $A$. We adopt from Hafez et al. (2026) the backward predictive uncertainty $H_b = H(S, A \mid S')$ as a measure of agent opacity — how many distinct (state, action) pairs produce indistinguishable environment transitions. High $H_b$ means the agent is opaque; low $H_b$ means it is legible. In adversarial settings, $B$'s opacity directly affects $A$'s ability to model $B$'s correction function: low $H_b^{(B)}$ (transparent target) enables targeted disruption that maximizes $\gamma_A$, while high $H_b^{(B)}$ forces $A$ to act against an uncertain model, reducing effective $\gamma_A$. Symmetrically, high $H_b^{(A)}$ (opaque adversary) degrades $B$'s ability to anticipate $A$'s disruptions — increasing the effective observation uncertainty $U_o$ in $B$'s model of $A$. The coupling effectiveness is thus modulated by opacity in both directions: $\gamma_A \propto 1/H_b^{(A)} \cdot 1/H_b^{(B)}$ is a qualitative relationship (precise functional form is open). $H_b$ is the formal dual of observation quality $U_o$: where $U_o$ characterizes how well the agent sees the world, $H_b$ characterizes how well the world sees the agent. See `#der-agent-opacity` for the formal definition, the sign-flip derivation via signed coupling, the emitter-side four-regime classification, and the 16-cell emitter-recipient composition that operationalizes adversarial-edge-targeting.

**Connection to extreme transition dynamics (Miller 2022).** The effects spiral has a constructive counterpart: the same self-reinforcing coupling mechanism that drives destabilization here can drive *regime transitions* rather than collapse when the coupling is constructive rather than destructive. An environmentally neutral variant accumulates through drift, creating a niche that a mutant in the opposing population exploits — a positive-feedback cascade that rapidly transforms both populations. The Lyapunov coupling model applies to both signs: destructive coupling (this segment) increases $\rho$; constructive coupling ( #der-team-persistence) decreases it. The difference is sign, not structure. The endogenous emergence of coupling — where $\gamma$ changes as population composition shifts — is the critical extension needed to formalize the full transition motif; it is flagged as a gap in Section III's dynamics (see #result-structural-adaptation-necessity for the single-agent analog and the dynamics-level gaps enumerated in the OUTLINE).

## Working Notes

- The decoupled analysis (treating $\mathcal{T}_A$ as exogenous) is conservative — it's the best case for $A$. In a fully coupled system, $A$'s actions against $B$ may divert adaptive capacity from $A$'s own mismatch correction, creating a self-limiting effect. The coupled analysis for symmetric adversarial composition is not a Lyapunov problem: it is a fixed-point / equilibrium problem on the joint best-response dynamics, and its formal home is `#deriv-strategic-composition`. The effects spiral in this segment's Corollary becomes a joint-Jacobian eigenvalue condition there. **Scope boundary:** `#result-contraction-template` (the contraction-metric generalization of `#result-sector-persistence-template`) covers the cooperative half of Section III composition. Adversarial / strategic composition lies structurally outside the contraction-metric framework (saddle-point equilibria are not attracting fixed points; Slotine compositional theorems do not apply); this segment's `#result-sector-persistence-template` instantiation with coupling-amplified disturbance is the correct tool for the asymmetric-adversarial regime.
- $\gamma_A$ is the product of coupling strength, observability, and action impact — it captures the full spectrum from tightly coupled (direct disruption) to loosely coupled (indirect environmental effects). In the software domain, coupling is precisely measurable from the dependency graph ( #def-system-coupling).
- The effects spiral is the formal analog of Boyd's cascading disorientation of the slower adversary — the same structural pattern (tempo advantage → destabilization → accelerating breakdown) appears in the Lyapunov analysis. The model captures the pattern; whether it captures the actual mechanisms of human disorientation is an empirical question, not a mathematical one. Future work should formalize the $\gamma_A(\Vert\delta_B\Vert)$ relationship to make the spiral a result rather than a discussion-grade observation. The formal home of that formalization is `#deriv-strategic-composition` (its Discussion sketches the joint-Jacobian spectral-abscissa condition); the strengthening — deriving it in closed form for concrete AAT agent classes, upgrading this segment's effects-spiral from discussion-grade to derived — is tracked. *(Indexed: `spikes/PROPOSED.md` Tier 1 — "Effects-spiral eigenvalue condition — concrete agent classes".)*


---

### Source: `der-interaction-channel-classification.md`

```yaml
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
```


# Derived: Interaction-Channel Classification (Recipient-Side)

The same signal from agent $A$ lands on recipient $B$ as one of four qualitatively different things — informative update, magnitude-shock, structural-shock, or ambient noise — determined by three independent boundary conditions stated entirely in $B$'s existing AAT quantities. The emitter-side collapse of this variation into a scalar $\gamma_A \mathcal T_A$ loses information that is load-bearing: the recipient's repair path depends on which regime the event falls into, and "more tempo" vs "different model class" address structurally different failure modes.

## Formal Expression

### Setup and Notation

Two purposeful agents $A$ and $B$ coupled through a shared environment. $A$'s praxis produces an event $e_\tau^A$ that enters $B$'s observation channel. On $B$'s side the event is processed by the standard AAT machinery: $h_B$ maps the $A$-induced environment state to observation $o_\tau^B$ ( #def-observation-function); mismatch is $\delta_\tau^B = o_\tau^B - \hat o_\tau^B$; update absorbs $\delta_\tau^B$ with gain $\eta_B^\ast = U_{M,B}/(U_{M,B} + U_{o,B})$ ( #emp-update-gain).

Two event-level quantities enter the classification and must not be conflated:

- $\lVert e_\tau^A\rVert_B$ — the **magnitude** of the event in $B$'s observation space (how large a perturbation it produces in $\delta_\tau^B$ on arrival).
- $\mathcal I(e_\tau^A)$ — the **information content** of the event conditional on $B$'s prior, formally $I(e_\tau^A; \Omega \mid M_{B,\tau^-})$ per NOTATION.md's event-information quantity. A large-magnitude already-predicted event has large $\lVert e\rVert$ but small $\mathcal I$; a tiny-magnitude structurally novel event has small $\lVert e\rVert$ but large $\mathcal I$.

Let $\mathcal F(\mathcal M_B)$ denote $B$'s model-class fitness ( #def-model-class-fitness), and $\mathcal I_{\max}(\mathcal M_B)$ the maximum per-event information content representable within the class (see Working Notes for the cleaner sufficient-statistics-span formulation).

### Classification Boundaries

*[Definition (regime-boundaries)]*

Event $e_\tau^A$ arriving at $B$ falls into one of four regimes, determined by three independent boundary conditions:

**Regime I (Informative update)** when all three hold:

$$\text{(I-a)} \quad \lVert e_\tau^A\rVert_B \leq R_B \qquad \text{(within sector-condition region)}$$

$$\text{(I-b)} \quad \mathcal I(e_\tau^A) \leq \mathcal F(\mathcal M_B) \cdot \mathcal I_{\max}(\mathcal M_B) \qquad \text{(representable within model class)}$$

$$\text{(I-c)} \quad \mathcal I(e_\tau^A) \cdot \nu^{(k)} \geq U_{o,B}^{(k)} \cdot c_\text{floor} \qquad \text{(above observability floor)}$$

where $k$ is the arrival channel, $\nu^{(k)}$ its event rate, and $c_\text{floor}$ a detection-theory constant controlling the false-alarm tolerance.

**Regime II-a (Magnitude-shock destabilization)** when (I-a) fails:

$$\lVert e_\tau^A\rVert_B \gt R_B$$

The event exits $B$'s sector-condition region on arrival. $B$'s correction function does not point inward strongly enough to discharge the mismatch before the next event; under sustained rate $\nu \gtrsim \alpha_B$, destabilization proceeds per #der-adversarial-destabilization.

**Regime II-b (Structural-shock destabilization)** when (I-a) holds but (I-b) fails:

$$\lVert e_\tau^A\rVert_B \leq R_B, \qquad \mathcal I(e_\tau^A) \gt \mathcal F(\mathcal M_B) \cdot \mathcal I_{\max}(\mathcal M_B)$$

The event's information content exceeds what $B$'s model class can represent. By #result-structural-adaptation-necessity, parametric update within $\mathcal M_B$ cannot close the mismatch; residuals retain systematic structure. Repair requires structural adaptation (a different model class), not more bandwidth.

**Regime III (Ambient noise / slow erosion)** when (I-a) and (I-b) hold but (I-c) fails:

$$\lVert e_\tau^A\rVert_B \leq R_B, \qquad \mathcal I(e_\tau^A) \leq \mathcal F(\mathcal M_B) \cdot \mathcal I_{\max}(\mathcal M_B), \qquad \mathcal I(e_\tau^A) \cdot \nu^{(k)} \lt U_{o,B}^{(k)} \cdot c_\text{floor}$$

The event is representable and within capacity but its information content sits below the observability floor. It contributes to $\delta_B$'s variance (enters Model S as part of $\sigma_{w,B}^2$) without triggering a usable update; $B$'s adaptive reserve $\Delta\rho_B^\ast$ slowly drains.

### Three Independent Boundaries

The three boundary conditions are structurally independent, each stated in quantities AAT already carries:

| Boundary | AAT quantities | Failure mode |
|---|---|---|
| (I-a) / (II-a): sector-region | $\lVert e\rVert_B$, $R_B$ (from #def-model-class-fitness / #result-sector-persistence-template) | *magnitude* — more capacity cures |
| (I-b) / (II-b): model-class | $\mathcal I(e)$, $\mathcal F(\mathcal M_B)$, $\mathcal I_{\max}(\mathcal M_B)$ | *class* — structural adaptation cures |
| (I-c) / (III): observability | $\mathcal I(e)$, $\nu^{(k)}_B$, $U_{o,B}^{(k)}$ (from #obs-gated-tempo-advantage) | *rate* — lower observation noise or higher event rate cures |

No new ad-hoc thresholds are introduced. $\mathcal I_{\max}(\mathcal M_B)$ is the only new symbol; see Working Notes for its cleaner sufficient-statistics-span formulation.

### Regime-Typed Disturbance Decomposition

*[Derived (regime-typed-rho-eff, from regime-boundaries + sector-persistence-template)]*

Under a stream of events $\{e_\tau^A\}$, $B$'s **regime-typed effective disturbance** rate decomposes into regime-typed contributions:

$$\rho_B^{\text{eff}} = \underbrace{\sum_{e \in \text{II-a}} \lVert e\rVert_B \cdot \nu_e}_{\text{magnitude disturbance}} \;+\; \underbrace{\text{floor}(\mathcal M_B) \cdot \sum_{e \in \text{II-b}} \nu_e}_{\text{structural mismatch floor}} \;+\; \underbrace{\sum_{e \in \text{III}} \sigma_e^2 \cdot \nu_e}_{\text{ambient variance}} \;-\; \underbrace{\sum_{e \in \text{I}} \iota_B(e)\,\mathcal I(e) \cdot \nu_e}_{\text{informative correction}}$$

The Regime-I term is **negative**: informative events reduce $B$'s effective disturbance rate, not increase it. This generalizes #der-team-persistence's cooperative-action term $-\gamma^{\text{coop}}\mathcal T_j$: a cooperative event is precisely a Regime-I event from an aligned emitter, and the sign flip in the emitter-side decomposition falls out of the regime assignment on the recipient side. Adversarial events land in Regimes II-a/II-b; ambient-noise events in Regime III.

The emitter-side formulation $\gamma_A \mathcal T_A \to \rho_B^{\text{eff}}$ compresses the regime-typed sum into a single scalar, losing (i) the sign of cooperative coupling, (ii) the magnitude vs structural distinction in destabilization, and (iii) the observability-floor loss to Regime III.

### Structured Derivation — Kalman-over-Kalman

*[Derivation (Kalman-over-Kalman, from regime-boundaries + update-gain)]*

For a concrete check, take $B$ as a Kalman filter on a scalar linear-Gaussian state with model class $\mathcal M_B = \{\theta \in [\theta_{\min}, \theta_{\max}]\}$, process noise $q$, observation noise $r$, sector parameter $\alpha_B = \eta_B^\ast = P_{\text{pred}}/(P_{\text{pred}} + r)$. $B$'s sector-region radius is $R_B = \sqrt{q/(1-\theta_{\max}^2)}$ (stationary standard deviation at the class edge).

$A$'s emitted perturbation $\xi_A$ enters $B$'s innovation as $\delta_\tau^B = \xi_A + \varepsilon_\tau + (\omega_\tau - \hat\omega_\tau)$. Four canonical distributions for $\xi_A$ partition the classification:

**Case 1 — Small-variance Gaussian $\xi_A \sim \mathcal N(0, s^2)$, $s^2 \ll r$ (expected Regime III).** $\mathcal I(\xi_A) \approx s^2/(2r \ln 2)$ nats — small. (I-a) holds ($s \ll R_B$); (I-b) holds (Gaussian-within-Gaussian); (I-c) fails because $\mathcal I(\xi_A) \lt U_{o,B} \cdot c_\text{floor}$. Result: Regime III. Derived consequence — the contribution to $\rho_B^{\text{eff}}$ is through $\sigma_{w,B}^2$; adaptive reserve drains by $\sum_e \eta_B^{\ast 2} s_e^2 \cdot \nu_e$.

**Case 2 — Moderate Gaussian $\xi_A \sim \mathcal N(\mu, s^2)$, $\mu \ll R_B$, $s^2 \sim r$ (expected Regime I).** $\mathcal I(\xi_A) = \tfrac{1}{2}\log(1 + (s^2 + \mu^2)/r)$ — substantial. All three (I-a)/(I-b)/(I-c) hold. Result: Regime I. Standard Kalman update; $M_B$ refines; Regime-I term contributes negatively to $\rho_B^{\text{eff}}$.

**Case 3 — Binary kick $\xi_A \in \{\pm\Delta\}$ with $\Delta \gt R_B$ (expected Regime II-a).** (I-a) fails by construction. The Kalman update $\hat x^+ = \hat x^- + \eta^\ast \Delta$ undershoots by $(1-\eta^\ast)\Delta$ per event. If events arrive at rate $\nu \gtrsim \alpha_B$, lag accumulates and $\alpha_B R_B \gt \rho_B^{\text{eff}}$ is violated. Result: Regime II-a — destabilization per #der-adversarial-destabilization. Notice: the signal is *within* the model class (Gaussian handles $\pm\Delta$ mathematically), but correction cannot discharge it fast enough.

**Case 4 — Heavy-tailed $\xi_A$ with $\mathbb E[\xi_A^2] \sim r$ but kurtosis $\kappa \to \infty$ (expected Regime II-b).** Mean contribution is fine; the problem is the distribution shape. The Kalman filter — Gaussian-optimal — mis-gains: too aggressive for small events, too conservative for genuine large ones. The per-event KL gap $D_{\text{KL}}(P_\text{true} \Vert P_{\mathcal M_B}) \gt 0$ for any heavy-tailed $P_\text{true}$ against Gaussian. By #def-model-class-fitness, $\mathcal F(\mathcal M_B) \lt 1 - \varepsilon$ with $\varepsilon$ lower-bounded by the KL gap; by #result-structural-adaptation-necessity, no parametric update within $\mathcal M_B$ closes the mismatch. Result: Regime II-b — residuals retain non-Gaussian structure (visible in kurtosis tests); repair requires expanding the model class (e.g., Student-$t$ observation model), not more Kalman tuning.

Each case lands where the classification predicts. The derivation transfers to any recipient architecture in which the underlying AAT quantities are well-defined — this is the scope inherited from #result-sector-persistence-template + #def-model-class-fitness + #def-adaptive-tempo.

### Recovery of Emitter-Side Results

*[Derived (emitter-side-recovery)]*

Each existing emitter-side result is a restriction of the four-regime decomposition:

- **#der-adversarial-destabilization** is Regime II-a integrated over a tempo-proportional event stream. The magnitude-shock sub-regime corresponds directly; the structural-shock II-b subcase is implicit in that segment, collapsed into "adaptive reserve exceeded" but here made explicit.
- **#result-adversarial-tempo-advantage** — superlinear tempo scaling follows from the sector-persistence template's $1/\alpha$ (Model D) vs $1/\sqrt\alpha$ (Model S) applied to Regime II events. The $b$-exponent drops toward zero in the high-$U_{o,B}$ limit because the fraction of $A$'s events landing in Regime II drops (more fall into Regime III).
- **#obs-gated-tempo-advantage** is the recipient-side expression of boundary (I-c): high $U_{o,B}$ pushes events into Regime III where they add to variance without contributing to destabilization.
- **#hyp-symbiogenic-composition** corresponds to asymmetric classification: host's signals to endosymbiont contain high-$\mathcal I$ structure the endosymbiont's class cannot initially represent (Regime II-b for the endosymbiont, forcing structural adaptation toward the host's class); endosymbiont's signals to the host land in Regime I (host absorbs endosymbiont's accumulated structure). Consolidation is the fixed-point where both streams are Regime I.
- **Cooperative signaling** (in #der-team-persistence) — Regime-I events from aligned emitters contribute negatively to $\rho_B^{\text{eff}}$ via the cooperative-action term. The communication-tempo $\nu_{ji}^{\text{comm}} \cdot \eta_{ji}^\ast$ is the rate of Regime-I events times the recipient's informative gain.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Three independent boundaries (sector-region / model-class / observability) | Import from #def-model-class-fitness + #result-sector-persistence-template + #obs-gated-tempo-advantage | Formulation choice (three-way partition; coarser / finer alternatives possible) |
| Four-regime partition (I / II-a / II-b / III) | The three boundaries yield four boundary-state combinations; only four are non-degenerate | Derived from the boundary structure |
| (I-a) / (II-a) boundary at $R_B$ | #result-sector-persistence-template's sector-region radius | Derived |
| (I-b) / (II-b) boundary at $\mathcal F(\mathcal M_B) \cdot \mathcal I_{\max}$ | #def-model-class-fitness + class-capacity normalization | Formulation (the $\mathcal I_{\max}$ normalization is heuristic; sufficient-statistics-span form is cleaner — see Working Notes) |
| (I-c) / (III) boundary at $U_{o,B} \cdot c_\text{floor}$ | #obs-gated-tempo-advantage + detection-theory threshold | Formulation ($c_\text{floor}$ is a detection-power parameter) |
| Regime-typed $\rho_B^{\text{eff}}$ decomposition with negative Regime-I term | Aggregation over event stream using regime classification | Derived (the sign of the Regime-I term is structural, not a choice) |
| Kalman-over-Kalman four-case derivation | Direct application of Kalman gain + sector + KL-gap + SNR analyses | Proved (for the stated case) |
| Recovery of #der-adversarial-destabilization, #hyp-symbiogenic-composition, #obs-gated-tempo-advantage, #der-team-persistence as restrictions | Each emitter-side result is exhibited as a per-regime special case | Derived |
| Non-Gaussian Case 4 derivation (heavy-tailed → II-b via KL gap) | Informal argument grounded in robust-filtering literature (Huber, Masreliez) | Discussion-grade (rigorous version requires per-family KL computation) |
| Class 2 (Partial) approximation with $\kappa_{\text{processing}}$ degradation | Transfer from Class 1 (Separated) with goal-blind-update failure | Formulation (qualitative); exact form requires spelling out the goal-contamination coupling |

## Epistemic Status

*Conditional.* Max attainable: *derived* for the classification structure in Class 1 (Separated) architectures; *exact* for the Kalman-over-Kalman worked case in sub-scope $\alpha$; *robust qualitative* for general sub-scope $\beta$ recipients.

The three boundaries are structurally independent and each is stated in an existing AAT quantity, so the four-regime partition is not ad-hoc; it is forced by the structure of the quantities already in the theory. Within Class 1 (Separated; goal-blind epistemic update per #der-directed-separation) and sub-scope $\alpha$ recipients (Kalman / conjugate-Bayesian / exponential-family / strongly-convex-gradient / linear-PD), the Kalman-over-Kalman derivation transfers with A2' derived per #der-gain-sector-bridge, and each case yields the predicted regime by direct substitution. In sub-scope $\beta$ (PID / rule-based / human-judgment), the classification's form transfers but boundary (I-a) requires per-instantiation verification of the sector bound, inheriting from #result-sector-persistence-template's sub-scope $\beta$ caveat.

**Scope limits.** Class 3 (Coupled) recipients are out of formal scope: the coupled epistemic-purposeful update violates #der-directed-separation, so the regime assignment cannot be cleanly computed against $M_B$ alone. This is `03-llm-core/` territory. Class 2 (Partial) recipients inherit with degradation proportional to $\kappa_{\text{processing}}$ (see `spikes/spike-kappa-hb-operationalization.md`): the Regime-I update may be goal-contaminated, and Regime II-b may be misdiagnosed as II-a or III under goal-blind-update failure. Per-event classification is singular-trajectory-indexed by #scope-agent-identity; aggregation over event streams is deferred to #result-sector-persistence-template.

**What the classification does not claim.** (i) It does not determine *semantic content*: knowing an event is Regime I tells you $B$ will update, not *what* $B$ will believe afterward — that lives in #disc-credit-assignment-boundary's default signal function. (ii) It does not make the four regimes sharp in practice: real recipients' sector regions and class capacities have estimation uncertainty, so borderline events oscillate across boundaries under parameter noise. (iii) It does not replace #result-sector-persistence-template's temporal aggregation; it provides the per-event regime label that feeds into the aggregate disturbance bound.

## Discussion

**Complement, not replacement, of the emitter-side segments.** #der-adversarial-destabilization, #result-adversarial-tempo-advantage, #obs-gated-tempo-advantage, #hyp-symbiogenic-composition, and #der-team-persistence each describe what happens when $A$'s praxis couples into $B$. They collapse the variation into a scalar increment on $B$'s effective disturbance rate. The recipient-side classification decomposes that increment into regime-typed contributions with (importantly) a **signed** Regime-I component. The five emitter-side segments are recovered as restrictions — the classification provides the pattern-recognizer to match the emitter-side optimizer.

**Why II-a vs II-b matters.** Both destabilization regimes manifest as "adaptive reserve exceeded" in the emitter-side view. But the repairs are different: magnitude-shock (II-a) calls for more bandwidth — larger $R_B$, higher $\alpha_B$, faster tempo; structural-shock (II-b) calls for a different model class — an expansion, grafting, or compression in the sense of #result-structural-adaptation-necessity. An organization running rapid-response incident drills against a bureaucratic-process adversary faces II-a and responds with more capacity; the same organization hit by a technology-regime change faces II-b and responds with restructuring. The two produce similar pain signals but admit opposite cures. Collapsing them confuses diagnosis.

**Pairing with #adversarial-edge-targeting (Section III GAP).** The classification provides the recipient-side pattern-recognizer; the emitter-side question — which of $B$'s strategy edges are most valuable for $A$ to attack — provides the adversary-optimization complement. The two compose: the emitter chooses which edge to target; the classification determines what happens at that edge. A particularly sharp move the classification makes visible but the emitter-side formulation hides: the **Regime-I-with-adversarial-content attack** — an emitter who can control the content $y_G$ fed into $B$'s default log-odds signal function (per #disc-credit-assignment-boundary) can choose the sign of $(y_G - \hat P_\Sigma)$ to push $\lambda_k$ in the direction that degrades $\Sigma_B$ most. This is not a destabilizing attack (which lands in Regime II); it is an *informational* attack that exploits $B$'s openness to Regime-I updates to inject misinformation. The emitter-side formulation, which represents coupling as a scalar $\gamma_A$, cannot express the sign lever; the recipient-side decomposition does. The value is maximized at edges with large plan-sensitivity $J_k$ and moderate credence $p_k$ — exactly the edges load-bearing for $\Sigma_B$.

**Agent opacity and the emitter-side regime distribution.** Hafez et al. (2026)'s agent opacity $H_b^B = H(S, A \mid S')$ is primarily *emitter-side*: it gates $A$'s ability to model which of $B$'s regimes a given signal will land in. As $H_b^B \to 0$ the emitter can target specific regimes adversarially; as $H_b^B \to \infty$ the emitter's signals distribute across regimes and the targeting advantage collapses. Formally, $\gamma_A^{\text{effective}} = \gamma_A^{\text{max}} \cdot f(H_b^B)$ with $f$ monotonically decreasing. This is the dual of #obs-gated-tempo-advantage's story: where observation-gates-advantage says the emitter's advantage degrades when its observations of the *environment* are noisy, opacity says the advantage degrades when its observations of *$B$* are noisy. Cooperative signaling is the mirror: low $H_b^B$ (legibility) enables aligned emitters to target signals into $B$'s Regime I. This is #hyp-auftragstaktik-principle's recipient-side translation: shared objectives give $A$ a better model of $B$'s prior and model class, which lets $A$ produce signals that land in $B$'s informative regime.

**Organizational reception intuition.** The four regimes correspond to a familiar organizational diagnostic: (Regime I) *heard* — the organization updated on the relevant edges of its $\Sigma_\text{org}$; (II-a) *shattered by shock* — signal was too large/fast, the organization's correction bandwidth was exceeded; (II-b) *couldn't hear* — signal required reorganization beyond the organization's structural capacity, matching Cohen & Levinthal's (1990) absorptive-capacity framing; (III) *absorbed as fatigue* — signal drained $\Delta\rho^\ast$ without producing structural change, the "death by a thousand memos" pattern. The cross-domain instantiation is cleanest where $\mathcal F(\mathcal M_B)$ maps to absorptive capacity and $U_{o,B}$ to communication-channel quality.

**Future meta-segment candidate.** The recipient-side classification is the *signal-reception* complement to #result-sector-persistence-template's *persistence-under-disturbance* structure. If a future pattern emerges elsewhere (e.g., consolidation dynamics classifying inputs, or a more general theory of inter-agent coupling) a meta-segment `#signal-reception-pattern` could name the recipient-classification shape. Premature at this stage; log as speculation.

## Working Notes

- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Scope-limits paragraph updated (Class 2 fully-merged → Class 3 Coupled; Class 3 partially-modular → Class 2 Partial). What-Is-Derived table updated (Class 3 approximation → Class 2 Partial approximation). The four-regime classification (I / II-a / II-b / III) is recipient-side signal-processing vocabulary — unaffected by the GUC rename. Removed at `candidate` stage per FORMAT.md Gate 4.

- **$\mathcal I_{\max}(\mathcal M_B)$ — replace with sufficient-statistics-span.** The boundary (I-b) uses $\mathcal F(\mathcal M_B) \cdot \mathcal I_{\max}(\mathcal M_B)$ as the class's representational ceiling on per-event information. The cleaner formulation: (I-b) holds iff the event's sufficient statistics for prediction lie in the span of $\mathcal M_B$'s sufficient statistics. For parametric families (exponential families, Gaussian) the explicit form is routine; for non-parametric classes it requires the projection-to-class formalism of #form-information-bottleneck. Worth refining at the next candidacy review.
- **Four regimes vs finer splits.** The partition is the *coarsest* useful split where each regime has a distinct AAT-machinery response. Regime I could split into within-observability / within-calibration (point update vs structural refinement) as a fifth-regime refinement; Regime II-a could split by transient vs sustained dynamics. These duplicate the structural-adaptation hierarchy and are not pursued here.
- **Heavy-tailed derivation rigorization.** The Case-4 argument is informal; a rigorous version would compute the effective Kalman gain under heavy-tailed observation misspecification and show residuals retain signal. This is the robust-filtering territory (Huber, Masreliez) and is standard; the classification does not depend on a specific non-Gaussian family, just on the KL gap being nonzero.
- **Regime II-b as candidate #disc-identifiability-floor Instance 3.** Under a sustained Regime II-b stream, $B$'s $\rho_B^{\text{eff}}$ degrades at a rate lower-bounded by the KL gap between $\mathcal M_B$ and the true event distribution — a quantitative misspecification-cost floor. This is adjacent to #disc-identifiability-floor's "Misspecification-cost quantification" open extension. Worth a focused spike to formalize.
- **Connection to active inference.** Regime II-b corresponds to high-surprise events that exceed the agent's generative model — what AI calls "novel generative context." The classification avoids AI's variational-free-energy-as-master commitment (per the spike-routing cycle, CHANGELOG 2026-05-17); it uses only the information-theoretic content of $\mathcal I(e)$, not the variational machinery.
- **Next spike candidates.** (1) Formalize the $f(H_b^B)$ emitter-side-effect function — tighten the qualitative $\gamma_A \propto f(H_b^B)$ into a derived form (tracked: `TODO.md` "Queued spike work"; cross-referenced in `spikes/PROPOSED.md` Reserved/owned-elsewhere). (2) Formalize Regime II-b misspecification-cost as a structural result ( #disc-identifiability-floor Instance 3 candidate) (tracked: `TODO.md` identifiability-floor queued-spike cluster; same cross-reference). (3) **Resolved — no longer a candidate.** The `#adversarial-edge-targeting` arg-max *is* formally solved in canon: #der-agent-opacity derives it as the 16-cell emitter-recipient composition (a Derived arg-max; the previously-reserved Section-III GAP is filled), with *this* segment supplying the recipient-side four-regime classification that pairs with the emitter side. Scope per #der-agent-opacity Epistemic Status: closed-form under sub-scope-$\alpha$ coupling; general non-convex coupling is per-case optimization, a noted scope caveat, not an open derivation.


---

### Source: `result-adversarial-tempo-advantage.md`

```yaml
---
slug: result-adversarial-tempo-advantage
type: result
status: conditional
depends:
  - hyp-mismatch-dynamics
  - der-adversarial-destabilization
  - result-persistence-condition
stage: draft
---
```


# Result: Adversarial Tempo Advantage

Under adversarial coupling where one agent's actions contribute to the other's disturbance rate, the steady-state mismatch ratio scales superlinearly with the tempo ratio.

## Formal Expression

*[Derived (adversarial-tempo-advantage, from sector-persistence-template + adversarial-destabilization coupling model)]*

**Setup.** Two agents $A, B$ with adaptive tempos $\mathcal T_A, \mathcal T_B$, each instantiating #result-sector-persistence-template with linear correction ($\alpha = \mathcal{T}$). The adversarial coupling of #der-adversarial-destabilization enters each agent's effective disturbance:

$$\rho_A^{\text{eff}} = \rho_{\text{base}} + \gamma_B \cdot \mathcal{T}_B, \qquad \rho_B^{\text{eff}} = \rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A$$

with $\gamma_A, \gamma_B \gt 0$ coupling effectivenesses and $\rho_{\text{base}}$ the shared background rate (asymmetric $\rho_{\text{base}}$ generalizes straightforwardly).

### Model D: Deterministic coupling, $b = 2$

*[Result (adversarial-tempo-advantage, Model D)]*

The template's Model D conclusion $\lVert\delta\rVert_{ss} = \rho^{\text{eff}}/\mathcal{T}$ (linear case, $\alpha = \mathcal{T}$) applied to both agents and ratioed:

$$\frac{\lVert\delta_B\rVert_{ss}}{\lVert\delta_A\rVert_{ss}} = \frac{(\rho_{\text{base}} + \gamma_A \mathcal{T}_A)\,\mathcal{T}_A}{(\rho_{\text{base}} + \gamma_B \mathcal{T}_B)\,\mathcal{T}_B}$$

In the coupling-dominant limit ($\gamma \mathcal{T} \gg \rho_{\text{base}}$) with symmetric coupling ($\gamma_A = \gamma_B$):

$$\frac{\lVert\delta_B\rVert_{ss}}{\lVert\delta_A\rVert_{ss}} \to \left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^2$$

The exponent is $b = 2$: a **squared** tempo advantage. A 2:1 tempo ratio yields a 4:1 mismatch ratio. The faster agent both (a) corrects its own mismatch faster and (b) generates disturbance for the opponent faster — the two effects compound rather than add. $\square$

### Model S: Stochastic coupling, $b = 3/2$

*[Derived (stochastic-tempo-advantage, from sector-persistence-template Model S + coupling)]*

Under Model S the coupling enters the noise scale: $\sigma_B^{\text{eff}} = \sigma_{\text{base}} + \gamma_A \mathcal T_A$. Adversary tempo increases unpredictability, not systematic direction. The template's Model S steady state $\lVert\delta\rVert_{\text{rms}} = \sigma/\sqrt{2\mathcal{T}}$ (linear $\alpha = \mathcal{T}$, scalar $n = 1$) applied to both agents:

$$\frac{\lVert\delta_B\rVert_{\text{rms}}}{\lVert\delta_A\rVert_{\text{rms}}} = \frac{(\sigma_{\text{base}} + \gamma_A \mathcal{T}_A)\sqrt{\mathcal{T}_A}}{(\sigma_{\text{base}} + \gamma_B \mathcal{T}_B)\sqrt{\mathcal{T}_B}}$$

In the coupling-dominant, symmetric limit:

$$\frac{\lVert\delta_B\rVert_{\text{rms}}}{\lVert\delta_A\rVert_{\text{rms}}} \to \left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^{3/2}$$

The exponent is $b = 3/2$. $\square$

**Why 3/2, not 2.** The half-power difference between the template's Model D ($1/\alpha$) and Model S ($1/\sqrt{\alpha}$) scalings propagates through the ratio. Numerator contributes $\mathcal T_A^1$ from the coupling; denominator contributes $\mathcal T_B^{1/2}$ from noise averaging; combined with the $A$-side $1/\mathcal T_A^{1/2}$ gives $\mathcal T_A^{3/2}/\mathcal T_B^{3/2}$.

### Summary of Regime-Dependent Exponents

| Regime | Coupling type | Dominance | Exponent $b$ | Source |
|:---|:---|:---|:---:|:---|
| 1 | Deterministic drift (Model D) | Coupling-dominant | $2$ | Derived above |
| 2 | Stochastic noise (Model S) | Coupling-dominant | $3/2$ | Derived above |
| 3 | Either | Non-coupling-dominant | $\to 1$ (det.) or $\to 1/2$ (stoch.) | Asymptotic limit |

**Regime 3 (non-coupling-dominant).** When $\rho_{\text{base}} \gtrsim \gamma \cdot \mathcal{T}$ (or $\sigma_{\text{base}} \gtrsim \gamma \cdot \mathcal{T}$), the base disturbance dominates and the coupling terms become a perturbation. The mismatch ratio degrades toward $\mathcal T_A / \mathcal T_B$ (linear, $b = 1$) for Model D, or toward $(\mathcal T_A / \mathcal T_B)^{1/2}$ for Model S.

The simulation validation across all three regimes is in #result-adversarial-exponent-regimes.

## Epistemic Status

Both coupling-dominant exponents are *exact* conditional on their respective disturbance models. The squared law ($b = 2$) is *exact* under Model D (deterministic bounded disturbance, GA-2) with coupling-dominant conditions. The $3/2$ law ($b = 3/2$) is *exact* under Model S (stochastic disturbance, GA-2S) with coupling-dominant conditions, derived from the $1/\sqrt{\alpha}$ steady-state scaling (Prop A.1S in #deriv-sector-condition). Both derivations are straightforward algebra from the respective steady-state formulas and the coupling model. The coupling model itself is an *assumption* — the same one used in #der-adversarial-destabilization.

The non-coupling-dominant limits ($b \to 1$ for Model D, $b \to 1/2$ for Model S) are derived asymptotically. The smooth transition between regimes is confirmed by simulation ( #result-adversarial-exponent-regimes) but the interpolation formula is empirical. The transition between regimes is smooth, not sharp.

Max attainable: exact conditional on the disturbance model and coupling model. The result is as strong as its assumptions; no additional work changes the epistemic status without changing the dynamical model.

## Discussion

**Superlinearity is the key result.** The naive expectation — twice as fast yields twice the advantage — is wrong under adversarial coupling. The mechanism is that the faster agent both (a) corrects its own mismatch faster and (b) generates disturbance for the opponent faster. These two effects multiply, producing the squared exponent. Speed advantage is not additive; it compounds.

**Relationship to #der-adversarial-destabilization.** The steady-state mismatch ratio quantifies how much worse the slower agent does *while both agents persist*. The destabilization threshold ( #der-adversarial-destabilization) marks where the slower agent fails entirely — its correction mechanism breaks down. Below the threshold, this segment's mismatch ratio applies. Above it, #der-adversarial-destabilization's Lyapunov divergence takes over. The two results are complementary: this one gives the score; that one gives the game-ending condition.

**Regime dependence is operationally significant.** Whether an adversary's tempo increase produces systematic drift (positional maneuvering, API changes, doctrinal initiative) or unpredictable noise (feints, randomized attacks, market volatility) determines the scaling law. The distinction is not academic — $b = 2$ vs. $b = 3/2$ means a 3:1 tempo ratio yields 9:1 vs. 5.2:1 mismatch ratio. The model predicts that consistent, directional pressure is more effective per unit of tempo than unpredictable disruption.

**Formal analog of OODA-loop observations.** The squared scaling is consistent with Boyd's observation that getting inside the opponent's decision cycle has disproportionate effects. The theory identifies a specific mechanism (multiplicative interaction of correction speed and disturbance generation) and a specific condition (coupling-dominant regime) under which this disproportionality holds. Whether this mechanism is the dominant one in actual adversarial interactions is an empirical question, not a mathematical one.

## Working Notes

- **Channel-independence assumption.** The tempo ratio $\mathcal T_A / \mathcal T_B$ uses scalar tempo, which inherits the channel-independence assumption from #def-adaptive-tempo. When either agent's observation channels are correlated, the additive formula overcounts their tempo, inflating or deflating the ratio and the derived mismatch advantage. The superlinear exponents ($b = 2$, $b = 3/2$) are exact given the scalar tempos; the caveat concerns whether the scalar tempos themselves are accurate.
- The analysis treats each agent's tempo as exogenous — $\mathcal T_A$ does not change in response to $B$'s actions and vice versa. A fully coupled analysis where both agents' mismatch states co-evolve simultaneously (joint Lyapunov function over $(\delta_A, \delta_B)$) is the open extension. The decoupled result is a worst-case bound for the slower agent: in practice, the faster agent may divert adaptive capacity to generating disturbance rather than correcting its own mismatch, creating a self-limiting effect.
- The stochastic exponent ($b = 3/2$) is now derived from both the AR(1) stationary variance (discrete) and the Itô-Lyapunov analysis (continuous, Prop A.1S). The continuous-time analog (Ornstein-Uhlenbeck) gives the same scaling, confirming the asymptotic-scaling claim is the fluid-limit value. The 0.019 gap between the simulation $b = 1.481$ and the asymptotic $b = 3/2$ is *not pure numerical noise*: it is consistent with a derivable finite-$\nu$ correction factor (proportional to $\sqrt{(2c_{\min} - \eta^\ast_A c_{\max}^2)/(2c_{\min} - \eta^\ast_B c_{\max}^2)}$ when $\eta^\ast_A \gt \eta^\ast_B$) that arises because the discrete steady-state variance carries the $O(\eta^\ast c_{\max}^2/c_{\min}^2) = O(c_{\max}^2/(c_{\min}^2 \nu))$ gap from #deriv-discrete-sector-condition. In the fluid limit ($\nu \to \infty$, $\eta^\ast \to 0$ at fixed $\mathcal T$), the correction factor approaches 1 and the asymptotic $b = 3/2$ is recovered exactly. The two models (D and S) are unified by the common sector-condition framework with different disturbance assumptions (GA-2 vs. GA-2S).
- Asymmetric coupling ($\gamma_A \neq \gamma_B$) appears as a multiplicative prefactor $\gamma_A / \gamma_B$ that shifts the mismatch ratio without changing the exponent. An agent with lower tempo but higher coupling effectiveness ($\gamma$) can partially compensate — but the squared dependence on tempo dominates for large tempo ratios.


---

### Source: `result-adversarial-exponent-regimes.md`

```yaml
---
slug: result-adversarial-exponent-regimes
type: result
status: conditional
depends:
  - der-adversarial-destabilization
  - result-adversarial-tempo-advantage
  - def-adaptive-tempo
  - result-persistence-condition
  - deriv-sector-condition
stage: draft
---
```


# Result: Adversarial Exponent Regimes

The adversarial tempo advantage exponent — the power $b$ in $\lVert\delta_B\rVert / \lVert\delta_A\rVert \sim (\mathcal T_A / \mathcal T_B)^b$ — is not a single number. It depends on two structural features of the disturbance: whether the adversarial coupling enters as deterministic drift (Model D) or stochastic noise (Model S), and whether the coupling dominates the base disturbance rate. Three regimes, with the coupling-dominant exponents now derived analytically from the respective disturbance models.

## Formal Expression

*[Derived (adversarial-exponent-regimes, from Model D/S steady states + coupling model; validated by simulation)]*

**Regime 1: Model D (deterministic drift), coupling-dominant.** When adversarial coupling enters as a persistent directional disturbance ($\rho_B = \rho_{\text{base}} + \gamma \cdot \mathcal T_A$, GA-2) and coupling dominates ($\gamma \cdot \mathcal T_B \gg \rho_{\text{base}}$):

$$b = 2 \qquad \text{(simulation: 1.999)}$$

Derived from the Model D steady state $\lVert\delta\rVert_{ss} = \rho/\mathcal{T}$ (Prop A.1). See #result-adversarial-tempo-advantage.

**Regime 2: Model S (stochastic noise), coupling-dominant.** When adversarial coupling enters through the noise scale of zero-mean perturbations ($\sigma_B = \sigma_{\text{base}} + \gamma \cdot \mathcal T_A$, GA-2S) and coupling dominates:

$$b = \frac{3}{2} \qquad \text{(simulation: 1.481)}$$

Derived from the Model S steady state $\lVert\delta\rVert_{\text{rms}} = \sigma_w/\sqrt{2\mathcal{T}}$ (Prop A.1S). The $1/\sqrt{\mathcal{T}}$ scaling (vs. $1/\mathcal{T}$ for Model D) removes one half-power from the denominator, reducing the exponent from 2 to 3/2. See #result-adversarial-tempo-advantage.

**Regime 3: Non-coupling-dominant.** When base disturbance is comparable to or exceeds the adversarial coupling ($\rho_{\text{base}} \gtrsim \gamma \cdot \mathcal T_B$):

$$b \to 1.0 \text{ (Model D)} \quad \text{or} \quad b \to 0.5 \text{ (Model S)}$$

The exponent degrades smoothly as the base-to-coupling ratio increases. The asymptotic limits are derived (they reflect the $1/\mathcal{T}$ or $1/\sqrt{\mathcal{T}}$ scaling without the coupling numerator); the smooth interpolation is empirical.

| $\rho_{\text{base}} / (\gamma \cdot \mathcal T_B)$ | Exponent (deterministic) | Exponent (stochastic) |
|:---:|:---:|:---:|
| 0.002 | 1.999 | 1.481 |
| 0.20 | 1.877 | 1.101 |
| 2.0 | 1.445 | 0.791 |
| 6.3 | 1.213 | 0.577 |

## Epistemic Status

*Exact conditional on disturbance model.* The coupling-dominant exponents are derived, not empirical: $b = 2$ follows from the Model D steady state (Prop A.1) and the coupling model; $b = 3/2$ follows from the Model S steady state (Prop A.1S) and the coupling model. The simulation results (6 variants, multiple parameter sweeps) now serve as validation of the derived exponents, not as their epistemic foundation. The non-coupling-dominant limits ($b \to 1$, $b \to 1/2$) are derived asymptotically; the smooth interpolation between coupling-dominant and non-coupling-dominant is empirical. What remains empirical is whether a given real adversarial interaction is better modeled as Model D or Model S — that is a domain question, not a theory question.

## Discussion

**The disturbance model determines the exponent.** The mismatch dynamics ( #hyp-mismatch-dynamics) now distinguish two disturbance models: Model D (bounded deterministic, GA-2) with steady-state $\rho/\mathcal{T}$, and Model S (stochastic zero-mean, GA-2S) with steady-state $\sigma_w/\sqrt{2\mathcal{T}}$. The different steady-state scaling is the root cause of the different exponents. This resolves the ambiguity that previously existed in the single-$\rho$ formulation.

**Why the squared law held for the coupling-dominance sweep.** In Variant A, the coupling enters as deterministic drift: $\rho_B = \rho_{\text{base}} + \gamma \cdot \mathcal T_A$, and the steady state is $\Vert\delta_B\Vert = \rho_B / \mathcal T_B$. The ratio $\Vert\delta_B\Vert / \Vert\delta_A\Vert$ in the coupling-dominant limit gives $(\mathcal T_A / \mathcal T_B)^2$ directly.

**Nonlinear correction creates thresholds, not lower exponents.** For saturating, sigmoid, and breakdown correction functions under deterministic drift, the issue is not a reduced exponent but a catastrophic divergence when $\rho$ exceeds the correction capacity ($\rho \gt \mathcal{T} \cdot R$). This is exactly the persistence threshold failure ( #result-persistence-condition), observed directly in simulation.

**Domain interpretation.** Whether a given opponent's tempo increase causes deterministic drift or stochastic noise depends on the domain:
- Military: an opponent who maneuvers faster creates systematic positional change (drift, $b \approx 2$)
- Market: a competitor who acts unpredictably creates noise in signals ($b \approx 1.5$)
- Software: a fast-changing API creates systematic drift in the codebase state (drift)
- Adversarial ML: an opponent who varies attack vectors increases observation noise ($b \approx 1.5$)

## Working Notes
- The interpolation between drift and noise regimes (Variant B) shows smooth transition, not a sharp boundary. At mixed drift-noise coupling, the exponent lies between the two asymptotes. The drift fraction $f = \mu / (\mu + \sigma)$ continuously parameterizes the transition.
- The exponent of 1.05 from the original sim2 was not a falsification of Corollary 11.2 — it reflected a stochastic model (noise-variance coupling) tested in a non-coupling-dominant regime. The original simulation was testing the wrong regime for the ODE's prediction.
- Simulation code: `../../spikes/track-b-nonlinear-sims/variants/variant_ab_drift.py`, `variant_cd_regimes.py`. Results: `variant_ab_results.md`, `variant_cd_results.md`.


---

### Source: `obs-gated-tempo-advantage.md`

```yaml
---
slug: obs-gated-tempo-advantage
type: observation
status: empirical
depends:
  - der-adversarial-destabilization
  - emp-update-gain
  - def-adaptive-tempo
stage: draft
---
```


# Observation: Gated Tempo Advantage

Observation noise collapses the adversarial tempo advantage. When agents observe their mismatch through a noisy channel, the faster agent's additional corrections become noisy, partially offsetting its tempo advantage. The optimal gain ( #emp-update-gain) partially restores the advantage but cannot fully recover it.

## Formal Expression

*[Observation (obs-gated-tempo-advantage, from track-b Variant E)]*

In a two-agent adversarial system with observation noise $\sigma_{\text{obs}}$ added to each agent's mismatch signal:

| $\sigma_{\text{obs}}$ | Exponent (fixed $\eta$) | Exponent (optimal $\eta^\ast$) |
|:---:|:---:|:---:|
| 0.00 | 1.04 | 1.04 |
| 0.10 | 1.00 | 0.97 |
| 0.20 | 0.92 | 0.94 |
| 0.50 | 0.60 | 0.63 |
| 1.00 | 0.18 | 0.40 |

At $\sigma_{\text{obs}} = 1.0$ (10x the process noise), the fixed-gain adversarial exponent drops from $\sim 1.0$ to $\sim 0.2$ — tempo advantage nearly vanishes. The Riccati-optimal gain restores it to $\sim 0.4$, more than doubling the advantage but not recovering the noise-free level.

**The mechanism.** When observation noise is high, each correction step adds noise to the mismatch estimate. The faster agent makes more corrections per unit time, each noisy, partially offsetting the benefit of higher tempo. The optimal gain mitigates this by reducing $\eta$ to match the noise level — correcting less aggressively but more accurately.

## Epistemic Status

*Empirical.* Max attainable: derived (the mechanism is analytically tractable via Riccati analysis of noisy AR(1) processes). The observation that noise degrades advantage is confirmed by simulation. The optimal gain's partial restoration is consistent with the uncertainty ratio principle ( #emp-update-gain: $\eta^\ast = U_M / (U_M + U_o)$). The quantitative degradation curve ($b$ vs. $\sigma_{\text{obs}}$) is empirical at these parameters; a general analytical expression would require solving the coupled noisy-AR(1) system.

## Discussion

**Observation quality gates tempo advantage.** Boyd insisted that the quality of Orient (observation processing) matters more than raw OODA speed. The simulation results show a formal analog of this pattern: faster tempo with noisy observations ($\sigma_{\text{obs}}$ high) gives nearly zero advantage over a slower agent with equally noisy observations. The tempo advantage is gated by observation quality — consistent with Boyd's emphasis, though the model captures a specific mechanism (noisy correction steps) rather than the full richness of Orient processing.

**The optimal gain helps most in the moderate-noise regime.** At $\sigma_{\text{obs}} = 0.05$ (observation noise half of process noise), the optimal gain cuts steady-state mismatch by 52% compared to fixed gain. At very high noise, the improvement is less dramatic in absolute terms but more important relatively (0.40 vs. 0.18 exponent).

**Practical implication.** An agent facing an adversary with superior tempo should invest in degrading the adversary's observation quality rather than trying to match their speed. Conversely, an agent with superior tempo should protect its observation channels — the tempo advantage is only as good as the observation quality that supports it.

**Connection to code quality.** In the software domain ( #der-code-quality-as-observation-infrastructure — cross-component reference, see `02-tst-core/`), code quality IS observation infrastructure. A well-structured codebase provides low-noise observations (clear tests, readable code, explicit interfaces). A poorly structured codebase adds observation noise to every development cycle, degrading the developer's effective tempo regardless of how fast they work.

**Recipient-side mechanism.** High $U_{o,B}$ pushes adversarial events below the observability floor (boundary (I-c) in #der-interaction-channel-classification). Events that would otherwise land in Regime II (destabilizing) instead fall into Regime III (ambient noise): they contribute to $\sigma_{w,B}^2$ without producing destabilizing mismatch. The tempo-advantage exponent drops because the *fraction* of $A$'s events landing in Regime II shrinks — $A$'s tempo still matters, but more of it is dissipated into the noise floor. This is the recipient-side expression of the rate boundary.

## Working Notes
- The finding that fixed $\eta = 0.1$ is "remarkably robust" to observation noise (42% degradation at $\sigma_{\text{obs}} = 10 \times q_{\text{env}}$) suggests that conservative gains are a reasonable default for environments with unknown noise levels. The cost of being slightly below optimal is much less than the cost of being above optimal (overcorrection amplifies noise).
- The interaction between observation noise and adversarial exponent regime (drift vs. stochastic) has not been tested. The Variant E results use stochastic coupling only. Whether observation noise degrades the deterministic-drift exponent ($b = 2$) by the same proportion is an open question.
- Simulation code: `../../spikes/track-b-nonlinear-sims/variants/variant_ef_extensions.py`. Results: `variant_ef_results.md`.


---

