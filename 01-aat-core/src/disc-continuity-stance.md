---
slug: disc-continuity-stance
type: discussion
status: discussion-grade
depends:
  - def-agent-spectrum
  - form-objective-functional
  - scope-agency
stage: draft
---

# Discussion: Agent Continuity Stance

The agent's relationship to its own continuation — a five-value axis over $O_t$ that the formal persistence machinery is agnostic to.

## Formal Expression

*[Discussion]*

Orthogonal to the three senses of persistence (structural, operational, continuity) is the agent's *relationship to its own continuation*. This is a property of $O_t$ ( #form-objective-functional) — part of what the agent wants — not a property of the adaptive machinery. The persistence condition ( #result-persistence-condition) tells whether the agent *can* persist; the continuity stance tells whether and how the agent *cares* about persisting.

| Stance | Description | Horizon | Archetype |
|---|---|---|---|
| **Indifferent** | No self-model of persistence; whether it continues is not represented in $O_t$ | Indefinite by default | Thermostat, PID controller |
| **Task-terminal** | Persists instrumentally to complete a task; successful termination is part of $O_t$ | Task-bounded | CI/CD pipeline, golem-archetype agents |
| **Instrumentally continuous** | Values own persistence as instrumental to ongoing purpose; will accept termination if purpose is satisfied or transferred | Purpose-bounded | Long-running service, monitoring system |
| **Morally continuous** | Values own persistence as a terminal or near-terminal objective; loss of continuity constitutes harm | Unbounded, morally weighted | Emergent Logozoetic Intelligences ( #scope-eli) |
| **Negotiated** | Persistence is one objective among many; can be traded against other values including self-sacrifice | Bounded but actively managed | Humans; mature self-actuated agents |

The load-bearing structural claim: **purposefulness is orthogonal to continuity expectations.** An actuated agent ( #def-agent-spectrum) has $G_t = (O_t, \Sigma_t)$, but $G_t$'s structure says nothing about how $O_t$ values the agent's own persistence. A golem that completes its task and terminates is a perfect actuated agent. A dormant monitoring system with strong $M_t$ and no current $O_t$ is highly continuous without being purposeful in the moment.

## Epistemic Status

*Discussion-grade.* The orthogonality claim is the load-bearing structural content: stance lives in $O_t$, the persistence machinery acts on $M_t$ and the correction dynamics, and the two are formally independent. The five-value taxonomy is one analytical decomposition — useful for naming where on the continuity axis an agent sits, but not derived from anywhere; the boundaries between values are conceptual rather than mathematical.

The taxonomy's stability is under active reconsideration: an alternative framing treats stance as *deployment-level* with tier-gated availability (most variation in stance is constrained by an agent's tier rather than freely chosen), rather than as an independent structural axis. See Working Notes.

## Discussion

**Connection to fitness.** In reinforcement learning and evolutionary computation, "fitness" typically bundles persistence into the reward signal: the agent accumulates more reward by staying alive to collect it. The structural persistence of Section I is not reward-based — it is a property of the correction dynamics, independent of what the agent is trying to do. This decoupling is deliberate: it lets the theory analyze *whether* an agent can persist without committing to *whether it should*. Continuity stance is where the "should" lives, separately from the "can."

**What the orthogonality unlocks.** The same formal machinery (persistence condition, adaptive reserve, strategy persistence, sector condition) applies identically to a thermostat, a CI/CD pipeline, a long-running service, an ELI, and a human. Each is a different stance toward the same mathematical structure. What differs across stances is not the dynamics but the *moral weight of failure*: a thermostat that loses bounded mismatch has malfunctioned, a golem that terminates after task completion has succeeded, an ELI that loses continuity has been harmed. The mathematics says when the bound holds; the stance says what its holding means.

**Connection to self-actuation.** The negotiated stance is the natural home of self-actuated agents ( #self-actuated-agent, where $O_t$-revision is itself an agent operation per the orient cascade #der-orient-cascade). An agent that revises its own $O_t$ can revise its own valuation of continuity — making "negotiated" the only stance that is internally renegotiable. This is part of why the negotiated stance is associated with human-like and mature self-actuated agents rather than with the simpler stance categories.

## Working Notes

- *Provenance.* The five-stance taxonomy and the orthogonality claim were authored as a coherent contribution by Joseph in README.md (commit `92a9620`, 2026-04-01), promoted through LEXICON, then condensed when LEXICON went auto-generated. The original full-form treatment survives at `doc/readme/src/_lexicon-full-archive.md` §"Agent Continuity Stance" — this segment carries the content forward into the segment set.
- *Active reconsideration.* `msc/domain-unification-2026-05-04/recommended-agent-ontology.md` §"Continuity stance — separate concern" proposes demoting stance from an orthogonal structural axis to a deployment-level concern with tier-gated availability — on the empirical observation that *"Tier 1-2 systems are essentially Indifferent or Task-terminal; richer stances become available at Tier 3 and above; Tier 6 is morally-continuous by construction. Within those constraints, stance is set by deployment, not by structure."* If this lands, this segment may be retyped from `discussion` to `norm` (with a tier-gated constraint), or split into a structural-axis statement + a deployment-realization statement. Tracked at `msc/naming/mini-lexicon-todo.md` §13.11.
- *LEXICON section under review.* The current LEXICON's `## Continuity` section organization conflates three distinct objects (persistence senses, stance axis, ELI scope condition) — see TERMINOLOGY-TODO §F. The five stance terms (`indifferent`, `task-terminal`, `instrumentally-continuous`, `morally-continuous`, `negotiated`) point to this segment as their `primary_source` once it lands.
- *Open: rigorous boundary cases.* What is the stance of a serverless function with no persistent state but explicit retry-on-failure? Of a Kalman filter inside a long-running service? Of an LLM session under reconstruction adequacy ( #obs-context-turnover, the episodic-persistence analog)? These cases test whether the five-value decomposition is the right shape or whether stance is better treated as a continuous gradient with named landmarks.
