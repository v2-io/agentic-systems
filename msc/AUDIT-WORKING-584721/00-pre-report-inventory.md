# Pre-report Inventory

State at transition to §6.1 Phase-2 (per Joseph's redirection 2026-04-25). 51 reflections + 1 consolidated = ~54 segments covered first-hand.

## Coverage

- **AAD Section I rows 1-30:** all read first-hand. Rows 1-10 batched in old discipline (consolidated reflection 01); rows 11-30 individually.
- **Appendix A read in-context per §4.2 exception:** deriv-recursive-update, deriv-sector-condition, deriv-gain-sector, result-sector-persistence-template.
- **AAD Section II rows 1-26:** all read first-hand individually.
- **Section II rows 27-28 NOT read** (der-orient-cascade, disc-exploit-explore-deliberate).
- **AAD Section III: NOT read** (13 segments).
- **AAD Appendix A remaining: NOT read** (~20 segments including deriv-strategic-dynamics, deriv-graph-structure-uniqueness, deriv-discrete-sector-condition (F-V1 territory), result-contraction-template, the meta-segments disc-additive-coordinate-forcing / disc-identifiability-floor / disc-separability-pattern, deriv-bias-bound, etc.).
- **AAD Appendix B (worked examples): NOT read** (detail-operationalization, example-kalman, example-bandit, example-strategy, example-L1, worked-example-cam).
- **TST: NOT read** (~20 segments).
- **03-logogenic-agents: NOT read** (7 segments).
- **04-logozoetic-agents: NOT read** (no segments).

Coverage gaps to surface in report's "what I didn't read" section.

## Findings to triangulate against tracking docs

### F-A series (depends-list-incomplete vs Formal-Expression-uses)

Five instances, root-caused:

| # | Segment | Row | Symbol used | Missing dep | Notes |
|---|---------|-----|-------------|-------------|-------|
| F-A0 | def-observation-function | 2 | $a_{t-1}$ | def-action-transition | ROOT CAUSE |
| F-A1 | scope-adaptive-system | 4 | $\mathcal C_t$ | def-chronica | Independent |
| F-A2 | form-information-bottleneck | 11 | $a_{t:\infty}$ | def-action-transition | Propagated from F-A0 |
| F-A3 | def-model-sufficiency | 12 | $a_{t:\infty}$ | def-action-transition | Propagated from F-A0 |
| F-A4 | form-event-driven-dynamics | 14 | $M_{\tau^-}$ | form-agent-model | Independent |
| F-A5 | def-mismatch-signal | 17 | $a_{t-1}$ | def-action-transition | Propagated from F-A0 |
| F-A6 (folded) | result-mismatch-decomposition | 18 | $a_{t-1}$ | def-action-transition | Propagated; not separately enumerated |

**Recommended root-cause fix:** add `def-action-transition` to `def-observation-function`'s depends. Propagates transitively. Three independent drifts remain: F-A1 (scope-adaptive-system → def-chronica), F-A4 (form-event-driven-dynamics → form-agent-model). Plus F-A0 itself.

**Severity:** mechanical / editorial. **Confidence:** high (verified against frontmatter directly).

### F-B1 (low-confidence, candidate)

`form-event-driven-dynamics` Discussion mentions "Section IV gap (see the three-part tempo decomposition gap in `AAD-FULL.md`)." Both "Section IV" and `AAD-FULL.md` look stale post-component-split. Need to verify in §6.1 Phase-2 whether file exists.

**Severity:** stale doc reference; low. **Confidence:** medium-low pending verification.

### F-D series (Pinsker / BH-identity integration debt)

Two instances:

- **F-D1:** disc-ciy-unified-objective uses Pinsker bound; canonical deriv-strategy-cost-regret-bound (per CLAUDE-2.md priming) was upgraded 2026-04-24 to use BH-identity ($D_{KL} = -\log(1-TV)$ exact under deterministic π*) as primary bound.
- **F-D2:** form-strategy-complexity-cost retains Pinsker for IB-shape-alignment. Documents the trade-off (Epistemic Status discusses linear-vs-square-root) but doesn't mention BH-identity as the available sharper alternative. Mild integration debt.

**Severity:** editorial; both segments have valid bounds, just not the sharpest available. **Confidence:** medium (assumes CLAUDE-2.md priming is accurate about BH-identity replacing Pinsker in canonical segment).

### F-C series RETIRED

7 instances of appendix-back-pointer "critical findings" originally logged. Per §4.2 mid-session refinement (appendix-back-pointer exception), these are not findings — they're the standard "result-in-body, proof-in-appendix" convention. Recasting as Section E confirmation.

## Section D candidates (bigger-picture pondering)

Hypothesis-tier observations from sustained engagement:

1. **Six-mechanism convergence on shallow-plan preference.** Independent arguments compounding: (a) chain-confidence decay; (b) evidence starvation; (c) cognitive cost (DL); (d) strategic-tempo bottleneck; (e) identifiability degradation; (f) interaction-horizon compression (Miller). All multiplicative in depth.

2. **OKR/AAD operational mapping.** disc-credit-assignment-boundary's substantive domain instantiation — vanity metrics, too-many-KRs, lagging indicators, Goodhart all mapped to formal AAD quantities. One of the framework's strongest domain-bridging contributions.

3. **Signed-coupling pattern across template instantiations** (Section III organizing principle). Every effective $\rho_\xi$ in result-sector-persistence-template instantiations decomposes as "environmental disturbance + cross-agent contribution with sign encoding cooperative vs adversarial coupling." Six segments instantiate; pattern worth elevating as Section III meta-segment.

4. **Experience-discounting / forgetting / consolidation as architectural primitive.** Multiple convergent threads: schema-strategy-persistence's forgetting prerequisite; form-consolidation-dynamics regime; deriv-detection-latency's stability-induced-myopia (per CLAUDE-2.md priming). Cluster worth unifying.

5. **"Matched vs forced" coordinate distinction.** AAD has *forced* coordinates at chain (log-additive identity), divergence (reverse-KL), update (log-odds), metric (Fisher) layers. Lyapunov quadratic is *matched*, not forced. Disc-additive-coordinate-forcing handles this; could be elevated.

6. **Expected-bridge + stochastic-disturbance composition.** Bridge theorems hold in expected value; per-step noise enters as Model S disturbance. Two layers compose cleanly across multiple segments.

7. **Type/token distinction as meta-architectural commitment.** scope-agent-identity makes AAD token-level. Should be visible across logogenic-agents.

8. **Gain-collapse / stability-induced-myopia / detection-latency-blowup unification.** Multiple names for one agent pathology.

9. **Structural-adaptation-as-deliberation-with-massive-Δτ.** Recurring informal analogy. Either formalize or explicitly retire.

10. **Seven-attack discipline pattern.** deriv-recursive-update tests its own result against seven counterexamples. Other inevitability-core segments could adopt this discipline.

11. **Diagnostic-CIY four-axis extension** (explore / exploit / deliberate / diagnose). der-causal-insufficiency-detection adds "diagnose" as fourth axis. Not yet propagated to disc-exploit-explore-deliberate.

12. **CLAUDE.md / MEMORY.md auto-load priming as structural problem.** Already partially addressed mid-session by CLAUDE-2.md split and MEMORY/CHANGELOG migration. Worth surfacing as instructions-stress-test observation.

## Section E confirmations (calibration)

Strong evidence the framework's discipline holds across what I read first-hand:

- **Inevitability-core segments live up to advertising.** der-recursive-update / deriv-recursive-update; result-mismatch-decomposition; result-persistence-condition; result-sector-condition-stability; der-gain-sector-bridge — all status:exact or robust-qualitative with clean derivations.
- **Recently-added structural moves propagate cleanly.** (PI) axiom (scope-agent-identity → der-gain-sector-bridge → others); BH-identity primary bound (per priming); monotone-operator lineage; Khasminskii stopping-time localization; structural Lipschitz-floor scope-exit; composition-level class inheritance from C-iv (in der-directed-separation); three-mode der-loop-interventional-access; consolidation timescale in der-temporal-nesting.
- **Tier-stratification within segments is honest** across many segments. form-information-bottleneck distinguishes "exact applied theorem" from "robust-qualitative β(ρ,π) claim"; def-causal-information-yield distinguishes "definition exact" from "λ-weighted EIG-surrogacy heuristic"; result-mismatch-decomposition flags alignment assumption.
- **Sub-scope α/β partition** is the framework's clearest scope-honesty move at the persistence machinery level.
- **Appendix-back-pointer convention** consistently followed (7 instances confirmed in Section I and II main-section→Appendix-A pointers).
- **Math verification spot-checks pass:** Lyapunov Props A.1, A.1S, A.2 (deriv-sector-condition); Kalman Props B.1, B.2 (deriv-gain-sector); gradient-equivalence Prop B.4 (deriv-gain-sector); bias-variance decomposition cross-term (result-mismatch-decomposition); strict-prerequisite L0 example numbers (def-strategy-dag, 0.877 vs 0.776); Pinsker derivation (form-strategy-complexity-cost); depth-bound formula (form-strategy-complexity-cost). All check out.
- **F1 strengthening** (der-causal-insufficiency-detection): converted soft observation into sharp no-go theorem with explicit construction and five-route boundary. CLAUDE-2.md priming on this matched the segment.
- **OKR/AAD operational mapping** (disc-credit-assignment-boundary): substantive domain bridging.
- **Honest-credit-to-broader-lineage** discipline (der-loop-interventional-access cites Friston, Wiener, Conant-Ashby with three AAD-distinctive moves; deriv-sector-condition cites Rockafellar / Bauschke-Combettes monotone-operator lineage with five distinctives). Strong scope-honesty.
- **Pearl-blanket vs Friston-blanket positioning** (der-directed-separation): adopts conditional-independence; refuses metaphysical reading; admits Class 2 scope exit.

## Triangulation targets for §6.1 Phase-2

To read next:

1. `TODO.md` "Active — Pending Findings" 2026-04-25 batch (F-V1 through F-V5 plus P-V1, P-V2, P-V3 per priming) — verify my F-A / F-B / F-D series aren't subsets/duplicates.
2. `PROPOSALS.md` — verify my Section D candidates aren't already in the proposal portfolio.
3. `msc/pending-findings-2026-04-25.md` — most recent prior findings batch.
4. `msc/pending-findings-2026-04-22.md` and `pending-findings-2026-04-23.md` — prior batches; some F-V findings re-surfaced as F-V3↔F8.
5. `msc/architectural-proposals-*.md` — for Section D triangulation.

Each new finding I report must survive: "is this still real in current src text?" + "is this already known?"
