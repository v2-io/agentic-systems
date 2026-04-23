---
slug: critical-mass-composition
type: derivation
status: conditional
depends:
  - composition-closure
  - scope-composite-agent
  - sector-persistence-template
  - sector-condition-derivation
  - team-persistence
  - adversarial-destabilization
  - symbiogenic-composition
  - unity-closure-mapping
stage: draft
---

# Derivation: Critical-Mass Composition

The composite sector constant $\alpha_c$ is derived — not merely bounded from below — for the symmetric-matched-Tier-1 two-agent case, yielding a closed-form critical-mass inequality in which the sign of the inter-agent coupling $\gamma$ and the teleological unity $U_O$ enter explicitly. The result subsumes the weakest-link bound, recovers #team-persistence (cooperative) and #adversarial-destabilization (adversarial) as signed special cases, formalizes #symbiogenic-composition's autonomy-reduction mechanism as an asymmetric Lyapunov-weight limit, and makes the scope-gate from #scope-composite-agent explicit as the second conjunct of composite persistence.

## Formal Expression

### Setup

Two sub-agents $A_1, A_2$, each a **Tier 1 agent** in the sense of #composition-closure's bridge-lemma taxonomy — mismatch-driven update, linear prediction, incremental sector-Lipschitz correction (Kalman, exponential-family Bayesian, gradient-on-strongly-convex, linear-with-PD-KH). **Matched architectures**: $f_1, f_2$ are structurally the same function, with $\alpha_1 = \alpha_2 = \alpha$, $R_1 = R_2 = R$. Disturbance statistics shared: each sees bounded $w_i(t)$ with $\lVert w_i\rVert \leq \rho$ (Model D, per #sector-persistence-template).

*[Formulation (coupling-model-C1, from #team-persistence + #adversarial-destabilization)]*

Inter-agent coupling enters additively to the disturbance at rate $\gamma \mathcal T_j$:

$$\rho_i^{\text{eff}} = \rho + \gamma \mathcal T_j \tag{C1}$$

with sign convention $\gamma \lt 0$ cooperative (ally's tempo-contribution reduces disturbance, recovering #team-persistence's $-\gamma^{\text{coop}}\mathcal T_j$ term), $\gamma \gt 0$ adversarial (ally's tempo-contribution amplifies disturbance, recovering #adversarial-destabilization's $+\gamma_A\mathcal T_A$ term). Symmetric case: $\gamma_{1 \to 2} = \gamma_{2 \to 1} = \gamma$.

*[Formulation (coordination-cost-C2)]*

Coordination overhead reduces each agent's effective correction rate symmetrically:

$$\alpha_i^{\text{eff}} = \alpha - C \tag{C2}$$

with $C \geq 0$ the $\Delta \mathcal T_i^{\text{cost}}$ from #team-persistence's coordination-overhead threshold.

### Critical-mass inequality (symmetric-matched-Tier-1 case)

*[Derived (critical-mass-symmetric, from #sector-persistence-template + C1 + C2)]*

Let $\xi = (\delta_1, \delta_2)^T$ and take the joint quadratic Lyapunov candidate $V(\xi) = \tfrac{1}{2}(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2)$. Under the block-diagonal correction structure with cross-coupling absorbed into $\rho_i^{\text{eff}}$ via (C1), and using $\lVert\delta_1\rVert + \lVert\delta_2\rVert \leq \sqrt{2(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2)}$ (Cauchy–Schwarz):

$$\dot V \leq -(\alpha - C)(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2) + (\rho + \gamma\mathcal T)\sqrt{2(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2)}.$$

Setting $\dot V = 0$ gives the ultimate bound on $\lVert\xi\rVert$ and, projecting to the macro-state $\delta_c = (\delta_1 + \delta_2)/\sqrt{2}$, the ultimate composite mismatch

$$R_c^\ast \leq \frac{\rho + \gamma\mathcal T}{\alpha - C}. \tag{L4}$$

The composite persists iff $R_c^\ast \lt R_c$. Inheriting $R_c = R$ from the symmetric-matched averaging projection:

$$\boxed{\;(\alpha - C)\,R \;\gt\; \rho + \gamma\mathcal T\;} \tag{CM2}$$

Rearranging into the composite contraction-rate form:

$$\kappa_c \;:=\; (\alpha - C) \;-\; \frac{\rho + \gamma\mathcal T}{R}, \qquad \text{composite persists iff } \kappa_c \gt 0. \tag{KC}$$

### Specialization checks

Under matched symmetry, (CM2) reduces correctly in four limits:

| Limit | Setting | (CM2) reduces to | Recovers |
|---|---|---|---|
| No coupling | $\gamma = 0$, $C = 0$ | $\alpha R \gt \rho$ | Single-agent #persistence-condition |
| Cooperative-symmetric | $\gamma \lt 0$, $C = 0$ | $\alpha R \gt \rho + \gamma\mathcal T$ (easier than individual) | #team-persistence's "teams persist where individuals can't" |
| Adversarial-symmetric | $\gamma \gt 0$, $C = 0$ | Fails when $\gamma\mathcal T \gt \alpha R - \rho$ | #adversarial-destabilization threshold (symmetric) |
| Coordination-dominated | $C \gt \alpha$, $\gamma = 0$ | LHS $\lt 0$; composite fails | Brooks's Law |

### Subsumption of the weakest-link bound

*[Derived (weakest-link-subsumption)]*

The weakest-link bound $\alpha_c \geq \min_i(\alpha_i - \Delta\mathcal T_i^{\text{cost}})$ from #composition-closure's derivation table specializes under matched symmetry to $\alpha_c \geq \alpha - C$. (KC) refines this by making the composite's effective disturbance explicit as $\rho + \gamma\mathcal T$, turning a correction-rate bound into a full persistence inequality. Critically, (KC) can yield $\kappa_c \gt 0$ even when the weakest-link bound alone fails — when cooperative coupling ($\gamma\mathcal T \lt 0$) reduces the effective disturbance below what the raw $\alpha - C$ margin would permit. The weakest-link bound cannot see this because it does not account for $\gamma$'s sign.

### $U_O$ entry: multiplicative-on-$\gamma$ plus scope-gate

*[Derived (unity-multiplicative-modulator, conditional on LQR-compatible action structure)]*

In a purposeful-agent setting where each sub-agent optimizes a quadratic objective $L_i(\omega) = \tfrac{1}{2}(\omega - r_i)^T Q(\omega - r_i)$ with target $r_i$, and $U_O := \operatorname{corr}(r_1, r_2)$ is the target correlation per #unity-dimensions' $U_O$, the cross-coupling in the joint dynamics has sign and magnitude controlled by $U_O$:

$$\gamma(U_O) \;=\; -\,\gamma_{\max}\, U_O, \qquad \gamma_{\max} \gt 0, \tag{UO-mult}$$

via aligned targets → aligned action directions in the shared environment → constructive (cooperative) cross-contribution in the symmetric eigendirection. Substituting into (KC):

$$\kappa_c(U_O) \;=\; (\alpha - C)R \;-\; \rho \;+\; \gamma_{\max}\,U_O\,\mathcal T. \tag{CM3}$$

*[Scope (scope-gate-from-composition-scope-condition)]*

(CM3) is necessary but not sufficient for composite existence. Under #scope-composite-agent, a composite exists as an AAD agent only when one of the three disjunctive alignment routes (shared objective, hierarchical derivation, mutual benefit) is satisfied. Below this threshold, no coherent $O_c$ is definable and composite-level quantities — including $R_c$ on the right of (CM2) — are ill-typed. The honest statement of composite persistence is therefore the conjunction:

$$\boxed{\;\kappa_c(U_O) \gt 0 \;\wedge\; \text{#scope-composite-agent satisfied} \;\Leftrightarrow\; \text{composite persists as AAD agent}\;} \tag{CM4}$$

$U_O$ enters (CM4) in two independent ways: multiplicatively within (CM3), and as scope-gate via #scope-composite-agent. It does **not** enter purely additively as a separate reserve term — there is no free-floating "$U_O$ contribution" detached from the coupling it modulates.

### Asymmetric limit and symbiogenic composition

*[Sketch (asymmetric-limit-symbiogenesis, from weighted Lyapunov)]*

Drop the matched-symmetric assumption. Let $\alpha_1 \gg \alpha_2$ with $\alpha_2 \to 0$. The unweighted joint Lyapunov $V = \tfrac{1}{2}(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2)$ fails (the weakest-link ultimate bound diverges as $\alpha_2 \to 0$). A **weighted** Lyapunov $V_\mu(\xi) = \tfrac{1}{2}(\lVert\delta_1\rVert^2 + \mu\lVert\delta_2\rVert^2)$ with $\mu \to 0$ yields

$$\dot V_\mu \leq -\alpha_1\lVert\delta_1\rVert^2 + \rho_1\lVert\delta_1\rVert \;+\; O(\mu),$$

so in the limit the composite's stability is controlled **entirely by agent 1**; agent 2's autonomous correction dynamics are weighted out of the stability accounting.

This provides a Lyapunov-weighted formalization of #symbiogenic-composition's **(S-3) autonomy reduction**: the endosymbiont's effective action space contracts ($\mathcal A_e^{\text{effective}} \to \mathcal A_e^{\text{restricted}}$) and its autonomous dynamics fall out of the joint Lyapunov argument. The asymmetric limit is a smooth deformation of (CM4), not a discontinuous regime change — symbiogenesis and peer coupling are parameter-limits of the same weighted-Lyapunov analysis. The result does **not** close #symbiogenic-composition's (S-1) objective absorption or (S-2) function transfer: what happens to agent 1's state space when it inherits structure from agent 2 is a separate question the weighting argument does not address.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Coupling model (C1): $\rho_i^{\text{eff}} = \rho + \gamma\mathcal T_j$ | Import from #team-persistence and #adversarial-destabilization | Formulation choice (requirement for the derivation) |
| Coordination-cost model (C2): $\alpha_i^{\text{eff}} = \alpha - C$ | Import from #team-persistence's coordination-overhead threshold | Formulation choice |
| Joint quadratic Lyapunov $V = \tfrac{1}{2}(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2)$ | Standard vector-Lyapunov construction (Matrosov 1962; Bellman 1962) | Formulation choice (canonical for matched-symmetric dyads) |
| Ultimate bound $R_c^\ast \leq (\rho + \gamma\mathcal T)/(\alpha - C)$ | Lyapunov dissipation + Cauchy–Schwarz | Derived |
| Critical-mass inequality (CM2): $(\alpha - C)R \gt \rho + \gamma\mathcal T$ | (L4) + sector-region fit $R_c^\ast \lt R_c = R$ | Derived (conditional on Tier 1 + matched-symmetric + Model D) |
| Four specialization checks (no-coupling / cooperative / adversarial / coordination-dominated) | Direct substitution into (CM2) | Proved (within stated scope) |
| Subsumption of weakest-link bound | (CM2) sign-sensitive; weakest-link is sign-blind | Proved |
| (UO-mult): $\gamma(U_O) = -\gamma_{\max}U_O$ | LQR-compatibility sketch; aligned targets → aligned actions → constructive cross-contribution | Discussion-grade |
| Composite persistence as (CM3) ∧ scope-satisfaction: (CM4) | (KC) with (UO-mult) + #scope-composite-agent | Derived (conditional) |
| Asymmetric limit → #symbiogenic-composition (S-3) via weighted Lyapunov | Matrosov-style weighting; $\mu \to 0$ limit | Sketch (the weighting is standard; the identification with (S-3) is structurally motivated but not a theorem) |
| (S-1) objective absorption and (S-2) function transfer formalizations | Not addressed by this derivation | Open (in #symbiogenic-composition Working Notes) |
| Heterogeneous-architecture case ($A_1$ Tier 1, $A_2$ Tier 2/3) | Requires per-sub-agent tiering per #composition-closure | Open |
| Heterogeneous-metric Tier-1M dyad ($\lambda_1 \neq \lambda_2$, $C_1 \neq C_2$, $k_{12} \neq k_{21}$) | #contraction-template (CM2-M) via Slotine 2003 negative-feedback small-gain: $(\lambda_1 - C_1)(\lambda_2 - C_2) \gt k_{12} k_{21}/4$ | Derived (conditional on #contraction-template (CT2) preconditions + Slotine 2003) |
| Nonlinear coupling $\gamma = \gamma(\delta_j)$ | Requires full joint-Lyapunov machinery from #adversarial-destabilization (effects-spiral corollary) | Open |
| Dynamic coordination cost $C = C_0 + C_1\lVert\delta_j\rVert$ | Quadratic inequality; admits closed form, loses interpretive cleanliness | Open |
| Fully-coupled tempo dynamics ($\mathcal T_i$ responsive to $\delta_j$) | Requires joint tempo analysis from #adversarial-destabilization Working Notes | Open |
| $N \gt 2$ scaling of (CM4) | Conjunction over pairwise terms generalizes but loses closed form; see `msc/spike-composition-scaling-N.md` | Open |

The dividing line: (C1), (C2), and the quadratic Lyapunov candidate are **formulation choices** imported from adjacent segments or from standard Lyapunov practice. The *consequences* under these choices — (L4), (CM2), (KC), the specialization checks, the weakest-link subsumption, and (CM4) with its scope-gate conjunct — are **derived**. The $U_O$-multiplicative modulator (UO-mult) is discussion-grade: it uses an LQR-compatibility argument whose rigor depends on an action-space inner-product analysis deferred to #unity-closure-mapping. The asymmetric-limit identification with #symbiogenic-composition (S-3) is sketch-level — the weighted-Lyapunov argument is standard but the semantic identification with autonomy reduction is structural, not proved.

## Epistemic Status

*Conditional.* Max attainable: *exact* (within the matched-symmetric-Tier-1 scope); *conditional* beyond.

(CM2) and (KC) are **proved** under Tier 1 architecture + matched-symmetric parameters + Model D disturbance + the (C1) disturbance-coupling model + the (C2) coordination-cost model. These conditions cover Kalman filters, exponential-family Bayesian updaters, gradient-on-strongly-convex agents, and linear-PD correctors — the same architecture class for which #composition-closure's bridge lemma is promoted from "conditional" to "derived." Within this scope the result is as strong as the standard Lyapunov argument allows.

(CM3) inherits the conditional status of (UO-mult), which is **discussion-grade**: the LQR-compatibility sketch is qualitatively clear, but a rigorous action-space inner-product derivation that pins down $\gamma_{\max}$ has not been produced. (CM4) is therefore conditional on both (UO-mult)'s rigor and on #scope-composite-agent's scope-gate being independently verified for the given composite candidate.

The asymmetric limit (§asymmetric-limit) is **sketch-level**. The weighted-Lyapunov argument is textbook (Matrosov 1962); the identification of the $\mu \to 0$ limit with #symbiogenic-composition's (S-3) autonomy-reduction mechanism is structurally motivated but not a theorem, because (S-2) function transfer is not formalized in #symbiogenic-composition. When (S-2) lands, the symbiogenic-limit result can be promoted to derived.

What this segment does **not** establish:

- Composite **incremental** sector bound (DA2'-inc) — still the domain of #composition-closure's bridge lemma and `msc/spike-bridge-lemma-contraction.md`. (CM4) gives composite (T2) at the macro level; the bridge lemma's contraction is a separate, stronger condition.
- Heterogeneous-architecture composites (Kalman + PID, Tier 1 + Tier 3): the joint Lyapunov construction requires agent-by-agent tiering; closed form is not available.
- Nonlinear or state-dependent coupling: (C1) assumes $\gamma$ independent of $\delta$. State-dependent $\gamma$ produces a nonlinear inequality in $\delta$; this is the effects-spiral corollary territory of #adversarial-destabilization, still open.
- $N \gt 2$ scaling: the matched-symmetric pairwise result generalizes by conjunction, but the Cauchy–Schwarz step degrades with team size; the closed form does not survive cleanly. See `msc/spike-composition-scaling-N.md`.

**On (T2) and sub-scoping.** The joint quadratic Lyapunov candidate presumes each sub-agent's correction is in sub-scope $\alpha$ of #sector-condition-derivation (Bayesian / exponential-family / strongly-convex-gradient / linear-PD) under directional fidelity per #gain-sector-bridge. Composites with sub-scope $\beta$ sub-agents (PID, rule-based, human-judgment) require (T2) verification per sub-agent at the composite level — the template's A2'-sub-scope label is inherited pairwise.

## Discussion

**Relationship to the bridge lemma.** #composition-closure's bridge lemma establishes when the macro-update map $f_c$ is **incrementally** contracting, at the trajectory-error level — a condition strictly stronger than the one-point sector bound. This segment is the complement at the macro-state level: given the bridge lemma's admissibility, (CM4) derives composite (T2), the one-point sector bound that #sector-persistence-template's instantiation for the composite requires. Both are necessary for the composite to be a stable macro-agent with bounded mismatch: bridge lemma says the macro-description tracks micro-reality (trajectory error stays bounded); (CM4) says the composite's own corrections drive composite mismatch back inside the sector region. Together they close the composite-persistence argument at both layers.

**Pattern across the signed-coupling instances.** (CM4) has the same shape as several persistence-flavored results already in AAD:

- #team-persistence: per-sub-agent inequality $\alpha_i R_i \gt \rho_{i,\text{env}} + \sum_j\gamma_{j \to i}^{\text{adv}}\mathcal T_j - \sum_j\gamma_{j \to i}^{\text{coop}}\mathcal T_j$
- #tempo-composition: composite inequality with effective disturbance $\rho_{\text{ext}} + \varepsilon^\ast\nu_c$
- #adversarial-destabilization: failure condition $\gamma_A\mathcal T_A \gt \alpha_B R_B - \rho_B$ (negation of persistence)
- this segment: matched-symmetric dyad with signed $\gamma$ and scope-gate

All four are instances of #sector-persistence-template's pattern with signed coupling controlling the sign of the cross-agent contribution to $\rho_\xi$. The template already names this pattern at the meta level; the present segment is the dyadic closed-form instance that the other three segments reference pairwise. A dedicated meta-segment for "signed-coupling critical-mass" was considered during spike work and judged redundant with #sector-persistence-template — the cross-instance structure is already visible in that segment's instantiation table.

**Potential-game generalization (via #strategic-composition).** (CM4) applies to composites with shared target (scope routes C-i / C-ii / C-iii from `#scope-composite-agent`) where contraction-to-shared-truth is the correct primitive. `#strategic-composition` carries the sibling result for composites with partially-opposing objectives (scope route C-iv — strategic composites): under the potential-game condition (Monderer-Shapley 1996), the sector-persistence template transfers to the gradient of the joint potential $\Phi$, with $\alpha_{\text{joint}}$ playing the role of the composite sector constant and $\xi = \pi - \pi^\ast$ (deviation from Nash) playing the role of the composite state. For matched-symmetric potential games, the structural form of (CM2) survives with $(\alpha, R, \rho, \gamma, C)$ replaced by $(\alpha_{\text{joint}}, R_{\text{Nash-basin}}, \rho_\xi, \gamma_{\text{strategic}}, C_{\text{strategic}})$; the specific mapping is instance-dependent and typically not closed-form for non-zero-sum games. The joint-quadratic-Lyapunov machinery of this segment and the potential-function-Lyapunov machinery of `#strategic-composition` are both instances of `#sector-persistence-template` at the composite-state-variable level; what varies is whether the composite state is *mismatch-to-shared-target* (this segment) or *deviation-from-Nash* (`#strategic-composition`).

**What (CM4) contributes beyond existing segments.**

1. **Derivation, not assumption.** The composite sector constant appearing in #composition-closure's (A4) was previously bounded by the weakest-link formula (a derived lower bound) but treated as an assumption for the bridge lemma. (CM4) *derives* $\alpha_c$ as a closed-form function of sub-agent parameters + coupling + unity + coordination overhead, in the matched-symmetric-Tier-1 case.
2. **Sign-sensitive.** The weakest-link bound is sign-blind — it gives the same $\alpha_c \geq \alpha - C$ regardless of whether the coupling is cooperative or adversarial. (CM4) makes the sign explicit through the $\rho + \gamma\mathcal T$ right-hand side and turns a correction-rate bound into a full persistence inequality.
3. **Unifies cooperative and adversarial regimes.** Teams persisting where individuals can't and adversarial destabilization are the same inequality viewed from opposite signs of $\gamma$, not independent results.
4. **Scope-gate made explicit.** Composite persistence requires both contraction (CM3) **and** scope-satisfaction ( #scope-composite-agent). (CM4) states this conjunction honestly; the absence of one or the other is a different failure mode (composite fails to contract vs. composite was never a composite).
5. **Symbiogenic and peer regimes connected.** The asymmetric limit shows symbiogenesis is a parameter-limit of peer coupling under a Lyapunov-weight deformation, not a discontinuous regime change requiring separate machinery.

**Why the matched-symmetric restriction is load-bearing.** Relaxing matched architectures requires per-sub-agent tiering in the sense of #composition-closure (Tier 1 / 2 / 3). Heterogeneous composites can still satisfy (T2) at the composite level, but the joint Lyapunov construction must be weighted per sub-agent's contraction capacity — and the weighted form loses the clean closed-form (CM2). Relaxing symmetric coupling ($\gamma_{1 \to 2} \neq \gamma_{2 \to 1}$) produces a non-symmetric matrix whose smallest eigenvalue must be computed explicitly per instance. The matched-symmetric case is the one where both sub-agent tiering and coupling symmetry collapse the Lyapunov construction to a scalar inequality — which is why closed form is available there and not elsewhere.

**Load-bearing role under `#discussion-identifiability-floor` Instance 3.** The composition-layer identifiability floor (Instance 3 of `#discussion-identifiability-floor`) establishes a no-go theorem: there exist pairs of coupled systems with identical marginal component-level observation distributions but opposite composite-contraction signs, so composite contraction is not in general identifiable from component data alone. Four structural escapes are named there; escape (b) — matched Tier at the composite level — is operationalized by the closed-form (CM2) in this segment. Under the floor, (CM2) is not just "a closed-form result in a special case" but **the unique broadly-available composition-contraction certificate** among the four escape routes listed. Without (CM2) or its metric-formulation generalization (CM2-M) via `#contraction-template`, the weakest-link bound (WL) is sign-blind and cannot distinguish the cooperative-contracting from the adversarial-destabilizing composite. This load-bearing status positions this segment as "the machinery that escapes the composition-layer floor" rather than as a closed-form curiosity in the matched-symmetric special case.

**Adjacent literature.** The joint Lyapunov construction is an instance of the classical **vector Lyapunov function** method (Matrosov 1962; Bellman 1962). The critical-mass inequality is the AAD sector-bounded analog of the **small-gain theorem for ISS systems** (Jiang–Teel–Praly 1994; Sontag 1989): in the small-gain framework, composition of two ISS systems is ISS iff the product of their gains is less than one; in AAD's sector-bounded framework, the composite persists iff the *sum* of parent reserve-rates exceeds the coupling-amplified disturbance (additive rather than multiplicative because the averaging projection averages rather than multiplies gains). In the linear-diagonal-coupling case, the matrix $A = \alpha I - \beta(I - J)$ where $J$ is the averaging operator is the graph-Laplacian-shifted form governing consensus convergence (Olfati-Saber & Murray 2004); (CM2) is consensus convergence rewritten as a persistence inequality. Relative to active inference's FEP-flow stability arguments (Friston 2019; narrowed by Aguilera et al. 2022 to small parameter regimes in NESS-density models), the present result inherits #sector-persistence-template's broader validity: it applies wherever (T1)–(T3) hold pairwise + (C1)/(C2) + matched symmetry, without requiring free-energy landscapes or NESS structure.

## Working Notes

- **Partial-derivation: heterogeneous-architecture dyad.** The clean closed form (CM2) relies on matched sub-agent architectures collapsing the joint Lyapunov candidate to a scalar inequality. A natural next move is the $(A_1, A_2)$ = (Tier 1, Tier 2) case: weighted Lyapunov $V_\mu = \tfrac12(\lVert\delta_1\rVert^2 + \mu(\delta_2)\lVert\delta_2\rVert^2)$ with the weight a function of agent 2's local contraction modulus. Likely produces a range-valued (not closed-form) critical-mass inequality. Defer until a specific Tier-mismatch composite motivates it.
- **Sharpen (UO-mult).** Upgrading $\gamma(U_O) = -\gamma_{\max}U_O$ from discussion-grade to derived requires an action-space inner-product analysis: define the environment's action-coupling operator, show that LQR-linear policies produce cross-actions with inner product proportional to target correlation, and pin down $\gamma_{\max}$ in terms of the quadratic objective's Hessian and the environment's coupling gain. This is mechanical but non-trivial; natural home is an extension to #unity-closure-mapping's linear-Gaussian closed-form section.
- **Close (S-2) function transfer in #symbiogenic-composition.** The asymmetric-limit result here identifies the Lyapunov-weight limit as (S-3) autonomy reduction but leaves (S-2) function transfer unformalized. A complete symbiogenic-limit theorem requires specifying what happens to agent 1's state space when it inherits structure from agent 2 — how $\mathcal F(M_e, \Sigma_e)$ lands in $M_h$. This is flagged in #symbiogenic-composition's Working Notes and is a prerequisite for promoting the limit result to derived.
- **Connection to Miller-2022 extreme-transition motif.** The asymmetric-limit smooth-deformation result contrasts with extreme-transition dynamics (pending dedicated Section III segments) where population-level niche-replacement proceeds discontinuously. The two mechanisms co-exist and are not reducible to one another; the weighted-Lyapunov analysis is specific to bilateral asymmetric integration.
- **$N$-agent scaling.** The conjunction generalization "composite persists iff (CM4) holds pairwise for all $i, j$" is probably too strong — pairwise cooperative effects can compose super-additively in particular topologies (ensemble filters, committee agents). A sharper $N$-agent theorem requires a graph-structured Lyapunov construction. See `msc/spike-composition-scaling-N.md` for a framing of the question.
