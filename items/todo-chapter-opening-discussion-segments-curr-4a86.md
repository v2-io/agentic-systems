---
kind: item
provenance: imported
source: TODO.md:306
section: TODO — Miscellaneous & details › Deferred — project structure / tooling › Chapter-discussion slug-prefix discipline + bin/align-slug recognition (queued 2026-05-13)
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
rechecked: 2026-10-30T21:56:14Z by Claude Opus 5.5 (item rechecker, t1-todo)
owner: F.1
restated: 'The section''s work (TODO.md:302-316, whose numbered steps were not imported) is open, and the hazard it warns of is live. bin/align-slug maps type discussion to prefix disc and has no intro/impl sub-class. A dry run of ''bin/align-slug --all'' at HEAD proposes causal-access-intro -> disc-causal-access-intro and the like for the 6 chapter-opening intro segments, and would do the same to the 17 impl- chapter-ends. The chapter-position distinction would collapse, and the ''do not run --all without spot-check'' guard lives only in TODO.md, which this effort will retire. Open: (1) teach align-slug the intro/impl sub-classes, a tool fix that should precede TODO.md''s retirement; (2) rename the 6 ''-intro'' suffix slugs to prefix form; (3) the semantic trap audit 773921 found (''strategy-structure-intro'' read as a structural-intro claim).'
---

# Chapter-opening discussion segments currently use a `-intro` *suffix*: `persistence-and-limits-intro`, `the-cycle-in-motion-intro`, `causal-access-intro`, `stra

Imported verbatim (relative links rebased) from `TODO.md` line 306, section *TODO — Miscellaneous & details › Deferred — project structure / tooling › Chapter-discussion slug-prefix discipline + bin/align-slug recognition (queued 2026-05-13)*. Not yet re-checked against HEAD: `vsect recheck item:todo-chapter-opening-discussion-segments-curr-4a86 --outcome holds|stale|landed|not-an-item --why …`.

- **Chapter-opening discussion segments** currently use a `-intro` *suffix*: `persistence-and-limits-intro`, `the-cycle-in-motion-intro`, `causal-access-intro`, `strategy-structure-intro`, `cooperative-adversarial-intro` (and others). These pre-date the role-prefix discipline established in the 2026-04-24 pilot.
