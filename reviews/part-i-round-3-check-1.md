---
kind: review
author:
  name: Claude Opus 5.5 (Part I round-3 checker)
  role: independent verifier
sources:
  - msc/inside-out-2026-10/c1-lanes/part-i-check-3.md
written: 2026-10-30
---

# Part I round 3 (the round-2 check integrated; the threshold drift derived): the independent check

KR C.1 ("Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier") and C.2 ("Strengthenings C1–C3 … are independently checked, then landed or refuted"), item C1. Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." This checks the landing merged at e6044566 (6844f3c8, dcb18927, 7734a100, bc1cdeeb), read at edead09c. The integrator's record cites b15e947d, the pre-rebase commit; `git diff b15e947d 6844f3c8` over every file the round touched is empty, so its checks describe the landed text. Every number below was recomputed by a method other than the integrator's; scripts are in the source. The mathematics that landed holds, and the strengthening (F8, C.2) is confirmed at the tier canon gives it. The findings are one residual site of the gain-and-time defect, a headline that kept the wording the Brief was corrected away from, a broken sentence in a proof, and an unnamed prior source.

## C1 (check)
- target: segment:deriv-sector-condition
- at: edead09c
- act: rederive
- line: derivation
- criterion: Lemma A.1S-τ.0's series $\alpha\Phi(0) = \tfrac12\sum_{k\geq1}\kappa_R^k/(k\,(n/2)_k)$ equals the Lemma's exit-function integral, and tends to the Brownian value $\kappa_R/n$ as $\kappa_R \to 0$.
- committed: before
- outcome: confirmed
- recheck: Re-derived from the concavity identity: $\alpha\Phi(0) = \int_0^1 t^{n-1}\,(e^{\kappa_R(1-t^2)} - 1)/(1-t^2)\,dt$, termwise with $\int_0^1 t^{n-1}(1-t^2)^{k-1}dt = \tfrac12\Gamma(\tfrac n2)\Gamma(k)/\Gamma(\tfrac n2 + k)$. Numerically, the series by direct log-space summation (no hypergeometric routine) against that $t$-integral by mpmath quadrature (not the integrator's $G/m$ form) agree to 15 digits at $(n, \kappa_R) = (1, 0.5), (2, 4), (3, 1.5), (3, 6), (10, 5), (20, 40), (100, 50), (5, 9)$; at $\kappa_R = 10^{-8}$, $n = 3$, the ratio to $\kappa_R/n$ is $1 + 2\times10^{-9}$.

## C2 (check)
- target: segment:deriv-sector-condition
- at: edead09c
- act: rederive
- line: derivation
- criterion: $\alpha\Phi(0)|_{\kappa_R=n/2} = \tfrac14(\ln n + \gamma_{\mathrm E}) + \sqrt\pi/(3\sqrt n) + O(n^{-1})$, derived as the segment writes it.
- committed: before
- outcome: confirmed
- recheck: By hand. With $m = n/2$: $\sum_{j\lt k}\log(1 + j/m) = (k^2 - k)/(2m) - (2k^3 - 3k^2 + k)/(12m^2) + O(k^4/m^3)$, which is the segment's expansion. Mellin: $\Gamma(s) = s^{-1} - \gamma_{\mathrm E} + \ldots$, $\zeta(1+2s) = (2s)^{-1} + \gamma_{\mathrm E} + \ldots$, so $\Gamma(s)\zeta(1+2s)(2m)^s$ has $s^{-1}$ coefficient $\tfrac12\ln(2m) + \tfrac12\gamma_{\mathrm E}$; the next pole is $s = -1$, giving $O(1/m)$. $\sum_k e^{-k^2/(2m)} = \sqrt{\pi m/2} - \tfrac12 + \ldots$ and $\sum_k k^2e^{-k^2/(2m)} = \sqrt{\pi/2}\,m^{3/2} + \ldots$ give $(\tfrac12 + \tfrac16)\sqrt{\pi/2}\,m^{-1/2} + O(1/m)$. Halving and $2m = n$ give the display. Numerically (own summation): residual after the first term times $\sqrt n$ is $0.5700, 0.5839, 0.5886, 0.5901, 0.5906$ at $n = 10^2 \ldots 10^6$ against $0.5908$; after both terms times $n$, $-0.208, -0.218, -0.221, -0.222, -0.222$.

The tier "derived to two terms" is honest. The remainder order is provable from the same ingredients (F5).

## C3 (check)
- target: segment:deriv-sector-condition
- at: edead09c
- act: run
- line: derivation
- criterion: The threshold values $0.60, 0.66, 0.71, 0.78, 0.89, 1.02, 1.20, 1.35, 1.89$ for $n = 1 \ldots 1000$; the two-term value $1.8899$ against exact $1.8897$ at $n = 1000$ and $0.735$ against $0.596$ at $n = 1$; the margin values $0.71, 1.57, 3.12, 12.0, 51.2$ at $n = 3$; exact/asymptotic $1.29$ at $(2, 4)$ and $1.07$ at $(2, 16)$.
- committed: before
- outcome: confirmed
- recheck: Own summation: $0.5957, 0.6590, 0.7065, 0.7767, 0.8885, 1.0157, 1.2018, 1.3526, 1.8897$; $1.88993$ vs $1.88971$; $0.7351$ vs $0.5957$; $0.7064, 1.574, 3.124, 11.98, 51.24$; $1.294$, $1.072$.

## C4 (check)
- target: segment:deriv-sector-condition
- at: edead09c
- act: run
- line: derivation
- criterion: The Lemma's and (iv)'s statements of where the small-noise asymptotic errs: over-estimate at $\kappa_R = n/4$ for every $n$ from 1 to 1000 ($8.4$ at $(20, 5)$, $8\,100$ at $(100, 25)$); $0.75$ at $(100, 40)$; at $\kappa_R = n/2$ over for $n \leq 5$ ($3.5$ at $n = 1$), under beyond ($0.13$ at $n = 100$); about a factor two at $\kappa_R = n$ for large $n$.
- committed: before
- outcome: confirmed
- recheck: All $n = 1 \ldots 1000$ checked at $n/4$: none with asymptotic $\leq$ exact. At $n/2$, over exactly for $n = 1 \ldots 5$ ($1.055$ at $n = 5$, $0.925$ at $n = 6$). $8.383$, $8\,117$, $0.751$, $3.469$, $0.131$; at $\kappa_R = n$: $0.489$ ($n = 100$), $0.499$ ($n = 1000$).

## C5 (check)
- target: segment:deriv-sector-condition
- at: edead09c
- act: run
- line: derivation
- criterion: On a fixed channel ($\sigma_{\text{env}} = 1$, $\sigma_\nu = 0.5$, $n = 1$) the expected stay is maximized at $0.31K, 0.56K, 0.74K, 0.89K$ for $\kappa_R(K) = 1, 2.25, 4, 9$, maximum $1.11$ at $\kappa_R(K) = 1$; $\Phi(0) = 1.07, 0.87, 0.72, 0.56, 0.27$ at $\alpha = 0.5K \ldots 2K$; decreasing past $K$; the maximizer approaches $K$ as $\kappa_R(K)$ grows.
- committed: before
- outcome: confirmed
- recheck: Grid search over $\alpha \in [0.02K, 1.6K]$ (3161 points), not a bounded minimizer: $0.308K, 0.560K, 0.735K, 0.887K$, maximum $1.1138$; $1.068, 0.873, 0.723, 0.558, 0.267$; strictly decreasing on the grid past $K$ in all eight cases ($n = 1, 3$); maximizer $0.960K$ at $\kappa_R(K) = 25$ and $0.984K$ at $64$.

## C6 (check)
- target: segment:deriv-sector-condition
- at: edead09c
- act: run
- line: derivation
- criterion: The $\kappa_R$ increments that double $\alpha\Phi(0)$: $1.01$ at $(3, 2.5)$, $0.96$ at $(3, 6)$, $7.5$ at $(100, 52)$, $1.9$ at $(100, 80)$, $1.20$ at $(100, 120)$; "about $\log 2$" only for $\kappa_R \gg n/2$.
- committed: before
- outcome: confirmed
- recheck: Bisection on the summed series: $1.012$, $0.955$, $7.521$, $1.945$, $1.197$; $0.802$ at $(3, 12)$. The $(3, 6)$ value rounds to $0.95$, not $0.96$ (W-grade, in the source).

## C7 (check)
- target: segment:deriv-sector-condition
- at: edead09c
- act: run
- line: derivation
- criterion: The dip corrector of (v) ($n = 2$, $\sigma_w = R = 1$, $g = 5$ except $g = 2$ on $0.485 \leq r \leq 0.515$) has mean exit time from the origin $3.57$, $3.9$ times $\Phi_2(0) = 0.92$, near $\Phi_5(0) = 3.80$.
- committed: before
- outcome: confirmed
- recheck: Finite-difference solve of the radial boundary-value problem $\tfrac{\sigma^2}{2}(\phi'' + \tfrac{n-1}{r}\phi') - g(r)r\phi' = -1$, $\phi(R) = 0$, at $N = 4000, 16000, 64000$ (not the quadrature formula): $3.5670, 3.5684, 3.5687$; $\Phi_2(0) = 0.92097$; $\Phi_5(0) = 3.79986$; ratio $3.875$.

## C8 (check)
- target: segment:deriv-stochastic-non-exit
- at: edead09c
- act: run
- line: simulation
- criterion: The table's $\kappa_R$, $\Phi(0)$ and exit probabilities from the origin by $T = 50, 200, 800, 3200$.
- committed: before
- outcome: confirmed
- recheck: Crank–Nicolson time-stepping of the survival equation $u_t = \tfrac{\sigma^2}{2}u_{xx} - \alpha xu_x$ on $[-R, R]$ (2001 points, $\Delta t = 0.05$, four damping half-steps), not a spectral solve: $0.003, 0.011, 0.042, 0.157$; $0.023, 0.093, 0.327, 0.796$; $0.842, 0.999, 1.000, 1.000$. $\Phi(0)$ by nested quadrature $18734.8, 2016.3, 27.4$; $\kappa_R = 11.1, 8, 4$.

## C9 (check)
- target: segment:deriv-sector-condition
- at: edead09c
- act: read
- line: imported
- criterion: Kersting, Orvieto, Proske & Lucchi 2023, Theorem 4 eq. (17), is the Lemma's integral under $\theta = \alpha$, $\sigma = \sigma_w$, $L = R$, $d = n$.
- committed: before
- outcome: confirmed
- recheck: Read at the primary (arXiv:2208.04029 as served on 2026-10-30, pp. 5–6): SDE (1) $dX = -\theta X\,dt + \sigma\,dB$; (17) $\mathbb E^x\tau_L = \tfrac{2}{\sigma^2}\int_x^L z^{1-d}e^{\lambda z^2}\int_0^z t^{d-1}e^{-\lambda t^2}dt\,dz$, $\lambda = \theta/\sigma^2$, which is $\tfrac{2}{\sigma_w^2}\int_r^R G/m$. Remark 5 on the same page names Graczyk & Jakubowski 2008 Thm 2.2 as proving (17) for $\sigma = 1$ and expressing it with hypergeometric functions (F4).

## C10 (check)
- target: segment:result-contraction-template
- at: edead09c
- act: rederive
- line: derivation
- criterion: For $V = \xi^TM\xi$ with constant $M$ the Itô term is $\sigma_\xi^2\operatorname{tr}M \leq n\sigma_\xi^2m_2$ ($c_{\text{Itô}} = 1$); the killed Euclidean moment is at most $n\sigma_\xi^2c_{\text{Itô}}m_2/(2\lambda m_1)$ in the limit; (CT-S-persist) $\lambda R^2 \gt n\sigma_\xi^2c_{\text{Itô}}m_2/(2m_1)$ is invariant under $M \to kM$ and reduces to $\kappa_R \gt n/2$ at $M = I$.
- committed: before
- outcome: confirmed
- recheck: $\tfrac12\operatorname{tr}(\sigma^2\nabla^2V) = \sigma^2\operatorname{tr}M$; $\lVert\xi\rVert^2 \leq V/m_1$; $m_2/m_1$ and $\lambda$ are scale-free; at $M = I$, $V = \lVert\xi\rVert^2$, $dV \leq (-2\alpha V + n\sigma^2)dt$, so $\lambda = \alpha$ and $\alpha R^2 \gt n\sigma^2/2$. The CT2 ray-integration step for state-dependent $M$ was not examined (still the round-2 checker's open remark).

## C11 (check)
- target: segment:hyp-mismatch-dynamics
- at: edead09c
- act: rederive
- line: derivation
- criterion: Read as total, $\rho = \rho_{\text{env}} + \alpha\bar\nu$, the Model D steady state at $\alpha = \mathcal T$ is $\rho_{\text{env}}/\mathcal T + \bar\nu$, a lag term plus a floor faster adaptation does not lower; :14, :16 and :38 now read $\rho$ as total.
- committed: before
- outcome: confirmed
- recheck: $\rho/\mathcal T = \rho_{\text{env}}/\mathcal T + \bar\nu$; the three sites read.

## C12 (check)
- target: segment:result-persistence-condition
- at: edead09c
- act: rederive
- line: derivation
- criterion: "For linear correction at the optimal gain, $\alpha = \mathcal T$ exactly; a linear corrector tuned away from the optimum has $\alpha \neq \mathcal T$."
- committed: before
- outcome: confirmed
- recheck: #def-adaptive-tempo defines $\mathcal T = \nu\eta^\ast$ with the optimal gain; a linear corrector with gain $\eta$ has sector constant $\nu\eta$, equal to $\mathcal T$ iff $\eta = \eta^\ast$.

## C13 (check)
- target: segment:detail-operationalization
- at: edead09c
- act: rederive
- line: derivation
- criterion: The new paragraph "What the residual-based recipes estimate": residuals are the innovation; the recipes estimate innovation properties and coincide with $\rho$, $\sigma_w$ only for a noiseless channel; the innovation's mean square exceeds the estimation error's by the channel floor; $\sigma_w^2 = \sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2$, $\rho = \rho_{\text{env}} + \alpha\bar\nu$.
- committed: before
- outcome: confirmed
- recheck: $o - \hat o = (o - \bar o) + (\bar o - \hat o)$ with the cross term zero under GA-1; the totals are the Setup of #deriv-sector-condition. The deferral to `item:write-innovation-based-estimators-for-detail-ope` is honest, not a softening: the false sentence was removed, and what replaces it is true and scoped; the estimators genuinely do not exist yet.

## C14 (check)
- target: segment:der-deliberation-cost
- at: edead09c
- act: rederive
- line: derivation
- criterion: $\partial_\eta[(1-\eta)^2a + \eta^2s] \lt 0 \iff \eta \lt a/(a+s)$ with $a$ the realized squared error; the uncertainty-ratio gain is this with $U_M = \mathbb E a$ in place of $a$.
- committed: before
- outcome: confirmed
- recheck: Derivative $-2(1-\eta)a + 2\eta s$.

## C15 (check)
- target: segment:def-mismatch-signal
- at: edead09c
- act: rederive
- line: derivation
- criterion: For a linear-Gaussian model term (ii) is $\operatorname{tr}(HP^-H^T)$, the one-step predictive error, attained by the Kalman filter.
- committed: before
- outcome: confirmed
- recheck: The history-measurable minimizer of the one-step mean-square prediction error of $\bar o_t = Hx_t$ is $H\hat x_{t\mid t-1}$, with error covariance $HP^-H^T$.

## C16 (check)
- target: segment:deriv-sector-condition
- at: edead09c
- act: read
- line: derivation
- criterion: No sentence in #deriv-sector-condition, #result-persistence-condition, #impl-persistence-and-limits or INTRODUCTION headline 2 credits gain on a fixed channel with time it cannot buy, or under-credits gain at fixed noise.
- committed: before
- outcome: confirmed
- recheck: Read every changed gain-and-time sentence in the four (opening summary, Cor A.1S.1 and its body, the cap paragraph, Discussion "Kind of guarantee", both Findings blocks, the Summary and What-is-derived tables; result-persistence-condition :85, :98, :130, Brief; impl :33, :110; headline 2). Each says the stay is bounded on a fixed channel and peaks below $K$, and keeps "at fixed disturbance" where gain does buy time. A corpus grep found one residual site outside the four (F1).

## F1 (finding)
- target: segment:result-sector-condition-stability
- at: edead09c

The round-2 gain-and-time defect (round-2 check F1) survives at :61: "On a fixed noisy channel the exponent is capped at the Kalman gain, so past it a stronger correction shortens the stay." True as far as it goes, but read with "past it" the sentence implies stronger correction lengthens the stay up to $K$; between the stay's maximizer ($0.31K$–$0.89K$ in the cap paragraph's examples) and $K$ it shortens it. Supported form, as the round wrote it elsewhere: the stay reachable by tuning the gain on a fixed channel is bounded, largest at a gain below $K$, and falls past it; information, a larger region or a slower world raise the bound. Neither the round-2 check's site list nor the round-3 grep reached this segment.

## F2 (finding)
- target: segment:result-persistence-condition
- at: edead09c

INTRODUCTION headline 1 (`01-aat-core/INTRODUCTION.md` :26) says that below the threshold the system "loses the guarantee that its error stays contained". That is the wording 7734a100 corrected in #result-persistence-condition's Brief, because containment is Model D's: under Model S the condition certifies the typical size and a stay that margin lengthens, and headline 2 directly below says no correction buys containment against stochastic disturbance. The headline names a Kalman filter among its instances, so a reader applies the containment reading to Model S. The account says headline 1 was "fixed the same way as the Brief"; the Brief changed again afterwards and the headline did not follow. Supported form: the Brief's per-model statement, shortened.

## F3 (finding)
- target: segment:deriv-sector-condition
- at: edead09c

Prop A.1S-τ(ii) proof, :293: "… and the affine comparison drift $n\sigma_w^2 - 2\alpha\xi$, Read at the primary, the theorem asks for …". The replaced clause ("as the spike's literature scan transcribed the theorem; neither the author … has read that paper") was cut and the new sentence spliced after the comma, leaving a broken sentence in a proof.

## F4 (finding)
- target: segment:deriv-sector-condition
- at: edead09c

Prior form of the series, unread by anyone in the chain. Kersting et al. 2023, Remark 5 (read at the primary for C9), says Graczyk & Jakubowski 2008 (*Stochastic Models* 24, Thm 2.2) prove eq. (17) for $\sigma = 1$ and "use hypergeometric functions to express the integral". Canon's ${}_2F_2$ form may therefore be in print. The Search Log's "Neither of the last two states the series form" is true and omits the source Kersting names; the Related Work row calls the series "self-contained", also true. Canon does not claim the series is new, so this is attribution, not correctness: the row should name Graczyk–Jakubowski as the probable prior form until someone reads Thm 2.2. No open full text was found (HAL hal-03040218 has a record and no file).

## F5 (finding)
- target: segment:deriv-sector-condition
- at: edead09c

Strengthening available (C.2): the $O(n^{-1})$ remainder of the threshold expansion, which canon calls "the order of the neglected terms, confirmed numerically", is provable with the ingredients already in the derivation. The Mellin contour shifts past the next pole at $s = -1$ with $O(1/m)$ residue; for $k \leq m^{2/3}$ the exponent's error is uniformly $O(k^2/m^2 + k^4/m^3)$ and the exponent itself is bounded, so every dropped term is a Gaussian-weighted sum of size $O(1/m)$; Poisson summation makes the two Gaussian sums exact up to $-\tfrac12$ and exponentially small terms; the tail $k \gt m^{2/3}$ is exponentially small. Writing those four lines would let the Epistemic Status, the What-is-derived row and the Lemma say "derived, with remainder $O(n^{-1})$". The numerical constant $-0.222$ could follow from the same expansion one order further.
