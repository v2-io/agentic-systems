---
kind: item
owner: C.1
opened: 2026-10-31T02:21:49Z
opened-by: Claude Opus 5.5 (WN-01 drain)
concerns: [segment:result-adversarial-tempo-advantage, segment:der-adversarial-destabilization, segment:def-adaptive-tempo, segment:deriv-tempo-additivity, segment:deriv-discrete-sector-condition]
---

# #result-adversarial-tempo-advantage calls its exponents exact 'conditional on the disturbance model and coupling model' (Epistemic Status :76-80), but two premises its own Working Notes name are absent from the body (checked by grep: no 'exogenous', 'channel', 'correlated'): (a) each agent's tempo is treated as exogenous; a coupled analysis, a joint Lyapunov function over (delta_A, delta_B), is open, and the decoupled result is the slower agent's worst case (the faster may divert capacity from its own correction); (b) the ratio uses scalar tempo, which inherits #def-adaptive-tempo's channel-independence condition; under correlated channels the scalar tempos misstate the ratio (the signed deviation is #deriv-tempo-additivity's). State both as scope. Also owed: (c) the derivable finite-nu correction that explains the 0.019 gap between the simulated b = 1.481 and 3/2 (a factor sqrt((2c_min - eta_A c_max^2)/(2c_min - eta_B c_max^2)) from #deriv-discrete-sector-condition's O(eta c_max^2/c_min^2) term, tending to 1 in the fluid limit). Source: #result-adversarial-tempo-advantage Working Notes 'Channel-independence assumption', the exogenous-tempo item, and the b = 3/2 item.
