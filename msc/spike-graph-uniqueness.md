# Spike: Is the DAG Structure Mathematically Forced?

**Status**: Exploratory — pushing on whether the graphical structure of Σ_t can be derived rather than chosen. This is the "Cox's theorem for strategy representation" question: just as Cox showed that consistency axioms force probability, can we show that operational axioms force directed graphical models?

**Date**: 2026-03-09

**The nuanced framing**: This spike emerged from asking "are we just justifying a destination we already knew?" The answer was: mostly yes for the v3 purposeful agency spike, but this graph uniqueness argument is different — the P3 → Markov step was not expected, and the acyclicity derivation resolves a listed known fragility. The graph STRUCTURE being forced (while the parameterization remains a choice) is a genuine mathematical result, not a repackaging of existing architecture. It should be stated with appropriate confidence: the proof sketch is tight but needs verification against the graphical models literature (Lauritzen 1996, Koller & Friedman 2009). The analog to Cox's theorem is suggestive, not established — Cox's theorem has a formal proof; this argument has a proof sketch.

---

## The Question

The v3 spike established functional requirements for strategy representations but concluded the specific formalism (DAG with AND/OR) was a "formulation choice." This spike asks: is that conclusion too pessimistic? Do the functional requirements actually force graphical structure more tightly than we claimed?

## The Axioms

Four properties that a strategy representation must satisfy. Each is independently motivated from the adaptive-systems foundation.

### P1: Directed temporal ordering

*[Derived from TF-02]*

If component A of the strategy causally produces component B, then A temporally precedes B. The strategy representation must respect this directionality — edges point from causes to effects, from actions to outcomes, from prerequisites to goals.

**This is not a modeling choice.** It is a consequence of the temporal axiom (TF-02): the arrow of time is constitutive, not incidental. Reversing a causal edge would mean effects precede causes, which is physically impossible.

### P2: Probabilistic uncertainty

*[Derived from Cox's theorem]*

The agent's uncertainty about whether each step of the strategy will succeed must be quantified by a measure satisfying Cox's axioms (consistency, universality, non-negativity). The unique such measure is probability.

**This is not a modeling choice.** Cox's theorem (1946) proves that any consistent quantification of plausibility is isomorphic to probability. The agent may use other representations internally (confidence scores, fuzzy logic), but these must be mappable to probability to be consistent.

### P3: State-local revisability

*[Derived from fragility + bounded computation]*

When the agent observes evidence about one component of its strategy (e.g., "step 3 succeeded" or "prerequisite 2 is blocked"), it must be able to update its beliefs about that component and its consequences WITHOUT recomputing the entire strategy from scratch.

**Why this is forced, not chosen:**

*From fragility*: Additive log-confidence (v3 §6.1) means longer chains are exponentially less reliable. The agent will frequently encounter partial failures. Each partial failure requires re-evaluation of the affected portion of the strategy. If each re-evaluation requires full recomputation, the agent's planning tempo T_Σ is catastrophically slow — potentially violating the strategy persistence condition.

*From bounded computation*: The agent has finite computational resources (the IB constraint applies to planning as well as to model maintenance). Full recomputation of a strategy with N components costs O(N) or worse. Local revision costs O(|affected|), which can be much smaller.

*From the persistence condition itself*: Strategy must be revised faster than the environment invalidates it (the proposed schema T_Σ > ρ_Σ / δ_Σ_critical). Local revision directly increases T_Σ by reducing the per-update cost. An agent that must recompute everything on each update has lower T_Σ and is more likely to fall below the persistence threshold.

### P4: Observable intermediates

*[Derived from fragility + monitoring requirement]*

The strategy representation must have internal checkpoints — observable states between the initial action and the final goal — that the agent can monitor to detect partial failure.

**Why this is forced**: Without intermediates, the agent cannot detect chain failure until the final outcome. By the time the final outcome reveals failure, all intermediate actions are wasted. With intermediates, the agent can detect failure at step k and revise, saving the cost of steps k+1 through n. The value of early detection grows with chain length (because longer chains fail more often — P2 + additive log- confidence).

---

## The Derivation

### Step 1: P1 → Directed edges

Each component X_i of the strategy has a set of direct causes Pa(X_i) — the components whose outcomes directly influence X_i's outcome. P1 requires that these causal relationships are directed: Pa(X_i) temporally precedes X_i. This gives directed edges Pa(X_i) → X_i.

### Step 2: P2 → Probability distributions on edges

Each edge carries uncertainty: P(X_i | Pa(X_i)). By P2 (Cox), this is a probability distribution. The joint distribution over all strategy components is some P(X_1, ..., X_n).

### Step 3: P3 → The Markov condition (this is the key step)

**Claim**: P3 (state-local revisability) implies the Markov condition.

**The Markov condition**: Each variable X_i is conditionally independent of its non-descendants given its parents:

$$X_i \perp \text{NonDesc}(X_i) \mid \text{Pa}(X_i)$$

**Proof sketch**:

Suppose the agent updates its belief about X_i using only Pa(X_i) — i.e., it computes P(X_i | Pa(X_i)) without considering other variables. For this to be correct (to match the full conditional P(X_i | Pa(X_i), other evidence)), we need:

$$P(X_i \mid \text{Pa}(X_i), \text{NonDesc}(X_i)) = P(X_i \mid \text{Pa}(X_i))$$

for all values of NonDesc(X_i). This IS conditional independence of X_i from its non-descendants given its parents — the Markov condition.

**Why non-descendants specifically**: Descendants of X_i DO depend on X_i (by construction — they're downstream). But updating X_i based on Pa(X_i) doesn't require knowing descendants, because the causal influence flows FROM X_i TO descendants, not the other way. Learning about descendants can provide evidence about X_i (diagnostic reasoning / explaining away), but that evidence flows through the graph structure itself — it doesn't violate P3 because the update still propagates locally through the graph.

**The factorization**: The Markov condition is equivalent to the factorization of the joint distribution:

$$P(X_1, \ldots, X_n) = \prod_{i=1}^{n} P(X_i \mid \text{Pa}(X_i))$$

This IS the defining property of a Bayesian network. So P3 forces the strategy to be representable as a Bayesian network.

### Step 4: P1 + finite horizon → Acyclicity

**Claim**: In a strategy over a finite future, temporal ordering prevents cycles.

**Argument**: Each node X_i in Σ_t represents a future event or state that has not yet occurred. These future events have temporal positions $\tau_1 \leq \tau_2 \leq \cdots$. An edge X_i → X_j requires $\tau_i \lt \tau_j$ (P1: causes precede effects). A cycle X_i → X_j → ··· → X_i would require $\tau_i \lt \tau_j \lt \cdots \lt \tau_i$, which is impossible for a real-valued time index.

**What about strategies involving iteration?** A strategy that says "try A, if fail try B, if fail try A again" appears cyclic. But in the time-indexed representation: A_1 → check_1 → B_1 → check_2 → A_2 → ... This is acyclic — A_1 and A_2 are distinct nodes at distinct times. The apparent cycle is a linear chain in the unrolled view. Any finite- horizon strategy, including those with "loops" in the informal sense, is acyclic when time-indexed.

**Formal grounding**: A finite partially ordered set (the set of future events with temporal ordering) is representable as a DAG. This is a standard result in order theory: every finite partial order has a Hasse diagram, which is a DAG.

### Step 5: Assembling the result

P1 (directed edges) + P2 (probabilistic) + P3 (Markov condition) + P4 (internal nodes) + finite horizon (acyclicity):

**The strategy representation must be representable as a directed acyclic graph with probability distributions at each node conditioned on its parents — a Bayesian network.**

---

## How Tight Is This?

### What's forced

The GRAPH STRUCTURE is forced. Any strategy representation satisfying P1-P4 must be expressible as a DAG with the Markov property. This is not a choice of formalism — it's a consequence of:
- Time having a direction (physics)
- Uncertainty being quantified by probability (Cox)
- Local revision being correct (Markov condition)
- Finite planning horizon (acyclicity)

### What's NOT forced (yet)

The PARAMETERIZATION is not forced by P1-P4. Specifically:

**CPT form**: At each node, the conditional distribution P(X_i | Pa(X_i)) can be arbitrary. The AND/OR restriction is a specific parameterization that reduces 2^k parameters to k (where k is the number of parents). This is not forced by P1-P4.

**Node types**: P1-P4 don't specify what the nodes represent — propositions, states, actions, events. The ontology of nodes is a modeling choice.

**Edge semantics**: P1-P4 require probabilistic edges but don't specify whether the probabilities are interventional (P(X_j | do(X_i))) or observational (P(X_j | X_i)). For strategy evaluation, interventional semantics are needed (the agent is asking "what happens if I DO this step"), but this is an additional requirement beyond P1-P4.

### Can we force AND/OR?

**The Boolean completeness argument** (for binary nodes):

If each node takes values in {0, 1} (achieved / not achieved), then the CPT at each node with k parents is a Boolean function {0,1}^k → [0,1] — a probability for each of the 2^k input configurations.

AND and OR are two such functions:
- AND: output is 1 iff all inputs are 1
- OR: output is 1 iff at least one input is 1

In Boolean algebra, {AND, OR, NOT} is a complete basis — any Boolean function can be expressed as a composition of ANDs, ORs, and NOTs. (De Morgan's theorem, disjunctive/conjunctive normal form.)

In the probabilistic extension (noisy-AND, noisy-OR):
- Noisy-OR: P(X = 1 | Pa) = 1 - Π(1 - p_j · Pa_j) — each parent independently has a chance of activating X
- Noisy-AND: P(X = 1 | Pa) = Π(p_j^{Pa_j}) — X requires all parents, each independently reliable

These have k parameters each, compared to 2^k for a general CPT.

**The parsimony argument**:

The agent has bounded cognitive resources (the IB constraint). A strategy node with k parents and a general CPT requires storing and updating 2^k parameters. For k = 10, that's 1024 parameters per node. For k = 20, over a million.

AND/OR with independent edges requires k parameters per node. This is exponentially more parsimonious.

Under bounded cognition, the agent is forced toward low-parameter representations. AND/OR is the most expressive such representation for binary outcomes (by Boolean completeness). Any other representation with O(k) parameters per node is either equivalent to AND/OR (via transformation) or less expressive.

**The argument, assembled**:

*[Hypothesis — not yet a theorem]*

For agents with binary-outcome strategy nodes and bounded cognitive resources:
- Boolean completeness means AND/OR can represent any combination rule
- Parsimony (IB + bounded cognition) forces O(k) parameterization
- AND/OR is the unique O(k)-parameter complete basis for binary combination

Therefore AND/OR is the optimal CPT parameterization for binary nodes under bounded cognition.

**Strength of this argument**: Moderate. It applies cleanly to binary outcomes. For continuous or multi-valued outcomes, AND/OR doesn't have the same completeness properties, and richer parameterizations may be needed. For binary outcomes with strong interaction effects between parents, AND/OR is still complete but the decomposition into AND/OR layers may require additional intermediate nodes.

---

## The Equivalence Class

Once we're in DAG territory, what representations are mathematically interchangeable?

**The fundamental equivalence**: A probability distribution P(X_1, ..., X_n) that satisfies a set of conditional independence relations can be represented by multiple equivalent graphical structures:

| Representation | Structure | Best for |
|---|---|---|
| Bayesian network | DAG + CPTs | Causal reasoning, do-calculus |
| Factor graph | Bipartite variable/factor graph | Message-passing algorithms |
| Junction tree | Tree of cliques | Exact inference |
| Influence diagram | DAG + decision + utility nodes | Decision problems |
| Chain graph | Mixed directed/undirected | Systems with both causal and symmetric relationships |

**Caution** (from Codex review): These are NOT all "mathematically equivalent" in a simple sense. Factor graphs and junction trees preserve factorization/inference structure without necessarily preserving directed causal semantics. Influence diagrams add decision/utility nodes (richer, not equivalent). Chain graphs can express independence models that are not just DAG presentational variants. Markov equivalence is a statement WITHIN DAG classes, not ACROSS all these object types.

The correct claim is narrower: within the class of DAGs, multiple DAGs can encode the same conditional independence relations (forming a Markov equivalence class, identified by a CPDAG). And for a given factorized distribution, DAG and factor-graph representations can compute the same marginals. But causal semantics (do-calculus) are DAG-specific and do not transfer to undirected or mixed representations without additional structure.

**What this means for AAD**: Once we've established that Σ_t must be a directed graphical model with the Markov property (from P1-P4), we can say:

"The graphical structure of the strategy representation is forced by the axioms. The specific graphical notation (Bayesian network, factor graph, influence diagram, etc.) is a presentational choice — all are mathematically equivalent. AAD uses the DAG with AND/OR nodes because: (a) AND/OR is the most parsimonious complete basis for binary outcomes, (b) the DAG notation naturally supports causal/interventional reasoning (Pearl's do-calculus), and (c) it converged across three independent formalism attempts, suggesting it's the most natural fit for strategic planning."

---

## Acyclicity: Not Just Assumed, Derived

This deserves emphasis because the existing theory flags "DAG acyclicity is an assumption, not forced" as a known fragility. It IS forced.

**Theorem sketch**: For a strategy representation over a finite future horizon, temporal ordering forces acyclicity.

**Proof**:
1. Each node X_i in Σ_t has an associated time $\tau_i \gt t$ (the future time at which the step occurs or the state is evaluated).
2. Each edge X_i → X_j requires $\tau_i \lt \tau_j$ (P1: causes temporally precede effects).
3. A cycle X_i → ... → X_i requires $\tau_i \lt ... \lt \tau_i$, which is impossible for real-valued time.
4. Therefore the graph is acyclic. ∎

**The "cycle" objection resolved**: Real strategies involve iteration ("keep trying until it works"). In the time-indexed representation, each attempt is a distinct node: try_1 → evaluate_1 → try_2 → evaluate_2 → ... This is a chain (acyclic), not a cycle. The iteration "terminates" when either: a node succeeds (the remaining retry nodes become probability-zero), the agent exhausts its budget (a resource constraint truncating the chain), or the horizon ends.

**Connection to Pearl**: Pearl's do-calculus requires acyclicity (or more precisely, it's defined on DAGs). Extensions to cyclic structures exist (cyclic SCMs, equilibrium models) but are substantially more complex and lose some of do-calculus's clean properties. The temporal argument here shows that for STRATEGY representations (future-looking plans), acyclicity is not a convenience restriction on Pearl's framework — it's a consequence of the temporal structure of planning.

**Note**: This does NOT apply to M_t's model of the environment, which may include cyclic causal processes (feedback loops in the physical world). The acyclicity holds for Σ_t (the agent's strategy) because Σ_t represents the agent's planned future actions, and the future is linearly (or partially) ordered. M_t's model of the environment's dynamics may need to represent cycles (via time-unrolled DBNs or other cyclic structures). The acyclicity result is specific to the purposeful substate, not to the epistemic substate.

---

## Summary of What's Forced

| Property | Forcing axiom | Strength |
|---|---|---|
| Directed edges | Temporal ordering (TF-02) | Proved |
| Probabilistic uncertainty | Cox's theorem | Proved |
| Markov factorization | Local revisability (P3) | Sketch — the step from "local updates" to "parent-conditional Markov" needs work; other sparse factorizations (e.g., message-passing structures) may also support locality |
| Acyclicity | Temporal ordering + finite horizon | Proved |
| Internal structure | Fragility + monitoring | Derived |
| **Graphical model (DAG)** | **All of the above** | **Sketch — promising but P3→Markov needs tightening** |
| AND/OR parameterization | Boolean completeness + parsimony | Hypothesis (binary outcomes) |
| Single-parameter edges | Parsimony / IB | Formulation choice |
| Specific node ontology | — | Formulation choice |

**The dividing line**: The graph structure (DAG with Markov property) is *mathematically forced* by operational axioms. The parameterization (AND/OR, CPT form, edge semantics) is a *formulation choice* within the forced structure, motivated by parsimony and domain fit but not by mathematical necessity.

This is analogous to: probability is forced by Cox's axioms, but the specific probability distribution for a given problem is a modeling choice. The framework is forced; the content is not.

---

## What This Means for AAD

1. **The DAG is not a design choice.** Section II can state: "Any strategy representation satisfying temporal ordering, probabilistic uncertainty, state-local revisability, and observable intermediates is representable as a directed acyclic graph with the Markov property. This is a theorem, not a formulation."

2. **Acyclicity is derived, not assumed.** Remove "DAG acyclicity is an assumption, not forced" from the known fragilities list. Replace with: "Acyclicity of Σ_t follows from temporal ordering over a finite planning horizon."

3. **Equivalent representations are acknowledged.** "The specific graphical notation (Bayesian network, factor graph, influence diagram) is a presentational choice. AAD uses DAG + AND/OR for parsimony and causal reasoning compatibility."

4. **The AND/OR restriction is honestly labeled.** It's a parsimony- motivated formulation for binary outcomes, not a derived necessity for all domains. For continuous or multi-valued outcomes, richer parameterizations within the forced graphical structure are needed.

5. **The remaining formulation choices are clearly bounded.** The agent community (and future researchers) know exactly what's forced (the graph) and what's chosen (the parameterization within the graph). Alternative parameterizations can be explored without abandoning the theoretical foundation.

---

## Status Assessment (from Codex review)

The goal of this spike is to **narrow the formulation-choice space**, not (yet) to promote strategy-dag from a post-scope definition to a derived theorem in src/. The current argument is good enough for the first goal — it shows the space of possible representations is much smaller than "anything goes" and that graphical structure is strongly motivated. It is NOT yet good enough for the second goal — the P3→Markov step is a sketch, not a proof, and the equivalence-class claims were overstated.

**Practical status**: Keep v3 as the authoring basis for src/. Treat this spike as a separate research appendix until the P3→Markov step and the representation-equivalence claims are tightened. The acyclicity argument is the strongest piece and may be ready for promotion independently.

## Open Questions

1. Can the P3 → Markov condition argument be made fully rigorous?
   The proof sketch above relies on "correct local updates require conditional independence." This is standard in the graphical models literature (Lauritzen 1996, Koller & Friedman 2009) but connecting it to AAD's specific axioms requires spelling out the full argument.

2. Is there a parsimony theorem for AND/OR specifically? Something like: "Among all O(k)-parameter CPT parameterizations for binary nodes, AND/OR (noisy-AND + noisy-OR) is the unique pair that forms a complete basis." I suspect this is true but haven't verified it.

3. For non-binary outcomes: what's the analog of AND/OR? In continuous domains, the natural analog might be min (AND) and max (OR), or additive and multiplicative combination. Is there a completeness result for these?

4. The Markov condition assumes causal sufficiency (no hidden common causes within the strategy). Since the agent BUILDS Σ_t, there are no "hidden" variables — the agent chose all the nodes. But could there be ENVIRONMENTAL common causes that affect multiple strategy steps? If so, the Markov condition within Σ_t is violated, and latent variable models or causal graphs with hidden nodes are needed. This connects to the edge identifiability problem.
