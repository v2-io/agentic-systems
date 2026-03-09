# ACT Development Roadmap

## Current State (March 2026)

**Part I (Adaptive Systems / TFT)**: Well-developed. TF-00 through TF-11 plus
appendices A-G. The foundation is solid, with one important empirical caveat
from simulations (Cor. 11.2 regime validity).

**Part II (Purposeful Agency)**: Exploratory sketch phase. Three convergence-
tested intent DAG formalism variants. Core structure identified (AND/OR nodes,
single-parameter edges, Orient cascade). Not yet consolidated into formal
documents.

**Domain Instantiations**: TST-via-TFT mapping exists (priors/tst/via-tft/).
Needs updating once ACT Part II is consolidated.

---

## Phase 1: Consolidation (immediate)

### 1.1 Consolidate Intent DAG Formalism
Merge the three variants (00-intent-dag-formalism, 02-alt-clean-slate,
03-alt-and-or-dag) into a single canonical treatment:
- AND/OR nodes with single-parameter edges (converged)
- Bayesian edge update mirroring TF-06 (converged)
- Orient cascade (converged)
- Node taxonomy: resolve categorical vs continuous (open — pick one and
  note the alternative)
- Strategic tempo T_G from the clean-slate variant
- Health metrics (keep the principled ones, flag scaffold ones)

### 1.2 Feed Simulation Results Back to TFT
The squared tempo advantage (Cor. 11.2) needs a regime-validity caveat.
Options:
- Add a note to TF-11 specifying the coupling-dominant, continuous-time regime
- Add a note to Appendix A referencing the simulation findings
- Consider whether the discrete-time AR(1) formula should be the primary
  result, with the continuous ODE as the approximation (inverting the current
  presentation)

### 1.3 Write the Goal-Formalism Formally
Promote scratch/03-goal-formalism-sketch.md into a formal treatment:
- G_t definition, goal uncertainty U_G, goal update gain
- Three mismatch signals (epistemic, goal-reality, feasibility)
- Extended policy objective
- Cold-start sequence
- Separation principle

---

## Phase 2: Multi-Agent Intent (highest-value next work)

### 2.1 Intent Decomposition
How does a high-level intent DAG decompose across agents? Formalize:
- Graph partitioning by inter-agent edge uncertainty
- Optimal cut minimizes uncertainty on spanning edges
- Connection to organizational design (who owns which sub-DAG?)

### 2.2 Directed Opportunism
Local grafting at OR-nodes within IB-compressed shared intent:
- How much can a subordinate's local G_t diverge?
- The Auftragstaktik IB: compress to constraints that keep inter-agent
  edges viable while freeing intra-agent edges
- When is local divergence beneficial vs. destructive?

### 2.3 Adversarial Dynamics on DAGs
Targeting edges in the opponent's intent DAG:
- High-centrality edges as priority targets
- Inter-agent coordination edges as fragmentation points
- Effects spiral as DAG pruning faster than grafting
- Structural interpretation of tempo advantage

### 2.4 Team Persistence via DAG Redundancy
Why teams persist where individuals can't:
- Aggregate DAG has more paths (higher R_w)
- More observation channels (higher observability coverage)
- Re-routing around failed edges via sub-DAG reassignment
- Collective grafting capacity

---

## Phase 3: Formal Document Sequence

### 3.1 Draft ACT Document Sequence
Modeled on TFT's structure (ACT-00 through ACT-NN):
- ACT-00: Notation, conventions, dependency structure
- ACT-01: Scope — Adaptive, Purposeful Agents Under Uncertainty
- ACT-02: Causal Structure (inheriting TF-02, extending to intent DAGs)
- ACT-03: The Dual Model (M_t and G_t)
- ACT-04: The Three Mismatch Signals
- ACT-05: The Orient Cascade
- ACT-06: Intent DAG Structure and Operations
- ACT-07: Goal Tempo and Goal Persistence
- ACT-08: Multi-Agent Intent (decomposition, shared intent, adversarial)
- Appendix: Simulation results (nonlinear dynamics, regime validity)

### 3.2 Revise TST-via-TFT as TST-via-ACT
Update the software domain instantiation to use ACT's full machinery:
- Developer's intent DAG (spec -> features -> tasks -> actions)
- Goal-reality mismatch in software
- Directed opportunism in software (recognizing better approaches)
- Team dynamics for software teams

---

## Phase 4: Validation

### 4.1 Additional Simulations
- Sim 3: Developer-as-ACT-agent on real codebase (from TST-via-TFT proposals)
- Sim 4: Multi-agent intent propagation simulation
- Sim 5: Counterfactual architecture evaluation (git fork + replay)

### 4.2 Empirical Testing of DAG Health Metrics
- Collect OKR/project data from real organizations
- Compute DAG health metrics (groundedness, redundancy, observability,
  depth fragility)
- Test prediction: DAG health predicts project outcomes better than
  simpler metrics

### 4.3 Regime Validity for Adversarial Dynamics
- Extend simulations to find the parameter regime where exponent -> 2
- Characterize the transition from linear to squared advantage
- Determine whether the continuous-time squared law is ever practically
  relevant or is purely a mathematical limit

---

## Open Questions (not yet assigned to phases)

1. Does the information bottleneck principle for shared intent produce
   non-obvious predictions about organizational communication structure?

2. Can the intent DAG formalism be extended to handle temporal dependencies
   (action ordering) as well as causal dependencies?

3. How does the 100% context turnover problem interact with the intent DAG?
   G_t may survive context death (via CLAUDE.md) even when M_t doesn't.
   What does this mean for the cold-start protocol?

4. Is there a "goal-reality-model triangle" analog of the bias-variance
   tradeoff? Too much focus on M_t accuracy delays goal-pursuit; too much
   focus on goal-pursuit with a bad M_t wastes action on wrong paths.

5. Can Hafez's bi-predictability P be derived from or mapped to ACT
   quantities? If P = f(T, eta*, ...), that would be a strong connection.

6. What is the relationship between ACT and active inference's prior
   preferences? Is there a formal equivalence or are they genuinely different?
