---
slug: result-section-ii-survival
type: result
status: conditional
depends:
  - scope-logogenic-agent
  - def-coupled-update-dynamics
  - der-directed-separation
  - form-complete-agent-state
  - def-agent-spectrum
  - form-objective-functional
  - def-value-object
  - def-strategy-dimension
  - der-causal-hierarchy-requirement
  - der-loop-interventional-access
  - scope-ciy-observational-proxy
  - disc-ciy-unified-objective
  - norm-explicit-strategy-condition
  - der-chain-confidence-decay
  - scope-and-or
  - def-strategy-dag
  - def-satisfaction-gap
  - def-control-regret
  - def-strategic-calibration
  - der-orient-cascade
  - der-observability-dominance
  - hyp-edge-update-via-gain
  - scope-edge-update-causal-validity
  - disc-credit-assignment-boundary
  - form-structural-change-as-parametric-limit
  - schema-strategy-persistence
stage: draft
---

# Result: Part II Survival Classification

Of Part II's 24 results, 16 survive exactly for Class 3 (Coupled) agents, 5 survive approximately with bounded error, 2 require modification, and 1 fails by definition. The damage from dropping directed separation is concentrated in the *processing dynamics* — the ordering of updates and the accuracy of individual update steps — not in the *definitional and structural* architecture.

> [!warning]
> **Goal-Update Coupling Class numbering changed 2026-05-09.** Anything older than git tag `pre-guc-rename-2026-05-09` uses the old Class numbering:
>
> | historical | actual current     | sometimes AKA  |
> | ---------- | ------------------ | -------------- |
> | Class 1    | GUC Class 1: Separated | Modular        |
> | Class 2    | GUC Class 3: Coupled   | Undirected     |
> | Class 3    | GUC Class 2: Partial   | Operational    |

## Formal Expression

*[Derived (section-ii-survival, from segment-by-segment analysis of directed-separation dependency)]*

### Classification

Each Part II result is classified by whether its statement or derivation references directed separation, and if so, whether the result can be recovered in the coupled formulation.

**SURVIVES EXACTLY (16):** The result does not reference directed separation in its statement or derivation. It holds for any agent with $X_t = (M_t, G_t)$, regardless of how the update factorizes. (Applies to Class 3 (Coupled) agents — logogenic territory.)

| # | Segment | Rationale |
|---|---------|-----------|
| 1 | #def-agent-spectrum | Classifies by what information is maintained, not how it is processed |
| 2 | #form-objective-functional | Defines evaluation interface $V_{O_t}$; no processing dependency |
| 3 | #def-value-object (definitions only) | $V_O$ and $Q_O$ as conditional expectations are agnostic to how $M_t$ was produced. **Partial.** The *causal-validity* claim — that $Q_O$ depends on $M_t$ alone as a state variable — is conditional on directed separation ( #def-value-object Epistemic Status) and degrades for Class 3 (Coupled) agents because $M_t$ carries goal-conditioned bias. Definitions survive exactly; the causal-validity layer does not. Count this as half-exact, half-approximate. |
| 4 | #def-strategy-dimension | Structural decomposition $G_t = (O_t, \Sigma_t)$; definitional, not dynamic |
| 5 | #der-causal-hierarchy-requirement | Evaluating $Q_O$ requires Level 2 queries; property of the question type, not the processing |
| 6 | #der-loop-interventional-access | The feedback loop provides interventional data by construction; architecture-independent |
| 7 | #scope-ciy-observational-proxy | Admissibility regimes (A/B/C) are domain properties, not agent-architecture properties |
| 8 | #disc-ciy-unified-objective | Policy objective structure (exploit + explore) exists for any learning agent |
| 9 | #norm-explicit-strategy-condition | Cost comparison $C_{\text{plan}} + C_{\text{maintain}} \lt C_{\text{explore}} + C_{\text{repair}}$ is architecture-independent |
| 10 | #der-chain-confidence-decay | $\log P(\text{chain}) = \sum_i \log P(E_i \mid E_{\lt i})$ — mathematical identity |
| 11 | #scope-and-or | Scope restriction on strategy representation; constrains $\Sigma_t$, not $f_M$ |
| 12 | #def-satisfaction-gap | Definition: $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O(M_t; \Pi, N_h)$; computed from $(M_t, V_{O_t})$ regardless of provenance |
| 13 | #def-control-regret | Definition: $\delta_{\text{regret}} = A_O - V_O(M_t, \pi_{\text{current}}; N_h)$; same reasoning |
| 14 | #der-observability-dominance | When $\sigma_v \approx 0$, $\eta_{\text{edge}} \to 0$; information-channel property |
| 15 | #scope-edge-update-causal-validity | Conditions (E1)–(E3) and regimes (A/B/C) are domain/interface properties |
| 16 | #disc-credit-assignment-boundary | DAG inference structure; "persistence is credit-assignment-free" (Prop B.5) holds for Class 3 (Coupled) |

Additionally, the DAG *structure* of #def-strategy-dag (acyclicity, propositional nodes, AND/OR combination, status propagation) survives exactly — these are properties of the strategy representation, not of the processing architecture.

**SURVIVES APPROXIMATELY (5):** The result's statement is exact under directed separation and becomes an approximation when directed separation fails, with error depending on $\kappa_{\text{processing}}$. (Applies to Class 3 (Coupled) agents — logogenic territory.)

| # | Segment | Source of approximation | Error structure |
|---|---------|------------------------|-----------------|
| 1 | #form-complete-agent-state | Factorized update dynamics | $\lVert f_X - (f_M, f_G \circ f_M)\rVert = O(\kappa)$; at $\kappa \approx 1$ the factored form is not useful |
| 2 | #def-strategic-calibration | Residual conflated with $M_t$ bias from goal-conditioning | $b_{ij} = O(\kappa \cdot \text{ambiguity}(e_\tau))$; see #scope-observation-ambiguity-modulation |
| 3 | #hyp-edge-update-via-gain | Signal function is goal-conditioned | Gain formula's form is robust; magnitude biased by $O(\kappa \cdot \text{goal-evidence correlation})$ |
| 4 | #schema-strategy-persistence | Sector parameter degraded by goal-conditioned signals | $\alpha_\Sigma^{\text{eff}} \leq \alpha_\Sigma - O(\kappa^2)$; persistence threshold harder to satisfy |
| 5 | #def-strategy-dag (credence conditioning) | Leaf and edge credences conditioned on full $X_t$ rather than $M_t$ alone | Credences may exhibit goal-dependent bias; see below |

**REQUIRES MODIFICATION (2):** (Applies to Class 3 (Coupled) agents — logogenic territory.)

| # | Segment | What changes |
|---|---------|-------------|
| 1 | #der-orient-cascade | Sequential ordering derived from unidirectional information dependency → replaced by coupled resolution with post-hoc diagnostic decomposition. Ordering survives as normative design pattern, not derived result. See #result-coupled-diagnostic-framework. |
| 2 | #def-strategy-dag (credence mechanism) | Leaf credences $p_v(M_t) \to p_v(X_t)$; edge credences $p_{ij}(M_t) \to p_{ij}(X_t)$. Credences become explicitly conditioned on the full state, reflecting goal-dependent assessment. |

**FAILS (1):** (Applies to Class 3 (Coupled) agents — logogenic territory.)

| # | Segment | Reason |
|---|---------|--------|
| 1 | #der-directed-separation | This is the result that defines the Class 3 (Coupled) boundary. It fails by construction for Coupled agents. |

### Scorecard

$$\text{Exact: } 15.5/24 \qquad \text{Approximate: } 5.5/24 \qquad \text{Modified: } 2/24 \qquad \text{Fails: } 1/24$$

**Note on the fractional counts.** #def-value-object is counted as half-exact (its definitions survive) and half-approximate (its causal-validity layer is conditional on directed separation and degrades for Class 3 (Coupled) agents). Most segments split cleanly into one category; #def-value-object does not. The scorecard's total stays at 24 to match the segment count but the fractional count acknowledges that a clean integer bucketing understates the qualitative complexity for segments whose definitions and dynamics live at different tier levels.

### Structure of the approximate results

*[Derived (approximation-error-structure, from analysis of goal-information leakage)]*

For the five approximately surviving results (in Class 3 (Coupled) agents), the fundamental error source is goal-information leaking into the epistemic update. Two quantities have to be kept apart here, and each has its own symbol. The belief's **goal-dependence** is the displacement of the goal-conditional post-update law from the goal-marginal one,

$$\lVert\Delta M_{\text{bias}}(G)\rVert \;:=\; d\big(P_{M_{\tau^+} \mid e_\tau, M_{\tau^-}, G},\; P_{M_{\tau^+} \mid e_\tau, M_{\tau^-}}\big),$$

the quantity #deriv-observation-ambiguity-bias-bound defines and bounds in expectation by the transferred goal information, $\kappa_{\text{processing}} \cdot H_\rho(G_t) = I_\rho(G; M_{\tau^+} \mid e_\tau, M_{\tau^-})$ under the probe law of #der-directed-separation (the goal varied at fixed inputs): in the Fisher–Rao metric $\mathbb{E}\,\lVert\Delta M_{\text{bias}}\rVert_{FR} \leq 2\sqrt{I}$ globally and $\sqrt{2}\sqrt{I}\,(1 + o(1))$ in the small-information regime, and a $W_2^2$ form linear in $I$ under a log-Sobolev condition. It is zero at $\kappa = 0$ and it saturates for any noiseless coupling, however small, because mutual information measures the goal's recoverability and not the belief's displacement. The belief's **distortion** is its divergence from the calibrated belief $\pi$, the conditional law of the world given the information the agent holds,

$$D_G \;:=\; \mathrm{KL}\big(\pi \,\Vert\, M_{\tau^+}^{(G)}\big) \quad\text{or}\quad \mathrm{TV}\big(M_{\tau^+}^{(G)}, \pi\big),$$

the quantity #scope-observation-ambiguity-modulation defines: zero for calibrated goal-dependent allocation, bounded model-free only by the size of the reweighting the processor applies ($\mathrm{TV} \leq L_G / 4$ for a log-density ratio of range $L_G$), and under that segment's fixed-gain tilt hypothesis bounded exactly by the gain and the residual spread of the goal-relevant quantity under $\pi$ (Bennett's lemma), which is where the familiar engineering fact lives: binary, verifiable observations pin the quantity the goal cares about and leave a tilt nothing to act on, whatever $\kappa$ is. That sharpness dependence is a hypothesis with a regression test, not a theorem.

A third quantity, the coupled update minus the goal-blind update $f_X^M(X_{\tau^-}, e_\tau) - f_M(M_{\tau^-}, e_\tau)$, is neither of these and is not used here: a goal-blind update is itself per-goal miscalibrated when it drops the realized action or when the goal carries world information ( #der-directed-separation, Scope Condition), so its distance from the coupled belief does not measure how wrong the coupled belief is. What makes a Part II diagnostic read *wrong*, rather than merely goal-dependent, is the distortion. For a diagnostic $A$ that is $L_A$-Lipschitz in the belief in the metric $d$, the error of its coupled reading relative to its reading off the calibrated belief is $\lvert A(M_{\tau^+}^{(G)}) - A(\pi)\rvert \leq L_A \cdot d(M_{\tau^+}^{(G)}, \pi)$, bounded by the distortion; under (NWI) the calibrated belief is the goal-blind Bayes filter's, which is the "clean" reading the coupled-diagnostic framework compares against ( #result-coupled-diagnostic-framework). The approximation quality of the surviving results is therefore read in two parts: the diagnostics' *goal-dependence* is bounded through the displacement bound, and their *error* is governed by the distortion, whose dependence on observation sharpness is the hypothesis.

## Epistemic Status

*Conditional.* The classification is conditional on: (1) the segment-by-segment analysis of each result's dependency on directed separation, and (2) the correctness of the underlying Part II results themselves. The "survives exactly" classifications are the strongest — they follow directly from verifying that the result's statement and derivation do not reference directed separation. The "survives approximately" classifications depend on two bounds with different standing. The diagnostics' *goal-dependence* is bounded by the displacement bound of [#deriv-observation-ambiguity-bias-bound](../../01-aat-core/src/deriv-observation-ambiguity-bias-bound.md), a conditional theorem under its named sub-scopes (Track 1, $W_2^2$ linear in the transferred information under a log-Sobolev condition; Track 2, Fisher–Rao with the global constant $2$ and the sharp local constant $\sqrt 2$ under (PI)+Čencov). The diagnostics' *error* is bounded by the distortion, whose model-free range bound is exact and whose dependence on observation sharpness is the fixed-gain hypothesis of [#scope-observation-ambiguity-modulation](scope-observation-ambiguity-modulation.md); so the approximation *error* of a surviving result is a conditional theorem only in the size of the processor's reweighting, and its dependence on the domain is a hypothesis with a test.

Max attainable: conditional. The classification's epistemic ceiling is determined by the underlying Part II results. If a Part II result is itself discussion-grade (e.g., #def-strategic-calibration), its survival classification inherits that status.

## Discussion

**Why the majority survives.** The survival rate (16/24 exact) reflects a structural property of AAT's design: Part II's *definitional architecture* — what states exist, how they decompose, what evaluation means, what the strategy represents — is about the *structure of purposeful agency*, not about the *processing architecture*. Directed separation is about how the state is *updated*, not about what the state *is*. Results that define objects ($V_{O_t}$, $\delta_{\text{sat}}$, $\delta_{\text{regret}}$, $\Sigma_t$ as DAG) or establish architectural requirements (causal hierarchy, interventional access) are processing-agnostic by construction.

**Where the damage is concentrated.** The five approximate results and two modified results all concern *dynamics* — how the state evolves, how edge credences are updated, how the orient cascade resolves, whether the strategy persists. These are precisely the results that depend on how the update factorizes. The pattern: *statics survive; dynamics degrade.*

**Implications for logogenic agent engineering.** The 16/24 exact-survival count is a *statement-level* result: these results' formal claims do not invoke directed separation, so their definitions and structural classifications carry over to Class 3 (Coupled) agents. This is not the same as *operational extractability* — the claim that an LLM agent system designer can *compute* these quantities at runtime without additional machinery. Operational extractability requires separate instrumentation: the satisfaction gap $\delta_{\text{sat}}$ is formally well-defined for a Class 3 (Coupled) agent, but computing it requires that $V_{O_t}^{\min}$ and $A_O$ actually be available to the agent's reasoning loop. For LLM-based agents this generally means explicit instrumentation beyond the agent's internal state — commit messages, PR descriptions, structured reasoning traces, external monitoring streams — that materialize the quantities the theory references. #scope-logogenic-agent discusses this distinction as the mapping from LLM interaction to AAT's formal objects; #def-coupled-update-dynamics treats the identification $X_t = (M_t, G_t)$ as approximate and analytical rather than computable. The instrumentation-boundary framing in `02-tst-core/`'s `#obs-software-epistemic-properties` P5 is the parallel observation in the software domain: statement-level survival does not imply that the quantities are cheap or automatic to extract.

So: Part II's *conceptual architecture* applies to Class 3 (Coupled) agents (16/24 exact survival is a claim about this), but Part II's *operational deployment* on Class 3 (Coupled) agents requires additional instrumentation whose design is the subject of `03-llm-core/` more broadly. The engineering challenge is therefore two-part: (a) minimizing goal-conditioned bias in the coupled update so the inherited structural results remain quantitatively accurate, and (b) instrumenting the agent system so the results' quantities are computable at all. The second is not a failure of the theory; it is the work the theory identifies as necessary for its application.

**The $\kappa^2$ result for strategy persistence.** The strategy persistence schema's sector parameter degrades as $O(\kappa^2)$, not $O(\kappa)$, because the bias must both enter the signal and survive the sector-condition averaging. This means Class 3 (Coupled) agents need faster correction rates — equivalently, they tolerate lower strategic disturbance rates — to achieve the same persistence guarantees. The squared dependence is a tighter result than the linear dependence of the other approximate results; it arises from the specific structure of the sector condition's inner-product averaging.

## Working Notes

- The classification counts #def-strategy-dag twice (once for the structure, which survives exactly, and once for the credence mechanism, which requires modification). The scorecard counts these as contributing to both categories. One could instead count #def-strategy-dag once as "survives approximately" (the weakest classification applying to any part of the result). The two-part count is more informative.
- **Regression guard.** $\Delta M_{\text{bias}}$ means one thing here, the goal-dependence displacement of #deriv-observation-ambiguity-bias-bound; the error of a diagnostic is bounded by the distortion $D_G$, not by the displacement, and not by a distance to the goal-blind update. Do not restore a product law $\kappa \cdot I(G; \Omega_\tau \mid \cdot)$ or $\kappa \cdot \mathcal A$ in any form.
- The "fails" category contains only #der-directed-separation itself. One might argue this is not a "failure" but a "scope exit" — the result defines the boundary, and Class 3 (Coupled) agents are outside it. The classification is stated as "fails" for symmetry with the other categories, but the semantic content is "inapplicable by design."
- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Logogenic agents are now Class 3 (Coupled), not Class 2. Every "Class 2" in this segment pre-rename referred to logogenic/fully-merged agents and now reads Class 3 (Coupled). Warning callout placed at top of segment (per plan §6 — heavy archaeological cross-reference target). Removed at `candidate` stage per FORMAT.md Gate 4.
