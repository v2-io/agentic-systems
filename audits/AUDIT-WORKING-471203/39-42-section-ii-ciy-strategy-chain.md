# Reflection: §II CIY proxy / unified objective / explicit-strategy / chain-decay (4 segments)

Covers `#scope-ciy-observational-proxy`, `#disc-ciy-unified-objective`, `#norm-explicit-strategy-condition`, `#der-chain-confidence-decay`.

## Status table

| Slug | Stage | Status | Type |
|------|-------|--------|------|
| `scope-ciy-observational-proxy` | draft | conditional | scope |
| `disc-ciy-unified-objective` | draft | discussion-grade | discussion |
| `norm-explicit-strategy-condition` | draft | conditional | normative |
| `der-chain-confidence-decay` | claims-verified | exact | derived |

Diff-voice instances 16 (scope-ciy-observational-proxy) and 17 (disc-ciy-unified-objective).

## Predictions vs evidence

I had predicted the unified policy objective $\pi^\ast = \arg\max [Q_O + \lambda \cdot \text{CIY}]$ as scalar form. Got the **tensor upgrade**: $a_t^\ast = \arg\max_a [Q_O(a) + \text{Tr}(\Lambda \cdot \mathcal{I}_o(a))]$ where $\Lambda$ is PSD shadow price and $\mathcal{I}_o(a)$ is the Fisher Information Matrix ("Matrix CIY"). This is a substantive upgrade I had not predicted — exploration is now mathematically forbidden from collapsing onto blank-wall trivial solutions because the trace-product structure distinguishes by direction.

The chain-confidence-decay is exactly $\log P(\text{chain}) = \sum_i \log P(E_i \mid E_{<i})$ — pure chain rule. Listed in FORMAT.md inevitability core; the anchor role in the coordinate-forcing meta-pattern is now explicit (this segment is the chain-layer identity that motivates three downstream uniqueness theorems).

## Substantive findings / observations

**(A) Status-label issue in `#disc-ciy-unified-objective`.**

YAML: `status: discussion-grade` and `type: discussion`. Epistemic Status text begins "*Exact.* Originally treated as a discussion-grade heuristic, the unified objective has now been formally derived..."

Two readings:
- *Permissive:* the segment is discussion-typed (commentary), so YAML is correct; the prose's "Exact" refers to the underlying derived result lifted from `#deriv-directional-survival-exploration`. Layered status, similar to `#der-recursive-update` (body conditional, appendix exact).
- *Strict:* the text claims "*Exact*" and "Max attainable: *exact*" — these are not appropriate for a discussion-grade segment. The YAML and the text disagree.

**Candidate finding (Low severity):** the disc-typed segment shouldn't carry "Max attainable: *exact*" — that line should be in the underlying derivation segment, not in the discussion summary. The honest fix: move the "exact" claim to `#deriv-directional-survival-exploration`'s Epistemic Status; this segment's Epistemic Status should say "summarizes the exact result derived in `#deriv-directional-survival-exploration`."

**(B) Possibly-stale cross-reference in `#disc-ciy-unified-objective`.**

The segment forward-references `#deriv-directional-survival-exploration` as the source of the Lagrangian-LMI derivation. This slug **does not appear in `01-aat-core/OUTLINE.md`** as I read it — the closest matches are `#deriv-causal-ib-exploration` and `#deriv-causal-ib-lmi`. Either:
- The slug was renamed and this reference wasn't updated.
- The slug is planned but not yet promoted.
- I missed it in the OUTLINE walk.

**Candidate finding (Medium severity):** stale or pre-promotion cross-reference. The segment's central upgrade (heuristic → exact via Lagrangian relaxation of LMI) depends on the cited derivation existing. Phase 2: verify by `grep -r 'deriv-directional-survival-exploration' src/`.

**(C) `#scope-ciy-observational-proxy`'s safety-condition is exemplary.** "The proxy form should NOT be used in policy optimization (e.g., as the CIY term in a policy objective) because an agent maximizing a sign-indefinite quantity may optimize in the wrong direction." This is the kind of explicit don't-do-this discipline that makes a framework safe to extend. Filing under "what holds."

**(D) The dark-room-problem framing in `#disc-ciy-unified-objective`** is sophisticated. AAD claims to *bypass* the dark-room problem entirely via the survival-imperative (high $\lambda_{\text{surv}} \propto 1/U_M$ as $U_M \to 0$ in drifting environments). This is the formal counter to the "preferences-as-priors collapses to dark-room behavior" critique. Phase 2: verify the `#deriv-causal-ib-exploration` derivation actually delivers this.

**(E) The "anchor-plus-three-theorem" framing in `#der-chain-confidence-decay`** is now explicit. The chain-rule identity here is the *anchor*; three uniqueness theorems force coordinates at other layers (reverse-KL, log-odds, Fisher). The fourth potential instance is the composition-monotonicity / contraction-tower telescoping, which inherits the chain-rule additivity. The meta-pattern (`#disc-additive-coordinate-forcing`) catalogs this. Important structural pattern.

**(F) Triple depth penalty** named in `#der-chain-confidence-decay`: confidence decay (chain rule) + evidence starvation (`#deriv-edge-credence-dynamics`) + cognitive cost (`#form-strategy-complexity-cost`). The three penalties are independent and compound. This is the structural reason long causal chains are bad: not just one penalty, three.

## Math verification

**Chain confidence decay:** $\log P(\text{chain}) = \sum_i \log P(E_i \mid E_{<i})$. Chain rule of probability. Exact identity. ✓

**Quantitative table** ($p = 0.9, 0.8$ at depth $1, 3, 5, 10, 20$): standard $p^d$ values. $0.9^{10} \approx 0.349$ ≈ 0.35 ✓. $0.8^{20} \approx 0.0115$ ≈ 0.01 ✓. Numbers correct.

**Tensor objective $\text{Tr}(\Lambda \cdot \mathcal{I}_o(a))$:** standard Lagrangian-LMI form. $\Lambda$ PSD ensures the bonus is non-negative; the trace product distinguishes by direction (the LMI's directional shadow price). Without verification of `#deriv-directional-survival-exploration`, the *form* is correct but the *derivation* is unverified.

**Bretagnolle-Huber identity** (`#disc-ciy-unified-objective`): $D_{KL}(\pi^\ast \| Q_{\Sigma_t}) = -\log(1 - TV(\pi^\ast, Q_{\Sigma_t}))$ for deterministic $\pi^\ast$. This is the BH 1978 result; correct and standard. Phase 2 verify the precise reference.

**Pinsker** for stochastic-$\pi^\ast$ extensions: $\text{TV} \leq \sqrt{D_{KL}/2}$, standard.

## Cross-segment consistency

The CIY-unified-objective references the regret-bound derivation in `#deriv-strategy-cost-regret-bound` (Appendix A); the chain-confidence-decay anchors the additive-coordinate-forcing meta-pattern via `#disc-additive-coordinate-forcing` (Appendix A). Both are forward-references to be verified.

The "Two Parallel Exploration Drives" framing ($\lambda_{\text{info}} \propto U_M$ + $\lambda_{\text{surv}} \propto 1/U_M$) is internally consistent — they compose so that exploration is high in either limit (high $U_M$ → epistemic; low $U_M$ → survival imperative). Smart.

The CIY proxy regime A/B/C in `#scope-ciy-observational-proxy` is consistent with `#der-loop-interventional-access`'s regime-indexed identification strength. Same A/B/C carving.

## Felt value

**Mid-high overall.** The chain-confidence-decay is foundationally clean (inevitability core, well-proved). The unified objective's tensor upgrade is structurally interesting but depends on an unverified derivation reference. The CIY proxy's regime classification + safety condition is good scope-honesty. The explicit-strategy-condition is honestly normative.

The phenomenological lift on the **"anchor-plus-three-theorem" framing** in `#der-chain-confidence-decay` is real — the meta-pattern (chain-rule identity → analog motivating three further uniqueness theorems) is the kind of structural-pattern naming that the framework's distinctive epistemic discipline produces.

## What this batch enables

- A *safe* CIY-style exploration objective with tensor / matrix Fisher form (when the supporting derivation lands).
- A clean *normative* criterion for whether explicit strategy is worth maintaining.
- The chain-rule-of-probability identity in its anchor role for the coordinate-forcing meta-pattern.
- The triple-depth-penalty framing for why long causal chains compound fragility three-fold.

## Wandering thoughts

The "Two Parallel Exploration Drives" framing is the kind of structural-symmetry observation I find satisfying. Most exploration-vs-exploitation discussions treat exploration's value monotonically (more uncertainty → more exploration). AAD says: high $U_M$ drives epistemic exploration; *low* $U_M$ in drifting environments drives survival exploration (because confident agents in changing worlds are mathematically guaranteed to die unless they actively probe). The two limits compose to a U-shaped exploration valuation: high at both extremes.

This bypasses the dark-room critique via physical-survival argument rather than via preference structure. It's the kind of *substantive disagreement* with active inference that AAD's positioning depends on. If `#deriv-causal-ib-exploration` delivers this rigorously, it's a genuinely novel structural commitment.

The triple-depth-penalty observation is the kind of "things compound" insight that's easy to miss until named. Each penalty individually is intuitive; their independence and compound effect is the structural observation. For software-development analysis: a 20-step plan has *three* sources of fragility, not one. For LLM agents with chain-of-thought: longer reasoning chains compound *three* penalties simultaneously.

A naming-brainstorm seed: "matrix CIY" or "Fisher CIY" might be a more specific term than "tensor CIY" — the Fisher Information Matrix framing makes the upgrade structurally precise. The current segment uses both "Matrix CIY" and references $\mathcal{I}_o(a)$; consistent terminology in any future Brief would help.

The status-label issue in `#disc-ciy-unified-objective` is interesting because it shows what happens when a segment is *upgraded* — the prose was rewritten to reflect the derivation, but the YAML status / type metadata wasn't updated. This is a real propagation-debt failure mode that the audit should surface for the integrator. Easy fix once identified.

Continuing.
