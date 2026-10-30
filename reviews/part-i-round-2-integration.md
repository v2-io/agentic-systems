---
kind: review
author:
  name: Claude Fable 5.1 (Part I round-2 integrator)
  role: integrator
sources:
  - msc/inside-out-2026-10/part-i-round-2.md
  - msc/inside-out-2026-10/c1-lanes/part-i-check.md
  - spikes/spike-exit-time-model-s-2026-10-30/de-novo-feedback-1.md
written: 2026-10-30
---

# Part I round 2 (C1 exit time, Prop A.1S replacement, the Model S window): the integrator's re-derivations

KR C.1 and C.2 (item C1). Top intent: "Complete 'in-place' refactor of ASF-- meta, all artifacts, and theory itself." These are the checks the integrator ran before and while landing a728475f. Each checker's carve was treated as an input to re-derive, not text to transcribe; where a checker's statement was confirmed it is recorded as confirmed by this mind's own derivation or run, and where it was not re-derived it is listed under findings as open. The scripts are in the first source. The KR asks for an independent verifier after this.

## C1 (check)
- target: segment:deriv-sector-condition
- at: a728475f
- act: rederive
- line: derivation
- criterion: The killed second-moment bound (i), $\mathbb E[\lVert\delta_t\rVert^2;\ \tau_R \gt t] \leq \lVert\delta_0\rVert^2e^{-2\alpha t} + \tfrac{n\sigma_w^2}{2\alpha}(1 - e^{-2\alpha t})$, holds under (A2') on the ball; a stopped-moment bound with the decay term is false under (ii).
- committed: before
- outcome: confirmed
- recheck: Itô on $e^{2\alpha s}V$ to $t\wedge\tau_R$, drop the $\{\tau_R \leq t\}$ part; the frozen mass carries no decay. Exact-discretization OU Monte Carlo ($n = 2$, $\alpha = 2$, $\sigma_w = R = 1$, 8000 paths): stopped moment $0.33, 0.51, 0.74, 0.93, 0.995$ at $t = 0.25, 0.5, 1, 2, 4$ against the would-be bound $0.5$; killed moment $0.22, 0.17, 0.09, 0.03, 0.002$ under (i)'s $0.32, 0.43, 0.49, 0.50, 0.50$.

Independent of the verifier's Euler run (`recheck.py` §5 in the account). The three-line argument from Cor A.1S.1 also checks: $R^2P(\tau_R \leq t) \leq \mathbb E\lVert\delta_{t\wedge\tau_R}\rVert^2 \to R^2 \gt n\sigma_w^2/(2\alpha)$.

## C2 (check)
- target: segment:deriv-sector-condition
- at: a728475f
- act: rederive
- line: derivation
- criterion: Prop A.1S-τ(i): $\mathbb E_x\tau_R \geq \Phi_{\alpha,n,\sigma_w,R}(\lVert x\rVert)$ under (S), (A1), (A2') on the ball; equality under radial tightness; upper bound with a ceiling $\bar\alpha$.
- committed: before
- outcome: confirmed
- recheck: Radial generator $\mathcal Lv = -\Phi'\hat\delta^TF + \tfrac{\sigma_w^2}{2}(\Phi'' + \tfrac{n-1}{r}\Phi')$; $-\Phi' \geq 0$ and $\hat\delta^TF \geq \alpha r$ give $\mathcal Lv \geq \mathcal L_{\mathrm{OU}}\Phi = -1$; Dynkin on the stopped process; the $t \to \infty$ limit uses only that $v$ is bounded and $v(\delta_{\tau_R}) = 0$.

## C3 (check)
- target: segment:deriv-sector-condition
- at: a728475f
- act: rederive
- line: derivation
- criterion: Prop A.1S-τ(ii): stochastic domination of the exit time by the OU benchmark, $n \geq 2$ by a same-noise radial comparison, $n = 1$ by Tanaka.
- committed: before
- outcome: confirmed
- recheck: $dr = \beta_t\,dt + \sigma_w\,dB_t$ with $\beta_t \leq b_\alpha(r_t)$; $D = r - \varrho$ has no martingale part; $b_\alpha$ strictly decreasing gives $\dot D \lt 0$ where $D \gt 0$; first-exceedance contradiction; polarity of the origin for $n \geq 2$; boundary regularity of the benchmark closes the touching case. The Ikeda–Watanabe route is cited, not read (F2 below).

## C4 (check)
- target: segment:deriv-sector-condition
- at: a728475f
- act: run
- line: simulation
- criterion: Lemma A.1S-τ.0's integral gives $\alpha\Phi(0) = 0.596, 0.659, 0.706, 0.777, 0.889, 1.016, 1.202, 1.353, 1.890$ at $\kappa_R = n/2$ for $n = 1, 2, 3, 5, 10, 20, 50, 100, 1000$; the margin values $0.71, 1.57, 3.12, 12.0, 51.2$ at $n = 3$.
- committed: before
- outcome: confirmed
- recheck: mpmath (30 digits), incomplete-gamma form of $G$, quadrature of $G/m$ on $[0, R]$; `recheck.py` §1. Agrees with the spike's table and the verifier's $n = 100, 1000$ values to four digits. The $\tfrac14\ln n$ drift is a computed trend ($\alpha\Phi(0) - \tfrac14\ln n = 0.20, 0.16$ at $n = 100, 1000$), not a derived asymptotic, and canon says so.

## C5 (check)
- target: segment:deriv-sector-condition
- at: a728475f
- act: rederive
- line: derivation
- criterion: The leading-order form $\kappa_R - \tfrac n2\log\kappa_R \geq \log\tfrac{2\alpha L}{\epsilon\Gamma(n/2)}$ is not a sufficient condition for $P_0(\tau_R \leq L) \leq \epsilon$.
- committed: before
- outcome: confirmed
- recheck: Left side tends to $+\infty$ as $\kappa_R \to 0$. Counterexample $n = 2$, $\alpha = R = 1$, $\sigma_w = 10$, $L = 1$, $\epsilon = 0.02$: condition holds ($4.615 \geq 4.605$), exact $\Phi(0) = 0.00501$ against the needed $50$; `recheck.py` §2.

The spike's Corollary 5 second display is therefore stated in canon as an asymptotic only.

## C6 (check)
- target: segment:deriv-sector-condition
- at: a728475f
- act: rederive
- line: derivation
- criterion: The elementary lower bound on $\Phi(0)$ in Prop A.1S-τ(iv) (for $2\kappa_R \gt n - 1$, any $s \in (0, \kappa_R)$) holds and approaches the exact value.
- committed: before
- outcome: confirmed
- recheck: $G$ increasing; $\varphi' $ increasing with $\varphi'(R) = (2\kappa_R - n + 1)/R$; $\int_a^R e^\varphi \geq (e^{\varphi(R)} - e^{\varphi(a)})/\varphi'(R)$; substitution checked by hand including $(\sigma_w^2/\alpha)^{n/2}R^{2-n}/\sigma_w^2 = \kappa_R^{1-n/2}/\alpha$. Ratio bound/exact, maximized over $s$: $0.57, 0.74, 0.91, 0.97$ ($n = 1$; $\kappa_R = 2, 4, 8, 16$), $0.62, 0.87, 0.96$ ($n = 2$; $4, 8, 16$), $0.69, 0.97, 0.99$ ($n = 20$; $20, 40, 80$), $0.80, 0.97, 0.99$ ($n = 100$; $75, 100, 200$); `recheck.py` §3.

## C7 (check)
- target: segment:deriv-sector-condition
- at: a728475f
- act: rederive
- line: derivation
- criterion: Prop A.1S-τ(iii) is at least as tight as Prop A.1S(iv) from every start: $1 - (\Phi(\lVert x\rVert) - L)/\Phi(0) \leq (\lVert x\rVert^2 + n\sigma_w^2L)/R^2$.
- committed: before
- outcome: confirmed
- recheck: $d\Phi/d(r^2) = -\tfrac{1}{\sigma_w^2}\int_0^1 t^{n-1}e^{(\alpha r^2/\sigma_w^2)(1-t^2)}dt$ decreases in $r$, so $\Phi$ is concave in $r^2$ and $\Phi(r) \geq \Phi(0)(1 - r^2/R^2)$; Theorem (i) at floor $0$ gives $\Phi(0) \geq R^2/(n\sigma_w^2)$ (Brownian exit by Dynkin on $\lVert\delta\rVert^2$).

## C8 (check)
- target: segment:result-persistence-condition
- at: a728475f
- act: rederive
- line: derivation
- criterion: With $\sigma_w^2 = \sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2$ the Model S condition is $\alpha \in (\alpha_-, \alpha_+)$ with $\alpha_\pm = (R^2 \pm \sqrt{R^4 - n^2\sigma_{\text{env}}^2\sigma_\nu^2})/(n\sigma_\nu^2)$; feasible iff $R^2 \gt n\sigma_{\text{env}}\sigma_\nu$; $\alpha_-\alpha_+ = K^2$; $\ln(\alpha_+/K) = \operatorname{arccosh}(R^2/(n\sigma_{\text{env}}\sigma_\nu))$.
- committed: before
- outcome: confirmed
- recheck: Quadratic $n\sigma_\nu^2\alpha^2 - 2R^2\alpha + n\sigma_{\text{env}}^2 \lt 0$ by hand; grid of 400,000 gains at $R^2 = 0.4, 0.5, 0.6, 1, 3$ ($\sigma_{\text{env}} = 1$, $\sigma_\nu = 0.5$, $n = 1$): no window at $0.4, 0.5$; analytic and grid endpoints agree to four places; product $4.0000 = K^2$; log half-width equals the arccosh; `recheck.py` §4. Model D form $\alpha(R - \bar\nu) \gt \rho_{\text{env}}$ by substitution.

## C9 (check)
- target: segment:deriv-sector-condition
- at: a728475f
- act: rederive
- line: derivation
- criterion: $\kappa_R(\alpha) = \alpha R^2/(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)$ is maximized at $\alpha = K$ with value $R^2/(2\sigma_{\text{env}}\sigma_\nu)$; the linear corrector's $\Phi(0) = g(\kappa_R(\alpha), n)/\alpha$ decreases for $\alpha \gt K$; its maximizer lies strictly below $K$.
- committed: before
- outcome: confirmed
- recheck: $d\kappa_R/d\alpha = 0$ at $\alpha^2\sigma_\nu^2 = \sigma_{\text{env}}^2$; scaling $u = Rv$ in Lemma A.1S-τ.0 gives $\Phi(0) = g(\kappa_R, n)/\alpha$ with $g$ increasing; for $\alpha \gt K$ both factors fall; $\tfrac{d}{d\alpha}\ln\Phi(0)\big|_K = -1/K$. Numerically ($n = 1$, $\sigma_{\text{env}} = 1$, $\sigma_\nu = 0.5$, $R = 1$): argmax of $\kappa_R$ at $2.000 = K$, $\kappa_{\max} = 1.0000$; $\Phi(0) = 1.07, 0.87, 0.72, 0.56, 0.27$ at $\alpha = 0.5K, 0.8K, K, 1.25K, 2K$; `recheck.py` §6.

The verifier's phrase "tenure is capped at the Kalman gain" is true of the exponent; the tenure maximizer itself sits below $K$. Canon states both.

## C10 (check)
- target: segment:deriv-persistence-cost
- at: a728475f
- act: rederive
- line: derivation
- criterion: Every linear filter $d\hat x = -(\lambda_s + \alpha)\hat x\,dt + \alpha\,dy$ on the same channel takes in information at the Kalman–Bucy rate $P/(2\sigma_\nu^2) = K/2$ per component, so the bound at a mis-tuned filter's error is slack.
- committed: before
- outcome: confirmed
- recheck: The filter equation is invertible in the observation path ($dy = (d\hat x + (\lambda_s + \alpha)\hat x\,dt)/\alpha$), so $I(x;\hat x) = I(x;y)$, which Duncan gives as $\tfrac{1}{2\sigma_\nu^2}\int P_t\,dt$ with $P_t$ the optimal error. $D(\alpha) \gt P$ for $\alpha \neq K$ on both sides; the floor $n\alpha\sigma_{\text{env}}^2/(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)$ exceeds $n\alpha/2$ iff $\alpha \lt K$ and is below $nK/2$ for every $\alpha \neq K$.

## C11 (check)
- target: segment:der-deliberation-cost
- at: a728475f
- act: rederive
- line: derivation
- criterion: For one linear update with gain $\eta$ on the innovation $\bar\delta + \varepsilon$, the post-update mean-square estimation error $(1-\eta)^2\lVert\bar\delta\rVert^2 + \eta^2\sigma_\varepsilon^2$ decreases in $\eta$ iff $\eta \lt \lVert\bar\delta\rVert^2/(\lVert\bar\delta\rVert^2 + \sigma_\varepsilon^2)$.
- committed: before
- outcome: confirmed
- recheck: Derivative $-2(1-\eta)\lVert\bar\delta\rVert^2 + 2\eta\sigma_\varepsilon^2$; the lag part $\lVert(1-\eta)\bar\delta\rVert$ falls by $\Delta\eta\lVert\bar\delta\rVert$, the benefit term's form.

## C12 (check)
- target: segment:example-kalman
- at: a728475f
- act: rederive
- line: derivation
- criterion: Low-mode steady state $P^- = 1.630$, $K_{ss} = 0.153$; high-mode $\mathcal T_{ss} = \nu K_{ss} = 1.95\ \text{s}^{-1}$, exact per-step rate $-\nu\ln(1 - 0.390) = 2.47\ \text{s}^{-1}$; the Model S structural trigger $R^2 = 0.0064 \lt P^- = 0.640$.
- committed: before
- outcome: confirmed
- recheck: Riccati $P^- = (q + \sqrt{q^2 + 4qr})/2$ with $q = 0.25$, $r = 9$: $(0.25 + 3.0104)/2 = 1.6302$, $K = 1.6302/10.6302 = 0.1534$; $5 \times 0.390 = 1.95$; $-5\ln 0.61 = 2.47$.

## C13 (check)
- target: segment:result-adversarial-tempo-advantage
- at: a728475f
- act: rederive
- line: derivation
- criterion: With self-injected channel noise, agent $i$'s Model S steady state is $(\sigma_i^2 + \mathcal T_i^2\sigma_{\nu,i}^2)/(2\mathcal T_i)$, so the fixed-$\sigma$ $3/2$ derivation requires $\gamma_A\mathcal T_A \gg \mathcal T_B\sigma_{\nu,B}$ and $\gamma_B\mathcal T_B \gg \mathcal T_A\sigma_{\nu,A}$, the second failing for a gain-raised tempo ratio above about $\gamma_B/\sigma_{\nu,A}$.
- committed: before
- outcome: confirmed
- recheck: Substitution of the Setup's $\sigma_w^2(\alpha)$ into the segment's ratio with $\alpha_i = \mathcal T_i$; algebra only. The regimes under the gain-dependent disturbance are not re-derived (F1).

## F1 (finding)
- target: segment:result-adversarial-exponent-regimes
- at: a728475f

The exponent regimes ($b = 3/2$, $b \to 1/2$) are derived at fixed noise intensity. Under $\sigma_w^2(\alpha) = \sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2$ the coupling-dominant law needs the scope condition now stated at #result-adversarial-tempo-advantage; the full regime map with self-injected noise, and the question whether pushing a target's gain out of its window from above is a distinct regime, are not derived. Same status for #result-per-dimension-persistence, #deriv-matrix-persistence-condition and #deriv-discrete-sector-condition under the total disturbance (exact at fixed disturbance; the reading changes). Narrows `question:model-s-total-disturbance-downstream` rather than closing it.

## F2 (finding)
- target: segment:deriv-sector-condition
- at: a728475f

Ikeda & Watanabe 1977 Thm 1.1 (the published comparison cited for Prop A.1S-τ(ii)), Kersting et al. 2023 Thm 4, Grebenkov 2015 eq. (75), Day 1983 and the heavy-tail sources have not been read at the primary by the spiker, the verifier or this integrator; the spike's literature scan read them (Day: bibliography only). Canon marks each. The self-contained proof is the basis for (ii), so nothing rests on the unread citation, but a primary read would let the citation carry weight. Project Euclid and relata did not return the Ikeda–Watanabe text when tried.

## F3 (finding)
- target: segment:deriv-sector-condition
- at: a728475f

Anisotropic noise: the verifier's time-change sketch (exponent $\alpha R^2/\lambda_{\max}(\Sigma_w)$, crude prefactor, two Monte Carlo instances) is noted in Prop A.1S-τ's scope as not landed. It wants a verifier before canon.

## F4 (finding)
- target: segment:result-contraction-template
- at: a728475f

CT-S is now stated as the killed moment, with the stopped-with-decay form named false. The exit-time comparison is not transferred to weighted metrics; whether a radial comparison in the $M$-norm goes through (and with what benchmark) is open.
