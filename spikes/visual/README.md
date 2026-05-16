# Spike: Visual Design and Diagrammatic Pedagogy for AAT

**Status.** Active. Established 2026-05-15.

**Scope.** How AAT's monograph (and the broader Agentic Systems framework) should design, label, and orchestrate its diagrams, illustrations, and figure portfolio. Investigates: pedagogical principles, audience-calibrated CRA ladders, the *driver-in-snow* as a candidate recurring worked example, and an epistemic-labeling discipline for figures that parallels the framework's existing claim-tag system.

**Predecessor.** Files were scattered across `msc/` (the two surveys, `diagram-catalog-ideation.md`) and `01-aat-core/src/img/` (the early TeX attempts). This spike consolidates them and adds the new working artifacts (`car-as-agent.md`, `epistemic-labeling-schema.md`, `TODO.md`).

## Contents

### Working artifacts (in order of intellectual dependence)

- [`surveys/survey-i.md`](surveys/survey-i.md) — *Diagrams & Illustrations for Accelerated Comprehension: A Principled Survey.* Cognitive-load theory, dual coding, Larkin–Simon, CRA ladder, taxonomy of diagram types, ideation methodology, design heuristics. Foundational.
- [`surveys/survey-ii.md`](surveys/survey-ii.md) — *Diagrams, Illustrations & Concept Maps in Monographs, Textbooks, and Theses: A Focused Survey.* Levin's taxonomy (5 functions), seductive-details effect, monograph-specific constraints (redundancy is condescending; B&W default; expert reader assumed), declarative captions, concept-map evidence base.
- [`catalog-ideation.md`](catalog-ideation.md) — Survey-informed re-catalog of candidate AAT figures, partitioned into 5 tiers by what each figure *buys* (bottleneck-density per slot, not section coverage). Replaces the earlier informal coverage-based catalog.
- [`car-as-agent.md`](car-as-agent.md) — The *driver-in-snow* worked example. Treated as a literal high-level structural instance of AAT, not as a metaphor. Carries (at last count) nine distinct AAT mechanisms in one referent. Candidate recurring worked example across the monograph.
- [`epistemic-labeling-schema.md`](epistemic-labeling-schema.md) — Proposal for figure-level YAML frontmatter and inline tags that parallel the framework's existing claim-tag discipline (`*[Definition]*`, `*[Derived]*`, …). Six axes: Function (Levin), Fidelity, CRA-rung, Role, Status, Dependencies.
- [`TODO.md`](TODO.md) — Actionable next steps. Captures decisions to make, figures to draft, and one Spivak-style monograph-architecture commitment that's currently pending Joseph.

### Attempts (the TikZ/PDF/PNG work to date)

In [`attempts/`](attempts/). Each is at *sketch* or *draft* stage, not camera-ready. The README in each `.tex` file names the segment it would companion if promoted.

- `bathtub-scaffold.{tex,pdf,png}` — 3-rung CRA ladder for persistence (concrete / metaphor / abstract). The two-panel predecessor (concrete / abstract) is preserved in the git history. **Highest-quality v1 of the batch; closest to claims-verified.** v2 work: add a fourth code-as-notation rung per the corrected CRA ladder (`car-as-agent.md` §4-rung).
- `sector-cone.{tex,pdf,svg,png}` — Two-panel control-theoretic figure (1D sector + 2D contraction). **Demonstrated v1-stage failure of the convention-without-teaching pattern** (cf. survey-ii §5.4): correct mathematics, fidelity tier *conventional*, hence Larkin–Simon failure for non-control-theory readers. Diagnostic-useful as a failure case; not a candidate for the monograph as-is.
- `strategy-dag-example.{tex,pdf,png}` — Worked AND/OR DAG with status propagation + numerical verification. Solid v1; edge labels could be tightened.
- `orient-cascade.{tex,pdf,png}` — Five-step cascade with branching at step 3's 2×2 diagnostic. Solid v1 structurally; "done" label collision is the main fix for v2.
- `driver-snow-foundation.{tex,pdf,png}` — First attempt at the driver-in-snow base schematic. **Draft only**; significant layout issues. Translation table column was mislabeled "CS-concrete" — per `car-as-agent.md` §4-rung correction, that rung is *code-as-notation*, not CS concepts.

## Status of findings

What the spike has surfaced so far (in rough order of confidence):

1. **High confidence — the survey-evidenced design moves apply directly.** Levin's three load-bearing functions (organizational / interpretational / transformational), Mayer's spatial contiguity, the seductive-details effect, the visual-literacy-as-prerequisite finding, the monograph-redundancy-is-condescending norm. None of these are project-specific; all of them sharpen AAT's figure portfolio.

2. **High confidence — the sector-cone is the diagnostic-useful failure case.** It demonstrates that *technically correct* and *convention-faithful* are not enough. The fidelity tier *conventional* is a real category; figures in it require visual-literacy teaching alongside.

3. **High confidence — the bathtub-scaffold direction is correct.** Three-rung CRA ladder with spatially-identical re-labeling passes Larkin–Simon. The 4-rung correction (insert *code-as-notation* rung) is a further sharpening, not a redirection.

4. **Medium-high confidence — the driver-in-snow is the right recurring worked example for AAT.** It instantiates persistence, adaptive tempo, deliberation cost, multi-timescale nesting, action-dependent drift, state-dependent capacity, the discrete/continuous duality, and (via the architectural-coupling reading) GUC Class 1/2/3 regimes. Nine mechanisms in one referent. Closest comparable: Spivak's "particle on a line" across Calculus; MacKay's "noisy channel" across ITILA.

5. **Medium confidence — figure-level epistemic labeling is worth adopting.** The six-axis schema in `epistemic-labeling-schema.md` parallels the framework's claim-tag system, would make the figure portfolio auditable, and would prevent convention-without-teaching failures by surfacing them in the metadata. Worth a FORMAT-supplement once the schema settles.

6. **Lower confidence — code-as-notation as a first-class pedagogical rung.** Joseph's corrected 4-rung ladder names *code-as-notation* (variable-named operational notation accessible to any reader with basic programming literacy) as the bridge between conceptual and mathematical. This is a real audience and a real bridge, but the framework hasn't tested it on first-readers yet. Worth carrying as a design commitment with explicit empirical follow-up.

## What this spike does NOT yet do

- It hasn't recruited a sympathetic outside first-reader (the Alan-Walton role from CLAUDE.md). All bottleneck-identification has been internal to me and Joseph. Real comprehension testing remains future work.
- It hasn't produced a camera-ready version of any figure. All `attempts/` are v1.
- It hasn't committed AAT to a specific recurring-worked-example architecture. That decision belongs to Joseph and the monograph-structure cycle.
- It hasn't proved that the epistemic-labeling schema is the right one. The 6-axis proposal is a starting point.

## Pickup notes for future sessions

When picking this up: read `surveys/survey-ii.md` Summary Matrix first (the monograph-redundancy finding is the most actionable single constraint), then `car-as-agent.md`, then `catalog-ideation.md`. The TeX `attempts/` are illustrative artifacts; iteration on them should follow decisions on the spike's open architectural questions, not precede them.
