# Prior-Art Analysis: Composite Agency, Closure Defect, and Symbiogenesis

**Target Claim:**
AAT defines composite (macro) agents via commutativity of coarse-graining: a group is a macro-agent if its coarse-grained macro-dynamics commute with the micro-dynamics of its sub-agents. The mismatch in this commutativity is the "closure defect" ($\varepsilon^*$). Using this framework, AAT formally derives *Brooks's Law*: adding sub-agents to a composite increases its gross tempo, but it also increases the internal closure defect. If the tempo consumed by internal coordination overhead (driven by the closure defect) exceeds the tempo contributed by the new agent, the macro-agent's net performance decreases. Finally, AAT distinguishes "peer coupling" from "Symbiogenesis," defining the latter as an asymmetric transition where a host absorbs an endosymbiont's objective ($O_e \to O_h$) and reduces its autonomy, crossing the composition scope boundary to form a single entity.

---

## 1. State of the Field & Scientific Precedence

The Undermind search reveals deep roots in systems theory, control theory, and evolutionary biology. AAT's approach to composite agency stands on three well-established mathematical and empirical pillars:

### Pillar 1: Composition via Commutativity and Lumpability
The definition of macro-states via the commutativity of dynamics and coarse-graining (projection) is a foundational concept in Markov processes and control theory.
- **Simon (1961)** pioneered "aggregation of variables," defining conditions under which a high-dimensional dynamic system can be faithfully represented by a lower-dimensional one. 
- **Pappas and Simic (2002)** and **Tabuada et al. (2001, 2005)** introduced "consistent abstractions" and "bisimulation" for control systems. They mathematically proved that a macro-system is a valid abstraction if there exists a surjective map (a coarse-graining) that preserves reachability and properties between the micro and macro levels. AAT's "closure defect" $\varepsilon^*$ is structurally identical to the "simulation functions" (e.g., Rungger and Zamani, 2015; Girard and Pappas, 2011) used to bound the error between a concrete interconnected system and its abstraction.
- **Buchholz (1994)** and **Tian and Kannan (2006)** cover "lumpability" in Markov chains, mathematically bounding when micro-states can be grouped into macro-states while retaining Markovian dynamics.

### Pillar 2: Coordination Overhead (Brooks's Law)
The concept that coordination overhead limits multi-agent capacity is well known in operations research and computer science.
- **Janow (2009)** provides a first-principles mathematical model of "Collaborative Entropy Costs," quantitatively predicting productivity variations in organizations. He uses a Shannon-like entropy to model the decision information that must be generated to coordinate actors, proving a fundamental limit on per-capita productivity.
- **Gurvich and Van Mieghem (2015)** formalize capacity limits in multitasking networks, proving that "collaboration and multitasking introduce synchronization requirements that may inflict unavoidable idleness of the bottleneck resources."

### Pillar 3: Symbiogenesis and Evolutionary Transitions
Symbiogenesis is a canonical concept in evolutionary biology.
- **Szathmáry (2015)** outlines the "major evolutionary transitions," specifically highlighting egalitarian transitions (where formerly independent units merge).
- **Frean and Abraham (2003)** provide a dynamical systems model of endosymbiosis, showing how a rapidly adapting species becomes highly cooperative and is effectively "enslaved" by a slowly evolving host.
- **Radzvilavicius and Blackstone (2015)** model the conflict and cooperation inherent in eukaryogenesis (mitochondrial absorption), detailing the reduction of symbiont autonomy required for the higher-level unit to stabilize.

---

## 2. Key Anchor Papers (Available in `/ref`)

1. **Pappas, G. J., & Simic, S. (2002). Consistent abstractions of affine control systems.** (`ref/pappas_consistent_abstractions_2002.pdf`)
   *Significance:* Provides the formal control-theoretic proof of defining macro-level systems via surjective projection maps, exactly mirroring AAT's commutativity requirement for composite agents.
2. **Girard, A., & Pappas, G. J. (2011). Approximate Bisimulation: A Bridge Between Computer Science and Control Theory.**
   *Significance:* Introduces simulation functions to bound the error (equivalent to AAT's $\varepsilon^*$ closure defect) between a micro-system and its macro-abstraction.
3. **Janow, R. (2009). A Fundamental Limit on Productivity in Organizations: Collaborative Entropy Costs.**
   *Significance:* A mathematical derivation showing that coordination overhead (collaborative entropy) acts as a strict cap on the capacity of multi-agent groups, acting as a precursor to AAT's Brooks's Law derivation.
4. **Frean, M., & Abraham, E. R. (2003). Adaptation and enslavement in endosymbiont-host associations.**
   *Significance:* Models the asymmetrical absorption of autonomy in biological symbiogenesis, validating AAT's formal framing of the process.

---

## 3. Conclusion on Novelty & Overlap

The core mechanisms—defining abstractions via commutativity, bounding error via simulation functions, modeling coordination overhead, and recognizing biological symbiogenesis—are all highly established in their respective fields (Control Theory, OR, and Evolutionary Biology).

**AAT's Novel Contribution:**
AAT exhibits strong **synthetic and architectural novelty**, and specific **pure mathematical novelty** in its derivation of the Composite Tempo Inequality.

1. **Pure Mathematical Novelty (Brooks's Law):** While Janow (2009) uses Shannon entropy to bound organizational productivity, AAT derives Brooks's Law entirely within its own cybernetic physics. AAT mathematically connects the spatial "closure defect" ($\varepsilon^*$) of the macro-projection directly to a temporal "coordination overhead penalty" ($C_{\text{coord}}$) using its persistence bounds. By formulating the equation $\mathcal T_c = \sum \mathcal T_i - C_{\text{coord}}$, AAT provides a novel, closed-loop cybernetic proof of Brooks's law based on the *tempo consumed by internal mismatch correction*.
2. **Architectural Novelty (Symbiogenesis):** While biology models symbiogenesis empirically, AAT extracts the mechanism (objective absorption $O_e \to O_h$ and autonomy reduction) and formalizes it as a generalized system-theoretic transition. AAT proves that Symbiogenesis is the specific dynamic pathway by which a multi-agent system crosses the mathematical scope boundary (creating a shared IB relevance variable) to become a single composite agent.