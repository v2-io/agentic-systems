# Causal Extensions: Beyond TFT's Current Scope

**Status**: Exploratory. This document explores what causal theory offers software development that goes beyond TFT's current treatment. TFT establishes causal structure as a postulate (TF-02) and builds Pearl's three-level hierarchy into the theory, but doesn't develop the full machinery of structural causal models, DAG-based inference, or do-calculus. Software development is a domain where this full machinery might be unusually productive.

## 1. Explicit Causal DAGs in Software

Most TFT domains require inferring causal structure from observational data or domain knowledge. Software is remarkable in that much of the causal structure is *declared*:

### 1.1 The Dependency DAG

Import statements, function calls, type dependencies, and module boundaries create an explicit directed graph:

    module A imports module B function f calls function g type T depends on type U service X calls service Y's API

This graph IS a (partial) causal DAG for change propagation: a change to module B may require changes to module A (because A depends on B), but not vice versa (unless there are cycles, which are themselves a diagnostic signal — they indicate causal structure the architecture failed to keep acyclic).

[Confident] This means Pearl's do-calculus can be applied more directly in software than in most domains. The question "if I change this interface, what else must change?" is a causal query answerable (approximately) from the dependency graph without needing randomized experiments or untestable assumptions.

### 1.2 The Change-Propagation DAG

Beyond static dependencies, the *historical* change propagation pattern (from git) reveals causal structure that the declared dependencies may not capture:

- Files that empirically co-change often have a causal relationship the dependency graph misses (shared assumptions, implicit contracts, copy-paste coupling)
- Files that are declared-dependent but rarely co-change have a weaker causal link than the dependency graph suggests (stable interfaces that absorb changes)

[Confident] TST's T-10 (coherence-coupling measurement) IS an attempt to measure this historical causal structure. But T-10 uses correlation (co-change frequency) as a proxy for causation (change propagation). The distinction matters: two files might co-change because they're both affected by a common cause (a shared requirement change) rather than because one causes changes in the other. Proper causal analysis would separate these.

### 1.3 Causal Discovery from Git History

Given sufficient git history, we can attempt causal discovery — inferring the causal DAG from observational data. The standard machinery applies:

**Temporal ordering** provides causal direction for free (TF-02's core insight). If commit C1 precedes commit C2, and C2 touches files that C1 also touched, C1 is in C2's causal past. The direction of causation is always known from the temporal order.

**Interventional data is naturally available.** Every commit IS an intervention — the developer chose to change specific files and observed the consequences (test results, production behavior, subsequent commits). This places software squarely in TF-08's Regime A (randomized interventions) for CIY estimation.

**Confounders exist but are partially identifiable.** The common cause "a new feature requirement" may drive changes to multiple files. But the requirement itself is often traceable (linked issues, PR descriptions), providing a partial confounder adjustment.

[Plausible] A causal discovery algorithm (PC, GES, or constraint-based) run on per-commit change data, with temporal ordering as a constraint, could produce a richer causal graph than either the static dependency DAG or the co-change correlation matrix. This would formalize what experienced developers know intuitively: which parts of the system are *actually* causally coupled in practice, not just declared-coupled in code.

**Open question**: How much does the causal graph differ from the dependency graph in practice? If they're mostly the same, the machinery adds little. If they diverge significantly, the causal graph is the one to optimize against — and the divergence points are architectural improvement opportunities.

## 2. Interventional Reasoning (Level 2)

Developers do Level 2 reasoning constantly:

    "If I do(change this function signature), what will break?"

In most TFT domains, this requires model-based prediction. In software, the developer can *actually perform the intervention* and observe:

- **Static analysis**: The compiler/linter tells you immediately which callers are now broken. This is an instant, low-noise Level 2 observation.
- **Test execution**: Run the test suite after the change. This is a slightly delayed, slightly noisier Level 2 observation (tests may not cover all effects).
- **Deployment to staging**: Observe behavior under realistic conditions. Higher latency, higher coverage.

[Confident] The software domain provides a *spectrum of Level 2 observation channels* with different (nu, U_o) characteristics:

| Level 2 channel | nu (speed) | U_o (noise) | Coverage |
|-----------------|------------|-------------|----------|
| Type checker | Instant | Near-zero | Syntactic/type only |
| Linter | Instant | Very low | Style + common errors |
| Unit tests | Seconds-minutes | Low | Tested paths only |
| Integration tests | Minutes | Low-medium | Cross-module paths |
| Staging deploy | Minutes-hours | Medium | Near-production |
| Production canary | Hours | Low (real traffic) | Full coverage |

Each channel is a CIY source. The "if I do this, what happens?" question is answered with progressively higher fidelity (lower U_o) and broader coverage, at the cost of higher latency (lower nu). The optimal developer strategy is to use fast, narrow channels first (type checker, unit tests) and escalate to slower, broader channels only when needed — exactly the sequential information-gathering strategy that TF-08's CIY framework motivates.

### 2.1 CIY for Software Actions

The causal information yield of a software action depends on what it reveals about the system's causal structure:

**High-CIY actions** (reveal causal structure):
- Changing an interface and observing what breaks (reveals actual coupling)
- Adding a failing test (reveals behavioral assumptions)
- Introducing a deliberate bug and observing detection time (reveals monitoring coverage — a meta-observation about observation quality)
- Asking an expert "why was this designed this way?" (query action with potentially enormous CIY — TF-08's barometer insight)

**Low-CIY actions** (reveal little causal structure):
- Reading code you already understand (confirming existing model — delta ≈ 0)
- Running passing tests on unchanged code (no new information)
- Re-deploying identical code (no intervention contrast)

[Plausible] This suggests an information-theoretic approach to developer workflow optimization: prioritize actions that maximize CIY per unit time. A developer stuck on a bug should ask: "What action would maximally reduce my uncertainty about the causal mechanism?" Often the answer is not "keep reading code" (low CIY if the code is already in-model) but "write a targeted test" (high CIY — the outcome directly reveals causal structure) or "ask someone" (potentially very high CIY if the source is reliable and the question is well-formed).

## 3. Counterfactual Reasoning (Level 3) via Git

This is where software development becomes exceptional among TFT domains.

### 3.1 The Counterfactual Machine

Git provides a literal time machine for counterfactual reasoning:

    "What would have happened if we had chosen architecture X instead of Y?"

Procedure:
1. git checkout <commit-before-decision>
2. Implement alternative architecture X
3. Replay subsequent features on top of X
4. Measure: change-set sizes, test failures, development time, runtime behavior
5. Compare to the actual history under architecture Y

This is Level 3 epistemic access with *ground-truth verification* — not model-based simulation with uncertain fidelity, but actual execution of the counterfactual. Nearly no other TFT domain has this.

[Confident] The ability to literally execute counterfactuals is profound. It means:

- **Architectural decisions can be retrospectively evaluated.** Not "we believe X was better" but "we measured that X would have resulted in 30% smaller change-sets for the subsequent 50 features."

- **TFT's model class fitness F(M) becomes empirically measurable.** Fork at a past point, try a different model class (architecture), and measure whether it would have achieved higher sufficiency for the actual future.

- **TST's n_future estimation can be validated.** Compare the predicted n_future at time t to the actual n_future observed by time t + Delta_t.

### 3.2 Limitations of Git Counterfactuals

The counterfactual isn't perfect:

1. **Replaying features requires re-specification.** You can fork the code, but you need to re-implement each subsequent feature in the alternative architecture. This takes real time and may introduce experimenter bias. (Partial mitigation: AI agents can re-implement at lower cost, with some standardization of effort.)

2. **Path dependence.** The sequence of features actually implemented may have been influenced by the architecture chosen. Under architecture X, the team might have chosen different features (because some become easier or harder). The counterfactual "same features, different architecture" may not be the most relevant comparison.

3. **Environmental coupling.** If the architecture choice affected external factors (team hiring, customer acquisition, competitor response), those effects can't be replayed.

4. **Computational cost.** Full counterfactual replay is expensive. Heuristic approximations (e.g., measuring change-set sizes for a sample of features, or using static analysis to predict change propagation) may be necessary.

[Confident] These limitations are real but much less severe than in other domains. A partial counterfactual (replay 10 representative features instead of 500) still provides far more information than model-based speculation. The marginal cost of counterfactual evaluation is also dropping as AI agents can re-implement features faster.

### 3.3 Counterfactual-Driven Architecture Evaluation

A new workflow becomes possible:

1. **At decision points** (new project, major refactoring, architectural crossroads):
   implement small proofs-of-concept in 2-3 candidate architectures.

2. **After N features under the chosen architecture**: fork from the decision point, re-implement a sample of those N features under each alternative, measure temporal cost (change-set size, comprehension time proxy, test failures).

3. **Use the counterfactual data to calibrate future decisions**: which architectural patterns actually minimized temporal cost for which feature types?

[Speculative] This could eventually create an empirical science of software architecture — not "we believe microservices are better" but "for systems with these change patterns, this architecture minimized total temporal cost by X%." The data would be expensive to gather but enormously valuable once accumulated. AI agents make the cost more tractable.

## 4. Causal Inference for Change Prediction

Beyond retrospective counterfactuals, causal modeling enables prospective prediction:

### 4.1 Predicting Change Propagation

Given the causal DAG (from dependency analysis + historical co-change + causal discovery), predict: "If we change module A, what is the probability that modules B, C, D will also need changes?"

This is a causal query: P(change(B) | do(change(A))), not the associational P(change(B) | change(A)). The distinction matters: modules A and B might historically co-change because of a common cause (shared requirement), but changing A might not cause B to need changes (if the common cause is absent this time).

[Plausible] Standard do-calculus adjustment on the identified DAG gives:

    P(change(B) | do(change(A))) = sum_C P(change(B) | change(A), C) * P(C)

where C is the set of confounders (common causes like shared requirements). If the DAG is correctly specified (a big if), this gives more accurate change propagation predictions than simple co-change correlation.

### 4.2 The Change-Set Size as Causal Downstream

TST's T-08 (implementation time proportional to change-set size) can be reframed causally: the change-set IS the set of all nodes in the causal DAG that are downstream of the initial intervention. Good architecture minimizes the expected downstream set for typical interventions.

[Confident] This reframing connects TST's empirical claim to a formal causal structure. The "change-set size" for feature F is |downstream(intervention(F), DAG)|. Architecture optimization is DAG optimization: arrange the causal structure so that typical interventions have small downstream sets.

### 4.3 Coupling as Causal Path Strength

TST's D-06 (coupling = P(change(B) | change(A))) is the associational analog.
The causal version is:

    coupling_causal(A, B) = P(change(B) | do(change(A)))

And the full coupling structure is the matrix of all pairwise causal coupling strengths — a weighted adjacency matrix of the causal DAG.

[Plausible] If we can estimate this matrix (from dependency analysis + adjusted co-change frequencies), we can optimize architecture against it. The goal is to minimize total expected downstream change propagation:

    minimize sum_F P(F) * |downstream(intervention(F), DAG)|

This is a graph optimization problem: find the DAG structure (architecture) that minimizes expected downstream set size given a distribution over interventions (features). This connects software architecture to causal structure optimization — a framing I haven't seen elsewhere.

## 5. Runtime Causal Models

TST's T-12 (continuous operation under perturbation) addresses runtime behavior, but without causal formalism. TFT's framework extends naturally:

### 5.1 The Runtime Environment as a Separate Omega

The running system has its own state (memory, connections, request queues, caches) that evolves according to its own dynamics. Production incidents are mismatch events where the system's behavior diverges from the developer's model of runtime behavior.

[Confident] This means the "agent" monitoring a production system is a distinct TFT agent (or a distinct mode of the same agent) with:
- Observation channels: logs, metrics, traces, alerts
- Actions: deploy, rollback, scale, restart, configure
- Model: expected runtime behavior
- Mismatch: anomaly detection (production behavior ≠ expected)
- Tempo: monitoring frequency × anomaly detection accuracy

### 5.2 Deployment as Intervention

A deployment is a Level 2 intervention on the runtime environment:

    do(deploy(new_code)) → observe(production_behavior)

The CIY of a deployment depends on how different the new code is from the old — a no-op deploy has zero CIY, a major feature deploy has high CIY. Canary deployments and feature flags are strategies to reduce the *blast radius* of the intervention while preserving its CIY — exactly the exploration-exploitation balance (TF-08) applied to the deployment domain.

[Plausible] Blue-green deployments, canary releases, and feature flags can all be formalized as CIY-preserving, risk-reducing intervention strategies. The optimal deployment strategy balances: information gained (CIY from observing the new code in production) against risk (the cost of a mismatch between expected and actual runtime behavior).

## 6. Open Questions for This Extension

1. **How much does the causal DAG differ from the dependency graph?** Empirical measurement on real codebases would answer this. If they're nearly identical, the causal machinery adds precision but not new insight. If they diverge significantly, the causal graph reveals hidden coupling that the dependency graph misses.

2. **Is causal discovery computationally tractable at codebase scale?** Standard causal discovery algorithms are O(n^2) to O(n^4) in the number of variables. For a codebase with thousands of files, this may require approximations (e.g., working at the module level rather than file level).

3. **Can counterfactual replay be automated?** If AI agents can re-implement features from specifications alone, the cost of counterfactual evaluation drops dramatically. This requires good specifications (TST's T-02) and sufficient shared context.

4. **How should the development-time causal model and the runtime causal model be integrated?** They share the codebase as a common element but have different dynamics, different observation channels, and different agents. A unified treatment would model the full lifecycle: develop → deploy → observe → learn → develop.
