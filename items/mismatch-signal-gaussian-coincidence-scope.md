---
kind: item
owner: C.1
opened: 2026-10-31T02:15:29Z
opened-by: drain-wn-01-gold-opus-5.5
concerns: [segment:def-mismatch-signal]
---

# #def-mismatch-signal:57 says the score and the residual 'coincide up to scaling' under Gaussian models. The Gaussian-likelihood score with respect to arbitrary parameters is J^T Sigma^{-1}(o - mu), not a scaled residual; they coincide when the differentiated coordinate is the predictive mean (526815). Proposed: 'for Gaussian observations parameterized by the predictive mean'. Checked at HEAD 4175aae7. Source: gold Follow-up (WN line 94).
