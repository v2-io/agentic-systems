# Drain: `01-aat-core` Working Notes outside the audit-gold blocks

*KR I.9 of `../INTENT.md` (every backlog surface drained into the ledger, one disposition per source item), serving I.10 (signal against noise) and I.5 (Working Notes carry only forward pointers and regression guards). Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." Working file, 2026-10-30, written as it goes.*

*In progress. Parts are being read in parallel; each part's dispositions land in `wn-01-other-pN.md` beside this file and are merged here when done.*

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

| part | OUTLINE sections | items | segments | file | coverage |
|---|---|---|---|---|---|
| p1 | Appendix A, `der-belief-…` to `deriv-mismatch-…` | 79 | 17 | `wn-01-other-p1.md` | pending |
| p2 | Appendix A, `deriv-persistence-cost` to the end | 113 | 24 | `wn-01-other-p2.md` | pending |
| p3 | Part II Meta-Architecture I | 104 | 16 | `wn-01-other-p3.md` | pending |
| p4 | Part I (all chapters) and the Part II preface and Lift | 141 | 28 | `wn-01-other-p4.md` | pending |
| p5 | Part II Causal Access, Strategy Structure, Strategy Dynamics, Orient Cascade | 130 | 25 | `wn-01-other-p5.md` | pending |
| p6 | Part III Meta-Architecture II, Scope and Formation, Composition Machinery | 85 | 11 | `wn-01-other-p6.md` | pending |
| p7 | Part III Unity, Cooperative/Adversarial, Strategic Composition; Appendix B | 100 | 21 | `wn-01-other-p7.md` | pending |

**Helpers.** All six fork launches were refused (the session's subagent cap), so every part below is read by this one agent, serially, in the order p4, p3, p5, p6, p7, p1, p2. The coverage column above is updated as each part closes.

**Cross-surface rule (Joseph, relayed 2026-10-30).** For each item that makes or joins a ledger entry, the other surfaces were searched for the same claim (slug and key phrases over `audits/`, `spikes/`, `msc/`, the influx regional files, other segments' Working Notes, `items/`, `questions/`). One ledger item carries every source found. Canon, history and guard dispositions were not searched across surfaces; nothing turns on them.

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
- [121] "**Engineering design for Class 3 (Coupled) agents.** … Hafez et al. (2026) … 89.3% of coupling degradations against 44.0%" — the IDT row is in the body's Related Work (:256). The figure attribution is **joined item:hafez-citations-der-agent-opacity-109-169-say-h** (F.3) and **review:b1-part-ii-check-1#C7** (which checked the abstract's 89.3%). The engineering-design paragraph is Volume 3 material: **set aside** for 01 (Volume 3's wrapping segments carry it).
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
- [235] "**Environmental common causes and the CMC.**" — **canon** (the body's "Exactness of Status Propagation" and `#def-strategy-dag`'s correlated-failure paragraph). Set aside.
- [236] "**Promotion potential.**" — **set aside** (status narration).

#### `deriv-observation-ambiguity-bias-bound`

- [253] "**Regression guard.** Do not restore the information term…" — **guard**.
- [254] "**$\rho_{\text{LSI}}$ for AAT-native cases.**" and [255] "**Large-information regime.**" — open computations. **owed → item:bias-bound-lsi-constant-and-large-information-regime** (C.4), citing `influx-scout/neurips.md` §4.3 ("$C=\sqrt2$ is universal" without the small-information qualifier) as the body-side defect of the same regime question, and Paper 3's spherical-arc constant as unread influx.
