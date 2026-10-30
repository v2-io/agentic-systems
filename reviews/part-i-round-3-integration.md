---
kind: review
author:
  name: Claude Opus 5.5 (Part I round-3 integrator)
  role: integrator
sources:
  - msc/inside-out-2026-10/c1-lanes/part-i-round-3.md
  - msc/inside-out-2026-10/part-i-round-2-check.md
written: 2026-10-30
---

# Part I round 3 (the round-2 check integrated; the threshold drift derived): the integrator's re-derivations

KR C.1 ("Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier") and C.2 ("Strengthenings C1–C3 … are independently checked, then landed or refuted"), item C1. Top intent: "Complete 'in-place' refactor of ASF-- meta, all artifacts, and theory itself." These are the checks this integrator ran before landing b15e947d, each by its own derivation or its own implementation (scripts in the first source). The round-2 checker's findings were inputs to re-derive. Where this record departs from them, it says so. The KR asks for an independent verifier after this.

## C1 (check)
- target: segment:deriv-sector-condition
- at: b15e947d
- act: rederive
- line: derivation
- criterion: Lemma A.1S-τ.0's benchmark from the origin is the series $\alpha\Phi(0) = \tfrac12\sum_{k\geq1}\kappa_R^k/(k\,(n/2)_k) = (\kappa_R/n)\,{}_2F_2(1,1;2,\tfrac n2+1;\kappa_R)$, equal to the Lemma's $G/m$ integral and to Kersting et al. 2023 eq. (17).
- committed: before
- outcome: confirmed
- recheck: Integrate the concavity identity over $s\in[0,R^2]$, expand $(e^{\kappa x}-1)/x$ with $x = 1-t^2$, use $\int_0^1 t^{n-1}(1-t^2)^{k-1}dt = \tfrac12 B(\tfrac n2,k)$. mpmath at 30 digits: the series, the Lemma's integral and Kersting's (17) agree to all printed digits at $(n,\kappa_R) = (1,0.5), (2,4), (3,1.5), (3,6), (10,5), (20,40), (100,50)$ and $(5,9)$.

## C2 (check)
- target: segment:deriv-sector-condition
- at: b15e947d
- act: rederive
- line: derivation
- criterion: $\alpha\Phi(0)|_{\kappa_R=n/2} = \tfrac14(\ln n + \gamma_{\mathrm E}) + \sqrt\pi/(3\sqrt n) + O(n^{-1})$.
- committed: before
- outcome: confirmed
- recheck: Series term $\tfrac1k\prod_{j\lt k}(1+j/m)^{-1}$ with $m = n/2$, expanded to $\tfrac1k e^{-k^2/(2m)}(1 + \tfrac{k}{2m} + \tfrac{k^3}{6m^2})$; Mellin residue of $\Gamma(s)\zeta(1+2s)(2m)^s$ at $s = 0$ gives $\tfrac12\ln(2m) + \tfrac12\gamma_{\mathrm E}$ (checked numerically: error $\varepsilon/12$); Euler–Maclaurin gives $\tfrac23\sqrt{\pi/2}\,m^{-1/2}$. Numerically the residual after the first term times $\sqrt n$ is $0.570, 0.584, 0.5886, 0.5901, 0.5906$ at $n = 10^2 \ldots 10^6$ against $\sqrt\pi/3 = 0.5908$; after both terms, times $n$, $-0.208, -0.218, -0.221, -0.222, -0.222$.

This goes past the round-2 checker, who derived the leading term by Frullani on the integral and left the second coefficient as a numerical guess. The two routes to the leading constant are independent. The $O(n^{-1})$ order is the order of the neglected terms, and it is supported numerically, not proved.

## C3 (check)
- target: segment:deriv-sector-condition
- at: b15e947d
- act: run
- line: derivation
- criterion: On a fixed channel ($\sigma_{\text{env}} = 1$, $\sigma_\nu = 0.5$) the expected stay is maximized at $0.31K, 0.56K, 0.74K, 0.89K$ for $n = 1$, $\kappa_R(K) = 1, 2.25, 4, 9$, with maximum $1.11$ at $\kappa_R(K) = 1$; $d\Phi(0)/d\alpha = -\Phi(0)/K$ at $K$.
- committed: before
- outcome: confirmed
- recheck: Bounded scalar minimization of $-\alpha\Phi(0)/\alpha$ via the ${}_2F_2$ form; $n = 3$ maximizers $0.20K, 0.42K, 0.64K, 0.87K$. Central difference $-0.361311$ against $-\Phi(0)/K = -0.361311$.

## C4 (check)
- target: segment:deriv-sector-condition
- at: b15e947d
- act: run
- line: derivation
- criterion: The $\kappa_R$ increment that doubles $\alpha\Phi(0)$ is $1.01$ at $(3, 2.5)$, $0.96$ at $(3, 6)$, $7.5$ at $(100, 52)$, $1.9$ at $(100, 80)$, $1.20$ at $(100, 120)$, so "about $\log 2$" holds only for $\kappa_R \gg n/2$.
- committed: before
- outcome: confirmed
- recheck: Root-finding on the series; agrees with the round-2 checker's numbers. The leading-order formula $\ln 2/(1 - n/(2\kappa_R))$ is itself unreliable near threshold at large $n$ (18.0 against the exact 7.5 at $(100, 52)$), so canon states exact increments rather than that formula.

## C5 (check)
- target: segment:deriv-sector-condition
- at: b15e947d
- act: run
- line: derivation
- criterion: The radial corrector with $n = 2$, $\sigma_w = R = 1$, $g = 5$ except $g = 2$ on $0.485 \leq r \leq 0.515$ has mean exit time from the origin $3.57$, $3.9$ times $\Phi_2(0) = 0.921$; $\Phi_5(0) = 3.800$.
- committed: before
- outcome: confirmed
- recheck: Radial Andronov–Vitt–Pontryagin formula with the corrector's own drift, by quadrature: $3.5688$. The spike's Euler–Maruyama run gave $3.519 \pm 0.061$, ratio $3.82$ to $\Phi_2(0)$.

This departs from the round-2 checker's D3 on one point. Canon's "3.8×" was the instance's ratio to its *floor* benchmark $\Phi_2(0)$; that $\Phi_5(0) = 3.80$ is a coincidence. The checker's conclusion stands: the sentence named the wrong corrector and gave no parameters.

## C6 (check)
- target: segment:deriv-sector-condition
- at: b15e947d
- act: run
- line: derivation
- criterion: The small-noise asymptotic over exact $\Phi(0)$: $0.77$ at $(2,4)$, $0.93$ at $(2,16)$; at $\kappa_R = n/4$ above one for every $n$ from 1 to 1000 ($8.4$ at $(20,5)$, $8\,100$ at $(100,25)$); at $\kappa_R = n/2$ above one for $n \leq 5$ ($3.5$ at $n = 1$) and below beyond ($0.13$ at $n = 100$); about $0.5$ at $\kappa_R = n$ for large $n$; $0.75$ at $(100, 40)$.
- committed: after
- outcome: confirmed
- recheck: mpmath on the series and $\tfrac{\Gamma(n/2)}{2}\kappa^{-n/2}e^\kappa$.

The criterion was written after the run, because the run showed the round-2 checker's W3 to be incomplete. Canon's "anti-conservative exactly near the mean-square threshold" holds at threshold only for $n \leq 5$, and the asymptotic under-estimates there for larger $n$. Canon now says so.

## C7 (check)
- target: segment:deriv-sector-condition
- at: b15e947d
- act: read
- line: imported
- criterion: Ikeda & Watanabe 1977 Theorem 1.1, with the weakened hypothesis (1.3)′ under pathwise uniqueness, and Remark 1.1 (localization to $[0,S)$) say what canon's proof of Prop A.1S-τ(ii) uses.
- committed: before
- outcome: confirmed
- recheck: Read at the primary (Osaka University OUKA, ojm14_03_14.pdf, OCR text layer, pp. 619–622): continuous $\sigma(t,x)$ with an increasing modulus $\rho$, $\int_{0+}\rho^{-2} = \infty$; continuous $b_1 \lt b_2$; $\beta_1 \leq b_1(x_1)$, $\beta_2 \geq b_2(x_2)$, $x_1(0) \leq x_2(0)$ give $x_1 \leq x_2$; $b_1 \leq b_2$ suffices under pathwise uniqueness of one equation; Remark 1.1 as stated.

## C8 (check)
- target: segment:deriv-sector-condition
- at: b15e947d
- act: read
- line: imported
- criterion: Kersting, Orvieto, Proske & Lucchi 2023 Theorem 4 eq. (17), and Grebenkov 2015 eqs. (75)–(77), are the Lemma's integral and small-noise form under $\theta = \alpha$, $\sigma = \sigma_w$, $\kappa = kL^2/(2k_BT) = \alpha R^2/\sigma_w^2$.
- committed: before
- outcome: confirmed
- recheck: Read at the primary (arXiv:2208.04029, arXiv:1411.3598). Kersting's SDE is $dX = -\theta X\,dt + \sigma\,dB$; eq. (17) recomputed numerically equals the series at $(d, L) = (2, 2), (5, 3)$. Grebenkov (76) is $\tfrac{L^2}{D}\Gamma(d/2)e^\kappa/(4\kappa^{1+d/2})$ with $D = \sigma_w^2/2$, which is canon's $\tfrac{\Gamma(n/2)}{2\alpha}\kappa^{-n/2}e^\kappa$. Grebenkov states the exponential exit law at large $\kappa$ informally. Kersting's large-$d$ result is at a fixed radius, a different limit from the threshold asymptotic.

## C9 (check)
- target: segment:result-contraction-template
- at: b15e947d
- act: rederive
- line: derivation
- criterion: For $V = \xi^TM\xi$ the Itô drift is $\sigma_\xi^2\operatorname{tr}(M + \ldots) \leq c_{\text{Itô}}\,n\sigma_\xi^2 m_2$ with $c_{\text{Itô}} = 1$ at constant $M$, the killed bound has stationary scale $n\sigma_\xi^2c_{\text{Itô}}m_2/(2\lambda)$, and mean-square persistence is $\lambda R^2 \gt n\sigma_\xi^2c_{\text{Itô}}m_2/(2m_1)$, invariant under $M \to kM$ and reducing to Prop A.1S at $M = I$.
- committed: before
- outcome: confirmed
- recheck: $\tfrac12\operatorname{tr}(\sigma^2\nabla^2V) = \sigma^2\operatorname{tr}M \leq n\sigma^2m_2$; $\mathbb E\lVert\xi\rVert^2 \leq \mathbb EV/m_1$; at $M = I$, $\lambda R^2 \gt n\sigma^2/2$ is $\kappa_R \gt n/2$. The ray-integration step of the CT2 proof sketch was not re-derived (round-2 checker's open remark).

## C10 (check)
- target: segment:deriv-stochastic-non-exit
- at: b15e947d
- act: run
- line: simulation
- criterion: The table's exit probabilities from the origin by $T = 50, 200, 800, 3200$ are $0.003, 0.011, 0.042, 0.157$; $0.023, 0.093, 0.327, 0.796$; $0.842, 0.999, 1.000, 1.000$, with $\Phi(0) = 18735, 2016, 27.4$.
- committed: before
- outcome: confirmed
- recheck: Own conservative finite-difference Dirichlet generator on $[-R,R]$ (4000 interior points, weight $e^{-\alpha x^2/\sigma^2}$, symmetric tridiagonal eigen-solve); cross-check $1 - e^{-T/\Phi(0)}$ within $0.005$; $1/\lambda_1 = 18730, 2014, 26.7$.

## C11 (check)
- target: segment:detail-operationalization
- at: b15e947d
- act: rederive
- line: derivation
- criterion: The innovation's mean square exceeds the estimation error's by the channel-noise floor (term (iii) of #result-mismatch-decomposition), and for linear correction the total disturbance is $\sigma_w^2 = \sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2$ (Model S) and $\rho = \rho_{\text{env}} + \alpha\bar\nu$ (Model D), so the residual-based recipes estimate innovation properties and not $\rho$, $\sigma_w$, except for a noiseless channel.
- committed: before
- outcome: confirmed
- recheck: $o - \hat o = (o - \bar o) + (\bar o - \hat o)$, cross term zero under the fresh-noise assumption; the Setup algebra of #deriv-sector-condition. That the optimal filter's innovations are white is the innovations property.

## C12 (check)
- target: segment:def-mismatch-signal
- at: b15e947d
- act: rederive
- line: derivation
- criterion: For a linear-Gaussian model the state-and-law floor (term (ii)) is $\operatorname{tr}(HP^-H^T)$, the predictive error, attained by the Kalman filter; not the posterior $P$.
- committed: before
- outcome: confirmed
- recheck: The Bayes predictor of $o_t$ is $H\hat x_{t\mid t-1}$; its error is $H(x_t - \hat x_{t\mid t-1})$ with covariance $HP^-H^T$.

## C13 (check)
- target: segment:der-deliberation-cost
- at: b15e947d
- act: rederive
- line: derivation
- criterion: The one-step threshold $\lVert\bar\delta\rVert^2/(\lVert\bar\delta\rVert^2 + \sigma_\varepsilon^2)$ uses the realized error; it is the uncertainty-ratio gain only with $U_M = \mathbb E\lVert\bar\delta\rVert^2$ in its place.
- committed: before
- outcome: confirmed
- recheck: $\partial_\eta[(1-\eta)^2a + \eta^2s] \lt 0 \iff \eta \lt a/(a+s)$; averaging $a$ over the agent's uncertainty gives $U_M/(U_M + U_o)$.