# 11 — form-information-bottleneck

*Type: formulation. Status: exact (for the IB-as-applied-theorem core). Stage: draft. Depends: [form-agent-model, def-action-transition].*

## Predictions vs evidence
Predicted: Tishby IB framework. Found: clean import with careful distinction between the formulation choice (IB vs MDL vs Bayesian-sufficiency) and the theorem (exact under the bindings).

## Cross-segment consistency
Forward-refs to `#def-model-sufficiency`, `#def-value-object`, `#def-shared-intent`, `#disc-compression-operations`, `#form-strategy-complexity-cost`, `#deriv-strategy-cost-regret-bound`, `#deriv-causal-ib-exploration`. Citations are well-sourced: Tishby/Pereira/Bialek 1999, Cover & Thomas, Friston 2010, Friston et al 2017, Parr & Pezzulo 2022, Alemi et al 2017, Tishby & Zaslavsky 2015, Tishby & Polani 2011, Rubin/Shamir/Tishby 2012, Levine 2018.

## Math verification
- IB Lagrangian: $\phi^* = \arg\min_\phi[I(M_t; \mathcal{C}_t) - \beta I(M_t; o_{t+1:\infty} \mid a_{t:\infty})]$. Standard Tishby form. ✓
- The Markov chain $Y - X - T$ with $(X, T, Y) = (\mathcal{C}_t, M_t, o_{t+1:\infty} \mid a_{t:\infty})$ holds because $M_t = \phi(\mathcal{C}_t)$ — $M_t \perp Y \mid X$. ✓
- The double-counting clarification (line 30-32): volatility $\rho$ natively degrades $I(\mathcal{C}_t; o_{t+1:\infty})$, so optimal $\phi^\ast$ automatically discards stale information without needing to adjust $\beta$. **Correct and methodologically important.** ✓

## Prose-coherence
Body is dense but well-organized — header preamble previews; Formal Expression carries the IB form + double-counting clarification; Discussion has four subsections (not prescriptive / model-sufficiency / policy-relativity / broader applicability) + the IT-MDP lineage subsection + variational free energy subsection. Light preamble-Discussion overlap; substantively complementary.

## Watch list
- **Type-vs-status tagging at exact-formulation.** Segment type `formulation` + status `exact` is unusual; the body reconciles this carefully (line 36) by distinguishing formulation-as-choice from theorem-as-imported. **This is a defensible novel pattern in the corpus.** Worth noting positively in §E "what holds" — the framework's distinction between "this *form* is a choice" and "given the choice, the *content* is exact" is methodologically precise.
- The $\beta$ vs $\rho$ double-counting argument (line 30-32) is *exactly* the kind of careful methodological move I'd want the framework to make. It defends against a natural-seeming-but-wrong claim ("agents should adjust $\beta$ as $\rho$ changes") with a structural argument.

## Next-segment predictions
`#def-model-sufficiency`. Will introduce $S(M_t) \in [0, 1]$ as the predictive-information ratio. Likely status `axiomatic` or `formulation`. Will reference `#form-information-bottleneck`.

## What I'd change
The IT-MDP-vs-IB lineage discussion (line 52) is excellent but very dense. Some readers will benefit from a small table summarizing the two lineages (IB = MI-to-observable; IT-MDP = KL-to-policy; both rate-distortion-derived; AAT uses both at different sites). Optional pedagogical polish; not a finding.

## Curiosity
The variational-free-energy connection (line 54) is handled with strong epistemic discipline — the framework adopts IB's rate-distortion form but explicitly declines to commit to active inference's stronger ontological stances ("borrows the form without committing to AI's preferences-as-priors stance or to expected free energy as master objective"). This is the kind of move that compounds — fresh readers know exactly where AAT agrees with FEP and where it deliberately doesn't.

## Wandering thoughts

**On the careful prior-art handling.** This segment is a small textbook example of how AAT integrates external machinery — Tishby's IB — without claiming novelty of the import. The status field is `exact`; the body honestly notes "this segment is *not* a novel formulation: it is an exact statement of [Tishby's] theorem under AAT's binding." Then the framework's specific contribution (the binding itself, the variational-free-energy positioning, the double-counting clarification) is articulated separately. This is exactly the methodological discipline `feedback_math_novelty_recognition.md` in MEMORY.md describes — recognizing both *imports as imports* and *applications as theorem-grade* without overclaim or underclaim.

**On the IB-vs-IT-MDP lineage handling.** Naming both lineages and placing them in the shared Shannon-rate-distortion ancestor is the kind of structural move that lets future segments use either form without confusion. The Discussion's line 52 explicitly says "Both lineages descend from Shannon rate-distortion theory and admit Lagrangian relaxation; the choice of fidelity term depends on whether the compressed variable should preserve information about an observable (IB form) or match a target policy (IT-MDP form)." This is the right framing.

**On the segment as a strong template.** I'd consider citing this segment in the §E "what holds" section of the FINAL as an exemplar of how external-machinery imports should look in AAT. The combination of (formulation-as-choice + exact-theorem-import + explicit lineage handling + double-counting clarification + variational-cousin positioning) is unusually well-executed.
