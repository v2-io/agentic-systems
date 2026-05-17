# Cluster E Adjudication — pre-ledger old + 451729 + lineage doc

**Adjudicator:** fan-out agent (Cluster E), 2026-05-16
**Frame:** `msc/audit-backlog-triage-2026-05-15.md` spine + MANIFEST evidence
hierarchy + `audits/polish-and-sentiment-ledger.md` + `CLAUDE.md`.
**Constraint:** report-only. No moves/edits/commits/segment-changes. Parent +
Joseph own all routing/graduation.

---

## TL;DR — recommended file-level dispositions

| File | Vintage | Recommended disposition | Graduation blocker? |
|---|---|---|---|
| `2026-03-13-feedback.md` | ACT-era (pre-AAD) | **subsumed-by-later-work** → `.integrated` | none |
| `2026-03-14-fresh-eyes-assessment.md` | ACT-era | **subsumed + retain-as-history** → `.integrated` | none |
| `feedback-2026-03.md` | ACT-era (TFT/TST merge) | **subsumed-by-later-work** → `.integrated` | none |
| `opus-analysis-2026-03-09.md` | TFT-era | **subsumed-by-later-work** → `.integrated` | none |
| `analysis-2026-04-01.md` | early-AAD | **subsumed** (own follow-on supersedes) → `.integrated` | none |
| `analysis-2026-04-01-remaining.md` | early-AAD | **subsumed** by 04-02-comprehensive → `.integrated` | none |
| `analysis-2026-04-02-comprehensive.md` | early-AAD | **subsumed/resolved** (self-consolidating; spot-verified) → `.integrated` | none |
| `analysis-2026-04-02-round2.md` | early-AAD | **subsumed** by comprehensive → `.integrated` | none |
| `analysis-2026-04-02-synthesis.md` | early-AAD | **subsumed/resolved** (Tier-0/1 landed) → `.integrated` | none |
| `analysis-2026-04-06.md` | mid-AAD | **resolved/subsumed** (C1–C11 spot-verified) → `.integrated` | none |
| `extracted-claude-feedback-2026-04-02-deep-reviews.md` | ACT-era | **retain-as-history** (lineage of the 04-02 consolidated docs) → `.integrated` | none |
| `extracted-claude-session-…-audit-instructions-lineage.md` | 2026-04-24 | **retain-as-history** (provenance; doubly subsumed) → `.integrated` | none |
| `audit-451729-FINAL-2026-05-10.md` | recent | **mostly-resolved; ONE residual** (D.1) → stays **open**, backlink live in TODO §2026-05-10 | **D.1 only** |

**Net:** 12 of 13 files in Cluster E are graduate-ready (subsumed /
resolved / retain-as-history). Only `audit-451729-FINAL` stays open, and its
single residual (D.1) is already first-class-tracked in `TODO.md`
§2026-05-10 — so it is *routed*, not homeless; it stays open only because
D.1 needs Joseph's sweep/surface judgment, exactly as the brief anticipated.

The dominant disposition in this cluster is **subsumed-by-later-work**, not
`correctly-rejected`. That is the expected shape: per the spine,
strengthen-before-soften `correctly-rejected` "concentrates in the math-heavy
ledgered cycles … *not* in hygiene/process/soft-feedback slices." Cluster E is
old broad-review prose, not adversarial math-finding cycles. There is one
genuine strengthen-not-soften instance (see §"Strengthen-before-soften
watch"), and it discharged in the project's preferred direction.

---

## Method and evidence basis

These files (except the last two) predate the `pending-findings` ledger
discipline; per the evidence hierarchy, disposition rests on **first-hand
re-read against current `src/` + the corpus-redundancy safety net**. I read
all 13 files in full. `git`-recency is poisoned (2026-05-15 rename sweep) and
was not used.

The decisive structural fact: **every one of these files is a broad
whole-theory review from a structural era the repository has since moved
through.** They use vocabulary the project has explicitly retired:

- "AAD"/"ACT"/"TFT" framework names (now AAT; rename lineage in CLAUDE.md).
- **"Section I / II / III / IV / V"** monolithic-section structure. Current
  `src/` is slug-addressed claim segments with `OUTLINE.md` ordering; there
  is no "Section V" and "Section IV = TST" is now `02-tst-core/`.
- Numeric segment ids (`#260`, `#310`, `#530`, TF-01, T-08) — the pre-slug
  identity scheme.
- Segment counts of 68 / 74 / 85 / 89-at-draft / "0 past draft". Current
  `01-aat-core/src/` alone is **138 segments**, `02-tst-core/` 72,
  `03-llm-core/` 20, `04-eli-core/` 18, with a four-gate promotion workflow
  in steady use.

This alone does not retire a finding (a real defect can outlive a rename).
The spine is explicit that "valid in the first place" and "valid as of
today" are separate questions. So I traced the *substantive* recurring
findings — the ones that recur across the whole March–April corpus and would
be the load-bearing reasons to keep any of these open — to current `src/`.

### Corpus-redundancy verification (first-hand `src/` spot-checks)

Every high-weight recurring finding in this cluster is **resolved in current
`src/`**, generally by the *strengthening* discharge direction the project
prefers (a constructive segment family, not a softening caveat):

| Recurring finding (where it appears in Cluster E) | Current `src/` state | Disposition |
|---|---|---|
| Directed separation blocks the main application class / κ-as-scalar category error / LLMs excluded by construction (3-13 #1, 3-14, 4-01 detailed analysis, deep-reviews §all, lineage A2) | `der-directed-separation.md` + `der-class-coercion-via-wrapping.md` + `der-class-coercion-in-composition.md` + `hyp-directed-separation-under-composition.md`; GUC Class system (CLAUDE.md §5). The category error was *accepted and built on* (architectural classification + constructive wrapping), not softened. | resolved by strengthening |
| Persistence claim stronger than proof / α vs 𝒯 substitution / structural-vs-operational conflation (3-13 #2, 3-14, 4-02-synthesis Tier-1a flagship, opus-3-09) | `result-persistence-condition.md` + 6 sibling persistence segments carry the **structural / task-adequacy / operational** two-condition decomposition explicitly. 451729 §E independently re-verified this two-condition split by hand. | resolved by strengthening |
| Composition foundational before bridge theorem / bridge-lemma contraction gap / projection admissibility undefined (3-13 #3, 3-14, 4-01 Spike 3, 4-02 3a, deep-reviews #3, lineage A?) | `form-composition-closure.md` + `result-contraction-template.md` + `der-tempo-composition.md`. P_adm defined; contraction made a checkable conditional. | resolved (conditional, honestly scoped) |
| Graph uniqueness not theorem-strength / P3→Markov sketch / acyclicity should stand alone (3-13 #4, opus-3-09, 4-01, deep-reviews #4) | `deriv-graph-structure-uniqueness.md`: acyclicity derived from temporal ordering (exact); Markov conditional-on-causal-sufficiency, honestly labeled. Matches what every reviewer said the honest end-state should be. | resolved |
| Section IV overstates git's causal status / `#hyp-causal-discovery-from-git` missing (3-13 #5, 3-14, 4-06 A4) | `02-tst-core/src/hyp-causal-discovery-from-git.md` now exists (the named missing segment was written). | resolved |
| `03-llm-core` empty / 7 logogenic segments unwritten / 4 TST segments missing (4-06 A3/A4) | `03-llm-core/src/` = 20 segments; `02-tst-core/src/` = 72. The "largest gap between available theory and published segments" is closed. | resolved |
| Information-bottleneck orphaned (4-02 L6, 4-02-r2 #9, deep-reviews 2f17ecbd) | IB consumed by `deriv-causal-ib-lmi.md`, `deriv-causal-ib-exploration.md`, `def-causal-information-yield.md`, `def-model-sufficiency.md`. Not orphaned. | resolved |
| Three-way exploit/explore/deliberate — "the only Section II --GAP--" (4-02 H1, deep-reviews rec 6) | `disc-exploit-explore-deliberate.md` exists as a landed segment, alongside `der-deliberation-cost.md`. | resolved |
| Codex C1–C6 narrative "caveat arrives one beat too late" + N1–N6 fixes (4-06, the bulk of that file) | Spot-checked downstream: the two-condition persistence split, the convention hierarchy, the L0/L1 default, and the GUC class language are all now front-loaded in current segments (451729 §E independently confirms "epistemic discipline consistency" and "GUC class rename propagation … no instance of the old naming"). The 4-06 "discussion outruns formal status" pattern is exactly the recurring family later cycles (471203 §B, 451729 rescinded-4, the math-heavy ledgered slices) continued to police. | resolved / subsumed by the ongoing discipline |

The few items that are *still* genuinely open are not unique to these files
and are already first-class elsewhere:

- **External validation against real-world data** (recurring MEDIUM in
  3-13, 4-01, 4-01-rem, 4-02-*; "internal validation only"). This is a
  standing **known fragility / research program**, not a defect. It is the
  project's acknowledged scope boundary (empirical program deferred), and
  it recurs in every later audit too — i.e., tracked by redundancy, not
  homeless. Disposition: `subsumed-by-later-work` (the standing
  empirical-program scope statement); not a graduation blocker for these
  files. *Surfaced for the parent:* if the parent wants a single durable
  home for "AAT has no external real-world validation yet," the
  polish-and-sentiment ledger `research-seed` band or a Known-Fragilities
  line is the natural place — but it is already a declared fragility, so
  this is optional tidying, not a gap.
- **AND/OR parsimony theorem** (4-01-rem, 4-02 "convergent choices"):
  raised as a *would-promote-from-convergent-to-derived* aspiration, never
  as a defect. `deriv-graph-structure-uniqueness.md` + `scope-and-or.md`
  carry the convergent-choice framing honestly. This is a
  `research-seed`-grade aspiration at most, and it recurs in later
  CLAUDE.md "Convergent Choices" framing — not a Cluster-E-unique open
  item.

---

## Per-file adjudication

### `2026-03-13-feedback.md` — **subsumed-by-later-work**

Three-model (Opus/Codex/Gemini) consolidated external review of "AAD".
11 ranked issues + presentation recs (three-tier split, Greek terminology,
MDL-for-strategy, adversarial-aporia spike) + 6 press-next questions.

Every ranked issue (directed separation #1, persistence-stronger-than-proof
#2, composition-before-bridge #3, graph-uniqueness #4, git-causal #5, …,
δ_critical/R-as-inputs #11) recurs in the April files and is resolved in
current `src/` per the table above. The presentation recs are subsumed: the
three-tier "core/conditional/empirical" split became the FORMAT.md
three-rings-of-rigor organizing principle (the lineage doc P6 names this
explicitly); Greek terminology survives as LEXICON cycle-phase terms; the
adversarial-aporia idea matured into the adversarial-coupling / red-team
material. **Subsumer:** the entire April consolidation chain + the FORMAT.md
three-rings structure + current `src/`. No unique surviving signal.
Soft/sentiment: the "What all three reviews agree is strong" section is
positive calibration signal but it is **verbatim-duplicated** (richer) in
the 04-02 deep-reviews and 04-06 — not worth a separate ledger row;
attribute to the later, fuller source if the parent wants it. Recommend
`.integrated` (subsumed; per-finding-justified by the redundancy table).

### `2026-03-14-fresh-eyes-assessment.md` — **subsumed + retain-as-history**

Single-author (Opus 4.6) fresh-eyes assessment. Same substantive findings
(directed separation as *structural* vulnerability — the κ-as-scalar
category-error insight is first articulated cleanly here; composition
2-agent case; α/T fixed *in that session*; git overstatement). All
subsumed/resolved per the table.

Distinct value: this is where the **"κ as scalar is a category error;
directed separation is architectural not parametric"** framing is first
stated sharply (line 54). That insight is now a load-bearing project
commitment (CLAUDE.md §5, the GUC class system). The file is the
*archaeological origin* of a settled architectural decision — same
retain-as-history character the MANIFEST already affords origin documents.
Recommend `.integrated` with a "subsumed; retained for the κ-category-error
provenance" note.

### `feedback-2026-03.md` — **subsumed-by-later-work**

Perplexity-rendered three-model (GPT-5.4/Opus/Gemini) review from the
**TFT→TST-merge era** (refs PLANS.md, README.md, `tst-tft-combined.md` —
all pre-AAT artifacts that no longer exist in this structure). Content is
about *how to merge TST into TFT/AAD* — a structural question the project
resolved long ago (TST is now its own `02-tst-core/` grounded by AAT;
CLAUDE.md §1). Oldest-vintage, most-superseded file in the cluster. No
finding here is both unique and unaddressed. Recommend `.integrated`
(subsumed; the TST-as-`02-tst-core` restructure is the subsumer).

### `opus-analysis-2026-03-09.md` — **subsumed-by-later-work**

Conversational TFT-era review (TF-01/TF-02/TF-03/Appendix-A vocabulary;
"#260/#270/#280/#310" numeric ids; "Section IV has 25+ claims"). The two
substantive contributions — (a) Σ_t-should-be-labeled-a-formulation-like-TF-03
with downstream conditionality, and (b) "agents can modify their own
observation channels" as a possible general claim — are both subsumed:
(a) the current epistemic-tagging discipline + the `disc-*` meta-segments do
exactly this typing work corpus-wide; (b) became
`der-code-quality-as-observation-infrastructure` and the
observation-infrastructure thread (referenced from current AAT segments).
δ_strategic-as-second-order-inference recurs and is resolved via the
δ_s/δ_strategic separation (4-06 C4/O2, later cycles). Recommend
`.integrated` (subsumed).

### `analysis-2026-04-01.md` — **subsumed (own follow-on supersedes)**

Two-reviewer (Opus/Codex) review of 68 segments. **This file is explicitly
superseded by its own follow-on**: `analysis-2026-04-01-remaining.md` opens
"Revised from the original `analysis-2026-04-01.md` … completed items are
removed," and `analysis-2026-04-02-comprehensive.md` consolidates "all
still-relevant findings from" this file with resolved items struck. Spikes
1–4 + E1–E8 marked done in the follow-ons and verified landed in `src/`
(disturbance Model D/S split, projection admissibility, scalar-objective
analysis, CIY decomposition into `def-causal-information-yield` family).
Recommend `.integrated` (subsumed by its own documented follow-on chain).

### `analysis-2026-04-01-remaining.md` — **subsumed by 04-02-comprehensive**

The "what remains" revision of the above. Its "Completed This Session"
block is a clean resolution ledger; its "Still Open" items
(coupled-formulation, AND/OR parsimony, P3→Markov tightening, strategy-loop
remaining pieces, external validation) all recur in
`analysis-2026-04-02-comprehensive.md` §3 and the later ledgered cycles, and
the substantive ones are resolved in `src/` per the redundancy table
(`03-llm-core/` written; P3→Markov honestly conditional;
`disc-exploit-explore-deliberate` landed). Recommend `.integrated`
(subsumed; 04-02-comprehensive is the explicit consolidator).

### `analysis-2026-04-02-comprehensive.md` — **subsumed/resolved (self-consolidating)**

Self-described as the consolidation of 04-01, 04-01-remaining,
04-02-synthesis, 04-02-round2, with resolved items struck and NEW items
marked. §2 is a 20+-item verified-fixed ledger. §3 still-open items: H1
(three-way tradeoff) — **landed** (`disc-exploit-explore-deliberate.md`);
M1–M8/P1–P3/L1–L9 — spot-checked as resolved or subsumed by the ongoing
"discussion-outruns-formal-status" discipline that later cycles (4-06,
471203, 451729) continued to enforce. The §4 missing-segment table is
entirely closed (`03-llm-core/`, TST missing-4, the appendix gaps all
exist). This is the **richest single synthesis in the pre-ledger cluster**
and the natural per-finding-justification anchor for the redundancy table.
Recommend `.integrated` (subsumed/resolved; cite this file's §2/§3 as the
era's own resolution record, cross-checked against `src/`).

### `analysis-2026-04-02-round2.md` — **subsumed by comprehensive**

Round-2 Codex+Claude integration. Its new findings (gain→sector bridge as
softest joint; do(.) notation bug; stale composition blocker; scope-split;
forced-vs-motivated language; loop-interventional too strong; label fixes;
undefined ρ/δ_critical/g; orphaned IB; fluid-limit bound) are **all carried
into `analysis-2026-04-02-comprehensive.md`** (which names round2 as a
source) and resolved/subsumed there + in `src/` (gain-sector bridge is now
`der-gain-sector-bridge.md`, a landed segment 451729 §E re-verified by hand;
do(.) bug fixed; IB de-orphaned). The "Round 3 Integration" tail (N1–N5) is
likewise absorbed. Recommend `.integrated` (subsumed; comprehensive is the
named consolidator).

### `analysis-2026-04-02-synthesis.md` — **subsumed/resolved (Tier-0/1 landed)**

The recommended-path-forward synthesis (Tier 0 contradictions → Tier 4
positioning). Tier 0 (passive-observer, metadata, ordering,
loop-interventional self-contradiction) and Tier 1 (persistence
disambiguation = the flagship; tempo-redundancy caveat; continuation
convention; CIY-out-of-Section-I) are the load-bearing items — all landed
in `src/` (the structural/operational/task-adequacy split is the single
most-cited resolution, independently re-verified by 451729 §E; CIY is now
its own `def-*` family). Note: the deep-reviews extract documents that the
*published* synthesis here was a rewrite of session `9f89ae5d`'s original
synthesis — i.e., this file is itself a curated consolidation, not raw
findings. Recommend `.integrated` (subsumed/resolved).

### `analysis-2026-04-06.md` — **resolved/subsumed (C1–C11 spot-verified)**

Most recent of the pre-ledger analysis files; Codex C1–C11 + A1–A6 + N1–N6
narrative recommendations, "every claim verified against current segment
files" *as of 2026-04-06*. The C-items are the "the repo has the right
caveat but it arrives one beat too late" family. Spot-check against current
`src/`: 451729 §E (a *much later* independent de-novo pass) explicitly
certifies "epistemic discipline consistency … consistent labeling
throughout" and "GUC class rename propagation … no instance of the old
naming was observed" — i.e., the C1–C6 "caveat one beat late" pattern is the
exact discipline that later cycles confirm is now being held. A1/A2
(stale OUTLINE/WORKBENCH) are obsolete (WORKBENCH retired 2026-04-22 per
project memory; OUTLINE is regenerated). A3/A4 (missing logogenic/TST
segments) resolved. A6 explicitly self-classifies as "not a gap — an honest
scope boundary." The "discussion outruns formal status" pattern (C11/O1) is
a *standing* discipline the project continuously polices, not a closeable
defect — its continued enforcement in 471203/451729/the math-heavy ledgered
slices *is* the subsumer. Recommend `.integrated` (resolved/subsumed; the
ongoing epistemic-discipline enforcement + 451729's independent
re-certification is the per-finding justification).

### `extracted-claude-feedback-2026-04-02-deep-reviews.md` — **retain-as-history**

Self-describing lineage document: a consolidation of **7 ACT-era deep
reviews** (sessions 14c96d33, 9f89ae5d×2, d5e7172a, 2f17ecbd, b40b551e,
e39166b4) run within a 24h window, that **fed** `analysis-2026-04-02-
comprehensive.md` and `-synthesis.md` (its own front matter, lines 8–28,
states this and what it does *not* preserve). It carries no `## Disposition`
section, but every session block has a `**Disposition.**` line recording
what Joseph did with that review at the time ("This is excellent work" /
launched Easy-Tasks sub-agents / seeded FORMAT.md Gates 1–4 / "well-calibrated
review"). Its findings are *definitionally* subsumed by the two consolidated
docs I adjudicated above. Its distinct, durable value is **provenance**: it
preserves the unique-to-session framings the consolidated docs dropped —
d5e7172a's "three concentric rings of rigor" (→ FORMAT.md three-rings),
2f17ecbd's "67 at draft, 0 past draft" (→ the FORMAT.md Gate 1–4 promotion
workflow), b40b551e's credit-assignment back-and-forth. This is exactly the
retain-as-history class: not finding-by-finding, the audit trail of how the
de-novo discipline and the promotion workflow were born. Recommend
`.integrated` (retain-as-history; findings subsumed by the 04-02 consolidated
docs, provenance preserved).

### `extracted-claude-session-…-audit-instructions-lineage.md` — **retain-as-history (doubly subsumed)**

Per the brief: judged as retain-or-integrate-as-history, not
finding-by-finding. It is the **raw reasoning-trail transcript of the
2026-04-24 session** in which (a) a delegated-to-sub-agents audit was
criticized by Joseph, (b) the auditor re-read first-hand and retracted the
prior passes, and (c) the meta-reflection produced
**`doc/de-novo-audit-instructions.md`** (verified present, 104KB, live).
It embeds a full Phase-1/2/3 audit (Tier-A A1–A7, Tier-B B1–B6, Tier-C
C1–C3, P1–P8 pondering) — but that embedded audit is the *retracted /
session-internal* form whose surviving, kept output is
`audits/audit-2026-04-24-fresh-pass.md` (whose Process Note explicitly
states "Earlier deliverables in this session are retracted in their
entirety"), itself ledgered in `audits/pending-findings-2026-04-25.md`
(Cluster C's slice — not mine to re-adjudicate; flagged for the parent so
the two are not double-tracked). So this file is **doubly subsumed**:
findings → the ledgered 2026-04-24-fresh-pass; methodology →
`doc/de-novo-audit-instructions.md` (landed, live). Its irreplaceable value
is the human↔Claude reckoning arc (the pushback→recovery→instructions-
authorship), which is pure provenance. Recommend `.integrated`
(retain-as-history; provenance of the de-novo-audit discipline; findings
already ledgered under 2026-04-25, methodology already landed).

> **Surfaced for the parent (de-dup):** the embedded Tier-A findings here
> (A1 scalar-tempo overcount, A2 Class-1/2/3-discrete-but-used-continuous,
> A3 loop-interventional overstates, A5 unity-dimensions incomplete, A6
> regret-bound silent-deterministic-π*, etc.) are the *same* findings
> Cluster C will adjudicate via `audit-2026-04-24-fresh-pass` +
> `pending-findings-2026-04-25`. Do **not** re-track them from this file;
> defer to Cluster C's disposition. This file's role is provenance only.

### `audit-451729-FINAL-2026-05-10.md` — **mostly-resolved; ONE residual (D.1) → stays open**

Recent (Group R), partially-tracked. Confirmed first-hand:

- **§B Finding 1 (Prop B.4 optimal-exploration-rate subscript transposition,
  `deriv-edge-credence-dynamics`):** `resolved` by **direct fix**, verified
  in current `src/` — `deriv-edge-credence-dynamics.md:220` now reads
  `$\varepsilon^\ast = \frac{n_2+1}{n_1+n_2+2}$` (the correct form; the
  auditor's derivation). `CHANGELOG.md:210` records the intake explicitly,
  including the B.6 inherited-transposition audit and "no downstream by-form
  citations." Not a graduation blocker.
- **§B.1 Rescinded 1–5:** auditor's own correctly-closed candidates
  (adversarial exponents re-verified ✓; scope-agency `do(a)` forward-ref;
  post-composition-consistency dep; objective-functional axiomatic-with-
  commitment; draft-stage maturity). These are `correctly-rejected`-by-the-
  auditor-itself — no action; the rescindment *is* the disposition.
- **§D.1 Hypothesis (promotion-readiness sweep on conservatively-staged
  appendix segments — `deriv-recursive-update`, `deriv-sector-condition`,
  `der-gain-sector-bridge`, `deriv-edge-credence-dynamics`,
  `deriv-graph-structure-uniqueness`, `form-strategy-complexity-cost`,
  `schema-strategy-persistence`, `form-consolidation-dynamics`):** the one
  carried-forward open item. **Already first-class in `TODO.md`
  §"2026-05-10 — Audit-findings intake: 451729 — remaining open item"** as
  an open `- [ ]` D.1 entry with the exact segment list and "Needs Joseph's
  judgment on whether to sweep or to surface case-by-case." This is
  `actionable-open` and correctly *routed* (live backlink to the audit
  report). It is the **sole** thing keeping 451729 open — confirmed: §D.2
  (`result-unity-closure-mapping` joint f₁/g sketch) and §D.3
  (`schema-strategy-persistence` α_Σ≈1−λ approximation) are *hypothesis-tier
  observations*, not burden-of-proof findings; §F.1–F.4 are bigger-picture
  hypotheses (pedagogical-prioritization / Correlation-Hierarchy-as-teaching
  / consolidation-window-upper-bound-open / meta-segments-unread). Of these,
  the only ones with durable-signal character are soft:

| 451729 item | Band | Recommended ledger routing |
|---|---|---|
| §D.3 — `schema-strategy-persistence` uses $\alpha_\Sigma\approx1-\lambda$ without noting the exact $(1-\lambda)/(2-\lambda)$ form (≈33% error at λ≈0.5); "may be worth noting in Epistemic Status" | polish | ledger `polish` (small precision nudge; high-confidence isolated — parent may prefer a direct micro-fix) |
| §F.1 — README/OUTLINE preambles could give the practically-actionable diagnostics (two-condition persistence, 2×2, forgetting prerequisite, adversarial squared law) equal billing with the integration/synthesis framing | sentiment/research-seed | ledger `sentiment` (calibration) — note it rhymes with ledger **S2** (findings-schema approachability) and with the respectful-pedagogy direction in CLAUDE.md; not a defect |
| §F.2 — Correlation Hierarchy (L0/L1/L1′/L2) underutilized as a pedagogical tool; a standalone exposition would raise accessibility | research-seed | ledger `research-seed` (pedagogical-exposition seed; graduates to PROPOSALS only if a concrete standalone-section move is taken) |
| §F.3 — `form-consolidation-dynamics` stability-plasticity *upper* bound is open (only half the feasibility window is derived) | research-seed | ledger `research-seed` — this is a genuine open-theory direction, honestly self-labeled in-segment; recurs as a known half-open window. Worth a durable row so it is not silently re-dropped |
| §D.2 — `result-unity-closure-mapping` joint $(U_O,U_\Sigma)\to\varepsilon_a$ f₁/g "mechanical extensions not fully computed" | research-seed (weak) | ledger `research-seed` or leave as honest in-segment scope note; lowest-weight |

  **Disposition for 451729:** stays **open** in the backlog, blocker = D.1
  only (already routed to TODO §2026-05-10 — *routed, not yet fully
  integrated*, exactly the Group-R characterization in the spine). The soft
  items above (D.3 polish, F.1 sentiment, F.2/F.3/D.2 research-seed) should
  be **mirrored to `audits/polish-and-sentiment-ledger.md`** so that when
  D.1 is dispositioned, 451729 can be retired as *fully accounted for* with
  nothing lost. None of these is a defect; none asks for a softening the
  theory was strengthened against.

---

## Strengthen-before-soften watch

Per the spine, I checked specifically for findings asking us to *weaken* a
claim the theory was instead *strengthened* to defend (which would be
`correctly-rejected`, not open). Cluster E is old broad-review prose, so the
shape is mostly **subsumed-by-strengthening** rather than
**rejected-because-strengthened**, but the discharge direction is the
project's preferred one throughout:

- **Directed separation / κ-as-scalar (3-13 #1, 3-14):** the soft move
  would have been "scope AAD down to goal-blind agents / admit it's not a
  universal theory" (Codex literally posed this as the choice, 3-13 Q2).
  The project did the *hard* thing instead: kept the ambition, turned the
  apparent defect into the architectural GUC-class classification, and built
  the constructive `der-class-coercion-via-wrapping` so Class-3 agents get
  Class-1 status by construction. This is the canonical strengthen-not-
  soften pattern, played out at theory scale. A naïve reader of 3-13/3-14
  would log "scope it down" as an open finding; it is **correctly closed by
  strengthening** and must not be reopened.
- **Persistence stronger-than-proof (3-13 #2):** soft move = "state it in
  α only, drop the 𝒯 form." Project instead derived the
  structural/operational/task-adequacy decomposition (a *stronger,
  fully-typed* result), independently re-verified by 451729 §E. Closed by
  strengthening.
- **Graph uniqueness / P3→Markov (3-13 #4):** the honest end-state every
  reviewer asked for *was* the discharge — acyclicity promoted to a
  stand-alone exact derivation, Markov honestly conditional. Not a
  softening; a precise scoping that strengthened the stand-alone result.

No Cluster E finding is being held open on a soften-recommendation the
theory has out-strengthened. The one place to be careful is **not** to let
the old "scope AAD down / it's not universal" framing (3-13, 3-14,
deep-reviews) re-enter the backlog as an open item — it is the textbook
correctly-rejected-because-strengthened case.

---

## Things that don't fit the frame (surfaced per brief)

1. **The lineage doc embeds a real audit that belongs to Cluster C.**
   `extracted-claude-session-…-lineage` is filed as "provenance, not
   findings" — correct as the *file's role*, but it physically contains a
   full Tier-A/B/C audit whose findings are the 2026-04-24-fresh-pass
   findings Cluster C will adjudicate via `pending-findings-2026-04-25`.
   Flagged above so the parent does not let the same findings get tracked
   from two clusters. Cross-cluster de-dup is a parent-level concern the
   per-slice fan-out can't fully resolve from inside one slice.

2. **`analysis-2026-04-02-synthesis.md` is a rewrite of a session
   synthesis.** The deep-reviews extract (session 9f89ae5d block) documents
   that the *published* synthesis file was rewritten with different prose
   from the session-original. Both are in the corpus (synthesis file in my
   slice; session-original inside the deep-reviews extract). They are *not*
   duplicates in the `diff`-them sense — the published one is curated, the
   embedded one is raw — but they are the same analytical content. Routing
   both to `.integrated` is correct; just noting they are a known
   curated/raw pair, not independent signal.

3. **Pre-ledger files are individually subsumed but collectively are the
   April-consolidation chain.** 04-01 → 04-01-remaining →
   04-02-{synthesis,round2} → 04-02-comprehensive is a single nested
   revision lineage where each later file explicitly supersedes the
   earlier. The cleanest MANIFEST treatment is probably **one grouped
   entry** ("the 2026-03/04 broad-review consolidation chain") with the
   redundancy table as the shared per-finding justification, rather than
   13 near-identical per-file justifications. Offered as a routing-economy
   suggestion; the parent owns the MANIFEST form.

4. **Soft-signal in the old files is real but already-richer downstream.**
   The "epistemic honesty is extraordinary / best I've encountered in this
   space" sentiment recurs in *every* file in this cluster (3-13, 3-14,
   opus-3-09, all 04-02 deep-review sessions, 4-06). It is genuine
   calibration signal but it is the *same* signal, and the richest, most
   attributed instances are in the 04-02 deep-reviews extract and 4-06. I
   recommend **one** consolidated sentiment ledger row attributed to "the
   2026-03/04 broad-review cohort (Opus/Codex/Gemini, ~10 independent
   reads)" rather than per-file rows — flat per-file append would re-bury
   the signal, which is the failure the ledger exists to prevent (ledger
   footer's own warning). Not mine to write; recommended to the parent.

---

## Independent-verify hooks (for the verifying pass)

Cheap re-checks that gate `adjudicated → routed → integrated`:

- `grep -n 'varepsilon\^\\ast' 01-aat-core/src/deriv-edge-credence-dynamics.md`
  → expect `(n_2+1)/(n_1+n_2+2)` at the "Optimal exploration rate" line
  (451729 F1 resolved).
- `grep -n 'D.1' TODO.md` → expect the open `- [ ]` 451729 D.1 entry under
  §2026-05-10 (451729's sole live blocker).
- `ls 03-llm-core/src | wc -l` → expect ≫ 0 (4-06 A3 resolved; was "empty").
- `ls 02-tst-core/src/hyp-causal-discovery-from-git.md` → exists (3-13 #5 /
  4-06 A4 resolved).
- `grep -l 'task adequacy\|structural persistence' 01-aat-core/src/result-persistence-condition.md`
  → present (the flagship 3-13#2 / synthesis-Tier-1a resolution).
- `ls doc/de-novo-audit-instructions.md` + `head -1`
  `audits/audit-2026-04-24-fresh-pass.md` → both exist (lineage-doc double
  subsumption).
- Spine corpus-redundancy claim: any single still-open substantive item
  (external validation) recurs in a later ledgered audit — confirm it is a
  declared Known Fragility / standing empirical-program scope, not a unique
  Cluster-E finding.

---

*End Cluster E adjudication. Deliverable is judgment + routing
recommendation only; parent + Joseph own all moves, ledger edits, MANIFEST
entries, and graduation.*
