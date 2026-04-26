# Agency Lift

Segments read in this batch:

- `#scope-adaptive-system`
- `#scope-agency`
- `#def-pearl-causal-hierarchy`
- `#def-causal-information-yield`
- `#form-complete-agent-state`
- `#der-directed-separation`
- `#form-objective-functional`
- `#def-strategy-dimension`
- `#def-value-object`
- `#def-satisfaction-gap`
- `#def-control-regret`

## Predictions vs evidence

The agency-lift structure is stronger and more explicit than I expected.
The framework does not hide its major scope restriction:
Section II is fundamentally modular/Class-1 theory, with Class 2 handled as a later coupled extension.

This batch also resolves part of an earlier concern:
the `a_t = \pi(M_t)` claim in `#der-action-selection` is not an unknown contradiction.
`#form-complete-agent-state` explicitly says that derivation is superseded after the lift to $(M_t, G_t)$.

That moves the likely classification from "theory contradiction" to "integration debt / misleading earlier segment."

## Reassessment of the `#der-action-selection` issue

Current best reading:

1. `#der-action-selection` is valid for Section I adaptive systems whose effective state is exhausted by $M_t$.
2. `#form-complete-agent-state` later narrows and replaces it for purposeful agents.
3. The problem is that the earlier segment is still written as if it were general, while the later segment carries the repair.

Because the repair exists in current `src`, this likely should not be reported as "the framework lacks the distinction."
If reported, it should be framed as:

- **integration debt / first-encounter miscue**
- not
- **missing theoretical resolution**

This is exactly the kind of Phase-2 distinction the audit instructions asked for.

## Cross-segment consistency notes

`#scope-adaptive-system` makes it clear that Section I is broad enough to include passive observers.
That reinforces the earlier point: `#der-action-selection` cannot quietly stand in for all of adaptive scope, because some adaptive-scope systems are passive and some purposeful systems later require $G_t$ explicitly.

`#der-directed-separation` is a major load-bearing segment and is notably honest.
It does not claim universal applicability.
It classifies architectures, names Class 2 as a genuine failure mode, and routes those cases into `03-logogenic-agents/`.

`#def-value-object` is ambitious but mostly disciplined.
It carefully distinguishes:

- exact definitions
- conditional causal-validity claims
- exact monotonicity of continuation conventions

That said, the segment is dense enough that downstream readers could easily remember the clean formula and forget the Class 2 caveat.
This is a general pattern in the framework: the caveats exist, but they are often several paragraphs away from the punchline.

## Strength notes

The satisfaction-gap / control-regret split looks genuinely consequential.
This is one of the clearer places where the framework seems to be offering a real diagnostic architecture rather than merely importing math.

`#form-complete-agent-state` is also unusually good at self-correction.
It directly names which earlier result stops being globally valid after the lift.
That is the kind of explicitness I wish some of the other repaired segments had.

## Predictions for next segments

The likely high-yield part of Section II now looks like:

- strategy-DAG formalization
- observability / edge-update validity
- orient cascade
- strategy-persistence / appendix support

I expect the next meaningful question to be whether the same honesty about Class 1 / 2 scope survives once the theory starts making stronger strategic and compositional claims.
