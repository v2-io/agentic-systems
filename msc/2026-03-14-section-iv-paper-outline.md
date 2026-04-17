# Section IV Standalone Paper — Outline

**Status**: Outline only — identifies content, gaps, and omissions. Not a draft.
**Target venue**: ICSE, FSE, or arXiv cs.SE preprint
**Working title**: "Temporal Optimization in Evolving Software Systems: A Control-Theoretic Framework"

---

## Thesis

Software development decisions are implicitly dual-optimization problems: minimizing both comprehension time (understanding what exists) and implementation time (changing what exists), weighted by how many future changes are expected. This paper formalizes the tradeoff using control-theoretic tools, derives specific predictions, and proposes git-based operationalization.

## What to include (from existing AAD segments)

### 1. Introduction: The Time Problem in Software
- Software systems that expect change ($P(\text{change}) > \varepsilon$) face a fundamental tradeoff between optimizing for the current change and for all future ones
- This is not a new observation (technical debt, YAGNI, over-engineering) — but it lacks formal treatment
- **Source**: #software-scope, #temporal-optimality (simplified, without Greek terminology)

### 2. Background: Adaptive Systems Meet Software
- Brief: software development as an adaptive system (developer has a model of the codebase, updates it through observation, acts through changesets)
- The key variables: mismatch (developer understanding vs. code reality), tempo (rate of learning), gain (how much each observation teaches)
- **Source**: Stripped-down #agent-model, #mismatch-signal, #adaptive-tempo — enough to define the formal objects, not the full AAD apparatus
- **Omit**: Full Section I derivation chain, persistence condition, adversarial dynamics, the cycle phase names

### 3. Feature Time Decomposition
- Comprehension time: cost of constructing local understanding of the code to be changed
- Implementation time: cost of making the change once understanding is achieved
- The decomposition is multiplicatively different under turnover: comprehension cost is per-reader, implementation cost is per-feature
- **Source**: #comprehension-time, #implementation-time
- **Omit**: Connection to M_t sufficiency (too theoretical for SE audience)

### 4. The Change-Expectation Baseline
- Jeffreys prior on feature lifetimes → Pareto(α=1) → median future = observed past
- This is a default prior for local reasoning, not a strong theorem of software evolution
- The mean is undefined (Pareto α=1) — the median-case optimization is conservative
- Note stationarity assumption
- **Source**: #change-expectation-baseline
- **Gap**: Need to present the Pareto derivation accessibly, without assuming control theory background

### 5. The Dual Optimization
- The core result: $C^* = \arg\min_C [t_0(C) + \hat{n}_{\text{future}} \cdot (t_{\text{comp}} + t_{\text{impl}})]$
- The turnover multiplier: comprehension cost compounds per reader
- Under 100% context turnover (AI agents): comprehension cost dominates overwhelmingly
- Practical implications: explicit code, linear control flow, local comprehensibility are *temporal optimizations*, not style preferences
- **Source**: #dual-optimization
- **Gap**: Need concrete worked examples (a refactoring decision, a DRY vs. explicit decision, an abstraction decision) with quantified costs

### 6. Supporting Results
- **Change investment threshold**: when extra time now pays off (#change-investment)
- **Coherence and coupling**: measurable from git (#coherence-coupling-measurement, #system-coupling, #system-coherence)
- **Changeset size principle**: time proportional to changeset size (#changeset-size-principle)
- **Change proximity**: co-located changes are cheaper (#change-proximity-principle)
- **Conceptual alignment**: code-domain alignment reduces comprehension time (#conceptual-alignment)

### 7. Empirical Operationalization Program (IMPORTANT: frame as program, not as proven bridge)
- How git data maps to the framework's variables
- Co-change data approximates coupling
- Module structure approximates coherence
- These are *promising empirical mappings*, not secured causal bridges
- **DO NOT claim git data is "genuinely causal"** — this was flagged by all three reviewers
- **Source**: #coherence-coupling-measurement, #causal-discovery-from-git (if written by then)
- **Gap**: Need preliminary empirical results from 5-10 open-source repos

### 8. Related Work
- Technical debt metrics (SQALE, SonarQube)
- DORA metrics (deployment frequency, lead time, change failure rate, MTTR)
- Developer experience research (DX framework, cognitive load)
- Code quality literature (McCabe complexity, Halstead metrics)
- AAD's contribution: the *formal tradeoff structure* that explains why these metrics matter and how they relate

### 9. Discussion: Connection to Adaptive Agency (brief)
- This paper derives from a broader framework (AAD) that connects software engineering to control theory, causal inference, and agent composition
- The framework explains WHY temporal optimization principles work — through the persistence condition and adaptive tempo
- Pointer to positioning preprint (if available by then)

### 10. Threats to Validity
- Stationarity assumption (#change-expectation-baseline assumes uniform feature rate)
- Pareto prior — a default, not a data-fitted distribution
- Comprehension-implementation decomposition may not be clean in practice
- Git-based operationalization is analogical, not formally grounded

## What to omit from the paper

- Greek cycle terminology (Prolepsis, Aisthesis, etc.)
- Full AAD apparatus (Lyapunov stability, sector conditions)
- Adversarial dynamics
- Multi-agent composition
- Logogenic/logozoetic taxonomy
- Directed separation
- The full Section I derivation chain
- Information bottleneck / model sufficiency formalism
- Pearl's causal hierarchy

These are all essential to AAD but create barriers for the SE audience. The paper should stand on its own with the minimum formal apparatus needed for the results.

## What needs to be created for the paper

1. **Worked examples**: 3 concrete software decisions analyzed through the dual optimization lens (refactoring decision, abstraction level, DRY vs. explicit)
2. **Preliminary empirical results**: Coherence-coupling measurement from 5-10 open-source repos. Even a small study would strengthen the paper enormously.
3. **Comparison table**: Dual optimization predictions vs. DORA, SQALE, DX framework predictions — where do they agree, where do they differ?
4. **Accessible Pareto derivation**: The change-expectation baseline needs to be explained without assuming mathematical statistics background

## Estimated effort

- Outlining and restructuring existing content: 1-2 days
- Writing worked examples: 1-2 days
- Preliminary empirical study: 3-5 days (the main bottleneck)
- Writing and polishing: 3-5 days
- Total: 1-2 weeks, as the research agenda estimated

## Strategic notes

- This paper doesn't require anyone to accept AAD. It stands on temporal optimality (a postulate most developers would accept intuitively) and the cost decomposition (straightforward).
- The empirical operationalization is the weakest part. A small pilot study (even just coherence/coupling metrics from 5 repos) would dramatically improve the paper's credibility.
- The competition is thin: none of the 25 surveyed frameworks have a formal software-specific theory that produces testable quantitative predictions from first principles. The gap analysis (msc/2026-03-13-landscape-research/gap-analysis.md) confirms "code quality as observation infrastructure" has no prior art as a formal control-theoretic treatment.
