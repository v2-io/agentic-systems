---
kind: item
owner: C.1 (with E.2)
opened: 2026-10-30T23:21:10Z
opened-by: Claude Opus 5.5 (Part I round-3 integrator)
concerns: [segment:detail-operationalization]
---

# Write innovation-based estimators for #detail-operationalization: the environmental intensities (sigma_env, rho_env) identified from the observation stream of a possibly mis-tuned filter (e.g. the innovation-autocovariance route of adaptive Kalman filtering's noise identification, Mehra 1970, to be read at the primary), the channel terms from calibration, the total disturbance computed as sigma_w^2 = sigma_env^2 + alpha^2 sigma_nu^2 or rho = rho_env + alpha nu_bar, and alpha and R from innovation data. Since round 3 (b15e947d) the segment's residual-based recipes are stated for a noiseless channel only. Verify each estimator on simulated data with known parameters before landing. Feeds E.2.
