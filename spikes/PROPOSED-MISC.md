# PROPOSED — misc detail home

Residual detail home for indexed spike efforts that are **real and un-started but neither moonshot/theory-edge** (those → [`PROPOSED-ADVANCED.md`](PROPOSED-ADVANCED.md)) **nor tied to a specific segment's Working Notes** (those keep their detail in the segment, the [`PROPOSED.md`](PROPOSED.md) index links to it). Often near-empty by design — that is expected, not a defect. Every entry here has a row in [`PROPOSED.md`](PROPOSED.md) and is reconciled with it bidirectionally (`../doc/spike-routing.md` §2-bis(3) + Refinement 10).

---

## sw-reciprocal-link-check — `bin/` enforcement for the reciprocal-link discipline

**Status:** proposed (un-started). **Added:** 2026-05-19.

The reciprocal-link discipline (every segment Working-Note strengthening / spike-proposal comment links to its `PROPOSED.md` tier; every index row links to its detail home) is currently prose-enforced only — exactly the failure mode that let `PROPOSED.md` silently drift before 2026-05-19. The teeth: a `bin/` check (Ruby, per the internal-script convention) that

- scans `*/src/*.md` Working Notes / Epistemic Status for strengthening / spike-proposal language (a small pattern set: "would land as … if pursued", "open … spike", "follow-on spike", "the named next spike", "spike target", "candidate … appendix if pursued", …) and flags any such comment with no `PROPOSED` back-reference;
- scans `PROPOSED.md` rows for a present, resolvable Details link;
- (stretch) cross-checks that `seg:<slug>`-sourced rows actually have the reciprocal back-link in `<slug>`'s Working Notes.

Output advisory (like `bin/lint-outline`), not blocking. Dogfood note: this entry *is* an indexed un-started effort, tracked by the very index whose integrity it would enforce.

## sw-wn-strengthening-sweep — one-time Working-Note sweep (process)

**Status:** done (2026-05-19). **Added:** 2026-05-19.

The known WN strengthenings (Q1/Q2 in `#def-strategy-dag`, C10 in `#der-turnover-information-recursion`) were indexed and back-linked as of 2026-05-19. A one-time opportunistic freshen — a corpus pass over segment Working Notes / Epistemic Status across `01-aat-core` / `02-tst-core` / `03-llm-core` / `04-eli-core` — ran 2026-05-19, surfacing the genuinely-unhomed spike-shaped ones and adding mutual links. This was a *freshen, not a standing completeness obligation* (Joseph 2026-05-19 calibration: PROPOSED is not a mandatory registry — completeness is explicitly not required; freshness + the mutual link are the disciplines). The pass is "done" in the sense that it ran and what it found is fresh and linked — **not** in the sense that the index is now exhaustive (it need not be).

**What the sweep added (small-real-set discipline applied — when an item did not clearly clear the bar, it was excluded; cross-referenced, not duplicated, when owned elsewhere):**

- **5 new Tier 3 rows + reciprocal back-links** for genuinely unhomed, spike-shaped, tier-moving WN strengthenings: `seg:result-unity-closure-mapping` ((UO-mult) discussion-grade→derived), `seg:form-consolidation-dynamics` (quantitative CLS instantiation), `seg:deriv-update-detection-latency` (R2 detection-latency sharpening), `seg:der-code-quality-as-observation-infrastructure` (2D bistability formalization, TST-side), `seg:deriv-adaptive-gain-dynamics` (meta-gain adversarial-tempo analog).
- **1 reciprocal-link-only fix (no new row):** `der-adversarial-destabilization.md:87` ("formalize $\gamma_A(\lVert\delta_B\rVert)$ … make the spiral a result") was an unlinked WN comment for an effort *already indexed* at Tier 1 ("Effects-spiral eigenvalue condition — concrete agent classes", source `seg:deriv-strategic-composition`). Back-link added pointing at the existing Tier 1 row; not double-listed. This is the canonical discipline-2 gap shape — an already-indexed effort whose originating segment lacked the back-link.

**Owned-elsewhere WN strengthenings (deliberately *not* minted as fresh rows — discoverable in their owning home per discipline 1; not duplicated):** the `#disc-identifiability-floor` adjacent-floor cluster (misspecification-cost / Regime II-b Instance-3 / Mehra meta-gain obstruction — surfaced from `#der-interaction-channel-classification`, `#form-consolidation-dynamics`, `#deriv-adaptive-gain-dynamics`; owned in `TODO.md` "Queued spike work" §Identifiability Floor 141–142); $f(H_b^B)$ emitter-side-effect (owned `TODO.md:167`); consolidation stability-upper-bound (owned `TODO.md:166`); the resource-axis open dynamical items in `#der-resource-bounded-destabilization` / `#form-resource-budget` (regenerative regime + closed-form $\tau$ — owned by the off-spine resource-structure architectural axis, `PROPOSALS.md` §D.6 O-BP12 / SP-12, Joseph-elected/gated per those segments' exploratory-branch notes).

**Judgment calls surfaced (for the verifier):**
1. **Stale-but-out-of-scope, flagged not fixed:** `der-interaction-channel-classification.md:174` "Next spike candidate (3)" proposes solving `#adversarial-edge-targeting` "formally" — but that gap is **already closed** in canon by `#der-agent-opacity`'s 16-cell emitter-recipient arg-max (`der-agent-opacity.md` Discussion + Findings). This is a navigator-level §4.1-class drift inside a segment Working Note (a resolved direction still presented as open). It is out of this sweep's scope (indexing, not segment-truth correction) and is recorded here for the navigator-reconciliation cycle rather than silently edited.
2. **Segment-shaped not spike-shaped (excluded):** "follow-on segment" / "separate segment" framings (e.g. `def-identity-sufficiency` identity-IB optimal-compression-family, `hyp-the-three-deaths` per-death `der-cognitive-death-*`, `def-five-constitutive-factors` graded measures) are recognized open *territory*, not the reasoning-trail of an *attempt* — same judgment recorded at `sketch-structural-adaptation-genericity.md:52`. Not swept (consistent with that established precedent); they belong in the segment/OUTLINE-GAP layer, not the spike-proposal index.
3. **Empirical-verification questions (excluded):** `04-eli-core` "Open questions for verification" blocks (cross-cohort incident study, "are there additional deaths") are empirical-program questions, not spike-shaped derivations.

Audit-trail note (the framing this entry originally carried, deflated 2026-05-19): an earlier draft of this entry treated the sweep as making the index "provably complete for all WN-resident efforts." That over-stated it — completeness is not a discipline here (see `PROPOSED.md` "Not a mandatory registry" + `doc/spike-routing.md` Refinement 10 Calibration). The honest statement is the one above: it ran, what it found is fresh and linked, and the index is *not* claimed exhaustive.
