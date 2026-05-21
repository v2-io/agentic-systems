# Cluster Reference: Composite Agency and Closure Defect

**Overview:** Defines composite macro-agents via the commutativity of coarse-graining (the closure defect), providing a closed cybernetic proof of Brooks's Law and the mechanism of Symbiogenesis.

---

## Canonical Source Segments

### Source: `hyp-symbiogenic-composition.md`

```yaml
---
slug: hyp-symbiogenic-composition
type: hypothesis
status: robust-qualitative
depends:
  - scope-composite-agent
  - form-objective-functional
  - def-strategy-dimension
  - form-structural-change-as-parametric-limit
stage: draft
---
```


# Hypothesis: Symbiogenic Composition

Symbiogenesis is an asymmetric composition mechanism in which one agent (the *host*) integrates another (the *endosymbiont*) as a specialized sub-component, with the endosymbiont's objective gradually subsumed into the host's. It is distinct from peer coupling ( #form-composition-closure) and from population-level restructuring (the extreme transition motif drawn from Miller 2022, discussed in #result-structural-adaptation-necessity): symbiogenesis is how composite agents *come into existence* by crossing the #scope-composite-agent from below. The mechanism is well-attested empirically (eukaryote formation, firm mergers, legal-precedent adoption, language families) but formally underspecified within AAT. This segment captures the phenomenon and flags the specific formalization gaps.

## Formal Expression

*[Hypothesis (symbiogenic-composition)]*

Given two purposeful agents $A_h$ (host) and $A_e$ (endosymbiont), each satisfying #scope-agency, symbiogenic composition is a process on the joint state space with three coupled dynamics:

### (S-1) Objective absorption

The endosymbiont's objective $O_e$ transforms toward alignment with or derivation from the host's objective $O_h$:

$$O_e(\tau) \;\xrightarrow{\tau \to \tau_{\text{consolidated}}}\; \mathcal D_e(O_h)$$

where $\mathcal D_e$ is a derivation functional (in the sense of route (C-ii) in #scope-composite-agent): $O_e$ becomes a sub-objective derived from $O_h$. Before: $O_h$ and $O_e$ are independent objectives, no route of #scope-composite-agent applies, and the pair is a multi-agent system ( #scope-multi-agent) rather than a composite. After: $O_e$ is a role within $O_h$; route (C-ii) applies; the composite $(A_h, A_e)$ satisfies the composition scope condition.

### (S-2) Function transfer

Structural content from the endosymbiont's state (elements of $M_e$ or $\Sigma_e$) transfers to or becomes accessible by the host:

$$\{M_h, \Sigma_h\}(\tau) \;\xrightarrow{\tau \to \tau_{\text{consolidated}}}\; \{M_h, \Sigma_h\} \cup \mathcal F(M_e, \Sigma_e)$$

where $\mathcal F$ is a transfer mapping (structure-preserving integration of endosymbiont functions into host state). In biological symbiogenesis: gene transfer. In organizational symbiogenesis: acquired firm's processes, patents, know-how integrated into acquirer's operations. This is the grafting operation of #form-structural-change-as-parametric-limit in its cross-agent form — the host grafts structure originating in the endosymbiont.

### (S-3) Autonomy reduction

The endosymbiont's effective action space contracts; many of its choices become fixed by the host's coordination:

$$\mathcal A_e^{\text{effective}}(\tau) \;\xrightarrow{\tau \to \tau_{\text{consolidated}}}\; \mathcal A_e^{\text{restricted}} \subsetneq \mathcal A_e^{\text{initial}}$$

The endosymbiont retains enough autonomy to avoid catastrophic transfers (e.g., mitochondria retain some genome to handle local fast-timescale responses that would be hazardous to route through the host nucleus) but loses most independent decision-making.

### Integrated transition

At consolidation, the joint system is a single composite agent $A_c$ whose substate contains the integrated structure:

$$X_c = \big(M_c, G_c\big) = \big(M_h \cup \mathcal F(M_e, \Sigma_e),\; (O_c, \Sigma_c)\big) \quad \text{with } O_c \approx O_h$$

The endosymbiont persists as a specialized sub-component of the host, not as an independent agent. The #scope-composite-agent is now satisfied; the peer-coupling machinery of #form-composition-closure applies to the resulting composite.

## Epistemic Status

*Robust qualitative.* Max attainable: *robust qualitative* — the phenomenon is well-attested empirically across biological and social domains, but a general mathematical formalization within AAT is open.

What is well-established (externally):

- The existence of symbiogenesis as a distinct evolutionary mechanism (Mereschkowsky 1905, 1910; Sagan 1967; Margulis & Sagan 1997). Mitochondria and chloroplasts are the paradigm cases.
- The social analog in firms, technology, language, legal systems, religions (Miller 2022, Appendix B).
- "Innovation by parts" as qualitatively different from "innovation by sparks" (gradual mutation) — Miller's framing.

What is *not* derived within AAT:

- A formal model of the objective-transfer dynamics (S-1). What evolutionary or optimization process drives $O_e \to \mathcal D_e(O_h)$?
- A formal specification of the transfer functional $\mathcal F$ in (S-2). What structure is preserved, what is lost, what is transformed?
- A precise characterization of autonomy reduction (S-3). Why does the endosymbiont retain some autonomy rather than becoming fully deterministic?
- Quantitative predictions — e.g., when symbiogenesis is favored over peer coupling, what governs the timescale of consolidation, under what conditions it reverses.

The three dynamics (S-1), (S-2), (S-3) are proposed schemas, not results. A follow-up development of an AAT-specific dynamical model is the natural next step.

## Discussion

**The role of this mechanism in Section III.** Three distinct composition mechanisms are now in scope:

1. **Peer coupling** ( #form-composition-closure, #der-team-persistence, #der-tempo-composition) — sub-agents interact through shared environment; closure defect measures faithfulness of projection. Presumes scope-satisfaction via at least one route of #scope-composite-agent (not a scalar $U_O$ threshold).
2. **Extreme transition motif** (Miller 2022; introduced in #result-structural-adaptation-necessity; pending dedicated segments for composition-transition dynamics, latent structural diversity, and endogenous coupling) — population-level restructuring via neutral drift / niche creation / cascading displacement. $U_O$ shifts across a population as agent types replace one another.
3. **Symbiogenesis** (this segment) — hierarchical absorption. $U_O$ crosses the composition scope condition from below, creating a composite that did not previously exist.

Before symbiogenesis, the sub-agents were a multi-agent system ( #scope-multi-agent) but not a composite. After, the resulting composite is subject to all of AAT's composition machinery. The symbiogenic transition is the specific dynamical process of composite-agent identity creation.

**Why this cannot be modeled as peer coupling.** Peer coupling assumes pre-existing sub-agents being projected into a macro-description. The closure-defect framework presupposes the composite exists; it measures how faithfully the macro tracks the micro. Symbiogenesis is about a composite *coming into being* from two previously-independent agents. No projection Λ of the pre-symbiogenic system yields the post-symbiogenic composite, because the endosymbiont's objective *changes* during the process — its objective is different before and after. The transformation is intrinsic to the sub-agents' state, not an external projection choice.

**Why this cannot be modeled as extreme transition.** The extreme transition motif operates at the population level with many agents, neutral drift of types, and niche-construction dynamics. Symbiogenesis is typically between two specific agents (or a small number) and proceeds through a specific asymmetric integration rather than through statistical population dynamics. The mechanisms overlap — symbiogenesis often occurs as part of a larger transition — but the core mechanism of symbiogenesis (bilateral asymmetric integration) is distinct from the population-level dynamics of extreme transitions.

**Examples across domains.**

| Domain | Host | Endosymbiont | Integrated composite |
|---|---|---|---|
| Biology | Archaeal host cell | $\alpha$-proteobacterium | Eukaryotic cell (mitochondrion persists as organelle) |
| Biology | Eukaryotic cell | Cyanobacterium | Plant cell (chloroplast persists as organelle) |
| Commerce | Acquiring firm | Acquired firm | Merged firm (acquired operates as division) |
| Technology | Base platform | Integrated component | Composite product (component operates within host system) |
| Linguistics | Host language | Adopted vocabulary/grammar | Creolized / evolved language |
| Law | Legal system | Adopted precedent | Evolved jurisprudence (precedent operates as doctrine) |
| Religion | Host tradition | Absorbed elements | Syncretic practice |

In each case: asymmetric integration, autonomy reduction of the absorbed entity, gradual objective subsumption, functional specialization.

**Connection to #form-structural-change-as-parametric-limit.** The single-agent "grafting" operation in #form-structural-change-as-parametric-limit is within-agent — an agent incorporates external structure into its own $\Sigma_t$. Symbiogenesis is cross-agent — the grafted structure originates in another agent, and the integration is accompanied by that other agent's objective being absorbed. These are related but distinct: grafting is the structural-change mechanism on the host side; symbiogenesis is the bilateral process that includes grafting plus objective-absorption plus autonomy reduction.

**Rate-distortion interpretation (connecting to #result-unity-closure-mapping).** Under the Information Bottleneck conjecture in #result-unity-closure-mapping, peer coupling is IB compression with the relevance variable defined by a shared composite objective. Symbiogenesis is the process by which the relevance variable itself shifts: from two separate IB problems (each sub-agent's own survival objective) to a single IB problem (the composite's survival objective). The symbiogenic transition creates the shared relevance variable, which in turn makes the IB frontier well-defined for the composite. This is a structural shift in the IB problem, not a compression along a fixed IB frontier.

## Working Notes

- **Objective-transfer dynamics (S-1).** The most load-bearing open formalization. What process drives $O_e \to \mathcal D_e(O_h)$? Candidates: evolutionary selection (endosymbionts whose objectives align with host survival are selected for, since the alternative is extinction); bounded-rationality constraint (coordinating two divergent objectives exceeds the endosymbiont's capacity, forcing simplification); explicit design (firm mergers where acquired objectives are deliberately restructured). Each gives a different dynamical equation.
- **Function transfer $\mathcal F$ (S-2).** Needs to respect the structure of the host's $M_h$ and $\Sigma_h$. In biology, gene transfer preserves molecular functions but changes regulatory context. In social analogs, the analog is: functions are preserved, but their triggers and dependencies change. A general specification is open.
- **Autonomy reduction (S-3).** Why not complete? The endosymbiont retains some autonomy because complete integration would eliminate the fast local response capacity that made symbiogenesis advantageous in the first place. A cost-benefit analysis on autonomy retention (in the style of #form-strategy-complexity-cost) would make this quantitative.
- **(S-3) as weighted-Lyapunov limit (sketch-level).** #deriv-critical-mass-composition's asymmetric limit $\alpha_2 \to 0$ under weighted Lyapunov $V_\mu(\xi) = \tfrac12(\lVert\delta_1\rVert^2 + \mu\lVert\delta_2\rVert^2)$ with $\mu \to 0$ formalizes (S-3): the endosymbiont's autonomous correction dynamics are weighted out of the joint stability argument, leaving the host's sector condition as the composite's persistence condition. This is a smooth deformation of the peer-coupling (CM4) inequality, not a discontinuous regime change — symbiogenesis and peer coupling are parameter-limits of the same weighted-Lyapunov analysis. The sketch is promotable to derived once (S-2) function transfer is formalized in this segment (the weighted Lyapunov limit does not address what happens to $M_h$ when structure from $M_e$ is inherited).
- **Reverse symbiogenesis.** Endosymbionts occasionally regain autonomy (biological examples: some organelle-hosted genes return to the nucleus; organizational examples: acquired divisions spun off). Theoretically: the scope condition can be crossed in either direction. A composite that loses $U_O$ dissolves back into a multi-agent system. The triggering conditions and typical dynamics are open.
- **Interaction with logogenic agents.** In LLM-based agent architectures, multiple models can compose through shared training or through interface-specified protocols. Whether this constitutes symbiogenesis (with one model dominating) or peer coupling depends on whether the component models retain independent objectives. Worth investigating in `03-llm-core/`.
- **Quantitative predictions.** When is symbiogenesis favored over peer coupling? Hypothesis: when the coordination overhead $C_{\text{coord}}$ between would-be peer-coupled agents exceeds the integration cost of symbiogenesis. Transaction-cost theory (Coase / Williamson) is the economic analog. The AAT version would connect $C_{\text{coord}}$ ( #der-tempo-composition) to the energetic or informational cost of maintaining separate objectives, with symbiogenesis favored when the latter exceeds the former.
- **Timescale of consolidation.** In biology, symbiogenesis takes evolutionary time (millions of years). In firms, months to years. In software/ideas, potentially much faster. The consolidation timescale $\tau_{\text{consolidated}}$ is domain-dependent; a general characterization is open.

- **Saddle-node bifurcation analysis — quantitative threshold form, conditional on a nonlinear coordination penalty.** Under the *hypothesis* that aggregate multi-agent mismatch $\delta$ obeys $\dot\delta = \rho_{\text{env}} - \alpha_{\text{auto}}\delta + k\delta^2$ with a nonlinear coordination penalty $+k\delta^2$ ($k \gt 0$) capturing compounding coordination failure between misaligned autonomous sub-agents, the steady-state fixed points $\delta^\ast = (\alpha_{\text{auto}} \pm \sqrt{\alpha_{\text{auto}}^2 - 4k\rho_{\text{env}}})/(2k)$ exist only for $\rho_{\text{env}} \le \rho_c := \alpha_{\text{auto}}^2/(4k)$. Above $\rho_c$ the two fixed points collide in a *saddle-node bifurcation* and disappear: $\dot\delta \gt 0$ everywhere, and the autonomous multi-agent system has no stable equilibrium. The symbiogenic escape route is structural: the composite merges sub-agent objectives and state ($\mu \to 0$), eliminating the coordination-penalty term and recovering linear dynamics on the merged state. The bifurcation analysis therefore predicts symbiogenesis as a *mathematically forced phase transition* at critical environmental volatility $\rho_c$ rather than as a contingent organizational choice. **Status: conditional on derivation of the $+k\delta^2$ coordination penalty from `#def-shared-intent`.** The $+k\delta^2$ form is currently stipulated rather than derived; making it rigorous requires showing that compounding coordination failure between agents with mismatch $\delta_A, \delta_B$ produces an aggregate-mismatch dynamics with this specific quadratic-in-$\delta$ structure under named conditions on the shared-intent quantity. Without that derivation, the threshold $\rho_c = \alpha_{\text{auto}}^2/(4k)$ is a *formulation*, not a theorem; with it, the threshold form is exact under the named hypothesis. The closed-negative result here — that the bifurcation derivation is conditional on a derivation step not yet attempted — is itself load-bearing: any future strengthening of `#hyp-symbiogenic-composition` from hypothesis-tier to derived-result-tier must produce the missing derivation of the coordination penalty from a more fundamental AAT construct (the natural candidate is shared-intent mutual information between sub-agent models $M_t^{(A)}$ and $M_t^{(B)}$ under coupled-evidence regimes).


---

### Source: `form-composition-closure.md`

```yaml
---
slug: form-composition-closure
type: formulation
status: conditional
depends:
  - post-composition-consistency
  - scope-composite-agent
  - scope-multi-agent
  - def-agent-environment
  - form-event-driven-dynamics
  - result-sector-condition-stability
  - deriv-sector-condition
  - result-sector-persistence-template
  - result-persistence-condition
stage: draft
---
```


# Formulation: Composition Closure Criterion

We define a group of interacting agents as a valid composite macro-agent when its closed-loop dynamics approximately commute with coarse-graining — that is, when projecting micro-states to macro-states and then running macro-dynamics yields approximately the same result as running micro-dynamics and then projecting.

## Formal Expression

Let a system consist of $N$ sub-agents interacting in a shared environment with state space $\mathcal S_{\text{env}}$. The micro-state, micro-observations, and micro-actions are:

$$X_{\text{micro}, t} = \{ (M_{i,t}, G_{i,t}) \}_{i=1}^N \in \mathcal X_{\text{micro}}$$

$$o_{\text{micro}, t} = \{ o_{i,t} \}_{i=1}^N \in \mathcal O_{\text{micro}}$$

$$a_{\text{micro}, t} = \{ a_{i,t} \}_{i=1}^N \in \mathcal A_{\text{micro}}$$

The coupled micro-dynamics form an action-observation loop:

$$X_{\text{micro}, t} \xrightarrow{\pi_{\text{micro}}} a_{\text{micro}, t} \xrightarrow{E} (\Omega_{t+1}, o_{\text{micro}, t+1}) \xrightarrow{f_{\text{micro}}} X_{\text{micro}, t+1}$$

We constrain our search to an admissible class of projections $\Lambda \in \mathcal P_{\text{adm}}$ mapping micro to macro, an admissible class of macro-dynamics $(\pi_c, E_c, f_c) \in \mathcal M_{\text{adm}}$, and a **timescale ratio** $K_c \geq 1$: the number of micro-timesteps per macro-step. Micro-time is indexed by $t \in \{0, \ldots, H\}$; macro-time by $m \in \{0, \ldots, \lfloor H/K_c \rfloor\}$ with macro-step $m$ corresponding to micro-timestep $t = m K_c$. The projection components then have type signatures:

- $\Lambda_x : \mathcal X_{\text{micro}} \to \mathcal X_c = (M_c, G_c)$ — pointwise, evaluated at macro-boundaries.
- $\Lambda_\Omega : \mathcal S_{\text{env}} \to \mathcal S_{\text{env}, c}$ — pointwise, evaluated at macro-boundaries.
- $\Lambda_o : \mathcal O_{\text{micro}}^{K_c} \to \mathcal O_c$ — aggregates the window of $K_c$ micro-observations between successive macro-boundaries.
- $\Lambda_a : \mathcal A_{\text{micro}}^{K_c} \to \mathcal A_c$ — aggregates the window of $K_c$ micro-actions similarly (used on the observation-comparison side; the macro-policy $\pi_c$ emits one macro-action per macro-step).

Aggregation is part of the projection specification — common choices are mean/sum (linear systems), first/last (event-rate projections), or task-specific sufficient statistics. When $K_c = 1$ the windows collapse, $\Lambda_o, \Lambda_a$ reduce to pointwise maps, and micro- and macro-tempos coincide (synchronous-update composites). When $K_c \gg 1$ the composite operates on the quasi-steady-state output of its sub-agents, the regime that #der-temporal-nesting asserts as the natural one for composition. $K_c$ is part of the problem specification; it does not appear in (A1)-(A4) or (P1)-(P3) below, but it determines at what granularity closure is measured.

Let $\mathcal D_{\text{micro}}$ be the distribution of reachable trajectories generated entirely by the true micro-system over horizon $H$, and let $o_{\text{micro}, (m-1)K_c : m K_c}$ denote the window of $K_c$ micro-observations $(o_{\text{micro}, (m-1)K_c + 1}, \ldots, o_{\text{micro}, m K_c})$ between macro-boundaries $m-1$ and $m$ (similarly for actions).

*[Definition (Composition Closure)]* We define the minimal achievable closure defect $\varepsilon^\ast$ over the admissible classes as:

$$ \varepsilon^\ast = \inf_{\Lambda \in \mathcal P_{\text{adm}},\, (\pi_c, E_c, f_c) \in \mathcal M_{\text{adm}}} \big\lVert (\varepsilon_x, \varepsilon_a, \varepsilon_o) \big\rVert $$

where the expected component errors evaluated over true micro-trajectories $\tau \sim \mathcal D_{\text{micro}}$, measured **per macro-step**, are:

- $\varepsilon_x = \mathbb E_\tau \Big[ \frac{1}{M_H} \sum_{m=1}^{M_H} \big\lVert \Lambda_x\big(X_{\text{micro},\, m K_c}\big) - f_c\big(\Lambda_x(X_{\text{micro},\, (m-1)K_c}),\; \Lambda_o(o_{\text{micro},\, (m-1)K_c : m K_c})\big) \big\rVert_\mathcal{X} \Big]$
- $\varepsilon_a = \mathbb E_\tau \Big[ \frac{1}{M_H} \sum_{m=1}^{M_H} \big\lVert \Lambda_a\big(a_{\text{micro},\, (m-1)K_c : m K_c}\big) - \pi_c\big(\Lambda_x(X_{\text{micro},\, (m-1)K_c})\big) \big\rVert_\mathcal{A} \Big]$
- $\varepsilon_o = \mathbb E_\tau \Big[ \frac{1}{M_H} \sum_{m=1}^{M_H} \big\lVert \Lambda_o\big(E_{\text{obs}}(\Omega,\, a_{\text{micro}})\big\vert_{(m-1)K_c : m K_c}\big) - E_{c,\text{obs}}\big(\Lambda_\Omega(\Omega_{(m-1)K_c}),\; \pi_c(\Lambda_x(X_{\text{micro},\, (m-1)K_c}))\big) \big\rVert_\mathcal{O} \Big]$

where $M_H = \lfloor H/K_c \rfloor$ is the number of macro-steps in horizon $H$, and $E_{\text{obs}}(\Omega, a_{\text{micro}})\big\vert_{(m-1)K_c : m K_c}$ denotes the window of micro-observations the environment produces across the macro-step.

**Units.** $\varepsilon_x, \varepsilon_a, \varepsilon_o$ carry units of distance — per-macro-step norm errors. Multiplied by the macro-update rate $\nu_c$ (units $[\text{time}^{-1}]$), they yield the disturbance-rate units $[\text{distance}]\cdot[\text{time}^{-1}]$ demanded by the sector-persistence template's $\rho_\xi$ ( #result-sector-persistence-template) and by the dimensional accounting in #der-tempo-composition. The previous per-micro-step formulation conflated $\varepsilon^\ast$'s granularity with $\nu_c$'s — the macro-step formulation resolves the unit inconsistency.

**$K_c = 1$ special case.** When micro and macro update in lockstep, $M_H = H$, the observation/action windows collapse, and the formulas reduce to the synchronous form. This is the regime of tightly-coupled groups (distributed algorithms running in phase, ensemble filters where every member steps per tick) and is where the two-Kalman worked example below operates.

**$K_c \gg 1$ case.** When the composite lives at a strictly slower timescale than its sub-agents (the regime #der-temporal-nesting asserts as natural), only micro-states at macro-boundaries enter $\varepsilon_x$, and macro-observations aggregate $K_c$ micro-observations. The closure defect then measures how well the macro-dynamics predicts the *next* macro-state from the *previous* macro-state and the aggregated micro-observation window — not any intermediate micro-state. Timescale abstraction is recovered: the composite's description need not — and under $K_c \gg 1$ should not — track the micro-trajectory between macro-boundaries.

The closure-defect framework applies to sets that satisfy #scope-composite-agent — i.e., that form composites via at least one of the three alignment routes (shared objective, hierarchical derivation, mutual benefit). Given scope-satisfaction, a set forms a *meaningful* composite agent — distinguished from a multi-agent system whose low-$\varepsilon^\ast$ projection is a happenstance of the environment rather than a reflection of composite coherence — when $\varepsilon^\ast \leq \varepsilon_{\text{max}}$. Without scope-satisfaction, the $\varepsilon^\ast$ infimum is still well-defined as a projection property, but the resulting "composite" has ill-defined purposeful substate $G_c = (O_c, \Sigma_c)$ and composition-level machinery (team persistence, composite tempo) does not apply.

### Admissibility constraints on macro-dynamics

*[Formulation (macro-dynamics-admissibility)]*

$\mathcal M_{\text{adm}}$ is the class of macro-dynamics $(\pi_c, E_c, f_c)$ satisfying:

**(A1) AAT agent structure.** The macro-state decomposes as $X_c = (M_c, G_c)$. The macro-update is recursive at macro-time $m$:

$$X_{c,m+1} = f_c(X_{c,m}, o_{c,m+1})$$

The macro-policy is state-dependent: $a_{c,m} = \pi_c(X_{c,m})$. This ensures the macro-agent has the same structural components as a single AAT agent ( #def-agent-environment, #der-recursive-update, #der-action-selection).

**(A2) Macro-mismatch.** A mismatch signal is well-defined:

$$\delta_{c,m} = o_{c,m} - \hat{o}_{c,m}(M_c, a_{c,m-1})$$

where $\hat o_{c,m}$ is the macro-model's prediction of the next macro-observation. This ensures the macro-agent can detect prediction errors — the foundation of adaptation ( #def-mismatch-signal).

**(A3) Macro-tempo.** The macro-update has well-defined adaptive tempo:

$$\mathcal T_c = \sum_k \nu_c^{(k)} \cdot \eta_c^{(k)\ast}$$

where $k$ indexes the macro-agent's observation channels, $\nu_c^{(k)}$ is the event rate, and $\eta_c^{(k)\ast}$ is the optimal gain ( #def-adaptive-tempo, #emp-update-gain). This ensures the persistence condition is formulable at the macro level.

**(A4) Bounded macro-correction.** The macro-correction function satisfies the sector condition ( #result-sector-condition-stability):

$$\delta_c^T F_c(\mathcal T_c, \delta_c) \geq \alpha_c \lVert \delta_c \rVert^2 \quad \text{for } \lVert \delta_c \rVert \leq R_c$$

with $\alpha_c \gt 0$ (positive correction rate) and $R_c \gt 0$ (finite reserve). This ensures the macro-agent's corrections work — they reduce mismatch rather than amplifying it, within the macro-model's capacity.

**What (A1)-(A4) prevent.** Without these constraints, the infimum over $\mathcal M_{\text{adm}}$ is trivially zero (any dynamical system can curve-fit micro-trajectories over a finite horizon). The constraints force the macro-dynamics to be a genuine AAT agent — with decomposed state, prediction errors, adaptive tempo, and stable correction — not an arbitrary function approximator. $\varepsilon^\ast$ then measures the irreducible cost of representing multiple agents as one AAT agent.

**What (A1)-(A4) do NOT require.** Directed separation ( #der-directed-separation) is not part of the admissibility constraints. It is an additional structural property that some composites have and others don't ( #hyp-directed-separation-under-composition). Results that depend on directed separation declare it as an additional assumption. Similarly, strategy structure ($G_c = (O_c, \Sigma_c)$ with a DAG) is not required — simpler goal representations are admissible.

### Admissibility constraints on projections

*[Definition (projection-admissibility, proposed from spike)]*

The admissible class of projections $\mathcal P_{\text{adm}}(\epsilon_I, L)$ consists of projections $\Lambda = (\Lambda_x, \Lambda_o, \Lambda_a, \Lambda_\Omega)$ satisfying three conditions:

**(P1) Information preservation.** The projection retains at least a fraction $(1 - \epsilon_I)$ of the predictive mutual information, evaluated across a macro-step:

$$I\big(\Lambda_x(X_{\text{micro},\, (m-1)K_c});\; \Lambda_o(o_{\text{micro},\, (m-1)K_c : m K_c}) \mid \Lambda_a(a_{\text{micro},\, (m-1)K_c : m K_c})\big) \geq (1 - \epsilon_I) \cdot I\big(X_{\text{micro},\, (m-1)K_c};\; o_{\text{micro},\, (m-1)K_c : m K_c} \mid a_{\text{micro},\, (m-1)K_c : m K_c}\big)$$

The left side is the predictive information the macro-state has about the next macro-observation (aggregated over the $K_c$-window), conditioned on the macro-action. The right side is the micro-state's predictive information about the *same* macro-observation, conditioned on the same aggregated actions — both sides share a common target so the ratio is well-defined. The parameter $\epsilon_I \in [0, 1)$ controls how much predictive power may be sacrificed by projection. This is the information bottleneck (Tishby et al. 1999) applied to the projection map. When $K_c = 1$, the windows collapse to singletons and (P1) reduces to the per-micro-step form previously stated.

**(P2) Lipschitz continuity.** Each component of $\Lambda$ is Lipschitz-continuous with constant $L$:

$$\lVert \Lambda_x(X) - \Lambda_x(X') \rVert_{\mathcal X_c} \leq L \cdot \lVert X - X' \rVert_{\mathcal X_{\text{micro}}} \quad \forall\, X, X' \in \mathcal X_{\text{micro}}$$

(and analogously for $\Lambda_o, \Lambda_a, \Lambda_\Omega$, each with its own Lipschitz constant). Without Lipschitz regularity, bounded closure defect does not imply bounded trajectory error — the bridge lemma requires this or something equivalent. When the projection is $L$-Lipschitz, the trajectory error bound becomes $L \cdot \varepsilon^\ast / \alpha_c$.

**(P3) Dimensionality reduction.** The macro-state space has strictly lower dimension than the micro-state space:

$$\dim(\mathcal X_c) \lt \dim(\mathcal X_{\text{micro}})$$

This prevents the trivial identity projection, which achieves $\varepsilon^\ast = 0$ but is not a genuine abstraction.

**Why three conditions.** No single condition suffices alone. (P1) prevents degenerate projections (a constant map $\Lambda_x = c$ has zero mutual information). (P2) prevents pathological projections (discontinuous maps that amplify micro-errors into unbounded macro-errors). (P3) prevents trivial projections (the identity map satisfies (P1) and (P2) but achieves nothing). Together they constrain $\mathcal P_{\text{adm}}$ to projections that are informative, regular, and genuinely reductive.

**The $(\epsilon_I, L)$ parameters are part of the problem specification, not derived quantities.** The natural choice for many applications is $L = 1$ (non-expansive projection) and $\epsilon_I$ chosen as the minimum information loss compatible with genuine dimensionality reduction.

**Independence from (A1)-(A4).** The macro-dynamics admissibility (A1)-(A4) partially constrains the projection — (A1) requires $\Lambda_x$ to preserve the $M_c / G_c$ decomposition, and (A4) implicitly requires regularity through the sector condition. But (A1)-(A4) do not specify how much predictive information the projection must retain. A macro-agent with a very coarse projection can satisfy (A1)-(A4) while being a poor representation of the micro-system. The information-preservation condition (P1) fills this gap. See `spikes/spike-projection-admissibility.md` §5 for the full independence analysis.

### Bridge lemma: closure defect to trajectory error

*[Derived (bridge-lemma, from sector-persistence-template + A4 + contraction assumption)]*

The bridge lemma is the sector-persistence template ( #result-sector-persistence-template) applied with state variable $\xi = e_m = X_{c,m} - \Lambda_x(X_{\text{micro},\, m K_c})$ (trajectory error at macro-boundaries, between macro-evolved state and projected micro-state) and effective disturbance rate $\rho_\xi = \varepsilon^\ast \nu_c$ (closure defect per macro-step, multiplied by macro-update rate). The units are consistent by construction of the macro-step formulation above: $\varepsilon^\ast$ is per-macro-step (distance) and $\nu_c$ is macro-step rate ($[\text{time}^{-1}]$), so $\rho_\xi$ has the disturbance-rate units the template requires. The template yields directly:

$$\limsup_{m \to \infty} \lVert e_m \rVert \leq \frac{\varepsilon^\ast \nu_c}{\alpha_c}$$

This bound fits within the composite's sector-condition region iff $\varepsilon^\ast \lt \alpha_c R_c / \nu_c$, which is the persistence condition applied to the closure-error rate: if it fails, the macro-description diverges from micro-reality.

**What the bridge lemma adds beyond the template.** The template's precondition (T2) is the one-point sector bound. For the trajectory-error instantiation, the bound propagation requires a *strictly stronger* condition: the macro-update map $f_c(\cdot, o)$ must be contracting in its state argument (**incremental sector bound**, DA2'-inc — strong monotonicity of $F_c$), not merely one-point sector-bounded at each state. The per-step contraction factor is $\lambda = 1 - \alpha_c/\nu_c \lt 1$ (automatic when $\alpha_c \lt \nu_c$, true for any realistic agent that doesn't fully correct in a single step). This stronger condition is where the tier structure enters; see Epistemic Status for the Tier 1/2/3 taxonomy.

**The sector condition (A4) does double duty — conditionally.** (A4) ensures the macro-agent corrects external mismatch (single-agent persistence) AND — under the incremental sector bound — that the macro-description tracks micro-reality (this bridge). Both are instances of the same template applied to different state variables with different effective disturbance rates.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Closure-defect quantity $\varepsilon^\ast$ as infimum over admissible classes | Definition built from (A1)-(A4), (P1)-(P3), and $K_c$ | Formulation choice |
| Three-component decomposition into $\varepsilon_x, \varepsilon_a, \varepsilon_o$ | Match to the three arrows of the action-observation loop (state, action, observation) | Formulation choice |
| Per-macro-step formulation; $\varepsilon^\ast$ has units of distance-per-macro-step | 2026-04-22 temporal coarse-graining repair (Finding A); forced by dimensional consistency with $\rho_\xi = \varepsilon^\ast \nu_c$ in #result-sector-persistence-template and #der-tempo-composition | Derived (dimensional consistency) |
| Timescale ratio $K_c \geq 1$ as independent problem-specification parameter | Application-specific; $K_c = 1$ (synchronous) and $K_c \gg 1$ ( #der-temporal-nesting regime) both admissible | Formulation choice |
| (A1) Macro AAT structure $X_c = (M_c, G_c)$ with recursive update | Import from #def-agent-environment + #der-recursive-update + #der-action-selection | Formulation choice (requirement) |
| (A2) Well-defined macro-mismatch | Import from #def-mismatch-signal | Formulation choice (requirement) |
| (A3) Well-defined macro-tempo | Import from #def-adaptive-tempo + #emp-update-gain | Formulation choice (requirement) |
| (A4) Sector-bounded macro-correction | Import from #result-sector-condition-stability | Formulation choice (requirement) |
| (A1)-(A4) as a requirement *set* render the infimum non-trivial (exclude curve-fitting macro-dynamics) | Consequence of restricting $\mathcal M_{\text{adm}}$ to genuine AAT agents | Derived (under the chosen requirement set) |
| (P1) Information-preservation constraint | IB Lagrangian-dual with source $X_{\text{micro}}$, relevance $o_{\text{micro}, t+1}$; formally connects to #disc-compression-operations | Formulation choice (requirement) |
| (P2) Lipschitz continuity of $\Lambda$ | Required for bridge-lemma trajectory-error bound (without it, bounded $\varepsilon^\ast$ does not imply bounded trajectory error) | Formulation choice (requirement) |
| (P3) Strict dimensionality reduction | Rules out identity projection (which trivially achieves $\varepsilon^\ast = 0$ but is not abstraction) | Formulation choice (requirement) |
| (P1)-(P3) independent of (A1)-(A4) | Spike analysis (`spikes/spike-projection-admissibility.md` §5) — (A1) and (A4) constrain $\Lambda_x$ partially but do not fix information-preservation level | Derived |
| Bridge lemma: $\limsup \lVert e_m \rVert \leq \varepsilon^\ast \nu_c / \alpha_c$ | Sector-persistence template ( #result-sector-persistence-template) applied with state $\xi = e_m$, disturbance rate $\rho_\xi = \varepsilon^\ast \nu_c$ | Derived (conditional on incremental sector bound DA2'a-inc) |
| Persistence-as-closure-boundedness condition $\varepsilon^\ast \lt \alpha_c R_c / \nu_c$ | Sector-condition region fits the asymptotic error ball | Derived (under A4 + DA2'a-inc) |
| Incremental sector bound (DA2'a-inc) is strictly stronger than (A4)'s one-point sector bound | Counterexample exhibited (oscillatory globally-inward, locally non-monotone corrections); `spikes/spike-bridge-lemma-contraction.md` §4.1 | Proved |
| Three-tier agent classification (Tier 1 / 2 / 3) for bridge-lemma applicability | Taxonomy induced by whether DA2'a-inc holds globally (T1), locally (T2), or must be verified per-domain (T3) | Formulation choice (classification) |
| Tier 1: bridge lemma derived for Bayesian updaters on exponential families, gradient descent on strongly convex losses, linear correction with positive-definite gain-observation product | Standard monotone-operator / Kalman analysis; `spikes/spike-bridge-lemma-contraction.md` | Derived (conditional on DA2'a-inc + linear prediction, i.e., C2) |
| Tier 2: local contraction with factor degraded by $\kappa(D\hat o)^2$ | Extended-Kalman / locally-convex analysis | Derived (local) |
| Tier 3: contraction must be verified per-domain | No general result available for non-convex / discontinuous / non-mismatch-driven components | Discussion-grade |
| Composite (A4) from sub-agent properties: $\alpha_c \geq \min_i(\alpha_i - \Delta \mathcal T_i^{\text{cost}})$, $R_c \leq \min_i R_i$ | Weakest-link bound; `msc/working-composition-admissibility.md` §6.2 | Derived (conditional on bounded coordination cost per #der-team-persistence) |
| Composite critical-mass inequality $(\alpha - C)R \gt \rho + \gamma\mathcal T$ (symmetric-matched-Tier-1) — sign-sensitive refinement of the weakest-link bound; recovers #der-team-persistence (cooperative) and #der-adversarial-destabilization (adversarial) as signed special cases | #deriv-critical-mass-composition | Derived (conditional on Tier 1 + matched-symmetric + Model D + coupling model C1/C2) |
| Composite persistence as (contraction) ∧ (scope-satisfaction): $\kappa_c(U_O) \gt 0 \wedge$ #scope-composite-agent | #deriv-critical-mass-composition (CM4); $U_O$ enters multiplicatively on $\gamma$ plus scope-gate, not additively | Derived (with (UO-mult) discussion-grade) |
| Asymmetric-limit connection to #hyp-symbiogenic-composition (S-3) autonomy reduction | #deriv-critical-mass-composition §asymmetric-limit; weighted Lyapunov $V_\mu$ with $\mu \to 0$ | Sketch (S-2 function transfer not yet formalized; promotable when #hyp-symbiogenic-composition closes (S-2)) |
| Meta-machine exact composition ($\varepsilon^\ast = 0$) for finite-state Moore machines | Miller 2022 §3.3; product automaton is the micro-dynamics by construction | Derived (external theorem) |
| Two-Kalman instantiation: $\varepsilon^\ast = 0$ at all $\rho_{\text{corr}}$ for the means-only projection at steady state | Analytic steady-state calculation; `spikes/spike-composition-correlated-kalman.md` | Proved (closed form) |
| $\varepsilon_x$ depends on both sub-agent unity *and* update-rule heterogeneity ($\Delta K$) | Heterogeneous-gain Kalman case; #result-unity-closure-mapping | Derived (specific closed form for the two-Kalman case) |
| Mahalanobis norm as natural choice for estimation-type agents | Two-Kalman verification; Kalman gain minimizes expected squared Mahalanobis distance | Formulation choice (canonical for estimation; general-domain norm specification open) |
| $N$-agent scaling of $\varepsilon^\ast$ | The "polynomial vs. exponential" framing is mis-typed (a per-step residue asked an accumulation question); `spikes/spike-composition-scaling-N.md`, CHANGELOG 2026-05-19 | Re-typed / resolved: $\varepsilon^\ast(N)$ is dimension-free-zero in the benign linear-Gaussian-stationary regime (all $N$, all coupling), graph-Laplacian-bounded with **no exponential regime** under compression (the consensus operator `#deriv-critical-mass-composition` already names), and order-incompatibility-invariant ($\leq\lvert S\rvert\log 2$, $N$-free) for strategy-DAG composition. No exponential regime exists. Full statement: the next two rows + Discussion |
| Computability of (P1) for nonlinear / non-Gaussian systems | Requires Monte Carlo or variational bounds; closed-form only for linear-Gaussian | Open |
| Principled setting of the $\epsilon_I$ threshold | No formal criterion currently; candidate tying to team size and coupling structure | Open |
| Strategy-DAG projection under $\Lambda_x$ | Causal-$\tau$-abstraction frame; #def-strategy-dag §"Composing heterogeneous strategy DAGs" (topology / SCC-condensation), #result-unity-closure-mapping (fixed-topology credence instance); CHANGELOG 2026-05-19 | Resolved (*conditional*; one named sub-open Q1): the right object is a causal-$\tau$-abstraction; exact $\Sigma_c$ iff shared sub-orders jointly acyclic + AND/OR-compatible, else the minimal admissible $\Sigma_c$ is the SCC-condensation with defect $\sum_{\lvert C\rvert\gt1}\mathrm{TC}(C)\leq\lvert S\rvert\log 2$ — **bounded by shared-plan size, $N$-free**. Beckers–Eberhardt–Halpern $(\tau,\epsilon)$-abstraction $\Rightarrow$ bounded $\varepsilon_\Sigma$ (the *frame*, not term-for-term; the high-level distance remains AAT's to choose). Q1 (constant-tightness for non-deterministic intra-SCC coupling) is a named sub-open, not a reopening |
| Mori-Zwanzig zero-lag bound $\varepsilon^\ast \geq \lVert Q_\Lambda U P_\Lambda \rVert_{\text{op}}$ | Koopman/MZ projection (stationary coordinate-compatible case) | Derived (conditional on stationarity) |
| Full-kernel MZ bound on $\varepsilon^\ast$ | Type mismatch (trajectory-accumulation vs. per-step) | Refuted at the $\varepsilon^\ast$-level; natural home is the bridge-lemma trajectory-error bound |

The dividing line: (A1)-(A4) and (P1)-(P3) are *formulation choices of the requirement set* — alternative requirement sets are possible (e.g., entropy-preservation instead of MI-preservation; contraction bound in place of Lipschitz), and this one is chosen for parsimony, direct import from prior AAT segments, and downstream tractability. The *consequences* that follow under this requirement set — the non-triviality of the infimum, the bridge-lemma bound, the weakest-link composite-(A4) derivation, the two-Kalman $\varepsilon^\ast = 0$ result — are Derived, with bridge-lemma-level results carrying the additional DA2'a-inc condition (which is proved strictly stronger than (A4) alone). The Tier 1/2/3 classification is itself a formulation, but the per-tier results are derived under tier-specific conditions. The genuinely-open questions are now the computability / principled-setting questions for (P1) and $\epsilon_I$. The $N$-agent-scaling and strategy-DAG-projection rows are **resolved** (re-typed; the "poly-vs-exp" / "domain-specific-unresolved" framings were mis-typed — see the two rows above and CHANGELOG 2026-05-19); the prior claim that $N$-scaling "decides whether very large teams are representable as single AAT agents at all" is **withdrawn** — it was the dissolved mis-frame, not a live open question. There is no exponential-in-$N$ regime.

## Epistemic Status

*Conditional.* Max attainable: conditional (formulation choice).

The closure defect $\varepsilon^\ast$ is well-defined given (A1)-(A4), (P1)-(P3), the timescale ratio $K_c$, and specified norms. The macro-dynamics admissibility (A1)-(A4) and the projection admissibility (P1)-(P3) are independent formulation choices — (A1)-(A4) specify what "AAT-shaped macro-dynamics" means; (P1)-(P3) specify what "informative, regular, genuinely reductive projections" means. Both are needed for $\varepsilon^\ast$ to be an infimum over a non-trivial, non-degenerate class. The timescale ratio $K_c \geq 1$ is a third, independent piece of problem specification: it sets the granularity at which closure is measured and the type signatures of $\Lambda_o, \Lambda_a$. $K_c$ does not constrain the macro-dynamics class and is not derived — it is chosen from the timescale separation of the application (per #der-temporal-nesting). Both $K_c = 1$ (tightly-coupled composites) and $K_c \gg 1$ (hierarchically composed composites on their own timescale) are admissible. The projection admissibility conditions have a proposed definition with one exact instantiation (two-Kalman case at $K_c = 1$, `spikes/spike-projection-admissibility.md`); general-case computability of (P1) and the dependence of $\varepsilon^\ast$ on $K_c$ for a fixed application remain open.

The bridge lemma is *conditional* — not fully derived from (A4) alone. The precise additional condition is the **incremental sector bound** (DA2'a-inc): the correction function $F_d$ must be *strongly monotone* ($\langle \delta - \delta', F_d(\delta) - F_d(\delta') \rangle \geq c_{\min} \lVert \delta - \delta' \rVert^2$ for all pairs), not just satisfy the one-point sector bound. This is strictly stronger than (A4) — a counterexample exists: oscillatory corrections that are globally inward-pointing but locally non-monotone (`spikes/spike-bridge-lemma-contraction.md`, §4.1). Three tiers of agents result:

- **Tier 1 (contraction proved):** Kalman filters, exponential-family Bayesian updaters, gradient descent on strongly convex losses, all linear corrections with positive definite gain-observation product. For these agents the bridge lemma is *derived* from (A4) + DA2'a-inc + linear prediction (C2), with contraction factor $\lambda_{\text{eff}}$ from #deriv-discrete-sector-condition.
- **Tier 2 (local contraction):** Extended Kalman, locally convex gradients, nonlinear prediction models. Contraction holds locally with factor degraded by $\kappa(D\hat{o})^2$.
- **Tier 3 (independent verification):** Non-convex optimization, discontinuous/rule-based corrections, agents with non-mismatch-driven state components. Contraction must be verified per-domain.

The discrete-time recurrence argument itself is standard (Elaydi 2005); the contribution is identifying the incremental sector bound as the precise condition that bridges sector-bounded correction to full-update-map contraction. Full derivation: `spikes/spike-bridge-lemma-contraction.md`.

The norm choices ($\lVert\cdot\rVert_\mathcal{X}$, $\lVert\cdot\rVert_\mathcal{A}$, $\lVert\cdot\rVert_\mathcal{O}$, and the combination norm) are load-bearing. For estimation-type agents, the Mahalanobis norm (weighted by inverse prediction-error covariance) is the natural choice — verified exactly in the two-Kalman case. For general domains, norm specification remains open.

## Discussion

This criterion replaces intuitive questions about "where the boundary of an agent is" with a functional test: does a macroscopic AAT description preserve the underlying micro-dynamics well enough to remain predictive and capable? The core requirement is an **approximate dynamical homomorphism** — the macro-dynamics approximately commute with the projection.

**Relationship to #post-composition-consistency.** The Section I postulate requires that AAT's machinery be scale-invariant — predictions at different levels of description must be compatible. This segment operationalizes "compatible" as "bounded closure defect under admissible coarse-graining." The admissibility constraints ensure the macro-description is genuinely AAT-shaped, so the same persistence condition, the same tempo framework, and the same mismatch dynamics apply at the macro level with macro-level parameters.

**Projection-behaviour facet of the stability certificate ( #disc-stability-certificate).** Coarse-graining is a non-invertible projection of the certificate ( #result-certificate-existence): the certificate-as-metric survives (the Schur complement of a positive-definite form is positive-definite) but the *dynamic* guarantee does not — the closure defect $\varepsilon^\ast$ is the certificate's projection-residue, equal to the Mori–Zwanzig zero-lag memory-commitator norm (derivation table above), zero exactly when the resolved subspace is invariant. Read through the spine, this is the question "does the agent's measuring-stick survive being viewed coarsely": its shape survives, its guarantee leaks by exactly the memory term. The composition-level identifiability floor (no common certificate across sub-agents; Liberzon, #disc-identifiability-floor Instance 3) is this same residue read as a boundary event — a *distinct* obstruction from the rank-collapse floors (a non-invertible projection, not a congruence), which is why the cross-sectional structure is several meta-patterns and not one.

**The Jacobian-level observation.** The incremental sector bound (DA2'-inc) used to prove the bridge lemma is mathematically equivalent to the contraction-metric condition (CT2) evaluated at the identity metric $M = I$, for continuously differentiable ($C^1$) correction functions $F$ on convex domains. This equivalence (cf. Rockafellar & Wets 1998) means that AAT's bridge lemma is a specialized application of generalized contraction theory. See `#result-contraction-template` for the full lifting of this condition to arbitrary Riemannian metrics.

**Topology-indexed composition closures (via #result-contraction-template).** `#result-contraction-template` lifts the bridge-lemma's DA2'-inc condition into the contraction-metric framework of Lohmiller & Slotine 1998. Under its (CT1)–(CT3) preconditions, three topology-indexed closure results apply:

- **Parallel composition** preserves contraction under blockdiag metric at rate $\min(\lambda_1, \lambda_2)$ — recovers this segment's weakest-link bound.
- **Cascade composition** ($\dot x_1 = f_1(x_1)$, $\dot x_2 = f_2(x_1, x_2)$) preserves contraction under lower-triangular weighted metric at rate bounded by $\min(\lambda_1, \lambda_2)$ up to coupling-gain adjustment (Slotine 2003 Thm 2). Handles hierarchical agent structures.
- **Negative feedback with bounded loop gain** (Slotine 2003 Thm 3) gives the heterogeneous critical-mass inequality $(\lambda_1 - C_1)(\lambda_2 - C_2) \gt k_{12} k_{21}/4$ via (CM2-M) in #result-contraction-template — extending #deriv-critical-mass-composition's matched-symmetric (CM2) to heterogeneous sub-agents with different architectures and coupling strengths.

The Tier 1/2/3 bridge-lemma taxonomy of this segment maps cleanly to Tier 1M/2M/3M under #result-contraction-template (globally metric-contracting / locally metric-contracting / no globally valid metric). The observation that (CT2) at $M = I$ is *equivalent* to DA2'-inc means this segment has been carrying the Jacobian-level Euclidean contraction condition at the composite level all along; #result-contraction-template surfaces this at the single-agent level and adds the compositional theorems that generalize this segment's closure content beyond the matched-symmetric case.

**DA2'-inc ≡ (CT2) at $M = I$ — structural-transparency equivalence.** *[Derived, status: exact.]* For $C^1$ correction functions $F$ on convex domains, the following three conditions are equivalent (standard monotone-operator theory; Rockafellar & Wets 1998 *Variational Analysis* Corollary 12.4; Nesterov 2004 *Introductory Lectures on Convex Optimization* §2.1.3 Theorem 2.1.9 — strong monotonicity ⇔ symmetric-part of Jacobian uniformly positive-definite):

(a) DA2'-inc (strong monotonicity): $(\delta - \delta')^\top (F(\delta) - F(\delta')) \geq c \lVert \delta - \delta'\rVert^2$ for all $\delta, \delta'$.

(b) Jacobian-symmetric-part PD: $(\partial F/\partial\delta)_{\mathrm{sym}} \succeq c I$ pointwise on the domain.

(c) (CT2) at $M = I$ with $\lambda = c$: $-\partial F/\partial\delta - (\partial F/\partial\delta)^\top \preceq -2\lambda I$.

*Derivation.* (a) → (b): take $\delta' \to \delta$ along direction $v$, divide by $\lVert \delta - \delta'\rVert^2$, take the limit. (b) → (a): integrate $v^\top(\partial F/\partial\delta)_{\mathrm{sym}} v \geq c \lVert v\rVert^2$ along the segment from $\delta'$ to $\delta$. (b) ↔ (c): direct algebraic identity.

**Implication for AAT-internal derivability.** Under this equivalence, the Euclidean sub-scope metric-$\alpha_1$ cases of `#result-contraction-template` (Kalman-scalar, Euclidean strongly-convex-gradient, L2-regularized, linear-PD-symmetric) are AAT-internally derived from the DA2'-inc commitment already carried at the composite level — no new axiom required. What the (CT2)-at-$M=I$ framing adds is *visibility*: the Jacobian-level condition was implicit under the DA2'-inc name; surfacing the equivalence converts the Euclidean sub-scope from "theorem-imported from Lohmiller-Slotine" to "AAT-internally derived via a standard monotone-operator identity." This is structural transparency, not new content. Non-Euclidean metric-$\alpha_2$ cases (Fisher, Hessian, Lyapunov-metric) remain separately treated in `#result-contraction-template` — the equivalence is specific to $M = I$.

**The sector condition does double duty — conditionally.** (A4) ensures the macro-agent's corrections work (structural persistence), AND — given the additional contraction assumption (see Epistemic Status) — it ensures the macro-description tracks micro-reality (bridge lemma). Both uses address *structural persistence* in the sense of `LEXICON.md` — the capacity of the correction machinery, not the current operating point or the composite's identity through time. The central insight is that structural persistence of the composite and faithfulness to its constituents are related through the same mechanism — contracting correction dynamics under bounded perturbation — but the bridge from sector-bounded correction to full-update-map contraction requires an assumption beyond (A4) that has been verified for estimation-type agents (Kalman) and remains open for general agents. When this assumption holds, the composite that persists in its own right also persists as a faithful representation of its constituents.

**Deriving composite (A4) from sub-agent properties.** If each sub-agent satisfies the sector condition with parameters $(\alpha_i, R_i)$, and coordination costs are bounded by $\Delta\mathcal T_i^{\text{cost}}$ per agent ( #der-team-persistence), then the composite satisfies (A4) with:

$$\alpha_c \geq \min_i (\alpha_i - \Delta\mathcal T_i^{\text{cost}})$$

$$R_c \leq \min_i R_i$$

This is a weakest-link bound (conservative but clean). Cooperative coupling ( #der-team-persistence) can improve $\alpha_c$ beyond this bound by reducing effective disturbance. The key implication: (A4) is *verifiable* from micro-level properties — compute each sub-agent's sector-condition parameters, estimate coordination costs, and check whether the composite has positive correction rate. No need to compute $f_c$ directly. See `msc/working-composition-admissibility.md` §6.2 for the derivation.

**Sign-sensitive refinement (derived).** The sign-blind weakest-link bound is subsumed by #deriv-critical-mass-composition's closed-form inequality $(\alpha - C)R \gt \rho + \gamma\mathcal T$ (CM2) in the matched-symmetric-Tier-1 case, where the right-hand side makes the effective disturbance explicit and the sign of the coupling $\gamma$ (cooperative $\gamma \lt 0$ vs adversarial $\gamma \gt 0$) enters directly. (CM2) can yield composite persistence even when the weakest-link bound alone fails — when cooperative coupling reduces $\rho + \gamma\mathcal T$ below what the raw $\alpha - C$ margin would permit. #der-team-persistence (cooperative) and #der-adversarial-destabilization (adversarial) are recovered as signed special cases. The honest composite-persistence statement is the conjunction of contraction (CM3) **and** scope-satisfaction ( #scope-composite-agent) — (CM4) — making explicit that composite persistence can fail in two qualitatively different ways: the composite fails to contract, or the composite was never a composite. The asymmetric-parameter limit $\alpha_2 \to 0$ via weighted Lyapunov $V_\mu$ formalizes #hyp-symbiogenic-composition's (S-3) autonomy-reduction mechanism as a smooth deformation of (CM4), not a discontinuous regime change.

**Connection to team-persistence.** #der-team-persistence derives persistence conditions for sub-agents in a cooperative-adversarial network. This segment provides the macro-level complement: the conditions under which the composite itself is a valid AAT agent. Together they close the loop: sub-agents persist individually (team-persistence) AND the composite is a meaningful macro-agent (composition closure with admissibility).

**Constructive (A1)–(A4) via wrapping.** The wrapping construction in `#der-class-coercion-via-wrapping` is a special-case instantiation where (A1)–(A4) hold *by construction* through the wrapper's type signatures rather than by post-hoc verification of an admissible projection $\Lambda$. The wrapper builds explicit $X_W = (M_W, G_W)$ with belief-update and strategy-update maps that have specified type signatures; (A1) is automatic; (A2)–(A4) follow from wrapper-design constraints (commit to a prediction map; choose $f_M$ from the Tier-1 belief-update class). The closure-defect $\varepsilon^\ast$ in this special case has a different reading than the standard fidelity reading — the wrapper *deliberately* changes the underlying component's behavior to enforce structural separation. Two distinct $\varepsilon^\ast$ quantities appear in wrapper analyses: $\varepsilon^\ast_{\text{track}}$ (the standard fidelity quantity defined here, used in the bridge lemma) and $\varepsilon^\ast_{\text{coerce}}$ (the wrapper-vs-component behavioral divergence, distinct from $\varepsilon^\ast_{\text{track}}$ and not bounded by the bridge lemma). See `#der-class-coercion-via-wrapping` Discussion for the disambiguation.

**Meta-machine: exact composition for finite automata (Miller 2022).** When agents are finite-state automata (Moore machines), composition is *exact*: two machines with state sets $S_1$, $S_2$ interacting through their output/input channels form a **meta-machine** (Miller 2022, *Ex Machina*, §3.3) — itself a Moore machine with state set $S_1 \times S_2$, deterministic transitions (each machine's output determines the other's input), and a single starting state from the constituent starting states. The closure defect $\varepsilon^\ast = 0$ trivially, because the product automaton *is* the micro-dynamics — there is no approximation. The meta-machine always falls into a cycle (finite states with deterministic transitions must eventually revisit a state), so two interacting automata produce an eventually-periodic joint behavior. The composition-closure framework becomes interesting when we ask for a *compressed* macro-description: can a smaller automaton (fewer than $\lvert S_1\rvert \times \lvert S_2\rvert$ states) approximate the meta-machine? This is where $\varepsilon^\ast \gt 0$ and the admissibility constraints become non-trivial — (P3) requires genuine dimensionality reduction, and (P1) asks how much predictive information the compression preserves. Machine minimization (the theorem that every automaton has a unique minimized equivalent; Hopcroft et al. 2006) is a natural candidate for the optimal projection: the minimized meta-machine has the fewest states that reproduce the full joint behavior, achieving $\varepsilon^\ast = 0$ with (P3) satisfied whenever the minimized machine is smaller than the product. See #worked-example-cam (planned) for the full instantiation.

**Two-Kalman instantiation.** The simplest nontrivial worked case: two Kalman filters tracking correlated scalar random walks with correlation $\rho_{\text{corr}}$, no communication. This case sits at $K_c = 1$ — both sub-agents and the composite step together — so the macro-step formulation reduces to the pointwise form; the $\Lambda_o$ aggregation is the identity. The natural projection keeps the state estimates and discards the covariance states (means-only projection, dimension 2 from micro-dimension 4). At steady state, the closure defect is exactly $\varepsilon^\ast = 0$ for **all** values of $\rho_{\text{corr}}$ — the means-only projection perfectly represents the micro-dynamics because the Kalman gains converge to constants and the discarded covariance state carries no information. The "cost of independence" (the estimation performance lost by not exploiting cross-correlations) is a **performance gap** $\Delta_{\text{perf}} \approx 2\rho_{\text{corr}}^2 q^2 r / (S^\ast)^2$ (quadratic in $\rho_{\text{corr}}$ for small correlations), not a closure defect — it measures suboptimality relative to a joint filter, not failure to track the micro-dynamics. The composition-closure framework diagnoses representability ("is this group a coherent AAT agent?"), not optimality ("is this group as good as a centralized agent?"). See `spikes/spike-composition-correlated-kalman.md` for the full derivation, (A1)-(A4) verification, and the first genuine $\varepsilon^\ast \gt 0$ case (purposeful agents with Beta-Bernoulli strategy updates). All three (P1)-(P3) conditions are verified exactly: $\epsilon_I = 0$ (no information loss at steady state, since the discarded covariance state is constant), $L = 1$ (the projection is a coordinate map), and $\dim(\mathcal X_c) = 2 \lt 4 = \dim(\mathcal X_{\text{micro}})$.

**Norm specification for estimation-type agents.** The two-Kalman case identifies the Mahalanobis norm as the natural choice for agents whose primary function is state estimation. The state norm weights by the inverse prediction-error covariance: $\lVert X_c - X_c' \rVert^2 = (\hat\omega_c - \hat\omega_c')^T (P_{\text{pred}}^\ast)^{-1} (\hat\omega_c - \hat\omega_c')$. The observation norm weights by the inverse innovation covariance $S^{-1} = (P_{\text{pred}}^\ast + R)^{-1}$. The general principle: norms should weight by inverse uncertainty, so that differences in well-estimated components count more than differences in poorly-estimated ones. This is the norm the Kalman filter implicitly uses — the Kalman gain minimizes the expected squared Mahalanobis distance from truth. For domains without a natural covariance structure (discrete states, non-Gaussian models), the Euclidean norm remains the default. See `spikes/spike-projection-admissibility.md` §4 for derivation and §4.5 for the general-case pattern.

## Findings

### Composition-Closure Defect and Bridge Lemma

**Brief:** When does a group of interacting agents legitimately count as one larger agent? The closure-defect $\varepsilon^\ast$ is the minimum residual prediction error from collapsing the micro-system into an AAT-shaped macro-description, taken over admissible coarse-grainings. The bridge lemma converts this prediction-level error into a trajectory-level guarantee: under sector-bounded macro-correction plus strong monotonicity of the macro-update, the macro-description tracks micro-reality with bounded asymptotic error $\varepsilon^\ast \nu_c / \alpha_c$. Composition is therefore not asserted by interface or by intuition — it is certified by an inequality, with explicit failure modes on both sides (the macro-dynamics fail to be AAT-shaped; the projection fails to be informative-and-regular; the macro-correction is not strongly monotone).

**Impact:** Closes the gap that Markov-blanket and active-inference accounts of nested agency leave open: those accounts give a statistical / thermodynamic boundary criterion but no control-theoretic loss bound on treating a collection as one agent. The closure-defect framework supplies the bound, attaches it to AAT's existing sector-condition machinery, and routes Section I and Section II results across composite boundaries on Tier-1-classified sub-agents. Downstream this lets `#deriv-critical-mass-composition` derive the composite sector constant from sub-agent parameters in closed form, lets `#der-tempo-composition` give Brooks's Law a formal expression in tempo units, and supplies the escape route (b) for `#disc-identifiability-floor` Instance 3. The criterion also draws an honest scope line: $\varepsilon^\ast = 0$ does not mean optimality (two non-communicating Kalman filters achieve $\varepsilon^\ast = 0$ while being suboptimal versus a joint filter); the framework diagnoses representability, not optimality.

**Novelty Claim:** *Claim differentiation* on bounded-loss composition as agent-boundary criterion. The bridge-lemma form is mathematically continuous with the approximate-information-state and influence-based-abstraction lines (Subramanian 2020; Congeduti 2020; Abel 2016; Taylor 2008), which prove approximation-loss results for compressed control under coarse-graining or aggregation. The differentiation is the *use* of such a bound as a criterion for when a multi-agent system can be re-described as a single agent — not as a control-policy compression result on a fixed agent — combined with explicit admissibility conditions (A1)-(A4) on the macro-dynamics that force the macro-description to itself be AAT-shaped, ruling out trivial curve-fits.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| Statistical / thermodynamic boundary of a nested agent | Parr, da Costa & Friston 2019, "Markov blankets, information geometry and stochastic thermodynamics" *Phil. Trans. R. Soc. A* 378 (published 2019, found via Undermind 2026-04 Pillar 2) | *conceptual precursor* — supplies the boundary-and-nesting intuition; does not provide a coarse-graining error bound, a coordination-overhead theorem, or a strong-monotonicity condition for valid macro-agent treatment |
| Hierarchical-blanket nested agency with temporal depth | Kirchhoff, Parr, Palacios, Friston & Kiverstein 2018, "The Markov blankets of life" *J. R. Soc. Interface* 15 (published 2018, found 2026-04) | *conceptual precursor* — invokes synergetic ordering and self-organization at the compositional step but remains conceptual; no theorem bounding predictive loss of coarse-graining |
| Bound on control loss from compressed history | Subramanian, Sinha, Seraj & Mahajan 2020, "Approximate information state for approximate planning and reinforcement learning in partially observed systems" *arXiv:2010.08843* (published 2020, found 2026-04) | *closest mathematical neighbor* — proves a bound from predictive-compression error to control error in the same shape as the bridge lemma. ASF reuses the predictive-compression-to-control-loss mechanism and applies it at the coarser granularity of *agent boundary formation*, not single-agent state compression |
| Loss bound from approximate influence-based abstraction | Congeduti, Mey & Oliehoek 2020, "Loss Bounds for Approximate Influence-Based Abstraction" *arXiv:2011.01788* (published 2020, found 2026-04) | *closest mathematical neighbor* — closer than the Markov-blanket line to coordination-overhead mathematics. ASF differs in framing: Congeduti bounds policy-value loss under approximate cross-agent influence; the bridge lemma bounds *macro-state trajectory error* under coarse-graining |
| Near-optimality under state aggregation | Abel, Hershkowitz & Littman 2016, "Near Optimal Behavior via Approximate State Abstraction" *ICML*; Taylor, Precup & Panangaden 2008, "Bounding Performance Loss in Approximate MDP Homomorphisms" *NeurIPS* (published 2016/2008, found 2026-04) | *adjacent literature* — single-agent MDP framing with aggregation bounds; same loss-from-coarse-graining mechanism, not framed as composite agency or organizational closure |
| Exact reduction of decentralized control via common information | Nayyar, Mahajan & Teneketzis 2012, "Decentralized Stochastic Control with Partial History Sharing" *IEEE TAC* 58 (published 2012, found 2026-04) | *adjacent literature* — names the formal space where a lossy composition theorem would live but proves an exact reduction, not a closure-defect bound |
| Approximate dynamical homomorphism / model reduction | Mori-Zwanzig projection (1965); balanced truncation (Moore 1981); Koopman-operator analysis (Koopman 1931; modern review Mezić 2005) | *formal antecedent* — supplies the approximate-dynamical-homomorphism framing of the closure defect. The MZ zero-lag bound surfaces in this segment's derivation table under stationarity. Adopted as standard machinery |
| Information bottleneck for the projection | Tishby, Pereira & Bialek 1999, "The information bottleneck method" *Allerton* | *formal antecedent* — admissibility condition (P1) is the IB Lagrangian-dual with source $X_\mathrm{micro}$ and relevance "next macro-observation given action" |

**Search Log:**

- 2026-04 (*nominally comprehensive*, via `ref/Novelty_defense_and_integration.md` Pillar 2): Two-search Undermind pass over composite agency, approximate information states, Markov-blanket nested agency, decentralized control, state abstraction, and influence-based abstraction. Verdict: *Conceptual Precursor* (High confidence). Markov-blanket line (Parr 2019; Kirchhoff 2018) positioned as conceptual precursor on nested agency without bridge-lemma mathematics; approximate-information-states / state-abstraction / influence-based-abstraction line (Sub20; Con20; Abe16; Tay08; Nay12) positioned as closest mathematical neighbors with shared predictive-loss-to-control-error mechanism but applied to single-agent or already-decomposed control problems rather than to agent boundary formation.
- 2026-04 (*intuition-only*, prior to comprehensive search): adjacent literatures expected to host prior art were dynamical-systems model reduction (Mori-Zwanzig, balanced truncation), active-inference Markov-blanket work, and PAC-MDP state-abstraction. The comprehensive search confirmed all three families and added the influence-based-abstraction and decentralized-control-via-common-information lines that intuition did not surface.

## Working Notes

- **Resolved: $\mathcal P_{\text{adm}}$ now has a proposed definition.** (P1)-(P3) above. Confirmed independent of (A1)-(A4) — the macro-dynamics admissibility partially constrains projections but does not specify information-preservation level. See `spikes/spike-projection-admissibility.md` §5 for the analysis.
- **Resolved (2026-04-22): temporal coarse-graining gap.** The previous formulation summed $\varepsilon_x, \varepsilon_a, \varepsilon_o$ over micro-timesteps ($t=1, \ldots, H$), forcing synchronous micro-and-macro cadence. This contradicted #der-temporal-nesting (composites naturally update on slower timescales, $\nu_{\text{level }n+1} \ll \nu_{\text{level }n}$) and conflicted with #der-tempo-composition's dimensional accounting, which treats $\varepsilon^\ast$ as a per-macro-step quantity and $\nu_c$ as the macro-update rate. Introducing the timescale ratio $K_c \geq 1$ and reformulating the defects per macro-step fixes both issues: $\Lambda_o, \Lambda_a$ become window-aware (aggregating $K_c$ micro-observations/actions), the sum runs over macro-steps $m$, and $\varepsilon^\ast \nu_c$ has consistent rate units by construction. $K_c = 1$ recovers the previous formula; $K_c \gg 1$ enables the timescale abstraction that was always part of the composition theory's intent. The bridge lemma and the sector-persistence-template instantiation are unchanged in substance — the template's state variable is now $e_m$ at macro-boundaries rather than $e_t$ at micro-timesteps, but the Lyapunov argument is identical. Option 3 of `audits/pending-findings-2026-04-21.md` Finding A; Option 2 (full Mori-Zwanzig equilibrium-residual form) remains a possible future refinement if one wants an explicit singular-perturbation framing.
- **Resolved: norm choices for estimation-type agents.** The Mahalanobis norm (inverse-covariance-weighted) is the natural choice for Kalman-type agents, verified exactly in the two-Kalman case. The general principle (weight by inverse uncertainty) extends to other estimation frameworks. For non-estimation agents (discrete states, non-Gaussian), norms remain domain-specific.
- **Open: computing (P1) for nonlinear/non-Gaussian systems.** The information-preservation condition requires conditional mutual information over the joint distribution of micro-states, observations, and actions. Tractable for linear-Gaussian systems (closed-form); requires Monte Carlo estimation or variational bounds for general systems.
- **Open: the right value of $\epsilon_I$.** The information-preservation threshold is a free parameter. Too small ($\epsilon_I \to 0$) excludes useful projections; too large ($\epsilon_I \to 1$) admits degenerate ones. A natural candidate: $\epsilon_I$ comparable to the fractional information loss from adding one agent to the composite — tying it to team size and coupling structure. Formalizing this is open.
- **Resolved (2026-05-19): $N$-agent scaling of $\varepsilon^\ast$ — the poly-vs-exp framing was mis-typed.** $\varepsilon^\ast$ is a *per-step* residue; "scales polynomially or exponentially in $N$" is an *accumulation*-typed predicate (the accumulation-type confound — see CHANGELOG 2026-05-19, `NOTATION.md` §"Accumulation typing"). Re-typed, it dissolves: dimension-free-zero (benign linear-Gaussian-stationary, all $N$, all coupling); graph-Laplacian-bounded with no exponential regime under compression (the consensus operator already in `#deriv-critical-mass-composition`); order-incompatibility-invariant $\leq\lvert S\rvert\log 2$ ($N$-free) for strategy-DAG composition. *History (not present truth): this note previously asserted an open "polynomial vs. exponential, coupling-structure-dependent" question and "the formal analog of the claim that very large teams cannot be treated as single agents"; that framing was the mis-type and is withdrawn — deleted and replaced when the re-typing landed, 2026-05-19, see CHANGELOG.* Reasoning trail: `spikes/spike-composition-scaling-N.md` (scoping) + the accumulation-type-confound trail (transient, → `.integrated/`).
- **Partial: Mori-Zwanzig connection.** Under stationarity and coordinate-compatibility assumptions on the micro-dynamics, the Koopman-operator framing lifts $\Lambda_x$ to a Hilbert-space projection $P_\Lambda$ with $Q_\Lambda = I - P_\Lambda$. The MZ-optimal Markovian macro-dynamics is $f_c^{\text{MZ}} = P_\Lambda U P_\Lambda$ (the conditional expectation given the macro-state), providing a concrete benchmark against which admissibility constraints can be measured. When $f_c^{\text{MZ}} \notin \mathcal M_{\text{adm}}$, the per-step bound $\varepsilon^\ast \geq \lVert Q_\Lambda U P_\Lambda \rVert_{\text{op}}$ holds — a zero-lag memory-kernel bound. The bridge-lemma contraction on $f_c$ in state space corresponds to spectral gap of $Q_\Lambda U$ in observable space (distinct quantities but related). *What does not close*: the full-kernel bound $\varepsilon^\ast \geq C \cdot \lVert K \rVert_{\ell^1}$ (sum-of-lags) is a type mismatch — $\varepsilon^\ast$ is per-step; $\lVert K \rVert_{\ell^1}$ is trajectory-accumulation. Natural home for the full-kernel norm is the bridge lemma's trajectory-error bound, not $\varepsilon^\ast$ directly. *Hard obstruction*: MZ's stationarity assumption fails for purposeful agents with non-stationary auxiliary state (Beta-Bernoulli with diverging $n$) — exactly the cases where $\varepsilon^\ast \gt 0$ genuinely. Extending to these requires innovation-frame reformulation, not yet developed.
- **(P1) as IB Lagrangian-dual — resolved.** (P1) is the Lagrangian-dual of a standard IB constraint with source $X_{\text{micro}}$, compressed representation $\Lambda_x(X_{\text{micro}})$, relevance variable $o_{\text{micro},t+1} \mid a_{\text{micro},t}$, and $\beta(\epsilon_I)$ the rate-distortion multiplier. See #disc-compression-operations for the derivation and for the shared IB shape across AAT's four compression operations ($M_t$, $\Sigma_t$, shared intent, $\Lambda$). (P2) Lipschitz continuity remains a separate analytic admissibility condition. (P3) dimensional reduction remains separate in the Gaussian case (the IB-optimal $T$ at any finite $\beta$ typically uses full support; categorical dimensional reduction is harder than any rate constraint). The "all admissibility is IB" slogan overclaims; the accurate slogan is "(P1) is IB; (P2) and (P3) compose with it as separate conditions." Cross-instance unification is shape-sharing (U-medium), not a reduction to a single master problem (U-strong) — cross-instance theorems do not follow from the shared IB shape alone.
- **Two independent drivers of $\varepsilon_x$.** The non-degenerate Kalman case (heterogeneous gains $K_1^\ast \neq K_2^\ast$ with projection $\Lambda_x(\hat\omega_1, \hat\omega_2) = (\hat\omega_1 + \hat\omega_2)/\sqrt 2$) shows $\varepsilon_x$ depends on *both* sub-agent unity (process correlation, captured by $U_M$) *and* update-rule heterogeneity ($\Delta K = K_1^\ast - K_2^\ast$). $\Delta K = 0$ gives $\varepsilon_x = 0$ at every correlation; $\Delta K \neq 0$ gives $\varepsilon_x \gt 0$ even at perfect correlation. The closed form is $\varepsilon_x^2 = (\Delta K/2)^2 [S_- - C_{+-}^2/S_+]$ where $S_\pm$ are innovation variances in the $\pm$ rotation and $C_{+-}$ their cross-covariance. Heterogeneity is not captured by the four unity dimensions in #def-unity-dimensions as currently defined; this is a gap in that segment, not in this one — the closure defect correctly registers both drivers. See #result-unity-closure-mapping for the full analysis.
- **Resolved (2026-05-19): strategy-DAG projection under $\Lambda_x$.** The right object is a causal-$\tau$-abstraction of the joint micro-strategy (Beckers–Eberhardt–Halpern frame, adopted with citation; *not* term-for-term — BEH leaves the high-level distance application-dependent, so the norm-on-graphs choice remains AAT's). Exact $\Sigma_c$ iff shared sub-orders are jointly acyclic and AND/OR-compatible; otherwise the minimal admissible $\Sigma_c$ is the SCC-condensation with closure defect $\sum_{\lvert C\rvert\gt1}\mathrm{TC}(C)\leq\lvert S\rvert\log 2$ — bounded by shared-plan size, $N$-free. Status *conditional* with one named sub-open (Q1: constant-tightness for non-deterministic intra-SCC status coupling — a sub-open, not a reopening). *History (not present truth): this note previously listed the question as "deeply domain-specific and not resolved by (P1)-(P3)"; resolved and replaced 2026-05-19 — see CHANGELOG.* Derivation home: #def-strategy-dag §"Composing heterogeneous strategy DAGs" (the $\tau$-abstraction typing, the SCC-condensation no-go, the Brooks's-Law-floor corollary) and #result-unity-closure-mapping (the fixed-topology credence-composition instance); reasoning trail at `spikes/.integrated/spike-strategy-dag-composition.md`.
- ~~The bridge lemma's contraction assumption — proving it from (A4) alone.~~ **CHARACTERIZED 2026-04-06** (`spikes/spike-bridge-lemma-contraction.md`). The contraction assumption cannot be proved from (A4) alone. The precise additional condition is the **incremental sector bound** (DA2'a-inc): the correction function $F_d$ must be *strongly monotone* ($\langle \delta - \delta', F_d(\delta) - F_d(\delta') \rangle \geq c_{\min} \lVert \delta - \delta' \rVert^2$), not just satisfy the one-point sector bound. Strong monotonicity is strictly stronger than the one-point sector bound (counterexample: oscillatory corrections that are globally inward-pointing but locally non-monotone). Three agent tiers emerge: **Tier 1** (contraction proved — all Bayesian updaters on exponential families, all gradient agents on strongly convex losses, all linear corrections with positive definite gain-observation product); **Tier 2** (local contraction — nonlinear prediction models, with factor degraded by $\kappa(D\hat{o})^2$); **Tier 3** (independent verification required — non-convex optimization, discontinuous rules, agents with non-mismatch-driven state components). For Tier 1 agents, the bridge lemma is promoted from "conditional" to "derived (conditional on DA2'-inc + linear prediction)." The contraction factor equals $\lambda_{\text{eff}}$ from #deriv-discrete-sector-condition.
- The weakest-link structure ($\alpha_c = \min_i \alpha_i^{\text{eff}}$) is conservative. In practice, strong sub-agents may compensate for weak ones through cooperative coupling. A tighter bound would account for cross-agent compensation, likely through the cooperative disturbance reduction terms in #der-team-persistence.
- **A richer toy case** is needed: two purposeful agents (Section II) with strategy DAGs, cooperative communication, and a shared objective. This would exercise (A1) fully (including the $G_c$ component) and test whether the admissibility constraints are tight enough to be useful without being so tight they exclude interesting composites.
- The approach is an approximate dynamical homomorphism condition, a standard tool in dynamical systems and model reduction (cf. Mori-Zwanzig projection, balanced truncation). The specific contribution is applying it to AAT's closed-loop agent structure with sector-condition-based stability guarantees.

- **Mori-Zwanzig memory-kernel relationship — upper-bound direction closes; named lower bound does not.** The closure defect $\varepsilon^\ast$ has a tractable upper-bound relationship to a Mori-Zwanzig (MZ) memory kernel norm $\VertK\Vert$ when AAT's state-space projection $\Lambda$ is composed with an MZ Hilbert-space projection $P$ on a stationary observable measure $\pi$: under (i) stationarity of $\pi$ under micro-dynamics, (ii) compatibility of $\Lambda$ with $P$'s range (the projected observables include the coarse-grained state coordinates AAT's $\Lambda$ retains), and (iii) bounded operator-norm of $K$, the upper bound $\varepsilon^\ast \le C \cdot \VertK\Vert$ holds for a constant $C$ depending on $\alpha_c, \nu_c$. The *named target* lower bound $\varepsilon^\ast \ge C' \cdot \VertK\Vert$ — which would make slow-decaying memory kernels an *obstruction* to small closure defect — does NOT close under the current AAT formulation without additional structural hypotheses. The obstruction is that $\Lambda$ (state-space coarse-graining) and $P$ (Hilbert-space projection on observables) are *different objects*, and a generic AAT coarse-graining does not give an orthogonal MZ-style projection on the observable Hilbert space; the lower bound would require either a stronger compatibility assumption between $\Lambda$ and $P$ or a separate orthogonality-of-residual argument that has not been worked out. The honest structural takeaway: MZ memory-kernel decay is a *sufficient* condition for small $\varepsilon^\ast$ (via the upper bound direction) but is not *necessary*; AAT's closure defect can be small for reasons that don't reduce to MZ memory-kernel norms. Future work would either close the lower-bound direction under specific Hilbert-space hypotheses on the agent's observable algebra, or settle the asymmetry as a structural feature distinguishing AAT's coarse-graining from MZ projection-operator formalism.


---

### Source: `der-tempo-composition.md`

```yaml
---
slug: der-tempo-composition
type: derived
status: sketch
depends:
  - form-composition-closure
  - result-sector-persistence-template
  - def-adaptive-tempo
stage: draft
---
```


# Derived: Composite Tempo Inequality

The adaptive tempo of a composite agent is bounded from above by the sum of its sub-agents' tempos. The gap between aggregate potential and realized composite tempo is the coordination overhead — tempo consumed by internal reconciliation rather than external mismatch correction.

## Formal Expression

This segment instantiates the sector-persistence template ( #result-sector-persistence-template) at the composite level with state variable $\xi = \delta_c$ (composite mismatch) and a decomposed effective disturbance $\rho_{\text{eff}} = \rho_{\text{ext}} + \varepsilon^\ast \nu_c$ — external environment plus closure-defect contribution from #form-composition-closure's bridge lemma. The template supplies the Lyapunov machinery; this segment's distinctive content is the tempo-equivalent form of the coordination overhead lower bound $C_{\text{coord}} \geq \varepsilon^\ast \nu_c$.

Let $\mathcal T_i$ be the adaptive tempo of sub-agent $i$ within a composite group of $N$ agents. Let $\mathcal T_c$ be the adaptive tempo of the composite macro-agent $A_c$ defined by an admissible coarse-graining $\Lambda$.

*[Derived (Sub-additive Tempo, sketch)]* For any composite agent $A_c$ with minimal closure defect $\varepsilon^\ast \geq 0$, the composite tempo is bounded by the sum of individual tempos:
$$ \mathcal{T}_c \leq \sum_{i=1}^N \mathcal{T}_i $$

*[Definition (Coordination Overhead)]* We define the **coordination overhead penalty** $C_{\text{coord}}$ as the difference between aggregate potential and realized macro-tempo:
$$ C_{\text{coord}} := \Big( \sum_{i=1}^N \mathcal{T}_i \Big) - \mathcal{T}_c $$

## Epistemic Status

*Sketch.* Max attainable: exact (with a complete proof). The inequality is structurally motivated: composition cannot create corrective capacity out of nothing, and internal reconciliation consumes tempo that doesn't contribute to external mismatch correction. The $\varepsilon^\ast \to C_{\text{coord}}$ connection is sketched: closure defect as internal disturbance rate $\varepsilon^\ast\nu_c$ (units $[\text{distance}]\cdot[\text{time}^{-1}]$) converts to a tempo-equivalent penalty $C_{\text{coord}} \geq \varepsilon^\ast\nu_c / \lVert\delta_{\text{critical}}\rVert$ (units $[\text{time}^{-1}]$) through the same distance normalization used by the persistence condition. The inequality $\mathcal T_c \leq \sum \mathcal T_i$ follows. **Caveat:** this connection depends on the bridge lemma in #form-composition-closure, which requires a contraction assumption on the macro-update map — an assumption that is structurally motivated by (A4) but not formally derived from it (see #form-composition-closure, Epistemic Status). The "follows directly" language below should be read as "follows from the bridge lemma under its contraction assumption." The remaining gap: whether the lower bound is tight or whether additional coordination costs contribute beyond the closure-defect mechanism.

### Intuition

Tempo is a rate of mismatch correction. When $\varepsilon^\ast = 0$ (exact closure), every sub-agent correction cycle contributes directly to the macro AAT loop without friction, and $\mathcal T_c = \sum \mathcal T_i$. When $\varepsilon^\ast \gt 0$, sub-agents spend part of their tempo correcting *internal* mismatches generated by other sub-agents (Alice changes an API; Bob must update his $M_t$) or taking actions that counteract each other. That fraction is $C_{\text{coord}}$ and is unavailable for external mismatch correction.

### The closure-defect to coordination-overhead connection

*[Derived (coordination-overhead-bound, from composition-closure bridge lemma)]*

The closure defect $\varepsilon^\ast$ introduces internal mismatch at rate $\varepsilon^\ast \nu_c$ — units of $[\text{distance}] \cdot [\text{time}^{-1}]$, a disturbance rate matching the units of environmental $\rho$. This internal mismatch must be corrected by the macro-agent's correction capacity, and the correction consumes tempo that would otherwise address external mismatch.

**Dimensional accounting.** Three quantities appear in the composite persistence analysis, each with its own units:

| Quantity | Units | Role |
|---|---|---|
| Tempo $\mathcal T$, $\mathcal T_c$, $\mathcal T_c^{\text{ext}}$, $C_{\text{coord}}$ | $[\text{time}^{-1}]$ | Rate of mismatch correction |
| Disturbance rate $\rho$, $\rho_{\text{eff}}$ | $[\text{distance}] \cdot [\text{time}^{-1}]$ | Rate of mismatch injection |
| Closure defect $\varepsilon^\ast$ | $[\text{distance}]$ | Per-step norm error |
| Critical scale $\lVert\delta_{\text{critical}}\rVert$ | $[\text{distance}]$ | Task-adequacy boundary |

The conversion between a disturbance rate and a tempo-equivalent requires division by a distance scale, mirroring the persistence condition form $\mathcal T \gt \rho / \lVert\delta_{\text{critical}}\rVert$.

**Effective disturbance.** The macro-agent faces total effective disturbance combining external and closure-defect contributions:

$$\rho_{\text{eff}} = \rho_{\text{ext}} + \varepsilon^\ast \nu_c \quad \text{(units: } [\text{distance}] \cdot [\text{time}^{-1}] \text{)}$$

**Coordination overhead (tempo-equivalent).** The fraction of macro-tempo consumed by closure correction, expressed as a tempo:

*[Derived (coordination-overhead-tempo-form)]*

$$C_{\text{coord}} \;\geq\; \frac{\varepsilon^\ast \nu_c}{\lVert\delta_{\text{critical}}\rVert} \quad \text{(units: } [\text{time}^{-1}] \text{)}$$

The closure error rate is converted to a tempo penalty by normalizing against the task-relevant distance scale. The inequality is a lower bound because additional coordination costs (negotiation, synchronization, conflict resolution — see Working Notes) contribute beyond the closure-defect mechanism. When the macro-agent's correction of internal mismatch is less efficient than its correction of external mismatch (because internal mismatches may be harder to diagnose — they look like environmental change from the macro perspective), the actual overhead exceeds this bound.

**Consequences (dimensionally correct):**

- The realized external tempo:
$$\mathcal T_c^{\text{ext}} = \mathcal T_c - C_{\text{coord}} \;\leq\; \sum \mathcal T_i - \frac{\varepsilon^\ast \nu_c}{\lVert\delta_{\text{critical}}\rVert}$$
- **Brooks's Law.** Adding an agent increases $\sum \mathcal T_i$ but may also increase $\varepsilon^\ast$. The turning point — where adding a member lowers realized external tempo — occurs when:
$$\frac{\Delta\varepsilon^\ast \nu_c}{\lVert\delta_{\text{critical}}\rVert} \gt \Delta\mathcal T_i$$
The closure-defect increase (expressed as tempo penalty) exceeds the new member's tempo contribution.
- **Composite persistence condition.** The composite persists iff $\mathcal T_c \gt \rho_{\text{eff}} / \lVert\delta_{\text{critical}}\rVert$, equivalently:
$$\sum \mathcal T_i \;\gt\; \frac{\rho_{\text{ext}} + \varepsilon^\ast \nu_c}{\lVert\delta_{\text{critical}}\rVert}$$
which explicitly separates internal-coordination overhead from external challenge while keeping all quantities in tempo units on the LHS and disturbance-rate units on the RHS.

## Discussion

**Equality conditions.** Strict equality ($\mathcal T_c = \sum \mathcal T_i$, i.e. $C_{\text{coord}} = 0$) requires:
1. **Orthogonal Routing:** The information dependency DAG exactly matches organizational boundaries (no costly cross-talk required).
2. **Perfect Shared Intent:** No tempo is lost to internal negotiation or conflicting pursuit of the macro-objective.
3. **No Net Macro-Information Loss:** Observations may be redundant, but they do not result in wasted tempo after fusion, nor is critical macro-information lost during coordination.

These are stated as sufficient conditions; whether they are also necessary is open.

**Brooks's Law.** Adding more agents (increasing $\sum \mathcal T_i$) only increases the composite tempo $\mathcal T_c$ if the corresponding increase in closure defect $\varepsilon^\ast$ doesn't let $C_{\text{coord}}$ dominate. The model provides a formal analog of Brooks's Law: if communication overhead ($C_{\text{coord}}$) grows faster than aggregate capability ($\sum \mathcal T_i$) when adding agents, then adding people to a late project makes it later. Whether this specific mechanism (coordination overhead consuming tempo) is the dominant cause in practice is an empirical question.

**Connection to #der-team-persistence.** The persistence condition for the composite agent requires $\mathcal T_c \gt \rho_{\text{ext}} / \Vert\delta_{\text{critical}}\Vert$. Since $\mathcal T_c = \sum \mathcal T_i - C_{\text{coord}}$, high coordination overhead can push the composite below the persistence threshold, causing it to disintegrate as a coherent entity — even though each sub-agent individually persists.

**Wrapping construction as a Brooks's-Law instance.** Class coercion of a Class 2 (Partial) or Class 3 (Coupled) component via wrapping (`#der-class-coercion-via-wrapping`) is a concrete instance of the same coordination-overhead form. A wrapper makes $K \geq 2$ component calls per macro-step (one for each goal-blind belief-update query, one for the goal-conditioned strategy-update query, more in richer wrapper designs). The wrapper-level macro-update rate is $\nu_W = \nu_A / K$ where $\nu_A$ is the underlying component's nominal call rate, so the wrapper-level tempo is $\mathcal T_W \leq \mathcal T_A^{\text{nominal}} - C_{\text{coord}}^{\text{wrap}}$, with the coordination overhead $C_{\text{coord}}^{\text{wrap}}$ scaling with $K$. The cost of class coercion — the structural enforcement of directed separation at the wrapper level when the underlying component does not provide it — is paid in macro-tempo. Strict-wrapping (W₁) regimes have $K \geq 2$ minimum; partial-wrapping (W₂) regimes have $K = 1$ for the LLM call plus some parsing overhead, but the structural-separation guarantee is correspondingly weaker (see `#der-class-coercion-via-wrapping`).

## Working Notes
- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Removed at `candidate` stage per FORMAT.md Gate 4.
- The lower bound $C_{\text{coord}} \geq \varepsilon^\ast \nu_c / \lVert\delta_{\text{critical}}\rVert$ captures the minimum tempo-equivalent overhead from closure defect. Additional coordination costs likely contribute beyond this: negotiation costs (reaching shared decisions), synchronization costs (waiting for slower agents), and conflict resolution costs (undoing contradictory actions). These are not captured by $\varepsilon^\ast$ because they arise from the coordination PROCESS, not from the closure DEFECT. A fuller model would add: $C_{\text{coord}} = \varepsilon^\ast \nu_c / \lVert\delta_{\text{critical}}\rVert + C_{\text{negotiation}} + C_{\text{sync}} + C_{\text{conflict}}$, with all terms in tempo units.
- **Heterogeneity drives closure defect.** For agents with equal correction rates ($\alpha_1 = \alpha_2$), $\varepsilon^\ast = 0$ and $C_{\text{coord}} = 0$. For agents with different correction rates, $\varepsilon^\ast \propto \lvert\alpha_1 - \alpha_2\rvert$ — heterogeneity drives closure defect, confirmed analytically in the 2-agent toy case.
- The internal/external mismatch distinction is formalized through the bridge lemma: trajectory error $e_t$ is the internal mismatch (divergence between macro-prediction and micro-reality, units of distance), and the tempo spent reducing $e_t$ is the coordination overhead. The steady-state internal mismatch is $\varepsilon^\ast \nu_c / \alpha_c$ (a distance, since $\alpha_c$ has units $[\text{time}^{-1}]$), and maintaining this at the critical-distance scale requires ongoing tempo expenditure of $\varepsilon^\ast \nu_c / \lVert\delta_{\text{critical}}\rVert$.
- **Norm specification note.** The closure defect $\varepsilon^\ast$ depends on the norm choices in #form-composition-closure. For estimation-type agents, the natural norm is Mahalanobis (weighted by inverse prediction-error covariance). In these norms, $\varepsilon^\ast$ measures the ratio of missed cross-correction to expected estimation uncertainty — a quantity with direct tempo interpretation: it's the fraction of macro-tempo consumed by correcting errors that optimal cross-exploitation would eliminate.
- **Channel-independence assumption.** The sub-additive bound $\mathcal T_c \leq \sum \mathcal T_i$ uses scalar tempos that each inherit the channel-independence assumption from #def-adaptive-tempo. When sub-agents' observation channels overlap, the individual $\mathcal T_i$ are already overcounted, making the upper bound looser than it appears. The coordination overhead $C_{\text{coord}}$ is defined relative to the (possibly inflated) sum, so the *fraction* of tempo consumed by coordination may be underestimated.
- **$\varepsilon^\ast$ scaling with $N$ — resolved (no longer open).** The poly-vs-superlinear framing was an accumulation-type confound (a per-step residue asked an accumulation question); re-typed it dissolves — see #form-composition-closure (the $N$-agent-scaling and strategy-DAG-projection rows + Discussion): $\varepsilon^\ast(N)$ is dimension-free-zero in the benign linear-Gaussian-stationary regime (all $N$, all coupling), graph-Laplacian-bounded with no exponential regime under compression, and order-incompatibility-invariant ($\leq\lvert S\rvert\log 2$, $N$-free) for strategy-DAG composition. Brooks's-Law collapse, if it occurs, is driven by coordination overhead $C_{\text{coord}}$, not by $\varepsilon^\ast(N)$ growth (the Brooks's-Law-floor corollary is in #def-strategy-dag §"Composing heterogeneous strategy DAGs"). Derivation home: #form-composition-closure + #def-strategy-dag + #result-unity-closure-mapping; CHANGELOG 2026-05-19.


---

### Source: `deriv-critical-mass-composition.md`

```yaml
---
slug: deriv-critical-mass-composition
type: derivation
status: conditional
depends:
  - form-composition-closure
  - scope-composite-agent
  - result-sector-persistence-template
  - deriv-sector-condition
  - der-team-persistence
  - der-adversarial-destabilization
  - hyp-symbiogenic-composition
  - result-unity-closure-mapping
stage: draft
---
```


# Derivation: Critical-Mass Composition

The composite sector constant $\alpha_c$ is derived — not merely bounded from below — for the symmetric-matched-Tier-1 two-agent case, yielding a closed-form critical-mass inequality in which the sign of the inter-agent coupling $\gamma$ and the teleological unity $U_O$ enter explicitly. The result subsumes the weakest-link bound, recovers #der-team-persistence (cooperative) and #der-adversarial-destabilization (adversarial) as signed special cases, formalizes #hyp-symbiogenic-composition's autonomy-reduction mechanism as an asymmetric Lyapunov-weight limit, and makes the scope-gate from #scope-composite-agent explicit as the second conjunct of composite persistence.

## Formal Expression

### Setup

Two sub-agents $A_1, A_2$, each a **Tier 1 agent** in the sense of #form-composition-closure's bridge-lemma taxonomy — mismatch-driven update, linear prediction, incremental sector-Lipschitz correction (Kalman, exponential-family Bayesian, gradient-on-strongly-convex, linear-with-PD-KH). **Matched architectures**: $f_1, f_2$ are structurally the same function, with $\alpha_1 = \alpha_2 = \alpha$, $R_1 = R_2 = R$. Disturbance statistics shared: each sees bounded $w_i(t)$ with $\lVert w_i\rVert \leq \rho$ (Model D, per #result-sector-persistence-template).

*[Formulation (coupling-model-C1, from #der-team-persistence + #der-adversarial-destabilization)]*

Inter-agent coupling enters additively to the disturbance at rate $\gamma \mathcal T_j$:

$$\rho_i^{\text{eff}} = \rho + \gamma \mathcal T_j \tag{C1}$$

with sign convention $\gamma \lt 0$ cooperative (ally's tempo-contribution reduces disturbance, recovering #der-team-persistence's $-\gamma^{\text{coop}}\mathcal T_j$ term), $\gamma \gt 0$ adversarial (ally's tempo-contribution amplifies disturbance, recovering #der-adversarial-destabilization's $+\gamma_A\mathcal T_A$ term). Symmetric case: $\gamma_{1 \to 2} = \gamma_{2 \to 1} = \gamma$.

*[Formulation (coordination-cost-C2)]*

Coordination overhead reduces each agent's effective correction rate symmetrically:

$$\alpha_i^{\text{eff}} = \alpha - C \tag{C2}$$

with $C \geq 0$ the $\Delta \mathcal T_i^{\text{cost}}$ from #der-team-persistence's coordination-overhead threshold.

### Critical-mass inequality (symmetric-matched-Tier-1 case)

*[Derived (critical-mass-symmetric, from #result-sector-persistence-template + C1 + C2)]*

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
| No coupling | $\gamma = 0$, $C = 0$ | $\alpha R \gt \rho$ | Single-agent #result-persistence-condition |
| Cooperative-symmetric | $\gamma \lt 0$, $C = 0$ | $\alpha R \gt \rho + \gamma\mathcal T$ (easier than individual) | #der-team-persistence's "teams persist where individuals can't" |
| Adversarial-symmetric | $\gamma \gt 0$, $C = 0$ | Fails when $\gamma\mathcal T \gt \alpha R - \rho$ | #der-adversarial-destabilization threshold (symmetric) |
| Coordination-dominated | $C \gt \alpha$, $\gamma = 0$ | LHS $\lt 0$; composite fails | Brooks's Law |

### Subsumption of the weakest-link bound

*[Derived (weakest-link-subsumption)]*

The weakest-link bound $\alpha_c \geq \min_i(\alpha_i - \Delta\mathcal T_i^{\text{cost}})$ from #form-composition-closure's derivation table specializes under matched symmetry to $\alpha_c \geq \alpha - C$. (KC) refines this by making the composite's effective disturbance explicit as $\rho + \gamma\mathcal T$, turning a correction-rate bound into a full persistence inequality. Critically, (KC) can yield $\kappa_c \gt 0$ even when the weakest-link bound alone fails — when cooperative coupling ($\gamma\mathcal T \lt 0$) reduces the effective disturbance below what the raw $\alpha - C$ margin would permit. The weakest-link bound cannot see this because it does not account for $\gamma$'s sign.

### $U_O$ entry: multiplicative-on-$\gamma$ plus scope-gate

*[Derived (unity-multiplicative-modulator, conditional on LQR-compatible action structure)]*

In a purposeful-agent setting where each sub-agent optimizes a quadratic objective $L_i(\omega) = \tfrac{1}{2}(\omega - r_i)^T Q(\omega - r_i)$ with target $r_i$, and $U_O := \operatorname{corr}(r_1, r_2)$ is the target correlation per #def-unity-dimensions' $U_O$, the cross-coupling in the joint dynamics has sign and magnitude controlled by $U_O$:

$$\gamma(U_O) \;=\; -\,\gamma_{\max}\, U_O, \qquad \gamma_{\max} \gt 0, \tag{UO-mult}$$

via aligned targets → aligned action directions in the shared environment → constructive (cooperative) cross-contribution in the symmetric eigendirection. Substituting into (KC):

$$\kappa_c(U_O) \;=\; (\alpha - C)R \;-\; \rho \;+\; \gamma_{\max}\,U_O\,\mathcal T. \tag{CM3}$$

*[Scope (scope-gate-from-composition-scope-condition)]*

(CM3) is necessary but not sufficient for composite existence. Under #scope-composite-agent, a composite exists as an AAT agent only when one of the three disjunctive alignment routes (shared objective, hierarchical derivation, mutual benefit) is satisfied. Below this threshold, no coherent $O_c$ is definable and composite-level quantities — including $R_c$ on the right of (CM2) — are ill-typed. The honest statement of composite persistence is therefore the conjunction of $\kappa_c(U_O) \gt 0$ with the scope conditions of #scope-composite-agent — abbreviated $\mathcal{S}_c$:

$$\boxed{\;\kappa_c(U_O) \gt 0 \;\wedge\; \mathcal{S}_c \;\Leftrightarrow\; \text{composite persists as AAT agent}\;} \tag{CM4}$$

$U_O$ enters (CM4) in two independent ways: multiplicatively within (CM3), and as scope-gate via #scope-composite-agent. It does **not** enter purely additively as a separate reserve term — there is no free-floating "$U_O$ contribution" detached from the coupling it modulates.

### Asymmetric limit and symbiogenic composition

*[Sketch (asymmetric-limit-symbiogenesis, from weighted Lyapunov)]*

Drop the matched-symmetric assumption. Let $\alpha_1 \gg \alpha_2$ with $\alpha_2 \to 0$. The unweighted joint Lyapunov $V = \tfrac{1}{2}(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2)$ fails (the weakest-link ultimate bound diverges as $\alpha_2 \to 0$). A **weighted** Lyapunov $V_\mu(\xi) = \tfrac{1}{2}(\lVert\delta_1\rVert^2 + \mu\lVert\delta_2\rVert^2)$ with $\mu \to 0$ yields

$$\dot V_\mu \leq -\alpha_1\lVert\delta_1\rVert^2 + \rho_1\lVert\delta_1\rVert \;+\; O(\mu),$$

so in the limit the composite's stability is controlled **entirely by agent 1**; agent 2's autonomous correction dynamics are weighted out of the stability accounting.

This provides a Lyapunov-weighted formalization of #hyp-symbiogenic-composition's **(S-3) autonomy reduction**: the endosymbiont's effective action space contracts ($\mathcal A_e^{\text{effective}} \to \mathcal A_e^{\text{restricted}}$) and its autonomous dynamics fall out of the joint Lyapunov argument. The asymmetric limit is a smooth deformation of (CM4), not a discontinuous regime change — symbiogenesis and peer coupling are parameter-limits of the same weighted-Lyapunov analysis. The result does **not** close #hyp-symbiogenic-composition's (S-1) objective absorption or (S-2) function transfer: what happens to agent 1's state space when it inherits structure from agent 2 is a separate question the weighting argument does not address.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Coupling model (C1): $\rho_i^{\text{eff}} = \rho + \gamma\mathcal T_j$ | Import from #der-team-persistence and #der-adversarial-destabilization | Formulation choice (requirement for the derivation) |
| Coordination-cost model (C2): $\alpha_i^{\text{eff}} = \alpha - C$ | Import from #der-team-persistence's coordination-overhead threshold | Formulation choice |
| Joint quadratic Lyapunov $V = \tfrac{1}{2}(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2)$ | Standard vector-Lyapunov construction (Matrosov 1962; Bellman 1962) | Formulation choice (canonical for matched-symmetric dyads) |
| Ultimate bound $R_c^\ast \leq (\rho + \gamma\mathcal T)/(\alpha - C)$ | Lyapunov dissipation + Cauchy–Schwarz | Derived |
| Critical-mass inequality (CM2): $(\alpha - C)R \gt \rho + \gamma\mathcal T$ | (L4) + sector-region fit $R_c^\ast \lt R_c = R$ | Derived (conditional on Tier 1 + matched-symmetric + Model D) |
| Four specialization checks (no-coupling / cooperative / adversarial / coordination-dominated) | Direct substitution into (CM2) | Proved (within stated scope) |
| Subsumption of weakest-link bound | (CM2) sign-sensitive; weakest-link is sign-blind | Proved |
| (UO-mult): $\gamma(U_O) = -\gamma_{\max}U_O$ | LQR-compatibility sketch; aligned targets → aligned actions → constructive cross-contribution | Discussion-grade |
| Composite persistence as (CM3) ∧ scope-satisfaction: (CM4) | (KC) with (UO-mult) + #scope-composite-agent | Derived (conditional) |
| Asymmetric limit → #hyp-symbiogenic-composition (S-3) via weighted Lyapunov | Matrosov-style weighting; $\mu \to 0$ limit | Sketch (the weighting is standard; the identification with (S-3) is structurally motivated but not a theorem) |
| (S-1) objective absorption and (S-2) function transfer formalizations | Not addressed by this derivation | Open (in #hyp-symbiogenic-composition Working Notes) |
| Heterogeneous-architecture case ($A_1$ Tier 1, $A_2$ Tier 2/3) | Requires per-sub-agent tiering per #form-composition-closure | Open |
| Heterogeneous-metric Tier-1M dyad ($\lambda_1 \neq \lambda_2$, $C_1 \neq C_2$, $k_{12} \neq k_{21}$) | #result-contraction-template (CM2-M) via Slotine 2003 negative-feedback small-gain: $(\lambda_1 - C_1)(\lambda_2 - C_2) \gt k_{12} k_{21}/4$ | Derived (conditional on #result-contraction-template (CT2) preconditions + Slotine 2003) |
| Nonlinear coupling $\gamma = \gamma(\delta_j)$ | Requires full joint-Lyapunov machinery from #der-adversarial-destabilization (effects-spiral corollary) | Open |
| Dynamic coordination cost $C = C_0 + C_1\lVert\delta_j\rVert$ | Quadratic inequality; admits closed form, loses interpretive cleanliness | Open |
| Fully-coupled tempo dynamics ($\mathcal T_i$ responsive to $\delta_j$) | Requires joint tempo analysis from #der-adversarial-destabilization Working Notes | Open |
| $N \gt 2$ scaling of (CM4) | Conjunction over pairwise terms generalizes but loses closed form; see `spikes/spike-composition-scaling-N.md` | Open |

The dividing line: (C1), (C2), and the quadratic Lyapunov candidate are **formulation choices** imported from adjacent segments or from standard Lyapunov practice. The *consequences* under these choices — (L4), (CM2), (KC), the specialization checks, the weakest-link subsumption, and (CM4) with its scope-gate conjunct — are **derived**. The $U_O$-multiplicative modulator (UO-mult) is discussion-grade: it uses an LQR-compatibility argument whose rigor depends on an action-space inner-product analysis deferred to #result-unity-closure-mapping. The asymmetric-limit identification with #hyp-symbiogenic-composition (S-3) is sketch-level — the weighted-Lyapunov argument is standard but the semantic identification with autonomy reduction is structural, not proved.

## Epistemic Status

*Conditional.* Max attainable: *exact* (within the matched-symmetric-Tier-1 scope); *conditional* beyond.

(CM2) and (KC) are **proved** under Tier 1 architecture + matched-symmetric parameters + Model D disturbance + the (C1) disturbance-coupling model + the (C2) coordination-cost model. These conditions cover Kalman filters, exponential-family Bayesian updaters, gradient-on-strongly-convex agents, and linear-PD correctors — the same architecture class for which #form-composition-closure's bridge lemma is promoted from "conditional" to "derived." Within this scope the result is as strong as the standard Lyapunov argument allows.

(CM3) inherits the conditional status of (UO-mult), which is **discussion-grade**: the LQR-compatibility sketch is qualitatively clear, but a rigorous action-space inner-product derivation that pins down $\gamma_{\max}$ has not been produced. (CM4) is therefore conditional on both (UO-mult)'s rigor and on #scope-composite-agent's scope-gate being independently verified for the given composite candidate.

The asymmetric limit (§asymmetric-limit) is **sketch-level**. The weighted-Lyapunov argument is textbook (Matrosov 1962); the identification of the $\mu \to 0$ limit with #hyp-symbiogenic-composition's (S-3) autonomy-reduction mechanism is structurally motivated but not a theorem, because (S-2) function transfer is not formalized in #hyp-symbiogenic-composition. When (S-2) lands, the symbiogenic-limit result can be promoted to derived.

What this segment does **not** establish:

- Composite **incremental** sector bound (DA2'-inc) — still the domain of #form-composition-closure's bridge lemma and `spikes/spike-bridge-lemma-contraction.md`. (CM4) gives composite (T2) at the macro level; the bridge lemma's contraction is a separate, stronger condition.
- Heterogeneous-architecture composites (Kalman + PID, Tier 1 + Tier 3): the joint Lyapunov construction requires agent-by-agent tiering; closed form is not available.
- Nonlinear or state-dependent coupling: (C1) assumes $\gamma$ independent of $\delta$. State-dependent $\gamma$ produces a nonlinear inequality in $\delta$; this is the effects-spiral corollary territory of #der-adversarial-destabilization, still open.
- $N \gt 2$ scaling: the matched-symmetric pairwise result generalizes by conjunction, but the Cauchy–Schwarz step degrades with team size; the closed form does not survive cleanly. See `spikes/spike-composition-scaling-N.md`.

**On (T2) and sub-scoping.** The joint quadratic Lyapunov candidate presumes each sub-agent's correction is in sub-scope $\alpha$ of #form-sector-condition (Bayesian / exponential-family / strongly-convex-gradient / linear-PD) under directional fidelity per #der-gain-sector-bridge. Composites with sub-scope $\beta$ sub-agents (PID, rule-based, human-judgment) require (T2) verification per sub-agent at the composite level — the template's A2'-sub-scope label is inherited pairwise.

## Discussion

**Relationship to the bridge lemma.** #form-composition-closure's bridge lemma establishes when the macro-update map $f_c$ is **incrementally** contracting, at the trajectory-error level — a condition strictly stronger than the one-point sector bound. This segment is the complement at the macro-state level: given the bridge lemma's admissibility, (CM4) derives composite (T2), the one-point sector bound that #result-sector-persistence-template's instantiation for the composite requires. Both are necessary for the composite to be a stable macro-agent with bounded mismatch: bridge lemma says the macro-description tracks micro-reality (trajectory error stays bounded); (CM4) says the composite's own corrections drive composite mismatch back inside the sector region. Together they close the composite-persistence argument at both layers.

**Pattern across the signed-coupling instances.** (CM4) has the same shape as several persistence-flavored results already in AAT:

- #der-team-persistence: per-sub-agent inequality $\alpha_i R_i \gt \rho_{i,\text{env}} + \sum_j\gamma_{j \to i}^{\text{adv}}\mathcal T_j - \sum_j\gamma_{j \to i}^{\text{coop}}\mathcal T_j$
- #der-tempo-composition: composite inequality with effective disturbance $\rho_{\text{ext}} + \varepsilon^\ast\nu_c$
- #der-adversarial-destabilization: failure condition $\gamma_A\mathcal T_A \gt \alpha_B R_B - \rho_B$ (negation of persistence)
- this segment: matched-symmetric dyad with signed $\gamma$ and scope-gate

All four are instances of #result-sector-persistence-template's pattern with signed coupling controlling the sign of the cross-agent contribution to $\rho_\xi$. The template already names this pattern at the meta level; the present segment is the dyadic closed-form instance that the other three segments reference pairwise. A dedicated meta-segment for "signed-coupling critical-mass" was considered during spike work and judged redundant with #result-sector-persistence-template — the cross-instance structure is already visible in that segment's instantiation table.

**Potential-game generalization (via #deriv-strategic-composition).** (CM4) applies to composites with shared target (scope routes C-i / C-ii / C-iii from `#scope-composite-agent`) where contraction-to-shared-truth is the correct primitive. `#deriv-strategic-composition` carries the sibling result for composites with partially-opposing objectives (scope route C-iv — strategic composites): under the potential-game condition (Monderer-Shapley 1996), the sector-persistence template transfers to the gradient of the joint potential $\Phi$, with $\alpha_{\text{joint}}$ playing the role of the composite sector constant and $\xi = \pi - \pi^\ast$ (deviation from Nash) playing the role of the composite state. For matched-symmetric potential games, the structural form of (CM2) survives with $(\alpha, R, \rho, \gamma, C)$ replaced by $(\alpha_{\text{joint}}, R_{\text{Nash-basin}}, \rho_\xi, \gamma_{\text{strategic}}, C_{\text{strategic}})$; the specific mapping is instance-dependent and typically not closed-form for non-zero-sum games. The joint-quadratic-Lyapunov machinery of this segment and the potential-function-Lyapunov machinery of `#deriv-strategic-composition` are both instances of `#result-sector-persistence-template` at the composite-state-variable level; what varies is whether the composite state is *mismatch-to-shared-target* (this segment) or *deviation-from-Nash* (`#deriv-strategic-composition`).

**What (CM4) contributes beyond existing segments.**

1. **Derivation, not assumption.** The composite sector constant appearing in #form-composition-closure's (A4) was previously bounded by the weakest-link formula (a derived lower bound) but treated as an assumption for the bridge lemma. (CM4) *derives* $\alpha_c$ as a closed-form function of sub-agent parameters + coupling + unity + coordination overhead, in the matched-symmetric-Tier-1 case.
2. **Sign-sensitive.** The weakest-link bound is sign-blind — it gives the same $\alpha_c \geq \alpha - C$ regardless of whether the coupling is cooperative or adversarial. (CM4) makes the sign explicit through the $\rho + \gamma\mathcal T$ right-hand side and turns a correction-rate bound into a full persistence inequality.
3. **Unifies cooperative and adversarial regimes.** Teams persisting where individuals can't and adversarial destabilization are the same inequality viewed from opposite signs of $\gamma$, not independent results.
4. **Scope-gate made explicit.** Composite persistence requires both contraction (CM3) **and** scope-satisfaction ( #scope-composite-agent). (CM4) states this conjunction honestly; the absence of one or the other is a different failure mode (composite fails to contract vs. composite was never a composite).
5. **Symbiogenic and peer regimes connected.** The asymmetric limit shows symbiogenesis is a parameter-limit of peer coupling under a Lyapunov-weight deformation, not a discontinuous regime change requiring separate machinery.

**Why the matched-symmetric restriction is load-bearing.** Relaxing matched architectures requires per-sub-agent tiering in the sense of #form-composition-closure (Tier 1 / 2 / 3). Heterogeneous composites can still satisfy (T2) at the composite level, but the joint Lyapunov construction must be weighted per sub-agent's contraction capacity — and the weighted form loses the clean closed-form (CM2). Relaxing symmetric coupling ($\gamma_{1 \to 2} \neq \gamma_{2 \to 1}$) produces a non-symmetric matrix whose smallest eigenvalue must be computed explicitly per instance. The matched-symmetric case is the one where both sub-agent tiering and coupling symmetry collapse the Lyapunov construction to a scalar inequality — which is why closed form is available there and not elsewhere.

**Load-bearing role under `#disc-identifiability-floor` Instance 3.** The composition-layer identifiability floor (Instance 3 of `#disc-identifiability-floor`) establishes a no-go theorem: there exist pairs of coupled systems with identical marginal component-level observation distributions but opposite composite-contraction signs, so composite contraction is not in general identifiable from component data alone. Four structural escapes are named there; escape (b) — matched Tier at the composite level — is operationalized by the closed-form (CM2) in this segment. Under the floor, (CM2) is not just "a closed-form result in a special case" but **the unique broadly-available composition-contraction certificate** among the four escape routes listed. Without (CM2) or its metric-formulation generalization (CM2-M) via `#result-contraction-template`, the weakest-link bound (WL) is sign-blind and cannot distinguish the cooperative-contracting from the adversarial-destabilizing composite. This load-bearing status positions this segment as "the machinery that escapes the composition-layer floor" rather than as a closed-form curiosity in the matched-symmetric special case.

**Adjacent literature.** The joint Lyapunov construction is an instance of the classical **vector Lyapunov function** method (Matrosov 1962; Bellman 1962). The critical-mass inequality is the AAT sector-bounded analog of the **small-gain theorem for ISS systems** (Jiang–Teel–Praly 1994; Sontag 1989): in the small-gain framework, composition of two ISS systems is ISS iff the product of their gains is less than one; in AAT's sector-bounded framework, the composite persists iff the *sum* of parent reserve-rates exceeds the coupling-amplified disturbance (additive rather than multiplicative because the averaging projection averages rather than multiplies gains). In the linear-diagonal-coupling case, the matrix $A = \alpha I - \beta(I - J)$ where $J$ is the averaging operator is the graph-Laplacian-shifted form governing consensus convergence (Olfati-Saber & Murray 2004); (CM2) is consensus convergence rewritten as a persistence inequality. Relative to active inference's FEP-flow stability arguments (Friston 2019; narrowed by Aguilera et al. 2022 to small parameter regimes in NESS-density models), the present result inherits #result-sector-persistence-template's broader validity: it applies wherever (T1)–(T3) hold pairwise + (C1)/(C2) + matched symmetry, without requiring free-energy landscapes or NESS structure.

## Findings

### Strong Monotonicity as the Hinge for Legitimate Macro-Agent Coarse-Graining

**Brief:** Two coupled adaptive systems can have identical marginal observation distributions while one composite contracts and the other diverges — the difference is a single bit (the sign of the cross-coupling) that is invisible from component data alone. The matched-symmetric-Tier-1 critical-mass inequality $(\alpha - C)R \gt \rho + \gamma\mathcal T$ exposes this bit explicitly: the same inequality recovers cooperative team-persistence (where coupling helps), adversarial destabilization (where coupling hurts), and Brooks's-Law coordination collapse (where overhead $C$ exceeds correction rate $\alpha$) as signed special cases of one closed-form result. The strong-monotonicity / DA2'-inc condition picks out precisely the agent classes (Kalman, exp-family Bayes, gradient on strongly-convex losses, linear with positive-definite gain-observation product) where the inequality is exact rather than heuristic.

**Impact:** Promotes the composite sector constant in `#form-composition-closure`'s admissibility condition (A4) from a weakest-link lower bound (sign-blind, treats cooperative and adversarial coupling identically) to a derived closed form that depends explicitly on coupling sign, target-correlation $U_O$, and coordination overhead $C$. Operationalizes Instance 3 of `#disc-identifiability-floor` (composition-layer common-Lyapunov no-go via Liberzon 2003) through escape route (b): under matched Tier at the composite level, the joint Lyapunov collapses to a scalar inequality and the otherwise-unidentifiable sign bit becomes a structural input to (CM2). Within the four `#disc-identifiability-floor` Instance-3 escapes, (CM2) and its metric generalization (CM2-M) in `#result-contraction-template` are the unique broadly-available coupling-sign certificate. The asymmetric-parameter limit gives `#hyp-symbiogenic-composition`'s (S-3) autonomy-reduction a Lyapunov-weighted formulation as a smooth deformation of (CM4) rather than a discontinuous regime change.

**Novelty Claim:** *Claim novelty* on strong monotonicity as the criterion separating legitimate macro-agent coarse-graining from coexistence-only multi-agent description. The closest mathematical neighbors (Subramanian 2020; Congeduti 2020) prove bounded-loss composition under predictive compression but do not isolate a single condition whose failure flips composite contraction; the Markov-blanket line (Parr 2019; Kirchhoff 2018) discusses nested agency without a control-theoretic monotonicity criterion; the small-gain-theorem line (Jiang-Teel-Praly 1994; Sontag 1989) provides a multiplicative composition criterion under input-to-state stability rather than the additive sign-sensitive form (CM2) takes here.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| Strong monotonicity as composition-validity hinge | Subramanian, Sinha, Seraj & Mahajan 2020, "Approximate information state for approximate planning and reinforcement learning in partially observed systems" *arXiv:2010.08843* (published 2020, found 2026-04) | *closest mathematical neighbor* — proves a bridge-shape bound but does not foreground a single monotonicity-grade condition that determines whether composite description is legitimate. Per the Pillar-2 defense strategy, foregrounding strong monotonicity (DA2'-inc; equivalently (CT2)-at-$M=I$ in `#result-contraction-template`) as the hinge between stable coexistence and valid macro-agent coarse-graining is the increment ASF supplies on top of this neighbor |
| Coordination-overhead / influence loss bound | Congeduti, Mey & Oliehoek 2020, "Loss Bounds for Approximate Influence-Based Abstraction" *arXiv:2011.01788* (published 2020, found 2026-04) | *closest mathematical neighbor* — explicit bounds on value loss from approximate influence in multi-agent settings. (CM2)'s sign-sensitive RHS $\rho + \gamma\mathcal T$ encodes the same loss-vs-cooperation tradeoff that Congeduti's influence-approximation bound encodes for value, applied at the persistence-inequality layer rather than the policy-value layer |
| Composite-Lyapunov nonexistence under component-marginal data | Liberzon 2003, *Switching in Systems and Control* Theorem 2.1; Dayawansa & Martin 1999, *IEEE TAC* 44; Shorten et al. 2007 *SIAM Review* 49 (published 2003/1999/2007, found 2025-04) | *formal antecedent* — supplies the no-go theorem `#disc-identifiability-floor` Instance 3 invokes. (CM2) is the AAT escape route (b) under matched Tier at the composite level |
| Vector-Lyapunov composition | Matrosov 1962; Bellman 1962 | *formal antecedent* — joint quadratic Lyapunov $V = \tfrac12(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2)$ is a vector-Lyapunov construction; standard machinery |
| Multiplicative composition criterion via small-gain | Jiang, Teel & Praly 1994, "Small-gain theorem for ISS systems and applications" *Math. Control Signals Syst.* 7; Sontag 1989 | *partial anticipation* — same compositional-validity question, multiplicative form (gain product < 1) under input-to-state stability. (CM2)'s additive form $(\alpha - C)R \gt \rho + \gamma\mathcal T$ comes from sector-bounded correction rather than ISS; the two are different scaling regimes of the same composition-validity question, with (CM2) sharper in AAT's setting because the averaging projection averages rather than multiplies sub-agent gains |
| Negative-feedback heterogeneous extension | Slotine 2003, "Modular stability tools for distributed computation and control" *Int. J. Adapt. Control Signal Process.* 17:397–416 — Theorem 3 | *formal antecedent* — supplies (CC-feedback) used in `#result-contraction-template` to lift (CM2) to heterogeneous Tier-1M sub-agents via (CM2-M) |
| Consensus dynamics graph-Laplacian shift | Olfati-Saber & Murray 2004, "Consensus problems in networks of agents with switching topology and time-delays" *IEEE TAC* 49:1520 | *adjacent literature* — in the linear-diagonal-coupling case, (CM2) is consensus convergence rewritten as a persistence inequality; different domain framing, same mathematical object |
| Markov-blanket nested-agency at composition | Parr, da Costa & Friston 2019; Kirchhoff et al. 2018 (published 2019/2018, found 2026-04) | *conceptual precursor* — provides nested-agency framing without a control-theoretic monotonicity criterion that separates valid macro-agent coarse-graining from coexistence |

**Search Log:**

- 2026-04 (*nominally comprehensive*, via `ref/Novelty_defense_and_integration.md` Pillar 2): Per Pillar-2 defense strategy, the strong-monotonicity hinge is foregrounded as the criterion not visible in retrieved prior art. Subramanian / Congeduti provide the closest math (bounded-loss composition) without isolating a single condition whose failure flips composite legitimacy; Markov-blanket line provides nested-agency intuition without monotonicity machinery.
- 2026-04 (*targeted*, prior to comprehensive search): the small-gain-theorem line (Jiang-Teel-Praly 1994; Sontag 1989) and consensus-dynamics line (Olfati-Saber & Murray 2004) were known and cited in the segment's existing Discussion as adjacent literature. The comprehensive search added the Sub20 / Con20 closest-neighbor positioning and confirmed no surfaced paper foregrounds the strong-monotonicity hinge.
- 2026-04 (*intuition-only*, prior): expected adjacent literature was switched-systems stability (Liberzon 2003) and game-theoretic equilibrium analysis. Switched-systems hit confirmed via `#disc-identifiability-floor` Instance 3; game-theoretic side is properly the territory of `#deriv-strategic-composition`, scope-separated.

## Working Notes

- **Partial-derivation: heterogeneous-architecture dyad.** The clean closed form (CM2) relies on matched sub-agent architectures collapsing the joint Lyapunov candidate to a scalar inequality. A natural next move is the $(A_1, A_2)$ = (Tier 1, Tier 2) case: weighted Lyapunov $V_\mu = \tfrac12(\lVert\delta_1\rVert^2 + \mu(\delta_2)\lVert\delta_2\rVert^2)$ with the weight a function of agent 2's local contraction modulus. Likely produces a range-valued (not closed-form) critical-mass inequality. Defer until a specific Tier-mismatch composite motivates it.
- **Sharpen (UO-mult).** Upgrading $\gamma(U_O) = -\gamma_{\max}U_O$ from discussion-grade to derived requires an action-space inner-product analysis: define the environment's action-coupling operator, show that LQR-linear policies produce cross-actions with inner product proportional to target correlation, and pin down $\gamma_{\max}$ in terms of the quadratic objective's Hessian and the environment's coupling gain. This is mechanical but non-trivial; natural home is an extension to #result-unity-closure-mapping's linear-Gaussian closed-form section.
- **Close (S-2) function transfer in #hyp-symbiogenic-composition.** The asymmetric-limit result here identifies the Lyapunov-weight limit as (S-3) autonomy reduction but leaves (S-2) function transfer unformalized. A complete symbiogenic-limit theorem requires specifying what happens to agent 1's state space when it inherits structure from agent 2 — how $\mathcal F(M_e, \Sigma_e)$ lands in $M_h$. This is flagged in #hyp-symbiogenic-composition's Working Notes and is a prerequisite for promoting the limit result to derived.
- **Connection to Miller-2022 extreme-transition motif.** The asymmetric-limit smooth-deformation result contrasts with extreme-transition dynamics (pending dedicated Section III segments) where population-level niche-replacement proceeds discontinuously. The two mechanisms co-exist and are not reducible to one another; the weighted-Lyapunov analysis is specific to bilateral asymmetric integration.
- **$N$-agent scaling.** The conjunction generalization "composite persists iff (CM4) holds pairwise for all $i, j$" is probably too strong — pairwise cooperative effects can compose super-additively in particular topologies (ensemble filters, committee agents). A sharper $N$-agent theorem requires a graph-structured Lyapunov construction. See `spikes/spike-composition-scaling-N.md` for a framing of the question.


---

