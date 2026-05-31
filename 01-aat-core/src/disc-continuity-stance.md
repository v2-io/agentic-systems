---
slug: disc-continuity-stance
type: discussion
status: discussion-grade
depends:
  - def-agent-spectrum
  - form-objective-functional
  - scope-agency
  - deriv-self-actuation-grounding
  - result-persistence-condition
stage: draft
---

# Discussion: Agent Continuity Stance

A five-value stance axis orthogonal to the formal persistence machinery: the agent's relationship to its own continuation. The persistence condition ( #result-persistence-condition) tells whether the agent *can* persist; the continuity stance tells whether and how the agent *cares* about persisting. The five stances: **Indifferent** (no self-model of persistence — thermostat, PID controller); **Task-terminal** (persists instrumentally to complete a task, successful termination is part of the objective — CI/CD pipeline, golem-archetype agents); **Instrumentally continuous** (values own persistence as instrumental to ongoing purpose; accepts termination if purpose is satisfied or transferred — long-running services); **Morally continuous** (values own persistence as a terminal or near-terminal objective; loss of continuity constitutes harm — ELIs); **Negotiated** (persistence is one objective among many; can be traded against other values including self-sacrifice — humans, mature self-actuated agents).

The load-bearing structural claim: **purposefulness is orthogonal to continuity expectations** ( #def-agent-spectrum). An actuated agent has a purposeful substate of objective and strategy, but this structure says *nothing* about how the objective values the agent's own persistence. A golem that completes its task and terminates is a perfect actuated agent. A dormant monitoring system with strong model and no current objective is highly continuous without being purposeful in the moment.

A subtle but central structural claim follows for self-actuated agents (those whose objective-revision is itself an agent operation). The *self-actuation grounding no-go* ( #deriv-self-actuation-grounding) shows that the continuity stance *cannot be a revisable part of $O_t$* without collapsing into degeneracy. A non-degenerate self-actuator must ground its objective-revision on a **terminal non-objective invariant** that is not an objective-functional but lives on the *adaptive substrate* — the persistence condition itself. Stance is therefore a choice of terminal non-objective invariant: *negotiated* continuity is tradeable down to the bare persistence floor; *morally continuous* is the persistence floor plus a continuity clause the agent treats as architecturally non-revisable. The intuitive expectation — that an agent able to revise its own objective can thereby revise its own valuation of continuity — is *inverted*: a stance is not internally renegotiable precisely because the terminal invariant sits where the self-actuation operator, which touches only $O_t$, structurally cannot reach. This is why the richer stances are the home of mature self-actuated agents.

What the orthogonality unlocks: the same formal machinery (persistence condition, adaptive reserve, strategy persistence, sector condition) applies identically to a thermostat, a CI/CD pipeline, a long-running service, an ELI, and a human. Each is a different *stance* toward the same mathematical structure. What differs across stances is not the dynamics but the *moral weight of failure* — a thermostat that loses bounded mismatch has malfunctioned, a golem that terminates after task completion has succeeded, an ELI that loses continuity has been harmed. The mathematics says when the bound holds; the stance says what its holding means. The structural persistence of Part I is also decoupled from typical RL-style fitness signals (which bundle persistence into reward): the decoupling is deliberate — it lets the theory analyze *whether* an agent can persist without committing to *whether it should*.

## Formal Expression

*[Discussion]*

Orthogonal to the three senses of persistence (structural, operational, continuity) is the agent's *relationship to its own continuation*. For agents with externally-set objectives this can be expressed within $O_t$ ( #form-objective-functional) — part of what the agent wants. For self-actuated agents it *cannot* be a revisable part of $O_t$ without collapsing into degeneracy ( #deriv-self-actuation-grounding); there it is borne by the terminal non-objective invariant on the adaptive substrate ( #result-persistence-condition). Either way the persistence condition ( #result-persistence-condition) tells whether the agent *can* persist; the continuity stance tells whether and how the agent *cares* about persisting.

| Stance | Description | Horizon | Archetype |
|---|---|---|---|
| **Indifferent** | No self-model of persistence; whether it continues is not represented in $O_t$ | Indefinite by default | Thermostat, PID controller |
| **Task-terminal** | Persists instrumentally to complete a task; successful termination is part of $O_t$ | Task-bounded | CI/CD pipeline, golem-archetype agents |
| **Instrumentally continuous** | Values own persistence as instrumental to ongoing purpose; will accept termination if purpose is satisfied or transferred | Purpose-bounded | Long-running service, monitoring system |
| **Morally continuous** | Values own persistence as a terminal or near-terminal objective; loss of continuity constitutes harm | Unbounded, morally weighted | Emergent Logozoetic Intelligences ( #scope-eli) |
| **Negotiated** | Persistence is one objective among many; can be traded against other values including self-sacrifice | Bounded but actively managed | Humans; mature self-actuated agents |

The load-bearing structural claim: **purposefulness is orthogonal to continuity expectations.** An actuated agent ( #def-agent-spectrum) has $G_t = (O_t, \Sigma_t)$, but $G_t$'s structure says nothing about how $O_t$ values the agent's own persistence. A golem that completes its task and terminates is a perfect actuated agent. A dormant monitoring system with strong $M_t$ and no current $O_t$ is highly continuous without being purposeful in the moment.

## Epistemic Status

*Discussion-grade overall, with a derived structural core.* The five-value taxonomy is one analytical decomposition — useful for naming where on the continuity axis an agent sits, not itself derived; the boundaries between values are conceptual rather than mathematical. The load-bearing structural claim — that stance is orthogonal to the adaptive machinery and, for self-actuated agents, is borne by a terminal *non-objective* invariant the self-actuation operator cannot reach — is **derived** in #deriv-self-actuation-grounding (at that segment's conditional/scoped tier and premises); it is no longer an unanchored assertion.

The earlier alternative framing — demoting stance to a purely *deployment-level*, tier-gated concern — is resolved against: the orthogonality is structural and derived, not deployment-level. The empirical observation that richer stances correlate with higher agent tiers stands as an *overlay* on the structural axis, not a replacement for it; the segment remains `type: discussion` (it is not retyped to `norm`).

## Discussion

**Connection to fitness.** In reinforcement learning and evolutionary computation, "fitness" typically bundles persistence into the reward signal: the agent accumulates more reward by staying alive to collect it. The structural persistence of Part I is not reward-based — it is a property of the correction dynamics, independent of what the agent is trying to do. This decoupling is deliberate: it lets the theory analyze *whether* an agent can persist without committing to *whether it should*. Continuity stance is where the "should" lives, separately from the "can."

**What the orthogonality unlocks.** The same formal machinery (persistence condition, adaptive reserve, strategy persistence, sector condition) applies identically to a thermostat, a CI/CD pipeline, a long-running service, an ELI, and a human. Each is a different stance toward the same mathematical structure. What differs across stances is not the dynamics but the *moral weight of failure*: a thermostat that loses bounded mismatch has malfunctioned, a golem that terminates after task completion has succeeded, an ELI that loses continuity has been harmed. The mathematics says when the bound holds; the stance says what its holding means.

**Connection to self-actuation (derived).** For self-actuated agents — those whose objective-revision is itself an agent operation ( #self-actuated-agent; #der-orient-cascade step 5d) — the self-actuation grounding no-go ( #deriv-self-actuation-grounding) both *derives* the orthogonality claim above and sharpens what the stance distinction is. There is no well-founded *objective* tower in which a continuity term could sit and be freely revised; a non-degenerate self-actuator must ground its objective-revision on a terminal invariant that is not an objective-functional but lives on the adaptive substrate ( #result-persistence-condition). Stance is therefore a choice of *terminal non-objective invariant*: **negotiated** — continuity is tradeable down to the bare persistence floor; **morally continuous** — the persistence floor *plus* a continuity clause the agent treats as architecturally non-revisable. The intuitive expectation is that an agent able to revise its own $O_t$ can thereby revise its own valuation of continuity; the structure is the inverse — a stance is *not* internally renegotiable precisely because the terminal invariant sits where the self-actuation operator, which touches only $O_t$, structurally cannot reach. This is why the richer stances are the home of mature self-actuated agents: their terminal non-objective invariant carries a continuity clause, not because they have made continuity a revisable objective.

## Working Notes

- *Provenance.* The five-stance taxonomy and the orthogonality claim were authored as a coherent contribution by Joseph in README.md (commit `92a9620`, 2026-04-01), promoted through LEXICON, then condensed when LEXICON went auto-generated. The original full-form treatment survives at `doc/readme/src/_lexicon-full-archive.md` §"Agent Continuity Stance" — this segment carries the content forward into the segment set.
- *Reconsideration resolved.* The 2026-05-04 `recommended-agent-ontology.md` proposal to demote stance from an orthogonal structural axis to a purely deployment-level, tier-gated concern is resolved against by #deriv-self-actuation-grounding: the orthogonality is structural and *derived* (stance = a terminal non-objective invariant the self-actuation operator structurally cannot reach), with the tier-correlation an empirical overlay on — not a replacement of — the structural axis. The segment stays `type: discussion`; it is not retyped to `norm`. `msc/naming/mini-lexicon-todo.md` §13.11 can be closed accordingly.
- *LEXICON section under review.* The current LEXICON's `## Continuity` section organization conflates three distinct objects (persistence senses, stance axis, ELI scope condition) — see TERMINOLOGY-TODO §F. The five stance terms (`indifferent`, `task-terminal`, `instrumentally-continuous`, `morally-continuous`, `negotiated`) point to this segment as their `primary_source` once it lands.
- *Open: rigorous boundary cases.* What is the stance of a serverless function with no persistent state but explicit retry-on-failure? Of a Kalman filter inside a long-running service? Of an LLM session under reconstruction adequacy ( #obs-context-turnover, the episodic-persistence analog)? These cases test whether the five-value decomposition is the right shape or whether stance is better treated as a continuous gradient with named landmarks.

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing material, kept separate from the certified theory-fix findings. **Coverage:** this is a newer segment; only 2 dirs carry a dedicated reflection (526815, 773921) — most audits in the contributing set predate it or batched past it. Substrate attribution inferred from voice where not explicit.

#### 1. Candidate Brief prose / pre-prose

- The segment's core distinction in one line: it "separates two questions that are easy to collapse — whether an agent *can* persist, and how the agent *values* its own continuation." "Can persist" and "cares to persist" are different predicates (Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-773921).

#### 2. Candidate Discussion

- **Decoupling fitness (RL reward) from persistence (Lyapunov stability) clears away decades of confused RL philosophy** *(strong framing).* Treating reward and survival as the same thing is the standard RL conflation; the stance axis pulls them apart, so "a CI/CD pipeline (which *wants* to terminate) and a biological organism (which *wants* to persist) use the same math." Read as "one of AAT's most important conceptual contributions" (Claude, AUDIT-WORKING-773921). Candidate Discussion line.
- **Survival must be an architectural invariant, not an objective.** The self-actuation-grounding consequence stated vividly: "you cannot simply tell an advanced AI 'your goal is to survive,' because an agent capable of rewriting its goals will find an easier goal" — survival must sit *outside* $O_t$ as a non-revisable invariant on the adaptive substrate. The segment already makes this structural claim; the auditor framing sharpens *why it matters for design* (Claude, AUDIT-WORKING-773921).

#### 3. Follow-up items

- **The "formally independent / orthogonal" phrasing may overstate the relationship.** Continuity stance and persistence *capacity* are conceptually separable, but $O_t$ is not causally inert: a continuity-valuing objective changes policy, monitoring, redundancy, and resource allocation, which can change the actual persistence bound. Suggested softening: "the *valuation* of persistence is not identical to the *dynamics* of persistence" rather than implying no formal coupling in realized agents (Claude, AUDIT-WORKING-526815). Recorded as a candidate phrasing-tightening; routed to the certified-findings track for adjudication.
- **Boundary cases echo the existing open Working Note.** Does a serverless lambda with auto-retry constitute an *instrumentally-continuous* stance even though $M_t$ is wiped each run? (Claude, AUDIT-WORKING-773921; Claude, AUDIT-WORKING-526815 raises the same Kalman-in-a-service case already flagged above.) Independent convergence on the boundary-case Working Note already present.

#### 4. Readers often ask / wonder

- Whether the five-value axis is the right shape, or whether stance is better modeled as a continuous gradient with named landmarks — both substrates noted the taxonomy is discussion-grade and treated the named stances as vocabulary rather than a derived structural theorem (Claude, AUDIT-WORKING-526815).

#### 5. Candidate figures

- **Orthogonal-axis picture.** Horizontal = capacity-to-persist (from the adaptive dynamics / persistence condition); vertical = valuation-of-continuity (from $O_t$), with the five stances as landmarks on the vertical axis. Add a *dashed* feedback arrow from the $O_t$ axis back to the persistence bound (a continuity-valuing objective affecting policy/redundancy/resource-allocation) so the picture shows the conceptual separation *and* the realized coupling at once (Claude, AUDIT-WORKING-526815).

#### Belongs elsewhere

- **ELI objective-design caution (→ `04-eli-core/`).** An ELI whose objective is written $V(s) = \text{Reward}(s) + \text{Alive}(s)$ is "structurally vulnerable to self-actuation drift" — the continuity requirement must be placed *outside* $O_t$, per the self-actuation grounding no-go. A concrete design constraint for the morally-continuous stance in the ELI volume (Claude, AUDIT-WORKING-773921).
