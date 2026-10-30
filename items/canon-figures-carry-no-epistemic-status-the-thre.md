---
kind: item
owner: H.3
opened: 2026-10-30T23:25:28Z
opened-by: Claude Opus 5.5 (spike drain fork D)
concerns: [segment:persistence-and-limits-intro, segment:strategy-structure-intro, segment:impl-orient-cascade]
---

# Canon figures carry no epistemic status: the three visual-spike figures now embedded in Part I segments (bathtub scaffold, strategy-DAG example, orient cascade) have captions that say what they show but not whether the picture is isomorphic to the formalism or only illustrative. Decide the figure discipline on the merits (spikes/visual/ proposes a six-axis schema; the minimum is a tier and an isomorphic/illustrative mark per figure) and test the pedagogy it serves with fresh readers.

Checked at cbd2f345: `01-aat-core/src/img/{bathtub-scaffold,strategy-dag-example,orient-cascade}.tex` are byte-identical to `spikes/visual/attempts/`, and are embedded at #persistence-and-limits-intro :36, #strategy-structure-intro :42 and #impl-orient-cascade :25; `driver-snow-foundation.tex` in `img/` is a later version than the spike's and is embedded in no segment, only at `01-aat-core/OUTLINE.md` :12, whose caption also calls it "the worked AAT instance recurring across Part I and beyond". No caption states a tier.

Source: `spikes/visual/` (README, TODO, `epistemic-labeling-schema.md`, `car-as-agent.md`, `catalog-ideation.md`, `surveys/survey-i.md`, `survey-ii.md`). Three decisions its TODO leaves "[Joseph]", which this effort resolves on the merits:

1. *Figure epistemic discipline.* The spike's six axes (Levin function, fidelity, concreteness rung, role, status, dependencies) may be more than is needed. The part the project's own rule demands is smaller: "the analog must be isomorphic, not merely evocative" (asf `CLAUDE.md`, respectful pedagogy). So each figure needs (a) the tier of what it depicts, the same as its home's, and (b) whether a reader who perturbs the picture gets predictions that hold. The spike's sector-cone attempt is its worked failure case: correct mathematics, conventional fidelity, opaque to readers without control theory (README findings 1–2). This arguably belongs under B (claims say what kind of claim they are) as much as H; no KR names figures today.
2. *The driver-in-snow as a recurring worked example.* Unadopted: it is in no segment, while INTRODUCTION :60 and the OUTLINE :13 caption say it "recurs across the chapters" (already item:influx-intro-anchor-sentences-outrun-bodies). Either thread it, which is real authoring with `car-as-agent.md`'s nine-mechanism mapping as the start, or drop the sentence. Its open technical question bears on any threading: whether over-applied wipers occluding the view is a directed-separation violation or an action-observation coupling (TODO "Open research questions"); audits 731548 (`10-form-agent-model.md`, `18-der-action-selection.md`, `19-def-mismatch-signal.md`) use the same example.
3. *Code-as-notation as a fourth explanatory rung.* A hypothesis about readers (including LLM readers), which H.3's fresh-reader measurement is the way to test, not a FORMAT decision to make first.

Set aside in the same directory, with reasons: `attempts/` duplicates canon `img/` (four files identical, the fifth superseded); `diagram-catalog-ideation.md` is byte-identical to `catalog-ideation.md`; the README and TODO link `msc/diagram-catalog-ideation.md` and `msc/diagrams-and-comprehension-survey.md`, which no longer exist. Related tooling item: item:todo-figure-artifact-drift-committed-pdf-prev-a1b6 (I.6), whose `bin/lint-figures` is the same tool the spike's TODO proposes for schema checks.
