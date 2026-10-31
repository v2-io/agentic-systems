---
kind: item
owner: C.1
opened: 2026-10-31T02:16:01Z
opened-by: drain-wn-01-gold-opus-5.5
concerns: [segment:hyp-mismatch-dynamics, segment:detail-linear-ode-approximation]
---

# #hyp-mismatch-dynamics states the Model D steady state as an equality, ||delta||_ss = rho/T. For arbitrary time-varying ||w(t)|| <= rho it is an ultimate bound, limsup ||delta|| <= rho/T. It is attained when the disturbance is constant or worst-case aligned (526815). #detail-linear-ode-approximation states the converse half: line 68 calls rho/T the worst case over disturbances. For a constant drift vector the linear system's delta aligns with w, so rho/T is the exact steady state, not a rarely hit bound (Gemini 193847, its Off-ramp WN line 236). Both segments are improved by one statement: equality for constant drift, ultimate bound otherwise. The segment is heuristic-tier, so this is precision, not a tier question. Checked at HEAD 4175aae7. Sources: #hyp-mismatch-dynamics gold Follow-up (WN line 93); #detail-linear-ode-approximation Off-ramp (WN line 236).
