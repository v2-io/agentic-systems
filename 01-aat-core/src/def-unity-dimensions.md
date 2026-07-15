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

The quality of a composite agent's composition — *conditional on #scope-composite-agent being satisfied via at least one of its four routes (three alignment routes + the strategic-equilibrium route (C-iv))* — is parametrized along **two architecturally distinct axes**:

- **Content axis (four unity dimensions).** What the sub-agents *share*: epistemic ($U_M$, shared model), teleological ($U_O$, shared objective), strategic ($U_\Sigma$, coordinated action), and perceptual ($U_{\text{obs}}$, shared observations).
- **Structural axis (update-rule homogeneity, $U_f$).** Whether sub-agents implement the *same* correction rule: how similar their $f_M$ updates are across the population.

Together, the two axes parametrize the rate-distortion curves for the component closure defects ( #form-composition-closure, #result-unity-closure-mapping). Higher unity along either axis permits more aggressive compression at lower closure defect; neither axis alone is sufficient. In pure Part I composition (passive estimators, no $G_t$), agents with identical content can still produce non-zero $\varepsilon_x$ if their update rules differ — the content axis cannot detect this, which is why the structural axis is required. Unity (in either sense) does not directly predict closure-defect magnitude; it controls the compressibility of the corresponding state, observation, or action component under projection.

**Scope.** The decomposition applies to composites that satisfy #scope-composite-agent. $U_O$ plays a role in the (C-i) route of the scope condition via value-correlation, but the scope condition is a disjunction of four routes — three alignment routes (shared objective, hierarchical derivation, mutual benefit) plus the strategic-equilibrium route (C-iv) — not a scalar threshold on $U_O$. Below scope-satisfaction (no route applies), the sub-agents are a multi-agent system per #scope-multi-agent and composition-level quantities are not well-defined.

## Formal Expression

*[Definition (definition-unity-dimensions)]*

For a composite agent $A_c$ composed of sub-agents $\{A_1, \ldots, A_n\}$, the unity profile consists of *four content dimensions* (this section, below) and *one structural dimension* ($U_f$, defined after the content dimensions).

### Content dimensions

**Epistemic unity** $U_M$ — how much of the reality model is shared:

$$U_M = \frac{I(M_t^{(1)}; \ldots; M_t^{(n)})}{(n-1)\,H(M_t^{(1)}, \ldots, M_t^{(n)})}$$

The fraction of total model information that is shared (total-correlation ratio, normalized to $[0,1]$). The numerator is the total correlation $I = \sum_i H(M_t^{(i)}) - H(M_t^{(1)}, \ldots, M_t^{(n)})$; the $(n-1)$ factor in the denominator is its normalizer, since each marginal entropy is at most the joint entropy and hence $I \leq (n-1)\,H(M_t^{(1)}, \ldots, M_t^{(n)})$, with equality iff each model determines all the others. So $U_M = 1$ for identical models and $U_M = 0$ for independent models, for every $n$. (Without the $(n-1)$ factor the ratio reaches $n-1$ at identity — the bare multi-information/joint-entropy form is normalized correctly only at $n = 2$.)

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

Where the four content unities measure shared *information* across sub-agents (state, objective, policy, observation), $U_f$ measures shared *structure* — whether the agents instantiate the same update law. The two axes are independent: agents can share a model ($U_M = 1$) while updating it differently ($U_f \lt 1$), and conversely. In purposeful settings ($G_t$ present), $U_\Sigma$ partially absorbs structural variation in the policy half of the cycle, but the model-update half remains uncovered without $U_f$. In pure Part I composition (passive estimators, no $G_t$), $U_f$ is the only handle on structural homogeneity. The closed-form linear-Gaussian instance — heterogeneous Kalman gains $\Delta K = K_1^\ast - K_2^\ast$ producing $\varepsilon_x \propto \lvert\Delta K\rvert$ — is derived in #result-unity-closure-mapping §Two-axis structure.

### Joint role in closure defect

The achievable component closure defect $\varepsilon_d^{\min}(k_d)$ under a projection of macro-dimension $k_d$ is a function of *both* axes — the relevant content unity $U_d$ and the structural unity $U_f$ — together with the projection-dimension parameter:

$$\varepsilon_d^{\min}(k_d) = f_d\!\left(k_d;\; U_d,\; U_f\right)$$

monotone decreasing in each unity argument and monotone increasing in compression aggressiveness (smaller $k_d$). The form is derived in #result-unity-closure-mapping; in linear-Gaussian scalar cases it admits closed-form expressions for $d \in \{x, o, a\}$. $U_O$ and $U_\Sigma$ enter $\varepsilon_a$ jointly rather than separately — collapsing alignment to a single scalar ($U_O$ alone) would mis-route the repair, since execution-path divergence ($U_\Sigma$) cannot be fixed by re-aligning targets. This is the **anti-collapse** discipline ( #disc-anti-collapse) at the composite layer: two distinct quantities a naive reading merges, routing to different corrections.

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

### Incidental audit gold (lift 2026-05-31)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical / framing / figure / naming material, kept separate from the certified theory-fix findings (the metric-repair findings F146–F150 from AUDIT-WORKING-526815 are routed for adjudication, not here — see the off-ramp note at the end). **Coverage:** three dirs carry a dedicated reflection (526815, 829314, 849201) plus two batched dirs (451729 batch-14, 613842 composition-cross-component). The other contributing dirs stopped earlier in the OUTLINE walk. Substrate attribution inferred from voice where not explicit; uncertain cases hedged. **Finding-vs-framing conflation preserved:** several "candidate Discussion" entries below were written as confident results in first-encounter cognition; that texture is signal, kept rather than sanitized.

#### 1. Candidate Brief prose / pre-prose

- Plain-statement of the structural-axis insight, Feynman-criterion-adjacent: "even if two agents know the exact same things and want the exact same things, if one learns fast and the other learns slow, they cannot be mathematically compressed into a single macro-agent without accumulating trajectory error" (Gemini, AUDIT-WORKING-829314). Compact hook for a Brief or Discussion opener on why content unity is not enough.
- "Decomposes 'teamwork' into its orthogonal mathematical components" — one-line gloss of the segment's contribution (Claude, AUDIT-WORKING-849201).

#### 2. Candidate Discussion

- **Clausewitz-three-gaps mapping is the standout pedagogy — promote it more prominently.** Two substrates independently flagged the mapping of the unity dimensions to Clausewitz's three gaps (Knowledge / Alignment / Effects) as "an absolutely brilliant piece of pedagogical framing … it grounds the abstract information theory in 200 years of practical military strategy"; the recommendation is to highlight that table even more prominently (Gemini, AUDIT-WORKING-829314; Gemini, AUDIT-WORKING-849201 — "a phenomenal domain connection").
- **Content alignment is dynamically unstable without structural alignment (the "metabolism mismatch" / "culture fit" framing).** The sharpest worked elaboration of $U_f$: a two-engineer team perfectly aligned on content ($U_M = U_O = U_\Sigma = 1$) but with mismatched update rules — Engineer A highly plastic (rewrites architecture on every bug), Engineer B highly stable (patches the line) — will violently diverge the instant a shared bug is observed, "not because they disagreed on facts or goals, but simply because their internal learning metabolisms were mismatched." This is offered as the formal content of the corporate "culture fit" problem: hiring is for $f_M$-compatibility, not only skills; dropping a "move fast and break things" developer into a slow-moving aerospace team spikes the closure defect $\varepsilon^\ast$ and destroys macro-agent tempo (Gemini, AUDIT-WORKING-829314). *(Finding-vs-framing texture: written as a proof — "proves mathematically that …" — but the general-$U_f$ monotonicity is only worked for the linear-Gaussian two-Kalman case per #result-unity-closure-mapping; promote as motivated framing, not as established theorem.)*
- **Epistemology does not guarantee strategy — the two-autonomous-cars example.** "Two autonomous cars might have perfect, identical models of an intersection ($U_M = 1$), but if they don't coordinate their policies, they will still crash ($U_\Sigma = 0$)." A vivid one-line separation of the epistemic and strategic content axes (Gemini, AUDIT-WORKING-829314).
- **Closure defect as the formal analog of "organizational complexity."** $\varepsilon^\ast$ reads as "the gap between what a collection of agents could achieve in principle and what a coherent macro-description can represent" — the formal version of what organizational scientists call organizational complexity. Crucially: coherence (closure defect) and efficiency (performance gap) are *orthogonal* axes — "you can have a perfectly coherent organizational description of an inefficient organization" (Claude, AUDIT-WORKING-451729, batch-14). A candidate framing-level Discussion note on what the two-axis taxonomy is *for*.
- **The two-Kalman $\varepsilon^\ast = 0$ diagnostic, in words.** Two non-communicating Kalman filters tracking correlated targets are "perfectly representable as one agent" even though they never share information — not because they cooperate, but because each individually generates a sufficient statistic for the macro-state's next observation. Representability $\neq$ optimality (Claude, AUDIT-WORKING-451729, batch-14). Belongs more to #result-unity-closure-mapping but motivates why the content axis alone is the wrong diagnostic here.

#### 3. Follow-up items

- **Mixed-motive $U_O$.** How does the theory handle $U_O$ in mixed-motive games where agents cooperate on survival but compete on resource allocation? The per-objective-dimension scalar ($+1$ to $-1$) is noted to cover this in principle, but the aggregation math "must be tricky" — worth a worked example (Claude, AUDIT-WORKING-849201; echoed Gemini, AUDIT-WORKING-829314 on group-level/nontransitive alignment).
- **C-iv ontology drift — closure/unity machinery still assumes the older shared-objective idiom.** A cross-component pass flagged that the scope layer ( #scope-composite-agent) has accepted route (C-iv) (strategic composites with no shared $O_c$, macro-state defined relative to equilibrium structure $\mathcal E$), but this segment "still describes the scope as a three-route disjunction and treats composition-level quantities as unavailable whenever the three alignment routes fail" — a real integration gap between the broadened scope and the unity machinery (Claude, AUDIT-WORKING-613842). The existing "$U_O$ as scope vs. quality" Working Note above already partly tracks this; the cross-component observation sharpens it into a propagate-C-iv-into-the-unity-segments task.

#### 4. Readers often ask / wonder

- Auditors converged on the same conceptual checks as natural reader questions: that $U_M = 1$ does not force $U_\Sigma = 1$ (the cars), and that the four content unities measure shared *content* but not shared *structure* — the "missing axis" that $U_f$ supplies. Two fresh readers independently praised the segment for flagging this gap rather than hiding it ("the epistemic honesty to flag this gap … is exemplary" — Claude, AUDIT-WORKING-849201; Gemini, AUDIT-WORKING-829314).

#### 5. Candidate figures

- **Two-axis closure-defect surface.** A rate-distortion surface controlled by two roughly-independent inputs — content unity and structural homogeneity — with the metric-normalization warning marked on the content side (since bad normalization would mislead the surface before any later derivation begins) (Codex/Claude, AUDIT-WORKING-526815).

#### Belongs elsewhere

- **Rate-distortion-as-compressibility army/management framing** belongs to #result-unity-closure-mapping (lifted there), but originates partly from the structural-axis intuition seeded here.

#### Off-ramp (NOT gold — routed to certified-findings track)

- AUDIT-WORKING-526815 raised five metric-level findings on this segment that are strengthen-first / repair candidates, not framing gold, and are flagged here only so they are not lost: **F146** — $U_M = I(M^{(1)};\dots;M^{(n)})/H(M^{(1)},\dots,M^{(n)})$ is *not* normalized to $[0,1]$ as the discussion-grade label implies (for $n$ identical variables of entropy $H$, total correlation is $(n-1)H$ and joint entropy is $H$, so the ratio is $n-1$, not $1$ — needs a capped/rescaled redundancy measure); **F147** — teleological unity as pairwise value-function correlation is distribution-/policy-dependent and undefined for zero-variance value functions (needs support/variance/aggregation conventions); **F148** — the strategic-unity KL ratio can have a zero denominator, infinite KL, or leave $[0,1]$ without clipping; **F149** (soft) — $U_{\text{obs}}$ as "fraction of observation information reaching all sub-agents" misses complementary-private-plus-routed and synergistic-private observation; **F150** (soft) — $U_f = 1 - d(\cdot)$ presumes a normalized $d \in [0,1]$ that the candidate operator/Fisher/IB distances do not automatically satisfy. *These are metric-formalization repairs (mostly scope/normalization tightenings), not no-gos; routed for adjudication on the strengthen-first track.*
