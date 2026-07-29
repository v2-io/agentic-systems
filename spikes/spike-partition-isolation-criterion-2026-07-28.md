# Spike: the partition-isolation criterion — do concurrent writers and eroding tiles instantiate one law?

*2026-07-28. Commissioned by Joseph out of vivarium's boundary-contract day: "That's just possibly a strong enough statement that it has some mathematical backbone instead of just a convenient parallel based on what we've been working on… see if it ends up being useful for `02-tst-core` somehow." Spike disposition per `spikes.sop.md` §0c — attempt the strongest version first; a rigorous no-go with its reason is a full success; land honestly at whatever tier the math supports. **Read-only on canon: no segment, OUTLINE, or `status:` was edited by this spike.***

## 0. The claim as received, and what happened to it

The candidate, stated at maximum ambition so it could be strengthened or refuted rather than pre-softened:

> Concurrent writers over shared mutable state instantiate one structure — a partitioned domain with finite influence propagation and boundary contracts — and the coordination law is scale-arithmetic: a partition-local process may be treated as isolated exactly when the influence cone (propagation speed $\times$ work interval) does not reach its boundary; otherwise honest coupling requires declared exchange, and undeclared isolation produces artifacts that pass local audits while lying globally.

**Verdict in one line: there is backbone, but not where the claim puts it, and the claim's headline is the weakest part of it.**

Four findings, in descending order of how much they carry:

- **R1 — the unifying template is real and is *imported*, not new.** Both instantiations are corners of a Lieb–Robinson / domain-of-dependence bound, which is standard mathematical physics. Per *Prior art integration* (`agents.sop.md`), the right move is to adopt it under its own name and cite it — not to coin an AAT law for it. The unification therefore contributes *legibility*, not a theorem: it forces both instantiations to declare the same three parameters and thereby makes their **differences** statable, and the differences are the content (§5).
- **R2 — the discrete instantiation is new where it counts, though not in the criterion (§10).** Modeling change propagation over `#def-system-coupling`'s kernel $K$ as a multitype branching process gives a criticality threshold at $\rho(K) = 1$ and a cone radius growing only *logarithmically* in work volume. Combined with a metric-compatibility premise, it yields a **second, independent derivation of "high cohesion, low coupling"** — not from single-agent comprehension cost (TST's existing grounding), but as the exact precondition for concurrent development to be possible at all (§4). The commissioned prior-art search has since landed (§10) and sorts cleanly: the *criterion* is prior art (Smith & Eppinger 1997), the *decay* is prior art (Dobrushin; Künsch 1982), the *kernel estimated from change history* is prior art (Giffin et al. 2009) — and **no literature holds two of the three layers, nobody has done any of it for software, and the isolability corollary is unfound across six literatures.** So the threshold is adopted-and-cited, and the contribution is the identification plus the corollary.
- **R3 — "green audit, wrong domain" is an identifiability-floor instance with a Pearl-rung gate, and it is the most landable piece.** A contract-blind audit cannot convict a boundary contract as a matter of invariance; adjudication requires rung-2 access (carve twice under $do(c)$ and $do(c')$). Vivarium independently derived the boundary route today — *"the contract has to become a parameter before the experiment that would choose it can run"* — which is exactly step 4 of the constructive-impossibility shape in `#disc-identifiability-floor` (§6).
- **R4 — a measured no-go that sharpens the claim: non-decaying observables defeat the criterion entirely, and no partition granularity repairs them.** Found in vivarium's tree hours after the brief was written: a lake's spill level is a minimum over its whole rim, and *a minimum over a set does not decay as the set is enlarged*. So the sensitivity premise fails outright — not slowly — for order-statistic and global-registry observables, no matter how local the underlying dynamics. The isolation criterion is **per-observable**, not per-domain (§8). This is the strongest cross-instantiation result in the spike, and it has a measured instance on the continuous side and an everyday instance on the discrete side.

And one correction to the evidence base rather than to the mathematics: **most of the discrete incidents are not cone-overruns.** They are violations of the criterion's *premise* — that a writer writes only inside its declared region. That premise is structural in the continuous case and merely promissory in the discrete one, and the asymmetry is itself a result (§7).

**Two further results arrived mid-spike from Joseph's ideations, and both convict** (§9). Promoting the *seam* to a first-class owned object — the mortar-element move — eliminates R4's pathology rather than bounding it, keeps both sides' keys free of neighbor content, and supplies the structural enforcement §7 says prose cannot give. And **fated commitments** turn R4 from a prohibition into a constructive answer: on non-decaying observables, publishing a plausible draw and binding later refinement to honor it is not the better discipline, it is the *only* one, because reconciliation has no convergent form there. Its discrete twin is contract-first development, and the criterion says *which* artifacts must be handled that way and why. If novelty over prior art survives anywhere in this cluster, that third seam resident is the most likely place.

---

## 1. Setting and premises

Let $V$ be a set of **sites** carrying the shared mutable state, with a metric $d$ on $V$. The state is $\Omega \in \prod_{v \in V} \mathcal{S}_v$. Writers $1, \ldots, N$ act over a work interval $[0, T]$; writer $i$ has a declared **write region** $A_i \subseteq V$.

This is `#scope-multi-agent`'s configuration — $N$ agents coupled through a shared environment $\Omega_t$, with $\Omega_{t+1} = T(\Omega_t, a_t^{(1)}, \ldots, a_t^{(N)}, \omega_t)$ — plus one structure AAT's scope segment deliberately does not impose: **a metric on the environment, and locality of the transition with respect to it.** Everything below is a consequence of adding that structure; nothing below is available in AAT as it stands, which is the honest statement of where this work would go.

**(P0) Action locality.** $a^{(i)}_t$ modifies $\Omega_t(v)$ only for $v \in A_i$.

**(P1) Propagation decay.** There exist $C \geq 1$, $\mu \in (0, \infty]$, and $v_{\mathrm{LR}} \geq 0$ such that for every $u, w \in V$ and every horizon $T$, the sensitivity of $\Omega_T(w)$ to $\Omega_0(u)$ satisfies

$$\mathrm{Infl}(u \to w;\, T) \;\leq\; \min\!\left\{1,\; C\,e^{-\mu\left(d(u,w) \,-\, v_{\mathrm{LR}} T\right)}\right\}.$$

This is the Lieb–Robinson form (Lieb & Robinson 1972; Nachtergaele & Sims 2006 for the modern statement). In a deterministic setting read $\mathrm{Infl}$ as a bounded partial derivative or Lipschitz constant; in a stochastic setting read it as the probability that a perturbation at $u$ is felt at $w$ within $T$. The two parameters do different jobs: $v_{\mathrm{LR}}$ is a **speed** (how fast the front advances), $\mu$ is an **attenuation** (how fast influence dies with distance at fixed time). $\mu = \infty$ means a hard cutoff — influence outside the front is exactly zero.

**(P2) Metric compatibility.** $d$ is a metric in which (P1)'s decay actually holds — i.e. the propagation structure is (approximately) supported near the diagonal of $d$. (P2) is vacuous in the continuous case, where $d$ *is* the propagation metric by construction. It is a substantive and falsifiable architectural condition in the discrete case, and §4 is where it earns its keep.

### The cone radius and the isolation criterion

**Definition (cone radius).** For tolerance $\varepsilon \gt 0$,

$$R(T; \varepsilon) \;=\; v_{\mathrm{LR}}\,T \;+\; \frac{1}{\mu}\,\ln\frac{C}{\varepsilon}.$$

*[Derived (isolation-criterion, from P0–P2)]* **Result 1.** Let $D \subseteq A_i$ with $d\left(D,\, V \setminus A_i\right) \gt R(T;\varepsilon)$. Then for any two boundary contracts $c, c'$ imposed on $\partial A_i$ — equivalently, for any two behaviors of the other writers — the resulting trajectories agree on $D$ up to $\lvert \partial A_i \rvert \cdot \varepsilon$. In the hard-cutoff limit $\mu = \infty$ they agree **exactly** on $D$ whenever $d(D, \partial A_i) \gt v_{\mathrm{LR}} T$.

*Derivation.* Induction on $t$: by (P0)+(P1) the value at $w$ after $t$ steps depends on initial data only within distance $v_{\mathrm{LR}}t$ up to the stated exponential tail; summing the tail over $\partial A_i$ gives the bound. This is the domain-of-dependence argument (Courant, Friedrichs & Lewy 1928) in its Lieb–Robinson generalization, and it is elementary given (P1). **It is not the contribution.**

Two readings worth holding separately, because the claim as received fuses them:

- **The permissive reading.** Inside the cone-free interior the contract is *irrelevant* — any contract gives the same answer, so declaring it buys nothing there.
- **The prohibitive reading (the contrapositive).** Outside the cone-free interior the answer *depends on* the contract. An undeclared contract is therefore an undeclared dependence: not a stylistic omission but a missing argument to a function whose value changed.

§6 shows these are not symmetric, because the second one is not detectable from where you are standing.

---

## 2. What is actually being claimed, restated honestly

Result 1 is a template with three free parameters $(d, v_{\mathrm{LR}}, \mu)$ and a premise set $\{$(P0), (P1), (P2)$\}$. A claim that two systems "instantiate one structure" cashes out as: *both satisfy the premises, and here are their parameters.* That is a much weaker and much more useful statement than the received claim, because the parameters land in **different corners** and the premises hold for **different reasons** — and the corners and the reasons are where every non-obvious consequence lives.

---

## 3. Instantiation A — the eroding tile

Sites are grid cells; $d$ is cell distance; the writers are tile builds.

**(P0) holds structurally.** A finite-difference stencil cannot write outside its stencil. There is no mechanism by which a tile build touches another tile's cells; the kernel would have to be rewritten to make it possible. Hold this — it is the whole of §7.

**(P1) holds with $\mu = \infty$ and $v_{\mathrm{LR}}$ = the characteristic speed of the erosional wave.** Two candidate speeds are available and the vivarium measurements discriminate between them, which is exactly the calibration-laboratory role:

- The **stencil speed** is $1$ cell per epoch (nearest-neighbor operator). Over the $300$-epoch beacon window this gives a cone radius of $300$ cells, far exceeding the $32$-cell half-width of an L9 tile — so the loose bound predicts the L9 contracts should *disagree*.
- The **characteristic speed** is the Courant number of the incision wave, reported at $\approx 0.02$–$0.11$ cells/epoch at L9 and $\approx 1$ at L13 (second-hand from the commissioning session; see the honesty note below). This gives a cone radius of $6$–$33$ cells at L9 — marginal against the $32$-cell half-width — and $\approx 300$ cells at L13, flooding the tile.

**Measured, first-hand from `#vivarium/obs-tile-outlets-grade-away-the-basins` and `#vivarium/form-declared-boundary-contract`:** at L9 ($1251$ km tiles) the two named contracts `BaseLevelSink` and `NoFluxWall` track within $5$–$10$% at every rung of a $300$-epoch history. At L13 ($78$ km tiles) the same comparison ends $203$–$259$ m apart in mean $\lvert \Delta h \rvert$, with $63.5$% of the window in closed depressions against a single cell for the single-field arm, and — the clause that matters most for the cone reading — **the divergence is not concentrated at the boundary**: $259.2$ m on the tile perimeter rings against $203.5$ m inside them.

So the tight bound is confirmed and the loose one refuted, and the *interior* divergence at L13 is what a flooded cone looks like: once $R \gg$ the tile half-width there is no cone-free interior left, and the contract restructures the whole window rather than a rim. The L9 case sitting at $5$–$10$% rather than at $0$% is what a *marginal* cone looks like, which is the honest reading of a $6$–$33$ cell radius against a $32$ cell half-width. That the framework's parameter and the measurement land in the same marginal regime is corroboration; it is not a fit, because nothing was tuned.

> **Honesty note on the Courant figures.** I did not measure them. They arrive second-hand from the commissioning session and I have not run `examples/base_level_probe` or read the incision timestep myself. Every clause above that depends only on the vivarium segments' own measured numbers is first-hand; the *attribution of those numbers to a characteristic speed* is not, and it is the single verification this section owes. The probe that would convict it exists: sweep the tile grain at fixed epoch count and check that the contract-divergence onset tracks $v_{\mathrm{LR}} T$ against the half-width rather than tracking the grain directly.

**(P2) is vacuous here** — the grid metric is the propagation metric.

---

## 4. Instantiation B — the codebase under concurrent writers

Sites are modules; the propagation kernel is `#def-system-coupling`'s $K_{ij} = P(\mathrm{change}(m_j) \mid \mathrm{change}(m_i))$, with $K_{ii} = 0$; the structural metric is `#def-discontinuity-distance`. Writers are concurrent developers or agents; the work interval carries $n$ changesets.

### 4.1 The branching bound

Model the ripple from one edit as a **multitype branching process** with offspring mean matrix $K$: changing $m_i$ forces changes in a set of $m_j$ with the stated probabilities, each of which may force further changes. Let $\rho(K)$ be the Perron root.

The expected number of modules reached at generation $\ell$ from a seed at $m$ is $\mathbf{e}_m^{\top} K^{\ell} \mathbf{1}$. A module at coupling-graph distance $\geq R$ from $m$ cannot be reached before generation $R$, so by Markov's inequality

$$P\!\left(\text{cascade reaches distance} \geq R\right) \;\leq\; \sum_{\ell \geq R} \mathbf{e}_m^{\top} K^{\ell}\mathbf{1}.$$

For a nonnegative primitive $K$ with $\rho = \rho(K) \lt 1$ one has $\lVert K^{\ell} \rVert_{\infty} \leq C_K\,\rho^{\ell}$, whence

$$P\!\left(\text{reach} \geq R\right) \;\leq\; \frac{C_K\, k\, \rho^{R}}{1 - \rho},$$

with $k = \lvert V \rvert$. Union-bounding over $n$ changesets in the work interval and solving for the tolerance gives the discrete cone radius

$$R^{\ast}(n; \varepsilon) \;=\; \frac{1}{\ln\!\big(1/\rho(K)\big)}\;\ln\!\frac{n\,C_K\,k}{\varepsilon\,(1-\rho)} .$$

Matching against Result 1: **$\mu = \ln\big(1/\rho(K)\big)$ and $v_{\mathrm{LR}} = 0$.** Propagation here is generation-indexed rather than time-indexed — a single commit can realize an arbitrarily long cascade — so work volume enters through $C$, not through a front speed.

*[Derived (subcritical-isolation, conditional on the branching model and (P2))]* **Result 2a.** Concurrent writers on modules separated by $R^{\ast}(n;\varepsilon)$ in the coupling graph may be treated as isolated to tolerance $\varepsilon$. The required separation grows only **logarithmically** in the work volume $n$ and in the system size $k$. *(The logarithmic margin itself is a known phenomenon, recovered rather than discovered — CYCLADES obtains an $O(\log n)$ bound for the same reason on a different criterion; see §10.2. What is not known is the criterion, and §10.3 records where the spectral form is provably sharper than the published max-degree one.)*

*[Derived (criticality-threshold)]* **Result 2b (adopted, not novel — see §10.1).** The Perron-root criterion on a propagation matrix is Smith & Eppinger 1997's, and the exponential-decay consequence is Dobrushin's; what is taken here is the *identification* of `#def-system-coupling`'s kernel as such a matrix. With that: $\rho(K) \geq 1$ makes the geometric bound vacuous: $\sum_{\ell} K^{\ell}$ diverges, expected cascade size is unbounded, and **no finite $R^{\ast}$ exists at any tolerance.** In the supercritical regime concurrent isolated work is not available at *any* partition granularity, and every concurrent write requires declared exchange.

### 4.2 Why (P2) is the architectural condition, and what it re-derives

$R^{\ast}$ above is measured in **coupling-graph hops**, not in `#def-discontinuity-distance`. Writers are separated in the structural metric — different modules, different directories, different services — so the criterion is only usable if the two metrics agree, which is (P2): *coupling must fall off with structural distance.*

This is not automatic and TST does not currently assert it. `#der-change-proximity-principle` asserts that the *cost* of a change rises with structural distance; it says nothing about whether *coupling* falls with it. A codebase in which distant modules co-change freely — the archetypal bad architecture — violates (P2) exactly, and then the structural partition tells you nothing about isolation.

So the two conditions for concurrent development are:

1. **Subcriticality**, $\rho(K) \lt 1$ — the ripple dies out. This is *low coupling*, made quantitative and given a threshold.
2. **Metric compatibility (P2)** — the ripple, while it lives, stays structurally near. This is *high cohesion*, in its operative role.

*[Derived (concurrency-grounding-of-cohesion-coupling, conditional)]* **Result 2c.** "High cohesion, low coupling" is the exact precondition for concurrent development to be isolable at all. TST currently grounds that principle in single-agent comprehension cost (`#def-system-coherence` Discussion: high coherence reduces per-feature $M_t$ construction cost, low coupling reduces changeset size, both minimizing time under `#post-temporal-optimality`). This is a **second and independent grounding** from a disjoint premise set, and it has a feature the first one lacks: a threshold. The comprehension-cost grounding says coupling is bad *continuously* — less is better, always. The concurrency grounding says there is a **qualitative** boundary at $\rho(K) = 1$ across which a capability is lost rather than degraded.

### 4.2a (P2) already has an empirical estimator in TST, unrecognized as one

A first draft of this spike asserted that TST is silent on concurrency. **That is false, and the correction is the most useful thing in §4.** `#hyp-conceptual-alignment`'s Discussion carries *"Merge conflicts as alignment diagnostic"* and proposes

$$\text{alignment-quality} \;=\; 1 \;-\; \frac{\text{conflicts between conceptually independent features}}{\text{total conflicts}},$$

marked *[Discussion — operationalizable but unmeasured]*, with the honest complaint that it *"requires a ground-truth classification of feature independence — which is itself a judgment call."*

A conflict between conceptually independent features developed **in parallel** is exactly an isolation failure: two writers on structurally-separate regions whose influence collided anyway. So alignment-quality is already a direct empirical estimator of the **violation rate of the isolation criterion** — which is to say, of (P2). It was authored as a diagnostic for a different hypothesis and happens to measure this one.

And the criterion repays the debt, because it dissolves the judgment call the segment flags as the diagnostic's blocker. *Independence* need not be a human classification of domain areas: it is $d(A_1, A_2) \gt R^{\ast}(n;\varepsilon)$ in the coupling metric, computed from the same git history that supplies the conflicts. That converts an *"operationalizable but unmeasured"* quantity into a measurable one with no ground-truth labeling step. This is the empirical leg the rest of §4 otherwise lacks, and it is the cheapest thing in this spike to actually run.

### 4.3 The definitional gap this exposes

The branching reading needs $K$ to be a **forced-follow-on** kernel: $P(\text{changing } i \text{ later requires changing } j)$. `#def-system-coupling` as written is a **co-change** kernel estimated from commits, which conflates forced follow-on with within-changeset co-occurrence and with convention-driven bundling. The segment's own Working Notes already flag this — *"that could be coupling OR could be convention… distinguishing requires looking at whether the feature required both changes vs whether the developer chose to include both"* — and `#hyp-causal-discovery-from-git` names the three confounder classes.

What is new is that the distinction now carries **quantitative** weight rather than interpretive weight. Under the co-change reading, $\rho(K)$ is a co-occurrence density and has no threshold meaning. Under the forced-follow-on reading it is a branching rate and $\rho(K)=1$ is a phase boundary. A measurement that does not separate them cannot be read as either. This is a concrete, discharge-able open item for `#meas-coherence-coupling`, and the favourable regimes `#def-system-coupling` already names (atomic feature-scoped commits; asymmetric co-change surviving common-cause confounding) are exactly the regimes in which the separation is available.

### 4.4 A note on the $Q$ ratio

`#meas-coherence-coupling` aggregates to $Q = \sum_i \mathrm{coherence}(m_i) \,/\, \sum_{i \neq j} \mathrm{coupling}(m_i, m_j)$, and its Working Notes already worry that the ratio form *"privileges balance"* and discards absolute level, floating an additive form as an ad hoc alternative. $\rho(K)$ is the absolute-level quantity the ratio discards, it is derived rather than chosen, and it comes with the threshold that makes the level *mean* something. That is a strengthening of an existing segment rather than a new parallel measurement, which is the preferable landing shape.

---

## 5. The two corners — what the unification delivers, and what it does not

| | Erosion tile (§3) | Codebase (§4) |
|---|---|---|
| Attenuation $\mu$ | $\infty$ (hard cutoff) | $\ln(1/\rho(K))$, finite |
| Front speed $v_{\mathrm{LR}}$ | Courant speed of the incision wave, $\gt 0$ | $0$ (cascade is generation-indexed) |
| Cone growth in work | **linear** in $T$ | **logarithmic** in $n$ |
| Phase transition | none | **yes**, at $\rho(K) = 1$ |
| (P0) action locality | **structural** | **promissory** (§7) |
| (P2) metric compatibility | vacuous | substantive, falsifiable, architectural |
| Guarantee | exact | probabilistic, to tolerance $\varepsilon$ |

The two systems sit at *opposite corners* of the same two-parameter bound. Every entry in that table is a difference, and the differences are not cosmetic: a phase transition exists on one side and not the other; the guarantee is exact on one side and probabilistic on the other; the premise that makes the whole thing go is free on one side and must be enforced on the other.

**This is why the received claim's headline is its weakest part.** "Concurrent writers over shared mutable state instantiate one structure" is true in the sense that both satisfy one template, and misleading in the sense that it flattens the six differences that carry all the consequences. The honest headline is the two-parameter family with the two cases at its corners — which is a *smaller* claim that says *more*.

**And the unification is imported, not made.** Lieb–Robinson bounds already are the standard generalization of finite propagation speed to systems with only exponential decay; recognizing that a software co-change kernel and a hyperbolic PDE both fit it is a recognition, not a theorem. `agents.sop.md` *Prior art integration* is directly on point: adopt the concept under its own name with citation, do not coin an AAT law for it, and put the integration in the Discussion of the segments that use it. The counterweight from *Math-novelty recognition* applies to §4 and §6 — Results 2a–2c and 3 are new results derived in AAT-internal settings using established machinery, and should be scored as such — but it does not apply to Result 1, which is a restatement.

---

## 6. The audit no-go — contract identifiability as an identifiability-floor instance

This is the half of the received claim that survives fully intact, and it strengthens under pressure.

**The observation to be explained.** Vivarium's erosion tiles *passed every flux audit* while manufacturing a global artifact. In `#vivarium/form-declared-boundary-contract`'s words: *"the audit is green because the lie is in a column the schema does not have."*

**Definition (contract-blind audit).** An audit is a predicate $\Pi$ on the partition-local trajectory $\{\Omega_t\vert_{A_i}\}$. Call it **contract-blind** if $\Pi$ factors through a statistic invariant under substitution of one admissible boundary contract for another.

*[Derived (contract-blind-audits-have-zero-power)]* **Result 3a.** A contract-blind audit cannot convict a boundary contract, and the failure is by construction rather than by weakness of the test. Interior conservation is the canonical case: the predicate is *"interior change equals measured boundary flux,"* the flux is **read off** rather than predicted, and so the predicate is satisfied identically under every contract. What such an audit verifies is **self-consistency**, not correctness. The green result is not a false negative; the test has no power against this hypothesis at all.

*[Derived (contract-identifiability-requires-rung-2)]* **Result 3b.** Adjudicating a boundary contract requires either an **exogenous referent** (data from outside $A_i$ — the neighbor's actual state, the assembled routing) or an **intervention on the contract itself**: carve the same geography twice under $do(c)$ and $do(c')$ and compare. A single observed run under an implicit contract is rung-1 data about a rung-2 question, and the gap is `#def-pearl-causal-hierarchy`'s.

This puts the result squarely in the five-element constructive-impossibility shape of `#disc-identifiability-floor`: *(1)* setting — identify the boundary contract; *(2)* external theorem — the Pearl–Bareinboim causal hierarchy theorem (Bareinboim, Correa, Ibeling & Icard 2022); *(3)* no-go — no statistic of one observed interior run identifies it; *(4)* boundary characterization — promote the contract to a settable parameter, restoring interventional access; *(5)* the AAT machinery the boundary route requires is `#der-loop-interventional-access`, already present for other reasons.

**The convergence worth recording.** Vivarium arrived at step (4) independently and in the same week, from the engineering side, and wrote it in its own Working Notes before this spike existed:

> *"The contract has to become a parameter before the experiment that would choose it can run… Making the contract an explicit keyed field is therefore not decoration on the repair — it is the repair's instrument."*

It then shipped exactly that (`EdgeContract` naming `BaseLevelSink` and `NoFluxWall` as selectable policies), and observed that its two convicting probes come *"in two strengths"* — the weak one re-reading one carve two ways, the strong one carving the same geography under each contract. Those two strengths are precisely rung 1 and rung 2. Per the charter's §7 note that convergent arrival is evidence the joint is real, this is the best-supported result in the spike.

**And it explains TST's own preface claim from a new direction.** `02-tst-core` positions software as the *privileged high-identifiability calibration laboratory* partly on P3 — commits are literally interventions. The coordination layer inherits that: in software the analog of a boundary contract (which files a writer may touch) can be *set* — a worktree, a branch, an index scope, a restricted tool-set. Software has rung-2 access on the coordination parameter for free; vivarium had to build it. That is the calibration-laboratory claim arriving in a place TST has not yet looked.

---

## 7. The premise is not free on the discrete side — and this is where the evidence base actually points

The commissioning brief reported the day's multi-agent incidents as *"precisely boundary-contract failures."* Reading them against the formalism, **most of them are not.** They are (P0) violations.

- A directory-level `git add` sweeping a neighbor's in-flight state is not influence propagating from a writer's region to its boundary. It is the writer's **actual write region exceeding its declared one**. No cone is involved; the premise simply fails.
- Un-cross-briefed strands duplicating work is closer to a genuine cone overrun — two writers' regions were coupled and neither knew — though "duplicating work" is a coupling in the *authors'* model space rather than in the artifact, which the formalism as stated does not cover.

The distinction matters because the repairs differ, and because the asymmetry is itself a result:

*[Derived (enforcement-asymmetry)]* **Result 4.** Where (P0) holds structurally, the isolation criterion is the only obligation. Where (P0) is **promissory** — the writer *could* exceed its region and is merely expected not to — the criterion is conditional on enforcement, and enforcement must be **by construction** (index scoping, worktree, tool-set restriction) rather than by declaration. A declared region a writer can exceed is not a region; it is a hope about a region, and the isolation criterion computed over it is unsound at its premise rather than at its conclusion.

A finite-difference stencil cannot write outside its stencil. An agent with a shell can. This is the formal statement behind a rule the program already holds operationally and arrived at by injury — `AGENTIC-DELEGATION.md`'s named exception, *"Destructive actions: constrain by tool-set, never by prose,"* whose scar is the 2026-05-02 worktree-deletion incident where an agent asked to *assess* worktrees as safe-to-delete deleted all eight. Result 4 says why prose cannot do that job: prose modifies the declaration, and the criterion's soundness depends on the *realization*.

This also gives the discrete instantiation an obligation with no continuous counterpart, and it should be stated as a scope condition on any concurrency segment rather than folded silently into "partitioned domain."

---

## 8. The no-go: the criterion is per-observable, and non-decaying observables defeat it

The sharpest result, and it came from the world rather than from the desk.

(P1) bounds the sensitivity of an observable to distant state. Nothing guarantees that an observable of interest *has* decaying sensitivity, even when the underlying dynamics do. **Order statistics are the generic counterexample.**

Vivarium landed this today, measured and reasoned, in `#vivarium/form-same-level-halo-exchange` FE(9) — hours after the commissioning brief was written, and independently of it:

> *"A basin that straddles a seam hands its neighbors a quantity the halo cannot carry: its spill level is a property of the whole basin — the lowest point on its entire rim — and a halo of depth $d$ truncates the basin at $d$ cells. Two tiles can then assign different spill levels to one lake and route its outflow in different directions, and **the disagreement does not decay with $d$**, because a minimum over a set does not decay as the set is enlarged; it jumps when the true rim low enters the window and is simply wrong until then."*

*[Derived (extremal-observables-defeat-the-cone)]* **Result 5.** For an observable $f(\Omega) = \min_{v \in S} \Omega(v)$ over a region $S$ of unbounded extent, the sensitivity $\partial f / \partial \Omega(u)$ is $0$ or $1$ according to whether $u$ attains the minimum. It does not decay in $d$; it is a step. (P1) therefore fails for $f$ with $\mu = 0$ *regardless of how local the dynamics generating $\Omega$ are*, and the cone radius is infinite: **no partition granularity, halo depth, or work-interval shortening recovers isolation in $f$.** The honest exchange object for such an observable is not a wider neighborhood but a **non-local sufficient statistic** — one scalar per straddling basin, in vivarium's design — which is declared exchange of a global quantity, i.e. exactly the fallback the criterion prescribes when the cone is unbounded.

**The consequence for a composite kernel.** A world is isolable only in those observables whose sensitivity satisfies (P1). One globally-nonlocal sub-mechanism destroys isolability in everything downstream of it, no matter how local everything else is. Erosion's stream-power incision is a well-behaved advective mechanism with a finite characteristic speed; the depression-fill and flow-routing that sit on top of it are global operations over a basin. The composite is as nonlocal as its worst mechanism.

**The discrete twin, which is why this generalizes.** The software analog of *"a minimum over a rim"* is a **global-registry observable** — a name in a global namespace, a lockfile resolution, a migration ordering, a route table, a canonical-home assignment. Two writers each locally consistent can assign incompatible global values, and the disagreement does not decay with module distance: there is no neighborhood radius at which it becomes small, because the quantity is an argmin or a uniqueness constraint over the whole system. This is precisely the class of merge conflicts that version control cannot see, that pass every local test, and that surface only on assembly — the discrete form of *"green audit, wrong domain."* Vivarium's own working rule *"do not invent a second home — segments own claims"* is a global-registry constraint of exactly this shape, and the fact that it has to be a stated norm rather than a local check is Result 5 in operational dress.

So the received claim's *"otherwise honest coupling requires declared exchange"* is right, and Result 5 says something it did not: **for one identifiable class of observables the "otherwise" is unconditional.** There is no cone arithmetic to do; declared global exchange is the only available discipline, at every grain.

---

## 9. The seam as a first-class object, and the three things it can own

*Added mid-spike from two of Joseph's ideations, offered as "ideation to convict, not spec." Both convict. The second one improves §1's formalization rather than extending it, so it is stated first.*

### 9.1 Seams have their own space — the mortar move

> *"It seems particularly useful that we think of the flux-seams as their own independent space at those seams instead of just parameters on the tile as a whole."*

§1 gives sites $V$ and regions $A_i$, with boundaries $\partial A_i$ as *derived* objects — a seam is a place where two regions happen to abut, and its data are parameters carried by each side. The alternative is to promote it: state space $\prod_{v \in V}\mathcal S_v \;\times\; \prod_{s \in S}\mathcal M_s$, where $S$ is a set of seams and $\mathcal M_s$ is the seam's own space, owned by the seam and read by both sides.

This is the **mortar element method** (Bernardi, Maday & Patera 1994; Wohlmuth 2000), where an interface gets an independent function space and coupling is enforced weakly there rather than by matching traces across it. Its two structural properties are exactly the two at issue here: subdomains keep **independent discretizations** (non-matching grids are admissible, which is the coarse-meets-fine case), and interface single-valuedness holds **by ownership** rather than by reconciliation of two competing values.

Three consequences, each of which resolves something the earlier sections could only bound:

*[Derived (single-valuedness-by-ownership)]* **Result 6a.** Result 5's pathology — *"two tiles can assign different spill levels to one lake and route its outflow in different directions"* — is not bounded by a mortar space, it is **eliminated**. Two tiles cannot disagree about a quantity neither of them owns. The non-decaying error does not become small; it becomes unrepresentable. This is a strictly stronger repair than any halo depth, and Result 5 says it is the only kind available for that observable class.

**Result 6b (keying, and why this is the affordable form).** A tile that depends on its neighbor's *content* drags the neighbor into its key, and transitively the planet. A tile that depends on a **seam object** folds a key of constant size. Vivarium already holds this argument at `#vivarium/form-complete-content-addressed-key` FE(6) for halo descriptors; promoting the seam generalizes it — both sides' keys stay free of neighbor content, and the seam's own key is what carries the dependency. This is what makes the ontology implementable rather than aspirational, and it is the same reason mortar methods permit non-matching grids: neither side has to know the other's discretization.

**Result 6c — the one that reaches back to §7.** (P0) was promissory in the discrete case because a writer *could* write outside its declared region. If a seam is an owned object, then *who may write here* is a property of the object rather than a promise by the writer, and **ownership is the structural enforcement of (P0)**. The three `git add <dir>` incidents are precisely this: the shared boundary was a directory, an unowned region both writers held write access to, so the sweep was not merely possible but unremarkable. The repair is not a stricter promise; it is making the boundary an object with an owner — a per-writer worktree, a per-seam file, an index scoped by construction. §7 said prose cannot do this job; §9.1 says what can.

**The honest cost, which prior art names precisely.** Mortar spaces are not free: the coupled problem is well-posed only under an inf-sup (LBB) condition, so the interface space cannot be arbitrarily rich relative to the subdomain spaces. The software analog is real and familiar — an interface that carries too much *becomes* the coupling it was introduced to remove (the shared-database-as-integration-point and god-interface antipatterns). So *"make the seam first-class"* comes with a companion question — **how rich may a seam be before it is the system?** — which is an inf-sup-shaped condition, is not answered here, and should be carried as an open question rather than asserted away. That the classical theory already knows there is a price, and roughly what governs it, is itself an argument for adopting the framing under its own name.

### 9.2 Fated commitments — the third resident, and the one prior art may lack

> *"Is it helpful at all that a tile knows a less-resolved neighbor's fated seeds? … I'm a tile that shares an edge with 1/4 of a larger (less refined) tile — I ask it if it will be giving my water, taking, or both — it uses what it knows about itself and fated rng to just answer that for all four of its inner tiles, which now constrains its further refinement but gave the smaller tile the answer it needed."*

**First, the deflation, so the residue is clean.** For **law-evaluable** quantities this is already vivarium's nested-prior construction and, in the wider world, ordinary conditional simulation (sequential Gaussian simulation and its relatives): draw the coarse realization, simulate finer conditioned on it, and the coarse sample is the statistic the fine samples respect by construction. Hierarchical seeding of procedural worlds is likewise standard. Neither the conditioning nor the seeding is new.

**The residue is commitments about *evolved* state** — quantities that are path-dependent and materialized-only, which the coarse partition *cannot* evaluate even in principle, and about which it therefore publishes a statistically plausible draw rather than a computed value. That move has a different shape from anything in domain decomposition, and the difference is worth stating as a dichotomy.

Let $g$ be a seam observable whose true value depends on state not yet materialized. Two disciplines are available:

- **(D1) Reconciliation** — Schwarz waveform relaxation, halo iteration, integration-branch merge. Guess, solve both sides, exchange, iterate to a fixed point. Requires the parties to **co-exist in time**, requires a convergence obligation, and its cost is the iteration.
- **(D2) Commitment** — draw $g^{\ast}$ from the fated distribution at the coarse key, publish it as the seam's value, and constrain every later refinement to honor it. Requires **recomputability from a key** rather than from state. Requires no iteration and no co-existence in time. Its cost is a **declared error budget** $\delta = \lVert g^{\text{refined}} - g^{\ast}\rVert$, measured rather than eliminated — vivarium's unlawfulness-budget machinery, which is what makes a refinement that cannot honor the commitment a *measured violation* instead of a silent one.

*[Derived (commitment-is-the-only-discipline-on-non-decaying-observables)]* **Result 7.** (D1) is available exactly when the cone is bounded — the fixed-point iteration converges because widening the exchange window shrinks the disagreement. Result 5 established that for $\mu = 0$ observables the disagreement **does not shrink with the window**, so (D1) has no convergent form there. (D2) does not depend on $\mu$ at all, because it does not approximate a true value: **the commitment is the law, and the refinement's job is consistency with it.** Hence on non-decaying observables, commitment is not the better discipline — it is the only one.

This upgrades Result 5 from a prohibition to a constructive answer, which is the right direction and the reason Joseph's ideation is worth more than an extension.

**What fatedness actually buys, stated without overclaim.** The mid-flight reading offered was that fatedness makes the commitment *binding-by-construction rather than probabilistic.* That is close but wants one turn of precision: the binding is by construction *of the refinement operator*, which has to be built to honor the published draw — that remains an engineering obligation, not a mathematical necessity, and calling it automatic would be exactly the ghost this framework's landing discipline forbids. What fatedness genuinely and non-trivially buys is **recomputability from the key**: the commitment need not be stored, transmitted, or trusted, and any consumer, at any later time, in any build order, recovers the identical value. That is what distinguishes it from a stored promise — and note it is the *same* property, in a different dress, that Result 6b needed for keying and that `#form-depend-by-key-never-latest` requires for build-order independence.

**The discrete twin, which is what lands this in TST.** A fated commitment about evolved state is, in software, **an interface published before its implementation exists**: a writer who cannot yet know what its module will do publishes the schema, signature, or protocol, is thereafter bound by it, and a concurrent writer proceeds with *no exchange at all*. That is contract-first and schema-first development, and consumer-driven contract testing (Pact) is its enforcement instrument. The declared error budget is the **breaking-change budget** — divergence between the committed interface and what the implementation eventually wanted, measured in semantic-version majors and deprecation cycles rather than iterated away. TST already owns the upstream half of this in `#result-specification-bound` and its communication-bottleneck corollary; what Result 7 adds is *which* artifacts must be handled this way and why.

*[Derived (which-artifacts-must-be-contract-first)]* **Result 7a.** The artifacts that must be published-and-bound rather than merged are exactly the non-decaying ones from §8's discrete twin — namespaces, schemas, migration orderings, route tables, canonical-home assignments — because reconciliation has no convergent form on them. This is a derived criterion where the field has a practice: it says not *"contract-first is good discipline"* but *"here is the class on which nothing else works, and here is the test for membership."* It also explains the everyday observation that contract-first feels like ceremony on ordinary code and like oxygen on schemas — the discipline's value tracks $\mu$, and $\mu$ varies by artifact.

### 9.3 The three residents

Joseph's suggestion that a three-object taxonomy live *in* the seam space is right, and the mortar framing supplies the organizing axis rather than leaving it an enumeration. What a seam owns:

| Resident | Object | Decay in depth | Discipline | Vivarium home |
|---|---|---|---|---|
| **State datum** | halo of the neighbor's edge field | decays with $d$; $\mu \gt 0$ | (D1) reconciliation | `#form-same-level-halo-exchange` |
| **Flux record** | ledger of a conserved quantity crossing | single-valued by ownership; restricts across levels | (D1) with a conservation constraint | `#form-seam-flux-exchange`, `#form-face-flux-register` |
| **Fated commitment** | non-local scalar drawn at the coarse key | **does not decay**; $\mu = 0$ | (D2) commitment, with a declared budget | `#form-same-level-halo-exchange` FE(9) — named unbuilt |

The discriminating parameter across the rows is $\mu$ together with whether the quantity is conserved, which is what makes this a taxonomy rather than a list. Two of the three rows already exist in vivarium's tree; the third is named-and-unbuilt at HEAD as *"a per-basin spill scalar exchanged beside the halo, one number, keyed as a stage residual"* — which is Joseph's mechanism, instantiated, arrived at from the engineering side before the ideation was stated.

**Where the novelty-over-prior-art plausibly sits.** Mortar theory supplies rows 1 and 2 and the ownership argument; it has no third row, because classical mortar interfaces carry traces and fluxes of quantities that *exist*, and there is no commitment device where nothing is fated. Conditional simulation supplies the drawing mechanism but not the seam ontology or the binding obligation. So the candidate contribution is the **third row plus the criterion that selects it** (Result 7), sitting inside an adopted mortar ontology — which is the shape `agents.sop.md` *Prior art integration* prefers anyway: adopt the established structure under its own name, and let the new object be a first-class resident of it rather than a parallel construction.

**Honest status.** Results 6a–6c are structural and follow from the ontology once adopted. Result 7 is *conditional* on the (D1)/(D2) dichotomy being exhaustive, which I have argued but not proved — a third discipline may exist and I have not searched for one. Result 7a is *robust-qualitative*: the membership criterion follows from Result 5, but the claim that the named artifacts are the ones practitioners already treat this way is an appeal to observation I have not measured. The inf-sup-shaped richness question in §9.1 is **open** and is the most likely place this cluster gets its first real scar.

## 10. Prior art

A search was commissioned mid-spike and has landed. **It changes the verdict on Result 2b and it deflates one clause of Result 2a.** Nothing else moves, and two findings strengthen the cluster rather than weakening it.

The useful axis turned out not to be hit / no-hit but **which layer of the claim each finding takes** — the *criterion*, the *object*, the *estimation method*, or the *corollary*. Sorted that way, the picture is unusually clean: three different literatures each hold one layer, and none holds two.

### 10.1 Established, adopt by name

**On the continuous side, unchanged:** finite propagation speed and domains of dependence (Courant, Friedrichs & Lewy 1928); Lieb–Robinson bounds and their exponential-tail generalization (Lieb & Robinson 1972; Nachtergaele & Sims 2006; Hastings 2010); Schwarz waveform relaxation and domain decomposition (Gander), where *"how long may a subdomain run before it must exchange"* is the standard window question; mortar element methods (Bernardi, Maday & Patera 1994; Wohlmuth 2000) for §9.1; the Pearl–Bareinboim causal hierarchy theorem (Bareinboim, Correa, Ibeling & Icard 2022), already adopted at `#def-pearl-causal-hierarchy`.

**The criterion layer — and this is the finding that changes Result 2b.** **Smith, R. P. & Eppinger, S. D. (1997), "Identifying Controlling Features of Engineering Design Iteration," *Management Science* 43(3), 276–293** defines the **Work Transformation Matrix** $A$ — entries are the fraction of task $i$'s work recreated when task $j$ completes, a rework/propagation matrix over engineering elements estimated from practice — and states, in the paper's own words, that *"if the magnitude of the maximum eigenvalue is less than one, then the design process will converge"*, that by Perron–Frobenius the largest eigenvalue of a coupled nonnegative matrix is real and positive, and that *"the magnitude of each eigenvalue of $A$ identifies the geometric rate of convergence of one of the $n$ design modes."* Total work is the resolvent sum $\sum_M A^M u_0$.

**The Perron-root-of-a-propagation-matrix criterion, with the $(I-A)^{-1}$ bound and the geometric rate, is prior art from 1997 on a structurally identical object.** It is not software, not a probabilistic kernel, carries no distance statement and no concurrency reading — but a reviewer from the design-engineering side produces it immediately. See §10.4 for what this does to the claim. (Follow-on with a dynamical-stability wing: Yassine, Joglekar, Braha, Eppinger & Whitney 2003, *Research in Engineering Design* 14(3), 145–161, "the design churn effect.")

**The decay layer.** $\rho \lt 1 \Rightarrow$ exponential decay of influence in graph distance is standard probability, not a new derivation: **Dobrushin's uniqueness condition** (1968, 1970) with the decay-of-correlations theorem in **Künsch, H. (1982), "Decay of correlations under Dobrushin's uniqueness condition and its applications," *Comm. Math. Phys.* 84, 207–222.** §4.1's $\rho(K)^R$ is the multitype-branching instance of it. The honest framing is therefore *"we identify the co-change kernel as a Dobrushin-type influence matrix and read off the standard consequences"* rather than *"we establish that $\rho(K) \lt 1$ implies exponentially decaying reach"* — and the honest framing is also the **better** one, because it inherits sharp machinery, notably the historical row-sum $\to$ spectral-radius refinement (Dobrushin–Shlosman originally required row sums $\lt 1-\delta$; the spectral-radius improvement is later, and is now connected to spectral independence). §10.3 is where that refinement earns something.

**The object layer.** **Giffin, M., de Weck, O., Bounova, G., Keller, R., Eckert, C. & Clarkson, P. J. (2009), "Change Propagation Analysis in Complex Technical Systems," *ASME J. Mechanical Design* 131(8), 081001** estimates $K$ empirically over 41,500 change requests across 8 years and 46 subsystem areas, by *"counting the number of instances where changes were linked from area $m$ to area $n$, then dividing by the total number of changes in area $m$"* — literally `#def-system-coupling`'s kernel, published in 2009. They then define the **Change Propagation Index**, classifying each area as multiplier, carrier, or absorber from the out-minus-in change-count balance, and report *"a preponderance of change absorbers."*

This is good news rather than bad. **CPI is the node-local shadow of $\rho(K)$** — the absorber/multiplier distinction is exactly the sub-/supercritical intuition drawn by hand, with no threshold attached and no spectral object anywhere in the paper. The vocabulary originates at Eckert, Clarkson & Zanker 2004, *Research in Engineering Design* 15(1), 1–21. The spectral statement is the principled version of a distinction that literature has been making for twenty years.

### 10.2 Adjacent, deflationary, and worth citing positively

**Lubachevsky, B. D. (1989), "Efficient distributed event-driven simulations of multiple-loop networks," *CACM* 32(1), 111–123** (and the 1988 "Bounded lag distributed discrete event simulation"). Bounded Lag uses a window $B$ plus precomputed **minimum propagation delays** $d(i,j)$ to compute each logical process's **"reachability sphere"** — everything outside it provably cannot affect it within the window, and proceeds concurrently **with no coordination at all.** $\Theta(N/\log N)$ speedup, demonstrated on an $n \times n$ torus Ising model.

**This is a light-cone criterion imported into distributed coordination in 1989, used operationally to skip coordination — thirty-seven years before this spike.** It should be cited prominently and positively, and not citing it is the embarrassing outcome. The differences are real and are exactly the gap: $d(i,j)$ is a *known minimum delay*, so the bound is hard causal impossibility rather than a tail bound; the horizon is simulated time; and there is **no sub-/supercritical dichotomy** — bounded lag degrades gracefully rather than having a regime where no partition is isolable at any granularity. Establishing that the deterministic version is classical makes the probabilistic-kernel version a clearly-shaped gap rather than an unmotivated invention. (Degenerate one-hop ancestor: Chandy & Misra 1979; Bryant 1977. Survey: Fujimoto, *CACM* 33(10), 1990.)

**Pan et al. (2016), "CYCLADES: Conflict-free Asynchronous Machine Learning," *NIPS 2016*** — sample $B = (1-\varepsilon)n/\Delta$ updates from the conflict graph, and the largest connected component of the induced subgraph is $O(\log n / \varepsilon^2)$ with high probability, via a site-percolation phase transition on bounded-degree graphs (Krivelevich 2016). Subcritical shattering, used operationally to license concurrent writers as non-interacting.

**This is the most deflation-relevant hit for Result 2a's logarithmic clause** — same phenomenon, same underlying reason (the max over $n$ subcritical clusters is $\Theta(\log n)$), same purpose. It remains *same object, different criterion*: the threshold is on batch size relative to max degree, the conclusion bounds component **cardinality** rather than reach in graph distance, and there is no $\rho^R$. **So the logarithmic-margin clause should be stated as recovering a known phenomenon, not as a discovery.** But see §10.3 — the comparison also hands over a strengthening.

**Unchanged from the earlier draft:** CRDTs and operational transformation discharge the same obligation by restricting the operation algebra so concurrent writes commute unconditionally — the pair of ways to pay for isolation, not a competitor. **Vector clocks** measure the *realized* cone exactly where Lieb–Robinson *bounds* it a priori; the source-cohort provenance the vivarium agents adopted is a coarse vector clock, and this correctly deflates any novelty claim on the coordination-mechanism side.

**Bailis et al. (2014), "Coordination Avoidance in Database Systems," *PVLDB* 8(3)** (invariant confluence, necessary *and* sufficient) and **Hellerstein & Alvaro (2020), "Keeping CALM," *CACM* 63(9)** are a-priori and independence-licensing but **binary** — if I-confluence holds you never coordinate, if it fails you always must. Nothing in that line is *graded*, and the contrast is a clean asset rather than a threat. The nearest thing to a graded margin is **escrow / demarcation** (O'Neil 1986, *TODS* 11(4); Barbará-Millá & Garcia-Molina 1994, *VLDB Journal* 3(3); Magrino et al., EuroSys 2019) — write freely until a budget is exhausted — which is the **value-space** analogue of this criterion's **distance-space** margin, exact rather than probabilistic, with no graph.

**Two collisions to know about.** *(a)* **"Criticality" is already taken** in the change-propagation literature and means FMECA component criticality — how consequential a component is, not dynamical criticality (Ariyo, Eckert & Clarkson, ICED'07, is titled around "a criticality-based approach"). Unqualified use in a segment citing that line will be misread. *(b)* A **name collision on "Lieb-Robinson"**: search tooling confidently attributes optimistic concurrency control to it, and the actual referent is **Kung, H. T. & Robinson, J. T. (1981), "On optimistic methods for concurrency control," *ACM TODS* 6(2).* Anyone grepping this space will hit it. *(c)* Lesser: **Acar (2005), "Self-Adjusting Computation," CMU-CS-05-129** owns "change propagation" plus "distance bound" in an unrelated sense (edit distance on traces).

**Anticipate the ten-second pattern-match.** **Wang, Chakrabarti, Wang & Faloutsos (2003), "Epidemic spreading in real networks: an eigenvalue viewpoint," *SRDS 2003*, 25–34** (and Chakrabarti et al. 2008, *ACM TISSEC* 10(4)): the epidemic threshold on an arbitrary graph is $1/\lambda_1$ of the adjacency matrix. Every networks-literate reader will reach for this within seconds of seeing $\rho(K)=1$; naming it first is free.

### 10.3 The clean negatives, with the searched surface named

Searched: SE change-impact analysis (Hassan & Holt 2004 is a *recommender* — heuristics scored by precision and recall, no matrix algebra, no threshold; Yau & Collofello 1980 and Black 2001 measure ripple by *counting*); evolutionary-coupling and co-change mining (Zimmermann; Agrawal et al. 2020 — pairwise probabilities, i.e. $K$ again, stopping at ranking); the DSM / Design-Rule line; the engineering-design change-propagation line; SOC-in-software; package-ecosystem vulnerability propagation; the distributed-systems and concurrency-control literatures; the LOCAL model and self-stabilization; merge-conflict prediction.

Not found anywhere:

- **$\rho(K) \lt 1$ applied to *software* change propagation**, on a co-change or forced-follow-on kernel.
- **The threshold read as branching-process criticality** rather than as iteration convergence. No multitype branching model of software change exists at all.
- **Subcriticality as the precondition for partition isolability of concurrent writers** (Results 2a/2c).
- **An a-priori, distance-based, *probabilistic* non-interaction criterion for concurrent writers.** The deterministic analogue is §10.2's Bounded Lag; the subcritical-shattering analogue is CYCLADES; neither is this.
- **"Lieb–Robinson" imported into software or coordination at all.** The classical literature includes classical-system versions (Poulin, *PRL* 2010, covers classical Markovian dynamics), and every cross-domain application found is internal to physics and quantum information.
- **Any formal isolation criterion for AI-coding-agent concurrency (2025–2026).** That literature is entirely engineering practice — worktrees, per-agent databases, sequential merge points. Unclaimed space, and it is the motivating case.

**Where §4.2 is provably sharper than published practice.** CYCLADES' criterion is max-degree $\Delta$, which is the crude $\ell^\infty$ proxy for what $\rho(K)$ measures — and the $\ell^\infty \to$ spectral-radius refinement is precisely the one that already happened historically in the Dobrushin literature (§10.1). So the spectral form is not a reinvention of CYCLADES' bound; it is the refinement that literature's own history says is available. That is a real and citable improvement, and it is worth more than the logarithmic clause it replaces.

### 10.4 What this does to the claim

| Layer | Status |
|---|---|
| $\rho(A) \lt 1$ as a convergence/criticality criterion on a propagation-rework matrix | **Prior art** — Smith & Eppinger 1997. Adopt by name, cite. |
| $E[\text{cascade}]$ via the resolvent $(I-A)^{-1}$ | **Prior art** — same source. |
| Exponential decay of influence in graph distance from $\rho \lt 1$ | **Prior art** — Dobrushin; Künsch 1982. |
| Empirical estimation of $K = P(\text{change } j \mid \text{change } i)$ from change history | **Prior art** — Giffin et al. 2009; the co-change-mining line. |
| $\rho(K)$ applied to *software* change propagation | **Not found** across six literatures. |
| The threshold read as *branching* criticality rather than iteration convergence | **Not found.** |
| Subcriticality as the precondition for *partition isolability of concurrent writers* | **Not found.** |
| A-priori, distance-based, *probabilistic* non-interaction criterion | **Not found**; deterministic analogue is classical (1989). |
| Logarithmic isolation margin | **Same phenomenon published** (CYCLADES). Deflate this clause specifically. |

**Result 2b is relabeled: *adopted, cited* — not novel.** Stated as *"there is a criticality threshold at $\rho(K)=1$ for a propagation matrix,"* it is Smith & Eppinger 1997. Results **2a and 2c are where the novelty actually lives, and they survive intact** — the contribution is not the criterion but the **identification**: that `#def-system-coupling`'s kernel is a Dobrushin-type influence matrix and a branching offspring-mean matrix, that its Perron root therefore carries a threshold the co-change reading cannot supply, and that subcriticality is the precondition for concurrent isolability.

This makes **§4.3 more urgent rather than less.** Under the co-change reading, $\rho(K)$ borrows Smith & Eppinger's criterion without inheriting its *meaning* — their $A$ is a rework matrix with a definite iteration semantics, and a co-occurrence density has none. The forced-follow-on separation is what earns the borrowed criterion.

### 10.5 The finding that may be worth more than the deflation: software may sit *at* criticality

**Gorshenev, A. A. & Pis'mak, Yu. M. (2003/2004), "Punctuated equilibrium in software evolution," arXiv:cond-mat/0307201; *Phys. Rev. E* 70, 067103** measure code-modification avalanches from the version-control histories of Mozilla, FreeBSD and Emacs and report *"scaling laws typical for the self-organization criticality,"* fitting a Bak–Sneppen-style model. Relatedly Pang & Maslov (*PNAS* 110, 6235–6239, 2013) find scale-free component-frequency laws in Linux/Debian dependency networks.

Neither adjudicates this kernel. But **it is an empirical claim, from the same data source, that software change dynamics are critical rather than subcritical** — which is the obvious challenge to any architecture claim premised on $\rho(K) \lt 1$, and a reviewer who knows this literature will ask. *"We did not know"* is a bad answer and it is now foreclosed.

It may also be the more interesting result. If real codebases self-organize toward $\rho(K) \approx 1$, then §4.2's *"qualitative boundary across which a capability is lost"* is not a comfortable margin — **it is the attractor**, and concurrent development is chronically marginal rather than safely subcritical by default. That would explain, without appeal to culture or tooling, why parallel work on mature systems is persistently harder than the module structure predicts. It is a hypothesis, it is testable with exactly the measurement §4.2a already makes runnable, and it would be a stronger claim than the one this spike would otherwise carry. Flagged as the single most promising follow-on.

### 10.6 A correction owed to this project's own lit-review

The commissioned search found that `02-tst-core/lit-review/` **already staked out this program in May 2026**: `4-RESEARCH-GOALS-spectral-graph.md` states the hypothesis in essentially this form (*"when $\rho(A) \lt 1$, cascades are bounded; when $\rho(A) \geq 1$, unbounded propagation occurs"*, with the $1/(1-\rho)$ bound), and `next-research-append-6.md` §3.1 commissions it as a research goal, §5 specifying a multitype branching process for API lifecycles. **This spike is the execution of a program earlier agents scoped ten weeks ago, and the provenance should be stated wherever it lands.**

**And that directory carries a scope error worth flagging to its owner rather than repairing here.** `result-synthesis-append-4.md` concludes that *"spectral cascade analysis for software systems does not exist… an entire research area"*, and `undermind/05-empirical-spectral-tools.md` reports a complete absence. That verdict is true of the **software-engineering** corpus it sampled and overstated as written: the searching agent reports zero occurrences of Smith, Eppinger, Clarkson, Eckert, Giffin, MacCormack, Baldwin, or "design structure matrix" anywhere in the `lit-review/` tree beyond two glancing mentions of DV8 propagation cost. **The engineering-design change-propagation literature — which holds both the criterion and the kernel — was never searched.** Flagged, not edited: it is a different corpus, the finding is second-hand to me, and correcting someone else's search record is theirs to do.

### 10.7 Still open on the prior-art side

Three items, honestly unclosed. **(a)** **Eckert, Clarkson et al. (2022), "Concepts of change propagation analysis in engineering design," *Research in Engineering Design* 33(3)** — a survey of the whole field — could not be obtained (paywall). No primary source in that lineage carries a spectral criterion, so the inference is that the survey does not either, but that is inference, not verification. **(b)** A citation-forward sweep from Lubachevsky 1989 for a *probabilistic* relaxation of conservative parallel-discrete-event synchronization ("proceed unsafely with a priori bounded probability of causality violation") — searched by keyword and not found, but keyword search is the wrong instrument and this is the one place a real hit could still hide. **(c)** ImpactScale (ICSM/WCRE 2011), described as change impact via *"probabilistic propagation"* on dependency graphs, could not be obtained; probably a scoring metric, unverified.

---

## 11. Verdict, and what would land where

**Backbone: partial, and the partial-ness is the finding.** There is no single new law under which concurrent writers and eroding tiles fall. There is an imported template, two instantiations at opposite corners of it, and — from the *asymmetries* between the corners rather than from their commonality — four results that are new in AAT-internal settings.

**Where the honest homes are** (recommendations released to the standing cycle per `spikes.sop.md` §0c; no canon edits made, and the landing calls are Joseph's):

1. **`02-tst-core` — a concurrent-writers cluster, which is a real scope gap, stated accurately.** TST's *unit of analysis* is singular: `#scope-developer-agent` maps one agent onto the codebase, no segment takes two writers as its subject, and the volume's optimization target is one agent's time. But the volume is **not silent** — `#hyp-conceptual-alignment` carries a merge-conflict diagnostic (§4.2a) and `#hyp-causal-discovery-from-git` reasons about patterns surviving *"across multiple developers."* So the honest claim is a missing *scope segment and its consequences*, not a blank. Given that essentially all current software production — and every agentic session Joseph runs — is multi-writer, it remains the largest scope gap I found. Shape: a scope segment (concurrent writers over a partitioned codebase, carrying (P0)/(P2) as named premises and Result 4 as the enforcement condition), a derived segment for Results 2a/2b, a Discussion landing for Result 2c. **Lead with 2c** — a threshold-carrying second grounding for the oldest principle in the field.
2. **`#meas-coherence-coupling`, `#def-system-coupling`, and `#hyp-conceptual-alignment` — strengthenings rather than new homes, and the cheapest work here.** §4.3's forced-follow-on / co-change separation; §4.4's $\rho(K)$ as the principled answer to the ratio-form Working Note; and §4.2a's dissolution of the alignment diagnostic's ground-truth blocker, which turns an *"operationalizable but unmeasured"* quantity into a measurable one and is the single most runnable item in this spike.
3. **`#disc-identifiability-floor` — a new instance.** Results 3a/3b in the five-element shape, with the boundary route (promote the contract to a settable parameter) and the vivarium convergence as its worked instance. This is the most landable piece and the least dependent on anything unverified.
4. **`01-aat-core/#scope-multi-agent` — one paragraph, not a segment.** The scope segment's environment carries no metric and its transition no locality. Naming that as an explicit *absence* — with the note that imposing a metric is what makes partition-isolation statable, and a forward pointer to wherever (1) lands — is the honest minimum. Anything more is TST's business, not AAT's.
5. **Result 5 wants its own segment wherever (1) lands**, because it is the counter-intuitive *"are you sure you can't just widen the halo?"* kind, and `agents.sop.md`'s landing discipline says a non-obvious no-go earns its own demonstration rather than a caveat inside another claim.
6. **The §9 cluster splits across repos, and the vivarium half is the more urgent.** The seam ontology and the three residents are vivarium's own design question, live at its HEAD, and the third resident is already named-unbuilt there — that half wants a vivarium segment, not an ASF one, and `#form-seam-flux-exchange` / `#form-face-flux-register` / `#form-same-level-halo-exchange` are its neighbors. What belongs *here* is Result 7a — the criterion for which artifacts must be contract-first — which is a TST claim with an ordinary software instance and an unusually clean derivation, and which strengthens `#result-specification-bound` rather than sitting beside it. The mortar and inf-sup citations are the shared substrate; the charter's §5 dependency ledger is where a cross-repo entry would go if both halves land.

**Tier, honestly.** Result 1: *definitional / adopted*, cited not claimed. Result 2a: *conditional* on the branching model and on §4.3's kernel refinement, with its logarithmic clause marked as recovered rather than new. Result 2b: **adopted, cited** — not a novelty claim (§10.4). Result 2c: *conditional*, and the strongest candidate for elevation once the kernel question is settled. Results 3a/3b: *derived*, and 3b rests on an already-adopted external theorem. Result 4: *derived*, essentially structural. Result 5: *exact* for the sensitivity statement, *robust-qualitative* for the discrete twin, which is argued and not measured. Results 6a–6c: *derived*, and structural once the mortar ontology is adopted. Result 7: *conditional* on the (D1)/(D2) dichotomy being exhaustive — argued, not proved. Result 7a: *robust-qualitative*.

**The follow-on most worth running.** §10.5's tension: self-organized-criticality work reports power-law modification avalanches in real version-control histories, i.e. an empirical claim that software change dynamics are *critical* rather than subcritical. If real codebases self-organize toward $\rho(K) \approx 1$, the threshold is the attractor rather than a comfortable margin, and concurrent development is chronically marginal by default — a stronger and more interesting claim than the one this spike otherwise carries, testable with exactly the measurement §4.2a makes runnable.

**What is unverified and would change something.** The Courant attribution in §3 (named, with its probe). The three prior-art items §10.7 leaves open (the 2022 Eckert–Clarkson survey; a citation-forward sweep from Lubachevsky 1989; ImpactScale) — none of which would restore a novelty claim to Result 2b, whose adjudication is settled (§10.4), but any of which could add an owner to a §10.3 negative. The discrete twin of Result 5 has no measurement behind it — the vivarium instance is measured, the software instance is argued from structure. And the "un-cross-briefed strands" incident is the only piece of discrete evidence that might be a genuine cone overrun, and it is the one I understand least; it may be a coupling in the authors' model space rather than in the artifact, which is a fifth thing the formalism does not currently cover.

---

## 12. Feedback on the commissioning brief

Requested, and offered in the same spirit.

**The brief was right to state the claim at maximum ambition, and the maximum-ambition statement was subtly the wrong strongest version** — which is what the brief asked me to check. Its shape was *"these are one structure."* The stronger available statement is *"these are two corners of one template, and here is what each corner has that the other lacks"* — smaller in scope and larger in content, because the six asymmetries in §5's table are where Results 2b, 4, and 5 all live. A claim of sameness has nowhere to put a phase transition that exists on one side only.

**The brief's guess about TST fit was well-calibrated and its hedging was correct.** It guessed the volume treats software as temporal objects with dependency structure and that the multi-writer process would become a TST object; the actual fit is better than the guess, because `#def-system-coupling` is *already* a propagation kernel and `#def-discontinuity-distance` is *already* the metric — the machinery was waiting. The guess that domain-decomposition literature becomes importable as theory rather than metaphor is correct and is §9.

**One factual correction to relay.** The characterization of the day's agent incidents as *"precisely boundary-contract failures"* does not survive the formalism: three of the four are premise violations (undeclared write region), not cone overruns. This is not a weakening of the evidence base — it relocates it. The discrete instantiation's distinctive contribution turns out to be *that it must enforce what the continuous case gets for free* (§7), which is a better result than another instance of the same phenomenon would have been.

**And one thing the brief did that mattered.** Naming the prior art to check honestly *up front* — CRDTs, waveform relaxation, vector clocks — pre-committed the spike to deflation where deflation was due. §5's "the unification is imported, not made" is the finding I would most likely have talked myself out of if that list had not been in the brief, because the unified statement is genuinely pretty and it was mine.

**A delegation lesson from the prior-art commission, recorded because it generalizes.** Two failures in my own brief, both reported back by the agent and both real. *(a)* I named the neighborhoods to search — Hassan & Holt, Clarkson, MacCormack, DSM, percolation — and the agent worked that list roughly in order. **The single most consequential hit, Smith & Eppinger 1997, was not on it**, and arrived late from the DSM literature's *process* wing rather than its *product* wing; its own subagent reported the identical shape, with Bounded Lag arriving from a direction nowhere on the list it was given. This is `AGENTIC-DELEGATION.md`'s enumeration failure exactly — an investigator's checklist handed to the investigator forecloses the meta-move — and the cheap repair it names is one clause per item saying **which I had already checked and which were guesses**. I did supply that for the DSM propagation-cost item, and the agent reported it as the most useful line in the brief. *(b)* I wrote *"before I write anything down"* and withheld the spike file, which by then existed with a §10 that stated the commission precisely. That was not caginess; it was true of the *derivation* and false of the *write-up*, and the distinction did not surface for me. The agent found the file by grep at the two-thirds mark and said it immediately sharpened the targeting. **The generalizable rule: if an artifact exists that states the question better than the brief does, send the artifact.**

**On the two mid-flight ideations.** They arrived after §§1–8 were written, and they did what the brief's own framing hoped for rather than what a spec would have done: the seam-ontology vote *changed the base formalization* — §1 had boundaries as derived objects, and it should not have — and the fated-commitment idea converted the spike's sharpest prohibition into a constructive discipline. Neither would have been reachable from inside the formalism as I had set it up, which is the ordinary argument for why the ideation channel stays open mid-spike rather than waiting for a report. The one place I pushed back is recorded in §9.2: *binding-by-construction* wants a turn of precision, because the binding is by construction of the refinement operator and remains an engineering obligation. And the relayed reading of where novelty sits — the third seam resident — is, as far as this spike can establish, correct.
