---
kind: item
provenance: imported
source: TODO.md:440
section: 'TODO — Miscellaneous & details › 2026-05-12 — Audit-findings intake: Codex + Gemini de-novo audits — remaining open items › Group (c) — TST surgical sweep — open items'
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:hyp-causal-discovery-from-git]
rechecked: 2026-10-30T21:54:28Z by Claude Opus 5.5 (item rechecker, t1-todo)
owner: F.1
restated: 'The scoping landed; the naming did not. #def-system-coupling (since ae118ab5, 2026-05-12) states when the git estimate is a causal parameter and otherwise calls it ''a descriptive statistic of co-change'', and #hyp-causal-discovery-from-git separates P(change(B) | change(A)) from the interventional quantity. But the defined symbol is still coupling(m_i, m_j) = P(change(m_j) | change(m_i)), an associational quantity under a name readers take as causal; the rename to cochange(m_i, m_j), with ''causal coupling'' reserved for adjusted estimates, has not happened (grep: no ''cochange'' anywhere in canon). That is a terminology decision through bin/term, which is F.1''s lane.'
---

# TST-4 git-as-intervention naming discipline — reserve `causal_coupling` for estimates with atomic commits / feature scope / temporal contrast / dependency-prior

Imported verbatim (relative links rebased) from `TODO.md` line 440, section *TODO — Miscellaneous & details › 2026-05-12 — Audit-findings intake: Codex + Gemini de-novo audits — remaining open items › Group (c) — TST surgical sweep — open items*. Not yet re-checked against HEAD: `vsect recheck item:todo-tst-4-git-as-intervention-naming-discipl-936c --outcome holds|stale|landed|not-an-item --why …`.

- [ ] **TST-4 git-as-intervention naming discipline** — reserve `causal_coupling` for estimates with atomic commits / feature scope / temporal contrast / dependency-prior constraints / explicit confounder adjustment; rename raw aggregates to `cochange(m_i, m_j)` elsewhere. Already partially addressed in `#hyp-causal-discovery-from-git`; needs cross-segment audit.
