---
kind: item
owner: C.3
opened: 2026-10-30T23:23:40Z
opened-by: drain-influx-2
concerns: [segment:def-mismatch-signal, segment:form-composition-closure]
---

# #def-mismatch-signal normalizes surprise by the wrong covariance, and canon already has the right one. Lines 21 and 65 (HEAD cbd2f345) say the mismatch magnitude 'should be understood as a Mahalanobis distance ... against the observation noise covariance' Sigma. A prediction error delta_t = o_t - E[o_t | M_t] has the innovation covariance S = P_pred + R, not R alone, so normalizing by observation noise overstates surprise by sqrt(1 + P_t/R) (the source computes about 4.1x at t = 0 under a vague prior; not re-run here). #form-composition-closure:318, in the verified two-Kalman case, already weights the observation norm by 'the inverse innovation covariance S^{-1} = (P_pred + R)^{-1}'. Reconcile #def-mismatch-signal to the innovation covariance (or say when Sigma means the full predictive covariance). Source: agent-core memory corpus lessons 08 §8 and 15 §2.3 (~/src/agent-core/memory/), relayed in msc/inside-out-2026-10/influx-scout/agent-core-memory.md C1.
