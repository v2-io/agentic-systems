# Prior-Art Analysis: Credit Assignment Boundary and Observability-by-Design

> [!note]
> **Refreshed 2026-05-21.** The previous version named only two intractability barriers (#P-hard + info-underdetermination) and omitted (a) the posterior-correlation barrier and (b) the **persistence-is-credit-assignment-free** result that is one of the most distinctive AAT contributions on this row. The actual segment `disc-credit-assignment-boundary.md` is far richer than the previous analysis credited. Restored.

**Target Claim:**
AAT characterizes the boundary between tractable and intractable per-edge credit assignment over a strategy DAG, and — distinctively — establishes what the theory can guarantee *without* solving credit assignment at all. The full structure:

1. **Three things the theory guarantees credit-assignment-free.**
   (i) *Persistence is credit-assignment-free*: the sector condition transfers from per-edge credence space to strategy-plan-confidence error $\delta_s = \hat P_\Sigma - \Phi$ via the Jacobian $\mathbf{J} = \nabla_\mathbf{p} P_\Sigma$, computable in $O(|V| + |E|)$ from status propagation — no outcome decomposition required (`#deriv-edge-credence-dynamics` Prop B.5).
   (ii) *Diagnostic framework is plan-level*: satisfaction gap, control regret, and orient cascade ordering operate on aggregate value.
   (iii) *Observability-dominance identifies the tractable edges*: only the observable subgraph can receive informative signals at all.

2. **Three independent intractability barriers** to exact per-edge attribution in general AND/OR DAGs with partial observability:
   (a) *Computational #P-hardness* via reduction to Shapley-value computation for weighted voting games (Deng & Papadimitriou 1994), since AND/OR DAGs represent monotone Boolean functions.
   (b) *Information-theoretic underdetermination*: $\dim(\mathcal I(\mathcal V_{\text{obs}})) \le |\mathcal V_{\text{obs}}|$; when fewer observable nodes than edges exist, some directions in credence-space are fundamentally unresolvable from data.
   (c) *Posterior correlation barrier*: any factored (per-edge-independent) representation discards correlation introduced by failure at multi-parent nodes; the exact posterior complexity grows exponentially with observed failures.

3. **Minimal design requirement: directional fidelity.** Any credit-assignment scheme need only satisfy $\mathbb E[(\text{signal} - p_{ij})(p_{ij} - \theta_{ij})] \le 0$ — the expected update points toward truth. Persistence is robust to approximation; a sloppy but directionally correct signal still produces bounded strategic mismatch.

4. **Hierarchy of credit assignment quality.** Level 0 (plan-level only — persistence guarantee, no per-edge diagnostics) / Level 1 (directional fidelity per edge — the concrete AAT default via gradient-attribution in log-odds coordinate with regime-modulating factor $\iota_k$) / Level 2 (proportional blame / expectation propagation) / Level 3 (full Bayesian posterior — #P-hard in general). AAT requires only Level 0; practical agents need Level 1; Level 2 is the sweet spot for most applications; Level 3 is computationally unattainable in the general case.

5. **Observability-by-design as the organizational instantiation: OKRs.** Inserting observable intermediate nodes converts a deep, partially-unobservable strategy DAG into one where credit assignment becomes componentwise. OKR failure modes (vanity metrics, too many Key Results, lagging indicators, Goodhart's Law) map to specific AAT predictions (table in `#disc-credit-assignment-boundary` §Discussion).

---

## 1. State of the Field & Scientific Precedence

The intractability side is settled across computer science and the observability-by-design side is settled in contract theory. The novelty sits in (a) the three-barrier unification, (b) the persistence-without-attribution result, (c) the log-odds default signal function with regime modulation, and (d) the OKR-as-strategy-DAG-instrumentation translation.

### Pillar 1: Complexity of Causal Responsibility and Blame
- **Eiter & Lukasiewicz (2001)** *Complexity results for structure-based causality* — NP-complete / $\Sigma_2^P$-complete results for actual-cause / responsibility / blame in structural models.
- **Eiter & Lukasiewicz (2002)** *Causes and explanations in the structural-model approach: Tractable cases*.
- **Chockler & Halpern (2003)** *Responsibility and blame: a structural-model approach* — Halpern-Pearl actual-cause and graded responsibility.
- **Aleksandrowicz, Chockler, Halpern & Ivrii (2014)** *The Computational Complexity of Structure-Based Causality* — refined complexity bounds under Halpern-Pearl's modified actual-cause definition.
- **Valiant (1979)** *The Complexity of Enumeration and Reliability Problems* — original #P-complete framework; reliability problems on graphs.
- **Provan & Ball (1983)** *The Complexity of Counting Cuts and of Computing the Probability that a Graph is Connected* — #P-hardness on graph-reliability problems closely related to AND/OR propagation.

### Pillar 2: Shapley Values, SHAP, and Boolean Function Attribution
- **Deng & Papadimitriou (1994)** *On the complexity of cooperative solution concepts* — the original #P-completeness proof for Shapley-value computation in weighted voting games, the reduction AAT cites for the AND/OR-DAG barrier.
- **Arenas, Barceló, Bertossi & Monet (2020)** *The Tractability of SHAP-Score-Based Explanations for Classification over Deterministic and Decomposable Boolean Circuits* — clean polynomial / #P-hard boundary depending on circuit structure; AAT's "tractable islands" correspond to Arenas's deterministic-decomposable condition.
- **Kara, Olteanu & Suciu (2023)** *From Shapley Value to Model Counting and Back* — tighter complexity equivalences.

### Pillar 3: Hidden-Variable Causal Identifiability
- **Balke & Pearl (1994)** *Counterfactual Probabilities: Computational Methods, Bounds and Applications* — counterfactual probabilities bounded (not point-identified) under hidden confounding.
- **Pearl & Robins (1995)** *Probabilistic evaluation of sequential plans from causal models with hidden variables*.
- **Shpitser & Pearl (2006, 2008)** identification of joint interventional distributions / completeness for the causal hierarchy.
- **Richardson, Robins & Shpitser (2012)** *Nested Markov Properties for Acyclic Directed Mixed Graphs*; **Shpitser, Evans, Richardson & Robins (2014)** nested Markov models — formalize the correlation structure introduced by latent confounding.
- **Maclaren & Nicholson (2019)** *What can be estimated? Identifiability, estimability, causal inference and ill-posed inverse problems* — distinguishes identifiability from estimability; warns that identifiability alone doesn't suffice if the inverse problem is unstable.

### Pillar 4: Sensitivity Analysis and Approximate Attribution
- **Chan & Darwiche (2001, 2004)** *When do Numbers Really Matter?* / *Sensitivity Analysis in Bayesian Networks* — global query behavior under local parameter changes; relevant for the "directional fidelity suffices" claim's robustness backbone.
- **Zhang & Poole (1994)** *Intercausal Independence and Heterogeneous Factorization*; the structural source of the posterior correlation barrier.

### Pillar 5: Observability-by-Design / Diagnosability Engineering
- **Travé-Massuyès, Escobet & Milne (2001)** *Model-based Diagnosability and Sensor Placement* — sensor placement changes detectability/discriminability/diagnosability by altering which internal failures are isolable.
- **Yassine, Ploix & Flaus (2008)** *A Method for Sensor Placement Taking into Account Diagnosability Criteria* — IJAMCS 18:497. The closest formal match for "inserting observable intermediates changes tractability class."

### Pillar 6: Moral Hazard, Observability, and Contracts
- **Holmstrom (1979)** *Moral Hazard and Observability* — the foundational sufficiency theorem: any signal containing information about the hidden action must be in the contract for optimal credit assignment.
- **Holmstrom & Milgrom (1991)** *Multitask Principal–Agent Analyses: Incentive Contracts, Asset Ownership, and Job Design* — extension to multidimensional tasks.

---

## 2. Key Anchor Papers Identified

1. **Deng, X. & Papadimitriou, C. (1994).** *On the complexity of cooperative solution concepts.*
   *Significance:* The original #P-completeness proof for Shapley-value computation over weighted voting games; the external theorem AAT imports for barrier (a).
2. **Arenas, M., Barceló, P., Bertossi, L. & Monet, M. (2020).** *The Tractability of SHAP-Score-Based Explanations for Classification over Deterministic and Decomposable Boolean Circuits.* AAAI.
   *Significance:* Clean tractability boundary: polynomial on deterministic-decomposable circuits, #P-hard otherwise. AAT's correlation-hierarchy escalation is the AAT-side mirror of this tractability boundary.
3. **Eiter, T. & Lukasiewicz, T. (2001).** *Complexity results for structure-based causality.*
   *Significance:* Foundational complexity bounds for structural-model attribution.
4. **Balke, A. & Pearl, J. (1994).** *Counterfactual Probabilities: Computational Methods, Bounds and Applications.*
   *Significance:* The cleanest precedent for the information-theoretic barrier — counterfactual queries bounded but not point-identified under hidden confounding.
5. **Holmstrom, B. R. (1979).** *Moral Hazard and Observability.*
   *Significance:* The economic foundation for observability-by-design; AAT's OKR-as-strategy-DAG-instrumentation translation generalizes this principal-agent insight to internal cybernetic structure.
6. **Yassine, A. A., Ploix, S. & Flaus, J. (2008).** *A Method for Sensor Placement Taking into Account Diagnosability Criteria.*
   *Significance:* The closest formal match for the engineering-diagnosability side of observability-by-design.
7. **Chan, H. & Darwiche, A. (2004).** *Sensitivity Analysis in Bayesian Networks: From Single to Multiple Parameters.*
   *Significance:* The closest match for "plan-level guarantees can transfer without exact local attribution" — sensitivity-of-global-query under local-parameter changes.

---

## 3. Conclusion on Novelty & Overlap

The intractability barriers are individually well-established. The observability-by-design side is well-established in contract theory and diagnosability engineering. AAT does not claim to invent #P-hardness, Shapley values, hidden-variable underdetermination, or moral-hazard contracts.

**Where AAT actually contributes:**

1. **Three-barrier unification on the strategy DAG (architectural-synthetic novelty).** The literature treats the three intractability sources separately — complexity theorists on #P-hardness, causal inferentialists on hidden-variable underdetermination, factor-graph people on the correlation-from-multi-parent-failures issue. AAT's contribution is to name all three as *independent* barriers on a *specific* structural object (the strategy DAG with AND/OR propagation) and treat them as a single boundary characterization. The three are genuinely different in kind: (a) hard computation, (b) data-insufficiency, (c) approximation-by-construction in *any* factored representation. Distinguishing them is analytical content, not just inventory.

2. **Persistence-without-credit-assignment (theorem-grade math).** The result that the sector condition transfers from per-edge credence space to strategy-plan-confidence error $\delta_s$ via the Jacobian — and is computable in $O(|V| + |E|)$ from status propagation alone, with *no outcome decomposition required* — is a theorem-grade derivation (Prop B.5 in `#deriv-edge-credence-dynamics`). The persistence guarantee for plan-level self-assessment does not depend on the agent's ability to attribute outcomes to edges. This is the most distinctive AAT contribution on this row, and the previous version of this analysis omitted it. It is a Nash-style result: new theorem derived using established sector-condition machinery in an AAT-internal setting (the strategy DAG with Jacobian-of-status-propagation).

3. **Directional fidelity as the minimal design requirement (architectural novelty).** Moving the discipline from "credit assignment is the problem" to "credit assignment is *one of several problems, with a clean minimal requirement*" is itself a re-framing. The condition $\mathbb E[(\text{signal} - p_{ij})(p_{ij} - \theta_{ij})] \le 0$ is the per-component version of the bridge theorem's B1 directional-fidelity condition — robust to approximation, sufficient for persistence, and independent of how the signals are computed. The framework explicitly does *not* require exact attribution, unbiased estimation, minimum-variance estimation, or optimality of any kind. The robustness statement — "a sloppy but directionally correct signal function still produces bounded strategic mismatch; the quality of the approximation affects the tightness of the persistence bound, not whether persistence holds at all" — is a real result and a significant theoretical convenience.

4. **Default signal function (formulation + theorem-grade content).** The log-odds gradient-attribution signal function with regime-modulating $\iota_k$ factor is a *formulation* — a concrete representational choice analogous to $\eta^\ast = U_M / (U_M + U_o)$ for gain. It is canonically positioned in the log-odds coordinate (the unique additive-evidence parameterization per `#deriv-edge-update-natural-parameter`), which closes a mechanical break the earlier probability-space presentation had (updates outside $[0,1]$ when $\|\mathbf J\|^2 \to 0$). The decomposition into outcome / attribution / regime axes is an AAT-native methodological move. The Regime-A/B/C $\iota$ scaling is the AAT-side accounting of causal validity at the per-edge update layer.

5. **OKRs as observability-by-design (synthetic-applied novelty).** The translation from Holmstrom's moral-hazard observability theorem and Yassine-style sensor-placement diagnosability to the strategy-DAG instrumentation is concrete and analytical. The OKR failure-mode table — vanity metrics ↔ observable-but-not-causally-connected nodes (high $\sigma_v$, low $p_{ij}$); too many Key Results ↔ wide OR-node correction dilution ($\alpha_\Sigma \propto 1/k$); lagging indicators ↔ evidence starvation ($\nu_{\text{obs}} \ll \rho$); Goodhart's Law ↔ terminal-condition misalignment with $O_t$ — gives the OKR discipline a structural reading: not metaphor but instantiation. The previous version of this analysis surfaced this; the refresh preserves it with the corrected scaffolding.

6. **The hierarchy of credit assignment quality (architectural novelty).** Levels 0/1/2/3 with explicit cost-benefit at each level, plus the observation that **AAT's formal guarantees require only Level 0** while practical agents need Level 1, is a non-trivial design discipline. It tells the agent how much credit-assignment investment is required for which purpose and where the tractable / intractable boundary actually matters.

**AAT-native methodological inventions on this row (per the math-novelty-recognition discipline):**
- The three-barrier decomposition (#P-hard / underdetermined / correlation-discarding) on the strategy DAG.
- The directional-fidelity B1 condition as the minimum requirement.
- The log-odds default signal function with regime-modulating $\iota_k$.
- The four-level credit-assignment quality hierarchy with explicit cost-benefit.
- The OKR ↔ strategy-DAG instrumentation translation with failure-mode prediction table.

**Where AAT does *not* claim novelty:**
- #P-hardness of Shapley value computation (Deng & Papadimitriou 1994; Arenas et al. 2020).
- Hidden-variable identifiability bounds (Balke-Pearl, Shpitser-Pearl, Maclaren).
- The correlation introduced by multi-parent failures (Zhang-Poole 1994; Richardson-Robins-Shpitser nested-Markov).
- Moral-hazard observability (Holmstrom 1979).
- Sensor placement for diagnosability (Yassine 2008).

**Epistemic status of the load-bearing segment.** `disc-credit-assignment-boundary.md` is `status: discussion-grade`. The boundary characterization (tractable cases, intractability barriers, design requirement) is discussion-grade with the intractability argument at sketch level. The design requirement is derived from the bridge theorem (`#der-gain-sector-bridge`, `#deriv-edge-credence-dynamics` Prop B.5) — that part is more like derived-conditional. The default signal function is *formulation*; its log-odds presentation is *derived-conditional* on the evidential-additivity axiom via `#deriv-edge-update-natural-parameter`. Max attainable: *conditional* — with a formal reduction from AND/OR credit assignment to Shapley value computation, the intractability claim could be promoted to derived.

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **Medium.** The persistence-without-credit-assignment result (sector-condition transfer via Jacobian, $O(|V|+|E|)$ computation) is theorem-grade in `#deriv-edge-credence-dynamics` Prop B.5. The directional-fidelity B1 condition is theorem-grade in `#der-gain-sector-bridge`. The log-odds default signal function carries the evidential-additivity-axiom uniqueness. Multiple substantive theorems beyond the imported #P-hardness machinery.
- *Arch Novelty:* **High.** The three-barrier unification on the strategy DAG, the four-level quality hierarchy, the directional-fidelity minimal requirement, the OKR-as-instrumentation translation — all architectural-methodological inventions.
- *Synth Novelty:* **High.** Bridges complexity theory + hidden-variable causal inference + sensitivity analysis + contract theory + diagnosability engineering through one structural object (the strategy DAG) with consistent vocabulary.
- *Appl Novelty:* **High.** The OKR failure-mode prediction table is a concrete domain instantiation; the framework predicts specific failure modes from specific structural defects in the OKR design.
- *Impact:* **High.** Bridging #P-hard complexity directly to human organizational design (OKRs) is highly novel cross-disciplinary work. The directional-fidelity result alone shifts the credit-assignment conversation from "exact attribution is hard" to "exact attribution may not be necessary; here's what is." The persistence-without-credit-assignment result is the kind of structural-decoupling theorem that has consequential downstream applications across RL, planning, and organizational design.
