---
slug: temporal-optimality
type: axiom
status: first-principled
depends: []
---

# Temporal Optimality

Among agents achieving identical outcomes across all non-temporal dimensions,
the one requiring least time is optimal.

## Formal Expression

*[Axiom (temporal-optimality)]*

Let $\mathbf{A} = \{A_1, A_2, \ldots, A_n\}$ be agents or strategies achieving
outcome $O$.

$$\text{If } \forall m \in \mathbf{M} \setminus \{\text{time}\},\; \forall i,j:\; m(A_i) \equiv m(A_j), \quad \text{then } A^* = \arg\min_{A_k} \text{time}(A_k)$$

where $\mathbf{M}$ is the set of all measurable outcome dimensions, and
identical outcomes $m(A_i) \equiv m(A_j)$ means equivalence across:
- **Functional**: Same input→output mappings
- **Non-functional**: Same performance, security, availability
- **Quality**: Same defect probability, maintainability
- **Sustainability**: Same impact on agent capacity and system evolution
- **Impact on others**: Same effect on other agents' capacity

## Epistemic Status

This is an axiom — deliberately tautological. The statement reduces to: "given
a choice between identical outcomes, the one that arrives sooner is preferred."
The inability to construct genuine counterexamples without violating the
equivalence precondition reveals its axiomatic nature. The fungibility argument
(below) is *discussion* — a qualitative observation about why time is a natural
optimization target, not a derived result.

## Discussion

**Why time is special.** Time is uniquely fungible among outcome dimensions:
saved time can become exploration, learning, rest, additional action — anything.
Other outcome dimensions (correctness, safety, quality) are not fungible in this
way. A unit of saved correctness cannot be spent on learning. This is why, once
all other outcome dimensions are held equal, time is the natural residual to
optimize. The axiom makes this optimization explicit.

**The equivalence precondition is load-bearing.** The phrase "identical outcomes
across all non-temporal dimensions" is doing most of the work. It must be
verified concretely before the axiom applies. Apparent counterexamples
invariably violate it:
- "Move fast and break things" — violates quality equivalence
- Burnout-inducing speed — violates sustainability equivalence
- Premature optimization for unlikely futures — optimizes for a counterfactual
  outcome, violating actual-outcome equivalence
- Skipping tests for speed — violates defect probability equivalence

The axiom does not say faster is always better. It says faster is better *given
identical outcomes*. An agent that achieves a worse outcome faster is not
preferred by this axiom. Misapplication of temporal optimality without verifying
the equivalence precondition produces exactly the pathologies listed above.

**Why start here.** The adaptive machinery that follows — tempo, gain,
persistence, adversarial dynamics — can be understood as consequences of
optimizing for this criterion under constraints of partial observability,
bounded resources, and environmental change. The connections are developed in
their respective claims; they are not implied by this axiom alone.

**Domain generality.** This axiom applies to any agent-environment pairing
within ACT's scope (#scope-condition). In the software domain, it specializes
to the statement that among implementations achieving identical outcomes, the
one requiring least development time is optimal (TST T-01). The generalization
is straightforward: replace "implementation" with "adaptive strategy."

## Scope Limitation

This axiom does not, by itself, say anything about *how* to achieve temporal
optimality. That is the subject of the rest of the theory.
