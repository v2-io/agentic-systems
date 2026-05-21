# Prior-Art Analysis: Causal Plan Graphs and Strategy DAGs

**Target Claim:**
AAT models the "strategy" of an agent not as a reactive policy (Moore machine), but as an explicit Causal Plan Graph (a DAG with probabilistic AND/OR semantics). AAT claims two profound properties of this structure:
1. **Intrinsic Interventional Data (Level 2):** An agent acting in a feedback loop generates Pearl Level-2 interventional data ($do(a)$) simply by acting, bypassing the causal hierarchy barrier between observation (L1) and intervention (L2).
2. **The Triple Depth Penalty:** A causal plan graph degrades severely with depth due to three independent, compounding mechanisms: probability confidence decay, evidence starvation at downstream nodes, and the sheer cognitive cost of maintaining the model structure.

---

## 1. State of the Field & Scientific Precedence

The Undermind search yields highly established prior art from two mostly separate domains: Automated Planning (AI) and Causal Inference. AAT sits squarely at the intersection.

### Pillar 1: Pearl's Calculus of Actions and Interventional Control
The formal distinction between observing an event (conditioning) and forcing an event (intervention) was crystallized by **Judea Pearl (1994, 1995)**.
- Pearl's *Calculus of Actions* explicitly introduced the $do(X)$ operator, providing the mathematical framework to calculate $P(Y \mid do(X=x))$. 
- **Bareinboim et al. (2022)** solidified the "Causal Hierarchy Theorem," proving that Level 2 queries (interventions) cannot, in general, be answered using only Level 1 (associational/observational) data.
- **Ortega and Braun (2008, 2010)** explicitly brought this into adaptive control with their *Bayesian Rule for Adaptive Control based on Causal Interventions*. They noted that when an agent acts, it is not merely observing; its actions are "causal interventions on the I/O stream." This forms a direct conceptual precedent for AAT's claim that the agent loop inherently provides Level 2 data.

### Pillar 2: Probabilistic Planning and AND/OR Graphs
The AI planning community has long modeled plans as graphs and trees with failure probabilities.
- **Kushmerick, Hanks, and Weld (1994, 1995)** developed probabilistic planning algorithms (like BURIDAN) that explicitly model actions with uncertain, context-dependent effects, generating plans that meet a probability-of-success threshold.
- **De Mello and Sanderson (1986)** pioneered the use of **AND/OR graphs** to represent assembly plans, explicitly balancing operational complexity against probability of success.
- **Bryce and Smith (2006)** analyzed "interaction" and "correlation" within plan graphs, recognizing that assuming independence between action preconditions leads to gross overestimates of success probability—a direct precursor to AAT's focus on causal insufficiency and correlation hierarchies in strategy DAGs.

### Pillar 3: Penalties of Depth (Evidence Starvation)
While the phrase "triple depth penalty" is unique to AAT, the underlying mechanisms are known.
- In Reinforcement Learning, **delayed credit assignment** and the exponentially decaying probability of reaching deep states (evidence starvation) are canonical problems addressed by temporal difference learning and eligibility traces.
- In Information Theory, the "cognitive cost" of a strategy aligns with Minimum Description Length (MDL) penalties for complex models.

---

## 2. Key Anchor Papers Identified & Deposited

1. **Pearl, J. (1994). A Probabilistic Calculus of Actions.** (`ref/pearl_calculus_of_actions_1994.pdf`)
   *Significance:* The foundational paper establishing the $do()$ operator, proving that actions are interventions, not passive conditions.
2. **Ortega, P. A., & Braun, D. A. (2008). A Minimum Relative Entropy Principle for Learning and Acting.** (`ref/ortega_adaptive_agent_2008.pdf`)
   *Significance:* Provides a direct precedent for AAT's "loop provides interventional data" claim, treating an active agent's outputs as causal interventions on the I/O stream.
3. **Bryce, D., & Smith, D. E. (2006). Using Correlation to Compute Better Probability Estimates in Plan Graphs.**
   *Significance:* Demonstrates the danger of assuming independence in plan graphs, mirroring AAT's focus on causal insufficiency.
4. **Kushmerick, N., Hanks, S., & Weld, D. S. (1994). An Algorithm for Probabilistic Least-Commitment Planning.**
   *Significance:* Classic AI planning literature establishing the evaluation of plan-success probabilities over sequential, uncertain actions.

---

## 3. Conclusion on Novelty & Overlap

The core building blocks of AAT's strategy representation—Pearl's $do$-calculus, AND/OR planning graphs, and the realization that action constitutes an intervention—are firmly established in the literature. Ortega and Braun (2008) in particular strongly preempt the conceptual claim that an active agent's history is an interventional dataset.

**AAT's Novel Contribution:**
AAT's novelty here is primarily **synthetic and architectural**. 

1. **Synthesis of the Triple Depth Penalty:** While the individual penalties of depth (probability compounding, evidence starvation, MDL complexity) are known in separate subfields, AAT formally synthesizes them into a single, unified "Triple Depth Penalty." It formally binds the structural topology of the DAG (AND/OR semantics) to the cybernetic correction loop (Fisher-local update gain).
2. **The Causal Hierarchy as an Epistemic Boundary:** Rather than just using $do$-calculus to *plan* (as in the AI literature), AAT uses the Causal Hierarchy Theorem as a negative boundary condition for *self-diagnosis*. AAT proves that because the loop provides Level 2 data, the agent *can* theoretically update its DAG. But if the DAG suffers from causal insufficiency (latent common causes between siblings), the independent AND/OR propagation fails, and the agent's on-policy diagnostic collapses. This structural formalization of when strategy graphs fail—and how the loop's Level 2 data is both the requirement and the boundary—is a novel cybernetic framing of causal planning.