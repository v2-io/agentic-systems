## For Auditors

**You are reading the auditor-facing README.** This version of the project README is intentionally narrower than [`README.md`](README.md) — sections that would prime a de-novo audit (specific novel-results claims, recent cycle narrative, known-issues list, recently-landed architectural moves) have been removed.

If you are conducting a de-novo audit, please read [`doc/de-novo-audit-instructions.md`](doc/de-novo-audit-instructions.md) before going further. It documents the audit posture, the source-ordering convention (segments first; `msc/`, `ref/`, git only when grounding requires it), and the failure modes prior audit cycles have surfaced.

The following files carry priming content and are best read only after your audit is complete, when the explicit purpose is to compare your independent findings against the project's existing record:

- `README.md` — the public README (has Findings, Recent Progress, Known Issues sections)
- `FINDINGS.md` — curated novel-results catalog
- `CHANGELOG.md` — cycle-by-cycle narrative of what has been judged settled
- `LOG.md` — pre-2026-04-24 cycle archaeology
- `TODO.md` — active and archived findings, including the "settled" framings of prior cycles
- `PROPOSALS.md` — architectural-proposal portfolio with prior-reasoning trails
- `doc/readme/src/_findings-summary.md`, `_recent-progress.md`, `_known-issues.md` — the auto-generated live includes underlying the public README
- `msc/pending-findings-*.md`, `msc/audit-*.md` — prior-cycle audit working documents

Reading these is not forbidden — nothing in this project is — but tends to bias toward ideas previous auditors have already heavily visited, and that's not in the spirit of a *de novo* audit. The most useful contributions from a fresh pass come from genuinely-fresh perspectives.
