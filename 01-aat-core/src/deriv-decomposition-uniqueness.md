---
slug: deriv-decomposition-uniqueness
type: derivation
status: exact
depends:
  - form-complete-agent-state
  - der-directed-separation
  - der-recursive-update
stage: draft
---

# Derivation: Decomposition Uniqueness — Underdetermination and Canonicity of the Epistemic/Purposeful Split

Appendix derivation resolving the uniqueness question left open in #form-complete-agent-state: is the decomposition $X_t = (M_t, G_t)$ forced, among decompositions preserving directed separation? The answer has two halves, and both are load-bearing. **Underdetermination:** preservation of directed separation alone does *not* force the decomposition — a two-line counterexample family exists inside GUC Class 1, because a frozen purposeful coordinate has the exact information-flow signature of a belief, and no property of the update algebra of a single agent can distinguish a stored setpoint from a stored fact. **Canonicity:** relative to a *goal-intervention family* — the operators that re-initialize the purposeful substate while leaving the epistemic substate alone — the decomposition is unique: under three named hypotheses, every separation-preserving decomposition's epistemic component is canonically isomorphic to the quotient of $X_t$ by goal-variation, which is $M_t$; the purposeful component is unique up to an explicitly characterized fiber-relabeling gauge. Together the halves say something sharper than the original conjecture aspired to: the belief/purpose partition is not discovered in the update dynamics, it is *carved by the intervention structure* — and once carved, it is carved uniquely. Defining the epistemic substate counterfactually (what is invariant under goal-variation) is therefore not one formulation choice among equals; it is the unique completion of the directed-separation condition.

The epistemic character parallels #deriv-recursive-update's C1/C2/C3 accounting: one hypothesis is structural, and two constitute a definitional commitment — to a particular intervention family — that cannot be "violated," only refused at the cost of leaving the partition underdetermined. The derivation is elementary throughout (congruence and quotient arguments); the machinery is standard, and the contribution is the identification, the counterexamples, and the gauge classification.

## Setup

We work with the lifted update system of #form-complete-agent-state in the structural representation of #deriv-recursive-update (Attack 5): state space $\mathcal X$, event set $\mathcal E$ (exogenous randomness absorbed into the event index), and update family $F_e : \mathcal X \to \mathcal X$, $F_e(X) = f_X(X, e)$. All statements are pathwise; the distributional version is discussed under Epistemic Status.

*[Definition (separated-decomposition)]*

A **separated decomposition** of $\mathcal X$ is a pair of maps $\mu : \mathcal X \to \mathcal M'$, $\gamma : \mathcal X \to \mathcal G'$ such that:

- **(D1) Product-completeness.** $(\mu, \gamma) : \mathcal X \to \mathcal M' \times \mathcal G'$ is a bijection onto the product.
- **(D2) Epistemic closure.** There exist maps $\phi_e : \mathcal M' \to \mathcal M'$ with $\mu(F_e X) = \phi_e(\mu(X))$ for all $X \in \mathcal X$, $e \in \mathcal E$.
- **(D3) Cascade form.** There exist maps $\gamma_e$ with $\gamma(F_e X) = \gamma_e\big(\gamma(X),\, \mu(F_e X)\big)$ — the purposeful update reads the *updated* epistemic component, matching #der-directed-separation's $f_G(G_{\tau^-}, M_{\tau^+}, e_\tau)$ form.

(D2) says the equivalence kernel of $\mu$ is a **congruence** of the update system — $\mathcal M'$ is a factor (quotient) dynamical system whose update references nothing outside $(\mu(X), e)$. This is the entire formal content of "preserves directed separation": in the lifted state, "does not reference purpose" can only mean "does not reference the complementary coordinate."

The base decomposition $\mu_0(m, g) = m$, $\gamma_0(m, g) = g$ of an agent satisfying directed separation is a separated decomposition, directly from #der-directed-separation's update forms.

*[Definition (decomposition-isomorphism)]*

Two separated decompositions $(\mu, \gamma)$, $(\mu', \gamma')$ are **isomorphic** when there are bijections $\alpha : \mathcal M' \to \mathcal M''$ and $\beta : \mathcal G' \to \mathcal G''$ (the latter possibly fibered over $\mathcal M'$) with $\mu' = \alpha \circ \mu$, $\gamma' = \beta \circ (\mu,\gamma)$, such that $\alpha$ intertwines the epistemic updates ($\alpha \circ \phi_e = \phi'_e \circ \alpha$) and the transported purposeful update satisfies (D3). Isomorphism of factored dynamical systems, not of bare sets: equality of the epistemic congruence up to relabeling, plus a fiber bijection compatible with the dynamics.

**Lemma 0 (the cascade form is a genuine extra condition exactly when epistemic updates lose information).** Given (D1)+(D2), $\gamma(F_e X)$ is automatically *some* function of $(\mu(X), \gamma(X), e)$. (D3) additionally requires the $\mu(X)$-dependence to factor through $\phi_e(\mu(X))$. If each $\phi_e$ is injective, this is no restriction ($\mu(X) = \phi_e^{-1}(\mu(F_e X))$); if some $\phi_e$ is non-injective, (D3) can fail for decompositions satisfying (D1)+(D2) (explicit witness in the gauge proposition below). $\square$

## Underdetermination

*[Derived (separation-underdetermination)]*

**Proposition 1.** Preservation of directed separation — (D1)–(D3) — does not determine the decomposition up to isomorphism. Two counterexample families:

**(a) Trivial factor.** $\mu = \mathrm{id}_{\mathcal X}$, $\mathcal G' = \{\ast\}$. (D1) holds; (D2) holds with $\phi_e = F_e$ — the update references no complementary coordinate because there is none; (D3) holds vacuously. The "epistemic" component is the entire state, purpose included.

**(b) Frozen-coordinate migration.** Let the base agent satisfy directed separation, with $G = (c, G_{\mathrm{rest}})$, $\mathcal G = \mathcal C \times \mathcal G_{\mathrm{rest}}$, where $c$ is any purposeful coordinate whose update is self-contained and goal-blind — the canonical case: an objective held fixed over the analysis window, $c_{\tau^+} = c_{\tau^-}$ (per #def-strategy-dimension's typical timescale ordering $\nu_M \gg \nu_\Sigma \gg \nu_O$, the generic condition between objective revisions). Then $\big((M, c),\, G_{\mathrm{rest}}\big)$ is a separated decomposition: (D1) by construction; (D2) since, writing $Y := (M, c)$, the update $Y_{\tau^+} = (f_M(M_{\tau^-}, e),\, c_{\tau^-})$ depends only on $(Y_{\tau^-}, e)$; (D3) since $c_{\tau^-} = c_{\tau^+}$ is recoverable from the updated epistemic component, so $G_{\mathrm{rest}, \tau^+} = f_{G_{\mathrm{rest}}}((c_{\tau^+}, G_{\mathrm{rest}, \tau^-}), M_{\tau^+}, e)$ is of the required form. Its epistemic component $\mathcal M \times \mathcal C$ is not isomorphic to $\mathcal M$: any intertwining bijection would have to collapse $\mathcal C$, but $c$ is dynamics-preserved and separates trajectories. $\square$

**What the counterexample shows.** Family (b) lives inside GUC Class 1 — a Kalman-filter-plus-LQR agent with a fixed reference admits both readings. A frozen goal has the information-flow signature of a belief: it updates on nothing, references nothing, and is read by the purposeful update exactly as beliefs are. The distinction between a stored setpoint and a stored fact is invisible to the update algebra of a single agent, because that algebra never exercises *variation of the goal*. The distinction must be supplied by additional structure — and the structure that supplies it is interventional.

**Cross-cutting decompositions, classified.** A "relevance-weighted model" $W = w(M, O)$ mixing belief and objective is either not a separated decomposition at all — generically $W_{\tau^+}$ requires $M$ and $O$ separately, violating (D2) — or, when $w$ is injective and the mixed-in purposeful content is update-frozen, a re-coordinatization of family (b). Cross-cutting decompositions are non-separated or frozen-coordinate instances; there is no third kind. (Such representations may of course still be *useful* — as derived quantities. The proposition only settles that they are not competing separation-preserving carvings of the state.)

## Canonicity

*[Definition (goal-intervention-family)]*

The **goal-intervention family** is the set of operators $\iota_g : \mathcal X \to \mathcal X$, $g \in \mathcal G^\dagger \subseteq \mathcal G$, acting in base coordinates as $\iota_g(m, \gamma) = (m, g)$: re-initialize the purposeful substate, leave the epistemic substate untouched. **Full intervention access** is the case $\mathcal G^\dagger = \mathcal G$. Let $\sim_{\mathrm{cf}}$ be the equivalence relation on $\mathcal X$ generated by $\{X \sim \iota_g X : g \in \mathcal G^\dagger\}$, and $q : \mathcal X \to \mathcal X/\!\sim_{\mathrm{cf}}$ the quotient map — the **goal-variation quotient**.

*[Definition (admissibility-hypotheses)]*

For a separated decomposition $(\mu, \gamma)$:

- **(R1) Product-completeness** — (D1) above (repeated as a named hypothesis because it does independent work: it excludes injective-but-not-surjective "copy" embeddings that smuggle epistemic content into the purposeful component as a constrained duplicate coordinate).
- **(R2) Purposeful purity** — $\mu \circ \iota_g = \mu$ for all $g \in \mathcal G^\dagger$: the epistemic component contains nothing goal-intervention can move.
- **(R3) Epistemic completeness** — the map $\mathcal X/\!\sim_{\mathrm{cf}} \to \mathcal M'$ induced by $\mu$ (well-defined under (R2)) is injective: the epistemic component retains everything goal-intervention cannot move.

**Lemma 1 (congruence lattice).** The congruences of the update system $(\mathcal X, \{F_e\})$ are closed under arbitrary intersection, hence form a complete lattice; in particular, for any relation $R$ on $\mathcal X$ there is a finest congruence containing $R$ (the congruence closure). *Derivation:* if $\{C_i\}$ are congruences and $X \,(\bigcap_i C_i)\, Y$, then for each $i$, $F_e X \; C_i \; F_e Y$, so $F_e X \,(\bigcap_i C_i)\, F_e Y$; the closure is the intersection of all congruences containing $R$, non-empty since the total relation is one. $\square$

*[Derived (decomposition-canonicity, from directed separation + full intervention access)]*

**Theorem 2.** Let the base agent satisfy directed separation and assume full intervention access. Then:

**(i)** $\sim_{\mathrm{cf}}$ is a congruence, its classes are $\{m\} \times \mathcal G$, and the goal-variation quotient is a separation factor canonically isomorphic to $\mathcal M$: $\mathcal X/\!\sim_{\mathrm{cf}} \cong \mathcal M$ via $[(m, \gamma)] \mapsto m$, intertwining the updates.

**(ii)** Every map $\mu$ satisfying (R2) factors through $q$: $\mu = \theta \circ q$ for a unique $\theta$.

**(iii)** Every separated decomposition satisfying (R1)–(R3) has $\mu = \alpha \circ q$ with $\alpha$ a bijection intertwining the updates. The epistemic component of any admissible decomposition *is* the goal-variation quotient — is $M_t$ — up to canonical isomorphism of factor dynamical systems.

*Derivation.* (i) The load-bearing computation is the commutation identity, which uses directed separation of the base agent essentially:

$$F_e(\iota_g(m, \gamma)) = \big(f_M(m, e),\; f_G(g,\, f_M(m, e),\, e)\big) = \iota_{g'}\big(F_e(m, \gamma)\big), \qquad g' := f_G(g,\, f_M(m, e),\, e).$$

The first coordinate is goal-independent precisely because $f_M$ has no $G$ argument; under full access $g' \in \mathcal G^\dagger$ automatically. So $F_e$ maps generators of $\sim_{\mathrm{cf}}$ to generators, hence classes to classes: $\sim_{\mathrm{cf}}$ is a congruence. Under full access the generated classes are exactly $\{m\} \times \mathcal G$ (any two goal values are connected by one intervention), so $[(m, \gamma)] \mapsto m$ is a bijection, and the quotient update is $[\,\cdot\,] \mapsto [F_e(\cdot)]$, which in the $m$-coordinate is $f_M(\cdot, e)$: the intertwining is immediate. The complementary coordinate $\gamma_0 = g$ gives (D3) directly from #der-directed-separation's $f_G$ form, so the quotient participates in a separated decomposition.

(ii) $\mu \circ \iota_g = \mu$ makes $\mu$ constant on generators, hence on the generated classes; the factorization and its uniqueness are the universal property of the quotient.

(iii) By (ii), $\mu = \theta \circ q$; $\theta$ is injective by (R3) and surjective because $\mu$ is (a coordinate of the bijection (R1)). Intertwining: $\theta(q(F_e X)) = \mu(F_e X) = \phi_e(\mu(X)) = \phi_e(\theta(q(X)))$, and $q(F_e X) = \bar\phi_e(q(X))$ by (i), so $\theta \circ \bar\phi_e = \phi_e \circ \theta$. Compose with (i)'s isomorphism to land on $\mathcal M$. $\square$

*[Derived (goal-fiber-gauge)]*

**Proposition 3 (the purposeful component is a gauge).** Fix the epistemic component as in Theorem 2(iii). The remaining freedom is exactly the choice of fiber coordinate: any $\gamma' = \beta \circ (\mu_0, \gamma_0)$ with every $\beta_m := \beta(m, \cdot) : \mathcal G \to \mathcal G'$ bijective satisfies (D1)+(D2) and yields the same decomposition-isomorphism class. Within this family, the sub-family additionally satisfying the cascade form (D3):

- contains every $m$-independent relabeling $\beta(m, g) = \beta_0(g)$ (the transported update $\gamma'_e(g', m^+) = \beta_0(f_G(\beta_0^{-1}(g'), m^+, e))$ is of the required form);
- equals the *full* family when every $\phi_e = f_M(\cdot, e)$ is injective (epistemically invertible updates: $m^-$ is recoverable from $(m^+, e)$, Lemma 0);
- is in general strictly between. *Witness for strictness:* $\mathcal M = \mathcal G = \{0, 1\}$, a single event with $f_M \equiv 0$ (total epistemic collapse) and $f_G(g, m^+, e) = g$; the gauge $\beta(m, g) = g \oplus m$ satisfies (D1)+(D2), but the transported purposeful update would need to produce $g$ from $(g \oplus m,\, m^+ = 0,\, e)$, and $m$ has been destroyed — (D3) fails. $\square$

The exact characterization of the (D3)-respecting gauge subgroup for partially-invertible epistemics is open (see Working Notes).

*[Derived (restricted-intervention-access)]*

**Corollary 4 (restricted families — the two halves are one phenomenon).** Under restricted access $\mathcal G^\dagger \subsetneq \mathcal G$, Theorem 2 holds with $\mathcal X/\!\sim_{\mathrm{cf}}$ in place of $\mathcal M$, where the classes are now $\{m\} \times R(\gamma)$ for the reachability classes $R$ of the intervention family (closed under the dynamics via the commutation identity, so the quotient remains a congruence when the base agent is separated and $f_G(g, \cdot, \cdot)$ preserves reachability classes for $g \in \mathcal G^\dagger$). The canonical epistemic component is then $\mathcal M \times (\mathcal G / R)$: **purposeful distinctions the intervention family cannot move classify as epistemic.** Proposition 1(b) is exactly this corollary's boundary case — a frozen coordinate *with* intervention access is excluded from $\mathcal M'$ by (R2); a frozen coordinate *without* intervention access genuinely belongs to the canonical epistemic component. The counterexample to the naive conjecture and the boundary behavior of the theorem are the same fact. $\square$

*[Discussion]*

**Corollary 5 (separation failure — GUC Class 3).** When the base agent violates directed separation, the commutation identity fails ($f_M$ has a $G$ argument, so the first coordinates differ), $\sim_{\mathrm{cf}}$ is not a congruence, and no separation factor realizes the goal-variation quotient. The canonical epistemic object is then the quotient by the congruence *closure* $\overline{\sim_{\mathrm{cf}}}$ (Lemma 1), which is strictly coarser: goal-coupled belief-update does not merely blur the belief/goal boundary, it shrinks the largest belief-like factor that can exist at all. The information gap between $\mathcal X/\!\sim_{\mathrm{cf}}$ and $\mathcal X/\overline{\sim_{\mathrm{cf}}}$ is a structural (architecture-level) companion to the distributional $\kappa_{\text{processing}}$ of #der-directed-separation — discussion-grade here; not developed further in this segment.

## What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| (D2) is the whole formal content of "preserves directed separation" | Analysis of what "does not reference purpose" can mean in the lifted state | Discussion-grade (clarifying observation) |
| Separation underdetermines the decomposition (Proposition 1) | Counterexample families (a), (b) | Proved (constructive) |
| Cross-cutting decompositions are non-separated or frozen-coordinate instances | Closure analysis on $w(M, O)$ | Proved (case analysis) |
| Goal-intervention family $\{\iota_g\}$ | Modeling input — the counterfactual apparatus | Definition (the analog of #deriv-recursive-update's C3: a commitment, not a discovery) |
| (R1) product-completeness | Structural hypothesis (blocks redundancy-smuggling) | Assumption (structural) |
| (R2) purity + (R3) completeness | The two directions of the counterfactual anchor (block the two degenerate ends) | Definition (jointly: $\mathcal M'$ *is* the goal-variation quotient) |
| Canonicity under (R1)–(R3) (Theorem 2) | Commutation identity + quotient universal property | Proved |
| Goal-fiber gauge classification (Proposition 3) | Direct construction + collapse witness | Proved (endpoints); open (middle) |
| Restricted-access behavior (Corollary 4) | Reachability-class quotient | Proved (under stated closure condition) |
| Class 3 behavior (Corollary 5) | Congruence closure | Discussion-grade |

Each hypothesis is individually necessary: dropping (R1) readmits the copy embedding, dropping (R2) readmits Proposition 1's families, dropping (R3) readmits the everything-is-goal decomposition ($\mu$ constant). The hypothesis set is minimal in this checkable sense.

## Epistemic Status

*Exact, pathwise, with a partly definitional character.* Proposition 1, Theorem 2, Proposition 3, and Corollary 4 are elementary derivations, exact under the stated hypotheses in the structural (randomized-function) representation of #deriv-recursive-update Attack 5 — all statements are pathwise in the exogenous randomness. Two honest boundaries. **(1) Distributional version open.** A kernel-level analog would route through strong lumpability of the update kernels; lumpable partitions are not in general closed under common refinement, so Lemma 1's meet-closure argument does not transfer as-is, and the distributional statement is neither asserted nor refuted here. **(2) The intervention family is a commitment.** (R2)/(R3) are relative to $\{\iota_g\}$; the theorem does not derive which interventions are physically available on a given architecture — that is an empirical and architectural question (for language-model agents, the prompt-vs-weights question). The accounting parallels #deriv-recursive-update: the partition is not discovered in the update algebra; it is carved by the intervention structure, and the theorem's content is that the carving, once committed to, is unique. Refusing the commitment is coherent, at the cost of the underdetermination Proposition 1 exhibits.

## Discussion

**What this settles for #form-complete-agent-state.** The lift $X_t = (M_t, G_t)$ was introduced as a formulation choice with an unproved uniqueness conjecture. The resolution is asymmetric: as a claim about the update factorization alone, uniqueness is *false* (Proposition 1); as a claim relative to the goal-intervention family, it is *true* (Theorem 2), and the residual freedom is exactly a relabeling gauge on the goal fiber (Proposition 3). The formulation-choice honesty survives in refined form: what remains chosen is the intervention family; what is forced given it is everything else.

**The counterfactual definition of belief is the unique completion of directed separation.** Proposition 1(b)'s moral is that beliefs and frozen purposes are congruent under every purely dynamical criterion — the single-agent factual trajectory never exercises the difference. The structure that *does* exercise it is goal-variation, and Theorem 2(iii) says the quotient by goal-variation is the only admissible epistemic component. Read as methodology: defining $M_t$ counterfactually — the invariant of the state under interventions on what the agent wants — is not a stylistic alternative to defining it structurally; the structural definition underdetermines and the counterfactual one is forced. This is the formal backbone for treating the coupling question as what carves the partition, rather than the partition as prior to the coupling question.

**Pearl-rung reading.** The goal-intervention operators are internal to the agent formalism (no dependency on the causal-hierarchy machinery is needed for the derivations), but the correspondence is worth naming: distinguishing belief from frozen purpose is a rung-2 question about the agent — no statistic of one observed (rung-1) trajectory settles it, since Proposition 1(b)'s two readings agree on every factual trajectory; the goal-variation quotient is exactly what interventional access to the goal makes well-defined. The same shape as the framework's other identifiability results: the boundary is crossed by promoting the quantity in question (here the goal) to a settable parameter.

**Restricted access is the operative case for real architectures.** For a Kalman + LQR agent, the reference input is a design parameter — full access, clean partition. For a language-model agent, prompt-level goal-setting is a rich-but-partial intervention family (it cannot reach goal-content baked into weights), and Corollary 4 predicts the honest consequence: weight-level purposeful content classifies as *belief* under prompt-level counterfactuals. The partition delivered by the counterfactual definition is only as fine as the intervention family that defines it — a scope statement, not a defect, and the reason the definition must always name its family.

## Working Notes

- **Open (main line):** the distributional/kernel-level analog — whether some weakening of strong lumpability restores meet-closure for the relevant sub-family of partitions, or whether a counterexample blocks any kernel-level canonicity. Neither constructed nor refuted this cycle.
- **Open:** exact characterization of the (D3)-respecting gauge subgroup between the two attained endpoints of Proposition 3 (partially-invertible epistemics) — expected shape: $\beta_m$ measurable with respect to the information about $m$ surviving into $(m^+, e)$.
- **Open (follow-on candidate):** quantifying Corollary 5's information gap for GUC Class 3 architectures as an architectural companion to $\kappa_{\text{processing}}$; natural home `03-llm-core/` if pursued.
- **Prior-art status.** The machinery is standard and imported by name: congruence lattices and quotient algebras (universal algebra — Burris & Sankappanavar, *A Course in Universal Algebra*), factorization/bisimulation quotients of transition systems (Park; Milner), Markov lumpability (Kemeny & Snell, *Finite Markov Chains*), and — closest in spirit — causal abstraction's intervention-commuting maps between models (Rubenstein et al. 2017, "Causal consistency of structural equation models"; Beckers & Halpern 2019) and the coarsest-partition constructions of causal feature learning (Chalupka, Perona & Eberhardt). These citations are from working knowledge; primary-source verification and a targeted novelty search on the specific result (uniqueness of an epistemic/purposeful state factorization relative to a goal-intervention family, with the gauge classification) are queued and must precede any external novelty claim. Reasoning trail: `spikes/spike-decomposition-uniqueness-2026-08-24.md`.
