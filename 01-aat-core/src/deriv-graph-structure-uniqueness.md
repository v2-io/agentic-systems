---
slug: deriv-graph-structure-uniqueness
type: derivation
status: conditional
depends:
  - def-strategy-dag
  - der-chain-confidence-decay
  - norm-explicit-strategy-condition
  - post-causal-structure
stage: claims-verified
---

# Derivation: Graph Structure Uniqueness

Operational requirements on the agent's representation — directed temporal ordering, probabilistic uncertainty, and the ability to test strategy components — are *sufficient* for the strategy to be a directed acyclic graph with the Markov factorization property. The argument parallels Cox's theorem for probability in *form* but not yet in *strength*: Cox's theorem is necessary-and-sufficient (the only measure satisfying the desiderata is probability); this result is sufficient only (the desiderata guarantee DAG+Markov, but no one has shown a non-DAG structure cannot satisfy them). Acyclicity and directed edges are *proved* from temporal ordering over a finite horizon; the Markov factorization is *proved under causal sufficiency* via the Causal Markov Condition theorem (Spirtes–Glymour–Scheines, Pearl). A fourth postulate (observable intermediates) is required for localized strategic diagnosis but not for the representation or persistence results themselves.

**How far the Cox parallel goes.** Cox's theorem starts from desiderata on how a rational agent should quantify uncertainty (consistency, universality, continuous functional composition) and proves that the *only* measure satisfying them is probability — necessity. This segment starts from desiderata on how a bounded agent can represent its strategy under causal action (directed temporal order, probabilistic edge uncertainty, causal sufficiency of the chosen nodes) and proves that DAG+Markov *suffices* to satisfy them — sufficiency. The necessity direction — no non-DAG structure (factor graphs, junction trees with cyclic message schedules, chain graphs) can satisfy P1–P4 plus causal sufficiency — is not established here. In practical terms this gap is unimportant because the proved sufficiency gives a rigorous grounding for the DAG structure; claims that AAD's strategy *must* be a DAG should be read as "must-if-sufficient-via-this-route," not as a proved necessity. A stronger Cox-style result is open. The placement of the DAG structure on a footing comparable to probability — a consequence of operational requirements rather than a modeling convenience — holds in the sufficiency direction; the full parallel with Cox awaits a uniqueness argument.

## Formal Expression

### The Postulates

Four properties that a strategy representation must satisfy. Each is independently motivated from the adaptive-systems foundation.

#### P1: Directed Temporal Ordering

*[Derived (from #post-causal-structure)]*

If component $A$ of the strategy causally produces component $B$, then $A$ temporally precedes $B$. The strategy representation must respect this directionality — edges point from causes to effects, from actions to outcomes, from prerequisites to goals.

This is a consequence of the temporal postulate ( #post-causal-structure): the arrow of time is constitutive, not incidental. Reversing a causal edge would mean effects precede causes, which is physically impossible.

#### P2: Probabilistic Uncertainty

*[Derived (from Cox's theorem)]*

The agent's uncertainty about whether each step of the strategy will succeed must be quantified by a measure satisfying Cox's axioms (consistency, universality, non-negativity). The unique such measure is probability (Cox 1946, "Probability, Frequency and Reasonable Expectation," *American Journal of Physics* 14(1):1–13; modern exposition in Jaynes 2003, *Probability Theory: The Logic of Science*, Cambridge University Press, Chapter 2). The agent may use other representations internally (confidence scores, fuzzy logic), but these must be mappable to probability to be consistent.

#### P3: State-Local Revisability

*[Derived (from #der-chain-confidence-decay + bounded computation)]*

When the agent observes evidence about one component of its strategy (e.g., "step 3 succeeded" or "prerequisite 2 is blocked"), it must be able to update its beliefs about that component and its consequences without recomputing the entire strategy from scratch.

**Why this is forced, not chosen:**

*From fragility.* Additive log-confidence ( #der-chain-confidence-decay) means longer chains are exponentially less reliable. The agent will frequently encounter partial failures. Each partial failure requires re-evaluation of the affected portion of the strategy. If each re-evaluation requires full recomputation, the agent's planning tempo $T_\Sigma$ is catastrophically slow — potentially violating the strategy persistence condition.

*From bounded computation.* The agent has finite computational resources (the IB constraint applies to planning as well as model maintenance). Full recomputation of a strategy with $N$ components costs $O(N)$ or worse. Local revision costs $O(\lvert\text{affected}\rvert)$, which can be much smaller.

*From the persistence condition.* Strategy must be revised faster than the environment invalidates it. Local revision directly increases $T_\Sigma$ by reducing the per-update cost. An agent that must recompute everything on each update has lower $T_\Sigma$ and is more likely to fall below the persistence threshold.

#### P4: Observable Intermediates

*[Derived (from #der-chain-confidence-decay + monitoring requirement)]*

To support **localized strategic diagnosis and revision**, the strategy representation benefits from internal checkpoints — observable states between the initial action and the final goal — that the agent can monitor to detect partial failure.

Without intermediates, the agent cannot detect chain failure until the final outcome. By the time the final outcome reveals failure, all intermediate actions are wasted. With intermediates, the agent can detect failure at step $k$ and revise, saving the cost of steps $k+1$ through $n$. The value of early detection grows with chain length, because longer chains fail more often (P2 + #der-chain-confidence-decay).

**Observable intermediates are not required for strategy representation or persistence.** When intermediates are unobservable, plan-level tracking ( #schema-strategy-persistence, Case 3) preserves the sector condition at the cost of per-edge diagnostic resolution — the agent knows the plan is failing but cannot localize which step needs revision ( #der-observability-dominance). P4 is therefore a requirement for *strong diagnostics*, not for strategy representation per se. The observability investment tradeoff ( #der-observability-dominance) quantifies the payoff: making an intermediate observable improves the sector parameter from $1/(n_\Phi + 1)$ (plan-level) to $\min(1/(n_1+1),\; \theta_1/(n_2+1))$ (per-edge weakest-link).

### The Derivation

#### Step 1: P1 implies directed edges

Each component $X_i$ of the strategy has a set of direct causes $\text{Pa}(X_i)$ — the components whose outcomes directly influence $X_i$'s outcome. P1 requires that these causal relationships are directed: $\text{Pa}(X_i)$ temporally precedes $X_i$. This gives directed edges $\text{Pa}(X_i) \to X_i$.

#### Step 2: P2 implies probability distributions on edges

Each edge carries uncertainty: $P(X_i \mid \text{Pa}(X_i))$. By P2 (Cox), this is a probability distribution. The joint distribution over all strategy components is some $P(X_1, \ldots, X_n)$.

#### Step 3: Causal sufficiency implies the Markov condition (proved)

*[Derived (Conditional on causal sufficiency of $\Sigma_t$)]*

**Claim.** For a causally sufficient strategy DAG, the Markov factorization property is a theorem — a consequence of the Causal Markov Condition (CMC).

**The Markov factorization property.** Each variable $X_i$ is conditionally independent of its non-descendants given its parents:

$$X_i \perp \text{NonDesc}(X_i) \mid \text{Pa}(X_i)$$

Equivalently, the joint distribution factorizes as:

$$P(X_1, \ldots, X_n) = \prod_{i=1}^{n} P(X_i \mid \text{Pa}(X_i))$$

(The equivalence holds for positive distributions — Lauritzen 1996, Theorem 3.27.)

**The argument has five parts:**

**(a) The DAG is a causal model.** P1 establishes that edges represent causal relationships: completing a parent step causally advances the child step. P2 establishes probabilistic uncertainty over outcomes. Together: $\Sigma_t$ is a causal DAG in the sense of structural causal models (Pearl 2009, Definition 7.1.1) — each node's outcome is determined by its parents' outcomes (through the causal mechanism encoded in the edge credences) plus exogenous uncertainty specific to that step. Formally, each node admits a structural equation:

$$X_i = f_i(\text{Pa}(X_i), \varepsilon_i)$$

where $f_i$ is the local causal mechanism and $\varepsilon_i$ is the exogenous noise (the residual uncertainty at step $i$ not determined by its parents).

**(b) Causal sufficiency implies exogenous independence.** The exogenous terms $\varepsilon_i$ are mutually independent if and only if no unmodeled common cause affects two or more nodes in the graph. This is precisely the **causal sufficiency** assumption: every variable that is a direct common cause of two or more nodes in $\Sigma_t$ is itself a node in $\Sigma_t$.

For agent-constructed strategies, causal sufficiency is a **modeling ideal, not a typical condition**. The agent designed the graph, so all *intended* causal relationships are explicit — but environmental common causes (shared infrastructure, weather, market shifts, correlated adversary actions) routinely affect multiple strategy steps without appearing as nodes. In complex, multi-stakeholder, or adversarial environments, causal insufficiency is the dominant case ( #def-strategy-dag, Correlation Hierarchy). When an environmental factor is omitted, the exogenous terms become correlated and the Markov condition fails. This is model inadequacy ( #result-structural-adaptation-necessity), and the remedy is to add the missing common-cause node — but identifying which common causes matter is a modeling judgment, not a mechanical procedure ( #def-strategy-dag, L1 construction principle). The proof's conditional on causal sufficiency is therefore a condition on model quality: the result holds exactly when the DAG is well-constructed, approximately when it is close, and fails when major common causes are missing. The Correlation Hierarchy in #def-strategy-dag provides the practical framework: L0 (independence, this proof's assumption) gives tractable results; L1 (augmented DAG with explicit common-cause nodes) is the practical default in complex domains; L0 formal results transfer to correctly constructed L1 DAGs.

**(c) The Causal Markov Condition theorem.** For a DAG $G$ over variables $V = \{X_1, \ldots, X_n\}$ with structural equations $X_i = f_i(\text{Pa}(X_i), \varepsilon_i)$ where the $\varepsilon_i$ are mutually independent:

$$P(X_1, \ldots, X_n) = \prod_{i=1}^{n} P(X_i \mid \text{Pa}(X_i))$$

This is the **Causal Markov Condition** — a proved theorem, not a modeling assumption. The standard references are Spirtes, Glymour, and Scheines (2000, Theorem 3.4) and Pearl (2009, §1.4.1, Theorem 1.4.1). The proof applies the chain rule in topological order: $P(X_1, \ldots, X_n) = \prod_i P(X_i \mid X_1, \ldots, X_{i-1})$, then uses the independence of $\varepsilon_i$ to show that conditioning on all predecessors reduces to conditioning on parents only. Each non-parent predecessor's influence on $X_i$ is fully mediated through the parents — its direct contribution enters through the causal mechanism $f_i$, not through $\varepsilon_i$.

**(d) P3 as consequence.** State-local revisability (P3) was originally stated as an independent postulate. The CMC reveals it is a *consequence* of the causal structure under causal sufficiency: since $X_i \perp \text{NonDesc}(X_i) \mid \text{Pa}(X_i)$, updating beliefs about $X_i$ requires only $\text{Pa}(X_i)$ — local revision is automatically correct. No information from the rest of the graph changes the conditional distribution of $X_i$ given its parents. P3 was motivated as an operational requirement (agents *need* local revision for computational tractability, and the persistence condition demands it). The CMC shows the requirement is automatically satisfied by any causally sufficient causal DAG. The two arguments converge from different directions: P3 says local revision is *needed*; the CMC says it is *guaranteed* (under causal sufficiency).

**(e) Connection to edge independence.** The CMC's exogenous independence condition ($\varepsilon_i$ mutually independent) is precisely the **edge-independence assumption** in the AND/OR status propagation ( #def-strategy-dag). When exogenous noise terms are independent, edge outcomes are conditionally independent given parents, and the AND/OR formulas compute correct probabilities. When they are correlated (causal insufficiency — latent common causes), the AND/OR propagation systematically overestimates success because it treats joint failure probability as the product of marginals. The validity of the Markov factorization and the validity of the independence model are the *same condition*: causal sufficiency of $\Sigma_t$. See #def-strategy-dag for the full treatment of correlated failure as the primary case.

**Assembling (a)-(e).** P1-P2 establish that $\Sigma_t$ is a causal DAG with probabilistic uncertainty. Under causal sufficiency (exogenous independence), the CMC theorem proves the Markov factorization. P3 (local revisability) follows as a validated consequence. The Markov property is both operationally required (P3) and structurally guaranteed (CMC). When causal sufficiency fails, the Markov factorization is still the agent's *intended* factorization — the one its DAG represents — but it is wrong about the world. The gap between intended and actual factorization manifests as correlated failure and $\hat P_\Sigma$ overestimation, and the fix is structural: add the missing common-cause nodes to restore causal sufficiency.

#### Step 4: P1 + finite horizon implies acyclicity (proved)

This is the strongest piece of the argument. See the dedicated section below.

#### Step 5: Assembly

P1 (directed edges + causal interpretation) + P2 (probabilistic) + causal sufficiency (CMC → Markov factorization) + P4 (internal nodes) + finite horizon (acyclicity):

**The strategy representation must be representable as a directed acyclic graph with probability distributions at each node conditioned on its parents — a Bayesian network.** P3 (local revisability) is validated as a consequence of this structure, not required as a premise.

### Acyclicity Derivation

*[Derived (from #post-causal-structure + finite planning horizon)]*

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

### What Is Derived vs. What Is Chosen

| Property | Motivating postulate | Strength |
|---|---|---|
| Directed edges | Temporal ordering (P1, #post-causal-structure) | Proved |
| Probabilistic uncertainty | Cox's theorem (P2) | Proved |
| Acyclicity | Temporal ordering + finite horizon (P1) | Proved |
| Internal structure | Fragility + monitoring (P4, #der-chain-confidence-decay) | Derived |
| Markov factorization | Causal Markov Condition theorem (P1 causal interpretation + P2 probability + causal sufficiency) | Proved under causal sufficiency (CMC theorem) |
| **DAG with Markov property** | **P1 + P2 + causal sufficiency (CMC) + P4** | **Conditional on causal sufficiency — which is testable and repairable** |
| AND/OR parameterization | Boolean completeness + parsimony | Hypothesis (binary outcomes only) |
| Single-parameter edges | Parsimony / IB | Formulation choice |
| Specific node ontology | — | Formulation choice |

The dividing line: acyclicity and directed edges are proved; the full DAG-with-Markov-property is conditional on causal sufficiency. The parameterization (AND/OR, CPT form, edge semantics) is a formulation choice within the strongly motivated structure, motivated by parsimony and domain fit but not by mathematical necessity.

### Equivalence Class

**Within the DAG class.** Multiple DAGs can encode the same conditional independence relations, forming a Markov equivalence class identified by a CPDAG (completed partially directed acyclic graph). Two DAGs in the same equivalence class make identical probabilistic predictions but may differ in causal interpretation.

**Across representation types.** Factor graphs, junction trees, influence diagrams, and chain graphs are NOT simple presentational variants of DAGs:

- **Factor graphs** and **junction trees** preserve factorization and inference structure without necessarily preserving directed causal semantics.
- **Influence diagrams** add decision and utility nodes — a richer object, not an equivalent one.
- **Chain graphs** can express independence models that are not representable as DAGs at all.
- **Markov equivalence** is a statement within DAG classes, not across all graphical model types.

The correct claim is narrow: for a given factorized distribution, DAG and factor-graph representations can compute the same marginals. But causal semantics (do-calculus) are DAG-specific and do not transfer to undirected or mixed representations without additional structure.

**AAD's choice.** AAD uses DAG + AND/OR because: (a) AND/OR is the most parsimonious complete basis for binary combination ( #scope-and-or), (b) the DAG naturally supports causal/interventional reasoning (Pearl's do-calculus), and (c) the representation converged across three independent formalism attempts.

## Epistemic Status

The acyclicity derivation is *exact* — it follows from temporal ordering over a finite horizon via standard order theory. The individual postulates P1, P2, and P4 are each well-grounded (temporal structure, Cox's theorem, and chain fragility respectively).

The Markov property is now *proved under causal sufficiency* via the Causal Markov Condition theorem (Spirtes, Glymour & Scheines 2000, Theorem 3.4; Pearl 2009, Theorem 1.4.1). The previous sketch argument (P3 requires locality → P1 identifies parents → therefore Markov) has been replaced by a rigorous chain: P1-P2 establish the causal DAG structure, causal sufficiency guarantees exogenous independence, and the CMC theorem proves the factorization. P3 (local revisability) is now a *consequence* of the Markov property, not a premise — the CMC shows that local revision is automatically correct for causally sufficient DAGs, validating P3's operational requirement.

The conditioning on causal sufficiency is the right level of conditionality: it is a property of *strategy quality* (did the agent include all relevant common causes as nodes?), not of agent architecture. It is testable in principle (correlated residuals after convergence indicate missing common causes) and repairable in practice (add the common-cause node). When causal sufficiency fails, the Markov factorization fails, and this manifests as correlated failure and $\hat P_\Sigma$ overestimation ( #def-strategy-dag). The edge-independence assumption in AND/OR propagation and the causal sufficiency condition for the Markov property are the same condition viewed from different angles.

Max attainable: *exact* for acyclicity (already there). *Derived conditional* for the full DAG-with-Markov-property — the derivation is rigorous (invokes a proved theorem), and the remaining condition (causal sufficiency) is about model quality, not proof quality.

The AND/OR restriction is a *hypothesis* for binary outcomes, grounded in Boolean completeness and parsimony. For non-binary outcomes, it does not apply and richer parameterizations within the derived graphical structure are needed.

The parallel to Cox's theorem is now tighter than previously stated: Cox's theorem proves that consistency axioms force probability; the CMC theorem proves that causal structure under sufficiency forces the Markov factorization. Both are formal results, not analogies. The remaining gap: Cox's axioms are necessary and sufficient for probability; AAD's postulates are sufficient for DAG+Markov structure, but the necessity direction (could a non-DAG structure satisfy P1-P4?) is not established. For practical purposes this gap is unimportant — the proved sufficiency gives a rigorous foundation for the strategy representation.

## Discussion

**The contribution of this analysis.** The dividing line between derived/conditional structure and chosen parameterization is the key result. The agent community (and future researchers) know exactly what is proved (acyclicity, directed edges), what is conditional (Markov property, contingent on causal sufficiency), and what is a formulation choice (the parameterization within the graph). Alternative parameterizations can be explored without abandoning the theoretical foundation.

**Acyclicity deserves emphasis.** The existing theory previously flagged "DAG acyclicity is an assumption, not forced" as a known fragility. The derivation above resolves this: acyclicity of $\Sigma_t$ follows from temporal ordering over a finite planning horizon. This is specific to the strategy — $M_t$'s environment model is not restricted to acyclic structures.

**The causal sufficiency assumption.** The Markov condition assumes causal sufficiency — no hidden common causes within the strategy. Since the agent constructs $\Sigma_t$, there are no "hidden" variables internal to the strategy (the agent chose all the nodes). But environmental common causes that affect multiple strategy steps may violate the Markov condition within $\Sigma_t$. If so, latent variable models or causal graphs with hidden nodes would be needed. This connects to the edge identifiability problem noted in #def-strategy-dag.

## Working Notes

- **P3→Markov: resolved.** The previous gap (P3 could be satisfied by non-Markov sparse factorizations) is resolved by grounding the Markov property in the CMC theorem rather than in P3. The CMC proves the factorization from the causal structure (P1) and causal sufficiency (exogenous independence), making P3 a consequence rather than a premise. The alternative-factorization concern (factor graphs, junction trees) is now moot: the Markov property follows from the causal semantics, not from locality. P3 remains valuable as an *operational requirement* that the CMC-guaranteed factorization satisfies.
- **Parsimony theorem for AND/OR.** Is there a formal result that AND/OR (noisy-AND + noisy-OR) is the unique $O(k)$-parameter complete basis for binary nodes? This would strengthen #scope-and-or from formulation choice to derived. The Boolean completeness half is standard; the uniqueness-under-parsimony half is not established.
- **Non-binary outcome analogs.** For continuous or multi-valued outcomes, the natural analogs of AND/OR might be min/max or additive/multiplicative combination. Is there a completeness result for these? The current argument applies cleanly only to binary outcomes.
- **Environmental common causes and the CMC.** The CMC proof makes the failure mode precise: when unmodeled environmental dependencies (weather, shared infrastructure, market conditions) affect multiple strategy steps, the exogenous noise terms $\varepsilon_i$ become correlated, causal sufficiency fails, and the Markov factorization is violated. The consequence is exactly the correlated-failure phenomenon in #def-strategy-dag: $\hat P_\Sigma$ overestimates success because it treats joint failure probability as the product of marginals. The fix is structural: add the common-cause as a condition node in $\Sigma_t$, restoring causal sufficiency and the Markov property for the augmented DAG. This connects the graph-theoretic result (Markov property) to the strategy-layer result (independence model validity) through a single condition: causal sufficiency.
- **Promotion potential.** With the CMC-based proof, #def-strategy-dag's DAG structure claim is now strongly grounded: acyclicity is proved, the Markov property is proved under causal sufficiency. The remaining "definition" character of strategy-dag is about the *parameterization* (AND/OR, single-parameter edges), which is a formulation choice within the proved graphical structure.
