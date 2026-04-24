---
slug: sector-persistence-template
type: result
status: exact
depends:
  - sector-condition-derivation
stage: draft
---

# Result: Sector-Persistence Template

Any state variable evolving under bounded-correction dynamics with bounded disturbance admits the same Lyapunov persistence argument. AAD's persistence-flavored results — epistemic, strategic, team, composite closure, composite tempo, adversarial destabilization — are instances of a single template. This segment states the template once in parameter-free form so that each instantiation can cite it and specify only what varies: its state variable, correction function, effective disturbance rate, and reserve.

## Formal Expression

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

The Model D result scales as $1/\alpha$; the Model S result scales as $1/\sqrt{\alpha}$ — correction is less effective against noise than against drift. This scaling difference propagates into the adversarial exponent regimes ( #adversarial-exponent-regimes): $b = 2$ under Model D, $b = 3/2$ under Model S.

### Instantiations in AAD

The template is invoked across six segments. Each specifies its own $(\xi, F, \rho_\xi, R)$ and verifies (T1)–(T3) locally:

| Segment | $\xi$ | Effective $\rho_\xi$ | $R$ | Locally-verified precondition |
|---|---|---|---|---|
| #persistence-condition | $\delta_t$ (epistemic mismatch) | $\rho$ (environmental disturbance rate) | model-class capacity, or task-adequacy threshold $\lVert\delta_{\text{critical}}\rVert$ if stricter | (T2) via #gain-sector-bridge |
| #strategy-persistence-schema | $\delta_\Sigma$ (strategic mismatch) | $\rho_\Sigma$ (rate of edge invalidation) | $R_\Sigma$ (strategic reserve) | (T2) via Beta-Bernoulli edge updates ( #strategic-dynamics-derivation Props B.1–B.6); constant-$\alpha$ requires experience discounting |
| #team-persistence | $\delta_i$ (sub-agent mismatch) | $\rho_i^{\text{eff}} = \rho_{i,\text{env}} + \sum_j \gamma_{j\to i}^{\text{adv}}\mathcal T_j - \sum_j \gamma_{j\to i}^{\text{coop}}\mathcal T_j$ | $R_i$ | Cooperative coupling can drive $\rho_i^{\text{eff}}$ below the single-agent $\rho$ |
| #composition-closure (bridge lemma) | $e_m$ (trajectory error at macro-boundaries $m$) | $\varepsilon^\ast \nu_c$ (closure-defect per macro-step $\times$ macro-update rate) | the composite's $R_c$ | Tier-specific contraction stronger than (T2): incremental sector bound (DA2'-inc). Tier 1 proved; Tier 2 local; Tier 3 domain-specific |
| #derived-tempo-composition | $\delta_c$ (composite mismatch) | $\rho_{\text{ext}} + \varepsilon^\ast \nu_c$ (external + internal) | $R_c$ | (T3) requires the bridge-lemma contraction; $C_{\text{coord}} \geq \varepsilon^\ast\nu_c$ is the tempo-equivalent of the internal disturbance |
| #adversarial-destabilization | $\delta_B$ (target-agent mismatch) | $\rho_{B,\text{base}} + \gamma_A \mathcal T_A$ (Model D) or $\sigma_{B,\text{base}} + \gamma_A \mathcal T_A$ (Model S) | $R_B$ | Destabilization is the negation of persistence: (T3)'s coupling-amplified disturbance violates $\alpha R \gt \rho_\xi$ |

The same Lyapunov argument applies in every row. What varies is how each instantiation defines its state variable, its correction function, and — most importantly — what counts as "effective disturbance" for its context (environmental noise, adversarial coupling, closure defect, or a decomposition of these).

### External mathematical lineage: monotone-operator theory

The sector-Lyapunov apparatus this segment factors out has a well-established mathematical home: AAD's sector condition (T2) is a **one-point strong monotonicity** condition in the sense of Rockafellar 1970 (*Convex Analysis*, §24) anchored at the equilibrium $\xi^\ast = 0$, and the incremental strengthening DA2'-inc required by `#composition-closure`'s bridge lemma is **full two-point strong monotonicity** in the Bauschke-Combettes 2017 (*Convex Analysis and Monotone Operator Theory in Hilbert Spaces*, 2nd ed., §§22–28) monotone-operator framework. The Lyapunov-plus-Grönwall argument proving the Model D ultimate bound and the Itô-Lyapunov argument proving Prop A.1S are standard specializations of the **monotone-operator perturbation theorem** (Bauschke-Combettes Thm 5.14–5.16; Parikh & Boyd 2014, *Proximal Algorithms*, §2). Banach-Picard contraction under bounded perturbation, monotone-operator convergence under square-summable noise, operator-splitting for composite systems (Douglas-Rachford, ADMM) — the full supporting apparatus is available in that literature.

AAD's relationship to monotone-operator theory is *specialization + repurposing*, not generalization. AAD-distinctive content: (i) **one-point anchoring at the equilibrium** — strictly weaker than full two-point strong monotonicity, matched to fixed-point-at-target semantics, admitting agent classes (PID-bounded-plant, variational-approximate) where full monotonicity fails but persistence-at-the-target is available. (ii) The **Model D / Model S disturbance decomposition** with distinct $1/\alpha$ vs $1/\sqrt\alpha$ scaling — monotone-operator theory has perturbation theorems but no systematic bounded-adversarial vs stochastic-zero-mean split propagating to adversarial-exponent regimes at $b = 2$ vs $b = 3/2$. (iii) Composition with the `#discussion-identifiability-floor` meta-pattern supplies a second (information-theoretic) axis orthogonal to the operator-theoretic machinery. (iv) The `#postulate-composition-consistency` postulate operates at AAD's level of description (agent / composite / macro-agent) rather than at the abstract operator level. (v) The sub-scope α/β epistemic labeling is scope-honesty, not a mathematical partition — it tracks which agent classes give the monotone-operator structure *by construction* versus *by per-instance verification*.

This acknowledgment is load-bearing for scope honesty: the mathematical machinery is established external to AAD; AAD's distinctive content is the agent-architecture specialization (singular-trajectory identity per `#scope-agent-identity`; signed-coupling composition; coordinate-forcing via uniqueness theorems per `#discussion-additive-coordinate-forcing`; three meta-patterns) rather than novel monotone-operator mathematics. `#sector-condition-derivation`'s Grounding paragraphs name the specific operator-family correspondence (proximal / firmly-nonexpansive / cocoercive / strongly-monotone-gradient / linear-PD) for the five sub-scope-α agent classes. `#contraction-template` extends to non-Euclidean metrics via Lohmiller-Slotine differential-contraction (also within the broader monotone-operator lineage). The honest limits of the unification: the coarse-graining projection $\Lambda$ (#composition-closure) does not fit the operator-sector primitive (heterogeneous spaces, three independent admissibility conditions); three of five metric-α₂ cases in `#contraction-template` remain theorem-imported rather than AAD-internally derived; the identifiability-floor axis is orthogonal to the operator-sector axis.

### Comparison with the FEP-flow stability argument

Active inference's stability arguments come from the geometry of the variational free-energy landscape — agents are argued to flow toward the minimum of variational free energy on a non-equilibrium-steady-state (NESS) density. The primary source for the NESS-density framing is Friston 2019, "A free energy principle for a particular physics," arXiv:1906.10184; the path-integral / particular-kinds methodological extension is Friston, Da Costa, Sakthivadivel, Heins, Pavliotis, Ramstead & Parr 2023, "Path integrals, particular kinds, and strange things," *Phys. Life Rev.* 47 (which rewrites the FEP-flow argument in path-integral language rather than proving new stability bounds). Aguilera, Millidge, Tschantz & Buckley (2022, "How particular is the physics of the free energy principle?", *Phys. Life Rev.* 40:24–50) showed that the FEP-flow argument's mathematical validity is narrow: the NESS-density framing holds only in a small parameter regime for non-equilibrium linear stochastic systems, and natural extensions (nonlinear, non-Gaussian, non-equilibrium) often fall outside the proven regime.

The AAD persistence template is structurally different: it is a Lyapunov-based argument requiring only (T1) zero-correction-at-zero-state, (T2) local sector condition (correction points inward), and (T3) bounded disturbance — all of which are checked locally for each instantiation ( #sector-condition-derivation Props A.1, A.1S, A.2). The template applies to bounded and to mean-square-stochastic disturbance, gives explicit ultimate-bound and adaptive-reserve formulas, and does not depend on NESS structure or on a free-energy gradient.

The breadth difference is not rhetorical: where the FEP-flow argument's parameter regime is debated in the AI literature itself, the sector-Lyapunov apparatus is the standard machinery of nonlinear control theory (Khalil 2002, *Nonlinear Systems*, 3rd ed., Prentice Hall, ch. 4) and applies wherever (T1)–(T3) hold. This is one of AAD's stronger structural positions and is worth making explicit when comparing AAD to active inference: AAD does the persistence work AI tries to do, with broader validity and explicit ultimate-bound formulas.

## Epistemic Status

*Exact.* The template is the abstract form of the Lyapunov result proved in #sector-condition-derivation (Props A.1, A.1S, A.2). The proofs transfer without modification whenever (T1)–(T3) hold; the template's contribution is the recognition that AAD's persistence-flavored results are instances of a single pattern and the enumeration of what each instantiation must verify.

**On (T2) and A2' sub-scoping.** (T2) is the local sector condition A2' transcribed to a generic state variable $\xi$. Within the state-variable spaces relevant to AAD's instantiations (epistemic mismatch $\delta$, strategic mismatch $\delta_\Sigma$, sub-agent mismatch $\delta_i$, composite trajectory error $e_m$, composite mismatch $\delta_c$, target-agent mismatch $\delta_B$), the update rules are overwhelmingly sub-scope $\alpha$ in the #sector-condition-derivation / #gain-sector-bridge sense — Bayesian, exponential-family, strongly-convex-gradient, or linear-PD. For these, (T2) is *derived* from the update-rule structure under B1 directional fidelity. For sub-scope $\beta$ instantiations (e.g., a team where some sub-agent runs a rule-based update), (T2) must be verified per-instantiation. This is not a weakening — it is the honest sub-scope labeling inherited from #sector-condition-derivation.

**On Prop A.1S region-awareness.** The Model S case uses the region-aware form of Prop A.1S (stopped bound + non-exit probability under the mean-square persistence condition). Instantiations that rely on the Model S result automatically inherit the stopping-time localization — no extra work is required at the template level.

Max attainable: *exact*. The result is as strong as Lyapunov stability theory. Additional work could extend the template (state-dependent noise, time-varying $\alpha$, non-quadratic Lyapunov functions) but would not strengthen it within its stated scope.

**What the template does not establish:**

- *Quantitative convergence rates.* Lyapunov gives stability and ultimate bounds, not convergence speed. Specific rates require instantiation-level analysis.
- *Behavior outside the sector-condition region.* (T2) holds only for $\lVert\xi\rVert \leq R$. Beyond $R$, correction may break down — the structural-adaptation regime of #structural-adaptation-necessity.
- *Time-varying parameters.* The template assumes constant $\alpha$ and $R$. Time-varying cases require additional machinery. #strategy-persistence-schema documents the most important AAD example: $\alpha_\Sigma = 1/(n+1)$ decays with experience, so strategic persistence requires experience discounting at rate $(1-\lambda) \gt \rho_\Sigma/R_\Sigma$ to recover constant-$\alpha$.
- *Heavy-tailed disturbances.* Neither (T3-D) nor (T3-S) covers disturbances with unbounded moments. Extreme tail events are better handled as triggers for structural adaptation than as disturbances the template can absorb.

## Discussion

**Why factor this out.** Every persistence-flavored result in AAD takes the form "correction rate exceeds effective disturbance rate (relative to reserve)" and is proved by the same Lyapunov function $V(\xi) = \tfrac{1}{2}\lVert\xi\rVert^2$. Stating the argument once, parameter-free, makes visible that the theory is *one result about bounded-correction dynamics applied to several state spaces*, not six separately-proved results that happen to look alike.

Each instantiation's distinctive content is now sharply visible: *what is the state variable, and what counts as its effective disturbance?* The Lyapunov machinery is shared; the characterization of $\rho_\xi$ is where the domain-specific insight lives. Adversarial destabilization's content is the coupling term $\gamma_A \mathcal T_A$; team persistence's content is the cooperative-minus-adversarial decomposition; composition closure's content is the closure-defect rate $\varepsilon^\ast \nu_c$. In each case, the template absorbs the Lyapunov boilerplate and lets the distinctive claim stand without it.

**What each instantiation must still verify.** Invoking the template is not trivial. Each instantiation must establish (T1)–(T3) for its specific $(\xi, F, \rho_\xi, R)$, and the non-trivial verifications differ substantively:

- *Strategic persistence* ( #strategy-persistence-schema): (T2) is verified for Beta-Bernoulli edge updates across five DAG topologies ( #strategic-dynamics-derivation Props B.1–B.6). But $\alpha_\Sigma = 1/(n+1)$ is time-varying: it decays monotonically with experience. Constant-$\alpha$ — and therefore the template's trajectory guarantee — requires experience discounting as a prerequisite, not a heuristic.
- *Composition closure* ( #composition-closure): (T2) as stated is insufficient. The bridge lemma requires the *incremental sector bound* (DA2'-inc) — strongly monotone $F$ across the whole state space, strictly stronger than the one-point sector bound (T2). Three agent tiers result: Tier 1 where contraction is proved for the full class (Bayesian on exponential families, gradient descent on strongly convex losses, linear correctors with positive-definite gain), Tier 2 where it holds locally, Tier 3 where it must be verified per-domain.
- *Team persistence* ( #team-persistence): (T3) is the decomposition $\rho_i^{\text{eff}} = \rho_{i,\text{env}} + \sum_j \gamma_{j\to i}^{\text{adv}}\mathcal T_j - \sum_j \gamma_{j\to i}^{\text{coop}}\mathcal T_j$. Cooperative coupling enters through a negative term, which can drive $\rho_i^{\text{eff}}$ below the single-agent $\rho$ — this is formally how teams persist where individuals cannot.

**Persistence and destabilization as one result.** Adversarial destabilization ( #adversarial-destabilization) is the template applied with coupling-amplified disturbance: $\rho_B = \rho_{B,\text{base}} + \gamma_A \mathcal T_A$. The "destabilization threshold" — the condition under which agent $A$ pushes agent $B$ past its stability boundary — is precisely the *negation* of the template's persistence condition for $B$'s instantiation. $B$ persists iff $\alpha_B R_B \gt \rho_B$; $B$ destabilizes iff $\rho_B \gt \alpha_B R_B$. These are the same inequality viewed in opposite directions, not independent results. The superlinear adversarial scaling ($b=2$ under Model D, $b=3/2$ under Model S) follows from the template's $1/\alpha$ vs $1/\sqrt{\alpha}$ scaling without further derivation.

**Signed-coupling pattern across instantiations.** The six instantiations above — plus #critical-mass-composition, which derives a closed-form composite (T2) for the matched-symmetric-Tier-1 dyad — share a signed-coupling structure: each effective $\rho_\xi$ is a sum of environmental disturbance plus a cross-agent contribution whose sign encodes cooperative vs adversarial coupling. Team persistence, composition closure (via bridge-lemma), tempo composition, adversarial destabilization, and composite critical-mass are instances of one inequality at different state-variable levels. The template is where this pattern lives at the meta level; the per-segment instantiations supply the domain-specific $(\xi, F, \rho_\xi, R)$ quadruples.

**Cost complement: the template's information-rate floor.** Alongside the threshold condition, each instantiation inherits an information-rate lower bound from #persistence-cost: under Model S with Gaussian-OU-shaped disturbance statistics on $\xi$, the sustained information rate required to maintain $\mathbb E[\lVert\xi\rVert^2]_{ss}$ at the ultimate bound satisfies $\dot R \geq n\alpha/2$ nats/time with the instantiation's own $(\alpha, n, \sigma_\xi^2)$. For the epistemic-mismatch instance, this translates to the channel-capacity floor $C \geq \mathcal T/2$ — a first-class persistence prerequisite that the threshold condition alone does not surface. Each instantiation can derive its own cost bound by direct substitution into the main theorem of #persistence-cost; the consolidation of this into a parametric template-cost subsection is flagged in that segment's Working Notes.

**The coordination overhead $C_{\text{coord}}$ is effective disturbance at the composite level.** The tempo-composition inequality $\mathcal T_c \leq \sum_i \mathcal T_i$ has a lower bound on the gap: $C_{\text{coord}} \geq \varepsilon^\ast \nu_c$ ( #derived-tempo-composition). This is the template's instantiation with $\xi = \delta_c$ and effective disturbance $\rho_{\text{ext}} + \varepsilon^\ast \nu_c$ — the composite's internal closure error acts as an additional disturbance at the macro level, absorbing correction capacity that would otherwise address the external environment. Brooks's Law follows as an instance: adding agents increases $\sum_i \mathcal T_i$ but may increase $\varepsilon^\ast \nu_c$ faster, pushing $\rho_c^{\text{eff}}$ above $\alpha_c R_c$.

**Relationship to #persistence-condition.** #persistence-condition is the canonical single-agent instantiation. It carries additional content beyond the template — *task adequacy*, a domain-specific constraint $R^\ast \lt \lVert\delta_{\text{critical}}\rVert$ that further restricts the usable region — and it instantiates the template in the linear special case where $F = \mathcal{T}\delta$, $\alpha = \mathcal{T}$, and (T2) holds globally. Task adequacy is not part of the template because it is not part of the Lyapunov argument; it is an application-level constraint the agent's domain imposes.

**Relationship to #postulate-composition-consistency.** The composition-consistency postulate requires that AAD's predictions be compatible across levels of description. The template is how this compatibility cashes out operationally: the same persistence argument applies at every level where a state variable with a sector-bounded correction function is present. Section III segments that invoke the template (team persistence, composition closure, tempo composition) are applying AAD's single persistence argument at the composite level, with effective disturbance decompositions that capture what is distinctive about the composite scope.

**Relationship to #contraction-template (metric-formulation generalization).** The Euclidean sector inequality (T2) is the $M = I$ specialization of a broader contraction-metric condition (CT2) under a Riemannian metric $M$ (Lohmiller & Slotine 1998). For several AAD-relevant agent classes, the natural Lyapunov lives in a non-Euclidean metric — Fisher for statistical-manifold learning (matrix Kalman in information metric; exponential family in natural parameters), Hessian-induced for ill-conditioned strongly-convex optimization, Lyapunov-equation-determined for asymmetric-stable linear systems, or Lyapunov-metric for PID-with-bounded-plant-nonlinearity. #contraction-template states the generalization once with (CT1)–(CT3) preconditions matching (T1)–(T3), adds compositional theorems (parallel / cascade / negative-feedback with small-gain) that extend `#critical-mass-composition` (CM2) to heterogeneous sub-agents via (CM2-M), and fills `#discussion-separability-pattern`'s seventh ladder (A2'-scope into metric-α₁ / metric-α₂ / metric-β). The Euclidean formulation stated in this segment remains the default for Euclidean-natural instances; #contraction-template is invoked when the natural coordinate is non-Euclidean. Structural consequence worth noting: the (CT2) condition at $M = I$ is equivalent to `#composition-closure`'s DA2'-inc (incremental sector bound), so AAD has been carrying the Jacobian-level Euclidean contraction condition at the composite level all along; #contraction-template makes this explicit at the single-agent level.

## Working Notes

- The template is type `result` because it states a result abstractly; the proof lives in #sector-condition-derivation (the canonical instance for $\delta$), and the transfer to other state variables is routine once (T1)–(T3) are verified. Treating it as a `formulation` would misrepresent its status — the Lyapunov argument does not leave room for alternative formulations within its stated scope.
- Candidate extensions that would strengthen the template: (i) time-varying $\alpha(t)$ with lower bound, for the strategic case; (ii) state-dependent noise intensity, for cases where the disturbance magnitude depends on the current mismatch; (iii) non-quadratic Lyapunov functions, for richer stability regions. Each is a real extension of Lyapunov theory, not specific to AAD.
- The template's role in #postulate-composition-consistency's "applies at every level" claim is now explicit: the claim holds at every level where (T1)–(T3) can be verified for the level's state variable. This sharpens the composition postulate from "applies at every level" to "applies at every level the template applies to," which is a testable condition rather than a universal assertion.
