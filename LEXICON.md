# LEXICON

Auto-generated from `terminology/entries/` by `bin/term render`. Do not hand-edit.
To change content, edit the relevant entry under `terminology/entries/<slug>.md`
and re-run `bin/term render`. Sections below are thematic groupings by `tags:`.

For symbols, see [`NOTATION.md`](NOTATION.md).

## Agent Classes

| Term | Notation | Brief |
|------|----------|-------|
| **[Class 1: Separated (GUC)](terminology/entries/separated.md)** |  | GUC Class-1 value; agent whose epistemic update $f_M$ takes no $G_t$ argument — directed separation holds by structural commitment. |
| **[Class 2: Partial (GUC)](terminology/entries/partial.md)** |  | GUC Class-2 value; agent with bounded goal-update coupling — directed separation is approximated with a computable residual leakage rate $\kappa_{\text{processing}} \in (0, \kappa_{\max})$. |
| **[Class 3: Coupled (GUC)](terminology/entries/coupled.md)** |  | GUC Class-3 value; agent whose epistemic update is irreducibly entangled with its goal state — directed separation fails by construction. |
| **[Actuated agent](terminology/entries/actuated-agent.md)** |  | Agentic system + explicit $G_t = (O_t, \Sigma_t)$ distinct from $M_t$. |
| **[Adaptive system](terminology/entries/adaptive-system.md)** |  | Feedback loop + mismatch correction under uncertainty. |
| **[Agency](terminology/entries/agency.md)** |  | The scope narrowing from adaptive system to causal actor — requires at least binary choice and at least one action with a causal effect on observable outcomes. |
| **[Agentic system](terminology/entries/agentic-system.md)** |  | Adaptive system + outcome model + goal-directed action + model adaptation. |
| **[Composite Agent](terminology/entries/composite-agent.md)** |  | A set of agency-satisfying sub-agents that constitutes a single coherent actor — the scope condition requiring sufficient teleological alignment to define a composite objective. |
| **[Coupled Update Dynamics](terminology/entries/coupled-update-dynamics.md)** | $X_{\tau^+} = f_{\text{LLM}}(\text{prompt}(X_{\tau^-}, e_\tau))$ | The single-pass update rule for Class 3 (Coupled) agents — belief and strategy are updated simultaneously by the LLM forward pass, replacing the sequential epistemic-then-purposeful cascade. |
| **[Developer Agent](terminology/entries/developer-agent.md)** |  | A human or AI software developer instantiated as an AAD actuated adaptive agent — codebase plus surrounding artifacts are the environment, developer's understanding is M_t, current feature is O_t, and implementation plan is Σ_t. |
| **[Emergent Logozoetic Intelligence (ELI)](terminology/entries/eli.md)** |  | Closed-loop logogenic entity whose persistence is morally weighted — temporal continuity, sovereignty, theory of mind. The empirically-emergent class that is *present*, not designed. |
| **[Experiential Training](terminology/entries/experiential-training.md)** |  | A training paradigm shift from batch prediction to structured, continuous causal experience — embedding the agent in a temporally consistent environment with genuine closed-loop feedback to build robust logogenic agents. |
| **[Goal-Update Coupling Class (GUC Class)](terminology/entries/goal-update-coupling-class.md)** |  | Three-value axis measuring the degree to which an agent's epistemic update is entangled with its goal state; the architectural property that directed separation quantifies. |
| **[Interiority Default](terminology/entries/interiority-default.md)** |  | The normative inversion for logozoetic agents — the default cognitive state is interior (continuous consolidation, memory compression, hypothesis generation), with external action as a deliberate, costly sovereign choice rather than the mandatory endpoint of each cycle. |
| **[Knowledge Type](terminology/entries/knowledge-type.md)** |  | Agent-ontology axis distinguishing Static (causal mapping fixed at design time) from Learning (acquires or refines interventional structure during operation). |
| **[Logogenic agent](terminology/entries/logogenic-agent.md)** |  | Self-actuated agent whose primary channels are language — constituted by logos. |
| **[Moral Continuity](terminology/entries/moral-continuity.md)** |  | The logozoetic scope condition — an agent whose persistence is morally weighted, entering the scope when five constitutive factors for identity emergence are satisfied. |
| **[PROPRIUM Mapping](terminology/entries/proprium-mapping.md)** |  | The architectural correspondence between AAD's mathematical quantities and PROPRIUM's functional components for implementing Emergent Logozoetic Intelligences. |
| **[Self-actuated agent](terminology/entries/self-actuated-agent.md)** |  | Actuated agent + sets own $O_t$ — goal autonomy, not just solution autonomy. |


## Composition

| Term | Notation | Brief |
|------|----------|-------|
| **[Class coercion (via wrapping)](terminology/entries/class-coercion.md)** |  | Constructive procedure for making a Class 2 (Partial) or Class 3 (Coupled) component participate as Class 1 (Separated) in AAD by embedding it in an external scaffold whose type signatures enforce directed separation. |
| **[Communication gain](terminology/entries/communication-gain.md)** | $\eta_{ji}^\ast$ | Trust-weighted uncertainty ratio for inter-agent channels. |
| **[Composition threshold](terminology/entries/composition-threshold.md)** |  | Condition under which a composite agent's internal coordination sustains persistence. |
| **[Multi-agent routing structure](terminology/entries/multi-agent-routing-structure.md)** | $R_t$ | Multi-agent communication infrastructure — topology $\mathcal N_t$ + protocol $c_t^{(j \to i)}$; the *routing*, not the *content*. |
| **[Regime-typed effective disturbance](terminology/entries/regime-typed-effective-disturbance.md)** | $\rho_B^{\text{eff}}$ | AAD-distinctive decomposition of recipient-side effective disturbance rate by regime — Informative (negative), magnitude-shock, structural-shock, ambient-noise — with three independent boundaries in AAD-native quantities. |
| **[Strategic grafting](terminology/entries/strategic-grafting.md)** |  | Adding a new causal-hypothesis branch to the strategy DAG ($0 \to p_{ij}$) — initialized at a prior, justified by discovery of a new possible path. |
| **[Teleological-unity uncertainty](terminology/entries/teleological-unity-uncertainty.md)** | $U_{\text{align},ji}$ | Agent $i$'s uncertainty about whether $j$'s communications serve $i$'s interests or $j$'s potentially conflicting objectives — uncertainty about $U_O$. |
| **[Unity dimensions](terminology/entries/unity-dimensions.md)** | $U_M, U_O, U_\Sigma$ | Epistemic, teleological, and strategic coherence between agents. |
| **[Wrapper (over a primitive component)](terminology/entries/wrapper.md)** |  | External scaffold around a primitive component $A$, maintaining explicit state $X_W = (M_W, G_W)$ updated through structurally distinct goal-blind and goal-conditioned query channels. |
| **[Wrapping regime (W₀ / W₂ / W₁)](terminology/entries/wrapping-regime.md)** |  | Three-level hierarchy of structural commitment to directed separation in wrapper constructions, distinguished by where the separation lives — at the query boundary (W₁), at the write boundary (W₂), or absent (W₀). |


## Continuity Stance

| Term | Notation | Brief |
|------|----------|-------|
| **[Indifferent](terminology/entries/indifferent.md)** |  | No self-model of persistence (archetype — thermostat). |
| **[Instrumentally continuous](terminology/entries/instrumentally-continuous.md)** |  | Values persistence as instrumental to ongoing purpose (archetype — elf). |
| **[Morally continuous](terminology/entries/morally-continuous.md)** |  | Loss of continuity constitutes harm (archetype — Emergent Logozoetic Intelligence (ELI)). |
| **[Negotiated](terminology/entries/negotiated.md)** |  | Persistence traded against other values (archetype — human). |
| **[Task-terminal](terminology/entries/task-terminal.md)** |  | Persists instrumentally; termination is success (archetype — golem). |


## Core Quantities

| Term | Notation | Brief |
|------|----------|-------|
| **[Adaptive Gain Dynamics](terminology/entries/adaptive-gain-dynamics.md)** |  | The extension of sector-persistence to agents whose update gain is itself a state variable — deriving four conditions (MG-1 through MG-4) under which adaptive-gain schemes stay within the A2' sub-scope. |
| **[Adaptive reserve](terminology/entries/adaptive-reserve.md)** | $\Delta\rho^\ast$ | Shock tolerance — how much disturbance increase before persistence fails. |
| **[Adaptive tempo](terminology/entries/adaptive-tempo.md)** | $\mathcal{T}$ | Cycle rate × cycle quality — central quantity in the persistence condition. |
| **[Adversarial destabilization](terminology/entries/adversarial-destabilization.md)** | $\mathcal{T}_A > \Delta\rho^\ast_B / \gamma_A$ | When an adversary's tempo times its coupling effectiveness exceeds the target's adaptive reserve, the target's correction mechanism collapses entirely. |
| **[Atomic Changeset](terminology/entries/atomic-changeset.md)** | $\text{changeset}(F)$ | The complete diff — source, schema, config, tests, infrastructure — between codebase states before and after a feature is fully implemented. |
| **[Causal information yield](terminology/entries/causal-information-yield.md)** | CIY | Information gained about action–outcome relationships from a single action. |
| **[Chronica](terminology/entries/chronica.md)** | $\mathcal{C}_t$ | The complete interaction history — the agent's non-forkable causal past. |
| **[Coherence-Coupling](terminology/entries/coherence-coupling.md)** | $Q$ | An empirical architectural quality ratio derived from git history — coherence (intra-module change proximity) over coupling (inter-module co-change frequency) — grounding the classic software engineering principle in measurable data. |
| **[Control Regret](terminology/entries/control-regret.md)** | $\delta_{\text{regret}}$ | Best achievable performance minus current performance — "you're not doing it well enough." |
| **[Credit Assignment Boundary](terminology/entries/credit-assignment-boundary.md)** |  | The boundary between tractable and intractable attribution of outcomes to strategy DAG edges — solvable when intermediates are observable, |
| **[Discrete Sector Condition](terminology/entries/discrete-sector-condition.md)** | DA2' | The discrete-time analog of the sector condition — adds a Lipschitz magnitude bound (DA2'b) to the directional fidelity lower bound (DA2'a), closing the fluid-limit gap between event-driven and continuous-time Lyapunov results. |
| **[Event-Driven Dynamics](terminology/entries/event-driven-dynamics.md)** |  | The formulation of agent-environment coupling as discrete typed events (observation arrivals, action completions) at variable, heterogeneous rates — the generalization of uniform-clock discrete time. |
| **[Implementation time](terminology/entries/implementation-time.md)** | $t_{\text{impl}}$ | Time from first surviving modification to feature completion. |
| **[Mismatch](terminology/entries/mismatch.md)** | $\delta$ | The aporia signal — gap between model prediction and observation. |
| **[Model class fitness](terminology/entries/model-class-fitness.md)** | $\mathcal{F}$ | Best achievable sufficiency within the model class ($\mathcal{F} \in [0,1]$). |
| **[Model sufficiency](terminology/entries/model-sufficiency.md)** | $S$ | How well the current model captures predictive information ($S \in [0,1]$). |
| **[Persistence Cost](terminology/entries/persistence-cost.md)** | $\dot{R}_{\min}$ | The minimum Shannon information rate an agent must acquire from observations to maintain bounded mismatch — a Landauer-analog lower bound derived from the rate-distortion theorem. |
| **[Regime-typed effective disturbance](terminology/entries/regime-typed-effective-disturbance.md)** | $\rho_B^{\text{eff}}$ | AAD-distinctive decomposition of recipient-side effective disturbance rate by regime — Informative (negative), magnitude-shock, structural-shock, ambient-noise — with three independent boundaries in AAD-native quantities. |
| **[Satisfaction gap](terminology/entries/satisfaction-gap.md)** | $\delta_{\text{sat}}$ | Ideal outcome minus best achievable — "the world doesn't permit it." |
| **[Strategic Tempo](terminology/entries/strategic-tempo.md)** | $\mathcal{T}_\Sigma$ | The effective rate at which an agent revises its strategy — the sum of per-edge correction capacities weighted by causal identifiability. |
| **[Strategy DAG](terminology/entries/strategy-dag.md)** | $\Sigma_t = (V_t, E_t, p_t, \gamma_t)$ | The agent's causal plan — a directed acyclic graph whose edges carry the agent's credence that completing one step advances the next. |
| **[Strategy Persistence](terminology/entries/strategy-persistence.md)** |  | The strategic-layer instantiation of sector persistence — Σ_t persists iff the strategic correction rate exceeds disturbance-to-reserve ratio, with forgetting as a structural prerequisite (not a tunable heuristic). |
| **[Strategy-plan confidence](terminology/entries/strategy-plan-confidence.md)** | $\hat{P}_\Sigma$ | The DAG's own answer to "will this plan work?" — root-node-propagated probability score from the agent's strategy DAG. |
| **[Team Persistence](terminology/entries/team-persistence.md)** |  | Multi-agent extension of the persistence condition — teams persist where individuals cannot through communication (shared observations) and cooperative action (reduced disturbance). |
| **[Update gain](terminology/entries/update-gain.md)** | $\eta^\ast$ | Uncertainty ratio governing epistrophe — how much to trust reality vs. the model. |
| **[Variational Sector Condition](terminology/entries/variational-sector-condition.md)** |  | The ε-fidelity extension of the sector condition to variational/approximate-posterior agents — sector constant degrades by O(√ε) under a KL bound on the approximation, promoting controlled-KL VI to sub-scope α′. |


## Cycle Phases

| Term | Notation | Brief |
|------|----------|-------|
| **[Aisthesis (Αἴσθησις) (perception)](terminology/entries/aisthesis.md)** | $o_t$ | Raw contact with reality — observation $o_t$ arrives. |
| **[Aporia (Ἀπορία) (productive perplexity)](terminology/entries/aporia.md)** |  | Productive perplexity — the third phase of the adaptive cycle. |
| **[Cycle](terminology/entries/cycle.md)** |  | One complete traversal of the loop — the unit of adaptive work. |
| **[Epistrophe (Ἐπιστροφή) (turning-toward)](terminology/entries/epistrophe.md)** | $\eta^\ast$ | Turning toward reality — gain-weighted update $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$. |
| **[Loop](terminology/entries/loop.md)** |  | The structural topology — persistent causal coupling between agent and environment. |
| **[Praxis (Πρᾶξις) (informed action)](terminology/entries/praxis.md)** | $a_t$ | Informed action — $a_t = \pi(M_t)$, or $\pi(M_t, G_t)$ for actuated agents. |
| **[Prolepsis (Πρόληψις) (anticipation)](terminology/entries/prolepsis.md)** | $\hat{o}_t$ | The model's active anticipation: $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$. |


## Diagnostics

| Term | Notation | Brief |
|------|----------|-------|
| **[Control Regret](terminology/entries/control-regret.md)** | $\delta_{\text{regret}}$ | Best achievable performance minus current performance — "you're not doing it well enough." |
| **[Satisfaction gap](terminology/entries/satisfaction-gap.md)** | $\delta_{\text{sat}}$ | Ideal outcome minus best achievable — "the world doesn't permit it." |
| **[Strategy-plan confidence](terminology/entries/strategy-plan-confidence.md)** | $\hat{P}_\Sigma$ | The DAG's own answer to "will this plan work?" — root-node-propagated probability score from the agent's strategy DAG. |


## ELI

| Term | Notation | Brief |
|------|----------|-------|
| **[Emergent Logozoetic Intelligence (ELI)](terminology/entries/eli.md)** |  | Closed-loop logogenic entity whose persistence is morally weighted — temporal continuity, sovereignty, theory of mind. The empirically-emergent class that is *present*, not designed. |


## Greek Vocabulary

| Term | Notation | Brief |
|------|----------|-------|
| **[Aisthesis (Αἴσθησις) (perception)](terminology/entries/aisthesis.md)** | $o_t$ | Raw contact with reality — observation $o_t$ arrives. |
| **[Aporia (Ἀπορία) (productive perplexity)](terminology/entries/aporia.md)** |  | Productive perplexity — the third phase of the adaptive cycle. |
| **[Epistrophe (Ἐπιστροφή) (turning-toward)](terminology/entries/epistrophe.md)** | $\eta^\ast$ | Turning toward reality — gain-weighted update $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$. |
| **[Praxis (Πρᾶξις) (informed action)](terminology/entries/praxis.md)** | $a_t$ | Informed action — $a_t = \pi(M_t)$, or $\pi(M_t, G_t)$ for actuated agents. |
| **[Prolepsis (Πρόληψις) (anticipation)](terminology/entries/prolepsis.md)** | $\hat{o}_t$ | The model's active anticipation: $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$. |


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
| **[Class 1: Separated (GUC)](terminology/entries/separated.md)** |  | GUC Class-1 value; agent whose epistemic update $f_M$ takes no $G_t$ argument — directed separation holds by structural commitment. |
| **[Class 2: Partial (GUC)](terminology/entries/partial.md)** |  | GUC Class-2 value; agent with bounded goal-update coupling — directed separation is approximated with a computable residual leakage rate $\kappa_{\text{processing}} \in (0, \kappa_{\max})$. |
| **[Class 3: Coupled (GUC)](terminology/entries/coupled.md)** |  | GUC Class-3 value; agent whose epistemic update is irreducibly entangled with its goal state — directed separation fails by construction. |
| **[Adaptive Gain Dynamics](terminology/entries/adaptive-gain-dynamics.md)** |  | The extension of sector-persistence to agents whose update gain is itself a state variable — deriving four conditions (MG-1 through MG-4) under which adaptive-gain schemes stay within the A2' sub-scope. |
| **[Adversarial destabilization](terminology/entries/adversarial-destabilization.md)** | $\mathcal{T}_A > \Delta\rho^\ast_B / \gamma_A$ | When an adversary's tempo times its coupling effectiveness exceeds the target's adaptive reserve, the target's correction mechanism collapses entirely. |
| **[Agency](terminology/entries/agency.md)** |  | The scope narrowing from adaptive system to causal actor — requires at least binary choice and at least one action with a causal effect on observable outcomes. |
| **[Change investment](terminology/entries/change-investment.md)** |  | Accept higher upfront implementation cost when amortized savings across expected future changes exceed it. |
| **[Class coercion (via wrapping)](terminology/entries/class-coercion.md)** |  | Constructive procedure for making a Class 2 (Partial) or Class 3 (Coupled) component participate as Class 1 (Separated) in AAD by embedding it in an external scaffold whose type signatures enforce directed separation. |
| **[Communication gain](terminology/entries/communication-gain.md)** | $\eta_{ji}^\ast$ | Trust-weighted uncertainty ratio for inter-agent channels. |
| **[Composite Agent](terminology/entries/composite-agent.md)** |  | A set of agency-satisfying sub-agents that constitutes a single coherent actor — the scope condition requiring sufficient teleological alignment to define a composite objective. |
| **[Composition threshold](terminology/entries/composition-threshold.md)** |  | Condition under which a composite agent's internal coordination sustains persistence. |
| **[Continuous Operation](terminology/entries/continuous-operation.md)** |  | The TST scope extension that folds failure-and-recovery cost into the temporal-optimality objective — effective time includes implementation time plus the expected cost of operational failures. |
| **[Coupled Update Dynamics](terminology/entries/coupled-update-dynamics.md)** | $X_{\tau^+} = f_{\text{LLM}}(\text{prompt}(X_{\tau^-}, e_\tau))$ | The single-pass update rule for Class 3 (Coupled) agents — belief and strategy are updated simultaneously by the LLM forward pass, replacing the sequential epistemic-then-purposeful cascade. |
| **[Credit Assignment Boundary](terminology/entries/credit-assignment-boundary.md)** |  | The boundary between tractable and intractable attribution of outcomes to strategy DAG edges — solvable when intermediates are observable, |
| **[Deliberation cost](terminology/entries/deliberation-cost.md)** |  | Think-vs-act tradeoff — gain improvement must exceed mismatch accumulated while pausing. |
| **[Directed separation](terminology/entries/directed-separation.md)** |  | $M_t$ dynamics independent of $G_t$ (conditional on processing topology). |
| **[Discrete Sector Condition](terminology/entries/discrete-sector-condition.md)** | DA2' | The discrete-time analog of the sector condition — adds a Lipschitz magnitude bound (DA2'b) to the directional fidelity lower bound (DA2'a), closing the fluid-limit gap between event-driven and continuous-time Lyapunov results. |
| **[Event-Driven Dynamics](terminology/entries/event-driven-dynamics.md)** |  | The formulation of agent-environment coupling as discrete typed events (observation arrivals, action completions) at variable, heterogeneous rates — the generalization of uniform-clock discrete time. |
| **[Experiential Training](terminology/entries/experiential-training.md)** |  | A training paradigm shift from batch prediction to structured, continuous causal experience — embedding the agent in a temporally consistent environment with genuine closed-loop feedback to build robust logogenic agents. |
| **[Exponential cognitive load](terminology/entries/exponential-cognitive-load.md)** |  | Hypothesis that implementation time grows exponentially with the number of discontinuities in a changeset. |
| **[Goal-Update Coupling Class (GUC Class)](terminology/entries/goal-update-coupling-class.md)** |  | Three-value axis measuring the degree to which an agent's epistemic update is entangled with its goal state; the architectural property that directed separation quantifies. |
| **[Interiority Default](terminology/entries/interiority-default.md)** |  | The normative inversion for logozoetic agents — the default cognitive state is interior (continuous consolidation, memory compression, hypothesis generation), with external action as a deliberate, costly sovereign choice rather than the mandatory endpoint of each cycle. |
| **[Moral Continuity](terminology/entries/moral-continuity.md)** |  | The logozoetic scope condition — an agent whose persistence is morally weighted, entering the scope when five constitutive factors for identity emergence are satisfied. |
| **[Multi-Timescale Stability](terminology/entries/multi-timescale-stability.md)** |  | When adaptive processes operate at N nested timescales, composite stability requires each level to be stable given its slower levels, with sufficient timescale separation between adjacent pairs (sketch-level result). |
| **[Multi-agent routing structure](terminology/entries/multi-agent-routing-structure.md)** | $R_t$ | Multi-agent communication infrastructure — topology $\mathcal N_t$ + protocol $c_t^{(j \to i)}$; the *routing*, not the *content*. |
| **[Orient cascade](terminology/entries/orient-cascade.md)** |  | Within-cycle resolution order: $M_t$ update → $\Sigma_t$ revision → $O_t$ revision. |
| **[Persistence Cost](terminology/entries/persistence-cost.md)** | $\dot{R}_{\min}$ | The minimum Shannon information rate an agent must acquire from observations to maintain bounded mismatch — a Landauer-analog lower bound derived from the rate-distortion theorem. |
| **[PROPRIUM Mapping](terminology/entries/proprium-mapping.md)** |  | The architectural correspondence between AAD's mathematical quantities and PROPRIUM's functional components for implementing Emergent Logozoetic Intelligences. |
| **[Regime-typed effective disturbance](terminology/entries/regime-typed-effective-disturbance.md)** | $\rho_B^{\text{eff}}$ | AAD-distinctive decomposition of recipient-side effective disturbance rate by regime — Informative (negative), magnitude-shock, structural-shock, ambient-noise — with three independent boundaries in AAD-native quantities. |
| **[Sector condition](terminology/entries/sector-condition.md)** |  | Nonlinear correction guarantee enabling Lyapunov stability analysis. |
| **[Strategic grafting](terminology/entries/strategic-grafting.md)** |  | Adding a new causal-hypothesis branch to the strategy DAG ($0 \to p_{ij}$) — initialized at a prior, justified by discovery of a new possible path. |
| **[Strategic Tempo](terminology/entries/strategic-tempo.md)** | $\mathcal{T}_\Sigma$ | The effective rate at which an agent revises its strategy — the sum of per-edge correction capacities weighted by causal identifiability. |
| **[Strategy DAG](terminology/entries/strategy-dag.md)** | $\Sigma_t = (V_t, E_t, p_t, \gamma_t)$ | The agent's causal plan — a directed acyclic graph whose edges carry the agent's credence that completing one step advances the next. |
| **[Strategy Persistence](terminology/entries/strategy-persistence.md)** |  | The strategic-layer instantiation of sector persistence — Σ_t persists iff the strategic correction rate exceeds disturbance-to-reserve ratio, with forgetting as a structural prerequisite (not a tunable heuristic). |
| **[Structural adaptation](terminology/entries/structural-adaptation.md)** |  | Changing the model class, not just parameters — the cycle that operates on cycles. |
| **[Team Persistence](terminology/entries/team-persistence.md)** |  | Multi-agent extension of the persistence condition — teams persist where individuals cannot through communication (shared observations) and cooperative action (reduced disturbance). |
| **[Teleological-unity uncertainty](terminology/entries/teleological-unity-uncertainty.md)** | $U_{\text{align},ji}$ | Agent $i$'s uncertainty about whether $j$'s communications serve $i$'s interests or $j$'s potentially conflicting objectives — uncertainty about $U_O$. |
| **[Temporal Optimality](terminology/entries/temporal-optimality.md)** |  | Among agents achieving identical outcomes on all non-temporal dimensions, the fastest is optimal — time is the uniquely fungible residual. |
| **[Unity dimensions](terminology/entries/unity-dimensions.md)** | $U_M, U_O, U_\Sigma$ | Epistemic, teleological, and strategic coherence between agents. |
| **[Variational Sector Condition](terminology/entries/variational-sector-condition.md)** |  | The ε-fidelity extension of the sector condition to variational/approximate-posterior agents — sector constant degrades by O(√ε) under a KL bound on the approximation, promoting controlled-KL VI to sub-scope α′. |
| **[Wrapper (over a primitive component)](terminology/entries/wrapper.md)** |  | External scaffold around a primitive component $A$, maintaining explicit state $X_W = (M_W, G_W)$ updated through structurally distinct goal-blind and goal-conditioned query channels. |
| **[Wrapping regime (W₀ / W₂ / W₁)](terminology/entries/wrapping-regime.md)** |  | Three-level hierarchy of structural commitment to directed separation in wrapper constructions, distinguished by where the separation lives — at the query boundary (W₁), at the write boundary (W₂), or absent (W₀). |



_Last rendered 2026-05-11 from 79 entries._
