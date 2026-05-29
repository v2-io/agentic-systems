# audits/ — orientation note

This tree is the audit-cycle output corpus. It holds three kinds of
thing: **top-level ALL-CAPS FINAL reports** (`audit-*.md`,
`analysis-*.md`, etc.) and **`pending-findings-*.md` resolution
trails** — both consumable deliverables — plus **per-cycle working
subdirectories of two distinct classes**: `AUDIT-WORKING-NNNNNN/` — the
**de-novo auditors' first-encounter cognition traces** (initial
predictions, per-segment between-segment reflections, running outlines,
and the §14 "Wandering Thoughts" ideation the de-novo protocol is
explicitly designed to elicit); and `ADJUDICATION-WORKING-NNNNNN/` — the
2026-05-16 audit-backlog-*triage* adjudication workspaces (a different
thing: per-cluster dispositions of the standalone-audit backlog). Top
level = consumable deliverable; the two `*-WORKING-*/` classes are
working/archaeology trails. (Working dirs were consolidated here from
`msc/` on 2026-05-15; the `ADJUDICATION-WORKING-` prefix split was added
2026-05-16 so the two classes are not confused — see the ⚠️ note next.)
It is a **historical backlog**: many reports have been processed into
the live theory but not all have been moved to `audits/.integrated/`,
and the corpus is large.

## ⚠️ The de-novo `AUDIT-WORKING-*` dirs are "the gold" — talk to Joseph before processing them

The `AUDIT-WORKING-NNNNNN/` dirs are **not scratch.** The de-novo audit
protocol (`doc/de-novo-audit-instructions.md`) is explicitly a cognition
experiment — it deliberately elicits incremental, first-encounter,
between-segment reflection and §14 "Wandering Thoughts" ideation from
each auditor. That accumulated first-encounter cognition is **"the
gold."** Its value is largely *orthogonal* to "which theory defects need
fixing"; to a triage mindset much of it reads as "irrelevant," and that
is exactly the trap.

**Before any processing, mining, summarization, cleanup, `.integrated/`
move, or deletion of the `AUDIT-WORKING-*` dirs, the responsible agent
MUST consult Joseph and decide _with him_ what is being done and why.**
He has stated he does not yet know the full intended disposition — only
the hard constraint: the gold must not be thrown away, summarized into
oblivion, or dropped into a black hole where it is never noticed again
*just because it was "irrelevant" to theory fixes.* This is a standing,
non-optional gate. It does **not** apply to the `ADJUDICATION-WORKING-*`
dirs — those are ordinary backlog-triage working trails, dispositioned
during the 2026-05-15/16 cleanup cycle (working spine archived at
[`.integrated/audit-backlog-triage-2026-05-15.md`](.integrated/audit-backlog-triage-2026-05-15.md)).

The **live routing status** — where each audit currently stands — is
[`STATUS.md`](STATUS.md); the **process** for routing findings is
[`../doc/audit-routing-instructions.md`](../doc/audit-routing-instructions.md).

## Naming: read "AAD" here as "AAT"

The mathematical core was renamed **Adaptation and Actuation Dynamics
(AAD) → Adaptation and Actuation Theory (AAT)** on **2026-05-15**
(the prior 2026-04-16 rename was ACT → AAD). This `audits/` tree was
*deliberately not swept* — it is archival/low-churn, and git preserves
the as-written record. So when you encounter **"AAD"** in any audit
document here, read it as **"AAT"**; the framework, sections, results,
and segment slugs it refers to are unchanged — only the name moved.
Directory *paths* (`01-aat-core/` etc.) were updated globally so
cross-references still resolve; only the *name* token is left as-was.

Canonical record of the rename (scope, rationale, disposition):
[`CHANGELOG.md`](../CHANGELOG.md), [`HISTORICAL-CONTEXT.md`](../HISTORICAL-CONTEXT.md),
and the *Naming note* in [`CLAUDE.md`](../CLAUDE.md). Full transition
plan: [`msc/AAD-to-AAT-TODO.md`](../msc/AAD-to-AAT-TODO.md).
