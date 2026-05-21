# Prior-Art Analysis: Directed Separation and Architectural Coupling

**Target Claim:**
Agent architectures can be formally categorized by "Directed Separation"—the degree to which their epistemic updating (beliefs, state estimation) is causally independent from their teleological processing (goals, action selection). Class 1 (Separated) architectures process events goal-blindly (e.g., Kalman + LQR). Class 3 (Coupled) architectures entangle goals with observation processing (e.g., Active Inference, LLMs). Furthermore, Class 3 systems can be coerced into Class 1 by enclosing them in an external scaffold that strictly segregates belief-queries from goal-queries, achieving modularity at the cost of execution tempo/speed (a cognitive analog to Brooks's Law).

---

## 1. State of the Field & Scientific Precedence

The Undermind search reveals a profound and explicit scientific precedence for AAT's structural dichotomy between separated and entangled architectures. This taxonomy maps cleanly onto the historical fault line between classical stochastic control (separated) and modern enactive/variational frameworks (coupled).

### Pillar 1: Class 1 Separated Architectures (The Separation Principle)
The mathematical bedrock for AAT's "Class 1" architecture is the **Separation Principle of Stochastic Control**, dating back to Wonham (1968) and Witsenhausen (1971). The Separation Theorem formally proves that for Linear-Quadratic-Gaussian (LQG) systems, optimal control can be factorized into two strictly independent modules: a state estimator (Kalman filter) that is completely blind to the control policy, and a deterministic controller (LQR) that acts on the estimator's output. In AI, this birthed the "sense-model-plan-act" pipeline, where belief updating is structurally separated from goal pursuit.

### Pillar 2: Class 3 Coupled Architectures (Dual Effect & Active Inference)
The concept that goals and observation processing become fundamentally entangled—AAT's "Class 3"—has two major precedents. 
1. **Dual Effect in Control Theory:** Bar-Shalom and Tse (1974) introduced the concept of the "dual effect," describing scenarios where an agent's control actions not only affect the system state but also alter the *quality of future information/observations*. When the dual effect is present, the separation principle breaks down, and estimation and control become intrinsically coupled.
2. **Active Inference:** Friston (2010, 2012) and the Active Inference community provide the modern formalization of entangled perception. In active inference, both action selection and belief updating are driven by the exact same objective: minimizing variational free energy. Crucially, goals (rewards) are absorbed into the agent's prior beliefs about its preferred states. Perception is no longer goal-blind; it is inherently biased by what the agent wants to achieve.

Baltieri and Buckley (2018, 2020) explicitly map this terrain, noting that the modularity of the "classical sandwich" of cognitive science perfectly mirrors the control-theoretic separation principle, whereas Active Inference provides a mathematically rigorous nonmodular (coupled) alternative. 

### Pillar 3: Blankets and Metaphysics (Friston vs. Pearl Blankets)
A critical conceptual anchor for AAT's architectural framing is provided by Bruineberg et al. (2021) in *"The Emperor’s New Markov Blankets"*. They distinguish between **Pearl blankets** (used instrumentally as an epistemic tool for conditional independence in Bayesian networks) and **Friston blankets** (used metaphysically to define the causal boundary of an agent). This maps tightly to AAT's focus on whether "perception-action coupling" is just an epistemic reality or a structural/architectural mandate.

### Pillar 4: Class Coercion and Scaffolding
The prior art for "Class Coercion"—wrapping an entangled system in a separated scaffold—is less mathematically unified but highly visible in applied AI and robotics. The literature on Hybrid Deliberative/Reactive architectures (e.g., Gat 1997, Arkin & MacKenzie 1994) involves orchestrating reactive (entangled) layers beneath deliberative (separated) planners. In modern AI, the rapid rise of "LLM Scaffolding" perfectly mirrors AAT's claim: taking an end-to-end coupled transformer and forcing it into a modular pipeline via prompt orchestration. The literature widely acknowledges that this modularization imposes severe **tempo costs**, introducing latency, serial bottlenecks, and query overhead (Malikopoulos 2021).

---

## 2. Key Anchor Papers Identified

1. **Baltieri, M., & Buckley, C. (2018). The modularity of action and perception revisited using control theory and active inference.**
   *Significance:* Explicitly draws the connection between cognitive modularity and the control-theoretic Separation Principle, contrasting it with the nonmodular structure of active inference.
2. **Bar-Shalom, Y., & Tse, E. (1974). Dual effect, certainty equivalence, and separation in stochastic control.**
   *Significance:* Formalizes when separation breaks down due to control actions affecting state uncertainty (the "dual effect"), forcing estimation and control to couple.
3. **Bruineberg, J., et al. (2021). The Emperor’s New Markov Blankets.**
   *Significance:* Provides the exact philosophical framing for distinguishing epistemic boundaries (Pearl) from architectural/metaphysical boundaries (Friston) in perception-action loops.
4. **Witsenhausen, H. (1971). Separation of estimation and control for discrete time systems.**
   *Significance:* A foundational text establishing the mathematical conditions under which belief-updating and action-selection can be structurally decoupled.

---

## 3. Conclusion on Novelty & Overlap

AAT's "Directed Separation" taxonomy is highly grounded, serving as a unifying nomenclature for a dichotomy that has existed in disparate fields for 50 years. 

**What is Novel:** 
While control theorists know about the Separation Principle, and cognitive scientists know about Active Inference, AAT's novelty lies in formalizing this as an *architectural class continuum* (Class 1 to Class 3) and introducing the formal dynamics of **Class Coercion**. Framing the orchestration of modern AI models (like LLMs) as coercing a Class 3 component into a Class 1 composite—and formally deriving the resulting tempo/bandwidth penalty as a cognitive analog to Brooks's Law—is a highly novel synthesis of control theory, systems architecture, and modern AI engineering.