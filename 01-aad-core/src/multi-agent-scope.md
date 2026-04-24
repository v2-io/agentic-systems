---
slug: multi-agent-scope
type: scope
status: axiomatic
depends:
  - scope-agency
  - postulate-composition-consistency
stage: draft
---

# Scope: Multi-Agent Scope

Section III applies wherever multiple agents satisfying the scope condition interact through a shared environment. Each agent observes, acts, and faces uncertainty; their actions affect each other's environments. This is the general case for organizations, teams, ecosystems, and adversarial encounters. Independence (agents whose actions don't affect each other) is the special case requiring justification.

## Formal Expression

*[Scope (multi-agent-scope)]*

A multi-agent system consists of $N$ agents $\{A_1, \ldots, A_n\}$, each satisfying the scope condition ( #scope-agency), interacting through a shared environment with state $\Omega_t \in \mathcal{S}_{env}$:

- Each agent $A_i$ has state $X_t^{(i)} = (M_t^{(i)}, G_t^{(i)})$
- Each agent observes: $o_t^{(i)} = h^{(i)}(\Omega_t, a_t^{(\neg i)}, \xi_t^{(i)})$ — observations may depend on other agents' actions
- Each agent acts: $a_t^{(i)} = \pi^{(i)}(X_t^{(i)})$
- The environment evolves: $\Omega_{t+1} = T(\Omega_t, a_t^{(1)}, \ldots, a_t^{(n)}, \omega_t)$

The coupling is through the environment: agent $i$'s actions enter agent $j$'s observation function and the shared environment transition. Agents may also communicate directly (a special case of action-observation coupling with a dedicated channel).

### Observation decomposition and routing

*[Definition (observation-decomposition)]*

Each agent's observation decomposes into environmental and inter-agent components:

$$o_t^{(i)} = \left(o_{\text{env},t}^{(i)},\; \{m_{ji,t}\}_{j \in \mathcal N_t(i)}\right)$$

where:
- $o_{\text{env},t}^{(i)} = h_\text{env}^{(i)}(\Omega_t, \xi_t^{(i)})$: direct environmental observation (no inter-agent content)
- $\mathcal N_t(i) \subseteq \{1, \ldots, N\} \setminus \{i\}$: the **communication neighborhood** — which agents send messages to $i$ at time $t$
- $m_{ji,t} = c_t^{(j \to i)}(X_t^{(j)})$: message from $j$ to $i$, determined by the sender's full state and the communication protocol

*[Definition (routing-structure)]*

The **routing structure** $R_t = (\mathcal N_t, \{c_t^{(j \to i)}\})$ specifies:
- The **topology** $\mathcal N_t$: who communicates with whom
- The **protocol** $c_t^{(j \to i)}$: the rule governing what class of information flows from $j$ to $i$

Note: the protocol $c_t^{(j \to i)}$ is a *rule* specifying the channel, not the specific content of any message. Individual messages reflect the sender's state $X_t^{(j)}$ — including their individual goals — through the sender's policy. What the routing structure governs is the *infrastructure*: which channels exist and what kind of information they carry.

*[Definition (goal-blind-routing)]*

Routing is **goal-blind** when neither the topology nor the protocol depends on the composite's goal state:

$$\mathcal N_t \perp G_t^c \qquad \text{and} \qquad c_t^{(j \to i)} \perp G_t^c \quad \forall\, j, i$$

This means the communication infrastructure does not change based on what the composite is trying to achieve. Individual messages naturally reflect individual agents' goals through their policies — this is action, not routing. The routing condition is about the *structure* of information flow, not the *content* of individual messages.

**Goal-dependent routing** occurs when either the topology or the protocol varies with $G_t^c$. Examples: activating crisis-specific communication channels, changing intelligence-sharing protocols based on the current mission, reassigning reporting chains based on the operational objective.

## Epistemic Status

*Axiomatic.* This is a scope definition — it describes the class of systems Section III addresses. The only substantive choice is that coupling goes through the shared environment rather than through direct state modification. This follows from the agent boundary assumption ( #agent-environment): agents affect each other by affecting the environment, not by directly altering each other's internal states.

## Discussion

**Correlated observations as default.** When agents share an environment, their observations are generically correlated — they see aspects of the same reality. Independence (uncorrelated observations) requires the agents to observe non-overlapping aspects of the environment, which is the special case. Most multi-agent settings of interest involve substantial observation correlation.

**The adversarial case is one end of a spectrum — but not a composite.** Agents whose objectives conflict are multi-agent systems with negative teleological unity ( #unity-dimensions) and thus do not satisfy #scope-composite-agent: the absence of shared purpose means no composite agent exists. Two distinct classes of machinery apply across this spectrum:

- **Agent-level machinery** (individual persistence, agent tempo, per-agent mismatch, sector-condition stability) applies to *every* agent in *every* multi-agent configuration — cooperative, adversarial, or indifferent — because each agent individually satisfies #scope-agency and Section I/II results apply directly. The adversarial tempo advantage ( #adversarial-tempo-advantage) and adversarial destabilization ( #adversarial-destabilization) results are applications of this agent-level machinery to the case where one agent's actions are a disturbance source for another.

- **Composite-level machinery** (closure defect, team persistence, composite tempo, unity-closure rate-distortion) applies *only* when #scope-composite-agent is satisfied — i.e., when the sub-agents' alignment is sufficient to define a coherent composite purpose. Adversarial pairs are *excluded* from this scope.

The adversarial regime sits at the negative-$U_O$ end of the unity spectrum. Its dynamics are captured using agent-level machinery applied across the pair, not by treating the adversarial pair as a composite. The existing adversarial segments ( #adversarial-destabilization, #adversarial-tempo-advantage) correctly operate at the agent-level; the scope distinction makes explicit what those segments have always done implicitly.

**Inter-agent communication as a special observation channel.** Messages from $j$ to $i$ are actions by $j$ and observations by $i$. The routing structure formalizes the infrastructure: who talks to whom ($\mathcal N_t$) and under what protocol ($c_t^{(j \to i)}$). The sender controls the content (unlike passive environmental observation), which introduces strategic manipulation ( #communication-gain). The gain from inter-agent communication enters the distributed tempo ( #communication-gain, Working Notes).

**The routing/content distinction matters for directed separation.** Individual messages reflect senders' goals — that's just action through policy. The directed-separation question at the composite level ( #directed-separation-under-composition) is about the *routing structure*: does the infrastructure change based on the composite's goals? Goal-blind routing preserves directed separation; goal-dependent routing breaks it.
