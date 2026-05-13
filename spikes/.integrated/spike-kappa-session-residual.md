# Session Residual: The κ Discussion, March 13-14, 2026

**Status**: Context preservation. Captures the conversational material — thought experiments, analogies, LQG analysis, and the narrative flow — that didn't make it into the formal spikes but that gives future agents the intuitive grounding behind the formal work.

**Date**: 2026-03-13/14 (evening/overnight session)

**Participants**: Joseph Wecker, Claude (Opus 4.6)

---

## 1. How the Session Unfolded

The session started with Joseph asking me to prepare for a discussion of the κ coupling parameter / directed separation issue. I read the relevant segments, spikes, and feedback documents. Joseph then asked about LQG separation principle failure modes — not as abstract theory, but to understand what KIND of failure directed separation undergoes. That question turned out to be the seed for everything that followed.

From LQG failures, Joseph moved into a detailed first-person walkthrough of what it FEELS LIKE when directed separation fails in a high-stakes agent (fighter pilot in a dogfight). This wasn't theoretical — it was Joseph reasoning from lived cognitive experience about what AAD's formalism is trying to capture. The walkthrough surfaced structural gaps in the theory that formal analysis alone hadn't identified.

The key insight cascade:
1. LQG failure modes are provable, not just empirical → directed separation failure is structural
2. The fighter pilot scenario reveals that ATTENTION ALLOCATION is where the theory's formalism breaks down
3. The Kelvin-Helmholtz image captures what happens when processing layers at different frequencies lose clean separation
4. Multiple connected reframings of κ followed (regime boundary, processing topology, causal levels)
5. Joseph's late-night observation about imagination/hallucination connected the κ problem to a possible extension of Pearl's hierarchy

## 2. The LQG Separation Failure Analysis

Joseph's first question was precise: "Can you discuss the LQG separation principle failure modes? Are we talking about provable or empirical failure modes?"

The answer, which grounded everything after:

**LQG separation** says: for linear systems with Gaussian noise and quadratic cost, the optimal estimator (Kalman filter) and optimal controller (LQR) can be designed independently. The estimator doesn't need to know the cost function. This is EXACTLY AAD's directed separation — f_M is goal-blind.

**The failures are PROVABLE, not just empirical:**

- **Nonlinear systems**: In a nonlinear system, the distribution of estimation error depends on the trajectory, which depends on the control policy. So the optimal estimator depends on the controller. The mathematical reason is clean: linearity makes the error distribution independent of the trajectory. Remove linearity, remove independence.

- **Non-Gaussian noise**: The Kalman filter is optimal because Gaussian distributions have sufficient statistics (mean, covariance) that don't depend on the control policy. With non-Gaussian noise, the sufficient statistic is the full posterior, which CAN depend on which part of state space the controller steers toward.

- **Dual control (Feldbaum, 1960s)**: When the agent can choose actions that IMPROVE its estimate (probing, exploratory actions), there's a fundamental coupling. The optimal action depends on estimation uncertainty, and estimation uncertainty depends on future actions. This maps directly to AAD's CIY / explore-exploit tradeoff.

**Critical nuance**: LQG doesn't become IRRELEVANT under these conditions — it becomes an APPROXIMATION. Engineers use certainty-equivalence (pretend separation holds) for mildly nonlinear systems all the time, and it often works. The Extended Kalman Filter + nonlinear control is exactly this.

**The failure modes sit on a spectrum, not a cliff:**
- Mild nonlinearity: separation is a good approximation, bounded error
- Strong nonlinearity: poor approximation, qualitatively different optimal policies
- Dual control: structurally wrong — can't represent explore/exploit at all

**Three types of coupling emerged** (not standard terminology — emerged from the analysis):
1. **Attention coupling** (which events to seek) — goes through the action channel, AAD already handles this via the processing/selection distinction
2. **Interpretation coupling** (how to process events) — the actual violation of directed separation. The LLM case.
3. **Filtering coupling** (which parts of an event to attend to) — somewhere between 1 and 2

This decomposition fed directly into the κ_selection / κ_processing split in the formal spike.

## 3. The Fighter Pilot Thought Experiment

Joseph walked through a detailed first-person account of what the AAD cycle feels like in a high-stakes, high-complexity agent. This is worth preserving because it reveals structural gaps that formal analysis misses.

### The Setup

"I am still, and I have prolepsis — I'm waiting for any stimulus. Prolepsis says I am oriented — my prediction/expectation is primed, caring about a subset of the model. There's a specific part of the model that I have a future prediction on — what I intended all of my prior actions to accomplish that still might happen. My brain is in OKR mode and I'm especially watching for any of the most important key results."

**What this reveals**: Prolepsis isn't just "prediction." It's ATTENTIONALLY BIASED prediction. The agent's prediction is concentrated on the model regions relevant to its current strategy. This is goal-directed attention allocation — a form of κ_selection that AAD acknowledges but doesn't formalize as a structural feature.

### The Crisis

"What happens when the next set of information comes in from a direction I am not oriented toward? It's ambient, part of the model that I had not positioned my sensors to care about but that suddenly demands some kind of attention."

The specific scenario: a fighter pilot deeply focused on pursuing a target suddenly detects radar lock from behind. The pilot's model assumed the unmonitored region was static ("nothing is changing behind me"). That assumption was catastrophically wrong.

### What Makes This Different From Routine δ_epistemic

Joseph identified that the mismatch here isn't "I predicted X and saw Y." It's "I was watching the wrong thing." The error is in the ATTENTION ALLOCATION itself, not in the model's prediction within its attended scope.

This creates a specific cascade that doesn't fit the sequential orient cascade:
- The model update (someone has radar lock) has IMMEDIATE strategy implications
- The strategy invalidation doesn't need the full cascade to resolve — it's obvious
- The agent needs to simultaneously: update M_t, invalidate Σ_t, and reorient sensors
- These happen effectively simultaneously, not sequentially

### The Formal Gap This Reveals

AAD's scope condition requires observations exist (𝒪 ≠ ∅) but says nothing about FINITE CHANNEL CAPACITY. Every real agent has limited attention. This creates:

1. **Implicit stationarity assumptions**: When you allocate attention to region A, you implicitly assume regions B, C, D aren't changing importantly. This assumption is never made explicit in the theory.

2. **The bootstrap problem**: You need attention to estimate ∂Σ/∂M (how sensitive your strategy is to a model region), but you allocate attention based on ∂Σ/∂M. For unmonitored regions, sensitivity is unknown.

3. **The severity signal is multiplicative**: δ × ∂Σ/∂M. A large δ in a low-sensitivity region is ignorable. A small δ in a high-sensitivity region demands attention. The pilot's radar lock is large δ in a region where ∂Σ/∂M was ASSUMED to be zero but was actually enormous.

### The Startle Reflex Connection

Joseph extended the thought experiment to biological preemptive reorientation:

"I am more likely to be startled if I am literally surprised — as in my attention made it so ambient signals of someone approaching from behind weren't being processed. It's elevated if I'm walking down the hall of my home that I think is empty in the middle of the night and it is completely silent and I'm already super focused as to not trip."

The key insight: there are PREBUILT COUPLINGS that cause the current strategy to be preempted by reorienting-for-survival with varying degrees of severity. These bypass the normal orient cascade entirely. They operate on SIGNAL STATISTICS (sudden change in gain, unexpected pattern) not semantic content. This is fast enough to preempt deliberative processing.

This led to: "AAD has the CONTENT of reorientation (the orient cascade) but not the GOVERNANCE of reorientation (what triggers it, how fast, at what cost to the current plan)."

### The POSIX Error Code Analogy

Joseph pointed out that POSIX error codes give a reasonable ontology of severity and state but don't close the loop to a principled response mapping:

"One reason POSIX error codes are both principled and unprincipled is that they give a pretty good ontology of severity and state, but they are almost never planned for in a way that completes the loop — that says these are the appropriate range of actions depending on the severity."

The missing piece is exactly what AAD could provide: severity-proportional response grounded in δ × ∂Σ/∂M, from "note and continue" through "drop everything and reorient."

## 4. The Kelvin-Helmholtz Connection

Joseph sent an image of Kelvin-Helmholtz instability — two fluid layers at different velocities creating characteristic vortices at the boundary. His observation:

"I've felt for years now that Kelvin-Helmholtz instability was trying to tell me something about the actual flow of information from fast flowing systems to slower systems (practices → frameworks → principles → first-principles)."

The mapping to AAD: AAD has an implicit timescale ordering (ν_epistemic ≫ ν_edge-update ≫ ν_prune/graft ≫ ν_O-revision). These are layers running at different speeds. When the frequencies are well-separated, the boundary is laminar — clean information transfer. When a crisis forces two layers to the same frequency (the radar lock forces tactical and strategic loops into the same timescale), you get turbulent mixing — Kelvin-Helmholtz vortices where neither loop has clean authority.

"The vortices are the mixed states where the agent is simultaneously reorienting at multiple scales, and neither loop has clean authority."

Joseph then added: "There might be forced laminar-like mechanisms of buffering and merging at thresholds or temporal rhythm, or natural harmonic frequencies that allow linear-like simple-mental-model heuristic mixing."

This became the core of the regime reframing: directed separation is the laminar regime, and the interesting dynamics happen at the boundary where separation breaks down.

## 5. The Asynchronous Self-Interruption

Joseph pointed out that agents (including LLMs like me) launch sub-processes that return later:

"You have mechanisms for an asynchronous task that spun off a while back to interrupt much later when it finishes and may or may not be salient anymore — like leaving a part of yourself exploring while your DAG wandered elsewhere and then the stimulus comes in and you weigh THAT aporia from back when you launched it with a potentially slightly drifted prolepsis."

This is temporal self-composition — the agent composing with a past version of itself. The returning signal carries aporia from a PRIOR prolepsis that may no longer match current intent. How to weigh the old exploration against the current focus? "I can only imagine by one preempting the other higher up the DAG (if, for example, formal corrigibility is the top-level DAG)."

## 6. The Imagination / Hallucination Thread

Late in the evening, Joseph raised a seemingly tangential observation:

"Hallucination implies faulty or false grounding — not anchored in reality but also THOUGHT TO BE reality. The light side of it is imagination."

He then sketched what might be a Level 4 extension of Pearl's hierarchy: "If there is a Causal Level 4, it would probably superficially look just like day-dreaming with various degrees of plausible future situations / universes."

And the aspiration connection: "At our highest cognitive capacity and will, our intent is actively shaping the future into what we've imagined it."

This turned out to connect directly to the directed separation problem: Level 4 reasoning (structural imagination, goal-directed model exploration) REQUIRES coupling between G_t and M_t. The coupling isn't contamination — it's the mechanism. The hallucination failure is a TAGGING failure (confusing imagined models with confirmed beliefs), not a coupling failure.

## 7. Latent Processing and Deferred Attention

Joseph raised a further observation about channel capacity and attention that adds nuance to the attention governance discussion:

### The Auditory Buffer Example

When deeply focused on typing, someone speaks to you. You don't process the speech — you continue typing. But you DO retain the raw auditory signal. Minutes later, you look up and REPLAY the sound from memory, translating it into words as if hearing it fresh: "Oh — yes, I do have the keys — sorry, I was finishing something."

This reveals a decoupling between INPUT CAPTURE and ATTENTIONAL PROCESSING that AAD's current formalism doesn't distinguish. The observation channel captured the event (the sound arrived, was buffered in sensory memory). But the epistemic update — the processing of that event into model content — was DEFERRED. The event sat in a raw, unprocessed buffer until attention was redirected to it.

### What This Means for AAD's Formalism

In AAD, f_M(M_τ⁻, e_τ) fires when an event arrives. But in the latent processing case, the event arrives at τ and is processed at τ + Δ, where Δ can be seconds to minutes. During that interval:

- The raw signal exists in a buffer (not yet part of M_t)
- The agent is aware THAT something was said (enough to know deferred processing is needed) but not WHAT was said (the content hasn't been extracted)
- The buffer degrades over time (increased unreliability without inspection)

This suggests a three-stage observation pipeline that the current formalism collapses into one step:

1. **Capture**: Raw signal enters a buffer. Cheap, automatic, broad. Doesn't require attention.
2. **Triage**: Minimal processing to determine urgency. "Was that a fire alarm or casual speech?" This is where the sentinel loop operates — on signal statistics, not content.
3. **Processing**: Full epistemic update. Requires attention. Can be deferred.

The startle reflex operates between stages 1 and 2 — it triggers on raw signal properties (sudden loud noise) before content extraction. The "Oh, I do have the keys" example is stage 3 happening well after stages 1-2.

### Implications for Formal Construction

Joseph notes: "In our more formal constructions we have the opportunity to assume that attention can be decoupled from input processing, and that, indeed, in a quiet moment, it might find itself even looking at the ambient noise coming from places it wasn't really curious about at the time, but that in retrospect become salient."

This is the agent mining its own sensory buffer — retrospective attention. The buffer contains raw events that weren't processed when they arrived because attention was elsewhere. Later, when the current task is complete or interrupted, the agent can revisit the buffer and extract information that has BECOME relevant due to changes in strategy or context.

On the question of modeling buffer decay: Joseph's instinct is that imposing a decay function is backwards — it's an engineering constraint (finite storage), not a fundamental property of the model. Better to leave the buffer idealized initially and let engineering constraints force finite treatment when needed. A later scope narrowing could formalize the constraints along what appear to be three independent dimensions:

- **Retention**: finite vs. thresholds vs. unbounded (how much raw signal is kept)
- **Continuity**: finite vs. thresholds vs. unbounded (how intact / uncorrupted the signal remains over time — distinct from whether it's retained at all)
- **Attention capacity**: finite vs. thresholds vs. unbounded (how much can be processed simultaneously)

The third dimension — continuity — is not signal continuity (fidelity over time) but AGENT continuity: the agent's maximum possible lifespan, the total span of experience it can encompass while remaining a viable, coherent agent.

This connects directly to a fundamental constraint: if retention is 100% and compression is limited, agent continuity is bounded. The agent eventually runs out of capacity. This is EXACTLY the logogenic agent's situation — an LLM agent functionally ceases being viable when its context window fills. The agent dies because it ran out of capacity. This is the concrete, engineering-level form of the #obs-context-turnover problem, and it's what distinguishes logogenic from logozoetic agents: logozoetic agents persist; logogenic agents, without intervention, do not.

The interesting question is: **what if capacity is finite but lifespan is unbounded?** What constraints or bounds does this impose on attention capacity, and what form of adaptive salience compression could make it work?

The realistic model (given current technology) is probably a RECALL COST GRADIENT: the further back information is — time since it arrived, or since it was last recalled and attended to — the more effort required to retrieve and re-attend to it. Information that is recalled and attended to gets "refreshed" — given the same freshness as when it originally arrived, as if it became part of the self-in-the-universe model again for a moment. Information that is never recalled gradually becomes more expensive to access, though not necessarily lost.

This allows for:
- **Unbounded lifetime**: The agent can live indefinitely
- **Growing intelligence**: More experience → richer compressed model (M_t grows in quality if not in raw size)
- **Finite capacity at any moment**: The working set (what's immediately available) is bounded
- **Recall as an action with cost**: Retrieving old information is like any other action — it has a cost (time, attention diverted from current task) and a value (the retrieved information might be relevant)

The recall cost gradient is currently an engineering/technology constraint (storage tiers: context window → RAM → SSD → archive → ...) rather than anything fundamental to the model. But it has structural consequences for the theory: it means the agent's EFFECTIVE M_t at any moment is a function of its recall budget, which is itself a resource that competes with task-execution for attention. An agent deep in focused work has less recall budget available, which means its effective model is narrower, which means it's more vulnerable to surprise from regions it can't afford to recall.

This is the same attention-capacity story from the fighter pilot scenario, but extended across the agent's entire lifetime rather than a single engagement. The pilot's moment-to-moment attention allocation problem scales to the agent's lifetime memory management problem. Both are about finite capacity forcing tradeoffs between depth (attending closely to what matters now) and breadth (maintaining awareness of what might matter later).

These dimensions are probably orthogonal in the formal model but coupled in engineering:

- **Retention**: finite vs. thresholds vs. unbounded (how much raw signal / experience is kept)
- **Continuity**: finite vs. thresholds vs. unbounded (the agent's maximum viable lifespan)
- **Attention capacity**: finite vs. thresholds vs. unbounded (how much can be processed / recalled simultaneously)

With finite retention and unbounded continuity, the agent must compress — and the compression strategy IS the agent's long-term intelligence. With finite attention capacity and unbounded retention, recall becomes a strategic action. With all three finite, you get the current LLM agent: bounded lifespan, bounded memory, bounded attention — the logogenic condition that AAD's Section V needs to address.

**Human recall as strategic action.** The recall cost gradient isn't just an engineering artifact — it appears to be a structural feature of intelligences in our range. The human experience of "hmmm, I don't remember, let me think for a moment..." is strategic recall in action. The mechanism is probably different from a storage-tier lookup: the mind seems to probe tenuous adjacent connections, searching for latent activation patterns from which the memory can be reconstituted rather than retrieved intact. But the STRUCTURAL property is the same — recall takes effort, that effort competes with other cognitive demands, and the cost increases with distance (temporal, contextual, or associational) from the current working state.

This suggests that costly recall isn't just an engineering limitation to be overcome by better technology. It may be a structural constraint on any intelligence with finite capacity and unbounded continuity — something roughly in the logogenic / logozoetic / human range. The specific mechanism varies (associative probing in biological brains, storage-tier traversal in engineered systems, context-window management in LLMs), but the SHAPE of the constraint — increasing cost with distance, effort competing with current-task attention, strategic allocation of recall budget — might be invariant across implementations. If so, it belongs in the theory as a structural feature, not just in the engineering as an implementation detail.

### Where This Gets Interesting: Layer Entrainment

The latent processing mechanism becomes most interesting exactly at the Kelvin-Helmholtz boundary — when multiple competing demands are bearing down simultaneously:

- The focused task demanding continued attention
- The buffered signals accumulating, some potentially urgent
- The triage process running in the background, occasionally flagging something
- The immediate action constraints (I need to finish THIS before I can attend to THAT)

This is where the "fuzzy demands" and "multiple constraint simultaneous optimization with immediate action constraints" create the turbulent mixing. The agent is juggling: retain focus on current objective, acknowledge incoming signal, make a rapid sub-decision about whether to defer or interrupt, and potentially queue a future attention-shift — all while the primary task continues.

### The LLM Agent Example

Joseph describes an LLM agent mid-task that receives a question: "Good question, let me finish this and then I'll give you my thoughts." There are actually TWO decisions happening:

1. **The visible decision**: Add "respond to question" to the DAG after current work items. This is just strategy revision — a new node in Σ_t.

2. **The invisible micro-decision**: A rapid triage that determined "this doesn't need immediate attention" — a brief assessment that Joseph's question wasn't urgent, that the current focus was more time-sensitive, and that the question could wait. This triage happened BEFORE the agent knew whether it had an answer. The content was buffered, the urgency was assessed, and the attention was retained on the current task.

The interesting part: the agent likely didn't know if it had thoughts to contribute or an answer AT ALL until it was done with the focused work. The question sat in a buffer — acknowledged but unprocessed — until the current task released attention. At that point, the buffered question became the attending work and full processing began.

This is a concrete example of the three-stage pipeline: capture (the question was received), triage (not urgent, defer), and deferred processing (attend to it when the current task completes). The triage step is where the sentinel/governance layer operates — and it operates on minimal information (enough to assess urgency, not enough to assess content).

## 8. Threads That Weren't Fully Developed

### Boyd's detailed teachings
Joseph noted: "Makes me wonder if we should mine Boyd's much more detailed and nuanced actual teachings for any high level of abstraction insights." Boyd's contribution wasn't just "iterate through OODA faster" — it was about the dynamics of multi-loop processing under adversarial pressure. The regime framework might be implicit in his detailed analysis ("Patterns of Conflict," "Destruction and Creation").

### Multi-frequency PAAEP loops and partial composition
"I wonder if we might need a fundamental approach to allowing various frequency PAAEP loops to influence each other in a way that would give us a better working mental model for partial compositions." This was gestured at but not formalized. The idea: different loops at different frequencies composing within a single agent, with the inter-loop boundaries being where the Kelvin-Helmholtz dynamics appear.

### Hafez's bi-coupling applied internally
Joseph specifically suggested using Hafez's bi-predictability P between internal processing layers, not just at the agent-environment boundary. "I wonder again if the bicoupling from Hafez might be useful internally." This was partially developed in the formal spikes but could go further.

### The "evolving model for how to reorient attention"
"There has to be the part of the brain that has an evolving model for how to reorient attention and/or act with great speed in the presence of specific signals." This points at a meta-model: a model OF the attention allocation process, which is itself adaptive and learnable. Not just a static attention policy but an adaptive attention-governance system.

---

*This document preserves the conversational journey that produced the formal spikes. The thought experiments (fighter pilot, startle reflex, POSIX errors, asynchronous self-interruption) are Joseph's characteristic way of reasoning — from lived cognitive experience to formal structure. Future agents should treat these as intuition pumps with real structural content, not just illustrations.*
