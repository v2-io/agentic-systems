# AAD Core Review — Remaining Items (2026-04-01)

Revised from the original `analysis-2026-04-01.md` after a full session of work.
Everything below is what remains actionable; completed items are removed.


## Completed This Session

For the record, the following were identified and resolved:

- **Easy tasks E1–E8** — all completed (outline ordering, missing dependency, CIY decomposition, status fixes, working note correction, content overlap reduction, cross-component reference annotation, forward reference fix)
- **Spike 1** (single-edge strategic dynamics) — sector condition verified, α_Σ = η_edge, promoted to segments
- **Spike 1b** (two-edge strategic dynamics) — evidence starvation derived, unobservable case analyzed, promoted to segments
- **Spike 2** (disturbance model split) — Model D/S distinguished, b=3/2 derived analytically, promoted to 9 segments + NOTATION.md
- **Spike 3** (projection admissibility) — P_adm (P1-P3) defined, two-Kalman instantiation exact, promoted to composition-closure
- **Spike 4** (scalar objective scope) — restriction analyzed, revealed-preference argument, AND-node workaround documented
- **Persistence taxonomy** — three senses (structural/operational/continuity) + five continuity stances added to LEXICON/README, referenced from 11 segments
- **Cycle vocabulary** — Greek phase terms planted into 9 segments where they carry precision
- **README revision** — Novel Results (11 items), Cross-Domain Joining table, Convergent Choices, Maturity Gradient, full Lexicon
- **Directed separation analysis** — detailed holds/fails/unclear for Class 2 agents, added to WORKBENCH


## Still Open: Spikes and Investigations

### Spike 5: External Validation Design (MEDIUM)

**Not attempted this session.** Both reviews note the empirical program is internal validation only. The theory makes testable predictions (persistence threshold, adversarial exponents, weak-dimension bottleneck, evidence starvation depth penalty) that have not been tested against real-world data.

**Candidates for first external test:**
- **Software teams:** Operationalize tempo, disturbance rate, model class fitness from git data. Predict which projects approach the persistence boundary. The TST bridge, but would validate AAD-level predictions.
- **RL agents:** Compare AAD's per-arm persistence predictions to actual arm-dropping behavior in deployed bandits.
- **Control systems:** Compare persistence condition to known stability margins in deployed adaptive controllers beyond the exact Kalman case.

**Priority:** Medium. Important for credibility but the formal theory needs to be more settled first. The disturbance model split (now done) makes the predictions more precise and therefore more testable.

### Coupled Formulation for Class 2 Agents

**The central open problem for 03-logogenic-agents/.** The directed-separation analysis identifies what survives (diagnostic vocabulary, cascade ordering, Section I quantities) and what fails (sequential update, G_t complexity bound, clean M_t persistence analysis). What's needed:

- What new phenomena emerge when separation fails (motivated reasoning, confirmation bias as coupling terms in f_M)
- What the persistence condition becomes for coupled systems (state-dependent α?)
- Which Section II results degrade gracefully vs. break entirely
- Engineering guidance for designing partially-separated LLM agent systems

This is not a spike — it's the scope of a new section. But a spike exploring the simplest coupled case (e.g., a two-state system where perception depends on goals through a single coupling parameter) could establish whether the Lyapunov machinery survives coupling or requires fundamentally different tools.

### AND/OR Parsimony Theorem

Three independent formalism attempts converged on AND/OR. A theorem showing AND/OR is the unique minimal complete basis under the theory's constraints would promote this from "convergent choice" to "derived." Currently in the Convergent Choices category (README.md). No spike attempted.

### P3→Markov Tightening

Currently conditional on causal sufficiency. The conditioning may be removable for agent-constructed strategies where causal sufficiency is guaranteed by construction. The three-part argument (locality from P3, directionality from P1, sufficiency from agent-constructed Σ_t) is plausible but not proven. Upgraded from sketch to conditional (2026-04-01) but not yet at derived.


## Still Open: Theory Gaps

### Strategy Maintenance Loop — Remaining Pieces

The strategy-persistence schema is now verified for three cases, but the full loop has gaps:

- **Signal function for continuous outcomes.** Binary outcomes are resolved (proportional-blame = exact marginal Bayesian). Continuous outcomes, multi-valued signals, and partial observability remain open.
- **Credit assignment for general DAG topologies.** The two-edge spike showed clean attribution for observable intermediates and plan-level fallback for unobservable ones. General multi-parent AND/OR nodes with mixed observability are not addressed.
- ~~**OR-node sector condition.** All verified cases use AND-nodes.~~ **DONE 2026-04-02.** OR-node sector condition verified in `spikes/spike-or-node-strategic-dynamics.md`. Key result: OR-nodes are exploration-gated (not depth-gated like AND). Sector condition holds with ε-greedy exploration; pure greedy fails. SA3 condition added to persistence schema. Scales as 1/k with k alternatives — creates pressure toward pruning.

### Composition — Remaining Pieces

Projection admissibility is now defined and instantiated, but:

- **Computing P1 for nonlinear systems.** The information-preservation condition requires conditional mutual information, tractable only for linear-Gaussian.
- **Choosing ε_I.** The information-preservation threshold is a free parameter.
- **N-agent scaling.** Whether closure defect scales polynomially or exponentially with N depends on coupling structure.
- **Strategy DAG projection.** How individual Σ_t compose under projection is domain-specific and unresolved.
- **Discrete-time bridge lemma formalization.** The continuous-time sketch is sound; the discrete-time contraction-mapping version is standard but not yet written.

### Disturbance Model — Remaining Propagation

The Model D/S split is now in 9 segments + NOTATION.md. Remaining:

- **Mixed environments.** Real domains may have both deterministic drift and stochastic noise. The operationalization segment has guidance but no formal treatment of the mixed case.
- **Heavy-tailed disturbances.** Model S assumes finite second moment. Heavy-tailed disturbances (e.g., adversarial outliers) require different analysis.


## Still Open: Presentation and Positioning

### Three-Way Presentation Split

All three reviewers (Opus, Codex, Gemini) recommend splitting the presentation into:
1. **Core results** — mathematically closed, independently statable
2. **Conditional architecture** — well-typed structure awaiting instantiation
3. **Empirical programs** — testable predictions awaiting validation

This is described as "the single highest-leverage presentation change." Not yet done. The README's Maturity Gradient section captures this conceptually but the segments themselves don't distinguish these layers.

### Prior Art Positioning

The following relationships deserve explicit treatment (dedicated segments or scope notes):

- **Active inference / FEP.** Structural isomorphism with expected free energy noted in CIY segment. AAD's differentiators: persistence condition (no FEP analog), adversarial dynamics, composition machinery. These should be stated explicitly.
- **POMDP planning.** Strategy DAG is close to a policy tree. AAD adds: mismatch dynamics, persistence condition, composition. The embedding is the contribution, not the DAG itself.
- **BDI architecture.** Named the parts; AAD adds dynamics. Brief positioning exists in `msc/02-prior-art-assessment.md` but not in the segments.

### Computational Tractability

Several AAD quantities (A_O, CIY, V_O, model sufficiency S) are defined as expectations or suprema that are intractable to compute in general. The operationalization appendix addresses some. A systematic analysis distinguishing "computable" from "intractable" quantities would strengthen the theory's practical credibility.

### Between-Event Dynamics

The recursive-update segment defines g_M(M_τ) for between-event evolution but this is never developed. For logogenic agents (LLMs generating tokens, humans thinking), the between-event dynamics may be where the real action is — the model evolving through internal computation before the next observation arrives. This connects to the deliberation-cost tradeoff but is more general.

### TST Bridge Formalization

The git → Lyapunov operationalization remains analogical, not formal. The chain git data → Q → comprehension time → developer tempo → α has empirical hypothesis steps. Either formalize the bridge or be explicit that it's an empirical research program. The missing segment #hyp-causal-discovery-from-git is the most prominent gap.


## Priority Order for Remaining Work

1. **Strategy loop completion** — OR-node sector condition, continuous signal function. Extends the verified cases toward the general result. High value, moderate effort.
2. **Three-way presentation split** — editorial restructuring of how the theory is presented. High leverage for reception, no new math.
3. **Prior art positioning** — active inference and POMDP comparisons. Important for credibility, small effort per comparison.
4. **Coupled formulation spike** — simplest Class 2 case. Opens 03-logogenic-agents/ with concrete content. High value, uncertain effort.
5. **External validation design** — first real-world test. Important but depends on the theory being stable enough to predict from.
6. **Composition remaining pieces** — N-agent scaling, discrete-time bridge lemma. Important for Section III but lower priority than Section II completion.
7. **TST bridge formalization** — critical for the operationalization story but somewhat independent of core AAD work.
