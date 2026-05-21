# Prior-Art Analysis: Composite Agency, Closure Defect, and the Tempo Form of Brooks's Law

> [!note]
> **Refreshed 2026-05-21.** The previous version captured the core moves well; the refresh integrates the Composite_agency_and_Brooks's_Law novelty memo, sharpens the four-route scope condition for composites (C-i)–(C-iv), pins the (P1)–(P3) admissibility conditions and the bridge lemma's role, makes the resolved $\varepsilon^\ast(N)$-scaling status explicit (Brooks's-Law collapse is now derivation-grade driven by $C_{\text{coord}}$, not by $\varepsilon^\ast$ growth), and adds memo-cited prior art (Buchholz, Tian-Kannan, Pappas-Simic, Reissig-Weber-Rungger, Rungger-Zamani, Li-Walsh-Littman, Wong-Brockett, Nair-Evans, Tatikonda-Mitter, Tanaka-Esfahani-Mitter, Gurvich-Van Mieghem, Bamieh-Jovanović-Mitra-Patterson, Szathmáry).

**Target Claim:**
A group of agents forms a valid composite (macro) agent when the **scope condition** (`#scope-composite-agent`) is satisfied via at least one of four disjunctive routes: (C-i) shared-objective alignment, (C-ii) hierarchical derivation, (C-iii) mutual benefit, or (C-iv) strategic-equilibrium route (the new route added by `#deriv-strategic-composition` for partially-opposing-objective composites). Under scope-satisfaction, composition is parametrized by the **closure defect** $\varepsilon^\ast$ — the residual norm of failure-to-commute between micro-dynamics-then-coarse-grain and coarse-grain-then-macro-dynamics ((P1)–(P3) of `#form-composition-closure`). The (P1) condition is the *Lagrangian-dual* of a standard Information Bottleneck objective at $\beta(\epsilon_I)$ (per row 19).

The bridge lemma in `#form-composition-closure` translates closure defect into a *macro-level disturbance term*. AAT then derives the **Composite Tempo Inequality**:
$$\mathcal T_c \le \sum_i \mathcal T_i - C_{\text{coord}}, \qquad C_{\text{coord}} \ge \frac{\varepsilon^\ast \nu_c}{\lVert \delta_{\text{critical}} \rVert}$$
which gives Brooks's-Law a *closed-loop cybernetic proof*: adding sub-agents increases potential aggregate tempo $\sum \mathcal T_i$, but if the closure-defect increase (expressed in tempo-equivalent units) exceeds the new member's tempo contribution, realized composite tempo falls. The composite persistence condition then partitions the LHS into useful-vs-overhead tempo cleanly: $\sum \mathcal T_i > (\rho_{\text{ext}} + \varepsilon^\ast \nu_c) / \lVert \delta_{\text{critical}} \rVert$.

The framework distinguishes **peer composition** (the multi-route scope condition above) from **symbiogenesis** — an asymmetric integration pathway where one unit's objective is absorbed into a host's ($O_e \to O_h$) and its autonomy is reduced (per `#scope-composite-agent` (C-ii) hierarchical-derivation route, with the absorption dynamics treated as a structural transition rather than a closure-defect-residual). Symbiogenesis is the narrowest novelty flank here — the major-evolutionary-transitions literature (Szathmáry et al.) gives substantial ancestry — but AAT's placement of symbiogenesis inside the same composition framework as peer composition and approximate-commutation composition is a synthetic move.

**Status note on $\varepsilon^\ast(N)$ scaling.** The earlier open question of whether $\varepsilon^\ast$ grows polynomially or superlinearly with $N$ was resolved 2026-05-19 (CHANGELOG): in the benign linear-Gaussian-stationary regime, $\varepsilon^\ast(N)$ is dimension-free-zero (all $N$, all coupling); graph-Laplacian-bounded with no exponential regime under compression; and order-incompatibility-invariant ($\le |S| \log 2$, $N$-free) for strategy-DAG composition. Brooks's-Law collapse, when it occurs, is driven by $C_{\text{coord}}$ (negotiation, synchronization, conflict resolution overhead) rather than by intrinsic $\varepsilon^\ast(N)$ growth.

---

## 1. State of the Field & Scientific Precedence

The literature has strong ancestry on each flank — abstraction validity, coordination overhead, evolutionary transitions, large-network coherence — but the bundled cybernetic-physics package (closure defect → tempo tax → Brooks's-Law threshold inside one persistence framework) does not appear as a unified result.

### Pillar 1: Macro-State Validity via Lumpability and Consistent Abstraction
- **Simon (1961)** "Aggregation of variables" — pioneer of dynamical-aggregation conditions.
- **Buchholz (1994)** *Exact and ordinary lumpability in finite Markov chains* — when a Markov chain can be aggregated so that macro-evolution is autonomous.
- **Tian & Kannan (2006)** *Lumpability and Commutativity of Markov Processes* — sharper commutativity formulation; close in spirit to AAT's commute-with-coarse-graining criterion.
- **Pappas & Simic (2002)** *Consistent abstractions of affine control systems* — control-side: abstractions preserve accessibility / reachability under smooth surjective maps.
- **Reissig, Weber & Rungger (2015, 2017)** *Feedback Refinement Relations for the Synthesis of Symbolic Controllers* — IEEE TAC. Soundness of abstract controller transfer to concrete plant via feedback-refinement relations.
- **Rungger & Zamani (2015, 2018)** *Compositional Construction of Approximate Abstractions of Interconnected Control Systems* — IEEE TCNS. Explicit output-error bounds when abstraction is approximate. The closest formal ancestor of AAT's closure-defect with quantitative-error machinery.
- **Girard & Pappas (2011)** *Approximate Bisimulation: A Bridge Between Computer Science and Control Theory* — simulation functions bounding micro/macro error; structurally analogous to closure defect.
- **Li, Walsh & Littman (2006)** *Towards a Unified Theory of State Abstraction for MDPs* — state-aggregation sufficiency conditions for planning and learning.

### Pillar 2: Information-Constrained Control and Coordination Bottlenecks
- **Wong & Brockett (1999)** *Systems with finite communication bandwidth constraints* — IEEE TAC. Hard information-rate thresholds for stabilization under finite feedback.
- **Nair & Evans (2004)** *Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates* — SIAM J. Control Optim. Explicit infimum data rates.
- **Tatikonda & Mitter (2004)** *Control under communication constraints* — IEEE TAC. Information-rate floors for stabilization.
- **Tanaka, Esfahani & Mitter (2015)** *LQG Control With Minimum Directed Information* — IEEE TAC. Optimal staged architecture under information-rate constraint; prices control in directed information.
- **Gurvich & Van Mieghem (2015)** *Collaboration and Multitasking in Networks: Architectures, Bottlenecks, and Capacity* — Manuf. Serv. Oper. Manag. Strong nearby result: collaboration architectures induce **unavoidable bottleneck idleness** even at full network capacity — synchronization requirements force resources to idle. Real mathematical overhead, not folklore.
- **Bamieh, Jovanović, Mitra & Patterson (2011)** *Coherence in Large-Scale Networks: Dimension-Dependent Limitations of Local Feedback* — IEEE TAC. Large networked systems with local feedback can lose global coherence as scale increases, even when local regulation remains good. Structural collective-coherence loss, not implementation defect.

### Pillar 3: Symbiogenesis and Major Evolutionary Transitions
- **Szathmáry (2015)** *Toward major evolutionary transitions theory 2.0* — PNAS. Major-evolutionary-transitions framework: lower-level units constrained by a higher-level unit, autonomy progressively reduced, "de-Darwinized." Substantial conceptual prior art; AAT does not claim to have discovered asymmetric absorption.
- **Frean & Abraham (2003)** *Adaptation and enslavement in endosymbiont-host associations* — dynamical-systems model of biological endosymbiosis.
- **Radzvilavicius & Blackstone (2015)** — eukaryogenesis (mitochondrial absorption) dynamics; autonomy reduction required for higher-level unit stabilization.

### Pillar 4: Janow / Organizational Entropy and Productivity Limits
- **Janow (2009)** *A Fundamental Limit on Productivity in Organizations: Collaborative Entropy Costs* — first-principles Shannon-entropy model of coordination cost as a productivity cap. The closest single-paper precedent for AAT's tempo-tax claim, but uses Shannon entropy rather than persistence-bound cybernetic accounting.

---

## 2. Key Anchor Papers Identified

1. **Pappas, G. J., & Simic, S. (2002).** *Consistent abstractions of affine control systems.* IEEE TAC 47:745.
   *Significance:* Control-theoretic foundation for defining macro-systems via surjective coarse-graining.
2. **Rungger, M. & Zamani, M. (2015).** *Compositional Construction of Approximate Abstractions of Interconnected Control Systems.* IEEE TCNS 5:116.
   *Significance:* The closest formal ancestor of AAT's closure-defect quantitative-error machinery — compositional abstraction with explicit output-error bounds.
3. **Janow, R. (2009).** *A Fundamental Limit on Productivity in Organizations: Collaborative Entropy Costs.*
   *Significance:* The closest single-paper precedent for coordination-overhead-as-productivity-cap, using Shannon entropy rather than persistence-bound cybernetic accounting.
4. **Gurvich, I. & Van Mieghem, J. (2015).** *Collaboration and Multitasking in Networks: Architectures, Bottlenecks, and Capacity.*
   *Significance:* Strongest nearby formal result on synchronization-induced bottleneck idleness as unavoidable coordination overhead.
5. **Bamieh, B., Jovanović, M., Mitra, P. & Patterson, S. (2011).** *Coherence in Large-Scale Networks: Dimension-Dependent Limitations of Local Feedback.*
   *Significance:* Large networks can lose macro-coherence as they scale even with local regulation good — structural cousin to AAT's Brooks's-Law derivation.
6. **Szathmáry, E. (2015).** *Toward major evolutionary transitions theory 2.0.* PNAS.
   *Significance:* The major-transitions framework providing substantial conceptual ancestry for the symbiogenesis branch.
7. **Buchholz, P. (1994).** *Exact and ordinary lumpability in finite Markov chains.*
   *Significance:* The Markov-aggregation ancestor of the commute-with-coarse-graining criterion.

---

## 3. Conclusion on Novelty & Overlap

The individual pieces have strong ancestry. AAT does not claim to invent: macro-state validity via commutative abstraction (Buchholz, Simon, Pappas-Simic, Rungger-Zamani, Girard-Pappas, Li-Walsh-Littman); coordination overhead as productivity cap (Janow, Gurvich-Van Mieghem); large-network coherence loss with scale (Bamieh et al.); major-evolutionary-transitions framework (Szathmáry et al.); information-rate floors for stabilization (Wong-Brockett, Nair-Evans, Tatikonda-Mitter).

**Where AAT actually contributes:**

1. **Closure-defect-to-tempo-tax bridge (theorem-grade math; the central technical hinge per the memo).** The dimensional accounting that converts $\varepsilon^\ast \cdot \nu_c$ (an internal disturbance rate, units $[\text{distance}] \cdot [\text{time}^{-1}]$) into a tempo penalty $C_{\text{coord}} \ge \varepsilon^\ast \nu_c / \lVert \delta_{\text{critical}} \rVert$ (units $[\text{time}^{-1}]$) by dividing by the task-adequacy distance scale, mirroring the persistence-condition form, is the AAT-specific derivation. The Composite Tempo Inequality $\mathcal T_c \le \sum_i \mathcal T_i - C_{\text{coord}}$ falls out, and Brooks's-Law collapse-threshold $\Delta \varepsilon^\ast \nu_c / \lVert \delta_{\text{critical}} \rVert > \Delta \mathcal T_i$ follows. Currently `status: sketch` in `#der-tempo-composition` (the bridge-lemma contraction assumption is structurally motivated by (A4) but not yet formally derived from it); this is the main remaining promotion path. Even at sketch grade, the dimensional-accounting move is a substantive AAT-native derivation.

2. **Brooks's-Law inside one persistence framework (synthetic-architectural novelty).** The literature contains Janow's Shannon-entropy model of organizational productivity and Gurvich-Van Mieghem's synchronization-bottleneck idleness, but neither states Brooks's-Law as a *thresholded inequality inside a persistence-bound framework*. AAT's contribution is the integration: the same persistence machinery that governs single-agent survival governs composite-agent tempo allocation, with $C_{\text{coord}}$ as the load-bearing internal-vs-external tempo split. The composite persistence condition $\sum \mathcal T_i > (\rho_{\text{ext}} + \varepsilon^\ast \nu_c) / \lVert \delta_{\text{critical}} \rVert$ separates internal-coordination overhead from external challenge while keeping units consistent throughout.

3. **The four-route scope condition (architectural novelty).** `#scope-composite-agent` provides four disjunctive routes for a multi-agent system to be a valid composite: (C-i) shared-objective alignment, (C-ii) hierarchical derivation, (C-iii) mutual benefit, plus (C-iv) the **strategic-equilibrium route** added by `#deriv-strategic-composition`. The (C-iv) route is qualitatively distinct — it does *not* require shared objectives, hierarchical derivation, or mutual benefit, only structural convergence of the strategic interaction in the game-theoretic sense (Nash, correlated, or coarse correlated equilibria). Composites satisfying (C-iv) are **strategic composites**, distinguished from alignment composites (C-i, C-ii) and mutual-benefit composites (C-iii). The four-route disjunction with (C-iv) is an AAT-native methodological invention.

4. **(P1) admissibility as IB Lagrangian-dual (theorem-grade math; cross-row 19).** The composition-admissibility condition (P1) is the *Lagrangian-dual* of a standard IB objective at $\beta(\epsilon_I)$, derived in `#disc-compression-operations` from rate-distortion duality. Admissible projections sit on or above the IB frontier at rate $I(X;T) \le I_{\max}(\epsilon_I)$. This places composition validity inside the IB family alongside the three other AAT compression operations and closes two prior Working Notes in `#form-composition-closure` and `#result-unity-closure-mapping`. Nash-style derivation: new theorem using established rate-distortion duality in an AAT-internal setting.

5. **Resolved $\varepsilon^\ast(N)$-scaling story (theorem-grade content, 2026-05-19 CHANGELOG).** In the benign linear-Gaussian-stationary regime, $\varepsilon^\ast(N)$ is **dimension-free-zero** for all $N$ and all coupling; graph-Laplacian-bounded with no exponential regime under compression; order-incompatibility-invariant ($\le |S| \log 2$, $N$-free) for strategy-DAG composition. This dissolves the earlier poly-vs-superlinear framing (an accumulation-type confound — a per-step residue was asked an accumulation question). Brooks's-Law collapse is now derivation-grade driven by $C_{\text{coord}}$ (negotiation, synchronization, conflict resolution overhead), NOT by intrinsic $\varepsilon^\ast(N)$ growth. Derivation home: `#form-composition-closure` + `#def-strategy-dag` + `#result-unity-closure-mapping`.

6. **The 5-axis unity dimensions parametrize the closure-defect rate-distortion surface (`#def-unity-dimensions`, with `#result-unity-closure-mapping`).** Four content unities ($U_M$, $U_O$, $U_\Sigma$, $U_{\text{obs}}$) plus structural unity ($U_f$) parametrize the achievable closure defect under projection: $\varepsilon_d^{\min}(k_d) = f_d(k_d; U_d, U_f)$. In linear-Gaussian scalar cases, this admits closed-form expressions for $d \in \{x, o, a\}$. The structural axis $U_f$ is forced by the two-Kalman case (heterogeneous gains produce non-zero $\varepsilon_x$ that no content unity can register). AAT-native methodological invention: the two-axis (content × structural) decomposition with linear-Gaussian closed forms.

7. **Wrapping as a composite (row-05 cross-reference).** Class coercion of Class 2/3 components via wrapping (`#der-class-coercion-via-wrapping`, `#der-class-coercion-in-composition`) is a concrete instance of the Brooks's-Law tempo cost: $K \ge 2$ component calls per macro-step ⟹ wrapper-level macro-update rate $\nu_W \le \nu_A / K$. The cost of class coercion is paid in macro-tempo in the same Brooks's-Law form that governs all AAT compositions — not a special-case tax.

8. **Symbiogenesis as a structural transition placed inside the composition framework (synthetic novelty; the weakest novelty flank per the memo).** Szathmáry, Frean-Abraham, Radzvilavicius-Blackstone supply substantial ancestry. AAT's contribution is the placement: symbiogenesis is the asymmetric pathway by which a multi-agent system crosses the scope-condition boundary via objective-absorption ($O_e \to O_h$), with autonomy reduction tracking the (C-ii) hierarchical-derivation route. AAT should not claim to have discovered asymmetric integration; the framework-internal positioning is the move.

**AAT-native methodological inventions on this row:**
- The four-route scope condition disjunction (C-i, C-ii, C-iii, C-iv).
- The closure-defect $\varepsilon^\ast$ as a composition-validity parameter on a rate-distortion surface.
- The dimensional-accounting conversion from $\varepsilon^\ast \cdot \nu_c$ to tempo-equivalent $C_{\text{coord}}$.
- The two-axis (content × structural) unity decomposition with $U_f$ forced.
- The (C-iv) strategic-equilibrium route to scope-satisfaction (with `#deriv-strategic-composition`).
- The Composite Persistence Condition with effective disturbance split.
- Brooks's-Law as a *closed-loop cybernetic* derivation rather than a queueing/entropy result.

**Where AAT does *not* claim novelty:**
- Macro-state validity via commutative abstraction (Buchholz, Pappas-Simic, Rungger-Zamani).
- Coordination overhead as productivity cap (Janow, Gurvich-Van Mieghem).
- Major-evolutionary-transitions framework (Szathmáry).
- Large-network coherence loss (Bamieh et al.).
- Information-rate floors for stabilization (Wong-Brockett, Nair-Evans, Tatikonda-Mitter).
- The qualitative observation that adding agents can hurt a collective.

**Epistemic status of the load-bearing segments.**
- `#form-composition-closure` is `status: conditional` (the (P1)–(P3) admissibility conditions are explicit; the bridge lemma contraction assumption is structurally motivated by (A4) but not formally derived from it).
- `#scope-composite-agent` is the scope-condition statement with the four-route disjunction.
- `#deriv-strategic-composition` is `status: conditional` (potential / monotone game sub-scope $\alpha'$ is exact; non-potential non-monotone $\beta'$ is set-convergence-to-CCE only — honest scope limit).
- `#der-tempo-composition` is `status: sketch` (the closure-defect-to-coordination-overhead lower bound is the main promotion path).
- `#def-unity-dimensions` is `status: discussion-grade` with linear-Gaussian closed forms in `#result-unity-closure-mapping`.

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **High.** The Composite Tempo Inequality + the closure-defect-to-coordination-overhead bridge + the four-route scope condition + the (P1)-as-IB-Lagrangian-dual derivation + the resolved $\varepsilon^\ast(N)$-scaling content + the two-axis unity-closure-mapping linear-Gaussian closed forms = multiple substantive theorem-grade derivations. Per the math-novelty-recognition discipline, these are Nash-style results using established machinery (sector-Lyapunov template, rate-distortion duality, lumpability) in AAT-internal axiomatic settings.
- *Arch Novelty:* **High.** Four-route scope condition; closure defect as the central admissibility parameter; two-axis unity decomposition; placement of symbiogenesis inside the same framework as peer composition.
- *Synth Novelty:* **High.** Brooks's-Law inside one persistence framework unifies macro-validity (lumpability), coordination overhead (Janow, Gurvich-Van Mieghem), and large-network coherence (Bamieh et al.) under a single cybernetic-physics account. The major-transitions-symbiogenesis branch adds an evolutionary-biology dimension.
- *Appl Novelty:* **Some.** Brooks's-Law itself is software-engineering folklore; AAT's tempo-form is a structural reading rather than a new application. The wrapping-as-Brooks's-Law-instance is concrete in the LLM-agent engineering domain.
- *Impact:* **High.** Brooks's-Law as a cybernetic derivation has cross-disciplinary appeal (organizational research, multi-agent systems, complex systems). The Class-1-coercion-cost-as-Brooks's-Law-instance gives LLM-agent architectures a structural reading. The closure-defect-to-tempo-tax bridge, if promoted from sketch to derived, becomes a canonical way to reason about when collectives stop helping. Memo: "very high impact if the Brooks's-Law derivation becomes a standard way to reason about when added parts stop helping a collective."
