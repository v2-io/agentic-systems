# TODO — Open Work Items

**Last reconciled:** 2026-04-22. This file is the living action list. For the 2026-04-21 master audit that seeded some current items, see `msc/opus-audit-2026-04-21.md`. For the 2026-04-22 three-audit batch (Gemini, Codex, Opus), local findings live in `msc/pending-findings-2026-04-22.md` and architectural proposals in `msc/architectural-proposals-2026-04-22.md`. For the 2026-04-02 round, see `msc/analysis-2026-04-02-comprehensive.md` — its concrete fixes are done and archived at the bottom of this file.


## Active — Strategic Architectural Proposals (HIGHEST IMPLIED PRIORITY)

Ten architectural proposals surfaced in the 2026-04-22 audits, each characterized in `msc/architectural-proposals-2026-04-22.md` as an *independent structural investment option* — evaluated on its own merits (beauty / concision / correctness / approachability / fundamentality), not primarily as machinery for subsuming findings. These are at the top of TODO because the project's governing purpose (CLAUDE.md) makes those virtues first-class. Some of these moves are more important than any individual finding; some will subsume several findings as a side-effect.

**Read `msc/architectural-proposals-2026-04-22.md`** for the full portfolio. One-line summaries below.

- **G-BP1 — Natural-parameter / logit reparameterization.** All beliefs in natural exponential-family parameters; additive gradient updates in $\mathbb{R}^n$; link functions at the interface. Merits: **correctness (high)**, concision, fundamentality. Subsumes Finding 2 (unbounded gradient). 2–3 sessions; scoping spike optional.
- **G-BP2 — Variational free-energy framing of strategy IB.** $\Sigma_t$ as a variational approximation of $\pi^\ast$; KL-divergence replaces Shannon MI; variational free energy replaces IB Lagrangian. Merits: **correctness (high)**, fundamentality, beauty. Subsumes Finding 3 (degenerate MI). Scoping spike essential; multi-session.
- **G-BP3 — Fisher-information unification of tempo and gain.** $\delta$ as KL-divergence; $\alpha$, $\eta^\ast$, $\mathcal{T}$ collapse into natural gradient descent; per-dimension becomes the anisotropic special case. Merits: **fundamentality (very high)**, concision, beauty. The largest single move in the portfolio. Major rewrite; scoping spike essential.
- **O-BP1 — Sector-persistence template as organizing principle.** Reframe OUTLINE preamble around "AAD decomposes disturbance for bounded-correction dynamics at each scale." Merits: **approachability (very high)**, beauty, concision. Subsumes Finding 9 (Section II preamble). 1–2 sessions, framing touch, low risk. **Natural first move.**
- **O-BP2 — Four compression operations as one hierarchy.** Agent as portfolio of compression maps with different relevance variables; $M_t$, $\Sigma_t$, shared intent, $\Lambda$ become projections not distinct objects. Merits: **fundamentality (high)**, approachability, beauty. Subsumes Finding 10 (IB status); strengthens existing $G_t$-single-object item. Scoping spike valuable.
- **O-BP3 — Continuous-parameter approximation tiering.** L0/L1/L2, C1/C2/C3, Tier 1/2/3 as points in continuous parameter spaces; results live in 3D operating-regime space. Merits: fundamentality, **beauty (high)**, concision. Subsumes the existing continuous-convention tier-C item; partial on Finding 11.
- **O-BP4 — Continuous-valued strategy DAG.** Edges carry expected-progress rates; nodes aggregate progress fields; replaces Boolean AND/OR for continuous-value domains. Merits: **correctness (high)**, approachability. Partial on Finding 2. Dedicated scoping spike recommended before any portfolio decision.
- **O-BP5 — Orient cascade as recursive adaptive cycle.** AAD applied at every level where a state variable has a correction function and bounded disturbance; unifies deliberation, cascade, and composition. Merits: beauty, fundamentality. No findings directly subsumed; strengthens composition-consistency.
- **O-BP6 — Identity promotion (`#agent-identity` to formal scope statement).** AAD applies to agents on singular causal trajectories; grounds why loop Level-2 access is interventional. Merits: **fundamentality (medium-high)**. Partial on Finding 5 (loop framing). Small (one session); no scoping spike needed.
- **O-BP7 — Known structural absences (meta-proposal).** Four gaps: tier-switching policy, misspecification cost quantification, cross-hierarchy monotonicity, CIY/EIG gap. Each candidate for future scoping spike. Long-term research agenda.

**Proposal clusters.** G-BP1 + G-BP3 + O-BP3 (natural parameters + Fisher geometry + continuous tiering); G-BP1 + O-BP4 (logit + continuous DAG); G-BP2 vs O-BP2 (alternative unifying framings); O-BP1 + O-BP5 + O-BP6 (template + recursion + identity, the "recursive persistence on singular trajectories" picture).

**Recommended first moves** (from rough smallest-payoff-to-effort ordering in the portfolio doc): **O-BP1** (framing touch, high payoff, low risk) → **O-BP6** (one session, localized) → **G-BP1** (fixes a real finding with groundwork in spike).


## Active — Pending Findings

Local findings — scope bugs, mechanical breaks, framing issues. Full characterizations in `msc/pending-findings-2026-04-22.md`. Each finding notes its "subsumed by" architectural proposal (if any); the choice between local repair and architectural move is Joseph's.

### 2026-04-22 batch — 11 findings (1 from pre-audit Gemini, 2 Gemini, 4 Codex, 4 Opus — Opus F1 deduplicated with Gemini pre-audit)

| # | Finding | Severity | Subsumed by |
|---|---------|----------|-------------|
| 1 | L0 residual under on-policy execution | Medium-high | — |
| 2 | Unbounded gradient in credit-assignment signal | High | G-BP1 |
| 3 | Degenerate MI in strategy IB objective | Medium-high | G-BP2 |
| 4 | Section II silent scope narrowing (agency → learning) | Medium | — |
| 5 | Loop framing overstates Level 2 access | Medium | Partial by O-BP6 |
| 6 | Composition timescale heuristic outruns bridge conditions | Medium-high | — |
| 7 | TST overstates git as complete chronica | High | — |
| 8 | (C-iii) mutual-benefit vs (A1) decomposable $G_c$ gap | Medium | — |
| 9 | Section II preamble framing understates survival | Medium-high | O-BP1 |
| 10 | `#information-bottleneck` status mismatches unification role | Low-medium | O-BP2 |
| 11 | Orient cascade step 4c convergence in non-stationary envs | Medium | Partial by O-BP3; compounds with F1 |

**Actionable now (independent of portfolio decisions):**

- **Finding 1** — already characterized; repair ready. 60–90 min. Covariance test stays as primary; residual demoted to exploration-rate-gated secondary.
- **Finding 7** — git claims; sharp and contained. 30–45 min.
- **Finding 10** — IB status reclassification; 15 min.

**Coordinated passes (multiple findings close together):**

- Findings 4 + 9 — both touch Section II scope framing at different layers. 60–90 min combined. Finding 9 absorbed if O-BP1 is adopted.
- Findings 1 + 11 — both concern step 4c mechanism under different failure modes. 30–45 min combined with Finding 1's repair.

**Holding for portfolio decisions:**

- Findings 2, 3 — subsumed by G-BP1 / G-BP2 respectively. Local repairs are wasted work if the architectural moves are pursued.

### 2026-04-21 batch — both RESOLVED 2026-04-22

Historical record of the 2026-04-21 audit residue and its resolution: see `msc/pending-findings-2026-04-21.md`. Both findings closed 2026-04-22.

### ~~Finding A — Temporal coarse-graining gap in `#composition-closure`~~ — RESOLVED 2026-04-22

Option 3 (per-macro-step formulation) executed. `#composition-closure` now carries the timescale ratio $K_c \geq 1$ alongside admissibility, rewrites $\varepsilon_x, \varepsilon_a, \varepsilon_o$ over macro-steps with window-aware $\Lambda_o, \Lambda_a$, restates (P1) at macro granularity, adds an explicit unit-consistency note to the bridge lemma, and records $K_c = 1$ as the previous-formulation special case. The sector-persistence-template instantiation table updated to show $e_m$ (trajectory error at macro-boundaries). The two-Kalman worked example continues to live at $K_c = 1$. See `msc/pending-findings-2026-04-21.md` Finding A for the closed-out resolution note.

### ~~Finding B — `#observation-ambiguity-modulation` is architecture-contaminated~~ — RESOLVED 2026-04-22

$\mathcal{A}(e_\tau)$ recast as an observation-stream property at the Bayesian-optimal level: $I(G;\Omega\mid e,M) / H(\Omega\mid e,M)$ under a reference goal prior $P_{\text{ref}}(G)$. No hypothetical processors appear in the definition; $\kappa_{\text{processing}}$ enters only through the explicit composition $\kappa_{\text{eff}} = \kappa \cdot \mathcal{A}$ in the scope condition. The bias bound simplifies to $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa \cdot I(G;\Omega\mid e,M)$. The operational estimator $\hat{\mathcal{A}}$ now uses a reference interpreter as a measurement instrument; the processor-probing form of $\hat\kappa_{\text{processing}}$ moved to `#directed-separation` where it belongs canonically. Holistic scan of the six other logogenic segments: no similar contamination — the pattern was localized. See `msc/pending-findings-2026-04-21.md` Finding B for the closed-out resolution note.


## Active — Tier-C Deferrals

Foundational moves currently deferred for specific reasons. Not a general "defer" bucket — the bigger-picture items from 2026-04-22 live under "Strategic Architectural Proposals" above, evaluated on their own merits.

- **$G_t$ as single object; $(O_t, \Sigma_t)$ as a property** (Opus 2026-04-21 synthesis §7). Axiomatic split currently; Class 2 agents carry both roles in one representation. A cleaner formulation would define $G_t$ as a single purposeful-state object and treat the decomposition as a property Class 1 agents have. Touches Section II scaffolding. **Defer until more Class 2 logogenic work lands.** Strengthened by O-BP2 (compressions-as-projections); if O-BP2 is pursued, this item converges with it.
- **Continuous convention hierarchy** $N_r \in [1, \infty]$ (Opus 2026-04-21 synthesis §8). C1/C2/C3 are limits of a continuous receding-horizon family. Subsumed by O-BP3 (continuous-parameter tiering) — moving to Strategic Proposals as part of O-BP3.


## Active — Genuinely Open MEDIUM Items

- **Composition scaling with $N$.** Whether closure defect scales polynomially or exponentially with team size (see `#composition-closure` Working Notes). Tree-structured coupling may allow efficient reduction; fully-connected may not. **Scoping spike done** (`msc/spike-composition-scaling-N.md`, 2026-04-22): four distinct readings of "scaling with $N$" identified, five candidate first moves named ($N$-Kalman chain and balanced-tree are cheapest), composing axes ($K_c$ macro-timescale; unity × update-heterogeneity) flagged. Question is well-framed but unresolved; execution deferred. Critical for large-team applications.

- **Multi-timescale stability formalization.** `#multi-timescale-stability` is stage `sketch`; `#temporal-nesting` leans on it. Needs formal $N$-timescale singular perturbation treatment. Partially overlaps with Finding A's repair path if Option 2 (Tikhonov) is chosen.

- **Communication-gain adversarial scope.** `#communication-gain`'s additive model fails for deception (trust is game-theoretic). Either extend or add explicit scope limitation to the segment.

- **Exploit/Explore/Deliberate spike findings.** `#exploit-explore-deliberate` was written, but the adversarial spike noted that the two-stage decomposition and $\Delta V_\Sigma$ approximation are hand-waving (simulation shows unified objective outperforms two-stage; deliberation rarely chosen by oracle). Segment may be substantially rewritten.


## Active — Missing Segments

### AAD Core (`01-aad-core/`)

| Slug | Section | Type | Description |
|------|---------|------|-------------|
| `adversarial-edge-targeting` | III | Derived? | Which strategy edges most valuable to attack — the Section III gap |
| `intent-dag-development` | A | Aside | Convergence history of AND/OR + single-$p$ (archaeological record, source: `msc/04-intent-dag-consolidated.md`) |
| `worked-example-cam` | A | Worked example | Coevolving automata (Miller 2022): AAD ↔ Moore machine mapping, meta-machine as $\varepsilon^\ast = 0$ composition, simplest adaptive agent. Source: `msc/spike-miller-act-bridge.md` §3, `msc/spike-fsa-dag-relationship.md`. Planned in `#composition-closure` Discussion. |

### Section III — Composition Dynamics gaps (from Miller + Hafez integration)

- Latent structural diversity (`msc/spike-neutral-drift-lyapunov.md`)
- Endogenous coupling — $\gamma$ as function of population composition
- Composition transition dynamics (Miller 2022 extreme-transition motif)
- Computational thresholds for social behavior (Miller 2022 ICE framework, Table 12.2)
- Agent opacity (Hafez et al. 2026 backward predictive uncertainty $H_b$)

### Cross-component (cost of AAD scope claims)

| Slug | Component | Relevance |
|------|-----------|-----------|
| `ai-agent-as-act-agent` | 03-logogenic | Written. Confirm status vs. spike. |
| `section-ii-survival` | 03-logogenic | Written. Cross-reference scan with Finding B repair. |
| `coupled-update-dynamics` | 03-logogenic | Written. Coupled formulation directed-separation defers to. |

### No longer open (tracked for cleanup elsewhere)

- ~~`prior-art-positioning`~~ — superseded; prior art integrated into individual segment Discussions.
- ~~`linear-ode-approximation`~~, ~~`exploit-explore-deliberate`~~ — written.
- ~~TST missing four segments (`software-epistemic-properties`, `developer-as-act-agent`, `code-quality-as-observation-infrastructure`, `causal-discovery-from-git`)~~ — written (verified 2026-04-22).


## Active — Presentation

- **Three-way presentation split.** All reviewers recommend: (a) core results, (b) conditional architecture, (c) empirical programs. Single highest-leverage presentation change. Not yet executed.

- **Prior-art positioning synthesis.** Active inference/FEP, POMDP, BDI relationships now in individual segments. A synthesis pass that surfaces the pattern across segments may still be valuable. Source: `msc/02-prior-art-assessment.md`.


## Active — Editorial Hygiene

- **Spike-to-segment reverse-check.** Per the 2026-04-21 cross-cutting pattern: spike-to-segment compression consistently runs one direction (spike stronger than segment). Add to `FORMAT.md` promotion workflow as a standing Gate 2 check: "What did the spike establish that the segment does not say?" — added in Session C.5; verify it's still present and visible.

- **Segment counts in CLAUDE.md "What's Settled" summary** could drift as new segments land; refresh opportunistically. (WORKBENCH.md retired 2026-04-22; live state now lives in OUTLINE.md + segment frontmatter + `bin/lint-outline` output.)


## Active — Promotion Pipeline

**Current state (2026-04-22):** 92 AAD core segments (excluding `old-*` bridges). Per `bin/lint-outline`: 16 claims-verified, 29 deps-verified, 46 draft, 1 unknown. Gate 1 (deps-verified) and Gate 2 (claims-verified) work was in flight before the 2026-04-21 audit cycle; the audit's repairs mostly preserved `draft` status. Recommended next promotion candidates remain the ones from the prior round: `sector-condition-derivation`, `recursive-update-derivation`, `mismatch-decomposition`, `chain-confidence-decay`, `persistence-condition`, `gain-sector-bridge`, `worked-example-kalman`, `discrete-sector-condition`, `satisfaction-gap`, `control-regret`, `graph-structure-uniqueness`. Reconcile stages across `OUTLINE.md` and segment frontmatter on the next promotion pass.


## Active — Lower Priority

- **Observability-dominance product formula.** $\text{conf}_{\text{obs}} = \text{conf} \cdot \text{obs}$ posited, not derived. Label as formulation choice or derive.
- **Strategy-complexity-cost IB operationalization.** $I(\Sigma_t; \pi^\ast \mid M_t)$ undefined in practice.
- **Strategic calibration aggregation.** $L^2$ norm unjustified. Label as design choice.
- **Scope architecture.** "Within AAD's scope" ambiguous between adaptive and agency scope.
- **`loop-interventional-access` status.** "exact" defensible; opening claim could be softened.
- **Between-event dynamics.** $g_M(M_\tau)$ defined but unreferenced. Important for logogenic agents.
- **Fully coupled adversarial dynamics.** Both agents' mismatch co-evolving. Open.
- **`objective-functional` labeling.** "axiomatic" for scalar-comparability is a formulation choice.
- **Heavy-tailed disturbances.** Model S assumes finite second moment.
- **`satisfaction-gap`/`control-regret` convention-dependence.** "exact" but convention-relative diagnostics. Add note to Epistemic Status.
- **External validation design.** Testable predictions not yet tested. Candidates: git data, RL bandits, adaptive controllers.


## Deferred — Project Structure

- Root-level assembly index (when content beyond AAD warrants it)
- `framework/` directory for non-mathematical content
- Multiple index support (paper, preprint, monograph)
- Section IV standalone paper outline (draft at `msc/2026-03-14-section-iv-paper-outline.md`)


## Deferred — Tooling

- `lint-md` directory arguments


## Archive — Work landed before 2026-04-22

Detailed historical items moved out of the active list. Kept here so that future agents can find what was done without expanding this file's top portion.

### 2026-04-21 audit cycle — COMPLETE (commits `6d3f219`, `98179f9`, `70c306d`, `ba2597c`, `499afa3`, `1c3a2d9`, `853888c`)

Session plan derived from `msc/opus-audit-2026-04-21.md` and executed per the deleted `TODO-04-21.md` (recoverable from git). Summary of what landed:

- **Session A** — `#sector-persistence-template` factored out as shared lemma; six persistence-flavored segments (`#persistence-condition`, `#strategy-persistence-schema`, `#team-persistence`, `#composition-closure` bridge lemma, `#tempo-composition`, `#adversarial-destabilization`) re-expressed as template instances. Four honesty fixes: forgetting-as-prerequisite in `#strategy-persistence-schema`, causal-sufficiency gate in `#orient-cascade`, walkback of `#composition-scope-condition` unified-form overreach to three-route disjunction, $\iota_{ij}$ propagation into operational machinery (`#strategic-tempo`, `#strategic-dynamics-derivation`, `#credit-assignment-boundary`).
- **Session B** — `#graph-structure-uniqueness` reframed as Cox-analog for strategy representation; two new meta-segments: `#independence-audit` and `#approximation-tiering`.
- **Session C** — Scope gates in `#composition-closure`, `#unity-dimensions` lead rewritten, `#software-epistemic-properties` P1 codebase-vs-environment scoping, `section-ii-survival` statement-level-vs-operational distinction, FORMAT.md promotion-workflow reverse-check.
- **Session D** — Scoping spike `msc/spike-ib-unification-plan.md` delivered; execution absorbed into `#compression-operations` segment with three integration edits to `#information-bottleneck`, `#strategy-complexity-cost`, `#shared-intent`.
- **Late-cycle Gemini batch** — L1 soft-facilitator gap handled; Finding A and Finding B above are the residue.

### 2026-04-02 Codex round-2 findings — COMPLETE

All numbered items from the round-2 review (strategy-persistence mismatch object, $\Phi$ as independence-model reference, composition-bridge honesty, `value-object` $O_t$-as-parameter qualifier, graph-structure forced-vs-motivated language) resolved in segments. Full history in `msc/analysis-2026-04-02-round2.md`.

### 2026-03-13 consolidated review — mostly COMPLETE

Top issues (1) directed-separation architectural classification, (2) $\alpha$-vs-$\mathcal{T}$ distinction, (3) composition-closure bridge lemma, (4) graph uniqueness at theorem strength, (6) assorted formal issues — all landed. Remaining: (5) `#causal-discovery-from-git` now written; TST overstatement of causal status of git data is covered within that segment.
