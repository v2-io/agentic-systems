# PROPOSED — misc detail home

Residual detail home for indexed spike efforts that are **real and un-started but neither moonshot/theory-edge** (those → [`PROPOSED-ADVANCED.md`](PROPOSED-ADVANCED.md)) **nor tied to a specific segment's Working Notes** (those keep their detail in the segment, the [`PROPOSED.md`](PROPOSED.md) index links to it). Often near-empty by design — that is expected, not a defect. Every entry here has a row in [`PROPOSED.md`](PROPOSED.md) and is reconciled with it bidirectionally (`../doc/sop/spikes.sop.md` §2-bis(3) + Refinement 10).

---

## sw-reciprocal-link-check — `bin/` enforcement for the reciprocal-link discipline

**Status:** proposed (un-started). **Added:** 2026-05-19.

The reciprocal-link discipline (every segment Working-Note strengthening / spike-proposal comment links to its `PROPOSED.md` tier; every index row links to its detail home) is currently prose-enforced only — exactly the failure mode that let `PROPOSED.md` silently drift before 2026-05-19. The teeth: a `bin/` check (Ruby, per the internal-script convention) that

- scans `*/src/*.md` Working Notes / Epistemic Status for strengthening / spike-proposal language (a small pattern set: "would land as … if pursued", "open … spike", "follow-on spike", "the named next spike", "spike target", "candidate … appendix if pursued", …) and flags any such comment with no `PROPOSED` back-reference;
- scans `PROPOSED.md` rows for a present, resolvable Details link;
- (stretch) cross-checks that `seg:<slug>`-sourced rows actually have the reciprocal back-link in `<slug>`'s Working Notes.

Output advisory (like `bin/lint-outline`), not blocking. Dogfood note: this entry *is* an indexed un-started effort, tracked by the very index whose integrity it would enforce.

**Sweep-scope precedents** (retained from the completed 2026-05-19 one-time WN-strengthening sweep — the sweep itself is done; these are the standing judgment-call precedents for what belongs in this index): (1) *segment-shaped not spike-shaped is excluded* — "follow-on segment" / "separate segment" framings are recognized open territory, not the reasoning-trail of an attempt (judgment recorded at `sketch-structural-adaptation-genericity.md:52`); they belong in the segment/OUTLINE-GAP layer. (2) *Empirical-verification questions are excluded* — e.g. `04-eli-core` "Open questions for verification" blocks are empirical-program questions, not spike-shaped derivations. (3) *Owned-elsewhere efforts are cross-referenced, never duplicated* (discipline 1).
