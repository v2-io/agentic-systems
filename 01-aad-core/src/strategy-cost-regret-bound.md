---
slug: strategy-cost-regret-bound
type: derivation
status: robust-qualitative
depends:
  - strategy-complexity-cost
  - value-object
  - objective-functional
  - chain-confidence-decay
  - strategy-dag
stage: draft
---

# Derivation: Regret-Bound Derivation of the Strategy-Cost KL Direction

The variational form of the strategy-cost objective ( #strategy-complexity-cost) carries a $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ relevance term. This appendix derives that **the $\pi^\ast$-first KL direction is forced** as the non-vacuous regret-bound form, and proves (conditional on a chain-rule additivity axiom motivated by #chain-confidence-decay) that **reverse-KL is uniquely forced within the direction-forced f-divergence family**.

## Formal Expression

### §1 — Setup

Fix $O_t$, $M_t$, continuation policy $\pi_{\mathrm{cont}}$, and horizon $N_h$. The action-value is the objective-functional evaluation at $a$: $V(a) := Q_O(M_t, a; \pi_{\mathrm{cont}}, N_h)$ ( #value-object; $V$ derives from $O_t$ per #objective-functional). The optimal action is $a^\ast := \arg\max_a V(a)$; under AAD's canonical scope ( #value-object), the optimal policy $\pi^\ast(\cdot \mid M_t) = \delta_{a^\ast}$ is the point mass on $a^\ast$ (tied-optimum extensions §8). Write $V_{\max} := \max_a V(a) - \min_a V(a)$ for the value range at fixed $M_t$; this is finite whenever $\mathcal{A}$ is a bounded action set under $V$.

$Q_{\Sigma_t}(\cdot \mid M_t)$ is the action distribution induced by the strategy DAG. In general $Q_{\Sigma_t}$ is stochastic — the DAG's edge-credence uncertainty induces policy stochasticity downstream of propagation.

### §2 — Regret against the optimal policy

*[Definition (strategy-induced-regret)]*

The strategy-induced regret of $Q_{\Sigma_t}$ against $\pi^\ast$ is:

$$R(Q_{\Sigma_t}) \;:=\; V(a^\ast) \;-\; \mathbb{E}_{a \sim Q_{\Sigma_t}}[V(a)] \;=\; \sum_{a} Q_{\Sigma_t}(a) \cdot \bigl[V(a^\ast) - V(a)\bigr]$$

Writing $\Delta(a) := V(a^\ast) - V(a) \in [0, V_{\max}]$ for the per-action regret gap. Three regret forms in the literature:

$$\mathbb{E}_{\pi^\ast}[V] - \mathbb{E}_{Q_{\Sigma_t}}[V], \qquad V(a^\ast) - \mathbb{E}_{Q_{\Sigma_t}}[V], \qquad \mathbb{E}_{\pi^\ast}[V - V_{Q_{\Sigma_t}}]$$

coincide identically under deterministic $\pi^\ast$.

### §3 — Total-variation bound (tight)

*[Derived (tv-regret-bound, from bounded $V$ + deterministic $\pi^\ast$)]*

$$R(Q_{\Sigma_t}) \;=\; \sum_a Q_{\Sigma_t}(a)\,\Delta(a) \;\leq\; V_{\max} \cdot \sum_{a \neq a^\ast} Q_{\Sigma_t}(a) \;=\; V_{\max} \cdot (1 - Q_{\Sigma_t}(a^\ast))$$

For deterministic $\pi^\ast = \delta_{a^\ast}$:

$$\operatorname{TV}(\pi^\ast, Q_{\Sigma_t}) \;=\; \tfrac{1}{2}\sum_a \lvert \pi^\ast(a) - Q_{\Sigma_t}(a)\rvert \;=\; 1 - Q_{\Sigma_t}(a^\ast)$$

Therefore:

$$\boxed{\;R(Q_{\Sigma_t}) \;\leq\; V_{\max} \cdot \operatorname{TV}(\pi^\ast, Q_{\Sigma_t})\;} \qquad \text{(tight)}$$

**Tightness.** Equality holds exactly when $\Delta(a) = V_{\max}$ for all $a \neq a^\ast$ (degenerate value landscape: every suboptimal action incurs the full value range). For typical landscapes the bound is loose by a factor $\mathbb{E}_{Q_{\Sigma_t}}[\Delta \mid a \neq a^\ast]/V_{\max} \in (0, 1]$.

### §4 — Exact regret-reverse-KL identity under deterministic $\pi^\ast$

Under AAD's canonical scope (deterministic $\pi^\ast = \delta_{a^\ast}$), reverse-KL and total variation are related by an *identity*, not merely an inequality. This gives a tight two-sided regret bound that the Pinsker inequality strictly weakens.

*[Derived (bh-identity-deterministic, under deterministic $\pi^\ast$)]*

**Identity.** For deterministic $\pi^\ast = \delta_{a^\ast}$ and any $Q$ with $Q(a^\ast) \gt 0$:

$$\boxed{\;D_{\mathrm{KL}}(\pi^\ast \Vert Q) \;=\; -\log Q(a^\ast) \;=\; -\log\bigl(1 - \operatorname{TV}(\pi^\ast, Q)\bigr)\;}$$

*Derivation.* $D_{\mathrm{KL}}(\delta_{a^\ast} \Vert Q) = \sum_a \delta_{a^\ast}(a)\log(\delta_{a^\ast}(a)/Q(a)) = -\log Q(a^\ast)$ (only the $a = a^\ast$ term contributes; $0 \log 0$ terms are conventionally $0$). And $\operatorname{TV}(\delta_{a^\ast}, Q) = 1 - Q(a^\ast)$ (direct from §3). Substituting gives the identity. $\square$

This is the Bretagnolle-Huber inequality (Bretagnolle & Huber 1978, "Estimation des densités," *Séminaire de probabilités XII*, Springer LNM 649; Tsybakov 2009 §2.4; Sason & Verdú 2016) specialized to the deterministic-$P$ case, where the general inequality $\operatorname{TV} \leq \sqrt{1 - e^{-D_{\mathrm{KL}}}}$ becomes an equality.

*[Derived (exact-regret-reverse-kl, under deterministic $\pi^\ast$)]*

Combining with the tight TV-regret bound of §3:

$$\boxed{\;R(Q_{\Sigma_t}) \;\leq\; V_{\max} \cdot \bigl(1 - e^{-D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}\bigr)\;}$$

**Matching lower bound.** Define the action-gap $\Delta_{\min} := \min_{a \neq a^\ast} \Delta(a) \gt 0$ (standard in RL theory; well-defined whenever the optimum is isolated over finite $\mathcal A$ with bounded $V$). Then:

$$R(Q_{\Sigma_t}) \;=\; \sum_{a \neq a^\ast} Q_{\Sigma_t}(a)\,\Delta(a) \;\geq\; \Delta_{\min} \cdot \sum_{a \neq a^\ast} Q_{\Sigma_t}(a) \;=\; \Delta_{\min} \cdot \operatorname{TV}(\pi^\ast, Q_{\Sigma_t})$$

Under the exact BH identity:

$$R(Q_{\Sigma_t}) \;\geq\; \Delta_{\min} \cdot \bigl(1 - e^{-D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}\bigr)$$

*[Derived (matched-lower-bound, under deterministic $\pi^\ast$ + isolated optimum)]*

**Lipschitz-equivalence corollary.** Regret and $(1 - e^{-D_{\mathrm{KL}}})$ are Lipschitz-equivalent with constants $\Delta_{\min}$ (below) and $V_{\max}$ (above):

$$\frac{\Delta_{\min}}{V_{\max}} \;\leq\; \frac{R(Q_{\Sigma_t})}{V_{\max}(1 - e^{-D_{\mathrm{KL}}})} \;\leq\; 1$$

The upper bound is tight when the value landscape is extremal ($\Delta(a) = V_{\max}$ for all $a \neq a^\ast$); the lower bound is tight when sub-optimal actions are uniformly bad ($\Delta_{\min} = \max_{a \neq a^\ast} \Delta(a)$).

$D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) \in [0, +\infty)$: finite and graded whenever $Q_{\Sigma_t}(a^\ast) \gt 0$; diverges only in the structural-failure limit where the strategy places zero mass on the optimum.

#### §4.1 — Pinsker bound as loose general form

The Pinsker inequality $\operatorname{TV}(P, Q) \leq \sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(P \Vert Q)}$ (Tsybakov 2009 §2.4; Cover & Thomas 2006 §11.6) yields a regret bound that does not assume deterministic $\pi^\ast$:

$$R(Q_{\Sigma_t}) \;\leq\; V_{\max} \cdot \sqrt{\tfrac{1}{2}\,D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$$

**Under AAD's canonical scope, this is strictly weaker than the BH-identity form of §4.** For any $D_{\mathrm{KL}} \gt 0$: $1 - e^{-D_{\mathrm{KL}}} \lt \sqrt{D_{\mathrm{KL}}/2}$ for small $D_{\mathrm{KL}}$ (the BH form is linear in $D_{\mathrm{KL}}$ while Pinsker is $\sqrt{D_{\mathrm{KL}}}$), and Pinsker's $V_{\max}\sqrt{D_{\mathrm{KL}}/2}$ exceeds the trivial $V_{\max}$ bound once $D_{\mathrm{KL}} \gt 2$, giving vacuous content there. The BH identity is informative uniformly in $D_{\mathrm{KL}}$.

Pinsker remains the correct tool for stochastic-$\pi^\ast$ extensions (§9) where the deterministic-$\pi^\ast$ scope is relaxed and the BH identity degrades back to inequality.

### §5 — Direction-forcing claim (the load-bearing result)

*[Derived (kl-direction-forced, from deterministic $\pi^\ast$)]*

**Claim.** The KL direction with $\pi^\ast$ *first* is forced as the non-vacuous regret-bound form. Forward-KL $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast)$ is *not* a non-vacuous bound on $R(Q_{\Sigma_t})$ under deterministic $\pi^\ast$.

**Derivation.** Expanding:

$$D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast) \;=\; \sum_a Q_{\Sigma_t}(a) \log\!\bigl(Q_{\Sigma_t}(a)/\pi^\ast(a)\bigr)$$

For any $a \neq a^\ast$: $\pi^\ast(a) = 0$ (point mass assumption). The summand $Q_{\Sigma_t}(a)\log(Q_{\Sigma_t}(a)/0) = +\infty$ unless $Q_{\Sigma_t}(a) = 0$. Therefore $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast) = +\infty$ whenever $Q_{\Sigma_t}$ places any mass off $a^\ast$ — for *all but a measure-zero subset* of stochastic strategies. A bound "$R \leq +\infty$" is vacuous.

This is the same shape of degeneracy as the original Shannon-MI form (Gemini Finding 2) that the V-medium move was introduced to escape: same degeneracy-when-$\pi^\ast$-is-deterministic, different value ($0$ vs $+\infty$). Only the *reverse* direction escapes both.

**Alignment with the structural problem.** Forward-KL is natural for *mode-covering* inference (where $Q$ is asked to cover $P$'s full support) and variational inference when $Q$ is learned to match a full distribution. Reverse-KL is natural for *mode-seeking* (concentrate $Q$ on $P$'s mode). The AAD strategy problem is mode-seeking by construction: the strategy should concentrate on $a^\ast$. The direction alignment with the structural problem is not accidental.

**Asymmetry is forced by regret's one-sidedness.** A second, independent argument for asymmetry — one that does not rely on the chain-rule axiom of §6.1. Under deterministic $\pi^\ast$, regret is a *one-sided* quantity: $R(Q_{\Sigma_t}) = \sum_{a \neq a^\ast} Q_{\Sigma_t}(a)\Delta(a)$ contributes only from $Q_{\Sigma_t}$'s off-optimum mass; $\pi^\ast$'s "mass off $Q_{\Sigma_t}$" is vacuous since $\pi^\ast$ has no support off $a^\ast$. Any divergence whose role is to bound this quantity should therefore be asymmetric — it should penalize $Q_{\Sigma_t}$'s deviation from $\pi^\ast$ without symmetrically penalizing the (trivially zero) deviation of $\pi^\ast$ from $Q_{\Sigma_t}$. Symmetric divergences (squared Hellinger, Jensen-Shannon, symmetrized KL) treat the two deviations interchangeably; under the one-sided regret quantity this is operationally wrong — it introduces a term with no semantic role. The asymmetry requirement is thus *structural*, emerging directly from what regret is as a functional, and is established independently of the chain-rule axiom that picks the specific asymmetric form in §6.1. The two arguments compose: *direction-forcing* (vacuity under deterministic $\pi^\ast$) + *asymmetry-forcing* (regret is one-sided) ⇒ the admissible bounding divergence is $\pi^\ast$-first and asymmetric; chain-rule additivity (§6.1) then picks reverse-KL uniquely within that family.

**Terminology note (Bishop-vs-AAD "reverse-KL").** AAD's canonical reverse-KL is $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ — optimum-first, agent-second. Under Bishop 2006's convention ($D_{\mathrm{KL}}(q \Vert p)$ with $q$ the approximation is called "reverse-KL"), AAD's form would be labeled "forward-KL." The two naming conventions disagree in surface labeling but agree in the operational property — both pick out the *mode-seeking* direction (concentrate the approximation on the target's mode). Literature that uses the Bishop convention (variational inference, generative modeling, Levine 2018) and literature that uses the $\pi^\ast$-first / target-first convention (decision theory, regret analysis, Rubin-Shamir-Tishby 2012) describe the same operational quantity under deterministic $\pi^\ast$. When this segment writes "reverse-KL," the $\pi^\ast$-first / AAD convention is meant; under softened targets the two conventions describe different objects and must be disambiguated explicitly.

### §6 — Admissible-divergence family and uniqueness of reverse-KL

*[Discussion (admissible-regret-divergences)]*

The regret-bound argument forces the *direction* (the reference distribution $\pi^\ast$ appears first) but admits a family of divergences. Each member yields a valid regret bound; they differ in tightness and operational properties:

| Divergence | Bound on $R$ | Tightness | Finite under det. $\pi^\ast$? | Gradient-tractable? |
|---|---|---|---|---|
| $\operatorname{TV}(\pi^\ast, Q_{\Sigma_t})$ | $V_{\max}\cdot\operatorname{TV}$ | **Tight** (extremal $V$) | Yes | No (non-differentiable) |
| $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ via Pinsker | $V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}}$ | Loose by $\sqrt{\cdot}$ | Yes | Yes |
| $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ via Bretagnolle-Huber | $V_{\max}\sqrt{1 - e^{-D_{\mathrm{KL}}}}$ | Tighter than Pinsker for large $D_{\mathrm{KL}}$ | Yes | Yes |
| $\chi^2(\pi^\ast \Vert Q_{\Sigma_t})$ (Le Cam) | $V_{\max}\cdot\tfrac{1}{2}\sqrt{\chi^2}$ | Typically looser than Pinsker | Yes: $\chi^2 = 1/Q_{\Sigma_t}(a^\ast) - 1$ | Yes |
| $D_\alpha(\pi^\ast \Vert Q_{\Sigma_t})$ (Rényi, $\alpha \geq 1$) | Various | Interpolates KL ($\alpha\to 1$) and $\chi^2$ ($\alpha = 2$) | Yes for $\alpha \geq 1$ | Yes |
| $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast)$ (forward-KL) | $+\infty$ | Vacuous | **No** | — |

**What is uniquely forced by the regret-bound argument alone.** The direction: the reference $\pi^\ast$ is first. This is a real derivation outcome, not a selection. Within the $\pi^\ast$-first family, multiple f-divergences each give valid bounds; an additional structural axiom is required to pick one uniquely.

#### §6.1 — Chain-rule uniqueness theorem

*[Derived (reverse-kl-uniqueness, Conditional on chain-rule axiom)]*

**Theorem (chain-rule / additivity uniqueness of KL among f-divergences; folk theorem, standard functional-equation derivation).** *Let $D_f(P\Vert Q) = \sum_x Q(x) f(P(x)/Q(x))$ be a smooth f-divergence with $f$ convex and $f(1) = 0$. The chain rule*

$$D_f(P_{XY} \Vert Q_{XY}) \;=\; D_f(P_X \Vert Q_X) \;+\; \mathbb{E}_{P_X}\!\left[D_f(P_{Y\mid X} \Vert Q_{Y\mid X})\right]$$

*holds for all joint distributions $(X, Y)$ if and only if $f(t) = c \cdot t\log t$ for some $c \gt 0$ — i.e., $D_f$ is reverse-KL up to positive scaling.*

**References.** The theorem is a classical folk result obtainable by direct functional-equation argument (sketched below). The canonical published axiomatic characterizations equivalent to the chain-rule statement are: **Hobson 1969**, "A new theorem of information theory," *J. Stat. Phys.* 1(3):383–391 — uniqueness of the Kullback expression via a composition/additivity axiom; **Csiszár 1991**, "Why least squares and maximum entropy? An axiomatic approach to inference for linear inverse problems," *Annals of Statistics* 19(4):2032–2066 — Theorem 3 corollary: the only transitive statistical projection rule is the I-divergence projection rule; Theorem 5: product-consistency characterizes I-divergence uniquely. See also **Shore & Johnson 1980**, "Axiomatic derivation of the principle of maximum entropy and the principle of minimum cross-entropy," *IEEE Trans. Info. Theory* 26(1):26–37 (system-independence axiom); **Sanov 1957**, "On the probability of large deviations of random variables," *Mat. Sb.* 42(84):11–44 (large-deviation rate function for empirical-distribution concentration); **Aczél & Daróczy 1975**, *On Measures of Information and Their Characterizations* (Academic Press) for the general functional-equation machinery.

**These are not independent uniqueness routes.** Hobson's composition axiom, Csiszár's transitive-projection axiom, Shore-Johnson's system-independence axiom, and Sanov's sampling-consistency condition are *structurally-equivalent re-formulations* of the same underlying requirement — all factor through independence-of-sub-problems (joint inference on independent subsystems decomposes additively over factorizations). The Cauchy functional equation that each reduces to is the common structural content beneath varied surface formulations. This matters for `#discussion-additive-coordinate-forcing`: the chain-rule axiom's load-bearing role is not weakened by noting multiple canonical references; conversely, the multiple references do not provide multiple independent uniqueness arguments. No known uniqueness route outside the independence-on-sub-problems family exists.

**Proof sketch.** Write $r_x = P(x)/Q(x)$, $s_{y\mid x} = P(y\mid x)/Q(y\mid x)$. The chain-rule identity must hold for all joint decompositions, which forces the functional equation $f(r s) = f(r) + r f(s) + g(r)$ for all $r, s \gt 0$. Combined with $f(1) = 0$ and convexity, the unique solution is $f(t) = c \cdot t\log t$ for $c \gt 0$ (Aczél & Daróczy 1975 §4).

**Why other members of the family fail the chain rule.** Concrete counterexample for $\chi^2$: take $Q_X$ uniform on $\{x_1, x_2\}$, $P_X = (3/4, 1/4)$, $Q(y\mid x)$ uniform, $P(y\mid x) = (3/4, 1/4)$ for both $x$. Direct calculation gives $\chi^2(P_{XY}\Vert Q_{XY}) = 9/16$, while $\chi^2(P_X\Vert Q_X) + \mathbb{E}_{P_X}[\chi^2(P_{Y\mid X}\Vert Q_{Y\mid X})] = 1/4 + 1/4 = 8/16$. Non-additive: $9/16 \neq 8/16$. Rényi-$\alpha$ for $\alpha \neq 1$ fails analogously; Bretagnolle-Huber is a monotone transform of reverse-KL (not an independent f-divergence); Hellinger-squared ($\alpha = 0$) likewise fails.

**AAD-internal motivation for the chain-rule axiom.** The chain rule is the *divergence-level analog* of the additive log-confidence decay in `#chain-confidence-decay`. AAD has already committed to additive-mismatch-decomposition-along-causal-chains in that segment; the divergence-level parallel is:

$$D(\pi^\ast \Vert Q_{\Sigma_t}) \;=\; \sum_{t=1}^T \mathbb{E}_{\pi^\ast}\!\left[D\bigl(\pi^\ast(\cdot\mid a_{\lt t}^\ast) \,\big\Vert\, Q(\cdot\mid a_{\lt t}^\ast)\bigr)\right]$$

— total mismatch between $\pi^\ast$ and $Q_{\Sigma_t}$ decomposes additively over the DAG's causal layers along the optimal trajectory. Non-chain-rule divergences (e.g., $\chi^2$) give super-additive decompositions in which layer-mismatches amplify multiplicatively — structurally discordant with the DAG factorization ( #strategy-dag). Adopting the chain-rule axiom is therefore not arbitrary; it is the divergence-level version of a decomposition principle AAD already relies on.

**Corollary (within the chain-rule axiom).** Under deterministic $\pi^\ast$ + bounded value + chain-rule additivity, reverse-KL is the unique smooth f-divergence in the direction-forced admissible family. The "Reverse-KL canonical among smooth divergences" status upgrades from formulation choice (under the pre-axiom reading) to *Derived (conditional on the chain-rule axiom)*.

**What the uniqueness theorem does not do.** It fixes the divergence within the f-divergence family; it does not fix the bounding function $g$ around the divergence (Pinsker vs Bretagnolle-Huber vs Le Cam-on-$\chi^2$ are *different bounds using different divergences*, so only Pinsker and BH-on-KL remain in scope after uniqueness — and these differ only in the $g$-envelope on top of reverse-KL, not in the divergence itself). It does not resolve the linear-vs-square-root form question of §7 (that is a Lagrangian-shape choice orthogonal to the divergence choice). Monotone transforms of reverse-KL (e.g., $1 - e^{-D_{\mathrm{KL}}}$) are equivalence-class members for gradient-based optimization and are not ruled out.

**Scope of the axiom.** The chain rule is stated for arbitrary joint decompositions. AAD's strategy spaces are discrete at the proposition level; the theorem applies directly. For continuous strategy spaces (e.g., low-level control), the chain rule extends by replacing sums with integrals against the dominating measure; the functional-equation derivation is identical in the continuous case (see Liese & Vajda 1987, *Convex Statistical Distances*, Teubner, for the standard measure-theoretic treatment of f-divergences and their decomposition properties).

#### §6.2 — Secondary characterizations (now supporting rather than load-bearing)

Four additional properties further motivate reverse-KL as the canonical choice; under §6.1 they are no longer load-bearing for uniqueness but remain informative about why reverse-KL is a comfortable fit with the rest of the AAD framework:

1. **Gradient-tractability.** TV is non-differentiable at mass boundaries; reverse-KL is smooth. Operational minimization via gradient methods rules out TV despite its tightness — independent of the uniqueness argument.
2. **Variational-inference alignment.** Reverse-KL is the standard divergence in the variational-inference lineage (ELBO derivation uses reverse-KL; Friston et al. 2017; Da Costa et al. 2020). The V-medium move's rhetorical payoff — shared vocabulary with active inference — lives on reverse-KL specifically. This is *convergent evidence* that reverse-KL is natural in multiple frames, not an independent uniqueness argument (Path D in `msc/spike-reverse-kl-uniqueness.md` §6 shows the ELBO decomposition itself uses the chain rule as a sub-step; logical priority is chain rule → reverse-KL → ELBO).
3. **Fisher geometry.** Reverse-KL's second-order expansion gives the Fisher information metric (Amari & Nagaoka 2000). *But by the differential-geometric framework in Eguchi 1983* ("Second order efficiency of minimum contrast estimators in a curved exponential family," *Annals of Statistics* 11(3):793–803, §2 contrast-function development; modern restatement at Amari & Cichocki 2010 Theorem 5 eq. (126)), every smooth f-divergence with $f''(1) \gt 0$ induces the Fisher metric at second order up to the scalar $f''(1)$. Fisher-metric-at-second-order is *not* a distinguishing axiom within the f-divergence family — it is satisfied by every member. Noted here because it is a commonly-invoked distinguishing property; it does not distinguish. (Eguchi's Theorem 3 itself is about estimator efficiency via $\Gamma^1$-transversality; the f-divergence/Fisher-metric result is a consequence of the §2 contrast-function machinery that supports Theorem 3, not the theorem statement.)
4. **Information-budget / MDL interpretation.** $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log Q_{\Sigma_t}(a^\ast)$ is the expected extra bits needed to code samples from $\pi^\ast$ under $Q_{\Sigma_t}$'s code. The coding interpretation aligns with the segment's MDL framing. MDL is itself a chain-rule-respecting coding scheme (the bits-to-code-a-joint decompose additively over factorizations); consistency with MDL is convergent with §6.1.

**Čencov/Morozova-Chentsov background** (Čencov 1982 *Statistical Decision Rules and Optimal Inference*, AMS Translations of Mathematical Monographs 53; Morozova & Chentsov 1991, "Markov invariant geometry on state manifolds," *Itogi Nauki i Tekhniki*, translated in *J. Sov. Math.* 56(5):2648–2669; Ay, Jost, Lê & Schwachhöfer 2017, *Information Geometry*, Springer). The f-divergence family itself is characterized by Markov-morphism invariance (sufficient-statistic coarse-graining invariance) — this is what makes "f-divergences" the right background family to search within. Amari 2009 shows the alpha-divergences are the sub-family that are simultaneously f-divergences and Bregman divergences. Reverse-KL sits at $\alpha = 1$ within the alpha-family; the chain-rule axiom of §6.1 is what picks $\alpha = 1$ out of the one-parameter alpha-family.

#### §6.3 — Bregman-Fenchel identification: reverse-KL and log-odds as dual coordinates

*[Derived (bregman-fenchel-dual-pair, exact; standard Legendre-Fenchel)]*

On the probability simplex $\Delta^{n-1}$, the **negative-entropy potential** $\phi(Q) = \sum_a Q_a \log Q_a$ is strictly convex, Legendre, and essentially smooth on the relative interior (Rockafellar 1970 *Convex Analysis* §26). Its Fenchel conjugate is the **log-partition function** $\phi^\ast(\eta) = \log \sum_a e^{\eta_a}$ on the natural-parameter space $\mathbb{R}^n$ modulo the affine-gauge direction. The primal-dual correspondence is softmax: $Q = \nabla \phi^\ast(\eta)$ gives $Q_a = e^{\eta_a}/\sum_{a'} e^{\eta_{a'}}$, and $\eta = \nabla\phi(Q) = \log Q + \mathbf 1$ (up to the constraint-normal direction) so $\eta_a - \eta_b = \log(Q_a/Q_b)$ is the **log-odds ratio**.

The Bregman divergence induced by $\phi$ on the primal simplex is **reverse-KL** exactly:

$$B_\phi(P, Q) \;:=\; \phi(P) - \phi(Q) - \langle \nabla\phi(Q), P - Q\rangle \;=\; \sum_a P_a \log\frac{P_a}{Q_a} \;=\; D_{\mathrm{KL}}(P \Vert Q)$$

*Derivation.* Expand: $\phi(P) - \phi(Q) = \sum_a(P_a \log P_a - Q_a \log Q_a)$; the inner-product term using $\nabla\phi(Q)_a = \log Q_a + 1$ gives $\sum_a(\log Q_a + 1)(P_a - Q_a) = \sum_a(\log Q_a)(P_a - Q_a)$ since $\sum_a(P_a - Q_a) = 0$. Substituting and simplifying yields $\sum_a P_a \log(P_a/Q_a) = D_{\mathrm{KL}}(P \Vert Q)$. $\square$

**Identification with `#edge-update-natural-parameter`.** The log-odds coordinate derived under evidential-additivity in `#edge-update-natural-parameter` is the *Fenchel-dual natural parameter* of this Legendre-Fenchel pair. The divergence-layer coordinate of this segment (reverse-KL on $\Delta^{n-1}$) and the update-layer coordinate of `#edge-update-natural-parameter` (log-odds on $\mathbb{R}^n/\mathbf 1$) are two sides of one exponential-family geometric structure, viewed through primal and dual coordinates respectively.

**What this adds.** The two segments independently derive their coordinates via Cauchy-FE on logically-independent AAD-internal axioms (chain-rule additivity here; evidential additivity in `#edge-update-natural-parameter`). The Fenchel-Bregman correspondence shows that *the coordinates the two axioms pick out are related by Legendre duality* — the axioms are not redundant (they have different logical forms and constrain different objects; see §6.1 vs. `#edge-update-natural-parameter`'s axiom) but the forced coordinates *coincide on one geometric object*. This is a Discussion-grade observation about the relationship between two primary instances of `#discussion-additive-coordinate-forcing`; it is textbook Legendre-Fenchel (Amari & Nagaoka 2000 §3.5; Bregman 1967; Beck & Teboulle 2003 *Mirror descent and nonlinear projected subgradient methods* — relevant for the operational consequence that mirror-descent on the policy simplex with negative-entropy regularizer is equivalent to exponentiated-gradient descent on log-odds coordinates). The full geometric-unification reading sits in `#discussion-additive-coordinate-forcing`'s meta-treatment.

#### §6.4 — Information-theoretic-MDP lineage and AAD's direction choice

*[Discussion (information-theoretic-mdp-lineage), positioning rather than derivation]*

AAD's reverse-KL strategy-cost form sits within an established research lineage — the information-theoretic treatment of decision problems initiated by **Tishby & Polani 2011** ("The Information Theory of Decision and Action," in *Perception-Action Cycle: Models, Architectures, and Hardware*, Springer, pp. 601–636; Eq. 15 p. 19 introduces **Information-to-Go** $\mathfrak{I}^\pi(s_t, a_t)$, the conditional multi-information of the entire future state-action trajectory; Eq. 17 p. 21 the trade-off objective $\arg\min_\pi[\mathfrak{I}^\pi - \beta Q^\pi]$) and developed by **Rubin, Shamir & Tishby 2012** ("Trading value and information in MDPs," in *Decision Making with Imperfect Decision Makers*, Springer, pp. 57–74; §2.2 Eq. 3 p. 4 **control information** $\Delta I(s) = \sum_a \pi_s(a) \log(\pi_s(a)/\rho_s(a))$; §3.1 Theorem 1 p. 5 Bellman recursion for the free-energy $F_\pi = I_\pi - \beta V_\pi$). The control-as-inference lineage via **Levine 2018** ("Reinforcement Learning and Control as Probabilistic Inference," arXiv:1805.00909; §3.1 Eq. 11 and §5.2 p. 15) develops the max-entropy-RL framework using $D_{\mathrm{KL}}(p_\theta \Vert p_{\mathrm{tgt}})$ throughout. The shared framework — value and information as joint first-class quantities in MDP optimization, with a KL divergence measuring the information cost of a policy against a reference — is the context in which AAD's strategy-cost objective naturally lives.

**AAD's direction is distinctive within this lineage.** Tishby-Polani 2011 uses the stationary marginal $\pi(a)$ of the policy itself as reference (Eq. 16 p. 20, Eq. 22 p. 22) — a direction-neutral multi-information rather than a KL-to-external-reference. Rubin et al. 2012 uses a default policy $\rho_s(a)$ (typically uniform) with direction $D_{\mathrm{KL}}(\pi_s \Vert \rho_s)$ — **agent-first, default-second**, a regularization/complexity cost. Levine 2018 uses $D_{\mathrm{KL}}(p_\theta \Vert p_{\mathrm{tgt}})$ — **proposal-first, target-second**, a variational ELBO form with softened exponentiated-reward target. **AAD's $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$** — **optimum-first, agent-second** — is the *opposite* direction to all three.

**The direction is forced, not chosen.** AAD's direction is not a convention adopted from the surrounding literature; it is forced by two independent structural requirements of this segment's derivation: (i) the regret-bound argument of §5 requires the optimum as the reference for the bound to be tight (mode-seeking toward $a^\ast$); (ii) the Bretagnolle-Huber identity of §4 is *exact* in the $\pi^\ast$-first direction under deterministic $\pi^\ast$ and degenerate in the flipped direction. The flipped direction (Rubin 2012's / Levine 2018's form with $\rho = \pi^\ast$) is vacuous here for the same reason forward-KL is vacuous in §5: $\pi^\ast$ has no support off $a^\ast$. AAD *owns* the direction-distinctiveness rather than inheriting it.

**Rubin 2012 Theorem 3 PAC-Bayesian motivation.** A fourth independent operational property of the $\pi^\ast$-first KL form comes from Rubin-Shamir-Tishby 2012 Theorem 3 (p. 10): under a-priori stochastic default policy and empirical reward estimate, the control information $I_\pi$ bounds the generalization gap of the value function:

$$\tilde D_{\mathrm{KL}}\bigl(\hat V_\pi(s_0) \,\big\Vert\, V_\pi(s_0)\bigr) \;\leq\; \frac{I_\pi(s_0) + \log(2m/\delta)}{m - 1}$$

This is a PAC-Bayesian concentration bound. In AAD terms: policies with lower strategy-cost have tighter value-function generalization under finite empirical data. Together with (a) the regret-bound direction-forcing of §5, (b) the chain-rule uniqueness of §6.1, and (c) the Bregman-Fenchel dual identification of §6.3, this is a fourth independent motivation for the KL-to-reference form — operational rather than axiomatic, and independent of the chain-rule axiom. The direction differs (Rubin uses agent-first; AAD uses optimum-first), but the generalization-bound structure transfers by the same PAC-Bayesian machinery: $I_\pi$ as regularizer against a reference.

**Relation to `#information-bottleneck`.** The canonical IB objective is $I(X; T) - \beta I(T; Y)$ with Shannon mutual information on both terms. AAD's strategy-cost relevance term is $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ — a KL divergence to a target, not a mutual information. The two are *sibling lineages*, both descended from Shannon rate-distortion theory (the IB instance uses MI-to-relevant-label as the fidelity term; the information-theoretic-MDP instance uses KL-to-reference-policy); neither reduces to the other without a change of relevance variable. AAD's compression-operations framework (`#compression-operations`) uses the IB form for $M_t$, $G_t^{\mathrm{shared}}$, and $\Lambda$ compressions; the strategy-cost compression uses the information-theoretic-MDP form. Both are valid Lagrangian relaxations of an underlying rate-distortion problem; the choice of fidelity term depends on whether the compressed variable is meant to preserve information about an observable (IB) or to match a reference policy (information-theoretic-MDP). The "abandoned IB purity" concern raised in external reviews (Gemini 2026-04-24) is defused at this level: AAD has not abandoned IB; its strategy-cost compression uses a different relevance quantity than its model-compression, and both are principled under the rate-distortion umbrella.

### §7 — $\beta_\Sigma$ interpretation under the regret bound

*[Discussion ($\beta_\Sigma$-local-vs-global)]*

The Pinsker bound gives $R(Q_{\Sigma_t}) \leq V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$. Two scale forms for the segment's trade-off parameter $\beta_\Sigma$ arise:

**(a) Square-root-KL form** (tight regret-bound scale):

$$\mathcal{L}(\Sigma_t) \;=\; \mathcal{R}(\Sigma_t) \;+\; \beta_\Sigma \cdot \sqrt{D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}, \qquad \beta_\Sigma = V_{\max}/\sqrt{2}$$

$\beta_\Sigma$ is *globally naturalized* as a constant scale proportional to the value range at fixed $M_t$. Cost: the form departs from the linear-Lagrangian IB shape that #compression-operations uses across the four compression operations.

**(b) Linear-KL form** (IB-shape instance, preserved in the segment):

$$\mathcal{L}(\Sigma_t) \;=\; \mathcal{R}(\Sigma_t) \;+\; \beta_\Sigma \cdot D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$$

Under this form, $\beta_\Sigma$'s regret-bound interpretation is *local*: differentiating the Pinsker bound, $\partial R/\partial D_{\mathrm{KL}} = V_{\max}/(2\sqrt{2 D_{\mathrm{KL}}})$, so $\beta_\Sigma$ represents the local cost-per-bit at the operating point but varies with $D_{\mathrm{KL}}$. Upside: consistency with the IB linear-Lagrangian shape ( #compression-operations). Downside: no uniform global $\beta_\Sigma$ scale.

**Choice made in #strategy-complexity-cost.** Keep the linear form (IB-shape alignment); note the square-root form in the Epistemic Status as the "source" derivation. The direction-forcing claim is the load-bearing strengthening; the linear-vs-square-root choice is a second-order trade-off that preserves architectural consistency at the cost of a fully naturalized $\beta_\Sigma$.

### §8 — Bound tightness and scope limits

**Vacuity regimes** (where the regret bound fails to be informative):

1. **$V_{\max} = \infty$ (unbounded value).** Then all bounds are $\infty$. AAD's $O_t$ is $\mathbb{R}$-valued ( #objective-functional); boundedness of $V$ over $\mathcal{A}$ at fixed $M_t$ is an additional assumption. Stated here as a scope condition of the derivation.
2. **$Q_{\Sigma_t}(a^\ast) = 0$ (strategy cannot express the optimum).** Then $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = +\infty$. This is structural failure — the strategy's DAG cannot produce the optimal action — and the infinite KL correctly flags it. *Informative degeneracy*, not pathology: operational minimization rejects such $\Sigma_t$.
3. **$\pi^\ast$ not deterministic (outside canonical scope).** For stochastic $\pi^\ast$ with larger support than $Q_{\Sigma_t}$, reverse-KL may still be infinite. §9 addresses tied-optimum extensions; stochastic $\pi^\ast$ under softmax-smoothing is future work.

**Tightness comparison.** Under deterministic $\pi^\ast$ (AAD's canonical scope), the Bretagnolle-Huber **identity** $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log(1 - \operatorname{TV}(\pi^\ast, Q_{\Sigma_t}))$ makes the KL and TV bounds *operationally equivalent in reverse-KL coordinates*: the KL-based bound $R \leq V_{\max}(1 - e^{-D_{\mathrm{KL}}})$ of §4 is exactly the TV-based bound of §3 re-expressed in the KL coordinate, with matching lower bound $R \geq \Delta_{\min}(1 - e^{-D_{\mathrm{KL}}})$ (§4). Pinsker is strictly weaker under this scope (see §4.1). Outside the deterministic-$\pi^\ast$ scope, the BH identity degrades back to the inequality $\operatorname{TV} \leq \sqrt{1 - e^{-D_{\mathrm{KL}}}}$ (Bretagnolle-Huber 1978; tighter than Pinsker for large $D_{\mathrm{KL}}$ but no longer an identity); Pinsker is the textbook fallback for general distributions. The net: reverse-KL is not merely "the tightest smooth divergence" — in AAD's canonical scope it carries the *exact* regret-bound relationship via BH, with Pinsker as a loose alternative retained only for stochastic-$\pi^\ast$ extensions.

### §9 — Extensions

**Tied-optimum case.** If $\pi^\ast$ has support on a tied-optimum set $\mathcal{A}^\ast = \{a : V(a) = V(a^\ast)\}$ with uniform mass, reverse-KL is finite whenever $Q_{\Sigma_t}$ covers $\mathcal{A}^\ast$. The regret-bound argument extends directly: $R(Q_{\Sigma_t}) = \sum_a Q_{\Sigma_t}(a)\Delta(a) \leq V_{\max} \cdot \mathbb{P}_{Q_{\Sigma_t}}(a \notin \mathcal{A}^\ast)$ and Pinsker applies unchanged.

**Softmax-smoothed $\pi^\ast$ (stochastic $\pi^\ast$ for non-degeneracy reasons).** A regret bound of the form

$$\mathbb{E}_{\pi^\ast}[V] - \mathbb{E}_{Q_{\Sigma_t}}[V]$$

with softmax-weighted $\pi^\ast$ also admits the Pinsker-KL step, with reverse-KL again the non-vacuous direction (forward-KL remains vacuous whenever $\pi^\ast$ has wider support than $Q_{\Sigma_t}$, and vice versa). Deferred for explicit treatment.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Regret definition $R(Q_{\Sigma_t}) := V(a^\ast) - \mathbb{E}_{Q_{\Sigma_t}}[V]$ | Definitional; collapses to the three literature forms under deterministic $\pi^\ast$ | Definition |
| TV-regret bound $R \leq V_{\max}\cdot\operatorname{TV}(\pi^\ast, Q_{\Sigma_t})$ | Bounded value range + deterministic $\pi^\ast$ | Proved (tight) |
| **BH identity** $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log(1 - \operatorname{TV}(\pi^\ast, Q_{\Sigma_t}))$ under deterministic $\pi^\ast$ | Direct calculation (Bretagnolle-Huber 1978 specialized to $P = \delta_{a^\ast}$) | **Proved (exact identity)** |
| **Regret-reverse-KL bound** $R \leq V_{\max}(1 - e^{-D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})})$ | TV-regret bound + BH identity, under deterministic $\pi^\ast$ | **Proved (tight in upper direction)** |
| **Matching lower bound** $R \geq \Delta_{\min}(1 - e^{-D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})})$ | Isolated-optimum action-gap $\Delta_{\min} \gt 0$ + BH identity | **Proved (Lipschitz-equivalence with $V_{\max}$ / $\Delta_{\min}$ constants)** |
| Pinsker-KL bound $R \leq V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$ | Pinsker's inequality applied to TV bound | Proved (strictly weaker than BH identity under deterministic $\pi^\ast$; correct form for stochastic-$\pi^\ast$ extensions) |
| **KL direction forced** (reverse-KL, $\pi^\ast$-first) | Forward-KL is vacuous ($+\infty$) under deterministic $\pi^\ast$ whenever $Q_{\Sigma_t}$ has off-optimum mass | **Proved (direction uniquely forced)** |
| **Asymmetry forced by regret's one-sidedness** | Regret contributes only from $Q_{\Sigma_t}$'s off-optimum mass; $\pi^\ast$'s off-$Q$ deviation is vacuous; symmetric divergences penalize interchangeably, which is operationally wrong | Proved (asymmetry forced; independent of chain-rule axiom) |
| **Reverse-KL uniquely forced within direction-forced f-divergences** | Chain-rule additivity axiom (Hobson 1969; Csiszár 1991 Theorem 3 corollary and Theorem 5; standard functional-equation derivation per Aczél & Daróczy 1975); AAD-internally motivated as divergence-level analog of #chain-confidence-decay (§6.1) | **Derived (conditional on chain-rule axiom)** |
| Secondary characterizations (gradient-tractability, VI-alignment, MDL coding) | Independent operational properties; each compatible with reverse-KL, none individually distinguishing | Formulation support (non-load-bearing under §6.1) |
| Fisher-metric-at-second-order does not distinguish reverse-KL | Eguchi 1983 §2 contrast-function framework (*Ann. Statist.* 11(3):793–803): every smooth f-divergence with $f''(1) \gt 0$ induces the Fisher metric up to scalar $f''(1)$ | Proved (no-go for Path A as uniqueness axiom) |
| Admissible family members (TV, Bretagnolle-Huber, $\chi^2$, Rényi-$\alpha$) | Each yields a valid regret bound; survey §6 | Derived (each) |
| Under deterministic $\pi^\ast$: TV and KL-coordinate bounds are equivalent via BH identity; Pinsker strictly weaker | §4 BH identity + §4.1 Pinsker comparison | Proved (scope-dependent tightness ordering) |
| Reverse-KL is the Bregman divergence of negative-entropy on $\Delta^{n-1}$; log-odds is the Fenchel-dual natural coordinate (Legendre-Fenchel pair) | Standard Legendre-Fenchel (Rockafellar 1970 §26; Amari & Nagaoka 2000 §3.5; Bregman 1967) applied to $\phi(Q) = \sum_a Q_a \log Q_a$ | Proved (textbook identification; §6.3) |
| AAD's $\pi^\ast$-first KL direction is distinctive within the information-theoretic-MDP lineage (TP2011 / Rubin 2012 / Levine 2018 all put agent-first) and is *forced* (not inherited) by the regret-bound + BH-identity derivations | Literature positioning (§6.4) + derivation structure (§§4–5) | Discussion (positioning; direction forced by §§4–5 derivations) |
| PAC-Bayesian generalization bound: $\tilde D_{\mathrm{KL}}(\hat V_\pi \Vert V_\pi) \leq (I_\pi + \log(2m/\delta))/(m-1)$ | Rubin-Shamir-Tishby 2012 Theorem 3 | Derived (external theorem applied; independent operational motivation alongside regret-bound + chain-rule + Fenchel-dual) |
| $\beta_\Sigma \propto V_{\max}$ naturalization (square-root-KL form) | Direct identification from Pinsker bound | Derived (under square-root form) |
| $\beta_\Sigma$ local interpretation (linear-KL form, segment-retained) | Differentiation of Pinsker bound at operating point | Derived (local only) |
| Linear-KL form retained over square-root form | IB-shape alignment with #compression-operations | Formulation choice |
| Vacuity regimes ($V_{\max}=\infty$, $Q_{\Sigma_t}(a^\ast)=0$, stochastic $\pi^\ast$) | Direct analysis of the bound | Proved (boundary) |
| Tied-optimum extension | $\pi^\ast$ uniform on $\mathcal{A}^\ast$; bound adapts directly | Derived |
| Softmax-smoothed $\pi^\ast$ extension | Sketched in §9 | Hypothesis (deferred) |
| Uniqueness under chain-rule axiom (§6.1) | Hobson 1969 / Csiszár 1991 Theorem 3 corollary and Theorem 5 / standard functional-equation argument per Aczél & Daróczy 1975, applied to the direction-forced family; axiom AAD-internally motivated (§6.1) | Derived (conditional) |

The dividing line: the KL **direction** is forced by the regret-bound derivation (strong result). The specific reverse-KL **form** within the direction-forced f-divergence family is *derived under the chain-rule additivity axiom* (§6.1) — conditional on an axiom that AAD independently motivates as the divergence-level version of the additive-decomposition principle already in #chain-confidence-decay. The $\beta_\Sigma$ naturalization is partial — available globally only under the square-root form, locally under the linear form retained for IB-shape alignment.

## Epistemic Status

*Robust qualitative* overall, with several specific claims at *exact* tier. The direction-forcing claim (§5) is derived under standard assumptions (bounded value, deterministic $\pi^\ast$ on the canonical AAD scope). The **Bretagnolle-Huber identity under deterministic $\pi^\ast$** (§4, $D_{\mathrm{KL}}(\pi^\ast \Vert Q) = -\log(1 - \operatorname{TV})$) is *exact* by direct calculation, and yields the tight regret bound $R \leq V_{\max}(1 - e^{-D_{\mathrm{KL}}})$ with matching lower bound $\Delta_{\min}(1 - e^{-D_{\mathrm{KL}}})$ — the segment's primary bound form. Pinsker (§4.1) is retained as the strictly-weaker general form, correct for stochastic-$\pi^\ast$ extensions. The TV bound (§3) is textbook. The admissible-divergence family characterization (§6) is a truthful survey. The **chain-rule uniqueness theorem (§6.1)** upgrades the reverse-KL selection to "uniquely forced conditional on the chain-rule axiom"; the axiom is AAD-internally motivated as the divergence-level analog of `#chain-confidence-decay`. **Asymmetry-from-one-sidedness (§5)** provides a second independent argument for the direction-forcing side, not requiring the chain-rule axiom. **Bregman-Fenchel identification (§6.3)** is textbook Legendre-Fenchel; ties the segment's divergence coordinate to `#edge-update-natural-parameter`'s update coordinate as Fenchel-dual aspects of one exponential-family structure. Fisher-metric-at-second-order is explicitly identified as *not* a distinguishing axiom within the f-divergence family (Eguchi's theorem), closing the most-obvious alternative candidate uniqueness route as a no-go. **Information-theoretic-MDP lineage positioning (§6.4)** is *Discussion-grade* (positioning in the literature, not a derivation); its role is to place AAD's direction-distinctive form honestly within the TP2011 / Rubin 2012 / Levine 2018 lineage rather than overclaim equivalence with any of them. The Rubin 2012 Theorem 3 PAC-Bayesian bound (§6.4) is a fourth independent operational motivation for the KL-to-reference form. The $\beta_\Sigma$ naturalization (§7) is a trade-off analysis, not a derivation. The extensions (§9) are sketches, not derivations.

Max attainable: *exact* for (a) "forward-KL is a vacuous bound on $R$ under deterministic $\pi^\ast$" (direct calculation; §5); (b) "under deterministic $\pi^\ast$, $D_{\mathrm{KL}}(\pi^\ast \Vert Q) = -\log(1 - \operatorname{TV}(\pi^\ast, Q))$" (BH identity; §4); (c) "regret is Lipschitz-equivalent to $(1 - e^{-D_{\mathrm{KL}}})$ with constants $\Delta_{\min}$ / $V_{\max}$" (§4 matched lower bound); (d) "reverse-KL is the Bregman divergence of negative-entropy; log-odds is its Fenchel-dual natural coordinate" (standard Legendre-Fenchel; §6.3); (e) "reverse-KL is the unique chain-rule-respecting f-divergence in the direction-forced family" (Hobson 1969 / Csiszár 1991; §6.1); (f) "asymmetry is forced by regret's one-sidedness" (direct; §5). *Robust qualitative* for the overall strengthened characterization — the chain-rule uniqueness is conditional on the chain-rule axiom, which is a principled axiom choice (AAD-internally motivated) but remains an axiom rather than a consequence of prior AAD commitments. The information-theoretic-MDP lineage positioning (§6.4) is *Discussion-grade* and honest about where AAD sits in the broader lineage rather than claiming formal equivalence.

## Discussion

**The convergence with active inference's reverse-KL.** Active inference's expected free energy (Friston et al. 2017; Parr & Pezzulo 2022) also uses reverse-KL against a preferred distribution, with the direction arising from the variational-free-energy-gradient lineage. AAD derives the direction from a regret-bound argument internal to the decision-theoretic scope. The convergence (two distinct derivations reach the same direction) is worth noting but is not a uniqueness argument — it shows reverse-KL is *natural* in multiple frames. The lineage difference preserves AAD's distinctive content: AAD's derivation does not require VFE as master objective or preferences-as-priors ( #ciy-unified-objective, #satisfaction-gap for the contrast).

**Why the regret bound is the right derivation, not Donsker-Varadhan.** The Donsker-Varadhan variational representation

$$\log\mathbb{E}_Q[e^f] \geq \mathbb{E}_P[f] - D_{\mathrm{KL}}(P \Vert Q)$$

gives reverse-KL bounds for exponential-moment functionals, but requires $V$ to have bounded exponential moments (a stronger-than-bounded assumption for unbounded $V$). The Pinsker-TV route used here requires only bounded value range and is closer to the AAD scope's natural assumptions. Donsker-Varadhan becomes relevant if unbounded-$V$ extensions are attempted.

**Relationship to standard policy-gradient regret bounds.** The argument here is structurally identical to standard policy-gradient / online MDP regret bounds (Agarwal, Kakade, Lee, Mahajan 2021 "On the theory of policy gradient methods" Lemma 3.2; Even-Dar, Kakade, Mansour 2009 "Online Markov decision processes"). AAD's contribution is *re-using the standard bound as the derivation of the KL direction in the strategy-cost objective*, not inventing the bound. This is consistent with AAD's integration-over-invention character.

**Position in the additive-coordinate-forcing pattern.** The chain-rule uniqueness theorem of §6.1 is the *divergence-level* instance of an AAD-wide pattern in which logarithmic coordinates are uniquely forced via Cauchy's functional equation on an AAD-internally-motivated additivity axiom. The pattern has two other primary instances: the chain-layer identity ( #chain-confidence-decay, the motivating anchor) and the update-layer log-odds uniqueness ( #edge-update-natural-parameter). #discussion-additive-coordinate-forcing catalogs the pattern, states the 1-anchor-plus-2-theorem structure precisely, and documents Lyapunov and IB Lagrangian as adjacent family members that share the additive-decomposition shape without the AAD-internal forcing structure.

## Working Notes

- **Linear vs. square-root form — revisit with downstream evidence.** The segment keeps the linear-KL form for IB-shape alignment. If downstream work shows the IB-shape-across-four-operations claim in #compression-operations is strained and the four $\beta$s want separate scales anyway, switching #strategy-complexity-cost to the square-root form (naturalizing $\beta_\Sigma$) becomes attractive. Revisit with the O-BP2 (four compressions as one hierarchy) work if pursued.
- **Stochastic-$\pi^\ast$ extension.** Flagged in §9 but not derived. The tied-optimum case is immediate; softmax-smoothed $\pi^\ast$ needs a careful treatment of what regret quantity is being bounded (expected-vs-max).
- **Family characterization strengthening.** *Resolved 2026-04-22* — see §6.1. The chain-rule additivity axiom (Hobson 1969; Csiszár 1991 Theorem 3 corollary and Theorem 5; standard functional-equation derivation per Aczél & Daróczy 1975) picks reverse-KL uniquely within the direction-forced f-divergence family. The Fisher-metric candidate was ruled out by Eguchi's theorem (every smooth f-divergence induces the Fisher metric at second order up to scale; not distinguishing). Full reasoning trail in `msc/spike-reverse-kl-uniqueness.md`, including the citation audit that corrected the initial draft's misattributions (Csiszár 1972, Amari 2009 Theorem 1, and Amari & Cichocki 2010 Prop 3.2 do not contain the chain-rule uniqueness theorem; the correct attributions are above).
- **BH identity under deterministic $\pi^\ast$ — elementary fact the earlier presentation underplayed.** *Resolved 2026-04-24.* §4 now presents the BH identity as primary, with Pinsker demoted to §4.1 as the loose general form. The earlier framing "non-Pinsker tighter bounds... BH flagged for operational work where the tightness difference matters" under-sold the result: under AAD's canonical deterministic-$\pi^\ast$ scope, the BH inequality specializes to an *identity* (not merely a tighter inequality), making the KL-coordinate bound exact rather than approximate. The segment now carries the exact two-sided relation with matching lower bound via $\Delta_{\min}$.
- **Citation verification (Path 1 content, §6.4).** The information-theoretic-MDP lineage content in §6.4 was PDF-verified 2026-04-24 against TP2011 / Rubin-Shamir-Tishby 2012 / Levine 2018. The verification process found a specific attribution error in an earlier spike draft — the objective form $\max_\pi \mathbb E[R] - \beta^{-1}I(\Pi;X)$ with KL-to-reference reference is **Rubin 2012's**, not TP2011's (TP2011's actual quantity is Information-to-Go multi-information $\mathfrak I^\pi$, a different object). The segment reflects the corrected attributions with explicit equation/page references. Full trail in `msc/spike-ib-purity-strategy-cost-strengthening-2026-04-24.md` §12 "Citation-verification addendum."
- **AAD-outlier-on-KL-direction — distinctive feature, not a departure.** *Documented 2026-04-24.* The literature uses agent-first or proposal-first directions; AAD uses optimum-first, forced by the regret-bound derivation and required for the BH identity to be exact. Owned rather than inherited; see §6.4.
- **Fenchel-Bregman connection to `#edge-update-natural-parameter`.** *Documented 2026-04-24.* §6.3 identifies reverse-KL and log-odds as Fenchel-dual coordinates of one exponential-family Legendre-Fenchel structure. The full geometric-unification reading (covering all four layers of `#discussion-additive-coordinate-forcing`) is a meta-segment-level observation; trail in `msc/spike-fenchel-bregman-reframe-additive-coordinate-forcing-2026-04-24.md`.
