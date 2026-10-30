---
kind: item
provenance: imported
source: TODO.md:246
section: TODO — Miscellaneous & details › Documentation queued
owner: ""
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
---

# Figure-artifact drift: committed `.pdf` + `-preview.png` are tracked but nothing auto-regenerates them (Joseph 2026-05-18). Same drift-class as the NOTATION ite

Imported verbatim (relative links rebased) from `TODO.md` line 246, section *TODO — Miscellaneous & details › Documentation queued*. Not yet re-checked against HEAD: `vsect recheck item:todo-figure-artifact-drift-committed-pdf-prev-a1b6 --outcome holds|stale|landed|not-an-item --why …`.

- **Figure-artifact drift: committed `.pdf` + `-preview.png` are tracked but nothing auto-regenerates them (Joseph 2026-05-18).** Same drift-class as the NOTATION item above, surfaced concretely by the `driver-snow-foundation` swap: `img/<base>.tex` is source-of-truth; `bin/build-monograph` recompiles it to the *gitignored* `<base>.mono.pdf` and embeds that, but by deliberate design (`bin/lib/segment_renderer.rb:658–689`, *"the build never mutates the committed `<base>.pdf` preview"*) it leaves the committed `<base>.pdf` (fallback in the priority chain) and `<base>-preview.png` (GitHub/eyeball artifact, not in the build path at all) untouched. So every diagram edit silently leaves two stale tracked artifacts unless a human remembers to rebuild them by hand — and diagrams will be edited constantly. **The tension that needs Joseph's call:** pure-gitignore (the LEXICON/NOTATION discipline) conflicts with *why* these two are tracked — the committed `.pdf` is the offline/no-TeX-toolchain render fallback, and `-preview.png` must be committed to render on GitHub; gitignoring either removes the reason it exists. **Recommended (strengthen-first, keeps both reasons intact):** keep them committed but add (a) `bin/refresh-figures` — rebuilds every `img/*.tex` → `.pdf` + `-preview.png`, folded into `bin/refresh-all` (parallel to `bin/build-readme` / `bin/term render`); and (b) `bin/lint-figures` — fails when any committed `.pdf`/`-preview.png` is older/stale vs its sibling `.tex` (mtime or content-hash; the README/LEXICON clobber-guard pattern, inverted to a staleness gate). Result: drift becomes a *loud build error*, not a silent stale commit, without losing the offline-fallback or GitHub-preview properties. Rejected alternative: build-time regeneration of the committed artifacts — reverses the deliberate read-only-w.r.t.-tracked-files rule and dirties the working tree on every `bin/build-monograph`. Cross-ref: figure-pipeline rationale in `msc/figure-pipeline-buildout-2026-05-18.md`; conventions-and-infra layer in [`FORMAT-TODO.md`](../../FORMAT-TODO.md).
