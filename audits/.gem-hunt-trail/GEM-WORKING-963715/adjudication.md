# Gem-hunt adjudication — audit-findings-963715

*Fresh-eyes mining of `audits/audit-findings-963715.md` against current canon, 2026-05-29. Report-only: no canon edits, no file moves, no commits. Landings + independent verification are Joseph's.*

## Bottom line

This audit's substance is **overwhelmingly already in canon, and richly so.** The 963715 cycle was a partial de-novo walk (Section I + first ~14 segments of Section II) whose value was always going to be calibration data and wandering-thought ideation, not net-new theory — and in the ~19 days since, the canon has *closed* most of what the audit surfaced as candidate. The honest result here is closer to "non-loss, safe — here are the loci" than to a pile of gems.

I did the first-hand confirmation work and found only **two genuine content gems**, both framing/positioning (wisdom/beauty), both small but real and *not* in canon. Everything else is either (a) fully captured (with loci below, several of which are valuable "non-loss" confirmations), or (b) process/staging hygiene that is not a gem by the strength/wisdom/beauty test but is worth surfacing because the audit's own "still real" labels have drifted in both directions since 2026-05-20.

**The most important drift-correction:** the audit's flagship structural finding (F2, "derived content embedded in a postulate," cross-cycle-converged with 472913, suggested `architectural`→PROPOSALS) has been **substantially resolved** — the segment was reframed from `type: postulate` / `status: axiomatic` to `type: discussion` / `status: discussion-grade` (commit `6f556aa`, "Recognize composition-consistency as Meta-Architecture II member"). What the audit treated as its highest-priority routable defect is mostly gone. A narrow residual remains (a Gate-1 tag/depends inconsistency), demoted to hygiene below. This is exactly the brief's warning — the pilot's flagship "still real" finding was already resolved 9 days later; here the same thing happened to *this* audit's flagship.

---

## (A) Ready-to-land gems

### A1. The modeler-perspective-vs-agent-perspective framing (wisdom/beauty; framing-level)

**(1) What it is.** AAT is written *from the agent's perspective* — about an agent who does *not* know the observation function $h$ or the transition law $T$ — in contrast to the standard RL/ML idiom, which is written from the *modeler's* perspective (the analyst who knows $h$ and $T$ and is designing for an agent). The sharp consequence the auditor drew: AAT's persistence condition $\alpha \gt \rho/R$ is a **survival condition, not an optimality condition.** That one distinction reorganizes what the framework can and cannot say — it is why AAT can speak about agents that merely persist (biological, organizational, logogenic) rather than only about agents that optimize, and it is the structural reason the survival/optimality split keeps recurring (closure defect ≠ optimality; survival-imperative exploration ≠ value maximization).

**(2) Loci checked — confirmed NOT in canon as a stated framing.** `grep -rni "modeler\|modeller"` across `01-aat-core/src/` returns **zero hits**. The *survival-not-optimality* distinction exists in canon but only *locally* and only for composition: `form-composition-closure.md:268` and `impl-composition-machinery.md:27` ("the framework diagnoses representability, not optimality"); `persistence-and-limits-intro.md:22-24` frames persistence as a regime/threshold and as a "sustained burn rate" but never names the *perspective contrast* with RL/ML, and never elevates "survival not optimality" to a framework-wide stance. The general, voice-defining version — *whose perspective the theory is written from, and what that buys* — is absent.

**(3) Why it's a gem.** Wisdom + beauty. It is precisely the kind of "what makes AAT's voice distinctive vs RL/ML" framing the project's respectful-pedagogy direction is reaching for (`feedback_respectful_pedagogy_mental_model_first`, CLAUDE.md §Feynman-criterion). It is *isomorphic, not merely evocative* (the brief's bar): perturb it — "what if the agent knew $h$ and $T$?" — and you correctly recover the RL/modeler setting where optimality, not survival, is the object. It unifies several scattered survival≠optimality remarks under one recognition.

**(4) Recommended home.** A short framing paragraph. Best fit is the `01-aat-core/OUTLINE.md` "Reading AAT" Layer-0 preamble (the mental-model-first layer), or `persistence-and-limits-intro.md` where survival-as-threshold already lives. Joseph's authoring/voice call — this is framing prose, auditor-visible and priming-heavy, so the honesty bar is sharp (the analog must hold against the formalism, which it does). One tight paragraph, not a new segment.

*Caveat I want to be honest about:* this sits right at the boundary between "real gem" and "nice restatement." I'm calling it a gem because the perspective-contrast is genuinely unstated and it does organizing work, but if Joseph reads the existing intros and feels the stance is already adequately *implied*, this collapses to a soft-polish. I'd rather flag it than inflate it.

---

## (B) Research-seeds

### B1. Noisy-OR rejection as an outward-facing critique of standard PGM planning tooling (wisdom/positioning)

**(1) What it is.** Canon rejects noisy-OR for AND/OR *inward* — as a modeling choice motivated by conjunctive overcounting. The auditor's recognition is *outward*: noisy-OR is the dominant causal-combination function in deployed PGM tooling (BNT, Netica, most Bayesian-network packages), so AAT's "noisy-OR systematically overcounts conjunctive structures" is a **specific technical critique of widely-used planning tooling**, not merely an internal formalism preference. Reframed that way, it is a small but real positioning claim with external bite.

**(2) Loci checked.** `scope-and-or.md:43` carries the full inward treatment — including the exact overcounting table (3 required KRs at $p=0.95,0.90,0.99$: noisy-OR $0.99995$ vs AND $0.846$), the WEIGHTED rejection, and the AND/OR-as-complete-Boolean-basis parsimony argument. The *content* (noisy-OR overcounts conjunctions) is fully present and well-derived. What is absent: any sentence positioning this as a critique of the *field's* tooling. `grep -rni "PGM\|Netica\|BNT\|graphical model"` finds the term "Bayesian network" used only constructively (DAG-as-Bayes-net), never as a target of the overcounting critique.

**(3) Why it's a seed not ready-to-land.** The content exists; only the framing is missing. But the outward claim needs a concrete first task before it can land honestly: **verify that noisy-OR (not log-linear/CPT/other) is in fact the default conjunctive-combination semantics in the named tools**, and confirm the overcounting critique applies to how *planning* (not just diagnosis) uses them. The audit asserts the tooling-dominance claim; I did not verify it, and asserting "this is a critique of standard tooling" in canon without checking the tools would be exactly the plausibility-dressed-as-verification trap. Cheap task (a literature/docs check on BNT/Netica combination defaults), but it is a real task.

**(4) Recommended home (after the verification task).** A 2-3 sentence Discussion addition to `scope-and-or.md`, or a Working-Notes flag there if Joseph wants it tracked as a positioning opportunity rather than landed. Modest value — flag honestly as "small."

### B2. Phase-3-1 cross-cycle pattern — "disambiguation of which parameter responds to which cause" (wisdom; meta-pattern candidate)

**(1) What it is.** Across three independent de-novo cycles (471203 Theme B, 472913 Phase-3-2, 963715 Phase-3-1) auditors converged on the same characterization of AAT's distinctive value-add: not "deriving new inequalities" but **disambiguating which parameter responds to which cause** — making clean distinctions that are "obvious once seen, easy to get wrong unseen." Canonical instances the auditor named: $\beta$ (architectural/memory-cost) vs $\rho$ (dynamical/volatility) in `form-information-bottleneck`; $\eta^\ast$ (architectural gain calibration) vs environmental volatility in `emp-update-gain`; iteration rate $\nu$ vs effective adaptation rate $\mathcal{T}$ in `def-adaptive-tempo`; $\mathcal{F}$ (class-best) vs $S(M_t)$ (achieved) in `def-model-class-fitness`.

**(2) Loci checked.** Each *instance* is in canon and correct (I confirmed the $\beta$-vs-$\rho$, $\eta^\ast$, tempo, and sufficiency distinctions first-hand above). What is *not* in canon is the **pattern named as such** — a `disc-*` meta-recognition that AAT repeatedly does "which-parameter-responds-to-which-cause" disambiguation, the way `disc-additive-coordinate-forcing` and `disc-separability-pattern` name *their* cross-sectional patterns. No segment grep-matches a "disambiguation pattern" meta-recognition.

**(3) Why it's a seed.** Strong *wisdom* candidate, and the convergence-as-framework-coherence evidence is real (Joseph's standing instruction — three independent auditors, different starting points). But naming a meta-pattern is judgment-heavy work that should not be done from four example-instances alone. **First task before landing:** a focused sweep of `01-aat-core/src/` to collect the *full* set of "parameter X responds to cause A, parameter Y to cause B, and conflating them is the common error" disambiguations, then decide whether the set is coherent and large enough to earn a meta-segment (the bar `disc-separability-pattern` / `disc-additive-coordinate-forcing` set) versus staying framing-level pedagogy. If it lands, it's a `disc-*` meta-segment or a respectful-pedagogy framing paragraph; if the sweep finds the instances are heterogeneous, it stays as scattered local Discussion (the honest "leave tiered" outcome).

*Note:* this is the single highest-leverage item in the audit if it pans out, precisely because it is cross-cycle-triangulated. But it is genuinely a research-seed (needs the sweep), not ready-to-land — and I flag that the brief's caution cuts both ways: the convergence makes it *tempting* to over-promote. The sweep is the discipline that keeps it honest.

---

## Process/staging items surfaced (NOT gems — drift-corrected, for the report)

These are not strength/wisdom/beauty treasures, but the brief asks me to weigh audit dispositions against current canon and correct drift. Current first-hand state:

| Audit finding | Audit's 2026-05-20 status | Current first-hand state (2026-05-29) | Note |
|---|---|---|---|
| **F2** (composition-consistency: derived content in a postulate) | "still real," → PROPOSALS, flagship cross-cycle | **Substantially resolved.** Now `disc-composition-consistency`: `type: discussion`, `status: discussion-grade` (was `postulate`/`axiomatic`; commit `6f556aa`). The "derived-in-a-postulate" framing is gone. **Residual:** the `*[Derived (Conditional on Tier 1M … from #result-contraction-template (CC-parallel)/(CC-cascade)/(CC-feedback))]*` tag at line 46 names source slugs (`result-contraction-template`, `form-composition-closure`) that are not in `depends:` (`depends: [scope-agency]` only). That is a real Gate-1 cond-4 tag/depends inconsistency, but hygiene, not architecture. | Flagship finding largely dissolved by canon motion. The residual is a one-line `depends:` reconciliation, not a PROPOSALS-grade move. |
| **F4** (`der-gain-sector-bridge` OUTLINE-vs-frontmatter stage mismatch) | "still real" | **Resolved.** Both OUTLINE row 63 and frontmatter now read `claims-verified` (commit `34a16b5` "audit-finding fixes"). | Closed. |
| **F3** (`def-model-sufficiency` deps-verified depends on `form-information-bottleneck` draft — Gate-1 staging) | "still real" | **Still real.** `def-model-sufficiency`: `stage: deps-verified`, depends includes `form-information-bottleneck`; the latter: `stage: draft`, `status: exact`. | Strengthen-direction (the audit got this right): promote `form-information-bottleneck` (it's `status: exact`), don't demote the dependent. Tooling/staging, → TODO. |
| **F5** (`scope-agent-identity` OUTLINE-vs-frontmatter stage mismatch) | "still real" | **Still real.** OUTLINE row 68 = `deps-verified`; frontmatter = `stage: draft`. | Reconcile via Gate-1 re-review (segment is content-rich; strengthen-direction = promote). → TODO. |
| **F1** (`scope-agency` Pearl-`do` without `depends`) | `correctly-rejected` (external-notation convention) | Confirmed unchanged; disposition holds. External-cited notation incurs no `depends:` obligation. | No action. The path-(a) "introduce `do()` at `post-causal-structure`" idea is an optional hygiene-strengthening, not a defect. |

The combined F3/F4/F5 class points at one genuinely useful tooling idea the audit named: **extend `bin/lint-outline` to check stage consistency between OUTLINE rows and segment frontmatter** (F4 was a member of this class and self-resolved, which is exactly the kind of silent drift a lint check would catch). That is a process/tooling recommendation for TODO, not a theory gem.

---

## Genuinely valueless or fully-superseded (with superseding locus)

The bulk of the audit lands here — and several are *valuable* confirmations (the brief: a confirmed "non-loss, safe" is equally valuable). All verified first-hand against current `src/`.

| Audit item (candidate) | Verdict | Superseding / containing locus |
|---|---|---|
| **Triple depth penalty** → shallow-OR-heavy strategy prior; LLM 10-step $0.8^{10}\approx 0.11$ example, "prefer ≤3-4 steps" | Fully captured (richer in canon) | `der-chain-confidence-decay.md:14,56` (names the triple penalty, anchors additive-coordinate-forcing); `form-strategy-complexity-cost.md:23,109-115,171` (derives max useful depth $d^\ast$ as min over 3 constraints; "systematic pressure toward shallow, OR-heavy strategies"). The LLM numeric instance is a domain application of canon. |
| **Gain-collapse as confirmation-bias formalism** (rational update, miscalibrated gain $\eta^\ast\approx 0$) | Fully captured | `emp-update-gain.md:19,52` (names "gain collapse," Boyd incestuous amplification, recovery mode); `def-mismatch-signal.md:18,52` (zero-aporia three readings); `disc-partial-coupling-pathways.md:153` distinguishes confirmation bias as $M_t^{prior}\to f_M$ self-coupling. |
| **Two parallel exploration drives** (survival $\lambda\propto 1/U_M$ vs epistemic $\lambda\propto U_M$; non-monotone $\lambda$; dark-room bypass) | Fully captured | `deriv-causal-ib-exploration.md:20,69-85` (derives survival drive, dark-room bypass, Brief); `disc-ciy-unified-objective.md:17,56-58` (both drives, opposite ends of uncertainty spectrum); LMI lift `deriv-causal-ib-lmi`. |
| **Sufficiency / fluency / causal-validity tridivision** (LLM high predictive sufficiency yet causally confused) | Fully captured | `def-model-sufficiency.md:16,45` ("Sufficiency is predictive, not causal"; backdoor condition; L1≠L2 not collapsed); `der-action-selection.md:15-17,51` (action fluency distinct from sufficiency). LLM instance is a domain application. |
| **C1/C2/C3 convention monotonicity** $A^{(1)}\le A^{RH}\le A^B$ | Fully captured (derived, exact) | `def-value-object.md:19,21,73,121` (convention hierarchy + derived monotonicity corollary on satisfaction gap / control regret). |
| **Identity-as-trajectory / clone problem / 100% context-turnover / lossy merge / type-vs-token** (ELI grief-framing wandering thoughts) | Fully captured | `scope-agent-identity.md` (whole segment: singular non-forkable $\mathcal{C}_t$; clone problem precisely stated at :53; lossy merge :31; summary-not-trajectory transfer :63; type/token exclusion :39; "structural feature not deficiency" :63; PI axiom + Čencov → Fisher at :35). `03-llm-core/src/obs-context-turnover.md` carries the turnover special case. |
| **Between-event / consolidation / "sleep" dynamics; event-driven vs turn-based asymmetry** | Fully captured (landed as first-class regime) | `form-consolidation-dynamics.md` (whole segment: $g_M$ consolidation regime; Complementary Learning Systems N1+N2 necessity — exactly the "LLM between-events is vacuous" point; stability-plasticity feasibility window; $\nu_{consol}\ll\nu_{online}$ scope). |
| **Modeler-vs-agent perspective switch** (Theme-A item 3) | Partially superseded — the *content* is everywhere implicitly; the *framing* is the A1 gem | See A1. Survival≠optimality exists locally (`form-composition-closure.md:268`) but the perspective-contrast framing is genuinely absent. |
| **§E positive-calibration cluster** (seg 1-3 scope-honesty, seg 17 zero-aporia, seg 23 AI-agent's-dilemma, seg 26 Feynman Brief, seg 37 honest-credit) | Calibration data, not landable content | These are observations *that the discipline held* — they describe canon, they are not additions to it. seg-23's reflexive self-application is the most quotable; `der-deliberation-cost` already carries it. Sentiment-ledger material at most. |
| **6 first-hand math verifications** (mismatch decomposition cross-term, Model-S Itô, sector counterexample, persistence forms, convention monotonicity, chain decay) — all passed | Calibration data (positive) | Confirms canon math; no edit implied. Genuinely valuable as a "non-loss, safe" signal on the §I core. |
| **Open-1…Open-5** (Section II-15+, Section III composition, Appendices, TST/03/04, GUC-rename in §III) | Not present-state findings — future-audit flags | These are coverage gaps of the *audit*, not defects of the *canon*. GUC-rename cleanliness within audited scope (Open-5) is a positive §E observation, already corroborated by the post-audit GUC-residue fixes in the git log (e.g. `0884e12`). Route as future-audit TODO if desired; not gems. |
| **Process-1/2/3** (batch-vs-single cadence; stable finding-IDs; priming-as-falsifiable-bets) | Methodology data | `doc/de-novo-audit-instructions.md` revision material, not theory. Out of gem scope. |

---

## Honest coverage statement

- **Read first-hand from `01-aat-core/src/` (current canon):** `scope-agency`, `disc-composition-consistency` (the former `post-composition-consistency`), `def-model-sufficiency`, `form-information-bottleneck`, `der-gain-sector-bridge`, `scope-agent-identity`, `scope-and-or`, `der-chain-confidence-decay`, `form-strategy-complexity-cost`, `emp-update-gain`, `def-mismatch-signal`, `deriv-causal-ib-exploration`, `disc-ciy-unified-objective`, `def-value-object`, `der-action-selection`, `form-consolidation-dynamics`, plus targeted greps across the full `src/` tree and `01-aat-core/OUTLINE.md` (rows 63, 68, 77). Confirmed `03-llm-core/src/` carries `obs-context-turnover` and the logogenic cluster.
- **Read the full audit file** `audits/audit-findings-963715.md` (466 lines, both pages) and `INTEGRATION-CLEANUP-TODO.md` for recovery context.
- **Checked git log** since 2026-05-19 on `01-aat-core/src/` to attribute the F2/F4 resolutions to specific commits (`6f556aa`, `34a16b5`).
- **Did not** independently verify the B1 tooling-dominance claim (BNT/Netica noisy-OR defaults) — that *is* B1's named first task, deliberately left for the verification gate rather than asserted.
- **Did not** re-derive the canon math (the audit's six verifications stand on the auditor's first-hand work; the segments are content-stable since 2026-05-10 except where noted).

## One frank methodological note

This audit was always going to be thin on gems by construction: it is a *partial walk of the most mature volume's most mature sections*, whose explicit value was calibration and ideation. The brief warns against manufacturing gems to show progress, and the honest read is that I found two small framing gems (A1, B1) and one genuine-but-needs-a-sweep meta-pattern (B2), against a large body of fully-captured content. The single most useful thing this pass produced is probably the *drift correction* on F2 — the audit's own flagship, routed as PROPOSALS-grade, is mostly resolved — which is exactly the failure-mode the brief named and worth more to the project than a forced gem would be.
