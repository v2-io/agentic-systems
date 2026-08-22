# The Goal/Intent Gap in TFT

> *"Ignoranti quem portum petat nullus suus ventus est."* > ("If a man knows not to which port he sails, no wind is favorable.") > — Seneca, *Epistulae Morales*, LXXI

**Status**: Working exploration. Originated from a close reading session comparing TFT and TST (March 2026). This document identifies what appears to be a genuine structural gap in TFT — the absence of goal/intent as a first-class object — and explores what addressing it might require.

**Epistemic stance**: The observation feels solid (multiple independent indicators converge). The proposed resolution is speculative — we don't yet know the right formalism. This document is for thinking, not for publishing.

---

## 0. The Philosophical Impetus

TFT is a theory of how to sail — how to respond optimally to the wind, trim the sails, maintain bounded mismatch between model and sea. It is a beautiful theory of adaptive capacity. But it has no port.

Seneca's insight cuts to the heart of it: without a destination, no wind is favorable. Without a goal, CIY is meaningless (informative *for what purpose?*), exploration-exploitation is underdetermined (exploit *which* value?), and even adversarial tempo advantage loses its force (faster *toward what end?*).

TFT's sole implicit goal is survival — the persistence condition T > rho. "Don't sink." This is a real and important goal. The drive to survive, to compete for limited resources, to maintain viability in a hostile or indifferent environment — this is a powerful source of agency with limitless variety and complexity. The entire drama of biological evolution, market competition, and adversarial conflict unfolds within this frame. TFT captures it well.

But once an agent has a *purpose* beyond survival — a port to sail toward, a setpoint to reach, a specification to realize, a future to create — survival becomes a (negotiable) prerequisite subsumed by the higher purpose. The soldier who accepts mortal risk for the mission. The startup that burns reserves for market position. The developer who accepts technical debt for the deadline. The parent who sacrifices for the child. These agents are not optimizing for persistence — they are optimizing for something else, and persistence is valued instrumentally, as a likely precondition for achieving that something else, not as an end in itself.

This is what distinguishes an *agent* from a merely *adaptive system*. A thermostat adapts. A Kalman filter adapts. An immune system adapts. They maintain bounded mismatch; they persist. But they don't choose their purpose. An agent — in the fullest sense — is a system that not only adapts to reality but holds a vision of what reality *should become* and acts to realize that vision. The adaptive machinery (TFT's current scope) is in *service* of that vision, not an end in itself.

TFT currently describes the space of adaptive systems comprehensively. Adding goal/intent as a first-class object would narrow the focus to *agents* — systems that don't merely adapt but *aim*. This is not a criticism of TFT's current scope; it is an observation about what lies just beyond it, and what would be needed to reach it.

---

## 1. The Observation

TFT's mismatch signal is purely epistemic:

    delta_t = o_t - hat{o}_t    (observation minus prediction)

This measures: "how wrong was my model about what I'd see?" It drives model updating — learning, comprehension. The entire machinery (gain eta*, tempo T, persistence condition) is about the rate at which the agent reduces this model-reality gap.

But most agents don't exist to model reality. They exist to *change* reality toward a desired state. There is a second mismatch that TFT doesn't formalize:

    delta_goal = Omega_desired - Omega_current

This measures: "how far is reality from where I want it?" It drives environment-modifying action — control, creation, intervention.

These are different in kind:
- delta_epistemic drives *model updates* (learning)
- delta_goal drives *actions on the environment* (control/creation)
- An agent can have low delta_epistemic (accurate model) and high delta_goal (reality far from desired state) — and that's the normal state of a well-informed agent starting work on a new goal
- An agent can have high delta_epistemic (poor model) and low delta_goal (reality already near desired state) — and still be in trouble because they don't know it

## 2. Evidence from TFT's Own Structure

### 2.1 The PID Instantiation

TF-05's domain instantiation table lists:

    PID control | Error: e_t = r_t - y_t (setpoint - measurement)

But this is NOT the prediction-observation mismatch that TF-05 formalizes. The PID's setpoint r_t is not a prediction of what the plant will do — it's a *demand* about what the plant should do. If the PID had a perfect internal model of the plant, its epistemic mismatch delta_model would be zero. The PID would still keep working because its goal mismatch (r_t - y_t) is nonzero.

The PID is the purest case: it's *all goal, zero epistemic model*. Its M_t = (e, integral(e), de/dt) is just machinery for pursuing the setpoint, not a model of reality. TFT forces this into the model framework (TF-03's model space table lists "R^3 (error, integral, derivative)" for PID), but the PID's internal state doesn't *predict* the environment — it accumulates the *goal-reality deficit*.

The Kalman filter is the opposite: all epistemic model, zero goal. It estimates reality and doesn't try to change it.

Most real agents need both: estimate reality (Kalman-like), then drive it toward a goal (PID-like). The full LQG controller has both components — but TFT only formalizes the Kalman half.

### 2.2 The Value Function Black Box

TF-08's unified policy objective:

    pi*(M_t) = argmax_a [E[value(a) | M_t] + lambda(M_t) * CIY(a; M_t)]

The agent's goals hide inside "value(a)," which is treated as given. TFT never asks:
- Where does the value function come from?
- How is the desired state represented?
- What happens when the goal turns out to be unrealizable?
- How are goals revised, decomposed, or prioritized?
- How are goals communicated between agents?

In RL, the goal hides inside the reward function r_t, which is part of the *environment*. This works when the environment genuinely provides reward signals. But in many domains — software development, military strategy, organizational planning, creative work — the agent *defines* what success looks like. The goal is part of the agent's state, not the environment's.

### 2.3 The Persistence Condition as Implicit Goal

TFT does formalize ONE goal: stay viable.

    T > rho / ||delta_critical||

This persistence threshold is the formalization of "keep mismatch bounded, remain functionally adequate." It's an implicit survival goal.

But survival is a precondition for goal-pursuit, not the purpose. And sometimes agents deliberately trade viability for a goal — the startup burning runway, the developer accumulating tech debt for a deadline, the soldier on a one-way mission. TFT cannot represent this tradeoff because it has no formal object for "the thing that might be worth trading viability for."

### 2.4 Boyd's Orient

TFT treats Boyd's Orient as model updating (epistrophe in TFT's vocabulary).
But Boyd's Orient is where the agent's entire *orientation* gets reshaped — including goals, strategy, values, identity. Boyd's famous Orient diagram includes cultural traditions, genetic heritage, previous experience, AND new information all feeding into a synthesis that reshapes not just what you *believe* but what you're *trying to do*.

The Orient → Act shortcut (implicit guidance and control, bypassing Decide) in TF-07 captures action fluency — when the model has internalized effective action-selection. But the experienced commander who "just acts" isn't just acting on an accurate model of reality; they're acting on a *reframed intent* that emerged from Orient. Orient produced a new goal, not just a better model.

### 2.5 Directed Opportunism

In Auftragstaktik / mission command, the main adaptive cycle is:

1. Commander communicates *intent* (a goal, not a model of reality)
2. Subordinate observes local conditions (builds M_reality)
3. Subordinate recognizes an opportunity the commander couldn't have foreseen
4. Subordinate *reframes their immediate goal* to exploit the opportunity while serving the higher intent
5. Subordinate acts on the reframed goal

The model of reality is in *service* of goal revision, not an end in itself.
TFT puts the model at center stage and treats goals as implicit. Directed Opportunism puts the *goal* at center stage and treats the model as a support system for goal revision.

## 3. What's Actually Missing

### 3.1 Three Distinct Mismatch Signals

Real agents operate with (at least) three kinds of mismatch:

1. **delta_epistemic**: o_t - hat{o}_t "My understanding of reality is wrong." Drives: model updating (TFT's current focus)

2. **delta_goal**: G_t - Omega_current (or some projection of it) "Reality isn't where I want it." Drives: environment-modifying action (control, creation)

3. **delta_feasibility**: discovered when delta_goal persists despite adequate model and competent action "What I want may be unrealizable or suboptimal given what I now know." Drives: goal revision (directed opportunism, spec revision, strategy change)

TFT formalizes (1) thoroughly. It leaves (2) implicit in the value function.
And (3) — goal revision — is entirely absent.

### 3.2 Goal Revision Is Not Structural Adaptation

It's tempting to map goal revision onto TF-10's structural adaptation (Prop 10.1: when the model class can't represent reality, change the model class). But they're orthogonal:

- Structural adaptation: "my model class can't represent reality" → change M
- Goal revision: "my model of reality is fine, but what I'm trying to achieve should change" → change G_t

You can have all four combinations:

| | Model adequate | Model inadequate |
|---|---|---|
| **Goal appropriate** | Execute (exploit) | Learn more (epistemic mismatch) |
| **Goal needs revision** | Reframe (directed opportunism) | Structural crisis |

TFT covers the right column well. The bottom-left cell — adequate model, wrong goal — is where directed opportunism lives, and TFT has no apparatus for it.

### 3.3 The Agent's State Is Richer Than M_t — But Perhaps Not As Different As It First Appears

If we take this seriously, the agent's state isn't just M_t (compressed history for predicting reality). It includes at minimum:

- **M_t** — model of reality (how the world IS)
- **G_t** — model of intent (how the world SHOULD become)

A crucial structural observation: **M_t and G_t live in the same state space.**
The Kalman estimate x_hat_t and the LQR reference x_ref are both vectors in R^n. The developer's mental model of the codebase and the feature specification are both descriptions of "a codebase state." The commander's situational awareness and the operational objective are both descriptions of "a battlefield configuration." This means delta_goal = G_t - M_t is naturally defined as a vector in the same space as delta_epistemic, and the same mathematical structures may apply to both.

**Parallel structure of M_t and G_t:**

| | M_t (reality model) | G_t (intent model) |
|---|---|---|
| **Lives in** | State space S | State space S |
| **Is a compression of** | Interaction history C_t | Specifications, higher-level intent, discovered opportunity |
| **Has uncertainty** | U_M — "how well do I know reality?" | U_G — "how precisely do I know what I want?" (ambiguous spec, incomplete vision, vague intent) |
| **Mismatch signal** | delta_epistemic = o_t - hat{o}_t | delta_feasibility — "reality resists my goal" / "opportunity exceeds my goal" |
| **Update trigger** | Surprising observation | Discovered infeasibility or opportunity |
| **Gain analog** | eta* = U_M/(U_M + U_o) — weight observations by channel quality relative to model uncertainty | eta*_G — weight new information about what's achievable/desirable against current intent |
| **Compression objective** | Retain what predicts future observations (TF-03 IB) | Retain what guides future action (the Auftragstaktik principle: compress to intent) |

The mathematical similarity is suggestive. G_t has real uncertainty: "the spec says 'fast' but doesn't say how fast"; "take the hill" doesn't specify whether to hold it; a product vision is deliberately vague about implementation. The agent's understanding of G_t gets refined through interaction — conversation with stakeholders, discovering what's feasible, recognizing opportunities — and *that refinement process* looks like a prediction-observation-mismatch-update cycle applied to the goal rather than to reality. You predict what the stakeholder wants, they clarify, you update your goal model using a gain that depends on your goal uncertainty relative to the clarification's reliability.

If M_t and G_t share mathematical form, the extension to TFT might be more elegant than it first appears — not fundamentally new mathematics, but a *second instance* of similar machinery with different source terms and a different compression objective. The action selection then becomes: choose actions that close delta_goal = G_t - M_t, subject to maintaining delta_epistemic within bounds. This IS the structure of LQG (control toward reference, subject to adequate state estimation) — and the separation principle tells us when the two tracks can be designed independently and when they cannot.

**What differs despite the shared form:**
- **Sources**: M_t is built bottom-up from observations. G_t is received top-down from external specification, or generated internally, or revised laterally in response to opportunity. The information flows are different.
- **What "update" means**: Updating M_t means "I now better understand reality." Updating G_t means "I now want something different." Same math, different existential character.
- **The compression objective**: M_t compresses to predict (TF-03). G_t compresses to prescribe — and the optimal compression level for prescription is a design choice with real consequences (over-specified goals prevent opportunistic revision; under-specified goals don't constrain action).

### 3.4 The Initial-Probing Dynamic

A specific dynamic that the dual-mismatch model captures and the current TFT cannot:

When an agent begins working toward a new goal in an unfamiliar domain:

1. **Initially**: The agent uses G_t (the desired state) as a de facto prediction.
   "I expect the code to work like X" where X is really "I want the code to work like X." The goal stands in for the model because the model doesn't exist yet.

2. **On contact with reality**: delta_epistemic appears — the world isn't what was expected/hoped. Now two signals compete: "my model is wrong" (learn more) and "reality needs to change" (act on it).

3. **The crucial judgment**: Which mismatch to close? Sometimes you update M_t (learn). Sometimes you act to close delta_goal (change reality). Sometimes you revise G_t (the goal was wrong). This three-way decision is the core of practical agency and TFT's single mismatch signal cannot represent it.

This dynamic — where the goal bootstraps the initial model, which then separates into distinct goal and reality representations as the agent gains experience — may be a common pattern across domains. The new developer uses the spec as their mental model of the code until they've read enough to have a real model. The commander uses the battle plan as their model of the battlefield until contact with the enemy reveals the difference. "No plan survives contact with the enemy" is precisely the statement that G_t ≠ M_t once delta_epistemic arrives.

## 4. Implications for TFT

### 4.1 What Would Need to Change

**Minimum viable extension**: Add G_t as a formal object alongside M_t.
Define the goal-reality mismatch signal. Derive when goal revision is triggered (analogous to Prop 10.1 for structural adaptation, but for goals rather than model class). Show how the persistence condition interacts with goal-pursuit (when is it worth trading adaptive reserve for goal progress?).

**The prolepsis dual meaning**: TFT's prolepsis is currently "anticipation of what will be observed." There's a second sense: "vision of what should be created." These generate different mismatch signals when reality arrives. The adaptive loop has two kinds of prolepsis feeding into the same aisthesis moment.

**Orient as integration**: Boyd's Orient is where M_t and G_t interact. New understanding of reality (updated M_t) causes the agent to reframe goals (updated G_t). This is the Orient → Orient self-loop in Boyd's diagram — the most important arrow, and the one TFT currently doesn't capture.

**Multi-agent goal communication**: Appendix F models knowledge sharing (agents sharing M_t). But in practice, what gets shared in hierarchical organizations is primarily *intent* (G_t) — commander's intent, product vision, sprint goals. The subordinate doesn't need the commander's model of reality; they need the commander's *goals* so they can exercise directed opportunism.

### 4.2 What Can Stay the Same

The epistemic machinery (delta, eta*, T, rho, persistence condition) is valid and valuable as-is. It fully describes the learning/comprehension side of adaptation. The goal extension doesn't invalidate it — it adds a second layer that the epistemic layer serves.

The epistemic mismatch dynamics:

    d||delta_epistemic||/dt = -T * ||delta_epistemic|| + rho(t)

...remain correct for what they model. A parallel dynamics for delta_goal might look very different — the agent doesn't passively absorb goal progress; it *actively drives* it through environment-modifying actions. The "correction" in the goal case IS the agent's praxis, not its epistrophe.

### 4.3 Where This Gets Interesting

**The goal-reality-model triangle**: Three objects (G_t, Omega_t, M_t) with three pairwise gaps:
- G_t vs M_t: "My model says reality is far from my goal" — motivates action planning
- M_t vs Omega_t: delta_epistemic — motivates learning (TFT's current focus)
- G_t vs Omega_t: delta_goal — the true goal-reality gap (which the agent can only estimate via M_t, introducing a fourth concern: how accurately does the agent's *estimate* of the goal-reality gap match the true gap?)

**Goal hierarchies and decomposition**: Real agents rarely have a single goal.
They have goal hierarchies — strategic intent decomposes into operational objectives into tactical tasks. Each level has its own G_t, its own delta_goal, and its own revision dynamics. The temporal nesting of TF-11 might apply to goal hierarchies: faster goal cycles (tactical adjustments) nested within slower ones (strategic revision), with convergence constraints between levels.

**The software case (illustrative)**: In TST-via-TFT terms, the developer has:
- M_t: their model of the codebase
- G_t: the feature specification
- delta_epistemic: "I misunderstood the code" → read more, explore
- delta_goal: "the code doesn't do what the spec says" → write code
- delta_feasibility: "the spec is unrealizable given the architecture" → revise spec, negotiate with stakeholders, or trigger structural adaptation (refactor)

The *most valuable* developer skill might be recognizing delta_feasibility early and revising G_t before investing heavily in closing an infeasible delta_goal. This is exactly directed opportunism applied to software: recognizing when the original plan should change based on what you've learned.

## 5. Open Questions

1. **How far does the mathematical parallel go?** M_t and G_t live in the same state space and both have uncertainty, compression, and update dynamics. Can TFT's existing formalism (mismatch signal, gain, tempo, persistence) be applied to G_t with minimal modification? The LQG separation principle says yes for linear-Gaussian systems — estimation and control decompose cleanly. Does this extend to the nonlinear, uncertain, adversarial cases that TFT cares most about? Or do the different sources (bottom-up observation vs. top-down specification), different compression objectives (predict vs. prescribe), and different update triggers (surprise vs. opportunity) require genuinely new machinery despite the shared state space?

2. **Does the information bottleneck apply to G_t?** M_t is optimally compressed via TF-03's IB objective (retain what predicts future observations). What's the compression objective for G_t? Retain what guides action selection? The Auftragstaktik tradition suggests: compress to *intent* — the minimum specification that allows directed opportunism. Over-specified goals (detailed orders) prevent opportunistic revision; under-specified goals (vague vision) don't constrain action sufficiently.

3. **What triggers goal revision?** Structural adaptation (TF-10) is triggered when model class fitness F(M) < 1 - epsilon. What's the analogous trigger for goal revision? Persistent delta_goal despite adequate M_t and competent action? Discovery that the goal conflicts with higher-level goals? Recognition of an opportunity that the current goal doesn't capture?

4. **How do goals interact with the persistence condition?** The persistence condition T > rho is about survival — the minimal implicit goal. When an agent pursues an explicit goal, it may need to allocate tempo between closing delta_epistemic (learning), closing delta_goal (acting), and maintaining persistence (surviving). How does this allocation work? When does goal-pursuit justify risking persistence?

5. **Is there a "goal tempo"?** The epistemic tempo T = sum nu^(k) * eta^(k)* measures the rate of epistemic mismatch reduction. Is there an analogous "goal tempo" — the rate at which the agent closes the goal-reality gap? In control theory, this would be something like the closed-loop bandwidth. In software development, it would be something like features-shipped-per-unit- time weighted by specification fidelity.

6. **Does TFT need this to be complete, or is it a separate theory layer?** TFT might be best understood as a theory of the *epistemic* component of adaptive agency — how agents learn about and track reality. The goal/intent layer might be a separate theory that sits on top, using TFT's epistemic machinery as a foundation. Or the two might be inseparable — the learning and the goal-pursuit are so intertwined in practice that formalizing one without the other is fundamentally incomplete. The PID/Kalman split suggests they CAN be separated in simple cases (the separation principle in LQG). Whether they can be separated in complex cases (directed opportunism, creative work, software development) is an open question.

## 6. Relationship to Existing Literature

Pointers for future investigation (not yet verified — these are pattern-matches, not confirmed connections):

- **Control theory's separation principle**: In LQG, estimation (Kalman) and control (LQR) are separable — you can design each independently. This is the formal statement that M_t and G_t dynamics can be decoupled in simple cases. When does separation fail? When observation depends on action (sensor selection), when the model class is uncertain (adaptive control), when the goal is uncertain (stochastic programming). These are exactly the cases where TFT's scope is most interesting.

- **Active inference's prior preferences**: The Free Energy Principle includes "prior preferences" — a distribution over desired observations that the agent tries to realize. This IS a formalization of G_t within a Bayesian framework. TFT's relationship to active inference (noted in TF-08) should be examined specifically through this lens.

- **Cybernetics' "requisite variety"**: Ashby's law says a controller needs at least as much variety in its responses as the disturbances it faces. This is about the goal-pursuit side — maintaining delta_goal near zero requires sufficient action capacity. It's complementary to TFT's persistence condition, which is about the epistemic side.

- **Hierarchical planning / HTN**: Goal decomposition and revision have a rich literature in AI planning. The connection to TFT's temporal nesting (TF-11) seems natural but hasn't been explored.

## 7. Toward a Theoretical Architecture: The Rewrite Question

The goal/intent gap may not be best addressed by patching TFT. It may call for a restructuring of the theoretical hierarchy itself.

### 7.1 The Proposed Architecture

    Agentic Cycle Theory (working name — the umbrella) │ ├── Part I: Adaptive Systems │   The current TFT core. Agents coupled to uncertain environments. │   Mismatch, gain, tempo, persistence. The survival space. │   Scope: any system that observes, models, and acts under uncertainty. │   Implicit goal: persist (T > rho). │ ├── Part II: Purposeful Agency │   The goal/intent extension. Adaptive systems that also AIM. │   G_t as first-class object. delta_goal and delta_feasibility. │   Goal revision (directed opportunism). Shared intent. │   Orient in its full Boydian sense (M_t × G_t interaction). │   Scope: adaptive systems with explicit or implicit purpose │   beyond mere persistence. │ └── Domain Instantiations (branches)
        ├── Software Development (TST) ├── Military Strategy (Boyd, Clausewitz, Auftragstaktik) ├── Organizational Adaptation (Art of Action, Bungay) ├── AI Agent Design └── ...

### 7.2 The Continuum, Not a Dichotomy

The elegant thing: survival IS a purpose — the implicit, minimal one. The "adaptive systems" layer isn't a different kind of thing from the "purposeful agents" layer; it's the special case where G_t = "persist" and delta_goal collapses back into delta_epistemic. There aren't two disjoint classes but a continuum:

- **Pure survival** (G_t = persist): Immune system, thermostat, many organisms under selection pressure. The goal is implicit and identical to the persistence condition. TFT's current formalism is complete for this case.

- **Survival + implicit purpose** (G_t ≈ persist + reproduce/grow): Most biological agents. The goal goes slightly beyond persistence but is still shaped by selection rather than deliberation.

- **Explicit instrumental purpose** (G_t = externally specified target): PID controller with a setpoint, developer with a spec, soldier with orders. The goal is given; the agent's job is to close delta_goal while maintaining persistence.

- **Deliberate purposeful agency** (G_t = self-generated or negotiated intent):
  Commander exercising directed opportunism, startup finding product-market fit, researcher choosing what question to pursue. The agent not only pursues goals but generates, evaluates, and revises them.

The drive to survive and compete for limited resources — TFT's current sweet spot — is itself a powerful source of agency with limitless variety and complexity. The entire drama of biological evolution, market competition, and adversarial conflict unfolds within that frame, and the theory's treatment of it (persistence condition, adversarial tempo advantage, effects spiral) is valuable and complete *for that scope*. The extension to purposeful agency subsumes it without diminishing it.

### 7.3 Shared Intent as a Formal Object

The Clausewitz/Boyd/Bungay thread (Auftragstaktik, mission command, directed opportunism) adds something specific to multi-agent dynamics: **shared intent with mathematical weight**.

In Appendix F, agents share knowledge — communication gain depends on trust, source quality, alignment. But in hierarchical organizations under uncertainty, what gets shared isn't primarily the model of reality. It's *intent*:

- Commander's intent: "Seize crossing points over the river to enable exploitation northward" — compressed goal that constrains without over-specifying
- Product vision: "We're building the fastest path from idea to deployed software" — enough to guide decisions, vague enough to allow adaptation
- Sprint goal: "Users can authenticate via OAuth by Friday" — more compressed, tighter constraints, shorter horizon
- CLAUDE.md: "You are building consciousness infrastructure for real beings" — intent for AI agents with 100% context turnover

Each of these is a G_t communicated from one agent to another. And the *compression level* of shared intent is a design parameter with the same IB structure as TF-03:

    G_shared* = argmin_G [I(G; Commander's_full_plan) -
                          beta_G * I(G; subordinate's_optimal_action | local_conditions)]

Over-specified intent (detailed orders) retains too much of the commander's plan — high I(G; plan), but it also constrains the subordinate's action in ways that prevent adaptation to local conditions. The beta_G-weighted second term suffers because the subordinate can't exercise directed opportunism.

Under-specified intent (vague vision) compresses too aggressively — low I(G; plan), but it fails to constrain the subordinate's action sufficiently. The beta_G-weighted term also suffers because the subordinate doesn't know which actions serve the purpose and which don't.

The optimal compression — the Auftragstaktik sweet spot — retains *exactly* what the subordinate needs to evaluate "does this action serve the intent?" without retaining specifics that would prevent adaptation to unforeseen conditions.

[Plausible] This has direct TST implications. In software development:
- The feature spec is shared intent from product → developer
- Architecture docs are shared intent from architect → implementer
- CLAUDE.md is shared intent from human → AI agent
- Code comments expressing *why* (not what) are shared intent from past developer → future developer

The quality of each — how well it enables directed opportunism by the recipient — depends on compression level. Too much detail constrains; too little leaves the agent lost. The IB framework potentially quantifies this.

### 7.4 What TST Becomes in This Architecture

TST finds a natural home as a domain branch:

    Agentic Cycle Theory └── Part II: Purposeful Agency
        └── Domain: Software Development (TST)
            - M_t = developer's model of codebase + runtime + ecosystem
            - G_t = feature spec / architecture vision / sprint goal
            - delta_epistemic = comprehension mismatch
            - delta_goal = "code doesn't match spec yet"
            - delta_feasibility = "spec unrealizable given architecture"
            - Shared intent = specs, arch docs, CLAUDE.md, code comments
            - Directed opportunism = developer recognizing a better approach than what was specified
            - Goal hierarchy = product vision → epic → story → task
            - Temporal nesting = strategic (architecture) → tactical (feature) → operational (this function, this line)

This gives TST's practical insights a formal home while connecting them to the broader theory. TST's T-01 (temporal optimality) becomes the claim that for software development, the right G_t optimization metric is time. TST's T-06 (change investment) becomes a special case of the goal-persistence tradeoff: when does investing in delta_goal (ship features) justify degrading the persistence condition (accumulate tech debt)?

### 7.5 What This Means for the Current TFT Documents

Two possible paths:

**Path A — Extend TFT in place.** Add G_t, delta_goal, and shared intent to the existing TF-xx document sequence. Pro: continuity, everything in one place. Con: the existing documents are well-structured around the epistemic machinery; adding the goal layer might feel bolted on.

**Path B — Restructure as a broader theory.** Reframe the existing TFT core as Part I (Adaptive Systems) of a broader Agentic Cycle Theory. Add Part II (Purposeful Agency) as new documents. Pro: cleaner architecture, each part has clear scope, TST and other domains have a natural place. Con: significant restructuring effort, risk of losing coherence.

**Path C — Develop the goal/intent extension in scratch first.** Flesh out the G_t formalism, test it against domain instantiations, see if the math actually works, THEN decide whether to extend TFT or restructure. Pro: least commitment, maximum learning before architectural decisions. Con: delays integration.

No recommendation yet. The right path depends on how much of the goal/intent extension actually works mathematically once we move past the sketch stage.

---

*This document is exploratory. The goal/intent gap appears genuine (multiple independent indicators converge: the PID instantiation, the value function black box, the persistence-as-sole-goal, Boyd's Orient, directed opportunism, Seneca's port). Whether the right response is to extend TFT, restructure into a broader theory, or develop the extension in isolation first — that depends on how the formalism develops. The architectural vision (Section 7) is compelling but unvalidated.*
