# Domain Instantiation Mappings — Verification Draft

For each domain, map: M_t, M, o_t, a_t, δ_t, η_t, φ, π, ν, ρ
and note where the mapping is clean vs. strained.

## 1. Kalman Filter (State Estimation)

| Universal | Kalman |
|-----------|--------|
| M_t | (x̂_t, P_t) — state estimate + covariance |
| M | R^n × S^n_++ (vectors × positive-definite matrices) |
| o_t | y_t = Hx_t + v_t (measurement) |
| a_t | u_t (control input) — often exogenous |
| δ_t | ỹ_t = y_t - Hx̂_{t|t-1} (innovation) |
| η_t | K_t = P_{t|t-1}H^T(HP_{t|t-1}H^T + R)^{-1} (Kalman gain) |
| φ | Recursive: sufficient statistic for linear Gaussian |
| π | Separate (often LQR controller uses x̂_t) |
| ν | Measurement rate |
| ρ | Process noise intensity (how fast true state drifts) |

**Mapping quality: EXACT.** The Kalman filter is arguably the purest
instance of the universal pattern. Every component maps precisely.
The optimal gain formula K_t IS η* = U_M/(U_M+U_o) in matrix form.

**Notes:**
- The Kalman filter SEPARATES estimation (model update) from control
  (action selection). This is the separation principle, which only
  holds for linear Gaussian systems. In general, estimation and
  control are coupled — the optimal action depends on the model,
  and the optimal observation strategy depends on what you plan to do.
- The sufficient statistic property is EXACT here: (x̂_t, P_t)
  captures all information from the history for prediction.
- Extended/Unscented Kalman filters relax linearity — same pattern,
  approximate sufficiency.


## 2. Reinforcement Learning (Value-Based: Q-Learning/DQN)

| Universal | RL |
|-----------|-----|
| M_t | Q(s,a) — action-value function (or V(s), or world model) |
| M | function space {S×A → R} (tabular, neural net, etc.) |
| o_t | (s_t, r_t, s_{t+1}) — state, reward, next state |
| a_t | action chosen by policy |
| δ_t | TD error: r_t + γ max_a' Q(s_{t+1},a') - Q(s_t,a_t) |
| η_t | α (learning rate) — often fixed, ideally adaptive |
| φ | Training process (batch or online) |
| π | ε-greedy, softmax, or derived policy from Q |
| ν | Steps per unit time (environment interaction rate) |
| ρ | Non-stationarity of reward/transition dynamics |

**Mapping quality: GOOD, with caveats.**

The TD error IS a mismatch signal — the difference between predicted
(Q(s,a)) and observed (r + γ max Q(s',a')). ✓

The fixed learning rate α is a DEGENERATE gain — not adapted to
uncertainty. Bayesian RL methods (posterior over Q) and adaptive
optimizers (Adam) approximate the optimal gain more closely. This
is a known limitation of basic Q-learning. ✓

The model space M is critical: tabular Q can represent any function
over finite S×A, but neural Q (DQN) has representational constraints
that determine what environments it can handle. Architecture choice
IS model class selection. ✓

**Where it strains:**
- The reward signal r_t doesn't fit cleanly as an "observation."
  It's part of the observation, but it has a special role — it
  defines what the agent should optimize. In the universal framework,
  "what to optimize" would be part of the model or the fitness
  criterion, not part of the observation. This is a real tension.
  → Resolution: reward can be treated as a CHANNEL — one component
  of the multi-channel observation, specifically the one that
  carries evaluative (vs. descriptive) information.


## 3. Model-Based RL (Dreamer / World Models)

| Universal | World Model RL |
|-----------|---------------|
| M_t | Learned world model P(s_{t+1}|s_t,a_t) + value model |
| M | Neural network parameter space for both models |
| o_t | (s_t, r_t, s_{t+1}) from environment |
| a_t | Action chosen by policy (learned via imagination) |
| δ_t | Reconstruction error + reward prediction error |
| η_t | Optimizer learning rate (Adam, etc.) |
| φ | World model training (gradient descent on experience) |
| π | Policy learned by "dreaming" trajectories in world model |
| ν | Real environment steps + imagined steps |
| ρ | Environment non-stationarity |

**Mapping quality: EXCELLENT.**

Dreamer is perhaps the most explicit implementation of the full pattern:
1. Learn world model from experience (update M from observations) ✓
2. Dream/imagine trajectories (use M for internal simulation) ✓
3. Learn policy from dreams (action selection from model) ✓
4. Act in environment (generate new observations) ✓

The distinction between "real" observations (from environment) and
"imagined" observations (from the world model during dreaming) maps
to the distinction between observation-driven and model-driven
updating. Internal simulation IS the model predicting without
acting — the counterfactual level of Pearl's hierarchy.


## 4. PID Controller

| Universal | PID |
|-----------|-----|
| M_t | (e_t, ∫e dτ, de/dt) — current, accumulated, rate of error |
| M | R^3 (three scalars) — VERY compressed |
| o_t | y_t (process variable measurement) |
| a_t | u_t (control output) |
| δ_t | e_t = r_t - y_t (setpoint - measurement) |
| η_t | (K_p, K_i, K_d) — fixed tuning constants |
| φ | Direct: model IS the error state |
| π | u_t = K_p·e + K_i·∫e + K_d·de/dt (deterministic) |
| ν | Control loop frequency |
| ρ | Disturbance magnitude and frequency |

**Mapping quality: GOOD, with important observations.**

PID is an extremely COMPRESSED instance. The "model" is just three
numbers tracking the error signal. There is no explicit world model,
no prediction of future states, no learned representation. The model
space M = R^3 is tiny.

Yet it works remarkably well for many problems. This is because
the STRUCTURE of the controller (proportional + integral + derivative)
embeds implicit assumptions about the environment:
- Proportional: responds to current mismatch (assumes stationarity)
- Integral: responds to accumulated mismatch (handles steady-state error)
- Derivative: responds to rate of change (anticipates near-future)

These three terms correspond to different TIMESCALES of adaptation,
which maps directly to temporal nesting:
- D-term: fastest (high-frequency response)
- P-term: medium (current state)
- I-term: slowest (long-term bias correction)

**Key insight: PID shows that even a minimal model (3 parameters)
instantiates the universal pattern. The pattern doesn't require
rich internal representations — it describes any coupling between
an agent and its environment through observation and action.**

The gains (K_p, K_i, K_d) are typically FIXED at design time.
Auto-tuning methods estimate them, and adaptive PID adjusts them
online — moving toward the full adaptive gain framework.
MPC (Model Predictive Control) generalizes PID with an explicit
model, adaptive gain, and planning — a richer instantiation.


## 5. Bayesian Inference (General)

| Universal | Bayesian |
|-----------|----------|
| M_t | P(θ|D_{1:t}) — posterior distribution |
| M | Δ(Θ) — distributions over parameter space |
| o_t | D_t (new data) |
| a_t | Experiment design / data collection choice |
| δ_t | P(D_t|θ) evaluated (likelihood — surprise of data) |
| η_t | Implicit in Bayes rule (posterior ∝ likelihood × prior) |
| φ | Bayes' theorem applied recursively |
| π | Bayesian decision theory: maximize expected utility |
| ν | Data arrival rate |
| ρ | Parameter drift rate (non-stationarity) |

**Mapping quality: EXACT (for the parametric case).**

Bayesian inference IS the update rule in its most general form
for parametric models. The posterior concentrates as data accumulates,
which IS the gain decreasing with increasing model confidence.

**Where Bayesian inference is BROADER than our pattern:**
It doesn't require a loop — you can do Bayesian inference on
a static dataset without any actions. Our pattern specifically
requires the action → observation → update cycle.

**Where our pattern is BROADER than Bayesian inference:**
It handles non-parametric models, implicit models, and models
that don't have probability distributions. A PID controller is
not naturally Bayesian, but it instantiates our pattern.

This suggests: Bayesian inference is the SPECIAL CASE of our
update rule when:
- M can be expressed as a probability distribution
- The observation model P(o|M) is known
- The update follows Bayes' theorem exactly

Our pattern encompasses cases where these conditions don't hold.


## 6. Boyd's OODA Loop

| Universal | Boyd's OODA |
|-----------|------------|
| M_t | Orientation — mental model, cultural traditions, genetic heritage, experience, new information |
| M | Space of possible orientations (implicit, never formalized by Boyd) |
| o_t | Observation — "what you see" filtered through orientation |
| a_t | Action — "what you do," fed by decision or implicit guidance |
| δ_t | Mismatch between expected and observed outcomes |
| η_t | Orientation's openness to revision (never formalized) |
| φ | Analysis/synthesis, destruction/creation |
| π | IG&C (implicit) or explicit decision |
| ν | OODA loop rate ("operating tempo") |
| ρ | Adversary's tempo + environmental change rate |

**Mapping quality: STRUCTURAL, not mathematical.**

Boyd never formalized his framework mathematically. The mapping is
structural — every component has a clear correspondence — but Boyd's
terms are descriptive/qualitative where ours are formal.

This is exactly the relationship we want: our theory provides the
formal grounding that Boyd's intuitions lacked. Boyd was right
about the structure but couldn't prove it. We can (partially).

**Key Boyd insights that our formalism captures:**
1. Orient dominates → model primacy (derived from η*'s role)
2. Implicit guidance → action as model function (Section 5.1)
3. Destruction/creation → model class switching (M_t change)
4. Inside the opponent's loop → adversarial tempo ratio (Section 7)
5. Effects spiral → mismatch divergence when T_A >> T_B

**What Boyd had that we should preserve:**
- The emphasis on CULTURAL and EXPERIENTIAL dimensions of orientation
- The recognition that observation is ALWAYS filtered through orientation
  (our h function is implicitly model-dependent — Boyd made this explicit)
- The adversarial focus (our Section 7 derives it but shouldn't lose
  the strategic richness of Boyd's applications)


## 7. Active Inference / Free Energy Principle

| Universal | Active Inference |
|-----------|-----------------|
| M_t | Recognition density Q(s|o) — approximate posterior |
| M | Variational distributions |
| o_t | Sensory observations |
| a_t | Actions that change sensory input |
| δ_t | Free energy F = -log P(o) + D_KL[Q||P(s|o)] |
| η_t | Implicit in variational update (gradient descent on F) |
| φ | Variational inference (minimize F w.r.t. Q) |
| π | Active inference: choose actions that minimize EXPECTED F |
| ν | Sensory processing rate |
| ρ | Environmental volatility |

**Mapping quality: DEEP but with tension.**

Active inference claims to be the universal framework already.
Our relationship to it is subtle:

AGREEMENT: The structure maps almost perfectly. Free energy
IS a measure of model-reality mismatch. Minimizing free energy
IS updating the model to reduce mismatch. Active inference
(choosing actions to minimize expected future F) IS exploration.

DISAGREEMENT: FEP claims that all adaptive systems MUST minimize
free energy — it's not an optimization target but a definitional
property of systems that maintain their form. Our framework doesn't
make this strong claim. We say systems that persist TEND TO have
properties consistent with mismatch minimization, but we don't
derive this from thermodynamic arguments.

OUR FRAMING: Free energy minimization is a CONSEQUENCE of effective
adaptation under our framework, not its foundation. A system that
follows our update rule with good gain will, as a side effect,
minimize something like free energy. But we ground this in
information theory (sufficient statistics, information bottleneck)
rather than in thermodynamics (entropy, self-organization).

This is a real philosophical difference, not just notational.
The FEP says "persistence implies free energy minimization."
We say "effective adaptation has these formal properties, which
in many cases look like free energy minimization."


## 8. PDCA / Lean / Organizational Learning

| Universal | PDCA |
|-----------|------|
| M_t | Current process understanding + performance data |
| M | Space of process designs / organizational knowledge |
| o_t | Performance metrics, defect data, customer feedback |
| a_t | Process changes, experiments, improvements |
| δ_t | Gap between target and actual performance |
| η_t | Organization's rate of implementing learnings |
| φ | Check/Study phase — analyze results, update understanding |
| π | Plan phase — design next experiment based on model |
| ν | PDCA cycle frequency (sprint length, review cadence) |
| ρ | Market change rate, competitor actions, tech evolution |

**Mapping quality: GOOD but looser.**

Organizational learning IS adaptive feedback, but the "model" is
distributed across humans, documents, processes, and culture. It's
not a single mathematical object. The mapping works conceptually
but the formalism can't be applied as precisely as in Kalman or RL.

**Key insight from this mapping:**
The organizational η is often the bottleneck — organizations that
DETECT mismatch but fail to UPDATE their model (bureaucratic inertia,
political resistance, sunk-cost fallacy) have high ν (fast observation)
but low η (poor incorporation of observations into practice).

The adaptive tempo T = ν · η* explains why some organizations with
frequent retrospectives (high ν) still fail to adapt (low η*) —
and why some with infrequent but decisive reviews (lower ν, high η*)
outperform them.


## 9. Biological Immune System

| Universal | Immune System |
|-----------|--------------|
| M_t | Antibody repertoire + immune memory cells |
| M | Space of possible antibody configurations |
| o_t | Pathogen antigens (innate recognition + adaptive detection) |
| a_t | Immune response (inflammation, antibody production, cell killing) |
| δ_t | Pathogen presence that current repertoire doesn't match |
| η_t | Clonal expansion rate / affinity maturation rate |
| φ | Somatic hypermutation + selection (evolutionary within lifetime) |
| π | Innate: hardcoded responses; Adaptive: learned, specific |
| ν | Immune surveillance rate |
| ρ | Pathogen mutation rate + new pathogen exposure rate |

**Mapping quality: SURPRISINGLY GOOD.**

The immune system is essentially a model-updating system:
- "Model" = antibody repertoire (what threats are recognized)
- "Mismatch" = unrecognized pathogen
- "Update" = clonal expansion of B-cells that recognize the pathogen
- "Gain" = how aggressively the immune system responds

Autoimmune disease = model error (attacking self = false positive)
Immunodeficiency = inadequate model (can't recognize threats)
Allergies = miscalibrated gain (overreacting to harmless signals)

The two-timescale structure is explicit:
- Innate immunity: fast, generic (fixed M, high ν)
- Adaptive immunity: slow, specific (M evolves, lower ν but better η*)

This is temporal nesting in a biological system.


## Summary Assessment

EXACT mapping (every component precise): Kalman, Bayesian inference
EXCELLENT mapping (minor caveats): Dreamer/world-model RL, immune system
GOOD mapping (some components loose): PID, value-based RL, PDCA
STRUCTURAL mapping (correct but informal): Boyd's OODA

The formalism is strongest for systems with EXPLICIT mathematical models
and weakest for systems with DISTRIBUTED or IMPLICIT models (organizations,
culture, subsumption architecture).

This is expected and honest — the formalism's value is in providing
the structure that these implicit systems are instances of, even when
the mapping can't be made fully precise. The math grounds the intuition;
the intuition extends beyond what the math can currently reach.
