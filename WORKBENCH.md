# WORKBENCH — AAD Theory Development

Working notes for theory development. This is a thinking tool, not a reference document. For the canonical theory structure, see `01-aad-core/OUTLINE.md`.


## Review Feedback — 2026-03-13 (PRIORITY)

Three independent frontier-model reviews (Claude Opus, OpenAI Codex, Google Gemini) converged on the same core issues. Full consolidated feedback with attribution: **[`msc/2026-03-13-feedback.md`](msc/2026-03-13-feedback.md)**

**Top issues to address (ranked by severity):**

1. **HIGH — Directed separation blocks the main application class.** LLM agents violate it; Section V is blocked. ~~Need: coupling-strength parameter $\kappa$, graded analysis of orient-cascade degradation, or explicit scoping decision.~~ **2026-03-14 update:** Resolved as architectural classification (not κ-as-scalar). **2026-04-01 update:** Architectural classification promoted from Working Notes to Formal Expression in #directed-separation, with $\kappa_{\text{processing}}$ operationalization. CIY admissibility regimes promoted to Formal Expression. Routing structure formalized in #multi-agent-scope. Composition cases in #directed-separation-under-composition.
2. ~~**HIGH — Persistence claim ($\mathcal{T}$) is stronger than its proof ($\alpha$).** The $\alpha = \mathcal{T}$ substitution is exact only for linear correction. Audit downstream uses.~~ **FIXED 2026-03-14.** #persistence-condition now presents general α > ρ/R first, with T form as linear special case. α-T relationship documented for each correction function class. δ_critical and R clarified as domain parameters.
3. **HIGH — Composition is foundational before its bridge theorem exists.** Closure-defect → trajectory-error bound is unresolved. Section III reads more settled than it is. **2026-03-14 update:** 2-agent bridge lemma spike written (`msc/spike-composition-bridge-2agent.md`). **2026-04-01 update:** Bridge lemma sketched in #composition-closure — sector condition (A4) implies trajectory error bounded at $\varepsilon^\ast / \alpha_c$, same Lyapunov argument as Prop A.1. Admissibility (A1)-(A4) specified. Sketch status — discrete-time formalization pending. **2026-04-02 update:** Full correlated Kalman derivation (`msc/spike-composition-correlated-kalman.md`) shows $\varepsilon^\ast = 0$ at steady state for ALL $\rho$. Prior claim that $\varepsilon^\ast \propto |\rho|$ was incorrect — the performance gap $\Delta_{\text{perf}} \propto \rho^2$ is a separate quantity (optimality, not representability). First genuine $\varepsilon^\ast > 0$ identified from purposeful substates (Beta-Bernoulli divergent auxiliary state).
4. ~~**MEDIUM-HIGH — Graph uniqueness not at theorem strength.**~~ **RESOLVED 2026-04-06.** P3→Markov fully proved via the Causal Markov Condition theorem (Spirtes, Glymour & Scheines 2000, Theorem 3.4; Pearl 2009, Theorem 1.4.1). The argument: P1 (causal edges) + P2 (probabilistic) establish a structural causal model; causal sufficiency guarantees exogenous independence; the CMC theorem proves the Markov factorization. P3 (local revisability) is now a *consequence*, not a premise. Additionally: CMC proof connects edge independence to causal sufficiency, grounding the Correlation Hierarchy (L0/L1/L2) in #strategy-dag.
5. **MEDIUM-HIGH — Section IV overstates causal status of git data.** #causal-discovery-from-git is missing. Frame as empirical program, not secure operationalization.
6. ~~**MEDIUM — Several formal issues:** CIY proxy sign-indefiniteness, complete-agent-state uniqueness claim, edge-independence assumption in strategy-dag, strategic-calibration type problem, $\delta_{\text{critical}}$/$R$ as inputs not outputs.~~ **ALL FIXED 2026-03-14.** CIY proxy safety conditions added. Uniqueness claim softened to conjecture. Edge-independence caveat elevated. Credit-assignment problem added. δ_critical/R clarified.

**Editorial:** All three reviewers recommend splitting presentation into (a) core results, (b) conditional architecture, (c) empirical programs. This is the single highest-leverage presentation change.


## Segment Status

### Written — Section I (28 segments, all written)

*Note: The authoritative stage for each segment is the `stage` field in its YAML frontmatter. The OUTLINE.md stage column should match. This WORKBENCH table is a summary; when in doubt, check the segment file.*

| Slug | Type | Stage |
|------|------|-------|
| [agent-environment](01-aad-core/src/agent-environment.md) | Definition | deps-verified |
| [observation-function](01-aad-core/src/observation-function.md) | Definition | deps-verified |
| [action-transition](01-aad-core/src/action-transition.md) | Definition | deps-verified |
| [scope-condition](01-aad-core/src/scope-condition.md) | Scope | claims-verified |
| [composition-consistency](01-aad-core/src/composition-consistency.md) | Postulate | deps-verified |
| [causal-structure](01-aad-core/src/causal-structure.md) | Postulate | deps-verified |
| [pearl-causal-hierarchy](01-aad-core/src/pearl-causal-hierarchy.md) | Definition | deps-verified |
| [chronica](01-aad-core/src/chronica.md) | Definition | deps-verified |
| [agent-model](01-aad-core/src/agent-model.md) | Formulation | deps-verified |
| [information-bottleneck](01-aad-core/src/information-bottleneck.md) | Formulation | deps-verified |
| [model-sufficiency](01-aad-core/src/model-sufficiency.md) | Definition | deps-verified |
| [model-class-fitness](01-aad-core/src/model-class-fitness.md) | Definition | deps-verified |
| [event-driven-dynamics](01-aad-core/src/event-driven-dynamics.md) | Formulation | deps-verified |
| [recursive-update](01-aad-core/src/recursive-update.md) | Derived | claims-verified |
| [action-selection](01-aad-core/src/action-selection.md) | Derived | deps-verified |
| [mismatch-signal](01-aad-core/src/mismatch-signal.md) | Definition | deps-verified |
| [mismatch-decomposition](01-aad-core/src/mismatch-decomposition.md) | Result | claims-verified |
| [update-gain](01-aad-core/src/update-gain.md) | Empirical | claims-verified |
| [causal-information-yield](01-aad-core/src/causal-information-yield.md) | Definition | deps-verified |
| [adaptive-tempo](01-aad-core/src/adaptive-tempo.md) | Definition | claims-verified |
| [mismatch-dynamics](01-aad-core/src/mismatch-dynamics.md) | Hypothesis | deps-verified |
| [deliberation-cost](01-aad-core/src/deliberation-cost.md) | Derived | claims-verified |
| [gain-sector-bridge](01-aad-core/src/gain-sector-bridge.md) | Derived | claims-verified |
| [sector-condition-stability](01-aad-core/src/sector-condition-stability.md) | Result | claims-verified |
| [persistence-condition](01-aad-core/src/persistence-condition.md) | Result | claims-verified |
| [structural-adaptation-necessity](01-aad-core/src/structural-adaptation-necessity.md) | Result | claims-verified |
| [temporal-nesting](01-aad-core/src/temporal-nesting.md) | Derived | deps-verified |
| [agent-identity](01-aad-core/src/agent-identity.md) | Discussion | deps-verified |

### Written — Section II (25 segments, all written)
| Slug | Type | Notes |
|------|------|-------|
| [agent-spectrum](01-aad-core/src/agent-spectrum.md) | Definition | Needs review |
| [complete-agent-state](01-aad-core/src/complete-agent-state.md) | Formulation | $X_t = (M_t, G_t)$ lift. Backward-compatible with Section I. |
| [objective-functional](01-aad-core/src/objective-functional.md) | Formulation | $O_t \to V_{O_t}$: trajectories $\to \mathbb{R}$. Scalar-comparability is a substantive commitment. |
| [value-object](01-aad-core/src/value-object.md) | Definition | $V_O$, $Q_O$ with convention hierarchy (C1/C2/C3) and monotonicity result. Extends policy objective with $\lambda(M_t, O_t, N_h)$. |
| [strategy-dimension](01-aad-core/src/strategy-dimension.md) | Definition | $G_t = (O_t, \Sigma_t)$. Evaluation vs guidance. Independence of richness dimensions. |
| [causal-hierarchy-requirement](01-aad-core/src/causal-hierarchy-requirement.md) | Derived + Scope | Level 2 for $Q_O$ evaluation. Scope: agents that learn during operation. |
| [loop-interventional-access](01-aad-core/src/loop-interventional-access.md) | Derived | Loop generates interventional data by construction. |
| [explicit-strategy-condition](01-aad-core/src/explicit-strategy-condition.md) | Normative | Cost inequality for explicit $\Sigma_t$. Makes temporal-optimality load-bearing. |
| [chain-confidence-decay](01-aad-core/src/chain-confidence-decay.md) | Derived | Log-confidence additive in depth. $p^n$ is special case. |
| [and-or-scope](01-aad-core/src/and-or-scope.md) | Scope | AND/OR restriction. Noisy-OR and WEIGHTED rejected. Parsimony argument. |
| [strategy-dag](01-aad-core/src/strategy-dag.md) | Definition | $\Sigma_t = (V, E, p, \gamma)$. Acyclicity derived. Edge semantics as causal credence. Correlation Hierarchy (L0/L1/L2) first-class. |
| [directed-separation](01-aad-core/src/directed-separation.md) | Derived + Scope | $f_M$ is $G_t$-independent. Scope condition for goal-conditioned agents. |
| [satisfaction-gap](01-aad-core/src/satisfaction-gap.md) | Definition | $\delta_{\text{sat}}$ with disambiguation table. $A_O$ (attainability) defined here. |
| [control-regret](01-aad-core/src/control-regret.md) | Definition | $\delta_{\text{regret}}$. 2×2 diagnostic with satisfaction gap. |
| [strategic-calibration](01-aad-core/src/strategic-calibration.md) | Definition | Edge residuals. Discussion-grade aggregation. |
| [orient-cascade](01-aad-core/src/orient-cascade.md) | Derived | Resolution order from information dependency. $G_t$ bounded by $M_t$. |
| [observability-dominance](01-aad-core/src/observability-dominance.md) | Derived | Low $\sigma$ → frozen edges → epistemically dead paths. |
| [edge-update-via-gain](01-aad-core/src/edge-update-via-gain.md) | Hypothesis | Gain principle extended to edge credences. Signal function open. |
| [edge-update-causal-validity](01-aad-core/src/edge-update-causal-validity.md) | Scope | Three-regime causal validity for edge updates. Identifiability coefficient $\iota_{ij}$. |
| [structural-change-as-parametric-limit](01-aad-core/src/structural-change-as-parametric-limit.md) | Formulation | Six operations from reweighting to full restructure. |
| [strategy-persistence-schema](01-aad-core/src/strategy-persistence-schema.md) | Proposed schema | Sector conditions for $\Sigma_t$. Schema, not result — needs instantiation. |
| [strategic-tempo](01-aad-core/src/strategic-tempo.md) | Definition | T_Σ = Σ ν_ij·η_edge,ij. Verified against four topologies. AND depth-gated, OR exploration-gated. |
| [strategy-complexity-cost](01-aad-core/src/strategy-complexity-cost.md) | Formulation | IB/MDL for strategy DAGs. Max useful depth d*. Triple depth penalty. Discussion-grade. |
| [exploit-explore-deliberate](01-aad-core/src/exploit-explore-deliberate.md) | Discussion | Extended deliberation threshold (derived). Two-stage decomposition NOT forced (unified objective outperforms in simulation). Dominance regimes qualitative. Deliberation = internal exploration (simulation, counterfactual reasoning, cross-domain synthesis). Discussion-grade. |

### Written — TST (20 segments; 4 missing, 0 old remain) — now in `02-tst-core/`
| Slug | Type | Notes |
|------|------|-------|
| [software-scope](02-tst-core/src/software-scope.md) | Scope | Needs review |
| [feature-definition](02-tst-core/src/feature-definition.md) | Definition | Needs review |
| [specification-bound](02-tst-core/src/specification-bound.md) | Result | Needs review; written by earlier agent with less context. Includes communication-as-bottleneck corollary. |
| [change-expectation-baseline](02-tst-core/src/change-expectation-baseline.md) | Derived | Median not expectation — key finding. Includes investment-scaling corollary. |
| [comprehension-time](02-tst-core/src/comprehension-time.md) | Definition | Needs review |
| [implementation-time](02-tst-core/src/implementation-time.md) | Definition | Needs review |
| [dual-optimization](02-tst-core/src/dual-optimization.md) | Derived | Turnover multiplier |
| [change-investment](02-tst-core/src/change-investment.md) | Derived | Pairwise threshold from dual-optimization. Compound effects are hypothesis, not derived. |
| [conceptual-alignment](02-tst-core/src/conceptual-alignment.md) | Hypothesis | Includes realignment-as-feature corollary. Functional form ungrounded. |
| [atomic-changeset](02-tst-core/src/atomic-changeset.md) | Definition | |
| [changeset-size-principle](02-tst-core/src/changeset-size-principle.md) | Empirical | Includes comprehension-follows-changeset corollary (hypothesis). |
| [change-distance](02-tst-core/src/change-distance.md) | Definition | |
| [change-proximity-principle](02-tst-core/src/change-proximity-principle.md) | Derived + Hypothesis | Qualitative derived; functional form hypothesis. |
| [exponential-cognitive-load](02-tst-core/src/exponential-cognitive-load.md) | Hypothesis | AAD deliberation-cost suggests dependency-structure model, not fixed exponent. |
| [system-coupling](02-tst-core/src/system-coupling.md) | Definition | Causal (interventional) interpretation via git. |
| [system-coherence](02-tst-core/src/system-coherence.md) | Definition | |
| [coherence-coupling-measurement](02-tst-core/src/coherence-coupling-measurement.md) | Measurement | Ratio form is one possible aggregation. |
| [principled-decision-integration](02-tst-core/src/principled-decision-integration.md) | Derived | General form of dual-optimization with per-feature $P(F_i)$. |
| [system-availability](02-tst-core/src/system-availability.md) | Definition | Standard reliability engineering. |
| [continuous-operation](02-tst-core/src/continuous-operation.md) | Scope | Extends temporal optimization to include operational failures. |

### Written — Section III (14 segments, all written)
| Slug                                                                | Type        | Notes                                                                                                                                |
| ------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| [multi-agent-scope](01-aad-core/src/multi-agent-scope.md)                       | Scope       | Coupling through shared environment.                                                                                                 |
| [composition-closure](01-aad-core/src/composition-closure.md)                   | Formulation | Operationalizes agent boundary as bounded closure defect. Admissibility (A1)-(A4) + projection admissibility (P1)-(P3) specified. Bridge lemma: (A4) + contraction assumption implies trajectory error bounded at $\varepsilon^\ast / \alpha_c$. Two-Kalman instantiation exact ($\varepsilon^\ast = 0$ uncorrelated). Mahalanobis norm specified for estimation-type agents. Status: conditional (discrete-time formalization pending, general-case P1 computability open). |
| [tempo-composition](01-aad-core/src/tempo-composition.md)                       | Sketch      | Sub-additive tempo inequality. Status: sketch (proof incomplete — $\varepsilon^\ast \to C_{\text{coord}}$ mapping open).             |
| [directed-separation-under-composition](01-aad-core/src/directed-separation-under-composition.md) | Hypothesis | Two cases: goal-blind routing preserves, goal-dependent routing breaks. Status: conditional — upgraded from discussion-grade after routing formalization in #multi-agent-scope and architectural classification promotion in #directed-separation. Remaining caveat: composition-closure admissibility placeholders. Earlier draft had a Case 3 (environmental coupling) that was correctly identified by review as not a directed-separation issue. |
| [unity-dimensions](01-aad-core/src/unity-dimensions.md)                         | Discussion  | 4 dimensions: epistemic, teleological, strategic, perceptual. Status: discussion-grade. Clausewitz mapping. $U_{\text{obs}}$ has no formula; $U_\Sigma$ circular. |
| [shared-intent](01-aad-core/src/shared-intent.md)                               | Definition  | IB-compressed purposeful state for inter-agent communication. Status: discussion-grade.                                              |
| [auftragstaktik-principle](01-aad-core/src/auftragstaktik-principle.md)         | Hypothesis  | $B_O \gt B_\Sigma \gt B_M$. Bungay evidence. Status: discussion-grade.                                                               |
| [adversarial-destabilization](01-aad-core/src/adversarial-destabilization.md)   | Derived     | Lyapunov destabilization + effects spiral. From TFT Appendix A, A.3/A.3.1.                                                           |
| [communication-gain](01-aad-core/src/communication-gain.md)                     | Hypothesis  | Trust-weighted inter-agent gain. From TFT Appendix F, F.2.                                                                           |
| [adversarial-exponent-regimes](01-aad-core/src/adversarial-exponent-regimes.md) | Result | Three regimes: $b=2$ (Model D/coupled), $b=1.5$ (Model S/coupled), $b \to 1$ (non-coupled). Both coupling-dominant exponents now **derived** (from Model D/S steady-state scaling). Status: conditional.                             |
| [observation-gates-advantage](01-aad-core/src/observation-gates-advantage.md)   | Observation | Obs noise collapses advantage; optimal gain partially restores. From track-b Variant E.                                              |
| [per-dimension-persistence](01-aad-core/src/per-dimension-persistence.md)       | Result      | Per-dim AR(1) exact to 4 sig figs. Scalar overestimates 72%. Model D/S thresholds now distinguished. Status: conditional. Regime-mixing issue **resolved**.                                                 |
| [team-persistence](01-aad-core/src/team-persistence.md)                         | Derived     | Distributed tempo, cooperative-adversarial $\rho$ decomposition, 3-lever persistence. From TFT F.3.                                  |
| [adversarial-tempo-advantage](01-aad-core/src/adversarial-tempo-advantage.md)   | Result      | Both coupling-dominant exponents derived: $b=2$ (Model D), $b=3/2$ (Model S). Status: conditional on disturbance model.                                  |

### Written — Appendices (9 segments)
| Slug | Type | Notes |
|------|------|-------|
| [sector-condition-derivation](01-aad-core/src/sector-condition-derivation.md) | Derivation | Full Lyapunov derivations (A.1, A.1S, A.2). A.1S adds stochastic (Model S) Itô-Lyapunov result. |
| [recursive-update-derivation](01-aad-core/src/recursive-update-derivation.md) | Derivation | Uniqueness derivation + 7 counterexample attacks. |
| [multi-timescale-stability](01-aad-core/src/multi-timescale-stability.md) | Sketch | N-timescale singular perturbation framework. |
| [operationalization](01-aad-core/src/operationalization.md) | Detail | Estimation procedures for AAD quantities. |
| [worked-example-kalman](01-aad-core/src/worked-example-kalman.md) | Worked example | End-to-end exact mapping. |
| [worked-example-bandit](01-aad-core/src/worked-example-bandit.md) | Worked example | End-to-end approximate mapping; persistence failure diagnostic. |
| [simulation-results](01-aad-core/src/simulation-results.md) | Detail | 6 variants validating/refining Section I predictions. Track-b reference. |
| [graph-structure-uniqueness](01-aad-core/src/graph-structure-uniqueness.md) | Derivation | 4 postulates + causal sufficiency → DAG with Markov property. Acyclicity exact. Markov property proved via CMC theorem (2026-04-06) — P3 is consequence, not premise. Edge independence = causal sufficiency. |
| [discrete-sector-condition](01-aad-core/src/discrete-sector-condition.md) | Derivation | Discrete-time Props DA.1, DA.1S, DA.2 via contraction mapping. Fluid limit theorem. **GA-5 closed** — Model D gap zero, Model S gap $O(\eta^\ast c_{\max})$. |

### Not Yet Written — 14 segments remaining

**TST (4 missing — now in `02-tst-core/`):**
- `#software-epistemic-properties` — software's 6 unique epistemic properties. Source: old-tst-via-tft-readme.
- `#developer-as-act-agent` — developer as $(M_t, O_t, \Sigma_t)$. Source: old-tst-via-tft-mapping.
- `#code-quality-as-observation-infrastructure` — code quality → $U_o$ → $\eta^\ast$ → $\mathcal{T}$. Source: old-tst-via-tft-mapping.
- `#causal-discovery-from-git` — git as interventional data source. Source: old-tst-via-tft-causal-extensions.

**Logogenic Agents (7 missing — now in `03-logogenic-agents/`; see coupled survival analysis):**
- `#ai-agent-as-act-agent` — AI agent as actuated agent (directed separation fails → coupled analysis).
- `#context-turnover` — 100% $M_t$ reset per session.
- `#coupled-update-dynamics` — Logogenic-specific coupled formulation $X_{\tau^+} = f_{\text{LLM}}(\text{prompt}(X_{\tau^-}, e_\tau))$. **NEW from spike.**
- `#section-ii-survival` — Which Section II results survive without directed separation (16/24 exactly, 5 approximately, 2 require modification). **NEW from spike.**
- `#coupled-diagnostic-framework` — Post-hoc diagnostic decomposition from coupled update. **NEW from spike.**
- `#m-preservation` — external memory as persistent $M_t$.
- `#observation-ambiguity-modulation` — $\kappa \times$ ambiguity scope condition. **NEW from spike.**

**Section III — Composition Dynamics (5 gaps):**
- Latent structural diversity — correction-architecture variation invisible to persistence analysis, consequential under regime change. Source: `msc/spike-neutral-drift-lyapunov.md`.
- Endogenous coupling — γ as function of population composition, not exogenous parameter. Source: `msc/spike-neutral-drift-lyapunov.md`.
- Composition transition dynamics — adopts Miller (2022) extreme transition motif: epochal stability → latent diversification → niche emergence → cascading restructuring → re-equilibration. Source: `msc/spike-miller-act-bridge.md`.
- Computational thresholds for social behavior — adopts Miller (2022) ICE framework: minimum agent complexity and interaction depth. Grounds #strategy-complexity-cost. Source: Miller (2022) Ch. 12, Table 12.2.
- Agent opacity — adopts Hafez et al. (2026) backward predictive uncertainty $H_b$: dual of observation quality; enters adversarial coupling and cooperative coordination. Source: `msc/spike-hafez-integration-audit.md`.

**Appendices (3 missing):**
- `#linear-ode-approximation` — pedagogical linear mismatch ODE (detail).
- `#intent-dag-development` — convergence on AND/OR + single-p (aside). Source: 04-intent-dag-consolidated.md.
- `#worked-example-cam` — coevolving automata (Miller 2022): AAD ↔ Moore machine mapping, meta-machine as ε*=0 composition, simplest adaptive agent. Source: `msc/spike-miller-act-bridge.md` §3, `msc/spike-fsa-dag-relationship.md`.

~~`#prior-art-positioning`~~ — **Superseded.** Prior art (Hafez, Miller, etc.) now integrated into Discussion sections of relevant segments rather than a separate appendix. Hafez: agent-spectrum (P ↔ T, agency/intelligence mapping), directed-separation (IDT as Class 2 monitoring), adversarial-destabilization (H_b as opacity metric), causal-hierarchy-requirement (bi-predictability as Level 2 evidence). Miller: structural-adaptation-necessity (neutral drift mechanism), agent-spectrum (Moore machine as minimal agent), adversarial-destabilization (transition motif), plus Section III dynamics gaps. Source material remains in `msc/02-prior-art-assessment.md`.


## Key Spikes

| Spike | Location | Status |
|-------|----------|--------|
| Purposeful agent derivation (v3) | `msc/spike-v3-purposeful-agent.md` | Section II porting **COMPLETE** — all 20 segments in src/ |
| Agent composition / holon | `msc/spike-agent-composition.md` | Core insight strong; composition laws are sketches |
| Composition closure | `msc/spike-composition-closure.md` | Formalized closure defect $\varepsilon^\ast$; promoted to #composition-closure + #tempo-composition |
| Graph structure uniqueness | `msc/spike-graph-uniqueness.md` | Acyclicity derived; P3→Markov needs tightening |
| Intent DAG consolidated | `msc/04-intent-dag-consolidated.md` | Canonical DAG reference; converged |
| Prior art assessment | `msc/02-prior-art-assessment.md` | Hafez/IBM/BDI/active-inference positioning |
| Discrete-time sector condition | `msc/spike-discrete-time-sector.md` | Closes GA-5 (Section I formal chain complete). **Promoted to segment.** |
| Strategy tempo + cognitive cost | `msc/spike-strategy-tempo-cost.md` | $\mathcal{T}_\Sigma$ defined; IB/MDL cost framework; max depth $d^\ast$ derived. **Promoted to segments.** |
| Coupled survival analysis | `msc/spike-coupled-survival-analysis.md` | Maps Section II for Class 2 agents: 16/24 survive exactly, 5 approximately, 2 need modification. 7-segment roadmap for `03-logogenic-agents/`. |
| Correlated Kalman composition | `msc/spike-composition-correlated-kalman.md` | Full derivation: $\varepsilon^\ast = 0$ for all $\rho$. $\Delta_{\text{perf}} \propto \rho^2$ is optimality, not representability. First $\varepsilon^\ast > 0$ from purposeful substates. |
| Edge semantics resolution | `msc/spike-edge-semantics-resolution.md` | Resolves observational/interventional tension: regime-indexed causal efficacy estimate. **Applied to segments.** |
| LLM causal access note | `msc/llm-causal-access-note.md` | Pearl reconciliation; potential intro/paper/blog |
| DAG boundary type closure | `msc/spike-dag-type-closure.md` | v2; reviewed by Codex; ready for porting |
| Single-edge strategic dynamics | `msc/spike-single-edge-strategic-dynamics.md` | **Sector condition verified** for Beta-Bernoulli. α_Σ = η_edge = 1/(n+1). **PROMOTED** to segments. |
| Two-edge strategic dynamics | `msc/spike-two-edge-strategic-dynamics.md` | Observable: weakest-link α_Σ with evidence starvation. Unobservable: per-edge fails (A1 violation), plan-level recovers. **PROMOTED** to segments. |
| Disturbance model split | `msc/spike-disturbance-model-split.md` | Model D vs Model S. Derives $b=3/2$ analytically. Resolves regime mixing. **PROMOTED** to 9 segments + NOTATION.md. |
| Projection admissibility | `msc/spike-projection-admissibility.md` | P_adm = (P1, P2, P3). Two-Kalman exact instantiation. Mahalanobis norms. **PROMOTED** to composition-closure + tempo-composition. |
| Scalar objective scope | `msc/spike-scalar-objective-scope.md` | Scalar is load-bearing for diagnostics, not structural results. Revealed-preference argument. AND-node workaround documented. **PROMOTED** to objective-functional + satisfaction-gap. |
| Track-b simulations | `msc/track-b-nonlinear-sims/` | 6 variants, all validated |
| Miller ↔ AAD bridge | `msc/spike-miller-act-bridge.md` | Maps Miller's *Ex Machina* (2022) to AAD. Five new Section III dynamics elements identified. FSA ↔ DAG relationship analyzed (orthogonal, not competing). Sector condition blind to neutral drift — new concept "latent structural diversity" needed. Paths C/D (automata foundations) ruled out; Path B (Section III dynamics) recommended. |
| FSA ↔ strategy-DAG | `msc/spike-fsa-dag-relationship.md` | Moore machine = behavioral surface; strategy DAG = epistemic interior. Orthogonal representations. DAG→FSA is lossy (discards causal semantics). FSA composition exact for behavior only; agent-level composition still approximate (ε* from internal state projection). |
| Neutral drift ↔ Lyapunov | `msc/spike-neutral-drift-lyapunov.md` | Phases 1,5 map cleanly; Phases 2-3 invisible to sector condition; Phase 4 partial (coupling emergence missing). Missing concept: latent structural diversity — correction-architecture variation invisible to persistence analysis. Endogenous γ needed. |


## What's Settled

*From convergence testing, spikes, and simulation:*

- Single-parameter edges with AND/OR nodes
- Orient cascade structure (derived from information dependency)
- Additive log-confidence decay (generalizes $p^n$)
- Observability as strategy enablement
- Directed separation (with explicit scope condition for goal-conditioned agents)
- $G_t = (O_t, \Sigma_t)$ split (definitional, not timescale-dependent)
- Satisfaction gap / control regret split (replaces simpler $\delta_{\text{objective}}$)
- DAG acyclicity derived from temporal ordering (former fragility resolved)
- Composition consistency required (not optional) by scope condition's level-independence
- Disturbance model split: Model D (deterministic, GA-2) vs Model S (stochastic, GA-2S) with distinct scaling
- Adversarial exponents derived: $b=2$ (Model D) and $b=3/2$ (Model S), both from steady-state scaling
- Strategy persistence schema verified for single-edge, two-edge observable, and plan-level cases (α_Σ = η_edge)
- Evidence starvation: downstream edge correction attenuated by ∏θⱼ (double depth penalty with chain-confidence decay)
- Projection admissibility (P1-P3) defined; independent of macro-dynamics admissibility (A1-A4)
- Scalar objective load-bearing for diagnostics; structural results survive vector extension
- Three senses of persistence disambiguated: structural, operational, continuity (see LEXICON in README.md)
- Agent continuity stance orthogonal to purposefulness (five stances defined)
- Fluid limit (GA-5) formally justified: discrete-time sector condition via contraction mapping recovers continuous results (Model D gap zero, Model S gap $O(\eta^\ast c_{\max})$)


## Theory Core

The theory has a small **inevitability core** — segments where mathematical necessity is the goal and is plausibly achievable — surrounded by **canonical formulations** (good representational choices, not forced) and **empirical/heuristic enrichment** (testable claims, design guidance). Keeping these layers explicit prevents two failure modes: trying to prove inherently empirical claims, and settling for "formulation" when a result is within reach.

### Inevitability core (~15 segments)

These are the segments where the goal is: "given the prior objects, this is the *only* compatible form." Mathematical inevitability is the ceiling.

| Segment | Why inevitability is plausible |
|---------|-------------------------------|
| #recursive-update + #recursive-update-derivation | Three constraints → unique recursive form. Strongest result in the theory. |
| #mismatch-decomposition | Bias-variance decomposition: mathematical identity once mismatch is defined. |
| #chain-confidence-decay | log(product) = sum(logs). Pure algebraic identity. |
| #persistence-condition | Given sector conditions, the threshold follows by Lyapunov. |
| #sector-condition-stability + #sector-condition-derivation | Lyapunov stability result applied to the mismatch dynamics. |
| #structural-adaptation-necessity | Parametric update converges within model class; wrong class → structural change necessary. |
| #orient-cascade | Resolution order forced by information dependency ($M_t$ before $\Sigma_t$ before $O_t$). |
| #satisfaction-gap / #control-regret | Two gaps are arithmetic once $V_{\text{ideal}}$, $A_O$, $V_{\text{current}}$ are defined. The diagnostic value is the insight. |
| #causal-hierarchy-requirement | Application of Bareinboim et al.'s causal hierarchy result to $Q_O$ evaluation. |
| #loop-interventional-access | Feedback loop generates interventional data by construction — structural property. |
| #directed-separation | $f_M$ independence from $G_t$ follows from the update structure, given scope condition. |
| #deliberation-cost | Think-vs-act threshold from information-theoretic argument. |
| #composition-consistency | If scope condition doesn't restrict level, predictions at different levels must be compatible. (Needs proof.) |

### Canonical formulations (second ring)

Good representational choices that are motivated but not forced. The three-question triage (FORMAT.md) answer to "what competing formulation would also fit?" is "at least one alternative exists." These are where AAD's *design* lives.

Includes: #complete-agent-state, #objective-functional, #value-object, #strategy-dimension, #strategy-dag, #and-or-scope, #agent-model, #information-bottleneck, #event-driven-dynamics, #adaptive-tempo, #structural-change-as-parametric-limit, #explicit-strategy-condition (normative, not derived), #composition-closure (operationalizes #composition-consistency but is a formulation choice, not the only possible operationalization), most definitions.

### Empirical, heuristic, and discussion (third ring)

Claims whose ceiling is empirical or heuristic — testable against the world but not derivable from the formalism. This is NOT a demotion: these are where AAD becomes falsifiable and useful. Section IV is mostly here.

Includes: #update-gain, #mismatch-dynamics, #edge-update-via-gain, #strategic-calibration, #communication-gain, #conceptual-alignment, #exponential-cognitive-load, #changeset-size-principle, most TST and logogenic agent segments, simulation observations.

### Usage

When developing or reviewing a segment, check which ring it belongs to. If it's in the inevitability core, the goal is tightening the proof. If it's a canonical formulation, the goal is explaining the choice and noting alternatives. If it's empirical/heuristic, the goal is stating falsifiable predictions and connecting to validation. Don't push segments upward beyond their ceiling; don't leave core segments at sketch status when a proof is within reach.

See FORMAT.md "Epistemic Triage" for the three-question diagnostic.


## What's Open

- ~~Action-deliberation-exploration tradeoff (three-way with $\Sigma_t$).~~ **Resolved 2026-04-02**: Two-stage formulation (act-vs-deliberate, then exploit-vs-explore). Extended deliberation objective adds $\Delta V_\Sigma$ (strategic benefit) to #deliberation-cost. Dominance regimes derived from constituent first-order conditions. Promoted to #exploit-explore-deliberate. Open: $\Delta V_\Sigma$ operationalization, interaction between epistemic and strategic improvement, discrete stopping-problem formulation.
- ~~Strategy tempo formalization ($\mathcal T_\Sigma$).~~ **Resolved 2026-04-02**: T_Σ = Σ ν_ij·η_edge,ij defined, verified against four topologies. AND-chains depth-gated, OR-nodes exploration-gated. Per-edge persistence formulation. Promoted to #strategic-tempo. Open: mixed AND/OR DAGs, optimal topology.
- ~~Cognitive cost of $\Sigma_t$ (no $\beta$ analog yet).~~ **Resolved 2026-04-02**: IB/MDL framework for strategy DAGs. DL(Σ_t) scaling O(|E| log |V|). Max useful depth d* derived. Triple depth penalty. Promoted to #strategy-complexity-cost. Open: computational tractability of strategy IB, dynamic complexity.
- Edge identifiability conditions (resolved in software, open in general). Edges claim interventional semantics ($p_{ij} = P(j \mid do(i), M_t)$) but update from observational signals. In confounded domains (military, organizational), this is a real causal-identification problem. In software, genuine interventions (tests, deploys, git bisect) are available. Resolution may come from the software domain pushing requirements back up.
- ~~P3→Markov step in graph uniqueness (sketch, needs tightening)~~ **Resolved 2026-04-01**: conditional on causal sufficiency
- Bridge lemma for composition closure: formally proving small expected component-wise errors guarantee bounded trajectory divergence under Lipschitz stability conditions.
- **Closure defect → coordination overhead mapping**: the core open problem in tempo-composition. The sub-additive inequality $\mathcal T_c \leq \sum \mathcal T_i$ is almost certainly correct, but the quantitative relationship $C_{\text{coord}}(\varepsilon^\ast)$ — how closure defect determines the tempo lost to internal reconciliation — is unproved. This is the missing bridge between the composition postulate (Section I) and a formally derived composition threshold. Proving this for the 2-agent case with orthogonal observation channels is the natural first step.
- Strategy persistence schema → result: sector condition **verified for single-edge Beta-Bernoulli case** (`msc/spike-single-edge-strategic-dynamics.md`). $\alpha_\Sigma = \eta_{\text{edge}} = 1/(n+1)$; persistence iff $n \lt R_\Sigma/\rho_\Sigma - 1$. Remaining: multi-edge extension (credit assignment, correlated edges), non-Bernoulli outcomes, stochastic Lyapunov formalization, connecting $\delta_\Sigma$ to $\delta_{\text{strategic}}$ from #strategic-calibration.
- Meta-adaptation of $\Pi$ and $N_h$: can the agent structurally adapt its own policy class and planning horizon? Analogous to model-class change (TF-10). Satisfaction gap's disambiguation table handles descriptively; formal mechanism open.
- DAG boundary type closure — **PORTED to #strategy-dag.** Leaf base credence ($p_v$) with temporal indexing, unique root terminal, well-formedness constraint, $\hat P_\Sigma$ as strategy self-assessment distinct from $A_O$, terminal alignment error as experience-only signal. Spike at `msc/spike-dag-type-closure.md` (v2). Terminal alignment error ($\delta_\text{align}$) formalization still open.
- Adversarial DAG targeting (Section III). Which strategy edges are most valuable to attack? Centrality in the DAG, inter-agent coupling edges, edges observable to the adversary. #chain-confidence-decay as a weapon: disrupting one AND-edge in a deep chain collapses the whole path.
- Composite directed separation (Section III). If each sub-agent's $f_M$ is $G_t$-independent, is the composite's $f_M^c$ independent of $G_t^c$? Hypothesis: goal-blindness composes, BUT coordination routing may break it — if which observations reach the composite depends on the shared objective, the composite's effective observation function is goal-dependent.
- Software tempo decomposition (TST / `02-tst-core/`). Three components: $\mathcal T_{\text{obs}}$ (compiler, linter, tests), $\mathcal T_{\text{explore}}$ (code reading, navigation), $\mathcal T_{\text{probe}}$ (test runs, staging). Which is the bottleneck? Each connects to #code-quality-as-observation-infrastructure. Source: old-tst-via-tft-mapping has the richest treatment.
- Logogenic agent gaps (all blocked on scope decision — `03-logogenic-agents/`):
  - **Cognitive loop formalization.** How does the logogenic agent's cycle differ from the generic orient cascade ( #orient-cascade)? What's specific to language-based agents? Source: [`msc/agentic-tft-cognitive-loop-spec.md`](msc/agentic-tft-cognitive-loop-spec.md). Also: [`msc/agentic-tft-narrative-as-implementation.md`](msc/agentic-tft-narrative-as-implementation.md) (why AAD quantities are estimated in language).
  - **Evaluation framework.** Measuring $M_t$ quality, $\Sigma_t$ quality, and tempo in AI agents. Connects to creche design. Source: [`msc/agentic-tft-evaluation-framework.md`](msc/agentic-tft-evaluation-framework.md).
  - **Creche concept.** AAD-grounded experiential training environments where agents develop adaptive capacity. Source: [`msc/agentic-tft-creche-concept.md`](msc/agentic-tft-creche-concept.md). Also: [`msc/agentic-tft-experiential-training.md`](msc/agentic-tft-experiential-training.md) (detailed three-level training design).
  - **Recursive completion.** An agent using AAD to guide its own behavior while operating on a codebase that implements AAD. Self-referential but not paradoxical — the recursion is well-founded because the agent's $M_t$ includes the theory as domain knowledge, not as self-reference.
  - **Known issues in source material.** The cognitive loop spec, evaluation framework, and ontology unification have cataloged issues: [`msc/agentic-tft-review-response.md`](msc/agentic-tft-review-response.md). Key flags: bootstrap problem (grounding epistemic estimates measurably), sovereignty in a designed system, "estimated in language" not yet operationalized.


## Cross-Segment Consistency Issues

- **Low-end examples (thermostat, PID) — RESOLVED.**
  Settled doctrine: the spectrum is about *richness*, not *presence/absence*. #agent-spectrum table relabeled from "absent" to "absent or trivial" with continuum framing. Thermostat has degenerate $M_t$ and $O_t$ (near origin, not truly reactive). PID has degenerate $M_t$ (not "no genuine $M_t$"). Reflex arc is the truly reactive case. #agent-model updated to match. Classification question is "rich enough for the machinery?" not "present or absent?"
- **"Section I carries over" compatibility boundary.** After the $X_t = (M_t, G_t)$ lift, epistemic machinery transfers cleanly to the $M_t$ substate. But #action-selection's derivation of $a_t = \pi(M_t)$ relied on $M_t$ being *complete* — this is superseded by $a_t = \pi(M_t, G_t)$. Noted in #complete-agent-state Discussion.


## Directed Separation: What Holds for Class 2 (Fully Merged) Agents

**2026-04-01 analysis.** The architectural classification (Class 1 modular / Class 2 merged / Class 3 partial) is settled. The question is: which Section II results survive when directed separation fails?

### Results that survive for Class 2

- **Satisfaction gap and control regret** — defined in terms of $V_O$, $A_O$, $\pi_{\text{current}}$. None reference $f_M$ or $f_G$. The 2×2 diagnostic works for LLMs.
- **Orient cascade ordering** — information dependency (need to know what's true before evaluating strategy) exists even in coupled systems. Becomes a simultaneous fixed-point problem rather than sequential resolution, but the logical structure is unchanged.
- **Strategy DAG structure** — goals decompose into subgoals causally regardless of whether perception is goal-conditioned.
- **Observability dominance** — gain principle drives update rate to zero for unobservable edges regardless of architecture.
- **Acyclicity** — temporal ordering still prevents cycles.
- **Section I quantities** — $\delta$, $\eta^\ast$, $\mathcal{T}$, the persistence condition remain well-defined on $M_t$.

### Results that genuinely fail for Class 2

- **Sequential M-then-G update** — for an LLM, epistemic and strategic processing happen in the same forward pass. No well-defined moment where $M_t$ is updated but $G_t$ is not.
- **$G_t$ complexity bound** — depends on $M_t$ being independently established. In a coupled system, the agent can "see what it wants to see," breaking the bound.
- **Clean persistence analysis on $M_t$ alone** — mismatch dynamics become coupled: perception quality depends on goals.

### Results where it's genuinely unclear

- **Persistence condition form.** Does $\alpha > \rho/R$ still hold? The Lyapunov machinery is general enough that it should — but $\alpha$ would depend on $G_t$ (goal-conditioned perception changes correction quality), making the persistence condition state-dependent rather than structural. This is a meaningful qualitative change. See Persistence (structural vs. operational) in `LEXICON.md`.
- **Adversarial dynamics.** If the target's perception is goal-conditioned, an adversary who knows the target's goals can exploit motivated reasoning — feeding observations that will be misinterpreted. New attack surface absent for Class 1. Exponents might change.
- **Composition.** Does directed separation under composition (#directed-separation-under-composition) make sense when components are Class 2?

### Engineering implications

The #directed-separation segment's Working Notes point toward the right response: even though an LLM is internally Class 2, the *agent system* (LLM + tools + memory + monitoring) can be designed with modular topology — creating partial separation at the system level. This is an architectural prescription that emerges from the classification: build Class 1 structure *around* Class 2 components.

### What's needed

A formal treatment of what happens to the dynamics when separation fails. Not just "it's harder" but: what new phenomena emerge (motivated reasoning, confirmation bias as coupling terms in $f_M$), what the persistence condition becomes for coupled systems (state-dependent $\alpha$?), and which Section II results survive as approximate or limiting cases. This is the scope of `03-logogenic-agents/`. **2026-04-02 update:** The coupled survival analysis (`msc/spike-coupled-survival-analysis.md`) now provides the detailed classification: 16 of 24 results survive exactly, 5 approximately, 2 require modification. A 7-segment minimal viable roadmap is specified.


## Known Fragilities

- ~~Edge semantics claim interventional but update from observational.~~ **RESOLVED 2026-04-02.** Resolved as regime-indexed interpretation: $p_{ij}$ is a causal efficacy estimate whose identification strength varies with the data regime (A/B/C). Single-parameter edge preserved; $\iota_{ij}$ characterizes causal warrant separately. See `msc/spike-edge-semantics-resolution.md`.
- Missing commitment/resource/temporal structure in the DAG
- Directed separation violated by goal-conditioned agents (LLMs) — now framed correctly: $M_t$-side quantities remain well-defined regardless; directed separation gives the clean factorized update and sequential orient cascade. Without it, coupled analysis, not broken theory. Updated in #directed-separation, #agent-spectrum, 01-aad-core/OUTLINE.md §II scope. Scalar objective scope restriction added to #objective-functional. See "Directed Separation: What Holds for Class 2" above for detailed analysis.
- **TST → AAD bridge is analogical, not formal.** Git-derived metrics (coherence, coupling, $Q$) are claimed to operationalize Lyapunov quantities ($\alpha$, $R$, $\rho$) but no mathematical proof connects them. The chain git data → $Q$ → comprehension time → developer tempo → $\alpha$ has empirical hypothesis steps. This matters because the operationalization story is AAD's main defense against the "unmeasurable quantities" critique. Either formalize the bridge or be explicit that it's an empirical research program, not a derivation.


## Codex Review Issues (from memory — fixes needed)

1. **State completeness**: Must lift to $X_t = (M_t, G_t)$. $M_t$ becomes epistemic substate, not complete state. Foundational.
2. **Level 2 too strong**: Pre-compiled controllers are purposeful at Level 1. Scope to agents that must *learn* action consequences during operation.
3. **Objective/strategy are independent dimensions**: Don't conflate in a single hierarchy. $O_t$ richness and $\Sigma_t$ richness vary independently. Split early.
4. **$O_t$ parametrizes TF-08's "value" term**: Cleaner insertion point.
5. **Objective as trajectory functional**: $J$: trajectories $\to \mathbb{R}$ is genuinely more general than point targets.
6. **Cost inequality for $\Sigma_t$**: Derive need for explicit planning from $\text{cost}(\text{plan}) \lt \text{cost}(\text{explore})$, making #temporal-optimality load-bearing.
7. **$p^n$ is the special case**: Robust result is additive log-confidence growth.
8. **Strategy persistence is a result schema**: Need strategic error state, correction operator, disturbance class.
9. **Directed separation is conditional**: $f_M$ is $G_t$-independent, but closed-loop $M$ transition depends on $G_t$ through action. Precise claim is about update function, not trajectory.
10. **$\delta_{\text{objective}}$ must split into TWO quantities**: satisfaction gap + control regret. Without this split, the $O_t$ revision cascade doesn't work.

Items 1–10 are addressed in v3 spike. Porting to src/ segments is the remaining work.


## Ordering Questions

*The current linearization in 01-aad-core/OUTLINE.md may need revision:*

- Should #temporal-optimality move from Section I to Section II? It's about specific objectives — arguably an actuated-agent concept, not a general adaptive-systems concept. Counter-argument: it applies to Section I agents too (a Kalman filter that converges faster is better).

- Should #composition-consistency move earlier or later? Currently at the end of Section I foundations, before the dynamics claims. Could go right after #scope-condition (it's a direct consequence of scope's level-independence). The composition spike argues for early placement.

- Section II ordering: the v3 spike proposes a specific 16-segment linearization (§11). Is that still the best ordering after the codex review corrections?

- ~~**Section III: #communication-gain appears after #team-persistence, but team-persistence depends on it.**~~ **FIXED.** communication-gain now appears before team-persistence in OUTLINE.md.

- **Section II: #complete-agent-state forward-references #directed-separation.** The factorization $M_{\tau^+} = f_M(\ldots)$, $G_{\tau^+} = f_G(\ldots)$ is labeled "Derived (from recursive-update + directed-separation)" but directed-separation doesn't appear until 10 segments later. Not wrong (forward references are allowed) but worth a note in the segment that the justification comes later.

- **Section III: cooperative → adversarial transition is abrupt.** Segments 1–7 build a cooperative composition story; segment 8 (adversarial-tempo-advantage) introduces adversarial coupling with no narrative bridge. A transition sentence in the section scope text or a brief framing segment could smooth this.


## Promotion Priorities (updated 2026-03-12)

The bottleneck is no longer idea generation — it is promotion, canonicalization, and scope-tightening:

1. ~~**Section II backbone** — DONE.~~ All 20 segments promoted to src/ and marked draft in 01-aad-core/OUTLINE.md.

2. ~~**Simulation results → AAD-native claims/appendices** — DONE.~~ adversarial-exponent-regimes, observation-gates-advantage, and per-dimension-persistence promoted to src/ as first-class segments.

3. ~~**Section III completion (2 segments)** — DONE.~~ `#team-persistence` and `#adversarial-tempo-advantage` promoted. Section III is now 13/13.

4. ~~**Appendices — graph-structure-uniqueness and simulation-results** — DONE.~~ Both promoted. Appendices now 8/11 (3 remaining).

5. **Logogenic agents scope decision (`03-logogenic-agents/`)** — directed separation fails for goal-conditioned LLMs (acknowledged). This is where the project wants to land. Need to decide: is it an approximate application of current AAD, or does it require a genuine coupled $M_t$/$G_t$ extension? Currently honest but strategically unresolved.

6. **TST remaining 4 segments (`02-tst-core/`)** — strengthens operationalization story. `#software-epistemic-properties`, `#developer-as-act-agent`, `#code-quality-as-observation-infrastructure`, `#causal-discovery-from-git`. Source material in old-tst-via-tft-* files.

7. **Remaining appendices (3)** — `#linear-ode-approximation`, `#intent-dag-development`, `#prior-art-positioning`. Lower urgency.

8. **Vocabulary normalization pass** — LEXICON.md (created 2026-03-12) establishes new vocabulary: cycle phases, adaptive/agentic distinction, agent class hierarchy, logogenic/logozoetic. The following need updating to reflect the new terminology:
   - **01-aad-core/OUTLINE.md**: section titles still use old names (Adaptive Systems Under Uncertainty, Actuated Adaptive Systems, etc.)
   - **WORKBENCH.md**: segment tables still use old section names
   - **CLAUDE.md**: still references old section names
   - **Segment files**: "loop" used where "cycle" may now be more precise; cycle phase vocabulary (Prolepsis, Aisthesis, etc.) not yet planted in early segments (scope-condition, adaptive-tempo, agent-environment)
   - **notation.md**: cycle phase names not yet listed as formal vocabulary
   Lower urgency — LEXICON.md is canonical; these are consistency updates, not content changes. Best done during the segment review pass.

### Completed non-promotion work (2026-03-12)
- **Systematic overclaiming sweep.** 12 fixes across 10 segment files: "formalizes X" / "formal content of" / "This IS" / "proves" language shifted to "formal analog" / "consistent with" / "captures the pattern" with empirical caveats. README, CLAUDE.md, 01-aad-core/OUTLINE.md also updated: "first-principles mathematical theory" → "mathematical framework." Operationalization section added to README.
- **README positioning overhaul.** "What AAD Contributes — Honest Calibration" with 5-category breakdown. Prior Art section expanded with explicit credit to borrowed mathematics. Operationalization section addresses the bridge gap across all sections.


## Simulation Findings (Summary)

The track-b simulations (`msc/track-b-nonlinear-sims/`) are theory-shaping, not merely confirmatory. They forced regime splits and narrowed claims that the analytical derivations left ambiguous. Full details in variant result files.

### Adversarial tempo exponent (Variants A–D)
- **Deterministic drift, coupling-dominant**: exponent = 2.0 (confirmed at 1.999). Cor. 11.2 exact.
- **Stochastic AR(1) noise, coupling-dominant**: exponent = **1.5, not 2.0**. Root cause: ODE steady-state scales as $\rho/\mathcal{T}$, but stochastic RMS scales as $\rho/\sqrt{\mathcal{T}}$. This is a fundamental model distinction, not a minor correction.
- **Non-coupling-dominant**: exponent degrades smoothly toward 1.0 as base disturbance increases relative to adversarial coupling. The coupling-dominant qualifier is quantitatively load-bearing.
- **Implication**: Cor. 11.2's squared law is correct but conditional on deterministic coupling dominance. Applications must distinguish whether an opponent's tempo increases systematic drift vs. unpredictability.

### Observation noise (Variant E)
- Observation noise collapses adversarial exponent from ~1.0 to **~0.2** — tempo advantage nearly vanishes.
- Optimal gain (TF-06's $\eta^\ast$) partially restores it (~0.4) but cannot fully recover.
- Consistent with Boyd's emphasis on Orient quality: faster OODA is worthless with bad observations.

### Anisotropic correction (Variant F)
- Per-dimension persistence theory is **exact** (matches AR(1) prediction to 4 significant figures).
- Scalar tempo **overestimates by ~72%** — the weak dimension is the bottleneck.
- Isotropic allocation beats anisotropic by 13%; targeted adversarial attack on weak dimensions amplifies advantage 17%.
- **Implication**: need per-dimension persistence condition, not scalar $\mathcal{T} \gt \rho / \lVert\delta_{\text{critical}}\rVert$.

### Gain validation (Variant E)
- TF-06's uncertainty ratio principle empirically validated: 52% mismatch reduction with Riccati-optimal gain.

### Hafez bridge (Variant Hafez)
- Bi-predictability $P$ measures coupling *architecture*; AAD mismatch measures *performance*. $P$ cannot detect adversarial dynamics.
- Agency has structural information cost: passive $P = 0.44$, active $P = 0.27$.
- $H_b$ (backward uncertainty / agent opacity) has no direct AAD analog — potential gap for multi-agent work.


## Prior Work Migration Map

All TFT and TST content has been copied into `old-*` files within their respective `src/` directories (`01-aad-core/src/` and `02-tst-core/src/`). The priors/ submodules are now purely historical. The `old-` prefix means the content is prior work that hasn't yet been fully converted — it may not conform to AAD formatting standards.

### TFT → AAD Mapping

| Old file | Content | AAD status |
|----------|---------|------------|
| ~~old-tf-readme~~ | ~~TFT overview~~ | **Archived.** Superseded by CLAUDE.md, FORMAT.md. |
| old-tf-00-notation-conventions | Symbol tables, conventions, adaptive loop phases, global assumptions, units, claim registry | **Partially absorbed.** Notation referenced by FORMAT.md. Adaptive loop phases, global assumptions table, claim registry format — AAD should have its own. |
| ~~old-tf-01-scope~~ | ~~Scope definitions~~ | **Archived.** → #agent-environment, #observation-function, #action-transition, #scope-condition. Coupling spectrum now in #causal-structure. |
| ~~old-tf-02-causal-structure~~ | ~~Temporal arrow, chronica, Pearl's 3 levels, recursive update~~ | **Archived.** → #causal-structure, #pearl-causal-hierarchy, #chronica, #recursive-update. |
| ~~old-tf-03-model~~ | ~~Model, IB, sufficiency~~ | **Archived.** → #agent-model, #information-bottleneck, #model-sufficiency. |
| ~~old-tf-04-event-driven-dynamics~~ | ~~Event types, channels, rates~~ | **Archived.** → #event-driven-dynamics. |
| ~~old-tf-05-mismatch-signal~~ | ~~Prediction error, Prop 5.1~~ | **Archived.** → #mismatch-signal, #mismatch-decomposition. |
| old-tf-06-update-gain | Uncertainty ratio, domain validation, gain dynamics, overfitting as miscalibration | **Mostly absorbed** into #update-gain. Domain validation tables and gain dynamics (convergence, reset) richer than AAD segment — enrich then archive. |
| ~~old-tf-07-action-selection~~ | ~~Action as model function, fluency~~ | **Archived.** → #action-selection. |
| ~~old-tf-08-exploration-exploitation~~ | ~~CIY, unified policy objective, query actions~~ | **Archived.** → #causal-information-yield. |
| ~~old-tf-09-deliberation-cost~~ | ~~Prop 9.1, deliberation threshold~~ | **Archived.** → #deliberation-cost. |
| ~~old-tf-10-structural-adaptation~~ | ~~Prop 10.1, destruction-creation, overfitting~~ | **Archived.** → #structural-adaptation-necessity + #model-sufficiency + #model-class-fitness. |
| old-tf-11-tempo-persistence | Temporal nesting table, mismatch ODE, adversarial dynamics, observation quality, per-dimension | **Mostly absorbed** across #adaptive-tempo, #persistence-condition, #sector-condition-stability, etc. Mismatch ODE as named hypothesis, speed-quality substitutability — enrich then archive. |
| ~~old-tf-appendix-a-lyapunov~~ | ~~Props A.1–A.3, Cor A.3.1, full proofs, Prop A.4 sketch~~ | **Absorbed.** → #sector-condition-derivation (A.1–A.2), #adversarial-destabilization (A.3, A.3.1), #multi-timescale-stability (A.4). Ready to archive. |
| ~~old-tf-appendix-b-operationalization~~ | ~~Estimation procedures for all TFT quantities~~ | **Absorbed.** → #operationalization. Ready to archive. |
| ~~old-tf-appendix-c-kalman-example~~ | ~~Complete Kalman worked example~~ | **Absorbed.** → #worked-example-kalman. Ready to archive. |
| ~~old-tf-appendix-d-rl-example~~ | ~~Nonstationary bandit worked example~~ | **Absorbed.** → #worked-example-bandit. Ready to archive. |
| ~~old-tf-appendix-e-tft-core~~ | ~~Condensed formal chain~~ | **Archived.** Superseded by 01-aad-core/OUTLINE.md. |
| old-tf-appendix-f-multi-agent | Communication gain, trust, distributed tempo, topology, game theory | **Partially absorbed.** → #communication-gain (F.2 core), #adversarial-destabilization (uses coupling model). **Still needed from F:** distributed tempo → #team-persistence (F.3), topology analysis (F.4), game-theoretic integration (F.5), trust transitivity details, falsification predictions (F.7). Extract as Section III segments get built. |
| ~~old-tf-appendix-g-agent-identity~~ | ~~Non-forkability, clone problem~~ | **Archived.** → #agent-identity. |
| ~~old-tf-recursive-update-derivation~~ | ~~Full uniqueness proof~~ | **Absorbed.** → #recursive-update-derivation. Ready to archive. |
| old-tf-goal-intent-gap | What TFT lacked (goals/intent) | **Historical.** The gap AAD exists to fill. Can archive when comfortable. |
| old-tf-citations-catalog | TFT reference catalog | **Reference material.** Useful for paper writing. |
| old-tf-novelty-analysis | What's novel in TFT | **Reference material.** Useful for positioning. |
| old-tf-ooda-universal-pattern | OODA as universal adaptive pattern (v7) | **Historical.** Early framing. Can archive when comfortable. |

### TST → AAD Mapping

| Old file | Content | AAD status |
|----------|---------|------------|
| ~~old-tst-readme~~ | ~~TST overview~~ | **Archived.** Superseded by 02-tst-core/OUTLINE.md. |
| ~~old-tst-01-temporal-optimality~~ | ~~T-01~~ | **Archived.** → #temporal-optimality (generalized). |
| ~~old-tst-02-specification-bound~~ | ~~D-01 + T-02 + C-02.1~~ | **Archived.** → #specification-bound, #feature-definition. |
| ~~old-tst-03-evolving-scope~~ | ~~T-03~~ | **Archived.** → #software-scope. |
| ~~old-tst-04-change-expectation~~ | ~~T-04, C-04.1, C-04.2~~ | **Archived.** → #change-expectation-baseline. |
| ~~old-tst-05-dual-optimization~~ | ~~D-02, D-03, T-05~~ | **Archived.** → #comprehension-time, #implementation-time, #dual-optimization. |
| ~~old-tst-06-change-investment~~ | ~~T-06~~ | **Archived.** → #change-investment. |
| ~~old-tst-07-conceptual-alignment~~ | ~~T-07 + C-07.1~~ | **Archived.** → #conceptual-alignment. |
| ~~old-tst-08-changeset-size~~ | ~~D-04, T-08, C-08.1~~ | **Archived.** → #atomic-changeset, #changeset-size-principle. |
| ~~old-tst-09-change-proximity~~ | ~~D-05, T-09, H-09.1~~ | **Archived.** → #change-distance, #change-proximity-principle, #exponential-cognitive-load. |
| ~~old-tst-10-coherence-coupling~~ | ~~D-06, D-07, T-10~~ | **Archived.** → #system-coupling, #system-coherence, #coherence-coupling-measurement. |
| ~~old-tst-11-decision-integration~~ | ~~T-11~~ | **Archived.** → #principled-decision-integration. |
| ~~old-tst-12-continuous-operation~~ | ~~D-08, T-12~~ | **Archived.** → #system-availability, #continuous-operation. |

### TST via-TFT Bridge Material → AAD Mapping

| Old file | Content | AAD status |
|----------|---------|------------|
| old-tst-via-tft-readme | Why the bridge exists, software's 6 unique epistemic properties, key open questions | **Partially absorbed.** The 6 properties → #software-epistemic-properties (outlined). Open questions (observation channel under agent control, 100% turnover, counterfactual replay) feed TST (`02-tst-core/`) and logogenic agents (`03-logogenic-agents/`). |
| old-tst-via-tft-mapping | Detailed TFT→software mapping: environment decomposition, observation channels, action taxonomy, model, mismatch, gain, tempo, persistence, structural adaptation, multi-agent | **Richest single document for TST (`02-tst-core/`).** Action taxonomy (exploration/probe/query/modify/infrastructure-investment), three-part tempo decomposition, code-quality feedback loop, death spiral formalization — much not yet in AAD segments. |
| old-tst-via-tft-causal-extensions | Explicit causal DAGs in software, interventional reasoning via tests, counterfactual evaluation via git, causal discovery from git, runtime causal models | **Partially absorbed** into #causal-discovery-from-git and #software-epistemic-properties. Detailed treatment of dependency DAG vs empirical DAG, Level 2 channel spectrum, counterfactual machine — largely not in AAD. |
| old-tst-via-tft-reformulated-sketch | S-00 through S-14: complete outline of TST rebuilt on TFT/AAD foundations | **Valuable roadmap** for TST work (`02-tst-core/`). Shows how each TST claim maps to the AAD framework. The "what's new" and "what's removed" sections are useful for understanding the transformation. |
| old-tst-via-tft-simulation-proposals | 6 simulation proposals ordered by value/effort | **Partially executed.** Sims 1-2 done (track-b). Sims 3-6 remain as future work. |


## Prior Art Positioning & Paper Strategy

*Detailed cross-mapping in `msc/02-prior-art-assessment.md`.*

**The landscape:** IBM (Miehling et al. 2025) calls for a systems theory of agentic AI — explicitly identifying the void. Hafez et al. (2026) provide a diagnostic metric (bi-predictability $P$) without dynamics or goals. No existing work fills the void. AAD is the most complete response identifiable.

- **Hafez** (bi-predictability $P$): complementary diagnostic, no goals/dynamics. $H_b$ has no AAD analog yet — matters for legibility/coordination.
- **IBM 2025** (systems theory manifesto): calls for what AAD provides. Their open challenges (subgoal emergence, residual control rights) directly addressed by AAD.
- **BDI**: named the parts, no dynamics.
- **Active inference**: closest competitor, different foundation. Expected free energy ≈ AAD's value + $\lambda \cdot \text{CIY}$ (structural isomorphism, different foundations). AAD grounds exploration in causal information specifically.

**Lead with:** Section I (proved, simulated) + Section II (purposeful-agent derivation). These are where AAD has real substance. Sections III–V are "the theory extends to" demonstrations.

**AAD's contributions — honest calibration:**

1. **The integration itself.** Control theory + causal inference + information theory + agent architecture under one framework. The individual pieces are mostly known; the synthesis is the contribution. This is worth doing (Maxwell unified electricity and magnetism using known equations) but should not be presented as discovery of the component parts.
2. **Novel formalizations of known patterns.** The satisfaction gap / control regret split applies an established pattern (approximation error vs. estimation error, model-class limitation vs. within-class suboptimality) to agent self-diagnosis with cascading corrective actions — the 2×2 diagnostic table and orient cascade ordering are genuinely new applications. The feedback loop as Level 2 engine is a useful bridge between Pearl and Sutton, with a real additional claim for non-RL agents (LLMs get interventional data from the loop despite no internal causal architecture).
3. **Known results applied to new domains.** DAG acyclicity from temporal ordering is standard in Dynamic Bayesian Networks (unrolling). Timescale separation for composition is standard singular perturbation theory. Both are useful applications to agent/strategy domains, not discoveries. Do not list these as "novel results."
4. **Genuinely open bridges.** The git → Lyapunov operationalization is analogical, not formal. There is no mathematical proof that git-derived metrics (coherence, coupling, $Q$) translate to Lyapunov bounds ($\alpha$, $R$). The chain git data → $Q$ → comprehension time → developer tempo → $\alpha$ has empirical hypothesis steps in the middle. This is a real gap, not just a presentation issue. TST's operationalization story (`02-tst-core/`) is promising but not yet a bridge.
5. **Software as both testbed and recursive instantiation.** This framing is genuinely distinctive — no other theory treats software development as both the primary operationalization domain and the domain where the theory's own agents will operate.

**Discipline:** Don't overclaim. Present as a unifying framework with specific novel results. Be honest about what's integration vs. what's discovery.

**Anticipated critique: "physics envy" / "just renaming."** A serious external review (Gemini, 2026-03-11) raised this directly: Section I's gain is the Kalman gain, the Lyapunov proof is standard, the deliberation threshold is opportunity cost. The review caught the pedagogical scaffold (linear ODE) and missed the load-bearing structure (sector-condition framework), read the Kalman exact case and missed the multi-domain structural claim, and didn't examine Section II's novel results at all. But the meta-critique is fair: Section I is largely careful synthesis of known mathematics (Kalman, Lyapunov, IB). The contribution is identifying these as aspects of a single structure and then building purposeful agency on top. Presentation implications:

1. **Lead with "unifying framework," not "new mathematics."** The individual pieces are mostly known; the synthesis and what it enables (Sections II–V) is the contribution. Don't let the presentation suggest the gain formula or the Lyapunov proof are discoveries — they are instantiations.
2. **Make the sector-condition framework more prominent than the linear ODE.** Casual readers who stop at mismatch-dynamics see the pedagogical scaffold and conclude the theory rests on a fluid-limit approximation. The actual foundation is the nonlinear Lyapunov analysis, which is robust. Title, ordering, and emphasis should guide readers to sector-condition-stability before mismatch-dynamics, or at minimum make the relationship unmissable.
3. **TST as the operationalization answer.** The charge that $\alpha$ and $R$ are unmeasurable outside hardware is answered by TST (`02-tst-core/`), where comprehension time, implementation time, and change rates are measurable from git history. This should be prominent in any paper — "here is the domain where we can actually measure these quantities" directly addresses the strongest version of the critique.
4. **Name the genuinely novel results explicitly.** Readers scanning for "what's new" need to find it fast: satisfaction gap / control regret split, DAG acyclicity derived from temporal ordering, feedback loop as Level 2 engine, composition consistency as structural requirement, the dual persistence pattern (individual + composite thresholds). These are not repackaging.


## Governing Objectives

1. **Subsume TFT as the adaptive-systems foundation.** The sector-condition/Lyapunov framework is primary; the linear ODE is pedagogical. TFT is absorbed, not extended.
2. **Derive purposeful agency from first principles.** Start with the simplest abstract purposeful object and derive the need for richer structure from mathematical necessity — specifically from the causal hierarchy result (Bareinboim et al.).
3. **Make TST a rigorous software-domain instantiation of AAD.** Every claim gets epistemic tagging; ungrounded assertions are derived, retagged, or removed.
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
5. Can Hafez's $P$ be derived from AAD quantities? Can $\Delta H$ (strategic legibility) enter multi-agent dynamics? ($H_b$ has no AAD analog yet.)
6. Relationship between AAD and active inference's prior preferences?
7. Which physical domains have deterministic vs stochastic $\rho$?
8. Cognitive cost of maintaining $\Sigma_t$ (the $\beta$ analog for strategy).
9. P3→Markov step in graph uniqueness: does state-local revisability strictly force the Markov condition? See `msc/spike-graph-uniqueness.md`.
10. Whether "code quality as observation infrastructure" is unique to software or an instance of a general pattern (agents modifying their own observation channels).
11. LLM causal access (`msc/llm-causal-access-note.md`): the loop argument (Response 1) is load-bearing. Responses 2–3 (internal representations, training-time causal exposure) are interesting but give critics easier targets if blended into the canonical theory. Keep the loop argument primary; others as discussion/aside.

12. **[Brainstorm] Internal aporia as sub-agent adversarial dynamics.** Is aporia within a composite agent structurally equivalent to adversarial dynamics between its sub-agents? When a composite agent experiences mismatch, its sub-agents may disagree about what went wrong and what to do — that disagreement IS adversarial dynamics at the sub-agent level, and its resolution IS the composite's epistrophe. This would explain why high-stakes human institutions (legal systems, scientific method, parliamentary procedure, red teams, Socratic dialectic) *deliberately engineer* internal adversarial dynamics: structured adversarial sub-processes produce higher-quality aporia than any single perspective can generate alone. Better aporia → better epistrophe → better adaptation. These institutions are "aporia amplifiers." Formally, this would mean: (a) the teleological unity between adversarial sub-agents is negative on specific dimensions but serves positive unity at the composite level; (b) Section I's adversarial tempo advantage, applied at the sub-agent level, becomes a mechanism for improving the composite's cycle quality; (c) theory of mind (recursive modeling of other agents) is what makes internal adversarial dynamics *productive* rather than merely destructive — you can only run a useful internal debate if the sub-processes can model each other's reasoning. Connection to logozoetic agents: theory of mind is a qualifying property, which may be partly *why* it qualifies — it enables the richer internal aporia that more sophisticated adaptation requires. Status: brainstorm, not even hypothesis yet. But it connects adversarial dynamics (Section I), composition (Section III), the orient cascade (Section II), and logozoetic agent properties (`04-logozoetic-agents/`) in a way that feels structurally motivated. See `LEXICON.md` for related discussion.


## Validation (after theory stabilizes)

- Extend nonlinear sims to characterize regime boundaries
- Developer-as-AAD-agent on real codebase (software worked example)
- Test DAG health metrics against real project outcome data
- Multi-agent intent propagation simulation
- TST testable predictions: specification bound calibration, coherence-coupling measurement
- Simulations 3–6 from old-tst-via-tft-simulation-proposals (Sims 1–2 done as track-b)
- **Flagship empirical agenda**: software unmaintainability threshold and measurement program. Formalize $\mathcal T_{\text{team}} \gt \rho_{\text{total}} / \lVert\delta_{\text{critical}}\rVert$ with observable precursors. This is where AAD could become decisively useful beyond elegant theory.
