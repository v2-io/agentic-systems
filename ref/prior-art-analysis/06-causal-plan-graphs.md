# Prior-Art Analysis: Strategy DAGs, Loop-Interventional Access, and the Correlation Hierarchy

> [!note]
> **Refreshed 2026-05-21.** The previous version captured the Pearl-and-AND/OR-planning ancestry but missed (a) the four-obstacle precision in the loop-as-Level-2-engine claim, (b) the Regime A/B/C identification-strength partition, (c) the three specific AAT-distinctive moves vs the active-inference / cybernetics shared-ancestry, (d) the correlation-hierarchy L0/L1/L1'/L2 escalation as the AAT response to causal insufficiency, and (e) the triple-depth-penalty breakdown into three specific axes. Restored.

**Target Claim:**
AAT's strategy is an **explicit Causal Plan Graph** (DAG with probabilistic AND/OR semantics, regime-indexed identification strength for edges, and compact single-parameter edge credences) whose execution by an in-scope agent provides **interventional data** in the sense of Pearl's Level 2. The framework's contribution decomposes into four results:

1. **Loop-interventional access (`#der-loop-interventional-access`, `status: exact`).** By the temporal-ordering postulate, an agent's action $a_t$ causally precedes the next observation $o_{t+1}$; the agent *chose* the action, the environment responded. The feedback loop therefore generates **intervention-produced data**. The result is *exact* as a logical consequence of temporal ordering and the feedback-loop structure; it is about *data availability*, not reasoning capacity.

2. **The four-obstacle precision (scope-honest framing).** AAT is unusually careful to distinguish *action-generated data* from *cleanly identified do-estimates*. Between intervention-produced data and a usable estimate of $P(o \mid do(a_t), \Omega_t)$ stand: (i) **coverage** (the agent must have tried diverse actions, not just one policy); (ii) **within-step confounding** (unobserved variables affecting both action choice and outcome); (iii) **delay** (consequences may appear much later than $t+1$); (iv) **partial observability** ($o_{t+1}$ reveals only part of the outcome).

3. **Regime-indexed identification strength (`#scope-edge-update-causal-validity`).** The strength of usable causal identification from loop data varies by domain. **Regime A**: intervention-rich (software, laboratory science) — clean do-estimates. **Regime B**: partial intervention (organizational settings) — moderately identified. **Regime C**: observation-only — weak; falls back to observational proxy. The identifiability coefficient $\iota_k \in [0, 1]$ per edge modulates the strength of the update at the per-edge level (per `#disc-credit-assignment-boundary`, row 17).

4. **The Triple Depth Penalty (composite finding from `#def-strategy-dag` + chapter-end implications segment).** Deep hierarchical plans pay along three distinct axes: (a) *probabilistic confidence decay* across conjunctive depth; (b) *evidence starvation* at downstream nodes (downstream edges receive less evidence because they are tested only when upstream steps succeed); (c) *cognitive maintenance burden* growing with depth. The bundled package — fragility + learnability + maintenance — gives a structural reason to prefer shallower observable strategies, with the three axes as separately addressable failure modes.

5. **Correlation Hierarchy (L0 / L1 / L1' / L2) as escalation rule.** When sibling action propositions share a latent common cause, the L0 independent-edge plan graph is *causally insufficient*. The framework supplies a principled escalation: L0 → L1 (augmented DAG with strict-prerequisite common-cause nodes) → L1' (mixture form for soft facilitators under Cramér-Rao-floor constraint) → L2 (full joint correlation, exponential). This is one instance of the framework's tiered-approximation pattern (row 18) and is operationalized by the identifiability-floor instance for on-policy L0-insufficiency detection (Instance 1 of `#disc-identifiability-floor`, row 11). The Pearl Level-2 escape via `#der-loop-interventional-access` is exactly the rank-augmentation that escapes the Sylvester-law-of-inertia rank-collapse floor at L0.

---

## 1. State of the Field & Scientific Precedence

The literature has strong ancestry on each flank. AAT's contribution is the bundled internal-agent synthesis: an internal strategy DAG learned from interventions of ordinary acting, with depth-cost bundle and principled correlation-hierarchy escalation.

### Pillar 1: Action-vs-Observation and the $do$-Calculus
- **Pearl (1994)** *A Probabilistic Calculus of Actions* — the $do$-operator and local surgery viewpoint.
- **Pearl & Robins (1995)** *Probabilistic evaluation of sequential plans from causal models with hidden variables* — sequential plans as intervention sequences.
- **Heckerman & Shachter (1994, 1995)** *Decision-Theoretic Foundations for Causal Reasoning* — decisions as causal nodes in DAG-like planning models.
- **Dawid (2002, 2010)** *Influence Diagrams for Causal Modelling and Inference* / *Identifying the consequences of dynamic treatment strategies*.
- **Bareinboim, Correa, Ibeling & Icard (2022)** *On Pearl's Hierarchy and the Foundations of Causal Inference* — the Causal Hierarchy Theorem that L2 distinctions are not in general identifiable from L1 data.
- **Tian (2008)** *Identifying Dynamic Sequential Plans* — reduction to identification of causal effects in causal Bayesian networks.
- **Shpitser & Tchetgen (2014)** *Causal Inference with a Graphical Hierarchy of Interventions* — node/edge/path interventions hierarchy.

### Pillar 2: Internal-Agent Adoption of Action-as-Intervention
- **Ortega & Braun (2008)** *A Minimum Relative Entropy Principle for Learning and Acting* — adaptive agent's own past actions in an input-output stream must be treated as interventions, not as ordinary evidence. **The closest existing ancestor for AAT's claim** that ordinary acting itself generates interventional evidence for internal learning.
- **Ortega & Braun (2009)** *A Bayesian Rule for Adaptive Control based on Causal Interventions* — extends the Bayesian-rule-as-intervention idea.

### Pillar 3: Compact AND/OR Plan Structures with Local Failure Parameters
- **Barnett (1983)** *Optimal searches from AND/OR nodes* — AND/OR search structure.
- **Cazenave & Moneret (1997)** *Development and Evaluation of Strategic Plans*.
- **Ghosh, Chakrabarti & Dasgupta (2021)** *Execution Ordering in AND/OR Graphs with Failure Probabilities* — expected penalty in AND/OR graphs with task-failure probabilities and rollback costs; execution ordering matters, optimal substructure can fail.
- **Kushmerick, Hanks & Weld (1994, 1995)** BURIDAN-style probabilistic planning with context-dependent action effects.
- **De Mello & Sanderson (1986)** AND/OR graphs for assembly plans balancing operational complexity against probability of success.
- **Bryce & Smith (2006)** *Using Correlation to Compute Better Probability Estimates in Plan Graphs* — assuming independence between action preconditions overestimates success probability; direct precursor to AAT's correlation-hierarchy escalation.

### Pillar 4: Reliability Engineering and Hidden Common-Cause Augmentation
- **Vesely (1972, 1987)** Fault Tree Handbook — minimal cut sets, qualitative-quantitative fault analysis.
- **Fleming & Raabe (1978)** common-cause-failure quantitative analysis.
- **Papazoglou & Mitra (1981)** sympathetic failures in redundant systems.
- **Page & Perry (1989)** common-cause-failure system reliability model.
- **Vaurio (2002)** *Treatment of general dependencies in system fault-tree and risk analysis* — IEEE Trans. Reliab. The clearest direct ancestor for the L0→L1 escalation when component independence fails.
- **Xing (2005, 2009)** reliability modeling for complex hierarchical systems with common-cause failures.
- **Meshkat (2003)**, **Xing, Meshkat & Donahue (2006)** phased-mission system reliability with dependent failures.

### Pillar 5: Action-Perception Loop in Active Inference and Cybernetics
- **Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo (2017)** *Active Inference: A Process Theory*.
- **Parr & Pezzulo (2022)** *Active Inference*, MIT Press, ch. 3.
- **Wiener (1948)** *Cybernetics*.
- **Conant & Ashby (1970)** *Every good regulator of a system must be a model of that system*.
- **Bruineberg, Dolega, Dewhurst & Baltieri (2022)** *The Emperor's New Markov Blankets* — explicit Pearl-vs-Friston blanket distinction; the conservative-form posture AAT inherits.

---

## 2. Key Anchor Papers Identified

1. **Pearl, J. (1994).** *A Probabilistic Calculus of Actions.*
   *Significance:* The $do$-operator and the formal action-vs-observation distinction that AAT inherits.
2. **Ortega, P. A. & Braun, D. A. (2008).** *A Minimum Relative Entropy Principle for Learning and Acting.*
   *Significance:* The closest existing ancestor — agent's own past actions in an I/O stream must be treated as interventions. AAT's specific contribution beyond is the internal-strategy-DAG synthesis and the regime-indexed identification strength.
3. **Bareinboim, E., Correa, J. D., Ibeling, D. & Icard, T. (2022).** *On Pearl's Hierarchy and the Foundations of Causal Inference.*
   *Significance:* The Causal Hierarchy Theorem; AAT's distinctive move is to use the loop-interventional-access result as the escape from the L2-not-identifiable-from-L1 floor (Instance 1 of `#disc-identifiability-floor`).
4. **Ghosh, P., Chakrabarti, P. & Dasgupta, P. (2021).** *Execution Ordering in AND/OR Graphs with Failure Probabilities.*
   *Significance:* AND/OR graph fragility cost analysis; structural ancestor for AAT's depth-cost bundling and for execution-order-dependent expected penalty.
5. **Bryce, D. & Smith, D. E. (2006).** *Using Correlation to Compute Better Probability Estimates in Plan Graphs.*
   *Significance:* Direct precursor to AAT's L0→L1 escalation — assuming independence between action preconditions overestimates success probability.
6. **Vaurio, J. (2002).** *Treatment of general dependencies in system fault-tree and risk analysis.*
   *Significance:* The reliability-engineering ancestor of common-cause augmentation; structurally analogous to AAT's L1 step.

---

## 3. Conclusion on Novelty & Overlap

AAT does not invent: the $do$-operator, the Causal Hierarchy Theorem, AND/OR graphs with local failure parameters, common-cause augmentation of fault trees, or the action-perception loop. Ortega-Braun (2008) supplies the closest existing ancestor for treating agent action as intervention; the active-inference and cybernetics lineages share the broader action-perception-loop framing.

**Where AAT actually contributes:**

1. **Loop-interventional access as a theorem-shaped result (`status: exact`).** AAT explicitly *lifts* the observation that action-generated data is interventional in character to a load-bearing theorem connected to Pearl's causal hierarchy via Bareinboim-Correa-Ibeling-Icard 2022. The active-inference / cybernetics tradition has the underlying observation but rests on Bayesian-network generative models (Pearl Level 1, associational); it does not invoke the causal-hierarchy theorem to argue the loop's data is the substrate Level-2 queries require. AAT does, and the consequence is that $\Sigma_t$ is positioned as a **causal** DAG rather than a **Bayesian-network** DAG.

2. **The three specific moves vs the action-perception-loop ancestry (architectural-methodological inventions).**
   - **The Bareinboim-hierarchy connection.** Lifts the loop-as-Level-2 observation to a theorem.
   - **Regime-indexed strength of causal identification.** Regime A (intervention-rich) / B (partial intervention) / C (observation-only) partitions edge updates with identifiability coefficients $\iota_k$. The AI literature treats causal identifiability uniformly within modeling assumptions and does not surface the regime distinction at the segment level.
   - **Explicit scope honesty.** The careful split between "data generated under intervention" and "cleanly identified do-estimates" — four obstacles (coverage, within-step confounding, delay, partial observability) made explicit. Bruineberg et al. (2022)'s Pearl-vs-Friston critique documents that the AI literature sometimes elides this; AAT's careful split is the conservative form.

3. **The triple-depth-penalty bundle (theorem-grade math + architectural synthesis).** The three axes (probabilistic confidence decay + evidence starvation + maintenance cost) are individually known: Ghosh et al. 2021 gives depth fragility; RL credit assignment gives evidence starvation; MDL gives complexity costs. AAT's contribution is the *bundled* package as one structural cost of depth, with the three axes as separately addressable failure modes for plan design.

4. **The Correlation Hierarchy L0 / L1 / L1' / L2 with named tier-transitions (architectural-methodological invention).** When sibling propositions share a latent common cause, AAT prescribes a principled escalation rather than ad-hoc parameter retuning: augment to L1 (strict-prerequisite common-cause node) → L1' (mixture form for soft facilitators) → L2 (full joint correlation). The Cramér-Rao-floor instance in `#deriv-edge-credence-dynamics` Prop B.7 (Instance 2 of `#disc-identifiability-floor`) makes the L1' transition theorem-grade: under unobservable common cause, the Fisher information matrix is rank-1 and per-conditional decomposition is *underdetermined* — the structural escape (observe the latent or jointly observe multiple children) is named exactly.

5. **Compact single-parameter edge credences as a deliberate first-order abstraction.** Single-parameter edge credences sit at a sweet spot — rich enough for causal revision (per the regime-indexed Beta-Bernoulli machinery in `#deriv-edge-credence-dynamics`), simple enough for practical strategy maintenance. AAT is explicit that this is a deliberate compression, not a universal sufficiency claim.

6. **The loop-interventional-access result is the unique broadly-available escape from the L0-causal-insufficiency-detection no-go (cross-row 11).** Instance 1 of `#disc-identifiability-floor`: under purely on-policy execution with short-circuit AND/OR semantics, L0 vs L1 distinction is a Level-2 question forbidden by the Causal Hierarchy Theorem from on-policy L1 data. The escape — joint sibling observability under exploration via `#der-loop-interventional-access` — is the rank-augmentation that breaks the Sylvester-law-of-inertia rank-collapse floor. This makes loop-interventional-access *load-bearing*, not just useful.

**AAT-native methodological inventions on this row:**
- The strategy DAG with regime-indexed identification strength as a *causal* internal-strategy object.
- The four-obstacle precision (coverage / within-step confounding / delay / partial observability).
- The Regime A/B/C edge-identification partition with $\iota_k$ coefficient.
- The triple-depth-penalty bundle as a structural cost of depth.
- The L0 / L1 / L1' / L2 Correlation Hierarchy with named tier-transitions.
- The compact single-parameter edge-credence representation as a deliberate first-order abstraction.
- The placement of loop-interventional-access as the unique broadly-available escape from the L0-causal-insufficiency-detection floor.

**Where AAT does *not* claim novelty:**
- The $do$-operator (Pearl 1994).
- Sequential-plan identification under hidden variables (Pearl-Robins 1995, Tian 2008).
- Decision nodes as causal nodes (Heckerman-Shachter 1994, 1995).
- AND/OR graph structure (Barnett 1983, Cazenave-Moneret 1997, Ghosh et al. 2021).
- Common-cause augmentation in reliability engineering (Vesely-Goldberg-Roberts-Haasl, Vaurio, Xing).
- Agent's own actions as interventions on the I/O stream (Ortega-Braun 2008, 2009).
- Action-perception loop in active inference / cybernetics (Friston et al., Parr-Pezzulo, Wiener, Conant-Ashby).
- The Causal Hierarchy Theorem (Bareinboim-Correa-Ibeling-Icard 2022).

**Epistemic status of the load-bearing segments.**
- `#der-loop-interventional-access` is `status: exact` (logical consequence of temporal ordering and feedback-loop structure).
- `#der-causal-insufficiency-detection` is *exact* for shallow strict-prerequisite cases and *robust qualitative* for general DAG topology.
- `#deriv-edge-credence-dynamics` Prop B.7 (Cramér-Rao floor for L1' identifiability) is *exact*.
- `#def-strategy-dag` is `status: definition` with the L0/L1/L1'/L2 hierarchy and the regime-indexed edge semantics.
- The triple-depth-penalty bundle is *robust qualitative*; the three axes individually are derivation-grade in supporting segments.

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **Some.** The loop-interventional-access result (`status: exact`); the on-policy L0-insufficiency-detection no-go (Instance 1 of identifiability-floor); the Fisher rank-1 mixture-identifiability refutation (Instance 2); the regime-indexed identification strength with $\iota_k$; the triple-depth-penalty bundle. These are theorem-grade in their home segments; this row catalogues them. Per the math-novelty-recognition discipline, this is theorem-grade content even if the constituent theorems live in sister segments.
- *Arch Novelty:* **High.** Strategy DAG as causal object with regime-indexed identification; four-obstacle precision; Correlation Hierarchy with named tier-transitions; compact-edge-credence first-order abstraction; placement of loop-interventional-access as unique escape from on-policy L0-detection floor.
- *Synth Novelty:* **High.** Bundles Pearl-style intervention semantics + decision-theoretic causal planning + Bayesian adaptive control (Ortega-Braun) + AND/OR-graph fragility + reliability-engineering dependence modeling + identifiability-floor meta-pattern under one strategy object.
- *Appl Novelty:* **None.** No domain-specific instantiation in this row's lead.
- *Impact:* **Medium-to-High.** Memo: "high impact if the 'ordinary acting as intervention stream' idea is seen as a useful internal-agent principle; very high impact if the compact causal-strategy-graph view becomes standard language for agent planning and diagnosis." The connection to row 11's identifiability-floor pattern + row 17's credit-assignment-boundary + row 18's tiered-approximation discipline makes this row a load-bearing hub for the framework's middle.
