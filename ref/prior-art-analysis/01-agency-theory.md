# Prior-Art Analysis: Agency Theory, Foundations, and Partial Observability

**Target Claim:**
An agent's internal model of reality is a many-to-one compression of a strictly irreversible, non-forkable sequence of events (the "chronica"). Under strict partial observability (where the agent never accesses true environment states) and computational constraints, state updates must be recursive (Markovian). Furthermore, the optimal compression of this history is defined by the Information Bottleneck principle: maximizing predictive information about future observations while minimizing retained historical data.

---

## 1. State of the Field & Scientific Precedence

The Undermind search yields a highly cohesive and robust chain of scientific precedence for this framework. The core components of the AAT foundation—treating history as the primitive, forcing recursive updates due to partial observability, and compressing that history via Information Bottleneck (IB)—are well-established in the literature, often intersecting across physics, theoretical computer science, and reinforcement learning.

AAT's claim does not invent these components but appears to formally synthesize them into a unified theory of agency. We can trace the scientific precedence through four distinct pillars of prior art:

### Pillar 1: History as the Primitive (Computational Mechanics)
The claim that an agent's internal model must be a compression of an irreversible event sequence is the foundational premise of **Computational Mechanics**, pioneered by Crutchfield and Shalizi (1999, 2001). They formalized the concept of "causal states" (the $\epsilon$-machine), which are defined exactly as the minimal sufficient statistics of the past needed to optimally predict the future. Their work proved mathematically that any optimal predictor must partition the continuous/infinite history of events into discrete, forward-predictive states.

### Pillar 2: Eliminating Latent Environment States (Predictive State Representations)
The claim that agents never access true environment states and must therefore construct state entirely from observation-action histories is formalized by **Predictive State Representations (PSRs)** (Littman, Sutton, and Singh, 2001). Standard POMDPs attempt to maintain a belief distribution over *hidden* environment states. PSRs argue this is fundamentally flawed and instead define "state" purely as a vector of predictions about future observable events (tests) conditioned on past observable histories. This establishes firm precedence for AAT’s rejection of latent environment-state access.

### Pillar 3: The Information Bottleneck (IB) & Predictive Rate-Distortion
AAT’s assertion that the optimal compression maximizes predictive information while minimizing retained history is a direct application of Tishby's **Information Bottleneck method** (2000), specifically as extended to dynamical systems and time-series via **Predictive Rate-Distortion Theory** (Marzen & Crutchfield, 2014, 2016). Bialek, Nemenman, and Tishby (2000) explicitly defined "predictive information" as the mutual information between the past and the future. Marzen and Crutchfield proved that applying the IB to infinite-order Markov processes effectively yields the causal states of computational mechanics, fully uniting Pillar 1 and Pillar 3. 

### Pillar 4: Recursive Updates in Control (Approximate Information States)
The constraint that these compressions must be recursively updateable (Markovian) to be computationally tractable is deeply rooted in modern stochastic control. Subramanian and Mahajan (2019, 2020) formalized the **Approximate Information State (AIS)**. They proved that for an agent to perform dynamic programming in a partially observed system without knowing the true model, it must construct a history-compression that is both sufficient for prediction and recursively updateable. This provides the exact mathematical bounds for AAT's "computational constraints force recursive updates" claim.

---

## 2. Key Anchor Papers (Deposited in `/ref`)

To verify the state of the field, the following highly relevant anchor papers have been identified (and explicitly fetched into the `ref/` directory for validation):

1. **Tishby, N., Pereira, F. C., & Bialek, W. (2000). The information bottleneck method.** (`ref/tishby_ib_2000.pdf`)
   *Significance:* The seminal paper defining the constrained optimization problem of finding a short code for variable $X$ (the past) that preserves maximum information about $Y$ (the future). This is the direct mathematical origin of AAT's optimal compression claim.
2. **Shalizi, C. R., & Crutchfield, J. P. (1999). Computational mechanics: Pattern and prediction, structure and simplicity.**
   *Significance:* Proves that the $\epsilon$-machine (causal states) is the minimal representation consistent with accurate prediction of a time series, establishing the "chronica-to-state" mapping.
3. **Marzen, S. E., & Crutchfield, J. P. (2016). Predictive Rate-Distortion for Infinite-Order Markov Processes.** (`ref/marzen_prd_2016.pdf`)
   *Significance:* Directly bridges IB and computational mechanics. Shows that attempting to compress arbitrarily long pasts requires routing the predictive rate-distortion objective through causal states to circumvent the curse of dimensionality.
4. **Littman, M. L., Sutton, R. S., & Singh, S. (2001). Predictive representations of state.**
   *Significance:* Introduces PSRs, providing the RL-theoretic grounding for why agents should build states from observable action-observation histories rather than tracking hidden environmental parameters.
5. **Subramanian, J., et al. (2020). Approximate information state for approximate planning and reinforcement learning in partially observed systems.** (`ref/subramanian_ais_2020.pdf`)
   *Significance:* Provides the rigorous control-theory proofs that an "information state" must be a recursively updateable function of history, and bounds the optimality loss when using approximate compressions.

---

## 3. Conclusion on Novelty & Overlap

The foundational premises of AAT are not novel in isolation; they are deeply grounded in established, rigorous literature. The specific phrasing of the "chronica" aligns perfectly with the "irreversible observation history" in computational mechanics. The "Information Bottleneck compression of history" is mathematically identical to Predictive Rate-Distortion theory. The necessity of "recursive Markovian updates" is the definition of an Information State in stochastic control.

**AAT's contribution at this layer is synthetic.** It takes the epistemological purity of PSRs, the structural optimality of computational mechanics, the objective function of the Information Bottleneck, and the recursive necessity of control theory, and weaves them into a single, cohesive axiom set for agency. 
