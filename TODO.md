# TODO — Open Work Items

**Last reconciled:** 2026-04-22. This file is the living action list. For the 2026-04-21 master audit that seeded most current items, see `msc/opus-audit-2026-04-21.md`. For the 2026-04-02 round that drove the prior wave of work, see `msc/analysis-2026-04-02-comprehensive.md` — its concrete fixes are done and archived at the bottom of this file rather than carried in the active list.


## Active — 2026-04-21 Pending Findings

Two theoretical findings that survived the 2026-04-21 audit and were explicitly deferred from that session. Both are characterized in `msc/pending-findings-2026-04-21.md`.

### ~~Finding A — Temporal coarse-graining gap in `#composition-closure`~~ — RESOLVED 2026-04-22

Option 3 (per-macro-step formulation) executed. `#composition-closure` now carries the timescale ratio $K_c \geq 1$ alongside admissibility, rewrites $\varepsilon_x, \varepsilon_a, \varepsilon_o$ over macro-steps with window-aware $\Lambda_o, \Lambda_a$, restates (P1) at macro granularity, adds an explicit unit-consistency note to the bridge lemma, and records $K_c = 1$ as the previous-formulation special case. The sector-persistence-template instantiation table updated to show $e_m$ (trajectory error at macro-boundaries). The two-Kalman worked example continues to live at $K_c = 1$. See `msc/pending-findings-2026-04-21.md` Finding A for the closed-out resolution note.

### Finding B — `#observation-ambiguity-modulation` is architecture-contaminated (MEDIUM)

`03-logogenic-agents/src/observation-ambiguity-modulation.md` defines ambiguity $\mathcal{A}(e_\tau)$ using *hypothetical* $\kappa = 1$ and $\kappa = 0$ processors, conflating observation properties with processor properties. The variable should be a property of the observation stream itself (e.g., conditional entropy of the generative process given the event) so that the downstream $\kappa \times \mathcal{A}$ product is an explicit composition rather than built into the definition.

**Repair direction:** recast $\mathcal{A}(e)$ as a domain quantity using the $\kappa_{\text{selection}} / \kappa_{\text{processing}}$ split from `msc/spike-kappa-hb-operationalization.md`. Preserve cross-references from `section-ii-survival`'s error-structure analysis.

**Effort:** 60–90 minutes. Consider scoping a broader logogenic consistency pass first — other logogenic segments may make similar architecture-contaminated moves.


## Active — Tier-C Deferrals (Opus 2026-04-21 bigger-picture synthesis)

These are foundational moves identified in `msc/opus-audit-2026-04-21.md` §"Bigger-picture synthesis" that were explicitly deferred. Not to be opened casually.

- **$G_t$ as single object; $(O_t, \Sigma_t)$ as a property** (Opus synthesis §7). The split is currently axiomatic. Class 2 (LLM) agents carry both roles in one representation; a cleaner formulation would define $G_t$ as a single purposeful-state object and treat the decomposition as a property Class 1 agents have. Touches Section II scaffolding. **Defer** until more Class 2 logogenic work lands.

- **Continuous convention hierarchy** $N_r \in [1, \infty]$ (Opus synthesis §8). C1/C2/C3 are limits of a continuous receding-horizon family. A continuous parameter subsumes the three conventions and makes monotonicity a one-line claim ($A_O(N_r)$ weakly monotone). Low urgency; natural part of a future `#value-object` revision pass.


## Active — Genuinely Open MEDIUM Items

- **Composition scaling with $N$.** Whether closure defect scales polynomially or exponentially with team size (see `#composition-closure` Working Notes line 179). Tree-structured coupling may allow efficient reduction; fully-connected may not. No spike done. Critical for large-team applications.

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

Per `WORKBENCH.md` §"Not Yet Written":

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

- ~~`prior-art-positioning`~~ — superseded; prior art integrated into individual segment Discussions. Noted in `WORKBENCH.md` §"Not Yet Written".
- ~~`linear-ode-approximation`~~, ~~`exploit-explore-deliberate`~~ — written.
- ~~TST missing four segments (`software-epistemic-properties`, `developer-as-act-agent`, `code-quality-as-observation-infrastructure`, `causal-discovery-from-git`)~~ — written (verified 2026-04-22). WORKBENCH still reflects old state; update on next substantial WORKBENCH touch.


## Active — Presentation

- **Three-way presentation split.** All reviewers recommend: (a) core results, (b) conditional architecture, (c) empirical programs. Single highest-leverage presentation change. Not yet executed.

- **Prior-art positioning synthesis.** Active inference/FEP, POMDP, BDI relationships now in individual segments (per WORKBENCH). A synthesis pass that surfaces the pattern across segments may still be valuable. Source: `msc/02-prior-art-assessment.md`.


## Active — Editorial Hygiene

- **Spike-to-segment reverse-check.** Per the 2026-04-21 cross-cutting pattern: spike-to-segment compression consistently runs one direction (spike stronger than segment). Add to `FORMAT.md` promotion workflow as a standing Gate 2 check: "What did the spike establish that the segment does not say?" — added in Session C.5; verify it's still present and visible.

- **CLAUDE.md / WORKBENCH.md drift.** Stage and segment-count tables in `WORKBENCH.md` lag actual tree state (§"Segment Status" still says "Section III 14 segments", "TST 4 missing", etc.; actual is higher and complete). Touch on next substantial WORKBENCH edit.


## Active — Promotion Pipeline

**Current state (2026-04-22):** 92 AAD core segments (excluding `old-*` bridges); all at `draft` stage per most-recent frontmatter scans. Gate 1 (deps-verified) and Gate 2 (claims-verified) work was in flight before the 2026-04-21 audit cycle; the audit's repairs mostly preserved `draft` status. Recommended next promotion candidates remain the ones from the prior round: `sector-condition-derivation`, `recursive-update-derivation`, `mismatch-decomposition`, `chain-confidence-decay`, `persistence-condition`, `gain-sector-bridge`, `worked-example-kalman`, `discrete-sector-condition`, `satisfaction-gap`, `control-regret`, `graph-structure-uniqueness`. Reconcile stages across `OUTLINE.md`, `WORKBENCH.md`, and segment frontmatter on the next promotion pass.


## Active — Lower Priority

- **Observability-dominance product formula.** $\text{conf}_{\text{obs}} = \text{conf} \cdot \text{obs}$ posited, not derived. Label as formulation choice or derive.
- **Strategy-complexity-cost IB operationalization.** $I(\Sigma_t; \pi^* \mid M_t)$ undefined in practice.
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
