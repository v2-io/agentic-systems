---
kind: review
author:
  name: c1-defender-noise
  role: integrator
written: 2026-10-31T03:04:01Z
---

# 2026-10-31: run of segment:obs-gated-tempo-advantage

## C1 (check)
- target: segment:obs-gated-tempo-advantage
- act: run
- line: derivation
- criterion: The recorded Variant-E table is reproduced by the closed form of #deriv-observation-noise-placement; the simulation code raises attacker tempo by gain on one noisy observation per step (variant_ef_extensions.py run_variant_e_adversarial), as the restated mechanism says; the split re-run places the collapse on the attacker's channel
- committed: after
- outcome: confirmed
- recheck: python3 -I empirica/track-b-nonlinear/variants/variant_e_noise_placement.py
- read: seg:deriv-observation-noise-placement, seg:emp-update-gain

