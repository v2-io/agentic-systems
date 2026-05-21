# Prior-Art Analysis: Credit Assignment Boundary and Observability

**Target Claim:**
AAT characterizes the mathematical boundary between tractable and intractable "credit assignment" over a strategy graph (the process of attributing an observed plan-level failure to specific edges in the DAG). AAT proves that exact per-edge attribution in a general AND/OR DAG with partial observability is computationally intractable (\#P-hard) because it takes the form of a Shapley value over a weighted threshold game. Furthermore, it is information-theoretically underdetermined when unobservable intermediate nodes exceed a certain threshold.

To resolve this, AAT elevates "Observability-by-Design" from an engineering best-practice to a structural imperative. By intentionally inserting observable intermediate nodes (checkpoints) into the strategy DAG, an agent explicitly breaks the \#P-hard credit assignment problem into decoupled, tractable, polynomial-time sub-problems. AAT maps this directly to human organizational frameworks like OKRs (Objectives and Key Results), framing them as cybernetic mechanisms that guarantee componentwise observability.

---

## 1. State of the Field & Scientific Precedence

The Undermind search yields highly mature prior art across computational complexity, causal inference, and organizational economics. The structural hardness of assigning blame and the economic necessity of observability are well-established facts.

### Pillar 1: Complexity of Causal Responsibility and Blame
The formal task of assigning "blame" to a specific node in a causal graph for a final outcome has been extensively mapped.
- **Chockler and Halpern (2003)** in *Responsibility and blame: a structural-model approach* provided the canonical framework for quantifying the degree of responsibility a specific variable has for an outcome in a Pearl-style structural causal model.
- **Eiter and Lukasiewicz (2001, 2002)** and **Aleksandrowicz et al. (2014)** established the exact computational complexity of this task. They proved that computing actual cause, responsibility, and blame in structural models is generally NP-complete or $\Sigma_2^P$-complete in binary models, and highly intractable in general networks.

### Pillar 2: Shapley Values and \#P-Hardness
AAT's specific claim that credit assignment takes the form of a Shapley value—and is therefore \#P-hard—is fully validated by the literature on Boolean circuits and cooperative games.
- **Arenas et al. (2020)** and **Karmakar et al. (2024)** studied the problem of quantifying the contribution of individual variables to the outcome of Boolean functions using Shapley/SHAP scores. They proved that computing these scores over general Boolean models is \#P-hard (equivalent to the model counting problem), while identifying specific "islands of tractability" (like deterministic decomposable circuits) where it can be done in polynomial time.

### Pillar 3: Moral Hazard and Observability in Organizations
The economic necessity of inserting observable checkpoints to solve credit assignment is the foundation of Contract Theory.
- **Holmstrom (1979)** in *Moral Hazard and Observability* proved that in a principal-agent relationship, any signal (observable intermediate) that provides information about the agent's hidden action must be included in the contract to achieve optimal credit assignment.
- **Baker (1992)** and **Ethiraj and Levinthal (2009)** extended this to complex organizations, showing that when terminal goals are hard to measure (or highly delayed), management must artificially insert intermediate, observable performance measures (like KPIs or OKRs) to coordinate behavior and prevent a "performance freeze."

---

## 2. Key Anchor Papers Identified

1. **Chockler, H., & Halpern, J. Y. (2003). Responsibility and blame: a structural-model approach.**
   *Significance:* The seminal paper establishing the formal semantics for quantifying the contribution (blame) of an intermediate node to a final outcome in a causal graph.
2. **Eiter, T., & Lukasiewicz, T. (2001). Complexity results for structure-based causality.**
   *Significance:* The rigorous proof that assigning causal responsibility in structural models is computationally intractable in the general case.
3. **Arenas, M., et al. (2020). The Tractability of SHAP-Score-Based Explanations for Classification over Deterministic and Decomposable Boolean Circuits.**
   *Significance:* Proves that assigning credit (Shapley values) over Boolean functions is \#P-hard, validating AAT's core computational boundary claim.
4. **Holmstrom, B. R. (1979). Moral Hazard and Observability.**
   *Significance:* The foundational economic proof that observability of intermediate states is the absolute prerequisite for solving the credit assignment/moral hazard problem.

---

## 3. Conclusion on Novelty & Overlap

The intractability of assigning blame in causal networks (Eiter, Halpern) and the \#P-hardness of Shapley values on Boolean functions (Arenas) are settled theorems in computer science. The economic need for observability (Holmstrom) is a settled theorem in economics. AAT does not claim to have discovered these limits.

**AAT's Novel Contribution:**
AAT's contribution is **Architectural Synthesis and Domain Mapping**. 

1. **Cybernetic Unification of Economics and AI:** AAT bridges the \#P-hard complexity class of computer science directly to the organizational mechanics of human teams. It takes Holmstrom's economic insight (observability solves moral hazard) and Arenas's computational insight (\#P-hard Shapley values) and unites them inside the cybernetic tracking loop of a single agent. 
2. **OKRs as Epistemic Tractability Hacks:** AAT's novel framing is treating human organizational frameworks like OKRs (Objectives and Key Results) not merely as management heuristics, but as rigorous "epistemic tractability hacks." By mapping OKRs directly onto its strategy DAG, AAT proves that an OKR is mathematically equivalent to inserting a fully observable intermediate node into a causal graph. This insertion forcibly breaks a \#P-hard, exponentially correlated posterior calculation into a set of decoupled, polynomial-time Beta-Bernoulli updates. Framing organizational design as a literal topological modification to an agent's internal causal graph to escape the \#P-hard boundary is a highly novel synthesis of computer science and management theory.