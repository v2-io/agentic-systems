# Exploratory extension: E3's mechanism aimed at `#impl-orient-cascade`'s open propagated-residual bound

*Written after the verification agent was launched on the main spike; the verifier's report does not cover this file unless it says so. Tier: **sketch / exploratory** — one derivation at outline grade, hypotheses labeled. Purpose: test whether Theorem E3's telescoping-with-contraction mechanism discharges the open item in `#impl-orient-cascade` (Working Note 2026-05-31): "a dedicated propagated-residual bound (how the per-step bias compounds across the five-step cascade) is an open strengthening, not attempted."*

## The shape

Canon's landed per-step bound (`#deriv-observation-ambiguity-bias-bound`): at $\kappa_{\text{processing}} \gt 0$, the cascade's step-1 output is displaced by $\lVert \Delta M_{\text{bias}} \rVert \leq b := C \kappa I$ per update. The open question is compounding: across the cascade's downstream steps within a cycle, and across repeated cycles.

**Within one cycle** (the five-step cascade, each step reading the previous step's output): if each downstream step $j$ is $L_j$-Lipschitz in its epistemic input (the same regularity `#impl-orient-cascade` already invokes for the diagnostic bound, $L_A$ domain-dependent), the within-cycle propagation is the product chain

$$\lVert \Delta(\text{step } k) \rVert \;\leq\; \Big( \prod_{j=2}^{k} L_j \Big)\, b,$$

which is mechanical and carries no surprise: it is bad exactly when some $L_j \gt 1$ (an amplifying step) and benign when the cascade is non-expansive. Nothing here needed E3.

**Across cycles is where E3's mechanism bites.** The displaced $M_t$ feeds the next cycle's step 1 as its prior. Model the cycle-to-cycle epistemic map as the true update $T_t$ (contractive toward the reality-tracking trajectory with factor $\beta \lt 1$ per cycle — the same Dobrushin-type coefficient E3 uses, here the belief-update's forgetting of its prior) perturbed per cycle by at most $b$. The E3 telescoping applies verbatim: the cumulative displacement after $n$ cycles satisfies

$$\lVert \Delta_n \rVert \;\leq\; \sum_{s=1}^{n} \beta^{\,n-s} b \;\leq\; \min\Big( n\,b,\; \frac{b}{1-\beta} \Big).$$

**Hypothesis (labeled):** the honest steady-state form of the cascade residual is therefore $\dfrac{C \kappa I}{1 - \beta}$ — coupling-bias over epistemic forgetting rate — with the linear regime $n b$ operative below the belief-mixing time. The interpretive content: a Class-2 agent's motivated-reasoning displacement does not grow without bound; it saturates at a floor set by the ratio of per-update goal-leak to how fast evidence overwrites priors. Fast-forgetting (high-$\beta$-gap) agents are structurally protected; slow-updating agents accumulate the full linear burn until mixing.

## What would make this a result rather than a sketch

1. Justify the per-cycle contraction $\beta \lt 1$ for the cascade's epistemic map from canon's own update dynamics (candidates: the contraction machinery in `#result-contraction-template` / the Fisher-gain segments) rather than assuming it.
2. Reconcile norms: $b$ is stated in $W_2$ / Fisher–Rao tracks; E3's telescoping is TV. Either run the telescoping in the metric $b$ is stated in (needs contraction in that metric) or bridge with the standard comparisons (each direction lossy; the losses must be carried).
3. The adversarial drill for the eventual universal claim: construct one architecture outside the motivating family where $\beta \to 1$ (non-forgetting belief) and confirm the bound's blow-up is real, not an artifact — the conjectured witness is a pure accumulator/counter belief, where displacement genuinely grows linearly forever.

None of the three is done here. If a future agent lands this, `#impl-orient-cascade`'s Working Note is the integration target.
