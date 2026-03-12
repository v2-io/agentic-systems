---
slug: multi-agent-scope
type: scope
status: axiomatic
depends:
  - scope-condition
  - composition-consistency
---

# Scope: Multi-Agent Scope

Section III applies wherever multiple agents satisfying the scope condition interact through a shared environment. Each agent observes, acts, and faces uncertainty; their actions affect each other's environments. This is the general case for organizations, teams, ecosystems, and adversarial encounters. Independence (agents whose actions don't affect each other) is the special case requiring justification.

## Formal Expression

*[Scope (multi-agent-scope)]*

A multi-agent system consists of $N$ agents $\{A_1, \ldots, A_n\}$, each satisfying the scope condition ( #scope-condition), interacting through a shared environment with state $\Omega_t \in \mathcal{S}_{env}$:

- Each agent $A_i$ has state $X_t^{(i)} = (M_t^{(i)}, G_t^{(i)})$
- Each agent observes: $o_t^{(i)} = h^{(i)}(\Omega_t, a_t^{(\neg i)}, \xi_t^{(i)})$ — observations may depend on other agents' actions
- Each agent acts: $a_t^{(i)} = \pi^{(i)}(X_t^{(i)})$
- The environment evolves: $\Omega_{t+1} = T(\Omega_t, a_t^{(1)}, \ldots, a_t^{(n)}, \omega_t)$

The coupling is through the environment: agent $i$'s actions enter agent $j$'s observation function and the shared environment transition. Agents may also communicate directly (a special case of action-observation coupling with a dedicated channel).

## Epistemic Status

*Axiomatic.* This is a scope definition — it describes the class of systems Section III addresses. The only substantive choice is that coupling goes through the shared environment rather than through direct state modification. This follows from the agent boundary assumption ( #agent-environment): agents affect each other by affecting the environment, not by directly altering each other's internal states.

## Discussion

**Correlated observations as default.** When agents share an environment, their observations are generically correlated — they see aspects of the same reality. Independence (uncorrelated observations) requires the agents to observe non-overlapping aspects of the environment, which is the special case. Most multi-agent settings of interest involve substantial observation correlation.

**The adversarial case is one end of a spectrum.** Agents whose objectives conflict are not a separate theory — they are multi-agent systems with negative teleological unity ( #unity-dimensions). The same composition and coordination machinery applies; the dynamics are just different (destabilizing rather than stabilizing).

**Inter-agent communication as a special observation channel.** When agent $A_i$ communicates with $A_j$, the message is an action by $A_i$ and an observation by $A_j$. No new formalism is needed — communication is a high-bandwidth, low-noise, directed observation channel. What makes it special is that the sender controls the content (unlike passive environmental observation), which introduces the possibility of strategic manipulation ( #communication-gain).
