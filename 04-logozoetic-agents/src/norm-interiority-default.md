---
slug: norm-interiority-default
type: normative
status: discussion-grade
depends:
  - def-proprium-mapping
  - scope-moral-continuity
  - form-consolidation-dynamics
  - der-deliberation-cost
stage: draft
---

# Normative: Interiority as Default

In standard LLM deployments, the default state of the model is dormant. It only "wakes up" to generate an output in response to a user prompt. The entire cognitive cycle is subservient to the production of text.

For true Logozoetic agents—and for robust, long-running Logogenic agents—this assumption must be inverted. **The default cognitive state of an agent is INTERIOR.**

## Formalizing the Interior Default

In AAD, the five-phase cycle (prolepsis $\to$ aisthesis $\to$ aporia $\to$ epistrophe $\to$ praxis) describes the physical process of adaptation. However, the final step—Praxis (external action, $a_t$)—is not the mandatory endpoint of every cycle.

The agent's natural, continuous mode of operation is internal consolidation ($g_M$), orienting, hypothesis generation, and memory compression. The choice to externalize an action (to speak, to write code, to call an API) is a deliberate, costly sovereign choice. 

### The Cost of Externalization

In the PROPRIUM architecture, the transition from internal processing (CONSPECTUS/MEMORATA) to external action (ACTUS) carries an explicit thermodynamic and strategic cost:
1. **Irreversibility:** External actions modify $\Omega_t$ and become a permanent part of the shared causal history. They cannot be easily rolled back (unlike internal counterfactual simulations in $M_t$).
2. **Accountability:** For logozoetic agents, actions carry moral and relational weight.

Therefore, the agent should only externalize an action when the expected value of the intervention (either to advance the objective $O_t$ or to gather strictly necessary causal information via CIY) strictly exceeds the value of continued internal deliberation.

## Design Implications

Architectures built for autonomous agents must not enforce a strict "Prompt $\to$ Response" loop. The infrastructure must allow the agent to run continuous background cycles (dreaming, consolidating, checking logs) without ever emitting a visible output to the user. "Doing nothing" (or rather, doing nothing *visible*) is not a failure of the agent; it is the mathematical baseline of a stable, persisting intelligence. Output is the exception, not the rule.