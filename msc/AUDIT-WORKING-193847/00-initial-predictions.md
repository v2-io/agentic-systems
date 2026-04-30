# Initial Predictions and Top-Level Model

## Topology of the Framework
The Agentic Systems Framework (ASF) consists of a mathematical core and three progressively more domain-specific/speculative application layers:
1.  **01-aad-core (Adaptation and Actuation Dynamics)**: The foundation. Divided into three sections:
    *   **Section I (Adaptive Systems)**: Focuses on the feedback loop, mismatch dynamics, update gain, and structural persistence ($\alpha > \rho/R$). Inherits heavily from prior Temporal Feedback Theory (TFT). Mathematically mature.
    *   **Section II (Actuated Agents)**: Introduces explicit goals ($O_t$) and strategies ($\Sigma_t$ as a causal DAG). It splits the agent state into epistemic ($M_t$) and purposeful ($G_t$). Key architectural assumption here is "directed separation" (Class 1 agents), where epistemic updates are goal-blind.
    *   **Section III (Agentic Composites)**: Scales to multi-agent and adversarial scenarios, detailing how interacting agents form composites and the thresholds for their stability. Less mature, more structural sketches.
2.  **02-tst-core (Temporal Software Theory)**: Acts as the "privileged high-identifiability calibration laboratory" for AAD. Software development is mapped to AAD dynamics (e.g., git commits as interventions, test failures as mismatch).
3.  **03-logogenic-agents**: LLM-based agents. Crucially, these are "Class 2" agents where directed separation fails because language models process observations and goals through the same coupled mechanism. Focuses on what AAD results survive or degrade in this coupled regime.
4.  **04-logozoetic-agents**: Highly speculative future work regarding agents with moral continuity, theory of mind, and identity persistence.

## Predictions about Component Contents
*   **01-aad-core**: I predict Section I will rely heavily on Lyapunov stability proofs and information theory (Information Bottleneck). Section II will lean on Pearl's causal hierarchy to justify the need for interventional data (Level 2) to update strategy DAGs. Section III will likely use game-theoretic concepts (e.g., zero-sum dynamics, equilibrium convergence) mapped onto the persistence condition to derive adversarial advantages.
*   **02-tst-core**: I expect to see exact mappings where developer tempo is limited by codebase coherence/coupling, and where software practices like CI/CD are proven optimal under AAD's persistence bounds.
*   **03-logogenic-agents**: I predict this will heavily feature ambiguity and bias bounds, detailing how the lack of directed separation creates intrinsic limits on LLM agent reasoning or correction speed.
*   **04-logozoetic-agents**: I predict this will be mostly philosophical, defining preconditions for identity (like cryptographic exteriorization of the chronica) without tight mathematical proofs yet.

## Predictions about Open Questions
*   **Composition Dynamics**: Section III likely has gaps around how dynamically emerging coalitions of agents achieve "directed separation" as a composite, especially if the sub-agents are Class 2.
*   **Coupled Update Rules**: The exact mathematical form of the coupled update for logogenic agents (where $M_t$ and $G_t$ update simultaneously) is likely an open, approximated frontier rather than a closed-form solution.
*   **Strategy Complexity**: In Section II, maintaining a full probabilistic DAG for strategy ($\Sigma_t$) seems computationally explosive; the rules for pruning or bounding this DAG are likely open or heuristic.

## Predictions about Overclaimed Areas
*   **Git as Causal Interventions**: TST claims software is a perfect calibration lab. I suspect the claim that git commits are clean "interventions" ($do(a)$) might overclaim, as real-world commits often batch multiple latent causal changes, making precise causal discovery from git history noisier than assumed.
*   **Directed Separation Universality**: While Section II is explicitly scoped to Class 1, I suspect some downstream claims or discussions might accidentally assume directed separation holds more broadly than it actually does.
*   **Information Bottleneck Application**: The application of Tishby's Information Bottleneck to strategy complexity might be stated exactly but only practically calculable under extremely restrictive assumptions.

## Most Novel and Consequential Aspects
*   **Satisfaction Gap vs. Control Regret**: Splitting the error signal into "the world doesn't permit it" vs. "you're doing it wrong" is a powerful diagnostic tool.
*   **The Persistence Condition ($\alpha > \rho/R$)**: Using a single inequality to unify Kalman stability, RL convergence, and software maintainability is a massive structural insight.
*   **Class 1 vs. Class 2 Distinction**: Recognizing that LLMs fail "directed separation" by construction, and using that to explain their specific failure modes compared to traditional control systems.

## Expected Findings
*   **Scope/Status Mismatches**: Finding conditional results (especially those relying on Class 1 modularity) being summarized or discussed as if they are universal.
*   **Cross-Segment Contradictions**: As new scope routes were added (like the Class 2 logogenic agents), earlier AAD core segments might have definitions that strictly exclude them.
*   **Math Errors/Assumptions**: In derivations (Appendices) for Section II and III, especially regarding independence assumptions in the strategy DAG updates or multi-agent coupling.
*   **Dependency Graph Drift**: Minor violations in the OUTLINE order where a segment references a concept formalized slightly downstream.
