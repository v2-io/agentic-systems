*KR **C.2** / item C1 (expected exit time under Model S). Top intent, Joseph: "Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself."*

# Derivation: the exit time from the certified region under Model S is bounded below by an explicit Ornstein–Uhlenbeck benchmark — non-asymptotically, in every dimension, with the Kramers exponent $\alpha R^2/\sigma_w^2$ as a corollary

Every statement below carries its tier in brackets. "Exact" means derived under the stated hypotheses, defeasible if someone finds a mistake. Numerical checks are in `checks.py` / `checks-output.txt` and are corroboration, never the basis.

## 0. Setup and standing hypotheses

Mismatch $\delta(t) \in \mathbb{R}^n$ under Model S, in the convention of `#deriv-sector-condition` Prop A.1S:

$$d\delta = -F(\delta)\,dt + \sigma_w\,dW_t, \qquad \delta(0) = x \in \bar{\mathcal B}_R,$$

with $W$ a standard $n$-dimensional Wiener process and $\sigma_w \gt 0$ the per-coordinate noise amplitude (so the Itô correction on $\tfrac12\lVert\delta\rVert^2$ is $\tfrac n2\sigma_w^2$). Write $\mathcal B_R = \{\lVert\delta\rVert \leq R\}$, $\tau_R = \inf\{t \geq 0 : \lVert\delta(t)\rVert \gt R\}$, and $r(t) = \lVert\delta(t)\rVert$. The tempo argument of $F(\mathcal T,\delta)$ is suppressed; $\mathcal T$ is fixed throughout.

**(A1)** $F(0) = 0$. **(A2')** $\delta^\top F(\delta) \geq \alpha\lVert\delta\rVert^2$ for all $\delta \in \bar{\mathcal B}_R$, some $\alpha \gt 0$. These are canon's hypotheses verbatim (`#form-sector-condition`).

**(S) regularity.** $F$ is measurable and locally bounded on $\bar{\mathcal B}_R$, and the SDE has a weak solution with continuous paths on $[0, \tau_R]$. This is all Itô's formula needs. It holds for every locally Lipschitz $F$ and, by Girsanov, for every bounded measurable $F$ on the ball; it does not require Lipschitz continuity, a gradient structure, or the sector condition outside the ball. (The only place a further fact is used is Theorem 2, which says so.)

The one quantity everything is expressed in:

$$\kappa := \frac{\alpha R^2}{\sigma_w^2} = \frac{n}{2}\Big(\frac{R}{R^\ast_S}\Big)^2, \qquad R^\ast_S = \sigma_w\sqrt{\frac{n}{2\alpha}}\ \text{(the Model S RMS radius, Prop A.1S(ii))}.$$

Canon's mean-square persistence condition $\alpha \gt n\sigma_w^2/(2R^2)$ is exactly $\kappa \gt n/2$.

## 1. The observation that makes the question non-asymptotic

A2' is a statement about one scalar: the radial component of the drift. Writing $\hat\delta = \delta/\lVert\delta\rVert$,

$$\hat\delta^\top F(\delta) \;\geq\; \alpha\,\lVert\delta\rVert \qquad (\delta \neq 0,\ \delta \in \bar{\mathcal B}_R).$$

It says nothing about the tangential component of $F$, and nothing about $F$ beyond $R$. Exit from a ball is also a statement about one scalar, $r(t)$. By Itô, on $\{r \gt 0\}$,

$$dr = \Big(-\hat\delta^\top F(\delta) + \frac{(n-1)\sigma_w^2}{2r}\Big)dt + \sigma_w\,dB_t, \qquad B_t := \int_0^t \hat\delta_s^\top\,dW_s,$$

and $B$ is a standard one-dimensional Brownian motion (Lévy's characterization: $\langle B\rangle_t = t$). So the radial process has the diffusion coefficient of a one-dimensional Brownian motion and a drift that A2' bounds pointwise from above:

$$\text{drift of } r \;\leq\; -\alpha r + \frac{(n-1)\sigma_w^2}{2r} \;=:\; b_\alpha(r).$$

The right-hand side is exactly the radial drift of the isotropic Ornstein–Uhlenbeck process $dY = -\alpha Y\,dt + \sigma_w\,dW$ in $\mathbb{R}^n$. The sector condition is therefore precisely the hypothesis a radial comparison with the OU process needs — no more, no less. Everything below is that comparison, run through the two standard channels (a Dynkin argument on the mean, and a same-noise pathwise argument on the law).

## 2. The benchmark: exit time of the isotropic OU process from a ball

**Lemma 1 (OU benchmark).** *[Exact; classical.]* Let $Y$ be the isotropic OU($\alpha$) process in $\mathbb{R}^n$ with per-coordinate noise $\sigma_w$, and let $\Phi(r) = \Phi_{\alpha,n,\sigma_w,R}(r) := \mathbb{E}_y[\tau_R]$ for $\lVert y\rVert = r \leq R$. Then

$$\Phi(r) = \frac{2}{\sigma_w^2}\int_r^R \frac{G(u)}{m(u)}\,du, \qquad m(u) = u^{\,n-1}e^{-\alpha u^2/\sigma_w^2}, \quad G(u) = \int_0^u m(s)\,ds = \tfrac12\Big(\frac{\sigma_w^2}{\alpha}\Big)^{n/2}\gamma\!\Big(\tfrac n2, \tfrac{\alpha u^2}{\sigma_w^2}\Big),$$

with $\gamma$ the lower incomplete gamma function. $\Phi$ is the unique radial $C^2$ solution of $\mathcal L_{\mathrm{OU}}\Phi = -1$ on $\mathcal B_R$ with $\Phi(R) = 0$, where for radial $\phi$,

$$\mathcal L_{\mathrm{OU}}\phi(r) = \frac{\sigma_w^2}{2}\Big(\phi''(r) + \frac{n-1}{r}\phi'(r)\Big) - \alpha r\,\phi'(r).$$

Moreover $\Phi'(r) = -\frac{2}{\sigma_w^2}\frac{G(r)}{m(r)} \leq 0$ on $(0,R]$, $\Phi'(0) = 0$, $\Phi(0) = \max\Phi$, and $v(y) := \Phi(\lVert y\rVert)$ is real-analytic on a neighborhood of $\bar{\mathcal B}_R$ (it is a power series in $\lVert y\rVert^2$ near $0$, since $G(r)/m(r) = \frac rn\,(1 + O(r^2))$ is $r$ times a series in $r^2$).

*Derivation.* Put $\psi = \phi'$ in $\mathcal L_{\mathrm{OU}}\phi = -1$: $\tfrac{\sigma_w^2}{2}\psi' + \big(\tfrac{\sigma_w^2(n-1)}{2r} - \alpha r\big)\psi = -1$. The integrating factor is $m$: $\tfrac{\sigma_w^2}{2}(m\psi)' = -m$, so $m(r)\psi(r) = -\tfrac{2}{\sigma_w^2}G(r)$ using $m\psi \to 0$ at $0$ ($m(0)=0$ for $n \geq 2$; $\psi(0)=0$ by evenness for $n=1$). Integrate from $r$ to $R$ with $\phi(R)=0$. That $\Phi = \mathbb{E}\tau_R$ is Dynkin's formula plus uniqueness for the Dirichlet problem on a bounded domain with non-degenerate generator (the Dirichlet–Poisson problem: Øksendal, *Stochastic Differential Equations*, ch. 9 — theorem number from memory, 9.3.3, to be verified; Khasminskii 2012 ch. 3), $\tau_R \lt \infty$ a.s. with finite mean being part of the same classical statement. $\square$

For $n = 1$ this is the explorer's scale-function formula (`explorers/part-i.md` §8.2) verbatim.

**Lemma 1′ (small-noise asymptotic, every $n$).** *[Exact; Laplace's method on Lemma 1.]* As $\kappa = \alpha R^2/\sigma_w^2 \to \infty$ with $n$ fixed,

$$\Phi(0) = \frac{\Gamma(n/2)}{2\alpha}\,\kappa^{-n/2}\,e^{\kappa}\,\big(1 + O(\kappa^{-1})\big), \qquad\text{hence}\qquad \sigma_w^2\log\Phi(r) \to \alpha R^2 \quad\text{for every fixed } r \lt R.$$

*Derivation.* $G(u) \to G(\infty) = \tfrac12\Gamma(\tfrac n2)(\sigma_w^2/\alpha)^{n/2}$ up to exponentially small error once $u \gg \sigma_w/\sqrt\alpha$; $\int^R u^{1-n}e^{\alpha u^2/\sigma_w^2}du$ is dominated by its endpoint, $= \tfrac{\sigma_w^2}{2\alpha}R^{-n}e^{\kappa}(1 + O(\kappa^{-1}))$; the region $u \lesssim \sigma_w/\sqrt\alpha$ contributes $O(1/\alpha)$, negligible against $e^\kappa$. Multiply. For $r \lt R$ fixed, $\Phi(0) - \Phi(r) = O(e^{\alpha r^2/\sigma_w^2}) = o(\Phi(0))$. $\square$ For $n=1$: $\tfrac{\sqrt\pi}{2\alpha}\kappa^{-1/2}e^\kappa$, the explorer's Kramers form. The exponent is dimension-free; the dimension enters the prefactor as $\kappa^{-n/2}$. (`checks.py` §(1)–(2) confirm Lemma 1 against the explorer's quadrature and against Euler–Maruyama in $n = 2, 3, 5$, and Lemma 1′'s ratio $\to 1$.)

**Reading of $\kappa$.** The OU process is a Brownian particle in the quadratic well $U(y) = \tfrac12\alpha\lVert y\rVert^2$ at temperature $T = \sigma_w^2/2$ (its stationary law is $\propto e^{-U/T}$). Then $\kappa = U(R)/T$ is the barrier height in units of temperature, and Lemma 1′ is Arrhenius–Kramers: $\mathbb{E}\tau \propto e^{U(R)/T}$. This is an isomorphism, not an analogy — the two systems are the same SDE.

## 3. Theorem 1 — mean exit time: the sector process cannot leave sooner, on average, than the OU benchmark

**Theorem 1 (mean exit-time comparison).** *[Exact under (S), A1, A2'.]* For every $x \in \bar{\mathcal B}_R$,

$$\mathbb{E}_x[\tau_R] \;\geq\; \Phi_{\alpha,n,\sigma_w,R}(\lVert x\rVert).$$

If in addition $F$ carries an upper sector constant on the ball, $\delta^\top F(\delta) \leq \bar\alpha\lVert\delta\rVert^2$ for $\delta \in \bar{\mathcal B}_R$, then also

$$\mathbb{E}_x[\tau_R] \;\leq\; \Phi_{\bar\alpha,n,\sigma_w,R}(\lVert x\rVert) \;\lt\; \infty.$$

Both inequalities are equalities when the sector bound is radially tight, $\delta^\top F(\delta) = \alpha\lVert\delta\rVert^2$ on $\bar{\mathcal B}_R$ — which includes $F = \alpha\delta$ and every $F = \alpha\delta + T(\delta)$ with $T(\delta) \perp \delta$ (any tangential component, linear or not).

*Proof.* Let $v(\delta) = \Phi(\lVert\delta\rVert)$ with $\Phi = \Phi_{\alpha,n,\sigma_w,R}$; $v \in C^2$ on a neighborhood of $\bar{\mathcal B}_R$ by Lemma 1. The generator of the sector dynamics is $\mathcal L v = -F\cdot\nabla v + \tfrac{\sigma_w^2}{2}\Delta v$. For radial $v$, $\nabla v = \Phi'(r)\hat\delta$ and $\Delta v = \Phi''(r) + \tfrac{n-1}{r}\Phi'(r)$, so

$$\mathcal L v(\delta) = -\Phi'(r)\,\hat\delta^\top F(\delta) + \frac{\sigma_w^2}{2}\Big(\Phi'' + \frac{n-1}{r}\Phi'\Big).$$

Since $-\Phi'(r) \geq 0$ (Lemma 1) and $\hat\delta^\top F \geq \alpha r$ (A2'), the first term is $\geq -\Phi'(r)\,\alpha r$, hence

$$\mathcal L v \;\geq\; \mathcal L_{\mathrm{OU}}\Phi \;=\; -1 \qquad\text{on } \bar{\mathcal B}_R\setminus\{0\},$$

and at $\delta = 0$ both sides equal $-1$ by continuity ($F(0)=0$ and $\Phi'(0)=0$). Dynkin's formula on the stopped process, $t \wedge \tau_R$, valid because $v \in C^2$ and the stopped path stays in $\bar{\mathcal B}_R$ where $F$ is bounded:

$$\mathbb{E}_x\big[v(\delta_{t\wedge\tau_R})\big] = v(x) + \mathbb{E}_x\!\int_0^{t\wedge\tau_R}\!\mathcal L v(\delta_s)\,ds \;\geq\; v(x) - \mathbb{E}_x[t\wedge\tau_R].$$

So $\mathbb{E}_x[t \wedge \tau_R] \geq v(x) - \mathbb{E}_x[v(\delta_{t\wedge\tau_R})]$. If $P_x(\tau_R = \infty) \gt 0$ the claim is trivial. Otherwise $v(\delta_{t\wedge\tau_R}) \to v(\delta_{\tau_R}) = \Phi(R) = 0$ a.s. as $t \to \infty$, $v$ is bounded on the ball, so by dominated and monotone convergence $\mathbb{E}_x[\tau_R] \geq v(x) = \Phi(\lVert x\rVert)$.

For the upper bound replace $\Phi$ by $\bar\Phi = \Phi_{\bar\alpha,n,\sigma_w,R}$: now $\hat\delta^\top F \leq \bar\alpha r$ and $-\bar\Phi' \geq 0$ give $\mathcal L\bar v \leq \mathcal L_{\mathrm{OU}(\bar\alpha)}\bar\Phi = -1$, so $\mathbb{E}_x[t\wedge\tau_R] \leq \bar v(x) - \mathbb{E}_x[\bar v(\delta_{t\wedge\tau_R})] \leq \bar v(x)$ since $\bar v \geq 0$; let $t \to \infty$. Finiteness of the right side gives $\tau_R \lt \infty$ a.s. as a by-product (consistent with Cor A.1S.1).

Equality: if $\hat\delta^\top F = \alpha r$ then $\mathcal L v = -1$ exactly, and Dynkin gives $\mathbb{E}_x\tau_R = v(x)$ by the same limit. $\square$

**What the proof used, and did not.** It used the pointwise inequality A2' on the closed ball and Itô's formula for a $C^2$ function along a continuous solution. It did not use: Lipschitz continuity of $F$; that $-F$ is a gradient; the sector condition anywhere outside $\mathcal B_R$; any large-deviations machinery; smallness of $\sigma_w$. The bound is therefore non-asymptotic — it holds at every $\sigma_w$, with the explicit benchmark of Lemma 1 — and the explorer's three owed items for the general-$F$ case (the Freidlin–Wentzell hypotheses as applied, Lipschitz, and the prefactor) do not arise: the prefactor of the lower bound is Lemma 1′'s, $\tfrac{\Gamma(n/2)}{2\alpha}\kappa^{-n/2}$, in every dimension.

**Generalization at no cost (radial profile floor).** *[Exact, same proof.]* If instead of a constant floor one has a radial profile, $\hat\delta^\top F(\delta) \geq g(\lVert\delta\rVert)$ on the ball with $g$ continuous, $g(0) = 0$, then $\mathbb{E}_x[\tau_R] \geq \Phi_g(\lVert x\rVert)$ where $\Phi_g$ is Lemma 1's formula with $m_g(u) = u^{n-1}\exp(-\tfrac{2}{\sigma_w^2}\int_0^u g)$; the proof is identical with $\mathcal L_{\mathrm{OU}}$ replaced by the generator of the radial drift $g$. The constant case is $g(r) = \alpha r$. This is the Model S counterpart of Lemma A.1N's mountain-pass remark: the object the exit time actually tracks is the whole radial profile (in one dimension, exactly $\int_0^R F$ — the barrier $2U(R)/\sigma_w^2$ of the scale function), and $\alpha = \inf_r g(r)/r$ is its worst case.

**Tightness is class-level, exactly as in Lemma A.1N.** *[Exact.]* Over the class $\mathcal F_\alpha$ of correctors satisfying A1, A2' on $\mathcal B_R$ with floor $\alpha$, the lower bound is attained (by $F = \alpha\delta$ and every radially tight member), so it is unimprovable from the floor alone. For a fixed $F$ it can be arbitrarily loose: the dip drift of Lemma A.1N's Remark (floor $\alpha$ attained only on a thin shell, correction much stronger everywhere else) has an exit time governed by its full profile, far above $\Phi_\alpha$ (`checks.py` §(4d)). The same hypothesis — radial tightness $\bar\alpha = \alpha$ — makes the Model D threshold an agent-level iff (A.1N) and the Model S exit time exact (Theorem 1). One condition governs both results. The explorer's observation that the rotation $\alpha I + \omega J$ attains the Freidlin–Wentzell bound is the asymptotic shadow of this: it is radially tight, so its whole exit-time law coincides with OU's (Theorem 2 below), at every noise level.

## 4. Theorem 2 — the whole law: stochastic domination of the exit time

**Theorem 2 (stochastic domination).** *[Exact under (S), A1, A2', and for $n \geq 2$ the fact that $\delta$ does not hit the origin at positive times.]* For every $x \in \bar{\mathcal B}_R$ and every $t \geq 0$,

$$P_x(\tau_R \gt t) \;\geq\; P^{\mathrm{OU}(\alpha)}_{\lVert x\rVert}(\tau_R \gt t),$$

i.e. $\tau_R$ under the sector dynamics stochastically dominates the OU($\alpha$) exit time from the same radius. With an upper sector constant $\bar\alpha$ the reverse domination by OU($\bar\alpha$) holds. In the radially tight case the laws coincide.

*Proof, $n \geq 2$.* On $\{r \gt 0\}$ the radial process satisfies $dr = \beta_t\,dt + \sigma_w\,dB_t$ with $\beta_t = -\hat\delta_t^\top F(\delta_t) + \tfrac{(n-1)\sigma_w^2}{2r_t} \leq b_\alpha(r_t)$ (§1), $B$ a Brownian motion. Non-degenerate diffusions with locally bounded drift do not hit points in dimension $n \geq 2$ (Girsanov on $[0, t\wedge\tau_R]$ reduces it to Brownian motion, for which points are polar), so this holds for all $t \in (0, \tau_R]$ a.s. Let $\varrho$ solve $d\varrho = b_\alpha(\varrho)\,dt + \sigma_w\,dB_t$, $\varrho(0) = \lVert x\rVert$, driven by the *same* $B$ — the radial OU process (a strong solution exists and stays positive for $n \geq 2$, as for Bessel processes; its law is the law of $\lVert Y\rVert$). Then $D := r - \varrho$ has no martingale part: $dD = (\beta_t - b_\alpha(\varrho_t))\,dt$, so $D$ is absolutely continuous with $D(0) = 0$. On any interval where $D \gt 0$: $\dot D = \beta_t - b_\alpha(\varrho_t) \leq b_\alpha(r_t) - b_\alpha(\varrho_t) \leq 0$, because $b_\alpha$ is strictly decreasing ($b_\alpha' = -\alpha - \tfrac{(n-1)\sigma_w^2}{2r^2} \lt 0$) and $r_t \gt \varrho_t$ there. Hence if $D(t_1) \gt 0$ for some $t_1$, with $t_0 = \sup\{t \lt t_1 : D(t) \leq 0\}$, $D$ is non-increasing on $(t_0, t_1]$ and $D(t_0) = 0$, a contradiction. So $r_t \leq \varrho_t$ for all $t \leq \tau_R$, and therefore $\tau_R(\delta) \geq \tau_R(\varrho)$ pathwise; since $\varrho \overset{d}{=} \lVert Y\rVert$, $P(\tau_R(\varrho) \gt t) = P^{\mathrm{OU}}(\tau_R \gt t)$.

*Proof, $n = 1$.* By Tanaka, $r = \lvert\delta\rvert$ satisfies $dr = -\operatorname{sgn}(\delta)F(\delta)\,dt + \sigma_w\,dB_t + dL_t$, with $B = \int\operatorname{sgn}(\delta)\,dW$ a Brownian motion and $L$ the local time at $0$; A2' gives $\operatorname{sgn}(\delta)F(\delta) = \delta F(\delta)/\lvert\delta\rvert \geq \alpha r$. Let $\varrho$ be the OU($\alpha$) process reflected at $0$ driven by the same $B$: $d\varrho = -\alpha\varrho\,dt + \sigma_w\,dB_t + dL^\varrho_t$; its law is that of $\lvert Y\rvert$ for $Y$ the one-dimensional OU, so $\tau_R(\varrho) \overset{d}{=} \tau_{(-R,R)}(Y)$. With $D = r - \varrho$: $dD = (-\operatorname{sgn}(\delta)F(\delta) + \alpha\varrho)\,dt + dL - dL^\varrho$. Where $D \gt 0$ we have $r \gt \varrho \geq 0$, so $dL = 0$ there, $dL^\varrho \geq 0$ only decreases $D$, and the drift is $\leq -\alpha r + \alpha\varrho = -\alpha D \lt 0$. The same first-exceedance argument gives $D \leq 0$. $\square$

The upper-bound and equality clauses follow by the symmetric argument with $\bar\alpha$ (for equality, $\beta_t = b_\alpha(r_t)$ identically, so $r = \varrho$).

**Corollary 2.1 (Laplace-transform order without the polarity fact).** *[Exact under (S), A1, A2' only.]* For every $\lambda \gt 0$, $\mathbb{E}_x[e^{-\lambda\tau_R}] \leq \mathbb{E}^{\mathrm{OU}(\alpha)}_{\lVert x\rVert}[e^{-\lambda\tau_R}]$. *Proof.* Let $\psi_\lambda$ be the radial OU solution of $\mathcal L_{\mathrm{OU}}\psi = \lambda\psi$ on $\mathcal B_R$, $\psi(R) = 1$ — it is $\mathbb{E}^{\mathrm{OU}}_r[e^{-\lambda\tau_R}] \in (0,1]$, and the integrating-factor identity $\tfrac{\sigma_w^2}{2}(m\psi_\lambda')' = \lambda m\psi_\lambda \geq 0$ with $m\psi_\lambda' \to 0$ at $0$ gives $\psi_\lambda' \geq 0$. With $w = \psi_\lambda(\lVert\delta\rVert)$, A2' and $\psi_\lambda' \geq 0$ give $\mathcal L w \leq \lambda w$, so $e^{-\lambda t}w(\delta_{t\wedge\tau_R})$ is a bounded supermartingale; optional stopping at $\tau_R$ (where $w = 1$) gives $\mathbb{E}_x[e^{-\lambda\tau_R}] \leq w(x)$. $\square$ This is weaker than Theorem 2 but needs nothing beyond Theorem 1's hypotheses; it already implies all moment inequalities $\mathbb{E}\tau_R^k \geq \mathbb{E}^{\mathrm{OU}}\tau_R^k$.

## 5. Corollary 3 — finite-lifetime containment, exponentially small in $\kappa$

**Corollary 3 (lifetime containment bound).** *[Exact under (S), A1, A2'.]* For every $x \in \bar{\mathcal B}_R$ and lifetime $L \geq 0$,

$$P_x(\tau_R \leq L) \;\leq\; 1 - \frac{\Phi(\lVert x\rVert) - L}{\Phi(0)}, \qquad\text{in particular}\qquad P_0(\tau_R \leq L) \;\leq\; \frac{L}{\Phi(0)} \;=\; \frac{2\alpha L}{\Gamma(n/2)}\,\kappa^{n/2}e^{-\kappa}\,\big(1 + O(\kappa^{-1})\big).$$

Under Theorem 2's hypotheses the sharper $P_x(\tau_R \leq L) \leq P^{\mathrm{OU}}_{\lVert x\rVert}(\tau_R \leq L)$ holds.

*Proof.* From Theorem 1's Dynkin step at $t = L$: $\mathbb{E}_x[v(\delta_{L\wedge\tau_R})] \geq v(x) - \mathbb{E}_x[L\wedge\tau_R] \geq v(x) - L$. On $\{\tau_R \leq L\}$ the left integrand is $\Phi(R) = 0$; on $\{\tau_R \gt L\}$ it is at most $\max v = \Phi(0)$. So $\Phi(0)\,P_x(\tau_R \gt L) \geq \Phi(\lVert x\rVert) - L$. $\square$

Three things to read off. **(i)** The bound is linear in $L$ and so is vacuous as $L \to \infty$ — exactly as `#deriv-stochastic-non-exit` says it must be; nothing here contradicts the no-go, and the bound's $L$-dependence is the no-go seen at finite horizon. **(ii)** Canon's finite-horizon statement, Prop A.1S(iv), gives $P_0(\sup_{[0,L]}\lVert\delta\rVert \gt R) \leq n\sigma_w^2L/R^2 = n\alpha L/\kappa$ — polynomial in $\kappa$. Corollary 3 is exponential in $\kappa$. The two are the same inequality seen with and without the sector condition's decay term: (iv) drops $-\delta^\top F$; Corollary 3 keeps it through the benchmark. For $\kappa$ above a few, Corollary 3 is the operative finite-horizon containment bound and (iv) should be read as its small-$\kappa$ companion (`checks.py` §(5) tabulates both against Monte Carlo). **(iii)** The bound is not tight in the small-$L$ regime (it is a mean-based bound), but with Theorem 2 the OU exit law itself is the bound, and for the OU process the exit time is asymptotically exponential with mean $\Phi(0)$ in the small-noise limit (Day 1983 — citation to be verified by the literature scan; the explorer's CV $\approx 0.98$ at $\kappa = 4$ is the numerical face of it), so $P^{\mathrm{OU}}_0(\tau_R \leq L) \approx 1 - e^{-L/\Phi(0)}$, and $L/\Phi(0)$ is its first-order expansion.

## 6. Corollary 4 — what the Model S persistence condition certifies, and the tenure-indexed condition it does not state

**Corollary 4 (the mean-square condition certifies scale, not tenure).** *[Exact for the OU benchmark; the sector process can only do better.]* At the mean-square persistence threshold $\kappa = n/2$ (i.e. $R = R^\ast_S$), the OU benchmark's expected exit time is of the order of one correction time constant in every dimension tested: `checks.py` §(3) tabulates $\alpha\Phi(0)$ at $\kappa = n/2$ for $n$ from $1$ to $50$ and finds $0.60, 0.66, 0.71, 0.78, 0.89, 1.02, 1.20$ for $n = 1, 2, 3, 5, 10, 20, 50$ — order one, slowly *increasing* in $n$. (My pre-numerics prediction was that it would decrease; it does not, and the record keeps the correction. No claim about the $n \to \infty$ behavior is made.) So an agent that satisfies $\alpha \gt n\sigma_w^2/(2R^2)$ with no margin typically leaves its certified region within one correction time. The condition guarantees the typical scale of mismatch (Prop A.1S(ii)), as canon already states; what it does not guarantee, and the exit-time theorem now quantifies, is tenure.

**Corollary 5 (tenure-indexed Model S condition).** *[Exact as a sufficient condition.]* Fix a required lifetime $L$ and a tolerated exit probability $\epsilon \in (0,1)$. Under (S), A1, A2',

$$\Phi_{\alpha,n,\sigma_w,R}(0) \;\geq\; \frac{L}{\epsilon} \quad\Longrightarrow\quad P_0(\tau_R \leq L) \leq \epsilon,$$

and by Lemma 1′ the left condition is, to leading order in $\kappa$,

$$\kappa - \frac n2\log\kappa \;\geq\; \log\frac{2\alpha L}{\epsilon\,\Gamma(n/2)}, \qquad \kappa = \frac{\alpha R^2}{\sigma_w^2}.$$

This is the Model S counterpart of the Model D condition $\alpha R \gt \rho$ that `#result-persistence-condition` states — the form in which "stay in the certified region" can be certified under stochastic disturbance at all. Its shape is the content: Model D containment is binary and free beyond its threshold (positive invariance, forever); Model S containment is bought, at a price logarithmic in lifetime over risk. Doubling the required lifetime, or halving the tolerated risk, costs $\log 2$ in $\kappa$. Since $\kappa = \tfrac n2(R/R^\ast_S)^2$, the price is paid in the ratio of certified radius to RMS radius, squared — i.e. in exactly the margin that the mean-square condition only requires to exceed $1$.

A note on the direction of the inequalities, so the integrators do not over-read: Corollary 5 is sufficient, not necessary (a corrector with slack above its floor lasts longer than the benchmark, so the true $\kappa$ it needs is smaller); the asymptotic form has $O(\kappa^{-1})$ relative error in $\Phi$, which is a bounded additive error in the $\kappa$-condition; and $L$ here is a lifetime inside the certified region, not the agent's lifetime (exit from $\mathcal B_R$ is loss of the certificate, not of the agent — §8).

## 7. The explorer's statement, located

The explorer's claim — $\liminf_{\sigma_w\to0}\sigma_w^2\log\mathbb{E}[\tau_R] \geq \alpha R^2$, with equality for linear isotropic $F$ — is Theorem 1 composed with Lemma 1′: $\sigma_w^2\log\mathbb{E}_x\tau_R \geq \sigma_w^2\log\Phi(\lVert x\rVert) \to \alpha R^2$. Where Freidlin–Wentzell applies to $F$ (Lipschitz, $\mathcal B_R$ in the basin, inward drift on the boundary — the last two are supplied by A2', the first is not), its quasi-potential barrier therefore satisfies $\min_{\partial\mathcal B_R}V \geq \alpha R^2$, which is the explorer's comparison-argument conclusion (§8.3) reached from the other side; where FW does not apply, Theorem 1 still holds. So the explorer's result is recovered and its owed items discharged: the FW hypotheses are not needed for the bound (only for identifying the bound's exponent with a quasi-potential), Lipschitz is not needed, and the lower bound's prefactor is explicit. The equality case is also wider than "linear isotropic": it is the radially tight case, which contains all tangential perturbations.

What the explorer's route gives that Theorem 1 does not: for a *specific* non-tight $F$ to which FW applies, the true exponent is the quasi-potential barrier, which lies strictly above $\alpha R^2$ (and below $\bar\alpha R^2$ when a ceiling exists); the explorer's non-normal linear example has barrier $0.486$ against floor $0.4$ and ceiling $1.6$. Theorem 1 bounds; it does not locate the true exponent of a non-tight corrector. That is the honest division of labor: the comparison theorem is sharp over the class, FW is sharp for the instance.

## 8. What this result does not say — the scope lines the integration must keep

1. **Exit from $\mathcal B_R$ is loss of the certificate, not of the agent.** `#sketch-structural-adaptation-genericity` is right that $R$ is the certified radius, not the breakdown radius, and that the OU benchmark is positively recurrent (it leaves and returns). Theorem 1 gives the hand-off into `#result-structural-adaptation-necessity` its timescale — the first-exit hazard is at most of order $1/\Phi(0) \sim \tfrac{2\alpha}{\Gamma(n/2)}\kappa^{n/2}e^{-\kappa}$ — and does nothing to close the $R$-versus-$\mathcal F(\mathcal M)$ gap. Whether what happens at the boundary is a transient excursion or a structural failure is not a question about $\tau_R$.
2. **Isotropic noise.** The radial comparison uses $\Sigma_w = \sigma_w^2 I$. Under anisotropic $\Sigma_w$ the radial generator acquires the term $\tfrac12[\Phi''\,\hat\delta^\top\Sigma_w\hat\delta + \tfrac{\Phi'}{r}(\operatorname{tr}\Sigma_w - \hat\delta^\top\Sigma_w\hat\delta)]$ whose sign is not controlled by a single $\sigma$ because $\Phi''$ changes sign; the explorer's conjecture (an $\alpha$ measured in the $\Sigma_w^{-1}$ metric) is plausible for the exponent (for linear $F = A\delta$ the FW barrier is $R^2/(2\lambda_{\max}\Sigma_\infty)$ with $A\Sigma_\infty + \Sigma_\infty A^\top = \Sigma_w$) and is not derived here. Open.
3. **Discrete time (DA2').** Not attempted; a discrete radial comparison would need the discrete small-noise theory. Open.
4. **State-dependent noise.** Not covered; `#deriv-stochastic-non-exit`'s Working Notes already name noise vanishing at the boundary as a different disturbance model under which pathwise containment can return.
5. **Heavy tails.** Not covered. Under $\alpha$-stable Lévy forcing the first exit is driven by a single large jump and the expected exit time scales polynomially in the noise amplitude, not exponentially (Imkeller & Pavlyukevich 2006 and successors — verified citation pending the literature scan in `02-literature.md`). Heavy-tailed environments are where the exponential reserve of Theorem 1 genuinely does not exist; canon's existing scope line ("neither model handles heavy tails; treat them as structural-adaptation triggers") stands and is now sharper: it is the regime where tenure is *not* bought exponentially.
6. **Mean, not hazard, for a general $F$.** The asymptotically exponential exit law (hazard reading) is established for the OU benchmark under FW/Day; for a general sector $F$ this spike gives stochastic domination by that law (Theorem 2), which is a one-sided statement about survival, not a hazard rate.

## 9. Adversarial instances (constructed before the numerics were read)

For every universally quantified claim above, at least one instance outside the motivating (linear, gradient) family, with the prediction written down first:

- **(a) Pure tangential nonlinearity**, $F = \alpha\delta + \omega(\lVert\delta\rVert^2)J\delta$ in $\mathbb{R}^2$ with $\omega$ large and oscillating. Radially tight. Prediction: $\mathbb{E}\tau_R$ equals the OU value to Monte Carlo accuracy (Theorem 1 equality clause), and the survival curve coincides (Theorem 2).
- **(b) Anisotropic linear** $\operatorname{diag}(\alpha, 5\alpha)$: floor $\alpha$, ceiling $5\alpha$. Prediction: strictly between $\Phi_\alpha(0)$ and $\Phi_{5\alpha}(0)$.
- **(c) Kinked radial profile** $g(r) = \alpha r$ for $r \lt R/2$, steeper beyond, with a corner (not $C^1$, so outside FW's Lipschitz-on-$C^1$ comfort zone but inside (S)). Prediction: above $\Phi_\alpha(0)$; equals $\Phi_g(0)$ of the profile generalization.
- **(d) The Lemma A.1N dip drift**: floor $\alpha$ attained only on a thin shell. Prediction: far above $\Phi_\alpha(0)$ — the bound holds and is very loose, as the class-level tightness remark says it may be.
- **(e) Non-normal with rotation**, symmetric part with eigenvalues $\{\alpha, 5\alpha\}$ plus an antisymmetric part. Prediction: in $[\Phi_\alpha(0), \Phi_{5\alpha}(0)]$.

Results are in `checks-output.txt` and discussed in `04-numerics.md`.
