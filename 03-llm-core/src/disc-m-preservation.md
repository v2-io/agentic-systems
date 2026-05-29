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

| Mechanism | What it preserves | Information loss | AAT interpretation |
|---|---|---|---|
| **Raw conversation logs** | Full $\mathcal{C}_t$ (chronica) | None (if complete), but reconstruction requires re-processing | Preserves the input to $\phi$ ( #form-agent-model); sufficiency depends on reconstruction fidelity |
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

### Accumulation across sessions

The per-boundary adequacy condition, iterated across the sequence of session boundaries, has a definite dynamical form. The reconstruction map is a lossy stochastic channel, so the relevant epistemic content contracts *multiplicatively* at each boundary while fresh information is reinjected *additively* — an affine information recursion $I_{k+1} \leq \eta_k I_k + a_k$ on the relevant mutual information $I_k = I(M_k^+;Y)$ ( #der-turnover-information-recursion). The accumulation is not an additive error sum with a break-even threshold; the loss is multiplicative.

The consequence is sharp. With no reinjection the walk decays geometrically to zero — there is no inter-session analog of the rate-condition $\alpha \gt \rho/R$, and #result-sector-persistence-template does not transfer to the destroy-and-reconstruct regime. Persistence across sessions holds *iff* the reinjection channel is non-vanishing ($\liminf_k a_k \gt 0$), at level $\bar a/(1-\bar\eta)$ — reinjection over the contraction gap. Persistence is therefore not a property the composite possesses intrinsically: it is wholly imported through a non-vanishing reinjection channel, which structurally is the externalization layer this segment describes. An agent whose reinjection eventually vanishes experiences geometric model degradation regardless of how faithful any single reconstruction is. The full derivation, the argued modeling commitments, and the honest scope (the no-go is about *uniformly* lossy turnover) are in #der-turnover-information-recursion.

This is the accumulation question for *predictive sufficiency* — the survival of the working reality model toward future-observation adequacy ( #def-model-sufficiency), the target this segment is about. The parallel question for *identity continuity* — whether an entity's identity-relevant state survives turnover toward the identity-relevance vector of #def-identity-sufficiency — is a structurally distinct operator on a distinct target: a reflected, relationally-compensated walk on the identity gap with a load-bearing driftless ($\mu=0$) boundary, treated in #der-identity-continuity-threshold. The two operators sit at opposite ends of the same singular contraction parameter and neither supersedes the other; the predictive regime here is not a normalization of the identity regime, nor the converse.

## Epistemic Status

*Discussion-grade, except the accumulation dynamics.* The framing — inter-session persistence as reconstruction adequacy — is well-motivated and structurally sound; the per-source sufficiency bounds and the externalization-mechanism table are engineering descriptions, not theory, and the single-boundary reconstruction-adequacy condition is by analogy to Part I, not by derivation. The *accumulation across boundaries*, by contrast, is resolved exactly: it is the affine information recursion of #der-turnover-information-recursion, which derives the geometric no-go, the non-transfer of #result-sector-persistence-template, and the conditional-positive characterization (persistence iff non-vanishing reinjection). That dynamical core is *exact* within an argued structural commitment and is no longer discussion-grade.

Max attainable: the accumulation dynamics are at ceiling (exact, in #der-turnover-information-recursion). The remaining discussion-grade content — the multi-source sufficiency decomposition and the per-mechanism information-preservation descriptions — could be made conditional with a formal model of each externalization channel's information geometry; it is discussion-grade because that per-channel formalization is absent, not because the cross-boundary dynamics are.

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

- The predictive-sufficiency accumulation across boundaries is resolved in #der-turnover-information-recursion: the operator is multiplicative (SDPI contraction), the break-even additive form is the wrong shape for it, and persistence is imported iff reinjection is non-vanishing. The identity-continuity accumulation is the distinct reflected operator of #der-identity-continuity-threshold — not this regime under a normalization. *History (not present truth): this section previously carried a discussion-grade additive accumulation $\epsilon^{(n)}=\sum_k\Delta\epsilon_k$ with a break-even inequality $\mathbb{E}[\Delta\epsilon_k]\leq\mathbb{E}[\Delta I_k]$; that presumed the wrong (additive) operator for the predictive-sufficiency regime and was deleted and replaced when the contraction–reinjection no-go landed, 2026-05-19 — see CHANGELOG.* The genuinely-open follow-ons are named in that segment's Working Notes: the SDPI coefficient $\eta_k$ for the concrete $f_{\text{init}}$ kernel is uncomputed, and the adversarially-correlated-reinjection second no-go (re-grounding vanishing exactly as $I_k$ falls) is the named next spike (`spikes/continuity-persistence/` §4.2).
- The treatment omits fine-tuning as a persistence mechanism. If the agent's weights are updated between sessions, information can persist in the weights rather than (or in addition to) external memory. This creates a third information source for reconstruction — but it is slow (requires training), coarse (cannot preserve specific contextual details), and introduces its own degradation risks (catastrophic forgetting). Worth a separate treatment if logogenic agent theory develops further.
- The retrieval-augmented memory mechanism deserves deeper analysis: the query-dependence of reconstruction means that $S(M_{k+1}^+)$ is not a single number but a function of the task. An agent starting a session on "fix the auth bug" retrieves different context than one starting on "add logging" — even if the external memory is identical. This is a form of goal-conditioned reconstruction, connecting back to the $\kappa_{\text{processing}}$ characterization.
