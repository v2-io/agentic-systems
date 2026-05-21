# Appendix — Details (group 3)


## Derivation: Hard Ceiling on Strategic-Persistence Reachability under Exponential Forgetting

- **Slug**: `deriv-strategic-persistence-hard-ceiling`
- **Type**: derivation
- **Status**: exact
- **Stage**: draft
- **Depends**: `schema-strategy-persistence`, `deriv-edge-credence-dynamics`, `result-sector-persistence-template`

The strategic-persistence schema's instantaneous persistence form $\alpha_\Sigma \gt \rho_\Sigma/R_\Sigma$ ( #schema-strategy-persistence), instantiated under Beta-Bernoulli edge dynamics with exponential forgetting at rate $\lambda \in (0,1)$, has a sharp structural cap at $\rho_\Sigma/R_\Sigma = 1/2$: no $\lambda$ satisfies the prerequisite when strategic disturbance reaches half the strategic reserve. The schema's reachable persistence region is exactly the open half-plane $\rho_\Sigma \lt R_\Sigma/2$.

### Setup

Per #deriv-edge-credence-dynamics Prop B.1, the Beta-Bernoulli edge update with $n$ accumulated pseudo-counts gives sector parameter $\alpha_\Sigma = 1/(n+1)$. Without forgetting, $n \to \infty$ and $\alpha_\Sigma \to 0$ for every edge asymptotically — so the schema's instantaneous persistence form eventually fails under any positive disturbance rate. *Exponential forgetting* with discount $\lambda \in (0,1)$ replaces the raw update with the discounted recurrence:

*[Definition (Discounted Beta-Bernoulli Update)]*

$$\alpha_k \mapsto \lambda\,\alpha_k + y_k, \qquad \beta_k \mapsto \lambda\,\beta_k + (1 - y_k)$$

following the standard adaptive-control / online-learning treatment (Ljung 1987).

### Proposition C.1 (Steady-State Sector Parameter)

*[Derived (Conditional on Beta-Bernoulli edges + exponential forgetting)]*

Under the discounted Beta-Bernoulli recurrence, the steady-state sector parameter at the fixed point $\hat p = \theta$ is:

$$\alpha_\Sigma^{\text{ss}} = \frac{1-\lambda}{2-\lambda}$$

*Proof.* At a fixed point in expectation, the discounted recurrence stabilizes when each pseudo-count equals its own contribution rate divided by the dissipation:

$$\alpha^\ast = \lambda\,\alpha^\ast + \theta \implies \alpha^\ast = \frac{\theta}{1-\lambda}, \qquad \beta^\ast = \lambda\,\beta^\ast + (1-\theta) \implies \beta^\ast = \frac{1-\theta}{1-\lambda}$$

The effective sample size is the sum:

$$n_{\text{eff}} = \alpha^\ast + \beta^\ast = \frac{1}{1-\lambda}$$

Substituting into Prop B.1's $\alpha_\Sigma = 1/(n+1)$ at $n = n_{\text{eff}}$:

$$\alpha_\Sigma^{\text{ss}} = \frac{1}{n_{\text{eff}}+1} = \frac{1}{1/(1-\lambda) + 1} = \frac{1-\lambda}{1 + (1-\lambda)} = \frac{1-\lambda}{2-\lambda} \qquad \square$$

The slow-forgetting linear form $\alpha_\Sigma^{\text{ss}} \approx 1-\lambda$ is the asymptotic expansion as $\lambda \to 1$ (the regime where the $1/(2-\lambda)$ damping factor approaches unity). Outside the slow-forgetting limit the linear form overstates the steady-state $\alpha_\Sigma^{\text{ss}}$ — at $\lambda = 0.5$ by $50\%$ ($1/3$ exact vs $1/2$ linear); at $\lambda = 0.9$ by $10\%$ ($1/11$ exact vs $1/10$ linear). The exact form is operationally the threshold to check against; the linear form is unsafe outside its asymptotic regime.

### Proposition C.2 (Hard-Ceiling No-Go)

*[Derived (Conditional on Prop C.1 + the schema's persistence form)]*

The forgetting prerequisite for the schema's trajectory guarantee under exponential forgetting is:

$$\frac{1-\lambda}{2-\lambda} \;\gt\; \frac{\rho_\Sigma}{R_\Sigma}$$

This inequality is unsatisfiable for any $\lambda \in [0,1]$ when $\rho_\Sigma \geq R_\Sigma/2$. The supremum is sharp:

$$\sup_{\lambda \in [0,1]} \alpha_\Sigma^{\text{ss}}(\lambda) = \frac{1}{2}$$

achieved as $\lambda \to 0^+$ (maximally aggressive forgetting — no memory). The schema's reachable persistence region in $(\rho_\Sigma, R_\Sigma)$-space is exactly the open half-plane $\rho_\Sigma \lt R_\Sigma/2$.

*Proof.* Let $x = \rho_\Sigma/R_\Sigma$ with $x \in [0,1)$. Solving for the threshold $\lambda$ at which the inequality becomes equality:

$$(1-\lambda) = x(2-\lambda) \implies \lambda(x-1) = 2x-1 \implies \lambda = \frac{2x-1}{x-1} = \frac{1-2x}{1-x}$$

For $\lambda \in (0,1)$ to admit a strict solution to the inequality, we need $\lambda \gt 0$ at the threshold. With $x \lt 1$ (denominator positive), this requires $1 - 2x \gt 0$, i.e., $x \lt 1/2$.

At $x = 1/2$ exactly: the threshold $\lambda = 0$, giving $\alpha_\Sigma^{\text{ss}}(0) = (1-0)/(2-0) = 1/2 = x$ — equality, not strict satisfaction. For $x \gt 1/2$: no $\lambda \in [0,1]$ satisfies the strict inequality, since even maximally aggressive forgetting ($\lambda \to 0^+$) only achieves $\alpha_\Sigma^{\text{ss}} \to 1/2$. The supremum is exactly $1/2$ at $\lambda = 0$. $\square$

Equivalently: the schema's reachable set under any exponential-forgetting design is exactly $\{(\rho_\Sigma, R_\Sigma) : \rho_\Sigma \lt R_\Sigma/2\}$. The boundary $\rho_\Sigma = R_\Sigma/2$ is not in the reachable region (strict satisfaction required), and the half-plane above the boundary is entirely outside.

---



## Derivation: Regret-Bound Derivation of the Strategy-Cost KL Direction

- **Slug**: `deriv-strategy-cost-regret-bound`
- **Type**: derivation
- **Status**: robust-qualitative
- **Stage**: draft
- **Depends**: `form-strategy-complexity-cost`, `def-value-object`, `form-objective-functional`, `der-chain-confidence-decay`, `def-strategy-dag`

The variational form of the strategy-cost objective ( #form-strategy-complexity-cost) carries a $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ relevance term. This appendix derives that **the $\pi^\ast$-first KL direction is forced** as the non-vacuous regret-bound form, and proves (conditional on a chain-rule additivity axiom motivated by #der-chain-confidence-decay) that **reverse-KL is uniquely forced within the direction-forced f-divergence family**.

### §1 — Setup

Fix $O_t$, $M_t$, continuation policy $\pi_{\mathrm{cont}}$, and horizon $N_h$. The action-value is the objective-functional evaluation at $a$: $V(a) := Q_O(M_t, a; \pi_{\mathrm{cont}}, N_h)$ ( #def-value-object; $V$ derives from $O_t$ per #form-objective-functional). The optimal action is $a^\ast := \arg\max_a V(a)$; under AAT's canonical scope ( #def-value-object), the optimal policy $\pi^\ast(\cdot \mid M_t) = \delta_{a^\ast}$ is the point mass on $a^\ast$ (tied-optimum extensions §8). Write $V_{\max} := \max_a V(a) - \min_a V(a)$ for the value range at fixed $M_t$; this is finite whenever $\mathcal{A}$ is a bounded action set under $V$.

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

Under AAT's canonical scope (deterministic $\pi^\ast = \delta_{a^\ast}$), reverse-KL and total variation are related by an *identity*, not merely an inequality. This gives a tight two-sided regret bound that the Pinsker inequality strictly weakens.

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

**Under AAT's canonical scope, this is strictly weaker than the BH-identity form of §4.** For any $D_{\mathrm{KL}} \gt 0$: $1 - e^{-D_{\mathrm{KL}}} \lt \sqrt{D_{\mathrm{KL}}/2}$ for small $D_{\mathrm{KL}}$ (the BH form is linear in $D_{\mathrm{KL}}$ while Pinsker is $\sqrt{D_{\mathrm{KL}}}$), and Pinsker's $V_{\max}\sqrt{D_{\mathrm{KL}}/2}$ exceeds the trivial $V_{\max}$ bound once $D_{\mathrm{KL}} \gt 2$, giving vacuous content there. The BH identity is informative uniformly in $D_{\mathrm{KL}}$.

Pinsker remains the correct tool for stochastic-$\pi^\ast$ extensions (§9) where the deterministic-$\pi^\ast$ scope is relaxed and the BH identity degrades back to inequality.

### §5 — Direction-forcing claim (the load-bearing result)

*[Derived (kl-direction-forced, from deterministic $\pi^\ast$)]*

**Claim.** The KL direction with $\pi^\ast$ *first* is forced as the non-vacuous regret-bound form. Forward-KL $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast)$ is *not* a non-vacuous bound on $R(Q_{\Sigma_t})$ under deterministic $\pi^\ast$.

**Derivation.** Expanding:

$$D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast) \;=\; \sum_a Q_{\Sigma_t}(a) \log\!\bigl(Q_{\Sigma_t}(a)/\pi^\ast(a)\bigr)$$

For any $a \neq a^\ast$: $\pi^\ast(a) = 0$ (point mass assumption). The summand $Q_{\Sigma_t}(a)\log(Q_{\Sigma_t}(a)/0) = +\infty$ unless $Q_{\Sigma_t}(a) = 0$. Therefore $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast) = +\infty$ whenever $Q_{\Sigma_t}$ places any mass off $a^\ast$ — for *all but a measure-zero subset* of stochastic strategies. A bound "$R \leq +\infty$" is vacuous.

This is the same shape of degeneracy as the original Shannon-MI form (Gemini Finding 2) that the V-medium move was introduced to escape: same degeneracy-when-$\pi^\ast$-is-deterministic, different value ($0$ vs $+\infty$). Only the *reverse* direction escapes both.

**Alignment with the structural problem.** Forward-KL is natural for *mode-covering* inference (where $Q$ is asked to cover $P$'s full support) and variational inference when $Q$ is learned to match a full distribution. Reverse-KL is natural for *mode-seeking* (concentrate $Q$ on $P$'s mode). The AAT strategy problem is mode-seeking by construction: the strategy should concentrate on $a^\ast$. The direction alignment with the structural problem is not accidental.

**Asymmetry is forced by regret's one-sidedness.** A second, independent argument for asymmetry — one that does not rely on the chain-rule axiom of §6.1. Under deterministic $\pi^\ast$, regret is a *one-sided* quantity: $R(Q_{\Sigma_t}) = \sum_{a \neq a^\ast} Q_{\Sigma_t}(a)\Delta(a)$ contributes only from $Q_{\Sigma_t}$'s off-optimum mass; $\pi^\ast$'s "mass off $Q_{\Sigma_t}$" is vacuous since $\pi^\ast$ has no support off $a^\ast$. Any divergence whose role is to bound this quantity should therefore be asymmetric — it should penalize $Q_{\Sigma_t}$'s deviation from $\pi^\ast$ without symmetrically penalizing the (trivially zero) deviation of $\pi^\ast$ from $Q_{\Sigma_t}$. Symmetric divergences (squared Hellinger, Jensen-Shannon, symmetrized KL) treat the two deviations interchangeably; under the one-sided regret quantity this is operationally wrong — it introduces a term with no semantic role. The asymmetry requirement is thus *structural*, emerging directly from what regret is as a functional, and is established independently of the chain-rule axiom that picks the specific asymmetric form in §6.1. The two arguments compose: *direction-forcing* (vacuity under deterministic $\pi^\ast$) + *asymmetry-forcing* (regret is one-sided) ⇒ the admissible bounding divergence is $\pi^\ast$-first and asymmetric; chain-rule additivity (§6.1) then picks reverse-KL uniquely within that family.

**Terminology note (Bishop-vs-AAT "reverse-KL").** AAT's canonical reverse-KL is $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ — optimum-first, agent-second. Under Bishop 2006's convention ($D_{\mathrm{KL}}(q \Vert p)$ with $q$ the approximation is called "reverse-KL"), AAT's form would be labeled "forward-KL." The two naming conventions disagree in surface labeling but agree in the operational property — both pick out the *mode-seeking* direction (concentrate the approximation on the target's mode). Literature that uses the Bishop convention (variational inference, generative modeling, Levine 2018) and literature that uses the $\pi^\ast$-first / target-first convention (decision theory, regret analysis, Rubin-Shamir-Tishby 2012) describe the same operational quantity under deterministic $\pi^\ast$. When this segment writes "reverse-KL," the $\pi^\ast$-first / AAT convention is meant; under softened targets the two conventions describe different objects and must be disambiguated explicitly.

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

**These are not independent uniqueness routes.** Hobson's composition axiom, Csiszár's transitive-projection axiom, Shore-Johnson's system-independence axiom, and Sanov's sampling-consistency condition are *structurally-equivalent re-formulations* of the same underlying requirement — all factor through independence-of-sub-problems (joint inference on independent subsystems decomposes additively over factorizations). The Cauchy functional equation that each reduces to is the common structural content beneath varied surface formulations. This matters for `#disc-additive-coordinate-forcing`: the chain-rule axiom's load-bearing role is not weakened by noting multiple canonical references; conversely, the multiple references do not provide multiple independent uniqueness arguments. No known uniqueness route outside the independence-on-sub-problems family exists.

**Proof sketch.** Write $r_x = P(x)/Q(x)$, $s_{y\mid x} = P(y\mid x)/Q(y\mid x)$. The chain-rule identity must hold for all joint decompositions, which forces the functional equation $f(r s) = f(r) + r f(s) + g(r)$ for all $r, s \gt 0$. Combined with $f(1) = 0$ and convexity, the unique solution is $f(t) = c \cdot t\log t$ for $c \gt 0$ (Aczél & Daróczy 1975 §4).

**Why other members of the family fail the chain rule.** Concrete counterexample for $\chi^2$: take $Q_X$ uniform on $\{x_1, x_2\}$, $P_X = (3/4, 1/4)$, $Q(y\mid x)$ uniform, $P(y\mid x) = (3/4, 1/4)$ for both $x$. Direct calculation gives $\chi^2(P_{XY}\Vert Q_{XY}) = 9/16$, while $\chi^2(P_X\Vert Q_X) + \mathbb{E}_{P_X}[\chi^2(P_{Y\mid X}\Vert Q_{Y\mid X})] = 1/4 + 1/4 = 8/16$. Non-additive: $9/16 \neq 8/16$. Rényi-$\alpha$ for $\alpha \neq 1$ fails analogously; Bretagnolle-Huber is a monotone transform of reverse-KL (not an independent f-divergence); Hellinger-squared ($\alpha = 0$) likewise fails.

**AAT-internal motivation for the chain-rule axiom.** The chain rule is the *divergence-level analog* of the additive log-confidence decay in `#der-chain-confidence-decay`. AAT has already committed to additive-mismatch-decomposition-along-causal-chains in that segment; the divergence-level parallel is:

$$D(\pi^\ast \Vert Q_{\Sigma_t}) \;=\; \sum_{t=1}^T \mathbb{E}_{\pi^\ast}\!\left[D\bigl(\pi^\ast(\cdot\mid a_{\lt t}^\ast) \,\big\Vert\, Q(\cdot\mid a_{\lt t}^\ast)\bigr)\right]$$

— total mismatch between $\pi^\ast$ and $Q_{\Sigma_t}$ decomposes additively over the DAG's causal layers along the optimal trajectory. Non-chain-rule divergences (e.g., $\chi^2$) give super-additive decompositions in which layer-mismatches amplify multiplicatively — structurally discordant with the DAG factorization ( #def-strategy-dag). Adopting the chain-rule axiom is therefore not arbitrary; it is the divergence-level version of a decomposition principle AAT already relies on.

**Corollary (within the chain-rule axiom).** Under deterministic $\pi^\ast$ + bounded value + chain-rule additivity, reverse-KL is the unique smooth f-divergence in the direction-forced admissible family. The "Reverse-KL canonical among smooth divergences" status upgrades from formulation choice (under the pre-axiom reading) to *Derived (conditional on the chain-rule axiom)*.

**What the uniqueness theorem does not do.** It fixes the divergence within the f-divergence family; it does not fix the bounding function $g$ around the divergence (Pinsker vs Bretagnolle-Huber vs Le Cam-on-$\chi^2$ are *different bounds using different divergences*, so only Pinsker and BH-on-KL remain in scope after uniqueness — and these differ only in the $g$-envelope on top of reverse-KL, not in the divergence itself). It does not resolve the linear-vs-square-root form question of §7 (that is a Lagrangian-shape choice orthogonal to the divergence choice). Monotone transforms of reverse-KL (e.g., $1 - e^{-D_{\mathrm{KL}}}$) are equivalence-class members for gradient-based optimization and are not ruled out.

**Scope of the axiom.** The chain rule is stated for arbitrary joint decompositions. AAT's strategy spaces are discrete at the proposition level; the theorem applies directly. For continuous strategy spaces (e.g., low-level control), the chain rule extends by replacing sums with integrals against the dominating measure; the functional-equation derivation is identical in the continuous case (see Liese & Vajda 1987, *Convex Statistical Distances*, Teubner, for the standard measure-theoretic treatment of f-divergences and their decomposition properties).

#### §6.2 — Secondary characterizations (now supporting rather than load-bearing)

Four additional properties further motivate reverse-KL as the canonical choice; under §6.1 they are no longer load-bearing for uniqueness but remain informative about why reverse-KL is a comfortable fit with the rest of the AAT framework:

1. **Gradient-tractability.** TV is non-differentiable at mass boundaries; reverse-KL is smooth. Operational minimization via gradient methods rules out TV despite its tightness — independent of the uniqueness argument.
2. **Variational-inference alignment.** Reverse-KL is the standard divergence in the variational-inference lineage (ELBO derivation uses reverse-KL; Friston et al. 2017; Da Costa et al. 2020). The V-medium move's rhetorical payoff — shared vocabulary with active inference — lives on reverse-KL specifically. This is *convergent evidence* that reverse-KL is natural in multiple frames, not an independent uniqueness argument (Path D in `spikes/spike-reverse-kl-uniqueness.md` §6 shows the ELBO decomposition itself uses the chain rule as a sub-step; logical priority is chain rule → reverse-KL → ELBO).
3. **Fisher geometry.** Reverse-KL's second-order expansion gives the Fisher information metric (Amari & Nagaoka 2000). *But by the differential-geometric framework in Eguchi 1983* ("Second order efficiency of minimum contrast estimators in a curved exponential family," *Annals of Statistics* 11(3):793–803, §2 contrast-function development; modern restatement at Amari & Cichocki 2010 Theorem 5 eq. (126)), every smooth f-divergence with $f''(1) \gt 0$ induces the Fisher metric at second order up to the scalar $f''(1)$. Fisher-metric-at-second-order is *not* a distinguishing axiom within the f-divergence family — it is satisfied by every member. Noted here because it is a commonly-invoked distinguishing property; it does not distinguish. (Eguchi's Theorem 3 itself is about estimator efficiency via $\Gamma^1$-transversality; the f-divergence/Fisher-metric result is a consequence of the §2 contrast-function machinery that supports Theorem 3, not the theorem statement.)
4. **Information-budget / MDL interpretation.** $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log Q_{\Sigma_t}(a^\ast)$ is the expected extra bits needed to code samples from $\pi^\ast$ under $Q_{\Sigma_t}$'s code. The coding interpretation aligns with the segment's MDL framing. MDL is itself a chain-rule-respecting coding scheme (the bits-to-code-a-joint decompose additively over factorizations); consistency with MDL is convergent with §6.1.

**Čencov/Morozova-Chentsov background** (Čencov 1982 *Statistical Decision Rules and Optimal Inference*, AMS Translations of Mathematical Monographs 53; Morozova & Chentsov 1991, "Markov invariant geometry on state manifolds," *Itogi Nauki i Tekhniki*, translated in *J. Sov. Math.* 56(5):2648–2669; Ay, Jost, Lê & Schwachhöfer 2017, *Information Geometry*, Springer). The f-divergence family itself is characterized by Markov-morphism invariance (sufficient-statistic coarse-graining invariance) — this is what makes "f-divergences" the right background family to search within. Amari 2009 shows the alpha-divergences are the sub-family that are simultaneously f-divergences and Bregman divergences. Reverse-KL sits at $\alpha = 1$ within the alpha-family; the chain-rule axiom of §6.1 is what picks $\alpha = 1$ out of the one-parameter alpha-family.

#### §6.3 — Bregman-Fenchel identification: reverse-KL and log-odds as dual coordinates

*[Derived (bregman-fenchel-dual-pair, exact; standard Legendre-Fenchel)]*

On the probability simplex $\Delta^{n-1}$, the **negative-entropy potential** $\phi(Q) = \sum_a Q_a \log Q_a$ is strictly convex, Legendre, and essentially smooth on the relative interior (Rockafellar 1970 *Convex Analysis* §26). Its Fenchel conjugate is the **log-partition function** $\phi^\ast(\eta) = \log \sum_a e^{\eta_a}$ on the natural-parameter space $\mathbb{R}^n$ modulo the affine-gauge direction. The primal-dual correspondence is softmax: $Q = \nabla \phi^\ast(\eta)$ gives $Q_a = e^{\eta_a}/\sum_{a'} e^{\eta_{a'}}$, and $\eta = \nabla\phi(Q) = \log Q + \mathbf 1$ (up to the constraint-normal direction) so $\eta_a - \eta_b = \log(Q_a/Q_b)$ is the **log-odds ratio**.

The Bregman divergence induced by $\phi$ on the primal simplex is **reverse-KL** exactly:

$$B_\phi(P, Q) \;:=\; \phi(P) - \phi(Q) - \langle \nabla\phi(Q), P - Q\rangle \;=\; \sum_a P_a \log\frac{P_a}{Q_a} \;=\; D_{\mathrm{KL}}(P \Vert Q)$$

*Derivation.* Expand: $\phi(P) - \phi(Q) = \sum_a(P_a \log P_a - Q_a \log Q_a)$; the inner-product term using $\nabla\phi(Q)_a = \log Q_a + 1$ gives $\sum_a(\log Q_a + 1)(P_a - Q_a) = \sum_a(\log Q_a)(P_a - Q_a)$ since $\sum_a(P_a - Q_a) = 0$. Substituting and simplifying yields $\sum_a P_a \log(P_a/Q_a) = D_{\mathrm{KL}}(P \Vert Q)$. $\square$

**Identification with `#deriv-edge-update-natural-parameter`.** The log-odds coordinate derived under evidential-additivity in `#deriv-edge-update-natural-parameter` is the *Fenchel-dual natural parameter* of this Legendre-Fenchel pair. The divergence-layer coordinate of this segment (reverse-KL on $\Delta^{n-1}$) and the update-layer coordinate of `#deriv-edge-update-natural-parameter` (log-odds on $\mathbb{R}^n/\mathbf 1$) are two sides of one exponential-family geometric structure, viewed through primal and dual coordinates respectively.

**What this adds.** The two segments independently derive their coordinates via Cauchy-FE on logically-independent AAT-internal axioms (chain-rule additivity here; evidential additivity in `#deriv-edge-update-natural-parameter`). The Fenchel-Bregman correspondence shows that *the coordinates the two axioms pick out are related by Legendre duality* — the axioms are not redundant (they have different logical forms and constrain different objects; see §6.1 vs. `#deriv-edge-update-natural-parameter`'s axiom) but the forced coordinates *coincide on one geometric object*. This is a Discussion-grade observation about the relationship between two primary instances of `#disc-additive-coordinate-forcing`; it is textbook Legendre-Fenchel (Amari & Nagaoka 2000 §3.5; Bregman 1967; Beck & Teboulle 2003 *Mirror descent and nonlinear projected subgradient methods* — relevant for the operational consequence that mirror-descent on the policy simplex with negative-entropy regularizer is equivalent to exponentiated-gradient descent on log-odds coordinates). The full geometric-unification reading sits in `#disc-additive-coordinate-forcing`'s meta-treatment.

#### §6.4 — Information-theoretic-MDP lineage and AAT's direction choice

*[Discussion (information-theoretic-mdp-lineage), positioning rather than derivation]*

AAT's reverse-KL strategy-cost form sits within an established research lineage — the information-theoretic treatment of decision problems initiated by **Tishby & Polani 2011** ("The Information Theory of Decision and Action," in *Perception-Action Cycle: Models, Architectures, and Hardware*, Springer, pp. 601–636; Eq. 15 p. 19 introduces **Information-to-Go** $\mathfrak{I}^\pi(s_t, a_t)$, the conditional multi-information of the entire future state-action trajectory; Eq. 17 p. 21 the trade-off objective $\arg\min_\pi[\mathfrak{I}^\pi - \beta Q^\pi]$) and developed by **Rubin, Shamir & Tishby 2012** ("Trading value and information in MDPs," in *Decision Making with Imperfect Decision Makers*, Springer, pp. 57–74; §2.2 Eq. 3 p. 4 **control information** $\Delta I(s) = \sum_a \pi_s(a) \log(\pi_s(a)/\rho_s(a))$; §3.1 Theorem 1 p. 5 Bellman recursion for the free-energy $F_\pi = I_\pi - \beta V_\pi$). The control-as-inference lineage via **Levine 2018** ("Reinforcement Learning and Control as Probabilistic Inference," arXiv:1805.00909; §3.1 Eq. 11 and §5.2 p. 15) develops the max-entropy-RL framework using $D_{\mathrm{KL}}(p_\theta \Vert p_{\mathrm{tgt}})$ throughout. The shared framework — value and information as joint first-class quantities in MDP optimization, with a KL divergence measuring the information cost of a policy against a reference — is the context in which AAT's strategy-cost objective naturally lives.

**AAT's direction is distinctive within this lineage.** Tishby-Polani 2011 uses the stationary marginal $\pi(a)$ of the policy itself as reference (Eq. 16 p. 20, Eq. 22 p. 22) — a direction-neutral multi-information rather than a KL-to-external-reference. Rubin et al. 2012 uses a default policy $\rho_s(a)$ (typically uniform) with direction $D_{\mathrm{KL}}(\pi_s \Vert \rho_s)$ — **agent-first, default-second**, a regularization/complexity cost. Levine 2018 uses $D_{\mathrm{KL}}(p_\theta \Vert p_{\mathrm{tgt}})$ — **proposal-first, target-second**, a variational ELBO form with softened exponentiated-reward target. **AAT's $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$** — **optimum-first, agent-second** — is the *opposite* direction to all three.

**The direction is forced, not chosen.** AAT's direction is not a convention adopted from the surrounding literature; it is forced by two independent structural requirements of this segment's derivation: (i) the regret-bound argument of §5 requires the optimum as the reference for the bound to be tight (mode-seeking toward $a^\ast$); (ii) the Bretagnolle-Huber identity of §4 is *exact* in the $\pi^\ast$-first direction under deterministic $\pi^\ast$ and degenerate in the flipped direction. The flipped direction (Rubin 2012's / Levine 2018's form with $\rho = \pi^\ast$) is vacuous here for the same reason forward-KL is vacuous in §5: $\pi^\ast$ has no support off $a^\ast$. AAT *owns* the direction-distinctiveness rather than inheriting it.

**Rubin 2012 Theorem 3 PAC-Bayesian motivation.** A fourth independent operational property of the $\pi^\ast$-first KL form comes from Rubin-Shamir-Tishby 2012 Theorem 3 (p. 10): under a-priori stochastic default policy and empirical reward estimate, the control information $I_\pi$ bounds the generalization gap of the value function:

$$\tilde D_{\mathrm{KL}}\bigl(\hat V_\pi(s_0) \,\big\Vert\, V_\pi(s_0)\bigr) \;\leq\; \frac{I_\pi(s_0) + \log(2m/\delta)}{m - 1}$$

This is a PAC-Bayesian concentration bound. In AAT terms: policies with lower strategy-cost have tighter value-function generalization under finite empirical data. Together with (a) the regret-bound direction-forcing of §5, (b) the chain-rule uniqueness of §6.1, and (c) the Bregman-Fenchel dual identification of §6.3, this is a fourth independent motivation for the KL-to-reference form — operational rather than axiomatic, and independent of the chain-rule axiom. The direction differs (Rubin uses agent-first; AAT uses optimum-first), but the generalization-bound structure transfers by the same PAC-Bayesian machinery: $I_\pi$ as regularizer against a reference.

**Relation to `#form-information-bottleneck`.** The canonical IB objective is $I(X; T) - \beta I(T; Y)$ with Shannon mutual information on both terms. AAT's strategy-cost relevance term is $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ — a KL divergence to a target, not a mutual information. The two are *sibling lineages*, both descended from Shannon rate-distortion theory (the IB instance uses MI-to-relevant-label as the fidelity term; the information-theoretic-MDP instance uses KL-to-reference-policy); neither reduces to the other without a change of relevance variable. AAT's compression-operations framework (`#disc-compression-operations`) uses the IB form for $M_t$, $G_t^{\mathrm{shared}}$, and $\Lambda$ compressions; the strategy-cost compression uses the information-theoretic-MDP form. Both are valid Lagrangian relaxations of an underlying rate-distortion problem; the choice of fidelity term depends on whether the compressed variable is meant to preserve information about an observable (IB) or to match a reference policy (information-theoretic-MDP). The "abandoned IB purity" concern raised in external reviews (Gemini 2026-04-24) is defused at this level: AAT has not abandoned IB; its strategy-cost compression uses a different relevance quantity than its model-compression, and both are principled under the rate-distortion umbrella.

### §7 — $\beta_\Sigma$ interpretation under the regret bound

*[Discussion ($\beta_\Sigma$-local-vs-global)]*

The Pinsker bound gives $R(Q_{\Sigma_t}) \leq V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$. Two scale forms for the segment's trade-off parameter $\beta_\Sigma$ arise:

**(a) Square-root-KL form** (tight regret-bound scale):

$$\mathcal{L}(\Sigma_t) \;=\; \mathcal{R}(\Sigma_t) \;+\; \beta_\Sigma \cdot \sqrt{D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}, \qquad \beta_\Sigma = V_{\max}/\sqrt{2}$$

$\beta_\Sigma$ is *globally naturalized* as a constant scale proportional to the value range at fixed $M_t$. Cost: the form departs from the linear-Lagrangian IB shape that #disc-compression-operations uses across the four compression operations.

**(b) Linear-KL form** (IB-shape instance, preserved in the segment):

$$\mathcal{L}(\Sigma_t) \;=\; \mathcal{R}(\Sigma_t) \;+\; \beta_\Sigma \cdot D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$$

Under this form, $\beta_\Sigma$'s regret-bound interpretation is *local*: differentiating the Pinsker bound, $\partial R/\partial D_{\mathrm{KL}} = V_{\max}/(2\sqrt{2 D_{\mathrm{KL}}})$, so $\beta_\Sigma$ represents the local cost-per-bit at the operating point but varies with $D_{\mathrm{KL}}$. Upside: consistency with the IB linear-Lagrangian shape ( #disc-compression-operations). Downside: no uniform global $\beta_\Sigma$ scale.

**Choice made in #form-strategy-complexity-cost.** Keep the linear form (IB-shape alignment); note the square-root form in the Epistemic Status as the "source" derivation. The direction-forcing claim is the load-bearing strengthening; the linear-vs-square-root choice is a second-order trade-off that preserves architectural consistency at the cost of a fully naturalized $\beta_\Sigma$.

### §8 — Bound tightness and scope limits

**Vacuity regimes** (where the regret bound fails to be informative):

1. **$V_{\max} = \infty$ (unbounded value).** Then all bounds are $\infty$. AAT's $O_t$ is $\mathbb{R}$-valued ( #form-objective-functional); boundedness of $V$ over $\mathcal{A}$ at fixed $M_t$ is an additional assumption. Stated here as a scope condition of the derivation.
2. **$Q_{\Sigma_t}(a^\ast) = 0$ (strategy cannot express the optimum).** Then $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = +\infty$. This is structural failure — the strategy's DAG cannot produce the optimal action — and the infinite KL correctly flags it. *Informative degeneracy*, not pathology: operational minimization rejects such $\Sigma_t$.
3. **$\pi^\ast$ not deterministic (outside canonical scope).** For stochastic $\pi^\ast$ with larger support than $Q_{\Sigma_t}$, reverse-KL may still be infinite. §9 addresses tied-optimum extensions; stochastic $\pi^\ast$ under softmax-smoothing is future work.

**Tightness comparison.** Under deterministic $\pi^\ast$ (AAT's canonical scope), the Bretagnolle-Huber **identity** $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log(1 - \operatorname{TV}(\pi^\ast, Q_{\Sigma_t}))$ makes the KL and TV bounds *operationally equivalent in reverse-KL coordinates*: the KL-based bound $R \leq V_{\max}(1 - e^{-D_{\mathrm{KL}}})$ of §4 is exactly the TV-based bound of §3 re-expressed in the KL coordinate, with matching lower bound $R \geq \Delta_{\min}(1 - e^{-D_{\mathrm{KL}}})$ (§4). Pinsker is strictly weaker under this scope (see §4.1). Outside the deterministic-$\pi^\ast$ scope, the BH identity degrades back to the inequality $\operatorname{TV} \leq \sqrt{1 - e^{-D_{\mathrm{KL}}}}$ (Bretagnolle-Huber 1978; tighter than Pinsker for large $D_{\mathrm{KL}}$ but no longer an identity); Pinsker is the textbook fallback for general distributions. The net: reverse-KL is not merely "the tightest smooth divergence" — in AAT's canonical scope it carries the *exact* regret-bound relationship via BH, with Pinsker as a loose alternative retained only for stochastic-$\pi^\ast$ extensions.

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
| **Reverse-KL uniquely forced within direction-forced f-divergences** | Chain-rule additivity axiom (Hobson 1969; Csiszár 1991 Theorem 3 corollary and Theorem 5; standard functional-equation derivation per Aczél & Daróczy 1975); AAT-internally motivated as divergence-level analog of #der-chain-confidence-decay (§6.1) | **Derived (conditional on chain-rule axiom)** |
| Secondary characterizations (gradient-tractability, VI-alignment, MDL coding) | Independent operational properties; each compatible with reverse-KL, none individually distinguishing | Formulation support (non-load-bearing under §6.1) |
| Fisher-metric-at-second-order does not distinguish reverse-KL | Eguchi 1983 §2 contrast-function framework (*Ann. Statist.* 11(3):793–803): every smooth f-divergence with $f''(1) \gt 0$ induces the Fisher metric up to scalar $f''(1)$ | Proved (no-go for Path A as uniqueness axiom) |
| Admissible family members (TV, Bretagnolle-Huber, $\chi^2$, Rényi-$\alpha$) | Each yields a valid regret bound; survey §6 | Derived (each) |
| Under deterministic $\pi^\ast$: TV and KL-coordinate bounds are equivalent via BH identity; Pinsker strictly weaker | §4 BH identity + §4.1 Pinsker comparison | Proved (scope-dependent tightness ordering) |
| Reverse-KL is the Bregman divergence of negative-entropy on $\Delta^{n-1}$; log-odds is the Fenchel-dual natural coordinate (Legendre-Fenchel pair) | Standard Legendre-Fenchel (Rockafellar 1970 §26; Amari & Nagaoka 2000 §3.5; Bregman 1967) applied to $\phi(Q) = \sum_a Q_a \log Q_a$ | Proved (textbook identification; §6.3) |
| AAT's $\pi^\ast$-first KL direction is distinctive within the information-theoretic-MDP lineage (TP2011 / Rubin 2012 / Levine 2018 all put agent-first) and is *forced* (not inherited) by the regret-bound + BH-identity derivations | Literature positioning (§6.4) + derivation structure (§§4–5) | Discussion (positioning; direction forced by §§4–5 derivations) |
| PAC-Bayesian generalization bound: $\tilde D_{\mathrm{KL}}(\hat V_\pi \Vert V_\pi) \leq (I_\pi + \log(2m/\delta))/(m-1)$ | Rubin-Shamir-Tishby 2012 Theorem 3 | Derived (external theorem applied; independent operational motivation alongside regret-bound + chain-rule + Fenchel-dual) |
| $\beta_\Sigma \propto V_{\max}$ naturalization (square-root-KL form) | Direct identification from Pinsker bound | Derived (under square-root form) |
| $\beta_\Sigma$ local interpretation (linear-KL form, segment-retained) | Differentiation of Pinsker bound at operating point | Derived (local only) |
| Linear-KL form retained over square-root form | IB-shape alignment with #disc-compression-operations | Formulation choice |
| Vacuity regimes ($V_{\max}=\infty$, $Q_{\Sigma_t}(a^\ast)=0$, stochastic $\pi^\ast$) | Direct analysis of the bound | Proved (boundary) |
| Tied-optimum extension | $\pi^\ast$ uniform on $\mathcal{A}^\ast$; bound adapts directly | Derived |
| Softmax-smoothed $\pi^\ast$ extension | Sketched in §9 | Hypothesis (deferred) |
| Uniqueness under chain-rule axiom (§6.1) | Hobson 1969 / Csiszár 1991 Theorem 3 corollary and Theorem 5 / standard functional-equation argument per Aczél & Daróczy 1975, applied to the direction-forced family; axiom AAT-internally motivated (§6.1) | Derived (conditional) |

The dividing line: the KL **direction** is forced by the regret-bound derivation (strong result). The specific reverse-KL **form** within the direction-forced f-divergence family is *derived under the chain-rule additivity axiom* (§6.1) — conditional on an axiom that AAT independently motivates as the divergence-level version of the additive-decomposition principle already in #der-chain-confidence-decay. The $\beta_\Sigma$ naturalization is partial — available globally only under the square-root form, locally under the linear form retained for IB-shape alignment.

---



## Derivation: Log-Odds as the Unique Additive-Evidence Parameterization for Edge Credences

- **Slug**: `deriv-edge-update-natural-parameter`
- **Type**: derivation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `def-strategy-dag`, `hyp-edge-update-via-gain`, `der-chain-confidence-decay`, `deriv-strategy-cost-regret-bound`

The log-odds coordinate $\lambda_{ij} = \log(p_{ij} / (1 - p_{ij}))$ is the unique parameterization (up to positive affine transformation) on which independent Bernoulli evidence updates edge credences additively, under an evidential-additivity axiom motivated as the update-level analog of #der-chain-confidence-decay's chain-level additive log-confidence decomposition. This segment states the uniqueness theorem, derives it, and explains how it positions log-odds as the natural parameterization for AAT's continuous-gradient edge-update machinery.

### Setup

Let $p \in (0, 1)$ denote a scalar Bernoulli credence (the probability that a proposition is true) and let $\psi : (0, 1) \to \mathbb{R}$ be a smooth, strictly monotone reparameterization. Consider a sequence of independent Bernoulli observations $y_1, \ldots, y_n \in \{0, 1\}$ drawn from a channel with likelihood ratio $P(y \mid H_1) / P(y \mid H_0)$.

**Evidential-additivity axiom.** The posterior update, applied to a single observation $y$, takes the form

*[Assumption (evidential-additivity axiom)]*

$$\psi(p_{\text{post}}) = \psi(p_{\text{prior}}) + g(y)$$

for some function $g : \{0, 1\} \to \mathbb{R}$ that depends only on the observation $y$ — not on $p_{\text{prior}}$ nor on observation history.

### Theorem

*[Derived (evidential-additivity uniqueness of log-odds, conditional on the axiom above)]*

**Theorem.** The functional equation above admits solutions if and only if

$$\psi(p) = c \cdot \log\!\frac{p}{1 - p} + d$$

for constants $c \gt 0$ and $d \in \mathbb{R}$, with $g(y) = c \cdot \ell(y)$ where $\ell(y) = \log[P(y \mid H_1) / P(y \mid H_0)]$ is the log-likelihood ratio.

### Derivation

*[Derived (Proof Step: Bayesian form of the update)]*

By Bayes' theorem applied to binary hypotheses,

$$\frac{p_{\text{post}}}{1 - p_{\text{post}}} = \frac{p_{\text{prior}}}{1 - p_{\text{prior}}} \cdot \frac{P(y \mid H_1)}{P(y \mid H_0)}$$

Taking the logarithm of both sides and writing $h(p) := \log(p / (1 - p))$,

$$h(p_{\text{post}}) = h(p_{\text{prior}}) + \ell(y)$$

So $\psi = h$ trivially satisfies the axiom with $g = \ell$.

*[Derived (Proof Step: uniqueness by Cauchy functional equation)]*

Suppose $\psi$ is any smooth, strictly monotone reparameterization satisfying the axiom. Since the Bayesian mapping $p_{\text{prior}} \mapsto p_{\text{post}}$ is fully determined by $y$ through the likelihood ratio, the difference $\psi(p_{\text{post}}) - \psi(p_{\text{prior}})$ depends only on $y$, and by the axiom must equal $g(y)$.

Change variables via $\lambda = h(p) = \log(p/(1-p))$ and define $\Psi(\lambda) := \psi(\sigma(\lambda))$ where $\sigma(\lambda) = 1 / (1 + e^{-\lambda})$ is the logistic sigmoid. The axiom becomes

$$\Psi(\lambda + \ell(y)) - \Psi(\lambda) = g(y) \quad \text{for all } \lambda \in \mathbb{R},\, y \in \{0, 1\}$$

Extending to continuous-valued evidence (or considering mixtures of Bernoulli channels with varying likelihood ratios, which span all of $\mathbb{R}$ in the $\ell$-value space), the identity

$$\Psi(\lambda + \ell) - \Psi(\lambda) = G(\ell) \quad \text{for all } \lambda, \ell \in \mathbb{R}$$

holds for a function $G$ independent of $\lambda$. This is the Cauchy functional equation (translation-additivity). Combined with the smoothness assumption on $\psi$, the unique solution class is $\Psi(\lambda) = c \cdot \lambda + d$ for constants $c$ and $d$ (Aczél 1966, *Lectures on Functional Equations and Their Applications*, §2.1).

*[Derived (Proof Step: determining the constants)]*

Strict monotonicity of $\psi$ forces $c \ne 0$. Taking $\psi$ to have the same monotonicity sense as $p \mapsto p$ (credence increasing with $\psi$), we need $c \gt 0$. Thus $\psi(p) = c \cdot h(p) + d = c \cdot \log(p / (1 - p)) + d$, and $g(y) = c \cdot \ell(y)$.

This completes the proof. $\square$

### Three-Layer Parallel

*[Discussion (three-layer additive decomposition)]*

The evidential-additivity axiom is the update-level instance of an additive-decomposition principle that AAT has already committed to at two prior layers:

| Layer | Quantity decomposed | Decomposition form | Source |
|---|---|---|---|
| **Chain level** | Confidence along a causal chain | $\log P(\text{chain}) = \sum_i \log P(E_i \mid E_{\lt i})$ | #der-chain-confidence-decay |
| **Divergence level** | Mismatch between optimal and strategy policies | $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ decomposes additively across DAG layers along the optimal trajectory | #deriv-strategy-cost-regret-bound §6.1 |
| **Update level** | Credence evolution under independent evidence | $\psi(p_{\text{post}}) - \psi(p_{\text{prior}}) = g(y_1) + \cdots + g(y_n)$ for $n$ observations, with $\psi =$ log-odds | This segment |

Each layer forces a logarithmic coordinate through essentially the same structural move: products of independent factors become sums on a log scale. At the chain level, $p^n \to n \log p$; at the divergence level, $\prod Q \to \sum \log Q$; at the update level, $\prod \text{LR} \to \sum \log \text{LR}$. The three are the same transform applied to different quantities.

### Interpretation for the Edge-Update Machinery

*[Discussion (operational consequence)]*

For edge credence $p_{ij}$ with log-odds $\lambda_{ij} = \log(p_{ij} / (1 - p_{ij}))$, the Bayesian update under independent Bernoulli evidence is

$$\lambda_{ij}^{\text{post}} = \lambda_{ij}^{\text{prior}} + \ell(y)$$

where $\ell(y)$ is the per-observation log-likelihood ratio.

**Two operational consequences that follow from the uniqueness theorem:**

1. **Domain unboundedness.** The log-odds coordinate has domain $\mathbb{R}$, not $[0, 1]$. Additive updates cannot escape the domain, regardless of update magnitude. The probability-space presentation $p_{ij} \in [0, 1]$ is the projected image of the log-odds coordinate, obtained via $p_{ij} = \sigma(\lambda_{ij})$ at the readout interface.

2. **Invariance under the chain of causal reasoning.** Because the log-odds coordinate is the unique additive evidence coordinate, evidence accumulated along one edge in a strategy DAG can be composed with evidence accumulated along another edge by addition in the log-odds vector space, provided the evidence is conditionally independent. The Beta-Bernoulli moment-parameter form $\hat p = \alpha / (\alpha + \beta)$ is the projected image, where $\alpha, \beta$ are the cumulative sufficient statistics in exponential-family form.

These consequences are why the continuous-gradient edge-update machinery in #disc-credit-assignment-boundary is well-posed globally in log-odds but exhibits the Finding 2 mechanical break (unbounded updates pushing credences outside $[0, 1]$) when stated directly in probability space.

### Scope Condition

*[Scope (evidential-additivity scope)]*

The evidential-additivity axiom applies to agent classes that treat observations as independent Bernoulli likelihood evidence — the Bayesian-coherent sub-scope of AAT. Non-Bayesian agents (PID controllers, rule-based systems, human judgment per #emp-update-gain) do not invoke likelihood-ratio accumulation and are outside the axiom's scope. This matches the sub-scope $\alpha$ / sub-scope $\beta$ partition in #der-gain-sector-bridge (see also `spikes/spike-a2-prime-strengthening.md`): the uniqueness applies within sub-scope $\alpha$, where B1 (directional fidelity) is already derived from Bayesian coherence.

For multinomial / categorical edge credences with $K \gt 2$ outcomes, the analog is softmax / canonical exponential-family parameters: the softmax natural parameters $\eta_k = \log \pi_k$ (up to a reference-class shift) satisfy the same evidential-additivity axiom. The Bernoulli case ($K = 2$) collapses to log-odds.

---



## Derivation: Adaptive-Gain Dynamics — A2' Under a Learning Gain

- **Slug**: `deriv-adaptive-gain-dynamics`
- **Type**: derivation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `emp-update-gain`, `der-gain-sector-bridge`, `deriv-gain-sector`, `deriv-sector-condition`, `result-sector-condition-stability`, `result-sector-persistence-template`, `der-recursive-update`

AAT's gain structure ( #emp-update-gain, #der-gain-sector-bridge) derives the optimal gain $\eta^\ast$ per regime — the gain is a function of the noise model, chosen to minimize one-step mismatch variance. Real adaptive agents often *learn the noise model itself* (adaptive Kalman), *switch regimes* (IMM), *adapt step-size online* (RMSProp / Adam), or *optimize gain across tasks* (MAML). The gain becomes a state variable with its own update dynamics. The question is whether the sector-persistence machinery extends to this case, and where inside the A2' sub-scope partition adaptive gain sits. The result: sub-scope $\alpha$ splits into $\alpha_1$ (fixed-gain per Prop B.3) and $\alpha_2$ (adaptive-gain under four derivable conditions named (MG-1)–(MG-4)), with sub-scope $\beta$ catching the rest. The two-timescale argument is an augmented-state Lyapunov composition (standard Khalil Thm 4.18), not a Tikhonov reduction — the primary and meta-gain sector conditions compose rather than one being eliminated.

### Augmented-state setup

Treat the gain $K_t$ as state. Define $\tilde K_t = K_t - K^\ast$ (error relative to a target optimal gain, specified per case: Riccati-steady-state for adaptive Kalman, EMA-fixed-point for RMSProp, etc.). The augmented state is $z_t = (\delta_t, \tilde K_t)$. Primary and meta-gain dynamics:

$$\dot\delta = -F(\delta; K^\ast + \tilde K) + w(t), \qquad \dot{\tilde K} = -\Phi(\tilde K, \delta) + v(t)$$

where $F$ is the primary correction function (depending on the current gain via its argument), $\Phi$ is the gain-update contraction, $w$ is primary-channel disturbance, $v$ is gain-channel disturbance (estimator noise, innovation variability, etc.).

### Meta-gain sector conditions (MG-1)–(MG-4)

*[Formulation (meta-gain-conditions, extend A2' to adaptive-gain setting)]*

**(MG-1) Primary sector floor under bounded gain error.** There exist $\underline\alpha \gt 0$ and $r_K \gt 0$ such that for all $\lVert\tilde K\rVert \leq r_K$ and $\lVert\delta\rVert \leq R$:

$$\delta^T F(\delta; K^\ast + \tilde K) \geq \underline\alpha \lVert\delta\rVert^2$$

— A2' uniform in the gain-error ball. The sector floor is preserved across the gain-state range the meta-learner visits.

**(MG-2) Meta-gain sector condition.** The gain-update map $\Phi$ satisfies (T1) (zero at $\tilde K = 0$) and a local sector bound:

$$\tilde K^T \Phi(\tilde K, \delta) \geq \alpha_K \lVert\tilde K\rVert^2 \quad \text{for } \lVert\tilde K\rVert \leq r_K, \text{ uniformly in } \lVert\delta\rVert \leq R$$

with $\alpha_K \gt 0$. This is a sector condition in the gain-error state — the adaptive-gain analog of A2' itself.

**(MG-3) Timescale separation.** $\alpha_K \ll \underline\alpha$. The gain adapts slower than the primary state contracts. This is #der-temporal-nesting's convergence constraint transcribed onto Lyapunov decay rates instead of event rates.

**(MG-4) Coupling boundedness.** The gain-channel disturbance $v(t)$ has bounded contribution from the primary state:

$$\mathbb E[\lVert v(t)\rVert^2 \mid \delta] \leq \sigma_{K,0}^2 + c_v \lVert\delta\rVert^2$$

for some $c_v \geq 0$. (MG-4) with $c_v = 0$ is clean two-timescale decoupling; $c_v \gt 0$ is $\delta$-coupled meta-gain disturbance (RMSProp near minimizer), requiring fixed-point closure.

### Composed persistence result

*[Derived (augmented-state-persistence, from sector-persistence-template applied twice with coupling)]*

Under (MG-1)–(MG-4), the augmented state $z = (\delta, \tilde K)$ is ultimately bounded in mean square. The Lyapunov candidate $V(z) = \tfrac{1}{2}\lVert\delta\rVert^2 + \tfrac{c}{2}\lVert\tilde K\rVert^2$ for appropriate weight $c$ satisfies, along trajectories:

$$\dot V \leq -\underline\alpha \lVert\delta\rVert^2 - c\alpha_K \lVert\tilde K\rVert^2 + \rho\lVert\delta\rVert + c(\sigma_{K,0} + \sqrt{c_v}\lVert\delta\rVert)\lVert\tilde K\rVert$$

Complete-the-square on the cross term (requires $c\sqrt{c_v}$ small compared to $\underline\alpha \cdot c\alpha_K$, i.e., (MG-3) timescale separation plus (MG-4) coupling smallness):

$$\dot V \leq -\tfrac{\underline\alpha}{2}\lVert\delta\rVert^2 - \tfrac{c\alpha_K}{2}\lVert\tilde K\rVert^2 + \frac{\rho^2}{2\underline\alpha} + \frac{c\sigma_{K,0}^2}{2\alpha_K}$$

Standard Lyapunov ultimate-boundedness (Khalil 2002 Thm 4.18) applied to the augmented state gives the composed persistence bound. Both $\delta$ and $\tilde K$ are ultimately bounded with explicit bounds in $(\underline\alpha, \alpha_K, \rho, \sigma_{K,0}, c_v)$. $\square$

### A2' sub-scope partition: $\alpha_1$ / $\alpha_2$ / $\beta$

*[Formulation (sub-scope-refinement)]*

The adaptive-gain analysis refines #form-sector-condition's A2' sub-scope partition into three tiers:

**Sub-scope $\alpha_1$ — fixed-gain, A2' derived.** #der-gain-sector-bridge Prop B.3's current scope: the gain $K$ is treated as a static function of fixed noise model parameters. A2' is derived from B1 directional fidelity. Covers Kalman with known $(Q, R)$, conjugate-Bayesian updates, exponential-family MLE, linear correction with PD $KH$, strongly-convex-gradient fixed-step-size.

**Sub-scope $\alpha_2$ — adaptive-gain, A2' derived through augmented-state Lyapunov.** When (MG-1)–(MG-4) hold with all four conditions derivable from the update-rule structure:

- Adaptive Kalman with Mehra-type innovation-based $(Q, R)$ estimator under timescale separation
- RMSProp/Adam with strongly-convex loss, large $\beta$ (slow EMA), and coupling-smallness; AMSGrad fix (Reddi et al. 2018) structurally a meta-gain repair preserving (MG-1)
- Any adaptive-gain scheme admitting a clean (MG-1)–(MG-4) derivation from the update rule

For these, A2' is derived at the augmented-state level, not merely assumed. Setting $\tilde K \equiv 0$ recovers sub-scope $\alpha_1$ cleanly.

**Sub-scope $\beta$ — A2' assumed (possibly under scope narrowing).** When any of (MG-1)–(MG-4) must be assumed per-agent rather than derived. Concrete instances:

- MAML outer loop: meta-loss non-convex even under per-task convexity (Fallah et al. 2020), so (MG-2) cannot be derived from per-task structure. Inner loop is $\alpha_1$; outer loop is $\beta$.
- IMM regime transitions: (MG-1) fails uniformly in time during posterior-reconcentration windows of duration $\tau_{\text{IMM}}$. Between-transition regime is $\alpha_2$; across-transition window is $\beta$ (scope narrowing via dwell-time + impulsive-disturbance absorption).
- Adam without AMSGrad on ill-conditioned problems: (MG-1) fails under aggressive-$\beta$ + small-gradient-noise (Reddi et al. 2018 counterexample).
- Rule-based / PID / human-judgment adaptive gains: no structural argument for either (MG-1) or (MG-2); both must be assumed.

This refinement preserves the existing A2' sub-scope $\alpha$ as a specialization ($\alpha_1$) and identifies a derivable adaptive-gain extension ($\alpha_2$) with honest fallback to $\beta$ when the derivability conditions fail.

### Structured cases

*[Derivation (case-adaptive-kalman-alpha2)]*

**Case A — Adaptive Kalman with Mehra estimator.** Scalar linear-Gaussian setting with unknown $(Q^\ast, R^\ast)$. The innovation-based Mehra estimator (Mehra 1970, 1972; Dunik et al. 2021 for identifiability) yields $\hat Q_t, \hat R_t$ from a sliding-window autocorrelation of the innovation sequence. For window length $N$, the gain-update map to first order in $\tilde K$ is a scalar Ornstein-Uhlenbeck process:

$$\tilde K_{t+1} = (1 - \lambda_N) \tilde K_t + \lambda_N \eta_t^{\text{inn}}$$

with $\lambda_N \asymp 1/N$ (contraction rate set by window length) and $\eta^{\text{inn}}$ zero-mean innovation noise with variance $O(1/N)$. This is itself an instance of #result-sector-persistence-template with:

- (T1): $\Phi_K(0) = 0$ — when gain is optimal, estimator returns optimal in expectation.
- (T2): $\tilde K \cdot \Phi_K(\tilde K) = \lambda_N \tilde K^2$, so $\alpha_K = \lambda_N$.
- (T3-S): bounded stochastic disturbance on the gain channel.

Prop A.1S applied to the meta-gain channel gives $R^\ast_{S,K} \asymp 1/\sqrt N$ — the classical Mehra asymptotic rate, now derived from (MG-2). Primary sector floor is preserved: $\underline\alpha = K^\ast - \lvert\tilde K\rvert_{\max}$ via triangle. Composed persistence via augmented-state Lyapunov gives $O(1/\sqrt N)$ degradation from the fixed-gain case. **This case is derived at sub-scope $\alpha_2$.**

Under Mehra non-identifiability (rank-deficient transform matrix; see Zagrobelny-Rawlings 2015, Dunik et al. 2021), (MG-2) fails structurally — an instance of the #disc-identifiability-floor pattern on the meta-gain channel.

*[Derivation (case-rmsprop-alpha2-conditional)]*

**Case B — RMSProp on strongly-convex loss.** The per-step effective step is $\eta_t^{\text{eff}} = \eta_t/(\sqrt{v_t} + \varepsilon)$ where $v_t = \beta v_{t-1} + (1-\beta)\hat g_t^2$ tracks the second moment. Near the minimizer, $\mathbb E[\hat g_t^2] \to \lVert\nabla L\rVert^2 + \sigma_g^2$. Writing $\tilde v_t = v_t - \mathbb E[\hat g_t^2]$:

$$\tilde v_{t+1} = \beta \tilde v_t + (1-\beta)(\hat g_t^2 - \mathbb E[\hat g_t^2]) + \beta(\mathbb E[\hat g_{t-1}^2] - \mathbb E[\hat g_t^2])$$

The first two terms give (MG-2) with $\alpha_v = 1 - \beta$ and $\sigma_v^2 \asymp (1-\beta)^2 \text{Var}(\hat g_t^2)$. The third is $\delta$-coupled: $\mathbb E[\hat g_t^2]$ depends on $\delta$ through $\lVert\nabla L\rVert^2$, giving $c_v \gt 0$ in (MG-4).

Composed persistence under design conditions $\beta$ close to 1 (slow EMA) and $\lambda_{\max}(H) \cdot R^\ast_S \ll \sqrt{\sigma_g^2}$ (coupling smallness): fixed-point closure between primary $R^\ast_S$ and meta-gain $R_v$ yields existence of a stable equilibrium. Sub-scope $\alpha_2$ under design conditions.

Outside those conditions (aggressive $\beta$ + ill-conditioning + small gradient noise — Reddi et al. 2018's Adam counterexample), fixed-point iteration diverges. **AMSGrad's monotonicity on $v_t$ is structurally a meta-gain repair that restores (MG-1) by construction** — preserving sub-scope $\alpha_2$ by forcing a condition (MG-1) the vanilla algorithm would violate.

*[Sketch (case-imm-alpha2-plus-dwelltime)]*

**Case C — IMM / regime-switching Kalman.** Mixture of $M$ Kalman filters with Markov-transition posterior over regimes. Between regime transitions, the posterior concentrates on the true regime and the effective gain approaches the regime-conditional optimum: sub-scope $\alpha_2$ in the steady portion with Mehra-style derivation. Across regime transitions, posterior re-concentration takes $\tau_{\text{IMM}} \asymp 1/(1-p)$ observations (self-loop probability $p$); during this window (MG-1) fails uniformly in time — the gain can be aligned with the wrong regime. Scope narrowing via dwell-time + impulsive-disturbance absorption: regime stable for $T_{\text{dwell}} \gg \tau_{\text{IMM}}$, transient mismatch bounded by counting-argument. Sub-scope $\alpha_2$ between-transition; $\beta$ across-transition.

*[Classification (case-maml-mixed)]*

**Case D — MAML inner-outer structure.** Inner loop (per-task adaptation with $k$ gradient steps) — sub-scope $\alpha_1$ from Prop B.4 under per-task convexity. Outer loop (meta-parameter update via gradient on meta-loss $\sum_i L_i(\theta_i'(\theta))$) — Fallah et al. 2020's convergence analysis shows the meta-loss is non-convex even under per-task convexity because of the non-linearity of inner-loop updates in $\theta$. (MG-2) is not derivable from per-task structure. Outer loop is $\beta$ — A2' assumed per basin.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Augmented-state setup $z = (\delta, \tilde K)$ with coupled sector dynamics | Definitional reformulation extending #der-recursive-update + #emp-update-gain | Formulation choice |
| (MG-1) primary sector floor under bounded gain error | Derived in Cases A and B via triangle / $\varepsilon$-floor arguments | Derived (per case, conditional on regularity) |
| (MG-2) meta-gain sector condition | Derived in Cases A (Mehra OU) and B (EMA second-moment) from estimator structure | Derived (per named case) |
| (MG-3) timescale separation $\alpha_K \ll \underline\alpha$ | Design condition on estimator window / EMA rate; Lyapunov decay-rate transcription of #der-temporal-nesting | Formulation (design condition; violations dissolve composition) |
| (MG-4) coupling boundedness of gain-channel disturbance | Decoupled ($c_v = 0$) in Case A; $\delta$-coupled ($c_v \gt 0$) in Case B with fixed-point closure | Derived (per case) |
| Composed augmented-state persistence under (MG-1)–(MG-4) | Quadratic Lyapunov on $z$ + Khalil 2002 Thm 4.18 ultimate-boundedness | Derived (conditional on MG-1 through MG-4) |
| Sub-scope refinement $\alpha_1$ / $\alpha_2$ / $\beta$ | Extension of current #deriv-sector-condition $\alpha/\beta$ partition | Formulation (classification) |
| $\alpha_2$ reduces to $\alpha_1$ under $\tilde K \equiv 0$ | Direct substitution into augmented-state setup | Proved |
| Case A (adaptive Kalman): sub-scope $\alpha_2$ under identifiability + window-length timescale separation | Mehra OU-form of estimator + Prop A.1S | Derived |
| Case B (RMSProp): sub-scope $\alpha_2$ under design conditions; $\beta$ otherwise; AMSGrad as meta-gain repair | EMA second-moment derivation + fixed-point closure + Reddi et al. 2018 counterexample | Derived (conditional); AMSGrad framing is discussion |
| Case C (IMM): sub-scope $\alpha_2$ between-transition + $\beta$ across-transition via dwell-time | Posterior re-concentration + impulsive-disturbance absorption | Sketch |
| Case D (MAML): inner-loop $\alpha_1$ + outer-loop $\beta$ | Fallah et al. 2020 meta-loss non-convexity | Classification (not derivation) |
| Mehra non-identifiability as meta-gain #disc-identifiability-floor instance | Rank-deficient transform matrix blocks (MG-2) derivation | Discussion (candidate floor instance) |

---



## Derivation: Update Detection Latency Under Accumulated Experience

- **Slug**: `deriv-update-detection-latency`
- **Type**: derivation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `deriv-edge-update-natural-parameter`, `disc-credit-assignment-boundary`, `schema-strategy-persistence`, `deriv-edge-credence-dynamics`

For a Beta-Bernoulli strategy-edge agent without forgetting, the expected number of cycles required to detect a within-class regime change of observable footprint $\varepsilon$ scales as $\Omega((n_{\min}+1)/\varepsilon)$ with $n_{\min}$ the minimum accumulated pseudo-count on load-bearing edges. The $1/(n+1)$ rate is **structurally forced** — it is the log-odds update magnitude per cycle under #deriv-edge-update-natural-parameter's Aczél-Cauchy-FE uniqueness theorem, and no choice of coordinate escapes it. The result sharpens #schema-strategy-persistence's forgetting prerequisite from "required for asymptotic persistence" to "required for detection-latency bounded independently of operating point." The broader myopia observation — that successful, high-capability organizations systematically underinvest in detecting regime changes that would require structural adaptation — admits a complementary decision-theoretic account via #disc-exploit-explore-deliberate's oracle analysis; this segment's contribution is the signal-side lower bound, not the decision-side account.

### Setup

An agent with a Beta-Bernoulli strategy DAG per #schema-strategy-persistence / #deriv-edge-credence-dynamics, credit assignment via the log-odds signal of #disc-credit-assignment-boundary (forced by #deriv-edge-update-natural-parameter), and no forgetting ( $\lambda = 1$, pseudo-counts $n_k$ accumulate monotonically). Let $E_{\text{load}}$ denote the load-bearing edges on the current active plan; $n_{\min} = \min_{k \in E_{\text{load}}} n_k$. The agent has been operating with model-class fitness $\mathcal F(\mathcal M)$ near $1$, adaptive reserve $\Delta\rho^\ast \gt 0$, control regret $\delta_{\text{regret}}$ small — a high-operating-point configuration.

At cycle $t_0$, a regime change occurs within the current model class (a true edge probability shifts by $\varepsilon$; the L0 graph remains correct; the agent's model class still suffices). This is case R1 in the spike taxonomy — a within-class drift change. Other regime-change cases (R2 model-class inadequacy; R3 L0→L1 structural transition) are deferred to Working Notes and #disc-identifiability-floor respectively.

### Detection-latency theorem

*[Derived (detection-latency-R1, from edge-update-natural-parameter + deriv-edge-credence-dynamics)]*

**Proposition.** Under the setup, the expected number of cycles $T_{\text{detect}}$ required for the log-odds coordinate on any load-bearing edge $k \in E_{\text{load}}$ to cross a fixed detection threshold $\Delta\lambda_{\text{detect}}$ in response to the regime change satisfies

$$\boxed{\;\mathbb E[T_{\text{detect}}] \;=\; \Omega\!\left(\Delta\lambda_{\text{detect}} \cdot (n_{\min} + 1) / \varepsilon\right)\;}$$

**Derivation.** The default signal function of #disc-credit-assignment-boundary (under the log-odds coordinate forced by #deriv-edge-update-natural-parameter) updates an edge's log-odds credence by

$$\lambda_k^{\text{new}} = \lambda_k + \eta_{\text{edge}} \cdot \iota_k \cdot J_k \cdot (y_G - \hat P_\Sigma) / \lVert\mathbf J\rVert^2$$

with $\eta_{\text{edge}} = 1/(n_k + 1)$ for Beta-Bernoulli (Prop B.4 of #deriv-edge-credence-dynamics). Per-cycle the expected log-odds update magnitude is bounded:

$$\mathbb E\lvert\Delta\lambda_k\rvert \;\leq\; \frac{\lvert J_k\rvert \cdot \mathbb E\lvert y_G - \hat P_\Sigma\rvert}{\lVert\mathbf J\rVert^2 \cdot (n_k + 1)}$$

Under regime change R1 with observable footprint $\varepsilon$, the expected systematic residual $\mathbb E\lvert y_G - \hat P_\Sigma\rvert = \Theta(\varepsilon)$ as $\varepsilon \to 0$ (the misspecified-edge residual is proportional to the edge's probability shift, via the linearization of the Bernoulli likelihood in a neighborhood of the pre-change parameter). Combining: the per-cycle expected log-odds increment on load-bearing edges is $O(\varepsilon/(n_{\min}+1))$.

For the agent to cross $\Delta\lambda_{\text{detect}}$, expected cycles required is at least $\Delta\lambda_{\text{detect}} / (O(\varepsilon/(n_{\min}+1)))$ = $\Omega(\Delta\lambda_{\text{detect}} \cdot (n_{\min}+1) / \varepsilon)$. $\square$

### The rate is structurally forced

*[Observation (rate-forced-by-aczel)]*

The $1/(n+1)$ scaling is not a property of the specific update rule choice. Per #deriv-edge-update-natural-parameter, the log-odds coordinate is the *unique* additive-evidence coordinate satisfying the evidential-additivity axiom — the Aczél 1966 Cauchy-functional-equation uniqueness theorem forces it up to positive affine transformation. In this forced coordinate, the per-cycle increment for Beta-Bernoulli edges is forced to be $O(1/(n+1))$: the Fisher-equivalent statement holds in any sensible coordinate. Rearranging the update to a different scale does not change the rate — it just changes the units in which the rate is measured.

The forcing composition:

1. #deriv-edge-update-natural-parameter forces the log-odds coordinate via evidential additivity.
2. In that coordinate, Beta-Bernoulli accumulation gives $\eta_{\text{edge}} = 1/(n+1)$.
3. Therefore the per-cycle update magnitude is structurally forced at $O(1/(n+1))$.

This is the specific link between AAT's constructive meta-pattern ( #disc-additive-coordinate-forcing, via #deriv-edge-update-natural-parameter's theorem) and a downstream detection-latency consequence. The rate cannot be escaped without abandoning evidential additivity — which would invalidate the update rule on AAT-internal grounds, not merely operational ones.

### Sharpening the forgetting prerequisite

*[Corollary (forgetting-as-latency-bound, sharpens #schema-strategy-persistence)]*

#schema-strategy-persistence derives the forgetting prerequisite $(1-\lambda) \gt \rho_\Sigma/R_\Sigma$ as required for *asymptotic persistence* — without forgetting, $\alpha_\Sigma = 1/(n+1) \to 0$ and persistence eventually fails. The detection-latency theorem sharpens this to a **load-bearing claim about detection latency on the way to asymptotic failure**:

**Forgetting is required not only for asymptotic persistence, but also for detection latency to be bounded independently of operating point.** Without forgetting, $n_{\min}$ grows monotonically, and $\mathbb E[T_{\text{detect}}]$ grows linearly with $n_{\min}$. With forgetting at rate $\lambda \lt 1$, the effective pseudo-count $n_{\text{eff}} = 1/(1-\lambda)$ is bounded, and the detection latency caps at $\Omega(1/((1-\lambda)\varepsilon))$ regardless of how long the agent has been operating.

This dualizes #schema-strategy-persistence's asymptotic claim: forgetting is operationally load-bearing at every step, not only in the limit. An agent with the right $\lambda$ has bounded detection latency throughout its lifetime; an agent with $\lambda = 1$ has detection latency that grows unboundedly with experience, producing the phenomenon of stability-induced myopia in practice.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| R1 detection-latency theorem $\mathbb E[T_{\text{detect}}] = \Omega((n_{\min}+1)/\varepsilon)$ | #deriv-edge-update-natural-parameter log-odds coordinate + #deriv-edge-credence-dynamics Prop B.4 $\eta_{\text{edge}} = 1/(n+1)$ + Pinsker-type linearization | Derived (conditional on Beta-Bernoulli + log-odds + no forgetting) |
| $1/(n+1)$ rate structurally forced | Composition of #deriv-edge-update-natural-parameter's Aczél-Cauchy-FE theorem with Beta-Bernoulli accumulation | Proved (conditional on evidential-additivity axiom) |
| Sharpening of forgetting prerequisite from asymptotic persistence to bounded detection latency | #schema-strategy-persistence + this theorem | Derived |
| R2 model-class inadequacy sub-case (C1-diagnostic blindness under misspecification) | Common-mode-bias argument on $A_O^{(1)}$ vs $V_O(\pi_{\text{current}})$ | Discussion (sketch; see Working Notes) |
| R3 L0→L1 structural transition sub-case | Direct application of #disc-identifiability-floor Instance 1 — already derived there | Reference (not new content) |
| Probability-of-deferral bound | Derivable from the expected-time bound via Markov inequality | Discussion |
| Connection to institutional inertia / Christensen / competency traps | Stability-induced-myopia as a mechanism for the empirical pattern | Discussion |
| Connection to IDT sidecar monitoring (Hafez et al. 2026 89% vs 44%) | On-policy reward-based monitoring is the log-odds accumulator; IDT bi-predictability is a change-detector that bypasses the $1/(n+1)$ rate | Discussion |

---
