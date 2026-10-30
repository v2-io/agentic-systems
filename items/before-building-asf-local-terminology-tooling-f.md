---
kind: item
owner: F.1
opened: 2026-10-30T21:56:32Z
opened-by: Claude Sonnet 5.5 (item rechecker, lane s1)
---

# Before building asf-local terminology tooling (F.1's proposed standard_name field on terminology entries, a NOTATION render from entries), check it against the program-level migration of the terminology system: bin/term, the entry format (YAML to udon) and per-project lexicons are planned to move to archterm, so a field built here may be re-homed or rebuilt.

From the note at the top of the deleted TERMINOLOGY-TODO.md (line 6, git show 6f98aa45^:TERMINOLOGY-TODO.md): 'don't build asf-local tooling features that the migration will re-home'. The plan is ~/src/arch/TODO.md section 'Terminology system -> program level (archterm)' (step list checked at HEAD, all unchecked). The plan's target path common/utl/ does not exist after the archema-io to arch rename, so the plan itself needs a path check. Whether F.1's field lands in asf now or in archterm is the decision this item holds.
