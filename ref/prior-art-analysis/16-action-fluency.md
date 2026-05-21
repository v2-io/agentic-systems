# Prior-Art Analysis: Action Fluency and Deliberation Cost

**Target Claim:**
AAT defines the threshold for "deliberation" vs "action fluency" as a strict mathematical tradeoff between the epistemic benefit of internal simulation (improving future action quality) and the "aporia" or mismatch drift accumulated during the deliberation pause. Deliberation is only justified when the marginal improvement in update gain outweighs the local mismatch drift rate. Consequently, in high-tempo or highly unstable environments (where the drift rate is high), the optimal duration of deliberation collapses to zero. The agent is forced into pure "implicit action" (System 1/fluency). 

AAT also extends this to a "Three-Way Resource Allocation" (Exploit, Explore, Deliberate), explicitly framing deliberation as *internal exploration* in model-space subject to diminishing returns due to finite model fidelity.

---

## 1. State of the Field & Scientific Precedence

The Undermind search reveals an extensive, multidisciplinary prior art covering the cost of deliberation, time-critical planning, and the arbitration between habitual (System 1) and goal-directed (System 2) processes.

### Pillar 1: Time-Dependent Planning & Metareasoning
The Artificial Intelligence and Planning communities have long studied the cost of thinking.
- **Boddy and Dean (1989, 1994)** pioneered "time-dependent planning" and "deliberation scheduling," introducing the concept of *anytime algorithms* (where solution quality improves with computation time, subject to diminishing returns). They explicitly modeled the utility of a decision as a function of the time spent deliberating versus the deadline constraints of the environment.
- **Horvitz (1987, 1989)** established the "Expected Value of Computation" (EVC) framework, formalizing how agents under scarce resources should trade off the cost of delay against the expected benefit of further reasoning.
- **Zilberstein (1995, 1996)** expanded this into operational bounds, showing how anytime algorithms can be compiled to dynamically trade deliberation time for quality in real-world robotics.

### Pillar 2: The Habitual vs. Goal-Directed Spectrum (Cognitive Science)
In computational neuroscience and reinforcement learning, the trade-off is framed as arbitrating between model-free (habitual/fluent) and model-based (deliberative) control.
- **Keramati, Dezfouli, and Piray (2011)** provide a highly relevant normative model demonstrating that arbitration between habits and goal-directed planning is fundamentally a *speed/accuracy trade-off*. Goal-directed planning is accurate but slow; habits are fast but inflexible. Their model shows that as the cost of time increases, the optimal strategy shifts toward habitual fluency.
- **Kool, Gershman, and Cushman (2018)** formalized how humans balance the computational costs of planning against the accuracy benefits, deciding "when hard thinking is worth it."
- **Pezzulo et al. (2013)** proposed a "Mixed Instrumental Controller" where mental simulation is only activated when its "Value of Information" exceeds the cognitive effort and the cost of reward delay.

### Pillar 3: Opportunity Cost of Time (Neuroeconomics)
- **Otto and Daw (2017)** and **Touzel et al. (2022)** frame the cost of deliberation purely as the *opportunity cost of time* (often linked to average reward rate and tonic dopamine). In fast-changing environments, the cost of delaying an action to think is the loss of the rewards that could have been acquired during that time.

---

## 2. Key Anchor Papers (Available in `/ref`)

1. **Boddy, M., & Dean, T. (1994). Deliberation Scheduling for Problem Solving in Time-Constrained Environments.**
   *Significance:* The seminal AI paper defining anytime algorithms and the formal trade-off between the expected value of continued planning and the cost of environmental deadlines.
2. **Horvitz, E. (1989). Reflection and Action Under Scarce Resources: Theoretical Principles and Empirical Study.**
   *Significance:* Provides the decision-theoretic foundation for the "Expected Value of Computation," modeling the exact cost-benefit threshold for when to stop thinking and act.
3. **Keramati, M., Dezfouli, A., & Piray, P. (2011). Speed/Accuracy Trade-Off between the Habitual and the Goal-Directed Processes.** (`ref/keramati_speed_accuracy_2011.pdf`)
   *Significance:* Proves mathematically that the transition to habitual (fluent) action is driven by the temporal cost of model-based deliberation.
4. **Pezzulo, G., et al. (2013). The Mixed Instrumental Controller: Using Value of Information to Combine Habitual Choice and Mental Simulation.**
   *Significance:* Frames deliberation explicitly as "mental simulation" evaluated by a Value of Information threshold, directly mapping to AAT's "internal exploration" claim.

---

## 3. Conclusion on Novelty & Overlap

The core intuition that deliberation takes time, that the environment changes while thinking, and that fast/unstable environments favor habits over planning is completely established science. EVC (Horvitz), anytime algorithms (Boddy/Dean), and model-based vs. model-free arbitration (Daw, Keramati) cover the exact behavioral dynamics AAT describes.

**AAT's Novel Contribution:**
AAT explicitly marks its overarching 3-way allocation (Exploit/Explore/Deliberate) as *discussion-grade* (synthetic/formulation-choice) and acknowledges its parallels to Active Inference and EVC.

However, AAT provides **pure mathematical novelty** in how it derives the *Deliberation Threshold*. Unlike neuroeconomic models that define the cost of time as "forgone average reward," AAT derives the threshold entirely from internal structural dynamics: **mismatch drift ($\rho_{\text{delib}}$) and epistemic gain ($\Delta\eta^\ast$)**. AAT proves that deliberation must stop when the marginal improvement in *update gain* drops below the *mismatch drift rate*. By formulating the cost of time not as an economic opportunity cost, but as an entropic accumulation of "aporia" (model-reality divergence) during inaction, AAT anchors the System 1 / System 2 transition directly to the physics of its core tracking loop.