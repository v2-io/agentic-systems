---
slug: context-turnover
type: observation
status: exact
depends:
  - ai-agent-as-act-agent
  - chronica
  - persistence-condition
  - model-sufficiency
stage: draft
---

# Observation: Context Turnover

At every session boundary, the LLM-based agent's context window is cleared. The chronica $\mathcal C_t$ is severed — no internal state carries over. This is a 100% $M_t$ reset: the agent begins each session with $M_t$ reconstructed entirely from external sources and the new prompt. The persistence condition, which assumes continuous or event-driven state evolution, does not apply in its standard form across session boundaries.

## Formal Expression

*[Observation (context-turnover)]*

Let $\tau_k$ and $\tau_{k+1}$ denote the start times of consecutive sessions. At the session boundary:

$$X_{\tau_{k+1}}^{\text{context}} = \emptyset$$

The agent's effective state at the start of session $k+1$ is reconstructed from external memory $\mathcal{E}_{\text{ext}}$ and the new prompt $p_{k+1}$:

$$X_{\tau_{k+1}} = f_{\text{init}}(\mathcal{E}_{\text{ext}}, p_{k+1}, M_0^{\text{weights}})$$

where:
- $\mathcal{E}_{\text{ext}}$ is the externally persisted information (files, databases, prior conversation summaries, structured memory stores)
- $p_{k+1}$ is the session-initiating prompt (user instruction, system prompt, retrieved context)
- $M_0^{\text{weights}}$ is the frozen pretrained prior (the LLM's weights)

*[Observation (chronica-severance)]*

The chronica ( #chronica) is severed at every session boundary. Within a session, $\mathcal C_t$ accumulates as the conversation history. Across sessions:

$$\mathcal C_{\tau_{k+1}} \neq \mathcal C_{\tau_k} \cup \{e_{\tau_k}, \ldots\}$$

The new session's chronica starts fresh. Any information from the prior session's chronica that is needed must have been *externalized* — written to $\mathcal{E}_{\text{ext}}$ — before the session boundary.

*[Observation (sufficiency-discontinuity)]*

Model sufficiency ( #model-sufficiency) is discontinuous at session boundaries:

$$S(M_{\tau_{k+1}}) = S(f_{\text{init}}(\mathcal{E}_{\text{ext}}, p_{k+1}, M_0^{\text{weights}}))$$

This is generically less than $S(M_{\tau_k^-})$ — the model sufficiency at the end of the prior session — because $f_{\text{init}}$ reconstructs $M_t$ from a lossy compression of the prior session's state. The sufficiency drop:

$$\Delta S_{\text{turnover}} = S(M_{\tau_k^-}) - S(M_{\tau_{k+1}})$$

is bounded below by the information lost in the externalization-reconstruction cycle:

$$\Delta S_{\text{turnover}} \geq 1 - \frac{I(M_{\tau_k^-};\, f_{\text{init}}(\mathcal{E}_{\text{ext}}, p_{k+1}, M_0^{\text{weights}}))}{H(M_{\tau_k^-})}$$

The numerator is the mutual information between the end-of-session state and the reconstructed state; the denominator normalizes by the entropy of the original state. When externalization captures everything relevant, $\Delta S_{\text{turnover}} \approx 0$. When nothing is externalized, $\Delta S_{\text{turnover}} \approx 1 - S(M_0^{\text{weights}})$ — the agent falls back to its pretrained prior.

## Epistemic Status

*Exact as an observation.* The 100% context reset at session boundaries is a structural fact of current LLM architectures, not an approximation. The sufficiency-discontinuity bound follows from information-theoretic definitions. What is *not* exact is the characterization of how much information is lost — that depends on the quality of $\mathcal{E}_{\text{ext}}$ and $f_{\text{init}}$, which are engineering choices.

Max attainable: exact. This is an observation about a structural property of the architecture.

## Discussion

**Qualitative difference from Section I persistence.** The persistence condition ( #persistence-condition) asks: "can the correction rate outpace the disturbance rate?" This assumes the state evolves continuously (or at least persists between events). For LLM agents, the intra-session dynamics follow this pattern — within a session, each tool result or message is an event that updates $X_t$ via the coupled dynamics. But the inter-session dynamics are qualitatively different: the state is not perturbed, it is *destroyed and reconstructed*. The relevant question is not $\alpha \gt \rho / R$ but whether the reconstruction is adequate:

$$S(f_{\text{init}}(\mathcal{E}_{\text{ext}}, p_{k+1}, M_0^{\text{weights}})) \geq S_{\text{min}}$$

where $S_{\text{min}}$ is the minimum model sufficiency required for the agent to function effectively in the new session. This is a reconstruction adequacy condition, not a rate condition.

**Two timescales of persistence.** LLM agent persistence operates at two timescales:
1. **Intra-session** (event-driven, continuous): standard ACT dynamics apply. The coupled update $X_{\tau^+} = f_{\text{LLM}}(\text{prompt}(X_{\tau^-}, e_\tau))$ ( #coupled-update-dynamics) processes events and evolves $X_t$. The persistence condition applies within a session.
2. **Inter-session** (episodic, discontinuous): the state is reconstructed from external memory. The persistence challenge is information preservation through the externalization-reconstruction cycle. See #m-preservation.

**Context window as finite $\mathcal C_t$ capacity.** Even within a session, the chronica is bounded by the context window length $L$. When $\lvert\mathcal C_t\rvert \gt L$, older events are dropped — a forced compression that degrades sufficiency. This creates an intra-session analog of the turnover problem: the agent must continuously prioritize which information to retain in its finite context. The rate of information loss from context-window overflow is an additional disturbance term in the intra-session mismatch dynamics.

**Implications for the orient cascade.** The 100% reset means the agent must re-establish its orient cascade from scratch each session. The epistemic state, strategic assessments, and diagnostic quantities ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$) must all be reconstructed. The first events in a new session are disproportionately important — they populate the context with the information needed for subsequent cascade steps.

## Working Notes

- The sufficiency-discontinuity bound is stated in information-theoretic terms. For practical measurement, proxies are needed: task completion rate across session boundaries, time-to-productive-action at session start, frequency of re-asking for already-provided information.
- The characterization of $f_{\text{init}}$ (what determines reconstruction quality) is deliberately left unformalized here. The mechanisms — retrieval-augmented generation, structured memory stores, conversation summaries — are engineering choices, not theory. See #m-preservation for the treatment.
- Fine-tuning changes the picture: if the weights are updated between sessions, $M_0^{\text{weights}}$ becomes $M_k^{\text{weights}}$, and some information from session $k$ persists in the weights. This is a partial mitigation of turnover, but the context-specific state ($G_t$, the current strategy, the working state of a multi-step task) is still lost.
