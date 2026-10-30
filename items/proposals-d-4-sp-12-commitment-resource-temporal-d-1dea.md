---
kind: item
provenance: imported
source: PROPOSALS.md:172
section: PROPOSALS — Architectural Portfolio › §D. Later — needs investigation-first scoping or upstream maturation
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:def-strategy-dimension, segment:def-strategy-dag, segment:def-satisfaction-gap, segment:deriv-strategic-composition]
rechecked: 2026-10-30T21:30:34Z by Claude Opus 5.5 (item rechecker, q-proposals lane)
owner: unassigned
restated: 'Extend the strategy DAG with a commitment state (considering vs committed, per Bratman / Rao-Georgeff; #def-strategy-dimension:97) and temporal structure (deadlines, durations); per-path resources are a third, separate leg, distinct from #form-resource-budget''s actuation-energy budget.'
---

# D.4 SP-12 — Commitment / resource / temporal DAG extensions

Imported verbatim (relative links rebased) from `PROPOSALS.md` line 172, section *PROPOSALS — Architectural Portfolio › §D. Later — needs investigation-first scoping or upstream maturation*. Not yet re-checked against HEAD: `vsect recheck item:proposals-d-4-sp-12-commitment-resource-temporal-d-1dea --outcome holds|stale|landed|not-an-item --why …`.


Newly surfaced in 2026-04-24 audit. Currently named in CLAUDE.md "Known Fragilities" but homeless in portfolio. Three dimensions the strategy DAG omits: **(a) commitment state** (BDI-style desire $D_t$ / committed intent $I_t$ split per Bratman / Rao-Georgeff); **(b) resource budgets** per path; **(c) temporal structure** (deadlines, durations, synchronization).

**Composes with O-BP12** (resource budget $B_t$ as master variable): SP-12 is the DAG-structure side; O-BP12 is the cost-allocation side. Together could provide the full bounded-rationality apparatus. **Composes with SP-11** (commitment state matters for composition-monotonicity — "we agreed" vs. "we committed" distinction).

**Medium-large effort** (multi-segment extension, requires spike). **Primary aspect: completeness. Secondary: reach (unlocks logogenic/Section-III work).** **Value: +6.**

**Independence: medium.** Touches `#def-strategy-dimension`, `#def-strategy-dag`, `#def-satisfaction-gap`, possibly `#deriv-strategic-composition`. Conflicts with any concurrent strategy-layer work, especially O-BP4 (retired but referenced) and any Section II strategy-DAG edits. New commitment-state object is mostly additive; existing semantics preserved. Safe to parallelize with Section I / III work and with Bundle 1 framing work.
