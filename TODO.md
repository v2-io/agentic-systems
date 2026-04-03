# TODO — Open Work Items

Canonical source: `msc/analysis-2026-04-02-comprehensive.md` for full context and rationale. This file is the action list.


## HIGH — Genuine Open Gaps

- **Three-way exploit/explore/deliberate tradeoff.** The only --GAP-- in Section II OUTLINE. Write segment connecting #temporal-optimality, #explicit-strategy-condition, #deliberation-cost into a resource-allocation framework. No spike done yet — the pieces exist but the integration does not.


## MEDIUM — Extensions and Refinements

- **Composition scaling with N.** Whether closure defect scales polynomially or exponentially with team size. Critical for applying the theory to large teams. No spike done.

- **Multi-timescale stability.** #multi-timescale-stability is a sketch; #temporal-nesting leans on it. Needs formal N-timescale singular perturbation treatment.

- **Channel independence caveat propagation.** Caveat added to #adaptive-tempo; propagate to #persistence-condition, #adversarial-tempo-advantage, #team-persistence, #tempo-composition (72% overestimate in anisotropic systems).

- **Edge-independence scope note.** Correlated edges flagged in #strategy-dag, #strategic-calibration, #chain-confidence-decay, #credit-assignment-boundary. No segment provides formal treatment. Either formalize or add a single cross-cutting scope note.

- **Communication-gain adversarial scope.** Additive model fails for deception (trust is game-theoretic). Either extend or add explicit scope limitation to #communication-gain.


## Missing Segments (narrative completeness)

### ACT Core (01-act-core/)

| Slug | Section | Type | Description |
|------|---------|------|-------------|
| (new: exploit-explore-deliberate) | II | Derived? | Three-way allocation with Sigma_t — **the** Section II gap |
| (new: adversarial-edge-targeting) | III | Derived? | Which strategy edges most valuable to attack — the Section III gap |
| #linear-ode-approximation | A | Detail | Pedagogical linear mismatch ODE — the only missing appendix segment |
| (new: intent-dag-development) | A | Aside | Convergence history of AND/OR + single-p (archaeological record) |
| (new: prior-art-positioning) | A | Detail | Active inference, POMDP, BDI positioning. Source: msc/02-prior-art-assessment.md |

### Cross-component (needed for ACT scope claims)

| Slug | Component | Relevance |
|------|-----------|-----------|
| #ai-agent-as-act-agent | 03-logogenic | Validates Section II for Class 2 agents |
| #section-ii-survival | 03-logogenic | Which Section II results survive without directed separation |
| #coupled-update-dynamics | 03-logogenic | The coupled formulation directed-separation defers to |
| #developer-as-act-agent | 02-tst-core | Validates Section II for human agents |
| #causal-discovery-from-git | 02-tst-core | Validates CIY and loop-interventional-access for software domain |


## Presentation

- **Three-way presentation split.** All reviewers recommend: (a) core results, (b) conditional architecture, (c) empirical programs. Single highest-leverage presentation change.

- **Prior art positioning.** Active inference/FEP, POMDP, BDI relationships. Source: msc/02-prior-art-assessment.md.

- **"Forced" vs "strongly motivated" language.** Audit for consistency: acyclicity IS proved, Markov IS conditional.


## Promotion Pipeline

**First batch (dependency leaves):** temporal-optimality, agent-environment, causal-structure, observation-function, action-transition, pearl-causal-hierarchy, chronica.

**Strongest candidates for full promotion:** sector-condition-derivation, recursive-update-derivation, mismatch-decomposition, chain-confidence-decay, persistence-condition, gain-sector-bridge, worked-example-kalman, discrete-sector-condition, satisfaction-gap, control-regret, graph-structure-uniqueness.


## Lower Priority

- **Observability-dominance product formula.** conf_obs = conf * obs posited but not derived from gain principle. Minor — label as formulation choice or derive.
- **Strategy-complexity-cost IB operationalization.** I(Sigma_t; pi* | M_t) undefined in practice. Depth bound d* is rigorous; broader framework is aspirational.
- **Strategic calibration aggregation.** L2 norm unjustified. Label explicitly as design choice.
- **Scope architecture.** "Within ACT's scope" ambiguous in prose between adaptive and agency scope.
- **loop-interventional-access status.** "exact" defensible; opening claim could be softened.
- **Between-event dynamics.** g_M(M_tau) defined but unreferenced. Important for logogenic agents.
- **Fully coupled adversarial dynamics.** Both agents' mismatch co-evolving. Open.
- **objective-functional labeling.** "axiomatic" for scalar-comparability is a formulation choice.
- **information-bottleneck orphaned.** No downstream segment uses IB objective formally.
- **Heavy-tailed disturbances.** Model S assumes finite second moment.
- **satisfaction-gap/control-regret convention-dependence.** "exact" but convention-dependent.
- **External validation design.** Testable predictions not yet tested. Candidates: git data, RL bandits, adaptive controllers.


## Project Structure (Deferred)

- Root-level assembly index (when content beyond ACT warrants it)
- `framework/` directory for non-mathematical content
- Multiple index support (paper, preprint, monograph)
- Section IV standalone paper outline (draft at `msc/2026-03-14-section-iv-paper-outline.md`)


## Tooling (Deferred)

- Lint-md directory arguments
