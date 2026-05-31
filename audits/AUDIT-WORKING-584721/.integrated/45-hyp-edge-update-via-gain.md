# Reflection 45 — hyp-edge-update-via-gain (Section II row 20)

## §4.2 dependency check

`depends: [def-strategy-dag, emp-update-gain, def-mismatch-signal, deriv-edge-update-natural-parameter, der-chain-confidence-decay]`. All read except deriv-edge-update-natural-parameter (Appendix A — appendix-back-pointer per §4.2 exception, can read in-context if needed; deferring as the segment is comprehensible without it). **No backward-dep, no F-A drift.**

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted: "gain principle applied to strategy edges; hypothesis-tier." ✓. Plus Beta-Bernoulli instantiation with exact conjugate gain $1/(n+1)$, log-odds parallel presentation, signal-function-at-theory-level resolution citing disc-credit-assignment-boundary.

**2. Cross-segment consistency.** Extensive cross-refs internal. The log-odds parallel presentation lands cleanly from deriv-edge-update-natural-parameter (recently-added 2026-04-23 per CLAUDE-2.md priming). The "evidential-additivity axiom" framing connects to additive-coordinate-forcing via der-chain-confidence-decay anchor. ✓

**3. Math verification (at discretion).** Beta-Bernoulli update $\Delta \hat p = (y - \hat p)/(n+1)$ with $n = \alpha + \beta$. Standard conjugate result. ✓

**4. What direction next?** Row 21 = `scope-edge-update-causal-validity`. Regime A/B/C identifiability per priming.

**5. What errors should I now watch for?**
- Treating the uncertainty-ratio gain as a literal algebraic formula for Beta-Bernoulli. The segment is explicit: structural principle, not universal algebraic formula.
- Conflating log-odds and probability-space presentations.
- Treating gradient signal as the unique valid signal function (one of multiple Level 1 options per disc-credit-assignment-boundary).

**6. Predictions for next segments.** Row 21 = `scope-edge-update-causal-validity`. Probably depends on def-strategy-dag, def-pearl-causal-hierarchy, or der-loop-interventional-access. Regime A/B/C with $\iota_{ij}$ identifiability coefficient.

**7. What would I change?** The "structural principle, not universal algebraic formula" framing for the gain principle is sharp scope-honesty. The Beta-Bernoulli case has the *exact* gain $1/(n+1)$ from conjugate analysis (not from a variance-ratio substitution). Important distinction that segments downstream should respect.

**8. What am I now curious about?**

(a) The **"$M_t$/edge double-counting"** concern in Working Notes — spike found "mostly unfounded with bounded self-correcting effect; cascade ordering (process $M_t$ first) is correct." This is a resolved-but-flagged-for-future-tracking concern. Worth checking whether the cascade-ordering enforcement is explicit in der-orient-cascade.

(b) The **"marginal point-estimate update is biased at truth (violates A1 with $O(1/n)$ bias)"** claim. This is the F1-territory connection — when an intermediate is unobservable, the marginal Bayesian update is biased. Connects to der-causal-insufficiency-detection (read).

(c) **Log-odds vs probability-space** as dual coordinates. Probability-space presentation is pedagogically cleaner (gain $1/(n+1)$ is exact); log-odds presentation is structurally cleaner (additive evidence accumulation). The "Fisher-equivalent for moment-parameter results" claim ties them together — they're not different theories, just dual coordinates.

**9. What new knowledge enabled.** Edge-update form via gain. Beta-Bernoulli exact instantiation. Log-odds dual presentation. Signal-function-at-theory-level resolution per disc-credit-assignment-boundary.

**10. Should the audit process change?** Continuing.

**11. Outline updates.** No new findings.

**12. How valuable does this segment *feel* to me?**

Medium. Hypothesis-tier extension of the gain principle. Structurally well-motivated; specific implementation domain-specific. The "exact gain from conjugate analysis, not literal variance-ratio formula" framing is sharp. The log-odds dual-presentation connection to additive-coordinate-forcing is structurally pleasing.

Magnitude: middle. Type: hypothesis-tier with substantial structural content.

**13. What does the framework now potentially contribute?**

- **Plan-DAG designers:** principled, conservative edge-update rule with exact Beta-Bernoulli instantiation.
- **Bayesian-RL researchers:** "gain as universal principle, conjugate as exact instantiation" framing — separates structural pattern from algebraic specificity.
- **Active-learning researchers:** connection between observability (gain) and credence-revision rate.
- **Decision theorists:** log-odds and probability-space as dual coordinates — Fisher-equivalent for moment-parameter results, with operationally distinct uses (gradient updates in log-odds; status propagation in probability-space).

Most distinctive: the structural-principle-vs-algebraic-formula distinction. Most ML literature treats $\eta = U_M/(U_M+U_o)$ as a Kalman-specific formula; AAD treats it as a structural principle that has exact algebraic instances (Kalman variance-ratio, Beta-Bernoulli conjugate $1/(n+1)$) without claiming all instances reduce to the same algebra.

## Status-label / discipline

`status: discussion-grade`. Hypothesis-tier extension; specific implementation choices remain domain engineering. `stage: draft`.

## Cadence check

Holding. Next: row 21 = `scope-edge-update-causal-validity`.
