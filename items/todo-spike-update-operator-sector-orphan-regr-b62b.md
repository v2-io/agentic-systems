---
kind: item
provenance: imported
source: TODO.md:472
section: TODO — Miscellaneous & details › 2026-05-12 (late) — Spike audit triage (99 spike files surveyed via 3 parallel agents)
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:deriv-sector-condition, segment:disc-identifiability-floor]
rechecked: 2026-10-30T21:15:23Z by Claude Opus 5.5 (item rechecker, t2-todo)
owner: G.2
closed: 2026-10-30 superseded by Claude Opus 5.5 (spike drain lead)
---

# `spike-update-operator-sector` — orphan, regression-checked CLEAR 2026-05-17 (genuine deferred orphan, not corrected-away); tractable landing pending: $\alpha$-

Imported verbatim (relative links rebased) from `TODO.md` line 472, section *TODO — Miscellaneous & details › 2026-05-12 (late) — Spike audit triage (99 spike files surveyed via 3 parallel agents)*. Not yet re-checked against HEAD: `vsect recheck item:todo-spike-update-operator-sector-orphan-regr-b62b --outcome holds|stale|landed|not-an-item --why …`.

- [ ] **`spike-update-operator-sector`** — orphan, regression-checked CLEAR 2026-05-17 (genuine deferred orphan, not corrected-away); **tractable landing pending**: $\alpha$-op/$\beta$-op refresh into `#deriv-sector-condition` + operator-layer no-go into `#disc-identifiability-floor` (present-tense canon); parent-owned §266(iii)/§8.2 placement.

Source added 2026-10-30 by Claude Opus 5.5 (spike drain fork A), after reading spikes/spike-update-operator-sector.md whole against HEAD: the landing this item asks for would put a false claim into canon. The spike's (O-A2') with a positive sector constant on the edge vector is false whenever the DAG has two or more identifiable edges and the outcome is one plan-level scalar y_G. The expected update is a multiple of the single direction J, so the fixed points form the level set {P_Sigma = Phi}, a manifold of dimension |E| - 1 (the spike's own §1.2), and no contraction to a point lambda* exists. The algebra fails at §2.2: (a.e)(b.e) is a rank-two quadratic form, and the symmetric part of (ab^T + ba^T)/2 has eigenvalues (a.b ± |a||b|)/2, so its least eigenvalue is at most 0 for |E| >= 2 (Case 2's 'PSD iff a.b >= 0' is wrong), and Case 1's componentwise inequality fails on e orthogonal to a. A two-edge AND simulation (theta = (0.8, 0.6)) converges to points on p1 p2 = 0.48 fixed by the initial credences, not to theta. What is true is already canon: persistence transfers only to the plan-level error delta_s (Prop B.5 via #disc-credit-assignment-boundary:20, :75) and per-edge attribution is underdetermined when observable nodes are fewer than edges (barrier (b), :101-105; the F60 note at :207). The §4.3 operator-layer Cramér-Rao break is the same rank statement. Never in canon (pickaxe of alpha_op / O-A2' over */src is empty), so there is nothing to retract. Suggested disposition, for a second mind to confirm: close this item as superseded and file the spike to spikes/.archived/ with this reason. The single-edge and fully-observable cases contract, but canon already covers them as the trivial observable-intermediates case.

Second mind, 2026-10-30, Claude Opus 5.5 (spike drain lead), by a different route from fork A's algebra and simulation. When the only observation is the plan-level outcome y_G ~ Bernoulli(prod_e p_e), its law depends on the edge credences only through the product. Every point on the level set {prod p_e = prod theta_e} is therefore observationally equivalent to theta. An update driven only by y_G, if unbiased at the plan level, has zero expected drift anywhere on that set, and if not, it fails at theta itself. Either way, no rule of that kind contracts to theta from every initialization once |E| >= 2. That is (O-A2')'s claim, so it is false for an identifiability reason, not only an algebraic one. Canon already carries the true statement (#disc-credit-assignment-boundary:101-105, barrier 2: dim of the identifiable subspace <= |V_obs|). I re-ran the exclusion pickaxe for alpha_{\text{op}} and O-A2' over 0*/src: both are empty, so it never entered canon. Closing as superseded. The spike goes to spikes/.archived/ with this reason.
