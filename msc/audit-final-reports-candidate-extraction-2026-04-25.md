# Audit Final Reports — Candidate Local Fixes (2026-04-25 extraction)

**Sources:**
- `msc/AUDIT-WORKING-584721/FINAL-2026-04-25.md` (Opus 4.7 1M, partial AAD §I + §II rows 1–26 + 4 Appendix-A reads-in-context)
- `msc/AUDIT-WORKING-613842/FINAL-2026-04-25.md` (substantial §I/§II + §III composition + targeted logogenic + targeted TST)
- `msc/AUDIT-WORKING-738192/AUDIT-FINAL-738192.md` (Gemini CLI, AAD §I/§II/§III)
- `msc/AUDIT-WORKING-742613/FINAL-2026-04-25.md` + `SUPPLEMENT-PHASE-2-TRIAGE.md` (Codex, partial AAD §I)
- `msc/AUDIT-WORKING-849201/000-FINAL-AUDIT-REPORT.md` (Sections I+II)
- `msc/AUDIT-WORKING-849201/000-FINAL-AUDIT-REPORT-SEC-III.md`
- `msc/AUDIT-WORKING-849201/000-FINAL-AUDIT-REPORT-TST.md`
- `msc/AUDIT-WORKING-849201/000-FINAL-AUDIT-REPORT-LOGOGENIC.md`

**Cross-referenced against:** `TODO.md` (Active — Pending Findings: 2026-04-25 F-V/P-V batch + F8 + 2026-04-22 F1–F15 + 2026-04-23 F22–F31), `PROPOSALS.md` §A–§G (especially Bundle 1, Bundle 2, §B/§C/§G membership, SP-21), `msc/pending-findings-2026-04-25.md`.

**Author posture:** triage agent, did not consult CLAUDE-2.md; did not modify segments/OUTLINE/TODO/CHANGELOG/PROPOSALS. Relied on first-hand reading of all 8 final reports plus current `TODO.md` and `PROPOSALS.md` only for cross-referencing.

---

## §A. High-confidence local independent fixes (NEW — not in TODO)

These meet all four criteria: local, independent, high-confidence, not in TODO/PROPOSALS. Most are presentational/editorial; none requires architectural decision or strengthening spike.

### AF-1: Score-function mismatch sign reversal in `#def-mismatch-signal`

- **Source audit(s):** 742613/F1 (high confidence, math direct). 742613 SUPPLEMENT-PHASE-2-TRIAGE classifies as "Likely new / not durably tracked" after first-hand `msc/`-search. 849201/17-def-mismatch-signal reflection praised the score-function formulation rather than flagging the sign — i.e., this was missed, not noted.
- **Segment(s):** `01-aad-core/src/def-mismatch-signal.md` (line 33).
- **Finding:** The segment defines $\tilde{\delta}_t = -\nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$ and prose claims this points "in the direction the model should move to increase the likelihood" and "coincides with $\delta_t$ up to scaling under Gaussian models." For Gaussian $o \sim \mathcal N(M, \sigma^2)$, $\nabla_M \log P = (o - M)/\sigma^2 = \delta/\sigma^2$. The segment's negative sign reverses the stated direction.
- **Fix:** Either remove the minus sign (define $\tilde{\delta}_t = \nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$) so prose and Gaussian-equivalence claim match; or keep the minus sign but rename / reframe the object as a negative-log-likelihood gradient (descent direction) and audit downstream usage. Codex's recommended cleaner repair: drop the minus sign.
- **Effort estimate:** ≤30 min.
- **Strengthen-before-soften posture:** Editorial sign-correction; no claim being weakened. Genuine math repair, not a soften.

### AF-2: Gradient-equivalence iff overstated in `#deriv-gain-sector` and `#der-gain-sector-bridge`

- **Source audit(s):** 742613/F3 (high confidence, math direct). SUPPLEMENT-PHASE-2-TRIAGE classifies as "Known distinction, unrepaired offender" — `#result-sector-persistence-template` lines 70–72 already correctly distinguish one-point sector from full two-point monotonicity, but `#deriv-gain-sector` (lines 127, 133, 157, 261) and `#der-gain-sector-bridge` retain "iff / equivalence" language.
- **Segment(s):** primary `01-aad-core/src/deriv-gain-sector.md` (Prop B.4, ~line 127ff); secondary `01-aad-core/src/der-gain-sector-bridge.md`.
- **Finding:** Prop B.4 claims "GA-3 holds with $(\alpha,R)$ iff $L$ is locally $(\alpha/\eta)$-strongly convex." The reverse direction proves only the $y = M^*$ instance of gradient monotonicity — that is one-point strong monotonicity / star-convex-like inwardness, not full local strong convexity. Codex's 1D counterexample $L'(x) = x(1 + \tfrac{1}{2}\sin(10x))$ satisfies the one-point sector condition but $L''(x)$ is negative on intervals.
- **Fix:** Replace "iff" with "Local strong convexity is sufficient for GA-3 / one-point sector. GA-3 itself is the weaker one-point condition. Full two-point / incremental monotonicity is needed only where composition or contraction arguments require it." Mirror the `#result-sector-persistence-template` framing already present.
- **Effort estimate:** 30–60 min (two segments; need to chase any downstream language that leaned on the iff).
- **Strengthen-before-soften posture:** Soften, but the audit considered strengthening: the spike trail (`msc/spike-jacobian-b1-strengthening.md`) and `#result-sector-persistence-template` already preserve the correct one-point-vs-two-point distinction. The strengthening to full two-point monotonicity would be wrong (the segment's intended claim is the one-point form). Genuine soften with documented strengthening rejection — OK to include.

### AF-3: Sub-secondary in `#deriv-gain-sector` — exponential-family natural-parameter sector overclaim

- **Source audit(s):** 742613/F3 secondary implication (line 173 cited).
- **Segment(s):** `01-aad-core/src/deriv-gain-sector.md` (~line 173).
- **Finding:** The segment treats exponential-family natural parameters as globally exact via $\lambda_{\min}(\text{Fisher})$. Pointwise Fisher PD does not imply uniform global lower bound. For Poisson natural parameter $\theta$, Fisher is $e^\theta$; $\inf_{\theta \in \mathbb R} e^\theta = 0$. Global sector constants need either compact / interior-bounded scope or an explicit uniform Fisher lower bound.
- **Fix:** Add a one-paragraph scope condition: "Global sector constants in this exponential-family setting require either parameter-domain compactness or an explicit uniform Fisher lower bound; for unbounded natural-parameter domains the sector is local rather than global." Cross-reference `#disc-identifiability-floor` if appropriate.
- **Effort estimate:** ≤30 min (one paragraph in one segment).
- **Strengthen-before-soften posture:** Genuine scope-honesty repair, not a softening of a substantive claim — the substantive claim is already true in compact-domain or uniform-lower-bound scope; the fix names the missing scope condition.

### AF-4: Action-selection result $a_t = \pi(M_t)$ exactness mismatch with later $\pi(M_t, G_t)$

- **Source audit(s):** 742613/F5 (medium-high confidence). SUPPLEMENT-PHASE-2-TRIAGE classifies as "Known supersession, integration debt" — `#form-complete-agent-state` line 36 already defines $a_t = \pi(M_t, G_t)$ and line 52 says `#der-action-selection` is superseded after the state lift. `#def-model-sufficiency` line 40 already uses $\pi(M_t, G_t)$. Integration debt only.
- **Segment(s):** `01-aad-core/src/der-action-selection.md` (lines 4, 19, 25, 29, 47).
- **Finding:** Frontmatter says `status: exact`; Formal Expression states $a_t = \pi(M_t)$; segment's own Discussion (line 47) admits the actuated-agent generalization is $\pi(M_t, G_t)$. The exact label fits Section I scope only when $G_t$ is fixed/absent/folded into $M_t$.
- **Fix:** Either (a) downgrade the Formal-Expression statement to $a_t = \pi(X_t)$ for complete action-relevant state $X_t$ with the Section-I instantiation $X_t = M_t$ explicit; or (b) keep $a_t = \pi(M_t)$ and add a one-sentence "superseded by complete-agent-state lift in `#form-complete-agent-state`" clause to the Formal Expression / Epistemic Status (not just Discussion). Codex's recommended phrasing in SUPPLEMENT.
- **Effort estimate:** ≤30 min.
- **Strengthen-before-soften posture:** Editorial integration-debt repair; the broader theory already has the stronger statement, and the segment Discussion already acknowledges it. Lifting the acknowledgement into Formal Expression / Epistemic Status is presentational, not a softening of substance.

### AF-5: Model-sufficiency $S(M_t)$ denominator-zero edge case

- **Source audit(s):** 742613/F8 (medium confidence). SUPPLEMENT-PHASE-2-TRIAGE: "Likely new local well-definedness gap" — no durable tracking found.
- **Segment(s):** `01-aad-core/src/def-model-sufficiency.md` (lines 19, 23, 25–28); downstream consumers `01-aad-core/src/def-model-class-fitness.md`, `01-aad-core/src/result-structural-adaptation-necessity.md` (no edits required there if the convention lands cleanly upstream).
- **Finding:** $S(M_t) = I(M_t; o_{t+1:\infty} \mid a_{t:\infty}) / I(\mathcal C_t; o_{t+1:\infty} \mid a_{t:\infty})$ has the total-predictive-information of the chronica in the denominator. In saturated-noise / iid / prediction-vacuous regimes the denominator is zero and $S(M_t)$ is undefined; boundary values for $S=1, S=0$ at lines 25–28 are stated unconditionally.
- **Fix:** Add a well-definedness clause to the Formal Expression / Epistemic Status: "$S(M_t)$ is defined when $I(\mathcal C_t; o_{t+1:\infty} \mid a_{t:\infty}) > 0$. When the denominator is 0, predictive sufficiency is vacuous; the convention is that $S$ is undefined / not applicable rather than $S = 1$ by limit." (The undefined convention is cleaner because downstream `#def-model-class-fitness` / `#result-structural-adaptation-necessity` results assume non-vacuous predictive information.)
- **Effort estimate:** ≤30 min.
- **Strengthen-before-soften posture:** Pure well-definedness repair. No softening — just naming a missing scope condition that was always implicit.

### AF-6: Depends-list missing `def-action-transition` (root cause + 4 propagated instances)

- **Source audit(s):** 584721/F-A (high confidence; mechanical violation of FORMAT.md Gate 1, verifiable from frontmatter alone). Cross-audit: 742613/F6 surfaces same class of issues from a different entry point and SUPPLEMENT classifies as "Tooling gap + prior-noted fragments."
- **Segment(s):**
  - F-A0 root cause: `01-aad-core/src/def-observation-function.md` — Formal Expression uses $a_{t-1}$, depends list lacks `def-action-transition`.
  - F-A2: `01-aad-core/src/form-information-bottleneck.md` — uses $a_{t:\infty}$.
  - F-A3: `01-aad-core/src/def-model-sufficiency.md` — uses $a_{t:\infty}$.
  - F-A5: `01-aad-core/src/def-mismatch-signal.md` — uses $a_{t-1}$.
  - F-A6: `01-aad-core/src/result-mismatch-decomposition.md` — uses $a_{t-1}$.
- **Finding:** Five segments use action symbols in Formal Expression without declaring `def-action-transition` in `depends:`. F-A0 is at `stage: deps-verified`; F-A1/F-A4/etc. are at varying stages. Mechanical Gate-1 violations.
- **Fix:** Add `def-action-transition` to each of the five segments' `depends:` field. (584721 notes that fixing F-A0 may cover F-A2/F-A3/F-A5/F-A6 if the dependency closure is transitive via `form-agent-model`/`def-observation-function`; verify with `bin/lint-outline` after fix.)
- **Effort estimate:** ≤30 min for all five (frontmatter touches only). Re-run `bin/lint-outline` after.
- **Strengthen-before-soften posture:** Pure mechanical bookkeeping. No claim being weakened.

### AF-7: Depends-list missing `def-chronica` in `#scope-adaptive-system`

- **Source audit(s):** 584721/F-A1 (independent from F-A0). 742613/F6 surfaces the same `scope-adaptive-system → def-chronica` body-level dependency miss as part of "early Section I canonical order is not a clean dependency linearization." Cross-audit convergence.
- **Segment(s):** `01-aad-core/src/scope-adaptive-system.md` (line 19 uses $\mathcal C_t$).
- **Finding:** Formal Expression / Discussion uses $\mathcal C_t$ without declaring `def-chronica` in `depends:`. Mechanical Gate-1 violation; lint-clean only because chronica is declared in adjacent transitive deps.
- **Fix:** Add `def-chronica` to `depends:` field.
- **Effort estimate:** ≤30 min (single frontmatter line).
- **Strengthen-before-soften posture:** Pure mechanical bookkeeping.

### AF-8: Depends-list missing `form-agent-model` in `#form-event-driven-dynamics`

- **Source audit(s):** 584721/F-A4 (independent from F-A0). 742613/F6 also surfaces `form-event-driven-dynamics` formal-expression uses $M_{\tau^-}$ without declaring `form-agent-model`. Cross-audit convergence.
- **Segment(s):** `01-aad-core/src/form-event-driven-dynamics.md` (lines 32–36, conditioned on $M_{\tau^-}$).
- **Finding:** Same Gate-1 pattern: Formal Expression uses $M_{\tau^-}$ without declaring `form-agent-model` in `depends:`.
- **Fix:** Add `form-agent-model` to `depends:` field.
- **Effort estimate:** ≤30 min.
- **Strengthen-before-soften posture:** Pure mechanical bookkeeping.

### AF-9: Wrong slug links `discrete-sector-condition.md` (should be `deriv-discrete-sector-condition.md`)

- **Source audit(s):** 742613/F6 (high confidence; specific). SUPPLEMENT classifies as "tooling gap" — `bin/lint-outline` doesn't body-scan, so this slipped through.
- **Segment(s):** `01-aad-core/src/hyp-mismatch-dynamics.md` (line 54), `01-aad-core/src/der-gain-sector-bridge.md` (line 127).
- **Finding:** Both segments cite `#deriv-discrete-sector-condition` for the formal justification of the fluid-limit framing. Both link to the wrong slug `discrete-sector-condition.md`. The actual segment is `deriv-discrete-sector-condition.md`.
- **Fix:** Rename links in both segments. Optionally also `bin/lint-outline`-level enhancement to body-scan slug links — but that's tooling, not a local fix.
- **Effort estimate:** ≤30 min.
- **Strengthen-before-soften posture:** Pure link correction.

### AF-10: `#form-consolidation-dynamics` undeclared upstream dependencies in Formal Expression

- **Source audit(s):** 742613/F6 (high confidence; specific lines cited).
- **Segment(s):** `01-aad-core/src/form-consolidation-dynamics.md` (lines 60–62 and 76).
- **Finding:** Formal Expression uses lower-bound from `#schema-strategy-persistence` (line 60–62) and references `#form-structural-change-as-parametric-limit` (line 76) without declaring either in `depends:`. Independent of the `disc-compression-operations` backmatter case (which Codex acknowledges as legitimate appendix-back-pointer territory).
- **Fix:** Add `schema-strategy-persistence` and `form-structural-change-as-parametric-limit` to `depends:` field; verify dependency-graph orderings via `bin/lint-outline`.
- **Effort estimate:** ≤30 min.
- **Strengthen-before-soften posture:** Pure mechanical bookkeeping.

### AF-11: BH-identity propagation gap in `#disc-ciy-unified-objective`

- **Source audit(s):** 584721/F-D1 (medium-high confidence; depends on CLAUDE-2 priming about BH-identity primary). The 2026-04-24 Tier-1 BH-identity landing is logged in TODO §"2026-04-24 Gemini pressure-point cycle — Tier 1 landing"; the upgrade is real.
- **Segment(s):** `01-aad-core/src/disc-ciy-unified-objective.md` (Discussion §"Regret-bound connection to the strategy-cost objective").
- **Finding:** Discussion paragraph cites Pinsker's inequality for the strategy-induced regret bound: $R(Q_{\Sigma_t}) \leq V_{\max}\sqrt{\tfrac{1}{2}D_{KL}(\pi^* \Vert Q_{\Sigma_t})}$. Doesn't reference the strictly-sharper Bretagnolle-Huber identity ($D_{KL}(\pi^* \Vert Q) = -\log(1 - TV)$ exact under deterministic $\pi^*$) that landed as primary in `#deriv-strategy-cost-regret-bound` 2026-04-24.
- **Fix:** One-paragraph Discussion addition: under deterministic $\pi^*$ (the standard regret-bound scope), Bretagnolle-Huber gives the sharper exact form; cross-reference `#deriv-strategy-cost-regret-bound` §4. Retain Pinsker for general / non-deterministic-$\pi^*$ scope.
- **Effort estimate:** 30–60 min (verify BH-identity primary status in `#deriv-strategy-cost-regret-bound` first; then add Discussion paragraph).
- **Strengthen-before-soften posture:** Editorial propagation of an existing strengthening; no claim being weakened. Pure integration debt.

### AF-12: BH-identity cross-reference missing in `#form-strategy-complexity-cost`

- **Source audit(s):** 584721/F-D2 (medium-high confidence). Audit notes the segment's Epistemic Status already discusses linear-vs-square-root-in-KL trade-off and explains why Pinsker is retained for IB-shape alignment, but doesn't reference BH-identity.
- **Segment(s):** `01-aad-core/src/form-strategy-complexity-cost.md` (Epistemic Status).
- **Finding:** Segment is aware of the trade-off and explains the Pinsker retention reason, but doesn't cite BH-identity as the available sharper alternative for the deterministic-$\pi^*$ case.
- **Fix:** One-sentence cross-reference: "For the deterministic-$\pi^*$ case, the sharper Bretagnolle-Huber identity holds (see `#deriv-strategy-cost-regret-bound` §4). Pinsker is retained here for IB-shape alignment under general $\pi^*$."
- **Effort estimate:** ≤30 min.
- **Strengthen-before-soften posture:** Editorial cross-reference; segment is already self-aware about the trade-off.

### AF-13: Stale `AAD-FULL.md` / "Section IV" reference in `#form-event-driven-dynamics`

- **Source audit(s):** 584721/F-B1 (medium-low confidence; first-hand verification deferred).
- **Segment(s):** `01-aad-core/src/form-event-driven-dynamics.md` Discussion §"Software-specific channels".
- **Finding:** Discussion closes with: *"This decomposition is a Section IV gap (see the three-part tempo decomposition gap in `AAD-FULL.md`)."* "Section IV" was the original location of TST before the 2026-03 restructure to `02-tst-core/`; `AAD-FULL.md` is not in current root.
- **Fix:** Verify `AAD-FULL.md` does not exist (`ls $REPO/AAD-FULL.md` should return non-existent). Update reference to the current TST location of the three-part tempo gap (likely `02-tst-core/OUTLINE.md` Section S — auditor flags "Developer tempo as $\mathcal T_{\text{obs}} + \mathcal T_{\text{explore}} + \mathcal T_{\text{probe}}$" GAP).
- **Effort estimate:** ≤30 min.
- **Strengthen-before-soften posture:** Doc-rot cleanup; no claim being weakened.

### AF-14: Spike-citations outside Working Notes (FORMAT.md violation)

- **Source audit(s):** 738192 implicit; 742613 "Other Observations" (explicit, lines 343–348). Identifies `deriv-sector-condition`, `der-gain-sector-bridge`, `deriv-gain-sector`, `result-structural-adaptation-necessity` as carrying `msc/spike-*` references outside Working Notes.
- **Segment(s):** `01-aad-core/src/deriv-sector-condition.md`, `01-aad-core/src/der-gain-sector-bridge.md`, `01-aad-core/src/deriv-gain-sector.md`, `01-aad-core/src/result-structural-adaptation-necessity.md`.
- **Finding:** FORMAT.md and `feedback_spike_references_only_in_working_notes.md` say spike citations belong only in Working Notes (and only for unfinished follow-on work — not as backing for promoted content). Multiple promoted segments still carry spike citations in Discussion / Epistemic Status / Formal-Expression-adjacent text.
- **Fix:** Per segment: identify spike references; move to Working Notes (or remove if the spike content is already in-segment); ensure no Formal-Expression / Epistemic-Status content rests on a spike pointer rather than on segment content. Each segment is independent.
- **Effort estimate:** 30–60 min per segment if grep-then-relocate is mechanical; 60–90 min combined for the four if working in parallel.
- **Strengthen-before-soften posture:** Pure FORMAT.md compliance. No claim weakening.

### AF-15: TST `#hyp-causal-discovery-from-git` confounder language already in TODO P-V3 — note

- **Source audit(s):** 849201/000-FINAL-AUDIT-REPORT-TST/Finding 2 echoes the same concern.
- **Status:** **Already in TODO** as P-V3 (landed in commit `a6b61fb` per Archive entry). Surfacing here for completeness; **DO NOT include in dispatch list.** Listed in §B below.

---

## §B. Findings already in TODO (extraction confirmation)

The prior 2026-04-25 extraction captured the following audit findings; cross-audit convergence with the eight final reports is high.

| Finding (audit-side description) | Source audit(s) | Existing TODO/PROPOSALS ID | Notes |
|---|---|---|---|
| Discrete-to-continuous Model S variance gap mis-stated | 742613 §F2 (different framing — see §C below for the live unresolved piece) | F-V1 (RESOLVED, commit `a6b61fb`) | F-V1 covered the asymptotic-scaling math correction. The deeper Markov-tail-vs-ever-exit error in 742613/F2 is **NOT subsumed**; see §C. |
| `scope-multi-agent` excludes adversarial; `scope-composite-agent` admits via C-iv | 613842 §F3 partial | F-V2 (RESOLVED, commit `a6b61fb`) | Editorial drift around C-iv route. |
| C-iii mutual-benefit composites lack coherent $G_c$ | 613842 §F3 (full integration story); 742613 SUPPLEMENT references F8/F-V3 | F-V3 ≈ F8 (Active — Path A vs SP-21 routing decision deferred to Joseph) | SP-21 in PROPOSALS.md §G. |
| Sign error in zero-sum worked example | (auditors absorbed prior knowledge of this issue) | F-V4 (Active follow-up review) | F-V4 fix landed; follow-up review still queued. |
| TST `scope-developer-agent` doesn't carry Class 2 caveats | 849201/LOGOGENIC consistent in spirit; 738192 doesn't flag directly | F-V5 (RESOLVED, commit `a6b61fb`) | Cross-component integration done. |
| "Not a discretization artifact" framing in `result-adversarial-tempo-advantage` | (no explicit re-surfacing in 8 final reports) | P-V1 (RESOLVED, commit `a6b61fb`) | — |
| "Linear projections of linear dynamics are exact" in `result-unity-closure-mapping` | (no explicit re-surfacing) | P-V2 (RESOLVED, commit `a6b61fb`) | — |
| `hyp-causal-discovery-from-git` "causal direction for free" overstates | 849201/TST §Finding 2 | P-V3 (RESOLVED, commit `a6b61fb`) | — |
| Adaptive tempo $\mathcal T = \sum \nu^{(k)} \eta^{(k)*}$ exactness vs prose caveat | 613842 §F1 (high); 742613 §F4 (high); 849201 §"Bigger-picture pondering" Observation 6 | F27 (already-caveated; retained for visibility); PROPOSALS.md notes "independence profile" SP-16 territory | Three audits independently flag — strong cross-audit convergence — but the framework's source already carries the caveats in `disc-independence-audit`, `result-persistence-condition`, `der-team-persistence`, `der-tempo-composition`. The remaining edit is a `def-adaptive-tempo` status/name change, which is a small editorial repair. **See §E borderline.** |
| Region-aware Prop A.1S over-compression in summaries | 613842 §F2 (high); convergent with the 742613/F2 stochastic-persistence concern | F-V1 partial (the math correction) + the broader "summary compression" critique | 613842/F2 is the *non-math, summary-compression* half of the Model S story; 742613/F2 is the *math-bound-vs-ever-exit* half. F-V1 closed the asymptotic-scaling math but did not address either of these two distinct concerns. **See §C and §E.** |
| C-iv strategic-composite route only partially integrated | 613842 §F3 | F-V2 (resolved) + F-V3/F8 (active) + SP-21 in PROPOSALS.md §G | Triply tracked. |
| Static / dynamics survival in Class 2 (logogenic) | 849201/LOGOGENIC §Finding 1, §Finding 2; consistent with 849201/TST §Finding 1 (100% turnover) | Already segmented as `result-section-ii-survival`, `obs-context-turnover`, `def-coupled-update-dynamics`, `scope-observation-ambiguity-modulation` | Audit consensus is the framework's existing logogenic story is correct; not a finding. |
| Section II "16/24 exact survival" headline compression | 849201 §Phase 2 confirmation, no flagging | F23 (Open; subsumed by C-BP1 three-layer separation) | — |

The prior extraction was substantially complete on the *F-V/P-V batch* targets. What it missed cluster in §A above (depends-list discipline; BH-identity propagation; doc-rot reference; spike-citation hygiene; isolated math/scope errors deeper in `#deriv-gain-sector` / `#der-action-selection` / `#def-mismatch-signal` / `#def-model-sufficiency`).

---

## §C. Strengthening-needed (NOT local fixes — escalate)

These are findings the audits propose softening repairs for, where the strengthening question hasn't been engaged. Per CLAUDE.md "Strengthen before softening", these need scoping spikes — not fix-agent dispatch.

### SN-1: Model S local stochastic persistence — Markov-tail-vs-ever-exit error

- **Source audit(s):** 742613/F2 (high confidence; math direct). 742613 SUPPLEMENT classifies as "Partly represented, not correctly integrated."
- **Segment(s):** `01-aad-core/src/deriv-sector-condition.md` (lines 180, 194, 242, 253, 270, 282); `01-aad-core/src/result-sector-persistence-template.md` (lines 47, 90); `01-aad-core/src/result-persistence-condition.md`.
- **Finding (substantive):** The current source converts a Markov-fixed-time / stationary tail bound $P(\|\delta(t)\| > R)$ into an infinite-horizon non-exit probability $P(\tau_R < \infty)$. For a non-degenerate OU process $d\delta = -\alpha\delta\,dt + \sigma_w\,dW_t$ on a finite ball, $P(\tau_R < \infty) = 1$ regardless of $\alpha R^2 / \sigma_w^2$. The asymptotic-scaling claim (3/2 in fluid limit) is correct; the *infinite-horizon non-exit* claim is wrong as stated.
- **Why this is strengthening territory, not local:**
  - The audit proposes softening (state only the stopped bound; require global sector for unstopped mean-square; or use finite-horizon exit probability).
  - The strengthening question wasn't engaged: *can the framework derive a stronger statement than the stopped bound?* Bounded stochastic disturbances + global sector + exit-by-RMS-deviation + invariant-domain hypotheses are candidates that haven't been worked through.
  - The downstream propagation (per 613842/F2) is its own integration question — even after the math is settled, the summary segments need their own pass.
- **Recommended next move:** Scoping spike (1 session) to attempt strengthening before falling back to softening. Document the strengthening attempt (or its honest failure) before any segment edits.
- **NOT a fix-agent dispatch candidate.**

### SN-2: Information-Bottleneck $\beta$ vs environment volatility $\rho$ conflation

- **Source audit(s):** 738192/Finding 1 (substantive critique).
- **Segment(s):** `01-aad-core/src/form-information-bottleneck.md` Discussion §"Dependence on volatility".
- **Finding (substantive):** Segment claims $\beta$ should be lowered when $\rho$ is high (volatile environments → favor compression). 738192 argues this is a double-counting error: $\beta$ dictates the agent's *preference* trade-off, but $P(\mathcal C_t, o_{t+1:\infty})$ already changes with $\rho$ (past-future MI decreases natively); the optimal $\phi^*$ will discard old information at constant $\beta$. Adjusting $\beta$ should reflect changes in *cost-of-memory-vs-accuracy*, not environment volatility.
- **Why this is strengthening territory, not local:**
  - Audit's framing is critique-only; doesn't engage whether the segment's claim survives under tightened conditions (e.g., when $\beta$ is the agent's hyperparameter for a fixed compression cost and $\rho$ shifts the IB Pareto frontier — there can be a derived relation between optimal $\beta$ and $\rho$ even though they are conceptually distinct).
  - This is a substantive-content claim, not a presentational mismatch. Framework's response could be (a) keep the claim and derive the $\beta(\rho)$ relation as a corollary; (b) downgrade to "the optimal $\phi^*$ shifts under $\rho$ with $\beta$ held fixed" (which is what the auditor argues); (c) something else.
  - Segment's own Epistemic Status acknowledges $\beta(\rho, \pi)$ dependence is *robust-qualitative* tier (per 584721 §E.3), so the claim is *not* exact tier — but the prose still presents it as an operational dependence. Need a strengthening attempt before softening.
- **Recommended next move:** Scoping spike to derive (or refute the existence of) an explicit $\beta^*(\rho)$ relation under stated coupling conditions. Document the result; revise Discussion accordingly.
- **NOT a fix-agent dispatch candidate.**

### SN-3: `git checkout` as Pearl Level 3 counterfactual — overclaim

- **Source audit(s):** 738192/Finding 2 (substantive critique).
- **Segment(s):** `01-aad-core/src/def-pearl-causal-hierarchy.md` (and downstream `02-tst-core/src/obs-software-epistemic-properties.md` / `02-tst-core/src/scope-developer-agent.md` if propagated).
- **Finding (substantive):** Segment claims `git checkout` provides L3 access "with ground-truth verification — the agent can literally execute the counterfactual." 738192 argues `git checkout` resets codebase state but not external environment / developer mind / external dependencies / time; it's a highly-reproducible L2 intervention, not a true L3 counterfactual. Approaches L3 only under deterministic / stateless / no-evaluator-evolution conditions.
- **Why this is strengthening territory, not local:**
  - The audit doesn't engage whether the framework has scope conditions under which the L3 claim survives (e.g., pure-function tests with reproducible build environments + deterministic test suites + agent-state-frozen-or-irrelevant). C-BP3's TST-as-calibration-laboratory framing already names environment-dependency relaxations as transfer assumptions.
  - The fix could be either a full L3 → L2 demotion (softening) or a scoped L3 claim ("under reproducible-build + deterministic-test + agent-state-irrelevance, `git checkout` provides L3 access") (strengthening with scope-honesty). The strengthening hasn't been attempted.
- **Recommended next move:** Scoping spike — does the L3 claim survive under explicit operational scope conditions? Or is it only ever an L2 claim with high reproducibility? Document attempt before edit.
- **NOT a fix-agent dispatch candidate.**

### SN-4: Opacity-Gain Tension in `#def-observation-function` vs `#emp-update-gain`

- **Source audit(s):** 849201/000-FINAL Finding 1. 849201 itself flags as "Known but unfixed" via cross-reference to 742613/02-def-observation-function reflection.
- **Segment(s):** `01-aad-core/src/def-observation-function.md`, `01-aad-core/src/emp-update-gain.md`.
- **Finding (substantive):** `#def-observation-function` strictly states the agent does not know $\varepsilon_t$'s distribution. `#emp-update-gain` defines optimal gain $\eta^* = U_M / (U_M + U_o)$. If the agent cannot know $U_o$ (= var $\varepsilon_t$), $\eta^*$ is uncomputable inside the agent.
- **Why this is strengthening territory, not local:**
  - 849201 itself flags this as needing either a bridging hypothesis (how is $U_o$ empirically estimated by the agent without violating opacity?) or a softening (relax the opacity axiom).
  - The strengthening attempt (derive the bridge from existing AAD machinery — adaptive filtering as part of $g_M$ or estimation via residual variance under Gaussian assumptions) hasn't been logged in `msc/`.
  - The softening attempt is also non-local: weakening opacity has cascading consequences across `def-observation-function` / `emp-update-gain` / Kalman example / sector-condition derivation.
- **Recommended next move:** Scoping spike (1 session). Two questions: (a) can $U_o$ be derived from observable residual statistics under standard regularity; (b) what AAD scope condition gates the bridge? Document attempt; segment edits afterward.
- **NOT a fix-agent dispatch candidate.**

---

## §D. Architectural / multi-cycle (NOT local)

These are framework-face / multi-segment / decision-pending findings that map to existing architectural proposals or surface candidate proposals.

### AR-1: 613842/F2 — Region-aware Prop A.1S summary-compression propagation depth

- **Maps to:** PROPOSALS.md §B/C — would land within Bundle 1 (framework-face reframe) OR as part of the post-BH-identity Tier-2 cleanup. Cross-cutting through `result-sector-persistence-template`, `result-sector-condition-stability`, `result-persistence-condition`. Scope-honesty drift, not a math error.
- **Why not §A:** Three load-bearing summary segments would need coordinated propagation pass; coordinating with C-BP1 (claim-level statuses) makes more sense than three independent edits. Touches Bundle 1 territory.

### AR-2: 613842/F3 — C-iv strategic-composite integration depth

- **Maps to:** Already at SP-21 in PROPOSALS.md §G + F-V3/F8 active routing decision. Triply tracked. **Confirms** that audit re-surfaces SP-21 motivation.
- **Why not §A:** Architectural; awaits Joseph routing decision.

### AR-3: 742613/F7 — Passive observers vs action-coupled primitives

- **Source audit(s):** 742613/F7 (medium-high). 584721 partial (cross-references in 584721/01-section-i-leaves.md per SUPPLEMENT). 849201/000-FINAL Phase 2 §"Epistemic Anchor" is consistent in spirit (the framework wants $P(o \mid do(a))$ rather than $P(\Omega \mid do(a))$ — but doesn't flag the primitive-definition mismatch).
- **Segment(s):** `def-agent-environment.md`, `def-action-transition.md`, `post-causal-structure.md`, `scope-adaptive-system.md`, `def-agent-spectrum.md`.
- **Finding:** AAD wants passive observers (passive Bayesian learners, passive trackers) inside the adaptive-system primitive scope, but the foundational definition of "agent" and "actions affect $\Omega$" excludes them. Repair = neutral primitive vocabulary + agency-scope reservation for interventional channels.
- **Why not §A:** Touches 5+ foundational segments coordinated; this is a primitive-vocabulary cleanup that needs Joseph's posture (introduce neutral "adaptive system / system-environment coupling" primitive vs. degenerate-action-channel framing). Maps to either Bundle 1 framework-face territory or to a new "scope-lattice" segment per O-BP8.
- **Maps to:** O-BP8 (scope lattice — Bundle 1) — closes F30 / F16 in the audit-batch dependency chain. Worth flagging in PROPOSALS.md as an explicit inclusion in O-BP8's scope.

### AR-4: 742613/F6 — Body-level dependency / link / canonicalization issues beyond the AF-6/7/8/9/10 set

- **Source audit(s):** 742613/F6 SUPPLEMENT classifies as "Tooling gap + prior-noted fragments." `bin/lint-outline` reports clean (0 ordering, 0 missing) because it only checks frontmatter `depends:`, not body-level slug usage / wrong-link strings.
- **Why not §A:** The specific instances I extracted to §A (AF-6 through AF-10) are the local independent ones. The remaining of F6 ("post-composition-consistency imports Section III machinery before introduction" at lines 14, 30–34, 50–56) is a foundational-postulate-vs-Section-III-content structural issue, not a local fix. Separately, the recommendation to extend `bin/lint-outline` with body-level scan is a tooling proposal.
- **Maps to:** Tooling enhancement (PROPOSALS.md candidate; not yet logged). Worth a one-line entry: "extend `bin/lint-outline` to body-level slug-link scan + canonical-symbol-coverage check". Effort: ~1 session for a focused script extension.

### AR-5: 584721 §A.2 — CLAUDE.md / MEMORY.md auto-load priming structural concern

- **Source audit(s):** 584721 §A.2 (instructions stress-test). Mid-session work resolved it (CLAUDE.md / CLAUDE-2.md split, MEMORY migration to CHANGELOG/LOG).
- **Why not §A:** Already done in-session by the audit. Surfaced here for completeness as instructions/de-novo-audit-process artifact rather than framework-content fix.

---

## §E. Borderline / orchestrator-judgment

### BL-1: `#def-adaptive-tempo` status `exact` vs prose caveat

- **Cross-audit convergence:** Three audits flag (613842/F1; 742613/F4; 849201 Observation 6) — high signal.
- **Why borderline:** The remaining work is a single segment frontmatter edit (status: exact → conditional) plus a one-line distinction between $\mathcal T$ (effective) and $\mathcal T_{\text{add}}$ (additive nominal). Editorial. **But:** the choice between "rename the additive scalar as upper-bound surrogate" vs "make exactness conditional on channel-independence and isotropy" vs "introduce $\mathcal T_{\text{add}}$ alongside effective $\mathcal T$" is a Joseph-judgment naming decision (exactly the kind of subject-noun decision the naming-pilot framework wants to handle deliberately), not a mechanical fix. Already on the F27 / SP-16 (independence-profile) track.
- **Recommendation:** Hold for Bundle 1 framework-face reframe (PROPOSALS.md §B.1); do not dispatch as parallel fix.

### BL-2: 613842/F2 — Region-aware Prop A.1S summary-compression

- **Why borderline:** Three load-bearing summary segments would each need a coordinated pass. Each individual edit is small and editorial, but the coherent framing of region-awareness → summary needs the same hand. Could be dispatched as a single agent task ("propagate Prop A.1S region-awareness language into the three summary segments") rather than three parallel ones.
- **Recommendation:** Wait until C-BP1 (claim-level statuses) lands or wait for an explicit consolidation agent. Not parallel-dispatch material.

### BL-3: 738192/Finding 1 (IB $\beta$ vs $\rho$) — escalated to §C, but very thin

- **Why borderline:** Audit is a single-segment Discussion concern. The strengthening question (§C/SN-2) might collapse to "rephrase the prose to say the optimal $\phi^*$ shifts with $\rho$ at fixed $\beta$" — which is local and editorial. But the audit's substantive critique implies the *current* prose is incorrect and needs replacement, not augmentation.
- **Recommendation:** Sequence: 30-min scoping spike to confirm whether the $\beta(\rho)$ derivation exists or not; if it doesn't, a one-paragraph rewrite is local and dispatchable. Not parallel-dispatch material until that scoping is done.

### BL-4: AF-14 spike-citation hygiene scope

- **Why borderline:** Listed in §A as an editorial fix per FORMAT.md, but the boundary between "Working-Notes-only spike citations" and "ineradicable spike pointers in promoted content" is judgment-dependent. Some segments cite spikes for the reasoning trail of a result that doesn't have its own derivation segment yet — reading FORMAT.md strictly says move-to-Working-Notes-or-promote-the-spike, but in practice each segment's reviewer has to decide.
- **Recommendation:** Include in §A but flag for orchestrator: dispatched fix-agent should follow strict FORMAT.md rule and surface "this segment's spike-citation can't move to Working Notes because it backs a claim" cases as escalations rather than silently leaving them in place.

---

## Summary of dispatch posture

- **§A (14 candidates) — high-confidence local independent fixes.** Most are ≤30 min editorial; a couple are 30–60 min. Safe to dispatch as parallel background-agent work. Five of the fourteen are pure mechanical bookkeeping (depends-list and link corrections); the other nine are editorial / scope-clarification / cross-reference adds.
- **§B — already in TODO.** Confirms prior extraction was substantially complete on F-V/P-V batch but missed about 14 distinct local items now surfaced. Cross-audit convergence on adaptive tempo / Model S framing / C-iv route is strong and validates existing tracking.
- **§C (4 items) — strengthening-needed.** Each of these the audit proposed softening for without engaging the strengthening question. Per CLAUDE.md "Working Conventions", these need scoping spikes (not fix-agent dispatch).
- **§D (5 items) — architectural / multi-cycle.** Map to existing portfolio bundles (Bundle 1 framework-face reframe; SP-21; tooling enhancements).
- **§E (4 items) — borderline.** Should wait for orchestrator judgment before parallel dispatch.

---

*This file records the audit-extraction triage at one shot; no segments touched.*
