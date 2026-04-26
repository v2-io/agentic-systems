# AAD: Adaptation and Actuation Dynamics

The mathematical core of the [Agentic Systems](../OUTLINE.md) research framework. AAD formalizes the adaptive cycle — one complete traversal of the agent-environment feedback loop — as the fundamental unit of analysis for adaptive, purposeful agents under uncertainty.

**Working draft.** The argument laid out claim by claim. The ordering is the current best linearization of the dependency DAG; it will change as the theory develops. Slugs are the stable identities. Treat this as a living proof sketch, not a specification.

**Reading AAD.** At the integration level AAD connects control theory, causal inference, information theory, and agent architecture under a common formalism. At the distinctive level AAD is an *epistemic architecture for bounded correction under decomposed disturbance*. Three meta-segments form AAD's cross-sectional structure: `#disc-separability-pattern` (positive half — separable core / structured repair / general open, across six ladders of increasing difficulty), `#disc-identifiability-floor` (negative half — structural no-go results derived from external information-theoretic theorems, each naming a unique escape via AAD machinery), and `#disc-additive-coordinate-forcing` (constructive half — Cauchy-functional-equation arguments on AAD-internally-motivated additivity axioms force logarithmic coordinates at chain, divergence, and update layers). Together they name what the theory covers, what it structurally cannot reach without information augmentation, and how its distinctive forcing moves work. Reading any segment through all three lenses surfaces what makes it load-bearing: what separability regime it sits in, what floors it abuts, and what coordinate (if any) is forced by an AAD-internal axiom.

**On mathematical precision.** The theory's relationship to formalism varies by section and is expected to. Section I (adaptive systems) is the most mathematically locked down — the persistence machinery, mismatch dynamics, and gain structure have clean derivations and Lyapunov proofs. Section II (purposeful agents) has an exact diagnostic core whose inferential force scales with the continuation convention hierarchy ( #def-value-object): from local heuristics (C1/one-step) through moderate-horizon diagnostics (C2/receding-horizon) to global conclusions (C3/Bellman). The strategy layer now has a proved DAG structure (acyclicity from temporal ordering, Markov property from the CMC theorem under causal sufficiency) and a first-class treatment of correlated failure via the Correlation Hierarchy ( #def-strategy-dag). Both the diagnostic core and the strategy layer depend on the directed-separation scope condition ( #der-directed-separation): **Section II's exact results apply to Class 1 (modular) agents.** The scope restriction to modular agents is detailed in the Section II preamble below. Section III (composition) has promising structure built on the Section I Lyapunov machinery but depends on admissibility choices that are formulated, not derived, and a bridge lemma that requires a contraction assumption beyond the stated admissibility constraints. This gradient — from exact core through conditionally exact architecture to open formulation — is the expected arc. The goal is to describe agentic systems, not to produce a purely mathematical artifact. We pursue mathematical precision when it yields genuine insight (the persistence condition, the CMC-based Markov proof, the convention hierarchy monotonicity) and settle for principled sketches when the insight is structural rather than quantitative (the strategy-revision loop, the composition admissibility). The boundaries between these regimes are fluid and still being discovered.

**Scope:** AAD covers the general theory of adaptive systems (Section I), actuated/purposeful agents (Section II), and agent composition (Section III). Domain instantiations (software: [`02-tst-core/`](../02-tst-core/OUTLINE.md)), logogenic agents ([`03-logogenic-agents/`](../03-logogenic-agents/OUTLINE.md)), and logozoetic agents ([`04-logozoetic-agents/`](../04-logozoetic-agents/OUTLINE.md)) are part of the broader Agentic Systems framework, grounded by AAD but developed independently.

See [`FORMAT.md`](../FORMAT.md) for segment file conventions. See [`NOTATION.md`](../NOTATION.md) for symbols, conventions, and units.

Every slug is linked to its intended `src/{slug}.md` file, even when that file doesn't exist yet (`missing` or `old` stage). This is deliberate — the links serve as stable intent markers so the only ongoing maintenance is updating the Stage column. A `missing` link means no file exists; an `old` link means the content lives in a corresponding `src/old-*` source file awaiting conversion. Segments may also contain forward references (`#slug-name`) to not-yet-written segments; these are intentional dependency markers, not broken links.

![Full dependency graph](src/img/dep-graph-full.svg)


---

## I. Adaptive Systems Under Uncertainty

*Scope: Any system consisting of an agent coupled to an environment through observation and action channels, where the environment is not fully observable. This is the general case — thermostats through commanders. The claims in this section are largely drawn from TFT (TF-01 through TF-11, Appendix A), which developed the adaptive-systems foundation that AAD subsumes.*

![Dependency Graph](src/img/dep-graph-section-I.svg)

| §   | Type        | N   | Tag                                                                        | Claim                                          | Stage           |
| --- | ----------- | --- | -------------------------------------------------------------------------- | ---------------------------------------------- | --------------- |
| I   | Definition  |     | [#def-agent-environment](src/def-agent-environment.md)                             | Agent-environment boundary                     | deps-verified   |
| I   | Definition  |     | [#def-observation-function](src/def-observation-function.md)                       | Lossy, noisy observations                      | deps-verified   |
| I   | Definition  |     | [#def-action-transition](src/def-action-transition.md)                             | Actions affect environment                     | deps-verified   |
| I   | Scope       |     | [#scope-adaptive-system](src/scope-adaptive-system.md)                     | Broadest AAD scope: observe under uncertainty  | claims-verified |
| I   | Scope       |     | [#scope-agency](src/scope-agency.md)                                       | Narrows to action with Pearl-level-2 contrast  | claims-verified |
| I   | Postulate   |     | [#post-composition-consistency](src/post-composition-consistency.md)                 | Agent/subagent scale invariance                | deps-verified   |
| I   | Definition  |     | [#def-chronica](src/def-chronica.md)                                               | Complete interaction history                   | deps-verified   |
| I   | Postulate   |     | [#post-causal-structure](src/post-causal-structure.md)                               | Irreducible causal structure                   | deps-verified   |
| I   | Definition  |     | [#def-pearl-causal-hierarchy](src/def-pearl-causal-hierarchy.md)                   | Three levels of causal reasoning               | deps-verified   |
| I   | Formulation |     | [#form-agent-model](src/form-agent-model.md)                                         | Compressed history as state                    | deps-verified   |
| I   | Formulation |     | [#form-information-bottleneck](src/form-information-bottleneck.md)                   | Optimal model compression                      | draft           |
| I   | Definition  |     | [#def-model-sufficiency](src/def-model-sufficiency.md)                             | Predictive information retained                | deps-verified   |
| I   | Definition  |     | [#def-model-class-fitness](src/def-model-class-fitness.md)                         | Best achievable sufficiency                    | deps-verified   |
| I   | Formulation |     | [#form-event-driven-dynamics](src/form-event-driven-dynamics.md)                     | Events in continuous time                      | deps-verified   |
| I   | Derived     |     | [#der-recursive-update](src/der-recursive-update.md)                               | State updates must be recursive                | claims-verified |
| I   | Derived     |     | [#der-action-selection](src/der-action-selection.md)                               | Action as function of model                    | deps-verified   |
| I   | Definition  |     | [#def-mismatch-signal](src/def-mismatch-signal.md)                                 | Prediction error signal                        | deps-verified   |
| I   | Result      |     | [#result-mismatch-decomposition](src/result-mismatch-decomposition.md)                   | Model error + obs noise                        | claims-verified |
| I   | Empirical   |     | [#emp-update-gain](src/emp-update-gain.md)                                         | Optimal update weighting                       | claims-verified |
| I   | Definition  |     | [#def-causal-information-yield](src/def-causal-information-yield.md)               | Information from interventions                 | deps-verified   |
| I   | Definition  |     | [#def-adaptive-tempo](src/def-adaptive-tempo.md)                                   | Rate of useful info acquisition                | claims-verified |
| I   | Hypothesis  |     | [#hyp-mismatch-dynamics](src/hyp-mismatch-dynamics.md)                             | Mismatch evolution ODE                         | deps-verified   |
| I   | Derived     |     | [#der-deliberation-cost](src/der-deliberation-cost.md)                             | Think vs act tradeoff                          | claims-verified |
| I   | Derived     |     | [#der-gain-sector-bridge](src/der-gain-sector-bridge.md)                           | Gain + directional fidelity → sector condition | claims-verified |
| I   | Result      |     | [#result-sector-condition-stability](src/result-sector-condition-stability.md)           | Nonlinear persistence (Lyapunov)               | claims-verified |
| I   | Result      |     | [#result-persistence-condition](src/result-persistence-condition.md)                     | Bounded mismatch condition                     | claims-verified |
| I   | Result      |     | [#result-structural-adaptation-necessity](src/result-structural-adaptation-necessity.md) | When parametric update fails                   | claims-verified |
| I   | Derived     |     | [#der-temporal-nesting](src/der-temporal-nesting.md)                               | Timescale stratification                       | deps-verified   |
| I   | Formulation |     | [#form-consolidation-dynamics](src/form-consolidation-dynamics.md)                   | Offline regime of $g_M$ driven by replayed/pseudo-events with IB-gap-reduction objective; stability-plasticity feasibility window; necessity under sub-state factorization + bounded per-event budget | draft |
| I   | Discussion  |     | [#scope-agent-identity](src/scope-agent-identity.md)                                   | Non-forkable causal trajectory                 | deps-verified   |


---

## II. Actuated Adaptation: Agentic Systems

*Scope: agents that not only track reality but aim at something — Section II adds objectives and strategy alongside the reality model. This is the **actuation** half of *Adaptation and Actuation Dynamics*: Section I develops adaptive systems in general; Section II develops the goal-directed layer built on top.*

***Headline contribution.** Section II's distinctive results are: the satisfaction gap / control regret split ( #def-satisfaction-gap, #def-control-regret) with the convention hierarchy ( #def-value-object) governing the inferential force of each diagnostic from local (C1) through global (C3); the $G_t$ complexity bound (in #der-orient-cascade); the graph-structure uniqueness argument with CMC-based Markov property ( #deriv-graph-structure-uniqueness); and the survival classification ( #result-section-ii-survival) showing that Section II's definitional and structural architecture transfers exactly to fully-coupled (Class 2) agents in 16/24 cases, with the remaining results either approximating with bounded error (5/24) or naming the precise modification required (2/24, plus 1 boundary-defining failure). The Class-2 bias bound underlying the approximate-survival category is now a conditional theorem under named sub-scopes ( #deriv-bias-bound), not order-of-magnitude guidance. The reach is wider than the most-restrictive scope condition suggests; the lattice below names exactly which results live where.*

***Scope lattice.** Section II's results sit at different points in a stacked lattice of scope conditions, not a single uniform scope. Reading inward from the broadest:*

*1. **Adaptive scope** ( #scope-adaptive-system): observation under uncertainty. Section I machinery applies here without further restriction.*

*2. **Agency scope** ( #scope-agency): adaptive + at least binary action choice + at least one action with Pearl-level-2 causal contrast. Section II's definitional architecture — $X_t = (M_t, G_t)$, $G_t = (O_t, \Sigma_t)$, the agent spectrum — is already non-vacuous here.*

*3. **Learning-agent scope** ( #der-causal-hierarchy-requirement Scope Narrowing): agency + the agent must acquire or refine its interventional structure during operation. Pre-compiled controllers (PID, LQR, hardcoded reactive policies) sit in agency scope but outside learning-agent scope — their causal mapping was supplied by a designer with external Level 2 access. Most Section II dynamics — the orient cascade, edge-update via gain, strategic calibration, the satisfaction-gap / control-regret diagnostic loop — operate in learning-agent scope.*

*4. **Class 1 (modular) architecture**: directed separation ( #der-directed-separation) holds by construction — epistemic processing $f_M$ has no causal path from $G_t$. Examples: Kalman filter + LQR, modular RL with separate world model, military intelligence separated from operations, tool-use AI agents with separate perception and planning modules. **Class 2 (fully merged) agents** — including transformer-based LLMs where attention processes goals and observations together — lie outside Class 1. Class 3 (partially modular) sits between, with coupling quantified by $\kappa_{\text{processing}}$ ( #der-directed-separation).*

*The lattice stacks. Kalman + LQR is in Class 1 (modular) but outside learning-agent scope (the control law is pre-computed); a designer applying Section II's diagnostic core to Kalman + LQR is using only the architecture-survival half, not the learning-dependent dynamics. The orient cascade, in particular, requires both Class 1 modularity (for sequential resolution) and learning-agent scope (for $\Sigma_t$ revision to be meaningful). The bias-bound theorem and survival classification ( #deriv-bias-bound, #result-section-ii-survival) trace exactly which Section II results require which lattice entries — see those segments for the per-result classification.*

*Section III's composite-agent scope sits below this lattice as a fifth tier and inherits the Class-1-sub-agents → Class-3-composite refinement of directed separation ( #hyp-directed-separation-under-composition, `#deriv-strategic-composition`).*

***Section I machinery applies regardless of architecture.** Adaptive dynamics on the epistemic substate $M_t$ — mismatch, gain, tempo, persistence — operate independently of how $f_M$ relates to $G_t$. Class 2 agents are adaptive systems in the Section I sense; what they lose is the clean factorization that gives Section II's coupled-formulation results their definitional simplicity. The coupled formulation Class 2 agents require is the subject of [`03-logogenic-agents/`](../03-logogenic-agents/OUTLINE.md), which inherits Section II's surviving 16/24 architecture and adds the additional machinery ( #scope-observation-ambiguity-modulation, ambiguity-gated bias bounds) that the coupled regime calls for.*

*The derivation chain for this section is mature (see `msc/spike-v3-purposeful-agent.md`). Much of it provides better justification and epistemic labels for architecture that already existed; the headline contribution above names what is genuinely novel.*

*"If a man knows not to which port he sails, no wind is favorable." — Seneca*

![Dependency Graph](src/img/dep-graph-section-II.svg)

| §   | Type            | N   | Tag                                                                                    | Claim                                                            | Stage |
| --- | --------------- | --- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ----- |
| II  | Definition      |     | [#def-agent-spectrum](src/def-agent-spectrum.md)                                               | ±model × ±objective quadrants                                    | deps-verified |
| II  | Formulation     |     | [#form-complete-agent-state](src/form-complete-agent-state.md)                                   | $X_t = (M_t, G_t)$                                               | claims-verified |
| II  | Derived + Scope |     | [#der-directed-separation](src/der-directed-separation.md)                                     | Epistemic update is goal-blind                                   | draft |
| II  | Formulation     |     | [#form-objective-functional](src/form-objective-functional.md)                                   | $O_t$ parametrizes value                                         | deps-verified |
| II  | Definition      |     | [#def-value-object](src/def-value-object.md)                                                   | Horizon/policy-conditioned value                                 | deps-verified |
| II  | Definition      |     | [#def-strategy-dimension](src/def-strategy-dimension.md)                                       | $G_t = (O_t, \Sigma_t)$ split                                    | deps-verified |
| II  | Derived + Scope |     | [#der-causal-hierarchy-requirement](src/der-causal-hierarchy-requirement.md)                   | Level 2 needed for planning                                      | deps-verified |
| II  | Derived         |     | [#der-loop-interventional-access](src/der-loop-interventional-access.md)                       | Feedback loop → Level 2 data                                     | draft |
| II  | Scope           |     | [#scope-ciy-observational-proxy](src/scope-ciy-observational-proxy.md)                             | When CIY is estimable from observational data                    | draft |
| II  | Discussion      |     | [#disc-ciy-unified-objective](src/disc-ciy-unified-objective.md)                                 | Joint exploitation-exploration objective                         | draft |
| II  | Normative       |     | [#norm-explicit-strategy-condition](src/norm-explicit-strategy-condition.md)                     | When planning beats exploring                                    | draft |
| II  | Derived         |     | [#der-chain-confidence-decay](src/der-chain-confidence-decay.md)                               | Log-confidence additive in depth                                 | claims-verified |
| II  | Scope           |     | [#scope-and-or](src/scope-and-or.md)                                                   | Conjunctive/disjunctive scope                                    | draft |
| II  | Definition      |     | [#def-strategy-dag](src/def-strategy-dag.md)                                                   | Strategy as probabilistic DAG                                    | draft |
| II  | Definition      |     | [#def-satisfaction-gap](src/def-satisfaction-gap.md)                                           | Ideal vs best achievable                                         | draft |
| II  | Definition      |     | [#def-control-regret](src/def-control-regret.md)                                               | Best achievable vs current                                       | draft |
| II  | Definition      |     | [#def-strategic-calibration](src/def-strategic-calibration.md)                                 | Edge residuals ( #disc-credit-assignment-boundary)                    | draft |
| II  | Derived         |     | [#der-causal-insufficiency-detection](src/der-causal-insufficiency-detection.md)               | Detecting latent common causes from structured residuals + interventional localization | draft |
| II  | Derived         |     | [#der-observability-dominance](src/der-observability-dominance.md)                             | Unobservable edges freeze                                        | draft |
| II  | Hypothesis      |     | [#hyp-edge-update-via-gain](src/hyp-edge-update-via-gain.md)                                   | Gain extends to strategy edges                                   | draft |
| II  | Scope           |     | [#scope-edge-update-causal-validity](src/scope-edge-update-causal-validity.md)                     | When edge updates are causally valid                             | deps-verified |
| II  | Discussion      |     | [#disc-credit-assignment-boundary](src/disc-credit-assignment-boundary.md)                       | Tractable/intractable boundary; design requirement               | draft |
| II  | Formulation     |     | [#form-structural-change-as-parametric-limit](src/form-structural-change-as-parametric-limit.md) | Pruning/grafting as continuous                                   | draft |
| II  | Definition      |     | [#def-strategic-tempo](src/def-strategic-tempo.md)                                             | Rate of useful $\Sigma_t$ revision                               | draft |
| II  | Formulation     |     | [#form-strategy-complexity-cost](src/form-strategy-complexity-cost.md)                           | Complexity cost of maintaining $\Sigma_t$ (IB/MDL for DAGs)      | draft |
| II  | Proposed schema |     | [#schema-strategy-persistence](src/schema-strategy-persistence.md)                     | Sector conditions for $\Sigma_t$                                 | draft |
| II  | Derived         |     | [#der-orient-cascade](src/der-orient-cascade.md)                                               | Resolution order by info dep                                     | deps-verified |
| II  | Discussion      |     | [#disc-exploit-explore-deliberate](src/disc-exploit-explore-deliberate.md)                       | Three-way exploit/explore/deliberate: extended deliberation threshold + conceptual framing | draft |


---

## III. Agentic Composites

*Scope: multiple agents interacting through a shared environment, or equivalently, the internal structure of composite agents. The composition postulate ( #post-composition-consistency) requires that the theory apply at every level of description where the scope condition is met. This section develops what "applies at every level" means formally (the composition closure criterion, which requires an additional contraction assumption beyond Section I's sector condition), what happens when composition is imperfect, and what the dynamics of inter-agent interaction look like.*

*Correlated observations as default; independence as the special case requiring justification. Adversarial dynamics are one end of a teleological unity spectrum, not a separate theory.*

*Three primary sources: the simulation-validated adversarial dynamics from TFT (TF-11/Appendix F, track-b simulations); the composition spike (`msc/spike-agent-composition.md`) which derives composition consistency from the scope condition's level-independence; and Miller's Coevolving Automata Model (Ex Machina, 2022), which provides constructive mechanisms for composition dynamics — how composites form, undergo phase transitions, and restructure through neutral drift and niche creation. Agent opacity ($H_b$) is adopted from Hafez et al. (2026).*

![Dependency Graph](src/img/dep-graph-section-III.svg)

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| III | Scope | | [#scope-multi-agent](src/scope-multi-agent.md) | Multiple agents, shared env | draft |
| III | Scope | | [#scope-composite-agent](src/scope-composite-agent.md) | Teleological alignment required for composite-agent status | draft |
| III | Hypothesis | | [#hyp-symbiogenic-composition](src/hyp-symbiogenic-composition.md) | Asymmetric absorption mechanism: host integrates endosymbiont; $U_O$ crosses scope threshold from below | draft |
| III | Formulation | | [#form-composition-closure](src/form-composition-closure.md) | Composite agent via closure defect | draft |
| III | Sketch | | [#der-tempo-composition](src/der-tempo-composition.md) | Sub-additive tempo inequality | draft |
| III | Hypothesis | | [#hyp-directed-separation-under-composition](src/hyp-directed-separation-under-composition.md) | Goal-blindness survives iff routing is goal-blind (two cases) | draft |
| III | Discussion | | [#def-unity-dimensions](src/def-unity-dimensions.md) | 4 dimensions of coherence | draft |
| III | Result | | [#result-unity-closure-mapping](src/result-unity-closure-mapping.md) | Unity parametrizes rate-distortion curves for closure defect; two-axis structure with update heterogeneity | draft |
| III | Definition + Discussion | | [#def-shared-intent](src/def-shared-intent.md) | IB-compressed purpose | draft |
| III | Hypothesis | | [#hyp-auftragstaktik-principle](src/hyp-auftragstaktik-principle.md) | Prioritize objective sharing | draft |
| III | Hypothesis | | [#hyp-communication-gain](src/hyp-communication-gain.md) | Trust-weighted update gain for inter-agent channels | draft |
| III | Derived | | [#der-team-persistence](src/der-team-persistence.md) | Composite persistence condition | draft |
| III | Derived | | [#der-adversarial-destabilization](src/der-adversarial-destabilization.md) | Inside opponent's loop; includes effects spiral corollary | draft |
| III | Derived | | [#der-interaction-channel-classification](src/der-interaction-channel-classification.md) | Recipient-side four-regime classification (Informative / magnitude-shock / structural-shock / ambient-noise) with three independent boundaries in AAD-native quantities; regime-typed $\rho_B^{\text{eff}}$ decomposition with signed Regime-I term; Kalman-over-Kalman derivation | draft |
| III | Result | | [#result-adversarial-tempo-advantage](src/result-adversarial-tempo-advantage.md) | Superlinear tempo advantage | draft |
| III | Derivation | | [#deriv-strategic-composition](src/deriv-strategic-composition.md) | Equilibrium-convergence framing for partially-opposing $O_t^{(i)}$; A2'-analog derived under potential-game (Monderer-Shapley 1996) and monotone-game (Rosen 1965) conditions; sub-scope α'/β' partition; formal home for the effects spiral (joint-Jacobian eigenvalue condition); Class-1-sub-agents → Class-3-composite refinement of `#der-directed-separation`; mechanism-design impossibility candidate for 4th `#disc-identifiability-floor` instance | draft |
| III | Derived | | [#der-agent-opacity](src/der-agent-opacity.md) | Backward predictive uncertainty $H_b^{A\mid B}(t, \tau) := H(a_{A,t+\tau} \mid \mathcal F_B^t)$ as dual of observation quality; sign-flip via signed coupling (cooperative requires predictability; adversarial uses opacity as mechanism); emitter-side four-regime classification dual to `#der-interaction-channel-classification`; 16-cell emitter-recipient composition operationalizes adversarial-edge-targeting with closed-form arg-max | draft |
| III | Observation | | [#result-adversarial-exponent-regimes](src/result-adversarial-exponent-regimes.md) | $\alpha = 2, 3/2, \text{or } {\sim}1$ | draft |
| III | Observation | | [#obs-gates-advantage](src/obs-gates-advantage.md) | Obs noise gates advantage | draft |
| III | Result | | [#result-per-dimension-persistence](src/result-per-dimension-persistence.md) | Weak dimension is bottleneck | draft |
| | --GAP-- | | | Latent structural diversity: variation in correction architectures invisible to persistence analysis, consequential under regime change | |
| | --GAP-- | | | Endogenous coupling: γ as function of population composition, not exogenous parameter; coupling emergence threshold | |
| | --GAP-- | | | Composition transition dynamics: epochal stability → latent diversification → niche emergence → cascading restructuring → re-equilibration (adopts Miller 2022's extreme transition motif) | |
| | --GAP-- | | | Computational thresholds for social behavior: minimum agent complexity and interaction depth for composition dynamics (adopts Miller 2022's ICE framework; grounds #form-strategy-complexity-cost) | |


---

## Appendices: Details

*Supporting material: derivations, sketches, simulation results, and operationalization procedures backing the main theory claims.*

| §   | Type       | N   | Tag                                                                    | Claim                                                                 | Stage   |
| --- | ---------- | --- | ---------------------------------------------------------------------- | --------------------------------------------------------------------- | ------- |
| A   | Derivation |     | [#deriv-sector-condition](src/deriv-sector-condition.md)     | Lyapunov derivations for bounded mismatch and adaptive reserve        | claims-verified |
| A   | Result     |     | [#result-sector-persistence-template](src/result-sector-persistence-template.md)     | Abstract sector-persistence template; six AAD results as instances    | draft   |
| A   | Derivation |     | [#deriv-persistence-cost](src/deriv-persistence-cost.md)                           | Sustained information rate $\dot R \geq n\alpha/2$ nats/time to maintain sector-persistence ultimate bound under Model S + Gaussian-OU; Kalman-Bucy saturates (Mitter-Newton 2005); channel-capacity floor $C \geq \mathcal T/2$ | draft |
| A   | Derivation |     | [#deriv-critical-mass-composition](src/deriv-critical-mass-composition.md)         | Closed-form composite sector-constant for symmetric-matched-Tier-1 dyad; (CM2)/(CM4) derive $\alpha_c$ from parent $(\alpha, R, \gamma, U_O, C)$; subsumes weakest-link bound; asymmetric limit formalizes #hyp-symbiogenic-composition (S-3) | draft |
| A   | Derivation |     | [#deriv-gain-sector](src/deriv-gain-sector.md)               | Gain-sector bridge proofs: Kalman, gradient equivalence, verification | deps-verified |
| A   | Derivation |     | [#deriv-recursive-update](src/deriv-recursive-update.md)     | Uniqueness derivation via three constraints + counterexamples         | claims-verified |
| A   | Sketch     |     | [#sketch-multi-timescale-stability](src/sketch-multi-timescale-stability.md)         | N-timescale singular perturbation sketch                              | draft   |
| A   | Derivation |     | [#deriv-discrete-sector-condition](src/deriv-discrete-sector-condition.md)         | Discrete-time Props DA.1, DA.1S, DA.2; fluid limit; GA-5 closed       | draft   |
| A   | Detail     |     | [#detail-linear-ode-approximation](src/detail-linear-ode-approximation.md)           | Pedagogical linear mismatch ODE                                       | draft   |
| A   | Derivation |     | [#deriv-graph-structure-uniqueness](src/deriv-graph-structure-uniqueness.md)       | 4 postulates + causal sufficiency → DAG with Markov property (CMC theorem)  | deps-verified |
| A   | Derivation |     | [#deriv-strategic-dynamics](src/deriv-strategic-dynamics.md) | Sector condition verification for strategy edges (5 cases + bridge)   | draft   |
| A   | Derivation |     | [#deriv-strategy-cost-regret-bound](src/deriv-strategy-cost-regret-bound.md)       | Regret-bound derivation of the strategy-cost KL direction ($\pi^\ast$-first forced; reverse-KL canonical in admissible family) | draft |
| A   | Derivation |     | [#deriv-edge-update-natural-parameter](src/deriv-edge-update-natural-parameter.md) | Log-odds as unique additive-evidence coordinate for edge credences (evidential-additivity axiom; update-level analog of #der-chain-confidence-decay) | draft |
| A   | Derivation |     | [#deriv-adaptive-gain-dynamics](src/deriv-adaptive-gain-dynamics.md)               | A2' under adaptive gain: meta-gain conditions (MG-1)–(MG-4) + augmented-state Lyapunov compose #result-sector-persistence-template twice; refines A2' sub-scope partition into $\alpha_1$ (fixed-gain) / $\alpha_2$ (adaptive-gain under MG-1-MG-4) / $\beta$ | draft |
| A   | Derivation |     | [#internal-external-decomposition](src/internal-external-decomposition.md)           | Log-additive split of viability into internal-operational health and environmental affordance | draft |
| A   | Derivation |     | [#deriv-detection-latency](src/deriv-detection-latency.md)                         | R1 within-class regime-change detection latency $\mathbb E[T_{\text{detect}}] = \Omega((n_{\min}+1)/\varepsilon)$ from #deriv-edge-update-natural-parameter log-odds forcing; sharpens #schema-strategy-persistence forgetting prerequisite to "required for bounded detection latency" | draft |
| A   | Discussion |     | [#disc-independence-audit](src/disc-independence-audit.md)                       | Six load-bearing independence assumptions with failure regimes + repairs | draft |
| A   | Discussion |     | [#disc-approximation-tiering](src/disc-approximation-tiering.md)                 | Meta-pattern: L0/L1/L2, C1/C2/C3, Tier 1/2/3 as common structure      | draft |
| A   | Discussion |     | [#disc-compression-operations](src/disc-compression-operations.md)               | Shared IB shape across $M_t$, $\Sigma_t$, shared intent, $\Lambda$ (P1); $\Sigma_t$ source reformulated, (P1) as IB Lagrangian-dual | draft |
| A   | Discussion |     | [#disc-identifiability-floor](src/disc-identifiability-floor.md)                 | Meta-pattern: structural no-go results from external info-theoretic theorems (CHT, Cramér-Rao, Liberzon common-Lyapunov-nonexistence); three instances (on-policy L0-detection, L1' mixture-identifiability, composite-contraction-from-component-data) | draft |
| A   | Discussion |     | [#disc-separability-pattern](src/disc-separability-pattern.md)                   | Meta-pattern: separable-core / structured-repair / general-open across seven ladders (correlation, convention, architecture, contraction, identification, scope, A2'-scope via #result-contraction-template); positive-half complement to #disc-identifiability-floor | draft |
| A   | Discussion |     | [#disc-additive-coordinate-forcing](src/disc-additive-coordinate-forcing.md)     | Meta-pattern: AAD forces coordinates via uniqueness theorems on AAD-internally-motivated axioms at four layers (chain-log-additive-identity; divergence-reverse-KL and update-log-odds via Cauchy-FE; metric-Fisher via (PI)/Čencov-invariance); 1-anchor-plus-3-theorem structure with Lyapunov and IB Lagrangian as adjacent family members | draft |
| A   | Result     |     | [#result-contraction-template](src/result-contraction-template.md)                   | Contraction-metric generalization of #result-sector-persistence-template (Lohmiller-Slotine 1998); 5 α-class promotions incl. linear-Hurwitz-non-symmetric and PID-bounded-plant; topology-indexed compositional closures (parallel/cascade/feedback) + heterogeneous (CM2-M); DA2'-inc ≡ (CT2) at M=I; (PI)/Čencov forces Fisher-metric cases AAD-internally | draft |
| A   | Derivation |     | [#deriv-variational-sector-condition](src/deriv-variational-sector-condition.md)   | ε-fidelity B1 under $\mathrm{KL}(q\Vert p) \leq \varepsilon$ via Pinsker's inequality; $O(\sqrt\varepsilon)$ sector-constant degradation; Regime A/B decomposition; sub-scope α' tier for controlled-KL variational agents; natural-gradient VI recovers full α | draft |
| A   | Derivation |     | [#deriv-l1-update-bias](src/deriv-l1-update-bias.md)                               | Closed-form bias formula $B_k(\rho)$ for log-odds update under L1' common cause; Cramér-Rao floor under forgetting; dual forgetting-rate requirement; Monte Carlo validation; quantitative numerical-floor companion to `#disc-identifiability-floor` Instance 2 | draft |
| A   | Derivation |     | [#deriv-fisher-whitened-update-rule](src/deriv-fisher-whitened-update-rule.md)     | Fisher-whitened edge update under correlated evidence; AAD-internal derivation under (PI)/Čencov axiom; log-odds angle ≤ 45° at any finite ρ (direction preserved, magnitude degraded by √(1−r²)); sub-scope α₃ and connection to `#deriv-adaptive-gain-dynamics` as degenerate meta-gain instance | draft |
| A   | Derivation |     | [#deriv-bias-bound](src/deriv-bias-bound.md)                 | Class-2 observation-ambiguity bias-bound constant $C$; Track 1 transport-inequality ($C_{W_2}^2 = 2L_{\text{post}}^2/\rho_{\text{LSI}}$ linear in $I$ under LSI + Lipschitz-posterior); Track 2 Fisher-Rao ($C_{FR} = \sqrt{2}$ universal dimension-free under (PI)+Čencov + small-$I$); no-go for universal $C$ under Euclidean-parameter norm justifies (PI) as load-bearing | draft |
| A   | Detail     |     | [#obs-simulation-results](src/obs-simulation-results.md)                       | 6 variants validating claims                                          | draft   |


---

## Appendices: Operational Domains

*Operational-specific appendices and end-to-end domain instantiations validating the theory chain.*

| §   | Type           | N   | Tag                                                    | Claim                                            | Stage |
| --- | -------------- | --- | ------------------------------------------------------ | ------------------------------------------------ | ----- |
| B   | Detail         |     | [#detail-operationalization](src/detail-operationalization.md)       | Estimation procedures for AAD quantities         | draft |
| B   | Worked example |     | [#example-kalman](src/example-kalman.md) | End-to-end Kalman instantiation (exact)          | draft |
| B   | Worked example |     | [#example-bandit](src/example-bandit.md) | End-to-end RL bandit instantiation (approximate) | draft |
| B   | Worked example |     | [#example-strategy](src/example-strategy.md) | Section II strategy DAG instantiation (3-arm bandit) | draft |
| B   | Worked example |     | [#example-L1](src/example-L1.md) | L1 augmented DAG: common-cause node, sector condition, L0/L1 comparison | draft |
| B   | Worked example |     | [#worked-example-cam](src/worked-example-cam.md) | Coevolving automata (Miller 2022): AAD ↔ Moore machine mapping, meta-machine as ε*=0 composition, simplest adaptive agent | missing |
