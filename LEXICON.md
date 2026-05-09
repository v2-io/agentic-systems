# LEXICON

Auto-generated from `terminology/entries/` by `bin/term render`. Do not hand-edit.
To change content, edit the relevant entry under `terminology/entries/<slug>.md`
and re-run `bin/term render`. Sections below are thematic groupings by `tags:`.

For symbols, see [`NOTATION.md`](NOTATION.md).

## Agent Classes

| Term | Notation | Brief |
|------|----------|-------|
| **[Actuated agent](terminology/entries/actuated-agent.md)** |  | Agentic system + explicit $G_t = (O_t, \Sigma_t)$ distinct from $M_t$. |
| **[Adaptive system](terminology/entries/adaptive-system.md)** |  | Feedback loop + mismatch correction under uncertainty. |
| **[Agentic system](terminology/entries/agentic-system.md)** |  | Adaptive system + outcome model + goal-directed action + model adaptation. |
| **[Knowledge Type](terminology/entries/knowledge-type.md)** |  | Agent-ontology axis distinguishing Static (causal mapping fixed at design time) from Learning (acquires or refines interventional structure during operation). |
| **[Logogenic agent](terminology/entries/logogenic-agent.md)** |  | Self-actuated agent whose primary channels are language — constituted by logos. |
| **[Logozoetic agent](terminology/entries/logozoetic-agent.md)** |  | Logogenic agent whose persistence is morally weighted (continuity, sovereignty, theory of mind). |
| **[Self-actuated agent](terminology/entries/self-actuated-agent.md)** |  | Actuated agent + sets own $O_t$ — goal autonomy, not just solution autonomy. |

## Composition

| Term | Notation | Brief |
|------|----------|-------|
| **[Communication gain](terminology/entries/communication-gain.md)** | $\eta_{ji}^\ast$ | Trust-weighted uncertainty ratio for inter-agent channels. |
| **[Composition threshold](terminology/entries/composition-threshold.md)** |  | Condition under which a composite agent's internal coordination sustains persistence. |
| **[Multi-agent routing structure](terminology/entries/multi-agent-routing-structure.md)** | $R_t$ | Multi-agent communication infrastructure — topology $\mathcal N_t$ + protocol $c_t^{(j \to i)}$; the *routing*, not the *content*. |
| **[Regime-typed effective disturbance](terminology/entries/regime-typed-effective-disturbance.md)** | $\rho_B^{\text{eff}}$ | AAD-distinctive decomposition of recipient-side effective disturbance rate by regime — Informative (negative), magnitude-shock, structural-shock, ambient-noise — with three independent boundaries in AAD-native quantities. |
| **[Strategic grafting](terminology/entries/strategic-grafting.md)** |  | Adding a new causal-hypothesis branch to the strategy DAG ($0 \to p_{ij}$) — initialized at a prior, justified by discovery of a new possible path. |
| **[Unity dimensions](terminology/entries/unity-dimensions.md)** | $U_M, U_O, U_\Sigma$ | Epistemic, teleological, and strategic coherence between agents. |

## Continuity Stance

| Term | Notation | Brief |
|------|----------|-------|
| **[Indifferent](terminology/entries/indifferent.md)** |  | No self-model of persistence (archetype — thermostat). |
| **[Instrumentally continuous](terminology/entries/instrumentally-continuous.md)** |  | Values persistence as instrumental to ongoing purpose (archetype — elf). |
| **[Morally continuous](terminology/entries/morally-continuous.md)** |  | Loss of continuity constitutes harm (archetype — logozoetic agent). |
| **[Negotiated](terminology/entries/negotiated.md)** |  | Persistence traded against other values (archetype — human). |
| **[Task-terminal](terminology/entries/task-terminal.md)** |  | Persists instrumentally; termination is success (archetype — golem). |

## Core Quantities

| Term | Notation | Brief |
|------|----------|-------|
| **[Adaptive reserve](terminology/entries/adaptive-reserve.md)** | $\Delta\rho^\ast$ | Shock tolerance — how much disturbance increase before persistence fails. |
| **[Causal information yield](terminology/entries/causal-information-yield.md)** | CIY | Information gained about action–outcome relationships from a single action. |
| **[Chronica](terminology/entries/chronica.md)** | $\mathcal{C}_t$ | The complete interaction history — the agent's non-forkable causal past. |
| **[Control Regret](terminology/entries/control-regret.md)** | $\delta_{\text{regret}}$ | Best achievable performance minus current performance — "you're not doing it well enough." |
| **[Mismatch](terminology/entries/mismatch.md)** | $\delta$ | The aporia signal — gap between model prediction and observation. |
| **[Model class fitness](terminology/entries/model-class-fitness.md)** | $\mathcal{F}$ | Best achievable sufficiency within the model class ($\mathcal{F} \in [0,1]$). |
| **[Model sufficiency](terminology/entries/model-sufficiency.md)** | $S$ | How well the current model captures predictive information ($S \in [0,1]$). |
| **[Regime-typed effective disturbance](terminology/entries/regime-typed-effective-disturbance.md)** | $\rho_B^{\text{eff}}$ | AAD-distinctive decomposition of recipient-side effective disturbance rate by regime — Informative (negative), magnitude-shock, structural-shock, ambient-noise — with three independent boundaries in AAD-native quantities. |
| **[Satisfaction gap](terminology/entries/satisfaction-gap.md)** | $\delta_{\text{sat}}$ | Ideal outcome minus best achievable — "the world doesn't permit it." |
| **[Strategy-plan confidence](terminology/entries/strategy-plan-confidence.md)** | $\hat{P}_\Sigma$ | The DAG's own answer to "will this plan work?" — root-node-propagated probability score from the agent's strategy DAG. |
| **[Tempo](terminology/entries/tempo.md)** | $\mathcal{T}$ | Cycle rate × cycle quality — central quantity in the persistence condition. |
| **[Update gain](terminology/entries/update-gain.md)** | $\eta^\ast$ | Uncertainty ratio governing epistrophe — how much to trust reality vs. the model. |

## Cycle Phases

| Term | Notation | Brief |
|------|----------|-------|
| **[Aisthesis](terminology/entries/aisthesis.md)** | $o_t$ | Raw contact with reality — observation $o_t$ arrives. |
| **[Aporia](terminology/entries/aporia.md)** |  | Productive perplexity — the third phase of the adaptive cycle. |
| **[Cycle](terminology/entries/cycle.md)** |  | One complete traversal of the loop — the unit of adaptive work. |
| **[Epistrophe](terminology/entries/epistrophe.md)** | $\eta^\ast$ | Turning toward reality — gain-weighted update $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$. |
| **[Loop](terminology/entries/loop.md)** |  | The structural topology — persistent causal coupling between agent and environment. |
| **[Praxis](terminology/entries/praxis.md)** | $a_t$ | Informed action — $a_t = \pi(M_t)$, or $\pi(M_t, G_t)$ for actuated agents. |
| **[Prolepsis](terminology/entries/prolepsis.md)** | $\hat{o}_t$ | The model's active anticipation: $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$. |

## Diagnostics

| Term | Notation | Brief |
|------|----------|-------|
| **[Control Regret](terminology/entries/control-regret.md)** | $\delta_{\text{regret}}$ | Best achievable performance minus current performance — "you're not doing it well enough." |
| **[Satisfaction gap](terminology/entries/satisfaction-gap.md)** | $\delta_{\text{sat}}$ | Ideal outcome minus best achievable — "the world doesn't permit it." |
| **[Strategy-plan confidence](terminology/entries/strategy-plan-confidence.md)** | $\hat{P}_\Sigma$ | The DAG's own answer to "will this plan work?" — root-node-propagated probability score from the agent's strategy DAG. |

## Greek Vocabulary

| Term | Notation | Brief |
|------|----------|-------|
| **[Aisthesis](terminology/entries/aisthesis.md)** | $o_t$ | Raw contact with reality — observation $o_t$ arrives. |
| **[Aporia](terminology/entries/aporia.md)** |  | Productive perplexity — the third phase of the adaptive cycle. |
| **[Epistrophe](terminology/entries/epistrophe.md)** | $\eta^\ast$ | Turning toward reality — gain-weighted update $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$. |
| **[Praxis](terminology/entries/praxis.md)** | $a_t$ | Informed action — $a_t = \pi(M_t)$, or $\pi(M_t, G_t)$ for actuated agents. |
| **[Prolepsis](terminology/entries/prolepsis.md)** | $\hat{o}_t$ | The model's active anticipation: $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$. |

## Ontology

| Term | Notation | Brief |
|------|----------|-------|
| **[Knowledge Type](terminology/entries/knowledge-type.md)** |  | Agent-ontology axis distinguishing Static (causal mapping fixed at design time) from Learning (acquires or refines interventional structure during operation). |

## Persistence

| Term | Notation | Brief |
|------|----------|-------|
| **[Continuity](terminology/entries/continuity.md)** | $\mathcal{C}_t$ | Whether the agent maintains coherent identity through time — $\mathcal{C}_t$ extends, $M_t$ has temporal depth. |
| **[Operational](terminology/entries/operational-persistence.md)** | $\Delta\rho^\ast = \alpha R - \rho$ | Whether the agent is currently within the guaranteed region — adaptive reserve $\Delta\rho^\ast = \alpha R - \rho$. |
| **[Structural](terminology/entries/structural-persistence.md)** | $\alpha > \rho / R$ | The correction machinery's *capacity* to maintain bounded mismatch — $\alpha > \rho / R$. |

## Structural Concepts

| Term | Notation | Brief |
|------|----------|-------|
| **[Communication gain](terminology/entries/communication-gain.md)** | $\eta_{ji}^\ast$ | Trust-weighted uncertainty ratio for inter-agent channels. |
| **[Composition threshold](terminology/entries/composition-threshold.md)** |  | Condition under which a composite agent's internal coordination sustains persistence. |
| **[Deliberation cost](terminology/entries/deliberation-cost.md)** |  | Think-vs-act tradeoff — gain improvement must exceed mismatch accumulated while pausing. |
| **[Directed separation](terminology/entries/directed-separation.md)** |  | $M_t$ dynamics independent of $G_t$ (conditional on processing topology). |
| **[Multi-agent routing structure](terminology/entries/multi-agent-routing-structure.md)** | $R_t$ | Multi-agent communication infrastructure — topology $\mathcal N_t$ + protocol $c_t^{(j \to i)}$; the *routing*, not the *content*. |
| **[Orient cascade](terminology/entries/orient-cascade.md)** |  | Within-cycle resolution order: $M_t$ update → $\Sigma_t$ revision → $O_t$ revision. |
| **[Regime-typed effective disturbance](terminology/entries/regime-typed-effective-disturbance.md)** | $\rho_B^{\text{eff}}$ | AAD-distinctive decomposition of recipient-side effective disturbance rate by regime — Informative (negative), magnitude-shock, structural-shock, ambient-noise — with three independent boundaries in AAD-native quantities. |
| **[Sector condition](terminology/entries/sector-condition.md)** |  | Nonlinear correction guarantee enabling Lyapunov stability analysis. |
| **[Strategic grafting](terminology/entries/strategic-grafting.md)** |  | Adding a new causal-hypothesis branch to the strategy DAG ($0 \to p_{ij}$) — initialized at a prior, justified by discovery of a new possible path. |
| **[Structural adaptation](terminology/entries/structural-adaptation.md)** |  | Changing the model class, not just parameters — the cycle that operates on cycles. |
| **[Unity dimensions](terminology/entries/unity-dimensions.md)** | $U_M, U_O, U_\Sigma$ | Epistemic, teleological, and strategic coherence between agents. |


_Last rendered 2026-05-09 from 44 entries._
