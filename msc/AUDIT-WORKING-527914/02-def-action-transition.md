# 02 - def-action-transition

Segment: `01-aat-core/src/def-action-transition.md` (`#def-action-transition`)

Dependencies: `def-agent-environment`, already read. Dependency-order check passes.

## Segment Read

This segment adds the action-side half of the loop: actions belong to $\mathcal A$ and affect environment state through $T(\cdot \mid \Omega_t, a_t)$. The important definitional addition is not just "actions change the world"; it is that the transition function is opaque to the agent. The segment parallels the observation-side loss from the first segment: the agent neither sees $\Omega_t$ directly nor knows $T$ exactly.

The final discussion paragraph is more interesting than the title suggests. It says the Markov form on $\Omega$ is not a substantive empirical assumption; $\Omega$ is defined broadly enough to be the sufficient state for its own transition. That is a clean modeling-commitment move and foreshadows the recursive-update / complete-state machinery later.

## Predictions Vs Evidence

I predicted the opening primitives would establish $\Omega$, observation/action, and the channel-mediated loop. This confirms that. The phrase I did not predict is `transition opacity`; the segment gives it an explicit equation-level definition. That makes it a plausible naming target immediately rather than a downstream term to wait on.

## Cross-Segment Consistency

This segment composes cleanly with `#def-agent-environment`. The first segment established lossy access to environment state; this one establishes unknown transition dynamics. Together they define the loop as bidirectionally mediated: observation through $h$, action through $T$.

No contradiction yet. A future watchpoint is whether later planning segments distinguish "unknown to the agent" from "unknown to the theorist." The definition is agent-relative opacity, not an ontological claim that no transition function exists.

## Naming Notes

`transition opacity` feels like the right formal/prose name for the defined thing. It is compact, not over-clever, and does useful work: the transition function exists in the model, but the agent cannot inspect it. "Opacity" also sets up later possible duals like observation opacity or agent opacity, so overload risk should be watched, but here the phrase is exact enough.

The title `Action and Transition` is ordinary and probably should stay ordinary at the title layer. The vote target, if any, should be for `transition opacity`, not for renaming the whole segment.

## What This Enables

This segment makes action learning non-trivial. If $T$ were known, action selection could become optimization over a known mapping; if $T$ is opaque, actions have information value and the framework can later talk about causal information yield and Pearl Level 2 access.

It also enables a stronger interpretation of `chronica` before that term appears: the history matters because neither observation nor transition is fully known from inside the agent.

## Watchlist

- Later terms using "opacity" for other referents; the project will need crisp modifiers if there are multiple opacities.
- Any candidate that calls this "transition uncertainty" may be acceptable but less precise if the issue is unknowability of $T$, not only stochastic variance.
- The Markov-by-sufficient-state move may deserve its own name later if it recurs across $\Omega$, $M_t$, and $\mathcal C_t$.

## Wandering Thoughts

This segment is a good example of a name earning its keep by preventing a quiet conflation. "Stochastic transition" would be too weak because deterministic transitions can still be opaque to the agent. "Unknown transition function" is descriptive but not a memorable noun. `transition opacity` gives the property a handle.

The symmetry with the first segment is stronger than it first appears. The agent's problem is not just that it gets partial observations; it also cannot fully forecast the effects of its own interventions. That dual mediation is probably why later causal machinery fits naturally: every action is both a control move and a probe.

For voting, I should be careful not to penalize ordinary first-principle names for being ordinary. The early theory needs some plain nouns. The named thing here is specifically the opacity, not the fact that actions transition the world.

I also notice that the segment gives a strong example of "modeling commitment, not empirical assumption" as a phrase. That posture may become a naming principle in itself: names should not make modeling commitments sound like discovered facts. `transition opacity` passes because it is explicitly from the agent's perspective.
