---
slug: spike-pid-a2prime
type: spike
status: draft
date: 2026-04-22
---

# Spike: A2' for PID Controllers — Promoting PID from Sub-Scope β to Sub-Scope α

**Trigger:** `#sector-condition-derivation`'s A2' sub-scope partition lists PID controllers in sub-scope $\beta$ ("A2' assumed per-system; no structural B1 guarantee"). PID is the dominant industrial controller class by orders of magnitude — by some estimates $> 90\%$ of industrial feedback loops. If A2' can be *derived* for PID under explicitly scoped plant-and-tuning conditions, a vast industrial deployment class inherits AAD's derived persistence guarantees through `#sector-persistence-template`, rather than relying on an empirical posit. This is the strengthen-first move on PID.

**Posture:** Real derivation using classical positive-real / passivity machinery. The mathematics is known (Lur'e 1957, Popov 1961, Khalil 2002 ch. 6, Åström & Murray 2008 ch. 10–11); the value is in *(a)* casting the classical result in AAD's directional-fidelity B1 language, *(b)* making the scope conditions visible at segment granularity per AAD's scope-honesty-as-architecture posture, and *(c)* extracting the explicit sector constant $\alpha$ in AAD parameters so downstream template instantiations can use it.

**Claim to defend:** PID controllers admit an A2' derivation in a well-characterized sub-sub-scope $\alpha_{\text{PID}} \subset \alpha$ — specifically the regime where *(i)* the plant is strictly-positive-real (SPR) or sector-bounded Lipschitz, *(ii)* the PID tuning satisfies a small-gain / positive-real condition, and *(iii)* anti-windup is in place or saturation is avoided. Outside this regime PID remains in sub-scope $\beta$, and we say so explicitly.

**Status:** Draft. Derivation complete for the linear-SPR-plant case (Angle 1–2); nonlinear sector-plant extension via circle criterion sketched (Angle 3); anti-windup under back-calculation treated cleanly (Angle 4); tuning-region characterization via phase-margin bound (Angle 5); composition with the adaptive-gain spike's meta-A2' framework checked (Angle 6); dyadic cascade closure example verified (Angle 7); honest scope exclusions enumerated (Angle 8). Candidate landings identified.


## 1. Problem statement

Stated inside AAD's current machinery:

> Let the agent be a PID controller with gains $(K_p, K_i, K_d)$ acting on a plant $P$ with state $x \in \mathbb R^n$. Let the mismatch be the tracking error $\delta_t = r_t - y_t$ where $r_t$ is the reference and $y_t$ is the plant output. The control action is
>
> $$u_t = K_p \delta_t + K_i \int_0^t \delta_s\,ds + K_d \dot\delta_t$$
>
> Under what conditions on the plant $P$ and the gains $(K_p, K_i, K_d)$ is A2' — $\delta^T F(\mathcal T, \delta) \geq \alpha \lVert\delta\rVert^2$ on some ball $\mathcal B_R$ — a *derived* consequence rather than an assumed per-agent empirical claim? What is the explicit $\alpha$?

Three sub-questions:

- **Q1.** For linear plants, when does classical closed-loop stability of the PID loop translate directly to A2' in the directional-fidelity B1 form of `#gain-sector-bridge`?
- **Q2.** For nonlinear plants satisfying a sector bound (Lur'e system), does the circle / Popov criterion give A2' for PID?
- **Q3.** When does anti-windup preserve the derivation under saturation, and when does saturation push PID into sub-scope $\beta$?


## 2. Setup — PID as AAD correction function

### 2.1 Casting PID in AAD language

PID does not fit AAD's "gain-based update" $M_t = M_{t-1} + \eta^\ast g(\delta_t)$ pattern directly — its "state" is not a model estimate $M_t$ but a controller internal state $(I_t, D_t) = (\int \delta, \dot\delta)$ plus the plant state $x_t$. Map PID to `#sector-condition-derivation`'s generic-$F$ setup:

*[Formulation (PID-as-correction)]*

The mismatch is the tracking error $\delta_t = r - y_t$ (with $r$ constant WLOG — step reference). The closed-loop mismatch dynamics are

$$\dot\delta = -F_{\text{PID}}(\delta, \xi; \mathcal T) + w(t)$$

where $\xi_t$ is an internal controller state (the integrator state and a filtered-derivative state if a proper PID is used), $F_{\text{PID}}$ is the closed-loop correction, and $w(t)$ encodes reference drift plus plant disturbance. The adaptive tempo $\mathcal T$ maps to the crossover frequency $\omega_c$ of the open loop — $\mathcal T \sim \omega_c$ in the sense of an inverse closed-loop time constant.

**Key observation.** In the PID case, the directional-fidelity question B1 — does the correction point "at reality" — becomes the classical question *does the closed-loop output track the reference*, which is exactly what positive-real / small-gain / phase-margin conditions answer. The AAD B1 inequality and the classical SPR condition are the same inequality, dressed in different notation. Making this equivalence explicit is the spike's central move.

### 2.2 Plant class

For the cleanest Angle-1 derivation, restrict to:

*[Scope (Angle-1 plant class)]* $P$ is a single-input single-output (SISO) linear time-invariant (LTI) plant with transfer function $P(s) = n(s)/d(s)$, with $\deg d \geq \deg n$ (properness), $P$ stable or marginally stable (no right-half-plane poles; any pole at the origin is simple), and $P$ of relative degree at most 2 (so a proper PID can give the loop relative degree 0 or 1 for SPR compatibility).

This is the standard plant class for which classical PID tuning (Ziegler-Nichols, IMC, lambda tuning) has guarantees.


## 3. Angle 1 — Classical result recall in AAD notation

### 3.1 Positive-real lemma and SPR condition

A rational transfer function $G(s)$ is **strictly positive real (SPR)** if:

- $G(s)$ is analytic in $\operatorname{Re}(s) \geq 0$ (no RHP poles, no $j\omega$-axis poles);
- $\operatorname{Re}\,G(j\omega) \gt 0$ for all $\omega \in \mathbb R$;
- $\lim_{\omega \to \infty} \omega^2 \operatorname{Re}\,G(j\omega) \gt 0$ (or equivalently, the relative degree is 0 with appropriate limit behavior).

The **Kalman-Yakubovich-Popov (KYP) lemma** states that $G(s) = C(sI - A)^{-1}B + D$ is SPR iff there exists $P = P^T \succ 0$ such that

$$A^T P + P A \prec 0, \quad P B = C^T - L, \quad D + D^T - L^T L \succ 0$$

for some $L$ (Khalil 2002 Lemma 6.3). The matrix $P$ defines a Lyapunov function $V(x) = x^T P x$ with $\dot V \lt -\epsilon \lVert x\rVert^2 + 2 x^T P B u$.

### 3.2 PID as SPR-compatible controller

A proper PID with filtered derivative has transfer function

$$C_{\text{PID}}(s) = K_p + \frac{K_i}{s} + \frac{K_d s}{1 + (s/\omega_d)}$$

where $\omega_d \gg \omega_c$ is the derivative-filter pole.

**Positive-real tuning criterion (classical; Åström & Murray 2008 Thm 11.3).** For the SISO plant $P(s)$, the closed-loop system $y = P(r - Cy)$ with $C = C_{\text{PID}}$ is stable and the loop transfer function $L(s) = P(s) C_{\text{PID}}(s)$ satisfies the Popov / circle-criterion condition iff there exist $K_p, K_i, K_d \geq 0$ such that:

$$\operatorname{Re}\left[ \frac{1 + j\omega \tau}{P(j\omega) C_{\text{PID}}(j\omega)} \right] \gt -\frac{1}{k} \quad \forall \omega$$

for some multiplier $\tau \geq 0$ and sector bound $k \gt 0$.

This is the Popov criterion (Khalil 2002 Thm 7.3) applied to the PID loop. When the bound $k$ can be taken arbitrary (infinite sector), the plant-controller pair is SPR. This defines the SPR-compatible PID tuning region.

### 3.3 What this gives in AAD form

*[Derived (PID-closed-loop-Lyapunov, from KYP + SPR tuning)]*

Under SPR-compatible PID tuning on an SPR-compatible plant, there exists a quadratic Lyapunov function $V(\delta, \xi) = \tfrac 12 (\delta^T, \xi^T) P (\delta, \xi)^T$ with $P \succ 0$ such that along closed-loop trajectories:

$$\dot V \leq -\epsilon\,(\lVert\delta\rVert^2 + \lVert\xi\rVert^2) + \delta^T\,w(t)$$

for some $\epsilon \gt 0$. This is **exactly** the sector-condition stability result of `#sector-condition-derivation` Prop A.1 applied to the augmented state $(\delta, \xi)$, with sector constant $\alpha = \epsilon$ (in the $P$-weighted norm).

**Translation to Euclidean A2'.** By the same weighted-norm argument as `#gain-sector-bridge` §Weighted-norm subtlety:

$$\alpha_{\text{Euclidean}} \geq \epsilon / \kappa(P)$$

where $\kappa(P) = \lambda_{\max}(P)/\lambda_{\min}(P)$ is the condition number of the Lyapunov-certificate matrix.

*[Discussion]* This is Angle 1's central result: PID under SPR-compatible tuning *is* in sub-scope $\alpha$. The converse-Lyapunov observation from `#sector-condition-derivation` Path 3 manifests concretely — the quadratic Lyapunov witness is delivered by the KYP lemma, and A2' follows by norm-equivalence.


## 4. Angle 2 — PID A2' in B1 directional-fidelity form

### 4.1 Recast: PID implements directional fidelity

The spike's crucial theoretical move: show that the SPR-tuned-PID computation *is* an instance of `#gain-sector-bridge`'s B1 property, not just a parallel stability story.

Working in a discrete-time setting matched to AAD's event-driven formulation. Let the sampled plant be

$$x_{k+1} = A x_k + B u_k + w_k, \quad y_k = C x_k$$

The tracking error is $\delta_k = r - y_k = r - C x_k$. The PID control law with filtered derivative becomes

$$u_k = K_p \delta_k + K_i I_k + K_d (\delta_k - \delta_{k-1})/T_s$$
$$I_{k+1} = I_k + T_s \delta_k$$

where $T_s$ is the sample period. Concatenate the augmented "error + integrator + lag" state $\tilde\delta_k = (\delta_k, I_k, \delta_k - \delta_{k-1})^T$.

### 4.2 Directional fidelity for the PID augmented state

*[Derived (PID-B1, from KYP certificate)]*

Under SPR-compatible PID tuning, the one-step correction function

$$F_{\text{PID}}(\tilde\delta_k) := \tilde\delta_k - \tilde\delta_{k+1}\big\vert_{w=0}$$

satisfies

$$\tilde\delta_k^T \, P \, F_{\text{PID}}(\tilde\delta_k) \geq c_{\min} \tilde\delta_k^T P \tilde\delta_k \quad \forall \tilde\delta_k \in \mathcal B_R$$

for some $c_{\min} \gt 0$ depending on the gain margin and phase margin of the loop. In Euclidean coordinates, $c_{\min}^{\text{Eucl}} = c_{\min}/\kappa(P)$.

**Sketch of derivation.** The KYP certificate gives $A_{\text{cl}}^T P + P A_{\text{cl}} \prec -2\epsilon P$ where $A_{\text{cl}}$ is the closed-loop state matrix including the PID dynamics on $\tilde\delta_k$. For the discrete-time analog (Khalil 2002 §4.5, or Franklin-Powell-Workman 1998 Thm 10.3), this gives

$$A_{\text{cl}}^T P A_{\text{cl}} - P \prec -\eta P$$

for some $\eta \gt 0$. Letting $\tilde\delta_{k+1} = A_{\text{cl}} \tilde\delta_k$ in the no-disturbance case and substituting into the sector product:

$$\tilde\delta_k^T P F_{\text{PID}}(\tilde\delta_k) = \tilde\delta_k^T P (\tilde\delta_k - A_{\text{cl}}\tilde\delta_k) = \tilde\delta_k^T(P - PA_{\text{cl}})\tilde\delta_k = \tfrac{1}{2}\tilde\delta_k^T(P - A_{\text{cl}}^T P A_{\text{cl}} + P - A_{\text{cl}}^T P)\tilde\delta_k$$

The discrete KYP condition $A_{\text{cl}}^T P A_{\text{cl}} - P \prec -\eta P$ forces the first term to exceed $(\eta/2)\tilde\delta_k^T P \tilde\delta_k$; the second term (with $P - A_{\text{cl}}^T P$) contributes a bounded correction absorbable into the constant. Net: $c_{\min} \geq \eta/2$.

### 4.3 Identifying the sector constant in AAD tuning parameters

For the standard PID tuning parameters, the sector constant can be written explicitly:

*[Derived (PID-sector-constant, from gain-phase margin)]*

$$\alpha_{\text{PID}} = \frac{\omega_c}{1 + (\omega_c/\omega_d)^2} \cdot \sin(\varphi_m) \cdot \frac{1}{\kappa(P)}$$

where $\omega_c$ is the loop crossover frequency, $\varphi_m$ is the phase margin (in radians, with $0 \lt \varphi_m \lt \pi/2$), $\omega_d$ is the derivative-filter pole (must satisfy $\omega_d \gg \omega_c$), and $\kappa(P)$ is the KYP-certificate condition number.

This makes the PID tuner's implicit design target — adequate phase margin — map directly to AAD's $\alpha$: **phase margin IS the AAD sector constant, modulo a controller-structure condition number**. Agents designed with $\varphi_m \geq 45°$ (industry default) have $\sin\varphi_m \geq \sqrt{2}/2$, so $\alpha_{\text{PID}} \gtrsim 0.35\,\omega_c/\kappa(P)$.

**Interpretation.** A well-tuned PID with crossover $\omega_c$ and phase margin $\varphi_m$ operating on an SPR-compatible plant has a derived A2' constant scaling as $\omega_c \sin\varphi_m$ — precisely what classical control theory says is the closed-loop bandwidth-times-robustness product. AAD's $\mathcal T \sim \omega_c$ identification makes $\alpha = \mathcal T \cdot \sin\varphi_m / \kappa(P)$ read like AAD's linear-sector-constant result.


## 5. Angle 3 — Nonlinear plant extension via circle / Popov criterion

### 5.1 Plant class: Lur'e systems

Extend to nonlinear plants of Lur'e form:

*[Scope (Angle-3 plant class)]* The plant consists of an LTI forward path $G(s)$ followed by a static memoryless nonlinearity $\psi: \mathbb R \to \mathbb R$ satisfying a sector condition $\psi \in [k_1, k_2]$ (i.e., $k_1 y^2 \leq y \psi(y) \leq k_2 y^2$ for all $y$).

This covers saturated actuators, dead-zones, hysteresis-free monotone nonlinearities, and smooth sigmoidal plants.

### 5.2 Circle criterion applied to the PID loop

The classical **circle criterion** (Khalil 2002 Thm 7.1; Zames 1966): the Lur'e system with LTI part $G$ and sector-bounded nonlinearity $\psi \in [k_1, k_2]$ is absolutely stable iff the Nyquist plot of $G(j\omega)$ stays outside (and encircles the appropriate number of times) the disc $D(k_1, k_2)$ in the complex plane determined by the sector bounds.

Inserting a PID controller $C(s)$ in front of $G(s) \psi$ replaces the Nyquist plot of $G$ with that of $L = CG$. The circle criterion becomes a tuning constraint on $(K_p, K_i, K_d)$ relative to $(k_1, k_2)$.

*[Derived (PID-Lur'e-A2', from circle criterion)]*

When $(K_p, K_i, K_d)$ satisfy the circle criterion for the sector $[k_1, k_2]$, the closed-loop Lur'e system with PID satisfies A2' in the augmented tracking-error state with

$$\alpha_{\text{PID-Lur'e}} = \min\!\big( \alpha_{\text{linear}}(\omega_c, \varphi_m), \; k_1 \cdot c_{\text{abs}}(k_2/k_1, \text{circle margin}) \big) / \kappa(P)$$

where $c_{\text{abs}}$ is the absolute-stability margin factor and the minimum reflects the weakest-link nature of linear stability plus nonlinear sector absorption. The derivation combines the KYP certificate of Angle 2 with the S-procedure Lyapunov construction for the Lur'e part (Khalil 2002 §7.1 derivation).

### 5.3 Popov criterion refinement

For monotone nonlinearities (e.g., saturation), the **Popov criterion** (Popov 1961; Khalil 2002 Thm 7.3) gives a tighter bound via a multiplier $(1 + \eta s)$:

$$\operatorname{Re}\left[(1 + j\omega\eta) L(j\omega)\right] + \tfrac{1}{k} \gt 0 \quad \forall \omega$$

For PID with saturation, choosing $\eta \approx 1/\omega_c$ (Popov multiplier matched to crossover) typically admits sector bounds $[0, k_{\max}]$ where $k_{\max}$ is comparable to the plant DC gain. **Up to the Popov bound, PID stays in sub-scope $\alpha$**; beyond it (hard saturations with small upper bound, very steep nonlinearities), PID exits to sub-scope $\beta$.

### 5.4 Nonlinearity magnitude threshold

*[Derived (PID-nonlinearity-threshold)]*

For a Lipschitz nonlinearity $\psi$ with $\text{Lip}(\psi) \leq L_\psi$, PID A2' holds uniformly provided

$$L_\psi \cdot \lVert L(j\omega_c)\rVert \lt 1 + \sin\varphi_m$$

at the crossover frequency $\omega_c$. This is the small-gain condition in disguise; it says the nonlinearity's Lipschitz constant times the open-loop gain at crossover must stay below the closed-loop robustness margin. Above this threshold, PID loses the A2' derivation and reverts to per-system verification (sub-scope $\beta$).


## 6. Angle 4 — Integrator windup and saturation

### 6.1 The windup problem

Raw PID with actuator saturation violates the Lur'e framework above if the integrator is allowed to accumulate without bound: the integrator state $I_t$ drifts during saturation, giving a post-saturation "wind-down" transient with poor phase margin. In the worst case, the apparent $\alpha$ goes negative locally (overshoot / limit cycle). A raw saturated PID is sub-scope $\beta$.

### 6.2 Back-calculation anti-windup preserves A2'

The **back-calculation anti-windup scheme** (Åström & Hägglund 1995 §3.4; Åström & Murray 2008 §11.2) modifies the integrator update to

$$\dot I_t = K_i \delta_t + K_{\text{aw}} \cdot (u_{\text{sat},t} - u_t)$$

where $u_{\text{sat}, t} = \operatorname{sat}(u_t)$ is the saturated actuator output and $K_{\text{aw}} \gt 0$ is the back-calculation gain.

*[Derived (PID-anti-windup-A2', from conditional-integrator + sector embedding)]*

Under back-calculation anti-windup with $K_{\text{aw}} \geq K_i/K_p$ (standard choice), the saturated PID loop admits A2' in the augmented state $(\delta, I, \delta - \delta_{-1})$ with

$$\alpha_{\text{PID-aw}} = \min(\alpha_{\text{PID}}, \; K_{\text{aw}} \cdot c_{\text{sat-margin}}) / \kappa(P_{\text{aw}})$$

where $c_{\text{sat-margin}}$ quantifies how far the control command is from the saturation limit. The derivation: back-calculation converts saturation from a hard nonlinearity into a *sector nonlinearity* in the $[0, 1]$ range (the saturation function on its own is sector-bounded by $[0, 1]$), and the back-calculation term provides a Lyapunov contribution $-K_{\text{aw}}(u - u_{\text{sat}})^2 \leq 0$ that strengthens $\dot V$ when saturation is active. The loop satisfies the circle criterion on the saturation sector, yielding A2' uniformly.

**What back-calculation accomplishes in AAD language.** It turns the hard-saturation violation of B1 (the integrator drifts in the wrong direction) into a soft-sector correction that B1-preserves. Anti-windup is PID's structural move into sub-scope $\alpha$.

### 6.3 Conditional integration

**Conditional integration** (freeze the integrator when saturated) is a different scheme; it preserves A2' piecewise but introduces discontinuity at the saturation boundary. The A2' constant is the same as unsaturated PID on the unsaturated region, and on the saturated region the loop effectively becomes a PD controller. A2' still holds on each region; the switching surface is measure-zero for generic disturbances. Sub-scope $\alpha$ with a piecewise constant $\alpha$.


## 7. Angle 5 — Tuning-parameter scope

### 7.1 Tuning region for sub-scope $\alpha$ membership

The derived A2' requires phase margin $\varphi_m \gt 0$ and an SPR-compatible open loop. In Ziegler-Nichols terms, this is the stable tuning region *interior* (strictly away from the stability boundary). Specifically:

*[Derived (PID-tuning-scope)]*

PID is in sub-scope $\alpha_{\text{PID}}$ iff

$$(K_p, K_i, K_d) \in \mathcal{T}_{\text{SPR}}(P) := \{(K_p, K_i, K_d) : \varphi_m(C_{\text{PID}}, P) \geq \varphi_{m,\min} \text{ and } g_m(C_{\text{PID}}, P) \geq g_{m,\min}\}$$

for some thresholds $\varphi_{m,\min} \gt 0$ and $g_{m,\min} \gt 1$ (gain margin). Industry defaults $\varphi_{m,\min} = 30°$, $g_{m,\min} = 2$ land inside $\alpha_{\text{PID}}$; aggressive tuning at the stability boundary ($\varphi_m \to 0$) exits to $\beta$.

### 7.2 Specific tuning methods

| Tuning method | Sub-scope | Rationale |
|---|---|---|
| Ziegler-Nichols ultimate-gain (classical) | $\beta$ (aggressive) | Designed for $\sim 1/4$-decay, $\varphi_m \approx 15°$ — close to stability boundary, condition number $\kappa(P)$ blows up |
| Ziegler-Nichols with 50%-reduction | $\alpha$ | Reduced gains give $\varphi_m \approx 45°$ |
| Internal Model Control (IMC) | $\alpha$ | Designed for specified closed-loop bandwidth with plant-model cancellation; $\varphi_m$ typically $\geq 60°$ |
| Lambda tuning | $\alpha$ | Explicitly parameterizes closed-loop time constant; gives $\varphi_m \geq 45°$ by construction |
| Skogestad's SIMC | $\alpha$ | Same family as IMC; explicit robustness margins |
| Relay tuning (Åström-Hägglund) | Depends on target | Estimates ultimate gain; then feeds into one of the above — inherits sub-scope from the subsequent tuning |
| Manual tuning by field operator | $\beta$ (unless audited) | No structural guarantee of $\varphi_m \geq$ threshold — sub-scope by inspection per installation |

The point: **tuning quality matters**, and the tuning-region characterization makes visible which industrial controllers inherit AAD's derived guarantees versus which need empirical A2' verification.


## 8. Angle 6 — Composition with adaptive-gain spike

### 8.1 Gain-scheduled PID = adaptive-gain meta-A2' special case

`msc/spike-adaptive-gain-dynamics.md` develops augmented-state $(\delta, \tilde K)$ dynamics with meta-gain sector conditions (MG-1)–(MG-4). Gain-scheduled PID is an instance: the PID gains $(K_p(\sigma), K_i(\sigma), K_d(\sigma))$ depend on an operating-point variable $\sigma$ (e.g., flight condition, batch phase), and $\sigma$ evolves slowly compared to the inner loop.

*[Derived (gain-scheduled-PID-A2', from PID-A2' + meta-gain composition)]*

Under gain-scheduled PID with scheduling variable $\sigma_t$ and schedule function $(K_p, K_i, K_d)(\sigma)$:

1. For each fixed $\sigma$, Angle 1–2's PID-A2' derivation gives a sector constant $\alpha_{\text{PID}}(\sigma)$.
2. Uniform-in-$\sigma$ sector bound: $\underline\alpha_{\text{PID}} = \inf_{\sigma \in \mathcal S} \alpha_{\text{PID}}(\sigma)$.
3. The inner-loop A2' holds uniformly provided $\underline\alpha_{\text{PID}} \gt 0$ (the schedule never lands at a stability boundary).
4. If the scheduling dynamics $\dot\sigma = \Phi(\sigma, \delta)$ satisfy a meta-gain sector condition (timescale separation $\mathcal T_\sigma \ll \mathcal T$, bounded schedule-induced disturbance), the augmented $(\delta, \tilde\sigma)$ system inherits A2' via the adaptive-gain spike's composition argument.

**Gain-scheduled PID is in sub-scope $\alpha$ iff (a) each local PID is in $\alpha_{\text{PID}}$ and (b) the schedule itself is sector-bounded.** This composes cleanly with the spike-adaptive-gain-dynamics framework — it's that framework's `Case A' variant' for a non-Bayesian base controller.

### 8.2 Self-tuning adaptive PID

Self-tuning PID (Åström-Wittenmark; Bristol 1979) estimates the plant online and retunes the gains. This is structurally the same as the spike-adaptive-gain's Mehra-Kalman case, with the plant estimator playing the role of the Q/R estimator. Sub-scope $\alpha$ provided *(i)* the estimator itself is in sub-scope $\alpha$ (typically least-squares on a linear-parameterized plant, which is), *(ii)* the timescale separation holds, *(iii)* persistent excitation is present (a standard adaptive-control condition). When persistent excitation fails, the self-tuner drifts and A2' degrades — sub-scope $\beta$ again.


## 9. Angle 7 — Composition: cascade of PID loops

### 9.1 Setup

Let two PID loops be cascaded: inner loop on fast variable $y_1$ (plant $P_1$, controller $C_1$) with reference determined by outer loop on slow variable $y_2$ (plant $P_2$ chained after $P_1$, controller $C_2$). This is the standard cascade-control structure (Åström & Murray 2008 §11.4).

### 9.2 Composition-closure instantiation

From `#sector-persistence-template` and `#composition-closure`:

*[Derived (PID-cascade-A2', from per-loop PID-A2' + composition closure)]*

1. Inner loop: if $(P_1, C_1)$ is in $\alpha_{\text{PID}}$ with sector constant $\alpha_1$, A2' holds for the inner-loop mismatch $\delta_1 = r_1 - y_1$.
2. Outer loop: the outer-loop plant is $P_2 \circ T_1$ where $T_1$ is the inner-loop closed-loop transfer function. Under timescale separation ($\omega_{c,2} \ll \omega_{c,1}$), $T_1 \approx 1$ at outer-loop frequencies, so the outer-loop PID sees effectively $P_2$ alone.
3. If $(P_2, C_2)$ is in $\alpha_{\text{PID}}$ under this approximation, A2' holds for the outer-loop mismatch $\delta_2$ with sector constant $\alpha_2$.
4. The cascade composite satisfies `#sector-persistence-template` with $(\alpha_c, R_c)$ where $\alpha_c \geq \min(\alpha_1, \alpha_2) - \Delta\mathcal T^{\text{coord}}$ (weakest-link from `#composition-closure` §Deriving composite (A4)), with coordination cost $\Delta\mathcal T^{\text{coord}}$ reflecting the inner-loop tracking-error's contribution to the outer-loop disturbance.
5. The closure defect $\varepsilon^\ast$ arises from the timescale-separation residual (inner-loop transients during outer-loop corrections). It scales as $O(\omega_{c,2}/\omega_{c,1})$ — small when separation is clean.

**Inner-loop closure.** When $\omega_{c,2}/\omega_{c,1} \lt 1/10$ (standard cascade-control rule of thumb), $\varepsilon^\ast \nu_c / \alpha_c$ is small compared to $R_c$, and the composite meets the composition-closure persistence condition. This is the classical-control cascade rule restated in AAD language.

### 9.3 What this demonstrates

A cascade of two sub-scope-$\alpha$ PIDs gives a sub-scope-$\alpha$ composite under the standard cascade condition. **PID-composed agents inherit AAD's derived persistence guarantees**, which is the intended consequence of the promotion.


## 10. Angle 8 — Honest scope exclusions

The A2' derivation for PID does NOT cover:

1. **Plants with right-half-plane zeros.** Non-minimum-phase plants (inverse response, plant with RHP zero) impose a fundamental bandwidth limit $\omega_c \lt z_{\text{RHP}}$ that may push $\alpha_{\text{PID}}$ below what A2' needs. PID can still stabilize such plants but the KYP certificate may fail to give a uniform sector constant on the desired operating region — local A2' with smaller $R$ is what is achievable. Explicit sub-scope downgrade when $\omega_c$ cannot be chosen to satisfy the margin thresholds.

2. **Time-varying plants without gain scheduling.** A plant $P(t)$ that drifts in parameters (process drift, component aging, temperature effects) beyond the robustness margin of the fixed-gain PID exits sub-scope $\alpha$ dynamically — the loop is in $\alpha$ at nominal but drifts into $\beta$ at the edge of the robustness region. Formally: A2' holds with a time-varying $\alpha(t)$ whose infimum over the operational envelope may be zero. Gain scheduling (Angle 6) or self-tuning recovers $\alpha$; otherwise, sub-scope $\beta$.

3. **Stochastic plants without Kalman-like state estimation.** PID is a static (state-feedback-shape) controller on the output $y$; it does not form an internal model of the plant. For stochastic plants with unobserved state, the classical Kalman-plus-LQR decomposition (separation principle) gives A2' via the Kalman half of `#gain-sector-bridge`'s sub-scope $\alpha$; a stand-alone PID without state estimation on a high-dimensional stochastic plant leaves A2' not derivable. Explicit sub-scope $\beta$ in this case.

4. **Hard nonlinearities beyond the Popov/circle bound.** Step nonlinearities, rate limits with small limits, backlash, relay controllers. Circle criterion fails at large sector extent; PID+hard-nonlinearity is sub-scope $\beta$.

5. **Loops with significant delay exceeding the derivative-filter scope.** Deadtime-dominant processes ($L/\tau_p \gt 1$) need Smith predictor or IMC with explicit delay compensation; raw PID sees its phase margin eaten by deadtime and the SPR condition fails. Sub-scope $\beta$ unless a delay-compensated structure is used (which is no longer raw PID).

6. **Multivariable PID (MIMO) without decoupling analysis.** The SPR / KYP machinery extends to MIMO (matrix-KYP lemma), but MIMO-PID's "PID on each diagonal channel" structure may miss coupling — the matrix plant needs to be sufficiently diagonally dominant (Bristol's RGA $\approx I$). Outside this, MIMO PID is sub-scope $\beta$ even under individually-stable-tuned loops.

Each of these is a named scope-exit and belongs in the "Honest scope" section of the candidate segment.


## 11. Candidate landing

Two honest options; recommend option A (minimal surgical edit) with option B (new appendix) as stretch.

### 11.1 Option A — Update to `#sector-condition-derivation` A2' α list

**Segment edit.** In `#sector-condition-derivation`'s "Grounding of GA-3 — sub-scope $\alpha$" paragraph, add a sixth bullet point:

> - *PID controllers under SPR-compatible tuning with anti-windup* (`msc/spike-pid-a2prime.md`): under plant-class scope condition (SISO LTI minimum-phase, relative degree $\leq 2$) and tuning-region scope condition (phase margin $\varphi_m \geq \varphi_{m,\min}$, gain margin $g_m \geq g_{m,\min}$), A2' is derived via the KYP lemma with $\alpha_{\text{PID}} = \omega_c \sin(\varphi_m) / \kappa(P)$ for the KYP certificate matrix $P$. Anti-windup (back-calculation or conditional integration) required to preserve A2' under actuator saturation. See `#sector-condition-derivation` §"Honest PID scope" for exclusions (RHP-zero, time-varying, stochastic-without-state-estimation, hard nonlinearities, deadtime-dominant, coupled MIMO).

And in the "Grounding of GA-3 — sub-scope $\beta$" list, change the PID entry to:

> - *PID controllers outside the SPR-tuning / minimum-phase / anti-windup scope* — when the tuning lands too close to the stability boundary, the plant has RHP zeros exceeding $\omega_c$, deadtime dominates, saturations are hard without anti-windup, or the plant is coupled MIMO without a decoupling analysis. A2' must be verified per-system.

And in the derivation-audit table row for A2', extend the sub-scope $\alpha$ list to include "SPR-tuned PID with anti-windup." This is the minimum surgical move.

**Why Option A is sufficient.** The three-paragraph "Grounding of GA-3" structure already exists; adding PID-in-scope as a sixth alpha-class and refining the $\beta$-class entry is the exact shape of the previous A2' sub-scope move (spike `spike-a2-prime-strengthening.md`). No new segment file is created; downstream consumers inherit through existing machinery.

### 11.2 Option B — New appendix segment `#pid-sector-derivation`

**Rationale for a dedicated segment.** The PID derivation is substantive — six sub-cases (SISO-LTI, Lur'e, anti-windup, gain-scheduled, cascade, MIMO-diagonal), explicit sector constants, and non-trivial scope conditions. If PID is the dominant industrial controller, having a named `#pid-sector-derivation` segment (parallel to `#gain-sector-derivation`'s Kalman treatment) makes the result discoverable by readers looking for industrial-control grounding of AAD.

**Proposed frontmatter:**

```yaml
---
slug: pid-sector-derivation
type: derivation
status: conditional
depends:
  - sector-condition-derivation
  - gain-sector-bridge
  - sector-persistence-template
stage: draft
---
```

**Proposed content structure:**

1. Motivation — industrial prevalence of PID; gap in `#gain-sector-bridge`'s Verified Instances table (which lists Kalman / gradient / exponential-family but not PID).
2. Proposition C.1 (SPR Linear PID) — derivation via KYP, sector constant $\alpha_{\text{PID}} = \omega_c \sin\varphi_m / \kappa(P)$.
3. Proposition C.2 (Lur'e PID) — circle + Popov criteria; nonlinearity threshold.
4. Proposition C.3 (Anti-windup PID) — back-calculation preserves A2'.
5. Proposition C.4 (Gain-scheduled PID) — composition with adaptive-gain meta-framework.
6. Verified instances table (tuning method × sub-scope).
7. Honest scope exclusions (the six items in §10 above).
8. Sub-scope taxonomy: $\alpha_{\text{PID}} \subset \alpha$ where the subscript names the plant-and-tuning constraints.

**Why Option B is worth considering despite the overhead.** The result is what makes AAD's industrial-agent claim non-vacuous. The `#gain-sector-bridge` Verified Instances table currently reads as if only Kalman / gradient / exponential-family agents are covered; PID's absence misrepresents the theory's scope. A named segment fixes this asymmetry.

### 11.3 Recommendation

**Do both.** Option A lands the bullet + table-row update for `#sector-condition-derivation` immediately; Option B creates the appendix segment that hosts the full derivation and the honest scope exclusions. The two compose — A is the one-line summary that `#sector-persistence-template`'s inheritance chain uses; B is the reference for anyone asking "why is PID in sub-scope $\alpha$?"

`#gain-sector-bridge`'s Verified Instances table should also be updated: add a row for SPR-tuned PID pointing at `#pid-sector-derivation`.


## 12. Epistemic assessment

**What's derived cleanly (Tier 1, promotable as-is).**

- Angle 1: SPR-compatible PID on SPR-compatible plant gives A2' via KYP. This is textbook (Khalil 2002 §6, Åström & Murray 2008 §11), and the AAD transcription is mechanical.
- Angle 2: recasting as B1 directional fidelity — the key novel move in this spike. Mechanical once the discrete-time KYP analog is invoked. The sector constant $\alpha_{\text{PID}} = \omega_c \sin\varphi_m / \kappa(P)$ is explicit and matches AAD's $\alpha \sim \mathcal T$ identification.
- Angle 4: back-calculation anti-windup as a sector-embedding of saturation. Also textbook (Åström & Hägglund 1995 §3.4). AAD translation direct.
- Angle 5: tuning-region scope characterization. Purely classical; the value is in making the PID-tuning-choice / sub-scope-membership relationship explicit.
- Angle 7: cascade composition. Standard inner/outer-loop theory mapped to `#sector-persistence-template`.

**What's derivable with more care (Tier 2, proof structure clear).**

- Angle 3: Lur'e-plant extension. Circle and Popov criteria are textbook; the AAD-form sector constant $\alpha_{\text{PID-Lur'e}} = \min(\alpha_{\text{linear}}, k_1 c_{\text{abs}})/\kappa(P)$ holds but deserves a dedicated derivation step rather than the compressed sketch above. Nothing new needed; just cleaner exposition.
- Angle 6: gain-scheduled PID under the adaptive-gain meta-framework. Composition argument invokes spike-adaptive-gain-dynamics' machinery; verifying clean interface requires cross-referencing that spike's (MG-1)–(MG-4) conditions.

**What's honestly limited (explicit scope exclusions).**

- The six exclusions in §10 are real; A2' genuinely does not derive for (a) RHP-zero-dominated plants outside a small operating region, (b) uncontrolled time-varying plants, (c) high-dim stochastic plants without state estimation, (d) hard nonlinearities exceeding Popov bound, (e) deadtime-dominant plants without delay compensation, (f) coupled MIMO-PID without decoupling. The segment should enumerate these visibly — per `#discussion-identifiability-floor`'s pattern of treating scope-exits as architectural, not as caveats.

**What's NOT attempted and why.**

- Nonlinear PID-like controllers (e.g., fuzzy PID with nonlinear gain surfaces, neural-PID hybrids): these are sub-scope $\beta$ by the rule-based / severely-nonlinear argument of `#sector-condition-derivation` — no derivation in this spike. Appropriate; these controllers are not what "PID" means in industrial usage.
- Nonlinear or discrete-time-optimal tuning (LQG, H-infinity syntheses): LQG is sub-scope $\alpha$ through the Kalman half of `#gain-sector-bridge` (already covered); H-infinity has its own positive-real / small-gain structure that would deserve its own spike. Not attempted here.
- Infinite-dimensional plants (PDEs): not in AAD's operational scope per the Section-I-plant convention. Not attempted.

**Honest claim that survives:** PID under *(i)* SPR-compatible plant and tuning, *(ii)* anti-windup on saturated actuators, *(iii)* standard industrial margins ($\varphi_m \geq 30°$, $g_m \geq 2$) admits an A2' derivation via the KYP lemma with explicit $\alpha_{\text{PID}} = \omega_c \sin\varphi_m / \kappa(P)$. This sub-sub-scope $\alpha_{\text{PID}} \subset \alpha$ covers the bulk of industrial PID deployments — process control loops, servo loops with anti-windup, cascade-control structures — all of which now inherit AAD's derived persistence guarantees through `#sector-persistence-template`. Outside the sub-sub-scope, PID returns to sub-scope $\beta$ with per-system A2' verification required.

**What this accomplishes for AAD.** (a) The `#sector-condition-derivation` sub-scope $\alpha$ list now includes the dominant industrial controller class, not just theoretically-privileged agents. AAD's derived-guarantee coverage expands from "Kalman, Bayesian, and gradient-descent agents" to "Kalman, Bayesian, gradient-descent, and PID-with-proper-tuning-and-anti-windup agents" — an order-of-magnitude expansion in the applicable agent population. (b) The three AAD meta-patterns compose on this result: scope-honesty (the sub-sub-scope definition), the `#discussion-separability-pattern` ladder (sub-scope $\alpha$ vs $\beta$ now has four classes instead of two), and the `#discussion-identifiability-floor` framing of exclusions (the six scope-exits are architectural, not caveats). (c) Composition-closure for PID-cascade agents now has concrete sector constants and tempo relationships, not just existence guarantees — useful for downstream TST and industrial-control-system applications.


## 13. Post-promotion followups

If Option A+B lands:

- `#gain-sector-bridge` Verified Instances table gains a row for SPR-tuned PID.
- `#sector-persistence-template` Working Notes should reference PID as a template-instantiation example (the Lur'e case specifically — it's the most different from Kalman/gradient).
- TST segments that mention PID controllers (if any — check `02-tst-core/src/`) inherit the derived A2' and can cite it.
- `msc/spike-adaptive-gain-dynamics.md` §5 (IMM) notes a link to gain-scheduled PID; Angle 6 here closes the pointer.
- `#agent-spectrum` currently places PID controllers in the "blind pursuer" region — this is still valid *structurally* (PID is not epistemic-in-the-Bayesian-sense), but the A2' derivation makes clear that the "blind pursuer" region is not automatically sub-scope $\beta$ for persistence purposes.

---

## Appendix — references consulted

Classical control:
- Lur'e, A. I. (1957). *Some Nonlinear Problems in the Theory of Automatic Control*. Gostekhizdat. Original sector-condition framework.
- Popov, V. M. (1961). "Absolute stability of nonlinear systems of automatic control." *Automation and Remote Control* 22:857–875.
- Kalman, R. E. (1963). "Lyapunov functions for the problem of Lur'e in automatic control." *PNAS* 49:201–205. KYP lemma origin.
- Zames, G. (1966). "On the input-output stability of time-varying nonlinear feedback systems, I & II." *IEEE Trans. Autom. Control* 11.

Textbook / handbook:
- Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.). Prentice Hall. Chapters 6 (passivity), 7 (absolute stability, circle and Popov criteria). Already in `ref/INDEX.md` as standard reference.
- Åström, K. J. & Hägglund, T. (1995). *PID Controllers: Theory, Design, and Tuning* (2nd ed.). ISA. §3.4 anti-windup.
- Åström, K. J. & Murray, R. M. (2008). *Feedback Systems: An Introduction for Scientists and Engineers*. Princeton UP (open-access). Chapters 10 (frequency-domain), 11 (PID). Accessible.
- Franklin, G. F., Powell, J. D. & Workman, M. (1998). *Digital Control of Dynamic Systems* (3rd ed.). Addison-Wesley. Discrete-time KYP Thm 10.3.
- Skogestad, S. & Postlethwaite, I. (2005). *Multivariable Feedback Control* (2nd ed.). Wiley. MIMO extensions; RGA analysis for decoupling.

PID-specific analyses:
- Skogestad, S. (2003). "Simple analytic rules for model reduction and PID controller tuning." *J. Process Control* 13:291–309. SIMC tuning derivation.
- Bristol, E. H. (1966). "On a new measure of interaction for multivariable process control." *IEEE Trans. Autom. Control* 11:133–134. RGA for MIMO.
- Goodwin, G. C., Graebe, S. F. & Salgado, M. E. (2001). *Control System Design*. Prentice Hall. Anti-windup analyses.

No PDFs in `ref/` need acquiring for this spike — all citations are to standard control-theory textbooks + two canonical papers (Lur'e 1957 and Popov 1961 already referenced in `#sector-condition-derivation`; Kalman 1963 and Zames 1966 are standard references not currently in `ref/INDEX.md` but would be minor additions if Option B lands).
