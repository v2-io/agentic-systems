# Running Outline — FINAL Report Structure

Living document. Updates after segments that change my sense of what the report should emphasize.

**Last revision:** 2026-04-25, end of Section I (30 main-section + 4 appendix-A segments read).

## Section A — Instructions stress-test

This audit is the first to use the v2 instructions, with mid-session refinements. Notable:

- The v2 instructions failed §4.4 in 0/3 agents (me, Codex, Gemini) per Joseph. Failure mode self-diagnosed: soft "consider writing" + "mental walk-through is enough" framing didn't trigger the consideration step.
- Mid-session §4.4 strengthening landed (Aside + IMPORTANT SELF-CHECK, plus the historical-honesty paragraph at top of file).
- Mid-session §4.2 update added the appendix-back-pointer exception (main-section→appendix-A back-pointers OK to read in-context, not critical findings).
- Mid-session §4.4 prompt 3 (math verification) refined to "at your discretion" with front-of-OUTLINE-over-verified vs back-of-OUTLINE-under-verified asymmetry guidance.
- Mid-session prompts 12 (subjective value) and 13 (field contribution) added — applied from reflection 24 forward.
- The CLAUDE.md / CLAUDE-2.md split and MEMORY.md / CHANGELOG.md migration landed mid-session to reduce auto-load priming bleed.

**For the report's Section A:** the audit was simultaneously the experiment and the iteration on the experiment's instructions. The instructions ended in a stronger state than they started.

## Section B — Findings under burden of proof

**F-A (root-cause): Depends-list incomplete vs Formal Expression usage.**

Five instances (rows 2, 11, 12, 17, 18 in OUTLINE) where a segment's `depends:` list is missing slugs whose symbols appear in the Formal Expression. Pattern is rooted at `def-observation-function` (row 2): it uses $a_{t-1}$ but doesn't depend on `def-action-transition` (row 3, downstream in OUTLINE). The drift propagates through `form-agent-model` to multiple downstream segments.

Root-cause fix: add `def-action-transition` to `def-observation-function`'s depends. This propagates the fix transitively for F-A2, F-A3, F-A5.

Independent F-A drifts: F-A1 (`scope-adaptive-system` missing `def-chronica`); F-A4 (`form-event-driven-dynamics` missing `form-agent-model`).

**Severity:** mechanical / editorial. Confidence: high. Status: still real (verified against frontmatter directly).

**F-B1 (candidate): Possibly-stale "Section IV" / `AAD-FULL.md` reference.**

`form-event-driven-dynamics` Discussion mentions "Section IV gap (see the three-part tempo decomposition gap in `AAD-FULL.md`)." "Section IV" was the old TST location before the four-component split; `AAD-FULL.md` may not exist in current repo. To verify in §6.1 Phase-2.

**F-C series RETIRED.** The 7 instances logged in reflections 6-21 are all instances of the appendix-back-pointer convention (main-section result citing Appendix A derivation). Per the §4.2 mid-session refinement, this is the standard "result-in-body, proof-in-appendix" convention, not a critical finding. Recasting as Section E confirmation of convention.

## Section C — Integration-debt vs theory-gap diagnosis

*To populate in §6.1 Phase-2 after segment-by-segment pass.*

## Section D — Bigger-picture pondering (Hypothesis-tier)

Accumulating candidates from reflection prompts (especially #7, #8, #10):

1. **Signed-coupling pattern across template instantiations as Section III's organizing principle.** Every effective $\rho_\xi$ in the result-sector-persistence-template instantiations is "environmental disturbance + cross-agent contribution with sign encoding cooperative vs adversarial coupling." Six segments instantiate this. Could be elevated as a Section III meta-segment.

2. **Experience discounting / forgetting / consolidation as architectural primitive.** Multiple convergent threads: schema-strategy-persistence requires forgetting rate; form-consolidation-dynamics formalizes consolidation regime; deriv-detection-latency (per priming) connects to stability-induced-myopia. Worth unifying.

3. **"Matched vs forced" coordinate distinction.** AAD has *forced* coordinates at chain (log-additive), divergence (reverse-KL), update (log-odds), metric (Fisher) layers via Cauchy-FE / Čencov uniqueness. Lyapunov quadratic is *matched*, not forced. The distinction is structural scope-honesty. Could be elevated in disc-additive-coordinate-forcing.

4. **"Expected-bridge + stochastic-disturbance" composition meta-pattern.** Bridge theorems hold in expected value; per-step noise enters as Model S disturbance in Prop A.1S framework. Two layers compose cleanly. Worth surfacing.

5. **Type/token distinction as meta-architectural commitment.** scope-agent-identity makes AAD token-level. Should be visible across logogenic-agents segments.

6. **Structural-adaptation-as-deliberation-with-massive-Δτ.** Recurring informal analogy across der-deliberation-cost, result-structural-adaptation-necessity, der-temporal-nesting. Either formalize or explicitly retire.

7. **Gain-collapse / stability-induced-myopia / detection-latency-blowup as one pathology.** Multiple names for what may be the same agent failure mode.

8. **Seven-attack pattern as discipline.** deriv-recursive-update tests its own result against seven counterexample attacks. Other inevitability-core segments could adopt this discipline.

## Section E — Confirmation and confidence calibration

The framework's discipline holds substantially across Section I. Notable confirmations:

- **Inevitability-core segments live up to advertising.** def-recursive-update / deriv-recursive-update, result-mismatch-decomposition, result-persistence-condition, result-sector-condition-stability, der-gain-sector-bridge — all at status:exact or robust-qualitative with clean derivations and honest tier-stratification.
- **Recently-added structural moves propagate cleanly.** (PI) axiom (scope-agent-identity → der-gain-sector-bridge → disc-additive-coordinate-forcing); BH-identity primary bound; monotone-operator lineage acknowledgment; Khasminskii stopping-time localization; structural Lipschitz-floor scope-exit.
- **Tier-stratification within segments is honest.** form-information-bottleneck explicitly distinguishes "exact applied theorem" from "robust-qualitative β(ρ,π) claim"; def-causal-information-yield distinguishes "definition exact" from "λ-weighted EIG-surrogacy heuristic"; result-mismatch-decomposition flags alignment assumption.
- **Sub-scope α/β partition** is the framework's clearest scope-honesty move at the persistence-machinery level.
- **Appendix-back-pointer convention** is consistently followed (7 main-section→appendix-A pointers observed in Section I; all are the standard result-in-body-proof-in-appendix pattern).
- **Math verification** (Lyapunov Props A.1, A.1S, A.2; Kalman Props B.1, B.2; gradient-equivalence Prop B.4; bias-variance decomposition cross-term) all check out.

The framework feels mature in its Section I core. Operational concerns exist (open work flagged honestly), but no math-error or load-bearing-claim-without-grounding has surfaced in the foundational backbone.

## Section F — Coverage statement

*Will populate when the audit completes.*

## Reading order tracking

- [x] AAD Section I rows 1-30 (in OUTLINE order; rows 1-10 batched in old discipline, rows 11-30 individually)
- [x] Cited Appendix A derivations: deriv-recursive-update, deriv-sector-condition, deriv-gain-sector, result-sector-persistence-template (read in-context per §4.2 exception)
- [ ] disc-compression-operations (Appendix A; cited from form-consolidation-dynamics; deferred as per-§4.2 candidate to read when other references trigger)
- [ ] AAD Section II segments (next: def-agent-spectrum)
- [ ] AAD Section III segments
- [ ] AAD Appendix A remaining segments (read in OUTLINE order or in-context per §4.2)
- [ ] AAD Appendix B (worked examples)
- [ ] TST segments
- [ ] 03-logogenic segments
- [ ] 04 (no segments)

## Strategic revision (per §4.5)

**Predictions check.** From 00-initial-predictions:
- ✓ Depends-drift pattern surfaced (F-A series).
- ✓ Status-label discipline mostly holds; tier-stratification is honest.
- ✓ (PI) axiom propagation lands cleanly across multiple segments.
- ✗ "Discussion claims that sound structural but aren't grounded" — mostly didn't materialize in Section I; the framework is honest in Discussion sections, with one or two hypothesis-grade claims clearly tier-marked.
- Pending: C-iv scope-route propagation check (Section III concern).

**Audit focus shift?** Not substantially. Continuing into Section II with same posture. Will specifically watch:
- Class 1/2/3 architectural classification propagation through Section II.
- Strategy-DAG content (especially given F-V3/F-V4 priming on strategic-composition).
- Forward references to recently-added segments (disc-compression-operations, deriv-detection-latency, etc.).
- Cross-component references into TST / logogenic-agents.

**Scratch-discipline check.** The 11 (now 13) prompt walk-through is producing substantive material. Reading appendices in-context per §4.2 exception is high-yield. The §4.4 cadence (one Read → one reflection → next Read) is holding. Math verification at-discretion is appropriate; not over-doing.

## Anti-bleed reminders

- F-V1 through F-V5 are *known* findings from MEMORY/TODO bleed. If I encounter them in src, log as confirmation in Section E, not as new findings.
- Gemini sub-agent failure mode (delegation of comprehension) is a known anti-pattern; not relevant since I haven't delegated reading.
- Several Section I observations may have been primed by CLAUDE.md / MEMORY.md / TODO.md content. Honest framing: this is not a clean de-novo audit; it's a partial-de-novo audit with priming-bleed acknowledged.

## Recently-added structural moves to track for cross-segment drift (per §5.2)

- C-iv scope route (`#scope-composite-agent`, 2026-04-23): propagation into `#scope-multi-agent` known-broken (F-V2). Watch other Section III segments.
- (PI) axiom (`#scope-agent-identity`, 2026-04-23): propagation lands cleanly in der-gain-sector-bridge ✓, disc-additive-coordinate-forcing (forward) expected, deriv-bias-bound (forward) expected, result-contraction-template (forward) expected.
- Sub-scope α₁/α₂/β partition (refined 2026-04-23): inherited by sector-persistence-template instances. Worth checking each instance verifies its sub-scope.
- BH-identity primary bound (2026-04-24): expected in `#deriv-strategy-cost-regret-bound` (forward).
- `#deriv-bias-bound` appendix (2026-04-24): expected in `#scope-observation-ambiguity-modulation` and `#result-section-ii-survival` (both in 03-logogenic-agents).
- DA2'-inc ≡ (CT2) at M=I structural transparency (2026-04-24): seen in result-sector-persistence-template ✓; expected in `#form-composition-closure` and `#result-contraction-template`.
- Three-mode `#der-loop-interventional-access` (2026-04-24): expected in der-loop-interventional-access (Section II).
- Consolidation timescale (2026-04-23): added to der-temporal-nesting's 5-level table ✓.

## Cadence checkpoint

30 main-section segments + 4 appendix-A = 34 reflections produced. Approximate runway remaining: substantial per Joseph's note that older tool calls are stripped from context, so I've stayed near 500k token utilization.

Section II + Section III + Appendix A remaining + Appendix B + TST + 03-logogenic = roughly 80+ more segments ahead. With current per-segment cadence (~5-10 minutes per reflection), this is feasible within remaining context budget.
