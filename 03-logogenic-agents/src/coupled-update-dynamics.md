---
slug: coupled-update-dynamics
type: definition
status: robust-qualitative
depends:
  - scope-logogenic-agent
  - complete-agent-state
  - recursive-update
  - directed-separation
  - event-driven-dynamics
stage: draft
---

# Definition: Coupled Update Dynamics

For Class 2 (fully merged) agents, the factored update — $M_t$ first, then $G_t$ — is replaced by a single coupled update on the full state. The LLM's forward pass, given a prompt assembled from the prior state and a new event, produces a response that simultaneously encodes updated beliefs and strategic assessments. This is the starting formulation for logogenic agent theory: rather than dropping directed separation as an approximation, we begin without it.

## Formal Expression

*[Definition (coupled-update)]*

The coupled update for an LLM-based agent:

$$X_{\tau^+} = f_{\text{LLM}}(\text{prompt}(X_{\tau^-}, e_\tau))$$

where:
- $X_{\tau^-} = (M_{\tau^-}, G_{\tau^-})$ is the agent state just before event $e_\tau$ (the current context window contents)
- $\text{prompt}: \mathcal{X} \times \mathcal{E} \to \mathcal{P}$ is the **prompt-assembly function** that constructs a token sequence from the prior state and the new event
- $f_{\text{LLM}}: \mathcal{P} \to \mathcal{X}$ is the **forward pass** — the transformer's autoregressive generation, mapping a prompt to a response that constitutes the updated state
- $X_{\tau^+} = (M_{\tau^+}, G_{\tau^+})$ is the post-event state, extractable from the response by functional decomposition

**Contrast with the factored update** ( #directed-separation):

| Property | Factored (Class 1) | Coupled (Class 2) |
|---|---|---|
| Update structure | $M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$, then $G_{\tau^+} = f_G(G_{\tau^-}, M_{\tau^+}, e_\tau)$ | $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ as a single computation |
| Information flow | Unidirectional: $M \to G$ | Bidirectional: $M \leftrightarrow G$ within the forward pass |
| Goal influence on beliefs | None (by construction) | Full ($\kappa_{\text{processing}} \approx 1$) |
| Orient cascade | Sequential, derived from information dependency | Simultaneous; ordering as design pattern, not derived result |

*[Definition (prompt-assembly)]*

The prompt-assembly function $\text{prompt}(X_{\tau^-}, e_\tau)$ constructs the input token sequence. Its structure determines which information is available to the forward pass:

$$\text{prompt}(X_{\tau^-}, e_\tau) = [\text{sys}(O_t), \; \text{mem}(\mathcal{E}_{\text{ext}}), \; \text{hist}(\mathcal C_{\tau^-}), \; \text{event}(e_\tau)]$$

where:
- $\text{sys}(O_t)$ encodes the objective (system prompt, task description) — places $G_t$ causally upstream of all subsequent processing
- $\text{mem}(\mathcal{E}_{\text{ext}})$ provides retrieved context from external memory
- $\text{hist}(\mathcal C_{\tau^-})$ is the conversation history (chronica) within the current session
- $\text{event}(e_\tau)$ is the new observation (tool result, user message, etc.)

The ordering within the prompt matters: tokens placed earlier are causally upstream in the attention pattern. The system prompt (carrying $O_t$) appearing first is the *mechanism* by which goal-conditioning enters every subsequent computation — it is why $\kappa_{\text{processing}} \approx 1$ for transformer architectures.

*[Definition (response-decomposition)]*

The forward pass produces a response $r_\tau = f_{\text{LLM}}(\text{prompt})$. The response is functionally decomposable:

$$r_\tau = (r_\tau^M, r_\tau^G, r_\tau^a)$$

where:
- $r_\tau^M$ is the epistemic content: updated beliefs about reality expressed in the response (analysis of code, interpretation of errors, assessment of system state)
- $r_\tau^G$ is the purposeful content: strategic assessments, plan updates, feasibility evaluations
- $r_\tau^a$ is the action content: tool invocations, messages, code edits

This decomposition is *post-hoc and analytical*, not a description of the forward pass's internal structure. The forward pass does not compute $r_\tau^M$, $r_\tau^G$, and $r_\tau^a$ separately — it generates tokens that interleave all three. The decomposition is the analyst's tool for extracting diagnostic quantities from the coupled output. See #coupled-diagnostic-framework.

## Epistemic Status

*Robust qualitative.* The coupled formulation $X_{\tau^+} = f_{\text{LLM}}(\text{prompt}(X_{\tau^-}, e_\tau))$ is an exact description of the LLM's computation at the functional level. What is approximate is the identification of $X_t = (M_t, G_t)$ within the context window — the boundary between epistemic and purposeful content is not sharp, because the forward pass entangles them. The prompt-assembly structure is a representational choice that reflects current LLM system design, not a theoretical necessity.

Max attainable: robust-qualitative. The formulation describes a concrete class of architectures. A different architecture (e.g., one with explicit state registers) would require a different formulation. The coupled-vs-factored distinction is exact (it follows from the architectural classification in #directed-separation), but the specific form of $f_{\text{LLM}}$ and $\text{prompt}(\cdot)$ is a modeling choice.

## Discussion

**What is preserved from AAD.** The coupled formulation preserves:

1. **The state decomposition** $X_t = (M_t, G_t)$ as a coordinate system — the analyst can still identify epistemic and purposeful content, even though the agent's processing does not respect the boundary
2. **The event-driven structure** ( #event-driven-dynamics) — the agent updates its state in response to discrete events, with the forward pass as the update mechanism
3. **The recursive structure** ( #recursive-update) — each state depends on the prior state and the new event, enabling all of AAD's recursive-update machinery
4. **The policy structure** — $a_t = \pi(X_t)$ is implemented by the action content of the response

**What changes.** The coupled formulation changes:

1. **No sequential cascade** — the orient cascade ( #orient-cascade) does not hold as a derived result. The information dependency ($M_t$ feeds into $G_t$ evaluation) still exists logically, but is not enforced by the processing architecture. See #section-ii-survival for which cascade results survive.
2. **Goal-conditioned epistemic state** — $M_{\tau^+}$ reflects the goals in the prompt. The agent's beliefs about code, for instance, are shaped by what it is trying to do with the code. This is the formal content of $\kappa_{\text{processing}} \approx 1$.
3. **Diagnostics are post-hoc** — the satisfaction gap, control regret, and strategic calibration are computed *after* the coupled update, from the response, not during sequential processing. See #coupled-diagnostic-framework.

**Chain-of-thought as approximate cascade.** When the LLM generates a chain-of-thought reasoning trace, the token-by-token generation process can approximate the sequential cascade: early tokens address "what happened?" (epistemic), middle tokens address "what does this mean for my plan?" (strategic), and late tokens address "what should I do?" (action). This approximation is shaped by training, not by architecture — there is no guarantee the LLM follows this ordering, and highly goal-relevant observations may disrupt it (the agent jumps to strategic conclusions before adequately processing the evidence). The quality of the cascade approximation is a behavioral property, not an architectural one.

**System-level factorization.** While the LLM component is Class 2, the agent *system* can introduce partial factorization through design: a separate retrieval module that processes documents without goal-conditioning, an external monitor that observes the $(S, A, S')$ stream independently, or a memory system that stores observations without strategic filtering. These system-level design choices can reduce the effective $\kappa_{\text{processing}}$ of the overall system below that of the LLM component alone.

## Working Notes

- The prompt-assembly function $\text{prompt}(\cdot)$ is where most engineering decisions live: what to retrieve, what context to include, how to format the objective, how much history to retain. These choices determine the effective $X_{\tau^-}$ available to the forward pass and hence the quality of the update. A theory of prompt engineering is, in AAD terms, a theory of the $\text{prompt}(\cdot)$ function's effect on update quality.
- The response-decomposition $(r_\tau^M, r_\tau^G, r_\tau^a)$ is not always clean. A single sentence ("This test failure means our auth fix broke the session handler, so we need to revert") simultaneously updates beliefs, evaluates strategy, and implies an action. The decomposition is for analytical purposes; no claim that it is computable in general.
- The between-event dynamics noted in #complete-agent-state ("$\dot{G} = g_G(G, M)$ allows autonomous purposeful evolution during deliberation") have a logogenic analog: the LLM's autoregressive generation, where each token generation is a micro-event that can shift the state. A long reasoning trace is a sequence of micro-events within a single macro-event (the tool result or user message that triggered the response).
