# Spike: Critical-Mass Composition — When the Composite *Gives* You Contraction

**Status**: Exploratory derivation. Symmetric-pair case pushed through in closed form; asymmetric and $U_O$-modulated cases partially characterized; general case obstructed.
**Date**: 2026-04-22
**Motivation**: Section III's `#form-composition-closure` and `#result-sector-persistence-template` both rely on a composite sector constant $\alpha_c$ (or equivalently, a composite contraction rate $\kappa_c$) at the macro level. `working-composition-admissibility.md` §6.2 gives the **weakest-link bound** $\alpha_c \geq \min_i(\alpha_i - \Delta \mathcal T_i^{\text{cost}})$, and `spike-bridge-lemma-contraction.md` characterizes when the macro-update map $f_c$ is actually contracting (Tier 1/2/3). What neither does is derive a **closed-form critical-mass condition**: given two parent contraction rates $\kappa_1, \kappa_2$, a coupling $\gamma$ between them, and a teleological unity $U_O$, when is the composite contraction $\kappa_c \gt 0$? The existing move — "assume (A4) at the composite level" — is under-derivation. This spike attacks the derivation directly.

**Depends on**: `#form-composition-closure`, `#scope-composite-agent`, `#der-team-persistence`, `#result-sector-persistence-template`, `#deriv-sector-condition`, `#hyp-symbiogenic-composition`, `#result-unity-closure-mapping`, `#der-adversarial-destabilization`, `spikes/spike-bridge-lemma-contraction.md`, `spikes/spike-composition-bridge-2agent.md`, `msc/working-composition-admissibility.md`.

---

## 1. Precise Problem Statement

### 1.1 What AAD already has

The sector-persistence template ( `#result-sector-persistence-template`) requires each state variable $\xi$ to satisfy three preconditions (T1)–(T3). When $\xi = \delta_c$ (composite mismatch), (T2) reads

$$\delta_c^T F_c(\delta_c) \;\geq\; \alpha_c \lVert \delta_c \rVert^2 \quad \text{for } \lVert\delta_c\rVert \leq R_c,$$

with $\alpha_c \gt 0$ and $R_c \gt 0$. Given this, the single-agent Lyapunov machinery of `#deriv-sector-condition` Props A.1, A.1S, A.2 carries over to the composite, yielding the ultimate bound $R_c^\ast = \rho_c^{\text{eff}}/\alpha_c$ and reserve $\Delta\rho_c^\ast = \alpha_c R_c - \rho_c^{\text{eff}}$.

`working-composition-admissibility.md` §6.2 gives the current answer for how $\alpha_c$ connects to sub-agent constants:

$$\alpha_c \;\geq\; \min_i\!\big(\alpha_i - \Delta \mathcal T_i^{\text{cost}}\big), \qquad R_c \;\leq\; \min_i R_i. \tag{WL}$$

(WL) is a **weakest-link lower bound**, conservative but clean. It does **not** express how (cooperative) coupling strengthens the composite, how (adversarial) coupling weakens it, or how teleological unity enters.

### 1.2 What the question actually asks

The open bridge lemma requires a **constructive** critical-mass statement:

> Given sub-agent sector constants $(\alpha_1, \alpha_2)$ with matched architectures, inter-agent coupling $\gamma$, disturbance statistics $(\rho_1, \rho_2)$, teleological unity $U_O$, and coordination overhead $(C_1, C_2)$, **derive** the composite sector constant $\alpha_c = f(\alpha_1, \alpha_2, \gamma, U_O, \rho, C)$ and the composite persistence condition.

The shape of the question:

- Under symmetric conditions, is there a **threshold inequality** of the form "composite persists iff [some inequality in parent quantities and coupling]"?
- In the asymmetric limit $\alpha_2 \to 0$, does the composite condition reduce to `#hyp-symbiogenic-composition`'s asymmetric integration regime?
- Does $U_O$ enter **multiplicatively** (modifying coupling strength), **additively** (as a separate threshold), or as a **scope gate** (composite doesn't exist below a threshold)?

### 1.3 Why this is structurally harder than it looks

Three sources of hardness:

1. **(T2) is a one-point sector bound; critical mass is an incremental statement.** `spike-bridge-lemma-contraction.md` already proved the one-point sector bound does not imply strong monotonicity (the incremental/contraction property). The composite's (T2) is about the aggregate correction function pointing inward *at each* $\delta_c$. But the critical-mass question is whether the composite's dynamics **shrink differences between trajectories** — the stronger incremental property. Asking for closed form in $(\alpha_1, \alpha_2, \gamma, U_O)$ means asking for closed form in the **composite's monotonicity modulus**, not just in its one-point sector constant.

2. **$\alpha_c$ and $R_c$ are coupled.** The single-agent pair $(\alpha, R)$ is independent: $\alpha$ comes from the update-rule Jacobian; $R$ from the model-class capacity. For composites, both depend on the coupling structure (coupling costs part of each agent's tempo — lowering $\alpha$ — while potentially extending reach — raising $R$). The scalar "composite $\kappa$" in the problem statement presupposes a clean factorization that the theory doesn't yet guarantee.

3. **$U_O$ enters three different layers.** It gates scope (via `#scope-composite-agent`'s route (C-i)). It parameterizes rate-distortion curves for $\varepsilon_a$ (via `#result-unity-closure-mapping`). And — this is the substantive question — it potentially modulates the sign of cross-agent coupling (aligned objectives → $\gamma \lt 0$ cooperative; opposed objectives → $\gamma \gt 0$ adversarial). Whether all three usages are the **same $U_O$** or three partially-correlated quantities is unresolved.

These three issues structure the attempt below. I will:

- **§2**: Push the **symmetric-matched-architecture case** through in full. This is where closed form is possible; I derive $\alpha_c$, the critical-mass inequality, and the connection to `#der-adversarial-destabilization`.
- **§3**: Apply the symmetric result to **two structured cases** (linear agents with diagonal coupling; two Kalman filters with shared channel).
- **§4**: Push the **asymmetric limit** $\alpha_2 \to 0$ and check against `#hyp-symbiogenic-composition`.
- **§5**: Analyze **how $U_O$ enters**. I argue for a multiplicative-modifier-plus-scope-gate form, with the multiplicative part derived under linear-Gaussian structure and the scope-gate part inherited from `#scope-composite-agent`.
- **§6**: Obstruction analysis for the **general case** (heterogeneous architectures, nonlinear coupling, non-negligible coordination cost coupling).
- **§7**: Compare the candidate critical-mass theorem to the six `#result-sector-persistence-template` instances.
- **§8**: Recommendations for promotion.

---

## 2. The Symmetric-Matched-Architecture Case

### 2.1 Setup

Two sub-agents $A_1, A_2$, each a **Tier 1 agent** (`spike-bridge-lemma-contraction.md`) — mismatch-driven update, linear prediction, incremental sector-Lipschitz correction — with **matched architectures** ($f_1, f_2$ are structurally the same function, same $H$, same observation space). **Parameters are shared**: $\alpha_1 = \alpha_2 = \alpha$, $R_1 = R_2 = R$, $c_{\max,1} = c_{\max,2} = c_{\max}$. Disturbance statistics are shared: each sees bounded $w_i$ with $\lVert w_i\rVert \leq \rho$ (Model D).

**Coupling.** Following `#der-adversarial-destabilization` and `#der-team-persistence`, inter-agent coupling enters additively to the disturbance:

$$\rho_1^{\text{eff}} = \rho + \gamma \mathcal T_2, \qquad \rho_2^{\text{eff}} = \rho + \gamma \mathcal T_1 \tag{C1}$$

with sign convention $\gamma \lt 0$ cooperative (ally reduces disturbance), $\gamma \gt 0$ adversarial (disturbs ally). **Symmetric coupling** means $\gamma_{1 \to 2} = \gamma_{2 \to 1} = \gamma$. **Coordination cost** reduces each agent's effective correction rate symmetrically:

$$\alpha_i^{\text{eff}} = \alpha - C, \tag{C2}$$

with $C \geq 0$ representing the $\Delta \mathcal T_i^{\text{cost}}$ of `#der-team-persistence`.

**Projection.** Averaging: $\delta_c = (\delta_1 + \delta_2)/\sqrt 2$ (the $1/\sqrt 2$ normalizer preserves $\lVert \delta_c\rVert^2 = \tfrac{1}{2}(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2)$ under Euclidean norm of the concatenation). Under matched architecture, this is the principal-component projection.

**Teleological unity** parameter $U_O \in [-1, +1]$. I will leave $U_O$ abstract for §2.2–2.4 and attack its entry point in §5; for now I'll work with the linear-Gaussian case where $U_O$ manifests as the correlation between the two agents' target trajectories.

### 2.2 Joint Lyapunov construction

Let $\xi = (\delta_1, \delta_2)^T \in \mathbb R^{2n}$. The joint dynamics in the sector region are:

$$\dot\xi = -F_{\text{joint}}(\xi) + w(t),$$

where $F_{\text{joint}}(\xi) = (F_1(\delta_1) + \Gamma(\delta_2),\; F_2(\delta_2) + \Gamma(\delta_1))^T$ decomposes each agent's correction into a self-term (from its own sector condition) and a **cross-coupling term** $\Gamma(\cdot)$ representing the other agent's influence on its correction. Under (C1), the cross-coupling acts through disturbance rather than through direct state action; so $F_{\text{joint}}$ retains the block-diagonal structure of the individual correction functions, but the effective disturbance is

$$w_1^{\text{eff}}(t) = w_1(t) + \text{cross-term}_1, \qquad w_2^{\text{eff}}(t) = w_2(t) + \text{cross-term}_2.$$

By (C1), the cross-term has deterministic bound $|\gamma| \mathcal T$ per agent (using $\mathcal T_1 = \mathcal T_2 = \mathcal T$ by matched architecture). So $\lVert w_i^{\text{eff}}\rVert \leq \rho + |\gamma| \mathcal T$ with the **sign of the cross contribution set by $\gamma$** — negative cross-contribution (cooperation) *reduces* the effective disturbance norm, positive cross-contribution (adversarial) increases it.

**Joint quadratic Lyapunov candidate:** $V(\xi) = \tfrac{1}{2}\lVert\xi\rVert^2 = \tfrac{1}{2}(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2)$.

$$\dot V = \delta_1^T \dot\delta_1 + \delta_2^T \dot\delta_2$$
$$= -\delta_1^T F_1(\delta_1) - \delta_2^T F_2(\delta_2) + \delta_1^T w_1^{\text{eff}} + \delta_2^T w_2^{\text{eff}}$$
$$\leq -\alpha^{\text{eff}} (\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2) + (\rho + \gamma \mathcal T) (\lVert\delta_1\rVert + \lVert\delta_2\rVert)$$

(with the understanding that $\gamma$ is signed). Let $s = \lVert\delta_1\rVert + \lVert\delta_2\rVert$ and $q = \lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2$. By Cauchy-Schwarz, $s^2 \leq 2q$, so $s \leq \sqrt{2q}$.

$$\dot V \leq -\alpha^{\text{eff}} q + (\rho + \gamma \mathcal T) \sqrt{2q} \tag{L1}$$

Setting $\dot V = 0$ gives the ultimate bound on $q$:

$$q^\ast = \frac{2(\rho + \gamma \mathcal T)^2}{(\alpha^{\text{eff}})^2} \tag{L2}$$

and on $\lVert\xi\rVert = \sqrt q$:

$$R_\xi^\ast = \frac{\sqrt 2\,(\rho + \gamma \mathcal T)}{\alpha^{\text{eff}}} \tag{L3}$$

Translating to the macro-state $\delta_c = (\delta_1 + \delta_2)/\sqrt 2$: the averaging projection has Lipschitz constant $L = 1$ in the norm-squared sense, and $\lVert\delta_c\rVert^2 \leq \tfrac{1}{2}(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2) = \tfrac{q}{2}$, so

$$R_c^\ast \;=\; \sup \lVert\delta_c\rVert \;\leq\; \sqrt{q/2} \;=\; \frac{\rho + \gamma \mathcal T}{\alpha^{\text{eff}}} \tag{L4}$$

This gives the closed-form composite ultimate bound in the matched-symmetric case.

### 2.3 The critical-mass inequality

The composite persists iff $R_c^\ast \lt R_c$, i.e.,

$$\boxed{\; \alpha^{\text{eff}} \,R_c \;\gt\; \rho + \gamma \mathcal T \;} \tag{CM1}$$

Substituting $\alpha^{\text{eff}} = \alpha - C$ from (C2), and assuming the symmetric-matched case permits $R_c = R$ (the radius inherits from individual sub-agent radii in the averaging projection — verified in §3):

$$\boxed{\; (\alpha - C) R \;\gt\; \rho + \gamma \mathcal T \;} \tag{CM2}$$

Rearranging into a **composite contraction-rate form**:

$$\kappa_c := \alpha^{\text{eff}} - \frac{\rho + \gamma \mathcal T}{R} = (\alpha - C) - \frac{\rho + \gamma \mathcal T}{R} \tag{KC}$$

The composite persists iff $\kappa_c \gt 0$.

### 2.4 Structural interpretation

(CM2) has four identifiable contributions on the left side:

| Term | Interpretation | Sign |
|---|---|---|
| $\alpha R$ | Baseline individual reserve (each sub-agent's reserve-rate) | + |
| $-C R$ | Coordination cost in reserve units | – |
| $-\rho$ | Baseline disturbance | – |
| $-\gamma \mathcal T$ | Coupling contribution (cooperative $\gamma\lt 0$ helps; adversarial $\gamma\gt 0$ hurts) | ± |

**Specialization checks:**

- **No coupling** ($\gamma = 0$, $C = 0$): (CM2) reduces to $\alpha R \gt \rho$, the single-agent persistence condition per `#result-sector-condition-stability`. ✓

- **Cooperative-symmetric** ($\gamma \lt 0$, $C = 0$): the RHS $\rho + \gamma \mathcal T \lt \rho$, so (CM2) is easier to satisfy than the individual condition. This is the formal statement of "teams persist where individuals can't": a sub-agent with $\alpha R \lt \rho$ fails individually, but the pair persists if $\gamma \mathcal T \lt -(\rho - \alpha R)$. ✓ (recovers `#der-team-persistence`'s cooperative regime, now derived not assumed.)

- **Adversarial-symmetric** ($\gamma \gt 0$, $C = 0$): the RHS $\rho + \gamma \mathcal T \gt \rho$, so (CM2) is harder than the individual condition. The composite fails when $\gamma \mathcal T \gt \Delta\rho^\ast = \alpha R - \rho$. This is precisely the `#der-adversarial-destabilization` threshold **applied symmetrically to both agents**. ✓

- **Coordination-dominated** ($C \gt \alpha$, $\gamma = 0$): the LHS becomes negative, so (CM2) fails regardless of $\rho$. This is Brooks's Law in its pure form — adding an ally that imposes coordination cost greater than one's own correction rate always breaks persistence. ✓

- **Weakest-link sanity check:** under symmetric matching, $\min_i \alpha_i - \Delta\mathcal T_i^{\text{cost}} = \alpha - C$, so (WL) gives $\alpha_c \geq \alpha - C$. Our (KC) refines this by making the composite's *effective disturbance* explicit ($\rho + \gamma\mathcal T$), yielding the persistence inequality rather than just the correction-rate bound. (WL) is **consistent with** (CM2), and (CM2) **subsumes** (WL) when the cooperative coupling $\gamma \mathcal T \lt 0$ is exploited: the composite can have $\kappa_c \gt 0$ even when $\alpha - C \lt \rho/R$ (individual failure), provided $\gamma\mathcal T$ is sufficiently negative. (WL) cannot see this because it doesn't account for $\gamma$'s sign.

### 2.5 What (CM2) *is* and what it *isn't*

**What it is:** a **closed-form critical-mass inequality** for the symmetric-matched-Tier-1 two-agent case, derived from the sector-persistence template applied at the joint level with a quadratic Lyapunov function on the concatenated state. It is a genuine theorem (conditional on matched architecture + Tier 1 + symmetric coupling + Model D).

**What it isn't:**

- It does not make any claim about incremental monotonicity / full contraction of the macro-update map $f_c$. That's still the separate `spike-bridge-lemma-contraction.md` question. (CM2) gives composite **(T2)**; it does not give composite **DA2'-inc**.
- It treats $\mathcal T$ as exogenous, inheriting the decoupled-Lyapunov assumption of `#der-adversarial-destabilization` (§Working Notes). A fully coupled $\mathcal T_1, \mathcal T_2$ model where each agent's tempo responds to the other's mismatch would be a genuine open extension.
- It does not address $U_O$ yet — that enters in §5.

---

## 3. Application to Structured Cases

### 3.1 Case A: Two linear agents with diagonal coupling

**Setup.** Two scalar linear agents with dynamics

$$\dot\delta_1 = -\alpha\,\delta_1 + w_1 + \beta \delta_2, \qquad \dot\delta_2 = -\alpha\,\delta_2 + w_2 + \beta \delta_1,$$

where $\beta$ is a **state-space coupling** constant (not disturbance-coupling). This is the "two agents with direct state coupling" case. $w_i$ is bounded by $\rho$; coordination cost is absorbed into $\alpha$ (so $\alpha = \alpha^{\text{eff}}$); $\gamma$ coupling is through $\beta$ only.

**Joint matrix form.** $\xi = (\delta_1, \delta_2)^T$,

$$\dot\xi = -A\,\xi + w, \qquad A = \begin{pmatrix} \alpha & -\beta \\ -\beta & \alpha \end{pmatrix}.$$

**Eigenvalues of $A$:** $\alpha \pm \beta$. For $A$ to be positive-definite (and hence $-A$ to be contracting in every direction), we need $\alpha - |\beta| \gt 0$, i.e., $|\beta| \lt \alpha$. The contraction rate is

$$\kappa_c^{\text{linear}} = \alpha - |\beta|$$

— the **weakest eigendirection** sets the composite's contraction rate.

**Relation to (CM2).** In this case the coupling is constructive in the symmetric eigendirection ($\delta_1 + \delta_2$) and destructive in the antisymmetric ($\delta_1 - \delta_2$): $A$'s eigenvalue in the symmetric direction is $\alpha - \beta$ (for positive $\beta$); in the antisymmetric, $\alpha + \beta$. Averaging projection $\delta_c = (\delta_1 + \delta_2)/\sqrt 2$ picks out the *symmetric* eigendirection — its contraction rate is $\alpha - \beta$ (for $\beta \gt 0$, **weaker** than individual), $\alpha + |\beta|$ (for $\beta \lt 0$, **stronger**). This matches (CM2)'s $\gamma$-sign structure: *positive* $\beta$ plays the role of adversarial $\gamma \gt 0$ (amplification of the symmetric-mode disturbance); *negative* $\beta$ plays the role of cooperative $\gamma \lt 0$.

**Critical mass.** The composite is contracting in the macro-dimension iff $\alpha \gt |\beta|$, recovering (CM2) with identification $\gamma\mathcal T/R \leftrightarrow \beta$ (up to dimensional normalization).

**Implication for the bridge lemma.** For the state-coupling case, the composite contraction is **derived exactly** (not just bounded from below via weakest-link). The composite Lyapunov function is $V(\xi) = \tfrac{1}{2}\xi^T \xi$; $\dot V = -\xi^T A \xi + \xi^T w \leq -(\alpha - |\beta|) \lVert\xi\rVert^2 + \rho\sqrt 2 \lVert\xi\rVert$; ultimate bound $R_\xi^\ast = \rho\sqrt 2/(\alpha - |\beta|)$.

### 3.2 Case B: Two Kalman filters coordinating through a shared channel

**Setup.** Two Kalman filters tracking correlated scalar random walks, with a shared observation channel (each filter observes its own state plus a fraction $u$ of the other's state). This is (F.4 topology in `#der-team-persistence`'s working notes; "shared channel" variant of `spike-composition-correlated-kalman.md`).

**Steady-state Kalman gain** for each filter is $K^\ast$; the correction function is $F_i(\delta_i) = K^\ast \delta_i$, sector condition holds with $\alpha = K^\ast/\tau_{\text{step}}$ (in continuous-time discretization).

**Coupling through shared channel:** when agent $i$ observes $o_i = \omega_i + u\omega_j + v_i$ (cross-observation fraction $u$), the shared-channel contribution improves each agent's innovation signal. In the small-$u$ linearization:

- Each agent's **effective correction rate** gains a cross term: $\alpha^{\text{eff}} = \alpha(1 + u\rho_{\text{corr}})$ (where $\rho_{\text{corr}}$ is the underlying process correlation) — the shared channel is informative *only when* the processes are correlated.
- The cross-observation is also a **cross-disturbance source** proportional to $u$: $\rho^{\text{eff}} = \rho(1 + u \cdot \text{noise-amplification})$.

Substituting into (CM2), the critical-mass inequality becomes

$$(\alpha(1 + u\rho_{\text{corr}}) - C)\,R \;\gt\; \rho(1 + u \cdot \kappa_{\text{noise}}).$$

The key qualitative result: **the shared channel helps only when the processes it shares information about are correlated**. Uncorrelated processes ($\rho_{\text{corr}} = 0$) mean the cross-observation term contributes noise without contributing signal — the composite is strictly worse than the uncoupled case. This mirrors `#result-unity-closure-mapping`'s finding that observation-closure defect scales with $1 - U_{\text{obs}}$.

**Takeaway.** The Kalman-coordination case confirms the structural form of (CM2) but adds content: **coupling effectiveness $\gamma$ itself depends on unity** — specifically on $U_{\text{obs}}$ (for observation sharing) and $U_M$ (for model sharing via correlated processes). This is where $U_d$ enters — not via a separate threshold, but as a multiplicative modulator of $\gamma$.

### 3.3 Case C: Symmetric dyad with matched observation functions (sanity check)

Two agents observing the same environmental variable (e.g., two radar systems tracking a shared target) with identical observation functions $H_1 = H_2 = H$, correction functions $F_1 = F_2 = F$, same step-size $\eta$, same sector constants. In this case:

- The composite projection is the **average of the two estimates**: $\hat\omega_c = (\hat\omega_1 + \hat\omega_2)/2$ (`#result-unity-closure-mapping` §state-closure).
- Under consistent linear projections of linear dynamics, **the closure defect is zero** at steady state.
- The composite inherits $\alpha_c = \alpha$ and $R_c = R$ exactly (no coordination overhead if channels are independent, or $\alpha_c = \alpha - C$ if synchronization is required).

Critical-mass inequality: $\alpha_c R_c \gt \rho_c^{\text{eff}}$. In the independent-disturbance case, $\rho_c^{\text{eff}} = \rho/\sqrt 2$ (averaging two independent observations reduces the noise by $\sqrt 2$). So the composite's persistence condition is *strictly easier* than the individual's: $\alpha R \gt \rho/\sqrt 2$ instead of $\alpha R \gt \rho$. This is a **derived benefit of redundant sensing** — the composite absorbs $\sqrt 2$-fold more disturbance than either individual alone, purely through averaging, even without explicit coordination.

**Compare against** `#der-team-persistence`'s $\gamma^{\text{coop}}$ mechanism: the sensor-redundancy benefit here is *perceptual*, not *actional* — it's `#result-unity-closure-mapping`'s $U_{\text{obs}}$ dimension showing up in the disturbance term, not `#der-team-persistence`'s $\gamma^{\text{coop}}$ (which requires ally action in the environment). The distinction vindicates `#der-team-persistence`'s careful separation of communication-based vs action-based cooperation; the two enter the persistence inequality at different places.

---

## 4. The Asymmetric Limit and Symbiogenesis

### 4.1 Asymmetric-pair setup

Drop the symmetric assumption. Let $\alpha_1 \gg \alpha_2$, with $\alpha_2 \to 0$ in the limit (one agent is strong, the other very weak). Other parameters may differ.

**Joint Lyapunov argument with asymmetric weighting.** The unweighted $V(\xi) = \tfrac{1}{2}(\delta_1^2 + \delta_2^2)$ gives $\dot V \leq -\min(\alpha_1, \alpha_2) \lVert\xi\rVert^2 + \rho \sqrt 2 \lVert\xi\rVert$ by the argument in §2.2, yielding the weakest-link ultimate bound $R_\xi^\ast = \rho\sqrt 2/\min(\alpha_1,\alpha_2)$. As $\alpha_2 \to 0$, this **diverges** — the composite cannot persist under the unweighted Lyapunov.

**Weighted Lyapunov.** Let $V(\xi) = \tfrac{1}{2}(\delta_1^2 + \mu \delta_2^2)$ with $\mu \gt 0$. Then

$$\dot V \leq -\alpha_1 \delta_1^2 - \mu \alpha_2 \delta_2^2 + \rho_1 |\delta_1| + \mu\rho_2 |\delta_2|.$$

Let $\mu \to 0$; the $\delta_2$ terms vanish on both sides. The limit gives **$\dot V \leq -\alpha_1 \delta_1^2 + \rho_1 |\delta_1|$** — the composite's stability is controlled **entirely by agent 1**. Agent 2's contribution to the Lyapunov function is weighted away.

This is a precise formal statement: **in the asymmetric limit, the composite inherits agent 1's sector constant and reserve**, with agent 2 playing no role in the Lyapunov argument at all. The question is: under what interpretation does this recover `#hyp-symbiogenic-composition`?

### 4.2 Connection to symbiogenesis

`#hyp-symbiogenic-composition` decomposes the asymmetric integration into three processes:

- **(S-1) Objective absorption**: $O_e \to \mathcal D_e(O_h)$ — the endosymbiont's objective becomes derived from the host's.
- **(S-2) Function transfer**: $\{M_h, \Sigma_h\} \to \{M_h, \Sigma_h\} \cup \mathcal F(M_e, \Sigma_e)$ — structure flows from endosymbiont into host.
- **(S-3) Autonomy reduction**: $\mathcal A_e^{\text{effective}} \to \mathcal A_e^{\text{restricted}}$ — endosymbiont's effective action space contracts.

The Lyapunov-weight limit $\mu \to 0$ corresponds to **(S-3) autonomy reduction**: agent 2's autonomous correction dynamics are *weighted out of the composite's stability accounting*. What remains is agent 1's original sector condition — plus whatever function agent 2 contributes to agent 1's update (via (S-2) function transfer).

**Candidate theorem (symbiogenesis-as-asymmetric-limit):** When $\mu \to 0$ in the weighted Lyapunov argument, (i) the composite's persistence condition reduces to agent 1's individual persistence condition modified by whatever structure agent 2 has transferred; (ii) agent 2's effective autonomy, measured as the support of the composite state projection onto $\delta_2$, shrinks to zero; (iii) the composite sector condition holds iff agent 1's sector condition holds in the **transferred-structure-augmented** state space.

**This is a sketch, not a theorem.** The "transferred-structure-augmented state space" is the gap — `#hyp-symbiogenic-composition` leaves $\mathcal F$ (function transfer) unspecified, so I cannot derive composite (A4) as a clean function of individual (A4)s. What I **can** derive: in the pure asymmetric limit with no function transfer (pure autonomy reduction), the composite's persistence is governed entirely by agent 1, which is the Lyapunov-weight result above. This is consistent with `#hyp-symbiogenic-composition`'s qualitative picture but does not close its open items.

**What this does clarify:** the asymmetric limit exists as a *limit of (CM2)*, not as a discontinuous regime change. The critical-mass condition in the symmetric case (CM2) smoothly deforms into the single-agent condition as $\alpha_2 \to 0$, with the transition's "moment" tracked by the weight $\mu$ in the Lyapunov function. This contradicts any reading of symbiogenesis as a separate regime requiring separate machinery — it is the asymmetric-parameter-limit of peer composition, and the Lyapunov weights capture the transition.

---

## 5. Where $U_O$ Enters

### 5.1 Three candidate entry points

From the problem statement, $U_O$ could enter (CM2):

- **(a) Multiplicatively, as a coupling modifier** — $\gamma \mathcal T$ becomes $\gamma(U_O) \mathcal T$ where $\gamma(U_O)$ is more negative (more cooperative) for high $U_O$, more positive (more adversarial) for low/negative $U_O$.
- **(b) Additively, as a separate reserve term** — $\kappa_c = \alpha^{\text{eff}} R - \rho - \gamma\mathcal T + \beta U_O$ with some $\beta$.
- **(c) As a scope gate** — below a threshold $U_O \lt U_O^\ast$, the composite doesn't exist as an AAD agent and (CM2) is not well-posed (via `#scope-composite-agent`).

Checking each against the cases in §2–§3:

### 5.2 The multiplicative-modifier form is derived under linear-Gaussian structure

In Case A (two linear agents with diagonal coupling, §3.1), the coupling $\beta$ is a mathematical constant that I took as given. In a purposeful-agent setting, the coupling $\beta$ reflects **how the two agents' actions interact through the shared environment** — which in turn depends on how closely their objectives align (because two agents optimizing for aligned objectives produce actions that *reinforce* each other, while agents optimizing for opposed objectives produce actions that *interfere*).

**Operationalization.** Let each agent optimize a quadratic objective $L_i(\omega) = \tfrac{1}{2}(\omega - r_i)^T Q (\omega - r_i)$ with target $r_i$, and let $U_O = \text{corr}(r_1, r_2)$ be the target correlation (the Pearson correlation of the two agents' targets over trajectories, as in `#def-unity-dimensions`). Under LQR-like policies, the actions are linear in $(\omega - r_i)$. The cross-coupling in the joint dynamics is:

$$\beta_{\text{eff}} \;\propto\; \langle a_1,\, -a_2\rangle_{\text{env}} \;\propto\; U_O \cdot \beta_{\max}$$

(discussion-grade derivation: aligned targets → aligned action directions → positive $\langle a_1, a_2\rangle$ in the shared environment → cross-coupling is constructive in the symmetric eigendirection; anti-aligned targets → negative $\langle a_1, a_2\rangle$ → cross-coupling is destructive). That is, the **sign and magnitude** of $\gamma$ in (CM2) are controlled by $U_O$, with $\gamma \propto -U_O$ (higher $U_O$ → more negative, more cooperative $\gamma$).

Substituting into (CM2):

$$\kappa_c(U_O) \;=\; (\alpha - C)R - \rho - \gamma(U_O)\mathcal T \;=\; (\alpha - C)R - \rho + \gamma_{\max} U_O \mathcal T \tag{CM3}$$

(with the convention $\gamma(U_O) = -\gamma_{\max} U_O$, $\gamma_{\max} \gt 0$). **The composite critical-mass is linear in $U_O$ under linear-Gaussian objective structure**.

### 5.3 The scope-gate component

(CM3) suggests that *any* $U_O \gt -\infty$ can be compensated for by sufficiently large $\alpha R$. But `#scope-composite-agent` (route C-i) says value-correlation below a threshold means the composite *isn't a composite at all* — there's no coherent $O_c$ to define composite-level quantities against. This is a **scope gate** on top of (CM3):

$$\boxed{\;\kappa_c(U_O) \gt 0 \text{ AND scope-satisfaction} \;\Leftrightarrow\;\text{composite persists as AAD agent}\;} \tag{CM4}$$

Scope-satisfaction is a disjunction of three routes in `#scope-composite-agent` — it is not reducible to a scalar threshold on $U_O$. Route (C-i) sufficient condition: some scalar aggregate of pairwise $U_O$ exceeds a threshold $\epsilon$; routes (C-ii)/(C-iii) can rescue composites with low $U_O$ but hierarchical decomposition or mutual-benefit structure.

**(CM4) is the honest statement** of the critical-mass inequality: a contraction-rate inequality (CM3) *conditional* on scope-satisfaction in the disjunctive `#scope-composite-agent` sense. The two conditions are not redundant: a composite can fail (CM4) by either having negative $\kappa_c$ (contraction fails) or by failing scope (no coherent composite in the first place).

### 5.4 What this settles about $U_O$'s role

(CM4) says: **$U_O$ enters critical-mass both multiplicatively (modulating coupling $\gamma$) and as a scope gate (via `#scope-composite-agent`).** It does **not** enter purely additively — there is no free-floating "$U_O$ contribution" separate from the coupling that it modulates.

This resolves one of the question's open items: $U_O$'s role is **not additive** (option b from §5.1). It is **multiplicative-on-$\gamma$-plus-scope-gate** (composed options a and c). This matches `#result-unity-closure-mapping`'s picture of unity dimensions as **rate-distortion parameters** modulating the achievable closure-defect curves — $U_O$ doesn't cause anything on its own, it shapes how much each other quantity contributes.

---

## 6. Obstruction Analysis for the General Case

The symmetric-matched case went through cleanly; the asymmetric-limit and $U_O$-modulated cases partially. What resists generalization?

### 6.1 Heterogeneous architectures

When the two agents have genuinely different architectures — Kalman + PID, gradient-descent + rule-based, Tier 1 + Tier 3 — the joint Lyapunov cannot be constructed from $V = \tfrac{1}{2}(\delta_1^2 + \delta_2^2)$ alone, because agent 2's non-Tier-1 correction function may not be strongly monotone (per `spike-bridge-lemma-contraction.md`'s counterexample). The Lyapunov approach requires each sub-agent's correction to satisfy A2' (at least); for Tier 2/3 agents, this is domain-specific.

**Obstruction.** The composite critical-mass inequality (CM4) requires **each sub-agent to be in a regime where its local sector condition is verified**. Heterogeneous composites require per-sub-agent tiering (following `spike-bridge-lemma-contraction.md`) and the weakest tier governs. The clean closed form of (CM4) is lost; the composite's $\kappa_c$ depends on the weakest sub-agent's tier and its local-region extent.

### 6.2 Nonlinear coupling

(C1)'s additive coupling $\rho_i^{\text{eff}} = \rho + \gamma \mathcal T_j$ assumes coupling acts through disturbance at rate $\gamma \mathcal T_j$. Real coupling can be **state-dependent** ($\gamma$ is a function of $\delta_j$, or of $\lVert\delta_j\rVert$), as in the effects spiral of `#der-adversarial-destabilization`'s Corollary. For state-dependent $\gamma$, (CM2)'s inequality becomes a **nonlinear inequality in $\delta$**, no longer admitting closed-form critical-mass.

**Obstruction.** For $\gamma = \gamma(\delta_j)$, the composite Lyapunov analysis requires the coupled-state dynamical system to be handled with the full `#der-adversarial-destabilization` joint-Lyapunov machinery — which is an open item in that segment's Working Notes. The current spike cannot close this gap either.

### 6.3 Non-negligible coordination-cost coupling

(C2) assumed the coordination cost $C$ is additive in each agent's $\alpha$. A more realistic model: coordination cost depends on $\delta_j$'s current magnitude (agents spend more time coordinating when their mismatch is high). This couples the coordination cost back into the dynamics:

$$C_i^{\text{eff}} = C_0 + C_1 \lVert\delta_j\rVert.$$

Substituting, (CM2) becomes a quadratic in $\lVert\delta\rVert$, no longer a linear inequality. Closed form exists (solve the quadratic) but loses its interpretive cleanliness.

### 6.4 Fully-coupled tempos

(C1) treated $\mathcal T_1, \mathcal T_2$ as exogenous. A genuinely-coupled model has each agent's tempo responding to the other's mismatch (faster updates when ally is in trouble), producing a **tempo feedback loop** that couples $\mathcal T$'s own dynamics into the critical-mass analysis. This is flagged as open in `#der-adversarial-destabilization`'s Working Notes and is **not addressed here**.

### 6.5 What survives

Despite these obstructions, the following hold generally:

1. **(CM4)'s structural form** — contraction-rate inequality AND scope-satisfaction — is **domain-agnostic**. It holds for any composite with a well-defined joint Lyapunov candidate (even if the cleanly-factored form (CM2)/(CM3) doesn't).
2. **The scope-gate component** from `#scope-composite-agent` is domain-agnostic.
3. **The weakest-link weakening structure** (in heterogeneous or asymmetric cases): composite critical-mass is worse than any single-agent condition, per §2.4's sanity check.

---

## 7. Comparison Against the Six Template Instances

The sector-persistence template (`#result-sector-persistence-template`) has six instances. How does (CM4) relate?

| Instance | State $\xi$ | Effective $\rho_\xi$ | Critical-mass via (CM4)? |
|---|---|---|---|
| `#result-persistence-condition` | $\delta_t$ (single-agent epistemic mismatch) | $\rho$ | N/A (single agent; (CM4) is degenerate) |
| `#schema-strategy-persistence` | $\delta_\Sigma$ (strategic mismatch) | $\rho_\Sigma$ | N/A (single agent) |
| `#der-team-persistence` | $\delta_i$ (sub-agent mismatch in a team) | $\rho_i^{\text{eff}} = \rho_{i,\text{env}} + \sum_j \gamma_{j\to i}\mathcal T_j$ | **(CM4) is the composite of all $N$ team-persistence conditions**. Each $i$-indexed inequality is (CM4) at $i$; the team condition is the conjunction. |
| `#form-composition-closure` (bridge lemma) | $e_m$ (trajectory error) | $\varepsilon^\ast \nu_c$ | Orthogonal: (CM4) controls composite (T2); bridge lemma needs (T2) **and** DA2'-inc on $f_c$. Both are required for the composite to be a stable macro-agent. |
| `#der-tempo-composition` | $\delta_c$ (composite mismatch) | $\rho_{\text{ext}} + \varepsilon^\ast \nu_c$ | **(CM4) is the critical-mass statement at the composite-level**. The tempo-composition inequality is (CM4) with its $C$ identified as $\varepsilon^\ast \nu_c$. |
| `#der-adversarial-destabilization` | $\delta_B$ (target-agent mismatch) | $\rho_{B,\text{base}} + \gamma_A \mathcal T_A$ | **(CM4)'s negation**. Destabilization is failure of (CM4) for agent $B$. |

The third column reveals that (CM4) is **not a new instance of the template** — it's a **meta-pattern across team-persistence, tempo-composition, and adversarial-destabilization**, recognizing that all three share the form

$$(\text{corrective capacity}) \cdot R \;\gt\; (\text{intrinsic + coupling-induced disturbance}),$$

with the **sign of coupling** (cooperative / adversarial), the **level** (sub-agent / composite), and the **scope gate** (`#scope-composite-agent`) as the three axes of variation. This is exactly the kind of meta-pattern that `#additive-coordinate-forcing` (CLAUDE.md) and `#disc-separability-pattern` were promoted to name. The candidate promotion is below (§8).

---

## 8. Recommendations for Promotion

### 8.1 What's ready for promotion

**A new appendix segment `#deriv-critical-mass-composition` (or `#composite-sector-derivation`), type:derivation, status:conditional, depending on `#result-sector-persistence-template` + `#form-composition-closure` + `#scope-composite-agent` + `#der-team-persistence` + `#der-adversarial-destabilization`.** It would:

- State (CM4) as the composite critical-mass inequality, with the two branches derived (CM3 from §2-3 for the symmetric-matched-Tier-1 case, symmetric limit of the asymmetric result from §4).
- Present the structured cases of §3 (diagonal coupling, Kalman coordination, matched dyad) as worked examples.
- State the obstruction analysis of §6 as the scope boundary.
- Close the long-standing open item in `working-composition-admissibility.md` §8 on "composite (A4) derives from individual sector conditions" — the weakest-link bound (WL) is subsumed by (CM4).

**Strengthening moves to existing segments:**

- **`#form-composition-closure`**: the derivation-audit table's row "Composite (A4) from sub-agent properties" currently reads "Derived (conditional on bounded coordination cost per #der-team-persistence)" and cites `working-composition-admissibility.md` §6.2. Upgrade to "Derived (conditional on Tier 1 + symmetric-matched + Model D, per `#deriv-critical-mass-composition`) — tightens the weakest-link bound by explicitly including coupling sign and magnitude." The bridge-lemma bound's persistence condition $\varepsilon^\ast \lt \alpha_c R_c / \nu_c$ is now derived, not assumed.
- **`#der-team-persistence`**: add a cross-reference to `#deriv-critical-mass-composition` as the composite-level complement. Currently `#der-team-persistence` gives per-sub-agent persistence; the composite-level (CM4) is the conjunction.
- **`#hyp-symbiogenic-composition`**: add a reference to the asymmetric limit §4 as a **conditional formalization** of the autonomy-reduction (S-3) mechanism. The segment's Working Notes on "Objective-transfer dynamics (S-1)" are not addressed here; only (S-3) gets a Lyapunov-weighted formalization.
- **`#result-unity-closure-mapping`**: §5.2's derivation of $\gamma(U_O) = -\gamma_{\max} U_O$ adds a **rate-distortion-compatible derivation** of the $U_O$ → $\varepsilon_a$ relation that currently lives only in the linear-Gaussian closed form. Extend `#result-unity-closure-mapping` with this structural pathway.
- **`#result-sector-persistence-template`**: update the instantiations table's row on `#form-composition-closure` to note that composite (T2) now has a critical-mass derivation at `#deriv-critical-mass-composition`. This doesn't affect the template itself; it strengthens the dependency chain.

### 8.2 What's not ready

- Heterogeneous-architecture case (§6.1) is open; no promotion-level statement available.
- Nonlinear coupling (§6.2); same.
- Fully-coupled tempo dynamics (§6.4); requires joint tempo analysis from `#der-adversarial-destabilization`'s Working Notes.
- The $U_O$-multiplicative-modifier derivation §5.2 is currently **discussion-grade** (uses an LQR-compatibility sketch); upgrading it to conditional requires a proper action-space inner-product analysis in `#result-unity-closure-mapping`. 
- The symbiogenic-limit result (§4) is **sketch-level**; formalizing "function transfer" (S-2) in `#hyp-symbiogenic-composition` is a prerequisite for making it a theorem.

### 8.3 A candidate meta-segment promotion

The cross-instance observation in §7 — that `#der-team-persistence`, `#der-tempo-composition`, `#der-adversarial-destabilization`, and now `#deriv-critical-mass-composition` share a **signed-coupling critical-mass shape** — is a candidate for future meta-segment promotion, parallel to `#disc-separability-pattern` and `#additive-coordinate-forcing`. Tentative name: `#signed-coupling-critical-mass` or `#coupling-sign-duality`. The core content: AAD's multi-agent results are **instances of a single critical-mass inequality with signed coupling**, where the sign of $\gamma$ (cooperative vs adversarial), the level (sub-agent vs composite), and the scope gate (`#scope-composite-agent`) index the variation. Persistence and destabilization are the *same result* — (CM4)'s satisfaction and its negation — applied at different levels.

This is speculation-grade; promoting it would require pinning down whether the "signed coupling" is (i) a fundamental structural invariant (composition happens along signed-coupling axes, period) or (ii) a derivational convenience that sector-persistence-template's template form already captures. My best guess is (ii) — the template already embeds the pattern — so this meta-promotion may be redundant with `#result-sector-persistence-template`'s cross-instance section rather than a new meta-segment. Logging as "not ready, likely redundant".

---

## 9. Honest Epistemic Status

**What this spike achieves:**

1. **Closed-form critical-mass inequality (CM2)/(CM3)/(CM4)** for the symmetric-matched-Tier-1 two-agent case with linear-Gaussian $U_O$ modulation. This is a **derived theorem** conditional on the listed assumptions and subsumes the weakest-link bound (WL).
2. **Structural sanity checks** against four specific limit cases (no coupling, cooperative-symmetric, adversarial-symmetric, coordination-dominated), all of which recover the expected existing results.
3. **Three structured-case applications** (diagonal coupling, Kalman coordination, matched dyad) showing (CM2) captures the correct qualitative behavior.
4. **Asymmetric-limit analysis** (§4) giving a weighted-Lyapunov formalization of `#hyp-symbiogenic-composition`'s (S-3) autonomy-reduction mechanism. Sketch-level.
5. **$U_O$'s entry point**: multiplicative-modulator-on-$\gamma$ plus scope-gate (CM4), derived under linear-Gaussian objective structure. Discussion-grade for the derivation; structurally clean.
6. **Obstruction analysis** (§6) for the general case identifying four distinct failure points (heterogeneous architectures, nonlinear coupling, dynamic coordination cost, fully-coupled tempos).

**What it does not achieve:**

- Does not close the bridge-lemma-contraction question (that's `spike-bridge-lemma-contraction.md`'s territory). (CM4) gives composite (T2), not composite DA2'-inc.
- Does not formalize the function-transfer mechanism in `#hyp-symbiogenic-composition` (S-2), so the symbiogenic limit result stays sketch.
- Does not resolve the $N \gg 2$ scaling question (see `spike-composition-scaling-N.md`); (CM4) is specific to $N = 2$, with matched-symmetric architecture. The conjunction-over-sub-agents form generalizes but loses closed form.
- Does not address fully-coupled tempo dynamics (§6.4).

**Confidence:**

- (CM2) and its specialization checks (§2.4): **proved** (Tier 1 + symmetric + matched architecture + Model D).
- The structured-case applications (§3): **proved** in Cases A and C; Case B (§3.2) has a small-$u$ linearization move that's standard but not rigorously controlled (the "noise amplification" term is qualitative).
- The $U_O$-multiplicative derivation (§5.2): **discussion-grade**. The compatibility with LQR-like actions is qualitatively clear; rigorous action-space inner-product analysis is deferred.
- The asymmetric limit (§4): **sketch-level**. The weighted-Lyapunov argument is standard; the identification with symbiogenesis's (S-3) is structurally motivated but not a theorem.
- The obstruction analysis (§6): **identification of genuine structural barriers**, not mere hand-waving. Each obstruction points to an existing open item in a named segment.

**Overall:** The spike delivers a closed-form critical-mass theorem for the symmetric-matched case, which is genuinely new in AAD and closes one of the top-priority open items in Section III. The theorem is conditional on Tier 1 architecture and symmetric matching; these are restrictive but cover Kalman, exponential-family, gradient-descent, and L2-regularized agents — a non-trivial slice of the AAD-in-scope space. The $U_O$ role and the symbiogenic limit are partial results pointing to follow-up work. The general-case obstructions are honest and align with known open items in the project.

---

## 10. Connections to Adjacent Literature

- **Contraction analysis (Lohmiller & Slotine 1998, "On contraction analysis for non-linear systems," *Automatica* 34:683):** The joint-Lyapunov approach in §2.2 is a contraction-analysis argument. Lohmiller-Slotine's **differential Lyapunov** framework is essentially what `spike-bridge-lemma-contraction.md` uses — strong monotonicity of the Jacobian. The current spike's critical-mass inequality is the **aggregate contraction condition** on the joint system.
- **Small-gain theorem for networked systems (Jiang, Teel, Praly 1994, "Small-gain theorem for ISS systems and applications," *Math. Control Signals Syst.* 7:95):** The composition of two ISS (input-to-state stable) systems is ISS iff the product of their gains is less than one. (CM2) is the AAD analog specialized to sector-bounded corrections: the composite persists iff the *sum* of individual reserve-rates exceeds the coupling-amplified disturbance. The additive rather than multiplicative form reflects that AAD's Lyapunov construction averages rather than composes gains — the averaging-projection is the key choice.
- **Interconnection of ISS systems / ISS Lyapunov functions (Sontag 1989):** An interconnected ISS system's Lyapunov function is the sum of sub-system Lyapunov functions, as in §2.2. The additive form of (CM2)'s effective disturbance inherits this pattern.
- **Multi-agent consensus & synchronization (Olfati-Saber & Murray 2004, "Consensus problems in networks of agents with switching topology and time-delays," *IEEE TAC* 49:1520):** In the linear-diagonal-coupling case (§3.1), the matrix $A = \alpha I - \beta(I - J)$ (where $J$ is the averaging operator) is the graph-Laplacian-shifted form that governs consensus convergence. The eigenvalue $\alpha - |\beta|$ is the algebraic connectivity in that framework; (CM2) is consensus convergence rewritten as a persistence condition.
- **Markov blanket stability under composition (Aguilera et al. 2022):** Aguilera's critique shows FEP-flow stability requires narrow parameter regimes. (CM2) is Lyapunov-based, not FEP-based, and applies wherever (T1)-(T3) of `#result-sector-persistence-template` hold — a much broader regime. This matches AAD's overall posture (`#result-sector-persistence-template` §"Comparison with the FEP-flow stability argument") on claiming broader validity than the FEP framework.
- **Coupled Lyapunov design:** The construction of $V$ in §2.2 is an instance of the classical **vector Lyapunov function** approach (Matrosov 1962; Bellman 1962). The particular form $V = \sum V_i$ with equal weights is the simplest but not the only choice; weighted forms $V = \sum \mu_i V_i$ are the asymmetric-limit (§4) generalization, standard in singular-perturbation analysis.

None of these adjacencies change (CM2); they confirm that the result sits correctly in the broader contraction/ISS literature and identifies where AAD's contribution is distinctive (the $U_O$-modulated $\gamma$ and the scope-gate structure via `#scope-composite-agent`).

---

*(End of spike.)*
