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
3. **Separating Agency from Identity:** While Enactivism and FEP tie the *mechanics of tracking* directly to the *drive for biological survival*, AAT formally separates them. By decoupling teleology from the continuity stance (per `#disc-continuity-stance`, row 15), AAT proves that the mechanics of agency apply equally to an indifferent thermostat and a self-preserving AI. Per row 13's self-actuation grounding no-go, this orthogonality is *derived*, not merely posited — the terminal grounding invariant must live on the adaptive substrate, where the self-actuation operator structurally cannot reach. This creates a framework uniquely suited for modern AI safety and alignment, domains where biological-survival theories struggle to map cleanly.

**Four-pillar framework-level novelty defense (from `ref/Novelty_defense_and_integration.md`).**

The Undermind defense memo identifies four AAT-distinctive contributions at the framework level, each with its own prior-art landscape:

| Pillar | Verdict | Main prior-art locus | Confidence |
|---|---|---|---|
| **Causal insufficiency and forced exploration** | Conceptual Precursor | Causal bandits / causal MDPs under hidden confounding (Bareinboim, Zhang, Forré, Lee 2018/2020) | High |
| **Composition closure defect and Bridge Lemma** | Conceptual Precursor | Approximate information states, state abstraction, decentralized control (Subramanian, Abel, Taylor, Nayyar, Congeduti) | High |
| **Logogenic bias bound for LLMs** | Wholly Novel | Empirical ambiguity / action-belief gap work + loose bounded-rationality analogies (Wang, Yan, Tan, Pal, Liu, Genewein) | Medium |
| **TST in agentic environments** | Wholly Novel | Developer-agent systems-and-benchmark papers, not formal economic theory (Yan, Pan, Vij, Xia, Gol) | Low |

The framework-level posture is **selective rather than maximalist**: several ASF claims position as sharpened syntheses over strong precursor mathematics; others appear genuinely new. Pillar 4 (TST) has the thinnest precedent search at this snapshot.

**Cross-cutting integration (per the top-level defense).** AAT bridges four signature pillars under one machine: the loop's interventional access (row 06) makes Pearl-Level-2 evidence available; the closure-defect / bridge lemma (row 08) supplies the composition machinery; the logogenic bias bound (rows 05 + 03-llm-core specialization) gives LLM-agent architectures a structural reading; and the TST-in-agentic-environments work extends the framework to developer-agent software economics (`02-tst-core`).

**Convergent meta-finding across the 12 per-topic Undermind memos.** The memos consistently identify AAT's novelty at the **package-integration level** rather than at any single component, **AND** at AAT-native methodological inventions (the GUC class typology, the W₀/W₁/W₂ wrapping hierarchy, the strategy DAG with regime-indexed identification, the closure defect $\varepsilon^\ast$, the Sector-Persistence Template, the constructive-impossibility five-step shape, the four-layer coordinate-forcing pattern, the stability-certificate spine, the Hafez bridge, the Sylvester recognition for rank-collapse floors, the auxilia hierarchy, and the directional-fidelity B1 condition for credit assignment). This is consistent with the math-novelty-recognition discipline (see project CLAUDE.md): AAT is not only Nash-style application of established machinery but also *purposeful invention* of new tools, methodologies, and notation in service of the theory.

**AAT-native methodological inventions at the framework level:**
- The agent spectrum (model × objective richness) with migration across regions (row 20).
- The GUC class typology (1 / 2 / 3 = Separated / Partial / Coupled) (rows 05, 14).
- The Sector-Persistence Template as a one-stop instantiation form (row 03).
- The closure defect $\varepsilon^\ast$ as composition-validity parameter (row 08).
- The stability-certificate spine with three facets (rows 11 / 12 / 18 / `#disc-separability-pattern`).
- The constructive-impossibility five-step pattern (row 11).
- The four-layer coordinate-forcing pattern (row 12).
- The four-instance compression-operations family with U-medium honest scope (row 19).
- The five-stance continuity-stance taxonomy with terminal-non-objective-invariant locus (rows 13, 15).
- The W₀ / W₁ / W₂ wrapping-regime hierarchy with Class-1-by-structure vs Class-1-by-behavior distinction (row 05).
- The directional-fidelity B1 condition + observability-by-design discipline (row 17).
- The four-regime recipient-side classification (row 10).
- The Hafez-bridge architecture-vs-performance distinction (row 20).

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **Some at the synthesis level**, with the constituent theorems living in their per-row segments (the row-21 contribution is framework-coherence, not theorem-derivation).
- *Arch Novelty:* **High.** The framework-level integration is itself architectural — placing AAT as a structurally-rigorous alternative to FEP + AIXI + bounded-rationality lineages, with explicit corrections to "preferences as priors" + NESS density assumptions.
- *Synth Novelty:* **High.** The four-pillar synthesis (causal insufficiency + closure defect + logogenic bias + TST) under one framework with consistent vocabulary across the agent spectrum.
- *Appl Novelty:* **None at this row's lead** (the four pillars have their own applied-novelty content).
- *Impact:* **High.** Per the meta-summary's Part 2 — AAT positions as a credible Grand Unification attempt with the distinctive epistemic-honesty discipline (no-gos as load-bearing apparatus) that FEP and AIXI lack. The reception will depend on how cleanly the framework's adoption-vs-extension distinction is communicated — the strongest defensive posture, per Gemini's anecdotal opinion in the meta-summary, is **radical transparency about priors** combined with the **architectural synthesis** framing.