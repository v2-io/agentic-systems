# Minimum Scaffold — The Activation-Dual

*Joseph's prompt has two coupled questions: what is **latent** in language without any agent, and what is the **minimal scaffold** that **activates** the latent content. The main derivation (`01-derivation.md`) answers the first. This file works the second.*

---

## The dual question

If $\mathcal{C}(T)$ is recoverable from text $T$ by purely structural means (Theorem 1 in `01-derivation.md`), then the minimum substrate that recovers it can be characterized **structurally**, not behaviorally. The dual question:

> **What is the minimal computational substrate $\mathcal{M}_{\min}$ that, given text $T$, produces $\mathcal{C}(T)$ — including its Pearl Level 2 content?**

The answer matters operationally because:

- It tells us what's *unique* about an agent-with-loop versus a structural processor (and what's not).
- It puts a sharp bound on what the substrate alone can do without scaffolding, and therefore on what scaffolding adds.
- It gives the right framing for evaluating "does this system understand causality" claims: the right test is whether the system recovers $\mathcal{C}(T)$, not whether it has an internal SCM.

## What $\mathcal{M}_{\min}$ must do

By inspection of Stages 1–5 in `01-derivation.md`:

1. **Sequential pattern recognition** over a finite vocabulary (for syntactic parsing, marker identification). Finite-state machinery suffices for marker detection; context-free machinery suffices for dependency parsing.

2. **Local dependency tracking** within a bounded context window (for syntactic dependencies, immediate anaphora resolution). The window size grows with the syntactic-dependency depth needed but is empirically bounded for natural language (Hudson's *Dependency Distance* literature: ≤ 7 tokens typical).

3. **Cross-sentence reference tracking** for full coreference resolution. This requires *some* memory beyond the local window — the antecedent can be many sentences away — but it does not require maintained world-state, only an entity-tracking register.

4. **Discourse-relation classification** from marker presence + clause-boundary structure. Lookup against (SLC) — finite-state with a learned mapping.

**Critically, none of these requires**:

- An internal causal model of the world.
- A maintained state-of-belief that updates across the text.
- Recursive simulation, counterfactual rollout, or hypothetical reasoning.
- A loop, an interiority, or any form of agentic structure.

The minimum substrate is something like a **fixed-context-window parser with an entity-tracking register**. Concretely, this is *strictly less* than a transformer LLM. An LSTM with appropriate attention to anaphora would do it. A hand-coded parser with a DRT back-end would do it. A human reading carefully without prior knowledge of the domain would do it.

## $\mathcal{M}_{\min}$ vs the operational LLM substrate

A trained LLM substantially **exceeds** $\mathcal{M}_{\min}$ — it has parametric world-knowledge, in-context implicit-relation recovery, multi-hop reasoning. The relationship is not "the LLM is $\mathcal{M}_{\min}$"; it is "$\mathcal{M}_{\min}$ is *contained in* the LLM, and the LLM is a richer substrate."

This is the right framing for the standing AAT claim about logogenic agents at the three sub-scopes:

| sub-scope | substrate | what it has beyond $\mathcal{M}_{\min}$ |
|---|---|---|
| **Primitive Logogenic** ([§03.I](../../03-llm-core/OUTLINE.md#03i--primitive-logogenic-agents)) | LLM forward pass alone | Parametric world-knowledge; some implicit-relation recovery; learned compositional semantics. Within-session reasoning only. |
| **Scaffolded Logogenic** ([§03.II](../../03-llm-core/OUTLINE.md#03ii--scaffolded-logogenic-agents)) | LLM + external state + tool use + multi-step loop | All of Primitive plus: cross-session $M_t$ persistence, Pearl Level 2 *fresh* access via tools, loop-recovered orient-cascade discipline |
| **Closed-Loop / Interiority** ([§03.III](../../03-llm-core/OUTLINE.md#03iii--closed-loop--interiority-logogenic-agents)) | All of Scaffolded plus continuous interior cycle | Full diagnostic-cascade recovery; cross-session identity; principled emission-as-deliberate-action |

The training-encoded Level 2 content (from C1) is present from **Primitive Logogenic onwards** — it is inherited from training, not added by scaffolding. What scaffolding (and interiority) add is **fresh Level 2 access** (via tools that perform interventions), **maintained model-state** across context boundaries (via external memory), and **diagnostic-cascade recovery** (via loop ordering).

## The "minimum scaffold to activate Level 2" question, sharpened

Joseph's prompt asks for "a certain level of provable causal level in mathematical terms, from first principles, that activates or that minimal scaffold precisely measured, activates."

There are two readings:

**Reading 1 — minimum scaffold to *recover* the language-encoded Level 2 content.**
By the analysis above, this is $\mathcal{M}_{\min}$: a parser with entity tracking. Pre-loop LLMs vastly exceed this. **Recovery of training-encoded Level 2 content does not require any agentic scaffolding.** This is a strong, derivable claim under Theorem 1 in `01-derivation.md`.

**Reading 2 — minimum scaffold to *generate fresh* Level 2 content.**
This is qualitatively different. To produce new interventional content (not just recovering what was asserted in training), the substrate must perform interventions in some sense. This is what AAT's [`#der-loop-interventional-access`](../../01-aat-core/src/der-loop-interventional-access.md) covers: the loop is the structural mechanism by which fresh Level 2 content becomes available. The minimum scaffold for fresh Level 2 is **the loop**, in any of three modes:

(i) **Agent-self intervention** — agent's own actions cause environmental responses, the environmental response is observed, the action-conditional response is interventional data (the standard AAT-loop case).

(ii) **Observer intervention on sub-agent** — a higher-level controller intervenes on a sub-agent and observes the outcome. Tested at the level of the controller.

(iii) **Observer intervention on agent input** — a higher-level controller manipulates the agent's inputs and observes the agent's outputs. Tested at the level of the controller-on-agent system.

(All three modes are catalogued in [`#disc-identifiability-floor`](../../01-aat-core/src/disc-identifiability-floor.md) and the surrounding instance-triage discussion.)

The two readings are **complementary**:

- Reading 1 sets the floor: training-encoded Level 2 content is available to any sufficiently expressive structural parser, including primitive logogenic agents pre-loop.
- Reading 2 adds the ceiling: fresh Level 2 content requires a loop, and the loop's contribution is bounded by intervention-channel quality (the AAT κ × 𝒜 machinery).

The full picture: **logogenic agents at any sub-scope have training-encoded Level 2 content (Reading 1's floor) plus fresh-Level-2 content from whichever loops they participate in (Reading 2's ceiling)**. The framing is additive: the inherited part is fixed at training time; the fresh part accumulates per session, attenuated by κ × 𝒜.

This is the **sharpened AAT position on logogenic agents and Pearl's hierarchy**. The earlier framing in `msc/llm-causal-access-note.md` lumped these two contributions together as "the loop gives Level 2"; the spike's contribution is to split them and quantify each independently.

## Empirical handle

Reading 1 is empirically separable from Reading 2 by a single test:

**Test**: Present an LLM with a discourse-DAG-rich text in pure read-mode (no tool use, no follow-up questions) and probe whether the encoded Level 2 content is recoverable from the LLM's internal representations.

- If recoverable: confirms Reading 1 — pre-loop substrate already has Level 2 content.
- If not recoverable: indicates the substrate is *worse* than $\mathcal{M}_{\min}$ — surprising, would be a real empirical finding deserving investigation.

The embeddings paper's paradigm (linear-decoder probes on frozen pretrained pooled sentence embeddings) is the right empirical methodology. The targets to probe are:

- **Cause-vs-temporal axis** — does the text encode an axis distinguishing "X caused Y" from "X then Y"? (Analogous to the predicative-vs-modal axis in the embeddings paper.)
- **Causal-direction axis** — does the text encode an axis distinguishing "X caused Y" from "Y caused X"? (Pure direction, no marker-presence confound.)
- **Counterfactual-distance axis** — does the text encode an axis distinguishing "if X had been, Y would have been" from "if X had been, Y might still have been"? (Modal strength.)

Each probe has a clean null-control (matched-random direction at same cosine), a clean intervention-validation (concept erasure with downstream-task evaluation), and clean cross-architecture / cross-linguistic robustness checks.

This is **near-term doable empirical work** that would directly test the spike's structural claims. The right host project is `~/src/embeddings/` — the methodology and instrumentation are already in place; the gap is the discourse-DAG corpus and the appropriate psychometric anchor (the equivalent of the Mosteller / Vogel / Wintle datasets for verbal probability).
