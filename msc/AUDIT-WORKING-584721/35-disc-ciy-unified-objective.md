# Reflection 35 — disc-ciy-unified-objective (Section II row 10)

## §4.2 dependency check

`depends: [def-causal-information-yield, scope-ciy-observational-proxy, def-value-object, der-action-selection]`. All upstream. **No backward-dep, no F-A drift.**

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted: "joint exploitation-exploration objective with $\lambda$-weighted CIY term." ✓. Plus the substantial active-inference comparison subsection (structural isomorphism + two AAD-distinctive differences) and the regret-bound connection to strategy-cost objective. **Substantially richer than predicted.**

**2. Cross-segment consistency.** Extensive cross-refs all internally consistent. The active-inference comparison cites Friston 2017, Da Costa 2020, Sajid 2021, plus Sun & Firestone 2020 for the dark-room critique. Sharp scope-honesty.

**Mild integration debt observation:** The segment cites the **Pinsker** bound for the regret-vs-KL-direction argument: "bounded above by $V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(\pi^* \Vert Q_{\Sigma_t})}$ under bounded value range (Pinsker)". Per CLAUDE-2.md priming, the canonical segment `#deriv-strategy-cost-regret-bound` was upgraded 2026-04-24 to use the **Bretagnolle-Huber identity** $D_{\mathrm{KL}} = -\log(1-\mathrm{TV})$ exact under deterministic $\pi^*$ as the primary bound (strictly sharper than Pinsker). This segment hasn't propagated the BH-identity update — it's still using the older Pinsker statement.

The Pinsker bound is *valid* (just not tightest), so this isn't a math error. But it's a mild integration debt around the recent BH-identity addition. Logging as **F-D1**: integration debt — disc-ciy-unified-objective uses Pinsker bound where the canonical segment now uses sharper BH-identity. Editorial fix; low severity.

**3. Math verification (at discretion).** The Pinsker bound itself is valid: $|\!|P-Q|\!|_{TV} \leq \sqrt{D_{KL}(P\|Q)/2}$, and bounded value range gives the regret bound stated. The BH-identity is the sharper exact form under deterministic $\pi^*$. Both correct; one is sharper.

**4. What direction next?** Row 11 = `norm-explicit-strategy-condition`. The "when planning beats exploring" normative segment.

**5. What errors should I now watch for?**
- Future segments using CIY as if it equals EIG (the segment is explicit they differ).
- Conflation of CIY-canonical (non-negative) with CIY-proxy (sign-indefinite).
- Active-inference framings that assume preferences-as-priors (Sun-Firestone dark-room critique applies).
- Other segments still using Pinsker where BH-identity now holds.

**6. Predictions for next segments.** Row 11 = `norm-explicit-strategy-condition`. status:draft per OUTLINE. Normative claim about when explicit strategy beats pure exploration.

**7. What would I change?** Update the Pinsker reference to mention BH-identity as the tighter form (with cross-ref to deriv-strategy-cost-regret-bound). Mild editorial; not a substantive content fix.

The "Connection to active inference" subsection is sharp — structural-isomorphism acknowledged, two AAD-distinctive differences named explicitly with citations. This is the kind of prior-art-positioning AAD does well.

**8. What am I now curious about?**

(a) **The "preferences-as-priors collapse" critique.** AAD's $O_t$ is a value functional on trajectories, not a prior over outcomes. So the dark-room critique doesn't apply: an AAD agent cannot reduce expected free energy by hiding in a dark room because the trajectory functional doesn't decrease just because observations are uniform. This is operationally significant and gives AAD a defensible position relative to active-inference critiques.

(b) **The five-domain $\lambda$ mapping** (Gittins / Kalman dual control / EFE precision / IDS / RL UCB) is operationally useful. Suggests AAD's framework is a generalization that includes these as special cases — which is an "integration claim" rather than a "novel-mathematics" claim. Consistent with CLAUDE.md framing: "AAD's contribution is integration."

(c) **The identifiability gate** (4 conditions before using CIY in policy optimization) is clean operational discipline. Action variation, regime identification, reference distribution, local stationarity — all required.

**9. What new knowledge enabled.** Joint exploitation-exploration policy objective. $\lambda$ as value-per-information weight unified across multiple decision-theoretic frameworks. Identifiability gate. Active-inference structural isomorphism with explicit AAD-distinctive moves. Regret-bound shape connecting value to strategy-complexity cost.

**10. Should the audit process change?** Continuing.

**11. Outline updates.** Adding F-D1 (BH-identity integration debt). Section E confirmation: the active-inference scope-honesty is sharp.

**12. How valuable does this segment *feel* to me?**

Medium-high. The active-inference scope-honesty is one of the framework's clearer prior-art-positioning moves. The regret-bound connection to strategy-cost is a useful structural bridge. The five-domain $\lambda$ table is operationally useful. The discussion-grade tier is honest.

Magnitude: middle-of-pack to top-quarter. Type: discussion-grade synthesis with substantive prior-art integration. Engagement: I noticed the Pinsker / BH-identity debt while reading.

**13. What does the framework now potentially contribute to the field?**

- **Decision-theory researchers** get a unified policy-objective formulation that explicitly distinguishes exploitation from exploration with regime-aware identifiability gate.
- **Active-inference researchers** get AAD's position: structural isomorphism on shape (value + information), divergence on substance (causal vs entropy-reduction; trajectory functional vs priors-as-preferences). Defensible with citations.
- **Bandit / IDS / Kalman-dual-control practitioners** get a five-domain $\lambda$ mapping showing their existing $\lambda$-style weighting is special case of AAD's general form.
- **Sun-Firestone dark-room critique** gets a formal AAD response: AAD's diagnostic structure (satisfaction-gap, control-regret) doesn't collapse under preferences-as-priors because AAD doesn't encode preferences that way.
- **Practitioners** get a clean default and identifiability gate: drop CIY term if action variation absent, regime unidentified, $q$ unspecified, or local stationarity fails.

**Most distinctive contribution:** explicit structural isomorphism with active inference plus two AAD-distinctive moves, supported by external citations. The formal handle on the dark-room critique is operationally significant for AAD-vs-active-inference debates.

## Status-label / discipline

`status: discussion-grade` honestly tier-marked — the segment explicitly says heuristic and surrogate-not-EIG. Tier-stratification within: structural form (well-supported by convergent literature) vs specific surrogate choice (heuristic).

`stage: draft`.

## Cadence check

Holding. Next: row 11 = `norm-explicit-strategy-condition`.
