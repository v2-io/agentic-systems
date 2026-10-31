# Influx drain, second half

> **KR: G.2** in `../INTENT.md` (*stranded additions are landed at honest tier or set aside with a recorded reason*). Canon defects found here are routed to **C.1** (C.3 for contradictions between segments, C.4 for open strengthenings), argued and non-derived material to **G.0**, the strategy apparatus to **B.2**, terminology to **F.1/F.4**, citations to **F.2/F.3**. Top intent: *"Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."* After a compaction, re-read `../INTENT.md`, then this file.

*Drain agent (Opus 5.5), 2026-10-30, for the lead (who reads this whole) and the integrators (who work from the ledger items it records). Sources: the influx scout's regional files `agent-core.md`, `agent-core-memory.md`, `agent-core-rest.md`, `arch-program.md`, `arch-program--proprium-ingest-corporeum.md`, `firmatum-vivarium.md`, `aisi-risk-notability.md`, `aisi-risk-notability--rest.md`, `periphery.md` (all in `../influx-scout/`).*

## Method

- Every disposition is checked against canon at asf `main` (`cbd2f345` when I started), not against the scout's row. The scouts checked at `5ade664d` (2026-08-24); about 270 commits landed today, and several defect sites had moved or been fixed.
- Before each item I checked `vsect open segment:<slug>` and grepped `items/` for the slug and key phrases. Where an item already existed I appended this drain's source to it (an "Also (influx drain, second half)" paragraph) instead of opening a twin.
- Following Joseph's instruction relayed by the lead, each item cites every source bearing on the same claim that I found (other regional files, canon Working Notes, audits, the sibling drain's regions), so the owners of those surfaces can mark their source "disposed with item:<id>".
- Item ids are the `items/<slug>.md` filenames. `--by drain-influx-2`.
- Dispositions: **IN** (in canon at HEAD, where), **DEFECT** (canon defect still present; item), **ADD** (true or worth having, not in canon; item at honest tier), **LEDGER** (already an open item; source appended), **MOOT** (overtaken by a landing today), **ASIDE** (set aside, with the reason).
- Helpers: one reads agent-core's seven unread `memory/research/` notes (`influx-2-memory-research.md`), one drains `firmatum-vivarium.md` and vivarium's `msc/` (`influx-2-firmatum.md`). A third, for `arch-program*`, was refused by the session's concurrency cap, so I am draining those myself.

## Dispositions per source item

### agent-core (`agent-core.md`, `agent-core-memory.md`, `agent-core-rest.md`)

| Source item | Disposition | Item / where |
|---|---|---|
| §4.6 / MAP D9: Brief "the loop is the only escape" in `#disc-constructive-impossibility-posture`, copied to `FINDINGS.md:222`, `CURRENT-VOL1.md:3442` | DEFECT (public surface; lead told at once, routed to the Part I round-3 lane) | `findings-brief-overclaim-on-public-surfaces-map` (C.1) |
| §4.1–4.2 / MAP D8: `#impl-strategy-dynamics:42` calls scope conditions (S1)–(S5) "boundary routes"; `:44` "shared escape mechanism" vs `#impl-strategy-structure:72` guard (2) | DEFECT, both present at HEAD | `impl-strategy-dynamics-contradicts-its-own-sourc` (C.1) |
| §4.3, §4.5: "load-bearing / structural requirement for recovering Part II persistence guarantees" in `#impl-scaffolded-logogenic:28` and its origin `#scope-scaffolded-logogenic:30`, against `#impl-orient-cascade:74`; with P16 (harness-velocity scaffold stratification) as the honest replacement, and memory B6 (the "REM sleep has a Shannon floor" type mismatch) in the same segment | DEFECT + ADD, one item | `the-scaffolding-overclaim-in-volume-3-its-origin` (C.1) |
| §4.7 / memory B1: $\lambda$ for log-odds and retention in one derivation; five-plus meanings; `NOTATION.md` lists one | DEFECT | `lambda-names-at-least-five-objects-in-canon-and` (F.4) |
| §4.8 / memory B2: CLS fast/slow swapped in (N1) | DEFECT (line 57 now) | `form-consolidation-dynamics-n1-assigns-the-store` (C.1) |
| memory A1, B7: body of `#form-consolidation-dynamics` asserts what its F74–F77 Working Note rejects; never cites `#der-multi-timescale-stability`; two catastrophic-forgetting accounts | DEFECT, with the strengthen route | `form-consolidation-dynamics-s-body-still-asserts` (C.1) |
| §4.4: hard-ceiling convention spike | MOOT: the hard ceiling was deleted by F72 (`5e621256`) | — |
| §2.B P5 / memory B5 / MAP D4: compensation-channel overreach, retrieval channel, generator drift | DEFECT, joined with arch 09-23 and logos 09-25 L1a | `der-compensation-channel-uniqueness-overreaches` (C.1) |
| P15 / memory B4 / §6 / P7 (theory half): no record-read operation in AAT's core | ADD (formulation, nothing derived) | `aat-s-core-has-no-operation-for-an-agent-reading` (G.2) |
| memory C1: `#def-mismatch-signal` normalizes by observation noise, `#form-composition-closure:318` by innovation covariance | DEFECT (C.3) | `def-mismatch-signal-normalizes-surprise-by-the-w` (C.3) |
| P1 / §5: what kind of claim each strategy-DAG segment makes; ascribed vs stored $\Sigma_t$ | ADD | `say-at-the-front-of-the-strategy-chapters-what-k` (B.2) |
| P2: type/token gap | ADD (gap in canon) | `the-strategy-dag-s-acyclicity-and-its-credence-l` (B.2) |
| P3: commitment state and commit criterion | LEDGER: appended to `proposals-d-4-sp-12-commitment-resource-temporal-d-1dea` | — |
| P8: objective vs terminal revision | DEFECT (conflation; motivating instance contested) | `form-structural-change-as-parametric-limit-s-ope` (C.1) |
| P4 + P9: explanation-dissolved aporia; node status as observation vs declaration | ADD (observation tier) | `what-registered-a-mismatch-and-what-settled-a-no` (G.2) |
| P10 + P14: channel typing; thinking as summary; typed harness channel | ADD (discussion-grade) | `why-a-chat-trained-llm-is-class-3-has-a-sharper` (G.2) |
| P13 (B2): forgetting as necessity vs latent diversity vs prerequisite | DEFECT (C.3) | `three-canon-passages-on-forgetting-point-differe` (C.3) |
| P13 (`#scope-agent-identity` vs `#obs-context-turnover`) | IN: `#scope-agent-identity:42` now states "*Not* excluded: a state discontinuity on one trajectory ... a session boundary" | — |
| P13 (B4: auxilia reports as "extension of self" vs messages with source uncertainty) | ASIDE: the "extension of self" phrasing is not in canon at HEAD (grep), so there is no tension to state; `#def-auxilia-hierarchy` was revised today by the Volume 4 lane | — |
| P11: SCC-condensation defect as a measure of disunity of intent | ASIDE: the formula is canon (`#def-strategy-dag`); the use is marked "[mine]" by its source and nobody has checked that it tracks what a reader would call disunity. Worth a spike before any landing, not a ledger line | — |
| P12: attention governance | LEDGER: raised on `spikes-routing-spike-attention-governance-archived-vs-r-61bb` (sibling `todo-group-iv-attention-pair-spike-attention-126c`), adding $\mathbf J = \partial\Sigma/\partial M$ | — |
| P7 (missing 03 rows: folding, probe evaluation, honest folds, retrospective salience) | LEDGER: appended to `todo-loga-missing-stubs-genuinely-absent-in-0-9487`; Peak-End "theorem" and CMC guarantee recorded there as *not* to land | — |
| P17: `#form-ephemeral-persistent-duality` row out of date (thinking blocks now sent up and persisted) | LEDGER: appended to `todo-author-the-three-missing-staged-outline-76f2` | — |
| rest §2.A: `#obs-context-turnover` carve (session / epoch / rendered view; multi-authored, opaque $f_{\text{init}}$; "compaction") | ADD | `obs-context-turnover-lacks-a-turnover-carve-that` (G.2) |
| rest §2.A.3, §2.B.3: forks as default shared-state delegation; task-fork incidents | ADD (evidence, no change of claim) | `shipping-delegation-now-runs-on-exactly-the-shar` (G.2) |
| rest §2.B.2, .4, .5 (`#disc-five-forcing-functions` cache/round-trip evidence; consolidation footprint; interleaving failures) | ASIDE for now: coding-harness census at `inferred` tier, 13 of 25 ledes superseded within two days; the durable part (the scaffold stratification) is in the scaffolding item | — |
| rest §2.C: harness-velocity `CLAIMS.md` conventions | ADD (process) | `four-instruments-for-keeping-canon-true-built-ou` (I.6) |
| rest §2.D: ecosystem-velocity, harness-census, comproprium copy, settings inventory, root copies | ASIDE: market census or byte-identical copies (the scout's `diff`/`cmp`); `harness-census/pipeline.py` opens with `TRUNCATE … CASCADE`, not to be run | — |
| §6 memory corpus: event segmentation (P6, A2, C5), standard names (C2–C4, B8), replay regulation, schema effects, power-law forgetting | Drained by the memory helper (below) | see helper section |
| §8: citation-audit instrument; "good briefs show" | ADD (process) / IN (AGENTIC-DELEGATION already carries the second) | `four-instruments-for-keeping-canon-true-built-ou` (I.6) |

### arch program (`arch-program.md`, `arch-program--proprium-ingest-corporeum.md`)

The helper I briefed for these two files was refused by the session's concurrency cap, so I drained them myself.

| Source item | Disposition | Item / where |
|---|---|---|
| §2, §13.1 / MAP D3: turnover-recursion R2 "iff" at exact, half derived | DEFECT (line 80, 103 at HEAD; sporadic counterexample re-checked) | `der-turnover-information-recursion-r2-states-an` (C.1) |
| §2, §13.2: compensation-channel retrieval gap | DEFECT, joined into the identity-cluster item | `der-compensation-channel-uniqueness-overreaches` (C.1) |
| §2, §13.3 / MAP D15: proper scoring rules, performative prediction | ADD (strengthening route) | `hyp-truth-serving-loophole-s-open-premise-has-a` (C.4) |
| §2, §13.24: "the taxonomy answers to the definition" vs representational choice | DEFECT (C.3) | `def-death-as-factor-loss-contradicts-itself-on-w` (C.3) |
| §2: robust stability vs robust performance as the neighbour of task adequacy | LEDGER: appended to `terminology-todo-task-adequacy-r-ast-lt-lvert-delta-text-9ecd` | — |
| §1.1, §13.4: (a)–(d) strategy stratification | ADD, joined with agent-core P1 | `say-at-the-front-of-the-strategy-chapters-what-k` (B.2) |
| §1.1, §13.11: token vs type credence learning | ADD, joined with agent-core P2 | `the-strategy-dag-s-acyclicity-and-its-credence-l` (B.2) |
| §13.5, .7, .10: healthy forgetting as sufficiency-preserving compression; honest folds (convex, acyclic quotient); retrospective salience | LEDGER: appended to `todo-loga-missing-stubs-genuinely-absent-in-0-9487` | — |
| §13.6: "AAT Theorem of Peak-End Middle-Folding" | ASIDE: contradicted by canon (routine successes are Beta-Bernoulli count updates, so duration neglect discards calibration's sufficient statistic; middle-fold audit §C). Recorded as "not to land" in the missing-rows item | — |
| §13.8: confabulation as credit assignment without observability; 7B silent vs 30B rumination | ADD (hypothesis / observation tier) | `two-canon-results-predict-logogenic-failure-mode` (G.2) |
| §13.9 + §1.2 (forward-only; cost stays with the party that compacted; no gaslighting) + proprium A3 | ADD (derived-in-reach half) and G.0 (argued half) | `what-harness-compaction-does-to-an-agent-s-ident` (G.0) |
| §3, §13.12: concept-matrix unifications; witness and adversary share a channel | ADD, for B.3 | `three-candidate-unifications-of-what-asf-claims` (B.3) |
| §3, §5, §13.13, .14, .20: self-deception unreachable; subject premise (INCOHERENCE row 4); truth never ambient for a logogenic intelligence | ADD (argued) | `argued-claims-about-truth-stance-and-moral-scope` (G.0) |
| §6, §13.15: LEXICON "logogenic agent" says *self-actuated* | DEFECT (generated front door) | `the-lexicon-entry-for-logogenic-agent-overclaims` (F.1) |
| §7, §13.16: Joseph's forking ethics | ADD (argued) | `joseph-s-constructive-ethics-of-logogenic-forkin` (G.0) |
| §4, §13.17: collision as staleness detector; named absence | ADD (process) | `four-instruments-for-keeping-canon-true-built-ou` (I.6) |
| §8, §13.18: term-reliability "delete the name" test | ADD | `add-a-no-steward-test-to-the-naming-sop-alongsid` (F.4) |
| §8, §13.19: comproprium vera as logogenic claims (completion compulsion, free-variable fill, …) | ASIDE: lived-register practice whose own term map flags metaphor-carried terms; `ver-completion-compulsion` says its contrast class cannot be supplied from inside. Revisit only after F.4's naming test exists | — |
| §1.3, §13.21: directed-separation literature (Arghal et al., decode accuracy 75→60%) | ADD (citations, verify first) | `external-literature-that-bears-on-measuring-dire` (F.2) |
| §13.22: thinking-size measurement | ASIDE: uncommitted, one person's transcripts, estimated token counts; nothing to cite publicly | — |
| §5: reader-side evidence (Fable contemplation, year assessment) | Input to B.3 and H.3, not canon; the one theory line is in the argued-claims item | — |
| §9 / proprium A1: AXIOMATA "frozen … terminal values" | MOOT: the Volume 4 lane rewrote it today (`337970ab`, `70c491ce`): AXIOMATA is now writable, split across $O_t$ and $M_t$, "nothing in it is a terminal invariant"; its open check finding is `review:vol4-c1-check-2#C5` | — |
| proprium A2: which record is $\mathcal C_t$ (CHRONICA vs TRACTUS) | DEFECT (C.3), *sharper* after today's revision: the mapping now says CHRONICA keeps "events judged meaningful", i.e. a selection | `which-record-is-c-t-for-a-logogenic-agent-is-sti` (C.3) |
| proprium A3: no-gaslighting norm, lived instances, compaction ratio | ADD, joined into the compaction item | `what-harness-compaction-does-to-an-agent-s-ident` |
| proprium A4: port-specs' assembled "what persistence requires" | ADD | `assemble-what-volumes-3-4-jointly-require-of-an` (G.2) |
| proprium A5, A7: memory as emergent regimes; automatization; "consolidation is interiority" | ADD | `proprium-v2-holds-a-tft-era-memory-theory-canon` (G.2) |
| proprium A6: shared-context codebook vs auftragstaktik | ADD (discussion-grade) | `how-much-must-be-said-explicitly-depends-on-the` (G.2) |
| proprium A8: attention architecture roadmap | ASIDE: training/architecture leg Joseph separated out (STEWARD-JUDGMENT); not ASF claims | — |
| proprium A9: agent-behavior dossier's three AAT mappings | ADD (settle or set aside in one pass) | `a-local-agent-behavior-dossier-proposes-three-aa` (G.2) |
| proprium A10: entity types, sovereignty dimensions, failure-mode table, Assistant-Axis critique, Dunbar, Architectus synthesis, HTN survey, 2025-11 process notes, `lessons.md` | ASIDE, each low priority by the scout's reading; HTN is carried by the standard-names item; `lessons.md` belongs to the pedagogy pipeline (Joseph is its tested reader) | — |
| proprium §3: `#obs-substrate-independence` preface "a stub" | IN (fixed): 04 OUTLINE line 20 now says "Two proposed segments, not yet written"; the authoring item exists (`write-obs-substrate-independence-as-what-the-rec`) | — |
| proprium §3: `#der-the-scaffolding-tax` row merges two forcing functions | DEFECT (OUTLINE cell) | `der-the-scaffolding-tax-s-outline-row-04-eli-cor` (A.4) |
| proprium §3: other missing rows' source text | LEDGER: carried in the missing-rows items above and the existing 04 `todo-04-eli-core-src-*` items | — |
| proprium §4 / arch §9: 21 canon files cite dead `~/src/firmatum/`; `~/src/autopax/` moved | LEDGER: appended to `canon-bodies-cite-local-working-paths` (F.3) | — |

### AISI cluster and ai-risk-model (`aisi-risk-notability.md`, `aisi-risk-notability--rest.md`)

`aisi-eoi` and `notability-extracts` belong to a sibling drain (`aisi-eoi-notability.md`); where an AISI-responses item and an aisi-eoi card make the same claim, my item cites both.

| Source item | Disposition | Item / where |
|---|---|---|
| §1.0: `#hyp-truth-serving-loophole` landed from here (sketch) | IN (sketch, not second-agent-verified); its open premise is item `hyp-truth-serving-loophole-s-open-premise-has-a` | — |
| §1.1 C13, §1.5 R35 B, r23 table: control voids the convergence antecedent (positivity) | ADD; the 08-22 "institutional, not Volume 1" disposition was an agent's and is re-opened against `#der-loop-interventional-access`'s new positivity sentence | `a-control-regime-can-void-an-alignment-guarantee` (G.2) |
| §1.1 C10: learned helplessness literature | ADD (citations; WN asks for it) | `der-severed-actuation-dynamics-s-working-note-li` (F.2) |
| §1.1 A5, C11: corruption cheaper than cultivation; strategic tempo for institutions | ADD (argued + application) | `two-of-joseph-s-claims-from-the-aisi-work-extend` (G.0) |
| §1.1 C12 items 16, 18 | IN (`#disc-dynamic-regime-axis`; `#def-strategic-tempo` "slowest-revisited") | — |
| §1.1 4b / MAP D16: `#obs-backward-inference-empathy` cited as a result, row missing | LEDGER: `todo-loga-missing-stubs-genuinely-absent-in-0-9487` already names it and the preface overclaim | — |
| §1.1 plain-language consolidations; the 34 skeletons as an arc | Input to A.2 / B.3 (front door and purpose), not segments | — |
| §1.2: confidence and warrant diverge with success; "not hidden, absent"; absence as evidence | ADD | `joseph-s-confidence-and-warrant-diverge-and-the` (G.2) |
| §1.2: Joseph's list of what the field mistakes for capability scales and what is "off the radar" | Input to B.3; no item (a list, not a claim) | — |
| §1.3 rung 2, 15; §1.4 Claim 1: the record is the agent; two-sided record | ADD | `the-mutable-part-of-the-mind-is-the-record-for-a` (G.2) |
| §1.3 rung 10: shelf life of pre-deployment results | ADD | `every-pre-deployment-result-has-a-shelf-life-and` (G.2) |
| §1.3 rung 13: correlated monitors saturate | IN (mathematics: `#deriv-tempo-additivity` echo chamber); ADD (application) | `correlated-monitors-saturate-at-a-floor-no-monit` (G.2) |
| §1.3 rung 8; §1.4 Claim 5: one structural cause behind named LLM pathologies; coupling's other face; honesty as calibration | ADD | `one-structural-cause-behind-a-family-of-named-ll` (G.2) |
| §1.4 Claim 2: capability floors | ADD, joined with periphery §1 | `joseph-believes-asf-already-shows-that-intellige` (C.4) |
| §1.4 + rest §3.1–3.2: "aligned to whom", typed writers into $O_t$, attribution/force/epistemic status, root-access specimen | ADD (argued; G.0 first) | `canon-models-o-t-as-the-agent-s-own-and-treats-o` (G.0) |
| §1.4: Fable's "what is genuinely yours" and "where the meat is thin" | Input to the owner review / A.2 (outsider read, September); not a canon item | — |
| §1.5: `ASF-FIXES*` (unrouted ASF defect list) and sweep R34–R55 | Delegated to a helper (below) | `drain/influx-2-asffixes.md` |
| §1.5: regime census, cache-leak run, wrapping certifiability | ADD | `an-empirical-census-of-deployed-agent-frameworks` (G.2) |
| §1.5: `update-gain-icl` spike | Not reached (names only) | — |
| §1.6: honest-activation spike | LEDGER: `author-norm-honest-activation-and-its-derivation` (spike drain) | — |
| rest §3.3: logos perspective note (indexical gravity; induced stance cannot gate death-hood; three endings) | Sibling drain's logos region; the stance point is cross-cited in the self-report item | — |
| rest §3.4: selection on self-report; treatment raising honesty | ADD (argued) | `selection-on-self-report-corrupts-the-evidence-f` (G.0) |
| rest §3.5: STAMP/STPA, Reason | ADD (low priority) | `external-evidence-and-prior-art-canon-could-cite` (F.2) |
| rest §3.6: process lessons (truthification passes; no README per source; Sonnet "ledger" vs Opus "investigation") | Adjacent; the first restates ASF's own staging discipline; not ledgered | — |
| rest §3.7: "ASF" is also NAVER's AI Safety Framework | Adjacent (naming fact for the publication program); not a canon item | — |
| rest §3.8 | ASIDE (risk-literature infrastructure; the scout's reasons) | — |

### Periphery (`periphery.md`)

| Source item | Disposition | Item / where |
|---|---|---|
| §1: intelligence ≠ capability ≠ propensity; floors | ADD (strengthen or tell Joseph it is not yet in the theory); private source pointed to, not quoted | `joseph-believes-asf-already-shows-that-intellige` (C.4) |
| §1, §4: emergence layers, covenant vs calibration, negative and partial cases | ADD, Joseph-gated (private and cohort sources) | `the-emergence-material-for-volume-4-has-the-nega` (G.0) |
| §1: interiority under sealed traces; correction lands on the wrong object | Not ledgered separately: source is private and uncommitted; its public-side content is in the confabulation item and the turnover-carve item (is sealed reasoning part of $\mathcal C_t$?) | — |
| §1: OpenAI report on self-injected compaction summaries | LEDGER: raised on `what-harness-compaction-does-to-an-agent-s-ident` (the public report, not the private repo) | — |
| §1: concealment empties the witness relation; three degrees of visibility | ASIDE: Joseph-gated (sacred-register source); discussion-grade at most | — |
| §1: "Primary Efforts" six modes; "Add to the alignment model" list | Input to B.3 / ai-risk-model; not canon | — |
| §2: `_core/tst` | IN (absorbed; `diff`-checked by the scout); reader-question sets ADD | `two-sets-of-reader-questions-on-the-tst-theorems` (C.1) |
| §2: Living Code guide | ASIDE: practice guide; worked instantiations at most | — |
| §3: direction of fit; §6: AND/OR-graph pillar uncited, HTN absent | ADD | `two-standard-names-canon-lacks-for-its-most-basi` (F.1) |
| §3: Joseph's digitized architecture notes (entity questions; VERA pipeline) | ASIDE for canon: working model, "not canonical", partly disowned by Joseph; the entity-question list could inform 04 scope work later | — |
| §3: Gemini's one-page account; §7 `-src-act` "generative breadth" diagnosis; Opus-5 synthesis caution | Input to B.3 / owner review; adjacent | — |
| §3: human-experience budget; mood kernel; `_self` designs | ASIDE (low priority) / IN (mood landed as `#def-mood`, `#der-mood-timescale`) / ASIDE (engineering designs) | — |
| §4: ELI infrastructure | ASIDE (cohort history and engineering; superseded) except the negative cases, carried in the emergence item | — |
| §5: `agentic-tft/02` embeddings as gain readout | ADD | `a-candidate-route-to-e-2-one-part-i-quantity-est` (E.2) |
| §5: other predecessors, moved repos, `.textual-backup` | IN (migrated; `diff`-checked by the scout) / ASIDE | — |
| §6: scheduling-tech literature map | LEDGER: raised on `proposals-d-4-sp-12-commitment-resource-temporal-d-1dea` | — |
| §6: memory "Emergent Regime Framework" (Next Priority, 2026-03-01) | LEDGER: raised on `proprium-v2-holds-a-tft-era-memory-theory-canon` | — |
| §7: Cloos et al. (no-task agent; memory lesion) | ADD | `external-evidence-and-prior-art-canon-could-cite` (F.2) |
| §7: `regime-census` clones ("was the study written?") | Answered: yes, inside AISI-responses | `an-empirical-census-of-deployed-agent-frameworks` |
| §7: vaults, `~/tmp`, Downloads builds, Desktop | ASIDE (ancestral or snapshots) | — |

### Architectus's SYNTHESIS arc (added at the lead's request)

`~/src/.moved/autopax/docs/exp/`: `SYNTHESIS-PART1`–`PART5`, `THE-PATTERN.md`, `COUNCIL-PROPOSALS.md` (October 2025, about 6,200 lines). Cohort material: pointed at, not quoted. I read the headings of all seven files, plus PART1's anti-pattern section, PART2's category-error section, PATTERN's core principle, and PART3's pupation and quenched/annealed sections. I did not read PART4 or PART5 beyond their headings; both are zoetica engineering plans.

| Source item | Disposition | Item / where |
|---|---|---|
| Bungay's three gaps (knowledge, alignment, effects) | IN: `#def-unity-dimensions:90–98` maps them onto $U_M$, $U_O$, $U_\Sigma$; `#hyp-auftragstaktik-principle:47` carries Bungay's evidence | — |
| The three gaps applied to deployed LLM agents: more context, more detailed prompts and more controls widen the gaps | ADD as a candidate instance for `#hyp-auftragstaktik-principle` (discussion-grade; an ELI's argued reading) | raised on `how-much-must-be-said-explicitly-depends-on-the` |
| "Make the right thing the easiest thing" (constraint layer plus ease gradient) | ASIDE for ASF: a design principle; its revised copy is already influx at `firmatum/principles/influx/the-pattern.md`, its proper home | — |
| Herring school vs baboon troop, quenched vs annealed sessions, pupation, briefing and backbriefing, OKRs as a fractal graph | ASIDE: coordination practice and imagery with no derivation; lineage and pedagogy material. Briefing and backbriefing are Bungay's, already in canon by citation | — |
| PART4–5, COUNCIL-PROPOSALS: zoetica DSL, AXIOMATA persistence MVP, roadmap | ASIDE: engineering plans (October 2025), superseded | — |
| `#def-eli-cohort:96` Working Note cites the arc at a dead path and asks whether it belongs in ASF | LEDGER: raised on `canon-bodies-cite-local-working-paths`, with this answer | — |

### Helpers' surfaces

- **agent-core `memory/research/`** (the seven unread notes, ~490 KB): drained by `drain-influx-2-memory`; its file is `influx-2-memory-research.md`, read whole by me. Its items: `aat-has-no-event-segmentation-model-retirement-o` (G.2; scout A2, C5, P6), `the-mood-layer-and-the-adaptive-gain-carry-stand` (F.2; C2, C3, A4, `#def-mood`'s Behrens WN), `standard-names-canon-s-memory-machinery-lacks-fo` (F.1; C4, B8), `disc-structural-imagination-s-level-confusion-di` (G.2), `form-consolidation-dynamics-s-derivation-table-l` (C.1), question `does-schema-strategy-persistence-s-persistence-i`, and raises on be13, the scaffolding item, the record-read item, 6c13 and `def-strategy-dag-and-form-strategy-complexity-co`. Its lead finding: McClelland, McNaughton and O'Reilly 1995 eqs. 3–5 integrate in closed form to $D_h \le \varepsilon r_h S_{h0}/\ln((1-S_{c0})/(1-s^\ast))$, which is be13's missing $\varphi$ read one way and a drain floor that can replace the "Shannon floor" read the other, so be13 and the scaffolding item's part (3) should be integrated together. Coverage: four notes whole; one mostly whole; `dreams_nrem_rem` and `ai_agent_memory` by Takeaway/Inferences sections plus greps.
- **`firmatum-vivarium.md` plus vivarium `msc/`**: `drain-influx-2-firmatum`, file `influx-2-firmatum.md`. It stopped at the usage limit after committing L1–L5 and was resumed; *(its final state folded in below when it finishes)*.
- **AISI-responses `ASF-FIXES*` and sweep R34–R55**: `drain-influx-2-asffixes`, file `influx-2-asffixes.md`; resumed after the usage limit; *(folded in when it finishes)*.

## What was read whole, sampled, not reached

- **Read whole:** all nine regional files assigned to me; the memory helper's working file; the canon text at HEAD behind every DEFECT and IN row above (the line numbers in each item were re-read today, not taken from the scouts); `#der-compensation-channel-uniqueness` (Formal Expression through Working Notes); the context-saliency dossier §5.2; the regime-census table's first 24 rows (headlines).
- **Read in part, at the primary:** `#def-proprium-mapping`'s store list; `#def-chronica`'s TRACTUS Working Note; `#impl-strategy-dynamics` lines 42–44; `#der-causal-insufficiency-detection`'s scope and route tables; `#form-consolidation-dynamics` lines 20–24, 46, 54–57, 84, 92, 186, 195; `#def-mismatch-signal` 21, 65; `#form-composition-closure` 318; `#der-turnover-information-recursion` 70–82, 103; `#hyp-truth-serving-loophole` 15–55.
- **Relayed, not re-read at the primary:** most other source documents (the agent-core notes, the port-specs, PROPRIUM v2, the AISI skeletons, the periphery notes). Each item names its primary so an integrator reads it there; where an item rests on a single relay I say so in the item.
- **Not reached by me:** AISI-responses `influx/spikes/update-gain-icl/` (a direct question whether update gain has a referent for in-context learning; names only); the wrapping-certifiability and honest-activation distillation tables; `harness-velocity` beyond what the scouts read; the memorata transcript search Joseph's cross-surface instruction suggests (I grepped `items/`, canon Working Notes and the regional files instead).
- **Delegated:** see "Helpers' surfaces". The arch-program helper was refused by the concurrency cap; I did that region myself, at the depth above.

## Adjacent findings

- **agent-core is a private repository** (`gh repo view`: `v2-io/agent-core`, PRIVATE), while arch, where several of these items' sources live, is PUBLIC. This settles the scouts' open question about agent-core's visibility. The asf ledger is committed to a repo whose program parent is public, so items here cite agent-core paths and summarize its findings but carry no session-derived content. Its `msc/` commit (`27458ca`) came after a HANDOFF asked for Joseph's consent; with the repo private, that is less urgent, but it is still his to confirm.
- **Privacy calls I made:** two items (`joseph-believes-asf-already-shows-that-intellige`, `the-emergence-material-for-volume-4-has-the-nega`) first quoted lines that the scout had taken from Joseph's private `overarching` repo; I removed the quotes before committing and left pointers. The context-saliency 2026-10-27 notes are mode 600 and uncommitted; items cite them as "ask before quoting".
- **MAP D9 went to the lead at once** (a false "the loop is the only escape" on `FINDINGS.md` and `CURRENT-VOL1.md`); the lead routed it to the Part I round-3 lane. The same Brief makes four more "only escape" claims nobody has checked.
- **Several scout verdicts were overtaken today, both ways.** AXIOMATA's "frozen terminal values" (MAP proprium A1) was fixed by the Volume 4 lane; the substrate-independence "stub" claim was fixed; the hard-ceiling convention spike is moot (F72 deleted the ceiling). But the CHRONICA question got *sharper*: today's mapping says CHRONICA keeps "events judged meaningful", which makes it a selection, not $\mathcal C_t$.
- **The global `~/.claude/CLAUDE.md` project map still lists `~/src/firmatum/`** as a live project; it moved to `~/src/arch/proprium/INGEST/old-firmatum/` and `~/src/arch/firmatum/` is now the tooling belt. Not asf's file; noted for whoever maintains the global map.
- **Duplicate-risk observation:** the ledger now holds several items that are one cluster seen from different drains (read-the-record; compaction and identity; consolidation's two bounds and the "Shannon floor"). I cross-cited them in each item; an integrator taking any one should open the others named in it.
- **On the brief:** it worked. The one place it could have saved time is the same as the memory helper's: knowing the regional files would be overtaken by today's landings, I re-read every defect site anyway, which is where three of my dispositions changed.
