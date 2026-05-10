# Prior Work Migration Map

Tracking of how prior-work content (TFT, TST, and TST-via-TFT bridge material) has been absorbed into the AAD framework. All TFT and TST content was copied into `old-*` files within their respective `src/` directories (`01-aad-core/src/` and `02-tst-core/src/`) as a staging step; the `old-` prefix means content is prior work that hasn't yet been fully converted to AAD format.

This file retires when the last `old-*` file is archived.

## TFT → AAD Mapping

| Old file | Content | AAD status |
|----------|---------|------------|
| ~~old-tf-readme~~ | ~~TFT overview~~ | **Archived.** Superseded by CLAUDE.md, FORMAT.md. |
| old-tf-00-notation-conventions | Symbol tables, conventions, adaptive loop phases, global assumptions, units, claim registry | **Partially absorbed.** Notation referenced by FORMAT.md. Adaptive loop phases, global assumptions table, claim registry format — AAD should have its own. |
| ~~old-tf-01-scope~~ | ~~Scope definitions~~ | **Archived.** → #def-agent-environment, #def-observation-function, #def-action-transition, #scope-adaptive-system, #scope-agency. Coupling spectrum now in #post-causal-structure. |
| ~~old-tf-02-causal-structure~~ | ~~Temporal arrow, chronica, Pearl's 3 levels, recursive update~~ | **Archived.** → #post-causal-structure, #def-pearl-causal-hierarchy, #def-chronica, #der-recursive-update. |
| ~~old-tf-03-model~~ | ~~Model, IB, sufficiency~~ | **Archived.** → #form-agent-model, #form-information-bottleneck, #def-model-sufficiency. |
| ~~old-tf-04-event-driven-dynamics~~ | ~~Event types, channels, rates~~ | **Archived.** → #form-event-driven-dynamics. |
| ~~old-tf-05-mismatch-signal~~ | ~~Prediction error, Prop 5.1~~ | **Archived.** → #def-mismatch-signal, #result-mismatch-decomposition. |
| old-tf-06-update-gain | Uncertainty ratio, domain validation, gain dynamics, overfitting as miscalibration | **Mostly absorbed** into #emp-update-gain. Domain validation tables and gain dynamics (convergence, reset) richer than AAD segment — enrich then archive. |
| ~~old-tf-07-action-selection~~ | ~~Action as model function, fluency~~ | **Archived.** → #der-action-selection. |
| ~~old-tf-08-exploration-exploitation~~ | ~~CIY, unified policy objective, query actions~~ | **Archived.** → #def-causal-information-yield. |
| ~~old-tf-09-deliberation-cost~~ | ~~Prop 9.1, deliberation threshold~~ | **Archived.** → #der-deliberation-cost. |
| ~~old-tf-10-structural-adaptation~~ | ~~Prop 10.1, destruction-creation, overfitting~~ | **Archived.** → #result-structural-adaptation-necessity + #def-model-sufficiency + #def-model-class-fitness. |
| old-tf-11-tempo-persistence | Temporal nesting table, mismatch ODE, adversarial dynamics, observation quality, per-dimension | **Mostly absorbed** across #def-adaptive-tempo, #result-persistence-condition, #result-sector-condition-stability, etc. Mismatch ODE as named hypothesis, speed-quality substitutability — enrich then archive. |
| ~~old-tf-appendix-a-lyapunov~~ | ~~Props A.1–A.3, Cor A.3.1, full proofs, Prop A.4 sketch~~ | **Absorbed.** → #deriv-sector-condition (A.1–A.2), #der-adversarial-destabilization (A.3, A.3.1), #sketch-multi-timescale-stability (A.4). Ready to archive. |
| ~~old-tf-appendix-b-operationalization~~ | ~~Estimation procedures for all TFT quantities~~ | **Absorbed.** → #detail-operationalization. Ready to archive. |
| ~~old-tf-appendix-c-kalman-example~~ | ~~Complete Kalman worked example~~ | **Absorbed.** → #example-kalman. Ready to archive. |
| ~~old-tf-appendix-d-rl-example~~ | ~~Nonstationary bandit worked example~~ | **Absorbed.** → #example-bandit. Ready to archive. |
| ~~old-tf-appendix-e-tft-core~~ | ~~Condensed formal chain~~ | **Archived.** Superseded by 01-aad-core/OUTLINE.md. |
| old-tf-appendix-f-multi-agent | Communication gain, trust, distributed tempo, topology, game theory | **Partially absorbed.** → #hyp-communication-gain (F.2 core), #der-adversarial-destabilization (uses coupling model). **Still needed from F:** distributed tempo → #der-team-persistence (F.3), topology analysis (F.4), game-theoretic integration (F.5), trust transitivity details, falsification predictions (F.7). Extract as Section III segments get built. |
| ~~old-tf-appendix-g-agent-identity~~ | ~~Non-forkability, clone problem~~ | **Archived.** → #scope-agent-identity. |
| ~~old-tf-recursive-update-derivation~~ | ~~Full uniqueness proof~~ | **Absorbed.** → #deriv-recursive-update. Ready to archive. |
| old-tf-goal-intent-gap | What TFT lacked (goals/intent) | **Historical.** The gap AAD exists to fill. Can archive when comfortable. |
| old-tf-citations-catalog | TFT reference catalog | **Reference material.** Useful for paper writing. |
| old-tf-novelty-analysis | What's novel in TFT | **Reference material.** Useful for positioning. |
| old-tf-ooda-universal-pattern | OODA as universal adaptive pattern (v7) | **Historical.** Early framing. Can archive when comfortable. |

## TST → AAD Mapping

| Old file | Content | AAD status |
|----------|---------|------------|
| ~~old-tst-readme~~ | ~~TST overview~~ | **Archived.** Superseded by 02-tst-core/OUTLINE.md. |
| ~~old-tst-01-temporal-optimality~~ | ~~T-01~~ | **Archived.** → #post-temporal-optimality (generalized). |
| ~~old-tst-02-specification-bound~~ | ~~D-01 + T-02 + C-02.1~~ | **Archived.** → #result-specification-bound, #def-feature. |
| ~~old-tst-03-evolving-scope~~ | ~~T-03~~ | **Archived.** → #scope-evolving-software. |
| ~~old-tst-04-change-expectation~~ | ~~T-04, C-04.1, C-04.2~~ | **Archived.** → #der-change-expectation-baseline. |
| ~~old-tst-05-dual-optimization~~ | ~~D-02, D-03, T-05~~ | **Archived.** → #def-comprehension-time, #def-implementation-time, #der-dual-optimization. |
| ~~old-tst-06-change-investment~~ | ~~T-06~~ | **Archived.** → #der-change-investment. |
| ~~old-tst-07-conceptual-alignment~~ | ~~T-07 + C-07.1~~ | **Archived.** → #hyp-conceptual-alignment. |
| ~~old-tst-08-changeset-size~~ | ~~D-04, T-08, C-08.1~~ | **Archived.** → #def-atomic-changeset, #emp-changeset-size-principle. |
| ~~old-tst-09-change-proximity~~ | ~~D-05, T-09, H-09.1~~ | **Archived.** → #def-discontinuity-distance, #der-change-proximity-principle, #hyp-exponential-cognitive-load. |
| ~~old-tst-10-coherence-coupling~~ | ~~D-06, D-07, T-10~~ | **Archived.** → #def-system-coupling, #def-system-coherence, #meas-coherence-coupling. |
| ~~old-tst-11-decision-integration~~ | ~~T-11~~ | **Archived.** → #der-principled-decision-integration. |
| ~~old-tst-12-continuous-operation~~ | ~~D-08, T-12~~ | **Archived.** → #def-system-availability, #scope-continuous-operation. |

## TST via-TFT Bridge Material → AAD Mapping

| Old file | Content | AAD status |
|----------|---------|------------|
| old-tst-via-tft-readme | Why the bridge exists, software's 6 unique epistemic properties, key open questions | **Partially absorbed.** The 6 properties → #obs-software-epistemic-properties. Open questions (observation channel under agent control, 100% turnover, counterfactual replay) feed TST (`02-tst-core/`) and logogenic agents (`03-logogenic-agents/`). |
| old-tst-via-tft-mapping | Detailed TFT→software mapping: environment decomposition, observation channels, action taxonomy, model, mismatch, gain, tempo, persistence, structural adaptation, multi-agent | **Richest single document for TST (`02-tst-core/`).** Action taxonomy (exploration/probe/query/modify/infrastructure-investment), three-part tempo decomposition, code-quality feedback loop, death-spiral formalization — much not yet in AAD segments. |
| old-tst-via-tft-causal-extensions | Explicit causal DAGs in software, interventional reasoning via tests, counterfactual evaluation via git, causal discovery from git, runtime causal models | **Partially absorbed** into #hyp-causal-discovery-from-git and #obs-software-epistemic-properties. Detailed treatment of dependency DAG vs empirical DAG, Level 2 channel spectrum, counterfactual machine — largely not in AAD. |
| old-tst-via-tft-reformulated-sketch | S-00 through S-14: complete outline of TST rebuilt on TFT/AAD foundations | **Valuable roadmap** for TST work (`02-tst-core/`). Shows how each TST claim maps to the AAD framework. The "what's new" and "what's removed" sections are useful for understanding the transformation. |
| old-tst-via-tft-simulation-proposals | 6 simulation proposals ordered by value/effort | **Partially executed.** Sims 1–2 done (track-b). Sims 3–6 remain as future work. |
