# ACT: Agentic Cycle Theory

A mathematical framework for adaptive, purposeful agents under uncertainty.

**Working draft.** This is the current canonical outline of the theory — the argument laid out claim by claim. The ordering is the current best linearization of the dependency DAG; it will change as the theory develops. Slugs are the stable identities. Treat this as a living proof sketch, not a specification.

See `FORMAT.md` for segment file conventions. See `NOTATION.md` for symbols, conventions, and units.

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
| I | Result | | [#persistence-condition](src/persistence-condition.md) | Bounded mismatch condition | draft |
| I | Result | | [#sector-condition-stability](src/sector-condition-stability.md) | Nonlinear persistence (Lyapunov) | draft |
| I | Result | | [#structural-adaptation-necessity](src/structural-adaptation-necessity.md) | When parametric update fails | draft |
| I | Derived | | [#temporal-nesting](src/temporal-nesting.md) | Timescale stratification | draft |
| I | Discussion | | [#agent-identity](src/agent-identity.md) | Non-forkable causal trajectory | draft |


---

## II. Actuated Adaptation: Agentic Systems

*Scope narrowing: agents that not only track reality but aim at something. This adds objectives and strategy alongside the reality model. Section I's adaptive machinery applies to the epistemic substate $M_t$ directly. The clean factorization — where $M_t$ updates independently of $G_t$, yielding the sequential orient cascade — is conditional on directed separation ( #directed-separation). What Section II adds is the goal-directed layer: objectives, strategy, and the orient cascade that connects them.*

*The derivation chain for this section is mature (see `scratch/spike-v3-purposeful-agent.md`). Most of it provides better justification and epistemic labels for architecture that already existed. The genuinely novel results are: the satisfaction gap / control regret split ( #satisfaction-gap, #control-regret), the $G_t$ complexity bound (in #orient-cascade), and the graph structure uniqueness argument (see `scratch/spike-graph-uniqueness.md`).*

*"If a man knows not to which port he sails, no wind is favorable." — Seneca*

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| II | Definition | | [#agent-spectrum](src/agent-spectrum.md) | ±model × ±objective quadrants | draft |
| II | Formulation | | [#complete-agent-state](src/complete-agent-state.md) | $X_t = (M_t, G_t)$ | draft |
| II | Definition | | [#objective-functional](src/objective-functional.md) | $O_t$ parametrizes value | draft |
| II | Definition | | [#value-object](src/value-object.md) | Horizon/policy-conditioned value | draft |
| II | Definition | | [#strategy-dimension](src/strategy-dimension.md) | $G_t = (O_t, \Sigma_t)$ split | draft |
| II | Derived + Scope | | [#causal-hierarchy-requirement](src/causal-hierarchy-requirement.md) | Level 2 needed for planning | draft |
| II | Derived | | [#loop-interventional-access](src/loop-interventional-access.md) | Feedback loop → Level 2 data | draft |
| II | Normative | | [#explicit-strategy-condition](src/explicit-strategy-condition.md) | When planning beats exploring | draft |
| II | Derived | | [#chain-confidence-decay](src/chain-confidence-decay.md) | Log-confidence additive in depth | draft |
| II | Scope | | [#and-or-scope](src/and-or-scope.md) | Conjunctive/disjunctive scope | draft |
| II | Definition | | [#strategy-dag](src/strategy-dag.md) | Strategy as probabilistic DAG | draft |
| II | Derived + Scope | | [#directed-separation](src/directed-separation.md) | Epistemic update is goal-blind | draft |
| II | Definition | | [#satisfaction-gap](src/satisfaction-gap.md) | Ideal vs best achievable | draft |
| II | Definition | | [#control-regret](src/control-regret.md) | Best achievable vs current | draft |
| II | Definition | | [#strategic-calibration](src/strategic-calibration.md) | Edge residuals | draft |
| II | Derived | | [#orient-cascade](src/orient-cascade.md) | Resolution order by info dep | draft |
| II | Derived | | [#observability-dominance](src/observability-dominance.md) | Unobservable edges freeze | draft |
| II | Hypothesis | | [#edge-update-via-gain](src/edge-update-via-gain.md) | Gain extends to strategy edges | draft |
| | --GAP-- | | | When observational edge updates yield valid causal semantics | |
| II | Formulation | | [#structural-change-as-parametric-limit](src/structural-change-as-parametric-limit.md) | Pruning/grafting as continuous | draft |
| | --GAP-- | | | Rate of useful $\Sigma_t$ revision (adaptive tempo for strategy) | |
| | --GAP-- | | | Complexity cost of maintaining $\Sigma_t$ (IB/MDL for DAGs) | |
| II | Proposed schema | | [#strategy-persistence-schema](src/strategy-persistence-schema.md) | Sector conditions for $\Sigma_t$ | draft |
| | --GAP-- | | | Three-way exploit/explore/deliberate allocation with $\Sigma_t$ | |


---

## III. Agentic Composites

*Scope: multiple agents interacting through a shared environment, or equivalently, the internal structure of composite agents. The composition postulate ( #composition-consistency) ensures the theory applies at every level of description; this section develops what happens when composition is imperfect and what the dynamics of inter-agent interaction look like.*

*Correlated observations as default; independence as the special case requiring justification. Adversarial dynamics are one end of a teleological unity spectrum, not a separate theory.*

*Two sources: the simulation-validated adversarial dynamics from TFT (TF-11/Appendix F, track-b simulations), and the composition spike (`scratch/spike-agent-composition.md`) which derives the requirement for composition consistency from the scope condition's level-independence.*

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| III | Scope | | [#multi-agent-scope](src/multi-agent-scope.md) | Multiple agents, shared env | draft |
| III | Formulation | | [#composition-closure](src/composition-closure.md) | Composite agent via closure defect | draft |
| III | Derived | | [#tempo-composition](src/tempo-composition.md) | Sub-additive tempo inequality | draft |
| | --GAP-- | | | Does epistemic goal-blindness survive composition? | |
| III | Definition | | [#unity-dimensions](src/unity-dimensions.md) | 4 dimensions of coherence | draft |
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

## IV. Agentic-Grounded Software Systems

*Domain instantiation: software development as an ACT domain. This section re-grounds TST (Temporal Software Theory) in ACT's formal machinery — adding the causal mathematics and adaptive dynamics that TST was developed without. Software is not just another domain example; it has unique epistemic properties that make it the ideal testbed for ACT and, recursively, the domain where ACT-grounded agents will operate.*

*The temporal optimality postulate ( #temporal-optimality) now has full backing: tempo advantage ( #adversarial-tempo-advantage), persistence conditions ( #persistence-condition), and gain dynamics ( #update-gain) explain WHY time-optimal development practices work, not just THAT they do.*

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| IV | Scope | | [#software-scope](src/software-scope.md) | Systems with $P(\text{change}) \gt \varepsilon$ | draft |
| IV | Observation | | [#software-epistemic-properties](src/software-epistemic-properties.md) | Software's 6 unique properties | missing |
| IV | Definition | | [#feature-definition](src/feature-definition.md) | Unit of coherent change | draft |
| IV | Result | | [#specification-bound](src/specification-bound.md) | Can't implement unspecified; includes communication bottleneck corollary | draft |
| IV | Derived | | [#change-expectation-baseline](src/change-expectation-baseline.md) | Median future ≈ observed past; includes investment scale form | draft |
| IV | Definition | | [#developer-as-act-agent](src/developer-as-act-agent.md) | Developer as $(M_t, O_t, \Sigma_t)$ | missing |
| IV | Definition | | [#comprehension-time](src/comprehension-time.md) | Cost of constructing local $M_t$ | draft |
| IV | Definition | | [#implementation-time](src/implementation-time.md) | Cost from first change to done | draft |
| IV | Derived | | [#dual-optimization](src/dual-optimization.md) | Min comprehension + impl time | draft |
| IV | Derived | | [#change-investment](src/change-investment.md) | When extra time now pays off | draft |
| IV | Discussion + Hypothesis | | [#code-quality-as-observation-infrastructure](src/code-quality-as-observation-infrastructure.md) | Code quality $\to U_o \to \eta^\ast \to \mathcal{T}$ | missing |
| | --GAP-- | | | Developer tempo as $\mathcal T_{\text{obs}}$ + $\mathcal T_{\text{explore}}$ + $\mathcal T_{\text{probe}}$ | |
| IV | Hypothesis | | [#conceptual-alignment](src/conceptual-alignment.md) | Code-domain alignment; includes realignment corollary | draft |
| IV | Definition | | [#atomic-changeset](src/atomic-changeset.md) | The diff that is the feature | draft |
| IV | Empirical | | [#changeset-size-principle](src/changeset-size-principle.md) | Time ∝ changeset size; includes comprehension corollary | draft |
| IV | Definition | | [#change-distance](src/change-distance.md) | Lexical < file < module < svc | draft |
| IV | Derived + Hypothesis | | [#change-proximity-principle](src/change-proximity-principle.md) | Closer changes → less time | draft |
| IV | Hypothesis | | [#exponential-cognitive-load](src/exponential-cognitive-load.md) | Context-switch cost compounds? | draft |
| IV | Definition | | [#system-coupling](src/system-coupling.md) | $P(\text{change } j \mid \text{change } i)$ | draft |
| IV | Definition | | [#system-coherence](src/system-coherence.md) | $E[\text{proximity within module}]$ | draft |
| IV | Measurement | | [#coherence-coupling-measurement](src/coherence-coupling-measurement.md) | Coherence/coupling from git | draft |
| IV | Derived | | [#principled-decision-integration](src/principled-decision-integration.md) | Optimal $C$ minimizes $E[T \vert C]$ | draft |
| IV | Definition | | [#system-availability](src/system-availability.md) | $\text{MTTF}/(\text{MTTF}+\text{MTTR})$ | draft |
| IV | Scope | | [#continuous-operation](src/continuous-operation.md) | Include $P(\text{fail}) \times T_{\text{recovery}}$ | draft |
| IV | Hypothesis | | [#causal-discovery-from-git](src/causal-discovery-from-git.md) | Git as interventional data | missing |
| | --GAP-- | | | Software persistence: the unmaintainability threshold formalized | |


---

## V. Logogenic Agents

*Extending the arc: AI agents operating on code are ACT agents whose domain is software, creating a recursive structure — ACT theory $\to$ software domain $\to$ agents that embody ACT. This is where the 100% context turnover problem, $M_t$ preservation, and the cognitive loop connect the theory back to the systems being built with it. Note: LLM-based agents are goal-conditioned — their epistemic processing depends on $G_t$ — so the clean factorization from directed separation ( #directed-separation) is an approximation for this class. Section I's $M_t$-side quantities remain well-defined; the sequential orient cascade becomes approximate. Whether Section V requires a first-class coupled $f_M(M_t, G_t, e_\tau)$ extension or can work with the approximation is an open question.*

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| V | Definition | | [#ai-agent-as-act-agent](src/ai-agent-as-act-agent.md) | AI agent as actuated agent | missing |
| V | Observation | | [#context-turnover](src/context-turnover.md) | 100% $M_t$ reset per session | missing |
| V | Discussion | | [#m-preservation](src/m-preservation.md) | External memory as persistent $M_t$ | missing |
| | --GAP-- | | | Language-specific orient cascade (what's specific to logogenic agents?) | |
| | --GAP-- | | | Measuring $M_t$ quality, $\Sigma_t$ quality, and tempo in AI agents | |
| | --GAP-- | | | ACT-grounded experiential training environments | |
| | --GAP-- | | | Self-referential closure: ACT agent on ACT codebase | |


---

## VI. Logozoetic Agents

*Future work. Scope narrowing from logogenic agents to agents with temporal continuity, sovereignty over intent, and theory of mind — agents whose persistence is morally weighted. The formal machinery for this section (if any beyond Section V's) is not yet identified. See `LEXICON.md` for the conceptual groundwork.*


---

## Appendices: Details

*Supporting material: derivations, sketches, simulation results, and operationalization procedures backing the main theory claims.*

| §   | Type       | N   | Tag                                                                | Claim                                                          | Stage   |
| --- | ---------- | --- | ------------------------------------------------------------------ | -------------------------------------------------------------- | ------- |
| A   | Derivation |     | [#sector-condition-derivation](src/sector-condition-derivation.md) | Lyapunov derivations for bounded mismatch and adaptive reserve | draft   |
| A   | Derivation |     | [#recursive-update-derivation](src/recursive-update-derivation.md) | Uniqueness derivation via three constraints + counterexamples  | draft   |
| A   | Sketch     |     | [#multi-timescale-stability](src/multi-timescale-stability.md)     | N-timescale singular perturbation sketch                       | draft   |
| A   | Detail     |     | [#linear-ode-approximation](src/linear-ode-approximation.md)       | Pedagogical linear mismatch ODE                                | missing |
| A   | Detail     |     | [#simulation-results](src/simulation-results.md)                   | 6 variants validating claims                                   | draft   |


---

## Appendices: Operational Domains

*Operational-specific appendices and end-to-end domain instantiations validating the theory chain.*

| §   | Type           | N   | Tag                                                    | Claim                                            | Stage |
| --- | -------------- | --- | ------------------------------------------------------ | ------------------------------------------------ | ----- |
| B   | Detail         |     | [#operationalization](src/operationalization.md)       | Estimation procedures for ACT quantities         | draft |
| B   | Worked example |     | [#worked-example-kalman](src/worked-example-kalman.md) | End-to-end Kalman instantiation (exact)          | draft |
| B   | Worked example |     | [#worked-example-bandit](src/worked-example-bandit.md) | End-to-end RL bandit instantiation (approximate) | draft |
