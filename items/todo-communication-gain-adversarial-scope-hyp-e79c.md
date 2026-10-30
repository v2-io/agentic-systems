---
kind: item
provenance: imported
source: TODO.md:157
section: TODO — Miscellaneous & details › Open theory items (MEDIUM)
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:hyp-communication-gain]
rechecked: 2026-10-30T21:24:53Z by Claude Opus 5.5 (item rechecker, t1-todo)
owner: C.1
restated: 'The scope sentence exists (Epistemic Status line 39 and intro line 19, present since the March migration, before this item was written). It does not settle the item, because it asserts a safety property the formula lacks. U_align is uncertainty about alignment, so certainty that a source is misaligned drives U_align to 0 and raises the gain: the model fully trusts a known liar. The work is representational: carry known misalignment as a bias (mean shift) or define U_align as expected squared misalignment, then restate ''conservative'' to what the formula actually does. The game-theoretic extension stays external, as the segment says.'
---

# Communication-gain adversarial scope — `#hyp-communication-gain`'s additive model fails for deception (trust is game-theoretic). Either extend or add explicit s

Imported verbatim (relative links rebased) from `TODO.md` line 157, section *TODO — Miscellaneous & details › Open theory items (MEDIUM)*. Not yet re-checked against HEAD: `vsect recheck item:todo-communication-gain-adversarial-scope-hyp-e79c --outcome holds|stale|landed|not-an-item --why …`.

- **Communication-gain adversarial scope** — `#hyp-communication-gain`'s additive model fails for deception (trust is game-theoretic). Either extend or add explicit scope limitation.

Source added 2026-10-30 by Claude Opus 5.5 (spike drain lead): spikes/spike-honest-activation-2026-09-23/03-derivations.md R3 is the representational repair this item asks for, derived and twice independently verified. Known or suspected misalignment is carried as a persistent source offset with a Gaussian bias prior N(0, tau^2), or as an honest/liar mixture (P(beta_j = 0) = p_j), rather than as noise variance. Under that model it gives the exact attribution floor (with persistent offsets, data identify only differences between sources, so priors decide who is believed); the asymptotic per-corroborator odds factor; the reversal (corroboration inverts when the agent's model of honest agreement is tighter than real honest scatter); and the class point that a trust model without a liar component gets only harmonic protection from corroboration. R2/R5d give the adversary's 'present as trustworthy' strategy that this segment's Epistemic Status says it misses. Plan item 4 (spikes/spike-honest-activation-2026-09-23/proposed-integration-plan.md). The landing of the rest of the spike is item:author-norm-honest-activation-and-its-derivation.
