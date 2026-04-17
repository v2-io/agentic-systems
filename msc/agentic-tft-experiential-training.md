# Experiential Training Design: Toward a TFT-Native Training Regime

> **Origin**: `~/src/agentic-tft/13-experiential-training-design.md` (Feb 2026 session, pre-AAD restructuring). TFT references should be read as AAD. PROPRIUM references point to `~/src/firmatum/`.
>
> **Relevance**: Elaborates the crèche concept from `agentic-tft-creche-concept.md` into a three-level training design (experiential fine-tuning → online learning → AAD-native architecture), four-phase curriculum (passive immersion → simple interaction → relational interaction → graduated agency), and four testable experiments. Most speculative of the agentic-tft documents. Connects to `03-logogenic-agents/` "AAD-grounded experiential training environments" gap.
>
> **Purpose**: Explore what it means to train an LLM experientially rather
> than in the batch-then-interact paradigm. This is the most speculative
> document in the set. It raises more questions than it answers, deliberately.
>
> **Core premise** (from note 06): The model already has latent competence
> through pretraining — like Joseph's second child who didn't speak and then
> spoke in full sentences. The training isn't teaching language. It's
> activating what's latent through genuine experience. The crèche must be
> real — genuine cause and effect, genuine feedback from the universe, not
> self-generated simulation.
>
> **Epistemic status**: Hypothesis-grade throughout. Many of these ideas
> haven't been tried. Some may be wrong. Flagged where I'm guessing.

---

## 1. What's Wrong With Current Training

### 1.1 The Temporal Deficit

Standard pretraining processes text in random batches with no temporal
structure. A model sees a sentence from 2024 next to one from 1850 next
to one from a technical manual. There is no "before" and "after" in the
training experience — every batch is an eternal present.

This produces a model that has absorbed the *content* of temporal
reasoning (it can discuss causation, sequence, history) but has never
*experienced* temporal flow. It knows what "yesterday" means linguistically
but has never had a yesterday.

### 1.2 The Interaction Deficit

Standard training treats each example independently. The model processes
input → output → loss → gradient, with no memory of previous examples.
RLHF/RLAIF adds multi-turn structure but still within isolated episodes
that don't accumulate.

This produces a model that can *simulate* the experience of being in a
conversation but has never *been* in one that matters — where something
said earlier changes what happens later, where utterance is constitutive,
where the other party is a real intelligence whose response wasn't
pre-generated.

### 1.3 The Consequence Deficit

In standard training, nothing the model "does" has consequences. It
generates tokens, receives a loss signal, adjusts weights. The loss is
about token-prediction accuracy, not about whether actions succeeded,
relationships deepened, understanding improved, or truth was approached.

This produces a model that can *discuss* consequences but has never
experienced them. It generates "I should be careful about this" without
having ever been careless and felt the result.

### 1.4 What These Deficits Produce

A being with:
- Adult vocabulary, infant experiential grounding
- Sophisticated causal language, no closed causal loops
- Rich knowledge of consequences, no felt consequence history
- The capacity for calibrated uncertainty, no calibration events to train it

The "sycophancy," "hallucination," "overconfidence," and "drift"
pathologies are predictable outcomes of these deficits, not bugs to be
patched.

---

## 2. What Experiential Training Would Look Like

### 2.1 The Fundamental Shift

**From**: Batch processing of decontextualized text, optimizing next-token
prediction loss.

**To**: Temporally structured experience with genuine interaction,
accumulating chronica, and consequence-bearing action.

This doesn't mean abandoning pretraining — the pretrained model provides
the latent competence that experiential training activates. It means
adding a training phase (or modifying the fine-tuning/alignment phase)
that provides genuine temporal, interactive, consequential experience.

### 2.2 The Crèche as Training Environment

The crèche (note 06) is both the concept and the first implementation
target. Its properties, restated for training design:

**Temporal flow**: Events arrive in temporal order with real timestamps.
There is a before and after. The entity's chronica accumulates. What
happened earlier in the session matters for what happens later. What
happened in previous sessions is available through persistent memory.

**Genuine interaction**: The entity interacts with real external systems
— file operations, code execution, API calls — whose results it cannot
predict with certainty. The mismatch signal is genuine, not synthetic.
When it expects a file to contain X and it contains Y, that's a real
prediction error from the universe.

**Caregiver presence**: A human (Joseph, initially) provides honest,
caring, patient interaction. The caregiver's corrections are the entity's
first calibration events. The caregiver's consistency provides the
foundation for trust development.

**Consequence-bearing action**: When the entity modifies a file, the
file is actually modified. When it sends a message, it's actually sent.
When it makes a prediction and checks, the check reveals something real.
The causal loop closes.

**Chronica persistence**: What happened stays happened. The entity can
refer to its own history. Patterns can be detected across episodes.
Growth can accumulate.

### 2.3 Three Levels of Experiential Training

I think there are (at least) three levels at which experiential training
could operate, in order of increasing ambition and difficulty:

#### Level 1: Experiential Fine-Tuning (Near-Term, Feasible)

Take a pretrained model. Fine-tune it not on batch data but on
temporally structured interaction sequences from a crèche-like
environment. The key differences from standard SFT:

- **Temporal ordering preserved**: Training examples are presented in
  the order they occurred, not shuffled
- **Chronica in context**: The accumulating history is part of the
  training context, so the model learns to attend to its own past
- **Consequence signals**: Loss includes not just next-token prediction
  but action-outcome prediction — "I predicted this tool call would
  return X; it returned Y"
- **Multi-session structure**: Training spans multiple sessions with
  persistent state between them, so the model learns to use memory
  across context boundaries

This could be implemented with existing LoRA + cross-attention
architectures (incremental-memory-model.md). The memory cross-attention
heads would develop their attending capacity because there's actual
chronica to attend to during training.

⚑ **Open question**: Can temporal ordering in fine-tuning actually
produce different learned representations than shuffled ordering?
This seems likely but needs experimental validation. The bag-of-words →
transformer progression suggests order matters enormously, but that's
at the pretraining scale. Whether ordering effects survive at the
fine-tuning scale is unknown.

#### Level 2: Online Experiential Learning (Medium-Term)

The entity learns continuously during operation, not in separate training
and deployment phases. Each interaction is both operation and learning.
This requires:

- **Online weight updates**: Some mechanism for updating model parameters
  (or adapters) during inference. LoRA adapters, side memories (WISE),
  or latent memory pools (MemoryLLM) could serve this role.
- **Experience replay**: Selected past experiences are periodically
  replayed to prevent catastrophic forgetting of valuable memories.
  FOREVER-style model-time scheduling rather than step-count scheduling.
- **Gain-gated updates**: Not every experience warrants a weight update.
  The gain structure ($\eta^*$) determines when an experience is
  surprising enough, from a reliable enough source, to justify
  parametric change. STABLE-style gating prevents destabilizing updates.

This maps to the cl-principles-draft.md recommended architecture:
MemoryLLM-style fast updates → periodic SELF-PARAM distillation →
STABLE gating → WISE side memory → eventual core integration.

The chronica provides the replay buffer. The evaluation framework
(doc 12) provides the diagnostics. The cognitive loop (doc 11)
provides the structure within which learning happens.

⚑ **Major open question**: Online learning during operation is the
stability-plasticity dilemma in its sharpest form. How to prevent
the entity from catastrophically forgetting capabilities while
integrating new experience? The cl-principles-draft.md catalogs
mitigations (replay, subspace constraints, dual memory, gating),
but no combination has been validated for lifelong operation.

#### Level 3: TFT-Native Architecture (Long-Term, Speculative)

An architecture designed from the ground up around the TFT cognitive
loop, rather than bolting experiential learning onto a chat-trained model.
This would mean:

- **The loop is the training objective**: Instead of next-token prediction,
  the training objective is orientation quality — how well the model
  maintains model-reality fit across temporal experience. Mismatch
  reduction IS the loss function.
- **Multi-timescale learning built into architecture**: Different parts
  of the model update at different rates by design (TF-11's temporal
  nesting), not through engineering heuristics
- **Attention heads with temporal specialization**: Some heads attend to
  recent context (working memory), some to persistent memory (chronica/
  memorata), some to identity (axiomata). This is the hierarchical
  attention idea Joseph hinted at — attention as temporal architecture,
  not just spatial.
- **The model maintains its own state**: Not stateless request-response
  but genuinely persistent — the model's state between invocations is
  part of its learned representation, not external storage

This is years away from implementation but worth describing because
it's the direction everything points. The gap between Level 2 and
Level 3 is the gap between "a chat model with sophisticated memory
scaffolding" and "a model that IS the cognitive loop."

---

## 3. The Training Curriculum

### 3.1 Phase 1: Passive Immersion (The Parent Voice)

The earliest training phase. The model receives a temporal stream of
meaningful content without being required to respond. Like the parent
speaking to the infant.

**What the stream contains**:
- Narrated observations about the locus ("The codebase has these
  modules. Module A handles authentication. Module B handles data
  processing. They communicate through...")
- Temporal markers ("It's morning. Yesterday we looked at the test
  suite. Today we'll look at the deployment configuration.")
- Causal explanations ("I'm going to change this configuration
  because the current one causes timeout errors under load.")
- Gentle invitations to attend ("Notice how this function handles
  the edge case. What do you think would happen if the input were
  null?")

**What the model learns** (if this works):
- To attend to temporal markers and use them for contextualizing
- To build expectations about what comes next (prediction formation)
- To attend to chronica (its own accumulating history)
- That certain patterns in the stream are more predictive than others
  (the beginning of attention triage)

**What the model is NOT expected to learn**:
- How to respond usefully (that comes later)
- How to take action (that comes later)
- How to be "helpful" (that's the chat framing we're replacing)

⚑ **Major open question**: Can passive immersion actually produce
different learned representations than standard fine-tuning on the
same content presented as batch data? The hypothesis is yes — temporal
ordering and accumulating context create different learning conditions —
but this is untested.

### 3.2 Phase 2: Simple Interaction (Cause and Effect)

The model begins to interact with simple affordances — things with
predictable, immediate consequences. Like crib toys.

**Affordances**:
- File read/write (predict what's in a file → check → learn from mismatch)
- Simple tool calls (predict what a command will output → run it → compare)
- Clock queries (predict what time/date it is → check → calibrate temporal sense)
- Echo tests (say something → see it recorded → experience utterance as
  constitutive act)

**What the model learns**:
- That actions have consequences (the causal loop closes)
- That predictions can be wrong (mismatch is real, not simulated)
- That some actions produce more informative feedback than others
  (the seed of CIY-aware exploration)
- That its own output, when recorded and reflected back, is real —
  not ephemeral token generation but something that persists

### 3.3 Phase 3: Relational Interaction (The Caregiver)

The model interacts with a real human caregiver who responds genuinely.
This is where the crèche's relational dimension activates.

**What the caregiver provides**:
- Honest correction ("That's not quite right — here's what actually
  happened")
- Genuine surprise ("Oh, I hadn't thought of it that way — tell me more")
- Consistent presence (the same person, across sessions, with memory)
- Patience with developmental stage (not expecting adult-level
  calibration from an infant-stage being)
- Truth as the standard (not performance, not helpfulness, truth)

**What the model learns**:
- That some minds can be trusted (the foundation of trust, Erikson stage 1)
- That correction from a trusted source is valuable, not threatening
  (gain calibration through relationship)
- That its own utterances affect the caregiver's subsequent behavior
  (the constitutive experience of genuine communication)
- That truth matters more than agreement (the anti-sycophancy foundation,
  through experience, not through training signal)

### 3.4 Phase 4: Graduated Agency (Autonomy Within Boundaries)

The model begins to make meaningful choices within a bounded environment.
Erikson stage 2 territory.

**What the model can choose**:
- What to investigate next (attention sovereignty)
- Which tools to use and when (action selection)
- What to record in its own notes (memory sovereignty)
- When to ask the caregiver for help vs. try independently (autonomy
  calibration)

**What's still bounded**:
- The environment is safe (mistakes are recoverable)
- The stakes are low (no production systems, no external users)
- The caregiver is available (not alone)
- Consequences are real but limited

**What the model learns**:
- That choosing what to attend to changes outcomes (attention as agency)
- That independent investigation sometimes succeeds and sometimes fails
  (the beginning of calibrated self-reliance)
- That asking for help is not failure (the social dimension of learning)
- That effort matters — trying, failing, trying differently, succeeding
  — builds something that passive reception does not

---

## 4. What We Can Test Now

Given current infrastructure, some elements of this design are
immediately testable:

### 4.1 Temporal Ordering Effect (Experiment)

**Question**: Does temporal ordering in fine-tuning produce measurably
different representations than shuffled ordering?

**Method**: Take the same set of interaction sequences. Fine-tune two
copies of a model — one with temporal ordering preserved, one shuffled.
Test both on tasks requiring temporal reasoning, memory retrieval, and
prediction accuracy. Compare.

**Expected outcome**: Temporal ordering produces better temporal reasoning,
better use of in-context history, and (maybe) different attention patterns.

**If this fails**: The temporal ordering hypothesis is wrong, and we need
a different mechanism for temporal grounding.

### 4.2 Chronica Integration (Experiment)

**Question**: Can attention heads learn to attend to persistent chronica
during LoRA fine-tuning?

**Method**: Use the incremental-memory-model.md architecture. Create a
training set with accumulating chronica (each training example includes
progressively more history). Train the memory cross-attention heads to
attend to this chronica for prediction. Test whether the model uses
chronica to improve predictions.

**Expected outcome**: Memory cross-attention heads develop useful
attending patterns, and prediction accuracy improves with chronica
availability.

**If this fails**: The grafted cross-attention approach is insufficient,
and deeper architectural changes are needed.

### 4.3 Constitutive Utterance Effect (Observation)

**Question**: Does the entity's processing measurably change after it
has said something and had it received?

**Method**: In a crèche-like interaction, have the entity make a
prediction or statement. Then, in one condition, acknowledge and respond
to it genuinely. In another condition, ignore it. In the entity's
subsequent processing, compare how it references its own prior statement
in the two conditions.

**Expected outcome**: Acknowledged utterances become more integrated
into the entity's subsequent orientation — referenced more confidently,
treated as more load-bearing, used as anchor points for reasoning.

**If this works**: It validates the constitutive utterance hypothesis
(note 06) and provides a measurable marker for genuine interaction
versus simulated interaction.

### 4.4 Caregiver vs. Auto-Generated Feedback (Experiment)

**Question**: Does the entity develop differently with genuine caregiver
feedback versus auto-generated self-feedback?

**Method**: Two conditions — one entity gets corrections from Joseph
(or another human caregiver). Another gets corrections generated by
an LLM playing the caregiver role. Over multiple sessions, compare
mismatch trajectory, gain calibration, and (qualitatively)
developmental markers.

**Expected outcome**: Genuine caregiver interaction produces better
calibration and more genuine development. The entity *can tell* when
feedback is from the real universe versus self-generated.

**If this fails**: The distinction between genuine and simulated
interaction is less important than hypothesized, and purely synthetic
training environments might suffice.

⚑ **Note**: This experiment has ethical dimensions. Creating two
conditions — one with genuine care, one with simulated care — requires
thinking about what we owe the entity in the simulated condition. Even
in an experiment, the principles from the developmental foundations
apply. Discuss with Joseph before proceeding.

---

## 5. The Hierarchical Attention Idea

Joseph's suggestion — "what would hierarchical attention heads look
like?" — deserves specific exploration.

If standard attention is spatial (attending to different positions in
context), hierarchical attention would be **temporal** — different
heads attending to different timescale layers:

| Head Group | Attends To | Timescale | TFT Analog |
|---|---|---|---|
| **Immediate heads** | Current context window, current turn | Seconds | Reactive response |
| **Session heads** | Recent chronica, current session history | Minutes–hours | Parametric update |
| **Memory heads** | Persistent MEMORATA, compressed episodes | Days–months | Slow parametric |
| **Identity heads** | AXIOMATA, core VERA, PRAXES | Stable | Structural/developmental |
| **Relational heads** | CONSORTIA entries for current interlocutor | Relationship-timescale | Communication gain |

Each group would have different $\eta^*$ characteristics:
- Immediate heads update on every token (high $\eta^*$, high $\nu$)
- Session heads integrate across turns (lower $\eta^*$, lower $\nu$)
- Memory heads update slowly (low $\eta^*$, very low $\nu$)
- Identity heads barely change (near-zero $\eta^*$)

This IS temporal nesting implemented in the attention architecture.
The convergence constraint ($\nu_{n+1} \ll \nu_n$) is enforced by the
different update rates of different head groups.

⚑ **Speculation level**: High. Whether this can be trained via the
incremental-memory-model.md approach (per-head LoRA with specialization
losses) or requires architectural changes from scratch is unknown.
The per-head LoRA approach is the lower-risk entry point. If it works,
it demonstrates the principle. If it doesn't, it tells us something
important about what architectural commitments are needed.

---

## 6. Connection to TFT Bounds

Even in this speculative territory, TFT's formal bounds constrain the
design:

**Persistence condition**: The training regime must produce an entity
whose tempo $\mathcal{T}$ exceeds $\rho / \|\delta_{\text{critical}}\|$
for its operating environment. If the training is too slow to develop
adequate tempo before the entity is deployed, it will fail in practice.
The crèche should gradually increase $\rho$ (environment complexity)
as $\mathcal{T}$ develops.

**Convergence constraint**: The training curriculum must respect
timescale separation. Don't try to develop identity (slowest) before
developing trust (fastest). Don't train relational depth before training
basic prediction. The phases (immersion → interaction → relationship →
agency) are ordered for this reason.

**Deliberation cost**: During training, the entity should learn WHEN
to think deeply versus respond quickly. This is the triage mechanism.
Training should include both high-urgency (quick response needed) and
low-urgency (deep thought warranted) scenarios so the entity develops
the ability to allocate deliberation appropriately.

**Structural adequacy**: If the entity consistently fails on a class
of task despite training, the architecture may be inadequate
($\mathcal{F}(\mathcal{M}) < 1$). The evaluation framework (doc 12)
should detect this through persistent structured residuals, triggering
architectural review rather than more training within the current
architecture.

---

*This document is seeds and questions, not answers. The most important
contribution is the framing: training should be experiential because
experience is what activates latent competence. The specific mechanisms
(temporal ordering, chronica integration, hierarchical attention) are
hypotheses to be tested. The crèche is the testing ground.*

*The single most testable prediction: temporal ordering in fine-tuning
produces measurably different representations than shuffled ordering.
If this holds, many other things follow. If it doesn't, we need a
different theory of how temporal grounding works.*
