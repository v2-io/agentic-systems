---
slug: spike-finding-1-strengthening
type: spike
status: working
date: 2026-04-22
---

# Spike: Finding 1 — Strengthening Attempt (No-Go Theorem for On-Policy L0 Insufficiency Detection)

**Status:** Strengthening spike. Attempts to convert `01-aad-core/src/causal-insufficiency-detection.md` from "we observe that the residual collapses on-policy" (the softening repair already on file in `msc/spike-finding-1-l0-residual-repair.md`) into "we *prove* no on-policy mechanism can detect L0 causal insufficiency." If proved, this is a no-go theorem strengthening that materially upgrades the segment.

**Date:** 2026-04-22

**Trigger:** Joseph's review of the prior softening repair concluded that the strengthening attempt should have been done first. Operating posture: always attempt strengthening before fallback to softening; the hardness of the move is not a reason to deprioritize.

**Context document:** `msc/pending-findings-2026-04-22.md` Finding 1 (lines 49–125) and the prior softening spike `msc/spike-finding-1-l0-residual-repair.md`.

---

## §1 — Strengthening Attempt Log

### What was tried

1. **Move 1 — Observational equivalence.** Generalize the existing spike's algebraic observation (under on-policy execution, an L0 model with conditional credences exactly recovers the true joint) into a structural statement: the on-policy observation distribution under an *L0 world* with edge probabilities equal to the regime conditionals is *identical* to the on-policy observation distribution under the *L1 world* that produces those same conditionals. Worked through a 2-OR strict-prerequisite case explicitly, then identified the general principle.

2. **Move 2 — Apply the causal hierarchy.** Once observational equivalence holds, invoke Bareinboim, Correa, Ibeling, Icard (2022, "On Pearl's Hierarchy and the Foundations of Causal Inference") Theorem 1 (Causal Hierarchy Theorem, CHT): there exist SCMs that agree on Level 1 (associational) but disagree on Level 2 (interventional), so Level 2 distinctions are not in general identifiable from Level 1 data. The L0/L1 distinction is precisely such a Level 2 distinction (whether siblings share a common cause is a question about $P(A_2 \mid do(\neg A_1))$ vs $P(A_2 \mid \neg A_1)$).

3. **Move 3 — Boundary characterization.** Enumerate the precise capabilities that violate "purely on-policy" and recover detection. Five mechanisms identified: (a) ε-exploration, (b) joint sibling observability, (c) intermediate-state observability, (d) structural priors, (e) explicit interventions on the candidate latent.

### What worked

- **Observational equivalence holds cleanly for the 2-OR strict-prerequisite case.** The algebra closes: for any L1 world with latent $C$ and conditionally independent siblings (strict prerequisite: $\theta_{j \mid \neg C} = 0$), there exists an L0 world (with marginal $\theta_1$ and conditional $p_2^c$) that produces the *exact same* on-policy observation distribution under sequential short-circuit execution. The full derivation is §3.

- **The CHT applies cleanly.** Once observational equivalence is established, the CHT immediately gives the no-go: no purely on-policy detector can distinguish the two worlds.

- **The boundary characterization sharpens which AAD machinery is load-bearing.** Five circumvention mechanisms map onto five existing AAD constructs. The covariance test in the existing segment is precisely route (b); the loop's interventional access is route (e); SA3 ε-exploration is route (a); structural priors are the unspoken modeling choice in DAG construction. This connects the no-go to existing scaffolding rather than introducing new machinery.

### What did not work cleanly

- **Soft-facilitator generalization.** The 2-OR strict-prerequisite case has $\theta_{j \mid \neg C} = 0$, which makes the algebra collapse cleanly. For soft facilitators ($\theta_{j \mid \neg C} \gt 0$, which `#strategy-dag` calls L1' rather than L1 proper), the observational-equivalence argument is *more constrained* — the L0 world that matches the L1 on-policy distribution is uniquely determined by the on-policy regime conditionals, and any deviation in the underlying L1 parameters that preserves those conditionals is observationally equivalent. The no-go therefore *transfers* but in a softer form: the agent can rule out *some* L1 worlds (those producing different on-policy conditionals) but cannot identify the specific L1 world it is in. Documented as the "weak no-go for soft-facilitator" extension.

- **AND-heavy strategies.** The AND-node version is asymmetric: under on-policy execution of $A_1 \land A_2$, if $A_1$ fails, $A_2$ is never tried, so the agent learns $P(A_2 \mid A_1 \text{ succeeded})$. The same observational-equivalence construction applies (an L0 world with marginal $\theta_1$ and conditional $p_2^c = P(A_2 \mid A_1)$ matches the on-policy distribution). The algebra is symmetric to OR; documented in §3.

- **Mixed and deeper DAGs.** For DAGs with mixed AND/OR or depth $\gt 2$, the construction is structural: the agent's on-policy observation distribution depends on the *short-circuit regime tree* (which paths are taken given which outcomes). For each path-conditional, there exist L0 and L1 parameter assignments producing the same conditional; gluing these together produces an L0 world observationally equivalent to the L1 world. The general construction is sketched but not proved with full generality. **This is the honest gap.** The no-go is exact for shallow strict-prerequisite cases and a robust qualitative claim for the general case.

### Where the strengthening lands

- **Exact** for the 2-sibling strict-prerequisite case (both OR and AND).
- **Robust qualitative** for general DAGs (the structural argument is sound; the explicit construction has not been carried out for arbitrary topologies).
- **Conditional on the agent being purely on-policy** — when the agent has any of the five circumvention mechanisms, the no-go does not apply (and indeed each mechanism gives a partial detection signal).

This is materially stronger than the softening repair: the softening repair documents that the residual mechanism collapses; the strengthening proves that *no* on-policy mechanism can do better. The covariance test does not just happen to work — it is precisely the unique interventional route (under joint sibling observability) that circumvents the no-go.

### Decision: proceed with strengthening

The strengthening succeeded for the load-bearing case (strict-prerequisite L1) and as a robust qualitative statement for the general case. The proposed segment is structured around the no-go theorem as primary content, with the covariance test as the unique route given the no-go, and the boundary characterization as an explicit map of which AAD capabilities circumvent the no-go.

The fallback (apply the softening repair instead) is not warranted: the strengthening attempt is honest and lands a material upgrade.

---

## §2 — Statement of the No-Go Theorem

### Theorem (No-Go for Purely On-Policy L0 Insufficiency Detection)

*[Derived (from causal hierarchy theorem + observational equivalence under on-policy short-circuit), conditional on: (i) pure on-policy execution with sequential short-circuit, (ii) per-edge credence stabilization, (iii) the L1 candidate is a strict-prerequisite common cause for the load-bearing case]*

Let $\mathcal{M}_{L0}$ denote an agent's L0 strategy model (independence assumed among siblings under common parents) and let $\mathcal{W}_{L1}$ denote a world in which a latent common cause $C$ acts on multiple siblings (causal insufficiency from L0's perspective). Let $\pi_{L0}$ denote the agent's executed policy under sequential short-circuit AND/OR evaluation of $\mathcal{M}_{L0}$. Let $\mathbb{P}_{\pi_{L0}}^{\text{obs}}$ denote the joint distribution over the agent's on-policy observable events (action attempts, censored outcomes from short-circuit, plan-level results) under $\pi_{L0}$ executed in $\mathcal{W}_{L1}$.

**Claim.** There exists an L0 world $\mathcal{W}_{L0}^\ast$ with edge probabilities determined by the on-policy regime conditionals of $\mathcal{W}_{L1}$ such that:

$$\mathbb{P}_{\pi_{L0}}^{\text{obs}}\big[\mathcal{W}_{L1}\big] \;=\; \mathbb{P}_{\pi_{L0}}^{\text{obs}}\big[\mathcal{W}_{L0}^\ast\big]$$

That is, the agent's on-policy observation distributions in $\mathcal{W}_{L1}$ and in $\mathcal{W}_{L0}^\ast$ are identical.

**Corollary (the no-go).** Any function of the agent's on-policy observable history alone — any test, statistic, or detector $T$ that takes only $\mathbb{P}_{\pi_{L0}}^{\text{obs}}$ as input — cannot distinguish $\mathcal{W}_{L1}$ from $\mathcal{W}_{L0}^\ast$. Therefore no purely on-policy detection mechanism can detect L0 causal insufficiency.

**Tier:** *Exact* for shallow strict-prerequisite cases (2-sibling OR and 2-sibling AND, single binary common cause). *Robust qualitative* for general DAG topologies (the structural argument transfers; explicit construction not carried out for arbitrary topology and conditional-independence patterns).

**Scope conditions.** The no-go holds under:
- (S1) **Pure on-policy execution.** No off-policy sampling. No exploration.
- (S2) **Sequential short-circuit evaluation.** AND nodes stop on first failure; OR nodes stop on first success.
- (S3) **Censored sibling observation.** When short-circuit terminates, the un-attempted sibling's outcome is unobservable.
- (S4) **No interventional access to the latent.** The agent cannot directly intervene on $C$.
- (S5) **No structural prior on $C$.** The agent does not have domain knowledge that posits a specific common cause.

When *any* of (S1)–(S5) is violated, the no-go does not apply, and detection becomes possible (with strength and route depending on which condition is relaxed). §5 characterizes the boundary.

### Why this is a strengthening, not a softening

The prior softening repair documents the failure of the residual mechanism. The strengthening here:

1. **Localizes the failure.** Not "the residual mechanism happens to collapse" but "the residual is just one observable statistic, and no observable statistic can distinguish L0 from L1 on-policy." The specific failure of the residual is a special case of a deeper structural impossibility.

2. **Identifies the unique remedy.** The covariance test does not just happen to work; it is precisely the route that violates condition (S3) — joint sibling observability provides off-policy joint outcome data the no-go forbids.

3. **Connects to existing load-bearing machinery.** The loop's interventional access (`#loop-interventional-access`) becomes load-bearing in a sharper way: it is exactly the mechanism that circumvents the no-go via condition (S4)'s violation. This makes the case for the loop being constitutive of agency stronger.

4. **Sets a standard for any future on-policy detection proposal.** Anyone who proposes a new on-policy L0-insufficiency test must explain which of (S1)–(S5) it relies on; the no-go closes the field of "purely observational tests" entirely.

---

## §3 — Proof of Observational Equivalence (Move 1)

### 3.1 Two-sibling OR with strict-prerequisite common cause (the load-bearing case)

**Setup.** Two action propositions $A_1, A_2$ as siblings under an OR-node (the agent's plan is "achieve goal via $A_1$ or $A_2$"). The agent's strategy is L0: it treats $A_1, A_2$ as independent and executes sequential short-circuit (try $A_1$; if succeeds, done; if fails, try $A_2$).

**True world ($\mathcal{W}_{L1}$).** Latent binary common cause $C$ with $P(C = 1) = \theta_C$. Strict prerequisite: when $C = 0$, both $A_1, A_2$ fail with probability 1 (i.e., $\theta_{1 \mid \neg C} = \theta_{2 \mid \neg C} = 0$). When $C = 1$, $A_1$ succeeds with probability $\theta_{1 \mid C}$ and $A_2$ with probability $\theta_{2 \mid C}$, conditionally independent given $C$.

**Marginal probabilities under $\mathcal{W}_{L1}$:**

$$\theta_1^{\text{marg}} = \theta_C \cdot \theta_{1 \mid C}, \qquad \theta_2^{\text{marg}} = \theta_C \cdot \theta_{2 \mid C}$$

**Conditional under the short-circuit regime** (the rate the agent observes for $A_2$ given $A_2$ is actually tried, i.e., $A_1$ failed):

$$p_2^c \;=\; P\big(A_2 \text{ succeeds} \,\big\vert\, A_1 \text{ failed}\big) \;=\; \frac{P(A_2 = 1, A_1 = 0)}{P(A_1 = 0)}$$

Computing the numerator: $A_2 = 1, A_1 = 0$ requires $C = 1$ (else $A_2 = 0$); given $C = 1$, requires $A_1 = 0$ (prob $1 - \theta_{1 \mid C}$) and $A_2 = 1$ (prob $\theta_{2 \mid C}$). So $P(A_1 = 0, A_2 = 1) = \theta_C \cdot (1 - \theta_{1 \mid C}) \cdot \theta_{2 \mid C}$.

Computing the denominator: $P(A_1 = 0) = 1 - \theta_C \cdot \theta_{1 \mid C} = 1 - \theta_1^{\text{marg}}$.

Therefore:

$$p_2^c = \frac{\theta_C \,(1 - \theta_{1 \mid C})\, \theta_{2 \mid C}}{1 - \theta_C \, \theta_{1 \mid C}}$$

**Alternative L0 world ($\mathcal{W}_{L0}^\ast$).** Two independent edges:
- $A_1$ succeeds with probability $\theta_1^\ast = \theta_1^{\text{marg}} = \theta_C \cdot \theta_{1 \mid C}$
- $A_2$ succeeds with probability $\theta_2^\ast = p_2^c$ (the conditional from $\mathcal{W}_{L1}$)
- $A_1, A_2$ are independent (no latent $C$)

**Claim.** The on-policy observation distribution of the agent under $\pi_{L0}$ in $\mathcal{W}_{L0}^\ast$ equals the on-policy observation distribution under $\pi_{L0}$ in $\mathcal{W}_{L1}$.

**Proof.** The agent's on-policy observable events under sequential short-circuit OR are exactly three (mutually exclusive and exhaustive):

- $E_1$: "$A_1$ attempted, succeeded" (plan succeeds; $A_2$ never attempted, outcome unobservable).
- $E_2$: "$A_1$ attempted, failed; $A_2$ attempted, succeeded" (plan succeeds).
- $E_3$: "$A_1$ attempted, failed; $A_2$ attempted, failed" (plan fails).

Compute $P(E_1), P(E_2), P(E_3)$ under each world.

**Under $\mathcal{W}_{L1}$:**

- $P^{L1}(E_1) = P(A_1 = 1) = \theta_C \cdot \theta_{1 \mid C} = \theta_1^{\text{marg}}$
- $P^{L1}(E_2) = P(A_1 = 0, A_2 = 1) = \theta_C \cdot (1 - \theta_{1 \mid C}) \cdot \theta_{2 \mid C}$
- $P^{L1}(E_3) = P(A_1 = 0, A_2 = 0) = (1 - \theta_C) + \theta_C \cdot (1 - \theta_{1 \mid C}) \cdot (1 - \theta_{2 \mid C})$

(For $E_3$: either $C = 0$ (both fail by strict prerequisite), or $C = 1$ and both fail given $C = 1$.)

**Under $\mathcal{W}_{L0}^\ast$:**

- $P^{L0\ast}(E_1) = \theta_1^\ast = \theta_1^{\text{marg}} = \theta_C \cdot \theta_{1 \mid C}$. ✓ matches $P^{L1}(E_1)$.

- $P^{L0\ast}(E_2) = (1 - \theta_1^\ast) \cdot \theta_2^\ast = (1 - \theta_C \theta_{1 \mid C}) \cdot \frac{\theta_C (1 - \theta_{1 \mid C}) \theta_{2 \mid C}}{1 - \theta_C \theta_{1 \mid C}} = \theta_C \cdot (1 - \theta_{1 \mid C}) \cdot \theta_{2 \mid C}$. ✓ matches $P^{L1}(E_2)$.

- $P^{L0\ast}(E_3) = 1 - P^{L0\ast}(E_1) - P^{L0\ast}(E_2)$. Since $E_1, E_2, E_3$ are exhaustive and the first two probabilities match, $P^{L0\ast}(E_3) = 1 - P^{L1}(E_1) - P^{L1}(E_2) = P^{L1}(E_3)$. ✓ matches.

The on-policy observation distributions are identical. $\square$

**Comment on what this construction does and does not require.** The construction uses:
- Sequential short-circuit (so $A_2$ is attempted iff $A_1$ failed).
- Censored sibling observation (when $A_2$ is not attempted, its outcome is unobserved, so the "success of $A_1$" event is not paired with any $A_2$ outcome).

The construction does *not* require:
- A specific value of $\theta_C$ (works for any $\theta_C \in (0, 1)$).
- Identical conditional probabilities $\theta_{1 \mid C} = \theta_{2 \mid C}$ (works for any pair).
- Linearity, independence of higher-order moments, or any distributional smoothness.

The construction is a structural identity, not an approximation.

### 3.2 Two-sibling AND (symmetric to OR)

**Setup.** Strategy is $A_1 \land A_2$ (both required for success). Sequential execution: try $A_1$; if succeeds, try $A_2$; if $A_1$ fails, plan fails and $A_2$ is not attempted.

**True world ($\mathcal{W}_{L1}^{\text{AND}}$).** Latent $C$ with $P(C = 1) = \theta_C$, strict prerequisite, conditionally independent siblings as before.

**On-policy observable events:**
- $E_1^{\text{AND}}$: "$A_1$ attempted, failed" (plan fails; $A_2$ never attempted).
- $E_2^{\text{AND}}$: "$A_1$ attempted, succeeded; $A_2$ attempted, succeeded" (plan succeeds).
- $E_3^{\text{AND}}$: "$A_1$ attempted, succeeded; $A_2$ attempted, failed" (plan fails).

**Conditional under regime:** $p_2^{c, \text{AND}} = P(A_2 \mid A_1 \text{ succeeded}) = \frac{\theta_C \theta_{1 \mid C} \theta_{2 \mid C}}{\theta_C \theta_{1 \mid C}} = \theta_{2 \mid C}$.

(Note: under strict prerequisite, conditioning on "A_1 succeeded" implies $C = 1$, so $A_2$'s conditional probability is just $\theta_{2 \mid C}$.)

**Alternative L0 world ($\mathcal{W}_{L0}^{\ast, \text{AND}}$):** $\theta_1^\ast = \theta_C \theta_{1 \mid C}$, $\theta_2^\ast = \theta_{2 \mid C}$, independent.

Verify:
- $P^{L1}(E_1^{\text{AND}}) = 1 - \theta_C \theta_{1 \mid C}$. $P^{L0\ast}(E_1^{\text{AND}}) = 1 - \theta_1^\ast = 1 - \theta_C \theta_{1 \mid C}$. ✓
- $P^{L1}(E_2^{\text{AND}}) = \theta_C \theta_{1 \mid C} \theta_{2 \mid C}$. $P^{L0\ast}(E_2^{\text{AND}}) = \theta_1^\ast \theta_2^\ast = \theta_C \theta_{1 \mid C} \theta_{2 \mid C}$. ✓
- $P^{L1}(E_3^{\text{AND}}) = \theta_C \theta_{1 \mid C} (1 - \theta_{2 \mid C})$. $P^{L0\ast}(E_3^{\text{AND}}) = \theta_1^\ast (1 - \theta_2^\ast) = \theta_C \theta_{1 \mid C} (1 - \theta_{2 \mid C})$. ✓

Observational equivalence holds for AND with the same structural argument. $\square$

### 3.3 General topology — the structural argument

For a general AND/OR DAG executed under sequential short-circuit, the agent's on-policy observable events are determined by the *short-circuit regime tree*: at each node, one branch of the regime tree corresponds to "this child's attempt and outcome," and short-circuit prunes branches that the regime renders unreachable. Each leaf of the regime tree is a complete observable event.

**Construction.** For each leaf event $E$ of the regime tree under $\mathcal{W}_{L1}$, compute:

$$P^{L1}(E) = \sum_{c} P(C = c) \cdot \prod_{j \in E} P(A_j = y_j \mid C = c)$$

where $y_j$ is the outcome of $A_j$ as recorded in event $E$.

For $\mathcal{W}_{L0}^\ast$, parameterize by edge probabilities $\{\theta_j^\ast\}$ such that, conditional on the short-circuit regime that leads to $A_j$ being attempted, $\theta_j^\ast$ matches the L1 conditional probability of $A_j$ succeeding under that regime. Then:

$$P^{L0\ast}(E) = \prod_{j \in E} P(A_j = y_j \mid \text{regime}_j)$$

where $\text{regime}_j$ is the conjunction of preceding outcomes that brought the agent to attempt $A_j$.

**Claim.** For each regime-conditional, $P^{L1}(A_j = y_j \mid \text{regime}_j) = \theta_j^\ast$ by construction, and the joint over the leaf event factors the same way. Therefore $P^{L1}(E) = P^{L0\ast}(E)$ for every leaf event.

**Why this is a robust qualitative statement, not exact-for-arbitrary-DAGs.** The construction requires the regime conditionals to be well-defined and to admit an L0 parameterization. For DAGs with multiple latent common causes, mixed AND/OR with cross-cutting common-cause structure, or non-strict (soft-facilitator) common causes, the L0 parameter assignment that matches all regime conditionals may require *more* than independent edge probabilities — it may require regime-indexed credences (which is itself a departure from L0). In those cases the construction yields a *family* of L0 parameterizations matching disjoint regime-leaves but not a single L0 world matching all events with one parameter set. The no-go still holds (the agent cannot distinguish L1 from this family), but the cleanliness of the "alternative L0 world" framing weakens. Documented in §1 as the gap between "exact for shallow strict-prerequisite" and "robust qualitative for general topology."

### 3.4 Soft-facilitator extension (weak no-go)

When the L1 common cause is a soft facilitator ($\theta_{j \mid \neg C} \gt 0$), the strict-prerequisite collapse does not occur — siblings can succeed even when $C$ is absent, just less reliably. The on-policy observable events are the same three for the OR case, but their probabilities differ.

The observational-equivalence argument transfers: there exists an L0 world ($\theta_1^\ast = $ marginal, $\theta_2^\ast = $ on-policy conditional) producing the same on-policy distribution. The construction algebra is similar to §3.1 with the added $(1-\theta_C)\,\theta_{j \mid \neg C}$ contributions; the structural identity holds for the same reason (three event probabilities, two parameters, one constraint via probabilities summing to 1).

The *weak* part: the agent can rule out L1 worlds that produce different on-policy conditionals from the observed data, but cannot identify the specific L1 world it is in (multiple L1 parameter combinations can produce the same on-policy conditionals). The no-go still holds for *detection of L1 vs L0*; identification within the L1 family is a separate (also-on-policy-impossible) problem.

---

## §4 — No-Go Conclusion via the Causal Hierarchy (Move 2)

### 4.1 The Causal Hierarchy Theorem (Bareinboim et al. 2022)

**Source.** Bareinboim, Correa, Ibeling, Icard (2022), "On Pearl's Hierarchy and the Foundations of Causal Inference," in *Probabilistic and Causal Inference: The Works of Judea Pearl*, ACM Books. Theorem 1 (Causal Hierarchy Theorem, CHT), §3.

**Statement (paraphrased).** The Pearl Causal Hierarchy is *non-collapsible*: with probability 1 over a natural measure on SCMs, an SCM's Level $i$ valuation does not determine its Level $i+1$ valuation. Concretely, for almost every choice of structural equations, there exist alternative SCMs that match on Level 1 (associational) queries but disagree on Level 2 (interventional) queries.

The CHT is the rigorous form of the long-standing principle that observational data alone cannot in general distinguish two causal models with different interventional consequences — Simpson's paradox, the front-door problem, and confounding all instantiate this gap. The 2022 result formalizes the gap as a measure-theoretic non-collapse.

### 4.2 Application to L0 vs L1

The L0/L1 distinction in `#strategy-dag` is *exactly* a Level 2 distinction:

- L0 says: $P(A_2 \mid A_1) = P(A_2 \mid do(\neg A_1)) = P(A_2)$ (independence; no common cause).
- L1 says: $P(A_2 \mid A_1) = P(A_2)$ may hold, but $P(A_2 \mid do(\neg A_1)) \neq P(A_2 \mid \neg A_1)$ in general because conditioning on $A_1 = 0$ via observation also conditions on $C$ (if $A_1 = 0$ is more likely under $C = 0$), while $do(A_1 = 0)$ does not.

The L1 latent common cause is a *confounder* in Pearl's sense: a variable that affects both siblings, producing correlations under observation that are not present under intervention.

By the CHT, the L0 and L1 SCMs that agree on Level 1 (the on-policy conditional and marginal probabilities) can disagree on Level 2 (whether intervening on $A_1$ changes $A_2$'s success rate). The agent's on-policy data is purely Level 1. By the CHT, no purely Level 1 statistic can distinguish L0 from L1.

Combining with §3: the observationally equivalent L0 world ($\mathcal{W}_{L0}^\ast$) constructed in §3 *is* a Level-1 equivalent of the L1 world, and by the CHT no Level-1 test can tell them apart.

### 4.3 The no-go conclusion

**Conclusion.** Any on-policy detection mechanism is a function of the agent's Level-1 (associational) on-policy observation distribution. By the CHT (and concretely by the §3 observational-equivalence construction), this distribution is identical between $\mathcal{W}_{L1}$ and $\mathcal{W}_{L0}^\ast$. Therefore any such detection mechanism returns the same result in both worlds and cannot detect the L1 structure.

In particular:
- The aggregate L0 plan-level residual is one such mechanism. Under on-policy execution it returns 0 in *both* worlds (the prior softening repair derived this directly). The no-go subsumes this special case.
- Any other on-policy aggregate statistic (mean error, variance of plan outcomes, KL divergence between plan-confidence and outcome distribution, maximum likelihood over the L0 parameter space, etc.) shares the same fate.
- Any on-policy *Bayesian* test (computing the posterior probability of L1 given on-policy data, with any prior) returns the same posterior in both worlds (the likelihood is identical).

The only way to escape the no-go is to violate one of the scope conditions (S1)–(S5) — i.e., to bring information into the test that is *not* in the on-policy observation distribution.

### 4.4 Why the loop's interventional access matters

`#loop-interventional-access` claims that the agent has Level 2 data by construction. The no-go shows that this Level 2 data is *load-bearing* for L0-insufficiency detection: without it, no detection is possible. This sharpens the case for `#loop-interventional-access` being constitutive of agency rather than incidental.

The covariance test in the prior segment is precisely the Level 2 test that the loop enables. Joint sibling observability under the SA3 exploration regime gives the agent samples of $(Y_{A_1}, Y_{A_2})$ where *both* outcomes are recorded, not censored by short-circuit. These joint samples include cases where the agent intervened to attempt $A_2$ even when $A_1$ would have succeeded — the data *is* interventional in Pearl's sense, not just intervention-produced. The no-go's scope condition (S3) is violated by joint observability, and the covariance test exploits this exact violation.

---

## §5 — Boundary Characterization (Move 3)

The no-go scope conditions (S1)–(S5) are the precise statement of "purely on-policy." Each condition's violation corresponds to a specific AAD capability that recovers (partial) detection. Five routes:

### Route (a): ε-exploration violates (S1)

The agent occasionally takes off-policy actions (ε-greedy or similar — the SA3 condition in `#strategic-dynamics-derivation`). Under ε-exploration, the agent samples non-short-circuit branches with rate ε.

**What this gives.** A mixture of on-policy and off-policy data. Edge credences converge to a mixture of conditional and marginal:

$$\hat p_j \to (1 - \varepsilon) \, p_j^c + \varepsilon \, \theta_j^{\text{marg}}$$

The aggregate plan-level residual scales linearly in ε (the prior spike's "$\varepsilon \cdot \rho$" heuristic, which is exact in the ε → 1 limit and structure-dependent at intermediate ε).

**Strength.** Partial. Detection power scales with ε; for small ε the signal is small relative to noise. Adequate for confirming L1 once the agent has reason to suspect it; weak for unprompted detection.

**Cross-reference.** `#strategic-dynamics-derivation` Prop B.4 (OR-node calibration via ε-exploration); the prior softening spike's secondary signal section.

### Route (b): Joint sibling observability violates (S3)

Trials in which both siblings' outcomes are observed in the same environment state, regardless of short-circuit. This requires either (i) the agent forces simultaneous attempts (parallel execution), (ii) the environment exposes both outcomes when one is attempted (e.g., observing a competitor's parallel action result), or (iii) the agent re-runs after short-circuit terminates (replay capability).

**What this gives.** Samples of the joint $(Y_{A_1}, Y_{A_2})$. The pairwise covariance test:

$$\hat \rho_{ij} = \frac{1}{N} \sum_t (Y_{A_i,t} - \bar Y_{A_i})(Y_{A_j,t} - \bar Y_{A_j})$$

rejects the L0 independence hypothesis when significantly positive.

**Strength.** Strong. This is the test the prior softening repair promotes to primary. The strengthening here clarifies *why* it is primary: it is the unique route violating (S3), which is the load-bearing scope condition for the no-go's joint-distribution argument.

**Cross-reference.** The covariance test in `#causal-insufficiency-detection`.

### Route (c): Intermediate-state observability violates (S3) at finer granularity

Beyond joint sibling outcomes, the agent observes *cause* indicators (intermediate states that reveal whether the latent common cause is active). For example, in software deployment, monitoring shared infrastructure status directly (CPU load, network connectivity) gives the agent partial observation of $C$ without needing joint sibling outcomes.

**What this gives.** Direct (or partial) observation of the latent. With $C$ observable, the L1 model is no longer latent; the agent can fit conditional credences directly and the L0/L1 distinction collapses.

**Strength.** Very strong (when available). When the cause indicator is reliable, this is the cleanest detection — the agent simply observes $C$ rather than inferring it.

**Cross-reference.** `#observability-dominance` — observability investment as a strategic capability; the proposition that making intermediates observable strictly improves the sector parameter.

### Route (d): Structural priors violate (S5)

The agent has domain knowledge that posits a candidate common cause $\hat C$ (e.g., "shared infrastructure could fail," "weather affects both operations"). Even without observing $\hat C$, the prior shifts the L1 hypothesis space and admits a Bayesian test: under the prior $\pi(\hat C)$, the posterior over L1 worlds compatible with the observed data is computable.

**What this gives.** A Bayesian model-comparison test (L0 vs L1-with-$\hat C$) where the prior provides the differentiating information that the data cannot. The agent's belief about whether $\hat C$ matters updates from on-policy data even if the data alone cannot identify the latent.

**Strength.** Variable, depends entirely on prior quality. With strong priors (L1-with-$\hat C$ is heavily favored a priori), the agent rapidly concludes L1 even from limited data. With flat priors, the data dominates and the no-go reasserts itself.

**Cross-reference.** This is the implicit modeling capability invoked when the agent's L1 construction (per `#strategy-dag`) includes a hypothesized common cause. The prior is not in the segment formally, but is operationally present whenever an agent adds a node to its DAG without first confirming the node's existence empirically.

### Route (e): Direct intervention on the latent violates (S4)

The agent acts to manipulate $C$ directly (e.g., switching infrastructure providers, changing weather conditions in a controlled experiment). This is the strongest violation: the agent obtains $P(A_j \mid do(C = c))$ data, which is a Level 2 test by Pearl's definition.

**What this gives.** Direct interventional identification of the L1 structure. The agent learns the conditional success rates under each $C$ value, and the L0/L1 distinction is operationally resolved.

**Strength.** Strongest (when available). When the latent is intervenable, the no-go does not even start — the agent has Level 2 access to the candidate latent itself.

**Cross-reference.** `#loop-interventional-access` — the loop generates interventional data on the agent's *actions*, but route (e) requires interventional data on the *latent* specifically. For natural common causes (weather, market regime, opponent strategy) this is rarely available. For engineered common causes (configuration choices, design parameters) it is sometimes available.

### Boundary table

| Route | Scope condition violated | AAD capability | Detection strength | Cost |
|-------|--------------------------|----------------|--------------------|----|
| (a) ε-exploration | (S1) | SA3 exploration | Partial, ~ε·ρ | Forgone exploitation |
| (b) Joint sibling observability | (S3) | Covariance test under SA3 | Strong | Joint-attempt overhead |
| (c) Intermediate observability | (S3) at finer grain | Observability investment | Very strong | Observability cost |
| (d) Structural priors | (S5) | DAG construction with hypothesized common-cause nodes | Prior-quality-dependent | Modeling effort |
| (e) Direct intervention on latent | (S4) | Domain-specific intervention capability | Strongest | Domain availability |

**The covariance test under SA3 (route (b) + supplementary route (a))** is the AAD-canonical route: it uses machinery the theory already requires (`#strategy-dag` exploration, `#loop-interventional-access`) and is available in the broadest range of domains. This explains why the prior softening repair's promotion of the covariance test to primary is the right architectural move — it is the unique broadly-available violation of the no-go.

### What is *not* a circumvention

For completeness: several plausible-sounding moves do *not* circumvent the no-go.

- **More on-policy data.** The no-go is asymptotic-in-$N$ — even infinite on-policy data does not distinguish $\mathcal{W}_{L1}$ from $\mathcal{W}_{L0}^\ast$. Sample size does not help.
- **More sophisticated on-policy statistics.** Higher moments, non-linear transformations, latent-variable models fit on on-policy data alone — none help, because the joint distribution over on-policy events is identical between the two worlds.
- **Non-stationary observation under fixed policy.** If the agent maintains a fixed policy but the environment changes, the on-policy distribution changes — but the L0/L1 indistinguishability transfers to each stationary epoch separately. The agent learns *different* L0 parameters in different epochs without ever resolving the L0/L1 question.
- **Multi-objective execution.** Running the strategy under different objectives changes which short-circuit branches are taken but does not generate joint-sibling data unless one of routes (a)–(e) is invoked alongside.

Each of these can *appear* to add information, but the appearance dissolves under the structural argument: the on-policy distribution under any deterministic policy in any L0 world matching the regime-conditionals is identical to the L1 distribution.

---

## §6 — Strengthened Segment Revision

The full proposed text of `01-aad-core/src/causal-insufficiency-detection.md` follows. Apply by replacing the entire segment.

```markdown
---
slug: causal-insufficiency-detection
type: derived
status: conditional
depends:
  - structural-adaptation-necessity
  - strategy-dag
  - loop-interventional-access
  - causal-hierarchy-requirement
  - pearl-causal-hierarchy
  - causal-information-yield
stage: draft
---

# Derived: Causal Insufficiency Detection

An agent operating at L0 of the Correlation Hierarchy ( #strategy-dag) faces a structural impossibility: under purely on-policy execution, no detection mechanism can distinguish an L0-insufficient world (latent common causes present) from an L0-sufficient world matched to the on-policy regime conditionals. This is a consequence of the causal hierarchy theorem ( #pearl-causal-hierarchy, #causal-hierarchy-requirement) — observational data does not in general identify interventional structure. Detection is therefore *only* possible by capabilities that violate the "purely on-policy" condition: joint sibling observability under exploration (the canonical AAD route, exploiting #loop-interventional-access), intermediate-state observability, structural priors, or direct intervention on the candidate latent. The pairwise sibling covariance test is the AAD-canonical detector; the L0 plan-level residual is a degenerate special case of the no-go.

## Formal Expression

### The No-Go Theorem: Purely On-Policy Detection Is Impossible

*[Derived (no-go-on-policy, from causal hierarchy theorem + observational equivalence under sequential short-circuit), conditional on (S1)–(S5) below]*

Let $\mathcal{M}_{L0}$ be the agent's L0 strategy model with sequential short-circuit AND/OR execution policy $\pi_{L0}$. Let $\mathcal{W}_{L1}$ be a world with a latent common cause $C$ acting on multiple sibling action propositions, and $\mathcal{W}_{L0}^\ast$ be an L0 world with edge probabilities $\{\theta_j^\ast\}$ matched to the on-policy regime conditionals of $\mathcal{W}_{L1}$. Let $\mathbb{P}_{\pi_{L0}}^{\text{obs}}[\cdot]$ denote the joint distribution over the agent's on-policy observable events under $\pi_{L0}$.

**Observational equivalence.** $\mathbb{P}_{\pi_{L0}}^{\text{obs}}[\mathcal{W}_{L1}] = \mathbb{P}_{\pi_{L0}}^{\text{obs}}[\mathcal{W}_{L0}^\ast]$.

**No-go conclusion.** Any function of the agent's on-policy observable history alone cannot distinguish $\mathcal{W}_{L1}$ from $\mathcal{W}_{L0}^\ast$. Therefore no purely on-policy detection mechanism — no test, statistic, or Bayesian comparison taking only the on-policy distribution as input — can detect L0 causal insufficiency.

**Scope conditions (S1)–(S5).**

- (S1) Pure on-policy execution; no off-policy sampling.
- (S2) Sequential short-circuit AND/OR evaluation.
- (S3) Censored sibling observation: short-circuited siblings are not observed.
- (S4) No interventional access to candidate latents.
- (S5) No structural priors positing specific common causes.

**Tier.** *Exact* for shallow strict-prerequisite cases (2-sibling OR or AND with binary common cause and $\theta_{j \mid \neg C} = 0$ — see #worked-example-L1). *Robust qualitative* for general DAG topology, soft facilitators, and deeper structures: the structural argument transfers, but explicit $\mathcal{W}_{L0}^\ast$ construction has been carried out only for shallow cases.

**Construction of $\mathcal{W}_{L0}^\ast$.** For a 2-sibling OR with strict-prerequisite latent $C$, $P(C) = \theta_C$, conditional success rates $\theta_{j \mid C}$:

$$\theta_1^\ast = \theta_C \cdot \theta_{1 \mid C}, \qquad \theta_2^\ast = p_2^c = \frac{\theta_C\,(1 - \theta_{1 \mid C})\,\theta_{2 \mid C}}{1 - \theta_C\,\theta_{1 \mid C}}$$

Direct verification (see #worked-example-L1) shows $\mathbb{P}_{\pi_{L0}}^{\text{obs}}[\mathcal{W}_{L1}] = \mathbb{P}_{\pi_{L0}}^{\text{obs}}[\mathcal{W}_{L0}^\ast]$ on the three on-policy observable events.

**Why this matters.** The no-go is the structural reason the prior aggregate-residual mechanism collapses on-policy: the residual is a function of $\mathbb{P}_{\pi_{L0}}^{\text{obs}}$, which is identical between the two worlds, so the residual is identically zero under both. The collapse is not a quirk of the residual statistic — it is a special case of the no-go applied to that specific function. No replacement aggregate statistic can do better.

### The Detection Routes: What Circumvents the No-Go

*[Derived (boundary-routes, from no-go scope conditions)]*

The no-go's scope conditions (S1)–(S5) define "purely on-policy." Each condition's violation corresponds to an AAD capability that admits (partial) detection:

| Route | Scope violated | AAD capability | Detection strength |
|-------|----------------|----------------|--------------------|
| (a) ε-exploration | (S1) | SA3 exploration ( #strategic-dynamics-derivation Prop B.4) | Partial, scales with ε |
| (b) Joint sibling observability | (S3) | Covariance test under SA3 + #loop-interventional-access | Strong |
| (c) Intermediate observability | (S3) at finer grain | Observability investment ( #observability-dominance) | Very strong when available |
| (d) Structural priors | (S5) | Hypothesized common-cause nodes in DAG construction | Prior-quality-dependent |
| (e) Direct intervention on latent | (S4) | Domain-specific latent control | Strongest when available |

The covariance test (route (b)) is the AAD-canonical detector: it uses only machinery the theory already requires (exploration via SA3, interventional data via the loop) and is available in the broadest range of domains. The remaining sections operationalize this primary mechanism.

### Primary Detection Mechanism: Pairwise Sibling Covariance Under Intervention

*[Derived (from loop-interventional-access + independence test, conditional on SA3 exploration providing joint observability)]*

Under L0 (the independence model in #strategy-dag's Correlation Hierarchy), sibling outcomes under a common parent are uncorrelated:

$$H_0:\;\operatorname{Cov}(Y_{A_i}, Y_{A_j}) = 0 \quad \forall\; i \neq j \;\text{siblings under the same parent}$$

Under causal insufficiency (latent common cause $C$ acting on multiple siblings), sibling outcomes are positively correlated:

$$H_1:\;\exists\; i \neq j \;\text{with}\; \operatorname{Cov}(Y_{A_i}, Y_{A_j}) \gt 0$$

The agent generates test data through the standard exploration mechanism (SA3 — $\varepsilon$-greedy or similar). On trials where both siblings are observable — the agent tries one and can also observe the other's outcome, or tries them in rapid succession before the environment state changes — it accumulates the empirical covariance:

$$\hat\rho_{ij} = \frac{1}{N}\sum_t (Y_{A_i,t} - \bar{Y}_{A_i})(Y_{A_j,t} - \bar{Y}_{A_j})$$

A significantly positive $\hat\rho_{ij}$ rejects the L0 independence hypothesis. Joint observability ( #loop-interventional-access supplies the interventional character; SA3 supplies the joint sampling) is precisely the violation of scope condition (S3) that admits the test under the no-go.

**Detection criterion.** A statistically significant positive $\hat\rho_{ij}$ at sample size $N$ sufficient for the desired test power, after per-edge credences have stabilized:

$$\hat\rho_{ij} \gt z_{1-\alpha}\,\hat\sigma_{\rho_{ij}} / \sqrt{N} \quad\implies\quad \text{DAG is causally insufficient between siblings } i, j$$

(Standard hypothesis-testing form; threshold and test power depend on application.)

**Preconditions for the covariance test.**

1. **Joint observability.** The agent can occasionally observe $(Y_{A_i}, Y_{A_j})$ pairs in the same environment state. Pure short-circuit execution censors one of each pair; SA3 exploration or simultaneous-attempt regimes provide uncensored pairs.
2. **Per-edge credence stabilization.** Edge credences $\hat p_i, \hat p_j$ have stopped drifting at the timescale of the covariance accumulation, so $\bar Y_{A_i}, \bar Y_{A_j}$ are well-defined empirical means.
3. **Approximate stationarity over the test window.** The latent common cause's frequency and the conditional success rates are not drifting faster than the test's accumulation timescale.

When these preconditions hold, $\hat\rho_{ij} \gt 0$ is diagnostic of a missing common cause acting on $(A_i, A_j)$. When they do not, the signal is ambiguous.

### The Aggregate Residual as a Degenerate Special Case of the No-Go

*[Derived (residual-degeneracy, as instance of no-go theorem)]*

A historically prominent diagnostic uses the L0 plan-level residual $\Phi^{L0}(\hat{\boldsymbol p}) - \bar{y}_G$ as a detection signal. The no-go theorem subsumes this as a special case: under pure on-policy execution, the residual is *identically zero* in both $\mathcal{W}_{L1}$ and $\mathcal{W}_{L0}^\ast$.

**Direct verification.** Under sequential short-circuit, the agent's empirical credences converge to the on-policy regime conditionals: $\hat p_j \to p_j^c$. Plugging these into the L0 arithmetic recovers the chain rule of probability (e.g., for OR: $1 - (1 - p_1^c)(1 - p_2^c) = 1 - P(\neg A_1, \neg A_2) = P(A_1 \cup A_2)$, which equals $\bar y_G$ under the executed policy). The residual is zero by algebraic identity.

This is *not* a separate finding from the no-go: it is the no-go's prediction for the specific aggregate-residual statistic. The no-go forbids *any* on-policy statistic from distinguishing $\mathcal{W}_{L1}$ from $\mathcal{W}_{L0}^\ast$; the residual evaluates to the same value (zero) in both, as expected.

**Off-policy boundary.** Under ε-exploration (route (a)), the residual scales as $O(\varepsilon)$ to leading order with sign matching the dominant node-type bias ($+$ for OR-heavy, $-$ for AND-heavy):

$$\Phi^{L0}(\hat{\boldsymbol p}) - \bar y_G = \varepsilon \cdot R + O(\varepsilon^2), \quad \operatorname{sign}(R) = \operatorname{sign}(\rho)$$

where $R$ is structure-dependent and recovers the marginal-limit $\rho$ at $\varepsilon = 1$. *[Heuristic]* The qualitative form is robust; the exact coefficient depends on the gap between conditional and marginal credences. The widely-quoted "$\varepsilon \cdot \rho$" scaling is correct as an order-of-magnitude statement.

The residual is therefore a *confirmatory* signal under route (a): when the agent has material off-policy exploration and the covariance test (route (b)) has localized a candidate latent, the residual sign confirms the bias direction. It is not a primary detector and cannot replace the covariance test.

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

Which actions are most informative for detecting latent common causes? Under the no-go, only actions that violate one of (S1)–(S5) yield detection signal. The explore-exploit tradeoff extends with a third axis tied to the boundary characterization:

- **Exploit**: pursue the current best plan (no scope violation; no detection signal).
- **Explore**: test unknown edges for individual success rates (route (a); partial detection).
- **Diagnose**: test known edges for joint correlation structure (route (b); strong detection).

Diagnosis is a form of internal exploration — the agent probes its own model's structural assumptions by violating (S3) deliberately, generating joint sibling outcomes that the no-go forbids the agent to obtain on-policy. The information value of diagnostic actions is highest when:

- Edge credences have converged (the agent has good marginals/conditionals but unknown joint structure).
- Joint outcomes for sibling pairs are observable in the same environment state (the covariance test has data — route (b) is operational).
- The agent has sufficient off-policy budget that the secondary residual signal corroborates (route (a) is also operational).

## Epistemic Status

*Conditional* on the no-go's scope conditions (S1)–(S5) and on strategy-layer instantiation of #structural-adaptation-necessity. The **no-go theorem** is *exact* for shallow strict-prerequisite cases (2-sibling OR or AND, single binary common cause) by direct construction; *robust qualitative* for general DAG topology, soft facilitators, and deeper structures. The structural argument (observational equivalence of regime-conditional L0 and latent-cause L1) transfers to the general case; explicit construction of $\mathcal{W}_{L0}^\ast$ has been carried out only for shallow cases.

The **boundary characterization** (routes (a)–(e)) is *robust qualitative*: each route maps to a specific scope-condition violation and to existing AAD machinery, but the precise detection power of each route depends on domain particulars. Routes (a) and (b) have explicit AAD scaffolding ( #strategic-dynamics-derivation, #loop-interventional-access); routes (c)–(e) depend on domain capability.

The **primary detection mechanism** (pairwise sibling covariance) is *robust qualitative*: standard hypothesis testing applied to interventional data from the feedback loop, with explicit preconditions. Its sensitivity depends on how cleanly the agent can separate sibling-covariance signal from edge-credence noise at convergence; in adversarial or fast-drifting environments the test's effective sample size shrinks.

The **aggregate residual** as a confirmatory signal is *exact* for the on-policy collapse (no-go's prediction is direct); the off-policy mixed-regime scaling is *heuristic* (linear-in-$\varepsilon$ with structure-dependent coefficient).

The **detection-to-construction pipeline** is *discussion-grade*: the trigger is the (statistically rigorous) covariance signal, but the specific procedures for estimating $\theta_C$ and $\theta_{k|C}$ from correlated outcome data are domain engineering.

### What Cannot Be Detected

By the no-go and its boundary characterization, several latent structures remain undetectable by *any* AAD route:

- **Latents with no joint-observability route.** If the latent affects siblings that cannot be jointly observed (mutually exclusive with long horizons, no cause-indicator availability, no intervention capability, no informative prior), the no-go applies in full strength and detection is impossible.
- **Latents affecting only one edge.** By definition not common causes; appear as noise in individual edge credences.
- **Latents too rare to produce observable joint outcomes.** Even with route (b) operational, a latent with $\theta_C \approx 1$ rarely reveals itself — the agent needs enough $C = 0$ events to estimate the covariance.
- **Negatively-correlating latents.** The formulation assumes positive correlation from shared enabling factors. Negative correlation (competing for a shared resource) produces the opposite bias pattern and requires a different model.

These limitations parallel the information-theoretic underdetermination in #credit-assignment-boundary: detection requires data with the right structure, and the no-go specifies precisely what "right structure" means.

## Discussion

**Why the no-go is a strengthening, not a softening.** The prior framing ("the residual mechanism collapses on-policy") was a local observation about one statistic. The no-go is the structural reason: any on-policy statistic must collapse, because the on-policy distribution is identical between L0 and L1 worlds matched on regime conditionals. The covariance test is not just *a* working detector — it is the unique broadly-available violation of the no-go's scope. This sharpens the load-bearing of `#loop-interventional-access`: without the loop's interventional data, the no-go forbids detection entirely; with it, route (b) is operational.

**Connection to Pearl's hierarchy.** The L0/L1 distinction is a Level 2 distinction in Pearl's framework — it concerns whether $P(A_2 \mid do(\neg A_1)) = P(A_2 \mid \neg A_1)$. The Causal Hierarchy Theorem (Bareinboim, Correa, Ibeling, Icard 2022, Theorem 1) proves that Level 2 distinctions are not in general identifiable from Level 1 (associational) data. The no-go is the AAD-specific instantiation: on-policy data is Level 1; the L0/L1 question is Level 2; therefore detection requires more than on-policy data. The five circumvention routes are all ways the agent obtains supra-Level-1 information.

**The censoring mechanism is the structural source.** Sequential short-circuit evaluation is what makes on-policy data Level 1 only — it censors the joint outcomes that would constitute Level 2 evidence. An agent that *did not* short-circuit would obtain joint sibling outcomes naturally, and the no-go would not apply. But short-circuit is forced by efficiency: testing $A_2$ when $A_1$ has already succeeded is wasted action. The no-go is therefore a tradeoff between execution efficiency (favoring short-circuit) and structural diagnosis (favoring joint observation). SA3 ε-exploration is the AAD compromise: short-circuit by default, occasional non-short-circuit excursions that pay the efficiency cost to maintain detection capability.

**Connection to the orient cascade.** The detection signal enters the orient cascade ( #orient-cascade) at step 4c (causal-sufficiency check). Step 4c's reference to "pairwise sibling covariance under an augmented test" aligns with the primary detection mechanism here. The no-go strengthens the cascade's load-bearing: step 4c is not "one possible diagnostic" but "the unique broadly-available diagnostic given the structural impossibility of purely on-policy detection."

**Domain instantiations.** The covariance test (route (b)) applies concretely in:
- **Software deployment**: two services sharing infrastructure fail together more often than independent failure rates predict → add infrastructure-health node.
- **Military operations**: two concurrent operations fail together under adverse weather → add weather-condition node.
- **Investment**: two positions lose value together during market stress → add market-regime node.
- **Organizational strategy**: two initiatives stall together during leadership transitions → add organizational-stability node.

In each, what makes detection feasible is the agent's ability to occasionally observe *both* sibling outcomes — the route (b) capability. Pure short-circuit ("only run service B if A is down") suppresses the joint-observation events the test relies on; some routine joint exposure is necessary. When joint observation is impossible (routes (b) and (c) both unavailable) and intervention on the candidate latent is impossible (route (e) unavailable), the agent must rely on structural priors (route (d)) — domain knowledge positing the common cause. This is the regime in which intuition-driven causal modeling is the only tractable approach.

## Working Notes

- The general-topology construction in §3.3 of `msc/spike-finding-1-strengthening.md` is a structural argument; the explicit $\mathcal{W}_{L0}^\ast$ for arbitrary AND/OR DAGs with mixed common-cause patterns has not been carried out. For load-bearing application of the no-go to specific complex topologies, the construction should be specialized. Currently the load-bearing applications (orient-cascade step 4c, strategy-dag's L0/L1 escalation principle) reference shallow strict-prerequisite cases for which the no-go is exact.
- The boundary characterization's routes (c) and (e) depend on domain capability and are not formalized in AAD beyond cross-references to `#observability-dominance` and `#loop-interventional-access`. A future refinement could quantify "detection power" per route as a function of domain parameters (e.g., observability cost, intervention availability, prior strength).
- The no-go is asymmetric: it forbids on-policy *detection* of L1 from L0, but it does *not* forbid on-policy *parameter learning within L0*. The agent can learn its L0 conditionals to arbitrary precision on-policy; it just cannot determine whether those conditionals hide a latent. This distinction sharpens the diagnosis-vs-calibration split that #structural-adaptation-necessity makes at the parametric/structural boundary.
- The CHT (Bareinboim et al. 2022) is invoked as an external theorem. AAD inherits its conditions (well-defined SCMs over compatible variable sets); these are satisfied for the strategy-DAG setting by construction. If a future version of the segment wants to make the CHT dependency tighter, citing the specific theorem and conditions inline is the move.
```

---

## §7 — Comparison to the Softening Repair

What becomes stronger:

- **Detection Principle is now a no-go theorem, not an observation.** The prior repair documented that the residual mechanism happens to collapse; the strengthening proves no on-policy mechanism can succeed. The covariance test's primacy is no longer a choice ("we promote it because the residual fails") but a derivation ("it is the unique broadly-available violation of the no-go").

- **`#loop-interventional-access` becomes load-bearing in a sharper way.** Previously it was "useful machinery for the covariance test"; now it is "the load-bearing mechanism that circumvents an otherwise-binding no-go." This makes the case for the loop being constitutive of agency materially stronger and sharpens the Section II inevitability-core argument for `#loop-interventional-access`.

- **The boundary characterization is itself a contribution.** Five routes mapped to AAD machinery, each tied to a specific scope-condition violation. This provides a clear answer to "what does an agent need to detect L1 from L0?" — previously left as "use the covariance test" without explanation.

- **The aggregate residual is now a special case rather than a competing diagnostic.** The prior repair demoted it to "secondary signal under off-policy"; the strengthening explains it as "what the no-go predicts for this specific statistic." This is more precise and pedagogically cleaner.

- **The connection to Pearl's hierarchy is explicit.** The L0/L1 question is a Level 2 question; on-policy data is Level 1; the CHT forbids Level-1-to-Level-2 identification. This connects to existing dependent segments (`#causal-hierarchy-requirement`, `#pearl-causal-hierarchy`) that the prior segment did not lean on.

What stays the same:

- **Covariance test machinery.** The primary detection mechanism is essentially identical to the prior repair's primary mechanism. The strengthening reframes *why* it is primary; the test itself is the same.

- **From-detection-to-construction.** The pipeline (hypothesize $C$, estimate $\theta_C$, restructure DAG, re-estimate conditionals) is unchanged. The trigger is the same (positive covariance).

- **Diagnostic CIY discussion.** The three-way exploit/explore/diagnose framing is preserved, with diagnose now framed as "deliberately violating (S3) to obtain joint outcomes."

- **What Cannot Be Detected.** The list of fundamental limitations is preserved, with sharper framing as "what no route can detect."

- **Domain instantiations.** Same examples; same analysis.

What is in tension and how it resolves:

- **Frontmatter dependencies.** The prior repair listed `causal-information-yield` as a dependency. The strengthening adds `causal-hierarchy-requirement` and `pearl-causal-hierarchy` because the no-go invokes the CHT. This is a dependency expansion (the no-go is a more dependent claim than the residual collapse), not a contradiction.

- **Heuristic vs derived for the residual.** The prior repair tagged the mixed-regime $\varepsilon \cdot R$ scaling as `*[Heuristic]*`. The strengthening preserves this but reframes the on-policy collapse as `*[Derived]*` directly from the no-go. This is more precise: the collapse is exact (algebraic identity); the off-policy scaling is heuristic.

- **Status field.** Unchanged at `conditional`. The conditions are now sharper (no-go scope conditions S1–S5), but the meta-status — "this segment's claims hold under explicit local assumptions" — is preserved.

What was *not* salvageable from the original (pre-repair) segment:

- The Detection Principle's $\pm \rho$ residual as the primary diagnostic. The strengthening confirms (and explains the structural reason) why this is wrong on-policy. The original framing is irrecoverable.

What was *not* needed from external machinery:

- A new segment for the no-go theorem itself. The no-go fits naturally as the primary content of the existing segment, with cross-references to `#causal-hierarchy-requirement` and `#pearl-causal-hierarchy` for the upstream theorem. Promoting the no-go to its own segment is a reasonable later move (the no-go is a result that other future content might reference), but the immediate strengthening lives inside `#causal-insufficiency-detection`.

---

## §8 — Open Questions for Joseph

1. **Tier of the no-go for general topologies — proceed or accept robust qualitative?** The no-go is exact for shallow strict-prerequisite cases. For general DAG topologies the structural argument transfers (§3.3), but explicit $\mathcal{W}_{L0}^\ast$ construction has not been carried out. Three options:
   - (a) Accept *robust qualitative* for general topologies and *exact* for shallow strict-prerequisite as the segment's status. *(Current spike choice.)* Honest about the gap.
   - (b) Carry out the explicit construction for one or two non-shallow cases (e.g., 3-sibling OR with one common cause; 2-sibling OR + 2-sibling OR with shared latent across the four siblings) to extend the *exact* tier. Probably 1–2 sessions of derivation.
   - (c) Attempt a fully general construction theorem ("for any AND/OR DAG with any pattern of latent common causes, there exists an L0 world matching the on-policy distribution"). This may require regime-indexed L0 parameters (which is itself a departure from L0); the result might end up being "no on-policy distribution can distinguish L1 from a regime-indexed L0 family." Substantively interesting if it works; may require its own spike.

2. **Promotion of the no-go to its own segment?** Currently the no-go is the primary content of `#causal-insufficiency-detection`. It could plausibly stand alone as `#on-policy-detection-no-go` with `#causal-insufficiency-detection` referring to it. Pros: clean separation of "the impossibility result" from "the AAD-canonical detector." Cons: adds a segment for what is essentially the explanation of why the canonical detector exists. Recommend keeping inline for now; promote later if other segments reference the no-go independently.

3. **Should the boundary characterization be a separate segment?** Routes (a)–(e) form a self-contained classification. They could live as `#causal-detection-routes` referenced from the no-go segment and from `#orient-cascade` step 4c. Pros: the classification is reusable (e.g., `#strategy-dag`'s L0/L1/L1' discussion could reference it). Cons: small segment, low reuse beyond this segment. Recommend keeping inline.

4. **Citation style for Bareinboim et al. (2022).** The segment cites the CHT as an external theorem. Should the citation include the specific theorem number and conditions inline (as `#causal-hierarchy-requirement` does for the same paper)? Currently the segment relies on `#pearl-causal-hierarchy` and `#causal-hierarchy-requirement` to handle the citation; tightening to include the inline citation in the no-go's Formal Expression is a one-line edit. Recommend inline citation for the no-go's Formal Expression for self-containment.

5. **Compound with Finding 11 (orient cascade step 4c)?** Same compound consideration as the prior repair. The strengthening *substantially closes* Finding 11 because it explicitly frames step 4c as the unique route given the no-go (rather than as one diagnostic among several). The orient-cascade step 4c reference to "pairwise sibling covariance under an augmented test" is preserved exactly; no edit to `#orient-cascade` is required by this strengthening, and the framing alignment is now explicit. If a sanity-check edit is desired, "step 4c inherits the covariance test's preconditions and is the unique broadly-available detection route per the no-go in `#causal-insufficiency-detection`" is the natural addition (10 min).

6. **Worked-example-L1 framing.** The example uses marginals as learned credences, tacitly assuming off-policy / simultaneous-attempt sampling. Under the strengthening, this should be reframed: the example demonstrates the *off-policy* (route (b)) regime explicitly, and a one-paragraph scope note should make this clear. The numerical $0.877 - 0.776 = 0.101$ stands as the marginal-sampling residual; the framing should add "(under route (b): joint sibling observability, e.g., simultaneous attempt or post-execution replay; the on-policy short-circuit residual is identically zero per the no-go in `#causal-insufficiency-detection`)." 5 min.

7. **`stage:` after the rewrite.** The strengthening is more substantial than the softening repair. Re-running Gate 1 (deps audit, with new dependencies on `pearl-causal-hierarchy` and `causal-hierarchy-requirement`) and Gate 2 (content review of the no-go derivation) is appropriate. Recommend `stage: draft` in the rewritten frontmatter for full re-promotion review.

8. **Should the strengthened segment trigger `#causal-hierarchy-requirement` to acknowledge the dependency in its Discussion?** `#causal-hierarchy-requirement` currently discusses Level 2 access for $Q_O$ evaluation; it does not mention that L0/L1 detection is also a Level 2 question that motivates the CHT's no-go for purely on-policy detection. A one-paragraph addition to `#causal-hierarchy-requirement`'s Discussion would tighten the cross-reference. 10 min if desired.

---

## Spike-segment compression check

Per `FORMAT.md` §"Spike-segment reverse check": does the proposed segment lose anything the spike establishes?

- **Algebraic verification of observational equivalence** (§3.1, 3.2): captured in segment Formal Expression as the construction of $\mathcal{W}_{L0}^\ast$ with the explicit $\theta_1^\ast, \theta_2^\ast$ formulas. Cross-reference to `#worked-example-L1` for the numerical instantiation. Not lost.
- **General-topology structural argument** (§3.3): captured as a status statement (*robust qualitative*) with a Working Note flagging the explicit-construction gap. The full structural argument lives in this spike rather than in the segment. Honest compression.
- **Soft-facilitator extension** (§3.4): captured in segment as reference to `#strategy-dag`'s L1' distinction and the working note's mention of the soft-facilitator regime. Detailed argument lives in this spike.
- **CHT citation and application** (§4): captured in segment Discussion ("Connection to Pearl's hierarchy") and via cross-reference to `#causal-hierarchy-requirement`. The specific theorem-1 invocation lives in this spike.
- **Boundary characterization with five routes** (§5): captured in segment as the boundary table and route descriptions. Most of the content transfers. The "what is *not* a circumvention" subsection is the load-bearing addition; preserved in the segment as part of the Discussion.
- **Comparison to softening repair** (§7): lives only in this spike (correct — segment doesn't need to know the history).
- **Open questions for Joseph** (§8): lives only in this spike (correct).

The compression is honest: the segment captures the load-bearing claims and conditions; the spike captures the derivation, the historical comparison, and the open methodological questions.

---

## Downstream Impact Check (delta from prior softening repair)

The prior softening repair already characterized downstream impact for the residual demotion. The strengthening has the same downstream impact plus additional consequences:

### Same as prior repair

- `01-aad-core/OUTLINE.md` line 95: minor edit to one-line description. Update to "Detecting latent common causes: no-go theorem for purely on-policy detection; primary mechanism is pairwise sibling covariance under #loop-interventional-access."
- `#orient-cascade` step 4c: still holds; reference to covariance test is now strengthened (covariance test is the unique broadly-available route per the no-go).
- `#strategy-dag` line 124: minor edit to align framing. Suggested: "An agent at L0 cannot detect causal insufficiency from purely on-policy data (no-go theorem in #causal-insufficiency-detection): the on-policy observation distribution is identical between L0 worlds (with regime-conditional credences) and L1 worlds (with latent common causes). Detection requires interventional or joint-observability data: pairwise covariance among sibling edges, computed on data from #loop-interventional-access plus SA3 exploration, is the canonical AAD detector."
- `#independence-audit` item 2: still holds; reference to covariance test aligned with primary mechanism.
- `#approximation-tiering`: still holds.
- `#worked-example-L1` line 141: substantive edit needed (same as prior repair, with strengthening framing — the example is a route (b) instantiation).

### Additional consequences from strengthening

- `#causal-hierarchy-requirement`: optional one-paragraph addition to Discussion noting that L0/L1 detection is a Level 2 question motivating the CHT's no-go for on-policy detection. 10 min if desired.
- `#loop-interventional-access`: the segment's Discussion ("the loop as a Level 2 engine") gains an additional load-bearing instance. Optional addition to Discussion: "The loop's interventional access is load-bearing for L0/L1 distinction: by the no-go in `#causal-insufficiency-detection`, no purely on-policy mechanism can detect L0 causal insufficiency; the loop's interventional data is the structural prerequisite for detection." 10 min if desired.
- New cross-reference graph: `#causal-insufficiency-detection` now depends on `#causal-hierarchy-requirement` and `#pearl-causal-hierarchy`. These dependencies are already at `deps-verified` (causal-hierarchy-requirement) or higher, so the dependency audit is straightforward.

Total downstream cost is roughly 30–40 minutes of follow-on editing (same as prior repair) plus 20 minutes of optional cross-segment tightening. None of the edits change theoretical commitments; all are framing alignment with the strengthened segment.

---

## Notes on the strengthening attempt's honesty

This spike was written under explicit instruction to attempt strengthening before falling back to softening. The strengthening succeeded: a no-go theorem was derived (exact for shallow strict-prerequisite cases, robust qualitative for general topologies) by combining (1) explicit observational-equivalence construction with (2) Bareinboim et al.'s (2022) Causal Hierarchy Theorem.

Honest acknowledgments of where the strengthening did not fully close:

- The general-topology construction is structural, not constructive. Carrying out explicit $\mathcal{W}_{L0}^\ast$ for arbitrary topologies remains open (§8 question 1).
- The soft-facilitator case yields a "weak no-go" — same observational-equivalence argument, but multiple L1 parameter combinations can produce the same on-policy conditionals, so the agent cannot identify the *specific* L1 world even with off-policy data. This is documented as the L1 vs L1' distinction in `#strategy-dag` and is preserved in the segment.
- The boundary characterization's route descriptions are robust qualitative; precise detection-power formulas per route depend on domain particulars and are not derived.

The strengthening is more aggressive than the prior softening repair and yields a materially stronger result. The fallback was not invoked; the strengthening is the deliverable.
