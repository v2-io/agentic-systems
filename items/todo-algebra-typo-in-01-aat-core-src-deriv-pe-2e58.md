---
kind: item
provenance: imported
source: TODO.md:389
section: TODO — Miscellaneous & details › 🌟 Parts III + IV active work (encounter cycle 2026-05-01) › Side findings flagged for upstream cleanup
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
rechecked: 2026-10-30T20:22:59Z by Claude Opus 5.5 (item rechecker, pilot)
owner: C.1 integrator (unassigned)
---

# Algebra typo in `01-aat-core/src/deriv-persistence-cost.md` — audit `61-deriv-persistence-cost.md` §3 caught: the derivation cancels $n$ incorrectly going from

Imported verbatim (relative links rebased) from `TODO.md` line 389, section *TODO — Miscellaneous & details › 🌟 Parts III + IV active work (encounter cycle 2026-05-01) › Side findings flagged for upstream cleanup*. Not yet re-checked against HEAD: `vsect recheck item:todo-algebra-typo-in-01-aat-core-src-deriv-pe-2e58 --outcome holds|stale|landed|not-an-item --why …`.

- **Algebra typo in `01-aat-core/src/deriv-persistence-cost.md`** — audit `61-deriv-persistence-cost.md` §3 caught: the derivation cancels $n$ incorrectly going from per-dimension to total rate. Constructive repair: state per-dimension RDF first ($\dot R_i = \sigma_w^2/(4 D_i^2)$), substitute $D_i^2 = \sigma_w^2/(2\alpha)$, sum to total $n\alpha/2$. Final result is correct; intermediate algebra is sloppy. Not lifted by the encounter cycle since 01-aat-core is priority territory; flagged here.
