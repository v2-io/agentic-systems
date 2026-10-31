# Drain: `01-aat-core` Working Notes outside the audit-gold blocks

*KR I.9 of `../INTENT.md` (every backlog surface drained into the ledger, one disposition per source item), serving I.10 (signal against noise) and I.5 (Working Notes carry only forward pointers and regression guards). Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." Working file, 2026-10-30, written as it goes.*

*Complete: all 752 items have one disposition each, and every part's file is merged here. The summary of what the drain found comes first; the per-item record follows under Dispositions.*

## What this covers, and how it was cut

**Extraction.** At asf `dc2b262c` (main), every `01-aat-core/src/*.md` `## Working Notes` section was split into items: a top-level bullet or numbered item with its nested lines, a paragraph, or a sub-headed block. Every `### …Incidental audit gold…` block is excluded down to the next heading of level 3 or above, with its `####` sub-blocks (Off-ramp, Follow-up, Belongs elsewhere, Readers ask, figures). That leaves **752 items in 142 segments, about 442k characters.** The earlier map's figure of about 1,317 counted all four volumes.

**The seam with the gold-lift drain.**

- `impl-persistence-and-limits`'s `### Teaching frames and implications (audit gold, lifted 2026-08-22)` block (from its line 104 to the end: the misquotation catalog, Candidate Discussion, the shadow catalogue, Candidate figures; 19 items) is gold under a different heading. It is left to the gold-lift drain and is named here so it cannot fall between us.
- Every `Off-ramp` block in 01 sits inside a gold block, so all of them belong to the gold-lift drain. The non-gold items here only *mention* an off-ramp (`der-agent-opacity`'s 2026-07-16 landing note; `impl-persistence-and-limits`'s "failure-boundary geometry" item).

**Live lanes.** Three worktrees were editing 01 segments when this ran: Part I round 3 (`def-mismatch-signal`, `der-deliberation-cost`, `deriv-matrix-persistence-condition`, `deriv-sector-condition`, `deriv-stochastic-non-exit`, `detail-operationalization`, `hyp-mismatch-dynamics`, `impl-persistence-and-limits`, `result-contraction-template`, `result-persistence-condition`, `result-sector-persistence-template`); A.1 round 5 (`def-action-transition`, `def-observation-function`, `example-kalman`, `scope-adaptive-system`); Volume 4 round 3 (`def-chronica`, `persistence-and-limits-intro`, `scope-agent-identity`). An item on those segments that a lane is fixing is marked *in flight* rather than filed as a fresh defect.

**Disposition vocabulary.**

- **canon**: already said in the segment body (or another segment's), checked at HEAD; where.
- **superseded**: overtaken; by what (segment, commit).
- **defect → item**: canon says something wrong that is not yet fixed; ledger item under the KR it serves.
- **owed → item**: true or worth having, never reached canon; ledger item at its honest tier.
- **joined item:x**: an existing ledger item already carries it; this source added to that item.
- **guard**: stays as a forward pointer or regression guard (what I.5 keeps).
- **set aside**: with the reason (history or provenance narration that belongs in CHANGELOG and git; a dead pointer; a stale question).
- **in flight**: a live lane is changing exactly this.

## Partition

*Coverage as of the commit that carries this line; updated in every commit of this drain. The `file` column names where a part would have gone had helpers run; with one agent, every part's dispositions are in this file.*

| part | OUTLINE sections | items | segments | file | coverage |
|---|---|---|---|---|---|
| p1 | Appendix A, `der-belief-…` to `deriv-mismatch-…` | 79 | 17 | `wn-01-other-p1.md` | **done** by the p6 helper: every item read whole and disposed; merged below (this commit) |
| p2 | Appendix A, `deriv-persistence-cost` to the end | 113 | 24 | `wn-01-other-p2.md` | **done** by a helper fork: every item read whole and disposed; merged below |
| p3 | Part II Meta-Architecture I | 104 | 16 | `wn-01-other-p3.md` | **done**: every item read whole and disposed (this commit) |
| p4 | Part I (all chapters) and the Part II preface and Lift | 141 | 28 | `wn-01-other-p4.md` | **done**: every item read whole and disposed (4d8bb49a, 9fcddd48, f0f81911) |
| p5 | Part II Causal Access, Strategy Structure, Strategy Dynamics, Orient Cascade | 130 | 25 | `wn-01-other-p5.md` | **done** by a helper fork: every item read whole and disposed; merged below (this commit) |
| p6 | Part III Meta-Architecture II, Scope and Formation, Composition Machinery | 85 | 11 | `wn-01-other-p6.md` | **done** by a helper fork: every item read whole and disposed; merged below (this commit) |
| p7 | Part III Unity, Cooperative/Adversarial, Strategic Composition; Appendix B | 100 | 21 | `wn-01-other-p7.md` | **done**: every item read whole and disposed (this commit) |

**Helpers.** The first six fork launches were refused (the session's subagent cap). Later, forks went through for p5 and p6; the p6 fork then also took p1, and a third fork took p2. This agent read p4, p3 and p7. Each helper wrote a part file, which was read whole, merged here and deleted; the `file` column names those part files, which no longer exist.

**Cross-surface rule (Joseph, relayed 2026-10-30).** For each item that makes or joins a ledger entry, the other surfaces were searched for the same claim (slug and key phrases over `audits/`, `spikes/`, `msc/`, the influx regional files, other segments' Working Notes, `items/`, `questions/`). One ledger item carries every source found. Canon, history and guard dispositions were not searched across surfaces; nothing turns on them.

## What the drain found

**Coverage.** 752 of 752 items have a disposition, checked by script against the extraction ids. This agent read p3, p4 and p7 whole (345 items). Helper forks read p1, p2, p5 and p6 whole (407 items). This agent read each helper's file whole before merging it, but did not re-read the 407 items under it. A body check means a grep of the segment body (Working Notes excluded), plus a read of the paragraph where the grep hit. Where a disposition rests on the note's words alone, its line says so. Cross-surface search was a grep of the ledger (`items/`, `questions/`) for each owed or joined item, plus targeted greps of `audits/`, `spikes/`, `msc/` and the influx files on key phrases. It was not an exhaustive per-item sweep. `memorata-search` was not used, and no influx primary was opened.

**Dispositions, all parts.** canon 79 · superseded 12 · owed or defect, into ledger items 212 · joined an existing ledger record 175 · guard 106 · set aside, with reason 164 · unclassified by the tally 4. The p1, p2, p5 and p6 figures are the helpers' own counts. The p3, p4 and p7 figures come from a script that takes each line's first disposition word, so an item split across two dispositions counts once, and the four unclassified are multi-id lines the script mis-split. Read the totals as good to a few items, not exact.

**Ledger effect.** 108 items opened (62 here, 46 by helpers) and about 107 sources raised onto existing items and questions. One pair was opened twice in parallel: `item:composition-closure-regime-scope-unstated` is closed as a duplicate of `item:part-iii-segments-name-their-regime-tier`. New items by owner: C.4 74 · G.2 8 · F.2 8 · A.1 5 · H.1 4 · C.1 4 · E.2 3 · C.3 1 · I.5 1.

**What I.5 inherits.** About 106 items stay as forward pointers and regression guards. That is about one Working-Note item in seven. Every other item is now in canon, in the ledger, or set aside with a reason recorded here, so it can leave the Working Notes. Three hazards for that cleanup:
- Some bodies cite their own Working Notes for content: `#der-observability-dominance`'s Claim Record and `#def-chronica`:17 so far. The content has to move before the note is deleted (item:canon-bodies-point-into-working-notes, I.5). Grep bodies for "Working Note" first.
- Several kept pointers name spike paths that moved to `spikes/.integrated/`: `fight/`, `spike-enrichment-cluster1/2-2026-05-21/`, `spike-value-object-convention-monotonicity-2026-05-30/` (the last holds reproducibility scripts), and `spike-causal-level-4-strictness-2026-07-16.md`. Repoint them; don't delete them.
- Some guards carry stale text that should be fixed when the guard is kept. `#deriv-convention-monotonicity`'s dead-end guard still states the (PC)/(SO) characterization the Part II check refuted (raised onto review:part-ii-check-1-b1-records#F1). `#der-team-persistence` and `#deriv-sector-condition` use retired deaths names.

**Findings that change what canon says, in my judgment ordered by consequence.**
1. **Exact results stated without premises their own notes name.** `#result-adversarial-tempo-advantage` calls its exponents exact without saying tempo is treated as exogenous or that scalar tempo assumes channel independence (item:adversarial-tempo-advantage-unstated-premises). `#deriv-gain-sector`'s bridge is an expectation-level argument and does not say so (item:gain-sector-bridge-in-expectation-scope). `#form-composition-closure` never names the R0 regime its (A2) and (A4) presume, and neither do its Part III citers (item:part-iii-segments-name-their-regime-tier). In all three the honest form is in the Working Notes, a few lines below the overstated body.
2. **Mathematics that lives only in Working Notes.** The Mori–Zwanzig upper bound $\varepsilon^\ast \le C\lVert K\rVert$, with no derivation written anywhere (item:composition-closure-mz-upper-bound-unverified). The measured dynamic-$\theta$ behaviour of `#der-tempo-composition`'s own witness (item:tempo-composition-dynamic-theta-witness). The result of the search that makes M3 a single-agent family (item:additive-coordinate-forcing-is-single-agent). Each needs verifying, then landing or deleting.
3. **Joseph's thinking with no home but a Working Note.** The grounding/intent reading of directed separation, the plainest answer in asf to why goal-update coupling governs so much (item:grounding-intent-reframe-of-directed-separation). The TRACTUS/CHRONICA question he asked to have documented (item:tractus-chronica-split-for-logogenic-implementation). His 2026-08-22 hypothesis that decoupling can itself be self-defeating (item:decoupling-self-defeat-modes).
4. **Small canon breakages.** `#disc-continuity-stance` cites `#self-actuated-agent`, which no segment has (item:self-actuated-agent-dangling-slug). `#der-orient-cascade` states its virtuous/vicious cycle with no tag, and its own note says the cycle is underived (item:orient-cascade-virtuous-cycle-underived).

**A note on the tree, for the lead.** 74 of the 108 new items sit under C.4. Its wording, "Part III and the open strengthenings outside C1–C3 have an owner", fits them, but it now holds most of the theory's open frontier as recorded in Working Notes, in one undifferentiated pile. If C.4 is to be worked, it probably wants sub-KRs by cluster: the strategy-DAG optimality questions; composition and closure; the persistence extensions; the impossibility clusters; the coupling typology. Those clusters are visible in the item slugs. I have not proposed them in INTENT; that is the lead's call.

**Mistakes made and corrected in this drain**, kept here so a reader can weigh the rest:
- p4 first said Volume 3 carries the IDT sidecar pattern; it is only in a 03 Working Note, and is now owed.
- p3 said two spike paths were gone when they had moved; the raise that repeated this is annotated.
- An item said no analysis of edge-update double counting existed when `spikes/.integrated/spike-edge-semantics-resolution.md` §7 has one; the item now says so.
- A merge script deleted p2's file before its content reached this one; the helper rewrote it and it was verified complete before merging.

## Dispositions

Item references are `[n]` (this drain's extraction id) plus the head of the item as it reads at `dc2b262c`; line numbers will shift when the lanes merge.

### Part p4 — Part I, the Part II preface and the Lift

#### `def-agent-environment` (Candidate scope question — boundary integrity, 7 items)

- [10]–[16] "The gold above (§3, Gemini AUDIT-WORKING-193847) records…" through "**What this is not.** Not a finding…" — one argument in seven paragraphs. **owed → item:boundary-integrity-second-constitutive-commitment** (question, A.1). Not in canon: the body names only the information-loss commitment. The same gem was adjudicated "not in canon" in `audits/.gem-hunt-trail/GEM-WORKING-193847/adjudication.md` B1, which also names the first task (decide whether the reward-channel no-gos already imply it). Other sources: this segment's gold line 65 (gold-lift drain), `audits/audit-findings-193847.md:113`, `audits/aat-reboot-aux-supplemental/01-def-agent-environment.md:62` ("Nothing else in the repo tracks it"). The conjecture in [15] (permeability and Class 3 coupling one fact, and whether wrapping repairs both) is carried in the item.

#### `def-agent-spectrum`

- [17] "**Candidate reframe of the two axes (pedagogical — not a theorem change).**" — the grounding/intent reframe ("the entire content of agency is the protected 1%"). Not in canon (`grounding`, `wishful`, `99` absent from bodies and ledger). **owed → item:grounding-intent-reframe-of-directed-separation** (H.1 framing layer, pedagogy grade; the owner review's top stranded item, `internal-surfaces/working-notes.md` §4.1).
- [18] "**Truthification reading.** Grounding is the agent's *truthfulness about reality*…" — part of the same reframe; carried in item:grounding-intent-reframe-of-directed-separation.
- [19] "**Temporal subtlety — what is load-bearing vs. a restatement.**" — the refuted "arrow of time as the $M_t/O_t$ separator" with the $\hat o_t$ counterexample. **guard** (a dead-end warning, kept).
- [20] "**The one genuinely-new thread: where the dangerous coupling concentrates.**" — the latent-present leakage locus. **joined item:land-the-leakage-locus-result-of-spikes-spike-le** (G.2, opened by the spike drain from `spikes/spike-leakage-locus-2026-05-18.md`); this Working Note is the plain-language statement of what that landing carries.
- [21] "**Complementary localization — through-what-stage of $f_M$.**" — the composition of the locus with `#disc-partial-coupling-pathways`' stage axis. **joined item:land-the-leakage-locus-result-of-spikes-spike-le** (same landing; the pathways body already says it).

#### `def-chronica` (Volume 4 lane live on this segment; its change touches only the non-forkability wording)

- [22]–[28] "Open question: TRACTUS / CHRONICA split…" (seven paragraphs, ending "Probable resolution: the distinction does need first-class treatment when logogenic implementation is in scope…"). Joseph's own framing (2026-05-01) asked that the question be documented. No ledger item, no 03 segment carries it (`tractus` absent from canon and ledger). **owed → item:tractus-chronica-split-for-logogenic-implementation** (G.2, owner of Volume 3), with the first half of [33] as its forcing use case.
- [29]–[32] "Open question: chronica as ordinal sequence vs metric timeline" (four items: sleep/awakening, heterogeneous-tempo coupling, the pointer paragraph). The body (line 17) says these implications "are tracked in the Working Notes below", a canon-to-Working-Note pointer that the I.5 cleanup has to resolve. **joined item:influx-event-time-seam** (C.1: canon takes both sides of event ticks vs between-event flow; the awakening gap is the same seam seen from an agent suspended between events). The heterogeneous-tempo coupling question [31] is **owed → item:cross-tempo-coupling-of-chronicae** (C.4), since no segment prescribes it and `#form-event-driven-dynamics` is named as its home.
- [33] "Two forward candidates surfaced while reading this segment for agentic-forensics applications." — (1) folds into item:tractus-chronica-split-for-logogenic-implementation; (2) the fork-undetectability experiment **joined item:proposals-surfaced-2026-05-29-qualitative-gem-hunt-14e1** (SP-27, which characterizes the same invisibility of continuity breaks under $\phi$) and **item:influx-non-forkability-tier**.

#### `def-control-regret`, `def-satisfaction-gap`

- [34] "**Cross-reference to NeurIPS Paper 2.**" (control regret as Component 1) and [40] the same for the satisfaction gap — **guard** (forward pointer into influx). The influx drain owns the paper (`influx-scout/neurips.md` §3 has no row for Component 1, so this pointer is the only index). Whether canon should absorb Paper 2's (A1) extended-real reading is the influx drain's call.
- [38] "$V_{O_t}^{\min}$ (the satisfaction threshold) is a property of the objective, not of the agent." — **canon** (`def-satisfaction-gap`:35 and the Claim Record's False-of line say exactly this).
- [39] "The supremum in $A_O$ is over $\Pi$, the available policy class." — **canon** (:45, "Expand $\Pi$ (structural adaptation of $\Sigma_t$)").

#### `def-mood`, `der-mood-timescale`

- [35] "**Regression guard — do not re-land timescale-matching.**" — **guard**.
- [36] "**Pre-goal volatility link (unverified).** … Behrens-style" — **owed → item:mood-volatility-learning-rate-citation** (F.2): no ledger item carries it, and no body cites Behrens (relata not consulted).
- [37] "**Part II enrichment.** A companion actuation-side segment…" — The body already defers this companion to Part II (:38), but no item owns it: **joined item:todo-mood-layer-prospective-mood-arc-released-9d91**, as an added source (its five follow-ons do not name the companion segment).
- [138] "**Verification record.** Independent refute-posture re-derivation (2026-06-17)…" — **guard** (provenance pointer to `spikes/.integrated/spike-mood-timescale-matching-2026-06-17.md`; kept as the regression trail for the $\sqrt\cdot$ law).
- [139] "**Open — exact AR(1).**", [140] "**Open — mood-sets-gain composition.**", [141] "**Open — asymmetric loss.**" — **joined item:todo-mood-layer-prospective-mood-arc-released-9d91** ([140] is its (ii), [141] its (iv); [139] was not in it and is added as a source; [140] names `audits/AUDIT-WORKING-731548/verify/06-mood-integration-verdict.md` as the sketch needing one re-derivation, and [141] `msc/mood-layer-sovereignty-carve-2026-06-17.md`).

#### `def-strategy-dimension`

- [59] "The independence of $O_t$ and $\Sigma_t$ richness has a practical consequence…" — **canon** (:15, :53 state the independence; the design corollary is a one-line restatement). Set aside.
- [60] "**Cognitive cost of $\Sigma_t$** … No formal analog of $\beta$ (compression cost) exists yet for strategy" — **owed → item:strategy-compression-price-beta-sigma** (C.4). The owner-review map (§3) calls this "strongly cross-substrate convergent"; the gold follow-ups of this segment and `form-strategy-complexity-cost` carry the same question.
- [61] "**Commitment state** (from intent-dag-consolidated DP-3)" and [62] "**Resource budget**" — **joined item:proposals-d-4-sp-12-commitment-resource-temporal-d-1dea** (which cites :97 directly).

#### `def-value-object`

- [69] "**Regression guard — the $M_t$-stratum.**" — **guard** for its two "do not restore" sentences. Its last sentence ("Open: the horizon-$N_h$ form of the identification under $\pi_{\text{cont}}$ … is not written out") is open theory: **joined review:part-ii-check-1-identification#F4** (the checker's finding on the premise structure of the $M_t$-form, which the next Part II integration takes up). The N_h-step g-formula is the same open object.
- [70] "**Migration note (2026-05-09 GUC rename):**" — **set aside**: history; CLAUDE.md's table carries the rename and git carries the date. (Same disposition for every one of the identical migration notes below; they are not repeated individually.)
- [71] "The one-step improvement convention is now the canonical default (promoted from Working Notes…)" — **set aside**: history of a landing (body :23).
- [72] "When a specific convergence guarantee is needed … the solution concept must be stated explicitly" — **canon** (the Continuation-convention paragraph, :61 on).
- [73] "For LLM agents with context turnover, $N_h$ has a natural bound: the current session." — **owed → item:llm-session-bounds-continuation-horizon** (G.2, Volume 3: `#obs-context-turnover` does not say it). Discussion-grade.

#### `der-causal-hierarchy-requirement`

- [92] "This scope narrowing connects to #norm-explicit-strategy-condition…" — **canon** in substance (the learning-agent narrowing, :16, :34; the exploration-vs-planning tradeoff is `#norm-explicit-strategy-condition`'s body). Set aside.
- [93] "LLMs trained on causally-structured text absorb causal priors…" — a Volume 3 remark (priors accelerate, the loop verifies). No 03 body carries it (grep `causal prior` in `03-llm-core/src`: none). Discussion-grade with no claim beyond `#der-loop-interventional-access`'s Level-2 point: **set aside**, reason: it restates that segment for one population and asserts an IB prediction ("causal structure will be retained in training") with no derivation behind it.
- [94] "The scope narrowing to "learning agents" is generous…" — **canon** (:39, :55, :86 say it).

#### `der-directed-separation`

- [117] "**Causal-discipline reframe — directed-separation foundation pass (2026-05-31).**" — its "do not re-scope `#der-orient-cascade` / `#der-action-selection`" sentence is a **guard**. Its "Remaining tail" is **joined item:todo-directed-separation-foundation-pass-rema-4810** (B.2), and the status-signal defect in it is already **review:items-recheck-t2#F1**.
- [118] "**Regression guard — the conditional independence is not the criterion.**" — **guard**.
- [119] "Directed separation connects to the orient cascade…" — **canon** (`#der-orient-cascade` :95 states the dependency ordering as exact). Set aside.
- [120] "**Sub-typology of Class 2 (Partial Coupling).**" — **canon** (`#disc-partial-coupling-pathways` is the segment; this is a summary of it). Set aside.
- [121] "**Engineering design for Class 3 (Coupled) agents.** … Hafez et al. (2026) … 89.3% of coupling degradations against 44.0%" — the IDT row is in the body's Related Work (:256). The figure attribution is **joined item:hafez-citations-der-agent-opacity-109-169-say-h** (F.3) and **review:b1-part-ii-check-1#C7** (which checked the abstract's 89.3%). The engineering-design paragraph is Volume 3 material: **set aside** for 01; checked: no Volume 3 body carries the IDT sidecar pattern; it appears only in `#scope-logogenic-agent`'s Working Notes (:78). It is a published external instance of system-level modularization for internally Coupled agents, so it is **owed → item:idt-sidecar-as-volume-3-modularization-instance** (G.2, Volume 3).
- [122] "**Implication for logogenic agents**: … start from the coupled formulation" — **canon** (:124 says it; `03-llm-core/src/def-coupled-update-dynamics.md` does it).
- [123] Migration note — **set aside** (history).
- [124] "**Provenance (composite-level inheritance, 2026-05-21):**" — **guard** (the withdrawn "Class 1 → Class 2 composite" claim, with its Cournot witness). The current inheritance row has its own open defect, item:the-composite-class-inheritance-row-class-1-sub (C.3), which this guard should be read beside.
- [125] "**Cross-reference to NeurIPS Paper 3.**" — **guard** (forward pointer); influx drain owns it (`influx-scout/neurips.md` §3 "Architecture coverage (A6)": pointer only).
- [126] "**Track E surface-back of catalog citations (2026-05-22).**" — **joined item:primary-source-verify-or-replace-with-read-sourc** (F.3; the body carries three `[^cat-2026-05-22]` marks).
- [127] "**Two senses of component competence — class-orthogonal vs $\kappa$-defining (open, 2026-05-28).**" — **canon** at discussion grade in `#der-class-coercion-via-wrapping` §Discussion; of its open lines, the decomposed estimator is **joined item:spikes-proposed-decomposed-empirical-estimator-accuracy-e63e** (E.1). The rest stays a forward pointer: **guard**.

#### `der-orient-cascade`

- [148] "The cascade as stated is sequential. In practice, agents may run steps in partial overlap…" — **canon** in substance (:95, the ordering is a logical dependency). The logical-not-temporal sentence is not said as such; it is a one-sentence clarification for the C.1 cascade item, so **joined item:todo-der-orient-cascade-a10-f83-f84-step-4a-d-5348**.
- [149] "The resource allocation question (how much of the agent's tempo budget to spend on each step) is open" — **joined question:cascade-objective-last-stopping-rule** (the open allocation and stopping questions of the cascade are one question about how much each step is owed).
- [150] "The virtuous/vicious cycle between $M_t$ quality and $\Sigma_t$ evaluable complexity is structurally motivated but not formally derived." — the body states the cycle (:147) without saying it is underived. **defect → item:orient-cascade-virtuous-cycle-underived** (B.1/C.4: either derive the coupled $(M_t,\Sigma_t)$ dynamics or tag the paragraph as hypothesis).
- [151] "**Strategy-maintenance status (updated).**" — **set aside**: a status summary of other segments, dated; the body's Epistemic Status carries the exact/recommendation split (:95), and the B.1 check C16 found the body itself still contradicts it.

#### `deriv-graph-structure`

- [232] "**P3→Markov: resolved.**" — **set aside**: history of a resolved gap, now the body's derivation.
- [233] "**Parsimony theorem for AND/OR.**" — **owed → item:and-or-parsimony-uniqueness** (C.4). Distinct from item:proposals-c-1-o-bp13-cox-parallel-necessity-for-de-f4cf (necessity of DAG semantics); this one is the uniqueness of the AND/OR basis under parsimony. The `#scope-and-or` off-ramp (gold-lift drain) is the same question's other half (k-of-n).
- [234] "**Non-binary outcome analogs.**" — carried in item:and-or-parsimony-uniqueness.
- [235] "**Environmental common causes and the CMC.**" — **canon** (this segment's "Exactness of Status Propagation", which the note itself cites, and `#def-strategy-dag`:82 on marginal-status multiplication being exact only under independent parents; checked).
- [236] "**Promotion potential.**" — **set aside** (status narration).

#### `deriv-observation-ambiguity-bias-bound`

- [253] "**Regression guard.** Do not restore the information term…" — **guard**.
- [254] "**$\rho_{\text{LSI}}$ for AAT-native cases.**" and [255] "**Large-information regime.**" — open computations. **owed → item:bias-bound-lsi-constant-and-large-information-regime** (C.4), citing `influx-scout/neurips.md` §4.3 ("$C=\sqrt2$ is universal" without the small-information qualifier) as the body-side defect of the same regime question, and Paper 3's spherical-arc constant as unread influx.
- [256] "**Class 2 (Partial) bias-bound analog.**" — whether a tighter bound exists for Class 2 with a known per-stage decomposition. Added as part (c) of item:bias-bound-lsi-constant-and-large-information-regime.
- [257] Migration note — **set aside** (history).
- [258] "**Cross-reference to NeurIPS Paper 3.**" — **guard** (forward pointer). It also records that the paper's architectural corollary uses the $\kappa$ ratio canon retired and excludes the goal-as-evidence Bayesian; that is a note for the paper, owned by the influx drain (`influx-scout/neurips.md` §2.D, "two incompatible definitions of $\kappa_{\text{processing}}$").

#### `deriv-strategic-composition`

The live correctness findings on this segment sit in its gold Off-ramp (gold-lift drain) and are already **item:strategic-composition-alpha-prime-transfer-overclaim** (C.1). The non-gold notes:

- [304] Migration note — **set aside** (history; the withdrawn class claim it narrates is guarded at [308]).
- [305] "**No $\gamma'$ sub-scope.**" — **guard** (a considered-and-collapsed alternative, with the reason).
- [306] "**Effects-spiral eigenvalue condition formalization.**" — **joined item:spikes-proposed-advanced-12-effects-spiral-eigenvalue-condition-d-d6f7** and **question:effects-spiral-spectral-iff-vs-state-dependent**.
- [307] "**Mechanism-design impossibility landed as `#disc-implementation-impossibility`…**" — **set aside** (history of a closed routing; the sister meta-segment exists).
- [308] "**Composite-class-inheritance refinement (resolved 2026-05-21 — withdrawn).**" — **guard** (the withdrawn claim and its Cournot witness), read with item:the-composite-class-inheritance-row-class-1-sub.
- [309] "**Bridge from strategic composition to `#form-composition-closure` $\varepsilon^\ast$.**" — **owed → item:closure-defect-for-equilibrium-statistic-macro** (C.4).
- [310] "**Replicator / evolutionary dynamics.**" — **joined item:spikes-proposed-advanced-14-aat-replicator-evolutionary-game-dyna-689c**.
- [311] "**Mean-field extension.**" — **joined item:spikes-proposed-advanced-7-mean-field-game-limit-for-population-d-61f3**.
- [312] "**Worked-example structure — Cournot substitution for sector-template instantiation.**" — **guard** (records the discarded regularization and its algebra error, the reason the Cournot duopoly carries the instantiation).
- [313]–[315] "**Track E surface-back of catalog citations (2026-05-22) — uncoupled-dynamics + passivity…**", the "Primary-source verification queued in the BG2 cluster" line and the `[^cat-2026-05-22]` footnote — **joined item:primary-source-verify-or-replace-with-read-sourc**.

#### `disc-continuity-stance`

- [386] "*Provenance.* The five-stance taxonomy and the orthogonality claim were authored as a coherent contribution by Joseph…" — **set aside** (provenance; commit `92a9620` and `doc/readme/src/_lexicon-full-archive.md` hold it).
- [387] "*Reconsideration resolved.*" — **set aside** (history; the closing pointer is into an archived tarball).
- [388] "*LEXICON section under review.*" — **joined item:terminology-todo-breakage-a-the-persistence-subgroup-mixe-2fb5**; already flagged as a stale status signal by review:items-recheck-s1#F2.
- [389] "*Open: rigorous boundary cases.*" — **owed → item:continuity-stance-boundary-cases** (C.4).
- [390] "*Orthogonality grain resolved (2026-05-30).*" — **set aside** (history; the L1/L2/L3 distinction is in the body). Its last sentence (the dashed-feedback figure is now *required*) is a figure owed to the body: folded into item:continuity-stance-boundary-cases as its figure clause.
- [391] "*Open follow-on (not attempted here).* The L3 coupling is established qualitatively … but not quantified." — **owed → item:continuity-stance-l3-margin-coupling-bound** (C.4); related to item:adaptive-reserve-standpoint-underived (the same $\Delta\rho^\ast$ read).

#### `disc-dynamic-regime-axis`

- [396] "**Sub-tier unification candidate.**", [398] "**`#disc-modularity-state-dynamics` parallel-pattern.**" and [402] "**Mechanism reduction question.**" — one open question about whether the regime axis and the M4 axis unify. **owed → item:regime-axis-and-m4-unification** (C.4).
- [397] "**§C.3 cost-asymmetry derivation (was J9) + standalone-paper trajectory (was J7)…**" — **joined item:spikes-proposed-c-3-cost-asymmetry-derivation-structural-cdd1**. The paper trajectory lives in `~/src/ops/papers/deferred/dynamic-regime-axis.md`: set aside here.
- [399] "**A4 second-pass Undermind on broadened Instance 3 (resolved 2026-05-21).**" — **set aside** (history: the two caveats it records are in the bodies it names); its citations are in item:primary-source-verify-or-replace-with-read-sourc.
- [400] "**Primary-source verification spike queued (2026-05-21).**" and [401] the `[^bg2-2026-05-21]` footnote — **joined item:primary-source-verify-or-replace-with-read-sourc**.
- [403] "**R3 machinery.**" — **joined item:spikes-proposed-advanced-7-mean-field-game-limit-for-population-d-61f3**.

#### `form-complete-agent-state`

- [502] "The between-event dynamics $\dot{G} = g_G(G, M)$ allow autonomous purposeful evolution…" — **set aside**: a remark (between-event $G$ dynamics may be negligible for session-bound LLMs) with no claim; the between-event seam is item:influx-event-time-seam.
- [503] "The formulation doesn't constrain the dimensionality or structure of $\mathcal{G}$." — **canon** in its load-bearing part: the type-stable interface $V_{O_t}$ is `#form-objective-functional`'s. The thermostat-to-commander range is the note's illustration; the body's True-of line (:60) names Kalman + LQR and Part I's trackers, not a thermostat (checked). Nothing owed.
- [504] "$G_t = \emptyset$ is not just a degenerate case." — **canon** (:70, "Backward compatibility with Part I — what survives the lift").

#### `form-sector-condition`

- [539] "Landing-context provenance: this segment was carved out of #deriv-sector-condition…" — **set aside** (provenance).
- [540] "The companion-property partition (A1, A2', A3 together) is held here as the canonical setup…" — **guard** (says where the sub-scope ladder lives and that it inherits by reference).

#### `hyp-directed-separation-under-composition`

- [554] Migration note — **set aside**.
- [555] "**Goal-information leakage is a separate phenomenon.**" — the body's gold "Readers ask" (line 108) answers a reader question by pointing at this Working Note, so the answer a reader needs is not in the body. **owed → item:goal-information-leakage-is-not-a-separation-failure** (C.4): put the distinction in the body, and decide whether $I(o_c; G^c_t \mid \Omega_t)$ gets its own home (`#der-agent-opacity` is the nearest existing one).
- [556] "**Partial goal-dependence.**" and [557] "**Testable prediction.**" — **owed → item:composite-routing-independence-fraction** (C.4; the prediction is the test).
- [558] "**Composite-class-inheritance table (canonical home: `#der-directed-separation`…)**" — **guard** (says where the table lives), read with **item:the-composite-class-inheritance-row-class-1-sub** (C.3).

#### `impl-persistence-and-limits` (Part I lane live; its branch has not touched these lines)

- [622] "**Scope of this segment.**" — the segment's statement of its own epistemic standing, which A.3 wants as an Epistemic Status: **joined item:format-todo-c14-discussion-segment-schema-split-in-f-09d7** (A.3).
- [623] "**Regression guard — do not restore the refuted forms.**" — **guard** (four refuted forms and the one-hop-downstream lesson).
- [624] "**Open — the matrix information-rate floor.**" — **joined item:todo-aat-1-tensor-adaptive-tempo-downstream-p-bbfe** (it lists the matrix information-rate floor extension); the Mitter–Newton/Riccati route is the added content.
- [625] "**Open — failure-boundary geometry for the weakest-link claim.**" — **joined item:weakest-link-needs-conjunctive-failure-boundary** (C.1).
- [626] "**Open — the two-layer mood corollary.**" — **joined item:todo-mood-layer-prospective-mood-arc-released-9d91** (its (ii)).
- [627] "**Forward — the three-condition picture.**" — **owed → item:transient-adequacy-third-persistence-condition** (C.4); sources include `#result-persistence-condition`'s gold note at its line 199 (gold-lift drain).
- [628] "**Forward — two capacities under one word.**" — **joined item:form-sector-condition-50-still-states-the-radius**.
- [629] "**Forward — the operator decision tree.**" — **joined item:todo-floor-routing-diagnostic-segment-final-f-a963**.
- [630] "**Forward — IB vs structural reserve.**" — **owed → item:ib-target-horizon-vs-structural-reserve** (C.4); the same tension is the gold note at `#result-structural-adaptation-necessity`:107 (gold-lift drain), and the 193847 disposition that routed it to PROPOSALS never arrived.
- [631] "**Candidate experiment (2026-08-12, agent-proposed).**" — **owed → item:context-budget-tempo-ceiling-experiment** (E.2).

#### `persistence-and-limits-intro` (Volume 4 lane live on this segment)

- [691]–[694] "This is a chapter-introduction segment…", "Three moves the intro tries to surface…", "The scope-coda paragraph…", "The closing … line is meant to register the chapter's role…" — **set aside**: authorial intent notes for an intro; the first is the segment's epistemic standing and is covered by item:format-todo-c14-discussion-segment-schema-split-in-f-09d7 (A.3).

#### `result-per-dimension-persistence`

- [714] "The diagonal-correction assumption: closed." — **canon** (the counterexample is `#deriv-matrix-persistence-condition` §4, :99–107). Set aside.
- [715] "The tensor formulation of tempo … Open: tightening this result's Formal Expression to invoke the tensor form directly" — **joined item:todo-aat-1-tensor-adaptive-tempo-downstream-p-bbfe**.
- [716] "Simulation code: `../../empirica/track-b-nonlinear/variants/variant_ef_extensions.py`." — **guard** (the path exists; reproducibility pointer).

#### `scope-adaptive-system` (A.1 lane live; these notes were written by it today)

- [735] "Reasoning trail: `spikes/epistemic-target-ontology/` …" — **guard** (pointer list).
- [736] "**What pins the physical housing.**" — **owed → item:adaptive-scope-what-pins-the-physical-housing** (A.1).
- [737] "**Making law learning declaration-robust (the strengthening to spike).**" — **owed → item:adaptive-scope-declaration-robust-law-learning-tail-rule** (A.1), which carries the note's tail-vs-invariant $\sigma$-field guard; the continuous-space case is question:does-adaptive-scope-membership-depend-on-pi-0-on. INTENT's A.1 row had said this one was already in vsect; it was not (the lead has corrected INTENT).
- [738] "**Compute-relative extension.**" — **owed → item:adaptive-scope-compute-relative-extension** (A.1), citing the 193847 gem adjudication B2 it succeeds.
- [739] "**Four-term refinement of the mismatch decomposition**" — **owed → item:four-term-mismatch-decomposition-refinement** (C.4), carrying the block's note that its checker should not have read spike §6.
- These four were first marked in flight; the A.1 round-5 integrator has finished, so the lead asked for them to be filed. The block's opening pointer [735] and [737]'s $\sigma$-field guard stay as **guards**.
- [740] "**The glyph $\theta$.**" — **joined item:influx-part-i-symbol-and-term-collisions** (F.4; it already names $\theta$).

#### `scope-agency`, `scope-agent-identity` (Volume 4 lane live on the second)

- [741] "**The nominal-agent class now has dynamics (2026-06-11).**" — **guard** (forward pointer to `#der-severed-actuation-dynamics`, which the body does not cite).
- [742] "**Consequence-3 re-grounding 2026-05-30…**" — **set aside** (history; the refuted form is guarded at [623], form (a)).
- [743] "**Cross-references to NeurIPS 2026 submissions.**" — **guard** (forward pointer; influx drain owns Papers 1–3).

#### Chapter intros (`the-cycle-in-motion-intro`, `the-reality-model-intro`)

- [765]–[770] — six authorial notes ("This is a chapter-introduction segment…", "The "two derivations from completeness" framing…", "The CIY-placement paragraph used to be apologetic…", "The "ceiling that's low…" framing is the centerpiece…", "The depends list is light by design…") — **set aside**: design intent for the intros, and one history note; the intros' standing is covered by item:format-todo-c14-discussion-segment-schema-split-in-f-09d7 (A.3).

### Part p3 — Part II Meta-Architecture I

#### `der-architecture-noidentifiability`

- [83] "**Finite-sample Fano refinement is honestly open.**", [84] "**General non-Gaussian sub-scope at exact tier.**", [85] "**The mechanism reduction's relationship to operator-sector machinery.**" — **owed → item:arch-noidentifiability-open-strengthenings** (C.4), with [85] pointed at item:floor-genericity-upgrade-instances-3-4 (same similarity orbit).

#### `der-interaction-channel-classification`

- [128] Migration note — **set aside** (history).
- [129] "**$\mathcal I_{\max}(\mathcal M_B)$ — replace with sufficient-statistics-span.**", [131] "**Heavy-tailed derivation rigorization.**" (the body's Case 4 at :114 is the informal argument), and [134] "**Next spike candidates.**" part (1), the emitter-side $f(H_b^B)$ — **owed → item:interaction-channel-classification-refinements** (C.4). Part (3) of [134] records a resolved item (the arg-max is derived in `#der-agent-opacity`): set aside.
- [130] "**Four regimes vs finer splits.**" — **joined item:interaction-channel-four-regimes-forced-vs-precedence** (raised; it supports the "formulation choice" reading).
- [132] "**Regime II-b as candidate #disc-identifiability-floor Instance 3.**" and [134] part (2) — **joined item:todo-adjacent-identifiability-floors-disc-ide-90c4** (its misspecification-cost extension; raised).
- [133] "**Connection to active inference.**" — **set aside**: a positioning remark (the classification uses $\mathcal I(e)$, not variational free energy) with no claim. The body never mentions active inference; nothing is owed unless F.2's positioning work wants the sentence.

#### `deriv-reward-channel-learning-no-go`

- [279] "**Provenance.** Authored 2026-05-22 via Track CR Phase 4b…" — **set aside** (provenance; Joseph's slug decision is in git and the spike).
- [280] "**Open before `candidate`.**" — (a) and (e) **owed → item:impossibility-clusters-owed-reading** (F.2); (b)–(d) **owed → item:value-functional-grounding-cluster-open-extensions** (C.4).
- [281] "**Cluster's peer meta-segment home landed (2026-05-22…)**" — **set aside** (history; `#disc-value-functional-grounding-floor` exists).
- [282] "**Skalse 2022 as cross-cluster bridge candidate.**" — **joined item:spikes-proposed-advanced-17-skalse-2022-reward-hacking-unhackabil-8188** (raised).

#### `deriv-self-actuation-grounding`

- [290] "Provenance: derived in the 2026-05-17 self-actuation grounding work trail…" — **set aside** (provenance; the review's three findings are now the body's tier and scope).
- [291] "Open before `candidate`: (a) the targeted prior-art search…" — (a) **owed → item:impossibility-clusters-owed-reading** (F.2); (b), (c) **owed → item:value-functional-grounding-cluster-open-extensions** (C.4).
- [292] "Landed status: wired into `01-aat-core/OUTLINE.md`…", [293] "**Cohen 2022 sister-segment landing…**", [294] "**Value-functional-grounding-floor meta-segment landing…**" — **set aside** (history).
- [295] "**Orthogonality grain corrected in Corollary 2(iii) (2026-05-30).**" — **set aside** (history; the L1/L2/L3 statement is in the body); its last sentence **joined item:continuity-stance-l3-margin-coupling-bound** (raised).
- [296] "**Open decision — whether to spin out a standalone `self-actuated-agent` class segment…**" — **defect → item:self-actuated-agent-dangling-slug** (C.1): `#disc-continuity-stance`:54 cites a slug that does not exist (checked; `#def-agent-spectrum` no longer uses it). The note's for-and-against reasoning stays as the decision's record until the item is resolved: **guard** meanwhile.

#### `disc-additive-coordinate-forcing`

- [352] "**Composition layer admits anchor-style additivity, not theorem-style.**" — **owed → item:additive-coordinate-forcing-is-single-agent** (G.2). Checked: the body's "Other AAT segments exhibit additive decompositions" paragraph (:70 on) does not state the composition-layer search or the single-agent conclusion.

#### `disc-anti-collapse`

- [363] "Named and catalogued 2026-05-29 (PROPOSALS SP-26)…" — **guard**, for its one forward pointer: the full graded instance list and the exclusion boundary are at `audits/.gem-hunt-trail/SP-26-disambiguation-sweep/sweep.md`. The provenance narration around it is history.
- [364] "Pedagogical placement…", [365] "Back-references added 2026-05-29 (Joseph-approved)…" — **set aside** (design intent already enacted by the OUTLINE placement; history of the back-references).

#### `disc-constructive-impossibility-posture`

- [380] "**Provenance.**" — **set aside** (provenance).
- [381] "**Why the posture is not a fifth cross-sectional meta-pattern.**" — **canon** (:55, "not a fifth cross-sectional meta-pattern"; checked).
- [382] "**Over-claim guards.**" — **guard**.
- [383] "**Naming alternates considered.**" — **set aside** (a naming record; names now go through `bin/term`).
- [384] "**Dependency rationale.**" — **guard** (why the `depends:` list is what it is).
- [385] "**Removed at `candidate` stage per FORMAT.md Gate 4.**" — **set aside**: an orphaned fragment with nothing to remove.

#### `disc-identifiability-floor`

- [412] "**Candidate instance at the top of the causal hierarchy (2026-07-16).**" — **joined item:disc-identifiability-floor-s-catalog-boundary-re** (raised).
- [413] "**Provenance of the methodology.**" — **canon** in its load-bearing part (:155, "*Whether the methodology is generative* … is a *hypothesis*"; checked). The convergent-not-generative history is set aside.
- [414] "**Sylvester-recognition provenance.**" — **set aside** (history).
- [415] "**Instance 3 broadened 2026-05-21.**" — **set aside** (history). Its phrase "the unique broadly-available R1-vs-R2 classifier" is stale: per `#disc-dynamic-regime-axis`'s notes ([399]) it was softened to "primary AAT-framework".
- [416] Migration note — **set aside**.
- [417] "**Naming convention.**" — **set aside** (naming record).
- [418] "**Instance 3 as a candidate.**" — **joined item:todo-adjacent-identifiability-floors-disc-ide-90c4** (raised, with the note that its "Instance 3" label predates today's numbering).
- [419] "**Is the floor pattern unique to causal/identifiability questions?**" — **joined item:posture-floors-vs-reachability-caps** (raised).
- [420] "**Cross-segment integrations.**" — **set aside**: a list of where the pattern surfaces, which the body's instance catalog carries.
- [421] "**Primary-source verification spike queued (2026-05-21).**" — the discharged target (i) record and its arXiv-vs-SODA pagination caution are a **guard**; the remaining targets **joined item:primary-source-verify-or-replace-with-read-sourc** (raised with the ordered list).
- [422] the `[^bg2-2026-05-21]` footnote — **joined item:primary-source-verify-or-replace-with-read-sourc**.

#### `disc-implementation-impossibility`

- [423] "**Provenance.**" — **set aside**.
- [424] "**Open before `candidate`.**" — (a) **owed → item:impossibility-clusters-owed-reading** (F.2); (b) **joined item:spikes-proposed-advanced-16-roberts-1979-affine-maximizers-as-can-0922**; (c) **joined item:spikes-proposed-advanced-17-skalse-2022-reward-hacking-unhackabil-8188** (both raised).
- [425] "**Depends list will grow as supporting segments land.**" — **superseded**: `depends:` now lists all three supporting segments (checked in the frontmatter).
- [426] "**Sister meta-segments are cross-references, not depends.**" — **guard**.
- [427] "**The three-cluster taxonomy is the substantive coupling with the Cohen-2022 strengthening cycle.**" — **set aside** (history).

#### `disc-modularity-state-dynamics`

- [437] "**Provenance.**", [441] "**Cross-segment ripple from the M4 landing.**", [444] "**Cross-probe convergence provenance.**" — **set aside** (history).
- [438] "**Open before `candidate`.**" (a)–(c) and [443] "**M4 amplification specificity per competence axis (open, 2026-05-28).**" — **owed → item:m4-open-before-candidate** (C.4). vsect warned that item:spikes-proposed-decomposed-empirical-estimator-accuracy-e63e looked close; it is the estimator one part of the new item would use, not the same work.
- [439] "**Worked-example slot.**" and [440] "**Two sub-spike candidates flagged from the Soviet sketch**" — **joined item:decide-where-the-soviet-worked-example-lives-and** (raised).
- [442] "**The convergence-finding observation as methodological pattern.**" — **set aside**: a methodology reflection whose home is `msc/reflections/27-…` (the `msc/` drain's).

#### `disc-separability-pattern`

- [455] "**Standalone-paper candidacy.**" — **joined question:which-key-result-carries-the-separability-ladder** (raised); its novelty record goes into item:separability-pattern-related-work-citations.
- [456] "**Citations to land on promotion to draft / when paper drafting begins:**" — **owed → item:separability-pattern-related-work-citations** (F.2). Checked: the body cites none of them.
- [457] "**Pending family rename and rung-rename decision.**" — **joined item:msc-decision-briefs-2026-07-15-name-the-three-separability-ladder-rungs-c2c2** (raised; its `msc/naming/` pointer is into the archived tarball).
- [458] "**Cross-ladder monotonicity.**" — **joined question:separability-general-open-infectious** (raised).
- [459] "**Extension candidates beyond the eight.**", [460] "**Necessity argument for the pattern itself.**" — **owed → item:separability-ladder-extensions-and-necessity** (C.4).
- [461] "**Does C-BP2 belong in AAT core or in the wider framework narrative?**" — **set aside**: placement is to follow TST adopting the pattern, and nothing proposes that adoption. The segment can move when it happens.
- [462] Migration note — **set aside**.

#### `disc-stability-certificate`

- [463] "**Provenance.**", [464] "**Interior-facet Helmholtz $S/A$ refinement (2026-05-22).**" — **set aside** (history; the refinement is in `#result-certificate-existence`; [464]'s `spikes/spike-enrichment-cluster1-2026-05-21/` path is stale: the directory moved to `spikes/.integrated/`).
- [465] "**Dependency rationale (for Gate-1 audit).**" — **guard**.
- [466] "**Provisional slug.**" — **set aside** (naming record).
- [467] "**Findings Brief sharpening queued (2026-05-28…)**" — **superseded**: the Brief (:92) now states option (i), the measure chosen so that every correction provably shrinks it faster than the world pushes it (checked).
- [468] "**Provisional OUTLINE position.**" — **superseded**: the spine leads its own chapter, Part II "Meta-Architecture I" (`01-aat-core/OUTLINE.md`:104–118).
- [469] "**Propagation plan…**" — **superseded**: steps 1–5 are landed (each named segment's body cites `#disc-stability-certificate`; checked by grep), and step 7's preamble reframe is OUTLINE:108 ("The certificate and its facets"). Step 6 (O-BP10's home) was not checked; it is a proposal-file pointer, and PROPOSALS is gone.
- [470] "**Open edges (from `99-verdict.md`).**" — **joined question:stability-certificate-obstructions-exhaustive** (raised with the linearized-anchor and function-space-Sylvester edges).

#### `disc-value-functional-grounding-floor`

- [481] "**Provenance.**", [486] "**Search provenance.**" — **set aside**.
- [482] "**Open before `candidate`.**" — (a) **joined item:spikes-proposed-advanced-18-cross-agent-value-functional-narrowne-bf71**; (b) **owed → item:value-functional-grounding-cluster-open-extensions**; (c) **joined item:spikes-proposed-two-routes-exhausts-adversarial-spike-on-3366** (raised).
- [483] "**The Skalse-2022 disposition.**" — **guard** (why it is not a member of this cluster).
- [484] "**Why the two charter instances suffice for landing.**" — **guard**: the body states the two instances and the two-routes geometry (:14, :85), but this argument for why two suffice is not in it, and it is the defense a reviewer will ask for. Per the note; the body's :77 completeness sentence is what item:spikes-proposed-two-routes-exhausts-adversarial-spike-on-3366 tests.
- [485] "**Two-routes-exhausts adversarial spike queued…**" — **joined item:spikes-proposed-two-routes-exhausts-adversarial-spike-on-3366**.

#### `form-composition-closure`

- [505] "**Resolved: $\mathcal P_{\text{adm}}$ now has a proposed definition.**", [506] "**Resolved (2026-04-22): temporal coarse-graining gap.**", [510] "**Resolved (2026-05-19): $N$-agent scaling…**" — **set aside** (history; the body carries (P1)–(P3), $K_c$, and the re-typed $N$-scaling row at :185).
- [507] "**Resolved: norm choices for estimation-type agents.**" — **canon** (Mahalanobis in the body; checked).
- [508] "**Open: computing (P1)…**", [509] "**Open: the right value of $\epsilon_I$.**", [516] "The weakest-link structure ($\alpha_c = \min_i \alpha_i^{\text{eff}}$) is conservative." — **owed → item:composition-closure-open-computations** (C.4).
- [511] "**Partial: Mori-Zwanzig connection.**" — **canon** for the zero-lag bound and the refuted full-kernel form (the body's table, :189–190; checked). Its "hard obstruction" (stationarity fails exactly where $\varepsilon^\ast\gt0$) is carried in item:composition-closure-mz-upper-bound-unverified.
- [512] "**(P1) as IB Lagrangian-dual — resolved.**" — **canon** (`#disc-compression-operations`; checked by grep).
- [513] "**Two independent drivers of $\varepsilon_x$.**" — **superseded** for its "gap in `#def-unity-dimensions`" sentence ($U_f$ answers it; the map verified this). Its closed form **joined item:the-heterogeneous-gain-closure-defect-does-not-v** (raised; it is the $K_c$-independent term that item says the spike dropped).
- [514] "**Resolved (2026-05-19): strategy-DAG projection under $\Lambda_x$.**" — **set aside** (history; the derivation is in `#def-strategy-dag`, :273–281). Its sub-open Q1 goes to item:composition-closure-open-computations, marked per the note.
- [515] "~~The bridge lemma's contraction assumption…~~ **CHARACTERIZED 2026-04-06**" — **canon** (the incremental bound is in the body, :254; checked).
- [517] "**A richer toy case** is needed…" — **joined item:todo-composition-admissibility-mathcal-m-text-10c4** (raised).
- [518] "The approach is an approximate dynamical homomorphism condition…" — **canon** (Related Work, :340).
- [519] "**Categorical-cybernetics fit-check candidate (added 2026-05-22).**" — **joined item:spikes-proposed-advanced-15-categorical-cybernetics-re-grounding-9642** (raised; its source-trail path is stale, the directory having moved to `spikes/.integrated/`. The raise first said the path was gone, and is annotated with the correction).
- [520] "**Mori-Zwanzig memory-kernel relationship — upper-bound direction closes; named lower bound does not.**" — **owed → item:composition-closure-mz-upper-bound-unverified** (C.4: verify, then land or delete).
- [521] "**Dynamic-regime placement (added 2026-05-21…)**" — **defect → item:part-iii-segments-name-their-regime-tier** (C.3). Checked: the body never names the regime. (The p6 helper and this part filed it at the same moment; item:composition-closure-regime-scope-unstated is closed as its duplicate.)
- [522], [523] "**Track E surface-back of catalog citations (2026-05-22).**" and its footnote — **joined item:primary-source-verify-or-replace-with-read-sourc** (raised).

#### `form-objective-functional`

- [531] "Compound objectives … might be modeled as terminal AND-nodes…" and [532] "The trajectory functional is real-valued…" — **canon**: the body grounds the scalar codomain as a representation result, with named failures and the Pareto case (:16, :50–62; checked).
- [533] "*History (not for the body):*…" — **set aside** (history).
- [534] "$O_t$ can change over time — objectives evolve. The *rate* of objective revision…" — **canon** in part: :58 states timescale separation for resolving conflicting objectives. The general ordering $\nu_O \ll \nu_\Sigma \ll \nu_M$, labelled "an empirical observation, not a derived result", is not in the body. It is a one-clause remark, so **set aside**; it needs no item.

#### `scope-edge-update-causal-validity`

- [753] "The interaction between $M_t$ updates and edge updates…" — **owed → item:edge-update-evidence-double-counting** (C.4). As first filed the item said no analysis existed; the p5 helper found one (`spikes/.integrated/spike-edge-semantics-resolution.md` §7, "mostly unfounded" with a bounded residual), and the item now asks for that verdict to reach the body.
- [754]–[756] "Can $\iota_{ij}$ be estimated online?", "**Regime C edges should be labeled.**", "The depth-dependent degradation for indirect edges…" — **owed → item:edge-update-causal-validity-open-questions** (C.4).

### Part p5 — Part II Causal Access, Strategy Structure, Strategy Dynamics, Orient Cascade (helper fork)

*KR I.9 (top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."). Written by a fork of the WN-01 drain, for merging into `wn-01-other.md`. All 130 items read whole, at asf `f0f81911`. Every "canon" below was checked against the body by grep and, where the grep hit, by reading the paragraph; where it was not, the line says "per the note; not re-checked".*

**Counts (130 items, 25 segments), by the disposition that decides each item's fate under I.5:** canon 18 · superseded 2 · owed → new item 29 · joined an existing item 30 · guard 24 · set aside 27. Some items carry a second disposition for one sentence (a guard plus an open clause); those are said in the line. Raises recorded with `vsect raise`: 22.

**New items (19):** confounded-positive-feedback-worked-failure (G.2), optimal-strategy-dag-topology, strategic-tempo-and-depth-on-mixed-and-or, terminal-alignment-diagnostic-delta-align, causal-insufficiency-no-go-non-shallow-construction, credit-assignment-open-formalizations, deliberation-strict-dominance-conditions, law-discovery-and-structural-imagination-relata-passes (F.2), structural-imagination-retype-under-invariance-cut (A.1), strategy-compression-by-convergence, stochastic-strategic-disturbance, where-new-strategy-edges-come-from, edge-signal-function-continuous-multiparent, consolidation-as-logogenic-primitive (G.2), mehra-instance-5-candidacy, strategy-restriction-on-sub-sphere, explicit-strategy-cost-inequality-readings, gain-modulated-noise-strategic-feasibility, canon-bodies-point-into-working-notes (I.5). Unmarked owners are C.4.

**For the parent, two things from outside p5.** (1) `item:edge-update-evidence-double-counting` (opened from p3's `#scope-edge-update-causal-validity`) says nobody has worked the double-counting question out; `#hyp-edge-update-via-gain`'s Working Notes record an analysis (`spikes/.integrated/spike-edge-semantics-resolution.md` §7, "mostly unfounded", with a bounded residual effect). Raised onto that item. (2) `item:canon-bodies-point-into-working-notes` (I.5) collects body sentences that point into their own Working Notes; p4's `#def-chronica`:17 is in it, and the p1–p3, p6, p7 passes may find more.

#### `causal-access-intro`

- [0] "This is a chapter-introduction segment; it bridges Chapter 1's lift…" — standing statement: **joined item:format-todo-c14-discussion-segment-schema-split-in-f-09d7** (A.3; raised).
- [1] "The "loop as Level-2 engine" framing is the chapter's central architectural move…" — **set aside**: authorial intent for the intro.
- [2] "The "tragedy of agency in a confounded world" framing comes from Gemini's first-encounter reaction…" — the worked failure mode (confounded positive feedback; the 2025-09-16 substrate-switching retrospective) is in no body (`#der-loop-interventional-access`: no hit for gambl/confound-win/confounded reinforcement). **owed → item:confounded-positive-feedback-worked-failure** (G.2).
- [3] "The pre-compiled / learning-agent distinction is small in segment terms but architecturally large…" — **set aside**: authorial intent; the cut is `#der-causal-hierarchy-requirement`:34.
- [4] "The CIY/EIG honesty is one of those moves that's easy to gloss over…" — **set aside**: authorial intent.

#### `def-strategic-calibration`

- [43] "The aggregation into a single $\delta_{\text{strategic}}$ may lose important structure." — **canon**: the body defines per-edge residuals $r_{ij}$ and opens by saying the quantity locates *where* miscalibration lives (:13).
- [44] "Alternative aggregation: maximum edge residual…" — **set aside**: a per-use-case design choice with no claim; the per-edge residual already serves location.
- [45] "Execution fidelity monitoring is a genuine challenge…" — **canon** for the condition (:36 names execution fidelity as a precondition); the domain remark is set aside.

#### `def-strategic-tempo`

- [46] "**2026-07-16 — OR/AND calibration-vs-performance divergence gloss added to Discussion**" — **set aside**: history.
- [47] "**2026-07-16 — noise-correlation scope made explicit…**" — **set aside**: history.
- [48] "**Mixed AND/OR DAGs.**" — the body itself says it is conditional for this reason (:100). **owed → item:strategic-tempo-and-depth-on-mixed-and-or**.
- [49] "**Optimal topology.** Given a fixed action budget $\nu$…" — the qualitative answer (shallow, OR-heavy) is in the body (:20) without derivation. **owed → item:optimal-strategy-dag-topology**, which also carries `#form-strategy-complexity-cost`'s version [542].
- [50] "**Dynamic complexity.** As $n_{ij}$ grows… Strategic tempo declines over time…" — **superseded** in substance by `#schema-strategy-persistence`'s forgetting prerequisite (:62, the count held at $n_{\text{eff}}$): with forgetting the gain stays at its stationary value; without it the decline is the gain-decay failure that segment derives. The note predates that framing.
- [51] "**Cross-reference to NeurIPS Paper 2.** The strategic-tempo aggregator is **bottleneck-not-sum**…" — **canon** for the content (:20 "bottleneck-limited by the weakest edge"; :92 $\alpha_\Sigma \le \mathcal T_\Sigma/\lvert E\rvert \le \mathcal T_\Sigma$); the paper pointer is a **guard** (influx drain owns Paper 2).

#### `def-strategy-dag`

- [52] "The Correlation Hierarchy (L0/L1/L2) is now first-class… what heuristics help agents identify which common causes are worth modeling at L1?" — **set aside**: the note itself calls it domain engineering, not a theoretical gap.
- [53] "The graph-sufficiency argument … is proved, not sketched." — **canon** (`#deriv-graph-structure`); its last clause (necessity of the graphical structure open) **joined item:proposals-c-1-o-bp13-cox-parallel-necessity-for-de-f4cf** (raised).
- [54] "Health metrics (groundedness, observability coverage…) are scaffold…" — **guard**: no body carries them (grep: none in `#def-strategy-dag`), and the note keeps them out of the formal chain.
- [55] "**Satisfaction criterion.** $V_{O_t}^{\min}$ is now introduced in #form-objective-functional…" — **canon** (`#form-objective-functional`:14).
- [56] "**Terminal alignment error.**" — no body names it (grep `align`: none). **owed → item:terminal-alignment-diagnostic-delta-align**.
- [57] "**Open (composition defect-constant tightness).**" — **joined item:spikes-proposed-scc-defect-constant-tightness-a1-q1-0815** (raised).
- [58] "**Open (mixture-support dynamics).**" — **joined item:spikes-proposed-mixture-support-dynamics-under-the-orien-ca66** (raised).

#### `der-causal-insufficiency-detection`

- [95] "The general-topology construction is a structural argument…" and [96] "The boundary characterization's routes (c) and (e) depend on domain capability…" — the body's Claim Record says the same (:179, :187) and :156 says routes (c)–(e) only cross-reference. **owed → item:causal-insufficiency-no-go-non-shallow-construction** (both parts; also cites the segment's gold note at :288).
- [97] "The no-go is asymmetric: it forbids on-policy *detection* of L1 from L0, but it does *not* forbid on-policy *parameter learning within L0*." — not in the body (grep: no hit). A reader-clarity gap: **joined item:readers-ask-der-causal-insufficiency-detection** (raised).
- [98] "The CHT (Bareinboim et al. 2022) is invoked as an external theorem." — **canon** (Related Work :258 names the CHT as the imported theorem); the "conditions satisfied by construction" sentence is per the note, not re-checked.

#### `der-chain-confidence-decay`

- [99] "The independent-edge assumption … is optimistic for positively correlated failures… Correlation structure is unmodeled" — **superseded**: the body now says $p^n$ is the special case and gives both dependence directions (:26).
- [100] "The additive log-confidence form is the robust result; $p^n$ is the special case…" — **canon** (:12, :26).

#### `der-loop-interventional-access`

- [135] "This result establishes that all agents within AAT's **agency scope** … have access to interventional data" — **canon** (:35 the availability claim; :67 "a tool-using LLM agent is the body's standing instance").
- [136] "The connection to #def-causal-information-yield: CIY quantifies *how much*…" — **set aside**: the distinction is the body's own ("availability of the channel", :55); the CIY cross-reference adds no claim. Per the note; the body's CIY sentence not compared.
- [137] "**Cross-reference to NeurIPS Paper 2.**" with its "**Regression guard:** a goal-conditioned policy does *not* violate sequential ignorability at its own inputs…" — **guard** (the regression guard and the (C2★) scope remark); the paper pointer is influx. This Working Note is now the corrected form of what review:b1-part-ii-check-1#F2 flagged (the old "violate (C2) by construction" sentence); whoever closes F2 can cite it.

#### `der-observability-dominance`

- [146] "The absorbing-state property of unobservable regions is a strong prediction. In organizational settings…" — the body's Claim Record cites this Working Note as its register evidence (:60, "Working Notes: poorly measured departments…"), so deleting the note breaks a body sentence. **owed → item:canon-bodies-point-into-working-notes** (I.5); the content itself is canon by that citation.
- [147] "Observability is not binary — it's a spectrum." — **canon** in substance: `#hyp-edge-update-via-gain`:19 reads observability dominance as the limiting case as destination observability goes to zero. The diagnostic question it ends on is the persistence condition itself.

#### `deriv-mechanism-counterfactual-separation`

- [247] "**Provenance.** Landed 2026-07-16 from `spikes/spike-causal-level-4-strictness-2026-07-16.md`…" — **set aside**: provenance; the path is now `spikes/.integrated/…` (the live path is dead).
- [248] "**Naming caution.**" — **guard**.
- [249] "**Priority-search record.**" — **guard** (records where the clean-miss search and its primary-confirmed readings are, and the one correction that mattered: Bongers prove interventional, not counterfactual, preservation). The standalone-note decision it mentions is in Joseph's ops queue, outside asf.

#### `disc-credit-assignment-boundary`

- [392] "A formal reduction from AND/OR credit assignment to Shapley value computation…", [393] "The proportional-blame heuristic … satisfies directional fidelity for independent edges. Does it satisfy directional fidelity in general?", [394] "The connection between AAT's credit assignment and RL's temporal credit assignment…" — the body asserts the #P-hardness via a Shapley form (:99) and states directional fidelity in expectation as the requirement (:22); neither the reduction nor the sufficiency check is derived, and no TD/eligibility positioning exists. **owed → item:credit-assignment-open-formalizations** (three parts).
- [395] "The log-odds presentation of the default signal function (this segment) closes the Finding 2 mechanical break…" — **guard** (forward pointer: if the strategy layer moves to log-odds, Props B.1–B.7 follow).

#### `disc-exploit-explore-deliberate`

- [404] Migration note — **set aside** (history).
- [405] "**Open: conditions for deliberation dominance.**" — the body gives the dominance conditions qualitatively (:98); strict-dominance conditions are not derived. **owed → item:deliberation-strict-dominance-conditions**.
- [406] "**Open: the additive decomposition.**" — **canon**: the body says the additive form is a linearization that ignores the interaction term (:72).
- [407] "**The $\Delta V_\Sigma$ approximation misses two channels of deliberation value.**" — **canon** (:78–83 name both channels); the third channel the body omits is item:regret-ceiling-omits-policy-class-expansion.
- [408] "**Landing context.**" — **set aside**: history.
- [409] "Reproducibility: the simulation-check outcomes … were produced by … `spikes/sim-three-way-tradeoff.py`" — **joined item:disc-exploit-explore-deliberate-s-epistemic-stat** (F.3), which already names this pointer and re-ran the script; not raised again. The file exists.
- [410] "**Open: the unified vs two-stage question.**" — **canon**: the body calls the two-stage decomposition "a modeling convenience, not a structural necessity" and writes the unified objective (:64–68).
- [411] "**Relationship to working memory.**" — **joined item:context-window-strategy-depth-bound** (raised: the window must hold deliberation as well as $M_t$ and $\Sigma_t$).

#### `disc-law-discovery-ceiling`

- [432] "**Provenance.** Developed dialogically with Joseph 2026-07-16…" — **set aside**: provenance.
- [433] "**Forward pointer (live).**" — **guard** (`03-llm-core/src/hyp-behavioral-self-knowledge-insufficiency.md` exists).
- [434] "**Floor-catalog candidacy.**" — **joined item:disc-identifiability-floor-s-catalog-boundary-re** (raised; that item already names the ceiling as a deferred candidate).
- [435] "**Relata pass owed before promotion:**" and [436] "**Standalone-paper feed.** … the Undermind novelty search (running 2026-07-16)…" — no Related Work row for these in the body; no recorded search result in `ref/`. **owed → item:law-discovery-and-structural-imagination-relata-passes** (F.2).

#### `disc-structural-imagination`

- [477] "**Provenance.**" — **set aside**.
- [478] "**Typed target adopted (2026-10-30); re-typing owed here.**" — **owed → item:structural-imagination-retype-under-invariance-cut** (A.1).
- [479] "**Relata pass owed** before promotion: Beckers & Halpern…" — **owed → item:law-discovery-and-structural-imagination-relata-passes** (F.2).
- [480] "**$\delta_{\text{structural}}$** (fifth mismatch type) deliberately withheld" — **guard**.

#### `form-consolidation-dynamics`

- [524] "**Stability upper bound derivation (open).**" — **joined item:todo-stability-upper-bound-for-form-consolida-be13** (raised).
- [525] "**Online-only no-go rigorization (open).**" and [528] "**Quantitative CLS instantiation.**" — **joined item:spikes-proposed-quantitative-cls-instantiation-of-consol-6c13** (raised).
- [526] "**EWC formulation as stability-weighted gain.**" — **canon** (the body names EWC/Kirkpatrick, :24 region).
- [527] "**Relationship to #form-strategy-complexity-cost compression-by-convergence.**" — **owed → item:strategy-compression-by-convergence**.
- [529] "**Logogenic primitive status.**" — no 03 body declares it (`#impl-scaffolded-logogenic` composes consolidation but does not); **owed → item:consolidation-as-logogenic-primitive** (G.2).
- [530] "**Is consolidation one segment or two?**" — **joined item:todo-stability-upper-bound-for-form-consolida-be13** (raised: split once the bound lands).

#### `form-strategy-complexity-cost`

- [541] "**Mixed topologies.**" — **owed → item:strategic-tempo-and-depth-on-mixed-and-or**.
- [542] "**Optimal topology.**" — **owed → item:optimal-strategy-dag-topology**.
- [543] "**Dynamic complexity.** As edges converge… The IB objective would favor *dropping* converged edges" — **owed → item:strategy-compression-by-convergence**.
- [544] "**Stochastic $\mathcal T_\Sigma$.**" — **owed → item:stochastic-strategic-disturbance**.

#### `form-structural-change-as-parametric-limit`

- [545] "The timescale ordering (reweight ≫ reclassify ≫ prune/graft ≫ revise $O_t$ ≫ full restructure) is an empirical observation that should be testable." — **set aside**: no body claims the ordering (the operations table :25–32 lists triggers, not rates); the objective-vs-strategy part is `#form-objective-functional`'s timescale-separation point (:58), whose own Working Note is in p3.
- [546] "Grafting (adding new edges) is qualitatively different…" — **owed → item:where-new-strategy-edges-come-from**.

#### `hyp-edge-update-via-gain`

- [559] "The signal function is characterized at the theory level … but remains domain-specific in implementation." and [560] "**Partial progress on the signal function**" — **owed → item:edge-signal-function-continuous-multiparent** (the body lists it open, :59; the partial result is in `#deriv-edge-credence-dynamics` Props B.2–B.3).
- [561] "The Beta-Bernoulli model assumes edge outcomes are i.i.d. Bernoulli draws." — **canon**: time-varying reliability is handled by discounting in `#schema-strategy-persistence`; correlated outcomes by the L1 hierarchy of `#def-strategy-dag`. Context-dependent reliability is not separately treated; per the note, not pursued.
- [562] "**$M_t$/edge evidence double-counting** analyzed in `spikes/.integrated/spike-edge-semantics-resolution.md` §7." — **guard** for the verdict, and **joined item:edge-update-evidence-double-counting** (raised: that item says no analysis exists; this one does, and the body still lists the interaction open).
- [563] "**Dependency removed 2026-05-11.**" — **set aside**: history. Its closing suspicion (the reverse edge `deriv-edge-update-natural-parameter` → `hyp-edge-update-via-gain` may also be mention-not-use) still applies: that depends entry is present at HEAD; per the note, not re-judged.

#### `impl-causal-access`

- [588] "**Scope.**" — **joined item:format-todo-c14-discussion-segment-schema-split-in-f-09d7** (A.3; raised).
- [589] "**Regression guard — singularity.**", [590] "**Regression guard — modes.**", [591] "**Regression guard — deliberation.**", [592] "**Regression guard — identification conditions vs wrapping's (C1)–(C3).**", [593] "**Regression guard — escape language.**", [594] "**Regression guard — tiers inherited from a discussion surface.**" — **guard** (six).
- [595] "**Forward — NeurIPS back-integration (out-of-canon pointer…)**" — **guard**.
- [596] "**Forward — Hafez IDT anchor.**" — **joined item:hafez-citations-der-agent-opacity-109-169-say-h** (raised).
- [597] "**Forward — source defects this pass surfaced, not fixed here (routed to TODO):**" — every defect it lists has an item now: **joined item:disc-sandbox-evaluation-ceiling-four-defects-fro**, **item:causal-access-chapter-register-defects-reported** (`#def-pearl-causal-hierarchy`:41, `#scope-ciy-observational-proxy`'s $\Omega_t$, `#causal-access-intro`:29), **item:norm-explicit-strategy-condition-44-says-explici** (F35). All three raised.
- [598] "**Forward — figures.**" — **joined item:pedagogy-home-for-lifted-audit-gold** (raised).
- [599] "**Forward — Regime B as the LLM software agent's typical regime**" — **joined item:ciy-proxy-omega-and-llm-agent-regime** (raised; its part (b) is this).
- [600] "**Teaching frames (lifted audit gold, attributed; chapter-end register).**" — **joined item:pedagogy-home-for-lifted-audit-gold** (raised, with Joseph's two quotes carried verbatim). This is 2026-08-22 lifted gold outside an "Incidental audit gold" heading, like `#impl-persistence-and-limits`' block; it is disposed here so it is not orphaned, and the gold-lift drain may want to know.
- [601] "**Forward — audit watches kept as guards**" — **guard**.
- [602] "**Belongs elsewhere.**" — **guard** (each pointer names a canon home).

#### `impl-orient-cascade`

- [613] "**Regression guard — scaffolding claim.**" and [614] "**Regression guard — bias-bound scaling.**" — **guard** (two). [613] is the same correction item:the-scaffolding-overclaim-in-volume-3-its-origin carries for Volume 3.
- [615] "**Open strengthening — per-direction bandwidth floor.**" — **joined item:todo-aat-1-tensor-adaptive-tempo-downstream-p-bbfe** (raised).
- [616] "**Causal-discipline re-scope (2026-05-31).**" — history, except its last sentence (the propagated-residual bound across the cascade is open), which item:apply-the-epsilon-programme-s-telescoping-with-c already cites by this line: **joined**, not raised again.
- [617] "This segment is a chapter-end discussion grouping findings from…" — **joined item:format-todo-c14-…** (raised).
- [618] "**Cross-reference vs canonical-home policy.**" — **set aside**: describes the body's layout.
- [619] "**`#13` (Coupled Diagnostic Framework) — segment exists in `03-llm-core/`.**" — **set aside**: `#result-coupled-diagnostic-framework` still has no `## Findings` section (checked); that is catalog formatting with no truth content, and the finding is carried in this segment's body.
- [620] "**Connection to NeurIPS submissions.**" — **guard** (pointer; influx).
- [621] "**Identifiability-floor pattern coverage update.**" — **set aside**: dated status narration ("five-sixths complete"); its one live content, the Mehra Instance 5 candidacy, has no owner: **owed → item:mehra-instance-5-candidacy**.

#### `impl-strategy-dynamics`

- [659] "This segment is a chapter-end discussion grouping findings from…" — **joined item:format-todo-c14-…** (raised).
- [660] "**Cross-reference vs canonical-home policy.**" and [661] "**Cross-segment findings — the heaviest content in this chapter.**" — **set aside**: describe the body's layout (CS1, CS2 live in the body).
- [662] "**Identifiability-floor pattern coverage so far.**" — **set aside** (status narration); Instance 5 is item:mehra-instance-5-candidacy.
- [663] "**Connection to NeurIPS submissions.**" — **guard** (pointer; influx).
- [664] "**Density flag and check-in.**" — **set aside**: process narration.

#### `impl-strategy-structure`

- [665] "This segment is a chapter-end discussion grouping what…" — **joined item:format-todo-c14-…** (raised).
- [666] "**Regression guards.**" — **guard** (five).
- [667] "**Open — the two-gap identity's grain.**" — **joined item:def-strategy-dag-and-form-strategy-complexity-co** (raised; its rg-0c result on sub-node diagnostics bears directly).
- [668] "**Open — the L1′ mixing weight.**" — **joined question:where-does-the-l1-mixing-weight-theta-c-for-a-so** (raised).
- [669] "**Open — partial (sub-sphere) restriction.**" — **owed → item:strategy-restriction-on-sub-sphere**.
- [670] "**Open — a `convergent-choice` register?**" — **joined item:say-at-the-front-of-the-strategy-chapters-what-k** (B.2; raised).
- [671] "**Connection to NeurIPS Paper 2.**" — **guard** (pointer).
- [672] "**Candidate figure — the chapter-end bridge diagram**" — **joined item:pedagogy-home-for-lifted-audit-gold** (raised).

#### `norm-explicit-strategy-condition`

- [681] "The inequality as stated is static…" and [683] "The cost inequality may be most useful not as a binary decision rule but as a way to calibrate $\Sigma_t$ complexity…" — neither reading is in the body (grep: no dynamic/calibration sentence). **owed → item:explicit-strategy-cost-inequality-readings** (discussion grade).
- [682] "Part of $C_{\text{maintain}}$ is the cognitive cost of keeping $\Sigma_t$ in the agent's representational capacity." — **joined item:context-window-strategy-depth-bound** (raised).

#### `schema-strategy-persistence`

- [728] "**Done.** Five cases verified…" — **set aside**: history; its last sentence (deeper mixed topologies, several common causes) went into item:strategic-tempo-and-depth-on-mixed-and-or.
- [729] "**Strategic tempo now formalized.**" — **canon** (`#def-strategic-tempo`:92).
- [730] "The strategic disturbance $\rho_\Sigma$ is qualitatively different from epistemic disturbance $\rho$." — **canon** (:143 defines it as the rate the environment invalidates causal links and calls it a domain parameter).
- [731] "The stochastic treatment (from track-b simulations) suggests $\rho_\Sigma / \sqrt{\mathcal T_\Sigma}$…" — **owed → item:stochastic-strategic-disturbance**.
- [732] "The forgetting prerequisite transforms an organizational platitude…" — **canon** (Claim Record :109, :113; institutional cases marked as illustrations).
- [733] "**Gain-modulated observation noise (forward pointer, `conditional` at most).**" — **owed → item:gain-modulated-noise-strategic-feasibility**.
- [734] "**Cross-reference to NeurIPS Paper 2.** The forgetting prerequisite is sharpened … into a structural-class theorem on gain-decay updates" — **guard** (pointer). Whether canon should land the class theorem is the influx drain's (`influx-scout/neurips.md` §3: "cited from bodies, not landed").

#### `scope-and-or`

- [744] "The AND/OR assignment per node ($\gamma(v)$) is itself uncertain and should be updateable." — **canon** (`#form-structural-change-as-parametric-limit`:28, "$\gamma$ reclassification … strong structural evidence").
- [745] "The parsimony argument applies cleanly to binary outcomes." — **joined item:and-or-parsimony-uniqueness** (raised).
- [746] "K-of-n thresholds are genuinely common…" — **joined item:scope-and-or-audit-finding-f41-still-open-in-its** (raised).

#### `strategy-structure-intro`

- [760] "This is a chapter-introduction segment…" — **joined item:format-todo-c14-…** (raised).
- [761]–[764] "The framing "Chapter 2 says whether to plan; Chapter 3 says what a plan IS"…", "The "what is and isn't derived in the formal commitment" framing…", "The "two diagnostic quantities, not one" framing…", "The chain-confidence-decay paragraph names what the identity unlocks downstream." — **set aside**: authorial intent for the intro. The derived-vs-chosen distinction they defend is item:say-at-the-front-of-the-strategy-chapters-what-k's subject.

### Part p6 — Part III Meta-Architecture II, Scope and Formation, Composition Machinery (helper fork)

*KR I.9. Written by a fork of the WN-01 drain, to be merged into `wn-01-other.md`. 85 items in 11 segments, all read whole at `dc2b262c`. Body checks were made by grep on the body (Working Notes excluded) and by reading the matching paragraph where the grep hit; where a disposition rests on the note's own words, it says "per the note; not re-checked". The Part I lane was live on `result-contraction-template` when this ran; its Working Notes lines are untouched on that branch as far as the diff shows.*

**Counts.** 85 items: canon 8 · superseded 2 · owed → new item 31 (into 13 items) · joined an existing item 24 · guard 5 · set aside 15. An item split between dispositions ([471], [606], [164]) is counted under its main one.

**New ledger items (13):** item:wrapping-open-theory-iterated-w2-and-form-selection, item:tempo-composition-dynamic-theta-witness, item:adversarial-coupling-pressure-prior-art-search, item:adversarial-mechanisms-on-partial-coupling-typology, item:adversarial-coupling-brief-feynman, item:defensive-scaffolding-composition-segment, item:strategic-self-coupling-primary-sources-and-cult-boundary, item:symbiogenic-composition-open-formalizations, item:truth-serving-loophole-open-questions, item:decoupling-self-defeat-modes, item:contraction-template-open-strengthenings, item:composite-scope-asymmetric-implicit-transitive, item:part-iii-segments-name-their-regime-tier.

**Raised onto existing items (14, recorded with `vsect raise`):** todo-detailed-tempo-accounting-for-canonical-e0c9, spikes-proposed-decomposed-empirical-estimator-accuracy-e63e, an-empirical-census-of-deployed-agent-frameworks, spikes-proposed-decorrelation-by-construction-class-3-bu-f138, primary-source-verify-or-replace-with-read-sourc, spikes-proposed-advanced-13-game-theoretic-formalization-of-the-m-4436, todo-disc-composition-consistency-does-direct-813e, readers-ask-disc-composition-consistency, spikes-proposed-composition-consistency-meta-segment-str-8fc7, spikes-proposed-spike-strategic-self-coupling-p2-p4-appe-3163, spikes-proposed-advanced-2-the-phase-transition-of-symbiogenesis-59b7, hyp-truth-serving-loophole-s-open-premise-has-a, todo-heredity-axiom-for-disc-composition-cons-3a39, format-todo-c14-discussion-segment-schema-split-in-f-09d7.

**One cross-part note.** item:part-iii-segments-name-their-regime-tier also carries `form-composition-closure`'s "Dynamic-regime placement" note (p3, item [521]): that segment's body never names a regime tier while its note says (A1)–(A4) hold only for R0. Whoever writes p3 can dispose [521] as joined to it.

#### `der-class-coercion-in-composition`

- [101] "**Detailed tempo accounting for canonical wrapper architectures.**" — **joined item:todo-detailed-tempo-accounting-for-canonical-e0c9**.
- [102] "**Connection to ELI-specific structure in `04-eli-core/`.**" — **set aside**: a remark that ELI structure sits on top of the wrapper, with no claim to land.
- [103] "**Segment split provenance (2026-05-11).**" — **set aside** (provenance; git carries the split).

#### `der-class-coercion-via-wrapping`

- [104] "**Empirical $\kappa$ measurement.**" — **joined item:spikes-proposed-decomposed-empirical-estimator-accuracy-e63e** (E.1); its ceiling-versus-realized-leak gap bears on review:part-ii-integration-1#F2 (what $\kappa_{W_1}^{\text{sel}}$ mixes), named in the raise.
- [105] "**Sub-type-aware wrapping regime selection.**" — **owed → item:wrapping-open-theory-iterated-w2-and-form-selection** (c). The wrapping body does not cite `#disc-partial-coupling-pathways` (grep on body: none).
- [106] "**Compositional wrapping (wrapper-of-wrapper).**" — **owed →** the same item, (a).
- [107] "**Behavioral compliance axiom for W₂.**" — **owed →** the same item, (b).
- [108] "**Identifying the regime in the wild.**" — **joined item:an-empirical-census-of-deployed-agent-frameworks** (G.2).
- [109] "**Segment split provenance (2026-05-11).**" — **set aside** (provenance).
- [110] "Reasoning-trail provenance: spike directories at `spikes/class-coercion-wrapping/` and `spikes/temporal-nesting-rg/`…" — **set aside**: a provenance pointer; both directories are the spike drain's (fork B1, and the RG verdict).
- [111] "**W₁ leakage-bound — regression guard.**" — **guard**.
- [112] "**Migration note (2026-05-09 GUC rename):**" — **set aside** (history; it also records that W₀/W₁/W₂ and Class A/B/C were unchanged, which the body already shows).
- [113] "**Track E surface-back of catalog citations (2026-05-22).**" and [116] the `[^cat-2026-05-22]` footnote — **joined item:primary-source-verify-or-replace-with-read-sourc** (F.3). The body's Related Work row (:203) carries Gat, Simmons and Au.
- [114] "**Spike candidate (2026-05-28): Decomposed empirical estimator…**" — **guard**: already a resolved pointer to item:spikes-proposed-decomposed-empirical-estimator-accuracy-e63e; the body's Discussion (:181) carries the substance.
- [115] "**Spike candidate (2026-05-28): Decorrelation-by-construction…**" — **joined item:spikes-proposed-decorrelation-by-construction-class-3-bu-f138** (unassigned; its owner is still open).

#### `der-tempo-composition`

- [162] "**Migration note (2026-05-09 GUC rename):**" — **set aside**.
- [163] "The lower bound $C_{\text{coord}} \geq \varepsilon^\ast \nu_c / \lVert\delta_{\text{critical}}\rVert$ captures the minimum…" — **canon** (body :88: "the inequality is a lower bound because additional coordination costs (ne[gotiation …])"; :111 names negotiation). The four-term additive model is not in the body; it is a sketch with no derivation, so set aside beyond that.
- [164] "**Heterogeneity drives closure defect.**" — **canon** elsewhere: `#result-unity-closure-mapping`'s heterogeneous-gain analysis (13 body hits on heterogeneity / $\Delta K$; paragraph not compared). The note's "$\varepsilon^\ast \propto \lvert\alpha_1-\alpha_2\rvert$" is a simplification of the closed form in `#form-composition-closure`'s Working Notes (p3 [513]); item:the-heterogeneous-gain-closure-defect-does-not-v (G.2) is where that closed form's spike claim is under correction.
- [165] "The internal/external mismatch distinction is formalized through the bridge lemma…" — **canon** (body :19–25: dimensional accounting through the bridge lemma and the template instantiation; per the body read, not term-by-term).
- [166] "**Norm specification note.**" — **canon** (`#form-composition-closure` body names the Mahalanobis norm, 3 hits).
- [167] "**Regression guard — do not restore the unconditional additive $\mathcal T_c \le \sum_i \mathcal T_i$.**" — **guard**.
- [168] "**Dynamic-$\theta$ regime (from the confirmer≠author verification, 2026-07-16).**", [169] "**(A4) uniformity wrinkle (static witness).**", [170] "**(P1) holds with $\epsilon_I = 0$ exactly**" — **owed → item:tempo-composition-dynamic-theta-witness** (C.4). None is in the body (grep `dynamic`, `random-walk`, `epsilon_I`, `uniform`: none).
- [171]–[173] "**Track E surface-back of catalog citations (2026-05-22).**" (Janow 2009, Gurvich and Van Mieghem 2015, Bamieh et al. 2011), the queued-verification line and the footnote — **joined item:primary-source-verify-or-replace-with-read-sourc**. Checked: these three exist only in Working Notes (body grep: none; the segment has no Related Work section in its body), which the raise records.

#### `disc-adversarial-coupling-pressure`

- [353] "**Promotion: requires targeted prior-art search.**" — **owed → item:adversarial-coupling-pressure-prior-art-search** (F.2).
- [354] "**Stage × source × form structure within the adversarial mechanisms.**" — **owed → item:adversarial-mechanisms-on-partial-coupling-typology** (C.4); the body has no stage mapping (grep `P3`/`stage`: frontmatter only).
- [355] "**Brief is not yet at Feynman criterion.**" — **owed → item:adversarial-coupling-brief-feynman** (H.1). The body Brief (:111) is as the note describes.
- [356] "**Game-theoretic formalization candidate.**" — **joined item:spikes-proposed-advanced-13-game-theoretic-formalization-of-the-m-4436**.
- [357] "**Defensive scaffolding deserves its own segment under Part III.**" — **owed → item:defensive-scaffolding-composition-segment** (G.2).
- [358] "**OUTLINE.md placement.**" — **superseded**: the segment is in `01-aat-core/OUTLINE.md` (6 hits), under Meta-Architecture II.
- [359] "**Sister segment for strategic self-coupling.**" — **superseded** by `#disc-strategic-self-coupling` (landed 2026-05-24).
- [360] "**Meta-segment landed 2026-05-24.**" — **set aside** (history).
- [361] "**Surfacing bounded-signaling in `#der-directed-separation`.**" — **canon** (`#der-directed-separation` :28 and :237, "Bounded-signaling assumption"; checked).
- [362] "**Migration note (2026-05-09 GUC rename + 2026-05-21 composite-claim withdrawal):**" — **set aside** (history; the withdrawn composite claim is guarded at `#der-directed-separation` and `#deriv-strategic-composition`, p4 [124], [308]).

#### `disc-composition-consistency`

- [369] "**Strengthening attempt — outcome.**" — **canon** (body :46–50, the Tier 1M closed forms (CC-parallel)/(CC-cascade)/(CC-feedback)); the residual Tier 2/3 screening is stated there too, per the body read.
- [370] "The timescale separation condition is essentially the singular perturbation argument from #der-temporal-nesting…" — not in the body (grep `singular perturb`, `temporal-nesting`: none). **joined item:spikes-proposed-composition-consistency-meta-segment-str-8fc7** (the strengthening of this meta-segment).
- [371] "Composition of directed separation: if each sub-agent's $f_M$ is $G_t$-independent…" — **joined item:todo-disc-composition-consistency-does-direct-813e** (B.2).
- [372] "The "atomic agent" question…" — **joined item:readers-ask-disc-composition-consistency** (its (1) asks exactly this).
- [373] "The relationship to holons (Koestler 1967)…" — not in the body; **joined item:spikes-proposed-composition-consistency-meta-segment-str-8fc7**, which already names Koestler in its prior-art list.
- [374] "**Provenance — retype from postulate to discussion-grade meta-recognition (2026-05-28).**" — **set aside** (provenance; it is also the record of Joseph's 2026-05-28 reframe, which `feedback_meta_segments_deserve_pedagogical_work.md` in project memory carries).

#### `disc-strategic-self-coupling`

- [471] "**Open before `candidate`.**" — (a) **owed → item:strategic-self-coupling-primary-sources-and-cult-boundary** (F.2); (b)–(d) **joined item:spikes-proposed-spike-strategic-self-coupling-p2-p4-appe-3163** (the spike drain names that item "the whole remainder").
- [472] "**Possible appendix companions**" — **joined** the same p2-p4 item.
- [473] "**Forward — the belief-update-layer instance (2026-08-22).**" — **guard** (forward pointer); its instruction for the inflection derivation is carried in the raise on the p2-p4 item.
- [474] "**Indexed at spike-proposals.**" — **joined** the p2-p4 item (the inflection derivation).
- [475] "**Boundary with cult-formation literature.**" — **owed →** item:strategic-self-coupling-primary-sources-and-cult-boundary. The body's boundary paragraph (:101) is there; Lifton and Singer are not cited.
- [476] Migration note — **set aside**.

#### `hyp-symbiogenic-composition`

- [570] "**Objective-transfer dynamics (S-1).**", [571] "**Function transfer $\mathcal{F}$ (S-2).**", [572] "**Autonomy reduction (S-3).**", [573] "**(S-3) as weighted-Lyapunov limit (sketch-level).**", [574] "**Reverse symbiogenesis.**", [575] "**Interaction with logogenic agents.**", [576] "**Quantitative predictions.**", [577] "**Timescale of consolidation.**" — **owed → item:symbiogenic-composition-open-formalizations** (C.4). The body states (S-1)–(S-3) as hypothesis parts (:23, :31, :39); none of the dynamics, the weighted-Lyapunov sketch (grep `weighted`: none) or the rest is there.
- [578] "**Saddle-node bifurcation analysis…**" — **joined item:spikes-proposed-advanced-2-the-phase-transition-of-symbiogenesis-59b7**. Its own statement that the threshold is a formulation until $+k\delta^2$ is derived is the guard, carried in that item.
- [579] "**Dynamic-regime placement (added 2026-05-21…)**" — the R1 → R0 reading is not in the body (grep `R0`/`R1`/`regime`: none). **owed →** item:symbiogenic-composition-open-formalizations, last clause.
- [580] "**Track E surface-back… Szathmáry 2015**" and [581] the footnote — **joined item:primary-source-verify-or-replace-with-read-sourc**. Working-Note-only (body grep `Szathm`: none).

#### `hyp-truth-serving-loophole`

- [582] "**Open — the truth-objective premise.**" — **joined item:hyp-truth-serving-loophole-s-open-premise-has-a** (C.4; this note is its source).
- [583] "**Open — sign of $\Delta_G$.**", [584] "**Open — is Mode 4 a fifth floor instance?**", [586] "**Open — declaration vs. detection.**" — **owed → item:truth-serving-loophole-open-questions** (C.4), which also names review:part-ii-check-1#F6.
- [585] "**Hypothesis (Joseph's, 2026-08-22) — decoupled architecture can itself be self-defeating.**" — **owed → item:decoupling-self-defeat-modes** (C.4). The body's local-vs-global reading (:27, :33) touches modes (a) and (b) but does not state the catalogue or attribute it.
- [587] "Placement: this segment sits after #hyp-directed-separation-under-composition…" — **guard** (says where the segment should move once it outgrows hypothesis grade).

#### `impl-composition-machinery`

- [603] "This segment is a chapter-end discussion grouping findings from…" and [604] "**Cross-reference vs canonical-home policy.**" — the segment's statement of its own standing and of which findings live here. **joined item:format-todo-c14-discussion-segment-schema-split-in-f-09d7** (A.3).
- [605] "**Class-coercion as truthification mechanism — connection to `#disc-modularity-state-dynamics`.**" — **canon** in `#disc-modularity-state-dynamics` (depends on and names the wrapping construction; per its body opening, paragraph not compared). This implications segment's own body never says "truthification" (grep: none); its composite-level twin, defensive scaffolding, is item:defensive-scaffolding-composition-segment.
- [606] "**Identifiability-floor pattern coverage now four-of-four.**" — **set aside** as a status summary. Its "Instance 5 (Mehra) remains candidate" matches canon: `#deriv-adaptive-gain-dynamics`:149 lists it as a "candidate floor instance". The test itself is item:mehra-instance-5-candidacy (p5).
- [607] "**No NeurIPS submission directly formalizes this chapter's machinery.**" — **set aside**: a negative pointer with no work in it.

#### `result-contraction-template` (Part I lane live on this segment)

- [708] "**Landing context.**" — **set aside** (provenance).
- [709] "**Heterogeneous general-graph composition.**" and [710] "**Jacobian-level B1 strengthening is open.**" — **owed → item:contraction-template-open-strengthenings** (C.4), (a) and (b). Neither is in the ledger (searched `small-gain`, `N \geq 3`, `Jacobian-level`, `B1*`; the one hit is the (CC-feedback) iff defect, a different thing).
- [711] "**Candidate strong-option promotion.**" — **joined item:todo-heredity-axiom-for-disc-composition-cons-3a39**.
- [712] "**Finsler metrics.**" — **canon** (Related Work row :196 cites Forni and Sepulchre 2014); the "not priority" judgment is set aside.
- [713] "**The (T2) / (CT2) structural observation matters for Part I too.**" — **owed →** item:contraction-template-open-strengthenings, (c). `#result-persistence-condition`'s body does not cite the contraction template (grep: none).

#### `scope-composite-agent`

- [747] Migration note — **set aside**.
- [748] "**Whether a common scalar exists across the alignment routes (resolved 2026-05-21 — negatively).**" — **set aside** as history of a resolved question. The route-to-regime mapping it states is not in the body (grep `R0`/`regime`: none), so its content goes into item:part-iii-segments-name-their-regime-tier.
- [749] "**Asymmetric unity.**", [750] "**Interaction with Class 3 (Coupled) architectures.**", [751] "**Transitivity.**" — **owed → item:composite-scope-asymmetric-implicit-transitive** (C.4).
- [752] "**Promotion dependencies.**" — **owed → item:part-iii-segments-name-their-regime-tier** (C.3).

### Part p7 — Part III Unity, Cooperative/Adversarial, Strategic Composition; Appendix B

#### `cooperative-adversarial-intro`

- [5] "This is a chapter-introduction segment…" — the intro's standing: **joined item:format-todo-c14-discussion-segment-schema-split-in-f-09d7** (A.3; raised).
- [6]–[9] "The "consultant vs employee" analogy…", "The "regime change rather than quantitative disadvantage" framing…", "The "mathematics of panic" framing…", "The "death by a thousand memos" framing…" — **set aside**: authorial notes on where the intro's framings came from and why it uses them; the intro's prose is the result.

#### `def-shared-intent`

- [41] "The IB formulation assumes a single relevance variable…" and [42] "How does shared intent interact with 100% context turnover?" — **owed → item:shared-intent-relevance-and-turnover** (C.4). The body's IB line (:28) has the single relevance variable; turnover is not in the body (checked).

#### `def-unity-dimensions`

- [63] "The independence of unity dimensions needs careful examination.", [64] "The specific metric formulations need testing on concrete cases…", [66] "**$U_f$ operator-distance choice is open.**" — **owed → item:unity-dimensions-open-formalizations** (C.4).
- [65] "The teleological unity scalar per objective dimension ($+1$ to $-1$)…" — the scale is canon (:42); its mixed-motive use **joined question:unity-mixed-motive-u-o-aggregation** (raised).
- [67] "**Joint $(U_O, U_\Sigma) \to \varepsilon_a$ dependence.**" — **canon** (the content axis in the body, :17, and `#result-unity-closure-mapping`'s $\varepsilon_a$ form, :52; checked by grep and the first matching lines).
- [68] "**$U_O$ as scope vs. quality.**" — **canon** for the four-route scope role (item:todo-613842-c-iv-idiom-drift-integration-debt-e3af records that the body now carries four routes). Its open sub-question (do the alignment routes reduce to one scalar?) is **superseded**: resolved negatively at `#scope-composite-agent` (p6 [748]).

#### `der-adversarial-destabilization`

- [74] "The decoupled analysis (treating $\mathcal T_A$ as exogenous) is conservative…" — **guard**: a forward pointer that names the coupled analysis's formal home (`#deriv-strategic-composition`) and the scope boundary against `#result-contraction-template` (saddle points are not attracting fixed points). The body does not carry the boundary (checked); the matching premise in the result segment is item:adversarial-tempo-advantage-unstated-premises.
- [75] "$\gamma_A$ is the product of coupling strength, observability, and action impact…" — **set aside**: a gloss. The software claim points at TST's `#def-system-coupling`, which is TST's to carry.
- [76] "The effects spiral is the formal analog of Boyd's cascading disorientation…" — **joined item:spikes-proposed-advanced-12-effects-spiral-eigenvalue-condition-d-d6f7** (raised).

#### `der-agent-opacity`

The overclaims in this segment's gold Off-ramp are item:der-agent-opacity-overclaims-f246-f255 (the gold-lift drain's territory). The non-gold notes:

- [77] Migration note — **set aside**.
- [78] "The (C-iv) scope route … full composition is open work." — **joined item:spikes-proposed-advanced-12-effects-spiral-eigenvalue-condition-d-d6f7** (raised).
- [79] "Candidate fourth-instance formalization for `#disc-identifiability-floor`: … Fano's inequality…" — **guard** (dead-end warning: two spikes found Fano is a finite-sample refinement, not an M1 floor anchor), and **joined item:collect-exclusion-criteria-meta-families** (raised). The note says the body's "Meta-pattern positioning" section is Fano-on-$H_b$'s home, but the body does not mention Fano (grep); recorded in the raise.
- [80] "The 16-cell emitter-recipient composition admits closed-form arg-max only under sub-scope $\alpha$…" — **canon** (sub-scope $\alpha$ scoping in the body; checked by grep).
- [81] "**2026-07-16 — arg-max formula and backward variance decomposition landed…**" — history, plus the status point that the product form is a Formulation until a second-order analysis lands: **joined item:der-agent-opacity-overclaims-f246-f255** (raised).
- [82] "Dual-filtration apparatus…" — **set aside**: the body indexes opacity by the observer's filtration $\mathcal F_B^t$ (:32); the symmetric "each model carries the other's filtration" form is called clean but unnecessary, and no derivation wants it.

#### `der-team-persistence`

- [156] "**2026-07-16 — noise-correlation scope corrected…**" — **guard** for its "do not restore the upper-bound reading"; the two-sided scope is canon (:37, checked). Its triangulation design consequence goes to item:team-persistence-coordination-cost-and-mixed-coupling (d).
- [157] "Topology: the peer network and the ensemble are treated in the Discussion…" — **guard** (says where hierarchy and game theory are handled).
- [158] "The coordination cost model … needs further specification" and [159] "The disturbance decomposition treats cooperative and adversarial coupling as additive and independent." — **owed → item:team-persistence-coordination-cost-and-mixed-coupling** (C.4); [159] also raised onto question:unity-mixed-motive-u-o-aggregation.
- [160] "**Continuity-persistence cross-reference (updated 2026-05-19).**" — **guard** (forward pointers that now resolve to canon). It still names the deaths "D1 Cognitive / D2 Relational / D3 Truth", which canon retired on 2026-06-10; raised onto item:terminology-todo-the-deaths-taxonomy-def-death-as-factor-e267 so the names are fixed when the note is kept.
- [161] "**Dynamic-regime placement (added 2026-05-21…)**" — **joined item:part-iii-segments-name-their-regime-tier** (raised; the body names no regime).

#### `deriv-critical-mass-composition`

- [197] "**Partial-derivation: heterogeneous-architecture dyad.**", [200] "**Connection to Miller-2022 extreme-transition motif.**", [201] "**$N$-agent scaling.**" — **owed → item:critical-mass-open-cases** (C.4). The body's table marks the dyad and $N\gt2$ Open (:127, :132), but no ledger item carried them; the Miller contrast is not in the body.
- [198] "**Sharpen (UO-mult).**" — **joined item:spikes-proposed-u-o-sector-constant-uo-mult-derivation-fbb6** (raised).
- [199] "**Close (S-2) function transfer in #hyp-symbiogenic-composition.**" — **joined item:symbiogenic-composition-open-formalizations** (raised).
- [202] "**Dynamic-regime placement…**" — **joined item:part-iii-segments-name-their-regime-tier** (raised; checked: the body names no regime).

#### `detail-operationalization` (Part I lane live on this segment)

- [349] "End-to-end worked examples … are in #example-kalman (exact) and #example-bandit (approximate)." — **set aside**: a pointer the OUTLINE already makes.
- [350] "The $\hat{\rho}$ estimator's dependence on $\hat{\mathcal{T}}$ creates a sequential estimation chain." — **joined item:write-innovation-based-estimators-for-detail-ope** (raised).
- [351] "The structural-switch trigger's $T_{\text{horizon}}$ … is itself uncertain…" — **set aside**: a remark (the model does the predicting) with nothing to derive or land.

#### Appendix B examples (`example-bandit`, `example-kalman`, `example-strategy`)

- [491] "The per-arm analysis is a natural instance of the per-dimension tempo decomposition…" — **set aside**: a reading of the example through `#result-per-dimension-persistence`, which the example can state when (f) of the item below is done.
- [492], [494], [495], [497]–[501] — the comparisons and extensions the examples' notes name (Q-learner vs Bayesian bandit; multi-dimensional Kalman; a real tracking system; a deeper DAG; Gittins vs explore-then-exploit; Monte Carlo for the satisfaction-gap table; a strategy-tempo example; an uncertain AND/OR domain) — **owed → item:worked-example-extensions-and-comparisons** (E.2).
- [493] "Reward-unit and surprise-unit formulations coincide up to normalization by $\sigma^2$." — **set aside**: true of this example by its parameters ($\sigma=1$); no claim beyond it.
- [496] "The Kalman filter is provably optimal for the linear-Gaussian case…" — **set aside**: the example's framing already says this; the "real test is non-Kalman domains" point is (f) of the item above.

#### `hyp-auftragstaktik-principle`

The gold Off-ramp's F162/F165 are item:t1-auftragstaktik-allocation-and-conway (C.1).

- [547] "The formal IB derivation of the priority ordering would need…" — the strengthen-first route for that item: **joined item:t1-auftragstaktik-allocation-and-conway** (raised).
- [548] "The principle may need qualification for AI agent teams…" — **joined item:how-much-must-be-said-explicitly-depends-on-the** (raised). The body's evidence is military-organizational (:20, :41); it does not qualify for AI teams.

#### `hyp-communication-gain`

- [549] "The communication gain enters the distributed tempo…" — **canon** (`#der-team-persistence`:19, distributed tempo; checked).
- [550] "Coordination overhead limits team size…" — **owed → item:team-persistence-coordination-cost-and-mixed-coupling** (b); not in either body (checked).
- [551] "The adversary's strategy (making $U_{\text{align}}$ *appear* low) creates a meta-game on trust estimation." — **joined question:in-aat-s-terms-tempo-reserve-mismatch-communicat** (raised).
- [552] "Open, now partially derived: when multiple intermediaries provide corroborating recommendations…" and [553] "Consider eventually **splitting $U_{\text{src},j}$ from $U_{\text{align},ji}$**…" — **owed → item:communication-gain-open-extensions** (C.4); [553] also raised onto item:todo-communication-gain-adversarial-scope-hyp-e79c. The body does not mention corroboration or a common source (grep).

#### `hyp-solicitable-escape`

- [564] "**Forward pointer.** The two promotion steps are named in Epistemic Status…" — **guard**.
- [565] "**Correction, 2026-07-29 … the premise was inherited from prose, not from a derivation.**" — **guard** for its regression-guard sentence; the correction narrative is history. The parent-segment overreach it found is item:observability-dominance-cannot-recognize-unscoped (C.1).
- [566] "**Regression guard — a truncation to not restore.**" — **guard**.
- [567] "**Naming.**" — **set aside**: naming is `bin/term`'s, and [564] already says the slug changes on promotion.
- [568] "**Provenance of the check.**" — **set aside** (provenance).
- [569] "**Provenance of the insight, not only of the check.**" — **guard**: first-person testimony that the targeting asymmetry was recognized from inside the condition. It is the only record of that standpoint, and the note itself counts it as weak evidence for the partition.

#### `impl-cooperative-adversarial`

- [608] "This segment is a chapter-end discussion grouping findings from…" and [609] "**Cross-reference vs canonical-home policy.**" — **joined item:format-todo-c14-discussion-segment-schema-split-in-f-09d7** (raised).
- [610] "**Forward-pointers into Ch.5 are heavy.**" — **set aside**: a reading note.
- [611] "**Identifiability-floor pattern coverage update.**" — **guard** for its distinction: contraction obstructions name where a *method* fails, while floors forbid *identifying* a quantity. The body's "Three adversarial obstructions to contraction" section (:49) does not draw it (checked); item:collect-exclusion-criteria-meta-families is where such exclusions are being collected.
- [612] "**Connection to NeurIPS submissions.**" — **set aside**: a negative pointer.

#### `impl-strategic-composition`

- [651] Migration note — **set aside** (history; the deeper rewrite it narrates is in the body).
- [652], [653] chapter grouping and canonical-home policy — **joined item:format-todo-c14-discussion-segment-schema-split-in-f-09d7** (raised).
- [654] "**`#28` Modular Safety as segment-promotion candidate.**" — **owed → item:modular-safety-under-goal-divergence-segment** (G.2).
- [655] "**Cross-segment finding without home — `#40` OODA + Detection Latency Self-Bound.**" — **canon**: this segment's body carries the composition (:52–54, the $\mathcal T^{\text{eff}}$ OODA reading beside the 16-cell composition); the note says the segment is its home.
- [656] "**Identifiability-floor pattern's full four-instance treatment…**" — **set aside** as a status summary; its "Instance 5 (Mehra) remains candidate" is item:mehra-instance-5-candidacy (filed by the p5 helper).
- [657] "**Connection to NeurIPS submissions.**" — **set aside**.
- [658] "**AAT chapter-end implications series complete.**" — **superseded**: the TST and logogenic chapter-ends it lists as remaining exist (`02-tst-core/src/impl-*`, `03-llm-core/src/impl-*`, four each).

#### `impl-unity-communication`

- [673], [674] chapter grouping and canonical-home policy — **joined item:format-todo-c14-discussion-segment-schema-split-in-f-09d7** (raised).
- [675] "**Cross-segment finding — bandwidth-and-trust as the layer between Ch.2 and Ch.4.**" — **canon** per the note (it says §4 of the body carries it; §4 not re-read).
- [676] "**Status discipline (regression guard).**" — **guard**.
- [677] "**Strengthening targets (for the sources, forward pointers).**" — (i) **joined item:t1-auftragstaktik-allocation-and-conway** (raised); (ii), (iii) **owed → item:communication-gain-open-extensions**.
- [678] "**No identifiability-floor instance lands in this chapter.**", [679] "**Connection to NeurIPS submissions.**" — **set aside**.

#### `obs-gated-tempo-advantage`

The $\nu$-versus-$\mathcal T$ collision and the one-sided noise prescription are items gated-tempo-nu-versus-tempo-collision and t1-gated-tempo-one-sided-noise-prescription (C.1).

- [688] "The finding that fixed $\eta = 0.1$ is "remarkably robust" to observation noise…" and [689] "The interaction between observation noise and adversarial exponent regime … has not been tested." — **owed → item:gated-tempo-noise-under-drift-and-default-gain** (C.4).
- [690] "Simulation code: …" — **guard** (reproducibility pointer; the path exists).

#### `result-adversarial-exponent-regimes`

- [695] "The interpolation between drift and noise regimes (Variant B) shows smooth transition…" — **canon** (:40; checked). The drift fraction as a lever is question:adversary-optimal-drift-fraction.
- [696] "The exponent of 1.05 from the original sim2 was not a falsification of Corollary 11.2…" — **guard** (keeps the old run from being read as a falsification).
- [697] "Simulation code: `empirica:track-b-nonlinear`…" — **guard**.
- [698] "**2026-07-16 — stochastic interpolation column corrected…**" — **guard** for "do not re-transcribe simulation numbers by table position"; the correction history is set aside.

#### `result-adversarial-tempo-advantage`

- [699] "**Channel-independence assumption.**", [701] "The analysis treats each agent's tempo as exogenous…", [702] "The stochastic exponent ($b = 3/2$) is now derived from both…" — **defect → item:adversarial-tempo-advantage-unstated-premises** (C.1): the body calls the exponents exact on the disturbance and coupling models without stating either premise (checked: no "exogenous", "channel" or "correlated" in the body); [702]'s finite-$\nu$ correction is part (c).
- [700] "**Opacity modulation ( #der-agent-opacity).**" — **joined item:der-agent-opacity-overclaims-f246-f255** (raised; the $\mathcal T_{\text{eff}}$ factor is one of its findings).
- [703] "Asymmetric coupling ($\gamma_A \neq \gamma_B$) appears as a multiplicative prefactor…" — **canon**: the general ratio (:36) carries $\gamma_A$ and $\gamma_B$ separately; the note reads it off.

#### `result-unity-closure-mapping`

- [721] "**Two-Kalman IB witness landed (2026-07-16).**" — **canon** (`#disc-compression-operations`:84). Its unrun numeric check **joined item:the-heterogeneous-gain-closure-defect-does-not-v** (raised).
- [722] "**Extension to nonlinear cases.**", [723] "**Structural-unity formalization.**", [724] "**Joint $(U_O, U_\Sigma)$ derivation.**" — **owed → item:unity-dimensions-open-formalizations** (C.4).
- [725] "**$U_O$ → sector-constant pathway…**" — **joined item:spikes-proposed-u-o-sector-constant-uo-mult-derivation-fbb6** (raised).
- [726] "**Mori-Zwanzig cross-check.**" — **joined item:composition-closure-mz-upper-bound-unverified** (raised).
- [727] "**Relationship to #scope-composite-agent.**" — **joined item:part-iii-segments-name-their-regime-tier** (raised; the body never says quality is conditional on a scope route, and the note's "three" routes is stale).

### Part p1 — Appendix A, `der-belief-strategy-attractor` to `deriv-mismatch-budget-attribution` (helper fork)

*KR I.9. Written by a fork of the WN-01 drain, to be merged into `wn-01-other.md`. 79 items in 17 segments, all read whole at `dc2b262c`. Body checks were made by grep on the body (Working Notes excluded), and the matching paragraph was read where the grep hit. Where a disposition rests on the note's own words or on a grep count alone, it says so. The Part I lane was live on `deriv-matrix-persistence-condition` when this ran.*

**Counts.** 79 items: canon 7 · superseded 1 · owed → new item 26 (into 14 items) · joined an existing record 22 · guard 11 · set aside 12. An item split between dispositions ([183], [196], [230]) is counted under its main one.

**New ledger items (14):** item:belief-strategy-attractor-o-vs-sigma-estimator, item:belief-strategy-attractor-brief-feynman, item:multi-timescale-stacking-contraction-metrics, item:resource-bounded-regenerative-regime-and-rates, item:adaptive-gain-open-extensions, item:bilateral-trade-adjacent-escapes, item:convention-monotonicity-rh-citations, item:discrete-sector-nonstationary-and-correlated-noise, item:fisher-local-gain-open-extensions, item:fisher-whitened-open-extensions, item:gain-sector-bridge-in-expectation-scope (C.1), item:matrix-persistence-2d-false-pass-simulation (E.2), item:mismatch-budget-attribution-under-model-s, item:l1-update-bias-n-child-common-cause.

**Raised onto existing records (16, `vsect raise`):** der-belief-strategy-attractor-conditional-run-th, the-composite-class-inheritance-row-class-1-sub, which-aat-structural-adaptation-mechanisms-satis, model-s-stacking-for-der-multi-timescale-stabili, mehra-instance-5-candidacy, spikes-proposed-adversarial-adaptive-gain-meta-gain-temp-06a0, impossibility-clusters-owed-reading, todo-causal-ib-lmi-follow-ons-segment-landed-f746, todo-aat-1-tensor-adaptive-tempo-downstream-p-bbfe, land-the-2026-08-24-decomposition-uniqueness-clu, the-prior-art-search-deriv-decomposition-uniquen, todo-heavy-tailed-disturbances-model-s-assume-f3de, adaptive-reserve-standpoint-underived, influx-sufficiency-fitness-horizon-and-class; question:ea1-beyond-averaging-estimators; and the finding review:part-ii-check-1-b1-records#F1 (see [196]).

**Two things worth the merger's attention.**

- **A guard that now carries a refuted claim.** `deriv-convention-monotonicity`'s "Documented dead-end" Working Note [196] ends by saying the right rung's strengthening "is the (PC)/(SO) characterization". The Part II check (review:part-ii-check-1-b1-records C1, C2) found the rung fails with (PC) and (SO) both true. Its F1 lists the body carriers to drain but not this Working Note, so I raised the Note onto F1. The guard against an unconditional rung stays; its last clause has to change with the body.
- **Dead pointers, both moved to `.integrated/`.** `spikes/fight/` ([152]; `der-resource-bounded-destabilization`'s reasoning trail) is now `spikes/.integrated/fight/`. `spikes/spike-value-object-convention-monotonicity-2026-05-30/` ([194]; the reproducibility scripts) is now `spikes/.integrated/spike-value-object-convention-monotonicity-2026-05-30/`. The second is a reproducibility pointer, so I.5 should repoint it, not delete it.

#### `der-belief-strategy-attractor`

- [86] "**Tier-upgrade gating sub-spike — derivation of $K(\Sigma)$ from utility-cost analysis.**" and [87] "**Tier-upgrade gating sub-spike — Pillar prior-art search.**" — **joined item:der-belief-strategy-attractor-conditional-run-th** (C.4; these notes are its source).
- [88] "**Composite-level extension.**" and [90] "**Connection to `#deriv-strategic-composition`.**" — **joined item:the-composite-class-inheritance-row-class-1-sub** (C.3): the inheritance table should also track composite sub-type, and with it attractor vulnerability.
- [89] "**Empirical estimator — distinguishing $O$-source bias from $\Sigma$-source attractor…**" — **owed → item:belief-strategy-attractor-o-vs-sigma-estimator** (C.4).
- [91] "**Brief is below Feynman criterion.**" — **owed → item:belief-strategy-attractor-brief-feynman** (H.1).

#### `der-multi-timescale-stability`

- [142] "**Open (which AAT mechanisms satisfy the premises).**" — **joined item:which-aat-structural-adaptation-mechanisms-satis** (B.1); item:outside-domains-that-meet-der-multi-timescale-st (C.4) cites the same note.
- [143] "**Open (Model S stacking).**" — **joined item:model-s-stacking-for-der-multi-timescale-stabili** (C.2).
- [144] "**Open (non-Euclidean metrics).**" — **owed → item:multi-timescale-stacking-contraction-metrics** (C.4). The body states the stacking in the Euclidean template only (grep `CT1`, `Fisher`: no per-level metric restatement).
- [145] "**Belongs elsewhere (ELI internal coherence).**" — **canon** at `04-eli-core/src/def-auxilia-hierarchy.md`:76 ("Trust-as-temporal-respect", in the body, above its Working Notes at :96). Per the note, not this segment's claim.

#### `der-resource-bounded-destabilization`

- [152] "Reasoning trail: `spikes/fight/03-energy-bound-effects-spiral.md`…" — **set aside**: provenance, and the path is dead (now `spikes/.integrated/fight/`, cited from the new item).
- [153] "**Open — regenerative regime.**", [154] "**Open — rate constants.**" and [155] "Exploratory-branch status… Promotion past `draft` is gated on Joseph electing to develop the resource axis…" — **owed → item:resource-bounded-regenerative-regime-and-rates** (C.4). The body has the $r_{\mathcal B}$ ODE and the $r_{\mathcal B}=0$ regime (:27, :37) but not the regenerative case. The item records that the Joseph gate is lifted and asks for develop-or-set-aside. It also names the parallel barrier-reachability item, spikes-proposed-continuity-4-2-second-no-go-adversariall-c4e7.

#### `deriv-adaptive-gain-dynamics`

- [174] "**Identifiability as meta-gain obstruction.**" — **joined item:mehra-instance-5-candidacy** (C.4). The body's table row :149 already carries Mehra non-identifiability as a candidate floor instance.
- [175] "**Rate-specific results.**", [177] "**Discrete-time form.**", [178] "**Relationship to #schema-strategy-persistence time-varying $\alpha$.**" and [181] "**Deterministic-meta-gain special cases.**" — **owed → item:adaptive-gain-open-extensions** (C.4). The body never names the Fisher-whitened or Fisher-local segments (grep: none).
- [176] "**Adversarial adaptive-gain.**" — **joined item:spikes-proposed-adversarial-adaptive-gain-meta-gain-temp-06a0**.
- [179] "**Template-composition as general technique.**" (three or more timescales) — **superseded** by `#der-multi-timescale-stability`, whose body is the $N$-level stacking (:13 on).
- [180] "**AMSGrad as $\alpha_2$-preserving meta-gain repair.**" — **canon** (body :81 names the AMSGrad fix with Reddi et al.).

#### `deriv-bilateral-trade-impossibility`

- [182] "**Provenance.**" — **set aside**.
- [183] "**Open before `candidate`.**" — (a) **joined item:impossibility-clusters-owed-reading** (F.2); (b), (c) **owed → item:bilateral-trade-adjacent-escapes** (C.4). The body's escape table (:69–70) has the rows, marked adjacent.
- [184] "**The honest-almost-entirely-outside scope-mark.**" — **set aside**: a rationale for how the three charter instances differ in how far outside AAT they sit. The scope marks themselves are in the body's escape table.

#### `deriv-causal-ib-exploration`

- [185] "**Empirical validation.**" — **guard** (reproducibility pointer). Checked: `empirica/track-b-nonlinear/variants/variant_causal_ib.py` exists, and `variant_causal_ib_results.md`:23 reports the greedy controller at 0.00% survival, as the note says.
- [186] "**LMI generalization landed.**" — **set aside** (history).
- [187] "**Cross-reference to NeurIPS Paper 1.**" — **guard** (forward pointer; the influx drain owns Paper 1, and item:influx-causal-ib-lmi-state-independence-boundary carries what changed).

#### `deriv-causal-ib-lmi`

- [188] "**Tensor adaptive tempo.**" — **joined item:todo-aat-1-tensor-adaptive-tempo-downstream-p-bbfe**.
- [189] "**Worked 2D example.**" and [190] "**2D simulation.**" — **joined item:todo-causal-ib-lmi-follow-ons-segment-landed-f746** (both are among its listed follow-ons).
- [191] "**EIG vs FIM gap.**" — **canon** per grep (11 body hits on EIG / expected information gain; paragraph not compared); the CIY-EIG surrogate is also in item:influx-active-inference-four-strengths.
- [192] "**Reasoning trail.**" — **set aside** (provenance).
- [193] "**Cross-reference to NeurIPS Paper 1.**" — **guard** (forward pointer, influx drain).

#### `deriv-convention-monotonicity`

- [194] "The reproducibility scripts for the counterexample and the two strengthenings live with the originating spike…" — **guard**, with a dead path: the directory is now `spikes/.integrated/spike-value-object-convention-monotonicity-2026-05-30/`. Repoint, don't delete.
- [195] "External citations for (RH-1/2/3) are `intuition-only` until a `relata` pass lands them…" — **owed → item:convention-monotonicity-rh-citations** (F.2).
- [196] "**Documented dead-end (so a future agent does not re-attempt it):**" — **guard** for the unconditional left rung. Its right-rung sentence is now wrong: **raised onto review:part-ii-check-1-b1-records#F1** (see the top of this file).

#### `deriv-decomposition-uniqueness`

- [203] "**Regression guard — do not re-formalize restricted access as a target-value subset…**" and [204] "**Regression guard — quantifier-vs-flagship verification…**" — **guards**.
- [205] "**Open (main line):** the distributional/kernel-level analog…" — **joined item:land-the-2026-08-24-decomposition-uniqueness-clu** (G.2). Per that item, the distributional spike's Theorem D answers the main-line question, so this Note is out of date until the landing.
- [206] "**Open:** exact characterization of the (D3)-respecting gauge subgroup…" and [207] "**Open (follow-on candidate):** quantifying Corollary 5's information gap for GUC Class 3…" — **joined** the same item, with an explicit note in the raise that the cluster may not cover them. Whoever lands the cluster settles whether they remain open.
- [208] "**Prior-art status.**" — **joined item:the-prior-art-search-deriv-decomposition-uniquen** (F.2; the search ran 2026-08-24 and never reached the segment).

#### `deriv-discrete-sector-condition`

- [209] "Non-stationary gain…" and [211] "Non-i.i.d. disturbances…" — **owed → item:discrete-sector-nonstationary-and-correlated-noise** (C.4). The body's DA.1S statement assumes i.i.d. zero-mean $w_k$ (:117), and neither extension is discussed.
- [210] "Heavy-tailed disturbances: DA.1S assumes finite second moment." — **joined item:todo-heavy-tailed-disturbances-model-s-assume-f3de**.

#### `deriv-evidence-allocation-ceiling`

- [212] "**Verification provenance.**" — **set aside**: a verification record from today, which belongs in vsect as a recorded check and in its integration-notes file (named in the Note), not in Working Notes.
- [213] "**Strengthening direction.**" — **joined question:ea1-beyond-averaging-estimators**.

#### `deriv-fisher-local-update-gain`

- [214] "**Multi-step extrapolation rate.**", [215] "**Edgeworth higher-order correction.**", [216] "**Variational-bound extension.**", [217] "**Multimodal posteriors.**" and [218] "**Consolidation / replay connection.**" — **owed → item:fisher-local-gain-open-extensions** (C.4). vsect flagged item:spikes-proposed-quantitative-cls-instantiation-of-consol-6c13 as close. It is not the same work; only clause (e) touches consolidation.
- [219] "**Honest obstructions.**" — **canon** (body :97 imports Amari 1998, :101 makes the tier conditional on (PI), :105 gives the outside-regime fallback; read).
- [220] "**Cross-reference to Paper 3 chart-rescaling no-go.**" — **guard** (forward pointer, influx drain).
- [221] "**Landing context.**" — **set aside**.
- [222] "**Downstream consumer at the persistence layer.**" — **canon** (`#def-adaptive-tempo`'s Tensor extension and `#deriv-matrix-persistence-condition` carry it; the latter's counterexample was checked for p4 [714]).

#### `deriv-fisher-whitened-update-rule`

- [223] "**Sub-scope $\alpha_4$ composition**", [224] "**L2 regime.**" and [225] "**Relationship to natural-gradient variational inference.**" — **owed → item:fisher-whitened-open-extensions** (C.4). Khan and Lin are not cited in the body (grep: none).
- [226] "**Landing context.**" — **set aside**.
- [227] "**Sibling segment at the model-parameter layer.**" — **set aside**: a cross-reference remark (direction here, magnitude in `#deriv-fisher-local-update-gain`), with no claim beyond the two bodies.

#### `deriv-gain-sector`

- [228] "The fluid-limit gap: the bridge analysis works in expected value." — **owed → item:gain-sector-bridge-in-expectation-scope** (C.1; the body never says its bridge is in expectation).
- [229] "For variational inference and other approximate methods, B1 is not guaranteed by optimality…" — **canon**: `#deriv-variational-sector-condition` treats exactly this (per its name and this body's :173 pointer; not compared).
- [230] "The adaptive-reserve factorization for gradient agents is $\Delta\rho^\ast = \eta\mu R - \rho$…" — **joined item:adaptive-reserve-standpoint-underived** (C.1), and folded into item:gain-sector-bridge-in-expectation-scope's last sentence.
- [231] "Full simulation code, raw traces, and intermediate analysis live in `spikes/.integrated/spike-gain-sector-bridge-nonlinear.md`…" — **set aside** (provenance).

#### `deriv-l1-update-bias`

- [237] "**Forward — citable-supplement script.**" — **guard** (says where the re-run script lives and that the original is lost).
- [238] "**Regression guard — do not restore the confabulated MC summary.**" — **guard**.
- [239] "**Open: non-matched-marginal transient bias.**" — **canon** (the body's "What is not established" list, :103, says it).
- [240] "**Open: $N$-edge common-cause extensions.**" — **owed → item:l1-update-bias-n-child-common-cause** (C.4).

#### `deriv-matrix-persistence-condition` (Part I lane live)

- [241] "**Counterexample as load-bearing content.**" — **set aside**: an assessment of the body's §4. Its "generalizations … are mechanical" claim is unverified, and nothing depends on it.
- [242] "**Empirical validation.**" — **owed → item:matrix-persistence-2d-false-pass-simulation** (E.2).
- [243] "**Open work — nonlinear matrix-sector.**", [244] "**Open work — adversarial extension.**" and [245] "**Open work — composition lift.**" — **joined item:todo-aat-1-tensor-adaptive-tempo-downstream-p-bbfe** (it lists all three).
- [246] "**Landing context.**" — **set aside**.

#### `deriv-mismatch-budget-attribution`

- [250] "`#example-kalman` is consumed by Corollary 1c … but deliberately absent from `depends:`…" — **guard** (explains a deliberate omission that `bin/lint-outline` would otherwise trip on).
- [251] "The class-ceiling leg of Proposition 4 and $\mathcal F(\mathcal M)$ … are defined over different objects…" — **joined item:influx-sufficiency-fitness-horizon-and-class** (C.4). The body's table (:104) already marks the identification as interpretation.
- [252] "Under Model S the relation $R^\ast = \rho/\alpha$ changes homogeneity in $\alpha$…" — **owed → item:mismatch-budget-attribution-under-model-s** (C.4).

### Part p2 — Appendix A, `deriv-persistence-cost` to the end (helper fork)

*KR I.9. Written by a fork of the WN-01 drain, to be merged into `wn-01-other.md`. 113 items in 24 segments, all read whole at `dc2b262c`. Body checks were made by grep on the body (Working Notes excluded), reading the matching paragraph where the grep hit; where a disposition rests on the note's own words, it says "per the note; not re-checked". The Part I lane was live on `deriv-sector-condition`, `deriv-stochastic-non-exit`, `detail-linear-ode-approximation`-adjacent `hyp-mismatch-dynamics`, and `result-sector-persistence-template` when this ran; no Working-Note line here is one it is changing as far as its branch diff shows, so nothing below is marked in flight.*

**Counts.** 113 items: canon 12 · superseded 1 · owed → new item 34 (into 15 items) · joined an existing item 21 · guard 21 · set aside 24. An item split between dispositions is counted under its main one.

**New ledger items (15):** item:persistence-cost-extensions, item:regime-indistinguishability-extensions, item:cor-a1s1-dichotomy-recurrence, item:tempo-additivity-pid-citations, item:tempo-additivity-finite-correlation-interpolation, item:detection-latency-extensions, item:variational-sector-extensions, item:sector-template-extensions, item:approximation-tiering-diagnostic-cost, item:two-kalman-ib-frontier-and-numeric-check, item:independence-audit-dependency-graph-and-bounds, item:partial-coupling-typology-open-lines, item:partial-coupling-brief-feynman, item:w1-leak-amplifying-state, item:resource-budget-open-dynamics. (vsect warned that two looked close to existing items: independence-audit vs `proposals-d-8-sp-16` (the empirical profile, which the new item cites) and resource-budget vs `proposals-d-6-o-bp12` (a master variable across the four $\beta$s, not the budget's own dynamics). Both read and judged distinct.)

**Raised onto existing items (22, `vsect raise`):** todo-adjacent-identifiability-floors-disc-ide-90c4, proposals-c-3-sp-14-observation-channel-capacity-c-f419, primary-source-verify-or-replace-with-read-sourc, structural-adaptation-genericity-bridge, spikes-proposed-advanced-18-cross-agent-value-functional-narrowne-bf71, impossibility-clusters-owed-reading, spikes-proposed-sub-scope-alpha-single-peaked-preference-16d5, proposals-e-3-sp-9-fenchel-bregman-reframe-of-addi-d684, todo-aat-1-tensor-adaptive-tempo-downstream-p-bbfe, spikes-proposed-r2-detection-latency-sharpening-under-mo-d44a, untested-catalog-predictions-for-e, mismatch-dynamics-model-d-equality-scope, question:separability-general-open-infectious, separability-ladder-extensions-and-necessity, the-heterogeneous-gain-closure-defect-does-not-v, proposals-d-8-sp-16-independence-audit-as-empirica-ea97, der-belief-strategy-attractor-conditional-run-th, land-the-leakage-locus-result-of-spikes-spike-le, w1-boundary-toy-sim-unregistered, spikes-proposed-decomposed-empirical-estimator-accuracy-e63e, proposals-d-6-o-bp12-resource-budget-b-t-as-master-2773, part-iii-segments-name-their-regime-tier.

**Dead pointers that are not dead.** `spikes/fight/` (`#form-resource-budget` [536]) and `spikes/spike-enrichment-cluster1-2026-05-21/` (`#result-certificate-existence` [705]) both exist under `spikes/.integrated/`; the Working-Note paths just predate the move.

#### `deriv-persistence-cost`

- [259] "**Template-cost subsection.**", [260] "**Model D adversarial analog.**", [261] "**Non-Gaussian signals.**", [263] "**Composite persistence cost.**", [265] "**Connection to #schema-strategy-persistence.**" — **owed → item:persistence-cost-extensions** (C.4), (a)–(e). The body has a "Relationship to `#result-sector-persistence-template`" paragraph (:137) that enumerates instantiations but states no parametric template-cost bound. [265]'s "pending spike G" no longer resolves.
- [262] "**Misspecification cost.**" — **joined item:todo-adjacent-identifiability-floors-disc-ide-90c4** (its misspecification-cost extension; raised).
- [264] "**Observation-channel capacity as notation.**" — **joined item:proposals-c-3-sp-14-observation-channel-capacity-c-f419** (raised).
- [266] "**Not forced by a Cauchy-FE axiom.**" — **guard**: records that this bound is a non-example of `#disc-additive-coordinate-forcing` (its linear-in-$\alpha$ coordinate comes from the Gaussian RDF's form, not an additivity axiom). That segment's body does not mention it (grep `persistence-cost`, `rate-distortion`: none); the note keeps someone from cataloguing it as a fourth instance.
- [267] "**Landauer-coefficient correction (2026-05-30).**" — **set aside** (history; the body carries the corrected $k_BT$/nat form, :121, checked; the refuted 0.35 form is guarded at `#impl-persistence-and-limits`, p4 [623], form (b)).

#### `deriv-recursive-update`

- [268] "C3's definitional character is a feature, not a bug — but it must be stated honestly." — **canon** (:23, "C3 … is *definitional* and cannot be 'violated'"; checked).
- [269] "The continuous-coupling generalization (Attack 2) deserves a proper note somewhere" — **canon** (the body's "Attack 2: Continuous environmental influence", :137). The event-time seam it touches is item:influx-event-time-seam.
- [270] "The information-set formalization (Doob-Dynkin) provides the cleanest technical proof." — **canon** in part (the body uses Doob–Dynkin, :125). Which proof is primary is a presentation choice; the body's measure-theoretic restatement has its own open defect, item:influx-recursive-update-information-sets. Set aside beyond that.

#### `deriv-regime-marginal-indistinguishability`

- [271] "**Provenance.**" — **set aside**.
- [272] "**Cross-regime witness sub-cases.**", [273] "**Connection to escape (e).**", [274] "**Composite-of-composites lift.**", [275] "**Fano-style finite-sample refinement.**" — **owed → item:regime-indistinguishability-extensions** (C.4). [273]'s scoping (escape (e) separates Witness 2, not Witness 1) is not in the body (grep `escape (e)`: none), so the item asks for it there.
- [276] Migration note — **set aside**.
- [277] "**Primary-source verification spike queued (2026-05-21).**" and [278] the `[^bg2-2026-05-21]` footnote — **joined item:primary-source-verify-or-replace-with-read-sourc** (raised with the ordered target list and the Hamdan 2000 caution).

#### `deriv-sector-condition`

- [283] "The adversarial extension (Prop A.3, coupled agents) and effects spiral (Cor A.3.1) are in #der-adversarial-destabilization…" — **guard** (where results that used to live here now live).
- [284] "The vector treatment of $\delta(t) \in \mathbb{R}^n$ connects directly to per-dimension tempo analysis" — **canon** in `#result-per-dimension-persistence` and `#deriv-matrix-persistence-condition`. Set aside.
- [285] "A global sector condition … would give global stability, making $\Delta\rho^\ast$ infinite" — **canon** (the derivation table, :346, "Global sector condition would give $\Delta\rho^\ast = \infty$ … rejected as unrealistic"; checked).
- [286] "Landing-context provenance: the sub-scope $\alpha$/$\beta$ partition…" — **set aside** (provenance).
- [287] "Landing-context provenance (A.1N + register)…" — **guard** (its closing "do not restore a fixed-agent iff" regression guard); the narrative before it is history.
- [288] "Regression guard (Model S containment)…" — **guard**.
- [289] "*Low-confidence ideation…*" — first and third glimpses **owed → item:cor-a1s1-dichotomy-recurrence** (C.4); the second glimpse **joined item:structural-adaptation-genericity-bridge** (raised; the note's "Three-Deaths" is a retired name and should not travel).

#### `deriv-social-welfare-aggregation-impossibility`

- [297] "**Provenance.**" — **set aside**.
- [298] "**Open before `candidate`.**" — (a) **joined item:impossibility-clusters-owed-reading**; (b) **joined item:spikes-proposed-advanced-18-cross-agent-value-functional-narrowne-bf71**; (c) **joined item:spikes-proposed-sub-scope-alpha-single-peaked-preference-16d5** (all raised).
- [299] "**The cluster's range, complete after this commit.**" — **set aside** (a status assessment; the future candidates it names are items `…advanced-16…` and `…advanced-17…`).
- [300] "**The Arrow-unique cardinal adjacency as the cluster's most-illuminating open question.**" — **joined item:spikes-proposed-advanced-18-cross-agent-value-functional-narrowne-bf71** (raised, with the note's emphasis).

#### `deriv-stochastic-non-exit`

- [301] "Regression guard: the Ville/Doob route…" — **guard**.
- [302] "The generality (any $F$ under A2', not just OU) rests on…" — **guard** ("no further strengthening of this half is open").
- [303] "Low-confidence glimpse (per "working notes FTW")…" — **owed → item:cor-a1s1-dichotomy-recurrence** (the same glimpse as [289]'s first).

#### `deriv-strategy-cost-regret-bound`

- [316] "**Linear vs. square-root form — revisit with downstream evidence.**" — **set aside**: conditional on the four-$\beta$ unification being strained, which is item:proposals-d-6-o-bp12-resource-budget-b-t-as-master-2773's scoping question; nothing to do until that answers.
- [317] "**Stochastic-$\pi^\ast$ extension.**" — **set aside**, reason: the body already names it as the scope boundary of the BH identity (§9, :106, checked), so a reader meets it there; an item adds nothing until a consumer needs stochastic optima.
- [318] "**Family characterization strengthening.** *Resolved 2026-04-22*" — **guard**, for its citation audit (Csiszár 1972, Amari 2009 Theorem 1 and Amari–Cichocki 2010 Prop 3.2 do *not* contain the chain-rule uniqueness theorem); the resolution itself is history (body §6.1).
- [319] "**BH identity under deterministic $\pi^\ast$…** *Resolved 2026-04-24.*" — **set aside** (history; body §4).
- [320] "**Citation verification (Path 1 content, §6.4).**" — **guard** (the Rubin 2012 vs TP2011 attribution correction).
- [321] "**AAT-outlier-on-KL-direction…**" — **canon** (:126, optimum-first; checked).
- [322] "**Cross-reference to NeurIPS Paper 2.**" — **guard** (forward pointer). `influx-scout/neurips.md` §3 records the point-mass identity as already in canon here (§4) before the paper, so the proposed standalone segment is the influx drain's to decide.
- [323] "**Fenchel-Bregman connection…**" — **joined item:proposals-e-3-sp-9-fenchel-bregman-reframe-of-addi-d684** (raised).

#### `deriv-strategy-proofness-impossibility`

- [324] "**Provenance.**" — **set aside** (the load-bearing point it records, $\alpha'$ secures convergence, not strategy-proofness, is the body's adjacency framing at :14; checked in part).
- [325] "**Open before `candidate`.**" — (a) **joined item:impossibility-clusters-owed-reading**; (b) and (c) **joined item:spikes-proposed-sub-scope-alpha-single-peaked-preference-16d5** (raised, (b) named as a further sub-spike).
- [326] "**The composite-revelation-mechanism reading and its sub-agents.**" — **canon** (:56–57; checked).
- [327] "**The cluster's discipline filter.**" — **set aside** (an assessment, not a claim).

#### `deriv-tempo-additivity`

- [328] "**Citation verification before promotion.**" — **owed → item:tempo-additivity-pid-citations** (F.2).
- [329] "**Finite-correlation-time interpolation.**" — **owed → item:tempo-additivity-finite-correlation-interpolation** (C.4).
- [330] "**Loewner-order statement.**" — **joined item:todo-aat-1-tensor-adaptive-tempo-downstream-p-bbfe** (raised).
- [331] "**Attribution conventions.**" — **guard** (forward pointer: choose the attribution convention consciously).
- [332] "**Trail.**" — **set aside** (provenance; the citations it mentions are [328]).

#### `deriv-update-detection-latency`

- [333] Migration note — **set aside**.
- [334] "**R2 sharpening (model-class inadequacy).**" — **joined item:spikes-proposed-r2-detection-latency-sharpening-under-mo-d44a** (raised).
- [335] "**R3 reference, not extension.**" — **canon** (:77, :93; checked).
- [336] "**Extension beyond Beta-Bernoulli.**", [337] "**Probability bound.**", [339] "**Multi-timescale connection.**", [340] "**Part III analog.**", [341] "**Class 3 (Coupled) architectures.**" — **owed → item:detection-latency-extensions** (C.4), (a)–(e).
- [338] "**Testable prediction.**" — **joined item:untested-catalog-predictions-for-e** (raised; that item already lists detection-latency growth with experience).

#### `deriv-variational-sector-condition`

- [342] "Landing context…" — **set aside**.
- [343] "**Open: $O(\varepsilon)$ rate via Talagrand T2.**", [344] "**Amortization gap bounds.**" — **owed → item:variational-sector-extensions** (C.4).
- [345] "**Connection to natural-gradient VI.**" — **canon** (:58, Khan & Lin 2017; checked).

#### `detail-linear-ode-approximation`

- [346] "The vector ODE … assumes isotropic correction…" — **canon** (`#deriv-matrix-persistence-condition` carries the anisotropic form). Set aside.
- [347] "The norm-inequality subtlety (Section 1 above) propagates into the adversarial scaling law…" — **joined item:mismatch-dynamics-model-d-equality-scope** (raised; the body's :56–62 is the norm inequality it builds on).
- [348] "Model S's Ito-Lyapunov derivation assumes $\sigma_w$ is constant." — **owed → item:sector-template-extensions** (b).

#### `disc-approximation-tiering`

- [366] "**Formal characterization of the tiering pattern.**" — **joined item:separability-ladder-extensions-and-necessity** (raised).
- [367] "**Interaction between tierings.**" — **joined question:separability-general-open-infectious** (raised).
- [368] "**Diagnostic costs.**" — **owed → item:approximation-tiering-diagnostic-cost** (C.4).

#### `disc-compression-operations`

- [375] "**The $\Sigma_t$ source reformulation changes the theoretical quantity…**" — **superseded**: `#form-strategy-complexity-cost` now cites this segment for $\beta_\Sigma$ (:74; checked).
- [376] "**(P1) as IB Lagrangian-dual does not close #form-composition-closure's other Working Notes.**" — **set aside**: it restates that those questions are open; they are item:composition-closure-open-computations.
- [377] "**Synthesis segment vs. full unification.**" — **guard** (the stopping rule for when to escalate to a full rewrite).
- [378] "**The Gaussian IB frontier derivation is deferred.**", [379] "**The heterogeneous-gain numeric check is unrun.**" — **owed → item:two-kalman-ib-frontier-and-numeric-check** (C.4); [379] also raised onto item:the-heterogeneous-gain-closure-defect-does-not-v.

#### `disc-independence-audit`

- [428] Migration note — **set aside**.
- [429] "**Interaction between assumptions.**", [430] "**Quantitative failure modes.**" — **owed → item:independence-audit-dependency-graph-and-bounds** (C.4).
- [431] "**Empirical audit.**" — **joined item:proposals-d-8-sp-16-independence-audit-as-empirica-ea97** (raised).

#### `disc-partial-coupling-pathways`

- [445] "**Promotion path requires two sub-spikes.**" — **joined item:der-belief-strategy-attractor-conditional-run-th** (raised; its "Both are in `TODO.md`" is stale).
- [446] "**Composite-level sub-type inheritance.**", [447] "**Trajectory coupling as separate axis.**", [448] "**Refined behavioral estimator — construction.**" — **owed → item:partial-coupling-typology-open-lines** (C.4).
- [449] "**Brief is not yet at Feynman criterion.**" — **owed → item:partial-coupling-brief-feynman** (H.1).
- [450] "**Connection back to `#def-agent-spectrum` Working Note.**" — **joined item:land-the-leakage-locus-result-of-spikes-spike-le** (raised).

#### `disc-sandbox-evaluation-ceiling`

- [451] "Promoted to its own segment 2026-05-28…", [452] "Open placement question … now resolved toward Appendix A…" — **set aside** (history).
- [453] "The theorem-grade formalization of the underlying loop-Level-2 result lives in NeurIPS 2026 Paper 2…" — **guard** (forward pointer; influx drain owns the paper).
- [454] "**Re-grounding 2026-05-30 (transportability spike…)**" — **guard** for its regression content (the "forkability implies Level 1" lemma is false: RCTs are forkable and Level 2); the rest is history. The segment's own open defects are item:disc-sandbox-evaluation-ceiling-four-defects-fro.

#### `disc-w1-structural-bound-boundary`

- [487] "Reasoning trail (filed)…" — **set aside** (provenance).
- [488] "The exact-enumeration sim exhibiting the $\Theta(\varepsilon^2)$ flatness…" — **joined item:w1-boundary-toy-sim-unregistered** (raised; the tracker it says the sim is blocked on was deleted today).
- [489] "**Open: amplifying-state mechanisms.**" — **owed → item:w1-leak-amplifying-state** (C.4).
- [490] "**Open: behavioral-monitor construction.**" — **joined item:spikes-proposed-decomposed-empirical-estimator-accuracy-e63e** (raised).

#### `form-resource-budget`

- [535] "The regenerative regime $r_{\mathcal{B}}\gt 0$ …" and [537] "Open: whether $\mathcal B_t$ should be vector-valued…" — **owed → item:resource-budget-open-dynamics** (C.4). The body (:53) lists alternative resource models as a representational choice but not these two dynamics.
- [536] "Reasoning trail: `spikes/fight/03-energy-bound-effects-spiral.md`…" — **guard** (provenance pointer; the path has moved to `spikes/.integrated/fight/`, which the item records).
- [538] "A NOTATION.md entry for $\mathcal B_t$ is added under a resource section" — **canon** (`NOTATION.md`:188; checked).

#### `internal-external-decomposition`

- [680] "Boundary regression-guard (2026-07-03, audit 731548 B-2)…" — **guard**. The segment's separate open defect on its constitutive no-go is item:internal-external-decomposition-59-states-the-co.

#### `obs-authored-world-laboratory`

- [684] "**Provenance and living bridge.**" — **guard** (pointer to `doc/vivarium.md` and the vivarium twin). Its `~/src/archema-io/vivarium/…` paths are stale; they now resolve under `~/src/arch/vivarium/`.
- [685] "**Build-state re-verification.**" — **guard**.
- [686] "**Chronica link (forward, cross-volume).**" — **guard**, with one slip in it: it places `#def-chronica` in `04-eli-core`; the segment is in `01-aat-core`. The co-development it asks for (`#hyp-checkpoint-forking-failure-modes`) is a forward pointer; the related non-forkability defect is item:influx-non-forkability-tier.
- [687] "**P2 uniqueness-claim maintenance.**" — **guard**.

#### `result-certificate-existence`

- [704] "**Provenance.**", [706] "**Provisional slug.**" — **set aside**.
- [705] "**R0-loss landing (2026-05-22).**" — **set aside** (history). Its admitted gap, the mid-case center-manifold construction (Carr 1981) sketched but not derived, is visible in the body's "Mixed case — Conley anchoring" paragraph (:93), so a reader meets it there; it is standard machinery and asks nothing new.
- [707] "**Organizing-principle linkage.**" — **set aside**: the step it waits on is an edit to PROPOSALS Bundle 1, and PROPOSALS is gone (its items are in the ledger; no Bundle-1 item names "contraction-over-drift").

#### `result-sector-persistence-template`

- [717] "The template is type `result` because…" — **guard** (why not `formulation`).
- [718] "Candidate extensions that would strengthen the template…" — **owed → item:sector-template-extensions** (C.4).
- [719] "The template's role in #disc-composition-consistency's "applies at every level" claim is now explicit…" — **canon**: `#disc-composition-consistency`:74 states transfer as tier-dependent (Tier 1 exact, Tier 2 degraded, Tier 3 per-domain), which is the testable form the note asks for (paragraph read; the phrase itself does not appear).
- [720] "**Dynamic-regime placement (added 2026-05-21…)**" — **joined item:part-iii-segments-name-their-regime-tier** (raised).

#### `sketch-structural-adaptation-genericity`

- [757] "Provenance: parent-generated 2026-05-16…" — **set aside** (provenance; Joseph's "it will get its day in the light" is why the segment exists, recorded in git).
- [758] "Segment-vs-spike judgment (recorded so it is not re-litigated)…" — **guard**.
- [759] "Related: the `#disc-identifiability-floor` family…" — **joined item:structural-adaptation-genericity-bridge** (raised).
