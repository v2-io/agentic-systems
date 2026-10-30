---
kind: review
author:
  name: Claude Opus 5.5 (Part I round-2 checker)
  role: independent verifier
sources:
  - msc/inside-out-2026-10/part-i-round-2-check.md
written: 2026-10-30
---

# Part I round 2 (Prop A.1S, Prop A.1S-τ, the Model S window, the $\sigma_w$ convention): the independent check

KR C.1 ("Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier") and C.2 ("Strengthenings C1–C3 … are independently checked, then landed or refuted"), item C1. Top intent: "Complete 'in-place' refactor of ASF-- meta, all artifacts, and theory itself." This checks the landing in 33cfb14c..9e3ec279, re-derived from the segment text. Derivations, tables and scripts are in the source above. The mathematics that landed holds. The defects are in sentences that summarize it, and in adjacent text the landing edited or relies on.

## C1 (check)
- target: segment:deriv-sector-condition
- at: 9e3ec279
- act: rederive
- line: derivation
- criterion: Prop A.1S(i), the killed second-moment bound, holds under (A2') on the ball, and a stopped-moment bound with the decay term is false under (ii).
- committed: before
- outcome: confirmed
- recheck: Itô on $e^{2\alpha s}V$ to $t\wedge\tau_R$, drop the part on $\{\tau_R \leq t\}$; falsity from $R^2P(\tau_R \leq t) \leq \mathbb E\lVert\delta_{t\wedge\tau_R}\rVert^2$ and Cor A.1S.1.

## C2 (check)
- target: segment:deriv-sector-condition
- at: 9e3ec279
- act: rederive
- line: derivation
- criterion: Prop A.1S(ii)–(iv): the threshold equivalence, the global Grönwall and Markov steps, the composed local tail, and (iv) from the stopped identity without decay.
- committed: before
- outcome: confirmed
- recheck: By hand; the composed tail is $P(\tau_R \leq t) + \mathbb E[\lVert\delta_t\rVert^2;\tau_R \gt t]/r^2$ with the first term from Prop A.1S-τ(iii).

## C3 (check)
- target: segment:deriv-sector-condition
- at: 9e3ec279
- act: rederive
- line: derivation
- criterion: Lemma A.1S-τ.0: the exit-function integral, the incomplete-gamma form of $G$, concavity of $\Phi$ in $r^2$, and the Laplace endpoint asymptotic.
- committed: before
- outcome: confirmed
- recheck: Integrating factor $m$; substitution $v = \alpha s^2/\sigma_w^2$; $d\Phi/ds = -\sigma_w^{-2}\int_0^1 t^{n-1}e^{(\alpha r^2/\sigma_w^2)(1-t^2)}dt$; endpoint Laplace.

## C4 (check)
- target: segment:deriv-sector-condition
- at: 9e3ec279
- act: run
- line: simulation
- criterion: The quoted numbers of Lemma A.1S-τ.0 and the Kalman-cap paragraph: the threshold table $0.60 \ldots 1.89$, the exact/asymptotic ratios $1.29$ at $(2,4)$ and $1.07$ at $(2,16)$, and $\Phi(0) = 1.07, 0.87, 0.72, 0.56, 0.27$ at $\alpha = 0.5K \ldots 2K$.
- committed: before
- outcome: confirmed
- recheck: Own mpmath implementation of the $s = r^2$ form $\alpha\Phi(0) = \int_0^{\kappa_R}\!\int_0^1 t^{n-1}e^{u(1-t^2)}dt\,du$, independent of the $G/m$ quadrature; scripts in the source.

## C5 (check)
- target: segment:deriv-sector-condition
- at: 9e3ec279
- act: rederive
- line: derivation
- criterion: Prop A.1S-τ(i) (mean, both directions, equality under radial tightness) and (ii) (stochastic domination, $n \geq 2$ by same-noise radial comparison, $n = 1$ by Tanaka).
- committed: before
- outcome: confirmed
- recheck: Generator inequality and Dynkin with bounded and monotone convergence; first-exceedance argument on $D = r - \varrho$; local time does not charge $\{D \gt 0\}$. Start at the origin for $n \geq 2$ is closed by the squared-radius route (C6), not by the radial Itô step.

## C6 (check)
- target: segment:deriv-sector-condition
- at: 9e3ec279
- act: read
- line: imported
- criterion: Ikeda & Watanabe 1977, Theorem 1.1 with Remark 1.1, applies to $\xi = \lVert\delta\rVert^2$ with common diffusion coefficient $2\sigma_w\sqrt{\xi^+}$ and comparison drift $n\sigma_w^2 - 2\alpha\xi$, for every $n \geq 1$, as canon transcribes.
- committed: before
- outcome: confirmed
- recheck: Read at the primary (Osaka University OUKA, ojm14_03_14.pdf). Yamada modulus $\rho(u) = 2\sigma_w\sqrt u$, $\int_{0+}\rho^{-2} = \infty$; the drifts are equal, so the weakened hypothesis (1.3)' is used, which needs pathwise uniqueness of one equation, held by the benchmark's CIR-type SDE (Yamada–Watanabe); Remark 1.1 with $S = \tau_R$.

## C7 (check)
- target: segment:deriv-sector-condition
- at: 9e3ec279
- act: rederive
- line: derivation
- criterion: Prop A.1S-τ(iii) and its domination of Prop A.1S(iv); the derivation of the elementary bound in (iv); the Corollary 5 counterexample.
- committed: before
- outcome: confirmed
- recheck: $\Phi_\alpha(0) \geq R^2/(n\sigma_w^2)$ by (i) at floor 0 on the benchmark; chord bound from concavity; the elementary bound's substitutions by hand (its ratio numerics not re-run); $0.01 - \ln 0.01 = 4.615 \geq \ln 100$.

## C8 (check)
- target: segment:deriv-sector-condition
- at: 9e3ec279
- act: rederive
- line: derivation
- criterion: The Kalman-gain cap: $\kappa_R(\alpha)$ peaks at $K$ at $R^2/(2\sigma_{\text{env}}\sigma_\nu)$; $\Phi(0) = g(\kappa_R,n)/\alpha$ with $g$ increasing; $d\Phi(0)/d\alpha = -\Phi(0)/K$ at $K$; the stay maximizer lies strictly below $K$ and approaches it as $\kappa_R(K)$ grows.
- committed: before
- outcome: confirmed
- recheck: Algebra; numerical derivative $-0.3613$ against $-\Phi(0)/K = -0.3613$; maximizers $0.31K, 0.56K, 0.74K, 0.89K$ at $\kappa_R(K) = 1, 2.25, 4, 9$ ($n = 1$). The sentences that summarize this are F1.

## C9 (check)
- target: segment:deriv-sector-condition
- at: 9e3ec279
- act: rederive
- line: derivation
- criterion: Setup: with linear correction and gain-injected white channel noise the estimation error obeys $d\delta = -\alpha\delta\,dt + \sigma_{\text{env}}dW - \alpha\sigma_\nu dV$, steady state $n(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)/(2\alpha)$, minimized at the Kalman–Bucy gain with the Kalman–Bucy error; Model D bound $\rho_{\text{env}}/\alpha + \bar\nu$.
- committed: before
- outcome: confirmed
- recheck: Kalman–Bucy error SDE and steady-state Riccati by hand.

## C10 (check)
- target: segment:result-persistence-condition
- at: 9e3ec279
- act: rederive
- line: derivation
- criterion: The Model S window $\alpha \in (\alpha_-, \alpha_+)$, feasibility iff $R^2 \gt n\sigma_{\text{env}}\sigma_\nu$, $\alpha_-\alpha_+ = K^2$, $\ln(\alpha_+/K) = \operatorname{arccosh}(R^2/(n\sigma_{\text{env}}\sigma_\nu))$; the Model D form $\alpha(R - \bar\nu) \gt \rho_{\text{env}}$.
- committed: before
- outcome: confirmed
- recheck: Quadratic in $\alpha$ by hand; $\alpha_+/K = x + \sqrt{x^2 - 1}$ with $x = R^2/(n\sigma_{\text{env}}\sigma_\nu)$.

## C11 (check)
- target: segment:deriv-persistence-cost
- at: 9e3ec279
- act: rederive
- line: derivation
- criterion: Every linear corrector on the channel takes in $nK/2$ (the filter path determines the observation path; Duncan), the floor at a mis-tuned corrector's error is strictly lower, and the error contracts at $\lambda_s + \alpha$.
- committed: before
- outcome: confirmed
- recheck: $dy = (d\hat x + (\lambda_s+\alpha)\hat x\,dt)/\alpha$; no feedback from $\hat x$ to $x$, so mutual and directed information agree; AM–GM for $\alpha\sigma_{\text{env}}^2/(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2) \leq K/2$.

## C12 (check)
- target: segment:der-deliberation-cost
- at: 9e3ec279
- act: rederive
- line: derivation
- criterion: One update with gain $\eta$ on innovation $\bar\delta + \varepsilon$ lowers the mean-square estimation error exactly when $\eta \lt \lVert\bar\delta\rVert^2/(\lVert\bar\delta\rVert^2 + \sigma_\varepsilon^2)$.
- committed: before
- outcome: confirmed
- recheck: Derivative of $(1-\eta)^2\lVert\bar\delta\rVert^2 + \eta^2\sigma_\varepsilon^2$. That threshold is the uncertainty-ratio gain in expectation only (source, W7).

## C13 (check)
- target: segment:result-adversarial-tempo-advantage
- at: 9e3ec279
- act: rederive
- line: derivation
- criterion: The $3/2$ law under self-injected channel noise needs $\gamma_A\mathcal T_A \gg \mathcal T_B\sigma_{\nu,B}$ and $\gamma_B\mathcal T_B \gg \mathcal T_A\sigma_{\nu,A}$; the second fails for a gain-raised tempo ratio above about $\gamma_B/\sigma_{\nu,A}$.
- committed: before
- outcome: confirmed
- recheck: Algebra on the per-agent steady state $(\sigma_i^2 + \mathcal T_i^2\sigma_{\nu,i}^2)/(2\mathcal T_i)$.

## C14 (check)
- target: segment:example-kalman
- at: 9e3ec279
- act: rederive
- line: derivation
- criterion: Riccati numbers: high mode $P^- = 0.640$, $K = 0.390$; low mode $P^- = 1.630$, $K = 0.153$; $\nu K_{ss} = 1.95\ \text{s}^{-1}$, $-\nu\ln(1-K_{ss}) = 2.47\ \text{s}^{-1}$; $R^2 = 0.0064 \lt P^-$.
- committed: before
- outcome: confirmed
- recheck: $P^- = (q + \sqrt{q^2 + 4qr})/2$ with $q = 0.25$, $r = 1, 9$; $K = P^-/(P^- + r)$.

## C15 (check)
- target: segment:deriv-stochastic-non-exit
- at: 9e3ec279
- act: rederive
- line: derivation
- criterion: $P(V \lt n\sigma_w^2/(4\alpha)) = P(\chi^2_n \lt n) \in (0.5, 0.69)$ for the stationary OU benchmark, and $n\sigma_w^2/(4\alpha)$ is its stationary mean of $V$.
- committed: before
- outcome: confirmed
- recheck: $V = (\sigma_w^2/(4\alpha))\chi^2_n$; $P(\chi^2_1 \lt 1) = 0.683$, decreasing to $1/2$.

## C16 (check)
- target: segment:deriv-stochastic-non-exit
- at: 9e3ec279
- act: run
- line: simulation
- criterion: The simulation table's exit probabilities.
- committed: before
- outcome: narrowed
- recheck: Spectral solve of the Dirichlet generator on $[-R,R]$, cross-checked against $1 - e^{-T/\Phi(0)}$ ($\Phi(0) = 18735, 2016, 27.4$). Exact $0.157$ and $0.796$ at $T = 3200$ against the table's $0.114$ and $0.720$; $0.842$ at $T = 50$ against $0.781$.

The Monte Carlo is biased low by discrete monitoring. The qualitative claim holds, and more strongly with the exact values.

## C17 (check)
- target: segment:result-contraction-template
- at: 9e3ec279
- act: rederive
- line: derivation
- criterion: CT-S: with $c_{\text{Itô}} = 1$ at $M = I$ the killed bound reduces to Prop A.1S, and (CT-S-persist) $\lambda R^2 \gt n\sigma_\xi^2c\,m_2^2/(2m_1)$ is the mean-square fit.
- committed: before
- outcome: broken
- recheck: At $M = I$ the stated definition $\tfrac12\sigma_\xi^2\operatorname{tr}M \leq c\,m_2$ gives $c = n\sigma_\xi^2/2$, not 1. $\mathbb E\lVert\xi\rVert^2 \leq \mathbb EV/m_1 \leq n\sigma_\xi^2c\,m_2/(2\lambda m_1)$, so the fit is $m_2/m_1$, not $m_2^2/m_1$; the canon form is not invariant under $M \to kM$.

Pre-existing; the landing edited the surrounding paragraph.

## F1 (finding)
- target: segment:deriv-sector-condition
- at: 9e3ec279

Gain is credited with time it cannot buy. On a fixed channel $\kappa_R \leq R^2/(2\sigma_{\text{env}}\sigma_\nu)$, so the stay reachable by tuning the gain is bounded, and it peaks strictly below $K$ ($0.31K$–$0.89K$ for $\kappa_R(K) = 1$–$9$). These sentences say or imply otherwise: :293 "buys expected time in the region only up to the Kalman gain"; :351 "lengthens the stay only up to the Kalman gain"; the Prop A.1S-τ Findings Impact "up to the Kalman gain on a fixed channel"; `01-aat-core/INTRODUCTION.md` headline 2 "can be pushed past any lifetime … — up to the Kalman gain" (no gain pushes it past every lifetime on a fixed channel; information does); #impl-persistence-and-limits :33 and its misquotation row; #result-persistence-condition :130 "the expected stay … capped on a fixed channel at the Kalman gain". Supported form: the exponent peaks at $K$; the stay peaks below $K$ and falls monotonically past it; only information raises the cap.

## F2 (finding)
- target: segment:deriv-sector-condition
- at: 9e3ec279

Prop A.1S-τ(iv): "Doubling the required time, or halving the tolerated risk, costs about $\log 2$ in $\kappa_R$." The leading-order cost is $\ln 2/(1 - n/(2\kappa_R))$. Exact: $\Delta\kappa_R = 7.52$ at $(n, \kappa_R) = (100, 52)$, $4.88$ at $(100, 60)$, $1.01$ at $(3, 2.5)$. Near the threshold, where the paragraph says readers apply it, the sentence is anti-conservative by several times.

## F3 (finding)
- target: segment:deriv-sector-condition
- at: 9e3ec279

Prop A.1S-τ(v): "the dip corrector stays $3.8\times$ the benchmark" names Lemma A.1N's dip corrector, but the number is the spike's instance (d) (`04-numerics.md`: $n = 2$, $\sigma_w = R = 1$, floor 2, bulk gain 5 with the floor only on a thin shell, Euler–Maruyama), which behaves like a linear corrector at gain 5 ($3.52$ against $\Phi_5(0) = 3.80$). Give the instance and its parameters, or drop the number.

## F4 (finding)
- target: segment:deriv-sector-condition
- at: 9e3ec279

Two unqualified sentences that the segment's own Setup makes false past $K$ on a fixed channel: :18 "Increasing $\alpha$ tightens the typical scale and lengthens the expected stay in the region, exponentially in $\kappa_R$", and the first Findings Brief "Stronger correction tightens the *typical* scatter (the RMS radius shrinks as $1/\sqrt\alpha$)". Elsewhere in the segment the qualifier "at fixed $\sigma_w$" is present.

## F5 (finding)
- target: segment:deriv-sector-condition
- at: 9e3ec279

Ikeda & Watanabe 1977 has now been read at the primary and the application checks (C6). The sentences at :279, in Epistemic Status and in Related Work that say neither the author nor the verifier has read it are no longer true; they should say what was read. Kersting et al. 2023, Grebenkov 2015, Day 1983 and the heavy-tail sources remain unread at the primary.

## F6 (finding)
- target: segment:deriv-sector-condition
- at: 9e3ec279

Old Model S convention at :349: "GA-2S: $\mathbb E[\lVert w(t)\rVert^2] = \sigma_w^2$", against the landed per-coordinate convention ($\mathbb E\lVert w\rVert^2 = n\sigma_w^2$ per unit time) in the same segment, NOTATION GA-2S and #result-sector-condition-stability. #result-contraction-template CT3 carries the same form. Also `\Vertw(t)` at :39, :75, :91 is an undefined control sequence (no space), which fails to render.

## F7 (finding)
- target: segment:deriv-sector-condition
- at: 9e3ec279

Working Note at :410 restates the un-narrowed hand-off ("structural adaptation is *certain over an unbounded horizon*"; "continuity *requires* recurring structural … adaptation, and the Model-S no-go makes that requirement inevitable"), cites "(iii′)", which no longer exists, and uses "Three-Deaths", a retired name. Keep it as ideation, stated at the narrowed strength.

## F8 (finding)
- target: segment:deriv-sector-condition
- at: 9e3ec279

Strengthening for C.2. Canon's "drifting upward like $\tfrac14\ln n + 0.15$ … a computed trend, not a derived asymptotic" can be replaced by the derived leading term $\alpha\Phi(0)|_{\kappa_R = n/2} = \tfrac14(\ln n + \gamma) + O(n^{-1/2})$, $\gamma/4 = 0.1443$. Derivation in the source: $t = e^{-y}$, a two-region replacement to $n^{-1/2}F(\Delta/\sqrt n)$, then $\int_0^X\sqrt\pi e^{x^2}\operatorname{erfc}x\,dx = \ln X + \ln 2 + \gamma/2 + O(X^{-2})$ by Frullani. The remainder's order is sketched, and its coefficient (about $0.59$) is numerical. Residuals $0.0570, 0.0185, 0.00589, 0.00187$ at $n = 10^2 \ldots 10^5$.

## F9 (finding)
- target: segment:result-contraction-template
- at: 9e3ec279

CT-S (C17). The Itô constant is defined inconsistently with "$c_{\text{Itô}} = 1$ at $M = I$"; state it as $\sigma_\xi^2\operatorname{tr}(M + \ldots) \leq c_{\text{Itô}}\,n\sigma_\xi^2m_2$. (CT-S-persist) should read $\lambda R^2 \gt n\sigma_\xi^2c_{\text{Itô}}m_2/(2m_1)$; as written it changes under rescaling $M \to kM$.

## F10 (finding)
- target: segment:hyp-mismatch-dynamics
- at: 9e3ec279

$\rho$ still read as environmental at :14 ("new mismatch injection from environmental change (the disturbance term $\rho$)"), :16 and :38 ("the ratio of how fast the environment changes to how fast the agent adapts"), while :28 declares it total. This is the unanswered part of `review:part-i-mismatch-lineage-check-1` C11/F3.

## F11 (finding)
- target: segment:detail-operationalization
- at: 9e3ec279

The Model D and Model S estimators read $\hat\rho_{\det}$ and $\hat\sigma_w$ off $s_t = \lVert\delta_t\rVert$ taken from prediction-versus-observation residuals, the innovation. Canon's $\rho$ and $\sigma_w$ are the total disturbance on the unobserved estimation error, and a well-tuned filter's innovation is white, with no correction dynamics to subtract. The operational definitions estimate another quantity. This site is downstream of the A7/A10 change of persistence state, and no drain has reached it.

## F12 (finding)
- target: segment:deriv-stochastic-non-exit
- at: 9e3ec279

The simulation table understates exit (C16): exact $0.157, 0.796$ at $T = 3200$ against $0.114, 0.720$. Lemma A.1S-τ.0 now supplies the exact values without simulation.

## F13 (finding)
- target: segment:deriv-sector-condition
- at: 9e3ec279

Wording and minor items: the killed moment is described as "the scale of the mismatch while still certified" (also #result-persistence-condition :17 "RMS scale while certified", #result-sector-persistence-template), which reads as the conditional moment that (i) does not bound; (iii) says "no fixed-time tail for the unstopped process follows" and then gives one; the Lemma's "below the mean-square threshold the asymptotic over-estimates by orders of magnitude at large $n$" fails near threshold (asymptotic/exact $0.75$ at $(100, 40)$).

## F14 (finding)
- target: segment:example-kalman
- at: 9e3ec279

The example applies Prop A.1S-τ and the Kalman-gain cap to a discrete-time filter, outside the proposition's stated scope (continuous time). The conclusions are plausible (the small-noise exponent is $R^2/(2\mathrm{Var}_{ss})$ for a stationary Gaussian AR(1) too, minimized at the Kalman gain) and the feasibility conclusion holds by a factor of 100 on $P^-$, but neither is covered as written.

## F15 (finding)
- target: segment:result-persistence-condition
- at: 9e3ec279

:85 "For linear correction … $\alpha = \mathcal T$ exactly" against :95 "a gain past the optimum … moves $\alpha$, not $\mathcal T$": the identity holds at the optimal gain. The Findings Brief ("persists when its correction speed beats the rate…"; "loses bounded behavior") contradicts both the window and Lemma A.1N.

## F16 (finding)
- target: segment:deriv-sector-condition
- at: 9e3ec279

The 01-aat-core/OUTLINE.md figure caption says that for a corrector exactly as strong as its sector floor "failure follows" at the threshold. Lemma A.1N forces escape for that corrector under the worst-case outward disturbance, not under every disturbance of size $\rho$.
