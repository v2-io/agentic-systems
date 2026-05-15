---
slug: disc-m-preservation
type: discussion
status: discussion-grade
depends:
  - obs-context-turnover
  - scope-logogenic-agent
  - result-persistence-condition
  - def-model-sufficiency
  - def-adaptive-tempo
stage: draft
---

# Discussion: External Memory as Persistent $M_t$

The 100% context turnover at session boundaries ( #obs-context-turnover) means the LLM agent's epistemic state must be reconstructed from external storage each session. The standard persistence condition ( #result-persistence-condition) — $\alpha \gt \rho / R$ — governs intra-session dynamics. Across sessions, the relevant condition is whether the externalized state can be reconstructed with sufficient fidelity: a *reconstruction adequacy* condition rather than a *rate* condition.

## Formal Expression

*[Discussion (m-preservation-condition)]*

### The inter-session persistence condition

Let $M_k^-$ denote the epistemic state at the end of session $k$, and $M_{k+1}^+$ denote the reconstructed state at the start of session $k+1$. The **externalization-reconstruction cycle** is:

$$M_k^- \xrightarrow{\text{externalize}} \mathcal{E}_{\text{ext}} \xrightarrow{\text{reconstruct}} M_{k+1}^+$$

The **reconstruction error**:

$$\epsilon_{\text{recon}} = d(M_k^-, M_{k+1}^+)$$

where $d$ is a distance on $\mathcal{M}$ (e.g., $\lVert M_k^- - M_{k+1}^+\rVert$ in a suitable norm, or the KL divergence if $M_t$ is a probability distribution).

The inter-session persistence condition:

$$S(M_{k+1}^+) \geq S_{\text{min}}$$

where $S(\cdot)$ is model sufficiency ( #def-model-sufficiency) and $S_{\text{min}}$ is the minimum sufficiency for the agent to function effectively. Equivalently, the reconstruction error must not push sufficiency below the threshold:

$$\epsilon_{\text{recon}} \leq \epsilon_{\text{max}}(S_{\text{min}}, M_k^-)$$

where $\epsilon_{\text{max}}$ is the maximum tolerable reconstruction error — itself a function of the current sufficiency and the threshold.

### Externalization strategies

*[Discussion (externalization-strategies)]*

The externalization function $\text{ext}: \mathcal{M} \to \mathcal{E}_{\text{ext}}$ maps the end-of-session state to a persistent store. Several mechanisms exist, with different information-preservation properties:

| Mechanism | What it preserves | Information loss | AAD interpretation |
|---|---|---|---|
| **Raw conversation logs** | Full $\mathcal C_t$ (chronica) | None (if complete), but reconstruction requires re-processing | Preserves the input to $\phi$ ( #form-agent-model); sufficiency depends on reconstruction fidelity |
| **Structured summaries** | Compressed $M_t$: key beliefs, decisions, open questions | Lossy — detail, context, uncertainty estimates | Approximate $M_t$ with bounded error; quality depends on compression |
| **File-backed state** | Explicit state registers: current plan, known facts, unresolved issues | Lossy but structured — the agent chooses what to externalize | Designed compression; the agent acts as its own $\phi$ |
| **Retrieval-augmented memory** | Indexed chunks retrievable by semantic similarity | Reconstruction is query-dependent — different prompts retrieve different subsets | Sufficiency varies per query; $S(M_{k+1}^+)$ depends on the alignment between the retrieval query and the needed information |
| **Vector databases / embeddings** | Dense representations of prior context | Lossy; information encoded in geometric structure rather than explicit content | Approximate $M_t$ in a fixed-dimensional embedding; retrieval accuracy is bounded by the embedding's mutual information with $M_k^-$ |

### Reconstruction as information recovery

*[Discussion (reconstruction-information)]*

The reconstruction function $\text{recon}: (\mathcal{E}_{\text{ext}}, p_{k+1}, M_0^{\text{weights}}) \to M_{k+1}^+$ combines three information sources:

1. **External memory** $\mathcal{E}_{\text{ext}}$: what was explicitly preserved
2. **New prompt** $p_{k+1}$: what the user or system provides at session start
3. **Pretrained prior** $M_0^{\text{weights}}$: what the LLM already knows from training

The reconstructed sufficiency is bounded by:

$$S(M_{k+1}^+) \leq \min\left(1,\; S_{\text{ext}} + S_{\text{prompt}} + S_{\text{prior}} - S_{\text{overlap}}\right)$$

where $S_{\text{ext}}$ is the sufficiency recoverable from external memory alone, $S_{\text{prompt}}$ from the prompt, $S_{\text{prior}}$ from the pretrained weights, and $S_{\text{overlap}}$ corrects for redundancy between sources. This is an informal bound — the interaction between information sources is not additive in general — but it captures the structure: reconstruction quality depends on complementary information from multiple sources.

### The accumulation problem

*[Discussion (accumulation-across-sessions)]*

Over many sessions, reconstruction error can accumulate:

$$\epsilon_{\text{recon}}^{(n)} = \sum_{k=1}^{n} \Delta\epsilon_k$$

where $\Delta\epsilon_k$ is the net information loss at session boundary $k$. If the agent systematically loses information at each boundary ($\Delta\epsilon_k \gt 0$ on average), the effective $M_t$ degrades over time — a long-timescale drift in model quality that is invisible within any single session.

This is the inter-session analog of the persistence failure described in #result-persistence-condition: not $\alpha \lt \rho / R$ (correction rate inadequate) but cumulative information loss exceeding the rate at which new sessions provide useful information. The agent persists across sessions when:

$$\mathbb{E}[\Delta\epsilon_k] \leq \mathbb{E}[\Delta I_k]$$

where $\Delta I_k$ is the new information acquired in session $k$ that compensates for the reconstruction loss. An agent that learns less each session than it forgets at each boundary will experience long-timescale model degradation.

## Epistemic Status

*Discussion-grade.* The framing — inter-session persistence as reconstruction adequacy — is well-motivated and structurally sound, but the formal content is limited: the bounds are informal, the sufficiency decomposition is not additive in general, and the accumulation analysis is a qualitative sketch. The specific mechanisms (summaries, retrieval, file-backed state) are engineering descriptions, not theory. The connection to Section I's persistence condition is by analogy, not by derivation.

Max attainable: conditional. With a formal model of the externalization-reconstruction cycle (e.g., specifying the information geometry of the compression), the reconstruction adequacy condition could be made exact. The accumulation analysis could be formalized as a random walk on sufficiency, with conditions for convergence. Currently discussion-grade because the formalization is absent.

## Discussion

**The persistence condition's two faces.** For any LLM agent, persistence has two independent requirements:

1. **Intra-session**: $\alpha \gt \rho / R$ — the standard persistence condition. The agent's correction rate must outpace the mismatch injection rate within a session. This is about the adaptive dynamics of the coupled update.
2. **Inter-session**: $S(M_{k+1}^+) \geq S_{\text{min}}$ — the reconstruction adequacy condition. The externalized state must be recoverable with sufficient fidelity. This is about the information-preservation properties of the memory system.

An agent can satisfy one without the other: excellent intra-session dynamics with no memory system (high $\alpha$, zero inter-session persistence), or perfect memory with poor intra-session adaptation (perfect reconstruction, low $\alpha$).

**Design implications.** The reconstruction adequacy condition suggests specific engineering priorities:

- **Explicit state externalization** (file-backed state, structured summaries) is more reliable than implicit preservation (hoping retrieval will recover what is needed), because the agent controls what is preserved.
- **Redundancy across mechanisms** improves robustness — combining conversation logs, structured summaries, and retrieved context provides complementary information.
- **Session-start protocols** that verify reconstruction quality (the agent checks whether it "remembers" key facts from prior sessions) can detect inter-session degradation before it affects task performance.
- **The prompt-assembly function** ( #def-coupled-update-dynamics) is the reconstruction mechanism — its design determines $S(M_{k+1}^+)$.

**Connection to the logogenic orient cascade.** The first events in a new session serve a special function: they populate the context window with the information needed for the coupled update to produce adequate diagnostics. A session that begins with poor context reconstruction will produce unreliable $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ values, leading to incorrect strategic assessments. The reconstruction quality directly gates the diagnostic framework ( #result-coupled-diagnostic-framework).

**Biological analogy.** Sleep is the biological analog of the session boundary: the organism's working memory is cleared, and the persistent store (long-term memory) must reconstruct the context for the next day's cognition. The consolidation process during sleep — selective strengthening and pruning of memories — is the biological $\text{ext}(\cdot)$. The quality of morning cognition depends on the quality of overnight consolidation, not on the quality of the previous day's terminal cognitive state.

## Working Notes

- The accumulation analysis ($\mathbb{E}[\Delta\epsilon_k] \leq \mathbb{E}[\Delta I_k]$) is the most theoretically interesting claim here but the least developed. Formalizing it requires: (a) a model of how reconstruction error accumulates (is it additive? multiplicative? does it have absorbing states?), (b) a model of how new information in each session compensates for loss, and (c) conditions under which the sufficiency process is stationary, ergodic, or divergent.
- The treatment omits fine-tuning as a persistence mechanism. If the agent's weights are updated between sessions, information can persist in the weights rather than (or in addition to) external memory. This creates a third information source for reconstruction — but it is slow (requires training), coarse (cannot preserve specific contextual details), and introduces its own degradation risks (catastrophic forgetting). Worth a separate treatment if logogenic agent theory develops further.
- The retrieval-augmented memory mechanism deserves deeper analysis: the query-dependence of reconstruction means that $S(M_{k+1}^+)$ is not a single number but a function of the task. An agent starting a session on "fix the auth bug" retrieves different context than one starting on "add logging" — even if the external memory is identical. This is a form of goal-conditioned reconstruction, connecting back to the $\kappa_{\text{processing}}$ characterization.
