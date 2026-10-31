---
kind: review
author:
  name: c1-defender-noise
  role: integrator
sources:
  - msc/inside-out-2026-10/c1-lanes/defender-noise-round-2.md
  - msc/inside-out-2026-10/c1-lanes/defender-noise-round-2.py
written: 2026-10-31T03:30:57Z
---

# The defender-noise lane, round 2: integrator's checks

KR C.1 ("Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier"). Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." These are the integrator's checks on the round-2 landing `2f622c4b`, which answers independent check 1. The reasoning is in the first source; the second prints the numbers (`python3 -I`, a few seconds).

## C1 (check)
- target: segment:deriv-observation-noise-placement
- at: 2f622c4b
- act: rederive
- line: derivation
- criterion: P4: by the Model S window, a mean-square persisting attacker on a fixed channel has $\alpha_A \lt \alpha_+ \leq 2R_A^2/(n\sigma_{\nu,A}^2)$ for every $\sigma_{\text{env},A}$; with P1(c), $2\gamma_A R_A^2/(n\sigma_{\nu,A}^2) \leq R_B^2/(n\sigma_{\nu,B}) - \sigma_{\text{base}}$ suffices for the defender to persist at its Kalman gain against every persisting attacker gain.
- committed: after
- outcome: confirmed
- recheck: By hand: the quadratic's larger root and the bound $\sqrt{R_A^4 - n^2\sigma_{\text{env},A}^2\sigma_{\nu,A}^2} \leq R_A^2$; strict inequalities chain. Numerically (second source): 20,000 random draws, 11,221 with a persistence window, no gain above the cap; 7,912 draws satisfying the condition, defender at its Kalman gain persists against every persistent attacker gain on a 300-point grid.
- read: seg:result-persistence-condition, seg:deriv-sector-condition, seg:der-adversarial-destabilization

## C2 (check)
- target: segment:deriv-observation-noise-placement
- at: 2f622c4b
- act: rederive
- line: derivation
- criterion: P2(c): with event rate $\nu_A$, per-event gain $h_A$ and per-event noise $s_A^2$, $\alpha_A^2\sigma_{\nu,A}^2 = \alpha_A h_A s_A^2$, so $V_A = n\sigma_{\text{env},A}^2/(2\alpha_A) + nh_As_A^2/2$; dominance fails near $\alpha_A \sim \sigma_{\text{env},A}^2/(h_As_A^2)$ and the exponent goes $3/2 \to 1$ with ratio $\gamma_A\alpha_A/(s_A\sqrt{h_A\alpha_B})$.
- committed: after
- outcome: confirmed
- recheck: By hand from $\sigma_{\nu,A}^2 = s_A^2/\nu_A$ and $\alpha_A = \nu_Ah_A$. Numerically: local exponent $1.494$ at low tempo and $1.000$ at high tempo (second source).
- read: seg:result-persistence-condition, seg:deriv-sector-condition

## C3 (check)
- target: segment:def-adaptive-tempo
- at: 2f622c4b
- act: rederive
- line: derivation
- criterion: With independent per-event noise of variance $s^2$ at event rate $\nu$, the tempo at the optimal gain is the Kalman–Bucy gain $\sigma_{\text{env}}\sqrt\nu/s$ and the smallest error $n\sigma_{\text{env}}s/\sqrt\nu$, so "regardless of loop speed" is false for independent noise; it holds for a shared persistent bias (the segment's channel noise-independence condition) and for the Model D bounded floor.
- committed: after
- outcome: confirmed
- recheck: From $\sigma_\nu^2 = s^2/\nu$ (the event-rate lever of #result-persistence-condition) and $K = \sigma_{\text{env}}/\sigma_\nu$. Discrete per-event Kalman for a random walk with per-event diffusion $1/\nu$ and unit noise: $\nu K = 0.618, 1.562, 3.531, 7.516, 15.508$ at $\nu = 1, 4, 16, 64, 256$, approaching $\sqrt\nu$.
- read: seg:result-persistence-condition, seg:deriv-sector-condition

## C4 (check)
- target: segment:result-adversarial-tempo-advantage
- at: 2f622c4b
- act: rederive
- line: derivation
- criterion: The scope paragraph's event-rate sentence: at a fixed per-event gain $h$ the injected term is $\mathcal T h s^2$, coupling dominance of the attacker fails near $\mathcal T_A \sim \sigma_A^2/(hs^2)$ with exponent $1$ past it, and stays only if the event rate grows at least as the square of tempo.
- committed: after
- outcome: confirmed
- recheck: As C2; dominance $\sigma_A^2 \gg \mathcal T_A h s^2$ held as $\mathcal T_A$ grows iff $h \lesssim \sigma_A^2/(\mathcal T_A s^2)$, i.e. $\nu = \mathcal T_A/h \gtrsim \mathcal T_A^2 s^2/\sigma_A^2$.
- read: seg:deriv-observation-noise-placement, seg:result-persistence-condition
