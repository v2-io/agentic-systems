# Spike: Finding 1 Repair — Covariance-Primary Restructuring of `#causal-insufficiency-detection`

**Status:** Spike (proposed segment revision). Promotion-ready replacement for `01-aad-core/src/causal-insufficiency-detection.md` addressing Finding 1 of `msc/pending-findings-2026-04-22.md` (L0 residual fails as on-policy detection signal).

**Date:** 2026-04-22

**Trigger:** Three independent audits (Gemini pre-audit, Opus F1, Codex r2) flagged that under rational pure-on-policy execution, the segment's $\pm\rho$ residual mechanism collapses to zero. The segment loads its detection principle on this signal; under its own rationality assumptions about the agent, the principle is silent.

**Confirmation of finding's premise.** The counterargument in `pending-findings-2026-04-22.md` lines 62–74 is correct as stated. Two independent checks:

1. **Algebraic.** For an OR-gated pair $(A_1, A_2)$ executed with sequential short-circuit, the agent's empirical estimate of the success rate of $A_2$ converges to $\hat p_2 \to P(A_2 \mid \neg A_1)$ — the conditional under the short-circuit regime, not the marginal $\theta_2$. Plugging conditionals into the L0 OR formula:
   $$\hat P_\Sigma = 1 - (1 - \hat p_1)(1 - \hat p_2) \to 1 - P(\neg A_1)\,P(\neg A_2 \mid \neg A_1) = 1 - P(\neg A_1, \neg A_2) = P(A_1 \cup A_2)$$
   This is exactly $\bar y_G$ under the executed policy. Residual $\to 0$.
2. **Worked-example consistency.** `#worked-example-L1` line 34 sets $\theta_1 = \theta_C \cdot \theta_{1\mid C} = 0.72$ — i.e., the *marginal* success probability of path 1, computed across all environment states. The example tacitly assumes the agent learns marginals. This is consistent with off-policy / forced-sampling estimation; under on-policy short-circuit it is not what the agent would learn.

The finding is real. The covariance test in §"Interventional Localization" is the durable mechanism; the $\pm\rho$ residual is the off-policy / marginal-sampling limit and should be gated explicitly on that scope.

---

## Choices Made

Three substantive choices in the revision below; documented here so Joseph can adjust before applying.

### (a) Ordering: covariance test first, residual second

The repair direction in `pending-findings-2026-04-22.md` is unambiguous on this — Part B says elevate the covariance test to the **primary** detection mechanism. I have followed that direction:

- **§"Interventional Localization" → renamed §"Detection Principle: Pairwise Sibling Covariance Under Intervention"** and moved to the front. This is now *the* L0-insufficiency detector. It load-bears on `#loop-interventional-access` (which AAD has by construction for actuated agents) and on the agent's exploration mechanism (SA3) generating off-policy samples for sibling pairs — both of which are already established machinery, not novel scope conditions.
- **The $\pm\rho$ residual → renamed §"Secondary Signal: Plan-Level Residual Under Off-Policy Sampling"** and moved after the covariance section. It is presented as a confirmatory/aggregate signal valid only when the agent has a material off-policy component, with the regime gating made explicit.
- **§"From Detection to L1 Construction"** stays in roughly the same form — the construction step is downstream of either detection mechanism, so it doesn't need restructuring. Minor edit to make "given a positive covariance signal" the primary trigger.
- **§"Diagnostic CIY"** stays as Discussion-grade.

This ordering also matches the downstream truth: `#orient-cascade` step 4c, `#independence-audit` (item 2), and `#strategy-dag` line 124 *all already* point to the covariance test as the diagnostic. The current segment was the outlier in leading with the residual.

### (b) Treatment of the $\varepsilon \cdot \rho$ scaling

Worked through the algebra (see "Confirmation" §1 above and the derivation sketch below). The honest result:

- For a two-edge OR with conditional vs marginal learning interpolated by $\varepsilon$ (mixture of on-policy and off-policy samples), the L0 residual is exactly:
  $$\Phi^{L0}(\hat p) - \bar y_G = \varepsilon R_1 - \varepsilon^2 R_2, \quad\text{where } R_1 - R_2 = \rho$$
  with $R_1 = (1-p_1^c)(\theta_2 - p_2^c) + (1-p_2^c)(\theta_1 - p_1^c)$, $R_2 = (\theta_1 - p_1^c)(\theta_2 - p_2^c)$, and $p_j^c$ the conditional credence under the short-circuit regime.
- The leading-order coefficient $R_1$ is *not* exactly $\rho$ — it is a structure-dependent positive constant of the same sign as $\rho$. Only at $\varepsilon = 1$ does the residual recover $\rho$ exactly.
- The widely-quoted "$\varepsilon \cdot \rho$" scaling from `pending-findings-2026-04-22.md` line 89 is therefore correct as an order-of-magnitude / qualitative statement, but the exact first-order coefficient has structure dependence.

**Tagging decision.** I have used:

- *[Derived]* for the boundary cases (residual $\to 0$ on-policy; residual $\to \pm\rho$ off-policy with marginal sampling) — these close cleanly.
- *[Heuristic]* for the linear-in-$\varepsilon$ scaling. The qualitative form is robust ($O(\varepsilon)$ leading, sign $= \operatorname{sign}(\rho)$), but the coefficient is not universally $\rho$ — so labeling it as *[Derived]* would overstate. Labeling it as *[Hypothesis]* would understate, since the bound is structurally provable. *[Heuristic]* is the honest middle category for "useful approximation; quantitative form may not hold."
- An explicit Working Note flags that a tighter coefficient bound (e.g., $|R_1| \leq C \cdot \rho$ with $C$ depending on conditional/marginal gap) is a derivable open item if anyone wants to close it.

If Joseph prefers, the *[Heuristic]* call could be tightened to *[Derived (Conditional on two-OR topology with binary edges)]* with the exact $R_1, R_2$ formulas given. I left it heuristic to avoid load-bearing on a topology-specific derivation in the Detection Principle.

### (c) What stayed and what moved

**Stayed (substantively unchanged):**
- §"From Detection to L1 Construction" (one minor reframe: trigger is now positive covariance, not residual)
- §"Diagnostic CIY" (Discussion-grade; explore/exploit/diagnose three-way framing intact)
- §"What Cannot Be Detected" (unchanged — applies to either detection mechanism)
- §"Discussion" (connection-to-orient-cascade and domain-instantiations bullet list)

**Moved to primary position:**
- The covariance test (was §"Interventional Localization", second position; now §"Primary Detection Mechanism", first position)

**Moved to secondary position with explicit scope gating:**
- The $\pm\rho$ residual (was §"The Detection Principle", first position; now §"Secondary Signal: Plan-Level Residual Under Off-Policy Sampling")

**Removed:**
- The original §"Detection Principle" framing language asserting the residual as a universal detection criterion.
- The original §"Preconditions" list (now restructured: stationarity and update-bias preconditions move into the secondary signal's scope conditions; marginal-convergence becomes a covariance-test precondition).

**Added:**
- Explicit on-policy / off-policy regime distinction in the secondary signal section.
- Heuristic-tagged $\varepsilon$-mixed scaling formula.
- Updated Epistemic Status paragraph reflecting the restructured load-bearing.
- Working Note documenting the open coefficient-bound item.

**Frontmatter changes:**
- `status: conditional` → unchanged (still conditional; the conditions are now better named).
- `depends:` unchanged. Existing dependencies (`structural-adaptation-necessity`, `strategy-dag`, `loop-interventional-access`, `causal-information-yield`) all still load — `loop-interventional-access` becomes the *primary* dependency rather than a secondary one.
- `stage: draft` unchanged. (The segment was at `draft` per the OUTLINE table; the rewrite leaves it at `draft` for re-review.)

---

## Proposed Revised Segment

The full text of the proposed `01-aad-core/src/causal-insufficiency-detection.md` follows. Apply by replacing the entire segment.

```markdown
---
slug: causal-insufficiency-detection
type: derived
status: conditional
depends:
  - structural-adaptation-necessity
  - strategy-dag
  - loop-interventional-access
  - causal-information-yield
stage: draft
---

# Derived: Causal Insufficiency Detection

An agent operating at L0 of the Correlation Hierarchy ( #strategy-dag) can detect that its strategy DAG is causally insufficient — that latent common causes exist — by testing for pairwise covariance among sibling edges using the interventional data the feedback loop generates. A secondary aggregate signal (the L0 plan-level residual) is available when the agent samples off-policy, but vanishes under purely greedy execution. This is #structural-adaptation-necessity applied to the strategy layer, with the independence model as the model class and pairwise covariance as the primary diagnostic.

## Formal Expression

### Primary Detection Mechanism: Pairwise Sibling Covariance Under Intervention

*[Derived (from loop-interventional-access + independence test, conditional on SA3 exploration + joint observability)]*

Under L0 (the independence model in #strategy-dag's Correlation Hierarchy), sibling outcomes under a common parent are uncorrelated:

$$H_0:\;\operatorname{Cov}(Y_{A_i}, Y_{A_j}) = 0 \quad \forall\; i \neq j \;\text{siblings under the same parent}$$

Under causal insufficiency (a latent common cause $C$ acting on multiple siblings), sibling outcomes are positively correlated:

$$H_1:\;\exists\; i \neq j \;\text{with}\; \operatorname{Cov}(Y_{A_i}, Y_{A_j}) \gt 0$$

The agent generates test data through the standard exploration mechanism (SA3 — $\varepsilon$-greedy or similar). On trials where both siblings are observable — the agent tries one and can also observe the other's outcome, or tries them in rapid succession before the environment state changes — it accumulates the empirical covariance:

$$\hat\rho_{ij} = \frac{1}{N}\sum_t (Y_{A_i,t} - \bar{Y}_{A_i})(Y_{A_j,t} - \bar{Y}_{A_j})$$

A significantly positive $\hat\rho_{ij}$ rejects the L0 independence hypothesis and localizes the latent common cause: $A_i$ and $A_j$ share a dependency not represented in the DAG.

The feedback loop ( #loop-interventional-access) is what makes this possible: the agent's actions are genuine interventions, so the $(A_i, Y_i)$ pairs are interventional data. The covariance test is a causal independence test conducted on interventional data — it detects common causes that would be confounded in purely observational data.

**Why this is the primary mechanism.** The covariance test does not require any particular execution policy beyond the joint-observability condition that the agent occasionally generates samples of $(Y_{A_i}, Y_{A_j})$ pairs not censored by short-circuit evaluation. Standard exploration (SA3, already required by #strategic-dynamics-derivation Prop B.4 for OR-node calibration) supplies these samples. The test runs on data the agent collects anyway and detects the structural property directly rather than indirectly through aggregate residuals.

**Detection criterion.** A statistically significant positive $\hat\rho_{ij}$ at sample size $N$ sufficient for the desired test power, after per-edge credences have stabilized:

$$\hat\rho_{ij} \gt z_{1-\alpha}\,\hat\sigma_{\rho_{ij}} / \sqrt{N} \quad\implies\quad \text{DAG is causally insufficient between siblings } i, j$$

(Standard hypothesis-testing form; threshold and test power depend on application.)

**Preconditions for the covariance test.**

1. **Joint observability.** The agent can occasionally observe $(Y_{A_i}, Y_{A_j})$ pairs in the same environment state. Pure short-circuit execution censors one of each pair; SA3 exploration or simultaneous-attempt regimes provide uncensored pairs.
2. **Per-edge credence stabilization.** Edge credences $\hat p_i, \hat p_j$ have stopped drifting at the timescale of the covariance accumulation, so $\bar Y_{A_i}, \bar Y_{A_j}$ are well-defined empirical means.
3. **Approximate stationarity over the test window.** The latent common cause's frequency and the conditional success rates are not drifting faster than the test's accumulation timescale. Under faster nonstationarity, $\hat\rho_{ij}$ may reflect tracking artifacts rather than structural insufficiency.

When these preconditions hold, $\hat\rho_{ij} \gt 0$ is diagnostic of a missing common cause acting on $(A_i, A_j)$. When they do not, the signal is ambiguous.

### Secondary Signal: Plan-Level Residual Under Off-Policy Sampling

*[Derived (Conditional on off-policy / marginal-sampling regime)]*

A second diagnostic uses the aggregate plan-level residual, but it is *only* available when the agent samples off-policy. The residual's magnitude scales with the off-policy fraction; under purely greedy on-policy execution it vanishes identically.

**Marginal-sampling limit (off-policy bound).** When the agent samples each edge's outcome unconditioned by execution context — i.e., the empirical credence $\hat p_k$ converges to the true marginal $\theta_k$ rather than to a conditional under the short-circuit regime — the L0 plan-confidence value at convergence equals $\Phi^{L0}(\boldsymbol\theta)$, the AND/OR formula at true marginals. This differs from actual plan success $\bar y_G$ by the latent covariance:

$$\Phi^{L0}(\boldsymbol\theta) - \bar{y}_G \;\longrightarrow\; \begin{cases} +\rho & \text{OR-heavy strategies (overestimation)} \\ -\rho & \text{AND-heavy strategies (underestimation)} \end{cases}$$

where $\rho$ aggregates the latent covariance structure. The $+\rho$ direction for OR siblings reflects illusory redundancy (independence overestimates coverage); the $-\rho$ direction for AND siblings reflects unrecognized synergy (independence underestimates joint success).

**On-policy collapse (greedy limit).** Under rational pure on-policy execution with sequential short-circuit evaluation:

- **OR node** ($A_1 \lor A_2$): if $A_1$ succeeds, $A_2$ is never executed. Empirical $\hat p_2 \to P(A_2 \mid \neg A_1)$, the conditional under the short-circuit regime — not the marginal $\theta_2$.
- **AND node** ($A_1 \land A_2$): if $A_1$ fails, $A_2$ is never executed. Empirical $\hat p_2 \to P(A_2 \mid A_1)$.

Plugging conditionally-learned credences into the naive L0 arithmetic recovers the exact true joint:

- OR L0: $\hat P_\Sigma = 1 - (1-\hat p_1)(1-\hat p_2) \to 1 - P(\neg A_1)\,P(\neg A_2 \mid \neg A_1) = 1 - P(\neg A_1, \neg A_2)$.
- AND L0: $\hat P_\Sigma = \hat p_1 \cdot \hat p_2 \to P(A_1)\,P(A_2 \mid A_1)$.

Therefore $\Phi^{L0}(\hat{\boldsymbol p}) - \bar y_G \to 0$ under pure on-policy execution. *The aggregate residual is identically zero for a purely greedy agent regardless of how much latent covariance the environment carries.* The agent cannot detect causal insufficiency from this signal alone.

**Mixed-regime scaling.** *[Heuristic]* For an agent executing mostly on-policy with a small off-policy fraction $\varepsilon$ (e.g., $\varepsilon$-greedy exploration), the empirical credence is a mixture:

$$\hat p_j = (1-\varepsilon)\,p_j^{\text{cond}} + \varepsilon\,\theta_j$$

where $p_j^{\text{cond}}$ is the conditional under the short-circuit regime. The residual at convergence scales linearly in $\varepsilon$ to leading order, with the same sign as the marginal-limit $\pm\rho$:

$$\Phi^{L0}(\hat{\boldsymbol p}) - \bar y_G = \varepsilon \cdot R + O(\varepsilon^2), \quad \operatorname{sign}(R) = \operatorname{sign}(\rho)$$

where $R$ is a structure-dependent coefficient that recovers the marginal-limit $\rho$ at $\varepsilon = 1$ but is not in general equal to $\rho$ at intermediate $\varepsilon$. The widely-quoted "$\varepsilon \cdot \rho$" scaling is correct as an order-of-magnitude statement; the exact coefficient depends on the gap between conditional and marginal credences.

**When the secondary signal is usable.** The plan-level residual is a useful confirmatory diagnostic when:

1. **Material off-policy fraction.** The agent has $\varepsilon$ large enough that $\varepsilon \cdot R$ exceeds the noise floor of empirical residual estimation. Purely greedy agents cannot use this signal.
2. **Marginal convergence.** Per-edge credences have actually stabilized at their (conditional or mixed) limits.
3. **Approximate stationarity.** True edge probabilities are not drifting faster than the agent's update rate.
4. **No systematic update bias** (e.g., the marginal Bayesian update for unobservable intermediates has $O(1/n)$ downward bias — see #strategic-dynamics-derivation, Prop B.3).

When all four hold and the residual is statistically significantly nonzero, its sign confirms the bias direction (OR overestimation vs AND underestimation) identified by the primary covariance test. The two diagnostics are complementary: covariance localizes *where* the missing common cause is; the residual sign characterizes the *aggregate bias direction* across the DAG.

This is #structural-adaptation-necessity's diagnostic criterion ("persistent irreducible mismatch after parametric convergence is diagnostic of model class inadequacy") instantiated for the strategy layer, with the independence model as the model class and the off-policy-regime $\rho$ as the irreducible mismatch — under the explicit scope condition that the agent samples off-policy enough to see it.

### From Detection to L1 Construction

*[Derived (from positive covariance signal + L1 construction principle in #strategy-dag)]*

Once the agent detects $\hat\rho_{ij} \gt 0$ between siblings $A_i$ and $A_j$, it knows a latent common cause exists but not its identity. The construction process:

1. **Hypothesize** a common-cause node $C$ that explains the correlation.
2. **Estimate** $\theta_C$ from the pattern of joint outcomes. The joint failure rate $P(A_i\text{ fails}, A_j\text{ fails})$ exceeds $(1-\theta_i)(1-\theta_j)$ by $\hat\rho_{ij}$; the excess localizes the common cause's frequency.
3. **Restructure** the DAG: factor $C$ above the correlated siblings ( #strategy-dag, L1 construction principle: factor the common cause above the correlation it creates).
4. **Re-estimate** conditional edge credences $\theta_{k|C}$ from the data, conditioned on the inferred $C$ state.

This is structural adaptation ( #structural-adaptation-necessity) at the strategy level: the agent changes its model class from L0 to L1, adding representational capacity for a pattern the L0 model cannot express. The cost is the standard cost of structural change: temporary performance degradation while the new credences converge, and increased graph complexity. (Soft-facilitator common causes require L1' rather than L1 — see #strategy-dag and #worked-example-L1 for the strict-prerequisite vs soft-facilitator distinction.)

### Diagnostic CIY

*[Discussion (diagnostic-ciy)]*

Which actions are most informative for detecting latent common causes? An action that tests multiple potentially-correlated edges simultaneously has high causal information yield for the independence hypothesis ( #causal-information-yield). The explore-exploit tradeoff extends with a third axis:

- **Exploit**: pursue the current best plan
- **Explore**: test unknown edges for their individual success rates
- **Diagnose**: test known edges for their joint correlation structure

Diagnosis is a form of internal exploration — the agent probes its own model's structural assumptions rather than learning new parameter values. A chess engine exploring futures is deliberation about state; an agent testing whether two alternatives share a common failure mode is deliberation about model structure. The information value of diagnostic actions is highest when:

- Edge credences have converged (the agent knows the marginals or conditionals but not the joint structure)
- Joint outcomes for sibling pairs are observable in the same environment state (the covariance test has data)
- The agent has sufficient off-policy budget that the secondary residual signal is also visible (corroborating diagnostic)

## Epistemic Status

*Conditional on strategy-layer instantiation of structural-adaptation-necessity.* The **primary detection mechanism** (pairwise sibling covariance) is *robust qualitative*: the test logic is standard hypothesis testing applied to interventional data from the feedback loop, and its preconditions (joint observability, per-edge stabilization, approximate stationarity) are explicit. Its sensitivity depends on how cleanly the agent can separate sibling-covariance signal from edge-credence noise at convergence; in adversarial or fast-drifting environments the test's effective sample size shrinks.

The **secondary signal** (L0 plan-level residual) is *conditional on off-policy sampling*: under pure on-policy execution it is identically zero (rational short-circuit produces conditional credences whose L0 arithmetic recovers the true joint), and its mixed-regime scaling is $O(\varepsilon)$ with structure-dependent coefficient. The bias-sign formula ($+\rho$ for OR-heavy, $-\rho$ for AND-heavy) is exact in the marginal-sampling limit; the linear-in-$\varepsilon$ scaling is *heuristic*. The signal is useful as a confirmatory diagnostic when the agent has substantial off-policy exploration; it is unavailable to a purely greedy agent.

The **detection-to-construction pipeline** is *discussion-grade*: the trigger is now the (statistically rigorous) covariance signal, but the specific procedures for estimating $\theta_C$ and $\theta_{k|C}$ from correlated outcome data are domain engineering. The **diagnostic CIY** discussion is ungrounded — it identifies the right question (which actions are most informative for structural detection) but does not derive the answer.

### What Cannot Be Detected

Interventions cannot detect common causes that:

- **Affect only one edge**: idiosyncratic factors are not common causes. They appear as noise in individual edge credences.
- **Are too rare to produce observable joint failures**: a common cause with $\theta_C \approx 1$ (almost always active) rarely reveals itself. The agent needs enough failure events to estimate the covariance.
- **Correlate edges that are never jointly observable**: if the agent can never observe both $A_i$ and $A_j$ in the same environment state (mutually exclusive with long horizons), the joint outcome data is unavailable.
- **Introduce negative correlation**: the formulation assumes positive correlation from shared enabling factors. Negative correlation (competing for a shared resource) requires a different model and produces the opposite bias pattern.

These limitations parallel the information-theoretic underdetermination in #credit-assignment-boundary: detection requires data, and the data must have the right structure.

## Discussion

**The detection-construction cycle.** The full cycle — L0 operation → detect positive sibling covariance → localize common cause → construct L1 → re-converge — is a concrete instance of the structural adaptation cycle described in #structural-adaptation-necessity. The agent starts with a simpler model class (L0), runs a structural test on data its exploration generates anyway, then transitions to a richer model class (L1) at the cost of temporary uncertainty. The covariance signal makes the detection criterion quantitative rather than qualitative: the agent has a hypothesis-test threshold rather than a vague "model feels wrong" signal.

**Why the primary signal is structural, not aggregate.** A rational agent executing a short-circuit AND/OR plan censors its own training data: edges downstream of failed prerequisites are never tested; OR-alternatives downstream of successes are never tried. Empirical credences therefore converge to *conditionals under the short-circuit regime*, not marginals. Naive L0 arithmetic with conditional inputs is the chain rule of probability — it recovers the true joint under the executed policy. So a purely greedy agent's plan-level residual is structurally zero; it is well-calibrated *to the world it actually samples*, even when its DAG omits common causes. Detecting causal insufficiency requires a signal that survives the censoring — and that is precisely what pairwise sibling covariance under exploration provides: a structural test on uncensored joint data, not an aggregate average over censored marginals.

**Connection to the orient cascade.** The detection signal enters the orient cascade ( #orient-cascade) at step 4c (causal-sufficiency check). The cascade's text already names "pairwise sibling covariance under an augmented test" as the diagnostic mechanism; this segment is its formal home. Step 4c's response is structural revision of $\Sigma_t$ (adding the common-cause node), routed through step 5b's $\Pi$-expansion as the L1 augmentation.

**Domain instantiations.** The detection mechanism applies concretely in:
- **Software deployment**: two services sharing infrastructure fail together more often than independent failure rates predict → add infrastructure-health node
- **Military operations**: two concurrent operations fail together under adverse weather → add weather-condition node
- **Investment**: two positions lose value together during market stress → add market-regime node
- **Organizational strategy**: two initiatives stall together during leadership transitions → add organizational-stability node

In each, what makes the detection feasible is the agent's ability to occasionally observe *both* sibling outcomes — running both services through the same incident, attempting both operations in the same weather window, holding both positions through the same market event, attempting both initiatives during the same leadership transition. Pure short-circuit ("only run service B if A is down") suppresses the joint-observation events the test relies on; some routine joint exposure is necessary.

## Working Notes

- The mixed-regime scaling formula $\Phi^{L0}(\hat{\boldsymbol p}) - \bar y_G = \varepsilon R + O(\varepsilon^2)$ is currently *[Heuristic]* — the qualitative form is robust but the coefficient $R$ is structure-dependent. A tighter result would bound $|R|$ in terms of $\rho$ and the gap between conditional and marginal credences. For the two-OR case, $R = (1-p_1^c)(\theta_2 - p_2^c) + (1-p_2^c)(\theta_1 - p_1^c)$ explicitly and $\rho = R - (\theta_1 - p_1^c)(\theta_2 - p_2^c)$ at $\varepsilon = 1$. Generalizing to $k$-sibling OR and to AND-heavy topologies is straightforward but tedious; if the secondary signal becomes load-bearing for any downstream result, this is the work to do. Currently no downstream segment loads on the *quantitative* form, only on the qualitative ("aggregate residual exists, sign matches dominant node type") — so the heuristic tag is honest and not blocking.
- The covariance test's effective sample size depends on the off-policy fraction $\varepsilon$ (which controls how often joint observations occur) and the latent common cause's prevalence $\theta_C$ (which controls how often joint failures actually occur). In the worst case (high $\theta_C$, common cause almost always active so failures are rare), the test is power-limited. A more sophisticated diagnostic might condition on environment-state proxies to focus the test on regimes where the common cause varies — but this presumes structure the L0 agent doesn't have. Moving from L0 to L1 is the proper response; refining the test within L0 is unlikely to pay off.
- This segment now leans entirely on `#loop-interventional-access` for the primary signal (was leaning equally on it before the rewrite, but the residual signal masked that dependency). If `#loop-interventional-access`'s scope is later qualified (e.g., by Finding 5 / O-BP6's regime-indexed treatment of "interventional" data), the covariance test inherits the same regime-conditional reading. Worth a re-check pass on this segment after any rewrite of `#loop-interventional-access`.
```

---

## Downstream Impact Check

Search results from the repo for `#causal-insufficiency-detection` and the $\pm\rho$ / "L0 residual" formulas. Each hit classified as: still holds / minor edit needed / substantive rework needed.

### `#causal-insufficiency-detection` references

| File | Line | Reference | Status |
|------|------|-----------|--------|
| `01-aad-core/OUTLINE.md` | 95 | One-line description: "Detecting latent common causes from structured residuals + interventional localization" | **Minor edit.** "structured residuals + interventional localization" inverts the new ordering. Suggested: "Detecting latent common causes via pairwise sibling covariance under intervention; secondary plan-level residual signal under off-policy sampling." |
| `01-aad-core/src/orient-cascade.md` | 16, 48, 85 | Step 4c diagnostic: "pairwise sibling covariance under an augmented test ( #causal-insufficiency-detection)" | **Still holds.** The reference is exactly to the surviving (and now primary) covariance test. Confirmed during pre-spike review per the finding's own note (line 122). No edit needed. |
| `01-aad-core/src/strategy-dag.md` | 124 | "An agent at L0 can detect causal insufficiency from its own data: persistent overestimation of plan success after edge credences have converged is the signal" — then describes the covariance test | **Minor edit needed.** The opening clause ("persistent overestimation … is the signal") is the now-demoted secondary signal, presented as the primary signal. The follow-on text correctly describes the covariance test as the localization mechanism, but the framing reverses the new ordering. Suggested rewrite: "An agent at L0 can detect causal insufficiency from its own data: pairwise covariance among sibling edges, computed on interventional data the feedback loop generates, rejects the independence hypothesis and identifies where to add L1 nodes. A secondary aggregate signal — persistent overestimation of plan success after edge credences have converged, available when the agent samples off-policy — corroborates the bias direction." 5 min. |
| `01-aad-core/src/independence-audit.md` | 45 | Item 2 diagnostic signal: "Pairwise covariance among sibling edges after edge credences have converged. Positive covariance rejects the independence hypothesis and localizes where a common cause is missing. See #causal-insufficiency-detection." | **Still holds.** Already references the surviving (and now primary) mechanism. No edit needed. |
| `01-aad-core/src/approximation-tiering.md` | 34 | Diagnostic for correlation tier: "Sibling-edge covariance after credence convergence ( #causal-insufficiency-detection)" | **Still holds.** Already references the surviving mechanism. No edit needed. |
| `01-aad-core/src/worked-example-L1.md` | 141 | "the L0 residual $\Phi^{L0} - \bar y_G$ converges to $+\rho$ (our example: $0.877 - 0.776 = 0.101$), providing a precise, quantitative detection signal. The agent does not need to know the common cause exists *a priori* — it discovers the need for L1 from persistent structured residuals after convergence." | **Substantive edit needed.** This passage is the most affected downstream reference. The numeric calculation (0.877 - 0.776 = 0.101) is correct *in the marginal-sampling limit* — and the worked example *implicitly assumes that limit* by using $\theta_1 = \theta_C \cdot \theta_{1|C} = 0.72$ as the agent's learned credence (the marginal). Suggested rewrite: lead with the covariance signal as the primary detection, retain the residual computation as the off-policy / marginal-sampling demonstration, and add an explicit scope note that the example assumes the agent samples both paths regardless of execution context (i.e., off-policy or simultaneous-attempt regime). The numbers stand; the framing needs to acknowledge the regime. 15–20 min. |
| `msc/analysis-2026-04-06.md` | 308, 309, 314, 536 | Historical analysis-grade text discussing the residual diagnostic | **Historical artifact.** msc/ analysis document; no edit needed. The newer pending-findings doc supersedes it. |

### `±ρ residual` / "L0 residual" prose mentions outside the segment

| File | Line | Context | Status |
|------|------|---------|--------|
| `01-aad-core/src/causal-insufficiency-detection.md` | 23, 25, 29, 41, 91 | The segment itself | Replaced by this spike. |
| `01-aad-core/src/worked-example-L1.md` | 141, 146 | Numeric instantiation + Epistemic Status note ("The direction-of-bias formula ($\pm\rho$) is exact for two binary siblings") | Line 141: see worked-example-L1 row above. Line 146: **still holds** — the $\pm\rho$ formula *is* exact for two binary siblings *in the marginal-sampling limit*, and the segment's Epistemic Status is honest about the conditioning. May warrant a one-clause addition: "exact for two binary siblings *under marginal sampling*." 2 min. |
| `TODO.md` | 55 | Findings index entry | **Will update on completion** of finding repair. |
| `msc/pending-findings-2026-04-22.md` | various | Finding 1's own description | The finding doc itself; no edit needed. |

### Frontmatter / dependency graph

`causal-insufficiency-detection` `depends:` list (`structural-adaptation-necessity`, `strategy-dag`, `loop-interventional-access`, `causal-information-yield`) is unchanged. The dependency on `loop-interventional-access` becomes more load-bearing (it now supplies the primary mechanism's interventional-data condition rather than the secondary's), but it was already listed.

`orient-cascade` `depends:` includes `causal-insufficiency-detection`. After the rewrite, `orient-cascade`'s step 4c claim ("pairwise sibling covariance under an augmented test") is *strengthened* by the rewrite (covariance is now the primary mechanism, matching the cascade's existing language) rather than weakened. No `depends:` change needed; no `orient-cascade` claim degradation. Step 4c's `robust-qualitative` Epistemic Status remains accurate.

### Net downstream cost

- **Zero edits required:** `orient-cascade.md`, `independence-audit.md`, `approximation-tiering.md`. These were already pointing to the surviving mechanism.
- **Minor edits (2–5 min each):** `OUTLINE.md` line 95 description; `strategy-dag.md` line 124 framing; `worked-example-L1.md` line 146 Epistemic Status clause.
- **Substantive but contained edit (15–20 min):** `worked-example-L1.md` line 141 framing — needs scope note clarifying the marginal-sampling regime the example tacitly assumes.

Total downstream cost is roughly 30–40 minutes of follow-on editing after applying the segment rewrite. None of the downstream edits change theoretical commitments; all are framing alignment.

---

## Open Questions for Joseph

1. **Structure-dependent coefficient $R$ — derive or leave heuristic?** The mixed-regime scaling $\Phi^{L0}(\hat{\boldsymbol p}) - \bar y_G = \varepsilon R + O(\varepsilon^2)$ has $R$ structurally derivable for any specific topology (the two-OR case is given explicitly in the Working Note). The honest blanket statement is "$R$ has the same sign as $\rho$ and recovers $\rho$ at $\varepsilon = 1$." Three options:
   - (a) Leave as *[Heuristic]* with the derivable-but-tedious open item flagged. *(Current spike choice.)*
   - (b) Tighten to *[Derived (Conditional on two-OR topology with binary edges)]* with the exact $R_1, R_2$ formulas in the Formal Expression. Honest but topology-locked.
   - (c) Prove a bound $|R| \leq c(\theta, p^c) \cdot \rho$ for a class of topologies (e.g., "all monotone OR-heavy DAGs with positive common-cause prevalence") and tag *[Derived]*. Probably one or two pages of algebra; doable but not done.
   The primary-mechanism reframe is independent of this choice — option (a) is sufficient for the segment to load-bear correctly; (b) and (c) are polish.

2. **Worked-example-L1 framing.** The example's setup uses marginals as learned credences, which is consistent with the segment's pre-rewrite framing but tacitly assumes off-policy / simultaneous-attempt sampling. Two ways to handle:
   - (a) Add a one-paragraph scope note to `worked-example-L1.md` clarifying the regime: "The example assumes the agent observes both path outcomes per trial, e.g., under simultaneous-attempt or off-policy exploration; under sequential short-circuit the agent's empirical credences would converge to conditionals and the residual would vanish — see #causal-insufficiency-detection §'On-policy collapse'." Cleanest. *(Recommended.)*
   - (b) Rework the example to show *both* regimes side-by-side. More pedagogically thorough but adds significant length to a worked example whose primary purpose is the L1 *construction* demonstration, not the detection mechanism.
   I suggest (a); flagging here in case you have a stronger view.

3. **Compound with Finding 11?** Finding 11 (`pending-findings-2026-04-22.md` line 393) flags step-4c's convergence assumption in non-stationary environments and notes a joint repair with Finding 1 is cleaner than two independent fixes. The current spike repairs Finding 1 in isolation. After this rewrite, the orient-cascade step 4c's reference to the covariance test is preserved exactly, and the covariance test's preconditions (now explicit in this segment) include "approximate stationarity over the test window" — which already addresses Finding 11's concern at the level of preconditions in the right place. So I think this rewrite *substantially closes* Finding 11 without further work, but a sanity-check edit to `orient-cascade.md` step 4c might be warranted: explicitly note that 4c inherits the covariance test's stationarity precondition rather than requiring a separate convergence assumption on $\delta_s$. 10 min if you want it; not strictly required. Worth a yes/no decision before applying the segment rewrite, to decide whether to package the orient-cascade tweak with this repair or leave it for a separate Finding 11 pass.

4. **`stage:` after rewrite — `draft` or revisit promotion track?** The segment was at `draft` per OUTLINE. The rewrite is substantial enough that re-running Gate 1 (deps audit) and Gate 2 (content review) from scratch is appropriate. I left `stage: draft` in the proposed frontmatter. If you want to immediately re-promote, that is a content-review judgment call after seeing the applied rewrite.

5. **Does the "worked-example-L1 Epistemic Status implies marginal-sampling" hold up?** I read line 146 ("The direction-of-bias formula ($\pm\rho$) is exact for two binary siblings") as honest under the marginal-sampling limit — but I want a second look from you to confirm I am not papering over a deeper inconsistency. The numerical $0.877 - 0.776 = 0.101$ is computed with marginals, so yes, it is the off-policy / marginal-sampling limit; the question is whether a future reader of `worked-example-L1` is at risk of inferring "this is what an on-policy L0 agent would observe" without the explicit scope note. I think yes, and that is why option 2(a) above is recommended — but flagging in case you read the Epistemic Status as already clear enough.

---

## Spike-segment compression check

Per `FORMAT.md` §"Spike-segment reverse check": does the proposed segment lose anything the spike establishes?

- **Confirmation of finding's premise:** captured in segment Working Notes via the working note explaining the on-policy collapse mechanism (the "Why the primary signal is structural, not aggregate" Discussion paragraph also captures this).
- **Coefficient bound for two-OR case:** captured in segment Working Notes verbatim from this spike's coefficient formulas.
- **Downstream-edit list:** lives in this spike, not the segment (correct — segment doesn't need to know).
- **Choices analysis (a)/(b)/(c) ordering / heuristic-tagging / what-stayed):** lives in this spike, not the segment (correct — segment is the result).

The compression direction is honest: the segment captures the load-bearing claims and scope conditions; the spike captures the audit context, alternative tagging choices, and downstream coordination work. Nothing the segment needs is lost.
