# Spike: Regimes Within Class 2 (Partial Coupling) — A Sub-Typology by Stage × Source × Form

**Date.** 2026-05-22.
**Status.** Landed in canon 2026-05-22 — `#disc-partial-coupling-pathways` (discussion-grade) + `#der-belief-strategy-attractor` (conditional), both at `draft` stage. Working-Notes pointers added to `#der-directed-separation`, `#disc-adversarial-coupling-pressure`, `#der-class-coercion-via-wrapping`, `#def-agent-spectrum`. OUTLINE.md updated. Two follow-on sub-spikes queued for tier-upgrade — see `INTEGRATION.md`. The math reaches *exact* on the two load-bearing structural results (content/process identifiability; source asymmetry) under stated linear-Gaussian + smooth-tilt assumptions; *robust qualitative* on the broader picture; *intuition-only* on prior-art coverage of the specific decomposition.

**Pressure point.** Joseph 2026-05-21: *"does AAT have an intuition yet of potential regimes within Class 2 partially coupled agents? I.e., exactly what constitutes fully-entangled should give some clues as to what can be partially detangled (I would think it might require a more thorough pondering of exactly what kinds of information are being used where in the processing...)"*

The current canon (`#der-directed-separation`) collapses all sub-architectural variation within Class 2 (Partial Coupling) into a single distribution-dependent scalar $\kappa_{\text{processing}} \in (0, 1)$. The scalar is honest about the *degree* of coupling but silent on the *kind*. Joseph's intuition — that understanding fully-entangled (Class 3) should illuminate partial-detanglement (Class 2 sub-types), via *what kinds of information are used where in the processing* — points at a structural decomposition the scalar hides.

## The thesis

Class 2 partial coupling decomposes along three structurally independent axes:

- **Stage** (where in $f_M$'s processing pipeline the goal-state enters): selection, featurization, likelihood evaluation, posterior aggregation, consolidation.
- **Source** (which component of $G_t = (O_t, \Sigma_t)$ does the coupling): $O_t$-source, $\Sigma_t$-source, or $M_t$-self-coupling through prior $G$-coupled updates.
- **Form** (the functional character of the dependency): *content* (additive, separable, post-hoc-debiaseable) vs *process* (multiplicative/compositional, non-separable, requires replacement).

The Class 3 (fully Coupled) limit is the point where *all stages couple, both sources are active, and the form is process*. Class 1 is the opposite limit (no coupling anywhere). Class 2 is everything between, parameterized by the (stage-set, source-set, form-type) tuple.

This is not a re-partition of the Class 1 / 2 / 3 trichotomy. It is a refinement *within* Class 2 — a sub-typology that predicts (i) which repair regime applies (post-hoc debiasing vs stage replacement vs full-agent wrapping); (ii) which dynamical signatures appear (belief-strategy attractors under $\Sigma$-source coupling; not under pure $O$-source); (iii) where the existing adversarial-coupling-pressure mechanisms (`#disc-adversarial-coupling-pressure`) sit in the typology; (iv) which Class 2 sub-types are *coercibly* Class 1 by external wrapping and which are not.

## File layout

| File | Contents |
|---|---|
| `01-setup.md` | The structural question, the canon position, and what this spike adds. |
| `02-formal-decomposition.md` | Pipeline decomposition of $f_M$ into four stages; the (stage × source × form) parameterization; formal definitions of content vs process. |
| `03-derivations.md` | The math, pushed: (a) content/process identifiability theorem; (b) stage-cascade propagation lemma; (c) source-asymmetry result with belief-strategy attractor; (d) composition with the leakage-locus result; (e) wrapping-regime correspondence theorem. |
| `04-canonical-cases.md` | Placement of confirmation bias, motivated reasoning, sunk cost, goal-directed attention, identity-protective consolidation, frame coupling. Tests the typology. |
| `05-relation-to-existing-machinery.md` | How this composes with W₀/W₁/W₂ wrapping, the three adversarial-coupling-pressure mechanisms, the Class-1-by-structure vs by-behavior refinement, the unlanded M4 modularity-state-dynamics meta-segment. |
| `06-edge-cases-and-no-gos.md` | Stress-testing the carve. Cases where stages collapse, where the form distinction fuzzes, where the parameterization is over-fine. Honest record of where the typology might fail. |
| `07-prior-art-followon.md` | Adjacent literatures (active inference, motivated-reasoning, dual-process, Bayesian persuasion). Sub-spike scoping. |
| `INTEGRATION.md` | Recommendation for canon integration — segment shape, placement, scope of changes to existing segments, deferred items. |

## Reader's posture

This spike is the reasoning trail. Per `feedback_math_lives_in_segments.md` and `feedback_segment_voice_not_diff_voice.md`, the math that lands in canon belongs in an appendix segment, not the spike. The integration recommendation in `INTEGRATION.md` specifies what should move where; the body of this spike preserves the development arc (including the dead-ends in `06-`) for future agents who want to see how the structure was found.
