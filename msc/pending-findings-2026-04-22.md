# Pending Findings — 2026-04-22

**Status:** Working note. Local findings (scope bugs, mechanical breaks, framing issues) from three de novo audits conducted on 2026-04-22 plus one earlier Gemini flag. Architectural proposals from the same audits — independent structural moves that advance the theory's beauty/concision/correctness/approachability/fundamentality — are documented separately in `msc/architectural-proposals-2026-04-22.md`.

**Resolution status (2026-04-22 strengthening cycle, commits `14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`):**

- **Finding 1 — RESOLVED.** No-go theorem strengthening; predecessor softening at `msc/spike-finding-1-l0-residual-repair.md`, strengthening at `msc/spike-finding-1-strengthening.md`, both in commit `14a6095`. The covariance test is now framed as the unique broadly-available violation of the no-go's scope, not a chosen primary; `#causal-insufficiency-detection` rewritten end-to-end.
- **Finding 3 — RESOLVED** (subsumed) by G-BP2 V-medium in commit `a14682e`. KL-form replaces Shannon-MI in `#strategy-complexity-cost`; degeneracy fixed by construction.
- **Finding 5 — PARTIALLY RESOLVED** by AI integration commit `a14682e`. `#loop-interventional-access` now distinguishes "data generated under intervention" from "cleanly identified do-estimates" via the three distinctive AAD moves and Bruineberg-blanket positioning. Full closure requires O-BP6 identity promotion.
- **Finding 7 — RESOLVED.** Per-quantity exactness audit + conditional maximality strengthening; predecessor at `msc/spike-finding-7-git-chronica-narrowing.md`, strengthening at `msc/spike-finding-7-strengthening.md`, both in commit `b6134c2`. $\mathcal{C}_t^{\text{commit}}$ added to NOTATION.md.
- **Finding 10 — RESOLVED.** Status reclassified discussion-grade → exact (applied external theorem). Spike at `msc/spike-finding-10-ib-status.md`; commit `a14682e`.
- **Finding 11 — PARTIALLY RESOLVED** by F1 strengthening. Step 4c is now reframed as the unique broadly-available diagnostic given the no-go (rather than as one diagnostic among several). Optional step-4c sanity edit in `#orient-cascade` itself remains as cleanup.
- **Finding 13 — RESOLVED.** Prop B.7 derived for L1' observable-$C$ + Cramér-Rao refutation for unobservable case. Predecessor softening at `msc/spike-finding-13-l1-default-narrowing.md`, strengthening at `msc/spike-finding-13-strengthening.md`, both in commit `4d050c8`. `#strategy-dag` headline + Correlation Hierarchy table updated; `#strategic-dynamics-derivation` open item #4 marked Resolved.

**Remaining open:** Findings 2 (partial — V-medium G-BP2 fixed Shannon-zero degeneracy in #strategy-complexity-cost; the unbounded-gradient pathology in #credit-assignment-boundary remains), 4, 6, 8, 9, 12, 14, 15. See `TODO.md` for current actionability and subsumption-by-architectural-proposal status.

**New meta-segment from this cycle:** `#discussion-identifiability-floor` collects the F1+F13 no-go pattern as an emerging structural commitment of the theory, with three open extensions (causal-IB, misspecification-cost quantification, tier-switching policy cost) added as new active items.

**Origins:**

- Gemini pre-audit review flagged the L0 residual mechanism on 2026-04-22 (post-promotion, pre-audit-batch).
- Three de novo audits on 2026-04-22: Gemini (2 local findings + 3 bigger-picture), Codex (4 local findings), Opus (5 local findings + 7 bigger-picture). Opus's Finding 1 duplicates the earlier Gemini flag — consolidated as Finding 1 below.

**Cross-audit compound notes:**

- **On-policy residual + step-4c convergence.** Finding 1 ($\pm\rho$ residual under on-policy execution) and Finding 11 (step 4c convergence in non-stationary environments) compound: even in stationary environments the residual is weaker than the segment implies, and in non-stationary environments the trigger may never fire. A single repair addressing both mechanisms jointly is cleaner than two independent fixes.
- **Section II scope layering.** Finding 3 (Codex: agency → learning-purposeful silent narrowing) and Finding 9 (Opus: OUTLINE preamble understates survival) touch Section II's framing at different layers — the former is internal (causal-hierarchy-requirement narrows but other segments still advertise full agency scope); the latter is external (OUTLINE preamble reads "falls outside" rather than "applies with coupling"). Coordinated reconciliation pass is more efficient than two separate ones.
- **Subsumed-by relationships.** Several findings have architectural proposals in the sibling document that would close them; see each finding's "Subsumed by" line. Choice between local repair and architectural move is explicit rather than hidden.

---

## Findings index

| # | Finding | Source | Severity | Subsumed by |
|---|---------|--------|----------|-------------|
| 1 | L0 residual under on-policy execution | Gemini (2026-04-22 pre-audit) / Opus F1 | Medium-high | — (local repair) |
| 2 | Unbounded gradient in credit-assignment signal | Gemini F1 | High | G-BP1 |
| 3 | Degenerate MI in strategy IB objective | Gemini F2 | Medium-high | G-BP2 |
| 4 | Section II silent scope narrowing (agency → learning) | Codex F1 | Medium | — |
| 5 | Loop framing overstates Level 2 access | Codex F2 | Medium | Partial by O-BP6 |
| 6 | Composition timescale heuristic outruns bridge conditions | Codex F3 | Medium-high | — |
| 7 | TST overstates git as complete chronica | Codex F4 | High | — |
| 8 | (C-iii) mutual-benefit vs (A1) decomposable $G_c$ gap | Opus F2 | Medium | — |
| 9 | Section II preamble framing understates survival | Opus F3 | Medium-high | O-BP1 |
| 10 | `#information-bottleneck` status mismatches unification role | Opus F4 | Low-medium | O-BP2 |
| 11 | Orient cascade step 4c convergence in non-stationary envs | Opus F5 | Medium | Partial by O-BP3; compound with F1 |
| 12 | Section II survival slides from statement-level to operationally extractable | Codex r2 F2 | High | C-BP1 |
| 13 | `#strategy-dag` L1-as-default overgeneralizes beyond strict-prerequisite | Codex r2 F3 | High | — |
| 14 | `#scope-developer-agent` exact-status mismatch (human vs AI regimes) | Codex r2 F4 | High | Partial by C-BP4 |
| 15 | Software "richest operationalization domain" headline overclaims | Codex r2 F5 | Low | C-BP3 |

**Actionable-now callouts** (lowest-effort / highest-clarity, if doing local repairs):

- **Finding 1** — already characterized below; repair ready.
- **Finding 7** (git claims) — sharp and contained, 30–45 min.
- **Finding 9** (Section II preamble) — 30 min rewrite, or subsumed by O-BP1 framing pass.
- **Finding 10** (IB status) — 15 min reclassification, or subsumed by O-BP2.
- **Finding 13** (strategy-dag L1-default narrowing) — 30–45 min, independent of portfolio.
- **Finding 15** (software richest-domain headline) — 15–30 min, or subsumed by C-BP3.

---

## Finding 1 — L0 residual detection mechanism fails under rational on-policy execution

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

---

## Finding 2 — Unbounded gradient updates in credit-assignment signal

**Source:** Gemini audit 2026-04-22, Finding 1. **Confidence:** high.

**Problematic passage** (`01-aad-core/src/credit-assignment-boundary.md`, default signal function):

$$\text{signal}_k(o_t) = p_k + \iota_k \cdot \frac{J_k \cdot (y_G - \hat P_\Sigma)}{\lVert\mathbf{J}\rVert^2}$$

Updating a probability $p_k \in [0, 1]$. The denominator $\lVert\mathbf{J}\rVert^2$ (squared Jacobian norm) can become arbitrarily small — particularly in deep or highly contingent AND/OR DAGs where edge sensitivities decay toward zero. When $\lVert\mathbf{J}\rVert^2 \to 0$ the signal magnitude explodes to $\pm\infty$; applied via $p_k^{\text{new}} = p_k + \eta \cdot (\text{signal} - p_k)$ this pushes credences outside the valid $[0, 1]$ probability domain.

**Strongest counterevidence in `src/`.** `#edge-update-via-gain` admits the gradient candidate "inherits $\hat P_\Sigma$'s overestimation bias under correlated failures" and "requires further validation." No segment mentions domain bounds or division-by-zero instability.

**Why this stands.** The formula is mechanically broken for bounded probability parameters. No link function (logit transform) or clipping mechanism is specified.

**msc/ lineage.** `msc/spike-credit-assignment-boundaries.md` (lines 259–263) had an explicit normalization constant $c$ ensuring the signal lies in $[0,1]$. When promoted to segment form, $c$ was dropped. `msc/spike-gain-sector-bridge-nonlinear.md` exhaustively tests gradient descent on logistic loss, noting natural-parameter spaces (logits) inherently satisfy the sector condition while keeping probabilities bounded. The core theory currently applies the continuous gradient update directly to probability parameters rather than to log-odds.

**Repair direction.**

- **Local fix:** restore the normalization constant $c$ from the spike, clip the signal to the valid probability domain, add a short Epistemic Status note that the update rule assumes $\lVert\mathbf{J}\rVert^2$ bounded below by a domain-specific constant. 30–45 min. Narrowest possible repair.
- **Architectural fix:** reparameterize edge credences in log-odds and apply the continuous gradient in $\mathbb{R}$, converting via sigmoid at the interface. Same fix mechanism as Gemini's bigger-picture G-BP1; see `msc/architectural-proposals-2026-04-22.md`. This is the principled move and may be the right scope if the reparameterization is adopted generally.

**Subsumed by:** G-BP1 (natural-parameter reparameterization). If G-BP1 is pursued, Finding 2 closes as a consequence without needing its own repair.

**Effort estimate:** 30–45 min for local fix; 2–3 sessions for G-BP1 architectural move that closes this plus related issues.

**Why deferred.** The choice between local repair and architectural move is Joseph's. If we're likely to pursue G-BP1, local repair is wasted work. If not, local repair is straightforward. Deferring for the portfolio decision.

---

## Finding 3 — Degenerate mutual information in strategy IB objective

**Source:** Gemini audit 2026-04-22, Finding 2. **Confidence:** high.

**Problematic passage** (`01-aad-core/src/strategy-complexity-cost.md`, theoretical objective):

$$\Sigma_t^\ast = \arg\min_{\Sigma_t} \left[\, I(\mathcal C_t;\, \Sigma_t) - \beta_\Sigma \cdot I(\Sigma_t;\, \pi^\ast \mid M_t)\right]$$

Under standard Shannon information theory, $\pi^\ast$ is a deterministic function of the complete epistemic state $M_t$. Conditioning on $M_t$ makes $\pi^\ast$ a constant; mutual information between any variable $\Sigma_t$ and a constant is strictly zero. So $I(\Sigma_t;\, \pi^\ast \mid M_t) = 0$ identically, and the entire objective degenerates into $\arg\min \operatorname{DL}(\Sigma_t)$ — trivially yielding an empty strategy.

**Strongest counterevidence in `src/`.** The segment marks the objective as "formulation/discussion-grade" and admits the term is "not operationalized." It conceptually explains the term as "how much the strategy helps the agent choose good actions beyond what the model already provides," implying an informal nod toward bounded computation.

**Why this partially stands.** The segment flags the term as not operationalized but does not acknowledge it evaluates to exactly zero under standard Shannon. A reader taking the objective literally finds it is mathematically empty, not merely unoperationalized.

**msc/ lineage.** `msc/spike-kappa-session-residual.md` discusses bounded computational budgets ("effort competes with other cognitive demands"). The intuition that computing $\pi^\ast$ from $M_t$ is not free is present in the msc work; the formalization in src uses standard Shannon MI, which assumes logical omniscience.

**Repair direction.**

- **Local fix:** replace the MI-conditional-on-$M_t$ with a bounded-computation-aware operational surrogate (e.g., an MDL-style cost that treats $\pi^\ast$ as accessible only via a budget-limited computation). Scope-conditional repair; preserves the objective's current shape. 45–90 min.
- **Architectural fix:** adopt variational free-energy framing per G-BP2 (`msc/architectural-proposals-2026-04-22.md`). Replaces $I(\Sigma_t;\, \pi^\ast \mid M_t)$ with a KL-divergence between the tractable DAG and the intractable optimal policy space. Natural resolution; requires scoping spike.

**Subsumed by:** G-BP2 (variational free-energy reframing).

**Effort estimate:** 45–90 min for local fix (scope note + operational surrogate); multi-session for G-BP2.

**Why deferred.** Same as Finding 2 — the choice between local scope note and architectural reframing depends on the portfolio decision about G-BP2.

---

## Finding 4 — Section II silent scope narrowing from agency to learning-purposeful

**Source:** Codex audit 2026-04-22, Finding 1. **Confidence:** high.

**Problematic passage** (`01-aad-core/src/causal-hierarchy-requirement.md`, around line 30):

> We restrict attention to **learning purposeful agents** ... All remaining Section II results operate within learning-agent scope.

**Strongest counterevidence in `src/`.**

- `#scope-agency` states Section II's purposeful machinery becomes non-vacuous at $S_{\text{agency}}$ (full agency scope, not the learning sub-scope).
- `#agent-spectrum` presents Section II as "the right column of actuated agents generally" (full agency scope).

**Why this stands.** The narrowing from agency to learning-purposeful in `#causal-hierarchy-requirement` is defensible as a sub-scope, but it is not integrated as a named Section II-wide commitment. The repo oscillates between "Section II applies to actuated agents" (in scope-condition and agent-spectrum) and "Section II applies to learning purposeful agents" (in causal-hierarchy-requirement). A reader cannot tell whether a downstream Section II claim uses the narrower or wider scope.

**msc/ lineage (not yet integrated).** `msc/analysis-2026-04-06.md` (line 265) and `msc/spike-purposeful-agent-derivation.md` (line 648) contain reasoning about the sub-scope but the integration pass has not happened.

**Repair direction.** Reconciliation pass: name the Section II-wide sub-scope explicitly (e.g., $S_{\text{learning}} \subsetneq S_{\text{agency}}$), amend `#scope-agency`, `#agent-spectrum`, and the Section II preamble in `01-aad-core/OUTLINE.md` so the narrowing is declared once and inherited by downstream Section II results. 45–60 min.

**Compound with Finding 9.** This and Finding 9 both touch Section II framing at different layers (Finding 4 inside segments; Finding 9 in OUTLINE preamble). A coordinated pass that rewrites the OUTLINE preamble plus the scope declarations in the inner segments is cheaper than two independent fixes.

**Subsumed by:** not directly. Reconciliation work. Partially simplified by O-BP1 (template-as-organizing-principle) if that reframing is adopted, since the "scope layering" becomes visible in the preamble.

**Effort estimate:** 45–60 min standalone; 60–90 min coordinated with Finding 9.

**Why deferred.** Coordination-with-Finding-9 decision; otherwise ready.

---

## Finding 5 — Loop framing overstates Level 2 access vs. identification conditions

**Source:** Codex audit 2026-04-22, Finding 2. **Confidence:** medium.

**Problematic passage** (`01-aad-core/src/loop-interventional-access.md`):

> Agency-scope agents gain Level 2 access ... through the loop itself. [line 14]
>
> ... the loop as a Level 2 engine. [line 38]

**Strongest counterevidence in `src/`.**

- `#edge-update-causal-validity` (line 26): intervention-produced data does not automatically yield clean causal identification.
- `#value-object` (line 36): the remaining requirement is that $M_t$ must actually support $P(o \mid do(a), M_t)$.

**Why this stands.** The source correctly distinguishes "data generated under intervention" from "identified do-estimates" in the specific segments, but the headline language in `#loop-interventional-access` collapses that distinction. In Pearl terms, many agents here have intervention-produced data with regime-dependent identifiability, not unconditional Level 2 knowledge. The segment overcommits on the headline that the more-careful segments qualify.

**msc/ lineage (not yet integrated).** `msc/spike-purposeful-agent-derivation.md` (line 646) discusses the same distinction.

**Repair direction.** Add a regime-indexed qualifier to the loop headlines: "the loop generates data *under intervention*; identification of causal effects from that data requires the regime conditions of `#edge-update-causal-validity`." Cross-reference between the two segments. 30 min.

**Subsumed by:** partial by O-BP6 (identity promotion). If `#agent-identity` is promoted to formal scope ("AAD applies to agents on singular causal trajectories"), the ontological ground for calling the loop *interventional* becomes explicit, and the Level-2 headline becomes honest-but-conditional rather than overclaimed.

**Effort estimate:** 30 min standalone; may be strengthened by the O-BP6 move.

**Why deferred.** Standard prioritization against portfolio decisions.

---

## Finding 6 — Composition timescale-separation heuristic outruns the verified bridge conditions

**Source:** Codex audit 2026-04-22, Finding 3. **Confidence:** high.

**Problematic passage** (`01-aad-core/src/composition-consistency.md` line 38 and following):

> [$\tau_{\text{eq}} \ll \tau_{\text{ext}}$ is] a reliable practical test ... the gap between passing that heuristic and meeting Tier 1 conditions is small in common settings.

**Strongest counterevidence in `src/`.**

- `#composition-closure` (line 149): the general case still has open computability and problem-specification choices.
- `#composition-closure` (line 151): bridge transfer is conditional on the stronger incremental sector bound (DA2'-inc).
- `#composition-closure` (line 199): still asks for a richer purposeful-agent toy case beyond the Kalman instantiation.

**Why this stands.** Section III has been substantially tightened, but the exact bridge is proved only for restricted classes. The "common organizational settings" language generalizes beyond the current purposeful-composite evidence base — a single Kalman instantiation does not warrant the "reliable practical test" framing for the much wider class of composites implied.

**msc/ lineage (not yet integrated).** `msc/spike-bridge-lemma-contraction.md` (line 457) and `msc/working-composition-admissibility.md` (line 454) contain the detailed tier-specific analysis that the heuristic overgeneralizes.

**Repair direction.** Walk back the "reliable practical test" language; retain the heuristic as explicitly Tier-1-conditional with a citation to the contraction-tier taxonomy. Add a scope note that the heuristic's effectiveness is verified for estimation-type agents (Kalman) but remains conjectural for general purposeful composites. 30–45 min.

**Subsumed by:** not directly. Scope-narrowing repair.

**Effort estimate:** 30–45 min.

**Why deferred.** Standard prioritization.

---

## Finding 7 — TST overstates git as complete/clean operational record

**Source:** Codex audit 2026-04-22, Finding 4. **Confidence:** high.

**Problematic passage** (`02-tst-core/src/software-epistemic-properties.md` lines 56, 58, 62):

> [line 56:] Exact exteriorized chronica.
>
> [line 58:] git's scope matches chronica precisely.
>
> [line 62:] environment-side AAD quantities are estimable from the historical record without the sampling and recall biases that afflict other domains.

**Strongest counterevidence in `src/`.**

- `#chronica` (line 15) defines $\mathcal C_t$ as the complete record of observations and actions (not just committed state transitions).
- `02-tst-core/src/scope-developer-agent.md` (line 89) lists many software observation channels not captured by git (IDE state, runtime observations, build system interactions, discussions outside commits).
- `02-tst-core/src/causal-discovery-from-git.md` (line 18) explicitly says the git-to-AAD chain is "empirical and unresolved."

**Why this stands.** Git records committed state transitions exactly; it does not record the full software chronica. Its causal use remains materially confounded by shared requirements, bundling conventions, and developer knowledge state that never enters commits. The current framing overstates by dropping the "committed-state subset" qualifier.

**msc/ lineage (not yet integrated).** `msc/2026-03-13-feedback.md` (line 80) and `msc/2026-03-14-section-iv-paper-outline.md` (line 60) already flag this as an empirical research program, not a derived equivalence.

**Repair direction.** Narrow P1 to "committed-state subset of chronica"; preserve the software-domain-advantage claim at a lower strength ("git captures a structured subset of the chronica with lower sampling and recall bias than self-report in other domains"). Revise P5 (causal-discovery implications) to explicitly flag the empirical chain. 30–45 min. This is sharp, contained, and does not require any other coordination.

**Subsumed by:** not directly. Scope-narrowing repair.

**Effort estimate:** 30–45 min. **Actionable now** — cleanest repair in the batch.

---

## Finding 8 — Gap between (C-iii) mutual-benefit composites and (A1) decomposable $G_c$

**Source:** Opus audit 2026-04-22, Finding 2. **Confidence:** medium.

**Problematic passages.**

`#scope-composite-agent` (lines 38–44), route (C-iii):

> Mutual-benefit alignment. There exists a relevance variable $Y$ such that the sub-agents' joint actions raise $E[Y]$ above the non-cooperation baseline for each sub-agent ... Weakest route. No explicit common objective, but interactions are positive-sum in some dimension.

`#composition-closure` (lines 73–77, 64–65):

> (A1) AAD agent structure. The macro-state decomposes as $X_c = (M_c, G_c)$. ... The closure-defect framework applies to sets that satisfy `#scope-composite-agent` — i.e., that form composites via at least one of the three alignment routes ... Given scope-satisfaction, a set forms a *meaningful* composite agent.

**Strongest mitigating passage.** `#scope-composite-agent` Epistemic Status notes "the three alternative routes are not exhaustive but cover the well-understood cases" and flags the route-relationship question as open.

**Why this stands.** The mitigating passage acknowledges the disjunction is open in principle but does *not* address the specific structural gap: (C-iii) admits composites with *no explicit* $O_c$, while (A1) *requires* $G_c = (O_c, \Sigma_c)$ as a state decomposition. For trading partners aligned only on mutual-benefit $Y$, $O_c$ cannot be naturally defined without strengthening the route — e.g., by positing $O_c = \text{maximize } E[Y]$, which collapses (C-iii) into (C-i). So either the three routes are not independently sufficient for the full closure framework, or the relationship between routes is not the honest disjunction currently advertised. The current text says both things in different places.

**msc/ lineage.** No msc document closes this. `msc/spike-agent-composition.md` and `msc/spike-symbiogenic-composition.md` are the likely homes if a broader investigation is warranted.

**Repair direction (two options).**

- **Option A:** restrict (A1) explicitly to composites satisfying (C-i) or (C-ii); treat (C-iii) as admitting only to `#multi-agent-scope` (the weaker machinery). Clean logical move; narrows what (C-iii) buys.
- **Option B:** redefine (C-iii) so that a mutual-benefit composite has an *induced* $O_c$ ("maximize $E[Y]$"), effectively collapsing (C-iii) into (C-i). Preserves (C-iii) as a route but eliminates its distinct theoretical status.

Either option resolves the logical gap; the choice depends on whether (C-iii) should be a genuinely distinct route (Option A) or an alternative framing of (C-i) (Option B).

**Subsumed by:** not directly. Scope-reconciliation repair with theoretical commitment.

**Effort estimate:** 45–60 min. Involves a substantive choice, not just editorial.

**Why deferred.** Requires Joseph's decision on Option A vs. Option B.

---

## Finding 9 — Section II preamble framing understates what `#section-ii-survival` establishes

**Source:** Opus audit 2026-04-22, Finding 3. **Confidence:** medium-high.

**Problematic passage** (`01-aad-core/OUTLINE.md`, Section II preamble):

> Class 2 (fully merged) agents — including transformer-based LLMs where attention processes goals and observations together — fall outside Section II's exact scope because directed separation (`#directed-separation`) fails by construction. The coupled formulation these agents require is the subject of `03-logogenic-agents/` ... This is the most significant scope restriction in the theory: the most important present-day agent class (LLM-based) requires work beyond Section II.

**Strongest mitigating passage.** `03-logogenic-agents/src/section-ii-survival.md` (§Scorecard and §Discussion):

> Exact: 15.5/24, Approximate: 5.5/24, Modified: 2/24, Fails: 1/24 ... Section II's *conceptual architecture* applies to Class 2 agents (16/24 exact survival is a claim about this), but Section II's *operational deployment* on Class 2 agents requires additional instrumentation.

Reinforced by `#observation-ambiguity-modulation`: in low-ambiguity domains, approximate-surviving results become *good approximations*.

**Why this stands.** The preamble's "falls outside Section II's exact scope" and "requires work beyond Section II" are literally correct but read as if Section II is non-applicable to LLM agents. The survival analysis + ambiguity modulation together say the opposite: the bulk of Section II's statement-level architecture transfers, and in low-ambiguity domains the approximate results become quantitatively tight. OUTLINE framing is the first thing a reader sees; the nuanced picture lives three documents deep.

**msc/ lineage.** `msc/spike-coupled-survival-analysis.md` contains the full 24-result classification, absorbed into `section-ii-survival.md`. Not back-propagated to the Section II preamble.

**Repair direction.** Rewrite the Section II preamble to lead with the survival classification: "Class 2 agents retain the bulk of Section II's architecture exactly (16/24), approximately in low-ambiguity domains, with specific modifications in the rest. See `#section-ii-survival` for the classification and `#observation-ambiguity-modulation` for the ambiguity-gated degradation." Preserve the fact of the Class 2 scope distinction; reframe its significance. 30 min.

**Subsumed by:** O-BP1 (template-as-organizing-principle). If the whole OUTLINE is reframed around disturbance decomposition at scales, "Class 2 is a scope exit" becomes "Class 2 is one more scale with a coupled update rule; the template applies." Natural absorption.

**Compound with Finding 4.** Both touch Section II scope framing; coordinated pass is more efficient than two independent ones.

**Effort estimate:** 30 min standalone; 60–90 min coordinated with Finding 4; absorbed if O-BP1 is adopted.

**Why deferred.** Coordination decision with Finding 4 and O-BP1.

---

## Finding 10 — `#information-bottleneck` status mismatches its unification role in `#compression-operations`

**Source:** Opus audit 2026-04-22, Finding 4. **Confidence:** low-medium.

**Problematic passage** (`#information-bottleneck` frontmatter and Epistemic Status):

> status: discussion-grade ... This is a *formulation* — it provides a principled framework for understanding compression trade-offs, not a claim about how actual agents compute their models.

**Tension.** `#compression-operations` now treats IB as the *shared shape* of four AAD compression operations (a substantial unification role) and derives that `#composition-closure`'s (P1) is the Lagrangian-dual of IB. This derivation implicitly depends on IB being a rigorous rate-distortion statement, not merely discussion-grade.

**Strongest mitigating passage.** `#compression-operations` Epistemic Status:

> The claim that the four compression operations share IB shape is *discussion-grade* ... The (P1) as Lagrangian-dual of IB is *derived* — rate-distortion duality is standard (see §I.12–13 of Cover & Thomas) and the constraint-form ↔ Lagrangian-form equivalence is mechanical.

**Why this partially stands.** The segment is honest about what's derived and what isn't. But `#information-bottleneck` itself is labeled discussion-grade while `#compression-operations` uses it as a *fixed point* for four compression operations. Consistent only because the duality invoked is external (Cover & Thomas), not internal. The labeling of `#information-bottleneck` as discussion-grade rather than "exact formulation (external theorem)" under-sells what the theory actually leans on.

**Repair direction.** Reclassify `#information-bottleneck` status from "discussion-grade" to "exact formulation (external theorem: Tishby et al. 1999)" or equivalent. Small frontmatter edit plus a one-paragraph Epistemic Status rewrite clarifying that the segment is an exact statement of an external theorem applied to AAD, not a novel formulation. 15 min.

**Subsumed by:** O-BP2 (four compressions as one hierarchy). If compression-as-hierarchy is adopted, IB's status becomes clear as the shared shape, not one of four separate objects.

**Effort estimate:** 15 min standalone; absorbed if O-BP2 adopted.

**Why deferred.** Smallest item in the batch; may be worth doing regardless of portfolio decisions just for accuracy.

---

## Finding 11 — Orient cascade step 4c convergence assumption in non-stationary environments

**Source:** Opus audit 2026-04-22, Finding 5. **Confidence:** medium.

**Problematic passage** (`#orient-cascade` step 4c):

> If persistent $\delta_s \approx 0$ coincides with persistent negative plan-outcome residuals ($y_G \lt \hat P_\Sigma$ on average, after edge credences have converged), this is evidence that the DAG is causally insufficient and L0 calibration is converging to a biased target.

**Strongest mitigating passages.**

- `#orient-cascade` Epistemic Status: "What is NOT derived is the *timing* — how long the agent should spend on each step before proceeding, and how long $\delta_s \approx 0$ must persist before 4c's signal is trusted."
- `#strategy-dag`: "The default assumption in complex environments should be L1, not L0."

**Why this partially stands.** Convergence of $\delta_s \approx 0$ requires the per-edge credences to have stabilized, which presumes a stationary environment for long enough. The environments where latent common causes are most dominant (adversarial, organizational, multi-stakeholder) are often non-stationary — precisely where the ascension signal may never fire. The mitigating passage's "use L1 by default" is a good practical answer but breaks the "cascade driven by information dependency" framing: in those regimes, the agent should not operate at L0 at all, making step 4c's trigger superfluous.

**Compound with Finding 1.** Under on-policy execution (Finding 1), the step-4c signal is zero rather than $\pm\rho$ even in stationary environments. Between Finding 1 (the signal is weak on-policy) and Finding 11 (the signal may never converge off-policy in non-stationary domains), the segment's 4c mechanism faces two different failure modes. A repair addressing both jointly is cleaner than two independent fixes.

**Repair direction.** Reframe step 4c: rather than "detect causal insufficiency from persistent residual after stationary convergence," treat L1 as the *default* in complex environments (per `#strategy-dag`'s own recommendation) and the covariance test (per Finding 1's repair) as the primary detection mechanism. Step 4c becomes a *confirmation* signal rather than a triggering signal, and the convergence assumption is reframed as a convenience rather than a requirement. 30–45 min combined with Finding 1 repair.

**Subsumed by:** partial by O-BP3 (continuous-parameter tiering). If L0→L1 is a continuous parameter, the escalation is smooth rather than triggered; the "wait for convergence to detect" framing dissolves into "increase correlation modeling depth as residuals accumulate."

**Effort estimate:** 30–45 min combined with Finding 1; absorbed in part if O-BP3 adopted.

**Why deferred.** Compound-with-Finding-1 decision; not independent.

---

## Codex round-2 findings (added 2026-04-22 late)

Second Codex audit, after the morning audit trio. One finding duplicates Finding 1 (third independent confirmation of the L0 residual issue). Four findings are new; logged below as Findings 12–15. Codex's four bigger-picture items are documented in `msc/architectural-proposals-2026-04-22.md` as C-BP1 through C-BP4.

---

## Finding 12 — Section II survival claim slides from statement-level to operationally extractable

**Source:** Codex audit 2026-04-22 round-2, Finding 2. **Confidence:** high.

**Problematic passages.**

- `03-logogenic-agents/src/section-ii-survival.md` line 37 opens with "16 survive exactly."
- `03-logogenic-agents/src/coupled-diagnostic-framework.md` line 18 says the diagnostic quantities "can be computed after each coupled update."

**Strongest counterevidence in `src/`.**

- `03-logogenic-agents/src/section-ii-survival.md` line 127 explicitly states this is *statement-level*, not operational extractability.
- `03-logogenic-agents/src/coupled-update-dynamics.md` line 66 says the $M / G$ decomposition is *post-hoc and analytical*, not architectural or computable.

**Why this stands.** The logogenic layer slides from formal well-definedness ("these quantities are defined in the Class 2 setting") to runtime measurability ("these quantities can be computed after each update") before the instrumentation layer has been published into `src/`. Readers who stop at the headline of `section-ii-survival.md` come away thinking LLM agents can run the 2×2 diagnostic directly; readers who continue to line 127 find out they can't without additional instrumentation. Similar issue in the opening of `coupled-diagnostic-framework.md`.

**msc/ lineage.** The missing operational layer for Class 2 agents already exists in `msc/agentic-tft-evaluation-framework.md` (measurement of $M_t$ / $\Sigma_t$ quality) and `msc/spike-hafez-integration-audit.md` (modular sidecar monitoring via IDT — bi-predictability $P$, entropy change $\Delta H$ monitored independently of LLM attention). The issue is not conceptual absence in the spike corpus; it is under-integration into `03-logogenic-agents/src/`.

**Repair direction (two options).**

- **Option A (local):** tighten the opening framing in both segments to lead with "statement-level" qualifiers and make the instrumentation-layer dependency explicit up front, not at line 127. 30–45 min. Fixes the headline slide without changing what the theory provides.
- **Option B (substantive):** publish the operational layer as new segments in `03-logogenic-agents/src/` — an evaluation-framework segment and an IDT-sidecar segment — drawing from the existing spike material. Substantially more work but closes the gap rather than masking it. 3–5 sessions.

**Subsumed by:** C-BP1 (three-layer separation of defined / causally valid / operationally extractable). If that framing is adopted systematically, the statement-level-vs-operational slide is prevented by convention rather than patched per-segment.

**Effort estimate:** 30–45 min for Option A; 3–5 sessions for Option B.

**Why deferred.** Option A vs Option B decision pending. Option B is closer to the honest response given the msc material already exists; Option A is the scope-hygiene repair that works regardless of how Option B proceeds.

---

## Finding 13 — `#strategy-dag` L1-as-default overgeneralizes beyond strict-prerequisite regime

**Source:** Codex audit 2026-04-22 round-2, Finding 3. **Confidence:** high.

**Problematic passages.**

- `01-aad-core/src/strategy-dag.md` line 20: "L1 ... is the practical default in complex domains," and that L0 results transfer exactly to correctly constructed L1 DAGs.
- Line 122: "The default assumption in complex environments should be L1, not L0."

**Strongest counterevidence in the same segment.**

- Line 105: L1 is the sweet spot only for **strict-prerequisite** common causes (the case formalized in `msc/spike-L1-worked-example.md`).
- Line 107: soft facilitators require L1' (mixture form), not L1 proper.
- Line 118: formal transfer for L1' is still open.

**Why this stands.** The right caveat now exists in the Correlation Hierarchy discussion, but the headline/default framing generalizes "use L1 by default" beyond the regime actually supported by the segment. A reader who takes the default at face value will apply L1 to soft-facilitator cases (common in real domains) where it is known to under-repair, missing the L1' regime entirely.

**msc/ lineage.** The L1 repair already exists in `msc/spike-L1-worked-example.md` (line 276) and is cataloged in `msc/SPIKES.md` (line 43). Integration gap: make "factor the common cause above the correlation it creates" *and* the strict-vs-soft split part of the front-door claim, not only the deep-discussion caveat.

**Repair direction.** Narrow the default framing: "L1 is the practical default **for strict-prerequisite common causes**; soft facilitators require L1' (formal transfer open) or direct L2 modeling." Move the strict-vs-soft distinction into the Formal Expression or opening discussion rather than leaving it in the deep-discussion paragraphs. 30–45 min.

**Subsumed by:** not directly, though the spirit of C-BP2 (master separability pattern) would make explicit that "L0/L1/L1'/L2" is one of several instances of the separability-plus-repair pattern, and the segment's presentation would align with that canonical framing.

**Effort estimate:** 30–45 min.

**Why deferred.** Standard prioritization.

---

## Finding 14 — `#scope-developer-agent` tagged `status: exact` but mapping collapses human and AI developer regimes

**Source:** Codex audit 2026-04-22 round-2, Finding 4. **Confidence:** high.

**Problematic passages.**

- `02-tst-core/src/scope-developer-agent.md` frontmatter line 4: `status: exact`.
- Line 160 (Epistemic Status): each AAD quantity has a concrete, identifiable software counterpart.

**Strongest counterevidence in the same segment.**

- Line 63: AI agents are "more explicitly representable" than human developers.
- Line 182 (Working Note): explicit DAG applicability to implicit human planning is an open question.

**Why this stands.** The segment collapses two distinct regimes — human developer (with implicit, non-externalized planning structures) and AI developer (with externalized planning artifacts: commits, PRs, reasoning traces, explicit DAGs) — into one `exact`-tagged mapping. The segment's own Working Note identifies that explicit-DAG applicability to implicit human planning is open; an `exact` status is inconsistent with this.

**msc/ lineage.** No mature msc repair for the human-developer exactness claim. Adjacent: `msc/feedback.md` (line 43) discusses software as the privileged high-identifiability domain, which suggests the cleaner framing (C-BP3 below) but does not itself address the human/AI regime split.

**Repair direction (two options).**

- **Option A (status downgrade):** downgrade status from `exact` to `robust-qualitative` with an explicit scope condition — "exact for AI developers with externalized planning artifacts; approximate for human developers where planning is implicit." 15–30 min.
- **Option B (segment split):** split into two segments — `developer-as-act-agent` (human regime, robust-qualitative) and `ai-developer-as-act-agent` (AI regime with externalized planning, exact). Stronger but requires more surgery, including updating dependencies. 45–60 min.

**Subsumed by:** partial by C-BP4 (claim-level epistemic statuses). Under C-BP4, the segment would carry one status for the definitional core and separate statuses for the transfer claims per regime, avoiding the "umbrella status tag forced to cover distinct regimes" failure mode.

**Effort estimate:** 15–30 min for Option A; 45–60 min for Option B.

**Why deferred.** Option A vs. Option B decision.

---

## Finding 15 — Software "richest operationalization domain" headline overclaims (already largely caveated)

**Source:** Codex audit 2026-04-22 round-2, Finding 5. **Confidence:** medium-high. Codex explicitly notes this is "already caveated" and "would not count as a deep theory defect."

**Problematic passage.**

- `02-tst-core/src/software-epistemic-properties.md` line 15: software's six properties "collectively make it the richest operationalization domain for AAD."

**Strongest counterevidence in the same segment.**

- Line 27 (scope block): major advantages are narrowed to codebase-only or code-internal regimes.
- Line 70 (Epistemic Status): the comparative claim is harder to verify and not systematic.

**Why this is low-severity.** The segment itself honestly narrows the claim in its body; only the headline/opening retains the strongest version. Codex explicitly says "would not count as a deep theory defect." Logged here for completeness and because C-BP3 (software as calibration laboratory not universal exemplar) would reframe it at the proposal level.

**Repair direction.** Tighten the headline to "highest identifiability / intervention access / logging among operationalization domains" or "software is the privileged high-identifiability calibration domain for AAD." Preserves the substantive claim (software is uniquely tractable) without the "richest" comparative framing that the segment's own body does not defend. 15–30 min.

**Subsumed by:** C-BP3 (software as calibration laboratory). Adopting C-BP3 closes this by changing the positioning of TST at the framework level, not just the headline of one segment.

**Effort estimate:** 15–30 min.

**Why deferred.** Low-priority; best handled as part of C-BP3 if that move is adopted.


---

## Post-strengthening evening batch (added 2026-04-22, after the strengthening cycle's commits)

A second triple-audit cycle (Codex / Gemini / Opus) ran *after* the strengthening cycle (commits `14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`) had landed. The audits were de novo against the current repository state. Three distinct kinds of finding emerged:

- **Integration gaps from prior cycles** — cross-segment updates that should have propagated when a result landed but did not. F18 (worked-example-L1 still says L1' is open) and F19 (section-ii-survival still has the entropy-form bias bound) are both in this class. Mechanical to fix.
- **New scope/operational-extractability frictions** — F16 (Section II scope lattice underspecified) and F17 (coupled-diagnostic-framework operational-computability overclaim) surface as distinct from the existing 15-finding batch.
- **Bugs introduced by the strengthening cycle itself** — F20 (KL direction degeneracy in the V-medium variational form) is a substantive theoretical issue introduced by commit `a14682e`. F21 (identifiability-floor frontmatter contradicts internal text) is a drafting artifact in the segment created by commit `b91493c`.

Six new findings logged below. The seven candidate findings rescinded by the new audits (Gemini Findings 4 + 5; Opus's Section III explore-agent items; Opus's six rescinded candidates) are listed in `msc/spike-active-inference-vs-aad.md`-style transparency tables in their respective audit transcripts; they do not appear here.

---

## Finding 16 — Section II scope lattice underspecified across segments

**Source:** Codex audit 2026-04-22 (post-strengthening evening), Finding 1. **Confidence:** high.

**Problematic passages.**

- `01-aad-core/src/scope-agency.md` line 14: "Adding causal action unlocks the interventional and purposeful results of Sections II and III."
- `01-aad-core/src/agent-spectrum.md` line ~30: actuated agents are "the full scope of AAD."

**Strongest counterevidence in `src/`.**

- `01-aad-core/src/causal-hierarchy-requirement.md` line 30 narrows to "learning purposeful agents" (a strict sub-scope of agency).
- `01-aad-core/src/directed-separation.md` line ~84 says exact Section II results apply to Class 1 architectures only; Class 2 requires the coupled formulation.

**Why this stands.** The caveats exist but are scattered. No segment carries the full intersection statement: agency-scope ∩ learning-agent-scope ∩ Class-1-architecture. A reader following the headline scope claims in `#scope-agency` and `#agent-spectrum` over-generalizes; a reader following the per-segment narrowings has to assemble the intersection themselves.

**Repair direction.** Two options: (a) Add the intersection statement to `#scope-agency` Discussion as the canonical Section II scope statement; (b) Promote a small meta-segment `#section-ii-scope-lattice` (or equivalent) that names the lattice once and is referenced from the Section II preamble in `01-aad-core/OUTLINE.md`. Option (b) is structurally cleaner and supports O-BP8 (scope-lattice naming) below.

**Subsumed by:** O-BP8 (explicit scope lattice). Partially subsumed by O-BP1 if the template-as-organizing-principle reframing happens to surface the lattice.

**Effort estimate:** 30–60 min for option (a); 1–2 sessions if pursued as a meta-segment.

---

## Finding 17 — `#coupled-diagnostic-framework` operational-computability overclaim

**Source:** Codex audit 2026-04-22 (post-strengthening evening), Finding 4. **Confidence:** high.

**Problematic passages.**

- `03-logogenic-agents/src/coupled-diagnostic-framework.md` line 18: diagnostic quantities "can be computed *after* each coupled update."
- Same segment around line 40: "From $X^{(\text{post})}$, compute …" presents a runtime-recipe phrasing.

**Strongest counterevidence in `src/`.**

- `03-logogenic-agents/src/section-ii-survival.md` line 127: statement-level survival is not "operational extractability"; separate instrumentation is required.
- `03-logogenic-agents/src/coupled-update-dynamics.md` line 66: the M/G decomposition is "post-hoc and analytical, not generally computable."

**Why this stands.** The recipe-style phrasing in `#coupled-diagnostic-framework` reads as runtime-extractable. The same logogenic layer's other segments correctly mark the M/G decomposition as analytical reconstruction. A fresh reader of the diagnostic-framework segment would think the framework is operational; a reader of the companion segments would conclude it requires instrumentation. The repo says both.

**Repair direction.** Reframe the segment's phrasing to acknowledge the M/G decomposition as analytical reconstruction, not runtime recipe. Cite `#coupled-update-dynamics` for the post-hoc-analytical-not-architectural distinction. Reference `msc/agentic-tft-evaluation-framework.md` and `msc/agentic-tft-cognitive-loop-spec.md` for the better framing (these quantities are estimated in language with explicit tracking/instrumentation, not directly read out from an internal state object). 30–45 min.

**Subsumed by:** C-BP1 (three-layer epistemic separation). The defined / causally valid / operationally extractable framework would force the segment to mark the diagnostic recipe explicitly at the operational layer, exposing the gap.

---

## Finding 18 — `#worked-example-L1` still says L1' transfer is "open" — STALE after F13 strengthening

**Source:** Gemini audit 2026-04-22 (post-strengthening evening), Finding 1. **Confidence:** high.

**Problematic passage.**

- `01-aad-core/src/worked-example-L1.md` line ~134: "Sector-condition verification for L1' has not been derived (each conditional sub-plan is an L0 DAG whose sector parameters are known, but their weighted combination introduces a $\theta_C$-dependent factor analogous to Prop B.6's $\theta_C$ gating; the full transfer through B.5b is an open item)."

**Strongest counterevidence in `src/`.**

- `01-aad-core/src/strategic-dynamics-derivation.md` Prop B.7 (added 2026-04-22 commit `4d050c8`): derives the L1' sector transfer for observable common cause with explicit five-way-gating $\alpha_{L1'}$ formula.
- `01-aad-core/src/strategy-dag.md` Correlation Hierarchy (updated same commit): four-row table with L1' sector status now "Derived."

**Why this stands.** Mechanical integration gap: F13 strengthening landed Prop B.7 but the cross-segment update to `#worked-example-L1` was queued (per `msc/spike-finding-13-strengthening.md` §8.4) and not performed. The "open" language is now stale; the example is structurally a B.7 instance (the worked example uses observable $C$, satisfying B.7's scope condition).

**Repair direction.** Update the relevant paragraph in `#worked-example-L1` to reflect Prop B.7's status: "Sector-condition verification for L1' is derived in Prop B.7 ( #strategic-dynamics-derivation) for the observable-$C$ case the example operates within (five-way gating $\alpha_{L1'}$ formula, with explicit reduction to B.6 in the strict-prerequisite limit). Under unobservable $C$, L1' is *refuted* by the Cramér-Rao floor (mixture identifiability obstruction; see B.7 §'Refuted Under Unobservable $C$' and #discussion-identifiability-floor)." 10–15 min.

**Subsumed by:** not directly. Pure cross-segment update.

---

## Finding 19 — `#section-ii-survival` bias bound in entropy form, stale after 2026-04-21 Finding B resolution

**Source:** Gemini audit 2026-04-22 (post-strengthening evening), Finding 3. **Confidence:** high.

**Problematic passage.**

- `03-logogenic-agents/src/section-ii-survival.md` line 109: $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa_{\text{processing}} \cdot H(G_t \mid e_\tau, M_{\tau^-})$
- Same segment line 136 (Working Notes): "The bound … deserves formal derivation … Without this, the bound is order-of-magnitude guidance, not a theorem."

**Strongest counterevidence in `src/`.**

- The 2026-04-21 Finding B resolution recast `#observation-ambiguity-modulation`'s definition and downstream bias bound as $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa \cdot I(G; \Omega \mid e, M)$ — a strict refinement (mutual information of the goal-conditional posterior given the observation, not entropy of the goal alone). Documented in `msc/pending-findings-2026-04-21.md` Finding B resolution and absorbed into `#observation-ambiguity-modulation`.
- `#section-ii-survival` still serves the older entropy form and the Working Note's "order-of-magnitude" disclaimer about it.

**Why this stands.** Cross-segment update gap from the 2026-04-21 cycle. The tighter MI form is a strict refinement (entropy is an upper bound on conditional MI; using MI gives a tighter bias bound). The integration touch on `#section-ii-survival` was not performed.

**Repair direction.** Replace the entropy form with the MI form on line 109; update the Working Note at line 136 to acknowledge the refinement and the source segment (`#observation-ambiguity-modulation` carries the canonical recasting). 15–25 min.

**Subsumed by:** not directly. Cross-segment update from prior cycle.

---

## Finding 20 — KL-direction degeneracy in `#strategy-complexity-cost` variational form (introduced by 2026-04-22 V-medium)

**Source:** Opus audit 2026-04-22 (post-strengthening evening), Finding 1. **Confidence:** medium-high. **Severity: high — affects the load-bearing G-BP2 V-medium move.**

**Problematic passage.**

- `01-aad-core/src/strategy-complexity-cost.md` line ~42:
$$\Sigma_t^\ast = \arg\min_{\Sigma_t} \left[\, I(\mathcal C_t;\, \Sigma_t) \;+\; \beta_\Sigma \cdot D_{\mathrm{KL}}\bigl(Q_{\Sigma_t}(\pi \mid M_t) \,\big\Vert\, \pi^\ast(\cdot \mid M_t)\bigr)\right]$$
- And the Epistemic Status text (line ~123) claiming "the KL form does not have this degeneracy."

**Why this stands.** When $\pi^\ast$ is deterministic given $M_t$ (the standard scope) — i.e., $\pi^\ast(\cdot \mid M_t) = \delta_{a^\ast(M_t)}$ — the forward KL $D_{\mathrm{KL}}(Q \Vert \delta_{a^\ast})$ is *infinite* unless $Q$'s support is contained in $\{a^\ast\}$. Equivalently: the divergence is binary (0 if $Q$ is exactly the optimum point mass, $+\infty$ otherwise) rather than graded. The original Shannon-MI degeneracy was zero (always uninformative); the KL-form degeneracy is a hard constraint (any sub-optimal $Q$ is infinitely penalized). The V-medium move resolved one degeneracy by introducing a structurally parallel one.

The mathematically clean fix: **reverse the KL direction.** $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log Q_{\Sigma_t}(a^\ast \mid M_t)$ is finite whenever $Q$ places positive mass on $a^\ast$ and grades continuously in that mass — exactly the "how close is the strategy to the optimum" measurement intended.

**Strongest counterevidence in `src/`.** Line 44 of the same segment says "well-defined when $\pi^\ast$ is deterministic-from-$M_t$." This is mathematically true (the extended-real value exists) but the segment uses it to justify "the degeneracy is avoided," conflating well-defined-value with graded-optimization-target.

The companion spike `msc/spike-active-inference-vs-aad.md` lines ~296–299 reproduces the same direction and same framing; the issue is genuinely absent from the working documents, not just the segment. The fix needs to land in both.

**Repair direction (three options).**

- **(a) Reverse the KL direction** to $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$, which equals $-\log Q_{\Sigma_t}(a^\ast \mid M_t)$ for deterministic $\pi^\ast$ — finite, graded, and the natural "negative log-likelihood of the optimal action." This is the recommended option.
- **(b) Treat $\pi^\ast$ as a Boltzmann-softmax over $V_{O_t}$.** Both KL directions become finite. Closer to active-inference's actual practice (policy posteriors are typically softmax-over-EFE in AI). Adds a temperature parameter.
- **(c) Acknowledge multiple admissible variational shapes.** Present the forward-KL as one option with the deterministic-$\pi^\ast$ caveat explicit; reverse-KL as another; let the segment be agnostic.

Recommended: option (a), with a brief Discussion paragraph noting the directional choice and crediting the active-inference literature's convention (forward KL with approximation first) while explaining why the AAD setting (deterministic $\pi^\ast$) requires the reverse direction for graded optimization.

**Effort estimate:** 30–45 min for the segment edit + spike repair + Epistemic Status update + cross-segment mention check.

**Subsumed by:** not directly. Theoretical-correction repair within the V-medium move.

---

## Finding 21 — `#discussion-identifiability-floor` frontmatter status conflicts with internal text

**Source:** Opus audit 2026-04-22 (post-strengthening evening), Finding 3. **Confidence:** medium. **Severity: low (drafting artifact).**

**Problematic passages.**

- `01-aad-core/src/discussion-identifiability-floor.md` line 4: `status: robust-qualitative`.
- Same segment Epistemic Status (line ~95): "*Robust qualitative.* The meta-pattern itself is a *discussion-grade* observation … Whether the pattern is a *generative principle* … is a *hypothesis* …"

**Why this stands.** The single Epistemic Status paragraph labels the meta-pattern three different ways (robust-qualitative, discussion-grade, hypothesis). The frontmatter chooses (i). Each phrasing is defensible on its own; the missing piece is a single non-contradictory statement.

**Repair direction.** Probable best resolution: change frontmatter to `status: discussion-grade` (the weakest of the three labels — honest about the meta-observation tier) and add a sentence in Epistemic Status making explicit that the *two derived instances* (Instance 1: exact for shallow / robust-qualitative for general; Instance 2: exact) are at higher tier than the meta-pattern itself. The segment's status reflects the meta-observation; the instances retain their own. 10–15 min.

**Subsumed by:** not directly. Drafting cleanup in segment created by commit `b91493c`.
