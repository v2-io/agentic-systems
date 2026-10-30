---
kind: item
provenance: imported
source: spikes/PROPOSED.md:35
section: PROPOSED — the spike-proposal index › Tier 1 — near-term / high-value (repair- or closure-shaped)
owner: ""
opened: 2026-10-30T20:17:42Z
opened-by: Claude Fable 5.1
concerns: [segment:def-action-transition, segment:def-observation-function]
---

# Equation-tag-vs-content-type drift for opacity claims

Imported verbatim (relative links rebased) from `spikes/PROPOSED.md` line 35, section *PROPOSED — the spike-proposal index › Tier 1 — near-term / high-value (repair- or closure-shaped)*. Not yet re-checked against HEAD: `vsect recheck item:spikes-proposed-equation-tag-vs-content-type-drift-for-o-9df0 --outcome holds|stale|landed|not-an-item --why …`.

| 2026-05-28 | Equation-tag-vs-content-type drift for opacity claims | seg:def-action-transition, seg:def-observation-function | Two instances: `#def-action-transition` line 31 tags the "transition opacity" claim (*"The agent does not know $T$ exactly."*) as `*[Definition (transition opacity)]*`; `#def-observation-function` line 31 tags the analogous "epistemic opacity" claim as `*[Definition (epistemic opacity)]*`. Per FORMAT.md `type: definition` = "Introduces a quantity, object, or notation" — but the opacity claims don't introduce an object; they constitutively restrict the agent's epistemic access, which reads more like `*[Postulate]*` or `*[Scope]*`. **Confidence weakened by Gemini cross-audit** (`AUDIT-WORKING-773921/02` + `/03`, 2026-05-28): Gemini did not independently surface this observation, suggesting it may be a Claude-architecture-specific reading rather than a cross-architecture-confirmed concern. Still worth recording as low-priority editorial because the pattern is observable (two instances, structurally similar) and the eq-tag taxonomy is the kind of small thing that compounds in build-pipeline / spec-reading work. Effort: trivial (two eq-tag changes, possibly accompanied by a FORMAT.md note that "Definition" is occasionally used as catch-all for "this introduces structure including constitutive sub-claims"). Defer until a sweep touches those segments for other reasons | proposed | 2026-05-28 | [audit-384279 §D Hypothesis 1] → segments' Working Notes (when touched) |
