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

---

*New entries are appended by the parent agent as files graduate, each with
a per-finding-justified disposition. Do not bulk-move by date; date is a
prioritization hint, not evidence.*
