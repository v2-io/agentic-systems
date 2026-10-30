---
kind: item
owner: C.1
opened: 2026-10-30T23:20:57Z
opened-by: Claude Opus 5.5 (audits drain)
concerns: [segment:deriv-variational-sector-condition]
---

# #deriv-variational-sector-condition:18 (summary paragraph) asserts that mean-field VI is 'structurally sub-optimal as an adaptive system by a factor sqrt(1-r^2) in the sector constant, regardless of compute or training data'. Checked at HEAD: r is never defined in the segment and no sqrt(1-r^2) factor is derived anywhere in it, nor anywhere else in 01-aat-core/src; the body's per-case verdict supports only a small additive O(sqrt(epsilon)) degradation. A Gate-2-shape claim: it reads as derived and is not. Strengthen first: the likely intended instance is a bivariate Gaussian target with correlation r, where mean-field marginal variances shrink by (1-r^2) (Bishop 2006 §10.1.2); derive the sector-constant consequence for that instance and state it with r defined and its scope (Gaussian, two blocks), or replace the sentence with what the body derives. Source: audits/AUDIT-WORKING-374162/08-batch-verification.md:5-11 (Fable 5 verifier, 2026-07-20; the quiz answer b08-3.7 inherited the sentence).
