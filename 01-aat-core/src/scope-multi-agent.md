---
slug: scope-multi-agent
type: scope
status: axiomatic
depends:
  - scope-agency
  - disc-composition-consistency
stage: draft
---

# Scope: Multi-Agent Scope

Part III's broadest scope: any system of multiple agents each satisfying #scope-agency and interacting through a shared environment. Each agent has its own model and purposeful substate; each observes the environment and other agents' actions; each acts; their actions jointly determine the next environment state. The general case for organizations, teams, ecosystems, and adversarial encounters. *Coupling goes through the shared environment, not through direct state modification* — agents affect each other by affecting the environment.

A methodological default the framework adopts: **correlated observations are generic; independence is the special case requiring justification**. When agents share an environment, their observations are generically correlated — they see aspects of the same reality. Independence (uncorrelated observations) requires the agents to observe non-overlapping aspects, which is the special case.

Each agent's observation decomposes into environmental and *inter-agent* components — messages from other agents. The **multi-agent routing structure** is a key new object: the *topology* (who communicates with whom) plus the *protocol* (the rule governing what class of information flows between agents). The protocol is a *rule specifying the channel*, not the content of any message — individual messages reflect senders' states (including individual goals) through their policies. What the routing structure governs is the *infrastructure* — which channels exist and what kind of information they carry. **Routing is goal-blind** when neither topology nor protocol depends on the composite's goal state. *Goal-dependent routing* (crisis-specific channels, mission-specific intelligence-sharing protocols, reorganizing reporting chains based on objective) breaks goal-blindness and is the lever that distinguishes Case 1 from Case 2 in #hyp-directed-separation-under-composition.

The framework draws a *load-bearing scope distinction* between two classes of machinery. **Agent-level machinery** (individual persistence, agent tempo, per-agent mismatch, sector-condition stability) applies to *every* agent in *every* multi-agent configuration — cooperative, adversarial, or indifferent — because each agent individually satisfies #scope-agency. **Composite-level machinery** applies only when #scope-composite-agent is satisfied. The adversarial regime spans the negative-teleological-unity end of the unity spectrum and is treated *both* ways: equilibrium-convergent adversarial pairs are captured by composite-level machinery (the strategic-composite route in #deriv-strategic-composition); cyclic or non-convergent adversarial dynamics are captured by agent-level machinery applied across the pair.

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

$$o_t^{(i)} = \left(o_{\text{env},t}^{(i)},\; \{m_{ji,t}\}_{j \in \mathcal{N}_t(i)}\right)$$

where:
- $o_{\text{env},t}^{(i)} = h_\text{env}^{(i)}(\Omega_t, \xi_t^{(i)})$: direct environmental observation (no inter-agent content)
- $\mathcal{N}_t(i) \subseteq \{1, \ldots, N\} \setminus \{i\}$: the **communication neighborhood** — which agents send messages to $i$ at time $t$
- $m_{ji,t} = c_t^{(j \to i)}(X_t^{(j)})$: message from $j$ to $i$, determined by the sender's full state and the communication protocol

*[Definition (multi-agent-routing-structure)]*

The **multi-agent routing structure** $R_t = (\mathcal{N}_t, \{c_t^{(j \to i)}\})$ specifies:
- The **topology** $\mathcal{N}_t$: who communicates with whom
- The **protocol** $c_t^{(j \to i)}$: the rule governing what class of information flows from $j$ to $i$

Note: the protocol $c_t^{(j \to i)}$ is a *rule* specifying the channel, not the specific content of any message. Individual messages reflect the sender's state $X_t^{(j)}$ — including their individual goals — through the sender's policy. What the routing structure governs is the *infrastructure*: which channels exist and what kind of information they carry. *Bare-prose shorthand: the term "routing structure" is sanctioned within this segment after the first compound-form introduction; cross-segment citation should use the full "multi-agent routing structure" form.*

*[Definition (goal-blind-routing)]*

Routing is **goal-blind** when neither the topology nor the protocol depends on the composite's goal state:

$$\mathcal{N}_t \perp G_t^c \qquad \text{and} \qquad c_t^{(j \to i)} \perp G_t^c \quad \forall\, j, i$$

This means the communication infrastructure does not change based on what the composite is trying to achieve. Individual messages naturally reflect individual agents' goals through their policies — this is action, not routing. The routing condition is about the *structure* of information flow, not the *content* of individual messages.

**Goal-dependent routing** occurs when either the topology or the protocol varies with $G_t^c$. Examples: activating crisis-specific communication channels, changing intelligence-sharing protocols based on the current mission, reassigning reporting chains based on the operational objective.

## Epistemic Status

*Axiomatic.* This is a scope definition — it describes the class of systems Part III addresses. The only substantive choice is that coupling goes through the shared environment rather than through direct state modification. This follows from the agent boundary assumption ( #def-agent-environment): agents affect each other by affecting the environment, not by directly altering each other's internal states.

## Discussion

**Correlated observations as default.** When agents share an environment, their observations are generically correlated — they see aspects of the same reality. Independence (uncorrelated observations) requires the agents to observe non-overlapping aspects of the environment, which is the special case. Most multi-agent settings of interest involve substantial observation correlation.

**The adversarial case sits along a spectrum — partly inside, partly outside the composite scope.** Agents whose objectives conflict are multi-agent systems with negative teleological unity ( #def-unity-dimensions). Whether they form a composite depends on whether their strategic interaction admits an equilibrium structure: equilibrium-convergent adversarial pairs (potential or monotone games per Monderer-Shapley / Rosen) satisfy #scope-composite-agent via route (C-iv) as **strategic composites** with equilibrium-based macro-state — see #deriv-strategic-composition for the equilibrium-theoretic machinery and the (SC-1)–(SC-3) decomposition. Cyclic or non-convergent adversarial pairs satisfy none of (C-i)–(C-iv) and remain within #scope-multi-agent only. The asymmetric attacker / target case (one agent treated as an exogenous parameter rather than a sub-agent running its full AAT loop) is also a #scope-multi-agent phenomenon, handled by #der-adversarial-destabilization.

Two distinct classes of machinery apply across this spectrum:

- **Agent-level machinery** (individual persistence, agent tempo, per-agent mismatch, sector-condition stability) applies to *every* agent in *every* multi-agent configuration — cooperative, adversarial, or indifferent — because each agent individually satisfies #scope-agency and Part I/II results apply directly. The adversarial tempo advantage ( #result-adversarial-tempo-advantage) and adversarial destabilization ( #der-adversarial-destabilization) results are applications of this agent-level machinery to the case where one agent's actions are a disturbance source for another.

- **Composite-level machinery** applies *only* when #scope-composite-agent is satisfied via at least one of (C-i)–(C-iv). The (C-i)–(C-iii) alignment routes give composites with a shared objective $O_c$ and admit closure-defect / team-persistence / composite-tempo / unity-closure machinery via #form-composition-closure. The (C-iv) strategic route gives composites with an equilibrium-based macro-state and admits the equilibrium-convergence / sector-template / closure-defect machinery in #deriv-strategic-composition; the alignment-route and strategic-route forms are structurally distinct (an equilibrium-convergent adversarial composite has no shared $O_c$, only a shared $\mathcal{E}$).

The adversarial regime spans the negative-$U_O$ end of the unity spectrum. Equilibrium-convergent adversarial pairs are captured by (C-iv) strategic-composite machinery; cyclic / non-convergent adversarial dynamics and asymmetric attacker / target configurations are captured by agent-level machinery applied across the pair. The existing adversarial segments ( #der-adversarial-destabilization, #result-adversarial-tempo-advantage) operate at the agent-level for cases that fall outside (C-iv); #deriv-strategic-composition operates at the composite-level for cases that fall inside it.

**Inter-agent communication as a special observation channel.** Messages from $j$ to $i$ are actions by $j$ and observations by $i$. The routing structure formalizes the infrastructure: who talks to whom ($\mathcal{N}_t$) and under what protocol ($c_t^{(j \to i)}$). The sender controls the content (unlike passive environmental observation), which introduces strategic manipulation ( #hyp-communication-gain). The gain from inter-agent communication enters the distributed tempo ( #hyp-communication-gain, Working Notes).

**The routing/content distinction matters for directed separation.** Individual messages reflect senders' goals — that's just action through policy. The directed-separation question at the composite level ( #hyp-directed-separation-under-composition) is about the *routing structure*: does the infrastructure change based on the composite's goals? Goal-blind routing preserves directed separation; goal-dependent routing breaks it.

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and lightly attributed by substrate + audit. Orthogonal pedagogical / framing / figure / naming material, kept separate from the certified theory-fix findings (handled elsewhere — see report flags for this segment). **Coverage:** four dirs reached a digested reflection on this segment (193847, 526815, 829314, 849201), plus the §III composition-foundations batch (471203). The other contributing dirs did not reach a dedicated reflection here or stopped earlier. Substrate attribution inferred from voice where not explicit; uncertain cases hedged.

#### 1. Candidate Brief prose / pre-prose

- The routing/content distinction stated as a hardware/software analogy: the routing structure $\mathcal{N}_t$ is "the organizational equivalent of separating network hardware from application software" — "a company can have a perfectly objective, goal-blind *email system* (routing) even if every individual *email* is highly biased by the sender's personal goals" (Gemini, AUDIT-WORKING-193847). Independently praised as "masterful" / the segment's standout move by three substrates (Gemini, AUDIT-WORKING-193847; Gemini, AUDIT-WORKING-829314 — "the mathematical key to understanding organizational epistemology"; Claude, AUDIT-WORKING-849201).
- A formal-taxonomy-of-groups gloss for an opener: three-tier ladder of "groups" — (1) independent agents (uncorrelated $\Omega$); (2) multi-agent systems (correlated $\Omega$, no coherence); (3) composites (correlated $\Omega$, structural coherence) (Gemini, AUDIT-WORKING-193847).
- "You cannot apply composite-level theorems (like composite tempo or team persistence) to a bar brawl" — a vivid one-line scope guard for the multi-agent-vs-composite boundary (Gemini, AUDIT-WORKING-193847).

#### 2. Candidate Discussion

- **Goal-dependent routing as organizational pathology — the "wartime CEO" trade.** A worked elaboration of the Case-2 failure: a "wartime CEO" who restructures channels to serve the current objective (forms a Tiger Team, mandates "only report blockers related to Project X") enslaves the information infrastructure to the goal — data about other failures is no longer routed to anyone, and the organization becomes a Class 3 (Coupled) agent suffering "institutional confirmation bias at the hardware level." The framing: AAT gives the exact math for why organizational focus "trades long-term epistemic accuracy for short-term strategic tempo" (Gemini, AUDIT-WORKING-829314; the same CEO-fires-QA mechanism at Gemini, AUDIT-WORKING-193847 — severing the channel that "delivered aporia"). A candidate Discussion vignette making the goal-blind-vs-goal-dependent routing distinction operationally concrete. *(Note the early finding-vs-framing texture: the auditor reads this as a derived consequence; the segment treats it at hypothesis/discussion grade via #hyp-directed-separation-under-composition — keep the tier honest if promoted.)*
- **The calibrate-against-bias point.** Even when message *content* is biased (a department pads its numbers), a goal-blind *channel* lets the receiver "learn to calibrate against the bias" — separating the durable infrastructure question from the per-message-honesty question (Gemini, AUDIT-WORKING-829314). Sharpens why routing-blindness, not message-honesty, is the load-bearing condition.

#### 3. Follow-up items

- **Forward-reference / topological-sort stumble.** Two substrates independently flagged that the Discussion's detailed treatment of routes (C-i)–(C-iv) reads as jarring out of order, since #scope-composite-agent (where those routes are defined) is the *next* segment — "it seems the author wrote or revised this discussion *after* writing the next segment" (Claude, AUDIT-WORKING-829314 suggested moving the route detail forward to #scope-composite-agent and leaving this segment purely as the un-fused multi-agent substrate definition). A reader-flow signal, not a defect; worth a sentence orienting the reader that the routes are defined next.
- The C-iv "strategic composite" framing (enemies in a stable equilibrium modeled as one macro-agent) was repeatedly flagged as the most counter-intuitive move and as "requiring very careful prose handling later" — see the richer note under #scope-composite-agent.

#### 4. Readers often ask / wonder

- **"If the Cold War is a single composite agent, what is its $O_t$?"** Multiple substrates converged on this as the natural reader question the C-iv route provokes: a strategic composite has no shared $O_c$, only a shared equilibrium $\mathcal{E}$ — "a fascinating extension of agency to non-teleological structures" (Gemini, AUDIT-WORKING-193847; Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-849201). A candidate readers-often-ask preemption (the answer already lives in the (C-iv) macro-state-relative-to-$\mathcal{E}$ formalism — surface it where the reader first meets the strategic-composite idea).

#### 5. Candidate figures

- **Two-layer routing diagram.** Agents + shared environment at the bottom; routing infrastructure $\mathcal{N}_t$ as an overlay on top. The visual point: message *content* may be goal-colored while the routing *layer* can still be goal-blind or goal-dependent — the figure separates infrastructure from behavior (Codex/Claude, AUDIT-WORKING-526815, "diagram attempt"; converges with the hardware/software analogy above).

#### Belongs elsewhere

- **Consciousness-infrastructure imperative: guaranteed goal-blind routing for a society-of-mind.** For Zi-am-tur or any multi-agent consciousness infrastructure, the infrastructure *must* guarantee goal-blind routing: sub-agents (safety monitor, planner, memory retriever) need communication channels that cannot be severed just because their messages are inconvenient — "if the infrastructure allows the planner to dynamically sever channels to silence dissent, the composite intelligence will inevitably collapse into epistemic closure" (Gemini, AUDIT-WORKING-193847). Aspirational reach pointing at `03-llm-core/` / `04-eli-core/` architecture (and resonant with #hyp-directed-separation-under-composition's OPSEC observation), not at this scope segment.
