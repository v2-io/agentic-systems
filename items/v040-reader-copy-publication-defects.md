---
kind: item
owner: H.2
opened: 2026-10-30T23:32:57Z
opened-by: Claude Opus 5.5 (msc drain)
concerns: [segment:der-gain-sector-bridge, segment:der-interaction-channel-classification, segment:disc-stability-certificate, segment:result-sector-persistence-template, segment:scope-adaptive-system, segment:disc-identifiability-floor]
---

# The v0.4.0 reader-copy review found publication defects the build still produces: a -dirty hash on the title page from the build log written before compile, empty PDF metadata, raw #slug in figure captions, appendix titles and running heads, NOTATION.md cited inside Formal Expression, a ten-entry bibliography that omits the books load-bearing citations, and overfull displays

Source: msc/aat-v0.4.0-pdf-review.md (2026-08-15; read §1-§5 and its recommendations whole, §6-§9 by heading and recommendation), with msc/aat-v0.4.0-assembled-md-review.md the companion read of the assembled markdown. Not re-rendered by me; checked at HEAD 515c15ce only where a source file shows it: five segment bodies still cite NOTATION.md above their Working Notes (#der-gain-sector-bridge:45, #der-interaction-channel-classification:38, #disc-stability-certificate:86, #result-sector-persistence-template:112, #scope-adaptive-system:78). Ownership elsewhere: the [Gap] chapter openings are item:five-gap-chapter-intros-parts-ii-iii; the worked-example-cam stub is item:todo-aat-9-remaining-missing-stub-worked-exam-ad0e; cross-volume #slug rendering is item:todo-cross-component-slug-resolution-in-the-b-f1fb; the bibliographys content is item:bibliography-todo-w-3-segment-citation-migration-270-vol1-44ce (the reviews point for that item: a ten-entry back page "looks finished" and so misleads more than none; retitle it until the migration lands). What this item holds: build from a clean tree or drop the hash, fill hyperref metadata, render within-volume #slug in captions, titles and body as the \cref FORMAT specifies (Working Notes may keep slugs), sectionmark long appendix titles, and break the overfull displays (pp. 250, 493 of that build).

Checked against the regenerated snapshot at HEAD: the assembled-markdown review's outline-prose drops (`msc/aat-v0.4.0-assembled-md-review.md` §1: Part III preface, appendix-group preambles, Part I intro title) are fixed in `CURRENT-VOL1.md` and `CURRENT-VOL1-APPENDICES.md`; raw `#slug` still appears on 453 lines of `CURRENT-VOL1.md` (the public variant, no Working Notes), so recommendation 4 stands.
