# Build / auto-generation-pipeline SOP

> [!note]
> **Status:** planned stub — not yet authoritative. This file marks the topic in the `doc/sop/` taxonomy ahead of migration; the procedure has not moved here yet.
> **Current authoritative home:** [`../../msc/markdown-first-pipeline.md`](../../msc/markdown-first-pipeline.md) (design record) + the `bin/` tool headers + [`../../FORMAT-TODO.md`](../../FORMAT-TODO.md) (live state).
> **Owns (planned):** the auto-generation disciplines (README / README-auditor / LEXICON / FINDINGS / recent-progress / known-issues are generated — edit the source, never the output; `bin/refresh-all` orchestration); the three-stage markdown-first monograph pipeline + chunk-format contract; the Ruby-for-internal / Python-for-community script-language convention.
> **Staleness check (live now):** `bin/refresh-all --check` regenerates the whole doc pipeline (extract-findings → extract-recent-progress → extract-known-issues → build-readme) in a temp copy and diffs all six generated outputs against the working tree — non-mutating, exit 1 on drift, `--diff` for unified diffs. Run it at cycle-close before committing; the pre-commit-hook one-liner is in the `bin/refresh-all` header. LEXICON.md is deliberately out of scope (separate `bin/term` pipeline; timestamp line defeats naive diffing — see the header note).
> **See also:** [`sop-creation.sop.md`](sop-creation.sop.md) (the SOP convention) · [`../../msc/sop-consolidation-design-2026-06-01.md`](../../msc/sop-consolidation-design-2026-06-01.md) (migration plan).
