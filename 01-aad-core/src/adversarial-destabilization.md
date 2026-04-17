---
slug: adversarial-destabilization
type: derived
status: conditional
depends:
  - sector-condition-stability
  - sector-condition-derivation
  - adaptive-tempo
stage: draft
---

# Derived: Adversarial Destabilization

When two agents are coupled such that one's praxis contributes to the other's disturbance rate, the faster agent can generate aporia in the target faster than the target's epistrophe can resolve it — driving the target outside its invariant region and causing the correction mechanism to break down entirely.

## Formal Expression

*[Derived (adversarial-destabilization, from sector-condition-stability)]*

**Setup.** Let both agents $A$ and $B$ satisfy the sector condition (A1, A2', A3 from #sector-condition-derivation) with respective parameters $(\alpha_A, R_A, \rho_{A,\text{base}})$ and $(\alpha_B, R_B, \rho_{B,\text{base}})$. The coupling:

*[Assumption (Coupling Model)]*

$$\rho_B = \rho_{B,\text{base}} + \gamma_A \cdot \mathcal{T}_A$$

where $\gamma_A \gt 0$ represents the effectiveness of $A$'s actions at disrupting $B$'s environment.

**Result.** $B$'s ultimately bounded radius under coupled dynamics is:

$$R^*_B = \frac{\rho_{B,\text{base}} + \gamma_A \cdot \mathcal{T}_A}{\alpha_B}$$

$B$ diverges (exits its sector-condition region) when $R^\ast_B \gt R_B$, i.e., when:

$$\gamma_A \cdot \mathcal{T}_A \gt \alpha_B R_B - \rho_{B,\text{base}} = \Delta\rho^*_B$$

That is:

$$\mathcal{T}_A \gt \frac{\Delta\rho^*_B}{\gamma_A}$$

Symmetrically, $B$ destabilizes $A$ when $\mathcal{T}_B \gt \Delta\rho^\ast_A / \gamma_B$.

The adversarial outcome depends on whether either agent can push the other past its stability limit. $\square$

**Interpretation.** "Getting inside the opponent's OODA loop" has a precise Lyapunov characterization: Agent $A$ destabilizes Agent $B$ when $A$'s praxis, multiplied by coupling effectiveness, generates aporia in $B$ faster than $B$'s epistrophe can resolve it — specifically, when $A$'s tempo times coupling exceeds $B$'s adaptive reserve $\Delta\rho^\ast_B$. This captures:

- **Asymmetric coupling** ($\gamma_A \neq \gamma_B$): an agent with lower tempo but higher coupling effectiveness can still win.
- **Finite reserves**: an agent with very high $\mathcal{T}$ but operating near its model-class limit ($\Delta\rho^\ast$ small) is vulnerable despite high tempo.
- **Structural collapse**: when $R^\ast_B \gt R_B$, the failure mode is not merely "large mismatch" but "correction mechanism breakdown" — connecting to #structural-adaptation-necessity.

### Corollary: The Effects Spiral

When Agent $B$ is driven past its stability boundary ($R^\ast_B \gt R_B$), and $B$'s degrading model causes $B$'s actions to become erratic in a way that increases $A$'s coupling effectiveness ($\gamma_A$ increases with $\Vert\delta_B\Vert$), the result is a positive-feedback Lyapunov instability:

*[Discussion — Mechanism Schematic]*

$$\Vert\delta_B\Vert \uparrow \;\Rightarrow\; B\text{'s actions become erratic} \;\Rightarrow\; \gamma_A \uparrow \;\Rightarrow\; \rho_B \uparrow \;\Rightarrow\; \Vert\delta_B\Vert \uparrow$$

With $\gamma_A$ now an increasing function of $\Vert\delta_B\Vert$, the disturbance term in $B$'s dynamics grows superlinearly. $\dot{V}_B \gt 0$ and increasing — mismatch accelerates away from the stability region. The spiral terminates only when $B$ undergoes structural adaptation ( #structural-adaptation-necessity — changing the model class) or ceases to function as an adaptive agent entirely.

## Epistemic Status

The destabilization threshold is *exact* under the coupling model (which treats $\mathcal{T}_A$ as exogenous). The coupling model itself is an *assumption* — it decouples the agents rather than modeling the fully coupled dynamical system where both agents' mismatch states co-evolve. The analysis therefore characterizes the *destabilization threshold* (the conditions under which $A$ *can* push $B$ past its stability boundary) rather than the full transient dynamics. This is a worst-case bound, treating $A$ as operating at its steady-state tempo.

The effects spiral (corollary) is *discussion-grade* — the positive-feedback mechanism is qualitatively clear, but formalizing the $\gamma_A(\Vert\delta_B\Vert)$ functional form and proving instability under it requires specifying how an agent's degrading model affects its action quality, which the theory does not yet formalize.

A full coupled Lyapunov analysis with a joint function $V(\delta_A, \delta_B)$ would capture mutual feedback effects but requires specifying how each agent's mismatch state affects the other's disturbance in real time — an open extension.

## Discussion

**Destabilization vs. steady-state ratio.** The destabilization threshold is a failure of *structural persistence* (see Persistence in `LEXICON.md`) — the point where the correction machinery can no longer outpace the adversarially amplified disturbance. An adversary does not need to attack operational persistence (pushing the target near its boundary) or continuity persistence (disrupting identity) directly; destroying structural persistence is sufficient, because without it, operational persistence degrades to zero and the agent ceases to function regardless of its continuity stance. The linear analysis in #mismatch-dynamics gives the steady-state mismatch ratio under coupling: a quantitative result about how much worse $B$ does. This segment gives the qualitative result: under what conditions does $B$ *fail entirely*, not merely fall behind. The linear analysis tells you the score; the Lyapunov analysis tells you when the game is over.

**Connection to #adversarial-tempo-advantage.** The simulation results show the tempo advantage is superlinear (exponent $\approx 2$ in pure adversarial regimes). This Lyapunov result explains WHY: the destabilization threshold creates a phase transition — below it, $B$ persists (possibly with degraded performance); above it, $B$'s correction mechanism collapses entirely, and the effects spiral accelerates the collapse.

**Agent opacity and coupling effectiveness.** $\gamma_A$ is stated as a parameter but its determinants are not decomposed. One key factor is how *legible* or *opaque* the target agent $B$ is to the adversary $A$. We adopt from Hafez et al. (2026) the backward predictive uncertainty $H_b = H(S, A \mid S')$ as a measure of agent opacity — how many distinct (state, action) pairs produce indistinguishable environment transitions. High $H_b$ means the agent is opaque; low $H_b$ means it is legible. In adversarial settings, $B$'s opacity directly affects $A$'s ability to model $B$'s correction function: low $H_b^{(B)}$ (transparent target) enables targeted disruption that maximizes $\gamma_A$, while high $H_b^{(B)}$ forces $A$ to act against an uncertain model, reducing effective $\gamma_A$. Symmetrically, high $H_b^{(A)}$ (opaque adversary) degrades $B$'s ability to anticipate $A$'s disruptions — increasing the effective observation uncertainty $U_o$ in $B$'s model of $A$. The coupling effectiveness is thus modulated by opacity in both directions: $\gamma_A \propto 1/H_b^{(A)} \cdot 1/H_b^{(B)}$ is a qualitative relationship (precise functional form is open). $H_b$ is the formal dual of observation quality $U_o$: where $U_o$ characterizes how well the agent sees the world, $H_b$ characterizes how well the world sees the agent. See the planned #agent-opacity segment for the formal definition and its role in cooperative coordination ( #team-persistence), where low $H_b$ (legibility) enables allies to coordinate without explicit communication.

**Connection to Miller's extreme transition motif.** The effects spiral has a constructive counterpart: in Miller's (2022) coevolving automata model, the same self-reinforcing coupling mechanism drives *regime transitions* rather than collapse. An environmentally neutral variant accumulates through drift, creating a niche that a mutant in the opposing population exploits — a positive-feedback cascade that rapidly transforms both populations. The Lyapunov coupling model applies to both: destructive coupling (this segment) increases $\rho$, constructive coupling ( #team-persistence) decreases it. The difference is sign, not structure. The endogenous emergence of coupling — where $\gamma$ changes as population composition shifts — is the critical extension needed to formalize the full transition motif. See `msc/spike-miller-act-bridge.md` §6.2 and `msc/spike-neutral-drift-lyapunov.md`.

## Working Notes

- The decoupled analysis (treating $\mathcal{T}_A$ as exogenous) is conservative — it's the best case for $A$. In a fully coupled system, $A$'s actions against $B$ may divert adaptive capacity from $A$'s own mismatch correction, creating a self-limiting effect. The coupled Lyapunov analysis is the open problem.
- $\gamma_A$ is the product of coupling strength, observability, and action impact — it captures the full spectrum from tightly coupled (direct disruption) to loosely coupled (indirect environmental effects). In the software domain, coupling is precisely measurable from the dependency graph ( #system-coupling).
- The effects spiral is the formal analog of Boyd's cascading disorientation of the slower adversary — the same structural pattern (tempo advantage → destabilization → accelerating breakdown) appears in the Lyapunov analysis. The model captures the pattern; whether it captures the actual mechanisms of human disorientation is an empirical question, not a mathematical one. Future work should formalize the $\gamma_A(\Vert\delta_B\Vert)$ relationship to make the spiral a result rather than a discussion-grade observation.

*(Descended from TFT Appendix A, Prop A.3 and Cor A.3.1.)*
