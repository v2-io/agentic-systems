# Theory-content-lifecycle — findings (2026-07-07)

*Cluster 01 of the meta-process review. Scope: segment promotion stages, the meta-segment pattern, OUTLINE hygiene/staleness, and especially the Working-Notes deluge. All counts verified firsthand against the working tree at commit `7c65b66` unless noted. Math in this file is LaTeX-delimited per project convention.*

## Corpus baseline (verified)

- **235 real segments** (`*/src/*.md` minus `old-*`): 01-aat-core 163, 02-tst-core 29, 03-llm-core 21, 04-eli-core 22. (A raw `ls */src/*.md` returns 279; the extra 44 are `old-*` staging files, almost all in TST.)
- **Stage distribution** (from frontmatter): `draft` 174, `deps-verified` 23, `claims-verified` 18, `format-clean` **0**, `candidate` **0**. Twenty segments carry **no `stage:` field at all** — all in 02-tst-core (only 9/29 TST segments are staged).
- **Status/tier distribution**: `conditional` 75, `discussion-grade` 64, `exact` 27, `axiomatic` 27, `robust-qualitative` 23, `sketch` 12, `empirical` 6, `heuristic` 1. This is consistent with the stated culture ("canon carries weak stuff, properly marked"): ~77 segments at solid tiers, the majority honestly-weak.
- **48 segments** carry a `## Findings` section (where the Brief lives).

---

## (a) De-facto processes actually running

**Gold-lift-into-WN (waves 1-4, then stopped).** The de-facto process that most shaped the current WN state. Cross-audit "wandering thoughts" harvested from `audits/AUDIT-WORKING-*/` were lifted per-segment into Working Notes under an `### Incidental audit gold` block. **122 AAT segments** carry such a block; **0** in TST/logogenic/logozoetic. These blocks are **67% of AAT's total WN word volume (101,267 of 151,580 words).** Method + tracker: `audits/.gem-hunt-trail/gold-lift-sweep-2026-05-30.md`; template pilot `result-persistence-condition` (commit `7594391`).

**Native Working-Notes authoring.** Segments accrete forward-pointers, open questions, resolved-item records, and prior-art fit-check candidates as normal development residue. This runs continuously and is healthy in form where it stays within the discipline (see TST `def-feature.md` — three clean forward-pointers, no gold-lift). It is unbounded in practice because nothing consumes it (see (d)).

**Meta-segment placement (M1-M4 + certificate spine).** The four `disc-*` meta-segments and the certificate spine are placed at Part II / Part III openings per the *introduced-before-used* discipline, depending on downstream content by design. This is de-facto and stable — but it collides with tooling (see (d), lint-outline).

**Back-integration landings.** Recent lifecycle activity is dominated not by promotion but by *new content landing* from sibling work (deaths-grounding from Inquiry Paper 4, `#def-mood`, mood-timescale, multi-timescale stability promoted `sketch`→`derived` in `de56b9a`). The live lifecycle is "author + land," not "promote through gates."

## (b) Aspirational processes the docs/SOPs intend

**The 5-stage promotion ladder** (`format.sop.md` §Promotion Workflow): `draft → deps-verified → claims-verified → format-clean → candidate`, each gated (Gate 1 dependency audit, Gate 2 content review, Gate 3 mechanical review, Gate 4 notes disposition). **Aspirational — barely running.** 174/215 staged segments sit at `draft`; the ladder has never produced a single `format-clean` or `candidate` segment. Gates 3 and 4 have effectively never fired corpus-wide.

**Working-Note discipline** (`format.sop.md` §"What earns a Working Note", single-sourced 2026-06-02, commit `f4258a0`): a WN earns its place *only* as forward-pointer / regression-guard / dead-end warning; no vanity-changelog, no unneeded spike refs. **Landed as doctrine, unenforced in tooling.** There is no linter for it. 95.3% of real segments (224/235) carry a WN section; grep signals 77 segments with vanity-changelog language (118 hits) and 47 segments pinning a live `spikes/spike-*` path in-file (the archivability-test tripwire named in `spikes.sop.md` §2-bis).

**Gate-4 notes disposition** as the WN drain: at `candidate`, every WN item must be resolved/deferred/promoted and the section emptied. **Never invoked** (0 candidate segments). This is the structural reason WNs only grow.

**OUTLINE as canonical ordering + accurate stage index** (`format.sop.md` §File Organization): each component's `OUTLINE.md` is the ordering source of truth and carries a per-row stage column. **Aspirational — the stage column is hand-maintained and unvalidated** (see (d)).

## (c) Emergent patterns from git history

- **The gold-lift sweep is abandoned mid-motion.** Tracker last touched **2026-05-31** (`74f096c`); no gold-lift commit since. Its own "Next — wave 5" section (A18-A21 + TST T1-T2 + logogenic L1-L2 + logozoetic E1-E2 + end-of-sweep batched/paired-note reconciliation) is entirely undone, confirmed by 0 gold blocks outside AAT. Five-plus weeks stalled as of today.
- **A recurring "stale-navigator find + fix" motif.** NEXT-UP records the 2026-06-30 case (four `scope-*` segments marked `missing` in `03-llm-core/OUTLINE.md` that already existed at `draft`, plus two more rows). The fix was a **point-fix of the specific PRACTICA-named rows**, not a systemic OUTLINE-vs-frontmatter reconciliation — so the class recurs (see (d)).
- **Promotion energy routes around the ladder.** Commit history shows heavy "integrate spike / land segment / back-integrate paper" traffic and almost no "promote `draft`→`deps-verified`→…" traffic. The team's real cadence is landing-driven; the gated ladder is a documented ideal the work does not follow.
- **WN as an off-ramp queue for certified findings.** The gold-lift sweep surfaced *theory-correctness* findings (strengthen-first / overclaim) that were parked in per-segment WN "off-ramp blocks" pending Joseph's routing (`gold-lift-sweep-2026-05-30.md` progress log). Several are load-bearing (W₁-leakage-possibly-vacuous; the `#schema-strategy-persistence` hard-ceiling convention). This overloads WN with a second function it was never scoped for — a decision queue — with no queue semantics.

## (d) Stale / broken / abandoned (concrete)

1. **Promotion ladder stalled at `claims-verified`.** 0 segments at `format-clean` or `candidate`. Gate 4 (the WN drain) has never run. *This is the root cause of the deluge, not a symptom.*
2. **Gold-lift sweep abandoned 2026-05-31**, ~57% done by component (AAT only), with no onward promotion of the 122 landed gold blocks into Brief/Discussion (0 such commits since). The harvest is a dead-end pool.
3. **OUTLINE stage-marker staleness, recurring and unremediated in 04-eli-core.** Verified stale (marked `missing` in the OUTLINE status column, but file exists at `stage: draft`, 84-98 lines of substantive content each): `scope-eli` (row 48), `def-five-constitutive-factors` (50), `def-eli-cohort` (51), `scope-emergence-conditions` (119), `scope-witness-bidirectional` (120), `obs-growth-vs-drift` (124). Plus `scope-observation-ambiguity-modulation` in `03-llm-core`. (Genuinely-missing and correctly-marked: `der-substrate-independent-persistence`, `def-character-aspiration-dialectic`, `form-congruency-selfhood`.) The 2026-06-30 fix did not cover these.
4. **No tooling checks OUTLINE-stage vs frontmatter-stage.** `bin/lint-outline` reads `stage:` from frontmatter for *ordering* checks but never compares it to the OUTLINE table's hand-authored status column — which is exactly why #3 persists silently.
5. **20 TST segments have no `stage:` field.** They are outside the staging system entirely; TST is markedly under-processed (no gold-lift, `old-*` files still present, 9/29 staged).
6. **`bin/lint-outline` signal degradation.** It reports **17 "ordering violations,"** but all 17 are the M1-M4 meta-segments and their kin (`disc-identifiability-floor`, `disc-separability-pattern`, `disc-additive-coordinate-forcing`, `disc-modularity-state-dynamics`, `disc-strategic-self-coupling`, `disc-implementation-impossibility`, `disc-value-functional-grounding-floor`) placed at section openings *by design*. The tool's headline count is ~100% expected-noise an agent must know to discount. (Its 65 "backmatter references" *are* correctly separated as intentional — the ordering check is not.)
7. **Vanity-changelog / diff-voice residue in WN despite the June discipline.** 180 segments carry date-stamps in WN (591 total date refs); `form-composition-closure` alone carries dated "Resolved (2026-04-22)" / "Resolved (2026-05-19)" notes with explicit "*History (not present truth)*" markers — content the discipline says belongs in CHANGELOG, not the segment.

## (e) Decisions genuinely blocked on Joseph

- **Is promotion-to-candidate a live process, or is `draft`+honest-tier the terminus for now?** The ladder's total stall may be a deliberate priority call (land breadth, defer polish) rather than a failure — but it is undocumented as such, and it is what makes the WN deluge structural. Joseph's call determines whether the fix is "run Gates 3-4" or "stop pretending the ladder is live and drain WN another way."
- **Gold-lift sweep: resume, or retire-in-place?** Five weeks stalled. If retire, the 122 AAT gold blocks and the un-swept TST/03/04 audit dirs need an explicit disposition. Open sub-decisions already flagged in NEXT-UP and awaiting him: the **Brief-as-section FORMAT move** (a Brief between title and Formal Expression, absorbing today's `Findings#brief`) — this is the natural home the parked gold would graduate into; batch-file dir split-vs-leave; the `184930` predictions-only gold doc (whole-framework framing, no per-segment anchor — flagged JOSEPH-DECISION in the tracker).
- **Routing of the WN off-ramp certified-findings** (strengthen-first queue vs spike) — partly landed into `TODO.md` (`e47afff`), but the reserved adjudications (W₁-leakage, schema-ceiling convention) still sit awaiting his gate per the tracker.

## (f) Candidate meta-process definitions

| # | Process | Trigger | Steps | Current health |
|---|---------|---------|-------|----------------|
| P1 | **Segment promotion (draft→candidate)** | A segment's deps are all at ≥ its target stage (topological readiness) | Gate 1 dep-audit → Gate 2 content review → Gate 3 mechanical/lint → Gate 4 notes disposition (empty WN) | **Broken/aspirational.** Tops out at `claims-verified`; Gates 3-4 never run corpus-wide; the designed WN drain is dormant. |
| P2 | **Working-Note discipline** | Any WN edit | Admit only forward-pointer / regression-guard / dead-end; exclude vanity-changelog + unneeded spike refs | **Aspirational/unenforced.** Doctrine landed 2026-06-02; no lint gate; 95% of segments carry WN; vanity + spike-pin residue persists. |
| P3 | **Gold-lift harvest → WN → Brief** | De-novo audit produces incidental "wandering-thoughts" gold | Lift per-segment into `### Incidental audit gold` → (later) promote into Brief/Discussion → file source-note to `.integrated/` | **Abandoned mid-sweep** (stopped 2026-05-31, AAT-only). Onward Brief-promotion leg **never started** (0 commits). Output is a 101K-word parked pool. |
| P4 | **OUTLINE hygiene (stage-marker accuracy + ordering)** | Segment authored / stage changes | Update OUTLINE row status; keep ordering topological | **Stale/recurring.** Confirmed stale rows in 04-eli (6) + 03 (1); point-fixed 2026-06-30, class recurred; no tooling check of status column. |
| P5 | **Meta-segment placement (M1-M4, certificate spine)** | A cross-cutting pattern earns introduced-before-used placement | Place at section opening; depend on downstream; cross-ref F1-F4 instances | **De-facto healthy as design; emergent tension** with lint-outline's ordering check (P4 tooling flags it as 17 violations). |
| P6 | **Stage-field maintenance** | Segment created | Add `stage:` frontmatter; keep in sync with OUTLINE | **Mixed/broken in TST.** 20 TST segments unstaged; 44 `old-*` files unconverted. |

## Out-of-scope surfacings (passed back)

- **WN has silently become a decision queue** for certified strengthen-first findings (W₁-leakage-vacuity, schema-ceiling convention, etc.) with no queue semantics and no owner. This is really cluster-02 (audit/spike) and cluster-07 (decision-routing) material, but it originates as WN content and inflates the deluge. Load-bearing theory-correctness items are parked where nothing watches them.
- **TST is the neglected component**: unstaged, un-gold-lifted, `old-*`-laden. Any "theory frontier" narrative that treats the four components as evenly maintained is wrong; 02-tst-core is roughly a stage behind.
- **`agents.sop.md` still carries the "under active reconsideration (2026-05-19→20)" banner** and points to `INTEGRATION-CLEANUP-TODO.md`; several G2/G3/D-2 items in that file are the connective tissue behind the P3/P4 stalls.
- **NEXT-UP.md is itself stale as a drain-signal**: it says "Delete once the queue drains" but still carries the 2026-06-30 gold-lift/audit-two-track threads as "active/hot" that git shows dormant since 2026-05-31. It is doing history-narration, not hot-pointer, duty.
