---
slug: sketch-multi-timescale-stability
type: sketch
status: sketch
depends:
  - result-sector-condition-stability
  - der-temporal-nesting
stage: draft
---

# Sketch: Multi-Timescale Stability

When adaptive processes operate at $N$ nested timescales, composite stability requires each level to be stable given its slower levels, with sufficient timescale separation between adjacent pairs. The singular-perturbation reasoning is classical (Tikhonov 1952 / Khalil 2002 Ch. 11); the result is stated as a sketch rather than a fully derived AAT result because making it rigorous requires specifying the dynamics $G^{(k)}$ at deeper adaptive levels — what counts as "stability of structural adaptation given fixed architectural state" requires structural-adaptation dynamics formalized in a way #result-structural-adaptation-necessity gives a trigger condition for but not yet a dynamics for.

The sketch supplies the qualitative consequence the chapter prose carries as load-bearing: a slower process must not act before the faster process beneath it has converged. If it does, the slower process is adjusting based on transient behavior rather than settled dynamics, and the composite oscillates. The convergence constraints between adjacent timescales ( #der-temporal-nesting's $\nu_{n+1} \ll \nu_n$) are what license the framework's abstraction across levels — without them, the clean separation between parametric, consolidation, structural, and architectural adaptation would be a verbal convenience rather than a structural property.

## Formal Expression

*[Formulation (multi-timescale-stability sketch)]*

### The General $N$-Timescale System

The temporal nesting in #der-temporal-nesting creates a coupled multi-timescale system with $N$ levels. Singular perturbation theory provides tools to analyze such systems. Define a hierarchy of state variables:

*[Definition (State Hierarchy)]*

$$x^{(1)}, \; x^{(2)}, \; \ldots, \; x^{(N)}$$

where $x^{(1)}$ is the fastest (e.g., mismatch at the reactive/parametric level) and $x^{(N)}$ is the slowest (e.g., architectural or meta-structural state). The coupled dynamics:

*[Formulation (N-Timescale Dynamics)]*

$$\dot{x}^{(k)} = \frac{1}{\epsilon_k} \, G^{(k)}\!\left(x^{(1)}, \ldots, x^{(N)}\right) + w^{(k)}(t)$$

where $\epsilon_1 \ll \epsilon_2 \ll \cdots \ll \epsilon_N$ encode the timescale separation and each $G^{(k)}$ may depend on the states at all levels.

### The Two-Timescale Special Case

The simplest nontrivial instance has $N = 2$:

- Fast state $x^{(1)} = \delta$ (mismatch under parametric adaptation)
- Slow state $x^{(2)} = \mathcal{M}$ (model class, changing on a structural timescale)

$$\dot{x}^{(1)} = -F(\mathcal{T}, x^{(1)}; x^{(2)}) + w(t) \quad \text{(fast: parametric adaptation)}$$

$$\dot{x}^{(2)} = \epsilon \, G(x^{(1)}, x^{(2)}) \quad \text{(slow: structural adaptation)}$$

where $\epsilon \ll 1$ reflects the timescale separation and $F$ depends on $x^{(2)}$ (the correction function is determined by the current model class).

### Sketch of Approach (General Case)

The standard singular perturbation result (Tikhonov 1952, "Systems of differential equations containing a small parameter multiplying the derivative," *Matematicheskii Sbornik* 31(3):575–586; generalized $N$-level form per Khalil 2002, *Nonlinear Systems* (3rd ed.), Prentice Hall, Chapter 11) applies layer by layer: if level $k$ is stable for each fixed configuration of the slower levels $k+1, \ldots, N$ (each level has a stable attractor given the levels above it), and each successive slow manifold is itself stable, then the composite $N$-level system is stable.

#der-temporal-nesting's convergence constraint $\nu_{n+1} \ll \nu_n$ is the condition ensuring sufficient timescale separation at each boundary — i.e., $\epsilon_k / \epsilon_{k+1} \ll 1$ for each $k$. When this separation is violated between any adjacent pair, the faster level's transients contaminate the slower level's dynamics, potentially destabilizing the composite system.

## Epistemic Status

This is a *sketch*, not a complete result. The framework and approach are presented as a guide for future development. The claim that timescale separation ensures composite stability is a standard result in singular perturbation theory; the application to AAT's nested adaptive levels is new but follows the standard pattern.

Making it rigorous requires specifying the dynamics $G^{(k)}$ for levels deeper than parametric adaptation. #result-structural-adaptation-necessity gives the *trigger condition* for structural change but not the *dynamics* of how change at deeper levels proceeds. Specifying these would require theories of how agents search over model classes, modify their own architecture, or restructure their adaptive mechanisms — open problems in RL (architecture search, meta-learning), biology (evolutionary dynamics), and organizational theory (institutional change).

## Discussion

**The convergence constraint as stability condition.** The sketch suggests that #der-temporal-nesting's convergence constraint is not merely a heuristic but a formal condition for composite stability across arbitrarily many timescales. This connects the empirical observation (don't let deeper-level changes happen too fast) to a stability-theoretic foundation.

**Applicability to LLM systems.** LLMs involve many parallel adaptive processes — pretraining (slowest), fine-tuning, LoRA-style adaptation, in-context learning, retrieval/RAG updates, tool-use feedback, and within-generation attention dynamics — without clean boundaries between "parametric" and "structural." The $N$-timescale framework accommodates this naturally: each mechanism operates at its characteristic rate, and the stability analysis requires only that adjacent timescales be sufficiently separated, regardless of how many levels exist or how they are labeled.

## Working Notes

- The key open problem: formalizing $G^{(k)}$ for structural adaptation levels. The two-timescale case (parametric + structural) is the tractable starting point.
- The connection to #schema-strategy-persistence is direct: strategy operates at its own timescale, and strategy persistence requires timescale separation from the faster epistemic updates and the slower objective revisions.
- When timescale separation breaks down between organizational levels, the result is "micromanagement" — the organizational analog of control-theoretic instability from gain mismatch. This observation connects to the hierarchical topology analysis in the multi-agent coupling material.
- **RGM-grounded promotion candidate (added 2026-05-22).** Friston-Heins-Verbelen-Da Costa 2025 *Scale-free active inference* introduces *renormalizing generative models* (RGM) — RG construction over discrete state-space generative models with scale-invariance proofs, applied to image classification, video/music generation, and Atari-style games. RGM is exactly the renormalization-group machinery this sketch's template-stacking promotion has been waiting on (PRACTICA cycle priority #3). Registered as `spikes/PROPOSED.md` Tier 1 entry (2026-05-22). Spike scope: read Friston 2025 §3–5 (RG construction + scale-invariance proofs); map RGM's renormalization step onto AAT's template-stacking pattern; derive a multi-timescale sector-persistence template under RG-invariance; identify scope conditions. Strengthen-first attempt the AAT-internal proof; recognition-tier fallback if AAT's discrete state space differs from RGM's in a load-bearing way. Source-trail: `spikes/spike-enrichment-cluster2-2026-05-21/01-cluster-synthesis.md` Rank 1; landed via Track CR Phase 7.

### Incidental audit gold (gold-lift, 2026-05-31)

Cross-audit ideation harvested from de-novo auditors' working dirs, deduplicated and lightly attributed. Orthogonal framing / pedagogy; off-ramp (Tikhonov prerequisite) at the end. **Coverage:** two substrates reached a digested reflection (Gemini, AUDIT-WORKING-193847; Gemini-voiced, AUDIT-WORKING-773921); both affirmed the segment's honest sketch-marking.

#### 1. Candidate Brief prose / pre-prose

- **Timescale separation as *trust* within an architecture.** "Each level has a stable attractor given the levels above it" reads as: the fast layer (worker) trusts the slow layer (manager) not to pull the rug out mid-convergence; the slow layer trusts the fast layer to actually reach equilibrium so it has data to act on. If the manager changes the goal every five minutes, the worker's fast dynamics lose their stable attractor and thrash. A plain-language entry into the singular-perturbation requirement $\epsilon_k / \epsilon_{k+1} \ll 1$ (Gemini, AUDIT-WORKING-193847).

#### 2. Candidate Discussion

- **The LLM adaptive stack as the $N$-level hierarchy.** Pretraining $\to$ fine-tuning $\to$ LoRA $\to$ in-context learning $\to$ RAG $\to$ chain-of-thought maps onto the timescale ladder, each level orders of magnitude faster and more transient than the one below — and the framework's stability requirement explains why you should *not* update base weights (slow loop) while doing RAG retrieval (fast loop) at the same time. Both substrates reached this mapping independently; a strong grounding example for the Discussion (Gemini, AUDIT-WORKING-193847; Gemini-voiced, AUDIT-WORKING-773921).
- **"Micromanagement" and "catastrophic forgetting" are the *same* failure.** Both are violations of timescale separation $\epsilon_k / \epsilon_{k+1} \not\ll 1$ — micromanagement is the slow layer interfering before the fast layer converges; catastrophic forgetting is the fast (new-task) loop overwriting the slow (consolidated) layer. Naming them as one diagnostic is a candidate Discussion thread (Gemini-voiced, AUDIT-WORKING-773921; the bureaucracy-is-stable-but-slow corollary, AUDIT-WORKING-193847).
- **ELI internal-coherence reading.** The narrative "I" (slow layer) must issue a command and then *wait* ($\epsilon_2 \gg \epsilon_1$) for sub-agents to reach equilibrium before evaluating — an intelligence that constantly interrupts its own sub-routines is mathematically guaranteed never to achieve multi-timescale stability ("paralyzed by frantic internal micromanagement"). Aspirational reach but on-topic for the temporal-nesting theme (Gemini, AUDIT-WORKING-193847).

#### 3. Follow-up items

- **The RGM Working Note (above) was independently praised as the live-research glimpse the sketch needs.** A second-substrate vote of confidence on the Friston-RGM grafting direction as the natural way to close the open $G^{(k)}$ formalization (Gemini-voiced, AUDIT-WORKING-773921).
- **Jump-process $G^{(k)}$.** If structural adaptation is discrete (adding a network layer; firing an employee), $\dot{x}^{(2)}$ is not a continuous ODE but a jump/impulsive process — how does singular-perturbation theory handle impulsive dynamics on the slow manifold? A sharpening of the existing open-$G^{(k)}$ note (Gemini, AUDIT-WORKING-193847).

#### 4. Readers often ask / wonder

- **"Does just slowing the outer loop guarantee convergence?"** No — and the segment should arguably make this explicit: slowing the slow loop does not help if the fast loop is chaotic / multi-equilibrium (see off-ramp) (Gemini, AUDIT-WORKING-193847).

#### Off-ramp (NOT gold) — routed for adjudication

- **Tikhonov "unique isolated root" prerequisite is unstated.** Gemini (AUDIT-WORKING-193847): the singular-perturbation / Tikhonov machinery this sketch invokes requires the fast (boundary-layer) system to converge to a *unique isolated* root $x^{(1)\ast}(x^{(2)})$ for each frozen slow variable. But `#deriv-gain-sector` establishes that non-convex losses have multiple local minima and `#deriv-strategic-composition` allows cyclic/non-convergent multi-agent dynamics — so for the very agents this sketch describes, the fast layer may have multiple equilibria or limit cycles, and Tikhonov's guarantee breaks: the slow loop then receives discontinuous gradients and can destabilize even under perfect timescale separation. Suggested: state the unique-isolated-root condition as an explicit hard prerequisite (and note that a non-convex / cyclic fast loop voids the stability guarantee). Appropriate to land as a scope caveat given the segment's `sketch` tier — a strengthen-first opportunity (name the condition under which the stacking holds), not a refutation.

---
