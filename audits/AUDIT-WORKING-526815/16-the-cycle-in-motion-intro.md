# 16 - the-cycle-in-motion-intro

Segment: `01-aat-core/src/the-cycle-in-motion-intro.md`
Dependencies: `form-agent-model`, `def-model-sufficiency`, `def-model-class-fitness` - satisfied.
Status observed: `type: discussion`, `status: discussion-grade`, `stage: draft`.
Reference just read by user request: `msc/diagrams-and-comprehension-survey.md`; I used it as diagram-process guidance only.

## Reflection

This intro makes the static-to-dynamic shift clear: once `M_t` is complete retained state, events push it forward, predictions meet observations, mismatch appears, gain weights correction, and tempo aggregates correction capacity. The high-level arc is coherent and the segment is appropriately marked as discussion-grade.

Two things now need watching. First, the intro says recursive update and action-selection are derived from completeness. Recursive update feels strongly derived from `M_t` completeness; action as a function of `M_t` alone may be too strong unless goal/objective or policy state is already included in `M_t`, which Part II later seems to separate as `G_t`. Second, the CIY paragraph explicitly explains why Pearl `do` notation appears before AAT's Pearl hierarchy segment. That is not a hidden-dependency accident; it is an intentional external-vocabulary import. I will keep watching whether local use is self-contained enough.

## Prompt pass

Predictions vs evidence: I expected event dynamics, recursion, action, mismatch, gain, CIY, tempo, and ODE preview. The intro matched the outline closely.

Cross-segment consistency: consistent with `form-agent-model` for epistemic updates. Potential future tension with Part II: "action depends on `M_t` alone" may later need `X_t=(M_t,G_t)` or `a_t=pi(M_t,G_t)` rather than `M_t` alone.

Math verification: no formal verification here. The gain formula is plausible and will need checking in `emp-update-gain`; the ODE ratio is a preview and should be treated as heuristic until later.

Direction next: `form-event-driven-dynamics` should define event times and pre/post update notation. It should bridge chronica's event indexing to continuous time without losing the ordinal/metric distinction.

Errors to watch: action-selection derivation ignoring goals; gain formula being overgeneralized beyond linear-Gaussian or specified uncertainty models; tempo being treated as raw speed without quality/gain.

What I would change: preview action-selection as depending on "complete agent state" or "currently available state" rather than `M_t` alone, unless `M_t` is being used more broadly than epistemic substate in this chapter.

Curiosity: the intro calls adaptive tempo the load-bearing capacity variable; I want to see whether information rate, gain, and event rate are dimensionally coherent later.

New knowledge enabled: I now have a target diagram for the chapter: event arrival -> model update -> prediction/mismatch -> gain -> tempo -> persistence preview.

Audit process change: applying the diagram survey, I parsed this as a sequential process plus bottlenecked conditional chain. A small-multiple/process diagram is better than a single static concept map.

Running outline change: add action-depends-on-M-only watch.

Value feel: medium-high. It is not proof, but it gives a useful map of the next eight segments.

## Diagram thought

Using the survey's workflow: structure type is sequential process; bottleneck is how static model quality becomes dynamic correction capacity; best diagram is a left-to-right pipeline with a feedback loop and one highlighted "capacity synthesis" point at tempo. Minimalism matters: do not include every future theorem, just the process skeleton.
