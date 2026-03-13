# Simulation Proposals

**Status**: Proposals, not implementations. Each simulation is described with its purpose, expected insights, and how it helps shore up the weaker parts of TFT and/or validate the TFT→software mapping. Ordered roughly by expected value per effort.

## Motivation

Both TFT and TST have theoretical claims that would benefit from empirical grounding:

- **TFT's linear mismatch ODE** is explicitly flagged as hypothesis. The quantitative results (steady-state formula, squared tempo advantage) depend on linearity. How far off is the linear approximation in practice?

- **TST's proportionality claims** (T-08: time ∝ changeset size; T-09: proximity affects time) are labeled empirical but lack empirical measurement.

- **The TFT→software mapping** (see mapping.md) is structurally motivated but untested. Do TFT's predictions (persistence threshold, adaptive reserve, gain dynamics) actually predict software development outcomes?

Simulations can address all three. The software domain is particularly amenable to simulation because the environment (codebase) is digital, the history (git) is perfectly recorded, and counterfactual replay is possible.

---

## Simulation 1: Nonlinear Mismatch Dynamics

**Purpose**: Test how far the linear mismatch ODE departs from more realistic
dynamics, and whether the qualitative results (persistence threshold, steady-state
bound) survive.

**For TFT**: This directly addresses TF-11 Open Question #1 — the linear ODE is a
first-order approximation; what happens with saturation, thresholds, and structural
breakdown?

### Setup

Simulate an adaptive agent tracking a drifting target (a simplified version of the
Kalman example in Appendix C, but with controlled nonlinearities):

1. **Environment**: Scalar state x_t following a random walk with drift rate q
   (controllable rho).

2. **Agent**: Maintains estimate x_hat_t, updates via:
   x_hat_{t+1} = x_hat_t + eta * g(delta_t)
   where g is the correction function.

3. **Correction functions to test**:
   - Linear: g(delta) = delta (TFT's current assumption)
   - Saturating: g(delta) = delta / (1 + |delta|/R) (bounded correction at large
     mismatch — plausible for agents with limited update capacity)
   - Threshold: g(delta) = delta * 1[|delta| > epsilon] (dead zone for small
     mismatch — plausible for agents that ignore small surprises)
   - Sigmoid: g(delta) = R * tanh(delta/R) (combines saturation and smoothness)
   - Structural breakdown: g(delta) = delta * 1[|delta| < R_max] (correction fails
     entirely beyond a mismatch radius — TF-10's model class inadequacy)

4. **Measurements**:
   - Steady-state |delta| vs. rho/T (compare to linear prediction)
   - Convergence rate (how fast |delta| decays from initial conditions)
   - Persistence threshold (at what rho does the agent fail?)
   - Distribution of |delta| (the linear ODE predicts a point; nonlinear dynamics
     may produce a distribution)

### Expected Insights

- The saturating case should show higher steady-state mismatch than the linear
  prediction (correction is less effective at large delta, so the system equilibrates
  at a higher level). The persistence threshold should be *harder* to satisfy.

- The threshold case should show a "dead zone" where small mismatch persists
  indefinitely — the agent doesn't bother correcting small errors. This is plausible
  for real systems (developers don't fix trivial naming issues; PID controllers have
  dead bands).

- The structural breakdown case should show catastrophic failure above R_max — a
  sharp transition from bounded mismatch to divergence. This would validate TF-10's
  structural adaptation trigger as a dynamical event, not just an information-
  theoretic observation.

**Effort**: Low-medium. This is a 1D simulation with simple dynamics. Could be done
in Python/NumPy in a few hundred lines.

---

## Simulation 2: Adversarial Coupling and the Squared Tempo Advantage

**Purpose**: Test whether the squared tempo advantage (Cor. 11.2) holds beyond the linear regime, and under what conditions it breaks down.

**For TFT**: This is the most "citable" quantitative result in TFT and the one most at risk from nonlinearity. If the squared relationship is merely a linear artifact, the adversarial analysis needs significant revision. If it's approximately correct even under nonlinear dynamics, the result is much stronger than currently claimed.

### Setup

Two agents A and B, each tracking its own drifting target, with adversarial coupling:

1. **Each agent**: As in Simulation 1, but with a coupling term:
   rho_B = rho_base + gamma_A * T_A (A's actions disrupt B's environment) rho_A = rho_base + gamma_B * T_B

2. **Vary**: T_A/T_B ratio from 0.5 to 5.0, gamma_A/gamma_B from 0.5 to 2.0, and test each correction function from Simulation 1.

3. **Measure**: The steady-state mismatch ratio |delta_B|/|delta_A| and compare to the predicted (gamma_A/gamma_B)(T_A/T_B)^2.

### Expected Insights

- Under linear correction: the squared relationship should hold exactly (this is a sanity check).

- Under saturating correction: the advantage should be *less* than squared (because A's high tempo saturates B's correction function, so the marginal damage of additional A-tempo is diminishing). The exponent might drop from 2 toward 1 or even sublinear.

- Under structural breakdown: there should be a *threshold* effect — below a critical T_A/T_B ratio, both agents persist; above it, B collapses catastrophically (exits the valid correction region). This would validate Prop A.3's destabilization threshold as a sharp transition.

**Effort**: Medium. Two coupled agents with parameterized dynamics. Extends Simulation 1 straightforwardly.

---

## Simulation 3: Developer-as-TFT-Agent on a Real Codebase

**Purpose**: Validate the TFT→software mapping by simulating a developer (or AI agent) navigating and modifying a real codebase, tracking TFT quantities throughout.

**For both theories**: This would be the "software development worked example" that TFT is missing (alongside Kalman and RL) and the empirical grounding TST has never had.

### Setup

1. **Codebase**: A real open-source project with substantial git history (e.g., a well-known library with 100+ contributors and 1000+ commits).

2. **Agent**: An AI agent (LLM) tasked with implementing a series of features that were actually implemented historically (from the git log). The agent implements each feature from the specification alone, without seeing the actual implementation.

3. **Track TFT quantities at each step**:
   - **Mismatch delta_t**: Compare the agent's predictions about the codebase (before reading) to what it finds (after reading). Measurable via: "predict which files need changing" → "discover which files actually needed changing."
   - **Gain eta***: How much the agent's model updates per observation (qualitatively:
     how much each file read changes the agent's plan).
   - **Tempo T**: Features completed per unit time, weighted by model accuracy.
   - **rho**: Rate at which the codebase changes between the agent's sessions (measurable from git history).

4. **Compare to actual history**: How do the agent's change-sets compare to the actual developer's? Are they larger (agent has higher delta)? More scattered (agent has lower architectural comprehension)? Do they converge as the agent "learns" the codebase within a session?

### Expected Insights

- The agent's initial mismatch should be high and decrease as it reads more code (validating the cold-start → comprehension → effective-action trajectory).

- Change-set sizes should decrease as the agent builds a better model (validating that higher model quality → smaller change-sets, connecting TFT to TST's T-08).

- There should be a measurable persistence condition: for sufficiently complex codebases or sufficiently fast-changing requirements, the agent's model degrades faster than it can be maintained (persistence failure).

- The 100% turnover problem should manifest as: each new session starts with high delta, and the steady-state session performance should depend on the quality of externalized memory (CLAUDE.md, documentation).

**Effort**: High. Requires an LLM agent framework, a curated set of historical features with specifications, and instrumentation to track the TFT quantities. But the payoff is substantial — this would be the first empirical validation of TFT in a non-trivial domain beyond Kalman filters.

---

## Simulation 4: Counterfactual Architecture Evaluation

**Purpose**: Demonstrate the counterfactual evaluation workflow described in causal-extensions.md — literally measure what would have happened under an alternative architecture.

**For TST-via-TFT**: This would be the first rigorous empirical evaluation of an architectural decision, grounding TST's investment calculus (T-06) in measured counterfactual data.

### Setup

1. **Select a real project** with a known architectural decision point in its history (e.g., the decision to split a monolith into services, or the choice of a particular state management pattern, or a major refactoring commit).

2. **Fork from just before the decision point.**

3. **Implement the alternative architecture** (the road not taken).

4. **Re-implement a sample of subsequent features** (10-20, selected to be representative) on top of the alternative architecture.

5. **Measure**:
   - Change-set sizes for each feature under both architectures
   - Number of files touched
   - Change proximity (TST's D-05)
   - Test failures introduced
   - Time to implement (if using an AI agent for both, this is directly measurable)

### Expected Insights

- For some decisions, the counterfactual data will confirm the actual choice was better (validating the developer's judgment).

- For others, the counterfactual will reveal the actual choice was suboptimal — providing concrete, quantitative evidence for the cost of the architectural decision.

- The magnitude of the differences will calibrate TST's T-06 investment formula:
  how much do architectural decisions actually affect future change-set sizes?

- The data will reveal whether TST's proportionality claim (T-08) holds: is implementation time actually proportional to change-set size, or is the relationship nonlinear?

**Effort**: Very high. Requires an AI agent capable of implementing features from specifications, careful selection of decision points and representative features, and substantial computation. But this is potentially the most valuable simulation of the set — it would produce data that no amount of theory can substitute for.

---

## Simulation 5: Multi-Agent Codebase Evolution

**Purpose**: Test Appendix F's multi-agent predictions in the software domain — does cooperative communication increase team persistence? Does adversarial coupling (conflicting objectives) degrade it?

### Setup

1. **Simulated codebase**: A simplified codebase model (not a real language — just a DAG of modules with defined interfaces, where "implementing a feature" means modifying a set of modules determined by the DAG structure).

2. **Multiple agents**: Each with their own M_t, observing different subsets of the codebase, making changes independently.

3. **Cooperative mode**: Agents share their models (communicate which modules they've modified and why). Communication has a cost (coordination overhead from F.3).

4. **Adversarial mode**: Some agents have conflicting objectives (e.g., one optimizes for feature A while another optimizes for feature B, and the optimizations are architecturally incompatible).

5. **Measure**:
   - Team steady-state mismatch under cooperative vs. independent operation
   - Whether cooperative communication enables persistence in environments where solo agents fail (Appendix F's key prediction)
   - How adversarial coupling degrades team persistence
   - Optimal team size (where marginal communication tempo = marginal coordination cost — F.3's prediction)

### Expected Insights

- Cooperative teams should maintain lower mismatch than independent developers working on the same codebase, up to a team-size limit.

- The team-size limit should correspond to the coordination-overhead breakeven from F.3.

- Adversarial coupling should create the effects spiral: once one faction's changes start degrading the other's model, the degradation accelerates.

- The optimal communication structure should depend on the codebase topology: modular codebases should favor independent work with narrow communication; monolithic codebases should favor tight communication.

**Effort**: Medium-high. The codebase model is simplified (no real code), but the multi-agent dynamics require careful implementation.

---

## Simulation 6: Gain Dynamics and the Cold-Start Problem

**Purpose**: Test the specific prediction that AI agents with 100% context turnover should exhibit TFT's gain dynamics — starting with high eta* (absorbing everything) and converging to lower eta* as their model stabilizes within a session.

### Setup

1. **Agent**: An LLM tasked with answering questions about a codebase it hasn't seen.

2. **Protocol**: Feed the agent files one at a time. After each file, ask it to predict properties of files it hasn't seen yet (function signatures, module dependencies, naming patterns).

3. **Measure**:
   - Prediction accuracy over time (should improve as M_t builds)
   - Rate of model change per observation (proxy for eta* — should decrease as the agent becomes more confident)
   - Mismatch between predictions and reality (should decrease toward an irreducible floor set by codebase complexity)
   - Whether there's a point where additional observations yield diminishing returns (the agent's model has "converged" for its current model class)

### Expected Insights

- The gain trajectory should match TFT's predictions: high initially, decaying toward a steady state.

- The steady-state should depend on codebase quality: well-structured codebases (low U_o) should yield lower steady-state mismatch than poorly-structured ones.

- There should be a measurable "model class inadequacy" signal: the agent's predictions stop improving even though its model keeps updating (it's fitting noise rather than learning structure — TF-10's symptom #2).

**Effort**: Medium. Requires an LLM, a codebase, and a prediction evaluation framework. The measurement of "eta*" in a non-parametric model (LLM) is the main challenge — it needs to be operationalized as something like "how much does the agent's prediction distribution shift after each observation."

---

## Priority Ordering

By expected value per effort:

1. **Simulation 1** (Nonlinear mismatch dynamics) — Low effort, directly shores up TFT's weakest formal claim. Do this first.

2. **Simulation 2** (Adversarial coupling) — Medium effort, extends Sim 1 naturally, tests TFT's most striking quantitative prediction.

3. **Simulation 6** (Gain dynamics / cold-start) — Medium effort, directly validates the TFT→software mapping for AI agents, timely given the AI-coding revolution.

4. **Simulation 3** (Developer-as-agent on real codebase) — High effort but highest payoff. This is the "software worked example" both theories need.

5. **Simulation 5** (Multi-agent codebase evolution) — Medium-high effort, tests Appendix F's predictions in a concrete domain.

6. **Simulation 4** (Counterfactual architecture) — Very high effort, but if feasible, the most novel contribution. This could create a new methodology.

---

## Technical Notes

**Language**: Python is the natural choice for Simulations 1-2 (numerical dynamics).
For Simulations 3-4, the AI agent framework matters more than the simulation language. For Simulation 5, an abstract codebase model can be implemented in anything.

**Reproducibility**: All simulations should follow Appendix B's minimal reproducibility checklist (adapted): mismatch definition, estimation methods, parameter specifications, and at least one ablation.

**Open question**: Can Simulations 1-2 (abstract dynamics) and 3-4 (real codebases) be connected? That is, can we measure the correction function g(delta) from real developer behavior (Simulation 3), then use that empirically-measured g in the dynamics simulations (Simulation 1) to validate the ODE predictions? This would close the loop between abstract theory and empirical observation.
