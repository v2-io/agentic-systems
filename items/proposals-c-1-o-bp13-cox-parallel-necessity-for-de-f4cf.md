---
kind: item
provenance: imported
source: PROPOSALS.md:95
section: PROPOSALS — Architectural Portfolio › §C. Soon — prereqs nearly met
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:deriv-graph-structure, segment:der-architecture-noidentifiability, segment:disc-identifiability-floor]
rechecked: 2026-10-30T21:30:34Z by Claude Opus 5.5 (item rechecker, q-proposals lane)
owner: unassigned
restated: Find out whether P1-P4 plus causal sufficiency force DAG semantics (#deriv-graph-structure:17 proves sufficiency only); expect the answer to split on causal sufficiency, with ADMG/chain-graph structure the honest form when it fails (Lauritzen-Sadeghi 2018; Evans-Richardson 2014).
---

# C.1 O-BP13 — Cox-parallel necessity for `#deriv-graph-structure`

Imported verbatim (relative links rebased) from `PROPOSALS.md` line 95, section *PROPOSALS — Architectural Portfolio › §C. Soon — prereqs nearly met*. Not yet re-checked against HEAD: `vsect recheck item:proposals-c-1-o-bp13-cox-parallel-necessity-for-de-f4cf --outcome holds|stale|landed|not-an-item --why …`.


Sharp theorem-spike question: can Lauritzen-Sadeghi 2018 unify enough to force DAG semantics from P1–P4 + causal sufficiency? Win/win outcome structure — success elevates the sufficiency-only claim to full Cox-parallel; failure is a *new* floor instance (or a named no-go under `#deriv-graph-structure`), **not** "Instance 4" — that slot is already occupied by `#der-architecture-noidentifiability` (landed 2026-05-21; four instances in `#disc-identifiability-floor`, first-hand). **1–2 session scoping spike; 2–3 sessions if tractable.** External literature ready (Lauritzen-Sadeghi 2018; Evans-Richardson 2014; Drton-Maathuis-Meinshausen 2017).

Primary aspect: correctness. Secondary: fundamentality, transparency. **Value: +5 framework / +7 paper.**

**Independence: high.** Self-contained spike on `#deriv-graph-structure`; either produces a necessity-direction derivation (segment extension) or a new floor/no-go (Instance 4 is taken). Either outcome touches one primary segment plus possibly the meta-segment; minimal cross-segment surface area. Safe to parallelize with any other active proposal.
