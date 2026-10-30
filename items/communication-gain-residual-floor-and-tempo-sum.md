---
kind: item
owner: C.1
opened: 2026-10-30T23:27:14Z
opened-by: drain-wn-01-gold-opus-5.5
concerns: [segment:hyp-communication-gain, segment:deriv-tempo-additivity]
---

# #hyp-communication-gain: two of the six 526815 findings in its Off-ramp (Working Notes line 105) are still live at HEAD 86489b0b. The others are handled. F167 is in canon (line 47 says the additive denominator is a structural heuristic; line 51 requires a common predictive-dispersion scale). F168 is item:todo-communication-gain-adversarial-scope-hyp-e79c. F171/F172 are question:how-should-the-null-distribution-p-0-of-hyp-comm. (F169) Line 51's fallback estimates U_src + U_align as residual variance minus U_o,ji. That difference can go negative and has no floor, and the residuals conflate calibration, alignment, receiver model error, nonstationarity and common shocks. (F170) Line 69 adds communication tempo linearly to the distributed tempo (T_i = sum_k nu eta + sum_j nu^comm eta), the additivity #deriv-tempo-additivity shows fails for redundant or common-source channels. The same Working Notes (line 72) already cite that segment's common-source regime for corroboration but not for this sum.
