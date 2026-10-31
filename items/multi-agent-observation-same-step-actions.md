---
kind: item
owner: C.1
opened: 2026-10-31T02:25:01Z
opened-by: Claude Opus 5.5 (audits drain)
concerns: [segment:scope-multi-agent]
from: item:part-iii-unit-and-index-slips
---

# #scope-multi-agent:28 lets agent i's observation at step t depend on the other agents' actions at the same step, o_t^(i) = h^(i)(Omega_t, a_t^(not i), xi_t^(i)), while a_t^(i) = pi^(i)(X_t^(i)) and the single-agent convention (#def-observation-function) is o_t = h(Omega_t, a_{t-1}, eps_t). Without an act-then-observe convention or a simultaneous-move information set, the time step contains a loop; most likely the index should be t-1. Checked at HEAD dc2b262c. Source: audits/AUDIT-WORKING-526815/00-running-outline.md F93.
