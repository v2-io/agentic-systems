---
kind: item
owner: C.3
opened: 2026-10-31T02:16:39Z
opened-by: Claude Opus 5.5 (audits drain)
concerns: [segment:disc-credit-assignment-boundary, segment:def-strategy-dag]
---

# #disc-credit-assignment-boundary:67 says that under causal insufficiency 'hat P_Sigma systematically overestimates success, making the residual systematically negative on failure', but #def-strategy-dag's own covariance table (:89 and neighbours) shows the sign depends on topology: positive covariance makes OR estimates optimistic and AND estimates conservative. The blanket claim holds only for OR-dominated redundancy; the gradient-attribution consequence drawn from it inherits the scope. Same blanket wording was flagged in #def-strategy-dag itself (F44) and appears fixed there by the table. Checked at HEAD dc2b262c. Source: audits/AUDIT-WORKING-526815/00-running-outline.md F62 and F44; the segment's Working Notes (:198) route F60-F62 to an off-ramp without a decision.
