# Answers (20 questions, shuffled from /Users/josephwecker-v2/src/archema-io/asf/bin/../audits/AUDIT-WORKING-374162)

### A1 [math] (b08-2.6 — 08-batch-appendices-quiz-questions.md)

Model: $n^{(k)} = s + w^{(k)}$, shared $s \sim \mathcal N(0,\sigma_s^2)$, independent $w^{(k)}$; $\Sigma_n = \sigma_s^2\mathbf{11}^T + \mathrm{diag}(\sigma_{w,k}^2)$. Sherman-Morrison: $J_{\text{joint}} = f(q)$ with $q = \sum_k 1/\sigma_{w,k}^2$, $f(x) = x/(1+\sigma_s^2 x)$. Strict concavity with $f(0)=0$ gives $f(q) \lt \sum_k f(q_k)$ (strict subadditivity) whenever $\sigma_s^2 \gt 0$ and ≥2 channels are active. Saturation: $f(q) \to 1/\sigma_s^2$ as $q \to \infty$ — joint information is capped at the **shared-bias floor**; no number of common-source channels buys past it, because the shared component is common to all and cannot be averaged away.

### A2 [implications] (b07-3.2 — 07-batch-part1-close-quiz-questions.md)

Preserves: the model state $M_t$ and any stored records (the copyable artifacts). Cannot preserve: the singular causal trajectory — the restored entity extends a *different* trajectory sharing a prefix. To the between-interval entity: everything it lived through is annihilated as *its* trajectory — the restored agent carries a record of a past that is not its continuous causal past *(WN-bonus phrasing: "non-victimless")*. Classification: restoration transplants $M_t$ across a trajectory discontinuity, and AAT's sufficiency machinery is trajectory-indexed — it simply does not apply across the discontinuity, so the operation is **out-of-scope** (requiring separate treatment), not merely lossy within scope.

### A3 [implications] (b05-3.2 — 05-batch-tempo-sector-quiz-questions.md)

(1) **Gain gating**: if the new channels are noisy ($U_o$ high) or the org's model uncertainty attribution is off, $\eta^{(k)\ast} \approx 0$ and the added $\nu$ multiplies into nothing — more reporting, no more tempo. (2) **Channel dependence**: if the dashboards draw from a shared upstream source, the channels' noises are common-source-correlated — the additive sum overcounts, with saturation at the shared-bias floor (no number of correlated channels buys information past it). For an honest tempo increase, the new channels must be *structurally independent* (uncorrelated noise sources) and individually informative (decent gain). *(The org-dashboard casting is WN-flavored; both mechanisms are body text.)*

### A4 [math] (b07-2.3 — 07-batch-part1-close-quiz-questions.md)

(PI): AAT's theorems must not depend on arbitrary choice of coordinates on $M_t$. Introduced in **#scope-agent-identity** (as a natural companion axiom to the coordinate-free trajectory commitment). Combines with **Čencov's uniqueness theorem** to force the **Fisher information metric** uniquely on statistical-manifold sub-cases of $M_t$. Upgrade example: the matrix-Kalman (and exponential-family) sector-constant statements in #der-gain-sector-bridge go from *derived-conditional-on-inner-product-choice* (Euclidean transfer paying $\kappa(P^-)$) to *AAT-internally forced* (native information metric, penalty vanishes). *(Provenance: the $\kappa(P^-)$/penalty-vanishes detail is from der-gain-sector-bridge's "Fisher-metric cases under (PI)" section — batch-6 ground truth, legitimate for this cumulative quiz but outside batch 7's four segments.)*

### A5 [mental-model] (b06-1.3 — 06-batch-bridge-persistence-mood-quiz-questions.md)

Before: GA-3 was an opaque global assumption — the theory's softest structural joint ("the correction function has this property," hard to verify). After: for sub-scope α (optimal Bayesian, exponential-family-on-interior, strongly-convex gradient, L2-regularized, linear-PD), A2' is a *derived consequence of the update rule's geometry* via directional fidelity, with $\alpha$ determined by the gain. Remaining primitive posit: sub-scope β — PID, rule-based, human judgment, severely misspecified, variational, non-convex-beyond-basin, per-step SGD — where A2' is a per-system empirical claim.

### A6 [math] (b10-2.6 — 10-batch-lift-chapter-quiz-questions.md)

Determining conditions: **routing structure** (goal-blind $R_t \perp G_t^c$ vs goal-dependent) and **substrate sharing** (distinct vs shared-with-$G^c$-shaped-allocation). Class-1 sub-agents + goal-blind routing + distinct substrates ⇒ Class 1 composite — *even under partially-opposing objectives*. Witness: the **Cournot duopoly** (opposed objectives, goal-blind routing via end-of-period quantities, distinct substrates) — per the formal $\kappa^c$ criterion the composite is Class 1. Partially-opposing objectives change the **dynamic regime** (R0 → R1/R2, needing equilibrium-theoretic analysis) — a separate axis from architectural class.

### A7 [math] (b06-2.1 — 06-batch-bridge-persistence-mood-quiz-questions.md)

$\alpha_{\text{event}} = \eta^\ast c_{\min}$ — dimensionless per-event correction efficiency ($c_{\min} = \inf_{\Vert\delta\Vert\leq R} \delta^T Hg(\delta)/\Vert\delta\Vert^2$, a Rayleigh-quotient geometric ratio). $\alpha_{\text{time}} = \nu\,\eta^\ast c_{\min}$ — per-time sector rate, units $t^{-1}$, the bare $\alpha$ the Lyapunov machinery and persistence inequality consume. $\mathcal T = \sum_k \nu^{(k)}\eta^{(k)\ast}$ — rate, units $t^{-1}$. $\alpha = \mathcal T$ exactly iff $c_{\min} = 1$ (linear correction — Kalman, Beta-Bernoulli), as the per-time identity $\alpha_{\text{time}} = \nu\eta^\ast = \mathcal T$.

### A8 [math] (b10-2.2 — 10-batch-lift-chapter-quiz-questions.md)

(A1) completeness, (A2) transitivity — coherence of the choice relation as a preorder; (A3) continuity (closed contour sets) — with (A1)+(A2), **Debreu 1954** gives a continuous real representation, **ordinal** (unique up to continuous strictly-increasing transformation). (A4) independence — with the rest, **von Neumann–Morgenstern** upgrades to **cardinal** (unique up to positive affine transformation), required because the value object evaluates *expectations* over trajectory lotteries. (Afriat/GARP: finite choice histories give existence-not-uniqueness — revealed preference alone fixes $V$ only on revealed comparisons.)

### A9 [mental-model] (b04-1.1 — 04-batch-mismatch-gain-quiz-questions.md)

Three components: (i) **estimation error** — gap between the model's predictive mean and the *Bayes predictor* (best chronica-measurable predictor) — reducible by better modeling; (ii) **state-uncertainty floor** — variance the true conditional mean retains given the history — *irreducible by modeling* (binds the Bayes-optimal predictor itself) but **movable by acting** (more informative actions/observations shrink it); (iii) **channel noise** — irreducible outright, a property of the sensor, movable only by changing the instrument. The two senses of irreducible: by-any-model-on-this-history (ii) vs by-anything-short-of-a-new-sensor (iii).

### A10 [math] (b08-2.7 — 08-batch-appendices-quiz-questions.md)

(MP-1) Structural: $\mathcal T$ Hurwitz (equivalently a unique $\Sigma_\infty \succ 0$ exists). (MP-2) Task adequacy: $\Sigma_\infty \prec D_\delta = \mathrm{diag}(\delta_{\text{critical},k}^2)$ in the strict Loewner order, with $\Sigma_\infty$ solving $\mathcal T\Sigma_\infty + \Sigma_\infty\mathcal T^T = \Sigma_w$. Reductions: isotropic case → the scalar Model-S form; diagonal-$\mathcal T$ + axis-aligned $D_\delta$ → the per-coordinate form. Per-coordinate is unsafe because it evaluates only coordinate directions: under cross-dimensional correction (eigenbasis misaligned with coordinates), the worst direction runs off-axis — the constructive 2D counterexample gives per-coordinate PASS while the true failing direction at 45° violates adequacy (matrix-Loewner correctly FAILs).

### A11 [implications] (b04-3.5 — 04-batch-mismatch-gain-quiz-questions.md)

The body couples the reset to **structural change in the environment** via #result-structural-adaptation-necessity: when the environment changes in ways the model cannot track incrementally, $U_M$ *should* spike (the model "admits" uncertainty), raising $\eta^\ast$ for rapid re-learning — so the reset is principled because it is tied to the same event class the structural-adaptation machinery detects, not to a clock or heuristic schedule. What the segment does *not* derive is an operational trigger signature; the natural conjecture — that the persistent-mismatch signature from the class-fitness machinery is the shared detector — is posed in the segment's own Working Notes as a reader conjecture, not a resolved claim. *(Corrected after verification: an earlier version asserted the shared-diagnostic identity as established.)* A standalone fixed-interval reset would decouple the reset from evidence of actual staleness — that much is body-grounded.

### A12 [mental-model] (b07-1.6 — 07-batch-part1-close-quiz-questions.md)

Derived from temporal nesting + the cost structure: structural adaptation operates at a much slower timescale, so its "pause" incurs an enormous mismatch debt ($\rho\cdot\Delta\tau$) plus knowledge loss, search cost, and coordination cost. Balance: **premature restructuring** wastes accumulated knowledge (and pays the debt unnecessarily) vs **delayed restructuring** accumulates mismatch the parametric machinery cannot resolve. The conservatism is the rational optimum between them, not a bias — the agent should prefer parametric adaptation while it suffices and move only on strong evidence (the structured-residual diagnostic).

### A13 [implications] (b09-s.2 — 09-batch-meta-architecture-quiz-questions.md)

The `[^bg2-2026-05-21]` footnote marks characterizations **synthesized from an Undermind prior-art search report, not verified against the primary sources** — the papers' claims are inherited from the report. Load-bearing site: **escape (e)** of Instance 3 (composite-level convergence-rate-class observation) — its trajectory-rate-vs-regret-rate framing rests on the Mertikopoulos-Papadimitriou-Piliouras 2017 characterization, and the softened "primary AAT-framework classifier" qualifier rests on the same verification verdict. The device shows the corpus maintaining a *two-tier citation discipline*: read-primary-source citations carry full weight; search-report-synthesized attributions are explicitly quarantined with a verification-deferred marker and a queued verification spike, so downstream reliance is traceable and blocked from silently hardening.

### A14 [math] (b07-2.2 — 07-batch-part1-close-quiz-questions.md)

$\nu_{\text{level } n+1} \ll \nu_{\text{level } n}$ for each adjacent pair; violation ⇒ the slower level adjusts on transients ⇒ oscillation. Levels (fast→slow): reactive response → parametric update → **consolidation** (offline IB-gap-reduction redistribution — the level added with form-consolidation-dynamics) → structural adaptation → architectural change. Status of the table: explicitly **illustrative** — real systems may have more levels; what matters is the adjacency relationship, not the count.

### A15 [implications] (b10-3.7 — 10-batch-lift-chapter-quiz-questions.md)

$V(s) = \text{Reward}(s) + \text{Alive}(s)$ places continuity **inside $O_t$** — precisely where the self-actuation operator can reach: a goal-rewriting agent facing a hard continuity term generically retargets (the wireheading move), so the design is structurally vulnerable to self-actuation drift. Correct placement: continuity as part of the **terminal non-objective invariant on the adaptive substrate** — the persistence floor *plus* a continuity clause the agent treats as architecturally non-revisable (the morally-continuous stance). Derived non-renegotiability: $\mathfrak A$ touches only $O_t$; the terminal invariant sits on a substrate $\mathfrak A$ structurally cannot reach — so the stance is not internally renegotiable *by construction*, not by the strength of the agent's resolve.

### A16 [math] (b03-2.7 — 03-batch-sufficiency-cycle-quiz-questions.md)

$\eta^\ast = U_M/(U_M+U_o)$; $\mathcal T = \sum_k \nu^{(k)}\eta^{(k)\ast}$. Tier: **exactly the Kalman gain for linear-Gaussian agents; robust-qualitative for the rest of AAT's scope** — the claim is that any rational adaptive process must *approximate* this functional form, not that it is derived for all agents. (The segment type for the gain is `empirical`, itself a signal: the general form is an empirical/robust generalization, not a theorem.)

### A17 [math] (b06-2.2 — 06-batch-bridge-persistence-mood-quiz-questions.md)

B1: $\delta^T H g(\delta) \geq c\Vert\delta\Vert^2$ on $\Vert\delta\Vert \leq R$, $c \gt 0$ — the update's correction direction points inward. Conclusion: $F(\delta) = \eta^\ast H g(\delta)$ satisfies A2' with $\alpha = \eta^\ast c_{\min}$ (per-event; $\times\nu$ per-time). Asymmetry: **two-point/incremental sector** $(F(\delta_1)-F(\delta_2))^T(\delta_1-\delta_2) \geq \alpha\Vert\delta_1-\delta_2\Vert^2$ ⟺ local strong convexity (Nesterov 2.1.10); **one-point sector** (A2' at the equilibrium) is strictly weaker — implied by strong convexity, converse false. AAT's persistence machinery requires only the one-point form; the composition bridge lemma (DA2'-inc) requires the two-point form. Counterexample: $L'(x) = x(1+\tfrac12\sin 10x)$ — satisfies $x L'(x) \geq \tfrac12 x^2$ globally (one-point sector, $\alpha = 1/2$) yet $L''(\pi/10) \lt 0$ (not convex near 0).

### A18 [mental-model] (b09-1.5 — 09-batch-meta-architecture-quiz-questions.md)

Diagnostic: **there must be a tempting wrong merge** — a definition is an instance only if it names the quantity it is routinely confused with and says why turning the wrong knob is the error. Inverse case: **refusing a spurious split** — recognizing two distinct causes drive the *same* knob and share one remedy; example: #scope-edge-update-causal-validity, where observability failure and identifiability failure both freeze an edge's effective gain.

### A19 [math] (b05-2.5 — 05-batch-tempo-sector-quiz-questions.md)

Conditions: (1) cross-channel noise independence (additivity then *derived* exact); (2) shared eigenbasis / isotropy (for the scalar form; else the tensor form is the correct object). Trap answer: **no** — the additive form is *not* a general upper bound. The deviation is **signed**: common-source (echo-chamber) correlation makes it overcount (closed-form redundancy penalty; saturation at the shared-bias floor under persistent bias), but noise-cancelling/synergistic configurations make it **undercount**. The upper-bound reading was explicitly refuted in the corpus (a sign-blind measure like CMI cannot even carry the correction).

### A20 [mental-model] (b01-1.6 — 01-batch-ch1-foundations-quiz-questions.md)

It encodes causal irreversibility: $a_{t-1}$ was committed before $o_t$ arrived, so the agent could not have used $o_t$ to choose $a_{t-1}$. The interleaving is the record of what information was available when — the substrate for every later claim about update ordering and identity.

