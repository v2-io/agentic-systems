# audits/ — orientation note

This tree is the audit-cycle output corpus. It holds three kinds of
thing: **top-level ALL-CAPS FINAL reports** (`audit-*.md`,
`analysis-*.md`, etc.) and **`pending-findings-*.md` resolution
trails** — both consumable deliverables — plus **per-cycle
`AUDIT-WORKING-NNNNNN/` subdirectories**, the lowercase intermediate
workspaces (predictions, per-segment reflections, scratch math,
running outlines) the FINALs were distilled from. The subdirectory
naming makes the split scannable: anything at the top level is a
deliverable; anything inside an `AUDIT-WORKING-*/` dir is an
archaeology trail. (Working dirs were consolidated here from `msc/`
on 2026-05-15; before that the intermediates lived in `msc/`.) It is
a **historical backlog**: many reports have been processed into the
live theory but not all have been moved to `audits/.integrated/`, and
the corpus is large.

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
