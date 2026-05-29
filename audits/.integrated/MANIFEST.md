# Manifest — `audits/.integrated/`

`audits/.integrated/` is where an audit file goes once **every finding it
raised has a verified disposition** — resolved (by strengthening, or by an
honest softening *after* a strengthening attempt was made and recorded as
failed), correctly rejected (e.g. it asked us to weaken a claim we instead
strengthened the theory to defend), genuinely subsumed/duplicated, or
captured as soft/idea/sentiment in a durable home so nothing is lost.

The unit that earns a move is the **finding**, not the file, and the test
is "closed *in the right direction*," not merely "closed." Moving a file
here asserts that. `git mv` is reversible if any classification was wrong.

This manifest is the per-file justification audit trail. The live routing tracker — where each audit currently stands (routed vs. graduated) — is [`../STATUS.md`](../STATUS.md); entries graduate here only once justified. The 2026-05-15/16 cleanup cycle's working spine (state machine, evidence hierarchy, per-file partition, agent briefs) is archived alongside this manifest at [`audit-backlog-triage-2026-05-15.md`](audit-backlog-triage-2026-05-15.md).

## Evidence hierarchy (what counts as "verified disposition")

Established 2026-05-15 during the audit-backlog cleanup. In decreasing
reliability:

1. **`pending-findings-*.md` resolution ledgers** — the de-novo spec's
   durable "what each finding became" record. Carry explicit per-finding
   status, landing commit hashes, spike pointers, and `See TODO.md`
   cross-refs for what stays open. Decisive for the cycles they cover
   (the 2026-04-21/22/23/25 intakes: 471203 / 584721 / 613842 / 742613 /
   etc.).
2. **`CHANGELOG.md` cycle narratives** (post-2026-04-24) — what each
   intake landed, what conventions/disciplines emerged.
3. **Open-`[ ]` backlinks in `TODO.md` / `PROPOSALS.md` / `PRACTICA.md`**
   — a live backlink to an audit file *or an associated `msc/` file* is a
   *sufficient* signal of NOT-integrated. (Absence of a backlink is **not**
   sufficient for integrated — that is why first-hand spot-check against
   current `src/` is required.)
4. **First-hand re-read of the finding against current `src/`** — required
   for files with no ledger (pre-2026-04-21) and for any no-backlink file
   before it earns a move. Corpus redundancy is the safety net here: audit
   findings are rarely unique, so a genuinely-unaddressed one almost
   certainly recurs in a more recent (ledgered) audit.

> **`git`-recency is poisoned as a signal.** The 2026-05-15 AAD→AAT rename
> sweep (`ce99ce6` / `9745397`) mechanically touched nearly every audit
> file, so "last commit date" and message-pickaxe over the `audits/` tree
> are uninformative for integration status. Use the ledgers, not the log.

## Already integrated

### 2026-05-12 — Codex + Gemini de-novo monograph-build audits

Moved here before 2026-05-15 (pre-dating this manifest; recorded
retroactively). Intake-and-disposition narrative: **CHANGELOG 2026-05-12**
("The eight surgical strengthen-first edits" ledger + the four spike-and-
integrate stages). Residual open items were lifted into `TODO.md`
§"2026-05-12 — Audit-findings intake" as their own first-class items
(build-pipeline / preface-discipline / real-missing-stubs), so the source
audits are *routed* even though follow-on work continues.

| File | What it was | Disposition |
|---|---|---|
| `codex-audit-results-2026-05-12.md` | line-precise cross-corpus (read the mono builds) | Findings routed; surgical strengthen-first edits landed (CHANGELOG 2026-05-12); residual opens → TODO §2026-05-12 |
| `gemini-audit-results-2026-05-12.md` | thematic cross-corpus | Findings routed; same intake; residual opens → TODO §2026-05-12 |
| `gemini-aad-audit-2026-05-12.md` | AAT-only math-verification | Findings routed; Gemini-AAT L1′ + CIY→LMI strengthenings landed (CHANGELOG 2026-05-12) |

*(The `TODO.md:380` reference to these three was repointed from `msc/…`
to `audits/.integrated/…` in commit `c1c80a9` — they had been moved here
but the live pointer still aimed at the old `msc/` path.)*

### 2026-05-15 — audit-471203 de-novo cycle (2026-04-28)

Adjudicated via pilot 583046; both consequential claims primary-source-
verified by the parent. Ledger note: 471203 has **no `pending-findings`
file** — its durable resolution record is its own SUPPLEMENT (§K
triangulation + §L). FINAL + SUPPLEMENT graduate together (one cycle).

| Finding | Disposition |
|---|---|
| §B F1 — stale xref to demoted `#deriv-directional-survival-exploration` | **resolved**, spot-checked: slug absent from `src/`; `disc-ciy-unified-objective.md:44` now cites `#deriv-causal-ib-lmi` |
| §B F2, F3 — disc-ciy status-label / implicit-Markov-of-Ω | resolved per SUPPLEMENT §K; pilot first-hand-confirmed against `src/` |
| §B F4 | resolved per SUPPLEMENT §K (pilot-verified) |
| §B F5 — `post-composition-consistency` depends/stage | already routed: PROPOSALS SP-6 + TODO:149 + F-A cluster (584721/742613). Not a graduation blocker |
| §B F6 — `scope-agency.md:19` Pearl `$do(a)$` before declaration | ≡ `audit-742613-FINAL:254`. Recorded under FORMAT-TODO **C12** (its existing general home) 2026-05-15 |
| §B F7 — Tishby-Zaslavsky 2015 miscites the IB↔VFE bridge | **resolved by strengthening** (SUPPLEMENT §L option b): kept T-Z for the deep-learning IB instantiation, added web-verified **Alemi, Fischer, Dillon & Murphy 2017 (arXiv:1612.00410)** for the variational bridge. `form-information-bottleneck.md:50` |
| §F1 — propose `#disc-theorem-import-architecture` 4th meta-segment | **PROPOSALS SP-23** (new, full schema) |
| §F7 — commitment-state $C_t$ extension to $G_t$ | ≡ **PROPOSALS SP-12** (§D.4) — exact pre-existing match |
| §F5 — Class-2 LLM engineering-guidance reach | subsumed by the class-coercion-via-wrapping cycle (CLAUDE.md / PROPOSALS) |
| §F6 — 04-eli-core OUTLINE-vs-present / README over-impression | → TODO:386 (preface/README-honesty discipline) |
| §F2, F3, F4, F8 — (PI)-uniqueness seed / composed-obstruction theorem / persistence hysteresis / CIY-naming | → polish-and-sentiment ledger S4–S7 (research-seed / naming-seed) |

Files moved: `audit-471203-FINAL-2026-04-28.md`,
`audit-471203-SUPPLEMENT-phase-2.md`.

### 2026-05-15 — extracted-gemini-feedback-2026-04-26-27

Self-disposed extract (carries its own `## Disposition`). Dispositions
verified closure-direction-correct against current `src/` (math-
strengthening spikes landed; opacity-gain → `deriv-adaptive-gain-dynamics`;
findings-schema split adopted; README items addressed then superseded by
the auto-gen pipeline). Soft/sentiment mirrored to the ledger: **S1**
(Domain-transfer kind — considered-declined-with-reason), **S2** (Gemini
schema enthusiasm — sentiment/calibration), **S3** (README 1–3 —
superseded-by the README v2 pipeline). File moved:
`extracted-gemini-feedback-2026-04-26-27.md`.

### 2026-05-16 — Cluster A: self-disposed extracts (verify-and-mirror, 13)

Adjudicated `ADJUDICATION-WORKING-704218`; load-bearing dispositions
parent-verified primary-source. All 13 carry their own `## Disposition`;
all closure-direction-correct against current `src/`. Dominant closure mode
**resolved-by-strengthening**, visible in `src/` (log-odds uniqueness
theorem; π\*-first KL + uniqueness; P3→Markov proved under causal
sufficiency) — these are *correctly closed*, not reopenable.

| Finding | Disposition |
|---|---|
| The 13 extracts' stated dispositions vs current `src/` | All **verified closure-direction-correct**; graduate. |
| `extracted-codex-feedback-2026-04-28` stated "Pending" | **Corrected, not mirrored:** all three items resolved primary-source (`bin/naming-aggregate.rb` defaults `votes_dir: msc/naming/naming-votes`, refs `doc/naming-principles.md`; the 3rd file reorganized away). MANIFEST records **resolved**. |
| `extracted-claude-feedback-2026-04-22-bf945f78` independence | *Not* independent corroboration — it **is** the Opus pass inside `extracted-audits-2026-04-22-morning`. Recorded so convergence-as-evidence is not miscounted. |
| `extracted-codex-feedback-2026-04-03` / `-04-06` / `-04-26-bridge-spike` | Provenance value: #04-03 = primary source for the CLAUDE.md Codex-open-questions-are-reader-clarity-gaps convention; #04-06 = the no-shortcuts/false-constraints/strengthen-before-soften origin; #04-26 = `research-trail/provenance` (bridge-spike contribution + Gemini→Codex provenance), **not** ledger-routed. Graduate *with* the provenance notes. |
| Soft / sentiment / declined / research-seed | → polish-and-sentiment ledger, one consolidated curated pass (S8–S15, dedup map applied): POMDP-collapse S8, Section-I-strongest S9, honesty-load-bearing S10, Tier-3 S11, 4c-sensitivity S12, Opus-residue S13, Cox-necessity S14, derived/chosen/assumed-table S15. |

Files moved: `extracted-audits-2026-04-21.md`, `extracted-audits-2026-04-22-morning.md`, `extracted-audits-2026-04-25.md`, `extracted-claude-feedback-2026-04-22-6d858f28.md`, `extracted-claude-feedback-2026-04-22-3546217a.md`, `extracted-claude-feedback-2026-04-22-bf945f78.md`, `extracted-codex-feedback-2026-04-01.md`, `extracted-codex-feedback-2026-04-02.md`, `extracted-codex-feedback-2026-04-03.md`, `extracted-codex-feedback-2026-04-06.md`, `extracted-codex-feedback-2026-04-22-r2.md`, `extracted-codex-feedback-2026-04-26-bridge-spike.md`, `extracted-codex-feedback-2026-04-28.md`.

### 2026-05-16 — Cluster B: math-heavy ledgered (584721 / 613842 / 742613+SUPPLEMENT / opus-2026-04-21 / audits-2026-04-22-evening / 738192)

Adjudicated `ADJUDICATION-WORKING-628401`; gating dispositions
parent-verified primary-source incl. the Model-S no-go worked first-hand
from the SDE and cascade-closure verified clean (routing tracker
2026-05-16 cont.2). Strengthen-before-soften had maximum bite here and the
project passed repeatedly (≈25/30 findings resolved, the majority by
strengthening, several past the audit's ask). Ledgers
`pending-findings-2026-04-2{1,2,3}.md` read as evidence — **not**
graduated (durable infrastructure).

| Finding | Disposition |
|---|---|
| 742613-F2 / 613842-F2 — Model-S P(τ_R<∞) infinite-horizon non-exit object in `deriv-sector-condition` Prop A.1S(iii) + summary segments | **resolved by strengthening-then-no-go** (state 3). Present state: Prop A.1S carries (iii′) fixed-time/stationary tail + (iv) finite-horizon sup-bound; the infinite-horizon object is **Corollary A.1S.1** (exact) — P(τ_R<∞) is exactly {0,1}, 0 under Model D, 1 under Model S, α-invariant — Model-S half proved in `#deriv-stochastic-non-exit`. Downstream cascade verified clean (every dependent consumes the stopped bound / MS-threshold / fixed-time tail; the falsified ever-exit object is propagated nowhere). Spike: `spikes/spike-stochastic-non-exit-strengthening-2026-05-16.md`; CHANGELOG 2026-05-16. 613842-F2 ≡ 742613-F2 — same segment-state; the precise ever-exit-conflation reading governs the dedup. |
| 742613-F1 — score-function sign (`def-mismatch-signal`) | resolved (sign corrected; `def-mismatch-signal.md:34`). |
| 742613-F3/F5/F8, 584721-F-A/F-D/F-B1, opus-2026-04-21 §1–4, 738192-F1/F2 | resolved, the majority **by strengthening** (log-odds uniqueness; π\*-first KL + uniqueness theorem; completeness-argument unification; BH-identity + matching lower bound; depends-graph lint clean; P3→Markov proved; opacity/IB strengthenings; `git checkout` scoped-L3 regime in the canonical TST segment, SN-3 landed `3072667`/`2666eca`). Per-finding detail: adjudication 628401. |
| 742613-F4 / 613842-F1 — `def-adaptive-tempo status: exact` vs additive-overcount | substance resolved by strengthening (matrix-Loewner canonical, scalar = special case); narrow frontmatter/status residue tracked TODO:395/126 — not a graduation blocker. |
| 742613-F6 residue (Pearl-`do` before declaration) | `duplicate` of 471203 §B F6 ≡ 742613:254 → FORMAT-TODO C12 (existing home; do not double-track). |
| §A/§D, process-feedback, bigger-picture/synthesis | → polish-and-sentiment ledger (S21, S22, S29 + P-block). opus-2026-04-21 "spike-stronger-than-segment" cross-cutting pattern recorded as the *validated-and-absorbed* empirical ancestor of strengthen-before-soften, not open. |

Files moved: `audit-584721-FINAL-2026-04-25.md`, `audit-742613-FINAL-2026-04-25.md`, `audit-742613-SUPPLEMENT-PHASE-2-TRIAGE.md`, `audit-613842-FINAL-2026-04-25.md`, `opus-audit-2026-04-21.md`, `audits-2026-04-22-evening.md`, `audit-738192-FINAL.md`.

### 2026-05-16 — Cluster C: 2026-04-24/25 + hygiene + portfolio (4)

Adjudicated `ADJUDICATION-WORKING-704182`; verify-and-mirror against the
self-disposed banded triage + `pending-findings-2026-04-25` (read as
evidence, not graduated). 5 of 8 F-V/P-V closed **by strengthening**.

| Finding | Disposition |
|---|---|
| F-V1/2/4/5, P-V1/2/3 | **resolved** (5/8 by strengthening; AF-2 a clean better-strengthening than the soften-justified extraction anticipated). |
| SN-3 (`def-pearl-causal-hierarchy` bald `git checkout`→L3) | **resolved by strengthening** — scoped to the α/β/γ regime, downstream-deferred; landed `3072667` + `2666eca` (parent co-owner direct-fix), parent-verified. |
| F-V3 / F8 (composite-agent C-iii) | `actionable-open` but **triple-tracked** (TODO:95 + PROPOSALS SP-21 §G + ledger). Graduates *with the open item living in TODO/PROPOSALS*, not double-tracked. |
| link-and-file-hygiene-findings | 8/11 `resolved` (doc-rot self-healed by 2026-04-28+ rewrites), 1 moot (sunset file), 1 tooling-rec; closed doc-rot snapshot. Fresh lint state (3 ordering + 1 missing-dep) → standing-hygiene TODO, blocks no graduation. |
| portfolio-reviews | `process/instruction-feedback` — strategic-portfolio provenance (the documentary origin of strengthen-before-soften, session 2c4918d4); retained-as-history, no open framework work. |
| J1–J10 | → ledger S20 (one themed sentiment row). |

Files moved: `audit-2026-04-24-fresh-pass.md`, `audit-final-reports-candidate-extraction-2026-04-25.md`, `link-and-file-hygiene-findings.md`, `extracted-claude-feedback-2026-04-22-25-portfolio-reviews.md`.

### 2026-05-16 — Cluster D: 2026-04-28 FINALs (829314 ×4, 849201 ×4)

Adjudicated `ADJUDICATION-WORKING-714206`; first-hand against current
`src/` (no SUPPLEMENT exists for 829314/849201 — their durable evidence is
the FINAL's inline Phase-2 + first-hand re-read; **a future verifier
should not hunt a non-existent SUPPLEMENT**). The encounter tracker
`msc/logogenic-encounter-2026-05-01/07-audit-integration-tracker.md`
tracks audit-id **193847**, *not* 829314 (coincidental digit overlap) —
not a 829314 integration record.

| Finding | Disposition |
|---|---|
| **Opacity-gain tension** (849201-F1) — cluster strengthen-first headline | **resolved by strengthening**, ≥3-cycle convergence (849201-F1 / extracted-gemini-2026-04-26-27 / AUDIT-WORKING-742613 flag → one shared `deriv-adaptive-gain-dynamics` strengthening; `emp-update-gain.md:44`). Stated once here, not re-litigated three times. |
| 829314-core-F1 | `duplicate` of 471203 §B F5 (+`correctly-rejected` on merits) → defer to that disposition; do not double-track. |
| 829314-core-F5 (`Descended from` footers) | **resolved** — 0 hits across all `src/` trees (parent-verified). |
| 829314-core-F6 / -LOGO-F1 / -TST-F3 (DB-entry bloat) | `subsumed-by-later-work` (markdown-first pipeline + FORMAT schema + extract-findings); declined Sidecar pattern → ledger S18 (with reason). |
| 829314-core-F7 (OUTLINE mis-describes `#der-team-persistence`) | **resolved** — co-owner direct-fix landed (`4172866`): OUTLINE now "Per-sub-agent persistence within a team (composite analog: #deriv-critical-mass-composition)". |
| 829314-LOGO-F2 / -LOGOZOETIC / -TST / 849201-FINAL F2 / -LOGOGENIC / -SEC-III / -TST | resolved / verified-still-honest / confirmation-class. Soft → ledger S16/S17 (convergence + cohort sentiment, one row each); 849201-F2 redundant with S7, skipped per adjudication. |
| 829314-TST-F2 / -TST-F5, OUTLINE-order F3/F4 | → ledger S23 / S24 / S26. |

Files moved: `audit-829314-FINAL-2026-04-28.md`, `audit-829314-FINAL-2026-04-28-LOGO.md`, `audit-829314-FINAL-2026-04-28-LOGOZOETIC.md`, `audit-829314-FINAL-2026-04-28-TST.md`, `audit-849201-FINAL.md`, `audit-849201-FINAL-LOGOGENIC.md`, `audit-849201-FINAL-SEC-III.md`, `audit-849201-FINAL-TST.md`.

### 2026-05-16 — Cluster E: pre-ledger old + the April-01/02 consolidation chain + lineage (12)

Adjudicated `ADJUDICATION-WORKING-472914`; first-hand re-read + the
corpus-redundancy safety net (these predate the `pending-findings`
ledger). Every high-weight recurring finding is **resolved in current
`src/`**, generally by the strengthening discharge (the κ-as-scalar →
GUC-class architectural classification is the theory-scale
strengthen-not-soften exemplar — *must not* be reopened as "scope it
down"). Routing-economy: the **April-01/02 nested-revision chain is one
grouped entry with a shared redundancy table**, not 12 near-identical
justifications.

| Finding (grouped) | Disposition |
|---|---|
| The 2026-03 + April-01/02 broad-review chain (04-01 → 04-01-remaining → 04-02-{synthesis,round2} → 04-02-comprehensive) | `subsumed-by-later-work` — each later file explicitly supersedes the earlier; every substantive recurring finding (directed-separation/κ-category-error, persistence-stronger-than-proof, composition-before-bridge, graph-uniqueness, git-causal, 03-llm-core-empty, IB-orphaned, three-way-tradeoff) is resolved in current `src/` per the shared redundancy table in the adjudication. `analysis-2026-04-02-synthesis` is a curated/raw pair with the deep-reviews extract — same content, *not* `diff`-duplicates; not independent signal. |
| `2026-03-14-fresh-eyes-assessment` | `subsumed` + **retain-as-history** — archaeological origin of the κ-as-scalar-category-error commitment (CLAUDE.md §5 / GUC). |
| `extracted-claude-feedback-2026-04-02-deep-reviews` | **retain-as-history** — lineage of the 04-02 consolidated docs + the three-rings-of-rigor / Gate-1–4 origins; findings subsumed, provenance preserved. |
| `extracted-claude-session-…-audit-instructions-lineage` | **retain-as-history** (doubly subsumed) — provenance of `doc/de-novo-audit-instructions.md`; the embedded Tier-A/B/C audit's findings are Cluster C's `pending-findings-2026-04-25` — **de-dup at routing; do not double-track from two clusters.** |
| External-validation recurring MEDIUM | `subsumed-by-later-work` (standing declared empirical-program fragility; recurs in every later audit). Soft → ledger S16 (one cohort sentiment row). |
| `audit-451729-FINAL-2026-05-10` | **does NOT graduate** — stays open on its single residual D.1 (first-class in TODO §2026-05-10, routed not homeless). Soft items → ledger S25/S28. |

Files moved: `2026-03-13-feedback.md`, `2026-03-14-fresh-eyes-assessment.md`, `feedback-2026-03.md`, `opus-analysis-2026-03-09.md`, `analysis-2026-04-01.md`, `analysis-2026-04-01-remaining.md`, `analysis-2026-04-02-comprehensive.md`, `analysis-2026-04-02-round2.md`, `analysis-2026-04-02-synthesis.md`, `analysis-2026-04-06.md`, `extracted-claude-feedback-2026-04-02-deep-reviews.md`, `extracted-claude-session-6da0db68-2026-04-24-audit-instructions-lineage.md`.

> **Not graduated, by design:** `audit-451729-FINAL-2026-05-10.md` (open,
> D.1), the four `pending-findings-2026-04-2{1,2,3,5}.md` ledgers (durable
> read-as-evidence infrastructure), `audits/README.md` (directory
> infrastructure + the gold-dir standing-gate pointer), the 19 de-novo
> `AUDIT-WORKING-*` "gold" dirs (separate standing gate — consult Joseph).
> The 6 `ADJUDICATION-WORKING-*` workspaces — confirmed fully integrated
> (every disposition/soft-row/observation routed; nothing lives only there)
> — were **cleared into `.integrated/ADJUDICATION-WORKING-<id>/`** per the
> working-directory-lifecycle policy (a served-purpose working dir does not
> stay in the live tree); they remain the cited un-flattened provenance,
> now co-located with this MANIFEST. Soft signal lives in
> [`../polish-and-sentiment-ledger.md`](../polish-and-sentiment-ledger.md)
> S8–S30 (one consolidated curated pass). S30 was adjudicated up by Joseph
> to the `#sketch-structural-adaptation-genericity` exploratory OUTLINE
> node. Authoritative process: [`../../doc/audit-routing-instructions.md`](../../doc/audit-routing-instructions.md).

---

*New entries are appended by the parent agent as files graduate, each with
a per-finding-justified disposition. Do not bulk-move by date; date is a
prioritization hint, not evidence.*
