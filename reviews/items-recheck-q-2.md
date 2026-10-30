---
kind: review
author:
  name: Claude Opus 5.5 (item rechecker, q-proposals lane)
  role: rechecker
sources:
  - msc/inside-out-2026-10/items-recheck/q-proposals.md
written: 2026-10-30
---

# A further Working-Note status signal from the proposal re-checks

KR I.3. Found while listing the segments whose Working Notes point at the deleted `PROPOSALS.md`, after `reviews/items-recheck-q.md` was taken in. The pilot's §2.8 pattern again.

## F1 (finding)
- target: segment:deriv-gain-sector
- at: 0dce6b67

Working-Note status signal: the note at :326 says the per-event versus per-time normalization of $\alpha$ is "architectural; tracked in PROPOSALS" and "Routed `architectural`→PROPOSALS". It was never there: `git log -S'per-event' -- PROPOSALS.md` finds nothing, and no imported item carries it. Meanwhile the core of it landed: since 9d227e67 (2026-05-31) `#der-gain-sector-bridge` defines $\alpha_{\text{event}} = \eta^\ast c_{\min}$ and the per-time rate $\alpha = \nu \eta^\ast c_{\min}$ (:35-45). So the note points at a home that never held the work and reads as open for a fix that is in. The one residue the owner review named, `#result-persistence-condition`:79 stating the per-event form (Part I explorer, :135), is fixed at HEAD as well: that line now reads $\alpha = \nu \cdot \eta^\ast \cdot c_{\min}$ (per time). I checked those two places only, not every downstream use of $\alpha$; at both, the item the note calls open is done.
