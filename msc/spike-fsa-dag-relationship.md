# Spike: FSA/Moore Machine vs. Strategy DAG

**Status**: Exploratory spike — investigating the formal relationship between AAD's strategy DAG and Miller's Moore machine representation of agent strategies.

**Date**: 2026-04-06

**References**: Miller, *Ex Machina* (2022); #strategy-dag; #graph-structure-uniqueness; #composition-closure.

---

## Analysis

AAD's strategy DAG and Miller's Moore machine formalize different aspects of what "strategy" means. They are not competing representations of the same object — they are representations of different objects that both get called "strategy."

**What each encodes.** The Moore machine $(S, A, \tilde{A}, \delta, \lambda, s_0)$ is a *reactive policy*: given the current state and the other agent's last action, produce an output and transition. It encodes a complete input-output mapping over an indefinite horizon. The strategy DAG $\Sigma_t = (V_t, E_t, p_t, \gamma_t)$ is a *causal plan*: a theory of which conditions must hold (AND/OR) and with what credence for the objective to be achieved. It encodes the agent's beliefs about the causal structure of its problem.

**Moore machine to DAG (partial embedding).** A Moore machine with $n$ states can be unrolled over a finite horizon $H$ into a tree of depth $H$ with branching factor $|\tilde{A}|$ (the opponent's action set). Each path through the tree is a sequence of (state, output) pairs — a scenario. This unrolled tree is a DAG (it is acyclic by construction). However, it lacks credence weights and AND/OR semantics. To produce a strategy DAG, one must supply: (a) probabilities over opponent actions at each branch (from $M_t$), and (b) AND/OR combination rules reflecting which branches the agent treats as jointly required vs. alternatively sufficient. The Moore machine does not contain this information — it is agnostic about which opponent responses are likely or which paths matter. The mapping is injective (every Moore machine yields a unique unrolled DAG skeleton) but requires external information to complete.

**DAG to Moore machine (lossy compilation).** A strategy DAG can be "compiled" into a reactive policy by the following (lossy) procedure: enumerate the leaves in topological order, and for each action leaf, define a Moore machine state that outputs that action and transitions based on observed success/failure. This discards: (a) the credence weights (the compiled machine is deterministic), (b) the AND/OR structure (the machine commits to a fixed execution order), and (c) the causal semantics (the machine has no representation of *why* actions are ordered this way). The compiled machine executes the plan but cannot reason about it — it cannot recompute plan-confidence when a leaf credence changes, which is exactly what status propagation provides.

**Generality.** Neither representation is strictly more general. Moore machines can represent reactive strategies with no causal model (tit-for-tat, grim trigger) that have no natural DAG form — there is no "plan" to encode, just a response rule. Strategy DAGs can represent plans with rich conditional structure and uncertainty that would require exponentially many Moore machine states to capture (because the Moore machine must enumerate every possible observation sequence, while the DAG factors through conditional independence). They are *orthogonal*: the Moore machine captures the behavioral surface (what the agent does); the DAG captures the epistemic interior (what the agent believes and why).

**Cycles vs. acyclicity.** The Moore machine's cycles (revisiting states) correspond to the DAG's time-unrolled iteration: the Moore machine state "cooperate" visited at $t=1$ and $t=5$ is a single node in the machine but two distinct nodes $v_{t=1}, v_{t=5}$ in the DAG. The DAG's acyclicity is not a restriction — it is a consequence of temporal indexing (#graph-structure-uniqueness). The Moore machine's cycles are not additional expressiveness — they are a compact encoding of repeated structure that the DAG represents explicitly. For finite horizons, both have equivalent expressive power over behavioral sequences; the Moore machine is exponentially more compact for repetitive strategies.

**Composition.** Miller's product-automaton construction gives *exact* composition: two Moore machines interacting produce a meta-machine whose state space is $S_1 \times S_2$ and whose transitions are deterministic. AAD's composition closure (#composition-closure) uses an *approximate* dynamical homomorphism with closure defect $\varepsilon^*$. These address different questions. The product automaton asks: "what behavior does the pair produce?" (answer: another automaton, exactly). AAD asks: "can this pair be described as a single AAD agent?" (answer: approximately, with bounded error). If strategies were Moore machines, composition of *behavior* would become exact (product automaton), but composition of *agent descriptions* (model $M_t$, objective $O_t$, strategy $\Sigma_t$) would still require the approximate framework — the closure defect comes from projecting the joint internal state, not from composing the policy.

## Summary of Findings

| Question | Status |
|---|---|
| Moore machine embeds in DAG? | Yes, via finite-horizon unrolling, but requires external credence information to complete. |
| DAG compiles to Moore machine? | Lossy — discards credences, AND/OR structure, causal semantics. |
| One strictly more general? | No. Orthogonal: behavioral surface vs. epistemic interior. |
| Cycles vs. acyclicity? | Equivalent for finite horizons; different encoding of the same temporal sequences. |
| Would FSA strategies make composition exact? | Behavioral composition yes (product automaton). Agent-level composition still approximate ($\varepsilon^*$ from internal state projection). |

**The core distinction**: a Moore machine is a *policy* (mapping from histories to actions); a strategy DAG is a *plan with a causal model* (theory of how actions produce outcomes). AAD needs the latter because adaptation requires knowing *why* you are doing something, not just *what* you are doing — otherwise there is no basis for strategy revision when $M_t$ changes.
