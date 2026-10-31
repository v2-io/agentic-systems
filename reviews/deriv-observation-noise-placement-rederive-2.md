---
kind: review
author:
  name: c1-defender-noise
  role: integrator
written: 2026-10-31T03:07:19Z
---

# 2026-10-31: rederive of segment:deriv-observation-noise-placement

## C1 (check)
- target: segment:deriv-observation-noise-placement
- act: rederive
- line: derivation
- criterion: Re-read after the P1(b) rewording: P1-P3 as re-derived in the first check; P1(b) now states the best attainable error n sigma_env,B sigma_nu,B is increasing in sigma_nu,B because the error at every gain is (the infimum of increasing functions), replacing an ambiguous 'noise-free value' aside
- committed: after
- outcome: confirmed
- recheck: python3 -I empirica/track-b-nonlinear/variants/variant_e_noise_placement.py
- read: seg:deriv-sector-condition, seg:result-adversarial-tempo-advantage, seg:der-adversarial-destabilization, seg:emp-update-gain

