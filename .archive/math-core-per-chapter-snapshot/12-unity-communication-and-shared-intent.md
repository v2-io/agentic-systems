# Unity, Communication, and Shared Intent


## Definition: Unity Dimensions

- **Slug**: `def-unity-dimensions`
- **Type**: definition
- **Status**: discussion-grade
- **Stage**: draft
- **Depends**: `scope-multi-agent`, `form-composition-closure`, `form-agent-model`, `def-strategy-dimension`

The quality of a composite agent's composition — *conditional on #scope-composite-agent being satisfied via at least one of its four routes (three alignment routes + the strategic-equilibrium route (C-iv))* — is parametrized along **two architecturally distinct axes**:

- **Content axis (four unity dimensions).** What the sub-agents *share*: epistemic ($U_M$, shared model), teleological ($U_O$, shared objective), strategic ($U_\Sigma$, coordinated action), and perceptual ($U_{\text{obs}}$, shared observations).
- **Structural axis (update-rule homogeneity, $U_f$).** Whether sub-agents implement the *same* correction rule: how similar their $f_M$ updates are across the population.

Together, the two axes parametrize the rate-distortion curves for the component closure defects ( #form-composition-closure, #result-unity-closure-mapping). Higher unity along either axis permits more aggressive compression at lower closure defect; neither axis alone is sufficient. In pure Section I composition (passive estimators, no $G_t$), agents with identical content can still produce non-zero $\varepsilon_x$ if their update rules differ — the content axis cannot detect this, which is why the structural axis is required. Unity (in either sense) does not directly predict closure-defect magnitude; it controls the compressibility of the corresponding state, observation, or action component under projection.

**Scope.** The decomposition applies to composites that satisfy #scope-composite-agent. $U_O$ plays a role in the (C-i) route of the scope condition via value-correlation, but the scope condition is a disjunction of four routes — three alignment routes (shared objective, hierarchical derivation, mutual benefit) plus the strategic-equilibrium route (C-iv) — not a scalar threshold on $U_O$. Below scope-satisfaction (no route applies), the sub-agents are a multi-agent system per #scope-multi-agent and composition-level quantities are not well-defined.

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

---



## Result: Unity-to-Closure Rate-Distortion Mapping

- **Slug**: `result-unity-closure-mapping`
- **Type**: result
- **Status**: conditional
- **Stage**: draft
- **Depends**: `def-unity-dimensions`, `form-composition-closure`, `form-information-bottleneck`

Unity dimensions parametrize rate-distortion curves for closure-defect components, not point-valued predictors. The achievable closure-defect component $\varepsilon_d$ under projection of macro-dimension $k_d$ is monotone decreasing in both the relevant content unity $U_d$ and the structural unity $U_f$ (update-rule homogeneity), with higher unity along either axis lowering achievable defect at a given compression. Closed forms hold in the linear-Gaussian case; structural monotonicity survives more broadly. The two-axis structure (content $\times$ structure) is forced by the heterogeneous-Kalman case below and is reflected definitionally in #def-unity-dimensions.

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

---



## Definition: Shared Intent

- **Slug**: `def-shared-intent`
- **Type**: definition
- **Status**: discussion-grade
- **Stage**: draft
- **Depends**: `def-unity-dimensions`, `form-information-bottleneck`, `form-objective-functional`

When sub-agents within a composite must coordinate, they face a communication problem: transmitting the full objective $O_t$ and strategy $\Sigma_t$ is expensive (high bandwidth, high latency), but acting without any shared purpose wastes coordination potential. The Information Bottleneck ( #form-information-bottleneck) applied to inter-agent communication predicts an optimal compression: transmit enough of $G_t$ to align behavior, not more.

*[Definition (shared-intent)]*

Let $G_t^{\text{full}}$ be the source agent's complete purposeful state $(O_t, \Sigma_t)$. Let $G_t^{\text{shared}}$ be the compressed representation communicated to partners. The shared intent is the IB-optimal compression:

$$G_t^{\text{shared}} = \arg\min_{G_s} \left[ I(G_t^{\text{full}}; G_s) - \beta \cdot I(G_s; a_t^{\text{coordinated}}) \right]$$

where $a_t^{\text{coordinated}}$ is the jointly optimal action and $\beta$ controls the complexity-relevance tradeoff. At high $\beta$, the agent communicates more detail (approaching full model sharing). At low $\beta$, communication is minimal (approaching independent action).

The shared intent is the *minimal sufficient statistic* of the sender's purposeful state for predicting the jointly optimal coordination behavior.

---



## Hypothesis: Auftragstaktik Principle

- **Slug**: `hyp-auftragstaktik-principle`
- **Type**: hypothesis
- **Status**: discussion-grade
- **Stage**: draft
- **Depends**: `def-shared-intent`, `def-unity-dimensions`, `def-adaptive-tempo`

For a composite agent with limited communication bandwidth, the optimal allocation prioritizes sharing objectives over strategies over models. This captures the structural insight of Auftragstaktik (mission-type tactics): investing communication bandwidth in shared purpose (teleological unity) while accepting lower epistemic and strategic unity, granting sub-agents autonomy to adapt locally. The model predicts the same priority ordering that military doctrine discovered empirically; whether the mechanism (IB-optimal bandwidth allocation) is the actual reason Auftragstaktik works is an open question.

*[Hypothesis (auftragstaktik-principle)]*

Let a composite agent's total inter-agent communication bandwidth be $B = B_O + B_\Sigma + B_M$, allocated across objective sharing ($B_O$), strategy coordination ($B_\Sigma$), and model synchronization ($B_M$).

The hypothesis: the allocation that maximizes composite tempo $\mathcal{T}_c$ (or equivalently, minimizes coordination overhead $C_{\text{coord}}$) prioritizes:

$$B_O \gt B_\Sigma \gt B_M$$

when:
- Objectives change slowly relative to strategies: $\nu_O \ll \nu_\Sigma$
- Strategies change slowly relative to models: $\nu_\Sigma \ll \nu_M$
- Sub-agents have sufficient local adaptive capacity: each $\mathcal{T}_i \gt \rho_i^{\text{local}} / \Vert\delta_{\text{critical}}^i\Vert$

The priority ordering follows from the IB framework ( #def-shared-intent): the bits with the longest shelf life and highest coordination value per bit should be transmitted first. Objectives change slowly and enable autonomous coordination (sub-agents who share objectives can independently choose compatible strategies). Models change fast and provide diminishing coordination value (two agents with the same model but different objectives still conflict).

---



## Hypothesis: Communication Gain

- **Slug**: `hyp-communication-gain`
- **Type**: hypothesis
- **Status**: discussion-grade
- **Stage**: draft
- **Depends**: `emp-update-gain`, `scope-multi-agent`

When an agent incorporates information from another agent (rather than from direct observation), the optimal update gain extends the uncertainty ratio with additional terms for source quality and teleological-unity uncertainty.

*[Hypothesis (communication-gain)]*

$$\eta_{ji}^* = \frac{U_{M_i}}{U_{M_i} + U_{o,ji} + U_{\text{src},j} + U_{\text{align},ji}}$$

where:
- $U_{M_i}$: agent $i$'s model uncertainty (same as #emp-update-gain)
- $U_{o,ji}$: **communication channel noise** — latency, ambiguity, compression loss, bandwidth limitations of the channel between $j$ and $i$
- $U_{\text{src},j}$: **source quality uncertainty** — $i$'s uncertainty about $j$'s model calibration and domain competence
- $U_{\text{align},ji}$: **teleological-unity uncertainty** — $i$'s uncertainty about whether $j$'s communications serve $i$'s interests or $j$'s potentially conflicting objectives

When all additional terms are zero (perfect channel, calibrated and aligned source): $\eta_{ji}^\ast \to 1$ (full trust). When any term is large: $\eta_{ji}^\ast \to 0$ (ignore the signal).

**Connection to single-agent case.** When $j$ is the environment (direct observation): $U_{\text{src}} = U_{\text{align}} = 0$, recovering #emp-update-gain's standard form $\eta^\ast = U_M / (U_M + U_o)$.

---
