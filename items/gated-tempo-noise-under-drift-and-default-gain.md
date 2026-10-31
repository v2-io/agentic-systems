---
kind: item
owner: C.4
opened: 2026-10-31T02:21:50Z
opened-by: Claude Opus 5.5 (WN-01 drain)
concerns: [segment:obs-gated-tempo-advantage, segment:result-adversarial-exponent-regimes, segment:emp-update-gain]
---

# Two open points on #obs-gated-tempo-advantage: (a) the Variant E runs use stochastic coupling only; whether observation noise degrades the deterministic-drift exponent (b = 2) by the same proportion is untested; (b) the runs found fixed eta = 0.1 robust to observation noise (42% degradation at sigma_obs = 10 q_env), suggesting a conservative fixed gain is a reasonable default under unknown noise because overcorrection costs more than undercorrection; the body does not say it, and whether the asymmetry is #emp-update-gain's general result was not checked. Related: item t1-gated-tempo-one-sided-noise-prescription. Source: #obs-gated-tempo-advantage Working Notes items 1-2; simulation empirica/track-b-nonlinear/variants/variant_ef_extensions.py.
