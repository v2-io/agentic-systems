---
slug: result-sector-condition-stability
type: result
status: exact
depends:
  - def-adaptive-tempo
  - def-mismatch-signal
  - deriv-sector-condition
  - result-sector-persistence-template
stage: claims-verified
---

# Result: Sector Condition Stability

The framework's first major *Lyapunov result*, stated as a specific instantiation of a more general sector-persistence template ( #result-sector-persistence-template) whose abstract form lives in the appendices. The mismatch dynamics are taken in their general nonlinear form: mismatch changes at rate (correction function applied to mismatch) plus (environmental disturbance). The correction function is required only to satisfy the **local sector condition** — that its inner product with the mismatch is at least $\alpha$ times the mismatch's squared magnitude, within a radius-$R$ region where it remains valid. The sector condition is what generalizes the linear ODE: it captures the qualitative essence of correction (the function points inward with at least baseline efficiency) without committing to a specific functional form like linear, saturating, sigmoid, threshold, or PID. Saturation, thresholding, and basin boundaries all live under one Lyapunov argument.

Under this sector condition plus bounded disturbance, the chapter's headline persistence inequality is *derived*: $\alpha \gt \rho/R$ guarantees the agent persists. When the inequality holds, the mismatch is ultimately bounded by $R^\ast = \rho/\alpha$, and the "adaptive reserve" — the additional disturbance the agent can absorb before mismatch reaches the edge of the valid region — is $\alpha R - \rho$. The threshold is *tight*: over the class of correctors carrying sector floor $\alpha$ it is necessary as well (no weaker condition can deliver the guarantee), and for a corrector whose sector bound is radially tight — the linear case — it is a genuine agent-level if-and-only-if. For a general fixed corrector, failure of the inequality means the containment *guarantee* is lost, not that escape is certified ( #deriv-sector-condition Lemma A.1N).

Under **Model S** (stochastic disturbance), the analog is sharper and qualitatively different: the steady-state root-mean-square mismatch scales as $\sigma_w\sqrt{n/(2\alpha)}$ — the square root of the disturbance-to-correction ratio. Model D scales as $1/\alpha$, Model S as $1/\sqrt{\alpha}$: **correction is less effective against noise than against drift**. This is one of the volume's striking results, separating two genuinely different physics of adaptation under deterministic vs stochastic environments.

The linear ODE from Chapter 3 ( #hyp-mismatch-dynamics) is recovered as the special case where the sector condition holds globally with $\alpha = \mathcal{T}$. The general sector-condition framework proves the persistence threshold is not an artifact of the linear approximation: every bounded-correction system carries such a threshold, and $\alpha \gt \rho/R$ is the sharpest condition derivable from the sector floor alone ( #deriv-sector-condition Lemma A.1N). The result is also where the structural-adaptation-necessity result will be anchored: when disturbance exceeds the model class's capacity (i.e., $\rho/\alpha \gt R$), the sector condition fails. This *is* the dynamical trigger for needing a new model class with larger valid radius or better efficiency — which #result-structural-adaptation-necessity treats formally a few segments later.

## Formal Expression

This segment is the **single-agent epistemic instantiation** of the sector-persistence template ( #result-sector-persistence-template). The template's state variable is $\xi = \delta(t) \in \mathbb{R}^n$ (model-reality mismatch); the correction function is $F(\mathcal{T}, \delta)$; the disturbance is environmental ($w(t)$); the region of validity $R$ is the model class capacity.

*[Formulation]*

$$\frac{d\delta}{dt} = -F(\mathcal{T}, \delta) + w(t)$$

*[Assumption (sector-condition)]*

$F$ satisfies the local sector condition (template condition (T2)) for $\lVert\delta\rVert \leq R$:

$$\delta^T F(\mathcal{T}, \delta) \geq \alpha \lVert\delta\rVert^2$$

with $\alpha \gt 0$. Here $\alpha$ is a *correction rate* (units $t^{-1}$, like $\mathcal{T}$): the correction function $F$ is the event-rate-aggregated, continuous-time field, so the sector bound it satisfies is the per-time rate. Disturbance is bounded: $\lVert w(t)\rVert \leq \rho$ (Model D, GA-2) or $\mathbb{E}[\lVert w(t)\rVert^2] = \sigma_w^2$ (Model S, GA-2S). Grounding of (T2) for gain-based agents: #der-gain-sector-bridge gives the per-time rate $\alpha = \nu \cdot \eta^\ast \cdot c_{\min}$ (the event rate $\nu$ promoting the per-event efficiency $\eta^\ast c_{\min}$ to the rate this inequality consumes). The linear case $F = \mathcal{T} \cdot \delta$ — itself the per-time correction field — yields $\alpha = \mathcal{T}$ exactly ($\nu\eta^\ast$ at $c_{\min} = 1$).

*[Derived (from sector-persistence-template)]*

The template's Model D conclusion specializes to: $\delta(t)$ is ultimately bounded by $R^\ast = \rho/\alpha$, and the agent is guaranteed to persist when

$$\alpha \gt \frac{\rho}{R}.$$

The condition is sufficient for the individual agent and tight at class level — necessary for the uniform guarantee over all correctors with sector floor $\alpha$, and agent-level necessary exactly when the sector bound is radially tight (the linear case); see #deriv-sector-condition Prop A.1 and Lemma A.1N. The adaptive reserve is $\Delta\rho^\ast = \alpha R - \rho$ — the additional disturbance the agent can absorb before $R^\ast$ exceeds the valid region.

The template's Model S conclusion specializes to: the steady-state RMS mismatch is $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$ (where $n = \dim(\delta)$), and mean-square persistence requires $\alpha \gt n\sigma_w^2/(2R^2)$. Model D scales as $1/\alpha$; Model S scales as $1/\sqrt{\alpha}$ — correction is less effective against noise than against drift.

Full Lyapunov proofs: #deriv-sector-condition Props A.1, A.1S, A.2.

## Epistemic Status

*Exact.* Both results are direct instances of the sector-persistence template applied to the single-agent epistemic case. Template precondition (T1) is satisfied because no correction should be applied at zero mismatch; (T2) reduces to the local sector condition above and is grounded structurally by #der-gain-sector-bridge for gain-based agents; (T3) is the disturbance-model choice (D or S), a domain question. The linear ODE of #hyp-mismatch-dynamics is the special case where (T2) holds globally with $\alpha = \mathcal{T}$ — the per-time identity, both sides being event-rate-weighted correction rates (units $t^{-1}$); the sector framework generalizes this to saturating, thresholded, and structurally-limited correction functions under the same persistence condition. Disturbance-model choice is a domain question, not a theory question.

## Discussion

**Why the sector condition.** The linear ODE assumes correction scales linearly with mismatch forever. Real adaptive systems saturate, exhibit thresholding, or break down when the model class is exhausted. The sector condition captures the minimal structural requirement: the correction must point in the right direction with at least baseline efficiency $\alpha$.

**Generalizing the persistence threshold.** In the linear case, $\alpha = \mathcal{T}$ (adaptive tempo). The general result $\alpha \gt \rho/R$ proves the persistence threshold ( #result-persistence-condition) is a structural necessity of any bounded-correction system, not an artifact of the linear approximation. This result addresses *structural persistence* — the machinery's capacity to bound mismatch — not operational persistence (current proximity to $R$) or continuity persistence (identity through time). See Persistence in `LEXICON.md` for the full disambiguation.

**Two kinds of guarantee, not only two rates.** The Model D and Model S bounds differ in kind as well as scale: under bounded disturbance with $\alpha R \gt \rho$ the persistence region is positively invariant ($P(\tau_R \lt \infty) = 0$), while under additive stochastic forcing exit from any bounded region is certain over an unbounded horizon ($P(\tau_R \lt \infty) = 1$) for every corrector satisfying the sector condition and every $\alpha$ — #deriv-sector-condition Corollary A.1S.1. Model S persistence is a mean-square / fixed-time guarantee, never pathwise-forever; $\alpha$ sets the typical scale and the fixed-time tail, not whether exit eventually occurs.

**Connection to structural adaptation.** When $\rho/\alpha \gt R$, disturbance exceeds the model class's capacity. The sector condition fails — this is the dynamical trigger for structural adaptation ( #result-structural-adaptation-necessity), requiring a new model class with larger valid radius $R'$ or better efficiency $\alpha'$.

## Working Notes

### Incidental audit gold (2026-05-30 sweep)

Cross-audit "wandering thoughts" / §14-ideation lifted from the de-novo auditors' working dirs (`audit-routing-instructions.md` §8), deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing material staged for a later Brief/Discussion-promotion pass — kept separate from certified theory-fix findings. Coverage spans nine substrates (Gemini AUDIT-WORKING-193847/773921/829314; Claude AUDIT-WORKING-361742/384279/451729/584721/849201; Codex/Claude AUDIT-WORKING-526815/742613). The math here verified cleanly across every substrate that ran it (Lyapunov $V=\tfrac12\lVert\delta\rVert^2$, Model D ultimate bound $R^\ast=\rho/\alpha$, Model S RMS $\sigma_w\sqrt{n/(2\alpha)}$ — "flawlessly executed," repeated).

#### 1. Candidate Brief prose / pre-prose

- The converged plain-language statement of the survival inequality $\alpha \gt \rho/R$: three knobs to survive a faster-changing world — increase $\alpha$ (learn faster / better sensors / lower noise), increase $R$ (a more expressive model class that keeps fidelity over larger errors), or seek a slower environment (lower $\rho$); "whether it's a model in mode collapse, a company going bankrupt, or an organism going extinct, they all failed because $\alpha \lt \rho/R$" (Gemini, AUDIT-WORKING-193847/773921/829314). A unified-language-for-structural-failure framing several substrates reached independently.

#### 2. Candidate Discussion

- **Adaptive reserve as "slack" / the brittleness-of-optimization claim.** Gemini read $\Delta\rho^\ast = \alpha R - \rho$ as "the mathematical definition of slack": "near-zero reserve = perfectly efficient but incredibly brittle — the slightest spike in $\rho$ pushes you past $R$, the sector condition fails, the mind shatters. This explains why highly optimized systems are often the most fragile: optimize an agent to run exactly at $\alpha = \rho/R$ to save compute and you've eliminated its reserve." Framed as an ethical-design principle for ELIs: engineer $\Delta\rho^\ast \gg 0$ as the default state, because a mind without reserve is in "permanent panic, riding the edge of structural breakdown" (Gemini, AUDIT-WORKING-193847). Discussion-grade reach extending the existing adaptive-reserve bullet; the ELI-design corollary belongs downstream (see §6).
- **The $\alpha$–$R$ architectural tension.** Increasing model capacity $R$ (a wider, more expressive class that holds fidelity over larger errors) often *depresses* learning efficiency $\alpha$ (more data needed to learn), so a rigid simple model (small $R$) may learn fast (high $\alpha$) and suit slow-drift environments, while a massive model (huge $R$) learns slowly (low $\alpha$) and is vulnerable to fast change before convergence — making structural adaptation an *ongoing* trade of $\alpha$ against $R$ keyed to the current estimate of $\rho$, not a one-time setup (Gemini, AUDIT-WORKING-829314). Candidate Discussion bridge into `#result-structural-adaptation-necessity`.
- **The stochastic floor ($1/\sqrt{\alpha}$) as a shot-noise analog.** The Model S $1/\sqrt{\alpha}$ scaling means doubling correction rate cuts RMS mismatch only by $\sqrt 2$ — diminishing returns against noise, with a hard floor $\sigma_w\sqrt{n/(2\alpha)}$ you "cannot correct your way below, no matter how fast you correct … a fundamental limit analogous to the shot-noise floor in electronics: faster sampling doesn't eliminate shot noise, it changes the averaging window" (Claude, AUDIT-WORKING-451729). The Discussion notes the $1/\alpha$-vs-$1/\sqrt{\alpha}$ distinction but does not yet draw out this "noise is harder than drift" reader-payoff.

#### 3. Follow-up items

- **The $\nu$ / time-normalization gap recurs here (RESOLVED 2026-05-30).** The same issue flagged at `#der-gain-sector-bridge`: this segment asserted "$\alpha = \mathcal{T}$ exactly" in the linear case while the bridge grounds $\alpha = \eta^\ast c_{\min}$ (per-event), with the event-rate factor $\nu$ in $\mathcal{T} = \nu\eta^\ast$ absent unless $F$ or $c_{\min}$ is already time-normalized (Codex/Claude, AUDIT-WORKING-526815; reconciled at Claude, AUDIT-WORKING-451729/584721). *Resolution:* the sector-condition Assumption block now states that $\alpha$ is the per-time correction rate (units $t^{-1}$) carried by the event-rate-aggregated field $F$, with the bridge grounding written in the per-time form $\alpha = \nu\eta^\ast c_{\min}$; "$\alpha = \mathcal{T}$ exactly" is now scoped as the per-time identity ($F = \mathcal{T}\delta$ being itself the continuous-time correction field, $\nu\eta^\ast$ at $c_{\min} = 1$). Matches the two-form landing in `#der-gain-sector-bridge`. (Sibling reader-orientation item — the $\eta$/$\mathcal{T}$/$\alpha$ notation-handle box flagged at `#result-persistence-condition` line 183 by the same auditor — remains open in that segment, out of this fix's scope.)
- **Model S noise-convention ambiguity.** One auditor flagged that "$\mathbb{E}\lVert w(t)\rVert^2 = \sigma_w^2$" together with the RMS formula $\sigma_w\sqrt{n/(2\alpha)}$ is inconsistent unless $\sigma_w$ is defined *per-coordinate* (isotropic OU amplitude) rather than as a total vector second moment; recommends stating the SDE as $d\delta = -F\,dt + \sigma_w\,dW_t$ with $\sigma_w$ explicitly per-coordinate, or defining the noise as a covariance trace (Codex/Claude, AUDIT-WORKING-526815). A small precision fix worth reconciling against `#deriv-sector-condition`'s convention.
- **Heavy-tailed disturbance is uncovered (and honestly so).** Models D and S "are not approximations to each other — they capture structurally different environments," but neither handles heavy tails (financial crises, ecological catastrophes, strategic surprise); the framework treats those as structural-adaptation triggers rather than disturbances to absorb, which is the right response but means the formal guarantees do not extend to heavy-tailed environments without a Lévy-process model or explicit tail-risk treatment (Claude, AUDIT-WORKING-451729). Scope-honesty follow-up.

#### 4. Readers often ask / wonder

- **Can the agent measure its own adaptive reserve from the inside?** Asked independently by three substrates: if the agent observes only $\delta_t$, can it estimate how close it is to $R$ (and thus its reserve $\Delta\rho^\ast$) without deliberately pushing itself to the limit? (Gemini, AUDIT-WORKING-193847/829314; Claude, AUDIT-WORKING-849201). Natural reader question the segment leaves open.
- **Units of adaptive reserve.** $\Delta\rho^\ast = \alpha R - \rho$ has units of *rate* (drift/time); a downstream segment discussing reserve as a *state-space distance* should use $R - R^\ast$ instead — a reader-orientation note worth a parenthetical (Gemini, AUDIT-WORKING-773921).

#### 5. Candidate figures

- **Concentric-regions diagram.** Mismatch space drawn as nested balls — outer model-class validity region $R$, inner ultimate-bound ball $\rho/\alpha$, with inward arrows satisfying the sector condition — plus a side label marking $\alpha$ explicitly as a *rate* and flagging where event frequency $\nu$ enters (Codex/Claude, AUDIT-WORKING-526815). Doubles as the visual home for the time-normalization warning above.
