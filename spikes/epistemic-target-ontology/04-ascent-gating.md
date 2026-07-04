# Ascent Gating: Belief-Layer Self-Coupling Forecloses Structural Adaptation — a First Derivation

*Deposited 2026-07-04 (night session) by the lead. Status: **worked first derivation, not independently verified** — the model is a stylized Formulation, the threshold result is exact within it, and the canon-facing vocabulary finding in §1 was checked against primary sources first-hand. Nothing here touches canon. Origin: `00-spike.md` §8 (the covenant/self-legislation thread; Joseph's referent-axis refinement) + the B-2 detection-signature work (audit 731548).*

## 1. The setting, and a canon-facing vocabulary finding (checked first-hand)

`#der-directed-separation` defines $\kappa_{\text{processing}} = I(G_t; M_{\tau^+} \mid e_\tau, M_{\tau^-}) / H(G_t \mid e_\tau, M_{\tau^-})$ — a specifically *belief-layer* measure (goal-information reaching the post-update belief state other than through evidence), and the object to which the entire certificate machinery attaches. Its Working Notes carry an explicit regression guard: "`#der-action-selection` … action selection legitimately couples goals." Meanwhile `#disc-strategic-self-coupling` *does* distinguish the layers in its §"Relationship to truthification" (truthification = commitment to goal-blind belief-update; strategic self-coupling = commitment to goal-conditioned *action-selection* — "deliberately weakens it **at the action-selection layer**"), so the conflation hypothesized at `00-spike.md` §8 first-contact is **not** conceptual. What remains is real but narrower — three items:

1. **Vocabulary overload.** The segment's framing sentences (opening ¶; §"The enabling polarity") describe all four mechanisms as "driving $\kappa_{\text{processing}}$ upward," and §"Asymmetric advantage" speaks of "different axes of $\kappa_{\text{processing}}$." By the formal definition, a pure Schelling device (external commitment; action-layer only) moves $\kappa_{\text{processing}}$ **not at all** — no $G_t$-information enters $M_{\tau^+}$ outside $e_\tau$ — and the directed-separation certificate survives it intact. Using the belief-layer symbol as the state variable for the action-layer operation implies, wrongly, that commitment devices degrade the certificate. The action-layer coupling needs its own symbol; call it $\chi_A$ here (the coupling state that parameterizes $\mathcal A(\chi_A)$ in the segment's (M1)).
2. **The four mechanisms are untyped by layer.** External device: pure $\chi_A$. Personal rules: mostly $\chi_A$. Identity coupling: mixed ($\chi_A$ + a $\kappa_B$ component insofar as identity filters interpretation). Emotional commitment: mixed-to-$\kappa_B$ (Frank's mechanism works *because* affect overrides appraisal — belief-layer by design). "Sincere-conviction persuasion" (opening ¶): essentially pure $\kappa_B$ — belief adopted for its strategic value is $G \to f_M$ verbatim.
3. **The inverted-U plausibly decomposes.** The segment's non-monotone $\mathcal A(\kappa_t)$ — rising (commitment-enabling) then falling (reality-tracking foreclosed) — reads naturally as the *sum of two monotone curves on two axes*: action-space gain rising in $\chi_A$, and reality-dependent action-space falling in $\kappa_B$. Mechanisms that load both axes trace the inverted-U as they intensify; a pure commitment device never enters the falling regime (its failure mode is different and milder: commitments outliving their justification — rigidity, not corruption). The interior optimum $\kappa^\ast$ would then be an artifact of aggregating the axes, and the segment's open "empirical shape" question resolves structurally. *(Hypothesis-grade; the decomposition claim needs its own check against the four literatures.)*

This typed setting is what the ascent-gating question needed: **corruption lives on $\kappa_B$; commitment lives on $\chi_A$; the derivation below shows the ascent signal cares only about $\kappa_B$.**

## 2. The configuration typology (the 2×2 the covenant thread predicts)

| | $\chi_A$ low (action uncommitted) | $\chi_A$ high (action bound) |
|---|---|---|
| **$\kappa_B = 0$ (belief goal-blind)** | the **calculator** — Schelling's non-credible rational actor: tracks reality, binds to nothing, can be talked out of anything; no credibility-dependent actions available | the **covenant configuration** — belief free of goals, action bound to commitments; the diplomat of the segment's own example; full ascent signal *and* full commitment reach |
| **$\kappa_B \gt 0$ (belief goal-coupled)** | the **self-legislator** — motivated cognition without real binding ("abideth not by law"); apparent flexibility, corrupted diagnostics | the **captured** — bound in action to a surrogate *and* unable to see it; the cult-formation endpoint; both deaths at once |

The framework's own truthification-dual sentence already names the covenant column without noticing it is a *configuration*: "truthification commits to not letting goals corrupt belief; strategic self-coupling commits to letting goals constrain action" — an agent doing **both** is the covenant-keeper, and the two commitments are not in tension because they live on different layers. The v34/v35 shadow (per `00-spike.md` §8) is the $\kappa_B$ row-distinction, *not* the $\chi_A$ column-distinction.

## 3. The derivation: a foreclosure threshold for the ascent signal

**Setup** *(Formulation — stylized but with each piece grounded in existing canon)*. Under genuine class-inadequacy the residual stream carries structure: $r_t = s_t + n_t$ with $s_t$ the systematic (class-gap) component — AR(1), autocorrelation $\varphi \in (0,1)$, variance $\sigma_s^2$ — and $n_t$ white channel noise, variance $\sigma_n^2$ (this is exactly the structured-vs-white discriminator of `#result-structural-adaptation-necessity` / the B-2 landing). Belief-layer coupling lets goal-state explain away goal-incongruent structure: the *monitored* residual is

$$\tilde r_t = (1 - \kappa_B)\, s_t + n_t,$$

i.e., a fraction $\kappa_B$ of the systematic component is absorbed into goal-congruent belief adjustment before it reaches the diagnostic. (White noise is not absorbable — there is no structure to reinterpret; this asymmetry is the model's one substantive commitment, and it is the motivated-cognition phenomenon itself: reinterpretation consumes *pattern*, not static.) Action-layer commitment $\chi_A$ constrains $\mathcal A$ and appears nowhere in $\tilde r_t$.

**The trigger threshold is economically forced positive.** The structural-adaptation trigger fires on detected residual structure. Because structural change carries enormous cost (knowledge loss, the massive-$\Delta\tau$ mismatch debt of `#der-deliberation-cost`; the rational-conservatism analysis in `#result-structural-adaptation-necessity`), a rational agent triggers only above a materiality threshold $c \gt 0$ on the (lag-1, say) residual autocorrelation — triggering on arbitrarily faint structure would be Premature-structural-change, which the framework itself prices as an error. Honest detectability requires $\rho_1(0) = \varphi\sigma_s^2/(\sigma_s^2 + \sigma_n^2) \gt c$: an uncorrupted agent can see the signal.

**Result A (exact in the model) — the monitored signal decays quadratically in the coupling.** With $a = 1 - \kappa_B$:

$$\tilde\rho_1(\kappa_B) = \frac{a^2 \varphi \sigma_s^2}{a^2 \sigma_s^2 + \sigma_n^2},$$

strictly decreasing in $\kappa_B$, independent of $\chi_A$.

**Result B (exact in the model) — the foreclosure threshold.** $\tilde\rho_1(\kappa_B) = c$ at

$$\bar\kappa_B \;=\; 1 - \sqrt{\frac{c\,\sigma_n^2}{\sigma_s^2\,(\varphi - c)}},$$

and $\bar\kappa_B \in (0,1)$ **exactly when honest detection is possible** ($\rho_1(0) \gt c$) — the threshold exists precisely for agents who had something to lose. For $\kappa_B \gt \bar\kappa_B$ the *population* autocorrelation of the monitored stream sits below the rational trigger threshold: **no sample size, no patience, no accumulation of experience ever justifies triggering.** This is permanent foreclosure, not delay — the agent is locally rational at every step and never ascends.

**Result C (standard statistics) — divergence on approach.** For $\kappa_B \lt \bar\kappa_B$, detecting $\tilde\rho_1 \gt c$ from $N$ samples needs $N \gtrsim z^2 (1 - \tilde\rho_1^2)^2 / (\tilde\rho_1 - c)^2$, and since $\tilde\rho_1 - c \propto (\bar\kappa_B - \kappa_B)$ to first order near the threshold, the expected detection time diverges as $(\bar\kappa_B - \kappa_B)^{-2}$. The trap announces itself: ascent gets slower and slower before it becomes impossible.

**Result D (the covenant half).** $\chi_A$ enters none of the above: action-layer commitment leaves the diagnostic untouched, so the covenant configuration ($\kappa_B = 0$, $\chi_A$ high) retains full ascent-routing regardless of how bound its actions are. One honest caveat, distinguished deliberately: a commitment that forecloses *informative actions* can impoverish the chronica (less CIY, weaker $\sigma_s^2$ in the monitored window) — but that is signal *impoverishment* (recoverable, and visible as such), not signal *corruption* (self-concealing). The two failure modes are of different kinds, and only the second is the v35 shape.

## 4. Reading, and connections

- **"They must remain filthy still" is the permanence of Result B.** The foreclosure is not imposed; it is the composition of two individually-rational structures — conservatism justified by the true cost of structural change, and filtering chosen for goal-comfort — into a trap with no interior escape. Nothing external breaks it (the sanctification no-go from `00-spike.md` §8: every restorative mechanism operates through the very diagnostic that has been corrupted). And the agent selected it. Joseph's "the saddest kind of all," now with an exponent.
- **Mood-complacency composes.** Under $\kappa_B \gt 0$ the *perceived* tracking is easier than the real tracking; the mood layer (which integrates perceived surprise) relaxes gain toward $g_{\min}$, further weakening correction exactly when the class gap is growing. The MG-1 floor bounds the damage but cannot restore the signal. Candidate composition derivation, not worked here.
- **Ascent-gating and Alma 12:9.** Graded disclosure "according to the heed and diligence" — the granting-side statement of the same gate the learning-side derivation finds: capacity to receive the next level is a monotone function of faithfulness to the current one, because faithfulness (here: $\kappa_B = 0$) is what keeps the receiving channel readable. Recorded as substrate resonance per the `00-spike.md` §8 register; the formal result stands on its own legs.

## 5. What would strengthen / what would soften

**Strengthen:** (i) independent re-derivation + a small simulation (the model is simple enough that an afternoon agent settles it); (ii) replace the linear-attenuation Formulation with a derivation of the filtering form *from* the $\kappa_{\text{processing}}$ definition (what does $I(G_t; M_{\tau^+} \mid e_\tau, M_{\tau^-}) \gt 0$ imply about the monitored-residual spectrum? — this is the real gap between "exact in the model" and "derived from the framework"); (iii) direction-selective filtering (goal-relevant subspace only) — expected to *sharpen* the result, since the class gap concentrates where the goals live; (iv) the §1.3 inverted-U decomposition checked against the four mechanism literatures. **Soften:** if motivated filtering empirically attenuates noise as much as signal (contra the model's asymmetry commitment), $\tilde\rho_1$ survives and only the mismatch *level* is distorted — the trigger would fire late but not never. The asymmetry commitment is therefore the load-bearing empirical question; the cognitive literature on motivated reasoning (pattern-level reinterpretation) supports it qualitatively, but that support is imported, not derived.

## 6. Routing

- §1's vocabulary finding → candidate strengthen-first item for `#disc-strategic-self-coupling` (introduce $\chi_A$; type the four mechanisms; decompose the inverted-U) — **needs a full-segment verification pass + Joseph** (it touches the M4 three-operation vocabulary).
- §3's derivation → stays here until independently verified; then per math-lives-in-segments it wants a segment home (natural candidates: a new appendix derivation under `#result-structural-adaptation-necessity`, with Discussion hooks in `#disc-strategic-self-coupling` and `#def-mood`).
- §2's 2×2 → candidate Discussion table for the self-coupling segment once §1 lands.
