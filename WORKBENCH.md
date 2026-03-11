# WORKBENCH — ACT Theory Development

Working notes for theory development. This is a thinking tool, not a
reference document. For the canonical theory structure, see
`CURRENT-FULL-THEORY.md`.


## Segment Status

### Written — Section I (28 segments, 27 written)
| Slug | Type | Notes |
|------|------|-------|
| [temporal-optimality](src/temporal-optimality.md) | Axiom | Needs review |
| [agent-environment](src/agent-environment.md) | Definition | Needs review |
| [observation-function](src/observation-function.md) | Definition | Needs review |
| [action-transition](src/action-transition.md) | Definition | Needs review |
| [scope-condition](src/scope-condition.md) | Scope | Needs review |
| [agent-model](src/agent-model.md) | Formulation | Needs review |
| [information-bottleneck](src/information-bottleneck.md) | Formulation | Needs review |
| [model-sufficiency](src/model-sufficiency.md) | Definition | Needs review |
| [model-class-fitness](src/model-class-fitness.md) | Definition | Needs review |
| [causal-structure](src/causal-structure.md) | Axiom | Needs review |
| [pearl-causal-hierarchy](src/pearl-causal-hierarchy.md) | Definition | Needs review |
| [chronica](src/chronica.md) | Definition | Needs review |
| [event-driven-dynamics](src/event-driven-dynamics.md) | Formulation | Needs review |
| [recursive-update](src/recursive-update.md) | Derived | Needs review |
| [action-selection](src/action-selection.md) | Derived | Needs review |
| [mismatch-signal](src/mismatch-signal.md) | Definition | Needs review |
| [mismatch-decomposition](src/mismatch-decomposition.md) | Theorem | Needs review |
| [update-gain](src/update-gain.md) | Empirical | Needs review |
| [causal-information-yield](src/causal-information-yield.md) | Definition | Needs review |
| [adaptive-tempo](src/adaptive-tempo.md) | Definition | Needs review |
| [mismatch-dynamics](src/mismatch-dynamics.md) | Hypothesis | Needs review |
| [deliberation-cost](src/deliberation-cost.md) | Derived | Needs review |
| [persistence-condition](src/persistence-condition.md) | Theorem | Needs review |
| [sector-condition-stability](src/sector-condition-stability.md) | Theorem | Needs review |
| [structural-adaptation-necessity](src/structural-adaptation-necessity.md) | Theorem | Needs review |
| [temporal-nesting](src/temporal-nesting.md) | Derived | Needs review |
| [agent-identity](src/agent-identity.md) | Discussion | Needs review |

### Not Yet Written — Section I
| Slug | Type | Source material |
|------|------|-----------------|
| composition-consistency | Axiom | `scratch/spike-agent-composition.md` |

### Written — Section II (1 of 20 segments)
| Slug | Type | Notes |
|------|------|-------|
| [agent-spectrum](src/agent-spectrum.md) | Definition | Needs review |

### Written — Section IV (1 of 28 segments)
| Slug | Type | Notes |
|------|------|-------|
| [specification-bound](src/specification-bound.md) | Theorem | Needs review |

### Not Yet Written — Section II
| Slug | Type | Source material |
|------|------|-----------------|
| complete-agent-state | Formulation | v3 spike §1 |
| objective-functional | Definition | v3 spike §2 |
| value-object | Definition | v3 spike §2.2 |
| strategy-dimension | Definition | v3 spike §3 |
| causal-hierarchy-requirement | Derived + Scope | v3 spike §4 |
| loop-interventional-access | Derived | v3 spike §4.3 |
| explicit-strategy-condition | Normative | v3 spike §5 |
| chain-confidence-decay | Derived | v3 spike §6.1 |
| and-or-scope | Scope | v3 spike §6.2 |
| strategy-dag | Definition | intent-dag-consolidated + graph uniqueness spike |
| directed-separation | Derived + Scope | v3 spike §8 |
| satisfaction-gap | Definition | v3 spike §7.3 |
| control-regret | Definition | v3 spike §7.4 |
| strategic-calibration | Definition | v3 spike §7.5 |
| orient-cascade | Derived | v3 spike §7.6 |
| observability-dominance | Derived | intent-dag-consolidated |
| edge-update-via-gain | Hypothesis | intent-dag-consolidated |
| structural-change-as-parametric-limit | Formulation | intent-dag-consolidated |
| strategy-persistence-schema | Proposed schema | v3 spike §9 |

### Not Yet Written — Sections III–V
All claims. Source material in TFT (TF-11, Appendix F, track-b sims),
composition spike, TST, and agentic-tft docs 10-14.


## Key Spikes

| Spike | Location | Status |
|-------|----------|--------|
| Purposeful agent derivation (v3) | `scratch/spike-v3-purposeful-agent.md` | **Definitive** for Section II porting |
| Agent composition / holon | `scratch/spike-agent-composition.md` | Core insight strong; composition laws are sketches |
| Graph structure uniqueness | `scratch/spike-graph-uniqueness.md` | Acyclicity derived; P3→Markov needs tightening |
| Intent DAG consolidated | `scratch/04-intent-dag-consolidated.md` | Canonical DAG reference; converged |
| Prior art assessment | `scratch/02-prior-art-assessment.md` | Hafez/IBM/BDI/active-inference positioning |
| LLM causal access note | `scratch/llm-causal-access-note.md` | Pearl reconciliation; potential intro/paper/blog |
| Track-b simulations | `scratch/track-b-nonlinear-sims/` | 6 variants, all validated |


## What's Settled

*From convergence testing, spikes, and simulation:*

- Single-parameter edges with AND/OR nodes
- Orient cascade structure (derived from information dependency)
- Additive log-confidence decay (generalizes $p^n$)
- Observability as strategy enablement
- Directed separation (with explicit scope condition for goal-conditioned
  agents)
- $G_t = (O_t, \Sigma_t)$ split (definitional, not timescale-dependent)
- Satisfaction gap / control regret split (replaces simpler
  $\delta_{\text{objective}}$)
- DAG acyclicity derived from temporal ordering (former fragility resolved)
- Composition consistency required (not optional) by scope condition's
  level-independence


## What's Open

- Action-deliberation-exploration tradeoff (three-way with $\Sigma_t$)
- Strategy tempo formalization
- Cognitive cost of $\Sigma_t$ (no $\beta$ analog yet)
- Edge identifiability conditions (resolved in software, open in general)
- P3→Markov step in graph uniqueness (sketch, needs tightening)
- Composition laws (specific forms are sketches; existence is required)


## Known Fragilities

- Edge semantics claim interventional but update from observational
- Missing commitment/resource/temporal structure in the DAG
- Directed separation violated by goal-conditioned agents (LLMs) —
  acknowledged as scope restriction, not a bug


## Codex Review Issues (from memory — fixes needed)

1. **State completeness**: Must lift to $X_t = (M_t, G_t)$. $M_t$ becomes
   epistemic substate, not complete state. Foundational.
2. **Level 2 too strong**: Pre-compiled controllers are purposeful at
   Level 1. Scope to agents that must *learn* action consequences during
   operation.
3. **Objective/strategy are independent dimensions**: Don't conflate in a
   single hierarchy. $O_t$ richness and $\Sigma_t$ richness vary
   independently. Split early.
4. **$O_t$ parametrizes TF-08's "value" term**: Cleaner insertion point.
5. **Objective as trajectory functional**: $J$: trajectories $\to \mathbb{R}$
   is genuinely more general than point targets.
6. **Cost inequality for $\Sigma_t$**: Derive need for explicit planning
   from $\text{cost}(\text{plan}) < \text{cost}(\text{explore})$, making
   #temporal-optimality load-bearing.
7. **$p^n$ is the special case**: Robust result is additive log-confidence
   growth.
8. **Strategy persistence is a theorem schema**: Need strategic error state,
   correction operator, disturbance class.
9. **Directed separation is conditional**: $f_M$ is $G_t$-independent, but
   closed-loop $M$ transition depends on $G_t$ through action. Precise claim
   is about update function, not trajectory.
10. **$\delta_{\text{objective}}$ must split into TWO quantities**:
    satisfaction gap + control regret. Without this split, the $O_t$ revision
    cascade doesn't work.

Items 1–10 are addressed in v3 spike. Porting to src/ segments is the
remaining work.


## Ordering Questions

*The current linearization in CURRENT-FULL-THEORY.md may need revision:*

- Should #temporal-optimality move from Section I to Section II? It's about
  specific objectives — arguably an actuated-agent concept, not a general
  adaptive-systems concept. Counter-argument: it applies to Section I agents
  too (a Kalman filter that converges faster is better).

- Should #composition-consistency move earlier or later? Currently at the end
  of Section I foundations, before the dynamics claims. Could go right after
  #scope-condition (it's a direct consequence of scope's level-independence).
  The composition spike argues for early placement.

- Section II ordering: the v3 spike proposes a specific 16-segment
  linearization (§11). Is that still the best ordering after the codex
  review corrections?


## Simulation Findings (Summary)

The track-b simulations (`scratch/track-b-nonlinear-sims/`) validated and
refined specific claims:

- Cor. 11.2's exponent = 2 under deterministic drift (confirmed: 1.999)
- Under stochastic disturbances, exponent = 1.5 (not 2.0)
- Observation noise collapses adversarial exponent from ~1.0 to ~0.2
- Per-dimension persistence exact (scalar overestimates by 72%)
- TF-06's gain principle empirically validated (52% reduction)


## Prior Work Migration Map

All TFT and TST content has been copied into `src/old-*` files. The priors/ submodules are now purely historical. The `old-` prefix means the content is prior work that hasn't been fully ACTualized yet — it may not conform to ACT formatting standards.

### TFT → ACT Mapping

| Old file | Content | ACT status |
|----------|---------|------------|
| ~~old-tf-readme~~ | ~~TFT overview~~ | **Archived.** Superseded by CLAUDE.md, FORMAT.md. |
| old-tf-00-notation-conventions | Symbol tables, conventions, adaptive loop phases, global assumptions, units, claim registry | **Partially absorbed.** Notation referenced by FORMAT.md. Adaptive loop phases, global assumptions table, claim registry format — ACT should have its own. |
| ~~old-tf-01-scope~~ | ~~Scope definitions~~ | **Archived.** → #agent-environment, #observation-function, #action-transition, #scope-condition. Coupling spectrum now in #causal-structure. |
| ~~old-tf-02-causal-structure~~ | ~~Temporal arrow, chronica, Pearl's 3 levels, recursive update~~ | **Archived.** → #causal-structure, #pearl-causal-hierarchy, #chronica, #recursive-update. |
| ~~old-tf-03-model~~ | ~~Model, IB, sufficiency~~ | **Archived.** → #agent-model, #information-bottleneck, #model-sufficiency. |
| ~~old-tf-04-event-driven-dynamics~~ | ~~Event types, channels, rates~~ | **Archived.** → #event-driven-dynamics. |
| ~~old-tf-05-mismatch-signal~~ | ~~Prediction error, Prop 5.1~~ | **Archived.** → #mismatch-signal, #mismatch-decomposition. |
| old-tf-06-update-gain | Uncertainty ratio, domain validation, gain dynamics, overfitting as miscalibration | **Mostly absorbed** into #update-gain. Domain validation tables and gain dynamics (convergence, reset) richer than ACT segment — enrich then archive. |
| ~~old-tf-07-action-selection~~ | ~~Action as model function, fluency~~ | **Archived.** → #action-selection. |
| ~~old-tf-08-exploration-exploitation~~ | ~~CIY, unified policy objective, query actions~~ | **Archived.** → #causal-information-yield. |
| ~~old-tf-09-deliberation-cost~~ | ~~Prop 9.1, deliberation threshold~~ | **Archived.** → #deliberation-cost. |
| ~~old-tf-10-structural-adaptation~~ | ~~Prop 10.1, destruction-creation, overfitting~~ | **Archived.** → #structural-adaptation-necessity + #model-sufficiency + #model-class-fitness. |
| old-tf-11-tempo-persistence | Temporal nesting table, mismatch ODE, adversarial dynamics, observation quality, per-dimension | **Mostly absorbed** across #adaptive-tempo, #persistence-condition, #sector-condition-stability, etc. Mismatch ODE as named hypothesis, speed-quality substitutability — enrich then archive. |
| old-tf-appendix-a-lyapunov | Props A.1–A.3, Cor A.3.1, full proofs, Prop A.4 sketch | **Mostly absorbed** into #sector-condition-stability. Full proofs and multi-timescale sketch worth preserving — enrich then archive. |
| old-tf-appendix-b-operationalization | Estimation procedures for all TFT quantities | **Not yet in ACT.** Practical reference. Future agent can port as appendix. |
| old-tf-appendix-c-kalman-example | Complete Kalman worked example | **Not yet in ACT.** Future agent can port as appendix. |
| old-tf-appendix-d-rl-example | Nonstationary bandit worked example | **Not yet in ACT.** Future agent can port as appendix. |
| ~~old-tf-appendix-e-tft-core~~ | ~~Condensed formal chain~~ | **Archived.** Superseded by CURRENT-FULL-THEORY.md. |
| old-tf-appendix-f-multi-agent | Communication gain, trust, distributed tempo, topology, game theory | **Partially absorbed** into Section III outline. Rich content — source material for Section III segments. |
| ~~old-tf-appendix-g-agent-identity~~ | ~~Non-forkability, clone problem~~ | **Archived.** → #agent-identity. |
| old-tf-recursive-update-proof | Full uniqueness proof | Supporting material for #recursive-update. Future agent can port as appendix or fold into segment. |
| old-tf-goal-intent-gap | What TFT lacked (goals/intent) | **Historical.** The gap ACT exists to fill. Can archive when comfortable. |
| old-tf-citations-catalog | TFT reference catalog | **Reference material.** Useful for paper writing. |
| old-tf-novelty-analysis | What's novel in TFT | **Reference material.** Useful for positioning. |
| old-tf-ooda-universal-pattern | OODA as universal adaptive pattern (v7) | **Historical.** Early framing. Can archive when comfortable. |

### TST → ACT Mapping

| Old file | Content | ACT status |
|----------|---------|------------|
| ~~old-tst-readme~~ | ~~TST overview~~ | **Archived.** Superseded by Section IV of CURRENT-FULL-THEORY.md. |
| ~~old-tst-01-temporal-optimality~~ | ~~T-01~~ | **Archived.** → #temporal-optimality (generalized). |
| old-tst-02-specification-bound | D-01 (feature def) + T-02 + C-02.1 | **Absorbed** into #specification-bound, #feature-definition, #communication-as-bottleneck. TST has richer discussion of LLM/AI implications. |
| old-tst-03-evolving-scope | T-03: evolving systems scope, infinite velocity insight | **Absorbed** into #software-scope. "Infinite velocity" framing preserved. |
| old-tst-04-change-expectation | T-04: Bayesian baseline, Jeffrey's prior, C-04.1, C-04.2, velocity inflection discussion | **Absorbed** into #change-expectation-baseline, #investment-scaling. Open question on velocity inflection not in ACT. |
| old-tst-05-dual-optimization | D-02, D-03, T-05: comprehension + implementation, turnover multiplier, AI collaboration implications | **Absorbed** into #comprehension-time, #implementation-time, #dual-optimization. Rich AI-turnover discussion not fully in ACT. |
| old-tst-06-change-investment | T-06: investment threshold, compound effects, near-zero cost reality, AI advantage | **Absorbed** into #change-investment. Detailed practical guidance not in ACT. |
| old-tst-07-conceptual-alignment | T-07 + C-07.1: alignment hypothesis, dual comprehension, startup pivot principle | **Absorbed** into #conceptual-alignment, #realignment-as-feature. |
| old-tst-08-changeset-size | D-04, T-08, C-08.1: atomic changeset, size principle, comprehension follows size | **Absorbed** into #atomic-changeset, #changeset-size-principle, #comprehension-follows-changeset. |
| old-tst-09-change-proximity | D-05, T-09, H-09.1, Der-09.1: change distance, proximity principle, exponential cognitive load hypothesis | **Absorbed** into #change-distance, #change-proximity-principle, #exponential-cognitive-load. |
| old-tst-10-coherence-coupling | D-06, D-07, T-10: coupling/coherence definitions, measurement from git | **Absorbed** into #system-coupling, #system-coherence, #coherence-coupling-measurement. |
| old-tst-11-decision-integration | T-11: principled decision integration, expanded temporal terms | **Absorbed** into #principled-decision-integration. |
| old-tst-12-continuous-operation | D-08, T-12: availability, fault-tolerant vs defensive, perturbation types | **Absorbed** into #system-availability, #continuous-operation. |

### TST via-TFT Bridge Material → ACT Mapping

| Old file | Content | ACT status |
|----------|---------|------------|
| old-tst-via-tft-readme | Why the bridge exists, software's 6 unique epistemic properties, key open questions | **Partially absorbed.** The 6 properties → #software-epistemic-properties (outlined). Open questions (observation channel under agent control, 100% turnover, counterfactual replay) feed Section IV/V. |
| old-tst-via-tft-mapping | Detailed TFT→software mapping: environment decomposition, observation channels, action taxonomy, model, mismatch, gain, tempo, persistence, structural adaptation, multi-agent | **Richest single document for Section IV.** Action taxonomy (exploration/probe/query/modify/infrastructure-investment), three-part tempo decomposition, code-quality feedback loop, death spiral formalization — much not yet in ACT segments. |
| old-tst-via-tft-causal-extensions | Explicit causal DAGs in software, interventional reasoning via tests, counterfactual evaluation via git, causal discovery from git, runtime causal models | **Partially absorbed** into #causal-discovery-from-git and #software-epistemic-properties. Detailed treatment of dependency DAG vs empirical DAG, Level 2 channel spectrum, counterfactual machine — largely not in ACT. |
| old-tst-via-tft-reformulated-sketch | S-00 through S-14: complete outline of TST rebuilt on TFT/ACT foundations | **Valuable roadmap** for Section IV work. Shows how each TST claim maps to the ACT framework. The "what's new" and "what's removed" sections are useful for understanding the transformation. |
| old-tst-via-tft-simulation-proposals | 6 simulation proposals ordered by value/effort | **Partially executed.** Sims 1-2 done (track-b). Sims 3-6 remain as future work. |


## Prior Art Positioning & Paper Strategy

*Detailed cross-mapping in `scratch/02-prior-art-assessment.md`.*

**The landscape:** IBM (Miehling et al. 2025) calls for a systems theory of agentic AI — explicitly identifying the void. Hafez et al. (2026) provide a diagnostic metric (bi-predictability $P$) without dynamics or goals. No existing work fills the void. ACT is the most complete response identifiable.

- **Hafez** (bi-predictability $P$): complementary diagnostic, no goals/dynamics. $H_b$ has no ACT analog yet — matters for legibility/coordination.
- **IBM 2025** (systems theory manifesto): calls for what ACT provides. Their open challenges (subgoal emergence, residual control rights) directly addressed by ACT.
- **BDI**: named the parts, no dynamics.
- **Active inference**: closest competitor, different foundation. Expected free energy ≈ ACT's value + $\lambda$ CIY (structural isomorphism, different foundations). ACT grounds exploration in causal information specifically.

**Lead with:** Section I (proved, simulated) + Section II (purposeful-agent derivation). These are where ACT has real substance. Sections III–V are "the theory extends to" demonstrations.

**ACT's unique contributions** (beyond repackaging):
1. The integration: control theory + causal inference + information theory + agent architecture under one framework
2. Novel results: satisfaction gap / control regret split, $G_t$ complexity bounded by $M_t$, compound probability decay as plan fragility, feedback loop as Level 2 causal access, adversarial tempo exponents, acyclicity derived from temporal ordering
3. Software as both testbed and recursive instantiation

**Discipline:** Don't overclaim. Present as a unifying framework with specific novel results. Be honest about what's integration vs. what's discovery.


## Governing Objectives

1. **Subsume TFT as the adaptive-systems foundation.** The sector-condition/Lyapunov framework is primary; the linear ODE is pedagogical. TFT is absorbed, not extended.
2. **Derive purposeful agency from first principles.** Start with the simplest abstract purposeful object and derive the need for richer structure from mathematical necessity — specifically from the causal hierarchy theorem.
3. **Make TST a rigorous software-domain instantiation of ACT.** Every claim gets epistemic tagging; ungrounded assertions are derived, retagged, or removed.
4. **Develop multi-agent dynamics to the degree needed for TST grounding.** Cooperative, adversarial, mixed. Not a complete multi-agent theory, but enough for software teams and adversarial dynamics.
5. **Maintain claim-segment structure throughout.** One claim per file, strictly incremental.


## Ungrounded Claims to Resolve

*Claims made or implied in current documents that lack their own derivation. These need to be either grounded, retagged as hypotheses, or removed.*

- "Principled implementation often costs nearly the same as quick" (TST T-06, empirical observation not derived — flagged in contents)
- "Comprehension dominates under high turnover" (TST T-05 implication, structurally motivated but quantitative relationship unformalized)
- "Code complexity accumulation rate" as instance of $\rho$ (needed to connect persistence condition to software maintainability)
- The virtuous/vicious cycle as persistence condition violation (structurally motivated, not formally derived)


## Open Questions

1. Does IB for shared intent produce non-obvious predictions about organizational communication structure?
2. Can the intent DAG handle temporal dependencies (action ordering)?
3. How does 100% context turnover interact with the intent DAG? $O_t$ and $\Sigma_t$ may survive context death even when $M_t$ doesn't.
4. Is there a derivable "comprehension vs action" optimal allocation from the dual-mismatch framework?
5. Can Hafez's $P$ be derived from ACT quantities? Can $\Delta H$ (strategic legibility) enter multi-agent dynamics? ($H_b$ has no ACT analog yet.)
6. Relationship between ACT and active inference's prior preferences?
7. Which physical domains have deterministic vs stochastic $\rho$?
8. Cognitive cost of maintaining $\Sigma_t$ (the $\beta$ analog for strategy).
9. P3→Markov step in graph uniqueness: does state-local revisability strictly force the Markov condition? See `scratch/spike-graph-uniqueness.md`.
10. Whether "code quality as observation infrastructure" is unique to software or an instance of a general pattern (agents modifying their own observation channels).


## Validation (after theory stabilizes)

- Extend nonlinear sims to characterize regime boundaries
- Developer-as-ACT-agent on real codebase (software worked example)
- Test DAG health metrics against real project outcome data
- Multi-agent intent propagation simulation
- TST testable predictions: specification bound calibration, coherence-coupling measurement
- Simulations 3–6 from old-tst-via-tft-simulation-proposals (Sims 1–2 done as track-b)
