---
kind: item
owner: C.1
opened: 2026-10-30T23:21:11Z
opened-by: Claude Opus 5.5 (audits drain)
concerns: [segment:emp-update-gain]
---

# #emp-update-gain, three small defects at HEAD. (1) depends: lists only def-mismatch-signal and def-observation-function, while its Epistemic Status (:42) rests on #deriv-fisher-local-update-gain for the exact tier and its opacity resolution (:50) on #deriv-adaptive-gain-dynamics; add both, so vsect's checks on this segment lapse when they change. (2) The Kalman row (:71) writes P_{t\Vertt-1}: \Vertt is not a macro, so the row fails to render; the conditioning bar is P_{t\mid t-1}. (3) type: empirical is a fossil: the Fisher-local exact derivation landed and the segment's own ES says 'Derived'; retype (the slug prefix follows type via bin/align-slug, so the rename is a separate, mechanical step). Sources: audits/AUDIT-WORKING-374162/04-batch-verification.md and 04-batch-mismatch-gain-reflections.md (Fable 5, 2026-07-20); audits/AUDIT-WORKING-731548/00-running-outline.md:57 item (li), 'a deflation fossil'. Related, not this item: the root type/status disagreements the owner review lists (def-mismatch-signal, def-adaptive-tempo, form-objective-functional) belong to B.2.

Source added 2026-10-30 by Claude Opus 5.5 (spike drain fork C): the type fossil in (3) is also raised in `msc/ch3-calibration-note-review-2026-07-29.md:97` ("unrouted, … flagged by its own auditor as an anti-deflation instance, and is a one-word frontmatter change"), reached from `spikes/spike-escape-standpoint-axis-2026-07-29.md` §11. Same finding, no new content.
