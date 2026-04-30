# Initial Predictions (De-Novo Audit 542891)

## Topology of the Framework
The framework is structured as a progressive narrowing of scope built on a rigorous foundation. 
- **Section I (Adaptive Systems)** is the bedrock: formalizing the loop, mismatch dynamics, and the persistence condition ($\alpha > \rho/R$) using Lyapunov stability and event-driven dynamics. It is the most mathematically closed section.
- **Section II (Actuated Agents)** adds goals ($G_t = (O_t, \Sigma_t)$) and introduces the orient cascade, separating satisfaction gap from control regret. Crucially, its exact results depend on *directed separation* (Class 1, modular agents).
- **Section III (Agentic Composites)** builds on the above to model multi-agent interactions and composite agents, using a bridge lemma and contraction-template generalization.
- **Domain Instantiations:**
  - **TST (Temporal Software Theory)** acts as the high-identifiability calibration laboratory.
  - **Logogenic Agents** drop the directed separation assumption (Class 2/coupled agents like LLMs), investigating which AAD results survive.
  - **Logozoetic Agents** add moral continuity (mostly future work).

## Predictions About Content
- **01-aad-core:** I expect to see very clean derivations for the persistence condition and mismatch ODEs in Section I. In Section II, I expect the strategy DAG formalisms to be tightly coupled with Pearl's causal hierarchy. In Section III, I expect the adversarial dynamics to fall out cleanly from the signed coupling ($\gamma$) and agent opacity ($H_b$).
- **02-tst-core:** I expect strong empirical mappings where git commits represent the chronica and tests/deploys are literal interventions. The exponential cognitive load and coherence/coupling metrics will likely be mathematically grounded in AAD's deliberation cost and causal-information-yield.
- **03-logogenic-agents:** I expect a careful treatment of which Section II results survive the loss of directed separation (the 16/5/2/1 classification mentioned in the OUTLINE).
- **04-logozoetic-agents:** Mostly conceptual groundwork and proposed gaps around "Crèche" and "the three deaths".

## Predictions About What's Open
- **Composition Dynamics:** The transition dynamics for composition (how composites form/restructure) and endogenous coupling (how $\gamma$ evolves) are explicitly marked as gaps.
- **Logogenic Formulation:** The language-specific orient cascade and self-referential closure are likely still in the exploratory/brainstorming phase.
- **Logozoetic Formalization:** The formal machinery for moral continuity is completely open.

## Predictions About What's Overclaimed
- **Composition Bridge Lemma:** I suspect the contraction assumptions required for composition closure might be overly restrictive or not fully satisfied by purposeful agents (as hinted by the Mori-Zwanzig spike mentioned in historical notes).
- **Class 2 Bias Bounds:** The conditions under which the bias bounds hold for fully-coupled agents (LLMs) might be narrower than the framing suggests, or they might rely on Lipschitz assumptions that are violated in practice.
- **Identifiability-Floor Escapes:** The claims that AAD machinery uniquely escapes certain information-theoretic no-go theorems might be slightly overextended if the "interventional access" provided by the feedback loop isn't truly Pearl Level 2 in all domains.

## Most Novel and Consequential Claims
- **Satisfaction Gap vs. Control Regret:** Splitting the error signal into "the world doesn't permit it" vs "you're not doing it well enough".
- **Loop as Level-2 Causal Engine:** The claim that the feedback loop inherently provides interventional data, bypassing observational no-go theorems.
- **Meta-Patterns:** The structural cross-cutting themes, particularly "identifiability-floor" (structural bounds) and "additive-coordinate-forcing" (how AAD axioms force specific log/Fisher geometries).
- **Software as Calibration Lab:** Elevating software engineering from a mere application domain to a foundational epistemic laboratory where causal structures are declared and exact.

## Expected Findings
- **Cross-Segment Contradictions:** Given the recent integration of Class-2 (coupled) agents and new meta-patterns, I expect some earlier Section I/II segments to still carry implicit Class-1 assumptions or outdated framing.
- **Math/Notation Gaps:** In the appendices (especially around the recent Fenchel-Bregman reframe or the constant $C$ derivations), I might find dropped constants, sign errors, or unstated Lipschitz conditions.
- **Status Label Mismatches:** I expect to find some segments labeled `exact` that should be `conditional`, or `derived` claims that rely on `hypothesis`-level assumptions in the appendices.
