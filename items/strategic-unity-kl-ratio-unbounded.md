---
kind: item
owner: C.1
opened: 2026-10-31T02:25:01Z
opened-by: Claude Opus 5.5 (audits drain)
concerns: [segment:def-unity-dimensions]
from: item:part-iii-unit-and-index-slips
---

# #def-unity-dimensions:50 defines strategic unity U_Sigma = 1 - KL(pi_actual || pi_opt) / KL(pi_independent || pi_opt) with no support condition: the denominator is zero when independent play is already optimal, KL can be infinite, and U_Sigma is negative when coordination does worse than none, so the stated reading (1 at optimal, 0 at independent) does not make it a [0,1] measure. Needs a support condition, clipping, or a bounded divergence. Checked at HEAD dc2b262c. Source: audits/AUDIT-WORKING-526815/00-running-outline.md F148; the segment's other unity-metric items (F146 landed, F147, F150) are in item:todo-def-unity-dimensions-a13-f146-u-m-i-h-no-6bb8.
