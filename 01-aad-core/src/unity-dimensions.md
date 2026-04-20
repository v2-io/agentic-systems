---
slug: unity-dimensions
type: discussion
status: discussion-grade
depends:
  - multi-agent-scope
  - composition-closure
  - agent-model
  - strategy-dimension
stage: draft
---

# Discussion: Unity Dimensions

The quality of a composite agent's composition can be decomposed along four substantially independent dimensions: epistemic (shared model), teleological (shared objective), strategic (coordinated action), and perceptual (shared observations). These dimensions parametrize rate-distortion curves for the component closure defects ( #composition-closure, #unity-closure-mapping) — higher unity permits more aggressive compression at lower closure defect. Unity does not directly predict closure-defect magnitude; it controls the compressibility of the corresponding state, observation, or action component under projection.

## Formal Expression

*[Definition (unity-dimensions)]*

For a composite agent $A_c$ composed of sub-agents $\{A_1, \ldots, A_n\}$:

**Epistemic unity** $U_M$ — how much of the reality model is shared:

$$U_M = \frac{I(M_t^{(1)}; \ldots; M_t^{(n)})}{H(M_t^{(1)}, \ldots, M_t^{(n)})}$$

The fraction of total model information that is shared (multi-information / total-correlation ratio). $U_M = 1$ for identical models; $U_M = 0$ for independent models.

**Teleological unity** $U_O$ — how aligned are the objectives:

$$U_O^{(i,j)} = \text{corr}\!\left(V_{O_t^{(i)}}(\tau),\; V_{O_t^{(j)}}(\tau)\right)$$

over trajectories the composite encounters. $+1$ for identical objectives; $-1$ for perfectly opposed; $0$ for orthogonal. The composite teleological unity is an aggregation over all pairs. The scalar ranges from fully cooperative to fully adversarial per objective dimension.

*[Scope note]* $U_O$ has a dual role: it is one of the four unity dimensions (this segment) *and* the scope condition for composition to exist ( #composition-scope-condition). The quality-metric role captured here is conditional on the scope threshold being met. Below the threshold, the sub-agents form a multi-agent system ( #multi-agent-scope) but not a composite, and composition-level quantities (closure defect, composite tempo, team persistence) are not well-defined.

**Strategic unity** $U_\Sigma$ — how coordinated is the joint policy:

*[Discussion]*

$$U_\Sigma = 1 - \frac{D_{\text{KL}}(\pi^c_{\text{actual}} \Vert \pi^c_{\text{optimal}})}{D_{\text{KL}}(\pi^c_{\text{independent}} \Vert \pi^c_{\text{optimal}})}$$

where $\pi^c_{\text{optimal}}$ is the jointly optimal policy. $U_\Sigma = 1$ when actual matches optimal; $U_\Sigma = 0$ when actual matches independent (no coordination). Requires knowing the jointly optimal policy, which is itself a strong assumption.

**Perceptual unity** $U_{\text{obs}}$ — how much of the observation stream is shared:

The fraction of total observation information that reaches all sub-agents. Full perceptual unity means all agents observe the same signals; zero means private observations only. Enables epistemic convergence without explicit model-sharing.

## Epistemic Status

*Discussion-grade.* Max attainable: empirical. The four dimensions are qualitatively motivated: they correspond to the four components of agent state ($M_t$, $O_t$, $\Sigma_t$, and the observation channel). The specific metrics proposed above are sketches — the information-theoretic formulations ($U_M$, $U_\Sigma$) are well-defined in principle but would require specifying distributions and distance measures for any practical computation. The claim that these dimensions are substantially independent is a hypothesis, not derived — epistemic unity may enable strategic unity (shared models allow coordination without explicit planning), so independence is approximate at best.

## Discussion

**Clausewitz's three gaps.** These dimensions map to the gaps identified by Clausewitz (systematized by Bungay in *The Art of Action*):

| Clausewitz Gap | Unity Dimension | Formal Quantity |
|---|---|---|
| Knowledge gap | Epistemic unity ($U_M$) | $1 - U_M$: fraction of model not shared |
| Alignment gap | Teleological unity ($U_O$) | $1 - U_O$: objective misalignment |
| Effects gap | Strategic + Perceptual unity | $1 - U_\Sigma$ + observation routing costs |

The mapping is not perfect — Clausewitz's "effects gap" blends action coordination with observation feedback — but it provides 200+ years of organizational evidence for the qualitative decomposition.

**Connection to closure defect.** The unity dimensions parametrize a rate-distortion relation with the component closure errors in #composition-closure, not a direct correspondence. The correct form (see `msc/spike-unity-closure-mapping.md`): for each unity dimension $U_d$, the achievable closure-defect component $\varepsilon_d(k_d)$ under a projection of macro-dimension $k_d$ decreases monotonically with $U_d$, with closed-form expressions in the linear-Gaussian case. Qualitative direction: $U_M$ controls the compressibility of state information ($\varepsilon_x$), $(U_O, U_\Sigma)$ jointly control action compressibility ($\varepsilon_a$), $U_{\text{obs}}$ controls observation compressibility ($\varepsilon_o$). The naive reading "high $U_d$ predicts low $\varepsilon_d$" fails for non-compressing projections — the means-only projection in the two-Kalman case has $\varepsilon_x = 0$ regardless of $U_M$. *Additionally, unity is not the only driver*: update-rule heterogeneity (agents with different $f_M$) contributes to $\varepsilon_x$ independently, and is not captured by any of the four unity dimensions as defined. See `msc/spike-unity-closure-mapping.md` §10 for the non-degenerate Kalman case exhibiting this two-axis structure.

**What each dimension's absence costs.**

- Low $U_M$: prediction conflicts → uncoordinated actions based on contradictory beliefs. Internal mismatch component from model disagreement.
- Low $U_O$: strategic friction → sub-agents pursue conflicting sub-goals. Effort wasted or counterproductive.
- Low $U_\Sigma$: redundancy and gaps → two agents fix the same bug while a critical one goes unnoticed.
- Low $U_{\text{obs}}$: information silos → critical signals observed by one agent but not actionable by the composite.

## Working Notes
- The independence of unity dimensions needs careful examination. High epistemic unity likely enables (but does not guarantee) high strategic unity — if agents share models, they can coordinate implicitly. The dimensions may be better described as "substantially independent inputs to a joint prediction of $\varepsilon^\ast$" rather than "independent properties."
- The specific metric formulations need testing on concrete cases (software team, military unit) to determine if they discriminate meaningfully between well-composed and poorly-composed groups.
- The teleological unity scalar per objective dimension ($+1$ to $-1$) captures mixed cooperative-competitive situations: a company can be cooperative on product quality and competitive on internal resource allocation simultaneously.
- **Update-rule heterogeneity is a missing axis** (identified 2026-04-20, #unity-closure-mapping §Two-axis structure). The four unity dimensions measure shared *content* (information, goals, policies, observations). In the non-degenerate Kalman case, different Kalman gains $K_1^\ast \neq K_2^\ast$ across agents produce $\varepsilon_x \gt 0$ independent of any unity dimension — even at perfect process correlation. Three resolution options: (A) add a fifth dimension "update homogeneity" $U_f$; (B) reinterpret $U_\Sigma$ broadly to cover $f_M$ heterogeneity in passive-estimator cases; (C) accept that the closure defect has a two-axis structure (unity × homogeneity) rather than a single unity axis. Option (C) is the current working position — it preserves the four-unity framework without overclaiming coverage. Formal resolution open.
- **Joint $(U_O, U_\Sigma) \to \varepsilon_a$ dependence.** State error tracks $U_M$; action error tracks *both* $U_O$ (target alignment) *and* $U_\Sigma$ (policy alignment); observation error tracks $U_{\text{obs}}$. The two dimensions jointly controlling action error are physically distinct: $U_O$ is about evaluation/preference agreement; $U_\Sigma$ is about execution-path agreement. Agents with identical objectives but different execution plans have high $U_O$, low $U_\Sigma$; agents coordinating on arbitrary shared routines have high $U_\Sigma$, low $U_O$. See #unity-closure-mapping for the quantitative relationship.
- **$U_O$ as scope vs. quality — partially resolved 2026-04-20.** The scope role of $U_O$ is now in #composition-scope-condition (draft, robust-qualitative). The quality-metric role remains here. A scope note has been added to the $U_O$ definition above. Open items: operationalization of $\epsilon_{\text{comp}}$ in the scope segment, and eventual auditing of which Section III segments implicitly assume the composition scope condition.
