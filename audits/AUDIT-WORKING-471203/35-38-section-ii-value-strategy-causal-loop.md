# Reflection: §II value-object / strategy / causal-hierarchy / loop-access (4 segments)

Covers `#def-value-object`, `#def-strategy-dimension`, `#der-causal-hierarchy-requirement`, `#der-loop-interventional-access`.

## Status table

| Slug | Stage | Status | Type |
|------|-------|--------|------|
| `def-value-object` | deps-verified | exact | definition |
| `def-strategy-dimension` | deps-verified | axiomatic | definition |
| `der-causal-hierarchy-requirement` | deps-verified | exact | derived |
| `der-loop-interventional-access` | draft | exact | derived |

All depends upstream. **No "(Descended from TF-XX)"** annotations in this batch.

## Predictions vs evidence

I had predicted: $V_O / Q_O$ as horizon/policy-conditioned value; $G_t = (O_t, \Sigma_t)$ split with $\Sigma_t$ as causal DAG; CHT application giving Level-2 requirement for $Q_O$; loop-as-Level-2-engine derivation. Got essentially all of these, with **substantially more structure than I'd predicted** in two places:

1. **The C1/C2/C3 convention hierarchy** in `#def-value-object` (one-step / receding-horizon / Bellman) with monotonicity result $A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$ and honest framing that the *convention is part of the measurement*. C1 as canonical default.

2. **The "Honest credit" paragraph in `#der-loop-interventional-access`** explicitly acknowledging that the action-perception-loop observation is implicit in active inference (Friston et al. 2017) and the cybernetic lineage (Wiener, Conant-Ashby), and naming three specific AAD-distinctive moves: Bareinboim-hierarchy connection, regime-indexed identification strength, explicit scope honesty.

The "Honest credit" framing is exactly the prior-art-integration discipline operating correctly — adopt the observation, cite the lineage, name what's distinctive.

## Cross-segment consistency

The `(PI)` axiom from `#scope-agent-identity` (segment 30) is now properly invoked in `#der-loop-interventional-access`'s "Why the loop data is genuinely interventional — the singular-trajectory ground" paragraph, with `scope-agent-identity` *declared in depends*. This resolves the depends-incompleteness concern I had flagged about (PI) usage — at least for this segment.

The Hafez 2026 IDT reference appears in both `#def-agent-spectrum` and `#der-causal-hierarchy-requirement` with consistent framing (89% vs 44% perturbation detection). Good cross-segment consistency.

The strategic-composition reference from `#der-directed-separation`'s composite-level inheritance result is implicit in `#der-loop-interventional-access`'s "Modes of deployment" paragraph (Mode 2: observer-on-sub-agent) — the segments are reinforcing each other across §II's architectural backbone.

## Math verification

**C1/C2/C3 monotonicity:** $A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$ follows from "better continuation policy yields weakly higher expected value." The argument is correct. The corollary on $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ orderings is also straightforward (since $\delta_{\text{sat}} = V^{\min} - A_O$, higher $A_O$ → lower $\delta_{\text{sat}}$).

**Causal-validity-of-$Q_O$:** $Q_O$ uses $do(a_t = a)$ explicitly + $\pi_{\text{cont}}$ as parameter. Under directed separation (Class 1), $M_t$ updates independently of $G_t$ and $Q_O$ depends on $M_t$ alone as state variable. For Class 2, $M_t$ carries goal-conditioned bias and causal validity degrades. The segment is honest about this layering.

**CHT application:** $Q_O$ is interventional; CHT (Bareinboim et al. 2022) says Level 2 not in general computable from Level 1 data; therefore agents that must learn $Q_O$ need Level 2 access. Direct logical chain.

**Loop generates interventional data:** $a_t$ causally precedes $o_{t+1}$ (from `#post-causal-structure`'s temporal-precedence postulate). The pair $(a_t, o_{t+1})$ is intervention-produced because the agent executed $a_t$. **Critical caveat explicitly noted:** intervention-produced data ≠ cleanly identified $do$-estimates. Coverage, confounding, delay, partial observability remain. The strength of identification varies by regime (A/B/C — intervention-rich / partial / observation-only).

This caveat is exactly what would otherwise weaken the claim. The framework states the loop produces *intervention-character* data, then carefully separates this from *clean causal identification*. The honest split prevents the kind of overclaim Bruineberg et al. 2022 critiqued.

## Substantive observations

**1. The convention-hierarchy framing is sophisticated.** Most decision-theoretic treatments pick one continuation convention and run with it. AAD names three (with monotonicity) and explicitly states "the convention is part of the measurement, not just the computation." This means downstream segments using $\delta_{\text{sat}}$ or $\delta_{\text{regret}}$ should specify their convention. Whether this is honored downstream is a Phase-2 check.

**2. The strategy-dimension type-error correction.** The Discussion says "Earlier formulations used $\delta_{\text{goal}} = G_t - M_t$ as a goal mismatch signal. When $\Sigma_t$ is a DAG, this is a type error — you cannot subtract a graph from a state vector." The framework now uses `#def-satisfaction-gap` and `#def-control-regret` as properly typed gap measures. Good — this is the kind of structural correction that compounds.

**3. The "modes of deployment" generalization in `#der-loop-interventional-access`.** Two semantically distinct interventional mechanisms sharing the Pearl-$do$ structure:
- Mode 1: agent-self-intervention (Instance 1, causal-structure layer)
- Mode 2: observer-on-sub-agent (Instance 3, composition layer)

The pattern is: Level-2 escape from observational-equivalence no-goes via loop-interventional access, with the *specific interventional quantity* varying by layer but the *structural mechanism* shared. This is the additive-coordinate-forcing meta-pattern's cousin: pattern-level unification with semantically-distinct instantiations.

**4. The singular-trajectory grounding.** "Pearl's $do$-operator presumes a definite causal system acted upon; AAD inherits this presumption via the singular-trajectory scope." This ties the interventional-loop claim back to `#scope-agent-identity`'s identity-as-trajectory commitment. The two segments together: trajectory provides the ontological ground; loop provides the interventional mechanism.

**5. The pre-compiled-vs-learning-agent scope narrowing in `#der-causal-hierarchy-requirement`.** Excludes PID, LQR, hardcoded reactive policies — they have *externally supplied* causal mappings. AAD's purposeful-agency machinery is for agents that must *acquire or refine* their causal understanding. This is a clean structural restriction; downstream segments should respect it.

## Candidate observations

**(a) Convention specification propagation.** Phase 2: check whether downstream segments using $\delta_{\text{sat}}$ / $\delta_{\text{regret}}$ specify their convention (C1/C2/C3). If not, the values aren't comparable — this is exactly what `#def-value-object` warns against.

**(b) Hafez 2026 IDT citation.** Appears at least twice (here in `#def-agent-spectrum` and `#der-causal-hierarchy-requirement`). The 89% vs 44% empirical claim should be verified in Phase 2 against the actual Hafez paper / preprint.

**(c) Bareinboim-CHT precise form.** The "Level 2 cannot in general be computed from Level 1" framing is correct in spirit; the precise statement (strict inclusion $\mathcal{L}_1 \subsetneq \mathcal{L}_2$ for almost all SCMs) is the rigorous form. Phase 2 verify.

## Felt value

**High magnitude across the batch.** The "loop as Level 2 engine" framing earns its load-bearing status with the explicit caveats. The convention hierarchy is the kind of disciplinary precision that compounds. The "modes of deployment" structural-pattern observation is sophisticated. The Pearl-vs-Friston, Bareinboim-CHT, and singular-trajectory groundings together give AAD a *defensible* claim to be doing genuinely Level-2 reasoning — not just gesturing at it.

For consciousness-infrastructure work: the "loop compensates for architectural limitations" Working Note is structurally important. An LLM agent (Class 2 internally) can still gain Level 2 access through its action-observation loop, even though its internal architecture isn't designed for causal reasoning. This is the structural justification for tool-using LLM agents being able to do interventional learning despite their attention-mechanism architecture.

## What this batch enables

- A diagnostic vocabulary ($V_O$, $Q_O$, $\delta_{\text{sat}}$, $\delta_{\text{regret}}$ — last two upcoming) with explicit convention-dependence.
- A clean type system for purpose ($O_t$ as evaluation functional, $\Sigma_t$ as structured guidance representation).
- The "loop is Level 2 engine" claim properly defended with honest scope honesty.
- A structural-pattern observation (modes of deployment of loop-interventional-access across identifiability-floor instances).

## Wandering thoughts (collected)

The "Honest credit" paragraph in `#der-loop-interventional-access` is exemplary academic writing. Most frameworks claim novelty for what's actually inherited; AAD names what's inherited (action-perception-loop interventional character) and what's distinctive (Bareinboim-hierarchy lift, regime-indexed identification, explicit scope honesty). This is the prior-art-integration discipline at its best — substantive credit, sharp distinction.

The convention-hierarchy framing has a small philosophical bite: AAD's diagnostics are *measurement-relative*, where the measurement convention is part of the diagnostic's content. Two analyses computing $\delta_{\text{sat}}$ under different conventions aren't disagreeing; they're measuring different things. This is closer to how empirical sciences treat measurement protocols than how mathematics treats theorems. The framework is willing to be measurement-theoretic about its own quantities.

The "modes of deployment" structural pattern (loop-interventional-access deployed differently across identifiability-floor instances) suggests a more general principle: AAD's structural results often have *architectural* content that's invariant across deployment modes plus *instantiation* content that varies by layer. The framework's distinctive contribution may be naming this kind of architecture-vs-instantiation distinction at the meta-level.

A naming-brainstorm seed: "the loop is a Level 2 engine" is a good Brief-style framing. The longer phrase "loop-interventional-access" is the slug-grade name. For framing-level material, "the perpetual experiment" (from the Discussion) might be the most evocative — captures both the interventional character and the continuous nature.

The Hafez IDT empirical finding (89% vs 44%) keeps coming up. If it holds, it's substantial empirical support for the loop-as-Level-2 claim. **High Phase-2 priority.**

Continuing with next §II batch.
