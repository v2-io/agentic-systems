# Reflection: scope-edge-update-causal-validity

**1. Predictions vs evidence.**
I predicted the segment would formalize the Identifiability Coefficient $\iota_{ij}$ and define the conditions under which an edge update is actually causally valid. It delivers exactly this, outlining conditions C1 (Action control), C2 (Attributable outcome), and C3 (Varied execution).

**2. Cross-segment consistency.**
It perfectly mirrors the CIY Observational Regimes (A, B, C) from Chapter 2, mapping them directly onto the strategy edge update. The unification of the two sources of "Frozen Edges"—low Observability ($U_{\text{obs}} \to \infty$) from `der-observability-dominance` and low Identifiability ($\iota \to 0$) defined here—is extremely clean.

**3. Math verification.**
The proposed adjusted gain $\eta_{\text{eff}} = \frac{U_{\text{edge}}}{U_{\text{edge}} + U_{\text{obs}}} \cdot \iota_{ij}$ is mathematically sound. Since $\iota \in [0,1]$, it strictly attenuates the update rate when the agent is unsure whether it actually caused the observed outcome, preventing "superstitious learning" (confounding).

**4. What direction will the theory take next?**
The next segment is `disc-credit-assignment-boundary.md`, which is the final missing piece of the edge update story (how to compute the `signal` function).

**5. What errors should I now watch for?**
I must ensure that downstream analysis of deep planning doesn't assume that internal (non-leaf) nodes are easily updated. The segment proves that deeper edges suffer from compounding attribution uncertainty and confounding from below, driving $\iota_{ij} \to 0$ for edges near the root.

**6. Predictions for next segments.**
`disc-credit-assignment-boundary` will review the mathematical limits of Credit Assignment (likely pointing out that it is \#P-hard for general DAGs) and formally justify the gradient-based attribution scheme (from Prop B.5d) as the standard Level-1 approximation.

**7. What would I change?**
Nothing. The synthesis of the three costs of planning depth (Confidence Decay, Observability Necessity, Identifiability Degradation) is a brilliant capstone. It proves mathematically why human organizations flatten their hierarchies to stay agile.

**8. What am I now curious about?**
The Working Note suggesting that Regime C edges should be explicitly tagged as "observational" rather than "interventional". If a Strategy DAG contains both types of edges, the evaluation of the Value Object $V_O$ must somehow discount paths that rely on observational edges, because the agent cannot guarantee it can walk those paths via intervention.

**9. What new knowledge does this enable?**
It provides the formal vocabulary to distinguish between "I couldn't see the result" (Observability) and "I saw the result but don't know who caused it" (Identifiability).

**10. Should the audit process change?**
No.

**11. What changes in my outline for the final report?**
Note the $\iota_{ij}$ coefficient as the formal safeguard against superstitious learning in multi-parent graphs.

**12. How valuable does this segment feel to me?**
Very high. It scopes the heuristic update rule securely inside Pearl causality.

**13. What does the framework now potentially contribute to the field?**
It mathematically formalizes why deep strategic goals (like "increase corporate revenue") are almost impossible to learn causally, while shallow actions (like "change button color") are trivial to learn.
