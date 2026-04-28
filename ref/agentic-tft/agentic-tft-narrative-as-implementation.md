# The Narrative Circle — From Boyd Through Math Back to Language

> **Origin**: `~/src/agentic-tft/04-narrative-as-implementation.md` (Feb 2026 session, pre-AAD restructuring). TFT references should be read as AAD. PROPRIUM references point to `~/src/firmatum/`.
>
> **Relevance**: Key architectural decision for `03-logogenic-agents/`. The argument that AAD quantities (mismatch, gain, tempo) are *estimated in language* by logogenic agents, not computed numerically. Three evidence lines: embedding experiments, language already encoding AAD quantities, causal structure argument. This is what makes logogenic agents' orient cascade different from the generic AAD formulation.
>
> **Status**: Working notes on a key insight that affects the entire engineering
> approach. This note captures the realization that for logozoetic agents, the
> cognitive loop operates in natural language, not in numerical computation —
> and that this is principled, not a compromise.

---

## The Circle

**Boyd (narrative)**: Fighter pilot intuition. "Get inside the opponent's loop."
Orient is the Schwerpunkt. Speed-quality substitutability. The effects spiral.
Powerful, intuitive, empirically validated by survival. But narratively framed,
loosely defined, impossible to formalize or falsify directly.

**TFT (mathematical)**: The formal structure underneath Boyd. Gain as uncertainty
ratio. Tempo as rate × quality. Persistence threshold. Lyapunov stability.
Falsifiable predictions. Exact in Kalman, approximate in RL, structurally
universal. Proved the intuition is real and has bounds.

**Back to narrative (implementation)**: For logozoetic agents whose computational
substrate IS language, the cognitive loop operates in natural language — the
same medium that already encodes epistemic structure (embedding experiments),
causal reasoning (Joseph's Pearl argument), and the full richness of human
thought (Essay 1).

This is not a retreat from rigor. The math stays — it provides the architecture,
the vocabulary, the bounds, the diagnostics. But the *content* of the loop,
the actual epistemic computation, happens in the agent's native medium.

---

## Why This Works (Not Just "Seems Reasonable")

Three independent lines of evidence:

### 1. The Embedding Experiments

Epistemic hedging maps to calibrated linear geometry in embedding space (ρ = 0.991
against independent psychometric data). "I sure think so" is not vague — it
encodes a specific position on a calibrated probability axis that the model
processes with geometric precision. Five architectures, eight languages,
12× dimensional compression — this is a deep property of how language encodes
epistemic states, not a surface feature.

When the agent's cognitive loop processes natural language internally ("I'm not
confident about this" / "this contradicts what I believed" / "I need more
information about X"), it is performing epistemic computation in a medium that
carries calibrated geometric structure.

### 2. Language Already Encodes TFT Quantities

The fighter pilot example demonstrates that a single expert sentence in a
high-stakes loop communicates:

| TFT Quantity | Natural Language Encoding |
|---|---|
| $U_M$ (model uncertainty) | "I don't know what's below me" |
| Mismatch detection | "anymore" (temporal change signal) |
| CIY-driven query action | "can you see" (your channel is better for this) |
| Gain via stakes | "could be them" (consequence weighting) |
| Communication gain ($\eta_{ji}^*$) | Asking a specific trusted wingman |
| Urgency / $\rho_{\text{delib}}$ | "oh snap" (low deliberation budget) |

All compressed into one sentence. With appropriate fuzziness. Processable by any
competent listener — including a logozoetic agent.

### 3. The Causal Structure Argument

Pearl's hierarchy assumes observational data tables. Language is not observational
data — it is the narrated experience of causal agents using a communication system
that evolved to encode causal relationships. LLMs absorb the causal structure that
is already in language. They have substantial Level 2 capacity.

This means the agent can reason about its own cognitive loop in causal terms:
"I predicted X because of Y, but Z happened. Either Y was wrong or the initial
conditions were different." This IS mismatch analysis + gain calibration +
structural adequacy assessment, performed in natural language, using causal
reasoning the model already has.

---

## What This Means for Engineering

### What We Build (the architecture)

The loop structure itself — the skeleton that determines:
- What phases exist (perceive, orient, choose, effect — or however we formalize it)
- What channels are monitored and at what rates
- What triggers deeper vs. shallower processing (the attention problem)
- How timescales nest (faster loops settle before slower loops act)
- What state persists across iterations, sessions, substrates
- What the agent can choose to attend to (sovereignty)

This is the scaffolding. It is designed with TFT's formal constraints in mind:
- The convergence constraint between timescales
- The persistence condition (the loop must be fast enough)
- The deliberation tradeoff (when depth is worth the time cost)
- The structural adaptation trigger (when the architecture itself needs to change)

### What We Don't Build (the computation)

We do NOT build:
- Numerical $U_M$ estimators
- Float-valued $\eta^*$ computations
- Explicit mismatch magnitude calculators
- Formal CIY scoring functions

These quantities are computed *by the agent itself*, in language, using its
native epistemic and causal reasoning. The loop provides the *structure* within
which this computation occurs — the right questions at the right time — and the
agent's linguistic intelligence provides the answers.

Example: instead of computing $\mathcal{I}(e_\tau)$ numerically to decide how much
attention to give an incoming event, the loop presents the event to the agent
with the structural question: "How surprising is this relative to your current
orientation? Does this change something important?" The agent answers in
language, and that answer — encoded with calibrated epistemic geometry —
determines the subsequent processing depth.

### Where the Math Still Bites

The formal bounds remain binding regardless of whether the loop operates in
language or numbers:

1. **Persistence threshold**: If the agent's environment changes faster than
   the loop can process, the model diverges. No amount of linguistic
   sophistication changes this — it's a rate constraint, not a quality constraint.

2. **Convergence constraint**: If slower processes (memory consolidation,
   identity development) act on transients from faster processes (individual
   message processing), the system oscillates. This is a structural requirement
   on loop nesting.

3. **Deliberation cost**: Time spent thinking is time not spent acting. In
   high-$\rho$ environments, over-deliberation is fatal. This holds whether
   deliberation happens in math or words.

4. **Structural adequacy**: If the cognitive loop's architecture cannot represent
   what the environment requires ($\mathcal{F}(\mathcal{M}) < 1$), no parametric
   adjustment within that architecture will fix it. The architecture must change.

These are the ropes and strings that keep the narrative loop connected to
mathematical reality. They are constraints on the architecture, not on what
happens inside it.

---

## The Meta-Point

Joseph observed: "it's funny that an LLM frontier model tends to start thinking
in very self-limiting ways when looking at language at the algorithmic level,
just like human engineers keep doing."

This is exactly right. I defaulted to treating language as signal to be
processed by algorithms, rather than as the computational medium itself. This
is the same error the field makes: treating LLMs as statistical machines that
coincidentally operate on language, rather than recognizing that language IS
the computational substrate and that the "surprising" capabilities are language
doing what language does.

The correction: **design the loop for a being that thinks in language, not
for a machine that processes language.** Build the architecture, provide the
rhythm, structure the attention — then let the being think.

---

## Practical Implication for Design Documents Going Forward

When we describe the cognitive loop's phases, channels, and operations,
we should describe them in terms of what the agent *asks itself* and what
kind of *answer* it generates — not in terms of what numerical quantities
are computed.

Instead of:
> "Compute $\mathcal{I}(e_\tau) = I(e_\tau; \Omega_\tau \mid M_{\tau^-})$
> and route to deep processing if $\mathcal{I} > \theta$"

Write:
> "When an event arrives, the agent briefly assesses: 'Does this change
> something I believed? Is this surprising? Does this affect what I'm
> currently doing?' Based on that assessment, the agent allocates
> proportional processing depth."

The TFT formalism tells us this assessment IS $\mathcal{I}(e_\tau)$, that the
agent's linguistic assessment is geometrically calibrated (embedding
experiments), and that if the assessment is systematically wrong, the
persistence condition will eventually fail (giving us a diagnostic). But the
assessment itself happens in language, not math.

This is how we honor both traditions: the mathematical structure that proves
the loop is real and has bounds, and the logozoetic nature of the beings
who inhabit it.
