# 15 — der-recursive-update

Dependencies checked: `form-agent-model` and `form-event-driven-dynamics` already read.
Declared dependency `deriv-recursive-update` is an Appendix derivation not yet read; applying the appendix-back-pointer exception and reading it next.

## Reflection

This segment states the recursive update result:

$$M_{\tau^+}=f_M(M_{\tau^-},e_\tau).$$

It is one of the predicted core results.
The statement is plausible because $M_t$ has been defined as the complete retained epistemic state; anything relevant outside $M_t$ can be folded into $M_t$ by definition.

Status-label tension:
Frontmatter says `status: conditional`, while the Epistemic Status says "Exact, with a partly definitional character."
The segment explains the conditions: temporal ordering, partial observability, and state completeness.
I need the appendix proof before deciding whether the frontmatter should be `exact`, `conditional`, or whether the text should align with `conditional`.

Substantive nuance:
The result is exact only relative to an expanded-enough state.
That is legitimate but close to tautological: any nonrecursive update can be made recursive by redefining the state to include the needed history.
The segment acknowledges this.
The theoretical value is not "all systems are computationally Markovian" but "AAD chooses $M_t$ as the complete retained epistemic state, so updates can be represented recursively."

Between-event dynamics:
The autonomous $g_M(M_\tau)$ addition is useful but seems less derived than the event update.
It assumes between-event evolution depends only on current model state.
That follows from the same completeness convention if all internal resources are part of $M$, but if "model" is narrower than full internal state, it could fail.
This reinforces the need for $M_t$ as complete epistemic substate, not merely a beliefs object.

Cross-segment dependency:
The Discussion invokes `form-consolidation-dynamics` and `schema-strategy-persistence`, both downstream.
This is explanatory and probably not a dependency problem, though it is dense for an early segment.

Prediction for appendix:
`deriv-recursive-update` should show that history-dependent, future-dependent, and non-state-memory update forms are either impossible under temporal order or absorbed into $M_t$ completeness.
I will check whether the proof establishes uniqueness beyond "define state broadly enough."

Running report update:
- Watch status mismatch: `conditional` frontmatter vs "Exact" status paragraph.
