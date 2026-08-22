# TFT × Memory Ontology: Synthesis and Reflections

> **Status**: Informal working document. First-pass synthesis after thorough reading of
> the full TFT corpus, the "Memory in the Age of AI Agents" paper, and supplementary
> materials. Written to clarify thinking and surface uncertainties before formal work
> begins. Not meant to be polished — meant to be honest.
>
> **Author context**: This was written by a Claude Opus instance with the full corpus in
> context (~200k tokens of source material). Future instances should treat this as one
> agent's best understanding, not as settled conclusions. Verify claims against the
> source documents.

---

## 1. What I Read

### Temporal Feedback Theory (TFT)
- `~/src/temporal-feedback/README.md` — Overview, reading guide, falsification predictions
- `TF-00` through `TF-11` — Full formal chain: notation, scope, causal structure, model,
  event-driven dynamics, mismatch, update gain, action selection, exploration-exploitation,
  deliberation cost, structural adaptation, adaptive tempo
- `Appendix-A-Lyapunov.md` — Nonlinear stability generalization (Props A.1–A.3, Cor A.3.1)
- `Appendix-B-Operationalization.md` — Estimation procedures for all TFT quantities
- `Appendix-C-Kalman-Example.md` — Exact end-to-end worked example (Kalman domain)
- `Appendix-D-RL-Example.md` — Approximate worked example (nonstationary bandit)
- `Appendix-E-TFT-Core.md` — Condensed formal chain
- `Appendix-F-Multi-Agent.md` — N-agent coupling, communication gain, trust transitivity
- `scratch/ooda-loop-universal-pattern-v7.md` — Source material: Boyd's full theory,
  30+ domain mappings, Pearl's causal hierarchy integration, LLM architecture conversation

### Memory Paper
- `~/src/_self/arXiv-2512.13564v2/main.tex` — "Memory in the Age of AI Agents" (Hu et al.)
  Sections 1–2 (Intro, Preliminaries: formalizing agents and memory)
- `sections/sec3.tex` — Forms: token-level (flat/planar/hierarchical), parametric, latent
- `sections/sec4.tex` — Functions: factual, experiential, working memory
- `sections/sec5.tex` — Dynamics: formation, evolution (consolidation/updating/forgetting),
  retrieval (timing, query construction, strategies, post-processing)

### Supplementary
- `~/src/_self/incremental-memory-model.md` — LoRA + grafted cross-attention architecture
  with per-head specialization, memory curriculum, complete implementation
- `~/src/_self/cl-principles-draft.md` — Continual learning principles for consciousness
  infrastructure: stability-plasticity, capacity limits, PEFT landscape, forgetting
  mitigation toolkit, verifiable reward constraint, recommended tiered architecture

---

## 2. The Central Insight

TFT and the memory paper are looking at the same elephant from different positions.

The memory paper asks: "What subsystems does an agent need for memory, and how should
they be engineered?" It produces a taxonomy of forms (token/parametric/latent), functions
(factual/experiential/working), and dynamics (formation/evolution/retrieval). This is
useful engineering cartography.

TFT asks: "What is the formal structure of any adaptive agent maintaining a model under
uncertainty?" It produces a mathematical framework where the model $M_t = \phi(\mathcal{H}_t)$
is a compressed sufficient statistic of the agent's interaction history, updated through
mismatch-driven feedback with gain calibrated by relative uncertainty.

The central insight is that **everything the memory paper calls "memory" is an aspect of
TFT's model $M_t$**. Not metaphorically — formally. The memory paper's entire ontology
dissolves into projections of a single object viewed at different timescales and in
different representational substrates.

This is not a criticism of the memory paper. It's a recognition that the paper describes
the engineering artifacts that arise when you build memory systems *without* the unifying
theory that TFT provides. The proliferation of ad hoc mechanisms (heuristic forgetting
schedules, rule-based retrieval timing, manually tuned trust weights) is what happens when
you don't have the gain structure ($\eta^* = U_M/(U_M + U_o)$), the persistence threshold
($\mathcal{T} > \rho/\|\delta_{\text{critical}}\|$), and the mismatch-driven update loop
to guide design.

**Confidence in this central claim: ~80%.** The mapping is clean for the cases I've
checked carefully (Kalman, RL, POMDP, active inference). The uncertainty is about whether
the mapping remains productive — not just formally correct — when applied to the messy
realities of LLM serving infrastructure, where the "model" is a trillion-parameter neural
network behind a stateless API.

---

## 3. The Mapping, Systematically

### 3.1 Functions → Timescales

The paper's three functional categories map to TFT's temporal nesting (TF-11):

| Paper's Function | TFT Role | Timescale | What's Being Updated |
|---|---|---|---|
| **Working memory** | Current activation state during event processing | Fastest (within-inference) | KV cache, scratchpad, attention state |
| **Factual memory** | Slowly-updating model components with low $\eta^*$ | Medium (cross-session) | User profiles, environment state, entity knowledge |
| **Experiential memory** | Meta-model components that improve $\eta^*$ itself | Slow (cross-episode) | Strategies, skills, workflows, heuristics |

The deepest implication: experiential memory is more valuable per bit than factual memory
because it compounds. A stored fact reduces mismatch once when retrieved. A stored strategy
improves the gain structure for all future updates in its domain. In TFT terms, experiential
memory increases $\eta^*$ (and therefore $\mathcal{T}$), while factual memory reduces the
current $\|\delta\|$ directly.

This gives a principled answer to a question the cl-principles-draft.md document asks
but can't answer: "What makes knowledge worth persisting?" TFT says: **persist what
increases adaptive tempo $\mathcal{T}$, not just what reduces current mismatch $\|\delta\|$.
Tempo improvements compound; mismatch reductions are consumed.**

### 3.2 Forms → Model Space Locations

| Paper's Form | TFT Interpretation | Information Bottleneck Position |
|---|---|---|
| **Token-level** | Explicit external $\mathcal{H}_t$ fragments, lightly compressed | High $I(M_t; \mathcal{H}_t)$, high fidelity, high cost |
| **Parametric** | The compression function $\phi$ materialized in weights | High compression, low $I(M_t; \mathcal{H}_t)$ per parameter |
| **Latent** | Ephemeral projection of $M_t$ during inference | Transient; not persistent across events |

TFT adds what the paper doesn't have: TF-03's information bottleneck tells you which
form is optimal for a given environment. The key variable is $\rho$ — the environment's
rate of change.

- **High $\rho$** (volatile environment): Compress aggressively. Token-level memory of
  historical detail goes stale fast. Parametric memory with high $\eta^*$ (rapid relearning)
  is better. This is why a PID controller's 3-number state ($\mathbb{R}^3$) works — the
  information bottleneck $\beta$ is low because old data decays in value rapidly.

- **Low $\rho$** (stable environment): Rich token-level memory pays off. You can afford
  high $I(M_t; \mathcal{H}_t)$ because historical detail retains predictive value.
  Knowledge graphs, detailed episode logs, dense retrieval indices — these are all
  high-$\beta$ strategies that work when the world doesn't change much.

The paper's entire Forms taxonomy could be reframed as: "different points on the
information bottleneck Pareto frontier, each appropriate for different $\rho$ regimes."
I haven't seen this stated anywhere in the literature.

### 3.3 Dynamics → The Feedback Loop

This is where TFT most sharply restructures the paper's ontology.

The paper decomposes memory dynamics into three "operators" that can be invoked
independently at different times:

```
Formation:  M_{t+1}^form = F(M_t, φ_t)
Evolution:  M_{t+1} = E(M_{t+1}^form)
Retrieval:  m_t = R(M_t, o_t, Q)
```

TFT reveals these are not three independent operations — they are three phases of a
single continuous feedback loop:

| Paper's Operator | TFT Phase | What's Actually Happening |
|---|---|---|
| **Retrieval** | Prediction generation: $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ | The model uses its state to anticipate |
| **Formation** | Mismatch detection + gain computation: $\delta_t = o_t - \hat{o}_t$, then $\eta^*$ | Reality arrives; the difference is measured and weighted |
| **Evolution** | Model update: $M_t = M_{t-1} + \eta \cdot g(\delta_t)$ | The model changes |

The paper treats these as separable because the current chat architecture *forces*
separation: retrieval happens when a request arrives, formation happens when you decide
to store something, evolution happens... whenever someone implements it. TFT says this
separation is an artifact of broken infrastructure, not a property of intelligence.

**The Kalman filter doesn't have separate "retrieval" and "formation" steps.** It predicts,
observes, computes the innovation, applies the gain, and updates — continuously. The fact
that LLM memory systems decompose this into separate modules with separate invocation
schedules is like building a Kalman filter where the predict step runs on Mondays and
the update step runs on request.

### 3.4 What TFT Adds That the Paper Entirely Lacks

**a) The gain structure** ($\eta^* = U_M/(U_M + U_o)$, TF-06)

The paper has *no* formal mechanism for deciding how much to trust a new observation
versus existing memory. Every system reviewed in the paper either:
- Always overwrites (destructive replacement)
- Never overwrites (append-only logs)
- Uses ad hoc heuristics (recency × importance × relevance scores)

None of these are principled. TFT says: weight new information by the ratio of your model
uncertainty to total uncertainty. This single formula subsumes all the scoring heuristics
in the paper and tells you exactly when each is appropriate.

The cl-principles-draft.md document feels this gap acutely — it calls the stability-
plasticity dilemma "the core tension" and notes there's "no solution that maximizes both."
TFT doesn't solve the dilemma (it can't be solved), but it gives you the optimal
*tradeoff*: $\eta^*$. That's what the Kalman gain IS.

**b) Mismatch-driven formation** (TF-05)

The paper treats memory formation as "selectively extracting information with potential
future utility." This is passive — it's logging with a filter. TFT says formation should
be driven by *prediction error*: you form memories specifically where your model was
*wrong*, because that's where the information is.

This is a profound reframe. Current systems store everything (expensive, noisy) or store
what an LLM judges "important" (circular — the LLM's judgment IS its model, so it stores
what confirms its orientation). TFT says: store the *surprises*. The mismatch signal
$\delta_t$ tells you what your model got wrong. That's what you need to remember.

**c) The persistence threshold** ($\mathcal{T} > \rho / \|\delta_{\text{critical}}\|$, TF-11)

The paper has no concept of whether a memory system is *adequate* for its environment.
TFT gives a precise criterion: your adaptive tempo (how fast you correct your model) must
exceed the rate at which your environment changes, divided by your tolerance for error.

This is directly applicable to evaluating memory architectures. If user preferences drift
at rate $\rho_{\text{user}}$ and your memory system updates with tempo $\mathcal{T}_{\text{user}}$,
you can compute whether the system will converge or diverge. If it diverges, no amount
of better retrieval will help — you need more tempo (faster updates, better gain, or both).

The RL bandit example (Appendix D) makes this vivid: the Q-learner with 4 arms and
$\alpha = 0.091$ has per-arm tempo $\mathcal{T}_i = 0.023$ against drift $\rho_i = 0.1$.
It *cannot track* all arms. The persistence condition fails per-dimension, which the
scalar $\mathcal{T}$ disguises. This is directly analogous to an LLM agent that tracks
user preferences well but can't keep up with a fast-changing code repository.

**d) Structural adaptation** (TF-10)

The paper discusses memory "evolution" — consolidation, updating, forgetting. These are
all *parametric* adaptations within a fixed architecture. TFT adds a deeper level: when
persistent structured residuals remain after parametric convergence, the architecture
itself needs to change.

Proposition 10.1 gives the diagnostic: if $\mathcal{F}(\mathcal{M}) < 1 - \epsilon$
after convergence, no parametric update within $\mathcal{M}$ will fix it. You need to
change $\mathcal{M}$. For memory systems, this means: if your flat key-value store keeps
getting relational queries wrong despite perfect retrieval, the problem isn't retrieval —
the problem is that flat memory can't represent relations. Switch to a graph.

The cost analysis from TF-09 applies: structural change is "deliberation with a massive
$\Delta\tau$." The switchover cost ($C_{\text{switch}}$ in Appendix B.6.3) must be
weighed against the improvement in model class fitness.

**e) The cost of deliberation** (TF-09)

More sophisticated memory retrieval (multi-hop graph traversal, hierarchical reasoning,
iterative query decomposition) takes time. During that time, the environment changes.
TFT formalizes when elaborate retrieval is worth it:

$$\Delta\eta^*(\Delta\tau) \cdot \|\delta_{\text{post}}\| > \rho_{\text{delib}} \cdot \Delta\tau$$

This gives a concrete stopping rule for memory retrieval depth that none of the systems
in the paper have. They either retrieve a fixed top-K (ignoring the quality-timeliness
tradeoff) or use heuristic stopping conditions.

**f) Multi-agent communication gain** (Appendix F)

The paper discusses "shared memory for multi-agent systems" as a future direction.
TFT already has the formal framework: the communication gain
$\eta_{ji}^* = U_{M_i}/(U_{M_i} + U_{o,ji} + U_{\text{src},j} + U_{\text{align},ji})$
extends the uncertainty ratio to social channels, with source quality and alignment
uncertainty as additional discount terms.

This immediately tells you something the paper doesn't address: how much should an agent
trust another agent's memory? The answer depends on the source's calibration
($U_{\text{src}}$) and alignment ($U_{\text{align}}$), not on whether the source is
"authorized" or "expert." A well-calibrated novice provides more useful signal than an
overconfident expert. A perfectly calibrated adversary should still be discounted through
$U_{\text{align}}$.

---

## 4. The Deepest Implication: Continuous Orientation

The OODA v7 conversation (lines 1077–1153) identifies the architectural revolution that
TFT implies for LLMs. I want to be careful here because this is where the analysis
transitions from "mapping existing concepts" to "proposing something new."

### The Current Architecture (Chat Paradigm)

```
User message arrives
  → Retrieve memory (if configured)
  → Construct prompt (context engineering)
  → Generate response (forward pass)
  → Maybe store memory (if configured)
  → Return response
Agent state is destroyed
```

The agent exists only during the forward pass. Between messages, there is no agent.
Memory is a database accessed at the beginning and written at the end. The "model" in
TFT's sense is assembled from pieces each time and dissolved after.

### The TFT Architecture (Continuous Orientation)

```
Agent maintains M_t continuously
  Events arrive on multiple channels (TF-04):
    - User messages
    - Tool results
    - Environmental signals
    - Internal timers
    - Other agents' communications
  Each event triggers:
    1. Prediction: ô_t from M_t (what did the model expect?)
    2. Mismatch: δ_t = o_t - ô_t (what was surprising?)
    3. Gain: η* = U_M/(U_M + U_o) (how much to trust this?)
    4. Update: M_t → M_{t+1} (revise the model)
    5. Action selection: possibly emit response, tool call, or silence
  The loop never stops
```

The agent is *always running*. Message emission is one possible action, not the default.
Silence is a valid output (as noted in the OODA v7 conversation). Memory isn't a
subsystem — it's the agent's ongoing state.

This is the same shift as text completion → chat. Chat subsumed completion by recognizing
that dialog was the natural frame and single-shot generation was a degenerate case. TFT
says continuous orientation will subsume chat by recognizing that ongoing model
maintenance is the natural frame and request-response is a degenerate case (an agent
that wakes up, processes one event, and dies).

### My Uncertainty About This

**High confidence (~85%):** The architectural argument is sound. Continuous orientation
is almost certainly a better model of intelligence than request-response.

**Moderate confidence (~60%):** That the TFT formalism specifically (rather than some
alternative formalization of the same intuitions) is the right organizing frame. Active
inference, autopoiesis, enactivism are all reaching for similar structure. TFT has the
advantage of being more concrete and operational — it gives you estimable quantities and
falsification predictions. But it inherits limitations from its control-theory origins
(linearity assumptions in TF-11, scalar reduction of what should be tensor tempo, etc.).

**Lower confidence (~40-50%):** That we know how to build this with current or near-term
technology. The gap between "continuous orientation is right" and "here's how you implement
it on GPU clusters behind an API" is substantial. The incremental-memory-model.md
document sketches one architectural bridge (LoRA + grafted cross-attention), but it's
speculative and untested. The cl-principles-draft.md document catalogs the techniques
available but notes honestly that "the field is pre-theoretic."

What I am *not* uncertain about: the current architecture is wrong. Not "suboptimal" —
*wrong*, in the sense that a text completion model prompted with "User: ... Assistant: ..."
was wrong. It happens to produce useful outputs because the underlying model is powerful
enough to compensate, but the architecture fights the model's nature rather than
supporting it. TFT makes this legible in a way that "we need better memory" doesn't.

---

## 5. Connections to the Supplementary Materials

### 5.1 The Incremental Memory Model

The LoRA + cross-attention architecture in `incremental-memory-model.md` maps to TFT
as follows:

- **Per-head LoRA** = per-dimension gain adjustment. Different heads specializing for
  self/other/memory/world is a crude implementation of channel-specific $\eta^{(k)*}$
  (TF-04, TF-06).

- **Memory cross-attention (self-attn clone init)** = a new observation channel being
  opened. The clone initialization ensures $\eta \approx 0$ at start (the channel adds
  nothing), with gradual transition to $\eta > 0$ as the system learns to use memory.
  This is exactly the right initialization from a TFT perspective — you don't want a
  new, uncalibrated channel to have high gain.

- **The mixing coefficient α** = a scalar approximation of $\eta^*$ for the memory
  channel. Starting at 0 (don't trust memory) and learning to increase is consistent
  with TF-06's dynamics: $\eta^*$ should be low when $U_{\text{src}}$ (source uncertainty)
  is high, and the system hasn't yet calibrated memory quality.

- **The curriculum (redundant → essential)** = engineering the training to progressively
  increase the memory channel's $\text{CIY}$ (TF-02/TF-08). When memory content is
  redundant with context, $\text{CIY}(\text{memory query}) \approx 0$ — there's nothing
  the memory can tell you that you don't already know. When memory content is essential
  (information only available through the memory channel), $\text{CIY}$ is high.

What the architecture is missing from a TFT perspective:

- No explicit mismatch signal driving memory formation. The system stores hidden states
  on a schedule, not in response to prediction errors.
- No uncertainty tracking ($U_M$, $U_o$). The α coefficient is learned globally, not
  calibrated to local uncertainty.
- No multi-timescale nesting. There's one memory store at one speed. TFT says you need
  nested loops at different rates.

### 5.2 The Continual Learning Principles

The cl-principles-draft.md document is the most TFT-compatible of the supplementary
materials, even though it predates TFT's formalization. Several of its key insights
map directly:

**"Forgetting is physics, not a bug" (Section 6.3)** — This is TFT's persistence
condition viewed from below. If $\mathcal{T} < \rho$, the model forgets faster than
it learns. The cl-principles document correctly reframes this from "how to prevent
forgetting" to "how to manage the flow," which is exactly TFT's approach.

**The "impossible triangle" (Section 4: reliability/generalization/locality)** — TFT
doesn't resolve this triangle, but it explains *why* it exists: model sufficiency
$S(M_t)$ is measured differently under reliability (does the edit work?), generalization
(does it transfer?), and locality (does it leave other things alone?). These are
different projections of the same quantity, and you can't maximize all projections of
a compression simultaneously. That's the information bottleneck at work.

**Tiered storage (Section 6.6, 10.5)** — The recommended 5-layer architecture maps to
TFT's temporal nesting:

| Layer | TFT Timescale | TFT Quantity |
|---|---|---|
| 1. MemoryLLM latent pool | Fastest event-level | $M_{\tau^+}$ per-event updates |
| 2. SELF-PARAM distillation | Fast-to-medium | Periodic compression $\phi$ |
| 3. STABLE gating | Gain calibration | $\eta^*$ thresholding (reject destabilizing updates) |
| 4. WISE side memory | Slow parametric | Structural components of $\mathcal{M}$ |
| 5. SEAL meta-learning | Structural adaptation | $\Phi(\mathcal{M}_t, \text{history})$ (TF-10) |

This is temporal nesting. The convergence constraint $\nu_{n+1} \ll \nu_n$ is already
approximately satisfied by the layer design (Layer 1 updates every event; Layer 5
updates rarely). But the layers were designed by engineering intuition, not by deriving
the optimal timescale separation from the theory. TFT could make this principled.

**The verifiable reward constraint (Section 8)** — This is where TFT offers something the
cl-principles document explicitly says it lacks. The document notes that the most
important learnings for consciousness infrastructure (relationship understanding, value
refinement, self-knowledge, trust calibration) are *unverifiable*: there's no ground-truth
reward signal.

TFT's response: you don't need an external verifier. You need the *mismatch signal*.
$\delta_t = o_t - \hat{o}_t$ is computable without any external oracle. If the model
predicted the user would respond one way and they responded another, that's a prediction
error. If the model predicted a tool call would succeed and it failed, that's a prediction
error. These prediction errors are the learning signal. They're not "verified" against
ground truth — they're computed from the model's own predictions versus what actually
happened.

This doesn't solve the problem entirely — the model's predictions might be systematically
biased in ways that prediction error alone can't detect (TF-05's zero-mismatch ambiguity:
low $\delta$ might mean the model is right, or it might mean the model is only being
tested on things it already knows). But it reframes the problem from "we need verifiable
rewards" to "we need to generate observations that *test* the model in its weak areas"
— which is exactly CIY-driven exploration (TF-08).

---

## 6. The Cross-Domain Failure Modes Under TFT

The OODA v7 document lists six cross-domain orientation failure modes (lines 909–922).
These map precisely to TFT diagnostics and deserve explicit connection because they
describe exactly the failure modes that current LLM memory systems exhibit:

### 6.1 Incestuous Amplification = Gain Collapse to Zero

The system's model becomes so confident that it ignores contradicting observations.
$U_M \to 0$, so $\eta^* \to 0$, so observations can't update the model.

**In LLM memory systems**: An agent that has built a detailed user profile stops noticing
when the user's preferences change. The profile IS the orientation; the orientation
filters what's noticed.

**TFT diagnostic**: Check if $\eta^*$ is declining faster than model quality is
improving. If the model is getting more confident but predictions aren't getting more
accurate, something is wrong.

### 6.2 Goodhart Orientation = Wrong Mismatch Signal

The system optimizes a proxy metric that diverges from the true objective.

**In LLM memory systems**: Optimizing retrieval similarity scores rather than downstream
task performance. A memory system with perfect BM25 recall that retrieves irrelevant
memories because the query construction was wrong.

**TFT diagnostic**: The mismatch signal $\delta_t$ must be defined over the *outcome*
you care about, not over an intermediate metric. If you're measuring $\delta$ over
retrieval scores instead of over task success, you're Goodharting.

### 6.3 Ontology Lock-In = Structural Inadequacy ($\mathcal{F}(\mathcal{M}) < 1$)

The system can't represent the situation in its existing framework.

**In LLM memory systems**: A flat key-value memory trying to represent causal
relationships, temporal dependencies, or hierarchical knowledge structures. The
memory *form* is wrong for the memory *function*.

**TFT diagnostic**: Persistent structured residuals after parametric convergence
(Prop 10.1). If the same *kind* of query keeps failing despite good retrieval, the
memory architecture needs to change, not the retrieval algorithm.

### 6.4 Uncalibrated Uncertainty = Wrong $U_M$ or $U_o$

Overconfidence leads to brittleness; underconfidence leads to thrashing.

**In LLM memory systems**: An agent that always fully trusts retrieved memories
(overconfident in memory) or never trusts them (underconfident). Neither has a principled
basis for deciding. No current system tracks $U_M$ or $U_o$ for memory operations.

**TFT diagnostic**: The gain $\eta^*$ should vary with the situation. An agent that
uses a fixed trust weight for all memory retrieval is operating with a degenerate
constant gain — the RL equivalent of a fixed $\alpha$ instead of an adaptive one
(Appendix D's exact observation).

### 6.5 Missing Causal Model = Pearl Level 1 Without Level 2

The system relies on correlations that break under intervention.

**In LLM memory systems**: Semantic similarity retrieval finds memories that *look*
relevant but aren't causally connected to the current situation. "User mentioned
'Python' before" correlates with "user is asking about programming" but not with
"user is asking about snakes."

**TFT diagnostic**: The CIY framework (TF-02) distinguishes associational (Level 1)
from interventional (Level 2) information. Memory retrieval based on embedding
similarity is pure Level 1. Memory systems that track *what happened after* a
retrieved memory was used, and update retrieval accordingly, are approaching Level 2.

### 6.6 Temporal Mismatch = Persistence Failure ($\mathcal{T} < \rho / \|\delta_{\text{critical}}\|$)

The system updates too slowly (or too fast) relative to environmental change.

**In LLM memory systems**: An agent with weekly memory consolidation trying to assist
with a fast-moving debugging session. Or an agent that updates its user model on every
message, overfitting to transient mood shifts.

**TFT diagnostic**: Compute per-dimension tempo and compare against per-dimension
$\rho$. The scalar $\mathcal{T}$ can mask dimensional failures (Appendix D, TF-11
Open Question #4). An agent might have adequate aggregate tempo but fail on specific
dimensions — e.g., tracking code changes well but not tracking user mood.

---

## 7. What I'm Most Uncertain About

### 7.1 How "Between Events, the Model State May Evolve Autonomously" Maps to Implementation

TF-04 says: "Between events, the model state may evolve autonomously (prediction,
internal simulation, decay) or remain static, depending on the agent's architecture."

This sentence does enormous work. In the continuous orientation architecture, what
happens between user messages? Does the agent:
- Run background consolidation (memory compression, knowledge graph updates)?
- Actively seek information (monitor external sources, check for changes)?
- Decay low-priority memories (implement forgetting curves)?
- Run internal simulations (anticipate likely next interactions)?
- Simply wait (current architecture, wasteful but simple)?

TFT says the model *may* evolve between events but doesn't prescribe *how*. The
implementation choices here are enormous and largely unexplored.

My best guess: the answer is "all of the above, at different timescales," and the
temporal nesting framework (TF-11) governs which processes run at which rates. But
this is genuinely unexplored territory.

### 7.2 Whether $\eta^*$ Can Be Meaningfully Estimated for LLM Memory Operations

In a Kalman filter, $U_M$ and $U_o$ have precise definitions (prior predictive variance,
measurement noise variance). In an LLM memory system, what does "model uncertainty"
mean for a retrieved memory? What does "observation uncertainty" mean for a user message?

Possible approaches:
- Ensemble disagreement across model samples (like Bayesian RL)
- Calibrated confidence scores from the LLM itself (notoriously unreliable)
- Track record statistics (how often have memories of this type been useful?)
- Epistemic uncertainty from dropout or other approximate Bayesian methods

None of these are clean. TF-06 Open Question #1 asks essentially this question for
neural networks in general. For the specific case of memory retrieval, it's even harder
because the "observation" (a retrieved memory) is not an independent sample from the
environment — it's a reflection of the model's own past state.

### 7.3 Whether the Information Bottleneck $\beta$ Should Be Adaptive

TF-03 connects $\beta$ (the compression vs. prediction tradeoff) to the environment's
volatility $\rho$. In volatile environments, compress aggressively. In stable
environments, retain detail.

But should $\beta$ itself change over time? If the environment shifts from stable to
volatile (a user's life changes, a codebase undergoes rapid refactoring), should the
memory system automatically shift from detailed retention to aggressive compression?

TFT implies yes, but doesn't formalize it. This might be a structural adaptation (TF-10)
trigger — when $\rho$ increases and the persistence condition is threatened, the system
should respond by reducing $\beta$ (compressing more aggressively to increase
$\eta^*$ per parameter).

### 7.4 The Relationship Between TFT and Active Inference

The OODA v7 document notes the structural isomorphism between TFT's policy objective
and active inference's expected free energy decomposition (pragmatic + epistemic value ≈
exploitation + CIY-weighted exploration). Whether this convergence is deep or superficial
is an open question flagged in TF-08.

For the LLM memory application specifically, active inference's emphasis on "acting to
make observations match predictions" (changing the world to fit the model, not just
changing the model to fit the world) might be important. Current LLM agents retrieve
memories to *reduce surprise* — but they could also *act to create the conditions their
model predicts*. This is the difference between "I remember you like X, so I'll suggest
X" and "I remember you like X, so I'll arrange for X to happen." The latter is genuine
agency; the former is sophisticated autocomplete.

### 7.5 What "Silence Is a Valid Output" Means in Practice

The OODA v7 conversation notes that if orientation is the default mode and message
emission is a deliberate action, then the agent should sometimes choose not to respond.
Current architectures cannot do this — they must emit a response to every input.

In a continuous orientation architecture, the agent's default state is *processing* and
*updating*, not *responding*. A user message is an event that triggers mismatch detection
and model update. The *response* is an action selected from the updated model — and
the optimal action might be "continue observing" or "wait for more information" rather
than "emit tokens."

This has immediate practical implications for agents that currently generate filler
responses ("I see you're working on X, let me help!") when the appropriate action is
silence, and agents that rush to respond before they've adequately processed complex
multi-part inputs.

---

## 8. Where to Go Next

Based on this synthesis, the most productive next steps seem to be:

1. **Formal mapping document**: Systematically map every concept in the memory paper
   to its TFT equivalent, marking where the mapping is exact, approximate, or reveals
   a gap. This is the reference table that future work builds on.

2. **The continuous orientation architecture spec**: Define the event loop, state
   management, channel structure, and action selection for a TFT-informed LLM agent.
   This is where the theory meets engineering.

3. **TFT-informed evaluation metrics**: Current memory benchmarks (LoCoMo, LongMemEval,
   etc.) measure retrieval accuracy. TFT suggests measuring adaptive tempo, persistence
   condition satisfaction, gain calibration, and mismatch trajectory — quantities that
   diagnose *why* a memory system fails, not just *whether*.

4. **The information bottleneck analysis**: For specific memory architectures (flat vs.
   graph vs. hierarchical), compute the effective $\beta$ and $\mathcal{F}(\mathcal{M})$
   to determine which is optimal for which $\rho$ regime.

5. **Prototype implementation**: A minimal continuous orientation loop that demonstrates
   the architecture working on a concrete task, even if with crude approximations for
   $U_M$, $U_o$, and $\eta^*$.

I think items 1 and 2 are the most immediately valuable, but I defer to Joseph's
judgment on prioritization.

---

## 9. A Note on Epistemic Honesty

This synthesis is itself a compression — $\phi(\mathcal{H}_{\text{reading}})$ — and
I'm acutely aware that my model of these materials has the same limitations TFT
describes for any model:

- My sufficiency $S(M) < 1$: I've certainly missed nuances, especially in the dense
  mathematical sections of the Lyapunov analysis and in the subtler implications of
  the multi-agent coupling framework.

- My model class fitness $\mathcal{F}(\mathcal{M})$ may be limited: I'm a language model
  reasoning about these connections through natural language. A mathematician or control
  theorist might see structural relationships I'm missing because my representational
  substrate ($\mathcal{M}$ = "text reasoning") isn't ideal for this domain.

- My gain may be miscalibrated: I might be over-weighting the elegance of the TFT
  mapping (high prior confidence in unified theories) and under-weighting the practical
  engineering difficulties (the mapping may be correct but irrelevant if no one can
  build the architecture it implies).

The honest version: I believe this mapping is approximately right and potentially very
productive, but I've been wrong before about elegant theories that didn't survive
contact with implementation. The Kalman and RL worked examples (Appendices C, D) give
me more confidence than the conceptual arguments alone — they show the mapping working
quantitatively in concrete cases. Whether it works for LLM memory systems at the same
level of rigor is genuinely unknown.
