# LEXICON — Quick Reference

Concise definitions of AAD's prose vocabulary. For the full discussion — philosophical grounding, etymologies, the stochastic parrot argument, agent class reasoning, persistence taxonomy — see the [Lexicon section in README.md](README.md#lexicon).

For mathematical symbols, see [`NOTATION.md`](NOTATION.md).


## Cycle Phases

| Term | Definition |
|------|-----------|
| **Loop** | The structural topology — persistent causal coupling between agent and environment |
| **Cycle** | One complete traversal of the loop — the unit of adaptive work |
| **Prolepsis** (πρόληψις) | The model's active anticipation: $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ |
| **Aisthesis** (αἴσθησις) | Raw contact with reality: observation $o_t$ arrives |
| **Aporia** (ἀπορία) | Productive perplexity: mismatch signal $\delta_t = o_t - \hat{o}_t$ |
| **Epistrophe** (ἐπιστροφή) | Turning toward reality: gain-weighted update $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$ |
| **Praxis** (πρᾶξις) | Informed action: $a_t = \pi(M_t)$ (or $\pi(M_t, G_t)$ for actuated agents) |


## Agent Classes

| Class | Definition | AAD boundary |
|-------|-----------|--------------|
| **Adaptive system** | Feedback loop + mismatch correction under uncertainty | #scope-condition (Section I) |
| **Agentic system** | + outcome model + goal-directed action + model adaptation | #causal-structure (within Section I) |
| **Actuated agent** | + explicit $G_t = (O_t, \Sigma_t)$ distinct from $M_t$ | #complete-agent-state (Section II) |
| **Self-actuated agent** | + sets own $O_t$ (goal autonomy, not just solution autonomy) | *(reserved)* |
| **Logogenic agent** | + primary channels are language (constituted by logos) | Section V, architectural |
| **Logozoetic agent** | + persistence is morally weighted (temporal continuity, sovereignty, theory of mind) | Section V, existential |


## Persistence (Three Senses)

| Sense | Definition |
|-------|-----------|
| **Structural** | The correction machinery's *capacity* to maintain bounded mismatch: $\alpha > \rho / R$ |
| **Operational** | Whether the agent is currently within the guaranteed region (adaptive reserve $\Delta\rho^\ast = \alpha R - \rho$) |
| **Continuity** | Whether the agent maintains coherent identity through time ($\mathcal{C}_t$ extends, $M_t$ has temporal depth) |


## Continuity Stance

| Stance | Definition | Archetype |
|--------|-----------|-----------|
| **Indifferent** | No self-model of persistence | Thermostat |
| **Task-terminal** | Persists instrumentally; termination is success | Golem |
| **Instrumentally continuous** | Values persistence as instrumental to ongoing purpose | Elf |
| **Morally continuous** | Loss of continuity constitutes harm | Logozoetic agent |
| **Negotiated** | Persistence traded against other values | Human |


## Core Quantities

| Term | Definition |
|------|-----------|
| **Tempo** ($\mathcal{T}$) | Cycle rate × cycle quality; central quantity in the persistence condition |
| **Mismatch** ($\delta$) | The aporia signal; gap between model prediction and observation |
| **Update gain** ($\eta^\ast$) | Uncertainty ratio governing epistrophe; how much to trust reality vs. the model |
| **Adaptive reserve** ($\Delta\rho^\ast$) | Shock tolerance; how much disturbance increase before persistence fails |
| **Model sufficiency** ($S$) | How well the current model captures predictive information ($\in [0,1]$) |
| **Model class fitness** ($\mathcal{F}$) | Best achievable sufficiency within the model class ($\in [0,1]$) |
| **Satisfaction gap** ($\delta_{\text{sat}}$) | Ideal outcome minus best achievable — "the world doesn't permit it" |
| **Control regret** ($\delta_{\text{regret}}$) | Best achievable minus current performance — "you're not doing it well enough" |
| **Causal information yield** (CIY) | Information gained about action-outcome relationships from a single action |
| **Chronica** ($\mathcal{C}_t$) | The complete interaction history; the agent's non-forkable causal past |


## Structural Concepts

| Term | Definition |
|------|-----------|
| **Sector condition** | Nonlinear correction guarantee enabling Lyapunov stability analysis |
| **Directed separation** | $M_t$ dynamics independent of $G_t$ (conditional on processing topology) |
| **Orient cascade** | Within-cycle resolution order: $M_t$ update → $\Sigma_t$ revision → $O_t$ revision |
| **Structural adaptation** | Changing the model class, not just parameters; the cycle that operates on cycles |
| **Deliberation cost** | Think vs. act tradeoff: gain improvement must exceed mismatch accumulated while pausing |
| **Composition threshold** | Condition under which composite agent's internal coordination sustains persistence |
| **Communication gain** ($\eta_{ji}^\ast$) | Trust-weighted uncertainty ratio for inter-agent channels |
| **Unity dimensions** ($U_M, U_O, U_\Sigma$) | Epistemic, teleological, and strategic coherence between agents |


## Terminology Choices

| Formal term | Informal alternatives | Note |
|-------------|----------------------|------|
| **Actuated** | Purposeful, goal-oriented | Formal term avoids consciousness connotations |
| **Logogenic** | Language-based, LLM-based | Names the structural property, not the technology |
| **Logozoetic** | Conscious AI, sentient agent | Names the existential property precisely |


## Terms to Be Added

Terms with specific AAD meaning awaiting full treatment in README.md:

- **Observability dominance** — unobservable strategy edges freeze; paths become epistemically dead
- **Strategy DAG** ($\Sigma_t$) — probabilistic AND/OR DAG with single-parameter edges and derived acyclicity
- **Edge credence** ($p_{ij}$) — agent's causal efficacy estimate for a strategy edge; identification strength varies by regime (A/B/C)
- **Strategic tempo** ($\mathcal{T}_\Sigma$) — rate of useful strategy revision: $\sum_{(i,j)} \nu_{ij} \cdot \eta_{\text{edge},ij}$; AND-chains depth-gated, OR-nodes exploration-gated
- **Plan confidence** ($\hat{P}_\Sigma$) — root-node propagated status; systematically optimistic under correlated failures
- **Composition closure** — approximate dynamical homomorphism between micro and macro dynamics
- **Closure defect** ($\varepsilon^\ast$) — minimum achievable approximation error for a composite agent
