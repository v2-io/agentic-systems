# 15 - deriv-recursive-update

Segment: `01-aat-core/src/deriv-recursive-update.md` (`#deriv-recursive-update`)

Dependencies: `form-agent-model`, `form-event-driven-dynamics`, `post-causal-structure`, `scope-adaptive-system`, `def-observation-function`, all read. Dependency-order check passes. This appendix was read immediately after its main-section back-pointer from `#der-recursive-update`; I had already pulled the main segment into context, so this is a small cadence repair rather than the ideal pre-read jump.

## Segment Read

This derivation proves that the recursive update form $M_{\tau^+}=f(M_{\tau^-}, e_\tau)$ is the unique form compatible with three constraints: arrow of time, partial observability, and state completeness. The strongest part is the honesty about C3: state completeness is definitional, not eliminative. If the agent has a replay buffer, the buffer is part of $M$.

The segment includes an information-set / Doob-Dynkin formalization and seven counterexample attacks. The continuous-coupling attack is the main limitation: event-driven updates are a special case, while continuous coupling needs $\dot M = g(M,u)$.

## Predictions Vs Evidence

I expected the appendix to justify recursion via Markov completeness. It does, and more explicitly than I expected. The "What Is Derived vs. What Is Chosen" table is exactly the kind of derivation-audit table FORMAT recommends and is helpful for naming: `recursive update` is a result name, while "state completeness" is the hidden modeling commitment.

## Cross-Segment Consistency

The derivation coheres with the prior segments:

- C1 comes from causal structure.
- C2 comes from adaptive-system partial observability.
- C3 comes from the reality-model formulation.
- Events come from event-driven dynamics.

The main-section `#der-recursive-update` frontmatter dependency on this appendix is an allowed appendix back-pointer. No critical ordering issue.

## Naming Notes

`recursive update` should be kept. It is short, standard, and exactly names the result form. Alternatives like "Markov update" would overemphasize the Markov property and hide the update-function shape.

`Derivation Audit` as a heading convention is validated here. The table is not just bureaucracy; it prevents readers from treating C3 as an empirical discovery. If there is a target for the derivation-audit table heading, this segment strongly supports it.

The phrase `state completeness` is important and should remain visible. It may not need its own vote yet, but it is the key to avoiding overclaim.

## What This Enables

This derivation gives formal backing to update gain, mismatch dynamics, and recursive model-state analysis. It also gives a reusable epistemic pattern: some "results" are exact given a definitional completion move, and the segment should say that rather than perform derivation purity.

## Watchlist

- Any candidate that renames recursive update to something hiding the definitional character of C3.
- Continuous-coupling caveat: future names should not make event-driven digital/sampled systems sound universal.
- Derivation table heading consistency across appendix segments.

## Wandering Thoughts

This is one of the stronger pieces of the early corpus because it attacks itself. The seven counterexamples make the proof feel less like a neat post-hoc derivation and more like a result that survived pressure.

The C3 circularity discussion is especially important. Many theories smuggle completeness into a state variable and then "derive" Markovian structure. This segment says the quiet part explicitly: the Markov structure follows because $M$ is defined as complete. That is not a flaw; it is a modeling commitment with consequences.

For naming, that honesty suggests the ordinary name is best. `Recursive update` is not grandiose. It does not claim novelty over control theory or stochastic processes. It names the update shape and leaves the proof to explain why AAD uses it.

The derivation audit table is also a naming object in its own right. A heading like "What Is Derived vs. What Is Chosen" is long, but it tells the reader exactly what epistemic work the table does. `Derivation audit` is a good compact name for the practice.
