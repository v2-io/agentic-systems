---
kind: item
owner: F.3
opened: 2026-10-30T23:24:45Z
opened-by: Claude Opus 5.5 (spike drain lead)
concerns: [segment:deriv-edge-credence-dynamics, segment:schema-strategy-persistence]
---

# NeurIPS Paper 2 says something about canon that is now false. ~/src/neurips/02-unified-convergence-rl/adjudicated/residue.md:27 calls the strategic-persistence forgetting gain 'Convention-dependent. SEG gives (1-lambda)/(2-lambda); ALT1 gives 1-lambda ... One-line convention decision owed.' Since 2026-10-30 (F72; spikes/spike-strategic-persistence-hard-ceiling-convention-2026-05-31-verify-1.md and its -integration-notes.md) canon holds that SEG and ALT1 are one estimator, and that the stationary per-observation gain is exactly 1 - lambda (#deriv-edge-credence-dynamics Prop B.1F). The (1-lambda)/(2-lambda) form was an algebra error, and #deriv-strategic-persistence-hard-ceiling is deleted. So the paper's 1 - lambda is right, no convention decision is owed, and Key Lemma 2's unexplained approximation can become an equality via Prop B.1F. The F72 integrator flagged this to the coordinator without editing; this item is the record. The paper is outside asf; whoever holds it makes the edit.

A paper's claim about canon is stale after today's correction (F.3: what crosses the canon boundary is faithful). Drained 2026-10-30.
