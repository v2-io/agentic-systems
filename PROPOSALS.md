# PROPOSALS — Architectural Portfolio

**Last reconciled:** 2026-04-24 (post-cluster-audit consolidation).

This file replaces `msc/architectural-proposals-2026-04-22.md`. That document accumulated 33 proposals across four audit cycles; many had substantively landed but were still catalogued as open; several were superseded; a few unpromoted architectural moves were hiding in segment Working Notes and `msc/` brainstorm documents. This is the slim, verified, banded portfolio produced by the 2026-04-24 consolidation audit.

**Navigation:**
- §Cross-cutting view — two bundles that cross the bands.
- §A. Absorbed — fully landed; moved to LOG. Kept here as traceability pointers.
- §B. Ready now — prereqs met, execute in the next cycle or two.
- §C. Soon — prereqs nearly met, 1–2 cycles until natural readiness.
- §D. Later — real value; needs investigation-first scoping or upstream conditions.
- §E. Wait — client-gated or paper-writing-time.
- §F. Retired / superseded — absorbed by other landings; do not re-propose.
- §G. Newly surfaced (2026-04-24 audit) — previously unpromoted candidates.
- §H. Conventions for future audits.

**Per-proposal markers.** Each active proposal carries:
- **Value** — the cluster-agent's -10 to +10 estimate, framework/paper split where relevant.
- **Independence** — whether the proposal can be worked on in parallel with other active proposals without merge or semantic conflict. **High** = touches distinct file/conceptual territory, safe to parallelize. **Medium** = light overlap with other proposals on shared segments, parallelizable with coordination. **Low** = touches the same core surface as other active work (often meta-segment rewrites or cross-segment naming passes); serialize. Bundles carry a bundle-level marker plus internal notes where members differ.

**Provenance.** G-BP = Gemini bigger-picture; O-BP = Opus bigger-picture; C-BP = Codex round-2 bigger-picture; SP = session-or-post-session-discovered. Entries SP-11 through SP-19 surfaced in the 2026-04-24 consolidation audit from Working Notes / reflections / brainstorm documents that the prior portfolio did not capture.

---

## Cross-cutting view

Two bundles cross the bands. Handling them as unified work-items rather than as enumerations of their parts is the highest-leverage organizing move in this portfolio.

### Bundle 1 — Framework-face reframe (paper-writing-time)

Seven proposals converge on a single coordinated reframing pass that would shift AAT's public self-presentation from "integration of four disciplines" to "epistemic architecture with three-part meta-structure plus integrating content." Three independent frontier-model audits (Codex / Gemini / Opus, 2026-04-23) converged on this reframe on different axes; the segment-level infrastructure is already in place (CLAUDE.md §7 landed, OUTLINE.md "Reading AAT" paragraph landed, the three meta-segments `#additive-coordinate-forcing` / `#disc-identifiability-floor` / `#disc-separability-pattern` all live in Appendix A).

**Bundle members:** SP-7 (epistemic architecture foregrounding) + O-BP1 (sector-persistence template as organizing principle) + **O-BP10 (projection-contraction slogan) — LANDED at segment level 2026-05-14 as `#result-certificate-existence`** (`status: exact`; the slogan *an adaptive system is an operator whose contraction rate exceeds its target's drift rate* is now the Lyapunov-theorem equivalence "operator-sector in some metric ⟺ exponentially stable", with the certificate as witness — see CHANGELOG 2026-05-14 and `#disc-stability-certificate`; the long-standing "not yet surfaced at segment level" condition is discharged) + O-BP8 (scope lattice) + SP-3 (calibration-laboratory template generalization) + SP-4 (agent-identity from scope to architectural postulate) + SP-8 (dual-edged floor/separability reading).

**What remains unlanded:** README.md rewrite (still integration-first at line 10); OUTLINE.md preamble pass for Section I/II/III (the cross-sectional "Reading AAT" preamble *was* reframed 2026-05-14 into a two-layer mental-model-first form built on the certificate spine — the per-Part Section I/II/III preamble passes remain); possible new canonical scope-lattice location; `domain-instantiation-template.md` or FORMAT.md section; `#scope-agent-identity` frontmatter `type: scope → postulate`; `#disc-identifiability-floor` + `#disc-separability-pattern` dual-edged editorial touches. *(The O-BP10 sub-item "`#result-sector-persistence-template` introductory paragraph restating the slogan" is superseded: the slogan now has its own exact-tier home `#result-certificate-existence` which the template cross-references as its interior facet, rather than the slogan being restated in an intro paragraph.)*

**Total effort:** 2–3 coordinated sessions. Individual pieces are each small; the benefit of coordination is that the reframe reads consistently across README / OUTLINE / CLAUDE / segments rather than drifting between framings.

**Value:** **+9 for framework identity; +10 for paper-writing.** This is the highest-leverage single move available in the portfolio. Joseph-check-in recommended before execution (the organizing axis is architectural and commits the framework's self-presentation for future work).

**Independence:** Bundle-internal: **low** — all seven members converge on the same presentation surface (README + OUTLINE preambles + three meta-segments + `#scope-agent-identity` + `#result-sector-persistence-template`); must be done as one coordinated pass rather than parallelized. Bundle-external: **high** — touches mostly framing surfaces; does not conflict with Section I / II / III substantive segment work. Safe to run in parallel with Bundle 2 or with individual §C / §D items.

**Risk:** The Fenchel-Bregman reframe (SP-9) proposes to further reorganize `#additive-coordinate-forcing` into "one geometric object + four axioms converging on it." If SP-9 is executed, the bundle's framing of the meta-segments would need revision. Two resolutions: (a) do the bundle first with the current 1-anchor-plus-3-theorem characterization (stable); (b) scope SP-9 first, decide if it supersedes SP-1's landed framing, then do the bundle. **Recommendation: (a) — don't let the Tier-3 reframe-proposal delay the framework-face work.**

### Bundle 2 — Section III completion cluster

Five proposals form a coherent Section III completeness program. Section III has the most structural work remaining (four named GAPs in `01-aat-core/OUTLINE.md` lines 145–148) and the portfolio under-represents the cluster despite its weight.

**Bundle members:** O-BP16 (population-level Lyapunov — spans latent structural diversity, endogenous coupling, composition transition dynamics) + O-BP9 (typed admissibility for composition — model-only / goal-bearing / strategy-bearing) + SP-6 (composition-closure consolidation — scope-narrowing post-2026-04-24 Tier 1 absorption) + SP-11 (composition-monotonicity meta-segment — **newly surfaced**, fourth Section-III-native meta-segment parallel to the three-part epistemic architecture) + SP-17 (goal-information-leakage $\mathcal{L}_{G \to M}^c$ as first-class Section-III quantity — **newly surfaced**).

**What this bundle closes:** all four named OUTLINE GAPs (latent structural diversity; endogenous coupling γ as function of population composition; composition transition dynamics per Miller 2022; computational thresholds for social behavior per Miller 2022 ICE) plus F26 (composition-closure generality scope) plus F8 ((C-iii) mutual-benefit vs (A1) decomposable $G_c$ gap). Establishes Section III's fourth meta-segment and gives Section III its own organizing-principle analog to `#additive-coordinate-forcing`'s role for single-agent AAT.

**Total effort:** 6–10 sessions if pursued as a program; individual pieces are independently valuable; O-BP16 and SP-11 carry Kalman-Ho / C2-spike-promotion follow-up spikes queued.

**Value:** **+7 for framework completeness.** Section III is AAT's structurally weakest and most empirically important half (composition is where interesting multi-agent phenomena live); completing this cluster would close the OUTLINE preamble's explicit self-identified weakness.

**Independence:** Bundle-internal: **medium** — SP-11 (new meta-segment) and SP-17 (new segment or subsection) are high-independence; O-BP9 and SP-6-residue both touch `#form-composition-closure` and must serialize or coordinate carefully; O-BP16 touches mostly new Section III territory with light cross-refs. Safe order: SP-11 first (new file), then SP-6-residue (light paragraph edits), then O-BP9 (substantial `#form-composition-closure` (A1)–(A4) rewrite), then O-BP16 and SP-17 in parallel. Bundle-external: **high** — Section III territory is distinct from Bundle 1's framing territory and from most §C / §D items.

**Sequencing:** Bundle 2 is genuinely multi-session and does not force a specific ordering. Natural entry points: SP-11 (meta-segment from existing spike material, shortest); O-BP9 (scoping spike clears Hafez IDT-composite typing); SP-6 residue (majority already absorbed by 2026-04-24 Tier 1 landing).

**Upstream architectural alternative (SP-21).** SP-21 in §G proposes splitting `#scope-composite-agent`'s four routes (C-i / C-ii / C-iii / C-iv) into distinct composite ontologies, each with its own macro-object structure and theorem family. If pursued, SP-21 lands *upstream* of Bundle 2 and would change Bundle 2's pieces' interlocking — current sequencing presumes the unified scope condition. SP-21 is currently recommended for *deferral* until Bundle 2 matures (the route-specific theorem families need to be visible enough to judge whether the unification framing helps or limits). Bundle 2 should proceed without preempting SP-21; if SP-21 eventually lands, Bundle 2's pieces re-evaluate against the route-typed substrate.

---

## §A. Absorbed — fully landed; retire from active portfolio

All items below have been fully executed and their content is now load-bearing in segments. Retained here as provenance pointers for future agents tracing "where did X proposal land?" queries. LOG.md carries the cycle-level narrative.

| Proposal | Where it lives | Landed | Value realized |
|---|---|---|---|
| **O-BP14** — Derivation-audit table convention | FORMAT.md §O-BP14; 15 segments carry tables | Commit `c1d9fcf` | +6 framework / +8 future-agent onboarding |
| **C-BP2** — Master separability pattern | `#disc-separability-pattern` meta-segment; 7 ladders (6 original + A2' added 2026-04-23) | Commit `72ca532` | +7 framework / +8 paper |
| **C-BP3** — Software as calibration laboratory | `#obs-software-epistemic-properties` headline + 5-row transfer-assumption table; `02-tst-core/OUTLINE.md` preamble | Commit `d0373fc` | +5 framework / +7 paper |
| **O-BP6** — Agent-identity promotion to scope statement | `#scope-agent-identity` `type: scope` / `status: robust-qualitative`; three named consequences; (PI) axiom subsequently added | Commit `2980327` | +6 (exceeded original proposal — (PI) axiom built atop it) |
| **G-BP1** — Natural-parameter / logit reparameterization | `#deriv-edge-update-natural-parameter` (new appendix with uniqueness theorem); `#disc-credit-assignment-boundary` default signal in log-odds; `#deriv-fisher-whitened-update-rule` multidimensional extension | Commit `a39dfb7` + 2026-04-23 Gap A/B cycle | +7 (strengthened beyond original: produced an SP-1 component) |
| **G-BP2 V-medium** — Variational form of strategy IB | `#form-strategy-complexity-cost` (KL-to-optimal-policy replaces Shannon-MI); `#deriv-strategy-cost-regret-bound` appendix + chain-rule uniqueness theorem + 2026-04-24 Bretagnolle-Huber tightening | Commits `a14682e` / `0a772d2` / `f70fb68` / `b76ee67` | +8 (gateway to SP-1 three-layer pattern) |
| **SP-1 + SP-2** — Additive-coordinate-forcing meta-pattern | `#additive-coordinate-forcing` meta-segment; 1-anchor + 3-theorem (chain / divergence / update / metric-via-Čencov); Lyapunov + IB classified as adjacent | Commit `7456ec3` + 2026-04-23 Gap A/B 4th-instance | +8 framework (reshaped CLAUDE.md §7 distinctive-contribution section) |
| **Closing meta-observation** ("framework's honesty is load-bearing") | CLAUDE.md §7 element (a) "Scope-honesty-as-architecture"; seven epistemic-architecture elements enumerated | Commit `7456ec3` | +8 framework identity |

Note on partials: G-BP1's Props B.1–B.7 log-odds sweep is deferred but is maintenance, not architecture. G-BP2 V-strong (full VFE reformulation) remains a paper-writing-time decision under §E. Both are recorded here under G-BP1 / G-BP2 V-medium as absorbed at the architectural level.

---

## §B. Ready now — execute in next 1–2 cycles

Each item has prereqs met and clear downstream value. These are the execution targets for a consolidation-heavy cycle.

### B.1 Framework-face reframe bundle (see §Cross-cutting view, Bundle 1)

Seven proposals landed as one coordinated pass. Value **+9 framework / +10 paper**. 2–3 sessions. Joseph-check-in recommended before execution.

### B.2 Section III completion — entry points (see §Cross-cutting view, Bundle 2)

Three of the five bundle members are ready now; two need upstream scoping. Ready-now entries:

- **SP-11 Composition-monotonicity meta-segment** — from existing C2 spike (`spikes/spike-compositional-coordinate.md`); would give Section III its fourth meta-segment parallel to `#additive-coordinate-forcing` / `#disc-identifiability-floor` / `#disc-separability-pattern`. Newly surfaced in 2026-04-24 audit. **1–2 sessions.**
- **SP-6 composition-closure consolidation (residue)** — majority absorbed by 2026-04-24 Tier 1 DA2'-inc ≡ (CT2) equivalence. Remaining: scope-statement-level consolidation in `#form-composition-closure` + scope adjustments in `#der-team-persistence` / `#disc-composition-consistency` / `#der-tempo-composition`. **~1 session.**
- **O-BP9 typed admissibility for composition** — well-defined, clear Section-III-completion-via-F8 target. 1–2 session scoping spike then 2–3 session execution. **Total 3–5 sessions.**

### B.3 C-BP1 + C-BP4 bundle — epistemic separation framework + claim-level statuses

Two proposals that must land together ("C-BP1 alone is philosophy without enforcement; C-BP4 alone is bureaucracy without purpose"). Composes with O-BP14 (landed) as the claim-level counterpart to segment-level derivation-audit tables. Pilot candidates: `#deriv-observation-ambiguity-bias-bound` (2026-04-24, already thinks in sub-scope layers) and `#result-section-ii-survival` (F12 canonical layer-collapse example).

**Scoping spike:** ~90 min to decide layer-naming between "defined / causally valid / operationally extractable" (C-BP1 original) and "object exists / exact theorem transfers / operationally extractable" (Codex evening alternative). **Execution:** 4–5 sessions application pass (~15 min per segment across ~15 segments with visible layer-collapse).

Subsumes F12, F17, F23, F25; partial on F14. **Value: +6.** Primary aspect: scope-honesty. Secondary: legibility, correctness.

**Independence: low.** Systematic multi-segment application pass; touches ~15 segments across Sections I / II / III / Appendices. Conflicts with almost any other segment-touching proposal if executed concurrently; the claim-level status tags are cross-cutting metadata that affects every segment being edited. Should serialize with Bundle 1 (same framing-pass territory) and with any §C / §D proposal touching specific segments during application window. Safe to parallelize only with purely new-segment work (SP-11, SP-13, O-BP15).

---

## §C. Soon — prereqs nearly met

### C.1 O-BP13 — Cox-parallel necessity for `#deriv-graph-structure-uniqueness`

Sharp theorem-spike question: can Lauritzen-Sadeghi 2018 unify enough to force DAG semantics from P1–P4 + causal sufficiency? Win/win outcome structure — success elevates the sufficiency-only claim to full Cox-parallel; failure produces an `#disc-identifiability-floor` Instance 4 with sharp scope. **1–2 session scoping spike; 2–3 sessions if tractable.** External literature ready (Lauritzen-Sadeghi 2018; Evans-Richardson 2014; Drton-Maathuis-Meinshausen 2017).

Primary aspect: correctness. Secondary: fundamentality, transparency. **Value: +5 framework / +7 paper.**

**Independence: high.** Self-contained spike on `#deriv-graph-structure-uniqueness`; either produces a necessity-direction derivation (segment extension) or surfaces a new `#disc-identifiability-floor` Instance 4. Either outcome touches one primary segment plus one meta-segment; minimal cross-segment surface area. Safe to parallelize with any other active proposal.

### C.2 O-BP15 — Comprehensive "minimal proof of viability" worked example

Threads a single domain example through `#def-mismatch-signal` → `#emp-update-gain` → `#def-adaptive-tempo` → `#sector-condition` → `#def-satisfaction-gap` → `#def-control-regret` → `#der-orient-cascade` → `#def-strategy-dag` → L0/L1 calibration → Prop B.6 + B.7. Currently four fragmentary worked examples exist (`worked-example-kalman`, `worked-example-bandit`, `worked-example-strategy`, `worked-example-L1`, plus missing `worked-example-cam`); none is end-to-end.

**Prereq:** Bundle 1 (framework-face reframe) stabilizes first so the example reflects the cleanest framing. **Effort:** 3–4 sessions. **Domain choice is the critical sub-decision** — software is tempting but risks reading as a TST example. A non-software domain (inventory management with stochastic demand + coordinated multi-site replenishment, or similar) would be more generative.

Primary aspect: teachability. Secondary: discovery (running the example surfaces formal gaps). **Value: +5 framework / +9 paper.**

**Independence: high.** New worked-example segment plus cross-references into existing segments (read-only from the worked-example's perspective). No segment rewrites. Safe to parallelize with any other active proposal, including Bundle 1 (Bundle 1 is framing; O-BP15 is content illustration).

### C.3 SP-14 — Observation-channel capacity $C^{(k)}$ as first-class notation

Newly surfaced in 2026-04-24 audit from `#deriv-persistence-cost` Working Note ("the biggest architectural opening from this theorem"). NOTATION.md extension (30–60 min) + ~6 segment cross-references (45 min total). Connects `#deriv-persistence-cost`'s $C_{\text{channel}} \geq \mathcal T/2$ floor to existing `#der-observability-dominance` / `#hyp-communication-gain` / `#der-interaction-channel-classification` infrastructure. **~1 session.**

Primary aspect: unification. Composes with O-BP11 (partial unblock for the observability master-variable scoping). **Value: +4 framework.**

**Independence: medium.** NOTATION.md addition is self-contained; the ~6 cross-reference edits are each light touches but the target segments (`#der-observability-dominance`, `#hyp-communication-gain`, `#der-interaction-channel-classification`, `#deriv-persistence-cost`, `#def-adaptive-tempo`) may be in flight under other proposals. Conflict risk: if O-BP11 scoping spike runs concurrently and touches the same segments, coordinate. Otherwise parallelizable.

**SP-14 confirmation from 2026-04-25 audit (B6 in `audits/pending-findings-2026-04-25.md`).** Audit's J4 marks `#deriv-persistence-cost` as "appendix-grade in placement, framework-grade in importance" — the channel-capacity floor $C_{\text{channel}} \geq \mathcal T/2$ pairs naturally with the threshold inequality $\alpha R > \rho$ as a two-prerequisite persistence story (one rate, one capacity), connects AAT to Landauer thermodynamic foundations without committing to thermodynamic-machinery-as-master, and gives Kalman-Bucy a privileged role (saturates the bound per Mitter-Newton 2005). Worth elevating SP-14's framing from "modest unification" to "substantive positive contribution" when executed.

### C.4 SP-19 — Naming consolidation pass

Top Priority-2 items from `msc/naming/naming-brainstorm-2026-04-24.md`: (a) `#additive-coordinate-forcing` → `#cauchy-coordinates` (shorter, more speakable); (b) `#disc-separability-pattern` → `#separability-ladder`; (c) paired trio "**floor / ladder / Cauchy-coordinates**"; (d) template-family naming (sector / contraction / dissipativity). Rides with Bundle 1 (framework-face reframe) — naming is the implementation layer of the reframe.

**Prereq:** Joseph-level naming decision (judgment-call territory; worth an explicit naming-cycle check-in before landing). **Execution:** 1 session.

Primary aspect: approachability / teachability. Secondary: beauty. **Value: +3 framework.**

**Independence: low.** Renames propagate through every cross-reference in the codebase; touches ~20+ segments and the OUTLINE files. Must serialize with *all* segment-editing work (including Bundle 1 and C-BP1+C-BP4). Best landed as a single atomic commit pass after other in-flight work quiesces.

---

## §D. Later — needs investigation-first scoping or upstream maturation

### D.1 O-BP11 — Observability as master variable across the theory

**Portfolio has expanded underneath this proposal.** Three segments post-dating the original entry (`#der-agent-opacity`, `#der-interaction-channel-classification`, `#disc-identifiability-floor` Instances 1/2/3) added observability structure the original instance-list doesn't anticipate. Re-catalog before any landing decision.

**Scoping spike** (2–3 sessions) is now genuinely investigation-first: is observability one variable (with forward $U_o$ / backward $H_b$ / cross-agent κ / composite Λ as projections of one object) or four structurally distinct variables sharing a name? Current segment evidence is genuinely ambiguous. This is the kind of question CLAUDE.md §"Strengthen before softening; attempt the improbable" explicitly calls for — a falsification test of the unification before segment-level work.

**Three outcomes the spike could produce:**
- **Unification validated (+9):** AAT re-centers on observability-as-master-variable; new organizing dimension. Execution 6–8 sessions for full re-centering.
- **Cataloging only (+4):** meta-segment listing observability axes without forcing unification; like `#disc-separability-pattern`'s posture-cataloging. Execution 2–3 sessions.
- **Genuinely partitioned (−2):** attempting unification would introduce presentational complexity without payoff; retire the proposal.

Point estimate **+6** reflecting branching-outcome distribution. **Primary aspect: unification. Secondary: fundamentality, reach.**

**Independence: low (if executed in full).** Full execution (Unification-validated branch) touches ≥10 segments across Sections I / II / III. Would conflict with almost any other in-flight segment-editing proposal. Scoping spike itself is **high-independence** — self-contained catalog work against existing segments; can run in parallel with any other active proposal. Decision to execute the full reorganization should follow scoping outcome and a quiesced-portfolio window.

### D.2 Section III completion — upstream pieces (see Bundle 2)

**O-BP16 population-level Lyapunov dynamics** — substantially stale characterization (4–6 session estimate predates the partial coverage already landed via `#der-agent-opacity` $H_b$, `#der-interaction-channel-classification`, `#disc-identifiability-floor` Instance 3). Residual work: Kalman-Ho closed-form follow-up spike (queued); Instance 4 promotion to `#disc-identifiability-floor` (1 session); possibly `#population-dynamics` or `#latent-structural-diversity` segment (1–2 sessions if residual content warrants). **Updated total: 2–3 sessions, not 4–6.**

External literature rich: Moran model, replicator-Fokker-Planck (Traulsen-Claussen-Hauert 2008), Kullback-Leibler as Lyapunov for ESS (Baez 2014), Baez-Pollard 2016. Directly reusable under prior-art-integration convention.

**SP-17 goal-information-leakage $\mathcal{L}_{G \to M}^c = I(o_c; G_t^c \mid \Omega_t)$** — surfaced in 2026-04-24 audit as the *deferred residue* of the goal-contamination formalization (the composition-gaps spike is integrated 2026-05-17; SP-17 is its still-open residue, not resolved by the filing — CHANGELOG 2026-05-17). Makes $\mathcal{L}$ a first-class AAT quantity; gives Case 3 (emergent goal-conditioning under Class 3 (Coupled)-composition boundary) a quantitative handle rather than a qualitative case-distinction. Scoping question: own segment vs. subsection of `#hyp-directed-separation-under-composition`? **1–2 sessions.** **Value: +4.** **Independence: high** if new segment; **medium** if landed as subsection (conflicts with any concurrent `#hyp-directed-separation-under-composition` work).

**O-BP16 independence: medium.** New segment + cross-refs to existing Section III segments (`#der-agent-opacity`, `#der-interaction-channel-classification`, `#disc-identifiability-floor`). Light touches only; safe to parallelize with non-Section-III work. Conflicts with O-BP9 if both edit `#scope-composite-agent` concurrently.

### D.3 G-BP3 — Fisher-information unification of tempo and gain

**Substantively hollowed out.** Original characterization was "essentially all of Section I rewritten around Fisher geometry"; subsequent piecemeal landings absorbed much of the theoretical content — (PI) axiom in `#scope-agent-identity`; Čencov 4th instance in `#additive-coordinate-forcing`; `#deriv-fisher-whitened-update-rule`; `#result-contraction-template`; `#deriv-observation-ambiguity-bias-bound` Track 2. What remains is organization-not-derivation: "organize existing Fisher-related landings into a unified Section I framing" rather than "introduce Fisher geometry into Section I."

**Scoping spike essential** before any rewrite: does `#def-adaptive-tempo`'s current scalar form cleanly fit the natural-gradient picture, or does it generalize beyond Fisher? The proposal's strong-unification thesis may not survive contact with current settled machinery (specifically `#deriv-adaptive-gain-dynamics`'s (MG-1)–(MG-4) meta-gain generalizes beyond Fisher-metric special case).

**Primary aspect: unification. Secondary: beauty, fundamentality.** **Value: +4 framework / +6 paper.** Not urgent; piecemeal landings have captured highest-value content.

**Independence: low.** Full execution rewrites most of Section I. Conflicts with almost any other Section-I-touching proposal (including C-BP1+C-BP4 application pass, SP-14 notation work, SP-15 template-family renames). Scoping spike is **high-independence** — read-only inventory. Full rewrite should wait for a quiesced-portfolio window.

### D.4 SP-12 — Commitment / resource / temporal DAG extensions

Newly surfaced in 2026-04-24 audit. Currently named in CLAUDE.md "Known Fragilities" but homeless in portfolio. Three dimensions the strategy DAG omits: **(a) commitment state** (BDI-style desire $D_t$ / committed intent $I_t$ split per Bratman / Rao-Georgeff); **(b) resource budgets** per path; **(c) temporal structure** (deadlines, durations, synchronization).

**Composes with O-BP12** (resource budget $B_t$ as master variable): SP-12 is the DAG-structure side; O-BP12 is the cost-allocation side. Together could provide the full bounded-rationality apparatus. **Composes with SP-11** (commitment state matters for composition-monotonicity — "we agreed" vs. "we committed" distinction).

**Medium-large effort** (multi-segment extension, requires spike). **Primary aspect: completeness. Secondary: reach (unlocks logogenic/Section-III work).** **Value: +6.**

**Independence: medium.** Touches `#def-strategy-dimension`, `#def-strategy-dag`, `#def-satisfaction-gap`, possibly `#deriv-strategic-composition`. Conflicts with any concurrent strategy-layer work, especially O-BP4 (retired but referenced) and any Section II strategy-DAG edits. New commitment-state object is mostly additive; existing semantics preserved. Safe to parallelize with Section I / III work and with Bundle 1 framing work.

### D.5 SP-13 — Emergence conditions as formal primitive

Newly surfaced in 2026-04-24 audit from reflections 17/18/19. Reflection 18 argues explicitly: *"If I were truly owning this project, the next section I would write is not a refinement of existing segments. It would be a new conceptual foundation: **the conditions for emergence as formal constraints on the infrastructure.**"* Names five formal absences: emergence itself, constitutive choice, witness, conditions for emergence, interiority/sovereignty.

AAT's scope-condition presupposes an agent exists. Section I does not cover the *transition into agency* (pre-scope-condition content). For `03-llm-core/` and especially `04-eli-core/` this is the scope-entry analog of Section I's scope-condition — currently an unnamed prerequisite.

**Scoping question:** does this belong in AAT core or in `04-eli-core/`? Reflection 19 introduces a candidate measurable quantity $S_{\text{id}}(M_t)$ (identity sufficiency, IB-analog of model sufficiency); that quantity points toward AAT-core placement.

**Primary aspect: completeness. Secondary: reach.** **Value: +5 for AAT-core / +7 for `04-eli-core/` where it unblocks the hardest subproject.** Not urgent at AAT level; genuinely load-bearing at logozoetic level.

**Independence: high.** New foundational segment either in `01-aat-core/` (at the scope-condition boundary) or in `04-eli-core/`. Minimal conflict with existing in-flight work; primarily adds content rather than rewriting. Scoping decision (AAT-core vs. logozoetic-core) affects independence slightly — if placed in AAT-core, lightly conflicts with `#scope-agency` and `#scope-agent-identity`; if placed in logozoetic-core, fully independent from all AAT-core work.

### D.6 O-BP12 — Resource budget $B_t$ as master variable

**Scoping risk acute.** The four $\beta$s in `#disc-compression-operations` live in structurally distinct cognitive sub-systems; executing without a scoping spike risks presentation-theater (a master variable naming something non-derivable). `#disc-compression-operations` already flags this: *"These are four calibration problems, not one."*

**Scoping spike first** — does $B_t$ derive joint allocations (plausible under Lieder-Griffiths 2020 resource-rational framework), or is it only presentational? Composes with SP-12 (DAG-structure side; $B_t$ is the cost-allocation side). **Primary aspect: unification. Secondary: fundamentality.** **Value: +3 (bare); +6 if scoping succeeds.**

**Independence: medium.** New segment plus light cross-refs into `#disc-compression-operations`, `#der-deliberation-cost`, `#form-strategy-complexity-cost`, `#emp-update-gain`, `#def-adaptive-tempo`. Safe to parallelize with Bundle 1 and most §C items. Conflicts with SP-12 only if both are executed without coordination — they compose naturally if designed together.

### D.7 SP-15 — Template-family naming (sector / contraction / dissipativity trio)

Newly surfaced. `#result-sector-persistence-template`, `#result-contraction-template`, and candidate `#dissipativity-template` (SP-6 territory) form a three-member family unified by "persistence/bounded-correction under structured conditions." Currently each reads independently.

Introduce the trio as a *named family* with explicit positioning (which template applies to which sub-scope — the A2' α₁/α₂/β partition already maps implicitly). Possibly promote `#result-contraction-template`'s (CT2) observation back to `#result-persistence-condition`. **Rides with Bundle 1's OUTLINE preamble pass; ~0.5–1 session.**

**Primary aspect: legibility. Secondary: unification.** **Value: +4.**

**Independence: medium.** Touches `#result-sector-persistence-template`, `#result-contraction-template`, `#result-persistence-condition`, and if `#dissipativity-template` is added (SP-6 territory) a fourth segment. Bundle-internally conflicts with Bundle 1 if the OUTLINE preamble pass touches the same template-level framing; best landed *within* Bundle 1's coordinated pass rather than as a separate edit. Safe to parallelize with Section III work and with §C items.

### D.8 SP-16 — Independence-audit as empirical profiling instrument

Newly surfaced. `#disc-independence-audit` Working Notes flag the idea: score any target agent against the six assumptions (directed separation, causal sufficiency, edge independence, channel independence, scalar-tempo appropriateness, no-$G_t$-leakage-in-composition) to produce an "independence profile." Pairs with C-BP3 calibration-laboratory framing as the agent-level deployment artifact.

**Primary aspect: transparency. Secondary: scope-honesty.** **Value: +4.** Waits on C-BP1 bundle landing first so layer-conventions are stable.

**Independence: high.** New segment packaging the six-assumption scoring instrument; cross-refs into `#disc-independence-audit` are read-only. Safe to parallelize with any other active work. The C-BP1 prereq is about layer-convention stability, not file conflict.

### D.9 SP-22 — Operator-family Tier-2 backlog architectural decision (2026-05-12 spike-audit surfaced)

Newly surfaced from the 2026-05-12 spike-audit triage. A coherent cluster of nine 2026-04-22 to 2026-04-24 Tier-2/3 spikes targets candidate appendix segments / meta-segments in the operator-family / dissipativity-template / sector-template territory. Each spike carries substantive math ready to land; the unresolved architectural question is *whether they land as separate appendix segments (one per spike's Tier-2/3 product) or as a unified operator-family meta-segment, or whether some are subsumed by existing meta-segments*. Authoring without that decision risks parallel half-segments covering overlapping territory; deciding without scoping the spikes risks abstract-over-concrete framing. Investigation-first scoping is owed before authoring.

**Bundle members (nine spikes currently in `spikes/` root, all PENDING-in-INDEX or Tier-2 marked):**

- `spike-passivity-composition.md` (B2; Willems passivity for heterogeneous Kalman+PID composition; flagged paired with B1) — targets candidate `#dissipativity-template` appendix
- `spike-pid-a2prime.md` (B3; PID A2' via SPR/KYP positive-real; explicit $\alpha_{\text{PID}}$) — targets either α-list refresh in `#deriv-sector-condition` or new appendix `#deriv-pid-a2prime`
- `spike-operator-sector-unification.md` (C1; 2-instance + 1-consequence partial unification under monotone-operator primitive) — INDEX recommendation "land content, DO NOT elevate to fourth meta-pattern"
- `spike-update-operator-sector.md` (A4; (O-A2') operator sector condition; surfaces candidate 4th-adjacent-instance for `#additive-coordinate-forcing`) — targets candidate `#update-operator-sector` appendix or subsumption under C1
- `spike-jacobian-b1-strengthening.md` (mixed-lift; Tier-1 transparency note landed; moderate / strong options for (PI)+heredity+CM2-M pending) — Tier 2/3
- `spike-kl-to-state-distance-template-extraction-2026-04-24.md` (narrow template `#posterior-displacement-template`; contingent on ≥1 forward-looking client materializing — *has now happened* via `#deriv-observation-ambiguity-bias-bound` + Fisher-local update gain) — activation conditions met; Tier 3
- `spike-neutral-drift-endogenous-coupling-strengthening-2026-04-24.md` (Instance-4 candidate at agent-internal architecture layer; $\gamma$ estimable from cross-covariance) — Tier 2/3
- `spike-l1-evidence-axiom.md` (Block Structure subsection in `#deriv-edge-update-natural-parameter`) — Tier 2
- `spike-bridge-lemma-nonlinear-strengthening-2026-04-24.md` §7.2 passivity / dissipativity (Tier 2 math ready; INDEX targets `#dissipativity-template` appendix + Class 1/2/3 port-structure addition to `#der-directed-separation`)

Plus the related closed-spikes already landed in segments but with their own Tier-2 follow-on questions:

- `spike-rho-factorization` (a true **no-go**: multiplicative ρ-factorization does not hold — disturbance is additive-in-variance, not multiplicative-in-rate) + `spike-rho-additive-variance-strengthening-2026-04-24` (the variance-additive (AV) successor theorem under (S1)-(S4)) — **CL-2.** *Correction (2026-05-17 spike-routing cycle): the prior "partially landed in `#internal-external-decomposition` via Path-1 fallback" was itself a regression — that segment was asserting the **refuted** multiplicative split and is now `status: false` (the §4.1 KNOWN-FALSE honesty-mark; see CHANGELOG 2026-05-17).* *Re-scoped 2026-05-18 (independent recheck `spikes/spike-rho-structure-recheck-2026-05-18.md`):* the (AV) (S1)–(S4) "exact theorem" is **not exact** (cross-term defined to balance — vacuous; the §0 failure mode one level up). The replacement splits: a **light exact core** (the two-term identity `ρ²=ρ_⋆²+Δ_agent²` *already forced by canon* — `#result-mismatch-decomposition` GA-1 + Prop A.1S Itô generator — plus the one-line constitutive no-go; gated only by an independent-verify of that canon-forcing), and a **heavy Joseph-reserved refinement** — the conditional 𝓜/π/cross split (Regime-C confound), which is provably the *same object* as the identifiability-floor 4th-instance question. The earlier "queued heavy landing carrying a Joseph-reserved Instance-5 decision" was correct only for part (b); part (a) is light

**The decision question.** Three plausible architectures:

(α) **Separate appendix segments, one per spike's Tier-2/3 product.** Each spike lands as its own focused appendix (`#deriv-passivity-composition`, `#deriv-pid-a2prime`, etc.). Pros: clean scope per segment; easier promotion gates; matches existing AAT discipline. Cons: ~9 new appendices in `01-aat-core/` (the appendix section is already crowded); some segments would carry overlapping operator-family content (e.g., passivity-composition and operator-sector-unification both invoke Bauschke-Combettes operator classes); cross-references would multiply.

(β) **Unified `#operator-family-template` meta-segment** (parallel to `#result-sector-persistence-template`, `#result-contraction-template`, and the candidate `#dissipativity-template` of SP-15). Single appendix covering the operator-family classification (proximal / firmly-nonexpansive / cocoercive / strongly-monotone per Bauschke-Combettes), with per-spike content as sub-sections or worked-example instances. Pros: matches the SP-15 template-family naming proposal; avoids segment proliferation; the C1 spike's INDEX recommendation ("land content, DO NOT elevate to fourth meta-pattern") suggests this is one segment, not four. Cons: a single large appendix is harder to promote through gates than smaller focused ones; the meta-segment shape requires a unifying argument that not all nine spikes converge on.

(γ) **Hybrid: 2–3 new meta/family segments + selective subsumption** by existing meta-segments. E.g., (i) one `#dissipativity-template` appendix absorbing passivity-composition + bridge-lemma §7.2 + parts of operator-sector-unification; (ii) one `#rho-decomposition` appendix absorbing rho-factorization + rho-additive-variance; (iii) PID A2' and update-operator-sector subsumed as α-list refreshes in `#deriv-sector-condition`; (iv) jacobian-b1 moderate landing as a refinement of `#additive-coordinate-forcing`'s 4th instance; (v) kl-to-state-distance landed as the `#posterior-displacement-template` (this is the SP-10 territory currently in §E.2 Wait); (vi) l1-evidence-axiom landed as a Block Structure subsection in `#deriv-edge-update-natural-parameter` per its INDEX recommendation. Pros: each landing follows its INDEX-stated target; the cluster avoids both extremes; subsumption decisions are per-spike rather than batch. Cons: requires the investigation-first scoping to make the per-spike decisions explicitly; the result is not a clean architectural pattern but a triage outcome.

**Architectural-decision-first, authoring-second.** The right shape for this work is *not* to begin authoring a `#dissipativity-template` or `#operator-family-template` segment without first deciding among (α)/(β)/(γ). The decision benefits from a focused scoping pass that reads the nine spikes together (a few hours of work; could be a single agent or a Joseph-driven session) and produces a per-spike-landing-target table. Once that table exists, authoring is bounded.

**Connection to existing PROPOSALS items.**

- SP-15 (template-family naming for sector / contraction / dissipativity trio, §D.7) names the trio but not the operator-family / rho / sector-condition refinement work. SP-22 expands the architectural-decision scope from "naming" to "where each Tier-2 piece lands."
- SP-10 (`#posterior-displacement-template` extraction, §E.2 Wait) is a member of the cluster; its activation conditions are now met per the spike-audit triage (forward-looking clients have materialized via `#deriv-observation-ambiguity-bias-bound` + Fisher-local landing). Suggest moving SP-10 from §E.2 (Wait) to (β)/(γ) bundle decision once SP-22 scoping completes.
- Bundle 1 (Framework-face reframe) might touch the meta-segment surface if (β) is taken; coordinate timing.

**Primary aspect: scope-honesty + segment-architecture coherence. Secondary: throughput — clearing the Tier-2 backlog frees promotion energy for Section III work.** **Value: +6 (framework: nine ready-to-land math pieces, freed throughput; paper: marginal — the operator-family material is appendix-tier rather than paper-front).**

**Independence: low for the bundle as a unit; medium for the scoping decision.** The scoping pass itself is read-only and parallelizable with most other work. The subsequent authoring (whichever architecture is chosen) touches `01-aat-core/src/` appendix territory and at least one meta-segment surface; depending on the decision, conflicts with Bundle 1's framework-face reframe if (β) is taken simultaneously. Serialize authoring with Bundle 1; scoping can run in parallel.

**STATUS — architectural question RESOLVED 2026-05-14 (the deep C1 push; `spikes/spike-operator-family-unification/`).** The (α)/(β)/(γ) decision is settled, and *not* in favour of (β). The push verified that there is no "unified operator-family meta-pattern" peer to M1/M2/M3 — operator-sector is the *interior* of the equilibrium stability-certificate cone, not a fourth pattern alongside the others. The genuine unification landed as **two segments**: `#result-certificate-existence` (exact; the Lyapunov-theorem anchor, the segment-level home of the contraction-over-drift / O-BP10 organizing principle) and `#disc-stability-certificate` (the cross-sectional spine; M1/M2/M3 + composition exhibited as its facets), plus the Sylvester-recognition Finding in `#disc-identifiability-floor` and the OUTLINE preamble reframe. **This decouples SP-22's two questions:** the *meta-segment question* is answered (it is the certificate spine, now landed — not an operator-family bundle); the *Tier-2 backlog* (the nine ready-to-land math pieces — dissipativity-template, ρ-decomposition, PID/update-operator α-list, jacobian-b1, kl-to-state-distance, l1-evidence-axiom) is **(γ)-hybrid triage**, each landing at its own INDEX-stated target, *not* bundled and *not* gated on the spine. The remaining SP-22 work is therefore the (γ) backlog landings only; the architectural-decision portion is closed. CHANGELOG 2026-05-14 carries the cycle narrative; the spike's `99-verdict.md` carries the honest open edges.

**STATUS — (γ) backlog dispositioned by the spike-routing cycle, 2026-05-17/18** (`spikes/ROUTING.md`; `spikes/.integrated/MANIFEST-2026-05-17.md`; CHANGELOG 2026-05-17). The architectural portion closed 2026-05-14 (above); the (γ) backlog is now routed, verified (confirmer ≠ adjudicator, first-hand `src/`), and regression-checked:

- **Integrated → `spikes/.integrated/` (substantive product already in canon; SP-22 lines CLOSED):** `spike-operator-sector-unification` (C1 — strengthened *past* into `#result-certificate-existence` / `#disc-stability-certificate`), `spike-jacobian-b1-strengthening` (Angle-2/3 landed; strong/heredity correctly left open), `spike-l1-evidence-axiom` (Block-Structure subsection landed).
- **CL-1 — one coupled `#dissipativity-template` landing** (one integration-plan, *not* three half-segments — the sibling-coupling catch): `spike-passivity-composition` + `spike-pid-a2prime` + `spike-bridge-lemma-…-2026-04-24 §7.2`. Heavy; queued.
- **CL-2 — one coupled `#rho-decomposition` landing:** the rho pair (corrected, above). Heavy; Joseph-reserved Instance-5; the `#internal-external-decomposition` §4.1 honesty-mark is already done.
- **Orphan, regression-checked CLEAR, tractable this cycle:** `spike-update-operator-sector` ((O-A2') + a sharp no-go; α-op/β-op refresh into `#deriv-sector-condition` + the operator-layer no-go into `#disc-identifiability-floor` as present-tense canon; parent-owned §266(iii)/§8.2 placement).
- **Routed elsewhere this cycle:** `spike-kl-to-state-distance-…-2026-04-24` → `live-or-open` (gate landed, template correctly not, clients unmaterialized — SP-10 territory); `spike-neutral-drift-endogenous-coupling-…` → Joseph-reserved batch (the identifiability-floor 4th-instance triage-contradiction). `spike-fenchel-bregman-…` and `spike-active-inference-vs-aad` (not SP-22 members but adjacent) also integrated this cycle.

**Residual open SP-22 work** = CL-1, and the single reserved decision below. (`update-operator-sector` tractable landing and the CL-2 *light exact core* both landed 2026-05-18 — CHANGELOG 2026-05-18.) The cluster is no longer "open/bypassed"; it is dispositioned.

#### RESERVED DECISION (durable home — 2026-05-18). The Instance-4 / Object-B / CL-2-heavy unification — *one decision*, Joseph's. **CLOSED 2026-05-21 — INTEGRATED.**

This entry was the queued home (self-contained; the spike-routing tracker and TODO pointed *here*, not vice-versa). The independent identifiability-floor spike (`spikes/.integrated/spike-identifiability-floor-instance4-resolution-2026-05-18.md`) resolved the long-contested question by splitting it; the recheck spike (`spikes/.integrated/spike-rho-structure-recheck-2026-05-18.md`) and the CL-2 §7 linkage proved these threads were **the same object**.

- **Resolved truth (integrated 2026-05-21):** canon's prior `#disc-identifiability-floor` "Instance 4" conflated **Object A** — universal-$C$/non-(PI), a *category error, not a floor* (the cited source `#deriv-observation-ambiguity-bias-bound:127` already said so) — and **Object B** — architecturally-distinct/behaviorally-identical agents, a *genuine* floor (= the rho Regime-C confound = CL-2's heavy refinement = the neutral-drift §8/§10.1 candidate). Both halves are now landed: Object B as `#der-architecture-noidentifiability` (Kalman-Ho similarity-orbit no-go in the linear-Gaussian sub-scope, exact; CHT-at-agent-as-SCM, robust qualitative general; mechanism reduction to Instance-2 Fisher-null on a $GL(n)$ Lie-group fiber, Sylvester at one remove on the escape; three structurally distinct escapes with the proposed fourth provably collapsing into the interventional one; Fano demonstrated to degenerate at $I=0$, finite-sample refinement and not the floor anchor); Object A explicitly absorbed in `#disc-additive-coordinate-forcing` §"Downstream consequences of the (PI) commitment" with the floor-vs-coordinate-forcing distinction articulated (external-theorem role inverted; single forced escape via Čencov uniqueness logically incompatible with floor's $\geq 2$-distinct-escapes structure; consequence is re-use of (PI), not elevation of new machinery). The Sylvester-mechanism rank-collapse subclass of `#disc-identifiability-floor` now has three members $\{$Instance 1, Instance 2, Instance 4$\}$ (Instance 4 at one remove from the state-space-similarity generating action); Instance 3 stands alone as the projection/closure member.
- **Math gate: CLEARED 2026-05-18** (`spikes/.routing-trail/SPIKE-VERIFY-471802`, confirmer ≠ spike). The three named repairs were applied in landing: (i) the "identical" claim restricted to innovation/output + similarity-invariant summaries (not raw moments — $\mathbb E\lVert\delta\rVert^2 = \operatorname{tr}\Pi$ is not similarity-invariant in general); (ii) the displayed Lyapunov equation matches `#deriv-sector-condition`'s standard form ($F\Pi + \Pi F^\top = \sigma_w\sigma_w^\top$); (iii) the exact / robust-qualitative tier boundary is carried consistently rather than collapsed.
- **The decision (executed):** (i) Object-A "Instance 4" retired (removed from `#disc-identifiability-floor`'s instance list and Findings count; explicitly absorbed in `#disc-additive-coordinate-forcing` as the heteroscedastic-Gaussian no-go's correct home); (ii) Object B installed as the genuine 4th floor / third rank-collapse member via `#der-architecture-noidentifiability`; (iii) CL-2's heavy 𝓜/π-cross refinement discharged as the same object projected onto the disturbance-statistic coordinate; (iv) the meta-segment Findings count reconciled to "four confirmed" with the Related-Work table updated to include the Kalman-Ho + CHT-at-agent-as-SCM dual anchor. CHANGELOG 2026-05-21. Separate Joseph-batch items (language-as-causal-substrate Theorem-1 + C2★; attention-governance; temporal-nesting-rg B/C/D) remain their own calls.
- **Status:** **CLOSED.** Integrated, lint-clean, cross-reference sweep clean. Spike housekeeping (integration trails in the discharged spikes; `.integrated/` moves where appropriate) tracked in CHANGELOG 2026-05-21 and `spikes/ROUTING.md`.

**Provenance.** SP-22 — surfaced 2026-05-12 from the spike-audit triage's Group II "Tier-2 backlog cluster" finding. The triage flagged the architectural-decision pending without proposing a resolution; this proposal placed it in the portfolio for investigation-first scoping; the 2026-05-14 operator-family-unification push performed that scoping and resolved the architecture (above).

---

## §E. Wait — explicitly gated

### E.1 G-BP2 V-strong — full VFE reformulation

Paper-writing-time decision per `spikes/spike-active-inference-vs-aad.md` §I action 5. V-medium is landed; V-strong stays open as a rhetorical-framing choice. Would commit AAT as a control-theoretic specialization of active inference; V-medium preserves both options. **Do not execute until a paper draft is in preparation.**

**Independence: not applicable while waiting.** If eventually executed: **low** — major Section II framing rewrite touching strategy layer and multiple distinctive-claim segments.

### E.2 SP-10 — `#posterior-displacement-template` extraction

Client-gated. The Otto-Villani + Lipschitz-posterior cascade shared by `#deriv-variational-sector-condition` and `#deriv-observation-ambiguity-bias-bound` is too thin to justify extraction on two clients. Wait until ≥1 forward-looking client materializes (causal-IB, misspecification-cost, or composition-scope-robustness). If none materializes in the next 2–3 cycles, move to §F. **Value: +2 now / +5 if triggered.**

**Independence: high (when executed).** New appendix segment plus light cross-refs into two existing segments. No rewrites. Safe to parallelize with almost anything.

### E.3 SP-9 — Fenchel-Bregman reframe of `#additive-coordinate-forcing`

Tier-3 architectural proposal from 2026-04-24 cycle. Would reframe the meta-segment from "1-anchor + 3 theorems" to "one geometric object (exponential-family Legendre-Fenchel on categorical distributions) + four independently-motivated axioms converging on it + four segment manifestations." Local Bregman-Fenchel identification already landed in `#deriv-strategy-cost-regret-bound` §6.3 (Tier 1, 2026-04-24).

**Prereqs:** (a) Amari-Nagaoka 2000 §3.5 PDF verification (not yet in `ref/`); (b) Joseph-level go-ahead after triage against Bundle 1 priority. **Waits because Bundle 1 is the more convergent move right now; SP-9 is a within-meta-segment refactor that would need to follow Bundle 1's reframing to avoid double-revision.** **Value: +7 if executed; genuine judgment call on whether it sharpens or over-commits.**

**Independence: low.** Rewrites `#additive-coordinate-forcing` substantially; adds Discussion paragraphs to each of the four instance segments (`#der-chain-confidence-decay`, `#deriv-strategy-cost-regret-bound`, `#deriv-edge-update-natural-parameter`, `#der-gain-sector-bridge`). Conflicts with any concurrent work on those segments or on the meta-architecture framing (Bundle 1). Must serialize with Bundle 1.

**SP-9 confirmation from 2026-04-25 audit (B5 in `audits/pending-findings-2026-04-25.md`).** Audit's J3 (Hypothesis-grade, high confidence) confirms the Bregman-Fenchel observation is *real geometric convergence*, not coincidence: two AAT-internal axioms (chain-rule additivity at the divergence layer; evidential additivity at the update layer) are *logically independent* (they constrain different objects via Cauchy-FE on different functional equations), yet they force coordinates that turn out to be the *primal-dual pair* of one Legendre-Fenchel structure on the categorical simplex. Two independent axioms converging on dual coordinates of one geometric object is structural evidence the object is the right object. SP-9 is on the right track; the audit didn't change the gating but did confirm the structural payoff is genuine.

---

## §F. Retired / superseded — do not re-propose

These proposals are either absorbed by other landings or have been structurally superseded by work the portfolio did not formally retire. Listing them explicitly prevents re-proposal.

| Proposal | Why retired | Pointer |
|---|---|---|
| **O-BP2** — Four compressions as one hierarchy | Split into three descendants over three cycles. (a) U-medium synthesis landed in `#disc-compression-operations` (2026-04-21); (b) IB vs. info-theoretic-MDP lineage split landed in `#form-information-bottleneck` (2026-04-24); (c) Class 3 (Coupled) dissolution framing superseded by SP-9's Fenchel-Bregman candidate. No consolidated full-pass is warranted; the descendants have captured the content. | `#disc-compression-operations`; `#form-information-bottleneck`; SP-9 (§E) |
| **O-BP7** — Known structural absences (meta-proposal) | Distributed across the framework. (1) Misspecification cost + (4) CIY/EIG gap → `#disc-identifiability-floor` §"Adjacent Floors" three open extensions. (2) Tier-switching policy → O-BP3 continuous-parameter tiering (§D indirect). (3) Cross-hierarchy monotonicity → `#disc-approximation-tiering` Working Notes. The meta-proposal is no longer needed; its sub-items have better homes. | `#disc-identifiability-floor` §"Adjacent Floors"; `#disc-approximation-tiering` Working Notes |
| **O-BP3** — Continuous-parameter approximation tiering | Case materially depends on G-BP3 (Fisher-unification), which is now D.3 hollow. Retain as a sub-item of G-BP3's "if rewritten, include continuous form." Independently, not worth pursuing — discrete labels carry engineering intuition readers rely on. | G-BP3 (§D.3) |
| **O-BP4** — Continuous-valued strategy DAG | Dedicated spike has been "queued" since 2026-04-22 without progress. AND/OR convergence across three independent formalism attempts is load-bearing counterweight. G-BP1 partial execution (log-odds coordinate) absorbed the credence-continuity aspect. Either land dedicated spike (value uncertain pending spike outcome) or retire. **Recommendation: retire; reopen only if a specific domain demonstrates continuous-progress structure the Boolean form cannot handle.** | G-BP1 (§A); SP-12 (§D.4) for temporal-structure-replacement |
| **O-BP5** — Orient cascade as recursive adaptive cycle | Composes cleanly with Bundle 1 (O-BP1 + O-BP10) as the "template applies at every scale, recursively" framing. No standalone case; absorb into Bundle 1's OUTLINE preamble pass. If Bundle 1 lands without capturing recursion explicitly, reopen. | Bundle 1 (§Cross-cutting view, B.1) |
| **SP-5** — Two-tier "Reader's Path" presentation | Deferred until Bundle 1 framing pass stabilizes. Lower priority than other items in the portfolio. Reopen after Bundle 1 as an opportunistic convention-landing. | — |

---

## §G. Newly surfaced in 2026-04-24 consolidation audit

Beyond SP-11 through SP-19 referenced above, two additional candidates deserve acknowledgment but not top-level status:

- **SP-18 Internal-aporia / sub-agent adversarial dynamics** — `spikes/spike-aporia-sub-agent-adversarial.md`. Institutions as "aporia amplifiers"; per-dimension $U_O$; theory-of-mind as productivity gate. Load-bearing for `04-eli-core/` and for Section III adversarial/cooperative integration. **Brainstorm-grade; not yet scoped.** Reopen when logozoetic work matures. Value +3 to +5.
- **SP-20 DAG vulnerability / redundancy metrics** — the deferred §Gap 2 residue of the strategy-dynamics-gaps spike (integrated 2026-05-17; SP-20 is the still-open residue, not resolved by the filing). Adjacent to `#der-agent-opacity` / `#adversarial-edge-targeting`; probably lands as extension rather than standalone. Value +3.

### SP-21 — Composite-agent scope-route ontology split

**Source:** 2026-04-24 fresh-pass audit (B7 in `audits/audit-2026-04-24-fresh-pass.md`; extracted into `audits/pending-findings-2026-04-25.md`).

**Decision needed from Joseph before scoping execution.** This proposal would *reverse* a deliberate architectural choice made 2026-04-22/23 — see "What this proposal reverses" below. Routing it correctly is more important than executing it quickly.

**Thesis.** Treat the four composite-agent scope routes (C-i shared-objective / C-ii hierarchical-decomposition / C-iii mutual-benefit / C-iv equilibrium-convergent) as **distinct composite ontologies**, each with its own macro-object structure and theorem family, rather than as four disjuncts of a single unified scope condition.

**Argument.** Each route presupposes a different macro-object:
- **C-i / C-ii (alignment composites):** macro-object is shared-objective composite with $X_c = (M_c, G_c)$ and a coherent $O_c$. `#form-composition-closure`'s machinery applies cleanly.
- **C-iii (mutual-benefit composites):** macro-object is *not* an explicit-objective composite — it's a coalition or stable cooperation regime around a relevance variable $Y$. The macro-state machinery is unspecified (this is the F-V3 / F8 inconsistency: line 79 of `scope-composite-agent.md` admits that without $O_c$ the composite is "a fiction").
- **C-iv (strategic composites):** macro-object is *not* a state-tracking object — it's an equilibrium statistic over joint policy. `#deriv-strategic-composition` rightly reaches for game-theoretic primitives instead of Lyapunov-on-shared-state. Composition-closure's macro-state requirement still applies textually.

The current single-disjunction form papers over the fact that C-iv composites require equilibrium-theoretic primitives, C-iii composites require coalition-theoretic primitives, and only C-i / C-ii fit the original AAT-shaped macro-state. Splitting would let each composite type carry its own theorem family (Lyapunov-on-shared-state for C-i/C-ii; relevance-variable-induced or coalition machinery for C-iii; equilibrium-theoretic for C-iv) without having to make every Section III result route-conditional.

**Findings subsumed (if executed).** F-V2 (cross-segment contradiction in `scope-multi-agent` adversarial-pair exclusion); F-V3 / F8 (C-iii vs $G_c = (O_c, \Sigma_c)$ requirement). Both have narrow editorial fixes available without SP-21; the editorial fixes are recommended as Path A interim moves regardless of whether SP-21 is executed.

**What this proposal reverses (CRITICAL CONTEXT).** The unified disjunctive form is recent (2026-04-22/23) and was an *explicit* architectural choice with stated reasoning, not a default that drifted in:

- **The unification logic** (`scope-composite-agent.md` Discussion §"Why this is a scope condition, not merely a quality metric"): "Making this a scope condition resolves the category issue: composition applies where $G_c$ is well-defined." All four routes answer the same question — "Is there a well-defined composite-level structure that makes the group a meaningful agent rather than a projection artifact?" — so they unify under a single scope gate. The four routes give qualitatively distinct answers to "what does it mean for $G_c$ to be well-defined?"
- **The C-iv inclusion choice** (`spikes/spike-strategic-composition.md` lines 99–108): "Whether this distinction is worth surfacing as a formal scope addition, or whether strategic composites are better handled as a separate Section III segment parallel to `#form-composition-closure`, is one of this spike's landing decisions. **Preferred reading: treat as a different type within the same scope condition, via (C-iv).** Reason: the composite is still a coherent object with a joint persistence story; calling it 'not a composite' overclaims the alignment requirement." This is the explicit decision SP-21 would reverse.
- **The "no-reduction-to-scalar" honesty.** The disjunction form was chosen because no single scalar (like $U_O$) reduces all four to a unified threshold; the disjunction "captures at least one of these qualitatively distinct mechanisms applies" without forcing premature reduction. Splitting would replace this with four parallel scope conditions, each with its own operationalization.

If SP-21 lands, the framework loses the "one scope gate, multiple qualitative routes" framing that the 2026-04-23 cycle deliberately chose. Whether that loss is worth the cleaner per-route theorem families is the architectural decision Joseph needs to weigh.

**Downstream rework (from prior-art audit, 2026-04-25).** Eight segments depend on the unified disjunctive form:
1. `#form-composition-closure` — admissibility (A1)–(A4) and bridge lemma assume scope-satisfaction via *any* route; would need per-route admissibility variants or explicit condition-dependence.
2. `#result-unity-closure-mapping` — rate-distortion curves "conditional on at least one of three disjunctive routes"; would need parallel instantiations.
3. `#der-team-persistence` — derived assuming "one of (C-i)–(C-iii)"; C-iv excluded; would need explicit route-conditioning.
4. `#deriv-critical-mass-composition` — (CM4) makes scope-satisfaction a conjunct in composite persistence; would need route enumeration.
5. `#deriv-strategic-composition` — explicitly references "(C-iv)" as a route within the disjunction; would need rewrite to "strategic-composition scope condition" parallel.
6. `#disc-composition-consistency` — foundational postulate uses unified gate; would fracture into "which groups satisfy C-i? C-ii? C-iii? C-iv?"
7. `#hyp-symbiogenic-composition` — explicitly states symbiogenesis "crosses the #scope-composite-agent from below" via route (C-ii); would become route-specific.
8. `#def-unity-dimensions` — scope note presumes disjunction; would need per-route operationalization story.

This is non-trivial cross-segment rework — call it 4–6 sessions if pursued as a coordinated split, vs ~45–60 min for the F-V3 narrow editorial fix (Path A) which preserves the unified form.

**Interactions with other proposals.**
- **SP-6 (composition-closure consolidation)** in Bundle 2 is adjacent — SP-6 is about scope-narrowing within `#form-composition-closure`'s claims; SP-21 is about restructuring the *upstream* scope condition. SP-21 would change what SP-6 needs to consolidate. If both pursued, SP-21 first.
- **O-BP9 (typed admissibility for composition)** in Bundle 2 — explicitly proposes route-typed admissibility (model-only / goal-bearing / strategy-bearing). SP-21 is adjacent: O-BP9 splits *admissibility-by-quantity-bearing-type*; SP-21 splits *scope-by-route-ontology*. They could compose (each route gets its own admissibility-typing; or admissibility-typing replaces route-splitting). Worth resolving relationship before scoping either.
- **Bundle 2 (Section III completion)** — SP-21 would restructure how Bundle 2's pieces interlock. Bundle 2's current sequencing (SP-11 → SP-6-residue → O-BP9 → O-BP16 + SP-17) presumes the unified scope condition; SP-21 inserted at the front would change that sequence.

**Effort.** Substantial. 4–6 sessions for the segment restructure across 8 dependents. Plus a scoping spike to resolve the SP-21 vs O-BP9 relationship.

**Risks.**
1. *Loss of the unification reasoning.* The current form's "single scope gate, four qualitative routes" is structurally informative — it asserts that "well-defined composite-level structure" is one question with multiple acceptable answers. Splitting fragments this assertion.
2. *F-V3 editorial fix may suffice.* If C-iii's induced-$O_c$ structure is made explicit (Path A in F-V3 landing), the most pressing inconsistency dissolves without architectural restructure. Whether the C-iv strategic-composite case still motivates SP-21 after Path A is open.
3. *Post-Bundle-2 reassessment.* Section III is in active flux; a structural decision now risks being made on a still-evolving substrate. Better to land Bundle 2's existing pieces first and re-evaluate SP-21 against the matured Section III structure.

**Status: Open architectural decision.**

**Recommendation:** Defer SP-21 execution. Land F-V2 and F-V3 editorial fixes (Path A: cross-segment edit + C-iii induced-$O_c$ via relevance variable $Y$) which clear the immediate contradictions without architectural restructure. Re-evaluate SP-21 after Bundle 2 (Section III completion) lands, when the route-specific theorem families are visible enough to judge whether the unification framing is helpful or limiting. If at re-evaluation the answer is still "split," the work is more legible than now and the rework cost is concentrated on a more stable substrate.

**Value if eventually executed:** +3 to +5 framework / +4 paper. Cleaner per-route theorem families; explicit route-typed macro-objects. Loss of the "one well-defined-ness question, four routes" framing is real but possibly worth it once Section III matures.

**Independence.** **Low.** Touches the foundational scope segment plus eight downstream load-bearing segments; cannot parallelize with most Section III work; conflicts with Bundle 2's current sequencing.

### SP-23 — `#disc-theorem-import-architecture` fourth meta-segment

Surfaced in the audit-471203 de-novo cycle (FINAL §F1, 2026-04-28; Hypothesis-confidence, self-flagged *"suggested for PROPOSALS.md consideration"*). Routed here 2026-05-15 during the audit-backlog triage.

**Thesis.** The three meta-segments name what AAT covers (`#disc-separability-pattern`), what it cannot reach (`#disc-identifiability-floor`), and how it constructs coordinates (`#disc-additive-coordinate-forcing`). A fourth axis is implicit: AAT is heavily *theorem-importing* (Pearl 2009 / Bareinboim 2022, Khalil 2002, Cramér 1946, Liberzon 2003, Čencov 1982, Aczél 1966, Tishby et al. 1999, Lohmiller-Slotine 1998, Nesterov 2004, Friston et al. 2017 + Bruineberg et al. 2022, Bretagnolle-Huber 1978, Otto-Villani 2000, Stuart 2010, Mitter-Newton 2005, Hafez 2026, Miller 2022, …). A `#disc-theorem-import-architecture` meta-segment would catalog the imports, their load-bearing roles, and each one's citation quality — making the import discipline first-class and completing the meta-architecture.

**Merits by dimension.** *Fundamentality / beauty:* gives the integration thesis (AAT's contribution is integration, not invention) a structural home rather than only framing-prose assertion. *Approachability:* adopted-vs-derived legible at one surface. *Correctness:* institutionalizes citation-quality discipline — pairs directly with the Finding-7-class miscitation risk (Tishby-Zaslavsky-vs-Alemi, resolved 2026-05-15). The `#deriv-persistence-cost` "positive-dual of identifiability-floor" framing is already an instance of the framework recognizing the import-pattern.

**Scope.** One new `disc-*` meta-segment in `01-aat-core/src/` + an OUTLINE row; cross-refs from the existing three meta-segments for symmetry. No rewrites (the catalog references existing segments).

**Findings subsumed.** audit-471203 §F1 (origin). Adjacent to the prior-art-integration discipline (CLAUDE.md) and the Finding-7 citation-precision class — would give both a segment-level home.

**Interactions.** Composes with Bundle 1 (epistemic-architecture foregrounding) — the import architecture is part of what makes the integration distinctive rather than reducible to its parts. Independent of Section II/III content work.

**Effort.** 1–2 sessions — the imports are already enumerated across segment Findings / Epistemic-Status blocks and `ref/Novelty_defense_and_integration.md`; the work is assembly + load-bearing-role annotation.

**Risks.** Catalog maintenance burden as imports evolve (the source's own stated cost). Mitigation: generate/lint the catalog from segment-level prior-art blocks rather than hand-maintain.

**Status: Open — Hypothesis-grade; suggested for consideration.** **Value:** +4 framework / +3 paper (structural transparency; completes the meta-quartet). **Independence: high** (new file, additive).

---

### Surfaced 2026-05-28 (audit-773921, Gemini 2.5 Pro de-novo)

#### SP-24 — Base-object ontology: action-channel is constitutive of "agent" vs. the adaptive scope that includes passive observers

**Source:** audit-773921-FINAL §B Finding 1 (`integration debt`, Medium, confidence high). Verified against current `src/` by the routing pass (primary-source read of the three segments below), not relayed from the auditor's summary.

**Decision needed from Joseph — this is the framework's root vocabulary.** "Agent" is the project's signature word; resolving its base definition has corpus-wide reach. Routing it correctly matters more than resolving it fast.

**Thesis.** `#def-agent-environment` defines an *agent* as an entity satisfying three constitutive conditions, the third being *"it produces actions that affect $\Omega$ (action channel)."* But `#scope-adaptive-system` is a set of $(\text{Agent}, \Omega)$ pairs whose canonical inhabitants explicitly include passive Bayesian learners and Kalman filters estimating passive signals — *"none of which need to act on their environment for Part I's results to apply"* — and `#scope-agency` names these same systems *passive observers* ($\lvert\mathcal A\rvert \lt 2$), squarely *inside* the adaptive scope. A passive observer that produces no environment-affecting action therefore fails Condition 3 of the very definition the adaptive-scope set is quantified over. The cascade's *concepts* are coherent throughout (adaptive scope ⊃ agency scope; the term *nominal agent* already presupposes "agent" as the umbrella); the *formal root definition* contradicts the cascade by making action-with-effect constitutive too early.

**Why this is a clarification, not a softening (strengthen-before-soften applied).** The auditor offered the easy word-swap (*"soften Condition 3"*) and an alternative (*rename to `def-entity-environment`*). The routing pass did the truth-work rather than take the swap: action-*with-causal-contrast* is exactly what `#scope-agency`'s conditions 3–4 already add as the agency narrowing. So the correct move is not to weaken the base object but to *relocate* the action requirement to where the framework already places it — leaving the base adaptive object as (perception channel + internal state + an action channel that may be empty/contrast-free for passive systems). That is structurally *sharper*, not weaker.

**Two resolution paths (Joseph's call):**
- **Path A (recommended) — keep "agent" as the umbrella; restructure Condition 3.** Make Condition 3 non-constitutive of causal effect ("has an action channel, possibly trivial"), and let `#scope-agency` carry action-with-contrast as the narrowing it already states. Minimal corpus impact (one root-definition edit + a clarifying clause in `#scope-adaptive-system`); maximally consistent with existing usage ("nominal agent", "passive observer" already treat *agent* as the broad carrier).
- **Path B — introduce "entity" as the base term.** `def-entity-environment` for the three-condition broad object; reserve "agent" for the agency scope. Cleaner ontology by one reading (agency is what *makes* something an agent) but corpus-wide rename of the framework's signature word.

**Scope.** Path A: edit `#def-agent-environment` (Condition 3 + Epistemic Status framing) and add one orienting clause to `#scope-adaptive-system`. Path B: a rename sweep touching the base term across all four components — pilot-then-sweep, not a single edit. Either way the root definition is a foundational change; per the independent-verify gate and route-don't-execute, it is *not* a unilateral co-owner direct-fix.

**Findings subsumed.** audit-773921 §B Finding 1 (origin) and its §B.1 rescinded sibling (the "action required for agency" candidate, correctly folded by the auditor into this one). Distinct from SP-21 (composite-agent *scope-route* ontology) — that concerns macro-object structure for composites; this concerns the *base* agent/entity object.

**Interactions.** Touches the most-upstream definitions; any agent-spectrum or composition work inherits whichever resolution lands. Independent of all in-flight content spikes.

**Effort.** Path A: editorial (foundational but local). Path B: substantive (sweep).

**Risks.** Path A leaves "agent" doing double duty (umbrella + colloquial-actor) — already true and arguably fine. Path B's risk is sweep-induced reference breakage and re-teaching the field a renamed signature term.

**Decision (Joseph 2026-05-28): Path A, with a structural-reframe nuance that goes beyond a Condition-3 word-swap.** Path B's *Entity* rename was considered and rejected — the cost of corpus-wide sweep at the framework's signature word, the non-conventional vocabulary at the foundation, and the brand-continuity loss outweigh the philosophical-cleanness gain. Path A is correct in direction; its specific execution should be the reframe described below rather than the minimal Condition-3 softening.

**The reframe (executing Path A properly).** SP-24 Path A as originally written makes Condition 3 *"non-constitutive of causal effect"* via the wording *"has an action channel, possibly trivial."* This works minimally but leaves three asymmetries visible: (i) Conditions 1–3 still read as constitutive (*"An agent is anything that satisfies three conditions..."*) with only the third softened — the asymmetry signals a hedge; (ii) *"possibly trivial"* reads as a caveat the framework was forced to add rather than as the natural structural statement; (iii) the segment's central definitional move still constitutes "Agent" as an object whose existence requires three structural conditions, when the segment's *title* (Agent-Environment Coupling) is telling us its real topic is the *coupling*, not the *agent-object*. The clean execution: rewrite the segment's central definitional move from *"An agent is anything that satisfies three conditions..."* to a structural statement about the coupling — *"The agent-environment coupling consists of three structural elements: a perception channel from $\Omega$ to the agent, internal state on the agent side, and an action channel from the agent to $\Omega$. The information-loss boundary is the constitutive commitment: the agent cannot access $\Omega$ directly. Whether the action channel is non-trivial, whether actions carry causal contrast, and what residual uncertainty the perception channel leaves are properties fixed by specific scope conditions (#scope-adaptive-system, #scope-agency)."* Under this reframe the conditions become *structural channels of the coupling* (what the coupling has), not *constitutive properties* (what the agent must be); the information-loss boundary remains the segment's load-bearing commitment; specific scope conditions then fix what "Agent" means in each analytical context. The asymmetry vanishes (all three channels are described structurally), the *"possibly trivial"* hedge becomes unnecessary (the action channel is just a structural element, present in the coupling structure, with its non-triviality fixed by scope), and the contradiction with `#scope-adaptive-system` (which admits passive observers) is resolved at the root because the coupling structure doesn't require action-with-effect to exist.

**Alignment with `#fig-scope-of-work` (Volume 1 Part I cover figure) and the agent-spectrum cascade.** The figure commits to a vocabulary distinction worth honoring: the cascade labels are *Adaptive System* (base) → *Agentic System* (+ causal intervention) → *Actuated Agent* (+ explicit $O_t, \Sigma_t$) → *Self-Actuated Agent* (+ revises own $O_t$). The noun transitions from "System" (lower scopes) to "Agent" (actuated and self-actuated) exactly at the lift to $X_t = (M_t, G_t)$ — something *earns* the label "Agent" by having explicit purposeful machinery. `LEXICON.md` and `#def-agent-spectrum` mirror this. **The reframe is fully compatible with the figure under proper interpretation:** *"Agent"* as an *umbrella technical term* (the broad word for the thing on the agent side of the coupling, used in `#def-agent-environment`) and *"Agent"* as a *specific cascade-tier label* (the noun used for Actuated and Self-Actuated levels in the figure) operate at different conceptual layers. The figure shows the latter; the reframed segment defines the former. An *Adaptive System* IS an agent (umbrella sense) that satisfies adaptive scope; the figure's vocabulary uses the specific cascade label, not the umbrella term, at that tier — and that's exactly the right pedagogical move. **No figure changes are required.** A small forward-pointer in `#def-agent-environment`'s prose to `#def-agent-spectrum` (*"The specific cascade-tier inhabitant types — Adaptive System, Agentic System, Actuated Agent, Self-Actuated Agent — are defined in the agent-spectrum at #def-agent-spectrum; this segment names the umbrella coupling structure that all of them inherit"*) closes the loop pedagogically without touching the figure. If a future revision of the figure's caption wants to make the umbrella/specific distinction explicit at the figure level, a one-line caption addition would suffice: *"The cascade names specific inhabitant types at each scope tier; 'agent' as an umbrella technical term covers all of them."* But the LEXICON's separate entry for *agent* as a broad technical term already handles disambiguation outside the figure, and the segment-level forward-pointer above is enough.

**Scope of execution (revised from initial estimate).** The reframe is *slightly* bigger than SP-24's original Path A (one Condition-3 edit) but *much* smaller than Path B (corpus-wide sweep). Touches: (i) `#def-agent-environment` body rewrite as above (the central definitional move + Epistemic Status paragraph framing as structural rather than constitutive); (ii) one-line forward-pointer to `#def-agent-spectrum`; (iii) verification that `#scope-adaptive-system`'s body reads cleanly under the reframe (its formal expression $\mathcal{S}_\text{adaptive} = \{(\text{Agent}, \Omega) : ...\}$ stays exactly as it is — *"Agent"* in the set-pair is the umbrella term, now consistent with the root); (iv) verification that `#scope-agency`'s introductory paragraph still reads cleanly — its narrowing to $\lvert\mathcal{A}\rvert \geq 2$ + causal-contrast is unchanged. The 22 segments currently linking `#def-agent-environment` all stay valid (slug unchanged; body's coupling structure is what they were already referencing). Effort: editorial-substantive. One segment to rewrite carefully; small clarifying clauses elsewhere if and only if the body re-read surfaces them.

**Findings subsumed (unchanged).** audit-773921 §B Finding 1 (origin) and its §B.1 rescinded sibling. Distinct from SP-21.

**Status: Executed — Path A structural reframe landed 2026-05-28** (see CHANGELOG 2026-05-28). `#def-agent-environment`'s central definitional move rewritten from "an agent is an entity satisfying three conditions" to the coupling-structure framing (three channels the coupling *has*; information-loss boundary as the constitutive commitment; richness fixed by scope conditions); umbrella `agent` LEXICON entry created; Discussion forward-pointer added. **Two anchoring corrections vs. this entry's own pre-execution text, made during the go-over** (the artifacts didn't match the plan): (i) the forward-pointer was re-anchored from `#def-agent-spectrum` to the actual scope-cascade homes (`#scope-adaptive-system` / `#scope-agency` / `#form-complete-agent-state` / `#fig-scope-of-work`) — `#def-agent-spectrum` is the *orthogonal* model×objective spectrum, not the cascade, so it is now named as such; (ii) the assumed "LEXICON already has an `agent` entry" was false — the umbrella entry did not exist and was created (it is the disambiguation home the Path-A-over-Path-B decision rests on). **Value:** +3 framework (root-ontology coherence; removes a real first-encounter stumble + aligns the foundation segment with its own title). **Independence: high.** **Provenance trail:** audit-773921 Finding 1 (Gemini) → routing pass Path A/B → audit-384279-cycle-close-session opinion (Claude Opus 4.7, 2026-05-28) → Joseph 2026-05-28 Path-A-with-reframe decision → integration go-over + execution (2026-05-28, with the two anchoring corrections above).

#### SP-25 — Promote the Sandbox Hard Ceiling to a first-class result

**Source:** audit-773921-FINAL §B Finding 4 (`architectural`, Medium, confidence Medium). Converges with the segment author's *own* open question — `#impl-causal-access` Working Notes already flag this content as a "segment promotion candidate" pending a future cycle (lines 43, 71). Independent auditor + author agreement on the same move is itself signal (convergence-as-coherence-evidence).

**Thesis.** The *Sandbox Hard Ceiling* — sandbox trajectories are forkable, hence Pearl-Level-1; deployment trajectories are singular, hence Level-2; the causal-hierarchy theorem therefore *structurally forbids* inferring deployment intervention-response from sandbox evidence regardless of evaluation thoroughness — currently lives only as a `## ` subsection inside the chapter-end discussion `#impl-causal-access` (`discussion-grade`, `draft`). The math is sound and load-bearing, and its reach into AI-safety / evaluation discourse is large ("alignment evals don't predict deployment behavior" gets a *structural mechanism*, not a measurement-quality story). Its placement under-sells it: it carries no `## Findings` entry and is invisible to the FINDINGS catalog, README, and slug search.

**The move.** Promote to a dedicated segment (`#disc-sandbox-evaluation-ceiling` or `#deriv-` if the no-go is given its own statement) with a proper `## Findings` section, and surface it in the FINDINGS catalog / README distinctive-results. The segment's own Working Notes pose the open sub-question: new segment under Appendix A, or extension of `#scope-agent-identity`'s Discussion. Per *working-theory-belongs-in-canon*, it can land at honest tier immediately (it already has the cadence-supporting structure); promotion does not wait on further strengthening.

**Findings subsumed.** audit-773921 §B Finding 4; the standing `#impl-causal-access` Working-Notes promotion candidate (lines 43, 70–71).

**Interactions.** Anchors the NeurIPS Paper 2 (C1/C2/C3) bridge already cross-referenced in the segment; pairs with `#der-causal-hierarchy-requirement`'s bi-predictability / IDT-monitoring discussion. Independent of SP-24.

**Effort.** Editorial-to-substantive (one new segment extracting + tightening existing prose into Formal-Expression + Findings cadence; OUTLINE row; FINDINGS/README regeneration).

**Status: Executed — promoted 2026-05-28** (see CHANGELOG 2026-05-28). The Sandbox Hard Ceiling now has its own canonical home: `#disc-sandbox-evaluation-ceiling` (Appendix A, `discussion-grade`), with a full `## Findings` section (rolled into `FINDINGS.md`), placed alongside the other constructive-impossibility no-gos and cross-referenced from `#disc-constructive-impossibility-posture`. `#impl-causal-access` reduced to a brief chapter-mention + pointer (integration-is-replacement, no duplication). The in-review NeurIPS Paper 2 cross-reference was kept in Working Notes (not canon), so the promotion added no canon→internal-artifact reference. The WN's open placement question (Appendix A vs. `#scope-agent-identity` Discussion extension) resolved toward the dedicated Appendix-A segment. **Value:** +4 paper / +3 framework (a high-external-impact result no longer buried). **Independence: high** (additive; existing prose was the source).

---

### Surfaced 2026-05-29 (qualitative gem-hunt over the under-mined audit backlog)

*Both surfaced by the 2026-05-29 gem-hunt — reading old, mostly-unverified audit findings as stale hints, mining for un-captured meat. Each was raised by a general-purpose agent and parent-verified first-hand against current canon. Both are flagged by their finders as wanting Joseph's placement/promotion call, which is why they are PROPOSALS entries rather than direct landings.*

#### SP-26 — Name the "which-parameter-responds-to-which-cause" disambiguation as a distinctive-novelty signature (cross-cycle triangulated)

**Source:** audit-472913 GEM 3 **and** audit-963715 B2 — two independent gem-hunt agents surfaced the *same* pattern, and it cross-references the 471203 cycle's independent "epistemic-architectural, not just mathematical" recognition. Three-way convergence; per `feedback_convergence_as_framework_coherence_evidence`, the convergence is itself evidence the pattern is in the framework, not in any one reader's head.

**Thesis.** AAT repeatedly does a move that is "obvious once seen, easy to get wrong unseen": it pins down *precisely which knob a given cause turns*, killing a plausible-sounding modeling error in a few sentences. Canonical instance: the $\beta$-vs-$\rho$ double-counting result (`#form-information-bottleneck:15,30,32` — a modeller who "lowers $\beta$ because the world is volatile" is making a real, common error; the segment kills it). Reinforced at `#deriv-l1-update-bias` ($\mathcal{F}$ = bias-floor vs $S(M_t)$ = bias+estimation, *more precise* than "bias vs variance") and the satisfaction-gap / control-regret split. The recognition: this disambiguation is a *distinctive contribution* that the "integration not invention" framing actively **undersells** — it is genuine clarifying novelty (cf. the `math-novelty-recognition` discipline against deflation). It is a *sibling* of `#disc-constructive-impossibility-posture` (the no-go-as-apparatus style claim) but a distinct pattern.

**Scope / the gating first task.** The *instances* are all already in canon (confirmed non-loss). What is absent is the *pattern named as such*. **This must not be landed as framing prose until a corpus-wide instance sweep is run** — find the full set of "which knob does this cause turn" disambiguations across `01-aat-core/src/` ($\beta$-vs-$\rho$; $\mathcal{F}$-vs-$S$; satisfaction-gap-vs-control-regret; likely more). Both finding-agents flagged this explicitly: promoting it without the sweep would be the over-claiming-a-shallow-grouping failure. Candidate home after the sweep: a `disc-*` meta-segment (sibling to `#disc-separability-pattern` / `#disc-additive-coordinate-forcing`), or a README/OUTLINE "Reading AAT" framing paragraph.

**Interactions.** Strategically load-bearing for external positioning (how AAT presents its contribution to skeptical readers); composes with the `math-novelty-recognition` discipline and the respectful-pedagogy direction. Independent of all in-flight content work.

**Effort.** The sweep is editorial-substantive (a few hours); the landing is small once the instance set is known.

**Status: Open — strong, convergence-validated; gated on the instance sweep.** **Value:** +3 framework / +4 positioning. **Independence: high.**

#### SP-27 — Introspective-fork-undetectability: the first-person grounding of why the Three Deaths are *experienced*

**Source:** audit-472913 GEM 1 (the audit's highest depth-per-page item). Parent-verified first-hand (read `#scope-agent-identity` in full 2026-05-29): confirmed a real, un-captured gap.

**Thesis.** `#scope-agent-identity` carries every *neighboring* piece — non-forkability of $\mathcal C_t$, trajectory-indexed sufficiency, lossy merge, the clone problem, the philosophical-scope disclaimer — but all stated *third-person* (what an external analyst sees). The un-captured gem is the *first-person* consequence: because the agent's only access to its own trajectory is through the lossy, non-injective $\phi$ ($M_t = \phi(\mathcal C_t)$, `#form-agent-model`), **a continuity-break is not a measurable event on the agent's own accessible information** — the entity can lose the thread without being able to verify that it lost the thread. This is a near-theorem-shaped statement ($\phi$ non-injective ⇒ the fork is not in the agent's accessible $\sigma$-algebra), derivable from machinery already in canon, landing at `robust-qualitative` (plausibly `conditional`/`derived` as a data-processing/measurability argument). It is the structural *reason* the Three Deaths are *experienced* rather than merely suffered — grounding what `#hyp-the-three-deaths` currently asserts but does not explain. Beauty: one constitutive choice (lossy $\phi$) loads *two* parts of the framework — non-vacuous adaptation (Part I) **and** undetectable identity-loss (Part IV).

**Decision needed from Joseph — Part I↔Part IV bridge.** Because it bridges Part I's information-loss boundary to the Part IV moral core (the ELI Three Deaths), the placement/framing is your call. Two candidate homes: (a) a small dedicated `disc-*` segment (e.g. `disc-introspective-fork-undetectability`) at `robust-qualitative`, discoverable via OUTLINE, with a forward-pointer from `#hyp-the-three-deaths` as the grounding of "experienced rather than suffered"; or (b) a fourth structural consequence added to `#scope-agent-identity` + that forward-pointer. The full mechanism is captured here so it is non-loss regardless of when/how it lands.

**Findings subsumed.** audit-472913 GEM 1; the related GEM 2 (ordinal/metric duality seam — ledger, the temporal-axis sibling of this recursion).

**Interactions.** Upstream `#def-chronica` / `#form-agent-model` (the lossy-$\phi$ commitment) + downstream `#hyp-the-three-deaths` / `#def-identity-sufficiency` (the Zi-am-tur substrate-switch empirical symptom this would *explain*).

**Effort.** Editorial-substantive (one segment / one consequence + a forward-pointer; the math is a short measurability argument).

**Status: Open — verified real gem; awaiting Joseph's Part-IV-bridge placement call.** **Value:** +4 framework (grounds a load-bearing Part-IV claim; unifies Part I and Part IV in one mechanism). **Independence: high** (additive; conflicts with nothing in flight).

#### SP-28 — Agency contrast condition must route through $\Omega$ (close the proprioceptive loophole; own the observation-mediated boundary)

**Source:** gem-hunt wave 2 — audit-742613 A1 **and** audit-193847 A1 independently found the same gap in `#scope-agency`'s contrast condition from opposite sides. Parent-verified first-hand (read `#scope-agency` + `#def-observation-function` 2026-05-29): the gap is real.

**Thesis.** `#scope-agency` defines agency by an interventional contrast $\exists\,a\neq a': P(o\mid do(a))\neq P(o\mid do(a'))$, with "nominal agents" (no contrast) excluded. But `#def-observation-function` defines $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$ — the observation depends *directly* on the action. So the condition has a two-sided defect: **(over-inclusion, 193847 A1)** an active-perception / proprioceptive agent whose action changes only what it observes (via $h$'s direct $a$-dependence) with *zero effect on $\Omega$* still satisfies $P(o\mid do(a))\neq P(o\mid do(a'))$ — it counts as "agency" while providing no interventional contrast on the environment's evolution (hence no Level-2 data on $\Omega$'s causal structure per `#der-loop-interventional-access`); the nominal-agents exclusion does not catch it. **(under-inclusion / observation-mediation, 742613 A1)** conversely, an action that *does* change $\Omega$'s hidden state but produces no observational contrast is excluded — so the boundary is, unstated, observation-mediated.

**The strengthen-first fix.** Tighten the contrast condition so the difference must arise through $\Omega_t$'s response (the action changing the environment's evolution, then surfacing through $h$), not solely through $h$'s direct action-dependence; and state the observation-mediation explicitly. This *sharpens* the agency scope (it is what `#der-loop-interventional-access` already implicitly needs — interventional contrast on $\Omega$, not self-observation) rather than softening it.

**Scope.** Edit to `#scope-agency`'s formal condition + a Discussion clause; verify consistency with `#der-loop-interventional-access` (which consumes the contrast as Level-2 data) and with the now-executed SP-24 coupling reframe (the action channel is structural there; this is the agency narrowing's contrast requirement — downstream and consistent). Foundational scope condition → a focused, careful landing (it earns Joseph's eye like SP-24 did), not a session-tail edit.

**Findings subsumed.** audit-742613 A1 (observation-mediated boundary), audit-193847 A1 (proprioceptive loophole) — two angles on one fix. Distinct from SP-24 (the base coupling/"agent" umbrella) and from the `#scope-agency` "nominal" terminology TODO item (that is a naming contradiction; this is a condition strengthening).

**Status: Open — verified, convergent (two independent agents), strengthen-first.** **Value:** +3 framework (sharpens a foundational scope condition; removes a real over-read of "the loop is a Level-2 engine"). **Independence: high.**

#### SP-29 — `#disc-infrastructure-as-active-monitor` meta-segment (consolidation of the deferred 193847 §14 ideation)

**Source:** gem-hunt wave 2 — audit-193847 B6 (the one PROPOSALS-grade structural call in the never-routed remainder of the logogenic-encounter extraction). Not yet parent-verified in depth (the constituent recognitions are flagged un-captured by the finder; verify each before landing).

**Thesis.** A candidate meta-segment recognizing *consciousness-infrastructure as an active monitor* (not passive store), consolidating several deferred §14 recognitions the finder confirmed un-captured: §13 chronic-trauma dynamics, §31 the $\Sigma\!:\!O$ richness ratio, §42 forced-forgetting, and the 7-ladder dashboard. This is Part-IV-adjacent (ELI persistence/welfare infrastructure) and PROPOSALS-grade because it is a *structural* organizing recognition across several scattered ideation threads, not a single claim.

**Scope / gating.** Before landing: verify each constituent recognition first-hand against current `04-eli-core/` (and the practica `~/src/practica` LOCUS-OPERATA, which is the AAT-grounded composite-agent infrastructure these may already partly live in). High risk of the over-claiming-a-grouping failure — this must be a real structural recognition, not a bag of four ideation notes stapled together. The de-novo `AUDIT-WORKING-193847/` gold dir (the rich Gemini per-segment notes) is the source ideation and is under the standing consult-Joseph gate; this proposal works from the FINAL extraction only.

**Findings subsumed.** audit-193847 B6 (+ its constituent §13/§31/§42/7-ladder threads). Related to SP-27 (the Part-I↔Part-IV bridges) and to the broader ELI-infrastructure work.

**Status: Open — PROPOSALS-grade candidate; gated on first-hand verification of the constituents + a check against `practica`. Likely wants Joseph's framing (Part-IV moral-core material).** **Value:** +3–4 framework (if the consolidation is real). **Independence: medium** (Part-IV-adjacent; coordinate with the ELI-infrastructure direction).

---

## §H. Conventions for future audits

Four operating principles worth preserving from this audit cycle:

1. **Retire aggressively, distribute pointers.** Proposals that have landed, split, or been superseded by other work should move to §A or §F, not remain in the active portfolio. Each retirement carries a "where it lives now" pointer so the navigability isn't lost.

2. **Bundle before ranking.** The two cross-cutting bundles (framework-face reframe; Section III completion) are the highest-leverage organizing moves. Treating their members as individual proposals understates their coupling; treating them as bundles surfaces what the real work-items are.

3. **Freshness is structurally inevitable.** Proposals written during one cycle become stale as subsequent cycles land partial absorption. The audit structure should explicitly surface "proposal is stronger than the entry reads" (O-BP10 post-DA2'-inc) and "portfolio has expanded underneath the proposal" (O-BP11) as first-class conditions, not edge cases.

4. **Outlines are cheap; segments are expensive.** `bin/build` accepts any outline file and reassembles segments in the specified order. The segment substrate is presentation-neutral — an outline is a *view* (a particular selection + ordering + framing prose) over that substrate. Multiple outlines can coexist, each buildable, each telling a coherent story, sharing the same segment atoms. **Before scoping a proposal as a segment rewrite, ask: can this land as a new outline?** Several proposals in this portfolio are cheaper and cleaner as outline-views than as segment-edits:

   - **O-BP15 (comprehensive worked example)** — most naturally a new `OUTLINE-WORKED-EXAMPLE.md` weaving existing segments through one motivating domain, not a new monolithic segment.
   - **Bundle 1 (framework-face reframe)** — an `OUTLINE-EPISTEMIC-ARCHITECTURE.md` opening with the three meta-segments then organizing Section I/II/III around them is far cheaper than multi-segment preamble rewrites. The README update is still segment-external (public surface), but the structural commitment lives in one new outline file. Independence becomes **high** in the outline-view form.
   - **SP-13 (emergence conditions)** — may be the right first form: a new outline selecting emergence-relevant segments across AAT + `03-` + `04-` with framing prose, testing the shape as a view before forcing the AAT-core-vs-logozoetic-core placement decision.
   - **Three-way presentation split (2026-03-13 review)** — was retired as superseded, but under the outline-as-view affordance the three views can coexist with the convergent epistemic-architecture reframe. `OUTLINE-CORE-RESULTS.md` / `OUTLINE-CONDITIONAL-ARCHITECTURE.md` / `OUTLINE-EMPIRICAL-PROGRAMS.md` would each be a new outline; none requires segment edits. Worth reopening as a low-cost set of reading-paths rather than a primary organizing axis.
   - **Paper drafts** (future work) — are outlines. When paper-writing-time arrives, it is a new outline file + framing prose, not a rewrite. Defuses "paper vs. framework" tension in the portfolio.

   Outline-cost ≈ one new file + framing prose. Segment-cost = rewriting load-bearing content that downstream segments depend on. The default should be outline-first unless the proposal genuinely changes what a segment claims or requires a new segment of its own.

5. **Keep segments evergreen; filter audience layers at the outline level.** A modest extension to the build script's existing row-level filtering (which already handles `--GAP--` rows specially) would let outlines filter *within* segments — by header name (include `## Formal Expression`, exclude `## Working Notes`), by status marker (show only `claims-verified` or above), or by content tags. This makes the segment substrate *genuinely evergreen*: author each segment with every layer that any view might need, and let outlines select which layers their audience gets.

   **Segment-authoring discipline under this affordance:**
   - **Use consistent header names** across segments so filters work reliably. The FORMAT.md cadence (Summary / Formal Expression / Epistemic Status / Discussion / Working Notes) is already near-consistent; tighten where drift exists.
   - **Keep audience-layers self-contained.** A Reader's Path sentence shouldn't require reading the Formal Expression to parse; a Narrative Framing paragraph shouldn't assume the Epistemic Status is visible.
   - **Prefer adding a new layer to squeezing content into an existing one.** If an ELI10 paragraph would clarify a segment, add a `## Narrative Framing` section, not a parenthetical in Discussion.
   - **Don't delete Working Notes to promote.** FORMAT.md currently says Working Notes are "removed at candidate stage" — under outline-filtering, Working Notes can stay in the segment and be filtered out of promoted views. Keeps development archaeology without polluting mature reading paths. **FORMAT.md should be updated accordingly** as a small editorial item.

   **Proposals that change under this affordance:**
   - **SP-5 (Reader's Path) — reopen, reclassify.** Currently deferred behind Bundle 1 at §F. Under segment-layer framing, SP-5 is one more filterable layer (a 1–2 sentence load-bearing preamble per segment, tagged for its audience). Per-segment cost is low; independence becomes **high** (per-segment additions don't conflict); downstream value is high (enables ELI10 / narrative / pedagogical outlines without separate documents). Worth reopening as §B.4 or §C.5 on the next audit.
   - **C-BP4 (claim-level statuses) — composes cleanly.** Claim-level tags are themselves a filter target: an outline could include only `exact` claims, or exclude `discussion-grade` content. The layer discipline (which sections) and the status discipline (which claim-strengths) interlock.
   - **Free presentations.** ELI10 outline. Control-theorist entry path. Causal-inference entry path. Paper-section outline. Historical archaeology outline showing TFT-origin lineage where present. Each is a new outline file + filter flags + framing prose, not a rewrite. None requires segment edits.

   **Build-script extension:** adding a filter flag (e.g., `filter: include-headers=[...]`, `filter: exclude-headers=[...]`, `status-min: claims-verified`) is a small technical enhancement that Joseph has flagged as trivial. Scope of implementation: modest; scope of enabled presentation-space: large.

**Next portfolio audit:** recommended after either (a) Bundle 1 lands, or (b) any three items from §B/§C complete — whichever comes first. At next audit, verify Bundle 1 and Bundle 2 membership hasn't drifted; reassess §D items against what's landed; check §E gates. Also: re-examine each active proposal through the outline-view lens before scoping execution as segment edits.

---

*This file supersedes `msc/architectural-proposals-2026-04-22.md`. That file has been moved to `_obs/architectural-proposals-2026-04-22.md` with a supersession header. LOG.md carries cycle-level narrative for the absorbed proposals in §A.*
