---
slug: worked-example-strategy
type: worked-example
status: conditional
depends:
  - scope-condition
  - causal-structure
  - agent-model
  - mismatch-signal
  - update-gain
  - adaptive-tempo
  - persistence-condition
  - objective-functional
  - value-object
  - strategy-dag
  - satisfaction-gap
  - control-regret
  - orient-cascade
  - chain-confidence-decay
  - observability-dominance
  - edge-update-via-gain
  - and-or-scope
  - directed-separation
  - strategic-calibration
stage: draft
---

# Worked Example: Nonstationary Bandit with Explicit Strategy (Section II Validation)

ACT's Section II machinery — objectives, strategy DAGs, the orient cascade, satisfaction gap, control regret, chain confidence decay, observability dominance, and edge update via gain — is exercised on a concrete system simple enough for closed-form analysis. The key payoff: Section II diagnostics tell the agent things that Section I quantities alone cannot.

## System

A 3-armed Bernoulli bandit with drifting success probabilities and an agent that maintains an explicit strategy DAG for arm selection.

*[Formulation]*

**Environment.** Three arms with time-varying success probabilities:

$$\theta_k(t) \in [0, 1], \quad k \in \{1, 2, 3\}$$

At each step, pulling arm $k$ yields reward $r_t \in \{0, 1\}$ with $P(r_t = 1 \mid a_t = k) = \theta_k(t)$. The best arm changes slowly: at rate $\rho_\theta$, a random arm's success probability shifts by a random perturbation clipped to $[0.1, 0.9]$.

**Concrete parameterization.** At $t = 0$: $\theta_1(0) = 0.7$, $\theta_2(0) = 0.5$, $\theta_3(0) = 0.3$. Drift rate: $\rho_\theta = 0.05$ per step (one arm shifts by $\pm 0.05$ every 20 steps on average). Horizon: $N_h = 100$ steps.

**Agent.** Maintains Beta-Bernoulli beliefs per arm and an explicit strategy DAG encoding its plan for achieving a target reward rate.

## Section I Chain Instantiation (Summary)

Section I quantities map as in #worked-example-bandit. The brief summary here establishes the epistemic baseline; the novel content is Section II.

**Scope** ( #scope-condition). $\Omega_t = (\theta_1(t), \theta_2(t), \theta_3(t))$; $\mathcal{A} = \{1, 2, 3\}$; residual uncertainty persists. *Exact.*

**Model** ( #agent-model). $M_t = (\alpha_k, \beta_k)_{k=1}^{3}$ — Beta posteriors per arm, with exponential discounting (effective window $W = 20$):

$$\hat\theta_k = \frac{\alpha_k}{\alpha_k + \beta_k}$$

*Exact structural mapping.*

**Mismatch** ( #mismatch-signal). $\delta_t = r_t - \hat\theta_{a_t}$. *Exact.*

**Update gain** ( #update-gain). The Beta-Bernoulli conjugate update with discounted pseudo-counts gives:

$$\eta_k^\ast = \frac{1}{\alpha_k + \beta_k + 1}$$

For a well-observed arm with $\alpha_k + \beta_k \approx W = 20$: $\eta_k^\ast \approx 0.048$. *Exact for the pulled arm; zero for unpulled arms.*

**Tempo** ( #adaptive-tempo). Per-arm tempo: $\mathcal T_k = \nu_k \cdot \eta_k^\ast$ where $\nu_k$ is the pull rate for arm $k$. Under uniform exploration: $\nu_k = 1/3$, so $\mathcal T_k \approx 0.016$ per step. *Approximate.*

## Section II Chain Instantiation

### Objective ( #objective-functional)

*Mapping: exact.*

The agent's objective: achieve a target average reward rate over the horizon.

*[Definition (bandit-objective)]*

$$V_{O_t}(\tau_{0:N_h}) = \frac{1}{N_h}\sum_{t=0}^{N_h - 1} r_t$$

$$V_{O_t}^{\min} = 0.6$$

This is a utility-type objective with a satisfaction threshold: the agent counts the mission as successful if its average reward rate meets or exceeds $0.6$. The value functional evaluates trajectories on $[0, 1]$ (average reward).

### Value Object ( #value-object)

*Mapping: exact.*

Under the one-step improvement convention ($\pi_\text{cont} = \pi_\text{current}$):

$$V_O(M_t, \pi; N_h) = \mathbb{E}\!\left[\frac{1}{N_h}\sum_{s=t}^{t + N_h - 1} r_s \;\middle\vert\; M_t, \pi\right]$$

For a greedy policy that always pulls the estimated-best arm $k^\ast = \arg\max_k \hat\theta_k$:

$$V_O(M_t, \pi_\text{greedy}; N_h) = \hat\theta_{k^\ast}$$

This is tractable: the agent's expected average reward under greedy play equals its belief about the best arm's success probability. With $M_0$: $V_O = \hat\theta_1 = 0.7$.

**Action-value form:**

$$Q_O(M_t, k; \pi_\text{greedy}, N_h) \approx \frac{1}{N_h}\hat\theta_k + \frac{N_h - 1}{N_h}\hat\theta_{k^\ast}$$

The first pull contributes $1/N_h$ of the horizon; the rest follows the greedy policy.

### Objective Attainability ( #satisfaction-gap)

*Mapping: exact.*

$$A_O(M_t; \Pi, N_h) = \sup_{\pi \in \Pi} V_O(M_t, \pi; N_h)$$

For a bandit with Beta-Bernoulli beliefs, the optimal policy (Gittins index or Bayes-adaptive) achieves an attainability that is bounded:

$$\max_k \hat\theta_k \leq A_O \leq \max_k \hat\theta_k + \epsilon_\text{info}$$

where $\epsilon_\text{info}$ accounts for the information value of exploration (pulling a suboptimal arm now to identify the true best arm later). The upper bound is tight when exploration can reveal a better arm. For our initial beliefs: $A_O \approx 0.70 + \epsilon_\text{info}$.

**Satisfaction gap:**

$$\delta_\text{sat} = V_{O_t}^{\min} - A_O = 0.6 - 0.70 \approx -0.10$$

$\delta_\text{sat} \lt 0$: the objective is **attainable**. The agent believes it can achieve a $0.6$ average reward rate. The negative gap is margin — the agent has room to spare.

### Control Regret ( #control-regret)

*Mapping: exact.*

Under an explore-then-exploit policy that spends 30 steps exploring uniformly, then exploits the estimated-best arm:

$$V_O(M_t, \pi_\text{explore-exploit}; 100) = \frac{30}{100}\cdot\bar\theta + \frac{70}{100}\cdot\hat\theta_{k^\ast\!(30)}$$

where $\bar\theta = (\hat\theta_1 + \hat\theta_2 + \hat\theta_3)/3$ is the average expected reward during exploration and $\hat\theta_{k^\ast\!(30)}$ is the estimated-best arm after 30 observations. With initial beliefs: $V_O \approx 0.3 \cdot 0.5 + 0.7 \cdot 0.7 = 0.64$.

$$\delta_\text{regret} = A_O - V_O(\pi_\text{explore-exploit}) \approx 0.70 - 0.64 = 0.06$$

The agent is leaving $0.06$ reward-rate points on the table with its current explore-then-exploit strategy — it explores too much. This is the signal for strategy revision ( #orient-cascade step 3).

**The 2x2 diagnostic** ( #control-regret Discussion):

| | $\delta_\text{sat} \leq 0$ | $\delta_\text{sat} \gt 0$ |
|---|---|---|
| $\delta_\text{regret} \approx 0$ | Success | Capability limit |
| $\delta_\text{regret} \gg 0$ | **Strategy problem** | Both |

Our agent is in the **Strategy problem** cell: the goal is achievable, but the current policy is suboptimal. Section I alone (which reports $\hat\theta_k$, $\eta^\ast_k$, and $\mathcal T_k$) cannot distinguish "good strategy, hard goal" from "bad strategy, easy goal." The 2x2 diagnostic is Section II's value-add.

### Strategy DAG ( #strategy-dag, #and-or-scope)

*Mapping: exact for structure and propagation; the DAG is simple enough for closed-form status.*

The agent's strategy for achieving $V_{O_t}^{\min} = 0.6$:

```
                   [root: "achieve ≥0.6 avg reward"] (AND)
                          /                    \
    [Phase 1: "identify best arm"] (OR)    [Phase 2: "exploit best arm"]
         /         |         \                      |
   [arm 1       [arm 2       [arm 3         [pull identified
    is best]     is best]     is best]        arm reliably]
```

**Nodes:**
- $v_\text{root}$: AND-node. Both phases must succeed: identify the best arm AND exploit it. Terminal satisfaction condition: average reward $\geq 0.6$.
- $v_\text{id}$: OR-node (Phase 1). Identifying the best arm succeeds if ANY one arm is correctly identified as best.
- $v_1, v_2, v_3$: leaf condition nodes. "Arm $k$ is the best arm." Base credence: $p_k(M_t) = P(\theta_k \gt \theta_j \;\forall j \neq k \mid M_t)$.
- $v_\text{exploit}$: leaf action node (Phase 2). "Pulling the identified arm yields reward $\geq 0.6$." Base credence: $p_\text{exploit}(M_t) = P(\theta_{k^\ast} \geq 0.6 \mid M_t)$.

**Edge credences.** The edges from leaf nodes to their parents carry causal credences:
- $p_{v_k, v_\text{id}}$: "correctly identifying arm $k$ as best enables Phase 1 success." These are structural (close to $1.0$) — if the agent correctly knows which arm is best, Phase 1 succeeds by definition. Set $p_{v_k, v_\text{id}} = 1.0$ for all $k$.
- $p_{v_\text{id}, v_\text{root}}$: "having identified the best arm advances the root goal." Set to $0.95$ (slight uncertainty about whether identification translates to exploitation success).
- $p_{v_\text{exploit}, v_\text{root}}$: "successful exploitation advances the root goal." Set to $0.90$ (the identified arm might drift below threshold during exploitation).

**Leaf base credences from $M_t$.** At $t = 0$ with $(\hat\theta_1, \hat\theta_2, \hat\theta_3) = (0.7, 0.5, 0.3)$ and moderate pseudo-counts $(\alpha_k + \beta_k \approx 5)$ from prior experience:

$$p_1(M_0) = P(\theta_1 \gt \theta_2, \theta_1 \gt \theta_3 \mid M_0) \approx 0.75$$

$$p_2(M_0) \approx 0.20, \quad p_3(M_0) \approx 0.05$$

$$p_\text{exploit}(M_0) = P(\theta_{k^\ast} \geq 0.6 \mid M_0) \approx 0.70$$

**Status propagation** ( #strategy-dag, #and-or-scope):

Phase 1 (OR-node):

$$s_{v_\text{id}} = 1 - \prod_{k=1}^{3}(1 - p_{v_k, v_\text{id}} \cdot p_k) = 1 - (1 - 0.75)(1 - 0.20)(1 - 0.05)$$

$$= 1 - (0.25)(0.80)(0.95) = 1 - 0.19 = 0.81$$

Phase 2 (leaf): $s_{v_\text{exploit}} = 0.70$.

Root (AND-node):

$$s_{v_\text{root}} = (p_{v_\text{id}, v_\text{root}} \cdot s_{v_\text{id}}) \cdot (p_{v_\text{exploit}, v_\text{root}} \cdot s_{v_\text{exploit}})$$

$$= (0.95 \times 0.81) \times (0.90 \times 0.70) = 0.770 \times 0.630 = 0.485$$

**Plan-confidence score:** $\hat P_\Sigma(M_0) = 0.485$. The strategy assigns about 49% confidence to achieving the objective. This is distinct from $A_O$ (which optimizes over all policies) — $\hat P_\Sigma$ is the DAG's self-assessment of *this specific plan*.

### Chain Confidence Decay ( #chain-confidence-decay)

*Mapping: exact (mathematical identity).*

The root node's confidence illustrates chain decay through an AND structure. The root requires two children to succeed, each with their own sub-chains:

$$\log \hat P_\Sigma = \log(p_{v_\text{id}, v_\text{root}} \cdot s_{v_\text{id}}) + \log(p_{v_\text{exploit}, v_\text{root}} \cdot s_{v_\text{exploit}})$$

$$= \log(0.770) + \log(0.630) = -0.261 + (-0.462) = -0.724$$

Each term is negative; the AND combination accumulates them additively in log-space. If the agent added a third AND-child (e.g., "maintain budget"), even with $s_\text{budget} = 0.95$, the plan confidence would drop to $0.485 \times 0.95 = 0.461$. The pressure toward shallow, narrow DAGs is structural.

**Contrast with the OR-node.** Phase 1 (OR-node) benefits from redundancy: three alternative arms provide resilience. The OR combination yields $s_{v_\text{id}} = 0.81$ even though no single arm has credence above $0.75$. The asymmetry between AND (multiplicative decay) and OR (complementary resilience) is the core structural result of #chain-confidence-decay combined with #and-or-scope.

### Orient Cascade ( #orient-cascade)

*Mapping: exact for ordering; the content of each step is tractable in this domain.*

Suppose at $t = 40$, the agent has been pulling arm 1 (the initially-best arm) and observes a run of failures: the last 8 of 10 pulls yielded $r_t = 0$. Meanwhile, arm 2's true probability has drifted to $\theta_2(40) = 0.8$ (unbeknownst to the agent) and arm 1 has drifted to $\theta_1(40) = 0.3$.

The orient cascade proceeds:

**Step 1: Reduce $\delta_\text{epistemic}$.** Update $M_t$ from the recent observations. The Beta posterior for arm 1 shifts:

$$\hat\theta_1: 0.70 \to 0.38 \quad (\text{after 8 failures in 10 trials with discounted prior})$$

Arms 2 and 3 are unobserved since the exploration phase ended. Their posteriors remain at approximately $\hat\theta_2 = 0.52$, $\hat\theta_3 = 0.28$ (slightly regressed toward the prior due to discounting). *The epistemic update proceeds without reference to $O_t$ or $\Sigma_t$* — directed separation ( #directed-separation) holds because the Beta update depends only on the observation and the prior, not on the agent's goals.

**Step 2: Evaluate $\delta_\text{sat}$.** With the updated $M_t$:

$$A_O(M_{40}) \approx \max_k \hat\theta_k + \epsilon_\text{info} = 0.52 + \epsilon_\text{info}$$

$$\delta_\text{sat} = 0.6 - (0.52 + \epsilon_\text{info})$$

If $\epsilon_\text{info} \approx 0.05$ (exploration can reveal a better arm): $\delta_\text{sat} \approx 0.6 - 0.57 = 0.03 \gt 0$. The objective is now **marginally unmet** — the agent believes it may not be able to achieve $0.6$ average reward. This triggers the disambiguation procedure ( #satisfaction-gap): is the goal truly infeasible, or is $M_t$ wrong about what's achievable?

**Step 3: Evaluate $\delta_\text{regret}$.** Under the current greedy policy (still pulling arm 1 despite updated beliefs):

$$V_O(M_{40}, \pi_\text{current}) = \hat\theta_1 = 0.38$$

$$\delta_\text{regret} = 0.57 - 0.38 = 0.19$$

Control regret is high. The agent is pulling arm 1 out of inertia, but $M_t$ now says arm 2 is better. *This is the Section II payoff*: Section I would report the mismatch $\delta_t$ on each pull and the updated $\hat\theta_1$, but it cannot diagnose that the *strategy* is the problem. The high $\delta_\text{regret}$ identifies the corrective action: revise $\Sigma_t$, not $O_t$.

**Step 4: Evaluate $\delta_\text{strategic}$.** The edge residual for the root AND-node's exploitation branch:

$$r_\text{exploit} = \mathbb{E}[\Delta V_O \mid \text{exploit arm 1}] - \Delta V_O^\text{observed}$$

The agent predicted reward $\approx 0.70$ per pull from arm 1; it observed $\approx 0.20$. The residual is large and positive, localizing the problem to the exploitation edge: the agent's causal belief that "pulling arm 1 yields high reward" is wrong.

Simultaneously, the leaf credences update: $p_1(M_{40}) \approx 0.15$ (arm 1 is probably not the best), $p_2(M_{40}) \approx 0.60$ (arm 2 is probably best, by default from the prior). The Phase 1 OR-node status shifts: the identification sub-goal may need to be revisited.

**Step 5: Revise $\Sigma_t$.** The agent restructures its strategy: switch exploitation target to arm 2 (the currently estimated-best arm). In DAG terms: $p_1(M_{40})$ has dropped to $0.15$ while $p_2(M_{40})$ has risen to $0.60$. The OR-node now routes through arm 2. The exploitation leaf updates: $p_\text{exploit}(M_{40}) = P(\theta_2 \geq 0.6 \mid M_{40}) \approx 0.40$.

After strategy revision: $\hat P_\Sigma(M_{40}) \approx (0.95 \times 0.73) \times (0.90 \times 0.40) = 0.693 \times 0.360 = 0.249$. Plan confidence has dropped from $0.485$ to $0.249$ — the agent correctly recognizes that its situation has deteriorated.

**What Section I alone cannot provide.** At $t = 40$, Section I reports: $\hat\theta_1 = 0.38$, $\hat\theta_2 = 0.52$, $\hat\theta_3 = 0.28$, and the per-arm mismatch signals. This tells the agent what it believes about each arm. It does NOT tell the agent:
- Whether its *goal* is still achievable ($\delta_\text{sat}$)
- Whether its *strategy* is the problem or the goal is ($\delta_\text{regret}$)
- Which *part* of the strategy is failing ($\delta_\text{strategic}$, edge residuals)
- What corrective action to take (the cascade's ordering)

### Observability Dominance ( #observability-dominance)

*Mapping: exact mechanism; approximate quantitative form.*

When the agent stops pulling arm 3 after the exploration phase (say at $t = 30$), the observation rate for arm 3 drops to $\nu_3 = 0$. By #update-gain:

$$\eta_3^\ast = \frac{U_{\text{edge},3}}{U_{\text{edge},3} + U_{\text{obs},3}}$$

With $U_{\text{obs},3} \to \infty$ (no observations): $\eta_3^\ast \to 0$. Arm 3's credence $p_3(M_t)$ is **frozen at its exploration-phase value**.

For the strategy DAG, the leaf node "arm 3 is best" has:
- Nominal credence: $p_3(M_t) \approx 0.05$ (from $t = 30$ beliefs)
- Path observability: $\sigma_3 = 0$ (arm 3 is not being pulled)
- Observability-adjusted confidence: $\text{conf}_\text{obs}(\text{arm 3 path}) = 0.05 \times 0 = 0$

Arm 3's path through the strategy is **epistemically dead** — the agent cannot learn whether arm 3 has become the best arm. If $\theta_3$ drifts to $0.9$ (which it might, given nonstationarity), the agent will never discover this through the exploitation-only policy.

**The observability-dominance diagnostic.** Compare arm 2 and arm 3:

| | Arm 2 | Arm 3 |
|---|---|---|
| Nominal credence $p_k$ | 0.52 | 0.28 (frozen) |
| Observability $\sigma_k$ | moderate (occasional pulls) | 0 (never pulled) |
| Adjusted confidence | $0.52 \times \sigma_2$ | 0 |
| Can be updated? | Yes | No |

Arm 2 is epistemically alive; arm 3 is epistemically dead. The agent should prefer exploring arm 2 (where it can learn) over arm 3 — unless it invests in making arm 3 observable again (pulling it despite low expected reward). This is the strategic case for exploration: not just expected value, but *observability maintenance*.

**Section I vs Section II diagnosis.** Section I reports $\hat\theta_3 = 0.28$ with growing uncertainty (the posterior variance increases under discounting with no new data). Section II adds the diagnostic: this arm's strategy path is epistemically dead ($\sigma_3 = 0$), and restoring observability has value beyond the arm's nominal expected reward.

### Edge Update via Gain ( #edge-update-via-gain)

*Mapping: exact for the Beta-Bernoulli case.*

When the agent pulls arm 1 at $t = 35$ and observes failure ($r_t = 0$):

**Leaf credence update.** The Beta posterior for arm 1 updates:

$$\beta_1 \to \beta_1 + 1, \quad \hat\theta_1 = \frac{\alpha_1}{\alpha_1 + \beta_1 + 1}$$

This is the standard conjugate update — the gain principle reduces to Bayesian updating in the binary case ( #edge-update-via-gain).

**Strategy propagation.** The updated $\hat\theta_1$ changes $p_1(M_t)$ (the credence that arm 1 is best). This propagates through the OR-node to the root:

$$s_{v_\text{id}}^{\text{new}} = 1 - (1 - p_1^{\text{new}})(1 - p_2)(1 - p_3)$$

The OR-node's status is *resilient* to single-arm credence drops: even if $p_1$ drops substantially, $p_2$ can compensate. This is the OR-node's structural advantage — redundancy absorbs single-edge failures.

**The exploitation edge.** The edge $p_{v_\text{exploit}, v_\text{root}} = 0.90$ is a causal credence: "pulling the identified-best arm reliably yields reward $\geq 0.6$." After observing repeated failures from arm 1:

$$\text{signal} = 0 \quad (\text{failure observed})$$

$$p_\text{exploit}^{\text{new}} = p_\text{exploit}^{\text{old}} + \eta_\text{edge} \cdot (0 - p_\text{exploit}^{\text{old}})$$

With $\eta_\text{edge} = U_\text{edge}/(U_\text{edge} + U_\text{obs})$, the exploitation edge's credence decreases. The rate of decrease is governed by the gain principle: well-established edges (many prior successes, $U_\text{edge}$ small) are slow to revise; newly formed edges are fast.

### Directed Separation ( #directed-separation)

*Mapping: exact. The agent is Class 1 (modular) by construction.*

The Beta-Bernoulli update for $M_t$ processes $(a_t, r_t)$ without reference to $(O_t, \Sigma_t)$:

$$(\alpha_{a_t}, \beta_{a_t}) \to (\alpha_{a_t} + r_t, \beta_{a_t} + 1 - r_t)$$

The update function $f_M$ has no $G_t$ argument. The strategy DAG then updates its leaf credences from the new $M_t$ — this is $f_G(G_t, M_{t+1}, e_t)$. The agent architecture is modular: a separate estimator (Beta posteriors) and planner (DAG evaluation), connected through the state-estimate interface.

$\kappa_\text{processing} = 0$ — no goal information flows into the epistemic update. Section II results apply exactly.

### Satisfaction Gap Dynamics

*Mapping: exact definition; approximate computation.*

Tracking $\delta_\text{sat}$ over time reveals the agent's evolving assessment of goal feasibility:

| Time | $\hat\theta_{k^\ast}$ | $A_O$ (approx) | $\delta_\text{sat}$ | Interpretation |
|------|---|---|---|---|
| $t = 0$ | 0.70 | 0.72 | $-0.12$ | Comfortably attainable |
| $t = 20$ | 0.68 | 0.70 | $-0.10$ | Still attainable |
| $t = 40$ | 0.52 | 0.57 | $+0.03$ | Marginally unmet |
| $t = 50$ (after exploring arm 2) | 0.75 | 0.77 | $-0.17$ | Attainable again — $M_t$ improved |
| $t = 70$ | 0.78 | 0.79 | $-0.19$ | Confidently attainable |

The key transition is $t = 40 \to 50$: $\delta_\text{sat}$ goes from positive (unmet) to negative (attainable) — not because the goal changed or the environment improved, but because $M_t$ improved. The agent explored arm 2, discovered $\hat\theta_2 \approx 0.75$, and its attainability assessment corrected upward. This matches the #satisfaction-gap disambiguation: the positive $\delta_\text{sat}$ at $t = 40$ was caused by a bad model, not an infeasible goal. The orient cascade's ordering (fix $M_t$ first, then reassess $\delta_\text{sat}$) produced the right diagnosis.

## The Section II Payoff

The purpose of this worked example is to demonstrate that Section II adds genuine diagnostic value beyond Section I. Here is the explicit comparison:

**Scenario at $t = 40$: arm 1 failing, arm 2 actually best, agent pulling arm 1.**

*Section I diagnosis.* The mismatch signal $\delta_t$ is large. The posterior $\hat\theta_1$ has dropped. Per-arm tempo $\mathcal T_1 \approx 0.016$ is adequate for tracking arm 1's drift. The agent knows arm 1 looks bad. Section I prescribes: update $M_t$ faster (increase $\eta^\ast$) or observe more (increase $\nu$).

*Section II diagnosis.* The orient cascade runs:
1. $M_t$ updates correctly — arm 1's posterior drops to $0.38$. (Directed separation: this happens goal-blindly.)
2. $\delta_\text{sat} = +0.03$ — the objective is marginally unmet. The agent's best-believed policy barely misses the target.
3. $\delta_\text{regret} = 0.19$ — the current policy (pulling arm 1) is far from the best available (pulling arm 2).
4. The 2x2 diagnostic says: "goal may be achievable, strategy is definitely suboptimal." Corrective action: revise $\Sigma_t$, then reassess $\delta_\text{sat}$.
5. Edge residuals localize the problem: the exploitation branch's predicted-vs-observed value gap is large. The leaf credences identify arm 2 as the best candidate.
6. Observability check: arm 3 is epistemically dead ($\sigma_3 = 0$). The agent should invest in observing arm 2 (or arm 3) before committing.

Section II tells the agent: *switch to arm 2, but first explore to confirm — the goal is probably still achievable, the current strategy is the problem, not the goal.* Section I tells the agent: *arm 1 looks bad.* The difference is the difference between a diagnosis and a symptom.

## Mapping Quality Summary

| ACT Concept | Bandit-Strategy Mapping | Status | Notes |
|---|---|---|---|
| Scope ( #scope-condition) | Exact | Definitional | Same as #worked-example-bandit |
| Model $M_t$ ( #agent-model) | Exact | Structural | Beta posteriors per arm |
| Mismatch $\delta_t$ ( #mismatch-signal) | Exact | Standard | Prediction error |
| Update gain $\eta^\ast$ ( #update-gain) | Exact | Conjugate | Beta-Bernoulli gain |
| Tempo $\mathcal{T}$ ( #adaptive-tempo) | Approximate | Per-arm decomposition | Assumes known allocation |
| Directed separation ( #directed-separation) | Exact | Class 1 by construction | Beta update is goal-blind |
| Objective $O_t$ ( #objective-functional) | Exact | Utility with threshold | $V_{O_t}^{\min} = 0.6$ |
| Value object $V_O$ ( #value-object) | Exact | Closed-form (greedy) | $V_O = \hat\theta_{k^\ast}$ |
| Satisfaction gap $\delta_\text{sat}$ ( #satisfaction-gap) | Exact | Definition applied | $V_{O_t}^{\min} - A_O$ |
| Control regret $\delta_\text{regret}$ ( #control-regret) | Exact | Definition applied | $A_O - V_O(\pi_\text{current})$ |
| Strategy DAG $\Sigma_t$ ( #strategy-dag) | Exact | AND/OR with 7 nodes | Small enough for manual propagation |
| AND/OR scope ( #and-or-scope) | Exact | Natural fit | Phase 1 is genuinely OR; root is genuinely AND |
| Status propagation | Exact | Closed-form | Forward pass computable by hand |
| Plan confidence $\hat P_\Sigma$ ( #strategy-dag) | Exact (computation) | From propagation; systematically optimistic under correlated failure | $0.485$ at $t = 0$ |
| Chain confidence decay ( #chain-confidence-decay) | Exact | Mathematical identity | AND-node multiplicative; OR-node resilient |
| Orient cascade ( #orient-cascade) | Exact (ordering) | All 5 steps exercised | Content is tractable in this domain |
| Observability dominance ( #observability-dominance) | Exact (mechanism) | Unpulled arms frozen | $\sigma_3 = 0 \Rightarrow \eta_3^\ast = 0$ |
| Edge update via gain ( #edge-update-via-gain) | Exact (binary case) | Beta-Bernoulli conjugate | Gain principle = Bayesian update |
| Strategic calibration ( #strategic-calibration) | Approximate | Credit assignment tractable here | Single-arm attribution is clean |
| Satisfaction gap dynamics | Exact | Time series of $\delta_\text{sat}$ | Model improvement resolves positive gap |

**Quantities that map cleanly.** All Section II definitions (objective, value object, satisfaction gap, control regret, strategy DAG) have exact instantiations. Plan confidence $\hat P_\Sigma$ is exact as a computation (the AND/OR propagation is correct), but systematically overestimates actual success probability under correlated edge failures ( #strategy-dag). In this toy bandit, edge independence is a reasonable approximation; in complex domains the overestimate may be severe. The orient cascade ordering is exact and all five steps are exercised.

**Quantities that map approximately.** Strategic calibration is approximate because even in this simple domain, attributing value changes to specific DAG edges requires assumptions about the agent's execution fidelity. Observability dominance is exact in mechanism but the multiplicative form $\text{conf}_\text{obs} = \text{conf} \cdot \text{obs}$ is a first-order approximation.

**Quantities that don't map.** No Section II quantity fails to map in this domain. The system is simple enough that every quantity is computable (at least approximately). This is the advantage of the bandit setting: it is the simplest system that exercises all Section II machinery.

## Epistemic Status

This is a *worked instantiation* — it demonstrates that the Section II formal chain is internally consistent and instantiable. The mapping quality is *conditional*: the quantitative relationships depend on the Beta-Bernoulli reward model, the specific DAG structure, and the parameterization. The qualitative conclusions — especially the diagnostic value of the 2x2 table and the orient cascade's ordering — should be robust across reward models and DAG topologies.

The status is *conditional* rather than *exact* because the attainability $A_O$ is approximated (the exact Bayes-optimal policy for a nonstationary bandit is intractable), and the strategic calibration mapping inherits the discussion-grade status of #strategic-calibration. The core Section II definitions (satisfaction gap, control regret, plan confidence) are exact instantiations.

## Working Notes

- This example uses a deliberately simple DAG (7 nodes, depth 2). A richer example with depth 3+ would better exercise chain confidence decay's exponential penalty and the evidence-starvation effect from #observability-dominance's quantitative discussion. A natural extension: add an intermediate "confirm arm $k$ is best" node between identification and exploitation, creating a 3-level chain.
- The explore-then-exploit policy is deliberately suboptimal to demonstrate nonzero $\delta_\text{regret}$. A Gittins-index agent would achieve $\delta_\text{regret} \approx 0$, demonstrating the "Success" cell of the 2x2 table. Comparing the two in the same environment would validate the control-regret diagnostic.
- The satisfaction gap dynamics table (Section "Satisfaction Gap Dynamics") would benefit from simulation confirmation. The specific numbers are plausible but hand-computed. A Monte Carlo study averaging over environment drift realizations would strengthen the claim.
- This example does not exercise strategy-level tempo ( #strategy-persistence-schema) or the three-way tradeoff ( #exploit-explore-deliberate). A future worked example targeting these would need a system with genuine deliberation costs — simulation in `msc/sim-three-way-tradeoff.py` provides a drifting-bandit version but found deliberation rarely dominates in simple settings.
- The DAG's AND/OR assignment is unambiguous in this domain (Phase 1 is genuinely disjunctive; the root is genuinely conjunctive). Domains where the AND/OR assignment is uncertain or updatable would be a stronger test of #and-or-scope.
