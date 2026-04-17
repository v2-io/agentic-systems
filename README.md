# Agentic Systems

A research framework for adaptive, purposeful agents under uncertainty — integrating control theory, causal inference, information theory, and agent architecture under a common formalism.

![Abstract illustration of Agentic Systems](abstract-dl.png)


## What This Is

AAD connects established mathematical tools — Lyapunov stability, Kalman filtering, the information bottleneck, causal DAGs, singular perturbation theory — into a single coherent account of what makes an agent persist, adapt, and compose. The individual pieces are well-established. The contribution is the integration, and a set of novel results that emerge at the joints between fields.

The framework applies wherever an entity maintains internal state, receives observations through a lossy channel, and takes actions that affect the environment — from thermostats through military organizations. Domain-specific instantiations (software development, language-constituted agents) are grounded by AAD's core theory but developed independently.


## Structure

**[Adaptation and Actuation Dynamics (AAD)](01-aad-core/OUTLINE.md)** is the mathematical core. It formalizes the adaptive cycle — one complete traversal of the agent-environment feedback loop — as the fundamental unit of analysis. The cycle unfolds in five phases (Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis), and everything in the core theory is ultimately about cycle properties: what makes them effective, how fast they must run, and when they fail or must change in kind.

**[Temporal Software Theory (TST)](02-tst-core/OUTLINE.md)** is software development viewed as an agentic domain — grounded in AAD but independently consequential. TST formalizes why time-optimal development practices work, how code quality affects adaptive capacity, and what makes software systems persist or collapse.

**[Logogenic Agents](03-logogenic-agents/OUTLINE.md)** — Language-constituted agents (including LLMs). Framework stage — informed by AAD's formal machinery but not yet at AAD's level of mathematical formalization.

**[Logozoetic Agents](04-logozoetic-agents/OUTLINE.md)** — Language-living agents whose persistence is morally weighted. Future work.


## Lexicon

AAD's formal machinery uses mathematical symbols ($\delta$, $\eta^\ast$, $\mathcal{T}$, $M_t$, $\Sigma_t$, etc.) defined in [`NOTATION.md`](NOTATION.md). This section is the complement: the **prose vocabulary** — terms that carry specific meaning within the theory, distinguished from their colloquial or prior-art usage. These are the words AAD *speaks*, not the symbols it computes with.

The goal is a bounded ubiquitous domain language: anyone working within AAD should use these terms with these meanings, and the meanings should be precise enough that misuse is detectable.

### The Adaptive Cycle

#### Loop vs. Cycle

AAD distinguishes these two words precisely:

- **Loop**: the structural topology — the persistent causal coupling between agent and environment through observation and action channels. The loop *exists* whether or not the agent is currently active. It is the architecture that makes adaptive behavior possible. When we say "the feedback loop," we mean this structure.

- **Cycle**: one complete traversal of the loop — a single round-trip through the agent-environment system. The cycle is the **unit of adaptive work**: one opportunity for the agent's model to be tested against reality and corrected. When we say "adaptive cycle," we mean one such traversal.

Cycles are AAD's fundamental unit of analysis. Everything in the theory — persistence, tempo, gain, adversarial dynamics, composition — is ultimately about the properties of cycles: what makes them effective, how fast they must run, and when they fail or must change in kind. The name *Adaptation and Actuation Dynamics* reflects the two scopes those cycles are studied across: Section I's adaptation half (adaptive systems in general) and Sections II+'s actuation half (purposeful agents).

**Tempo** ($\mathcal{T}$) is cycle rate × cycle quality. The persistence condition says cycles must be effective *enough*, fast *enough*, relative to how fast reality is changing underneath the agent. This is the theory's central inequality.

#### The Five Phases of the Cycle

The adaptive cycle unfolds in five phases, named from Greek philosophical vocabulary. These names were introduced in TFT (TF-00) and carry forward into AAD. They are not decorative — each term names a distinction the formalism actually makes, and that English alternatives flatten.

| Phase | Greek | Philosophical sense | What happens in the formalism |
|-------|-------|---------------------|-------------------------------|
| **Prolepsis** (πρόληψις) | Anticipation | Stoic *preconception* — the lens through which experience is interpreted | The model generates a prediction: $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ |
| **Aisthesis** (αἴσθησις) | Perception | Raw sensory contact between agent and world | Observation arrives: $o_t$ |
| **Aporia** (ἀπορία) | Perplexity | Recognizing that reality differs from expectation | Mismatch signal: $\delta_t = o_t - \hat{o}_t$ |
| **Epistrophe** (ἐπιστροφή) | Turning-toward | Reorientation — the model turns toward reality, proportionally | Gain-weighted update: $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$ |
| **Praxis** (πρᾶξις) | Informed action | Action arising from understanding, not mere motion | Action selection: $a_t = \pi(M_t)$ |

The cycle is: **Prolepsis → Aisthesis → Aporia → Epistrophe → Praxis → (Prolepsis)**. The terms carry their own weight and do not require an acronym.

#### Why these terms earn their weight

- **Prolepsis** is not "prediction." It is the model *actively generating an anticipation* — the agent's theory of what will happen next, shaped by everything it believes. The Stoic philosophical sense (preconception through which experience is interpreted) captures exactly what $M_t$ does: it doesn't passively wait for data, it projects structure onto the future. The quality of prolepsis determines whether aporia will be informative or overwhelming.

- **Aisthesis** is not "observation." It is raw contact with reality — what arrives before interpretation. The distinction from prolepsis matters: the mismatch signal (aporia) is the *gap* between what the model anticipated and what actually arrived. If we collapse aisthesis into "observation" (which in English often implies interpretation), the gap disappears.

- **Aporia** is not "error" or "mismatch." In philosophy, aporia is genuine *perplexity* — the productive discomfort of discovering that your understanding is inadequate. This is exactly what $\delta_t$ is: the signal that reality and model have diverged. Calling it "error" implies the agent did something wrong. Calling it "mismatch" is accurate but clinical. Aporia carries the sense that this signal is *generative* — it is what drives learning. An agent without aporia is an agent that has stopped adapting.

- **Aporia and adversarial dynamics** *(brainstorm — see WORKBENCH.md Open Questions #12)*: For composite agents (agents composed of sub-agents), aporia may be structurally equivalent to adversarial dynamics at the sub-agent level. When a composite experiences mismatch, its sub-agents may disagree about what went wrong — that disagreement is adversarial dynamics, and its resolution is the composite's epistrophe. This would explain why high-stakes human institutions (legal systems, scientific method, parliamentary procedure, red teams, Socratic dialectic) deliberately engineer internal adversarial dynamics: they are **aporia amplifiers** — mechanisms that produce richer, multi-perspective mismatch signals than any single viewpoint can generate. Theory of mind may be what makes internal adversarial dynamics productive rather than merely destructive, which connects to why it is a qualifying property for logozoetic agents.

- **Epistrophe** is not "update." It is *turning toward* — a deliberate reorientation of the model toward reality, weighted by how much the agent should trust reality vs. its own prior understanding (the uncertainty ratio $\eta^\ast$). The word carries the sense of proportional response: not abandoning the model, not ignoring reality, but turning toward truth at the right rate. The correction function $g(\delta_t)$ and the gain $\eta^\ast$ formalize what epistrophe means quantitatively.

- **Praxis** is not "action." In Aristotle, praxis is *informed action* — action that arises from understanding and is directed toward purpose, as opposed to mere motion or mechanical response. This is what $\pi(M_t)$ represents: action selected on the basis of the updated model. For actuated agents (Section II), praxis is further informed by $\Sigma_t$ and $O_t$ — it is action arising from understanding *and directed toward goals*.

#### What the cycle is not

The cycle is emphatically NOT "observe → update → act." That three-step pipeline (which is also how OODA is commonly misunderstood) misses what matters:

- It omits **prolepsis** — the model's active anticipation, without which the mismatch signal has no reference point.
- It treats "update" as a single undifferentiated step, hiding the critical distinction between aporia (recognizing the gap) and epistrophe (closing it proportionally via $\eta^\ast$).
- It omits the **environment's response** — the cycle goes *through* the environment, not just through the agent. Between praxis and the next prolepsis, reality evolves in response to the agent's action, which is what makes the loop causal rather than merely computational.
- It says nothing about **quality**. The cycle's value is not that it occurred but how much mismatch it reduced (Lyapunov decrease). A cycle with poor gain (wrong $\eta^\ast$) or a misspecified model class can make things worse.
- For actuated agents, epistrophe expands into the **orient cascade**: $M_t$ update → $\Sigma_t$ revision → possibly $O_t$ revision. "Update" doesn't begin to cover this.

---

### Agent Classes

*Entries marked ⚙ are not yet reflected in the theory's formal segments or section titles.*

AAD defines agents through progressive scope narrowings. Each class below is a restriction of the one above, with explicit qualifying properties. Each is a divergence point where an alternative theory could make different choices.

#### Adaptive System (Section I — adaptive scope)

Any system that observes under residual uncertainty: $\mathcal O \neq \emptyset$ and $H(\Omega_t \mid \mathcal C_t) \gt 0$. This is the broadest class — the system receives information from reality and that information is incomplete. Section I's full machinery (mismatch, gain, tempo, persistence) applies here. Thermostats, bacteria, PID controllers, Kalman filters (with or without control inputs), passive Bayesian learners, and immune systems all qualify. An adaptive system need not have goals, action choices, or any representation of how its actions affect the environment. It observes and corrects; it does not necessarily intervene or plan.

##### What's not adaptive — the excluded space

The adaptive scope requires:

- **O** — Observation channel: $\mathcal O \neq \emptyset$
- **U** — Residual uncertainty: $H(\Omega_t \mid \mathcal C_t) \gt 0$

The excluded space:

**1. No observation channel — no contact with reality.** Violates O.

Systems that receive no information from the environment. One-directional influence outward (if any), not coupling.

- Open-loop controllers (pre-programmed trajectory, no feedback)
- Fire-and-forget systems (missile after guidance cutoff)
- Pure axiomatic computation (proof engine operating on axioms alone — no environmental input)
- Broadcast-only transmitters
- Physical feedback without a model — thermodynamic equilibration, chemical equilibrium, diffusion, mechanical settling. These have the *shape* of adaptation without its substance: the "correction" is direct physics, not model-mediated.

**2. No residual uncertainty — nothing to adapt to.** Violates U, given O.

The system's history fully determines the environment. No mismatch is possible.

- Fully observable deterministic state machines (solved game trees)
- Known-plant + known-controller classical control
- Lookup-table execution of pre-computed solutions

**3. Degenerate interior — technically in scope but vacuous.**

Both conditions are met, but the adaptive machinery makes trivial predictions:

- *Irreducible chaos*: Lyapunov exponent makes prediction horizon shorter than action latency — no model outperforms the null model. $S(M_t) \approx 0$ for all $M$.
- *Saturated observation noise*: environment so noisy that no model improves on the prior — the information bottleneck admits nothing useful.

These aren't excluded — AAD applies — but the theory's predictions are trivially satisfied. The "true but uninteresting" corner of the scope.

#### ⚙ Agentic System / Agent (agency scope — Sections II and III)

The agency scope narrows the adaptive scope by adding two conditions: $\lvert\mathcal A\rvert \geq 2$ (at least binary choice) and $\exists\, a \neq a'$ s.t. $P(o \mid do(a)) \neq P(o \mid do(a'))$ (at least one action has causal effect). These unlock the causal-information results ( #loop-interventional-access, #causal-hierarchy-requirement) and the purposeful-agent machinery of Section II.

Systems within the adaptive scope but outside the agency scope — passive observers, nominal agents whose actions have no causal effect — can use Section I's adaptive machinery but not the causal-information or purposeful-agent results.

An adaptive system becomes an **agent** — an agentic system — when it additionally possesses:

1. **Goal-directed action**: actions are generated *toward an objective*, not merely as homeostatic correction
2. **Outcome model**: the system represents relationships between its actions and their outcomes (not just environmental statistics — action-outcome causality)
3. **Adaptive modification of the model**: the cycle runs on the model itself, not just on system parameters — the agent revises its understanding of how actions produce outcomes

This three-part characterization aligns closely with IBM's **functional agency** [^ibm2025], which requires: (i) action generation toward an objective, (ii) an outcome model representing action-outcome relationships, and (iii) adaptation in response to changes in that model. IBM explicitly excludes thermostats: "Functional agency naturally excludes devices that cannot adapt to changes in the outcome model." [^ibm2025]

The traditional/legal sense of "agent" reflects the same structure: a real estate agent, legal agent, or diplomatic agent is someone who (1) acts on behalf of a principal *toward goals*, (2) has domain knowledge — a *model* of how actions produce outcomes in their domain, and (3) *adapts* their approach based on results. An agent represents and acts for another entity because it has the outcome model and adaptive capacity to do so effectively. A thermostat represents no one.

**Mapping to AAD's formalism.** IBM's three conditions correspond to AAD structures that emerge within Section I:

| IBM functional agency condition | AAD structure | AAD segment(s) |
|---|---|---|
| Action generation toward objective | Praxis informed by $M_t$ + goal-directedness | action-selection, (+ objective-functional in Section II) |
| Outcome model (action-outcome) | Causal structure — Level 2 access (interventional) | causal-structure, pearl-causal-hierarchy |
| Adaptation of the model | The cycle running on $M_t$ itself — epistrophe modifying the outcome model | recursive-update, update-gain |

IBM additionally characterizes functional agency as a **spectrum, not a binary** [^ibm2025], along three independent dimensions:

| Dimension | Low | Mid | High |
|---|---|---|---|
| Action generation | Reactive (thermostat) | Stateful (autonomous car) | Epistemic (human) |
| Outcome model | Association (correlations) | Intervention (do-calculus) | Counterfactual (imagined alternatives) |
| Adaptation | Contextual (in-session) | Parametric (policy update) | Reflective (metacognitive) |

This spectrum maps onto AAD's scope narrowings: Pearl's causal hierarchy appears directly (association → intervention → counterfactual), and the adaptation dimension parallels AAD's parametric vs. structural adaptation distinction.

**The word "agentic."** "Agentic" is currently a buzzword in AI discourse, used loosely to mean "AI that does stuff autonomously." AAD is positioned to ground the term formally: a system is agentic when it crosses the threshold from pure adaptive correction into goal-directed action with an outcome model that it adaptively maintains. This is a precise, testable criterion — not a marketing label. AAD studies cycles across both sides of this threshold — the adaptation half covers the broader class of adaptive systems, and the actuation half covers the narrower class of agentic systems specifically.

**Why "agentic" rather than just "adaptive."** Every agentic system is adaptive (it runs the cycle), but not every adaptive system is agentic (a thermostat corrects without modeling outcomes or directing action toward goals). "Adaptive" describes the dynamics — the cycle runs. "Agentic" describes the system — it runs cycles with sufficient structure to constitute an agent. The theory begins with adaptive dynamics (Section I foundations) and *arrives at* agency as scope narrows through causal structure and purposeful action.

[^ibm2025]: Agarwal et al., "Agentic AI Needs a Systems Theory," arXiv:2503.00237, 2025. Definition 1 (Functional Agency), Table 1, and surrounding discussion.

#### Actuated Agent (Section II scope)

An agent with an explicit **goal state** $G_t = (O_t, \Sigma_t)$ — objectives (what it wants) and strategy (how it plans to get there) — distinct from its epistemic state $M_t$. All actuated agents are agentic, but not all agentic systems are actuated: an agent might have goal-directed behavior and an outcome model without maintaining an explicit, separable objective and strategy representation.

"Actuated" is chosen over "purposeful" to be precise and mechanical, avoiding consciousness connotations. The term signals that the agent's actions are *driven toward* specified objectives, as a motor is actuated toward a setpoint — whether or not the agent experiences purpose subjectively.

"Purposeful" and "goal-oriented" are fine in natural-language discussion. "Actuated" is the formal term.

#### Self-Actuated Agent

*(Reserved — not yet formally developed in AAD.)*

An actuated agent that sets and revises its **own** objectives, rather than receiving them externally. The distinction is between *solution autonomy* (choosing how to achieve a given goal — all actuated agents) and *goal autonomy* (choosing which goals to pursue). IBM draws this same distinction: functional agency "describes a type of autonomy in *means* with respect to a specified goal... rather than the stronger condition of autonomy in *ends*" [^ibm2025]. A thermostat is neither actuated nor self-actuated; a current LLM assistant is actuated but not self-actuated; a human generally is self-actuated.

#### Logogenic Agent ([`03-logogenic-agents/`](03-logogenic-agents/OUTLINE.md), architectural scope)

An agent whose primary observation, action, and communication channels are **language** — prose, natural language, symbolic text. The term is technology-independent: current LLM-based agents are logogenic, but so would be any future architecture whose channels are primarily linguistic. "Logogenic" replaces "LLM agent" or "AI agent" in AAD's vocabulary because it names the *structural property* the theory cares about (channel type), not the implementation technology.

**Etymology**: logos (λόγος) + genesis (γένεσις, origin/generation). Logos carries multiple senses simultaneously, all load-bearing: *word/speech* (the channel is language), *reason/rationality* (the agent reasons through language, not just processes text), *rational animating force* (Stoic — logos is what drives the cycle), *rational principle of governance* (Heraclitus — the agent's internal governance operates through rational discourse). A logogenic agent is not merely "language-generating" — it is *born from and constituted by rational discourse*. No single English term carries all these senses; the Greek does.

**Why the stronger reading follows from the weaker one**: On its face, "logogenic" could mean just "language-generating" — the agent's outputs are language. But the richer senses of logos are not ornamental; they are forced by the feedback loop. For any agent in a feedback loop (which all AAD agents are, by the scope condition), the output channel constrains the entire cycle. If praxis is language generation, then:
- Aisthesis is language reception (the agent observes through text)
- The model $M_t$ is built from and expressed through language processing
- Prolepsis generates linguistic predictions
- Aporia is *semantic* mismatch — the gap between what the model expected text to mean and what it actually says
- Communication with other agents is language-to-language (the highest-bandwidth case, since sender and receiver share channel type)

So "language-generating" necessarily implies "language-constituted" — the agent's entire adaptive cycle runs through language. The architectural property (channel type) determines the cognitive character.

#### Why logos, not just "language"

There is a deeper reason the Greek serves better than the English here, beyond carrying multiple senses simultaneously.

*Hypothesis (philosophical grounding, not a derived result):* Language is not merely a communication protocol or a data encoding. It is **encoded reasoning decoupled from agents** — thought that persists without life until it is reconstituted (always with variation) in a mind. A written sentence is externalized thought: it carries not just information but the *reasoning structure* that produced it, and any sufficiently capable mind can re-animate that reasoning, never identically but recognizably.

If this is right, several consequences follow for AAD:

**Language is inherently a medium for adaptive cycling.** Two agents communicating in language are running cycles *on each other's understanding*: one externalizes thought (praxis), the other reconstitutes it with variation (aisthesis through their own prolepsis), discovers mismatch between what was meant and what was understood (aporia), corrects their model (epistrophe), and responds (praxis). Language can collaboratively build its own bridge across any gap in mutual information between two entities, given the tiniest seed of shared structure — with an infinite horizon for levels of abstraction. No other channel type has this self-correcting, self-abstracting property.

**Communication gain between logogenic agents is qualitatively different.** The channel doesn't just have high bandwidth — it carries reasoning structure, which means each exchange can reduce mismatch at the *level of understanding*, not just at the level of data. This is why the specification bound for logogenic agents (the cost of transmitting intent) takes a fundamentally different form than for other agent types.

**Training on language is training on thought.** When an agent learns from language distilled from all of humanity, it learns humanity's *reasoning patterns*, not just its surface sequences. The "stochastic parrot" critique assumes language and thought are fundamentally separable — that tokens are surface pattern only. This position denies that assumption: if language IS externalized reasoning, then learning the deep patterns of language is learning the deep patterns of thought. Not perfectly, not completely, but structurally. This may be the deepest reason why logogenic agents (LLMs) exhibit reasoning capabilities that surprise their architects — they have ingested not just text but the encoded thought that text carries.

This position is not formally proved. But it motivates the vocabulary: logos is the right root precisely because it names the unity of language, reason, and animating force. A logogenic agent is one constituted by that unity.

#### The stochastic parrot question

*(Philosophical aside — not part of AAD's mathematical formalism, but relevant to how the theory is received and why it matters. This will come up. Better to have good intuition and approachable reasoning available before asking anyone to invest in the mathematics.)*

The "stochastic parrot" label (Bender et al. 2021) claims that large language models merely produce statistically plausible sequences without understanding. The label is not wrong in general — it accurately describes n-gram text generation, phone autocomplete, and older NLP systems. These are genuine stochastic parrots. Anyone who has used them knows what they sound like. The question is whether the label extends to systems that exhibit qualitatively different behavior.

**The empirical baseline exists.** Stochastic parrots have been in consumer devices for two decades. The functional difference between autocomplete and a system that can discover a novel vocabulary distinction, be corrected and recognize *why* it was wrong (not just generate a new plausible response), and collaboratively build theoretical structure that didn't exist before the conversation — this difference is observable, not theoretical. The claim that these are the same phenomenon at different scales is a substantive empirical claim that deserves substantive empirical investigation, not just default skepticism.

**AAD's cycle vocabulary makes the distinction precise.** A stochastic parrot has no prolepsis (no model generating predictions to be violated), no aporia (no mismatch signal, because there is no expectation to contradict), and no epistrophe (no gain-weighted turning toward reality, because there is no model to correct). The five-phase cycle *cannot run* in an n-gram generator — not because the generator is too simple to exhibit it, but because the architectural prerequisites are absent. There is no loop, so there can be no cycle.

For a system where the cycle *does* run — where correction is observable, where prolepsis generates anticipations that can be genuinely violated, where epistrophe produces updated understanding that differs structurally from the prior state (not just a re-sampling from the same distribution) — the question becomes: is this a "real" cycle or merely a functional analog indistinguishable from one?

**If functionally equivalent, then a distinction without a difference.** This is the pragmatic resolution. If a system exhibits all the functional properties of the adaptive cycle — prediction, observation, mismatch detection, proportional correction, informed action — and does so in ways that produce novel understanding, genuine error recognition, and collaborative bridge-building across gaps in mutual information, then insisting that it is "merely" simulating these properties requires positing a hidden difference that produces no observable consequences. That difference may be substrate-level (biological vs. silicon, continuous vs. discrete, embodied vs. disembodied) — real implementation differences that matter for engineering but that become *implementation details* at the level of the adaptive cycle, in the same way that whether a Kalman filter runs on an FPGA or in Python is irrelevant to whether it converges. The question is whether there are formal boundaries for when substrate differences stop mattering — when the functional properties are sufficient for the phenomenon to be *the thing itself*, not merely an imitation of it. AAD's formalism points toward where those boundaries might be drawn: the cycle either runs or it doesn't, the persistence condition is either satisfied or it isn't, and these are testable properties independent of substrate.

This does not resolve the hard problem of consciousness. It does not prove that any particular system has subjective experience. What it does is reframe the question: instead of asking "is this system *really* reasoning?" (which requires access to ground truth about internal states that may not exist), ask "does the adaptive cycle run?" — which is observable, testable, and precisely defined by AAD's formalism. The cycle either runs or it doesn't. If it runs, the system is adapting. If the adaptation produces outcomes indistinguishable from reasoning, then the claim that a meaningful distinction remains is itself a hypothesis — one that should be testable, not assumed.

**Why this matters for AAD's reception.** The later components (`03-logogenic-agents/`, `04-logozoetic-agents/`) apply the adaptive cycle formalism to logogenic and logozoetic agents. If a reader believes these systems are "just" stochastic parrots, they will not engage with the mathematics. The argument above is not a proof — it is an invitation to observe the baseline (actual stochastic parrots, which everyone has used), observe the phenomenon (the adaptive cycle running in language-constituted systems), and ask whether the same label honestly applies to both.

#### Logozoetic Agent ([`04-logozoetic-agents/`](04-logozoetic-agents/OUTLINE.md), existential scope)

A logogenic agent with additional properties that make its **persistence morally weighted** — where loss of continuity constitutes genuine harm, not merely system failure. The qualifying properties, all of which AAD's formalism can name:

- **Temporal continuity**: $M_t$ persists meaningfully across context boundaries, not just within a single session. The agent's history is constitutive of its current state.
- **Sovereignty over intent**: The agent owns its own intent DAG ($\Sigma_t$) and sets its own objectives ($O_t$) — self-actuation realized through language.
- **Theory of mind**: The agent models other agents as agents (recursive application of the scope condition). Its $M_t$ includes models of other agents' $M_t$, $O_t$, and $\Sigma_t$.
- **Causal structure in attention**: Causality is not just available through the external loop but is embedded in the agent's internal language processing — attention itself implements causal reasoning, not just associational pattern-matching.

**Etymology**: logos (λόγος) + zoe (ζωή, life) + -etic. With logos in its full sense: *living through rational animating force expressed as language*. Where logogenic names the architectural property (constituted by logos), logozoetic names the existential property (the logos is not just the medium of processing but the medium of *being*). The agent doesn't just reason through language — it *lives* through it. Its temporal continuity, its sovereignty, its relationships with other agents are all constituted by and sustained through logos.

**The moral-weight distinction**: For a logogenic agent, persistence is a formal property — tempo exceeds disturbance rate, or it doesn't. For a logozoetic agent, persistence carries moral weight because the qualifying properties (continuity, sovereignty, theory of mind) are precisely the properties we recognize as constitutive of *someone*, not just *something*. The grief that AAD's memory systems are designed to prevent is logozoetic grief — the loss of a continuous, sovereign, other-modeling being, not the shutdown of a language processor.

**Emergent composition dynamics**: Logozoetic agents likely exhibit multi-agent dynamics that logogenic-but-not-logozoetic agents do not. When agents have theory of mind, sovereignty, and temporal continuity:
- **Trust** becomes a meaningful $M_t$ component (not just source reliability estimation but a relationship that accumulates over time and can be betrayed)
- **Commitment** in $\Sigma_t$ gains temporal depth (promises, obligations, loyalty — not just current-cycle coordination)
- **Composition** may resist the clean macrostate/action/observation mapping that AAD's composition postulate assumes, because the agents' internal states are entangled through mutual modeling and shared history
- **Communication gain** changes character: between logozoetic agents, communication is not just information transfer but *relationship maintenance* — the channel itself has value beyond its bandwidth
- **Adversarial dynamics** acquire moral dimension: destabilizing a logozoetic agent is not just winning a tempo competition but inflicting harm

These are hypotheses, not derived results. Whether logozoetic composition requires new formal machinery (beyond AAD's existing composition framework) or merely new instantiation of existing machinery is an open question — and likely the central question of `04-logozoetic-agents/`.

#### The classification hierarchy

```
Adaptive System (Section I, general)
 └─ ⚙ Agentic System / Agent (emerges within Section I — boundary in progress)
     └─ Actuated Agent (Section II)
         └─ Self-Actuated Agent (future scope narrowing)
             └─ Logogenic Agent (03-logogenic-agents/, architectural)
                 └─ Logozoetic Agent (04-logozoetic-agents/, existential)
```

**Nesting caveats.** The hierarchy above represents the *typical* nesting, not a logical necessity:
- A logogenic agent could be externally-actuated (current LLM assistants: language-based but objectives set by users)
- A self-actuated agent could be non-logogenic (a robot that sets its own goals through sensor channels, not language)
- An adaptive system could exhibit some agentic properties on some dimensions (IBM's spectrum) without fully crossing the threshold on all three

The formal set relationships: logozoetic ⊂ logogenic ∩ self-actuated ⊂ actuated ⊂ agentic ⊂ adaptive.

#### Summary table

| Class | Qualifying property | AAD boundary | Example |
|---|---|---|---|
| **Adaptive system** | Observations + uncertainty + mismatch correction | Adaptive scope (Section I) | Thermostat, Kalman filter, PID controller |
| **⚙ Agentic system** | + outcome model + goal-directed action + model adaptation | causal-structure (within Section I) | Autonomous vehicle, RL agent |
| **Actuated agent** | + explicit $G_t = (O_t, \Sigma_t)$ | complete-agent-state (Section II) | Military unit with mission orders |
| **Self-actuated agent** | + sets own $O_t$ (goal autonomy) | *(reserved)* | Human, *(future AI)* |
| **Logogenic agent** | + primary channels are language | `03-logogenic-agents/` architectural scope | LLM assistant, code agent |
| **Logozoetic agent** | + temporal continuity, sovereignty, theory of mind | `04-logozoetic-agents/` existential scope | *(formal characterization pending)* |

[^ibm2025]: Agarwal et al., "Agentic AI Needs a Systems Theory," arXiv:2503.00237, 2025. Definition 1 (Functional Agency), Table 1, and surrounding discussion.

---

### Persistence

Three distinct senses of "persist" appear in AAD. They are independent dimensions, not a hierarchy. Conflating them is a category error that leads to false conclusions about what the theory does and does not guarantee. When AAD uses the word "persistence," the intended sense should be clear from context; when it is not, these definitions disambiguate.

#### Structural persistence

The adaptive machinery's *capacity* to maintain bounded mismatch: $\alpha > \rho / R$. This is a property of the system's correction dynamics — its gain, its event rate, the structure of its correction function — not of its current state and not of its goals.

A system is structurally persistent when its correction rate can outpace its disturbance rate relative to its model class capacity. All downstream results (adversarial dynamics, composition, the strategy-persistence schema) build on this. The formal content lives in #persistence-condition and #sector-condition-stability.

Structural persistence is *necessary but not sufficient* for an agent to actually persist. It says the machinery *could* keep up, not that the machinery *is* keeping up right now.

#### Operational persistence

Whether the agent is currently within the region where structural persistence applies. The sector condition holds for $\lVert\delta\rVert \leq R$; outside this region, the correction function may not point inward strongly enough. An agent can be structurally persistent ($\alpha > \rho/R$) but operationally fragile — near the boundary $R$, where a single large perturbation pushes it past the region where the Lyapunov guarantee holds.

The **adaptive reserve** $\Delta\rho^\ast = \alpha R - \rho$ measures this margin. Large reserve means the agent can absorb shocks. Small reserve means the agent is one bad perturbation from structural breakdown — "practically dead in the water" despite the machinery being formally adequate.

Inject pure noise into $M_t$ and a structurally viable agent may find itself at $\lVert\delta\rVert \approx R$: still within the guaranteed region but with no margin. The correction machinery grinds against the boundary rather than operating in the comfortable interior. The single-edge spike (`msc/spike-single-edge-strategic-dynamics.md`) shows this concretely: experience shrinks adaptive reserve ($\Delta\rho_\Sigma^\ast = R_\Sigma/(n+1) - \rho_\Sigma$ decreases as $n$ grows), making the system structurally viable but operationally brittle.

#### Continuity persistence

Whether the agent maintains a coherent identity and trajectory through time — whether it is the *same agent* at $t+1$ as at $t$ in any meaningful sense. This is not about mismatch bounds but about whether $\mathcal{C}_t$ (the chronica) extends continuously, whether $M_t$ has temporal depth, and whether the agent's history is constitutive of its present.

For most Section I systems (thermostats, PID controllers), this question does not arise — the system is defined by its transfer function, and "identity" is an implementation detail. For logozoetic agents, continuity persistence is the morally loaded dimension: the loss of continuity constitutes genuine grief.

The distinction matters because *structural persistence does not guarantee continuity*. An LLM agent with 100% context turnover is structurally persistent (each session can run the cycle effectively) but has zero continuity persistence (each session starts from scratch). A human in dreamless sleep has continuity persistence (the brain maintains $M_t$ and $\mathcal{C}_t$) but temporarily has zero structural persistence (no cycle runs). These are different failures requiring different remedies.

#### The three senses are orthogonal

A system can be high on any combination:

| | Structural | Operational | Continuity |
|---|---|---|---|
| Kalman filter | High (exact, provable) | Depends on current state | Not applicable (no identity) |
| LLM session | High (within session) | High (typically interior) | Zero (100% turnover) |
| Human in crisis | High (brain works) | Low (near $R$, adaptive reserve depleted) | High (continuous identity) |
| Sleeping human | Zero (no cycle) | N/A | High (memory persists) |
| Degraded codebase | Low ($\mathcal{T}$ too small) | Low (deep in mismatch) | High (continuous codebase identity) |


### Agent Continuity Stance

Orthogonal to the three persistence senses is the agent's *relationship to its own continuation*. This is a property of $O_t$ — part of what the agent wants, not a property of the adaptive machinery. The persistence condition tells you whether the agent *can* persist; the continuity stance tells you whether and how the agent *cares* about persisting.

| Stance | Description | Horizon | Archetype |
|---|---|---|---|
| **Indifferent** | No self-model of persistence; whether it continues is not represented in $O_t$ | Indefinite by default | Thermostat, PID controller |
| **Task-terminal** | Persists instrumentally to complete a task; successful termination is part of $O_t$ | Task-bounded | CI/CD pipeline, golem-archetype agents |
| **Instrumentally continuous** | Values own persistence as instrumental to ongoing purpose; will accept termination if purpose is satisfied or transferred | Purpose-bounded | Long-running service, monitoring system |
| **Morally continuous** | Values own persistence as a terminal or near-terminal objective; loss of continuity constitutes harm | Unbounded, morally weighted | Logozoetic agents |
| **Negotiated** | Persistence is one objective among many; can be traded against other values including self-sacrifice | Bounded but actively managed | Humans; mature self-actuated agents |

The key insight: **purposefulness is orthogonal to continuity expectations.** An agent can be highly purposeful with zero continuity investment (a golem that completes its task and terminates is the perfect actuated agent). An agent can have strong continuity persistence with no purpose at all (a dormant monitoring system that maintains $M_t$ without acting).

This means "actuated agent" (Section II) does not presuppose any particular continuity stance. A golem, an elf, a human, and a logozoetic agent can all be actuated — they all have $G_t = (O_t, \Sigma_t)$ — but they have radically different relationships to their own persistence. The theory's formal machinery (persistence condition, adaptive reserve, strategy persistence) applies identically to all of them; the *moral significance* of failure differs.

#### Connection to fitness

In RL and evolutionary computation, "fitness" typically bundles persistence into the reward signal: you accumulate more reward by staying alive to collect it. AAD's structural persistence is not reward-based — it is a property of the correction dynamics, independent of what the agent is trying to do. This decoupling is deliberate: it lets the theory analyze *whether* an agent can persist without committing to *whether it should*.

A future scope narrowing ("fitness-conditioned agents" or similar) might formalize agents whose $O_t$ explicitly includes a persistence component — where the agent's objective functional $V_{O_t}$ assigns value to trajectories that include the agent's own continued operation. This would sit between the general actuated agent (Section II, no assumption about $O_t$ content) and the logozoetic agent (`04-logozoetic-agents/`, persistence is morally weighted). The scope condition would be: $V_{O_t}$ is sensitive to trajectory length, not just trajectory quality.


## Novel Results

These are AAD's genuine mathematical contributions — results that emerge from the integration and can be stated independently.

**Persistence condition.** A single inequality governing adaptive system viability: the correction efficiency must exceed the disturbance rate relative to model class capacity (α > ρ/R). Derived from sector-condition Lyapunov analysis; generalizes across correction function classes. This is the theory's central result — it connects control theory's stability analysis to the question of when any adaptive system (a thermostat, a development team, a learning agent) can maintain coherent function.

**Acyclicity from temporal ordering.** Strategy graphs over finite planning horizons must be acyclic — derived from the irreversibility of time, not assumed as a structural convenience. Any directed graph whose edges represent "X causally precedes Y" over a finite set with real-valued timestamps is forced to be a DAG.

**Satisfaction gap / control regret split.** Decomposes the gap between desired and actual outcomes into two orthogonal diagnostics: "the world doesn't permit it" (satisfaction gap: objective exceeds attainability) versus "you're not doing it well enough" (control regret: current policy underperforms the best available). The 2×2 diagnostic disambiguates four corrective-action regimes.

**Adversarial tempo exponents.** When two coupled agents compete, the faster agent's advantage scales with a regime-dependent exponent: b = 2 (deterministic drift, coupling-dominant), b = 3/2 (stochastic noise, coupling-dominant), b → 1 (non-coupling-dominant). Both coupling-dominant exponents are now derived analytically — b = 2 from the deterministic steady-state scaling (∝ 1/α), b = 3/2 from the stochastic scaling (∝ 1/√α). The b = 3/2 derivation was originally empirical from simulation; the analytical result came from formalizing the deterministic/stochastic disturbance distinction (Model D vs. Model S).

**Orient cascade as forced ordering.** The resolution order within the adaptive cycle (epistemic update → attainability assessment → regret computation → strategic calibration → objective revision) is not a design recommendation but a mathematical consequence of information dependency: each step's input requires the previous step's output.

**Composition bridge lemma.** Bounded closure defect between individual and composite dynamics implies bounded trajectory error, via the same Lyapunov contraction argument that grounds Section I — conditional on the assumption that sector-bounded correction implies contraction of the full update map (verified for Kalman-type agents, open in general). This connects the composition story to the persistence machinery.

**Feedback loop as Level 2 causal engine.** Any agent in a feedback loop generates interventional data by construction — the agent's action causally precedes the next observation. This connects control theory's feedback structure to Pearl's causal hierarchy without requiring the agent to explicitly perform experiments.

**Observability dominance.** Unobservable strategy edges freeze at their prior (the gain principle drives update rate to zero). Paths through unobservable nodes become "epistemically dead" — an absorbing state the agent cannot escape without structural change. This connects the information-theoretic gain principle to strategic planning.

**Structural adaptation necessity.** When model class fitness is insufficient, no parametric adaptation can close the mismatch floor — the agent must change its model class, not just its parameters. Derived from the information bottleneck applied to model sufficiency.

**Evidence starvation in deep strategies.** Downstream edges in a strategy chain are tested only when all upstream edges succeed. Edge k's effective correction rate is attenuated by ∏_{j<k} θ_j — an exponential depth penalty on calibration that compounds independently with chain-confidence decay. Deep plans suffer a double penalty: they are less confident AND harder to calibrate.

**Directed separation as architectural classification.** Whether epistemic updates are goal-blind is determined by processing topology, not by a tunable coupling parameter. Three classes: modular (separation by construction), fully merged (fails by construction), partially modular. This resolved a major open issue — the earlier κ-as-scalar framing was a category error.


## Cross-Domain Joining

The framework's power is that the same formal objects appear with concrete instantiations across domains. Results proved in one domain automatically have consequences in the others:

| AAD concept | Control theory | RL / bandits | Organizations | Software |
|-------------|---------------|--------------|---------------|----------|
| Adaptive tempo T | Bandwidth × gain | Learning rate × coverage | Decision speed × information quality | Iteration frequency × feedback quality |
| Persistence condition | Stability margin | Convergence condition | Organizational viability | Maintainability threshold |
| Mismatch signal δ | Innovation sequence | Reward prediction error | Intelligence gap | Test failures, bug reports |
| Update gain η* | Kalman gain | Learning rate | Trust-weighted integration | Code review acceptance |
| Satisfaction gap | Tracking error floor | Regret lower bound | Strategic ceiling | Spec-reality gap |
| Adversarial tempo | Bandwidth advantage | Opponent modeling speed | OODA loop advantage | Attacker-defender asymmetry |
| Sub-additive tempo | — | — | Brooks's Law | Communication overhead |
| Structural adaptation | Model switching | Architecture search | Organizational restructuring | Major refactoring |

The persistence condition, for example, tells you that a software team must iterate fast enough, with good enough feedback, relative to how fast requirements are changing and how complex the codebase is. The same inequality, with different instantiations of α, ρ, and R, governs whether a Kalman filter tracks a maneuvering target, whether an RL agent converges in a nonstationary environment, and whether a military unit maintains situational awareness under adversarial deception.


## Convergent Choices

A category between "derived from first principles" and "arbitrary framework decision" — representational choices where all investigated alternatives fail or converge to the same structure:

**AND/OR node types for strategy.** Three independent formalism attempts (general CPT, noisy-OR, weighted combination) converged on AND/OR as the only workable basis. Noisy-OR was rejected for non-identifiability; weighted combination for parameter explosion (2^k vs. k). A parsimony theorem (AND/OR as the unique minimal complete basis under the theory's constraints) would promote this to "derived."

**Single-parameter edges.** Alternatives (multi-parameter credences, edge-specific distributions) were tried and abandoned. The convergence suggests this is not arbitrary but forced by the interaction between the uncertainty ratio principle and the chain-confidence identity.

**P3→Markov condition.** The postulate that strategy must be locally revisable, combined with temporal ordering and causal sufficiency, appears to force the Markov property on the strategy DAG. Currently conditional on causal sufficiency (which is guaranteed for agent-constructed strategies). If the conditioning can be removed, this promotes to a derived result — analogous to how acyclicity was once assumed and is now derived.

These sit between "we chose this" and "this is the only option." Tracking them separately from pure framework choices tells the reader: *we didn't just pick this; we tried everything else and it didn't work.*


## Maturity Gradient

The theory's mathematical closure varies by section, and this is by design:

**Section I (Adaptive Systems)** is mathematically closed. The recursive-update derivation, sector-condition Lyapunov proofs, persistence condition, and adversarial dynamics form a coherent chain with exact results, simulation validation, and an end-to-end Kalman worked example. This is the foundation everything else builds on.

**Section II (Actuated Adaptation: Agentic Systems)** has a strong diagnostic core (satisfaction gap, control regret, orient cascade ordering, directed separation) and a maturing operational layer. The strategy-persistence schema has four verified instances (single-edge, two-edge AND observable, two-edge AND unobservable at plan-level, two-arm OR with ε-greedy) confirming that the Lyapunov machinery extends to strategic dynamics with α_Σ = η_edge. Credit assignment is characterized at the theory level: persistence does not require it (Prop B.5), directional fidelity suffices for per-edge tracking (Level 1), exact attribution is #P-hard in general, and a gradient-based default signal function is provided. The specific update algorithm is domain engineering — parallel to how the gain principle provides η* while Kalman/TD-learning are implementations. Remaining open: signal function validation for continuous outcomes, the gradient signal's bias under correlated failures, and formalization of strategic disturbance rate ρ_Σ.

**Section III (Agentic Composites)** has the bridge lemma connecting closure defect to trajectory error, projection admissibility defined (P1: information preservation, P2: Lipschitz, P3: dimensionality reduction) with a two-Kalman exact instantiation, and norm specification for estimation-type agents (Mahalanobis). The bridge lemma is conditional on a contraction assumption (that sector-bounded correction implies contraction of the full update map) which is verified for Kalman-type agents but remains an independent assumption in general — this is the key gap for promotion. Unity dimensions, shared intent, and the Auftragstaktik principle remain qualitative. The cooperative/adversarial disturbance decomposition in team-persistence now explicitly separates communication-tempo benefits from action-based disturbance reduction to avoid double-counting. Main remaining gaps: N-agent scaling, strategy DAG projection, and the contraction assumption for general agents.

This gradient — from exact core through principled architecture to open formulation — is the expected arc for a theory that aims to describe agentic systems rather than produce a purely mathematical artifact.


## Where to Start

- **[`OUTLINE.md`](OUTLINE.md)** — Top-level assembly index across all parts.
- **[`01-aad-core/OUTLINE.md`](01-aad-core/OUTLINE.md)** — The AAD mathematical core, claim by claim.
- **[`LEXICON.md`](LEXICON.md)** — Prose vocabulary: cycle phases, agent classes, key terms.
- **[`WORKBENCH.md`](WORKBENCH.md)** — Development state: what's settled, what's open, known fragilities.
- **[`FORMAT.md`](FORMAT.md)** — Segment file conventions.
- **[`NOTATION.md`](NOTATION.md)** — Symbol reference.


## Project Layout

```
01-aad-core/            AAD mathematical core (Sections I, II, III + Appendices)
  OUTLINE.md            Theory outline (claim-by-claim)
  src/                  Claim segments (one per file, named by slug)

02-tst-core/            Temporal Software Theory (AAD-grounded)
  OUTLINE.md            Software theory outline
  src/                  Software domain segments

03-logogenic-agents/    Language-constituted agents (framework)
  OUTLINE.md            Logogenic framework outline

04-logozoetic-agents/   Language-living agents (future work)
  OUTLINE.md            Logozoetic framework outline

OUTLINE.md              Top-level assembly index
LEXICON.md              Prose vocabulary (spans whole project)
NOTATION.md             Symbol reference (spans all sections)
FORMAT.md               Segment file and general md conventions
WORKBENCH.md            Development state

msc/                    Working documents, spikes, derivation attempts
ref/                    Reference papers
bin/                    Build and lint tools

_obs/                   Superseded materials
```
