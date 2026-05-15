# 17 - der-action-selection

Segment: `01-aat-core/src/der-action-selection.md` (`#der-action-selection`)

Dependencies: `form-agent-model`, `der-recursive-update`, both read. Dependency-order check passes.

## Segment Read

This segment derives action selection from complete internal state: under Section I, $a_t=\pi(M_t)$ or $a_t\sim\pi(\cdot\mid M_t)$; under Section II, the same completeness argument lifts to $\pi(M_t,G_t)$. The formal result is simple. The richer discussion introduces action fluency: the degree to which effective praxis flows from the model without deliberation.

The implicit/explicit distinction is valuable: action may be model-embedded and cheap, or deliberative and simulation-heavy. Fluency is distinct from model sufficiency.

## Predictions Vs Evidence

I expected action selection to follow from model completeness. That is confirmed. I did not expect `action fluency` to appear this early, but it is a natural name for a qualitative concept that will matter in deliberation-cost and TST contexts.

## Cross-Segment Consistency

The segment extends `#form-agent-model` and `#der-recursive-update` cleanly. It uses Pearl Level 2 reasoning for deliberation, which I have read. It also forward-references Section II's $G_t$ and directed separation; those are framed as lifts, not needed for the Section I result.

No contradiction. Status is exact for the policy form and discussion-grade for fluency; the segment says so clearly.

## Naming Notes

`action selection` is accurate but generic. It is the standard name for $\pi$ mapping state to action, and should probably be kept.

`policy` should remain the formal name for $\pi`; no AAD-specific replacement needed.

`action fluency` is strong. It captures the qualitative phenomenon better than "implicit action" alone because it names a degree, not a binary mode. It also travels well to software development: familiar code and known patterns enable fluent action.

`praxis` appears as the cycle phase for informed action; as with epistrophe, I should wait for the phase vocabulary target.

## What This Enables

This enables deliberation cost, exploit/explore/deliberate tradeoffs, strategic planning, and the coupling of $M_t$/$G_t$ through action. It gives a formal basis for talking about faster implicit action as adaptive advantage.

For naming, it separates:

- `action selection`: policy form
- `praxis`: cycle phase
- `action fluency`: qualitative property of cheap effective action

Those should not be conflated.

## Watchlist

- Candidates that rename `action fluency` as reflex/intuition only; the segment's scope is broader.
- Deliberation terms that imply explicit reasoning is always better; the persistence condition penalizes slow action.
- Section II action-selection names should include $G_t$ once purposeful state is defined.

## Wandering Thoughts

This segment is a good example of a formal result with a more interesting qualitative consequence. The equation $a=\pi(M)$ is unsurprising. The idea that action-generating capacity can become embedded in the model, making effective action cheap, is much more generative.

`Action fluency` feels like a name that could survive outside the paper. A software developer has high action fluency in a familiar codebase; a martial artist has it in trained movement; a team has it in standard operating procedures. It is not merely speed, because the action must remain effective.

The model sufficiency distinction matters. Knowing a lot about the world is not the same as being able to act well without computation. Chess is the obvious example, but software has the same shape: knowing what the system does does not mean knowing the safe change immediately.

For voting, I should protect `action fluency` if it is targeted. It names a real slot.
