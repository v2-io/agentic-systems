# 27 — der-gain-sector-bridge

*Type: derived. Status: conditional. Stage: claims-verified. Depends: [emp-update-gain, def-mismatch-signal, form-sector-condition, deriv-gain-sector].*

## Predictions vs evidence
Predicted: derivation of $\alpha = \eta^* c_{\min}$ from B1 directional fidelity. Found: that, plus extensive Verified Instances table + Fisher-metric (PI)-forced upgrade + five named failure modes.

## **Math verification (key claim — one-point sector strictly weaker than strong convexity)**
Counterexample at line 49: $L'(x) = x(1 + (1/2)\sin(10x))$.
- $x \cdot L'(x) = x^2(1 + (1/2)\sin(10x)) \in [x^2/2, 3x^2/2]$, so $\geq x^2/2$ — one-point sector holds with $\alpha = 1/2$. ✓
- $L''(x) = 1 + (1/2)\sin(10x) + 5x\cos(10x)$.
- At $x = \pi/10$: $L''(\pi/10) = 1 + 0 + 5(\pi/10)(-1) = 1 - \pi/2 \approx -0.5708 < 0$. ✓
- Therefore $L$ is not convex on any neighborhood of $x^* = 0$. ✓

**Counterexample verified — one-point sector at equilibrium ≠ local strong convexity.**

## Math verification (Verified Instances)
- Scalar Kalman: $K = P^-/(P^- + R_\text{obs}) = U_M/(U_M + U_o) = \eta^*$. ✓
- Matrix Kalman: $\lambda_{\min}^+(KH)$ in $(P^-)^{-1}$-norm. ✓
- Beta-Bernoulli: edge update rate $1/(n+1)$. ✓
- Exponential family natural params: $\eta\mu_0$ with $\mu_0 = \inf_{\Theta_0}\lambda_{\min}(\mathbf{I})$. ✓
- Strongly convex gradient: $\eta\mu$ via Nesterov. ✓
- L2-regularized: $\eta\lambda$ floor. ✓

## Prose-coherence — strong
- Bidirectional ⇔ one-directional distinction (two-point sector vs one-point sector) is handled with surgical precision — strong convexity ⇒ one-point sector, but reverse fails (counterexample). Nesterov 2004 Thm 2.1.10 correctly cited.
- Fisher-metric upgrade under (PI) + Čencov 1982 (line 108-115) — names that the matrix-Kalman row is *natively* in $(P^-)^{-1}$, and under (PI) axiom is *forced* there. Eliminates the $\kappa(P^-)$ Euclidean-transfer penalty.
- Five failure modes (line 64-76) catalogued: directional infidelity, gain collapse, nonlinear saturation, unobservable directions, model misspecification.

## Cross-segment consistency
Forward-refs `#deriv-sector-condition`, `#deriv-discrete-sector-condition`, `#form-composition-closure`, `#der-observability-dominance`, `#result-structural-adaptation-necessity`, `#deriv-gain-sector` (appendix), `#scope-agent-identity` (for the (PI) axiom), `#disc-additive-coordinate-forcing`, `#deriv-strategy-cost-regret-bound`, `#deriv-edge-update-natural-parameter`. Coherent.

## Watch list
- The (PI) parameterization-invariance axiom is claimed to live in `#scope-agent-identity` (line 108). Verify when I reach that segment.
- The chain-rule-additivity / divergence / update / Fisher coordinate-forcing claim chain — touches `#disc-additive-coordinate-forcing` and `#deriv-strategy-cost-regret-bound` and `#deriv-edge-update-natural-parameter`. The "1-anchor-plus-3-theorem structure" mentioned in OUTLINE's Meta-Architecture I should consolidate this.

## Next-segment predictions
`#result-sector-condition-stability`. Will state the nonlinear persistence (Lyapunov) result using A2'. Status likely `exact`. Will state Prop A.1 (ultimate boundedness under Model D) and Prop A.1S (Model S).

## Brief wandering
The Fisher-metric (PI)-forcing argument is one of the most elegant moves in the framework. It says: rather than picking $(P^-)^{-1}$ inner product as a *modeling choice* and paying the Euclidean-transfer penalty, the framework's parameterization-invariance axiom + Čencov 1982 uniqueness theorem *forces* the Fisher metric. The framework gets exact sector-constants in the natural metric instead of approximate sector-constants in Euclidean. Methodologically clean.
