---
slug: agent-opacity
type: derived
status: conditional
depends:
  - agent-identity
  - interaction-channel-classification
  - adversarial-destabilization
  - adversarial-tempo-advantage
  - team-persistence
  - directed-separation
  - discussion-identifiability-floor
stage: draft
---

# Derived: Agent Opacity ($H_b$)

Alongside AAD's heavily formalized *forward* observation quality (how well the agent sees the world — observation ambiguity, model-class fitness, identifiability floor on what the agent can infer), AAD carries a **dual quantity** measuring how well the world sees the agent: **backward predictive uncertainty $H_b$**, an observer-indexed, horizon-indexed, trajectory-indexed entropy of the agent's future actions given another agent's filtration. Adopted from Hafez et al. 2026 as a first-class multi-agent quantity. $H_b$ is the dual of observation quality $U_o$: where $U_o$ characterizes how well the agent sees the world, $H_b$ characterizes how well the world sees the agent. It is **sign-flipped in value across regimes**: low $H_b$ (legibility) enables cooperative coordination ( #team-persistence); high $H_b$ (opacity) enables adversarial effectiveness ( #adversarial-destabilization, #adversarial-tempo-advantage). The sign-flip is a direct consequence of AAD's existing signed-coupling structure rather than a separate posit. This segment's emitter-side four-regime classification is the dual of `#interaction-channel-classification`'s recipient-side theory; together they close `#adversarial-edge-targeting` as emitter-optimizer paired with recipient-classifier.

## Formal Expression

*[Definition (agent-opacity-Hb)]*

For agent $A$ on singular trajectory $\mathcal C_A$ and observer agent $B$ with filtration $\mathcal F_B^t$ (per-trajectory observable history per `#agent-identity`'s token-level commitment):

$$H_b^{A \mid B}(t, \tau) := H(a_{A, t+\tau} \mid \mathcal F_B^t)$$

the entropy of agent $A$'s action at horizon $\tau$ conditional on observer $B$'s filtration at time $t$. **Four indexing arguments:** observer $B$, time $t$, horizon $\tau$, trajectory $\mathcal C_A$. Each is load-bearing:

- **Observer-indexed.** Different observers (allies with shared infrastructure; adversaries with limited instrumentation; environment itself) have different filtrations $\mathcal F_B^t$; $H_b$ varies accordingly.
- **Horizon-indexed.** Immediate-next-action opacity ($\tau = 1$) and long-horizon-plan opacity ($\tau \gg 1$) decouple: an agent may be predictable at immediate action but unpredictable at plan level, or vice versa.
- **Trajectory-indexed.** Per `#agent-identity`, AAD applies to agents on singular trajectories. $H_b^{A\mid B}$ is the opacity of *this* trajectory's continuation, not a type-level claim.
- **Time-indexed.** Opacity may drift with learning (as $B$'s model of $A$ improves, $H_b^{A\mid B}(t)$ decreases); steady-state values exist for ergodic regimes.

Under the IDT-observer specialization — $B$ operates as Hafez's Information Digital Twin monitoring $(S_A, a_A, S'_A)$ from outside $A$'s processing — and under ergodicity, $H_b^{A\mid B}(t, \tau) \to H(S, A \mid S')$ as defined in Hafez et al. 2026. AAD's added features (observer-indexing, horizon-indexing, trajectory-indexing) are the distinctive extensions.

### Sign-flip via signed coupling

*[Derived (sign-flip-from-signed-coupling)]*

The value of $H_b^A$ *to $A$* depends on the sign of $A$'s coupling to other agents — the same signed-coupling structure that organizes `#team-persistence`, `#adversarial-destabilization`, and `#critical-mass-composition`'s (CM2) $\gamma$ parameter.

- **Cooperative coupling ($\gamma^{\text{coop}} \gt 0$, reducing allies' disturbance).** For $B$ to treat $A$'s action as cooperation rather than disturbance, $B$ must predict $A$'s action well enough to preempt or complement it. Under `#interaction-channel-classification`'s recipient-side decomposition, unpredictable ally actions fall into Regime II (magnitude/structural shock) rather than Regime I (informative update). Therefore cooperative coupling effectiveness $\gamma_{A \to B}^{\text{coop}}$ is *increasing in legibility*, equivalently decreasing in $H_b^{A\mid B}$. Under sub-scope $\alpha$ Gaussian coupling: $\gamma^{\text{coop, effective}} \propto (1 - H_b^{A\mid B}/H_b^{\max})$.
- **Adversarial coupling ($\gamma^{\text{adv}} \gt 0$, amplifying target's disturbance).** Predicted attacks are neutralized; unpredicted attacks deliver effective disturbance. Adversarial coupling effectiveness is *increasing in opacity* — the mechanism of adversarial advantage (per `#adversarial-tempo-advantage`) operates *through* $B$'s failure to predict $A$. Under the same sub-scope $\alpha$ setup: $\gamma^{\text{adv, effective}} \propto H_b^{A\mid B}/H_b^{\max}$.

**The sign-flip on $H_b$'s value-to-$A$ lives in the sign of $\gamma$ itself, not in a different sign on $H_b$.** Cooperative regime $(\gamma^{\text{coop}} \gt 0)$ rewards low $H_b$; adversarial regime ($\gamma^{\text{adv}} \gt 0$) rewards high $H_b$. The same $H_b$ quantity, the same monotone dependence; opposite value-to-$A$ because the signs of the coupling terms differ.

### Emitter-side four-regime classification

*[Formulation (emitter-regimes, dual to #interaction-channel-classification)]*

Parallel to `#interaction-channel-classification`'s recipient-side four regimes, the emitter $A$ sends events that fall into four emitter-side regimes based on $A$'s opacity signal structure and self-model quality:

- **E-I Broadcast.** $A$ emits actions transparently; $H_b^{A\mid B}$ is low for any observer $B$ with standard instrumentation. Examples: public announcements, published decisions, legible industrial controllers.
- **E-II Selective-signal.** $A$ is transparent to some observers and opaque to others (e.g., shared allied infrastructure gives allies lower $H_b$ than adversaries without that infrastructure). Boundary: differential instrumentation in $\mathcal F_B^t$ across observers.
- **E-III Information-hide.** $A$ is uniformly opaque to observers; actions are randomized, encrypted, or routed through dead-drops. $H_b^{A\mid B}$ near $H_b^{\max}$ for all observers lacking the key / pattern / channel.
- **E-IV Active-deceive.** $A$ emits actions that mispredict — the observer's model of $A$ converges to a *wrong* prediction that differs from the actual action by a larger margin than the same observer's model of the environment would accommodate. Boundary: $A$'s self-model quality (for active-deceive, $A$ must model the observer's model of $A$ well enough to choose actions that exploit it).

The 16-cell emitter-recipient composition (four emitter regimes × four recipient regimes) gives a closed-form *adversarial-targeting arg-max* under `#adversarial-edge-targeting`: the most-valuable-to-attack edge is the one where the product of emitter's opacity-to-target and target's vulnerability-to-shock is maximized. This closes the Section III gap that `#adversarial-edge-targeting` (previously GAP) was reserved for; the segment is now operationalized with targeting-fidelity factor $(1 - H_b^{B\mid A}/H_b^{\max})$ from $A$'s self-model quality plus the four-regime recipient classification from `#interaction-channel-classification`.

### Tempo amplification by opacity

*[Derived (tempo-amplification-by-opacity)]*

`#adversarial-tempo-advantage`'s tempo-multiplier $\gamma_A \mathcal T_A$ in `#adversarial-destabilization` decomposes into a tempo term and an opacity term:

$$\mathcal T_A^{\text{effective}} = \mathcal T_A \cdot \frac{H_b^{A\mid B}}{H_b^{\max}} \quad \text{(Model D adversarial coupling)}$$

The superlinear formula $(\mathcal T_A / \mathcal T_B)^2$ becomes $(\mathcal T_A / \mathcal T_B)^2 \cdot (H_b^{A\mid B} / H_b^{B\mid A})^2$ under bilateral opacity — a higher-order tensor product with the same exponent $b = 2$ (Model D) or $b = 3/2$ (Model S) from `#adversarial-exponent-regimes`. Whether $b$ itself is reshaped under bilateral opacity is open; the leading-order scaling is the tempo-opacity product.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| $H_b^{A\mid B}(t, \tau)$ definition | Adopted from Hafez et al. 2026; extended with observer / horizon / trajectory indexing per `#agent-identity` | Formulation choice (adoption + AAD-extension) |
| Reduction to Hafez's $H(S, A \mid S')$ under IDT-observer + ergodic regime | Direct substitution | Derived (exact under IDT + ergodicity) |
| Sign-flip via signed coupling | Cooperative coupling requires predictability (allies preempt); adversarial coupling operates via disturbance-injection (predicted attack is neutralized) | Derived (from existing `#team-persistence` + `#adversarial-destabilization` signed-$\gamma$ structure) |
| Emitter-side four-regime classification | Dual construction to `#interaction-channel-classification`'s recipient-side four regimes | Formulation choice |
| 16-cell emitter-recipient composition closes `#adversarial-edge-targeting` | Product of emitter opacity × recipient vulnerability-to-shock over four × four cells | Derived (arg-max construction) |
| Tempo-amplification leading-order: $\mathcal T^{\text{eff}} = \mathcal T \cdot H_b/H_b^{\max}$ | First-order substitution into `#adversarial-tempo-advantage`'s tempo-multiplier under Model D | Derived (conditional on Gaussian-coupling sub-scope $\alpha$) |
| Parameterization-invariance of $H_b$ | $H_b$ is an action-marginal entropy; action space is coordinate-free per `#agent-identity` | Derived |
| Candidate 4th `#discussion-identifiability-floor` instance (generic observer-side form) | $H_b$'s formal structure — "observer cannot predict agent's future action better than $H_b^{A\mid B}$" — is a CHT-style no-go at the observer-side-inference task | Discussion-grade (framing; precise external theorem not yet identified) |
| Candidate opacity ladder for `#discussion-separability-pattern` | Transparent-core / partial-transparency / full-opacity across observer filtrations | Formulation choice (ladder proposal) |
| Effects-spiral opacity amplification (higher $H_b$ → higher $\gamma_A$ → larger $\dot V_B$ → $B$'s actions become more erratic → observer's model of $B$ degrades → higher $H_b^{B\mid A}$) | Composition of sign-flip derivation with `#adversarial-destabilization`'s effects spiral | Sketch (discussion-grade; specific functional form open) |
| Dual-filtration apparatus (each agent's $M_t$ carries an other-filtration as feature) | Would unify observer-indexing with `#agent-identity`'s single-trajectory formalism more tightly | Open extension (mild architectural, orthogonal to derivations) |
| Sharp functional form for $\gamma^{\text{adv}}_{\text{effective}} = f(H_b)$ | Leading-order: $\gamma \propto H_b$. Exact function depends on sub-scope — Gaussian-coupling linear; sigmoid-coupling saturating | Open per sub-scope |

## Epistemic Status

*Conditional.* Max attainable: *exact* for the Hafez-reduction under IDT + ergodicity; *derived* for the sign-flip via signed-coupling; *formulation choice* for the emitter-regime classification structure; *conditional* for the tempo-amplification formula; *discussion-grade* for the meta-pattern candidate status.

**Load-bearing:**
- The sign-flip derivation from existing signed-$\gamma$ structure is the segment's core structural contribution — the adversarial/cooperative opacity duality is not a separate posit; it falls out of AAD's existing signed-coupling apparatus.
- The emitter-side four-regime classification is a clean dual to `#interaction-channel-classification`; its derivation is parallel (boundaries in AAD-native quantities — emitter opacity signal structure, self-model quality, coupling regime).
- The closure of `#adversarial-edge-targeting` via the 16-cell composition is a derived arg-max; the previously-stated GAP is filled.

**Not established:**
- Sharp functional forms for $\gamma^{\text{adv}}_{\text{effective}}(H_b)$ outside Gaussian-coupling sub-scope $\alpha$.
- Whether $b$ (the adversarial exponent from `#adversarial-exponent-regimes`) is reshaped under bilateral opacity.
- Formal fourth `#discussion-identifiability-floor` instance (requires external-theorem anchoring not yet identified); discussion-grade framing only.
- The effects-spiral's opacity amplification (composition with `#adversarial-destabilization`'s spiral) is sketch-level.

## Honest Limits

- **Observer-indexing under complex information structures.** $\mathcal F_B^t$ may include shared memory, cryptographic keys, insider knowledge, or partial access to $A$'s internal state. Enumerating all relevant observer-filtration structures for a specific application is task-specific; the segment provides the formal framework, not the per-instance enumeration.
- **Active-deceive (E-IV) requires $A$ to model $B$'s model of $A$.** Mutual-modeling regress under partially-opposing objectives connects to `#strategic-composition`'s joint-Jacobian analysis. Active-deceive is formally reachable only when $A$'s Class 1/2/3 architecture admits modeling another agent's model — typically Class 2 (LLM-style) or Class 3 architectures.
- **Type-level vs token-level opacity.** $H_b$ is trajectory-indexed per `#agent-identity`. Statements about "the opacity of model X" (aggregated across deployments) are type-level claims outside AAD's formal scope; they require additional machinery (e.g., population-level dynamics per Section III gaps).

## Discussion

**Dual to observation quality.** $U_o$ characterizes how well the agent sees the world: observation noise, ambiguity, model-class fitness. $H_b$ characterizes how well the world sees the agent: predictability to observers. The duality is structural — both quantify information flow through the agent-environment boundary, in opposite directions. High $U_o$ agent (observes the world well) and low $H_b$ agent (is observed well) are independent properties; an agent can have one without the other.

**Closing `#adversarial-edge-targeting`.** The segment provides the emitter-side arg-max structure missing from the Section III adversarial machinery. Paired with `#interaction-channel-classification`'s recipient-side four-regime decomposition, the full adversarial-targeting problem has a closed-form: choose edges where emitter's $H_b$ (to target) and target's recipient-side vulnerability (Regime II magnitude/structural shock) are jointly maximized. This operationalizes what "inside the opponent's loop" means at the targeting layer — Boyd's aphorism becomes an explicit optimization over the 16-cell emitter-recipient product.

**Meta-pattern positioning.**
- *`#discussion-identifiability-floor`:* $H_b$'s structure suggests a generic observer-side floor — "the observer cannot predict the agent's action better than $H_b$" — that Instances 1/2/3 specialize on specific variables (causal structure / mixture parameters / coupling sign). The generic framing is candidate-status: it lacks a single external-theorem anchor clear enough to match F1's CHT or F13's Cramér-Rao, but $H_b$ appears naturally in Instance 3's coupling-sign unidentifiability and in Instance 1's on-policy detection no-go (an observer watching the agent's on-policy play has non-zero $H_b$ on the agent's interventional regime).
- *`#discussion-separability-pattern`:* candidate opacity ladder — transparent-core (E-I Broadcast; allies / public interfaces) / structured-repair (E-II Selective-signal; trust-weighted partial instrumentation) / general-open (E-III, E-IV; uniformly opaque or active-deceive). Adds to the ladder count if adopted.
- *`#discussion-additive-coordinate-forcing`:* $H_b$'s logarithmic form is adopted from Shannon via Khinchin-Aczél axiomatics, imported as an applied external theorem rather than re-forced under an AAD-internal additivity axiom. Cross-agent additivity fails under the coupling regimes AAD cares about (correlated opacity structures break independence). Adjacent family member, parallel to the IB Lagrangian's position — not a primary instance.

**Parameterization-invariance composes cleanly.** $H_b$ is an action-marginal entropy. Under `#agent-identity`'s (PI) axiom, the action space is coordinate-free; $H_b$ is invariant under change of the agent's internal-state parameterization. This composes with the (PI)/Čencov fourth primary instance of `#discussion-additive-coordinate-forcing` without adding a new axiom.

**Relation to `#directed-separation`.** Class 2 (fully merged) agents have high structural opacity to any observer without internal access — their $f_M$ and $G_t$ are entangled, so predicting the next action requires joint state modelling. Class 1 (modular) agents are more transparent at the interface level because the decomposed update admits separate modelling of epistemic vs. purposeful components. $H_b$ therefore tends to be *architecturally higher* for Class 2 agents — a structural consequence of architecture rather than choice, beyond what E-III Information-hide captures.

**Hafez integration note.** The IDT pattern (Hafez et al. 2026) uses bi-predictability $P$ (how well a sidecar observer can predict the agent's next state-action) and entropy change $\Delta H$ as diagnostics. The IDT's reported 89% perturbation-detection accuracy (vs. 44% for reward-based monitoring) operates on the Level-2 structure per `#loop-interventional-access`. In AAD terms, the IDT is a low-$H_b$-preserving observation channel — its presence as a modular sidecar reduces $H_b$ for the operator without increasing the agent's internal complexity. For `03-logogenic-agents/`, this validates that modular monitoring of internally-merged agents is feasible and effective even when the agent itself is architecturally Class 2.

## Working Notes

- The (C-iv) scope route of `#scope-composite-agent` accommodates adversarial composition via equilibrium convergence; the effects-spiral joint-Jacobian eigenvalue condition of `#strategic-composition` composes with this segment's opacity-amplification story to give a fully-coupled picture of symmetric adversarial dynamics. Full composition is open work.
- Candidate fourth-instance formalization for `#discussion-identifiability-floor`: the most natural external-theorem anchor is Fano's inequality (relating $H_b$ to error-probability lower bounds) applied to the observer-side prediction task. Open; not pursued here.
- The 16-cell emitter-recipient composition admits closed-form arg-max only under sub-scope $\alpha$ coupling; general non-convex coupling requires per-case optimization.
- Dual-filtration apparatus ($M_A$ carries $\mathcal F_B^t$ as feature, $M_B$ carries $\mathcal F_A^t$ as feature) would tighten the formalism by unifying observer-indexing with the single-trajectory scope of `#agent-identity`. Architecturally clean; not needed for the derivations here.
