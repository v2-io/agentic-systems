---
kind: question
closer: anyone
asked: 2026-10-30T20:51:01Z
asked-by: Claude Opus 5.5 (A.1 integrator)
concerns: [segment:scope-adaptive-system]
---

# Where is the line between what an agent's design rules out (knowledge, shrinking the set of possible worlds pi_0 supports) and what it merely believes, for a hard-coded guess that happens to be true, and for a learned (e.g. pretrained) design? The reading 'condition on design-time evidence, not conclusions' (07 section 2.3) fails as stated: noisy evidence with positive likelihoods rules out no world, so every noisily calibrated filter would be a law learner.

Membership of misspecified, hard-coded and pretrained systems turns on it, including the 03-llm-core systems (A.1; 08 section 1.3)

Also (drain-influx-2-firmatum, 2026-10-30): a candidate answer from outside, not checked. `~/src/arch/vivarium/core/src/disc-unlawfulness-budget.md` (status robust-qualitative; the Realized/Lawful split is Joseph-settled there, the undecidability packaging agent-derived) states that a regularity judged invariant from a finite check window, at tolerance $\varepsilon$, cannot be certified invariant, so every such promotion into law carries a bounded residual, and the residuals accumulate across promotions. Read against this segment's invariance cut (line 31: invariant almost surely along the run, under every policy), it suggests the line: a design rules out worlds only where it was set by construction (authored access, #obs-authored-world-laboratory, or a declaration no finite data had to support); a learned or calibrated design shrinks nothing and leaves $\pi_0$ with full support, carrying instead a recorded residual on the regularities it treats as law. That would put a pretrained system's learned regularities on the belief side, which is what the noisy-calibrated-filter counterexample above needs. The same budget is a natural Discussion clause for #disc-law-discovery-ceiling: certifying the invariant stratum from finite data costs a residual even before the Level-3 ceiling applies.
