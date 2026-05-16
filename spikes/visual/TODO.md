# TODO — Visual Spike

Actionable next steps. Grouped by category, not strictly ordered (some items depend on Joseph's decisions; flagged as `[Joseph]` where so).

## Architectural decisions pending

- `[Joseph]` **Adopt the driver-in-snow as recurring worked example?** This is a monograph-architecture commitment. If yes: front-matter naming, Findings-brief cross-references, chapter-intro threading. If no: the example remains a Tier-1 anchor for the preamble + persistence chapter only. See [`car-as-agent.md`](car-as-agent.md) §"Threading the example across chapters" for the provisional mapping.
- `[Joseph]` **Adopt the 6-axis epistemic-labeling schema?** Or refine first. See [`epistemic-labeling-schema.md`](epistemic-labeling-schema.md) for the proposal and worked examples on the existing `attempts/`.
- `[Joseph]` **Adopt code-as-notation as a first-class explanatory rung?** This affects FORMAT.md, the chapter-intro disciplines, and the visual style guide. Code-as-notation is continuous with `02-tst-core/` but currently lives there only.

## Figure work (sketch / draft / camera-ready)

### Priority 1 — iterate the highest-leverage figures

- **Bathtub v3 — add the code-as-notation rung.** Current v2 is three panels (concrete / metaphor / abstract). v3 inserts a code-as-notation panel between metaphor and abstract, making the full 4-rung ladder visible. ~30 min of TikZ work.
- **Driver-snow foundation v2.** Layout fixes per critique in main thread:
  - Move translation table below the schematic (vertical stack), so title has room.
  - Drop the speedometer (Levin *decorational*; doesn't earn its slot).
  - Reshape the wiper-dial as a small inset rather than embedded.
  - Spread callout labels to non-overlapping positions.
  - Drop the "winds" stray label.
  - Fix the table column to be *code-as-notation*, not "CS-concrete."

### Priority 2 — fill out the Tier-1 figure set

- **Architecture-class three-panel.** Class 1 / Class 2 / Class 3 panels using the driver-in-snow scenario, each showing the agent's information flow with different coupling levels. This is the *pedagogical breakthrough* from the 2026-05-15 brainstorming and has not yet been visualized. Probably the highest-impact next figure after the bathtub v3.
- **Concept map of the certificate spine + four facets.** The visual companion to `#disc-stability-certificate`. Higher-level than the existing `dep-graph-*.svg`. Not yet sketched.
- **Worked-example panel — persistence in driving.** The persistence inequality $\alpha > \rho/R$ instantiated for the driving case, alongside the bathtub. Probably a small panel rather than a full figure.

### Priority 3 — apply the framework to existing img/

- **Iterate the orient-cascade.** Fix the "done" label collision with the "strategy" outcome box. Reshape step 5's compressed sub-bullets. ~20 min.
- **Iterate the strategy-dag-example.** Tighten edge-label positioning where arrows cross. Optionally compress the right-side legend block. ~15 min.
- **The sector-cone is a deliberate fail-case.** Do not invest further iteration; preserve as a diagnostic-useful artifact. The replacement (concrete contraction-race for first-encounter contexts) is a different figure entirely.

## Schema and tooling

- **Write `FORMAT-FIGURES.md`** (or a §Figures section in `FORMAT.md`) once schema settles.
- **Apply schema retroactively to `attempts/`** as worked-example calibration. Already started in [`epistemic-labeling-schema.md`](epistemic-labeling-schema.md) §Examples.
- **`bin/lint-figures`**. Modeled on `bin/lint-md`. Parses figure-frontmatter YAML, flags missing or invalid metadata, checks `illustrates:` slugs exist. *Low priority until schema adopted.*
- **Decide on retroactive labeling of existing `01-aat-core/src/img/*.svg`.** Recommended: opportunistic only (label when touched for other reasons). The existing figures predate this schema.

## Audience testing

- **Recruit a sympathetic outside first-reader.** The Alan-Walton role from CLAUDE.md. Best done after Bathtub v3 and the Architecture-class three-panel are camera-ready. Test: does the reader arrive at the bathtub conclusion (persistence inequality) before reading the prose? Does the architecture-class three-panel make Class 1/2/3 distinction obvious without prior framework exposure?
- **LLM auditor check on code-as-notation rung.** Run a small audit comparing comprehension of code-rung versions vs. math-rung versions of the same content, across model sizes. Joseph's hypothesis: code-rung is easier for LLMs to track. *Speculative; worth testing.*

## Cross-references to other spikes / project artifacts

- **Updates needed in [`msc/diagram-catalog-ideation.md`](../../msc/diagram-catalog-ideation.md)**: the catalog uses "CS-concrete" terminology that should be replaced with "code-as-notation" per the 2026-05-15 Joseph correction. Either revise in place or note the correction at the top.
- **Update `spikes/INDEX.md`** with a row for this spike (visual / pedagogy). Status: active.
- **Possible cross-link to `02-tst-core/`** — the code-as-notation rung is continuous with TST's substrate. A note in `02-tst-core/OUTLINE.md` Discussion saying "TST's code-substrate also functions as AAT's pedagogical bridge rung at the framing level" is worth considering.

## Open research questions

- **Is "wipers occlude when over-applied" actually a directed-separation violation, or an adjacent action-observation coupling?** The technical claim was sharpened in the main thread but deserves a precise written-up form. Probably belongs in `#der-directed-separation` Discussion or in a new short note. Important for the Architecture-class three-panel figure's accompanying prose.
- **Does the example commit AAT to a specific stance on multi-timescale composition?** The wiper / speed / route nesting is a clean instance of `#der-temporal-nesting`. Should it be the canonical worked example for that section? Confidence: medium-yes.
- **Spivak-precedent writeup.** The Spivak/MacKay "recurring worked example" technique is in `survey-i.md` §3.3 (concreteness fading) and `survey-ii.md` §1.6 (orchestrated as ensemble) but not formalized as a separate practice. A short writeup naming the practice — call it *extended-metaphor architecture* — would be a useful contribution to the visual literature, and worth flagging in `PROPOSALS.md` as an architectural-move candidate for the monograph.
