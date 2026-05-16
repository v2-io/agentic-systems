# Update / Action Structure

Segments read in this batch:

- `#deriv-recursive-update`
- `#der-recursive-update`
- `#der-action-selection`
- `#der-deliberation-cost`
- `#result-mismatch-decomposition`
- `#result-structural-adaptation-necessity`
- `#der-temporal-nesting`

## Predictions vs evidence

The recursive-update chain is stronger than I expected.
It is unusually honest about the definitional role of completeness and does not pretend the Markov structure was "discovered" rather than induced by the modeling commitment.

The biggest new issue is not in recursive update but in action selection.

## Candidate finding watchpoint: `a_t = π(M_t)` overclaims beyond Section I's honest scope

`#der-action-selection` formally states:

$$a_t = \pi(M_t) \quad \text{or} \quad a_t \sim \pi(\cdot \mid M_t)$$

and its Epistemic Status treats this as derived from `#form-agent-model`'s completeness commitment.

But the same segment's own Discussion later says:

- for actuated agents action selection involves not just $M_t$ but also $G_t = (O_t, \Sigma_t)$
- the policy becomes $\pi(M_t, G_t)$

That is not a small elaboration.
It means the formal expression in this Section I segment is not the general AAD action-selection law; it is at best:

1. a Section I adaptive-tracker special case, or
2. a claim that should have used the complete agent state rather than $M_t$ alone

This matters because the segment currently reads like a general derivation, not a scoped special case.
If Section I's scope includes agents that do have distinct $G_t$ structure, the segment is too strong.
If it is intended only for agents whose complete state is exhausted by $M_t$, that scope needs to be explicit in the Formal Expression and Epistemic Status, not introduced later as a discussion caveat.

This is one of the strongest candidate findings so far.

## Cross-segment consistency notes

`#result-structural-adaptation-necessity` is careful about its alignment assumption and seems honest.
The qualitative result is good even though the exact mismatch-floor mechanism is conditional.

`#der-deliberation-cost` is also well-scoped as conditional on a local deliberation-drift assumption.

`#der-temporal-nesting` and `#deriv-recursive-update` feel more like strengths than liabilities.
They make the framework's architecture more legible rather than less.

## Math / status notes

`#deriv-recursive-update` is a good example of the framework doing epistemic work correctly:

- it separates physical elimination from definitional commitment
- it attacks its own result with counterexamples
- it states exactly what is and is not being proved

`#der-action-selection` does not maintain that same discipline.
The body effectively contains its own narrowing correction, but the formal claim is still presented in broader form than the discussion supports.

## Predictions for next segments

I expect Section II to clarify whether this is:

1. a genuine contradiction left behind in Section I, or
2. an intended special-case lift that was never labeled as such

I also expect the agency-scope and complete-agent-state segments to determine whether `#der-action-selection` becomes a defended finding or dissolves into a scope misunderstanding.
