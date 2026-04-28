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


## For Auditors

**You are reading the auditor-facing README.** This version of the project README is intentionally narrower than [`README.md`](README.md) — sections that would prime a de-novo audit (specific novel-results claims, recent cycle narrative, known-issues list, recently-landed architectural moves) have been removed.

If you are conducting a de-novo audit, please read [`doc/de-novo-audit-instructions.md`](doc/de-novo-audit-instructions.md) before going further. It documents the audit posture, the source-ordering convention (segments first; `msc/`, `ref/`, git only when grounding requires it), and the failure modes prior audit cycles have surfaced.

The following files carry priming content and are best read only after your audit is complete, when the explicit purpose is to compare your independent findings against the project's existing record:

- `README.md` — the public README (has Findings, Recent Progress, Known Issues sections)
- `HISTORICAL-CONTEXT.md` — long-form positioning document with peer-framework comparisons that name specific contested positions
- `FINDINGS.md` — curated novel-results catalog
- `CHANGELOG.md` — cycle-by-cycle narrative of what has been judged settled
- `LOG.md` — pre-2026-04-24 cycle archaeology
- `TODO.md` — active and archived findings, including the "settled" framings of prior cycles
- `PROPOSALS.md` — architectural-proposal portfolio with prior-reasoning trails
- `doc/readme/src/_findings-summary.md`, `_recent-progress.md`, `_known-issues.md` — the auto-generated live includes underlying the public README
- `msc/pending-findings-*.md`, `msc/audit-*.md` — prior-cycle audit working documents

Reading these is not forbidden — nothing in this project is — but tends to bias toward ideas previous auditors have already heavily visited, and that's not in the spirit of a *de novo* audit. The most useful contributions from a fresh pass come from genuinely-fresh perspectives.


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
msc/                  Working documents, spikes, brainstorms
  SPIKES.md           Spike index
ref/                  Reference papers
bin/                  Build, lint, generation scripts
_obs/                 Superseded materials
```


## Contributing

ASF is research-stage work; contributions take a few specific forms.

**Engaging with the theory.** The most valuable contribution is *de-novo evaluation*: read segments without first reading existing audits or pending findings, form independent judgments, and surface what you find. Where you disagree with a claim or its scope, that is signal. Procedure: see [`doc/de-novo-audit-instructions.md`](doc/de-novo-audit-instructions.md). Read [`README-auditor.md`](README-auditor.md) instead of this README for the audit-safe framing.

**Adding theory content.** Segments are added under `{component}/src/` following [`FORMAT.md`](FORMAT.md) conventions: YAML frontmatter (slug, type, status, dependencies); one-sentence summary; Formal Expression with epistemic tags; Epistemic Status; Discussion; optional Findings; optional Working Notes. Promotion follows a four-gate workflow detailed in FORMAT.md. Slugs follow `{type-prefix}-{subject-noun}` and are aligned mechanically by [`bin/align-slug`](bin/align-slug).

**Spikes.** Speculative or in-progress work that is not yet ready for segment promotion lives under `msc/spike-{topic}.md`. Spikes are honest reasoning trails; results that promote out of spikes land in segments per the math-lives-in-segments discipline.

**Tooling.** Internal process scripts (build, extract, lint) are written in Ruby; community-facing tooling (simulations, reproducibility scripts) is written in Python. New scripts in `bin/` follow this convention; existing scripts that don't are not retroactively rewritten.

**Editing this README.** This file is *auto-generated* from partials under [`doc/readme/src/`](doc/readme/src/) via [`bin/build-readme`](bin/build-readme). Direct edits to `README.md` will be overwritten on the next build. To change README content, edit the relevant partial (`doc/readme/src/_<name>.md`) and re-run `bin/build-readme`, or run [`bin/refresh-all`](bin/refresh-all) to also regenerate the auto-extracted partials (`_findings-summary.md`, `_recent-progress.md`, `_known-issues.md`). Templates live in `doc/readme/*.liquid` and only change when the section *order* or *set* changes. The same discipline applies to `README-auditor.md`.

**Reporting issues.** Open an issue on GitHub or contact the project maintainer (see commit history).

