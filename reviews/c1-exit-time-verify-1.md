---
kind: review
author:
  name: c1-spike-verifier
  role: independent-verifier
sources:
  - spikes/spike-exit-time-model-s-2026-10-30/de-novo-feedback-1.md
written: 2026-10-30
---

# Prop A.1S(i), the stopped second-moment bound, checked against Cor A.1S.1

KR C.2 (item C1). This review carries the canon-level check from the independent pass on the exit-time spike in the typed form `vsect take` reads. The full argument, the Monte Carlo table, the replacement statements and the cascade list are in the source file, §1.

## C1 (check)
- target: segment:deriv-sector-condition
- at: 481943e4
- act: rederive
- line: derivation
- criterion: Does Prop A.1S(i), $\mathbb{E}[\lVert\delta(t\wedge\tau_R)\rVert^2] \leq \lVert\delta(0)\rVert^2e^{-2\alpha t} + n\sigma_w^2/(2\alpha)$ for all $t \geq 0$ under (A1) and (A2′) on $\mathcal B_R$, hold, and does (iii′)'s stated limit $n\sigma_w^2/(2\alpha R^2)$ follow from it?
- committed: after
- outcome: broken
- recheck: de-novo-feedback-1 §1. Three lines: $\mathbb{E}\lVert\delta_{t\wedge\tau}\rVert^2 \geq R^2P(\tau_R \leq t) \to R^2$ by Cor A.1S.1, while the bound tends to $(R^\ast_S)^2 \lt R^2$ under (ii). Numerically: OU with $n=2$, $\alpha=2$, $\sigma_w=R=1$, $\delta_0=0$, paths frozen at the sphere on exit. The stopped moment is $0.93$ at $t=2$ against the bound $0.5$.

Under the mean-square condition (ii), (i) is inconsistent with Cor A.1S.1, and (i) is the false one. The derivation's localization step (`:221`) applies Grönwall to the stopped moment. The decay term holds only on $\{t \lt \tau_R\}$, because mass frozen on the sphere does not decay, so Grönwall does not close.

- **What survives:**
  - the killed moment $\mathbb{E}[\lVert\delta_t\rVert^2;\tau_R \gt t] \leq \lVert\delta_0\rVert^2e^{-2\alpha t} + \tfrac{n\sigma_w^2}{2\alpha}(1-e^{-2\alpha t})$, via Itô on $e^{2\alpha t}V$;
  - (iv);
  - (i) and (iii′) under global A2′.
- **(iii′)'s inequality** $P(\lVert\delta_t\rVert \gt R) \leq \mathbb{E}\lVert\delta_{t\wedge\tau}\rVert^2/R^2$ is true, but its limit is $1$. Under local A2′ the region-aware fixed-time tail must combine the killed moment with an exit-time bound.
- **(i) and (iii′) together** bound $P(\tau_R \leq t)$ below one uniformly in $t$, which re-implies the infinite-horizon bound deleted in 2026-05-16.
- **Same shape elsewhere:** the Model S stopped bound at `#result-contraction-template` :61, and the citation at `#result-sector-persistence-template` :93.
