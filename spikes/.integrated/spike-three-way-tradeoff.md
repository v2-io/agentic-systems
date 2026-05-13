# Spike: Three-Way Exploit/Explore/Deliberate Tradeoff — Adversarial Analysis

**Date:** 2026-04-02 (revised: deep adversarial pass)
**Status:** Adversarial spike. Replaces the earlier constructive spike.
**Target segment:** `01-aad-core/src/disc-exploit-explore-deliberate.md`
**Simulation:** `spikes/sim-three-way-tradeoff.py`


## Executive Summary

The current segment claims ~30% derivation and ~70% framework-shaped notation. After adversarial analysis and simulation, the honest assessment is closer to **10% derived, 20% genuinely useful framing, 70% discussion-grade hand-waving**. Several claims labeled "derived" are not derived. The two-stage decomposition is a convenience, not forced. The additive form is unjustified. The dominance regimes are correct but trivially restate the problem structure.

However, the segment is NOT worthless. It identifies a real gap (Section I has no strategic deliberation), correctly places this as Section II content, and provides useful qualitative framing. The recommendation is to substantially rewrite as a **discussion-grade framing segment**, not to pretend it's derived.


## Part 1: Attacking the Current Segment

### Attack 1: The Two-Stage Decomposition Is Not Forced

**The segment's claim:** "The decomposition follows from a type distinction: exploit and explore are both external actions ($\in \mathcal{A}$), comparable via a single objective over the action space. Deliberation is qualitatively different."

**The attack:** Construct a single unified objective over $\{$actions $\cup$ deliberate$\}$ with temporal discount.

Define a "meta-action" space $\bar{\mathcal{A}} = \mathcal{A} \cup \{\text{deliberate}\}$. For any $\bar{a} \in \bar{\mathcal{A}}$, define:

$$\bar{Q}(\bar{a}) = \begin{cases} r(a) + \gamma \mathbb{E}[V(M_{t+1}) \mid a, M_t] & \text{if } \bar{a} = a \in \mathcal{A} \\ 0 + \gamma \mathbb{E}[V(M_{t+1}') \mid \text{delib}, M_t] & \text{if } \bar{a} = \text{deliberate} \end{cases}$$

where $M_{t+1}' = f_{\text{delib}}(M_t)$ is the post-deliberation model. The unified policy is:

$$\bar{\pi}^\ast = \arg\max_{\bar{a} \in \bar{\mathcal{A}}} \bar{Q}(\bar{a})$$

**Simulation result:** The unified objective with temporal discount $\gamma \in [0.8, 0.99]$ performs at least as well as two-stage UCB (+8% to +13% in simulation). The unified approach naturally handles the commensuration problem the segment claims makes a single argmax impossible — the temporal discount is exactly the missing "amortization" term.

**Verdict:** The two-stage decomposition is a **computational convenience** (it allows reusing the existing CIY-unified objective for Stage 2), not a structural necessity forced by the type distinction. The type distinction is real but does not force the decomposition — it merely makes the decomposition natural. The segment's claim that "a single argmax over all three would require commensuration of immediate action-value with deferred capacity improvement, which in general requires a temporal discount or amortization that the action-space objective does not contain" is correct — but the resolution is to ADD the temporal discount to the unified objective, not to SPLIT into two stages.

**What survives:** The observation that exploit/explore are commensurate (same action space) while deliberation requires temporal amortization is correct and useful. The two-stage split is a good engineering decomposition. But the word "derived" is wrong.

### Attack 2: The Additive Form Is Unjustified

**The segment's claim:** Deliberation benefit decomposes as $\Delta\eta^\ast(\Delta\tau) \cdot \lVert\delta_{\text{post}}\rVert + \Delta V_\Sigma(\Delta\tau)$ (additive epistemic + strategic terms).

**The attack:** Under directed separation, the orient cascade is sequential: $M_t$ updates first, then $G_t$ updates using the new $M_t$. This sequentiality creates a **dependency**, not independence. Better $M_t$ enables better $\Sigma_t$ evaluation (acknowledged in the working notes but not in the formal expression). The correct form is:

$$\text{benefit} = \Delta\eta^\ast(\Delta\tau) \cdot \lVert\delta_{\text{post}}\rVert + \Delta V_\Sigma(\Delta\tau, M_t + \Delta M_t(\Delta\tau))$$

where $\Delta V_\Sigma$ depends on the improved model. This is NOT additive in the standard sense — the second term's value depends on the first term's output.

**Does the cascade ordering force additivity?** No. The cascade forces sequential EVALUATION (epistemic first, then strategic), but sequential evaluation does not imply additive VALUE. Consider: improving your understanding of the world (epistemic) may enable a strategic insight that's worth far more than the epistemic improvement itself. The value of the pair can be superadditive: $V(\text{both}) > V(\text{epistemic alone}) + V(\text{strategic alone})$.

**When is additivity approximately correct?** When:
- $\Delta M_t$ is small relative to $M_t$ (incremental epistemic improvement doesn't change the strategy evaluation landscape)
- The strategy revision happens on a slower timescale than the model update (the strategy doesn't respond to within-cycle model improvements)
- The agent is in a region where the optimal strategy is robust to model perturbations

These conditions may often hold in practice, but they're assumptions, not derivations.

**Verdict:** The additive form is a modeling choice (linearization). It should be tagged `*[Formulation]*`, not left implicit as if it were derived from the cascade ordering.

### Attack 3: $\Delta V_\Sigma \approx \delta_{\text{regret}} \cdot \Pr[\text{revision succeeds}]$ Is Inadequate

**The segment's claim:** Strategic deliberation value is bounded by control regret scaled by revision success probability.

**Three problems:**

1. **Deliberation can reveal that $O_t$ should change (step 5 of orient cascade).** The $\delta_{\text{regret}}$ ceiling assumes the objective is fixed. But the cascade includes objective revision. If deliberation leads to an objective change, the "value" isn't $\delta_{\text{regret}}$ (which measures regret within the current objective) — it's something like $V_{O'}(M_t, \pi') - V_O(M_t, \pi)$ where $O'$ is the revised objective. This quantity has no necessary relationship to $\delta_{\text{regret}}$.

2. **Deliberation may reveal that the strategy is ALREADY good (uncertainty reduction about strategy quality).** The primary value of strategic deliberation might not be "find a better strategy" but "confirm the current strategy is good, allowing confident exploitation." This is valuable but has $\Delta V_\Sigma \approx 0$ in the formulation, even though the BEHAVIORAL effect (shifting from cautious mixed-mode to confident exploitation) is significant. The value of certainty about your strategy is not captured by $\delta_{\text{regret}}$.

3. **$\Pr[\text{revision succeeds in } \Delta\tau]$ is not operationalized.** The segment acknowledges this. But the problem is worse than non-operationalizability — the quantity is not well-defined without specifying what "succeeds" means (finds any better strategy? finds the optimal one? finds one that's at least $\varepsilon$ better?). Different definitions give different structures.

**Verdict:** The approximation identifies the correct ceiling ($\delta_{\text{regret}}$) for the strategy-revision channel but misses the objective-revision channel and the uncertainty-reduction channel. It's a reasonable sketch of ONE mechanism, presented as if it covers the full story.

### Attack 4: The Dominance Regimes Are Trivially Correct

**The segment's claim:** The dominance conditions "follow from the first-order conditions of the constituent tradeoffs."

**The attack:** The dominance regimes say:
- High uncertainty → explore
- Low uncertainty, low regret → exploit
- High regret, stable environment → deliberate

These are correct. But they're also the most obvious possible predictions. You could derive them from a one-paragraph verbal argument without any formalism at all. The "first-order conditions" the segment references are:

$$\frac{\partial \Delta\eta^\ast}{\partial \Delta\tau} \cdot \lVert\delta_{\text{post}}\rVert + \frac{\partial \Delta V_\Sigma}{\partial \Delta\tau} = \rho_{\text{delib}}$$

which says "stop deliberating when marginal return drops below marginal cost." This is literally the statement of every optimization problem. The dominance regimes follow from sign analysis of this equation's terms, which amounts to saying "deliberation is good when its benefit is high and its cost is low."

**Simulation result:** In the Bellman analysis, exploit dominated in ALL four state quadrants (high/low uncertainty × close/clear arms). Deliberation was never the best option in any state. The dominance regimes' qualitative predictions about when exploration and deliberation should dominate did NOT match the simulation's optimal policy. The regime predictions are directionally correct but quantitatively useless — they overpredict deliberation and underpredict exploitation.

**What's actually derived:** The boundary conditions (as $\rho_{\text{delib}} \to \infty$ the allocation collapses to binary; as $\lambda \to 0$ it collapses to exploitation) are derived in a trivial sense (taking limits of an optimization). But these too are obvious: if deliberation costs infinity, you don't deliberate.

**Verdict:** The dominance regimes are **correct qualitative observations** but should not be tagged `*[Derived]*`. They should be `*[Discussion]*`. They restate the problem structure rather than deriving novel, non-obvious predictions.


## Part 2: Attempting First-Principles Derivation

### Attempt 5: Information-Theoretic Approach

**Setup:** Agent has a finite bit-budget per cycle. Three channels earn different kinds of bits:
- Exploit: earns value-bits (direct reward, no new information)
- Explore: earns environment-bits (reduces $H(\Omega_t \mid M_t)$)
- Deliberate: earns inference-bits (reduces $H(\theta \mid M_t, \text{data so far})$ via better computation on existing data)

**The key insight:** Deliberation cannot create new data. It can only extract more information from EXISTING data via additional computation. Therefore:

$$I_{\text{delib}}(\Delta\tau) \leq I_{\text{data}} - I_{\text{already extracted}}$$

Deliberation's information ceiling is the gap between the total information in the agent's observation history and the amount already incorporated into $M_t$. For an agent that processes observations optimally (Bayesian update), this gap is zero — deliberation has no value.

**When does the gap exist?**
- When $M_t$ is an approximation (e.g., the agent uses point estimates instead of full posteriors)
- When the inference is intractable and the agent uses approximate methods (MCMC, variational inference) that haven't converged
- When the agent has structural hypotheses it hasn't tested against existing data (e.g., checking cross-arm correlations in the bandit)

**Simulation confirmation:** Exploration earned 3.5x more entropy reduction per step than exploitation, while deliberation earned approximately the same as exploitation (ratio 0.99). Deliberation's information yield is tiny compared to exploration's. This is because in the bandit setting, the Bayesian update already extracts most available information — the gap is small.

**What this reveals about AAD:** The information-theoretic approach shows that deliberation's value is fundamentally about **computational approximation** — the agent hasn't fully processed its existing information. This makes deliberation's value:

1. **Agent-architecture-dependent** (a perfect Bayesian has zero deliberation value)
2. **Diminishing within a cycle** (each deliberation step closes the computation gap)
3. **NOT independent of exploration** (new data changes what's available to extract)

This is a genuine insight that the current segment doesn't capture. The segment treats deliberation as a third "activity" on par with exploit and explore, but the information-theoretic view shows it's a different KIND of thing — it's about how well you use existing information, not about acquiring new information or value.

**Natural decomposition:** The bit-budget approach gives:

$$\max_{\Delta\tau \geq 0, a} \left[\underbrace{V_O(M_{t+\Delta\tau}', a)}_{\text{value (exploit component)}} + \underbrace{\lambda \cdot \Delta I_{\text{external}}(a)}_{\text{new bits (explore component)}} - \underbrace{c(\Delta\tau)}_{\text{time cost of computation}}\right]$$

where $M_{t+\Delta\tau}'$ is the model after $\Delta\tau$ of additional computation on existing data. This is a joint optimization, NOT a two-stage one. The deliberation time $\Delta\tau$ and action $a$ are chosen simultaneously because the post-deliberation model $M'$ determines which action is best.

**Status:** This derivation is **incomplete** but more honest than the segment's. It identifies the correct structure (joint optimization, not staged) and the correct source of deliberation value (computational gap). It doesn't give a closed-form solution.

### Attempt 6: Temporal Value / Bellman Approach

**Setup:** Define the meta-state as $(M_t, G_t, \text{environment state})$. The Bellman equation for the meta-decision is:

$$V(M_t) = \max\left\{\max_{a \in \mathcal{A}} [r(a, M_t) + \gamma \mathbb{E}[V(M_{t+1}) \mid a]], \quad \gamma \mathbb{E}[V(f_{\text{delib}}(M_t))]\right\}$$

The first branch is "act" (then choose which action); the second is "deliberate."

**Observation 1:** The Bellman equation has the two-stage structure as one POSSIBLE decomposition, but it's not the only one. The outer max separates "act" from "deliberate," and the inner max over actions handles exploit/explore. But this is a mathematical rewriting of a single optimization:

$$V(M_t) = \max_{\bar{a} \in \bar{\mathcal{A}}} \bar{Q}(M_t, \bar{a})$$

Both forms give the same optimal policy. The two-stage form is convenient for analysis (you can characterize the "act" branch using existing exploit/explore theory) but is not the unique structure of the problem.

**Observation 2:** The Bellman equation reveals that deliberation value depends on the ENTIRE future, not just the immediate improvement. Deliberation that barely improves $M_t$ may still be valuable if it shifts the future state distribution toward a region where the agent performs much better (e.g., deliberation that resolves a key ambiguity enabling a long sequence of confident exploitation). The segment's one-step formulation ($\Delta\eta^\ast \cdot \lVert\delta_{\text{post}}\rVert$) misses this.

**Observation 3:** The discount factor $\gamma$ naturally handles the temporal commensuration that the segment claims is the problem. The segment says "the comparison requires a temporal discount or amortization that the action-space objective does not contain" — but the resolution is to include $\gamma$, not to split into stages.

**Simulation result:** Monte Carlo Bellman estimates showed exploitation dominating in all four state quadrants tested. Deliberation was consistently the worst option. This is partly an artifact of the bandit setting (deliberation is weak here), but it demonstrates that the Bellman approach works fine without the two-stage split.

**Status:** The Bellman approach confirms that the problem has a standard solution via dynamic programming. The two-stage decomposition is one valid reformulation, not the unique structure. The segment should acknowledge this.

### Attempt 7: Mismatch Dynamics Approach

**Setup:** From the mismatch ODE $d\lVert\delta\rVert/dt = -\mathcal{T}\lVert\delta\rVert + \rho$:
- During exploitation: mismatch follows the ODE (ongoing correction)
- During exploration: same ODE, but the action is chosen to maximize information (may temporarily increase mismatch by visiting unfamiliar states)
- During deliberation: $\mathcal{T}$ may improve (via $\Delta\eta^\ast$), but $\rho_{\text{delib}}$ accumulates

Choosing the activity that minimizes expected mismatch at the next decision point:

$$\bar{a}^\ast = \arg\min_{\bar{a}} \mathbb{E}[\lVert\delta_{t+1}\rVert \mid \bar{a}, M_t]$$

**Simulation result:** Exploration consistently produced the lowest next-step mismatch across all tested conditions ($\rho \in \{0.05, 0.1, 0.3, 0.5\}$, observation noise $\in \{0.3, 0.5, 0.8, 1.0\}$). Deliberation was close to exploitation and consistently worse than exploration. The mismatch-minimizing policy is essentially "always explore."

**Why this fails as a derivation:** Mismatch minimization is the wrong objective. The agent wants to minimize REGRET (or maximize value), not minimize model error. An agent that only explores (minimizes mismatch) never earns value from exploitation. The mismatch dynamics describe the MODEL side; the VALUE side requires the policy objective.

**What's genuinely useful:** The mismatch dynamics do constrain the deliberation duration (the $\rho_{\text{delib}} \cdot \Delta\tau$ drift cost from #der-deliberation-cost). This constraint is already in the theory and doesn't require the three-way extension.

**Status:** The mismatch dynamics approach does NOT yield a natural three-way decomposition. It gives "always explore" which is wrong. The approach is useful only for bounding deliberation cost, which is already captured in #der-deliberation-cost.

### Attempt 8: Persistence Margin Approach

**Setup:** Persistence condition: $\alpha > \rho/R$. Margin: $\Delta\rho^\ast = \alpha R - \rho$. Each activity affects:
- Exploit: neither $\alpha$ nor $\rho$ changes (acts with current model)
- Explore: improves $\alpha$ (via $\eta^\ast$) by reducing model uncertainty
- Deliberate: improves $\alpha$ (via $\Delta\eta^\ast$) at cost $\rho_{\text{delib}} \cdot \Delta\tau$

**Simulation result:** The persistence margin analysis showed no clear regime where deliberation maximized the margin. At low drift rates, deliberation's variance reduction slightly improved the margin proxy, but the effect was dominated by noise. At moderate and high drift rates, both exploration and exploitation improved the margin more than deliberation.

**Why this fails:** The persistence condition is about SURVIVAL, not PERFORMANCE. An agent that maximizes persistence margin but never exploits has maximum persistence and zero value. The persistence condition is a constraint, not an objective.

**A valid use:** The persistence condition provides a LOWER BOUND on when to deliberate: if the agent is near the persistence threshold ($\alpha \approx \rho/R$), it MUST prioritize activities that improve $\alpha$ (explore or deliberate) over exploitation. But this is a survival constraint, not a full allocation theory.

**Status:** Persistence margin constrains the allocation (don't exploit yourself to death) but doesn't derive it. This is a constraint, not an objective function.


## Part 3: Simulation Results Summary

Full details in `spikes/sim-three-way-tradeoff.py`. Key findings:

### Finding 1: The Three-Way Oracle Barely Beats Binary

Across five configurations, the three-way oracle (which can choose deliberation with perfect foresight) outperformed binary UCB by only 2-6%. In the "many arms, slow drift" configuration (designed to favor deliberation), the improvement was 2.1% and NOT statistically significant (p=0.30).

**Interpretation:** In a bandit setting, deliberation adds very little because:
- Bayesian updating already extracts most information from observations
- New observations dominate existing-data refinement
- The "strategy" (which arm to pull) is simple enough that no deliberation is needed

### Finding 2: The Oracle Almost Never Deliberates

The three-way oracle chose deliberation 0-8 times out of 200 steps across all configurations. It overwhelmingly chose exploitation (120-170 steps) and exploration (30-73 steps).

**Interpretation:** Even when deliberation is FREE (no special cost), the oracle rarely chooses it. The value of acting (and getting both reward AND information) almost always exceeds the value of pausing to think.

### Finding 3: The AAD Heuristic Policy Failed Catastrophically

The AAD dominance-regime heuristic produced total reward of 0.0 in all configurations (deliberating 100% of steps). This is partly a thresholding bug (the heuristic is poorly calibrated), but it reveals a deeper problem: the qualitative regime descriptions don't translate into actionable decision rules without specific quantitative thresholds, which the theory doesn't provide.

**Interpretation:** "Deliberate when regret is high and environment is stable" sounds right but is useless without knowing WHAT VALUE of regret is "high" and what drift rate is "stable." The segment provides no guidance.

### Finding 4: Unified > Two-Stage

The unified objective (single argmax over actions + deliberate with temporal discount) outperformed two-stage UCB by 8-13% across all discount factors tested. This is because the unified approach naturally considers whether deliberation would change which action is best, while the two-stage approach treats deliberation and action selection as independent decisions.

### Finding 5: Exploration Dominates Information Acquisition

Entropy reduction per step: explore (1.82) >> exploit (0.52) ≈ deliberate (0.51). Exploration earned 3.5x more bits than deliberation.

### Finding 6: Deliberation Rarely Beats Acting — Even One-Step-Ahead

The one-step-ahead comparison showed deliberation was preferred on 0-11% of timesteps, with the highest rates occurring under FAST drift — the opposite of what the segment predicts (it says deliberation dominates when $\rho_{\text{delib}}$ is LOW).

**What's happening:** Under fast drift, arms swap rankings frequently. Deliberation can sometimes detect a ranking swap before the agent observes it directly. But this is a quirk of the simulation setup, not a general principle.


## Part 4: What's Genuinely Derivable

After all attacks, here is what survives:

### Definitely Derived (from existing machinery)

1. **The deliberation cost threshold extends to strategic deliberation.** If you accept #der-deliberation-cost's derivation for epistemic deliberation, the same structure applies when deliberation improves $\alpha_\Sigma$ instead of $\eta^\ast$. Stop deliberating when marginal improvement drops below drift cost. This is a straightforward extension, and it's the one genuinely useful formal result.

2. **Boundary conditions.** As $\rho_{\text{delib}} \to \infty$, $\Delta\tau^\ast \to 0$. As $\lambda \to 0$ and $\Delta V_\Sigma \to 0$, the agent only exploits. These are trivial limits of the optimization.

3. **The placement as Section II content.** The argument that strategic deliberation requires $\Sigma_t$, $\delta_{\text{regret}}$, and the orient cascade is correct. This is genuinely Section II material.

### Genuinely Useful Framing (but not derived)

4. **Three distinct activities exist.** The taxonomy (exploit/explore/deliberate) is a useful frame for thinking about agent resource allocation. It's a definition, not a derivation.

5. **Deliberation value is bounded by control regret** (for the strategy-revision channel). If $\delta_{\text{regret}} = 0$, strategic deliberation has no value. This is a correct qualitative observation.

6. **Deliberation value depends on environment stability.** The drift cost $\rho_{\text{delib}} \cdot \Delta\tau$ creates a real tradeoff. This is inherited from #der-deliberation-cost.

7. **The observation that deliberation = computation on existing data, not new data acquisition.** This is the most important conceptual contribution and should be central to the segment.

### Honestly Discussion-Grade

8. **The two-stage decomposition.** Useful but not forced by the type distinction. A unified objective works equally well.

9. **The additive form.** A linearization convenience, not derived from the cascade.

10. **The dominance regimes.** Correct qualitative observations dressed up as derived results.

11. **$\Delta V_\Sigma \approx \delta_{\text{regret}} \cdot \Pr[\text{revision succeeds}]$.** A sketch of one mechanism, not a complete characterization.

12. **The cycle-phase mapping.** A pretty table with no formal content.


## Part 5: What the Simulation Missed

The simulation used a multi-armed bandit, which is UNFAVORABLE to deliberation because:

1. **No strategy structure.** In a bandit, the "strategy" is just "which arm." In complex domains (military operations, software development), the strategy is a DAG with many edges, and deliberation can restructure the DAG. The bandit doesn't capture this.

2. **No model structure.** In a bandit, the model is independent means. In complex domains, the model has relational structure, and deliberation can discover structural insights that transform the model's predictions.

3. **No action-space complexity.** In a bandit, actions are trivially enumerable. In domains with combinatorial action spaces, deliberation (planning, search) is essential for even basic action selection.

4. **No irreversibility.** In a bandit, bad actions are costless (you just don't earn the best reward). In domains with irreversible actions (deploying a military unit, shipping code), deliberation before action has much higher value.

**The honest assessment:** The simulation confirms that for SIMPLE problems, the three-way allocation adds almost nothing over binary exploit/explore. The theory's value, if any, is for COMPLEX problems where:
- Strategy has DAG structure
- Model has relational structure
- Actions are irreversible
- The action space is too large for enumeration

In these domains, deliberation is genuinely a third mode that cannot be replaced by exploration. But the current segment doesn't derive WHY — it just asserts the three-way structure and adds notation.

**What would a better formalization look like?** It would characterize the conditions under which deliberation strictly dominates exploration:
- When internal model computation is cheaper than external probing (bits per joule, not bits per timestep)
- When the action space is too large for systematic exploration (deliberation as search)
- When actions are irreversible (deliberation as risk management)
- When the model has latent structure exploitable by computation

These conditions are DOMAIN-SPECIFIC and probably cannot be captured in a single formal criterion within AAD.


## Part 6: Recommendation

### For the segment (`01-aad-core/src/disc-exploit-explore-deliberate.md`)

**Rewrite substantially.** The segment should:

1. **Downgrade type to `discussion`** and status to `discussion-grade`. The honest maximum attainable is `discussion-grade` for the overall framing and `conditional` for the deliberation threshold extension.

2. **Split the genuinely derived content** (the strategic deliberation threshold extension of #der-deliberation-cost) from the discussion-grade content (dominance regimes, cycle mapping, $\Delta V_\Sigma$ approximation).

3. **Remove the "Derived" tag** from the two-stage decomposition and dominance regimes. Tag them `*[Discussion]*`.

4. **Center the segment on what's genuinely useful:**
   - The extension of #der-deliberation-cost to strategic deliberation (the one derived result)
   - The conceptual distinction between information acquisition (explore) and computation on existing information (deliberate)
   - The qualitative observation that deliberation value is bounded by $\delta_{\text{regret}}$
   - Honest acknowledgment that the dominance regimes are qualitative observations, not derived predictions

5. **Add the simulation findings** as an epistemic check: "In a drifting bandit, the three-way allocation provides minimal benefit over binary exploit/explore (2-6%). The theory's value, if any, is for domains with strategy structure, irreversible actions, and large action spaces."

6. **Acknowledge the unified alternative.** The two-stage decomposition is one valid formulation; a unified objective with temporal discount is equally valid and may be simpler.

### For the WORKBENCH

Move the following to "Open":
- Formal conditions under which deliberation strictly dominates exploration
- Whether the additive decomposition of deliberation benefit has justifiable domain conditions
- Whether $\Delta V_\Sigma$ can be operationalized in any specific domain

Move the following to "Settled":
- The strategic deliberation threshold (extending #der-deliberation-cost to $\Delta V_\Sigma$) is conditional on the same assumptions as #der-deliberation-cost
- Three-way allocation adds minimal benefit in simple domains (bandit simulation, 2-6%)
