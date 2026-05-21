# Prior-Art Analysis: Adaptive Tempo and Fisher-Local Gain

**Target Claim:**
AAT introduces "Adaptive Tempo" ($\mathcal{T}$) as the central scalar (and tensor) capacity metric of an agent. It is mathematically defined as the product of the agent's *event rate* (loop speed, $\nu$) and its *epistemic update quality* (gain, $\eta^*$). 

Under the "Fisher-local invariance regime," AAT formally derives the tensor extension of Adaptive Tempo, where the update gain is a matrix operator $K^{(k)} = (H_M + H_L^{(k)})^{-1} H_L^{(k)}$ governed by the Fisher information of the prior ($H_M$) and the likelihood ($H_L$). AAT claims that scalar tempo is only exact in the isotropic/shared-eigenbasis case, and that anisotropic correction (cross-dimensional coupling) strictly requires the matrix-Loewner persistence condition because scalar tempo dangerously overestimates adaptive capacity along weak dimensions.

---

## 1. State of the Field & Scientific Precedence

The Undermind search results for "Adaptive Tempo" connect deeply to three established mathematical domains: Adaptive Kalman Filtering, Information Geometry (Natural Gradient), and Information-Theoretic Control. While the *term* "Adaptive Tempo" is unique to AAT, the underlying mathematical primitives (the matrix gain operator governed by Fisher information) are highly precedented.

### Pillar 1: Information Geometry and Natural Gradient Descent
The realization that parameter spaces have a Riemannian metric structure defined by Fisher Information was established by **Shun-ichi Amari (1998)** in his seminal work on *Natural Gradient Works Efficiently in Learning*. Amari proved that moving along the natural gradient (pre-conditioned by the inverse Fisher information matrix) provides Fisher-efficient, optimal adaptation that avoids the plateau phenomena of standard Euclidean gradient descent. 

AAT's derivation of the tensor gain $K^{(k)} = (H_M + H_L)^{-1} H_L$ operates exactly on this Riemannian manifold. By incorporating the prior precision ($H_M$), AAT mathematically bridges Bayesian filtering with Amari's natural gradient.

### Pillar 2: Equivalence of Kalman Filtering and Natural Gradient
The specific insight that Extended Kalman Filters (EKF) and Natural Gradient Descent are algebraically equivalent has been rigorously proved in recent years.
- **Ollivier (2017, 2019)** in *Online natural gradient as a Kalman filter* provides the exact mathematical equivalence: using an online natural gradient descent on data log-likelihood to evaluate a probabilistic model is exactly equivalent to an extended Kalman filter.
- **Li et al. (2017)** (*Information Geometric Approach to Recursive Update in Nonlinear Filtering*) derived recursive Bayesian filtering updates explicitly using natural gradient descent on the statistical manifold, recovering the EKF equations as a special case.
- **Parellier et al. (2024)** further applied Amari's natural gradient to explicitly identify the noise covariance parameters of the EKF.

This body of work forms the exact mathematical bedrock for AAT's "Fisher-local invariance regime." The matrix gain operator $K^{(k)}$ used in AAT is algebraically identical to the Kalman gain expressed in information (Fisher) coordinates.

### Pillar 3: Information-Theoretic Bounds on Corrective Capacity
While the filtering literature provides the *gain* term, the control literature provides the *rate* term.
- **Touchette and Lloyd (2001)** and **Tishby and Polani (2011)** model controllers as "actuation channels" that must transform initial states to target states under information limits. 
- **Silva et al. (2014)** and **Kostina and Hassibi (2019)** establish "rate-cost tradeoffs," explicitly linking the event/data rate of a channel to the asymptotic variance/cost of the control system. 

---

## 2. Key Anchor Papers (Available in `/ref`)

1. **Amari, S. (1998). Natural Gradient Works Efficiently in Learning.**
   *Significance:* The foundational paper establishing that optimal learning trajectories must be pre-conditioned by Fisher Information, the geometric basis for AAT's tensor gain.
2. **Ollivier, Y. (2017). Online natural gradient as a Kalman filter.**
   *Significance:* Provides the rigorous algebraic proof that recursive Bayesian updates (Kalman filtering) and Natural Gradient descent are identical, explicitly validating AAT's "Fisher-local" derivations.
3. **Li, Y., et al. (2017). Bayesian Nonlinear Filtering via Information Geometric Optimization.**
   *Significance:* Derives nonlinear filtering explicitly through information geometric optimization on a statistical manifold, serving as a direct precursor to AAT's tensor update equations.
4. **Tishby, N., & Polani, D. (2011). Information Theory of Decisions and Actions.**
   *Significance:* Grounds the interaction between an agent's processing bandwidth (tempo) and action selection in rate-distortion theory.

---

## 3. Conclusion on Novelty & Overlap

The mathematical primitives of AAT's Adaptive Tempo—specifically the Fisher-local matrix gain $K^{(k)}$ and the equivalence of natural gradient to Bayesian filtering—are firmly established by Amari, Ollivier, and Li. AAT does not claim to have invented the natural gradient or the Kalman filter.

**Where AAT actually contributes:**

1. **The tensor adaptive tempo $\mathcal T = \nu \cdot K$ as a unified capacity metric (AAT-native methodological invention).** The information-geometry community studies the *geometry of the update* (the gain / direction); the networked-control community studies the *speed of the update* (the data rate / frequency). AAT's $\mathcal T = \nu \cdot K$ multiplies them into a single capacity metric. This is a methodological invention purposeful to the cybernetic-physics frame, not a relabel: the multiplication makes the trade-off between richer-per-step updates and faster-per-step updates analytically explicit, and the matrix form makes the anisotropic case first-class.

2. **The matrix-Loewner persistence condition $\Sigma_\infty \prec D_\delta$ (theorem-grade math).** Under cross-dimensional correction (where prior and likelihood eigenbases misalign), a scalar tempo metric is mathematically *unsafe* and will falsely predict survival. AAT lifts the persistence inequality into a matrix-Loewner condition, providing a rigorous closed-form test for survival in anisotropic environments. This is theorem-grade math derived using established Lyapunov / matrix-comparison machinery in an AAT-internal axiomatic setting (Nash-style — new theorem using existing techniques).

3. **The Fisher-local invariance regime as scope-marker (architectural-methodological invention).** Explicit naming of the regime under which the Fisher-local matrix-gain analysis is exact (and identifying the larger scope where it is approximate) is the CS-norm scope-precision-is-valuable move. The Fisher-local-vs-Fisher-global distinction is AAT-native methodological apparatus.

4. **The cross-eigenbasis safety result (theorem-grade, application-of-Loewner-comparison).** Proving that scalar tempo overestimates capacity along weak dimensions in anisotropic environments is itself a substantive Nash-style result. The proof uses Loewner-comparison machinery; the result is new.

**AAT-native methodological inventions on this row:**
- The tensor tempo $\mathcal T = \nu \cdot K$ as a unified capacity metric.
- The Fisher-local invariance regime.
- The matrix-Loewner persistence condition $\Sigma_\infty \prec D_\delta$.
- The "isotropic vs anisotropic" agent-environment distinction with the safety-of-scalar-tempo result.

**Where AAT does *not* claim novelty:**
- Amari's natural gradient (1998).
- Ollivier's EKF-as-natural-gradient equivalence (2017).
- Li et al.'s information-geometric Bayesian filtering (2017).
- Touchette-Lloyd / Tishby-Polani actuation channels (2001 / 2011).
- Silva et al. / Kostina-Hassibi rate-cost tradeoffs (2014 / 2019).
- Fisher information itself, the Kalman gain, or the natural gradient as classical objects.

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **High.** The matrix-Loewner persistence condition + the cross-eigenbasis safety theorem + the tensor tempo capacity metric are theorem-grade derivations using established machinery in AAT-internal axiomatic settings.
- *Arch Novelty:* **High.** The Fisher-local invariance regime as scope-marker; the isotropic-vs-anisotropic agent-environment distinction; the matrix-form-makes-anisotropy-first-class architectural move.
- *Synth Novelty:* **High.** Unifies information geometry (Amari natural gradient), Bayesian filtering (Kalman gain in information coordinates), and information-theoretic control (rate-cost tradeoffs) into one cybernetic-capacity metric.
- *Appl Novelty:* **None.** No domain-specific instantiation in this row.
- *Impact:* **High.** Per the meta-summary's Part 2 — the tensor capacity metric "translates pure information geometry into a rigorous existential bound on agent survival" and the matrix-Loewner condition is "scalar tempo is unsafe in anisotropic environments." The connection to active-inference / FEP-adjacent fields gives this row broad cross-disciplinary reach.