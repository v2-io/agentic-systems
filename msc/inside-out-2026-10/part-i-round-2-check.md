*KR C.1 — "Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier" — and C.2 — "Strengthenings C1–C3 … are independently checked, then landed or refuted" — item C1, with A3 and the A7 round-2 findings. Top intent: "Complete 'in-place' refactor of ASF-- meta, all artifacts, and theory itself."*

# Part I round 2: the independent check

The typed record is `reviews/part-i-round-2-check-1.md` (taken into vsect). This file carries the derivations, numbers and scripts behind it. I read the landing at 9e3ec279 (commits 33cfb14c..9e3ec279) from the segment text, without the integrator's re-derivations open, and only read `part-i-round-2.md` and the spike's numerics afterwards to locate where numbers came from. Every segment cited below is unchanged between 9e3ec279 and e9f50e94 except `#example-kalman`, `#impl-orient-cascade`, `NOTATION.md` and `01-aat-core/OUTLINE.md`, which other lanes edited in between; nothing I say about them depends on those edits.

## What holds

The mathematics that landed is right. I re-derived each of the following by hand, and recomputed every number canon quotes with my own implementation.

- **Prop A.1S(i), the killed moment.** Itô on $e^{2\alpha s}V$ to $t \wedge \tau_R$, $2\alpha V - \delta^T F \leq 0$ on the ball, drop the non-negative part on $\{\tau_R \leq t\}$, multiply by $2e^{-2\alpha t}$. The stopped moment with a decay term is false under (ii) in three lines: $R^2 P(\tau_R \leq t) \leq \mathbb E\lVert\delta_{t\wedge\tau_R}\rVert^2$ and $P(\tau_R \leq t) \to 1$ by Cor A.1S.1, while the would-be bound tends to $n\sigma_w^2/(2\alpha) \lt R^2$.
- **Prop A.1S(ii)–(iv).** The equivalence $R^\ast_S \lt R \Leftrightarrow \kappa_R \gt n/2$; the global Grönwall and Markov steps; the composed local tail $P(\lVert\delta_t\rVert \gt r) \leq P(\tau_R \leq t) + \mathbb E[\lVert\delta_t\rVert^2; \tau_R \gt t]/r^2$ with the first term from Prop A.1S-τ(iii); (iv) from the stopped identity without the decay term.
- **Lemma A.1S-τ.0.** The ODE with integrating factor $m$, the incomplete-gamma form of $G$, $\Phi'(0) = 0$, concavity in $s = r^2$ via $d\Phi/ds = -\sigma_w^{-2}\int_0^1 t^{n-1}e^{(\alpha r^2/\sigma_w^2)(1-t^2)}\,dt$, and the Laplace endpoint asymptotic $\Phi(0) \sim \tfrac{\Gamma(n/2)}{2\alpha}\kappa_R^{-n/2}e^{\kappa_R}$.
- **Prop A.1S-τ(i).** $\mathcal Lv \geq \mathcal L_{\mathrm{OU}}\Phi = -1$ from $-\Phi' \geq 0$ and $\hat\delta^TF \geq \alpha r$; Dynkin; the limit by bounded and monotone convergence; the ceiling direction with the inequalities reversed; equality under radial tightness.
- **Prop A.1S-τ(ii).** For $n \geq 2$ the radial SDE, $\beta_t \leq b_\alpha(r_t)$, $D = r - \varrho$ absolutely continuous with $\dot D \lt 0$ wherever $D \gt 0$, the first-exceedance contradiction, and boundary regularity of the benchmark at the touching time. For $n = 1$ the Tanaka form, where the local time of $\delta$ does not charge $\{D \gt 0\}$ and the reflection of $\varrho$ only lowers $D$. One rigor gap, closed by the published route: from $x = 0$ with $n \geq 2$, Itô for $r$ is not available at $t = 0$. The squared-radius comparison below has no singularity there.
- **Ikeda & Watanabe 1977, read at the primary** (Osaka University repository, `ir.library.osaka-u.ac.jp/repo/ouka/all/7664/ojm14_03_14.pdf`, OCR text). Theorem 1.1: a common continuous diffusion coefficient $\sigma(t,x)$ with $\lvert\sigma(t,x) - \sigma(t,y)\rvert \leq \rho(\lvert x - y\rvert)$, $\int_{0+}\rho^{-2} = \infty$; drifts $b_1 \lt b_2$; $x_1(0) \leq x_2(0)$; $\beta_1(t) \leq b_1(t, x_1(t))$, $\beta_2(t) \geq b_2(t, x_2(t))$; then $x_1 \leq x_2$ a.s., and $b_1 \leq b_2$ suffices when one of the two equations has pathwise uniqueness. Remark 1.1 localizes to $[0, S)$ for a stopping time $S$. Applied to $\xi = \lVert\delta\rVert^2$: $d\xi = (n\sigma_w^2 - 2\delta^TF)\,dt + 2\sigma_w\sqrt{\xi}\,dB$, the coefficient $2\sigma_w\sqrt{x^+}$ has modulus $\rho(u) = 2\sigma_w\sqrt u$ with $\int_{0+}\rho^{-2} = \infty$, $\beta_1 = n\sigma_w^2 - 2\delta^TF \leq n\sigma_w^2 - 2\alpha\xi$, the benchmark's squared radius has exactly that affine drift, the two drifts are equal so the weakened hypothesis is the one used, and the benchmark's CIR-type equation has pathwise uniqueness (Yamada–Watanabe). Remark 1.1 with $S = \tau_R$ covers the local sector condition. The application is as canon transcribed it, for every $n \geq 1$ at once, including the start at the origin.
- **Prop A.1S-τ(iii)** and its comparison with (iv): $\Phi_\alpha(0) \geq R^2/(n\sigma_w^2)$ by (i) with floor $0$ applied to the benchmark itself, and the chord bound $\Phi(r) \geq \Phi(0)(1 - r^2/R^2)$ from concavity.
- **Prop A.1S-τ(iv)**, the elementary bound: derivation checked by hand, including $(\sigma_w^2/\alpha)^{n/2}R^{2-n}/\sigma_w^2 = \kappa_R^{1-n/2}/\alpha$. I did not re-run its ratio numerics.
- **The Corollary 5 counterexample.** $0.01 - \ln 0.01 = 4.615 \geq \ln 100 = 4.605$, and $\Phi(0) \approx R^2/(n\sigma_w^2) = 0.005$.
- **The Kalman-gain cap.** $\kappa_R(\alpha)$ peaks at $K$ with value $R^2/(2\sigma_{\text{env}}\sigma_\nu)$; $\Phi(0) = g(\kappa_R, n)/\alpha$ with $g(\kappa, n) = 2\kappa\int_0^1\!\int_0^v (t/v)^{n-1}e^{\kappa(v^2 - t^2)}\,dt\,dv$ increasing; $d\Phi(0)/d\alpha = -\Phi(0)/K$ at $K$ (numerically $-0.3613$ against $-0.3613$). A remark that may help readers: $\kappa_R = R^2/(2\,\mathbb E\lVert\delta\rVert^2_{ss}/n)$, so "the exponent peaks at the Kalman gain" is the same fact as "the steady-state variance is smallest there".
- **The window** in `#result-persistence-condition`: the quadratic, the roots, $\alpha_-\alpha_+ = K^2$, $\ln(\alpha_+/K) = \operatorname{arccosh}(R^2/(n\sigma_{\text{env}}\sigma_\nu))$, feasibility, and the Model D form $\alpha(R - \bar\nu) \gt \rho_{\text{env}}$.
- **The Setup's Model S closed form**: $d\delta = -\alpha\delta\,dt + \sigma_{\text{env}}\,dW - \alpha\sigma_\nu\,dV$, steady state $n(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)/(2\alpha)$, minimized at the Kalman–Bucy gain with the Kalman–Bucy error.
- **`#deriv-persistence-cost`.** The corrector $d\hat x = -(\lambda_s + \alpha)\hat x\,dt + \alpha\,dy$ gives error contraction $\lambda_s + \alpha$ and $D(\alpha) = (\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)/(2(\lambda_s + \alpha))$. The filter path determines the observation path, so $I(x;\hat x) = I(x;y)$. With no feedback from $\hat x$ to $x$ this equals the directed information (Massey). Duncan gives $P/(2\sigma_\nu^2) = K/2$ per component. The floor at $D(\alpha)$ is strictly below it by AM–GM. Holding a target $D$ with $\alpha \neq K$ needs a channel whose intake $K'/2$ exceeds $\sigma_{\text{env}}^2/(2D)$.
- **`#der-deliberation-cost`'s one-step derivation**, `#result-adversarial-tempo-advantage`'s scope algebra, `#deriv-stochastic-non-exit`'s $P(\chi^2_n \lt n) \in (0.5, 0.683]$, `#example-kalman`'s Riccati numbers (high mode $P^- = 0.640$, $K = 0.390$; low mode $P^- = (q + \sqrt{q^2 + 4qr})/2 = 1.630$, $K = 0.153$; $\nu K = 1.95$, $-\nu\ln(1 - K) = 2.47$).

Numbers, from an implementation independent of the spike's and the integrator's. I used the $s = r^2$ form, $\alpha\Phi(0) = \int_0^{\kappa_R}\!\int_0^1 t^{n-1}e^{u(1-t^2)}\,dt\,du$, rather than the $G/m$ quadrature. Threshold table $0.5957, 0.6590, 0.7064, 0.7767, 0.8885, 1.0157, 1.2018, 1.3526, 1.8897$ for $n = 1, 2, 3, 5, 10, 20, 50, 100, 1000$, which agrees with canon to its printed digits. Exact over asymptotic: $1.294$ at $(n, \kappa_R) = (2, 4)$, $1.072$ at $(2, 16)$. Kalman-cap example: $\Phi(0) = 1.068, 0.873, 0.723, 0.558, 0.267$ at $\alpha = 0.5K, 0.8K, K, 1.25K, 2K$.

## Defects in what landed

### D1. Gain is credited with time it cannot buy on a fixed channel

The derivation in Prop A.1S-τ's cap paragraph is right. Several sentences that summarize it are not. On a fixed channel $\kappa_R(\alpha) \leq R^2/(2\sigma_{\text{env}}\sigma_\nu)$, so the expected stay reachable by tuning the gain is bounded. The expected stay is maximized strictly below $K$. Computed maximizers of $\Phi(0)$ over $\alpha$ ($\sigma_{\text{env}} = 1$, $\sigma_\nu = 0.5$):

| $n$ | $R$ | $\kappa_R(K)$ | $\arg\max/K$ | $\max\Phi(0)$ | $\Phi(0)$ at $K$ |
|---|---|---|---|---|---|
| 1 | 1.0 | 1.00 | 0.308 | 1.114 | 0.723 |
| 1 | 1.5 | 2.25 | 0.560 | 3.708 | 2.863 |
| 1 | 2.0 | 4.00 | 0.735 | 15.9 | 13.72 |
| 1 | 3.0 | 9.00 | 0.887 | 1358 | 1279 |
| 3 | 1.5 | 2.25 | 0.423 | 0.927 | 0.656 |
| 3 | 2.0 | 4.00 | 0.644 | 2.665 | 2.176 |
| 3 | 3.0 | 9.00 | 0.868 | 88.8 | 82.8 |

So between the maximizer and $K$, a stronger correction already shortens the stay. Sentences that say otherwise or imply it:

- `01-aat-core/INTRODUCTION.md` headline 2. "What correction strength buys instead is time … so the certain event can be pushed past any lifetime at a margin cost logarithmic in that lifetime — up to the Kalman gain". Correction strength on a fixed channel cannot push exit past any lifetime: the reachable $\kappa_R$ is capped. What pushes it past any lifetime is margin in $\kappa_R$ from any source, and on a fixed environment that means information (smaller $\sigma_\nu$), as the body itself says ("what buys time without limit is information … not gain").
- `#deriv-sector-condition` :293 "correction strength buys expected time in the region only up to the Kalman gain"; :351 "on a fixed noisy channel it lengthens the stay only up to the Kalman gain"; the Prop A.1S-τ Findings Impact "… exponentially in $\kappa_R$ at fixed disturbance, up to the Kalman gain on a fixed channel".
- `#impl-persistence-and-limits` :33 "on a fixed noisy channel it buys time only up to the Kalman gain", and the misquotation-catalog row "(… capped at the Kalman gain on a fixed channel)".
- `#result-persistence-condition` :130 "the expected stay … capped on a fixed channel at the Kalman gain" (the stay is not what is capped at $K$).

What the derivation supports: the exponent rises to its maximum at $K$; the expected stay peaks at a gain below $K$ that approaches $K$ as $\kappa_R(K)$ grows (0.31K to 0.89K above), and falls monotonically past $K$; the stay reachable by gain on a fixed channel is bounded; only information raises the cap. This is also my answer to `question:the-front-door-sentences-say-gain-buys-time-only`.

### D2. "Doubling the lifetime costs about $\log 2$ in $\kappa_R$" holds only far from threshold

Prop A.1S-τ(iv) says "Doubling the required time, or halving the tolerated risk, costs about $\log 2$ in $\kappa_R$". From $\kappa_R - \tfrac n2\ln\kappa_R$ the leading-order cost is $\ln 2/(1 - n/(2\kappa_R))$, which is $\ln 2$ only for $\kappa_R \gg n/2$. Exact $\Delta\kappa_R$ to double $\alpha\Phi(0)$:

| $n$ | $\kappa_R$ | exact $\Delta\kappa_R$ | $\ln 2/(1 - n/(2\kappa_R))$ |
|---|---|---|---|
| 3 | 2.5 | 1.012 | 1.73 |
| 3 | 6 | 0.955 | 0.92 |
| 3 | 12 | 0.802 | 0.79 |
| 100 | 52 | 7.52 | 18.0 |
| 100 | 60 | 4.88 | 4.16 |
| 100 | 80 | 1.95 | 1.85 |
| 100 | 120 | 1.197 | 1.19 |

Near the mean-square threshold, which the same paragraph names as where a reader applies the formula, the cost is several times $\log 2$. The sentence is anti-conservative there, the trap the segment warns about two sentences earlier for Corollary 5's form. The "cost logarithmic in $L/\epsilon$" statements are asymptotically right and can stay.

### D3. The "3.8×" in Prop A.1S-τ(v) belongs to a different corrector

"(the dip corrector stays $3.8\times$ the benchmark)". In context ("the dip corrector of the Remark after A.1N" in (i)) this names Lemma A.1N's corrector ($g \geq 10$, dip to $0.1$ at $r = 0.5$). The number is the spike's instance (d) in `04-numerics.md`: $n = 2$, $\sigma_w = R = 1$, floor $\alpha = 2$, bulk gain $5$ with the floor only on a shell of width $0.03$ at $r = 0.5$, Euler–Maruyama with discrete monitoring, which biases means upward by a few percent. Its expected exit time ($3.52$) sits just under the bulk-gain benchmark $\Phi_5(0) = 3.80$, so the corrector behaves like a linear corrector at its bulk gain. Lemma A.1N's corrector at any modest noise would stay astronomically longer. The qualitative sentence stands; the number needs its instance and parameters, or should go.

### D4. Unqualified "stronger correction tightens the scale" survives inside the segment that disproves it

`#deriv-sector-condition` :18 (the opening): "Increasing $\alpha$ tightens the typical scale and lengthens the expected stay in the region, exponentially in $\kappa_R$". The first Findings Brief (:359): "Stronger correction tightens the *typical* scatter (the RMS radius shrinks as $1/\sqrt\alpha$)". The Setup of the same segment makes both false past $K$ on a fixed channel, and the second false past the stay maximizer. Elsewhere in the segment (Corollary text, Discussion, Interpretation) the qualifier "at fixed $\sigma_w$" is present; these two lack it.

### D5. The Ikeda–Watanabe sentence is now false as written

Canon (:279, Epistemic Status, Related Work) says Ikeda–Watanabe 1977 "has not been read at the primary by the author or the verifier". It now has been read, and the application checks (above). For the integrator: the citation can carry weight, and those sentences should say what was read. Kersting et al. 2023, Grebenkov 2015, Day 1983 and the heavy-tail sources remain unread at the primary by anyone in the chain; I did not read them.

## Pre-existing defects in text the landing edited or relies on

### P1. `result-contraction-template` CT-S: the Itô constant and the persistence condition

The Itô-correction bound is stated as $\tfrac12\sigma_\xi^2\operatorname{tr}(M + \dots) \leq c_{\text{Itô}}m_2$, with "$c_{\text{Itô}} = 1$" when $M = I$. At $M = I$ the left side is $n\sigma_\xi^2/2$, so the stated definition gives $c_{\text{Itô}} = n\sigma_\xi^2/2$, not $1$. The bound that follows ($\tfrac{n\sigma_\xi^2c_{\text{Itô}}m_2}{2\lambda}$) needs $\sigma_\xi^2\operatorname{tr}(M + \dots) \leq c_{\text{Itô}}\,n\sigma_\xi^2 m_2$, which is dimensionless with $c = 1$ for constant $M$ and $V = \xi^TM\xi$. Second, (CT-S-persist) reads $\lambda R^2 \gt n\sigma_\xi^2c\,m_2^2/(2m_1)$. Derivation: $\mathbb E\lVert\xi\rVert^2 \leq \mathbb EV/m_1 \leq n\sigma_\xi^2c\,m_2/(2\lambda m_1)$, so mean-square fit is $\lambda R^2 \gt n\sigma_\xi^2c\,m_2/(2m_1)$. Scale test: under $M \to kM$, $m_1, m_2 \to km_1, km_2$ and $c$ is unchanged, so the canon right side scales by $k$ while the left does not. The condition as written is not invariant under rescaling the metric. (CT-D-persist) has the invariant ratio $\sqrt{m_1/m_2}$. CT3 also still reads $\mathbb E\lVert w\rVert^2 = \sigma_\xi^2$ (see P2).

### P2. The old Model S convention survives at two sites

`#deriv-sector-condition` :349 (Discussion, "Two disturbance models") states "GA-2S: $\mathbb E[\lVert w(t)\rVert^2] = \sigma_w^2$", against the landed convention $\mathbb E\lVert w\rVert^2 = n\sigma_w^2$ per unit time in the same segment, `NOTATION.md` GA-2S and `#result-sector-condition-stability`. `#result-contraction-template` CT3 carries the same form. Also in `#deriv-sector-condition`: `\Vertw(t)` at :39, :75, :91 is an undefined control sequence (no space after `\Vert`), which fails in KaTeX/LaTeX. md-press does not flag it.

### P3. `#hyp-mismatch-dynamics` still reads $\rho$ as environmental in three places

:14 "grows at the rate of new mismatch injection from environmental change (the disturbance term $\rho$)", :16 "$\rho/\mathcal T$ — the ratio of how fast the environment changes to how fast the agent adapts", :38 the same gloss under the Model D steady state. The segment now declares $\rho$ total at :28. This is the residue of `review:part-i-mismatch-lineage-check-1` C11/F3 ("its summary and Model D gloss read $\rho$ as environmental"), so I leave that finding open.

### P4. `#detail-operationalization` estimates $\rho$ and $\sigma_w$ from the wrong object

Its estimators take $s_t = \lVert\delta_t\rVert$ "measurable from prediction-versus-observation residuals", the innovation, and read $\hat\rho_{\det}$ and $\hat\sigma_w$ off its increments. Canon's $\rho$ and $\sigma_w$ are now the total disturbance on the estimation error, which the agent does not observe, and the innovation of a well-tuned filter is white, with no correction dynamics to subtract. The operational definitions therefore estimate something else, and no segment says what. This is downstream of the A7/A10 change of persistence state rather than of round 2. It is a "one reading per symbol" site that no drain has reached.

### P5. A Working Note restates the claim the landing narrowed everywhere else

`#deriv-sector-condition` :410: "the corrected (iii′)+dichotomy says structural adaptation is *certain over an unbounded horizon* for long-lived language-constituted agents … continuity *requires* recurring structural (not just parametric) adaptation, and the Model-S no-go makes that requirement inevitable". This is the un-narrowed hand-off that is open at `#sketch-structural-adaptation-genericity`. "(iii′)" no longer exists in the segment. "Three-Deaths" is a retired name for what canon now calls the deaths taxonomy (four deaths). The ideation can stay as ideation, stated at the narrowed strength.

### P6. `#deriv-stochastic-non-exit`'s simulation table understates exit

Exact exit probabilities for its three rows, by a spectral solve of the Dirichlet generator on $[-R, R]$, and independently from $1 - e^{-T/\Phi(0)}$ with $\Phi(0)$ from the Lemma ($\kappa_R = 11.1, 8, 4$; $\Phi(0) = 18735, 2016, 27.4$), agree to three digits:

| row | $T = 50$ | $200$ | $800$ | $3200$ |
|---|---|---|---|---|
| 1 exact / table | 0.003 / 0.002 | 0.011 / 0.010 | 0.042 / 0.030 | 0.157 / 0.114 |
| 2 exact / table | 0.023 / 0.020 | 0.093 / 0.074 | 0.327 / 0.276 | 0.796 / 0.720 |
| 3 exact / table | 0.842 / 0.781 | 0.999 / 0.998 | 1.000 | 1.000 |

The table's Monte Carlo is biased low by discrete monitoring. The point it illustrates is stronger with the exact values, which Lemma A.1S-τ.0 now supplies without simulation.

## Strengthening (C.2): the threshold drift is derived

Canon says $\alpha\Phi(0)$ at $\kappa_R = n/2$ drifts "like $\tfrac14\ln n + 0.15$ … a computed trend, not a derived asymptotic". It can be derived, and the constant is $\gamma/4 = 0.1443$ ($\gamma$ Euler's constant):

$$\alpha\,\Phi(0)\big|_{\kappa_R = n/2} \;=\; \tfrac14\big(\ln n + \gamma\big) + O(n^{-1/2}).$$

*Derivation.* $\alpha\Phi(0)$ depends only on $(\kappa_R, n)$; take $\alpha = \sigma_w = 1$. From the concavity identity, $\alpha\Phi(0) = \int_0^{\kappa_R} I_n(u)\,du$ with $I_n(u) = \int_0^1 t^{n-1}e^{u(1-t^2)}\,dt$. Put $t = e^{-y}$: $I_n(u) = \int_0^\infty \exp\big(-ny + u(1 - e^{-2y})\big)\,dy$, and $1 - e^{-2y} = 2y - 2y^2 + O(y^3)$, so the exponent is $-\Delta y - 2uy^2 + O(uy^3)$ with $\Delta = n - 2u \in [0, n]$. Where $\Delta \gg \sqrt n$ the integral is $1/\Delta$ to relative $O(1/n)$ whatever the quadratic coefficient. Where $\Delta \lesssim \sqrt n$ the relevant $y$ is $O(n^{-1/2})$, $u = n/2 + O(\sqrt n)$, and the cubic term is $O(n^{-1/2})$. In both regions, to relative $O(n^{-1/2})$, $I_n(u) = n^{-1/2}F(\Delta/\sqrt n)$ with $F(a) = \int_0^\infty e^{-az - z^2}\,dz = \tfrac{\sqrt\pi}{2}e^{a^2/4}\operatorname{erfc}(a/2)$. With $du = -\tfrac{\sqrt n}{2}\,da$ and then $a = 2x$,

$$\alpha\Phi(0) \approx \tfrac12\int_0^{\sqrt n}F(a)\,da = \tfrac12\int_0^{\sqrt n/2} h(x)\,dx, \qquad h(x) = \sqrt\pi\,e^{x^2}\operatorname{erfc}(x) = 2\int_0^\infty e^{-t^2 - 2xt}\,dt.$$

Integrating in $x$ first, $\int_0^X h = \int_0^\infty e^{-t^2}(1 - e^{-2Xt})\,dt/t$. Split it as $\int_0^\infty (e^{-t^2} - e^{-t})\,dt/t + \int_0^\infty (e^{-t} - e^{-2Xt})\,dt/t - \int_0^\infty e^{-2Xt}(1 - e^{-t^2})\,dt/t$. The first is $\gamma/2$, the second is $\ln(2X)$ (Frullani), and the third is $O(X^{-2})$. So $\int_0^X h = \ln X + \ln 2 + \gamma/2 + O(X^{-2})$, and at $X = \sqrt n/2$, $\alpha\Phi(0) = \tfrac12(\tfrac12\ln n + \gamma/2) + O(n^{-1/2}) = \tfrac14(\ln n + \gamma) + O(n^{-1/2})$. The error control in the two-region replacement is a sketch, not a proof. The leading term is derived; the order of the remainder is supported by the numbers below rather than proved.

*Numbers.* $\int_0^X h - \ln X$ at $X = 10^4$, with the $1/(4X^2)$ tail added, equals $\ln 2 + \gamma/2$ to 18 digits. Direct quadrature of $\alpha\Phi(0)$, compared with $\tfrac14(\ln n + \gamma)$, leaves a residual of $0.0570, 0.0185, 0.00589, 0.00187$ at $n = 10^2, 10^3, 10^4, 10^5$. Residual times $\sqrt n$ is $0.570, 0.584, 0.589, 0.590$, so the next term is about $0.59/\sqrt n$; whether that coefficient is $\sqrt\pi/3 = 0.5908$ I have not checked. Canon's "$+0.15$" is $\gamma/4$ plus a finite-$n$ correction. "About one correction time" at threshold is $\tfrac14\ln(ne^\gamma)$ correction times: $0.6$ at $n = 1$, $1.9$ at $n = 1000$, $3.6$ at $n = 10^6$.

Tier for the integrator to decide: leading term derived (exact under the two-region replacement, whose $O(n^{-1/2})$ error is sketched); the $n^{-1/2}$ coefficient is numerical.

## Wording and minor

- **W1. Killed moment read as conditional scale.** "This is the scale of the mismatch while still certified" (A.1S(i)), "its RMS scale while certified is $R^\ast_S$" (`#result-persistence-condition` :17), "(the scale of $\xi$ while it is still inside $\mathcal B_R$)" (`#result-sector-persistence-template`). Bound (i) is on $\mathbb E[\lVert\delta_t\rVert^2;\ \tau_R \gt t]$, not $\mathbb E[\lVert\delta_t\rVert^2 \mid \tau_R \gt t]$, and dividing by $P(\tau_R \gt t)$ does not give a usable bound. For the linear corrector the quasi-stationary law looks more concentrated than the stationary one, and the integrator's Monte Carlo agrees (conditional $\approx 0.25$–$0.29$ against $0.5$). For a general sector corrector I do not know a proof. Either say "counted while inside" or derive the conditional statement.
- **W2.** A.1S(iii) says "no fixed-time tail for the unstopped process follows" under a local sector condition, and the next display is one (the composed form bounds $P(\lVert\delta(t)\rVert \gt r)$ for the unstopped process). It means no tail of Markov-on-the-unstopped-moment form.
- **W3.** Lemma A.1S-τ.0: "below the mean-square threshold … the asymptotic over-estimates by orders of magnitude at large $n$". At $(n, \kappa_R) = (100, 40)$ it under-estimates (asymptotic/exact $= 0.75$). At $(100, 25)$ it over-estimates $8\,100$-fold and at $(20, 5)$ $8.4$-fold. The over-estimate is far-below-threshold behaviour.
- **W4.** `#example-kalman` invokes Prop A.1S-τ and the Kalman-gain cap for a discrete-time filter, outside the proposition's stated scope (continuous time; DA2' not covered). The conclusions are plausible: the small-noise exponent is $R^2/(2\,\mathrm{Var}_{ss})$ for a stationary Gaussian AR(1) as well, and $\mathrm{Var}_{ss}$ is minimized at the Kalman gain. The structural-adaptation trigger uses the continuous window's feasibility condition, and its discrete analog ($R^2$ against the prior error $P^-$) holds by a factor of 100, so the conclusion is safe. Neither step is covered as written.
- **W5.** `01-aat-core/OUTLINE.md` figure caption: "for a corrector whose correction is exactly as strong as its sector floor … failure follows". Lemma A.1N forces escape for the tight corrector under the worst-case outward disturbance, not under every disturbance of size $\rho$, and snowfall is not adversarial.
- **W6.** `#result-persistence-condition` :85 "For linear correction (Kalman, Beta-Bernoulli), $\alpha = \mathcal T$ exactly" against :95 "a gain past the optimum … moves the correction rate $\alpha$, not $\mathcal T$". The identity holds at the optimal gain.
- **W7.** `#der-deliberation-cost`: the threshold gain $\lVert\bar\delta\rVert^2/(\lVert\bar\delta\rVert^2 + \sigma_\varepsilon^2)$ uses the realized error, so it is the uncertainty-ratio gain only in expectation ($U_M = \mathbb E\lVert\bar\delta\rVert^2$).
- **W8.** `#def-mismatch-signal`: "the Kalman error $P$ is that floor". Term (ii) in the discrete setting is the predictive $HP^-H^T$, not the posterior $P$. Also, "never to zero" is absolute where the floor can vanish in the edge cases `#result-mismatch-decomposition` names.
- **W9.** `#result-persistence-condition`'s Findings Brief ("persists when its correction speed beats the rate … Below this threshold the system … loses bounded behavior") contradicts both the window (faster correction past $\alpha_+$ fails) and Lemma A.1N (certificate, not behaviour). INTRODUCTION headline 1 has the same "loses bounded behavior"; the integrator assigned that to A.2.

## Dispositions in vsect

Confirmed answered by the current text (each re-read against the finding): `review:c1-exit-time-verify-1#C1/finding`; `review:part-i-mismatch-lineage-check-1` F1, F2, F4–F14, C2/finding, C5/finding. Left open: C11/finding and F3 (P3 above). The lapsed checks of the integration and lineage records are not re-bound. My own checks bind to the current versions instead. Answered: `question:the-front-door-sentences-say-gain-buys-time-only` (D1).

## What I did not check

The adversarial regime map under $\sigma_w(\alpha)$, anisotropic noise, and discrete time (all named as not landed). The elementary bound's ratio numerics (I checked the derivation only). The numbers in `#obs-gated-tempo-advantage`. Kersting, Grebenkov and Day at the primary. Any segment outside the landing's diff except `#detail-operationalization` and `#result-contraction-template`'s CT2 proof sketch. The latter integrates (CT2) along a ray with a state-dependent $M$ and looked loose to me, but I did not work it through. A sweep for other un-drained readings of $\rho$ or $\sigma_w$ as environmental beyond the grep for $\sigma_w$ in Part I.

## Scripts

Run with `python3 -I`; numpy, scipy and mpmath. Output reproduced above.

```python
# phi: alpha*Phi(0) from the s = r^2 form; threshold table; exact/asymptotic ratios
from mpmath import mp, mpf, quad, exp, gamma, log, euler, sqrt, expm1, erfc, pi
mp.dps = 25
def inner(u, n): return quad(lambda t: t**(n-1)*exp(u*(1-t*t)), [0, 1])
def aPhi0(k, n): return quad(lambda u: inner(u, n), [0, mpf(k)/2, k])
def asym(k, n): return gamma(mpf(n)/2)/2*mpf(k)**(-mpf(n)/2)*exp(k)
for n in [1,2,3,5,10,20,50,100,1000]: print(n, aPhi0(mpf(n)/2, n))
print([(n,k,aPhi0(k,n)/asym(k,n)) for n,k in [(2,4),(2,16),(100,40),(100,25),(20,5)]])
# large n: the constant and the residual
h = lambda x: sqrt(pi)*exp(x*x)*erfc(x)
X = mpf(10)**4; print(quad(h,[0,1,X]) - log(X) - 1/(4*X*X), log(2) + euler/2)
def I(u, n):
    s = 1/sqrt(n); return quad(lambda y: exp(-n*y + u*(-expm1(-2*y))), [0, s/10, s, 5*s, 30*s, 1, mp.inf])
for n in [100, 1000, 10000, 100000]:
    k = mpf(n)/2; v = quad(lambda u: I(u, n), [0, k/2, k-3*sqrt(n), k-sqrt(n), k])
    print(n, v, (v - (log(n)+euler)/4)*sqrt(n))
```

```python
# cap: maximizer of Phi(0) over the gain; cost of doubling the stay
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar, brentq
def inner(u, n): return quad(lambda t: t**(n-1)*np.exp(u*(1-t*t)), 0, 1, limit=200)[0]
def aPhi0(k, n): return quad(lambda u: inner(u, n), 0, k, limit=200)[0]
se, sn = 1.0, 0.5; K = se/sn
for n in [1, 3]:
    for R in [1.0, 1.5, 2.0, 3.0]:
        f = lambda a: -aPhi0(a*R*R/(se**2 + a*a*sn**2), n)/a
        r = minimize_scalar(f, bounds=(1e-3*K, 1.5*K), method='bounded', options={'xatol': 1e-6})
        print(n, R, r.x/K, -r.fun, aPhi0(R*R/(2*se*sn), n)/K)
for n, ks in [(3, [2.5, 6, 12]), (100, [52, 60, 80, 120])]:
    for k in ks:
        t = 2*aPhi0(k, n); print(n, k, brentq(lambda x: aPhi0(x, n) - t, k, k+20) - k)
```

The non-exit table's exact values come from a symmetric finite-difference generator on $[-R, R]$ (1200 interior points, conservative form with weight $e^{-\alpha x^2/\sigma^2}$, Dirichlet ends), survival from the centre by eigen-expansion, cross-checked against $1 - e^{-T/\Phi(0)}$.
