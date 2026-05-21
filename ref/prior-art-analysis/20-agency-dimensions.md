# Prior-Art Analysis: Agency Dimensions and Social Threshold

**Target Claim:**
AAT explicitly defines the dimensions of coherence ("Unity") between agents along two distinct axes: **Content Unity** (what is shared: Epistemic $U_M$, Teleological $U_O$, Strategic $U_\Sigma$, Perceptual $U_{obs}$) and **Structural Unity** (how similarly they update, $U_f$). AAT proves that Unity does not directly guarantee low closure defect; rather, it parametrizes a rate-distortion surface (higher unity permits more aggressive compression/coarse-graining). 

Furthermore, AAT defines the "Social Threshold" structurally. It maps the emergence of agency onto the capacity of a system's internal model. Drawing on the finding that 1-state Moore machines cannot sustain social cooperation while 2-state machines can, AAT formally identifies the 2-state machine as the minimal threshold for "Adaptive Tracking" (the onset of agency), marking the structural boundary where social composition becomes mathematically possible.

---

## 1. State of the Field & Scientific Precedence

The Undermind search yields a highly specific and rigorous sub-field that bridges evolutionary game theory, complex systems, and information theory. The literature on defining the structural minimums for social agency and the informational boundaries of individuals is well established.

### Pillar 1: Finite Automata and the Origins of Social Behavior
The use of finite state automata (Moore and Mealy machines) to establish the minimum cognitive bounds for social behavior is canonical in game theory.
- **Rubinstein (1986)** and **Abreu & Rubinstein (1988)** pioneered the study of bounded rationality by forcing agents in repeated games to be implemented by finite automata, proving that complexity costs strictly limit the types of equilibria (cooperation) that can emerge.
- **Miller (1996, 2022)** in *Ex Machina: Coevolving Machines and the Origins of the Social Universe* provides the direct empirical anchor for AAT's claim. Miller demonstrated via co-evolutionary simulation that 1-state Moore machines are permanently locked in an asocial morass (always defecting). The evolutionary jump to a 2-state machine provides the exact minimum memory required to condition behavior on past interaction (e.g., Tit-For-Tat), triggering the emergence of the "social universe." AAT directly maps its definition of the minimal agent to Miller's 2-state threshold.

### Pillar 2: The Information Theory of Individuality and Agency
Defining the boundaries of an agent (or a composite group of agents) using information theory is a rapidly maturing field.
- **Krakauer, Bertschinger, Olbrich, Flack, and Ay (2014)** in *The Information Theory of Individuality* define individuals as aggregates that "propagate information from their past into their futures." They use information theory to detect adaptive aggregations that do not have physical boundaries, mathematically identifying when a group functions as a single individual.
- **Hafez et al. (2026)** in *A Mathematical Theory of Agency and Intelligence* introduce "bipredictability" ($P$), a bounded measure of the shared information across an agent's observation-action-outcome loop. Hafez formally distinguishes "agency" (the capacity to act on predictions) from "intelligence" (the capacity to adapt the scope of the loop), providing a direct complement to AAT's $2 \times 2$ Agent Spectrum (Model Richness $\times$ Objective Richness).

### Pillar 3: Informational Closure
- **Bertschinger et al. (2006)** in *Information and closure in systems theory* define a system as "informationally closed" if no information flows into it from the environment. They demonstrate that cognitive systems can achieve closure by successfully modeling their environment, mirroring AAT's focus on the "closure defect" of composite macroscopic states.

---

## 2. Key Anchor Papers (Available in `/ref`)

1. **Miller, J. H. (2022). Ex Machina: Coevolving Machines and the Origins of the Social Universe.**
   *Significance:* The direct empirical precedent establishing the 1-state to 2-state Moore machine transition as the absolute computational threshold for the emergence of social/cooperative behavior.
2. **Krakauer, D., et al. (2014). The information theory of individuality.** 
   *Significance:* Provides the formal information-theoretic mathematics for determining when a group of components crosses the threshold to become a single, unified "individual" (a composite agent).
3. **Hafez, W., et al. (2026). A Mathematical Theory of Agency and Intelligence.**
   *Significance:* Offers a parallel, mathematically rigorous taxonomy of agency based on informational limits (bipredictability), validating the necessity of AAT's formal agent spectrum.
4. **Rubinstein, A. (1986). Finite automata play the repeated prisoner's dilemma.**
   *Significance:* The foundational economics paper proving that the structural complexity (number of states) of an agent fundamentally limits its strategic capacity.

---

## 3. Conclusion on Novelty & Overlap

The empirical observation that 2-state memory is required for social cooperation (Tit-For-Tat) is a settled finding in evolutionary game theory (Miller, Rubinstein). The use of information theory to draw boundaries around composite individuals is also established (Krakauer).

**AAT's Novel Contribution:**
AAT's contribution here is **Architectural Formalization**.

1. **The Unity Dimensions as a Rate-Distortion Surface:** Prior art like Krakauer uses information theory to identify *if* an individual exists. AAT goes further by decomposing the "quality" of that composite individual into five orthogonal axes (Epistemic, Teleological, Strategic, Perceptual, and Structural). AAT achieves pure mathematical novelty by proving that these Unity dimensions do not directly output a "cohesion score." Instead, they parameterize the Lagrangian-dual of the Information Bottleneck constraint, acting as inputs to a Rate-Distortion surface. AAT proves that even with 100% Content Unity (perfect agreement), a group will fail to act as a single agent (it will leak closure defect) if it lacks Structural Unity ($U_f$, homogeneous update rules).
2. **Anchoring the Agent Spectrum:** AAT explicitly maps Miller's evolutionary threshold to its own formal ontology. It defines the 1-state machine as the "Reactive System" (degenerate $M_t$), and the 2-state machine as the "Adaptive Tracker" (the minimal $M_t$ capable of holding a mismatch signal). By formally mapping evolutionary game theory onto cybernetic state structures, AAT grounds its abstract mathematical spectrum in verifiable empirical thresholds.