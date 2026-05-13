# Spike: Stability-Induced Myopia

**Date.** 2026-04-22

**Status.** Research spike. Not a promoted segment. The argument below is exploratory; it probes whether the observed barrier-to-structural-adaptation at high-operating-points is structurally forced by AAD's machinery or already captured by existing segments.

**Bottom line (deposited up front, argued below).** There IS a structural result in this neighborhood, and it is *not* fully subsumed by `#disc-exploit-explore-deliberate`, `#result-structural-adaptation-necessity`, or `#schema-strategy-persistence`, though each of those contributes an ingredient. The result is a *detection-latency theorem*: under the canonical configuration (no forgetting, C1 convention, gradient credit assignment, on-policy data), the expected number of cycles between regime change and structural-revision trigger scales linearly in the accumulated pseudo-count $n$ on load-bearing edges. This is a direct consequence of the log-odds coordinate forced by `#deriv-edge-update-natural-parameter` composed with `#disc-identifiability-floor` Instance 1 (on-policy L0/L1 detection no-go). The barrier-to-structural-adaptation is real, it is forced, and it composes with AAD's existing meta-architecture. The recommendation is promotion to an appendix segment, not a main-line segment — the result sharpens existing machinery rather than standing alone.


## 1. Problem Statement

**Empirical observation.** Agents at high-operating-point exhibit a higher barrier to structural adaptation than agents at low-operating-point. The immediate cost of restructuring is concrete and visible (reduced capability during transition). The benefit is future-contingent and uncertain. Mature organizations, stable species, established technology platforms, and political systems all show this pattern:

- Christensen (1997, *The Innovator's Dilemma*): successful firms systematically fail to adopt disruptive technology that would cannibalize current revenue streams.
- Levitt & March (1988, "Organizational learning"): **competency traps** — accumulated skill at the current approach raises the threshold for switching to a potentially better one.
- Hannan & Freeman (1984, "Structural inertia and organizational change"): older, more structured organizations exhibit measurably higher resistance to restructuring.
- March (1991, "Exploration and exploitation in organizational learning"): organizations systematically under-invest in exploration relative to a horizon-balanced optimum, because exploitation returns are certain and exploration returns are deferred and uncertain.
- Eldredge & Gould (1972, "Punctuated equilibria"): evolutionary populations exhibit long periods of stasis punctuated by rapid restructuring — stasis is the high-fitness trap.

**The question this spike addresses.** Is this barrier *structurally forced* by how AAD's machinery accumulates — a theorem about high-operating-point states — or is it merely a decision-theoretic choice falling out of `#disc-exploit-explore-deliberate`'s oracle analysis (which already shows deliberation is rarely chosen)?

**Notation for "high-operating-point."** The task uses "$\kappa$" informally; but $\kappa$ in AAD (specifically $\kappa_{\mathrm{processing}}$ in `#der-directed-separation`) is a distinct architectural coupling parameter. To avoid collision, I use the operating-point descriptor:

$$\mathrm{OP}(A) = (\Delta\rho^\ast,\; \mathcal{F}(\mathcal{M}),\; \{n_{ij}\}_{(i,j)\in E},\; \delta_{\mathrm{regret}},\; \lambda)$$

for an agent $A$ with: adaptive reserve $\Delta\rho^\ast = \alpha R - \rho$, model-class fitness $\mathcal{F}(\mathcal{M})$, per-edge accumulated pseudo-counts $\{n_{ij}\}$, control regret $\delta_{\mathrm{regret}}$, and forgetting rate $\lambda$. A *high* operating point has: $\Delta\rho^\ast$ positive and large, $\mathcal{F}(\mathcal{M})$ near 1, $n_{ij}$ large for load-bearing edges, $\delta_{\mathrm{regret}}$ small, $\lambda$ near 1 (weak forgetting). A *low* operating point has the opposite — narrow margin, modest fitness, small $n$, positive regret, strong forgetting ($\lambda$ well below 1).

The observed barrier is the claim: at high $\mathrm{OP}$, the agent defers structural adaptation when warranted, more often than at low $\mathrm{OP}$.


## 2. What This Is NOT

Before attempting a derivation, this spike distinguishes the target phenomenon from three adjacent ones that existing segments already handle.

### 2.1 NOT `#result-structural-adaptation-necessity`'s failure condition

`#result-structural-adaptation-necessity` says: when $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$, parametric adaptation cannot close the mismatch floor. This is a result about *when structural adaptation is necessary*. It does not say when it is *chosen*. The myopia question is about the gap between necessity and choice — about the agent's *detection* of the trigger.

An agent whose model class has genuinely become inadequate — where `#result-structural-adaptation-necessity`'s hypothesis is satisfied at truth — may still fail to detect this because its own signals (residuals, attainability, regret) are computed under the current model class. The segment itself notes (Epistemic Status) that the corollary "persistent irreducible mismatch is diagnostic of model class inadequacy" is conditional on an alignment assumption; without alignment, the lost predictive information manifests in proper-scoring regret rather than one-step mismatch. Proper-scoring regret is not a quantity the typical agent computes.

**Distinction:** `#result-structural-adaptation-necessity` says WHEN to restructure. Stability-induced myopia says why the agent's DETECTION SIGNAL for restructuring is suppressed when the conditions for restructuring are actually satisfied.

### 2.2 NOT `#disc-exploit-explore-deliberate`'s oracle result

`#disc-exploit-explore-deliberate` Epistemic Status reports: *"The oracle almost never chose deliberation (0–8 out of 200 steps)."* This is a finding about what an oracle with full ground-truth would do in a drifting multi-armed bandit: under the specific simulation regime, deliberation rarely pays. The segment's regime descriptions (exploit-dominates / explore-dominates / deliberate-dominates) are qualitative observations, not derived thresholds.

The oracle result is *unfavorable* evidence for the myopia claim as usually stated: "agents defer when they shouldn't." If even the oracle defers, deferral isn't mistake — it's correct decision-theory under the simulation's structure.

**But the oracle result is compatible with the myopia claim in the following important way:** the simulation was designed to make deliberation's *strategic benefit* small — "no strategy structure, small action space, reversible actions" (segment's own caveat). The oracle's deferral is correct *given* the setup. The myopia claim is about settings where the strategic benefit of deliberation is actually large (structural regime change invalidating load-bearing edges), but the agent's signal for that benefit is suppressed. The oracle sees the truth; the agent sees its signals. The gap between them is exactly where stability-induced myopia lives.

**Distinction:** `#disc-exploit-explore-deliberate` evaluates a decision given signals. Stability-induced myopia is about the *quality of the signals themselves* — specifically about a predictable bias in those signals as a function of operating point.

### 2.3 NOT `#schema-strategy-persistence`'s forgetting prerequisite

`#schema-strategy-persistence` derives: for Beta-Bernoulli edges, $\alpha_\Sigma = 1/(n+1)$ decays monotonically with experience. Without forgetting ($\lambda$ close to 1), $\alpha_\Sigma \to 0$ and persistence eventually fails. The segment calls this the *forgetting prerequisite* and positions it as structural: an agent without forgetting has no long-run strategic persistence.

This is closely related to the myopia phenomenon and supplies its critical ingredient, but it is not the full phenomenon. The segment's framing is: "forgetting is required for asymptotic persistence to hold at all." The myopia framing is: "*while* the agent is persisting, detection of regime change is delayed in proportion to accumulated $n$." These compose: the forgetting prerequisite tells you that weak forgetting eventually kills structural persistence; the myopia result tells you that weak forgetting simultaneously delays detection of structural drift in a quantifiable way.

**Distinction:** the forgetting prerequisite states a *necessary condition for long-run persistence to hold*. Myopia states a *detection-latency consequence on the way there*.

### 2.4 NOT `#disc-identifiability-floor` Instance 1 alone

Instance 1 of `#disc-identifiability-floor` says: under on-policy execution, no detection mechanism can distinguish L0-insufficient from L0-sufficient DAGs (Bareinboim CHT applied). The five boundary routes characterize escape via $\varepsilon$-exploration, joint observability, intermediate-state observability, structural priors, or direct intervention.

The myopia phenomenon *includes* Instance 1 as a contributing mechanism: when regime change introduces a latent common cause (L0 → L1 structural transition at truth), the agent's on-policy signals cannot detect it. But the myopia phenomenon is broader: it covers regime changes that do NOT involve L0/L1 transitions — e.g., changes in the true edge probability $p^\ast_{ij}$ within the current L0 graph, or drift in the environment dynamics that the current model class continues to cover but with degraded efficiency.

**Distinction:** Instance 1 is a *structural no-go* result on detecting one specific change (L0 → L1 transition). Myopia is a *detection-latency* result covering a broader class of regime changes, for which Instance 1 is one component among three.

### 2.5 Summary of what's settled vs. what remains

| Existing segment | Contributes | Does NOT supply |
|---|---|---|
| `#result-structural-adaptation-necessity` | Defines trigger condition at truth | Does not characterize detection by agent |
| `#disc-exploit-explore-deliberate` | Gives decision rule given signals | Does not audit signal quality across operating points |
| `#schema-strategy-persistence` | Supplies $\alpha_\Sigma = 1/(n+1)$ decay and forgetting prerequisite | Does not connect to detection latency for regime change |
| `#disc-identifiability-floor` Inst. 1 | Forbids detection of L0/L1 transition from on-policy data | Covers only the structural (L0/L1) transition case |
| `#deriv-edge-update-natural-parameter` | Forces log-odds coordinate as unique additive-evidence form | Does not connect the forced coordinate to detection latency |

What remains: a *composed* result using the log-odds coordinate's additivity structure + the on-policy detection no-go + the $1/(n+1)$ per-cycle update magnitude to bound the expected cycles-to-detect as a function of accumulated $n$. This is what the rest of the spike attempts.


## 3. The Attempt: Detection-Latency Theorem

### 3.1 Setting

Fix an agent operating at the high operating point described in §1. Specifically:

- The strategy DAG $\Sigma_t$ uses Beta-Bernoulli edges with per-edge pseudo-count $n_{ij}$. Let $n_{\min} = \min_{(i,j) \in E_{\mathrm{load}}} n_{ij}$ over the load-bearing edges — those on the current active plan path.
- Credit assignment uses the default gradient-based log-odds rule from `#disc-credit-assignment-boundary`, with identifiability $\iota_k = 1$ for observable edges.
- Continuation convention is C1 (one-step improvement, canonical default).
- The agent has no forgetting mechanism — pseudo-counts accumulate monotonically.
- The model-class fitness $\mathcal{F}(\mathcal{M})$ is high at the pre-change regime. Adaptive reserve $\Delta\rho^\ast$ is positive.

At cycle $t_0$, a regime change occurs. Let the change be parametrized by a scalar $\varepsilon$ representing the L0-observable footprint of the change — i.e., the magnitude of the shift in the one-step residual distribution detectable under on-policy execution. Three sub-cases cover the main regime-change shapes:

- **(R1) Within-class drift.** A true edge probability $p^\ast_{ij}$ shifts by $\varepsilon$. The L0 graph is still correct; only parameters have moved.
- **(R2) Model-class inadequacy.** $\mathcal{F}(\mathcal{M})$ drops to $1 - \varepsilon$. Section `#result-structural-adaptation-necessity` triggers at truth.
- **(R3) Structural (L0 → L1) transition.** A latent common cause becomes active, introducing correlation between sibling edges that was absent before. L0 graph is now insufficient.

### 3.2 Mechanism 1 — Log-odds accumulation rate (both cases R1 and R2)

Under the default signal function (log-odds coordinate, `#disc-credit-assignment-boundary`):

$$\lambda_k^{\mathrm{new}} = \lambda_k + \eta_{\mathrm{edge}} \cdot \iota_k \cdot J_k \cdot (y_G - \hat P_\Sigma) / \lVert \mathbf{J}\rVert^2$$

with $\eta_{\mathrm{edge}} = 1/(n_{ij}+1)$ for Beta-Bernoulli. Per-cycle, the expected log-odds update magnitude is bounded:

$$\mathbb{E}\lvert \Delta\lambda_k \rvert \leq \frac{\lvert J_k \rvert \cdot \mathbb{E}\lvert y_G - \hat P_\Sigma \rvert}{\lVert \mathbf{J}\rVert^2 \cdot (n_k + 1)}$$

Under regime change (R1 or R2) the expected systematic residual $\mathbb{E}[y_G - \hat P_\Sigma]$ scales with $\varepsilon$: $\mathbb{E}\lvert y_G - \hat P_\Sigma \rvert = \Theta(\varepsilon)$ as $\varepsilon \to 0$.

Therefore, cycle-by-cycle, the log-odds coordinate on a load-bearing edge moves by at most $\Theta(\varepsilon / (n_k + 1))$ in expectation.

For the agent to cross a detection threshold $\Delta\lambda_{\mathrm{detect}}$ — whatever threshold the operational diagnostic uses to flag a significant credence shift — the number of cycles required is at least:

$$T_{\mathrm{detect}}^{(\mathrm{R1 \lor R2})} = \Omega\!\left( \Delta\lambda_{\mathrm{detect}} \cdot (n_k + 1) / \varepsilon \right)$$

This is derivable from the log-odds additivity structure of `#deriv-edge-update-natural-parameter`: because log-odds is the *unique* additive-evidence coordinate (Cauchy functional equation under evidential-additivity axiom), the per-cycle increment is fixed at $O(1/(n+1))$ in this coordinate. No change of parameterization can escape this — the Fisher-equivalent statement holds in any sensible coordinate. The detection time is structurally forced to scale linearly in $n$.

**This is the first piece of the myopia result.** The bound is not a property of any particular detection algorithm; it's a property of the evidence-accumulation structure.

### 3.3 Mechanism 2 — C1 diagnostic blindness (case R2)

Under C1 continuation, the control regret diagnostic is:

$$\delta_{\mathrm{regret}}^{(1)} = A_O^{(1)}(M_t) - V_O(M_t, \pi_{\mathrm{current}})$$

Both $A_O^{(1)}$ and $V_O(\pi_{\mathrm{current}})$ are computed under the *current* $M_t$. When regime change R2 invalidates the model class (truth drifts outside $\mathcal{M}$), both quantities are biased in the same direction — they both overestimate what is actually achievable. The *gap* $\delta_{\mathrm{regret}}^{(1)}$ stays small because the bias is common-mode.

The satisfaction gap $\delta_{\mathrm{sat}}^{(1)} = V_{O_t}^{\min} - A_O^{(1)}$ does not cancel in this way — but it is subject to the disambiguation table in `#def-satisfaction-gap`: before revising $O_t$, the orient cascade checks $M_t$ adequacy, $\Pi$ expressiveness, and $N_h$. If $M_t$ passes its own internal adequacy check (residuals look OK because the model is within-class confidently wrong — `#result-structural-adaptation-necessity` calls this "gain collapse without performance"), the cascade's orientation phase provides no signal for model-class change.

The monotonicity result from `#def-value-object` ($\delta_{\mathrm{regret}}^{(1)} \leq \delta_{\mathrm{regret}}^{\mathrm{RH}} \leq \delta_{\mathrm{regret}}^{\mathrm{B}}$) says C1 gives the *smallest* regret estimate — the one most likely to look near-optimal when global optimality is failing. This is a feature for computational tractability but a liability for structural-drift detection.

**This is the second piece of the myopia result.** The canonical C1 default systematically under-reports regret when the underlying model is structurally drifting. Agents using richer conventions (C2 or C3) would detect R2-class regime change earlier, but at super-linear computational cost.

### 3.4 Mechanism 3 — On-policy detection no-go (case R3)

When regime change R3 introduces a latent common cause, `#disc-identifiability-floor` Instance 1 applies directly: under on-policy execution, no detection mechanism can distinguish L0-insufficient from L0-sufficient DAGs with matched regime conditionals. The expected detection time is *unbounded* without access to one of the five boundary routes: $\varepsilon$-exploration, joint sibling observability, intermediate-state observability, structural priors, or direct intervention.

The high-operating-point agent is precisely the agent *least* likely to satisfy these escape conditions. At high $\mathrm{OP}$:

- **$\varepsilon$-exploration is minimal.** The agent's policy has converged; exploration would be expensive (low immediate value under current $M_t$, uncertain future value). Under `#disc-exploit-explore-deliberate`, the CIY-unified objective deprecates exploration when $\lambda(M_t) \to 0$, which happens precisely when model uncertainty is low — the high-OP condition.
- **Joint sibling observability is policy-dependent.** Short-circuit AND/OR execution at high OP tends to stop at first success/failure, censoring sibling outcomes. Effective $\varepsilon$-exploration (regime-aware) is required to violate this, which brings us back to the exploration cost.
- **Intermediate-state observability requires infrastructure.** Observability is a design choice; at high OP, the agent has no incentive to add instrumentation.
- **Structural priors are not automatically present.** Unless the agent was explicitly initialized with a suspicion of L1 structure, it won't check for it.
- **Direct intervention is the most expensive route.** Deliberate disturbance to test causal structure is the strongest signal but the highest-cost action at high OP.

**This is the third piece of the myopia result.** Under R3-type regime change, the detection no-go applies directly, and high-OP agents are structurally least equipped to satisfy the boundary routes that escape it.

### 3.5 Composition — the theorem shape

Combining §3.2, §3.3, §3.4: the expected time from regime change to structural-revision trigger is bounded below by an expression monotone in accumulated operating-point quantities.

**Claim (detection-latency theorem, attempt).** For an agent at operating point $\mathrm{OP}$ experiencing regime change with observable footprint $\varepsilon$:

$$\mathbb{E}[T_{\mathrm{detect}}] \geq \begin{cases} C_1 \cdot (n_{\min} + 1) / \varepsilon & \text{(R1: within-class drift)} \\ C_2 \cdot (n_{\min} + 1) / \varepsilon + C_3 \cdot \mathcal{C}(\mathrm{convention}) & \text{(R2: model-class inadequacy)} \\ \infty \text{ unless escape route active} & \text{(R3: structural L0 → L1)} \end{cases}$$

where $C_1, C_2, C_3$ are positive constants depending on the agent's detection threshold and DAG topology, $\mathcal{C}(\mathrm{convention})$ is the additional latency from C1 blindness (zero under C3, positive under C1), and the $\infty$ in R3 reflects `#disc-identifiability-floor` Instance 1 unless the agent is in an escape route.

**Corollary (probability bound).** The probability that the agent triggers structural revision within the next $T$ cycles after regime change is bounded:

$$\Pr[\text{structural revision triggered within } T] \leq g(n_{\min}, T, \varepsilon)$$

where $g$ is decreasing in $n_{\min}$ and increasing in $\varepsilon$ and $T$.

### 3.6 Tier and Scope Assessment

**What this gets right:**

- The $1/(n+1)$ scaling is exact for Beta-Bernoulli, robust qualitative for any update rule with log-odds natural parameter (which `#deriv-edge-update-natural-parameter` argues is forced by evidential additivity).
- The R1 bound is derivable given the log-odds coordinate is forced. The derivation uses `#deriv-edge-update-natural-parameter` + Pinsker-style inequality for the residual-to-log-odds transfer.
- The R3 case is a direct application of `#disc-identifiability-floor` Instance 1.
- The R2 case is the weakest — the C1 blindness argument is qualitative at this stage; making it quantitative requires coupling the common-mode bias between $A_O^{(1)}$ and $V_O(\pi_{\mathrm{current}})$ to the specific form of model misspecification.

**What it does NOT get:**

- It does not bound the *probability that regime change is warranted but not chosen*. That would require a model of the agent's restructuring decision rule (which varies) and the cost structure (which is domain-specific).
- It does not distinguish "should restructure but doesn't" from "should restructure but correctly defers because restructuring costs more than waiting." The theorem is about signal latency, not about whether the signal, once received, yields the right decision.
- It does not speak to settings where the agent has strong forgetting ($\lambda$ well below 1). Under strong forgetting, $n_{\mathrm{eff}} = 1/(1-\lambda)$ is bounded, and the $n_{\min}$-scaling disappears. This is consistent with the qualitative observation: organizations with strong turnover / institutional memory decay exhibit less inertia.

**Epistemic tier of the full claim:**
- R1 sub-case: *robust qualitative* with an *exact* path (derivable from `#deriv-edge-update-natural-parameter` + update-rate bound).
- R2 sub-case: *discussion-grade* currently; promotable to *conditional* with a quantitative C1-blindness model.
- R3 sub-case: *exact* (direct from `#disc-identifiability-floor` Instance 1 + $\varepsilon$-exploration cost under `#disc-exploit-explore-deliberate`).
- Composition: *discussion-grade*, pending sharpening of R2.

The *qualitative* claim — "expected detection time is monotone in accumulated $n$" — is robust across all three sub-cases. The *specific* scaling is $1/(n+1)$ for R1 and R2, and the sub-cases compose additively with R3's structural no-go.


## 4. Answering the Task's Five Questions

### 4.1 Is there actually a structural theorem, or is `#disc-exploit-explore-deliberate` already the full account?

**There is a structural theorem.** `#disc-exploit-explore-deliberate` is about decision given signals; the myopia theorem is about the signals themselves. The two compose: even a perfect decision rule operating on degraded signals produces deferred action. The oracle result ("deliberation rarely chosen") is a *lower bound on what a perfect-information agent does*, not an analysis of what a myopic agent does — these are different.

The theorem lives at a different scale from `#disc-exploit-explore-deliberate`: it's about the *bias in the inputs* to that decision, not the decision itself. This is the distinction between "how good is the agent at deciding given data" vs. "how informative is the data the agent has access to" — the latter being the territory `#disc-identifiability-floor` opened and this spike extends.

### 4.2 What's the precise mechanism?

The task offered four candidate mechanisms. The derivation above touches all four:

| Task-candidate mechanism | Derivation contact |
|---|---|
| Higher-$\kappa$ agents have larger sunk investment in adaptive reserve | *Partial.* §3.5 touches adaptive reserve, but the specific sunk-cost framing was not load-bearing. The primary mechanism is evidence accumulation $n$, not reserve $\Delta\rho^\ast$. |
| Local (C1) diagnostic tractability masks global structural drift | **Direct.** §3.3 — Mechanism 2. |
| Strategy-DAG complexity makes restructuring cost grow | *Peripheral.* `#form-strategy-complexity-cost`'s description length is relevant but not load-bearing for detection latency; it's relevant for the *cost* side, which is not what the theorem addresses. |
| Convention hierarchy: C1 diagnostics miss structural drift visible at C3 | **Direct.** §3.3 — Mechanism 2 in its convention form. |

The derivation found a *fifth* mechanism the task did not enumerate: the log-odds evidence-accumulation rate scaling as $1/(n+1)$ is the primary quantitative lever, and it is *structurally forced* by `#deriv-edge-update-natural-parameter`. This is the mechanism most deeply AAD-native — it emerges from the constructive meta-pattern (`#additive-coordinate-forcing`) rather than from general decision-theory considerations.

### 4.3 Is this distinct from `#result-structural-adaptation-necessity`?

Yes — see §2.1. `#result-structural-adaptation-necessity` is about WHEN restructuring is needed at truth; stability-induced myopia is about DETECTION LATENCY between truth-change and agent-trigger. `#result-structural-adaptation-necessity` is a characterization of the condition; myopia is a characterization of the agent's ability to recognize that the condition has been satisfied.

### 4.4 Is there a bound of shape "probability of deferring structural adaptation when warranted $\geq g(\mathrm{OP})$"?

Yes — the corollary in §3.5 gives exactly this shape, with $g$ decreasing in $n_{\min}$. However, the cleanest form of the bound is expected-time-to-trigger rather than probability-of-deferral — the latter requires a time horizon $T$, which the former can be translated into via Markov's inequality or tight concentration.

### 4.5 Does this interact with multi-timescale stability?

Yes, but obliquely. `#der-temporal-nesting` (and the forthcoming multi-timescale stability sketch in `#sketch-multi-timescale-stability`) treat the timescale separation as: parametric updates (fast) vs. structural updates (slow). The myopia theorem adds an empirical prediction about this separation: **the slow timescale gets slower with accumulated fast-timescale state.** An agent whose fast-timescale updates have averaged over large $n$ will have a structurally slower slow-timescale response to regime change. The two timescales are not independent — the fast one's accumulated state feeds back into the slow one's responsiveness. This is the formal version of the institutional-inertia observation.

An interesting side-observation: the forgetting prerequisite ($\lambda \lt 1 - \rho_\Sigma/R_\Sigma$) in `#schema-strategy-persistence` can be read as *"the slow timescale must be prevented from slowing below a structural threshold."* The myopia theorem says the same thing from the detection side: without forgetting, slow-timescale responsiveness degrades proportionally to accumulated fast-timescale state, eventually crossing the threshold at which regime-change detection cannot keep up with regime-change rate.


## 5. Comparison to Adjacent Literature

### 5.1 Christensen's *Innovator's Dilemma*

Christensen's empirical observation is that successful firms systematically miss disruptive technology. The common interpretation is about *incentive structure* (cannibalization of current revenue). The myopia theorem provides a *complementary epistemic* interpretation: even with incentive alignment, the firm's signal-detection system is structurally slow to flag regime change because accumulated experience suppresses per-observation update magnitude. The two interpretations compose — incentive barriers + signal suppression both delay response.

### 5.2 Levitt & March competency traps

Competency traps are usually framed as: "practice at option A raises expected return of A, which raises relative value of A vs. B, which increases practice of A." This is a positive-feedback story about the exploit/explore tradeoff. The myopia theorem supplies a mechanism for the *signal* side of this story: as practice accumulates, the per-practice-unit information accumulated decays as $1/(n+1)$. So the competency trap is not merely decision-theoretic (option A looks better) but information-theoretic (evidence against A is dilutedby prior accumulation).

### 5.3 Hannan & Freeman structural inertia

Their density-dependence argument gives inertia as a function of organizational age/size. The myopia theorem offers a mechanism: older organizations have larger $n$ on load-bearing edges, and the detection-latency bound is monotone in $n$. This gives a micro-foundation for their macro-observation, at least in the strategic-DAG sense.

### 5.4 March exploration/exploitation

March's concern is long-run under-investment in exploration relative to a horizon-balanced optimum. The myopia theorem is a complementary finding: at high $\mathrm{OP}$, exploration's *perceived* value drops (because CIY is estimated under the current model, which is overconfident), and exploration's *actual* value for detecting regime change is exactly what the myopia theorem says is required to escape `#disc-identifiability-floor` Instance 1. The agent's signals say "exploration is not worth it"; the theorem says "exploration is the unique broadly-available violation of the detection no-go."

### 5.5 Eldredge-Gould punctuated equilibria

In evolutionary biology, stasis-then-punctuation is the observed pattern. The myopia theorem gives a cognitive/organizational analog: stasis is the regime where accumulated $n$ suppresses detection; punctuation is the regime where $\varepsilon$ finally exceeds the threshold $\Delta\lambda_{\mathrm{detect}} (n+1)$ and the log-odds coordinate crosses the trigger. Miller (2022)'s extreme transition motif (referenced in `#result-structural-adaptation-necessity` Discussion) provides one constructive mechanism for the punctuation side; the myopia theorem provides one constructive mechanism for the stasis side.

### 5.6 Reinforcement learning under non-stationarity

The CUSUM and generalized likelihood ratio tests in the change-detection literature give the information-theoretic best-case for detection latency: roughly $\log(1/\alpha) / D_{\mathrm{KL}}(P_0 \Vert P_1)$ cycles for false-alarm rate $\alpha$. The myopia theorem's bound $\Omega((n+1)/\varepsilon)$ is *worse* than this information-theoretic optimum because the agent uses a Bayesian credence accumulator rather than an optimal change-detector. The gap is load-bearing: it is the cost of using the forced log-odds coordinate rather than a bespoke change-detector. An agent that added an explicit CUSUM sidecar could beat the myopia bound; the bound characterizes the cost of running the theory's default machinery without such augmentation.

This connects to `#der-directed-separation`'s IDT (Information Digital Twin) note: Hafez et al. (2026) show that a sidecar monitor on bi-predictability $P$ and entropy change $\Delta H$ detects perturbations at 89% accuracy vs. 44% for reward-based monitoring. The myopia theorem is an AAD-native explanation: on-policy reward signals are the log-odds-accumulator; bi-predictability is a causal-structural test that effectively acts as the change-detector sidecar.


## 6. How This Composes With AAD's Meta-Segments

Reading the myopia theorem through the three meta-segments of CLAUDE.md §7:

### 6.1 Through `#disc-separability-pattern` (positive half)

The myopia theorem sits along the **identification-regime ladder** of `#disc-separability-pattern`: high-OP agents are stuck in Regime C (observational) because their exploration has collapsed; low-OP agents retain sufficient exploration to keep Regime A or B access to load-bearing edges. The theorem is about the *cost* of sliding down this ladder with accumulated experience. The "structured repair" position in the ladder — instrumenting for joint sibling observability — is exactly the boundary-route escape from `#disc-identifiability-floor` Instance 1 that §3.4 identifies as hardest to satisfy at high OP.

### 6.2 Through `#disc-identifiability-floor` (negative half)

The theorem is partially a *generalization* of Instance 1: where Instance 1 forbids detection of L0/L1 transitions under on-policy data, the myopia theorem weakens this to a *latency bound* under on-policy data for a broader class of regime changes. The structural no-go becomes a quantitative no-go: detection is not forbidden, but structurally slow in a way that tracks accumulated operating-point state.

If promoted, the myopia theorem would be a candidate **Instance 3** of `#disc-identifiability-floor`, with the shape:

1. **Setting.** Detect regime change (R1/R2/R3) from on-policy data while accumulating Bayesian credences under the default update rule.
2. **External theorem.** Combination of Cauchy functional equation (forcing log-odds coordinate) and Bareinboim CHT (forbidding L0/L1 on-policy detection).
3. **No-go.** Expected detection time is $\Omega(n_{\min}/\varepsilon)$ for R1/R2 and unbounded for R3 absent escape routes.
4. **Boundary characterization.** Forgetting ($\lambda \lt 1 - \rho_\Sigma/R_\Sigma$), sidecar change-detector, active exploration, richer continuation convention.
5. **Strengthened consequence.** The forgetting prerequisite elevates from "required for asymptotic persistence" to "required for detection-latency to be bounded independently of operating point." This sharpens `#schema-strategy-persistence`.

### 6.3 Through `#additive-coordinate-forcing` (constructive half)

The theorem is *structurally enabled* by the additive-coordinate-forcing move. Specifically, `#deriv-edge-update-natural-parameter` forces the log-odds coordinate via the evidential-additivity axiom (Aczél 1966 Cauchy functional equation). In this forced coordinate, the per-cycle update is $O(1/(n+1))$ — the accumulation-rate consequence is *automatic* given the coordinate. If the coordinate were not forced, one might hope for a faster-updating alternative. Because it is forced, the $1/(n+1)$ bound is structural.

This is a case where AAD's meta-patterns interact with specific claims in a productive way: the constructive pattern (forcing a coordinate) has a downstream consequence (bounded detection rate) that lands as part of the negative pattern (identifiability floors). The myopia theorem is where the three meta-patterns co-produce a result neither could produce alone.


## 7. Recommendation

### 7.1 Is this worth promoting?

Yes — as an appendix segment, not a main-line segment. Rationale:

- The result *sharpens* existing segments (`#schema-strategy-persistence`, `#result-structural-adaptation-necessity`, `#disc-exploit-explore-deliberate`, `#disc-identifiability-floor`) rather than standing alone. Sharpening work belongs in appendix-adjacent positions.
- The R1 sub-case is derivable to *robust qualitative* with a clean proof path; the R3 sub-case is direct from Instance 1; the R2 sub-case needs more work. An appendix segment can stage these three tiers.
- There is a clear downstream effect: the *corollary* of §6.2 — elevating the forgetting prerequisite's load-bearing role — belongs in `#schema-strategy-persistence`'s Discussion. This spike's content would flow into both the new appendix segment and a sharpening edit on `#schema-strategy-persistence`.

### 7.2 Proposed segment structure

**Slug.** `#detection-latency-at-high-operating-point` (or shorter: `#stability-detection-latency`).

**Type.** `result` (the bounds are derived) or `discussion` (if R2 remains unfinished and the segment presents the three sub-cases as a cluster).

**Status.** `conditional` (conditional on log-odds coordinate + Beta-Bernoulli update rule + observable-footprint parametrization of regime change).

**Depends on.**
- `edge-update-natural-parameter` (log-odds coordinate forced)
- `credit-assignment-boundary` (default signal function in log-odds)
- `identifiability-floor` (Instance 1 for R3)
- `strategy-persistence-schema` (forgetting prerequisite)
- `structural-adaptation-necessity` (trigger condition at truth)
- `value-object` (C1 convention)
- `exploit-explore-deliberate` (decision rule on signals)

**Stage.** Would land at `draft`. R1 and R3 bounds would be at derivation-level; R2 would carry an honest note that the sub-case is qualitative.

### 7.3 Integrations into existing segments

If promoted, three cross-segment touches:

1. **`#schema-strategy-persistence` Discussion.** Add a note that the forgetting prerequisite also bounds detection latency for regime change, not only asymptotic persistence. Cite the new segment.

2. **`#disc-identifiability-floor`.** Add the new segment as a candidate Instance 3, or as an adjacent floor in the "Adjacent Floors (Open Research Directions)" section that has now been derived rather than open.

3. **`#disc-exploit-explore-deliberate` Working Notes.** Add an observation that the oracle's low deliberation rate and the myopia theorem are complementary — oracle sees truth and defers correctly in simple regimes; agent sees degraded signals and defers for reasons that compound. The asymmetric cost of restructuring vs. deliberating observed in the simulation gains a theoretical underpinning.

### 7.4 If NOT promoted

If the reviewer judges R2 too incomplete and R1 too derivable-from-existing-machinery, the appropriate disposition is:

- Absorb R1's $1/(n+1)$ bound into `#disc-credit-assignment-boundary` Discussion as an observation about detection latency.
- Absorb R3 reference into `#disc-identifiability-floor` Working Notes as a more specific latency consequence of Instance 1.
- Retain this spike as exploratory record.

The lower-cost disposition is viable and would capture about 60% of the content. The appendix segment is the higher-leverage disposition and captures the composition result (the three mechanisms co-act) that the distributed-absorption path would not surface.

### 7.5 Honest epistemic close

This spike did not produce a new theorem by itself — what it did was:

1. Distinguish the myopia phenomenon from four adjacent phenomena already covered by segments. The distinctions are real and load-bearing.
2. Compose three existing AAD mechanisms (log-odds accumulation rate; C1 blindness; Instance 1 no-go) into a *detection-latency* claim that none of them makes individually.
3. Identify the $1/(n+1)$ scaling as the load-bearing quantity, and connect it to `#additive-coordinate-forcing` as structurally forced rather than contingent.
4. Surface a concrete strengthening move for `#schema-strategy-persistence` (the forgetting prerequisite is load-bearing for detection latency, not only asymptotic persistence).

Whether this rises to the level of a new appendix segment is a judgment call the reviewer should make against the backlog. The underlying phenomenon is real; the AAD-native mechanism is identifiable; the cross-segment composition is new. But none of the three pieces is itself a new result — they are visible in the source segments once one looks for them. The appendix segment would do the assembly work and make the composition citable.

My weak recommendation: promote as appendix segment. My strong recommendation: if not promoted, land R1 in `#disc-credit-assignment-boundary` Discussion and R3 reference in `#disc-identifiability-floor` — the corollary that "forgetting prerequisite is load-bearing for detection latency" belongs in `#schema-strategy-persistence` either way.


## 8. Working Notes (for potential future execution)

- **Sharpening R2.** The weakest step is §3.3's argument that $A_O^{(1)}$ and $V_O(\pi_{\mathrm{current}})$ share common-mode bias under model-class inadequacy. A clean version would model the bias as a function of `#result-mismatch-decomposition`'s model-error vs. observation-noise decomposition, show that common-mode bias is $O(1)$ (not $O(\varepsilon)$) when the model class is inadequate in a specific direction, and derive the convention-dependent detection latency. This is probably a one-evening spike.

- **R1 sharpening.** The expected log-odds update magnitude $\mathbb{E}\lvert \Delta\lambda_k \rvert$ can be made tighter under specific regime-change forms. For independent edge drift (R1 local to one edge), the bound should be tight. For correlated drift across multiple edges, the Jacobian coupling in `#disc-credit-assignment-boundary`'s gradient form distributes the signal; this could either tighten or loosen the bound depending on the drift's alignment with $\mathbf{J}$. Worth a careful treatment.

- **Connection to empirical detection rates.** Hafez et al. (2026) observed 89% vs. 44% detection accuracy for IDT vs. reward-based monitoring. The myopia theorem predicts the reward-based gap grows with accumulated experience; the IDT's structural-information-theoretic test should not. A direct simulation over varied agent-experience levels could test this prediction.

- **Extension to purposeful DAGs beyond Beta-Bernoulli.** The $1/(n+1)$ scaling is specific to Beta-Bernoulli. For Gaussian edges (continuous credence), the scaling is $1/(n+c)$ with analogous behavior. For exponential-family edges in natural-parameter form, the scaling follows the sufficient-statistic accumulation. The theorem's *qualitative* form (detection time monotone in accumulated sufficient statistic) is more general than Beta-Bernoulli; the *quantitative* $1/(n+1)$ is specific.

- **Does the myopia theorem have a Section III analog?** In composite agents, do larger teams/organizations face longer detection latency for regime change via analogous accumulation? This probably reduces to: for a team with $N$ members at varying individual operating points, the team's effective detection latency is at least $\min$-bounded by the slowest member's OP (or more precisely, by the OP of the member whose edge update is most load-bearing for the team decision). Connects to `#der-team-persistence` and the "weak dimension is the bottleneck" result of `#result-per-dimension-persistence`.

- **Does this change under Class 2 architectures?** For fully-merged agents (LLMs), the edge-update structure is absorbed into the single merged computation; there is no literal Beta-Bernoulli accumulator. But there is an analogous accumulator — the token statistics during pretraining. Do LLMs exhibit an analog of the myopia theorem? This is in the domain of `03-logogenic-agents/` and may be already partially addressed under the frozen-weights / context-turnover framing.

- **Naming alternative.** "Stability-induced myopia" captures the phenomenon but emphasizes the symptom. "Detection latency at high operating point" captures the mechanism. "Operating-point detection floor" positions it within `#disc-identifiability-floor`'s nomenclature. The right name depends on where the segment lands; my current preference is `#stability-detection-latency` if it stands alone, or absorbing it as `#disc-identifiability-floor` Instance 3 under the name "On-Policy Regime-Change Detection Under Accumulated Experience."
