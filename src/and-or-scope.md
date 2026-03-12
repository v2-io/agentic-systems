---
slug: and-or-scope
type: scope
status: robust-qualitative
depends:
  - strategy-dimension
  - chain-confidence-decay
---

# Scope: AND/OR Combination Scope

We restrict to environments where the causal combination of strategy steps is approximately conjunctive (AND: all parents required) or disjunctive (OR: any parent sufficient), without strong interaction effects between parents.

## Formal Expression

*[Scope Narrowing (and-or-scope)]*

Under this restriction, strategy nodes combine parent contributions via:

**AND-node** (all parents must succeed):

$$P(v \mid \text{parents}) = \prod_{i \in \text{pa}(v)} p_{iv} \cdot P(i)$$

**OR-node** (any parent sufficient):

$$P(v \mid \text{parents}) = 1 - \prod_{i \in \text{pa}(v)} (1 - p_{iv} \cdot P(i))$$

The combination type $\gamma(v) \in \{\text{AND}, \text{OR}\}$ is assigned per node. The causal question determines assignment: "if I remove one parent, can $v$ still be achieved?" YES → OR. NO → AND.

## Epistemic Status

*Robust qualitative.* This scope narrowing converged independently across three formalism attempts (track-a/00, track-a/02, track-a/03). It captures the dominant structure in most planning domains. The excluded case — complementarity, substitutability, interaction effects between parents — requires richer combination rules and is a legitimate divergence point for future work.

The AND/OR restriction with single-parameter edges gives $k$ parameters per node (one per parent edge) instead of $2^k$ for a general conditional probability table. This parsimony is motivated by bounded cognition ( #information-bottleneck): agents with limited representational capacity are forced toward low-parameter models.

## Discussion

**Why AND/OR and not alternatives.**

*Why not Noisy-OR universally.* The first formalism attempt used noisy-OR for all nodes. This **systematically overestimates conjunctive structures**:

| Structure | Noisy-OR | AND | Reality |
|-----------|----------|-----|---------|
| 3 required KRs at $p = 0.95, 0.90, 0.99$ | 0.99995 | 0.846 | ~AND |

The noisy-OR model cannot represent "all of these are required." This was the primary motivation for the AND/OR revision.

*Why not WEIGHTED combination.* A clean-slate formalism (track-a/02) introduced $P(v) = \min(1, \sum \alpha_{iv} \cdot p_{iv} \cdot P(i))$ to handle k-of-n thresholds. This reintroduces a two-parameter estimation problem ($\alpha$ weights per edge). If k-of-n semantics are genuinely needed, nested AND/OR structure can represent them: group alternatives into OR-nodes, then AND the groups. This keeps estimation localized to the node taxonomy rather than spreading it across a new per-edge parameter.

**The parsimony argument.** For binary-outcome nodes, AND and OR form a complete Boolean basis — any Boolean combination can be decomposed into layers of AND/OR (disjunctive/conjunctive normal form). Under bounded cognition, the agent needs the most expressive $O(k)$-parameter representation. AND/OR is the natural candidate. This is a parsimony-motivated hypothesis, not a derived necessity — see `scratch/spike-graph-uniqueness.md` for the full argument and its limitations.

**What this scope excludes.** Environments with strong interaction effects: where the value of combining parent contributions is not separable into independent per-parent terms. Examples: synergistic drug interactions (combined effect exceeds sum of individual effects), complementary goods (neither is useful alone), strategic surprise (the combination of actions matters more than any individual action). These require richer parameterizations within the forced graphical structure ( #strategy-dag) — a direction for future work.

## Working Notes

- The AND/OR assignment per node ($\gamma(v)$) is itself uncertain and should be updateable. A node assumed to be OR (alternatives) might turn out to be AND (all required) when the agent discovers unexpected dependencies. $\gamma$ reclassification is rare — it requires strong structural evidence — and operates on a slower timescale than edge-weight updates.
- The parsimony argument applies cleanly to binary outcomes. For continuous or multi-valued outcomes, AND/OR doesn't have the same completeness properties. The natural continuous analogs might be min (AND) and max (OR), or additive and multiplicative combination. Whether there's a completeness result for these is an open question.
- K-of-n thresholds are genuinely common (e.g., "need at least 3 of 5 team members available"). The nested AND/OR representation works but can be verbose. Whether this verbosity is a problem in practice (given bounded cognition constraints) is empirical.
