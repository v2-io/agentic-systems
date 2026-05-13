---
slug: spike-reverse-kl-uniqueness
type: spike
status: promoted
date: 2026-04-22
---

# Spike: Reverse-KL Uniqueness Within the Direction-Forced Family

**Migration note.** The load-bearing math has been migrated to `#deriv-strategy-cost-regret-bound` §6.1 (new subsection: "Chain-rule uniqueness of reverse-KL") and the working note on family-characterization strengthening is marked resolved. This spike retains the strengthening-cycle reasoning trail only: which of Paths A–F were tried, which failed and why, which succeeded and under what axiom set.

**Charter.** Is there a set of structural axioms under which reverse-KL is *uniquely* the smooth f-divergence providing an upper regret bound $R(Q) \leq g(D(\pi^\ast \Vert Q))$ within the $\pi^\ast$-first family?

**Outcome: A (uniqueness theorem found).** Under the additional structural axiom of **chain-rule additivity over conditional factorizations** (Hobson 1969's composition/additivity axiom; Csiszár 1991 Theorem 5 composition-consistency characterization; standard functional-equation derivation), reverse-KL (equivalently, the I-divergence / KL-divergence) is the unique f-divergence among the direction-forced family. The axiom is independently motivated by AAD's decomposition of strategic plans into conditional sub-plans (DAG factorization), which should produce an additive rather than multiplicative cost-of-mismatch. Paths A, D, E, F fail (honestly; each explained); Path B narrows the family to alpha-divergences (Čencov/Morozova-Chentsov); Path C closes the uniqueness.

**Citation audit note (2026-04-22 evening, post-landing).** The load-bearing citations in §4 were corrected after a post-landing citation audit. Original draft cited Csiszár 1972 *Periodica Math. Hung.* 2:191–213 and Amari 2009 IEEE *Trans. Inf. Theory* 55(11):4925–4931 Theorem 1 as the source of the chain-rule uniqueness theorem; **both attributions were incorrect** (Csiszár 1972 is about f-informativity of observation channels, not chain-rule uniqueness; Amari 2009 proves $\alpha$-divergence uniqueness at f-div∩Bregman-div intersection, not chain-rule uniqueness; Amari & Cichocki 2010's claimed "Prop. 3.2" does not exist). The corrected citations are **Hobson 1969** (*J. Stat. Phys.* 1(3):383–391) for the canonical axiomatic uniqueness via additivity/composition, **Csiszár 1991** (*Ann. Statist.* 19:2032–2066, Theorem 3 corollary + Theorem 5 composition-consistency) for the projection-rule-level uniqueness of I-divergence, and **Shore & Johnson 1980** (*IEEE Trans. Info. Theory* 26:26–37) for system-independence axioms; the functional-equation derivation itself is folk (see also Aczél & Daróczy 1975 *On Measures of Information and Their Characterizations*, Academic Press). Additionally, **Eguchi 1983** was cited to *AISM* 35(1):1–24; the correct venue is ***Annals of Statistics*** 11(3):793–803. See §11 References for the corrected list.

## §1 — The Question Precisely

Fix the setting of `#deriv-strategy-cost-regret-bound`: $\pi^\ast = \delta_{a^\ast}$, $Q = Q_{\Sigma_t}$, bounded value range $V_{\max}$, strategy-induced regret $R(Q) := V(a^\ast) - \mathbb{E}_Q[V]$.

The F20 direction-forcing result: forward-KL $D_{\mathrm{KL}}(Q \Vert \pi^\ast) = +\infty$ under deterministic $\pi^\ast$ with off-optimum mass → a bound using forward-KL is vacuous. So the admissible family is $\{D_f(\pi^\ast \Vert Q) : f \text{ convex, } f(1) = 0, f \text{ smooth at } 1\}$. Within this $\pi^\ast$-first smooth-f-divergence family, the F20 table enumerates members:

- Reverse-KL ($f(t) = t \log t$) via Pinsker: $g(x) = V_{\max}\sqrt{x/2}$
- $\chi^2$ ($f(t) = (t-1)^2$) via Le Cam: $g(x) = V_{\max}\sqrt{x}/2$
- Bretagnolle-Huber-KL: $g(x) = V_{\max}\sqrt{1-e^{-x}}$
- Rényi-$\alpha$ for $\alpha \geq 1$: various

**Question.** Is there an axiom set under which reverse-KL is *uniquely* forced within this family?

## §2 — Path A (Fisher-metric second-order expansion). FAILS.

**Candidate axiom.** "Reverse-KL is the unique smooth f-divergence whose Hessian at $P = Q$ equals the Fisher information metric on the policy manifold."

**Why this fails.** This is exactly what **Eguchi's theorem** (Eguchi 1983, "Second order efficiency of minimum contrast estimators in a curved exponential family," *Annals of Statistics* 11(3):793–803; see also Amari & Cichocki 2010 Theorem 5 eq. (126) which credits Eguchi 1983 for the derivation) forbids.

**Eguchi's theorem (restated).** For any smooth f-divergence $D_f(P\Vert Q) = \int f(dP/dQ)\, dQ$ with $f''(1) \gt 0$, the Hessian at $P = Q$ equals $f''(1)$ times the Fisher information metric:

$$\left.\frac{\partial^2}{\partial\epsilon^2}\right\vert_{\epsilon=0} D_f(P_\epsilon \Vert Q) \;=\; f''(1) \cdot g_{ij}(Q) \cdot \dot\theta^i \dot\theta^j$$

where $P_\epsilon = Q$ at $\epsilon = 0$ and $g_{ij}$ is the Fisher matrix. (See also Amari & Nagaoka 2000, *Methods of Information Geometry*, §3.2; Amari 2016, *Information Geometry and Its Applications*, §4.1.)

**Consequence.** *Every* smooth f-divergence with $f''(1) \gt 0$ induces the Fisher metric at second order, up to the scalar factor $f''(1)$. For reverse-KL: $f(t) = t\log t$, $f''(1) = 1$. For $\chi^2$: $f(t) = (t-1)^2$, $f''(1) = 2$. For Bretagnolle-Huber, Rényi-$\alpha$ etc., the constant varies but the metric structure is identical up to scale.

Therefore "Fisher metric at second order" does *not* distinguish reverse-KL within the family. It distinguishes the f-divergence family as a whole from divergences like weighted-$L^2$ that do not induce a Fisher metric — but within the f-divergence family, the axiom is satisfied by every member.

**Verdict.** Path A fails, exactly as Joseph's prior predicted. The working note's candidate axiom is strictly insufficient.

**Secondary check: is there a second-order invariant that distinguishes reverse-KL?** The third-order term (the dual-connection skewness tensor, $T_{ijk}$ in Amari's notation) *does* distinguish f-divergences. Specifically: for the alpha-family $D_\alpha$, the third-order skewness depends on $\alpha$. Reverse-KL corresponds to $\alpha = 1$ (the exponential connection); $\chi^2$ to $\alpha = 3$; forward-KL to $\alpha = -1$. So "reverse-KL is the unique $\alpha = 1$ divergence" is a statement about a third-order geometric invariant — but this only restates which parameter value in the alpha-family we are picking; it does not pick out reverse-KL uniquely on independent grounds.

## §3 — Path B (Čencov/Chentsov sufficient-statistic invariance). NARROWS TO ALPHA-DIVERGENCES.

**Candidate axiom.** "Reverse-KL is the unique divergence invariant under sufficient-statistic coarse-grainings of the action space."

**Čencov's theorem (1982, *Statistical Decision Rules and Optimal Inference*, AMS Transl. Math. Monographs 53; extended by Campbell 1986, "An extended Čencov characterization of the information metric," Proc. AMS 98(1), 135–141).** On finite probability simplices, the Fisher information metric is the *unique* (up to positive scale) Riemannian metric invariant under Markov morphisms (sufficient-statistic coarse-grainings). This is a remarkable rigidity result: the Fisher metric is not a choice among many — it is forced by invariance.

**Extension to divergences: Morozova-Chentsov (1991) and Ay et al. 2017.** Morozova & Chentsov 1991 ("Markov invariant geometry on state manifolds," *Itogi Nauki i Tekhniki*, translated in J. Sov. Math. 56(5):2648–2669) extended the invariance program to divergences. Ay, Jost, Lê & Schwachhöfer 2017, *Information Geometry* (Springer), Chapters 2–4 — the modern reference — give the following characterization:

**Theorem (Morozova-Chentsov; Ay et al. 2017).** The family of divergences on probability simplices satisfying (a) non-negativity with $D(P\Vert P) = 0$, (b) smooth in the distribution arguments, (c) invariant under sufficient-statistic coarse-grainings (Markov morphisms), is exactly the class of **f-divergences** $D_f(P\Vert Q) = \sum_x Q(x) f(P(x)/Q(x))$ for convex $f$ with $f(1) = 0$.

**Secondary result (Amari 2009, "$\alpha$-divergence is unique, belonging to both $f$-divergence and Bregman divergence classes," IEEE Trans. Info. Theory 55(11):4925–4931).** Within the f-divergence family, the *alpha-divergences* $D_\alpha$ are the unique sub-family that is *also* a Bregman divergence (induced by a potential function on the exponential family). Reverse-KL is the $\alpha = 1$ alpha-divergence; $\chi^2$ is $\alpha = 3$; forward-KL is $\alpha = -1$; Hellinger-squared is $\alpha = 0$.

**Consequence for the uniqueness question.** Čencov + Morozova-Chentsov narrows the admissible family from "all smooth divergences" to "all f-divergences" — but this is already the family F20 was working with. It does not narrow within f-divergences.

Amari's alpha-family narrows further to the one-parameter alpha-family. But the $\pi^\ast$-first direction-forcing argument rules out $\alpha \leq 0$ (which correspond to forward-KL and Hellinger — vacuous under deterministic $\pi^\ast$; Hellinger is bounded, so gives a non-vacuous but weaker bound actually — needs separate check; see §7 edge case). For $\alpha \geq 1$ members, each gives a valid (non-vacuous) regret bound. The Bregman-+-f-divergence intersection axiom is satisfied by every alpha-divergence, not just reverse-KL.

**Verdict.** Path B narrows to alpha-divergences but not to reverse-KL specifically. An *additional* axiom is needed to pick $\alpha = 1$ out of $\{\alpha \geq 1\}$ (or out of the whole alpha-family, depending on how much the direction-forcing constrains).

## §4 — Path C (Chain-rule / conditional additivity). CLOSES UNIQUENESS.

**Candidate axiom (chain rule).** For any joint distribution $(X, Y)$:

$$D(P_{XY} \Vert Q_{XY}) \;=\; D(P_X \Vert Q_X) \;+\; \mathbb{E}_{P_X}\!\left[D(P_{Y\mid X} \Vert Q_{Y\mid X})\right]$$

This is the "additivity over conditional decomposition" property: the total mismatch between joint distributions equals the marginal mismatch plus the expected conditional mismatch.

**Theorem (KL uniqueness among f-divergences via chain rule).** The chain rule above holds for an f-divergence $D_f$ (on arbitrary joint distributions) *if and only if* $f(t) = c \cdot t\log t$ for some constant $c \gt 0$ — i.e., $D_f$ is reverse-KL (up to positive scaling).

**Status of the theorem and its references.** The theorem itself is a classical folk result in information theory, obtainable by a direct functional-equation argument (below). The canonical published sources for the axiomatic characterizations *equivalent to* the chain-rule statement are:

- **Hobson 1969**, "A new theorem of information theory," *Journal of Statistical Physics* 1(3):383–391 — the closest direct match. Hobson proves that the Kullback expression $I = k\sum p_i \log(p_i / p_i^0)$ is the unique measure satisfying four conditions, one of which is a *composition/additivity property*: information about subdivided events equals information about the coarse partition plus the conditional-expectation of information about the subdivisions. This is exactly the chain-rule axiom in the form used above.
- **Csiszár 1991**, "Why least squares and maximum entropy? An axiomatic approach to inference for linear inverse problems," *Annals of Statistics* 19:2032–2066 — Theorem 3 corollary: "The only transitive statistical projection rule (on $R_+^n$ or $\Delta_n$) is the I-divergence projection rule." Theorem 5(ii): product-consistency selects I-divergence uniquely. These are the projection-rule-level statements of the chain-rule / additivity uniqueness for KL.
- **Shore & Johnson 1980**, "Axiomatic derivation of the principle of maximum entropy and the principle of minimum cross-entropy," *IEEE Trans. Info. Theory* 26:26–37 — system-independence axiom (stronger than Csiszár 1991's product-consistency) uniquely characterizes cross-entropy / I-divergence minimization.
- **Aczél & Daróczy 1975**, *On Measures of Information and Their Characterizations*, Academic Press — comprehensive treatment of functional-equation arguments for characterizing information measures.

**Proof sketch (standard functional-equation argument).** The chain rule for $D_f(P_{XY}\Vert Q_{XY}) = \sum_{x,y} Q(x,y) f(P(x,y)/Q(x,y))$. Decompose $P(x,y) = P(x)P(y\mid x)$ and $Q(x,y) = Q(x)Q(y\mid x)$. Let $r_x = P(x)/Q(x)$ and $s_{y\mid x} = P(y\mid x)/Q(y\mid x)$. Then $P(x,y)/Q(x,y) = r_x \cdot s_{y\mid x}$ and:

$$D_f(P_{XY}\Vert Q_{XY}) = \sum_x Q(x) \sum_y Q(y\mid x) f(r_x s_{y\mid x})$$

For the chain rule to hold as an identity in $\{r_x, s_{y\mid x}\}$:

$$\sum_x Q(x) \sum_y Q(y\mid x) f(r_x s_{y\mid x}) = \sum_x Q(x) f(r_x) + \sum_x P(x) \sum_y Q(y\mid x) f(s_{y\mid x})$$

Fix $x$ and consider the inner sums. The identity must hold for all $Q(y\mid x)$-profiles and all $r_x, s_{y\mid x}$. Taking $Q(y\mid x) = \delta_{y_0}$ degenerate (point-mass on some $y_0$), the inner sum degenerates. Considering instead full-support $Q(y\mid x)$ and varying $s_{y\mid x}$ independently at each $y$, the identity implies:

$$f(r s) = f(r) + r f(s) + g(r)$$

for some function $g$, where the equation holds for all $r, s \gt 0$. This functional equation has solution $f(t) = c \cdot t \log t + h(t-1)$ for linear $h$, and the normalization $f(1) = 0$ with convexity forces $h = 0$, leaving $f(t) = c \cdot t\log t$. QED. (See Aczél & Daróczy 1975 §4 for the general functional-equation machinery; Hobson 1969 for the specific KL characterization via this argument.)

**Why other f-divergences fail the chain rule (quick checks):**

- **$\chi^2$.** $f(t) = (t-1)^2$, so $\chi^2(P\Vert Q) = \sum_x (P(x)-Q(x))^2/Q(x)$. Concrete counterexample on a $2\times 2$ joint: take $Q_X$ uniform on $\{x_1, x_2\}$, $P_X = (3/4, 1/4)$, $Q(y\mid x)$ uniform for both $x$, and $P(y\mid x) = (3/4, 1/4)$ for both $x$ (same conditional shape). Then $P(x,y) = P(x)P(y\mid x)$ has ratios $r_{xy} \in \{9/4, 3/4, 3/4, 1/4\}$ against uniform $Q(x,y) = 1/4$. LHS: $\chi^2(P_{XY}\Vert Q_{XY}) = \frac{1}{4}\bigl[(5/4)^2 + (1/4)^2 + (1/4)^2 + (3/4)^2\bigr] = 36/64 = 9/16$. RHS: $\chi^2(P_X\Vert Q_X) = 1/4$; $E_{P_X}[\chi^2(P_{Y\mid X}\Vert Q_{Y\mid X})] = 1/4$ (same conditional for each $x$, and each contributes $1/4$); so RHS = $1/4 + 1/4 = 8/16$. Chain rule fails: $9/16 \neq 8/16$.

- **Bretagnolle-Huber-KL (the bound $1-e^{-D_{KL}}$).** This is a *different* functional on top of KL, not a separate f-divergence — it is $1 - e^{-D_{KL}(P\Vert Q)}$. The underlying divergence is still KL, which satisfies the chain rule; the BH transformation does not. If we ask whether the composite $\phi(D_{KL})$ for $\phi(x) = 1 - e^{-x}$ is itself an f-divergence, the answer is no — it is a $\phi$-transform of one.

- **Rényi-$\alpha$ for $\alpha \neq 1$.** $D_\alpha(P\Vert Q) = \frac{1}{\alpha - 1}\log\sum_x Q(x)^{1-\alpha}P(x)^\alpha$. Rényi-$\alpha$ is an f-divergence only in a weakened sense (it's a monotone transform of an f-divergence for $\alpha \gt 0$; see Liese & Vajda 2006). It satisfies a *weaker* pseudo-additivity: $D_\alpha(P_{XY}\Vert Q_{XY}) \neq D_\alpha(P_X\Vert Q_X) + E_{P_X}[D_\alpha(P_{Y\mid X}\Vert Q_{Y\mid X})]$ in general; it satisfies the additivity only for *independent* joints and only as $\alpha \to 1$. Rényi fails the chain rule for general conditional decompositions.

**Verdict.** **Path C closes the uniqueness.** The chain-rule axiom, combined with the direction-forcing (which rules out forward-KL), picks out reverse-KL as the unique smooth f-divergence in the $\pi^\ast$-first family.

## §5 — AAD-Internal Motivation for the Chain-Rule Axiom

The uniqueness theorem of §4 is a pure mathematical result. For it to land as a segment update (not merely a technical aside), the chain-rule axiom must be *AAD-internally motivated* — the chain rule must correspond to something AAD cares about structurally.

**The motivation.** AAD's strategy is a **probabilistic causal DAG** ( #def-strategy-dag). The DAG decomposes into a joint over (action chains, conditional sub-plan outcomes, final-action distributions). The DAG's factorization is *compositional*: a plan $\Sigma_t$ decomposes into a sequence of sub-plans $(\Sigma_t^{(1)}, \Sigma_t^{(2)}, \ldots)$ at different causal layers, with each sub-plan carrying conditional structure.

The natural question AAD asks of a mismatch functional is: **does the total mismatch between $\pi^\ast$ and $Q_{\Sigma_t}$ decompose additively over the DAG's causal layers?** If yes, then the per-layer mismatch is a well-defined local quantity, and the total is the sum of layer-mismatches weighted by layer-accessibility.

This is *exactly* the chain-rule axiom applied to the DAG factorization. Specifically:

**Claim (chain rule is AAD-structurally natural).** For a DAG-factorized strategy $Q_{\Sigma_t}(a_{1:T}) = \prod_{t=1}^T Q(a_t \mid a_{\lt t})$, the mismatch functional should satisfy:

$$D(\pi^\ast \Vert Q_{\Sigma_t}) \;=\; \sum_{t=1}^T \mathbb{E}_{\pi^\ast}\!\left[D(\pi^\ast(\cdot\mid a_{\lt t}^\ast) \Vert Q(\cdot\mid a_{\lt t}^\ast))\right]$$

Under deterministic $\pi^\ast = \delta_{a_{1:T}^\ast}$, this collapses to a sum of per-step KL terms along the optimal trajectory — *additive cost-of-mismatch across causal layers*.

**Non-chain-rule divergences (e.g., $\chi^2$) would give non-additive decompositions.** For $\chi^2$, the total mismatch $\chi^2(P_{XY}\Vert Q_{XY}) \neq \chi^2(P_X\Vert Q_X) + E_{P_X}[\chi^2(P_{Y\mid X}\Vert Q_{Y\mid X})]$; the total is super-additive (cross-layer terms amplify each other). Operationally: a mismatch at layer 1 and a mismatch at layer 2 interact multiplicatively rather than combining independently. This is **structurally discordant with the DAG factorization** AAD already committed to in `#def-strategy-dag` and `#der-chain-confidence-decay`.

**The parallel to #der-chain-confidence-decay.** AAD's #der-chain-confidence-decay segment already commits to *additive log-confidence decay* along causal chains (multiplicative confidence in linear space becomes additive in log space). The chain-rule-for-divergence axiom is the natural analog for mismatch: **additive mismatch decay along causal chains.** Reverse-KL is the unique f-divergence making this work.

**Verdict.** The chain-rule axiom is not arbitrary — it is the divergence-level version of the additive-decomposition principle AAD already relies on for confidence decay. Adopting it forces reverse-KL; rejecting it is equivalent to adopting a super-additive or sub-additive decomposition, which AAD has already rejected elsewhere.

## §6 — Paths D, E, F (the remaining candidates). None independently close uniqueness.

**Path D (Variational / ELBO decomposition).** Reverse-KL is the divergence used in the ELBO decomposition $\log Z - D_{KL}(Q\Vert P_{\text{target}}) = E_Q[\log p(X, z)] - E_Q[\log Q(z)]$. This is a real result (Jordan et al. 1999, "An introduction to variational methods for graphical models," *Machine Learning* 37(2):183–233; Blei et al. 2017, "Variational inference: A review for statisticians," *JASA* 112(518):859–877) but the ELBO's role is in the *learning* of $Q$ to approximate $P$, not in bounding regret. The ELBO-reverse-KL connection is the `#form-strategy-complexity-cost` variational motivation (already in the segment); it is *convergent evidence* that reverse-KL is natural in the variational-inference frame, not an independent uniqueness argument. The ELBO decomposition uses KL's chain rule as a sub-step, so the logical priority is: chain rule → reverse-KL → ELBO decomposition, not the reverse.

**Verdict.** Path D reduces to Path C.

**Path E (Sanov large-deviations).** Sanov's theorem (Cover & Thomas 2006 §11.4; Dembo & Zeitouni 2010, *Large Deviations Techniques and Applications*, Springer, Theorem 2.1.10) states that for i.i.d. samples from $Q$, the empirical measure $\hat P_n$ concentrates on $P$ at exponential rate $D_{KL}(P\Vert Q)$:

$$-\frac{1}{n}\log \mathbb{P}_Q[\hat P_n \approx P] \;\to\; D_{KL}(P\Vert Q) \qquad\text{as } n\to\infty$$

The rate function is reverse-KL (with $P$ as the empirical target, $Q$ as the sampling distribution). If we ask: "at what exponential rate does a strategy sampling from $Q_{\Sigma_t}$ produce trajectories that concentrate on $\pi^\ast$?" — the answer involves $D_{KL}(\pi^\ast\Vert Q_{\Sigma_t})$. This is the **Sanov rate function for the question AAD cares about**.

However: Sanov gives a *rate-function identification* at the asymptotic-large-sample limit, not a *regret bound*. The rate function is reverse-KL because $P$ (the target of concentration) appears first in the rate. This is direction-consistent with F20 but adds no new structural content beyond what F20 already established. More importantly, Sanov's uniqueness of the rate function is an *asymptotic-sample* statement; the regret-bound question is a *single-distribution* statement. The two questions are related but not identical.

**Verdict.** Path E gives further convergent evidence (the same direction is natural under large-deviation analysis), but no new uniqueness argument. At most, it could motivate: "among smooth direction-forced divergences, reverse-KL is the unique one that *equals its own large-deviation rate function*." This is a genuine result but is equivalent to Path C via Sanov ↔ KL correspondence.

**Path F (Asymptotic tightness).** In the small-$D$ limit ($D \to 0$), Pinsker and Bretagnolle-Huber agree to leading order: $\sqrt{1 - e^{-D}} \approx \sqrt{D}$ as $D\to 0$; Pinsker gives $\sqrt{D/2}$. So reverse-KL via Pinsker is *a factor of $\sqrt{2}$ looser than BH* in this limit, not uniquely tight. In the large-$D$ limit, BH is strictly tighter than Pinsker. No asymptotic regime makes reverse-KL uniquely tight within the smooth family.

**Verdict.** Path F does not close uniqueness. Reverse-KL is not asymptotically tightest; TV is always tight, BH is tight at large $D$, and Pinsker is loose by $\sqrt{\cdot}$ at all scales within $[0, \infty)$.

## §7 — Edge cases and caveats on the uniqueness theorem

**(a) Scope: deterministic $\pi^\ast$.** The direction-forcing argument uses $\pi^\ast = \delta_{a^\ast}$. For stochastic $\pi^\ast$ (tied-optima, softmax-smoothed), forward-KL can become finite but the chain-rule axiom still picks out reverse-KL as the unique additive-decomposition divergence. The uniqueness theorem is scope-robust across F20's handled sub-cases (tied optima §9).

**(b) Hellinger and $\alpha = 0$.** Squared Hellinger distance $H^2(P, Q) = 2(1 - \sum_x\sqrt{P(x)Q(x)})$ is symmetric, bounded, and finite under deterministic $\pi^\ast$ (unlike forward-KL). Hellinger is the $\alpha = 0$ member of the alpha-family. Does Hellinger escape the direction-forcing and give a non-vacuous bound? Yes — Hellinger-squared is finite under deterministic $\pi^\ast$: $H^2(\delta_{a^\ast}, Q) = 2(1 - \sqrt{Q(a^\ast)}) \in [0, 2]$. Le Cam's inequality gives $\operatorname{TV} \leq H\sqrt{2 - H^2/2}$ → $R \leq V_{\max} \cdot H\sqrt{2 - H^2/2}$. So Hellinger would also be a non-vacuous bound. But Hellinger *fails the chain rule* (in the $\alpha = 0$ direction; the symmetric-positive-f ancestor is $f(t) = (\sqrt t - 1)^2$ which does not satisfy the additive chain rule). So the chain-rule axiom rules Hellinger out, and the uniqueness holds.

**(c) Composite divergences (e.g., Jensen-Shannon).** JSD is symmetrized KL: $\operatorname{JSD}(P, Q) = \frac{1}{2}D_{KL}(P\Vert M) + \frac{1}{2}D_{KL}(Q\Vert M)$ with $M = (P+Q)/2$. JSD is bounded, finite under deterministic $\pi^\ast$ (since $M$ has full support whenever $Q$ does), and arguably natural for two-distribution comparison. JSD also fails the chain rule: the symmetrization and the midpoint-mixing both break additive decomposability. So JSD is ruled out by the chain-rule axiom, consistent with the uniqueness theorem.

**(d) Asymmetry.** The chain rule as stated has $\mathbb{E}_{P_X}[\cdot]$ (expectation over the *first-argument marginal*). This is the asymmetric form. A symmetric chain rule would fix a stronger constraint but reverse-KL satisfies only the asymmetric form (the $P$-first form). Forward-KL satisfies the symmetric form only if we write the chain rule with $E_{Q_X}$ — so the chain rule is direction-sensitive. Under $\pi^\ast$-first direction (forced by regret-vacuity), the chain-rule axiom picks reverse-KL; under $Q$-first direction, it would pick forward-KL. The combination of direction-forcing (F20 §5) + chain rule (this spike §4) closes the uniqueness.

**(e) Continuous action spaces.** The uniqueness theorem references $\sum_x$ and $\int$; the chain rule holds for both discrete and continuous conditional decompositions (Amari & Nagaoka 2000 §3.5 discusses the continuous case; no new subtleties). AAD's action space is generally discrete at the proposition level; the theorem applies directly.

## §8 — Outcome Declaration

**Outcome A.** Under the additional structural axiom of **chain-rule additivity over conditional factorizations** (Hobson 1969; Csiszár 1991 Theorem 3 corollary and Theorem 5; standard functional-equation derivation per Aczél & Daróczy 1975), reverse-KL is the **unique** smooth f-divergence in the $\pi^\ast$-first direction-forced family providing an upper regret bound.

The axiom is independently motivated by AAD's DAG factorization of strategies ( #def-strategy-dag) and by the parallel with additive log-confidence decay ( #der-chain-confidence-decay). It is the divergence-level analog of additive-mismatch-decomposition-along-causal-chains, a principle AAD has already committed to.

**Within the strengthened axiom set**, the "Reverse-KL canonical among smooth divergences" row in `#deriv-strategy-cost-regret-bound`'s derivation-audit table moves from *Formulation choice* to **Derived (conditional on chain-rule axiom)**.

**What the theorem does not do.** The uniqueness theorem holds *within the f-divergence family*. It does not rule out non-f-divergence choices (e.g., the BH-composite $1-e^{-D_{KL}}$, which is a monotone transform of reverse-KL and therefore equivalent for any downstream gradient-based optimization). It does not address the linear-vs-square-root form question (that's a formulation choice on top of the chosen divergence; §7 of `#deriv-strategy-cost-regret-bound` handles it).

## §9 — Segment update executed

1. **`#deriv-strategy-cost-regret-bound`** — added new subsection §6.1 "Chain-rule uniqueness of reverse-KL" with the Csiszár/Amari theorem, the AAD-internal motivation (chain-rule additivity parallel to `#der-chain-confidence-decay`), and the updated table row. Moved "Reverse-KL canonical among smooth divergences" in the derivation-audit table from "Formulation choice" to "Derived (conditional on chain-rule axiom)". Updated Working Notes: "Family characterization strengthening" marked resolved with pointer to §6.1. Left the untouched §6.2 (the four canonical-not-unique grounds) as background context — those grounds remain independently useful (gradient-tractability, VI-alignment, Fisher geometry, MDL coding) but are no longer load-bearing for uniqueness.

2. **`#disc-identifiability-floor`** — no update needed. This outcome is Outcome A (uniqueness found), not Outcome C (structural non-uniqueness, which would have been a new Instance 3). The identifiability-floor pattern is unchanged.

3. **OUTLINE.md** — no change to stage or title (the segment was already at draft; the addition is a sub-section strengthening).

## §10 — New research agenda items flagged

1. **Continuous-action chain-rule scope.** The uniqueness theorem cites Amari & Nagaoka for continuous-case chain-rule validity. AAD's strategy spaces are discrete; extending to continuous strategy DAGs (e.g., low-level control) would require re-verifying the chain-rule scope. Not urgent.

2. **BH-transform equivalence class.** The transform $\phi(D_{KL}) = 1 - e^{-D_{KL}}$ is a monotone function of reverse-KL; any monotone transform of reverse-KL is operationally equivalent for gradient-based optimization. The uniqueness-up-to-monotone-transform is a finer classification if downstream work needs it.

3. **Parallel chain-rule uniqueness results for Bregman divergences.** Amari 2009's theorem gives alpha-divergences as the intersection of f-divergences and Bregman divergences. Within Bregman, a separate chain-rule characterization could be derived; would it again pick reverse-KL (i.e., $\alpha = 1$)? Expected yes, by the same decomposability argument. Worth a brief check if AAD adopts a Bregman-divergence view elsewhere.

## §11 — References invoked

**Axiomatic uniqueness of KL / I-divergence** (load-bearing for §4 chain-rule uniqueness):
- Hobson, A. 1969. "A new theorem of information theory." *Journal of Statistical Physics* 1(3):383–391. *(Canonical source for KL uniqueness via composition/additivity axioms equivalent to the chain rule.)*
- Csiszár, I. 1991. "Why least squares and maximum entropy? An axiomatic approach to inference for linear inverse problems." *Annals of Statistics* 19(4):2032–2066. *(Theorem 3 corollary: transitive statistical projection rule is I-divergence uniquely; Theorem 5: product-consistency characterizes I-divergence.)*
- Shore, J. E. & Johnson, R. W. 1980. "Axiomatic derivation of the principle of maximum entropy and the principle of minimum cross-entropy." *IEEE Trans. Info. Theory* 26(1):26–37. *(System-independence axiom characterization.)*
- Aczél, J. & Daróczy, Z. 1975. *On Measures of Information and Their Characterizations.* Academic Press. *(Functional-equation machinery for characterizing information measures.)*

**Information geometry of f-divergences:**
- Eguchi, S. 1983. "Second order efficiency of minimum contrast estimators in a curved exponential family." *Annals of Statistics* 11(3):793–803. *(Fisher-metric-from-contrast-function derivation; see Amari & Cichocki 2010 Theorem 5 eq. (126) for the modern restatement.)*
- Čencov, N. N. 1982. *Statistical Decision Rules and Optimal Inference.* AMS Translations of Mathematical Monographs 53.
- Campbell, L. L. 1986. "An extended Čencov characterization of the information metric." *Proceedings of the AMS* 98(1):135–141.
- Morozova, E. A. & Chentsov, N. N. 1991. "Markov invariant geometry on state manifolds." (Russian, English translation in *J. Sov. Math.* 56(5):2648–2669.)
- Ay, N., Jost, J., Lê, H. V. & Schwachhöfer, L. 2017. *Information Geometry.* Springer (Ergebnisse der Mathematik 64).
- Amari, S. 2009. "$\alpha$-divergence is unique, belonging to both $f$-divergence and Bregman divergence classes." *IEEE Trans. Information Theory* 55(11):4925–4931. *($\alpha$-divergence uniqueness at f-div∩Bregman-div intersection; NOT the chain-rule uniqueness theorem.)*
- Amari, S. & Nagaoka, H. 2000. *Methods of Information Geometry.* AMS / Oxford University Press.
- Amari, S. 2016. *Information Geometry and Its Applications.* Springer Applied Mathematical Sciences 194.
- Amari, S. & Cichocki, A. 2010. "Information geometry of divergence functions." *Bulletin of the Polish Academy of Sciences: Technical Sciences* 58(1):183–195. *(Survey; Theorem 5: f-divergence induces Fisher metric uniquely via information monotonicity. Does NOT contain a "Prop 3.2" chain-rule theorem.)*
- Csiszár, I. 1972. "A class of measures of informativity of observation channels." *Periodica Mathematica Hungarica* 2:191–213. *(f-informativity of observation channels with data-processing theorem and f-radius/channel-capacity minimax result; NOT a chain-rule uniqueness theorem. Cited only for background on f-informativity framework.)*
- Liese, F. & Vajda, I. 2006. "On divergences and informations in statistics and information theory." *IEEE Trans. Info. Theory* 52(10):4394–4412.
- Sason, I. & Verdú, S. 2016. "f-divergence inequalities." *IEEE Trans. Info. Theory* 62(11):5973–6006.

**Other invoked results:**
- Cover, T. & Thomas, J. 2006. *Elements of Information Theory.* Wiley (2nd ed.).
- Dembo, A. & Zeitouni, O. 2010. *Large Deviations Techniques and Applications.* Springer (2nd ed.).
- Jordan, M. I., Ghahramani, Z., Jaakkola, T. S. & Saul, L. K. 1999. "An introduction to variational methods for graphical models." *Machine Learning* 37(2):183–233.
- Blei, D., Kucukelbir, A. & McAuliffe, J. D. 2017. "Variational inference: A review for statisticians." *JASA* 112(518):859–877.

## Working Notes

- **The chain-rule axiom is the tightest structural constraint I found.** Earlier axioms (Fisher-metric at second order, Čencov invariance) did not pick out reverse-KL. The chain rule *does* — it is the unique structural property of reverse-KL that no other direction-forced f-divergence shares. The result is robust.

- **Why I am confident the theorem is correct (post-audit).** The chain-rule / composition-additivity uniqueness of KL is a classical folk result obtainable by direct functional-equation argument (§4 sketch). The canonical published sources are **Hobson 1969** (composition-additivity axiom → KL uniquely) and **Csiszár 1991** (transitive statistical projection rule → I-divergence uniquely, Theorem 3 corollary; product-consistency → I-divergence, Theorem 5). The functional-equation machinery is in **Aczél & Daróczy 1975**. The $\chi^2$ counterexample in §4 ($9/16 \neq 8/16$) is a concrete arithmetic check; it is correct. I verified by hand.

- **Citation audit history (2026-04-22 evening).** On initial landing, the load-bearing citations here were **Csiszár 1972** *Periodica Math. Hung.* 2:191–213 and **Amari 2009** *IEEE Trans. Info. Theory* Theorem 1 and **Amari & Cichocki 2010** *Bull. Pol. Acad. Sci.* Prop 3.2. A post-landing citation audit (by careful reading of the actual papers) found that: (a) Csiszár 1972 is about f-informativity of observation channels and contains no chain-rule uniqueness theorem; (b) Amari 2009's main Theorem is about $\alpha$-divergence at f-div∩Bregman-div intersection, not about chain-rule uniqueness, and there is no "Theorem 1" labeled with that content (the paper's first numbered theorem is in §IV on $\alpha$-divergence); (c) Amari & Cichocki 2010 has no Prop 3.2 — its theorem numbering runs 1–12, and its f-divergence characterization (Theorem 3) uses information monotonicity, not chain rule. The attributions were wrong even though the theorem itself is correct. Corrected citations above. Additionally, Eguchi 1983 was cited to *AISM* 35(1):1–24; the correct venue is *Annals of Statistics* 11(3):793–803 (Amari & Cichocki 2010 reference [37] confirms this).

- **The axiom's AAD-internal motivation is the key load-bearing piece.** A pure Hobson-theorem uniqueness would be technically correct but unmotivated. The §5 argument — that the chain rule is the natural divergence-level analog of additive log-confidence decay, which AAD already commits to — is what makes the axiom a principled choice rather than an imported constraint. If Joseph pushes back on §5's motivation, the uniqueness theorem still holds but loses its AAD-groundedness.

- **What this does not resolve.** The linear-vs-square-root form choice in `#deriv-strategy-cost-regret-bound` §7 is orthogonal — the uniqueness result picks the divergence; the functional form around the divergence is a separate choice. Also, the choice between Pinsker and BH bounds on top of reverse-KL is not forced by the uniqueness theorem (both use reverse-KL; they differ in the bounding function $g$). The segment already handles these via the admissible-family table.
