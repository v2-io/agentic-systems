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
- The effects spiral is the formal analog of Boyd's cascading disorientation of the slower adversary — the same structural pattern (tempo advantage → destabilization → accelerating breakdown) appears in the Lyapunov analysis. The model captures the pattern; whether it captures the actual mechanisms of human disorientation is an empirical question, not a mathematical one. Future work should formalize the $\gamma_A(\Vert\delta_B\Vert)$ relationship to make the spiral a result rather than a discussion-grade observation.
