# Spike: Interaction-Channel Classification — the Recipient-Side Theory

**Status**: Structural spike. Formalization of recipient-side reception of inter-agent signals within AAD's existing machinery. First pass — proposes a derived classification boundary, establishes scope, flags what the machinery can and cannot carry.

**Date**: 2026-04-22

**Motivation**: AAD has emitter-side Section III results — `#adversarial-destabilization`, `#adversarial-tempo-advantage`, `#observation-gates-advantage`, `#symbiogenic-composition` in part — that describe what happens when one agent's praxis couples into another's disturbance rate. What AAD does *not* have is a systematic recipient-side theory: given an incoming signal $a$ from emitter $A$, what determines whether recipient $B$ absorbs it as an informative update, a destabilizing shock, or ambient noise? The three regimes have different dynamics — they land at different terms of $B$'s sector-persistence template with qualitatively different effects on $(M_B, \Sigma_B, \kappa_B)$ — and the choice among them is not something the emitter decides. It is forced by the interaction of $B$'s internal state with the signal's information content.

This spike proposes the classification boundary and checks it against AAD's existing machinery.

**Depends on**: #observation-function, #mismatch-signal, #mismatch-decomposition, #update-gain, #adaptive-tempo, #model-class-fitness, #model-sufficiency, #structural-adaptation-necessity, #persistence-condition, #sector-persistence-template, #adversarial-destabilization, #adversarial-tempo-advantage, #observation-gates-advantage, #symbiogenic-composition, #communication-gain, #team-persistence, #discussion-identifiability-floor, #agent-identity.

---

## 1. Problem Statement

### 1.1 The recipient-side question

Let $A$ and $B$ be two purposeful agents coupled through a shared environment. $A$ acts, producing either a direct signal (communication) or an environmental perturbation whose shadow reaches $B$ through $B$'s observation channel. Write the incoming stream — whatever form it takes — as an event $e_\tau$ entering $B$'s update at time $\tau$.

On $B$'s side, the event is processed by the standard AAD machinery:

- $B$'s observation function $h_B$ maps the $A$-induced environment state and $B$'s own prior action to an observation $o_\tau^B$ ( #observation-function).
- $B$'s model $M_B$ yields a prediction $\hat o_\tau^B$; the mismatch is $\delta_\tau^B = o_\tau^B - \hat o_\tau^B$ ( #mismatch-signal).
- $B$'s update rule $f_B$ absorbs $\delta_\tau^B$ with gain $\eta_B^\ast$ ( #update-gain).
- $B$'s strategy $\Sigma_B$ re-evaluates through the orient cascade.

Emitter-side results (e.g., `#adversarial-destabilization`) treat $A$'s contribution as an increment $\gamma_A \mathcal T_A$ to $B$'s effective disturbance rate $\rho_B^{\text{eff}}$, then run the sector-persistence template. That characterization is uniform in the signal: every $A$-event is an increment to $\rho_B$. What it misses is that *the same signal* $e_\tau$ lands differently depending on $B$'s internal state — its prior, model-class fitness, tempo reserve, and the log-odds-space update coordinates on whatever edges the signal touches.

The recipient-side question: **given the signal content and $B$'s internal state, which of three dynamics does $B$ exhibit?**

### 1.2 The three regimes (working partition)

The question suggests a three-way split:

- **Regime I (Informative update)**: $B$ absorbs $e_\tau$ within the sector-condition region. $\delta_B$ is reduced; $M_B$ (or $\Sigma_B$, depending on the signal type) is refined; $\kappa_B$ — where we use Joseph's coupling-coefficient shorthand for $B$'s directed-separation quality or more generally for its adaptive-reserve expenditure on this event — remains positive or improves. This is the classical AAD update: the event rides the sector-persistence template in the expected direction.

- **Regime II (Prediction-error shock / destabilization)**: $\delta_B$ exceeds the sector-condition region $R_B$, or the signal's content lies outside $B$'s model class $\mathcal M_B$, or the update gain collapses. The sector condition fails locally; the correction function does not point inward strongly enough to restore bounded mismatch. The emitter-side `#adversarial-destabilization` story kicks in: $B$ either exits its invariant region (Lyapunov divergence) or begins the structural-adaptation regime of #structural-adaptation-necessity.

- **Regime III (Ambient noise / slow erosion)**: The signal is below $B$'s observability floor — its information content is absorbed into $U_o^B$ but its structural content is not identifiable at the current tempo. $B$ does not update $M_B$ or $\Sigma_B$ but its adaptive reserve $\Delta\rho_B^\ast$ slowly shrinks as the signal accumulates; operationally, $\mathcal T_B$ is being drained against a barely-observable disturbance. This is the "background annoyance" regime: the organization neither learns nor breaks, but its margin against future shocks quietly erodes.

### 1.3 Why the emitter-side results don't reduce to this

The emitter-side view treats $\gamma_A \mathcal T_A$ as a scalar disturbance-rate increment. This collapses the three regimes:

- It cannot distinguish Regime I from Regime III because both are "bounded mismatch after update." Both show as $\lVert\delta_B\rVert_{\text{ss}}$ within $R_B$, but Regime I returns information (model improves) whereas Regime III returns none (reserve drains).
- It captures Regime II as "adaptive reserve exhausted," which is correct but under-specified: the emitter-side story does not distinguish reserve exhaustion via disturbance-magnitude (the signal is just too big) from reserve exhaustion via model-class inadequacy (the signal contains structure $B$ cannot represent, no matter its magnitude). The two failure modes require different repairs — more tempo vs. structural adaptation — yet are collapsed.
- The emitter-side treatment takes $\gamma_A$ as exogenous. The recipient-side view decomposes $\gamma_A$ into properties of $B$'s observation function, prior, model-class fitness, and adaptive-tempo reserve. This decomposition is the content this spike is trying to make formal.

In short, the recipient-side theory is not a rescaling of the emitter-side results. It is a separate classification of which emitter-side result applies — and a characterization of the boundary in $B$'s own state variables.

### 1.4 Scope commitments

This spike works within AAD's existing scope:

- Class 1 (modular) architectures as primary. The classification is stated for agents whose epistemic update is goal-blind ( #directed-separation). Class 3 (partially modular) approximations inherit with degradation proportional to $\kappa_{\text{processing}}$ (see `msc/spike-kappa-hb-operationalization.md`); Class 2 agents require the coupled formulation from `03-logogenic-agents/`.
- Single-recipient analysis. Multi-recipient ($A$ broadcasting to $\{B_1, \ldots, B_n\}$) inherits per-recipient by independence in the emitter-side disturbance decomposition; genuine population dynamics are out of scope (see Section III gaps).
- Singular-trajectory recipient. By #agent-identity, $B$'s sufficiency is trajectory-indexed; the classification is about *this* $B$ on *its* $\mathcal C_t^B$, not about a type.
- Agent-opacity enters as a conditioner on the *emitter*'s predicted effect, not as a reshape of the recipient's classification — see §5.

---

## 2. Formal Setup

Notation, restricted to what this spike needs. All quantities are $B$'s unless marked.

| Symbol | Meaning |
|---|---|
| $M_B$ | $B$'s model state ( #agent-model) |
| $\mathcal M_B$ | $B$'s model class ( #model-class-fitness) |
| $\mathcal F(\mathcal M_B)$ | $B$'s model-class fitness |
| $h_B$ | $B$'s observation function |
| $U_{o,B}$ | $B$'s observation noise on the relevant channel |
| $U_{M,B}$ | $B$'s model uncertainty on the relevant channel |
| $\eta_B^\ast$ | $B$'s optimal gain, $= U_{M,B}/(U_{M,B} + U_{o,B})$ |
| $\mathcal T_B$ | $B$'s adaptive tempo |
| $\alpha_B$ | $B$'s sector-condition lower bound |
| $R_B$ | $B$'s sector-condition region radius (model-class capacity) |
| $\Delta\rho_B^\ast$ | $B$'s adaptive reserve, $= \alpha_B R_B - \rho_B$ |
| $e_\tau^A$ | $A$-originating event arriving at $B$ at $\tau$ |
| $\mathcal I(e_\tau^A)$ | information content of the event conditional on $B$'s prior model |
| $\lVert e_\tau^A\rVert_B$ | the magnitude with which $e_\tau^A$ enters $B$'s mismatch |
| $\iota_B(e_\tau^A)$ | the regime-A identifiability coefficient ( #edge-update-causal-validity) when $e_\tau^A$ affects a strategy-edge decision |
| $H_b^B$ | $B$'s agent opacity (Hafez 2026), $H(S,A \mid S')$ |

The quantities $\lVert e_\tau^A\rVert_B$ and $\mathcal I(e_\tau^A)$ should not be confused. The first is a metric magnitude (how large a perturbation the event produces in $B$'s observation space). The second is an information-theoretic magnitude (how much $B$'s predictive distribution moves conditional on the event). A large-magnitude, already-predicted event has large $\lVert e\rVert$ but small $\mathcal I$; a tiny-magnitude, structurally novel event can have small $\lVert e\rVert$ but large $\mathcal I$. The classification in §3 uses both.

---

## 3. The Classification Boundary

I propose a three-regime partition with boundaries stated entirely in existing AAD quantities. The boundaries are stated first, then derived in §4.

### 3.1 Boundary conditions (proposed)

Event $e_\tau^A$ arriving at $B$ falls into:

**Regime I (Informative update)** when all three hold:

$$\text{(I-a)} \quad \lVert e_\tau^A\rVert_B \leq R_B \qquad \text{(within sector region)}$$

$$\text{(I-b)} \quad \mathcal I(e_\tau^A) \leq \mathcal F(\mathcal M_B) \cdot \mathcal I_{\max}(\mathcal M_B) \qquad \text{(representable within model class)}$$

$$\text{(I-c)} \quad \mathcal I(e_\tau^A) \cdot \nu^{(k)} \geq U_{o,B}^{(k)} \cdot c_\text{floor} \qquad \text{(above observability floor)}$$

where (I-b) reads: the information content required to represent the event is within what the model class can express (normalized by the class's maximum information capacity $\mathcal I_{\max}$; heuristic — see Working Notes), and (I-c) reads: the per-channel event rate carries enough signal to exceed the noise floor at a coefficient $c_\text{floor}$ depending on the desired detection power.

**Regime II (Prediction-error shock / destabilization)** when either:

$$\text{(II-a)} \quad \lVert e_\tau^A\rVert_B > R_B \qquad \text{(exits sector region) — magnitude-shock}$$

or

$$\text{(II-b)} \quad \mathcal I(e_\tau^A) > \mathcal F(\mathcal M_B) \cdot \mathcal I_{\max}(\mathcal M_B) \qquad \text{(outside model class) — structural-shock}$$

with the additional condition that the mismatch generated by the event is sustained long enough that $B$'s correction function cannot discharge it before the next event arrives (i.e., the event falls within the timescale where the disturbance integrates faster than $\alpha_B$ dissipates).

**Regime III (Ambient noise / slow erosion)** when (I-a) and (I-b) hold but (I-c) fails:

$$\text{(III)} \quad \lVert e_\tau^A\rVert_B \leq R_B, \quad \mathcal I(e_\tau^A) \leq \mathcal F(\mathcal M_B) \cdot \mathcal I_{\max}(\mathcal M_B), \quad \mathcal I(e_\tau^A) \cdot \nu^{(k)} < U_{o,B}^{(k)} \cdot c_\text{floor}$$

The signal is representable and within capacity, but its information content is below the channel's noise floor. It contributes to $\delta_B$'s variance (enters Model S as part of $\sigma_{w,B}^2$) without triggering a usable update.

### 3.2 Interpretation of the three boundaries

- **(I-a) vs (II-a)** is the emitter-side boundary: magnitude exceeds $B$'s sector-condition capacity. This is the destabilization regime of #adversarial-destabilization applied to a single event rather than a tempo-integrated stream. The condition is *magnitude-based*.
- **(I-b) vs (II-b)** is the *structural* boundary: the event's information content requires a model the class cannot express. This is #structural-adaptation-necessity applied to a single event. The condition is *class-based*.
- **(I-c) vs (III)** is the observability boundary: the event's information content is below the channel's noise floor. This is #observation-gates-advantage applied at the single-event level. The condition is *rate-based*.

Three boundaries — magnitude-based, class-based, rate-based — give three ways a recipient can exit Regime I, corresponding to Regimes II-magnitude-shock, II-structural-shock, and III. Regime II splits into two sub-regimes because magnitude failure and class failure are structurally different dynamics, even though both are "the signal is too much for $B$."

### 3.3 The four-regime refinement (§3.5 below expands)

Once we split Regime II into magnitude-shock (II-a) and structural-shock (II-b), the effective classification has four regimes. I label them:

- **I**: Informative update. $M_B$ refines; $\Sigma_B$ edges update by the default signal function (log-odds gradient, #credit-assignment-boundary).
- **II-a (magnitude-shock)**: $\lVert e\rVert_B$ exceeds $R_B$ transiently; the sector condition fails. Response: within model class but above the correction machinery's capacity. $B$ exits its invariant region, begins Lyapunov divergence. Recovery requires the event stream to slow enough for $B$'s machinery to reassert; otherwise, destabilization proceeds as in #adversarial-destabilization.
- **II-b (structural-shock)**: $\mathcal I(e)$ exceeds class capacity. Response: $B$ cannot represent the event regardless of magnitude. The floor in #structural-adaptation-necessity kicks in: parametric adaptation cannot close the mismatch; structural adaptation is required. This is the "the signal is trying to teach you something your model class cannot hear."
- **III**: Ambient noise. Event adds to $\sigma_{w,B}^2$; does not update $M_B$. Effect is drain on $\Delta\rho_B^\ast$ over time.

The magnitude/structural split is substantive: the two sub-regimes have different repair paths. II-a is cured by more capacity (larger $R_B$, higher $\alpha_B$); II-b is cured by a different model class. An organization in II-a needs more correction bandwidth; an organization in II-b needs a different framework. The emitter-side treatment confounds them because both appear as "adaptive reserve exceeded"; the recipient-side treatment distinguishes them because the conditions that produce them differ in which of $B$'s structural quantities gates.

This four-regime version is what §4–§6 derive against.

### 3.4 Boundaries stated in AAD-native quantities (claim)

All four boundaries — (I-a), (I-b), (I-c), and the Regime II/III taxonomy — are stated in quantities already in NOTATION.md or in named segments:

| Boundary | AAD quantities used |
|---|---|
| (I-a)/(II-a): sector-region | $\lVert e\rVert_B$, $R_B$ (#model-class-fitness, #sector-persistence-template's $R$) |
| (I-b)/(II-b): model-class | $\mathcal I(e)$, $\mathcal F(\mathcal M_B)$, $\mathcal I_{\max}(\mathcal M_B)$ |
| (I-c)/(III): observability | $\mathcal I(e)$, $\nu^{(k)}_B$, $U_{o,B}^{(k)}$ |

No new ad-hoc thresholds. This is the first thing to check and it checks out. The only introduction is $\mathcal I_{\max}(\mathcal M_B)$ — a normalizer capturing the class's maximum representable information per observation. §4.2 argues this is a well-defined quantity; see also Working Notes.

### 3.5 What changes vs the emitter-side collapse

The emitter-side story treats the incoming stream as $\gamma_A \mathcal T_A$ into $\rho_B$. The four-regime recipient story decomposes this into per-event classification and reaggregates:

$$\rho_B^{\text{eff}} = \underbrace{\sum_{e \in \text{II-a}} \lVert e\rVert_B \cdot \nu_e}_{\text{magnitude disturbance}} + \underbrace{\text{floor}(\mathcal M_B) \cdot \sum_{e \in \text{II-b}} \nu_e}_{\text{structural mismatch floor}} + \underbrace{\sum_{e \in \text{III}} \sigma_e^2 \cdot \nu_e}_{\text{ambient variance}} - \underbrace{\sum_{e \in \text{I}} \iota_B(e) \mathcal I(e) \cdot \nu_e}_{\text{informative correction}}$$

This is structurally new. The negative term — Regime I events reduce $B$'s effective disturbance rate — does not appear in the emitter-side formulation. It generalizes the cooperative-action term in #team-persistence: a cooperative event is precisely a Regime I event (informative, within class, above observability floor) from an aligned $A$. Adversarial events are Regime II events (shocks). Ambient-noise events are Regime III (drain).

The decomposition composes with #team-persistence: the cooperative $\gamma^{\text{coop}}$ and adversarial $\gamma^{\text{adv}}$ coupling coefficients get regime-typed. What was a sign flip in the emitter-side decomposition is now a regime assignment on the recipient side. The sign flip falls out of the classification.

---

## 4. Structured Derivation — A Specific Kalman-Over-Kalman Case

To check that the four-regime classification has force, I derive it for a specific observation-function / model-class pair. The case is chosen for tractability, not coverage. The broader claim is that the boundary conditions transfer to any recipient architecture in which the underlying AAD quantities ($U_M$, $U_o$, $\mathcal F(\mathcal M)$, $R$, $\eta^\ast$, $\mathcal T$) are well-defined.

### 4.1 Setup

$B$ is a recipient running a Kalman filter on a one-dimensional state:

- **Model class** $\mathcal M_B$: the family of Gaussian state-space models with fixed process noise $q$, observation noise $r$, but *parametric* dynamics $x_{t+1} = \theta x_t + w_t$ with $\theta \in [\theta_{\min}, \theta_{\max}]$. Model class capacity $R_B$: the maximum representable dynamics-magnitude is $\theta_{\max}$, so in state-space, $R_B = \sqrt{q/(1-\theta_{\max}^2)}$ (the stationary standard deviation at the edge of the class).
- **Observation function** $h_B(\Omega_t, \varepsilon_t) = \Omega_t + \varepsilon_t$ with $\varepsilon_t \sim \mathcal N(0, r)$.
- **Prior**: $M_{B,0} = (\hat x_0, P_0)$ with prior variance $P_0$.
- **Update**: standard Kalman — $\eta_B^\ast = P_{t\vert t-1}/(P_{t\vert t-1} + r)$, sector parameter $\alpha_B = \eta_B^\ast$ (the linear Kalman case is exactly on the gain-sector bridge).

$A$ is an emitter producing, once per event, a perturbation of the form $\Omega_t \leftarrow \Omega_t + \xi_A$, where $\xi_A$ is drawn from a distribution parametrized by what kind of signal $A$ is sending. $B$ receives $o_t = \Omega_t + \xi_A + \varepsilon_t$; its mismatch is $\delta_t = o_t - \hat o_t = \xi_A + (\Omega_t - \hat\Omega_t) + \varepsilon_t$.

For classification purposes the relevant content of $\xi_A$ is its magnitude and distribution. Three canonical cases:

- $\xi_A \sim \mathcal N(0, s^2)$ with $s^2 \ll r$ — small-variance Gaussian perturbation. Regime III expected.
- $\xi_A \sim \mathcal N(\mu, s^2)$ with $\mu \ll R_B$, $s^2 \sim r$ — moderate Gaussian perturbation. Regime I expected.
- $\xi_A \in \{-\Delta, +\Delta\}$ with $\Delta > R_B$ — binary kick exceeding sector region. Regime II-a expected.
- $\xi_A$ follows a non-Gaussian heavy-tailed distribution with variance $\sim r$ but kurtosis $K \to \infty$ — heavy-tailed perturbation. Regime II-b expected (Gaussian model class cannot represent the heavy tail, so per-event likelihood is systematically wrong regardless of Kalman tuning).

### 4.2 Derivation: each case lands where the classification predicts

**Case 1: $\xi_A \sim \mathcal N(0, s^2)$, $s^2 \ll r$ (expected Regime III).**

*[Derived]* The Kalman filter's update is $\hat x_t^+ = \hat x_t^- + \eta^\ast \delta_t$. With $\delta_t = \xi_A + \varepsilon_t + (\Omega - \hat\Omega)$, the contribution of $\xi_A$ to the update is $\eta^\ast \xi_A$, distributed as $\mathcal N(0, \eta^{\ast 2} s^2)$. The informativeness of $\xi_A$ for updating $\hat x$ is $\mathcal I(\xi_A) = \tfrac{1}{2}\log(1 + s^2/r)$ bits. For $s^2 \ll r$, $\mathcal I(\xi_A) \approx s^2/(2r \ln 2)$ — small.

Check the three conditions:
- (I-a): $\lVert\xi_A\rVert \sim s$, which is small; $s \ll r \ll R_B$ (since $R_B$ is the model-class stationary std). So (I-a) holds.
- (I-b): Gaussian-within-Gaussian; representable. So (I-b) holds.
- (I-c): $\mathcal I(\xi_A) \cdot \nu < U_{o,B} \cdot c_\text{floor}$ when $s^2/r$ is small enough. By hypothesis, $s^2 \ll r$, so (I-c) fails.

Result: Regime III. Derived consequence: the contribution to $\rho_B^{\text{eff}}$ is through $\sigma_{w,B}^2$ not through useful correction. Over time $B$'s adaptive reserve $\Delta\rho_B^\ast$ drains by $\sum_e \eta^{\ast 2} s_e^2 \cdot \nu_e$ — small but nonzero; the filter does not extract structural signal but does consume tempo. This is the formal version of "organization slowly absorbs signal as fatigue."

**Case 2: $\xi_A \sim \mathcal N(\mu, s^2)$, $\mu$ moderate (expected Regime I).**

*[Derived]* Now the perturbation has substantial informativeness: $\mathcal I(\xi_A) = \tfrac{1}{2}\log(1 + (s^2 + \mu^2)/r)$ bits. If $\mu \ll R_B$ and $s^2 \sim r$, all three conditions for Regime I hold. The Kalman update responds correctly: the mean shifts by $\eta^\ast \mu$ in one step, and the posterior uncertainty shrinks toward its stationary value. The update is informative; $M_B$ improves; the contribution to $\rho_B^{\text{eff}}$ is *negative* in the decomposition — the event carries information that tightens the model.

Result: Regime I. This is the classical Bayesian update; nothing special. The point of deriving it is to confirm the classification picks it out.

**Case 3: $\xi_A \in \{-\Delta, +\Delta\}$ with $\Delta > R_B$ (expected Regime II-a).**

*[Derived]* The event $\delta_t = \pm\Delta + \text{noise}$. Since $\Delta > R_B$, this pushes $B$ outside its sector-condition region after a single event. The Kalman filter updates: $\hat x_t^+ \leftarrow \hat x_t^- + \eta^\ast \Delta$. For $\eta^\ast < 1$ (steady state), the update undershoots: the filter's belief lags the true state by $(1-\eta^\ast)\Delta$ per event. If events arrive at rate $\nu$ such that $\nu > \alpha_B = \eta^\ast$, the lag accumulates: $B$'s mismatch grows without bound.

The structural-persistence condition $\alpha_B R_B > \rho_B^{\text{eff}}$ is violated: with $\rho_B^{\text{eff}} \approx \nu \Delta$, we need $\eta^\ast R_B > \nu \Delta$, which fails when $\Delta > R_B$ and $\nu \gtrsim \eta^\ast$. $B$ exits its invariant region; by #sector-condition-stability the Lyapunov $V(\delta)$ is no longer monotonically decreasing; destabilization per #adversarial-destabilization proceeds.

Result: Regime II-a. Derived consequence: the magnitude-shock triggers the emitter-side destabilization dynamics. The signal is within the model class — Gaussian handles $\pm\Delta$ just fine mathematically — but the correction machinery cannot discharge it fast enough.

**Case 4: $\xi_A$ heavy-tailed with $E[\xi_A^2] \sim r$ and kurtosis $K \to \infty$ (expected Regime II-b).**

*[Derived]* This is the most interesting case. The mean contribution of $\xi_A$ to the update is fine (it's zero-mean, moderate variance). The Kalman filter, treating $\xi_A$ as part of Gaussian observation noise, updates $\hat x_t^+ = \hat x_t^- + \eta^\ast \delta_t$ with the Gaussian-optimal gain. But $\xi_A$'s distribution is not Gaussian: most events are small; a small fraction are enormous. The Kalman filter's gain — calibrated to Gaussian — is too aggressive for small events (it treats them as signal when they are outliers) and too small for large events (it discounts them when they are genuine big signals).

The per-event expected log-likelihood under the true distribution $P_\text{true}(\xi_A)$ vs the Gaussian model $P_{\mathcal M_B}(\xi_A)$ has a KL gap:

$$D_{KL}(P_\text{true} \Vert P_{\mathcal M_B}) > 0$$

This is nonzero for any heavy-tailed $P_\text{true}$ against any Gaussian. By #model-class-fitness's structural-inadequacy condition, $\mathcal F(\mathcal M_B) < 1 - \varepsilon$ with $\varepsilon$ lower-bounded by the KL gap. By #structural-adaptation-necessity, no parametric update within $\mathcal M_B$ can close the mismatch; $B$'s residuals will retain systematic structure (a non-Gaussian residual distribution). The sector condition's $\alpha_B$ effectively shrinks because correction cannot discharge the structural component of the mismatch.

Result: Regime II-b. Derived consequence: the failure is diagnostic — $B$'s residuals retain non-Gaussian structure visible in kurtosis tests — and the repair path is structural (expand the model class to include heavy-tailed observation distributions, e.g., Student-$t$), not parametric.

### 4.3 Generalization beyond Kalman-over-Kalman

The four derivations above depend on:

- The sector-condition region $R_B$ being bounded by model-class capacity (Case 3).
- The model-class fitness bounding a KL gap against structurally distinct distributions (Case 4).
- The observability floor being characterizable by an SNR ratio (Case 1).
- The informativeness $\mathcal I(e)$ being upper-bounded by the class's representational capacity (implicit in Case 2's "moderate").

These are the four AAD-native quantities that carry the classification. For any recipient where they are well-defined — which, by #sector-persistence-template + #model-class-fitness + #adaptive-tempo, is any AAD agent within Section I's scope — the classification transfers. The Kalman case verifies the *form* of the argument; the conceptual content is carried by the general AAD quantities.

For non-Gaussian recipient architectures (conjugate Bayesian, exponential-family variational, RL Q-learning with function approximation), the same four conditions can be stated in the native quantities. Kalman is a sub-scope $\alpha$ instantiation per #sector-condition-derivation; for sub-scope $\beta$ agents (PID, rule-based, human judgment) the classification conditions still hold, but the individual derivations require per-case verification of the A2' sector bound. The classification is robust to sub-scope; the per-case bounds may or may not be tight.

---

## 5. Agent-Opacity $H_b$ — Where It Enters

Joseph's question (3): does $H_b$ (Hafez's backward predictive uncertainty $H(S,A \mid S')$, adopted into AAD via `msc/spike-hafez-integration-audit.md` as agent opacity) primarily concern the emitter's uncertainty over $B$'s state, or does it reshape the recipient's classification?

### 5.1 Direct answer

$H_b^B$ is primarily an *emitter-side* quantity: it captures $A$'s uncertainty about what $(S,A)$-pair at $B$ produced an observed transition. In emitter-side reasoning, $H_b^B$ gates $A$'s ability to target $B$'s adaptive machinery — high $H_b^B$ (opaque recipient) reduces $A$'s effective $\gamma_A$ because $A$ cannot model $B$ well enough to choose signals that maximize destabilization. This is the role `#adversarial-destabilization` Working Notes currently carry.

$H_b^B$ does *not* directly reshape the recipient's classification because $B$'s classification depends on $B$'s own state variables — its $U_M$, $U_o$, $\mathcal F(\mathcal M)$, $R$, $\mathcal T$ — not on what $A$ knows about $B$.

However, $H_b^B$ enters the *effective emitter-side couplings* (the $\gamma_A$ coefficients) that set the *rate* at which events of each regime arrive. If $A$ cannot model $B$, $A$'s signals are essentially random from $B$'s perspective: their distribution over regime-classes is uniform-ish (large fractions in Regime III and Regime II-a, small fraction in Regime II-b). If $A$ can model $B$ perfectly ($H_b^B \to 0$), $A$ can target: choose signals that maximize the fraction in $B$'s failure mode of interest.

### 5.2 A refined read: opacity conditions the emitter's regime-targeting

Let $A$ have a model $\tilde M_A(B)$ of $B$'s state with uncertainty measured by $H_b^B$. For each event $e$ $A$ sends, $A$'s predicted regime for $B$ is a probability distribution $P_A(\text{regime}(e) \mid \tilde M_A(B))$. The emitter's expected effect on $B$ decomposes as:

$$\mathbb E_A[\text{effect}] = \sum_{\text{regime}} P_A(\text{regime}) \cdot \text{expected effect} \mid \text{regime}$$

As $H_b^B \to 0$: $P_A$ concentrates on the intended regime; emitter can choose adversarially. As $H_b^B \to \infty$: $P_A$ approaches a uniform-over-feasible-regimes; emitter cannot target.

The formal structure:

$$\gamma_A^{\text{effective}} = \gamma_A^{\text{max}} \cdot f(H_b^B)$$

with $f$ a monotonically decreasing function of opacity. In the high-opacity limit, the emitter-side advantage $(\mathcal T_A/\mathcal T_B)^b$ of #adversarial-tempo-advantage degrades because the fraction of $A$'s events landing in $B$'s destabilizing regimes (II-a, II-b) drops.

This is structurally the same as the `#observation-gates-advantage` result, but applied at the emitter rather than the recipient: where observation-gates-advantage says $A$'s tempo advantage degrades when $A$'s observations of the *environment* are noisy, the opacity result says $A$'s tempo advantage degrades when $A$'s observations of *$B$* are noisy. Both are "tempo without calibration is overrated." The opacity-as-inverse-$U_o$ dual that the current `#adversarial-destabilization` Working Notes gesture at is now formal.

### 5.3 Symmetric read — legibility is cooperative

Dually, low $H_b^B$ (legible recipient) enables cooperative signaling: an emitter that shares $B$'s $O_t$ and can model $B$'s state can choose signals that maximize $B$'s Regime I probability. This is the recipient-side translation of `#auftragstaktik-principle`'s "share purpose before plans": shared purpose gives $A$ a better model of $B$'s prior and model class, which means $A$ can target signals that fall within $B$'s $\mathcal F(\mathcal M_B)$ and above its observability floor.

So: $H_b^B$ is not a reshape of the recipient's classification. It is a modulator of which regime-distribution the incoming event stream has, which then is classified by $B$'s own machinery.

### 5.4 An adjacent question: the dual $H_b^A$ — the recipient's uncertainty over the emitter

A less-discussed quantity is $B$'s uncertainty about *the emitter* — the dual of Hafez's $H_b$ with $B$ as observer. This enters the communication-gain term $U_{\text{src},j}$ in `#communication-gain`: $B$'s estimate of $A$'s calibration. For recipient-side classification, this modulates $B$'s posterior on $\mathcal I(e_\tau^A)$: a well-known-calibrated $A$ gives $B$ high confidence in the signal's informativeness, pushing borderline-(I-c) events into Regime I; a poorly-calibrated $A$ pushes them into Regime III.

This is the trust-calibration lever in recipient-side reception. It is already in the communication-gain formula; the classification just surfaces it. No new quantity needed.

---

## 6. Connections

### 6.1 Recovery of emitter-side results as limits

The classification recovers the existing emitter-side results as restrictions to specific regimes:

- **`#adversarial-destabilization`** — Regime II-a with coupled event streams from $A$. The emitter-side derivation is about integrating Regime II-a contributions over time; the structural-shock in II-b was implicit, being collapsed into "adaptive reserve exceeded."
- **`#adversarial-tempo-advantage`** — Regime II (aggregate) applied with tempo-proportional event rates. The superlinear scaling follows from the sector-persistence template's $1/\alpha$ (Model D) vs $1/\sqrt\alpha$ (Model S) applied to Regime II events. The classification does not change the scaling; it just sharpens the story: tempo advantage is only effective insofar as $A$'s tempo produces Regime II events, not Regime III.
- **`#observation-gates-advantage`** — this is the recipient-side expression of the rate boundary (I-c). When $U_{o,B}$ is high, more of $A$'s events slip into Regime III (lost to noise floor), and $A$'s tempo advantage collapses. The classification makes this a structural prediction rather than an empirical finding: the $b$-exponent should drop toward zero in the high-$U_{o,B}$ limit because the fraction of $A$'s events landing in Regime II drops to zero.
- **`#symbiogenic-composition`** — the integrated transition (S-1, S-2, S-3) corresponds to $A$'s events being classified as Regime I for $B$: they refine $B$'s $M_B$ with content that becomes part of $B$'s structure. The host-endosymbiont asymmetry is precisely "most of endosymbiont's signals to host are Regime I; host's signals to endosymbiont are a mix including high-$\mathcal I$ signals that rewrite $\mathcal M_\text{endo}$ toward $\mathcal M_\text{host}$." The Regime I sub-classification recovers catalysis/update dynamics.
- **Cooperative signaling (implicit in `#team-persistence`)** — Regime I events from $A$ contribute negatively to $\rho_B^{\text{eff}}$ via the `#team-persistence` cooperative-disturbance term. This is the shared-intent channel: the emitter is deliberately producing Regime I events for the recipient. The communication tempo $\nu_{ji}^\text{comm} \cdot \eta_{ji}^\ast$ is the Regime I event rate times the recipient's informative-gain.

All five emitter-side results appear as special cases; none of them require changes.

### 6.2 The GAP: `#adversarial-edge-targeting`

Section III has an open GAP "which strategy edges are most valuable to attack." The emitter-side formulation would ask: given $A$ can produce signals, which edge $(i,j)$ of $B$'s $\Sigma_B$ maximizes the destabilization per unit of $A$'s tempo?

The recipient-side classification *directly pairs* with this question. The most-valuable edges for $A$ to attack are exactly the edges on which Regime II targeting is possible for $A$:

- Edges where $B$'s observability $\sigma_v^B$ is high (so Regime III is small — $A$'s signals don't fall below the floor).
- Edges where $\iota_B$ (regime-A identifiability) is high (so $B$ is actually going to update).
- Edges where $\Sigma_B$'s plan-confidence Jacobian $J_k$ is large (so the update contaminates $\hat P_\Sigma$ strongly).
- Edges where the nominal credence $p_k$ is far from $\{0,1\}$ (so the update moves the credence, not just reinforces extremes).

The adversary's optimization is: given $B$'s state, find edges $(i,j)$ where signals land in Regime I for $B$ (so $B$ updates) but the update content is *wrong* (so $B$'s $\Sigma_B$ degrades). This is a Regime-I-with-adversarial-content attack: not pushing $B$ into Regime II, but exploiting $B$'s openness to Regime I to inject misinformation.

The recipient-side classification makes this possibility visible. The emitter-side formulation (a single $\gamma_A \mathcal T_A$ disturbance rate) cannot express "Regime I event with adversarial content" — it can only express "more $\gamma_A$." The recipient-side version exposes the lever the adversary has that the emitter-side formulation hides.

Concretely: the `#credit-assignment-boundary` log-odds update is

$$\lambda_k^\text{new} = \lambda_k + \eta_\text{edge} \cdot \iota_k \cdot J_k \cdot (y_G - \hat P_\Sigma)/\lVert\mathbf J\rVert^2$$

An adversary who can control $y_G$ can choose the sign of $(y_G - \hat P_\Sigma)$ to push $\lambda_k$ in whichever direction degrades $\Sigma_B$ most. The attack is strongest at edges with large $J_k$ and moderate $p_k$ — exactly the edges AAD's machinery already identifies as "load-bearing" for the strategy.

This suggests `#adversarial-edge-targeting` has the form:

*Proposition (sketch).* Given $B$'s $\Sigma_B$ and an adversary capable of producing Regime I events on arbitrary edges, the value per unit adversary tempo is maximized at edges $k$ satisfying:

$$\arg\max_k \iota_k \cdot J_k \cdot p_k(1 - p_k) \cdot \sigma_k^B$$

where $\sigma_k^B$ is $B$'s observability of edge $k$. The first three factors are $B$'s own plan-sensitivity; the last is the gate for signal arrival.

This pairs cleanly with the classification. The emitter is choosing the target edge; the classification determines what happens there. Together they answer "which edges, hit by what signals, produce what effect." The recipient-side classification is the *pattern-recognizer* for what happened; the emitter-side edge-targeting is the *optimizer* for the adversary. The two fit in the same framework because they run against the same underlying quantities.

### 6.3 Identifiability-floor connection

Regime II-b — the structural-shock — is the per-event shadow of the identifiability-floor pattern ( #discussion-identifiability-floor). When the signal's information content requires a model class that $B$ does not have, $B$ cannot identify the structure of the incoming signal regardless of how many samples it sees. This is formally the Cramér-Rao-floor / misspecification-cost structural limit applied at the signal level rather than the estimator level.

The adjacent-floor "Misspecification-cost quantification" open problem in #discussion-identifiability-floor — "under fixed information budget, the degradation rate from misspecification is bounded below by an information-theoretic quantity" — is precisely what Regime II-b's dynamics should give once formalized: the rate at which $B$'s $\rho_B^{\text{eff}}$ degrades under a sustained Regime II-b stream is lower-bounded by the KL gap between $B$'s model class and the truth. This would make the misspecification-cost floor concrete: the emitter-side term is $\text{floor}(\mathcal M_B) \cdot \sum_{e \in \text{II-b}} \nu_e$ in the decomposition of §3.5.

### 6.4 Pairing with `#symbiogenic-composition`

§6.1 flagged that symbiogenic absorption lives in Regime I from the host's perspective. The converse — the endosymbiont's perspective — is richer. During symbiogenesis:

- The host's signals to the endosymbiont include high-$\mathcal I$ structure that the endosymbiont's model class can barely represent (Regime II-b from the endosymbiont's side). Over the consolidation time, the endosymbiont's $\mathcal M$ adapts structurally — gene transfer, specialization — which *grows* its model class to accommodate the host's signals. This is #structural-adaptation-necessity running continuously.
- Simultaneously, the host's $\mathcal M_h$ absorbs endosymbiont functional content (Regime I for the host): the endosymbiont's accumulated structure $(M_e, \Sigma_e)$ is transferred, which refines the host's model at no structural cost to the host.

The asymmetry of symbiogenesis — host absorbs structure; endosymbiont restructures — has a clean classification-level characterization: *symbiogenesis is a process in which the stream in one direction is Regime I and the stream in the other direction is Regime II-b driving structural adaptation.* The autonomy reduction (S-3 in `#symbiogenic-composition`) corresponds to the endosymbiont's $\mathcal M_e$ progressively coinciding with a sub-manifold of $\mathcal M_h$; once the coincidence is tight, the endosymbiont's Regime II-b stream collapses to Regime I because the structural mismatch has been closed.

This is speculative but concrete. It suggests that symbiogenic composition is the fixed-point of a classification-asymmetric signaling process. The fixed-point condition — the consolidation condition — is that both streams are Regime I. Pre-fixed-point, the asymmetric II-b / I split forces structural adaptation on one side.

---

## 7. Scope Honesty and Limits

Following the posture of #discussion-identifiability-floor and #discussion-separability-pattern, this section states precisely what the classification does and does not cover.

### 7.1 What the classification admits

- Class 1 (modular) recipients: full classification applies per §4 derivation.
- Class 3 (partially modular) recipients: classification applies with degradation proportional to $\kappa_{\text{processing}}$ (see `msc/spike-kappa-hb-operationalization.md`). The Regime I update may be goal-contaminated; the Regime II-b structural-shock may be mis-identified as II-a or III due to goal-blind-update failure. The classification's *form* transfers; the boundaries become approximate.
- Sub-scope $\alpha$ recipients: the Kalman-over-Kalman derivation transfers exactly; the boundary conditions carry the sector-parameter derivation from #gain-sector-bridge.
- Sub-scope $\beta$ recipients: the classification's form transfers; the boundary condition (I-a) requires a per-instantiation verification of the sector bound, inheriting from #sector-persistence-template's sub-scope $\beta$ caveat.

### 7.2 What the classification does not admit

- **Class 2 (fully merged) recipients**: the classification presupposes goal-blind epistemic update ( #directed-separation). When the recipient's update is entangled with its objective, the "what happens to $M_B$" question depends on "what happens to $G_B$" simultaneously; the four-regime partition would need a coupled formulation. This is `03-logogenic-agents/` territory.
- **Non-singular trajectories**: by #agent-identity, the classification is trajectory-indexed. Type-level claims (how does an equivalence-class-agent receive a signal?) require additional machinery.
- **Sustained multi-event dynamics**: each boundary is stated per-event. Regime II-a in particular requires event-rate information to determine whether the mismatch integrates faster than correction dissipates. The per-event classification is the building block; aggregation over event streams is the sector-persistence template's job. The classification does not replace the template; it types the events that feed it.
- **Cascading regime transitions**: a Regime III stream might, over time, drain $\Delta\rho^\ast$ enough that subsequent events — nominally Regime I — enter Regime II-a because the recipient's correction capacity has degraded. This meta-dynamic is not captured in the static classification.

### 7.3 What the classification does not claim

- It does not claim the four regimes are exhaustive. There may be finer distinctions within each (Regime II-a with and without structural-shock overlap; Regime I with and without causal-identification, etc.). The four-regime partition is the coarsest useful split given the three AAD-native boundaries.
- It does not claim the boundaries are sharp in practice. Real recipients' sector regions and model classes have uncertain parameters; the boundaries are sharp in the formalism but fuzzy under estimation error. A Regime I event with $\lVert e\rVert \approx R_B$ may oscillate into Regime II-a under parameter-uncertainty.
- It does not claim the classification determines the event's *semantic content*. Knowing an event is Regime I tells you $B$ will update; it does not tell you *what* $B$ will believe afterward. The update's content is in the default signal function ( #credit-assignment-boundary) and the recipient's specific priors.

### 7.4 Epistemic status

- **Boundary form**: *robust qualitative*. The three-boundary partition uses existing AAD quantities; the split (magnitude, class, rate) matches the three distinct failure modes that AAD machinery already recognizes.
- **Boundary conditions (I-a), (II-a)**: *exact* under the sector-condition machinery inherited from #sector-persistence-template.
- **Boundary conditions (I-b), (II-b)**: *conditional*. The normalization by $\mathcal I_\max(\mathcal M_B)$ is heuristic; a cleaner form would state (I-b) as "the event's sufficient statistics for prediction are in the span of $\mathcal M_B$'s sufficient statistics," which is exact but abstract. See Working Notes.
- **Boundary condition (I-c)**: *robust qualitative*. The specific coefficient $c_\text{floor}$ is a detection-theory parameter; the form (SNR threshold) is standard.
- **The Kalman-over-Kalman derivation (§4)**: *exact* for the stated case.
- **Emitter-side recovery (§6.1)**: *derived* — each emitter-side result is exhibited as a restriction of the four-regime decomposition.
- **`#adversarial-edge-targeting` pairing (§6.2)**: *sketch*. Direction is clear; the formal optimization problem is proposed, not solved.
- **Symbiogenic-composition asymmetric-classification read (§6.4)**: *hypothesis / discussion-grade*.

Max attainable: *derived* for the classification structure; the per-case bounds retain their individual statuses.

---

## 8. Recommendations for Promotion

### 8.1 Landing segment

Recommend a new appendix-or-Section-III segment `#interaction-channel-classification`:

- **Type**: *derived* — the classification is derivable from existing AAD quantities.
- **Status**: *conditional* — conditional on the per-case boundary derivations (§4).
- **Location**: Section III appendix or late-Section III segment, positioned between `#adversarial-destabilization` and the `#adversarial-edge-targeting` GAP. It is a companion to the emitter-side segments, not a replacement.
- **Depends on**: #observation-function, #mismatch-signal, #update-gain, #adaptive-tempo, #model-class-fitness, #structural-adaptation-necessity, #persistence-condition, #sector-persistence-template, #adversarial-destabilization, #adversarial-tempo-advantage, #observation-gates-advantage, #symbiogenic-composition, #communication-gain, #team-persistence, #credit-assignment-boundary.
- **Cross-referenced by**: #adversarial-destabilization (recipient-side perspective of $\gamma_A \mathcal T_A$), #symbiogenic-composition (asymmetric classification read), #team-persistence (Regime I as the cooperative-action term), #observation-gates-advantage (rate-boundary is the recipient-side expression).

### 8.2 Satellite moves

- **`#adversarial-edge-targeting`**: promote from GAP to draft segment with the §6.2 optimization statement. Type: *derived*, status: *sketch*. The sketch becomes derived once the optimization problem is formally solved.
- **`#adversarial-destabilization` Working Notes**: replace the "decoupled analysis is conservative" Working Note with a reference to `#interaction-channel-classification`'s rigorous recipient-side decomposition.
- **`#discussion-identifiability-floor`**: add Regime II-b / misspecification-cost as a third concrete instance of the pattern (currently "open extension").
- **`#symbiogenic-composition`**: §6.4's asymmetric-classification read is a candidate Working Note; would land as "discussion connection to recipient-side classification."
- **`#team-persistence`**: tighten the cooperative-disturbance decomposition by referencing Regime I events. The sign-flip in $\rho_i^{\text{eff}}$'s decomposition is precisely the Regime I sub-sum.

### 8.3 Candidate meta-segment — `#signal-reception-pattern`

A longer-term candidate, analogous to `#discussion-separability-pattern` and `#discussion-identifiability-floor`. The structural pattern: recipient-side classification is a three-boundary (magnitude / class / rate) decomposition of inter-agent coupling, composing with the existing meta-segments:

- Separability: the classification partitions signals into separable-core (Regime I, within scope), structured-repair (Regime II-a, magnitude-structured, bounded by sector region), and general-open (Regime II-b, structural adaptation).
- Identifiability floor: Regime II-b instantiates the floor per-event; Regime III instantiates it for the observability dimension.
- Additive-coordinate-forcing: the log-odds coordinate of `#credit-assignment-boundary` is what makes Regime I updates safe — no mechanical break under large $\mathcal I(e)$, which would force a premature regime reclassification.

This meta-positioning is speculative at present but worth flagging. The classification currently composes with all three meta-segments; whether it rises to its own meta-segment depends on whether the pattern recurs elsewhere in AAD beyond the single composition story.

### 8.4 What should NOT be promoted yet

- The symbiogenic-composition asymmetric read (§6.4). Too speculative for segment-level; retain as spike content.
- The agent-opacity regime-distribution story (§5.2). The form $f(H_b^B)$ is sketched, not derived. A cleaner derivation would relate $H_b^B$ to the variance of $A$'s predictive distribution over $B$'s regime classification, then to the emitter's expected effect. Worth a follow-up spike.
- The Regime II-b / identifiability-floor misspecification-cost formalization. Needs its own derivation — the KL-gap bound has to be made concrete.

---

## 9. Summary

The recipient-side theory is formalizable within existing AAD machinery. The four regimes — Informative update (I), Magnitude-shock destabilization (II-a), Structural-shock destabilization (II-b), Ambient noise (III) — are forced by three boundary conditions stated in AAD-native quantities:

- sector-region (magnitude) via $R_B$ (from #model-class-fitness / #sector-persistence-template)
- model-class (structural) via $\mathcal F(\mathcal M_B)$
- observability (rate) via $U_{o,B}$ and $\nu^{(k)}_B$

The classification recovers `#adversarial-destabilization` (Regime II-a), `#symbiogenic-composition` (Regime I with structural asymmetry), `#observation-gates-advantage` (rate-boundary), and cooperative signaling (`#team-persistence`'s action-based cooperative coupling as Regime I) as special cases. It pairs with the `#adversarial-edge-targeting` GAP as the recipient-side pattern-recognizer to the emitter-side optimizer.

Agent opacity $H_b^B$ enters as an *emitter-side* modulator of the regime distribution $A$ can target, not as a recipient-side reshape. The recipient's classification depends on the recipient's own state; opacity controls what arrives.

The classification is honest about its scope: Class 1 fully, Class 3 approximately, Class 2 not without coupled formulation; singular trajectories only; per-event with aggregation deferred to #sector-persistence-template.

Recommendation: promote to a new segment `#interaction-channel-classification` as a derived-conditional result positioned between `#adversarial-destabilization` and the `#adversarial-edge-targeting` GAP, with the seven cross-references above tightened to reflect the recipient-side decomposition.

---

## Working Notes

- **$\mathcal I_\max(\mathcal M_B)$ normalization.** The boundary (I-b) uses $\mathcal F(\mathcal M_B) \cdot \mathcal I_\max(\mathcal M_B)$ as the class's representational ceiling on per-event information. The cleaner form is: (I-b) holds iff the event's sufficient statistics for prediction lie in the span of $\mathcal M_B$'s sufficient statistics. This is exact but abstract. For parametric families (exponential families, Gaussian, etc.) the explicit form is routine; for non-parametric classes it requires the projection-to-class formalism of #information-bottleneck. The normalization by $\mathcal I_\max$ is a heuristic for the exact condition; it may be worth replacing with the sufficient-statistics-span form in the segment version.

- **The four vs three regime question.** The partition splits II-a / II-b because they have different repair paths. But one could argue for a coarser three-regime split (I / II / III) where II collapses magnitude and structural shocks; or a finer five-regime split (I-a / I-b / II-a / II-b / III) where Regime I separates into "within observability" and "within calibration" depending on whether the signal produces a point update or a structural refinement. The four-regime version is the coarsest split where each regime has a distinct AAD-machinery response. Going finer than four would duplicate the structural-adaptation hierarchy.

- **Where does $\mathcal I(e)$ come from operationally?** The spike uses $\mathcal I(e)$ somewhat loosely as "the information content conditional on $B$'s prior." Formally this is $I(e; \Omega \mid M_{B,\tau^-})$ — the NOTATION.md $\mathcal I(e_\tau)$ quantity. For Gaussian cases it's the Kalman innovation's log-likelihood; for conjugate-Bayesian cases it's the per-event Bayes factor; for general cases it's the per-event KL divergence between prior and posterior predictive. The classification's reliance on $\mathcal I(e)$ is thus grounded in an existing AAD quantity, not a new one.

- **Checking the non-Gaussian case (Case 4 in §4.2).** The heavy-tailed derivation is informal; a rigorous version would compute the effective Kalman gain under misspecification and show the residuals retain signal. This is standard — robust filtering literature (Huber, Masreliez, etc.) has worked this out. The classification doesn't depend on the specific non-Gaussian family, just on the KL gap being nonzero.

- **Relation to active inference.** Active inference casts reception as surprise minimization; regime II-b in particular corresponds to high-surprise events that exceed the agent's generative model. The classification's Regime II-b is the AAD analog of what AI calls "novel generative context" — the agent's free-energy landscape does not contain the region the event points to. The classification avoids the active-inference commitment to variational free energy as master objective (per `msc/spike-active-inference-vs-aad.md`); it uses only the information-theoretic content, not the variational machinery.

- **Is this one result or many?** The classification is one structural result (three boundaries, four regimes) with consequences across multiple segments. The derivation is routine modulo the per-case sector-bound verification. The *novelty*, such as it is, is noticing the three boundaries are independent and that all three are already named in existing segments. The recipient-side theory does not require new formalism; it requires recombining existing machinery in the recipient-centric view instead of the emitter-centric view.

- **The organizational-reception intuition.** Joseph framed the motivation around "you tried to teach the organization and it heard you / it shattered / it slowly absorbed the signal as fatigue." The classification maps to:
  - Heard: Regime I on the relevant edges of $\Sigma_\text{org}$.
  - Shattered: Regime II — specifically II-b if the signal required reorganization beyond the org's structural capacity (cf. Cohen & Levinthal 1990 absorptive capacity), II-a if the signal was just too large/fast.
  - Slowly absorbed as fatigue: Regime III — drains $\Delta\rho^\ast_\text{org}$ without producing structural change. This is the "death by a thousand memos" pattern.

  The absorptive-capacity literature (Cohen & Levinthal 1990) is the organizational analog of $\mathcal F(\mathcal M_B)$: an organization with low absorptive capacity cannot integrate high-$\mathcal I$ signals regardless of how clearly they are communicated. This is one of the cleanest cross-domain instantiations of AAD's machinery and would strengthen the TST-adjacent domain coverage. Worth mentioning in the segment version under Discussion.

- **Next spike candidates.**
  1. Formal derivation of the $f(H_b^B)$ function in §5.2 — the emitter's expected effect as a function of recipient opacity. Would tighten the `#adversarial-destabilization` Working Notes' qualitative $\gamma_A \propto 1/H_b$ into a derived form.
  2. Formalization of the misspecification-cost floor as a Regime II-b structural result, closing one of `#discussion-identifiability-floor`'s adjacent-floor open questions.
  3. Formal solution of the `#adversarial-edge-targeting` optimization in §6.2 — the arg-max over edges given $B$'s plan Jacobian and edge observabilities. Pairs with this spike as the emitter-side counterpart.
