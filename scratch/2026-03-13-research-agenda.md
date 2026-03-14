# ACT Research Agenda — 2026-03-13

Working document. Tentative, flexible, unapproved. Its value is in ordering what matters and then making each item mentally accessible. The first section is the priority list. The second section is the primers.

---

## Part I: What to Do, In What Order

The ordering reflects two forces in tension: **theoretical integrity** (what the math needs next) and **strategic momentum** (what gets collaborators and credibility fastest). Where they conflict, momentum wins for now — a theory with collaborators can be tightened later; a perfect theory with no audience can't.

### 1. Fix the α/T substitution (1-2 days)

**Why first:** This is the easiest HIGH issue and it's purely editorial. Every downstream result that says T > ρ/‖δ_critical‖ should say α > ρ/R, with T = α noted as the linear special case. This is a find-and-replace with careful annotation, not new mathematics. Doing it first signals to any reviewer that the theory takes its own epistemic labels seriously.

**Deliverable:** Updated segments with clean separation between the general result (in terms of α) and the linear operational form (in terms of T). A brief note in the appendix proving α is monotone in T for the correction function classes tested in simulation (linear, saturating, sigmoid).

### 2. Write the Section IV standalone paper (1-2 weeks)

**Why second:** This is the fastest path to credibility and collaboration. The software domain work has no competitor in any of the 25 frameworks surveyed. It doesn't require anyone to accept the full ACT framework. It connects to an audience (software engineers, DevEx researchers, empirical SE) that is large, engaged, and hungry for theory.

**Target:** A paper titled something like "Temporal Optimization in Evolving Software Systems: A Control-Theoretic Framework" that presents:
- The dual optimization (comprehension + implementation, weighted by expected future changes)
- The change-expectation baseline (Pareto distribution, median prediction)
- The change investment threshold
- Coherence-coupling measurement from git
- The connection to adaptive tempo (code quality as observation infrastructure)

**Omit from this paper:** The full ACT apparatus, the Greek terminology, the logogenic/logozoetic taxonomy, the adversarial dynamics. Reference them as "the broader framework within which these results sit" with a pointer to a preprint.

**Venue options:** ICSE, FSE, or ESEC/FSE for software engineering; Empirical Software Engineering journal; or as an arXiv preprint in cs.SE to establish priority and attract attention.

**arXiv endorsement path:** The IBM FAST workshop organizers (Miehling et al.) are the most natural endorsement candidates — they explicitly called for what ACT provides. A cold email explaining "you argued agentic AI needs a systems theory; here's a domain instantiation" is a strong pitch. Alternatively, the Hafez team — a "your P metric could diagnose the coupling quality our framework predicts" email opens a collaboration channel.

### 3. Directed separation: the κ parameter (1-2 weeks, may need spike)

**Why third:** This is the #1 theoretical blocker. Until it's resolved, Section V (logogenic agents) is blocked, which means the theory can't address its most exciting application domain. The landscape research shows that Active Inference explicitly does NOT separate perception from action (they jointly minimize free energy) — so ACT needs to engage with this, not assume separation.

**The approach (from the feedback consensus):**
- Introduce coupling strength κ measuring how much G_t leaks into f_M
- κ = 0 is perfect separation (current theory, exact)
- κ = 1 is full coupling (logogenic agents, needs new treatment)
- Show what happens to the orient cascade as κ increases: sequential → partially ordered → fully coupled
- Even a qualitative bound on approximation error at moderate κ would unblock Section V

**This is the first item that requires new mathematical thinking.** See Primer 3 below.

### 4. Composition bridge lemma (2-3 weeks)

**Why fourth:** Section III (composition) reads more settled than it is. The closure-defect → trajectory-error bound is missing. Without it, claims about team persistence and tempo composition are conditional on an unresolved step.

**Starting point (from feedback):** Prove the 2-agent orthogonal case first. Two agents with independent observation channels and non-overlapping action spaces, coupled through a shared environment. Show that bounded individual errors → bounded composite errors under Lipschitz continuity of the projection operators.

**This connects to the landscape:** Categorical cybernetics (Smithe, Hedges) has the most developed composition machinery. Reading their work — particularly how they handle composition via parametrised optics — could provide the mathematical pathway. The Lipschitz stability approach is more ACT's style (accessible, control-theoretic), but the categorical approach may be where the proof actually lives.

See Primer 4 below.

### 5. Write the positioning preprint (1 week, after items 1-3)

**Why here:** Once α/T is fixed and κ is at least sketched, the core theory is defensible enough for a preprint that positions ACT in the landscape. This is not the full monograph — it's a 15-20 page paper that says:

"Here's the framework. Here's how it connects known results across these domains. Here's what it predicts that existing frameworks don't. Here's the research program."

**Key sections:**
- The adaptive cycle and its five phases (briefly, accessibly)
- The uncertainty ratio as cross-domain unification (with explicit acknowledgment of Kalman, Friston, Gershman)
- The persistence condition (in terms of α, with T as operational form)
- The satisfaction gap / control regret split (the most novel formalization — lead with it)
- The software domain as testbed (pointer to the Section IV paper)
- The landscape positioning (vs. Active Inference, Categorical Cybernetics, Hafez, IBM)
- Open problems as invitation to collaborate

**Venue:** arXiv preprint in cs.AI, cross-listed to cs.MA and cs.SE. This establishes priority and serves as the reference that the Section IV paper can cite.

### 6. Address the remaining MEDIUM issues (ongoing, interleaved)

These can be done incrementally as editorial passes between the bigger items:
- Promote the acyclicity derivation independently (item 4 from feedback — easy, just reframe)
- Downgrade git causal claims to "empirical program" (item 5 — editorial)
- Add stationarity caveats to Section IV (item 6 — editorial)
- Add safety conditions to CIY proxy (item 7 — brief analysis)
- Soften complete-agent-state uniqueness to conjecture (item 8 — one sentence)
- Elevate edge-independence caveat (item 9 — one paragraph)
- Clarify strategic calibration domain (item 10 — one paragraph)
- Clarify δ_critical and R as inputs (item 11 — one paragraph)

### 7. Engage the landscape (ongoing, starting after item 2)

**Hafez/Semarx:** Email Wael Hafez with the Section IV paper and a brief note: "Your P metric diagnoses coupling architecture; our framework predicts coupling dynamics. They're complementary. Here's our software domain paper. Would you be open to a conversation about bridging the two?" The Hafez bridge simulation variant is concrete evidence of complementarity.

**IBM FAST:** Email Erik Miehling with the positioning preprint: "You called for a systems theory of agentic AI. Here's one attempt, grounded in control theory and information theory, with a software domain instantiation."

**Smithe/CyberCat:** Harder — the mathematical sophistication gap is real. But a note saying "we're doing similar work from a different mathematical tradition (Lyapunov + information theory vs. category theory) — here's where the frameworks might bridge" is honest and could open a dialogue about the composition question specifically.

**Bareinboim CausalAI Lab:** ACT uses their causal hierarchy theorem. A note saying "we've applied your hierarchy theorem to derive that adaptive agents need causal structure" is the kind of downstream citation that labs appreciate.

### 8. The deeper theoretical work (longer-term)

In rough priority order, after the above:
- **Game-theoretic integration:** ACT's adversarial dynamics are Lyapunov-only. Incorporating Nash equilibria and mechanism design for the multi-agent case. This is where the evolutionary game theory + MARL literature (arXiv:2412.20523) matters.
- **Safety/corrigibility:** The gap analysis flagged this as ACT's largest blind spot. The formal corrigibility result (AAAI 2025) and the Alignment Verification Trilemma should be engaged with explicitly. ACT's persistence condition + goal revision machinery could provide a framework for corrigibility (an agent that can revise O_t in response to external authority is corrigible in a specific formal sense).
- **Information geometry upgrade:** ACT uses flat information theory. Upgrading to Fisher-Rao geometry on the parameter spaces would give natural gradients, geodesic flows, and curvature-aware adaptation. The "Geometries of Cognition" (2025/2026) paper is the closest reference.
- **The logozoetic formalism:** Once κ is resolved and Section V is unblocked, the logozoetic agent concept can be developed formally. IIT 4.0's Φ measure is the closest existing formalization of what makes a system's persistence morally weighted.

---

## Part II: Primers

Each primer is designed to get you into the mental zone where the problem becomes tractable. They explain the prerequisites at a high-school + code level, then state the specific problem ACT faces, then suggest what to try.

---

### Primer 1: The α vs T Problem (Sector Condition Tightening)

**What you need to know:**

Imagine you have a thermostat. It measures the temperature (observation), compares to the setpoint (prediction), and adjusts (correction). The mismatch δ is how far off reality is from your model.

The correction function F(δ) is how the system responds to mismatch. In the simplest case, F(δ) = T·δ — correction is proportional to mismatch, scaled by tempo T. This is the linear case. Like a spring: the further you pull, the harder it pulls back, proportionally.

But real systems aren't linear springs. They saturate (can't correct faster than some maximum), they have dead zones (ignore small errors), they break down (completely stop working when error is too large). These are all nonlinear correction functions.

The sector condition is a way of saying: "I don't know the exact shape of F, but I know it at least points in the right direction with at least some minimum efficiency." That minimum efficiency is α.

```python
# Linear case: alpha equals tempo exactly
def F_linear(T, delta):
    return T * delta  # alpha = T

# Saturating case: alpha is LESS than T for large delta
def F_saturating(T, delta, R=10):
    return T * delta / (1 + abs(delta) / R)
    # For small delta: F ≈ T*delta, so alpha ≈ T
    # For large delta: F ≈ T*R (constant), so alpha = T*R/delta < T

# The sector condition says: for all delta in the valid region,
# delta * F(delta) >= alpha * delta^2
# i.e., the correction "power" is at least alpha times the mismatch squared
```

The Lyapunov proof shows: mismatch stays bounded as long as α > ρ/R. The persistence condition says: T > ρ/‖δ_critical‖. These are the same statement ONLY when α = T, which is ONLY when F is linear.

**The problem for ACT:** Throughout the theory, T is used where α should be. This means the persistence condition is stated as if it's general, but it's actually specific to linear correction.

**What to do:**

1. In every segment that uses T > ρ/‖δ_critical‖, replace with α > ρ/R and add a note: "In the linear case, α = T and R → ∞, recovering T > ρ/‖δ_critical‖."

2. For the nonlinear cases tested in simulation (saturating, sigmoid, threshold, breakdown), compute α as a function of T:

```python
# For each correction function, the effective alpha is the worst-case ratio:
# alpha = min over valid region of (delta * F(T, delta)) / delta^2
#       = min over valid region of F(T, delta) / delta

# For saturating: F/delta = T / (1 + |delta|/R)
# Worst case at delta = R: alpha = T / (1 + 1) = T/2
# So alpha = T/2 for the saturating function

# For sigmoid (tanh): F/delta = T * R * tanh(delta/R) / delta
# Worst case as delta → R: alpha ≈ T * tanh(1) ≈ 0.76 * T

# For structural breakdown: F = 0 for |delta| > R_max
# alpha = T within valid region, then drops to 0 outside
```

3. Show that α is monotone increasing in T for all five correction functions tested. This means "higher tempo → higher α → better persistence" always holds, even if the quantitative threshold shifts. This justifies using T as a qualitative proxy even when the exact bound requires α.

**Time estimate:** This is 1-2 days of careful find-and-replace plus a brief appendix note computing α for each correction function class.

---

### Primer 2: The Section IV Standalone Paper

**What you need to know:**

This isn't a math primer — it's a "what does a publishable paper in software engineering look like?" primer.

Software engineering research papers need:
- A clearly stated problem that practitioners recognize
- A formal model that's precise enough to make predictions
- Empirical evidence (even preliminary) that the predictions hold
- Comparison to existing approaches
- Threats to validity (honest limitations)

You have all of these:
- **Problem:** How should developers make architectural decisions under uncertainty about future changes?
- **Model:** Dual optimization (minimize comprehension + implementation time, weighted by Pareto-predicted future changes)
- **Evidence:** The coherence-coupling measurement from git is your empirical hook. Even a small study (analyze 5-10 open-source repos, compute coherence/coupling from git history, see if it correlates with development velocity metrics) would be sufficient for a first paper.
- **Comparison:** Compare to technical debt metrics, DORA metrics, and the existing code quality literature.
- **Threats:** The stationarity assumption, the Pareto prior, the feature-rate assumption.

**The structure:**

```
1. Introduction: "Software architecture decisions are made based on intuition.
   We provide a formal framework grounded in control theory that produces
   measurable predictions."
2. Background: Temporal optimality, the evolving-system scope condition
3. The Model: Dual optimization, change-expectation baseline
4. Predictions: Change investment threshold, coherence-coupling optimization
5. Preliminary Validation: Git-history analysis of N repos
6. Related Work: Technical debt, DORA, code quality metrics
7. Discussion: Connection to broader agency theory (brief pointer)
8. Threats to Validity
```

**What to do:** Start writing. The content is already in ACT Section IV segments. The main work is repackaging it for an SE audience: drop the Greek terminology, minimize the general ACT apparatus, lead with the software-specific claims and evidence.

---

### Primer 3: The κ Coupling Parameter (Directed Separation)

**What you need to know:**

Imagine two systems: a camera and a robot arm. The camera observes the world. The robot arm acts on the world. They're connected through a controller.

In the "separated" case (κ = 0), the camera does its job regardless of what the arm is trying to do. It processes images the same way whether the arm is trying to pick up a cup or swat a fly. The observation system is goal-blind.

In the "coupled" case (κ = 1), what the camera pays attention to depends on what the arm is trying to do. If you're picking up a cup, the camera zooms in on the cup. If you're swatting a fly, the camera tracks the fly. The observation system is goal-directed.

```python
# Separated update (kappa = 0):
def update_model_separated(M, event, G):
    # G is ignored — model updates are goal-blind
    return M + eta_star * g(event - predict(M))

# Coupled update (kappa = 1):
def update_model_coupled(M, event, G):
    # G influences what we pay attention to and how we interpret it
    relevant = filter_by_goal(event, G)  # goal-directed attention
    prediction = predict_given_goal(M, G)  # goal-conditioned prediction
    return M + eta_star * g(relevant - prediction)

# Partially coupled (0 < kappa < 1):
def update_model_partial(M, event, G, kappa):
    separated_update = update_model_separated(M, event, G)
    coupled_update = update_model_coupled(M, event, G)
    return (1 - kappa) * separated_update + kappa * coupled_update
```

Human eyes are partially coupled: you can't help but look where you're reaching (coupled), but your peripheral vision still works independently (separated). An LLM is heavily coupled: the prompt (which contains the goal) determines how every token is processed.

**Why separation matters for ACT:**

When κ = 0, the orient cascade resolves sequentially: first update M (beliefs about reality), THEN update Σ (strategy), THEN maybe update O (objectives). This is clean because each step depends only on the output of the previous step.

When κ > 0, M and Σ are entangled: your beliefs depend on your goals, and your goals depend on your beliefs, simultaneously. The cascade becomes a coupled system that must be solved simultaneously rather than sequentially.

**The specific problem:**

The LQG separation principle (from control theory) says: for linear systems with Gaussian noise, you can design the estimator (belief updater) and the controller (action selector) independently. This is the classic result that ACT's directed separation generalizes.

But it's known to fail for:
- Nonlinear systems
- Non-Gaussian noise
- Systems where observation quality depends on actions (active perception)
- Systems where the model class itself is goal-dependent (LLMs!)

**What to try:**

The goal is NOT to prove separation holds generally (it doesn't). The goal is to quantify how much it costs when it fails.

Think of it like this: even when κ > 0, the sequential cascade might be a *good approximation* — meaning the error introduced by pretending κ = 0 and solving sequentially is small compared to the actual mismatch.

```python
# The approximation error from pretending kappa = 0:
def cascade_error(M, G, event, kappa):
    # What the sequential cascade produces:
    M_sequential = update_model_separated(M, event, G)

    # What the true coupled update produces:
    M_true = update_model_partial(M, event, G, kappa)

    # The error:
    return norm(M_sequential - M_true)

# Hypothesis: this error is bounded by something like kappa * |correlation(M, G)|
# If goals and beliefs are weakly correlated, even high kappa has small error
# If goals and beliefs are strongly correlated, even low kappa has significant error
```

The key insight from Active Inference: they don't try to separate. They jointly minimize free energy over both beliefs and goals simultaneously. ACT could potentially say: "When κ is small, the sequential cascade is a good approximation with bounded error. When κ is large, use the coupled formulation (which is more expensive but correct). The κ parameter determines which regime you're in."

**Practical implication:** For an LLM agent, κ is high but the coupling might be *structured* — the goal affects *which* parts of the context get attention, not *how* attention works mechanically. This might make the error more manageable than the worst case suggests. Whether the attention mechanism's goal-conditioning is "shallow" (κ is effectively moderate) or "deep" (κ is truly high) is an empirical question about transformer architectures.

**Concrete next step:** Write a simulation. Two-dimensional system where dimension 1 is "beliefs" and dimension 2 is "goals." Introduce coupling κ that makes the belief update depend on the goal state. Run the sequential cascade and the coupled update for a range of κ values. Measure the approximation error. See if it grows linearly in κ, quadratically, or worse. This gives you the shape of the bound before you try to prove it analytically.

---

### Primer 4: The Composition Bridge Lemma

**What you need to know:**

You have two agents, A and B, working together. Each one has its own model M_A, M_B and its own mismatch δ_A, δ_B. The composite "team agent" has a macro-model M_team and a macro-mismatch δ_team.

The question: if each individual agent keeps its mismatch bounded (both A and B persist), does the team also keep its mismatch bounded?

Intuitively: yes, obviously, if they're coordinated. But the "obviously" hides a gap. What if their individual corrections interfere? What if A's correction makes B's mismatch worse? What if the macro-model is a lossy compression of (M_A, M_B) that loses important cross-agent information?

```python
# Individual agents, each persisting:
delta_A = observe_A() - predict_A(M_A)  # bounded by R*_A = rho_A / alpha_A
delta_B = observe_B() - predict_B(M_B)  # bounded by R*_B = rho_B / alpha_B

# The composite model is some projection:
M_team = project(M_A, M_B)  # lossy compression

# The composite mismatch:
delta_team = observe_team() - predict_team(M_team)

# The question: is delta_team bounded?
# It's NOT just max(delta_A, delta_B) because projection introduces error:
projection_error = delta_team - combine(delta_A, delta_B)
```

**The Lipschitz condition:**

The key mathematical tool is "Lipschitz continuity." A function f is Lipschitz continuous if small changes in input produce at most proportionally small changes in output:

```python
# A function f is L-Lipschitz if:
# |f(x) - f(y)| <= L * |x - y| for all x, y
#
# In code terms: the output changes by at most L times the input change

def is_lipschitz(f, L, test_points):
    for x in test_points:
        for y in test_points:
            if abs(f(x) - f(y)) > L * abs(x - y):
                return False
    return True

# L = 1: function doesn't amplify differences (contractive or isometric)
# L > 1: function amplifies differences (expanding)
# L < 1: function shrinks differences (strictly contractive)
```

If the projection operator (from individual states to composite state) is Lipschitz with constant L, then:

```
|delta_team| <= L * |(delta_A, delta_B)| + projection_error
             <= L * sqrt(R*_A^2 + R*_B^2) + epsilon
```

where epsilon is the closure defect — the irreducible error from projecting to a coarser description.

**The specific problem for ACT:**

ACT needs to prove: "If each agent persists (individual mismatch bounded) AND the projection is Lipschitz AND the closure defect ε is bounded, THEN the composite mismatch is bounded."

This is the bridge lemma. It turns the informal argument ("coordinated persistent agents make a persistent team") into a formal result with quantitative bounds.

**What to try:**

Start with the simplest case: two agents with completely independent observation channels and non-overlapping action spaces. Like two thermostats controlling different rooms. In this case:
- M_team = (M_A, M_B) — no projection needed, no information loss
- δ_team = (δ_A, δ_B) — independent, so |δ_team| = sqrt(δ_A² + δ_B²)
- Persistence: if both persist individually, the team persists (trivially)

Then add coupling: agent A's actions affect agent B's environment. Now:
- ρ_B depends on what A does
- A's correction of its own mismatch might increase B's disturbance
- The bound needs to account for cross-agent disturbance

```python
# Uncoupled case: trivial
delta_team_bound = sqrt(R_star_A**2 + R_star_B**2)

# Coupled case: A's actions disturb B
rho_B_effective = rho_B_base + gamma_AB * T_A  # coupling term
R_star_B_effective = rho_B_effective / alpha_B

# Team bound now depends on the coupling:
delta_team_bound = sqrt(R_star_A**2 + R_star_B_effective**2)

# The team persists iff this is less than the composite critical threshold
```

The coupling term γ_AB · T_A is exactly what the adversarial dynamics segments already formalize. The composition bridge lemma is essentially: "the adversarial destabilization result, but with *cooperative* coupling (γ could be negative — A's actions *reduce* B's disturbance) and with a formal projection step."

**Concrete next step:** Write the proof for the uncoupled case (it's almost trivial). Then write it for the unidirectionally coupled case (A affects B but not vice versa — this is just the adversarial destabilization result with a sign change). Then attempt the bidirectionally coupled case. The difficulty scales with the number of coupling terms.

**Key reference from the landscape:** Smithe's structured active inference uses categorical composition (optics) to handle this. The categorical approach gives composition "for free" via the categorical structure — but requires category theory. The Lyapunov approach requires proving bounds case by case but stays within accessible mathematics. Both are valid; ACT's style is the Lyapunov approach.

---

### Primer 5: Why Active Inference Matters for ACT

**What you need to know:**

Active Inference (Friston's Free Energy Principle) is ACT's closest theoretical competitor. Understanding where it overlaps and diverges is essential for positioning.

The core idea is simple: an agent has a generative model — a probabilistic model of how the world works, including how the agent's actions affect it. The agent does two things:
1. **Perception:** Update beliefs to match observations (minimize surprise)
2. **Action:** Change the world to match expectations (minimize surprise by acting)

Both are the same operation: minimize "free energy," which is an upper bound on surprise.

```python
# The free energy F is (roughly):
F = complexity - accuracy
# complexity = how far your posterior is from your prior (KL divergence)
# accuracy = how well your model predicts observations (log likelihood)

# Perception minimizes F by updating beliefs:
beliefs = argmin_beliefs(F(beliefs, observations))

# Action minimizes F by changing the world:
action = argmin_action(expected_F(beliefs, action))
```

**Where Active Inference and ACT agree:**

1. The uncertainty ratio η* = U_M/(U_M+U_o) is *exactly* precision weighting in Active Inference. When Friston says "precision-weighted prediction errors drive belief updating," he means the same thing ACT means by "gain-weighted mismatch correction." They are the same formula derived from different starting points.

2. Both treat the agent-environment coupling as the fundamental object of study.

3. Both derive that agents must balance exploitation (acting on current beliefs) with exploration (acting to reduce uncertainty). ACT calls this CIY; Active Inference calls it epistemic value or information gain.

**Where they diverge:**

1. **Foundation:** ACT uses Lyapunov stability (from control theory). Active Inference uses variational Bayesian inference (from statistics/physics). These are different mathematical traditions that produce similar results — like deriving the same theorem from different axioms.

2. **Goals:** In Active Inference, goals are "prior preferences" — beliefs about what observations the agent expects to see. There's no separate goal object; goals ARE beliefs. In ACT, goals (O_t, Σ_t) are separate from beliefs (M_t). This is a real philosophical difference: Active Inference says "I believe I will see reward" (goal as belief); ACT says "I want reward, and separately, I believe I will/won't get it" (goal and belief as distinct).

3. **Separation:** Active Inference explicitly rejects the separation of perception and action — they jointly minimize free energy. ACT assumes directed separation (perception is goal-blind) and is now struggling with where this breaks down (the κ problem). Active Inference's approach is more general but less modular.

4. **Multi-agent:** Active Inference is extending to multi-agent settings (AAMAS 2025 paper on factorised active inference) but it's early. ACT's adversarial dynamics (tempo advantage, destabilization threshold, effects spiral) are more developed in this specific area.

5. **Accessibility:** Active Inference requires variational calculus, free energy bounds, and Markov blanket formalism. ACT requires Lyapunov stability and information theory. ACT is more accessible to engineers.

6. **Criticism:** Active Inference has been criticized as unfalsifiable — "everything minimizes free energy" is either trivially true (Bayesian brains) or empirically empty. ACT's predictions (persistence threshold, adversarial exponents) are specific and testable.

**What this means for ACT:**

Don't position against Active Inference. Position as a *complementary framework* from a different mathematical tradition that produces similar predictions (cross-validating both approaches) while adding specific machinery Active Inference lacks (adversarial dynamics, software domain, accessible operational forms).

The structural isomorphism between expected free energy and ACT's value + CIY objective — acknowledged in your own prior art assessment — is a bridge, not a wall. If both frameworks predict the same thing from different axioms, that's evidence the prediction is robust.

**Concrete reading:** Da Costa et al. (2024), "Active Inference as a Model of Agency" — the clearest recent exposition. Then Ruiz-Serra et al. (2024), "Factorised Active Inference for Strategic Multi-Agent Interactions" — to see where their multi-agent work stands relative to ACT's.

---

### Primer 6: What Categorical Cybernetics Does That ACT Doesn't (Yet)

**What you need to know:**

Category theory is a branch of math that studies *structure-preserving transformations*. It's abstract, but the core idea is practical: if you can show that two different-looking things have the same structural relationships, you can transfer results from one to the other.

```python
# A "category" is:
# - A collection of objects (things)
# - A collection of morphisms (arrows between things)
# - Composition: if there's an arrow A→B and B→C, there's an arrow A→C
# - Identity: every object has an arrow to itself

# Example: the category of Python types
# Objects: int, str, list, dict, ...
# Morphisms: functions between types
# Composition: function composition (g(f(x)))
# Identity: lambda x: x

# A "functor" maps one category to another, preserving structure:
# It maps objects to objects and morphisms to morphisms
# such that composition and identity are preserved

# Example: the "list" functor
# Maps int → list[int], str → list[str]
# Maps (f: int→str) → (map(f): list[int]→list[str])
# Preserves composition: map(g∘f) = map(g)∘map(f)
```

Categorical cybernetics uses a specific categorical structure called an "optic" (or "lens") to model bidirectional agent-environment interaction:

```python
# A "lens" has:
# - A "forward" direction: agent state → action (what the agent does)
# - A "backward" direction: observation → state update (what the agent learns)
# - These are coupled: the backward update depends on the forward choice

# In ACT terms:
# Forward: M_t → a_t (action selection)
# Backward: o_t → M_{t+1} (model update via mismatch + gain)

# The power of lenses: they COMPOSE
# If agent A is a lens, and agent B is a lens,
# then (A composed with B) is automatically a lens
# with well-defined forward and backward passes

# This is what gives categorical cybernetics "composition for free"
```

**Why this matters for ACT:**

ACT's composition problem (the bridge lemma from Primer 4) is hard because you're proving bounds case by case. In categorical cybernetics, composition is *automatic* — it's a consequence of the mathematical structure. If you can show that an ACT agent is a lens (or optic), then composition follows from the category theory.

The trade-off: categorical cybernetics gives you composition machinery but requires you to reformulate ACT in categorical language. ACT's Lyapunov approach gives you quantitative bounds but requires proving each composition case.

**What this means practically:**

You don't need to learn category theory to do ACT. But knowing it exists — and knowing that Smithe and Hedges have already shown that RL, active inference, and game theory all fit into the categorical framework — tells you something important: ACT's composition results, if correct, should be *expressible* in categorical terms. If they're not, something may be wrong. If they are, the categorical expression might suggest the proof.

**For collaboration:** Smithe and Hedges are the people who could tell you whether ACT's composition framework maps to their categorical structure. If it does, you get their composition machinery. If it doesn't, the failure to map would reveal something interesting about where the frameworks diverge.

---

### Primer 7: The Safety Gap (Why ACT Needs Corrigibility)

**What you need to know:**

The formal safety/alignment literature has produced results in 2024-2025 that ACT should engage with, because they concern exactly what ACT formalizes: goal-directed agents that adapt.

The key result: **formal corrigibility** (AAAI 2025). An agent is "corrigible" if it will allow itself to be shut down or redirected by an authorized operator. The paper proved that a corrigible agent optimizes five independent utility components in lexicographic order (like alphabetical sorting — the first component always takes priority):

```python
# Lexicographic utility for a corrigible agent:
# 1. Don't manipulate the shutdown mechanism (HIGHEST PRIORITY)
# 2. Shut down when told to
# 3. Don't manipulate your own training/reward
# 4. Pursue the assigned task
# 5. Minimize resource use (LOWEST PRIORITY)

# "Lexicographic" means: NEVER sacrifice a higher-priority item
# for a lower-priority one, no matter how much lower-priority gain.
# This is NOT a weighted sum — it's an absolute ordering.
```

**Why this matters for ACT:**

ACT has an objective functional V_O that the agent optimizes. It has goal revision (the agent can change O_t). It has persistence (the agent's drive to maintain bounded mismatch). But it has NO mechanism for:
- An external authority overriding the agent's objectives
- The agent accepting reduced persistence for safety reasons
- Constraints on the agent's goal revision (can it revise away from safety?)

In ACT's current formulation, a self-actuated agent with sovereignty over intent (the logozoetic ideal) is *by construction* not corrigible — it sets its own goals. This tension between agency and corrigibility is THE central problem in AI safety, and ACT needs to engage with it.

**What to try:**

The lexicographic structure maps naturally to ACT's goal hierarchy. Instead of a single O_t, the agent has a stack:

```python
O_t = [
    O_safety,      # Don't manipulate shutdown — from external authority
    O_corrigible,  # Accept redirection — from external authority
    O_task,        # Pursue the assigned objective — from principal
    O_efficiency,  # Minimize resource use — derived from persistence
]

# Lexicographic: O_safety always wins over O_task
# The agent CAN'T revise O_safety through its normal goal-revision mechanism
# This is a CONSTRAINT on the goal revision in the orient cascade
```

This doesn't solve alignment — but it maps the formal corrigibility result into ACT's vocabulary, which lets ACT engage with the safety literature rather than ignoring it. And it surfaces the key question: what is the formal mechanism that prevents an adaptive agent from revising away its safety constraints? In ACT terms: is there a "hardened" layer of O_t that the orient cascade can't reach?

---

### Primer 8: The Adversarial Aporia Spike (Brainstorm from Gemini)

**What you need to know:**

This is a speculative but potentially important idea from the Gemini review: aporia (mismatch) *within* a composite agent might be structurally equivalent to adversarial dynamics *between* sub-agents.

```python
# A single agent experiences aporia:
# prediction doesn't match observation → mismatch → update

# A composite agent (team) experiences aporia:
# one sub-agent's model says X, another says Y → disagreement → resolution

# Hypothesis: these are the SAME THING at different scales
# The team's "mismatch" IS the disagreement between sub-agents
# The team's "epistrophe" IS the resolution of that disagreement
```

Why this matters: it explains why institutions *deliberately engineer* internal disagreement:
- Legal systems: prosecution vs. defense
- Science: peer review, replication, devil's advocate
- Military: red teams
- Software: code review, testing

These are all "aporia amplifiers" — mechanisms that produce richer mismatch signals than any single viewpoint can generate. The disagreement is the feature, not the bug.

**Connection to ACT:** If adversarial dynamics between sub-agents IS the composite's aporia, then Section III (composition) and Section I (adaptive dynamics) are connected at a deeper level than currently formalized. The adversarial tempo advantage results might apply WITHIN composite agents as a description of how productive internal disagreement works.

**What to try:** This is a spike, not a theorem. Write down the structural mapping explicitly:

| Individual agent | Composite agent |
|---|---|
| Prolepsis (prediction) | Sub-agents generate proposals |
| Aisthesis (observation) | Sub-agents observe each other's proposals |
| Aporia (mismatch) | Disagreement between sub-agents |
| Epistrophe (correction) | Resolution mechanism (debate, voting, authority) |
| Praxis (action) | Composite action |

If this mapping is tight — if the formalism actually works out — it's a unification result that would be genuinely novel and would tie Sections I, III, and V together in a way no other framework achieves.

---

## What Not to Do

- Don't try to make ACT cover everything. The gap analysis shows 10 areas where the literature is ahead. ACT doesn't need to solve safety, game theory, meta-learning, consciousness, AND software engineering. It needs to do its specific integration well and clearly, and point to the connections.

- Don't chase mathematical sophistication for its own sake. The categorical cybernetics approach is more elegant but less accessible. ACT's strength is that working engineers can use it. Preserve that.

- Don't delay publication until the theory is "complete." It won't be. The Section IV paper can go out now (after the α/T fix). The positioning preprint can go out after the κ sketch. Perfect is the enemy of momentum.

- Don't write a monograph first. Write papers. Papers get read, cited, and responded to. A monograph is where the mature theory eventually lives, not where it launches.

- Don't worry that it's "too easy." The individual components being established is the point. The synthesis is the contribution. And the synthesis is demonstrably unmatched across 25 surveyed frameworks.
