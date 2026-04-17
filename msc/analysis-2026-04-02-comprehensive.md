# Comprehensive AAD Core Review — 2026-04-02

Consolidates the full review of `01-aad-core/` (68 segments) with all still-relevant findings from `analysis-2026-04-01.md`, `analysis-2026-04-01-remaining.md`, `analysis-2026-04-02-synthesis.md`, and `analysis-2026-04-02-round2.md`. Items resolved since those analyses were written are marked ~~struck~~ and noted. Items from the new review that were not in prior analyses are marked **NEW**.

---

## 1. Overall Assessment

AAD is a well-constructed integrative framework — 68 segments forming a coherent argument from adaptive-systems axioms through purposeful agency to multi-agent composition. The epistemic honesty system is the single most impressive feature: nearly every segment correctly self-classifies. The theory achieves genuine integration of control theory, causal inference, information theory, and agent architecture.

**Section I** (28 segments): Mathematically tight. The Lyapunov persistence machinery is exact and well-proved. Gain-sector bridge grounds the central assumption (GA-3) in verifiable properties. Discrete-sector-condition closes GA-5.

**Section II** (25 segments): Strong diagnostic core (satisfaction gap / control regret) and novel architectural classification (directed separation). Strategy-revision loop remains the weakest formal chain (signal function, credit assignment, mixed AND/OR persistence).

**Section III** (15 segments): Promising structure grounded in simulations. Composition-closure framework is sophisticated but bridge lemma has contraction gap. Adversarial dynamics are well-validated.

**Appendices** (10 segments): Rigorous support. Worked examples validate the full chain. One missing segment (#linear-ode-approximation).

---

## 2. Resolved Items (from prior analyses)

All of the following were identified in prior analyses and have been verified as fixed:

- ~~Codex #1: Q_O causal validity conditions on wrong state~~ — Fixed in value-object.md (do-operator severs confounding)
- ~~Codex #2: Orient cascade contradicts 2×2 diagnostic~~ — Fixed ("if feasible" gate removed; all four quadrants handled)
- ~~Codex #3: Strategy-persistence overstates Prop B.5~~ — Fixed (distinguishes plan-confidence δ_s from calibration δ_strategic)
- ~~Codex #4: Composition bridge assumes extra contraction~~ — Caveat added to tempo-composition
- ~~Codex #5: A_O mixes full-policy and one-step~~ — Fixed (canonical one-step improvement convention)
- ~~Codex #6: Graph-structure-uniqueness overclaims~~ — Title/summary qualified
- ~~Spike 1: Single-edge strategic dynamics~~ — Promoted to segments
- ~~Spike 2: Disturbance model split~~ — Model D/S promoted to 9 segments + NOTATION.md
- ~~Spike 3: Projection admissibility~~ — P_adm (P1-P3) defined; two-Kalman instantiation exact
- ~~Spike 4: Scalar objective scope~~ — Revealed-preference argument; AND-node workaround documented
- ~~E1-E8: Editorial fixes~~ — All completed (outline ordering, chronica dependency, CIY decomposition, status fixes, working note correction, content overlap, cross-component refs, forward refs)
- ~~Gain-sector bridge~~ — Written as segment; GA-3 now derivable from directional fidelity (B1)
- ~~Persistence disambiguation~~ — Three senses (structural/operational/continuity) defined
- ~~do(.) notation in causal-hierarchy-requirement~~ — Fixed
- ~~Stale blocker in directed-separation-under-composition~~ — Updated
- ~~model-sufficiency status~~ — Fixed (axiomatic)
- ~~adversarial-destabilization status~~ — Fixed (conditional)
- ~~Dependency cycle gain-sector-derivation ↔ gain-sector-bridge~~ — Fixed
- ~~kappa_processing conditioning~~ — Fixed (conditions on M_{tau-})
- ~~Plan confidence marking in worked-example-strategy~~ — Fixed (caveat added)
- ~~OR-node sector condition~~ — Verified in spike; SA3 condition added

---

## 3. Still-Open Issues

### 3.1 HIGH — Genuine Open Gaps

**H1. Three-way exploit/explore/deliberate tradeoff.**
The only --GAP-- in Section II's OUTLINE. No spike done. The individual pieces exist (#temporal-optimality, #explicit-strategy-condition, #deliberation-cost) but the integration into a single resource-allocation framework does not. This is the one genuinely missing argument in Section II.
- *Affects:* Section II completeness
- *Source:* OUTLINE.md, analysis-2026-04-01

### 3.2 Resolved by Spikes (confirmed closed)

The following were listed as HIGH in prior analyses but have been addressed by spike work and promoted to segments:

- ~~**Signal function for strategy edge updates.**~~ Resolved at theory level. #credit-assignment-boundary has the gradient-based default formalized as a `[Formulation]` with directional fidelity (B1), O(|V|+|E|) computation, REINFORCE connection, and correlated-failure caveat. #strategy-persistence-schema item 5 says "Characterized at the theory level... the specific update algorithm is domain engineering, not theory." Continuous-outcome and multi-parent cases are extensions, not blocking gaps.

- ~~**Mixed AND/OR DAG persistence.**~~ Four topologies verified (Props B.1-B.4). Plan-level persistence proved via B.5 without needing per-edge credit assignment. Mixed case is a natural extension; the structural argument (per-edge sector conditions transfer individually) covers the general case at the plan level.

- ~~**Bridge lemma contraction.**~~ Sketched in #composition-closure with (A4) → trajectory error bounded at ε*/α_c. Correlated Kalman spike shows ε*=0 at steady state. Projection admissibility (P1-P3) defined and instantiated. The contraction assumption is documented and bounded, not unaddressed. Discrete-time formalization is the remaining piece.

- ~~**Strategic persistence gain-collapse.**~~ α_Σ = 1/(n+1) derived in single-edge spike. Forgetting fix stabilizes α. Critical experience n* implicit in the derivation. This is a prose clarification, not a theory gap.

### 3.2 MEDIUM — Structural Improvements

**M1. Channel independence caveat propagation.**
Adaptive tempo T = sum(nu_k * eta_k*) and scalar persistence condition both assume informationally independent channels. Simulation shows 72% overestimate in anisotropic 3D systems. Caveat added to adaptive-tempo but not propagated to downstream segments.
- *Segments needing caveat:* persistence-condition, adversarial-tempo-advantage, team-persistence, tempo-composition
- *Source:* analysis-2026-04-02-synthesis 1b, new review

**M2. **NEW** Observability-dominance product formula unjustified.**
conf_obs = conf * obs is posited but not derived from the gain principle. Why multiply rather than another operation? Should be derived or flagged as formulation choice.
- *Affects:* observability-dominance
- *Source:* new review

**M3. Strategy-complexity-cost IB objective not operationalized.**
The mutual information term I(Sigma_t; pi* | M_t) — "decision relevance" — is undefined in practice. The depth bound d* is rigorous; the broader IB framework for strategies is aspirational.
- *Affects:* strategy-complexity-cost
- *Source:* analysis-2026-04-01-remaining, new review

**M4. Composition scaling with N.**
Whether closure defect scales polynomially or exponentially with team size is unresolved. Critical for applying the theory to large teams.
- *Affects:* composition-closure, team-persistence
- *Source:* analysis-2026-04-01-remaining, new review

**M5. **NEW** Strategic calibration aggregation unjustified.**
L2 aggregation with criticality weighting is a "reasonable first pass, not derived." Why not L-infinity (worst-calibrated edge)? The aggregation function is a design choice that should be more carefully defended or explicitly labeled as such.
- *Affects:* strategic-calibration
- *Source:* new review

**M6. Communication-gain additive model fails for adversarial settings.**
Four-denominator model treats all uncertainty sources as independent zero-mean noise. Conservative for trustworthy communication but fails for deception where trust is game-theoretic.
- *Affects:* communication-gain, team-persistence
- *Source:* analysis-2026-04-01-remaining, new review

**M7. **NEW** multi-timescale-stability is a sketch.**
N-timescale singular perturbation is referenced by temporal-nesting but the formal treatment is incomplete. For a theory claiming timescale stratification as a feature, this is notable.
- *Affects:* temporal-nesting
- *Source:* new review

**M8. Edge-independence assumption addressed nowhere.**
Flagged in strategy-dag, strategic-calibration, chain-confidence-decay, credit-assignment-boundary, but no segment provides formal treatment of correlated edges. Acknowledged everywhere, resolved nowhere.
- *Affects:* Multiple Section II/III segments
- *Source:* analysis-2026-04-02-synthesis, new review

### 3.3 MEDIUM — Presentation and Positioning

**P1. Three-way presentation split.**
All three original reviewers recommend splitting into: (a) core results, (b) conditional architecture, (c) empirical programs. "Single highest-leverage presentation change." Not yet done. README's Maturity Gradient captures conceptually but segments don't distinguish layers.
- *Source:* analysis-2026-04-01-remaining, msc/2026-03-13-feedback.md

**P2. Prior art positioning.**
Active inference/FEP, POMDP, BDI relationships deserve explicit treatment. Segment #prior-art-positioning is missing. Brief positioning exists in msc/02-prior-art-assessment.md but not in segments. AAD's differentiators vs. active inference: persistence condition (no FEP analog), adversarial dynamics, composition machinery.
- *Source:* analysis-2026-04-01, analysis-2026-04-01-remaining

**P3. **NEW** "Forced" vs "strongly motivated" language inconsistency.**
strategy-dag Discussion says "strongly motivated" while other segments and OUTLINE.md sometimes say "forced." Acyclicity IS proved; Markov IS conditional. These should be consistently distinguished throughout.
- *Source:* analysis-2026-04-02-round2 DD3, new review

### 3.4 LOWER — Open Questions and Refinements

**L1. Scope architecture: adaptive vs agency scope.**
scope-condition has two formal scope levels, but "within AAD's scope" remains ambiguous in prose. Multiple review rounds flagged this. Current caveat paragraphs address it but a structural split (or formal "scope levels" subsection) would be cleaner.
- *Source:* analysis-2026-04-02-round2 DD1

**L2. loop-interventional-access status.**
Still "exact." Claim is about data CHARACTER (interventional by construction) vs. identified estimates (regime-dependent). Current status is defensible but the opening claim could be softened.
- *Source:* analysis-2026-04-02-round2 DD2

**L3. Between-event dynamics g_M(M_tau) never developed.**
Defined in recursive-update but unreferenced elsewhere. For logogenic agents, this is where the interesting dynamics live (LLMs generating tokens, humans deliberating between observations).
- *Source:* analysis-2026-04-01, analysis-2026-04-01-remaining

**L4. Fully coupled adversarial dynamics.**
All adversarial results treat the faster agent's tempo as exogenous. Fully coupled analysis where both agents' mismatch co-evolve is open.
- *Source:* analysis-2026-04-01-remaining, new review

**L5. **NEW** Objective-functional epistemic labeling.**
Labeled "axiomatic" but the scalar-comparability commitment is a substantive formulation choice. "Formulation" with "axiomatic" grounding would be more precise.
- *Source:* new review

**L6. **NEW** information-bottleneck is orphaned.**
No downstream segment formally uses the IB objective; it provides conceptual framing only. Either formalize its role (strategy-complexity-cost is the closest consumer) or note its status as motivational.
- *Source:* analysis-2026-04-02-round2

**L7. Composition assumes AAD-shaped macro-agents.**
Admissibility (A1)-(A4) constrains the macro-agent to be AAD-shaped. This IS acknowledged in composition-closure (verified), but the Discussion could be more explicit that this is a constrained representation test, not unconstrained scale-invariance.
- *Source:* analysis-2026-04-02-round2 N4

**L8. Heavy-tailed disturbances.**
Model S assumes finite second moment. Heavy-tailed environments require different analysis.
- *Source:* analysis-2026-04-01-remaining

**L9. **NEW** Satisfaction-gap/control-regret convention-dependence.**
Both labeled "exact" but are convention-dependent on value-object's horizon/policy conventions. "Conditional" might be more accurate, or the convention-dependence should be noted in Epistemic Status.
- *Source:* new review

---

## 4. Missing Segments and Narrative Gaps

### 4.1 AAD Core (01-aad-core/) — OUTLINE Gaps

| Gap | Section | Type | Description | Difficulty |
|-----|---------|------|-------------|------------|
| #exploit-explore-deliberate | II | Derived? | Three-way allocation with Sigma_t. Connects temporal-optimality, explicit-strategy-condition, deliberation-cost. **The only Section II gap.** | Medium — needs to formalize the three cost terms as competing draws on the same resource budget |
| #adversarial-edge-targeting | III | Derived? | Which strategy edges are most valuable to attack. Connects to adversarial-destabilization and observability-dominance. | Medium — likely involves sensitivity analysis on DAG structure |
| #linear-ode-approximation | A | Detail | Pedagogical linear mismatch ODE. Currently the linear form appears only in mismatch-dynamics. A standalone appendix would let mismatch-dynamics focus on the qualitative behavior and point here for the full linear treatment. | Small |

### 4.2 AAD Core — Missing Appendices (from WORKBENCH.md)

| Gap | Type | Description | Difficulty |
|-----|------|-------------|------------|
| #intent-dag-development | Aside | Convergence history: three independent formalism attempts all arrived at AND/OR + single-parameter edges. Currently described in README's Convergent Choices; a segment would preserve the archaeological record. | Small |
| #prior-art-positioning | Detail | Hafez, IBM, BDI, active inference positioning. Source material in msc/02-prior-art-assessment.md. | Medium |

### 4.3 Segments at Sketch Status Needing Development

| Segment | Current Status | What's Needed |
|---------|---------------|---------------|
| #tempo-composition | sketch | Close epsilon* → C_coord mapping. Bridge lemma contraction is the gate (discrete-time formalization pending). |
| #multi-timescale-stability | sketch | Formal N-timescale singular perturbation treatment. |
| #strategy-persistence-schema | sketch | Natural next step: mixed AND/OR DAGs (four pure topologies verified). Formalize strategic disturbance rho_Sigma. |

### 4.4 Cross-Component Gaps Relevant to AAD

These are tracked in other components' OUTLINEs but their absence affects how AAD's scope claims read:

| Gap | Component | Relevance to AAD |
|-----|-----------|-------------------|
| #ai-agent-as-act-agent | 03-logogenic | Validates Section II scope claims about Class 2 agents |
| #section-ii-survival | 03-logogenic | Documents which Section II results survive without directed separation (16/24 exactly, 5 approximately, 2 require modification per spike) |
| #coupled-update-dynamics | 03-logogenic | The coupled formulation that Section II's directed-separation explicitly defers to |
| #developer-as-act-agent | 02-tst-core | Validates Section II for human agents (developer as (M_t, O_t, Sigma_t)) |
| #causal-discovery-from-git | 02-tst-core | Validates causal-information-yield and loop-interventional-access for software domain |

---

## 5. Promotion Pipeline

### 5.1 Recommended First Promotion Batch (Dependency Leaves)

These segments have zero or only definitional dependencies and should be the first batch promoted to `deps-verified`:

| Segment | Type | Dependencies |
|---------|------|-------------|
| temporal-optimality | Postulate | none |
| agent-environment | Definition | none |
| causal-structure | Postulate | agent-environment |
| observation-function | Definition | agent-environment |
| action-transition | Definition | agent-environment |
| pearl-causal-hierarchy | Definition | causal-structure, scope-condition |
| chronica | Definition | agent-environment, observation-function, action-transition, causal-structure |

### 5.2 Strongest Candidates for Full Promotion to `candidate`

These segments are closest to passing all four gates (deps-verified, claims-verified, format-clean, candidate):

1. **sector-condition-derivation** — Exact Lyapunov proofs. The mathematical backbone.
2. **recursive-update-derivation** — Uniqueness + 7 counterexamples. Thorough.
3. **mismatch-decomposition** — Clean result with correct assumptions.
4. **chain-confidence-decay** — Mathematical identity. Trivially exact.
5. **persistence-condition** — Core result with clear three-sense disambiguation.
6. **gain-sector-bridge** — Grounds GA-3. Well-verified.
7. **worked-example-kalman** — End-to-end exact. Validates the chain.
8. **discrete-sector-condition** — Closes GA-5. Rigorous.
9. **satisfaction-gap + control-regret** — Clean definitions with diagnostic power.
10. **graph-structure-uniqueness** — Acyclicity proved; Markov conditional but well-argued.

### 5.3 Segments Needing Work Before Promotion

| Segment | Issue |
|---------|-------|
| strategic-calibration | L2 aggregation is a design choice; label explicitly (M5) |
| strategy-persistence-schema | Mixed AND/OR is natural next step; four topologies verified |
| tempo-composition | Discrete-time bridge lemma formalization pending |
| unity-dimensions | U_obs has no formula; U_Sigma circular |
| multi-timescale-stability | Sketch status; needs formal treatment (M7) |

---

## 6. External Validation Design (Deferred but Important)

Not attempted. Theory makes testable predictions not yet tested against real-world data.

**Candidates:**
- Software teams: git data → developer tempo → persistence boundary prediction
- RL agents: bandit arm-dropping matches persistence-condition prediction
- Control systems: adaptive controllers → sector condition verification
- Multi-agent: team tempo vs. individual tempo (sub-additive inequality)

**Priority:** Medium — formal theory needs settling first; disturbance model split makes predictions more precise.

---

## 7. What the Prior Analyses Covered That Is Now Fully Resolved

For the record, the following investigation threads from the prior analysis files are now complete and do not need further attention:

- Directed separation scope analysis (architectural classification promoted)
- Persistence taxonomy (three senses defined and propagated)
- Alpha/T relationship (verified for all correction function classes)
- Edge semantics tension (resolved as regime-indexed causal efficacy)
- Correlated Kalman composition (epsilon*=0 at steady state for all rho)
- Scalar objective scope (revealed-preference argument)
- Model D / Model S distinction (derived and propagated to 9 segments)
- OR-node sector condition (SA3 added; exploration-gated)
- All six Codex diagnostic chain items (Q_O conditioning, cascade consistency, B.5 overstatement, bridge contraction caveat, A_O convention, graph-uniqueness language)
- Gain-sector bridge (GA-3 grounded in directional fidelity)
- All editorial fixes E1-E8
