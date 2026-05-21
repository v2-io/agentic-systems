# Cluster Reference: Agency Dimensions and Social Threshold

**Overview:** Formalizes the dimensions of coherence (unity) between agents and the threshold at which independent agents cross into composite social behavior.

---

## Canonical Source Segments

### Source: `def-unity-dimensions.md`

```yaml
---
slug: def-unity-dimensions
type: definition
status: discussion-grade
depends:
  - scope-multi-agent
  - form-composition-closure
  - form-agent-model
  - def-strategy-dimension
stage: draft
---
```


# Definition: Unity Dimensions

The quality of a composite agent's composition — *conditional on #scope-composite-agent being satisfied via at least one of its four routes (three alignment routes + the strategic-equilibrium route (C-iv))* — is parametrized along **two architecturally distinct axes**:

- **Content axis (four unity dimensions).** What the sub-agents *share*: epistemic ($U_M$, shared model), teleological ($U_O$, shared objective), strategic ($U_\Sigma$, coordinated action), and perceptual ($U_{\text{obs}}$, shared observations).
- **Structural axis (update-rule homogeneity, $U_f$).** Whether sub-agents implement the *same* correction rule: how similar their $f_M$ updates are across the population.

Together, the two axes parametrize the rate-distortion curves for the component closure defects ( #form-composition-closure, #result-unity-closure-mapping). Higher unity along either axis permits more aggressive compression at lower closure defect; neither axis alone is sufficient. In pure Section I composition (passive estimators, no $G_t$), agents with identical content can still produce non-zero $\varepsilon_x$ if their update rules differ — the content axis cannot detect this, which is why the structural axis is required. Unity (in either sense) does not directly predict closure-defect magnitude; it controls the compressibility of the corresponding state, observation, or action component under projection.

**Scope.** The decomposition applies to composites that satisfy #scope-composite-agent. $U_O$ plays a role in the (C-i) route of the scope condition via value-correlation, but the scope condition is a disjunction of four routes — three alignment routes (shared objective, hierarchical derivation, mutual benefit) plus the strategic-equilibrium route (C-iv) — not a scalar threshold on $U_O$. Below scope-satisfaction (no route applies), the sub-agents are a multi-agent system per #scope-multi-agent and composition-level quantities are not well-defined.

## Formal Expression

*[Definition (definition-unity-dimensions)]*

For a composite agent $A_c$ composed of sub-agents $\{A_1, \ldots, A_n\}$, the unity profile consists of *four content dimensions* (this section, below) and *one structural dimension* ($U_f$, defined after the content dimensions).

### Content dimensions

**Epistemic unity** $U_M$ — how much of the reality model is shared:

$$U_M = \frac{I(M_t^{(1)}; \ldots; M_t^{(n)})}{H(M_t^{(1)}, \ldots, M_t^{(n)})}$$

The fraction of total model information that is shared (multi-information / total-correlation ratio). $U_M = 1$ for identical models; $U_M = 0$ for independent models.

**Teleological unity** $U_O$ — how aligned are the objectives:

$$U_O^{(i,j)} = \text{corr}\!\left(V_{O_t^{(i)}}(\tau),\; V_{O_t^{(j)}}(\tau)\right)$$

over trajectories the composite encounters. $+1$ for identical objectives; $-1$ for perfectly opposed; $0$ for orthogonal. The composite teleological unity is an aggregation over all pairs. The scalar ranges from fully cooperative to fully adversarial per objective dimension.

*[Scope note]* $U_O$ plays a role in #scope-composite-agent — primarily along route (C-i), where value-correlation is the operationalization of teleological alignment. The scope condition itself is disjunctive: it is satisfied when *any* of the alignment routes (C-i), (C-ii), (C-iii) applies, or when the strategic-equilibrium route (C-iv) applies; not by $U_O$ alone crossing a common scalar threshold. The quality-metric role of $U_O$ captured in this segment presumes scope-satisfaction via *some* route; on the (C-iv) side it tracks at best the alignment projection of a strategic composite whose macro-state is defined by equilibrium structure rather than by a shared target. When the sub-agents fail all four routes, they form a multi-agent system ( #scope-multi-agent) but not a composite, and composition-level quantities (closure defect, composite tempo, team persistence) are not well-defined.

**Strategic unity** $U_\Sigma$ — how coordinated is the joint policy:

*[Discussion]*

$$U_\Sigma = 1 - \frac{D_{\text{KL}}(\pi^c_{\text{actual}} \Vert \pi^c_{\text{optimal}})}{D_{\text{KL}}(\pi^c_{\text{independent}} \Vert \pi^c_{\text{optimal}})}$$

where $\pi^c_{\text{optimal}}$ is the jointly optimal policy. $U_\Sigma = 1$ when actual matches optimal; $U_\Sigma = 0$ when actual matches independent (no coordination). Requires knowing the jointly optimal policy, which is itself a strong assumption.

**Perceptual unity** $U_{\text{obs}}$ — how much of the observation stream is shared:

The fraction of total observation information that reaches all sub-agents. Full perceptual unity means all agents observe the same signals; zero means private observations only. Enables epistemic convergence without explicit model-sharing.

### Structural dimension

**Update-rule homogeneity** $U_f$ — how similar the sub-agent update rules are:

*[Definition]*

$$U_f = 1 - d\!\left(f_M^{(1)}, \ldots, f_M^{(n)}\right)$$

where $d$ is a distance over the space of update operators $f_M : (M, o, a) \mapsto M'$, normalized so that $U_f = 1$ when all sub-agents implement the same correction rule and $U_f = 0$ at maximal heterogeneity. The choice of $d$ is case-specific — for parametric Kalman-like updates, $d \propto \lvert\Delta K\rvert / K_{\max}$ on the gain parameter; for Bayesian updates with shared structural form but different priors, $d$ tracks divergence between the induced kernels; for arbitrary $f_M$ in function space, candidates include operator-norm distance, Fisher-information-weighted distance, or IB-style comparison.

*[Discussion]*

Where the four content unities measure shared *information* across sub-agents (state, objective, policy, observation), $U_f$ measures shared *structure* — whether the agents instantiate the same update law. The two axes are independent: agents can share a model ($U_M = 1$) while updating it differently ($U_f \lt 1$), and conversely. In purposeful settings ($G_t$ present), $U_\Sigma$ partially absorbs structural variation in the policy half of the cycle, but the model-update half remains uncovered without $U_f$. In pure Section I composition (passive estimators, no $G_t$), $U_f$ is the only handle on structural homogeneity. The closed-form linear-Gaussian instance — heterogeneous Kalman gains $\Delta K = K_1^\ast - K_2^\ast$ producing $\varepsilon_x \propto \lvert\Delta K\rvert$ — is derived in #result-unity-closure-mapping §Two-axis structure.

### Joint role in closure defect

The achievable component closure defect $\varepsilon_d^{\min}(k_d)$ under a projection of macro-dimension $k_d$ is a function of *both* axes — the relevant content unity $U_d$ and the structural unity $U_f$ — together with the projection-dimension parameter:

$$\varepsilon_d^{\min}(k_d) = f_d\!\left(k_d;\; U_d,\; U_f\right)$$

monotone decreasing in each unity argument and monotone increasing in compression aggressiveness (smaller $k_d$). The form is derived in #result-unity-closure-mapping; in linear-Gaussian scalar cases it admits closed-form expressions for $d \in \{x, o, a\}$. $U_O$ and $U_\Sigma$ enter $\varepsilon_a$ jointly rather than separately.

## Epistemic Status

*Discussion-grade.* Max attainable: empirical. The four content dimensions are qualitatively motivated by correspondence with the four components of agent state ($M_t$, $O_t$, $\Sigma_t$, and the observation channel); the structural dimension $U_f$ is forced by the linear-Gaussian two-Kalman case ( #result-unity-closure-mapping §Two-axis structure), where heterogeneous gains produce non-zero $\varepsilon_x$ that no content dimension can register. The two-axis architecture (content $\times$ structure) is therefore a definitional commitment of this segment, not a heuristic.

The specific metrics are sketches. The information-theoretic formulations ($U_M$, $U_\Sigma$) are well-defined in principle but require specifying distributions and distance measures for practical computation. $U_f$ is even less prescriptive — the choice of operator distance $d$ is case-specific, and a general theory of structural-variation measures across arbitrary $f_M$ classes is open.

The claim that the dimensions are *substantially independent* is a hypothesis, not derived. Epistemic unity may enable strategic unity (shared models allow coordination without explicit planning); content unity along $U_M$ does not constrain $U_f$ (agents can share a posterior while updating it differently). Independence holds approximately, with documented joint dependencies: $(U_O, U_\Sigma)$ jointly control $\varepsilon_a$ and cannot be separated; $U_f$ enters all three closure components ($\varepsilon_x, \varepsilon_o, \varepsilon_a$) as a structural multiplier on what content unity alone would predict.

## Discussion

**Clausewitz's three gaps.** These dimensions map to the gaps identified by Clausewitz (systematized by Bungay in *The Art of Action*):

| Clausewitz Gap | Unity Dimension | Formal Quantity |
|---|---|---|
| Knowledge gap | Epistemic unity ($U_M$) | $1 - U_M$: fraction of model not shared |
| Alignment gap | Teleological unity ($U_O$) | $1 - U_O$: objective misalignment |
| Effects gap | Strategic + Perceptual unity | $1 - U_\Sigma$ + observation routing costs |

The mapping is not perfect — Clausewitz's "effects gap" blends action coordination with observation feedback — but it provides 200+ years of organizational evidence for the qualitative decomposition.

**Connection to closure defect.** The unity dimensions parametrize a rate-distortion relation with the component closure errors in #form-composition-closure, not a direct correspondence. The formal statement is in #result-unity-closure-mapping: the achievable closure-defect component $\varepsilon_d(k_d)$ under a projection of macro-dimension $k_d$ decreases monotonically in both the relevant content unity $U_d$ and the structural unity $U_f$, with closed-form expressions in the linear-Gaussian case. Qualitative direction along the content axis: $U_M$ governs the compressibility of state information ($\varepsilon_x$), $(U_O, U_\Sigma)$ jointly govern action compressibility ($\varepsilon_a$), $U_{\text{obs}}$ governs observation compressibility ($\varepsilon_o$). The naive reading "high $U_d$ predicts low $\varepsilon_d$" fails: for non-compressing projections (e.g., the means-only projection in the two-Kalman case) $\varepsilon_x = 0$ regardless of $U_M$, while for heterogeneous-gain projections $\varepsilon_x \gt 0$ even at perfect content correlation. Both observations point at the same correction — closure defect lives on a rate-distortion surface with two unity arguments, not a single one.

**What each dimension's absence costs.**

- Low $U_M$: prediction conflicts → uncoordinated actions based on contradictory beliefs. Internal mismatch component from model disagreement.
- Low $U_O$: strategic friction → sub-agents pursue conflicting sub-goals. Effort wasted or counterproductive.
- Low $U_\Sigma$: redundancy and gaps → two agents fix the same bug while a critical one goes unnoticed.
- Low $U_{\text{obs}}$: information silos → critical signals observed by one agent but not actionable by the composite.
- Low $U_f$: structural drift → even agents sharing identical models, objectives, observations, and policy targets produce divergent macro-trajectories under aggressive projection, because their corrections respond to the same evidence with different gains. The composite cannot be summarized at low macro-dimension without residual error scaling with the gain mismatch.

## Working Notes
- The independence of unity dimensions needs careful examination. High epistemic unity likely enables (but does not guarantee) high strategic unity — if agents share models, they can coordinate implicitly. The dimensions may be better described as "substantially independent inputs to a joint prediction of $\varepsilon^\ast$" rather than "independent properties." Independence between content axis and structural axis ($U_d \perp U_f$) is cleaner — content sharing and update-rule similarity are categorically distinct properties — but a formal proof is open.
- The specific metric formulations need testing on concrete cases (software team, military unit) to determine if they discriminate meaningfully between well-composed and poorly-composed groups.
- The teleological unity scalar per objective dimension ($+1$ to $-1$) captures mixed cooperative-competitive situations: a company can be cooperative on product quality and competitive on internal resource allocation simultaneously.
- **$U_f$ operator-distance choice is open.** The definition leaves $d$ case-specific. A general theory of structural-variation measures across arbitrary $f_M$ classes (operator-norm distance, Fisher-information-weighted distance, IB-style comparison) is unsettled. The linear-Gaussian Kalman case ($d \propto \lvert\Delta K\rvert / K_{\max}$) is the only worked closed form; non-Gaussian and non-linear cases are open follow-up work tracked in #result-unity-closure-mapping Working Notes.
- **Joint $(U_O, U_\Sigma) \to \varepsilon_a$ dependence.** State error tracks $U_M$; action error tracks *both* $U_O$ (target alignment) *and* $U_\Sigma$ (policy alignment); observation error tracks $U_{\text{obs}}$. The two dimensions jointly controlling action error are physically distinct: $U_O$ is about evaluation/preference agreement; $U_\Sigma$ is about execution-path agreement. Agents with identical objectives but different execution plans have high $U_O$, low $U_\Sigma$; agents coordinating on arbitrary shared routines have high $U_\Sigma$, low $U_O$. See #result-unity-closure-mapping for the quantitative relationship.
- **$U_O$ as scope vs. quality.** The scope role is in #scope-composite-agent as a disjunction of four routes (three alignment + one strategic-equilibrium) — $U_O$ is the value-correlation operationalization of route (C-i), not a universal scope variable. The quality-metric role remains here, presumed conditional on scope-satisfaction via at least one route. Open: whether the three alignment routes (C-i)–(C-iii) reduce to a single scalar is not established, and the strategic-equilibrium route (C-iv) is structurally distinct from any alignment-side aggregation, so "scope-satisfaction" and "$U_O$ value" should be treated as distinct concerns in downstream uses.


---

### Source: `result-unity-closure-mapping.md`

```yaml
---
slug: result-unity-closure-mapping
type: result
status: conditional
depends:
  - def-unity-dimensions
  - form-composition-closure
  - form-information-bottleneck
stage: draft
---
```


# Result: Unity-to-Closure Rate-Distortion Mapping

Unity dimensions parametrize rate-distortion curves for closure-defect components, not point-valued predictors. The achievable closure-defect component $\varepsilon_d$ under projection of macro-dimension $k_d$ is monotone decreasing in both the relevant content unity $U_d$ and the structural unity $U_f$ (update-rule homogeneity), with higher unity along either axis lowering achievable defect at a given compression. Closed forms hold in the linear-Gaussian case; structural monotonicity survives more broadly. The two-axis structure (content $\times$ structure) is forced by the heterogeneous-Kalman case below and is reflected definitionally in #def-unity-dimensions.

## Formal Expression

### Rate-distortion framing (general)

*[Formulation (unity-rate-distortion)]*

Fix a composite agent satisfying the admissibility conditions (A1)-(A4) in #form-composition-closure. For each content unity dimension $U_d$ (with $d \in \{M, \Sigma, \text{obs}\}$, and $U_O$ contributing jointly with $U_\Sigma$ — see below) and the structural unity $U_f$ (update-rule homogeneity, defined in #def-unity-dimensions), the achievable component closure defect under a projection whose corresponding macro-dimension is $k_d$ satisfies:

$$\varepsilon_d^{\min}(k_d) = f_d\big(k_d;\; U_d,\; U_f\big)$$

where $f_d$ is monotone decreasing in both unity arguments, monotone increasing in aggressiveness of compression (smaller $k_d$). The mapping from unity to closure-defect *magnitude* is via the shape of this rate-distortion surface; unity does not directly predict closure-defect value. In the linear-Gaussian Kalman case the structural argument reduces to $1 - U_f \propto \lvert\Delta K\rvert / K_{\max}$ on the gain mismatch.

### Linear-Gaussian closed forms (two-agent scalar case)

*[Derived (obs-closure-linear-Gaussian, from unity-dimensions, composition-closure)]*

For two agents with scalar observations correlated at $\rho_{o,\text{eff}}$ (combining $\rho_{\text{env}}$ and $\rho_{\text{obs}}$), under 1D principal-component projection of observations, the minimum achievable observation closure defect is:

$$\varepsilon_o^2(k_o=1) = \sigma_o^2 \cdot \frac{1 - \rho_{o,\text{eff}}}{2} \;\propto\; 1 - U_{\text{obs}}$$

Higher perceptual unity → observations are more redundant → 1D summary suffices → $\varepsilon_o$ small. Exact in the linear-Gaussian scalar case.

*[Derived (action-closure-independent-policies, from unity-dimensions, composition-closure)]*

For two agents with scalar quadratic objectives, independent LQR policies ($\rho_\Sigma = 0$), scalar targets $r_1, r_2$ with correlation $\rho_O$, under 1D state projection, the minimum achievable action closure defect is:

$$\varepsilon_a^2 \propto \kappa^2 \cdot (1 - \rho_O) \;\propto\; \kappa^2 \cdot (1 - U_O)$$

where $\kappa$ is the scalar LQR gain. Adding policy coordination ($\rho_\Sigma \gt 0$) further reduces $\varepsilon_a$ through a multiplicative factor. The joint $(U_O, U_\Sigma)$ dependence takes the form:

$$\varepsilon_a^2 \propto (1 - U_O) \cdot f_1(U_\Sigma) + g(U_\Sigma)$$

with $f_1$ decreasing in $U_\Sigma$ and $g$ capturing residual strategic-misalignment error even when targets coincide.

### State closure in linear-Gaussian

*[Derived (state-closure-linear-Gaussian-trivial, from composition-closure)]*

For linear-Gaussian micro-dynamics with consistent linear projections $\Lambda_x$ and $\Lambda_o$ (the macro observation projection is the same linear combination as the macro state projection), the state closure defect vanishes:

$$\varepsilon_x = 0$$

regardless of $U_M$ or compression dimension. Linear projections of linear dynamics are exact *when the range of $\Lambda_x$ is invariant under the micro-dynamics matrix*. $\varepsilon_x$ becomes non-trivial when:

- the projection's range is non-invariant under the dynamics matrix — even with linear dynamics, consistent projections, and homogeneous updates, cross-coordinate coupling or anisotropic noise scales that mix macro-subspace components with their orthogonal complement give $\varepsilon_x \gt 0$ (the Mori-Zwanzig zero-lag bound $\varepsilon^\ast \geq \lVert Q_\Lambda U P_\Lambda \rVert_{\text{op}}$ in #form-composition-closure is the general expression of this obstruction),
- the projection is inconsistent (macro state and macro observation projections disagree),
- the micro-dynamics are nonlinear, or
- sub-agent update rules are heterogeneous (see Two-axis structure below).

### Two-axis structure (update heterogeneity)

*[Derived (two-axis-structure, from composition-closure, linear-Gaussian case)]*

In the non-degenerate linear-Gaussian case with heterogeneous sub-agent update rules — e.g., two Kalman filters with different gains $K_1^\ast \neq K_2^\ast$ tracking correlated processes, projected to the 1D sum $\hat\omega_+ = (\hat\omega_1 + \hat\omega_2)/\sqrt 2$ — the state closure defect has the closed form:

$$\varepsilon_x^2 = (\Delta K/2)^2 \big[S_- - C_{+-}^2 / S_+\big]$$

where $\Delta K = K_1^\ast - K_2^\ast$, $S_\pm$ are the innovation variances in the $\pm$ directions, and $C_{+-}$ is their cross-covariance.

This exhibits two independent drivers of $\varepsilon_x$, one along each unity axis of #def-unity-dimensions:

1. **Content unity** ($U_M$, via process correlation $\rho$): higher correlation → lower $\varepsilon_x$.
2. **Structural unity** ($U_f$, via gain mismatch $\Delta K$): when $\Delta K = 0$ (i.e., $U_f = 1$), $\varepsilon_x = 0$ at every $\rho$; when $\Delta K \neq 0$, $\varepsilon_x \gt 0$ even at perfect content correlation.

The four content unities measure shared information (goals, policies, observations, model state); $U_f$ measures whether sub-agents implement the same correction rule. The two axes contribute to the closure-defect rate-distortion surface independently — content unity controls compressibility of what the agents agree on; structural unity controls whether projection induces memory by mixing the discarded subspace into the retained one.

**Strategy-layer instance (credence composition).** The same structural-unity axis has an exact closed form one level up, at the strategy layer. For $N$ agents reasoning over a shared plan skeleton $(V,E)$ and disagreeing only on edge-credences, work in the log-odds coordinate $\lambda_{ij}=\log\tfrac{p_{ij}}{1-p_{ij}}$ — the unique additive-evidence coordinate ( #def-strategy-dag; forced by #deriv-edge-update-natural-parameter) in which edge updates are additive and the natural macro-projection is the log-odds centroid. The per-step closure defect is then driven by update-rule heterogeneity exactly as the Kalman case is, with the per-agent edge gains $\eta_{\Sigma,i}$ playing the role of the Kalman gains:

$$\varepsilon_\Sigma^{\ast 2} \;=\; \lvert E\rvert\cdot\overline{\mathrm{Var}_i[\eta_{\Sigma,i}]}\cdot\mathrm{Var}[r],$$

where $r$ is the per-edge evidence residual. This is the structural-unity ($U_f$) axis lifted from state to strategy: homogeneous gains ($\overline{\mathrm{Var}_i[\eta_{\Sigma,i}]}=0$, $U_f=1$) give $\varepsilon_\Sigma=0$; gain dispersion across agents drives the defect, scaled by plan size $\lvert E\rvert$ and evidence-residual variance. It is *dimension-free in $N$* — a population variance is estimated more precisely, not enlarged, by adding agents from the same gain-distribution — the strategy-layer twin of the dimension-free state-composition regime. The complementary heterogeneous-*topology* case (incompatible shared sub-orders, an order-theoretic non-existence rather than a magnitude) is the SCC-condensation defect landed in #def-strategy-dag's causal-abstraction composition subsection; the two together exhaust strategy-layer composition (credence axis here, topology axis there).

## Epistemic Status

*Conditional.* Max attainable: *exact* (linear-Gaussian scalar cases) to *robust qualitative* (general).

- The observation and action closed forms are *exact* in the linear-Gaussian scalar case with stated projection choices.
- The state closure form $\varepsilon_x^2 = (\Delta K/2)^2 [S_- - C_{+-}^2/S_+]$ is *exact* in the two-Kalman heterogeneous case.
- The strategy-layer credence-composition form $\varepsilon_\Sigma^{\ast 2} = \lvert E\rvert\cdot\overline{\mathrm{Var}_i[\eta_{\Sigma,i}]}\cdot\mathrm{Var}[r]$ is *exact* in the fixed-topology heterogeneous-credence case (log-odds additivity is forced by #deriv-edge-update-natural-parameter) and dimension-free in $N$.
- The rate-distortion framing (unity as compressibility parameter rather than direct predictor) is *robust qualitative* — it survives beyond linear-Gaussian, but concrete rate-distortion curves require case-by-case derivation.
- The joint $(U_O, U_\Sigma) \to \varepsilon_a$ formula is a *sketch* — the leading structure is derived; the precise forms of $f_1$ and $g$ are mechanical extensions not fully computed here.

Ceiling-limiting factors: non-Gaussian cases require information-theoretic bounds (Gaussian IB is fully tractable; general IB is not), and the structural-unity axis $U_f$ has worked closed forms in two cases — the linear-Gaussian Kalman gain-mismatch case (state layer) and the fixed-topology credence-composition case (strategy layer, via log-odds additivity) — while a general theory of $f_M$ structural variation across arbitrary update operators is open.

## Discussion

**Why a one-axis reading fails.** A "high $U_M$ predicts low $\varepsilon_x$" reading is wrong in the two-Kalman case with the standard means-only projection: $\varepsilon_x \equiv 0$ for every correlation value, irrespective of $U_M$. The closure-defect surface depends on the projection choice, on the content-unity axis, and on the structural-unity axis $U_f$ — high content unity with mismatched update rules still produces $\varepsilon_x \gt 0$, while low content unity under a non-compressing projection still produces $\varepsilon_x = 0$. The rate-distortion framing is what makes the multi-parameter dependence explicit.

**Connection to the Information Bottleneck ( #form-information-bottleneck).** The rate-distortion shape is not coincidental. Projection admissibility condition (P1) in #form-composition-closure is the Lagrangian-dual of the IB constraint: the projection sits on or above the IB frontier at rate $I(X; T) \leq I_{\max}(\epsilon_I)$ for the relevance variable "next observation given action" ( #disc-compression-operations supplies the derivation). Unity dimensions — measured as mutual-information-like quantities between sub-agent state components — parametrize the frontier's shape. The four AAT compression operations ($M_t$, $\Sigma_t$, shared intent, $\Lambda$) share IB shape but are not shown to reduce to a single master problem (U-medium, per #disc-compression-operations); cross-instance theorems do not follow from shared shape alone. (P2) Lipschitz continuity is not naturally IB and remains a separate admissibility condition; (P3) dimensional reduction remains separate in the Gaussian case. The Gaussian-IB closed form applies to linear-Gaussian composition setups; beyond them, the IB frontier is definitional but requires variational or numerical approximation.

**Two-axis structure.** The unity profile in #def-unity-dimensions decomposes into a content axis (four dimensions: $U_M$, $U_O$, $U_\Sigma$, $U_{\text{obs}}$) measuring shared information, and a structural axis ($U_f$) measuring shared correction rules. In purposeful-agent settings ($G_t$ present), $U_\Sigma$ already absorbs structural variation in the policy half of the cycle — agents with different action laws have different effective policies — but the model-update half remains uncovered without $U_f$. In pure Section I composition (passive estimators, no $G_t$), $U_f$ is the only handle on structural homogeneity, and the heterogeneous-Kalman case in this segment is the canonical instance where it bites.

**Interpretation of "low closure defect."** Unity controls the rate-distortion curve; low closure defect is achievable with aggressive compression when unity is high. But closure defect alone does not measure composite *optimality* (see #form-composition-closure §5.1): two independent Kalman filters can have $\varepsilon^\ast = 0$ (perfectly representable) while failing to exploit cross-correlations (suboptimal relative to a joint filter). The rate-distortion mapping is about representability, not optimality.

## Working Notes

- **Extension to nonlinear cases.** The framing is linear-Gaussian because that's where rate-distortion has closed forms. Extension to nonlinear micro-dynamics would likely show $\varepsilon_x \gt 0$ even with consistent projections (the identity-propagation argument in Formal Expression relies on linearity). Worth a follow-up spike.
- **Structural-unity formalization.** A quantitative measure $U_f$ across arbitrary $f_M$ functions (beyond the linear-Gaussian gain-mismatch closed form) is open. Candidates for the underlying operator distance: operator-norm distance in function space, Fisher-information-weighted distance, or IB-style comparison. See #def-unity-dimensions Working Notes.
- **Joint $(U_O, U_\Sigma)$ derivation.** The exact $f_1$ and $g$ functional forms require a full joint-LQR vs independent-LQR comparison. Mechanical but deferred.
- **$U_O$ → sector-constant pathway (partial via #deriv-critical-mass-composition).** The LQR-compatibility sketch $\gamma(U_O) = -\gamma_{\max}U_O$ in #deriv-critical-mass-composition §5.2 (flagged discussion-grade) is a structural complement to this segment's rate-distortion framing: it channels $U_O$ into the composite sector-constant $\kappa_c$ through the signed coupling $\gamma$ rather than through the closure defect $\varepsilon$. Upgrading (UO-mult) from discussion-grade to derived requires the action-space inner-product analysis natural to this segment: define the environment's action-coupling operator, show that LQR-linear policies produce cross-actions with inner product proportional to target correlation, and pin $\gamma_{\max}$ in terms of the quadratic objective's Hessian and the environment's coupling gain. Natural extension to the linear-Gaussian closed-form section above. *(Indexed: `spikes/PROPOSED.md` Tier 3 — "$U_O$ → sector-constant (UO-mult) derivation".)*
- **Mori-Zwanzig cross-check.** Under a stationary-measure setting, the Koopman-operator formulation of the projection-induced dynamics identifies the non-degenerate Kalman case as exercising the zero-lag memory kernel $K_0$ non-trivially, with $\lVert K_0 \rVert$ scaling with $\lvert\Delta K\rvert$. This is consistent with the two-axis finding here — a Mori-Zwanzig lower bound on $\varepsilon^\ast$ via the zero-lag kernel and the rate-distortion bound via IB should coincide at the same linear-algebraic quantity (the $L^2$ residual of projecting off an eigenspace of the micro-propagator). Formal equivalence not yet established. The MZ connection is developed further in #form-composition-closure Epistemic Status.
- **Relationship to #scope-composite-agent.** This segment describes quality *conditional* on composition existing — i.e., on #scope-composite-agent being satisfied via at least one of its three disjunctive routes (shared objective, hierarchical derivation, mutual benefit), *not* via a scalar $U_O$ threshold. The rate-distortion curves parametrize quality given scope-satisfaction; they do not address whether a composite exists at all. For multi-agent systems where no scope route applies, closure-defect quality talk is a category error — there is no composite whose closure defect to measure.


---

