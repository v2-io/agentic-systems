---
kind: review
author:
  name: c1-defender-noise
  role: integrator
written: 2026-10-31T03:03:56Z
---

# 2026-10-31: rederive of segment:deriv-observation-noise-placement

## C1 (check)
- target: segment:deriv-observation-noise-placement
- act: rederive
- line: derivation
- criterion: P1-P3 re-derived from the Setup steady state of #deriv-sector-condition with Coupling Model S; the discrete closed form reproduces both recorded Variant-E exponent columns to within 0.003; the Variant-E loop re-run with channels separated gives defender-only slope 0.82 with the ratio rising at every tempo ratio and attacker-only slope 0.40; the P2(b) 1/2 limit checked numerically (local slope 0.500)
- committed: after
- outcome: confirmed
- recheck: python3 -I empirica/track-b-nonlinear/variants/variant_e_noise_placement.py from that directory; compare with variant_ef_results.md E3
- read: seg:deriv-sector-condition, seg:result-adversarial-tempo-advantage, seg:der-adversarial-destabilization, seg:emp-update-gain

