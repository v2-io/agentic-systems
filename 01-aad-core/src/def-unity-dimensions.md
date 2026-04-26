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

# Definition: Unity Dimensions

The quality of a composite agent's composition — *conditional on #scope-composite-agent being satisfied via at least one alignment route* — is parametrized along **two architecturally distinct axes**:

- **Content axis (four unity dimensions).** What the sub-agents *share*: epistemic ($U_M$, shared model), teleological ($U_O$, shared objective), strategic ($U_\Sigma$, coordinated action), and perceptual ($U_{\text{obs}}$, shared observations).
- **Structural axis (update-rule homogeneity, $U_f$).** Whether sub-agents implement the *same* correction rule: how similar their $f_M$ updates are across the population.

Together, the two axes parametrize the rate-distortion curves for the component closure defects ( #form-composition-closure, #result-unity-closure-mapping). Higher unity along either axis permits more aggressive compression at lower closure defect; neither axis alone is sufficient. In pure Section I composition (passive estimators, no $G_t$), agents with identical content can still produce non-zero $\varepsilon_x$ if their update rules differ — the content axis cannot detect this, which is why the structural axis is required. Unity (in either sense) does not directly predict closure-defect magnitude; it controls the compressibility of the corresponding state, observation, or action component under projection.

**Scope.** The decomposition applies to composites that satisfy #scope-composite-agent. $U_O$ plays a role in the (C-i) route of the scope condition via value-correlation, but the scope condition is a disjunction of three routes (shared objective, hierarchical derivation, mutual benefit), not a scalar threshold on $U_O$. Below scope-satisfaction (no route applies), the sub-agents are a multi-agent system per #scope-multi-agent and composition-level quantities are not well-defined.

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

*[Scope note]* $U_O$ plays a role in #scope-composite-agent — primarily along route (C-i), where value-correlation is the operationalization of teleological alignment. The scope condition itself is disjunctive: it is satisfied when *any* of routes (C-i), (C-ii), or (C-iii) applies, not by $U_O$ alone crossing a common scalar threshold. The quality-metric role of $U_O$ captured in this segment presumes scope-satisfaction via *some* route. When the sub-agents fail all three routes, they form a multi-agent system ( #scope-multi-agent) but not a composite, and composition-level quantities (closure defect, composite tempo, team persistence) are not well-defined.

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
- **$U_O$ as scope vs. quality.** The scope role is in #scope-composite-agent as a disjunction of three routes — $U_O$ is the value-correlation operationalization of route (C-i), not a universal scope variable. The quality-metric role remains here, presumed conditional on scope-satisfaction via at least one route. Open: whether the three routes reduce to a single scalar is not established, so "scope-satisfaction" and "$U_O$ value" should be treated as distinct concerns in downstream uses.
