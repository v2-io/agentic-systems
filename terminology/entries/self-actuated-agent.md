---
slug: self-actuated-agent
schema_version: 1
term: self-actuated agent
name: Self-actuated agent
brief: Actuated agent + sets own $O_t$ — goal autonomy, not just solution autonomy.
layer: framing-vocabulary
status: canon
tags: [agent_classes]
source_type: asf
primary_source: 01-aat-core/src/der-orient-cascade.md
first_asf_mention: 01-aat-core/src/der-orient-cascade.md
see_also: [actuated-agent, logogenic-agent, eli]
aliases: []
do_not_confuse: []
---

An [actuated agent](actuated-agent.md) that revises its own objective $O_t$,
not only its strategy $\Sigma_t$ for reaching a given objective — goal autonomy
on top of solution autonomy. The self-actuation operator — the internalization
of the orient cascade's terminal $O_t$-revision branch — is formalized in
`#deriv-self-actuation-grounding`, which also establishes (as a conditional,
scoped no-go) that a non-degenerate self-actuator cannot ground its
objective-revision on an agent-internal objective and must instead ground on a
non-objective terminal invariant — canonically, the persistence bound.
