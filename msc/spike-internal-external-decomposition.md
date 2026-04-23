# Spike: Internal-External Decomposition of Agent Viability

*Started 2026-04-22. Research spike. Not canon.*

## 1. The diagnostic problem

An AAD agent persists. Mismatch is bounded; the persistence condition holds. Someone asks: is this agent *good*, or is its *environment easy*?

The question has real consequences. "This team is shipping" might reflect a strong team or an easy codebase — and the correct intervention (expand scope / rotate people through) depends on which. "This Kalman filter is tracking" might reflect a well-tuned filter or a benign signal. "This autonomous car isn't crashing" might reflect good perception or an over-engineered test route. Attributing performance to the wrong side produces wrong interventions.

The standard result AAD offers is the **persistence condition** ( #persistence-condition):

$$\alpha \gt \frac{\rho}{\lVert\delta_{\text{critical}}\rVert}$$

(Model D, linearized form.) The left-hand side is the agent's correction capacity; the right-hand side is the environment's demand. Persistence is the *inequality*, a single scalar relation. But the question "how much of the margin is agent capacity vs. environmental leniency?" asks us to attribute the *margin itself* to its two sides.

Adjacent but not identical: **mismatch decomposition** ( #mismatch-decomposition) splits *this instant's mismatch* into reducible model error plus irreducible observation noise. That's a decomposition of *one signal* into *one agent property* and *one channel property*. What we want is a decomposition of *the persistence margin* (a quantity that integrates across time) into *all* the agent-side properties vs. *all* the environment-side properties.

This spike develops that decomposition.

## 2. Candidate target quantities

Before deriving anything, name the quantity being decomposed. Four candidates exist; each gives a different decomposition.

**Candidate (a): the persistence margin itself.**

$$\Pi = \alpha - \frac{\rho}{\lVert\delta_{\text{critical}}\rVert}$$

"How far above the threshold is the agent?" Sign matters (persists / fails); magnitude gives cushion. This is the most direct operational quantity.

**Candidate (b): the adaptive reserve.**

$$\Delta\rho^\ast = \alpha R - \rho$$

"How much *additional* disturbance can the agent absorb before the sector condition breaks?" From #sector-condition-stability. Structural rather than task-oriented.

**Candidate (c): the steady-state mismatch.**

$$R^\ast = \frac{\rho}{\alpha} \quad \text{(Model D)}, \qquad R^\ast_S = \sigma_w\sqrt{\frac{n}{2\alpha}} \quad \text{(Model S)}$$

"How badly wrong is the agent, on average?" The smaller, the better. This is a *ratio* quantity; its logarithm will split additively.

**Candidate (d): the tempo ratio.**

$$\mathcal{T} / \rho$$

"How many units of correction per unit of disturbance?" A dimensionless capacity-to-demand ratio that matches the dimensional structure of the persistence condition.

Each candidate admits a decomposition, but the shapes differ. Candidate (a) is additive in agent-side and environment-side *thresholds*, which does not cleanly factor into separate components. Candidate (b) is similarly additive on one side and multiplicative on the other. Candidate (c), by contrast, is a *ratio of an environment quantity to an agent quantity*, and its logarithm is an *additive decomposition of log-viability into a sum*. Candidate (d) is the inverse of (c).

**The spike's target quantity.** I adopt **log-viability**

$$\mathcal{V} = \log \frac{\lVert\delta_{\text{critical}}\rVert}{R^\ast} = \log \lVert\delta_{\text{critical}}\rVert - \log R^\ast$$

as the target. This has three properties that make it the natural choice:

1. $\mathcal V \gt 0$ is exactly the task-adequacy condition $R^\ast \lt \lVert\delta_{\text{critical}}\rVert$ (see #persistence-condition).
2. $\log R^\ast = \log \rho - \log \alpha$ (Model D) is a *difference* of an environment term and an agent term, so $\mathcal V$ splits additively into four terms: domain-generosity, environment-benignity, agent-capacity, and task-toughness.
3. The logarithmic coordinate is AAD's natural scale for quantities built from independent factors (cf. #additive-coordinate-forcing). It is not *forced* by a Cauchy functional equation here — viability has no chain-rule-like compositionality axiom to invoke — so $\mathcal{V}$ is an *adjacent family member*, matched to the three anchors rather than derived by one. This is the honest characterization.

Under Model D:

$$\mathcal{V} \;=\; \underbrace{\log \lVert\delta_{\text{critical}}\rVert}_{\text{task-toughness (inverse)}} \;-\; \underbrace{\log \rho}_{\text{environment-demand}} \;+\; \underbrace{\log \alpha}_{\text{agent-capacity}}$$

Under Model S:

$$\mathcal{V}_S \;=\; \log \lVert\delta_{\text{critical}}\rVert - \log \sigma_w - \tfrac12 \log(n/2) + \tfrac12 \log \alpha$$

The Model-S form has $\tfrac12 \log \alpha$ rather than $\log \alpha$, reflecting the $1/\sqrt\alpha$ scaling of noise vs. $1/\alpha$ for drift. The log-capacity coefficient is regime-dependent; the additive structure is regime-invariant.

## 3. Where do $\alpha$ and $\rho$ come from?

The first decomposition ($\mathcal V = $ capacity $-$ demand $+$ task) is coarse. It separates agent from environment but doesn't touch the internal vs. external question within $\alpha$ and $\rho$. Both terms carry further structure.

### 3.1 Agent-capacity factor $\alpha$

Section I derives $\alpha$ as the sector-condition lower bound ( #sector-condition-stability, #gain-sector-bridge). For gain-based agents with directional fidelity (the sub-scope α partition per the 2026-04-22/23 A2' spike):

$$\alpha = \eta^\ast \cdot c_{\min}$$

where $\eta^\ast$ is the optimal update gain and $c_{\min}$ is worst-case directional fidelity of the correction map. For the linear Kalman/Beta-Bernoulli case $\alpha = \mathcal T = \nu \cdot \eta^\ast$.

Continuing the decomposition:

$$\alpha = \nu \cdot \eta^\ast \cdot c_{\min}$$

with

$$\eta^\ast = \frac{U_M}{U_M + U_o}$$

(from #update-gain).

Now the question: which of $\nu, \eta^\ast, c_{\min}$ are internal-to-the-agent vs. set-by-the-environment?

**$\nu$ (event rate).** Partially internal, partially external. The agent can decide to poll more often, run more tests, check more channels — but only up to the rate the environment emits events. In a low-traffic production system, $\nu$ is capped by the environment; in a heavily instrumented test loop, $\nu$ is agent-determined.

**$\eta^\ast$.** Jointly determined. $U_M$ is agent-internal (model uncertainty is a property of the model class and data history). $U_o$ is channel-property — *mostly* external, but per #software-epistemic-properties P6, agents can modify their own observation quality over long timescales by restructuring the environment. For the instantaneous decomposition, treat $U_o$ as external; for the long-run decomposition, acknowledge that $U_o$ at time $t$ depends on agent actions at $s \lt t$.

**$c_{\min}$.** Structural property of the correction function and the loss landscape. For gradient descent on a strongly convex loss, $c_{\min}$ is the strong-convexity modulus — a *joint* property of the model class (agent) and the loss surface induced by the environment. It is not cleanly one-sided.

**Working split.**

$$\alpha \;=\; \underbrace{\nu}_{\text{loop-speed (mixed)}} \;\cdot\; \underbrace{\frac{U_M}{U_M + U_o}}_{\text{gain (mixed)}} \;\cdot\; \underbrace{c_{\min}}_{\text{directional-fidelity (mixed)}}$$

Every factor is "mixed." This is the first warning signal: $\alpha$ is not an agent-only quantity. It's a *coupling property* of the agent-environment pair.

### 3.2 Environment-demand factor $\rho$

$\rho$ is the environmental disturbance rate ( #mismatch-dynamics). Naively external. But:

**Disturbance is model-relative.** $\rho$ measures the rate at which *unpredicted* change is injected — the magnitude of what the model fails to anticipate. A richer model predicts more of the environment's change, so $\rho$-as-measured depends on $M_t$'s expressiveness. This is the model-class-fitness connection ( #model-class-fitness): $\rho \mid \mathcal{M}$ can be much larger than $\rho \mid \mathcal{M}'$ for a richer $\mathcal{M}'$.

**Disturbance is action-policy-relative.** In an interactive setting, the distribution over $\Omega_{t+1}$ depends on $a_t$. If the agent chooses actions that keep the environment in a benign region (a racing car that doesn't corner hard, a trader who avoids volatile assets), the *observed* $\rho$ underestimates the environment's *potential* $\rho$ under a more exploratory policy. This is the `#loop-interventional-access` feedback — by choosing $a_t$, the agent chooses *which* $\rho$ it faces.

**Working split.**

$$\rho \;=\; \underbrace{\rho_{\text{external}}}_{\text{environment-volatility (pure external)}} \;\cdot\; \underbrace{f(\mathcal{M})}_{\text{model-class-expressiveness (agent)}} \;\cdot\; \underbrace{g(\pi)}_{\text{policy-benignity (agent)}}$$

where $f(\mathcal{M}) \leq 1$ (richer model predicts more, reducing effective $\rho$) and $g(\pi) \leq 1$ (conservative policy keeps environment in benign region). A maximally-expressive model with a maximally-conservative policy achieves $\rho = \rho_{\text{external}} \cdot \min_{\mathcal{M}, \pi} fg$. The *pure external* $\rho_{\text{external}}$ is the asymptote — "how hard can this environment hit me if I don't do anything clever about it?"

On log-scale (the natural coordinate, per §2):

$$\log \rho = \log \rho_{\text{external}} + \log f(\mathcal{M}) + \log g(\pi)$$

with $\log f, \log g \leq 0$. Every agent-side choice reduces log-$\rho$ below a log-ceiling set by the environment.

### 3.3 Task-toughness factor $\lVert\delta_{\text{critical}}\rVert$

Mostly external — set by the domain (how wrong can the agent be before its actions become harmful?). But:

**Task-toughness is objective-conditional.** $\lVert\delta_{\text{critical}}\rVert$ depends on what the agent is trying to do. A stricter objective (tighter safety constraint, higher-quality output) lowers $\lVert\delta_{\text{critical}}\rVert$. An agent choosing to take on a harder job is choosing a smaller $\lVert\delta_{\text{critical}}\rVert$.

**Task-toughness is action-space-conditional.** An agent with a richer action space can sometimes compensate for higher mismatch — "the model is off by 10% but I can route around it." This means $\lVert\delta_{\text{critical}}\rVert$ is larger for richer action spaces.

**Working split.**

$$\lVert\delta_{\text{critical}}\rVert \;=\; \underbrace{\lVert\delta_{\text{critical}}^{\text{domain}}\rVert}_{\text{domain-intrinsic}} \;\cdot\; \underbrace{h(O_t)}_{\text{objective-chosen-ambition}}$$

with $h(O_t)$ reflecting the chosen objective's ambition (tighter objective → smaller $h$).

## 4. The full decomposition

Assembling §§3.1–3.3 into log-viability $\mathcal V$, under Model D:

$$
\begin{aligned}
\mathcal{V} \;=\;& \log \lVert\delta_{\text{critical}}^{\text{domain}}\rVert + \log h(O_t) \\
&- \log \rho_{\text{external}} - \log f(\mathcal{M}) - \log g(\pi) \\
&+ \log \nu + \log \frac{U_M}{U_M + U_o} + \log c_{\min}
\end{aligned}
$$

Group by attribution:

$$
\mathcal{V} \;=\; \underbrace{\log \lVert\delta_{\text{critical}}^{\text{domain}}\rVert - \log \rho_{\text{external}} + \log \nu_{\text{external-cap}}}_{\text{environmental affordance } \mathcal{V}_E}
\;+\; \underbrace{\log h(O_t) - \log f(\mathcal{M}) - \log g(\pi) + \log \frac{\nu_{\text{chosen}}}{\nu_{\text{external-cap}}} + \log \eta^\ast + \log c_{\min}}_{\text{internal-operational-health } \mathcal{V}_I}
$$

Here I've split $\nu = \nu_{\text{external-cap}} \cdot (\nu_{\text{chosen}}/\nu_{\text{external-cap}})$ — the first factor is the maximum rate the environment supports; the second is the fraction of that the agent actually uses.

The **internal-external decomposition** is:

$$\boxed{\;\mathcal{V} = \mathcal{V}_E + \mathcal{V}_I\;}$$

with the explicit constituents:

$$
\mathcal{V}_E = \log \lVert\delta_{\text{critical}}^{\text{domain}}\rVert - \log \rho_{\text{external}} + \log \nu_{\text{external-cap}}
$$

$$
\mathcal{V}_I = \log h(O_t) - \log f(\mathcal{M}) - \log g(\pi) + \log \frac{\nu_{\text{chosen}}}{\nu_{\text{external-cap}}} + \log \eta^\ast + \log c_{\min}
$$

**Reading the terms.**

$\mathcal{V}_E$ (environmental affordance) has three summands:
- $\log \lVert\delta_{\text{critical}}^{\text{domain}}\rVert$: how forgiving is this domain's error tolerance?
- $-\log \rho_{\text{external}}$: how benign is the environment's intrinsic volatility?
- $\log \nu_{\text{external-cap}}$: how densely does the environment emit usable events?

$\mathcal{V}_I$ (internal-operational health) has six summands:
- $\log h(O_t)$: did the agent choose an ambitious objective (penalty) or a cautious one (bonus)?
- $-\log f(\mathcal{M})$: how expressive is the model class? (richer $\Rightarrow f$ smaller $\Rightarrow -\log f$ larger)
- $-\log g(\pi)$: how cleverly does the policy keep the environment in a benign region?
- $\log \nu_{\text{chosen}}/\nu_{\text{external-cap}}$: how much of the environment's event bandwidth does the agent actually use?
- $\log \eta^\ast$: is the update gain well-calibrated?
- $\log c_{\min}$: does the correction function point in a good direction?

**Conservation.** Improving $\mathcal V_I$ by one log-unit and improving $\mathcal V_E$ by one log-unit both move the agent the same distance above the viability threshold. This is the decomposition's operational claim: log-units of internal improvement and log-units of external affordance are *commensurable* contributions to persistence.

## 5. Confounding: internal capacity co-produces environmental affordance

A skilled agent constructs a benign environment. An experienced team writes cleaner code (lowers future $U_o$), institutes better processes (increases effective $\nu$), and stays out of crisis territory (keeps $\rho$ low). The decomposition as stated treats $\mathcal{V}_E$ and $\mathcal{V}_I$ as independent, but in feedback systems they are structurally entangled.

### 5.1 The entanglement, made precise

Four confounding channels — each an AAD machinery piece — couple internal capacity to environmental affordance:

**(i) Observation-quality feedback ( #software-epistemic-properties P6).** Agent actions modify $h$, the observation function. Code quality *is* $U_o$. Write better code now; read better code later. Formally:

$$U_o^{(t)} = U_o^{\text{intrinsic}} + Q(a_{1:t-1})$$

where $Q(\cdot)$ captures the cumulative quality of past actions affecting future observability. The "intrinsic" term is environmental; $Q$ is agent-produced. $\log \eta^\ast$ today contains a cumulative-history term.

**(ii) Policy-benignity feedback.** $g(\pi)$ already absorbs this at the rho-level, but notice: a higher-capacity agent can run a more exploratory policy with the same risk, so $g$ is not policy-neutral. A novice running the "conservative policy" may still produce higher effective $\rho$ than an expert running an "aggressive policy," because the expert's policy benignity is realized only by the expert.

**(iii) Structural-adaptation feedback ( #structural-adaptation-necessity).** A high-capacity agent recognizes when $\mathcal{F}(\mathcal{M})$ is insufficient and switches model classes, after which $f(\mathcal{M}')$ drops. The environment hasn't changed; $\log f(\mathcal{M}')$ decreased because the agent upgraded. Over long horizons $\log f$ is agent-controllable.

**(iv) Objective re-choice.** When performance is high, agents take on harder objectives ( $h(O_t)$ decreases). When struggling, agents take on easier ones ( $h(O_t)$ increases). This is adaptive scope management — but it means *observed* $\mathcal{V}_I$ from field data is biased downward for high-capacity agents (they chose hard problems) and biased upward for low-capacity agents (they chose easy ones).

### 5.2 Is the entanglement breakable?

**Short answer: no, not observationally.** The entanglement is structural: the agent's actions affect the environment, so any observed distribution of $(\mathcal{V}_E, \mathcal{V}_I)$ over time reflects the joint feedback. This is the classical endogeneity problem of econometrics (Pearl's term: *reflection*; Oaxaca–Blinder decomposition's domain).

**Long answer: yes, under specific identification regimes** — and these regimes map exactly onto AAD's existing scope machinery (#edge-update-causal-validity, #ciy-observational-proxy).

**Regime A (intervention-rich).** The analyst can *vary* agent capacity while holding environment fixed, or vary environment while holding agent fixed. Rotation experiments (same team, different codebase; different team, same codebase) do this. Under Regime A, $\mathcal{V}_E$ and $\mathcal{V}_I$ are separately identifiable.

**Regime B (observational, with structural assumptions).** Observing multiple (agent, environment) pairs over time, identify via conditional-independence assumptions: e.g., "changes in team composition are conditionally independent of environmental volatility given the product line." Results inherit the assumption.

**Regime C (passive).** No variation in either side. $\mathcal{V}_E$ and $\mathcal{V}_I$ appear only as their sum. The decomposition becomes *definitional* (one can always write $\mathcal V = \mathcal V_E + \mathcal V_I$ by assumption) but not *identified*.

This regime structure is *identical* to the CIY admissibility regimes ( #ciy-observational-proxy). That is not a coincidence: both are facets of the same underlying identification question — can an analyst (or an agent) distinguish an internal contribution from an external contribution to an observed outcome using the data at hand?

### 5.3 Connection to `#discussion-identifiability-floor`

The internal-external decomposition has an identifiability floor in Regime C. The floor has the canonical shape of `#discussion-identifiability-floor`:

1. **Setting.** Decompose $\mathcal V$ observed in a steady-state agent-environment loop into $\mathcal V_E + \mathcal V_I$.
2. **External theorem.** Pearl/Bareinboim causal hierarchy: distinguishing internal contribution from external contribution requires Level 2 (interventional) data — hold one side fixed, vary the other. Observational data under a fixed agent-environment coupling is Level 1.
3. **No-go.** Under purely observational data (Regime C), for any observed $\mathcal{V}^{\text{obs}}$ there exist infinitely many $(\mathcal V_E, \mathcal V_I)$ pairs consistent with it. The two components are not separately identifiable.
4. **Boundary characterization.** Four escape routes:
   - Rotate agents across environments (vary $\mathcal V_I$ at fixed $\mathcal V_E$).
   - Rotate environments under fixed agents (vary $\mathcal V_E$ at fixed $\mathcal V_I$).
   - Natural experiments: regime shocks that change $\rho_{\text{external}}$ without changing the agent (observe before/after).
   - Structural assumptions about the functional form of $f, g, h$ (identification-by-restriction).
5. **Strengthened consequence.** The rotation-experiment or natural-experiment design is not a *diagnostic convenience* but a *structural requirement* for the decomposition to be meaningful. Without one of the four escapes, "the team is good" vs. "the codebase is easy" is *not a well-posed question*, regardless of what metrics one computes.

This is Instance 3 of the identifiability-floor pattern: the internal-external decomposition is structurally unidentifiable in Regime C. The pattern is shared with Instance 1 (on-policy L0-insufficiency detection) and Instance 2 (L1' under unobservable common cause): all three are cases where the relevant distinction is a Level 2 property that Level 1 data cannot support.

## 6. Identifiability details

Even in Regime A or B, the component-wise decomposition faces more granular identification problems. Catalog:

**$\rho_{\text{external}}$ vs. $f(\mathcal M) \cdot g(\pi)$.** Only observed $\rho$ = product. Separating intrinsic disturbance from model-expressiveness-reduction requires observations under *multiple* model classes or policies. A practical proxy: $f(\mathcal M)$ can be estimated by fitting a saturated (over-parameterized) model and comparing residual magnitudes; $g(\pi)$ by running different policies on a held-out segment. Both are domain-specific and require instrumented variation.

**$\nu_{\text{external-cap}}$ vs. $\nu_{\text{chosen}}/\nu_{\text{external-cap}}$.** If the agent is already at the cap, both are equal and the ratio is 1; the split is vacuous. Separation requires observing the agent operating *below* the cap (with slack to turn up the event rate).

**$\log \eta^\ast$ vs. $\log c_{\min}$.** Jointly determine $\alpha / \nu$; only the product is observed from mismatch trajectories. Separation requires independent estimates of $U_M$, $U_o$, and the correction function's directional structure — available in closed form for Kalman, inferable for Beta-Bernoulli, difficult for PID, essentially unavailable for human judgment.

**$\lVert\delta_{\text{critical}}^{\text{domain}}\rVert$ vs. $h(O_t)$.** The split between "domain tolerance" and "objective ambition" is partly a framing choice. Identification requires comparison across agents with different objectives on the same domain, or the same agent across objectives. Natural candidate: the "ambitious objective" factor $h(O_t)$ is how the *agent* interprets domain criticality; the domain's intrinsic criticality is what a maximally-cautious reference agent would enforce.

**Summary table.**

| Component | Identifiable in Regime A? | Identifiable in Regime B? | Identifiable in Regime C? |
|---|---|---|---|
| $\mathcal V_E$ (aggregate) | yes, via rotation or natural experiments | conditionally, under assumptions | no |
| $\mathcal V_I$ (aggregate) | yes, symmetric to $\mathcal V_E$ | conditionally | no |
| $\rho_{\text{external}}$ vs. $f(\mathcal M), g(\pi)$ | yes, with policy/model variation | conditionally | no |
| $\nu_{\text{external-cap}}$ vs. $\nu_{\text{chosen}}$ | yes, if agent operates below cap | yes, if cap is known | no |
| $\eta^\ast$ vs. $c_{\min}$ | yes, domain-dependent | conditionally | no |
| $\lVert\delta_{\text{critical}}^{\text{domain}}\rVert$ vs. $h(O_t)$ | yes, with objective variation | conditionally | no |

## 7. Worked example: Kalman-tracking agent

Take the Kalman setting from #worked-example-kalman. Scalar state $x_t$, process noise $q = 0.25$, observation noise $r_{a_t}$ with modes $L$ ($r_L = 9$) and $H$ ($r_H = 1$), event rate $\nu = 5$, action mix $70\%H / 30\%L$.

**Compute the viability terms under Model D.**

Given in the example:
- $\rho = 0.18$ surprise/s
- $\lVert\delta_{\text{critical}}\rVert = 1$
- $\bar\eta^\ast = 0.663$
- $\mathcal{T} = 3.315$, $\alpha = \mathcal{T} = 3.315$ (linear Kalman: $\alpha = \mathcal{T}$ by #gain-sector-bridge)
- $R^\ast = \rho/\alpha = 0.054$

$$\mathcal V = \log \lVert\delta_{\text{critical}}\rVert - \log R^\ast = 0 - \log(0.054) = 2.92$$

Decomposing (natural log):

$$\mathcal V = \log \lVert\delta_{\text{critical}}\rVert - \log \rho + \log \alpha = 0 - \log(0.18) + \log(3.315) = 1.71 + 1.20 = 2.91$$

(Roundoff; the two compute the same quantity.)

**Attribute to internal vs. external.**

Assume the scenario: signal $x_t$ has process noise $q = 0.25$ — this is the environment. The agent chose to use both modes $L$ and $H$ rather than one. High-mode sensing is a better $h$, lower $U_o$, agent-selected.

- $\rho_{\text{external}} = $ intrinsic environmental volatility. In this linear-Gaussian setting, process noise $q$ translates to $\rho$ via $\rho \sim \sqrt{q}$-scale injection per second: approximately $\rho_{\text{external}} \approx q \cdot \nu^{1/2} = 0.25 \cdot \sqrt 5 \approx 0.56$? No — cleaner: the *fully-observed* mismatch injection rate equals the process-noise innovation rate, which in continuous-time Kalman is $q$ per unit time. Taking $\rho_{\text{external}} \approx 0.5$ surprise/s (upper bound if the agent had no model).
- $f(\mathcal M)$: the agent has a perfect linear-Gaussian model, so $f(\mathcal M) \approx 0.36$ (reducing 0.5 to 0.18).
- $g(\pi) = 1$ (policy does not affect $\rho$ in this passive-tracking example).
- $\nu_{\text{external-cap}} = 5$ (agent uses the full cap).
- $\eta^\ast = 0.663$ (chosen via action-mix — this is agent-controllable given the sensor choice).
- $c_{\min} = 1$ (Kalman is linear; directional fidelity is 1).

Compute:

$$\mathcal V_E = \log(1) - \log(0.5) + \log(5) = 0 + 0.693 + 1.609 = 2.30$$
$$\mathcal V_I = 0 - \log(0.36) - \log(1) + \log(1) + \log(0.663) + \log(1) = 1.02 - 0.411 = 0.61$$

Check: $\mathcal V_E + \mathcal V_I = 2.30 + 0.61 = 2.91$. ✓

**Interpretation.** The agent's viability margin of 2.91 log-units decomposes as 2.30 from environmental affordance (forgiving task, modest volatility, dense event cap) and 0.61 from internal operational health (model-class expressiveness plus gain calibration). The bulk of the margin is environmental; the agent is good but not great *and the environment is forgiving*.

This matches intuition: a Kalman filter on a linear-Gaussian process is mostly living off the good behavior of the domain. The domain's linearity and Gaussianity are gifts; the agent adds the modest value of using both sensor modes and tracking reasonably well.

**What would change under harder environment?** Triple $q$ (more volatile process): $\rho_{\text{external}} \to 1.5$, $\log \rho_{\text{external}} \to 0.405$, $\mathcal V_E \to 1.20$. Same agent loses 1.1 log-units; persistence margin collapses.

**What would change under better agent?** Upgrade to constant-acceleration model class (richer $\mathcal M'$): $f(\mathcal M') \to 0.1$ say, $-\log f \to 2.30$, $\mathcal V_I \to 1.89$. Same environment, same task: $\mathcal V \to 4.19$, substantially more robust.

The decomposition tells you *where the margin came from*, which tells you what to change.

## 8. TST specialization

Map the decomposition onto a software-development team. Use `#software-epistemic-properties` P1–P6 and the developer-as-AAD-agent mapping in `#scope-developer-agent`.

### 8.1 Per-component TST mapping

**$\rho_{\text{external}}$: environmental disturbance rate, pure external.** What in the codebase/product environment generates unpredicted change that the team had no causal role in producing?

Candidates:
- Upstream dependency breaks (deprecations, CVEs, API changes)
- User requirement shocks (market shifts, regulatory changes)
- Runtime failures not caused by the team's recent changes (load spikes, cloud outages)
- Competitor moves and business-level redirections

Estimator: rate of incidents/changes whose proximal cause is *outside* $\mathcal C_t^{\text{commit}}$ — not attributable to team commits. Measurable from the union of incident logs, deployment-correlated-with-upstream-dep-bumps, and requirement-change tickets, *minus* the subset attributable to the team's own commits.

Exactness: *approximate* in TST's per-quantity exactness audit. Not exact from $\mathcal C_t^{\text{commit}}$ alone — requires incident logs and ticket systems (see #software-epistemic-properties P5: quantities beyond $\mathcal C_t^{\text{commit}}$).

**$f(\mathcal M)$: model-class-expressiveness.** How well does the team's mental model / documentation / architectural representation compress the codebase and its dynamics?

Candidates:
- Architecture documentation quality (prose estimator; low-exactness)
- Design-decision traceability (ADRs, RFCs)
- Type-system coverage (richness of the partially-explicit causal structure P4)
- Test coverage on *semantic* behavior (not line coverage — behavior coverage)

Estimator: approximation of $S(M_t)$ for the team collectively. Poorly identified in practice; proxies include "comprehension time for new hires" ( #comprehension-time) and "frequency of surprise bugs" (diagnostic: structural pattern in the residuals per #structural-adaptation-necessity).

**$g(\pi)$: policy-benignity.** How cleverly does the team's choice of *what to work on* avoid hitting the hard parts of the codebase?

Candidates:
- Change distribution across modules (hitting the stable core vs. the volatile edges — #change-distance, #change-proximity-principle)
- Coupling-weighted change rate ( #system-coupling): changes concentrated on low-coupling modules have lower $\rho$-inducement
- Changeset-size distribution ( #changeset-size-principle): smaller changes have smaller blast radius

Estimator: co-change analysis on $\mathcal C_t^{\text{commit}}$. *Exact* (per the P5 audit, #system-coupling and related quantities are EXACT estimators) as estimators of their own definitions; the inferential step "low coupling implies low $\rho$-inducement" is regime-conditional.

**$\nu_{\text{external-cap}}$ and $\nu_{\text{chosen}}/\nu_{\text{external-cap}}$: event rate, split into cap and usage.**

External cap: the rate at which the environment emits events the team *could* respond to (tickets filed, PRs submitted, alerts fired). Agent ratio: fraction the team actually engages with.

Estimator for the cap: ticket-filing rate, alert rate, PR-submission rate — observable from ticketing and CI systems. Not in $\mathcal C_t^{\text{commit}}$ alone.

Estimator for the chosen rate: commit rate per engineer, PR-merge rate. *Exact* from $\mathcal C_t^{\text{commit}}$ (per #software-epistemic-properties P5).

**$\eta^\ast$: update gain.** Quality of how the team updates its collective understanding on each new piece of information. This is heterogeneous and hard to measure directly; the surrogate TST-native quantities are:

- Post-incident learning uptake (retros → concrete changes) — low-exactness, narrative data
- Refactoring triggered by failed predictions (bug → architecture change) — observable from commit topology near bug fixes
- Cross-module knowledge diffusion ( #conceptual-alignment) — empirical

Exactness: mostly approximate. The team's $\eta^\ast$ is the hardest-to-estimate TST quantity in the decomposition.

**$c_{\min}$: directional fidelity of corrections.** Does the team, when presented with a mismatch signal, tend to change things in a productive direction?

Proxy: fraction of bug fixes that *stay* fixed vs. get reopened or cause regression. Reopen rate and regression rate are observable in issue trackers; the inferential step to $c_{\min}$ is Regime B at best.

**$\lVert\delta_{\text{critical}}^{\text{domain}}\rVert$: domain tolerance for model error.** How much wrongness can the team afford before the product fails?

Candidates: user-facing SLA, business-critical vs. internal-tool distinction, regulatory constraint tightness.

Estimator: operational — post-hoc from incident blast radius and recovery cost. Not a $\mathcal C_t^{\text{commit}}$ quantity.

**$h(O_t)$: objective ambition.** How hard are the features the team is choosing to build?

Proxy: feature complexity (story points? — heuristic), cross-module reach of the targeted feature (P4 causal structure), innovation index (new capabilities vs. incremental improvements).

Estimator: available from PM tools and rough empirical scales. Low-exactness.

### 8.2 TST exactness summary for the decomposition

Borrowing the format from the #software-epistemic-properties per-quantity audit:

| Component | TST estimator | P5 exactness | Regime |
|---|---|---|---|
| $\rho_{\text{external}}$ | Incident-log rate minus commit-attributable subset | Approximate — requires non-commit channels | B |
| $f(\mathcal M)$ | Saturated-model-fit residual ratio | Approximate — requires model variation | B |
| $g(\pi)$ | Coupling-weighted change rate on $\mathcal C_t^{\text{commit}}$ | **Exact** as estimator of its own definition | A for definition, B for $\rho$-mechanism |
| $\nu_{\text{external-cap}}$ | Ticket/alert/PR-submission rate | Approximate — outside $\mathcal C_t^{\text{commit}}$ | A |
| $\nu_{\text{chosen}}/\nu_{\text{cap}}$ | Commit rate / submission rate | **Partially exact** — numerator from $\mathcal C_t^{\text{commit}}$ | A |
| $\eta^\ast$ | Multiple proxies (retro-uptake, refactor-to-mismatch) | Approximate — low-exactness | B/C |
| $c_{\min}$ | Reopen rate, regression rate | Approximate | B |
| $\lVert\delta_{\text{critical}}^{\text{domain}}\rVert$ | SLA, blast radius | Approximate | B |
| $h(O_t)$ | Feature-complexity proxy | Heuristic | C |

**Reading the table.** In TST, the decomposition's components vary dramatically in estimability. The policy-benignity factor ($g(\pi)$, via system-coupling and changeset-size) is *exactly* computable from $\mathcal C_t^{\text{commit}}$. The external-cap and chosen-rate factors are cleanly separable *if* the team has ticketing instrumentation. The internal-operational-health components that are hardest to estimate — $\eta^\ast$, $c_{\min}$, $h(O_t)$ — are exactly the *cognitive* components of the team, which are agent-internal and not exteriorized by current standard team protocols (per #software-epistemic-properties P5 scope).

**Consequence for the diagnostic question.** In practice, a team rotation experiment (route the same team through multiple codebases, or route multiple teams through the same codebase) separates $\mathcal V_E$ from $\mathcal V_I$ cleanly without requiring any of the hard-to-estimate components. This is why rotation is the standard engineering-management diagnostic — it's Regime A identification for the aggregate $(\mathcal V_E, \mathcal V_I)$ split, bypassing the per-component identifiability problems.

### 8.3 Example diagnostic framing

"This team is shipping; should we expand their scope, or rotate people through the codebase?"

The decomposition reframes this:

1. Observe team+codebase pair, estimate $\mathcal V^{\text{obs}}$ (large; the team is shipping).
2. Rotate: either (a) move part of the team to a different codebase for a sprint, or (b) bring in another team to work on the same codebase for a sprint.
3. Under (a): the moved-team's new $\mathcal V$ holds their $\mathcal V_I$ fixed; difference is $\Delta \mathcal V_E$.
4. Under (b): the new-team's $\mathcal V$ holds the codebase's $\mathcal V_E$ fixed; difference is $\Delta \mathcal V_I$.
5. If $\Delta \mathcal V_E$ is large (the original codebase was much easier than others), the apparent team excellence was partly environmental affordance. Decision: rotate people through — the easy codebase won't train up generalists.
6. If $\Delta \mathcal V_I$ is large (other teams struggle on this codebase), the apparent excellence was team-side. Decision: expand scope.

This is the Oaxaca–Blinder-shaped decomposition of wage gap in econometrics, applied to team/codebase attribution.

## 9. Connection to adjacent literature

**Oaxaca–Blinder decomposition (1973).** In econometrics, wage gaps between demographic groups are decomposed into an *endowment* component (group means of observable characteristics differ) and a *return* component (coefficients on those characteristics differ between groups). The internal-external decomposition has the same shape: $\mathcal V_E$ is the endowment component (environment-side "what you start with"); $\mathcal V_I$ is the return component (agent-side "what you do with what you have"). The identification problems — particularly endogeneity when agent and environment co-evolve — are structurally identical.

**Variance decomposition in ANOVA.** When variation in viability across (agent, environment) pairs is observable, ANOVA-style decomposition assigns $\text{Var}(\mathcal V) = \text{Var}_E(\mathcal V_E) + \text{Var}_I(\mathcal V_I) + 2\text{Cov}(\mathcal V_E, \mathcal V_I)$ (if additive). The covariance term is the confounding term §5 identifies — in feedback systems, $\text{Cov}(\mathcal V_E, \mathcal V_I) \gt 0$ generically.

**Shapley-value attribution.** An alternative decomposition framework: attribute $\mathcal V$ to $\mathcal V_E$ and $\mathcal V_I$ via their Shapley values, computed by averaging the marginal contribution of each across all orderings of adding them to the coalition. Under additivity the Shapley values coincide with the log-additive split; under interactions (which are present in the multiplicative pre-log form), the Shapley values smooth out the interaction term. I do not pursue this here; the log-additive split is cleaner and has the Cauchy-FE adjacency.

**Counterfactual attribution (Pearl, Bareinboim).** The "what would have happened if $\mathcal V_E$ had been different?" question is a Level 3 counterfactual. Answering it with observed data requires either intervention (Regime A rotation) or structural assumptions (Regime B functional forms). This is the standard causal-inference framework and is the explicit basis for §5.3's identifiability-floor instance.

**Causal mediation analysis (Imai, Keele, Yamamoto 2010).** When internal capacity partially causes environmental affordance (our confounding channels in §5.1), mediation analysis decomposes the *direct* effect of the agent on viability from the *indirect* effect mediated through environmental affordance. This is the right framework for quantifying the confounding channels precisely; implementing it requires functional-form assumptions ($f, g, h, Q$).

## 10. Sketch derivation: from the persistence condition to the decomposition

The decomposition is not a new theorem — it's a *rearrangement* of existing AAD quantities. But the rearrangement is non-obvious, and the internal/external attribution is a substantive claim. Sketch the derivation.

**Start.** From #persistence-condition (linear Model D operational form):

$$R^\ast = \frac{\rho}{\alpha} \quad \text{(steady-state mismatch)}$$

$$\text{Agent persists} \iff R^\ast \lt \lVert\delta_{\text{critical}}\rVert$$

**Take log-ratio.** Define

$$\mathcal V := \log \frac{\lVert\delta_{\text{critical}}\rVert}{R^\ast} = \log \lVert\delta_{\text{critical}}\rVert - \log R^\ast$$

Persistence is $\mathcal V \gt 0$. This is the target.

**Expand $R^\ast$.** Substitute the Model D steady state:

$$\mathcal V = \log \lVert\delta_{\text{critical}}\rVert - \log \rho + \log \alpha$$

Three summands, each on log-scale. This is the coarse decomposition of §2.

**Expand $\alpha$.** By #gain-sector-bridge, under sub-scope α (Kalman / strongly-convex / exponential-family / linear-PD / gradient), $\alpha = \eta^\ast \cdot c_{\min}$, and $\mathcal T = \nu \cdot \eta^\ast$, so for the linear case $\alpha = \mathcal T$. For the general sub-scope α case:

$$\log \alpha = \log \nu + \log \eta^\ast + \log c_{\min}$$

**Expand $\rho$.** The model-class-expressiveness and policy-benignity factorization (§3.2) gives:

$$\log \rho = \log \rho_{\text{external}} + \log f(\mathcal M) + \log g(\pi)$$

This is the only step requiring an AAD-novel claim. The claim is that $\rho$ in the persistence condition is the *effective* disturbance rate — the rate at which unpredicted change is injected *into the agent's model* — and that this factors multiplicatively into an environmental constant times model-expressiveness-reduction times policy-benignity-reduction. The factorization is approximate (the three factors may interact in reality), but log-additive at first order under the assumption that the three effects operate on independent aspects of $\rho$: $\rho_{\text{external}}$ is the raw rate, $f$ filters what's predicted, $g$ filters what's attempted.

**Expand $\lVert\delta_{\text{critical}}\rVert$.** Similarly, $\log \lVert\delta_{\text{critical}}\rVert = \log \lVert\delta_{\text{critical}}^{\text{domain}}\rVert + \log h(O_t)$ with $h(O_t) \leq 1$ for ambitious objectives.

**Expand $\nu$.** Split into external cap and chosen fraction: $\nu = \nu_{\text{external-cap}} \cdot (\nu_{\text{chosen}}/\nu_{\text{external-cap}})$.

**Assemble.** Substituting all the expansions and grouping by attribution gives the full decomposition of §4.

**Epistemic tier.** The coarse form ($\mathcal V = \log \lVert\delta_{\text{critical}}\rVert - \log \rho + \log \alpha$) is *exact* for Model D linear — it's an algebraic identity on log-$R^\ast$. The expansions of $\rho$, $\alpha$, $\lVert\delta_{\text{critical}}\rVert$, and $\nu$ are at tiers varying from *exact* (the $\alpha = \eta^\ast c_{\min}$ under sub-scope α, from #gain-sector-bridge) to *robust-qualitative* (the $\rho$ and $\lVert\delta_{\text{critical}}\rVert$ factorizations). The overall decomposition sits at *robust-qualitative* because the $\rho$-factorization is the weakest link. Under Model S, the $\log\alpha$ coefficient becomes $\tfrac12 \log\alpha$; the additive structure survives but the coefficient is regime-dependent.

**Conservation, restated.** The decomposition's operational claim — that log-units of internal improvement and log-units of external affordance are commensurable — is *exact under the log-additive form*. It is the geometric claim behind the rearrangement; it follows from the log-linearity without further assumption.

## 11. Relationship to AAD's three meta-segments

Where does this decomposition sit in AAD's architecture?

**#discussion-separability-pattern (positive half).** The decomposition is a separability result — it names the *separable core* of viability attribution (regimes A/B where the components are identifiable) and the *structured repair* (Regime B with functional-form assumptions) and the *general open* (Regime C, where the decomposition is not identifiable observationally). It adds a seventh ladder to the six in `#discussion-separability-pattern`:

| Ladder | Separable core | Structured repair | General open |
|---|---|---|---|
| **Internal-external attribution** (this spike) | **Regime A** — rotation experiments, natural experiments separate $\mathcal V_E$ from $\mathcal V_I$ | **Regime B** — functional-form assumptions on $f, g, h, Q$ | **Regime C** — observational, fixed-coupling data; decomposition is not identifiable |

**#discussion-identifiability-floor (negative half).** §5.3 derives the Regime-C identifiability floor for this decomposition. The external theorem invoked is the Pearl/Bareinboim CHT: separating internal contribution from external contribution requires Level 2 data (holding one side fixed). This is Instance 3 of the floor pattern — shares its shape with Instance 1 (on-policy L0-insufficiency detection) and Instance 2 (L1' single-channel unidentifiability).

**#additive-coordinate-forcing (constructive half).** The log-viability coordinate $\mathcal V$ is an *adjacent family member* of the three Cauchy-FE anchors, not a fourth theorem. Viability has no chain-rule-like compositionality axiom whose Cauchy solution would force the logarithmic form. The logarithmic coordinate is *matched* to the structure (products of independent factors become log-additive), not *forced* by an AAD-internal axiom. This is the honest characterization; elevating it to a fourth theorem would require identifying a compositionality axiom on viability, which I do not see.

**Reading through all three.** The decomposition is:
- a positive-half separability result (seventh ladder candidate);
- a negative-half identifiability floor instance (Instance 3 candidate);
- a constructive adjacent family member, logarithmic by matching rather than by forcing.

Each read surfaces a different load-bearing role.

## 12. Recommendations for promotion

### 12.1 Proposed new segment: `#internal-external-decomposition`

**Slug.** `internal-external-decomposition`

**Type.** `derivation` (claims a log-additive rearrangement of the persistence condition, with honest tier labeling on the expansion steps).

**Status.** `robust-qualitative` at the overall decomposition level; individual expansion steps inherit their own statuses.

**Location.** Appendix A (derivations) — sibling to `#strategy-cost-regret-bound` and `#edge-update-natural-parameter`.

**Depends.**
- `#persistence-condition` (the base inequality being rearranged)
- `#sector-condition-stability` (the $R^\ast = \rho/\alpha$ form)
- `#gain-sector-bridge` (the $\alpha = \eta^\ast c_{\min}$ expansion, sub-scope α)
- `#update-gain` (the $\eta^\ast = U_M/(U_M + U_o)$ expansion)
- `#adaptive-tempo` (the $\mathcal T = \nu \eta^\ast$ identity)
- `#mismatch-dynamics` (the $\rho$ role)
- `#model-class-fitness` (the $f(\mathcal M)$ factor)
- `#edge-update-causal-validity` (Regime A/B/C identification framework)
- `#discussion-identifiability-floor` (the negative-half instance discussion)
- `#discussion-separability-pattern` (the positive-half seventh-ladder discussion)

**Content shape.**
1. Target quantity ($\mathcal V$, log-viability).
2. Coarse decomposition (three terms, *exact* for Model D linear).
3. Fine decomposition ($\mathcal V_E + \mathcal V_I$ split, *robust-qualitative* due to $\rho$ factorization).
4. Identifiability analysis (regime-dependent).
5. Worked Kalman instantiation.
6. TST specialization with per-quantity exactness table.
7. Derivation audit table (see FORMAT.md O-BP14).

### 12.2 Updates to `#operationalization`

Add a section on "Decomposing the persistence margin" with:
- The estimator recipes for $\mathcal V_E$ and $\mathcal V_I$ under Regime A (rotation experiments) and Regime B (functional-form assumptions).
- Cross-reference to `#internal-external-decomposition` for the full derivation.
- A diagnostic checklist: when to suspect the observed viability is agent-driven vs. environment-driven.

### 12.3 Cross-references to add

- `#persistence-condition`: add a Discussion paragraph noting that the persistence inequality admits the internal-external decomposition above; cross-reference the new segment.
- `#discussion-separability-pattern`: add the seventh ladder row.
- `#discussion-identifiability-floor`: add Instance 3 (internal-external decomposition under Regime C).
- `#software-epistemic-properties`: add a Discussion note that the per-quantity exactness audit supports a well-posed TST specialization of the decomposition; cross-reference.
- `#mismatch-decomposition`: add a note distinguishing this per-instant decomposition from the per-history internal-external decomposition.

### 12.4 Pending work before promotion

1. **The $\rho$ factorization is the weakest link.** The log-additive form assumes the three effects ($\rho_{\text{external}}$, $f(\mathcal M)$, $g(\pi)$) operate on independent aspects of the injection rate. This is a working hypothesis, not derived. Either prove it under sub-scope assumptions (e.g., for sufficiently-expressive model classes operating on stationary disturbances, the three effects are first-order-separable), or downgrade the status to heuristic for the expansion step and note the decomposition holds at *robust-qualitative* via the coarse form $\mathcal V = \log \lVert\delta_{\text{critical}}\rVert - \log\rho + \log\alpha$ while the per-component attribution is heuristic.

2. **The confounding in §5 is qualitative.** Formalizing the mediation analysis (Imai et al. 2010-style) for the four specific confounding channels would upgrade the identifiability analysis from discussion-grade to conditional-exact under functional-form assumptions.

3. **The Instance-3-of-identifiability-floor claim needs checking.** Instances 1 and 2 of the floor cite specific external theorems (CHT, Cramér-Rao). Instance 3 cites CHT. Is the CHT application here as clean as in Instance 1? The on-policy L0-insufficiency-detection no-go (Instance 1) constructs a specific L0-world with matched regime conditionals. The internal-external-decomposition no-go (Instance 3) claims that *any* $(\mathcal V_E, \mathcal V_I)$ split consistent with observed $\mathcal V$ is Level-1-equivalent under observational data. Worth writing out the matched-distribution pair explicitly to confirm this is as tight as Instance 1.

4. **Does the decomposition interact with #agent-identity (singular-trajectory scope)?** Viability is defined per trajectory. Aggregating $\mathcal V_E$ across *copies* of an environment (e.g., across multiple customer installations) requires the trajectory-indexed/type-like distinction per `#agent-identity`. The TST specialization (team operating on one codebase) is cleanly token-level; population-level claims about "how viable is *a* team operating on *a* codebase" would need additional scope machinery.

### 12.5 Not in scope of this spike

- Shapley-value attribution: mentioned in §9 but not developed. Cleaner under multiplicative (pre-log) form; the log-additive form makes Shapley and the direct decomposition coincide, so Shapley isn't adding anything here.
- Mediation analysis formalization: noted as future work in 12.4.
- Agent-environment co-evolution dynamics: §5 identifies the confounding but doesn't model the dynamics. A full treatment would need a coupled ODE for $(\mathcal V_E(t), \mathcal V_I(t))$ — structurally adjacent to #adversarial-destabilization's coupled disturbance form.
- Composition: does the decomposition compose when agents form teams (Section III)? Probably: $\mathcal V$ of the composite is related to $\mathcal V$ of the components by a closure-defect term. Not developed here.

## 13. Open questions

1. **Is the log-viability coordinate forced by an AAD-internal axiom?** Per §11, I do not currently see a chain-rule-like compositionality axiom for viability. If such an axiom could be identified — e.g., "viability of a sequence of adaptive cycles is the sum of per-cycle viabilities under independence" — the logarithmic coordinate would become a fourth Cauchy-FE theorem. This would be a substantial strengthening. My current read: plausible but not obviously there.

2. **Does the $\rho$ factorization hold under adversarial environments?** In adversarial settings (#adversarial-destabilization), $\rho$ is not purely "external" — it's partly induced by the adversary's actions. The decomposition as stated treats only one agent; extending to adversarial pairs would require splitting $\rho_{\text{external}}$ further into nature-produced and adversary-produced terms, with the adversary's term being the other agent's internal-operational-health projected onto this agent's environment-demand.

3. **Is there a primal/dual formulation?** The log-viability is a scalar persistence margin. A dual formulation might express the decomposition as a rate-distortion relation: for given viability $\mathcal V$, what's the minimal internal capacity required as a function of environmental affordance (and vice versa)? This would connect to #compression-operations' IB framework.

4. **Connection to cognitive-cost framework.** Increasing $\mathcal V_I$ via richer $\mathcal M$ (lower $f$) and better $\eta^\ast$ has a cost (see `#strategy-complexity-cost`). A full cost-benefit analysis would balance $\mathcal V_I$-gains against computational / deliberative / organizational costs. Not developed here; candidate follow-on spike.

5. **The TST rotation-experiment diagnostic.** Is there literature on engineering-management rotation designs that the TST specialization could reference? (Google's "20% time," Spotify's tribes/guilds, various rotation programs.) If so, the decomposition gives them a principled theoretical grounding. If not, the decomposition suggests a new design posture.

## 14. Summary

- **Target quantity.** Log-viability $\mathcal V = \log \lVert\delta_{\text{critical}}\rVert - \log R^\ast$. Persistence is $\mathcal V \gt 0$. This is the natural coordinate because $R^\ast = \rho/\alpha$ is a ratio of environment-side and agent-side quantities; its log is additive.
- **Coarse decomposition.** $\mathcal V = \log \lVert\delta_{\text{critical}}\rVert - \log \rho + \log \alpha$, *exact* for Model D linear.
- **Fine decomposition.** $\mathcal V = \mathcal V_E + \mathcal V_I$ where $\mathcal V_E$ collects the purely-external factors ($\lVert\delta_{\text{critical}}^{\text{domain}}\rVert$, $\rho_{\text{external}}$, $\nu_{\text{external-cap}}$) and $\mathcal V_I$ collects the agent-controllable factors (objective ambition, model expressiveness, policy benignity, chosen event rate, update gain, directional fidelity). Status *robust-qualitative*, limited by the $\rho$ factorization.
- **Confounding.** Four channels (P6 observation-quality feedback, policy-benignity, structural adaptation, objective re-choice) entangle $\mathcal V_E$ and $\mathcal V_I$ in feedback systems. Structural, not removable.
- **Identifiability.** Regime A (rotation / natural experiments) separately identifies $\mathcal V_E$ and $\mathcal V_I$. Regime B requires functional-form assumptions. Regime C is an identifiability floor (Instance-3 candidate for `#discussion-identifiability-floor`).
- **Worked Kalman example.** For the `#worked-example-kalman` setup, $\mathcal V = 2.91$ decomposes as $\mathcal V_E = 2.30$ (environment-heavy) and $\mathcal V_I = 0.61$ (modest agent contribution) — the agent is tracking well mostly because the domain is forgiving.
- **TST specialization.** Policy-benignity ($g(\pi)$) is exactly estimable from $\mathcal C_t^{\text{commit}}$ (system-coupling / changeset-size); the aggregate $(\mathcal V_E, \mathcal V_I)$ split is separately identifiable via team-rotation experiments without requiring per-component estimation. The internal-operational-health components hardest to estimate are exactly the cognitive ones — not exteriorized by standard team protocols.
- **Meta-segment placement.** Positive-half separability seventh-ladder candidate; negative-half identifiability-floor Instance 3 candidate; adjacent family member in the logarithmic-coordinate family (not a fourth Cauchy-FE theorem, absent a compositionality axiom for viability).
- **Recommendation.** Promote as new appendix segment `#internal-external-decomposition`; update `#operationalization`, `#persistence-condition`, `#discussion-separability-pattern`, `#discussion-identifiability-floor`, `#software-epistemic-properties`, `#mismatch-decomposition` with cross-references and companion notes.

## Appendix A: per-term ontological inventory

A reference table naming each component's ontological status in one place. "Pure" means cleanly one-sided; "mixed" means feedback channels couple it.

| Term | Mathematical form | Ontological status | Estimator difficulty |
|---|---|---|---|
| $\lVert\delta_{\text{critical}}^{\text{domain}}\rVert$ | domain tolerance constant | pure external (domain property) | medium (post-hoc) |
| $h(O_t)$ | objective ambition multiplier | pure internal (agent's chosen objective) | heuristic |
| $\rho_{\text{external}}$ | intrinsic disturbance rate | pure external (environment property) | hard (requires model-comparison) |
| $f(\mathcal M)$ | model-class-expressiveness factor | pure internal (agent's model class) | medium (via residuals) |
| $g(\pi)$ | policy-benignity factor | pure internal (agent's policy) | in TST: exact from commits |
| $\nu_{\text{external-cap}}$ | max event rate environment emits | pure external | medium (requires ticket data) |
| $\nu_{\text{chosen}}/\nu_{\text{external-cap}}$ | fraction of cap the agent uses | pure internal | in TST: exact |
| $\eta^\ast$ | update gain | mixed ($U_M$ internal, $U_o$ external but P6-modifiable) | domain-dependent |
| $c_{\min}$ | directional fidelity | mixed (correction function × loss landscape) | hard outside Kalman |

The "pure external" rows define $\mathcal V_E$; "pure internal" rows define $\mathcal V_I$; "mixed" rows are assigned via the P6 / directional-fidelity arguments in §3.

## Appendix B: comparison with #mismatch-decomposition

The mismatch decomposition is a different decomposition on a different quantity. Comparison:

| Aspect | #mismatch-decomposition | Internal-external decomposition |
|---|---|---|
| Target quantity | $\mathbb{E}[\lVert\delta_t\rVert^2]$ (one-instant MSE) | $\mathcal V$ (log-viability, integrated) |
| Decomposition type | additive (bias-variance identity) | additive on log-scale |
| Components | model error (reducible) + obs noise (irreducible) | environmental affordance $\mathcal V_E$ + internal-operational health $\mathcal V_I$ |
| Agent attribution | model error is agent-side | $\mathcal V_I$ is agent-side (multiple factors) |
| Environment attribution | obs noise is environment-side | $\mathcal V_E$ is environment-side (multiple factors) |
| Identification | exact (bias-variance identity) | regime-dependent (Regime A/B/C) |
| Tier | exact | robust-qualitative |
| Aggregation level | per-observation | per-history |

The mismatch decomposition is *cross-sectional*; the internal-external decomposition is *longitudinal*. They're complementary: one could apply the mismatch decomposition at each instant, integrate the model-error term over time, and relate it to the internal components of the internal-external decomposition (model-error accumulates exactly where $\mathcal V_I$ is low). Not pursued here; candidate follow-on.

---

*End of spike. To be promoted as a new appendix segment plus cross-reference updates per §12, subject to the pending-work items in §12.4.*
