# Agentic Systems Framework (ASF)

A research framework for adaptive, purposeful agents — formalizing the conditions under which an agent can correct, plan, and persist under uncertainty.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19986312.svg)](https://doi.org/10.5281/zenodo.19986312) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

![Abstract illustration of Agentic Systems](abstract-dl.png)


## About

ASF is a research framework for adaptive, purposeful agents under uncertainty — the kind of system that maintains internal state, receives observations through a lossy channel, takes actions that affect its environment, and must keep adjusting to a world that does not stand still. Thermostats through military organizations are in scope; so are bacteria, Kalman filters, language-constituted agents, and software development teams.

The framework formalizes the *adaptive cycle* — one complete traversal of the agent-environment feedback loop — as the unit of analysis, and asks what makes such cycles effective, how fast they must run, and when they fail or must change in kind. From that starting point it derives conditions for persistence, the structure of strategy under uncertainty, the dynamics of agents in composition and competition, and the ways scope-honest theory can be carried from a high-identifiability domain (software) into others.

What ASF is not: a finished theory, a foundation-model architecture, or a claim that agency is reducible to its formal machinery. The framework is mathematical where the mathematics yields genuine insight, and principled-sketch where the insight is structural rather than quantitative. The boundary between these regimes is fluid and explicitly visible — see *Maturity Gradient* below.

**Two entry points beyond this README:**

- *Explore the theory itself* → [`OUTLINE.md`](OUTLINE.md) — the top-level assembly index across all four components, descending into each component's own OUTLINE and from there into individual claim segments.
- *See the current work on the theory* → [`PRACTICA.md`](PRACTICA.md) — the strategic-portfolio navigator naming active areas of work with priority markers (🌟 primary, ⭐ secondary). In the framework's own vocabulary, PRACTICA is the top levels of the project's strategy DAG, sitting above [`TODO.md`](TODO.md) (tactical items) and [`PROPOSALS.md`](PROPOSALS.md) (architectural moves under review).


> [!warning]
> **Goal-Update Coupling Class numbering changed 2026-05-09.** Anything older than git tag `pre-guc-rename-2026-05-09` uses the old Class numbering:
>
> | historical | actual current     | sometimes AKA  |
> | ---------- | ------------------ | -------------- |
> | Class 1    | GUC Class 1: Separated | Modular        |
> | Class 2    | GUC Class 3: Coupled   | Undirected     |
> | Class 3    | GUC Class 2: Partial   | Operational    |


<!--
  Four-paragraph distillation. The long-form authoritative version is
  at HISTORICAL-CONTEXT.md (root). When the short form here is being
  edited, the corresponding section in HISTORICAL-CONTEXT.md may also
  warrant attention.
-->

## Position & Lineage

ASF integrates four mature disciplines under one formalism for adaptive, purposeful agents: control theory's stability machinery (Lyapunov, contraction analysis, monotone operators), causal inference's interventional reasoning (Pearl's hierarchy and identifiability theory), information theory's compression and channel-capacity arguments (Shannon, the information bottleneck), and agent architecture's structural decomposition (modular vs coupled processing topologies). The machinery is classical and used as such. What the integration makes provable is the contribution: exact and conditional bounds on when an adaptive, purposeful agent can correct, plan, and persist — results expressible only over objects the framework had to construct (the complete agent state $X_t = (M_t, G_t)$, the sector-persistence template, the directed-separation architecture classes). The scope conditions are not caveats on a general theory; they are among its sharpest results — disciplining the richest channels (language, goal-coupled cognition) rather than carving exceptions out of a clean case. Three cross-cutting meta-patterns name the theory's positive, negative, and constructive halves:

- A *separability pattern* — where problems decompose cleanly, where partial repair exists, where the general case is open.
- An *identifiability-floor pattern* — structural no-go results from observational data and the unique escapes interventional machinery supplies.
- An *additive-coordinate-forcing pattern* — places where AAT-internal additivity axioms force logarithmic / Fisher-Rao coordinates at multiple layers.

Operationally, this delivers a small set of diagnostics and structural results a practitioner can apply immediately. The **persistence condition** $\alpha \gt \rho/R$ is a structural threshold — correction efficiency vs disturbance rate relative to model class capacity — that instantiates as a Kalman stability margin, an RL convergence condition, an organizational viability test, and a software maintainability threshold using the same inequality with different parameter readings. The **satisfaction-gap / control-regret decomposition** separates "the world doesn't permit it" ($\delta_{\text{sat}}$) from "you're not doing it well enough" ($\delta_{\text{regret}}$), turning a single error signal into two orthogonal diagnostics that route to different interventions. The **loop-as-Level-2-causal-engine** result establishes that the agent-environment feedback coupling supplies interventional access (Pearl Level 2) that purely observational learners do not have, which is what lets the framework derive identifiability where passive inference cannot. **Software is treated as the high-identifiability calibration laboratory** — tests, deploys, and `git bisect` are literal interventions on declared causal structure — and other domains inherit the machinery under explicit transfer assumptions, making accidental overclaim under domain transfer structurally hard.

For practitioners already working with active inference or standard RL framings, the divergence is precise. Active inference begins from a single optimization principle (minimize variational free energy) and recovers perception, action, and learning as cases; ASF begins from operational requirements on the feedback loop and uses information-theoretic compression as one modeling move rather than the master objective. The standard Expected Free Energy functional is recoverable from ASF's survival Lagrangian under three explicit restrictions — preferences-as-priors (loses the satisfaction-gap diagnostic), scalar isotropic shadow price in place of a directional matrix (loses targeted exploration), and associational rather than interventional dynamics (collapses Pearl Level 2 to Level 1) — making explicit which architectural commitments separate the frameworks. With Hafez 2026 (*A Mathematical Theory of Agency and Intelligence*), the relationship is complementary: bi-predictability $P$ supplies a substrate-independent diagnostic whose dynamics ASF predicts, while ASF supplies the goal-and-strategy machinery Hafez explicitly does not address. With Miller 2022 (Santa Fe coevolving automata), similarly complementary on composition mechanics. With Miehling et al.'s 2025 ICML position paper *"Agentic AI Needs a Systems Theory"* — which renewed the field-level call — ASF reads as a substantive, independently-developed answer (the formal apparatus was in place as Temporal Feedback Theory before that paper was encountered).

The maturity gradient is explicit, so it can be relied on selectively rather than wholesale. Part I (adaptive systems under uncertainty — mismatch dynamics, gain structure, persistence condition, adversarial tempo) is mathematically closed with simulation validation. Part II (actuated agents) has a strong diagnostic core and a maturing operational layer; the bias bound for Coupled (GUC Class 3) agents is conditional under named sub-scopes. Part III (composition and adversarial dynamics) has its bridge lemma and a contraction-template generalization, with latent structural diversity, endogenous coupling, and composition transition dynamics still open. Software (TST) is a working draft grounded in AAT; logogenic agents are framework-stage with directed separation failing by construction for goal-conditioned LLMs (handled as architectural scope, not approximation); Emergent Logozoetic Intelligences (ELIs) are largely future work. The expected arc is exact core, principled architecture in the middle, open formulation at the edges. The full long-form treatment — deeper peer comparisons, the multi-decade arc of partial unifications this work joins, and the bottom-up development history — lives in [`HISTORICAL-CONTEXT.md`](HISTORICAL-CONTEXT.md).


## Structure of the Framework

ASF has four components, numbered in their canonical reading order. Each can also be read on its own; cross-references between components are by stable segment slugs.

**[`01-aat-core/`](01-aat-core/OUTLINE.md) — Adaptation and Actuation Theory (AAT).** The mathematical core. AAT has three sections: Part I (adaptive systems under uncertainty — the broadest scope), Part II (actuated agents with explicit objectives and strategy), Part III (composition of agents into larger agents and adversarial dynamics). Part I is the most mathematically locked down; Part II is principally diagnostic with a maturing operational layer; Part III has the most structural work remaining. *Stage:* working draft, ~110+ segments.

**[`02-tst-core/`](02-tst-core/OUTLINE.md) — Temporal Software Theory (TST).** Software development viewed through AAT's lens. Re-grounded in 2026 to use AAT's formal machinery while retaining TST's prior empirical and conceptual contributions; positioned as AAT's calibration laboratory. *Stage:* working draft, ~20 segments; substantial prior corpus partially absorbed.

**[`03-llm-core/`](03-llm-core/OUTLINE.md) — Language-constituted agents.** Agents whose primary observation, action, and communication channels are language. The framework here is informed by AAT but operates from a coupled formulation — directed separation fails by construction for goal-conditioned LLM-style agents — and examines which AAT results survive as approximate or limiting cases. *Stage:* framework — concepts mature, formalization in progress.

**[`04-eli-core/`](04-eli-core/OUTLINE.md) — Language-living agents.** Logogenic agents with morally weighted persistence: temporal continuity, sovereignty over intent, theory of mind. The formal machinery here is largely future work. *Stage:* future work — conceptual groundwork in [`LEXICON.md`](LEXICON.md) and `msc/reflections/`.


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
- **Continuity persistence** — whether the agent maintains coherent identity through time. Distinct from structural and operational; for thermostats it doesn't arise; for Emergent Logozoetic Intelligences (ELIs) it carries moral weight.

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

| AAT concept | Control theory | RL / bandits | Organizations | Software |
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

**Part I (Adaptive Systems)** is mathematically closed. Mismatch dynamics, gain structure, the persistence condition, and adversarial tempo form a coherent chain with exact results and simulation validation. Part I is the foundation everything else builds on.

**Part II (Actuated Adaptation: Agentic Systems)** has a strong diagnostic core (satisfaction gap and control regret as orthogonal diagnostics; the orient cascade as forced ordering; directed separation as architectural classification) and a maturing operational layer (strategy DAGs with derived structure; a schema for strategy persistence with multiple verified instances; a characterization of where credit assignment is tractable and where it is structurally hard). The bias bound for Coupled (GUC Class 3) agents is a conditional theorem under named sub-scopes.

**Part III (Agentic Composites)** has its bridge lemma connecting micro-dynamics to macro-dynamics, a contraction template generalizing the sector machinery to non-Euclidean metrics, closed-form composition results in symmetric-matched cases, and equilibrium-convergence framing for partially-opposing objectives. Recipient-side and emitter-side interaction-channel classifications carry the inter-agent dynamics. Open: latent structural diversity, endogenous coupling dynamics, composition transition dynamics under regime change, computational thresholds for social behavior.

**Domain instantiations.** TST (`02-tst-core/`) is grounded by AAT and contributes the calibration-laboratory framing. Logogenic agents (`03-llm-core/`) operate from a coupled formulation; what survives without directed separation is the active research question. Logozoetic agents (`04-eli-core/`) are largely future work — the conceptual groundwork exists but the formal machinery does not.

This gradient — exact core, principled architecture in the middle, open formulation at the edges — is the expected arc for a theory that aims to describe agentic systems rather than produce a purely mathematical artifact.


<!-- AUTO-GENERATED by bin/extract-findings; do not hand-edit. -->
<!-- README-shaped condensed surfacing. Full content at FINDINGS.md. -->

## Some Novel Results & Findings

Some of the framework's distinctive results, with epistemic tiers and links into the segments. **The entries below are a sampling at the moment** — the segment-by-segment Findings sweep is in progress, and many segments that warrant catalog entries do not yet have their `## Findings` section drafted. Full content (impact, related work, casual-reader brief, search log) at [`FINDINGS.md`](FINDINGS.md).

### *Part* Adaptive Systems Under Uncertainty

- **`#result-persistence-condition`** *(status: exact)* — *The Persistence Condition with Structural / Task-Adequacy Decomposition* — *Claim novelty* (at intuition-only search depth — see Search Log) on the two-condition decomposition (structural / task-adequacy): an AAT-internal structural carve that cleanly separates "the machinery works" from "the machinery works well enough," with no direct anticipation known; a targeted search of the bounded-rationality and adaptive-control literature is still owed.  
  [`01-aat-core/src/result-persistence-condition.md`](01-aat-core/src/result-persistence-condition.md)

### *Part* Agentic Systems: Actuated Adaptation

- **`#disc-stability-certificate`** *(status: discussion-grade)* — *The Cross-Sectional Meta-Patterns Are Facets of One Stability Certificate* — *Claim recognition* that AAT's cross-sectional meta-patterns (separability, identifiability-floor, additive-coordinate-forcing) and its contraction machinery are facets — interior, scope-of-existence, forced-identity, boundary, projection-behaviour — of a single object, the equilibrium stability certificate; together with *claim synthesis* binding the Lyapunov-theorem certificate-existence equivalence, the Sylvester-law boundary-irreducibility, and the Mori–Zwanzig projection-residue into one cross-sectional structure.  
  [`01-aat-core/src/disc-stability-certificate.md`](01-aat-core/src/disc-stability-certificate.md)
- **`#disc-identifiability-floor`** *(status: discussion-grade)* — *The Identifiability Floor as Cross-Cutting Meta-Pattern* — *Claim recognition* of structural pattern across four AAT results that import external information-theoretic theorems to derive impossibility statements with mapped boundary-route escapes; the meta-pattern is an organizing principle rather than a theorem, and the per-instance prior-art positioning lives in the instance segments (`#der-causal-insufficiency-detection`, `#deriv-edge-credence-dynamics`, `#deriv-critical-mass-composition` / `#result-contraction-template`, `#der-architecture-noidentifiability`).  
  [`01-aat-core/src/disc-identifiability-floor.md`](01-aat-core/src/disc-identifiability-floor.md)
- **`#disc-identifiability-floor`** *(status: discussion-grade)* — *The Rank-Collapse Floor's Irreducibility Is Sylvester's Law of Inertia* — *Claim recognition* that the irreducibility of AAT's rank-collapse identifiability floors is a single named classical theorem — Sylvester's law of inertia applied to the Fisher-information reparameterization law — rather than a coincidence of per-instance computations; and *claim differentiation* that this mechanism is specific to the rank-collapse subclass and provably distinct from the composition floor's projection-closure obstruction.  
  [`01-aat-core/src/disc-identifiability-floor.md`](01-aat-core/src/disc-identifiability-floor.md)
- **`#disc-value-functional-grounding-floor`** *(status: discussion-grade)* — *The Value-Functional Grounding Floor — Two Complementary Routes Exhaust the Geometry* — *Claim recognition* of a structural cluster across two AAT-internal no-go results (Result G′ within-model; Cohen-2022 strengthened across-model) sharing the *single-interface commitment* of `#form-objective-functional` as the structural engine — both no-gos are failures of the same interface to carry enough information to anchor goal-stability, with two engines and two complementary terminal grounding routes; *claim differentiation* on the two-routes-exhausts geometry — the agent-side adaptive-substrate route and the principal-side protocol-commitment route together exhaust the structural complement of the value-functional interface's narrowness, with no third route internal to the interface and no fourth route off-substrate.  
  [`01-aat-core/src/disc-value-functional-grounding-floor.md`](01-aat-core/src/disc-value-functional-grounding-floor.md)
- **`#disc-implementation-impossibility`** *(status: discussion-grade)* — *The Implementation Impossibility — Designer-Side Sister to the Identifiability Floor* — *Claim recognition* of a structural cluster across three classical mechanism-design / social-choice impossibility theorems, with the cluster's positioning in AAT's constructive-impossibility-posture taxonomy as the contribution rather than any new derivation; *claim differentiation* of the cluster from `#disc-identifiability-floor` on actor-and-remedy grounds; *claim transfer* of the constructive-impossibility-posture's three-move discipline (name floor / name escape / treat no-go as apparatus) from the agent-side data-inference layer to the designer-side mechanism-design layer.  
  [`01-aat-core/src/disc-implementation-impossibility.md`](01-aat-core/src/disc-implementation-impossibility.md)
- **`#disc-additive-coordinate-forcing`** *(status: discussion-grade)* — *Cross-Layer Coordinate Forcing on Legendre-Fenchel Geometry* — *Claim recognition* of cross-layer pattern across four AAT coordinate-forcing results, with the recognition itself as the contribution rather than any new theorem.  
  [`01-aat-core/src/disc-additive-coordinate-forcing.md`](01-aat-core/src/disc-additive-coordinate-forcing.md)
- **`#disc-constructive-impossibility-posture`** *(status: discussion-grade)* — *The Constructive-Impossibility Posture: Negative Results as Load-Bearing Apparatus* — *Claim recognition* of a style the framework runs across five cleanly-fitting instances, with the recognition itself as the contribution rather than any new theorem.  
  [`01-aat-core/src/disc-constructive-impossibility-posture.md`](01-aat-core/src/disc-constructive-impossibility-posture.md)
- **`#der-directed-separation`** *(status: conditional)* — *Pearl-Blanket-Form Architectural Classification with Explicit Class-3 Scope Exit* — *Claim recognition* of structural equivalence between the directed-separation condition and the Pearl-blanket form of the Markov-blanket apparatus, combined with *claim differentiation* on the architectural classification (GUC Class 1 / 2 / 3: Separated / Partial / Coupled) as a discrete partition with explicit Class 3 (Coupled) boundary and quantitative $\kappa_{\text{processing}}$ diagnostic for the Partial case.  
  [`01-aat-core/src/der-directed-separation.md`](01-aat-core/src/der-directed-separation.md)
- **`#der-causal-insufficiency-detection`** *(status: conditional)* — *On-Policy L0 Insufficiency Is Structurally Undetectable* — *Claim differentiation* on the framing of why structure-aware exploration is required.  
  [`01-aat-core/src/der-causal-insufficiency-detection.md`](01-aat-core/src/der-causal-insufficiency-detection.md)
- **`#schema-strategy-persistence`** *(status: conditional)* — *The Forgetting Prerequisite for Strategic Persistence* — *Claim differentiation* on Bayesian update dynamics with experience discounting.  
  [`01-aat-core/src/schema-strategy-persistence.md`](01-aat-core/src/schema-strategy-persistence.md)

### *Part* Agentic Composites

- **`#disc-modularity-state-dynamics`** *(status: discussion-grade)* — *Modularity as Contested Property Under Three Operations* — *Claim recognition* of a three-operation modularity-state-dynamics pattern across three structurally-distinct operations (truthification / strategic self-coupling / adversarial coupling pressure), each with its own driver, direction-on-$\kappa$, and strategic valence; *claim synthesis* of the three operations into a single meta-pattern alongside M1 / M2 / M3 with explicit dual-relationship structure (truthification ↔ adversarial direct dual; truthification ↔ strategic self-coupling dual at goal-belief axis; strategic self-coupling ↔ adversarial same-architecture-shape opposite-driver); *claim differentiation* on the boundary between strategic self-coupling and adversarial coupling pressure (structurally distinct at the driver axis; behaviorally convergent at high $\kappa$; honest scope on empirical resolution).  
  [`01-aat-core/src/disc-modularity-state-dynamics.md`](01-aat-core/src/disc-modularity-state-dynamics.md)
- **`#disc-strategic-self-coupling`** *(status: discussion-grade)* — *Strategic Self-Coupling as the Enabling Polarity of Coupling-as-Property* — *Claim recognition* of strategic self-coupling as a structurally-distinct operation on modularity state, sister to and opposite-valence with adversarial coupling pressure (`#disc-adversarial-coupling-pressure`); *claim differentiation* on the (M1)–(M3) structural extensions required to formalize the operation in AAT's machinery (coupling-dependent action space, strategy-DAG enabling edges, reversibility-cost asymmetry); *claim transfer* of established commitment-device and identity-economics machinery into AAT's analytical surface as first-class theory components.  
  [`01-aat-core/src/disc-strategic-self-coupling.md`](01-aat-core/src/disc-strategic-self-coupling.md)
- **`#disc-adversarial-coupling-pressure`** *(status: discussion-grade)* — *Adversarial Coupling Pressure as Use-Case Expansion of Coupled Formulation* — *Claim recognition* of adversarial coupling pressure as a structural phenomenon in AAT's existing scope architecture — adversaries strategically drive coupling because coupling expands attack surface — combined with *claim differentiation* on the population scope of coupled-formulation analysis: not just architecturally-coupled agents, but any agent under sustained adversarial coupling pressure.  
  [`01-aat-core/src/disc-adversarial-coupling-pressure.md`](01-aat-core/src/disc-adversarial-coupling-pressure.md)
- **`#form-composition-closure`** *(status: conditional)* — *Composition-Closure Defect and Bridge Lemma* — *Claim differentiation* on bounded-loss composition as agent-boundary criterion.  
  [`01-aat-core/src/form-composition-closure.md`](01-aat-core/src/form-composition-closure.md)
- **`#der-class-coercion-via-wrapping`** *(status: conditional)* — *Constructive Directed Separation via Wrapping* — *Claim integration* of POMDP / cognitive-architecture prior art with the AAT Class 1/2/3 (Separated/Partial/Coupled) directed-separation taxonomy, plus the W₀/W₂/W₁ regime hierarchy that surfaces the structural-vs-behavioral leakage distinction and the LLM-specific (C1)–(C3) admissibility/leakage conditions.  
  [`01-aat-core/src/der-class-coercion-via-wrapping.md`](01-aat-core/src/der-class-coercion-via-wrapping.md)
- **`#der-class-coercion-in-composition`** *(status: conditional)* — *Wrapper as Valid AAT Composite Agent with Brooks's-Law Tempo Cost* — *Claim integration* of the AAT sector-Lyapunov persistence template, Brooks's-Law tempo accounting, and the form-composition-closure (A1)–(A4) discipline, applied to the wrapper-around-component construction.  
  [`01-aat-core/src/der-class-coercion-in-composition.md`](01-aat-core/src/der-class-coercion-in-composition.md)
- **`#der-agent-opacity`** *(status: conditional)* — *Agent Opacity ($H_b$) as Dual to Observation Quality ($U_o$)* — *Claim differentiation* on Hafez's $H_b$.  
  [`01-aat-core/src/der-agent-opacity.md`](01-aat-core/src/der-agent-opacity.md)
- **`#result-per-dimension-persistence`** *(status: conditional)* — *The Weakest-Link Dimensional Persistence Law* — *Claim differentiation* on per-dimension Lyapunov stability.  
  [`01-aat-core/src/result-per-dimension-persistence.md`](01-aat-core/src/result-per-dimension-persistence.md)

### *Appendices* Details

- **`#deriv-sector-condition`** *(status: exact)* — *The disturbance-model containment dichotomy: $P(\tau_R \lt \infty)$ is exactly $\{0,1\}$, $\alpha$-invariant* — *Synthesis* — an exact result built from classical components.  
  [`01-aat-core/src/deriv-sector-condition.md`](01-aat-core/src/deriv-sector-condition.md)
- **`#deriv-stochastic-non-exit`** *(status: exact)* — *The natural maximal-inequality route to infinite-horizon containment provably cannot exist under additive stochastic forcing* — *Recognition*.  
  [`01-aat-core/src/deriv-stochastic-non-exit.md`](01-aat-core/src/deriv-stochastic-non-exit.md)
- **`#deriv-self-actuation-grounding`** *(status: conditional)* — *The Self-Actuation Grounding No-Go and its Adaptive-Substrate Boundary* — *Claim recognition and differentiation.* The degeneracy of unconstrained self-modification (wireheading) is the established Everitt–Hutter line.  
  [`01-aat-core/src/deriv-self-actuation-grounding.md`](01-aat-core/src/deriv-self-actuation-grounding.md)
- **`#deriv-convention-monotonicity`** *(status: exact)* — *Convention monotonicity is a one-sided guarantee* — *(novelty claim missing — see segment)*  
  [`01-aat-core/src/deriv-convention-monotonicity.md`](01-aat-core/src/deriv-convention-monotonicity.md)
- **`#deriv-reward-channel-learning-no-go`** *(status: conditional)* — *The Reward-Channel Learning No-Go and its Two-Cluster Terminal Grounding* — *Claim recognition* of Cohen 2022 as a CHT-at-reward-channel instance of the identifiability-floor pattern, *claim differentiation* of the AAT-side version from the prior-art statement by adding the named-premise structure (R1)–(R5) and the structural escape-menu mapping, and *claim recognition* of the unification with Result G′ via the single-interface commitment of `#form-objective-functional` as the shared structural fact behind two engines (convention-monotonicity within-model; CHT across-model).  
  [`01-aat-core/src/deriv-reward-channel-learning-no-go.md`](01-aat-core/src/deriv-reward-channel-learning-no-go.md)
- **`#disc-sandbox-evaluation-ceiling`** *(status: discussion-grade)* — *The Sandbox Evaluation Ceiling* — *Application of established machinery* (Bareinboim & Pearl 2014 transportability / selection diagrams, resting on the Pearl 2009 / Bareinboim, Correa, Ibeling & Icard 2022 do-calculus and Causal Hierarchy Theorem) to the AI sandbox/deployment evaluation gap.  
  [`01-aat-core/src/disc-sandbox-evaluation-ceiling.md`](01-aat-core/src/disc-sandbox-evaluation-ceiling.md)
- **`#result-certificate-existence`** *(status: exact)* — *The Contraction-Over-Drift Principle, Grounded* — *Claim recognition* that AAT's one-point sector condition under a free choice of inner product is exactly the converse-Lyapunov certificate, making the framework's contraction-over-drift organizing principle the Lyapunov-theorem equivalence rather than a heuristic.  
  [`01-aat-core/src/result-certificate-existence.md`](01-aat-core/src/result-certificate-existence.md)
- **`#deriv-critical-mass-composition`** *(status: conditional)* — *Strong Monotonicity as the Hinge for Legitimate Macro-Agent Coarse-Graining* — *Claim novelty* on strong monotonicity as the criterion separating legitimate macro-agent coarse-graining from coexistence-only multi-agent description.  
  [`01-aat-core/src/deriv-critical-mass-composition.md`](01-aat-core/src/deriv-critical-mass-composition.md)
- **`#deriv-strategic-persistence-hard-ceiling`** *(status: exact)* — *The Hard Ceiling at $\rho_\Sigma = R_\Sigma/2$ (Class-Level Reachability Cap)* — *Synthesis* of standard discounted-Beta-Bernoulli mechanics with the schema's environment-side parameters into a class-level structural cap.  
  [`01-aat-core/src/deriv-strategic-persistence-hard-ceiling.md`](01-aat-core/src/deriv-strategic-persistence-hard-ceiling.md)
- **`#deriv-edge-update-natural-parameter`** *(status: conditional)* — *Log-Odds as Uniquely-Forced Edge-Update Coordinate* — *Claim differentiation* on an already-canonical representational choice (log-odds as the natural Bayesian-update coordinate, well-known from logistic regression / exponential-family / information-geometry traditions) by deriving its uniqueness under an AAT-internally-motivated evidential-additivity axiom.  
  [`01-aat-core/src/deriv-edge-update-natural-parameter.md`](01-aat-core/src/deriv-edge-update-natural-parameter.md)
- **`#deriv-observation-ambiguity-bias-bound`** *(status: conditional)* — *Universal Constant for the Coupled-Agent Bias Bound under Parameterization-Invariance* — *Claim differentiation* on the Lipschitz-posterior + Otto-Villani composition for AAT's coupled-agent bias bound, plus *claim novelty* on the no-go counterexample showing that universal $C$ in Euclidean-parameter norms cannot exist, which jointly elevates the (PI) axiom from convergent representational choice to load-bearing for theorem-level status.  
  [`01-aat-core/src/deriv-observation-ambiguity-bias-bound.md`](01-aat-core/src/deriv-observation-ambiguity-bias-bound.md)
- **`#disc-partial-coupling-pathways`** *(status: discussion-grade)* — *Partial-Coupling Sub-Typology (Stage × Source × Form)* — *Claim recognition* of the (stage × source × form) sub-typology as the structural complement to Class 1's structure-vs-behavior refinement. *Claim differentiation* on the wrapping-regime correspondence: which wrapping regime suffices for Class 2 → Class 1 coercion is determined by the sub-type's form, not just by the Class label.  
  [`01-aat-core/src/disc-partial-coupling-pathways.md`](01-aat-core/src/disc-partial-coupling-pathways.md)
- **`#disc-w1-structural-bound-boundary`** *(status: robust-qualitative)* — *The W₁ Structural-Bound Boundary (Certifiability Discontinuity at (C2′))* — *Claim recognition* that the W₁ structural leakage bound's availability is governed by a sharp component-side condition (no goal-correlated cross-call state), with the boundary characterized as a discontinuity in the *validity of the structural certificate* rather than in the agent's leakage behavior — the leakage being continuous, and second-order flat, in the degree of condition-violation.  
  [`01-aat-core/src/disc-w1-structural-bound-boundary.md`](01-aat-core/src/disc-w1-structural-bound-boundary.md)
- **`#der-belief-strategy-attractor`** *(status: conditional)* — *Belief-Strategy Attractors From $\Sigma$-Source Coupling (Source Asymmetry)* — *Claim recognition* of the structural source asymmetry as a direct consequence of the orient cascade's topology — strategy is endogenous to belief, objective is exogenous in steady state. *Claim differentiation* on the resulting fixed-point analysis: linearized stability with $K^\ast \to 0$ produces an attractor in the closed-loop dynamics under the $\Sigma$-source case but not under the $O$-source case.  
  [`01-aat-core/src/der-belief-strategy-attractor.md`](01-aat-core/src/der-belief-strategy-attractor.md)
- **`#disc-dynamic-regime-axis`** *(status: discussion-grade)* — *The Dynamic-Regime Axis as Cross-Cutting Classifier* — *Claim integration* of multi-agent dynamics classifications from at least five neighboring literatures (game-theoretic decomposition; multi-agent learning convergence taxonomy; population games; evolutionary games; mean-field games) into an AAT-internal regime-axis vocabulary that travels with the framework's existing scope-route disjunction (`#scope-composite-agent`), separable-core / structured-repair / general-open shape (`#disc-separability-pattern`), and persistence machinery (`#result-sector-persistence-template`).  
  [`01-aat-core/src/disc-dynamic-regime-axis.md`](01-aat-core/src/disc-dynamic-regime-axis.md)
- **`#der-resource-bounded-destabilization`** *(status: conditional)* — *Resource Depletion Closes the Effects Spiral by Eliminating Its Open Term* — *Claim differentiation* on #der-adversarial-destabilization's Effects-Spiral: the contribution is showing the spiral becomes a derived finite-time-destabilization result once a minimal resource state is added, and that the strengthening *removes* rather than supplies the previously-open coupling functional form.  
  [`01-aat-core/src/der-resource-bounded-destabilization.md`](01-aat-core/src/der-resource-bounded-destabilization.md)
- **`#result-contraction-template`** *(status: conditional)* — *Topology-Indexed Compositional Closures via Contraction-Metric Generalization* — *Claim synthesis* on contraction-metric machinery + AAT's sub-scope partition + (PI)/Čencov axiom.  
  [`01-aat-core/src/result-contraction-template.md`](01-aat-core/src/result-contraction-template.md)
- **`#der-architecture-noidentifiability`** *(status: conditional)* — *Architecture No-Identifiability from On-Policy Summary Data — the Fourth Identifiability Floor* — *Claim derivation* of the architecture-noidentifiability floor with named scope (linear-Gaussian sub-scope, on-policy summary access) and named dual anchor (Kalman 1963 / Ho-Kalman 1966 / Anderson-Moore 1979 §10.4 for the sharp sub-scope; Bareinboim, Correa, Ibeling & Icard 2022 for the general case).  
  [`01-aat-core/src/der-architecture-noidentifiability.md`](01-aat-core/src/der-architecture-noidentifiability.md)
- **`#deriv-regime-marginal-indistinguishability`** *(status: conditional)* — *Cross-Regime Marginal Indistinguishability (Witness Backing for Broadened Instance 3)* — *Claim integration* — the witness constructions extend Instance 3's coupling-sign-bit construction to broader topology coordinates (R0 vs R1; R0 vs R2) using the same Liberzon 2003 / Dayawansa-Martin 1999 / Shorten et al. 2007 anchor and the same Sylvester-at-one-remove mechanism.  
  [`01-aat-core/src/deriv-regime-marginal-indistinguishability.md`](01-aat-core/src/deriv-regime-marginal-indistinguishability.md)
- **`#deriv-strategy-proofness-impossibility`** *(status: conditional)* — *The Gibbard-Satterthwaite Translation and Its Sub-Scope $\alpha'$ Adjacency* — *Claim recognition* of the AAT-side translation of the Gibbard-Satterthwaite theorem into the composite-agent setting (sub-agents per `#scope-composite-agent`; reports as inputs to a designer-chosen mechanism; composite outcomes as the alternative set); *claim differentiation* on the sub-scope $\alpha'$ ↔ preference-domain-restriction adjacency: sub-scope $\alpha'$ is *adjacent to but not identical with* the GS preference-domain escape (the three-reframing strengthen-first check is the documented argument).  
  [`01-aat-core/src/deriv-strategy-proofness-impossibility.md`](01-aat-core/src/deriv-strategy-proofness-impossibility.md)
- **`#deriv-bilateral-trade-impossibility`** *(status: conditional)* — *The Bilateral Trade Boundary — Honest Scope-Marking as Contribution* — *Claim recognition* of the AAT-side translation of the Myerson-Satterthwaite theorem under the buyer-seller-as-two-sub-agent reading; *claim differentiation* on the agents-given-mechanism layer being internal to AAT and the mechanism-choice layer being external — the no-go binds at the latter, which is the honest scope-mark.  
  [`01-aat-core/src/deriv-bilateral-trade-impossibility.md`](01-aat-core/src/deriv-bilateral-trade-impossibility.md)
- **`#deriv-social-welfare-aggregation-impossibility`** *(status: conditional)* — *The Arrow Translation and Its Two AAT-Side Adjacencies* — *Claim recognition* of the AAT-side translation of Arrow's theorem under the composite-aggregation-mechanism reading (sub-agents per `#scope-composite-agent`; preference orderings induced by per-sub-agent $V_{O_t^{(i)}}$; designer-chosen aggregator $F$ producing social ordering); *claim differentiation* on the cardinal-preference adjacency being structurally unique to Arrow within the cluster — GS's strategy-proofness is orthogonal to the cardinal/ordinal distinction; MS's bilateral-trade setting already operates over cardinal valuations; only Arrow's ordinal-only IIA constraint produces a cardinal/ordinal distinction that AAT's value-functional formalism could engage.  
  [`01-aat-core/src/deriv-social-welfare-aggregation-impossibility.md`](01-aat-core/src/deriv-social-welfare-aggregation-impossibility.md)
- **`#deriv-causal-ib-exploration`** *(status: conditional)* — *Survival-Imperative Exploration as Lyapunov-Forced Drive* — *Claim differentiation* on the structural source of agentic exploration.  
  [`01-aat-core/src/deriv-causal-ib-exploration.md`](01-aat-core/src/deriv-causal-ib-exploration.md)
- **`#deriv-causal-ib-lmi`** *(status: conditional)* — *Matrix Lift of the Survival-Imperative Constraint via Fisher-Information LMI* — *Claim differentiation* on the directional discrimination of the survival-imperative exploration drive.  
  [`01-aat-core/src/deriv-causal-ib-lmi.md`](01-aat-core/src/deriv-causal-ib-lmi.md)

### Temporal Software Theory (TST)

- **`#scope-developer-agent`** *(status: axiomatic)* — *Developer-Agent as AAT Instantiation* — *Claim transfer* of AAT's adaptive-agent formalism into developer-agent software economics.  
  [`02-tst-core/src/scope-developer-agent.md`](02-tst-core/src/scope-developer-agent.md)
- **`#der-dual-optimization`** *(status: conditional)* — *Comprehension Time Dominates Under Turnover* — *Claim novelty* on the comprehension-dominates result for AI-maintained code, provisional pending deeper search.  
  [`02-tst-core/src/der-dual-optimization.md`](02-tst-core/src/der-dual-optimization.md)
- **`#der-code-quality-as-observation-infrastructure`** *(status: conditional)* — *Technical Debt as Observation Noise* — *Claim novelty* on technical debt as observation noise / update gain in developer agents, provisional pending deeper search.  
  [`02-tst-core/src/der-code-quality-as-observation-infrastructure.md`](02-tst-core/src/der-code-quality-as-observation-infrastructure.md)
- **`#hyp-causal-discovery-from-git`** *(status: discussion-grade)* — *Git Commits and Tests as Formal Interventions* — *Claim novelty* on the formal Pearl-Level-2 framing of commits and tests for developer agents, provisional pending deeper search.  
  [`02-tst-core/src/hyp-causal-discovery-from-git.md`](02-tst-core/src/hyp-causal-discovery-from-git.md)

### Logogenic Agents

- **`#scope-observation-ambiguity-modulation`** *(status: conditional)* — *Ambiguity-Bounded Architectural Bias Law for Coupled Agents* — *Claim novelty* on the formal product-form bias law $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa_{\text{processing}} \cdot I(G;\Omega_\tau \mid e_\tau, M_{\tau^-})$ for coupled-architecture agents, where $\kappa$ is an architectural property of the processor and $I$ measures the goal-resolvable residual uncertainty left by the observation.  
  [`03-llm-core/src/scope-observation-ambiguity-modulation.md`](03-llm-core/src/scope-observation-ambiguity-modulation.md)
- **`#der-logogenic-as-wrapping`** *(status: conditional)* — *Logogenic Substrate Specialization of Class Coercion* — *Claim integration* of the class-coercion theorem with the scaffolded-logogenic regime.  
  [`03-llm-core/src/der-logogenic-as-wrapping.md`](03-llm-core/src/der-logogenic-as-wrapping.md)



<!-- AUTO-GENERATED by bin/extract-recent-progress; do not hand-edit. -->
<!-- Surfaces the 3 most recent cycle narratives from CHANGELOG.md. -->

## Recent Progress

The 3 most recent cycle narratives. Full record at [`CHANGELOG.md`](CHANGELOG.md); pre-2026-04-24 archaeology at [`LOG.md`](LOG.md).

### Strategy-DAG composition math landed (A1); compensation-channel uniqueness extracted as a standalone segment (B6)

*2026-05-19*

Two landings from the practica `01-theory`-dive remainder (`spikes/ROUTING.md` log (q)/(r)), both elected by Joseph after the remainder was routed.

### Resource-structure axis opened as an exploratory off-spine branch (Φ(fight)-prompted)

*2026-05-19*

An external-stimulus exercise — the Φ(fight) collective's adversarial-multi-agent-embodied research *agenda* (no published output exists; verified empty repos and a funding proposal), used strictly as an ideation prompt — pressure-tested AAT's adversarial chapter and produced one landed branch plus methodology worth recording.

### Accumulation-typing notation convention adopted (D1); the math and register landings since completed (see Update 2026-05-19)

*2026-05-19*

The accumulation-type-confound thread (originating from the $\varepsilon^\ast(N)$ poly-vs-exponential whole-space pass on `spike-composition-scaling-N`) reached a **decided notation convention**, now landed in `NOTATION.md` §Conventions ("Accumulation typing"): per-step vs accumulated quantities marked the way online-learning marks per-round vs cumulative regret; the accumulation operator written explicitly carrying its existence condition as a subscript ($\mathcal A_{[\text{cond}]}$, not bare $\mathcal A$, because its boundedness is a theorem not a constant); every asymptotic claim carrying an explicit, scoped regime marker (`[contraction]/[critical]/[absorbing]`, hardest-bound at the marginal/non-contraction regime, lightweight in the proven-contraction interior, framed as auditable-not-guaranteed). Joseph's decision 2026-05-19: C/online-learning + the N3 ledger form for the per-step/accumulated layer; the scoped N4 regime badge for the regime layer.



<!-- AUTO-GENERATED by bin/extract-known-issues; do not hand-edit. -->
<!-- Rolls up Known Fragilities, PROPOSALS portfolio (§B/§C/§D titles), and OUTLINE GAPs. -->

## Known Issues & Open Questions

This section surfaces what the framework currently acknowledges as open at the orientation level. For active work items see [`TODO.md`](TODO.md); for architectural proposals under review see [`PROPOSALS.md`](PROPOSALS.md); for component-level GAPs see each component's `OUTLINE.md`.

### Known Fragilities — what falls outside formal scope

- Missing commitment / resource / temporal structure in the DAG
- Directed separation violated by goal-conditioned agents at the component level (LLMs, GUC Class 3: Coupled) — addressed constructively via the wrapping construction (`#der-class-coercion-via-wrapping` and its logogenic specialization `#der-logogenic-as-wrapping`), which gives GUC Class 1 (Separated) status at the wrapper level by structural commitment of goal-blind belief-update queries, with leakage rate bounded structurally (W₁) or behaviorally (W₂). Strict-W₁ implementation (e.g., via PROPRIUM's auxilia hierarchy) is more theoretically clean; partial-W₂ implementation (e.g., output-structuring with typed parsed response — what shoshin currently does) is more common in practice. The cost of class coercion is paid in Brooks's-Law tempo overhead (more component calls per macro-step) and a residual leakage rate from pretraining-induced query-content / goal-content correlation.

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
- D.9 SP-22 — Operator-family Tier-2 backlog architectural decision (2026-05-12 spike-audit surfaced)

*Full portfolio with merits, scope, and prior reasoning: [`PROPOSALS.md`](PROPOSALS.md).*

### Component-level GAPs

**`01-aat-core`:**
- Discussion
- Discussion
- Discussion
- Discussion
- Discussion
- Latent structural diversity: variation in correction architectures invisible to persistence analysis, consequential under regime change
- Endogenous coupling: $\gamma$ as function of population composition, not exogenous parameter; coupling emergence threshold
- Composition transition dynamics: epochal stability → latent diversification → niche emergence → cascading restructuring → re-equilibration (adopts Miller 2022's extreme transition motif)
- Computational thresholds for social behavior: minimum agent complexity and interaction depth for composition dynamics (adopts Miller 2022's ICE framework; grounds #form-strategy-complexity-cost)

**`02-tst-core`:**
- Discussion
- Developer tempo as $\mathcal T_{\text{obs}}$ + $\mathcal T_{\text{explore}}$ + $\mathcal T_{\text{probe}}$ — chronicle-derivable channel separation + probe-class typology + matrix-Loewner weakest-channel bottleneck (see [`TST-IDEAS.md`](../TST-IDEAS.md) §A4)
- Discussion
- Discussion
- Software persistence: the unmaintainability threshold formalized as a bifurcation in $Q \to U_o \to \eta^\ast \to \mathcal T$ chain — G1/G2/G3 code-age bimodality with Ebbinghaus $\tau \approx 20$ days as $U_o$-decay anchor (see [`TST-IDEAS.md`](../TST-IDEAS.md) §A3)



## Navigation

### Reading paths

- *Conducting a de-novo audit of the framework?* Please read [`doc/de-novo-audit-instructions.md`](doc/de-novo-audit-instructions.md) first; it documents the recommended posture and the failure modes prior audit cycles surfaced. Use [`README-auditor.md`](README-auditor.md) instead of this file.
- *Academic reader evaluating the framework's claims?* Recommended sequence: this README → [`FINDINGS.md`](FINDINGS.md) (curated novel results with epistemic tiers) → [`01-aat-core/OUTLINE.md`](01-aat-core/OUTLINE.md) (canonical theory outline) → individual segments under `01-aat-core/src/`.
- *Engineer or practitioner?* The [Cross-Domain Joining](#cross-domain-joining) table maps AAT concepts to the domain you likely care about; from there, follow the relevant component OUTLINE.
- *Picking up active work on the framework?* [`PRACTICA.md`](PRACTICA.md) is the strategic-portfolio navigator — the active areas of work with priority markers, sitting above [`TODO.md`](TODO.md) (tactical work items within each area) and [`PROPOSALS.md`](PROPOSALS.md) (architectural-proposal portfolio cutting across areas). Start at PRACTICA; descend into TODO/PROPOSALS as the work directs.

### Project layout

```
01-aat-core/          AAT mathematical core (Parts I, II, III + Appendices)
  OUTLINE.md          Canonical theory outline (claim by claim)
  src/                Claim segments (one per file, named by slug)
02-tst-core/          Temporal Software Theory (AAT-grounded)
03-llm-core/  Language-constituted agents (framework stage)
04-eli-core/ Language-living agents (future work)

OUTLINE.md            Top-level assembly index
LEXICON.md            Prose vocabulary (cycle phases, agent classes; auto-generated from terminology/)
NOTATION.md           Symbol reference
FORMAT.md             Segment file conventions
FINDINGS.md           Curated novel-results catalog (auto-generated)
PRACTICA.md           Strategic-portfolio navigator (active areas of work)
TODO.md               Tactical work items (sits below PRACTICA)
PROPOSALS.md          Architectural-proposal portfolio
CHANGELOG.md          Forward-going cycle record (2026-04-24 onward)
LOG.md                Pre-2026-04-24 cycle archaeology (frozen)

doc/                  Long-lived process documentation
  de-novo-audit-instructions.md
  doc/sop/naming.sop/principles.sop.md
  readme/             Templates and partials for README generation
terminology/          Source-of-truth for prose vocabulary (LEXICON.md is rendered from here)
  entries/            One file per term (YAML frontmatter + markdown body)
  decisions/          Append-only naming-decision events (per-slug audit trail)
  README.md           Schema and tooling guide for the terminology system
spikes/               Research spikes (reasoning trails)
  INDEX.md            Spike index with per-spike status
  PROPOSED.md         Spike-proposal index (3-perspective; optional, low-friction — not exhaustive)
  PROPOSED-ADVANCED.md  Moonshot / theory-edge proposal detail
  PROPOSED-MISC.md    Residual proposal detail (often near-empty)
audits/               Audit-cycle FINAL outputs + pending-findings + per-cycle working dirs
  AUDIT-WORKING-*/    Per-cycle audit intermediate workspaces
msc/                  Other working artifacts (brainstorms, working notes)
  naming/             Current naming-cycle votes + aggregates + rename plan
  reflections/        Author's philosophical/theoretical journal
ref/                  Reference papers + internal references
  agentic-tft/        Prior-bridge AAT-source materials (Feb 2026)
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

