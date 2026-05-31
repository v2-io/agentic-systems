---
slug: disc-credit-assignment-boundary
type: discussion
status: discussion-grade
depends:
  - def-strategy-dag
  - hyp-edge-update-via-gain
  - deriv-edge-update-natural-parameter
  - def-strategic-calibration
  - der-observability-dominance
  - der-gain-sector-bridge
  - deriv-edge-credence-dynamics
stage: draft
---

# Discussion: Credit Assignment Boundary

The strategy-revision loop requires assigning credit for observed outcomes to specific edges in the strategy DAG — decomposing "the plan partially worked" into "step 3 failed, step 5 was irrelevant, step 1 succeeded." This is AAT's version of RL's temporal credit assignment problem. This segment characterizes the boundary between tractable and intractable cases, states what the theory requires of any credit-assignment scheme, and identifies what the theory can guarantee *without* solving the problem at all.

The framework names **three things the theory can guarantee without solving credit assignment**. (1) *Persistence is credit-assignment-free*: the sector condition transfers from per-edge credence space to strategy-plan-confidence error $\delta_s = \hat P_\Sigma - \Phi$ via the Jacobian $\mathbf{J} = \nabla_\mathbf{p} P_\Sigma$, computable from status propagation in $O(\lvert V\rvert + \lvert E\rvert)$ — no outcome decomposition required (Prop B.5 in #deriv-edge-credence-dynamics). (2) *The diagnostic framework is plan-level*: the satisfaction gap ( #def-satisfaction-gap), control regret ( #def-control-regret), and orient cascade ordering ( #der-orient-cascade) operate on aggregate value, telling the agent *whether* the strategy is failing without per-edge attribution. (3) *Observability-dominance identifies the tractable edges*: only the observable subgraph ( #der-observability-dominance) can receive informative signals at all. Three independent intractability barriers prevent exact per-edge attribution in the general case: (a) computational #P-hardness via reduction to Shapley values over the AND/OR propagation game; (b) information-theoretic underdetermination — when fewer nodes are observable than edges exist, some directions in $\boldsymbol\theta$-space are fundamentally unresolvable from the available data; (c) the posterior correlation barrier — any factored representation necessarily discards the correlation introduced by failure at multi-parent nodes.

The **design requirement** is stated cleanly: any credit-assignment scheme need only satisfy *directional fidelity* — the expected update for each edge must point toward the true credence. Persistence is *robust to approximation*: a sloppy but directionally correct signal function still produces bounded strategic mismatch; the quality of the approximation affects the tightness of the persistence bound, not whether persistence holds at all. The framework presents a **default signal function** based on gradient-attribution, stated natively in the log-odds coordinate $\lambda_k = \log(p_k/(1-p_k))$ — the unique additive-evidence coordinate forced by the evidential-additivity axiom ( #deriv-edge-update-natural-parameter), which eliminates a mechanical break the earlier probability-space presentation suffered (updates outside $[0,1]$). A useful **hierarchy of credit assignment quality** is presented: Level 0 (plan-level tracking only — persistence guarantee, no per-edge diagnostics); Level 1 (directional fidelity per edge — persistence plus rough per-edge diagnostics, the gradient signal function is the concrete default); Level 2 (proportional blame / expectation propagation); Level 3 (full Bayesian posterior — #P-hard in general). AAT's formal guarantees require only Level 0; practical agents need at least Level 1; Level 2 is the sweet spot for most applications; Level 3 is computationally unattainable in the general case. A clean practical insight follows: *credit assignment is primarily an observability design problem*, not an algorithm design problem — an agent that designs its strategy with observable intermediates sidesteps the intractability entirely (OKRs as the organizational instantiation).

## Formal Expression

### The Credit Assignment Problem for Strategy DAGs

*[Discussion (credit-assignment-problem)]*

Given strategy DAG $\Sigma_t = (V, E, p, \gamma)$, an observed outcome at the root (and possibly at some intermediate nodes), produce per-edge signals $\text{signal}(o_t, i, j)$ for each edge $(i,j) \in E$ such that the edge update

$$p_{ij}^{\text{new}} = p_{ij} + \eta_{\text{edge}} \cdot (\text{signal}(o_t, i, j) - p_{ij})$$

drives credences toward truth. The problem is trivial when all intermediates are observable (each edge updates from its own observation) and genuinely hard when intermediates are unobservable and the DAG has shared structure.

### Default Signal Function (Gradient-Based Attribution, Regime-Aware)

*[Formulation (gradient-signal-function)]*

Any edge-update signal function decomposes along three independent axes: *what happened* at the child node, *whether that outcome is attributable* to the specific edge being updated, and *how causal* the evidence is:

$$\text{signal}(o_t, i, j) = f\bigl(\text{outcome}(o_t, j),\; \text{attribution}(o_t, i, j),\; \text{regime}(i, j)\bigr)$$

The outcome component answers "what was observed at $j$?" The attribution component answers "can we credit that outcome to edge $(i,j)$ specifically, or did other parents contribute?" The regime component answers "how causal is the evidence — is it interventional (Regime A), partially identified (Regime B), or observational (Regime C)?" This decomposition is derived from the regime-indexed edge semantics of #def-strategy-dag and #scope-edge-update-causal-validity: the same signal pipeline must carry the regime distinction through to the update.

AAT's default implementation, analogous to $\eta^\ast = U_M/(U_M + U_o)$ being the default gain. The update is stated in the log-odds coordinate $\lambda_k = \log(p_k/(1-p_k))$ — the unique additive-evidence coordinate forced by the evidential-additivity axiom ( #deriv-edge-update-natural-parameter). The probability-space form is the projected image via $p_k = \sigma(\lambda_k)$ at the readout interface:

$$\lambda_k^{\text{new}} = \lambda_k + \eta_{\text{edge}} \cdot \iota_k \cdot \frac{J_k \cdot (y_G - \hat P_\Sigma)}{\lVert\mathbf{J}\rVert^2}, \qquad p_k^{\text{new}} = \sigma(\lambda_k^{\text{new}})$$

where:
- $\mathbf{J} = \nabla_\mathbf{p} P_\Sigma$ is the plan-value gradient (computable from status propagation in $O(\lvert V\rvert + \lvert E\rvert)$) — supplying the *attribution* component
- $(y_G - \hat P_\Sigma)$ is the plan-level residual — the *outcome* component
- $\iota_k \in [0, 1]$ is the edge's identifiability coefficient ( #scope-edge-update-causal-validity) — the *regime* modulation, scaling the correction by the fraction of evidence that genuinely identifies this edge's causal effect
- $\eta_{\text{edge}}$ is the edge-level update gain ( #hyp-edge-update-via-gain); for Beta-Bernoulli the moment-parameter form recovers $\eta_{\text{edge}} = 1/(n_k+1)$ under the sufficient-statistic correspondence

For Regime-A edges ($\iota_k \approx 1$), the log-odds update recovers the pure gradient-based form $\Delta\lambda_k = \eta_{\text{edge}} \cdot J_k(y_G - \hat P_\Sigma)/\lVert\mathbf{J}\rVert^2$. For Regime-C edges ($\iota_k \approx 0$), the update is essentially zero — no meaningful update is made because no meaningful causal evidence is available. Regime-B edges receive proportionally reduced updates that honestly reflect the weaker identification.

**Why log-odds rather than probability-space.** In probability space, the same update written as $\text{signal}_k - p_k$ can push $p_k^{\text{new}}$ outside $[0, 1]$ when $\lVert\mathbf{J}\rVert^2$ is small — a mechanical break of the $[0, 1]$ probability domain. The log-odds coordinate has domain $\mathbb{R}$, so additive updates never escape the domain; the sigmoid projection at the readout interface guarantees $p_k^{\text{new}} \in (0, 1)$ by construction. The log-odds coordinate is the unique (up to positive affine transformation) parameterization on which Bayesian independent-evidence accumulation is additive ( #deriv-edge-update-natural-parameter); this makes it the natural presentation for any continuous-gradient update rule that aims to preserve Bayesian coherence. The probability-space presentation remains useful for interpretation but is the projected image, not the native update coordinate.

**Properties:**
- **Domain closure (no mechanical break):** Updates live on $\lambda_k \in \mathbb{R}$, so no update magnitude can push credence outside the valid probability domain. The sigmoid projection $p_k = \sigma(\lambda_k) \in (0, 1)$ at the readout interface guarantees $[0, 1]$ boundedness by construction — not by clipping. The historical probability-space presentation required a normalization constant and could diverge when $\lVert\mathbf{J}\rVert^2 \to 0$; the log-odds presentation eliminates this failure mode.
- **Directional fidelity (B1):** For $\iota_k \gt 0$, satisfies $\mathbb{E}[\Delta\lambda_k] \propto \iota_k \cdot J_k(\Phi - \hat P_\Sigma) \propto \iota_k \cdot J_k \cdot \delta_s$. Since $J_k \geq 0$ for monotone AND/OR DAGs and $\iota_k \geq 0$ by definition, the expected log-odds update pushes each edge's credence toward truth whenever evidence is available to push it. The probability-space image inherits directional fidelity through the monotonic sigmoid.
- **Sector parameter:** $\alpha_s = \iota_k \cdot \eta_{\text{edge}}$ for componentwise corrections (regime-adjusted Prop B.5b); $\alpha_s = \iota_k \cdot \eta_{\text{edge}} / \kappa(\mathbf{J})^2$ for coupled corrections. Regime-C edges have $\alpha_s \approx 0$, making them effectively frozen — consistent with #der-observability-dominance's treatment of unobservable edges. The sector parameter is Fisher-equivalent across coordinates (see Epistemic Status); the probability-space and log-odds-space statements of Props B.1–B.7 carry the same content.
- **Computational cost:** $O(\lvert V\rvert + \lvert E\rvert)$ — the same forward pass that computes $\hat P_\Sigma$ also yields $\mathbf{J}$. The $\iota$ factors are per-edge domain parameters, not computed from the DAG structure. The sigmoid projection is $O(\lvert E\rvert)$ per update step.
- **Relationship to RL:** This is the AAT analog of REINFORCE with a causal-identification weighting — the Jacobian $\mathbf{J}$ is the score function, $(y_G - \hat P_\Sigma)$ is the advantage, and $\iota_k$ is the causal-validity discount on each edge's update.

**Correlated-failure interaction (L0 vs L1).** The gradient signal operates at L0 of the Correlation Hierarchy ( #def-strategy-dag). When the DAG is causally insufficient (the dominant real-world case), the residual $(y_G - \hat P_\Sigma)$ decomposes into per-edge miscalibration *plus* omitted correlation structure. $\hat P_\Sigma$ systematically overestimates success, making the residual systematically negative on failure. The gradient signal then attributes to individual edges what is actually causal insufficiency (missing common-cause nodes). The signal retains directional fidelity *on average* (it pushes edges downward when the plan is overconfident, which is the correct direction), but the per-edge attribution is contaminated. The principled fix is L1: add common-cause nodes to restore causal sufficiency, then apply gradient attribution to the augmented DAG. In the augmented DAG, the residual correctly decomposes into per-edge miscalibration because the correlation structure is explicitly represented.

Domains with richer observation structure can do better (Thompson sampling, full belief propagation, domain-specific attribution). The gradient-based signal is the *concrete Level 1 default* — the minimum viable credit-assignment scheme that satisfies the theory's requirements.

### What the Theory Can Guarantee Without Solving Credit Assignment

Three results hold independently of any specific credit-assignment scheme:

**1. Persistence is credit-assignment-free.** Proposition B.5 in #deriv-edge-credence-dynamics shows that the sector condition transfers from per-edge credence space to **strategy-plan-confidence error** $\delta_s = \hat P_\Sigma - \Phi$ via the Jacobian $\mathbf{J} = \nabla_\mathbf{p} P_\Sigma$. The Jacobian is computable from status propagation in $O(\lvert V\rvert + \lvert E\rvert)$ — no outcome decomposition required. The persistence guarantee (whether the strategy's plan-level self-assessment can be maintained) does not depend on the agent's ability to attribute outcomes to edges. **Note:** this proves persistence of $\delta_s$ (strategy-plan-confidence error), not of $\delta_{\text{strategic}}$ (the per-edge calibration residual from #def-strategic-calibration). Extending persistence to $\delta_{\text{strategic}}$ requires solving the credit-assignment problem — that is the gap this segment characterizes.

**2. The diagnostic framework is plan-level.** The satisfaction gap ( #def-satisfaction-gap), control regret ( #def-control-regret), and the orient cascade ordering ( #der-orient-cascade) operate on aggregate value, not per-edge quantities. They tell the agent *whether* the strategy is failing (and whether the failure is feasibility vs. optimality vs. calibration), without requiring per-edge attribution.

**3. Observability-dominance identifies the tractable edges.** #der-observability-dominance determines which edges have nonzero observability — only these can receive informative signals. Edges with zero observability are frozen regardless of the credit-assignment scheme. The tractable boundary is the observable subgraph of $\Sigma_t$.

### The Tractable Cases

*[Discussion (tractable-credit-assignment)]*

Credit assignment is solved (exact, polynomial-time) when:

| Condition | Why tractable | Update rule |
|---|---|---|
| **All intermediates observable** | Each edge has its own observation; updates decouple | Beta-Bernoulli per edge (Prop B.2) |
| **Binary outcomes, independent edges, linear chain** | Marginal Bayesian update = proportional blame | Prop B.3 (with plan-level fallback for unobservable) |
| **Tree DAG, observable leaves** | No shared descendants; message passing is exact | Belief propagation (standard) |

### The Intractable Cases: Three Independent Barriers

*[Discussion (intractable-credit-assignment)]*

Exact per-edge attribution in general AND/OR DAGs with partial observability faces three independent barriers:

**1. Computational intractability (\#P-hardness).** The "contribution of edge $k$ to the observed outcome" has the form of a Shapley value over a cooperative game defined by the AND/OR propagation. Since AND/OR DAGs can represent any monotone Boolean function (including weighted threshold functions), and Shapley value computation for weighted voting games is \#P-complete (Deng and Papadimitriou, 1994), exact attribution is \#P-hard. *Caveat:* the reduction is to *exact* computation; approximate Shapley values are computable in polynomial time with sampling.

**2. Information-theoretic underdetermination.** When intermediates are unobservable, per-edge attribution is *underdetermined*, not just hard. The identifiable subspace has dimension bounded by the number of observable nodes:

$$\dim(\mathcal{I}(\mathcal{V}_{\text{obs}})) \leq \lvert\mathcal{V}_{\text{obs}}\rvert$$

When $\lvert\mathcal{V}_{\text{obs}}\rvert \lt \lvert E\rvert$ (fewer observable nodes than edges), some directions in $\boldsymbol\theta$-space are fundamentally unresolvable from the available data. Any attribution in the unidentifiable directions relies on prior beliefs, not evidence.

**3. The posterior correlation barrier.** Even for approximately identifiable cases, any factored representation (independent Beta posteriors per edge) necessarily discards the correlation introduced by failure at multi-parent nodes. The exact posterior complexity grows exponentially with the number of observed failures. The factored representation is an approximation by construction — coupled corrections are inherent to the problem, not an artifact of a bad algorithm.

### The Design Requirement

*[Discussion (credit-assignment-design-requirement)]*

The theory does not prescribe a specific credit-assignment scheme. It states what any scheme must satisfy for the persistence guarantees to hold:

**Minimal requirement (from #der-gain-sector-bridge):** The per-edge signal function must have **directional fidelity** — the expected update for each edge must point toward the true credence:

$$\mathbb{E}[(\text{signal}(o_t, i, j) - p_{ij}) \cdot (p_{ij} - \theta_{ij})] \leq 0$$

(the expected correction is non-positively correlated with the current error). This is the per-component version of condition B1 from the bridge theorem. Any signal function satisfying this produces sector-satisfying corrections that transfer losslessly to value space (Prop B.5b, componentwise case).

**Sufficient condition for persistence:** Per-component directional fidelity + bounded gain ($\eta_{\text{edge}} \gt 0$). The theory guarantees persistence when these hold, regardless of how the signals are computed.

**What's NOT required:** Exact attribution, unbiased estimation, minimum-variance estimation, or optimality of any kind. The persistence guarantee is robust to approximation — a sloppy but directionally correct signal function still produces bounded strategic mismatch. The *quality* of the approximation affects the *tightness* of the persistence bound (how close $R^\ast_\Sigma$ is to zero), not whether persistence holds at all.

### The Hierarchy of Credit Assignment Quality

| Level | Requirement | What it buys | Cost |
|---|---|---|---|
| **0** (none) | Plan-level tracking only | Persistence guarantee (Prop B.5) | No per-edge diagnostics |
| **1** (directional) | Directional fidelity per edge | Persistence + rough per-edge diagnostics | Gradient computation $O(\lvert V\rvert + \lvert E\rvert)$ |
| **2** (approximate) | Proportional blame / expectation propagation | Persistence + per-edge diagnostics (with bias) | Factor-graph inference |
| **3** (exact) | Full Bayesian posterior | Persistence + optimal per-edge calibration | \#P-hard (general case) |

AAT's formal guarantees require only Level 0. Practical agents need at least Level 1 for adaptive behavior — and the default signal function (above) provides a concrete Level 1 scheme. Level 2 is the sweet spot for most applications. Useful Level 2 factor-graph approximations include: exact Belief Propagation (BP) on tree or polytree cases, loopy BP or max-sum for MAP-style diagnosis, Expectation Propagation (EP) for approximate marginals, and structured variational methods only where common-cause structure is explicitly modeled. Level 3 is a mathematical ideal that is computationally unattainable in the general case.

## Epistemic Status

*Mixed.* The default signal function (gradient-based attribution, stated in log-odds) is a *formulation* — a concrete, well-motivated representational choice analogous to the gain principle's $\eta^\ast$ formula. It satisfies directional fidelity for monotone AND/OR DAGs (derivable from Jacobian non-negativity). The log-odds presentation is *canonically selected* by the evidential-additivity axiom — the unique additive-evidence parameterization up to positive affine transformation ( #deriv-edge-update-natural-parameter). The boundary characterization (tractable cases, intractability barriers, design requirement) is *discussion-grade*, with the intractability argument at sketch level and the design requirement derived from the bridge theorem ( #der-gain-sector-bridge, #deriv-edge-credence-dynamics Prop B.5).

**Historical note on the presentation choice.** An earlier probability-space presentation of the default signal function, written as

$$\text{signal}_k = p_k + \iota_k \cdot J_k(y_G - \hat P_\Sigma)/\lVert\mathbf{J}\rVert^2$$

with the update $p_k^{\text{new}} = p_k + \eta(\text{signal}_k - p_k)$, exhibited a mechanical break: when $\lVert\mathbf{J}\rVert^2 \to 0$ the signal magnitude could push $p_k^{\text{new}}$ outside $[0, 1]$. The log-odds presentation above eliminates this failure mode by construction. Props B.1–B.7 of #deriv-edge-credence-dynamics remain as stated — their sector-parameter content is Fisher-equivalent across parameterizations, and the moment-parameter form is retained for algebraic clarity. The current segment writes the *default* signal in log-odds (native coordinate), with the moment-parameter form understood as the projected image via sigmoid.

Max attainable: *conditional* — with a formal intractability reduction, the boundary characterization could be promoted. The design requirement is already exact (it follows from the bridge theorem). The log-odds presentation is *derived-conditional* (on the evidential-additivity axiom) via #deriv-edge-update-natural-parameter, structurally parallel to the reverse-KL uniqueness result under the chain-rule axiom in #deriv-strategy-cost-regret-bound §6.1.

## Discussion

**AAT characterizes the structure, not the algorithm.** The theory's contribution to credit assignment is not a solution but a characterization: when it's trivial (observable intermediates), when it's hard (general partial observability), what any solution must satisfy (directional fidelity), and what guarantees hold without it (persistence, plan-level diagnostics). This is the right level of ambition for a theory of adaptive systems — the specific algorithm is domain-specific engineering; the structural characterization is universal.

**The analogy to the gain principle.** #emp-update-gain characterizes the optimal gain structure ($\eta^\ast = U_M/(U_M + U_o)$) without prescribing how $U_M$ and $U_o$ are estimated. A Kalman filter computes them exactly; an RL agent approximates them; a human intuits them. The gain *principle* is theory; the gain *estimator* is engineering. Credit assignment has the same structure: the *requirement* (directional fidelity) is theory; the *implementation* (proportional blame, gradient attribution, belief propagation) is engineering.

**The observability lever.** The most powerful insight from this analysis is that credit assignment is primarily an *observability design problem*, not an algorithm design problem. An agent that designs its strategy with observable intermediates (instrumented plans, staged rollouts, checkpoints) sidesteps the intractability entirely. This connects to #der-observability-dominance's practical guidance: invest in making intermediate states observable, because unobservable regions are both epistemically dead (frozen credences) and computationally intractable (no efficient attribution).

**OKRs as observability-by-design.** The Objectives and Key Results framework is a direct organizational instantiation of this principle. The OKR discipline converts a deep, partially-unobservable strategy DAG (objective → vague initiatives → daily actions) into one with explicitly observable intermediate nodes (objective → measurable Key Results → tracked initiatives). In AAT terms: Key Results are intermediate nodes with $\sigma_v \approx 1$ by construction, making credit assignment between actions and objectives componentwise (Prop B.2) rather than intractable.

OKR failure modes map to AAT predictions:

| OKR Failure | AAT Analog | Formal Quantity | Consequence |
|---|---|---|---|
| **Vanity metrics** (measurable but irrelevant) | Observable node not causally connected to objective | High $\sigma_v$, low $p_{ij}$ | Edge updates, but the edge doesn't lead where the agent thinks — correction effort is wasted |
| **Too many Key Results** | Wide OR-node exploration-gating | $\alpha_\Sigma \propto 1/k$ (Prop B.4) | Correction capacity diluted across alternatives; persistence threshold harder to meet |
| **Lagging indicators** | Evidence starvation by delay | $\nu_{\text{obs}} \ll \rho$ | By the time the KR is measured, the correction window has passed; mismatch accumulated beyond $R_\Sigma$ |
| **Goodhart's Law** (metric becomes the goal) | Terminal-condition misalignment with $O_t$ | $V_{O_t}(\tau) \lt V_{O_t}^{\min}$ despite terminals achieved | Well-formedness constraint ( #def-strategy-dag) violated; agent optimizes the intermediate rather than the objective |

This is not an analogy — it is a domain instantiation. The same formal machinery that predicts when strategic persistence holds also predicts when OKRs work: when Key Results are genuinely causally connected to the Objective ($p_{ij}$ is high and calibrated), few enough to monitor effectively ($k$ is small), and measured on a timescale that permits correction (observation rate exceeds environment drift rate). The TST bridge to software team dynamics runs through exactly this connection.

## Working Notes

- A formal reduction from AND/OR credit assignment to Shapley value computation would promote the intractability claim from sketch to derived. The key step: mapping the AND/OR propagation to a weighted threshold game.
- The proportional-blame heuristic (attribute in proportion to prior credence) satisfies directional fidelity for independent edges. Does it satisfy directional fidelity in general? The two-edge analysis (B.3) shows it introduces O(1/n) bias — which means it has directional fidelity in expectation but not per-step. Whether the expected-value directional fidelity is sufficient for the sector condition (it should be, since the sector condition is also stated in expectation) is worth verifying formally.
- The connection between AAT's credit assignment and RL's temporal credit assignment (TD learning, eligibility traces) deserves formal treatment. Both face the same structural problem (partial observability of the causal chain) and both use similar heuristics (discounted attribution to recent actions). AAT's DAG structure is richer than RL's linear temporal chain, which may make the problem harder but also provides more structural information.
- The log-odds presentation of the default signal function (this segment) closes the Finding 2 mechanical break by construction ( `audits/pending-findings-2026-04-22.md` §Finding 2, `spikes/spike-gbp1-logit-scoping.md`). Props B.1–B.7 remain in moment-parameter form because Fisher-equivalence keeps their sector-parameter content parameterization-agnostic; if a future pass moves the entire strategy layer to log-odds as its primary coordinate (full G-BP1 execution, likely paired with G-BP3 Fisher unification), the Prop B.1–B.7 restatements should follow. The scoping found the current narrow fix sufficient.

### Incidental audit gold (lift 2026-05-31, batch A9)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. *Orthogonal* material (pedagogical framing, analogies, candidate figures, reader-confusion signals), staged for an eventual careful promotion pass, kept separate from the certified theory-fix findings. **Coverage for this segment:** 193847, 361742, 471203, 526815, 584721, 773921, 829314, 849201. (Multiple substrates rated this segment top-decile, principally for the OKR mapping.)

#### 1. Candidate Brief prose / pre-prose

- **"Observability is the lever, not algorithm design."** The segment's headline reframing, independently named by nearly every substrate: credit assignment is "primarily an *observability design problem*, not an *algorithm design problem*" — invest in observable intermediates rather than smarter attribution algorithms (Claude/849201, 361742, 584721; Gemini/773921). A candidate Brief / Discussion thesis line.
- **The four-level credit-assignment hierarchy as the clean tiering.** Level 0 (plan-level, none) suffices for *persistence*; Level 1 (directional) for *adaptive behavior*; Level 2 is the practical sweet spot; Level 3 (exact Bayesian) is #P-hard. Most ML literature implicitly demands Level 3; AAT's claim that Level 1 suffices for the formal guarantees is the distinctive, citable move (Claude/584721, 471203, 361742).

#### 2. Candidate Discussion

- **OKRs as observability-by-design — the standout domain instantiation.** Universally hailed (Claude/193847, 584721, 471203; Gemini/829314, 773921, 849201) as the framework's clearest reach into management practice. The mechanism: a deep CEO→…→Revenue DAG has unobservable intermediates, so exact attribution is #P-hard and learning freezes; a "Key Result" is a *forced, observable intermediate node* ($\sigma_v\approx 1$) that decomposes the #P-hard problem into trivial local $O(1)$ updates and localizes strategy-error vs execution-error. The failure-mode table is the load-bearing artifact (cited verbatim by 471203):
  - **Vanity metrics** — observable but causally disconnected (high $\sigma_v$, low $p_{ij}$).
  - **Too many KRs** — wide OR exploration-gating ($\alpha_\Sigma\propto 1/k$).
  - **Lagging indicators** — evidence starvation by delay ($\nu_{\text{obs}}\ll\rho$).
  - **Goodhart's Law** — terminal-condition misalignment ($V_{O_t}(\tau)\lt V_{O_t}^{\min}$ despite terminals achieved).
  One auditor's adversarial caution worth recording: the four modes are *known* management pathologies, so the genuine predictive test is whether AAT predicts a *new* OKR failure mode absent from the standard literature (candidate: the `#der-observability-dominance` "absorbing-state" prediction applied to organizational measurement gaps) (Claude/471203). A sharpening of the *mechanism*: OKRs work, when they work, because each Key Result is an *observable intermediate node* that converts the intractable (#P-hard) credit-assignment problem into the tractable componentwise case (Prop B.2) — "the OKR system is essentially an organizational protocol for the observability-investment strategy" (Claude/451729). Organizations routinely ask "which initiatives contributed most?" — exactly the #P-hard partial-observability credit-assignment problem, escapable only by observability investment.
- **Proportional blame *is* Bayesian marginalization, not a heuristic.** Worth surfacing as a "the intuition was right for a formal reason" Discussion note: for independent Beta-Bernoulli edges with an unobservable intermediate, "credit each edge in proportion to its prior responsibility" turns out to be exactly the optimal marginal Bayesian point estimate — the same pattern as EM's posterior-weighted latent updates and variational inference's credit-through-the-variational-posterior; "credit proportional to prior probability is Bayesian marginalization in disguise" (Claude/451729). (Complements the existing Working-Notes B.3 result that this marginal update is nonetheless *biased at truth* when fed back into a factored DAG.)
- **AAT-as-REINFORCE-with-causal-weighting.** The default signal reads as RL with a causal discount: "Jacobian is the score function, $(y_G-\hat P_\Sigma)$ is the advantage, $\iota_k$ is the causal-validity discount" — a candidate bridge to RL theory that also marks AAT's distinct contribution (Claude/584721).

#### 3. Follow-up items

- *(No framing-grade follow-ups beyond what Working Notes already track. The Codex/526815 items F60/F61/F62 are routed to the off-ramp — see lift report — as candidate findings: the gradient signal cannot point *every* edge toward its own truth from a single signed plan residual; the $\div\|J\|^2$ update is still unbounded as $\|J\|\to 0$ even in log-odds; the "causally insufficient DAG always overestimates" claim is topology-dependent in sign.)*

#### 4. Readers often ask / wonder

- **How do biological brains do #P-hard credit assignment?** Presumably localized approximations (gradient/backprop-like) plus heavy evolutionarily-enforced observability gating — a natural reader question the intractability result invites (Gemini/829314).
- **How does a Regime-C-only agent ever learn a strategy** if $\iota_k\approx 0$ zeroes its edge updates? (Claude/193847) — answered by combining priors + active probing, worth pre-empting.

#### 5. Candidate figures

- **Scalar-residual-fanned-onto-edges diagram.** One scalar plan residual projected onto several edge coordinates through the nonnegative Jacobian: when edge errors are aligned it works as a rough per-edge signal; when they have mixed signs the *same* residual sign is broadcast through all positive $J_k$, so some edge-local directions must be wrong (Codex/526815). Doubles as the figure *and* the visual statement of the F60 limitation.

#### Belongs elsewhere

- **Log-odds as the coordinate of *conviction* — trauma/phobia reading → `04-eli-core/`.** In probability space, learning "feels stopped" near $p=0.999$; in log-odds space the belief is still moving fast, and $|\lambda|\gg 0$ is the *depth of conviction* — how much counter-evidence it takes to change one's mind. A deep negative conviction ($\lambda=-100$) that the environment has since rendered safe needs a massive positive-evidence influx to drag back above zero: "the mathematical definition of trauma or phobia." Implication for consciousness infrastructure: monitor not just $p$-values but the *log-odds momentum* of an agent's beliefs to catch deep rigid convictions before they paralyze the strategy DAG (Gemini/193847). Aspirational reach pointing at interiority / memory material in `04-eli-core/`.
- **Credit-assignment ↔ RL temporal-credit-assignment formal treatment.** Already a Working-Notes item; the audits reinforce it as a cross-field bridge (TD-learning / eligibility traces vs AAT's richer DAG structure).
