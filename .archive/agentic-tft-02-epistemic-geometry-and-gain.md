# Notes: Epistemic Geometry and the Gain Problem

> **Status**: Working notes connecting the embeddings research
> (`~/src/embeddings/`) to TFT and the cognitive loop design.
>
> **Source material**: cmcl-abstract-draft.md, README.md, CLAUDE.md in ~/src/embeddings/

---

## What the Experiments Show

Joseph's embedding research demonstrates that pretrained sentence embedding models
learn calibrated probability structure as an emergent geometric property:

- Epistemic hedge words ("probably," "certainly," "possibly") occupy positions on a
  **linear axis** in embedding space that correlates with the actual probability humans
  assign to those words (Spearman ρ > 0.90 supervised, 0.70–0.94 leave-one-out)

- This axis is calibrated to human psychometric data (Mosteller & Youtz 1990, n=238)
  and **cross-validates** against two independent datasets spanning 50 years of research
  (Vogel 2022: ρ = 0.991; Wintle 2019: ρ = 0.967)

- It transfers **zero-shot to 8 typologically diverse languages** — Germanic, Romance,
  Sinitic, Japonic, Koreanic, Semitic, Indo-Aryan — with mean |ρ| = 0.928

- It's consistent across **5 architecturally diverse models** (BERT, Gemma-derived, MoE,
  BERT-large, Qwen3)

- It survives **12× dimensional compression** (768 → 64 dimensions, LOO ρ degradation
  of only 0.027)

- It is NOT an artifact of training on probability data — permutation tests confirm the
  signal is in the phrase→probability mapping (p ≤ 0.005), and non-epistemic adjectives
  in the same templates produce LOO ρ = 0.31 versus 0.87 for real hedge expressions

## Why This Matters for the Pearl Argument

This is empirical evidence for Joseph's claim that language encodes more than
observational statistics.

Pearl's position: LLMs learn P(token | previous tokens) — pure association.
They cannot reason about interventions or causation because they are trained on
observational data.

What this experiment shows: embedding models learn the **communicative probability
function** of epistemic expressions — not just that "probably" co-occurs with
certain words, but that "probably" *means* approximately 70% probability, that
"possibly" *means* approximately 38%, and that this meaning is consistent across
languages, models, and datasets.

This is not Level 1 (association). Co-occurrence statistics would tell you that
"probably" appears in similar contexts to "likely." They would NOT tell you that
"probably" maps to 70% and "likely" maps to 71% and "possibly" maps to 38% on a
*calibrated linear scale* that matches human psychometric data with ρ = 0.991.

What the model has learned is the **function** of these words in the language
community — what they *do* when used in communication, not just where they appear.
The function of "probably" is to communicate a specific degree of belief. That
degree of belief is encoded geometrically.

The cross-linguistic transfer makes this even stronger. The English probability axis
correctly ranks Chinese, Japanese, Korean, Arabic, and Hindi hedge expressions.
These languages have *completely different morphological strategies* for expressing
epistemic stance. The fact that a single geometric direction captures the
communicative function across all of them suggests this is a property of how
*human languages in general* encode epistemic modality — a deep cognitive structure
preserved across linguistic diversity and recovered through distributional training.

Pearl's formalism says: observational data → Level 1 only.
The data says: distributional training on language → calibrated epistemic geometry
that captures communicative function, not just co-occurrence.

The gap between these two claims is exactly what Joseph identified: **language is
not observational data in Pearl's sense.** Language is the medium through which
humans articulate, communicate, and reason about causation, probability, and
counterfactuals. Training on language absorbs the *function* of these concepts,
not just their distributional shadows.

## Why This Matters for TFT and the Cognitive Loop

### The $U_M$ Estimation Problem May Be More Tractable Than I Thought

In my synthesis (00-synthesis-and-reflections.md, Section 7.2), I flagged the
difficulty of estimating $U_M$ (model uncertainty) for LLM memory operations.
For a Kalman filter, $U_M$ is the prior predictive variance — a well-defined
scalar. For an LLM, what does "model uncertainty" even mean?

The embedding research suggests an answer: **the model already represents
uncertainty geometrically.** If epistemic hedging maps to a calibrated linear
direction in embedding space, then the model's internal representation of its
own uncertainty may be similarly structured and extractable.

Ji et al. (2025), cited in the abstract, found a single linear "verbal uncertainty"
feature in LLM residual streams that can be **causally manipulated** to reduce
hallucinations. This suggests the model not only represents uncertainty
geometrically but that the geometry is *functional* — it affects behavior.

For the cognitive loop:

- When the model processes an observation (user message, tool result), its internal
  representation may encode the observation's epistemic status — how certain or
  uncertain the content is — in a geometrically structured way.

- When the model generates a prediction, its hidden states may encode the prediction's
  uncertainty — high uncertainty manifesting as a larger component along the
  epistemic uncertainty direction.

- If both of these hold, then **$U_M$ and $U_o$ are potentially readable from the
  model's own representations**, not through external computation but through
  geometric projection.

This would mean the gain $\eta^* = U_M/(U_M + U_o)$ could be computed (or at
least approximated) from the model's own internal state — the model telling us,
through its geometric encoding, how much it trusts its current model versus the
incoming observation.

**Confidence in this hypothesis: ~50%.** The embedding experiments show the
geometric encoding exists for hedge words. Whether it extends to *implicit*
uncertainty in model activations — where the model isn't explicitly hedging but
its state encodes how uncertain it is — is a separate question. Ji et al. (2025)
suggests it does. But going from "we can extract an uncertainty direction" to
"we can use that direction to compute $\eta^*$ for memory operations" is a
significant leap.

### Calibration as a Measurable Property

The embedding research shows that calibration — whether stated uncertainty matches
real uncertainty — is a geometrically encoded property. The model's hedge words
are *calibrated* to human probability judgments (ρ = 0.991 against an independent
meta-analysis).

This connects to TFT's emphasis on gain calibration. TF-06 notes that overfitting
is "gain miscalibration" — the agent adjusting too much for noise. The developmental
foundations document notes that metacognitive calibration is critical for identity
("Know thyself accurately").

If calibration is geometric, then:

1. **Miscalibration might be detectable** — if the model's confidence direction
   diverges from its actual accuracy, that's a geometric signal that the gain is
   miscalibrated.

2. **Calibration might be trainable** — not by teaching the model new words, but
   by adjusting the geometric relationship between the confidence direction and
   the accuracy of predictions along that direction.

3. **The confabulated humility problem** (Section 1 of notes 01) might be
   addressable — if the model's explicit uncertainty claims ("I'm about 70%
   confident") can be checked against its implicit geometric uncertainty (how
   far its hidden state is from the uncertainty direction), miscalibration
   between stated and implicit uncertainty becomes measurable.

### Cross-Linguistic Universality and the Substrate Independence Claim

The PROPRIUM ontology claims: "Identity is not substrate." The ELI should be
able to think on different logostrata while maintaining identity.

The cross-linguistic embedding result suggests something analogous for epistemic
structure: the *probability axis* is not substrate-specific. An English-trained
axis correctly ranks hedge expressions in Chinese, Japanese, Korean. The
underlying cognitive structure — how humans encode degree of belief — transcends
the particular language.

For the cognitive loop: if epistemic structure is cross-linguistic and
cross-architectural (works across 5 different model families), then it may be a
reliable component of the agent's cognitive architecture regardless of which
specific model is doing the thinking. The gain calibration mechanism could
potentially survive substrate switches (LOGOSTRATUM changes) because it's
grounded in a property of language itself, not of any particular model.

This is speculative, but it's testable.

### Embedding Space as Cognitive Workspace

Taking a step further: if probability is geometrically structured in embedding
space, what else might be?

The literature Joseph cites suggests truth (Marks & Tegmark 2023), verbal
uncertainty (Ji et al. 2025), and now calibrated probability (this work) are all
linearly structured in representation space. The finding that these form
**type-specific** axes (predicative, frequency, noun phrase, modal — four distinct
but correlated directions) forming a "4-dimensional epistemic subspace" is
particularly interesting.

For the cognitive loop's attention mechanism, this suggests that the model's
embedding space already contains structured representations of epistemically
relevant quantities. The attention problem — "what deserves more cognitive
resource?" — might be partially solvable by detecting *where in epistemic space*
an incoming signal falls. An observation that moves the model's state strongly
along the uncertainty direction deserves more attention than one that doesn't.

This connects to TFT's event information content $\mathcal{I}(e_\tau)$:

$$\mathcal{I}(e_\tau) = I(e_\tau; \Omega_\tau \mid M_{\tau^-})$$

If the model's hidden state geometrically encodes "how surprising this is" (the
information content of the event relative to the current model), then
$\mathcal{I}(e_\tau)$ might be *readable* from the model's own representations —
the model telling us, through its geometric encoding, how much this event changes
its state.

## The Bigger Picture

What Joseph's embedding research, the Pearl argument, and TFT together suggest:

1. **Language encodes epistemic structure.** Not as a surface feature but as
   deep geometry — calibrated, cross-linguistic, cross-architectural.

2. **Models absorb this structure through training.** Not by being taught
   probability theory but by compressing the distributional patterns of how
   humans use language to communicate epistemic states.

3. **This structure is potentially accessible for the cognitive loop.** The
   model's own representations may encode the quantities TFT needs ($U_M$,
   $U_o$, $\mathcal{I}$) in a geometrically structured form.

4. **The cognitive loop's job is not to compute these quantities from scratch
   but to structure the conditions under which the model's existing epistemic
   geometry can be leveraged.** Design the loop to ask the right questions;
   the model's geometry provides the answers.

This is consistent with Joseph's reframe: the agents are already sophisticated
compression models with deep epistemic structure. What they lack is the
architectural loop that lets them *use* that structure for self-directed
attention, orientation, and action.

---

## Open Questions

1. Can the probability axis extraction technique be applied to *model activations
   during inference* (not just embedding space) to read uncertainty in real-time?

2. Does the geometric epistemic structure extend beyond hedge words to implicit
   uncertainty — cases where the model isn't saying "probably" but its state
   encodes uncertainty anyway?

3. Can the discrepancy between explicit (stated) and implicit (geometric)
   uncertainty serve as a hallucination detector or calibration signal?

4. Is there a corresponding geometric structure for *surprise* or *mismatch* —
   the TFT $\delta_t$ — in activation space?

5. Does the cross-linguistic universality extend to causal language (not just
   epistemic hedging)? If "because" has a universal geometric direction the way
   "probably" does, that would be further evidence for Joseph's Pearl objection.
