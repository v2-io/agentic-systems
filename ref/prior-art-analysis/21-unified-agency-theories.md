# Prior-Art Analysis: Unified Agency Theories

**Target Claim:**
AAT serves as an overarching, mathematically unified theory of agency that bridges adaptive cybernetics, control theory, and information geometry into a single framework applicable across the "Agent Spectrum" (from thermostats to AGI). It models agency not as a biological exclusive or an algorithmic optimization, but as a formal physical and structural phenomenon defined by causal intervention, information bottleneck compression, and Lyapunov persistence. AAT positions itself as a rigorous alternative to existing grand unified theories (like Active Inference or AIXI), specifically replacing their reliance on thermodynamic non-equilibrium steady states (NESS) and "priors-as-preferences" with classical control-theoretic sector bounds and decision-theoretic regret.

---

## 1. State of the Field & Scientific Precedence

The Undermind search yields a massive, highly cited body of literature attempting to formulate a "Theory of Everything" for agency and intelligence. The desire to unify perception, action, and planning under a single mathematical formalism has driven the most ambitious theoretical AI and cognitive science research of the last 25 years.

### Pillar 1: Active Inference and the Free Energy Principle
The closest and most dominant formal antecedent to AAT is the **Free Energy Principle (FEP)** and **Active Inference**.
- **Friston (2010, 2012, 2015, 2019)** has iteratively built FEP into a universal framework where biological and artificial systems survive by minimizing variational free energy. In Active Inference, perception, action, and exploration are completely unified under a single objective (Expected Free Energy). 
- **Parr, Da Costa, and Friston (2019, 2021)** have formalized this as "Bayesian Mechanics," tying Markov blankets and information geometry directly to stochastic thermodynamics and Non-Equilibrium Steady States (NESS). This is the exact domain in which AAT operates.

### Pillar 2: Universal AI and Algorithmic Intelligence
The effort to mathematically define the absolute limit of agentic capacity stems from algorithmic information theory.
- **Hutter (2000, 2007)** introduced **AIXI**, a parameterless theory of universal artificial intelligence that combines Solomonoff induction with sequential decision theory. 
- **Legg and Hutter (2007)** formulated a formal, universal measure of machine intelligence based on this framework. Unlike FEP, which focuses on biological survival, Universal AI focuses on theoretical limits of expected reward maximization in unknown environments.

### Pillar 3: Information-Theoretic Bounded Rationality
The unification of bounded capacity with action selection is heavily formalized.
- **Ortega and Braun (2012, 2015)** and **Tishby and Polani (2011)** model decision-making fundamentally as a thermodynamic or rate-distortion problem. They prove that bounded rational decision-makers trading off expected utility against information-processing costs (relative entropy) naturally optimize a free-energy functional, providing a formal bridge between physics, information theory, and decision theory.

### Pillar 4: Enactivism and Autopoiesis
In philosophy of mind and complex systems, theories of agency focus on boundary maintenance and structural autonomy.
- **Maturana and Varela (1980)** defined *Autopoiesis* (self-creation), which **Di Paolo (2005)** and **Barandiaran et al. (2009)** extended into *Enactive Agency*. They define agency via normativity, individuality, and causal asymmetry, framing agency as the continuous effort to maintain systemic integrity against environmental entropy (highly analogous to AAT's focus on maintaining the Lyapunov sector condition).

---

## 2. Key Anchor Papers (Available in `/ref`)

1. **Friston, K. J. (2019). A free energy principle for a particular physics.** 
   *Significance:* The apex of FEP, establishing Markov blankets and free energy as the universal physics of self-organizing systems.
2. **Hutter, M. (2000). A Theory of Universal Artificial Intelligence based on Algorithmic Complexity.** 
   *Significance:* The foundational text for AIXI, establishing the theoretical limit of uncomputable optimal agency.
3. **Ortega, P. A., & Braun, D. A. (2012). Thermodynamics as a theory of decision-making with information-processing costs.** 
   *Significance:* Unifies expected utility maximization with the physical costs of information processing using variational free energy.
4. **Levine, S. (2018). Reinforcement Learning and Control as Probabilistic Inference.** 
   *Significance:* The definitive review bridging modern RL/control with the exact variational inference math used by FEP and AAT.

---

## 3. Conclusion on Novelty & Overlap

The *ambition* of creating a mathematically unified theory of agency that bridges physics, control, and information theory is not novel; it is the explicit, highly contested territory of Karl Friston, Marcus Hutter, and Pedro Ortega. Furthermore, the mathematical *shape* of the resulting unifications—variational inference bounds, KL-divergence regularizers, and information bottlenecks—is shared across all these frameworks.

**AAT's Novel Contribution:**
AAT's overarching novelty lies in its **Epistemological Foundation** and its **Correction of Active Inference's Flaws**. AAT explicitly positions itself as a more structurally rigorous, control-theoretic alternative to the Free Energy Principle.

1. **Rejecting "Preferences as Priors":** Active Inference achieves unification by assuming that an agent encodes its goals as prior beliefs about the world, and that action is just "fulfilling expectations." AAT explicitly rejects this (Topic 13/14), proving that collapsing "wanting" and "expecting" destroys the agent's ability to orthogonally diagnose failure (the Satisfaction vs. Regret split). AAT achieves the same elegant variational unification without committing this epistemological category error.
2. **Rejecting NESS for Sector-Lyapunov Bounds:** FEP relies mathematically on the assumption that a system settles onto a Non-Equilibrium Steady State (NESS) density to define its survival boundaries. AAT notes (echoing critiques by Aguilera et al. 2022) that this assumption is mathematically fragile for non-linear, non-stationary systems. AAT provides **pure mathematical novelty** by replacing the NESS requirement entirely with the classical Lur'e/Zames **Sector Condition** (Topic 10). It proves that universal agency bounds can be derived directly from standard Lyapunov persistence, which is mathematically vastly more robust than FEP's density assumptions.
3. **Separating Agency from Identity:** While Enactivism and FEP tie the *mechanics of tracking* directly to the *drive for biological survival*, AAT formally separates them. By decoupling teleology from the continuity stance (Topic 16), AAT proves that the mechanics of agency apply equally to an indifferent thermostat and a self-preserving AI, creating a framework uniquely suited for modern Artificial Intelligence safety and alignment, domains where biological survival theories struggle to map cleanly.