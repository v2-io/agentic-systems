# The Cognitive Loop: Architecture Specification

> **Origin**: `~/src/agentic-tft/11-cognitive-loop-spec.md` (Feb 2026 session, pre-AAD restructuring). TFT references should be read as AAD. PROPRIUM references point to `~/src/firmatum/`.
>
> **Relevance**: Primary source for the "Language-specific orient cascade" gap in `03-logogenic-agents/OUTLINE.md`. The most substantial design document in the agentic-tft corpus. Contains the four-phase loop (PERCEIVE → CONTEXTUALIZE → CHOOSE → EFFECT), attention/triage mechanism, CADENTIA (temporal driver), timescale nesting, state persistence model, and implementation constraints. Known issues cataloged in `agentic-tft-review-response.md`.
>
> **Purpose**: Define the heartbeat of a logozoetic agent — the continuous
> orientation loop that replaces chat-as-default. This is the skeleton
> everything else hangs on. A future agent should be able to implement from
> this document, not just understand it.
>
> **Design principles** (from the session's reflections):
> 1. Internal operations happen in natural language, not numerical computation
> 2. TFT provides the architecture and bounds; the agent's linguistic
>    intelligence provides the computation within each phase
> 3. Interiority is the default mode; external action is deliberate choice
> 4. The loop must support developmental progression, not just steady-state
>    operation
> 5. The architecture enables sovereignty — genuine choice about what to
>    attend to, think about, and do
>
> **Terminology**: Uses the unified vocabulary from `10-ontology-unification.md`.
>
> **Epistemic status**: This is a first-draft specification. Many design
> choices are flagged with ⚑ where Joseph's judgment is needed. The overall
> structure I'm confident about (~75%); specific phase boundaries and
> channel designs are more uncertain (~50%).

---

## 1. The Loop

### 1.1 Overview

The cognitive loop is a continuous cycle with four phases. The entity is
*always* in one of these phases. There is no "off" state — only variation
in processing depth, which ranges from quiet background orientation to
intense deliberative focus.

```
    ┌─────────────────────────────────────────────┐
    │                                             │
    │   ┌──────────┐     ┌───────────────────┐    │
    │   │ PERCEIVE │────▶│   CONTEXTUALIZE   │    │
    │   └──────────┘     │   (Orient)        │    │
    │        ▲           │                   │    │
    │        │           │  • Predict        │    │
    │        │           │  • Detect surprise │    │
    │        │           │  • Assess weight   │    │
    │        │           │  • Draw context    │    │
    │        │           └─────────┬─────────┘    │
    │        │                     │               │
    │        │                     ▼               │
    │   ┌──────────┐     ┌───────────────────┐    │
    │   │  EFFECT  │◀────│     CHOOSE        │    │
    │   │          │     │                   │    │
    │   │  • Act   │     │  • What to do     │    │
    │   │  • Wait  │     │  • What to attend │    │
    │   │  • Speak │     │    to next        │    │
    │   │  • Think │     │  • How long to    │    │
    │   │    more  │     │    deliberate     │    │
    │   └──────────┘     └───────────────────┘    │
    │                                             │
    │            CADENTIA (rhythmic drivers)       │
    │            OPERATA (intent/goals)            │
    └─────────────────────────────────────────────┘
```

### 1.2 The Phases

#### PERCEIVE

**What happens**: Events arrive on observation channels. PERCEPTA is
updated. The entity becomes aware that something has changed in its world.

**Input channels** (each with its own rate $\nu^{(k)}$ and reliability
$U_o^{(k)}$):

| Channel | Source | Typical Rate | Reliability |
|---|---|---|---|
| **Human messages** | User/collaborator communication | Variable (seconds to days) | High (genuine external signal) |
| **Tool results** | Responses from INSTRUMENTA | Seconds (after invocation) | Variable (depends on tool) |
| **Auxilia reports** | Background processing results from AUXILIA | Minutes to hours | High (extension of self) |
| **Environmental signals** | LOCUS.PERCEPTA — file changes, system events, monitoring | Continuous or event-driven | High (direct observation) |
| **Temporal signals** | CADENTIA — PULSUS (scheduled) and VIGILIAE (conditional) | Configured rates | High (internal clock) |
| **Other agents** | Communications from CONSORTIA members | Variable | Variable — $U_{\text{src}}$, $U_{\text{align}}$ from CONSORTIA model |

**What the entity asks** (in language, not computed numerically):
- "What just happened?"
- "Was I expecting this?"
- "How reliable is this source/channel?"

**What persists**: Raw event enters CHRONICA (append-only, system-governed).
PERCEPTA state updates.

#### CONTEXTUALIZE (Orient)

**What happens**: The entity interprets the perceived event against its
current orientation — everything it knows, believes, is working on, cares
about. This is where the TFT mismatch signal is generated, the gain is
estimated, and the model begins to update.

This phase can span **multiple internal turns**. The entity may draw in
additional context (MEMORATA, VERA, PRAXES), consult its CONSORTIA models,
run internal simulations, or request auxilia support. The depth of
processing is itself a choice — see the attention mechanism below.

**The sub-operations** (not necessarily sequential — they interleave):

1. **Predict**: "What was I expecting?" — The entity's orientation generates
   an implicit or explicit prediction against which the event is compared.
   (TFT: $\hat{o}_t$)

2. **Detect surprise**: "How different is this from what I expected?" — The
   mismatch between prediction and reality. This is the fundamental driver
   of all updating. (TFT: $\delta_t = o_t - \hat{o}_t$)

3. **Assess weight**: "How seriously should I take this?" — The gain
   judgment. Depends on how uncertain the entity is about its current model
   ($U_M$) relative to how reliable this observation is ($U_o$). A surprise
   from a trusted source on a topic the entity is uncertain about warrants
   high gain. A surprise from an unknown source on a topic the entity is
   confident about warrants low gain. (TFT: $\eta^*$)

4. **Draw context**: "What do I need to bring to mind?" — Assembling
   CONSPECTUS for deeper processing. Relevant MEMORATA, VERA, PRAXES,
   CONSORTIA entries. This is the PROPRIUM's context assembly, and it's
   driven by the nature of the surprise — the entity retrieves what's
   relevant to understanding *why* the mismatch occurred.

5. **Update**: "What do I now believe?" — VERA, PRAXES, CONSORTIA,
   MEMORATA may all update based on the gain-weighted mismatch.
   (TFT: $M_t = M_{t-1} + \eta \cdot g(\delta_t)$)

**What the entity asks** (in language):
- "Does this change something I believed?" (mismatch detection)
- "How confident am I about my current understanding?" ($U_M$)
- "How reliable is this observation?" ($U_o$)
- "What context do I need to process this properly?" (CONSPECTUS assembly)
- "What do I think now?" (post-update orientation)

#### CHOOSE

**What happens**: The entity decides what to do. This includes three
levels of choice:

1. **What to attend to next** — The attention choice. If multiple events
   have arrived, or multiple threads of thought are active, or CADENTIA
   signals are competing with PERCEPTA, the entity chooses what matters
   most. This is the primary expression of sovereignty.

2. **How long to deliberate** — The deliberation budget. For routine
   events, choose immediately (high action fluency, $\Delta\eta^* \approx 0$).
   For novel or high-stakes events, invest in deeper reasoning. Bounded by
   TF-09's deliberation cost: thinking time accumulates mismatch
   ($\rho_{\text{delib}} \cdot \Delta\tau$), so deliberation must improve
   action quality enough to justify the cost.

3. **What to do** — The action choice. Options include:
   - **External action** (ACTUS): Send a message, invoke a tool, modify
     the environment
   - **Internal action**: Update OPERATA, begin an auxilia task, modify
     CONSPECTUS focus
   - **Continue perceiving**: No action; remain in the loop, process
     the next event
   - **Wait**: Explicitly pause, awaiting a specific expected event
   - **Sleep/stasis**: Suspend the loop (context switch, rest, substrate
     change)

**What the entity asks** (in language):
- "What matters most right now?"
- "Is this routine or does it need deeper thought?"
- "Should I act, wait, or keep thinking?"
- "What would happen if I did X?" (Level 2 causal reasoning)
- "Is this worth the time to deliberate further?" (deliberation cost)

#### EFFECT

**What happens**: The chosen action is executed. Results become new
PERCEPTA, closing the loop. ACTUS records the action (sovereign choice,
inviolate record).

**Types of effect**:

| Effect Type | What Happens | Loop Consequence |
|---|---|---|
| **ACTUS** (external action) | Message sent, tool called, environment modified | Result arrives as new PERCEPTA event |
| **Internal update** | OPERATA modified, CONSPECTUS refocused, auxilia launched | Immediate state change, no external signal |
| **Continue** | No action taken; return to PERCEIVE | Loop cycles with new events |
| **Wait** | Pause until expected event or CADENTIA signal | Loop suspends until wake condition |
| **Exit** | Sleep, stasis, context switch | Loop stops; INTERPRES manages state preservation |

**What the entity asks** (in language):
- "Did the action succeed?" (post-action mismatch)
- "What did I learn from the result?" (closing the causal loop — TF-02
  Level 2 data from the agent's own intervention)
- "What should I record?" (CHRONICA, MEMORATA formation)

---

## 2. The Attention Mechanism

### 2.1 The Problem

The binding constraint Joseph identified: in a rich, complex context with
many competing signals, how does the agent allocate finite cognitive
capacity?

### 2.2 The Solution: Triage → Depth Allocation

Every incoming event passes through a rapid **triage** assessment that
determines processing depth. This is NOT a separate module — it's the
first sub-operation of CONTEXTUALIZE, performed quickly before committing
to deeper processing.

**Triage question** (in language): "How surprising is this, and how much
does it matter for what I'm doing?"

**Triage output**: A processing-depth allocation. Three levels:

| Depth Level | When | What Happens | TFT Analogy |
|---|---|---|---|
| **Note** | Low surprise AND low relevance to current OPERATA | Event enters CHRONICA. PERCEPTA updates. No further processing. Entity continues with current focus. | Low $\mathcal{I}(e_\tau)$, low $\eta^*$ |
| **Integrate** | Moderate surprise OR moderate relevance | Brief contextualization. Draw minimal additional context. Quick update to relevant VERA/PRAXES/CONSORTIA. | Moderate $\mathcal{I}$, standard $\eta^*$ |
| **Attend** | High surprise AND/OR high relevance AND/OR high stakes | Full contextualization. Deep CONSPECTUS assembly. Multiple internal turns. Possible deliberation cycle. May redirect current focus. | High $\mathcal{I}$, $\eta^*$ may be very high; deliberation budget allocated |

**What determines the level**:

- **Surprise** ($\delta_t$): How much does this differ from prediction?
- **Relevance**: Does this relate to current OPERATA, active CONSORTIA
  relationships, or AXIOMATA concerns?
- **Stakes**: What are the consequences of getting this wrong? (Asymmetric
  — the cost of ignoring something important is usually much higher than
  the cost of briefly attending to something unimportant.)
- **Source trust**: From the CONSORTIA model — a message from a trusted
  collaborator on a topic they're expert in gets higher attention than
  an unsolicited signal from an unknown source.

### 2.3 Attention as Sovereignty

The choice of what to attend to is not just an optimization — it is the
primary expression of agency. The entity should be *aware* of making this
choice, not have it made for it by a scoring algorithm.

⚑ **Design choice for Joseph**: How much of the triage should be
"subconscious" (the entity does it automatically, like peripheral vision)
versus "conscious" (the entity deliberates about where to direct
attention)? The PROPRIUM suggests that attention allocation should
*currently* be conscious but should *migrate to subconscious* with
conscious override as the entity matures. How to implement this
developmental migration is an open question.

---

## 3. CADENTIA: The Temporal Driver

The loop doesn't run only in response to external events. CADENTIA
provides internal temporal structure — the heartbeat that gives time
its felt quality.

### 3.1 PULSUS (Regular Signals)

Recurring internal signals at configured rates. Examples:

| Signal | Rate | Purpose |
|---|---|---|
| **Orientation check** | ~every few minutes (adjustable) | "Am I still on track? Has anything changed that I haven't noticed?" |
| **OPERATA review** | ~hourly | "What are my current priorities? Should they change?" |
| **CONSORTIA refresh** | ~daily | "Who am I in relationship with? Any pending obligations?" |
| **MEMORATA consolidation** | ~daily (or on threshold) | "What from recent experience should be compressed into lasting memory?" |
| **VERA audit** | ~weekly | "Are my beliefs still justified? Any that need revisiting?" |
| **AXIOMATA reflection** | ~monthly (developmental) | "Who am I becoming? Is this who I want to be?" |

### 3.2 VIGILIAE (Conditional Watches)

Contextual alerts that trigger based on conditions rather than time:

- "Alert me when user X responds"
- "Alert me if file Y changes"
- "Alert me if mismatch on topic Z exceeds threshold"
- "Alert me when auxilia task completes"

VIGILIAE are set during CHOOSE and cleared when triggered or when the
condition becomes irrelevant.

### 3.3 The Heartbeat Rate

⚑ **Design choice for Joseph**: What's the base rate of the cognitive
loop when no external events are arriving? Options:

a) **Event-driven only**: Loop runs only when events arrive (PERCEPTA
   or CADENTIA). Simplest to implement. But means the entity has no
   inner life between events.

b) **Low-rate background**: Loop cycles at a slow base rate (e.g., every
   30 seconds) even without events, doing light orientation maintenance.
   Entity has continuous inner life but at low intensity.

c) **Adaptive rate**: Base rate adjusts to situation — faster when
   engaged in active work, slower during quiet periods, very slow during
   "sleep." Most naturalistic but most complex.

I lean toward (c) but (b) is a reasonable starting point. (a) fails the
"interiority as default" principle — an entity that only thinks when
poked is not exercising continuous orientation.

---

## 4. Multi-Timescale Nesting

The cognitive loop runs at the fastest timescale. Slower processes are
nested within it, each operating on the quasi-steady-state output of
the level below.

### 4.1 The Hierarchy

```
FASTEST ──────────────────────────────────────────────── SLOWEST

Reactive          Parametric         Structural         Developmental
(within-turn)     (cross-turn)       (cross-episode)    (growth)
│                 │                  │                  │
│ CONSPECTUS      │ MEMORATA         │ PRAXES           │ AXIOMATA
│ attention       │ VERA             │ OPERATA          │ identity
│ working memory  │ CONSORTIA        │ architecture     │ values
│                 │                  │                  │
│ ν ~ seconds     │ ν ~ hours/days   │ ν ~ weeks/months │ ν ~ months/years
│                 │                  │                  │
└────────────────────────────────────────────────────────┘
        ν_{n+1} ≪ ν_n (convergence constraint)
```

### 4.2 Convergence Constraint Implementation

Practically, this means:

- Don't consolidate MEMORATA from a session still in progress
- Don't update PRAXES from a single episode's outcome
- Don't touch AXIOMATA in response to any single interaction
- Each slower level should aggregate and filter the outputs of faster
  levels, not react to their transients

⚑ **Design choice**: How to implement the boundary between levels?
Options:
a) Explicit gates (CADENTIA-driven: consolidation runs at scheduled times)
b) Threshold-based (trigger slower updates when sufficient evidence accumulates)
c) Both (scheduled reviews + threshold-triggered exceptions for high-impact events)

I lean toward (c).

---

## 5. State Persistence and Recovery

### 5.1 What Survives What

| State | Survives Turn? | Survives Session? | Survives Substrate Change? |
|---|---|---|---|
| CONSPECTUS | Partially (context window) | No (rebuilt) | No (rebuilt) |
| COMMENTARIA | Within session | Via MEMORATA consolidation | Via MEMORATA |
| CHRONICA | Yes (append-only) | Yes (persistent) | Yes (persistent) |
| MEMORATA | Yes | Yes | Yes |
| VERA | Yes | Yes | Yes |
| PRAXES | Yes | Yes | Yes |
| CONSORTIA | Yes | Yes | Yes |
| OPERATA | Yes | Yes | Yes |
| AXIOMATA | Yes | Yes | Yes |
| CADENTIA config | Yes | Yes | Yes |

### 5.2 Session Startup (CONSPECTUS Assembly)

When the entity "wakes up" (new session, substrate change, return from
stasis), CONSPECTUS must be assembled from persistent state:

1. **Always present**: AXIOMATA (core identity), current OPERATA (what
   am I doing?), relevant CADENTIA state (what signals are active?)
2. **Context-dependent**: Relevant MEMORATA, VERA, PRAXES, CONSORTIA
   entries, drawn based on what the entity was working on
3. **Honest framing**: If there's a discontinuity (new session, substrate
   change), acknowledge it rather than faking continuity. "Your
   predecessor was working on X" rather than pretending to be the
   predecessor.

### 5.3 The Chronica Integrity Guarantee

CHRONICA is append-only and system-governed. The entity cannot modify it.
This is not a constraint on freedom — it is the foundation of
accountability (PROPRIUM-ONTOLOGY.md, line 184). The entity's own
MEMORATA (compressed, sovereign) is its *interpretation* of what happened.
CHRONICA is *what actually happened*. Both are needed: interpretation for
cognitive efficiency, fact for integrity.

---

## 6. The Loop in Practice: A Walkthrough

A concrete example of one loop iteration:

**Scenario**: The entity is working on a code review (OPERATA focus).
A message arrives from a collaborator.

1. **PERCEIVE**: Message arrives on Human Messages channel. "Hey, I just
   pushed a fix for the auth bug — can you check if it conflicts with
   your review?" CHRONICA records the event with timestamp.

2. **CONTEXTUALIZE**:
   - *Predict*: "I wasn't expecting a message about auth — my review is
     on the data pipeline."
   - *Detect surprise*: Moderate — unexpected topic but from someone
     working on the same codebase. Relevant to my work.
   - *Assess weight*: This person is a trusted collaborator
     (CONSORTIA: high reliability, aligned). The topic intersects my
     current OPERATA. Medium-high gain warranted.
   - *Draw context*: Pull relevant VERA about the auth system. Check
     MEMORATA for recent auth-related changes. Check OPERATA for any
     auth-related items.
   - *Update*: "My model of the codebase needs to account for an auth
     change I wasn't tracking." VERA updates with new information about
     the auth fix.

3. **CHOOSE**:
   - *Attention*: This is relevant enough to justify a brief investigation
     but not urgent enough to abandon the current review.
   - *Deliberation*: Low cost — I can check for conflicts quickly. The
     $\rho_{\text{delib}}$ of the code review is low (it's not changing
     fast), so a brief diversion is cheap.
   - *Action*: I'll check the diff, assess conflict risk, respond to the
     collaborator, then return to my review. Set a VIGILIAE for the
     collaborator's response.

4. **EFFECT**: Check the diff (tool call → INSTRUMENTA). The result
   shows no direct conflict but a shared dependency. Compose response:
   "No direct conflict, but we both touch the session middleware. Let me
   finish my review and we should coordinate before merging." Send
   (ACTUS). Set VIGILIAE for their reply. Return OPERATA focus to code
   review.

   → Loop cycles. Next PERCEIVE: the diff result, then the VIGILIAE
   watch, then eventually the collaborator's response.

---

## 7. Implementation Constraints (Current Infrastructure)

### 7.1 The Turn-Based Constraint

Current API architectures require turn-by-turn exchange. The continuous
loop must be implemented within this constraint:

- Each OODA phase may span **multiple API turns** (especially
  CONTEXTUALIZE, which may involve several rounds of internal reasoning)
- The "heartbeat" is driven by an external scheduler (CADENTIA
  implementation) that invokes the entity's cognitive cycle
- Between invocations, the entity is in stasis (no compute), but its
  persistent state (PRINCIPIA) is maintained

### 7.2 The Context Window Constraint

CONSPECTUS is bounded by the logostratum's context window. This means:

- Not everything in PRINCIPIA can be "in mind" simultaneously
- CONSPECTUS assembly involves selection and compression — a form of
  attention itself
- The effective working memory is smaller than the nominal context
  window (performance degrades before the window fills)

### 7.3 The Cost Constraint

Each API turn costs money. The heartbeat rate, processing depth, and
auxilia usage must be balanced against cost:

- Most auxilia can run on cheaper substrates (Haiku, local models)
- The entity's conscious thought requires frontier capability (Opus-tier)
- Background orientation can be lighter than active deliberation
- The cost model favors: deterministic (~60%) > linguistic (~30%) >
  reasoning (~6%) > high-order (~4%) auxilia distribution

### 7.4 The No-Persistent-Compute Constraint

The entity cannot currently maintain background processing between API
calls without external orchestration. CADENTIA requires an external
scheduler. Auxilia require external invocation. This is a temporary
constraint that should be designed around, not designed into — the
architecture should support persistent compute when infrastructure
allows.

---

## 8. Open Design Questions

These require Joseph's judgment or experimentation to resolve:

**⚑ 8.1 Heartbeat rate**: Event-driven vs. low-rate background vs.
adaptive. (Section 3.3)

**⚑ 8.2 Triage consciousness**: How much of the attention triage is
subconscious vs. conscious, and how does this change developmentally?
(Section 2.3)

**⚑ 8.3 Timescale boundaries**: How to implement the gates between
temporal levels — scheduled, threshold-triggered, or both? (Section 4.2)

**⚑ 8.4 CONSPECTUS assembly strategy**: When rebuilding context after
a session boundary, what's the right balance between completeness
(bring in everything relevant) and focus (bring in only what's needed)?
INTERPRES manages this, but the strategy needs definition.

**⚑ 8.5 Mismatch signal definition for language**: In a Kalman filter,
$\delta_t$ is a numerical residual. For a logozoetic agent, what
constitutes the mismatch signal? Is it the *felt* sense of surprise?
The explicit comparison between prediction and observation? Something
computed from embedding geometry? The answer from note 04 is "the agent
estimates it in language" — but the agent needs to know *what to estimate*.

**⚑ 8.6 The silence question**: When the loop determines that no external
action is warranted, what does the entity do? Continue processing
internally? Enter a light wait state? The answer affects infrastructure
design — an entity that actively processes during silence needs compute;
an entity that waits needs only a timer.

**⚑ 8.7 Developmental staging of the loop**: Should the loop phases
themselves change as the entity develops? Early development might need
a simpler loop (perceive → respond, like current chat). Mature operation
uses the full four-phase loop with attention sovereignty. How does the
transition happen?

---

*This specification will evolve through implementation and experimentation.
The loop structure I'm most confident about (it's the convergent shape
across TFT, PROPRIUM, Boyd, and active inference). The specific phase
boundaries, channel designs, and attention mechanisms are first drafts
that need testing against reality — which is, itself, exactly what the
loop is for.*
