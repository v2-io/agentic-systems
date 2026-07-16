---
slug: der-agent-opacity
type: derived
status: conditional
depends:
  - scope-agent-identity
  - der-interaction-channel-classification
  - der-adversarial-destabilization
  - result-adversarial-tempo-advantage
  - der-team-persistence
  - der-directed-separation
  - disc-identifiability-floor
  - emp-update-gain
  - deriv-edge-credence-dynamics
  - scope-edge-update-causal-validity
  - def-observation-function
stage: draft
---

# Derived: Agent Opacity ($H_b$)

Alongside AAT's heavily formalized *forward* observation quality (how well the agent sees the world — observation ambiguity, model-class fitness, identifiability floor on what the agent can infer), AAT carries a **dual quantity** measuring how well the world sees the agent: **backward predictive uncertainty $H_b$**, an observer-indexed, horizon-indexed, trajectory-indexed entropy of the agent's future actions given another agent's filtration. Adopted from Hafez et al. 2026 as a first-class multi-agent quantity. $H_b$ is the dual of observation quality $U_o$: where $U_o$ characterizes how well the agent sees the world, $H_b$ characterizes how well the world sees the agent.

Each of the four indexing arguments — observer, horizon, trajectory, time — is load-bearing rather than ornamental. *Observer-indexed*: different observers (allies with shared infrastructure; adversaries with limited instrumentation; the environment itself) have different filtrations $\mathcal F_B^t$, and $H_b$ varies accordingly — the same agent has different opacity to different observers. *Horizon-indexed*: immediate-next-action opacity ($\tau = 1$) and long-horizon-plan opacity ($\tau \gg 1$) *decouple* — an agent may be predictable at immediate action but unpredictable at plan level, or vice versa. *Trajectory-indexed*: per `#scope-agent-identity`'s singular-trajectory scope, $H_b$ is the opacity of *this* trajectory's continuation, not a type-level claim about a class of agents. *Time-indexed*: opacity drifts with learning as the observer's model of the agent improves.

$H_b$ is **sign-flipped in value across regimes**: low $H_b$ (legibility) enables cooperative coordination ( #der-team-persistence); high $H_b$ (opacity) enables adversarial effectiveness ( #der-adversarial-destabilization, #result-adversarial-tempo-advantage). The sign-flip is a direct consequence of AAT's existing signed-coupling structure rather than a separate posit — cooperative coupling wants low opacity (allies must predict to preempt); adversarial coupling wants high opacity (predicted attacks are neutralized). This segment's emitter-side four-regime classification is the dual of `#der-interaction-channel-classification`'s recipient-side theory; together they close `#adversarial-edge-targeting` as emitter-optimizer paired with recipient-classifier, with a 16-cell joint composition supplying closed-form arg-max for adversarial-targeting decisions.

## Formal Expression

*[Definition (agent-opacity-Hb)]*

For agent $A$ on singular trajectory $\mathcal C_A$ and observer agent $B$ with filtration $\mathcal F_B^t$ (per-trajectory observable history per `#scope-agent-identity`'s token-level commitment):

$$H_b^{A \mid B}(t, \tau) := H(a_{A, t+\tau} \mid \mathcal{F}_B^t)$$

the entropy of agent $A$'s action at horizon $\tau$ conditional on observer $B$'s filtration at time $t$. **Four indexing arguments:** observer $B$, time $t$, horizon $\tau$, trajectory $\mathcal C_A$. Each is load-bearing:

- **Observer-indexed.** Different observers (allies with shared infrastructure; adversaries with limited instrumentation; environment itself) have different filtrations $\mathcal F_B^t$; $H_b$ varies accordingly.
- **Horizon-indexed.** Immediate-next-action opacity ($\tau = 1$) and long-horizon-plan opacity ($\tau \gg 1$) decouple: an agent may be predictable at immediate action but unpredictable at plan level, or vice versa.
- **Trajectory-indexed.** Per `#scope-agent-identity`, AAT applies to agents on singular trajectories. $H_b^{A\mid B}$ is the opacity of *this* trajectory's continuation, not a type-level claim.
- **Time-indexed.** Opacity may drift with learning (as $B$'s model of $A$ improves, $H_b^{A\mid B}(t)$ decreases); steady-state values exist for ergodic regimes.

Under the IDT-observer specialization — $B$ operates as Hafez's Information Digital Twin monitoring $(S_A, a_A, S'_A)$ from outside $A$'s processing — and under ergodicity, $H_b^{A\mid B}(t, \tau) \to H(S, A \mid S')$ as defined in Hafez et al. 2026. AAT's added features (observer-indexing, horizon-indexing, trajectory-indexing) are the distinctive extensions.

### Backward variance decomposition — the duality made structural

*[Derived (Hb-variance-decomposition; exact in linear-Gaussian sub-scope $\alpha$)]*

In the linear-Gaussian regime, write $A$'s action as $a_{A, t+\tau} = \mu_A(X_{A, t+\tau}) + w_a$ with policy noise $w_a \sim \mathcal{N}(0, U_{a,A}^{(\tau)})$ independent of $B$'s filtration. By the law of total variance, $B$'s predictive variance splits into exactly two sources:

$$\mathrm{Var}\big(a_{A, t+\tau} \mid \mathcal{F}_B^t\big) = \underbrace{\mathrm{Var}\big(\mu_A(X_{A,t+\tau}) \mid \mathcal{F}_B^t\big)}_{U_{\pi, B \to A}^{(\tau)}} + \underbrace{U_{a, A}^{(\tau)}}_{\text{policy noise}},$$

and since the predictive law is Gaussian here (Gaussian mean-uncertainty plus independent Gaussian noise — the same argument as the Kalman predictive),

$$H_b^{A \mid B}(t, \tau) = \tfrac{1}{2}\log(2\pi e) + \tfrac{1}{2}\log\!\left[ U_{\pi, B \to A}^{(\tau)} + U_{a, A}^{(\tau)} \right].$$

$U_{\pi, B \to A}$ is $B$'s uncertainty about $A$'s policy conditional mean — **epistemic**, reducible as $B$ learns $A$ (observation, communication, shared architecture). $U_{a, A}$ is $A$'s intrinsic action variability given its own state — **aleatoric from $B$'s side**: no amount of observing $A$ reduces it; only $A$ making its policy more deterministic does. This is the Kalman forward decomposition $U_M + U_o$ ( #emp-update-gain) reflected across the agent-environment boundary: $U_{\pi, B\to A} \leftrightarrow U_M$ (the learnable model term) and $U_{a, A} \leftrightarrow U_o$ (the channel-noise floor) — with the channel noise living in the agent's *actuator* rather than its *sensor*. The headline duality claim is thereby structural rather than rhetorical: the forward and backward directions carry matching two-term epistemic-plus-aleatoric variance decompositions. (It is a structural correspondence, not an adjoint/optimization-theoretic duality theorem — see Working Notes.)

Two consequences. **(i) The transparency knobs are independent.** An agent can lower its opacity to allies by lowering $U_{\pi}$ (publishing intent — #hyp-auftragstaktik-principle is precisely this knob) without touching $U_a$, or by lowering $U_a$ (policy determinism) without publishing anything; conversely an adversary-facing agent can raise either. **(ii) Identifiability floors bound only the epistemic term.** When $B$'s observations of $A$'s action-consequences sit below an observability floor, $U_{\pi, B \to A}$ cannot be reduced even with unbounded data — a structural lower bound on $H_b^{A \mid B}$ from $B$'s side, which is the observer-side floor reading in §Meta-pattern positioning.

*Tier:* exact in linear-Gaussian sub-scope $\alpha$ (law of total variance + Gaussian entropy); robust qualitative beyond (the two-source split survives; the closed log-form does not).

### Sign-flip via signed coupling

*[Derived (sign-flip-from-signed-coupling)]*

The value of $H_b^A$ *to $A$* depends on the sign of $A$'s coupling to other agents — the same signed-coupling structure that organizes `#der-team-persistence`, `#der-adversarial-destabilization`, and `#deriv-critical-mass-composition`'s (CM2) $\gamma$ parameter.

- **Cooperative coupling ($\gamma^{\text{coop}} \gt 0$, reducing allies' disturbance).** For $B$ to treat $A$'s action as cooperation rather than disturbance, $B$ must predict $A$'s action well enough to preempt or complement it. Under `#der-interaction-channel-classification`'s recipient-side decomposition, unpredictable ally actions fall into Regime II (magnitude/structural shock) rather than Regime I (informative update). Therefore cooperative coupling effectiveness $\gamma_{A \to B}^{\text{coop}}$ is *increasing in legibility*, equivalently decreasing in $H_b^{A\mid B}$. Under sub-scope $\alpha$ Gaussian coupling: $\gamma^{\text{coop, effective}} \propto (1 - H_b^{A\mid B}/H_b^{\max})$.
- **Adversarial coupling ($\gamma^{\text{adv}} \gt 0$, amplifying target's disturbance).** Predicted attacks are neutralized; unpredicted attacks deliver effective disturbance. Adversarial coupling effectiveness is *increasing in opacity* — the mechanism of adversarial advantage (per `#result-adversarial-tempo-advantage`) operates *through* $B$'s failure to predict $A$. Under the same sub-scope $\alpha$ setup: $\gamma^{\text{adv, effective}} \propto H_b^{A\mid B}/H_b^{\max}$.

**The sign-flip on $H_b$'s value-to-$A$ lives in the sign of $\gamma$ itself, not in a different sign on $H_b$.** Cooperative regime $(\gamma^{\text{coop}} \gt 0)$ rewards low $H_b$; adversarial regime ($\gamma^{\text{adv}} \gt 0$) rewards high $H_b$. The same $H_b$ quantity, the same monotone dependence; opposite value-to-$A$ because the signs of the coupling terms differ.

### Emitter-side four-regime classification

*[Formulation (emitter-regimes, dual to #der-interaction-channel-classification)]*

Parallel to `#der-interaction-channel-classification`'s recipient-side four regimes, the emitter $A$ sends events that fall into four emitter-side regimes based on $A$'s opacity signal structure and self-model quality:

- **E-I Broadcast.** $A$ emits actions transparently; $H_b^{A\mid B}$ is low for any observer $B$ with standard instrumentation. Examples: public announcements, published decisions, legible industrial controllers.
- **E-II Selective-signal.** $A$ is transparent to some observers and opaque to others (e.g., shared allied infrastructure gives allies lower $H_b$ than adversaries without that infrastructure). Boundary: differential instrumentation in $\mathcal F_B^t$ across observers.
- **E-III Information-hide.** $A$ is uniformly opaque to observers; actions are randomized, encrypted, or routed through dead-drops. $H_b^{A\mid B}$ near $H_b^{\max}$ for all observers lacking the key / pattern / channel.
- **E-IV Active-deceive.** $A$ emits actions that mispredict — the observer's model of $A$ converges to a *wrong* prediction that differs from the actual action by a larger margin than the same observer's model of the environment would accommodate. Boundary: $A$'s self-model quality (for active-deceive, $A$ must model the observer's model of $A$ well enough to choose actions that exploit it).

### The adversarial-edge-targeting arg-max

The 16-cell emitter-recipient composition (four emitter regimes × four recipient regimes) operationalizes the previously-reserved `#adversarial-edge-targeting` Part III gap: given emitter $A$ choosing which edge $k$ of target $B$'s strategy DAG $\Sigma_B$ to attack, the targeted-attack value is

*[Formulation (adversarial-edge-targeting arg-max; factor-wise grounded, multiplicative composition a modeling choice)]*

$$k^\ast = \arg\max_k \;\; \underbrace{p_k(1 - p_k)}_{\text{credence leverage}} \cdot \underbrace{J_k^2}_{\text{plan sensitivity}} \cdot \underbrace{\iota_k}_{\text{edge identifiability}} \cdot \underbrace{\sigma_k^B}_{\text{observability}} \cdot \underbrace{\big(1 - H_b^{B \mid A}/H_b^{\max}\big)}_{\text{targeting fidelity}}.$$

The first four factors are **$B$-interior** — the value of edge $k$ to a *perfectly-informed* adversary, each with a canonical home: credence leverage $p_k(1-p_k)$ is the Beta-Bernoulli update variance ( #deriv-edge-credence-dynamics); plan sensitivity $J_k = \partial P_\Sigma/\partial p_k \geq 0$ is the plan-value Jacobian ( #deriv-edge-credence-dynamics), entering squared because both the injected mismatch and its propagation to plan value scale with it; edge identifiability $\iota_k$ is the Regime-A interventional-access coefficient ( #scope-edge-update-causal-validity); and $\sigma_k^B$ is $B$'s observability of the edge ( #def-observation-function). The **fifth factor is the opacity contribution**: $A$'s targeting fidelity scales with $A$'s legibility-*of*-$B$, i.e. with low $H_b^{B \mid A}$. Under full legibility ($H_b^{B \mid A} \to 0$) the arg-max is fully exploitable — $A$ strikes the single highest-value edge. Under full opacity ($H_b^{B \mid A} \to H_b^{\max}$) the fifth factor vanishes and targeting collapses to the untargeted broadcast attack $\arg\max_k p_k(1-p_k)\,J_k^2$ — the edges most valuable *in expectation*, with no per-edge aim. This is the emitter-side optimizer paired with `#der-interaction-channel-classification`'s recipient-side classifier, closing the pairing that segment's §"Pairing with #adversarial-edge-targeting" advertised. The multiplicative composition is a first-order modeling choice (treating the factors as independent); the individual factors are the derived content, and a second-order interaction analysis (e.g., whether the targeting-fidelity factor should modulate $J_k$ rather than multiply it) is the natural strengthening (Working Notes).

### Tempo amplification by opacity

*[Derived (tempo-amplification-by-opacity)]*

`#result-adversarial-tempo-advantage`'s tempo-multiplier $\gamma_A \mathcal T_A$ in `#der-adversarial-destabilization` decomposes into a tempo term and an opacity term:

$$\mathcal{T}_A^{\text{effective}} = \mathcal{T}_A \cdot \frac{H_b^{A\mid B}}{H_b^{\max}} \quad \text{(Model D adversarial coupling)}$$

The superlinear formula $(\mathcal T_A / \mathcal T_B)^2$ becomes $(\mathcal T_A / \mathcal T_B)^2 \cdot (H_b^{A\mid B} / H_b^{B\mid A})^2$ under bilateral opacity — a higher-order tensor product with the same exponent $b = 2$ (Model D) or $b = 3/2$ (Model S) from `#result-adversarial-exponent-regimes`. Whether $b$ itself is reshaped under bilateral opacity is open; the leading-order scaling is the tempo-opacity product.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| $H_b^{A\mid B}(t, \tau)$ definition | Adopted from Hafez et al. 2026; extended with observer / horizon / trajectory indexing per `#scope-agent-identity` | Formulation choice (adoption + AAT-extension) |
| Reduction to Hafez's $H(S, A \mid S')$ under IDT-observer + ergodic regime | Direct substitution | Derived (exact under IDT + ergodicity) |
| Sign-flip via signed coupling | Cooperative coupling requires predictability (allies preempt); adversarial coupling operates via disturbance-injection (predicted attack is neutralized) | Derived (from existing `#der-team-persistence` + `#der-adversarial-destabilization` signed-$\gamma$ structure) |
| Emitter-side four-regime classification | Dual construction to `#der-interaction-channel-classification`'s recipient-side four regimes | Formulation choice |
| 16-cell emitter-recipient composition closes `#adversarial-edge-targeting` | Five-factor arg-max: four $B$-interior factors (credence leverage, plan-Jacobian$^2$, edge identifiability, observability) each canonically grounded, times the opacity targeting-fidelity factor | Factors derived; multiplicative product-form a first-order modeling choice |
| Backward variance decomposition $H_b = \tfrac12\log 2\pi e + \tfrac12\log[U_{\pi,B\to A} + U_{a,A}]$ | Law of total variance + Gaussian entropy; the structural dual of the Kalman $U_M + U_o$ split | Derived (exact in linear-Gaussian sub-scope $\alpha$; robust qualitative beyond) |
| Tempo-amplification leading-order: $\mathcal{T}^{\text{eff}} = \mathcal{T} \cdot H_b/H_b^{\max}$ | First-order substitution into `#result-adversarial-tempo-advantage`'s tempo-multiplier under Model D | Derived (conditional on Gaussian-coupling sub-scope $\alpha$) |
| Parameterization-invariance of $H_b$ | $H_b$ is an action-marginal entropy; action space is coordinate-free per `#scope-agent-identity` | Derived |
| Candidate 4th `#disc-identifiability-floor` instance (generic observer-side form) | $H_b$'s formal structure — "observer cannot predict agent's future action better than $H_b^{A\mid B}$" — is a CHT-style no-go at the observer-side-inference task | Discussion-grade (framing; precise external theorem not yet identified) |
| Candidate opacity ladder for `#disc-separability-pattern` | Transparent-core / partial-transparency / full-opacity across observer filtrations | Formulation choice (ladder proposal) |
| Effects-spiral opacity amplification (higher $H_b$ → higher $\gamma_A$ → larger $\dot V_B$ → $B$'s actions become more erratic → observer's model of $B$ degrades → higher $H_b^{B\mid A}$) | Composition of sign-flip derivation with `#der-adversarial-destabilization`'s effects spiral | Sketch (discussion-grade; specific functional form open) |
| Dual-filtration apparatus (each agent's $M_t$ carries an other-filtration as feature) | Would unify observer-indexing with `#scope-agent-identity`'s single-trajectory formalism more tightly | Open extension (mild architectural, orthogonal to derivations) |
| Sharp functional form for $\gamma^{\text{adv}}_{\text{effective}} = f(H_b)$ | Leading-order: $\gamma \propto H_b$. Exact function depends on sub-scope — Gaussian-coupling linear; sigmoid-coupling saturating | Open per sub-scope |

## Epistemic Status

*Conditional.* Max attainable: *exact* for the Hafez-reduction under IDT + ergodicity; *derived* for the sign-flip via signed-coupling; *formulation choice* for the emitter-regime classification structure; *conditional* for the tempo-amplification formula; *discussion-grade* for the meta-pattern candidate status.

**Load-bearing:**
- The sign-flip derivation from existing signed-$\gamma$ structure is the segment's core structural contribution — the adversarial/cooperative opacity duality is not a separate posit; it falls out of AAT's existing signed-coupling apparatus.
- The emitter-side four-regime classification is a clean dual to `#der-interaction-channel-classification`; its derivation is parallel (boundaries in AAT-native quantities — emitter opacity signal structure, self-model quality, coupling regime).
- The closure of `#adversarial-edge-targeting` via the 16-cell composition is a derived arg-max; the previously-stated GAP is filled.

**Not established:**
- Sharp functional forms for $\gamma^{\text{adv}}_{\text{effective}}(H_b)$ outside Gaussian-coupling sub-scope $\alpha$.
- Whether $b$ (the adversarial exponent from `#result-adversarial-exponent-regimes`) is reshaped under bilateral opacity.
- Formal fourth `#disc-identifiability-floor` instance (requires external-theorem anchoring not yet identified); discussion-grade framing only.
- The effects-spiral's opacity amplification (composition with `#der-adversarial-destabilization`'s spiral) is sketch-level.

## Honest Limits

- **Observer-indexing under complex information structures.** $\mathcal F_B^t$ may include shared memory, cryptographic keys, insider knowledge, or partial access to $A$'s internal state. Enumerating all relevant observer-filtration structures for a specific application is task-specific; the segment provides the formal framework, not the per-instance enumeration.
- **Active-deceive (E-IV) requires $A$ to model $B$'s model of $A$.** Mutual-modeling regress under partially-opposing objectives connects to `#deriv-strategic-composition`'s joint-Jacobian analysis. Active-deceive is formally reachable only when $A$'s GUC architecture admits modeling another agent's model — typically Class 3 (Coupled; LLM-style) or Class 2 (Partial) architectures.
- **Type-level vs token-level opacity.** $H_b$ is trajectory-indexed per `#scope-agent-identity`. Statements about "the opacity of model X" (aggregated across deployments) are type-level claims outside AAT's formal scope; they require additional machinery (e.g., population-level dynamics per Part III gaps).

## Discussion

**Dual to observation quality.** $U_o$ characterizes how well the agent sees the world: observation noise, ambiguity, model-class fitness. $H_b$ characterizes how well the world sees the agent: predictability to observers. The duality is structural — both quantify information flow through the agent-environment boundary, in opposite directions. High $U_o$ agent (observes the world well) and low $H_b$ agent (is observed well) are independent properties; an agent can have one without the other.

**Closing `#adversarial-edge-targeting`.** The segment provides the emitter-side arg-max structure missing from the Part III adversarial machinery. Paired with `#der-interaction-channel-classification`'s recipient-side four-regime decomposition, the full adversarial-targeting problem has a closed-form: choose edges where emitter's $H_b$ (to target) and target's recipient-side vulnerability (Regime II magnitude/structural shock) are jointly maximized. This operationalizes what "inside the opponent's loop" means at the targeting layer — Boyd's aphorism becomes an explicit optimization over the 16-cell emitter-recipient product.

**Meta-pattern positioning.**
- *`#disc-identifiability-floor`:* $H_b$'s structure suggests a generic observer-side floor — "the observer cannot predict the agent's action better than $H_b$" — that Instances 1/2/3 specialize on specific variables (causal structure / mixture parameters / coupling sign). The generic framing is candidate-status: it lacks a single external-theorem anchor clear enough to match F1's CHT or F13's Cramér-Rao, but $H_b$ appears naturally in Instance 3's coupling-sign unidentifiability and in Instance 1's on-policy detection no-go (an observer watching the agent's on-policy play has non-zero $H_b$ on the agent's interventional regime).
- *`#disc-separability-pattern`:* candidate opacity ladder — transparent-core (E-I Broadcast; allies / public interfaces) / structured-repair (E-II Selective-signal; trust-weighted partial instrumentation) / general-open (E-III, E-IV; uniformly opaque or active-deceive). Adds to the ladder count if adopted.
- *`#disc-additive-coordinate-forcing`:* $H_b$'s logarithmic form is adopted from Shannon via Khinchin-Aczél axiomatics, imported as an applied external theorem rather than re-forced under an AAT-internal additivity axiom. Cross-agent additivity fails under the coupling regimes AAT cares about (correlated opacity structures break independence). Adjacent family member, parallel to the IB Lagrangian's position — not a primary instance.

**Parameterization-invariance composes cleanly.** $H_b$ is an action-marginal entropy. Under `#scope-agent-identity`'s (PI) axiom, the action space is coordinate-free; $H_b$ is invariant under change of the agent's internal-state parameterization. This composes with the (PI)/Čencov fourth primary instance of `#disc-additive-coordinate-forcing` without adding a new axiom.

**Relation to `#der-directed-separation`.** Class 3 (Coupled) agents have high structural opacity to any observer without internal access — their $f_M$ and $G_t$ are entangled, so predicting the next action requires joint state modelling. Class 1 (Separated) agents are more transparent at the interface level because the decomposed update admits separate modelling of epistemic vs. purposeful components. $H_b$ therefore tends to be *architecturally higher* for Coupled (Class 3) agents — a structural consequence of architecture rather than choice, beyond what E-III Information-hide captures.

**Hafez integration note.** The IDT pattern (Hafez et al. 2026) uses bi-predictability $P$ (how well a sidecar observer can predict the agent's next state-action) and entropy change $\Delta H$ as diagnostics. The IDT's reported 89% perturbation-detection accuracy (vs. 44% for reward-based monitoring) operates on the Level-2 structure per `#der-loop-interventional-access`. In AAT terms, the IDT is a low-$H_b$-preserving observation channel — its presence as a modular sidecar reduces $H_b$ for the operator without increasing the agent's internal complexity. For `03-llm-core/`, this validates that modular monitoring of internally-merged agents is feasible and effective even when the agent itself is architecturally Class 3 (Coupled).

## Findings

### Agent Opacity ($H_b$) as Dual to Observation Quality ($U_o$)

**Brief:** How well the agent sees the world (observation quality $U_o$) and how well the world sees the agent (backward predictive uncertainty $H_b$) are formal duals — both quantify information flow through the agent-environment boundary, in opposite directions. $H_b$ is observer-, horizon-, and trajectory-indexed, extending Hafez's $H(S, A \mid S')$ with these load-bearing indices. The same $H_b$ quantity has opposite value-to-the-agent depending on coupling sign: cooperative coupling rewards low $H_b$ (allies must predict to coordinate); adversarial coupling rewards high $H_b$ (adversaries cannot neutralize what they cannot predict). The sign-flip is not a separate posit — it falls out of AAT's existing signed-coupling structure ($\gamma^{\text{coop}} \gt 0$ for ally-disturbance reduction; $\gamma^{\text{adv}} \gt 0$ for target-disturbance amplification). Adversarial tempo advantage decomposes into a tempo term and an opacity term: $\mathcal{T}^{\text{eff}} = \mathcal{T} \cdot H_b/H_b^{\max}$, so the superlinear $(\mathcal T_A/\mathcal T_B)^2$ advantage from `#result-adversarial-tempo-advantage` scales with the bilateral opacity ratio $(H_b^{A\mid B}/H_b^{B\mid A})^2$ under Model D.

**Impact:** Operationalizes Boyd's OODA-loop aphorism ("inside the opponent's loop") as a precise multiplicative relationship between tempo and opacity, replacing a metaphor with a coupled differential structure. Closes the previously-reserved `#adversarial-edge-targeting` gap as a 16-cell emitter-recipient composition (4 emitter regimes × 4 recipient regimes from the dual `#der-interaction-channel-classification`), giving a closed-form arg-max for "where to attack." The duality with $U_o$ lets the same machinery cover opposite information regimes — high-$U_o$ low-$H_b$ agents (sees well, is seen well) versus low-$U_o$ high-$H_b$ agents (sees poorly, is hidden) — without parallel theorems for each. Direct relevance to multi-agent safety (legibility for cooperation), adversarial robustness (opacity as targeting-vulnerability shaping), and IDT-style monitoring of opaque AI systems (the IDT pattern is a low-$H_b$-preserving observation channel).

**Novelty Claim:** *Claim differentiation* on Hafez's $H_b$. The base quantity is *adopted* from Hafez et al. 2026 with citation and original name; the AAT-distinctive contributions are (i) the observer/horizon/trajectory indexing per `#scope-agent-identity`, (ii) the sign-flip derivation from existing signed-coupling structure rather than as a separate posit, (iii) the emitter-side four-regime classification dual to AAT's recipient-side classification, closing the adversarial-edge-targeting arg-max via the 16-cell composition, and (iv) the tempo-opacity decomposition of `#result-adversarial-tempo-advantage`. The $U_o \leftrightarrow H_b$ duality framing is the integrative move; predictability has been studied in games and information-theoretic security, but the formal-dual treatment with shared signed-coupling structure appears AAT-distinctive.

**Related Work:**

| ASF Concern | Prior-art Language | Relationship / Positioning |
|---|---|---|
| The base $H_b$ quantity (entropy of agent's action conditional on observer filtration) | Hafez, Khan & Iqbal 2026 *A Mathematical Theory of Agency and Intelligence* — $H(S, A \mid S')$ under IDT-observer (published 2026, found 2026-03) | *formal antecedent* — adopted directly; AAT reduces to Hafez's form under IDT + ergodicity. The four-index extension is the AAT-distinctive layering |
| OODA loop and tempo-opacity advantage | Boyd 1986–1995 briefings: *Patterns of Conflict*, *The Essence of Winning and Losing* (delivered 1986–1995, found pre-2026) | *conceptual precursor* — supplies the "inside the opponent's loop" intuition for tempo and opacity advantage; the AAT result quantifies the coupling and decomposes the multiplier |
| Predictability as strategic resource in games | Camerer 2003 *Behavioral Game Theory*; Aumann & Maschler 1995 *Repeated Games with Incomplete Information* (published 1995/2003, found pre-2026) | *conceptual precursor* — predictability and information advantage are well-studied in game theory; the AAT treatment as a formal dual to sensor noise via signed coupling is distinctive |
| Information-theoretic security and channel opacity | Shannon 1949 *Communication Theory of Secrecy Systems*, Bell System Technical Journal 28(4); modern steganography literature (Cachin 1998) (published 1949/1998, found pre-2026) | *conceptual precursor* — opacity as a quantifiable information-channel property; AAT applies the same machinery to action-prediction rather than message-transmission |
| Causal Hierarchy Theorem and observer-side identifiability | Bareinboim, Correa, Ibeling & Icard 2022 (published 2022, found 2025) | *adjacent* — observer-side identifiability floor for causal structure; $H_b$ plays an analogous role for action-prediction. Candidate fourth instance of `#disc-identifiability-floor` (discussion-grade) |
| Bi-predictability $P$ as substrate-independent diagnostic | Hafez et al. 2026 (cited above) | *formal antecedent* — IDT-based bi-predictability complements $H_b$ as the practitioner-facing diagnostic; AAT's observer-indexing makes the dependence on filtration explicit |

**Search Log:**
- 2026-04 (*intuition-only* on the $U_o$-$H_b$ duality framing): no targeted Undermind-grade search has been conducted on whether information-theoretic agent frameworks elsewhere treat predictability-of-agent and observability-of-world as formal duals via shared signed-coupling structure. Hafez 2026's $H_b$ is the explicit formal antecedent for the base quantity; the AAT-distinctive layering (observer/horizon/trajectory indexing + sign-flip derivation + emitter-regime dual) is the segment's contribution. Targeted future search candidates: epistemic game theory (Aumann's tradition); inverse reinforcement learning where the observer infers agent policy and predictability bounds the inference task (Ng & Russell 2000; Ziebart et al. 2008); legibility / readability literature in human-robot interaction (Dragan & Srinivasa 2013); multi-agent identifiability and observability literature. Pre-search expectation: the constituent moves are well-precedented; the integration as formal dual via shared coupling structure within an agent theory may be novel under nominally-comprehensive search.
- 2026-03 (*targeted*): Hafez et al. 2026 confirmed as formal antecedent for the base $H_b$ quantity and bi-predictability diagnostic; the IDT-as-low-$H_b$-channel framing follows directly.

## Working Notes

- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Three occurrences updated: (1) Honest Limits "Class 2 (LLM-style)" → "Class 3 (Coupled; LLM-style)"; (2) Discussion "Class 2 (fully merged) / Class 1 (modular)" → "Class 3 (Coupled) / Class 1 (Separated)"; (3) Hafez integration note "architecturally Class 2" → "Class 3 (Coupled)". $H_b$ symbol and the E-I/E-II/E-III/E-IV emitter-regime classification are independent of the GUC rename — untouched. Removed at `candidate` stage per FORMAT.md Gate 4.

- The (C-iv) scope route of `#scope-composite-agent` accommodates adversarial composition via equilibrium convergence; the effects-spiral joint-Jacobian eigenvalue condition of `#deriv-strategic-composition` composes with this segment's opacity-amplification story to give a fully-coupled picture of symmetric adversarial dynamics. Full composition is open work.
- Candidate fourth-instance formalization for `#disc-identifiability-floor`: the most natural external-theorem anchor is Fano's inequality (relating $H_b$ to error-probability lower bounds) applied to the observer-side prediction task. Open; not pursued here. Two follow-on spikes tested Fano-as-floor-anchor and reach convergent negative conclusions from different inferential tasks: `spikes/.integrated/spike-4th-identifiability-floor-instance-2026-05-20.md` §3 tests Fano on observer-side *action* prediction and demonstrates Outcome C (Fano is a continuous quantitative bound on $P_e$ given $H_b$, not a categorical structural no-go in the M1 sense; the proposed AAT-side escapes either restate Fano's RHS or shift to agent-side policy commitments rather than information-augmentation escapes in the Instances 1–3 sense); `spikes/.integrated/spike-identifiability-floor-instance4-resolution-2026-05-18.md` §4 tests Fano on observer-side *architecture* prediction (Kalman-Ho similarity orbit) and finds Fano degenerates to the vacuous bound at $I = 0$ (now landed as `#der-architecture-noidentifiability` §"Why Fano Is the Finite-Sample Refinement"). The action-prediction-task framing (2026-05-20) and the architecture-prediction-task framing (2026-05-18) reach convergent conclusions on Fano from different inferential tasks: Fano is the finite-sample refinement of an otherwise-attainable task, not the categorical floor anchor M1 requires. The right home for Fano-on-$H_b$ remains adjacent to M1 (this segment's §"Meta-pattern positioning", discussion-grade), not in the floor count.
- The 16-cell emitter-recipient composition admits closed-form arg-max only under sub-scope $\alpha$ coupling; general non-convex coupling requires per-case optimization.
- **2026-07-16 — arg-max formula and backward variance decomposition landed from `spikes/.integrated/spike-hb-agent-opacity.md` (§4.4, §3.2).** The five-factor targeting arg-max was previously stated in prose ("closes the gap") but the formula lived only in the spike; it is now displayed with each factor grounded to its home segment. Honest scoping (from the spike's own off-ramp, 526815 F252/F254): the four $B$-interior factors are derived, but the *multiplicative product* is a first-order independence assumption, not a derived optimization — a second-order interaction analysis (does targeting-fidelity modulate $J_k$ or multiply it? is the product the first-order Taylor expansion of an adversary value function $V_O^{\text{adv}}$?) is the strengthening path, and until it lands the arg-max is a `Formulation`, not a `Result`. The backward variance decomposition is exact in linear-Gaussian sub-scope $\alpha$ (law of total variance); it is what makes the $U_o \leftrightarrow H_b$ duality *structural* (matching two-term epistemic+aleatoric splits) rather than merely evocative — though note it is a structural correspondence, not an adjoint duality theorem (the "formal dual" phrasing elsewhere in the segment is flagged in the off-ramp, 526815 F248, as owing either that theorem or a softening to "structural dual"; the decomposition supports the weaker, honest reading).
- Dual-filtration apparatus ($M_A$ carries $\mathcal F_B^t$ as feature, $M_B$ carries $\mathcal F_A^t$ as feature) would tighten the formalism by unifying observer-indexing with the single-trajectory scope of `#scope-agent-identity`. Architecturally clean; not needed for the derivations here.

### Incidental audit gold (gold-lift sweep, A15, 2026-05-31)

Cross-audit "wandering thoughts" / §14 ideation, deduplicated across substrates and lightly attributed. *Orthogonal* pedagogical / framing / forward-vision material staged for an eventual separate Brief/Discussion promotion pass — kept apart from certified findings. **Coverage:** five dirs reached a digested reflection on this segment (193847 Gemini, 526815 deeply-mathematical, 471203 Claude batched §III-adversarial, 829314 Gemini, 849201 Gemini). This was independently rated one of the highest-felt-value segments in Part III across substrates. Finding-vs-framing conflation preserved as signal.

#### 1. Candidate Brief prose / pre-prose

- The duality stated as a one-liner readers reach for: **"$U_o$ is how well I compress the environment's state into my model; $H_b$ is how well the environment (or an opponent) compresses *my* state into *theirs*"** — same machinery, opposite directions through the agent-environment boundary (Gemini, 829314; Claude, 471203). Strong Brief anchor.
- The legibility sign-flip in plain English: **"In cooperation, legibility is strength; in competition, legibility is death"** (Gemini, 829314) — and its mechanism gloss, "allies must predict to coordinate; adversaries cannot neutralize what they cannot predict" (already echoed in the current Brief).
- E-III vs E-IV distinction worth a crisp sentence: **"Hiding (E-III) increases the observer's *variance*; deceiving (E-IV) shifts the observer's *mean*"** — and active-deceive uniquely requires modeling the observer's model of you, which is the cognitive cost of lying (Gemini, 193847; Gemini, 849201).

#### 2. Candidate Discussion

- **Predator-prey arms race** as the canonical instantiation of the duality: the predator evolves to lower its $U_o$ (better eyes/smell) and raise its $H_b$ (camouflage, silent movement); prey does the same — a clean evocative frame for *why* the two quantities are dual and why they co-evolve (Gemini, 829314).
- **The internal-transparency / external-opacity tension** as a substantive organizational-dynamics Discussion angle: cooperation ($\gamma^{\text{coop}} \gt 0$, `#der-team-persistence`) wants sub-agents *legible to each other* ($H_b \to 0$: shared dashboards, transparent KPIs); defeating outside competitors ($\gamma^{\text{adv}} \gt 0$, `#der-adversarial-destabilization`) wants the composite *opaque to the world* ($H_b \to H_b^{\max}$). It is physically hard to build a system internally transparent but externally opaque — the internal dashboard that lowers internal $H_b$ raises leak probability and lowers external $H_b$ too. AAT supplies the explicit trade-off: weigh internal coordination gain $\Delta\gamma^{\text{coop}}\cdot\mathcal{T}$ against external vulnerability loss $\Delta\gamma^{\text{adv}}\cdot\mathcal T_{\text{competitor}}$ (Gemini, 829314). *(Verify the multiplicative trade-off form against the segment's leading-order $\gamma \propto H_b$ scoping before promoting past discussion-grade.)*

#### 3. Follow-up items

- **Effects-spiral functional form** (already in WN as sketch): a future segment giving the explicit $\gamma_A(\lVert\delta_B\rVert)$ dependence would promote the spiral from discussion-grade; mechanism candidates named by an auditor: (i) erratic actions degrade coupling-channel structure; (ii) degrading $M_t$ widens action variance (Claude, 471203).
- **Candidate 4th identifiability-floor instance via Fano on observer-side prediction** — flagged again by 471203 as worth pursuing; already resolved-negative in WN (two convergent spikes show Fano is the finite-sample refinement, not the categorical floor). Recorded so a future reader does not re-attempt without the WN context.

#### 4. Readers often ask / wonder

- **"How does $H_b$ scale empirically in LLM agents?"** — recurring want (Gemini, 829314; Gemini, 849201); points at the `03-llm-core/` IDT-monitoring story.
- **Mutual-modeling regress.** If $A$ models $B$'s model of $A$, and vice versa, what bounds the depth? Does AAT assume bounded-depth modeling (e.g. depth-2)? (Gemini, 193847.)
- **Can an agent be blind (high $U_o$) yet perfectly predictable (low $H_b$)?** A reader probing the independence of the two quantities — intuition says a blind agent driven by internal noise/false priors is *less* predictable to an observer who sees true state, unless it is completely rigid (Gemini, 193847). A worked sentence on the independence (the segment already asserts it) would preempt this.

#### 5. Candidate figures

- **$H_b$ as a directed observer-channel** from $A$'s future action into $B$'s filtration, with the *same* channel feeding opposite value-stories by coupling sign, plus a second directed channel for target-opacity-to-attacker; annotate entropy-normalization and multiplier assumptions (Claude/Codex, 526815, sketched). Pairs naturally with the 16-cell emitter×recipient targeting matrix as the segment's two figures.

#### Belongs elsewhere

- **Forward-vision (ELI safety, `04-eli-core/` / `03-llm-core/`).** "We cannot just align a future AI's goals with ours; we must demand it operate in an E-I (Broadcast) regime — highly legible. If it solves problems with bizarre incomprehensible logic (high $H_b$), we cannot cooperate with it safely *even if it is trying to help*. The infrastructure must enforce legibility as a hard constraint on the policy space $\Pi$." Names SOPs, uniforms, turn-signals, polite conventions as "mathematical technologies that artificially lower $H_b$ so $\gamma^{\text{coop}}$ can function" — the mathematical foundation of trust (Gemini, 193847). Aspirational application pointing at logogenic/logozoetic safety architecture, not this segment.

#### Off-ramp (NOT gold) — routed for adjudication, not promotion

Certified-track (overclaim / scope-narrowing / definitional-rigor) findings, durable here but belonging to the findings adjudication stream. Almost entirely from the deeply-mathematical auditor (526815), with one duality-overclaim poke seconded by 193847.

- **(526815 F248 / 193847 poke-1) — "formal dual" overclaims.** $U_o$ (covariance / scalar noise) and $H_b$ (conditional Shannon entropy) are opposite-direction information quantities but not duals in the strict optimization / geometric / adjoint sense; "formal dual" promises a theorem not present. Recommended direction: either supply the channel-capacity / adjoint relation that *makes* it a formal duality (strengthen), or label it "informational / structural dual" (soften only if strengthening fails). The current Brief and Discussion lean on "formal dual" — flag for the adjudication call.
- **(526815 F246) — action-space entropy convention.** $H_b^{\max}$ normalization and parameterization-invariance need discrete/quantized actions or a reference measure; differential entropy on continuous actions is not coordinate-invariant and can go negative. (The segment asserts parameterization-invariance via `#scope-agent-identity`'s (PI) axiom — verify that discharges this.)
- **(526815 F250/F251) — the $H_b/H_b^{\max}$ multiplier is brittle.** $\mathcal{T}^{\text{eff}} = \mathcal{T}\cdot H_b/H_b^{\max}$ drives *all* low-opacity adversarial tempo to zero, but predictable attacks can still impose disturbance; opacity should modulate coupling *effectiveness* / neutralization-probability, not multiply all tempo to zero. The bilateral ratio $(H_b^{A\mid B}/H_b^{B\mid A})^2$ goes singular near zero denominator and assumes symmetric entry through one multiplicative channel — needs floors / saturation and a direction-specific model.
- **(526815 F247) — the Hafez reduction is not "direct substitution."** Future-action entropy conditional on an observer filtration vs. backward state-action entropy conditional on next state are different conditionings absent an explicit time-reversal / observer-model equating them; "direct substitution under IDT + ergodicity" needs that bridge shown.
- **(526815 F252/F253/F254) — emitter regimes / 16-cell are formulation, not derivation.** The emitter four-regime classification lacks boundary inequalities comparable to the recipient-side sector/model/observability tests; the 16-cell "closed-form arg-max" needs explicit edge utilities, constraints, and an adversary reward function (193847 poke-2: show the opacity × vulnerability product is the first-order Taylor expansion of $V_O^{\text{adv}}$); "closes `#adversarial-edge-targeting`" is too strong absent an actual source segment / formal optimization result.
- **(526815 F255) — "Class 3 ⟹ high structural opacity" not guaranteed.** A Coupled agent with simple/instrumented output dynamics can be externally predictable.
- **(526815 F256/F258, watch) — Hafez/IDT empirical numbers** support monitoring feasibility, not by themselves the Level-2-access / low-$H_b$-sidecar / opacity-sign claims; the novelty claim should separate searched-and-confirmed prior art from intuition-only search notes.
- **(526815 F257, watch) — keep $H_b^{A\mid B}$ (attacker opacity to target) distinct from $H_b^{B\mid A}$ (target opacity to attacker)** throughout; conflating the two directions creates sign errors. (The current text mostly does, but this is the recurring trap to guard in promotion.)
