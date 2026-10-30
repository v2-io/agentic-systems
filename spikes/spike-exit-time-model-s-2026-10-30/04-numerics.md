*KR **C.2** / item C1. Top intent, Joseph: "Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself."*

# Numerical checks — what they corroborate, what they corrected, and what they cannot show

Scripts: `checks.py` (sections 1–7; its first run stalled at §4d and was killed — see below; output of the completed sections in `checks-output-partial.txt`), `checks2.py` (follow-ups A–C, `checks2-output.txt`), `checks-cont.py` (§4d onward with a milder dip drift, `checks-cont-output.txt`). numpy 2.4.1, scipy 1.17.1, seeds 20261030 / 20261031. Euler–Maruyama with discrete monitoring of $\lVert\delta\rVert \gt R$; $\sigma_w = R = 1$ throughout so $\kappa = \alpha$.

Every number below is corroboration of something derived in `03-derivation.md`, or the record of a prediction that was wrong. None is the basis of a claim.

## 1. Lemma 1 (OU benchmark) — closed form checked three ways

- **$n = 1$**: $\Phi(0)$ agrees with the explorer's scale-function quadrature to all printed digits at $\kappa = 0.5, 1, 2, 3, 4, 6, 8$ ($1.1915, 1.4452, 2.2508, 3.7873, 6.8582, 26.98, 126.02$). The incomplete-gamma form of Lemma 1 and the explorer's double integral are the same function.
- **$n = 2, 3, 5$**: $\Phi(0)$ against Monte Carlo at $dt = 10^{-4}$, 2000 paths — e.g. $n=2,\kappa=2$: $0.9210$ vs $0.951 \pm 0.017$; $n=3,\kappa=3$: $0.7440$ vs $0.758 \pm 0.014$; $n=5,\kappa=2.5$: $0.3107$ vs $0.314 \pm 0.005$. The MC sits $1$–$4\%$ above the formula everywhere. `checks2.py` §A shows this is discrete-monitoring bias, not a formula error: at $n=2,\kappa=2$ the MC mean is $0.977, 0.950, 0.941$ for $dt = 10^{-3}, 10^{-4}, 2\cdot10^{-5}$, converging toward $0.921$, and the Broadie–Glasserman–Kou correction (exit from the ball of radius $R + 0.5826\,\sigma_w\sqrt{dt}$) reproduces the MC values to within one standard error ($0.982, 0.940, 0.929$). (The BGK constant is from memory of the barrier-option literature; it is used only to explain the bias, not in any derivation.)
- **Lemma 1′**: $\Phi(0)/\Phi_{\text{asym}}(0) \to 1$ from above: $n=2$: $1.29, 1.18, 1.10, 1.07$ at $\kappa = 4, 8, 12, 16$; $n=5$: $1.73, 1.31, 1.15, 1.10$ at $\kappa = 6, 12, 20, 30$. The $O(\kappa^{-1})$ relative error is visible and of the predicted sign and size (at $n=2$, $\kappa=16$: $7\%$; $1/\kappa = 6\%$). Below $\kappa \approx 2$ the asymptotic is wrong by factors, as the explorer also found in $n=1$; it is a large-$\kappa$ statement.

## 2. Corollary 4 — the mean-square threshold is one correction time

$\alpha\,\Phi(0)$ at $\kappa = n/2$ (i.e. $R = R^\ast_S$):

| $n$ | 1 | 2 | 3 | 5 | 10 | 20 | 50 |
|---|---|---|---|---|---|---|---|
| $\alpha\,\mathbb{E}_0[\tau_R]$ | 0.596 | 0.659 | 0.706 | 0.777 | 0.889 | 1.016 | 1.202 |

Order one in every dimension tested, slowly increasing in $n$. **Prediction corrected:** I wrote, before running this, that the values would decrease with $n$ (reasoning from the stationary radial law concentrating on the sphere $r = R^\ast_S$). They increase. The derivation file now states the computed fact and withdraws the mechanism; no claim is made about $n \to \infty$. The qualitative point Corollary 4 rests on — that at the mean-square threshold the benchmark leaves the certified region within about one correction time constant — survives in every dimension computed. Margin buys tenure fast: at $n=3$, $\alpha\Phi(0)$ goes $0.71, 1.57, 3.12, 12.0, 51.2$ as $\kappa$ goes from $n/2$ to $n/2 + 1, 2, 4, 6$.

## 3. Theorem 1 — adversarial instances, $n=2$, floor $\alpha = 2$ ($\kappa = 2$, $\Phi_2(0) = 0.921$)

Predictions were written in `03-derivation.md` §9 before the runs.

| instance | predicted | MC $\mathbb{E}\tau$ ($\pm$ s.e.) | ratio to $\Phi_2(0)$ |
|---|---|---|---|
| OU($2$) reference | $= \Phi_2(0)$ up to monitoring bias | $0.970 \pm 0.015$ | 1.05 |
| (a) radially tight tangential field, $\omega = 6 + 20\sin(5r^2)$ | $=$ OU | $0.895 \pm 0.014$ (plain EM, $dt=10^{-4}$) | 0.97 |
| (b) $\operatorname{diag}(2, 10)$ | strictly $\gt$, $\lt \Phi_{10}(0) = 124.5$ | $1.984 \pm 0.033$ | 2.16 |
| (c) kinked radial profile (corner at $r = 0.5$) | $\gt$ | $1.769 \pm 0.029$ | 1.92 |
| (d) dip drift, bulk $g = 5$, floor on a thin shell | $\gg$, $\lt \Phi_5(0) = 3.80$ | $3.519 \pm 0.061$ | 3.82 |
| (e) non-normal, sym eig $\{2, 10\}$ + rotation | $\in [\Phi_2(0), \Phi_{10}(0)]$ | $2.611 \pm 0.045$ | 2.84 |

Same set at floor $\alpha = 4$ ($\kappa = 4$, $\Phi_4(0) = 2.208$): OU $2.244 \pm 0.047$; (a) tangential, plain EM, $2.239 \pm 0.047$ — equal to OU within $0.2\%$; (b) $\operatorname{diag}(4,12)$: $5.80 \pm 0.13$, ratio $2.63$, far below $\Phi_{12}(0) = 623$.

**On (a).** The first run showed the tight tangential field $8\%$ *below* the OU reference under the same integrator — the opposite side from every other instance and nominally against the equality clause. The cause is the integrator, not the dynamics: Euler–Maruyama applied to a fast rotation $\omega J\delta$ multiplies $\lVert\delta\rVert$ by $\sqrt{1 + \omega^2 dt^2}$ per step (with $\omega$ up to $26$ and $dt = 10^{-4}$ that is a spurious outward radial drift of order $\omega^2 dt\,r/2 \approx 0.03\,r$, i.e. $\sim1.5\%$ of the sector floor — small, but it accumulates in the direction that shortens exit). `checks2.py` §B re-runs (a) with a splitting scheme that applies the rotation exactly (norm-preserving) and EM to the radial OU part: at $dt = 10^{-4}$, OU $0.931 \pm 0.014$ vs tangential $0.911 \pm 0.014$; at $dt = 2\cdot10^{-5}$, OU $0.906 \pm 0.020$ vs tangential $0.918 \pm 0.019$. Survival curves at $t = 0.25, 0.5, 1, 2$ agree to within $0.01$ at both step sizes. Plain EM at $dt = 2\cdot10^{-5}$ (§C) gives $0.942 \pm 0.020$, i.e. the artifact shrinks with $dt$ as a scheme artifact should. The equality clause holds; the first number was the scheme. This is recorded because it is exactly the kind of near-miss a verifier should know was examined.

**On (b), (c).** Both strictly above the floor benchmark by factors $\approx 2$, as predicted, and far below the ceiling benchmark for (b). (c) has a corner in the radial profile, so it lies outside the $C^1$ comfort zone of a Freidlin–Wentzell treatment while squarely inside hypothesis (S); the comparison bound holds.

**On (d) — a design error, recorded.** The first version of the dip drift used bulk correction $g = 20$. That gives an effective exponent near $20$ and $\mathbb{E}\tau \sim e^{20}/40$; the Monte Carlo could not finish and was killed after the other sections completed. The error was mine (the instance was meant to be "far above the floor benchmark," not "astronomically above"). It was rerun with bulk $g = 5$, floor $2$ on a shell of width $0.03$ at $r = 0.5$ — still an A.1N-shaped instance (the floor is attained only where the dynamics rarely sit).

## 4. Corollary 3 — the lifetime bound, and its comparison with Prop A.1S(iv)

`checks-cont-output.txt` §5, $n = 2$, $\kappa = 2$: $P_0(\tau_R \leq L) \leq L/\Phi_2(0)$ is $0.543$ at $L = 0.5$ and vacuous beyond; MC gives $0.342$ (OU) and $0.163$ ($\operatorname{diag}(2,10)$) at $L = 0.5$ — the bound holds and is loose, as a mean-based bound at small $\kappa$ must be. Canon's (iv) bound $n\sigma_w^2L/R^2 = 2L$ is already vacuous at $L = 0.5$. The comparison bound's content is at larger $\kappa$, where (iv) stays vacuous: at $\kappa = 6$ ($n=2$), $P_0(\tau \leq 1) \leq 1/\Phi_6(0) = 1/6.97 = 0.14$; at $\kappa = 10$, $\leq 1/124.5 = 0.008$. The exponential-vs-linear gap is the whole point.

**Correction (advisor-caught).** I had written that (iv) is the better bound at small $\kappa$. It is not, from the origin, at any $\kappa$: as $\kappa \to 0$ the benchmark is Brownian motion with mean exit time $R^2/(n\sigma_w^2) = 1/n$ here, and $\Phi(0)$ approaches it from above — $n=1$: $1.0033, 1.034, 1.19$ at $\kappa = 0.01, 0.1, 0.5$; $n=2$: $0.5013, 0.513, 0.570$; $n=3$: $0.334, 0.340, 0.370$. So $L/\Phi(0) \leq n\sigma_w^2L/R^2$ always, with equality only in the limit. (iv) earns its place by being closed-form and simple in the start point, not by ever being tighter at the origin.

## 5. Theorem 2 — survival ordering

`checks-cont-output.txt` §6, empirical $P(\tau \gt t)$, $\operatorname{diag}(2,10)$ vs OU($2$): $0.837$ vs $0.658$ ($t=0.5$); $0.639$ vs $0.339$ ($t=1$); $0.364$ vs $0.092$ ($t=2$); $0.115$ vs $0.007$ ($t=4$). Pointwise domination as predicted, by a widening margin. The tangential case in §3 (survival curves agreeing to $0.01$ at four times under the rotation-exact scheme) is the equality instance of the same theorem.

## 6. What the numerics cannot show

- Monte Carlo cannot distinguish $\mathbb{E}\tau_R = \Phi$ from $\mathbb{E}\tau_R = \Phi(1 + 0.01)$ at these path counts; the equality clause is established by the proof (the generator identity $\mathcal L v = -1$ under radial tightness), and the numerics only fail to refute it.
- All instances are two-dimensional with isotropic unit noise and $R = 1$; the theorem is proved for all $n$, but the adversarial set exercises only $n = 2$ (Lemma 1 itself is checked at $n = 1, 2, 3, 5$).
- Discrete monitoring biases every MC mean upward by $O(\sqrt{dt})$; comparisons are therefore made between MC runs at the same $dt$ and the same scheme, or against the BGK-corrected formula, never between a raw MC mean and the raw formula.
- Nothing here tests anisotropic noise, discrete time, state-dependent noise, or heavy tails; those are out of scope in the derivation too.
