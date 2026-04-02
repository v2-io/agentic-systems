---
slug: graph-structure-uniqueness
type: derivation
status: conditional
depends:
  - strategy-dag
  - chain-confidence-decay
  - explicit-strategy-condition
  - causal-structure
stage: draft
---

# Derivation: Graph Structure Uniqueness

Four operational postulates — directed temporal ordering, probabilistic uncertainty, state-local revisability, and observable intermediates — force the strategy representation to be a directed acyclic graph with the Markov property.

## Formal Expression

### The Postulates

Four properties that a strategy representation must satisfy. Each is independently motivated from the adaptive-systems foundation.

#### P1: Directed Temporal Ordering

*[Derived (from #causal-structure)]*

If component $A$ of the strategy causally produces component $B$, then $A$ temporally precedes $B$. The strategy representation must respect this directionality — edges point from causes to effects, from actions to outcomes, from prerequisites to goals.

This is a consequence of the temporal postulate ( #causal-structure): the arrow of time is constitutive, not incidental. Reversing a causal edge would mean effects precede causes, which is physically impossible.

#### P2: Probabilistic Uncertainty

*[Derived (from Cox's theorem)]*

The agent's uncertainty about whether each step of the strategy will succeed must be quantified by a measure satisfying Cox's axioms (consistency, universality, non-negativity). The unique such measure is probability (Cox 1946). The agent may use other representations internally (confidence scores, fuzzy logic), but these must be mappable to probability to be consistent.

#### P3: State-Local Revisability

*[Derived (from #chain-confidence-decay + bounded computation)]*

When the agent observes evidence about one component of its strategy (e.g., "step 3 succeeded" or "prerequisite 2 is blocked"), it must be able to update its beliefs about that component and its consequences without recomputing the entire strategy from scratch.

**Why this is forced, not chosen:**

*From fragility.* Additive log-confidence ( #chain-confidence-decay) means longer chains are exponentially less reliable. The agent will frequently encounter partial failures. Each partial failure requires re-evaluation of the affected portion of the strategy. If each re-evaluation requires full recomputation, the agent's planning tempo $T_\Sigma$ is catastrophically slow — potentially violating the strategy persistence condition.

*From bounded computation.* The agent has finite computational resources (the IB constraint applies to planning as well as model maintenance). Full recomputation of a strategy with $N$ components costs $O(N)$ or worse. Local revision costs $O(\lvert\text{affected}\rvert)$, which can be much smaller.

*From the persistence condition.* Strategy must be revised faster than the environment invalidates it. Local revision directly increases $T_\Sigma$ by reducing the per-update cost. An agent that must recompute everything on each update has lower $T_\Sigma$ and is more likely to fall below the persistence threshold.

#### P4: Observable Intermediates

*[Derived (from #chain-confidence-decay + monitoring requirement)]*

The strategy representation must have internal checkpoints — observable states between the initial action and the final goal — that the agent can monitor to detect partial failure.

Without intermediates, the agent cannot detect chain failure until the final outcome. By the time the final outcome reveals failure, all intermediate actions are wasted. With intermediates, the agent can detect failure at step $k$ and revise, saving the cost of steps $k+1$ through $n$. The value of early detection grows with chain length, because longer chains fail more often (P2 + #chain-confidence-decay).

### The Derivation

#### Step 1: P1 implies directed edges

Each component $X_i$ of the strategy has a set of direct causes $\text{Pa}(X_i)$ — the components whose outcomes directly influence $X_i$'s outcome. P1 requires that these causal relationships are directed: $\text{Pa}(X_i)$ temporally precedes $X_i$. This gives directed edges $\text{Pa}(X_i) \to X_i$.

#### Step 2: P2 implies probability distributions on edges

Each edge carries uncertainty: $P(X_i \mid \text{Pa}(X_i))$. By P2 (Cox), this is a probability distribution. The joint distribution over all strategy components is some $P(X_1, \ldots, X_n)$.

#### Step 3: P3 + P1 + causal sufficiency imply the Markov condition

*[Derived (Conditional on causal sufficiency of $\Sigma_t$)]*

**Claim.** P3 (state-local revisability) combined with P1 (temporal ordering) and causal sufficiency of the strategy representation implies the local Markov property.

**The local Markov property.** Each variable $X_i$ is conditionally independent of its non-descendants given its parents:

$$X_i \perp \text{NonDesc}(X_i) \mid \text{Pa}(X_i)$$

**The argument has three parts:**

**(a) P3 requires some local neighborhood to suffice.** When the agent updates its belief about $X_i$, it must do so using a local neighborhood $\text{Ne}(X_i)$ rather than the entire graph. For the local update to be correct:

$$P(X_i \mid \text{Ne}(X_i), \text{rest}) = P(X_i \mid \text{Ne}(X_i))$$

P3 establishes that SOME such neighborhood exists. It does not specify which.

**(b) P1 identifies parents as the natural neighborhood.** In a directed graph respecting temporal ordering, causal influence on $X_i$ flows from temporally preceding nodes through directed edges. The nodes with direct causal influence on $X_i$ are precisely $\text{Pa}(X_i)$ — the parents. Non-parent predecessors can only affect $X_i$ through the parents (their influence is mediated). Non-descendants are either predecessors (influence mediated through parents) or temporally unrelated (no causal path to $X_i$). Therefore: in a temporally ordered directed graph, $\text{Pa}(X_i)$ is the minimal local neighborhood that captures all direct causal influence on $X_i$.

**(c) Causal sufficiency makes parents sufficient.** The above requires that all direct causes of $X_i$ ARE represented as parents in the graph — that there are no latent common causes between $X_i$ and its non-descendants. This is the causal sufficiency assumption.

For $\Sigma_t$ specifically, causal sufficiency is a reasonable assumption: the agent *constructed* the strategy graph, so all nodes are explicit. There are no "hidden" strategy components — the agent chose every node. If environmental factors affect multiple strategy steps (shared infrastructure, weather, market conditions), they should appear as condition nodes in $\Sigma_t$ ( #strategy-dag, source constraint). If they are omitted, the strategy is model-inadequate — exactly the situation #structural-adaptation-necessity addresses — and the Markov condition fails for the explicit nodes. This is a model quality issue, not a structural limitation of the argument.

**Assembling (a)-(c).** P3 requires a sufficient local neighborhood. P1 identifies parents as the causal neighborhood. Causal sufficiency ensures parents capture all direct influences. Therefore:

$$P(X_i \mid \text{Pa}(X_i), \text{NonDesc}(X_i)) = P(X_i \mid \text{Pa}(X_i))$$

This IS the local Markov property.

**Equivalence to factorization.** For positive distributions (all configurations have nonzero probability — a mild regularity condition), the local Markov property is equivalent to the global Markov property and to the factorization property (Lauritzen 1996, Theorem 3.27; Verma 1993):

$$P(X_1, \ldots, X_n) = \prod_{i=1}^{n} P(X_i \mid \text{Pa}(X_i))$$

This is the defining property of a Bayesian network.

**What about non-parent local neighborhoods?** The earlier sketch noted that other sparse factorizations (e.g., factor graphs with message-passing) might also support local revision. This is true — factor-graph message passing achieves exact inference for trees and approximate inference for loopy graphs, using a different local neighborhood (the factor's scope, not the parents). But P1 (directed temporal ordering) selects the parent-conditional factorization specifically, because the causal direction matters: the agent needs to reason about consequences of interventions ($do(X_i)$), and Pearl's do-calculus is defined on the parent-conditional DAG factorization, not on undirected factor graphs. Directed local neighborhoods (parents) are forced by the combination of locality (P3) and causal directionality (P1); undirected alternatives sacrifice the causal semantics that #strategy-dag requires.

**Why non-descendants specifically.** Descendants of $X_i$ depend on $X_i$ by construction — they are downstream. Updating $X_i$ based on $\text{Pa}(X_i)$ does not require knowing descendants, because causal influence flows FROM $X_i$ TO descendants, not the reverse. Learning about descendants can provide evidence about $X_i$ (diagnostic reasoning / explaining away), but that evidence flows through the graph structure itself via belief propagation — it does not violate P3 because the update still propagates locally.

#### Step 4: P1 + finite horizon implies acyclicity (proved)

This is the strongest piece of the argument. See the dedicated section below.

#### Step 5: Assembly

P1 (directed edges) + P2 (probabilistic) + P3 (Markov condition) + P4 (internal nodes) + finite horizon (acyclicity):

**The strategy representation must be representable as a directed acyclic graph with probability distributions at each node conditioned on its parents — a Bayesian network.**

### Acyclicity Derivation

*[Derived (from #causal-structure + finite planning horizon)]*

This resolves a former known fragility in the theory. Acyclicity of $\Sigma_t$ is derived, not assumed.

**Result.** For a strategy representation over a finite future horizon, temporal ordering forces acyclicity.

**Derivation.**

1. Each node $X_i$ in $\Sigma_t$ represents a future event or state with temporal position $\tau_i \gt t$ (the future time at which the step occurs or the state is evaluated).
2. Each edge $X_i \to X_j$ requires $\tau_i \lt \tau_j$ (P1: causes temporally precede effects).
3. A cycle $X_i \to X_j \to \cdots \to X_i$ would require $\tau_i \lt \tau_j \lt \cdots \lt \tau_i$, which is impossible for a real-valued time index.
4. Therefore the graph is acyclic. $\square$

Formally: a finite set with a strict partial order (future events ordered by time) is representable as a DAG. This is a standard result in order theory — every finite partial order has a Hasse diagram, which is a DAG.

**The iteration objection resolved.** A strategy that says "try $A$, if fail try $B$, if fail try $A$ again" appears cyclic.

In the time-indexed representation:

$$A_1 \to \text{check}_1 \to B_1 \to \text{check}_2 \to A_2 \to \ldots$$

Each attempt is a distinct node at a distinct time. The apparent cycle is a linear chain in the unrolled view. Iteration "terminates" when either a node succeeds (remaining retry nodes become probability-zero), the agent exhausts its resource budget (a constraint truncating the chain), or the horizon ends. Any finite-horizon strategy, including those with "loops" in the informal sense, is acyclic when time-indexed.

**Scope.** This applies to $\Sigma_t$ (the agent's strategy over the future), not to $M_t$'s model of the environment. $M_t$ may include cyclic causal processes — feedback loops in the physical world, market dynamics, ecosystem interactions. The acyclicity is specific to the purposeful substate because $\Sigma_t$ represents planned future actions and the future is partially ordered by time. $M_t$'s model of environmental dynamics may need to represent cycles (via time-unrolled DBNs or other cyclic structures).

**Connection to Pearl.** Pearl's do-calculus is defined on DAGs. Extensions to cyclic structures exist (cyclic SCMs, equilibrium models) but are substantially more complex and lose some of do-calculus's clean properties. The temporal argument here shows that for strategy representations (future-looking plans), acyclicity is not a convenience restriction on Pearl's framework — it is a consequence of the temporal structure of planning.

### What Is Forced vs. What Is Chosen

| Property | Forcing postulate | Strength |
|---|---|---|
| Directed edges | Temporal ordering (P1, #causal-structure) | Proved |
| Probabilistic uncertainty | Cox's theorem (P2) | Proved |
| Acyclicity | Temporal ordering + finite horizon (P1) | Proved |
| Internal structure | Fragility + monitoring (P4, #chain-confidence-decay) | Derived |
| Markov factorization | Local revisability (P3) + temporal ordering (P1) + causal sufficiency | Conditional — holds for causally sufficient strategies |
| **DAG with Markov property** | **P1 + P2 + P3 + P4 + causal sufficiency** | **Conditional — causal sufficiency is the remaining assumption** |
| AND/OR parameterization | Boolean completeness + parsimony | Hypothesis (binary outcomes only) |
| Single-parameter edges | Parsimony / IB | Formulation choice |
| Specific node ontology | — | Formulation choice |

The dividing line: the graph structure (DAG with Markov property) is forced by operational postulates. The parameterization (AND/OR, CPT form, edge semantics) is a formulation choice within the forced structure, motivated by parsimony and domain fit but not by mathematical necessity.

### Equivalence Class

**Within the DAG class.** Multiple DAGs can encode the same conditional independence relations, forming a Markov equivalence class identified by a CPDAG (completed partially directed acyclic graph). Two DAGs in the same equivalence class make identical probabilistic predictions but may differ in causal interpretation.

**Across representation types.** Factor graphs, junction trees, influence diagrams, and chain graphs are NOT simple presentational variants of DAGs:

- **Factor graphs** and **junction trees** preserve factorization and inference structure without necessarily preserving directed causal semantics.
- **Influence diagrams** add decision and utility nodes — a richer object, not an equivalent one.
- **Chain graphs** can express independence models that are not representable as DAGs at all.
- **Markov equivalence** is a statement within DAG classes, not across all graphical model types.

The correct claim is narrow: for a given factorized distribution, DAG and factor-graph representations can compute the same marginals. But causal semantics (do-calculus) are DAG-specific and do not transfer to undirected or mixed representations without additional structure.

**ACT's choice.** ACT uses DAG + AND/OR because: (a) AND/OR is the most parsimonious complete basis for binary combination ( #and-or-scope), (b) the DAG naturally supports causal/interventional reasoning (Pearl's do-calculus), and (c) the representation converged across three independent formalism attempts.

## Epistemic Status

The acyclicity derivation is *exact* — it follows from temporal ordering over a finite horizon via standard order theory. The individual postulates P1, P2, and P4 are each well-grounded (temporal structure, Cox's theorem, and chain fragility respectively).

The P3→Markov step is now *conditional on causal sufficiency* of $\Sigma_t$. The argument has three parts: P3 requires some local neighborhood (locality), P1 identifies parents as the causal neighborhood (directionality), and causal sufficiency ensures parents capture all direct influences (no hidden common causes). Assembling these gives the local Markov property, which Lauritzen (1996, Theorem 3.27) proves equivalent to the factorization property for positive distributions. The causal sufficiency assumption is reasonable for agent-constructed strategies (all nodes are explicit) and fails precisely when the strategy is model-inadequate — the situation #structural-adaptation-necessity addresses.

The previous concern about alternative sparse factorizations (factor graphs, message-passing structures) is resolved: P1's directed temporal ordering selects the parent-conditional factorization specifically, because undirected alternatives sacrifice the causal semantics that #strategy-dag requires for interventional reasoning.

Max attainable: *exact* for acyclicity (already there). *Conditional* for the full DAG-with-Markov-property claim — conditional on causal sufficiency, which is a property of strategy quality rather than agent architecture. This is an honest upgrade from the previous "sketch" status.

The AND/OR restriction is a *hypothesis* for binary outcomes, grounded in Boolean completeness and parsimony. For non-binary outcomes, it does not apply and richer parameterizations within the forced graphical structure are needed.

The analogy to Cox's theorem — consistency axioms force probability; operational postulates force graphical structure — is suggestive but not established. Cox's theorem has a formal proof; this argument has a derivation sketch with one step that needs tightening. The analogy is worth stating as motivation but should not be relied on as evidence.

## Discussion

**The contribution of this analysis.** The dividing line between forced structure and chosen parameterization is the key result. The agent community (and future researchers) know exactly what is mathematically forced (the graph) and what is a formulation choice (the parameterization within the graph). Alternative parameterizations can be explored without abandoning the theoretical foundation.

**Acyclicity deserves emphasis.** The existing theory previously flagged "DAG acyclicity is an assumption, not forced" as a known fragility. The derivation above resolves this: acyclicity of $\Sigma_t$ follows from temporal ordering over a finite planning horizon. This is specific to the strategy — $M_t$'s environment model is not restricted to acyclic structures.

**The causal sufficiency assumption.** The Markov condition assumes causal sufficiency — no hidden common causes within the strategy. Since the agent constructs $\Sigma_t$, there are no "hidden" variables internal to the strategy (the agent chose all the nodes). But environmental common causes that affect multiple strategy steps may violate the Markov condition within $\Sigma_t$. If so, latent variable models or causal graphs with hidden nodes would be needed. This connects to the edge identifiability problem noted in #strategy-dag.

## Working Notes

- **P3 implies Markov tightening.** The critical open question. The argument that local revisability requires the Markov condition is plausible but not proved. The specific gap: other sparse factorizations (message-passing on factor graphs, junction tree decompositions) also support local computation. Does P3 specifically force parent-conditional independence, or does it force a weaker structural property that the Markov condition happens to satisfy? The answer likely depends on how "local" is formalized — if it means "conditioned on direct causes only," the Markov condition follows by definition; if it means "conditioned on a small neighborhood," broader structures qualify.
- **Parsimony theorem for AND/OR.** Is there a formal result that AND/OR (noisy-AND + noisy-OR) is the unique $O(k)$-parameter complete basis for binary nodes? This would strengthen #and-or-scope from formulation choice to derived. The Boolean completeness half is standard; the uniqueness-under-parsimony half is not established.
- **Non-binary outcome analogs.** For continuous or multi-valued outcomes, the natural analogs of AND/OR might be min/max or additive/multiplicative combination. Is there a completeness result for these? The current argument applies cleanly only to binary outcomes.
- **Environmental common causes.** Multiple strategy steps may share unmodeled environmental dependencies (weather affecting both supply chain and demand). This violates the Markov condition within $\Sigma_t$ even though the agent chose all the nodes, because the agent did not model the common cause as a node. Addressing this requires either adding latent variables to the DAG or acknowledging that the independent-edge calculations systematically overestimate confidence (consistent with the correlated-failure note in #strategy-dag).
- **If P3 implies Markov is tightened to a full proof**, #strategy-dag could potentially be promoted from Definition to Derived — the DAG structure would be forced rather than chosen. Until then, the definition stands and this segment provides the best available structural motivation.
