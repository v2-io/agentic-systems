# 08 — post-causal-structure

*Type: postulate. Status: axiomatic. Stage: deps-verified. Depends: [def-agent-environment, def-chronica].*

## Predictions vs evidence
Predicted: postulate-style causal-irreducibility statement. Found: clean, well-structured postulate: "event $A$ can be a cause of event $B$ only if $A$ temporally precedes $B$." Plus a useful four-tier coupling spectrum (strong/weak/nominal/zero) and "consequences for the feedback loop" enumeration.

## Cross-segment consistency
Forward-refs `#def-pearl-causal-hierarchy`, `#def-mismatch-signal`, `#def-causal-information-yield`, `#scope-adaptive-system`, `#scope-agency` — all reasonably scoped. Crucially: line 38 explicitly addresses the zero-coupling case as "**Outside the agency scope** ( #scope-agency)" — making the prior segment's exclusion criterion operational here.

## Math verification
No equations beyond the postulate statement. Clean.

## Prose-coherence
- "Sections II and III" terminology (line 38). Section/Part pattern continues.
- The four-tier coupling spectrum elegantly maps onto scope-adaptive vs scope-agency: zero coupling drops out of agency. Consistent and clean.

## Watch list
- This segment introduces the "interventional information per action is sparse" framing (line 37) for the nominal-coupling case. Watch whether this framing is carried consistently to `#def-causal-information-yield` and `#der-loop-interventional-access`.

## Next-segment predictions
End of Ch.1 (Coupled Loop). Next chapter "The Reality Model" starts with `#the-reality-model-intro` (Discussion-grade chapter intro). Expect transitional prose introducing $M_t = \phi(\mathcal{C}_t)$ — the compressed-history-as-state framing.

## What I'd change
Nothing structural. This is a strong postulate segment — the four-tier spectrum is pedagogically helpful and the integration with scope-agency / scope-adaptive-system is clean.

## Curiosity
The nominal-coupling case ("agent's choice of what to observe produces distinguishable observation distributions") is a subtle inclusion. It's a Pearl-Level-2 case where the do-intervention is on the observation channel itself, not on the world transition. Scientific instrumentation works this way. Worth tracking whether the framework formally engages query-as-intervention in `#der-loop-interventional-access`.

## Wandering thoughts

**On the postulate-density of Part I Chapter 1.** Ch.1 has — by the OUTLINE table — 8 segments: four definitions, two scopes, two postulates. The framework front-loads its commitments and then derives consequences over Chapters 2-4 and Parts II/III. This is methodologically rigorous: a reader who agrees with the eight Ch.1 segments has agreed to every meta-commitment the framework will lean on. A reader who disagrees with one of them has a clear locus to push back. Strong.

**Causality-by-temporal-precedence as the "most primitive" notion.** This is a meaningful and defensible choice. Reichenbach's principle, Pearl's hierarchy, and Hume's regularity-theory all use stronger notions; AAT picks the weakest commitment that lets the loop have a direction. The cost: AAT's causal claims will live at the do-calculus level (with Pearl as imported machinery) rather than at a metaphysical-causality level. This is the right tradeoff for a framework that wants to apply across substrates without ontological commitment.

**Closing thought on Ch.1.** Eight segments, all internally clean, with two candidate observations: (a) the "Section" terminology drift (corpus-wide, low-severity, §G or editorial), and (b) the post-composition-consistency placement question (medium-severity, project-acknowledged via OUTLINE annotation). I'll keep these alive in the watch list as I continue. The chapter does its job — installs scope, action, observation, history, agency, composition, causality — without going beyond what a postulates-and-scope chapter should.
