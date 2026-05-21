# Prior-Art Analysis: Composition Under Goal Divergence

**Target Claim:**
AAT analyzes what happens when Class 1 (Separated) sub-agents interact in a shared environment with partially-opposing objectives ($U_O < 1$). AAT proves that they *cannot* compose into a Class 1 macro-agent. The across-agent coupling (through the environment and mutual observation) destroys directed separation at the macro-level, degrading the composite into a Class 2 (Partial) architecture.

To recover stability, AAT shifts the mathematical framing from "Lyapunov contraction on a shared state" to "equilibrium convergence of coupled best-responses." By transcribing Monderer and Shapley's (1996) Potential Games and Rosen's (1965) Monotone Games into its cybernetic tracking loop, AAT proves that the "Sector-Persistence Template" successfully transfers to the equilibrium layer. The composite sector constant ($\alpha_{\text{joint}}$) is structurally inherited from the joint potential's curvature or the joint Jacobian's symmetric part, forcing the use of Mechanism Design to guarantee stability.

---

## 1. State of the Field & Scientific Precedence

The Undermind search reveals that analyzing the convergence of independent, selfish agents to a joint equilibrium is the central pursuit of continuous game theory, networked control, and multi-agent learning. The mathematical boundaries are highly formalized.

### Pillar 1: Potential Games and Monotone Games
AAT explicitly anchors its convergence sub-scopes on two foundational game theory results:
- **Monderer and Shapley (1996)** formalized *Potential Games*, where the incentives of all players perfectly align with a single global scalar potential function. If a game has a potential function, gradient-based play naturally converges to a Nash equilibrium.
- **Rosen (1965)** defined *Diagonally Strictly Concave* (monotone) games, proving that a unique Nash equilibrium exists and gradient play converges to it if the symmetric part of the joint Jacobian is negative-definite.
AAT explicitly imports these as its "Sub-scope $\alpha'$" conditions.

### Pillar 2: Uncoupled Dynamics and Impossibility
AAT's claim that goal-divergent composition inherently breaks down (without specific structural guarantees like potential functions) is deeply precedented by impossibility theorems in game dynamics.
- **Hart and Mas-Colell (2003)** in *Uncoupled Dynamics Do Not Lead to Nash Equilibrium* proved a sweeping negative result: if agents do not know the utility functions of other agents (uncoupled dynamics), there is no general learning algorithm guaranteed to converge to Nash equilibrium. 
- **Milionis et al. (2023)** expanded on this, showing that Nash existence proofs are non-constructive and that natural game dynamics fundamentally fail to converge in general games, leading to chaotic or cycling behavior (e.g., **Mertikopoulos et al., 2017** on *Cycles in adversarial regularized learning*).

### Pillar 3: Passivity and Dissipativity in Nash Seeking
The control theory community has actively worked to solve these non-convergence issues by applying physical stability concepts to game theory.
- **Fox and Shamma (2012)** and **Arcak and Martins (2020)** mapped population games onto passive input-output systems. They used dissipativity theory to prove that if the learning dynamics are passive and the game itself is "stable" (a generalization of monotone), the system converges to a Nash equilibrium.
- **Gadjov and Pavel (2019, 2023)** and **Belgioioso and Grammatico (2018)** applied monotone operator theory to distributed Nash equilibrium seeking, showing that proximal-point algorithms and Laplacian feedback can guarantee convergence even in partially observable or hypomonotone regimes.

---

## 2. Key Anchor Papers (Available in `/ref`)

1. **Monderer, D., & Shapley, L. (1996). Potential Games.**
   *Significance:* The foundational paper proving that when player incentives align with a global potential, best-response dynamics converge; explicitly used by AAT to define its $\alpha'$ sub-scope.
2. **Hart, S., & Mas-Colell, A. (2003). Uncoupled Dynamics Do Not Lead to Nash Equilibrium.**
   *Significance:* Proves the fundamental impossibility of guaranteed convergence when agents act independently without knowing others' payoffs, validating AAT's focus on the breakdown of Class 1 composition under divergence.
3. **Fox, M. J., & Shamma, J. (2012). Population games, stable games, and passivity.**
   *Significance:* Pioneers the use of control-theoretic passivity to analyze game theoretic convergence, strongly mirroring AAT's transfer of the sector-persistence condition to the equilibrium layer.
4. **Arcak, M., & Martins, N. C. (2020). Dissipativity Tools for Convergence to Nash Equilibria in Population Games.**
   *Significance:* Uses dissipativity and contractivity to guarantee global asymptotic stability of Nash equilibria, directly paralleling AAT's use of Lyapunov persistence in strategic composition.

---

## 3. Conclusion on Novelty & Overlap

The mathematical primitives of AAT's strategic composition—Potential Games, Monotone Games, and the use of control-theoretic tools (passivity/dissipativity) to prove convergence to Nash equilibria—are canonical, active areas of research. AAT explicitly acknowledges Monderer-Shapley and Rosen as the source of its theorems.

**AAT's Novel Contribution:**
AAT's contribution is **Architectural synthesis and Taxonomic Refinement**.

1. **Class 2 Degradation Theorem:** AAT's novel claim is not that games converge under potential functions, but the architectural observation about *what happens to directed separation*. AAT proves that even if every individual sub-agent is perfectly "Class 1" (belief updates are strictly goal-blind), the resulting macro-agent is forcibly degraded into "Class 2" (Partial). The across-agent coupling (my beliefs depend on your actions, which depend on your goals) unavoidably infects the macro-system's epistemic loop with goal-bias. 
2. **Transferring the Sector Constant:** In the control literature, passivity is usually an external property used by the analyst. AAT achieves structural synthesis by proving that the exact same "Sector-Persistence Template" that governs a single agent's belief update also governs the multi-agent equilibrium convergence. AAT proves that the macro-agent's survival constant ($\alpha_{\text{joint}}$) physically lives at the *curvature of the joint potential* (the symmetric part of the joint Jacobian). 
3. **Framing Mechanism Design as an Epistemic Floor:** By proving that $\alpha_{\text{joint}}$ requires potential/monotone game structures to avoid chaotic failure (sub-scope $\beta'$), AAT frames Mechanism Design not just as an economic tool, but as a mandatory architectural repair strategy required to restore Class 1 stability to a degraded composite system.