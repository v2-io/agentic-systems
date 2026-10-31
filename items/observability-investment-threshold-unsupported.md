---
kind: item
owner: C.1
opened: 2026-10-31T02:16:39Z
opened-by: Claude Opus 5.5 (audits drain)
concerns: [segment:der-observability-dominance, segment:deriv-edge-credence-dynamics]
---

# #der-observability-dominance:132 says making intermediate B observable improves alpha_Sigma from the plan-level 1/(n_Phi+1) to min(1/(n_1+1), theta_1/(n_2+1)) and that 'the improvement is positive whenever theta_1 > 1/2 and experience is distributed similarly across edges'. Taken at face value the comparison goes the other way: with equal counts n, the per-edge minimum is theta_1/(n+1), below 1/(n+1) for every theta_1 < 1; with n_2 = theta_1 n (edge 2 sees evidence only after edge 1 succeeds) it is theta_1/(theta_1 n + 1), also below 1/(n+1). So the theta_1 > 1/2 threshold does not follow from the displayed formulas under either counting convention I tried; the benefit of observability may lie elsewhere (identification of which edge failed, the absence of the O(1/n) bias of the unobservable case at :128), not in a larger sector constant. Needs the derivation's counting convention and comparison baseline stated, or the claim restated to what holds. My arithmetic is a check on the displayed formulas, not a re-derivation of #deriv-edge-credence-dynamics B.2-B.3. Source: audits/AUDIT-WORKING-526815/00-running-outline.md F53 (2026-05-15).
