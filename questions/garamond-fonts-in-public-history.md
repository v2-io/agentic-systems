---
kind: question
closer: steward-fact
asked: 2026-10-30T21:22:18Z
asked-by: Claude Opus 5.5 (item rechecker, lane p-process)
---

# The Adobe Garamond Premier Pro font files, including a FontForge-modified variant, were committed in 8c1bb9a0 and untracked in 2addfd82 (2026-07-15), but they remain in the history of origin/main, and github.com/v2-io/agentic-systems is public. .gitignore itself calls them 'licensed + locally modified; NOT redistributable'. Does the license allow their presence in a public repository's history? If not, removing them needs a history rewrite (git filter-repo), which changes every later commit hash, breaks commit references in CHANGELOG.md and tags, and moves the asf submodule pointer in ~/src/arch.

Found re-checking the 2026-07-15 repo-weight decision brief. Only the license holder can say what the license permits, and a history rewrite of a shared public repo is not an act a rechecker should take.
