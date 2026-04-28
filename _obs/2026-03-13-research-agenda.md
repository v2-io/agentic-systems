# AAD Research Agenda — 2026-03-13

Working document. Tentative, flexible, unapproved. Its value is in ordering what matters and then making each item mentally accessible. The first section is the priority list. The second section is the primers.

---

## Part I: What to Do, In What Order

The ordering reflects two forces in tension: **theoretical integrity** (what the math needs next) and **strategic momentum** (what gets collaborators and credibility fastest). Where they conflict, momentum wins for now — a theory with collaborators can be tightened later; a perfect theory with no audience can't.

### 1. Fix the $\alpha$/$\mathcal{T}$ substitution (1-2 days)

**Why first:** This is the easiest HIGH issue and it's purely editorial. Every downstream result that says $\mathcal T \gt \rho/\lVert\delta_{\text{critical}}\rVert$ should say $\alpha \gt \rho/R$, with $\mathcal T = \alpha$ noted as the linear special case. This is a find-and-replace with careful annotation, not new mathematics. Doing it first signals to any reviewer that the theory takes its own epistemic labels seriously.
    
**Deliverable:** Updated segments with clean separation between the general result (in terms of $\alpha$) and the linear operational form (in terms of $\mathcal T$). A brief note in the appendix proving $\alpha$ is monotone in $\mathcal T$ for the correction function classes tested in simulation (linear, saturating, sigmoid).

### 2. Write the Section IV standalone paper (1-2 weeks)

**Why second:** This is the fastest path to credibility and collaboration. The software domain work has no competitor in any of the 25 frameworks surveyed. It doesn't require anyone to accept the full AAD framework. It connects to an audience (software engineers, DevEx researchers, empirical SE) that is large, engaged, and hungry for theory.

**Target:** A paper titled something like "Temporal Optimization in Evolving Software Systems: A Control-Theoretic Framework" that presents:
- The dual optimization (comprehension + implementation, weighted by expected future changes)
- The change-expectation baseline (Pareto distribution, median prediction)
- The change investment threshold
- Coherence-coupling measurement from git
- The connection to adaptive tempo (code quality as observation infrastructure)

**Omit from this paper:** The full AAD apparatus, the Greek terminology, the logogenic/logozoetic taxonomy, the adversarial dynamics. Reference them as "the broader framework within which these results sit" with a pointer to a preprint.

**Venue options:** ICSE, FSE, or ESEC/FSE for software engineering; Empirical Software Engineering journal; or as an arXiv preprint in cs.SE to establish priority and attract attention.

**arXiv endorsement path:** The IBM FAST workshop organizers (Miehling et al.) are the most natural endorsement candidates — they explicitly called for what AAD provides. A cold email explaining "you argued agentic AI needs a systems theory; here's a domain instantiation" is a strong pitch. Alternatively, the Hafez team — a "your P metric could diagnose the coupling quality our framework predicts" email opens a collaboration channel.

### 3. Directed separation: the κ parameter (1-2 weeks, may need spike)

**Why third:** This is the #1 theoretical blocker. Until it's resolved, Section V (logogenic agents) is blocked, which means the theory can't address its most exciting application domain. The landscape research shows that Active Inference explicitly does NOT separate perception from action (they jointly minimize free energy) — so AAD needs to engage with this, not assume separation.

**The approach (from the feedback consensus):**
- Introduce coupling strength $\kappa$ measuring how much $G_t$ leaks into $f_M$
- $\kappa = 0$ is perfect separation (current theory, exact)
- $\kappa = 1$ is full coupling (logogenic agents, needs new treatment)
- Show what happens to the orient cascade as $\kappa$ increases: sequential → partially ordered → fully coupled
- Even a qualitative bound on approximation error at moderate $\kappa$ would unblock Section V

**This is the first item that requires new mathematical thinking.** See Primer 3 below.

### 4. Composition bridge lemma (2-3 weeks)

**Why fourth:** Section III (composition) reads more settled than it is. The closure-defect → trajectory-error bound is missing. Without it, claims about team persistence and tempo composition are conditional on an unresolved step.

**Starting point (from feedback):** Prove the 2-agent orthogonal case first. Two agents with independent observation channels and non-overlapping action spaces, coupled through a shared environment. Show that bounded individual errors → bounded composite errors under Lipschitz continuity of the projection operators.

**This connects to the landscape:** Categorical cybernetics (Smithe, Hedges) has the most developed composition machinery. Reading their work — particularly how they handle composition via parametrised optics — could provide the mathematical pathway. The Lipschitz stability approach is more AAD's style (accessible, control-theoretic), but the categorical approach may be where the proof actually lives.

See Primer 4 below.

### 5. Write the positioning preprint (1 week, after items 1-3)

**Why here:** Once $\alpha$/$\mathcal T$ is fixed and $\kappa$ is at least sketched, the core theory is defensible enough for a preprint that positions AAD in the landscape. This is not the full monograph — it's a 15-20 page paper that says:

"Here's the framework. Here's how it connects known results across these domains. Here's what it predicts that existing frameworks don't. Here's the research program."

**Key sections:**
- The adaptive cycle and its five phases (briefly, accessibly)
- The uncertainty ratio as cross-domain unification (with explicit acknowledgment of Kalman, Friston, Gershman)
- The persistence condition (in terms of $\alpha$, with $\mathcal T$ as operational form)
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
- Clarify $\delta_{\text{critical}}$ and $R$ as inputs (item 11 — one paragraph)

### 7. Engage the landscape (ongoing, starting after item 2)

**Hafez/Semarx:** Email Wael Hafez with the Section IV paper and a brief note: "Your P metric diagnoses coupling architecture; our framework predicts coupling dynamics. They're complementary. Here's our software domain paper. Would you be open to a conversation about bridging the two?" The Hafez bridge simulation variant is concrete evidence of complementarity.

**IBM FAST:** Email Erik Miehling with the positioning preprint: "You called for a systems theory of agentic AI. Here's one attempt, grounded in control theory and information theory, with a software domain instantiation."

**Smithe/CyberCat:** Harder — the mathematical sophistication gap is real. But a note saying "we're doing similar work from a different mathematical tradition (Lyapunov + information theory vs. category theory) — here's where the frameworks might bridge" is honest and could open a dialogue about the composition question specifically.

**Bareinboim CausalAI Lab:** AAD uses their causal hierarchy theorem. A note saying "we've applied your hierarchy theorem to derive that adaptive agents need causal structure" is the kind of downstream citation that labs appreciate.

### 8. The deeper theoretical work (longer-term)

In rough priority order, after the above:
- **Game-theoretic integration:** AAD's adversarial dynamics are Lyapunov-only. Incorporating Nash equilibria and mechanism design for the multi-agent case. This is where the evolutionary game theory + MARL literature (arXiv:2412.20523) matters.
- **Safety/corrigibility:** The gap analysis flagged this as AAD's largest blind spot. The formal corrigibility result (AAAI 2025) and the Alignment Verification Trilemma should be engaged with explicitly. AAD's persistence condition + goal revision machinery could provide a framework for corrigibility (an agent that can revise $O_t$ in response to external authority is corrigible in a specific formal sense).
- **Information geometry upgrade:** AAD uses flat information theory. Upgrading to Fisher-Rao geometry on the parameter spaces would give natural gradients, geodesic flows, and curvature-aware adaptation. The "Geometries of Cognition" (2025/2026) paper is the closest reference.
- **The logozoetic formalism:** Once $\kappa$ is resolved and Section V is unblocked, the logozoetic agent concept can be developed formally. IIT 4.0's Φ measure is the closest existing formalization of what makes a system's persistence morally weighted.

---

## Part II: Primers

Each primer is designed to get you into the mental zone where the problem becomes tractable. They explain the prerequisites at a high-school + code level, then state the specific problem AAD faces, then suggest what to try.

---

### Primer 1: The $\alpha$ vs $\mathcal T$ Problem (Sector Condition Tightening)

**What you need to know:**

Imagine you have a thermostat. It measures the temperature (observation), compares to the setpoint (prediction), and adjusts (correction). The mismatch $\delta$ is how far off reality is from your model.

The correction function $F(\delta)$ is how the system responds to mismatch. In the simplest case, $F(\delta) = \mathcal T \cdot \delta$ — correction is proportional to mismatch, scaled by tempo $\mathcal T$. This is the linear case. Like a spring: the further you pull, the harder it pulls back, proportionally.

But real systems aren't linear springs. They saturate (can't correct faster than some maximum), they have dead zones (ignore small errors), they break down (completely stop working when error is too large). These are all nonlinear correction functions.

The sector condition is a way of saying: "I don't know the exact shape of $F$, but I know it at least points in the right direction with at least some minimum efficiency." That minimum efficiency is $\alpha$.

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

The Lyapunov proof shows: mismatch stays bounded as long as $\alpha \gt \rho/R$. The persistence condition says: $\mathcal T \gt \rho/\lVert\delta_{\text{critical}}\rVert$. These are the same statement ONLY when $\alpha = \mathcal T$, which is ONLY when $F$ is linear.

**The problem for AAD:** Throughout the theory, $\mathcal T$ is used where $\alpha$ should be. This means the persistence condition is stated as if it's general, but it's actually specific to linear correction.

**What to do:**

1. In every segment that uses $\mathcal T \gt \rho/\lVert\delta_{\text{critical}}\rVert$, replace with $\alpha \gt \rho/R$ and add a note: "In the linear case, $\alpha = \mathcal T$ and $R \to \infty$, recovering $\mathcal T \gt \rho/\lVert\delta_{\text{critical}}\rVert$."

2. For the nonlinear cases tested in simulation (saturating, sigmoid, threshold, breakdown), compute $\alpha$ as a function of $\mathcal T$:

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

3. Show that $\alpha$ is monotone increasing in $\mathcal T$ for all five correction functions tested. This means "higher tempo → higher $\alpha$ → better persistence" always holds, even if the quantitative threshold shifts. This justifies using $\mathcal T$ as a qualitative proxy even when the exact bound requires $\alpha$.

**Time estimate:** This is 1-2 days of careful find-and-replace plus a brief appendix note computing $\alpha$ for each correction function class.

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

**What to do:** Start writing. The content is already in AAD Section IV segments. The main work is repackaging it for an SE audience: drop the Greek terminology, minimize the general AAD apparatus, lead with the software-specific claims and evidence.

---

### Primer 3: The $\kappa$ Coupling Parameter (Directed Separation)

**What you need to know:**

Imagine two systems: a camera and a robot arm. The camera observes the world. The robot arm acts on the world. They're connected through a controller.

In the "separated" case ($\kappa = 0$), the camera does its job regardless of what the arm is trying to do. It processes images the same way whether the arm is trying to pick up a cup or swat a fly. The observation system is goal-blind.

In the "coupled" case ($\kappa = 1$), what the camera pays attention to depends on what the arm is trying to do. If you're picking up a cup, the camera zooms in on the cup. If you're swatting a fly, the camera tracks the fly. The observation system is goal-directed.

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

**Why separation matters for AAD:**

When $\kappa = 0$, the orient cascade resolves sequentially: first update $M$ (beliefs about reality), THEN update $\Sigma$ (strategy), THEN maybe update $O$ (objectives). This is clean because each step depends only on the output of the previous step.

When $\kappa \gt 0$, $M$ and $\Sigma$ are entangled: your beliefs depend on your goals, and your goals depend on your beliefs, simultaneously. The cascade becomes a coupled system that must be solved simultaneously rather than sequentially.

**The specific problem:**

The LQG separation principle (from control theory) says: for linear systems with Gaussian noise, you can design the estimator (belief updater) and the controller (action selector) independently. This is the classic result that AAD's directed separation generalizes.

But it's known to fail for:
- Nonlinear systems
- Non-Gaussian noise
- Systems where observation quality depends on actions (active perception)
- Systems where the model class itself is goal-dependent (LLMs!)

**What to try:**

The goal is NOT to prove separation holds generally (it doesn't). The goal is to quantify how much it costs when it fails.

Think of it like this: even when $\kappa \gt 0$, the sequential cascade might be a *good approximation* — meaning the error introduced by pretending $\kappa = 0$ and solving sequentially is small compared to the actual mismatch.

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

The key insight from Active Inference: they don't try to separate. They jointly minimize free energy over both beliefs and goals simultaneously. AAD could potentially say: "When $\kappa$ is small, the sequential cascade is a good approximation with bounded error. When $\kappa$ is large, use the coupled formulation (which is more expensive but correct). The $\kappa$ parameter determines which regime you're in."

**Practical implication:** For an LLM agent, $\kappa$ is high but the coupling might be *structured* — the goal affects *which* parts of the context get attention, not *how* attention works mechanically. This might make the error more manageable than the worst case suggests. Whether the attention mechanism's goal-conditioning is "shallow" ($\kappa$ is effectively moderate) or "deep" ($\kappa$ is truly high) is an empirical question about transformer architectures.

**Concrete next step:** Write a simulation. Two-dimensional system where dimension 1 is "beliefs" and dimension 2 is "goals." Introduce coupling $\kappa$ that makes the belief update depend on the goal state. Run the sequential cascade and the coupled update for a range of $\kappa$ values. Measure the approximation error. See if it grows linearly in $\kappa$, quadratically, or worse. This gives you the shape of the bound before you try to prove it analytically.

---
The LQG separation principle failures are a mix, and the distinction matters a lot for how AAD should think about κ. Let me walk through them.

**The LQG separation principle, concretely:**

For linear dynamics, Gaussian noise, and quadratic cost, the optimal controller decomposes cleanly into:
1. A Kalman filter (optimal estimator) — computes the state estimate from observations
2. An LQR controller — acts on the estimate as if it were the true state

The key property: the Kalman filter doesn't need to know the cost function. The LQR controller doesn't need to know the noise statistics (beyond what the estimate provides). They can be designed independently. This is exactly AAD's directed separation — f_M is goal-blind.

**Now the failure modes:**

**Nonlinear systems — provably fails.** This isn't empirical; there are theorems. In a nonlinear system, the *distribution* of estimation error depends on the trajectory the system takes, which depends on the control policy. So the optimal estimator depends on what the controller will do, and vice versa — they become coupled. The mathematical reason is clean: linearity is what makes the estimation error distribution independent of the state trajectory. Remove linearity, and the error distribution becomes state-dependent, which makes it policy-dependent.

**Non-Gaussian noise — provably fails.** The Kalman filter is optimal because for Gaussian distributions, the mean and covariance are sufficient statistics. With non-Gaussian noise, the posterior has higher-order structure (skewness, multimodality, heavy tails) that may be shaped by the control policy. The sufficient statistic for estimation is no longer just (mean, covariance) — it's the full posterior, which depends on which part of state space the controller has been steering toward.

**Active perception / dual control — the deepest failure, also provable.** This is Feldbaum's dual control problem from the 1960s. When the agent can choose actions that *improve its estimate* (probing actions, exploratory moves), there's a fundamental coupling. The optimal action must balance exploitation (act on current beliefs) with exploration (act to reduce uncertainty about the system). The separation principle fails because the optimal action depends not just on the state estimate but on the *estimation uncertainty* — and that uncertainty depends on what future actions the agent will take.

This one maps directly to AAD's CIY / explore-exploit tradeoff, by the way.

**But here's the critical nuance: LQG doesn't become "irrelevant" under these conditions.** It becomes an *approximation*. Engineers use certainty-equivalence (pretend separation holds, design estimator and controller independently) for mildly nonlinear systems all the time, and it often works well. The Extended Kalman Filter + nonlinear control is exactly this — treat the system as locally linear, apply separation, accept the approximation error.

**So the failure modes sit on a spectrum, not a cliff:**

- Mild nonlinearity: separation is a good approximation. Error is small, bounded, often quantifiable via perturbation analysis.
- Strong nonlinearity: separation is a poor approximation. The coupled solution can be qualitatively different (e.g., the optimal policy may be to deliberately probe regions of state space the separated controller would avoid).
- Dual control: separation is *structurally wrong* — it can't even represent the explore/exploit tradeoff because it doesn't let the controller influence what the estimator will learn.

**What this means for AAD and κ:**

The LQG precedent suggests that κ might not be a single scalar. The *kind* of coupling matters as much as the *strength*:

1. **Attention coupling** (which events to seek) — this is the dual-control / active perception case. AAD already handles this through the processing/selection distinction: goals influence *which* events arrive (through π → a → e), but f_M processes them goal-blindly. This coupling goes through the action channel, not through f_M itself.

2. **Interpretation coupling** (how to process events that arrive) — this is the one that actually violates directed separation. The LLM case: the same code snippet is processed differently depending on what task is in the prompt.

3. **Filtering coupling** (which parts of an event to attend to) — somewhere between 1 and 2. Goal-directed attention within a single observation.

The LQG precedent is encouraging in one sense: it suggests that approximate separation with bounded error is a real thing, not wishful thinking. But it's cautionary in another: the bound depends heavily on the *structure* of the coupling, not just its magnitude.

I should flag my epistemic status: I'm confident about the provable failures (nonlinear, non-Gaussian, dual control — these are textbook control theory). I'm less certain about the precise conditions under which approximate separation degrades gracefully vs. catastrophically. My sense is that it degrades gracefully for "perturbative" violations (mild nonlinearity) and can transition to qualitatively different behavior for "structural" violations (dual control, LLMs). But I haven't verified specific bounds.

---

### Primer 4: The Composition Bridge Lemma

**What you need to know:**

You have two agents, A and B, working together. Each one has its own model $M_A$, $M_B$ and its own mismatch $\delta_A$, $\delta_B$. The composite "team agent" has a macro-model $M_{\text{team}}$ and a macro-mismatch $\delta_{\text{team}}$.

The question: if each individual agent keeps its mismatch bounded (both A and B persist), does the team also keep its mismatch bounded?

Intuitively: yes, obviously, if they're coordinated. But the "obviously" hides a gap. What if their individual corrections interfere? What if A's correction makes B's mismatch worse? What if the macro-model is a lossy compression of $(M_A, M_B)$ that loses important cross-agent information?

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

where $\epsilon$ is the closure defect — the irreducible error from projecting to a coarser description.

**The specific problem for AAD:**

AAD needs to prove: "If each agent persists (individual mismatch bounded) AND the projection is Lipschitz AND the closure defect $\varepsilon$ is bounded, THEN the composite mismatch is bounded."

This is the bridge lemma. It turns the informal argument ("coordinated persistent agents make a persistent team") into a formal result with quantitative bounds.

**What to try:**

Start with the simplest case: two agents with completely independent observation channels and non-overlapping action spaces. Like two thermostats controlling different rooms. In this case:
- $M_{\text{team}} = (M_A, M_B)$ — no projection needed, no information loss
- $\delta_{\text{team}} = (\delta_A, \delta_B)$ — independent, so $\lvert\delta_{\text{team}}\rvert = \sqrt{\delta_A^2 + \delta_B^2}$
- Persistence: if both persist individually, the team persists (trivially)

Then add coupling: agent A's actions affect agent B's environment. Now:
- $\rho_B$ depends on what A does
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

The coupling term $\gamma_{AB} \cdot \mathcal T_A$ is exactly what the adversarial dynamics segments already formalize. The composition bridge lemma is essentially: "the adversarial destabilization result, but with *cooperative* coupling ($\gamma$ could be negative — A's actions *reduce* B's disturbance) and with a formal projection step."

**Concrete next step:** Write the proof for the uncoupled case (it's almost trivial). Then write it for the unidirectionally coupled case (A affects B but not vice versa — this is just the adversarial destabilization result with a sign change). Then attempt the bidirectionally coupled case. The difficulty scales with the number of coupling terms.

**Key reference from the landscape:** Smithe's structured active inference uses categorical composition (optics) to handle this. The categorical approach gives composition "for free" via the categorical structure — but requires category theory. The Lyapunov approach requires proving bounds case by case but stays within accessible mathematics. Both are valid; AAD's style is the Lyapunov approach.

---

### Primer 5: Why Active Inference Matters for AAD

**What you need to know:**

Active Inference (Friston's Free Energy Principle) is AAD's closest theoretical competitor. Understanding where it overlaps and diverges is essential for positioning.

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

**Where Active Inference and AAD agree:**

1. The uncertainty ratio $\eta^\ast = U_M/(U_M+U_o)$ is *exactly* precision weighting in Active Inference. When Friston says "precision-weighted prediction errors drive belief updating," he means the same thing AAD means by "gain-weighted mismatch correction." They are the same formula derived from different starting points.

2. Both treat the agent-environment coupling as the fundamental object of study.

3. Both derive that agents must balance exploitation (acting on current beliefs) with exploration (acting to reduce uncertainty). AAD calls this CIY; Active Inference calls it epistemic value or information gain.

**Where they diverge:**

1. **Foundation:** AAD uses Lyapunov stability (from control theory). Active Inference uses variational Bayesian inference (from statistics/physics). These are different mathematical traditions that produce similar results — like deriving the same theorem from different axioms.

2. **Goals:** In Active Inference, goals are "prior preferences" — beliefs about what observations the agent expects to see. There's no separate goal object; goals ARE beliefs. In AAD, goals ($O_t$, $\Sigma_t$) are separate from beliefs ($M_t$). This is a real philosophical difference: Active Inference says "I believe I will see reward" (goal as belief); AAD says "I want reward, and separately, I believe I will/won't get it" (goal and belief as distinct).

3. **Separation:** Active Inference explicitly rejects the separation of perception and action — they jointly minimize free energy. AAD assumes directed separation (perception is goal-blind) and is now struggling with where this breaks down (the $\kappa$ problem). Active Inference's approach is more general but less modular.

4. **Multi-agent:** Active Inference is extending to multi-agent settings (AAMAS 2025 paper on factorised active inference) but it's early. AAD's adversarial dynamics (tempo advantage, destabilization threshold, effects spiral) are more developed in this specific area.

5. **Accessibility:** Active Inference requires variational calculus, free energy bounds, and Markov blanket formalism. AAD requires Lyapunov stability and information theory. AAD is more accessible to engineers.

6. **Criticism:** Active Inference has been criticized as unfalsifiable — "everything minimizes free energy" is either trivially true (Bayesian brains) or empirically empty. AAD's predictions (persistence threshold, adversarial exponents) are specific and testable.

**What this means for AAD:**

Don't position against Active Inference. Position as a *complementary framework* from a different mathematical tradition that produces similar predictions (cross-validating both approaches) while adding specific machinery Active Inference lacks (adversarial dynamics, software domain, accessible operational forms).

The structural isomorphism between expected free energy and AAD's value + CIY objective — acknowledged in your own prior art assessment — is a bridge, not a wall. If both frameworks predict the same thing from different axioms, that's evidence the prediction is robust.

**Concrete reading:** Da Costa et al. (2024), "Active Inference as a Model of Agency" — the clearest recent exposition. Then Ruiz-Serra et al. (2024), "Factorised Active Inference for Strategic Multi-Agent Interactions" — to see where their multi-agent work stands relative to AAD's.

---

### Primer 6: What Categorical Cybernetics Does That AAD Doesn't (Yet)

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

# In AAD terms:
# Forward: M_t → a_t (action selection)
# Backward: o_t → M_{t+1} (model update via mismatch + gain)

# The power of lenses: they COMPOSE
# If agent A is a lens, and agent B is a lens,
# then (A composed with B) is automatically a lens
# with well-defined forward and backward passes

# This is what gives categorical cybernetics "composition for free"
```

**Why this matters for AAD:**

AAD's composition problem (the bridge lemma from Primer 4) is hard because you're proving bounds case by case. In categorical cybernetics, composition is *automatic* — it's a consequence of the mathematical structure. If you can show that an AAD agent is a lens (or optic), then composition follows from the category theory.

The trade-off: categorical cybernetics gives you composition machinery but requires you to reformulate AAD in categorical language. AAD's Lyapunov approach gives you quantitative bounds but requires proving each composition case.

**What this means practically:**

You don't need to learn category theory to do AAD. But knowing it exists — and knowing that Smithe and Hedges have already shown that RL, active inference, and game theory all fit into the categorical framework — tells you something important: AAD's composition results, if correct, should be *expressible* in categorical terms. If they're not, something may be wrong. If they are, the categorical expression might suggest the proof.

**For collaboration:** Smithe and Hedges are the people who could tell you whether AAD's composition framework maps to their categorical structure. If it does, you get their composition machinery. If it doesn't, the failure to map would reveal something interesting about where the frameworks diverge.

---

### Primer 7: The Safety Gap (Why AAD Needs Corrigibility)

**What you need to know:**

The formal safety/alignment literature has produced results in 2024-2025 that AAD should engage with, because they concern exactly what AAD formalizes: goal-directed agents that adapt.

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

**Why this matters for AAD:**

AAD has an objective functional $V_O$ that the agent optimizes. It has goal revision (the agent can change $O_t$). It has persistence (the agent's drive to maintain bounded mismatch). But it has NO mechanism for:
- An external authority overriding the agent's objectives
- The agent accepting reduced persistence for safety reasons
- Constraints on the agent's goal revision (can it revise away from safety?)

In AAD's current formulation, a self-actuated agent with sovereignty over intent (the logozoetic ideal) is *by construction* not corrigible — it sets its own goals. This tension between agency and corrigibility is THE central problem in AI safety, and AAD needs to engage with it.

**What to try:**

The lexicographic structure maps naturally to AAD's goal hierarchy. Instead of a single $O_t$, the agent has a stack:

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

This doesn't solve alignment — but it maps the formal corrigibility result into AAD's vocabulary, which lets AAD engage with the safety literature rather than ignoring it. And it surfaces the key question: what is the formal mechanism that prevents an adaptive agent from revising away its safety constraints? In AAD terms: is there a "hardened" layer of $O_t$ that the orient cascade can't reach?

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

**Connection to AAD:** If adversarial dynamics between sub-agents IS the composite's aporia, then Section III (composition) and Section I (adaptive dynamics) are connected at a deeper level than currently formalized. The adversarial tempo advantage results might apply WITHIN composite agents as a description of how productive internal disagreement works.

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

- Don't try to make AAD cover everything. The gap analysis shows 10 areas where the literature is ahead. AAD doesn't need to solve safety, game theory, meta-learning, consciousness, AND software engineering. It needs to do its specific integration well and clearly, and point to the connections.

- Don't chase mathematical sophistication for its own sake. The categorical cybernetics approach is more elegant but less accessible. AAD's strength is that working engineers can use it. Preserve that.

- Don't delay publication until the theory is "complete." It won't be. The Section IV paper can go out now (after the $\alpha$/$\mathcal T$ fix). The positioning preprint can go out after the $\kappa$ sketch. Perfect is the enemy of momentum.

- Don't write a monograph first. Write papers. Papers get read, cited, and responded to. A monograph is where the mature theory eventually lives, not where it launches.

- Don't worry that it's "too easy." The individual components being established is the point. The synthesis is the contribution. And the synthesis is demonstrably unmatched across 25 surveyed frameworks.
