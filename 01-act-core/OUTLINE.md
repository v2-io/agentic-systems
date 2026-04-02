# ACT: Agentic Cycle Theory

The mathematical core of the [Agentic Systems](../OUTLINE.md) research framework. ACT formalizes the adaptive cycle — one complete traversal of the agent-environment feedback loop — as the fundamental unit of analysis for adaptive, purposeful agents under uncertainty.

**Working draft.** The argument laid out claim by claim. The ordering is the current best linearization of the dependency DAG; it will change as the theory develops. Slugs are the stable identities. Treat this as a living proof sketch, not a specification.

**On mathematical precision.** The theory's relationship to formalism varies by section and is expected to. Section I (adaptive systems) is the most mathematically locked down — the persistence machinery, mismatch dynamics, and gain structure have clean derivations and Lyapunov proofs. Section II (purposeful agents) has an exact diagnostic core (satisfaction gap, control regret, orient-cascade ordering) but the strategy-revision machinery remains a principled design sketch with open pieces. Section III (composition) has promising structure built on the Section I Lyapunov machinery but depends on admissibility choices that are formulated, not derived. This gradient — from exact core through principled architecture to open formulation — is the expected arc. The goal is to describe agentic systems, not to produce a purely mathematical artifact. We pursue mathematical precision when it yields genuine insight (the persistence condition, the acyclicity derivation, the architectural classification) and settle for principled sketches when the insight is structural rather than quantitative (the strategy-revision loop, the composition admissibility). The boundaries between these regimes are fluid and still being discovered.

**Scope:** ACT covers the general theory of adaptive systems (Section I), actuated/purposeful agents (Section II), and agent composition (Section III). Domain instantiations (software: [`02-tst-core/`](../02-tst-core/OUTLINE.md)), logogenic agents ([`03-logogenic-agents/`](../03-logogenic-agents/OUTLINE.md)), and logozoetic agents ([`04-logozoetic-agents/`](../04-logozoetic-agents/OUTLINE.md)) are part of the broader Agentic Systems framework, grounded by ACT but developed independently.

See [`FORMAT.md`](../FORMAT.md) for segment file conventions. See [`NOTATION.md`](../NOTATION.md) for symbols, conventions, and units.

Every slug is linked to its intended `src/{slug}.md` file, even when that file doesn't exist yet (`missing` or `old` stage). This is deliberate — the links serve as stable intent markers so the only ongoing maintenance is updating the Stage column. A `missing` link means no file exists; an `old` link means the content lives in a corresponding `src/old-*` source file awaiting conversion. Segments may also contain forward references (`#slug-name`) to not-yet-written segments; these are intentional dependency markers, not broken links.


---

## I. Adaptive Systems Under Uncertainty

*Scope: Any system consisting of an agent coupled to an environment through observation and action channels, where the environment is not fully observable. This is the general case — thermostats through commanders. The claims in this section are largely drawn from TFT (TF-01 through TF-11, Appendix A), which developed the adaptive-systems foundation that ACT subsumes.*

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| I | Postulate | | [#temporal-optimality](src/temporal-optimality.md) | Least-time is optimal | draft |
| I | Definition | | [#agent-environment](src/agent-environment.md) | Agent-environment boundary | draft |
| I | Definition | | [#observation-function](src/observation-function.md) | Lossy, noisy observations | draft |
| I | Definition | | [#action-transition](src/action-transition.md) | Actions affect environment | draft |
| I | Scope | | [#scope-condition](src/scope-condition.md) | Where ACT applies | draft |
| I | Postulate | | [#composition-consistency](src/composition-consistency.md) | Agent/subagent scale invariance | draft |
| I | Postulate | | [#causal-structure](src/causal-structure.md) | Irreducible causal structure | draft |
| I | Definition | | [#pearl-causal-hierarchy](src/pearl-causal-hierarchy.md) | Three levels of causal reasoning | draft |
| I | Definition | | [#chronica](src/chronica.md) | Complete interaction history | draft |
| I | Formulation | | [#agent-model](src/agent-model.md) | Compressed history as state | draft |
| I | Formulation | | [#information-bottleneck](src/information-bottleneck.md) | Optimal model compression | draft |
| I | Definition | | [#model-sufficiency](src/model-sufficiency.md) | Predictive information retained | draft |
| I | Definition | | [#model-class-fitness](src/model-class-fitness.md) | Best achievable sufficiency | draft |
| I | Formulation | | [#event-driven-dynamics](src/event-driven-dynamics.md) | Events in continuous time | draft |
| I | Derived | | [#recursive-update](src/recursive-update.md) | State updates must be recursive | draft |
| I | Derived | | [#action-selection](src/action-selection.md) | Action as function of model | draft |
| I | Definition | | [#mismatch-signal](src/mismatch-signal.md) | Prediction error signal | draft |
| I | Result | | [#mismatch-decomposition](src/mismatch-decomposition.md) | Model error + obs noise | draft |
| I | Empirical | | [#update-gain](src/update-gain.md) | Optimal update weighting | draft |
| I | Definition | | [#causal-information-yield](src/causal-information-yield.md) | Information from interventions | draft |
| I | Definition | | [#adaptive-tempo](src/adaptive-tempo.md) | Rate of useful info acquisition | draft |
| I | Hypothesis | | [#mismatch-dynamics](src/mismatch-dynamics.md) | Mismatch evolution ODE | draft |
| I | Derived | | [#deliberation-cost](src/deliberation-cost.md) | Think vs act tradeoff | draft |
| I | Derived | | [#gain-sector-bridge](src/gain-sector-bridge.md) | Gain + directional fidelity → sector condition | draft |
| I | Result | | [#sector-condition-stability](src/sector-condition-stability.md) | Nonlinear persistence (Lyapunov) | draft |
| I | Result | | [#persistence-condition](src/persistence-condition.md) | Bounded mismatch condition | draft |
| I | Result | | [#structural-adaptation-necessity](src/structural-adaptation-necessity.md) | When parametric update fails | draft |
| I | Derived | | [#temporal-nesting](src/temporal-nesting.md) | Timescale stratification | draft |
| I | Discussion | | [#agent-identity](src/agent-identity.md) | Non-forkable causal trajectory | draft |


---

## II. Actuated Adaptation: Agentic Systems

*Scope narrowing: agents that not only track reality but aim at something. This adds objectives and strategy alongside the reality model. Section I's adaptive machinery applies to the epistemic substate $M_t$ directly. The clean factorization — where $M_t$ updates independently of $G_t$, yielding the sequential orient cascade — is conditional on directed separation ( #directed-separation). What Section II adds is the goal-directed layer: objectives, strategy, and the orient cascade that connects them.*

*The derivation chain for this section is mature (see `msc/spike-v3-purposeful-agent.md`). Most of it provides better justification and epistemic labels for architecture that already existed. The genuinely novel results are: the satisfaction gap / control regret split ( #satisfaction-gap, #control-regret), the $G_t$ complexity bound (in #orient-cascade), and the graph structure uniqueness argument (see `msc/spike-graph-uniqueness.md`).*

*"If a man knows not to which port he sails, no wind is favorable." — Seneca*

| §   | Type            | N   | Tag                                                                                    | Claim                                                            | Stage |
| --- | --------------- | --- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ----- |
| II  | Definition      |     | [#agent-spectrum](src/agent-spectrum.md)                                               | ±model × ±objective quadrants                                    | draft |
| II  | Formulation     |     | [#complete-agent-state](src/complete-agent-state.md)                                   | $X_t = (M_t, G_t)$                                               | draft |
| II  | Formulation     |     | [#objective-functional](src/objective-functional.md)                                   | $O_t$ parametrizes value                                         | draft |
| II  | Definition      |     | [#value-object](src/value-object.md)                                                   | Horizon/policy-conditioned value                                 | draft |
| II  | Definition      |     | [#strategy-dimension](src/strategy-dimension.md)                                       | $G_t = (O_t, \Sigma_t)$ split                                    | draft |
| II  | Derived + Scope |     | [#causal-hierarchy-requirement](src/causal-hierarchy-requirement.md)                   | Level 2 needed for planning                                      | draft |
| II  | Derived         |     | [#loop-interventional-access](src/loop-interventional-access.md)                       | Feedback loop → Level 2 data                                     | draft |
| II  | Scope           |     | [#ciy-observational-proxy](src/ciy-observational-proxy.md)                             | When CIY is estimable from observational data                    | draft |
| II  | Discussion      |     | [#ciy-unified-objective](src/ciy-unified-objective.md)                                 | Joint exploitation-exploration objective                         | draft |
| II  | Normative       |     | [#explicit-strategy-condition](src/explicit-strategy-condition.md)                     | When planning beats exploring                                    | draft |
| II  | Derived         |     | [#chain-confidence-decay](src/chain-confidence-decay.md)                               | Log-confidence additive in depth                                 | draft |
| II  | Scope           |     | [#and-or-scope](src/and-or-scope.md)                                                   | Conjunctive/disjunctive scope                                    | draft |
| II  | Definition      |     | [#strategy-dag](src/strategy-dag.md)                                                   | Strategy as probabilistic DAG                                    | draft |
| II  | Derived + Scope |     | [#directed-separation](src/directed-separation.md)                                     | Epistemic update is goal-blind                                   | draft |
| II  | Definition      |     | [#satisfaction-gap](src/satisfaction-gap.md)                                           | Ideal vs best achievable                                         | draft |
| II  | Definition      |     | [#control-regret](src/control-regret.md)                                               | Best achievable vs current                                       | draft |
| II  | Definition      |     | [#strategic-calibration](src/strategic-calibration.md)                                 | Edge residuals                                                   | draft |
| II  | Derived         |     | [#orient-cascade](src/orient-cascade.md)                                               | Resolution order by info dep                                     | draft |
| II  | Derived         |     | [#observability-dominance](src/observability-dominance.md)                             | Unobservable edges freeze                                        | draft |
| II  | Hypothesis      |     | [#edge-update-via-gain](src/edge-update-via-gain.md)                                   | Gain extends to strategy edges                                   | draft |
| II  | Scope           |     | [#edge-update-causal-validity](src/edge-update-causal-validity.md)                     | When edge updates are causally valid                             | draft |
| II  | Formulation     |     | [#structural-change-as-parametric-limit](src/structural-change-as-parametric-limit.md) | Pruning/grafting as continuous                                   | draft |
|     | --GAP--         |     |                                                                                        | Rate of useful $\Sigma_t$ revision (adaptive tempo for strategy) |       |
|     | --GAP--         |     |                                                                                        | Complexity cost of maintaining $\Sigma_t$ (IB/MDL for DAGs)      |       |
| II  | Proposed schema |     | [#strategy-persistence-schema](src/strategy-persistence-schema.md)                     | Sector conditions for $\Sigma_t$                                 | draft |
|     | --GAP--         |     |                                                                                        | Three-way exploit/explore/deliberate allocation with $\Sigma_t$  |       |


---

## III. Agentic Composites

*Scope: multiple agents interacting through a shared environment, or equivalently, the internal structure of composite agents. The composition postulate ( #composition-consistency) ensures the theory applies at every level of description; this section develops what happens when composition is imperfect and what the dynamics of inter-agent interaction look like.*

*Correlated observations as default; independence as the special case requiring justification. Adversarial dynamics are one end of a teleological unity spectrum, not a separate theory.*

*Two sources: the simulation-validated adversarial dynamics from TFT (TF-11/Appendix F, track-b simulations), and the composition spike (`msc/spike-agent-composition.md`) which derives the requirement for composition consistency from the scope condition's level-independence.*

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| III | Scope | | [#multi-agent-scope](src/multi-agent-scope.md) | Multiple agents, shared env | draft |
| III | Formulation | | [#composition-closure](src/composition-closure.md) | Composite agent via closure defect | draft |
| III | Derived | | [#tempo-composition](src/tempo-composition.md) | Sub-additive tempo inequality | draft |
| III | Hypothesis | | [#directed-separation-under-composition](src/directed-separation-under-composition.md) | Goal-blindness survives iff routing is goal-blind (two cases) | draft |
| III | Discussion | | [#unity-dimensions](src/unity-dimensions.md) | 4 dimensions of coherence | draft |
| III | Definition + Discussion | | [#shared-intent](src/shared-intent.md) | IB-compressed purpose | draft |
| III | Hypothesis | | [#auftragstaktik-principle](src/auftragstaktik-principle.md) | Prioritize objective sharing | draft |
| III | Derived | | [#team-persistence](src/team-persistence.md) | Composite persistence condition | draft |
| III | Result | | [#adversarial-tempo-advantage](src/adversarial-tempo-advantage.md) | Superlinear tempo advantage | draft |
| III | Hypothesis | | [#communication-gain](src/communication-gain.md) | Trust-weighted update gain for inter-agent channels | draft |
| III | Derived | | [#adversarial-destabilization](src/adversarial-destabilization.md) | Inside opponent's loop; includes effects spiral corollary | draft |
| | --GAP-- | | | Which strategy edges are most valuable to attack | |
| III | Observation | | [#adversarial-exponent-regimes](src/adversarial-exponent-regimes.md) | $\alpha = 2, 3/2, \text{or } {\sim}1$ | draft |
| III | Observation | | [#observation-gates-advantage](src/observation-gates-advantage.md) | Obs noise gates advantage | draft |
| III | Result | | [#per-dimension-persistence](src/per-dimension-persistence.md) | Weak dimension is bottleneck | draft |


---

## Appendices: Details

*Supporting material: derivations, sketches, simulation results, and operationalization procedures backing the main theory claims.*

| §   | Type       | N   | Tag                                                                | Claim                                                          | Stage   |
| --- | ---------- | --- | ------------------------------------------------------------------ | -------------------------------------------------------------- | ------- |
| A   | Derivation |     | [#sector-condition-derivation](src/sector-condition-derivation.md) | Lyapunov derivations for bounded mismatch and adaptive reserve | draft   |
| A   | Derivation |     | [#recursive-update-derivation](src/recursive-update-derivation.md) | Uniqueness derivation via three constraints + counterexamples  | draft   |
| A   | Sketch     |     | [#multi-timescale-stability](src/multi-timescale-stability.md)     | N-timescale singular perturbation sketch                       | draft   |
| A   | Detail     |     | [#linear-ode-approximation](src/linear-ode-approximation.md)       | Pedagogical linear mismatch ODE                                | missing |
| A   | Derivation |     | [#graph-structure-uniqueness](src/graph-structure-uniqueness.md)   | 4 postulates → DAG; acyclicity proved, P3→Markov sketch        | draft   |
| A   | Detail     |     | [#simulation-results](src/simulation-results.md)                   | 6 variants validating claims                                   | draft   |


---

## Appendices: Operational Domains

*Operational-specific appendices and end-to-end domain instantiations validating the theory chain.*

| §   | Type           | N   | Tag                                                    | Claim                                            | Stage |
| --- | -------------- | --- | ------------------------------------------------------ | ------------------------------------------------ | ----- |
| B   | Detail         |     | [#operationalization](src/operationalization.md)       | Estimation procedures for ACT quantities         | draft |
| B   | Worked example |     | [#worked-example-kalman](src/worked-example-kalman.md) | End-to-end Kalman instantiation (exact)          | draft |
| B   | Worked example |     | [#worked-example-bandit](src/worked-example-bandit.md) | End-to-end RL bandit instantiation (approximate) | draft |
| B   | Worked example |     | [#worked-example-strategy](src/worked-example-strategy.md) | Section II strategy DAG instantiation (3-arm bandit) | draft |
