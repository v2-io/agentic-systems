# 02 — def-action-transition

*Type: definition. Status: axiomatic. Stage: deps-verified. Depends: [def-agent-environment].*

## Predictions vs evidence
Predicted: a $T: \Omega \times \mathcal{A} \to \mathcal{P}(\Omega)$-style formalization possibly axiomatic. Found: roughly that — `$\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$` with the (possibly-stochastic) transition function. Includes a *transition opacity* sub-claim (agent does not know $T$ exactly).

## Cross-segment consistency
Forward-refs `#def-observation-function` (line 12) and `#deriv-recursive-update` (lines 16, 45). The latter is correctly disambiguated against the main-section `#der-recursive-update`: line 45 mentions both ("#der-recursive-update" as the Ch.3 segment, "#deriv-recursive-update Constraint C3" as the appendix derivation). Two-slug naming convention is intentional in the codebase (segment + appendix derivation pair). Solid.

## Math verification
One equation: $\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$. Notation-consistent with NOTATION.md ($T$ as transition distribution, $a_t \in \mathcal{A}$). Markov-in-$\Omega$ explicitly flagged as modeling commitment, not empirical assumption — good. No errors possible at this level.

## Direction
Closes the loop $\Omega_t \xrightarrow{h} o_t \to \text{agent} \xrightarrow{a_t} \Omega_{t+1}$ before formalizing observation. Order of presentation: action first, observation second is slightly unusual — typical control-theoretic exposition presents observation first, then action. But the OUTLINE row order has action before observation. May be deliberate — closing-loop framing introduces both channels with the action one already named.

## Watch list (new)
1. **Equation-tag-vs-type taxonomy possible drift.** Line 31 tags *[Definition (transition opacity)]* — but the content ("The agent does not know $T$ exactly") is structurally a *postulate* or *scope* claim under FORMAT.md §`type` ("Definition introduces a quantity, object, or notation"; the opacity claim doesn't introduce an object, it restricts the agent's epistemic access). The segment's umbrella `type: definition` and the equation-tag `*[Definition]*` align with each other but possibly misclassify the opacity claim. Low-severity hypothesis-tier. Watch whether other segments have similar equation-tag-vs-content mismatches.
2. **Parallel Markov-completeness move.** Body claims Markov-of-$\Omega$ and Markov-of-$M_t$ are "independent" parallel moves. I should confirm this independence claim holds when I get to `#der-recursive-update` and especially `#deriv-recursive-update`.

## Next-segment predictions
`#def-observation-function`. Will introduce $h$ formally, $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$, also axiomatic, likely with a similar opacity sub-claim. The pairing with this segment will then close the observation/action duality.

## What I'd change
Line 12's "What makes action non-trivial..." paragraph (in the preamble) is paraphrased by Discussion (line 43). Small structural redundancy. Either tighten the preamble or merge with Discussion. Not finding-worthy, just an observation about the cadence.

## Curiosity
The Markov-of-$\Omega$-as-modeling-choice move is a quietly important methodological commitment. Most adjacent literatures invoke Markov for tractability and treat it as an approximation. AAT inverts this: it *defines* $\Omega$ as whatever is needed to make the dynamics Markov, then carries the "non-Markov environments are absorbed into $\Omega$" framing forward. This is the same move POMDPs make for belief-state, but AAT applies it to the world side rather than the agent side. Cleaner. Question: does this commitment travel cleanly to the multi-agent / composite scope (Part III), where one agent's $\Omega$ contains another agent's $M_t$, $G_t$, $\Sigma_t$? Watch.

## New knowledge enabled
The Markov-by-completeness move at the world-side is a structural inheritance for everything downstream. Without it, $T$ would have to carry a memory of the chronica, which would create circularity when defining the agent's chronica relative to the same world.

## Process change?
No. The 14-prompt walk continues to surface usefully small things even on clean foundational segments. Keeping cadence.

## Outline-update
None substantive yet.

## Felt value
Medium. The Markov-by-completeness move is genuinely a structural choice worth carrying forward. The transition-opacity claim is constitutive for the framework's whole epistemic stance.

## Field contribution
The explicit framing of Markov as modeling commitment rather than empirical assumption is methodologically useful — practitioners often muddle these. Naming it cleanly in foundational segments creates a precedent the framework can lean on later (e.g., when reaching coupled-agent regimes where the Markov-completeness move has to be redone).

## Wandering thoughts

**The "transition opacity" claim at the equation-tag level.** I keep returning to this. The segment's `type: definition` is documenting *what is being introduced*. The equation-tag `*[Definition (transition opacity)]*` reads to me less as a definition of an object and more as a *postulate about the epistemic situation*. FORMAT.md's `postulate` type is exactly "tautological or foundational — cannot be derived, only accepted" which fits this content much better than `definition`. I think the umbrella segment type (definition) is appropriate because the segment as a whole introduces $\mathcal{A}$, $T$, and the transition relation; but the *transition-opacity* atom inside it is a postulate-flavored statement that probably warrants `*[Postulate (transition-opacity)]*` even if the segment type stays as definition. The eq-tag taxonomy in FORMAT.md (line 137-150) allows multiple tags within a segment — `*[Postulate (slug)]*` is on the list. So this is honestly correctable without restructuring the segment.

**On the elegance of opacity as a parallel move.** Lines 12-14 and 37 emphasize that *both* $h$ (observation function) and $T$ (transition function) are opaque to the agent, and that this *joint* opacity is what creates the need for adaptive behavior. If only $h$ were unknown, the agent could plan against a known dynamics; if only $T$ were unknown, the agent could see the world directly but couldn't predict consequences. The framework is making a structural commitment that adaptation under uncertainty requires opacity on both legs of the loop. This is a non-obvious modeling choice — many RL formalisms treat dynamics as the only unknown (model-based / model-free distinction lives there) and tacitly assume full observability. The framework's symmetric opacity is closer to the POMDP-with-unknown-dynamics setting, which is harder but more honest.

**Personal observation on auditing-pace.** I'm finding that each short foundational segment produces about 600-1000 tokens of reflection at the cadence I'm using. At 159 segments that's ~150k tokens of reflections alone, which is fine for 1M context but worth tracking. If I notice cadence-bloat as the segments get richer, I'll dial back to the structural skeleton (predictions / consistency / math / next-segment) and let the wandering-thoughts compress.

**On Markov-as-modeling-commitment, from the agent's PoV.** A thoughtful reader might object: "But the world *is* non-Markov in the messy sense — molecules don't reset between observations." AAT's response is that the *named object* $\Omega$ is by definition the smallest sufficient state. If your $\Omega$ doesn't make dynamics Markov, you've under-named $\Omega$. This is fine for theory; in practice it's a hidden cost because you may need a very large $\Omega$ to make the move work. The framework doesn't owe a discussion of practical $\Omega$-construction here — that's a downstream concern — but somewhere (probably in `02-tst-core/` or `03-llm-core/`) the practical question of $\Omega$-sizing should be addressed. Watch.
