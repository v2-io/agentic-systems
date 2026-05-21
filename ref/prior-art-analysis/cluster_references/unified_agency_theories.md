# Cluster Reference: Unified Agency Theories

**Overview:** The overarching synthesis bridging adaptive cybernetics, control theory, and information geometry into a single, cohesive framework of agency from thermostats to AGI.

---

## Canonical Source Segments

### Source: `scope-adaptive-system.md`

```yaml
---
slug: scope-adaptive-system
type: scope
status: axiomatic
depends:
  - def-agent-environment
  - def-observation-function
  - def-chronica
stage: claims-verified
---
```


# Scope: Adaptive System

AAT's broadest scope: any system that observes an uncertain environment supports Section I's adaptive machinery. Adding causal action narrows to the agency scope ( #scope-agency); this segment names the outer scope from which agency is a restriction.

## Formal Expression

*[Scope (scope-adaptive-system)]*

$$\mathcal S_\text{adaptive} = \left\{(\text{Agent}, \Omega) \;:\; \mathcal O \neq \emptyset, \;\; H(\Omega_t \mid \mathcal C_t) \gt 0 \right\}$$

Two conditions:

1. **Observations exist**: $\mathcal O \neq \emptyset$ — the system has some perceptual channel to the environment ( #def-observation-function)
2. **Residual uncertainty persists**: $H(\Omega_t \mid \mathcal C_t) \gt 0$ — the environment is not fully determined by the interaction history

This is sufficient for the mismatch signal ( #def-mismatch-signal), update gain ( #emp-update-gain), adaptive tempo ( #def-adaptive-tempo), the persistence condition ( #result-persistence-condition), and all of Section I's adaptive dynamics. A Kalman filter estimating a passive signal, a passive Bayesian learner, and any system that observes and updates a model under uncertainty are within this scope.

## Epistemic Status

*Axiomatic.* This is a scope definition — it draws the boundary around the systems Section I addresses. The two conditions are not derived; they are the minimal requirements for the adaptive machinery to be non-vacuous.

## Discussion

**What is included.** Any system that observes under uncertainty. Passive Bayesian learners, Kalman filters (with or without control inputs), biological sensory systems. These are Section I's subjects — instances that build $M_t$ through mismatch-driven updates without necessarily acting to influence their environment.

**What is excluded.**

- **Closed-form systems** ($H(\Omega_t \mid \mathcal C_t) = 0$): When the agent has complete knowledge of the environment, there is no uncertainty to adapt to. Optimal control over known dynamics is a solved problem outside AAT's concerns.
- **Pure computation** ($\mathcal O = \emptyset$): A system with no observation channel — e.g., a mathematical proof engine operating on axioms alone — has no agent-environment boundary in AAT's sense.

**Narrowing to agency.** Adding causal action unlocks the interventional and purposeful results of Sections II and III. The agency scope ( #scope-agency) is the intersection of $\mathcal S_\text{adaptive}$ with the condition that actions carry Pearl-level-2 contrast: distinct actions produce distinct interventional outcome distributions. Adaptive-scope systems that remain outside agency are *passive observers* (no choice) or *nominal agents* (choices with no causal effect); for both, Section I's machinery applies but the causal-information and purposeful-agent results do not.


---

### Source: `scope-agency.md`

```yaml
---
slug: scope-agency
type: scope
status: axiomatic
depends:
  - scope-adaptive-system
  - def-action-transition
stage: claims-verified
---
```


# Scope: Agency

The agency scope narrows AAT's adaptive scope ( #scope-adaptive-system) to systems whose actions carry Pearl-level-2 causal contrast — distinct actions produce distinct interventional outcome distributions. This is the scope required for Sections II (purposeful agents) and III (composition); every segment that relies on the agent acting-with-effect depends on it.

## Formal Expression

*[Scope (scope-agency)]*

$$\mathcal S_\text{agency} = \mathcal S_\text{adaptive} \;\cap\; \left\{(\text{Agent}, \Omega) \;:\; \lvert\mathcal A\rvert \geq 2, \;\; \exists\, a \neq a' \text{ s.t. } P(o \mid do(a)) \neq P(o \mid do(a')) \right\}$$

Two conditions added to those of #scope-adaptive-system:

3. **At least binary choice**: $\lvert\mathcal A\rvert \geq 2$ — the agent can choose between at least two actions ( #def-action-transition)
4. **At least one action has causal effect**: there exist distinct actions $a, a'$ whose interventional outcome distributions differ (where $do(\cdot)$ is Pearl's intervention operator; see #def-pearl-causal-hierarchy) — the agent's choices make a difference to what it can observe

These are required for the adaptive loop to generate interventional data ( #der-loop-interventional-access), for the causal hierarchy requirement ( #der-causal-hierarchy-requirement) to be well-posed, and for the purposeful-agent machinery of Section II ($O_t$, $\Sigma_t$, the orient cascade) to be non-vacuous. Section III's composition theory inherits this requirement.

## Epistemic Status

*Axiomatic.* This is a scope definition — it names the boundary around systems whose behavior can be analyzed with Section II/III machinery. The conditions are not derived; they are the minimal additions to $\mathcal S_\text{adaptive}$ under which interventional data exist at all.

## Discussion

**What is included.** Systems whose actions make a causal difference: thermostats, Kalman filters with control inputs, RL agents, military commanders, software developers, AI agents with tool use. These are instances of the same formal framework at different points in the agent spectrum ( #def-agent-spectrum).

**What is in adaptive scope but excluded from agency.**

- **Passive observers** ($\lvert\mathcal A\rvert \lt 2$): Can observe and model, but cannot intervene. #scope-adaptive-system applies; the causal-information and purposeful-agent results do not.
- **Nominal agents** ($P(o \mid do(a)) = P(o \mid do(a'))$ for all $a, a'$): Have choices that make no difference. Can estimate but cannot learn causal structure. Same as passive observers for AAT's purposes: adaptive only.

**Why causal effect matters.** Binary choice ($\lvert\mathcal A\rvert \geq 2$) is necessary but not sufficient. Two actions that produce identical outcome distributions provide no interventional contrast — the agent cannot learn which action produces which effect because the effects are the same. The causal-effect condition ensures at least one meaningful contrast exists, which is what #der-loop-interventional-access needs to generate Level 2 data.

**Relationship to downstream segments.** Every segment that relies on the agent acting-with-effect depends on this scope: purposeful-agent machinery ($O_t$, $\Sigma_t$, orient cascade) in Section II; composition machinery (sub-agents acting jointly) in Section III. Downstream segments reference `#scope-agency` when they assert "the agent can act" as a prerequisite.


---

### Source: `post-composition-consistency.md`

```yaml
---
slug: post-composition-consistency
type: postulate
status: axiomatic
depends:
  - scope-agency
stage: deps-verified
---
```


# Postulate: Composition Consistency

AAT's predictions must be compatible across levels of description. If a system $S$ and its decomposition $\{S_1, \ldots, S_n\}$ both satisfy the scope condition, the theory's claims at the $S$-level and at the $\{S_i\}$-level cannot contradict each other. This cross-level compatibility is a structural requirement for AAT's internal coherence — the scope condition does not restrict which level the theory applies to, so the theory must be level-invariant in its predictions.

The operational consequences — when a decomposed system actually behaves as a single composite agent, and which Section I/II results carry across decompositions — are *derived* from this postulate under specific conditions: the composition scope condition ( #scope-composite-agent, teleological alignment threshold) determines *which* groups are composites; the composition closure criterion ( #form-composition-closure, admissibility conditions (A1)-(A4) and bridge lemma) determines *how faithfully* macro-dynamics track micro-dynamics for those groups; and the tier-specific contraction assumption in the bridge lemma ( #form-composition-closure Epistemic Status) determines *which* composites admit the cleanest cross-level transfer of results.

## Formal Expression

*[Postulate (postulate-composition-consistency)]*

For any system $S$ satisfying the scope condition ( #scope-agency), and any decomposition of $S$ into subsystems $\{S_1, \ldots, S_n\}$ where each $S_i$ also satisfies the scope condition, AAT's predictions at the system level must be compatible with its predictions at the subsystem level. Specifically, composition laws must exist such that:

1. **Tempo composition**: $\mathcal T_S$ is expressible as a function of $\{\mathcal T_{S_i}\}$ and the coordination structure among them
2. **Persistence compatibility**: the system's persistence is derivable from the sub-agents' individual persistence conditions plus coordination structure
3. **Mismatch consistency**: $\delta_S$ is derivable from $\{\delta_{S_i}\}$ and their interaction structure

*[Structural consequence (derivation hierarchy)]*

Cross-level compatibility requires three successively more specific conditions, each with its own segment in Section III:

1. **Scope**: The decomposition is a *composite* (not merely a multi-agent system) when #scope-composite-agent is satisfied — teleological alignment via at least one of three disjunctive routes (shared objective, hierarchical derivation, or mutual benefit). Without scope-satisfaction via any route, level-compatibility is vacuous (composition quantities are not well-defined, so there is nothing to be consistent about).

2. **Admissibility**: Given a composite, its macro-dynamics are well-posed when the closure admissibility conditions (A1)-(A4) hold ( #form-composition-closure). These require AAT-shaped macro-state, macro-mismatch, macro-tempo, and sector-bounded correction at the composite level.

3. **Transfer of results**: Individual Section I/II results lift to the composite level through the bridge lemma in #form-composition-closure, which requires a *tier-specific contraction assumption* beyond (A4). For **Tier 1** agents (all Bayesian updaters on exponential families, linear correctors with positive-definite gain, gradient descent on strongly convex losses), the contraction holds and Section I results transfer exactly. For **Tier 2** agents (locally convex, nonlinear prediction models), transfer holds locally with factor degradation. For **Tier 3** agents (non-convex optimization, discontinuous corrections, non-mismatch-driven state), contraction must be verified per-domain and Section I results do not automatically lift.

*[Derived (Conditional on Tier 1M + admissible composition topology, from #result-contraction-template (CC-parallel) / (CC-cascade) / (CC-feedback))]*

**Composite contraction rate — closed form under Tier 1M.** When sub-agents satisfy the contraction-template preconditions (CT1)–(CT3) of #result-contraction-template (Tier 1M, equivalently Tier 1 of #form-composition-closure's bridge lemma under the DA2'-inc ≡ (CT2)-at-$M=I$ equivalence) and the composition topology falls under one of the closure cases of #result-contraction-template, the composite contraction rate $\lambda_c$ admits a closed-form lower bound:

- **Parallel composition** (CC-parallel): $\lambda_c = \min_i \lambda_i$ — the composite contraction rate equals the slowest sub-agent's, with composite metric $M_c = \mathrm{blockdiag}(M_1, M_2)$. Equivalently in timescale form, the composite relaxation time $\tau_c = 1/\lambda_c = \max_i \tau_i$ is bounded *below* by the slowest sub-agent's timescale.
- **Hierarchical / cascade** (CC-cascade): same bound, up to coupling-gain adjustment.
- **Negative-feedback heterogeneous** (CC-feedback) / (CM2-M): $(\lambda_1 - C_1)(\lambda_2 - C_2) \gt k_{12} k_{21}/4$ with feedback-loop gains $k_{ij}$ and coordination costs $C_i$ from #der-team-persistence.

Macro-level persistence then reduces to the standard persistence condition ( #result-persistence-condition) applied to the composite: $\alpha_c \gt \rho_{\text{eff}}/R_c$, with $\alpha_c$ bounded by the topology-specific result above and effective disturbance $\rho_{\text{eff}} = \rho_{\text{ext}} + \varepsilon^\ast \nu_c$ from #der-tempo-composition's bridge-lemma instantiation. Both Section I results (single-agent persistence) and the bridge-lemma's macro-tracking faithfulness flow from this single inequality. This is the formal counterpart to the screening test below: under Tier 1M the screening test is *derived*, not heuristic.

*[Heuristic (timescale separation — residual scope: Tier 2 / Tier 3)]*

**Practical screening test for composites outside Tier 1M.** Tier 2 sub-agents (extended-Kalman, locally-convex gradients, nonlinear prediction models) and Tier 3 sub-agents (non-convex optimization, discontinuous corrections, non-mismatch-driven state) do not in general carry the closed-form composite-rate bound above — the bridge-lemma contraction holds only locally with $\kappa(D\hat o)^2$ degradation (Tier 2) or must be verified per-domain (Tier 3). For these composites, the qualitative condition

$$\tau_{\text{eq}} \ll \tau_{\text{ext}}$$

— internal equilibration timescale (the time for sub-agents to approximately synchronize models and coordinate actions) short relative to external-dynamics timescale — remains a useful *discussion-grade screening test*. When it holds, composite description is plausibly well-posed; when it fails, composite description is plausibly broken. The screening test is the operational analog of the persistence condition ( #result-persistence-condition), but for Tier 2 / Tier 3 it does not entail the formal persistence condition without local-region or per-domain verification. Whether common organizational settings (software teams, military units) genuinely sit in Tier 1M or merely satisfy the heuristic without satisfying Tier 1M conditions is an empirical question, not a derived fact.

## Epistemic Status

*Axiomatic* for the meta-requirement (cross-level compatibility). The postulate itself is a structural requirement for AAT's internal consistency: if the scope condition doesn't restrict which level the theory applies to, the predictions must not contradict across levels.

The operational consequences decompose into three layers with distinct epistemic statuses:

- **Scope selection** ( #scope-composite-agent, robust-qualitative): which decompositions constitute composites. The scope condition is a disjunction of three qualitatively distinct routes (shared objective, hierarchical derivation, mutual benefit); whether they reduce to a common scalar threshold is open. Coverage of well-understood cases holds via the disjunction.

- **Admissibility of composite dynamics** ( #form-composition-closure, conditional): the (A1)-(A4) conditions are stated formally; the bridge lemma is conditional on the incremental sector bound (DA2'-inc), strictly stronger than (A4) alone.

- **Transfer of individual-agent results** (tier-dependent): Tier 1 composites transfer Section I/II results exactly; Tier 2 transfer with degraded factors; Tier 3 require per-domain verification. This is the sharpest scoping of "every result applies at every level" — it applies at every level *for Tier 1 composites*, degrades gracefully for Tier 2, and holds per-domain for Tier 3.

The composite contraction rate has two epistemic layers. **Tier 1M is derived (exact)**: under (CT1)–(CT3) on each sub-agent and an admissible composition topology, $\lambda_c$ admits the closed-form lower bound from #result-contraction-template's (CC-parallel) / (CC-cascade) / (CC-feedback) — the slowest-sub-agent / coupling-adjusted / heterogeneous (CM2-M) cases respectively. The screening condition $\tau_{\text{eq}} \ll \tau_{\text{ext}}$ is, in this regime, the formal persistence condition $\alpha_c \gt \rho_{\text{eff}}/R_c$ specialized to internal-vs-external rate balance — not heuristic. **Tier 2 and Tier 3 retain heuristic / discussion-grade status**: the closed-form composite rate does not transfer (Tier 2 with local degradation; Tier 3 per-domain), and $\tau_{\text{eq}} \ll \tau_{\text{ext}}$ remains a useful screening test without entailing macro-level persistence. The "small gap between screening and Tier 1M conditions in common settings" is an empirical claim about the population of real composites, not a derived fact.

## Discussion

**The same pattern as individual persistence.** The persistence condition says: there is a measurable threshold below which an individual agent's mismatch grows without bound and the agent degrades. Composition consistency says the same thing at the composite level: there is a measurable threshold below which the composite description breaks down. Under Tier 1M, the threshold is exact and closed-form — $\alpha_c \gt \rho_{\text{eff}}/R_c$ with $\alpha_c$ from (CC-parallel) / (CC-cascade) / (CC-feedback). Under Tier 2 / Tier 3, the threshold is only qualitatively captured by the screening ratio $\tau_{\text{eq}} / \tau_{\text{ext}}$ and exact transfer requires local-region or per-domain verification. The two-tier structure is the precise way "the theory applies broadly" — broadly under Tier 1M, qualitatively-with-conditions outside it.

**What this buys the theory.** With composition consistency stated early:
- Section I/II results lift to the composite level *for Tier 1 composites passing the composition scope condition*, with degraded-factor lift for Tier 2 and per-domain verification for Tier 3 — the three-layer decomposition above makes this precise rather than leaving "applies at every level" as an unbounded claim
- Section III becomes the study of *what happens near and beyond the threshold* — coordination overhead, unity dimensions, symbiogenic transitions, adversarial dynamics — rather than a separate multi-agent theory
- The formal test for composition validity ( #form-composition-closure) develops the rigorous version of the timescale condition, with the incremental sector bound identifying which agent classes admit the contraction needed for cross-level transfer; #result-contraction-template lifts that bound into a metric-aware framework where (CC-parallel) / (CC-cascade) / (CC-feedback) yield the topology-indexed closed forms cited above

**When composition fails.** The persistence condition $\alpha_c \gt \rho_{\text{eff}}/R_c$ (Tier 1M) — or its qualitative shadow $\tau_{\text{eq}} \ll \tau_{\text{ext}}$ (Tier 2 / Tier 3) — fails when:
- Internal coordination slows: $C_{\text{coord}}$ from #der-tempo-composition rises through coupling overhead, conflict, or bureaucratic process, depressing $\alpha_c$ below the threshold; equivalently, $\tau_{\text{eq}}$ stretches.
- External dynamics accelerate: $\rho_{\text{ext}}$ rises (adversary acts faster, market shifts, crisis compresses decision timescales); equivalently, $\tau_{\text{ext}}$ shortens.
- Both simultaneously (the classic organizational failure mode — internal friction increases while external demands intensify).

This is the formal analog of Brooks's Law: adding people to a late project increases $\varepsilon^\ast \nu_c$ in $\rho_{\text{eff}}$ ( #der-tempo-composition's coordination-overhead bound) and stretches $\tau_{\text{eq}}$ while $\rho_{\text{ext}}$ and $\tau_{\text{ext}}$ stay fixed (the deadline doesn't move). Under Tier 1M the mechanism is formal — eventually the persistence inequality flips. Under Tier 2 / Tier 3 the mechanism is qualitative. Whether the specific mechanism (coordination-overhead saturation crossing the persistence threshold) is the dominant cause of Brooks's Law in practice is an empirical question.

**The boundary is a modeling choice.** A development team is simultaneously: individual developers (each an AAT agent), the team (a composite AAT agent), and part of an organization (a sub-agent within a larger composite). The scope condition is satisfied at every level. Composition consistency ensures the theory doesn't give contradictory answers about observable quantities (e.g., whether the team persists) regardless of which boundary is chosen.

**What composition consistency does NOT say.** It does not specify the form of the composition laws — those are derived in Section III ( #der-tempo-composition). It does not say every decomposition is equally useful for analysis. And it does not require perfect internal coordination — only that internal equilibration is fast relative to external dynamics.

## Working Notes
- **Strengthening attempt — outcome.** The "macro-timescale bounded below by slowest sub-agent" claim was attacked via #result-contraction-template's compositional theorems before falling back to heuristic-only framing. Under Tier 1M (sub-agents satisfying (CT1)–(CT3) with metrics $M_i$, rates $\lambda_i$): (CC-parallel) yields $\lambda_c = \min_i \lambda_i$ exactly under blockdiag composite metric — the formal version of "composite is no faster than the slowest sub-agent"; (CC-cascade) yields the same bound up to coupling-gain adjustment; (CC-feedback) / (CM2-M) yields the heterogeneous closed-form inequality. No new math required — the strengthening is achieved by binding the postulate's heuristic to the existing (CC-*) closed forms via the DA2'-inc ≡ (CT2)-at-$M=I$ equivalence in #form-composition-closure. Tier 2 (local with $\kappa(D\hat o)^2$ degradation) and Tier 3 (per-domain) retain heuristic / discussion-grade screening; this residual is what the strengthening attempt could not eliminate.
- The timescale separation condition is essentially the singular perturbation argument from #der-temporal-nesting applied to composition: the fast internal dynamics approximately equilibrate, and the composite's behavior is described by the slow (external) dynamics on the equilibrium manifold. The formal connection should be made explicit when temporal-nesting is reviewed.
- Composition of directed separation: if each sub-agent's $f_M$ is $G_t$-independent, does the composite's $f_M^c$ remain $G_t^c$-independent? Hypothesis: goal-blindness composes, BUT coordination routing may break it — if which observations reach the composite depends on the shared objective, the composite's effective observation function is goal-dependent. This is the organizational analog of the LLM scope restriction in #der-directed-separation.
- The "atomic agent" question: if every agent is decomposable, where does it bottom out? At agents whose internal dynamics are not usefully described by AAT — below the level where observations, actions, and uncertainty exist, the scope condition fails and the recursion terminates.
- The relationship to holons (Koestler 1967): an AAT agent satisfying composition consistency is a holon — simultaneously a whole (analyzable as a single agent) and a part (decomposable into sub-agents). The term is occasionally useful but carries significant mystical baggage from later appropriations. Use sparingly.


---

### Source: `disc-stability-certificate.md`

```yaml
---
slug: disc-stability-certificate
type: discussion
status: discussion-grade
depends:
  - result-certificate-existence
  - result-sector-persistence-template
  - deriv-sector-condition
stage: draft
---
```


# Discussion: The Stability Certificate — One Object Behind the Cross-Sectional Meta-Patterns

AAT's cross-sectional structure is the geometry of a single object — the **equilibrium stability certificate**, the positive-definite form whose existence certifies that an agent can correct itself faster than its world drifts; operator-sector is that object's interior, the separability pattern its scope of existence, additive-coordinate-forcing its forced identity, and the identifiability floor its boundary, with composition the question of whether it survives projection.

The three meta-segments #disc-separability-pattern, #disc-identifiability-floor, and #disc-additive-coordinate-forcing read, separately, as three independent organizing insights that happen to recur. This segment names the object they are facets of. The relationship is the same one #disc-additive-coordinate-forcing already runs at smaller scale ("layer-specific manifestations of a single geometric object"), raised to the framework: not a fourth meta-pattern *alongside* the three, but the spine the three are projections of.

## Formal Expression

### The object

*[Definition (stability-certificate)]*

For an agent with error dynamics $\dot e=-F(e)$ about an equilibrium $e^\ast$ ($F(e^\ast)=0$, $F\in C^1$ near $e^\ast$, Jacobian $J:=DF(e^\ast)$), a **stability certificate** is a symmetric positive-definite $\mathcal M$ for which the one-point sector condition holds in the $\mathcal M$-inner-product on a ball $\mathcal B_R(e^\ast)$:

$$\langle F(e),\,e-e^\ast\rangle_{\mathcal M}\;\ge\;\kappa\,\lVert e-e^\ast\rVert_{\mathcal M}^2,\qquad \kappa\gt0. \tag{C}$$

The certificate is not unique: it is whatever positive-definite form makes the dynamics contract. In the recurring sub-cases it specializes — to the Fisher information for Bayesian agents, to $(P^-)^{-1}$ for Kalman agents, to the loss Hessian for gradient agents, and to a plant-selected Lyapunov metric for linear-Hurwitz or PID agents. These are not four separate stories; they are one object under four certificates.

### The anchor

*[Result (cited: #result-certificate-existence)]*

The object is load-bearing only because its existence is not a definition but an equivalence: **a stability certificate exists iff the agent is exponentially stable about its target** — operator-sector in *some* inner product and exponential stability are the same statement, with the certificate as the converse-Lyapunov witness, and the certificate admits a strict strength ladder R0 ⟸ R1 ⟸ R2 (widest one-point/local; cocoercive; Čencov-forced). This is the segment-level form of the contraction-over-drift organizing principle. The equivalence, the ladder, and the proof are stated and derived exactly in #result-certificate-existence; this spine cites that result and builds the cross-sectional reading on it rather than re-deriving it.

### The four facets

*[Discussion]*

The certificate is one object; the cross-sectional meta-patterns are its facets on the positive-semidefinite cone $\mathbb S^n_{\succeq0}$:

| Facet | Meta-segment | What the facet is | Canonical home |
|---|---|---|---|
| **Interior** | #result-sector-persistence-template, #result-contraction-template | $\mathcal M\succ0$ on the scope ball: the contraction holds | the template segments |
| **Scope of existence** | #disc-separability-pattern | the region where a certificate exists at all (separable core / structured repair / general open) | M2 |
| **Forced identity** | #disc-additive-coordinate-forcing | *which* certificate: Čencov forces $\mathcal M=$ Fisher uniquely in statistical scope; matched (existence-only) elsewhere | M3 |
| **Boundary** | #disc-identifiability-floor | $\mathcal M$ drops rank ($\partial\mathbb S^n_{\succeq0}$): the inferential task is structurally impossible | M1 |
| **Projection behaviour** | #form-composition-closure | whether a *common* certificate survives coarse-graining; the closure defect $\varepsilon^\ast$ is the certificate's projection-residue | composition-closure |

Each meta-segment retains its own canonical home and per-instance derivations; this segment claims only the recognition that they are facets of one object, and what that buys (Discussion below).

### The three obstructions are distinct — the plurality is the content

*[Discussion]*

A tempting reading is that the certificate's failures are one obstruction seen three ways (a single "failure of integrability"). They are not. The three failure modes are irreducibly distinct, each invariant under the others' degrees of freedom:

- **Forced-identity failure — Helmholtz–Hodge.** $J$ non-symmetric ⟹ the field is not a gradient ⟹ no potential ⟹ the certificate is *matched* (converse-Lyapunov existence), not *forced* (Čencov). A non-symmetric Hurwitz $J$ still has a certificate (it is *not* on the boundary), so this is an M3 failure, not an M1 one. Invariant: symmetry of $J$.
- **Existence failure — Sylvester's law of inertia.** The certificate drops rank. Every coordinate/metric change acts on the certificate by congruence; congruence preserves inertia; so a rank-deficient certificate is rank-deficient in *every* coordinate. The boundary is invariant under the agent's entire representational freedom (that freedom *is* the congruence orbit); the only escape is rank-augmentation — genuinely new information, not a re-mapping. (Detailed in #disc-identifiability-floor's Sylvester finding.) Invariant: inertia under congruence.
- **Projection failure — Mori–Zwanzig / Schur.** Coarse-graining is a non-invertible projection. The certificate-as-metric survives (the Schur complement of a positive-definite form is positive-definite) but the *dynamic* guarantee does not: the closure defect $\varepsilon^\ast$ equals the norm of the Mori–Zwanzig memory commutator, zero exactly when the resolved subspace is $J$-invariant. Invariant: $J$-invariance of the resolved subspace.

Each obstruction is untouched by the others' freedoms: a metric change does not fix non-invariance; projection does not fix non-symmetry; rank-augmentation does not fix a memory kernel. That mutual invariance is the reason the cross-sectional structure is *several* meta-patterns and not one — stated as a structural fact rather than left as "they are different concerns."

## Epistemic Status

*Discussion-grade* at the organizing-principle level. This segment names a single object behind separately-derived results; it is not itself a new theorem. What is derivative here is the recognition that the cross-sectional meta-patterns are facets of one certificate — the recognition, not a fresh derivation, is the content.

*Constituent results retain their own, higher status.* The certificate-existence equivalence (Lyapunov theorem; Formal Expression "anchor") is *exact* at the linearized level and *exact-with-standard-remainder* locally. The certificate-strength ladder R0/R1/R2 is *exact* as an ordering of conditions. The boundary-irreducibility mechanism (Sylvester's law) is *exact*; its full statement and per-instance verification live in #disc-identifiability-floor. The projection-residue identification ($\varepsilon^\ast=$ memory-commutator norm) is *robust-qualitative*, with the per-case content in #form-composition-closure. The forced-vs-matched distinction (Čencov statistical-scope-only) is established in #disc-additive-coordinate-forcing.

*Scope honesty.* The anchor equivalence is linearized/local — this is the level at which AAT's persistence results already operate (sector conditions, contraction templates, the bridge lemma all linearize about the equilibrium), so it is not a weakening relative to the rest of the theory, but it is a genuine scope statement and is not papered over: there is no claim that one-point operator-sector is equivalent to *global* exponential stability (it is not, in general). The synthesis claim — that AAT's *entire* cross-sectional structure is this one cone — is *robust-qualitative*: each per-facet identification is exact or cited, and the "all of it" is as strong as those identifications jointly, no stronger. Whether exactly three obstructions exhaust the failure modes is not proved; three are established and each is exact, but exhaustiveness is open.

Max attainable: *discussion-grade* for the organizing claim (it is a presentational spine, not a derivation). The anchor equivalence and the Sylvester mechanism retain their *exact* status at their own canonical homes.

## Discussion

**What the spine buys.** Three things. (i) It converts "AAT has several recurring organizing insights" into "AAT's cross-section is one object's facets," which is the difference between a catalog and a structure — a reader who holds the certificate picture can predict where the meta-patterns will bite (interior / scope / forced-identity / boundary / projection) rather than meeting them as separate surprises. (ii) It grounds the long-standing organizing slogan — *an adaptive system is an operator whose contraction rate exceeds its disturbance rate* — at segment level, as the anchor equivalence rather than as a heuristic. (iii) It makes the framework's scope-honesty sharper: the prior positioning that the identifiability floor is "orthogonal" to the contraction machinery is replaced by the exact geometric statement that the floor is the *boundary* of the very cone whose interior the contraction machinery is, with the boundary held invariant by Sylvester's law against the framework's only representational freedom.

**Relationship to the facet segments.** This segment cross-references; it does not restate. #disc-identifiability-floor remains the canonical home of the floor instances and the Sylvester mechanism; #disc-separability-pattern of the separable-core / structured-repair / general-open ladders; #disc-additive-coordinate-forcing of the Čencov/Cauchy-FE forcing; #result-sector-persistence-template and #result-contraction-template of the contraction machinery; #form-composition-closure of the closure defect. The spine's contribution is the cross-segment recognition and the anchor equivalence, not any per-facet content.

**Why the plurality of obstructions is a feature.** Had the three failure modes collapsed to one, the spine would be a single clean theorem — elegant but false on the evidence (the integrability collapse fails: a non-symmetric Hurwitz field has a certificate yet no potential; congruence is invertible while projection is not). The honest structure is more useful: it tells a future agent precisely *not* to seek a single mechanism unifying the floor, the closure defect, and the forcing failure — they are Sylvester, Mori–Zwanzig, and Helmholtz respectively, and the proof of their distinctness is their mutual invariance. The unification is real at the object level and the no-go is real and plural at the failure level; both are load-bearing.

**Complementarity with the existing meta-segment framing.** #disc-separability-pattern names AAT's positive half and #disc-identifiability-floor its negative half; #disc-additive-coordinate-forcing names the constructive half. The spine names what all three are halves *of*. The three remain the right reading lenses for any individual segment; the spine is the reason those lenses compose rather than merely coexist.

**The accumulation-typing pattern is the temporal dual of the Interior facet, not a fifth meta-segment (the D3 register answer).** The Interior facet ( #result-sector-persistence-template) is the *static* statement "$\mathcal M\succ0$ on the scope ball: the contraction holds." Read in *accumulation/temporal* vocabulary it is the statement "the operator carrying a per-step residue to its accumulated consequence is bounded" — and, per that template's typed-bridge framing, this is **two-model, not one operator** (Model D / Model S; the $1/\alpha$ vs $1/\sqrt\alpha$ scaling and the Cor-A.1S.1 categorical containment dichotomy are the fingerprint that they are different functionals, not one read in two norms). The recurring *accumulation-type confound* — asking about a per-step residue in the vocabulary of its accumulation, which dissolved the $\varepsilon^\ast(N)$ poly-vs-exponential question and recurred across the framework — run through this segment's own test ("is a candidate organizing pattern a new facet, or a genuinely new object?") returns **neither**: it is a new *reading* of an existing facet (the temporal/representation dual of the Interior), so the cone gains no sixth facet and the framework no fifth independent meta-segment. The notation that carries it is durable canon ( `NOTATION.md` §"Accumulation typing"); its theorem-anchor is the Interior facet's template. The structure becomes load-bearing exactly at the *Interior↔Boundary transition* — contraction degrading toward rank-loss — where two operator families separate: $\mathcal A_{\mathrm{refl}}$ (a reflected Lindley/Loynes walk whose content is the driftless $\mu=0$ boundary) instantiates the template on the turnover index ( #der-identity-continuity-threshold), while $\mathcal A_D$ (the linear destroy-and-reconstruct contraction whose norm diverges as the gap closes) is the honest *non-transfer* boundary ( #der-turnover-information-recursion). The $\mu=0$ boundary of the one is the pole of the other — independently adjudicated ( `spikes/adjudicate-disc-m-preservation-operator.md`) — which is why they are distinct operators and treating one as a linearization or normalization of the other is a category error. This is the framework's first worked answer to its own "new pattern?" test: *no — it is this existing object seen from the time side.*

## Findings

### The Cross-Sectional Meta-Patterns Are Facets of One Stability Certificate

**Brief:** Think of an adaptive agent as trying to stay on a moving target, and ask one question: is there a way of measuring "how far off am I?" such that every correction the agent makes provably shrinks that measure faster than the world pushes it back out? That measuring-stick is the stability certificate. The whole cross-sectional skeleton of AAT turns out to be facts about *this one stick*: the agent can keep up exactly when the stick exists and is positive (operator-sector — the interior); the framework's reach is exactly the region where some such stick exists (the separability pattern); when the stick is pinned down uniquely it is pinned by one classical invariance theorem and only in the statistical case (additive-coordinate-forcing); and the agent provably *cannot* keep up exactly when the stick goes flat in some direction (the identifiability floor — the boundary), with a second classical theorem (Sylvester's law of inertia) proving no change of measuring units ever un-flattens it — only genuinely new information does. A thoughtful non-specialist can carry the whole structure away from the one picture: existence of the stick = can adapt; flatness of the stick = a blind spot no re-measurement fixes; uniqueness of the stick = a special (statistical) privilege, not the general case; and looking at the stick through a coarse lens (composition) keeps its shape but loses its guarantee by exactly a memory term.

**Impact:** Reorganizes AAT's self-description from three independent meta-patterns plus a contraction mechanism into one object with four facets and one anchor equivalence, so the framework's cross-section can be read predictively rather than as a catalog of separate recurrences. Grounds the organizing slogan (contraction-rate-exceeds-drift) at segment level via the Lyapunov-theorem equivalence, discharging the long-standing "not yet surfaced at segment level" status. Sharpens the scope-honesty posture: "the floor is orthogonal to operator-sector" becomes "the floor is the boundary of the cone whose interior is operator-sector, held invariant by Sylvester's law against the framework's only representational freedom." Bounds its own claim honestly: the unification is at the object level; the three failure obstructions are provably *distinct* (Helmholtz / Sylvester / Mori–Zwanzig), and that plurality is precisely why AAT carries multiple cross-sectional meta-patterns rather than one — now a stated structural fact instead of an intuition. Gives every future organizing-pattern candidate a test: is it a new facet of the certificate, or a genuinely new object?

**Novelty Claim:** *Claim recognition* that AAT's cross-sectional meta-patterns (separability, identifiability-floor, additive-coordinate-forcing) and its contraction machinery are facets — interior, scope-of-existence, forced-identity, boundary, projection-behaviour — of a single object, the equilibrium stability certificate; together with *claim synthesis* binding the Lyapunov-theorem certificate-existence equivalence, the Sylvester-law boundary-irreducibility, and the Mori–Zwanzig projection-residue into one cross-sectional structure. The constituent theorems are classical; the contribution is the recognition that AAT's separately-derived meta-patterns are one object's facets and that their failure modes are provably plural.

**Related Work:**
- Lyapunov, A. M. (1892), *The General Problem of the Stability of Motion*; Khalil, H. K. (2002), *Nonlinear Systems* 3rd ed., Thm 4.6 (found 2026-05-14) — *formal antecedent* — the certificate-existence equivalence (operator-sector in some metric ⟺ Hurwitz).
- Sylvester, J. J. (1852), *Phil. Mag.* 4(23):138–142; Horn & Johnson (2013), *Matrix Analysis* 2nd ed., Thm 4.5.8 (found 2026-05-14) — *formal antecedent* — the boundary-irreducibility mechanism; full treatment in #disc-identifiability-floor.
- Mori (1965) / Zwanzig (1961); Chorin, Hald & Kupferman (2002), *Physica D* 166:239 (found 2026-05-14) — *formal antecedent* — the projection-residue (memory kernel) underlying the composition facet; per-case content in #form-composition-closure.
- The facet segments #disc-identifiability-floor, #disc-separability-pattern, #disc-additive-coordinate-forcing — *adjacent* — each carries its own per-instance prior-art landscape; the spine adds the cross-segment object, not the per-facet priors.

**Search Log:**
- 2026-05-14 (*targeted*): The recognition was assembled from classical pieces (Lyapunov / Sylvester / Mori–Zwanzig) plus the framework's own meta-segments. The search target was whether "an integrated agent theory's cross-sectional meta-patterns are facets of a single stability-certificate cone" appears as an articulated structure elsewhere. Not found at this depth; the constituent theorems are textbook and the per-facet identifications are individually well-precedented, but the cross-segment unification as a framework spine is a fresh presentational recognition. Expected to remain *recognition*/*synthesis*-tier under deeper search — the pieces are classical; the assembly is the contribution. Per-facet comprehensiveness is inherited from the facet segments, not from a fresh cross-facet search.

## Working Notes

- **Provenance.** The certificate-spine recognition, the anchor equivalence, the Sylvester boundary mechanism, and the broken-integrability-triad result were worked out in the 2026-05-14 operator-family-unification cycle (the deep push of the predecessor C1 "2-instance-plus-1-consequence" question and the prior co-owner "do not elevate unless O-BP10 surfaces at segment level" gate, now met by the anchor equivalence). See CHANGELOG 2026-05-14 for the cycle narrative. The originating spike is absorbed archaeology, not a live reference; the load-bearing content is in this segment, #result-certificate-existence, and the #disc-identifiability-floor Sylvester finding.
- **Dependency rationale (for Gate-1 audit).** `depends:` lists `result-certificate-existence` (the anchor equivalence this spine builds the cross-sectional reading on — a genuine dependency, consumed not merely recognized) plus `result-sector-persistence-template` and `deriv-sector-condition` (the persistence machinery the anchor's drift half rests on). #disc-identifiability-floor, #disc-separability-pattern, #disc-additive-coordinate-forcing, and #form-composition-closure are **cross-referenced as facets, not depended on**: per FORMAT.md Gate 1, a dependency is genuine only when the segment uses the referenced segment's definitions/results, not when it is recognized or related in Discussion. The spine *recognizes* the meta-segments as facets of one object; it does not consume their definitions to make its claim. This is why the spine is correctly placed *before the three meta-segments* in OUTLINE (it is the object they are facets of, so it reads first) without an ordering violation — the facet relationship is lateral recognition, not a dependency edge — while being placed *after* `#result-certificate-existence` (a genuine dependency, which therefore precedes it). Treat the facet `#…` references as expected forward/lateral cross-refs (FORMAT.md §Cross-References).
- **Provisional slug.** `disc-stability-certificate`. Alternative considered: `disc-certificate-cone` (names the geometry rather than the object). Subject-noun discipline favours the object ("the stability certificate"); the cone/interior/boundary is what the segment *says about* it. Route through the naming pipeline if a better name surfaces; the spike verdict floated both.
- **Provisional OUTLINE position.** Placed in `## *Appendices* Details` immediately before #disc-identifiability-floor, as the lead of the four-row meta-segment cluster (spine → M1 → M2 → M3). Provisional because: (a) the meta-segments may eventually warrant their own chapter rather than Appendix-A residence; (b) if the OUTLINE preamble is reframed to lead with the spine, the cluster likely moves to a more prominent position. Both are propagation steps below, not landed here.
- **Propagation plan (ordered by commitment; steps 6–7 are framework-voice keystones gated on Joseph, not auto-executed):**
  1. #disc-identifiability-floor — cross-ref line in its "complementarity" Discussion paragraph naming the spine as the object whose boundary it is. (Sylvester finding + Working Note already point here.) Cross-ref only.
  2. #disc-separability-pattern — parallel line: it is the *scope-of-existence* facet (where the certificate $\succ0$). Cross-ref only.
  3. #disc-additive-coordinate-forcing — frame its (PI)/Čencov content as the *forced-identity* facet. Cross-ref only; Čencov machinery's canonical home stays M3.
  4. #result-sector-persistence-template / #result-contraction-template — one Discussion sentence: the template condition is the certificate interior; cross-ref the spine for the cone reading. No formal change.
  5. #form-composition-closure — Discussion line framing $\varepsilon^\ast$ as the certificate's projection-residue and Liberzon as "no common certificate"; cross-ref the spine. (Its Mori–Zwanzig Working Note already exists.)
  6. **O-BP10 keystone (Joseph's call).** Recommend this segment *is* O-BP10's segment-level home: the slogan is its one-sentence summary, the equivalence is its anchor. The PROPOSALS Bundle-1 O-BP10 entry then points here. Do not auto-rewrite Bundle 1.
  7. **OUTLINE preamble reframe (highest commitment; Joseph's call).** OUTLINE.md line 17 currently opens "Three meta-segments form AAT's cross-sectional structure: #disc-separability-pattern … #disc-identifiability-floor … #disc-additive-coordinate-forcing …". Proposed replacement, for Joseph's confirmation before it goes live in the auditor-visible preamble: *"AAT's cross-sectional structure is one object — the equilibrium stability certificate ( #disc-stability-certificate). Its interior is operator-sector (the contraction machinery); its scope of existence is the separability pattern ( #disc-separability-pattern, positive half); its forced identity is additive-coordinate-forcing ( #disc-additive-coordinate-forcing, constructive half, Čencov-forced in statistical scope only); its boundary is the identifiability floor ( #disc-identifiability-floor, negative half); and its behaviour under coarse-graining is the composition-closure defect. Reading any segment through the certificate and its facets surfaces what makes it load-bearing: whether a certificate exists for it, which one is forced, what boundary it abuts, and whether it survives projection."* Execute only on Joseph's confirmation, having seen the segment land first.
- **Open edges (from `99-verdict.md`).** Anchor equivalence is linearized/local (stated in Epistemic Status). "Exactly three obstructions" is robust-qualitative, not proved exhaustive — a fourth (e.g. non-autonomous certificate drift for time-varying systems) is not searched. Sylvester is proved finite-dimensional; the function-space ($M_t$ for logogenic agents) extension is unchecked and flagged for any future logogenic application, not load-bearing for the AAT-core claim.


---

