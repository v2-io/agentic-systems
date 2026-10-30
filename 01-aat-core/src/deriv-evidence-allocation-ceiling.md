---
slug: deriv-evidence-allocation-ceiling
type: derivation
status: exact
depends:
  - deriv-edge-credence-dynamics
  - result-sector-persistence-template
  - deriv-discrete-sector-condition
  - schema-strategy-persistence
stage: draft
---

# Derivation: Evidence-Allocation Ceiling on Strategic Persistence

When strategy edges that must all stay calibrated share one observation stream, each edge's credence lags a drifting truth by at least the drift accumulated since that edge was last observed, on average $\rho_\Sigma/\pi_i$ for an edge observed with probability $\pi_i$ per step. No update rule that averages observed outcomes, and no forgetting rate, does better than trusting the most recent observation, which attains the bound. A $K$-alternative OR node can therefore keep every alternative calibrated only if $\rho_\Sigma \lt R_\Sigma/K$, and a two-arm node only if $\rho_\Sigma \lt R_\Sigma/2$. The cap comes from how evidence is allocated, so the update mechanism cannot remove it.

## Formal Expression

### Setup

*[Formulation (allocation setting)]*

- **Edges and drift.** Edges $i = 1, \dots, K$ have true success probabilities $\theta_{i,t}$ that drift under Model D, $\lvert\theta_{i,t+1} - \theta_{i,t}\rvert \le \rho_\Sigma$ per time step, whether or not the edge is observed that step.
- **Fixed allocation.** At step $s$ edge $i$ is observed with probability $\pi_i$, independently of all outcomes and of the past. An observation reports $y_{i,s} \sim \text{Bernoulli}(\theta_{i,s})$ and is incorporated into $\hat p_{i,s+1}$. For one observation per step routed to one alternative of an OR node, $\sum_i \pi_i \le 1$. This is the allocation of #deriv-edge-credence-dynamics Prop B.4 ($\pi = (1-\varepsilon, \varepsilon)$); for a downstream AND-chain edge with observable intermediates (Prop B.2) the edge is observed when every upstream link fires, so $\pi_k = \prod_{j \lt k}\theta_j$.
- **Estimator class $\mathcal C$.** $\hat p_{i,t} = w_0\,\hat p_{i,0} + \sum_{s \in O_{i,t}} w_s\,y_{i,s}$, with $w \ge 0$, $\sum w = 1$, and the weights determined by the observation history $O_{i,t}$ (the steps before $t$ at which edge $i$ was observed), not by the outcomes. $\mathcal C$ contains Beta-Bernoulli updating with or without exponential forgetting, with the discount applied per observation or per time step (the counts depend only on $O_{i,t}$), every innovation-form update $\hat p + g(y - \hat p)$ with $g \in [0,1]$ set by the observation history, and the last-observation rule $\hat p_{i,t} = y_{i,\max O_{i,t}}$.
- **Mismatch and target.** $m_{i,t} = \mathbb{E}[\hat p_{i,t}] - \theta_{i,t}$, the mean-dynamics reading of Props B.1–B.4. Persistence of the node requires every edge's mean mismatch to stay within the reserve $R_\Sigma$: (SA3) of #schema-strategy-persistence, which asks that every OR alternative be kept calibrated.
- **Age.** $A_{i,t} = t - \max O_{i,t}$ if edge $i$ has been observed before $t$, and $A_{i,t} = t$ otherwise.

### Proposition EA.1 (Allocation lag)

*[Derived (Conditional on fixed allocation + estimator class $\mathcal C$ + Model D)]*

Start calibrated, $\hat p_{i,0} = \theta_{i,0}$. Under constant-sign drift $\theta_{i,s+1} - \theta_{i,s} = \rho_\Sigma$, every estimator in $\mathcal C$ satisfies

$$m_{i,t} \;\le\; -\rho_\Sigma\,\mathbb{E}[A_{i,t}], \qquad \mathbb{E}[A_{i,t}] = \frac{1 - (1-\pi_i)^t}{\pi_i} \;\uparrow\; \frac{1}{\pi_i}.$$

The last-observation rule attains it: under constant drift its mean mismatch is exactly $-\rho_\Sigma\,\mathbb{E}[A_{i,t}]$, and under any drift with $\lvert\theta_{i,s+1} - \theta_{i,s}\rvert \le \rho_\Sigma$ it satisfies $\lvert m_{i,t}\rvert \le \rho_\Sigma/\pi_i$ for all $t$.

**Proof.** The allocation is independent of the outcomes, so conditional on $O_{i,t}$ each observed $y_{i,s}$ still has mean $\theta_{i,s}$, and since the weights are fixed by $O_{i,t}$,

$$\mathbb{E}[\hat p_{i,t} \mid O_{i,t}] - \theta_{i,t} = -\Big(w_0\,(\theta_{i,t} - \theta_{i,0}) + \sum_{s \in O_{i,t}} w_s\,(\theta_{i,t} - \theta_{i,s})\Big).$$

Under constant drift $\theta_{i,t} - \theta_{i,s} = \rho_\Sigma(t-s)$. Every observed $s$ satisfies $t - s \ge A_{i,t}$, and the prior term has $t - 0 \ge A_{i,t}$. The weights sum to one, so the bracket is at least $\rho_\Sigma A_{i,t}$. Taking expectations over $O_{i,t}$ gives the bound. For $k \le t$, $A_{i,t} \ge k$ iff edge $i$ was unobserved at steps $t-1, \dots, t-k+1$, which has probability $(1-\pi_i)^{k-1}$; summing $\mathbb{E}[A_{i,t}] = \sum_{k=1}^{t}(1-\pi_i)^{k-1}$ gives the closed form. For the last-observation rule the bracket is exactly $\theta_{i,t} - \theta_{i,\max O}$, which is $\rho_\Sigma A_{i,t}$ under constant drift and at most $\rho_\Sigma A_{i,t}$ in magnitude under any bounded drift. $\square$

### Corollary EA.2 (Reachable region)

*[Derived (Conditional on Proposition EA.1)]*

For a single edge, the Model-D ultimate mean mismatch of the best estimator in $\mathcal C$ is $\rho_\Sigma/\pi_i$, so edge $i$ can persist iff $\rho_\Sigma \lt \pi_i R_\Sigma$. For a node whose edges must all persist, the reachable region is $\rho_\Sigma \lt R_\Sigma \min_i \pi_i$. When one observation per step is shared among $K$ alternatives, $\min_i \pi_i \le 1/K$, so

$$\sup_{\text{allocations},\ \mathcal C}\ \frac{\rho_\Sigma}{R_\Sigma} \;=\; \frac{1}{K},$$

attained by uniform allocation with the last-observation rule.

**Instances.**

- **Single edge** ($K = 1$, $\pi = 1$): $\rho_\Sigma \lt R_\Sigma$, the floor of #deriv-edge-credence-dynamics Prop B.1F, reached by exponential forgetting as $\lambda \to 0$.
- **Two-arm $\varepsilon$-greedy OR** (Prop B.4): $\rho_\Sigma \lt R_\Sigma \min(\varepsilon, 1-\varepsilon) \le R_\Sigma/2$, with equality only at $\varepsilon = 1/2$. With forgetting at the stationary per-observation gain $1-\lambda$, the admissible exploration interval is $\rho_\Sigma/((1-\lambda)R_\Sigma) \lt \varepsilon \lt 1 - \rho_\Sigma/((1-\lambda)R_\Sigma)$, non-empty iff $\rho_\Sigma \lt (1-\lambda)R_\Sigma/2$.
- **$K$-alternative OR:** $\rho_\Sigma \lt R_\Sigma/K$, matching the $1/k$ dilution of B.4's $k$-arm sector parameter.
- **AND chain with observable intermediates** (Prop B.2, upstream $\theta_j$ held fixed as there): the downstream edge $k$ persists only if $\rho_\Sigma \lt R_\Sigma \prod_{j \lt k}\theta_j$. The gates of Props B.6 and B.7 multiply into $\pi$ the same way.

### Discount convention

*[Formulation (where the discount is applied)]*

For an intermittently observed edge, exponential forgetting can discount the counts **per observation of that edge** or **per time step**. Both conventions lie in $\mathcal C$, so Corollary EA.2's cap holds under both and is approached under both as $\lambda \to 0^{+}$, where the most recent observation's weight tends to $1$. They differ below the cap. Per-observation discounting initialized at the stationary count gives each observation gain exactly $1-\lambda$ (Prop B.1F), so the expected per-step correction rate is exactly $\pi_i(1-\lambda)$. Per-time-step discounting lets the count decay between observations, so each observation lands with a larger gain. Its rate is at most $\pi_i$ by Proposition EA.1, but no closed form is derived here. At $\lambda = 0$ exactly, per-time-step discounting leaves an edge with $\pi_i \lt 1$ with a zero count between observations, so that convention needs $\lambda \gt 0$. The threshold $\lambda$ at which a given intermittent edge persists depends on the convention. The exploration interval above, and Prop B.4's (SA3), use per-observation discounting.

## Epistemic Status

*Exact* under the named conditions: (i) fixed allocation, independent of outcomes; (ii) estimator class $\mathcal C$, convex combinations of observed outcomes with outcome-independent weights; (iii) Model D drift per time step on every edge, observed or not; (iv) the persistence target that every alternative stay calibrated, (SA3); (v) the mean-mismatch reading that Props B.1–B.4 use. Proposition EA.1's inequality is pathwise in the observation history, and the corollary is its expectation. The supremum $1/K$ is attained, so the cap is sharp within (i)–(v).

Two routes give the result. The expected-correction route uses a deterministic per-observation gain $g_i \le 1$: edge $i$'s per-step sector parameter is $\pi_i g_i \le \pi_i$, and #deriv-discrete-sector-condition DA.1 gives the ultimate bound $\rho_\Sigma/(\pi_i g_i)$. The age route of Proposition EA.1 also covers gains that depend on the observation history, as in Beta-Bernoulli updating away from its stationary count and in per-time-step discounting. The two routes agree where both apply.

Outside the conditions, the result is not claimed. Under state-dependent allocation (greedy switching, UCB, Thompson sampling) the observation history depends on outcomes, so the weights are no longer outcome-independent and the proof does not apply as written. Estimators that extrapolate a learned drift fall outside $\mathcal C$ (their weights are not a convex combination of past outcomes). Under constant drift they can lag less; whether a worst case over drift sequences restores a comparable bound is open. If only the currently chosen alternative must stay calibrated, the target changes and so does the cap.

## Discussion

**Where the cap comes from.** One observation per step can refresh only one alternative. While an alternative goes unobserved, its truth keeps moving and nothing the agent does to its credence can follow. The best any averaging rule can do is put all weight on the newest evidence. Its lag is then the drift since the last refresh, on average $1/\pi_i$ steps of drift. Forgetting governs how much old evidence is kept, and the ceiling sits above every forgetting rate. Forgetting's own structural role is the other boundary: without it (B.1, $\lambda = 1$) the gain decays to zero and every positive drift rate is eventually fatal.

**Parametric tuning cannot cross the ceiling; structural change can.** Above $\rho_\Sigma = R_\Sigma \min_i \pi_i$, no forgetting rate, exploration rate, or update rule in $\mathcal C$ keeps every alternative calibrated. What moves the ceiling changes the strategy's structure or its evidence channels:

- More evidence per step, which breaks $\sum_i \pi_i \le 1$: parallel trials, or counterfactual or off-policy observation of alternatives not taken.
- Fewer alternatives held in calibration: prune the OR node, or relax the requirement for alternatives the agent has stopped considering.
- For AND chains, direct observation of deeper links, which raises $\pi_k$ above $\prod_{j \lt k}\theta_j$.

This has the same shape as #result-structural-adaptation-necessity at the epistemic layer, where parametric adaptation cannot close a gap that a class change can. The correspondence is structural, at discussion grade. It is not a derivation of one result from the other.

**Breadth costs drift tolerance.** Each alternative an agent keeps calibrated divides the drift rate it can survive. The design question for an OR node is therefore how many alternatives the evidence stream can keep calibrated at the environment's $\rho_\Sigma/R_\Sigma$, not only which alternative is best: at most $R_\Sigma/\rho_\Sigma$ of them. The answer follows from the allocation alone, and the update rule does not change it.

## Findings

### Evidence allocation caps strategic persistence at $\rho_\Sigma \lt R_\Sigma/K$

**Brief:** An agent keeping several alternative plans in view can try only one per turn. The real odds of every plan keep shifting, so a plan's estimate is out of date by however much the world moved since that plan was last tried, on average $1/\pi$ turns of drift for a plan tried with probability $\pi$. No way of updating beliefs or forgetting old evidence beats simply trusting the most recent trial, and that rule's lag is exactly this. So if $K$ alternatives must all stay accurate, the world can drift at most $1/K$ of the agent's error tolerance per turn; with two alternatives, half.

**Impact:** Locates where the strategic-persistence design space is genuinely capped. The cap comes from how evidence is allocated across alternatives that must stay calibrated, not from the forgetting mechanism, which reaches the universal single-edge floor $\rho_\Sigma \lt R_\Sigma$. It gives (SA3) of #schema-strategy-persistence a satisfiability condition: SA3 can be met iff $\rho_\Sigma \lt R_\Sigma \min_i \pi_i$, at most $R_\Sigma/K$. Past the ceiling, the remedies are structural: more evidence channels per step, fewer alternatives held in calibration, or direct observation of deep links. A strategy's breadth is purchased with drift tolerance.

**Novelty Claim:** *Claim differentiation.* That an arm's estimate cannot track drift faster than it is sampled is elementary, and the non-stationary bandit literature treats the explore-versus-track trade-off in regret terms. The AAT contribution is stating it as a sharp reachability ceiling on the sector-persistence form across a whole estimator class: Bayesian counts with or without forgetting under either discount convention, and every history-gained innovation update. It covers OR alternatives, starved AND edges and the gated L1 cases in one statement, and it attaches to (SA3) a satisfiability condition the schema did not have.

**Related Work:**

| ASF Concern | Prior-art Language | Relationship / Positioning |
|---|---|---|
| Tracking drifting arms under limited sampling | Garivier & Moulines 2011, *On Upper-Confidence Bound Policies for Switching Bandit Problems*, ALT 2011 (discounted and sliding-window UCB) | *conceptual precursor*: explore-versus-track trade-off under non-stationarity, stated as regret rather than as a persistence ceiling |
| Variation-budget non-stationary bandits | Besbes, Gur & Zeevi 2014, *Stochastic Multi-Armed-Bandit Problem with Non-stationary Rewards*, NeurIPS 2014 | *conceptual precursor*: drift budget versus achievable regret; AAT's $\rho_\Sigma$ plays the variation-budget role per step |
| Exponential forgetting | Ljung 1987, *System Identification: Theory for the User*, MIT Press | *formal antecedent*: the discounted update whose two conventions both fall in $\mathcal C$ |
| Parametric cannot, structural can | #result-structural-adaptation-necessity | *parallel structural pattern* at the epistemic layer |

**Search Log:**
- 2026-10-30 (*intuition-only*): the sampling-lag bound is elementary; the bandit-tracking literature above was recalled, not searched for this framing. Targeted future search: persistence or stability formulations of non-stationary bandits (not regret), and "observation scheduling for tracking" in sensor-management literature.

## Working Notes

- **Verification provenance.** Proposed in the 2026-10-30 adversarial verification of the strategic-persistence forgetting analysis (`spikes/spike-strategic-persistence-hard-ceiling-convention-2026-05-31-verify-1.md` §5.1, expected-correction route). Re-derived independently by its integrator via the age route above, and checked with an exact mean-lag simulation (outcomes replaced by their means, which is exact for $\mathcal C$ under fixed allocation) at $\pi \in \{1, 0.5, 0.3\}$, $\lambda \in \{0, 0.5, 0.9\}$ under both discount conventions: per-observation rates matched $\pi(1-\lambda)$ to four decimals, and per-time-step rates stayed at or below $\pi$, approaching it as $\lambda \to 0^{+}$. Record: `spikes/spike-strategic-persistence-hard-ceiling-convention-2026-05-31-verify-1-integration-notes.md`.
- **Strengthening direction.** Extend Proposition EA.1 beyond $\mathcal C$ (drift-extrapolating estimators) and to state-dependent allocation, plausibly as a minimax statement over drift sequences of bounded magnitude.
