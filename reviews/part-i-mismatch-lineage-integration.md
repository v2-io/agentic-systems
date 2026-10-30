---
kind: review
author:
  name: Claude Opus 5.5 (C.1 integrator, A7/A10 lane)
  role: integrator
sources:
  - msc/inside-out-2026-10/c1-lanes/part-i-mismatch-lineage.md
  - msc/inside-out-2026-10/owner-review/integrator-items.md
written: 2026-10-30
---

# Part I mismatch objects and persistence lineage (A7, A10): the integrator's re-derivations

KR C.1. These are the checks the integrator re-ran before and while landing A7 and A10 in da38d358. They are the integrator's own; the KR asks for an independent verifier after this. The account with the scripts and the reasoning is the first source above.

## C1 (check)
- target: segment:deriv-sector-condition
- at: da38d358
- act: rederive
- line: derivation
- criterion: Is the state of the dynamics $\dot\delta = -F(\delta) + w$ the estimation error $\bar\delta = \bar o - \hat o$ rather than the innovation $o - \hat o$, and does the disturbance on it include channel noise injected by the correction?
- committed: before
- outcome: confirmed
- recheck: Scalar Kalman–Bucy $dx = s\,dW$, $dy = x\,dt + o\,dV$, $d\hat x = k(dy - \hat x\,dt)$ gives $de = -k e\,dt + s\,dW - k o\,dV$; the innovation increment $dy - \hat x\,dt$ is white for the optimal $k$ and has no contained dynamics.

The innovation has no dynamics a correction contains; the estimation error does, and its disturbance is $s\,dW - k o\,dV$.

## C2 (check)
- target: segment:deriv-sector-condition
- at: da38d358
- act: run
- line: simulation
- criterion: Model S steady state of a linear corrector at rate $\alpha$ with channel noise is $(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)/(2\alpha)$, minimized at $\alpha = \sigma_{\text{env}}/\sigma_\nu$ with value $\sigma_{\text{env}}\sigma_\nu$ (the Kalman–Bucy error), not $\sigma_{\text{env}}^2/(2\alpha)$.
- committed: before
- outcome: confirmed
- recheck: Euler–Maruyama, $s = 1$, $o = 0.5$, $dt = 10^{-3}$, 200 paths of $4\times 10^5$ steps; script `kb_check.py` in the account

Simulated MSE $0.622, 0.503, 0.624, 1.069$ at $k = 1, 2, 4, 8$ against the closed form $0.625, 0.500, 0.625, 1.063$; the environment-only form gives $0.500, 0.250, 0.125, 0.0625$.

## C3 (check)
- target: segment:deriv-sector-condition
- at: da38d358
- act: rederive
- line: derivation
- criterion: Model D with linear correction and channel noise bounded by $\bar\nu$: is the ultimate bound $R^\ast = \rho_{\text{env}}/\alpha + \bar\nu$?
- committed: before
- outcome: confirmed
- recheck: Disturbance $w_{\text{env}} - \alpha\nu$ has norm at most $\rho_{\text{env}} + \alpha\bar\nu$; Prop A.1 gives $R^\ast = (\rho_{\text{env}} + \alpha\bar\nu)/\alpha$.

## C4 (check)
- target: segment:result-persistence-condition
- at: da38d358
- act: rederive
- line: derivation
- criterion: "Two levers in $\mathcal T$": raising gain on fixed observations past the optimum enlarges the error; raising event rate lowers the channel-noise intensity ($\sigma_\nu^2 \propto 1/\nu$) and the minimum $n\sigma_{\text{env}}\sigma_\nu$.
- committed: before
- outcome: confirmed
- recheck: Follows from C2's closed form; $\nu$ independent events of variance $r$ per unit time give white-noise intensity $r/\nu$.

## C5 (check)
- target: segment:deriv-persistence-cost
- at: da38d358
- act: rederive
- line: derivation
- criterion: The continuous-time limit of the scalar Gauss–Markov sequential RDF $\tfrac12\log(a^2 + W/D)$ is $\sigma^2/(2D) - \lambda$, and Kalman–Bucy's Duncan rate $P/(2\sigma_o^2)$ equals it at $D = P$ for every $\lambda$.
- committed: before
- outcome: confirmed
- recheck: Expansion $a^2 + W/D = 1 - 2\lambda\Delta + \sigma^2\Delta/D + O(\Delta^2)$; Riccati $\sigma^2 - 2\lambda P - P^2/\sigma_o^2 = 0$; numerically at $(\lambda, \sigma, \sigma_o) = (0, 1, 0.5), (0.3, 1, 0.5), (1, 2, 0.3)$ the discrete bound over $\Delta$ converges to the Duncan rate as $\Delta \to 0$; script `srdf_kb_check.py` in the account

## C6 (check)
- target: segment:deriv-persistence-cost
- at: da38d358
- act: read
- line: imported
- criterion: Tanaka, Kim, Parrilo & Mitter 2017 state the scalar sequential RDF $\tfrac12\log(a^2 + w/D)$ (when positive) and its attainment by a linear-Gaussian sensor with a Kalman filter.
- committed: before
- outcome: confirmed
- recheck: arXiv 1411.7632 (ar5iv), Section V-A eq. (28) and Proposition 1 / Section V-A on the sensor-plus-Kalman realization

## C7 (check)
- target: segment:result-persistence-condition
- at: da38d358
- act: read
- line: imported
- criterion: Widrow, McCool, Larimore & Johnson 1976 state that gradient noise grows with the speed of adaptation, lag falls with it, and their sum is minimized where the two are equal.
- committed: before
- outcome: confirmed
- recheck: Proc. IEEE 64(8):1151, abstract and §I, full text registered in relata as widrow-1976-stationary

## C8 (check)
- target: segment:example-kalman
- at: da38d358
- act: run
- line: simulation
- criterion: For $q = 0.25$, $r_H = 1$: $P^- = 0.640$, $K_{ss} = 0.390$, $P = 0.390$, innovation RMS $1.28$; fixed-gain prior variance $V(K) = (q + K^2 r)/(1 - (1-K)^2)$ gives $0.982, 0.640, 0.940$ at $K = 0.15, 0.39, 0.81$; $P(\lvert e^-\rvert \gt 1.4) = 0.080$.
- committed: before
- outcome: confirmed
- recheck: Riccati closed form plus Monte Carlo of the discrete filter ($4\times 10^5$ steps per gain: $0.982, 0.639, 0.941$); script `example_kalman_numbers.py` in the account
