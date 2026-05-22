# *Volume* TST: Temporal Software Theory
## *Preface*

Software development as an agentic domain — grounded in AAT's formal machinery, restored to its original status as a consequential body of research in its own right.

**Working draft.** TST re-grounds the original Temporal Software Theory in AAT's mathematical framework — adding causal mathematics, adaptive dynamics, and the persistence condition that explain *why* time-optimal development practices work, not just *that* they do.

**Software as AAT's calibration laboratory.** Software serves as the *privileged high-identifiability calibration laboratory* for AAT, not a generic "best operationalization domain." Its role is specifically architectural: it is the domain in which AAT's quantitative machinery can be most cleanly grounded — where edge interventions can sometimes be literally interventional (tests, deploys, `git bisect`), where the chronica is partially exteriorized with exact cryptographic immutability over its committed subset ( #obs-software-epistemic-properties P5), where the causal DAG is partially declared rather than inferred (P4), and where the observation function itself is under agent control (P1/P6). Other domains instantiate AAT under *additional transfer assumptions* that must be stated explicitly — approximation of interventional access, sampled rather than exteriorized chronica, inferred rather than declared causal structure. The calibration-lab framing makes these transfer assumptions first-class rather than implicit and prevents unacknowledged overclaim when AAT machinery calibrated in software is used in other domains.

See [`../FORMAT.md`](../FORMAT.md) for segment file conventions. See [`../NOTATION.md`](../NOTATION.md) for symbols.

**Relationship to AAT:** TST segments reference AAT concepts by slug (e.g., `#result-persistence-condition`, `#def-adaptive-tempo`). The temporal optimality postulate — TST's foundational normative principle — is grounded by AAT's descriptive results: tempo advantage, persistence conditions, and gain dynamics explain WHY time-optimal development practices work. The dependency is one-directional: TST depends on AAT, not the reverse. `#post-temporal-optimality` lives in TST (where it is normatively load-bearing) and is referenced parenthetically from AAT (where the persistence condition provides the descriptive grounding).


---

## *Part* Software as Agentic Domain

### *Preface*

*Domain instantiation: software development viewed through AAT. The developer (or AI agent) is an actuated adaptive agent whose environment is a codebase, whose observations are mediated by tools (compiler, tests, IDE), and whose actions are code changes. Software's distinctive epistemic properties — codebase inspectability, genuine test-based interventions, counterfactual replay via version control, exact cryptographic recording of committed-state transitions — establish it as AAT's privileged high-identifiability calibration laboratory (see preamble). Other domains inherit AAT's machinery under additional transfer assumptions rather than by direct equivalence.*

### *Chapter* Foundations and Features

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| S | Postulate | | [#post-temporal-optimality](src/post-temporal-optimality.md) | Least-time is optimal (given equivalent outcomes) | deps-verified |
| S | Scope | | [#scope-evolving-software](src/scope-evolving-software.md) | Systems with $P(\text{change}) \gt \varepsilon$ | draft |
| S | Observation | | [#obs-software-epistemic-properties](src/obs-software-epistemic-properties.md) | Software's 6 unique properties | draft |
| S | Definition | | [#def-feature](src/def-feature.md) | Unit of coherent change | draft |
| S | Result | | [#result-specification-bound](src/result-specification-bound.md) | Can't implement unspecified; includes communication bottleneck corollary | draft |
| S | Derived | | [#der-change-expectation-baseline](src/der-change-expectation-baseline.md) | Median future ≈ observed past; includes investment scale form | draft |
| S | Discussion | | [#impl-foundations-features](src/impl-foundations-features.md) | Chapter additional implications & discussion: software as calibration laboratory (#12), specification bound as persistence-bandwidth at spec layer (#32), temporal optimality grounding (#53), domain-generalization transfer theorem candidate (#41) | draft |

<!--
Internal arc: the normative postulate (temporal optimality) sets TST's
optimization target; the scope condition narrows to evolving systems where
the lifecycle sum dominates initial cost; the epistemic-properties segment
positions software as AAT's calibration laboratory via the six properties
P1–P6, with the calibration-lab framing as the load-bearing TST commitment
that disciplines transfer to other domains. The unit of analysis is the
feature; the specification-bound and change-expectation segments give two
upstream quantities — minimum-communication time and median future feature
count $\hat n_{\text{future}}$ — that downstream chapters use as inputs to
the dual optimization.
-->

### *Chapter* The Developer Agent and Time Decomposition

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| S | Discussion | | --GAP-- | | missing |
| S | Definition | | [#scope-developer-agent](src/scope-developer-agent.md) | Developer as $(M_t, O_t, \Sigma_t)$ | draft |
| S | Definition | | [#def-comprehension-time](src/def-comprehension-time.md) | Cost of constructing local $M_t$ | draft |
| S | Definition | | [#def-implementation-time](src/def-implementation-time.md) | Cost from first change to done | draft |
| S | Derived | | [#der-dual-optimization](src/der-dual-optimization.md) | Min comprehension + impl time | draft |
| S | Derived | | [#der-change-investment](src/der-change-investment.md) | When extra time now pays off | draft |
| S | Discussion + Hypothesis | | [#der-code-quality-as-observation-infrastructure](src/der-code-quality-as-observation-infrastructure.md) | Code quality $\to U_o \to \eta^\ast \to \mathcal{T}$ | draft |
| S | Definition | | --GAP-- (candidate: `#def-developer-tempo-channels`) | Developer tempo as $\mathcal T_{\text{obs}}$ + $\mathcal T_{\text{explore}}$ + $\mathcal T_{\text{probe}}$ — chronicle-derivable channel separation + probe-class typology + matrix-Loewner weakest-channel bottleneck (see [`TST-IDEAS.md`](../TST-IDEAS.md) §A4) | missing |
| S | Discussion | | [#impl-developer-agent](src/impl-developer-agent.md) | Chapter additional implications & discussion: AI-maintained-code regime as normal-case for comprehension dominance (#16), persistence-threshold bifurcation from $Q \to U_o \to \eta^\ast \to \mathcal T$ chain (#17), multi-channel developer tempo decomposition | draft |

<!--
Instantiates AAT's actuated-agent machinery in software. Internal arc: the
developer-agent scope segment maps $\Omega_t$, $M_t$, $O_t$, $\Sigma_t$,
observation channels, and action classes onto the developer's environment;
comprehension and implementation times partition feature time; dual-
optimization derives the trade-off across the (typically much larger)
turnover-multiplier-weighted future; change-investment is the pairwise
decision rule; code-quality-as-observation-infrastructure closes the chain
$Q \to U_o \to \eta^\ast \to \mathcal T \to$ persistence, giving "this
codebase is unmaintainable" a formal inequality. The trailing GAP
(developer tempo decomposition into obs / explore / probe) names the
natural next-segment slot pairing with AAT's `#def-adaptive-tempo`
channel machinery.
-->

### *Chapter* Code Structure and Implementation Cost

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| S | Discussion | | --GAP-- | | missing |
| S | Hypothesis | | [#hyp-conceptual-alignment](src/hyp-conceptual-alignment.md) | Code-domain alignment; includes realignment corollary | draft |
| S | Definition | | [#def-atomic-changeset](src/def-atomic-changeset.md) | The diff that is the feature | draft |
| S | Empirical | | [#emp-changeset-size-principle](src/emp-changeset-size-principle.md) | Time ∝ changeset size; includes comprehension corollary | draft |
| S | Definition | | [#def-discontinuity-distance](src/def-discontinuity-distance.md) | Lexical < file < module < svc | draft |
| S | Derived + Hypothesis | | [#der-change-proximity-principle](src/der-change-proximity-principle.md) | Closer changes → less time | draft |
| S | Hypothesis | | [#hyp-exponential-cognitive-load](src/hyp-exponential-cognitive-load.md) | Context-switch cost compounds? | draft |
| S | Discussion | | [#impl-code-structure](src/impl-code-structure.md) | Chapter additional implications & discussion: joint structural-mechanics composition (alignment + size + proximity + discontinuity) as operational substrate for Ch.2's dual-optimization, exponential cognitive load with structure-dependent refinement (#48), atomic changeset as Pearl-Level-2 interventional substrate, chain-confidence-decay anchor at the depth-fragility level | draft |

<!--
Structural mechanics of code that govern implementation cost. Internal arc:
conceptual-alignment is the upstream determinant (code structure matching
the domain model reduces comprehension time); atomic-changeset is the
observable trace of an implementation decision; size-principle gives the
first-order proportionality between changeset size and implementation time;
discontinuity-distance hierarchy and proximity-principle add the structural-
correction term (scattered changes are harder than concentrated ones at
constant size); exponential-cognitive-load is the candidate multiplicative
form not yet derived — qualitative effect robust, quantitative form open.
The chapter pairs with Ch.2: that chapter develops the time *decomposition*;
this chapter develops the structural *mechanics* that determine the times.
-->

### *Chapter* System Measures, Operation, and Causal Substrate

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| S | Discussion | | --GAP-- | | missing |
| S | Definition | | [#def-system-coupling](src/def-system-coupling.md) | $P(\text{change } j \mid \text{change } i)$ | draft |
| S | Definition | | [#def-system-coherence](src/def-system-coherence.md) | $E[\text{proximity within module}]$ | draft |
| S | Measurement | | [#meas-coherence-coupling](src/meas-coherence-coupling.md) | Coherence/coupling from git | draft |
| S | Derived | | [#der-principled-decision-integration](src/der-principled-decision-integration.md) | Optimal $C$ minimizes $E[T \vert C]$ | draft |
| S | Definition | | [#def-system-availability](src/def-system-availability.md) | $\text{MTTF}/(\text{MTTF}+\text{MTTR})$ | draft |
| S | Scope | | [#scope-continuous-operation](src/scope-continuous-operation.md) | Include $P(\text{fail}) \times T_{\text{recovery}}$ | draft |
| S | Hypothesis | | [#hyp-causal-discovery-from-git](src/hyp-causal-discovery-from-git.md) | Git as interventional data | draft |
| S | Hypothesis | | --GAP-- (candidate: `#hyp-software-unmaintainability-bifurcation`) | Software persistence: the unmaintainability threshold formalized as a bifurcation in $Q \to U_o \to \eta^\ast \to \mathcal T$ chain — G1/G2/G3 code-age bimodality with Ebbinghaus $\tau \approx 20$ days as $U_o$-decay anchor (see [`TST-IDEAS.md`](../TST-IDEAS.md) §A3) | missing |
| S | Discussion | | [#impl-system-measures](src/impl-system-measures.md) | Chapter additional implications & discussion: coupling/coherence as system-level diagnostic infrastructure, OKR-as-observability-engineering generalization across multi-agent systems (#42), interventional vs associational reading of git (#49), operational availability as persistence-bandwidth-floor analog, domain-generalization transfer theorem candidate (#41), TST volume closes here | draft |

<!--
System-level synthesis plus operational and meta-level extensions. Internal
arc: coupling and coherence are the system-wide aggregate measures (inter-
module and intra-module structure as conditional probabilities and expected
proximities); the coherence-coupling measurement is the operational
quantity computable from git; principled-decision-integration is the full
optimization that integrates Ch.2's time decomposition with Ch.3's
structural mechanics under the feature-intensity profile $\lambda(F_i)$,
sitting here as the synthesis bridge between feature-level mechanics and
system-level measures; system-availability and continuous-operation extend
the optimization target to operational time (downtime is part of the
feature-delivery cost from the user's perspective); causal-discovery-from-
git names the meta-question of how interventional the git-derived
substrate actually is, with three confounder classes (shared requirements,
convention-driven bundling, developer knowledge state) constraining the
causal interpretation of the segments above. The trailing software-
persistence GAP is the natural next-segment slot — the unmaintainability
threshold formalized at the codebase scale, pairing with the code-quality-
to-persistence chain from Ch.2 lifted from the developer-channel level to
the system level.

Placement tension worth flagging: `der-principled-decision-integration`
draws on segments from Chapters 2 (dual-optimization) and 3 (alignment,
changeset, proximity) more than from Chapter 4's own coupling/coherence
measures. It could equally close Ch.3 as the synthesis of feature-level
mechanics; placement in Ch.4 follows the existing OUTLINE ordering and
reads the integration as the bridge from feature-level mechanics to
system-level optimization, where estimating the feature-intensity profile
$\lambda(F_i)$ benefits from the aggregate system knowledge developed in
the coupling/coherence segments.
-->


