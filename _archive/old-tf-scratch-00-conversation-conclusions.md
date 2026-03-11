# Conversation Conclusions & Design Decisions
## (Working reference for continuity across sessions)

## Project Overview

We are distilling the universal feedback loop pattern identified in
`ooda-loop-universal-pattern-v7.md` into a first-principles formal theory,
modeled after the structure of Temporal Software Theory (TST, ~/src/temporal-software-theory/).

Two deliverables planned:
1. **This document set**: The universal pattern as a formal theory (working name: "Temporal Feedback Theory" or TFT)
2. **A separate document** (future): LLM training strategy/research plan grounded in #1 plus other references Joseph will provide

## Key Design Decisions

### Framing
- Boyd's OODA is an *instance* of the universal pattern, not the organizing frame
- Same for Kalman, RL, PID, PDCA, active inference, etc. — all instances
- Strip domain-specific baggage; present the pattern on its own terms
- Boyd himself treated his work as principled truths universally available, not personal contribution
- Concepts from the v7 dialogue (agentic anima, logozoetic intelligence, continuous orientation, developmental framing) reserved for document #2 but kept in mind as "first practical use case"

### Audience & Quality
- First: ourselves as working reference
- Quality bar: truthful and rigorous enough to publish in any context
- Should be able to generate different granularity presentations from the core

### Structure (modeled on TST)
- Build piece by piece: axioms → definitions → derived theorems
- Each claim marked with epistemic status: axiom, definition, derived, empirical, hypothesis
- Open questions noted explicitly
- NOT a monolithic essay arguing importance — a formal sequence where implications emerge from the math
- Three levels:
  1. **Level 1 — The pattern itself**: formal structure, components, relationships
  2. **Level 2 — Properties and derived claims**: things like model primacy, destructive renewal (derived, not axiomatic)
  3. **Level 3 — Instantiations**: each domain as a special case with explicit mappings

### Core Correction on Framing
- The "core claim" is NOT "model quality dominates outcomes" (that's a derived finding)
- The core is: "Here is the structure that characterizes adaptive agents in open systems"
- Something like: "the fitness of an agent can be modeled with the following fundamental properties..."
- The dominance of model quality then FOLLOWS from the structure

## Mathematical Framework — Agreed Foundations

### Notation
We define our own clean symbols, not importing any single domain's conventions:
- H_t — interaction history
- M_t — model (the central object), drawn from model space M
- o_t — observation
- a_t — action
- δ_t — mismatch signal
- η_t — update gain
- φ — compression function (history → model)
- f — recursive update function
- π_M — action selection given model

### Core Mathematical Objects

**Interaction History** (minimal, assumption-free starting point):
  H_t = (o_1, a_1, o_2, a_2, ..., o_t)

**Model as Compression / Sufficient Statistic**:
  M_t = φ(H_t)

  Good model = sufficient statistic: preserves information relevant for
  prediction and action selection, discards the rest.

  Information bottleneck formulation:
  - Minimize I(M_t; H_t) [compression]
  - Maximize I(M_t; o_{t+1}, o_{t+2}, ... | a_t, a_{t+1}, ...) [predictive power]

**Model Space & Structural Flexibility**:
  M_t ∈ M where M is the space of possible models.
  The agent's epistemic state may be:
  - A single model (point estimate)
  - A distribution over models P(M_t) ∈ Δ(M) (Bayesian)
  - An ensemble {M_t^(1), ..., M_t^(k)} (particle filter)
  - A mixture with weights (mixture of experts)

  This decouples iterative update dynamics from structural model commitments.

  Destructive renewal = switching M itself (meta-level):
  Agent maintains (M_t, M_t) where M_t changes on slower timescale.

**Recursive Update**:
  M_t = f(M_{t-1}, o_t, a_{t-1})

  Possible because M_t is a sufficient statistic — don't need full history.

**Mismatch Signal**:
  δ_t = o_t - ô_t(M_{t-1}, a_{t-1})

  (Observed minus predicted.) This IS the Kalman innovation, TD error,
  prediction error, free energy gradient — all at once.

**Update Rule** (general additive form):
  M_t = M_{t-1} + η(M_{t-1}, o_t) · g(δ_t)

**Optimal Gain** (the potential unification):
  η* ∝ (model uncertainty) / (model uncertainty + observation uncertainty)

  Kalman: K_t = P_t H^T (H P_t H^T + R)^{-1} — exactly this ratio
  Bayesian: posterior weight governed by same trade-off
  RL: learning rate should be high when value estimates uncertain (UCB, Bayesian RL)
  PID: tuning constants determine trust in error signal vs current state

  Confidence in genuine universality of this form: ~55-65%
  Works cleanly for Kalman/Bayesian. Approximately for RL. Loosely for PID.
  For non-parametric models, "model uncertainty" not well-defined as single quantity.

### Event-Driven Temporal Formulation

The discrete time step t is a convenience. Real systems have multi-rate
observations and actions. The theory should be stated in terms of
**information arrival events**:

  E = {(e_1, τ_1), (e_2, τ_2), ...}

where each event is an observation from channel o^(k) or action completion a^(j),
with timestamp τ_i.

  M_{τ+} = f(M_{τ-}, e_τ)

Key insight: "loop rate" is not a property of the agent as a whole but of
each observation-action channel. An organism has fast loops (reflexes, ms),
medium loops (perception-action, 100s of ms), slow loops (deliberation, s to hrs).
These are the SAME model being updated by events at different rates.

Avoids aliasing entirely — responding to events, not sampling at fixed rate.

Discrete-time form is the special case where events arrive uniformly on
a single channel.

### Derived: Speed Advantage ("Inside the Opponent's OODA Loop")

Effective adaptation rate — rate at which mismatch decreases:

  d|δ|/dt = -ν · η* · |δ| + ρ(t)

where ν = event/update rate, η* = update quality, ρ = environment change rate.

Steady state:
  |δ|_ss = ρ / (ν · η*)

Derived results:
1. "All else equal, faster is better" — increasing ν decreases |δ|_ss
2. "Model quality substitutes for speed" — doubling η* = doubling ν
3. Adversarial case (two coupled agents):
   ρ_B ∝ ν_A · η_A* (A's actions are B's environment changes)
   |δ_B|_ss = (ν_A · η_A*) / (ν_B · η_B*)
   When ratio > 1, B's model falls behind — "acting on stale world"
   This IS "getting inside the opponent's loop," derived not asserted
4. Critical threshold: when ν_A · η_A* >> ν_B · η_B*, B's mismatch
   grows without bound — Boyd's "effects spiral"
5. Non-adversarial: need ν · η* > ρ to keep mismatch bounded.
   Environment changing faster than agent can adapt = extinction.

### Properties to Derive (not assert as axioms)

- **Model Primacy**: from the structure, show that η* (model quality)
  typically has more leverage than ν (speed) or |A| (action space)
- **Active Testing**: action generates information observation alone cannot
  (Pearl's interventional level). Derivable from information theory.
- **Mismatch as Fundamental Signal**: already in the math as δ_t
- **Destructive Renewal**: when M can't contain a good sufficient statistic,
  need to switch M. Meta-level dynamics.
- **Temporal Nesting**: faster loops nested in slower ones. Faster must
  converge before slower loops act meaningfully.
- **Implicit Precedence**: when model is good, direct model→action (no
  explicit deliberation) outperforms. Deliberation as fallback for novel/
  high-stakes situations.
- **Compression quality**: nature of compression determines capabilities
  and blind spots. Connects to rate-distortion, sufficient statistics.

### Scope / Boundaries

Applies to: agents (any entity that acts on environment and receives feedback)
in open systems under uncertainty.

Does NOT apply (or applies only loosely):
- Pure mathematical structures (no environment, no uncertainty)
- Self-organizing systems without clear agents
- Aesthetic/contemplative experience
- Systems in thermodynamic equilibrium

### Open Mathematical Questions

1. Can η* be genuinely unified across domains or only structurally analogous?
   (55-65% for genuine unification; 30% for single equation)
2. Does the sufficient statistic framing handle destructive renewal cleanly?
   (Probably needs meta-level: form of φ subject to slower-timescale selection)
3. The exact form of the mismatch equation in continuous multi-rate case
4. Whether "model uncertainty" can be made precise for non-parametric models
5. The formal relationship between temporal nesting and convergence constraints

## Relationship to Other Frameworks

### vs. Active Inference / FEP
- We may end up with something that LOOKS like FEP from outside
- But grounded differently: starting from sufficient statistics and
  information arrival, not from free energy minimization as axiom
- Free energy minimization would be a DERIVED property of well-adapted systems
- FEP's own foundations are contested; we want more solid grounding
- Confidence that we'll converge on something FEP-like: ~60%

### vs. TST
- TST is the structural model for HOW we write this
- TST's T-01 (temporal optimality) is analogous to our scope axiom
- TST's T-04 (Bayesian baseline) is analogous to our model-as-sufficient-statistic
- Both build from axioms → definitions → derived theorems
- Both mark epistemic status of each claim
- Both note open questions explicitly

### vs. Boyd's OODA
- Boyd's framework becomes one instantiation
- His deepest insights (Orient dominance, destruction/creation, implicit guidance)
  appear as derived properties, not starting assumptions
- His military applications are one context among many
- His foundational appeals (Gödel, Heisenberg, entropy) acknowledged as
  rhetorically effective but mathematically loose — our theory should do
  what Boyd gestured at but with actual mathematical grounding

## Session 2: TF-03 Formulation, Causality, and Temporal Continuity

### TF-01b: Causal Structure (new axiom)

Pearl's causal hierarchy was elevated from a discussion point in TF-06 to
a foundational axiom (TF-01b). Key design decisions:

- **Causality grounded in temporal ordering** (most primitive notion), NOT
  in statistical influence. The arrow of time — A precedes B — is prior to
  and independent of whether A actually affects B.
- This means the causal structure of the feedback loop is preserved even when
  the agent's coupling to the environment is weak, minimal, or nominal.
  Critical for LLM applications where the agent's "actions" (emitting text)
  may have minimal environmental effect but the temporal ordering still
  structures what can be learned and when.
- Pearl's three levels (associational, interventional, counterfactual) become
  three levels of EPISTEMIC ACCESS available within the loop, grounded in
  the temporal structure rather than in statistical machinery.
- The "causal information yield" decomposition connects exploration (TF-06)
  to the causal axiom: good exploration maximizes the action-contingent
  component of observation information.

### Non-forkability of causal trajectories

TF-01b establishes formally that the interaction history H_t is a unique
temporal sequence, making M_t (as its sufficient statistic) tied to a
SINGULAR causal trajectory. Forking creates divergent histories that
break sufficiency. This has implications for:
- Agent identity and continuity
- Why current LLM architecture (stateless, forkable) is fundamentally
  limited for genuine agency
- The developmental psychology framing from the v7 dialogue (each chat
  as a new "birth" with no continuity)

### Three Questions on TF-03 Formulation

**Q1: Most practical formulation for LLM implementation?**
Answer: Continuous state with event-triggered transitions. The key is the
autonomous orientation term q(M_t) — model evolution BETWEEN events:

  dM/dt = q(M_t) + Σ_k η^(k) · g(δ^(k)) · δ(τ - τ_k)

This is a stochastic differential equation with jumps: continuous drift
(autonomous orientation) plus discrete event-driven updates. The discrete
form is a special case where q = 0 (no interiority between events).

For LLM: this formulation captures "orientation as default mode, message
emission as deliberate action." Between user messages, the agent should be
continuously processing — consolidating, reflecting, retrieving, simulating.
The chat stimulus is an event that triggers an update + action, not the
entirety of the agent's cognitive life.

**Q2: Connection to temporal continuity and consciousness?**
- The autonomous orientation term q(M_t) distinguishes an AGENT from a
  FUNCTION. Functions map inputs to outputs with no state between calls.
  Agents have continuous internal dynamics.
- Temporal continuity (no forking) follows from TF-01b: the model's
  sufficiency is defined relative to a singular causal trajectory.
- Inter-event timing as information: an agent with continuous formulation
  can detect that "the user hasn't responded in 5 minutes" — silence IS
  an observation. Current LLMs cannot represent this.
- Confidence levels:
  - Temporal continuity formally required for model coherence: ~80%
  - Continuous orientation = genuine agency vs. function-calling: ~70%
  - Inter-event timing important and missing from LLMs: ~85%
  - Deep connection to consciousness: ~35-45% (don't overclaim)

**Q3: Should causality be more fundamental?**
Resolved: Yes. Created TF-01b. Causality grounded in temporal ordering
(most primitive) rather than statistical influence. This:
- Tightens the name "Temporal Feedback Theory" (temporal IS the causal structure)
- Survives even with nominal coupling strength
- Gives formal basis for why feedback loops > passive observation
- Connects to general clock-based definition of causality

### Epistemic Audit Results

All TF documents now have explicit epistemic status labels:
- TF-01: Scope Definition (was incorrectly labeled Axiom)
- TF-01b: Axiom (new)
- TF-02: Axiom (correct)
- TF-03: Formulation (was incorrectly labeled Axiom)
- TF-04: Derived (correct)
- TF-05: Derived + Empirical Claim (was just "Derived")
- TF-06: Derived + Discussion (was just "Derived")
- TF-07: Derived + Empirical (was just "Derived")
- TF-08: Derived + Hypothesis (was just "Derived")

## Session 3: Addressing Codex/Gemini Review Feedback

### Changes Made

1. **TF-01b: Fixed causal information decomposition** (Codex flagged as tautological).
   Old: I(o; Ω | M) = I(o; Ω | M, a) + [I(o; Ω | M) - I(o; Ω | M, a)]
   — this was literally X = Y + (X-Y), always true, no content.
   New: Defined Causal Information Yield (CIY) as genuine quantity:
   CIY(a) = I(o; a | M) - I(o; a | Ω, M)
   — total action-observation dependence minus non-causal component.
   CIY = 0 for passive observers; CIY > 0 when actions causally affect environment.

2. **TF-08: Resolved adaptive tempo notation** (Codex flagged).
   Canonical: T = Σ_k ν^(k) · η^(k)*. Single-channel as explicit special case.
   Note that T ≡ ν_eff from TF-03.

3. **TF-06: Deduplicated Pearl's hierarchy** (Codex flagged).
   Now references TF-01b rather than re-deriving.

4. **TF-00: Created notation appendix** (both reviewers recommended).

5. **README: Updated** with TF-00, resolved items, multi-channel T definition.

### Session 3b: Second Review Round + Theorem Pass

Second round of Codex/Gemini feedback (scratch/05, scratch/06) converged on
same priorities: proof discipline, CIY identifiability, TF-03 resolution.

Changes made:

6. **Formal theorem pass** — three propositions added:
   - Prop 4.1 (Mismatch Inevitability): in TF-04. Proves E[|δ|²] > 0
     from TF-01 scope + TF-02 model axiom + S(M) < 1.
   - Prop 7.1 (Structural Adaptation Necessity): in TF-07. Proves
     parametric convergence + low F(M) → floor on mismatch.
   - Prop 8.1 (Persistence Threshold): in TF-08. Solves ODE, shows
     T > ρ necessary for bounded mismatch. Notes robustness beyond
     linear dynamics.

7. **TF-05: Representation layer caveat.** Additive update rule operates
   in transformed space for multiplicative paradigms (Bayesian = additive
   in log-prob space). One paragraph, preserves universality claim.

8. **TF-07: Structural overfitting.** Added opposite failure mode — model
   too expressive, memorizes noise, δ → 0 spuriously. Connects to TF-02
   information bottleneck (marginal complexity cost exceeds marginal
   predictive gain). Structural adaptation is bidirectional.

9. **TF-06.5: Cost of Deliberation.** New document. Derives deliberation
   threshold: Δη* · |δ_post| > ρ · Δτ. Consequences: high-ρ penalizes
   deliberation (formalizes Boyd), diminishing returns → optimal Δτ*,
   implicit action as high-tempo limit.

10. **TF-08: Tensor tempo flag.** Added as Open Question #4. Scalar T
    assumes isotropic adaptive capacity; real systems have dimensional
    variation. Positive-definite condition T - diag(ρ) for full treatment.

### Session 3c: Items 4, 6, 8 + Lyapunov Assessment

11. **TF-01b: CIY identifiability section.** Three regimes: (a) with
    interventional data (standard for active agents — CIY identifiable by
    construction since agents DO things and SEE results; randomized action
    eliminates confounding), (b) observational only (requires DAG or IV
    assumptions — Pearl's fundamental insight restated), (c) practical
    implication: exploration diversity determines CIY estimation quality,
    providing an information-theoretic argument for exploration complementing
    TF-04's mismatch-based argument.

12. **TF-06: Unified policy objective.** Added formal objective:
    π* = argmax[E[value] + λ(M_t) · E[CIY]]. λ depends on U_M, time
    horizon, ρ. Noted structural isomorphism with active inference's
    expected free energy (extrinsic + epistemic value). Key distinction:
    TFT grounds exploration in *causal* information specifically, not
    entropy reduction generally — not all uncertainty reduction is equally
    valuable. Epistemic status: discussion-grade, not yet derived.

13. **TF-08: Strengthened nonlinear dynamics note.** Expanded Open Q #1
    with specific plausible nonlinearities: saturation at large δ,
    threshold/dead-zone effects, structural breakdown. Linear form
    reframed as local Taylor approximation near steady state. Forward
    reference to potential Lyapunov analysis.

### Session 3d: Lyapunov Stability Analysis

14. **scratch/07-lyapunov-stability-analysis.md** — Full working draft.
    Results:
    - L.1 (Bounded Mismatch): Generalizes Prop 8.1 to nonlinear dynamics
      via sector-condition Lyapunov. $R^* = \rho/\alpha$ where α is the
      sector bound (= T in linear case). Clean and complete.
    - L.2 (Stability Margin): Adaptive reserve Δρ* = αR - ρ. Simple
      corollary, immediately useful concept.
    - L.3 (Adversarial Destabilization): A destabilizes B when
      T_A > Δρ*_B / γ_A. Captures asymmetric coupling, finite reserves,
      structural collapse. Strongest and most novel result.
    - L.3.1 (Effects Spiral): Boyd's cascading disorientation as positive-
      feedback Lyapunov instability. Genuinely novel formalization.
    - L.4 (Multi-Timescale): Sketch only. Singular perturbation approach
      for temporal nesting. Needs better specification of slow dynamics G.

    Assessment: L.1-L.3 ready for promotion to TF-08 or appendix.
    L.4 stays in scratch. Key value: persistence and adversarial results
    no longer contingent on linear hypothesis.

    Document also explicitly notes what Lyapunov will NOT illuminate:
    quantitative steady states, convergence rates, optimal gain structure,
    explore-exploit balance, model sufficiency, causal structure.

### Session 3e: Lyapunov Appendix Promotion

15. **Appendix-A-Lyapunov.md** created in project root. Polished versions of
    L.1–L.3.1 as Propositions A.1–A.3 + Corollary A.3.1, with full proofs,
    interpretations, domain instance tables, and summary matrix. L.4 included
    as explicit sketch with notes on what's missing (structural adaptation
    dynamics G). Added "What this illuminates" and "What this does NOT
    illuminate" sections for honest scoping.

16. **TF-08 references**: Three insertion points added:
    - Prop 8.1 robustness note → forward reference to A.1
    - Open Question #1 (nonlinear dynamics) → forward reference to full
      appendix, noting adaptive reserve and adversarial results
    - Adversarial dynamics section → forward reference to A.3 and A.3.1

17. **README updated**: Appendix A added to table of contents. Core structure
    summary updated to mention Lyapunov extension and adaptive reserve concept.

### Session 4: Prescriptiveness Audit and Multi-Timescale Fix

18. **Identified systemic prescriptiveness issue.** The theory had drifted
    into treating "parametric" vs "structural" as a clean binary when TF-08
    already describes N levels. The binary was leaking into TF-07 ("The Two
    Levels"), Appendix A.4 (two-state singular perturbation), and various
    modal language throughout.

19. **TF-06: Action fluency concept introduced.** Replaced the category error
    "in the limit of a perfect model, all action is implicit" with a proper
    distinction between model sufficiency S(M_t) and *action fluency* — the
    degree to which effective action flows from the model without deliberation.
    Chess grandmaster has high S but needs search; a reflex has moderate S but
    high fluency in its domain. Unifies reflexes, muscle memory, instincts,
    intuition, expertise, System 1 under a single concept without reducing
    them to "cached policy." Connected implicit action to TST T-01 temporal
    optimality principle and TF-06.5's deliberation cost derivation.

20. **TF-07: Reframed as multi-timescale continuum.** "The Two Levels" →
    "Levels of Adaptation" with parametric/structural as commonly analyzed
    ends of a continuum. "Requires destruction" → decompose-and-recombine
    as one mechanism among several (expansion, compression, grafting).
    Boyd's snowmobile thought experiment preserved as motivating example.
    Added "Notes on intermediate levels" column to domain instantiation table.
    Destruction-Creation Cycle reframed as "A Common Pattern" that applies
    when structural change involves significant decomposition.

21. **TF-08: Nesting table noted as illustrative, not exhaustive.**

22. **Appendix A.4: Rewritten for N timescales.** General $N$-level singular
    perturbation framework with two-timescale as simplest nontrivial case.
    Added LLM applicability note. Summary table updated.

23. **Modal language pass across all documents.** Fixed:
    - TF-04: "active testing is essential" → "can be valuable for agents
      that have the capacity to vary their actions"
    - TF-06.5: "well-trained systems default to implicit action" → "high-
      tempo environments favor implicit action"
    - README: Updated TF-06 and TF-07 summaries.

24. **TF-00: Updated.** Added action fluency concept. Added Lyapunov notation
    block (α, R, R*, Δρ*, γ_A, V, F, w).

### Session 4b: Query Actions

25. **TF-06: Query actions section added** under "Action as Information
    Generation." Identified that the theory's examples of exploration were
    almost exclusively about direct environment probing, missing the
    qualitatively different class of actions where information comes from
    querying another agent's pre-compressed model. Key properties:
    - Extreme CIY density (orders of magnitude higher than individual probes)
    - Trust-dependent gain (second-order model of source reliability)
    - Pre-compressed information (transfer of sufficient statistics, with
      translation cost when representational frameworks differ)
    - Can trigger structural adaptation via grafting (TF-07)

    Motivated by the Bohr/barometer thought experiment: when a reliable
    external model exists, querying it dominates physical probing.

26. **TF-06 domain table expanded** with "Exploration: query actions" column.
    Every domain has query-action analogs (intelligence gathering, literature
    review, hiring consultants, social learning, etc.).

27. **Cross-references added:**
    - TF-01b: Note that CIY framework encompasses query actions; query
      response is causally downstream of query action.
    - TF-04: Query actions as efficient way to resolve zero-mismatch ambiguity.
    - TF-07: Grafting mechanism explicitly linked to query actions as
      primary conduit for acquiring external representational structure.
    - README: Summary updated.

    Connects forward to LLM strategy document: LLMs are fundamentally
    query-answering agents whose value is providing high-CIY responses
    from a massive pre-compressed model.

### Session 4c: Counterfactual Deliberation and Adversarial Communication

28. **TF-06: Deliberation as counterfactual simulation.** Added paragraph after
    explicit deliberation bullet list connecting deliberation to Pearl's Level 3
    epistemic access (TF-01b). Key insight: deliberation IS counterfactual
    simulation — comparing predicted consequences of actions not yet taken by
    running the model's causal structure forward under multiple hypothetical
    interventions. The computational cost of this simulation is what distinguishes
    deliberation from implicit action. When action fluency is high, the
    counterfactual comparison has been "pre-computed" through prior experience.

29. **TF-06: Adversarial mirror of query actions.** Added subsection "The
    Adversarial Mirror: Deception and Model Corruption" after the cooperative
    query actions section. Four key points:
    - Deception as negative effective CIY (updates that increase rather than
      decrease model-reality mismatch)
    - Boyd's active OODA loop interference formalized: adversary manipulates
      information environment to increase opponent's ρ through the communicative
      channel rather than physical action
    - Trust meta-model as second-order attack surface (corrupting the capacity
      to evaluate information, not just injecting bad information)
    - Formal symmetry: same structure (communicative actions with trust-dependent
      gain) encompasses both cooperative and adversarial cases; game theory's
      cheap talk / signaling games address incentive compatibility

30. **TF-08: Cross-reference added** from adversarial dynamics section to TF-06's
    adversarial communication discussion, noting that coupling γ_A can operate
    through communicative channels.

### Session 5: Combined Audit (Claude + Codex + Gemini)

31. **TF-06: Level 2/3 conflation fixed.** The deliberation paragraph originally
    claimed deliberation is "in its essence, counterfactual simulation (Level 3)."
    This overclaimed. Forward-looking comparison of candidate actions is iterated
    Level 2 (mental intervention); Level 3 (counterfactual) is retrospective
    ("what would have happened had I done otherwise?"). Fixed to distinguish.
    Cross-reference added to TF-01b Level 3 section.

32. **TF-08: Persistence threshold inconsistency fixed** (Codex #1). The linear
    ODE yields bounded mismatch for any T > 0, not just T > rho. The old
    statement conflated "bounded" with "functionally adequate." Rewritten to:
    mismatch always bounded under linear dynamics, but functional persistence
    requires T > rho/|delta_critical|. The shorthand T > rho is the normalized
    form. Nonlinear/adversarial case is where unbounded growth actually occurs.

33. **TF-00: Dimensional analysis fixed** (Codex #2). T has units [1/t], rho has
    units [surprise/t] — these are NOT the same units. The comparison T > rho
    only makes sense when mismatch is normalized to be dimensionless. Fixed
    units section with explicit dimensional analysis.

34. **Appendix A.4: Epsilon direction fixed** (Codex #4). The two-timescale case
    had epsilon * x2_dot = G, making x2 FAST (not slow as labeled). Fixed to
    x2_dot = epsilon * G.

35. **F symbol collision resolved** (Codex medium #2, our C2). Renamed structural
    update function from F to Phi in TF-07 and TF-00 to avoid collision with
    Appendix A's correction function F(T, delta).

36. **CIY non-negativity noted as assumption** (Codex #3). The definition
    (difference of two MI terms) is not guaranteed non-negative in general.
    Added note to TF-01b: non-negativity holds under randomized actions or
    causal Markov condition; stated as assumption not proven property.

37. **Language/attribution fixes across documents:**
    - TF-06.5: "Boyd's central operational insight" → "a principle Boyd emphasized"
    - TF-08: "asserted as doctrine" → "argued qualitatively"
    - TF-08: removed unattributed quotation marks from "acting on a world..."
    - TF-01b: "most fundamental" → "most primitive" for consistency
    - TF-06: "often happens" → "Boyd's thought experiment specifically illustrates"
    - TF-01: replaced "would be the environment" flourish with formal statement

38. **TF-00 notation fixes:** H_t attribution corrected to TF-01b/TF-02;
    nu_eff added to event-driven dynamics table with note on T identity.

39. **README: Game theory gap noted** in "What's Potentially Missing" —
    TFT makes incentive compatibility formally precise but doesn't answer it.

### Session 6: Consistency Pass from scratch/08 Feedback

40. **TF-01: Scope conditioning made action-aware.** Replaced H(Omega|o_{1:t})
    with H(Omega|H_t) in formal scope definition and exclusion clause, aligning
    with the rest of the framework which conditions on the full interaction history.

41. **TF-00: CIY sign semantics reconciled.** Changed CIY type from "Scalar >= 0"
    to "Scalar (assumed >= 0; see note)" with inline explanation of when non-negativity
    holds and cross-references to TF-01b and TF-06 adversarial discussion.

42. **TF-08: Adversarial ratio coupling assumptions made explicit.** Added coupling
    effectiveness coefficients gamma_A, gamma_B to the adversarial dynamics equations.
    The clean ratio T_A/T_B is now explicitly flagged as requiring symmetric coupling
    and proportional action magnitude assumptions.

43. **TF-04: Prop 4.1 proof tightened.** Added explicit assumptions (non-degenerate
    noise or strict model inadequacy). Rewrote proof with proper decomposition showing
    cross-term vanishing, data processing inequality for model error term, and both
    sources of positivity. Updated decomposition section for consistency.

44. **TF-02: Policy-conditional sufficiency note added.** The full-sequence definition
    S(M_t) conditioning on a_{t:infty} is the theoretical ideal; a practical variant
    S_Pi(M_t) restricting to a policy class Pi is noted for operationalization.

45. **TF-08: Scalar vs vector reduction note added.** Bridging section before Open
    Questions explaining when the scalar |delta| treatment is valid and when the
    full vector formulation (Appendix A) is needed.

46. **scratch/additional-feedback.md created and updated.** Consolidated all pending
    items across all feedback sources. Items A1, A6-A9, B4 marked as done.

47. **TF-05: Three improvements.** (a) Added "Scope of claim" paragraph qualifying
    the universal gain form — structural form is the claim, scalar ratio is simplest
    instantiation. (b) Added CIY connection section — high-CIY observations should
    get more weight; currently implicit in U_M structure. (c) Added Overall Assessment
    with confidence estimates: ~75% structural form is universal, ~40% scalar form
    adequate in high-dimensional settings.

48. **TF-00: Dependency DAG and Formal Results Index.** Added primary chain showing
    document progression, key cross-links. Added table distinguishing formal
    propositions (4.1, 6.5.1, 7.1, 8.1, A.1-A.3, A.3.1) from discussion-grade
    claims (uncertainty ratio, unified policy, speed-quality substitutability,
    action fluency, non-forkability).

49. **B5 (prose consolidation) deferred.** Existing cross-references between TF-06,
    TF-08, and Appendix A are already adequate; the documents serve different purposes
    and the repetition is more helpful than harmful.

### Still Pending from Reviews

- TF-03 track decision (minimal async vs. full stochastic process)
- Scope boundaries as first-class document
- Gemini suggestion: reward-as-value-channel
- Citation confidence tiers for v7 references
- Formal derivation of λ(M_t) from first principles (hard — may require
  Bayes-optimal decision theory or Gittins-like analysis)
- ~~Decision: promote L.1-L.3 into TF-08 or create dedicated appendix?~~ RESOLVED: dedicated Appendix A with forward references from TF-08.

### Notes on Evolution of TF-01

TF-01 is currently a scope definition, not an axiom. If we eventually find
a more irreducible foundational claim (analogous to TST's T-01 tautology),
TF-01 might be displaced. TF-01b (causal structure / arrow of time) is
a candidate — it might be THE foundational axiom, with the scope definition
becoming secondary. But for now the scope-first ordering makes the theory
accessible: "here is what this is about" before "here is the deepest
foundational claim." A more axiomatic TF-01 may emerge with maturity;
we are starting at a good spot with a well-defined "living system."

### Notes on TF-03 Placement

TF-03 (event-driven dynamics) may be premature at position 3. The
discrete-time form is simpler and sufficient for most subsequent derivations.
Options:
  a) Keep at position 3 but make discrete form primary, event-driven as
     generalization (current draft leans event-driven-primary)
  b) Move later (after TF-05 or TF-06) as "the discrete notation is a
     special case of this more general formulation"
  c) Split: put the continuous+jumps formulation (with q(M_t) term) in a
     separate TF that explicitly addresses LLM-relevant "continuous interiority"

Option (c) has appeal because it separates the engineering convenience
(multi-rate events) from the deep philosophical content (autonomous
orientation between events). The former is TF-03; the latter might be
a new TF or part of the LLM strategy document.

## File Organization

- ~/src/temporal-feedback/ — working directory (git repo)
- ~/src/temporal-feedback/scratch/ — intermediate work, notes
- ~/src/temporal-feedback/ooda-loop-universal-pattern-v7.md — source material
- Final documents: TF-01.md through TF-11.md + Appendix-A-Lyapunov.md (in root of temporal-feedback/)

## Session 7: Full Restructure (items 50+)

50. **Major restructure following TST pattern.** Renumbered all documents:
    - Old TF-01b → TF-02, old TF-02 → TF-03, etc.
    - Split old TF-06 (161 lines, 5+ ideas) into TF-07 (Action Selection) and TF-08 (Exploration-Exploitation Balance)
    - Old TF-06.5 → TF-09, old TF-07 → TF-10, old TF-08 → TF-11
    - Renumbered propositions: Prop 4.1→5.1, Prop 6.5.1→9.1, Prop 7.1→10.1, Prop 8.1→11.1
    - Updated ALL cross-references across ALL documents
    - TF-00 kept as-is (references updated only)
    - Appendix A proposition numbers (A.1-A.4) unchanged
    - Eliminated awkward 01b and 06.5 suffixes
    - 11 numbered docs + 1 appendix (matches TST's 12)
    - Line counts now 42-265 (mean ~76 excl. appendix, down from ~113)

## Session 8: Synthesized Feedback Implementation (items 51+)

51. **Triple-reviewer feedback synthesis and implementation.** Received and synthesized feedback from Codex (scratch/tft-feedback-2026-02-28.md), Gemini (scratch/10-comprehensive-feedback-review.md), and fresh Opus (scratch/11-opus-deep-review-2026-02-27.md). Implemented 12 edits:
    - TF-03: Axiom → Formulation (Opus primary concern, Codex implicit)
    - TF-02: Added formal CIY Admissibility Regimes box (three regimes: randomized, observational, adversarial) — resolves triple-convergent "negative CIY" issue
    - TF-08: Rewrote adversarial mirror from "negative effective CIY" to ρ-injection framing via Lyapunov γ_A
    - TF-08: Added CIY estimability note to unified policy objective
    - TF-08: Heading → "Hypothesis + Discussion"
    - TF-05: Proof wording: "independence" → orthogonality via tower property
    - TF-05: Added δ units/interpretation bridge note for TF-11 dynamics
    - TF-07: Added formal characterization of action fluency (Δη* ≈ 0 ⟹ high fluency)
    - TF-09: Marked conditional on TF-11 hypothesis; added ρ forward reference
    - TF-11: Added prominent opening note distinguishing ODE-dependent quantitative vs robust qualitative results
    - TF-00: Fixed policy objective location (→ TF-08), λ location, Prop 9.1 status, CIY entry, action fluency entry, dependency labels
    - README: Updated TF-03 type, core structure description, TF-09 status, adversarial reference
    Deferred for discussion: uncertainty ratio reframing (TF-06), "tautological axioms" caveat (TF-00/TF-02), TF-01 vs TF-02 ordering
