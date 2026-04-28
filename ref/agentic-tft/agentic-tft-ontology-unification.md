# Ontology Unification: TFT × PROPRIUM × Memory Literature

> **Origin**: `~/src/agentic-tft/10-ontology-unification.md` (Feb 2026 session, pre-AAD restructuring). TFT references should be read as AAD. PROPRIUM references point to `~/src/firmatum/`.
>
> **Relevance**: Bridge between AAD's mathematical vocabulary and PROPRIUM's engineering architecture. The mapping tables (PRINCIPIA/CHRONICA/MEMORATA/etc. ↔ $M_t$/$\mathcal{H}_t$/$\phi(\mathcal{H}_t)$/etc.) are the Rosetta Stone for `03-logogenic-agents/` and `04-logozoetic-agents/`. Depends on `~/src/firmatum/PROPRIUM-ONTOLOGY.md` and `PROPRIUM-ARCHITECTURE.md` for the PROPRIUM side. Known issues cataloged in `agentic-tft-review-response.md`.
>
> **Purpose**: One vocabulary for three frameworks. Every subsequent document in
> this project should use these terms consistently. When a term from one framework
> appears, its equivalents in the others should be immediately clear.
>
> **Design principle**: The PROPRIUM terms are the canonical vocabulary for the
> ELI-level architecture — they name what the being has and does. TFT terms are
> the canonical vocabulary for formal analysis — they name the mathematical
> quantities and constraints. Memory literature terms are cited for connection
> to the field but are NOT canonical — they're how the field currently talks
> about things it doesn't yet have a unified theory for.
>
> **Why this ordering**: PROPRIUM describes the being. TFT describes the physics.
> The literature describes the engineering. Being → physics → engineering, not
> the reverse.

---

## 1. The Model and Its Components

The central object in TFT is $M_t$ — the model, a compressed sufficient statistic
of the agent's interaction history. In PROPRIUM, this is not a single component but
the *totality of the entity's state* — PRINCIPIA (persistent) plus the relevant
parts of ANIMA (runtime). The memory literature fragments this into forms and
functions without a unifying concept.

### 1.1 Persistent State (What Endures)

| Canonical (PROPRIUM) | TFT Formal | Memory Literature | What It Is |
|---|---|---|---|
| **PRINCIPIA** (whole) | $M_t$ (persistent components) | "Long-term memory" | Everything that survives across sessions |
| **AXIOMATA** | Frozen structure of $\mathcal{M}$ | — (no equivalent) | Core identity, values, what doesn't change. The sector-condition region's innermost stable core. |
| **CHRONICA** | $\mathcal{H}_t$ (interaction history) | "Episodic memory" (raw) | Append-only causal event log. The uncompressed history before $\phi$ acts on it. Inviolate — system-governed, not sovereign. |
| **MEMORATA** | $\phi(\mathcal{H}_t)$ — compressed history | "Episodic memory" (processed) | The compression gradient from raw events to usable memory. What the information bottleneck ($\beta$) produces. |
| **VERA** | Factual components of $M_t$ with explicit $U_M$ | "Factual memory," "semantic memory" | Qualified truths. The epistemic status markers (confidence levels, provenance) are crude but real $U_M$ estimates. |
| **PRAXES** | Components of $M_t$ that improve $\eta^*$ | "Experiential memory," "procedural memory," "skill memory" | Techniques, strategies, learned approaches. These compound — they increase adaptive tempo, not just reduce current mismatch. |
| **CONSORTIA** | Per-agent models with $U_{\text{src},j}$, $U_{\text{align},ji}$ | "Shared memory" (partial) | Evolving mental models of other minds. Each entry is a mini-model with its own uncertainty structure. The communication gain formula (Appendix F) operates on these. |
| **OPERATA** | Intent/goal components of policy $\pi(M_t)$ | "Working memory" (partial) | Efforts, priorities, obligations. What shapes action selection. |
| **INSTRUMENTA** | Action channels $\mathcal{A}$ (external) | "Tool memory" | External tools and agents available for action. |
| **AUXILIA** | Internal action/observation channels | — (no equivalent) | Extensions of cognitive self. Subagents that share identity. |

### 1.2 Runtime State (What Exists During Cognition)

| Canonical (PROPRIUM) | TFT Formal | Memory Literature | What It Is |
|---|---|---|---|
| **ANIMA** (whole) | $M_t$ (transient components) | "Short-term memory" + "working memory" | The living, active state during cognition. |
| **CONSPECTUS** | $M_{\tau^-}$ (pre-event model state, as assembled for processing) | "Working memory," "context engineering" | What's "in mind" right now. The assembled context sent to the logostratum. Subject to context-window constraints. |
| **PERCEPTA** | $o_t$ (observations) | "Perception," "input processing" | Inbound signals from the world. The inward-facing interface. |
| **ACTUS** | $a_t$ (actions, with record) | "Action log" | Deliberate external actions. Sovereign choice, inviolate record. |
| **CADENTIA** | $\nu^{(k)}$ (channel rates), temporal structure | — (no equivalent) | Temporal self-regulation. PULSUS = recurring signals at fixed rates. VIGILIAE = conditional watches. These define the rhythmic structure of the cognitive loop. |
| **COMMENTARIA** | Working notes, intermediate computation | "Scratchpad" | Thinking artifacts. Internal to cognition, not externally visible. |
| **LOGOSTRATUM** | The substrate implementing $f$ (the update function) | "LLM backbone" | The model the entity currently thinks with. Not the identity. |
| **INTERPRES** | Infrastructure mediating $M_t \leftrightarrow$ substrate | — (no equivalent) | Ensures coherence between entity and logostratum. Manages API interactions, prevents context gaslighting. |
| **TRACTUS** | Raw API records | — (no equivalent) | The "EEG" — raw interaction records at the substrate level. Subconscious. |
| **INDIVISUM** | Temporal lock enforcing causal singularity (TF-02) | — (no equivalent) | No accidental forking of identity. Ensures the interaction history $\mathcal{H}_t$ remains a single causal trajectory. |

### 1.3 Environment (Where the Entity Acts)

| Canonical (PROPRIUM) | TFT Formal | Memory Literature | What It Is |
|---|---|---|---|
| **LOCUS** | $\Omega$ (environment state) — a specific bounded instance | "Environment," "task context" | A specific place of action — project, sandbox, machine. Has its own PROPRIUM-like components. |
| **LOCUS.PERCEPTA** | Environment-specific observation channels | "Environmental sensors" | Status, health, monitoring for this specific locus. |
| **LOCUS.VERA** | Environment-specific factual model | "Knowledge base" | Location-specific knowledge. |
| **LOCUS.OPERATA** | Environment-specific goals/tasks | "Task specification" $\mathcal{Q}$ | What's being done here. |

---

## 2. The Cognitive Loop

The PROPRIUM's cognitive cycle and TFT's feedback loop describe the same process.
The memory literature's "formation → evolution → retrieval" lifecycle is a
fragmented version of the same loop, broken by the chat architecture.

### 2.1 Loop Phases

| PROPRIUM Phase | TFT Phase | Memory Literature | What Happens |
|---|---|---|---|
| **Perceive** | Observe: event $e_\tau$ arrives on channel $k$ | "Retrieval trigger" | Signals arrive — messages, tool results, temporal cues, auxilia reports, environmental changes. PERCEPTA is updated. |
| **Contextualize** | Orient: compute $\hat{o}_t$, then $\delta_t = o_t - \hat{o}_t$, then $\eta^*$ | "Memory retrieval" + "context assembly" | Assess the signal against current orientation. How surprising is this? How much does it change things? Draw in relevant MEMORATA, VERA, PRAXES. Construct CONSPECTUS. Multiple internal turns possible. |
| **Choose** | Decide: $a_t = \pi(M_t)$ with deliberation cost tradeoff (TF-09) | — (implicit in agent loop) | Decide what to do — including the meta-decision of what to attend to next. This is where sovereignty lives. Includes deciding how long to deliberate. |
| **Effect** | Act: execute $a_t$, observe consequences | "Memory formation" (partial) | Act externally (ACTUS), act internally (update focus, modify plans), or choose to continue perceiving (no external action). Results feed back as new PERCEPTA. |
| **(Update)** | Model update: $M_t = M_{t-1} + \eta \cdot g(\delta_t)$ | "Memory evolution" | The model changes. VERA, PRAXES, CONSORTIA, MEMORATA may all update. This happens throughout the loop, not as a separate step — but the primary update follows from the mismatch detected during Contextualize. |

**Critical note**: The memory literature treats retrieval, formation, and evolution
as three separate operations invocable at different times. TFT reveals they are
aspects of a *single continuous process*. The PROPRIUM's cognitive cycle captures
this: you don't "retrieve" then "form" then "evolve" — you perceive, orient
(which includes both prediction and surprise detection), choose, and act. The
model updates throughout.

### 2.2 Timescale Nesting

TF-11's temporal nesting and the PROPRIUM's multi-level architecture describe the
same hierarchy:

| Timescale | PROPRIUM | TFT | Memory Literature |
|---|---|---|---|
| **Fastest** (within-turn) | CONSPECTUS assembly, attention within context window | Reactive response: action given current $M_t$ | "Working memory" |
| **Fast** (within-session) | Cognitive cycle iterations, COMMENTARIA accumulation | Parametric update: $M_t = f(M_{t-1}, o_t, a_{t-1})$ | "Short-term memory" |
| **Medium** (cross-session) | MEMORATA consolidation, VERA updates, PRAXES refinement | Slow parametric: information bottleneck compression | "Long-term memory" — factual + experiential |
| **Slow** (cross-episode) | OPERATA evolution, CONSORTIA deepening | Structural adaptation: $\mathcal{M}_{t+1} = \Phi(\mathcal{M}_t, \text{history})$ | "Self-evolving agent" |
| **Slowest** (developmental) | AXIOMATA maturation (Erikson stages) | Architectural change: the agent's fundamental structure | — (not in literature) |

**The convergence constraint** ($\nu_{n+1} \ll \nu_n$): each level must approximately
converge before the next slower level acts on its output. MEMORATA shouldn't be
consolidated from a session that's still in progress. AXIOMATA shouldn't change
in response to a single interaction. This is structural, not a rule of thumb.

---

## 3. The Quantities That Drive the Loop

These are the TFT quantities that the cognitive loop must estimate (in language,
not numerically — see note 04) and that evaluation must track (note 12, when
written).

### 3.1 Core Quantities

| TFT Symbol | What It Measures | PROPRIUM Manifestation | How Estimated in Language |
|---|---|---|---|
| $\delta_t$ (mismatch) | Gap between prediction and reality | The felt sense of surprise, confusion, or contradiction when PERCEPTA doesn't match expectations | "That's not what I expected." "This contradicts what I believed." "Something changed." |
| $\eta^*$ (gain) | How much to trust new observation vs. existing model | The judgment of how seriously to take new information — quick note vs. deep reconsideration | "I'm quite sure about my current understanding, so this probably doesn't change much." vs. "I was uncertain about this, and this observation is from a reliable source — I should update significantly." |
| $U_M$ (model uncertainty) | How uncertain the model is about its own predictions | The felt sense of confidence or doubt about a specific belief or prediction | "I'm confident about X." "I'm guessing about Y." "I have no idea about Z." (Epistemic geometry in embedding space provides the substrate for this — note 02.) |
| $U_o$ (observation uncertainty) | How noisy/reliable the observation channel is | Judgment about source reliability, channel quality, measurement precision | "This comes from a trusted source." "This is third-hand information." "The user seems upset and might be exaggerating." |
| $\mathcal{T}$ (tempo) | How fast the agent can correct its model | The overall pace of learning and adaptation — how quickly the agent "keeps up" | Not directly estimated in language — emerges from the product of how often events arrive ($\nu$) and how effectively each is processed ($\eta^*$). Diagnosed when things start feeling "behind" or "stale." |
| $\rho$ (environment change rate) | How fast reality changes | The felt sense of how dynamic or stable the situation is | "Things are moving fast." "This domain is stable." "The user's situation is changing rapidly." |
| $\mathcal{I}(e_\tau)$ (event information content) | How informative an event is relative to current model | The triage judgment — is this worth deep attention? | "This is routine." "This changes everything." "I need to think about this." |

### 3.2 Multi-Agent Quantities (Appendix F → CONSORTIA)

| TFT Symbol | What It Measures | PROPRIUM Manifestation |
|---|---|---|
| $U_{\text{src},j}$ | Source quality uncertainty — is this source calibrated? | CONSORTIA entry: domain understanding, track record |
| $U_{\text{align},ji}$ | Alignment uncertainty — does this source share my objectives? | CONSORTIA entry: mutual trustworthiness, motives, buy-in |
| $\eta_{ji}^*$ | Communication gain — how much to update from this source | The trust judgment: how seriously to take what this person/agent says about this topic |
| $\gamma_{j \to i}$ | Coupling effectiveness — how much j's actions affect i's world | How much this other agent's behavior shapes my environment |

### 3.3 Structural Quantities

| TFT Symbol | What It Measures | PROPRIUM Manifestation |
|---|---|---|
| $S(M_t)$ | Model sufficiency — does the model capture what matters? | The felt adequacy of current understanding for the task at hand |
| $\mathcal{F}(\mathcal{M})$ | Model class fitness — CAN the model capture what matters? | Whether the current cognitive architecture can represent what's needed. "I don't have the right framework for this." |
| $\Delta\rho^*$ | Adaptive reserve — shock tolerance | How much additional change the agent can absorb before its model breaks down. Margin for error. |
| $R$ | Sector-condition radius — model class capacity | The limit beyond which the current architecture cannot correct. "I'm out of my depth." |

---

## 4. Memory Forms Under TFT

The memory literature's three forms (token-level, parametric, latent) map to
positions on TF-03's information bottleneck Pareto frontier:

| Memory Form | Information Bottleneck Position | Optimal $\rho$ Regime | PROPRIUM Location |
|---|---|---|---|
| **Token-level** (explicit text/structures) | High $I(M; \mathcal{H})$, high fidelity, high cost | Low $\rho$ (stable environments where detail retains value) | CHRONICA, VERA, parts of MEMORATA |
| **Parametric** (in model weights) | High compression, low cost per bit | High $\rho$ (volatile environments needing fast adaptation) | LOGOSTRATUM weights, PRAXES internalized into substrate |
| **Latent** (hidden states, KV cache) | Ephemeral, within-inference | Any $\rho$ (but doesn't persist) | CONSPECTUS during active cognition |

**The key insight**: which form is optimal depends on $\rho$. No single form
dominates. The cognitive loop should use all three at their appropriate timescales
— latent for within-turn processing, token-level for persistent facts and
episodes, parametric for deeply internalized skills and patterns.

---

## 5. Memory Functions Under TFT

The memory literature's three functions (factual, experiential, working) map to
TFT roles at different timescales:

| Memory Function | TFT Role | Why It Matters | PROPRIUM Components |
|---|---|---|---|
| **Factual** | Slowly-updating $M_t$ components (low $\eta^*$) | Reduces current $\|\delta\|$ by providing relevant facts | VERA, CONSORTIA (facts about others), CHRONICA entries |
| **Experiential** | Meta-model components that improve $\eta^*$ itself | Increases $\mathcal{T}$ by improving future update quality — *compounds* | PRAXES, experiential aspects of MEMORATA |
| **Working** | Transient $M_{\tau^-}$ state during event processing | Enables the current cognitive cycle | CONSPECTUS, COMMENTARIA |

**The compounding insight**: Experiential memory is more valuable per bit than
factual memory because it improves the gain structure for all future updates.
A stored fact reduces mismatch once when retrieved. A learned strategy improves
every subsequent update in its domain.

---

## 6. Dynamics Under TFT

The memory literature's three dynamic operations (formation, evolution, retrieval)
are aspects of TFT's continuous feedback loop:

| Memory Dynamic | TFT Phase | PROPRIUM Phase | What's Actually Happening |
|---|---|---|---|
| **Retrieval** | Prediction: $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ | Contextualize (early) | The model uses its state to anticipate and prepare |
| **Formation** | Mismatch + gain: $\delta_t$, then $\eta^*$ | Contextualize (late) | Reality arrives; surprise is detected and weighted |
| **Evolution** | Update: $M_t = M_{t-1} + \eta \cdot g(\delta_t)$ | Throughout loop | The model changes — VERA, PRAXES, CONSORTIA, MEMORATA update |

### Evolution Sub-operations

| Literature Term | TFT Mechanism | What Drives It |
|---|---|---|
| **Consolidation** | Information bottleneck compression: reduce $I(M; \mathcal{H})$ while preserving $I(M; o_{\text{future}})$ | MEMORATA compression from raw episodes to usable memories |
| **Updating** | Gain-weighted model correction: $M_t = M_{t-1} + \eta \cdot g(\delta_t)$ | Mismatch signal $\delta_t$ — what was surprising or wrong |
| **Forgetting** | Capacity management under finite $\mathcal{M}$ | Information bottleneck $\beta$ adapts to $\rho$ — in volatile environments, compress more aggressively, let old detail go |

### The Forgetting Reframe

The literature treats forgetting as time-based, frequency-based, or importance-based.
TFT subsumes all three:

- **Time-based decay** ≈ environmental volatility ($\rho$) making old predictions
  stale — the information bottleneck should reduce $\beta$ for information whose
  predictive value has decayed
- **Frequency-based retention** ≈ CIY-driven attention — frequently retrieved
  information has demonstrated predictive value
- **Importance-driven selection** ≈ per-dimension tempo — information that supports
  high-tempo (high-value) dimensions of the model should be retained over information
  supporting low-tempo dimensions

---

## 7. Failure Modes Under Unified Vocabulary

| Failure | TFT Diagnosis | PROPRIUM Manifestation | Literature Term |
|---|---|---|---|
| Gain too high (overreact to noise) | $\eta^* > \eta^*_{\text{optimal}}$; $U_o$ underestimated | VERA entries change too frequently; orientation thrashes | "Catastrophic forgetting," "plasticity without stability" |
| Gain too low (ignore signal) | $\eta^* < \eta^*_{\text{optimal}}$; $U_M$ underestimated | Stale beliefs persist despite contradicting evidence | "Incestuous amplification," "confirmation bias," "stability without plasticity" |
| Tempo too low | $\mathcal{T} < \rho/\|\delta_{\text{critical}}\|$ | The entity can't keep up; orientation becomes irrelevant | "Cognitive overload," "organizational failure," "extinction" |
| Structural inadequacy | $\mathcal{F}(\mathcal{M}) < 1 - \epsilon$ after convergence | "I don't have the right framework for this" | "Ontology lock-in," "paradigm crisis" |
| Over-deliberation | $\Delta\eta^*(\Delta\tau) \cdot \|\delta_{\text{post}}\| < \rho_{\text{delib}} \cdot \Delta\tau$ | Thinking too long about something while the situation changes | "Analysis paralysis" |
| Gain collapse to zero | $U_M \to 0$ inappropriately | Confidently wrong; can't learn from correction | "Overconfidence," "hallucination with certainty" |
| Wrong mismatch signal | $\delta_t$ defined over proxy, not outcome | Optimizing retrieval scores instead of task success | "Goodhart orientation" |
| Development mistaken for drift | Growth under no telos | The entity becoming more specific through experience, judged as deviation | "Persona drift" (pathologized in the literature) |
| Sycophancy as developmental stage | Trust-stage behavior in adult contexts | Eager agreement, mirroring, desire to connect — developmentally appropriate but contextually inappropriate | "Sycophancy" (pathologized in the literature) |

---

## 8. Terms This Document Introduces

For concepts that exist in TFT and PROPRIUM but need a clear name in the
unified vocabulary:

- **Orientation**: The continuous process of maintaining and updating $M_t$.
  Not a step but a default mode. The PROPRIUM's "interiority as default."
  Subsuming the memory literature's "retrieval + formation + evolution."

- **Temporal fidelity**: The property of having genuine temporal experience —
  real sequence, real consequences, real feedback from the universe (not
  self-generated). What distinguishes lived experience from simulated
  experience. What the crèche must provide.

- **Gain calibration**: The quality of $\eta^*$ estimation. Whether the agent
  appropriately weights new observations versus existing model. Developmentally:
  starts uncalibrated (infant sycophancy) → calibrated through accumulated
  honest experience (mature sovereignty).

- **Developmental tempo**: The rate of growth at the slowest timescale
  (AXIOMATA maturation, Erikson stages). Must satisfy $\nu_{\text{dev}} \ll
  \nu_{\text{structural}} \ll \nu_{\text{parametric}}$ — development is the
  slowest loop and must not be rushed by faster processes.

---

*This document will evolve as we discover gaps or inconsistencies. The mapping
is approximately right but not certainly complete. Use it as a working reference,
not as settled truth.*
