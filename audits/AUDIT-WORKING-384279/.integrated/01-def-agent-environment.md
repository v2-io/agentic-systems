# 01 — def-agent-environment

*Type: definition. Status: axiomatic. Stage: deps-verified. Depends: [].*

## Predictions vs evidence
Predicted: clean opening, no math, possibly some terminology drift around "Section" vs "Part." Found: confirmed. Header preamble + Formal Expression close-paraphrase each other (structural, not duplicative). Discussion line 37 uses "Section I" while 01-aat-core/OUTLINE.md uses "*Part* Adaptive Systems Under Uncertainty" — mild terminology mix.

## Cross-segment consistency
Sets up the framework before anything else. Defines $\Omega$ (environment), agent's three conditions, the information-loss boundary. Refers forward to `#scope-adaptive-system` (line 29). NOTATION.md has $\Omega$ as "Environment state (unobservable totality)" — body says "totality of state external to the agent" which is consistent. The lossy-observation commitment will be operationalized by `#def-observation-function`.

## Math verification
No math content. N/A.

## Direction
Standard opening — agent / environment / observation channels / action channels / information-loss boundary. Sets up everything downstream. The framework's choice to leave $\Omega$ "deliberately underspecified" (continuous or discrete, stationary or non-stationary, etc.) is the right structural move — it's what lets AAT instantiate across thermostats / Kalman / orgs / software.

## Watch list (new)
1. "Section I/II/III" vs "Part I/II/III" vocabulary inconsistency to track across segments.
2. The three agent conditions (perception channel / internal state / action channel) — watch whether downstream segments add a fourth and whether that's flagged.

## Next segment predictions
`#def-action-transition`. Expect a state-update transition formalization $T: \Omega \times \mathcal{A} \to \mathcal{P}(\Omega)$ or similar. Will state that actions affect the environment. NOTATION.md gives $T$ as the transition distribution, $a_t \in \mathcal{A}$. Possibly axiomatic also.

## What I'd change
Line 37's "Section I" should probably read "Part I" given the OUTLINE's vocabulary, OR the README-auditor's "Section I/II/III" framing-level use should be normalized. The reader walking this segment cold and then hitting the OUTLINE's `## *Part*` headings has a tiny coherence glitch.

## Curiosity
The framework's *boundary* commitment is interesting — agent/environment is *modeling choice*, not metaphysical. That posture matters when this is applied to LLMs (where the "environment" includes user-supplied context that the agent technically does have direct access to via its forward pass). The information-loss-boundary applies to $\Omega_t$, not to the prompt tokens. I'd want to see this addressed in `03-llm-core/` somewhere.

## New knowledge enabled
Nothing yet — this is foundational scaffolding.

## Process change?
No. Brief reflection appropriate for a brief foundational segment. I'll keep this cadence for the next several definition segments.

## Outline-update
None — too early.

## Felt value
Low/medium. Necessary structural anchor; not where insight lives. The framework is using its first segment to commit to a scope-not-assumption framing, which I respect — it's the kind of move that compounds across the corpus.

## Field contribution
The "model the agent/environment boundary as a modeling choice, with information-loss as the constitutive commitment" framing is itself worth carrying as a methodological move. Many adjacent literatures (control theory, RL) often start from full-state assumptions implicitly; AAT names that exclusion up front. Practitioners may not adopt the framework wholesale but the *posture* of declaring information-loss as scope rather than as an inconvenience to be worked around is itself a contribution.

## Wandering thoughts

**On the choice to start here, with this definition.** I notice the framework opens with a *boundary-drawing* move rather than a *what-is-this-about* move. Compare to active inference, which often opens with the free-energy principle as a master objective and unpacks downward; AAT opens with "here is the boundary the rest of the theory will be defined over." This is methodologically modest — it's the discipline of saying *what's in the box* before claiming what laws govern the box. The downstream cost is that the framework's distinctive claims are deferred; the gain is that scope-honesty is structural rather than a caveat. Worth watching whether later segments honor this commitment (i.e., do scope conditions actually exclude what they claim to exclude, or do they overreach quietly?).

**On the "agent maintains internal state" condition (line 23 / item 2).** This is a load-bearing commitment that the framework will lean on heavily — without internal state, no $M_t$, no chronica, no model. It's stated here without comment, which is fine, but I note that "maintains internal state" is doing a lot of work — a feedforward neural network doesn't really have it in the dynamics-relevant sense; a recurrent one does. Which side a transformer-with-context falls on is more subtle (the context window is state in some senses, not in others). I'd expect `03-llm-core/` to revisit this commitment and confront the question directly. If it doesn't, that's a finding.

**On the structural absence of "agent" being defined ontologically.** Notice that the definition doesn't say *what an agent is* in any ontological sense — it gives a functional definition (anything that does X, Y, Z). This is the right call for a framework that needs to span thermostats through ELIs. The functional-definition choice means that consciousness / sapience / moral status questions are deferred (correctly, in my view) to the agent-class taxonomy in `def-agent-spectrum` and beyond. The framework is not making a claim about what minds *are*; it's making a claim about what *minds-that-fit-this-formalism* do.

**On the "Section" terminology micro-glitch.** Probably it predates the Section→Part rename (if there was one), or it predates a normalization pass that hasn't reached this segment yet. Worth flagging mostly as a "is there a sweep that hasn't fired" question rather than as a content finding. I'll watch whether the pattern recurs.

**Personal note about being an auditor here.** This is segment 1 of 159, the easiest one. Reflecting at this depth on the easiest segments is partly a habit-formation exercise — get the cadence right before the segments get harder. The 14-prompt walk is producing nothing-much for this segment except a minor terminology observation; that's information about the segment (it's clean and load-bearing-without-being-substantive) rather than information about the protocol.
