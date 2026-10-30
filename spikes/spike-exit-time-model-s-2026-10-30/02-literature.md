*KR **C.2** (Objective C: "the theory is correct where it is known wrong, and stronger where strengthening was found"); item C1, expected exit time under Model S. Top intent, Joseph: "Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself." Literature scan requested by the derivation agent; written 2026-10-30.*

# Literature scan: exit times of a diffusion with a one-point (radial) monotone drift, from a ball

Setting in one line: $d\delta = -F(\delta)\,dt + \sigma\,dW_t$ with $\sigma$ per coordinate, $F(0)=0$, $\delta^\top F(\delta) \geq \alpha\lVert\delta\rVert^2$ on $\bar{\mathcal B}_R$, $\tau_R$ the first exit from the ball, $\kappa = \alpha R^2/\sigma^2$. Symbol warning: $\alpha$ is canon's sector constant. The stable index of Lévy noise is written $\beta$ below even where the source writes $\alpha$.

**Verification tags.** [R] I read the statement in the source's own text (PDF text extraction, and page images where the extraction garbled equations). [A] abstract or metadata only. [S] second-hand: described by a paper that cites it; not opened. [M] from memory; nothing checked. Bibliographic data (journal, volume, pages, DOI) for every item were checked against Crossref or arXiv metadata, separately from the content tag; exceptions are noted.

**Method and limits.** Web search, plus downloading arXiv and open-access PDFs and reading them, plus a few numerical checks (section 9). Not searched: MathSciNet, zbMATH, citation graphs. No book was opened. "Not found" below means "not found by this route".

## 1. Verdict

1. **The method is standard and in print; the statement as you intend to state it was not found in print.** The method is the radial (or squared-radial) comparison of a diffusion with an isotropic OU benchmark, through Ikeda–Watanabe-type comparison or through a Dynkin argument. I found no source that states "$\mathbb{E}_x\tau_R \geq \mathbb{E}^{\mathrm{OU}}_{\lVert x\rVert}\tau_R$", or stochastic domination of the whole exit law, as a theorem for a drift that satisfies only a one-point/radial condition, and none that pairs it with the closed-form OU benchmark.

2. **Three sources carry the method, and their hypotheses are what decide how far your result goes beyond them.**
   - Ikeda–Watanabe 1977, Theorem 1.1 with Remark 1.1 (section 3.1). Comparison of two scalar Itô processes up to a stopping time, with the comparison coefficients continuous and the actual drifts arbitrary adapted processes bounded by them. Applied to $\lVert\delta\rVert^2$ this needs no regularity of $F$ (my reading, section 10.1).
   - Altmeyer, arXiv:2208.13296, proof of Theorem 2.12, Step 1 (section 3.4). Uses exactly this step to dominate $\lVert L_t-\theta^\ast\rVert$ by an OU radius for a strongly convex Langevin diffusion. Gradient case; used as a lemma for a tail bound, not stated as an exit-time theorem; arXiv-only as far as I know.
   - Li–Zhang, arXiv:1202.4131 v9, Lemma 2.12 (section 3.5). Same-Brownian radial comparison from the origin for bounded Borel drift, with the polarity-of-the-origin step and a first-exceedance argument, in the opposite direction (domination from below). Unrefereed; nine arXiv versions.

3. **The OU benchmark is a classical closed form in every dimension.** Kersting–Orvieto–Proske–Lucchi 2023 Theorem 4 (their eq. (17)) and Grebenkov 2015 eq. (75) give $\mathbb{E}\tau_R$ for all $n$ and all $\sigma$; Grebenkov eq. (76) gives the large-$\kappa$ asymptotic $\Gamma(n/2)\,e^{\kappa}/(2\alpha\,\kappa^{n/2})$, which is your Lemma 1′. Both checked numerically (section 9).

4. **The Freidlin–Wentzell exponent for non-gradient drift is standard** (Berglund 2013, Theorem 2.2; Aleksian–Villeneuve 2025/26, Proposition 1.5), but under Lipschitz $b,\sigma$, which A2′ does not supply. Your comparison route bypasses the hypothesis; I know of no source that does this.

5. **The asymptotically exponential exit law for non-gradient drift** is Day 1983 (Berglund 2013, Theorem 2.3), under the Freidlin–Wentzell setting (unique stable equilibrium, domain in its basin, nontangential boundary, smooth nondegenerate coefficients). I did not read Day's paper; hypotheses are from Berglund and from Day's 1999 survey. Huisinga–Meyn–Schütte 2004 give an approximately-exponential statement under $V$-uniform ergodicity, non-reversible, no gradient assumption (abstract and introduction read; the quantitative theorem not read). Neither is available for $F$ satisfying A2′ on a ball alone.

6. **Heavy tails.** The citable "polynomial rather than exponential" statement is Imkeller–Pavlyukevich 2006, Theorem 1.1 ([R]; one-dimensional, gradient, small noise), and for finite-dimensional non-gradient drift Högele–Pavlyukevich 2014, Theorem 2.1 / Corollary 2.1 ([R]). Both are small-noise asymptotics for a fixed domain, not non-asymptotic bounds.

7. **2025–2026.** Nothing found that states your result. Items that bear on it: Geng–Markowsky 2025 (the squared-modulus Ikeda–Watanabe trick, and a caution), Li–Zhang v9 (2026), Aleksian–Villeneuve (published 2026), Wang–Rhee (Feb 2026; discrete-time heavy-tailed Freidlin–Wentzell analogue, non-gradient drift allowed).

## 2. Doubts about the framing, and things not to over-read

- **Three claims are bundled and rest on different literatures.** (i) Domination of the exit time by the OU exit time: comparison theory, no small-noise assumption, no regularity beyond what the comparison needs. (ii) The explicit benchmark and its $\kappa\to\infty$ form: classical OU computation. (iii) The identification of the exponent with a Freidlin–Wentzell quasi-potential, and any exponential-law statement: large-deviation theory, which needs Lipschitz drift and more. Canon can state (i) and (ii) without (iii); the text should not let (iii)'s hypotheses leak back.

- **Symbol clash.** In Imkeller–Pavlyukevich $\alpha$ is the stable index and the sector constant has no counterpart; a canon sentence citing them must rename one of the two.

- **Geng–Markowsky's caution is about a different ordering.** Their Remark 1 says exit-time monotonicity is "in general not true if the drift is assumed to be non-constant (a simple comparison relation between the drifts does not have a clear implication on the relation between exit times)". Their counterexample is a drift ordered in the signed coordinate that pushes back toward the centre on one side. A2′ is an ordering of the radial component of the drift, which is what a comparison on $\lVert\delta\rVert^2$ uses. I read the two as compatible; worth one clause in canon so a reader who knows the remark does not think it contradicts the result.

- **$\kappa$ versus $n$.** Kersting et al. Corollary 8 says that as $d\to\infty$ at fixed radius and fixed $\sigma,\theta$, the OU mean exit time is asymptotically that of Brownian motion. Your Corollary 4 scans $\kappa=n/2$. These are different regimes ($\kappa=\alpha R^2/\sigma^2$ fixed in $n$ versus $\kappa$ growing with $n$) and do not conflict; my numbers (section 9) agree with your tabulated values at $\kappa=n/2$.

- **The leading asymptotic (76) is not a bound.** The ratio of exact to leading term is below 1 at small $\kappa$ and above 1 beyond a dimension-dependent crossover (section 9). For a rigorous lower bound use the integral formula, not (76).

- **Kersting et al.'s explicit bounds are weak at large $\kappa$.** Their lower bound (35) carries $\exp(2\kappa/(n+2))$, not $\exp(\kappa)$, so it loses the exponent. For an exponent-$\kappa$ lower bound cite the integral formula (their eq. (17)).

- **A cheap consistency check on the quasi-potential side (mine, section 10.2):** A2′ forces the quasi-potential barrier to satisfy $\min_{\partial\mathcal B_R}V\geq\alpha R^2$ by a three-line deterministic argument, independent of any exit-time theorem. That agrees with what Theorem 1 gives when Freidlin–Wentzell applies.

- **Hajek 1982 is not "the opposite direction"** (differing from a first impression I had): the negative-drift theorem in the drift-analysis literature bounds the time to reach a level when the drift points away from it, which for exit from a restoring region is the right direction. It is discrete time, with uniform drift and a sub-exponential increment condition, and I have not read the original (section 6.4).

## 3. Comparison theorems (the method)

### 3.1 Ikeda–Watanabe 1977 [R]

- **Citation.** N. Ikeda and S. Watanabe, "A comparison theorem for solutions of stochastic differential equations and its applications", Osaka J. Math. 14(3) (1977) 619–633. DOI 10.18910/7664. PDF: https://ir.library.osaka-u.ac.jp/repo/ouka/all/7664/ojm14_03_14.pdf. Read in full; equations checked on page images (pp. 2, 3, 10, 11 of the PDF).

- **Theorem 1.1 (section 1), data.** (i) A real continuous $\sigma(t,x)$ on $[0,\infty)\times\mathbb{R}$ with $\lvert\sigma(t,x)-\sigma(t,y)\rvert\leq\rho(\lvert x-y\rvert)$, $\rho$ increasing on $[0,\infty)$, $\rho(0)=0$, $\int_{0+}\rho(\xi)^{-2}\,d\xi=\infty$ (Yamada's condition; $\rho(\xi)=c\sqrt{\xi}$ qualifies). (ii) Real continuous $b_1(t,x)\lt b_2(t,x)$ on $[0,\infty)\times\mathbb{R}$. (iii) Two real adapted continuous processes $x_1,x_2$ on a filtered space, (iv) a one-dimensional $\mathcal F_t$-Brownian motion $B$, (v) real adapted well-measurable processes $\beta_1,\beta_2$, with $x_i(t)-x_i(0)=\int_0^t\sigma(s,x_i(s))\,dB(s)+\int_0^t\beta_i(s)\,ds$ ($i=1,2$), $x_1(0)\leq x_2(0)$, $\beta_1(t)\leq b_1(t,x_1(t))$, $\beta_2(t)\geq b_2(t,x_2(t))$ for all $t$. **Conclusion:** $x_1(t)\leq x_2(t)$ for all $t\geq0$ a.s. If pathwise uniqueness holds for at least one of $dX=\sigma(t,X)\,dB+b_i(t,X)\,dt$, the same conclusion holds with the strict inequality $b_1\lt b_2$ weakened to $b_1\leq b_2$.

- **Remark 1.1.** If there is a stopping time $S\gt0$ such that $x_i$ is defined on $[0,S)$ and the relations hold there, the conclusion holds on $[0,S)$. This is the "up to the exit time" form.

- **What the hypotheses do and do not ask of the drift.** The actual drifts enter only as the processes $\beta_i$; the single link to the comparison coefficient is the pointwise inequality $\beta_1(t)\leq b_1(t,x_1(t))$. Nothing is assumed about how $\beta_1$ is generated, so no Lipschitz or continuity requirement on $F$ appears. (My reading of the statement; consequences in section 10.1.)

- **Section 3, Theorem 3.1 and Remark 3.1 and Example 3.1.** A comparison theorem for the one-dimensional projection $p(X_t)$ of a multi-dimensional diffusion $dX^i=\sum_k\sigma^i_k(X)\,dB^k+b^i(X)\,dt$ with "sufficiently smooth" coefficients on $\mathbb{R}^n$, where $a(x)=\sum a^{ij}p_ip_j$, $b(x)=(Lp)(x)/a(x)$, and $a^\pm,b^\pm$ are the sup/inf over level sets of $p$, assumed finitely determined and locally Lipschitz on the open interval. Four comparison diffusions with generators $a^\pm(\xi)(\tfrac12\,d^2/d\xi^2+b^\pm(\xi)\,d/d\xi)$; conclusion is an ordering of the running maxima and minima (their (3.13)–(3.15)). Remark 3.1: if $a$ depends only on $p$, the two envelopes of $a$ coincide. Example 3.1 uses $p(x)=\tfrac12\lvert x\rvert^2$ (Hasminskii's explosion test). With $p=\tfrac12\lvert x\rvert^2$ and isotropic constant noise $a=\sigma^2\lvert x\rvert^2$ depends only on $p$; so Theorem 3.1 is literally the radial comparison, in the form of running maxima, which is what exit from a ball needs. **Limitation:** the envelopes $b^\pm$ must be locally Lipschitz, which A2′ (an inequality) does not give; Theorem 1.1 is the one that fits.

- **Relation to your statement.** The comparison lemma underlying Theorem 2 of your derivation is this theorem. I found no statement in the paper of an exit-time corollary; its applications are an optimal-control problem (section 2) and explosion tests (section 3).

- **Yamada 1973** (T. Yamada, "On a comparison theorem for solutions of stochastic differential equations and its applications", J. Math. Kyoto Univ. 13(3) (1973) 497–512, DOI 10.1215/kjm/1250523321) is the predecessor that Theorem 1.1 modifies [S, via Ikeda–Watanabe's introduction]. Not opened.

### 3.2 Geng and Markowsky 2025 [R]

- **Citation.** X. Geng and G. Markowsky, "Stochastic domination of exit times for random walks and Brownian motion with drift", Stochastic Models 42(1) (2025) 51–59. DOI 10.1080/15326349.2025.2515964. arXiv:2408.00277 (v2, 3 Jun 2025): https://arxiv.org/abs/2408.00277.

- **Statement.** Theorem 1(ii): for standard one-dimensional Brownian motion $B$ and $\tau^b_\lambda=\inf\{t: B_t+\lambda t\notin(-b,b)\}$, for each fixed $t\gt0$ the map $\lambda\mapsto P(\tau^b_\lambda\gt t)$ is decreasing on $[0,\infty)$. Two proofs: Girsanov (sections 2–3), and a sketch (section 4) that applies the Ikeda–Watanabe comparison theorem to $Y_t=\lvert B_t+\lambda t\rvert^2$, which satisfies the genuine SDE $dY=2\sqrt{Y}\,dW+(1+2\lambda\sqrt{Y}\tanh(\lambda\sqrt{Y}))\,dt$ whose drift is increasing in $\lambda$. They note that $\lvert B_t+\lambda t\rvert$ itself is not an Itô diffusion (local time at zero) while its square is. Remark 2: the Ikeda–Watanabe conditions are "slightly technical to state but straightforward to verify", not verified in the text. The section 4 argument is labelled a sketch.

- **Remark 1 (verbatim).** "Theorem 1 seems surprisingly resistant to generalisations. The conclusion is in general not true if the drift is assumed to be non-constant (a simple comparison relation between the drifts does not have a clear implication on the relation between exit times). For instance, if the drift is allowed to depend on the position of the path, one could make a large positive drift when the process goes negative which would push it back to the center, resulting in longer stay in the interval. The theorem also fails to hold in general if the drift is assumed to be time-dependent."

- **Relation.** Same technique (Ikeda–Watanabe on the squared modulus to obtain exit-time domination), for a different family (constant drift, symmetric interval, $n=1$). Section 4 is an in-print precedent for using the squared radius to avoid the local-time term that your $n=1$ proof handles with Tanaka and a reflected OU. See section 2 for how Remark 1 relates to A2′.

### 3.3 Ouyang, arXiv:1310.3996 [R, section 4]

- **Citation.** S. Ouyang, "Volume growth, comparison theorem and escape rate of diffusion process", arXiv:1310.3996 v1 (Oct 2013), https://arxiv.org/abs/1310.3996. I found no journal reference for this version; a related paper with a different title, Ouyang, "Volume growth and escape rate of symmetric diffusion processes", Stochastics 88(3) (2015) 353–372, DOI 10.1080/17442508.2015.1072532, exists (relation unverified, not opened).

- **Theorem 4.1.** Setting: $M$ a complete smooth connected Riemannian manifold, $L=\Delta+Z$ with $Z$ a $C^1$ vector field, $o\in M$, $\rho_o=d(\cdot,o)$. Assume some measurable $\theta$ on $[0,\infty)$ with $L\rho_o\leq\theta(\rho_o)$ on $M\setminus\mathrm{cut}(o)$. Let $x_t$ solve $dx_t=\theta(x_t)\,dt+\sqrt2\,dw_t$, $x_0=r=\rho_o(x)\lt R$. Then for all $t\gt0$ and $0\lt\delta\lt R$: $P^0_r(x_t\lt\delta,\ t\lt\tau^0_R)\leq P_x(\rho_o(X_t)\lt\delta,\ t\lt\tau_R)$. Proof by the parabolic maximum principle (not pathwise). The text says "for every $0\lt R\lt\delta_K$" when defining $\tau^0_R$; I could not tell where $\delta_K$ is defined, so I do not know whether it restricts $R$.

- **Relation.** On $\mathbb{R}^n$ with $Z=-F$, $C^1$, noise normalized to $\sigma^2=2$: $L\rho=(n-1)/\rho-F\cdot x/\rho\leq(n-1)/\rho-\alpha\rho=:\theta(\rho)$, the radial OU drift. Letting $\delta\uparrow R$ in (4.4) gives $P(t\lt\tau^0_R)\leq P(t\lt\tau_R)$, i.e. the same domination of the exit time (my reading; the paper states it for escape rates). Needs $F\in C^1$, more than A2′, and a global field on $M$; the inequality (4.2) must hold on all of $M\setminus\mathrm{cut}(o)$, so $F$ would have to be extended outside the ball with the sector inequality. It is a PDE proof of the same domination under stronger regularity, and gives distributional (not pathwise) comparison.

- **Lineage cited by Ouyang** [S]: Ichihara, J. Multivariate Anal. 24(2) (1988) 177–188, DOI 10.1016/0047-259X(88)90034-6 (his Theorem 2.1 and Lemma 2.1); Debiard–Gaveau–Mazet, Publ. RIMS Kyoto 12(2) (1976) 391–425, DOI 10.2977/prims/1195190722 (cited by Ikeda–Watanabe as the Riemannian comparison background). Neither opened.

### 3.4 Altmeyer, arXiv:2208.13296 [R, one proof step]

- **Citation.** R. Altmeyer, "Polynomial time guarantees for sampling based posterior inference in high-dimensional generalised linear models", arXiv:2208.13296 v3 (23 Jul 2025), https://arxiv.org/abs/2208.13296. Publication status unknown to me.

- **What the proof does.** Theorem 2.12 bounds the exit probability of a discrete Langevin chain from a region of local curvature by relating it to a continuous Langevin diffusion $dL_t=-\nabla f(L_t)\,dt+\sqrt2\,dW_t$ with $f$ strongly convex and $\nabla f$ Lipschitz on the region. Step 1: Itô for $\lVert L_t-\theta^\ast\rVert$ (non-hitting of the point for $p\geq2$ by Girsanov); strong convexity gives $(\theta-\theta^\ast)\cdot\nabla f(\theta)\geq(m/2)(\theta-\theta^\ast)\cdot(\theta-\bar\theta)$ with $\bar\theta=\theta^\ast+(2/m)\nabla f(\theta^\ast)$; then "By a comparison argument for scalar Itô processes [31] we get $\lVert L_t-\theta^\ast\rVert\leq\lVert V_t-\theta^\ast\rVert$ $P$-almost surely for all $t\geq0$" (their (2.16)), where $V$ is the OU process $dV=-(m/2)(V-\bar\theta)\,dt+\sqrt2\,d\tilde W$ driven by the same scalar Brownian motion, and [31] is Ikeda–Watanabe 1977. The tail $P(\sup_{t\leq T}\lVert L_t-\theta^\ast\rVert\gt3\eta/16)$ is then bounded through the scalar Brownian maximum.

- **Relation.** The closest in-print instance I found of your step: a one-point (strong-monotonicity) condition, radial Itô, same-noise domination by an OU radius, citing Ikeda–Watanabe. Differences: gradient drift; used only as a lemma for a probability bound (no expectation or law of $\tau_R$, no closed form); arXiv-only for all I know. I did not audit the step when the OU is centred at $\bar\theta\neq\theta^\ast$ (the radial drift of $V$ about $\theta^\ast$ then depends on direction as well as radius, so a scalar comparison is not immediate); when $\bar\theta=\theta^\ast$ it is exactly the pattern. Cite as precedent, not as a proof.

### 3.5 Li and Zhang, arXiv:1202.4131 v9 [R, Lemma 2.12 and its proof]

- **Citation.** C. Li and L. Zhang, "Selection in the Zero-Noise Limit for High-Dimensional Diffusions with Measurable Drift", arXiv:1202.4131 (v9 dated 24 Sep 2026; I read v9), https://arxiv.org/abs/1202.4131. Unrefereed as far as I know; nine versions, so statements may move.

- **Statement.** For $d\geq2$, bounded Borel drift $b$, $dX^\varepsilon=b(X^\varepsilon)\,dt+\varepsilon\,dW$, $X_0=0$: Theorem 2.11 (the process does not return to the origin at positive times: Girsanov on $[0,T]$ via Novikov, then polarity of points in $d\geq2$). Lemma 2.12: with $\varphi(r)$ the worst-case lower bound of the radial component $\langle b(x),x/\lvert x\rvert\rangle$ on the sphere of radius $r$ (Assumption (A1): positive, continuous at positive radii), $B_t=\int_0^t\langle\theta_s,dW_s\rangle$ (a Brownian motion), $dr_t=\varphi(r_t)\,dt+\varepsilon\,dB_t$, $r_0=0$, one has $P\{R^\varepsilon_t\geq r_t\ \forall t\geq0\}=1$ for $R^\varepsilon=\lvert X^\varepsilon\rvert$. The proof writes $dR=(v+c/R)\,dt+\varepsilon\,dB$, $c=\varepsilon^2(d-1)/2$, $v=\langle b,\theta\rangle\geq\varphi(R)$, sets $D=R-r$, which is absolutely continuous, and runs a first-entrance argument into $\{D\lt0\}$. Remark 2.13 says the comparison "uses the radial lower bound, its continuity at positive radii, and the positive geometric drift. Point polarity does not by itself prove that ordering."

- **Relation.** The proof architecture is that of your Theorem 2 for $n\geq2$ (same Brownian motion, no martingale part in the difference, first exceedance, polarity from Girsanov), in the opposite direction (domination from below) and for bounded Borel drift. It is evidence that the argument is routine and sound in this generality, not a source for your direction. The condition there is on the inf of the radial component; yours is on the sup, and the continuity requirement of their (A1) has no counterpart in your argument as written (you use monotonicity of $b_\alpha$ instead); worth confirming that you do not need it.

### 3.6 Set aside

- **Huang, Kim, Mao**, "Variational principles for the exit time of non-symmetric diffusions", arXiv:2006.16446 v2 (Jan 2024) [R, statements]: comparison of exit times for $L_\gamma=\nabla\cdot a\nabla+\gamma\,b\cdot\nabla$ across $\gamma$, under $\operatorname{div}b=0$ (their Assumption A3) and $C^{1,\alpha}$ coefficients; conclusions are for $\int_D\mathbb{E}_x\tau\,dx$ (integrated over the domain), non-increasing in $\gamma\geq0$. Not applicable: wrong structure (divergence-free perturbation of a symmetric diffusion) and an integrated, not pointwise, statement.

- **Hamana 2020**, "The probability distributions of the first hitting times of radial Ornstein–Uhlenbeck processes", Studia Math. 251 (2020) 65–88, DOI 10.4064/sm180410-27-12 [A]: hitting times of a target closer to the origin than the start. Not exit times; not relevant.

## 4. The OU benchmark: mean exit time from a ball, closed form

### 4.1 Kersting, Orvieto, Proske, Lucchi 2023 [R]

- **Citation.** H. Kersting, A. Orvieto, F. Proske, A. Lucchi, "Mean first exit times of Ornstein–Uhlenbeck processes in high-dimensional spaces", J. Phys. A: Math. Theor. 56 (2023) 215003. DOI 10.1088/1751-8121/acc559. arXiv:2208.04029 (v2, 17 Jan 2023): https://arxiv.org/abs/2208.04029.

- **Theorem 4 (their eq. (17)).** For $dX=-\theta X\,dt+\sigma\,dB$ in $\mathbb{R}^d$, $\lambda=\theta/\sigma^2\in\mathbb{R}$, $\tau_L=\inf\{t\geq0:\lVert X_t\rVert=L\}$ and $\lVert X_0\rVert=x\in[0,L]$, for all $\sigma\gt0$ and all $\lambda$:

$$\mathbb{E}^x\tau_L=\frac{2}{\sigma^2}\int_x^L z^{1-d}e^{\lambda z^2}\Big(\int_0^z t^{d-1}e^{-\lambda t^2}\,dt\Big)\,dz,$$

and for $\lambda\gt0$ (eq. (18)) $\mathbb{E}^x\tau_L=\dfrac{1}{\lambda^{d/2}\sigma^2}\displaystyle\int_x^L z^{1-d}e^{\lambda z^2}\,\gamma(d/2,\lambda z^2)\,dz$ (the factor follows from $\int_0^z t^{d-1}e^{-\lambda t^2}dt=\tfrac12\lambda^{-d/2}\gamma(d/2,\lambda z^2)$; the extracted text of their (18) is ambiguous about it, so this is my reading, consistent with (17)). Here $\gamma$ is the lower incomplete gamma function (the paper calls it "upper"; the displayed integral $\int_0^y t^{n-1}e^{-t}\,dt$ is the lower one). With $\theta=\alpha$, $d=n$, $L=R$ this is your Lemma 1 term for term. Proof route: the radial SDE (their eq. (5), $d\rho=((d-1)\sigma^2/(2\rho)-\theta\rho)\,dt+\sigma\,dB$), the Andronov–Vitt–Pontryagin boundary value problem (their Theorem 2 and Corollary 3, citing Schuss 2010, Theorem 4.4.3 and Corollary 4.4.1), uniqueness by Picard–Lindelöf, the case $x=0$ by the strong Markov property and a limit.

- **Other results there.** Theorem 7 (explicit upper and lower bounds), Corollary 8 ($d\to\infty$: $\mathbb{E}^x\tau_L\sim(L^2-x^2)/(\sigma^2 d)$ for every $\theta\geq0$, the Brownian value). I verified Theorem 7's four inequalities numerically at $x=0$ over 30 pairs $(n,\kappa)$, no violation (section 9). The lower bound (35) behaves like $e^{2\kappa/(n+2)}$, which loses the exponent.

- **Relation.** Cite this for the benchmark in every dimension and every noise level (it is the one source with general $\sigma$ and general $d$ in a single proof). Remark 5 there says the formula is "already partially known": Grebenkov 2014/2015 eq. (75) and Graczyk–Jakubowski 2008 Theorem 2.2; the incomplete-gamma form (18) is claimed as new there.

### 4.2 Grebenkov 2015 [R, sections 2.8 and eqs. (75)–(77)]

- **Citation.** D. S. Grebenkov, "First exit times of harmonically trapped particles: a didactic review", J. Phys. A: Math. Theor. 48 (2015) 013001. DOI 10.1088/1751-8113/48/1/013001. arXiv:1411.3598 (I read v2, 22 Jun 2025): https://arxiv.org/abs/1411.3598. A Corrigendum exists (J. Phys. A 58 (2025) 289501, DOI 10.1088/1751-8121/adebc8); I did not open it, and my numerical checks of (75) and (76) are consistent with the text as printed in v2.

- **Statements.** Eq. (75), mean exit time of the multi-dimensional OU from a ball of radius $L$ (Dirichlet at $r_0=L$, regular at $0$): $\langle\tau\rangle_{r_0}=\frac{L^2}{D\kappa}\int_{\sqrt{\kappa}r_0/L}^{\sqrt\kappa}dr_1\,r_1^{1-d}e^{r_1^2}\int_0^{r_1}dr_2\,r_2^{d-1}e^{-r_2^2}$ (the prefactor as I read the extracted text; it matches Kersting et al. after the substitution $z=Lr_1/\sqrt\kappa$ and my numerics). Limit $\kappa\to0$: $(L^2-r_0^2)/(2dD)$. Eq. (76), $\kappa\gg1$, any $r_0$ not too close to $L$: $\langle\tau\rangle\simeq\dfrac{L^2\,\Gamma(d/2)\,e^{\kappa}}{D\,4\kappa^{1+d/2}}$. Eq. (77): $\lambda_0\simeq\frac{D}{L^2}\frac{4\kappa^{1+d/2}}{\Gamma(d/2)}e^{-\kappa}$, the inverse; the other eigenvalues grow linearly in $\kappa$ (eq. (78)), so "the first exit time follows approximately an exponential law $P\{\tau\gt t\}\simeq\exp(-t/\langle\tau\rangle)$". The parameter is $\kappa=kL^2/(2k_BT)$ with $D=k_BT/\gamma$ (diffusion coefficient with $\langle x^2\rangle=2Dt$); for $dX=-\alpha X\,dt+\sigma\,dW$ this is $D=\sigma^2/2$, $k/\gamma=\alpha$, hence $\kappa=\alpha R^2/\sigma^2$ and (76) becomes $\Gamma(n/2)\,e^{\kappa}/(2\alpha\kappa^{n/2})$, your Lemma 1′.

- **Relation.** The physics-literature home of the benchmark, including the spectral picture (gap grows linearly, lowest eigenvalue exponentially small) behind the near-exponential law of the OU exit time. The statement about the exponential law is for the OU process itself, via the spectral expansion, at the level of rigor of a review ("approximately"); it is not a theorem for non-OU drifts.

- **Mean exit time in one dimension with Kramers prefactor:** Grebenkov's eq. (39) and surrounding text note that the large-$\kappa$ forms "can be obtained by the Kramers theory of escape from a potential well".

### 4.3 Graczyk and Jakubowski 2008 [S]

- **Citation.** P. Graczyk and T. Jakubowski, "Exit times and Poisson kernels of the Ornstein–Uhlenbeck diffusion", Stochastic Models 24(2) (2008) 314–337. DOI 10.1080/15326340802009337. HAL record: https://hal.univ-angers.fr/hal-03040218. (A web-search summary I received gave the journal as Stochastics and Dynamics; Crossref says Stochastic Models.)

- **Content, second-hand.** Kersting et al. Remark 5: Theorem 2.2 there proves the same mean-exit-time formula for $\sigma=1$, $\theta\geq0$ (using hypergeometric functions), via a boundary value problem (their Theorem 2.1). Their abstract (via search): exit time of the OU diffusion from an open ball, expected exit time, exit-position law (the Poisson kernel of the ball). Not opened.

### 4.4 Other OU exit-time items

- **Guillaume 2026**, "The joint exit-time and exit-location law of a planar Ornstein–Uhlenbeck process on annular sectors and principal-axis rectangles", arXiv:2609.21685 (18 Sep 2026) [A, abstract and first page]: explicit eigenfunction expansions for the survival probability, density and moments of the exit time and the joint law with the exit boundary, isotropic planar OU on annular sectors. Relevant only if the full OU exit law in $n=2$ is wanted in closed spectral form; the ball case is also in Grebenkov (survival probability via Kummer functions, eqs. (63)–(73) there).

- **Jakubowski 2007**, "The estimates of the mean first exit time from a ball for the $\alpha$-stable Ornstein–Uhlenbeck processes", Stochastic Process. Appl. 117(10) (2007) 1540–1560. DOI 10.1016/j.spa.2007.02.007 [A, via RePEc]: sharp estimates for the expected first exit time from a ball for the OU process driven by an isotropic $\beta$-stable process, compared with the Gaussian OU diffusion. The abstract's quantifiers are garbled in my copy ("for all and r>0"). This is the heavy-tailed analogue of section 4.1 and the natural non-asymptotic OU benchmark if canon ever wants the heavy-tailed counterpart; the theorem itself was not read.

- **Ryznar 2025**, "On the mean exit time from a ball for a symmetric stable process", arXiv:2503.12272 [A]: pure stable process (no drift), Getoor's formula extended to any symmetric stable process up to a constant. Context only.

## 5. Small-noise asymptotics and the exit law for non-gradient drift

### 5.1 Berglund 2013 [R, section 2]

- **Citation.** N. Berglund, "Kramers' law: validity, derivations and generalisations", Markov Process. Related Fields 19(3) (2013) 459–490; arXiv:1106.5799 (v2, 22 Jan 2013): https://arxiv.org/abs/1106.5799.

- **Setting (his section 2).** $dx_t=f(x_t)\,dt+\sqrt{2\varepsilon}\,dW_t$ with "$f$ need not be equal to the gradient of a potential"; action functional $I(\varphi)=\tfrac12\int_0^T\lVert\dot\varphi-f(\varphi)\rVert^2\,dt$ (Wentzell–Freidlin, [VF70]); $x^\ast$ a stable equilibrium of $\dot x=f(x)$; $D$ a domain whose closure lies in the domain of attraction of $x^\ast$ (all orbits starting in $D$ converge to $x^\ast$); quasi-potential $V(z)=\inf_{T\gt0}\inf_{\varphi(0)=x^\ast,\varphi(T)=z}I(\varphi)$.

- **Theorem 2.2** ([VF69, VF70]). For $\tau=\inf\{t\gt0:x_t\notin D\}$ and any initial condition in $D$: $\lim_{\varepsilon\to0}2\varepsilon\log\mathbb{E}^{x_0}\{\tau\}=\inf_{z\in\partial D}V(z)=:\bar V$. Sketch of proof given (large deviations plus Markov property at multiples of a fixed time).

- **Theorem 2.3** ([Day83]). In the same situation, $\lim_{\varepsilon\to0}P\{\tau\gt s\,\mathbb{E}\{\tau\}\}=e^{-s}$ for all $s\gt0$. Not restricted to gradient $f$. The survey does not list the regularity hypotheses beyond "the situation described above".

- **Relation to the prefactor.** The survey says large deviations prove Arrhenius' law "for more general than gradient systems, but fails to control the prefactor"; the Eyring–Kramers prefactor is proved for gradient systems (his section 3, BEGK04). For $f=-\alpha\delta$, $2\varepsilon=\sigma^2$, $\bar V=\alpha R^2$; the exponent in your normalization is $\sigma^2\log\mathbb{E}\tau\to\inf_{\partial D}V$ with $V$ built from $I=\tfrac12\int\lvert\dot\varphi+F(\varphi)\rvert^2$.

### 5.2 Day 1983 and related [R for the survey, S for the 1983 paper]

- **Citation.** M. V. Day, "On the exponential exit law in the small parameter exit problem", Stochastics 8(4) (1983) 297–323. DOI 10.1080/17442508308833244. **Primary not read** (publisher page returned HTTP 403; not on the author's page).

- **What the author says of it, 1999 survey [R].** M. V. Day, "Mathematical approaches to the problem of noise-induced exit", in *Stochastic Analysis, Control, Optimization and Applications: A Volume in Honor of W. H. Fleming* (McEneaney, Yin, Zhang eds.), Birkhäuser 1999, pp. 269–287; DOI 10.1007/978-1-4612-1784-8_16; preprint https://personal.math.vt.edu/daymv/research/Exit.pdf. Setting there: $dx^\varepsilon=b(x^\varepsilon)\,dt+\varepsilon^{1/2}\sigma(x^\varepsilon)\,d\omega$, $D$ the basin of an asymptotically stable point; "typical regularity assumptions would require $a(\cdot),b(\cdot)$ to be $C^3$, with a positive definite hypothesis on $a(\cdot)$. Similarly $D$ is assumed to be bounded with $C^3$ boundary", the survey explicitly not concerned with precise hypotheses. Its eq. (1.13): "A relative leveling result for the mean exit time is provided by Corollary 1 of [7] [Day 1983]: $\lambda^\varepsilon\,\mathbb{E}_x[\tau^\varepsilon_D]\to1$, holding uniformly on any compact $K\subseteq D$" (superscripts restored; the text extraction dropped them), with $\lambda^\varepsilon$ the principal Dirichlet eigenvalue; and: "The treatment in [7] only considered the nontangential case", i.e. $n\cdot b\lt0$ on $\partial D$. This is the source of the exponential law (principal-eigenvalue dominance plus leveling). Note: your $\bar{\mathcal B}_R$ has $\langle b,n\rangle\leq-\alpha R\lt0$ on the boundary, so it is the nontangential case.

- **Williams 1982** [S]. M. Williams, "Asymptotic exit time distributions", SIAM J. Appl. Math. 42(1) (1982) 149–154. DOI 10.1137/0142012. From the SIAM abstract as surfaced by search: a deterministic system with a single attracting critical point perturbed by nondegenerate white noise; "the limiting distribution of the exit time is exponential in the potential case" — gradient only. Not opened. (Not the same as R. G. Williams's 1978 Caltech thesis.)

### 5.3 Aleksian and Villeneuve [R, arXiv v1]

- **Citation.** A. Aleksian and S. Villeneuve, "Freidlin–Wentzell type exit-time estimates for time-inhomogeneous diffusions and their applications", arXiv:2501.11797 (v1, 21 Jan 2025); published in Stochastic Process. Appl. 197 (2026) 104932, DOI 10.1016/j.spa.2026.104932. I read the arXiv v1; the published text may differ.

- **Classical result restated (their section 1).** $dZ=\sqrt\varepsilon\sigma(Z)\,dW+b(Z)\,dt$; "we will always assume that $b$ and $\sigma$ are continuous Lipschitz functions". Assumption 1.1: unique stable equilibrium $a\in D$ for the flow, $D$ positively invariant with all orbits converging to $a$. Assumption 1.2: $\langle b(x),n(x)\rangle\lt0$ on $\partial D$. Assumption 1.3: all eigenvalues of the Jacobian of $b$ at $a$ are negative (they remark this gives $\langle b(x),x-a\rangle\leq-L\lvert x-a\rvert^2$ for some $L\gt0$, near $a$). Assumption 1.4: $\lambda^{-1}\lt\lVert\sigma\rVert\lt\lambda$ on $D$, $\sigma\sigma^\ast$ uniformly positive definite on $\partial D\cup\{a\}$. They add that these are special cases of Assumptions (A-1) to (A-4) of Dembo–Zeitouni [Chapter 5] and of Exercise 5.7.29 there. **Proposition 1.5** (Freidlin–Wentzell): for compact $K\subset D$, (1) for every $\eta\gt0$, $\liminf_{\varepsilon\to0}\inf_{x\in K}P(\exp(2(H-\eta)/\varepsilon)\leq\tau\leq\exp(2(H+\eta)/\varepsilon))=1$; (2) $\lim_{\varepsilon\to0}\tfrac\varepsilon2\log\mathbb{E}[\tau]=H$ uniformly on $K$; (3) exit-location concentration on the minimisers of $Q$; here $H=\inf_{y\in\partial D}Q(y)$ is the height of the quasi-potential.

- **Their remark on the open problem** (verbatim): "Proving the Eyring-Kramers formula under the general assumptions of Freidlin and Wentzell remains an open problem."

- **Relation.** The most explicit restatement of the Freidlin–Wentzell hypotheses I found; compare with A2′ on the ball: strict inward pointing on $\partial\mathcal B_R$ (Assumption 1.2) follows from A2′ as $\langle b,n\rangle\leq-\alpha R$; positive invariance and convergence to $0$ (Assumption 1.1) follow from $\tfrac{d}{dt}\lVert x\rVert^2\leq-2\alpha\lVert x\rVert^2$ along the flow (my check); Assumption 1.3 follows if $F$ is differentiable at $0$ (the symmetric part of $DF(0)$ is at least $\alpha I$); nondegeneracy holds for $\sigma I$. What A2′ does not supply is Lipschitz continuity of $b$.

### 5.4 Huisinga, Meyn, Schütte 2004 [R: abstract, introduction, Theorems 3.1–3.2 and section 3.2 start; not the quantitative exit-time theorem]

- **Citation.** W. Huisinga, S. Meyn, C. Schütte, "Phase transitions and metastability in Markovian and molecular systems", Ann. Appl. Probab. 14(1) (2004) 419–458. DOI 10.1214/aoap/1075828057. PDF (FU Berlin repository): http://publications.imp.fu-berlin.de/67/1/HuMeSc04.pdf.

- **Abstract (quoted in part).** Main assumption "$V$-uniform ergodicity of the process" ("equivalent to any common formulation of exponential ergodicity"); "the conditional distributions of exit times are approximately exponential. These results represent a significant expansion of the classical Wentzell–Freidlin theory. In particular, the results require no special structure beyond geometric ergodicity; reversibility is not assumed". The introduction: "As a direct consequence of geometric ergodicity of the associated twisted process we find that the distribution of the exit time is approximately exponential. The magnitude of the error is related to the spectral gap for this twisted process"; a spectral gap in the weighted $L_\infty$ setting is equivalent to geometric ergodicity, equivalent to the existence of a Lyapunov function.

- **Theorem 3.2(i), as I read the page image.** For a diffusion satisfying their (13): if some $h\gt0$ (finite a.e.) has $\mathcal Ah\leq-\bar\Gamma h$ on $A$, then the exit rate satisfies $\Gamma(A)\geq\bar\Gamma$. That bounds the exit *rate* from below, i.e. exits are at least that fast: the wrong side for a lower bound on $\tau$. Part (ii) is the converse existence statement; part (iii) an eigenfunction equation on a metastable set.

- **Relation.** If A2′ held on all of $\mathbb{R}^n$ (with $F$ locally Lipschitz), $V(\delta)=\lVert\delta\rVert^2$ would satisfy $\mathcal L V\leq-2\alpha V+n\sigma^2$, a Lyapunov function, hence $V$-uniform ergodicity, and the framework applies to non-gradient $F$ without Lipschitz-based large deviations. Whether the ball is a metastable set in their sense and what the explicit error bound is for it, I did not check; this is a route to an exponential-law statement for non-gradient $F$, not a statement I can attest. A2′ on the ball alone does not give global ergodicity.

### 5.5 Prefactors for non-reversible drift; gradient case

- **BEGK 2004 and BGK 2005** (gradient, reversible; Eyring–Kramers prefactor): A. Bovier, M. Eckhoff, V. Gayrard, M. Klein, J. Eur. Math. Soc. 6(4) (2004) 399–424, DOI 10.4171/jems/14; A. Bovier, V. Gayrard, M. Klein, J. Eur. Math. Soc. 7(1) (2005) 69–99, DOI 10.4171/jems/22 [A]. Not opened; their gradient hypothesis is as described by Berglund.

- **Bouchet–Reygner 2016** [A]: F. Bouchet, J. Reygner, "Generalisation of the Eyring–Kramers transition rate formula to irreversible diffusion processes", Ann. Henri Poincaré 17(12) (2016) 3499–3532, DOI 10.1007/s00023-016-0507-4, arXiv:1507.02104. Abstract: prefactor for irreversible diffusions with the Freidlin–Wentzell quasi-potential playing the role of the potential, "a correction depending on the non-Gibbsianness of the system along the instanton"; method "a WKB analysis of the quasistationary distribution ... and a probabilistic study of the process in the neighbourhood of saddle-points". A search snippet describes Berglund 2021 as justifying their formal result for a particular class; I take Bouchet–Reygner to be formal-asymptotic, not opened.

- **Landim, Mariani, Seo 2019** [A]: "Dirichlet's and Thomson's principles for non-selfadjoint elliptic operators with application to non-reversible metastable diffusion processes", Arch. Ration. Mech. Anal. 231(2) (2019) 887–938, DOI 10.1007/s00205-018-1291-8. **Lee and Seo**, "Non-reversible metastable diffusions with Gibbs invariant measure I: Eyring–Kramers formula", arXiv:2008.08291 (abstract read): rigorous Eyring–Kramers formula for non-reversible diffusions with a Gibbs invariant measure, showing the non-reversible transition is faster than the reversible one. Both are rigorous prefactor results for a *structured* non-gradient drift (Gibbs invariant measure), not for a one-point monotone drift.

- **Non-asymptotic Kramers-type bounds for non-gradient drift under a monotonicity hypothesis:** none found. The nearest are the comparison arguments of section 3, which are not stated as exit-time bounds in the sources found.

### 5.6 Books [M or S]

- A. Dembo, O. Zeitouni, *Large Deviations Techniques and Applications*, 2nd ed., Springer 1998 (corrected 2010), Theorem 5.7.11 and Exercise 5.7.29 [S, via Aleksian–Villeneuve and other papers' citations of "Theorem 5.7.11(a)" for the exit-time asymptotics]. Not read. The hypotheses are Assumptions (A-1)–(A-4) of its Chapter 5 per Aleksian–Villeneuve.
- M. I. Freidlin, A. D. Wentzell, *Random Perturbations of Dynamical Systems*, 3rd ed., Springer 2012 (2nd ed. 1998), Chapter 4 on a single asymptotically stable equilibrium [S, publisher blurb]. Theorem numbers not verified; not read. Original papers cited by Berglund: [VF69], [VF70].

## 6. Heavy-tailed noise

Stable index is written $\beta$ below; the sources call it $\alpha$.

### 6.1 Imkeller and Pavlyukevich 2006 [R, arXiv v2 text]

- **Citation.** P. Imkeller, I. Pavlyukevich, "First exit times of SDEs driven by stable Lévy processes", Stochastic Process. Appl. 116(4) (2006) 611–642. DOI 10.1016/j.spa.2005.11.006. arXiv:math/0409246 (v2, 31 Jan 2006), under the title "First exit times of solutions of non-linear stochastic differential equations driven by symmetric Lévy processes with $\alpha$-stable components"; the arXiv front page says it will appear under the SPA title. https://arxiv.org/abs/math/0409246. I read the arXiv text, not the published version.

- **Setting.** $X^\varepsilon_t=x-\int_0^tU'(X^\varepsilon_{s-})\,ds+\varepsilon L_t$ in one dimension, $L$ the sum of a Brownian motion (variance $d\geq0$) and an independent symmetric $\beta$-stable Lévy process with Lévy measure $dy/\lvert y\rvert^{1+\beta}$, $0\lt\beta\lt2$. Potential: $U'(x)x\geq0$, $U'(x)=0$ iff $x=0$, $U''(0)=M\gt0$; $U'$ locally Lipschitz and growing faster than linear at $\pm\infty$; $U\in C^3$ on a sufficiently large interval around $0$. Exit from $[-b,a]$, $\sigma(\varepsilon)=\inf\{t:X^\varepsilon_t\notin[-b,a]\}$.

- **Theorem 1.1.** There are $\varepsilon_0,\gamma,\delta,C\gt0$ such that for $0\lt\varepsilon\leq\varepsilon_0$, uniformly for $x\in[-b+\varepsilon^\gamma,a-\varepsilon^\gamma]$ and $u\geq0$, with $\theta=a^{-\beta}+b^{-\beta}$:

$$\exp\Big(-u\varepsilon^\beta\tfrac{\theta}{\beta}(1+C\varepsilon^\delta)\Big)(1-C\varepsilon^\delta)\leq P_x(\sigma(\varepsilon)\gt u)\leq\exp\Big(-u\varepsilon^\beta\tfrac{\theta}{\beta}(1-C\varepsilon^\delta)\Big)(1+C\varepsilon^\delta),$$

and consequently

$$\mathbb{E}_x\sigma(\varepsilon)=\frac{\beta}{\varepsilon^\beta}\Big(\frac1{a^\beta}+\frac1{b^\beta}\Big)^{-1}(1+O(\varepsilon^\delta)).$$

Theorem 1.2 is the one-sided counterpart: $\mathbb{E}_x\tau(\varepsilon)=\beta a^\beta\varepsilon^{-\beta}(1+O(\varepsilon^\delta))$ for exit from $(-\infty,a]$.

- **Their own summary of the mechanism (quoted, introduction).** "Instead of the height of the potential well, a large jump to exit just takes note of the distance from the domain's boundary. Pure horizontal distances replace geometric quantities related to the potential in the large deviations' estimates for exit times in the $\alpha$-stable Lévy case. Also, the mean values of the exit times change essentially in comparison to the Gaussian noise setting: instead of Kramers' times we obtain exit times of the order of $\varepsilon^{-\alpha}$ in the small noise limit, i.e. times of polynomial instead of exponential dependence on $\varepsilon$."

- **Relation.** This is the citable source for "polynomial rather than exponential expected exit time", with the exact hypotheses above: one dimension, gradient drift $-U'$, additive noise $\varepsilon L$ with $\varepsilon\to0$ and a fixed interval; the leading term does not contain $U$ at all (only $a$, $b$, $\beta$, $\varepsilon$), which is the precise sense in which drift strength does not buy exit time at leading order under heavy tails. It is an asymptotic statement ($\varepsilon\leq\varepsilon_0$, unspecified constants), not a non-asymptotic bound, and it does not cover multiple dimensions or non-gradient drift (see 6.3). Their section 1 also states the Gaussian counterpart for comparison: Kramers' law and the exponential law of $\hat\sigma(\varepsilon)/\mathbb{E}\hat\sigma(\varepsilon)$ (citing Williams 1982, Day 1983, Bovier–Gayrard–Klein 2005).

### 6.2 The rest of the one-dimensional lineage

- **Imkeller–Pavlyukevich–Wetzel 2009** [R, abstract]: "First exit times for Lévy-driven diffusions with exponentially light jumps", Ann. Probab. 37(2) (2009) 530–564, DOI 10.1214/08-AOP412, arXiv:0711.0982. Jump measure with $\nu([u,\infty))\sim\exp(-u^\beta)$: the exit time has an exponential tail and $\ln\mathbb{E}\sigma\sim\varepsilon^{-\beta}$ for $0\lt\beta\lt1$, $\ln\mathbb{E}\sigma\sim\varepsilon^{-1}\lvert\ln\varepsilon\rvert^{1-1/\beta}$ for $\beta\gt1$ ("an intriguing phase transition at the critical index $\beta=1$"). Light jumps: between polynomial and Gaussian.
- **Yang and Duan 2008** [A, abstract]: "An intermediate regime for exit phenomena driven by non-Gaussian Lévy noises", Stoch. Dyn. 8(3) (2008) 583–591, DOI 10.1142/S0219493708002469, arXiv:0808.1085: "for a class of non-Gaussian Lévy noises ... the mean exit time is asymptotically faster than exponential ... but slower than polynomial".
- **Imkeller–Pavlyukevich 2008** [A]: "Metastable behaviour of small noise Lévy-driven diffusions", ESAIM Probab. Stat. 12 (2008) 412–437, DOI 10.1051/ps:2007051, arXiv:math/0601771: multi-well one-dimensional potential, heaviest tail regularly varying; metastable (Markov-jump) behaviour on a polynomial time scale.
- **Pavlyukevich 2011** [S, search summary]: "First exit times of solutions of stochastic differential equations driven by multiplicative Lévy noise with heavy tails", Stoch. Dyn. 11(2–3) (2011) 495–519, DOI 10.1142/S0219493711003413: first exit from a bounded domain for a gradient system under small multiplicative heavy-tailed Lévy noise. Not opened.

### 6.3 Finite-dimensional, non-gradient: Högele and Pavlyukevich 2014 [R]

- **Citation.** M. Högele, I. Pavlyukevich, "The exit problem from a neighborhood of the global attractor for dynamical systems perturbed by heavy-tailed Lévy processes", Stoch. Anal. Appl. 32(1) (2014) 163–190. DOI 10.1080/07362994.2014.858554. arXiv:1303.5031: https://arxiv.org/abs/1303.5031 (read v1, Mar 2013; the published text may differ).

- **Setting.** $\dot u=f(u)$ on a bounded domain $D\subset\mathbb{R}^d$ with piecewise $C^1$ boundary, $f\in C^2(D)$ pointing uniformly inward at $\partial D$, a global attractor $A\subset D$ carrying a unique invariant measure $P$ in the time-average sense (D.1) (stable fixed point and stable limit cycle are the examples); perturbation by multiplicative noise driven by a Lévy process whose Lévy measure is regularly varying at infinity with index $-\beta$ (S.1) (tail $h(r)=r^{-\beta}/\ell(r)$), and coefficients satisfying local Lipschitz and boundedness conditions (S.2) (Itô, Fisk–Stratonovich and Marcus forms covered). Exit time $T_x(\varepsilon)$ from $D$.

- **Theorem 2.1 and Corollary 2.1.** Under (D.1), (S.1–2), $Q(\partial D)=0$ and $Q(D^c)\gt0$ with $Q(U)=\int_A\mu(E^U(y))\,P(dy)$ and $h_\varepsilon=h(1/\varepsilon)$: $Q(D^c)\,h_\varepsilon\,T_x(\varepsilon)\xrightarrow{d}\mathrm{EXP}(1)$ and $P(X^\varepsilon_{T_x(\varepsilon)}\in U)\to Q(U\cap D^c)/Q(D^c)$, uniformly over initial values in $D_{\varepsilon^\gamma}$, $\gamma\in(0,\tfrac15)$. Since $h_\varepsilon$ is regularly varying of index $\beta$ in $1/\varepsilon$, the exit time is of algebraic order in $1/\varepsilon$ and asymptotically exponentially distributed.

- **Their statement of context (quoted).** "For the case of non-gradient and degenerate systems we refer to [2, 8, 13]. They all have in common that the first exit time rate grows in $\varepsilon$ with the order $\exp(\bar V/\varepsilon^2)$"; and for heavy tails the stable-fixed-point case was "treated in [9, 14, 18, 19, 24]" (gradient or point attractors); the exit "occurs when a system jumps from a vicinity of $s$".

- **Relation.** The finite-dimensional non-gradient (and non-fixed-point attractor) counterpart of 6.1, at the same level of generality as the Freidlin–Wentzell non-gradient statement in the Gaussian case: small-noise, regular variation, drift $C^2$ and inward pointing, no monotonicity hypothesis of the one-point type. For canon: "algebraic of order $h(1/\varepsilon)^{-1}$" is citable here for $d\geq1$; the exact constant depends on the jump distribution and the attractor's invariant measure.

- **Högele–Pavlyukevich 2015** [A]: "Metastability in a class of hyperbolic dynamical systems perturbed by heavy-tailed Lévy type noise", Stoch. Dyn. 15(3) (2015) 1550019, DOI 10.1142/S0219493715500197; finite-dimensional Morse–Smale-type systems; not opened.

### 6.4 Dissipativity under heavy tails, and discrete time

- **Kulik and Pavlyukevich 2021** [A]: "Moment bounds for dissipative semimartingales with heavy jumps", Stochastic Process. Appl. 141 (2021) 274–308, DOI 10.1016/j.spa.2021.07.004, arXiv:2004.12449. Abstract: if large jumps have a finite $p$-moment, "the radial part of its drift is dominated by $-\lvert X\rvert^\kappa$ for some $\kappa\geq-1$, and the balance condition $p+\kappa\gt1$ holds", then $\sup_t\mathbb{E}\lvert X_t\rvert^{p_X}\lt\infty$ for $p_X\in(0,p+\kappa-1)$, an upper bound that is "generically optimal"; proof by Lyapunov functions for semimartingales. A radial (one-point) dissipativity hypothesis in the heavy-tailed setting, hence the natural place to look for the heavy-tailed analogue of the stopped second-moment statement in Prop A.1S(i); I read the abstract only. Their $\kappa$ is not the $\kappa$ of this scan.

- **Wang and Rhee 2026** [R, assumptions and Corollary 3.2; the proofs not read]: "First-exit time analysis for truncated heavy-tailed dynamical systems", arXiv:2602.07968 (8 Feb 2026), https://arxiv.org/abs/2602.07968; unrefereed as far as I know. Discrete-time $X^\eta_{j+1}=X^\eta_j+\eta a(X^\eta_j)+\eta\sigma(X^\eta_j)Z_{j+1}$ and a truncated variant, noise $Z$ multivariate regularly varying with index $\beta\gt1$ and $\mathbb{E}Z=0$ (Assumption 1), $a,\sigma$ Lipschitz (Assumption 2), Assumption 3: $a(0)=0$, $I$ bounded open containing $0$, the flow $\dot y=a(y)$ started in $I\setminus\{0\}$ stays in $I$ and converges to $0$, and $a(x)\cdot x\lt0$ in a small punctured ball about $0$; gradient structure is "of particular interest" but not assumed. Corollary 3.2 (untruncated case): under $C(\partial I)=0$ and $\lVert\sigma(0)\rVert\gt0$, $H(\eta^{-1})\,\tau^\eta(x)$ is asymptotically exponential (in the scaled sense with constant $C^\infty_I$) and exit locations are distributed by $C(\cdot)/C^\infty_I$. The abstract calls the results "a comprehensive heavy-tailed counterpart of the classical Freidlin–Wentzell theory". Relevant to the discrete-time open item (DA2′) because it is a discrete-time exit-time theory with non-gradient drift, small step size and heavy tails; it is small-step asymptotics with Lipschitz coefficients, so it does not supply a one-point-monotone non-asymptotic bound.

- **Hajek 1982 and the drift-analysis negative-drift theorem** [A, plus a secondary statement]: B. Hajek, "Hitting-time and occupation-time bounds implied by drift analysis with applications", Adv. Appl. Probab. 14(3) (1982) 502–525, DOI 10.2307/1426671. Abstract (via search): exponential-type bounds on first-hitting and occupation times of a real sequence with uniform negative drift above a level and a uniform exponential decay condition on increments. Lengler, "Drift analysis", arXiv:1712.00964, Theorem 22 ("Negative Drift", following Oliveto–Witt and Hajek): for a process with $\mathbb{E}[X_t-X_{t+1}\mid\mathcal F_t,X_t=s]\leq-\delta$ and increments with geometrically decaying tails, started at $X_0\geq bn$, $\Pr[T_a\leq e^{cn}]\leq e^{-cn}$ for the hitting time $T_a$ of $[0,an]$ ($a\lt b$), with $c$ existing but not explicit in that statement. Mapping $X_t=R-\lVert\delta_t\rVert$, a restoring drift is drift away from the target, so this is the discrete-time relative of the exit-time lower bound, with uniform (not radius-proportional) drift and non-explicit constants. Not read in the original.

## 7. What 2025–2026 adds, in one place

No 2025–2026 source found states the comparison or the exit-time domination you derive; searches for it (radial comparison, one-sided Lipschitz or strongly monotone drift, exit time, Ornstein–Uhlenbeck benchmark, non-asymptotic Kramers bound) returned the items below and nothing closer. The items, each described in its section: Geng–Markowsky (Stochastic Models 2025; arXiv v2 Jun 2025), the squared-modulus Ikeda–Watanabe argument and the Remark 1 caution (3.2); Altmeyer v3 (Jul 2025), the Langevin comparison step (3.4); Aleksian–Villeneuve (arXiv Jan 2025, SPA 197 (2026)), the cleanest restatement of the Freidlin–Wentzell hypotheses and the open-problem sentence (5.3); Li–Zhang v9 (Sep 2026), the radial same-Brownian comparison for bounded Borel drift (3.5); Wang–Rhee (Feb 2026), the discrete-time heavy-tailed Freidlin–Wentzell analogue (6.4); Grebenkov v2 (Jun 2025) with its July 2025 corrigendum, the benchmark (4.2); Guillaume (Sep 2026), planar OU exit law on annular sectors (4.4); Ryznar (Mar 2025), pure stable ball exit (4.4). Huang–Kim–Mao v2 (Jan 2024) is set aside (3.6).

## 8. Not opened: where a textbook version probably lives

Nothing below was opened and no theorem numbers are given, because I could not check them. These are the places I would look next, from general knowledge of the field [M]: Khasminskii, *Stochastic Stability of Differential Equations* (Lyapunov-function and Dynkin-formula estimates of mean exit times from bounded domains); Karatzas–Shreve, *Brownian Motion and Stochastic Calculus* and Revuz–Yor, *Continuous Martingales and Brownian Motion* (the one-dimensional SDE comparison theorem, in the Yamada–Watanabe form); Hsu, *Stochastic Analysis on Manifolds* (radial-process comparison); Øksendal, *Stochastic Differential Equations* (Dynkin formula and the Dirichlet–Poisson problem; your derivation cites "9.3.3 from memory", which I also could not verify, while Kersting et al. cite Schuss 2010, Theorem 4.4.3 and Corollary 4.4.1, for the Andronov–Vitt–Pontryagin identification, which is verified as their citation but not opened). The absence of the statement from the sources I did open does not show it is absent from these.

## 9. Numerical checks run for this scan

Checks of the sources' formulas with independent code (mpmath quadrature; Euler–Maruyama in numpy); units $\alpha=1$, $R=1$, $\sigma^2=1/\kappa$, so every mean exit time below is $\alpha\,\mathbb{E}\tau$. These corroborate; they are not the basis of any statement above.

- **Formula against simulation.** Kersting et al. eq. (17) at $n=3$, $\kappa=3$: $2.232$. Euler–Maruyama with $4000$ paths: $2.240\pm0.029$ at $\Delta t=2.5\times10^{-4}$ and $2.250\pm0.028$ at $\Delta t=6.25\times10^{-5}$ (and $2.343\pm0.030$ at $10^{-3}$, where discrete monitoring misses exits and biases the mean up).

- **Leading asymptotic (Grebenkov (76)) against the exact formula**, ratio exact/asymptotic (rounded):

  | $n$ | $\kappa=5$ | $\kappa=20$ | $\kappa=40$ | $\kappa=80$ |
  |---|---|---|---|---|
  | 1 | 1.126 | 1.027 | 1.013 | 1.0064 |
  | 3 | 1.445 | 1.087 | 1.040 | 1.019 |
  | 10 | 1.559 | 1.372 | 1.148 | 1.068 |

  At small $\kappa$ the ratio is below $1$ (for example $0.288$ at $n=1$, $\kappa=0.5$; $0.654$ at $n=3$, $\kappa=1.5$; $0.948$ at $n=5$, $\kappa=2.5$; $0.0009$ at $n=30$, $\kappa=5$), and it is above $1$ at moderate $\kappa$ for larger $n$ ($1.56$ at $n=10$, $\kappa=5$; $3.37$ at $n=30$, $\kappa=15$). So (76) is a large-$\kappa$ asymptotic, not a bound. Numerically $(\text{ratio}-1)\,\kappa\to n/2$ ($0.51$, $1.55$, $5.4$ at $\kappa=80$ for $n=1,3,10$); a direct expansion of eq. (17) (integrate by parts once in the outer integral; the correction from the inner integral's tail is $O(\log\kappa)$ against $e^{\kappa}$) gives $\Phi(0)=\frac{\Gamma(n/2)}{2\alpha}\kappa^{-n/2}e^{\kappa}\big(1+\frac{n}{2\kappa}+O(\kappa^{-2})\big)$, which is a sharper form of your Lemma 1′ than $1+O(\kappa^{-1})$ (my calculation, consistent with these numbers).

- **At the mean-square threshold $\kappa=n/2$**, $\alpha\,\Phi(0)$: $0.596$ ($n=1$), $0.659$ ($n=2$), $0.706$ ($n=3$), $0.777$ ($n=5$), $0.889$ ($n=10$), $1.096$ ($n=30$). These agree with the values tabulated in your Corollary 4 ($0.60,0.66,0.71,0.78,0.89$; and between your $1.02$ at $n=20$ and $1.20$ at $n=50$ for $n=30$).

- **Kersting et al. Theorem 7 at $x=0$**, reading (33)–(36) as: lower bounds $\kappa/n$ (the Brownian value $R^2/(n\sigma^2)$, eq. (36)) and $\frac{1+2/n}{2\alpha}\big(e^{2\kappa/(n+2)}-1\big)$ (eq. (35), re-derived from their eqs. (42)–(43)); upper bounds (33) and (34), with (34) read as $(e^{\kappa}-1)/(n\alpha)$ from their eq. (40). No violation of the ordering lower $\leq$ exact $\leq$ (33) $\leq$ (34) at $n\in\{1,2,3,5,10,30\}$, $\kappa\in\{n/2,n,5,20,40\}$ (30 cases). Illustrations of how weak the lower bound is: $n=10$, $\kappa=20$: exact $2497$, lower (35) $16.2$, upper (33) $8.1\times10^{6}$, upper (34) $4.9\times10^{7}$; $n=1$, $\kappa=5$: exact $66.2$, lower (35) $40.5$, upper (33) $99.9$, upper (34) $147.4$.

## 10. Observations of mine arising from the reading (unrefereed)

### 10.1 Ikeda–Watanabe Theorem 1.1 applied to $\lVert\delta\rVert^2$ covers your Theorem 2 without Tanaka or polarity

This is my reading of the statement of Theorem 1.1 and Remark 1.1 (section 3.1 above), not something I found in print; the Geng–Markowsky section 4 sketch does the same thing for a different family.

- $x_1:=\lVert\delta\rVert^2$ satisfies $dx_1=(n\sigma^2-2\delta^\top F(\delta))\,dt+2\sigma\sqrt{x_1}\,dB$ with $B=\int\hat\delta\cdot dW$ ($\hat\delta:=e_1$ when $\delta=0$), a Brownian motion by Lévy's characterization; no local-time term appears for any $n\geq1$.
- Take $\sigma(\xi)=2\sigma\sqrt{\xi^+}$ (Yamada modulus $\rho(\xi)=2\sigma\sqrt\xi$, $\int_{0+}\rho^{-2}=\infty$) and $b_1=b_2=b$, $b(\xi)=n\sigma^2-2\alpha\xi$, continuous. A2′ gives $\beta_1(t)=n\sigma^2-2\delta_t^\top F(\delta_t)\leq b(x_1(t))$ for $t\leq\tau_R$; take $x_2$ the strong solution of $dx_2=\sigma(x_2)\,dB+b(x_2)\,dt$, $x_2(0)=\lVert x\rVert^2$, with $\beta_2=b(x_2)$.
- Here $b_1=b_2$, so the weak form (1.3)′ is needed, which requires pathwise uniqueness for one of the two equations: it holds for $dX=2\sigma\sqrt{X}\,dB+(n\sigma^2-2\alpha X)\,dt$ by the Yamada–Watanabe theorem (Yamada–Watanabe 1971 is item [11] in Ikeda–Watanabe's bibliography; I did not open it).
- Remark 1.1 with $S=\tau_R$ gives $x_1\leq x_2$ on $[0,\tau_R)$ almost surely, so $\tau_R(\delta)\geq\tau_R(x_2)$ almost surely; $x_2$ has the law of $\lVert Y\rVert^2$ for the OU process $Y$ (uniqueness in law of the same equation). The conclusion is pathwise domination, hence stochastic domination of the exit law.
- What it requires of $F$: Borel measurable, locally bounded on the ball, and a weak solution; the processes $\beta_i$ must be "well-measurable" in Ikeda–Watanabe's phrasing, and I checked only that $\beta_1$ is progressively measurable (a progressively measurable process has an optional version equal to it $dt$-a.e., which should suffice, but I did not verify). Section 3 of Ikeda–Watanabe (the smooth, locally-Lipschitz-envelope version) would not give this; Theorem 1.1 does.
- Squaring the radius is also what removes the singular Bessel drift $(n-1)\sigma^2/(2r)$: Theorem 1.1 asks for continuous $b_i$ on $[0,\infty)\times\mathbb{R}$, which the radius itself does not have for $n\geq2$.

### 10.2 A2′ lower-bounds the Freidlin–Wentzell quasi-potential barrier by $\alpha R^2$, deterministically

With action $I_T(\varphi)=\tfrac12\int_0^T\lvert\dot\varphi+F(\varphi)\rvert^2\,dt$ and $\varphi(0)=0$, for any absolutely continuous $\varphi$ staying in $\bar{\mathcal B}_R$ (all that is needed for paths up to their first hit of $\partial\mathcal B_R$):

$$\tfrac{d}{dt}\,\alpha\lvert\varphi\rvert^2=2\alpha\varphi\cdot(\dot\varphi+F)-2\alpha\varphi\cdot F\leq2\alpha\lvert\varphi\rvert\lvert\dot\varphi+F\rvert-2\alpha^2\lvert\varphi\rvert^2\leq\tfrac12\lvert\dot\varphi+F\rvert^2+2\alpha^2\lvert\varphi\rvert^2-2\alpha^2\lvert\varphi\rvert^2,$$

so $\alpha\lvert\varphi(T)\rvert^2\leq I_T(\varphi)$ and $\min_{\partial\mathcal B_R}V\geq\alpha R^2$, with equality for $F=\alpha\delta$ along $\dot\varphi=\alpha\varphi$. Using the normalization of Berglund's Theorem 2.2 ($2\varepsilon=\sigma^2$, rate function $\tfrac12\int\lvert\dot\varphi-f\rvert^2$), this is the same inequality as $\liminf\sigma^2\log\mathbb{E}\tau_R\geq\alpha R^2$ in the Freidlin–Wentzell regime. It is a consistency check on the exponent, derived independently of exit-time comparison; it requires no Lipschitz hypothesis, but identifying $\min V$ with the actual exit exponent still does (section 5.3).
