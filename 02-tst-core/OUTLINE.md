# TST: Temporal Software Theory

Software development as an agentic domain — grounded in ACT's formal machinery, restored to its original status as a consequential body of research in its own right.

**Working draft.** TST re-grounds the original Temporal Software Theory in ACT's mathematical framework — adding causal mathematics, adaptive dynamics, and the persistence condition that explain *why* time-optimal development practices work, not just *that* they do. Software is not just another domain example; it has unique epistemic properties that make it the ideal testbed for ACT and, recursively, the domain where ACT-grounded agents will operate.

See [`../FORMAT.md`](../FORMAT.md) for segment file conventions. See [`../NOTATION.md`](../NOTATION.md) for symbols.

**Relationship to ACT:** TST segments reference ACT concepts by slug (e.g., `#persistence-condition`, `#adaptive-tempo`). The temporal optimality postulate — TST's foundational normative principle — is grounded by ACT's descriptive results: tempo advantage, persistence conditions, and gain dynamics explain WHY time-optimal development practices work. The dependency is one-directional: TST depends on ACT, not the reverse. `#temporal-optimality` lives in TST (where it is normatively load-bearing) and is referenced parenthetically from ACT (where the persistence condition provides the descriptive grounding).


---

## Software as Agentic Domain

*Domain instantiation: software development viewed through ACT. The developer (or AI agent) is an actuated adaptive agent whose environment is a codebase, whose observations are mediated by tools (compiler, tests, IDE), and whose actions are code changes. Software's unique epistemic properties — full observability in principle, genuine interventions via tests, counterfactual replay via version control — make it the richest operationalization domain for ACT.*

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| S | Postulate | | [#temporal-optimality](src/temporal-optimality.md) | Least-time is optimal (given equivalent outcomes) | deps-verified |
| S | Scope | | [#software-scope](src/software-scope.md) | Systems with $P(\text{change}) \gt \varepsilon$ | draft |
| S | Observation | | [#software-epistemic-properties](src/software-epistemic-properties.md) | Software's 6 unique properties | missing |
| S | Definition | | [#feature-definition](src/feature-definition.md) | Unit of coherent change | draft |
| S | Result | | [#specification-bound](src/specification-bound.md) | Can't implement unspecified; includes communication bottleneck corollary | draft |
| S | Derived | | [#change-expectation-baseline](src/change-expectation-baseline.md) | Median future ≈ observed past; includes investment scale form | draft |
| S | Definition | | [#developer-as-act-agent](src/developer-as-act-agent.md) | Developer as $(M_t, O_t, \Sigma_t)$ | missing |
| S | Definition | | [#comprehension-time](src/comprehension-time.md) | Cost of constructing local $M_t$ | draft |
| S | Definition | | [#implementation-time](src/implementation-time.md) | Cost from first change to done | draft |
| S | Derived | | [#dual-optimization](src/dual-optimization.md) | Min comprehension + impl time | draft |
| S | Derived | | [#change-investment](src/change-investment.md) | When extra time now pays off | draft |
| S | Discussion + Hypothesis | | [#code-quality-as-observation-infrastructure](src/code-quality-as-observation-infrastructure.md) | Code quality $\to U_o \to \eta^\ast \to \mathcal{T}$ | missing |
| | --GAP-- | | | Developer tempo as $\mathcal T_{\text{obs}}$ + $\mathcal T_{\text{explore}}$ + $\mathcal T_{\text{probe}}$ | |
| S | Hypothesis | | [#conceptual-alignment](src/conceptual-alignment.md) | Code-domain alignment; includes realignment corollary | draft |
| S | Definition | | [#atomic-changeset](src/atomic-changeset.md) | The diff that is the feature | draft |
| S | Empirical | | [#changeset-size-principle](src/changeset-size-principle.md) | Time ∝ changeset size; includes comprehension corollary | draft |
| S | Definition | | [#change-distance](src/change-distance.md) | Lexical < file < module < svc | draft |
| S | Derived + Hypothesis | | [#change-proximity-principle](src/change-proximity-principle.md) | Closer changes → less time | draft |
| S | Hypothesis | | [#exponential-cognitive-load](src/exponential-cognitive-load.md) | Context-switch cost compounds? | draft |
| S | Definition | | [#system-coupling](src/system-coupling.md) | $P(\text{change } j \mid \text{change } i)$ | draft |
| S | Definition | | [#system-coherence](src/system-coherence.md) | $E[\text{proximity within module}]$ | draft |
| S | Measurement | | [#coherence-coupling-measurement](src/coherence-coupling-measurement.md) | Coherence/coupling from git | draft |
| S | Derived | | [#principled-decision-integration](src/principled-decision-integration.md) | Optimal $C$ minimizes $E[T \vert C]$ | draft |
| S | Definition | | [#system-availability](src/system-availability.md) | $\text{MTTF}/(\text{MTTF}+\text{MTTR})$ | draft |
| S | Scope | | [#continuous-operation](src/continuous-operation.md) | Include $P(\text{fail}) \times T_{\text{recovery}}$ | draft |
| S | Hypothesis | | [#causal-discovery-from-git](src/causal-discovery-from-git.md) | Git as interventional data | missing |
| | --GAP-- | | | Software persistence: the unmaintainability threshold formalized | |


---

## Prior Work and Source Material

*TST has a substantial prior research corpus at `~/src/_core/tst/` (960 analyses, Obsidian vault, empirical tools). Most of this content has been absorbed. Source material lives in `src/old-tst-*` files, empirical tools in `empirical-discontinuity/`, simulations in `simulations/`, and literature review in `lit-review/`.*

### Absorbed into `src/old-tst-*`

**Earlier TST formalization** (same claims, SE-literature derivation path):
- `old-tst-software-first-principles` — The 13 original "First Principles" (FP-001–FP-013) with full discussion
- `old-tst-t01` through `old-tst-t15` — Earlier theorem statements (T-01–T-15)
- `old-tst-d01` through `old-tst-d08` — Earlier definition statements (D-01–D-08)
- `old-tst-appendix-a-version-mapping` — Mapping between FP-* and T-* numbering

**Synthesis and meta-analysis**:
- `old-tst-960-analysis-synthesis` — Synthesis of 960 SE literature analyses: validated discoveries, mathematical frameworks, speculative hypotheses
- `old-tst-comprehensive-synthesis` — Full mathematical theory of software evolution
- `old-tst-synthesis-theoretical-foundations` — Complete definitions and formal theorem statements
- `old-tst-synthesis-executive-summary` — Synthesis across 7 research domains with empirical validation
- `old-tst-meta-analysis-topology` — Topological analysis of cross-references
- `old-tst-meta-analysis-priority-rankings` — Priority-ranked findings
- `old-tst-research-findings-top-100` — Top 100 findings from the analysis corpus
- `old-tst-exemplar-analyses` — Collection of highest-quality individual analyses
- `old-tst-general-discussion` — General discussion from the theory section

**Mathematical grounding**:
- `old-tst-lindy-foundations` + `old-tst-lindy-math-foundations` — Bayesian derivation of Lindy via Jeffreys prior, maximum entropy, hazard rates → #change-expectation-baseline
- `old-tst-ai-specification-limit` — As implementation time → 0, specification quality becomes sole determinant → #software-epistemic-properties, #developer-as-act-agent
- `old-tst-proximity-coherence-for-ai` — Proximity/coherence/coupling analysis specific to AI agents
- Prior art for #specification-bound (Austin, Putnam, Shannon) is in `lit-review/` — see `specification-bound-prior-art.md`, `formal-bounds-on-implementation-speed.md`, `putnam-vs-tst-bounds.md`

**TFT bridge work** (maps TFT/ACT concepts to the software domain):
- `old-tst-via-tft-readme` — Why software is uniquely suited as ACT testbed (6 epistemic properties)
- `old-tst-via-tft-mapping` — Detailed TFT↔software domain mapping (~8,500 words)
- `old-tst-via-tft-causal-extensions` — Causal DAGs in software, Level 2/3 reasoning, counterfactual via git
- `old-tst-via-tft-reformulated-sketch` — S-00 through S-14 structured outline
- `old-tst-via-tft-simulation-proposals` — 6 concrete simulation proposals ranked by expected value

### Absorbed into directories

- **`empirical-discontinuity/`** — Git-based empirical validation toolkit for #exponential-cognitive-load. Validates $T = T_{\text{base}} \times (1+\alpha)^d$ with $\alpha \approx 0.118$ for normal development (d ≤ 25). Includes analysis scripts, methodology, findings, and visualization.
- **`simulations/`** — Stochastic Lindy Effect simulations: corrected model, Gaussian start, math verification, regime transitions, three-regime comparison, stochastic breakout. Validates survival distributions for #change-expectation-baseline.
- **`lit-review/`** — 29+ files: literature review across 7 research domains (optimal control, economic models, spectral graph theory, species-specific comprehension, stochastic processes, hybrid systems), Undermind paper reviews (10 papers), prior art for T-01, highest-cited SE works, research goals.

### Not yet absorbed (at `~/src/_core/tst/`)

- **`vault/03-library/analyses/`** — 965 structured analyses from 5 books (Pragmatic Programmer, Release It!, Programming Elixir, Designing Elixir Systems, Metaprogramming Elixir), each mapped to TST principles with mathematical formalization. These are concrete examples grounding principles in practice.
