---
kind: item
provenance: imported
source: BIBLIOGRAPHY-TODO.md:87
section: Per-paper claim verification (works for AAT segment cites too)
owner: ""
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
---

# Linting before any submission / publication

Imported verbatim (relative links rebased) from `BIBLIOGRAPHY-TODO.md` line 87, section *Per-paper claim verification (works for AAT segment cites too)*. Not yet re-checked against HEAD: `vsect recheck item:bibliography-todo-linting-before-any-submission-publicatio-b0fc --outcome holds|stale|landed|not-an-item --why …`.


```bash
relata lint                                    # all entries
relata lint 01-aat-core                        # a specific paper/volume dir
REFS_LINT_STRICT=1 relata lint                 # non-zero exit on any finding
```

`lint` checks the anonymization deny-list (catches DOIs / authors that must not appear in a blind submission), schema validity, missing cited keys, and self-cite handling.
