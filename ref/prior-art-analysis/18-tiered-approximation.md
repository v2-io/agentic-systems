# Prior-Art Analysis: Tiered Approximation as Scope Honesty

**Target Claim:**
AAT uses a recurring meta-pattern for handling intractability: rather than offering a single heuristic approximation, it introduces a *tiered hierarchy of approximations*. Each hierarchy must satisfy four formal conditions: an indexing parameter for tractability (AT1), proved monotonicity between tiers (AT2), graceful degradation (AT3), and most importantly, an *explicit ascension diagnostic* (AT4) that tells the agent when the current tier is binding and escalation is required. 

AAT formalizes three major instances of this: the Correlation Hierarchy (L0/L1/L2) for causal structure, the Convention Hierarchy (C1/C2/C3) for continuation policies, and the Contraction Taxonomy (Tier 1/2/3) for composite closure. AAT claims this pattern makes "scope honesty" an operational mechanism rather than just a rhetorical label.

---

## 1. State of the Field & Scientific Precedence

The Undermind search reveals that structured, monotonic hierarchies of approximations with built-in convergence or refinement diagnostics are highly established in formal verification, optimization, and stochastic control.

### Pillar 1: Counterexample-Guided Abstraction Refinement (CEGAR)
In formal verification and model checking, CEGAR is a foundational paradigm that perfectly mirrors AAT's AT1-AT4 pattern.
- **Clarke et al. (2000)** in *Counterexample-Guided Abstraction Refinement* introduced the method of starting with a coarse, highly tractable abstraction of a state space (AT1, AT3). If the model checker finds a counterexample that is *spurious* (caused by the over-approximation rather than a true bug), this serves as an exact, formal *ascension diagnostic* (AT4). The algorithm uses the spurious counterexample to refine the abstraction, strictly ascending the hierarchy (AT2) until the property is proved or a real bug is found.
- **Chadha and Viswanathan (2008)** extended CEGAR to Markov decision processes, demonstrating how probabilistic systems dynamically manage the approximation/tractability tradeoff.

### Pillar 2: Lasserre's Moment-SOS Hierarchy
In polynomial and global optimization, moving through a strict hierarchy of relaxations is the standard method for handling non-convex intractability.
- **Lasserre (2000, 2007)** introduced a sequence of semidefinite relaxations (the Moment-SOS hierarchy) that provide increasingly tight convex lower bounds on polynomial optimization problems. 
- **Nie (2012, 2013)** and others formalized *flat truncation*, a mathematical condition that serves as the explicit diagnostic (AT4) certifying that the current tier of the hierarchy is exact and no further ascension is necessary. 

### Pillar 3: Information Relaxations in Dynamic Programming
For intractable sequential decision making, dual bounding methods provide tiered guarantees.
- **Brown, Smith, and Sun (2010, 2014)** established *Information Relaxations* for stochastic dynamic programs. They relax nonanticipativity constraints to compute tractable bounds, punishing violations with penalties. This creates a spectrum of approximations (AT1) with proved bounding properties (AT2), allowing the system to trade computational effort for tightness.

---

## 2. Key Anchor Papers (Available in `/ref`)

1. **Clarke, E., et al. (2000). Counterexample-Guided Abstraction Refinement.**
   *Significance:* The seminal computer science paper establishing the formal paradigm of starting with a cheap approximation and using explicit failure diagnostics to trigger monotonic refinement.
2. **Lasserre, J. (2000). Global Optimization with Polynomials and the Problem of Moments.**
   *Significance:* Establishes the Moment-SOS hierarchy, the canonical example of converting an intractable problem into a tiered sequence of monotonic approximations.
3. **Brown, D. B., Smith, J. E., & Sun, P. (2010). Information Relaxations and Duality in Stochastic Dynamic Programs.**
   *Significance:* Provides a formal framework for relaxing constraints in intractable MDPs/DPs to achieve bounded, monotonic approximations of the value function.

---

## 3. Conclusion on Novelty & Overlap

The mathematical pattern of using monotonic, tiered approximations with specific diagnostic triggers (like spurious counterexamples in CEGAR or flat truncation in SOS optimization) is a settled and highly successful paradigm in algorithms and applied mathematics. AAT does not claim to have invented the concept of approximation hierarchies.

**AAT's Novel Contribution:**
AAT's contribution is **Architectural and Synthetic**. 

It elevates the algorithmic design pattern of CEGAR/Lasserre into a universal *epistemic requirement for bounded agents*. Instead of treating approximations as static engineering choices made by a human programmer before deployment, AAT forces the agent to dynamically navigate its own intractability at runtime using these explicit hierarchies. 

By making the *ascension diagnostic*—such as detecting sibling-edge covariance for the Correlation hierarchy, or a persistent satisfaction gap for the Convention hierarchy—an explicit, on-policy part of the agent's internal tracking loop, AAT translates formal verification principles into the real-time cognitive architecture of an autonomous agent. AAT makes "scope honesty" (knowing exactly when your current heuristic is invalid and having a formal path to escalate) an operational, measurable behavior of the cybernetic loop.

**AAT-native methodological inventions on this row:**
- The **four-condition formal schema** (AT1 indexing parameter / AT2 monotonicity between tiers / AT3 graceful degradation / AT4 explicit ascension diagnostic) characterizing what counts as a "tiered approximation" in AAT.
- The **three landed instances** of the schema:
  - **Correlation Hierarchy** (L0 / L1 / L1' / L2) for causal structure in strategy DAGs (cross-row 06; Instance 1 + Instance 2 of `#disc-identifiability-floor`).
  - **Convention Hierarchy** (C1 one-step improvement / C2 receding-horizon / C3 Bellman) for continuation policies in value evaluation, with the **proved monotonicity result** $\delta_{\text{sat}}^B \le \delta_{\text{sat}}^{RH} \le \delta_{\text{sat}}^{(1)}$ from `#def-value-object`'s static corollary (`status: exact`). This is the convention-monotonicity Lemma 1 used in the self-actuation grounding no-go (row 13).
  - **Contraction Taxonomy** (Tier 1 exact contraction on class / Tier 2 local with bounded degradation / Tier 3 per-domain verification) for composition closure.
- The **explicit ascension diagnostic as on-policy cybernetic-loop primitive** — the agent itself navigates its own intractability at runtime, not a designer choice baked in pre-deployment.
- The **cost-accounting condition** (the prompt's AT4) embedded in the diagnostic — escalation has a structurally accountable cost in each hierarchy.

**Connection to `#disc-identifiability-floor`.** The Correlation Hierarchy's L0→L1' transition is constructively forced by Instance 2 (Fisher rank-1 mixture-identifiability refutation; row 11). The Convention Hierarchy's C1→C3 cost-accounting is the core machinery of the self-actuation grounding no-go (row 13). The tiered-approximation pattern and the constructive-impossibility pattern are *complementary* — the tiered hierarchy supplies the positive escalation path; the identifiability floor names the precise condition under which escalation becomes necessary.

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **Some.** The Convention-Hierarchy monotonicity result is *exact* (per `#def-value-object`'s static corollary). The Correlation-Hierarchy L1' identifiability bound is *exact* (Fisher rank-1, cross-row 11). The four-condition formal schema has analytical content (it bounds what counts as a valid tiered approximation). These are Nash-style applications of established techniques (Bellman convention analysis, Fisher information, contraction analysis) in AAT-internal hierarchical-approximation settings.
- *Arch Novelty:* **High.** Four-condition formal schema + three landed instances + ascension-diagnostic-as-on-policy-cybernetic-primitive. Multiple AAT-native methodological inventions.
- *Synth Novelty:* **Medium.** Bridges CEGAR (counterexample-guided abstraction refinement), Lasserre SOS hierarchies, and approximate planning hierarchies under one bounded-agent epistemic-requirement framing.
- *Appl Novelty:* **None at this row's lead.**
- *Impact:* **Medium.** The tiered-approximation pattern is one of AAT's distinctive constructive moves. The connection to the identifiability-floor pattern via the Cramér-Rao L1' refutation and the convention-monotonicity convention-hierarchy gives this row a load-bearing role in framing AAT's scope-honesty discipline as operational.