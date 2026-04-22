# Pending Findings — 2026-04-22

**Status:** Working note. One finding flagged during post-promotion review of `#causal-insufficiency-detection` (surfaced by Gemini). Scope-condition bug — the segment's detection mechanism is mathematically sound only under off-policy sampling but asserts it as a general principle.

**Origin:** Gemini review flagged 2026-04-22, after the day's Gate 2 promotion work.

---

## Finding — L0 residual detection mechanism fails under rational on-policy execution

### Problematic passage

`01-aad-core/src/causal-insufficiency-detection.md` §"The Detection Principle" (lines 21–43):

> After edge credences converge ($\hat p_k \approx \theta_k$, low gain), the plan-confidence error $\delta_s \approx 0$ — the agent is well-calibrated within the independence model. The agent also observes actual plan outcomes $y_G \in \{0, 1\}$. The **L0 residual** — the gap between the independence-model reference value and actual success — converges to:
> $$\Phi^{L0} - \bar{y}_G \longrightarrow \begin{cases} +\rho & \text{OR-heavy strategies (overestimation)} \\ -\rho & \text{AND-heavy strategies (underestimation)} \end{cases}$$
> ...
> **Detection criterion.** A persistently nonzero L0 residual after edge-credence convergence is a strong indicator of causal insufficiency.

### The counterargument

A rational agent executing an AND/OR strategy DAG uses sequential short-circuit evaluation, which systematically censors its own training data:

- **OR node** ($A_1 \lor A_2$): agent tries $A_1$. If $A_1$ succeeds, the goal is met and $A_2$ is not executed. $A_2$ is only executed when $A_1$ fails. Learned credence for $A_2$ therefore converges to the *conditional* $P(A_2 \mid \neg A_1)$, not the marginal $\theta_2$.
- **AND node** ($A_1 \land A_2$): agent tries $A_1$. If $A_1$ fails, the plan fails and $A_2$ is not executed. Learned credence for $A_2$ converges to $P(A_2 \mid A_1)$.

When the agent plugs conditionally-learned credences into the naive L0 independence formulas, the algebra exactly recovers the true joint:

- OR L0: $\hat P_\Sigma = 1 - (1 - \hat p_1)(1 - \hat p_2) \to 1 - P(\neg A_1)P(\neg A_2 \mid \neg A_1) = 1 - P(\neg A_1, \neg A_2) = P(A_1 \cup A_2)$.
- AND L0: $\hat P_\Sigma = \hat p_1 \cdot \hat p_2 \to P(A_1) P(A_2 \mid A_1) = P(A_1 \cap A_2)$.

In both cases, $\hat P_\Sigma$ converges to the *exact true joint* under the executed policy. Consequently $\Phi^{L0} - \bar{y}_G \to 0$, and the agent cannot detect causal insufficiency via this signal. The $\pm\rho$ bias appears only if the agent *irrationally* continues executing $A_2$ after the outcome is determined — i.e., only under off-policy sampling.

**Confidence in the counterargument:** high. The math is clean and the mechanism is structural. The segment's Detection Principle section asserts the $\pm\rho$ formula as if it held universally, but it requires the agent to be sampling marginals, which a rational agent executing its own strategy is not doing.

### Why this matters

The segment's entire Detection Principle section (its core formal claim) load-bears on the $\pm\rho$ residual as *the* diagnostic signal. Under the segment's own rationality assumptions about the agent, the residual is zero. The agent cannot use its on-policy experience to detect that its DAG is causally insufficient.

Downstream dependency check:

- `#orient-cascade` step 4c (just promoted to claims-verified 2026-04-22) references `#causal-insufficiency-detection` for the "causal-sufficiency check" diagnostic. Fortunately, the specific reference is to the **pairwise sibling covariance test** ($\hat\rho_{ij}$), which lives in the segment's §"Interventional Localization" and explicitly requires off-policy / interventional data. That half of the segment survives the finding. Orient-cascade's step 4c is therefore less affected than the causal-insufficiency-detection segment itself.
- No other segment currently references the $\pm\rho$ residual signal.

### Scope considerations

Two scope considerations temper but do not eliminate the problem:

1. **Exploration partially restores the signal.** Under $\varepsilon$-greedy or similar (which the segment's §"Interventional Localization" explicitly invokes via "SA3 — $\varepsilon$-greedy or similar"), the agent samples off-policy occasionally. Learned credences converge to an $\varepsilon$-weighted mixture of marginal and conditional, giving a residual of magnitude roughly $\varepsilon \cdot \rho$ rather than $\rho$. The detection threshold changes but the signal is not identically zero. The current segment's formula $\Phi^{L0} - \bar{y}_G \to \pm\rho$ is the off-policy-only limit, not the mixed-regime form.

2. **The covariance test is independently valid.** The segment's second half (Interventional Localization) uses pairwise sibling covariance $\hat\rho_{ij}$, which requires genuinely off-policy data by construction ("trials where both siblings are observable — the agent tries one and can also observe the other's outcome"). This test survives the finding. It detects the common cause through a different mechanism (joint distribution of outcomes under intervention) than the L0 residual (average discrepancy under policy).

The finding's substantive implication: the covariance test should be promoted to the *primary* detection mechanism, and the $\pm\rho$ residual demoted to a secondary signal valid only under substantial exploration, with the exploration rate appearing explicitly in the formula.

### Repair direction

Two-part revision to `#causal-insufficiency-detection`:

**Part A — Detection Principle section.** Replace the $\pm\rho$ limit with the mixed-regime form:

- State that under rational pure-on-policy execution, learned credences converge to conditionals (specifically $P(A_j \mid \text{short-circuit regime})$) not marginals.
- Note that naive L0 arithmetic with conditional inputs produces the correct joint, so $\Phi^{L0} - \bar{y}_G \to 0$ under pure on-policy.
- Under exploration with rate $\varepsilon$, derive (or at least estimate) the residual scaling as approximately $\varepsilon \cdot \rho$. Make the exploration dependence explicit.
- Reframe the section: the $\pm\rho$ residual is a signal when the agent has a material off-policy component; it is not available to a purely greedy agent.

**Part B — Elevate the covariance test.** Restructure the segment so §"Interventional Localization" is positioned as the primary detection mechanism, not as localization-after-detection:

- The covariance test doesn't need the residual signal as a trigger; it can run independently given off-policy data.
- The "detection → localization" pipeline becomes "covariance → structural repair," with the residual as an optional additional signal.

Both parts are scope-condition fixes rather than new derivations; the segment's underlying logic is sound, just asserted with too few conditions.

**Effort estimate:** 60–90 minutes. The existing text scaffolds the revision well — most of what needs to change is framing and adding scope conditions, not new math. The only non-trivial piece is deriving (or at least sketching) the $\varepsilon \cdot \rho$ scaling; if it doesn't close cleanly, labeling it as a hypothesis is acceptable.

### Why deferred

The segment's current claim is reviewer-flagged as structurally incorrect (not just imprecise), so a repair is warranted. Deferring briefly for Joseph's review of the severity assessment and of the recommended repair direction before executing the segment edit. Once the severity is confirmed, the fix itself is straightforward.

### Notes for the next agent

- The covariance test in the segment's §"Interventional Localization" is the durable half. When repairing, start from there and build the residual mechanism back in as a scope-conditional secondary signal.
- `#orient-cascade` step 4c currently references "pairwise sibling covariance under an augmented test" — this is correctly aligned with the surviving half of `#causal-insufficiency-detection`. That reference doesn't need changing.
- The bias sign formulas ($+\rho$ for OR-heavy, $-\rho$ for AND-heavy) are correct *if* the agent is sampling marginals. Keep them, but clearly gate them on the off-policy sampling assumption.
- `msc/spike-credit-assignment-boundaries.md` has related analysis of when on-policy data is sufficient. Worth consulting during the repair.
