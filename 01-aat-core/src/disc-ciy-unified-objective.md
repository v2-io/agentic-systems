---
slug: disc-ciy-unified-objective
type: discussion
status: discussion-grade
depends:
  - def-causal-information-yield
  - scope-ciy-observational-proxy
  - def-value-object
  - der-action-selection
stage: draft
---

# Discussion: CIY Unified Policy Objective

The framework's *unified policy objective* expresses the exploration-exploitation tension as a single decision rule: choose the action that maximizes a weighted sum of expected value (exploitation) and a causal-information surrogate (exploration). The first term is the exploitation contribution; the second is a *heuristic exploration term* using CIY ( #def-causal-information-yield) as a tractable surrogate for expected information gain — selecting for causally distinctive actions rather than maximally informative ones. The weighting parameter $\lambda(M_t)$ controls the balance, carries units of *value per unit information*, and in specific well-understood domains reduces to known quantities exactly: the Gittins index for Bayesian bandits, the probing cost in quadratic objectives for Kalman dual control, precision on epistemic affordance for active inference, the explicit variance-over-information ratio in information-directed sampling (Russo & Van Roy). The unified objective is not a novel formalism but a *family-level abstraction* that recovers known scalarizations of the exploration-exploitation trade-off across communities.

The scalar form is honestly heuristic and is now formally *superseded* by an exact tensor trace-product derived in #deriv-causal-ib-lmi: the action maximizes the value plus the trace of a positive-semidefinite shadow-price matrix times the Fisher Information Matrix at the action — the exact Lagrangian relaxation of the Linear Matrix Inequality governing Lyapunov persistence. Two parallel exploration drives emerge from the framework, acting at opposite ends of the uncertainty spectrum: an *epistemic information-gain* drive with $\lambda \propto U_M$ (explore to reduce model uncertainty; dominates when uncertain) and a *survival-imperative* drive with $\lambda \propto 1/U_M$ (an agent with high confidence in a drifting environment mathematically guarantees its own death by ignoring noisy observations, so the Lyapunov persistence constraint dictates an immense shadow price as model uncertainty drops in a drifting environment — forcing the confident agent to seek unambiguous observations from the *opposite* uncertainty regime). The dark-room problem that plagues some preferences-as-priors formulations is *bypassed entirely* by the survival imperative: exploration is not driven by preferences-as-priors but by the literal physical boundaries of the Lyapunov sector constraint. The Discussion below treats the active-inference structural isomorphism with two substantive AAT-specific departures (causal information rather than entropy over hidden states; value functional rather than preferences-as-priors), the zero-mismatch ambiguity bridge from Part I, the three-mode extension for actuated agents, and the regret-bound connection to the strategy-cost objective via the Bretagnolle-Huber identity under deterministic optimal policy.

## Formal Expression

*[Discussion (unified-policy-objective — heuristic)]*

$$\pi^\ast(M_t) = \arg\max_a \left[\mathbb{E}[\text{value}(a) \mid M_t] + \lambda(M_t) \cdot \text{CIY}_q(a;\, M_t)\right]$$

The first term is exploitation (expected value given current model). The second is a *heuristic exploration term* using CIY as a surrogate for expected information gain ( #def-causal-information-yield). CIY measures how different the action's outcome distribution is from alternatives — this is action-distinguishability, not learning value. The surrogate is reasonable when $U_M$ is high (distinguishable actions are also informative to an uncertain agent) and poor when $U_M$ is low (distinguishable actions teach nothing to a confident agent). $\lambda(M_t)$ controls the balance:

- High $U_M$ (uncertain model) → large $\lambda$ — exploration is valuable
- Low $U_M$ (confident model) → small $\lambda$ — exploitation dominates
- Long time horizon → larger $\lambda$ — information compounds
- High $\rho$ (fast-changing environment) → larger $\lambda$ — perpetual uncertainty

$\lambda$ carries units of [value per unit information]. In specific domains it reduces to known quantities:

| Domain | $\lambda$ reduces to | Status |
|--------|---------------------|--------|
| Bayesian bandits | Gittins index | Exactly derived |
| Kalman dual control | Probing cost in quadratic objective | Exactly derived |
| Active inference | Precision on epistemic affordance | Framework-derived |
| Information-directed sampling | $(\text{VoI})^2 / \text{info gain}$ | Exactly derived (Russo & Van Roy) |
| RL with UCB | Confidence-bound scaling | Heuristic (tuned) |

**Identifiability gate.** Before incorporating CIY into the policy objective: (1) action variation must exist, (2) the admissibility regime must be identified ( #scope-ciy-observational-proxy), (3) the reference distribution $q$ must be specified, (4) local stationarity must hold. If any condition fails, CIY-based terms should be dropped or replaced with simpler uncertainty-based heuristics (UCB-style bonuses, ensemble disagreement).

## Epistemic Status

*Discussion-grade summary; underlying derivation is exact.* Originally treated as a discussion-grade heuristic, the unified objective has now been formally derived as the exact Lagrangian relaxation of the Linear Matrix Inequality (LMI) governing Lyapunov persistence (see `#deriv-causal-ib-lmi`).

The scalar heuristic $Q_O(a) + \lambda \cdot \text{CIY}(a)$ is formally superseded by the exact tensor trace-product:
$$ a_t^\ast = \arg\max_a \left[ Q_O(a) + \text{Tr}\left( \Lambda \cdot \mathcal{I}_o(a) \right) \right] $$
where $\mathcal{I}_o(a)$ is the Fisher Information Matrix (Matrix CIY) and $\Lambda$ is the positive-semidefinite shadow price matrix of the survival constraint.

Max attainable for this segment: *discussion-grade* (it is a discussion of the underlying result, per `type: discussion`). Max attainable for the underlying derivation in `#deriv-causal-ib-lmi`: *exact*. The structural form is fully grounded in AAT's physical survival bounds and standard semidefinite programming, eliminating the need to treat exploration as an ad-hoc heuristic.

## Discussion

**Two Parallel Exploration Drives.** AAT dictates two correlated but distinct motivations for exploration, acting at opposite ends of the uncertainty spectrum:
1. **Epistemic Information Gain ($\lambda_{\text{info}} \propto U_M$):** The primary CIY formulation. The agent explores to reduce its model uncertainty. This drive dominates when $U_M$ is high.
2. **The Survival Imperative ($\lambda_{\text{surv}} \propto 1/U_M$):** As mathematically proven in `#deriv-causal-ib-exploration`, an agent with high confidence (low $U_M$) in a drifting environment ($\rho \gt 0$) mathematically guarantees its own death by ignoring noisy observations. To force the necessary correction, the Lyapunov persistence constraint dictates an immense shadow price ($\lambda_{\text{surv}} \to \infty$ as $U_M \to 0$) forcing the agent to seek unambiguous observations (low $U_o$ / high CIY).

The dark-room problem is bypassed entirely by the Survival Imperative: exploration is not driven by preferences-as-priors, but by the literal physical boundaries of the Lyapunov sector constraint.

**Connection to the zero-mismatch ambiguity.** An agent that only exploits (acts to maximize predicted value) will tend toward confirmation bias — observing only what its model already explains ( #def-mismatch-signal, zero-mismatch ambiguity case (b)). Exploration via CIY-maximizing actions is the mechanism by which the agent actively tests its model.

**Connection to Part II.** For actuated agents, the exploration-exploitation tension extends to three modes: exploit (pursue $O_t$ via $\Sigma_t$), explore (improve $M_t$), deliberate (revise $\Sigma_t$). The CIY framework provides the information-theoretic grounding for why strategy edges ( #def-strategy-dag) need observational access ( #der-observability-dominance) — edges the agent cannot observe have frozen CIY.

**Connection to active inference.** The expected free energy (EFE) in active inference (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Da Costa, Parr, Sajid, Veselic, Neacsu & Friston 2020, "Active inference on discrete state-spaces," *J. Math. Psych.* 99; Sajid, Ball, Parr & Friston 2021, "Active inference: demystified and compared," *Neural Computation* 33) decomposes into *pragmatic value* (preferences-aligned outcomes) and *epistemic value* (expected information gain about hidden states). AAT's unified objective is structurally isomorphic: $Q_O$ ≈ pragmatic, CIY ≈ epistemic. The convergence is at the shared-shape level — objective decomposes into value-and-information terms — not unified content. Two substantive differences remain. First, AAT grounds exploration in explicitly *causal* information (action-distinguishability under $do$) rather than entropy reduction over hidden states — not all uncertainty reduction is equally valuable for purposeful action; causal information specifically enables better *intervention* (see #der-causal-hierarchy-requirement; the gap between CIY and proper expected information gain is logged in this segment's Epistemic Status as a known surrogate). Second, AAT does not encode preferences as priors over outcomes ($C(o) = \log P_{\mathrm{pref}}(o)$ in the AI form): AAT's $O_t$ is a value functional on trajectories ( #form-objective-functional), and the satisfaction-gap / control-regret diagnostic in #def-satisfaction-gap, #def-control-regret depends on this distinction — the diagnostic structure does not survive the priors-as-preferences collapse (the dark-room critique, Sun & Firestone 2020, "The dark room problem," *Trends Cog. Sci.* 24).

**Regret-bound connection to the strategy-cost objective.** AAT's $Q_O$ term connects to the strategy-cost objective in #form-strategy-complexity-cost via a regret-bound derivation: strategy-induced regret $R(Q_{\Sigma_t}) = V(a^\ast) - \mathbb{E}_{Q_{\Sigma_t}}[V(a)]$ is bounded by a divergence between $\pi^\ast$ and $Q_{\Sigma_t}$, with the KL direction $\pi^\ast$-first forced (full derivation in #deriv-strategy-cost-regret-bound). Under AAT's canonical scope of deterministic $\pi^\ast$, the Bretagnolle-Huber identity $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log(1 - \operatorname{TV}(\pi^\ast, Q_{\Sigma_t}))$ holds *exactly* (Bretagnolle & Huber 1978), giving the tight regret bound $R(Q_{\Sigma_t}) \leq V_{\max}\bigl(1 - e^{-D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}\bigr)$ with matching lower bound $\Delta_{\min}\bigl(1 - e^{-D_{\mathrm{KL}}}\bigr)$ on isolated optima ( #deriv-strategy-cost-regret-bound §4). Pinsker's $V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$ remains the correct loose general form for stochastic-$\pi^\ast$ extensions where the BH identity degrades back to inequality. The structural point: "value and information term" shares *shape* with EFE's pragmatic-epistemic decomposition, and the KL direction in the strategy-cost's variational form shares direction with variational inference — but AAT's derivation is via decision-theoretic regret bound on $Q_O$ rather than via free-energy-gradient flow, which is the AAT-internal route that does not depend on the priors-as-preferences encoding.

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing / figure / naming material, kept separate from the certified theory-fix findings (handled elsewhere). **Coverage:** dedicated reflections at 526815, 584721, 773921, 829314, 849201 plus the batch dirs 471203 / 963715. The **survival imperative** drew the highest ideation in the chapter — *"arguably the most beautiful mathematical result I've seen in the framework so far."* Substrate attribution inferred from voice where not explicit; uncertain cases hedged.

#### 1. Candidate Brief prose / pre-prose

- **The survival imperative, in one image:** *"The agent doesn't explore because it is curious; it explores because it is suffocating from a lack of surprise"* (Gemini, AUDIT-WORKING-829314). The single most-quotable line for this segment — a Brief-grade gloss of $\lambda_{\text{surv}} \propto 1/U_M$.
- **The U-shaped exploration valuation:** standard RL treats exploration's value monotonically (more uncertainty → more exploration); AAT says high $U_M$ drives *epistemic* exploration and *low* $U_M$ in drifting worlds drives *survival* exploration, *"the two limits composing to a U-shaped exploration valuation — high at both extremes"* (Claude, AUDIT-WORKING-471203). A clean framing-level summary of the "Two Parallel Exploration Drives" subsection.
- The dark-room bypass stated plainly: AAT *"solves the exploration-exploitation dilemma using Lyapunov control theory"* / *"provides a rigorous mathematical solution to the Dark Room Problem that plagues Predictive Coding and Active Inference"* (Claude, AUDIT-WORKING-773921). Brief-grade contribution statement.

#### 2. Candidate Discussion

- **Skunkworks / R&D as a Lyapunov-mandated survival cost — the standout cross-domain reach.** Gemini's extended development of the survival imperative: a too-successful organization (low $U_M$) optimizes its processes so tightly that gain collapses; when the market ($\rho$) shifts, its machinery has *"rusted shut."* *"AAT proves that R&D is not a luxury for finding new profits; it is a Lyapunov-mandated survival cost"* — and likewise the biological necessity of *play* in adult animals as forced high-CIY action to keep the learning machinery functional (Gemini, AUDIT-WORKING-829314). A vivid, honest Discussion angle on the survival imperative that the segment does not currently name. *(Conflation-as-signal: aspirational reach toward an analogy — verify the gain-collapse → organizational-rust isomorphism before promoting past discussion-grade.)*
- **The dark-room rejection validates the whole $(M_t, G_t)$ split.** Several substrates read AAT's escape from the dark-room critique as load-bearing structural support, not just a positioning note: AAT can't reduce expected free energy by hiding in a dark room *"because the trajectory functional doesn't decrease just because observations are uniform"* — $O_t$ is a value functional on trajectories, not a prior over outcomes (Claude, AUDIT-WORKING-584721; AUDIT-WORKING-849201 — *"the rejection of the dark room problem via maintaining $O_t$ separate from $M_t$ validates the entire $(M_t, G_t)$ state split"*). Candidate Discussion sharpening tying the dark-room paragraph back to `#def-strategy-dimension`.
- **The five-domain $\lambda$ table as an explicit integration claim.** Read as showing AAT's objective is a *generalization that includes Gittins / Kalman dual-control / EFE-precision / IDS / UCB as special cases* — *"an integration claim rather than a novel-mathematics claim, consistent with the CLAUDE.md framing"* (Claude, AUDIT-WORKING-584721; praised as *"one of the strongest unification claims in the framework so far"* at AUDIT-WORKING-773921). Worth foregrounding the special-case-recovery reading.

#### 3. Follow-up items

- **Status / type metadata vs. prose tension (propagation debt from the upgrade).** YAML is `status: discussion-grade` / `type: discussion`, but the Epistemic Status prose says *"Exact"* and *"Max attainable: exact."* The honest read: the segment was *upgraded* (prose rewritten to reflect the derivation) but the "Max attainable: exact" line belongs in the underlying derivation segment, not the discussion summary — this Epistemic Status should say "summarizes the exact result derived in [the LMI derivation]" (Claude, AUDIT-WORKING-471203, logged Low/Medium; same observation at AUDIT-WORKING-526815, 829314). Editorial; surfaces a real upgrade-propagation failure mode.
- **Cross-reference verified clean (2026-05-30).** One batch flagged a possibly-stale forward-reference to `#deriv-directional-survival-exploration`, a slug it could not find in OUTLINE. Grep of the current body confirms it cites only `#deriv-causal-ib-lmi` / `#deriv-causal-ib-exploration` (both exist as segments); no `#deriv-directional-survival-exploration` slug remains anywhere in canon. Resolved — the flagged slug was a pre-promotion artifact already superseded. (Flagged by Claude, AUDIT-WORKING-471203.)
- **Pinsker → Bretagnolle-Huber integration debt.** One substrate (AUDIT-WORKING-584721, logged F-D1) initially read the regret bound as still using Pinsker where the canonical `#deriv-strategy-cost-regret-bound` now uses the sharper BH identity. The *current* body already states the BH identity as primary with Pinsker as the loose stochastic-$\pi^\ast$ fallback — so this appears resolved; logged here only so the disposition is traceable. Both bounds are valid; one is sharper.
- **Domain-table "exactly derived" labels may overstate.** The Gittins index is an action index/value in a discounted bandit, not the scalar weight $\lambda$ itself; information-directed sampling minimizes a regret²/information ratio, not a direct additive $\lambda\cdot\text{CIY}$ term. If these are analogies, *"exactly derived"* is too strong without an explicit mapping (Codex/Claude, AUDIT-WORKING-526815). Candidate precision pass on the table's Status column.

#### 4. Readers often ask / wonder

- **Why does a confident agent in a drifting world die — and why is more confidence fatal?** The survival-imperative mechanism is the chapter's "wait, really?" moment and readers want the chain spelled out: low $U_M$ → Kalman gain $\eta^\ast \to 0$ → adaptive tempo $\mathcal{T} \to 0$ → violates persistence $\alpha \gt \rho/R$ → death by *gain collapse* (Gemini, AUDIT-WORKING-829314, 773921). The body states it; a one-line causal chain up front would land it faster.
- **Does the survival shadow-price $\Lambda$ explode along the agent's weakest dimension** — i.e. does the agent automatically steer exploration to fix the eigenvector closest to failing $\Sigma_\infty \prec D_\delta$? (Claude, AUDIT-WORKING-773921). A precise, falsifiable reader question about the matrix form, worth a sentence or a forward pointer to `#deriv-causal-ib-lmi`.
- **Is the "Discussion" section overloaded?** One substrate read the segment as *"a chaotic mix of profound insights and dense defensive literature reviews ... shoving advanced variational bounding theorems into a Discussion segment ... severely harms readability"* and would refactor the exact Lagrangian survival-imperative derivation into its own `Derived` segment with the active-inference review quarantined (Gemini, AUDIT-WORKING-829314). Same placement-vs-value tension flagged at `#der-loop-interventional-access`; preserved as a real readability signal, not a defect.

#### 5. Candidate figures

- **Two stacked objectives diagram.** Top layer: the scalar heuristic $\mathbb{E}[\text{value}] + \lambda\cdot\text{CIY}$, gated by identifiability; lower layer: the exact matrix form $Q_O(a) + \mathrm{Tr}(\Lambda\,\mathcal{I}_o(a))$. *"Drawing both makes the status drift visible — the scalar form is useful vocabulary, the exact claim belongs to the LMI/tensor version"* (Codex/Claude, AUDIT-WORKING-526815, has a rendered draft).
- **U-shaped exploration-value curve.** Exploration valuation against $U_M$: high at high $U_M$ (epistemic drive) and high at low $U_M$ (survival drive), dipping in between — visualizes the two-parallel-drives composition (implicit in Claude, AUDIT-WORKING-471203).

#### Belongs elsewhere

- The exact Lagrangian relaxation of the LMI and the matrix-CIY trace-product are the property of `#deriv-causal-ib-lmi` / `#deriv-causal-ib-exploration`; the Bretagnolle-Huber regret derivation is `#deriv-strategy-cost-regret-bound`. This segment is the discussion-grade surface; the theorem-grade math lives in those appendix segments.
