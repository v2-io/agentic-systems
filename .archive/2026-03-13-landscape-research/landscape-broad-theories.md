# Landscape: Broad Unified Agency Frameworks (25 frameworks identified)

**Date**: 2026-03-13
**Source**: Research agent output from comparative theory analysis session
**Context**: Part of a deep analysis comparing ACT against Hafez et al. (2026) "A Mathematical Theory of Agency and Intelligence" and the broader landscape of unified agency frameworks.

---

Now I have a comprehensive picture. Let me compile the full landscape report.

---

# Comprehensive Landscape: Unified Theoretical Frameworks for Agency, Adaptation, and Intelligence

## TIER 1: HIGHEST RELEVANCE -- Broad integrative ambition with mathematical rigor

### 1. Categorical Cybernetics (Capucci, Hedges, Gavranovic, Rischel)

**What it is:** A categorical framework for processes that interact bidirectionally with both an environment and a "controller." Coined by Jules Hedges around 2019 and formalized in "Towards Foundations of Categorical Cybernetics" (ACT 2021). The CyberCat Institute was incorporated as a nonprofit in 2024 to support this research.

**Mathematical formalism:** Parametrised optics (a generalization of lenses) in category theory. Agents are modeled as parametrised bidirectional processes. Selection relations abstract agent "goals" or "personality." Composition is achieved via categorical composition (sequential) and monoidal products (parallel).

**Domain coverage:**
- Control theory: Yes -- bidirectional controller-environment interaction is the core abstraction
- Reinforcement learning: Yes -- Hedges & Rodriguez Sakamoto (2024, updated 2025) showed major RL algorithms (dynamic programming, Monte Carlo, TD learning, deep RL) all fit as "different extremal cases" of parametrised optics
- Multi-agent/game theory: Yes -- compositional game theory (open games) is a direct ancestor; extensive-form games translated to open games with agency
- Dynamics: Yes -- optics model bidirectional dynamical flows
- Goals/intent: Yes -- selection relations formalize agent objectives

**Gaps:** Does not directly address biological adaptation, organizational theory, or adversarial dynamics as first-class concerns. Multi-agent composition is inherited from open games but not deeply developed for large-scale systems.

**Key papers:**
- [Towards Foundations of Categorical Cybernetics](https://arxiv.org/abs/2105.06332)
- [Reinforcement Learning in Categorical Cybernetics](https://arxiv.org/abs/2404.02688)
- [CyberCat Institute](https://cybercat.institute/)

---

### 2. Structured Active Inference (Toby St Clere Smithe)

**What it is:** A large generalization of active inference using categorical systems theory. Smithe's PhD thesis from Oxford (2023) laid the mathematical foundations, and the 2024 extended abstract formalized agents as controllers dual to their generative models, with compositional interfaces replacing Markov blankets.

**Mathematical formalism:** Bayesian lenses, statistical games (fibrations thereof), categorical systems theory. Generative models are systems "on an interface" -- a compositional abstraction of Markov blankets. Goals are expressed as formal predicates via categorical logic. The chain rule of relative entropy is a strict section; free energy gives lax sections.

**Domain coverage:**
- Control theory: Yes -- agents as controllers, formally dual to generative models
- Reinforcement learning: Yes -- subsumes POMDP-based active inference
- Multi-agent composition: Yes -- "agents that can manage other agents," "self-organizing ensembles of agents," meta-agents
- Dynamics: Yes -- mode-dependent structured interfaces, interaction with APIs
- Goals/intent: Yes -- goals as formal predicates with context-dependent satisfaction
- Biological adaptation: Partial -- inherits from active inference/Bayesian brain
- Formal verification: Yes -- structured policies amenable to verification

**Gaps:** Still largely theoretical; limited empirical validation. Adversarial dynamics not explicitly treated. Organizational theory not addressed.

**Key papers:**
- [Mathematical Foundations for a Compositional Account of the Bayesian Brain](https://arxiv.org/abs/2212.12538) (PhD thesis)
- [Structured Active Inference (Extended Abstract)](https://arxiv.org/abs/2406.07577)
- [Shared Protentions in Multi-Agent Active Inference](https://www.mdpi.com/1099-4300/26/4/303) (with Albarracin, Pitliya -- uses polynomial morphisms and topoi for gluing agents' internal universes)

---

### 3. Compositional Game Theory / Open Games (Ghani, Hedges, Winschel, Zahn)

**What it is:** A category-theoretic foundation for economic game theory where games are morphisms of a symmetric monoidal category. Open games represent games played relative to an arbitrary environment, introducing "coutility" as utility returned to the environment.

**Mathematical formalism:** Symmetric monoidal categories, string diagrams, lenses. Games compose via categorical composition (sequential moves) and monoidal products (simultaneous moves). Extended to Bayesian open games handling stochastic environments and incomplete information.

**Domain coverage:**
- Game theory: Yes -- this is its core domain
- Multi-agent composition: Yes -- compositional by design; large-scale economic models
- Goals/intent: Yes -- utility functions as first-class objects
- Dynamics: Partial -- sequential games capture temporal structure
- Control theory / RL: Connected via categorical cybernetics

**Gaps:** Not designed for biological adaptation, organizational theory, or continuous dynamical systems. Agency is modeled through utility maximization only.

**Key papers:**
- [Compositional Game Theory](https://arxiv.org/abs/1603.04641)
- [Bayesian Open Games](https://arxiv.org/abs/1910.03656)

---

### 4. Polynomial Functors as a Theory of Interaction (Spivak, Niu)

**What it is:** David Spivak's monograph and course at the Topos Institute present polynomial functors as a "general theory of interaction." Positions represent states, directions represent observations/actions. Morphisms send positions forward and directions backward, modeling two-way communication.

**Mathematical formalism:** The category of polynomial endofunctors on Set, with dependent lenses as morphisms. Composition models sequential interaction; tensor products model parallel interaction. Used to model dynamical systems, decision processes, databases, and agent interaction protocols.

**Domain coverage:**
- Dynamical systems: Yes -- core application
- Agent interaction: Yes -- explicitly models interactive behavior
- Composition: Yes -- categorically compositional by construction
- Multi-agent: Yes -- interaction protocols between multiple agents
- Goals/intent: Not explicitly first-class

**Gaps:** Abstract mathematical framework; does not specifically address agency, goals, adaptation, or biological systems. Serves more as mathematical infrastructure than a theory of agency per se.

**Key paper:**
- [Polynomial Functors: A Mathematical Theory of Interaction](https://arxiv.org/abs/2312.00990)

---

### 5. Active Inference / Free Energy Principle (Friston et al.)

**What it is:** The most ambitious existing framework. Claims that all biological agents minimize variational free energy (a bound on surprise). Extended to "Bayesian mechanics" -- a physics of and by beliefs. Recently extended with renormalization group methods for multi-scale compositionality.

**Mathematical formalism:** Variational Bayesian inference, Markov blankets, POMDPs, path integrals, Langevin dynamics, variational free energy, expected free energy. Recent extensions: Bayesian mechanics for stationary processes, renormalizing generative models (RGM) using the renormalization group.

**Domain coverage:**
- Biological adaptation: Yes -- this is the home domain
- Control theory: Yes -- active inference subsumes optimal control
- Reinforcement learning: Yes -- formally shown to subsume RL, Bayesian decision theory
- Dynamics: Yes -- path integral formulation, Langevin dynamics
- Goals/intent: Yes -- prior preferences as "goals"
- Multi-agent: Partial and developing -- see below
- Organizational: Partial -- applied to team formation, industrial engineering

**Multi-agent status (critical assessment):**
- "Free-Energy Equilibria" (Hyland et al., ICML 2024 Workshop) extends expected free energy to strategic multi-agent contexts, merging Nash equilibria with bounded rationality
- "Factorised Active Inference for Strategic Multi-Agent Interactions" (Ruiz-Serra et al., AAMAS 2025) introduces factorized generative models where agents maintain beliefs about other agents' internal states
- Fields & Glazebrook (2024) frame physical interactions as games using FEP
- BUT: a general theory of multi-agent interactions under FEP is acknowledged as lacking
- Adversarial dynamics require augmentation (Distributionally Robust Free Energy, Nature Communications 2025)

**Multi-scale compositionality:**
- "From Pixels to Planning: Scale-Free Active Inference" (Friston et al., 2024/2025) uses renormalization group for hierarchical generative models with compositionality over space and time
- This is the most mathematically developed multi-scale story in any framework

**Gaps:** Multi-agent theory remains underdeveloped. Software engineering and organizational theory are addressed only superficially. The framework has been criticized for being too broad (everything minimizes free energy, making it potentially unfalsifiable). Adversarial settings require separate extensions.

**Key papers:**
- [Path integrals, particular kinds, and strange things](https://www.sciencedirect.com/science/article/pii/S1571064523001094) (Friston et al., Physics of Life Reviews, 2023)
- [Probabilistic Principles for Biophysics and Neuroscience](https://arxiv.org/abs/2410.11735) (2024)
- [From Pixels to Planning: Scale-Free Active Inference](https://arxiv.org/abs/2407.20292) (2024/2025)
- [Factorised Active Inference for Strategic Multi-Agent Interactions](https://arxiv.org/abs/2411.07362) (AAMAS 2025)
- [Distributionally Robust Free Energy](https://www.nature.com/articles/s41467-025-67348-6) (Nature Communications, 2025)
- [Active Inference & Behavior Engineering for Teams](https://researchgate.net/publication/344190964_Active_Inference_Behavior_Engineering_for_Teams)
- [Distributed Science as Multi-Scale Active Inference](https://www.researchgate.net/publication/374782654_Distributed_Science_-_The_Scientific_Process_as_Multi-Scale_Active_Inference)

---

## TIER 2: SIGNIFICANT PARTIAL MATCHES -- Strong formalism, narrower scope or less integrative

### 6. AIXI / Universal Artificial Intelligence (Hutter, Legg)

**Mathematical formalism:** Solomonoff induction + sequential decision theory. Defines universal intelligence as reward maximization over all computable environments, weighted by Kolmogorov complexity.

**Strengths:** Maximally rigorous mathematical definition of intelligence. Top-down approach deriving agent properties from theorems. Formally defines optimal behavior for any computable environment.

**Gaps:** Incomputable (theoretical only). Single-agent only. No multi-agent composition. No biological grounding. No organizational theory. No dynamics beyond sequential decisions. Goals are reward functions only. No adaptation -- the agent is already defined as optimal.

**Key reference:** [Universal Artificial Intelligence](https://hutter1.net/ai/suaibook.pdf) (Hutter, 2005); [Universal Intelligence: A Definition of Machine Intelligence](https://arxiv.org/abs/0712.3329) (Legg & Hutter)

---

### 7. Causal Game Theory (Everitt, Halpern, Koller et al.)

**Mathematical formalism:** Causal Bayesian networks extended with decision and utility nodes. Multi-Agent Influence Diagrams (MAIDs). Do-calculus for interventional reasoning. Recent work on Sequential Causal Normal Form Games.

**Domain coverage:** Multi-agent: Yes. Goals: Yes (utility nodes). Composition: Developing -- modular causal RL. Dynamics: Sequential. Adversarial: Yes via game-theoretic equilibria.

**Gaps:** No biological adaptation. No organizational theory. Limited dynamics. Primarily a decision-theoretic rather than dynamical framework.

**Key papers:**
- [Graphical Models for Decision-Making](https://arxiv.org/pdf/2504.13210) (2025 survey)
- [Causal Incentives Working Group](http://causalincentives.com/)

---

### 8. John Baez's Categorical Agent-Based Models

**What it is:** Uses category theory (double categories, decorated cospans) to compose agent-based models. Major project at ICMS in 2024 with Osgood, Patterson, Brown et al. aimed at creating category-based software for ABMs.

**Mathematical formalism:** Double categories of "open systems" using the variable-sharing paradigm. Stochastic C-set rewriting systems.

**Domain coverage:** Composition: Yes. Multi-agent: Yes (ABMs). Dynamics: Yes (stochastic). Goals/agency: Not directly formalized.

**Gaps:** Focused on epidemiological ABMs; does not address agency, goals, intelligence, or adaptation at a theoretical level.

**Key references:**
- [Applied Category Theory for Modeling](https://math.ucr.edu/home/baez/ACT_for_modeling.pdf)
- [Agent-Based Models blog series](https://johncarlosbaez.wordpress.com/2023/07/06/agent-based-models-part-1/) (2023-2024)

---

### 9. Guaranteed Safe AI Framework (Dalrymple, Bengio, Russell et al.)

**Mathematical formalism:** World models (mathematical descriptions of AI-environment effects) + safety specifications + verifiers producing proof certificates. Draws on formal verification and automated theorem proving.

**Domain coverage:** Agent safety: Yes. Formal verification: Yes. Composition: Not explicitly. Multi-agent: Not directly. Goals: Safety specifications as constraints.

**Gaps:** Framework for safety assurance, not a theory of agency. No dynamics, adaptation, or biological grounding.

**Key paper:** [Towards Guaranteed Safe AI](https://arxiv.org/abs/2405.06624) (2024)

---

### 10. Maximum Entropy / Information-Theoretic Bounded Rationality

**Mathematical formalism:** KL-divergence as information acquisition cost, maximum entropy inference, rate-distortion theory. Active inference shown to subsume these when expressed variationally. Recent work (December 2025) consolidates formal correspondences between expected free energy minimization and classical frameworks.

**Domain coverage:** Decision theory: Yes. Bounded rationality: Yes. Agent behavior: Yes. Multi-agent: Limited. Composition: No.

**Key papers:**
- [A Maximum Entropy Model of Bounded Rational Decision-Making](https://arxiv.org/abs/2102.09180)
- [Bounded Rationality, Abstraction, and Hierarchical Decision-Making](https://www.frontiersin.org/articles/10.3389/frobt.2015.00027/full)
- [Decision, Inference, and Information: Formal Equivalences Under Active Inference](https://www.mdpi.com/1099-4300/28/1/1) (Dec 2025)

---

### 11. Evolutionary Connectionism (Richard Watson)

**Mathematical formalism:** Shows that natural selection adjusting relationships between components is mathematically isomorphic to Hebbian learning in neural networks. Associative learning in spring systems is mathematically isomorphic to weight changes in connectionist models. Provides a formal bridge between evolution and learning.

**Domain coverage:** Biological adaptation: Yes. Multi-scale: Yes (evolutionary transitions, development, ecology). Learning: Yes (formal equivalence). Agency: Implicit (collective intelligence).

**Gaps:** Not framed as a theory of agency per se. No multi-agent game theory. No control theory. No organizational theory explicitly.

**Key papers:**
- [Evolutionary Connectionism](https://pubmed.ncbi.nlm.nih.gov/27932852/) (2016)
- [The Collective Intelligence of Evolution and Development](https://journals.sagepub.com/doi/10.1177/26339137231168355) (Watson & Levin, 2023)

---

### 12. Michael Levin's Multi-Scale Collective Intelligence

**What it is:** Frames morphogenesis, regeneration, and development as behavioral outcomes of problem-solving across multiple scales. Cells and tissues are agential materials navigating "morphospace."

**Mathematical formalism:** Bioelectric networks as computational media. Formal treatment of goal-directedness in biological systems (William James' definition). Limited explicit mathematical formalism -- more conceptual/experimental than mathematical.

**Domain coverage:** Biological adaptation: Yes (core). Multi-scale: Yes (molecular > cellular > tissue > organism). Agency: Yes -- basal cognition framework. Goals: Yes -- target morphology as attractors.

**Gaps:** Limited formal mathematical treatment. No multi-agent game theory. No organizational or software engineering applications. More a research program than a mathematical theory.

**Key references:**
- [The Multiscale Wisdom of the Body](https://onlinelibrary.wiley.com/doi/10.1002/bies.202400196) (2025)
- [The Collective Intelligence of Evolution and Development](https://journals.sagepub.com/doi/10.1177/26339137231168355) (with Watson, 2023)

---

## TIER 3: NOTABLE PARTIAL MATCHES AND EMERGING WORK

### 13. "Agentic AI Needs a Systems Theory" (Miehling et al., IBM Research, 2025)

A position paper arguing agentic AI requires systems-theoretic perspective to understand emergent capabilities and risks from agent-agent and agent-environment interactions. Identifies the problem space but proposes limited new mathematical formalism.

**Paper:** [arXiv:2503.00237](https://arxiv.org/abs/2503.00237)

---

### 14. "Good Regulator Theorem" for Embodied Agents (Virgo, Biehl, Baltieri, Capucci, 2025)

Extends Conant-Ashby with observer-dependent interpretation of belief updating. More broadly applicable than the original theorem. Connects to categorical cybernetics researchers.

**Paper:** [arXiv:2508.06326](https://arxiv.org/abs/2508.06326)

---

### 15. Dynamical Systems Framework for RL (FTLE/LCS approach, 2025)

Treats RL agent + environment as a discrete-time autonomous dynamical system. Uses Finite-Time Lyapunov Exponents to identify Lagrangian Coherent Structures as the "skeleton" governing behavior. Introduces "Aggregated Spurious Attractor Strength" to quantify goal focus.

**Paper:** [arXiv:2508.15588](https://arxiv.org/pdf/2508.15588) (2025)

---

### 16. A Geometric Theory of Cognition (Laha Ale, 2025)

Represents cognitive states on differentiable manifolds with learned Riemannian metrics. Cognition unfolds as gradient flow of a "cognitive potential" combining predictive accuracy, parsimony, task utility, and normative constraints. Single-agent; no multi-agent or composition.

**Paper:** [arXiv:2512.12225](https://arxiv.org/abs/2512.12225)

---

### 17. Geometries of Cognition: Information-Geometric Framework for Self-Evolving AI Agents (2026)

Uses Fisher information geometry, geodesic flows on statistical manifolds, and natural gradient for hierarchical self-modification. Covers dynamic memory, architectural sparsity, geometric robustness, adversarial resilience.

**Reference:** [Academia.edu](https://www.academia.edu/164799727/Geometries_of_Cognition_A_Unified_Information_Geometric_Framework_for_Self_Evolving_Artificial_Intelligence_Agents)

---

### 18. "Towards a Science of Scaling Agent Systems" (Google, 2024)

Empirical rather than theoretical. Derives quantitative scaling principles for multi-agent AI systems from 180 configurations. Identifies tool-coordination trade-offs, capability saturation, error amplification. Predictive model achieves R^2=0.524.

**Paper:** [arXiv:2512.08296](https://arxiv.org/abs/2512.08296)

---

### 19. Joscha Bach's MicroPsi / Psi Theory

Cognitive architecture integrating motivation, emotion, and cognition as interdependent processes. Three drive types (physiological, social, cognitive) influence goal formation. Formalized implementation of Dorner's Psi theory.

**Gaps:** Architecture, not a general mathematical theory. No multi-agent composition. No biological adaptation formalism.

---

### 20. Coalgebraic Methods for Behavioral Systems

Coalgebras as the "mathematics of computational dynamics." Models state-based systems (automata, transition systems, process calculi). Composition via distributive laws. Active research through CALCO 2025.

**Relevance:** Provides mathematical infrastructure for agent dynamics and composition but does not address agency, goals, or adaptation directly.

---

### 21. Constructor Theory (Deutsch, Marletto)

Expresses physics in terms of possible vs. impossible tasks. Composition principle: every regular network of possible tasks is a possible task. Information theory derived from physics. Recent work on constructor theory of time (May 2025).

**Relevance:** Highly abstract. Could potentially ground a theory of agency (what transformations an agent can/cannot perform). But does not currently address agency, adaptation, or multi-agent systems.

---

### 22. Viable System Model (Stafford Beer, modern extensions)

Classic cybernetic model for organizational viability based on Ashby's Law of Requisite Variety. Five systems (operations, coordination, optimization, intelligence, policy). Being applied to agentic AI and decentralized autonomous organizations.

**Mathematical formalism:** Rooted in cybernetics but primarily architectural/organizational rather than rigorously mathematical in modern terms. Being translated into software patterns.

---

### 23. Roman Leventov's Active Inference Agency Ontology

Distinguishes active inference as intelligence architecture vs. theory of agency. Defines agency as observer-dependent: an observer predicts an agent's trajectory by assuming it has its own generative model. Predicts that language models trained via self-supervised learning will exhibit self-evidencing behavior.

**References:**
- [The Two Conceptions of Active Inference](https://leventov.medium.com/the-two-conceptions-of-active-inference-an-intelligence-architecture-and-a-theory-of-agency-e97a6a40f5e5)
- [Refinement of Active Inference Agency Ontology](https://www.alignmentforum.org/posts/6E4L96H2PbJbfKBYS/refinement-of-active-inference-agency-ontology)

---

### 24. Computational Mechanics / Epsilon Machines (Crutchfield, Shalizi)

Defines causal states and epsilon-machines as minimal maximally predictive models of stochastic processes. Measures statistical complexity as information needed to specify the machine state. Connects to ergodic and information theories.

**Relevance:** Powerful formalism for pattern and prediction in complex systems, but does not address agency, goals, or adaptation directly. Infrastructure-level rather than a theory of agency.

---

### 25. Pearl's Causal Hierarchy and Interventionist Framework

Three-layer hierarchy: seeing (observation), doing (intervention), imagining (counterfactuals). Do-calculus for reasoning about interventions. Agency enters through the interventionist layer.

**Relevance:** Provides the causal reasoning infrastructure that any rigorous agency theory needs, but is not itself a theory of agency, adaptation, or multi-agent dynamics.

---

## SUMMARY ASSESSMENT

**What exists that attempts comparable integrative breadth with mathematical rigor:**

| Framework | Math Rigor | Multi-Domain | Dynamics | Goals | Multi-Agent | Composition |
|-----------|-----------|-------------|----------|-------|-------------|-------------|
| Categorical Cybernetics | High | Medium | Yes | Yes | Yes (via open games) | Yes |
| Structured Active Inference (Smithe) | High | High | Yes | Yes | Yes | Yes |
| Active Inference / FEP (Friston) | High | High | Yes | Yes | Developing | Developing |
| Compositional Game Theory | High | Low | Partial | Yes | Yes | Yes |
| Polynomial Functors (Spivak) | High | Medium | Yes | No | Yes | Yes |
| AIXI (Hutter) | High | Low | Partial | Yes | No | No |
| Evolutionary Connectionism (Watson) | Medium | Medium | Yes | Implicit | Implicit | Implicit |
| Levin Collective Intelligence | Low-Med | Medium | Yes | Yes | Implicit | Implicit |

**The closest existing work to a truly unified mathematical theory spanning control theory, RL, multi-agent systems, organizational theory, biological adaptation, and AI agent design appears to be the convergence of three research programs:**

1. **Smithe's Structured Active Inference** -- the most ambitious single attempt, using categorical systems theory to give active inference compositional multi-agent structure with formal goals
2. **Categorical Cybernetics** (CyberCat Institute) -- providing the mathematical backbone connecting control, RL, and game theory through parametrised optics
3. **Friston's Active Inference / Bayesian Mechanics** -- the broadest empirical scope (biology, neuroscience, physics), now developing multi-scale compositionality via renormalization and multi-agent via factorised models

These three are converging: Smithe explicitly bridges Friston's active inference with categorical cybernetics. The major gap across all existing work remains: no framework yet provides a single mathematical treatment that rigorously covers adversarial multi-agent dynamics, organizational hierarchy, software engineering concerns, AND biological adaptation under one umbrella. The landscape is active and fragmented, with the categorical and information-geometric approaches offering the most promising paths toward unification.