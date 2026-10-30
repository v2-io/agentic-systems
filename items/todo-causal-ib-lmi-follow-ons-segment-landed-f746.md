---
kind: item
provenance: imported
source: TODO.md:171
section: TODO — Miscellaneous & details › Open theory items (MEDIUM)
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:deriv-causal-ib-lmi, segment:def-adaptive-tempo]
rechecked: 2026-10-30T21:23:46Z by Claude Opus 5.5 (item rechecker, t1-todo)
owner: C.1
restated: 'Before the four follow-ons, a defect in the LMI itself: the ''if and only if'' between survival (lambda_max(Sigma) < R^2) and E[I_o] >= I_min with I_min SPD is false whenever A mixes directions. A rank-one information matrix stabilizes under a rotation A (reviews/items-recheck-t1.md C2). State the separable or aligned hypothesis under which the minimal information set is a single matrix, or recast the constraint as membership in an upward-closed set, and recheck the KKT blank-wall argument under it. Of the follow-ons: tensor tempo downstream is the AAT-1 item (lane t2); the worked 2D example and the 2D simulation are not done (variant_causal_ib.py is the scalar explore/exploit simulation of #deriv-causal-ib-exploration), and the 2D test should include a mixing A, the case that breaks the iff; ''closed-form I_min via DARE'' presumes a unique I_min, which exists only in the aligned case.'
---

# Causal-IB LMI follow-ons (segment landed `#deriv-causal-ib-lmi`)

Imported verbatim (relative links rebased) from `TODO.md` line 171, section *TODO — Miscellaneous & details › Open theory items (MEDIUM)*. Not yet re-checked against HEAD: `vsect recheck item:todo-causal-ib-lmi-follow-ons-segment-landed-f746 --outcome holds|stale|landed|not-an-item --why …`.

- **Causal-IB LMI follow-ons** (segment landed `#deriv-causal-ib-lmi`):
  - Tensor adaptive tempo *downstream* — the per-direction matrix primitive is in `#def-adaptive-tempo` (Tensor extension); the LMI and the composition/summary results still read scalar (same remainder as AAT-1).
  - Worked 2D blank-wall example (~30–60 min editorial).
  - 2D simulation update (`empirica/track-b-nonlinear/variants/variant_causal_ib.py` to 2D with separable drifting/non-drifting subspaces).
  - Closed-form $\mathcal I_{\min}$ via DARE (currently theorem-imported per Boyd et al. 1994).
