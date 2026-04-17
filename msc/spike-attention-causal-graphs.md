# Causal Graphs for Attention-Observation-Orientation Coupling

**Status**: Exploratory. Multiple graph versions to see what the causal structure reveals. Working from Joseph's sketch of an observation-channel-centric orientation loop.

**Date**: 2026-03-13 (overnight session, continued)

---

## Version 1: Joseph's Sketch (Cleaned Up)

Starting from the observation-channel-centric view Joseph sketched:

```
                    ┌──────────────────────────────────┐
                    │                                  │
                    ▼                                  │
             ┌─────────────┐                           │
             │ Orientation  │  (current attention       │
             │ (where we    │   allocation: which       │
             │  look)       │   channels are active,    │
             └──────┬───────┘   at what fidelity)       │
                    │                                   │
                    │ determines channel                │
                    │ fidelity/sensitivity/throughput    │
                    ▼                                   │
             ┌─────────────┐                            │
             │ Observation  │  (what arrives through     │
             │ Channels     │   each channel, gated      │
             └──────┬───────┘   by orientation)          │
                    │                                    │
                    │ mismatch against                   │
                    │ prolepsis (per channel)             │
                    ▼                                    │
             ┌─────────────┐                             │
             │ Attentional  │  (aporia that signals      │
             │ Aporia       │   "something needs          │
             └──────┬───────┘   attention here")          │
                    │                                     │
                    │ drives                              │
                    ▼                                     │
             ┌─────────────┐                              │
             │ Epistrophe   │  (model correction:         │
             │ of Model     │   update M_t in the         │
             └──────┬───────┘   affected region)          │
                    │                                     │
                    │ revised model implies               │
                    │ revised attention needs              │
                    ▼                                     │
             ┌─────────────┐                              │
             │ Attention    │  (reallocation of            │
             │ Reallocation │   observation capacity       │
             └──────┬───────┘   based on updated model)   │
                    │                                     │
                    ├──────────────────────────────────────┘
                    │                           (back to Orientation)
                    │ also drives
                    ▼
             ┌─────────────┐
             │ Epistrophic  │  (corrective action
             │ Action       │   in the environment)
             └─────────────┘
```

**Observation**: This is a SINGLE loop, but it has a branch point at Epistrophe — the model correction both redirects attention (the meta-level) AND drives action (the object-level). The two outputs compete for resources.

**Key causal claim**: Orientation → Observations is a causal link (changing where you look CAUSES different observations). This means the observation channel is not exogenous — it's endogenous to the agent's attentional state. AAD's scope condition treats 𝒪 ≠ ∅ as given, but the actual information content of 𝒪 depends on orientation.

---

## Version 2: Two Competing Loops (Task vs. Sentinel)

What if we decompose this into two loops that share the observation channels and compete for action space?

```
    ┌─── TASK LOOP ──────────────────────────────────────────┐
    │                                                         │
    ▼                                                         │
┌────────────┐     ┌────────────┐     ┌────────────┐         │
│ Task       │────▶│ Task-Directed│───▶│ Task       │         │
│ Prolepsis  │     │ Observations │    │ Aporia     │         │
│ (what I    │     │ (high fidelity│   │ (δ within  │         │
│  expect    │     │  in task     │    │  task      │         │
│  next in   │     │  scope)      │    │  scope)    │         │
│  task)     │     └─────────────┘    └──────┬─────┘         │
└────────────┘                                │               │
      ▲                                       │               │
      │                              ┌────────▼─────────┐    │
      │                              │ Task Epistrophe   │    │
      │                              │ (update M_t in    │    │
      │                              │  task-relevant    │    │
      │                              │  region)          │    │
      │                              └────────┬──────────┘    │
      │                                       │               │
      │                                       ▼               │
      │                              ┌──────────────────┐     │
      └──────────────────────────────│ Task Action       │────┘
                                     │ (advance strategy) │
                                     └──────────────────┘

                          ▲ COMPETES FOR ACTION SPACE ▲

    ┌─── SENTINEL LOOP ─────────────────────────────────────┐
    │                                                        │
    ▼                                                        │
┌────────────┐     ┌────────────┐     ┌────────────┐        │
│ Stationarity│───▶│ Ambient     │───▶│ Sentinel   │        │
│ Assumption  │    │ Observations │    │ Aporia     │        │
│ (nothing is │    │ (low fidelity│    │ (something │        │
│  changing   │    │  in non-task │    │  changed   │        │
│  outside    │    │  scope)      │    │  outside   │        │
│  task scope)│    └─────────────┘    │  task scope)│        │
└────────────┘                        └──────┬─────┘        │
      ▲                                      │              │
      │                             ┌────────▼──────────┐   │
      │                             │ Sentinel Epistrophe│   │
      │                             │ (update M_t in     │   │
      │                             │  ambient region OR │   │
      │                             │  INTERRUPT task    │   │
      │                             │  loop)             │   │
      │                             └────────┬───────────┘   │
      │                                      │               │
      │                                      ▼               │
      │                             ┌──────────────────┐     │
      └─────────────────────────────│ Reorientation    │─────┘
                                    │ Action (redirect  │
                                    │ attention OR      │
                                    │ escalate to       │
                                    │ strategic loop)   │
                                    └──────────────────┘
```

**Key causal link**: Sentinel Epistrophe → INTERRUPT task loop. This is the preemptive reorientation. The sentinel loop's correction can *preempt* the task loop, forcing attention reallocation.

**Competition for action space**: At any given moment, the agent must choose between:
- Task Action (advance the current strategy)
- Reorientation Action (redirect attention based on sentinel signal)
- Exploration Action (deliberate expansion of observed scope)

This competition is itself a causal graph node — an action-selection point that weighs multiple inputs.

---

## Version 3: The DAG With Strategy Sensitivity

Adding the ∂Σ/∂M sensitivity that emerged in the evening conversation:

```
                     ┌───────────┐
                     │ Current   │
                     │ Strategy  │
                     │ Σ_t       │
                     └─────┬─────┘
                           │
              ┌────────────┼────────────────┐
              │            │                │
              ▼            ▼                ▼
        ┌──────────┐ ┌──────────┐    ┌──────────┐
        │ ∂Σ/∂M    │ │ ∂Σ/∂M    │    │ ∂Σ/∂M    │
        │ Region A  │ │ Region B │    │ Region C │
        │ (HIGH:    │ │ (LOW:    │    │ (UNKNOWN: │
        │ task-     │ │ background│   │ unmonitored│
        │ critical) │ │ stable)  │    │ assumed   │
        └────┬──────┘ └────┬─────┘    │ benign)   │
             │             │          └─────┬─────┘
             │             │                │
             ▼             ▼                ▼
        ┌──────────┐ ┌──────────┐    ┌──────────┐
        │ Attention │ │ Attention│    │ Attention │
        │ = HIGH   │ │ = LOW    │    │ = MINIMAL │
        │ (primary │ │ (periodic│    │ (sentinel │
        │ loop)    │ │ check)   │    │ only)     │
        └────┬─────┘ └────┬─────┘    └─────┬────┘
             │             │                │
             ▼             ▼                ▼
        ┌──────────┐ ┌──────────┐    ┌──────────┐
        │ δ in A:  │ │ δ in B:  │    │ δ in C:  │
        │ SMALL    │ │ SMALL    │    │ LARGE    │
        │ (routine │ │ (expected│    │ (SURPRISE │
        │ update)  │ │ stable)  │    │ — radar  │
        └────┬─────┘ └────┬─────┘    │ lock!)   │
             │             │          └─────┬────┘
             │             │                │
             │             │                │
             ▼             ▼                ▼
        ┌──────────┐ ┌──────────┐    ┌──────────────────────┐
        │ Normal   │ │ No       │    │ CRISIS:               │
        │ cascade  │ │ action   │    │ δ × ∂Σ/∂M = LARGE    │
        │ (update  │ │ needed   │    │                       │
        │ M, check │ │          │    │ → Σ_t INVALIDATED    │
        │ δ_sat,   │ │          │    │ → Preempt task loop  │
        │ etc.)    │ │          │    │ → Force reorientation │
        └──────────┘ └──────────┘    └───────────────────────┘
```

**The key causal chain for crisis**: Low attention in Region C → Low-fidelity observation → Large δ detected anyway → High ∂Σ/∂M (the strategy was sensitive to this region) → δ × ∂Σ/∂M exceeds threshold → Preempt task loop.

**DAG implication**: The product δ × ∂Σ/∂M is the *effective severity signal*. This is NOT just δ magnitude. A large δ in a low-sensitivity region is ignorable. A small δ in a high-sensitivity region is important. The severity depends on both the mismatch AND the strategy's dependence on that model region.

**But ∂Σ/∂M for Region C was UNKNOWN.** The agent assumed Region C was benign, so it never computed ∂Σ/∂M there. The sensitivity itself is a model quantity that requires attention to estimate. This creates a bootstrap problem: you need attention to know sensitivity, but you allocate attention based on sensitivity.

This is the formal version of "you don't know what you don't know." The stationarity assumption in unmonitored regions is an implicit claim that ∂Σ/∂M ≈ 0 there. When that claim is wrong, you get surprise.

---

## Version 4: Parallel Epistrophic Intent Loops

Taking Joseph's hint about "epistrophic intent as a continual loop with its own parallel":

```
          STRATEGIC INTENT                    EPISTROPHIC INTENT
          (Goal-driven)                       (Model-driven)

    ┌─────────────────┐                 ┌─────────────────┐
    │ O_t: What I     │                 │ Perplexity:     │
    │ want to achieve  │                │ Where is my     │
    │                  │                │ model uncertain  │
    │ Σ_t: How I plan │                │ or degrading?   │
    │ to achieve it   │                │                 │
    └────────┬────────┘                └────────┬────────┘
             │                                  │
             │ generates                        │ generates
             │ task actions                     │ epistrophic actions
             ▼                                  ▼
    ┌─────────────────┐                 ┌─────────────────┐
    │ Actions serving  │                │ Actions serving  │
    │ the strategy:    │                │ the model:       │
    │ - execute plan   │                │ - look around    │
    │ - advance toward │                │ - verify assump. │
    │   O_t            │                │ - probe uncertain│
    │                  │                │   regions        │
    └────────┬────────┘                └────────┬────────┘
             │                                  │
             │           ┌─────────┐            │
             └──────────▶│ ACTION  │◀───────────┘
                         │ SPACE   │
                         │ (finite │
                         │ capacity│
                         │ — must  │
                         │ choose) │
                         └────┬────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │ Environment      │
                    │ responds         │
                    └────────┬─────────┘
                             │
                ┌────────────┼──────────────┐
                │                           │
                ▼                           ▼
    ┌─────────────────┐            ┌─────────────────┐
    │ Observations     │            │ Observations     │
    │ relevant to      │            │ relevant to      │
    │ strategy         │            │ model quality    │
    └────────┬────────┘            └────────┬────────┘
             │                              │
             ▼                              ▼
    ┌─────────────────┐            ┌─────────────────┐
    │ Strategic        │            │ Epistemic        │
    │ Aporia:          │            │ Aporia:          │
    │ δ_sat, δ_regret, │           │ δ_epistemic,     │
    │ δ_strategic      │            │ model sufficiency│
    └────────┬────────┘            └────────┬────────┘
             │                              │
             │  feeds back to               │ feeds back to
             ▼                              ▼
    ┌─────────────────┐            ┌─────────────────┐
    │ Strategy revision│            │ Model correction │
    │ or O_t revision  │            │ + attention      │
    │                  │            │ reallocation     │
    └────────┬────────┘            └────────┬────────┘
             │                              │
             └──────────┬───────────────────┘
                        │
                        ▼
              ┌──────────────────┐
              │ Updated Σ_t      │
              │ (including new   │
              │ attention        │
              │ allocation)      │
              └──────────────────┘
```

**The key structural insight**: There are TWO parallel intent systems competing for the same action space:
- **Strategic intent**: "What actions advance my plan?" (exploitation)
- **Epistrophic intent**: "What actions improve my model?" (exploration/sentinel)

This is AAD's CIY tradeoff, but drawn as a causal DAG rather than a single optimization. The λ parameter in the policy objective:

    π*(M_t, G_t) = argmax [Q_O(...) + λ · CIY(a; M_t)]

is essentially the resource allocation between these two intent systems. But drawn as a DAG, something becomes visible: **the two systems have different causal paths to action and different feedback paths from observation.** They're not just two terms in a sum — they're parallel causal structures that merge at the action node and split at the observation node.

**Implication for directed separation**: The epistrophic intent loop is inherently goal-blind (it's driven by model quality, not by O_t). The strategic intent loop is inherently goal-driven (it's driven by Σ_t). If these are architecturally separate (different modules, different processing paths), directed separation is natural — the epistrophic loop processes observations without consulting goals. If they're architecturally merged (same attention mechanism, same processing path — as in a transformer), directed separation fails because the two intent systems share processing resources and contaminate each other.

This is a causal-graph argument for WHY directed separation is architecture-dependent, not a universal property.

---

## Version 5: The Hierarchical Composition View

What if we see the attention governance as a COMPOSITION of agents at different timescales?

```
    ┌────────────────────────────────────────────────────────┐
    │                    META-AGENT                          │
    │  (governs attention allocation across sub-agents)      │
    │                                                        │
    │  M_meta: which sub-agent is currently "in focus"       │
    │  G_meta: overall mission / survival                    │
    │  π_meta: attention allocation policy                   │
    │                                                        │
    │  PAAEP cycle: SLOW (strategic timescale)               │
    │                                                        │
    │  ┌──────────────────┐    ┌──────────────────┐          │
    │  │   SUB-AGENT 1    │    │   SUB-AGENT 2    │          │
    │  │   (Task Executor) │    │   (Sentinel)     │          │
    │  │                  │    │                  │          │
    │  │  M_1: task model │    │  M_2: ambient    │          │
    │  │  G_1: task goal  │    │       model      │          │
    │  │  π_1: task policy│    │  G_2: detect     │          │
    │  │                  │    │       anomalies  │          │
    │  │  PAAEP: FAST     │    │  π_2: scan policy│          │
    │  │  (tactical)      │    │                  │          │
    │  │  Attention: HIGH │    │  PAAEP: MEDIUM   │          │
    │  │  in task scope   │    │  (background)    │          │
    │  │                  │    │  Attention: LOW   │          │
    │  │                  │    │  but BROAD        │          │
    │  └────────┬─────────┘    └────────┬─────────┘          │
    │           │                       │                    │
    │           │  SHARED               │                    │
    │           │  ENVIRONMENT          │                    │
    │           └───────┬───────────────┘                    │
    │                   │                                    │
    │           ┌───────▼──────────┐                         │
    │           │ Shared M_t       │                         │
    │           │ (composite model │                         │
    │           │  with regions of │                         │
    │           │  varying fidelity)│                        │
    │           └──────────────────┘                         │
    │                                                        │
    │  INTERRUPT MECHANISM:                                  │
    │  When Sub-Agent 2 detects anomaly:                     │
    │    severity = δ_2 × ∂Σ_1/∂M_2_region                  │
    │    if severity > threshold:                            │
    │      Meta-Agent reallocates attention                  │
    │      (may pause Sub-Agent 1, promote Sub-Agent 2)      │
    │                                                        │
    └────────────────────────────────────────────────────────┘
```

**This is literally a composition problem.** The meta-agent composes sub-agents that share an environment and a model. The composition spike's framework applies:
- Each sub-agent has its own PAAEP cycle at its own frequency
- They share M_t but attend to different regions
- The meta-agent governs inter-sub-agent coordination (attention allocation)
- The interrupt mechanism is a specific kind of coordination failure/override

**The teleological unity between sub-agents varies:**
- Sub-Agent 1 and the Meta-Agent have high teleological unity (task executor serves the mission)
- Sub-Agent 2 has a *different* objective (detect anomalies, not advance the mission) — it's deliberately somewhat adversarial to Sub-Agent 1 (it wants to interrupt the task when danger is detected)

This is exactly the "adversarial aporia" spike from Gemini's review suggestion: internal disagreement (Sub-Agent 2 says "danger!" while Sub-Agent 1 says "I'm busy!") IS the composite agent's aporia mechanism. The argument between the sentinel and the executor is how the composite agent detects things that neither sub-agent alone would catch.

---

## What Falls Out of These Graphs

### 1. The bootstrap problem of ∂Σ/∂M in unmonitored regions

Version 3 reveals: you need attention to estimate sensitivity, but you allocate attention based on sensitivity. For unmonitored regions, ∂Σ/∂M is unknown, which means severity can't be computed until the signal is already detected. This suggests that sentinel monitoring should be **unconditional** (not gated by estimated sensitivity) but **low-bandwidth** (cheap enough to run everywhere). The severity computation happens AFTER the signal breaks through, not before.

This is how the startle reflex works: it responds to statistical anomalies (sudden loud noise, unexpected movement) regardless of relevance. The relevance assessment happens AFTER the reflexive response (the cortex evaluates whether the startling stimulus was actually dangerous). The biology has separated *detection* (fast, unconditional, crude) from *evaluation* (slow, conditional, precise).

### 2. Directed separation is architecture-dependent, not universal

Version 4 reveals: if the epistrophic intent and strategic intent are architecturally separate (different processing paths), directed separation is natural. If they're merged, it fails. This is a causal-structural argument, not a scope condition — it's about the topology of the processing graph, not a parameter of the agent.

For LLMs: the processing paths are merged (same attention mechanism). κ_processing is high by architectural necessity.
For modular agents: the processing paths can be separate. κ_processing can be low by design.
For biological agents: partially separate (thalamic monitoring is separate from cortical processing) but with extensive cross-talk.

### 3. The severity signal is a product, not a sum

Versions 3 and 5: severity = δ × ∂Σ/∂M. This is multiplicative. A large δ in an insensitive region = low severity. A small δ in a sensitive region = moderate severity. A large δ in a sensitive region = crisis.

This product structure means the severity signal is zero whenever EITHER factor is zero. An agent with no strategy (∂Σ/∂M = 0 everywhere) never experiences urgency from model updates — it's a pure adaptive tracker. An agent with no mismatch (δ = 0 everywhere) never needs to reallocate attention — its prolepsis is perfect. Urgency requires both surprise AND strategic relevance.

### 4. The competition for action space is causal, not just economic

Version 4 shows: task actions and epistrophic actions compete for the same finite action space. But this isn't just a resource-allocation problem — it has causal implications. Taking an epistrophic action (probing an uncertain region) changes what observations arrive in the NEXT cycle, which changes what mismatches are detected, which changes what actions are considered. The choice between exploitation and exploration isn't just "how to spend this time step" — it shapes the entire future observation trajectory.

This is the dual-control problem from LQG, surfaced as a causal graph. The LQG separation principle fails precisely because this causal path (action → future observation quality → future model quality → future action quality) creates a loop that couples the estimator and controller.

### 5. The interrupt mechanism IS composition dynamics

Version 5 shows: the sentinel interrupting the task executor is a specific case of AAD's composition dynamics. It's one sub-agent overriding another based on a severity threshold. The meta-agent's interrupt policy is a composition coordination mechanism.

This means the attention governance layer might not need NEW theory — it might be an application of Section III's composition framework to the case of intra-agent sub-systems. The question becomes: does the composition bridge lemma (if we had it) cover the case of sub-agents that share a model and can preempt each other?

---

## What I Notice Is Missing From All Versions

**1. Time.** These graphs are static. The real dynamics involve CYCLES — the loops running at different frequencies, the interrupt happening mid-cycle, the phase relationships between loops. A static DAG can't capture the temporal dynamics. We might need something like a timed Petri net or a dynamical system on a graph.

**2. The between-event dynamics.** AAD has Ṁ = g_M(M) for autonomous model evolution between events. The attention allocation probably also evolves between events — the agent's attention gradually drifts or narrows over time without new observations. This drift is part of what makes the stationarity assumption in unmonitored regions dangerous: attention narrows over time, and the agent progressively forgets that it was once attending to something else.

**3. The cost of reorientation.** Switching attention has a real cost — context-switching overhead, loss of accumulated context in the prior focus, startup cost in the new focus. This cost should appear as a barrier in the severity calculation: reorientation happens when severity EXCEEDS the switching cost, not just when severity is positive.

**4. Memory of prior orientations.** The agent should maintain some memory of what it was monitoring before and what the model state was in those regions. This decaying memory is what allows the sentinel loop to detect anomalies — it compares current ambient observations against a remembered baseline. Without this memory, every ambient observation is equally surprising. AAD's M_t preservation framework (CLAUDE.md, memory files) is an engineering solution to this for LLM agents across sessions. Within a session, the memory of prior orientations is part of M_t.

---

## Implications for the κ Problem

Drawing these causal graphs reframes the κ problem:

**κ is not about a parameter of f_M.** It's about the **topology of the processing graph.** When the epistrophic path and the strategic path share causal infrastructure (same attention mechanism, same processing pipeline), κ_processing is high because the goal state is causally upstream of the observation processing. When they're separated (different modules, different data paths), κ_processing is low because the goal state is not causally connected to the observation processing.

This suggests that the "right" approach to directed separation isn't to parameterize the coupling and bound the error. It's to **characterize which processing topologies admit separation and which don't**, and then develop the appropriate analytical tools for each topology class.

For the laminar regime (separated topology): use the sequential cascade. Done.
For the turbulent regime (merged topology): develop the coupled analysis. This is the hard work.
For the mixed regime (partially separated): identify which boundaries are separated and which aren't, and apply the appropriate tool to each.

The κ_processing measure from the operationalization spike would then be a DIAGNOSTIC — you measure it to determine which regime you're in, not to parameterize a perturbation expansion.

---

*Several of these graphs want to be drawn properly (mermaid or graphviz) rather than ASCII art. The ASCII conveys the structure but not the dynamics. A simulation would help — run the two-loop version (task + sentinel) and watch how they interact as you vary the frequency ratio and coupling strength.*
