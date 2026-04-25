---
slug: hyp-causal-discovery-from-git
type: hypothesis
status: discussion-grade
depends:
  - obs-software-epistemic-properties
  - scope-developer-agent
  - def-pearl-causal-hierarchy
  - post-causal-structure
  - def-causal-information-yield
  - def-system-coupling
  - meas-coherence-coupling
stage: draft
---

# Hypothesis: Causal Discovery from Git

Git history contains interventional data: each commit is a developer intervention, and the subsequent observations (test results, production behavior, downstream commits) are outcomes. In principle, this provides Level 2 causal data for estimating AAD quantities. In practice, substantial confounding structure weakens the causal interpretation. This segment states what the data is, what it could tell us, and why the chain from git data to AAD quantities is empirical and unresolved.

## Formal Expression

### The interventional claim

*[Hypothesis (git-as-intervention)]*

Each git commit is an intervention in the sense of #def-pearl-causal-hierarchy (Level 2):

$$\text{commit } c = do(\text{change files } \{f_1, \ldots, f_m\})$$

The developer chose to modify specific files and observed the consequences (compiler output, test results, production behavior, subsequent development effort). The temporal ordering ( #post-causal-structure) identifies the *structure of possible influence*, narrowing the candidate set of actual causal directions: if commit $c_1$ precedes commit $c_2$, and $c_2$ touches files that $c_1$ also touched, then $c_1$ is in $c_2$'s causal past in the structure-of-possible-influence sense — actual causal influence remains an empirical question subject to the confounding structure (C1–C3) discussed below.

The outcome of interest for TST is the downstream cost: which other files required subsequent changes, how much time elapsed before the next modification of the affected region, whether tests failed, whether incidents occurred. In AAD terms, the commit is an action $a_t$ and the downstream costs are observations $o_{t+1}, o_{t+2}, \ldots$ that carry information about the causal structure of the codebase.

### The causal coupling estimate

*[Hypothesis (causal-coupling-from-git)]*

The causal coupling between modules — the interventional probability $P(\text{change}(B) \mid do(\text{change}(A)))$ — is the quantity that #def-system-coupling approximates with the associational $P(\text{change}(B) \mid \text{change}(A))$. Given sufficient history, the interventional quantity could in principle be estimated from git data by adjustment:

$$P(\text{change}(B) \mid do(\text{change}(A))) = \sum_C P(\text{change}(B) \mid \text{change}(A), C) \cdot P(C)$$

where $C$ is the set of confounders (common causes such as shared requirements). The associational and causal quantities coincide when there are no common causes — when every co-change of $A$ and $B$ is because $A$ causally necessitated $B$'s change. They diverge when common causes are present, which is the typical case.

### The confounding structure

*[Discussion (git-confounding)]*

Three classes of confounders weaken the interventional interpretation:

**C1. Shared requirements.** A new feature requirement may drive changes to modules $A$ and $B$ independently. The requirement is a common cause, not a causal link from $A$ to $B$. Partially identifiable when requirements are tracked (linked issues, PR descriptions), but requirement tracking is inconsistent across projects and the link between a requirement and its code footprint is often approximate.

**C2. Convention-driven bundling.** Developers group related changes into single commits for organizational reasons (clean git history, atomic deployments), not because the changes are causally linked. A commit touching files $A$, $B$, and $C$ does not imply a causal chain $A \to B \to C$ — it may reflect a convention of bundling logically related but causally independent changes.

**C3. Developer knowledge state.** An experienced developer may change $A$ and $B$ together because they *know* (from their $M_t$) that both need updating, not because changing $A$ caused them to discover the need to change $B$. The co-change reflects the developer's causal model, not a causal process observed in the data. This is a selection effect: the developer's choice of what to include in a commit is conditioned on their private causal model, which is unobserved.

### What remains after accounting for confounding

*[Hypothesis (residual-causal-signal)]*

Even with confounding, git history provides a genuine causal signal that goes beyond what the static dependency graph offers:

1. **Temporal ordering is always available.** Regardless of confounding, the direction of potential influence is known from timestamps. Causal discovery algorithms can use this as a constraint, eliminating half the possible edge orientations.

2. **The dependency graph provides a structural prior.** The declared dependency graph (imports, API contracts, type dependencies) constrains the set of plausible causal edges. Historical co-change data that deviates from the dependency graph reveals either (a) undeclared coupling (hidden causal links) or (b) confounding. The divergence points are diagnostic: either the architecture is incomplete (architectural improvement opportunity) or the co-change is spurious (confounder-driven).

3. **Frequency asymmetries carry causal information.** If changes to $A$ are frequently followed by changes to $B$, but changes to $B$ are rarely followed by changes to $A$, this asymmetry is evidence of a directed causal link $A \to B$ that survives common-cause confounding (since common causes would produce symmetric co-change).

4. **Intervention contrast exists but is noisy.** Different commits change different subsets of files. Commits that change $A$ without $B$ vs. commits that change $A$ with $B$, conditioned on available confounders, provide weak but nonzero interventional contrasts.

## Epistemic Status

This is a *hypothesis* — a research program, not a derivation. The status is *discussion-grade* because:

1. The claim that commits are interventions (the interventional claim) is structurally sound: developers do perform genuine causal interventions on codebases, and git does record the intervention-outcome pairs. This is not in dispute.

2. The claim that the interventional data is *usable* for estimating causal structure is the substantive hypothesis, and it faces serious obstacles. The three confounding classes (C1–C3) are not merely theoretical concerns — they are the *typical* case. Most git commits are confounded by shared requirements, convention-driven bundling, or developer knowledge state. The unconfounded signal is a residual, not the primary content.

3. The chain from git data to AAD quantities ($\rho$, coupling strength, $U_o$) is entirely empirical. No formal result in AAD establishes that git-derived causal estimates converge to the true AAD parameters. The connection is analogical: if we *could* correctly estimate causal coupling from git, it would correspond to AAD's coupling quantities. But the "if" is doing all the work.

Max attainable: *empirical*. Even with perfect confounding adjustment and unlimited data, the claim that git-derived causal structure matches AAD's formal quantities would remain an empirical finding, not a derivation. The theory does not entail this correspondence — the domain does.

## Discussion

**What the static dependency graph already provides.** Import graphs, type dependencies, and API contracts already declare a partial causal DAG for change propagation ( #obs-software-epistemic-properties, P4). A change to module $B$'s interface may require changes to module $A$ (because $A$ depends on $B$), but not vice versa (unless there are cycles). This declared structure is available without any historical analysis and is not subject to the confounding problems of git history. The question for causal discovery from git is: how much does the *historical* causal structure diverge from the *declared* structure, and is the divergence informative?

**Where git history adds value over the dependency graph.** Two cases:

1. *Undeclared coupling.* Files that empirically co-change often but have no declared dependency share implicit contracts — shared assumptions, copy-paste coupling, or convention dependencies. These are causal links the architecture fails to capture. Identifying them is architecturally valuable regardless of whether the causal estimates are precise.

2. *Inert declared coupling.* Files that are declared-dependent but rarely co-change have stable interfaces that absorb changes. The declared coupling overstates the actual causal link strength. Knowing this is useful for change-impact prediction.

**Computational tractability.** Standard causal discovery algorithms (PC, GES, constraint-based methods) are $O(n^2)$ to $O(n^4)$ in the number of variables. For a codebase with thousands of files, this requires approximation — working at the module or package level rather than file level. The dependency graph provides a sparsity prior that may make discovery tractable for larger systems.

**The research program.** A productive approach would be:

1. Select codebases with rich git history and good requirement tracking (to partially adjust for C1).
2. Estimate both the associational co-change matrix ( #meas-coherence-coupling) and the dependency graph.
3. Apply causal discovery algorithms with temporal ordering and dependency-graph constraints.
4. Compare the resulting causal graph to the dependency graph, identifying divergence points.
5. Validate: do the divergence points predict future co-change better than either source alone?

This is an empirical research program. Its outcome would strengthen or weaken the hypothesis, but the hypothesis is not currently testable from within the theory.

**Connection to TST's measurement segment.** #meas-coherence-coupling already defines operational measures of coupling and coherence from git data, using co-change frequency as the observable. The present segment asks: is the co-change frequency a causal measure or merely an associational one? If the confounding is manageable, the existing measurements approximate causal coupling. If confounding dominates, the measurements are useful descriptive statistics but do not support causal claims about change propagation.

**The changeset-as-downstream result.** If the causal graph were correctly estimated, the expected changeset size for a feature would be $\lvert\text{downstream}(\text{intervention}(F), \text{DAG})\rvert$ — the number of nodes causally downstream of the initial intervention. This connects #emp-changeset-size-principle to causal graph structure: good architecture minimizes the expected downstream set for typical interventions. But this reframing depends entirely on having the causal graph, which is the hypothesis under discussion.

## Working Notes

- The strongest version of this hypothesis would be: given a causal discovery algorithm with appropriate confounding adjustment, the estimated causal graph predicts future change propagation better than the declared dependency graph alone. This is a concrete, testable claim. The weaker version is: git history provides *some* causal information beyond the dependency graph. The weaker version is almost certainly true but not very interesting.
- C3 (developer knowledge state) is the most challenging confounder because it is fundamentally unobservable from git data alone. The developer's $M_t$ determines what they include in a commit, and $M_t$ is not recorded. AI agents with explicit reasoning traces might partially address this — the agent's planning log could serve as a partial record of $M_t$ at commit time.
- The frequency-asymmetry observation (point 3 under "What remains") is the most promising causal identification strategy, because it survives common-cause confounding. It is related to Granger causality (temporal precedence + predictive power), which has known limitations but at least provides a falsifiable test.
- The connection between this segment and #scope-edge-update-causal-validity in AAD is worth noting: AAD's strategy-edge updates face the same observational-vs-interventional tension. The resolution there (regime-indexed interpretation with A/B/C classification) may be informative for the git case — different commits may fall into different causal-identification regimes.

*(Source: old-tst-via-tft-causal-extensions.md, "Causal Discovery from Git History," "Interventional Reasoning," "Causal Inference for Change Prediction.")*
