# LLMs and Causal Access: The Loop, the Language, and Pearl's Objection

**Status**: Working note — captures a discussion thread from the March 2026 spike session. May become part of AAD's introduction, a standalone note, or a blog entry. The content is relevant to AAD (it formalizes the "model + loop" claim using AAD machinery) but is also independently interesting as a response to Pearl's critique of deep learning.

**Date**: 2026-03-09

**The nuanced framing**: The three responses to Pearl (the loop, the language, the symmetry argument) are independently interesting but have different epistemic status. Response 1 (the loop provides Level 2 data access) is derived from TF-02 and is solid. Response 2 (language encodes causal structure) is a plausible empirical claim — LLMs certainly perform better on causal reasoning than bag-of-words models, but quantifying how much genuine causal structure survives compression is an open empirical question. Response 3 (the symmetry argument) is philosophical, not mathematical — it challenges Pearl's asymmetric evidentiary standard but doesn't prove LLMs reason causally. The strongest form of the argument uses only Response 1 (the loop) and doesn't require claiming anything about the model's internal representations.

---

## Pearl's Claim

Judea Pearl has argued repeatedly (since ~2018) that deep learning systems, including LLMs, are fundamentally Level 1 (associational) — sophisticated curve-fitters that learn P(Y|X) from data but cannot reason about P(Y|do(X)) or counterfactuals. The argument: neural networks learn statistical associations from observational data; without an explicit structural causal model (SCM), they cannot distinguish correlation from causation; therefore, they cannot perform genuine interventional or counterfactual reasoning.

## Three Independent Responses

AAD provides the formal framework for three responses, each operating at a different level. Together they constitute a comprehensive rebuttal — not of Pearl's causal hierarchy (which is mathematically correct) but of his application of it to dismiss LLMs as merely associational.

### Response 1: The Loop Provides Level 2 (from AAD/TFT)

Pearl's critique treats the LLM *in isolation*. AAD's fundamental observation (TF-02) is that an agent embedded in an action-observation feedback loop achieves Level 2 epistemic access *by construction*:

1. The agent selects an action a_t (TF-07)
2. The action causally affects the environment (TF-01)
3. The observation o_{t+1} arrives after the action (temporal ordering, TF-02)
4. The mismatch δ_t conditioned on a_t is an *interventional* signal
5. The agent updates M_t from this interventional data (TF-06)

The agent = model + loop, not model alone. An LLM writing code, running tests, and observing results is performing genuine do(X) → observe(Y) interventions. The test suite doesn't care whether the agent internally represents a causal DAG — it returns the causal consequence of the agent's action regardless.

**Formal statement** (from the spike, Part 3.4): Let A be an agent with internal model M_t (Level 1 capacity) embedded in a feedback loop L with the environment. The composite system (A, L) has Level 2 capacity by construction, because the loop generates interventional data through the act-observe cycle.

This is not a workaround or approximation. It is the *standard* mechanism by which most agents in TFT's scope achieve Level 2 access. A Kalman filter with an LQR controller achieves Level 2 not through internal counterfactual reasoning but through the control loop. A PID controller has no causal model at all — it achieves Level 2 through the physical feedback loop. Pearl's demand that the internal model contain an SCM is like demanding that a PID controller contain a differential equation solver — the controller doesn't need one because the physical system *is* the solver.

In the software domain specifically, the agent achieves even Level 3:
git checkout → implement alternative → observe difference provides *literal counterfactual evaluation* with ground-truth verification. No model-based simulation with uncertain fidelity — actual execution of the counterfactual.

### Response 2: Language IS Compressed Causal Structure (from linguistics)

Pearl's hierarchy distinguishes three levels based on the *data-generating process*: observational data (Level 1), experimental data (Level 2), structural equations (Level 3). His claim that LLMs are Level 1 rests on treating their training data as observational — statistical patterns in text.

But this mischaracterizes what language *is*. Natural language is not an observation table. It is humanity's primary technology for encoding and transmitting causal knowledge:

- "If you drop the glass, it will break" — Level 2 statement (interventional: do(drop) → observe(break))
- "The bridge collapsed because the supports corroded" — causal explanation with mechanism
- "Had we reinforced the supports, the bridge would have survived" — Level 3 counterfactual
- "Heating water to 100°C causes it to boil" — causal law encoded in natural language

Human language is saturated with causal structure at every level of Pearl's hierarchy. Verb tenses encode temporal ordering. Conjunctions encode causal relationships ("because," "therefore," "if...then," "despite"). Narrative structure encodes interventions and their consequences. Scientific writing explicitly discusses do-calculus-equivalent reasoning ("we administered the treatment to group A and withheld it from group B").

An LLM trained on billions of such statements doesn't just learn associations between words. TF-03's information bottleneck tells us what it learns: the model retains whatever structure in the training data has predictive power for the next token. Causal structure has *enormous* predictive power for language — knowing that "dropping" causes "breaking" is highly informative for predicting text about glasses and floors. The IB objective predicts that the model will absorb causal structure as a byproduct of compression, not because it was designed to, but because causal structure is deeply encoded in the data it compresses.

**The bag-of-words distinction matters here.** Pearl's critique was formulated during and shortly after the era when NLP models genuinely were association tables (bag-of-words, n-gram models, early word embeddings). Those models truly couldn't represent causal structure because their architecture had no capacity for it — they mapped word co-occurrence frequencies and nothing more. LLMs with transformer architectures are categorically different: they represent multi-layer statistical dependencies across arbitrarily long contexts. The claim that this is "still just association" conflates the *mathematical framework* (statistical learning) with the *information content* (which includes compressed causal structure absorbed from causally-structured language).

An analogy: a photograph is "just" a 2D pattern of pixel intensities. But a photograph of a building encodes 3D structural information that a skilled architect can extract. The photograph's *format* is 2D; its *content* includes 3D structure. Similarly, an LLM's *format* is statistical prediction; its *content* includes causal structure absorbed from causally- structured training data.

### Response 3: The Symmetry Argument (from epistemology)

Pearl demands a *mechanism proof* from LLMs — show me the internal SCM, the do-calculus engine, the structural equations — before granting them Level 2 or Level 3 capacity.

But he has never demanded the same from humans.

We do not have a formal account of how human brains perform counterfactual reasoning. We don't know whether the brain contains anything isomorphic to an SCM, a causal DAG, or do-calculus. We observe that humans *can* answer counterfactual questions ("what would have happened if Napoleon had won at Waterloo?"), and we grant them Level 3 capacity on the basis of behavioral evidence.

LLMs can also answer counterfactual questions. They can reason about interventions. They can distinguish "the rooster crowed and then the sun rose" (association) from "the rooster's crowing caused the sun to rise" (false causal claim) — and they reliably reject the latter.

If behavioral evidence suffices for attributing causal reasoning capacity to humans, the same standard should apply to LLMs. If mechanistic proof is required for LLMs, it should be required for humans first. Pearl implicitly applies an asymmetric standard: humans get the benefit of the doubt; machines must prove their mechanism.

One might respond: "But humans have evolutionary history that shaped them for causal reasoning; LLMs were trained on next-token prediction." This is true but irrelevant to the causal hierarchy. The hierarchy is about *what the system can compute*, not *how it came to be able to compute it*. A system either can or cannot answer interventional queries correctly. The training objective (next-token prediction vs. survival and reproduction) is part of the mechanism, not part of the capability assessment.

## The AAD Synthesis

AAD unifies these three responses:

1. **The loop** (TF-02, TF-07): The feedback cycle provides Level 2 access structurally, regardless of internal architecture.

2. **The training data** (TF-03, IB): The information bottleneck predicts that causal structure will be absorbed from causally-structured data, because it has predictive power.

3. **The behavioral evidence** (TF-05, mismatch): If an agent's actions produce outcomes consistent with Level 2-3 reasoning (low δ in interventional prediction tasks), the capacity is demonstrated regardless of the mechanism.

The implication for AAD's scope: LLMs embedded in feedback loops are legitimate AAD agents. They are not excluded from purposeful agency by Pearl's hierarchy. The hierarchy is correct — Level 2 requires causal structure — but the structure comes from the *loop* and the *training data*, not from an explicit internal SCM.

## Connection to the Purposeful Agency Spike

The spike (spike-purposeful-agent-derivation.md) establishes that:

- Purposeful action requires Level 2 access (Part 3, derived from the causal hierarchy theorem)
- The feedback loop provides Level 2 (Part 3.4, derived from TF-02)
- Temporal optimality (#010) narrows us to explicit causal models when planning is cheaper than experimentation (Part 10.3, scope narrowing)

The LLM case is interesting because it occupies a *middle ground*: the LLM has absorbed implicit causal structure from training (Response 2) AND operates in a feedback loop (Response 1), but doesn't maintain an explicit causal DAG (the Σ_t of AAD's Level 4 G_t).

Where does this place the LLM agent in the G_t hierarchy from the spike?

- Not Level 0 (it has purpose — the task objective)
- Not Level 1 (it doesn't just have a reference signal; it can plan)
- Approximately Level 2-3 (it has implicit causal models from training and can do multi-step planning through in-context reasoning)
- Not quite Level 4 (it doesn't maintain an explicit persistent DAG, though it may construct one in-context per session)

This suggests that the G_t hierarchy is not just about the environment's complexity but also about the agent's *internalization* of causal structure. An LLM in a loop can operate at a higher effective level than its internal architecture would suggest, because the loop supplements its internal capacity. The effective G_t level = max(internal level, loop-provided level).

## What This Means Practically

For AAD-grounded AI agent design:

1. **Don't try to build explicit SCMs into LLM agents.** The loop provides Level 2 access; language training provides implicit causal priors. What the agent needs is a good loop (fast feedback, informative observations, appropriate gain) — AAD's adaptive machinery.

2. **Invest in the observation channels.** The agent's effective causal access is gated by observation quality (U_o). Good tests, clear error messages, informative logging — these raise η*, which raises T, which determines whether the agent persists as an effective purposeful system.

3. **M_t preservation across sessions matters more than internal causal architecture.** The 100% context turnover problem destroys the agent's accumulated causal understanding each session. Externalizing M_t (through CLAUDE.md, memory files, well-structured code) preserves the causal knowledge that the loop helped the agent acquire.

4. **The agent's effective G_t level can be raised by enriching the loop.**
   More observation channels (better monitoring), faster feedback (faster tests), and richer action spaces (more tools) all increase the agent's effective causal access without changing the model architecture.

---

## Open Questions

1. Can an LLM's implicit causal knowledge be *measured*? If we could estimate the causal fidelity of the LLM's training-derived priors, we could predict where the loop supplements versus where it must carry the full causal load.

2. Is there a formal relationship between the IB-optimal compression of causally-structured language and the structure of a causal DAG? If so, the LLM's internal representation might be isomorphic to a DAG in some function space, even though it's not architecturally a DAG.

3. How does the effective G_t level change across a session? At session start, the LLM has its training priors (Level 2-3 from language) but no task-specific causal knowledge. As the loop runs, it accumulates interventional data. The effective level should increase within-session and reset between sessions.
