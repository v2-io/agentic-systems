# Gem-hunt adjudication — audit-findings-526815

*Adjudicator: Claude Opus 4.8 (1M), 2026-05-29. Report-only — no canon edits, no file moves, no commits. Landings and independent verification are Joseph's.*

## What this audit is, and the headline result

`audits/audit-findings-526815.md` is itself an *extraction* (Opus 4.7, 2026-05-20) of the de-novo working dir `AUDIT-WORKING-526815/` (Opus 4.7, 2026-05-15). The original walk was the deepest AAT-only first-encounter in the corpus — 94 segments first-hand, 258 F-numbered candidates, per-segment TikZ-PDF renders. No FINAL was written, so every observation is candidate-fresh.

The extraction agent did first-hand verification of its four "Theme 1" high-severity findings *as of 2026-05-20* and stamped them "still real." I re-verified those four plus several others first-hand against current canon (2026-05-29) — **9 days and several commits later**. The headline result is exactly the pilot lesson the brief warned about, and it cuts the *opposite* way from naive expectation:

**The audit's flagship structural findings have been resolved in canon since the extraction. The surviving gems are the two clean isolated math errors the audit ranked alongside them.** Labels lied in the over-claiming direction here: "verified still real 2026-05-20" was true then and false now for F2/F116-118/F151/F66/F68.

Concretely, of the high-severity / cross-cycle-convergent set:

| Audit finding | Extraction said (2026-05-20) | First-hand now (2026-05-29) |
|---|---|---|
| **T1-F2** (composition-consistency forward-`*[Derived]*`) | "still real," 3-cycle convergent, → PROPOSALS split | **RESOLVED** — split executed. See §C-1 below. |
| **T1-F116/117/118** (tempo-composition double-count) | "likely still real" | **RESOLVED (needs your confirm)** — dimensional-accounting rework. §C-2. |
| **F151** (unity-closure intra-segment C-iv contradiction) | flagged easy-to-verify, deferred | **RESOLVED** — segment now says "three routes" throughout. §C-3. |
| **F66 / F68** (strategic-tempo throughput-vs-bottleneck naming) | → FINAL §F naming | **RESOLVED** — fully distinguished. §C-4. |
| **T1-F69** (strategy-complexity-cost table row) | "still real" | **STILL REAL** — gem A-1. |
| **T1-F146** (unity-dimensions $U_M$ normalization) | "still real" | **STILL REAL** — gem A-2. |

This is the un-captured/captured weigh the brief asks for: the structural-placement findings turned out captured (canon moved); the two arithmetic/normalization errors are genuinely un-captured and would have to be re-found later, so they are the real treasure.

---

## (A) Ready-to-land gems — content exists, needs only a home + your verification

### A-1. `form-strategy-complexity-cost` quantitative-illustration table: the $n=100, \rho/R=0.01$ row is wrong ($d^\ast=0$, not 5)

**(1) What it is.** In `01-aat-core/src/form-strategy-complexity-cost.md`, the "Quantitative illustration" table (lines 96-105) lists, for $\theta=0.8, \nu=1$:

| $n$ | $\rho_\Sigma/R_\Sigma$ | $d^\ast$ (table) | $d^\ast$ (correct) |
|---|---|---|---|
| 10 | 0.01 | 10 | 10 ✓ |
| 10 | 0.1 | 0 | 0 ✓ |
| **100** | **0.01** | **5** | **0** ✗ |
| 100 | 0.1 | 0 | 0 ✓ |

The segment's own formula is $d^\ast = 1 + \lfloor \log(\nu/((n+1)\rho/R)) / \log(1/\theta)\rfloor$, and its own interpretive note (line 92) says "When $\nu/((n+1)\rho/R)\le 1$, even $d=1$ fails." For the $n=100,\rho/R=0.01$ row: $\nu/((n+1)\rho/R)=1/(101\cdot0.01)=1/1.01\approx0.990 < 1$ → even $d=1$ fails → $d^\ast=0$. The table says 5, which contradicts both the formula and the segment's own note. I recomputed all four rows by hand; **only this one row is wrong** (the other three check out, including the $n=10$ row's $d^\ast=10$).

**(2) Loci checked first-hand.** `01-aat-core/src/form-strategy-complexity-cost.md` read in full; formula at lines 84-92, table at 96-105, interpretive note at 92. Recomputed every row.

**(3) Why it's a gem — strength.** A clean, anyone-could-find-it arithmetic error in a quantitative table inside a `robust-qualitative` segment, sitting two lines below a formula that says the opposite. An external reader who checks the arithmetic loses trust in the surrounding (correct) machinery. Catching it is pure strength (correctness).

**(4) Recommended home.** Existing segment, direct fix. Two honest options, your call: (a) recompute the row to $d^\ast=0$; or (b) change the row's parameters to ones that genuinely yield $d^\ast=5$ (e.g. raise $n$/lower $\rho/R$ so the log-argument lands in $[\theta^{-4}, \theta^{-5})$). Option (b) better preserves the table's pedagogical intent of showing a non-degenerate intermediate depth. Either way, re-verify the whole row set at fix time. **Not a softening; a correctness fix.**

### A-2. `def-unity-dimensions` epistemic-unity $U_M$: "$U_M=1$ for identical models" is false for $n\ge 3$

**(1) What it is.** `01-aat-core/src/def-unity-dimensions.md:34-36` defines $U_M = I(M^{(1)};\ldots;M^{(n)}) / H(M^{(1)},\ldots,M^{(n)})$ (multi-information / total-correlation over joint entropy) and claims "$U_M=1$ for identical models; $U_M=0$ for independent models." For $n$ identical RVs each with entropy $H$: total correlation $T=\sum_i H(X_i)-H(\text{joint})=nH-H=(n-1)H$; joint entropy $=H$; ratio $=n-1$. So the claim holds *only coincidentally at $n=2$*; at $n=3$ it gives 2, and it is unbounded in $n$ — the metric is not the $[0,1]$-valued quantity the segment and all downstream uses assume. The strengthen-first repair (not a soften): renormalize, e.g. $U_M = T/((n-1)\max_i H_i)$, which lands identical-models at exactly 1 and is in $[0,1]$; or swap to normalized total correlation (Watanabe 1960). The choice ripples into `result-unity-closure-mapping`'s "monotone in $U_M$" surface, so a tiny normalization spike that confirms the chosen form preserves the segment's substantive monotonicity claims is the careful path.

**(2) Loci checked first-hand.** `def-unity-dimensions.md` read in full (current state: `status: discussion-grade`, `stage: draft`). Formula and the "$U_M=1$ for identical models" claim at line 36, unchanged since the audit. `result-unity-closure-mapping.md` read for the downstream dependency (line 12, the "$\varepsilon_d$ monotone decreasing in $U_d$" surface).

**(3) Why it's a gem — strength (with a wisdom caveat).** The error is real and load-bearing: $U_M$ is the base of the unity-closure / shared-intent / auftragstaktik machinery, and a base axis that exceeds its claimed range quietly breaks every "$[0,1]$-valued unity" downstream statement. *Caveat that lowers its severity vs the audit's framing:* the segment is now honestly tier-marked `discussion-grade`, and its Working Notes openly say "the specific metrics are sketches... require specifying distributions." So this is not unmarked false confidence — it is a concrete false *claim* ("$U_M=1$ for identical models") inside an honestly-hedged segment. Still worth fixing, because the specific identical-models limit is exactly the kind of sanity-check claim a reader uses to trust the metric, and it's wrong as stated.

**(4) Recommended home.** Existing segment, edit at line 36 + a one-paragraph normalization note; optionally a small spike first to pick the normalization that preserves downstream monotonicity (so this borders on B). I place it in A because the fix is local and the content (the corrected limit) is fully specified above. The siblings F147/F148/F150 ($U_O$ distribution-dependence, $U_\Sigma$ KL can be infinite/negative, $U_f$ not naturally $[0,1]$) are plausibly real too but I did **not** re-verify them first-hand — flag for the same pass since they're co-located.

---

## (B) Research-seeds — real direction, needs a concrete first task before landing

### B-1. Chronica record-vs-causal-token: a possible second symbol ($\gamma_t$) for the trajectory token

**(1) What it is.** The audit (F16 / Theme 10 / Theme A) observed — across *three* independent cycles (471203 Theme A, 472913 F4 ordinal/metric seam, 526815 F16) — that `def-chronica` uses $\mathcal{C}_t$ for two things the framework leans on differently: the agent's *represented record* (an ordered $(o_1,a_1,\ldots)$ sequence whose representation *can* be copied) and the *singular non-forkable causal trajectory* (which cannot). The non-forkability claim is true of the causal token, not of the mathematical record. The auditor's concrete proposal: introduce $\gamma_t$ for the causal trajectory token and reserve $\mathcal{C}_t$ for the record, then state sufficiency/non-forkability as indexed to $\gamma_t$.

**(2) Loci checked first-hand.** `def-chronica.md` (full — `status: axiomatic`; line 14 "complete *record*", line 36 "unique causal *trajectory*" both bound to $\mathcal{C}_t$; Working Notes track ordinal-vs-metric and TRACTUS/CHRONICA but *not* record-vs-token). `scope-agent-identity.md` (full — type/token distinction is *already in canon* at lines 19, 39; non-forkability, clone problem, trajectory-indexed sufficiency, logogenic bridge all present). So the *substance* is captured; only the record/token *notational* split is not.

**(3) Why it's a gem — wisdom.** This is the precise hinge on which substrate-migration / "Three Deaths" persistence claims turn for the ELI program: copying a model snapshot (record) does *not* copy the trajectory (token), and a sharp symbol makes that un-foolable in the math rather than relying on prose. Three-cycle convergence is strong evidence the distinction is load-bearing and currently under-notated. (Per `feedback_convergence_as_framework_coherence_evidence`.)

**(4) First task before landing.** Decide whether the record/token split earns a *second Part-I symbol* or is better carried by the *already-planned logogenic-side split* (`def-chronica` Working Notes already foresee `def-tractus` + a refined chronica when `03-llm-core/` matures). The honest first task: a half-page decision memo answering "does $\gamma_t$-vs-$\mathcal{C}_t$ buy anything in Part I that the TRACTUS/CHRONICA + scope-agent-identity type/token machinery doesn't already buy?" If yes → land the symbol in `def-chronica` + `scope-agent-identity`; if no → record the decision in `def-chronica` Working Notes so the fourth cycle stops re-surfacing it. **Home: honest-frontier decision, then either `def-chronica`/`scope-agent-identity` or `04-eli-core/` framing.**

### B-2. Cross-segment C-iv route-count inconsistency: `def-unity-dimensions` (four routes) vs `result-unity-closure-mapping` (three routes)

**(1) What it is.** The audit's F151 flagged an *intra-segment* contradiction in `result-unity-closure-mapping` (opening said four routes incl. C-iv, Working Notes said three). That intra-segment contradiction is **resolved** (§C-3). But in re-verifying it I found a related *cross-segment* tension that is live: `def-unity-dimensions.md` (lines 15, 22, 44, 116) conditions on `#scope-composite-agent` "via at least one of its four routes (three alignment + the strategic-equilibrium route C-iv)," while `result-unity-closure-mapping.md:123` conditions on the same scope "via at least one of its three disjunctive routes (shared objective, hierarchical derivation, mutual benefit)" — i.e. *excluding* C-iv. Two tightly-coupled segments (one `depends:` on the other) disagree on whether C-iv is a scope route for the same composite-quality machinery.

**(2) Loci checked first-hand.** `def-unity-dimensions.md` (four-route framing, multiple loci above). `result-unity-closure-mapping.md` (full; three-route framing at line 123; opening and IB sections carry no four-route claim). I did **not** read `scope-composite-agent.md` itself to determine which count is currently canonical — that's the gating task below.

**(3) Why it's a gem — wisdom/strength.** Part III composition scope is in active evolution (the audit's Theme 9 names C-iv as recently added). When two coupled segments disagree on the route count, downstream "$U_M$ is conditional on scope" statements are conditioned on different scopes — exactly the cross-level inconsistency `disc-composition-consistency` exists to forbid. Cheap to find, real, not the same as the resolved F151.

**(4) First task before landing.** Read `scope-composite-agent.md` first-hand and establish the *current canonical route count* (3 alignment, or 3+C-iv). Then harmonize the two dependents to it (one-line edits) — and check whether the audit's F241 ("`deriv-strategic-composition` introduces C-iv as a formulation choice rather than a routed update to the scope segment") is the origin of the drift. **Home: existing segments after the scope-segment read; possibly a small PROPOSALS note if C-iv's status is genuinely unsettled rather than just unpropagated.**

### B-3. Expected-vs-realized information convention (PMI/KL vs channel MI) — multi-segment + a LEXICON entry

**(1) What it is.** The audit (Theme 3: F5/F19/F203/F204) observed a recurring notational pattern: formulas written as mutual information $I(X;Y\mid Z)$ (an *expected*, channel-average quantity) but described in prose as the *realized* information content of a particular event/instance. The quantities the segments actually reach for are well-defined (pointwise MI, surprisal, $D_{KL}(p(\Omega\mid M,e)\Vert p(\Omega\mid M))$) — so this is a notation/consistency issue, not a content error.

**(2) Loci checked first-hand.** I did **not** re-verify the four instances against current `src/` (honest defer — these are spread across `form-event-driven-dynamics`, `der-directed-separation`, `der-interaction-channel-classification`). I am carrying the auditor's reading; given the four flagship structural findings *resolved* under me, treat this as un-verified-hint until checked.

**(3) Why it's a gem — beauty (clarity/unification).** A single LEXICON entry distinguishing "expected channel MI" from "realized event information," plus a one-pass sweep, would remove a recurring reader-confusion across foundational and downstream segments and institutionalize the distinction. Low-risk, clarity-improving.

**(4) First task before landing.** Re-verify the four instances are still in their flagged form against current `src/` (the resolution rate in this audit means this is non-optional), then draft the LEXICON entry + sweep. **Home: LEXICON entry + per-segment editorial; consider a FORMAT.md "information-quantity convention" note.**

### B-4. Dimensional/unit-normalization seam across the gain/tempo/persistence triangle — finish `der-gain-sector-bridge` first

**(1) What it is.** The audit's single most-recurrent *substantive* concern (Theme 4: F9/F10/F13/F14/F15/F17/F189/F190/F215/F209, ~8+ instances): AAT has several rate-shaped quantities — per-event update gain $\eta^\ast$, event rate $\nu$, scalar adaptive tempo $\mathcal{T}$, sector correction rate $\alpha$ — and downstream segments routinely assume the bridge between them ($\alpha=\mathcal{T}$, etc.) has landed *exact* when `der-gain-sector-bridge` is (per the audit) `status: conditional, stage: draft` with proof dependencies not yet in order. The strengthen-first move (explicitly *not* a soften): finish `der-gain-sector-bridge` + `deriv-gain-sector` + `deriv-sector-condition`, then propagate the cleaned per-event-vs-per-time normalization through the ~8 downstream segments.

**(2) Loci checked first-hand.** I did **not** open `der-gain-sector-bridge.md` or the proof segments this pass (the audit itself never reached Appendix A — its "Open-H1" thread). Carrying the auditor's reading. Note `scope-agent-identity.md:35` shows the (PI)+Čencov route that *forces* the Fisher metric on $M_t$ sub-cases is already in canon — relevant to F13's "weighted/Fisher metric vs Euclidean" sub-point, suggesting part of the bridge's machinery has matured since 2026-05-15.

**(3) Why it's a gem — strength.** If real, it's a keystone: the dimensional convention underpins the persistence inequality everywhere. The auditor's reading is that the bridge segment is *unusually careful* (471203 called it a "high-water mark") and its honesty is precisely what makes the downstream over-assumption visible — so the gem is "finish + propagate," not "the bridge is wrong."

**(4) First task before landing.** Read `der-gain-sector-bridge.md` + `deriv-sector-condition.md` first-hand and establish current status/stage (the audit's data is 2-weeks-stale and the resolution rate above says re-check before investing). If still draft/conditional: scope the finishing spike. If matured: the gem collapses to a propagation-sweep. **Home: PROPOSALS (multi-segment), queued behind the bridge-finishing cycle; connects to PRACTICA's persistence-and-stability area.**

### B-5. `impl-*` synthesis discipline: a FORMAT convention forcing chapter-end segments to inherit weakest-dependency status

**(1) What it is.** The audit's Theme 6 (F46/F88-91/F139-144/F173-176/F222-225) observed a clean recurring class: chapter-end `impl-*` discussion segments synthesize locals + future/appendix proof homes, and the synthesis prose sometimes presents deferred/discussion-grade claims as chapter-level deliverables (status laundering). The strengthen-first move: a FORMAT.md sub-convention — "each implied claim in an `impl-*` segment cites its proof home and inherits that home's status" — closes most of the class mechanically and aligns with the CLAUDE.md "respectful pedagogy" direction (scaffold without laundering status).

**(2) Loci checked first-hand.** Not re-verified this pass (would require reading the `impl-*` segments). Carrying the auditor's reading.

**(3) Why it's a gem — wisdom (process/form).** It's a structural discipline, not a one-segment fix; if the class is real it prevents a whole family of over-claims at the most auditor-visible (priming-heavy) prose layer. The brief's own strengthen-first reflex applies — make dependency-status explicit rather than softening the synthesis.

**(4) First task before landing.** Spot-verify 2-3 of the named instances against current `src/` (e.g. `impl-composition-machinery` F139-144 — note F2's resolution means the composition-machinery area has been actively reworked, so several of these may already be gone). If the class survives, draft the FORMAT convention. **Home: PROPOSALS (FORMAT convention) + per-instance editorial; cross-ref CLAUDE.md respectful-pedagogy.**

### B-6. Dependency-graph eq-tag lint (TG1-analog) — tooling, not theory

**(1) What it is.** The audit's Theme 2 was the highest-instance-count class in any single cycle (~20+ explicit cases): segments whose `*[Derived (… from #X …)]*` eq-tags or body `#slug` references cite slugs not in `depends:`. The proposed strengthen-first move is *tooling*: extend `bin/lint-outline` to parse `*[Derived (… from #X …)]*` and require `#X` in `depends:` (and topologically prior); plus a softer "hidden-semantic-dependency" warn-lint for body `#slug` references. This routes to existing PROPOSALS SP-6.

**(2) Loci checked first-hand.** The flagship instance of this class was **F2**, which I verified is now *resolved* (the offending eq-tag is gone — §C-1). I did not enumerate the other ~20. Important nuance: F2's resolution means the *instance count is stale* — an unknown fraction of the 20+ may have been cleaned in the same reworks. The *class* (and the tooling value) stands regardless.

**(3) Why it's a gem — wisdom (durable tooling).** A lint rule converts a recurring manual-audit burden into a mechanical gate — durable value independent of how many current instances remain. This is the right shape for the deepest-instance-count finding: don't chase the instances, build the check.

**(4) First task before landing.** Feasibility spike: can `bin/lint-outline` parse the `*[Derived (… from #X …)]*` eq-tag grammar cleanly? (The audit flagged this as an open feasibility question.) Then implement + run to get the *current* instance count. **Home: PROPOSALS SP-6 (consolidate, do not open N rows); tooling work.**

---

## (C) Confirmed non-losses — findings resolved in canon since the audit (each a "safe" result)

Per the brief, a confirmed "already in canon / resolved" with the locus is equally valuable. These were the audit's *strongest-rated* findings; all checked first-hand 2026-05-29.

### C-1. T1-F2 (composition-consistency forward-`*[Derived]*`) — RESOLVED via the exact split the audit recommended.
The audit flagged `post-composition-consistency` as `type: postulate, status: axiomatic` carrying a downstream `*[Derived (Conditional on Tier 1M…, from #result-contraction-template …)]*` eq-tag at line 36, with none of the cited slugs in `depends:` — a Gate-1 cond-4 violation, flagged 3-cycle-convergent (471203/472913/526815), recommended "split not soften," and stamped "still real" on 2026-05-20. **Current state** (`01-aat-core/src/disc-composition-consistency.md`): renamed `post-` → `disc-`; `type: discussion`, `status: discussion-grade`; the eq-tag is now `*[Commitment (composition-consistency)]*` + `*[Structural consequence (derivation hierarchy)]*`; the downstream-derived $\lambda_c$ closed forms are **removed from the Formal Expression** and the segment now *narrates* the three-layer scope/admissibility/transfer hierarchy, pointing to where the math lives (`#form-composition-closure`, `#result-contraction-template`) rather than carrying the payload. This is precisely the recommended fix, executed. (CHANGELOG: commit `6f556aa` "Recognize composition-consistency as Meta-Architecture II member.") The `depends: [scope-agency]` is still minimal, but a `discussion` segment's narrative prose references are not the Gate-1 cond-4 violation an eq-tag-cited `*[Derived]*` source is. **Non-loss: the structural insight (Chapter-1 postulate shouldn't carry downstream-derived payload) was correct and is now embodied in canon.**

### C-2. T1-F116/F117/F118 (tempo-composition double-accounting) — RESOLVED (recommend you confirm the algebra).
`01-aat-core/src/der-tempo-composition.md` now carries an explicit **"Dimensional accounting"** units table (lines 48-57) and a "Consequences (dimensionally correct)" section. F116's alleged double-subtraction no longer holds: $C_{\text{coord}}$ is now defined as $\geq \varepsilon^\ast\nu_c/\lVert\delta_{\text{critical}}\rVert$ (closure-defect-driven), **not** as $\sum\mathcal{T}_i-\mathcal{T}_c$; and $\mathcal{T}_c=\sum\mathcal{T}_i$ only at $\varepsilon^\ast=0$. F117's disturbance-vs-tempo "double count" is now one consistent ledger ($\rho_{\text{eff}}=\rho_{\text{ext}}+\varepsilon^\ast\nu_c$ on one side; persistence converts once). F118's "not equivalent" is now derived with units annotated (lines 73-80). I verified the structure first-hand but did **not** re-derive every algebraic step — recommend a quick confirm at the equivalence at lines 78-80.

### C-3. F151 (unity-closure intra-segment C-iv contradiction) — RESOLVED.
`01-aat-core/src/result-unity-closure-mapping.md` now says "three disjunctive routes (shared objective, hierarchical derivation, mutual benefit)" at line 123, and the opening carries no competing four-route claim. The intra-segment contradiction is gone. (The remaining "four" mentions in that file refer to the four *content unities* $U_M/U_O/U_\Sigma/U_{\text{obs}}$ — a different object.) The *cross-segment* count mismatch with `def-unity-dimensions` is a distinct, still-live issue → gem B-2.

### C-4. F66 / F68 (strategic-tempo throughput-vs-bottleneck) — RESOLVED, thoroughly.
`01-aat-core/src/def-strategic-tempo.md` now explicitly distinguishes throughput-sum from persistence-bottleneck: line 20 "Persistence is bottleneck-limited by the weakest edge, not governed by the aggregate"; line 94 "minimum ≤ average ≤ sum"; line 115 names "$\mathcal{T}_\Sigma=\sum$ … is the throughput aggregation; the bottleneck form is the persistence-relevant aggregation" (with a NeurIPS Paper 2 `#lem-forgetting` cross-ref). F68's heterogeneous-edge concern is handled: persistence is stated per-edge ($\forall(i,j)$, line 20/86-90), with $|E|\cdot\rho/R$ explicitly marked necessary-but-not-sufficient (line 94).

---

## Genuinely valueless / fully-superseded for gem purposes

- **Theme B (epistemic-architectural contribution observation)** — the extraction agent already marked this `subsumed-by-prior-extractions` (richer in 471203/472913). It is a real and important framing but it is *not un-captured* — CLAUDE.md's "Math-novelty recognition" and "Reading and writing posture" sections already carry it. No gem; the third independent landing is corroboration, not new content.
- **Theme E (cross-domain operationalization), Theme G (audit-as-instance-of-theory), Theme C (pacing/phenomenology)** — process/methodology observations, already `subsumed` or `process/instruction-feedback` per the extraction. Real for audit-instruction evolution, not theory-content gems.
- **Theme F (per-segment PDF-render methodology)** — genuinely distinctive *audit methodology* and worth a Joseph-decision on the gold-standing gate for the ~462 render artifacts in `AUDIT-WORKING-526815/`, but it is not AAT-content. Note for your gold-gate call: the renders are first-encounter cognition embodied as compiled artifacts; the brief told me to ignore them for token-economy and I did. Surfacing as a process item, not a gem.

---

## Honest coverage + caveats

**Re-verified first-hand against current `01-aat-core/src/` (2026-05-29):** `disc-composition-consistency.md` (full), `form-strategy-complexity-cost.md` (full, all 4 table rows recomputed), `def-unity-dimensions.md` (full), `der-tempo-composition.md` (lines 40-89), `result-unity-closure-mapping.md` (full + grep), `def-strategic-tempo.md` (full + grep), `scope-agent-identity.md` (full), `def-chronica.md` (full). Read in full: the audit file (552 lines) and `INTEGRATION-CLEANUP-TODO.md`.

**Carried from the audit without first-hand re-verification (honest defer — and the resolution rate above is the reason these need checking before investment):** Theme 3 (F5/F19/F203/F204), Theme 4 (the ~8 dimensional instances), Theme 5 (~18 scope/status), Theme 6 (the `impl-*` instances), Theme 7 (~25 probability findings beyond F146/F69), Theme 9 (C-iv composition machinery beyond F151), Theme 11 (trust/loss-function). Several of these almost certainly have moved the way F2/F116-118/F151/F66/F68 did, since they cluster in the same actively-reworked composition/unity/tempo machinery.

**The load-bearing caution for you.** This pass's dominant finding is *not* a pile of new gems — it is that **this audit's flagship substance has largely landed in canon**, and the two surviving content gems (A-1, A-2) are clean isolated errors the audit ranked correctly. I deliberately did not manufacture gems from the ~200 unverified F-rows; doing so would have inverted the brief, because the verified ones resolved at a high rate and the unverified ones share their neighborhoods. The careful result here is "two real un-captured errors + four confirmed non-losses + five seeds that each need a first-hand re-check before they earn investment" — and the strongest single recommendation is to **fix A-1 and A-2** (they would otherwise have to be re-found) and to **treat any Theme-2/4/5/6 instance count as stale** until re-grepped.
