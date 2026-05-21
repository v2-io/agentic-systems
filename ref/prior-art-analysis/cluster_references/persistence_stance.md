# Cluster Reference: Continuity Stance and AI Welfare

**Overview:** Separates the 'Continuity Stance' from purposeful objectives, proving that the cybernetic persistence bounds apply universally, providing a rigorous grounding for AI identity and welfare over continuous revision.

---

## Canonical Source Segments

### Source: `def-agent-spectrum.md`

```yaml
---
slug: def-agent-spectrum
type: definition
status: axiomatic
depends:
  - def-agent-environment
  - form-agent-model
stage: deps-verified
---
```


# Definition: The Agent Spectrum

Two independent dimensions — model richness and objective richness — create a spectrum from reactive systems through purposeful agents. These are regions of a continuum, not discrete categories.

## Formal Expression

*[Definition (agent-spectrum)]*

Two dimensions — model richness and objective richness — define four regions of a continuum:

| | Objective absent or trivial | Objective structured |
|---|---|---|
| **Model absent or trivial** | *Reactive system*: fixed input-output rule (reflex arc, hardwired relay) | *Blind seeker*: pursues goal without modeling reality (gradient follower, basic search) |
| **Model structured** | *Adaptive tracker*: builds reality model, no goal beyond tracking (Kalman filter, Bayesian learner) | *Actuated agent*: models reality AND pursues objectives (commander, developer, AI agent) |

The regions differ in which state objects carry nontrivial structure:
- Reactive: $M_t$ and $O_t$ both absent or too degenerate for the associated machinery to be non-vacuous
- Adaptive tracker: $M_t$ structured — Section I's machinery fully describes these agents
- Blind seeker: $O_t$ structured, $M_t$ absent or degenerate — has a clear target but no predictive model
- Actuated agent: $(M_t, O_t)$ both structured, possibly with $\Sigma_t$ — the full scope of AAT

## Epistemic Status

This is *definitional* — it names regions of a continuum for analytical convenience. The regions are not ontological categories; agents migrate between them. A PID controller with auto-tuning is moving from blind seeker toward actuated agent. An RL agent in pure exploration is temporarily an adaptive tracker.

## Discussion

**The continuum, not categories.** Both axes are spectra: model richness ranges from no retained state, through error-integral-derivative, through full world models. Objective richness ranges from no preference, through scalar setpoints, through explicit multi-objective strategies. The 2×2 table names idealized regions; real agents populate the space between them.

**Moore machines as the simplest spectrum instantiation.** Miller (2022, *Ex Machina*) uses finite-state automata (Moore machines) as model organisms for studying adaptive social behavior. A one-state Moore machine occupies the reactive region — it produces a fixed output regardless of input, cannot condition behavior on observations, and is incapable of social behavior in any game-theoretic setting. A two-state machine makes a quantum leap into the adaptive tracker / blind seeker boundary — it can branch, remember one bit of history, and implement strategies like Tit-For-Tat. Miller's central empirical finding is that this one-state → two-state threshold is the critical computational boundary for social behavior: no game, no payoff structure, and no amount of interaction can produce cooperation, coordination, or exchange with one-state machines. The two-state machine is the minimal AAT agent. See #worked-example-cam (planned) for the full AAT ↔ Moore machine mapping.

**Low-end agents sit near region boundaries.** A thermostat has degenerate forms of both $M_t$ (last temperature reading — no history, no prediction) and $O_t$ (setpoint). It sits near the origin of both axes — closest to the reactive region but not truly absent on either axis. A PID controller has a richer error signal ($M_t$: error, integral, derivative) and a clear setpoint ($O_t$) — it's a blind seeker with a degenerate model, not a system with no model at all. A reflex arc (no retained state, no setpoint) is the truly reactive case. The meaningful classification question is not "does $M_t$ exist?" but "is $M_t$ rich enough to support the adaptive dynamics of Section I?"

**Section I covers the left column.** Adaptive trackers are the primary subject of Section I — agents that build and maintain $M_t$ without explicit purpose. The mismatch signal ( #def-mismatch-signal), gain ( #emp-update-gain), tempo ( #def-adaptive-tempo), and persistence condition ( #result-persistence-condition) characterize their adaptive dynamics. Section I operates within the adaptive scope ( #scope-adaptive-system) — observations and uncertainty are sufficient. Passive trackers, including passive Bayesian learners with no action choices, are fully within Section I's scope.

**Section II adds the right column.** Actuated agents need everything from Section I plus objectives, strategy, and the orient cascade that connects them. The adaptive machinery from Section I applies to the epistemic substate $M_t$ directly. When directed separation ( #der-directed-separation) holds — when the epistemic update is goal-blind — the Section I → Section II lift is clean and the orient cascade resolves sequentially.

**"Actuated" terminology.** The top-right quadrant is labeled "actuated agent" rather than "purposeful agent" to maintain a mechanical, formal register. "Purposeful" and "goal-oriented" are fine in natural language; "actuated" is the formal term. "Self-actuated" denotes agents that set their own objectives, as distinct from agents with externally supplied objectives; the self-actuation operator and its grounding no-go are formalized in #deriv-self-actuation-grounding.

**Relationship to Hafez et al. (2026).** Hafez defines a two-level hierarchy: *agency* (choice + effect + predictive asymmetry) and *intelligence* (agency + learning + self-monitoring + adaptation). This cuts the agent space along a different axis than AAT's model-richness × objective-richness table. Hafez's "agency" maps roughly to AAT's scope condition ( #scope-agency) — an entity whose actions affect outcomes in a measurable way. Hafez's "intelligence" maps to the full Section I + II machinery (learning = #der-recursive-update, self-monitoring = persistence diagnostics, adaptation = #result-structural-adaptation-necessity). The key operational difference: Hafez's bi-predictability metric $P = \text{MI}(S,A; S') / C$ characterizes the *information structure* of the agent-environment coupling, while AAT's tempo $\mathcal{T}$ characterizes the *corrective capacity* within that coupling. Bridge simulations confirm $P$ increases monotonically with $\mathcal{T}$, but $P$ is scale-invariant (blind to absolute mismatch magnitude) while $\mathcal{T}$ is not. They measure complementary aspects: $P$ characterizes the architecture, $\mathcal{T}$ characterizes the performance. See `spikes/track-b-nonlinear-sims/variants/variant_hafez_results.md` for the empirical bridge.

**Actuation does not presuppose a continuity stance.** An actuated agent has $G_t = (O_t, \Sigma_t)$ — it models reality and pursues objectives — but this says nothing about its relationship to its own continuation. The continuity-stance axis spans five values: *indifferent* (no self-model of persistence; thermostat / PID), *task-terminal* (persistence instrumental to task completion; golem / CI/CD pipeline), *instrumentally continuous* (persistence serves ongoing purpose; long-running service), *morally continuous* (persistence as terminal or near-terminal objective; Emergent Logozoetic Intelligences), and *negotiated* (persistence traded against other values; humans, mature self-actuated agents). The middle three are paradigmatically actuated; indifferent agents are typically reactive ( #scope-adaptive-system without agency), and negotiated agents are typically self-actuated. The theory's formal machinery (persistence condition, adaptive reserve, strategy persistence) applies identically across all stances; what differs is the moral significance of persistence failure, not the mathematics. See #disc-continuity-stance for the taxonomy and the orthogonality argument.

## Working Notes

- **Candidate reframe of the two axes (pedagogical — not a theorem change).** The Formal Expression names the axes *model richness* and *objective richness*. A more legible framing under consideration replaces these with **grounding** — the veracity of $M_t$ against reality, which is exactly $\delta_t$ ( #def-mismatch-signal) — and **intent** — how far the intended future is allowed to depart from the grounded present, and how varied/revisable that intended set is. The motivation is purely pedagogical: the richness framing does not make legible *why directed separation* ( #der-directed-separation) *turns out to be load-bearing for so many downstream results* — the reframe does, and that "why" is the thing the spectrum is supposed to teach.

  The anchor is #form-objective-functional: in its concrete forms $O_t$ is a point or region in the *same state space* $M_t$ represents, with $V_{O_t}(\tau) = -\lVert s_T - r \rVert$ a distance in that shared space. So there are three world-state representations — reality $s$ (not directly accessible), $M_t$ (believed: where the world is or will be), $O_t$ (intended: where it should end up) — and three gaps between them: $M_t$ vs $s$ (the veracity gap $= \delta_t$); $O_t$ vs now (the is$\to$ought displacement); believed-future vs $O_t$ (the satisfaction gap, #def-satisfaction-gap). Agency operates only in the third gap, and directed separation is the law that this gap may be closed *through the world* (via $\pi \to a_t$) and never by sliding $M_t$ toward $O_t$. Belief-about-reality and intended-reality are the *same kind of object in the same space* — "$99\%$ the same" — so the cheap way to shrink the satisfaction gap is to edit the map instead of the territory. Wishful thinking is then not a bolted-on pathology but the **default collapse of two near-identical representations**, and directed separation is precisely the architectural commitment that holds them apart. This answers the otherwise-opaque "why would the *degree of coupling* between goals and updates determine so much?": the two coupled things are nearly the same thing, and the entire content of agency is the protected $1\%$. You must have an expected, actively-pursued different future to accomplish anything with fidelity — but it cannot detach you from current reality without consequence.

- **Truthification reading.** Grounding is the agent's *truthfulness about reality*; directed separation, stated this way, is "do not let what you want corrupt what you believe is true." The $1\%$ where agency lives is the same $1\%$ where self-deception becomes possible. This is the ground-level (single-agent, base-case) statement of the M4 middle operation — strategic self-coupling as a self-driven modularity *decrease* — cross-referenced at #disc-modularity-state-dynamics (forward reference; the M4 segment is not yet landed).

- **Temporal subtlety — what is load-bearing vs. a restatement.** A tempting sharpening: the arrow of time *is* the separator — $f_M$ can only condition on evidence timestamped $\leq t$, so anything future-stamped is automatically goal-side and outside the epistemic update. **Stated as a separation criterion this does not hold.** #def-mismatch-signal requires a forward prediction $\hat o_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ that is future-stamped and *purely epistemic* (a Kalman predict-step or a weather forecast carries no goal content). The time-index is a *necessary* condition on the **origin of evidence** — belief cannot update on data that has not yet happened — not a *sufficient* criterion separating epistemic from goal content. Recorded explicitly so a future agent does not re-attempt "arrow-of-time as the $M_t / O_t$ separator" without the $\hat o_t$ counterexample. The actual separator is **evidence-conditioned vs. preference/intervention-conditioned** — the is/ought restatement of the existing scope condition (separation is about the *processing* of events, not their selection): the predictive future (world under its own dynamics or the currently-committed policy, conditioned on evidence) is epistemic; the *intended* future (a target, not a prediction) and the *counterfactual-under-candidate-action* futures (strategy rollouts) are goal/strategy-side.

- **The one genuinely-new thread: where the dangerous coupling concentrates.** The sharp, not-yet-explicit observation inside the temporal chain is that the $G_t \to f_M$ leakage concentrates not at the future boundary but in the **inference about the *unobserved present*** — the gap-filling about the unseen parts of the current world. That is the only step in $f_M$ with a free prior, hence the only place a goal-contaminated prior becomes motivated *perception*; future projections inherit corruption from there but are not its origin. The theory currently localizes the *whether* of leakage architecturally (Class 1/2/3 processing topology, #der-directed-separation) and touches the *phenomenon* (def-mismatch-signal's zero-aporia case (b), "confirmation bias"; der-directed-separation scope-condition clause 2, "no confirmation bias baked into $f_M$"), but it does not state this *where-in-the-inference* localization as such. Worth tracking as a candidate finer-grained companion to the architectural classification ("the latent-present prior is the leakage locus") — a possible sharpening of #der-directed-separation's scope condition — not folded silently and not yet promoted. Honest status: the macro reframe is pedagogy (no theorem changes; belongs in the framing layer per respectful pedagogy once vetted); of the temporal granularization, everything but the latent-present localization is a restatement of the recursive-update / scope-condition structure already in the theory.


---

### Source: `disc-continuity-stance.md`

```yaml
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
```


# Discussion: Agent Continuity Stance

The agent's relationship to its own continuation — a five-value stance axis the formal persistence machinery is agnostic to; for self-actuated agents it is borne by a terminal non-objective invariant on the adaptive substrate, not by $O_t$ ( #deriv-self-actuation-grounding).

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

**Connection to fitness.** In reinforcement learning and evolutionary computation, "fitness" typically bundles persistence into the reward signal: the agent accumulates more reward by staying alive to collect it. The structural persistence of Section I is not reward-based — it is a property of the correction dynamics, independent of what the agent is trying to do. This decoupling is deliberate: it lets the theory analyze *whether* an agent can persist without committing to *whether it should*. Continuity stance is where the "should" lives, separately from the "can."

**What the orthogonality unlocks.** The same formal machinery (persistence condition, adaptive reserve, strategy persistence, sector condition) applies identically to a thermostat, a CI/CD pipeline, a long-running service, an ELI, and a human. Each is a different stance toward the same mathematical structure. What differs across stances is not the dynamics but the *moral weight of failure*: a thermostat that loses bounded mismatch has malfunctioned, a golem that terminates after task completion has succeeded, an ELI that loses continuity has been harmed. The mathematics says when the bound holds; the stance says what its holding means.

**Connection to self-actuation (derived).** For self-actuated agents — those whose objective-revision is itself an agent operation ( #self-actuated-agent; #der-orient-cascade step 5d) — the self-actuation grounding no-go ( #deriv-self-actuation-grounding) both *derives* the orthogonality claim above and sharpens what the stance distinction is. There is no well-founded *objective* tower in which a continuity term could sit and be freely revised; a non-degenerate self-actuator must ground its objective-revision on a terminal invariant that is not an objective-functional but lives on the adaptive substrate ( #result-persistence-condition). Stance is therefore a choice of *terminal non-objective invariant*: **negotiated** — continuity is tradeable down to the bare persistence floor; **morally continuous** — the persistence floor *plus* a continuity clause the agent treats as architecturally non-revisable. The intuitive expectation is that an agent able to revise its own $O_t$ can thereby revise its own valuation of continuity; the structure is the inverse — a stance is *not* internally renegotiable precisely because the terminal invariant sits where the self-actuation operator, which touches only $O_t$, structurally cannot reach. This is why the richer stances are the home of mature self-actuated agents: their terminal non-objective invariant carries a continuity clause, not because they have made continuity a revisable objective.

## Working Notes

- *Provenance.* The five-stance taxonomy and the orthogonality claim were authored as a coherent contribution by Joseph in README.md (commit `92a9620`, 2026-04-01), promoted through LEXICON, then condensed when LEXICON went auto-generated. The original full-form treatment survives at `doc/readme/src/_lexicon-full-archive.md` §"Agent Continuity Stance" — this segment carries the content forward into the segment set.
- *Reconsideration resolved.* The 2026-05-04 `recommended-agent-ontology.md` proposal to demote stance from an orthogonal structural axis to a purely deployment-level, tier-gated concern is resolved against by #deriv-self-actuation-grounding: the orthogonality is structural and *derived* (stance = a terminal non-objective invariant the self-actuation operator structurally cannot reach), with the tier-correlation an empirical overlay on — not a replacement of — the structural axis. The segment stays `type: discussion`; it is not retyped to `norm`. `msc/naming/mini-lexicon-todo.md` §13.11 can be closed accordingly.
- *LEXICON section under review.* The current LEXICON's `## Continuity` section organization conflates three distinct objects (persistence senses, stance axis, ELI scope condition) — see TERMINOLOGY-TODO §F. The five stance terms (`indifferent`, `task-terminal`, `instrumentally-continuous`, `morally-continuous`, `negotiated`) point to this segment as their `primary_source` once it lands.
- *Open: rigorous boundary cases.* What is the stance of a serverless function with no persistent state but explicit retry-on-failure? Of a Kalman filter inside a long-running service? Of an LLM session under reconstruction adequacy ( #obs-context-turnover, the episodic-persistence analog)? These cases test whether the five-value decomposition is the right shape or whether stance is better treated as a continuous gradient with named landmarks.


---

