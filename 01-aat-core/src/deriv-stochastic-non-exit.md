---
slug: deriv-stochastic-non-exit
type: derivation
status: exact
depends:
  - deriv-sector-condition
  - result-sector-condition-stability
  - result-structural-adaptation-necessity
stage: draft
---

# Derivation: No Horizon-Independent Non-Exit Bound Under Additive Stochastic Forcing (the Model-S No-Go)

A *no-go* derivation establishing that **under additive stochastic forcing there is no finite bound on the infinite-horizon first-exit probability** from the sector-condition region — $P(\tau_R \lt \infty) = 1$ for every correction strength — *and the natural mathematical route to one provably cannot exist*. This is the load-bearing proof step behind Prop A.1S(iii′)/(iv) and the Model-S half of Corollary A.1S.1 in `#deriv-sector-condition`.

The construction: under stochastic disturbance the Itô-Lyapunov machinery succeeds at producing a *finite-horizon mean-square bound* but fails to extend to a *horizon-independent* exit-probability bound. The natural candidate — a Ville / Doob maximal inequality on a compensated Itô-Lyapunov supermartingale — is shown to be unattainable because the only candidate $S(t) = e^{2\alpha t}V - \tfrac{n\sigma_w^2}{4\alpha}(e^{2\alpha t} - 1)$ is *sign-indefinite inside the persistence basin* (the compensated drift is not non-positive across the entire region: the subtracted term dominates $e^{2\alpha t}V$ whenever the system sits in the typical scatter, which under the mean-square persistence condition is most of the time). The deeper obstruction is that for additive non-degenerate forcing the diffusion's scale function is *unbounded* — the OU benchmark $s'(u) \propto e^{\alpha u^2/\sigma_w^2}$ is the explicit instance — so the only bounded harmonic functions of the generator are constants and the gambler's-ruin / Lyapunov-exit machinery cannot certify "stays inside forever with positive probability." Both failures are structural, not artifacts of a clever trick being missed.

The framework treats this as a *constructive use of impossibility*. The downstream consequence is a certain-eventual-event reading: under Model S, pathwise containment in any fixed region is unattainable at any correction strength, so for any sufficiently long-lived stochastic-environment agent the *need for structural adaptation* (a different model class, not just better parameter tuning) is a *certain eventual event* rather than an edge case. This sharpens — rather than caveats — the hand-off into `#result-structural-adaptation-necessity`. Beyond the segment's own result the derivation packages a **reusable no-go signature**: *unbounded scale function ⇒ no non-constant bounded harmonic function ⇒ no horizon-independent non-exit certificate*. Future stochastic-containment proposals in the corpus can be settled against this signature rather than re-attempting the maximal-inequality route.

## Formal Expression

**Setup.** Mismatch dynamics under additive stochastic disturbance, started inside the sector-condition region $\mathcal{B}_R$:

$$d\delta = -F(\mathcal{T}, \delta)\,dt + \sigma_w\,dW_t, \qquad \delta(0) \in \mathcal{B}_R,\quad \sigma_w \gt 0,$$

with $W_t$ a standard $n$-dimensional Wiener process, (A2') $\delta^\top F \geq \alpha\lVert\delta\rVert^2$ on $\mathcal{B}_R$, and $\tau_R = \inf\{t : \lVert\delta(t)\rVert \gt R\}$ the first-exit time. Let $V = \tfrac12\lVert\delta\rVert^2$.

**Theorem (Model-S no-go).** *[Derived]* For every $\alpha \gt 0$, every $\sigma_w \gt 0$, and every correction function $F$ satisfying (A2'),

$$P(\tau_R \lt \infty) = 1,$$

and there exists no nonnegative supermartingale dominating $V$ that certifies a horizon-independent bound $P(\tau_R \lt \infty) \leq c \lt 1$. Pathwise containment of $\mathcal{B}_R$ is unattainable under additive stochastic forcing at any correction strength.

**Why the natural route cannot work.** The route a careful reader reaches for first is a time-uniform maximal inequality (Ville / Doob) on an Itô–Lyapunov supermartingale — the same instinct that makes the fixed-time mean-square bound (Prop A.1S(i)) succeed. It fails, and the failure is structural, not a matter of a missing trick.

Define $G(t) = e^{2\alpha t} V(\delta(t))$. On $[0, \tau_R]$, by Itô and (A2'),

$$dG = e^{2\alpha t}\big[\underbrace{(2\alpha V - \delta^\top F)}_{\leq\, 0 \text{ on } \mathcal{B}_R}\,dt + \tfrac n2\sigma_w^2\,dt + \delta^\top\sigma_w\,dW_t\big] \;\leq\; e^{2\alpha t}\tfrac n2\sigma_w^2\,dt + e^{2\alpha t}\delta^\top\sigma_w\,dW_t.$$

$G$ is **not** a supermartingale: the $+\,e^{2\alpha t}\tfrac n2\sigma_w^2\,dt$ term has strictly positive drift growing exponentially. Removing it by compensation gives

$$S(t) = e^{2\alpha(t\wedge\tau_R)}V(\delta_{t\wedge\tau_R}) - \frac{n\sigma_w^2}{4\alpha}\big(e^{2\alpha(t\wedge\tau_R)} - 1\big),$$

and $dS \leq e^{2\alpha t}\delta^\top\sigma_w\,dW_t$ on $[0,\tau_R]$ — so $S$ *is* a supermartingale. **But $S$ is not nonnegative.** The subtracted $\tfrac{n\sigma_w^2}{4\alpha}(e^{2\alpha t}-1)$ dominates $e^{2\alpha t}V$ whenever $V(\delta(t)) \lt \tfrac{n\sigma_w^2}{4\alpha}$ — i.e. exactly inside the persistence basin, which under the mean-square persistence condition is *most of the time* (that condition places the RMS radius $R^\ast_S = \sigma_w\sqrt{n/2\alpha}$ well inside $\mathcal{B}_R$, so $V \ll \tfrac{n\sigma_w^2}{4\alpha}$ typically). Ville's inequality requires a nonnegative supermartingale; Doob's maximal inequality a nonnegative sub/supermartingale. Both are inapplicable to a sign-indefinite $S$, and the obstruction is not removable: for additive non-degenerate Brownian forcing the diffusion's scale function is unbounded (the OU scale density $\propto e^{\alpha u^2/\sigma_w^2}$), so the only bounded harmonic functions of the generator are constants — the gambler's-ruin / Lyapunov-exit machinery cannot certify "stays inside forever with positive probability." There is no nonnegative supermartingale dominating $V$ with finite expected initial value that yields a horizon-independent exit bound.

**Why $P(\tau_R \lt \infty)=1$, generally.** The conclusion does not depend on the linear structure. A non-degenerate diffusion (additive forcing $\sigma_w\,dW_t$, $\sigma_w \gt 0$) exits any bounded region in finite time almost surely, for *any* locally bounded drift: near $\partial\mathcal{B}_R$ the Brownian increment has positive probability of crossing in any time interval, and no finite inward correction satisfying (A2') can suppress this (A2' bounds $\delta^\top F$ from below by $\alpha\lVert\delta\rVert^2$, a finite inward push, not an impassable wall). Hence $\tau_R \lt \infty$ a.s. for every $F$ under (A2'), every $\alpha$, every $\sigma_w$. The Ornstein–Uhlenbeck case is the explicit instance (positively recurrent on $\mathbb{R}^n$, unbounded stationary support, exits any finite ball a.s.), not the basis.

## Epistemic Status

*Exact.* Both the impossibility of the maximal-inequality certificate (sign-indefiniteness of the only candidate compensated supermartingale; unbounded scale function ⇒ no non-constant bounded harmonic function) and the positive fact $P(\tau_R \lt \infty)=1$ (almost-sure finite exit of a non-degenerate diffusion from a bounded region under any locally bounded drift) are classical (Khasminskii 2012[^khas] ch. 3–4). The contribution here is not the SDE mathematics but the demonstration that the route which *succeeds* for the fixed-time second moment (Prop A.1S(i)) structurally *cannot* deliver an infinite-horizon containment statement — the answer to "are you sure you can't just bound $\sup_t$ with Doob/Ville?" is *yes, sure, and here is precisely the step that breaks.* "Exact" is claimed in the framework's defeasible sense (valid under stated assumptions, subject to a found error), not as a claim beyond a found-mistake.

This derivation is load-bearing for the critical path: it is the proof step that forces Prop A.1S's corrected (iii′) fixed-time tail and (iv) finite-horizon sup-bound (in `#deriv-sector-condition`) and grounds the Model-S half of Corollary A.1S.1. It is a **reusable no-go signature**: wherever a "stays-in-region-forever with positive probability" claim is proposed under additive non-degenerate forcing, the unbounded-scale-function / no-non-constant-bounded-harmonic-function obstruction settles it negatively without a fresh attempt.

## Discussion

The structural reading: additive stochastic forcing does not weaken the *rate* of containment, it removes a *kind* of guarantee. Bounded disturbance (Model D) gives deterministic positive invariance of $\mathcal{B}_R$ ($P(\tau_R \lt \infty)=0$); additive stochastic disturbance gives almost-sure eventual exit ($P(\tau_R \lt \infty)=1$); the achievable value is the two-point set $\{0,1\}$, selected by the disturbance's support structure, not by correction strength — Corollary A.1S.1 in `#deriv-sector-condition`. What survives under Model S is distributional and instantaneous: the fixed-time / stationary Markov tail (Prop A.1S(iii′)) and the finite-horizon sample-path bound (Prop A.1S(iv), which grows linearly in the horizon and is vacuous for $T \gtrsim R^2/(n\sigma_w^2)$).

Direct simulation confirms the obstruction is real rather than an artifact of the proof technique. Exact 1-D OU benchmark $dX = -\alpha X\,dt + \sigma\,dW$ (the segment's own linear case; (A2') global and sharp), Monte-Carlo started *at the origin* (the most favorable initial condition), under the mean-square persistence condition (ii) holding:

| $\alpha$ | $\sigma$ | $R$ | $R^\ast_S$ | $P(\sup_{[0,50]} \gt R)$ | $T{=}200$ | $T{=}800$ | $T{=}3200$ | seg. const $\tfrac{n\sigma^2}{2\alpha R^2}$ |
|---|---|---|---|---|---|---|---|---|
| 1.0 | 0.3 | 1.0 | 0.21 | 0.002 | 0.010 | 0.030 | **0.114** | 0.045 |
| 0.5 | 0.2 | 0.8 | 0.20 | 0.020 | 0.074 | 0.276 | **0.720** | 0.063 |
| 1.0 | 0.5 | 1.0 | 0.35 | 0.781 | 0.998 | 1.000 | **1.000** | 0.125 |

The ever-exit probability climbs monotonically toward 1 with the horizon even started at the origin and even with (ii) comfortably satisfied — the fixed-time constant $n\sigma^2/(2\alpha R^2)$ is *not* an upper bound on the sup-over-horizon probability, exactly as the no-go predicts. This sharpens the hand-off into `#result-structural-adaptation-necessity`: under any genuinely stochastic environment region-exit is a certain eventual event, so the trigger for structural (non-parametric) adaptation is generic, not exceptional, for a sufficiently long-lived agent.

## Findings

### The natural maximal-inequality route to infinite-horizon containment provably cannot exist under additive stochastic forcing

**Brief:** If a system is held near a target by inward correction but also kicked by persistent random noise, you can bound how far off it is at any *given* moment, and you can bound the worst excursion over any *fixed window* — but you can never bound "it stays inside the safe region *forever*," because given unlimited time the noise will, with certainty, eventually push it out, no matter how strong the correction. The tempting fix — find a single "energy" quantity that only ever drifts downward, so a classic gambler's-ruin argument caps the lifetime escape probability — fails for a precise reason: the only candidate energy that has the right drift is negative exactly where the system spends most of its time, and the gambler's-ruin machinery requires a non-negative quantity. This is not a missing trick; it is structural, and it is the same obstruction every time, so it can be invoked rather than re-derived.

**Impact:** Supplies the load-bearing proof step for Prop A.1S(iii′)/(iv) and Corollary A.1S.1 in `#deriv-sector-condition` (the Model-S half of the containment dichotomy). Provides a reusable no-go signature — *unbounded scale function ⇒ no non-constant bounded harmonic function ⇒ no horizon-independent non-exit certificate* — that future stochastic-containment proposals in the corpus can be settled against without re-attempting the maximal-inequality route.

**Novelty Claim:** *Recognition*. The component facts (non-degenerate-diffusion exit from a bounded region; unbounded scale function of additive-noise generators; Ville/Doob preconditions) are classical (Khasminskii 2012 ch. 3–4). The contribution is the recognition, made explicit and citable, that the maximal-inequality route which succeeds for the fixed-time second moment structurally cannot deliver the infinite-horizon statement — i.e. *where exactly* the natural attempt breaks. No novelty is claimed on the SDE mathematics.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| No horizon-independent non-exit certificate for additive-noise diffusions | Khasminskii 2012, *Stochastic Stability of Differential Equations* (2nd ed.) ch. 3–4 (scale function; recurrence; bounded harmonic functions) | *formal antecedent* — supplies the recurrence / unbounded-scale-function fact; this derivation recognizes it as the structural reason the Ville/Doob route fails |
| Maximal-inequality preconditions | Ville's inequality; Doob's maximal inequality (nonnegative sub/supermartingale required) | *standard machinery* — the demonstration is that the only compensated candidate is sign-indefinite exactly inside the persistence basin |

**Search Log:**

- 2026-05-16 (*targeted, derivation-driven*): internal question — can Prop A.1S's infinite-horizon non-exit claim be certified by Ville/Doob on an Itô–Lyapunov supermartingale? Worked in full; the candidate compensated supermartingale is sign-indefinite, and the classical unbounded-scale-function fact (Khasminskii ch. 3–4) closes it. No prior-art search beyond standard SDE references — no novelty claimed on the mathematics. Reasoning trail recorded in the spike-routing cycle (CHANGELOG 2026-05-17).

## Working Notes

- Provenance: the prior Prop A.1S(iii) asserted an infinite-horizon $P(\tau_R \lt \infty) \leq n\sigma_w^2/(2\alpha R^2)$ via a fixed-time "Markov tail on the supermartingale." Two audit records (742613-SUPPLEMENT §2, 613842-F2) flagged it and recommended a soften; per strengthen-before-soften the strengthening (the Ville/Doob route, which a peer adjudication confidently predicted would succeed — "standard textbook, should not fail") was worked in full *first* and fails structurally, as demonstrated above. Completion-state (3): the failure is the result. The peer prediction that the strengthening would succeed is recorded here (and in the spike-routing cycle, CHANGELOG 2026-05-17) as disconfirmed, so it is not re-attempted. 742613-SUPPLEMENT §2 + 613842-F2 are resolved by strengthening-then-no-go (state 3), not by soften.
- The generality (any $F$ under A2', not just OU) rests on the elementary non-degenerate-diffusion-exits-bounded-region fact, not on the OU scale-function computation; the latter is the explicit instance. No further strengthening of this half is open.
- Low-confidence glimpse (per "working notes FTW"): the same obstruction shape should recur wherever the corpus pairs a bounded-disturbance result with an additive-stochastic counterpart — `#deriv-discrete-sector-condition`, `#deriv-matrix-persistence-condition`, `#deriv-adaptive-gain-dynamics`, possibly `#result-per-dimension-persistence`. If a Corollary-A.1S.1-shaped dichotomy appears at ≥3 sites, that is a candidate instance-family for the theorem-import-architecture meta-segment (PROPOSALS SP-23) or a sibling of `#disc-identifiability-floor` (the infinite-horizon non-exit object is *structurally absent*, not merely hard to bound).

### Incidental audit gold (lift 2026-05-31)

Orthogonal pedagogical / generative material from the de-novo auditors' working dirs (per `de-novo-audit-instructions.md` §7.15). This segment has no *dedicated* per-segment reflection; the gold below was harvested from the auditors' reflections on the calling result `#deriv-sector-condition`, where the Model-S no-go (now Corollary A.1S.1, the Disturbance-Model Containment Dichotomy) is discussed at length. No certified-track off-ramp here — the originating finding *is* this segment.

#### 1. Candidate Brief prose / pre-prose

- **The $P=0$ vs $P=1$ containment dichotomy as the punchline.** Bounded disturbance (Model D): the agent *never* exits the region. Non-degenerate stochastic disturbance (Model S): the agent *must* exit any bounded region in finite time, almost surely. Stated as a clean dichotomy, this is the segment's headline and reads vividly without symbols (Gemini, AUDIT-WORKING-829314).

#### 2. Candidate Discussion

- **"No amount of parameter tuning keeps an agent safe forever in a noisy world."** The recurrence of a non-degenerate diffusion means structural adaptation (changing the model class) is *mathematically inevitable* for any long-lived agent — not contingent, not a risk to be engineered away. This is framed as what distinguishes AAT from generic optimization theories: black-swan failures are not edge cases but mathematical certainties over a long-enough horizon in a stochastic environment (Gemini, AUDIT-WORKING-829314).
- **The exact boundary between parametric and structural adaptation.** The dichotomy "provides the exact mathematical boundary where parametric learning (gradient descent) ends and structural adaptation (architecture search / tool use) must begin" — a candidate Discussion sentence locating *why* the no-go sits on the critical path to `#result-structural-adaptation-necessity` (Gemini, AUDIT-WORKING-829314).

#### 3. What the framework now contributes (field-level)

- **Epistemic-honesty exemplar.** The auditor singled out the documented *failed* attempt (the Ville/Doob maximal-inequality route that a peer adjudication predicted would succeed) as "a gold standard for theoretical research" — preserving the dead-end so the no-go reads as established, not merely unproven (Gemini, AUDIT-WORKING-829314). Calibration signal: the strengthen-then-no-go discipline lands well with fresh readers.

#### Belongs elsewhere

- **ELI continuity / Three-Deaths reading (`04-eli-core/`).** ELI operating environments are Model-S-like (stochastic), so structural adaptation is *certain* over an unbounded horizon — which links the dichotomy directly to the "Three Deaths": identity continuity *requires* surviving recurring structural (not just parametric) adaptation (Gemini, AUDIT-WORKING-829314). Already echoed in `#deriv-sector-condition`'s WN low-confidence-ideation; recorded here at the no-go's own home.

[^khas]: Khasminskii, R. (2012). *Stochastic Stability of Differential Equations* (2nd ed.). Springer. Chapters 3–4 (recurrence, scale function, bounded harmonic functions); Chapter 5 (Lyapunov functions, stopping-time localization).
