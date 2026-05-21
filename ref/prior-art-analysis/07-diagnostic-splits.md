# Prior-Art Analysis: Failure Diagnosis and Persistence (Diagnostic Splits)

**Target Claim:**
AAT actively splits agent failure diagnosis orthogonally into the "Satisfaction Gap" (is the goal achievable at all?) and "Control Regret" (is the current policy optimal?). This 2x2 matrix separates "the goal is too hard" from "the strategy is weak." To resolve this, AAT enforces the **Orient Cascade**, a strict, information-dependency-forced sequence of cognitive updates: Update Model $\to$ Check Satisfaction $\to$ Check Regret $\to$ Revise Strategy $\to$ Revise Objective (last resort). 
Furthermore, tracking drifting environments to support these diagnostics explicitly requires "exponential forgetting" (bounding effective sample size); without it, confidence calcifies and the agent loses the ability to diagnose failure.

---

## 1. State of the Field & Scientific Precedence

The Undermind search yields strong prior art divided into two distinct domains: Stochastic Shortest Path (SSP) planning (which addresses goal-feasibility vs policy optimality) and Adaptive Signal Processing / Non-stationary Bandits (which addresses the mathematical necessity of forgetting).

### Pillar 1: Feasibility vs. Optimality (SSPs with Dead Ends)
In standard reinforcement learning, a single reward/value function conflates goal achievability with policy efficiency. However, the Automated Planning community has explicitly encountered the need to separate these concepts when dealing with "dead ends" (states from which the goal is unreachable).
- **Kolobov, Mausam, and Weld (2012)** in *A Theory of Goal-Oriented MDPs with Dead Ends* explicitly extend SSPs to model domains where goals might be physically unachievable. 
- **Teichteil-Königsbuch (2012)** and **Trevizan et al. (2017)** developed "Stochastic Safest and Shortest Path Problems" and the "Min-Cost given Max-Prob" (MCMP) criterion. This dual-optimization framework exactly mirrors AAT's Satisfaction/Regret split: it explicitly separates the diagnosis of *maximizing the probability of reaching the goal* (satisfaction) from *minimizing the expected cost of the policy* (regret).

### Pillar 2: The Orient Cascade and Cognitive Ordering
While OODA (Observe-Orient-Decide-Act) is a common heuristic, formal mathematical orderings of internal diagnostic updates are rarer but present in Active Inference.
- **Friston et al. (2015, 2017)** model policy selection using Expected Free Energy (EFE), which decomposes into *pragmatic value* (goal satisfaction) and *epistemic value* (information gain). However, as AAT explicitly notes in its derivations, AI's EFE aggregates these into a single scalar metric. It supports policy ranking but does not generate the strict 2x2 categorical separation of causes that AAT's Cascade requires.

### Pillar 3: Non-Stationary Tracking and Exponential Forgetting
The requirement that agents must "forget" old data to track drifting environments is a settled law of adaptive control.
- **Garivier and Moulines (2008)** proved that in non-stationary bandit problems, algorithms *must* use discounted/sliding-window mechanisms (exponential forgetting) to match lower-bound regret rates. 
- **Guo, Ljung, and Priouret (1993)** and **Kozdoba et al. (2018)** formalized the performance of Recursive Least Squares (RLS) and Kalman filters, proving that an explicit forgetting factor (bounding the effective memory) is required to maintain bounded tracking error matrices when parameters drift.

---

## 2. Key Anchor Papers (Available in `/ref`)

1. **Kolobov, A., Mausam, & Weld, D. S. (2012). A Theory of Goal-Oriented MDPs with Dead Ends.** (`ref/kolobov_ssp_dead_ends_2012.pdf`)
   *Significance:* Provides the formal AI planning framework for environments where goals can become impossible, separating the existence of a path from the cost of the path.
2. **Teichteil-Königsbuch, F. (2012). Stochastic Safest and Shortest Path Problems.**
   *Significance:* Introduces the dual-criterion optimization (MaxProb vs MinCost) that serves as the closest formal precursor to AAT's Satisfaction Gap / Control Regret orthogonal split.
3. **Garivier, A., & Moulines, É. (2008). On Upper-Confidence Bound Policies for Non-Stationary Bandit Problems.** (`ref/garivier_ucb_nonstationary_2008.pdf`)
   *Significance:* Provides the definitive proof that optimal tracking in non-stationary environments strictly requires discounted/sliding-window upper confidence bounds (forgetting).
4. **Guo, L., Ljung, L., & Priouret, P. (1993). Performance analysis of the forgetting factor RLS algorithm.**
   *Significance:* The classic control-theoretic proof that tracking time-varying parameters requires a bounded effective sample size.

---

## 3. Conclusion on Novelty & Overlap

The core components—dual criteria for goal reachability vs path cost, and the necessity of exponential forgetting in non-stationary tracking—are well established in AI planning and adaptive control, respectively. AAT does not claim to have invented forgetting factors or the concept of dead-ends.

**AAT's Novel Contribution:**
AAT's primary contribution here is **Architectural Synthesis and Dependency-Forcing**.

1. **The Orient Cascade as a Dependency Proof:** In standard AI, diagnostic steps (like evaluating goal feasibility or updating a model) are usually scheduled by human-designed loops. AAT provides a formal *information-dependency proof* (the Orient Cascade) that dictates exactly why the update order MUST be: Epistemic $\to$ Satisfaction $\to$ Regret $\to$ Strategy $\to$ Objective. AAT proves that because the evaluation of the Satisfaction Gap requires the updated model ($M_t$), and the evaluation of Control Regret requires the output of the Satisfaction Gap to disambiguate the cause of failure, the cognitive sequence is logically forced, not heuristically chosen.
2. **Avoiding the EFE "Dark Room" Collapse:** AAT explicitly contrasts its 2x2 diagnostic split with Active Inference. AAT points out that by treating preferences as log-priors ($C(o) = \log P_{\text{pref}}(o)$), Active Inference collapses the diagnostic distinction between "wanting" and "expecting", turning both "goal is too hard" and "strategy is too weak" into the exact same scalar EFE penalty. AAT's novel architectural move is to strictly partition value functional evaluation from epistemic prediction, preserving the orthogonal diagnostic power required to trigger the correct structural adaptation.