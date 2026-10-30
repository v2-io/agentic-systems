---
kind: item
provenance: imported
source: BIBLIOGRAPHY-TODO.md:36
section: 'BIBLIOGRAPHY-TODO.md — ASF citation system: discipline, tooling, workstreams › How to use relata, today'
owner: ""
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
---

# Querying

Imported verbatim (relative links rebased) from `BIBLIOGRAPHY-TODO.md` line 36, section *BIBLIOGRAPHY-TODO.md — ASF citation system: discipline, tooling, workstreams › How to use relata, today*. Not yet re-checked against HEAD: `vsect recheck item:bibliography-todo-querying-3ad9 --outcome holds|stale|landed|not-an-item --why …`.


```bash
relata search bareinboim          # fuzzy-match key / author / title / year
relata show pearl-2009-causality  # full entry + verification status + cited-by
relata list --verified            # all entries; flag those with all-criteria verified
relata possible-duplicates --title "active inference" --author friston
```
