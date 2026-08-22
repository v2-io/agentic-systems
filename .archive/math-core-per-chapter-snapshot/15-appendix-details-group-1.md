# Appendix — Details (group 1)


## Derivation: No Horizon-Independent Non-Exit Bound Under Additive Stochastic Forcing (the Model-S No-Go)

- **Slug**: `deriv-stochastic-non-exit`
- **Type**: derivation
- **Status**: exact
- **Stage**: draft
- **Depends**: `deriv-sector-condition`, `result-sector-condition-stability`, `result-structural-adaptation-necessity`

Under additive stochastic forcing there is no finite bound on the infinite-horizon first-exit probability — $P(\tau_R \lt \infty) = 1$ for every correction strength — and the natural maximal-inequality route to one provably cannot exist; this is the load-bearing proof step behind Prop A.1S(iii′)/(iv) and the Model-S half of Corollary A.1S.1.

**Setup.** Mismatch dynamics under additive stochastic disturbance, started inside the sector-condition region $\mathcal B_R$:

$$d\delta = -F(\mathcal T, \delta)\,dt + \sigma_w\,dW_t, \qquad \delta(0) \in \mathcal B_R,\quad \sigma_w \gt 0,$$

with $W_t$ a standard $n$-dimensional Wiener process, (A2') $\delta^\top F \geq \alpha\lVert\delta\rVert^2$ on $\mathcal B_R$, and $\tau_R = \inf\{t : \lVert\delta(t)\rVert \gt R\}$ the first-exit time. Let $V = \tfrac12\lVert\delta\rVert^2$.

**Theorem (Model-S no-go).** *[Derived]* For every $\alpha \gt 0$, every $\sigma_w \gt 0$, and every correction function $F$ satisfying (A2'),

$$P(\tau_R \lt \infty) = 1,$$

and there exists no nonnegative supermartingale dominating $V$ that certifies a horizon-independent bound $P(\tau_R \lt \infty) \leq c \lt 1$. Pathwise containment of $\mathcal B_R$ is unattainable under additive stochastic forcing at any correction strength.

**Why the natural route cannot work.** The route a careful reader reaches for first is a time-uniform maximal inequality (Ville / Doob) on an Itô–Lyapunov supermartingale — the same instinct that makes the fixed-time mean-square bound (Prop A.1S(i)) succeed. It fails, and the failure is structural, not a matter of a missing trick.

Define $G(t) = e^{2\alpha t} V(\delta(t))$. On $[0, \tau_R]$, by Itô and (A2'),

$$dG = e^{2\alpha t}\big[\underbrace{(2\alpha V - \delta^\top F)}_{\leq\, 0 \text{ on } \mathcal B_R}\,dt + \tfrac n2\sigma_w^2\,dt + \delta^\top\sigma_w\,dW_t\big] \;\leq\; e^{2\alpha t}\tfrac n2\sigma_w^2\,dt + e^{2\alpha t}\delta^\top\sigma_w\,dW_t.$$

$G$ is **not** a supermartingale: the $+\,e^{2\alpha t}\tfrac n2\sigma_w^2\,dt$ term has strictly positive drift growing exponentially. Removing it by compensation gives

$$S(t) = e^{2\alpha(t\wedge\tau_R)}V(\delta_{t\wedge\tau_R}) - \frac{n\sigma_w^2}{4\alpha}\big(e^{2\alpha(t\wedge\tau_R)} - 1\big),$$

and $dS \leq e^{2\alpha t}\delta^\top\sigma_w\,dW_t$ on $[0,\tau_R]$ — so $S$ *is* a supermartingale. **But $S$ is not nonnegative.** The subtracted $\tfrac{n\sigma_w^2}{4\alpha}(e^{2\alpha t}-1)$ dominates $e^{2\alpha t}V$ whenever $V(\delta(t)) \lt \tfrac{n\sigma_w^2}{4\alpha}$ — i.e. exactly inside the persistence basin, which under the mean-square persistence condition is *most of the time* (that condition places the RMS radius $R^\ast_S = \sigma_w\sqrt{n/2\alpha}$ well inside $\mathcal B_R$, so $V \ll \tfrac{n\sigma_w^2}{4\alpha}$ typically). Ville's inequality requires a nonnegative supermartingale; Doob's maximal inequality a nonnegative sub/supermartingale. Both are inapplicable to a sign-indefinite $S$, and the obstruction is not removable: for additive non-degenerate Brownian forcing the diffusion's scale function is unbounded (the OU scale density $\propto e^{\alpha u^2/\sigma_w^2}$), so the only bounded harmonic functions of the generator are constants — the gambler's-ruin / Lyapunov-exit machinery cannot certify "stays inside forever with positive probability." There is no nonnegative supermartingale dominating $V$ with finite expected initial value that yields a horizon-independent exit bound.

**Why $P(\tau_R \lt \infty)=1$, generally.** The conclusion does not depend on the linear structure. A non-degenerate diffusion (additive forcing $\sigma_w\,dW_t$, $\sigma_w \gt 0$) exits any bounded region in finite time almost surely, for *any* locally bounded drift: near $\partial\mathcal B_R$ the Brownian increment has positive probability of crossing in any time interval, and no finite inward correction satisfying (A2') can suppress this (A2' bounds $\delta^\top F$ from below by $\alpha\lVert\delta\rVert^2$, a finite inward push, not an impassable wall). Hence $\tau_R \lt \infty$ a.s. for every $F$ under (A2'), every $\alpha$, every $\sigma_w$. The Ornstein–Uhlenbeck case is the explicit instance (positively recurrent on $\mathbb R^n$, unbounded stationary support, exits any finite ball a.s.), not the basis.

---



## Derivation: The Self-Actuation Grounding No-Go

- **Slug**: `deriv-self-actuation-grounding`
- **Type**: derivation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `der-orient-cascade`, `def-value-object`, `def-satisfaction-gap`, `def-control-regret`, `form-objective-functional`, `der-directed-separation`, `scope-agent-identity`, `def-agent-spectrum`, `result-persistence-condition`, `disc-continuity-stance`

A self-actuated agent revises its own objective; the invariant that would have to make that revision non-degenerate cannot be constructed from the agent's own objective-side machinery — so the grounding of any well-formed self-actuator is forced onto the non-objective adaptive substrate, where the persistence condition supplies a canonical instance. This is a scoped no-go with a constructive boundary, conditional on three named premises.

**The self-actuation operator.** The orient cascade ( #der-orient-cascade) terminates, when $\delta_{\text{sat}} \gt 0$ persists across $M_t$-correction, policy-class expansion, and convention escalation, in step 5d: *revise $O_t$*. For an **actuated** agent the objective's update source is external ( #def-strategy-dimension: $O_t$ is "assigned, discovered, revised" by a principal) — step 5d exits the agent boundary. A **self-actuated** agent performs step 5d on itself: an operator

$$\mathfrak{A}:\ (M_t,\, O_t,\, \Sigma_t,\, \mathcal{C}_t)\ \longmapsto\ O_t'$$

that revises the objective endogenously — goal autonomy stacked on the solution autonomy ($\Sigma_t$-revision) every actuated agent already has.

**Unconstrained $\mathfrak{A}$ is degenerate.** $O_t$'s sole interface is the value functional $V_{O_t}:\text{trajectories}\to\mathbb{R}$ ( #form-objective-functional) and the satisfaction gap $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O$ ( #def-satisfaction-gap). If $\mathfrak{A}$ may return any $O_t'$, it returns one whose threshold the current trajectory already meets — driving $\delta_{\text{sat}}\to 0$ by moving the target onto the arrow already in flight. This is the formal shadow of wireheading / reward corruption, and it is the generic outcome of an unconstrained $\mathfrak{A}$, not a marginal one. Non-degeneracy therefore requires an invariant $\Phi$ preserved across the revision.

**The question.** Can $\Phi$ be an *agent-internal objective-functional the agent itself self-actuates on*? Make the requirements explicit: $\Phi$ must be **(R1)** value-functional-typed, **(R2)** non-vacuously monotone across revision (a constant everywhere-admissible reading is the trivial indicator the degenerate case already admits), **(R3)** agent-internal and itself self-actuatable, **(R4)** convention- and trajectory-stable (an invariant of the agent, not of the analyst).

**No-go (scoped).**

*[Derived (Conditional on scalar-objective scope, no-primitive-reflective-oracle, and the #der-directed-separation substrate stage)]*

No $\Phi$ satisfying (R1)–(R4) can be constructed from AAT's covered objective-side machinery: the meta-objective tower a non-degenerate $\mathfrak{A}$ would require **cannot be a tower of agent-internal objectives**. Any non-degenerate self-actuator AAT covers must therefore ground on a terminal invariant that is *not* an AAT objective-functional.

The claim is scoped to what the constructions below exhaust; it is not the unscoped "no such object exists" (see Epistemic Status — the universal-over-all-$\Phi$ step is argued, not derived).

**Lemma 1 (objective-functionals carry no convention-invariant infeasibility verdict; static-pointwise, from #def-value-object).** Fix a decision point: a single model $M_\tau$, horizon $N_h$, policy class $\Pi$. By the convention-monotonicity result ( #def-value-object Corollary, the static-evaluation form, `status: exact`),

$$\delta_{\text{sat}}^{\text{B}} \;\leq\; \delta_{\text{sat}}^{\text{RH}} \;\leq\; \delta_{\text{sat}}^{(1)},$$

so the canonical C1 reading $\mathbb{1}[\delta_{\text{sat}}^{(1)} \gt 0]$ holds on a strict superset of the genuinely-infeasible set $\{\delta_{\text{sat}}^{\text{B}} \gt 0\}$ — strictly so on the locally-stuck-but-globally-recoverable objectives ( #def-satisfaction-gap Epistemic Status: "C1 gives the most false 'unattainable' diagnoses"; #der-orient-cascade step 5c). A genuine infeasibility verdict requires the C3/Bellman reading. This is the static-pointwise statement #def-value-object actually supports — its stated preconditions are exactly fixed $M_\tau,N_h,\Pi$, and the segment is explicit that the cross-revision/replanning transfer "does not automatically" hold; that transfer is neither used nor needed here. The pointwise fact — *at any fixed decision point the cheap canonical verdict is not a genuine infeasibility verdict* — is exact and is sufficient.

**Lemma 2 (the in-scope agent cannot evaluate the C3 verdict per step; from #der-directed-separation + #form-objective-functional).** An AAT-covered agent's entire dynamical system is $f_M, f_G, \pi$ with no out-of-band oracle ( #der-directed-separation Formal Expression), on a single non-forkable trajectory ( #scope-agent-identity). The C3 verdict is a global Bellman optimum, generally intractable ( #def-value-object C3; #def-satisfaction-gap Epistemic Status); evaluating it is not a finite per-step operation, and an agent that could not act until it did so would be "stuck, not purposeful" — the disqualification #form-objective-functional Epistemic Status §1 already imposes through its revealed-preference commitment. Hence $\mathbb{1}[\delta_{\text{sat}}^{\text{B}} \gt 0]$ is not available to an in-scope agent as a per-step predicate.

**Assembly.** Suppose $\Phi$ satisfies (R1)–(R4). By (R1)+(R3), $\Phi$ is an AAT objective-functional the agent self-actuates on, so by #form-objective-functional its *sole* theory-visible handle is $V_\Phi$ and the satisfaction/regret apparatus read off it ("the sole interface between $O_t$ and the rest of the theory"). Any monotone property of $\Phi$ the theory can state across revision (R2) must therefore be a statement about $\delta_{\text{sat}}^{\Phi}$ (or $\delta_{\text{regret}}^{\Phi}$, which inherits the identical convention-monotonicity by #def-control-regret) — there is no other channel. Non-vacuity (R2) forces that monotone fact to rest on a *verdict* over $\delta_{\text{sat}}^{\Phi}$; a constant everywhere-admissible reading is exactly the trivial indicator the degenerate case already admits. By (R4) the verdict must be convention-invariant; by Lemma 1 the only convention-invariant infeasibility verdict is the C3 reading. By (R3) the verdict licensing $\Phi$'s own revision must be available to the agent per step; by Lemma 2 it is not. Contradiction. $\square$

The contradiction is the collision of two AAT-internal facts — convention-monotonicity (Lemma 1, #def-value-object) and finite-no-oracle per-step action (Lemma 2, #der-directed-separation + #form-objective-functional Epistemic Status §1). It introduces no new postulate. It is exhibited for the three constructions below, which exhaust the objective-side routes a $\Phi$ could come from:

- **(A)** $\Phi$ as the admissible set's own structure: collapses to the vacuous indicator (fails R2).
- **(B)** $\Phi$ as a cascade-licensing potential: its licensing verdict *is* a $\delta_{\text{sat}}$-verdict, so it inherits the Lemma 1 / Lemma 2 collision.
- **(C)** $\Phi$ as a fresh agent-internal scalar: by (R1)+(R3) it is an AAT objective-functional, hence subject to the same collision one level up — the break is structural in (R1)+(R3), not a regress that "gives up".

### Constructive boundary

**Corollary 1 (necessary form of a terminal grounding invariant).** The contradiction came entirely from $\Phi$ being an AAT objective-functional the agent self-actuates on (R1+R3). Drop that and it dissolves. So a terminal grounding invariant $\Phi^{(K)}$ for a non-degenerate self-actuator must be an object that is **(i) convention-invariant** (its verdict does not move with C1/C2/C3 — escaping Lemma 1), **(ii) agent-available per step** without an oracle (escaping Lemma 2), and **(iii) not an AAT objective-functional the agent self-actuates on** (so it is not subject to the convention split and is genuinely terminal). Equivalently: it lives on the *adaptive/correction substrate* ($M_t$ and the correction dynamics), not the *objective substrate* ($O_t$).

**Corollary 2 (the persistence bound is a canonical terminal grounding invariant).** Structural persistence ( #result-persistence-condition: $\alpha \gt \rho/R$, `type: result, status: exact`) satisfies (i)–(iii):

- **(i) convention-invariant.** Persistence is a Lyapunov property of the correction dynamics on $M_t$ ( #result-persistence-condition Formal Expression), with no continuation-convention argument; C1/C2/C3 are conventions for evaluating *objectives*. The convention split does not reach it.
- **(ii) agent-available per step.** The adaptive reserve $\Delta\rho^\ast = \alpha R - \rho$ ( #result-persistence-condition) is a finite local read the in-scope agent already maintains ( #der-orient-cascade steps 1–2 are the per-step adaptive update), not a Bellman solve. No oracle; no "stuck, not purposeful".
- **(iii) not an AAT objective-functional.** It lives on $M_t$ and the correction machinery; #disc-continuity-stance makes the orthogonality explicit (the persistence machinery acts on $M_t$ and the correction dynamics, formally independent of $O_t$). $\mathfrak{A}$ revises $O_t$; the persistence bound is not in $O_t$, so it sits where $\mathfrak{A}$ structurally cannot reach.

Concretely the terminal invariant is: *do not revise $O_t$ to an objective whose pursuit pushes the operating point outside the persistence region.* An $O_t'$ that breaks $\alpha \gt \rho/R$ is self-defeating — the agent that adopts it cannot maintain bounded mismatch ( #result-persistence-condition Discussion: below the structural threshold "mismatch grows without effective bound") and so cannot reliably satisfy $O_t'$ either.

### What is derived vs. chosen

| Property | Source | Strength |
|---|---|---|
| Unconstrained $\mathfrak{A}$ is degenerate | #form-objective-functional + #def-satisfaction-gap (the $\arg\min$ argument) | Derived |
| Lemma 1 (static-pointwise convention split) | #def-value-object Corollary (static-evaluation form, exact) | Proved (within the fixed-$M_\tau,N_h,\Pi$ scope) |
| Lemma 2 (no per-step C3 verdict) | #der-directed-separation + #form-objective-functional ES §1 | Derived (conditional on the substrate stage) |
| No-go (no objective-side $\Phi$) | Assembly of Lemmas 1–2 | Derived (conditional; scoped to the three exhausted constructions) |
| Corollary 1 (necessary form) | Negation of (R3) in the Assembly | Derived |
| Corollary 2 (persistence bound qualifies) | #result-persistence-condition against (i)–(iii) | Derived (the persistence bound itself is `exact`) |

---



## Result: Sector-Persistence Template

- **Slug**: `result-sector-persistence-template`
- **Type**: result
- **Status**: exact
- **Stage**: draft
- **Depends**: `deriv-sector-condition`

Any state variable evolving under bounded-correction dynamics with bounded disturbance admits the same Lyapunov persistence argument. AAT's persistence-flavored results — epistemic, strategic, team, composite closure, composite tempo, adversarial destabilization, and identity-continuity across turnover — are instances of a single template. This segment states the template once in parameter-free form so that each instantiation can cite it and specify only what varies: its state variable, correction function, effective disturbance rate, and reserve.

*[Template preconditions (sector-persistence-template)]*

Let $\xi(t) \in \mathbb{R}^n$ be a state variable evolving under

$$\frac{d\xi}{dt} = -F(\xi) + w(t)$$

where $F$ is a correction function and $w(t)$ is a disturbance. The template applies when:

**(T1) Zero correction at zero state.** $F(0) = 0$ — no correction is applied when the state is at its target.

**(T2) Local sector condition.** There exist $\alpha \gt 0$ and $R \gt 0$ such that

$$\xi^T F(\xi) \geq \alpha \lVert\xi\rVert^2 \quad \text{for } \lVert\xi\rVert \leq R.$$

The correction points inward with at least baseline efficiency $\alpha$ throughout the region of radius $R$.

**(T3) Bounded disturbance.** Either:

- *Model D (deterministic bound):* $\lVert w(t)\rVert \leq \rho_\xi$, or
- *Model S (stochastic zero-mean):* $\mathbb{E}[\lVert w(t)\rVert^2] = \sigma_\xi^2$ with $w(t)$ a Wiener-process increment.

*[Template result (from sector-condition-derivation Props A.1, A.1S, A.2)]*

Under (T1)–(T3), with $V(\xi) = \tfrac{1}{2}\lVert\xi\rVert^2$ as Lyapunov function:

**Model D.** The state is ultimately bounded by $R^\ast = \rho_\xi / \alpha$. Structural persistence (the ultimate bound fits within the sector-condition region) requires

$$\alpha \gt \frac{\rho_\xi}{R}.$$

The adaptive reserve — the additional disturbance the system can absorb before persistence fails — is $\Delta\rho_\xi^\ast = \alpha R - \rho_\xi$.

**Model S.** The state satisfies $\mathbb{E}[\lVert\xi(t)\rVert^2] \to n\sigma_\xi^2/(2\alpha)$ in mean square, giving RMS bound $R^\ast_S = \sigma_\xi\sqrt{n/(2\alpha)}$. Structural persistence in the mean-square sense requires

$$\alpha \gt \frac{n\sigma_\xi^2}{2R^2}.$$

The Model D result scales as $1/\alpha$; the Model S result scales as $1/\sqrt{\alpha}$ — correction is less effective against noise than against drift. This scaling difference propagates into the adversarial exponent regimes ( #result-adversarial-exponent-regimes): $b = 2$ under Model D, $b = 3/2$ under Model S.

### Instantiations in AAT

The template is invoked across seven segments. Each specifies its own $(\xi, F, \rho_\xi, R)$ and verifies (T1)–(T3) locally:

| Segment | $\xi$ | Effective $\rho_\xi$ | $R$ | Locally-verified precondition |
|---|---|---|---|---|
| #result-persistence-condition | $\delta_t$ (epistemic mismatch) | $\rho$ (environmental disturbance rate) | model-class capacity, or task-adequacy threshold $\lVert\delta_{\text{critical}}\rVert$ if stricter | (T2) via #der-gain-sector-bridge |
| #schema-strategy-persistence | $\delta_\Sigma$ (strategic mismatch) | $\rho_\Sigma$ (rate of edge invalidation) | $R_\Sigma$ (strategic reserve) | (T2) via Beta-Bernoulli edge updates ( #deriv-edge-credence-dynamics Props B.1–B.6); constant-$\alpha$ requires experience discounting |
| #der-team-persistence | $\delta_i$ (sub-agent mismatch) | $\rho_i^{\text{eff}} = \rho_{i,\text{env}} + \sum_j \gamma_{j\to i}^{\text{adv}}\mathcal T_j - \sum_j \gamma_{j\to i}^{\text{coop}}\mathcal T_j$ | $R_i$ | Cooperative coupling can drive $\rho_i^{\text{eff}}$ below the single-agent $\rho$ |
| #form-composition-closure (bridge lemma) | $e_m$ (trajectory error at macro-boundaries $m$) | $\varepsilon^\ast \nu_c$ (closure-defect per macro-step $\times$ macro-update rate) | the composite's $R_c$ | Tier-specific contraction stronger than (T2): incremental sector bound (DA2'-inc). Tier 1 proved; Tier 2 local; Tier 3 domain-specific |
| #der-tempo-composition | $\delta_c$ (composite mismatch) | $\rho_{\text{ext}} + \varepsilon^\ast \nu_c$ (external + internal) | $R_c$ | (T3) requires the bridge-lemma contraction; $C_{\text{coord}} \geq \varepsilon^\ast\nu_c$ is the tempo-equivalent of the internal disturbance |
| #der-adversarial-destabilization | $\delta_B$ (target-agent mismatch) | $\rho_{B,\text{base}} + \gamma_A \mathcal T_A$ (Model D) or $\sigma_{B,\text{base}} + \gamma_A \mathcal T_A$ (Model S) | $R_B$ | Destabilization is the negation of persistence: (T3)'s coupling-amplified disturbance violates $\alpha R \gt \rho_\xi$ |
| #der-identity-continuity-threshold | $g_k$ (identity gap, turnover-indexed) | $\rho_k$ (projected static identity rate-distortion floor, per boundary) | $D_\Delta$ (fidelity-bounded identity-relevant information) | The reflected (Lindley) discrete instantiation on the turnover axis; compensation is relational re-grounding $\varrho_{\text{rg},k}$; Model-S-family, $\mu=0$ driftless boundary load-bearing; conditional under (M-ADD)/(M-FREE)/(C-S) — the $\mathcal A_{\mathrm{refl}}$ operator family (see Discussion) |

The same Lyapunov argument applies in every row. What varies is how each instantiation defines its state variable, its correction function, and — most importantly — what counts as "effective disturbance" for its context (environmental noise, adversarial coupling, closure defect, or a decomposition of these).

### External mathematical lineage: monotone-operator theory

The sector-Lyapunov apparatus this segment factors out has a well-established mathematical home: AAT's sector condition (T2) is a **one-point strong monotonicity** condition in the sense of Rockafellar 1970 (*Convex Analysis*, §24) anchored at the equilibrium $\xi^\ast = 0$, and the incremental strengthening DA2'-inc required by `#form-composition-closure`'s bridge lemma is **full two-point strong monotonicity** in the Bauschke-Combettes 2017 (*Convex Analysis and Monotone Operator Theory in Hilbert Spaces*, 2nd ed., §§22–28) monotone-operator framework. The Lyapunov-plus-Grönwall argument proving the Model D ultimate bound and the Itô-Lyapunov argument proving Prop A.1S are standard specializations of the **monotone-operator perturbation theorem** (Bauschke-Combettes Thm 5.14–5.16; Parikh & Boyd 2014, *Proximal Algorithms*, §2). Banach-Picard contraction under bounded perturbation, monotone-operator convergence under square-summable noise, operator-splitting for composite systems (Douglas-Rachford, ADMM) — the full supporting apparatus is available in that literature.

AAT's relationship to monotone-operator theory is *specialization + repurposing*, not generalization. AAT-distinctive content: (i) **one-point anchoring at the equilibrium** — strictly weaker than full two-point strong monotonicity, matched to fixed-point-at-target semantics, admitting agent classes (PID-bounded-plant, variational-approximate) where full monotonicity fails but persistence-at-the-target is available. (ii) The **Model D / Model S disturbance decomposition** with distinct $1/\alpha$ vs $1/\sqrt\alpha$ scaling — monotone-operator theory has perturbation theorems but no systematic bounded-adversarial vs stochastic-zero-mean split propagating to adversarial-exponent regimes at $b = 2$ vs $b = 3/2$. (iii) Composition with the `#disc-identifiability-floor` meta-pattern supplies a second (information-theoretic) axis orthogonal to the operator-theoretic machinery. (iv) The `#post-composition-consistency` postulate operates at AAT's level of description (agent / composite / macro-agent) rather than at the abstract operator level. (v) The sub-scope α/β epistemic labeling is scope-honesty, not a mathematical partition — it tracks which agent classes give the monotone-operator structure *by construction* versus *by per-instance verification*.

This acknowledgment is load-bearing for scope honesty: the mathematical machinery is established external to AAT; AAT's distinctive content is the agent-architecture specialization (singular-trajectory identity per `#scope-agent-identity`; signed-coupling composition; coordinate-forcing via uniqueness theorems per `#disc-additive-coordinate-forcing`; three meta-patterns) rather than novel monotone-operator mathematics. `#deriv-sector-condition`'s Grounding paragraphs name the specific operator-family correspondence (proximal / firmly-nonexpansive / cocoercive / strongly-monotone-gradient / linear-PD) for the five sub-scope-α agent classes. `#result-contraction-template` extends to non-Euclidean metrics via Lohmiller-Slotine differential-contraction (also within the broader monotone-operator lineage). The honest limits of the unification: the coarse-graining projection $\Lambda$ (#form-composition-closure) does not fit the operator-sector primitive (heterogeneous spaces, three independent admissibility conditions); three of five metric-α₂ cases in `#result-contraction-template` remain theorem-imported rather than AAT-internally derived; the identifiability-floor axis is orthogonal to the operator-sector axis.

### Comparison with the FEP-flow stability argument

Active inference's stability arguments come from the geometry of the variational free-energy landscape — agents are argued to flow toward the minimum of variational free energy on a non-equilibrium-steady-state (NESS) density. The primary source for the NESS-density framing is Friston 2019, "A free energy principle for a particular physics," arXiv:1906.10184; the path-integral / particular-kinds methodological extension is Friston, Da Costa, Sakthivadivel, Heins, Pavliotis, Ramstead & Parr 2023, "Path integrals, particular kinds, and strange things," *Phys. Life Rev.* 47 (which rewrites the FEP-flow argument in path-integral language rather than proving new stability bounds). Aguilera, Millidge, Tschantz & Buckley (2022, "How particular is the physics of the free energy principle?", *Phys. Life Rev.* 40:24–50) showed that the FEP-flow argument's mathematical validity is narrow: the NESS-density framing holds only in a small parameter regime for non-equilibrium linear stochastic systems, and natural extensions (nonlinear, non-Gaussian, non-equilibrium) often fall outside the proven regime.

The AAT persistence template is structurally different: it is a Lyapunov-based argument requiring only (T1) zero-correction-at-zero-state, (T2) local sector condition (correction points inward), and (T3) bounded disturbance — all of which are checked locally for each instantiation ( #deriv-sector-condition Props A.1, A.1S, A.2). The template applies to bounded and to mean-square-stochastic disturbance, gives explicit ultimate-bound and adaptive-reserve formulas, and does not depend on NESS structure or on a free-energy gradient.

The breadth difference is not rhetorical: where the FEP-flow argument's parameter regime is debated in the AI literature itself, the sector-Lyapunov apparatus is the standard machinery of nonlinear control theory (Khalil 2002, *Nonlinear Systems*, 3rd ed., Prentice Hall, ch. 4) and applies wherever (T1)–(T3) hold. This is one of AAT's stronger structural positions and is worth making explicit when comparing AAT to active inference: AAT does the persistence work AI tries to do, with broader validity and explicit ultimate-bound formulas.

---



## Result: Certificate Existence — Operator-Sector in Some Metric Is Exponential Stability

- **Slug**: `result-certificate-existence`
- **Type**: result
- **Status**: exact
- **Stage**: draft
- **Depends**: `deriv-sector-condition`, `result-sector-persistence-template`

A stability certificate exists for an agent exactly when the agent is exponentially stable about its target; the organizing slogan *an adaptive system is an operator whose contraction rate exceeds its target's drift rate* is not a heuristic but this equivalence, with the certificate as its witness.

### The object

*[Definition (stability-certificate)]*

For an agent with error dynamics $\dot e=-F(e)$ about an equilibrium $e^\ast$ ($F(e^\ast)=0$, $F\in C^1$ near $e^\ast$, Jacobian $J:=DF(e^\ast)$), a **stability certificate** is a symmetric positive-definite $\mathcal M$ for which the one-point sector condition holds in the $\mathcal M$-inner-product on a ball $\mathcal B_R(e^\ast)$:

$$\langle F(e),\,e-e^\ast\rangle_{\mathcal M}\;\ge\;\kappa\,\lVert e-e^\ast\rVert_{\mathcal M}^2,\qquad \kappa\gt0. \tag{C}$$

The certificate is not unique: it is whatever positive-definite form makes the dynamics contract. In the recurring sub-cases it specializes — to the Fisher information for Bayesian agents, to $(P^-)^{-1}$ for Kalman agents, to the loss Hessian for gradient agents, and to a plant-selected Lyapunov metric for linear-Hurwitz or PID agents. These are not four separate stories; they are one object under four certificates.

### The equivalence

*[Result (certificate-existence), exact at the linearized level]*

At the linearized level (C) reads $\mathcal M J+J^\top\mathcal M\succeq 2\kappa\mathcal M\succ0$, a strict Lyapunov inequality for the system matrix $A=-J$. The following are equivalent:

1. $A=-J$ is Hurwitz — the linearized error dynamics $\dot e=-Je$ is exponentially stable;
2. there exist $\mathcal M\succ0$ and $\kappa\gt0$ with $\mathcal M J+J^\top\mathcal M\succeq2\kappa\mathcal M$ — a one-point sector condition (a stability certificate) in *some* inner product;
3. for every $Q\succ0$ there exists a unique $\mathcal M\succ0$ with $\mathcal M J+J^\top\mathcal M=Q$.

So "operator-sector in *some* inner product" and "the equilibrium is exponentially stable" are **the same statement**, with the certificate $\mathcal M$ as the converse-Lyapunov witness — an equivalence, not an analogy.

### The certificate-strength ladder

*[Derived (ordering of conditions; exact)]*

The certificate admits three strictly-ordered strengths, all on the one object:

| Rung | Condition | Equivalent to | Certificate is |
|---|---|---|---|
| R0 | one-point (C), some $\mathcal M$, local | $A=-J$ Hurwitz + remainder dominated | converse-Lyapunov $\mathcal M$ (exists; generally not forced) |
| R1 | incremental (two-point) $\mathcal M$-strong-monotonicity on $\mathcal B_R$ | global $\mathcal M$-strong-monotone (cocoercive class) | curvature-like $\mathcal M$ (potential sub-case) |
| R2 | R1 with $\mathcal M$ *forced* by a uniqueness theorem on an AAT-internal axiom | natural-gradient in the Čencov-unique Fisher metric | Fisher metric (Čencov-forced) |

R0 ⟸ R1 ⟸ R2 strictly. R0 is the *widest* rung — it reaches the plant-Lyapunov cases (linear-Hurwitz-non-symmetric, PID) where no potential exists; R1 is the cocoercive/proximal class where a variational structure is available; R2 is the uniqueness-theorem-forced statistical case. The widest rung is not a weakness: it is exactly the reach the narrower rungs cannot give. (R2's forcing is established in #disc-additive-coordinate-forcing; R1's cocoercive class in #result-contraction-template.)

---



## Derivation: Persistence Cost — Information Rate to Maintain Bounded Mismatch

- **Slug**: `deriv-persistence-cost`
- **Type**: derivation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `result-persistence-condition`, `result-sector-condition-stability`, `deriv-sector-condition`, `result-sector-persistence-template`, `def-adaptive-tempo`, `emp-update-gain`, `der-gain-sector-bridge`, `def-model-class-fitness`

AAT's persistence machinery establishes that under the sector condition, mismatch stays bounded. It does not quantify the *sustained rate of effort* an agent must expend to hold that bound. Two agents with identical persistence guarantees can face wildly different demands — a Kalman filter tracking a stationary process vs one tracking a rapidly non-stationary process are both persistent; one is dormant, the other running hot. Under Model S with Gaussian-OU signal, the sustained Shannon information rate the agent must acquire from observations to maintain the sector-persistence ultimate bound is $\dot R_{\min} \geq n\alpha/2$ nats per unit time — a Landauer-analog lower bound that depends only on the signal's second-order statistics and the sector constant $\alpha$, and that Kalman-Bucy saturates in steady state. The bound promotes channel capacity $C \geq \mathcal T/2$ into a first-class persistence prerequisite that the current theory does not name.

### Setup

The agent is in scope of #result-sector-condition-stability Model S (GA-2S, stochastic disturbance).
Per Prop A.1S the state satisfies $\mathbb E[\lVert\delta\rVert^2]_{ss} = n\sigma_w^2/(2\alpha)$.
The RMS bound is $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$.
The environmental signal is $n$-dimensional independent-component Ornstein-Uhlenbeck with per-component intrinsic drift $\lambda_s$ and diffusion coefficient $\sigma_w^2$.
The mean-square persistence condition $\alpha \gt n\sigma_w^2/(2R^2)$ holds.
Sector-persistence is achieved at the tight bound $D^2 = R^{\ast 2}_S$.

### Persistence Information Rate (main theorem)

*[Proved (persistence-information-rate, from Shannon RDF + Prop A.1S)]*

**Proposition.** Any adaptive process achieving the tight Model-S ultimate bound $\mathbb E[\lVert\delta\rVert^2]_{ss} = n\sigma_w^2/(2\alpha)$ under the stated setup must acquire information from observations at sustained rate

$$\boxed{\;\dot R \;\geq\; \dot R_{\min} \;=\; \frac{n\alpha}{2} \text{ nats per unit time}\;}$$

**Derivation.** Shannon's rate-distortion theorem (Shannon 1948; Berger 1971; Cover & Thomas 2006 Theorem 10.2.1) states that for any source-code achieving mean-square distortion $D^2$, the coding rate satisfies $\dot R \geq R(D^2)$ where $R(\cdot)$ is the rate-distortion function. For $n$-dimensional independent-component OU in the high-resolution regime ($D^2 \ll \sigma_x^2 = \sigma_w^2/(2\lambda_s)$), the RDF per unit time is (Ihara 1993 Theorem 4.6.4; Gray 1972 Theorem 2):

$$\dot R(D^2) = \frac{n\sigma_w^2}{4 D^2}$$

Substituting $D^2 = R^{\ast 2}_S = n\sigma_w^2/(2\alpha)$:

$$\dot R_{\min} = \frac{n\sigma_w^2}{4 \cdot n\sigma_w^2/(2\alpha)} = \frac{\alpha}{2} \cdot 1 = \frac{n\alpha}{2} \text{ nats per unit time}$$

(the calculation gives $\alpha/2$ per dimension and $n\alpha/2$ total for $n$ independent OU components). The agent's observation-channel information rate must meet this bound regardless of the specific correction function, filter structure, or implementation. $\square$

### Kalman-Bucy Saturates the Bound

*[Derived (Kalman-tight, Mitter-Newton 2005)]*

The Kalman-Bucy filter attains the bound exactly in steady state. Mitter & Newton (2005, *J. Stat. Phys.* 118:145–176) derive the filter's rate of information supply as

$$\dot I = \tfrac{1}{2}\operatorname{tr}(H^T \Sigma_o^{-1} H P_{ss})$$

Scalar case ($H = 1$, $\Sigma_o = \sigma_o^2$) with steady-state covariance $P_{ss} = \sigma_o \sigma_w$ in the drift-dominated limit and Kalman gain $K_{ss} = P_{ss}/\sigma_o^2 = \sigma_w/\sigma_o$:

$$\dot I = \frac{P_{ss}}{2\sigma_o^2} = \frac{K_{ss}}{2} = \frac{\alpha}{2}$$

Under the linear-correction identification $\alpha = K_{ss}$ (from #der-gain-sector-bridge, scalar Kalman case), the Kalman filter's information supply rate equals $\alpha/2$ exactly. This matches the RDF lower bound, confirming tightness. **The bound is not merely a lower bound — it is achieved by the Kalman-optimal filter.**

### Channel-Capacity Prerequisite

*[Derived (channel-capacity-floor, from main theorem + Shannon capacity)]*

By Shannon's channel coding theorem (Cover & Thomas 2006 §7.7), an observation channel of Shannon capacity $C_{\text{channel}}$ can support any information rate up to $C_{\text{channel}}$ and no higher. Combining with the persistence information rate:

$$C_{\text{channel}} \;\geq\; \dot R_{\min} \;=\; \frac{n\alpha}{2}$$

Under the linear-correction identification $\alpha = \mathcal T$ (from #def-adaptive-tempo + #der-gain-sector-bridge scalar Kalman):

$$\boxed{\;C_{\text{channel}} \;\geq\; \mathcal T / 2 \text{ nats/time per dimension}\;}$$

**Persistence demands observation-channel capacity at least half the adaptive tempo.** This is a *new first-class persistence diagnostic* not present in the current theory. Its binding matters most in capacity-constrained settings — bandwidth-limited distributed systems, biological neurons, context-window-limited LLMs — where the tempo framework alone underestimates the difficulty of maintaining bounded mismatch.

### Rejected Candidate Cost Metrics

The information-rate bound is not the only candidate for a cost-of-persistence quantity. Three alternatives fail structurally. Recording them here keeps the scope-honesty visible.

*[Observation (gain-magnitude-tautological)]* $\mathbb E[\lVert K(t)\rVert]$ as a cost metric: in the linear Kalman case $K_{ss} = \alpha$ (sub-scope $\alpha$ per #der-gain-sector-bridge), so "gain magnitude" equals the sector constant itself. Any bound of shape $\mathbb E[\lVert K\rVert] \geq f(\alpha, \ldots)$ becomes tautological. Rejected as fundamental cost metric — it recapitulates $\alpha$.

*[Observation (control-effort-filter-specific)]* $\mathbb E[\lVert u(t)\rVert^2]$ (per-unit-time control-effort integral): filter-specific. Different filters achieving the same steady-state variance $P_{ss}$ have different control-effort integrals. The Kalman filter is minimum-effort among linear filters (optimal-control interpretation of the Riccati equation); nonlinear filters can trade effort vs variance differently. A filter-agnostic bound cannot be stated in this quantity — it is not invariant under the equivalence class of filters meeting the persistence condition.

*[Observation (Lyapunov-dissipation-conservation)]*
$\mathbb E[\alpha\lVert\delta\rVert^2]_{ss}$ (Lyapunov dissipation rate) at steady state equals $n\sigma_w^2/2$ regardless of $\alpha$ — a non-equilibrium-steady-state conservation law (dissipation balances disturbance-power injection).
The quantity is *structurally invariant*: it does not depend on the quality of adaptation, only on the disturbance statistics.
This is what makes the RDF bound tight at the Model-S ultimate bound (the steady state is active, not slack), but it cannot itself serve as a cost metric because it does not distinguish well-adapted from poorly-adapted agents at a given $\alpha$.

Candidate 4 — the Shannon information rate above — is the one that closes. The structural reason: information rate is filter-agnostic (depends only on signal second-order statistics and target distortion), universal (any filter implementation is lower-bounded), and has a clean thermodynamic interpretation (Still et al. 2012, "Thermodynamics of Prediction", *Phys. Rev. Lett.* 109:120604: nonpredictive information retained equals dissipation during interaction).

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Persistence information rate $\dot R_{\min} \geq n\alpha/2$ | Shannon RDF (Berger 1971; Gray 1972; Ihara 1993 Thm 4.6.4) composed with Prop A.1S | Derived (conditional on Model S + Gaussian-OU + high-resolution regime) |
| Kalman-Bucy saturates bound | Mitter-Newton 2005 Theorem (information-supply identity); linear-correction identification $\alpha = K_{ss}$ per #der-gain-sector-bridge | Derived (linear-Gaussian; exact when A2' is derived in sub-scope $\alpha$) |
| Channel-capacity prerequisite $C \geq \mathcal T/2$ | Main theorem + Shannon channel-capacity theorem (Cover-Thomas 2006 §7.7) + $\alpha = \mathcal T$ identification | Derived |
| Gain-magnitude as cost metric | $\mathbb E[\lVert K\rVert] \approx \alpha$ in sub-scope $\alpha$ | Rejected as fundamental (tautological) |
| Control-effort integral as cost metric | Filter-specific; depends on optimality class | Rejected as universal (filter-dependent) |
| Lyapunov dissipation rate | Conservation law $= n\sigma_w^2/2$ at steady state | Not a cost metric — structural observation enabling tightness of main theorem |
| Non-Gaussian signal extension | Different RDF form (Berger 1971 Ch. 4) | Open — qualitative scaling $\dot R \propto$ innovation-rate/$D^2$ likely preserved; exact prefactor changes |
| Model D (bounded disturbance) analog | Requires adversarial / minimax information argument (Csiszár-Körner 2011 Ch. 11) | Open |
| Transient-regime rate | Bound is steady-state; transient rates during structural adaptation much higher | Open |
| Sub-scope $\beta$ transfer | RDF bound holds as inequality (data-processing); tightness not guaranteed | Conditional (holds as lower bound; Kalman-Bucy saturation requires sub-scope $\alpha$) |

---
