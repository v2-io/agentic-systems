# TODO — Open Work Items

Canonical source: `msc/analysis-2026-04-02-comprehensive.md` for full context and rationale. This file is the action list.


## Codex Review Findings (2026-04-02, round 2)

1. ~~**HIGH — Strategy-persistence stated for wrong mismatch object.**~~ **FIXED.** Rewrote Formal Expression in #strategy-persistence-schema to be explicit: schema applies to any mismatch state; what's proved is persistence of δ_s (plan-confidence error), not δ_strategic (calibration residual). Persistence of δ_strategic remains open (requires credit-assignment machinery).

2. ~~**HIGH — Φ called "true plan success probability" but isn't under correlated failure.**~~ **FIXED.** Changed language in #strategic-dynamics-derivation B.5: Φ = P_Σ(θ) is now "independence-model reference value," not "true success probability." Added explicit note that δ_s tracks calibration within the independence model, not calibration to reality.

3. **HIGH — Composition bridge still open.** Already honest in #composition-closure (line 161: "additional assumption beyond (A4)") and #tempo-composition (sketch status). Codex recommends presenting as "AAD plus contraction premise," not as scale invariance discharged. **Action:** Audit prose in OUTLINE.md and README for overstatement. No segment fix needed — the segments are correct.

4. ~~**MEDIUM — value-object "depends on M_t alone" hides O_t dependence.**~~ **FIXED.** Added qualifier: "as a state variable" — O_t enters as a fixed parameter, same as π_cont and N_h.

5. **MEDIUM — Graph-structure-uniqueness overclaims.** P3→Markov is conditional, not forced. Already labeled correctly in segment; language audit needed for consistency elsewhere. Covered by the "forced vs strongly motivated" audit item below.

### Codex Open Questions (answers needed)

- **Canonical strategic mismatch: δ_s or δ_strategic?** Answer: δ_s is proved; δ_strategic is the orient-cascade's operational target but persistence for it is open. Both are legitimate; they measure different things. Document this distinction prominently. **DONE** in #strategy-persistence-schema.

- **Is P̂_Σ calibrated probability or tractable heuristic?** Answer: tractable heuristic (independence-model surrogate). B.5 proves calibration of the surrogate, not calibration to reality. **DONE** in #strategic-dynamics-derivation.

- **Bridge lemma contraction: derive from A4 or make explicit assumption?** Answer: currently an explicit additional assumption. Deriving it from A4 is the open research problem. No action needed — already correctly scoped.

- **Satisfaction-gap/control-regret: intrinsic or convention-relative?** Answer: convention-relative. They are diagnostics relative to a chosen continuation convention and scalarization. The convention is part of the measurement. Already documented in #value-object and #satisfaction-gap but could be more prominent. **Action:** Add brief note to both segments' Epistemic Status.


## Exploit/Explore/Deliberate (in progress)

- ~~**Three-way tradeoff gap.**~~ Segment written. Deep adversarial spike in progress (simulation + first-principles attack). Segment may be substantially rewritten based on spike findings. Current assessment: two-stage decomposition and δ_regret ceiling are genuine; additive objective form and ΔV_Σ approximation are hand-waving.


## MEDIUM — Extensions and Refinements

- **Composition scaling with N.** Whether closure defect scales polynomially or exponentially with team size. Critical for applying the theory to large teams. No spike done.

- **Multi-timescale stability.** #multi-timescale-stability is a sketch; #temporal-nesting leans on it. Needs formal N-timescale singular perturbation treatment.

- ~~**Channel independence caveat propagation.**~~ **DONE.** Caveats added to persistence-condition, adversarial-tempo-advantage, tempo-composition. team-persistence already had it.

- ~~**Edge-independence scope note.**~~ **DONE.** Cross-cutting subsection added to strategy-dag Discussion covering buys/costs/mitigation with cross-references.

- **Communication-gain adversarial scope.** Additive model fails for deception (trust is game-theoretic). Either extend or add explicit scope limitation to #communication-gain.


## Missing Segments (narrative completeness)

### AAD Core (01-aad-core/)

| Slug | Section | Type | Description |
|------|---------|------|-------------|
| ~~exploit-explore-deliberate~~ | ~~II~~ | ~~Written~~ | ~~Three-way allocation — under adversarial spike~~ |
| ~~linear-ode-approximation~~ | ~~A~~ | ~~Written~~ | ~~Pedagogical linear mismatch ODE~~ |
| (new: adversarial-edge-targeting) | III | Derived? | Which strategy edges most valuable to attack — the Section III gap |
| (new: intent-dag-development) | A | Aside | Convergence history of AND/OR + single-p (archaeological record) |
| (new: prior-art-positioning) | A | Detail | Active inference, POMDP, BDI positioning. Source: msc/02-prior-art-assessment.md |

### Cross-component (needed for AAD scope claims)

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

- ~~**"Forced" vs "strongly motivated" language.**~~ **DONE.** Three-tier classification (proved/conditional/choice) now consistent across graph-structure-uniqueness, strategy-dag, and-or-scope.

- ~~**Composition presentation.**~~ **DONE.** composition-consistency and WORKBENCH fixed to flag contraction assumption explicitly.


## Promotion Pipeline

**30 segments at deps-verified** (Gate 1 complete for batches 1+2).

**Next: Gate 2 (claims-verified)** in topological order. Start with the strongest candidates: sector-condition-derivation, recursive-update-derivation, mismatch-decomposition, chain-confidence-decay, persistence-condition, gain-sector-bridge, worked-example-kalman, discrete-sector-condition, satisfaction-gap, control-regret, graph-structure-uniqueness.


## Lower Priority

- **Observability-dominance product formula.** conf_obs = conf * obs posited but not derived. Label as formulation choice or derive.
- **Strategy-complexity-cost IB operationalization.** I(Sigma_t; pi* | M_t) undefined in practice.
- **Strategic calibration aggregation.** L2 norm unjustified. Label as design choice.
- **Scope architecture.** "Within AAD's scope" ambiguous between adaptive and agency scope.
- **loop-interventional-access status.** "exact" defensible; opening claim could be softened.
- **Between-event dynamics.** g_M(M_tau) defined but unreferenced. Important for logogenic agents.
- **Fully coupled adversarial dynamics.** Both agents' mismatch co-evolving. Open.
- **objective-functional labeling.** "axiomatic" for scalar-comparability is a formulation choice.
- **information-bottleneck orphaned.** No downstream segment uses IB objective formally.
- **Heavy-tailed disturbances.** Model S assumes finite second moment.
- **satisfaction-gap/control-regret convention-dependence.** "exact" but convention-relative diagnostics. Add note to Epistemic Status.
- **External validation design.** Testable predictions not yet tested. Candidates: git data, RL bandits, adaptive controllers.


## Project Structure (Deferred)

- Root-level assembly index (when content beyond AAD warrants it)
- `framework/` directory for non-mathematical content
- Multiple index support (paper, preprint, monograph)
- Section IV standalone paper outline (draft at `msc/2026-03-14-section-iv-paper-outline.md`)


## Tooling (Deferred)

- Lint-md directory arguments
