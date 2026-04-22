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
| #tempo-composition | $\delta_c$ (composite mismatch) | $\rho_{\text{ext}} + \varepsilon^\ast \nu_c$ (external + internal) | $R_c$ | (T3) requires the bridge-lemma contraction; $C_{\text{coord}} \geq \varepsilon^\ast\nu_c$ is the tempo-equivalent of the internal disturbance |
| #adversarial-destabilization | $\delta_B$ (target-agent mismatch) | $\rho_{B,\text{base}} + \gamma_A \mathcal T_A$ (Model D) or $\sigma_{B,\text{base}} + \gamma_A \mathcal T_A$ (Model S) | $R_B$ | Destabilization is the negation of persistence: (T3)'s coupling-amplified disturbance violates $\alpha R \gt \rho_\xi$ |

The same Lyapunov argument applies in every row. What varies is how each instantiation defines its state variable, its correction function, and — most importantly — what counts as "effective disturbance" for its context (environmental noise, adversarial coupling, closure defect, or a decomposition of these).

### Comparison with the FEP-flow stability argument

Active inference's stability arguments come from the geometry of the variational free-energy landscape — agents are argued to flow toward the minimum of variational free energy on a non-equilibrium-steady-state (NESS) density (Friston 2019, "A free energy principle for a particular physics," arXiv:1906.10184; Friston, Da Costa, Sakthivadivel, Heins, Pavliotis, Ramstead & Parr 2023, "Path integrals, particular kinds, and strange things," *Phys. Life Rev.* 47). Aguilera, Millidge, Tschantz & Buckley (2022, "How particular is the physics of the free energy principle?", *Phys. Life Rev.* 40) showed that this argument's mathematical validity is narrow: the NESS-density framing for the FEP-flow holds only in a small parameter regime for non-equilibrium linear stochastic systems, and natural extensions (nonlinear, non-Gaussian, non-equilibrium) often fall outside the proven regime.

The AAD persistence template is structurally different: it is a Lyapunov-based argument requiring only (T1) zero-correction-at-zero-state, (T2) local sector condition (correction points inward), and (T3) bounded disturbance — all of which are checked locally for each instantiation ( #sector-condition-derivation Props A.1, A.1S, A.2). The template applies to bounded and to mean-square-stochastic disturbance, gives explicit ultimate-bound and adaptive-reserve formulas, and does not depend on NESS structure or on a free-energy gradient.

The breadth difference is not rhetorical: where the FEP-flow argument's parameter regime is debated in the AI literature itself, the sector-Lyapunov apparatus is the standard machinery of nonlinear control theory (Khalil 2002, *Nonlinear Systems*, 3rd ed., Prentice Hall, ch. 4) and applies wherever (T1)–(T3) hold. This is one of AAD's stronger structural positions and is worth making explicit when comparing AAD to active inference: AAD does the persistence work AI tries to do, with broader validity and explicit ultimate-bound formulas.

## Epistemic Status

*Exact.* The template is the abstract form of the Lyapunov result proved in #sector-condition-derivation (Props A.1, A.1S, A.2). The proofs transfer without modification whenever (T1)–(T3) hold; the template's contribution is the recognition that AAD's persistence-flavored results are instances of a single pattern and the enumeration of what each instantiation must verify.

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

**The coordination overhead $C_{\text{coord}}$ is effective disturbance at the composite level.** The tempo-composition inequality $\mathcal T_c \leq \sum_i \mathcal T_i$ has a lower bound on the gap: $C_{\text{coord}} \geq \varepsilon^\ast \nu_c$ ( #tempo-composition). This is the template's instantiation with $\xi = \delta_c$ and effective disturbance $\rho_{\text{ext}} + \varepsilon^\ast \nu_c$ — the composite's internal closure error acts as an additional disturbance at the macro level, absorbing correction capacity that would otherwise address the external environment. Brooks's Law follows as an instance: adding agents increases $\sum_i \mathcal T_i$ but may increase $\varepsilon^\ast \nu_c$ faster, pushing $\rho_c^{\text{eff}}$ above $\alpha_c R_c$.

**Relationship to #persistence-condition.** #persistence-condition is the canonical single-agent instantiation. It carries additional content beyond the template — *task adequacy*, a domain-specific constraint $R^\ast \lt \lVert\delta_{\text{critical}}\rVert$ that further restricts the usable region — and it instantiates the template in the linear special case where $F = \mathcal{T}\delta$, $\alpha = \mathcal{T}$, and (T2) holds globally. Task adequacy is not part of the template because it is not part of the Lyapunov argument; it is an application-level constraint the agent's domain imposes.

**Relationship to #composition-consistency.** The composition-consistency postulate requires that AAD's predictions be compatible across levels of description. The template is how this compatibility cashes out operationally: the same persistence argument applies at every level where a state variable with a sector-bounded correction function is present. Section III segments that invoke the template (team persistence, composition closure, tempo composition) are applying AAD's single persistence argument at the composite level, with effective disturbance decompositions that capture what is distinctive about the composite scope.

## Working Notes

- The template is type `result` because it states a result abstractly; the proof lives in #sector-condition-derivation (the canonical instance for $\delta$), and the transfer to other state variables is routine once (T1)–(T3) are verified. Treating it as a `formulation` would misrepresent its status — the Lyapunov argument does not leave room for alternative formulations within its stated scope.
- Candidate extensions that would strengthen the template: (i) time-varying $\alpha(t)$ with lower bound, for the strategic case; (ii) state-dependent noise intensity, for cases where the disturbance magnitude depends on the current mismatch; (iii) non-quadratic Lyapunov functions, for richer stability regions. Each is a real extension of Lyapunov theory, not specific to AAD.
- The template's role in #composition-consistency's "applies at every level" claim is now explicit: the claim holds at every level where (T1)–(T3) can be verified for the level's state variable. This sharpens the composition postulate from "applies at every level" to "applies at every level the template applies to," which is a testable condition rather than a universal assertion.
