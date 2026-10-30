*KR **C.2** (Objective C: "the theory is correct where it is known wrong, and stronger where strengthening was found"); item C1, expected exit time under Model S. Top intent, Joseph: "Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself."*

# De-novo feedback 1 on the exit-time spike — independent critical pass

Written 2026-10-30 (15:27 MDT start), against spike commit `96acba79`, repo HEAD `bce14e0b`, by an Opus verifier with a bare brief. Who reads this: the integrator who lands C1, the coordinator who routes it, and any second verifier. Findings are ordered by damage-if-wrong. Every numerical claim below is corroboration of an argument given beside it, and the scripts are inlined or described so they can be rerun.

**What I read whole:** `README.md`, `01-neighborhood-map.md`, `03-derivation.md`, `04-numerics.md`, `debrief.md`, `proposed-integration-plan.md`, the three `checks*-output.txt`; canon `#form-sector-condition` and the Model S parts of `#deriv-sector-condition` (Prop A.1S, Cor A.1S.1, Lemma A.1N and Remark, Epistemic Status, Findings, Working Notes) and `#deriv-stochastic-non-exit`. **Read in part:** `02-literature.md` §§1–3.5 and §10 headings; `checks.py` header and `Phi`. **Not read:** any primary source (Ikeda–Watanabe, Kersting et al., Grebenkov, Day); I relied on the scan's transcription of Ikeda–Watanabe Thm 1.1 and checked the spike's use of it against that transcription.

## Verdict in one paragraph

The spike's core mathematics holds: I re-derived Lemma 1, Lemma 1′ (fixed $n$), Theorem 1 in both directions with its equality clause, both proofs of Theorem 2, Corollary 3 and its comparison with Prop A.1S(iv), and an independent arbitrary-precision implementation of the benchmark reproduces the spike's numbers to four digits. Two of its displayed consequences are wrong as stated (Corollary 5's asymptotic form is not a sufficient condition; Corollary 2.1's moment claim is false), and one reading overreaches for non-tight agents (Corollary 4). The largest finding is not in the spike but under it: **canon's Prop A.1S(i) stopped bound is false whenever the mean-square condition (ii) holds**, it is jointly inconsistent with canon's own Cor A.1S.1, and the spike's neighborhood map inherited it as fact. That changes what the spike's result is for. It is not a sibling to place beside A.1S. It is the correct region-aware Model S statement, and it should replace the broken one. Four strengthenings are offered in §4 (adapted drift, every-start dominance of (iv), a rigorous non-asymptotic tenure condition, and anisotropic noise at the correct exponent), each tiered as my own work.

## 1. Canon break: Prop A.1S(i) is false under the mean-square condition, and (iii′)'s stated limit falls with it

**The statement** (`01-aat-core/src/deriv-sector-condition.md:153-155`): under (A1), (A2′) on $\mathcal B_R$, for all $t \geq 0$, $\mathbb{E}[\lVert\delta(t\wedge\tau_R)\rVert^2] \leq \lVert\delta(0)\rVert^2e^{-2\alpha t} + n\sigma_w^2/(2\alpha)$.

**Why it cannot hold, in canon's own objects (three lines, no spike result needed).**

1. On $\{\tau_R \leq t\}$ the stopped path sits on the sphere, so $\mathbb{E}[\lVert\delta(t\wedge\tau_R)\rVert^2] \geq R^2\,P(\tau_R \leq t)$.
2. Cor A.1S.1 (canon, exact) gives $P(\tau_R \lt \infty) = 1$, so $P(\tau_R \leq t) \to 1$ and the left side tends to $R^2$ (bounded convergence; it is in fact $\to R^2$ exactly).
3. The right side tends to $n\sigma_w^2/(2\alpha) = (R^\ast_S)^2$, which under (ii) is strictly less than $R^2$.

So (i), (ii) and Cor A.1S.1 cannot all hold. (i) is the one that is false: it fails at every finite $t$ past a point, exactly in the regime (ii) is meant for. When (ii) fails, (i)'s limit is at least $R^2$ and the inconsistency disappears, which is why the error is invisible until the condition the segment cares about is imposed.

**Where the derivation breaks** (`:221`, "Stopping-time localization … The stopped Grönwall bound (i) follows"). For the stopped process,

$$\frac{d}{dt}\mathbb{E}[V(\delta_{t\wedge\tau_R})] = \mathbb{E}\big[\mathbf 1_{\{t \lt \tau_R\}}\big(-\delta^\top F + \tfrac n2\sigma_w^2\big)\big] \leq -2\alpha\,\mathbb{E}\big[V(\delta_t)\mathbf 1_{\{t \lt \tau_R\}}\big] + \tfrac n2\sigma_w^2,$$

and the decay term carries the indicator: the mass frozen on the sphere does not decay. Replacing $\mathbb{E}[V\mathbf 1_{\{t\lt\tau\}}]$ by $\mathbb{E}[V(\delta_{t\wedge\tau})]$ is the step that is not available, and without it Grönwall does not close. Localization makes A2′ applicable; it does not make the frozen mass contract.

**Corroboration.** OU with $n = 2$, $\alpha = 2$, $\sigma_w = R = 1$ ($\kappa = 2 \gt n/2$, so (ii) holds), $\delta_0 = 0$, 20000 Euler–Maruyama paths at $dt = 2\cdot10^{-4}$, paths frozen at the sphere on exit:

| $t$ | $\mathbb{E}\lVert\delta_{t\wedge\tau}\rVert^2$ (MC) | canon (i) bound | $P(\tau_R \leq t)$ | $\mathbb{E}[\lVert\delta_t\rVert^2;\,\tau_R \gt t]$ |
|---|---|---|---|---|
| 0.25 | 0.323 | 0.316 | 0.107 | 0.216 |
| 0.5 | 0.511 | 0.432 | 0.343 | 0.168 |
| 1 | 0.741 | 0.491 | 0.650 | 0.091 |
| 2 | 0.927 | 0.500 | 0.902 | 0.025 |
| 4 | 0.995 | 0.500 | 0.993 | 0.002 |

```python
import numpy as np
rng=np.random.default_rng(11); n=2; a=2.0; s=1.0; R=1.0; dt=2e-4; N=20000
x=np.zeros((N,n)); stop=np.zeros(N,bool); cps=[0.25,0.5,1,2,4]; i=0
for k in range(1,int(4/dt)+2):
    act=~stop; xa=x[act]; xa=xa-a*xa*dt+s*np.sqrt(dt)*rng.standard_normal(xa.shape); x[act]=xa
    out=(xa*xa).sum(1)>R*R; idx=np.where(act)[0][out]
    x[idx]*=R/np.sqrt((x[idx]**2).sum(1))[:,None]; stop[idx]=True; t=k*dt
    if i<len(cps) and t>=cps[i]-1e-12:
        r2=(x*x).sum(1); print(t, r2.mean(), (n*s*s/(2*a))*(1-np.exp(-2*a*t)), stop.mean(), (r2*~stop).mean()); i+=1
```

**What is true instead** (strengthen-before-soften; these are the replacements I would put in front of the integrator).

- *(i′) The killed moment satisfies the displayed bound.* Itô on $e^{2\alpha s}V(\delta_s)$ over $[0, t\wedge\tau_R]$ with A2′ gives $\mathbb{E}[e^{2\alpha(t\wedge\tau)}V(\delta_{t\wedge\tau})] \leq V(\delta_0) + \tfrac{n\sigma_w^2}{4\alpha}(e^{2\alpha t}-1)$; dropping the non-negative $\{\tau \leq t\}$ part, $\mathbb{E}[\lVert\delta_t\rVert^2;\,\tau_R \gt t] \leq \lVert\delta_0\rVert^2e^{-2\alpha t} + \tfrac{n\sigma_w^2}{2\alpha}(1-e^{-2\alpha t})$. The last column of the table is this object. It is the scale of the mismatch *while still certified*, and it says nothing about mismatch after exit.
- *The exact stopped identity* is $\mathbb{E}\lVert\delta_{t\wedge\tau}\rVert^2 = \lVert\delta_0\rVert^2 + n\sigma_w^2\,\mathbb{E}[t\wedge\tau] - 2\,\mathbb{E}\int_0^{t\wedge\tau}\delta^\top F\,ds$. (iv) comes from dropping the last term rather than from the decay, so **(iv) survives**, and so does the spike's Corollary 3(ii) comparison.
- *(iii′)*: the inequality $P(\lVert\delta_t\rVert \gt R) \leq \mathbb{E}\lVert\delta_{t\wedge\tau}\rVert^2/R^2$ is true, but its limit is $1$, not $n\sigma_w^2/(2\alpha R^2)$. Under A2′ on the ball only, the unstopped tail after exit is uncontrolled: $F$ is arbitrary outside, so no fixed-time tail for the unstopped process follows. The displayed "stationary-sharp $n\sigma_w^2/(2\alpha R^2)$" is true under **global** A2′ (unstopped Grönwall then closes; this covers the sub-scope-$\alpha$ families with a global floor, such as Gaussian-mean, L2-regularized and linear-PD). Under local A2′ the correct region-aware fixed-time tail composes (i′) with the spike's Corollary 3. For $r \leq R$, $P_x(\lVert\delta_t\rVert \gt r) \leq P_x(\tau_R \leq t) + \mathbb{E}_x[\lVert\delta_t\rVert^2;\,\tau_R \gt t]/r^2 \leq \Big[1 - \frac{\Phi(\lVert x\rVert) - t}{\Phi(0)}\Big] + \frac{\lVert x\rVert^2e^{-2\alpha t} + (R^\ast_S)^2(1-e^{-2\alpha t})}{r^2}$. This holds whatever $F$ does outside the ball. It is the honest region-aware form, and it needs the spike's benchmark to exist.

**Cascade to check** (my grep; a verifier should re-grep rather than trust this list):

- `#deriv-sector-condition` :16 (summary), :153–165 ((i), (iii′)), :221 (localization), :244 and :263 (Findings tables, "stopped bound … stationary-sharp"), :272/:276 (Epistemic Status calls (i) and (iii′) exact), :309 (prior-art row).
- `#result-contraction-template` :61, where CT-S has the same stopped-Grönwall shape and the same defect in a weighted metric.
- `#result-sector-persistence-template` :93 ("stopped second-moment bound + the fixed-time tail … under the mean-square persistence condition").
- `#result-sector-condition-stability` and `#result-persistence-condition` consume "typical scale / fixed-time tail" and need re-reading under local versus global A2′.
- `#result-adversarial-exponent-regimes`: whether $b = 3/2$ rests on the $1/\sqrt\alpha$ scale under global A2′ (fine) or under the local-A2′ stopped bound (then it inherits the defect). I did not check this.

**History worth knowing.** Audits 742613 (FINAL §"Finding 2": "State only the stopped bound …") and 613842, and the no-go cycle that resolved them, certified the stopped bound as the safe fallback (`audits/audit-findings-742613.md:95-107`, `audits/audit-findings-613842.md:81-93`, "Cascade verified clean"). The object the 2026-05-16 cycle retreated *to* fails for the same reason as the object it retreated *from*: both treat the stopped second moment as if the frozen mass decayed. Read literally, (i)+(iii′) re-imply the deleted (iii): they bound $P(\tau_R \leq t)$ by a constant below one uniformly in $t$. That makes this a §2a regression-axis finding, not only a fresh defect.

**What it does to the spike.**

- `01-neighborhood-map.md` row 1 lists (i) as established canon. Corollary 4 says "the condition guarantees the typical scale of mismatch (Prop A.1S(ii)), as canon already states", and the debrief says "certifies scale, not tenure."
- Under the hypothesis canon actually states (A2′ on the ball), the mean-square condition certifies only the *killed* scale, and only for as long as the process stays certified. That duration is exactly $\tau_R$, and at the threshold the spike shows it is about one correction time from the origin.
- So the honest reading of (ii) under local A2′ is stronger than "scale, not tenure". Without a margin in $\kappa$ it certifies very little beyond a correction time. The spike's result is therefore more consequential than the spike claims: it is the only region-aware Model S containment statement canon would have that is true.
- Landing implication: the exit-time comparison and Corollary 3 should *replace* (i)/(iii′) as the region-aware content of Prop A.1S. They should not sit beside it as "the when to A.1S.1's whether". (i′), the global-A2′ version of (i)/(iii′), and (iv) are what remain.

## 2. Corollary 5's displayed asymptotic form is not a sufficient condition

The first display ($\Phi(0) \geq L/\epsilon \Rightarrow P_0(\tau_R \leq L) \leq \epsilon$) is exact and correct. The second, $\kappa - \tfrac n2\log\kappa \geq \log\tfrac{2\alpha L}{\epsilon\Gamma(n/2)}$, is labeled with the first under "[Exact as a sufficient condition]". It is defended as "a bounded additive error in the $\kappa$-condition", and that defense is false.

- **The left side is not monotone in $\kappa$.** It decreases on $(0, n/2)$ and tends to $+\infty$ as $\kappa \to 0$. So the displayed condition is satisfied by arbitrarily *weak* correction.
- **Counterexample, $n = 2$.** Take $\alpha = 1$, $R = 1$, $\sigma_w = 10$ (so $\kappa = 0.01$), $L = 1$ (one correction time) and $\epsilon = 0.02$. Then LHS $= 4.615 \geq$ RHS $= 4.605$, so the condition "certifies" $P_0(\tau_R \leq 1) \leq 0.02$. The exact value is $\Phi(0) = 0.00501$, essentially the Brownian $R^2/(n\sigma_w^2) = 0.005$, against $L/\epsilon = 50$; the asymptotic formula gives $50.5$. The process leaves in about $1/200$ of a correction time, and $P_0(\tau_R \leq 1) \approx 1$.
- **Counterexample, $n = 100$, below the threshold.** Take $\kappa = 25$, half the mean-square threshold, with $\alpha = 25$, $\sigma_w = R = 1$, $L = 1$, $\epsilon = 0.01$. The condition is satisfied ($-135.94 \geq -136.05$). The exact $\alpha\Phi(0) = 0.342$ against $\alpha L/\epsilon = 2500$; the asymptotic gives $2.8\times10^3$.
- **Why.** Lemma 1′'s $(1+O(\kappa^{-1}))$ is non-uniform in $n$. The endpoint Laplace step uses $\tfrac{d}{du}[\alpha u^2/\sigma_w^2 - (n-1)\log u]$ at $u = R$, which is $(2\kappa - n + 1)/R$, not $2\kappa/R$. The uniform leading form is therefore $\Phi(0) \approx \Phi_{\text{asym}}\cdot\frac{\kappa}{\kappa - (n-1)/2}$, valid once $\kappa - n/2 \gg \sqrt n$. Below $\kappa \approx n/2$ the asymptotic overestimates by orders of magnitude.

$\Phi(0)/\Phi_{\text{asym}}$, independent mpmath implementation ($\sigma_w = R = 1$):

| $n$ | $\kappa = n/4$ | $\kappa = n/2$ | $\kappa = 3n/4$ | $\kappa = n$ | $\kappa = 2n$ | $\kappa = 4n$ |
|---|---|---|---|---|---|---|
| 20 | 0.119 | 2.54 | 3.28 | 2.31 | 1.35 | 1.15 |
| 100 | 0.0001 | 7.62 | 3.40 | 2.04 | 1.34 | 1.14 |
| 1000 | $\approx 0$ | 33.7 | 3.02 | 2.00 | 1.33 | 1.14 |

At large $n$ the ratio approaches $c/(c-1)$ along $\kappa = cn/2$, which is the $\kappa/(\kappa - n/2)$ factor. The crossover from overestimate to underestimate sits at the mean-square threshold, so the asymptotic is anti-conservative exactly where a reader is most likely to apply it: near the condition canon already states.

**A rigorous replacement** (my derivation; checked numerically below). For $2\kappa \gt n-1$ and any $s \in (0,\kappa)$, with $P(\cdot,\cdot)$ the regularized lower incomplete gamma,

$$\Phi(0) \;\geq\; \frac{\Gamma(n/2)}{2\alpha}\,\kappa^{-n/2}e^{\kappa}\cdot P\big(\tfrac n2, s\big)\cdot\frac{2\kappa}{2\kappa - n + 1}\cdot\Big(1 - \big(\tfrac{\kappa}{s}\big)^{(n-1)/2}e^{-(\kappa - s)}\Big).$$

*Derivation.* Put $s = \alpha a^2/\sigma_w^2$. Since $G$ is increasing, $\Phi(0) = \tfrac{2}{\sigma_w^2}\int_0^R G/m \geq \tfrac{2}{\sigma_w^2}G(a)\int_a^R e^{\varphi(u)}du$ with $\varphi(u) = \alpha u^2/\sigma_w^2 - (n-1)\log u$. Here $\varphi'$ is increasing, so $\varphi' \leq \varphi'(R) = (2\kappa - n + 1)/R$ on $[a,R]$, and $\int_a^R e^\varphi \geq (e^{\varphi(R)} - e^{\varphi(a)})/\varphi'(R)$. Substituting $G(a) = \tfrac12(\sigma_w^2/\alpha)^{n/2}\Gamma(\tfrac n2)P(\tfrac n2, s)$ gives the display.

So the sufficient tenure condition, valid at every $\kappa$ and $n$, is: the right side above $\geq L/\epsilon$ for some $s$. At $n = 1$ the bound reduces to $\Phi_{\text{asym}}P(\tfrac12,s)(1 - e^{s-\kappa})$. Ratio of this bound to the exact $\Phi(0)$, maximized over a grid of $s$:

| $n$ | values (at $\kappa$) |
|---|---|
| 2 | 0.62 (4), 0.87 (8), 0.96 (16) |
| 20 | 0.69 (20), 0.97 (40), 0.99 (80) |
| 1000 | 0.93 (600), 0.99 (750), 0.997 (1000) |

Every value is below 1, as required, and it approaches 1 as $\kappa$ grows. The same caution applies to the asymptotic in Corollary 3's display and in §8.1's hazard figure: usable as asymptotics, not as bounds.

## 3. Corollary 2.1's moment claim is false

"[Laplace-transform order] already implies all moment inequalities $\mathbb{E}\tau_R^k \geq \mathbb{E}^{\mathrm{OU}}\tau_R^k$." Laplace-transform order implies the first-moment inequality and not the higher ones. Counterexample: $X \equiv 1$, $Y$ uniform on $\{0,2\}$. Then $\mathbb{E}e^{-\lambda X} = e^{-\lambda} \leq \tfrac12(1 + e^{-2\lambda}) = \mathbb{E}e^{-\lambda Y}$ for every $\lambda$ (AM–GM), yet $\mathbb{E}X^2 = 1 \lt 2 = \mathbb{E}Y^2$. The moment ordering does hold under Theorem 2, which gives stochastic domination. With Theorem 2's second proof (§5 below), Theorem 2 needs nothing beyond Theorem 1's hypotheses. Corollary 2.1's stated reason to exist ("without the polarity fact") is gone, and its one false sentence should go with it. The Corollary is true but subsumed.

## 4. Strengthenings (mine, tiered; offered, not landed)

**S1. Adapted, time-varying, non-Markov drift — exact, same proofs.**

- *Statement.* Replace $F(\delta)$ by any predictable, locally bounded drift process $F_t$ with $\delta_t^\top F_t \geq \alpha\lVert\delta_t\rVert^2$ whenever $\lVert\delta_t\rVert \leq R$. Then Theorem 1 (lower bound), Corollary 2.1, Corollary 3 and Theorem 2 (second proof) hold verbatim, with $\mathbb{E}_x$ read as the law started at $\delta_0 = x$.
- *Why the proofs carry over.* Theorem 1's proof is Itô for $v(\delta_t)$ along an Itô process, and the generator inequality is pointwise in $(t,\omega)$. Ikeda–Watanabe's drifts are arbitrary well-measurable processes.
- *Why it matters for AAT.* Canon writes $F(\mathcal T,\delta)$, and tempo adapts (`#deriv-adaptive-gain-dynamics`). With A3, $\delta^\top F(\mathcal T_t,\delta) \geq \delta^\top F(\mathcal T_{\min},\delta)$, so the theorem covers adaptive-tempo and learning agents with $\alpha = \alpha(\mathcal T_{\min})$, provided the floor holds over the tempos visited. The spike fixes $\mathcal T$ (§0) and does not need to.
- *The upper-bound and equality clauses* carry over the same way with a ceiling $\bar\alpha$.

**S2. Corollary 3 dominates (iv) from every start, not only the origin — exact.**

- *Claim.* $1 - (\Phi(\lVert x\rVert) - L)/\Phi(0) \leq (\lVert x\rVert^2 + n\sigma_w^2L)/R^2$ for all $x$, $L$ and $\alpha \gt 0$.
- *The $L$ terms* compare by $\Phi(0) \geq R^2/(n\sigma_w^2)$, which the spike already proves.
- *The constant terms* need $\Phi(r)/\Phi(0) \geq 1 - r^2/R^2$, which is concavity of $\Phi$ in $s = r^2$. Indeed $d\Phi/ds = -\tfrac{1}{\sigma_w^2}\int_0^1 t^{n-1}e^{(\alpha r^2/\sigma_w^2)(1-t^2)}dt$, which is decreasing in $r$.
- *Limit case.* At $\alpha \to 0$ the two bounds coincide identically in $x$. Checked on a grid at $(\alpha,n) = (0.3,2), (2,2), (6,3), (10,10)$.
- *Consequence for the spike.* §5(ii) and the plan's reason to keep (iv) ("simpler dependence on a general start") stays true as a simplicity argument, but (iv) is never the tighter bound from any start.

**S3. Anisotropic noise at the correct exponent — my sketch, not independently checked.** This closes §8.2's "Open" at the level of a rigorous lower bound.

- *Setting.* $d\delta = -F\,dt + \Sigma^{1/2}dW$, constant $\Sigma \succ 0$ with extreme eigenvalues $\lambda_{\max}, \lambda_{\min}$.
- *The time change.* Write $\xi = \lVert\delta\rVert^2$. Then $d\xi = (\operatorname{tr}\Sigma - 2\delta^\top F)\,dt + 2\sqrt{\xi q_t}\,dB$, with $q_t = \hat\delta^\top\Sigma\hat\delta \in [\lambda_{\min},\lambda_{\max}]$. Change time by $A_t = \int_0^t q$. The process $\tilde\xi(s) = \xi(A^{-1}(s))$ has unit-type diffusion $2\sqrt{\tilde\xi}\,d\tilde B$ and drift $(\operatorname{tr}\Sigma - 2\delta^\top F)/q \leq n' - 2\alpha'\tilde\xi$, with $n' = \operatorname{tr}\Sigma/\lambda_{\min}$ and $\alpha' = \alpha/\lambda_{\max}$. This step uses $\delta^\top F \geq 0$.
- *Comparison.* Ikeda–Watanabe gives $\tilde\xi \leq$ the squared-radial OU of real dimension $n'$, rate $\alpha'$ and unit noise. Since $A_t \leq \lambda_{\max}t$, $\tau_R \geq S/\lambda_{\max}$ in law. Hence $\mathbb{E}_x\tau_R \geq \lambda_{\max}^{-1}\Phi_{\alpha/\lambda_{\max},\,n',\,1,\,R}(\lVert x\rVert)$. Lemma 1's ODE derivation holds verbatim for real $n' \gt 0$.
- *Exponent.* The exponent is $\alpha R^2/\lambda_{\max}$. It is tight for $F = \alpha\delta$, where the Freidlin–Wentzell quasi-potential is $\alpha y^\top\Sigma^{-1}y$ with minimum $\alpha R^2/\lambda_{\max}$ on the sphere. The isotropic case reduces exactly to Theorem 2.
- *Prefactor.* It is crude, because $n'$ grows with anisotropy. Monte Carlo at $\alpha = 2$, $R = 1$ gives a bound of $0.28$ against MC $2.09$ for $\Sigma = \operatorname{diag}(1, 0.25)$, and $2.40$ with an added rotation $8J\delta$. For $\Sigma = \operatorname{diag}(1, 0.5)$ the bound is $0.54$ against $1.61$ and $1.60$. The bound holds and is loose.
- *Before canon.* This wants a verifier before landing.

**S4.** The rigorous tenure condition in §2.

**S5.** The region-aware fixed-time tail in §1, built from (i′) and Corollary 3.

## 5. What I re-derived and found sound

- **Lemma 1.**
  - The integrating factor $m$, the formula, the incomplete-gamma form, $\Phi' \leq 0$, $\Phi'(0) = 0$, and $C^2$ (indeed analytic) regularity of $v$ at the origin all check.
  - My mpmath implementation (lower incomplete gamma, independent code) reproduces the spike's $\alpha\Phi(0)$ table at $\kappa = n/2$ to four digits ($0.5957, 0.6590, 0.7064, 0.7767, 0.8885, 1.0157, 1.2018$).
- **Lemma 1′** (fixed $n$). The endpoint evaluation and the $\Gamma(n/2)$ prefactor are right. The next term is $n/(2\kappa)$, matching the scan, and it is the first term of $\kappa/(\kappa - n/2)$ (§2).
- **Theorem 1.**
  - Signs: $-\Phi' \geq 0$ and A2′ give $\mathcal L v \geq \mathcal L_{\mathrm{OU}}\Phi = -1$, and the upper bound follows symmetrically with $\bar\alpha$.
  - At $\delta = 0$ no continuity of $F$ is needed, because $F(0) = 0$ and $\nabla v(0) = 0$ directly.
  - The $t \to \infty$ passage in the lower-bound direction assumes nothing about $\mathbb{E}\tau_R \lt \infty$.
  - The equality clause covers every radially tight $F$, including nonlinear tangential parts.
- **Radial-profile generalization.** It is correct, and $v = \Phi_g\circ\lVert\cdot\rVert$ stays $C^2$ at the origin for continuous $g$ with $g(0) = 0$.
- **Theorem 2, proof 1** ($n \geq 2$). The first-exceedance argument on the absolutely continuous $D$ is sound, and strict monotonicity of $b_\alpha$ is what replaces the continuity hypothesis Li–Zhang need, as the scan asked.
- **Theorem 2, proof 2** (Ikeda–Watanabe on $\lVert\delta\rVert^2$).
  - Under the scan's transcription of Thm 1.1 and Remark 1.1 the application is correct. The common diffusion coefficient $2\sigma_w\sqrt{\xi^+}$ satisfies Yamada's condition, and the affine $b$ gives pathwise uniqueness.
  - **The scan's open "well-measurable" item discharges:** $\beta_1(t) = n\sigma_w^2 - 2\delta_t^\top F(\delta_t)$ is a Borel function of a continuous adapted process. It is therefore predictable, hence optional, which is to say well-measurable. Under S1's adapted drift, require $F_t$ predictable.
- **Corollary 3** and §5(ii) hold (the $\alpha \to 0$ Brownian limit is right), and both are extended by S2.
- **§7 and the scan's §10.2.** The deterministic barrier bound holds. From $\tfrac12\lvert u\rvert^2 \geq \tfrac{d}{dt}(\alpha\lvert\varphi\rvert^2)$ with $u = \dot\varphi + F(\varphi)$, which is $\tfrac12\lvert u - 2\alpha\varphi\rvert^2 \geq 0$ plus A2′, the action to reach the sphere is at least $\alpha R^2$.
- **Regression axis (spikes SOP §2a).** The axis is clean. The exclusion pickaxes `git log -S` for Kramers, Freidlin, Arrhenius, "mean exit", and $e^{\kappa}$ over `*/src/*` are empty. "exit time" appears only in the definition of $\tau_R$ (commits `80b40d28`, `716ea89a`). No exit-time claim was ever landed and corrected away, so landing this one cannot be a restoration. The regression this pass *did* find is §1's, and it runs the other way: a corrected-away object survives implicitly inside a sibling claim.

## 6. Smaller items

1. **Corollary 4 overreads for non-tight agents.** "An agent that satisfies $\alpha \gt n\sigma_w^2/(2R^2)$ with no margin typically leaves its certified region within one correction time." This is the benchmark's behavior. A non-tight agent's tenure can be far longer: the dip instance is $3.8\times$ the benchmark, and only the ceiling $\bar\alpha$ bounds it above. The licensed statement concerns the guarantee: the mean-square condition *certifies* no more than about one correction time of expected tenure. The same overreach is in the debrief ("an agent meeting the condition … typically leaves") and in the C1 brief text it inherited.
2. **Corollary 4 along $n$.** $\alpha\Phi(0)$ at $\kappa = n/2$ is not bounded in $n$; it drifts like $\tfrac14\ln n$.

   | $n$ | 100 | 300 | $10^3$ | $3\cdot10^3$ | $10^4$ |
   |---|---|---|---|---|---|
   | $\alpha\Phi(0)$ | 1.353 | 1.604 | 1.890 | 2.157 | 2.453 |
   | $\alpha\Phi(0) - \tfrac14\ln n$ | 0.201 | 0.178 | 0.163 | 0.155 | 0.150 |

   A mechanism, offered as a conjecture: from the origin at $\kappa = n/2$, $\mathbb{E}\lVert Y_t\rVert^2 = R^2(1-e^{-2\alpha t})$ approaches $R^2$ only exponentially, while the fluctuation of $\lVert Y_t\rVert^2$ is about $R^2\sqrt{2/n}$. Exit happens when the deficit meets the fluctuation, at $\alpha t \approx \tfrac14\ln(n/2)$. This also explains why the spike's withdrawn "concentration on the sphere" mechanism predicted the wrong sign. The qualitative point survives (a few correction times at any practical $n$), but "order one in every dimension" should be bounded to the tested $n$ or carry the logarithm. A related exact fact may be worth a line: at $\kappa = n/2$ the benchmark's stationary law puts $P(\chi^2_n \gt n)$ of its mass outside $\mathcal B_R$. That is $0.32$ at $n = 1$, rising toward $1/2$, since $P(\chi^2_n \leq n) = 0.683, 0.632, 0.584, 0.519, 0.506$ at $n = 1, 2, 5, 100, 1000$.
3. **The noise convention moves $n$ into the exponent.** "The exponent is dimension-free; the dimension enters the prefactor" holds in the per-coordinate convention the spike adopts. Under GA-2S as canon writes it ($\mathbb{E}\lVert w\rVert^2 = \sigma_w^2$, total), $\kappa = n\alpha R^2/\sigma_w^2$. The invariant reading is barrier over per-degree-of-freedom temperature. The spike flags the convention as pre-existing; my addition is that the convention must be settled *before* any formula reaches the front door (`INTRODUCTION.md:27` per the plan), because the headline exponent's $n$-dependence flips with it.
4. **§8.1 states a "hazard" bound the spike says it does not have (§8.6).** "first-exit hazard is at most of order $1/\Phi(0)$" is not proved for general $F$. What is proved is an averaged-rate statement from the origin, $P_0(\tau_R \leq L) \leq L/\Phi(0)$. The plan repeats the hazard wording for `#sketch-structural-adaptation-genericity`.
5. **Minor rigor in Theorem 2's last step.** Theorem 2 concludes "therefore $\tau_R(\delta) \geq \tau_R(\varrho)$ pathwise" from $r \leq \varrho$ on $[0,\tau_R(\delta)]$. The touching case $\varrho(\tau_R(\delta)) = R$ needs one sentence: strong Markov at that stopping time plus regularity of the boundary for the non-degenerate benchmark. Then $\varrho$ exceeds $R$ immediately a.s. The same sentence serves proof 2.
6. **§3, the radial-profile remark.** "in one dimension, exactly $\int_0^R F$" is right for odd $F$. For non-symmetric $F$, exit from $(-R,R)$ involves both sides, and the profile bound uses $g(r) = \min(F(r), -F(-r))$.
7. **Stale text.** These are the items the integrator reads first.
   - `proposed-integration-plan.md` item 7 still says "$\alpha\Phi(0) \lt 1$ … decreasing in $n$" and offers the withdrawn concentration mechanism. This directly contradicts `04-numerics.md` §2 (1.02 at $n=20$, 1.20 at $n=50$, increasing), and it is the highest-damage stale line.
   - Plan item 6 offers Corollary 2.1 as the fallback that proof 2 has superseded.
   - Plan item 3 says the $n \geq 2$ benchmark is "checked only numerically", but Kersting et al. is now cited.
   - Theorem 2's tier line still lists the polarity hypothesis that proof 2 removes.
   - `debrief.md` lists `02-literature.md` as "scan, in progress".
   - `checks-output.txt` and `checks-output-partial.txt` are byte-identical (`diff` empty); the README and derivation header name different ones.
8. **Adjacent canon sentence.** `#deriv-stochastic-non-exit` :44: "that condition places the RMS radius … well inside $\mathcal B_R$, so $V \ll \tfrac{n\sigma_w^2}{4\alpha}$ typically." The condition is only $R^\ast_S \lt R$, not "well inside". And $\tfrac{n\sigma_w^2}{4\alpha}$ is exactly the OU stationary mean of $V$, so $V$ is typically comparable to it, not much smaller: $P(V \lt \tfrac{n\sigma_w^2}{4\alpha}) = P(\chi^2_n \lt n) \in (0.5, 0.69)$. The no-go needs only positive probability of that event, so the demonstration stands and the sentence overstates.

## 7. Scope of this pass — the finding list, not its silence, is the content

- **Not done.** I did not open any primary source. Theorem 2 proof 2 and the well-measurable discharge rest on the scan's transcription of Ikeda–Watanabe. I read the $n=1$ Tanaka proof and found nothing wrong, but I did not re-derive it independently. I did not rerun the spike's `checks*.py`, and I did not audit its adversarial drift implementations; my numbers come from independent scripts.
- **Partial.** `02-literature.md` was read in part. Discrete time and heavy tails are untouched. S3 is a sketch with two Monte Carlo sanity instances.
- **§1's cascade.** It is a grep plus reading three loci, not a full consumer audit. `#result-adversarial-exponent-regimes` in particular is unchecked.
- **vsect.** Asf's standing orders say a broken check is recorded in `vsect`. I have **not** recorded anything, because the brief asked for exactly one committed file and vsect writes event files into the shared tree. I would record `vsect take --check segment:deriv-sector-condition --criterion "Prop A.1S(i) stopped second-moment bound, for all t" --outcome broken` (ground: counterexample, §1), plus a `vsect ask` on `segment:result-contraction-template`, if the coordinator wants those events left uncommitted for them.

## 8. Feedback on the spike as a piece of work, and on the brief

The spike was easy to verify, and that is to its credit. Every statement carries a tier, the plan orders checks by damage-if-wrong, the do-not-inherit list is accurate (I would add Corollary 4's agent-level sentence to it), and the corrections the author made along the way are recorded where a verifier needs them. The miss is in the neighborhood map. It read Prop A.1S as settled, and the very first consistency check it proposed ("any exit-time result must be consistent with it") would have caught (i), had (i) been tested against the spike's own Theorem 1 rather than assumed: the spike's Monte Carlo already shows $P(\tau_R \leq 2) = 0.91$ at $\kappa = 2$. For future spikes in this corpus, the transferable lesson is that the neighborhood map should re-derive, or at least sanity-check numerically, the canon statements a new result will sit beside, not only list them.

The bare brief worked. "Re-derive from what is written rather than from what you can tell was intended" is what sent me back into Prop A.1S's localization paragraph instead of accepting it as the spike's background.

I am staying on the line for follow-ups, including the vsect recording or a closer look at the §1 cascade if that is useful.
