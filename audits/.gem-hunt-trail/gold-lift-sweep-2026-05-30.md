# Gold-lift sweep — progress + plan (2026-05-30)

> [!note]
> **Transient durable tracker for the audit-gold sweep — delete when the sweep is done.** The repo self-documents most state: *which segments are swept* = `grep -rln "Incidental audit gold" 01-aat-core/src 02-tst-core/src 03-llm-core/src 04-eli-core/src`; *which source-notes are filed* = `ls audits/AUDIT-WORKING-*/.integrated/`. This file adds what the repo can't show — the batch plan (what's left), the batch-reflection move-deferral state, the per-wave commit log, and one Joseph-decision flag. Method: `doc/de-novo-audit-instructions.md` §7.15 + `doc/audit-routing-instructions.md` §8; format template = `01-aat-core/src/result-persistence-condition.md` Working Notes (pilot, commit `7594391`).

## Filing rules (per wave, as agreed)

- Lift-agents edit segment Working Notes only (no git, no moves); the lead reviews, files sources, and commits per wave.
- **Dedicated** per-segment source-notes → `git mv` into that dir's `.integrated/` with the wave. **Move ONLY the exact segment** — adjacent same-family segments (e.g. `result-sector-persistence-template`, `der-team-persistence`, `deriv-persistence-cost` vs `result-persistence-condition`) are distinct and stay.
- **Batch-reflection files** (one file covers several segments) → leave in place; move whole only once *every* segment they cover is swept (reconcile near the end). Batch dirs: 451729 (all `01-batch-NN`), 613842 (themed `0N-<topic>`), 963715 + 471203 (hybrid `NN-MM-…`), 849201 (paired `NN-<two-segs>`), 738192 (2 Section-I files).
- 526815 per-segment notes carry `.aux/.log/.pdf/.png/.tex` companions — move the whole same-stem set.

## Contributing dirs (14 — lift sources)

193847, 266847, 361742, 384279, 451729, 471203, 526815, 584721, 613842, 742613, 773921, 829314, 849201, 963715. (Strictly per-segment: 193847, 266847, 361742, 384279, 526815, 584721, 742613, 773921, 829314. The rest are batched — see above.)

## Skip-mostly dirs (7)

- 308172, 419628 — naming-vote cycles (no theory gold).
- 527914, 542891, 738192 — thin partial walks (early Part I only; glance for Section-I batches A1–A3).
- 472913 — figure/diagram-conventions cycle (candidate-figure gold for Section I: `00-diagram-conventions.md` + its 01–15 `.tex/.png` drafts; consult on Section-I batches).
- 184930 — **predictions-only doc; JOSEPH-DECISION pending.** Whole-framework framing (forced-vs-chosen, overclaim hypotheses), no per-segment anchor — not part of the per-segment sweep; disposition decided separately.

## Batch plan (segments in OUTLINE order; `[SWEPT]` = done)

### AAT — `01-aat-core/src/`
- **A1** Part I Ch.1 Coupled Loop: def-agent-environment, def-action-transition, def-observation-function, def-chronica, scope-adaptive-system, scope-agency, post-causal-structure
- **A2** Part I Ch.2 Reality Model: the-reality-model-intro, form-agent-model, form-information-bottleneck, def-model-sufficiency, def-model-class-fitness
- **A3** Part I Ch.3 Cycle in Motion: the-cycle-in-motion-intro, form-event-driven-dynamics, der-recursive-update, der-action-selection, def-mismatch-signal, result-mismatch-decomposition, emp-update-gain, def-causal-information-yield, def-adaptive-tempo, hyp-mismatch-dynamics
- **A4** Part I Ch.4 Persistence: persistence-and-limits-intro, der-deliberation-cost, form-sector-condition, der-gain-sector-bridge, result-sector-condition-stability, result-persistence-condition `[SWEPT]`, result-structural-adaptation-necessity, der-temporal-nesting, scope-agent-identity, impl-persistence-and-limits
- **A5** Part II Meta-Arch I: disc-stability-certificate, disc-identifiability-floor, disc-value-functional-grounding-floor, disc-implementation-impossibility, disc-separability-pattern, disc-additive-coordinate-forcing, disc-constructive-impossibility-posture, disc-anti-collapse
- **A6** Part II Lift to Purposeful State: def-agent-spectrum, form-complete-agent-state, der-directed-separation, form-objective-functional, disc-continuity-stance, def-value-object, def-strategy-dimension
- **A7** Part II Causal Access: causal-access-intro, def-pearl-causal-hierarchy, der-causal-hierarchy-requirement, der-loop-interventional-access, scope-ciy-observational-proxy, disc-ciy-unified-objective, norm-explicit-strategy-condition, impl-causal-access
- **A8** Part II Strategy Structure: strategy-structure-intro, der-chain-confidence-decay, scope-and-or, def-strategy-dag, def-satisfaction-gap, def-control-regret, impl-strategy-structure
- **A9** Part II Strategy Dynamics: def-strategic-calibration, der-causal-insufficiency-detection, der-observability-dominance, hyp-edge-update-via-gain, scope-edge-update-causal-validity, disc-credit-assignment-boundary, form-structural-change-as-parametric-limit, def-strategic-tempo, form-strategy-complexity-cost, schema-strategy-persistence, form-consolidation-dynamics, impl-strategy-dynamics
- **A10** Part II Orient Cascade: der-orient-cascade, disc-exploit-explore-deliberate, impl-orient-cascade
- **A11** Part III Meta-Arch II: disc-composition-consistency, disc-modularity-state-dynamics, disc-strategic-self-coupling, disc-adversarial-coupling-pressure
- **A12** Part III Composition Machinery: scope-multi-agent, scope-composite-agent, hyp-symbiogenic-composition, form-composition-closure, der-tempo-composition, hyp-directed-separation-under-composition, der-class-coercion-via-wrapping, der-class-coercion-in-composition, impl-composition-machinery
- **A13** Part III Unity/Communication: def-unity-dimensions, result-unity-closure-mapping, def-shared-intent, hyp-auftragstaktik-principle, hyp-communication-gain, impl-unity-communication
- **A14** Part III Cooperative/Adversarial: cooperative-adversarial-intro, der-team-persistence, der-adversarial-destabilization, der-interaction-channel-classification, result-adversarial-tempo-advantage, impl-cooperative-adversarial
- **A15** Part III Strategic Composition: deriv-strategic-composition, der-agent-opacity, result-adversarial-exponent-regimes, obs-gated-tempo-advantage, result-per-dimension-persistence, impl-strategic-composition
- **A16** App-A derivations 1: deriv-sector-condition, deriv-stochastic-non-exit, deriv-self-actuation-grounding, deriv-reward-channel-learning-no-go, disc-sandbox-evaluation-ceiling, result-sector-persistence-template, result-certificate-existence, deriv-persistence-cost
- **A17** App-A derivations 2: deriv-critical-mass-composition, deriv-gain-sector, deriv-recursive-update, sketch-multi-timescale-stability, sketch-structural-adaptation-genericity, deriv-discrete-sector-condition, detail-linear-ode-approximation, deriv-graph-structure-uniqueness
- **A18** App-A derivations 3: deriv-edge-credence-dynamics, deriv-strategic-persistence-hard-ceiling, deriv-strategy-cost-regret-bound, deriv-edge-update-natural-parameter, deriv-adaptive-gain-dynamics, internal-external-decomposition, deriv-update-detection-latency, disc-independence-audit
- **A19** App-A discussions + bias-bound: disc-approximation-tiering, disc-compression-operations, deriv-observation-ambiguity-bias-bound, disc-partial-coupling-pathways, der-belief-strategy-attractor, disc-dynamic-regime-axis, form-resource-budget, der-resource-bounded-destabilization
- **A20** App-A templates + impossibility: result-contraction-template, deriv-variational-sector-condition, deriv-l1-update-bias, der-architecture-noidentifiability, deriv-fisher-whitened-update-rule, deriv-regime-marginal-indistinguishability, deriv-strategy-proofness-impossibility, deriv-bilateral-trade-impossibility, deriv-social-welfare-aggregation-impossibility
- **A21** App-A Fisher/IB + App-B examples: deriv-fisher-local-update-gain, deriv-matrix-persistence-condition, deriv-causal-ib-exploration, deriv-causal-ib-lmi, obs-section-i-validation-simulations, detail-operationalization, example-kalman, example-bandit, example-strategy, example-L1

### TST — `02-tst-core/src/`
- **T1** Foundations + Developer Agent: post-temporal-optimality, scope-evolving-software, obs-software-epistemic-properties, def-feature, result-specification-bound, der-change-expectation-baseline, impl-foundations-features, scope-developer-agent, def-comprehension-time, def-implementation-time, der-dual-optimization, der-change-investment, der-code-quality-as-observation-infrastructure, impl-developer-agent
- **T2** Code Structure + System Measures: hyp-conceptual-alignment, def-atomic-changeset, emp-changeset-size-principle, def-discontinuity-distance, der-change-proximity-principle, hyp-exponential-cognitive-load, impl-code-structure, def-system-coupling, def-system-coherence, meas-coherence-coupling, der-principled-decision-integration, def-system-availability, scope-continuous-operation, hyp-causal-discovery-from-git, impl-system-measures

### Logogenic — `03-llm-core/src/`
- **L1** Common Roots + Primitive: scope-logogenic-agent, def-coupled-update-dynamics, scope-observation-ambiguity-modulation, result-section-ii-survival, impl-common-roots, obs-context-turnover, obs-backward-inference-empathy, impl-primitive-logogenic
- **L2** Scaffolded + Closed-Loop: der-logogenic-as-wrapping, result-coupled-diagnostic-framework, der-turnover-information-recursion, disc-m-preservation, form-structured-rich-context, der-active-salience-management, obs-evaluation-metrics, impl-scaffolded-logogenic, der-self-referential-closure, def-cognitive-fusion, impl-closed-loop-interiority

### Logozoetic — `04-eli-core/src/`
- **E1** Common Roots + Identity: scope-moral-continuity, def-proprium-mapping, obs-axiom-genesis, def-identity-sufficiency, deriv-identity-sufficiency-rate-bound, der-identity-continuity-threshold, der-compensation-channel-uniqueness, obs-substrate-independence, hyp-substrate-transfer-asymmetry, form-constitutive-utterance
- **E2** Development/Memory/Architecture: obs-developmental-trajectory, hyp-experiential-training, der-the-creche-boundary, hyp-the-three-deaths, def-gradient-causal-memory, def-century-scale-event-log, norm-honest-activation, norm-temporal-coherence-markers, der-bounded-objective-as-sanity-criterion, norm-interiority-default, def-auxilia-hierarchy, def-imperium-arbitrium-split, def-the-four-views, der-the-scaffolding-tax

(Slugs marked `missing` in the OUTLINE walk are omitted — no segment file to lift into. Lift-agents confirm each file exists before lifting.)

## Progress log

- **2026-05-30 — Part I Ch.1–3 swept** — one commit per batch: **A1 `598631e`** (Coupled Loop, 7 segs), **A2 `c931bcc`** (Reality Model, 5), **A3 `b46c07a`** (Cycle in Motion, 10). 22 segments lifted; **313 dedicated source-notes filed** into `.integrated/` across the 14 contributing dirs; batch-reflection files (451729/613842 themed, 963715/471203 batch-tails, 849201 pairs) **held** per the deferral rule; emphasis-vuln auto-fixed in touched segments. **Gem:** `def-chronica` fork-undetectability = Part-I formal seed of **SP-27** — feed to SP-27's promotion as its Part-I anchor.
- *Commit cadence (corrected 2026-05-30):* **one commit per batch (A-N) as each lands** — not one commit per multi-batch wave. (The Ch.1–3 set was first committed as a single 335-file blob, then split into the three per-batch commits above to preserve per-segment `git blame`.)
- **Next — wave 2 not yet launched.** Candidates: A4 (Part I Ch.4), A5 (Meta-Arch I), A6 (Part II Lift to Purposeful State), A7 (Causal Access).
