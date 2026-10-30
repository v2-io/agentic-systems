---
kind: review
author:
  name: Claude Sonnet 5.5 (item rechecker, lane s1)
  role: rechecker
sources:
  - msc/inside-out-2026-10/items-recheck/s1-navigation.md
written: 2026-10-30
---

# Item re-check lane s1 (navigation and structural trackers): findings on segments

KR I.3, under the top intent *"Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself"*. These came up while re-checking the five files of lane s1 against HEAD 2ec6ec58 and deleting four of them. Neither is a clear instance of the pilot's section 2.8 (a Working Note that says resolved about something unresolved); both are stale status lines, and the first is its mirror image. The lane found no instance of the 2.8 pattern proper.

## F1 (finding)
- target: segment:deriv-recursive-update

Working-Note status signal: the Working Note at line 230 says 'The "(Descended from TFT Appendix ...)" annotation is diff-voice in the body. Editorial: move to Working Notes or remove', reporting an open defect in the body. The body has no such annotation at HEAD: a search of the segment for 'Descended', 'TFT' and 'predecessor' finds only the Working Note line itself, and the line has been the only occurrence since it was lifted in 46168faf (2026-05-31). It is the mirror image of the pilot's pattern: the note signals an unresolved defect the body does not have, which sends a future reader looking for something that is not there. Delete the line, or keep it only if it guards against re-adding the annotation. Similar lines in other segments (`emp-update-gain.md:104`, `post-causal-structure.md:70`, `def-adaptive-tempo.md:84`) were not checked.

## F2 (finding)
- target: segment:disc-continuity-stance

Working-Note status signal: the Working Note at line 60 says the LEXICON's Continuity section is 'under review — see TERMINOLOGY-TODO §F' and that the five stance terms 'point to this segment as their `primary_source` once it lands'. TERMINOLOGY-TODO.md was deleted on 2026-10-30 (its content is now ledger items; the reorganization is `item:terminology-todo-breakage-a-the-persistence-subgroup-mixe-2fb5`), so the pointer dangles. The future tense is also stale: the segment has landed, and `terminology/entries/indifferent.md` and `negotiated.md` already name it as `primary_source`. The review itself is real and still open. The Working Note before it ('Reconsideration resolved') says the proposal to demote the stance axis is resolved against by `#deriv-self-actuation-grounding`; I read the cited Discussion paragraph (line 106, 'Consequence for continuity stance') and it supports that. Relink the pointer to the ledger item and drop 'once it lands'.
