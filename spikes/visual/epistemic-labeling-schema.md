# Epistemic Labeling Schema for Figures

**Status.** Proposal. Working artifact. Once adopted, would graduate to `FORMAT-FIGURES.md` or a new §"Figures" in `FORMAT.md`.

**Origin.** Joseph's observation (2026-05-15): the framework already runs rigorous epistemic labeling on its claims (`*[Definition]*`, `*[Derived]*`, `*[Hypothesis]*`, …, with tiers *exact / robust-qualitative / heuristic / conditional* and stages *draft / claims-verified / candidate*). The figure portfolio currently lacks the same discipline. This proposal closes the gap.

## The 6-axis schema

Each figure carries six metadata axes, modeled directly on the segment-level system.

### Axis 1 — Function (Levin, 1987)

What the figure *does* for the reader's comprehension. One of:

- *organizational* — shows structural/spatial relationships among elements
- *interpretational* — clarifies a difficult concept; helps explain an abstract idea
- *transformational* — encodes material in a mnemonic / memorable form for recall

Two further Levin categories — *decorational* and *representational* — are not load-bearing per the survey-ii §1.3 / §1.4 evidence (the seductive-details effect). Any figure that would carry one of these labels should be redesigned to earn one of the three above, or removed.

### Axis 2 — Structural fidelity

The figure-analog of claim tiers. Four levels:

- *exact* — every visible structural relationship is mathematically required by the formalism. Perturbing the picture predicts a perturbation of the formalism. Examples: commutative diagrams in category theory; the strategy DAG's AND/OR propagation when worked numerics are shown.
- *robust-qualitative* — captures the right shape; specific quantitative details are illustrative. Examples: phase portraits with example trajectories; Lyapunov sublevel sets drawn as schematic ellipses.
- *heuristic* — useful for intuition; some perturbations do not track the formalism. Often arises when a higher-dimensional or topological constraint is rendered in 2D. Example: the 2D rendering of a half-plane sector-condition constraint as a wedge.
- *conventional* — requires reader to know a domain-specific reading convention. Example: classical sector-plot from absolute-stability theory. *Triggers a visual-literacy-prerequisite check* (Axis 6).

### Axis 3 — CRA rung

Which abstraction level the figure primarily speaks to. One of (per the corrected 4-rung ladder from `car-as-agent.md`):

- *universal-concrete* — physical phenomena from lived experience
- *code-as-notation* — variable-named operational notation
- *conceptual* — AAT plain-English vocabulary
- *mathematical* — formal symbols
- *multi-rung* — explicitly carries multiple rungs in one figure (the bathtub-scaffold is multi-rung)

### Axis 4 — Role

What the figure does in the argumentative structure:

- *anchor* — carries a mental model into a chapter or section (preamble figures; the driver-snow foundation)
- *worked-example* — instantiates the formalism on a concrete case (the strategy DAG example with numerics)
- *architecture* — shows structural relationships among parts (block diagrams; Class 1/2/3 panels; the directed-separation three-block)
- *concept-map* — navigational; shows how concepts relate (the existing dep-graphs are dependency analogs; concept maps would be the sibling)
- *proof-aid* — makes a step in a derivation perceptible (annotated commutative diagrams; the sector-condition Lyapunov-sublevel-set figure as proof-aid)
- *diagnostic* — lets the reader verify their own understanding (worked-numerics figures)

### Axis 5 — Status / stage

Parallels segment stages:

*sketch* → *draft* → *claims-verified* → *camera-ready*

Where *claims-verified* means: the figure matches what the cited claim actually says (analog of the segment claims-verified stage). *Camera-ready* is the final monograph-ready form.

### Axis 6 — Dependencies

Like segment `depends:`. The figure declares which claim slugs it illustrates and which other figures it builds on. The build pipeline can then enforce consistency: if a cited claim's content changes, the figure flagged for re-review.

Sub-fields:

- `illustrates:` — list of claim slugs the figure is designed to support
- `companion-of:` — list of segments where the figure is intended to live
- `builds-on:` — list of other figure slugs the figure depends on (e.g., chapter-anchor figures that subsequent chapter figures re-annotate)
- `visual-literacy-prereqs:` — required when *fidelity = conventional*. Lists the conventions the figure assumes and where they should be taught.

## YAML frontmatter

A figure file (`.tex` or `.svg` companion file) carries a `.figure.yml` next to it (or YAML frontmatter in a comment header). Worked examples:

### Example 1 — bathtub-scaffold

```yaml
slug: bathtub-scaffold
function: interpretational
fidelity: robust-qualitative
cra-rung: multi-rung
role: anchor
illustrates:
  - result-persistence-condition
  - deriv-sector-condition
  - disc-stability-certificate
companion-of:
  - aat-preamble
  - persistence-and-limits-intro
honesty-notes: |
  The drain-as-correction analog is structurally isomorphic when the
  correction rate is approximately linear in mismatch (within the sector
  condition's validity regime, ||delta|| <= R). Outside that regime the
  analog is schematic, not literal. Bathtub geometry does not encode the
  vector character of multi-dimensional mismatch — it captures the
  scalar persistence inequality only.
status: claims-verified
stage: draft
```

### Example 2 — sector-cone (the diagnostic-useful failure case)

```yaml
slug: sector-cone
function: representational      # NOTE: fails the load-bearing check
fidelity: conventional
cra-rung: mathematical
role: proof-aid
illustrates:
  - result-sector-condition-stability
  - deriv-sector-condition
visual-literacy-prereqs:
  - absolute-stability sector plot (Khalil / Vidyasagar)
  - Lyapunov sublevel sets with ultimate-bound interpretation
honesty-notes: |
  The 2D rendering of a one-sided sector renders an unbounded
  half-plane as a wedge. The "envelope" intuition naturally read by
  the reader is incorrect — the wedge has no upper boundary slope.
  Conventional fidelity means the reader must already know the sector-
  condition convention to read this figure correctly. The figure FAILS
  the load-bearing check (function = representational) — replace
  with a concrete-anchored contraction-race for first-encounter
  contexts; retain only in the appendix for already-expert readers.
status: draft
stage: sketch
```

The `sector-cone` example is what the schema is *for*: surfacing the issues that motivated `car-as-agent.md` in the first place, in the figure's own metadata, so they don't have to be re-discovered each time.

### Example 3 — strategy-dag-example

```yaml
slug: strategy-dag-example
function: interpretational
fidelity: exact
cra-rung: mathematical
role: worked-example
illustrates:
  - def-strategy-dag
companion-of:
  - strategy-structure-intro
  - def-strategy-dag
honesty-notes: |
  Worked numerics let the reader verify status propagation directly.
  The AND/OR semantics map to the propagation formulas exactly. The
  particular choice of "Get to airport on time" is a CRA-(a) anchor;
  any plan-structured task with capability uncertainty would work.
status: claims-verified
stage: draft
```

### Example 4 — orient-cascade

```yaml
slug: orient-cascade
function: organizational
fidelity: exact
cra-rung: mathematical
role: architecture
illustrates:
  - der-orient-cascade
  - def-satisfaction-gap
  - def-control-regret
companion-of:
  - der-orient-cascade
honesty-notes: |
  Flowchart structure is exact to the cascade's derived sequential
  order. The 2x2 diagnostic at step 3 maps to the four-case
  decomposition in #der-orient-cascade. Sub-steps 4a/4b/4c and
  5a/5b/5c/5d are compressed for figure-readability; the segment
  carries the full structure.
status: claims-verified
stage: draft
```

## Inline tag (for captions)

Analog of the segment-level equation tags. Appears in the figure caption when the figure is first referenced:

> *[Figure: interpretational; fidelity robust-qualitative; rung multi-rung; role anchor]*

Short-form alternative for inline use:

> *[Fig. interp / robust-qual / multi-rung / anchor]*

The full YAML lives next to the source; the inline tag is a reading convenience.

## Benefits

**Forces honest commitment per figure.** Authors must name what each figure does and how literally to read it. The sector-cone v1 would have been flagged at design time (function = representational + fidelity = conventional → both red flags), not at user-feedback time.

**Makes the catalog rubric audit-driven.** `catalog-ideation.md` partitions figures into 5 tiers by what each buys. Each tier corresponds to specific epistemic constraints:
- *Tier 1 (load-bearing comprehension)*: function ∈ {interpretational, transformational}; fidelity ∈ {exact, robust-qualitative}; role ∈ {anchor, worked-example}.
- *Tier 5 (deferrable / don't draw)*: function ∈ {decorational, representational} OR fidelity = conventional without visual-literacy-prereqs taught.

This makes the catalog mechanizable rather than aspirational.

**Prevents convention failures.** Any figure with `fidelity: conventional` triggers a visual-literacy-prerequisite check (survey-ii §5.4): does the surrounding prose teach the convention before deploying it? If not, the convention is undefined for the reader.

**Build-pipeline figure-claim consistency.** A figure declaring `illustrates: [#result-persistence-condition]` can be marked stale if that claim's status changes (parallel to the cross-segment dependency machinery in `bin/`).

**Auditor-safe handling.** Like the rest of the framework's claim-grade discipline, figure-grade discipline lets a de-novo auditor distinguish "this figure makes a literal mathematical claim" from "this figure is an intuition-builder" without re-reading the surrounding prose. The labels are stable; the prose is not.

## Open questions

1. **Where does this discipline live?** Options: (a) extend `FORMAT.md` with a §Figures section; (b) sibling file `FORMAT-FIGURES.md`; (c) inline in each `.tex` file. Recommend (b) once the schema settles.

2. **Tooling.** Should the build pipeline parse the YAML frontmatter and surface inconsistencies (e.g., figure cites a claim that doesn't exist; status mismatch)? This is parallel to `bin/lint-md` and would be valuable, but not blocking.

3. **Migration discipline.** Should existing figures (`agent-environment.svg`, `agent-spectrum.svg`, `chain-confidence-decay.svg`, etc. in `01-aat-core/src/img/`) be back-labeled? They predate this schema. Recommend: label opportunistically when a figure is touched for other reasons; don't run a sweep.

4. **Companion-of semantics.** A figure can companion *multiple* segments (the bathtub-scaffold companions the preamble *and* `#result-persistence-condition`). Is there a primary-companion notion, or are they all equal? Recommend: equal, but the first listed is the "first-encounter" segment.

5. **Stage vocabulary.** Does *claims-verified* mean "I checked the figure against the claim" or "an external reviewer checked"? Recommend the former (parallel to segment-level discipline) with the latter being a separate metadata field (`reviewed-by:` if needed).

## Pickup notes

To advance this schema:

1. Joseph commits or refines the 6 axes.
2. Write `FORMAT-FIGURES.md` (or §Figures in FORMAT.md) with the schema as canonical.
3. Apply the schema retroactively to the `attempts/` in this spike as worked examples.
4. Decide on tooling: at minimum, `bin/lint-figures` that flags missing or invalid frontmatter.
5. Decide on retroactive labeling of existing img/ figures (recommended: opportunistic, not sweep).
