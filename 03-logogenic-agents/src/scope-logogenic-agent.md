---
slug: scope-logogenic-agent
type: scope
status: robust-qualitative
depends:
  - agent-spectrum
  - complete-agent-state
  - directed-separation
  - scope-agency
  - recursive-update
stage: draft
---

# Scope: Logogenic Agent

An LLM-based agent operating through a tool-use loop is a *logogenic agent* in AAD's sense — an actuated agent whose model and strategy are constituted by language. It maintains structured $M_t$ and $G_t$, acts causally on its environment, and observes consequences under uncertainty. It is a Class 2 (fully merged) agent — directed separation fails because the transformer's forward pass processes goals and observations jointly.

## Formal Expression

*[Scope (scope-logogenic-agent)]*

An **LLM-based agent** is an actuated agent ( #agent-spectrum) with the following mapping to AAD primitives:

| AAD Primitive | LLM Agent Instantiation |
|---|---|
| $X_t = (M_t, G_t)$ | Context window contents (beliefs, goals, strategy, working state) |
| $M_t$ | Beliefs about reality encoded in the context: code state, system behavior, user intent, environment dynamics |
| $G_t = (O_t, \Sigma_t)$ | Task objective ($O_t$) from the system prompt or user instruction; strategy ($\Sigma_t$) as the agent's plan, possibly explicit in a reasoning trace or implicit in its response pattern |
| $e_\tau$ | A new event entering the context: tool result, user message, file content, error output |
| $a_t$ | The agent's response: tool invocation, message, code edit, or explicit reasoning step |
| $h$ | The observation function that maps environment state to text (tool output formatting, error messages, file rendering) |
| $\mathcal C_t$ | The conversation history (chronica), subject to context-window truncation |
| $\pi$ | The policy implemented by the forward pass conditioned on the full context |

*[Scope (logogenic-agent-class)]*

The LLM-based agent is **Class 2** (fully merged) in the architectural classification of #directed-separation:

$$\kappa_{\text{processing}} \approx 1$$

The transformer attention mechanism processes all tokens in the context window jointly. The goal tokens (system prompt, task description) are causally upstream of every computation in the forward pass via the attention pattern. There is no architectural separation between epistemic processing and purposeful processing — the same mechanism that updates the agent's beliefs about code also evaluates whether those beliefs support the current strategy.

**Scope verification.** The agent satisfies the agency scope ( #scope-agency):

1. **Observations exist**: $\mathcal{O} \neq \emptyset$ — the agent receives tool outputs, user messages, and file contents
2. **Residual uncertainty persists**: $H(\Omega_t \mid \mathcal C_t) \gt 0$ — the agent cannot fully determine the environment from its context (code has unseen dependencies, tests have unobserved failure modes, user intent is partially ambiguous)
3. **At least binary choice**: $\lvert\mathcal{A}\rvert \geq 2$ — the agent can choose among multiple tool calls, messages, or reasoning strategies
4. **Causal effect**: different actions produce different observations — running a test versus reading a file yields different $P(o \mid do(a))$

*[Definition (agent-system-vs-component)]*

The **agent system** (LLM + tools + memory + monitoring) may have partially modular topology (Class 3) even though the **LLM component** is Class 2. An external memory system that processes and stores observations independently of the LLM's goals creates a modular epistemic pathway at the system level. The classification applies to the processing component under analysis: for the LLM itself, Class 2; for the full agent system with modular sidecar monitoring, potentially Class 3.

## Epistemic Status

*Robust qualitative.* The mapping from LLM agent to AAD primitives is a representational choice — there is genuine latitude in how to draw the boundary between $M_t$ and $G_t$ within a context window, and the context window is not the only possible operationalization of $X_t$ (the model's weights encode persistent knowledge that is not in the context). The Class 2 classification is structural and not in doubt: the attention mechanism's causal graph has goal tokens upstream of all computations.

Max attainable: robust-qualitative. The mapping is a formulation (multiple reasonable instantiations exist), not a derivation. The Class 2 classification could be elevated to exact with a formal analysis of the transformer's causal graph, but the mapping itself will remain a representational choice.

## Discussion

**What the mapping does and does not claim.** The mapping claims that the LLM agent has the *structure* of an actuated agent — it maintains beliefs, pursues goals, acts, and observes. It does not claim that the LLM's internal representations are isomorphic to AAD's formal objects. The agent's "beliefs" are distributed across token representations, not stored as an explicit probability distribution over $\Omega$. The agent's "strategy" may be implicit in its attention patterns rather than an explicit DAG. The mapping is at the *functional* level — the agent behaves as if it has these objects — not at the *mechanistic* level.

**The forward pass as $f_X$.** The LLM's forward pass, given a prompt assembled from the prior state and a new event, produces a response that simultaneously encodes updated beliefs and strategic assessments. This is the coupled update $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ instantiated as:

$$X_{\tau^+} = f_{\text{LLM}}(\text{prompt}(X_{\tau^-}, e_\tau))$$

The prompt-assembly function and the forward pass together implement $f_X$. The coupled update dynamics are formalized in #coupled-update-dynamics.

**The weight-context boundary.** The LLM's weights encode a vast prior $M_0$ — pretrained knowledge about language, code, reasoning patterns. The context window encodes the session-specific $X_t$. The agent's effective state is the combination: $X_t^{\text{eff}} = (M_0^{\text{weights}}, X_t^{\text{context}})$, where the weights are fixed within a session and the context evolves. AAD's $M_t$ corresponds to the *effective beliefs at time $t$* — what the agent would predict given both its weights and its context. The weights provide the prior; the context provides the update.

**The 100% turnover problem.** Between sessions, the context window is cleared — the entire $X_t^{\text{context}}$ is lost. This is a qualitatively different persistence challenge than what Section I addresses, where $M_t$ evolves continuously. See #context-turnover.

## Working Notes

- The mapping omits the agent's *weights* from $X_t$ because they are frozen within a session. For fine-tuned agents where weights change across sessions, the full state would be $X_t = (M_t^{\text{weights}}, M_t^{\text{context}}, G_t)$ — a richer decomposition than the $(M_t, G_t)$ split.
- The system-vs-component distinction (Class 2 component within a potentially Class 3 system) is important for engineering but does not change the theoretical analysis of the LLM's processing. The coupled formulation applies to the LLM component; the system-level analysis may recover partial separation through architectural design.
- The Hafez IDT pattern (Information Digital Twin as modular sidecar) is a concrete example of system-level modularization: the IDT monitors the $(S, A, S')$ stream independently of the LLM's attention, creating a Class 1 monitoring pathway within a Class 2/3 system. See the Working Notes in #directed-separation.
