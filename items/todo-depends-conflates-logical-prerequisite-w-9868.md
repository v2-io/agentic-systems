---
kind: item
provenance: imported
source: TODO.md:264
section: TODO — Miscellaneous & details › Editorial hygiene (standing items)
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:form-strategy-complexity-cost, segment:deriv-strategy-cost-regret-bound, segment:def-model-sufficiency, segment:form-information-bottleneck]
rechecked: 2026-10-30T21:22:07Z by Claude Opus 5.5 (item rechecker, t2-todo)
owner: H.2
restated: 'One live depends: 2-cycle (form-strategy-complexity-cost <-> deriv-strategy-cost-regret-bound), where the formulation->appendix edge is a forward pointer. Since vsect binds checks to the depends: chain, such edges are now wrong basis edges, not just lint noise; give forward pointers their own field or drop them.'
---

# `depends:` conflates logical-prerequisite with forward-reference — candidate FORMAT field (gem-hunt 613842 B1/B3; converges with the eq-tag item above and 47291

Imported verbatim (relative links rebased) from `TODO.md` line 264, section *TODO — Miscellaneous & details › Editorial hygiene (standing items)*. Not yet re-checked against HEAD: `vsect recheck item:todo-depends-conflates-logical-prerequisite-w-9868 --outcome holds|stale|landed|not-an-item --why …`.

- **`depends:` conflates logical-prerequisite with forward-reference — candidate FORMAT field (gem-hunt 613842 B1/B3; converges with the eq-tag item above and 472913 GEM 6).** Confirmed a direct mutual 2-cycle in current canon: `#form-strategy-complexity-cost` ⟷ `#deriv-strategy-cost-regret-bound` each list the other in `depends:`. Diagnosis: the appendix→formulation edge is genuinely logical (derives a property *of* the formulation), but the formulation→appendix edge is *motivational/forward-reference* (a formulation pointing forward to its own strengthening appendix, not back to a prerequisite). A second instance: `#def-model-sufficiency` → `#form-information-bottleneck`. The strengthen-first fix is structural, not a patch: a `strengthens:` / `forward-ref:` FORMAT field separating "logical prerequisite" from "where the strengthening lives," which dissolves the spurious cycles, makes the dependency DAG acyclic, keeps every cross-link, and *encodes the strengthen-before-soften architecture structurally*. This is the systematic form of the three converging forward-reference-hygiene findings. Effort: FORMAT.md addition + `bin/lint-outline`/`bin/align-slug` awareness + a sweep to reclassify motivational edges. Worth a focused scoping pass; not urgent (the cycles are benign today). Detail: `audits/.gem-hunt-trail/GEM-WORKING-613842/`.
