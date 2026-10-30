# Internal surfaces: trackers and peripheral non-canon material

*Objectives tree: feeds **KR3.2** of `../INTENT.md` (live theory stranded inside asf is mapped), and through it KR3.3 and O1. Cross-surface synthesis: `00-cross-surface-map.md`.*

*Written 2026-10-30 (clock: 11:45 MDT) by a fork of the internal-surfaces coordinator, at asf HEAD `7ad5cd34`. Sibling maps in this directory cover Working Notes, audits (two maps), spikes, and `msc/`. This one covers the root trackers (TODO, PROPOSALS, PRACTICA, TST-IDEAS, FORMAT-TODO, BIBLIOGRAPHY-TODO, TERMINOLOGY-TODO, INTEGRATION-CLEANUP-TODO, TODO-big-picture, JOSEPH-TODO), `msc/decision-briefs-2026-07-15.md`, HISTORICAL-CONTEXT, `ref/`, `02-tst-core/lit-review/`, `02-tst-core/empirical-discontinuity/`, the legacy `old-*` files inside the component `src/` dirs, `empirica/`, `releases/`, `doc/DOMAINS.md`, `NOTATION.md`, the OUTLINE GAP and missing-file rows, and git branches.*

**Who reads this.** The coordinator first; then goal-setting with Joseph, the owner-level reviewer, and later integration agents who need to know where to go. So each item names where it lives, how old it is (git dates), what it is in my judgment, and the slugs it bears on. Section 9 is a slug-keyed join table for merging with the sibling maps.

**What "verified" means here.** Where I say *verified*, I checked current canon or git myself today. Everything else is what a tracker says about itself, marked as such. Trackers in this repo are themselves stale in places (they say so), so their claims are hypotheses about canon, not facts about it.

---

## 1. What I think matters most (judgment, ranked by bearing on what the theory *is*)

1. **TST is the most stranded volume, and the strandedness is mostly not in its trackers.** Verified: `02-tst-core/src/` holds 72 markdown files, but 43 of them are `old-tst-*` legacy documents (7,739 lines) that are in no OUTLINE; the real TST canon is **29 segments**. Around those 29 sit: `TST-IDEAS.md` §9, which declares five candidate segments *segment-ready* since 2026-05-21, gated only on "Joseph's go-ahead on placement" (none has a file today, verified); a theorem-grade result, the wrapper-level persistence inequality, living only in `spikes/tst-ideas-cycle-2026-05-21/` with no OUTLINE row (verified); two later spikes (2026-07-04 independent derivations, 2026-07-28 partition isolation) that each recommend a new TST cluster; a 15k-line April 2026 literature review in `02-tst-core/lit-review/` that canon reaches only through the `old-tst-*` files; and the two OUTLINE `--GAP--` rows (developer tempo channels, unmaintainability bifurcation) whose candidates the spikes resolved. TST's actual theory is several times larger than its canon.
2. **A backlog of theory decisions waited on Joseph, and today's lifting of gates releases all of it.** `JOSEPH-TODO.md`, pointing at `msc/decision-briefs-2026-07-15.md` ("the valve") carries roughly fifteen decisions with options and lead recommendations, most unchanged since 2026-07-15. Several are root-level theory calls, not process: SP-30 (the typed epistemic target $S_t = (\Omega_t, \theta)$, whose gating claim is verified and whose decision package has sat ready since 2026-07-04), C5 (the intelligence–empathy convergence legs), the 01-aat-core ordering call, and the names of the separability-ladder rungs and agent-spectrum quadrants. Section 3 sorts them.
3. **The 03/04 volumes are mostly OUTLINE rows without files.** Verified: 03-llm-core has 7 named slugs with no file and 04-eli-core has 13. Several of these are what the volume prefaces lean on (substrate independence, substrate-independent persistence, honest activation). The 2026-09-23 honest-activation spike (spikes map) is the live work for `#norm-honest-activation`, which has no file.
4. **The "external research to integrate" lists are scattered across at least eight places** and partly absorbed. Section 4 gives them one findable home, per the request relayed from Joseph today.
5. **Section III (composition) is the structurally weakest part of AAT by its own account.** PROPOSALS Bundle 2 and the four population-level `--GAP--` rows in `01-aat-core/OUTLINE.md` (rows 304–307) all point at it; TODO calls `msc/working-composition-admissibility.md` (473 lines, 2026-04-01) "Section III's most load-bearing open problem"; CL-1 (`#dissipativity-template`) has been queued since 2026-05-17 with no file.
6. **The trackers mirror Joseph's diagnosis of lost clarity.** They are organized by provenance and by cycle (which audit, which spike cycle, which date) rather than by what the theory claims. Not one tracker is organized around the theory's questions (what is being claimed about which class of agents). Section 8 develops this.

---

## 2. Measurement corrections for the coordinator's table

- **Segment count.** The README table's 290 counts every `*/src/*.md`. Verified: 44 of those are legacy documents, not segments: 43 `02-tst-core/src/old-tst-*.md` plus `01-aat-core/src/old-tf-appendix-f-multi-agent.md` (281 lines, TFT-era multi-agent appendix). None is in an OUTLINE. **Real segments: 246** (01: 172, 02: 29, 03: 23, 04: 22). Four live TST/AAT segments still cite `old-*` files (`#def-causal-information-yield`, `#der-code-quality-as-observation-infrastructure`, `#hyp-causal-discovery-from-git`, `#scope-developer-agent`).
- **"Theory-body motion: 4 of 436 commits since 2026-08-24."** Verified, with the cause: 377 of the 437 commits since 2026-08-24 touch only `empirica/glyph-sequence-perception/`, a glyph-perception study for notation (Section 7.4) with no canon consumers. Outside that study, everything since 2026-08-24 is the 2026-08-24 decomposition-uniqueness cluster, the 2026-09-23 honest-activation spike plus two de novo verifications, the 2026-09-25 `audits/aat-reboot-aux-supplemental/` findings from the aat rewrite attempt, a 2026-10-10 quote-level-marks spike, and today's commits. Theory work after late August moved out of asf to `~/src/aat-refactored/` and `~/src/aat-v3/`.

---

## 3. The decision backlog (JOSEPH-TODO + the 2026-07-15 valve), sorted for today

Source: `JOSEPH-TODO.md` (last touched 2026-10-05) pointing at `msc/decision-briefs-2026-07-15.md` (2026-07-15; each brief has context, options, lead recommendation, pointer). The briefs were verified against state on 2026-07-15. I re-verified only where noted.

**Theory-substantive (each changes what the theory says):**

| Decision | Bears on | State | Note |
|---|---|---|---|
| SP-30: typed epistemic target $S_t = (\Omega_t, \theta)$ vs state-only $\Omega_t$ | `#scope-adaptive-system`, GA-1 / the three-term mismatch decomposition, bandit and exploit-explore segments | Package complete since 2026-07-04 (`spikes/epistemic-target-ontology/` 00–04; `01-ga1-verification.md` verifies the gating claim, a two-horn no-go under state-only $\Omega$). No lead rec was offered; "the math now favors (1)". | Root ontology. Every segment that meets law-content $\theta$ houses it ad hoc. Also fixes the false exclusion of standard RL (audit 731548 B-3). |
| C5: intelligence–empathy convergence (structural leg in 03, normative-dynamic leg contesting Bostrom's orthogonality in 04) | `#def-cognitive-fusion` (no file), `#obs-backward-inference-empathy` (no file), 04 normative register | Unchanged since 2026-07-04; source `msc/era-artifact-asf-contributions-2026-07-04.md` Addendum 2 | The corpus's boldest claim, with no segment. T-05's 21/21 comprehension-dominance result is offered as its theorem-grade anchor. |
| 01-aat-core ordering: `#impl-persistence-and-limits` (Part I) consumes `#result-per-dimension-persistence` (Part III) | both slugs | Open since 2026-05-22; the one red `bin/lint-outline` item | The segment's own WN says the Part-III content "is essentially Part I". |
| 9 scope-first orderings in 03/04 | 03/04 `scope-*` openers | Whitelist or reorder | Placement, light theory. |
| Separability-ladder rung names (Hintikka echo *definable / identifiable / non-identifiable* vs descriptive) | `#disc-separability-pattern` (rename to `#disc-separability-ladder` pending) | Unchanged since 2026-05; the Hintikka senses were never checked against the ladder's | Publication-facing via `msc/separability-standalone-paper-proposal.md`. |
| Agent-spectrum quadrant names as one parallel set | `#def-agent-spectrum` | No option set exists | Interim "blind seeker" since 2026-05-17. |
| Greek cycle vocabulary: earn each distinction in segments or soften README | cycle-phase segments, `#def-adaptive-cycle`, README | Partly pre-decided (keep Greek, add English anchor) | Voting cohort vs audit-471203 disagree; Joseph sided with the audit ("I've had that exact same complaint"). |
| LEXICON Continuity-to-Persistence reorg; is Continuity Stance an axis or a deployment property | `#disc-continuity-stance`, LEXICON | Breakage twice re-verified | A duplicate `### Persistence` still renders. |
| `#schema-strategy-persistence` hard ceiling (F72, verdict B: name the convention, keep `exact`) | `#schema-strategy-persistence`, `#deriv-strategic-persistence-hard-ceiling` | Held for an "external-eye" gate since 2026-05-31 | Gate now lifted. |
| Five missing Vol-3 segments: write at honest tier, or recast `03-llm-core` `impl-*` passages that describe them in the present tense | `#obs-backward-inference-empathy`, `#form-structured-rich-context`, `#der-active-salience-management`, `#der-self-referential-closure`, `#def-cognitive-fusion` | Open since 2026-08-22 | The present-tense content claims are the defect. |

**Process (each retires a gate or shapes the system; important to the effort, not to the theory's content):** A1 gold-dir standing policy (moot today: Joseph lifted the gate); A4 what replaces stage-gating and what drains Working Notes (Gate 4 never fired; 225 of 280 files carried WN on 2026-07-15); A6 CLAUDE.md as unreviewed amplifier (generate the derivable parts plus a review cadence); de-block Findings from the stalled naming refactor (PRACTICA's 🌟 Findings workstream has been "soft-blocked" behind a naming queue stalled since about 2026-05-10, with 506 of 629 currents unrouted); A7 split 04-eli-core into its own repo (strategic; repo already public).

**Dated out:** FAST @ NeurIPS 2026 workshop deadline 2026-08-29 has passed. I have not checked whether anything was submitted; that sits outside asf.

---

## 4. External research awaiting integration (the lists)

Joseph recalls "a list in there somewhere (or several places) that talks about external research that needs to be integrated." Inside asf there are at least these eight, plus scattered citation debts. Ordered by freshness.

| # | Where | Date (git) | What it asks to integrate | State I could check | Slugs it bears on |
|---|---|---|---|---|---|
| E1 | `ref/prior-art-analysis/agentic-systems-landscape-2026-08-22.md` (117 lines, "a letter to Joseph") | 2026-08-22 | 46 source-verified verdicts on the agentic-systems landscape. Five "sharper news" items: Richens et al. 2025 (competence implies a world model, a converse to AAT's posited model); Baltieri & Suzuki 2025 (agent-criteria survey; a do-surgery objection to `#scope-agency`; a failure-with-persistence gap AAT fills); the Hafez $H_b$ fidelity problem (AAT's $H_b$ is a different, observer-indexed object, so "adopts" should read "generalizes"); Eslami & Yu's stability budget with delay and dwell terms (a strengthening target for the persistence condition); FAST. Also Meulemans et al. (Embedded Universal Predictive Intelligence) as the sharpest foil for `#der-loop-interventional-access`. | 5 rows routed to `spikes/PROPOSED.md` as `ext:` items (verified; all status proposed). Richens is cited in 3 segments, Baltieri in 6 (counts include WN). The Hafez fix is listed in TODO §2026-07-03 source-segment defects, unfixed. | `#form-agent-model`, `#def-model-sufficiency`, `#scope-agency`, `#der-agent-opacity`, `#result-persistence-condition`, `#der-directed-separation`, `#der-loop-interventional-access`, Part III |
| E2 | `ref/layer-3-mechanism-counterfactual-sep.md` + `.csv` | 2026-07-16 | Undermind priority search for `#deriv-mechanism-counterfactual-separation` | Integrated: its result (separation unanticipated; nearest priors positioned) is in the segment's Epistemic Status per commit `70fb215f`; citation debt gated in WN | `#deriv-mechanism-counterfactual-separation` |
| E3 | `ref/prior-art-analysis/` (21 per-topic analyses, 12 novelty memos, `00-impact-meta-summary.md`, `cluster_references/`) + 20 `ref/Prior_art_for_AAT_*.csv/.md` Undermind catalogs | 2026-05-20 to 2026-05-22 (4 cluster files touched 2026-07-14) | Per-topic novelty scoring and nearest prior art for 21 AAT topics. Its meta-summary ranks eight "immediate impact" results (directed separation and class coercion; self-actuation grounding; adversarial tempo; credit-assignment boundary; composite agency and Brooks's Law; Lyapunov persistence; adaptive tempo; continuity stance). | This is a positioning corpus, not a to-integrate list. Its integration demand is implicit: each memo names nearest prior art that canon should cite. The 20 catalogs were bulk-imported into relata (BIBLIOGRAPHY-TODO, 2026-06-04). Row 14's Class 2 vs Class 3 tension is flagged "Joseph-reserved". | every AAT row topic; see the meta-summary table |
| E4 | `ref/enrichment-candidates-2026-05-21.md` (464 lines) | 2026-05-21 | Prior art that could *enrich* AAT toward first-principles agency theory: Conley's fundamental theorem, Hodge decomposition for games, $\alpha$-Rank, symplectic gradient adjustment, Cheung–Piliouras–Tao passivity/regret/recurrence; post-2020 papers (Mertikopoulos et al., Richens, Virgo et al. good-regulator, Cohen–Hutter–Osborne, Smithe, scale-free active inference); adjacent frameworks (constructor theory, sheaf contextuality, Aumann, ZX); cross-disciplinary anchors (cognitive ethology, Csibra–Gergely, Ericsson, Pessoa); lightly used existing citations (Wolpert et al., Rungger–Zamani, Genewein et al., Marzen, Subramanian et al.) | Grep of canon (counts include WN mentions): §1–§2 and §5 are largely touched (Piliouras 7, Genewein 6, Subramanian 5, Conley 3, Mertikopoulos 3); untouched are symplectic gradient adjustment, constructor theory, Abramsky, ZX, Csibra, Ericsson, Pessoa, Wolpert, Marzen, critical slowing down | dynamics and game segments in Part III; `#form-agent-model`; Part I persistence |
| E5 | `02-tst-core/lit-review/next-research.md` + `next-research-append-2..7.md` (+ `result-synthesis*.md`, `SYNTHESIS-temporal-framework-validation.md`, `undermind/`) | 2026-04-01 (moved 2026-05-15) | Research programs for TST: species-specific comprehension (human $T_{base}(1+\alpha)^d$ vs AI forms), optimal control/HJB for software maintenance, economic models (technical-debt interest rates), spectral graph theory for architecture, stochastic processes (Hawkes, queueing), human–AI complementarity baselines, and lists of papers "requiring full acquisition" | Pre-AAT TST vocabulary (FP-0xx / T-xx). Canon reaches it only through `old-tst-*` footnotes. The 2026-07-28 partition-isolation spike reports that this lit-review's "complete absence" verdict on spectral change propagation is mis-scoped (Smith & Eppinger 1997, Giffin et al. 2009, Dobrushin) and flags the correction for its owner, not yet made. | `#hyp-exponential-cognitive-load`, `#meas-coherence-coupling`, `#def-system-coupling`, `#hyp-software-unmaintainability-bifurcation` (no file), TST Ch.2/Ch.4 |
| E6 | `ref/Novelty_defense_and_integration.md`, `ref/Prior_art_for_unified_agency_theories.md`, `ref/separability-ladder-prior-art-report.md`, `ref/Unidentifiability_and_rate_class_prior_art.md` | 2026-04-26 to 2026-05-21 | Undermind framework-level novelty defense; separability-ladder prior art (Hintikka 1991 anchor); unidentifiability prior art | `Novelty_defense_and_integration.md` is still cited by 8 Search-Log rows in `FINDINGS.md` and by segment bodies (`#der-directed-separation`, `#der-causal-insufficiency-detection`, `#deriv-causal-ib-exploration`, `#deriv-causal-ib-lmi`, four TST segments). INTEGRATION-CLEANUP G3 calls that a canon-to-artifact defect. | named segments; `#disc-separability-pattern` |
| E7 | TODO.md §README v2 (Alan Walton's first human review, 2026-04-27) | queued 2026-04-27 | David Deutsch's theory of explanations (*The Beginning of Infinity*, *The Fabric of Reality*) as a conceptual precursor; Alan's "split goal state and model state" as field-grade convergent evidence for $G_t$ vs $M_t$; his testing-scaffolding hierarchy as an engineering anchor | Deutsch: 0 canon mentions (verified). Constructor theory (E4 §3.a, also Deutsch) also 0. | `#disc-additive-coordinate-forcing`, `#disc-identifiability-floor`, `#obs-software-epistemic-properties` |
| E8 | `spikes/PROPOSED.md` `ext:` rows | 2026-08-22 | The E1 follow-ups as spike proposals, plus Jørgensen–Weichwald–Hammond's non-emergence lemma for composites and Virgo & Baltieri arXiv 2508.06326 marked "unread — survey gap" | 5 rows, all proposed (spikes map covers PROPOSED in full) | as E1; Part III composition |

**Citation and novelty-search debts inside canon or spikes** (each is "external research owed" at a single site): six `[^bg2-2026-05-21]` citations in `#disc-identifiability-floor` Instance 3 escape (e) that were "synthesized rather than read" and that a softening rests on, flagged three times (2026-05-21, 2026-07-29, per `spikes/INDEX.md`); a targeted novelty search queued for `#deriv-decomposition-uniqueness` ("required before any external novelty claim"); the class-2 typology prior-art sub-spike, never run (`spikes/spike-class2-typology-2026-05-22/07-prior-art-followon.md`: Kruglanski, Bénabou–Tirole, Akerlof–Kranton, active inference) gating `#disc-partial-coupling-pathways` and `#der-belief-strategy-attractor`; PID-impossibility citations (Williams–Beer; Rauh et al.) flagged for relata verification in `#deriv-tempo-additivity`; acquiring the Hafez IDT paper to check its author list (`ref/INDEX.md:103`); Naur 1985 owed to TST (0 canon mentions, verified); Seligman and Abramson–Seligman–Teasdale owed to `#der-severed-actuation-dynamics` before it advances; the Amari–Nagaoka §3.5 check gating SP-9. And the larger structural debt: about 270 prose author-year references in Vol 1 with effectively zero formal `\cite{}` (BIBLIOGRAPHY-TODO W-3, an author-judgment migration).

**Outside asf, for the influx scout:** `~/src/.moved-and-integrated/relata/IMPORT-ASF-TODO.md` (2026-05-20, found via `memorata-search --no-rerank`) is relata's side of the ASF import plan.

---

## 5. Tracker by tracker

Every tracker below was last touched 2026-08-22 or 2026-08-24, except JOSEPH-TODO (2026-10-05), TST-IDEAS (2026-05-21), PRACTICA (2026-08-22), LEXICON (2026-07-15). The 2026-07-15 "tracker prune sweep" deleted about 103 done items, so what remains is meant to be live.

### 5.1 `PRACTICA.md` (121 lines; the navigator)

What it holds: areas, not items. Its 🌟 cycle priority order (added 2026-05-09) still lists (1) the Gate-1 audit of the four 03 scope segments, (2) Class-3 closure-defect dynamics (Move F of `spikes/temporal-nesting-rg/99-verdict.md`), (3) identity through substrate transitions (`#der-substrate-independent-persistence`, no file), (4) multi-timescale stacking remainders. It also records two register allowances from 2026-05-09 (normative claims where structurally backed; narrative segments) that no segment has yet used as narrative segments. The 🌟 Findings workstream is soft-blocked on naming. Ops lists a "Theory Improvement process and rhythm" with every box unchecked. Judgment: PRACTICA's priority order is five months old and predates the deaths, mood, decomposition-uniqueness, and epistemic-target work; it no longer describes where the theory's frontier is.

### 5.2 `TODO.md` (526 lines; dated sections)

Live theory inside it, by section (examples, not exhaustive):

- **§Strengthen-first candidates from the 2026-05-30/31 gold-lift sweep.** Tier 1: the directed-separation foundation tail, including the substantive point that a frozen LLM with KV-cache violates $(C2')$, so logogenic wrapping may get only a behavioral $W_2$ bound (`#der-logogenic-as-wrapping`, `#def-auxilia-hierarchy`); the hard-ceiling convention; the $(C2')$-realization over-claim in `#def-auxilia-hierarchy` (separate substrate is sufficient, not necessary); the goal-flow duality with a discussion-grade landing available. Tier 2: under-gated "valid composite" (`#der-class-coercion-in-composition`); $C_{\text{coord}}$ double-counted (`#der-tempo-composition`); $U_M$ unnormalized (`#def-unity-dimensions`); "does directed separation compose?" ripe to promote (`#disc-composition-consistency`); `#form-consolidation-dynamics` mis-positioned; C-iv idiom drift across composition segments. These are the "stale gem-hints" the sweep itself warns about.
- **§Open theory items (MEDIUM).** Composition admissibility $\mathcal M_{\text{adm}}$ (🌟 HIGH; `msc/working-composition-admissibility.md`); composition scaling with $N$; deaths-taxonomy follow-ons (D1/D4 terminal forms; continuity-death composition; deaths-as-harms norm segment); mood-layer follow-ons, where the $\dot\alpha$ drift-rate derivation is called "the single highest-leverage next move" because it closes both the capture segment and `#def-mood`; communication-gain adversarial scope; exploit/explore rewrite; adjacent identifiability floors; Class 2 observation-ambiguity bias bound; F28 $\rho_\Sigma$ operationalization; transient dependency amplification's promotion obligations; causal-IB LMI follow-ons; six domain cross-transfer questions; the Pearl/LLM causal-access note (`msc/llm-causal-access-note.md`, 2026-03-09).
- **§Queued spike work.** Misspecification-cost floor; CL-1; heredity axiom; wrapper tempo accounting; empirical $\kappa_{W_1}$ protocols; Class-3 closure-defect dynamics; consolidation stability upper bound; EWC tensor gain; "single axiomatic obstruction behind Cauchy-FE failure + Cramér-Rao rank deficiency".
- **§Parts III + IV active work (2026-05-01).** The longest stranded list for 03/04: eleven 04 promotion candidates and six new-segment candidates (`disc-possibility-space-theory`, `obs-self-model-from-recursion`, `obs-substrate-convergent-kinship`, `def-vera-architecture`, `obs-active-soul-obstructed-not-absent`, `disc-language-as-epistemic-substrate`), many with canonical sources outside asf (synaptic, zoetica, ennaos, firmatum, `_self/writing`). About 50 of 75 Gemini audit notes from AUDIT-WORKING-193847 were never read for this cycle.
- **§2026-05-12 intake, groups (a)–(d).** Preface claim-substantiation pass (Joseph 2026-05-12: "We shouldn't make any claims in prefaces or intro discussions that aren't substantiated or first claimed in an actual claim (segment)"); AAT-1 tensor tempo downstream (the persistence and composition results still read scalar); AAT-8 appendix dependency map; TST-4/7/8; LOGA-1/2/3 scope narrowings; ELI-2 moral/empirical claims boundary; ELI-4/5 measurement protocols for the constitutive factors.
- **§2026-07-03 audit 731548 routing.** Three AAT `impl-*` segments plus TST ×4 and LLM ×4 still owe the status-tagging pass; two lists of source-segment defects from the 2026-08-22 impl passes (about 25 named sites); a legacy quantifier sweep; a floor-routing diagnostic segment ("five independent auditor arrivals converge"); a Volume-4 shadow-catalogue appendix (ten Part-I theorems with Vol-4 readings).
- **Mechanical/editorial, verified still open today:** "nominal" means opposite things in `#scope-agency` and `#post-causal-structure` (WN note present, no rename); `#form-strategy-complexity-cost` and `#deriv-strategy-cost-regret-bound` still list each other in `depends:`, which motivates the proposed `strengthens:` field (a FORMAT change that would encode strengthen-before-soften structurally).
- **Tooling and monograph.** scrbook appendix numbering bug (parked 2026-05-17, pickup-ready, design call open); NOTATION auto-generation; figure-staleness lint; release-notes pipeline; `bin/rename-slug` bare-filename bug; `intro`/`impl` prefix handling in `bin/align-slug`.

### 5.3 `PROPOSALS.md` (442 lines; architectural portfolio)

Structured by readiness bands from the 2026-04-24 consolidation audit, with per-proposal value scores. Live structural moves:

- **Bundle 1, framework-face reframe** (+9/+10, "the highest-leverage single move available"): shift public self-presentation from "integrates four disciplines" to "epistemic architecture". Still unlanded per its own text: `_position-and-lineage.md` still leads with "integrates four mature disciplines"; `#scope-agent-identity` `type: scope` to `postulate`; the dual-edged floor/separability touches. HISTORICAL-CONTEXT §"What ASF Is" still opens "At the level of *integration*" (verified), consistent with this.
- **Bundle 2, Section III completion** (+7): population-level Lyapunov (O-BP16), typed admissibility (O-BP9), composition-monotonicity meta-segment (SP-11), goal-information leakage $\mathcal L_{G \to M}^c$ as a first-class quantity (SP-17). Closes the four OUTLINE GAP rows.
- **§D investigation-first:** observability as master variable (O-BP11; "is observability one variable or four sharing a name?"); Fisher unification of tempo and gain (G-BP3, "substantively hollowed out"); commitment/resource/temporal DAG extensions (SP-12, the BDI desire/intent split; this is the missing-structure item CLAUDE.md lists under Known Fragilities, and bears directly on Joseph's strategy-DAG question); emergence conditions as formal primitive (SP-13); resource budget $B_t$ (O-BP12); template-family naming (SP-15); independence profile instrument (SP-16); CL-1 residual (SP-22).
- **§G/§SP late entries:** SP-21 composite-route ontology split (open architectural decision); SP-23 theorem-import meta-segment; SP-27 introspective-fork undetectability, "why the deaths are *experienced*" (verified-real gem, awaiting a Part-IV bridge call); SP-29 infrastructure-as-active-monitor meta-segment; SP-30 (Section 3).

Judgment: PROPOSALS is the closest thing to a map of what the theory might become, but its value scores and bands date from April–May and from a framework-presentation frame. Several items (SP-12, O-BP11, SP-13, SP-27) are exactly the kind of "what is this theory saying universally" questions Joseph raised today, scored as optional extensions.

### 5.4 `TST-IDEAS.md` (450 lines; 2026-05-21)

A substrate from mining the roughly 960-analysis TST corpus at `~/src/_core/tst/planning/analysis/` (outside asf; influx scout territory), then seven spikes. Its §9 is the clearest stranded-theory statement in the repo:

- Theorem-grade: the **wrapper-level persistence inequality** $\mathcal T_\text{wrapper} := 1/T_\text{restart} \gt \rho_\text{child} \lVert\delta_\text{failure}\rVert / \lVert\delta_\text{critical}^\text{wrapper}\rVert$, with `max_restarts/max_seconds` as its estimator; landing target `#der-wrapper-persistence-condition` under `#der-class-coercion-via-wrapping`. No file, no OUTLINE row (verified).
- **Actuated $\rho$-regulation** with an AAT-internal sign condition (admission control helps persistence on channel $k$ only if $\rho^{(k)}/(\nu^{(k)}\lVert\delta_\text{critical}\rVert) \gt \eta^{(k)\ast}$); targets `#disc-rho-actuation` + `#deriv-actuated-disturbance-rate`. No files.
- Segment-ready: `#def-developer-tempo-channels`, `#scope-running-software-agent` (+3 siblings), `#hyp-software-unmaintainability-bifurcation`. No files; two are OUTLINE GAP candidates.
- Still spike-grade: Conway's Law as a GUC-class bound; substrate-modifying actions as class 4c; composite sat-gap aggregation under admission control.

### 5.5 `INTEGRATION-CLEANUP-TODO.md` (86 lines)

Carries the ratified D-1 principle (canon cites only canon and the published world; WN are not canon) and its open tails: G1 CLAUDE.md audit; G3 citation tails; G4 naming sims as spike-class; G5 CLAUDE.md as amplifier. Two open items bear on the whole effort: Joseph's hedged **provisional thought** that segments need no per-segment histories because traces live in `{spikes,audits}/.integrated/` (unblocked 2026-07-16, awaiting ratification), and the named gap **"no process for draining WN follow-ups"** (proposal in `msc/wn-discipline-coherence-pass-2026-05-31.md`, not adopted).

### 5.6 `TODO-big-picture.md` (64 lines; 2026-05-16 vintage, touched 2026-08-22)

Self-corrected in its own header: W1/W2 "wrong as framed"; W4 done. Live: **W3**, a per-result read of which segments hold the calibrated register versus the flattened one, with the denominator being the `impl-*` layer. It also carries Joseph's 2026-05-16 cleanup principle (state the kind, drop magnitude disclaimers) and flags that its own "in kind, not magnitude" guard violates that principle, "left verbatim pending his hand". The 2026-08-22 impl passes did part of W3's work without referencing it.

### 5.7 `FORMAT-TODO.md`, `BIBLIOGRAPHY-TODO.md`, `TERMINOLOGY-TODO.md` (infrastructure)

- FORMAT-TODO (2026-08-24): citation, cross-ref, footnote, and sidenote conventions; C12 an *AAT-native vs imported* visual distinction (relevant to the math-novelty question); C14 a schema split for discussion segments; C17 chapter grouping *quality* (Joseph's concern).
- BIBLIOGRAPHY-TODO (2026-08-22): relata holds the bibliography; the build emits `.bib`; segment migration of about 270 prose references is the open author-judgment work.
- TERMINOLOGY-TODO (2026-08-22): C8 and C12 residues; §D 13 deferred decisions; §E agent-spectrum tetrad; §F LEXICON Continuity reorg. The 506 unrouted naming currents live in the packed `.archive/msc-naming-2026-08-22.tar.gz`, which `bin/naming-*` tools still expect unpacked. The terminology *system* is migrating to the Archema level (`archterm`).

### 5.8 `HISTORICAL-CONTEXT.md` (94 lines, 2026-08-22)

The long-form positioning document (lineage; comparisons with active inference, Miehling/IBM 2025, Hafez 2026, Miller 2022, Baigozin 2025, OODA). It predates the 2026-08-22 landscape letter (E1), whose verdicts (Richens, Baltieri & Suzuki, Eslami & Yu, Meulemans et al., the Hafez fidelity issue) have not reached it.

---

## 6. OUTLINE GAP and missing-file rows (verified today)

| Component | OUTLINE slugs with no file | `--GAP--` rows |
|---|---|---|
| 01-aat-core | `worked-example-cam` (renders *(missing)* in the v0.4.0 snapshot), `fig-driver-snow-foundation` (a figure slug) | 4 untitled Discussion GAPs in Parts II–III (rows 170, 188, 240, 260, 297); 4 titled population-level GAPs (rows 304–307: latent structural diversity; endogenous coupling $\gamma$; composition transition dynamics after Miller 2022; computational thresholds for social behavior) |
| 02-tst-core | `def-developer-tempo-channels`, `hyp-software-unmaintainability-bifurcation` (both resolved to segment-ready by spikes, 2026-05-21) | 3 untitled Discussion GAPs (rows 43, 68, 90) + the two candidate rows |
| 03-llm-core | `def-cognitive-fusion`, `der-active-salience-management`, `der-self-referential-closure`, `disc-tool-interface-design`, `form-ephemeral-persistent-duality`, `form-structured-rich-context`, `obs-backward-inference-empathy` | — |
| 04-eli-core | `def-century-scale-event-log`, `def-character-aspiration-dialectic`, `def-gradient-causal-memory`, `def-the-four-views`, `der-substrate-independent-persistence`, `der-the-creche-boundary`, `der-the-scaffolding-tax`, `form-congruency-selfhood`, `form-constitutive-utterance`, `norm-honest-activation`, `norm-temporal-coherence-markers`, `obs-axiom-genesis`, `obs-substrate-independence` | — |

(`ii-actuated-adaptation-agentic-systems`, `working-conventions`, `source-material` matched my slug regex in OUTLINE prose but are anchors, not segment rows.) Note on 04: many of these rows describe operational PROPRIUM/zoetica/firmatum infrastructure (GCM, CHRONICA, the four views, the crèche), so their canonical sources are outside asf.

---

## 7. Peripheral directories

### 7.1 `02-tst-core/src/old-tst-*.md` (43 files, 7,739 lines; last content change 2026-04-01, sweeps since)

Pre-AAT TST: the first-principles and theorem files (`old-tst-t01` … `t15`, `d01` … `d08`, typed `Theorem`/`Definition` with subtypes), syntheses, the 960-analysis synthesis, the meta-analysis priority rankings (1,017 lines), the TFT-mapping set, and an AI-specification-limit note. They live in the canon directory but are in no OUTLINE, so a reader sees them as segments and the build does not. Whether all of their content has a modern home I could not tell without reading them against the 29 TST segments; the T-xx numbering in the 2026-07-04 independent-derivations spike (T-01 … T-13) is this corpus's, and that spike found several T-items (T-01 axiom, T-03, T-04, T-07, T-11, T-12, T-13-operational) "never reproduced" by naive derivations, so they rest on premises the current TST does not state. Worth an integration agent's dedicated pass: map each `old-tst-*` claim to a live segment, a TST-IDEAS candidate, or a deliberate retirement. Same treatment for `01-aat-core/src/old-tf-appendix-f-multi-agent.md`.

### 7.2 `02-tst-core/lit-review/` (40 files, about 15.4k lines; 2026-04-01) and `02-tst-core/empirical-discontinuity/`

The literature review is Section 4 E5. `empirical-discontinuity/` (2026-04-01) is a toolkit testing $T_\text{comprehend} = T_\text{base}(1+\alpha)^d$ on git history, with its own FINDINGS.md and METHODOLOGY.md; two live segments (`#der-code-quality-as-observation-infrastructure`, `#hyp-exponential-cognitive-load`) reference it by path. Under the D-1/R3 principle it should either become an `empirica:` entry with a MANIFEST and RUNS record, or its claims should be restated without the path. INTEGRATION-CLEANUP G4 lists it; not done.

### 7.3 `ref/agentic-tft/` (8 files, 2,667 lines; originals 2026-02, copied in 2026-04-28)

Pre-AAT "agentic TFT" bridge documents: foundational premises, ontology unification, cognitive-loop spec, evaluation framework, crèche concept, experiential training, narrative as implementation, and a review response cataloguing internal inconsistencies, each sorted fix-now / accept / disagree / flag-for-Joseph. Eight live segments and the 03/04 OUTLINEs reference them (verified by grep; I did not check whether in body or WN). The crèche and experiential-training documents are named as canonical sources for `#der-the-creche-boundary` and `#form-constitutive-utterance` (no files). The review response's "flag for Joseph" items have, as far as I can see, never been re-surfaced.

### 7.4 `empirica/`

- `track-b-nonlinear/` (registered 2026-07-16): the Section-I validation simulations, with five canon consumers. Its INDEX row says vivarium rerun "planned". Healthy.
- `glyph-sequence-perception/` (2026-08-25 to 2026-10-10; about 33k lines tracked, plus gitignored answer ledgers; 377 commits): a study of which glyph sequences LLM minds perceive, for notation and mark design (the `spikes/quote-level-marks` spot check of 2026-10-10 draws on it). MANIFEST: "No claims. … Consumers: None." Halted 2026-10-06 by Joseph's choice. It is not ASF theory content. Its relevance here is that it dominates recent git history, and its interim results bear on notation choices (`NOTATION.md`, udon marks), not on agency. Whether it belongs in asf's `empirica/` at all is a fair question for the effort.

### 7.5 `releases/`, `CURRENT-VOL1*`, `NOTATION.md`, `doc/DOMAINS.md`, `01-aat-core/INTRODUCTION.md`

- `releases/v0.4.0.md` (2026-08-15/22): its "four results anchor the volume" list (Persistence Threshold, Containment Dichotomy, Stability Equivalence, Architectural Classification) is the most recent authoritative statement of what Vol 1 claims, mirrored in `01-aat-core/INTRODUCTION.md`. For Joseph's "what is this theory trying to illuminate", these two files are the current answer as written, and the strategy DAG is not among the four.
- `CURRENT-VOL1.md` (2026-08-22) predates the 2026-08-24 decomposition-uniqueness landing; it is a generated snapshot and simply stale by one cluster.
- `NOTATION.md`: self-declared "lagging index, not the arbiter"; auto-generation queued since 2026-05-09/18.
- `doc/DOMAINS.md` (2026-07-03, "working draft, exploratory"): a domain-instantiation table on four axes (scope tier, knowledge type, GUC class, arity), canon-cited from INTRODUCTION as a breadth reference. It is the closest existing artifact to Joseph's request to map theory classes onto concrete, testable examples.

### 7.6 Git state

No stranded branches: `tmp-new`, `guc-rename-2026-05-09`, `auto` are all fully merged into main (0 commits ahead). No stashes. Untracked: `msc/joseph-working-notes.md` (gitignored, mtime 2026-04-29; the msc map has it); `.claude/` and `.practica` files are local tool state.

---

## 8. The tracker system as a system (thoughts the frame invites)

- **Trackers are indexed by provenance and date; the theory has no index by question.** Every tracker section is titled by its origin ("2026-05-12 intake", "audit 731548 routing", "gold-lift sweep"). An integration agent who wants everything bearing on, say, composition, or on what the strategy DAG claims, must read all of them. The join table below is a first slug-keyed view; a question-keyed view ("which class of agents does this claim hold for, and what would test it?") does not exist anywhere and would serve Joseph's stated loss of clarity directly.
- **The valve worked as a design and failed as a flow.** The 2026-07-15 decision briefs are excellent (decidable from the brief alone), but almost none were decided in 3.5 months, and items marked "Joseph-reserved" or "awaiting go-ahead on placement" became the longest-lived stranded theory (TST §9, SP-30, C5, SP-27). With today's gates lifted, the effort could treat every brief with a lead recommendation as decided-by-default, and spend Joseph's attention only on SP-30, C5, A7, and naming.
- **The WN drain gap is the same failure at a smaller scale.** INTEGRATION-CLEANUP names it: a WN future-work item has no route to being picked up. TODO's 2026-05-30/31 tier lists are one attempt; they carry their own warning that half the first items were already resolved.
- **Self-staleness is pervasive and honest.** Trackers warn about themselves (NOTATION "lagging", TODO-big-picture "wrong as framed", TODO "stale gem-hints, verify first", INDEX "convenience record, not ground truth"). That honesty raises the cost of using them: every item needs re-verification. A tooling idea: a `bin/` check that resolves every `#slug` and file path named in a tracker, reports which named slugs have no file, and which tracker items name segments whose git history has moved since the item's date. That would turn "stale-until-checked" into a sortable list.
- **Gate words became a stall pattern.** "Joseph-reserved", "awaiting Joseph", "external-eye gate", "go-ahead on placement" each parked real results for months. The same words recur across the spikes map's territory (ROUTING.md's Joseph batch). Worth stating in the effort's SOPs what replaces them now.

---

## 9. Slug join table

Key: **T** TODO · **P** PROPOSALS · **Pr** PRACTICA · **TI** TST-IDEAS · **JT** JOSEPH-TODO/decision briefs · **IC** INTEGRATION-CLEANUP · **E#** Section 4 list · **O** OUTLINE GAP/missing · **old** legacy files. "No file" = slug named but absent from `src/` (verified).

| Slug | Surfaces | Kind | Latest date |
|---|---|---|---|
| `#scope-adaptive-system` | P SP-30, JT | root-ontology decision (typed target $S_t$) | 2026-07-04 |
| `#form-agent-model`, `#def-model-sufficiency` | E1, E8 | adopt Richens et al. converse | 2026-08-22 |
| `#scope-agency` | E1, E8, T (nominal) | answer the do-surgery objection; nominal-term collision | 2026-08-22 |
| `#post-causal-structure` | T (nominal) | rename "nominal coupling" to "query-only coupling" | 2026-05-29 |
| `#der-agent-opacity` | E1, T | Hafez $H_b$ is a refinement, not an adoption | 2026-08-22 |
| `#result-persistence-condition` | E1, E8, T (bathtub) | delay/dwell strengthening; Feynman brief | 2026-08-22 |
| `#impl-persistence-and-limits`, `#result-per-dimension-persistence` | JT, T | ordering call (move result to Part I) | 2026-05-22 |
| `#disc-identifiability-floor` | T (adjacent floors), cite debt (bg2), ROUTING (operator-layer no-go) | three floor extensions; six unread citations | 2026-07-29 |
| `#disc-separability-pattern` | JT, T, E6 | rename to ladder + rung names | 2026-05-04 |
| `#def-agent-spectrum` | JT, TERMINOLOGY §E | quadrant-name set | 2026-05-17 |
| `#der-directed-separation` | T Tier 1, P CL-1 | foundation tail; port-structure addition | 2026-05-31 |
| `#der-logogenic-as-wrapping`, `#def-auxilia-hierarchy` | T Tier 1 | frozen LLM + KV-cache violates $(C2')$; necessity over-claim | 2026-05-31 |
| `#der-class-coercion-via-wrapping` | TI §9 | host for the wrapper persistence theorem | 2026-05-21 |
| `#der-wrapper-persistence-condition` | TI §9 | theorem-grade, no file, no OUTLINE row | 2026-05-21 |
| `#disc-rho-actuation`, `#deriv-actuated-disturbance-rate` | TI §9 | new AAT segments, no files | 2026-05-21 |
| `#def-developer-tempo-channels`, `#hyp-software-unmaintainability-bifurcation` | TI §9, O, T (TST §1887) | segment-ready, no files | 2026-05-21 |
| `#scope-running-software-agent` (+3) | TI §9 | runtime-agent chapter, no files | 2026-05-21 |
| `#def-system-coupling`, `#meas-coherence-coupling` | E5, partition-isolation spike | branching-process criticality; lit-review correction | 2026-07-28 |
| `#form-composition-closure`, `#der-team-persistence`, `#deriv-critical-mass-composition` | P Bundle 2, T AAT-1, T $\mathcal M_{\text{adm}}$ | Section III completion; tensor lift | 2026-05-12 |
| `#dissipativity-template` | P D.9, T | CL-1 coupled landing, no file | 2026-05-17 |
| `#der-tempo-composition` | T Tier 2 + 2026-08-22 defects | $C_{\text{coord}}$ double-count | 2026-08-22 |
| `#def-unity-dimensions`, `#result-unity-closure-mapping` | T Tier 2, T editorial | normalization; route count; C-iv drift | 2026-08-22 |
| `#scope-composite-agent` | T F8/F-V3, P SP-21 | C-iii without $O_c$; route-ontology split | 2026-04-25 |
| `#def-strategy-dag`, `#def-strategy-dimension` | P SP-12, T defects | commitment/resource/temporal structure | 2026-08-22 |
| `#form-strategy-complexity-cost` and `#deriv-strategy-cost-regret-bound` | T editorial | mutual `depends:`; `strengthens:` field idea | 2026-05-29 |
| `#schema-strategy-persistence` | JT F72, T Tier 1 | hard-ceiling convention | 2026-05-31 |
| `#disc-dynamic-regime-axis` | T (Track A Phase 6) | promotion to a fifth meta-pattern, unblocked since 2026-05-24 | 2026-05-25 |
| `#def-mood`, `#der-mood-timescale`, `#der-captured-objective-dynamics` | T | $\dot\alpha$ drift-rate derivation, called highest leverage | 2026-07-03 |
| `#def-death-as-factor-loss`, `#der-severed-actuation-dynamics` | T | D1/D4 terminal forms; harms norm; Seligman adoption | 2026-06-17 |
| `#def-cognitive-fusion`, `#obs-backward-inference-empathy` | JT C5, O, T | no files; C5 home | 2026-08-22 |
| `#form-structured-rich-context`, `#der-active-salience-management`, `#der-self-referential-closure` | JT, O, T | no files | 2026-08-22 |
| `#disc-tool-interface-design`, `#form-ephemeral-persistent-duality`, `#form-congruency-selfhood` | T (2026-07-04), O | no files | 2026-07-04 |
| `#obs-substrate-independence`, `#der-substrate-independent-persistence` | Pr, T, O | no files; preface-load-bearing | 2026-05-09 |
| `#norm-honest-activation` | T, O, honest-activation spike (spikes map) | no file | 2026-09-23 |
| `#der-the-creche-boundary`, `#form-constitutive-utterance` | T, O, `ref/agentic-tft/` | no files | 2026-05-01 |
| `#hyp-exponential-cognitive-load`, `#der-code-quality-as-observation-infrastructure` | `empirical-discontinuity/`, old | path references to unregistered toolkit | 2026-04-01 |
| `#scope-developer-agent`, `#hyp-causal-discovery-from-git`, `#def-causal-information-yield` | old | cite `old-*` files | 2026-04-01 |
| `#deriv-decomposition-uniqueness`, `#form-complete-agent-state` | cite debt | novelty search queued | 2026-08-24 |
| `#disc-partial-coupling-pathways`, `#der-belief-strategy-attractor` | cite debt (class-2 prior art) | Pillar search never run | 2026-05-22 |
| `#scope-agent-identity` | P Bundle 1 | `type: scope` to `postulate` | 2026-04-24 |
| `#disc-stability-certificate` | TODO-big-picture | in-canon register exemplar; W3 census | 2026-05-16 |
| `worked-example-cam` | O, T AAT-9 | missing appendix | 2026-05-12 |

---

## 10. Limits of this map, and feedback on the brief

- I read the trackers whole except PROPOSALS (§B/§C/§E bodies skimmed) and FORMAT/BIBLIOGRAPHY/TERMINOLOGY (headings and open items only). I did not read the `old-tst-*` files, the lit-review bodies beyond the next-research files' headings, `ref/agentic-tft/` beyond one header, or the 21 prior-art analyses beyond the meta-summary. Section 7.1's "worth a dedicated pass" is a judgment from size and placement, not from content.
- Canon grep counts include Working Notes mentions, so "cited in N segments" overstates integration.
- I re-verified a handful of tracker items (nominal collision, mutual depends, C-iv drift note, missing files, TST §9 landings, PROPOSED `ext:` rows). I did not re-verify the roughly 25 source-segment defects in TODO §2026-07-03.
- On the brief: the surface list was good. One thing it missed, and that mattered: `*/src/` contains non-segments, so per-segment measurements made with `ls */src/*.md` are inflated by about 18%, and the TST figure most of all (72 vs 29). A second: recent git history is dominated by one non-theory study, which a commit-count measure of "motion" hides.
