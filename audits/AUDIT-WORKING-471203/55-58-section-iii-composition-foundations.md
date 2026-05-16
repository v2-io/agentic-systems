# Reflection: §III composition foundations (4 segments)

Covers `#scope-multi-agent`, `#scope-composite-agent`, `#hyp-symbiogenic-composition`, `#form-composition-closure`. The composition-closure segment is the substantive load-bearing one — large, multi-Findings, with the full bridge lemma and tier classification.

## Standout observations

**(A) `#scope-composite-agent`'s four routes** (C-i shared objective, C-ii hierarchical derivation, C-iii mutual benefit, C-iv equilibrium-convergent strategic interaction). The (C-iv) addition is sophisticated — adversarial pairs that admit Nash / VI / regret-minimization CCE convergence count as *strategic composites* with equilibrium-based macro-state. This admits a class of adversarial systems into the composition machinery that pure-alignment routes (C-i)-(C-iii) would exclude. The disjunctive form is honest — the four routes are not unified into a single scalar.

**(B) `#form-composition-closure`'s bridge lemma is well-defended.** The DA2'-inc (incremental sector bound) is correctly identified as strictly stronger than (A4)'s one-point sector bound. The Tier 1/2/3 classification (contraction proved / local / per-domain) is structurally clean. The DA2'-inc ≡ (CT2)-at-$M=I$ equivalence converts what would be "theorem-imported from Lohmiller-Slotine" into "AAD-internally derived via standard monotone-operator identity" — structural transparency, not new content.

**(C) The two-Kalman $\varepsilon^\ast = 0$ result is structurally important.** Two non-communicating Kalman filters tracking correlated random walks have $\varepsilon^\ast = 0$ at *all* correlations under the means-only projection. The "cost of independence" (suboptimality vs joint filter) is a *performance gap*, not a closure defect. **The composition-closure framework diagnoses representability, not optimality.** This is exactly the right scope-honesty move.

**(D) `#hyp-symbiogenic-composition`** as the formal mechanism by which composites *come into being*. Three coupled dynamics: (S-1) objective absorption, (S-2) function transfer, (S-3) autonomy reduction. The connection to `#deriv-critical-mass-composition`'s asymmetric weighted-Lyapunov limit ($\alpha_2 \to 0$, $\mu \to 0$) formalizes (S-3) as smooth deformation of (CM4). The mechanism is well-attested empirically (mitochondria, firm acquisitions, language adoption) but formally underspecified — appropriate robust-qualitative status.

**(E) Per-macro-step formulation with timescale ratio $K_c$.** The 2026-04-22 repair fixes the dimensional inconsistency between $\varepsilon^\ast$ (was per-micro-step) and $\rho_\xi = \varepsilon^\ast \nu_c$ (rate units). The macro-step formulation handles both $K_c = 1$ (synchronous) and $K_c \gg 1$ (hierarchical) cleanly. Honest engineering.

## Adversarial observations

**On (C-iv) strategic composites:** the route admits adversarial pairs *only when* they admit potential-game (Monderer-Shapley 1996) or monotone-game (Rosen 1965) structure. **Most real adversarial dynamics don't satisfy these:** cyclic best-response in zero-sum without pure Nash; non-convex strategic interactions; iterated dilemmas without unique equilibria. The framework's honest sub-scope $\beta'$ exit (VI existence + CCE set-convergence only for non-potential non-monotone games) acknowledges this. **§F observation candidate:** the strategic-composite machinery covers a narrower slice of adversarial systems than the (C-iv) framing suggests; the practical implication is that most adversarial systems remain in `#scope-multi-agent` (handled by `#der-adversarial-destabilization` agent-level machinery) rather than as strategic composites.

**On the Tier 1/2/3 bridge-lemma classification:** Tier 1 (contraction proved) covers Bayesian / convex / linear-PD agents. Tier 3 (per-domain verification) covers non-convex / discontinuous / non-mismatch-driven. **Most LLM-based composite agents are Tier 3** — transformer attention is non-convex, prediction models are nonlinear, update dynamics aren't naturally mismatch-driven. The framework's strongest results don't apply *exactly* to the most consequential modern composites. The Tier 2/3 results (local with degradation; per-domain) do apply but with caveats.

**On (P1) computability:** the information-preservation condition requires conditional MI over joint distributions. **Tractable only for linear-Gaussian systems** (closed-form). For general systems, requires Monte Carlo or variational bounds. The two-Kalman case is the only verified instance. Practical applicability is limited to a narrow class of systems.

**On the $N$-agent scaling open question:** the segment explicitly flags "Whether the closure defect scales polynomially or exponentially with $N$" as open. **This is the structural test** of whether very large teams can be treated as single agents at all. The framework provides the framework but not the answer.

**On `#hyp-symbiogenic-composition`'s formal underspecification:** the three dynamics (S-1, S-2, S-3) are *proposed schemas, not results*. The symbiogenic mechanism is well-attested empirically but the framework gives no quantitative predictions (when symbiogenesis is favored over peer coupling; what governs consolidation timescale; under what conditions reverses). The scope-honesty (robust qualitative) is appropriate but the framework doesn't yet operationalize this.

## Felt value

**Very high** on the composition-closure segment for the structural-completeness of the framework (closure defect + admissibility + bridge lemma + tier classification + worked example). **High** on `#scope-composite-agent` for the (C-iv) addition. **Mid-high** on `#hyp-symbiogenic-composition` for the empirical scope despite formal underspecification. **Mid** on `#scope-multi-agent` for routing-structure precision (goal-blind routing distinction).

## Continuing

Going to skip ahead to the substantive Section III adversarial-dynamics segments (`#der-adversarial-destabilization`, `#result-adversarial-tempo-advantage`, `#der-interaction-channel-classification`, `#der-agent-opacity`) since they're the highest-leverage adversarial-reading territory. Then sample Appendix A's bias-bound and persistence-cost (the structurally distinctive ones I've cross-referenced multiple times). Then 02-tst-core / 03-logogenic / 04-logozoetic.
