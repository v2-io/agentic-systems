# Spike: Resolving the Interventional/Observational Edge Semantics Tension

**Status**: Spike (investigatory). Resolves the known fragility "edge semantics claim interventional but update from observational."

**Date**: 2026-04-02

**Objective**: State the tension precisely, analyze three candidate resolutions, recommend one, draft specific language changes for the affected segments, and address two secondary issues (the signal function gap and the $M_t$/edge evidence double-counting question).

**Depends on**: #strategy-dag, #edge-update-via-gain, #edge-update-causal-validity, #loop-interventional-access, #ciy-observational-proxy, #credit-assignment-boundary, #strategic-calibration, #causal-hierarchy-requirement, #chain-confidence-decay, #strategic-dynamics-derivation

---

## 0. The Tension, Stated Precisely

### 0.1 What is claimed, where

**Claim 1 (strategy-dag, Edge semantics).** Edge credences are defined as:

$$p_{ij} = \text{Cr}_i(j \text{ advances} \mid i \text{ completed},\, M_t)$$

The Discussion section explicitly connects this to Pearl: "The strategy DAG is a causal Bayesian network where the agent is both the modeler and the intervener. Pearl's do-calculus applies in intervention-rich domains where the agent can experimentally verify edge credences." The segment qualifies that "in confounded domains, the credence is weaker: it encodes the agent's best causal belief, but that belief may be biased by observational confounding."

**Claim 2 (loop-interventional-access).** "An agent in the feedback loop generates interventional data by construction: the agent's action $a_t$ causally precedes the next observation $o_{t+1}$." Status: exact. But the segment is careful: "this does not mean the agent automatically has access to a clean estimate of $P(o \mid do(a_t), \Omega_t)$."

**Claim 3 (edge-update-via-gain).** Edge credences update from execution data:

$$p_{ij}^{\text{new}} = p_{ij}^{\text{old}} + \eta_{\text{edge}} \cdot (\text{signal}(o_t, i, j) - p_{ij}^{\text{old}})$$

Status: hypothesis. The update rule draws evidence from whatever data the agent observes, with no mechanism enforcing that the data carries interventional content about the specific edge being updated.

**Claim 4 (edge-update-causal-validity).** Three regimes (A: intervention-rich, B: partial intervention, C: observation-only) classify how clean the causal identification is. The identifiability coefficient $\iota_{ij}$ modulates the gain. Status: conditional.

### 0.2 Where the inconsistency lies

The inconsistency is narrow but real. It is not between claim 1 and claim 3 in isolation --- both are carefully qualified. It is between the **conjunction** of these claims as they interact across segments:

1. **strategy-dag** defines $p_{ij}$ and its semantics in one place, using language ("causal credence," connection to Pearl's do-calculus) that implies the edges have interventional meaning.

2. **edge-update-via-gain** defines the update rule in a separate place, using a generic gain-based mechanism that works identically regardless of the causal regime.

3. **edge-update-causal-validity** acknowledges the gap but treats it as a *scope condition on the update*, not as a *revision of the edge semantics*.

The result: a reader tracing the dependency chain encounters $p_{ij}$ defined with interventional connotations in one segment, updated with an evidence-agnostic mechanism in a second, and told the update may not preserve the definition's semantics in a third. The tension is not that any single segment is wrong but that the **semantic contract between the definition and the update is unclear**. What does $p_{ij}$ *mean* after it has been updated from Regime C data? Is it still a "causal credence"? If so, in what sense?

### 0.3 What is NOT a problem

Several aspects that might look problematic are already adequately handled:

- **The three-regime classification** (edge-update-causal-validity) is excellent work. The tension is not that the regimes are wrong but that they scope the *update mechanism* without revising the *edge definition*.
- **loop-interventional-access** is precise about what it claims (data availability, not estimation quality). No issue there.
- **The identifiability coefficient** $\iota_{ij}$ is a sound mechanism for degrading the update gain when attribution is weak. It addresses the *magnitude* of the update but not the *semantics* of what $p_{ij}$ represents after the update.
- **credit-assignment-boundary** thoroughly characterizes when per-edge attribution is tractable. This is a computational question orthogonal to the semantic one.

The genuine gap is: **what does $p_{ij}$ mean as a theoretical quantity, given that its operational definition (the update rule) does not enforce the semantics implied by its definitional description?**

---

## 1. Resolution A: Soften the Claim

### The proposal

Change the edge semantics in strategy-dag from "causal credence" with interventional connotations to **"causal efficacy credence"** --- the agent's best estimate of how effective completing step $i$ is at advancing step $j$, given its current model and the best available evidence.

The key move: the definition would acknowledge from the start that $p_{ij}$ is the agent's *working belief about causal efficacy*, not a formal interventional probability. In Regime A, this working belief approximates $P(j \mid do(i), M_t)$ because the data supports it. In Regime C, it is a confounded estimate that the agent treats as if it were causal. The label makes the semantic gradient explicit.

### What changes

**strategy-dag edge semantics.** Replace the current:

> $p_{ij} = \text{Cr}_i(j \text{ advances} \mid i \text{ completed},\, M_t)$
>
> This is the agent's credence that completing step $i$ causally advances step $j$

with a formulation that makes the semantic scope explicit from the definition.

**edge-update-via-gain.** No change needed. The update rule is already regime-agnostic by design.

**edge-update-causal-validity.** Reframe from "where the update preserves interventional semantics" to "where the working credence is a good estimate of causal efficacy." The three regimes remain unchanged; only the framing shifts.

### Assessment

**Strengths.** Honest. Simple. Requires minimal structural change. The theory already has all the machinery (three regimes, $\iota_{ij}$, CIY admissibility) to say precisely when the working credence is good and when it is weak. Softening the claim aligns the definition with what the formalism actually delivers.

**Weaknesses.** "Causal efficacy credence" is vague enough that a hostile reader could ask: "what does this mean formally?" The answer is "the agent's subjective probability, updated via the gain principle, interpreted causally by the agent for planning purposes" --- which is operationally clear but philosophically murky. It also loses the direct connection to Pearl's do-calculus, which was one of the formalism's appealing features.

**Verdict.** Workable but slightly unsatisfying. The definition becomes less precise in exchange for honesty about what the formalism delivers.

---

## 2. Resolution B: Strengthen the Update

### The proposal

Keep the interventional semantics ($p_{ij} = \text{Cr}(j \mid do(i), M_t)$) but restrict the update mechanism to preserve those semantics:

- **Regime A edges** update via the gain principle as currently specified. These updates preserve the interventional interpretation.
- **Regime B/C edges** are *not* updated via the standard gain mechanism. Instead, they maintain their prior credences (or a separate, weaker mechanism updates an "observational estimate" $\hat p_{ij}$ that is explicitly not $p_{ij}$).

The key move: the update mechanism is conditioned on the regime. Interventional credences are updated only from interventional data.

### What changes

**edge-update-via-gain.** Adds a precondition: the update applies only when $\iota_{ij}$ exceeds some threshold, or equivalently, only in Regime A (and the strong end of Regime B).

**strategy-dag.** No change to the definition. The interventional semantics are preserved.

**edge-update-causal-validity.** Becomes load-bearing in a new way: it determines not just the *quality* of the update but whether the update *applies at all*.

### Assessment

**Strengths.** Semantically clean. $p_{ij}$ means one thing everywhere. The connection to Pearl is preserved. The theory can make strong statements about Regime A agents.

**Weaknesses.** Practically crippling for the theory's generality. Most real-world agents (organizational, military, political) operate in Regimes B and C. A theory that can only update edge credences in Regime A is a theory of software agents and laboratory scientists, not a general theory of purposeful agency. It also creates an awkward two-tier system: some edges are "real" (updatable) and some are "frozen" (stuck at priors), with the boundary determined by a regime classification that is itself domain-dependent and hard to assess in practice.

Furthermore, the "frozen at prior" treatment is epistemically dishonest in a different way. An agent in Regime C that repeatedly observes associations between $i$-completion and $j$-advancement *should* update its beliefs, even if the update is confounded. Forbidding the update in the name of semantic purity means the agent ignores useful (if imperfect) evidence.

**Verdict.** Too restrictive. The semantic precision comes at the cost of theoretical generality and practical applicability. A theory of adaptive agents should not forbid adaptation in the majority of real domains.

---

## 3. Resolution C: Separate the Layers

### The proposal

Each edge carries two quantities:

- $p_{ij}^I$: **interventional credence** --- the agent's best estimate of $P(j \mid do(i), M_t)$, updated only from data with adequate causal identification (Regime A, strong Regime B).
- $p_{ij}^O$: **operational credence** --- the agent's working estimate, updated from all available evidence via the standard gain mechanism.

The agent uses $p_{ij}^O$ for status propagation and planning. The identifiability coefficient $\iota_{ij}$ bridges the two:

$$p_{ij}^O \approx p_{ij}^I \quad \text{when } \iota_{ij} \approx 1$$

When $\iota_{ij} \ll 1$, the agent knows that $p_{ij}^O$ may diverge from $p_{ij}^I$ and should treat its plan-confidence score with appropriate skepticism.

### What changes

**strategy-dag.** Edge parameterization doubles: each edge carries $(p_{ij}^I, p_{ij}^O)$ or equivalently $(p_{ij}^O, \iota_{ij})$ where $\iota_{ij}$ encodes the gap between operational and interventional credences.

**edge-update-via-gain.** Two update rules: one for $p_{ij}^O$ (always active, current mechanism), one for $p_{ij}^I$ (active only under adequate identification).

**Status propagation.** Uses $p_{ij}^O$. The plan-confidence score $\hat P_\Sigma$ is explicitly an operational quantity.

### Assessment

**Strengths.** Conceptually precise. Each quantity has clear semantics. The agent has an explicit model of its own epistemic limitations (the gap between operational and interventional credences). This could feed into sophisticated meta-reasoning: "I believe this edge works (high $p^O$) but I don't causally know why (low $\iota$), so I should seek probe actions."

**Weaknesses.** Doubles the parametric complexity of every edge. Violates the design principle that converged on single-parameter edges (#and-or-scope). The theory fought hard to get to one number per edge; adding a second re-opens questions that were settled. The $\iota_{ij}$ bridge is already available in edge-update-causal-validity as a gain modulator --- promoting it to a first-class edge parameter adds notational weight without clear theoretical benefit.

More fundamentally, this resolution reifies a distinction that may not be meaningful in practice. For most edges, the agent has no way to independently estimate $p_{ij}^I$ --- it has only the data it has. The "interventional credence" becomes a ghost quantity: formally defined but operationally inaccessible except in Regime A, where it equals $p_{ij}^O$ anyway.

**Verdict.** Over-engineered. The conceptual precision is real but the practical cost is too high. The theory's elegance depends on single-parameter edges, and the two-layer system adds complexity without proportional insight.

---

## 4. Recommendation: Resolution A, Enhanced

### Why Resolution A

Resolution A is the right choice because it honestly aligns the definition with what the formalism delivers. The key insight: **the existing three-regime classification in edge-update-causal-validity already does most of the work**. What is missing is not new machinery but a clearer semantic contract in strategy-dag that acknowledges the regime-dependent interpretation from the start.

The theory's strength is that it has the $\iota_{ij}$ machinery (from edge-update-causal-validity) and the CIY admissibility classification (from ciy-observational-proxy) to say precisely when edge credences carry interventional force and when they are confounded estimates. The gap is that strategy-dag's *definition* does not reference this machinery --- it defines $p_{ij}$ as if it always has interventional content, and then edge-update-causal-validity cleans up afterward.

### The enhancement: regime-indexed interpretation

Resolution A becomes fully precise with one addition: the edge definition explicitly states that the *interpretation* of $p_{ij}$ varies with the identification regime.

This is not vagueness --- it is a scope-indexed definition, analogous to how loop-interventional-access distinguishes between "the data is interventional in character" and "the agent has access to a clean causal estimate." The edge credence $p_{ij}$ is always the agent's best estimate of how effective $i$-completion is at advancing $j$. The *causal content* of that estimate depends on the data that produced it:

| Regime | $p_{ij}$ interpretation | Formal status |
|--------|------------------------|---------------|
| **A** | Approximates $P(j \mid do(i), M_t)$ | Interventional credence |
| **B** | Partially identified causal estimate with known bias direction | Confounded causal credence |
| **C** | Observational association treated as causal for planning | Associational proxy for causal credence |

This is not three different quantities --- it is one quantity ($p_{ij}$) whose epistemic warrant varies with the data regime. The single-parameter edge is preserved. The gain-based update is preserved. What changes is the *interpretive frame* surrounding the definition.

### Why not B or C

**Resolution B** (restrict updates to Regime A) sacrifices the theory's generality. AAD aims to cover agents from software bots to military commanders. Restricting edge updates to intervention-rich domains makes it a theory of Regime A agents with an acknowledgment that other agents exist. This is the wrong scope for a general framework.

**Resolution C** (two-layer edges) violates the single-parameter-edge design principle that three independent formalism attempts converged on. The $\iota_{ij}$ coefficient already exists as a gain modulator in edge-update-causal-validity --- promoting it to a first-class edge parameter adds weight without theoretical return. The ghost-quantity problem (interventional credence is operationally inaccessible except where it equals the operational credence) makes the separation formally tidy but practically empty.

---

## 5. Drafted Language Changes

### 5.1 strategy-dag: Edge semantics paragraph

**Current text:**

> **Edge semantics.** Each edge carries a single causal credence weight:
>
> $$p_{ij} = \text{Cr}_i(j \text{ advances} \mid i \text{ completed},\, M_t)$$
>
> This is the agent's credence that completing step $i$ causally advances step $j$, given its current model. In **intervention-rich domains** (software, laboratory science --- where the agent performs genuine experiments), this credence approximates the interventional probability $P(j \mid do(i), M_t)$. In **confounded domains** (military, organizational --- where evidence is delayed, correlated, or strategically distorted), the credence is weaker: it encodes the agent's best causal belief, but that belief may be biased by observational confounding. The strength of the causal interpretation depends on the domain's identifiability conditions ( #causal-information-yield, admissibility regimes).

**Proposed replacement:**

> **Edge semantics.** Each edge carries a single credence weight:
>
> $$p_{ij} = \text{Cr}(j \text{ advances} \mid i \text{ completed},\, M_t)$$
>
> This is the agent's credence that completing step $i$ advances step $j$, given its current model --- its **causal efficacy estimate** for the link. The agent treats $p_{ij}$ as a causal quantity for planning purposes (status propagation, plan-confidence scoring, action selection). Whether $p_{ij}$ is a *good* estimate of causal efficacy depends on the identification regime of the data that produced it ( #edge-update-causal-validity):
>
> - **Regime A** (intervention-rich: software, laboratory science). The agent's execution-observation pairs are genuine interventions with clean attribution. $p_{ij}$ approximates the interventional probability $P(j \mid do(i), M_t)$.
> - **Regime B** (partial intervention: organizational, coordinated action). The agent acts but attribution is blurred by concurrent actions and self-selection. $p_{ij}$ is a partially identified causal estimate, typically biased upward.
> - **Regime C** (observation-only: passive monitoring, intelligence analysis). The agent observes associations but does not intervene. $p_{ij}$ is an observational proxy for the causal quantity --- useful for planning but potentially confounded.
>
> The identifiability coefficient $\iota_{ij}$ ( #edge-update-causal-validity) quantifies the strength of the causal interpretation for each edge. When $\iota_{ij} \approx 1$, the agent's credence is well-identified causally. When $\iota_{ij} \approx 0$, the credence is associational. The single-parameter edge design is preserved: $p_{ij}$ is always the agent's working estimate, with $\iota_{ij}$ characterizing its causal warrant separately.

### 5.2 strategy-dag: Discussion paragraph on Pearl

**Current text:**

> **Connection to Pearl's framework.** The strategy DAG is a causal Bayesian network where the agent is both the modeler and the intervener. Pearl's do-calculus applies in intervention-rich domains where the agent can experimentally verify edge credences. In confounded domains, the DAG degrades to a "best causal belief" structure --- useful for planning but with acknowledged potential for systematic bias.

**Proposed replacement:**

> **Connection to Pearl's framework.** The strategy DAG shares structure with a causal Bayesian network: directed edges, propositional nodes, and a probabilistic factorization. In Regime A domains, where the agent performs genuine interventions and observes isolated outcomes, the DAG's edge credences approximate interventional probabilities, and Pearl's do-calculus applies to status propagation and plan evaluation. In Regimes B and C, the edge credences are the agent's working causal beliefs, updated from data of weaker identification strength. The DAG remains useful for planning --- the agent must act on *some* causal model --- but the plan-confidence score $\hat P_\Sigma$ inherits the identification weaknesses of its constituent edges. An agent operating primarily in Regime C should treat $\hat P_\Sigma$ as a rough heuristic, not a calibrated probability. The regime-indexed interpretation (above) makes this gradient explicit rather than leaving it as a caveat.

### 5.3 edge-update-via-gain: Summary sentence

**Current text:**

> The uncertainty-ratio gain principle ( #update-gain) extends from epistemic updates to strategy-edge updates: edge credences revise in proportion to the ratio of edge uncertainty to observation noise. This gives a principled, conservative update rule that avoids overreacting to single observations.

**Proposed replacement:**

> The uncertainty-ratio gain principle ( #update-gain) extends from epistemic updates to strategy-edge updates: edge credences revise in proportion to the ratio of edge uncertainty to observation noise, modulated by the identifiability of the causal link ( #edge-update-causal-validity). This gives a principled, conservative update rule that avoids overreacting to single observations and degrades gracefully when causal identification is weak.

### 5.4 edge-update-causal-validity: Opening sentence

**Current text:**

> The gain-based edge update ( #edge-update-via-gain) revises interventional credences $p_{ij}$ using execution data. This data is interventional in character ( #loop-interventional-access) but varies in identification strength depending on the edge's position in the DAG and the domain's causal structure.

**Proposed replacement:**

> The gain-based edge update ( #edge-update-via-gain) revises edge credences $p_{ij}$ --- causal efficacy estimates whose identification strength varies with the data regime ( #strategy-dag). This segment scopes where the update yields credences that approximate the interventional quantity $P(j \mid do(i), M_t)$, where it yields partially identified estimates, and where it yields associational proxies.

---

## 6. The Signal Function Gap

### 6.1 Current state

The signal function $\text{signal}(o_t, i, j)$ is acknowledged as the critical missing piece in edge-update-via-gain. Partial progress from strategic-dynamics-derivation:

- **Binary outcomes, observable intermediate (Prop B.2):** signal is trivial ($y_B$ for edge 1, $y_G$ for edge 2 given $y_B = 1$). Sector condition verified with $\alpha_\Sigma = \min(1/(n_1+1), \theta_1/(n_2+1))$.
- **Binary outcomes, unobservable intermediate (Prop B.3):** proportional-blame signal $q_k = P(\text{edge } k \text{ caused failure} \mid y_G = 0)$ is the marginal Bayesian point estimate. Correct as a Bayesian computation but produces $O(1/n)$ bias in the factored representation.
- **credit-assignment-boundary:** default gradient-based signal $\text{signal}_k(o_t) = p_k + J_k \cdot (y_G - \hat P_\Sigma) / \lVert\mathbf{J}\rVert^2$ satisfies directional fidelity for monotone AND/OR DAGs.
- **Open:** continuous outcomes, multi-parent nodes, general DAG topologies.

### 6.2 How the resolution affects the signal function

The regime-indexed interpretation (Resolution A, enhanced) has a clarifying effect on the signal function specification. The signal function decomposes into three sub-problems, which now align with the three regime-dependent aspects of the edge definition:

$$\text{signal}(o_t, i, j) = f(\underbrace{\text{outcome}(o_t, j)}_{\text{what happened at } j}, \underbrace{\text{attribution}(o_t, i, j)}_{\text{was it because of } i?}, \underbrace{\text{regime}(i, j)}_{\text{how causal is the evidence?}})$$

In Regime A, the attribution component is strong (high $\iota_{ij}$), and the signal function reduces to the clean cases already solved (Props B.2, B.3, gradient-based default). In Regime C, the attribution component is weak, and the signal function should produce a conservative update --- which is exactly what the identifiability-adjusted gain ($\eta_{\text{edge}}^{\text{adj}} = \eta_{\text{edge}} \cdot \iota_{ij}$) already delivers.

The resolution does *not* solve the signal function for continuous outcomes or multi-parent nodes. But it clarifies the relationship: the signal function is the *outcome extraction* and *attribution* mechanism; the $\iota_{ij}$ coefficient handles the *regime-dependent causal interpretation*. These are separable concerns. The signal function can be specified independently of the regime question, and the regime question (now resolved by the edge semantics revision) modulates the overall update strength.

### 6.3 Concrete specification path

The signal function specification should proceed in layers, matching the credit-assignment hierarchy (credit-assignment-boundary):

| Level | Signal function | Requirement | Status |
|-------|----------------|-------------|--------|
| **0** | None (plan-level tracking only: $y_G - \hat P_\Sigma$) | None | Solved (B.5) |
| **1** | Gradient-based: $\text{signal}_k = p_k + J_k(y_G - \hat P_\Sigma)/\lVert\mathbf{J}\rVert^2$ | Directional fidelity | Solved (credit-assignment-boundary) |
| **2** | Observable-intermediate: direct observation of each node | Full observability | Solved (B.2) |
| **3** | Proportional blame: marginal Bayesian for unobservable nodes | Binary outcomes, known structure | Solved with $O(1/n)$ bias (B.3) |
| **4** | Continuous/multi-parent | General specification | Open |

The gradient-based signal (Level 1) is the recommended default because it satisfies directional fidelity, is computable in $O(\lvert V\rvert + \lvert E\rvert)$, and works for arbitrary AND/OR DAG topologies. Agents with richer observation structure can do better (Levels 2--3).

---

## 7. The $M_t$/Edge Evidence Double-Counting Question

### 7.1 The concern

The orient cascade (#orient-cascade) processes $M_t$ first (step 1), then edge updates (step 4). Both use the same observation $o_t$. The concern: when the $M_t$ update extracts information from $o_t$, and the edge update also uses $o_t$ (possibly via the updated $M_t$), is there double-counting of evidence?

### 7.2 Analysis: the concern is mostly unfounded

The $M_t$ update and the edge update extract **different information from the same observation**. They answer different questions:

- $M_t$ update: "what does $o_t$ tell me about the state of the world?"
- Edge update: "what does $o_t$ tell me about whether completing step $i$ advanced step $j$?"

These are distinct inference targets. The observation $o_t$ can be informative about both without either "using up" the other's evidence. This is analogous to how a single blood test result simultaneously updates a doctor's belief about the patient's kidney function ($M_t$) and the doctor's belief about whether the prescribed medication is working (edge credence).

### 7.3 Where a real issue exists

There is a genuine (but bounded) concern in one specific configuration: when $M_t$'s update changes the **leaf credences** $p_v(M_t)$, and the edge update then uses the **same observation** that drove the $M_t$ change.

Concretely: suppose $o_t$ reveals that condition $C_v$ holds (a condition leaf). The $M_t$ update incorporates this, changing $\Pr(C_v(\tau_v) \mid M_t)$ from 0.3 to 0.9. Then the edge update for the edge above $C_v$ uses the same $o_t$ as evidence that the edge works. The leaf credence change already propagates through status propagation to update $\hat P_\Sigma$. If the edge update also treats $o_t$ as evidence about the edge, the observation has influenced the plan-confidence score through two channels: once via the leaf credence, once via the edge credence.

### 7.4 Why the impact is bounded

This double-channel effect is bounded because:

1. **Leaf credences and edge credences are about different things.** The leaf credence $p_v(M_t)$ answers "will condition $C_v$ hold?" The edge credence $p_{ij}$ answers "if $i$ is completed, does that advance $j$?" Observing that $C_v$ holds is directly informative about the leaf credence but only indirectly informative about edge credences (through downstream status propagation).

2. **The gain mechanism is self-correcting.** Even if the edge update double-counts by incorporating $o_t$ into both the leaf credence (via $M_t$) and the edge credence (via the signal function), the gain $\eta_{\text{edge}}$ scales with $U_{\text{edge}}$, which decreases as the edge accumulates evidence. Systematic double-counting would produce a transient over-correction that subsequent observations would correct.

3. **The cascade ordering is the right response.** By processing $M_t$ first, the cascade ensures that edge updates operate against the most current model. This is the correct information-flow direction. The alternative (updating edges on stale $M_t$) would be worse --- it would attribute edge success/failure incorrectly because the background model is out of date.

### 7.5 Practical recommendation

The double-counting concern does not warrant architectural changes. The cascade ordering is correct. The practical impact is a slight over-correction in edge credences immediately after large $M_t$ revisions --- a transient effect that self-corrects under the gain mechanism. An agent that wanted to be fastidious could condition the edge signal on the *innovation* component of $o_t$ (the part not predicted by the prior $M_t$), but this adds complexity for marginal benefit.

This should be noted as a known, bounded effect in edge-update-via-gain's Working Notes, not elevated to a formal concern.

---

## 8. Summary of Recommendations

| Item | Recommendation | Affected segments |
|------|---------------|-------------------|
| **Edge semantics** | Resolution A (enhanced): regime-indexed causal efficacy estimate. Single-parameter edge preserved. | strategy-dag (definition + discussion), edge-update-causal-validity (framing) |
| **Edge update rule** | No structural change. Add forward reference to $\iota_{ij}$ in the summary sentence. | edge-update-via-gain (summary) |
| **Signal function** | Adopt gradient-based signal as concrete Level 1 default. Layer higher-quality signals on top. No change to the specification path. | credit-assignment-boundary (already done), edge-update-via-gain (reference) |
| **$M_t$/edge double-counting** | Note as bounded effect in Working Notes. No architectural change. | edge-update-via-gain (working notes) |
| **WORKBENCH fragility** | Reclassify from "known fragility" to "resolved (scope narrowing)." | WORKBENCH.md |

### What this resolves

- The "edge semantics claim interventional but update from observational" fragility is resolved by acknowledging that $p_{ij}$ is a working estimate whose causal warrant varies with the identification regime. The theory does not claim interventional precision where it cannot deliver it.
- The semantic contract between strategy-dag and edge-update-via-gain is clarified: strategy-dag defines what $p_{ij}$ represents (causal efficacy estimate, regime-indexed), edge-update-via-gain specifies how it is revised (gain principle, modulated by $\iota_{ij}$), and edge-update-causal-validity scopes where the revision yields credences of various causal strengths.

### What this does NOT resolve

- The signal function for continuous outcomes and multi-parent nodes remains open.
- The $O(1/n)$ bias in unobservable-intermediate credit assignment (Prop B.3a) is unchanged.
- The edge-independence assumption in status propagation is unchanged.
- The P3 $\to$ Markov step in graph uniqueness is unchanged.

These are genuine open problems that are orthogonal to the edge semantics question.
