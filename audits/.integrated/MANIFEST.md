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

This manifest is the per-file justification audit trail. The in-flight
triage spine (state machine, evidence hierarchy, per-file partition, agent
briefs) lives at [`msc/audit-backlog-triage-2026-05-15.md`](../../msc/audit-backlog-triage-2026-05-15.md);
entries graduate here only once justified.

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

---

*New entries are appended by the parent agent as files graduate, each with
a per-finding-justified disposition. Do not bulk-move by date; date is a
prioritization hint, not evidence.*
