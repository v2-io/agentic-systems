# OUTLINE-accepted — accepted-by-design ordering violations (lint-outline whitelist)

This file is tool configuration for `bin/lint-outline`: each table row records one dependency-ordering violation in `OUTLINE.md` that is accepted *by design*, with its grounding. The tool still prints accepted violations (marked ✓, under "ACCEPTED ORDERING VIOLATIONS") but exits green when only accepted violations remain; any ordering violation not listed here stays red. Rows are keyed by the (segment, depends-on) slug pair, so they survive OUTLINE row moves; if a slug is renamed or the violation is otherwise resolved, the row goes stale and the tool reports it as a warning — prune stale rows when you see that warning.

To accept a new violation: add a row with the two slugs, the acceptance date, and a reason grounded in a citable record (CHANGELOG entry, decision memo) — not convenience. The columns are `segment` (the earlier row), `depends-on` (the later row it depends on), `accepted` (date), `reason`.

All rows below are the *introduced-before-used* meta-segment placements: the ten meta-segments relocated to the two Meta-Architecture chapter openings (Part II and Part III) deliberately precede the instance segments their `depends:` lists point at. Record: CHANGELOG 2026-05-25 "Track C: Meta-Architecture Relocation (Introduced Before Used)" + same-day "Track C refinement: two-cluster Part-opening placement"; the discipline originates with Joseph 2026-05-25 ("introduced before used — out of the appendices and into the chapters before they are used") and the Track B 2026-05-22 meta-segments-before-instances landings.

| segment | depends-on | accepted | reason |
| --- | --- | --- | --- |
| disc-identifiability-floor | der-causal-insufficiency-detection | 2026-07-14 | M1 meta-segment at Meta-Architecture I (Part II opening) before its Part II instance segments (CHANGELOG 2026-05-25 Track C) |
| disc-identifiability-floor | der-causal-hierarchy-requirement | 2026-07-14 | M1 meta-segment before its Part II instance segments (CHANGELOG 2026-05-25 Track C) |
| disc-identifiability-floor | der-loop-interventional-access | 2026-07-14 | M1 meta-segment before its Part II instance segments (CHANGELOG 2026-05-25 Track C) |
| disc-value-functional-grounding-floor | form-objective-functional | 2026-07-14 | M1-sister (agent-side) meta-segment before the single-interface commitment segment it names (CHANGELOG 2026-05-25 Track C; Track B 2026-05-22) |
| disc-implementation-impossibility | deriv-strategic-composition | 2026-07-14 | M1-sister (designer-side) meta-segment at Part II opening before its Part III supporting material (CHANGELOG 2026-05-25 Track C; Track B 2026-05-22) |
| disc-separability-pattern | def-strategy-dag | 2026-07-14 | M2 meta-segment at Meta-Architecture I before its instance segments (CHANGELOG 2026-05-25 Track C) |
| disc-separability-pattern | def-value-object | 2026-07-14 | M2 meta-segment before its instance segments (CHANGELOG 2026-05-25 Track C) |
| disc-separability-pattern | der-directed-separation | 2026-07-14 | M2 meta-segment before its instance segments (CHANGELOG 2026-05-25 Track C) |
| disc-separability-pattern | form-composition-closure | 2026-07-14 | M2 meta-segment at Part II opening before its Part III instance segment (CHANGELOG 2026-05-25 Track C) |
| disc-separability-pattern | scope-edge-update-causal-validity | 2026-07-14 | M2 meta-segment before its instance segments (CHANGELOG 2026-05-25 Track C) |
| disc-separability-pattern | def-agent-spectrum | 2026-07-14 | M2 meta-segment before its instance segments (CHANGELOG 2026-05-25 Track C) |
| disc-additive-coordinate-forcing | der-chain-confidence-decay | 2026-07-14 | M3 meta-segment before its first instance in Part II Ch.3 (named explicitly in CHANGELOG 2026-05-25 Track C refinement) |
| disc-modularity-state-dynamics | disc-adversarial-coupling-pressure | 2026-07-14 | M4 meta-segment leads Meta-Architecture II (Part III opening) before its operation legs (CHANGELOG 2026-05-25 Track C refinement) |
| disc-modularity-state-dynamics | disc-strategic-self-coupling | 2026-07-14 | M4 meta-segment before its operation legs (CHANGELOG 2026-05-25 Track C refinement) |
| disc-modularity-state-dynamics | der-class-coercion-via-wrapping | 2026-07-14 | M4 meta-segment before the wrapping construction that develops in the chapters following the Part III opening (CHANGELOG 2026-05-25 Track C refinement) |
| disc-strategic-self-coupling | disc-adversarial-coupling-pressure | 2026-07-14 | M4 operation leg ordered before its sister leg within the Meta-Architecture II unit, matching the record's unit ordering (CHANGELOG 2026-05-25 Track C refinement; 2026-05-24 M4 cycle) |

**Deliberately NOT whitelisted** (stays red until resolved or explicitly accepted by Joseph): `impl-persistence-and-limits` (§I) → `result-per-dimension-persistence` (§III) — recorded in NEXT-UP §6.8 (`spikes/.integrated/NEXT-UP-archived-2026-05-25.md`, "OUTLINE-debt cleanup 2026-05-22") as Gate-1-GENUINE *deferred awaiting Joseph's structural call*, with two candidate resolutions (move the result to Part I, or refactor the chapter-end synthesis); an open structural decision is not an accepted design.
