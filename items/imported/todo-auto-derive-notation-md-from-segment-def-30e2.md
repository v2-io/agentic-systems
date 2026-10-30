---
kind: item
provenance: imported
source: TODO.md:245
section: TODO — Miscellaneous & details › Documentation queued
owner: ""
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:result-mismatch-decomposition]
---

# Auto-derive `NOTATION.md` from segment definitions (drift fix; Joseph 2026-05-18). `NOTATION.md` is hand-maintained and the live theory drifts from it — spike f

Imported verbatim (relative links rebased) from `TODO.md` line 245, section *TODO — Miscellaneous & details › Documentation queued*. Not yet re-checked against HEAD: `vsect recheck item:todo-auto-derive-notation-md-from-segment-def-30e2 --outcome holds|stale|landed|not-an-item --why …`.

- **Auto-derive `NOTATION.md` from segment definitions (drift fix; Joseph 2026-05-18).** `NOTATION.md` is hand-maintained and the live theory drifts from it — spike findings and rewritten segments change a quantity's structure without updating it (the §0 "NOTATION is a lagging proxy, never authority" trap; worked instance: the $\rho$ gloss vs the `#result-mismatch-decomposition` additive truth, 2026-05-18). Structural fix: generate `NOTATION.md` from per-segment symbol declarations the way `LEXICON.md` is generated from `terminology/entries/` and `README.md` from `doc/readme/` partials — symbols defined once, at the segment, extracted; the index then *cannot* drift. Scope: a symbol-declaration convention in segment frontmatter or a tagged block, plus a `bin/`-generator + lint (parallels `bin/term`/`bin/build-readme`/`bin/extract-findings`). Until then the drift caveat at the head of `NOTATION.md` stands and the file is non-authoritative by construction.
