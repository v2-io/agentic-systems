---
kind: item
owner: C.1
opened: 2026-10-31T02:17:24Z
opened-by: Claude Opus 5.5 (audits drain)
concerns: [segment:der-interaction-channel-classification, segment:def-unity-dimensions, segment:scope-multi-agent]
---

# Three small unit and index slips in Part III, each checked present at HEAD dc2b262c. (1) #der-interaction-channel-classification:108, Case 1: 'I(xi_A) ~ s^2/(2r ln 2) nats'. Dividing by ln 2 converts nats to bits; for small-variance Gaussian forcing the information is (1/2) ln(1 + s^2/r) ~ s^2/(2r) nats. Either the unit or the formula is wrong (526815 F209). (2) #def-unity-dimensions:50 defines strategic unity U_Sigma = 1 - KL(pi_actual || pi_opt)/KL(pi_independent || pi_opt) with no support condition: the denominator is zero when independent play is already optimal, KL can be infinite, and U_Sigma goes negative when coordination is worse than none, so the stated [0,1] reading fails without clipping or a bounded divergence (526815 F148). (3) #scope-multi-agent:28 lets agent i's observation at t depend on the other agents' actions at the same t, o_t^(i) = h^(i)(Omega_t, a_t^(not i), xi_t^(i)), while a_t^(i) = pi^(i)(X_t^(i)) and the single-agent convention (#def-observation-function) is o_t = h(Omega_t, a_{t-1}, eps_t). Without an act-then-observe convention or a simultaneous-move information set, the time step contains a loop; most likely the index should be t-1 (526815 F93). Source: audits/AUDIT-WORKING-526815/00-running-outline.md F93, F148, F209.
