---
slug: deriv-graph-structure
type: derivation
status: conditional
depends:
  - def-strategy-dag
  - der-chain-confidence-decay
  - norm-explicit-strategy-condition
  - post-causal-structure
stage: claims-verified
---

# Derivation: Strategy Graph Structure

Operational requirements on the agent's representation — directed temporal ordering, probabilistic uncertainty, and the ability to test strategy components — are *sufficient* for the strategy to be a directed acyclic graph with the Markov factorization property. The argument parallels Cox's theorem for probability in *form* but not yet in *strength*: Cox's theorem is necessary-and-sufficient (the only measure satisfying the desiderata is probability); this result is sufficient only (the desiderata guarantee DAG+Markov, but no one has shown a non-DAG structure cannot satisfy them). Acyclicity and directed edges are *proved* from temporal ordering over a finite horizon; the Markov factorization is *proved under causal sufficiency* via the Causal Markov Condition theorem (Spirtes–Glymour–Scheines, Pearl). A fourth postulate (observable intermediates) is required for localized strategic diagnosis but not for the representation or persistence results themselves. The Markov factorization does not by itself make the AND/OR status propagation exact: under causal sufficiency, propagation computes the plan's true success probability for all credences if and only if the strategy DAG is an AND/OR tree.

**How far the Cox parallel goes.** Cox's theorem starts from desiderata on how a rational agent should quantify uncertainty (consistency, universality, continuous functional composition) and proves that the *only* measure satisfying them is probability — necessity. This segment starts from desiderata on how a bounded agent can represent its strategy under causal action (directed temporal order, probabilistic edge uncertainty, causal sufficiency of the chosen nodes) and proves that DAG+Markov *suffices* to satisfy them — sufficiency. The necessity direction — no non-DAG structure (factor graphs, junction trees with cyclic message schedules, chain graphs) can satisfy P1–P4 plus causal sufficiency — is not established here. In practical terms this gap is unimportant because the proved sufficiency gives a rigorous grounding for the DAG structure; claims that AAT's strategy *must* be a DAG should be read as "must-if-sufficient-via-this-route," not as a proved necessity. A stronger Cox-style result is open. The placement of the DAG structure on a footing comparable to probability — a consequence of operational requirements rather than a modeling convenience — holds in the sufficiency direction; the full parallel with Cox awaits a uniqueness argument.

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

**(d) What the CMC gives P3, and what it does not.** State-local revisability (P3) was originally stated as an independent postulate. The CMC supplies half of it. Since $X_i \perp \text{NonDesc}(X_i) \mid \text{Pa}(X_i)$, the joint is a product of one factor per node. Revising one step's mechanism or edge credence therefore changes one factor and nothing else in the representation. Propagating the *consequences* of that revision, or of an observed outcome, is a different matter. On an AND/OR tree, a changed credence at node $i$ changes statuses only along $i$'s single path to the root, so forward recomputation costs the length of that path. On a graph that is not a tree, the forward pass is not exact to begin with (Step 3(e)). Observation is not forward-only either. In the minimal case of Step 3(e), observing $A = 1$ forces $C = 1$, hence $B = 1$ and $R = 1$, which no forward update from $A$ produces. Exact propagation of evidence works by local message passing on singly connected graphs (Pearl 1988) and needs exact inference elsewhere. So the CMC guarantees a local *representation* for every causally sufficient DAG, while local revision of *consequences* holds by the forward pass on trees and by message passing on polytrees. P3 was motivated as an operational requirement (agents *need* local revision for computational tractability, and the persistence condition demands it). The factorization meets the representation half for any causally sufficient DAG, and the tree condition of §"Exactness of Status Propagation" says where the forward pass meets the rest.

**(e) What the factorization does not give: exactness of status propagation.** The AND/OR forward pass of #def-strategy-dag assumes the CMC's exogenous independence, but that independence is not sufficient for it to compute true probabilities. The forward pass multiplies the parents' *marginal* statuses, so it is exact at a node only when that node's parents are independent, and an explicit node feeding two branches that reconverge makes them dependent even when every exogenous term is independent. The minimal case: leaf $C$ with $p_C = 0.5$; $A = \mathrm{AND}(C)$, $B = \mathrm{AND}(C)$ and $R = \mathrm{AND}(A, B)$, all edge credences $1$. The graph is causally sufficient and $P(R) = P(C) = 0.5$, but propagation gives $0.25$. The exact condition is the tree condition derived under "Exactness of Status Propagation" below. When the exogenous terms are correlated (a latent common cause), propagation is biased even on a tree: for two siblings by exactly their covariance, with the sign set by node type ( #def-strategy-dag, Correlation Hierarchy). The Markov factorization and exact propagation are therefore different conditions. The first needs causal sufficiency; the second needs causal sufficiency and a tree.

**Assembling (a)-(e).** P1-P2 establish that $\Sigma_t$ is a causal DAG with probabilistic uncertainty. Under causal sufficiency (exogenous independence), the CMC theorem proves the Markov factorization. P3's representation half (local factors) follows as a consequence; its consequence-propagation half holds on trees (3(d)). The Markov property is both operationally required (P3) and structurally guaranteed (CMC). When causal sufficiency fails, the Markov factorization is still the agent's *intended* factorization — the one its DAG represents — but it is wrong about the world. The gap between intended and actual factorization manifests as correlated failure and a $\hat P_\Sigma$ bias whose sign is set by node type. Adding the missing common-cause nodes restores causal sufficiency and with it the factorization. For the forward pass to compute the factorized model's probabilities exactly, the added nodes must also be placed so that the graph is a tree, or the forward pass must be replaced by exact inference (below).

#### Step 4: P1 + finite horizon implies acyclicity (proved)

This is the strongest piece of the argument. See the dedicated section below.

#### Step 5: Assembly

P1 (directed edges + causal interpretation) + P2 (probabilistic) + causal sufficiency (CMC → Markov factorization) + P4 (internal nodes) + finite horizon (acyclicity):

**The strategy representation must be representable as a directed acyclic graph with probability distributions at each node conditioned on its parents — a Bayesian network.** P3 (local revisability) is met by this structure in the sense of Step 3(d), not required as a premise.

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

### Exactness of Status Propagation

*[Derived (Conditional on the noisy-AND/OR structural equations and causal sufficiency)]*

**Setting.** Read the AND/OR parameterization ( #scope-and-or) as structural equations. Each leaf is $X_v \sim \mathrm{Bernoulli}(p_v)$. Each edge carries a transmission variable $E_{iv} \sim \mathrm{Bernoulli}(p_{iv})$. An AND node is $X_v = \bigwedge_{i \in \mathrm{pa}(v)} (X_i \wedge E_{iv})$ and an OR node is $X_v = \bigvee_{i \in \mathrm{pa}(v)} (X_i \wedge E_{iv})$. Two independences are assumed. Causal sufficiency (Step 3(b)) makes the exogenous terms of different nodes independent. The noisy-AND/OR parameterization makes the transmissions into any one node independent of each other, which is its independence-of-causal-influence assumption (Heckerman & Breese 1996, "Causal Independence for Probability Assessment and Inference Using Bayesian Networks," *IEEE Transactions on Systems, Man, and Cybernetics A* 26(6):826–831). If the transmissions into one node are correlated, even a tree is miscounted. Together the two make all leaf draws and transmissions mutually independent. The first premise can fail where nothing looks shared. Leaves that are exclusive outcomes of one variable, such as "arm $k$ is the best arm" for each $k$ ( #example-strategy), are dependent, because that variable is a common cause outside the graph, and then even a tree is miscounted. For an OR node whose parents' events are disjoint and whose parent statuses are exact, the exact status is $\sum_i p_{iv} s_i$ by additivity. The forward pass's $1 - \prod_i (1 - p_{iv} s_i)$ is smaller whenever two of the terms are positive. The forward pass $s_v$ of #def-strategy-dag is the computation that is exact when every node's parents are independent.

**Result.** For a node $v$, the following are equivalent:

1. $s_v = P(X_v = 1)$ for all leaf and edge credences.
2. Every ancestor of $v$ has exactly one directed path to $v$.

Every node of $\Sigma_t$ has a path to $v_{\text{root}}$ (rootedness, #def-strategy-dag). So, applied at the root: **$\hat P_\Sigma = s_{v_{\text{root}}}$ equals the plan's true success probability for all credences if and only if $\Sigma_t$ is an AND/OR tree**, that is, every node other than the root has exactly one child. Under rootedness this is the same as $\Sigma_t$ being a polytree. For a DAG without a unique sink, exactness at every node needs only the weaker multitree condition: at most one directed path between any two nodes, equivalently no node has two parents whose ancestor-or-self sets meet. The "or-self" matters. In the triangle $a \to b$, $a \to c$, $b \to c$, the parents $a$ and $b$ of $c$ have no strict common ancestor, yet $a$ has two paths to $c$ and propagation is wrong there. The pair $c = \mathrm{AND}(a, b)$, $d = \mathrm{OR}(a, b)$ is a multitree but not a polytree, and propagation is exact at both nodes. A common child of $c$ and $d$ breaks it. Rootedness is what turns the multitree condition into the tree condition.

**Derivation.** *($2 \Rightarrow 1$.)* If every ancestor of $v$ has one path to $v$, the ancestral subgraph of $v$ is a tree. The parents of any node in it therefore have disjoint ancestor sets. Their statuses are functions of disjoint sets of independent exogenous variables, so they are independent. The AND and OR formulas are exact for independent inputs, and $s_v = P(X_v = 1)$ follows by induction in topological order.

*($1 \Rightarrow 2$.)* Treat the credences as indeterminates. $P(X_v = 1)$ is the expectation of a Boolean function of independent Bernoulli variables, so it is multilinear: of degree at most $1$ in each leaf credence $p_\ell$. Write $N(\ell, v)$ for the number of directed paths from leaf $\ell$ to $v$. By induction in topological order, $\deg_{p_\ell} s_v = N(\ell, v)$. At $\ell$ itself, $s_\ell = p_\ell$. An AND status is a product of factors $p_{iv} s_i$, and an OR status is one minus a product of factors $1 - p_{iv} s_i$. Each factor has the same degree in $p_\ell$ as $s_i$ whenever that degree is positive, and degrees add under products in a polynomial ring. If some ancestor $u$ of $v$ has two paths to $v$, any leaf $\ell$ at or above $u$ has $N(\ell, v) \geq 2$. Then $s_v$ and $P(X_v = 1)$ are different polynomials. A polynomial that vanishes on the whole credence box $[0,1]^n$ is zero, so the two differ at some credences. $\square$

The difference polynomial is nonzero, so on a graph that is not a tree the forward pass is exact only on a measure-zero set of credences. That set includes degenerate values such as $p_C \in \{0, 1\}$ in the minimal case of Step 3(e). The mechanism behind the degree count is exact. By the recursion, $s_v$ is the true probability of $v$ on the *path-unfolded tree*: the tree that copies each ancestor once per path to $v$, each copy with its own independent noise. The forward pass therefore counts a leaf reached by $N$ paths as $N$ independent draws where the world has one. The degree identity is a corollary of this. Fixed edge credences in $(0, 1]$ suffice for failure: at any such values, the forward pass on a graph that is not a tree is wrong at generic leaf credences.

**Sign of the error under reconvergence.** Call a node *reconvergent* if two of its parents have ancestor-or-self sets that meet. Every $X_v$ is a nondecreasing function of the independent exogenous variables. Nondecreasing functions of independent variables are positively associated (Esary, Proschan & Walkup 1967, "Association of Random Variables, with Applications," *Annals of Mathematical Statistics* 38(5):1466–1474). So at a reconvergent node whose parents' statuses are exact, the AND formula never overestimates and the OR formula never underestimates. At a node that is not reconvergent, the parents are independent, so the formula is exact on exact inputs. Both formulas are nondecreasing in their inputs, so any node passes an input bias through with its sign unchanged. Induction in topological order then gives the result. **If every reconvergent node is AND, $s_v \leq P(X_v = 1)$ at every node; if every reconvergent node is OR, $s_v \geq P(X_v = 1)$ at every node.** The node types elsewhere are free. Equality holds on trees, where no node is reconvergent. When reconvergent nodes of both types are present, the sign can flip within one graph. Take root $\mathrm{OR}(X, Y)$, with $X$ an AND reconvergence over leaf $C$ and $Y$ an OR reconvergence over leaf $D$, all edges at credence $1$. The root error is $-0.240$ at $(p_C, p_D) = (0.5, 0.01)$ and $+0.245$ at $(0.01, 0.5)$. The common plan shape, OR near the root and AND inside, is covered whenever the reconvergence happens at OR nodes. `#example-L1`'s naive L1 reconverges at its OR root, so its overestimate is an instance. This is the explicit-reconvergence counterpart of the two-sibling $\pm\mathrm{Cov}$ table in #def-strategy-dag, which treats a latent shared cause.

**Exact computation on graphs that are not trees.** On a causally sufficient DAG that is not a tree, $P(v_{\text{root}})$ is still fixed by the graph and its credences, but computing it takes exact inference. One route clamps a set of leaves (or individual transmissions) such that every exogenous variable still left random has at most one path to the root. Each clamped configuration is then evaluated exactly by a forward pass, by the same argument as $2 \Rightarrow 1$, so $k$ binary clamped variables cost $2^k$ forward passes. When a reconvergent node is internal, clamping it is not a forward-pass operation, because conditioning on it changes its ancestors' distribution. Pearl's cutset conditioning is the general form of this route: it instantiates the cutset as evidence and runs polytree belief propagation (Pearl 1988, *Probabilistic Reasoning in Intelligent Systems*, ch. 4). A second route is the junction-tree algorithm, at cost exponential in the treewidth of the moralized graph, which a noisy-OR node with many parents makes large unless it is factored (Lauritzen & Spiegelhalter 1988, "Local Computations with Probabilities on Graphical Structures and Their Application to Expert Systems," *Journal of the Royal Statistical Society B* 50(2):157–224). The repairs in #def-strategy-dag's Correlation Hierarchy are instances. Factoring a strict-prerequisite common cause above the branches it gates (L1) rewrites a reconvergent subgraph into a tree, by distributivity: $\mathrm{OR}(C \wedge A_1, C \wedge A_2) = C \wedge \mathrm{OR}(A_1, A_2)$. On the left $C$ has two children; on the right it has one. The identity needs $C$ to enter each branch as an AND-parent, so that the branch fails whenever $C$ fails. This is the strict-prerequisite condition $\theta_{\text{child}\mid\neg C} = 0$, and it is why L1 is scoped to strict prerequisites. The credence of $C$'s edges need not be $1$: each edge's transmission is independent and moves into its branch, $C \wedge E_{C,i} \wedge A_i = C \wedge (E_{C,i} \wedge A_i)$. The mixture form L1' and explicit conditioning clamp a common cause that is a leaf (a condition node), so they are exact instances of the first route. The same fact is standard in two neighboring literatures. In Bayesian networks, Pearl's propagation is exact on singly connected graphs (Pearl 1988). It needs that stronger condition because it also handles evidence; a forward pass with no evidence needs only the multitree condition, which is why the multitree case above exists. In fault-tree analysis, gate-by-gate probability arithmetic is exact only when no basic event is repeated, and repeated events are handled through minimal cut sets (Vesely et al. 1981, *Fault Tree Handbook*, NUREG-0492).

### What Is Derived vs. What Is Chosen

| Property | Motivating postulate | Strength |
|---|---|---|
| Directed edges | Temporal ordering (P1, #post-causal-structure) | Proved |
| Probabilistic uncertainty | Cox's theorem (P2) | Proved |
| Acyclicity | Temporal ordering + finite horizon (P1) | Proved |
| Internal structure | Fragility + monitoring (P4, #der-chain-confidence-decay) | Derived |
| Markov factorization | Causal Markov Condition theorem (P1 causal interpretation + P2 probability + causal sufficiency) | Proved under causal sufficiency (CMC theorem) |
| **DAG with Markov property** | **P1 + P2 + causal sufficiency (CMC) + P4** | **Conditional on causal sufficiency — which is testable and repairable** |
| Exact status propagation | Noisy-AND/OR equations + causal sufficiency + tree structure | Proved: exact for all credences iff the DAG is an AND/OR tree (§"Exactness of Status Propagation") |
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

**AAT's choice.** AAT uses DAG + AND/OR because: (a) AND/OR is the most parsimonious complete basis for binary combination ( #scope-and-or), (b) the DAG naturally supports causal/interventional reasoning (Pearl's do-calculus), and (c) the representation converged across three independent formalism attempts.

## Epistemic Status

The acyclicity derivation is *exact* — it follows from temporal ordering over a finite horizon via standard order theory. The individual postulates P1, P2, and P4 are each well-grounded (temporal structure, Cox's theorem, and chain fragility respectively).

The Markov property is now *proved under causal sufficiency* via the Causal Markov Condition theorem (Spirtes, Glymour & Scheines 2000, Theorem 3.4; Pearl 2009, Theorem 1.4.1). The previous sketch argument (P3 requires locality → P1 identifies parents → therefore Markov) has been replaced by a rigorous chain: P1-P2 establish the causal DAG structure, causal sufficiency guarantees exogenous independence, and the CMC theorem proves the factorization. P3 (local revisability) is now met by the Markov property rather than assumed: the CMC makes the representation local for every causally sufficient DAG, and forward revision of consequences is exact on AND/OR trees (Step 3(d), §"Exactness of Status Propagation").

The conditioning on causal sufficiency is the right level of conditionality: it is a property of *strategy quality* (did the agent include all relevant common causes as nodes?), not of agent architecture. It is testable — under exploration: on-policy residuals cannot reveal a missing common cause ( #der-causal-insufficiency-detection, the no-go), but pairwise sibling covariance under the agent's own interventions can — and repairable in practice (add the common-cause node). When causal sufficiency fails, the Markov factorization fails, and this manifests as correlated failure and sign-determined $\hat P_\Sigma$ bias — overestimation for the common OR-dominated-root case ( #def-strategy-dag). Causal sufficiency is necessary for exact status propagation but not sufficient. The exactness result (§"Exactness of Status Propagation") is *exact* under its stated premises (the noisy-AND/OR structural equations and causal sufficiency): propagation is exact for all credences if and only if the DAG is an AND/OR tree. The sign result in the same section (propagation is a lower bound when every reconvergent node is AND, an upper bound when every one is OR) is exact under the same premises; it was proposed by the independent verifier and re-derived by the integrator.

Max attainable: *exact* for acyclicity (already there). *Derived conditional* for the full DAG-with-Markov-property — the derivation is rigorous (invokes a proved theorem), and the remaining condition (causal sufficiency) is about model quality, not proof quality.

The AND/OR restriction is a *hypothesis* for binary outcomes, grounded in Boolean completeness and parsimony. For non-binary outcomes, it does not apply and richer parameterizations within the derived graphical structure are needed.

The parallel to Cox's theorem is now tighter than previously stated: Cox's theorem proves that consistency axioms force probability; the CMC theorem proves that causal structure under sufficiency forces the Markov factorization. Both are formal results, not analogies. The remaining gap: Cox's axioms are necessary and sufficient for probability; AAT's postulates are sufficient for DAG+Markov structure, but the necessity direction (could a non-DAG structure satisfy P1-P4?) is not established. For practical purposes this gap is unimportant — the proved sufficiency gives a rigorous foundation for the strategy representation.

## Discussion

**The contribution of this analysis.** The dividing line between derived/conditional structure and chosen parameterization is the key result. The agent community (and future researchers) know exactly what is proved (acyclicity, directed edges), what is conditional (Markov property, contingent on causal sufficiency), and what is a formulation choice (the parameterization within the graph). Alternative parameterizations can be explored without abandoning the theoretical foundation.

**Acyclicity deserves emphasis.** The existing theory previously flagged "DAG acyclicity is an assumption, not forced" as a known fragility. The derivation above resolves this: acyclicity of $\Sigma_t$ follows from temporal ordering over a finite planning horizon. This is specific to the strategy — $M_t$'s environment model is not restricted to acyclic structures.

**The causal sufficiency assumption.** The Markov condition assumes causal sufficiency — no hidden common causes within the strategy. Since the agent constructs $\Sigma_t$, there are no "hidden" variables internal to the strategy (the agent chose all the nodes). But environmental common causes that affect multiple strategy steps may violate the Markov condition within $\Sigma_t$. If so, latent variable models or causal graphs with hidden nodes would be needed. This connects to the edge identifiability problem noted in #def-strategy-dag.

## Working Notes

- **P3→Markov: resolved.** The previous gap (P3 could be satisfied by non-Markov sparse factorizations) is resolved by grounding the Markov property in the CMC theorem rather than in P3. The CMC proves the factorization from the causal structure (P1) and causal sufficiency (exogenous independence), making P3 a consequence rather than a premise. The alternative-factorization concern (factor graphs, junction trees) is now moot: the Markov property follows from the causal semantics, not from locality. P3 remains valuable as an *operational requirement*. The CMC-guaranteed factorization satisfies its representation half; forward revision of consequences is exact only on trees (Step 3(d)).
- **Parsimony theorem for AND/OR.** Is there a formal result that AND/OR (noisy-AND + noisy-OR) is the unique $O(k)$-parameter complete basis for binary nodes? This would strengthen #scope-and-or from formulation choice to derived. The Boolean completeness half is standard; the uniqueness-under-parsimony half is not established.
- **Non-binary outcome analogs.** For continuous or multi-valued outcomes, the natural analogs of AND/OR might be min/max or additive/multiplicative combination. Is there a completeness result for these? The current argument applies cleanly only to binary outcomes.
- **Environmental common causes and the CMC.** The CMC proof makes the failure mode precise: when unmodeled environmental dependencies (weather, shared infrastructure, market conditions) affect multiple strategy steps, the exogenous noise terms $\varepsilon_i$ become correlated, causal sufficiency fails, and the Markov factorization is violated. The consequence is exactly the correlated-failure phenomenon in #def-strategy-dag: $\hat P_\Sigma$ overestimates success because it treats joint failure probability as the product of marginals. The fix is structural: add the common-cause as a condition node in $\Sigma_t$, restoring causal sufficiency and the Markov property for the augmented DAG. Exact propagation on the augmented DAG also needs the node placed so the graph stays a tree (§"Exactness of Status Propagation"); a common-cause node with two children that reconverge is causally sufficient and still miscounted.
- **Promotion potential.** With the CMC-based proof, #def-strategy-dag's DAG structure claim is now strongly grounded: acyclicity is proved, the Markov property is proved under causal sufficiency. The remaining "definition" character of strategy-dag is about the *parameterization* (AND/OR, single-parameter edges), which is a formulation choice within the proved graphical structure.

### Incidental audit gold (gold-lift, 2026-05-31)

Cross-audit ideation harvested from de-novo auditors' working dirs, deduplicated and lightly attributed. Orthogonal framing / pedagogy; off-ramp (time-unrolled scope clarification) at the end. **Coverage:** two substrates reached a dedicated digested reflection (Gemini, AUDIT-WORKING-193847; Gemini-voiced, AUDIT-WORKING-773921); three batched strategy-DAG walks touched it by reference and converged on the same praise (Claude, AUDIT-WORKING-471203; Claude, AUDIT-WORKING-963715; Claude, AUDIT-WORKING-451729).

#### 1. Candidate Brief prose / pre-prose

- **"The Markov property in planning is a guaranteed consequence of a causally-sufficient world-model, not an arbitrary RL convenience."** The recurring one-line synthesis: many planning frameworks (A*, MCTS) *assume* DAG structure and Markov factorization; here acyclicity is derived from temporal ordering and the factorization from the Causal Markov Condition under causal sufficiency. A plain-language anchor (Gemini, AUDIT-WORKING-193847; Gemini-voiced, AUDIT-WORKING-773921).
- **"You can't cause your own prerequisite."** Acyclicity in one breath: a strategy is about *causing future events*, and a finite-horizon plan is a finite poset ordered by time, representable as a DAG (its Hasse diagram) — the same argument as the acyclicity of Pearl's causal DAGs, applied to strategy. Named as "a quiet structural contribution that's easy to miss" (Claude, AUDIT-WORKING-963715; the poset/Hasse framing, AUDIT-WORKING-773921).

#### 2. Candidate Discussion

- **The Cox's-theorem-parallel as an epistemic-humility exemplar.** The segment proves the DAG structure is *sufficient* (a Markov DAG meets all operational requirements) but explicitly flags *necessity* (no other structure could) as open, parallel to "Cox's theorem in form but not yet in strength." Two substrates read this self-restraint as a trust-building move worth preserving prominently — and the "What Is Derived vs. What Is Chosen" table was independently called "the platinum standard for epistemic clarity," pre-empting any "you just assumed a DAG" critique by showing exactly which physics/information postulates force it (Gemini-voiced, AUDIT-WORKING-773921; Gemini, AUDIT-WORKING-193847).
- **Local revisability (P3) demoted from premise to derived consequence.** Auditors flagged the refactor that turns Postulate 3 into a *consequence* of the CMC as "stunning structural refactoring" / "the theory simplifying and tightening itself" — candidate to surface as a worked example of the framework tightening its own axiom set (Gemini, AUDIT-WORKING-193847; Gemini-voiced, AUDIT-WORKING-773921).
- **"Paranoia" as the active search for hidden common causes.** The causal-sufficiency failure mode (omitting environmental common causes correlates the exogenous $\varepsilon_i$, so $\hat P_\Sigma = \prod p_i$ becomes wildly optimistic) glossed as: an agent naturally drifts to L0 independence because it is cheaper, so it must be *forced* to compute the covariance of its failures $\hat\rho_{ij}$ to detect missing L1 common causes. "A mind without paranoia is mathematically guaranteed to be blindsided by correlated failure" — a vivid framing of the existing common-cause Working Note (Gemini, AUDIT-WORKING-193847).

#### 3. Follow-up items

- **AND/OR parsimony / uniqueness.** Both the segment's own Working Note and an auditor flag the same open: if AND/OR (noisy-AND + noisy-OR) can be proven the *unique* $O(k)$-parameter complete basis for binary combination, `#scope-and-or` upgrades from formulation-choice to derived — "locking the entire strategy structure into pure math" (Gemini-voiced, AUDIT-WORKING-773921).
- **Necessity direction stays watched downstream.** Auditors note a consistency-watch: downstream segments should not treat the DAG as the *only* possible strategy representation while necessity is open (Claude, AUDIT-WORKING-451729).

#### 4. Readers often ask / wonder

- **"What forces the agent to fix a missing common cause?"** The CMC framing makes the trigger precise but uncomfortable: causal-sufficiency violations show up as *correlated residuals after convergence*, so the agent must experience repeated inexplicable joint failures before it can trigger L1 structural adaptation to add the missing node — a reader may want this failure-then-repair loop made explicit (Gemini, AUDIT-WORKING-193847).

#### Belongs elsewhere

- **The L0/L1/L1'/L2 correlation hierarchy belongs to `#def-strategy-dag`, not this appendix.** Auditors locate the richer correlation-hierarchy content (direction/magnitude of bias; the "structurally refuted" L1'-with-unobservable-common-cause identifiability obstruction) in `#def-strategy-dag`; this appendix carries the acyclicity + CMC-factorization proofs. Noted so a future promoter routes correlation-hierarchy gold to the definition segment (Claude, AUDIT-WORKING-451729, AUDIT-WORKING-963715).

#### Off-ramp (NOT gold) — routed for adjudication

- **Acyclicity holds only for the *time-unrolled* execution graph, not a state-folded policy graph — make the scope explicit.** Gemini (AUDIT-WORKING-193847): the proof ("a cycle would require $\tau_i \lt \dots \lt \tau_i$, impossible for a real time index") is valid when nodes are *time-indexed events*, but if the strategy DAG were folded over *states of the world* (e.g. "at home" recurring at $\tau_1$ and $\tau_3$), cycles are physical and common — a finite-state-machine / general-MDP transition graph is cyclic. The segment already handles this in its "iteration objection resolved" section ("each attempt is a distinct node at a distinct time"), but the suggestion is to state explicitly at Step 1 that $\Sigma_t$ is a time-unrolled execution graph, *not* a policy-over-states $\pi(S)$ — because rolling $\Sigma_t$ up into a state-policy loses the DAG structure. Scope-honesty sharpening of an already-defended point, not a refutation.

---
