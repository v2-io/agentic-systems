# ACT: Agentic Cycle Theory — Contents

**Working draft.** This is a best-effort outline of the theory's current shape
— a map of what we think we know and where the gaps are. The ordering,
grouping, and even which claims exist will evolve as the theory develops.
Claims will fill in from both directions: general theory pushing toward domain
instantiation, and domain-specific results pushing requirements back up. Treat
this as a living proof sketch, not a specification.

A first-principles theory of adaptive, purposeful agents under uncertainty.

## How to Read This

Each entry has: **number · slug** — Type — Status, then a one-sentence summary.

**Claim types** (following TFT conventions from TF-00):
- **Axiom**: Tautological or foundational — cannot be derived, only accepted
- **Definition**: Introduces a quantity, object, or notation
- **Scope**: Restricts or broadens the domain under discussion
- **Formulation**: Representational or modeling choice (could be different)
- **Derived**: Logical consequence of prior claims under stated assumptions
- **Theorem**: Formally stated and proved (or proof-sketched)
- **Corollary**: Follows directly from a theorem
- **Hypothesis**: Structurally motivated, needs validation
- **Empirical**: Generalization supported by data, not fully derived
- **Observation**: Finding from simulation or empirical investigation
- **Discussion**: Conceptual or normative claim used for interpretation
- **Measurement**: Operationalization of a theoretical quantity
- **Gap**: Known missing step — we know something belongs here

**Epistemic tiers** (combining TFT's claim registry with TST's precision):
- **First-principled**: Axiomatic or tautological — cannot be derived, only accepted
- **Exact**: Mathematically validated under stated assumptions
- **Robust qualitative**: Survives across assumptions; specific form approximate
- **Heuristic**: Useful approximation; quantitative form may not hold
- **Conditional**: Depends on explicitly named local assumptions
- **Empirical**: Supported by data or simulation, not fully derived
- **Discussion-grade**: Argued qualitatively or by analogy, not derived
- **Sketch**: Direction identified but formalization incomplete
- **Gap**: Placeholder — we know the step is needed

Epistemic tiers appear in each segment file's **Epistemic Status** paragraph,
not in this contents listing. This listing shows only the claim **type**. When
a type label includes a qualifier (e.g., "Hypothesis," "Empirical," "Derived +
Discussion"), that is a signal about the claim's epistemic character. Absence
of qualifier on a Definition, Axiom, or Scope entry is normal — these are
definitional, not truth-claims.

**References** use `#slug-name` tags. Dependencies are mostly sequential;
explicit only when reaching back to non-adjacent claims.

**Numbering** by 10s to allow insertion. The slugs in YAML frontmatter are the
stable cross-references — numbers may be renormalized as the structure settles.

---

## I. Adaptive Systems Under Uncertainty

*Scope: Any system consisting of an agent coupled to an environment through
observation and action channels, where the environment is not fully observable.
This is the general case — thermostats through commanders. The claims in this
section are largely drawn from TFT (TF-01 through TF-11, Appendix A), which
developed the adaptive-systems foundation that ACT subsumes.*

**010 · temporal-optimality** — Axiom
Among agents achieving identical outcomes across all non-temporal dimensions,
the one requiring least time is optimal. *(Generalizes TST T-01 beyond
software.)*

**020 · agent-environment** — Definition
An agent receives observations from an environment, maintains internal state,
and produces actions that affect the environment. The agent cannot access the
environment directly — observations are necessarily lossy. This is constitutive:
the theory applies where the agent-environment boundary entails information
loss. *(From TF-01.)*

**030 · observation-function** — Definition
Observations are lossy, possibly noisy functions of environment state:
o_t = h(Ω_t, a_{t-1}, ε_t). The agent knows neither h nor the noise
distribution exactly. *(From TF-01.)*

**040 · action-transition** — Definition
Actions affect environment: Ω_{t+1} ~ T(· | Ω_t, a_t). The transition function
T is unknown to the agent and possibly stochastic. *(From TF-01.)*

**050 · scope-condition** — Scope
ACT applies where: observations exist, the agent has at least binary choice
(|A| ≥ 2, the minimum for interventional contrast and causal learning), and
residual uncertainty persists: H(Ω_t | C_t) > 0. *(From TF-01.)*

**060 · causal-structure** — Axiom
The agent-environment interaction has irreducible causal structure. Temporal
ordering is constitutive, not incidental. The interaction creates a causal DAG
from which associations, interventions, and counterfactuals derive.
*(From TF-02, grounded in Pearl.)*

**070 · pearl-causal-hierarchy** — Definition
Three levels of causal reasoning: Level 1 (association — "what if I observe?"),
Level 2 (intervention — "what if I do?"), Level 3 (counterfactual — "what if I
had done differently?"). The binary action requirement (#scope-condition)
ensures Level 2 access. *(From TF-02.)*

**080 · chronica** — Definition
The interaction history C_t = (o_1, a_1, ..., o_t) is the complete record of
agent-environment interaction. All the agent can ever know derives from this
sequence. *(From TF-02.)*

**090 · agent-model** — Definition
M_t = φ(C_t): the agent's compressed representation of how the world works,
mapping interaction history to model space M. This is a formulation choice — we
commit to analyzing the agent as having a complete state M_t that subsumes all
retained information from its history. *(From TF-03.)*

**100 · information-bottleneck** — Formulation
Optimal model compression balances retained history against predictive power:
φ* = argmin[I(M_t; C_t) − β·I(M_t; o_{t+1:∞} | a_{t:∞})]. The trade-off β
depends on environment volatility ρ: volatile → aggressive compression (low β);
stable → dense retention (high β). *(From TF-03.)*

**110 · model-sufficiency** — Definition
S(M_t) measures what fraction of predictive information the model retains
relative to the full history. S = 1 means M_t is a sufficient statistic.
S < 1 means predictive information has been lost. *(From TF-03/TF-10.)*

**115 · model-class-fitness** — Definition
F(M) = sup_{M ∈ M} S(M). When F(M) < 1 − ε, no model in the current class can
adequately represent reality, regardless of parameter tuning. This is the
trigger for structural change (#structural-adaptation-necessity). *(From TF-10.)*

**120 · event-driven-dynamics** — Formulation
The primary formulation is event-driven: observations and actions occur as
events in continuous time at potentially different and variable rates.
Discrete-time notation is the special case of uniform-interval events on a
single channel. *(From TF-04.)*

**130 · recursive-update** — Derived
Agent state updates must be recursive: M_{τ+} = f_M(M_{τ−}, e_τ). Between
events, the model evolves autonomously: dM/dτ = g_M(M_τ). The agent cannot
re-derive M_t from scratch at each event — this is computational necessity for
finite agents, and architectural choice for others. *(From TF-04.)*

**140 · mismatch-signal** — Definition
δ_t = o_t − ô_t: the discrepancy between observation and prediction. This is
the fundamental error signal that drives all adaptation. Zero mismatch can mean
accurate model, confirmation bias, or high observation noise masking
miscomprehension. *(From TF-05.)*

**150 · mismatch-decomposition** — Theorem
E[||δ||²] = E[||model_error||²] + E[||obs_noise||²]. Mismatch decomposes into
reducible model error (improvable by learning) and irreducible observation noise
(a property of the channel). This is Prop 5.1, proven. *(From TF-05.)*

**160 · update-gain** — Empirical Claim
η* = U_M / (U_M + U_o): the optimal update weight balances model uncertainty
against observation uncertainty. High model uncertainty → trust observations.
Low model uncertainty → trust the model. Riccati-optimal gain validated
empirically with 52% mismatch reduction. *(From TF-06.)*

**170 · adaptive-tempo** — Definition
T = Σ ν^(k) · η*^(k): adaptive tempo is the sum across observation channels of
event rate × gain. This measures the agent's total rate of useful information
acquisition. *(From TF-06/TF-08.)*

**180 · persistence-condition** — Theorem
The agent maintains bounded mismatch (persists) iff T > ρ / ||δ_critical||,
where ρ is the rate of environment change and δ_critical is the maximum
tolerable mismatch. Robust across all correction functions tested.
*(From TF-07, Appendix A.)*

**190 · sector-condition-stability** — Theorem
The general nonlinear persistence result: the correction function g(δ) must
satisfy sector bounds [α, β] with α > ρ/T. This is the Lyapunov/sector-
condition framework — more general than the linear ODE, handles arbitrary
nonlinear correction functions. The linear ODE is a pedagogical special case.
*(From Appendix A, promoted to primary.)*

**200 · structural-adaptation-necessity** — Theorem
When model class fitness F(M) < 1 − ε, no parametric update closes the mismatch
floor. The agent must change its model class (structural adaptation), not just
its parameters. Catastrophic breakdown observed at predicted threshold.
Prop 10.1, proven. *(From TF-10.)*

---

## II. Purposeful Adaptive Systems

*Scope narrowing: agents that not only track reality but aim at something. This
adds objectives and strategy alongside the reality model. The adaptive machinery
from Section I carries over unchanged (#directed-separation) — what we add is
the goal-directed layer. "If a man knows not to which port he sails, no wind is
favorable." — Seneca*

**210 · agent-spectrum** — Definition
Two independent dimensions create an agent spectrum: {±model} × {±objective}.
Four quadrants: reactive system (thermostat), adaptive tracker (Kalman filter),
blind pursuer (PID controller), purposeful agent (commander, developer, AI
agent). These are regions of a continuum, not discrete categories. *(From
ACT-01.)*

**220 · objective** — Definition
O_t ∈ S or O_t ⊆ S: what the agent wants — a target state, region, or condition
in environment state space. The port, the destination, the desired end-state.
O_t specifies *what*, not *how*. *(From ACT-03.)*

**230 · strategy-dag** — Definition
Σ_t = (V, E, p, γ): a probabilistic causal DAG encoding the agent's theory of
how its actions produce goal-achievement. Nodes are propositions; edges carry
causal confidence weights p ∈ [0,1]; combination rules γ(v) ∈ {AND, OR}
determine how parent evidence combines. *(From intent-dag-consolidated.
Converged across three independent formalisms.)*

**240 · and-or-semantics** — Definition
AND nodes: all parents required — P(v) = Π p_ij. OR nodes: any parent
sufficient — P(v) = 1 − Π(1 − p_ij). The noisy-OR-everywhere assumption
(first formalism attempt) was rejected: it systematically overestimates
conjunctive structures. *(From track-a/03-alt-and-or-dag.)*

**250 · directed-separation** — Theorem
M_t dynamics are independent of O_t and Σ_t. O_t is independent of M_t
(though may be revised based on it). Σ_t depends on both M_t and O_t. Action
selection couples all three. The adaptive-systems layer (Section I) is valid on
its own; the purposeful layer requires it. *(From ACT-03, derived from causal
structure.)*

**260 · compound-probability-decay** — Theorem
Path confidence through n sequential AND-edges decays as p^n. Five steps at
p = 0.9 each: path confidence 0.59. Ten steps: 0.35. Deep strategies are
exponentially fragile. Mathematical necessity. *(From intent-dag-consolidated.)*

**270 · observability-dominance** — Derived
Unobservable edges freeze beliefs — the agent cannot update confidence on what
it cannot see. Strategy effectiveness is gated by which edges the agent can
observe. Observability enables strategy; its absence disables it, regardless of
the strategy's structural quality. *(From intent-dag-consolidated.)*

**280 · orient-cascade** — Derived
The update ordering when new information arrives: observation → M_t update
(#recursive-update) → Σ_t edge revision → feasibility check → possible O_t
revision. Timescale separation: ν_M ≫ ν_Σ ≫ ν_O. The reality model updates
fastest; objectives change most rarely. *(From ACT-03/intent-dag-consolidated.)*

**290 · edge-update-via-gain** — Hypothesis
Strategy edges update via the same uncertainty ratio principle: η_edge =
U_edge / (U_edge + U_obs). TFT's gain machinery (#update-gain) extends to
strategy revision. *Parallel to M_t gain but not independently validated.*
*(From intent-dag-consolidated.)*

**300 · structural-change-as-parametric-limit** — Formulation
In the probabilistic DAG, pruning (edge → 0) and grafting (0 → edge) are
continuous operations on edge weights, not discrete structural events. TF-10's
destruction-creation cycle is the rare limiting case. *(From intent-dag-
consolidated, converged.)*

**310 · three-mismatch-types** — Definition (sketch)
δ_epistemic: reality model error (Section I's mismatch, carries over).
δ_objective: gap between current state and O_t.
δ_strategic: strategy's predicted outcomes vs actual progress.
*δ_strategic is the least crisp — it's a second-order inference ("trying hard
with good model, gap not closing → strategy may be wrong"). Possible
formalization: likelihood ratio on critical-path confidence vs observed
progress.* *(From founding notes.)*

**315 · ???** — Gap
*How do the three mismatch types interact? When δ_epistemic is high, can we
even measure δ_strategic? Is there a dominance ordering? This likely connects
to the orient cascade (#orient-cascade) — you must resolve δ_epistemic before
δ_strategic is meaningful.*

**320 · ???** — Gap
*Action-deliberation-exploration tradeoff. Three-way: exploit (pursue O_t via
Σ_t), explore (improve M_t), deliberate (revise Σ_t). How does the agent
allocate across these? TF-07/08/09 treat the explore/exploit case for M_t;
adding Σ_t creates a richer tradeoff. Connects to CIY (TF-09) and gain.*

**330 · ???** — Gap
*Strategy tempo. What is the analog of adaptive tempo (#adaptive-tempo) for
Σ_t updates? T_Σ = Σ channels contributing to strategy revision? This matters
for strategy persistence — you need to revise strategy fast enough to keep up
with changing feasibility.*

**340 · strategy-persistence** — Hypothesis (sketch)
Σ_t persists iff T_Σ > ρ_Σ / ||δ_Σ_critical||. Strategy faces its own
persistence condition, analogous to the model's (#persistence-condition).
A strategy that can't adapt to changing conditions faster than conditions change
becomes incoherent. *(Structural parallel, not independently motivated.)*

**345 · ???** — Gap
*Cognitive cost of Σ_t. TF-03 has β for M_t compression cost
(#information-bottleneck). The intent DAG has no analog. A 500-node strategy
DAG is qualitatively different from a 12-node one, even at identical path
confidences. For finite-context agents, the DAG must fit in working memory.
Connects to IB-compressed shared intent (#shared-intent).*

**350 · ???** — Gap
*Edge semantics and identifiability. Edges claim interventional semantics
(p_ij = P(j | do(i), M_t)) but update from observational signals without
identifiability assumptions. In confounded domains (military, organizational),
this is a real causal-identification problem. In software, genuine interventions
(tests, deploys, git bisect) are available, so the gap is less severe there.
Resolution may come from the software domain pushing requirements back up.*

---

## III. Coordinated and Adversarial Systems

*Scope broadening: multiple agents interacting through a shared environment.
Correlated observations as default; independence as special case. This is where
shared intent, adversarial dynamics, and tempo advantage become load-bearing.*

**400 · multi-agent-scope** — Scope
Multiple agents interact through shared environment. Observations may be
correlated (the default; independence is the special case requiring
justification). Each agent has its own (M_t, O_t, Σ_t) triple. Agents may be
cooperative, adversarial, or mixed. *(From TF-11/Appendix F, with correlation
fix.)*

**410 · shared-intent** — Definition + Discussion (sketch)

IB-compressed purpose communicated between agents for coordinated action. The
Auftragstaktik insight: communicate *enough* intent to enable local adaptation,
not so much that you constrain it. The information bottleneck principle
(#information-bottleneck) applied to inter-agent purpose rather than
intra-agent compression. *(From intent-dag-consolidated.)*

**415 · ???** — Gap
*Intent decomposition. How does a commander's Σ_t decompose across
subordinates? Graph partitioning minimizing inter-agent edge uncertainty. What
can a subordinate do locally vs what requires coordination? This is where
Auftragstaktik gets formalized.* *(From track-a/04.)*

**420 · ???** — Gap
*Directed opportunism bounds. How much can a subordinate's local Σ_t diverge
from the shared intent without breaking team coherence? There must be a
KL-divergence-like measure of intent alignment.* *(From track-a/04.)*

**430 · adversarial-tempo-advantage** — Theorem
Tempo advantage is superlinear: the ratio of adversarial mismatch scales as
(T_A/T_B)^α where α > 1 in all coupling-dominant regimes. Faster adaptation
doesn't just help linearly — it compounds. This is the formal grounding of
Boyd's OODA loop insight. *(From TF-11, validated across 6 simulation
variants.)*

**440 · adversarial-exponent-regimes** — Observation
The exponent α depends on the disturbance mechanism: α = 2 under deterministic
drift (coupling-dominant); α = 3/2 under stochastic disturbances; α ≈ 1 when
coupling doesn't dominate base noise. The linear ODE is correct in the
deterministic regime; the stochastic regime needs separate treatment.
*(From simulation variants C/D.)*

**450 · observation-gates-advantage** — Observation
Observation noise (U_o) collapses adversarial exponent from ~1.0 to ~0.2.
Optimal gain (#update-gain) partially restores it to ~0.4. Formally grounds
Boyd's emphasis on Orient quality over raw OODA speed — a fast agent with bad
observations loses most of its advantage. *(From simulation variant E.)*

**460 · per-dimension-persistence** — Theorem
Scalar tempo is a poor summary for anisotropic systems (72% overestimate in
simulation). The per-dimension persistence condition is exact: T_k >
ρ_k / δ_critical_k for each dimension k. The weak dimension is the bottleneck
(84% of total mismatch). Targeted adversarial attack on the weak dimension
amplifies advantage by 17%. *(From simulation variant F.)*

**470 · ???** — Gap
*Adversarial DAG targeting. Which strategy edges are most valuable to attack?
Centrality in the DAG, inter-agent coupling edges, edges that are observable
to the adversary. How does an adversary use knowledge of Σ_t structure to
target actions? This is where #compound-probability-decay becomes a weapon:
disrupting one AND-edge in a deep chain collapses the whole path.*
*(From track-a/04.)*

**475 · ???** — Gap
*Team persistence via DAG redundancy. Why do teams persist where individuals
can't? More paths (OR branches), more observation channels, member
reassignment, collective grafting of strategy alternatives. Connects
#persistence-condition to multi-agent resilience.* *(From track-a/04.)*

---

## IV. Evolving Software Systems

*Domain instantiation: software development as an ACT domain. This section
re-grounds TST (Temporal Software Theory) in ACT's formal machinery —
adding the causal mathematics and adaptive dynamics that TST was developed
without. Software is not just another domain example; it has unique epistemic
properties that make it the ideal testbed for ACT and, recursively, the domain
where ACT-grounded agents will operate.*

*The temporal optimality axiom (#temporal-optimality) now has full backing:
tempo advantage (#adversarial-tempo-advantage), persistence conditions
(#persistence-condition), and gain dynamics (#update-gain) explain WHY
time-optimal development practices work, not just THAT they do.*

**500 · software-scope** — Scope
ACT's software domain applies to systems with non-negligible future change
probability: P(n_future > 0) > ε. For such systems, total lifetime cost
dominates initial implementation cost. Stable subsystems with P(change) < ε
operate at "infinite velocity" — consuming zero future time. *(Regrounding
TST T-03 in ACT.)*

**510 · software-epistemic-properties** — Observation
Software has six unique epistemic properties: (1) fully inspectable environment
— partial observability from cognitive bandwidth, not physics; (2) Level 3
counterfactuals executable via git; (3) causal DAG partially explicit — imports,
types, dependencies; (4) history perfectly recorded — git as complete chronica;
(5) multi-agent through shared versioned artifact; (6) observation channel
quality under agent control — code quality IS observation infrastructure.
*(From via-tft.)*

**520 · feature-definition** — Definition
A unit of functionality that coherently changes the codebase and/or running
system, as perceived by those who requested, implement, or use it. Includes
refactoring (alters future implementation time), excludes true no-ops. *(TST
D-01.)*

**530 · specification-bound** — Theorem
time_min(F) ≥ time_specify(F, context). You cannot implement what you cannot
specify. Information-theoretic necessity: Shannon entropy of the feature
specification bounds implementation time below, modulated by shared context
between specifier and implementer. As AI approaches instant implementation,
software engineering becomes specification engineering. *(TST T-02. One of
TST's strongest claims.)*

**535 · communication-as-bottleneck** — Corollary
As implementation time approaches the specification bound, communication speed
and quality become the limiting factor. *(TST C-02.1.)*

**540 · change-expectation-baseline** — Theorem
E[n_future | n_past] = n_past. The Bayesian consequence of maximum ignorance
(Jeffrey's prior, scale-invariant). Not a heuristic — the mathematical null
hypothesis of temporal prediction. Any deviation requires information that
justifies it. Creates intellectual accountability for abstraction decisions.
*(TST T-04. Genuinely well-grounded.)*

**545 · investment-scaling** — Corollary
Abstraction investment should scale with n_past. Systems with n_past < 3
warrant minimal structural investment. *(TST C-04.1.)*

**550 · developer-as-act-agent** — Definition
The developer's M_t = codebase understanding (mental model of architecture,
dependencies, conventions, state). O_t = task objective ("implement OAuth,"
"fix the race condition"). Σ_t = implementation strategy (the plan, with
AND/OR structure, observable checkpoints, contingency branches). *(From ACT-03
software section.)*

**560 · comprehension-time** — Definition
Time from initial idea to first surviving change. Reading, understanding,
discovering hidden dependencies, building and validating mental model. This is
the cost of constructing M_t for the relevant portion of the codebase.
*(TST D-02.)*

**565 · implementation-time** — Definition
Time from first change to complete feature. Writing, testing, addressing
immediate issues. *(TST D-03.)*

**570 · dual-optimization** — Derived
Principled decisions minimize both comprehension time and implementation time
for future features. Under high turnover (especially 100% context turnover
per AI instance), comprehension cost compounds across every new reader.
*(TST T-05, derived from #temporal-optimality + #change-expectation-baseline.
The claim that comprehension dominates under high turnover is structurally
motivated but the quantitative relationship needs formalization.)*

**580 · change-investment** — Derived
Accept X extra minutes now to save Y per future change when X < n_future × Y.
The threshold form is derived from #temporal-optimality + #change-expectation-
baseline. *(TST T-06. TST also claims that principled implementation "often
costs nearly the same" as quick implementation — this is an empirical
observation, not derived from the formalism.)*

**590 · code-quality-as-observation-infrastructure** — Discussion + Hypothesis
Past actions (writing code) affect future observation quality (reading code).
Well-written code has low U_o for future readers; obfuscated code has high U_o.
This creates a second-order feedback loop: code quality → U_o → η*
(#update-gain) → T (#adaptive-tempo) → slack → code quality. *[Plausible]*
The structural argument is sound — code quality does affect comprehension, and
comprehension does affect effective tempo. Whether this is distinctive to
software or an instance of a more general pattern (agents modifying their own
observation channels) is an open question. The quantitative claim that
#persistence-condition formalizes the virtuous/vicious threshold requires
formalizing "code complexity accumulation rate" as ρ. *(From via-tft mapping.)*

**600 · conceptual-alignment** — Hypothesis
time_comprehension ∝ 1/alignment(code, domain). Misalignment (code says
"user_score," domain says "reputation") taxes every future comprehension. Not
just naming — module boundaries, relationship structure, abstraction levels.
*(TST T-07.)*

**605 · realignment-as-feature** — Corollary — Derived
As domain understanding evolves, realigning code is a principled investment when
T_align < n_future × Δt_comprehension. This isn't cleanup — it's temporal
optimization with measurable ROI. *(TST C-07.1.)*

**610 · atomic-changeset** — Definition
The diff between codebase states before and after feature implementation,
excluding generated artifacts. Crosses architectural boundaries: source, schema,
config, tests, infrastructure, documentation. If it must change to deliver the
feature, it's part of the changeset. *(TST D-04.)*

**620 · changeset-size-principle** — Empirical — Hypothesis
time_implementation(F) ∝ |changeset(F)|. Nearly tautological (more changes take
more time), but reveals that good architecture minimizes FUTURE changeset sizes.
The proportionality constant is unvalidated. *(TST T-08.)*

**625 · comprehension-follows-changeset** — Corollary + Hypothesis
Understanding a feature that touched 20 files requires comprehending 20
contexts. Double the changeset ≈ double the comprehension burden. Creates
double penalty for unnecessarily large changesets. *(TST C-08.1.)*

**630 · change-distance** — Definition
Distance between changes in a codebase: lexical < file < module < service.
*(TST D-05.)*

**640 · change-proximity-principle** — Derived + Hypothesis
Given identical changeset sizes, closer changes require less implementation
time. Explains why modules group co-changing code, layers localize changes,
domain boundaries contain related changes. *(TST T-09.)*

**645 · exponential-cognitive-load** — Hypothesis — Hypothesis
time_actual = time_baseline × k^discontinuities, where k > 1. If context-
switching compounds multiplicatively, even modest k (1.1–1.2) creates
substantial differences across many discontinuities. Requires empirical
validation — the actual relationship may be linear or sub-exponential.
*(TST H-09.1.)*

**650 · system-coupling** — Definition
coupling(module_i, module_j) = P(change(module_j) | change(module_i)).
*(TST D-06.)*

**655 · system-coherence** — Definition
coherence(module) = E[proximity(changes within module)]. *(TST D-07.)*

**660 · coherence-coupling-measurement** — Measurement
quality = Σ coherence / Σ coupling. Computable from git history. Transforms
architectural discussions from opinion to empirical observation. Requires
sufficient history, stable boundaries, representative feature distribution.
*(TST T-10.)*

**670 · principled-decision-integration** — Integration
C* = argmin E[T|C] where expected time integrates across future features,
weighting comprehension (#conceptual-alignment), changeset size (#changeset-
size-principle), and proximity (#change-proximity-principle). Perfect
optimization is impossible (requires knowing all future features), but the
framework structures the decision space and makes tradeoffs explicit. *(TST
T-11.)*

**680 · system-availability** — Definition
availability = MTTF / (MTTF + MTTR). *(TST D-08.)*

**685 · continuous-operation** — Scope Extension
For operational systems: T_effective = T_implementation + P(failure) ×
T_recovery. A non-operational system has infinite implementation time from
the user's perspective. Fault-tolerant design (accept failure, minimize
recovery) can be time-optimal vs defensive programming (prevent failure, complex
recovery). Explains supervision trees, circuit breakers, bulkheads, health
checks. *(TST T-12.)*

**690 · causal-discovery-from-git** — Principle — Plausible
Git provides temporal ordering + interventional data (every commit is an
intervention). Proper causal analysis — not just co-change correlation — is
possible. Software is in Pearl's Regime A (randomized interventions) for causal
discovery. The gap between declared dependencies and empirical causal structure
reveals hidden coupling or stable interfaces. *(From via-tft
causal-extensions.)*

**695 · ???** — Gap
*Three-part tempo decomposition for software: T_obs (compiler, linter, tests)
+ T_explore (code reading, navigation) + T_probe (test runs, staging). Which
component is the bottleneck? How does each connect to code quality as
observation infrastructure (#code-quality-as-observation-infrastructure)?*

**698 · ???** — Gap
*Software persistence condition: the unmaintainability threshold formalized.
T_team > ρ_total / ||δ_critical||. When does a codebase cross from maintainable
to unmaintainable? What are the observable precursors? How does this connect to
the virtuous/vicious cycle (#code-quality-as-observation-infrastructure)?*

---

## V. Software-Grounded Agentic Systems

*Extending the arc: AI agents operating on code are ACT agents whose domain is
software, creating a recursive structure — ACT theory → software domain → agents
that embody ACT. This is where the 100% context turnover problem, M_t
preservation, and the cognitive loop connect the theory back to the systems being
built with it.*

**700 · ai-agent-as-act-agent** — Definition
An AI coding agent is a purposeful adaptive agent with 100% context turnover per
session. It inhabits the purposeful quadrant (#agent-spectrum): it has M_t
(context window + retrieved memory), O_t (task objective), and Σ_t (approach
plan). *(From via-tft mapping, agentic-tft.)*

**710 · context-turnover** — Observation
M_t resets to near-zero at session start. Not gradual degradation but
catastrophic loss. The agent must reconstruct M_t from the environment
(codebase, CLAUDE.md, memory files) at each session. This is fundamentally
different from human developers who retain M_t across sessions.
*(From via-tft mapping.)*

**720 · m-preservation** — Discussion
External memory (CLAUDE.md, memory directories, well-structured code) converts
ephemeral M_t into persistent environmental state. The agent's past actions
modify the environment to make future M_t reconstruction faster. This is
#code-quality-as-observation-infrastructure applied to agent infrastructure
itself. *(From via-tft mapping.)*

**730 · ???** — Gap
*Cognitive loop formalization. The cycle: read environment → construct M_t →
form/revise Σ_t → select action → observe result → update M_t. How does this
differ from the generic orient cascade (#orient-cascade)? What's specific to
language-based agents? Agentic-tft docs 10-14 have substantial thinking on
this.* *(From agentic-tft.)*

**740 · ???** — Gap
*Evaluation framework. How do you measure an AI agent's ACT quantities? M_t
quality (can the agent predict what it will find?), Σ_t quality (does the plan
lead to O_t?), tempo (how fast does the agent acquire useful information?).
Connects to crèche and training design.* *(From agentic-tft.)*

**750 · ???** — Gap
*Crèche concept. Experiential training environments where agents develop their
adaptive capacity. What does an ACT-grounded training regime look like? How do
you train for good M_t construction, effective Σ_t formation, appropriate gain
calibration?* *(From agentic-tft.)*

**760 · ???** — Gap
*The recursive completion. An agent using ACT to guide its own behavior while
operating on a codebase that implements ACT. Self-referential but not
paradoxical — the agent's understanding of tempo, persistence, and gain
directly informs its development decisions. What does this look like in
practice?*

---

## Appendices (Evidence & Reference)

*These support specific claims above with detailed evidence, worked examples,
or historical development.*

**A · linear-ode-approximation** — Reference
The linear ODE from TF-11: dδ/dt = ρ − T·g(δ). Correct for deterministic drift
in continuous time. Pedagogically valuable, not the general case. The sector-
condition framework (#sector-condition-stability) is primary. *(From TF-11,
demoted.)*

**B · simulation-results** — Evidence
Six simulation variants validating and refining claims from Sections I–III.
Variant A/B: deterministic drift confirms α = 2. Variant C/D: stochastic gives
α = 1.5. Variant E: observation noise gates advantage. Variant F: per-dimension
persistence exact. *(From track-b-nonlinear-sims.)*

**C · worked-examples** — Reference
Kalman filter (M_t only), PID controller (O_t only), LQG (M_t + O_t without
explicit Σ_t), RL agent (full triple), developer (software domain).

**D · intent-dag-development** — Historical
Three independent formalism attempts converging on AND/OR + single-parameter
edges. Documents the convergence testing and what was settled vs open.
*(From track-a-intent-dag/ and 04-intent-dag-consolidated.md.)*

**E · prior-art-positioning** — Reference
Assessment of Hafez (bi-predictability), IBM 2025 (the void), BDI (named the
parts, no dynamics), active inference (closest competitor, less transparent),
FAST workshop papers. *(From scratch/02-prior-art-assessment.md.)*

---

## Dependency Summary

The claim graph is mostly sequential, but key non-local dependencies include:

- **#update-gain** is used throughout: in M_t updates (Section I), Σ_t edge
  updates (#edge-update-via-gain), and observation-quality analysis
  (#observation-gates-advantage, #code-quality-as-observation-infrastructure)

- **#persistence-condition** grounds both M_t persistence (Section I) and
  strategy persistence (#strategy-persistence), software maintainability
  (#code-quality-as-observation-infrastructure), and team resilience (#475)

- **#temporal-optimality** is the optimization criterion that everything serves:
  it motivates adaptive tempo (Section I), grounds TST's practical claims
  (Section IV), and explains why adversarial dynamics are superlinear
  (Section III)

- **#information-bottleneck** applies to M_t compression (Section I), shared
  intent compression (#shared-intent), and cognitive cost of Σ_t (#345)

- The software domain (Section IV) both *applies* the general theory AND
  *pushes requirements back up* — e.g., #code-quality-as-observation-
  infrastructure reveals a feedback loop that the general theory should
  accommodate, and #edge-semantics identifiability (#350) is resolved in
  software but not in general
