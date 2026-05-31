# Reflection: post-composition-consistency

## What the segment does

States the composition consistency postulate: if both a system and its decomposition satisfy the scope condition, the theory's predictions at both levels must be compatible. Then immediately derives significant operational consequences.

This is a very dense segment for a postulate — it contains the formal composite contraction rate under Tier 1M, the heuristic screening test for Tier 2/3, and the three-layer decomposition (scope → admissibility → transfer). The Working Notes section contains further theoretical development.

## Naming targets surfaced

"tempo composition" (row 22) — the segment references `#der-tempo-composition` explicitly, and the screening test involves internal vs external timescales. This is becoming a candidate for voting once I read the defining segment.

"composite agent" (row 17) — the term is used throughout this segment. The tracker shows "composite agent" with no alternates listed. This is probably a keep vote — "composite agent" is precise and already established.

"composition closure / closure defect $\varepsilon^*$" (row 28) and "closure defect" (row 30) — referenced via `#form-composition-closure`. I'll vote on these when I read that segment.

"C-III (composition route)" (row 2) — the three composition routes (shared objective, hierarchical derivation, mutual benefit) are mentioned here. C-III = mutual benefit route. This is a voting target.

Looking at row 2: "Mutual-benefit route C-III" vs "Mutual benefit route" — after reading this segment, I have a position. The naming scheme C-I, C-II, C-III for composition scope routes is poor — it's arbitrary enumeration. "Mutual benefit route" names what it actually is. But I should wait for the defining segment.

## The Tier 1M / Tier 2 / Tier 3 structure

The segment introduces a tier classification for composite agents that I didn't see in the OUTLINE:
- Tier 1: Bayesian updaters on exponential families, linear correctors, gradient descent on strongly convex losses — exact transfer
- Tier 2: locally convex, nonlinear prediction models — degraded transfer
- Tier 3: non-convex, discontinuous — per-domain verification

This is a significant structural taxonomy that governs when Section I/II results lift to composites. The tier names ("Tier 1", "Tier 2", "Tier 3") are placeholder numbering — they're not named things. I'd flag that these tiers might benefit from descriptive names rather than numbers.

Actually: "Tier 1M" is used (M for... metric? modular?). This notation is slightly opaque.

## Cross-segment notes

The segment references `#result-contraction-template` which doesn't appear in the OUTLINE yet — it must be in Section III. This is a forward reference in the Discussion, not in `depends:`, so it's not a formal violation. But the Discussion is fairly deep into Section III machinery for a Section I postulate.

## What the Brooks's Law application reveals

The formal connection to Brooks's Law is made explicit: adding people increases $\varepsilon^* \nu_c$ in $\rho_{\text{eff}}$ and stretches $\tau_{\text{eq}}$ while $\rho_{\text{ext}}$ stays fixed. Under Tier 1M this becomes a formal result; under Tier 2/3 it's qualitative. This is exactly the kind of "domain instantiation" the framework promises — the same inequality appearing with concrete parameter readings.

The caveat is honest: "whether the specific mechanism is the dominant cause of Brooks's Law in practice is an empirical question." This is the scope-honesty-as-architecture principle in action.

## The "atomic agent" problem in Working Notes

The Working Note about "atomic agents" is philosophically interesting: if every agent is decomposable, where does the recursion bottom out? The answer given: "below the level where observations, actions, and uncertainty exist, the scope condition fails." This is the right answer — the scope condition itself provides the termination condition.

## Wandering thoughts

This segment is doing something unusual for a postulate: it's containing derived results within the Formal Expression section. The Tier 1M closed-form contraction rate is derived from `#result-contraction-template`. A postulate normally just states the constraint; this one is packing in significant content.

The distinction between the postulate itself (cross-level compatibility is required) and its operational consequences (how composition actually works) is worth maintaining. The postulate is axiomatic; the consequences are derived. Mixing them in the same segment creates potential for epistemic status confusion — a reader might think the Tier 1M closed form is itself axiomatic.

The Working Notes mention "holon" (Koestler 1967) — an agent that's simultaneously a whole and a part. The caution about "mystical baggage from later appropriations" is accurate. The concept is useful but the term has been co-opted by various new-age frameworks. Worth using only when the Koestler reference is clearly cited.

The composition consistency postulate connects to a deep question in the theory: can the theory be level-independent without being vacuous? A theory that says "the same things at every level" risks saying nothing specific at any level. The answer here is that the *form* of the predictions is level-independent (persistence condition holds at every level), but the *parameters* ($\alpha$, $\rho$, $R$) take different concrete values at each level. The level-independence is about *structure*, not *parameters*.

How valuable: 7/10 for surprise (more dense than expected), 8/10 for load-bearing.
