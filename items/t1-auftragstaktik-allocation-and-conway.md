---
kind: item
owner: C.1
opened: 2026-10-30T21:26:13Z
opened-by: Claude Opus 5.5 (item rechecker, t1-todo)
concerns: [segment:hyp-auftragstaktik-principle]
---

# #hyp-auftragstaktik-principle: the hypothesis states a total-allocation ordering B_O > B_Sigma > B_M (line 30) where the argument is about marginal value of bandwidth (F162); and line 56 says Conway's Law 'is a consequence', which nothing derives (F165). Restate as a marginal-priority claim, and Conway as consistent-with, or derive it.

Split from TODO.md:498 (the 2026-08-22 impl batch's routed source-segment defects; CHANGELOG 2026-08-22, impl-unity-communication and batch two). Text confirmed unchanged at HEAD by the t1-todo rechecker.

Source added 2026-10-30 by Claude Opus 5.5 (spike drain fork B1): `spikes/track-a-intent-dag/04-multi-agent-intent-priorities.md` (March 2026, pre-AAT) states a sharper, testable form of the principle this item restates. Its Q1: when an objective's strategy DAG is split across agents, the cut should run through high-confidence, well-observed edges, so the best decomposition minimizes uncertainty on the edges that span agents (a weighted graph-partition criterion). Its Q2: shared intent should compress to exactly the constraints that keep those spanning edges viable, leaving intra-agent edges free for local grafting. Neither is in canon (no "spanning edge" or cut criterion in `#hyp-auftragstaktik-principle`, `#impl-unity-communication` or `#deriv-graph-structure`). It is direction-setting, never derived; consider it when restating, at hypothesis tier, or leave it here.

Source added 2026-10-30 by Claude Opus 5.5 (spike drain fork D): `spikes/tst-ideas-cycle-2026-05-21/spike-class-coercion-via-supervision.md` §6 attempts the Conway derivation this item says nothing supplies, from the coupling-class side rather than the bandwidth side: the system's GUC class is upper-bounded by the team's, because each developer's $\Sigma_t$ over the architecture is shaped by communication access. The spike holds it hypothesis-grade and leaves open whether the architecture is the union or the intersection of what developers can implement. It is part 4 of item:the-2026-05-21-tst-spike-cycle-carries-four-deve; whoever restates :56 should read both, since one derivation could serve both segments. #meas-coherence-coupling :41–45 carries Conway as an observation, correctly marked not derived.
