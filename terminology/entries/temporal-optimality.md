---
slug: temporal-optimality
schema_version: 1
term: temporal optimality
name: Temporal Optimality
notation:
brief: Among agents achieving identical outcomes on all non-temporal dimensions, the fastest is optimal — time is the uniquely fungible residual.
layer: framing-vocabulary
status: canon
tags: [structural_concepts]
source_type: asf
primary_source: 02-tst-core/src/post-temporal-optimality.md
first_asf_mention: 02-tst-core/src/post-temporal-optimality.md
see_also: [continuous-operation, developer-agent, atomic-changeset, coherence-coupling]
aliases: []
do_not_confuse: []
---

TST's founding normative postulate: when agents $A_1, \ldots, A_n$ achieve outcome $O$ with
identical functional, non-functional, quality, sustainability, and impact-on-others properties,
the optimal agent is $A^* = \arg\min \text{time}(A_k)$.

The equivalence precondition is **load-bearing**. The postulate does *not* say faster is always
better — it says faster is better *given identical outcomes*. Every apparent counterexample
(burnout, "move fast and break things," premature optimization) violates the precondition: they
trade a non-temporal dimension for time, violating the "identical outcomes" clause.

**Why time is special.** Time is uniquely fungible: saved time can be spent on exploration,
learning, rest, or additional action. Saved correctness cannot be spent on anything. Once all
other outcome dimensions are held equal, time is the natural residual to optimize.

The postulate is deliberately tautological in isolation — its structural role is as a
**normative selection rule** that downstream TST claims instantiate. Tempo, gain, persistence,
and adversarial dynamics are consequences of optimizing under this criterion. The full TST
consequence chain is developed in the segments that depend on this postulate.

Stated in [`#post-temporal-optimality`](../../02-tst-core/src/post-temporal-optimality.md).
