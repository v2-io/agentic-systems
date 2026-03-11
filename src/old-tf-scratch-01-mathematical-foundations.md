# Mathematical Foundations — Working Draft

## 1. Primitive Objects

We need the minimum set of objects from which everything else can be built.

### 1.1 The Environment

Let Ω denote the state of the environment — the totality of what exists
external to the agent. We make no assumptions about Ω's structure
(continuous, discrete, finite, infinite, stationary, adversarial).

The agent CANNOT access Ω directly. This is not a technological limitation
but a constitutive one: any entity that could directly access the full state
of its environment would BE the environment, not an agent within it.

### 1.2 Observation and Action Spaces

O — the space of possible observations (what the agent can perceive)
A — the space of possible actions (what the agent can do)

The observation function (environment → agent):
  o_t = h(Ω_t, ε_t)
where h is a lossy mapping and ε represents observation noise/limits.

The action effect (agent → environment):
  Ω_{t+1} = T(Ω_t, a_t, ξ_t)
where T is the (possibly stochastic) transition and ξ represents
environmental stochasticity.

Key: The agent knows neither h nor T exactly. These are part of what
the model must approximate.

### 1.3 Interaction History

The complete record available to the agent:

  H_t = (o_1, a_1, o_2, a_2, ..., a_{t-1}, o_t)

This is the ONLY raw material the agent has. Everything else must be
constructed from this.

Note: In the event-driven formulation, this becomes:
  H_τ = {(e_i, τ_i) : τ_i ≤ τ}
where events include both observations and action completions, each
with its own timestamp.


## 2. The Model

### 2.1 Model as Compression

Definition: A MODEL M_t is a compression of the interaction history:

  M_t = φ(H_t)

where φ: H* → M maps histories to elements of a model space M.

The model space M is itself a choice — it determines what kinds of
representations the agent CAN maintain. Different M spaces yield
different agent architectures:
  - M = R^n (state vector) → Kalman filter, state estimators
  - M = Δ(Θ) (distribution over parameters) → Bayesian agents
  - M = {Q: S×A → R} (action-value functions) → RL agents
  - M = neural network weights → deep learning agents
  - M = (organizational procedures, shared beliefs) → organizations

### 2.2 Sufficient Statistic Property

A model is ADEQUATE if it is a sufficient statistic for the history
with respect to future prediction:

  I(H_t; o_{t+1:∞} | M_t, a_{t:∞}) = 0

i.e., knowing the full history H_t gives no additional predictive
power beyond knowing M_t, given future actions.

When this holds:
  M_t = f(M_{t-1}, o_t, a_{t-1})

The model can be updated recursively — you don't need the full history.

NOTE: Perfect sufficiency is an ideal. Real models are approximately
sufficient. The DEGREE of sufficiency is itself a measure of model quality:

  S(M_t) = 1 - I(H_t; o_{t+1:∞} | M_t, a_{t:∞}) / I(H_t; o_{t+1:∞} | a_{t:∞})

S = 1 means perfectly sufficient. S = 0 means the model captures nothing.

### 2.3 Model Quality as Compression Efficiency

The information bottleneck gives us a formal measure. A model trades off:

  Compression: I(M_t; H_t)  — how much of the history it retains
  Prediction:  I(M_t; o_{t+1:∞} | a_{t:∞})  — how much it predicts

The optimal model at a given compression level β:

  M* = argmin_{φ} [I(M; H) - β · I(M; future | actions)]

Different β values trace out a curve of Pareto-optimal models.
Small β → aggressive compression, lossy prediction.
Large β → faithful history, accurate prediction but expensive.

This IS the rate-distortion curve for the agent's epistemic problem.

### 2.4 Model Space as Meta-Parameter

The choice of M constrains what models are representable. If M cannot
contain any good sufficient statistic for the actual environment dynamics,
no amount of parameter updating within M will produce an adequate model.

Define MODEL CLASS FITNESS:

  F(M) = max_{M ∈ M} S(M)

The best achievable sufficiency given the model class.

When F(M) is poor, the agent needs STRUCTURAL adaptation — changing M
itself. This is:
  - Neural architecture search in ML
  - Paradigm shift in science (Kuhn)
  - Destruction and creation in Boyd
  - Model class selection in Bayesian nonparametrics

The agent's full adaptive state is therefore the pair (M_t, M_t),
evolving at different timescales.


## 3. The Mismatch Signal

### 3.1 Definition

Given model M_{t-1} and action a_{t-1}, the model generates a prediction:

  ô_t = E[o_t | M_{t-1}, a_{t-1}]

(or more generally, a predictive distribution P(o_t | M_{t-1}, a_{t-1}))

The mismatch signal:

  δ_t = o_t - ô_t

In the distributional case, this generalizes to:

  δ_t = -∇_M log P(o_t | M_{t-1}, a_{t-1})

(the score function — direction of steepest increase in likelihood
of the actual observation under the model)

### 3.2 Properties of δ_t

If the model is perfect (M perfectly predicts o given a), δ_t = 0 always.

If the model is completely wrong, δ_t is large and unpredictable.

The EXPECTED magnitude of δ:

  E[|δ_t|²] = model_error² + irreducible_noise²

The model can only drive the first term to zero. The second term
(aleatoric uncertainty) is a property of the environment, not the model.

This distinction matters: an agent that tries to eliminate ALL mismatch
(including irreducible noise) will OVERFIT — it will adjust its model
to explain noise, degrading future predictions. This is where the
update gain η becomes critical.

### 3.3 Mismatch as Information

The mismatch signal carries information:

  I(δ_t; Ω_t | M_{t-1}) > 0  when model is imperfect

Each mismatch event tells the agent something about the gap between
its model and reality. The agent that ignores mismatch signals loses
information. The agent that overreacts to them (high η) treats noise
as signal. The optimal η MAXIMIZES the information extracted from δ_t
for model improvement.

### 3.4 Zero Mismatch Ambiguity

IMPORTANT: δ_t ≈ 0 does NOT necessarily mean the model is good.
It means the model's predictions match observations — which could be because:
  a) The model is accurate (true low mismatch)
  b) The agent is only observing things the model already explains
     (confirmation bias / insufficient exploration)
  c) The observation channel is too noisy to detect model errors
     (low signal-to-noise ratio)

Only (a) is desirable. This is why ACTIVE TESTING (choosing actions
that discriminate between model states) is essential — it converts
case (b) into genuine signal.


## 4. The Update Rule

### 4.1 General Form

  M_t = M_{t-1} + η(M_{t-1}, o_t) · g(δ_t)

where:
  η: update gain (how much to adjust)
  g: mismatch transformation (what direction to adjust)

### 4.2 The Optimal Gain

Claim (to be validated per domain): The optimal gain balances
model uncertainty against observation uncertainty:

  η* = U_M / (U_M + U_o)

where U_M = model uncertainty, U_o = observation uncertainty.

**Kalman filter (exact derivation):**
  K_t = P_t H^T (H P_t H^T + R)^{-1}

  Here P_t is model uncertainty (state covariance),
  R is observation noise covariance,
  H maps state to observation space.

  K_t literally IS P_t H^T / (P_t H^T + R) in scalar case = U_M / (U_M + U_o). ✓

**Bayesian posterior (exact):**
  P(θ|D) ∝ P(D|θ) · P(θ)

  In exponential family with conjugate priors, the posterior mean is:
  θ_posterior = (n/(n+κ)) · θ_data + (κ/(n+κ)) · θ_prior

  where n = data count (more data → trust data more),
  κ = prior strength (stronger prior → trust prior more).

  This is (observation info) / (observation info + prior info),
  which is exactly U_M / (U_M + U_o) from the MODEL's perspective
  (uncertain model → trust data; certain model → trust prior). ✓

**RL (approximate):**
  Standard TD update: Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)]

  Fixed α doesn't adapt to uncertainty. But OPTIMAL RL methods do:
  - Bayesian RL: maintains posterior over Q, update weight depends on uncertainty
  - UCB: exploration bonus ∝ uncertainty
  - Thompson sampling: acts on sampled model, implicitly weighting by uncertainty

  The fixed-α case is a DEGENERATE form where η is constant rather
  than adapted. This is known to be suboptimal — learning rate schedules
  and adaptive methods (Adam, etc.) exist precisely to approximate
  the uncertainty-adapted gain. ✓ (approximately)

**PID (loose mapping):**
  u(t) = K_p · e(t) + K_i · ∫e(τ)dτ + K_d · de/dt

  The gains K_p, K_i, K_d are typically tuned offline, not adapted online.
  Auto-tuning methods (Ziegler-Nichols, relay feedback) estimate
  plant characteristics to set gains — effectively estimating system
  uncertainty. But the mapping to U_M / (U_M + U_o) is loose.

  PID is perhaps best understood as a SIMPLIFIED instance where the
  gain is fixed at design time rather than adapted continuously.
  Model Predictive Control (MPC) is the more general control-theory
  instance that does adapt. ✓ (with caveat)

### 4.3 Gain Adaptation Dynamics

The gain itself must change over time. In general:

  - Early (high model uncertainty): η should be large (learn fast)
  - Late (low model uncertainty): η should be small (maintain stability)
  - After structural change: η should RESET to large (re-learn)

This is:
  - Kalman filter convergence (P_t → steady state → K_t → steady state)
  - RL learning rate annealing
  - Bayesian posterior concentration
  - The "unlearning" problem when environment shifts

The gain reset after structural change connects to destructive renewal:
when M changes, the model is newly uncertain, so η should spike.


## 5. Action Selection

### 5.1 Action as Model Function

Action selection is a FUNCTION of the model, not a separate process:

  a_t = π(M_t)    [deterministic]
  a_t ~ π(·|M_t)  [stochastic]

where π is the policy / control law / decision rule.

Key insight: when the model is GOOD (sufficient, well-calibrated),
the policy can be implicit — embedded in the model's structure
rather than requiring deliberate computation. This is:
  - Boyd's implicit guidance and control (IG&C)
  - Expert intuition (System 1 / Kahneman)
  - A well-tuned PID controller
  - A trained RL policy in exploitation mode

Explicit deliberation (planning, search, simulation) is the FALLBACK
when the model is uncertain or stakes are high:
  - Boyd's explicit Decide step (rare in experts)
  - MCTS / planning in RL
  - MPC's online optimization
  - Human System 2 reasoning

### 5.2 Exploration vs. Exploitation

The agent faces a fundamental trade-off in action selection:

  Exploit: choose a_t to maximize immediate predicted value given M_t
  Explore: choose a_t to maximize information gained about M_t's errors

Exploitation uses the model AS-IS. Exploration tests the model.

The optimal balance depends on:
  - Model uncertainty (high → explore more)
  - Time horizon (long → explore more early)
  - Cost of exploration (high → explore less)
  - Mismatch history (persistent δ ≠ 0 → explore the source)

This connects to Active Testing (Section 3.4): actions that generate
maximally informative mismatch signals are the ones that test the
model most aggressively.


## 6. Event-Driven Temporal Dynamics

### 6.1 Multi-Rate Formulation

Replace the single time index t with an event stream:

  E = {(e_i, τ_i) : i = 1, 2, ...}

Each event e_i is typed:
  - Observation from channel k: e_i = (obs, k, o^(k))
  - Action completion on channel j: e_i = (act, j, result^(j))

The model updates on each event:
  M_{τ+} = f(M_{τ-}, e_τ)

Different channels have different characteristic rates ν^(k), ν^(j).

### 6.2 Channel-Specific Gains

Each observation channel may have its own reliability:

  η^(k) = U_M^(k) / (U_M^(k) + U_o^(k))

where U_M^(k) is the model's uncertainty about what channel k reveals,
and U_o^(k) is channel k's noise level.

A noisy channel (high U_o^(k)) gets low gain — its observations
don't shift the model much. A reliable channel gets high gain.

### 6.3 Effective Adaptation Rate

The agent's overall adaptation rate combines across channels:

  ν_eff = Σ_k ν^(k) · η^(k)*

Each channel contributes its rate × its information efficiency.

This gives the steady-state mismatch equation:

  |δ|_ss = ρ / ν_eff = ρ / Σ_k (ν^(k) · η^(k)*)

### 6.4 Temporal Nesting

Channels naturally stratify by rate:
  - Fast channels (high ν): handle immediate perturbations
  - Slow channels (low ν): structural model updates

Constraint: faster loops must approximately converge before
slower loops can meaningfully act. If a slow loop adjusts
the model structure while fast loops are still adapting
to the last change, the system oscillates.

This creates a HIERARCHY of timescales, each operating on
the quasi-steady-state output of the one below it.
This is:
  - PID's P/I/D terms (fast/medium/slow)
  - RL's policy evaluation (fast) vs. policy improvement (slow)
  - Organizational operations (fast) vs. strategy (slow)
  - Boyd's tactical (fast) vs. strategic (slow) OODA loops
  - Biological reflexes (fast) vs. learning (medium) vs. evolution (slow)


## 7. Adversarial Dynamics (Derived)

### 7.1 Coupled Agents

Two agents A and B, each modeling an environment that INCLUDES the other:

  Ω_A includes B's actions → ρ_A depends on B's adaptation rate
  Ω_B includes A's actions → ρ_B depends on A's adaptation rate

In the simplest coupling:
  ρ_B ≈ ν_A · η_A* · |Δa_A|  (rate at which A changes B's world)
  ρ_A ≈ ν_B · η_B* · |Δa_B|

### 7.2 Steady-State Mismatch Ratio

  |δ_B|_ss / |δ_A|_ss = (ν_A · η_A*) / (ν_B · η_B*)

When this ratio > 1: B is falling behind; A is "inside B's loop."
When >> 1: B's model becomes disconnected from reality (effects spiral).

### 7.3 The Speed-Quality Product

Define ADAPTIVE TEMPO:  T_A = ν_A · η_A*

This single quantity captures an agent's capacity to keep up
with environmental change. The adversarial advantage is the
RATIO of adaptive tempos.

Speed (ν) and quality (η*) are substitutable:
  - Doubling speed has the same effect as doubling update quality
  - But they compound: improving both multiplies the advantage

### 7.4 Critical Threshold

In the non-adversarial case, there's a survival threshold:

  T_agent = ν · η* > ρ  (adapt faster than environment changes)

Below this: mismatch grows without bound → model failure → extinction.
Above this: mismatch bounded → sustainable adaptation.

This threshold existence is what makes both speed and quality matter —
the question is always whether T_agent > ρ_environment.


## 8. Edge Cases and Limitations to Check

- Does the formalism handle the case where the agent HAS no model
  (pure reactive systems like Brooks' subsumption architecture)?
  → Possibly: the "model" is implicit in the wiring. M is the architecture.
  → But can this be made precise without stretching the definition?

- Swarm/collective intelligence: is the "agent" the individual or the swarm?
  → The formalism should work at both levels, but this needs checking.

- Equilibrium systems: a thermostat at setpoint has δ ≈ 0 and acts
  occasionally. Does the formalism degenerate gracefully?
  → Should be fine: low ρ → low ν_eff needed → infrequent updates.

- Creative/generative systems: is art-making a feedback loop?
  → Maybe at the technique level, but the creative vision isn't clearly
  a mismatch-reduction process. This may be a genuine boundary.

- Mathematical proof: is theorem-proving a feedback loop?
  → Each proof attempt generates "observations" (does this step work?).
  → The "model" is the proof strategy. δ is the gap between expectation
  and result. Possibly fits, but feels like a stretch.


## 9. Questions for Next Iteration

1. Should TF-01 be the scope definition (like TST's T-03) or the
   interaction history definition? What's the true starting point?

2. How many axioms vs. definitions vs. derived results?
   TST has 2 axioms (T-01, T-02), then derives. We might need
   fewer axioms if the math is tight enough.

3. Where does action selection (Section 5) sit? Is it an axiom
   (agents act) or derived from the model formalism?

4. The information bottleneck formulation (2.3) is elegant but
   may be too technical for early in the document. Placement?

5. How explicit should we be about the FEP connection?
   (Derive it as a consequence? Note it as related work?)
