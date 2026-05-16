# Reflection: #def-model-class-fitness

**Stage:** deps-verified. **Status:** axiomatic. **Type:** definition. **Depends:** [def-model-sufficiency].

## Dependency check

Upstream. ✓

## Predictions vs evidence

Predicted exactly: $\mathcal{F}(\mathcal{M}) = \sup_{M \in \mathcal{M}} S(M)$. Plus the structural inadequacy condition $\mathcal{F}(\mathcal{M}) < 1 - \varepsilon$ as the structural-change trigger. Clean.

## Cross-segment consistency

Forward-ref to `#result-structural-adaptation-necessity` (downstream) is appropriate — the substantive consequence is downstream.

The bias-vs-variance analogy is useful: class fitness = bias ceiling, instance sufficiency = bias + variance.

## Math verification

Standard supremum definition. Well-formed.

## What direction next

`#form-event-driven-dynamics` — the continuous-time event model.

## Errors to watch for

The "agent cannot directly compute $\mathcal{F}(\mathcal{M})$ — would need to search over all models" framing implies a specific operational gap. Whether *any* AAD result requires the agent to know its own class fitness is a worth-watching question. If yes, there's a circularity (need class fitness to detect, can only detect via persistent mismatch which requires the parameter-update process). If no, the segment is fine.

## Predictions for next segments

`#form-event-driven-dynamics`: continuous-time event arrival, event rates $\nu^{(k)}$, event-driven state updates $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$. Probably the substrate for `#def-adaptive-tempo`.

## What would I change

Nothing.

## Curious about

Whether `#form-structural-change-as-parametric-limit` (in §II) treats structural change as a limiting case of parametric change, which would dissolve the bias-variance distinction this segment leans on. If so, the definition's framing of "structural change vs parameter update" needs reconciliation.

## What new knowledge does this enable

Class-level vs instance-level diagnosis: persistent mismatch despite good learning → class fitness ceiling, not estimation problem. Important for the structural-adaptation-necessity result downstream.

## Should the audit process change

No.

## Outline changes for FINAL

No.

## Felt value

**Low magnitude, confirmatory.** Foundation-stone definition with one structural commitment (bias-variance analogy) that I'll watch for downstream consistency.

## What the framework now potentially contributes

The class-vs-instance distinction makes "your model class is wrong" a *first-class diagnostic* rather than a meta-level realization. AAD agents can in principle measure their own class limitations (via persistent-mismatch-despite-learning) and trigger structural change — this is the substrate for adaptive architecture-search behavior in agents.

## Wandering thoughts

The class-vs-instance distinction maps cleanly onto an interesting empirical question for logogenic agents: when an LLM gets things persistently wrong, is it a *parameter problem* (needs more training data, more inference compute, better prompting) or a *class problem* (needs a different architecture, different model size, different objective)? AAD's diagnostic distinction lifts this from "intuitive" to "structural" — the persistent-mismatch-despite-learning signature is in principle measurable.

For the `04-eli-core/` proposed `#norm-honest-activation` ("deceptive prompts mathematically guarantee gain collapse") — if I'm reading the title right, the claim is that lying-to-the-agent breaks the gain mechanism. That would be a class-fitness statement of a sort: the agent's model class (which presumably assumes honest input) is structurally inadequate when input is deceptive. The cleanest formal hook for that claim probably runs through this segment's machinery.

A naming-brainstorm seed: "model class fitness" is fine. "Best achievable sufficiency" is the gloss; "Class-Capacity Ceiling" is more evocative. Tentative.

Continuing.
