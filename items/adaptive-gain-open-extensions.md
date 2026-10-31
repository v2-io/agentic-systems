---
kind: item
owner: C.4
opened: 2026-10-31T02:21:45Z
opened-by: Claude Opus 5.5 (WN-01 drain p1)
concerns: [segment:deriv-adaptive-gain-dynamics, segment:schema-strategy-persistence, segment:deriv-discrete-sector-condition, segment:deriv-fisher-whitened-update-rule, segment:deriv-fisher-local-update-gain]
---

# Open extensions of #deriv-adaptive-gain-dynamics: (a) derive the 1/sqrt(N) rate of Mehra-adaptive Kalman from (MG-1)-(MG-4) and the augmented-state Lyapunov (the composed result is a bound, not a rate; classical asymptotics give the rate directly); (b) the discrete-time form, with #deriv-discrete-sector-condition's Lipschitz bound on both F and Phi (mechanical, deferred); (c) re-read #schema-strategy-persistence's alpha_Sigma = 1/(n+1) as adaptive-gain dynamics where (MG-1) fails asymptotically without forgetting; (d) state in the body that deterministic meta-gains (Fisher whitening K_t = I^{-1}(lambda_t); the Fisher-local K = (H_M + H_L)^{-1} H_L) satisfy (MG-1)-(MG-4) trivially, so those segments are degenerate cases of this one (the body never names them). Source: #deriv-adaptive-gain-dynamics Working Notes 'Rate-specific results', 'Discrete-time form', 'Relationship to #schema-strategy-persistence', 'Deterministic-meta-gain special cases'.
