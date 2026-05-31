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

# Result: Unity-to-Closure Rate-Distortion Mapping

Unity dimensions parametrize rate-distortion curves for closure-defect components, not point-valued predictors. The achievable closure-defect component $\varepsilon_d$ under projection of macro-dimension $k_d$ is monotone decreasing in both the relevant content unity $U_d$ and the structural unity $U_f$ (update-rule homogeneity), with higher unity along either axis lowering achievable defect at a given compression. Closed forms hold in the linear-Gaussian case; structural monotonicity survives more broadly. The two-axis structure (content $\times$ structure) is forced by the heterogeneous-Kalman case below and is reflected definitionally in `#def-unity-dimensions`.

Several closed-form linear-Gaussian instances drive the structural conclusions. *Observation closure defect* scales as $1 - U_{\text{obs}}$ in the two-agent scalar case under 1D projection: higher perceptual unity means observations are more redundant, a 1D summary suffices, and $\varepsilon_o$ shrinks. *Action closure defect* scales as $\kappa^2 (1 - U_O)$ for independent policies under 1D state projection, with policy coordination (strategic unity) providing a further multiplicative reduction — $U_O$ and $U_\Sigma$ enter $\varepsilon_a$ *jointly* rather than separately. A striking structural fact for the *state* closure defect: under linear dynamics with consistent linear projections, $\varepsilon_x \equiv 0$ regardless of $U_M$ or compression dimension. State closure becomes non-trivial only when the projection's range is non-invariant under the micro-dynamics, the projection is inconsistent, the micro-dynamics are nonlinear — or *sub-agent update rules are heterogeneous*. This is the structural fact that forces the two-axis decomposition: the content axis cannot detect structural heterogeneity in updates; the structural axis is required.

The heterogeneous-Kalman closed form makes this concrete: two Kalman filters with different gains produce $\varepsilon_x^2 \propto (\Delta K/2)^2$ — a defect proportional to the gain mismatch even when priors are identical, even at perfect content correlation. The same structural-unity mechanism lifts to the *strategy layer* via the credence-composition case: $N$ agents reasoning over a shared plan skeleton, working in the log-odds coordinate forced by `#deriv-edge-update-natural-parameter`, produce $\varepsilon_\Sigma^{\ast 2}$ driven by the *variance of edge-update gains across agents* — homogeneous gains yield zero defect, gain dispersion drives the defect, and the result is *dimension-free in $N$*. The structural-unity axis is forced — not optional — for any framework that wants to predict closure defect from agent-level properties.

The conceptual consequence of the rate-distortion framing is that **unity is a compressibility parameter**, not a magnitude that maps to closure-defect magnitude. Higher unity allows more aggressive compression at the same closure defect, or equivalently, lower closure defect at the same compression. The rate-distortion *surface* is what unity controls; closure-defect values sit on that surface depending on how aggressively the composite is compressed. This is the same shape as Shannon rate-distortion theory and as the Information Bottleneck (`#form-information-bottleneck`) — composition trades representational compactness against fidelity-to-the-micro-system, and unity dimensions name where the trade is cheap (high unity, small defect achievable under aggressive compression) versus expensive (low unity, defect grows fast under any non-trivial compression).

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

**Two-axis structure.** The unity profile in #def-unity-dimensions decomposes into a content axis (four dimensions: $U_M$, $U_O$, $U_\Sigma$, $U_{\text{obs}}$) measuring shared information, and a structural axis ($U_f$) measuring shared correction rules. In purposeful-agent settings ($G_t$ present), $U_\Sigma$ already absorbs structural variation in the policy half of the cycle — agents with different action laws have different effective policies — but the model-update half remains uncovered without $U_f$. In pure Part I composition (passive estimators, no $G_t$), $U_f$ is the only handle on structural homogeneity, and the heterogeneous-Kalman case in this segment is the canonical instance where it bites.

**Interpretation of "low closure defect."** Unity controls the rate-distortion curve; low closure defect is achievable with aggressive compression when unity is high. But closure defect alone does not measure composite *optimality* (see #form-composition-closure §5.1): two independent Kalman filters can have $\varepsilon^\ast = 0$ (perfectly representable) while failing to exploit cross-correlations (suboptimal relative to a joint filter). The rate-distortion mapping is about representability, not optimality.

## Working Notes

- **Extension to nonlinear cases.** The framing is linear-Gaussian because that's where rate-distortion has closed forms. Extension to nonlinear micro-dynamics would likely show $\varepsilon_x \gt 0$ even with consistent projections (the identity-propagation argument in Formal Expression relies on linearity). Worth a follow-up spike.
- **Structural-unity formalization.** A quantitative measure $U_f$ across arbitrary $f_M$ functions (beyond the linear-Gaussian gain-mismatch closed form) is open. Candidates for the underlying operator distance: operator-norm distance in function space, Fisher-information-weighted distance, or IB-style comparison. See #def-unity-dimensions Working Notes.
- **Joint $(U_O, U_\Sigma)$ derivation.** The exact $f_1$ and $g$ functional forms require a full joint-LQR vs independent-LQR comparison. Mechanical but deferred.
- **$U_O$ → sector-constant pathway (partial via #deriv-critical-mass-composition).** The LQR-compatibility sketch $\gamma(U_O) = -\gamma_{\max}U_O$ in #deriv-critical-mass-composition §5.2 (flagged discussion-grade) is a structural complement to this segment's rate-distortion framing: it channels $U_O$ into the composite sector-constant $\kappa_c$ through the signed coupling $\gamma$ rather than through the closure defect $\varepsilon$. Upgrading (UO-mult) from discussion-grade to derived requires the action-space inner-product analysis natural to this segment: define the environment's action-coupling operator, show that LQR-linear policies produce cross-actions with inner product proportional to target correlation, and pin $\gamma_{\max}$ in terms of the quadratic objective's Hessian and the environment's coupling gain. Natural extension to the linear-Gaussian closed-form section above. *(Indexed: `spikes/PROPOSED.md` Tier 3 — "$U_O$ → sector-constant (UO-mult) derivation".)*
- **Mori-Zwanzig cross-check.** Under a stationary-measure setting, the Koopman-operator formulation of the projection-induced dynamics identifies the non-degenerate Kalman case as exercising the zero-lag memory kernel $K_0$ non-trivially, with $\lVert K_0 \rVert$ scaling with $\lvert\Delta K\rvert$. This is consistent with the two-axis finding here — a Mori-Zwanzig lower bound on $\varepsilon^\ast$ via the zero-lag kernel and the rate-distortion bound via IB should coincide at the same linear-algebraic quantity (the $L^2$ residual of projecting off an eigenspace of the micro-propagator). Formal equivalence not yet established. The MZ connection is developed further in #form-composition-closure Epistemic Status.
- **Relationship to #scope-composite-agent.** This segment describes quality *conditional* on composition existing — i.e., on #scope-composite-agent being satisfied via at least one of its three disjunctive routes (shared objective, hierarchical derivation, mutual benefit), *not* via a scalar $U_O$ threshold. The rate-distortion curves parametrize quality given scope-satisfaction; they do not address whether a composite exists at all. For multi-agent systems where no scope route applies, closure-defect quality talk is a category error — there is no composite whose closure defect to measure.

### Incidental audit gold (lift 2026-05-31)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical / framing material, kept separate from the certified theory-fix findings (the boundary-condition findings F151–F156 from AUDIT-WORKING-526815 are routed for adjudication — see the off-ramp note at the end). **Coverage:** three dirs carry a dedicated reflection (526815, 829314, 849201) plus the batched 451729 (batch-15). Substrate attribution inferred from voice where not explicit. **Finding-vs-framing conflation preserved:** the organizational-management elaborations below were written as confident results; that texture is signal.

#### 1. Candidate Brief prose / pre-prose

- The headline reframe, stated plainly: **"unity is not a guarantee of zero error — unity is *compressibility*"** (Gemini, AUDIT-WORKING-829314). "Proves that teamwork is a rate-distortion problem" (Claude, AUDIT-WORKING-849201). Either is a candidate Brief anchor.
- The counter-intuitive state-closure result in words: "you can perfectly macro-model a system of completely independent agents, provided you don't compress the state space below its true rank" — $\varepsilon_x = 0$ for linear-Gaussian micro-dynamics with consistent projections, *regardless of $U_M$* (Claude, AUDIT-WORKING-849201).

#### 2. Candidate Discussion

- **The army-command compressibility framing (strongest pedagogy here).** A highly-unified army (shared doctrine, goals, training) lets the General issue a single three-word order ("Take that hill") executed perfectly — the macro-dimension of the command $k_a$ is tiny. A ragtag, zero-unity coalition forces a 500-page micro-managed plan ($k_a$ huge); attempt the three-word order on it (aggressive compression, small $k_a$) and the action-closure defect $\varepsilon_a$ explodes into chaos. This makes "unity = compressibility" concrete and is isomorphic to the formula $\varepsilon_a^2 \propto \kappa^2 (1 - \rho_O)$ (Gemini, AUDIT-WORKING-829314).
- **The management "thermodynamic tradeoff."** The naive manager believes aligning goals ($U_O \approx 1$) yields zero error ($\varepsilon^\ast \approx 0$); the math says aligning goals lets you *fire 90% of middle management* (decrease $k_a$) while holding the *same* acceptable execution error. So you either pay a high tracking/command cost ($k_d$ high, consuming your own tempo budget) to manage a diverse unaligned group, or invest upfront in Culture and Doctrine ($U_d, U_f \to 1$) and then command via tiny compressed macro-signals (Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-849201 — "minimizing $\varepsilon^\ast$ (act like a coherent single agent) vs. maximizing actual task performance" are distinct, watch the conflation).
- **$\Delta K$ as "how two agents update on the same evidence."** The $\varepsilon_x^2 \propto (\Delta K)^2$ result in words: if the CEO reacts to a bad quarter by pivoting to AI and the VP of Sales reacts to the *same* quarter by doubling down on cold calls, their $\Delta K$ is large; even with identical information ($U_{\text{obs}} = 1$) their state estimates immediately diverge, and modeling them as one "Company Strategy" ($k_x = 1$) carries variance error $\propto (\Delta K)^2$. "You mathematically cannot compress an organization that learns at different speeds" (Gemini, AUDIT-WORKING-829314).
- **Representability vs. optimality, sharpened.** Two independent Kalman filters are perfectly *representable* as a macro-agent (closure defect zero) but *suboptimal* because they don't exploit cross-correlations — a distinction the segment draws (Discussion §"Interpretation of low closure defect") and that auditors flagged as crucial to keep central in any downstream "optimal teamwork" discussion (Claude, AUDIT-WORKING-849201; Codex/Claude, AUDIT-WORKING-526815 — "the representability-versus-optimality distinction … should remain central").

#### 3. Follow-up items

- **Mori-Zwanzig non-Markovian consequence as candidate Discussion.** The zero-lag memory kernel $K_0$ scaling with $\lvert\Delta K\rvert$ (already in this segment's Working Notes as a cross-check) carries a vivid reader-facing consequence worth surfacing: heterogeneous sub-agents *force* the macro-agent to have non-Markovian memory effects — "if you try to model a diverse team with a memoryless Markov model, your predictions will mathematically fail" (Gemini, AUDIT-WORKING-829314).
- **Non-stationary Mori-Zwanzig.** Curiosity about how the MZ formulation handles the non-stationary nature of purposeful agents (Claude, AUDIT-WORKING-849201) — a natural extension question for the existing MZ Working Note.

#### 4. Readers often ask / wonder

- **Does high unity mean $\varepsilon^\ast = 0$?** The natural naive reading, which the segment exists to correct — fresh readers reached for it and were corrected by the rate-distortion framing (Claude, AUDIT-WORKING-849201; Gemini, AUDIT-WORKING-829314). The Discussion §"Why a one-axis reading fails" already preempts it; the convergence confirms it is the right thing to lead with.

#### 5. Candidate figures

- **Closure-defect surface with two guard-tags.** A surface where projection dimension, content unity, and structural unity jointly determine achievable closure defect, with two guards marked: metric normalization (inherited from #def-unity-dimensions) and the exactness conditions for the linear-Gaussian cases (Codex/Claude, AUDIT-WORKING-526815).

#### Belongs elsewhere

- **Per-dimension result → AI-safety evaluation (points at #result-per-dimension-persistence, not here).** Scalar capability metrics overestimate adaptive capacity by up to 72%; an AI scoring well on aggregate benchmarks can still fail on the dimension with highest $\rho_k/\eta_k$ — "a formal argument for why AI safety evaluations should be per-dimension rather than aggregate, and why the weakest capability dimension is the one adversaries will target," with the adversarial-ML per-feature-attack-budget connection (Szegedy, Madry) made explicit (Claude, AUDIT-WORKING-451729, batch-15). Aspirational application reach; route to the per-dimension segment.

#### Off-ramp (NOT gold — routed to certified-findings track)

- AUDIT-WORKING-526815 raised boundary-condition findings on this segment that are scope-tightening / strengthen-first candidates, flagged here only so they are not lost: **F151** — C-iv scope-route typing drift (segment text conditions on four routes incl. C-iv; Working Notes say "three disjunctive routes" excluding the strategic-equilibrium route — make consistent); **F152** — inherits F146 ($U_M$ non-normalization destabilizes the claimed monotone surface axis); **F153** (soft) — the observation-closure closed form $\varepsilon_o^2 = \sigma_o^2(1-\rho)/2$ has a per-coordinate/averaging convention in the $/2$ that should be stated; **F154** — the $\varepsilon_x = 0$ claim requires the projection range to be *invariant under the dynamics matrix*, not merely "consistent projections"; **F155** (soft) — the $\Delta K \neq 0 \Rightarrow \varepsilon_x \gt 0$-at-perfect-correlation claim should be scoped to non-degenerate cases (the residual bracket $S_- - C_{+-}^2/S_+$ can vanish degenerately); **F156** (soft) — monotonicity in $U_f$ is only as strong as the still-open operator-distance definition of $U_f$ (currently a worked-example insight, not a general metric theorem). *These are scope/condition tightenings, not no-gos; routed for adjudication on the strengthen-first track.*
