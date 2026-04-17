# Alternative: AND/OR Intent DAG

**Status**: Design exploration. Alternative to the noisy-OR formulation in 00-intent-dag-formalism.md.
**Date**: March 2026
**Depends on**: 00-intent-dag-formalism.md, TF-06 (gain/uncertainty ratio), 03-goal-formalism-sketch.md

> The noisy-OR combination rule (00, Section 1.2) handles disjunctive causes
> well but conjunctive causes badly. Many real strategies have conjunctive
> structure: "the feature works only if BOTH the backend AND the frontend are
> implemented." This document develops an AND/OR DAG variant that handles
> both naturally.

---

## 0. The Problem with Noisy-OR

The base formalism (00, Definition 1.5) computes the expected contribution
to node j from its parents as:

    P(j achieved) = 1 - product_{i in parents(j)} (1 - p_ij * theta_ij)

This is a noisy-OR: each parent independently has a chance of causing j,
and j is achieved if ANY parent's contribution succeeds. It encodes:

    "Any one of my parents can get me there."

This works when any parent suffices (e.g., alternative initiatives for a KR).
But it fails for AND-structured sub-goals:

    Objective: "Users can authenticate via OAuth"
        <- KR1: "Token flow works"      (p = 0.95)
        <- KR2: "Sessions persist"       (p = 0.90)
        <- KR3: "Existing auth intact"   (p = 0.99)

All three KRs are REQUIRED. The objective is not achieved if any one fails.
Noisy-OR gives P(O) = 1 - (0.05)(0.10)(0.01) = 0.99995, which is absurd --
it treats each KR as an independent sufficient cause. The correct computation
is P(O) = 0.95 * 0.90 * 0.99 = 0.846, the conjunction.

The noisy-OR formulation from 00 systematically overestimates the
achievement probability of conjunctive nodes. This is not a minor issue.
Most real objectives require ALL their key results, not ANY of them.

---

## 1. Formal Definitions

### 1.1 Node Combination Type

**Definition 1.1 (Combination type).** Each non-source node v in V carries
a combination type:

    gamma(v) in {AND, OR}

- **AND-node**: v is achieved only if ALL parent contributions succeed.
  Represents conjunctive requirements.
- **OR-node**: v is achieved if ANY parent contribution succeeds.
  Represents disjunctive alternatives.

The combination type is a property of the node, not the edge. It answers:
"given that my parents have various probabilities of contributing to me,
how do those contributions combine?"

### 1.2 Extended Intent DAG

**Definition 1.2 (AND/OR Intent DAG).** The agent's intent at time t is:

    G_t = (V_t, E_t, w_t, tau_t, gamma_t)

where V_t, E_t, w_t, tau_t are as in 00 (Definition 1.6), and:
- gamma_t : V_t -> {AND, OR, LEAF} assigns a combination type to each node
- LEAF is assigned to source nodes (no parents); AND and OR to all others

**Edge weights simplify.** With explicit AND/OR structure, the
two-parameter weight (p, theta) from 00 reduces to a single p_ij.
Theta was partly compensating for noisy-OR's inability to express
"all siblings are also needed." With AND/OR nodes, that structural
requirement is explicit, and p_ij alone carries the causal confidence:

    w(i, j) = p_ij = P(i's contribution to j succeeds | do(i), M_t)

### 1.3 Structural Constraints (Revised)

The five constraints from 00 (Section 1.3) hold unchanged, plus:

6. **Combination type consistency**: Objective nodes with multiple KR
   children are typically AND-nodes (all KRs needed). KR nodes with
   multiple initiative parents are typically OR-nodes (any initiative
   suffices). This is the DEFAULT assignment; specific domains may
   override it.

7. **Homogeneous parent sets**: All parents of an AND-node should
   represent contributions of the same logical kind (co-required
   components). All parents of an OR-node should represent
   alternative approaches to the same sub-goal. Mixed sets --
   where some parents are co-required and others are alternatives --
   indicate the node should be decomposed into an AND-node with
   OR-node children (see Section 1.4).

---

## 2. Achievement Probability Propagation

### 2.1 Base Cases

For a source node (action or observable) v:

    P(v achieved) = p_v

where p_v is the agent's confidence that this action can be executed
or this observation obtained. For actions already executed, p_v updates
toward 0 or 1 based on the outcome.

### 2.2 OR-Node Propagation

For an OR-node v with parents {u_1, ..., u_k}:

    P(v achieved) = 1 - product_{i=1}^{k} (1 - p_{u_i, v} * P(u_i achieved))

The noisy-OR, unchanged. Each parent independently offers a chance.

### 2.3 AND-Node Propagation

For an AND-node v with parents {u_1, ..., u_k}:

    P(v achieved) = product_{i=1}^{k} p_{u_i, v} * P(u_i achieved)

Every parent must contribute. The conjunction under independence.

### 2.4 Recursive Propagation

Achievement probability propagates bottom-up through the DAG via
topological sort. For each node v in topological order:

    P(v) = cases:
        p_v                                                 if v is a source
        1 - prod_i (1 - p_{u_i,v} * P(u_i))               if gamma(v) = OR
        prod_i (p_{u_i,v} * P(u_i))                        if gamma(v) = AND

This is computable in O(|V| + |E|) time, same as the noisy-OR-only
version.

### 2.5 Example: OAuth Objective (Corrected)

Using the OKR example from 00 (Section 5.3), now with AND/OR types:

    Objective O [AND-node]:
        <- KR1 [OR-node]:  p_{KR1,O} = 0.95
            <- Init A:     p_{A,KR1} = 0.80
            <- Init B:     p_{B,KR1} = 0.60
        <- KR2 [LEAF]:     p_{KR2,O} = 0.90
            <- Init C:     p_{C,KR2} = 0.85
        <- KR3 [LEAF]:     p_{KR3,O} = 0.99

Propagation:

    P(KR1) = 1 - (1 - 0.80)(1 - 0.60) = 0.92     [OR: either initiative]
    P(KR2) = 0.85                                   [single parent]
    P(KR3) = direct observation, ≈ 1.0              [monitoring KR]

    P(O) = (0.95 * 0.92) * (0.90 * 0.85) * (0.99 * 1.0)
         = 0.874 * 0.765 * 0.990
         = 0.662

Compare:
- Noisy-OR everywhere: P(O) ≈ 0.9999 (absurd overestimate)
- AND/OR: P(O) = 0.662 (realistic -- three uncertain dependencies
  compound multiplicatively)

The AND/OR model correctly captures that requiring three things is
harder than requiring any one of them.

---

## 3. Edge Weight Updates

### 3.1 The Update Rule

Edge weights update identically to 00 (Section 2.1):

    p_ij^{new} = p_ij^{old} + eta_edge * (signal - p_ij^{old})
    eta_edge = U_edge / (U_edge + U_obs)

TFT's uncertainty ratio, unchanged. What differs is the downstream
IMPLICATION of the update.

### 3.2 Asymmetric Impact of Updates

**Key difference from the noisy-OR-only model**: the same edge weight
change has very different impact depending on the child's combination type.

For an OR-node with k parents, all at confidence p:

    P(OR) = 1 - (1-p)^k

    dP(OR)/dp_i = (1-p)^{k-1}      [diminishing marginal value]

For an AND-node with k parents, all at confidence p:

    P(AND) = p^k

    dP(AND)/dp_i = k * p^{k-1}     [large when p is high, devastating when low]

Implications:

- **Improving the weakest link matters more for AND-nodes.** If one
  parent of an AND-node has low confidence, the entire node is bottlenecked.
  Raising that one edge has outsized impact. This is the "chain is only as
  strong as its weakest link" principle, now derived rather than aphoristic.

- **Adding redundancy matters more for OR-nodes.** Adding a new parent
  to an OR-node raises its probability by (1-P_current) * p_new. For an
  AND-node, adding a required parent LOWERS the probability by a factor
  of p_new. More requirements means harder, not easier.

- **The agent should invest observation budget differently.** Edges
  feeding AND-nodes should be tested preferentially (because a failure
  anywhere kills the conjunction). Edges feeding OR-nodes need less
  testing (because one success anywhere saves the disjunction).

---

## 4. Health Metrics (Revised)

### 4.1 Fragility of AND-Nodes

**Definition 4.1 (Conjunction fragility).** For an AND-node v with
parents {u_1, ..., u_k}, the conjunction fragility is:

    Frag_AND(v) = 1 - P(v achieved)
                = 1 - product_i (p_{u_i,v} * P(u_i))

For uniform parent confidence p across k parents:

    Frag_AND(v) = 1 - p^k

This grows rapidly with k. An AND-node with 5 parents at p = 0.9 each
has fragility 1 - 0.9^5 = 0.41. With 10 parents: 1 - 0.9^10 = 0.65.

**Prescription**: AND-nodes with many parents are structurally fragile.
Reduce parent count by grouping related requirements into sub-AND-nodes
(decomposition), or by converting some parents from required to optional
(relaxing the conjunction). Each grouping reduces the effective depth of
the conjunction while preserving the logical structure.

### 4.2 Robustness of OR-Nodes

**Definition 4.2 (Disjunction robustness).** For an OR-node v with
k parents at uniform confidence p:

    Rob_OR(v) = 1 - (1-p)^k

An OR-node with 3 parents at p = 0.5 has robustness 0.875. With 5: 0.97.
But the marginal robustness of the (k+1)-th alternative decays
geometrically as (1-p)^k * p, so at some point cost exceeds gain.

### 4.3 Bottleneck Identification

**Definition 4.3 (Bottleneck score).** For each node v in the DAG:

    Bottleneck(v) = dP(root) / dP(v)

The sensitivity of the top-level objective probability to changes in v's
achievement probability. Computed via chain rule through the DAG.

For AND-ancestors of v, the bottleneck score propagates multiplicatively
(every AND-node on the path to root amplifies v's importance). For
OR-ancestors, it propagates with diminishing weight (v is one of several
alternatives).

**The highest-bottleneck node is the strategic priority.** This is the
node where improvement (or failure) has the largest impact on overall
objective achievement. In the noisy-OR-only model, bottleneck scores
are relatively flat (every parent of every node contributes
independently). In the AND/OR model, bottleneck scores can be sharply
peaked: the weakest required parent of a conjunction dominates.

### 4.4 Revised Aggregate Health

    Health(G_t) = Groundedness * ObsCoverage * P(root objective)

where P(root objective) is computed via the AND/OR propagation
(Section 2.4). This replaces the fragility-based formula in 00
(Section 3.6) with a direct probability estimate.

The advantage: P(root) already encodes conjunction fragility (AND-nodes
lower it when parents are uncertain) and disjunction robustness (OR-nodes
raise it when alternatives exist). No separate fragility term is needed.

---

## 5. What Predictions Differ from Noisy-OR

### 5.1 Achievement Probability Estimates

| Structure                  | Noisy-OR P(O)  | AND/OR P(O)    | Direction |
|----------------------------|----------------|----------------|-----------|
| All parents OR             | Same           | Same           | --        |
| All parents AND            | ~1 (inflated)  | p^k (correct)  | Much lower|
| Mixed (AND of ORs)         | ~1 (inflated)  | Moderate       | Lower     |
| Mixed (OR of ANDs)         | High           | Lower-moderate | Somewhat lower |

The noisy-OR is systematically OPTIMISTIC about conjunctive structure.
Agents using it will under-hedge and under-invest in bottleneck
mitigation for AND-structured sub-goals.

### 5.2 Resource Allocation

- **Noisy-OR**: Invest in highest-return edges everywhere (proportional).
- **AND/OR**: Invest in lowest-confidence parents of AND-nodes FIRST
  (bottleneck concentration), then highest-return OR-node parents.

Qualitatively different. AND/OR reasoning identifies the conjunctive
bottleneck; noisy-OR spreads effort evenly.

### 5.3 Pruning Behavior

Pruning a parent of an AND-node is catastrophic (zeros the conjunction).
AND-parents should never be pruned unless replaced. OR-parents can be
pruned freely when alternatives remain.

### 5.4 Hedging Prescriptions

- **Hedge across OR-nodes**: standard parallel alternatives.
- **Hedge WITHIN AND-nodes**: each required parent should itself be an
  OR-node backed by alternatives (component-level hedging).
- **Do NOT hedge at the AND-level**: more required components = more
  fragile, not more robust.

### 5.5 Depth Fragility (Compounded)

The depth-fragility result from 00 (Section 3.5) becomes more severe.
A chain of AND-nodes each with k parents at confidence p has
end-to-end probability:

    P(chain) = (p^k)^d = p^{kd}

where d is the chain depth. The exponent is k*d, not d as in the
serial-chain case. A depth-3 chain of AND-nodes each requiring 3
parents at p = 0.9:

    P = 0.9^9 = 0.387

Compared to a simple depth-3 serial chain: P = 0.9^3 = 0.729.

AND-nodes amplify depth fragility. Strategies with deep chains of
conjunctions are exponentially more fragile than strategies with deep
chains of disjunctions.

---

## 6. The OKR Mapping Revisited

### 6.1 Natural AND vs OR Structure in OKRs

The AND/OR distinction maps cleanly to OKR practice:

**AND-structure (all required):**
- Objective <- KRs: Typically AND. "Launch OAuth" requires token flow
  AND session persistence AND backward compatibility.
- Sequential dependencies: A -> B effectively AND (both must succeed).

**OR-structure (any suffices):**
- KR <- Initiatives: Often OR. "Token flow works" via library X OR
  raw HTTP OR third-party service.
- Risk mitigations, market channel alternatives.

**The typical OKR shape is AND-of-ORs**: the objective requires ALL key
results (AND), and each key result can be achieved through ANY of several
initiatives (OR). This is the natural two-level structure:

    O [AND]
    ├── KR1 [OR]
    │   ├── Init A
    │   └── Init B
    ├── KR2 [OR]
    │   └── Init C
    └── KR3 [OR]
        └── Init D

The AND-of-ORs shape is actually well-behaved: the OR-level provides
robustness within each requirement, and the AND-level correctly captures
the conjunction across requirements. The problematic shapes are:

- **AND-of-ANDs**: Deep conjunctive chains. Exponentially fragile.
- **OR-of-ANDs**: Each alternative is itself a conjunction. The
  disjunction provides robustness, but each branch is fragile.

### 6.2 Diagnostic: OKR Health via AND/OR Analysis

For Objective o [AND-node]: P(o) = product_{KR_i} P(KR_i contributes).
The weakest KR determines the ceiling: P(o) <= min_i P(KR_i -> o).

The strategic priority is ALWAYS the weakest KR (formally derivable,
not just heuristic). Within that KR (OR-node), check if adding
alternatives would help; if its children are already high-confidence,
the bottleneck is the KR-to-O edge itself.

---

## 7. Is the AND/OR Distinction Principled or Scaffold?

This is the critical question. Two sub-questions:

### 7.1 Can AND/OR Be Derived from the Domain?

In some cases, yes. The combination type is derivable from the causal
semantics of the domain:

**Principled AND**: When the parent contributions are COMPLEMENTARY
COMPONENTS of a single mechanism. "The bridge requires BOTH the span
AND the supports." This is an AND because the physical mechanism
requires all components. You can read the AND off the causal structure
of reality (M_t).

**Principled OR**: When the parent contributions are ALTERNATIVE
MECHANISMS for the same effect. "The river can be crossed by bridge OR
ford OR boat." This is an OR because multiple independent mechanisms
can produce the same result.

**The test**: Ask "if I remove one parent, does the child still have a
mechanism for achievement?" If yes, the node is OR. If no, the node
is AND. This is a causal question, answerable (in principle) from M_t.

So the AND/OR distinction is derivable from the agent's causal model of
reality. It is not an arbitrary annotation -- it reflects the causal
structure of the domain. This makes it PRINCIPLED in the same way that
the edge weight p_ij is principled: it is a claim about reality,
updatable as M_t improves.

### 7.2 Can AND/OR Be Wrong?

Yes. The agent's assignment of AND or OR can be incorrect:

- **False AND**: The agent believes all parents are required, but in
  reality one parent is sufficient. Effect: the agent over-invests in
  ensuring all components succeed when it could succeed with fewer.
  Pessimistic error.

- **False OR**: The agent believes any parent suffices, but in reality
  all are required. Effect: the agent under-invests, relying on a
  single path when multiple are needed. Optimistic error. THIS IS
  EXACTLY THE NOISY-OR FAILURE MODE -- the noisy-OR treats everything
  as OR, which is systematically optimistic about conjunctive structures.

The combination type should be updateable. One mechanism: the agent
starts with a prior gamma(v) based on domain knowledge, then updates
based on evidence. If the agent achieves one parent of a supposed
AND-node and finds that v is achieved anyway, the node should be
reclassified as OR (or the extra parents recognized as redundant).

### 7.3 Generalizations

**Continuous relaxation.** A gamma in [0,1] could model k-of-n
thresholds ("at least 3 of 5 KRs must be met"). Probably not worth
the complexity for a first formalism; binary AND/OR captures the
dominant distinction.

**Relationship to factor graphs.** The AND/OR DAG is a restricted
factor graph: O(1) parameters per node vs. O(exp(k)) for a full factor.
The restriction is justified when domain causation is predominantly
conjunctive-or-disjunctive. Complex interactions (synergies, inhibition)
can be decomposed into intermediate AND/OR nodes.

---

## 8. Cost of Complexity

### 8.1 What the AND/OR Structure Adds

1. One bit per node. Same O(|V| + |E|) propagation complexity.
2. Correct probability estimates for conjunctive structures.
3. Sharp bottleneck identification via chain-rule sensitivity.
4. Principled resource allocation (weakest required link first).
5. Correct hedging prescriptions (hedge alternatives, not requirements).

### 8.2 What It Costs

1. **Gamma must be assigned.** One additional modeling decision per node.
   Usually obvious from domain knowledge, but edge cases require judgment.
2. **Gamma can be wrong.** Misassignment produces systematic errors.
   The noisy-OR also produces systematic errors, but consistently
   (always optimistic). AND/OR errors depend on which nodes are wrong.
3. **Grafting is conditional on gamma.** Adding a parent to an AND-node
   HURTS (more requirements). The agent must know gamma before grafting.
4. **Less graceful degradation at AND-nodes.** An AND-parent's weight
   declining to zero is catastrophic (zeros the conjunction). The smooth
   degradation story from 00 (Section 2.7) partially breaks.

### 8.3 Net Assessment

The AND/OR extension is a net gain for all target domains (software,
military, organizational). Most real strategies are AND-of-ORs, and
the AND-level is where noisy-OR fails most visibly.

**Recommendation**: Adopt AND/OR as the default. The noisy-OR is the
special case gamma(v) = OR for all v.

---

## 9. Interaction with the Orient Cycle

The Orient cycle from 00 (Section 4.3) gains one new operation:
**gamma reclassification** -- updating a node's AND/OR type when
evidence shows the structural relationship between parents differs
from what was assumed. The timescale ordering extends:

    nu_{weight-update} >> nu_{gamma-reclassify} >> nu_{prune/graft} >> nu_{objective-revision}

Reclassification is rarer than weight updates (needs strong structural
evidence) but more frequent than pruning (which abandons a causal
hypothesis entirely).

---

## 10. Summary

| Property | Noisy-OR (00) | AND/OR (this document) |
|----------|---------------|------------------------|
| Combination semantics | Implicit OR everywhere | Explicit AND or OR per node |
| Conjunctive sub-goals | Systematically overestimates P | Correct P = product |
| Disjunctive sub-goals | Correct P = 1 - product(complements) | Same |
| Edge weight parameters | (p, theta) -- two per edge | p only -- one per edge |
| Bottleneck identification | Flat (all parents contribute independently) | Sharp (weakest AND-parent dominates) |
| Resource allocation | Proportional to return | Concentrate on weakest required link |
| Hedging prescription | Hedge everywhere proportionally | Hedge alternatives (OR), reinforce requirements (AND) |
| Depth fragility | P = p^d | P = p^{kd} for AND-chains (worse) |
| Modeling cost | No per-node annotation needed | One bit per node (AND/OR type) |
| Graceful degradation | Smooth everywhere | Smooth at OR-nodes, sharp at AND-nodes |
| Principled or scaffold? | Scaffold (independence assumption) | More principled (derivable from causal structure) |

The AND/OR DAG corrects a systematic error (noisy-OR overestimation of
conjunctions), provides sharper prescriptions (bottleneck concentration,
differential hedging), and is more principled (derivable from causal
semantics of M_t). Cost: one bit per node, one modeling decision, less
uniform degradation at AND-nodes. It should replace noisy-OR as the
default combination semantics for the AAD intent DAG.
