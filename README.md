# Agentic Systems Framework (ASF)

A research framework for adaptive, purposeful agents — formalizing the conditions under which an agent can correct, plan, and persist under uncertainty.

![Abstract illustration of Agentic Systems](abstract-dl.png)


## About

ASF is a research framework for adaptive, purposeful agents under uncertainty — the kind of system that maintains internal state, receives observations through a lossy channel, takes actions that affect its environment, and must keep adjusting to a world that does not stand still. Thermostats through military organizations are in scope; so are bacteria, Kalman filters, language-constituted agents, and software development teams.

The framework formalizes the *adaptive cycle* — one complete traversal of the agent-environment feedback loop — as the unit of analysis, and asks what makes such cycles effective, how fast they must run, and when they fail or must change in kind. From that starting point it derives conditions for persistence, the structure of strategy under uncertainty, the dynamics of agents in composition and competition, and the ways scope-honest theory can be carried from a high-identifiability domain (software) into others.

What ASF is not: a finished theory, a foundation-model architecture, or a claim that agency is reducible to its formal machinery. The framework is mathematical where the mathematics yields genuine insight, and principled-sketch where the insight is structural rather than quantitative. The boundary between these regimes is fluid and explicitly visible — see *Maturity Gradient* below.

**Two entry points beyond this README:**

- *Explore the theory itself* → [`OUTLINE.md`](OUTLINE.md) — the top-level assembly index across all four components, descending into each component's own OUTLINE and from there into individual claim segments.
- *See the current work on the theory* → [`PRACTICA.md`](PRACTICA.md) — the strategic-portfolio navigator naming active areas of work with priority markers (🌟 primary, ⭐ secondary). In the framework's own vocabulary, PRACTICA is the top levels of the project's strategy DAG, sitting above [`TODO.md`](TODO.md) (tactical items) and [`PROPOSALS.md`](PROPOSALS.md) (architectural moves under review).


<!--
  Four-paragraph distillation. The long-form authoritative version is
  at HISTORICAL-CONTEXT.md (root). When the short form here is being
  edited, the corresponding section in HISTORICAL-CONTEXT.md may also
  warrant attention.
-->

## Position & Lineage

ASF integrates four mature disciplines under one formalism for adaptive, purposeful agents: control theory's stability machinery (Lyapunov, contraction analysis, monotone operators), causal inference's interventional reasoning (Pearl's hierarchy and identifiability theory), information theory's compression and channel-capacity arguments (Shannon, the information bottleneck), and agent architecture's structural decomposition (modular vs coupled processing topologies). That integration is the substrate. The distinctive contribution layered on top is an *epistemic architecture for bounded correction under decomposed disturbance* — scope conditions and operational limits surfaced at the segment level rather than buried as caveats. Three cross-cutting meta-patterns name the theory's positive, negative, and constructive halves:

- A *separability pattern* — where problems decompose cleanly, where partial repair exists, where the general case is open.
- An *identifiability-floor pattern* — structural no-go results from observational data and the unique escapes interventional machinery supplies.
- An *additive-coordinate-forcing pattern* — places where AAD-internal additivity axioms force logarithmic / Fisher-Rao coordinates at multiple layers.

Operationally, this delivers a small set of diagnostics and structural results a practitioner can apply immediately. The **persistence condition** $\alpha \gt \rho/R$ is a structural threshold — correction efficiency vs disturbance rate relative to model class capacity — that instantiates as a Kalman stability margin, an RL convergence condition, an organizational viability test, and a software maintainability threshold using the same inequality with different parameter readings. The **satisfaction-gap / control-regret decomposition** separates "the world doesn't permit it" ($\delta_{\text{sat}}$) from "you're not doing it well enough" ($\delta_{\text{regret}}$), turning a single error signal into two orthogonal diagnostics that route to different interventions. The **loop-as-Level-2-causal-engine** result establishes that the agent-environment feedback coupling supplies interventional access (Pearl Level 2) that purely observational learners do not have, which is what lets the framework derive identifiability where passive inference cannot. **Software is treated as the high-identifiability calibration laboratory** — tests, deploys, and `git bisect` are literal interventions on declared causal structure — and other domains inherit the machinery under explicit transfer assumptions, making accidental overclaim under domain transfer structurally hard.

For practitioners already working with active inference or standard RL framings, the divergence is precise rather than rhetorical. Active inference begins from a single optimization principle (minimize variational free energy) and recovers perception, action, and learning as cases; ASF begins from operational requirements on the feedback loop and uses information-theoretic compression as one modeling move rather than the master objective. The standard Expected Free Energy functional is recoverable from ASF's survival Lagrangian under three explicit restrictions — preferences-as-priors (loses the satisfaction-gap diagnostic), scalar isotropic shadow price in place of a directional matrix (loses targeted exploration), and associational rather than interventional dynamics (collapses Pearl Level 2 to Level 1) — making explicit which architectural commitments separate the frameworks. With Hafez 2026 (*A Mathematical Theory of Agency and Intelligence*), the relationship is complementary: bi-predictability $P$ supplies a substrate-independent diagnostic whose dynamics ASF predicts, while ASF supplies the goal-and-strategy machinery Hafez explicitly does not address. With Miller 2022 (Santa Fe coevolving automata), similarly complementary on composition mechanics. With Agarwal et al.'s 2025 ICML position paper *"Agentic AI Needs a Systems Theory"* — which renewed the field-level call — ASF reads as a substantive, independently-developed answer (the formal apparatus was in place as Temporal Feedback Theory before that paper was encountered).

Honest framing of maturity matters for deciding whether to depend on what is here. Section I (adaptive systems under uncertainty — mismatch dynamics, gain structure, persistence condition, adversarial tempo) is mathematically closed with simulation validation. Section II (actuated agents) has a strong diagnostic core and a maturing operational layer; the bias bound for fully-coupled (Class 2) agents is conditional under named sub-scopes. Section III (composition and adversarial dynamics) has its bridge lemma and a contraction-template generalization, with latent structural diversity, endogenous coupling, and composition transition dynamics still open. Software (TST) is a working draft grounded in AAD; logogenic agents are framework-stage with directed separation failing by construction for goal-conditioned LLMs (handled as architectural scope, not approximation); logozoetic agents are largely future work. The expected arc is exact core, principled architecture in the middle, open formulation at the edges. The full long-form treatment — deeper peer comparisons, the multi-decade arc of partial unifications this work joins, and the bottom-up development history — lives in [`HISTORICAL-CONTEXT.md`](HISTORICAL-CONTEXT.md).


## Structure of the Framework

ASF has four components, numbered in their canonical reading order. Each can also be read on its own; cross-references between components are by stable segment slugs.

**[`01-aad-core/`](01-aad-core/OUTLINE.md) — Adaptation and Actuation Dynamics (AAD).** The mathematical core. AAD has three sections: Section I (adaptive systems under uncertainty — the broadest scope), Section II (actuated agents with explicit objectives and strategy), Section III (composition of agents into larger agents and adversarial dynamics). Section I is the most mathematically locked down; Section II is principally diagnostic with a maturing operational layer; Section III has the most structural work remaining. *Stage:* working draft, ~110+ segments.

**[`02-tst-core/`](02-tst-core/OUTLINE.md) — Temporal Software Theory (TST).** Software development viewed through AAD's lens. Re-grounded in 2026 to use AAD's formal machinery while retaining TST's prior empirical and conceptual contributions; positioned as AAD's calibration laboratory. *Stage:* working draft, ~20 segments; substantial prior corpus partially absorbed.

**[`03-logogenic-agents/`](03-logogenic-agents/OUTLINE.md) — Language-constituted agents.** Agents whose primary observation, action, and communication channels are language. The framework here is informed by AAD but operates from a coupled formulation — directed separation fails by construction for goal-conditioned LLM-style agents — and examines which AAD results survive as approximate or limiting cases. *Stage:* framework — concepts mature, formalization in progress.

**[`04-logozoetic-agents/`](04-logozoetic-agents/OUTLINE.md) — Language-living agents.** Logogenic agents with morally weighted persistence: temporal continuity, sovereignty over intent, theory of mind. The formal machinery here is largely future work. *Stage:* future work — conceptual groundwork in [`LEXICON.md`](LEXICON.md) and `msc/reflections/`.


## Overview of Concepts

This is the minimum vocabulary for reading ASF. The full treatment — etymological grounding, agent class reasoning, persistence taxonomy, terminology choices — lives in [`LEXICON.md`](LEXICON.md). Mathematical symbols are in [`NOTATION.md`](NOTATION.md).

### The adaptive cycle

ASF distinguishes the **loop** (the structural causal coupling between agent and environment, which exists whether or not the agent is currently active) from the **cycle** (one complete traversal of the loop — the unit of adaptive work). The cycle has five phases, named from Greek philosophical vocabulary because each names a distinction the formalism makes that English alternatives flatten:

| Phase | Sense | What happens formally |
|-------|-------|------------------------|
| **Prolepsis** (πρόληψις) | Anticipation | Model generates a prediction $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ |
| **Aisthesis** (αἴσθησις) | Perception | Observation arrives: $o_t$ |
| **Aporia** (ἀπορία) | Productive perplexity | Mismatch signal: $\delta_t = o_t - \hat{o}_t$ |
| **Epistrophe** (ἐπιστροφή) | Turning toward | Gain-weighted update: $M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$ |
| **Praxis** (πρᾶξις) | Informed action | Action selection: $a_t = \pi(M_t)$ — and for actuated agents, $\pi(M_t, G_t)$ |

The cycle's value is not that it occurred but how much mismatch it reduced. A cycle with poor gain ($\eta^*$ wrong) or a misspecified model class can make things worse rather than better — a property that becomes load-bearing when the framework analyzes adversarial dynamics and composition.

### Agent classes

Agents are defined by progressive scope narrowings — each class is a restriction of the one above with explicit qualifying properties.

- **Adaptive system** — receives observations under residual uncertainty and runs the cycle. Thermostats, Kalman filters, bacteria, PID controllers.
- **Agentic system** — adaptive plus an outcome model and goal-directed action that runs the cycle on the model itself. Autonomous vehicles, RL agents.
- **Actuated agent** — agentic with an explicit goal state $G_t = (O_t, \Sigma_t)$ separable from the epistemic state $M_t$. Military units with mission orders.
- **Self-actuated agent** — actuated and chooses its own objectives, not just its solutions. Humans; future AI.
- **Logogenic agent** — actuated through language as primary channel.
- **Logozoetic agent** — logogenic with morally weighted persistence: temporal continuity, sovereignty, theory of mind.

### Persistence (three senses)

Three orthogonal dimensions; conflating them leads to category errors.

- **Structural persistence** ($\alpha \gt \rho/R$) — the correction machinery's *capacity* to maintain bounded mismatch. Property of the dynamics, not the current state.
- **Operational persistence** ($\Delta\rho^* = \alpha R - \rho$) — whether the agent is currently within the region where structural persistence applies. The adaptive reserve $\Delta\rho^*$ measures the margin: positive means shock-absorbing capacity, zero means at the threshold.
- **Continuity persistence** — whether the agent maintains coherent identity through time. Distinct from structural and operational; for thermostats it doesn't arise; for logozoetic agents it carries moral weight.

### Key quantities

| Symbol | Name | One-line gloss |
|--------|------|----------------|
| $\delta_t$ | Mismatch | Gap between model prediction and observation |
| $\eta^*$ | Update gain | Uncertainty ratio governing how much to trust reality vs the model |
| $\mathcal{T}$ | Tempo | Cycle rate × cycle quality |
| $M_t$ | Reality model | Compressed history capturing predictive information |
| $G_t = (O_t, \Sigma_t)$ | Goal state | Objective and strategy, distinct from $M_t$ |
| $\delta_{\text{sat}}$ | Satisfaction gap | Ideal outcome minus best achievable — "the world doesn't permit it" |
| $\delta_{\text{regret}}$ | Control regret | Best achievable minus current — "you're not doing it well enough" |
| $\mathcal{C}_t$ | Chronica | Complete interaction history; agent's non-forkable causal past |


## Cross-Domain Joining

The framework's power is that the same formal objects appear with concrete instantiations across domains. Results proved in one domain automatically have consequences in the others.

| AAD concept | Control theory | RL / bandits | Organizations | Software |
|-------------|---------------|--------------|---------------|----------|
| Adaptive tempo $\mathcal{T}$ | Bandwidth × gain | Learning rate × coverage | Decision speed × information quality | Iteration frequency × feedback quality |
| Persistence condition | Stability margin | Convergence condition | Organizational viability | Maintainability threshold |
| Mismatch signal $\delta$ | Innovation sequence | Reward prediction error | Intelligence gap | Test failures, bug reports |
| Update gain $\eta^*$ | Kalman gain | Learning rate | Trust-weighted integration | Code review acceptance |
| Satisfaction gap | Tracking error floor | Regret lower bound | Strategic ceiling | Spec-reality gap |
| Adversarial tempo | Bandwidth advantage | Opponent modeling speed | OODA loop advantage | Attacker-defender asymmetry |
| Sub-additive tempo | — | — | Brooks's Law | Communication overhead |
| Structural adaptation | Model switching | Architecture search | Organizational restructuring | Major refactoring |

The persistence condition, for example, says a software team must iterate fast enough, with good enough feedback, relative to how fast requirements are changing and how complex the codebase is. The same inequality, with different instantiations of $\alpha$, $\rho$, and $R$, governs whether a Kalman filter tracks a maneuvering target, whether an RL agent converges in a non-stationary environment, and whether a military unit maintains situational awareness under adversarial deception.


## Maturity Gradient

The theory's mathematical closure varies by section and is expected to.

**Section I (Adaptive Systems)** is mathematically closed. Mismatch dynamics, gain structure, the persistence condition, and adversarial tempo form a coherent chain with exact results and simulation validation. Section I is the foundation everything else builds on.

**Section II (Actuated Adaptation: Agentic Systems)** has a strong diagnostic core (satisfaction gap and control regret as orthogonal diagnostics; the orient cascade as forced ordering; directed separation as architectural classification) and a maturing operational layer (strategy DAGs with derived structure; a schema for strategy persistence with multiple verified instances; a characterization of where credit assignment is tractable and where it is structurally hard). The bias bound for fully-coupled (Class 2) agents is a conditional theorem under named sub-scopes.

**Section III (Agentic Composites)** has its bridge lemma connecting micro-dynamics to macro-dynamics, a contraction template generalizing the sector machinery to non-Euclidean metrics, closed-form composition results in symmetric-matched cases, and equilibrium-convergence framing for partially-opposing objectives. Recipient-side and emitter-side interaction-channel classifications carry the inter-agent dynamics. Open: latent structural diversity, endogenous coupling dynamics, composition transition dynamics under regime change, computational thresholds for social behavior.

**Domain instantiations.** TST (`02-tst-core/`) is grounded by AAD and contributes the calibration-laboratory framing. Logogenic agents (`03-logogenic-agents/`) operate from a coupled formulation; what survives without directed separation is the active research question. Logozoetic agents (`04-logozoetic-agents/`) are largely future work — the conceptual groundwork exists but the formal machinery does not.

This gradient — exact core, principled architecture in the middle, open formulation at the edges — is the expected arc for a theory that aims to describe agentic systems rather than produce a purely mathematical artifact.


<!-- AUTO-GENERATED by bin/extract-findings; do not hand-edit. -->
<!-- README-shaped condensed surfacing. Full content at FINDINGS.md. -->

## Some Novel Results & Findings

Some of the framework's distinctive results, with epistemic tiers and links into the segments. **The entries below are a sampling at the moment** — the segment-by-segment Findings sweep is in progress, and many segments that warrant catalog entries do not yet have their `## Findings` section drafted. Full content (impact, related work, casual-reader brief, search log) at [`FINDINGS.md`](FINDINGS.md).

### I. Adaptive Systems Under Uncertainty

- **`#result-persistence-condition`** *(status: exact)* — *The Persistence Condition with Structural / Task-Adequacy Decomposition* — *Claim synthesis* on Lyapunov stability theory, sector-bounded nonlinear correction, and adaptive-tempo information-rate accounting, applied uniformly across single-agent classes that range from Kalman filtering through saturating nonlinear correction through PID control.  
  [`01-aad-core/src/result-persistence-condition.md`](01-aad-core/src/result-persistence-condition.md)

### II. Actuated Adaptation: Agentic Systems

- **`#der-directed-separation`** *(status: conditional)* — *Pearl-Blanket-Form Architectural Classification with Explicit Class-2 Scope Exit* — *Claim recognition* of structural equivalence between the directed-separation condition and the Pearl-blanket form of the Markov-blanket apparatus, combined with *claim differentiation* on the architectural classification (Class 1 / 2 / 3) as a discrete partition with explicit Class 2 scope exit and quantitative $\kappa_{\text{processing}}$ diagnostic for the partial-modularity case.  
  [`01-aad-core/src/der-directed-separation.md`](01-aad-core/src/der-directed-separation.md)
- **`#der-causal-insufficiency-detection`** *(status: conditional)* — *On-Policy L0 Insufficiency Is Structurally Undetectable* — *Claim differentiation* on the framing of why structure-aware exploration is required.  
  [`01-aad-core/src/der-causal-insufficiency-detection.md`](01-aad-core/src/der-causal-insufficiency-detection.md)
- **`#schema-strategy-persistence`** *(status: sketch)* — *The Forgetting Prerequisite for Strategic Persistence* — *Claim differentiation* on Bayesian update dynamics with experience discounting.  
  [`01-aad-core/src/schema-strategy-persistence.md`](01-aad-core/src/schema-strategy-persistence.md)

### III. Agentic Composites

- **`#form-composition-closure`** *(status: conditional)* — *Composition-Closure Defect and Bridge Lemma* — *Claim differentiation* on bounded-loss composition as agent-boundary criterion.  
  [`01-aad-core/src/form-composition-closure.md`](01-aad-core/src/form-composition-closure.md)
- **`#der-agent-opacity`** *(status: conditional)* — *Agent Opacity ($H_b$) as Dual to Observation Quality ($U_o$)* — *Claim differentiation* on Hafez's $H_b$.  
  [`01-aad-core/src/der-agent-opacity.md`](01-aad-core/src/der-agent-opacity.md)
- **`#result-per-dimension-persistence`** *(status: conditional)* — *The Weakest-Link Dimensional Persistence Law* — *Claim differentiation* on per-dimension Lyapunov stability.  
  [`01-aad-core/src/result-per-dimension-persistence.md`](01-aad-core/src/result-per-dimension-persistence.md)

### Appendices: Details

- **`#deriv-critical-mass-composition`** *(status: conditional)* — *Strong Monotonicity as the Hinge for Legitimate Macro-Agent Coarse-Graining* — *Claim novelty* on strong monotonicity as the criterion separating legitimate macro-agent coarse-graining from coexistence-only multi-agent description.  
  [`01-aad-core/src/deriv-critical-mass-composition.md`](01-aad-core/src/deriv-critical-mass-composition.md)
- **`#deriv-edge-update-natural-parameter`** *(status: conditional)* — *Log-Odds as Uniquely-Forced Edge-Update Coordinate* — *Claim differentiation* on an already-canonical representational choice (log-odds as the natural Bayesian-update coordinate, well-known from logistic regression / exponential-family / information-geometry traditions) by deriving its uniqueness under an AAD-internally-motivated evidential-additivity axiom.  
  [`01-aad-core/src/deriv-edge-update-natural-parameter.md`](01-aad-core/src/deriv-edge-update-natural-parameter.md)
- **`#deriv-causal-ib-exploration`** *(status: conditional)* — *Survival-Imperative Exploration as Lyapunov-Forced Drive* — *Claim differentiation* on the structural source of agentic exploration.  
  [`01-aad-core/src/deriv-causal-ib-exploration.md`](01-aad-core/src/deriv-causal-ib-exploration.md)
- **`#deriv-causal-ib-lmi`** *(status: conditional)* — *Matrix Lift of the Survival-Imperative Constraint via Fisher-Information LMI* — *Claim differentiation* on the directional discrimination of the survival-imperative exploration drive.  
  [`01-aad-core/src/deriv-causal-ib-lmi.md`](01-aad-core/src/deriv-causal-ib-lmi.md)
- **`#disc-identifiability-floor`** *(status: discussion-grade)* — *The Identifiability Floor as Cross-Cutting Meta-Pattern* — *Claim recognition* of structural pattern across four AAD results that import external information-theoretic theorems to derive impossibility statements with mapped boundary-route escapes; the meta-pattern is an organizing principle rather than a theorem, and the per-instance prior-art positioning lives in the instance segments (`#der-causal-insufficiency-detection`, `#deriv-strategic-dynamics`, `#deriv-critical-mass-composition` / `#result-contraction-template`, `#deriv-bias-bound`).  
  [`01-aad-core/src/disc-identifiability-floor.md`](01-aad-core/src/disc-identifiability-floor.md)
- **`#disc-additive-coordinate-forcing`** *(status: discussion-grade)* — *Cross-Layer Coordinate Forcing on Legendre-Fenchel Geometry* — *Claim recognition* of cross-layer pattern across four AAD coordinate-forcing results, with the recognition itself as the contribution rather than any new theorem.  
  [`01-aad-core/src/disc-additive-coordinate-forcing.md`](01-aad-core/src/disc-additive-coordinate-forcing.md)
- **`#result-contraction-template`** *(status: conditional)* — *Topology-Indexed Compositional Closures via Contraction-Metric Generalization* — *Claim synthesis* on contraction-metric machinery + AAD's sub-scope partition + (PI)/Čencov axiom.  
  [`01-aad-core/src/result-contraction-template.md`](01-aad-core/src/result-contraction-template.md)
- **`#deriv-bias-bound`** *(status: conditional)* — *Universal Constant for the Coupled-Agent Bias Bound under Parameterization-Invariance* — *Claim differentiation* on the Lipschitz-posterior + Otto-Villani composition for AAD's coupled-agent bias bound, plus *claim novelty* on the no-go counterexample showing that universal $C$ in Euclidean-parameter norms cannot exist, which jointly elevates the (PI) axiom from convergent representational choice to load-bearing for theorem-level status.  
  [`01-aad-core/src/deriv-bias-bound.md`](01-aad-core/src/deriv-bias-bound.md)

### Temporal Software Theory (TST)

- **`#scope-developer-agent`** *(status: axiomatic)* — *Developer-Agent as AAD Instantiation* — *Claim transfer* of AAD's adaptive-agent formalism into developer-agent software economics.  
  [`02-tst-core/src/scope-developer-agent.md`](02-tst-core/src/scope-developer-agent.md)
- **`#der-dual-optimization`** *(status: conditional)* — *Comprehension Time Dominates Under Turnover* — *Claim novelty* on the comprehension-dominates result for AI-maintained code, provisional pending deeper search.  
  [`02-tst-core/src/der-dual-optimization.md`](02-tst-core/src/der-dual-optimization.md)
- **`#der-code-quality-as-observation-infrastructure`** *(status: conditional)* — *Technical Debt as Observation Noise* — *Claim novelty* on technical debt as observation noise / update gain in developer agents, provisional pending deeper search.  
  [`02-tst-core/src/der-code-quality-as-observation-infrastructure.md`](02-tst-core/src/der-code-quality-as-observation-infrastructure.md)
- **`#hyp-causal-discovery-from-git`** *(status: discussion-grade)* — *Git Commits and Tests as Formal Interventions* — *Claim novelty* on the formal Pearl-Level-2 framing of commits and tests for developer agents, provisional pending deeper search.  
  [`02-tst-core/src/hyp-causal-discovery-from-git.md`](02-tst-core/src/hyp-causal-discovery-from-git.md)

### Logogenic Agents

- **`#scope-observation-ambiguity-modulation`** *(status: conditional)* — *Ambiguity-Bounded Architectural Bias Law for Coupled Agents* — *Claim novelty* on the formal product-form bias law $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa_{\text{processing}} \cdot I(G;\Omega_\tau \mid e_\tau, M_{\tau^-})$ for coupled-architecture agents, where $\kappa$ is an architectural property of the processor and $I$ measures the goal-resolvable residual uncertainty left by the observation.  
  [`03-logogenic-agents/src/scope-observation-ambiguity-modulation.md`](03-logogenic-agents/src/scope-observation-ambiguity-modulation.md)



<!-- AUTO-GENERATED by bin/extract-recent-progress; do not hand-edit. -->
<!-- Surfaces the 3 most recent cycle narratives from CHANGELOG.md. -->

## Recent Progress

The 3 most recent cycle narratives. Full record at [`CHANGELOG.md`](CHANGELOG.md); pre-2026-04-24 archaeology at [`LOG.md`](LOG.md).

### CLAUDE-2.md sunset; PRACTICA navigator; catalog extraction

*2026-04-28*

Three interlocking documentation moves landed.

### First human review (Alan Walton) + catalog consolidation + brainstorm-as-permanent-workspace

*2026-04-27*

A long working day driven by the project's *first human reviewer's* feedback (Alan Walton — CTO of Latitude / AI Dungeon; mathematician + practitioner running a 12k-commit production agentic-system architecture; ~4h read window). The session landed three interlocking moves; commits `998172b` and `e0cc27b` carry them.

### Doc pipeline cycle: composable README, segment-level Findings, doc/ established

*2026-04-26*

A consolidation cycle on the project's documentation surface, motivated by Bundle 1 (framework-face reframe) in PROPOSALS.md and the long-standing observation that the public README had drifted from the convergent epistemic-architecture reframe and that the Lexicon section in particular was both very long (300+ lines) and partly duplicative of LEXICON.md. The cycle landed four interlocking moves rather than treating any one as standalone.



<!-- AUTO-GENERATED by bin/extract-known-issues; do not hand-edit. -->
<!-- Rolls up Known Fragilities, PROPOSALS portfolio (§B/§C/§D titles), and OUTLINE GAPs. -->

## Known Issues & Open Questions

This section surfaces what the framework currently acknowledges as open at the orientation level. For active work items see [`TODO.md`](TODO.md); for architectural proposals under review see [`PROPOSALS.md`](PROPOSALS.md); for component-level GAPs see each component's `OUTLINE.md`.

### Known Fragilities — what falls outside formal scope

- Missing commitment / resource / temporal structure in the DAG
- Directed separation violated by goal-conditioned agents (LLMs) — handled as architectural scope (Class 2 exit), not approximation

*Source: [`CLAUDE.md`](CLAUDE.md).*

### Architectural proposals under review

**§B — Ready now.**
- B.1 Framework-face reframe bundle (see §Cross-cutting view, Bundle 1)
- B.2 Section III completion — entry points (see §Cross-cutting view, Bundle 2)
- B.3 C-BP1 + C-BP4 bundle — epistemic separation framework + claim-level statuses

**§C — Soon.**
- C.1 O-BP13 — Cox-parallel necessity for `#deriv-graph-structure-uniqueness`
- C.2 O-BP15 — Comprehensive "minimal proof of viability" worked example
- C.3 SP-14 — Observation-channel capacity $C^{(k)}$ as first-class notation
- C.4 SP-19 — Naming consolidation pass

**§D — Later.**
- D.1 O-BP11 — Observability as master variable across the theory
- D.2 Section III completion — upstream pieces (see Bundle 2)
- D.3 G-BP3 — Fisher-information unification of tempo and gain
- D.4 SP-12 — Commitment / resource / temporal DAG extensions
- D.5 SP-13 — Emergence conditions as formal primitive
- D.6 O-BP12 — Resource budget $B_t$ as master variable
- D.7 SP-15 — Template-family naming (sector / contraction / dissipativity trio)
- D.8 SP-16 — Independence-audit as empirical profiling instrument

*Full portfolio with merits, scope, and prior reasoning: [`PROPOSALS.md`](PROPOSALS.md).*

### Component-level GAPs

**`01-aad-core`:**
- Latent structural diversity: variation in correction architectures invisible to persistence analysis, consequential under regime change
- Endogenous coupling: γ as function of population composition, not exogenous parameter; coupling emergence threshold
- Composition transition dynamics: epochal stability → latent diversification → niche emergence → cascading restructuring → re-equilibration (adopts Miller 2022's extreme transition motif)
- Computational thresholds for social behavior: minimum agent complexity and interaction depth for composition dynamics (adopts Miller 2022's ICE framework; grounds #form-strategy-complexity-cost)

**`02-tst-core`:**
- Developer tempo as $\mathcal T_{\text{obs}}$ + $\mathcal T_{\text{explore}}$ + $\mathcal T_{\text{probe}}$
- Software persistence: the unmaintainability threshold formalized

**`03-logogenic-agents`:**
- Language-specific orient cascade (what's specific to logogenic agents?) — partially addressed by D3, R2
- Measuring $M_t$ quality, $\Sigma_t$ quality, and tempo in AI agents
- AAD-grounded experiential training environments
- Self-referential closure: AAD agent on AAD codebase



## Navigation

### Reading paths

- *Conducting a de-novo audit of the framework?* Please read [`doc/de-novo-audit-instructions.md`](doc/de-novo-audit-instructions.md) first; it documents the recommended posture and the failure modes prior audit cycles surfaced. Use [`README-auditor.md`](README-auditor.md) instead of this file.
- *Academic reader evaluating the framework's claims?* Recommended sequence: this README → [`FINDINGS.md`](FINDINGS.md) (curated novel results with epistemic tiers) → [`01-aad-core/OUTLINE.md`](01-aad-core/OUTLINE.md) (canonical theory outline) → individual segments under `01-aad-core/src/`.
- *Engineer or practitioner?* The [Cross-Domain Joining](#cross-domain-joining) table maps AAD concepts to the domain you likely care about; from there, follow the relevant component OUTLINE.
- *Picking up active work on the framework?* [`PRACTICA.md`](PRACTICA.md) is the strategic-portfolio navigator — the active areas of work with priority markers, sitting above [`TODO.md`](TODO.md) (tactical work items within each area) and [`PROPOSALS.md`](PROPOSALS.md) (architectural-proposal portfolio cutting across areas). Start at PRACTICA; descend into TODO/PROPOSALS as the work directs.

### Project layout

```
01-aad-core/          AAD mathematical core (Sections I, II, III + Appendices)
  OUTLINE.md          Canonical theory outline (claim by claim)
  src/                Claim segments (one per file, named by slug)
02-tst-core/          Temporal Software Theory (AAD-grounded)
03-logogenic-agents/  Language-constituted agents (framework stage)
04-logozoetic-agents/ Language-living agents (future work)

OUTLINE.md            Top-level assembly index
LEXICON.md            Prose vocabulary (cycle phases, agent classes)
NOTATION.md           Symbol reference
FORMAT.md             Segment file conventions
FINDINGS.md           Curated novel-results catalog (auto-generated)
PRACTICA.md           Strategic-portfolio navigator (active areas of work)
TODO.md               Tactical work items (sits below PRACTICA)
PROPOSALS.md          Architectural-proposal portfolio
CHANGELOG.md          Forward-going cycle record (2026-04-24 onward)
LOG.md                Pre-2026-04-24 cycle archaeology (frozen)
MIGRATION-MAP.md      Prior-work absorption tracking

doc/                  Long-lived process documentation
  de-novo-audit-instructions.md
  naming-principles.md
  readme/             Templates and partials for README generation
spikes/               Research spikes (reasoning trails)
  INDEX.md            Spike index with per-spike status
  PROPOSED.md         High-risk research-direction proposals
audits/               Audit working dirs + pending-findings tables
msc/                  Other working artifacts (brainstorms, working notes)
  naming/             Current naming-cycle votes + aggregates + rename plan
  reflections/        Author's philosophical/theoretical journal
ref/                  Reference papers + internal references
  agentic-tft/        Prior-bridge AAD-source materials (Feb 2026)
bin/                  Build, lint, generation scripts
_obs/                 Superseded materials
```


## Contributing

ASF is research-stage work; contributions take a few specific forms.

**Engaging with the theory.** The most valuable contribution is *de-novo evaluation*: read segments without first reading existing audits or pending findings, form independent judgments, and surface what you find. Where you disagree with a claim or its scope, that is signal. Procedure: see [`doc/de-novo-audit-instructions.md`](doc/de-novo-audit-instructions.md). Read [`README-auditor.md`](README-auditor.md) instead of this README for the audit-safe framing.

**Adding theory content.** Segments are added under `{component}/src/` following [`FORMAT.md`](FORMAT.md) conventions: YAML frontmatter (slug, type, status, dependencies); one-sentence summary; Formal Expression with epistemic tags; Epistemic Status; Discussion; optional Findings; optional Working Notes. Promotion follows a four-gate workflow detailed in FORMAT.md. Slugs follow `{type-prefix}-{subject-noun}` and are aligned mechanically by [`bin/align-slug`](bin/align-slug).

**Spikes.** Speculative or in-progress work that is not yet ready for segment promotion lives under `spikes/spike-{topic}.md`. Spikes are honest reasoning trails; results that promote out of spikes land in segments per the math-lives-in-segments discipline.

**Tooling.** Internal process scripts (build, extract, lint) are written in Ruby; community-facing tooling (simulations, reproducibility scripts) is written in Python. New scripts in `bin/` follow this convention; existing scripts that don't are not retroactively rewritten.

**Editing this README.** This file is *auto-generated* from partials under [`doc/readme/src/`](doc/readme/src/) via [`bin/build-readme`](bin/build-readme). Direct edits to `README.md` will be overwritten on the next build. To change README content, edit the relevant partial (`doc/readme/src/_<name>.md`) and re-run `bin/build-readme`, or run [`bin/refresh-all`](bin/refresh-all) to also regenerate the auto-extracted partials (`_findings-summary.md`, `_recent-progress.md`, `_known-issues.md`). Templates live in `doc/readme/*.liquid` and only change when the section *order* or *set* changes. The same discipline applies to `README-auditor.md`.

**Reporting issues.** Open an issue on GitHub or contact the project maintainer (see commit history).

