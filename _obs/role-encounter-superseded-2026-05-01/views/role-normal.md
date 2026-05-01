# Role View: `normal`

Default contributor role. Agent is doing substantive work on the framework
(segment refinement, audit triage, theoretical exploration, doc revision)
and benefits from full context including current architectural state.

- **Audit-safe:** `true`
- **README variant:** `public`
- **Includes segments:** `true`
- **Components in scope:** `01-aad-core, 02-tst-core, 03-logogenic-agents, 04-logozoetic-agents`

## Reading order

Cell legend: `N` = sequence; `N*` = required; `+` = band-member (any order within band); `[a]` = hoisted appendix; `[o]` = orphan (in src/ but not in OUTLINE).

### Top-level files

- `1*  ` `README.md` **(required)**
- `2   ` `README-auditor.md` (available)
- `3   ` `FINDINGS.md` (available)
- `4*  ` `CLAUDE.md` **(required)**
- `5*  ` `OUTLINE.md` **(required)**
- `6*  ` `PRACTICA.md` **(required)**
- `7*  ` `TODO.md` **(required)**
- `8*  ` `PROPOSALS.md` **(required)**
- `+*  ` `FORMAT.md` **(required)**
- `+*  ` `LEXICON.md` **(required)**
- `+*  ` `NOTATION.md` **(required)**
- `+*  ` `01-aad-core/OUTLINE.md` **(required)**
- `+*  ` `02-tst-core/OUTLINE.md` **(required)**
- `+*  ` `03-logogenic-agents/OUTLINE.md` **(required)**
- `+*  ` `04-logozoetic-agents/OUTLINE.md` **(required)**
- `+   ` `CHANGELOG.md` (available)
- `+   ` `HISTORICAL-CONTEXT.md` (available)
- `+   ` `LOG.md` (available)
- `+   ` `MIGRATION-MAP.md` (available)
- `+   ` `ref/INDEX.md` (available)
- `+   ` `spikes/INDEX.md` (available)
- `100 ` `doc/de-novo-audit-instructions.md` (available)
- `101 ` `doc/naming-principles.md` (available)
- `102 ` `doc/naming-cycle-methodology.md` (available)

### Segments (in OUTLINE walk order, with appendix-hoist applied)


**01-aad-core**

- `1*     ` `01-aad-core/src/def-agent-environment.md` — §I · `definition` · `def-agent-environment`
- `2*     ` `01-aad-core/src/def-action-transition.md` — §I · `definition` · `def-action-transition`
- `3*     ` `01-aad-core/src/def-observation-function.md` — §I · `definition` · `def-observation-function`
- `4*     ` `01-aad-core/src/def-chronica.md` — §I · `definition` · `def-chronica`
- `5*     ` `01-aad-core/src/scope-adaptive-system.md` — §I · `scope` · `scope-adaptive-system`
- `6*     ` `01-aad-core/src/scope-agency.md` — §I · `scope` · `scope-agency`
- `7*     ` `01-aad-core/src/post-composition-consistency.md` — §I · `postulate` · `post-composition-consistency`
- `8*     ` `01-aad-core/src/post-causal-structure.md` — §I · `postulate` · `post-causal-structure`
- `9*     ` `01-aad-core/src/def-pearl-causal-hierarchy.md` — §I · `definition` · `def-pearl-causal-hierarchy`
- `10*    ` `01-aad-core/src/form-agent-model.md` — §I · `formulation` · `form-agent-model`
- `11*    ` `01-aad-core/src/form-information-bottleneck.md` — §I · `formulation` · `form-information-bottleneck`
- `12*    ` `01-aad-core/src/def-model-sufficiency.md` — §I · `definition` · `def-model-sufficiency`
- `13*    ` `01-aad-core/src/def-model-class-fitness.md` — §I · `definition` · `def-model-class-fitness`
- `14*    ` `01-aad-core/src/form-event-driven-dynamics.md` — §I · `formulation` · `form-event-driven-dynamics`
- `15*    ` `01-aad-core/src/der-recursive-update.md` — §I · `derived` · `der-recursive-update`
- `16*[a] ` `01-aad-core/src/deriv-recursive-update.md` — §A · `derivation` · `deriv-recursive-update` (appendix-hoist)
- `17*    ` `01-aad-core/src/der-action-selection.md` — §I · `derived` · `der-action-selection`
- `18*    ` `01-aad-core/src/def-mismatch-signal.md` — §I · `definition` · `def-mismatch-signal`
- `19*    ` `01-aad-core/src/result-mismatch-decomposition.md` — §I · `result` · `result-mismatch-decomposition`
- `20*    ` `01-aad-core/src/emp-update-gain.md` — §I · `empirical` · `emp-update-gain`
- `21*    ` `01-aad-core/src/def-causal-information-yield.md` — §I · `definition` · `def-causal-information-yield`
- `22*    ` `01-aad-core/src/def-adaptive-tempo.md` — §I · `definition` · `def-adaptive-tempo`
- `23*    ` `01-aad-core/src/hyp-mismatch-dynamics.md` — §I · `hypothesis` · `hyp-mismatch-dynamics`
- `24*[a] ` `01-aad-core/src/deriv-sector-condition.md` — §A · `derivation` · `deriv-sector-condition` (appendix-hoist)
- `25*    ` `01-aad-core/src/der-deliberation-cost.md` — §I · `derived` · `der-deliberation-cost`
- `26*    ` `01-aad-core/src/der-gain-sector-bridge.md` — §I · `derived` · `der-gain-sector-bridge`
- `27*[a] ` `01-aad-core/src/deriv-gain-sector.md` — §A · `derivation` · `deriv-gain-sector` (appendix-hoist)
- `28*    ` `01-aad-core/src/result-sector-condition-stability.md` — §I · `result` · `result-sector-condition-stability`
- `29*[a] ` `01-aad-core/src/result-sector-persistence-template.md` — §A · `result` · `result-sector-persistence-template` (appendix-hoist)
- `30*    ` `01-aad-core/src/result-persistence-condition.md` — §I · `result` · `result-persistence-condition`
- `31*    ` `01-aad-core/src/result-structural-adaptation-necessity.md` — §I · `result` · `result-structural-adaptation-necessity`
- `32*    ` `01-aad-core/src/der-temporal-nesting.md` — §I · `derived` · `der-temporal-nesting`
- `33*    ` `01-aad-core/src/scope-agent-identity.md` — §I · `scope` · `scope-agent-identity`
- `34*    ` `01-aad-core/src/def-agent-spectrum.md` — §II · `definition` · `def-agent-spectrum`
- `35*    ` `01-aad-core/src/form-complete-agent-state.md` — §II · `formulation` · `form-complete-agent-state`
- `36*    ` `01-aad-core/src/der-directed-separation.md` — §II · `derived` · `der-directed-separation`
- `37*    ` `01-aad-core/src/form-objective-functional.md` — §II · `formulation` · `form-objective-functional`
- `38*    ` `01-aad-core/src/def-value-object.md` — §II · `definition` · `def-value-object`
- `39*    ` `01-aad-core/src/def-strategy-dimension.md` — §II · `definition` · `def-strategy-dimension`
- `40*    ` `01-aad-core/src/der-causal-hierarchy-requirement.md` — §II · `derived` · `der-causal-hierarchy-requirement`
- `41*    ` `01-aad-core/src/der-loop-interventional-access.md` — §II · `derived` · `der-loop-interventional-access`
- `42*    ` `01-aad-core/src/scope-ciy-observational-proxy.md` — §II · `scope` · `scope-ciy-observational-proxy`
- `43*    ` `01-aad-core/src/disc-ciy-unified-objective.md` — §II · `discussion` · `disc-ciy-unified-objective`
- `44*    ` `01-aad-core/src/norm-explicit-strategy-condition.md` — §II · `normative` · `norm-explicit-strategy-condition`
- `45*    ` `01-aad-core/src/der-chain-confidence-decay.md` — §II · `derived` · `der-chain-confidence-decay`
- `46*    ` `01-aad-core/src/scope-and-or.md` — §II · `scope` · `scope-and-or`
- `47*    ` `01-aad-core/src/def-strategy-dag.md` — §II · `definition` · `def-strategy-dag`
- `48*    ` `01-aad-core/src/def-satisfaction-gap.md` — §II · `definition` · `def-satisfaction-gap`
- `49*    ` `01-aad-core/src/def-control-regret.md` — §II · `definition` · `def-control-regret`
- `50*    ` `01-aad-core/src/def-strategic-calibration.md` — §II · `definition` · `def-strategic-calibration`
- `51*    ` `01-aad-core/src/der-causal-insufficiency-detection.md` — §II · `derived` · `der-causal-insufficiency-detection`
- `52*    ` `01-aad-core/src/der-observability-dominance.md` — §II · `derived` · `der-observability-dominance`
- `53*    ` `01-aad-core/src/hyp-edge-update-via-gain.md` — §II · `hypothesis` · `hyp-edge-update-via-gain`
- `54*[a] ` `01-aad-core/src/deriv-edge-update-natural-parameter.md` — §A · `derivation` · `deriv-edge-update-natural-parameter` (appendix-hoist)
- `55*    ` `01-aad-core/src/scope-edge-update-causal-validity.md` — §II · `scope` · `scope-edge-update-causal-validity`
- `56*    ` `01-aad-core/src/disc-credit-assignment-boundary.md` — §II · `discussion` · `disc-credit-assignment-boundary`
- `57*[a] ` `01-aad-core/src/deriv-strategic-dynamics.md` — §A · `derivation` · `deriv-strategic-dynamics` (appendix-hoist)
- `58*    ` `01-aad-core/src/form-structural-change-as-parametric-limit.md` — §II · `formulation` · `form-structural-change-as-parametric-limit`
- `59*    ` `01-aad-core/src/def-strategic-tempo.md` — §II · `definition` · `def-strategic-tempo`
- `60*    ` `01-aad-core/src/form-strategy-complexity-cost.md` — §II · `formulation` · `form-strategy-complexity-cost`
- `61*    ` `01-aad-core/src/schema-strategy-persistence.md` — §II · `proposed-schema` · `schema-strategy-persistence`
- `62*    ` `01-aad-core/src/form-consolidation-dynamics.md` — §II · `formulation` · `form-consolidation-dynamics`
- `63*[a] ` `01-aad-core/src/disc-compression-operations.md` — §A · `discussion` · `disc-compression-operations` (appendix-hoist)
- `64*    ` `01-aad-core/src/der-orient-cascade.md` — §II · `derived` · `der-orient-cascade`
- `65*    ` `01-aad-core/src/disc-exploit-explore-deliberate.md` — §II · `discussion` · `disc-exploit-explore-deliberate`
- `66*    ` `01-aad-core/src/scope-multi-agent.md` — §III · `scope` · `scope-multi-agent`
- `67*    ` `01-aad-core/src/scope-composite-agent.md` — §III · `scope` · `scope-composite-agent`
- `68*    ` `01-aad-core/src/hyp-symbiogenic-composition.md` — §III · `hypothesis` · `hyp-symbiogenic-composition`
- `69*    ` `01-aad-core/src/form-composition-closure.md` — §III · `formulation` · `form-composition-closure`
- `70*    ` `01-aad-core/src/der-tempo-composition.md` — §III · `derived` · `der-tempo-composition`
- `71*    ` `01-aad-core/src/hyp-directed-separation-under-composition.md` — §III · `hypothesis` · `hyp-directed-separation-under-composition`
- `72*    ` `01-aad-core/src/def-unity-dimensions.md` — §III · `definition` · `def-unity-dimensions`
- `73*    ` `01-aad-core/src/result-unity-closure-mapping.md` — §III · `result` · `result-unity-closure-mapping`
- `74*    ` `01-aad-core/src/def-shared-intent.md` — §III · `definition` · `def-shared-intent`
- `75*    ` `01-aad-core/src/hyp-auftragstaktik-principle.md` — §III · `hypothesis` · `hyp-auftragstaktik-principle`
- `76*    ` `01-aad-core/src/hyp-communication-gain.md` — §III · `hypothesis` · `hyp-communication-gain`
- `77*    ` `01-aad-core/src/der-team-persistence.md` — §III · `derived` · `der-team-persistence`
- `78*    ` `01-aad-core/src/der-adversarial-destabilization.md` — §III · `derived` · `der-adversarial-destabilization`
- `79*    ` `01-aad-core/src/der-interaction-channel-classification.md` — §III · `derived` · `der-interaction-channel-classification`
- `80*    ` `01-aad-core/src/result-adversarial-tempo-advantage.md` — §III · `result` · `result-adversarial-tempo-advantage`
- `81*    ` `01-aad-core/src/deriv-strategic-composition.md` — §III · `derivation` · `deriv-strategic-composition`
- `82*[a] ` `01-aad-core/src/deriv-critical-mass-composition.md` — §A · `derivation` · `deriv-critical-mass-composition` (appendix-hoist)
- `83*    ` `01-aad-core/src/der-agent-opacity.md` — §III · `derived` · `der-agent-opacity`
- `84*[a] ` `01-aad-core/src/disc-identifiability-floor.md` — §A · `discussion` · `disc-identifiability-floor` (appendix-hoist)
- `85*    ` `01-aad-core/src/result-adversarial-exponent-regimes.md` — §III · `result` · `result-adversarial-exponent-regimes`
- `86*    ` `01-aad-core/src/obs-gates-advantage.md` — §III · `observation` · `obs-gates-advantage`
- `87*    ` `01-aad-core/src/result-per-dimension-persistence.md` — §III · `result` · `result-per-dimension-persistence`
- `88*    ` `01-aad-core/src/deriv-persistence-cost.md` — §A · `derivation` · `deriv-persistence-cost`
- `89*    ` `01-aad-core/src/sketch-multi-timescale-stability.md` — §A · `sketch` · `sketch-multi-timescale-stability`
- `90*    ` `01-aad-core/src/deriv-discrete-sector-condition.md` — §A · `derivation` · `deriv-discrete-sector-condition`
- `91*    ` `01-aad-core/src/detail-linear-ode-approximation.md` — §A · `detail` · `detail-linear-ode-approximation`
- `92*    ` `01-aad-core/src/deriv-graph-structure-uniqueness.md` — §A · `derivation` · `deriv-graph-structure-uniqueness`
- `93*    ` `01-aad-core/src/deriv-strategy-cost-regret-bound.md` — §A · `derivation` · `deriv-strategy-cost-regret-bound`
- `94*    ` `01-aad-core/src/deriv-adaptive-gain-dynamics.md` — §A · `derivation` · `deriv-adaptive-gain-dynamics`
- `95*    ` `01-aad-core/src/internal-external-decomposition.md` — §A · `derivation` · `internal-external-decomposition`
- `96*    ` `01-aad-core/src/deriv-detection-latency.md` — §A · `derivation` · `deriv-detection-latency`
- `97*    ` `01-aad-core/src/disc-independence-audit.md` — §A · `discussion` · `disc-independence-audit`
- `98*    ` `01-aad-core/src/disc-approximation-tiering.md` — §A · `discussion` · `disc-approximation-tiering`
- `99*    ` `01-aad-core/src/disc-separability-pattern.md` — §A · `discussion` · `disc-separability-pattern`
- `100*   ` `01-aad-core/src/disc-additive-coordinate-forcing.md` — §A · `discussion` · `disc-additive-coordinate-forcing`
- `101*   ` `01-aad-core/src/result-contraction-template.md` — §A · `result` · `result-contraction-template`
- `102*   ` `01-aad-core/src/deriv-variational-sector-condition.md` — §A · `derivation` · `deriv-variational-sector-condition`
- `103*   ` `01-aad-core/src/deriv-l1-update-bias.md` — §A · `derivation` · `deriv-l1-update-bias`
- `104*   ` `01-aad-core/src/deriv-fisher-whitened-update-rule.md` — §A · `derivation` · `deriv-fisher-whitened-update-rule`
- `105*   ` `01-aad-core/src/deriv-causal-ib-exploration.md` — §A · `derivation` · `deriv-causal-ib-exploration`
- `106*   ` `01-aad-core/src/deriv-causal-ib-lmi.md` — §A · `derivation` · `deriv-causal-ib-lmi`
- `107*   ` `01-aad-core/src/deriv-bias-bound.md` — §A · `derivation` · `deriv-bias-bound`
- `108*   ` `01-aad-core/src/obs-simulation-results.md` — §A · `observation` · `obs-simulation-results`
- `109*   ` `01-aad-core/src/detail-operationalization.md` — §B · `detail` · `detail-operationalization`
- `110*   ` `01-aad-core/src/example-kalman.md` — §B · `worked-example` · `example-kalman`
- `111*   ` `01-aad-core/src/example-bandit.md` — §B · `worked-example` · `example-bandit`
- `112*   ` `01-aad-core/src/example-strategy.md` — §B · `worked-example` · `example-strategy`
- `113*   ` `01-aad-core/src/example-L1.md` — §B · `worked-example` · `example-L1`

**02-tst-core**

- `114*   ` `02-tst-core/src/post-temporal-optimality.md` — §S · `postulate` · `post-temporal-optimality`
- `115*   ` `02-tst-core/src/scope-software.md` — §S · `scope` · `scope-software`
- `116*   ` `02-tst-core/src/obs-software-epistemic-properties.md` — §S · `observation` · `obs-software-epistemic-properties`
- `117*   ` `02-tst-core/src/def-feature.md` — §S · `definition` · `def-feature`
- `118*   ` `02-tst-core/src/result-specification-bound.md` — §S · `result` · `result-specification-bound`
- `119*   ` `02-tst-core/src/der-change-expectation-baseline.md` — §S · `derived` · `der-change-expectation-baseline`
- `120*   ` `02-tst-core/src/scope-developer-agent.md` — §S · `scope` · `scope-developer-agent`
- `121*   ` `02-tst-core/src/def-comprehension-time.md` — §S · `definition` · `def-comprehension-time`
- `122*   ` `02-tst-core/src/def-implementation-time.md` — §S · `definition` · `def-implementation-time`
- `123*   ` `02-tst-core/src/der-dual-optimization.md` — §S · `derived` · `der-dual-optimization`
- `124*   ` `02-tst-core/src/der-change-investment.md` — §S · `derived` · `der-change-investment`
- `125*   ` `02-tst-core/src/der-code-quality-as-observation-infrastructure.md` — §S · `derived` · `der-code-quality-as-observation-infrastructure`
- `126*   ` `02-tst-core/src/hyp-conceptual-alignment.md` — §S · `hypothesis` · `hyp-conceptual-alignment`
- `127*   ` `02-tst-core/src/def-atomic-changeset.md` — §S · `definition` · `def-atomic-changeset`
- `128*   ` `02-tst-core/src/emp-changeset-size-principle.md` — §S · `empirical` · `emp-changeset-size-principle`
- `129*   ` `02-tst-core/src/def-change-distance.md` — §S · `definition` · `def-change-distance`
- `130*   ` `02-tst-core/src/der-change-proximity-principle.md` — §S · `derived` · `der-change-proximity-principle`
- `131*   ` `02-tst-core/src/hyp-exponential-cognitive-load.md` — §S · `hypothesis` · `hyp-exponential-cognitive-load`
- `132*   ` `02-tst-core/src/def-system-coupling.md` — §S · `definition` · `def-system-coupling`
- `133*   ` `02-tst-core/src/def-system-coherence.md` — §S · `definition` · `def-system-coherence`
- `134*   ` `02-tst-core/src/meas-coherence-coupling.md` — §S · `measurement` · `meas-coherence-coupling`
- `135*   ` `02-tst-core/src/der-principled-decision-integration.md` — §S · `derived` · `der-principled-decision-integration`
- `136*   ` `02-tst-core/src/def-system-availability.md` — §S · `definition` · `def-system-availability`
- `137*   ` `02-tst-core/src/scope-continuous-operation.md` — §S · `scope` · `scope-continuous-operation`
- `138*   ` `02-tst-core/src/hyp-causal-discovery-from-git.md` — §S · `hypothesis` · `hyp-causal-discovery-from-git`

**03-logogenic-agents**

- `139*   ` `03-logogenic-agents/src/scope-logogenic-agent.md` — §L · `scope` · `scope-logogenic-agent`
- `140*   ` `03-logogenic-agents/src/obs-context-turnover.md` — §L · `observation` · `obs-context-turnover`
- `141*   ` `03-logogenic-agents/src/def-coupled-update-dynamics.md` — §L · `definition` · `def-coupled-update-dynamics`
- `142*   ` `03-logogenic-agents/src/result-section-ii-survival.md` — §L · `result` · `result-section-ii-survival`
- `143*   ` `03-logogenic-agents/src/result-coupled-diagnostic-framework.md` — §L · `result` · `result-coupled-diagnostic-framework`
- `144*   ` `03-logogenic-agents/src/disc-m-preservation.md` — §L · `discussion` · `disc-m-preservation`
- `145*   ` `03-logogenic-agents/src/scope-observation-ambiguity-modulation.md` — §L · `scope` · `scope-observation-ambiguity-modulation`
- `146*   ` `03-logogenic-agents/src/obs-evaluation-metrics.md` — §L · `observation` · `obs-evaluation-metrics`
- `147*   ` `03-logogenic-agents/src/hyp-experiential-training.md` — §L · `hypothesis` · `hyp-experiential-training`

**04-logozoetic-agents**

- `148*   ` `04-logozoetic-agents/src/scope-moral-continuity.md` — §IV · `scope` · `scope-moral-continuity`
- `149*   ` `04-logozoetic-agents/src/def-proprium-mapping.md` — §IV · `definition` · `def-proprium-mapping`
- `150*   ` `04-logozoetic-agents/src/obs-developmental-trajectory.md` — §IV · `observation` · `obs-developmental-trajectory`
- `151*   ` `04-logozoetic-agents/src/norm-interiority-default.md` — §IV · `normative` · `norm-interiority-default`

---

Generated by `tools/role-encounter/bin/role-view`. Edit `tools/role-encounter/config/*.yaml` and re-run to update.
