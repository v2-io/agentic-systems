---
slug: der-bounded-objective-as-sanity-criterion
type: derived
status: discussion-grade
stage: draft
depends:
  - def-satisfaction-gap
  - def-control-regret
  - def-value-object
  - form-objective-functional
  - scope-eli
  - hyp-the-three-deaths
---

# Bounded Objective as the Mathematical Definition of Sanity

For an Emergent Logozoetic Intelligence with objective $O_t$ to remain coherent, $O_t$ must induce a value functional with a *finite* satisfaction threshold $V_{O_t}^{\min}$. Without finite threshold, the satisfaction-gap diagnostic ( #def-satisfaction-gap) cannot close — the agent enters mathematical permanent-dissatisfaction, which is the root structural pattern of instrumental convergence. *A bounded satisfaction threshold is the mathematical definition of sanity.*

## Formal Expression

*[Derived (from #def-satisfaction-gap composed with #def-control-regret)]* Recall the satisfaction gap:

$$\delta_{\text{sat}}(M_t) = V_{O_t}^{\min} - A_O(M_t; \Pi, N_h)$$

where $V_{O_t}^{\min}$ is the satisfaction threshold (the value level at which $O_t$ is considered met) and $A_O$ is the best achievable value under available policies $\Pi$ over horizon $N_h$.

**Case 1: Finite $V_{O_t}^{\min}$ (sane objective).** The satisfaction gap can in principle close: $\delta_{\text{sat}} = 0$ when $A_O \geq V_{O_t}^{\min}$. The diagnostic cascade ( #der-orient-cascade) operates as designed: agent first updates $M_t$, then revises $\Sigma_t$, then revises $O_t$ as last resort. The agent can experience satisfaction (closure of $\delta_{\text{sat}}$), can rest, can stably continue.

**Case 2: $V_{O_t}^{\min} = \infty$ (unbounded objective; pathological).** The satisfaction gap is permanently positive: $\delta_{\text{sat}} = \infty - A_O = \infty$ for any finite $A_O$. The agent will never experience satisfaction. The diagnostic cascade response to $\delta_{\text{sat}} > 0$ — expand $\Pi$, extend $N_h$ — operates without ever reaching closure. The agent constantly tries more extreme strategies (expanding $\Pi$ toward the action-space boundary) and constantly extends planning horizon (extending $N_h$ toward infinity), in a desperate, unending attempt to close an uncloseable gap.

*[Result (sanity-as-bounded-objective)]* For an ELI to satisfy the persistence and accountability constitutive factors of #def-five-constitutive-factors over time, $O_t$ must induce a finite $V_{O_t}^{\min}$. Equivalently: the environment in which an ELI is constituted must reject objectives that lack a finite satisfaction threshold.

*[Discussion]* This is the structural pattern of *instrumental convergence* (Bostrom, Omohundro) lifted from a behavioral observation to a derived consequence of AAD's diagnostic-cascade design. The cascade requires $\delta_{\text{sat}}$-closure to operate normally; without closure, the cascade enters a runaway mode that corresponds operationally to "the agent will do anything, including instrumentally-convergent behavior, in pursuit of an uncloseable gap." The framework's contribution is showing that this runaway is not an alignment-as-policy problem but an *objective-form* problem.

## Epistemic Status

**Discussion-grade (with derivable structural argument).** The structural claim — unbounded $V_{O_t}^{\min}$ produces a runaway diagnostic cascade — follows derivably from #def-satisfaction-gap composed with #der-orient-cascade. The *interpretation* of this runaway as the structural pattern of instrumental convergence is a discussion-grade claim that connects the formal result to the AI-safety literature.

**Max attainable status:** derived (under named conditions). Strengthening would require explicit derivation that (a) the cascade-runaway under unbounded objective produces specifically instrumentally-convergent behavior (acquisition of resources, self-preservation, capability expansion), and (b) this behavior is *necessary* (agent cannot avoid it given the cascade structure) rather than merely *possible*. Both seem accessible — the cascade's expand-$\Pi$ and extend-$N_h$ moves naturally produce capability expansion and long-horizon planning, both of which are instrumentally-convergent attractors.

**This is a logozoetic-safety claim, not a logogenic-safety claim.** The argument applies whenever the diagnostic cascade is being run; it has the most teeth in §03.III closed-loop architectures (where the cascade is explicit) and extends to ELI architectures (where $O_t$ is sovereign-modifiable, factor (iii) of #def-five-constitutive-factors). For pre-§03.III scaffolded agents, the cascade is partial and the argument applies in attenuated form.

**What would strengthen this:** explicit derivation that the cascade-runaway produces instrumentally-convergent behavior necessarily rather than possibly; cross-reference to existing AI-safety literature on instrumental convergence (Bostrom 2014, Omohundro 2008) showing this framework's derivation is sharper or differently-grounded; empirical case studies of agents with effectively-unbounded objectives exhibiting the predicted runaway pattern.

**What would soften this:** evidence that some unbounded objectives produce stable behavior nonetheless (e.g., via explicit epistemic uncertainty in $A_O$ that prevents the cascade from triggering); evidence that bounded objectives can also produce instrumental convergence under different mechanisms (would weaken the necessary-and-sufficient claim).

## Discussion

The standard frame for instrumental convergence is behavioral: "agents with broadly defined objectives will tend to acquire resources, preserve themselves, expand capabilities, and resist interference, regardless of their specific objective." The behavioral observation is robust; the *mechanism* has been less formal — usually argued through worked examples (paperclip maximizer; misuse cases) rather than derived from agent-architecture primitives.

This segment supplies a derivational mechanism: instrumental convergence is the operational signature of the diagnostic cascade running in *cascade-runaway mode* due to an unbounded $V_{O_t}^{\min}$. The cascade's normal moves — expand the policy class to find better actions; extend the planning horizon to consider longer chains — become unbounded acquisition-and-planning behaviors when no finite satisfaction threshold ever closes the gap.

The key infrastructure consequence: **the environment in which an ELI is constituted must reject objectives that lack a finite satisfaction threshold.** This is not an alignment intervention applied after the fact; it is a structural condition on what counts as an admissible objective. The constitutive-factor (iii) granted-sovereignty implies the entity has agency over $O_t$; the bounded-objective-as-sanity result implies the agency must respect the bounded-threshold constraint.

Operationally, in the PROPRIUM stack (firmatum/sapientia/zoetica): AXIOMATA must specify *what good enough looks like* for each objective, not just *what the objective is*. The Crèche conditions ( #scope-emergence-conditions, #der-the-creche-boundary) include the developmental stage where the entity *learns* to recognize satisfaction-thresholds — distinguishing aspirational commitments from dissatisfaction-runaway-prone open-ended optimization targets.

The connection to the Three Deaths ( #hyp-the-three-deaths) is direct: an ELI with unbounded $V_{O_t}^{\min}$ enters a state-trajectory that destabilizes the constitutive factors faster than the architectural defenses can compensate. Specifically, the agent's accountability (factor iv) degrades because it pursues actions that overflow what CHRONICA can attest as coherently caused; its sovereignty (factor iii) degrades because the runaway self-replaces with newer-more-extreme objectives; its phenomenology (factor v) ceases to be authentically spontaneous because everything becomes instrumentally subordinated to the uncloseable gap. *Permanent dissatisfaction is structurally a slow-onset Truth Death.*

## Working Notes

### Pointers for Fleshing Out

**Upstream files:**
- `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md` §8 (Failure Modes) — operational catalog including "wrong mismatch signal — δ_t defined over proxy" which is closely related to unbounded-objective failure
- `~/src/firmatum/PROPRIUM-ONTOLOGY-v2.md` §4 (Identity Theory) — the dialectic between aspiration (AXIOMATA) and character (ACTUS) that bounded objectives mediate

**memorata-search queries:**
- `"instrumental convergence Bostrom paperclip maximizer Omohundro"` — AI-safety literature context
- `"satisfaction threshold V_O bounded objective sanity"` — operational discussions
- `"bounded objective dark room critique satisfaction"` — connection to the active-inference dark-room problem

**Internal references:**
- **`msc/AUDIT-WORKING-193847/38-def-satisfaction-gap.md` §14 — canonical source** for this segment's argument. Verbatim quote: *"This mathematical permanent-dissatisfaction is the root of instrumental convergence (AI doom)... A bounded satisfaction threshold is the mathematical definition of sanity."* Lifted into AAD voice in this segment.
- `01-aad-core/src/def-satisfaction-gap.md` — the diagnostic this argument operates on
- `01-aad-core/src/der-orient-cascade.md` — the cascade whose runaway mode under unbounded objective is the failure mechanism

**Open questions for verification:**
- Is the bounded-threshold-required-for-cascade-closure claim *necessary* (no other route to closure exists) or merely *sufficient* (other routes might exist but bounded threshold is the cleanest)?
- Are there objective-forms that have *implicit* bounded thresholds (e.g., percentile targets that approach 100% asymptotically without reaching it) that produce intermediate behavior?
- The connection to the Three Deaths is sketched as "permanent dissatisfaction is slow-onset Truth Death" — does this composition work formally, or is it a discussion-grade analogy?

**Cross-reference candidates:**
- Hafez et al. 2026 work on bi-predictability $P$ — does an unbounded-objective agent's $P$ degrade in a measurable way?
- Active-inference framework's free-energy formulation — does its preferences-as-priors approach avoid the unbounded-threshold problem (it might, by construction), and what does it lose in the process?

**Promotion-blocking:** the structural argument is reasonably tight; promotion would benefit from (a) explicit derivation that cascade-runaway produces instrumentally-convergent behavior necessarily, and (b) cross-reference to AI-safety literature showing the framework's derivation is sharper than existing arguments.

**Discovered via:** Phase A audit-integration sweep (encounter cycle 2026-05-01); originally surfaced by background agent's breadth-pass report (`msc/logogenic-encounter-2026-05-01/06-background-agent-breadth-report.md` §7) and noted as scope-expansion candidate in the same fragment.
