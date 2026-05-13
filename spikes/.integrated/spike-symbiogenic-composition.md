# Spike: Symbiogenic Composition and Teleological Unity as Scope Condition

**Status**: Spike — structural reframing proposal for Section III. Two convergent findings integrated into a single proposal.

**Date**: 2026-04-20

**Motivation**: Two findings converged in a single session.

1. Careful reading of Miller (2022) *Ex Machina* Appendix B (Social Symbiogenesis) revealed a composition mechanism genuinely missing from AAD: hierarchical absorption / innovation-by-parts, qualitatively distinct from peer coupling (current Section III) and from the extreme-transition motif (`spikes/spike-miller-act-bridge.md`).
2. Joseph observed that teleological unity $U_O$ "may need to be controlled and/or assumed as definitional" — unlike the other three unity dimensions, which behave as quality metrics.

These findings are not independent. **Symbiogenesis is the mechanism by which teleological unity emerges from zero to one.** Taken together, they propose a restructuring of Section III: composition has an *existence condition* (teleological unity) distinct from its *quality metrics* (the other unities, update heterogeneity, closure defect); symbiogenesis is the specific dynamical process that creates composite-agent identity by crossing the existence condition from below.

**Depends on**: #scope-agency, #def-unity-dimensions, #form-composition-closure, #der-directed-separation, #form-structural-change-as-parametric-limit, #scope-multi-agent, `spikes/spike-miller-act-bridge.md`, `spikes/spike-unity-closure-mapping.md`, Miller (2022) Appendix B.

---

## 1. The Reframing Proposal

### 1.1 Current framing

`#def-unity-dimensions` treats the four unity dimensions ($U_M$, $U_O$, $U_\Sigma$, $U_{\text{obs}}$) as substantially independent parameters characterizing composite quality. `#form-composition-closure` treats a group as forming a composite whenever an admissible projection with small closure defect exists. The question "is there actually a composite here, or merely a group coincidentally approximable by a macro-description?" is not explicitly asked.

### 1.2 Proposed framing

**Teleological unity $U_O$ is a scope condition for composition**, paralleling `#scope-agency` for single agents. The other unities and update-heterogeneity parametrize composite *quality*, given that composition exists.

*[Scope (composition-scope-condition, proposed)]*

A set of purposeful sub-agents $\{A_1, \ldots, A_N\}$, each satisfying `#scope-agency`, constitutes a composite agent iff there is sufficient teleological alignment: $U_O \geq \epsilon_{\text{comp}}$ for some operationalization of $U_O$ and threshold $\epsilon_{\text{comp}}$.

Three sufficient routes (weakest to strongest):

(C-i) **Shared objective**: there exists $O_c$ such that each sub-agent's effective policy is $\epsilon$-compatible with $O_c$-optimal.
(C-ii) **Hierarchical derivation**: the sub-agents' objectives $\{O_i\}$ are derivable as sub-objectives of a common parent objective $O_c$.
(C-iii) **Minimum mutual benefit**: there exists a relevance variable for which all sub-agents' actions are marginally beneficial (analog of Miller's IAM definition's "mutual benefit" requirement).

When none of these hold, the agents are a valid object of study — a multi-agent system per `#scope-multi-agent` — but are not a composite agent. AAD's composition machinery (closure defect, team persistence, tempo composition) does not apply to them in the composite sense.

### 1.3 Why this matters

The current framework treats composite-existence as a derived question: a low-$\varepsilon^\ast$ projection implies a valid macro-agent. But two sub-agents with orthogonal objectives may admit a low-$\varepsilon^\ast$ projection without there being any meaningful composite. The composite's purposeful substate $G_c = (O_c, \Sigma_c)$ is ill-defined when sub-agents' purposes do not align: *whose* objective is the composite pursuing?

With $U_O$ as scope condition, the existence question is asked first. For composites that exist, the quality question (closure defect, tempo composition, persistence) is well-posed. For agent groups below the threshold, the theory correctly refuses to apply composite concepts.

This parallels the single-agent case. A thermostat-in-environment satisfies `#scope-agency` and is an agent whose adaptive tempo we can measure; a rock-in-environment is not an agent, and asking for its tempo is a category error. The composite analog: aligned-purpose sub-agents form a composite we can analyze; orthogonal-purpose sub-agents form a multi-agent system, for which asking about composite tempo is the same category error.

---

## 2. Social Symbiogenesis (Miller Appendix B)

### 2.1 The mechanism

Miller identifies a composition mechanism distinct from peer coupling (current Section III) and extreme-transition dynamics (absorbed via `spike-miller-act-bridge.md`):

> "Symbiogenesis (also known as endosymbiotic theory) is the idea that formerly free-living organisms can get tightly integrated into new free-living entities in a symbiotic relationship. This integration can be so complete that the endosymbiont gives up some of its genetic autonomy, transfers most of its genes to the host cell's genome, and becomes an organelle of the host."
> (Miller 2022, p 285)

Key properties:

- **Asymmetric**: host and endosymbiont play distinct roles; it is not peer coupling.
- **Innovation by parts**: whole sub-systems integrated, not gradual parameter change. Miller contrasts "innovation by sparks" (standard evolution) with "innovation by parts" (symbiogenesis).
- **Gradual autonomy loss**: the endosymbiont transfers functions to the host, retaining minimal structural identity (enough to avoid hazardous transfers and maintain responsiveness).
- **Biological examples**: mitochondria (α-proteobacterium), chloroplasts (cyanobacterium), eukaryotic cell formation generally.
- **Social examples** (Miller p 287): firm mergers, technology recombination (patents / prior art), language families, legal precedent (Magna Carta, common law), market institutions (double auction adoption), religious canon overlap.

### 2.2 Why AAD currently cannot model this

AAD's `#form-structural-change-as-parametric-limit` lists six operations from reweighting to full restructure, including "grafting — incorporating external structure." Per `spikes/spike-miller-act-bridge.md` §1.1, the grafting label was flagged as hand-wavy: a category without a formalism.

Symbiogenesis **is** the formal mechanism for grafting. More generally, AAD's composition framework is structured around projecting pre-existing micro-agents into a macro-description. It has no machinery for the *creation* of a composite agent from previously-independent agents. The closure-defect framework asks "how faithful is this macro-description?" — it cannot ask "how did the macro-agent come into being?"

Symbiogenesis answers the second question. The host agent absorbs structure from the endosymbiont agent; the endosymbiont's independent objective is subsumed into the host's; a new composite agent exists where two independent ones stood.

### 2.3 The key insight

**Symbiogenesis is precisely the dynamical process by which $U_O$ transitions from 0 (two independent agents) to 1 (composite with unified purpose).**

- Before: host and endosymbiont have independent objectives, $U_O \approx 0$. They are a multi-agent system, not a composite.
- During: gene transfer, functional specialization, gradual integration. $U_O$ rises.
- After: endosymbiont functions for host survival. $U_O \to 1$ (by definition — the endosymbiont no longer has an independent objective to be misaligned with).

The transition from "two agents" to "one composite" is not a projection choice; it is a physical process of objective integration. Symbiogenesis is the mechanism of that integration.

This reframes the two findings not as additions to AAD but as complementary pieces of one story: **teleological unity is the composition existence condition, and symbiogenesis is the mechanism by which that condition gets crossed from below.**

---

## 3. The Composition Scope Condition (detailed)

### 3.1 Operationalizations of $U_O$

`#def-unity-dimensions` gives $U_O^{(i,j)} = \text{corr}(V_{O_t^{(i)}}, V_{O_t^{(j)}})$ over trajectories. This is a pair-wise correlation in value functions. For $N$-agent composition, aggregate to the full system.

Alternative operationalizations candidate for the scope condition:

- **$O_c$ existence**: a composite objective $O_c$ exists such that $\min_i \text{corr}(V_{O_c}, V_{O_i}) \geq \epsilon$.
- **Mutual-benefit form**: there is a relevance variable $Y$ for which the sub-agents' joint actions collectively raise $\mathbb{E}[Y]$ above the non-cooperation baseline (Miller's IAM form).
- **Common-parent hierarchical form**: $\{O_i\}$ are derivable from $O_c$ via decomposition consistent with `#post-composition-consistency`.

Different operationalizations admit different composites. The scope condition is satisfied if *any* of them applies — the three are progressively weaker routes to the same qualitative requirement.

### 3.2 "Control" and "definitional" as compatible framings

Joseph's original framing: $U_O$ "may need to be controlled and/or assumed as definitional." These are compatible:

- **Definitional** framing: $U_O \geq \epsilon_{\text{comp}}$ is a gate. Below the gate, composition does not apply.
- **Control** framing: $U_O$ is treated as an input parameter; we study composite behavior as $U_O$ varies, including near the transition.

The control framing is a subset of the definitional framing: sweeping $U_O$ means varying above and through the threshold. Below threshold: degenerate case (no composite; multi-agent system). Above threshold: composite quality varies with the other unities.

### 3.3 What the scope condition excludes

Cases where the scope condition fails:

- **Orthogonal multi-agent systems**: agents with independent, non-interacting objectives. Valid object of study (`#scope-multi-agent`), but not a composite.
- **Adversarial pairs**: agents with opposed objectives ($U_O < 0$). `#der-adversarial-destabilization` and `#result-adversarial-tempo-advantage` are correctly about multi-agent dynamics, not composite dynamics. The existing segments implicitly respect this (they don't invoke closure defect on the adversarial pair).
- **Coincidental aggregates**: two agents that happen to be in the same environment with no teleological relationship. A person and a thermostat in a room.

What *does* satisfy the scope condition:

- **Cooperative teams**: explicitly aligned around a shared objective. `#der-team-persistence` applies.
- **Hierarchical organizations**: sub-agents with sub-objectives derived from parent objective. Military doctrine; corporate hierarchy.
- **Symbiotic pairs**: endosymbionts whose survival depends on host. Mitochondria + cell.
- **Mutual-benefit ecologies**: agents with overlapping positive-sum relationships even without explicit shared objective.

---

## 4. Recovery of the Other Unities as Quality Metrics

Given composition exists (the $U_O$ gate passes), the other unities parametrize composite quality:

- **$U_M$** (epistemic): how much of the reality model is shared → compressibility of the macro-state's epistemic substate → $\varepsilon_x$ rate-distortion curve (per `spike-unity-closure-mapping.md` §4.1)
- **$U_\Sigma$** (strategic): deviation of actual joint policy from joint-optimal → partial control of $\varepsilon_a$
- **$U_{\text{obs}}$** (perceptual): shared observation information → $\varepsilon_o$ rate-distortion curve (per `spike-unity-closure-mapping.md` §4.2)
- **Update heterogeneity** (from unity-closure spike §10): structural variation in $f_M$ update rules → additional rate-distortion dial, not captured by any of the four unities as currently defined

These determine the rate-distortion curves for closure-defect components *given* that the composite exists. Before the scope condition passes, talking about rate-distortion of the closure defect is category-error: there is no composite agent whose closure defect to measure.

This cleans up the "two-axis structure" from `spike-unity-closure-mapping.md` §10. The closure defect depends on:

(a) **Existence axis** ($U_O$, new): gate — does the composite exist at all?
(b) **Information axis** ($U_M$, $U_{\text{obs}}$): compressibility of state/observation info
(c) **Coordination axis** ($U_\Sigma$): policy coordination
(d) **Structural axis** (update heterogeneity): homogeneity of update rules

Four axes, not two. The gate axis (a) was implicit in the existing framework; making it explicit is the restructuring.

---

## 5. Implications for Existing Segments

### 5.1 #def-unity-dimensions

Restructure: separate $U_O$ as scope from $\{U_M, U_\Sigma, U_{\text{obs}}\}$ as quality metrics. Existing Discussion text on Clausewitz's gaps remains applicable; the structural reframing does not change the content, only its role.

### 5.2 #form-composition-closure

The admissibility conditions (A1)-(A4) presuppose a valid composite (macro-state has AAD structure, macro-mismatch well-defined, etc.). Under the proposal, (A1)-(A4) are conditional on the composition-scope-condition. The framework is strengthened by making this explicit: "given a composite that exists, here are the conditions under which its macro-dynamics are admissible."

### 5.3 #hyp-directed-separation-under-composition

The Case 1 / Case 2 analysis (goal-blind vs. goal-dependent routing) is well-posed only for composites that pass the scope condition. Case 2 (goal-dependent routing) requires high $U_O$ by definition — otherwise goal-dependent routing is ill-defined (routing based on *whose* goal?). The segment's existing claims are preserved; they gain a cleaner presupposition.

### 5.4 #form-structural-change-as-parametric-limit

The six operations are within-agent. The "grafting" label becomes a pointer to symbiogenic composition, which is a cross-agent structural change — qualitatively different from the other five. Recommend: move grafting out of this segment and into the new `#hyp-symbiogenic-composition`.

### 5.5 #der-team-persistence

Applies to composites (scope condition passes). The cooperative-adversarial decomposition ($\gamma^{\text{coop}} \mathcal T_j$ vs. $\gamma^{\text{adv}} \mathcal T_j$) already implicitly assumes $U_O$: cooperation is $U_O$-positive coupling; adversarial is $U_O$-negative. Under the reframing, cooperative coupling is *within-composite* dynamics, and adversarial coupling is *multi-agent* dynamics. The formal structure is preserved; the scope interpretation is sharpened.

### 5.6 #scope-multi-agent

Currently defines the scope for multi-agent systems. Under the proposal, this segment becomes the *broader* scope; `#scope-composite-agent` is a *restriction* to systems where a composite agent exists. Multi-agent systems without $U_O$ still satisfy `#scope-multi-agent` and are valid objects of study (adversarial dynamics, orthogonal ecosystems); they just don't form composites.

---

## 6. Connection to the IB Unification Conjecture

From `spikes/spike-unity-closure-mapping.md` §6: composition is IB with appropriate relevance variables. Proposed refinement:

**The choice of relevance variable is itself the $U_O$ question.**

For a single agent, relevance is defined by that agent's objective $O$:

- $M$-compression: relevance = future observations given actions (for predictive sufficiency)
- Strategy compression: relevance = future value (for optimality)

For a composite, relevance must be defined by $O_c$. But $O_c$ exists only if $U_O$ passes the scope condition. Without $U_O$, there is no shared relevance variable, no well-defined joint IB problem, no composite IB frontier — and hence no composite at all.

**IB reformulation of the scope condition**: composition existence ≡ well-defined shared relevance variable ≡ $U_O$-gate passes.

Symbiogenesis is the process by which the relevance variable shifts: from "host's individual survival" and "endosymbiont's individual survival" as two separate IB problems, to "combined organism's survival" as a single IB problem. The symbiogenic transition creates the shared relevance variable.

Under this view, the three composition mechanisms are three ways relevance variables can combine or merge:

1. **Peer coupling**: sub-agents retain individual relevance variables, but interactions modify their marginal distributions. Closure defect = IB distortion given the projection.
2. **Extreme transition**: population-level dynamics; relevance variables stay individual but the distribution over agent types shifts, creating new coupling regimes.
3. **Symbiogenesis**: relevance variables *merge* — two IB problems become one. The endosymbiont's relevance is absorbed into the host's.

Symbiogenesis is the mechanism distinctive to the third type. It cannot be represented as a projection or as a population shift; it is a change in what the IB problem is.

---

## 7. Three Composition Mechanisms, Unified Picture

The reframing unifies AAD's Section III around three distinct composition mechanisms, each with a different role:

| Mechanism | What happens | $U_O$ behavior | AAD machinery |
|---|---|---|---|
| **Peer coupling** | Sub-agents interact through shared environment | $U_O$ held fixed (quality given existence) | `#form-composition-closure`, `#der-team-persistence`, `#der-tempo-composition` |
| **Extreme transition** | Population-level restructuring via drift/niche/cascade | $U_O$ can shift across population as agent types replace one another | `spike-miller-act-bridge.md`; pending segments (`composition-transition-dynamics` etc.) |
| **Symbiogenesis** | Hierarchical absorption; one agent integrates another | $U_O$ crosses scope condition from 0 to near-1 | **Missing — proposed `#hyp-symbiogenic-composition`** |

All three exist in real composite agents. Symbiogenesis is how composites *form*; peer coupling is how they *operate*; extreme transition is how they *restructure*.

AAD has machinery for the second. It has machinery in progress for the third. It has nothing for the first — which is, paradoxically, the mechanism that creates the objects the other two describe.

---

## 8. Epistemic Status

| Claim | Status |
|---|---|
| Symbiogenesis is a composition mechanism distinct from peer coupling | Robust qualitative, well-grounded in Miller + evolutionary biology |
| Symbiogenesis corresponds to $U_O$ emergence from 0 to 1 | Hypothesis, structurally motivated; formalization requires more work |
| $U_O$ as composition scope condition | Proposal, requires buy-in; consistent with existing segments when interpreted carefully |
| Recovery of other unities as quality metrics | Natural given the scope framing; compatible with existing `#def-unity-dimensions` text |
| IB reformulation: $U_O$ = existence of shared relevance | Plausible; extends unity-closure spike §6 but not formally derived |
| Three-mechanism taxonomy (peer coupling / extreme transition / symbiogenesis) | Robust qualitative organizational claim |

Max attainable for the overall framing: *robust qualitative*. Specific formalizations (symbiogenesis as a formal dynamical process on agent state spaces, $U_O$ threshold as precise inequality) require additional spike work.

---

## 9. Open Questions

1. **Threshold form of the scope condition**: a sharp threshold seems artificial. More plausible: smooth transition from "not-quite-composite" to "composite" with closure-defect framework degrading gracefully in the low-$U_O$ region. The threshold might be defined by phase transition rather than by cutoff.

2. **Asymmetric unity**: in symbiogenesis, host and endosymbiont have asymmetric roles. The sub-agents' objectives need not be equally represented in $O_c$; one typically dominates. The scope condition should accommodate asymmetric composition (composites where sub-objectives are dominated, not just shared).

3. **Transitivity**: if three sub-agents align pairwise but not all three on a common objective, do they form a composite? Probably yes via (C-ii) — hierarchical derivation of sub-objectives from common parent. But this should be formally checked.

4. **Logogenic-agent interaction**: Class 2 (fully merged) agents fail directed separation at the individual level. Does the composition scope condition apply to composites of logogenic agents? Probably yes with caveats — shared intent in logogenic composites may be implicit (through shared training) rather than explicit (through stated objectives). Worth a sub-spike.

5. **Minimum symbiogenic transition dynamics**: a formal dynamical model of symbiogenesis within AAD. The endosymbiont's objective parameter gradually shifts toward host's; corresponding strategy restructures. Likely requires new machinery (objective-transfer dynamics, function-specialization mechanism). Biological precedent: gene transfer as a continuous parameter shift; AAD analog: objective-parameter transfer.

6. **Reverse symbiogenesis**: does composition ever run backward? (Endosymbiont "escaping" and regaining autonomy.) Biologically rare but not impossible. Theoretically: the scope condition can be crossed in either direction. A composite that loses $U_O$ dissolves back into a multi-agent system.

---

## 10. Proposed Work

### Immediate (promotion to segments)

1. **New segment: `#scope-composite-agent`** — formal statement of the scope condition, paralleling `#scope-agency`. Likely a Scope-type segment.
2. **New segment: `#hyp-symbiogenic-composition`** — the mechanism distinct from peer coupling. Likely a Formulation- or Hypothesis-type segment.
3. **Revision: `#def-unity-dimensions`** — separate $U_O$ as scope from $\{U_M, U_\Sigma, U_{\text{obs}}\}$ as quality metrics.
4. **Revision: `#form-structural-change-as-parametric-limit`** — remove grafting from the within-agent list; point to the new symbiogenesis segment.

### Deferred

5. Formal dynamical model of symbiogenic transition (objective-transfer, function-specialization). Significant follow-on spike.
6. Interaction with logogenic-agent architectural class (Class 2 composites). Sub-spike.
7. Restructuring of Section III into three sub-sections: (a) scope + mechanisms (scope condition, three mechanisms), (b) quality (closure defect, unities, team persistence), (c) dynamics (transitions, adversarial). Editorial.

### What this does not deliver

- It does not replace the closure-defect framework. Peer coupling's machinery is preserved.
- It does not resolve the bridge lemma's contraction obstruction for non-stationary purposeful agents (that's a separate open problem; see `spikes/spike-mori-zwanzig-composition.md`).
- It does not provide a closed-form rate-distortion formula for symbiogenic transitions. That requires the deferred follow-on work.

---

## 11. Why This Is Worth Doing Now

Three reasons:

1. **It closes a real gap.** Symbiogenic composition is the mechanism behind most real hierarchical composites (eukaryotes, organisms, organizations, legal systems, religions). AAD cannot currently model any of these as composition events — only as static projections of already-composed systems.

2. **It resolves latent confusion.** The current `#def-unity-dimensions` framework leaves the "what counts as a composite?" question implicit. The proposal makes it explicit via the scope condition. This should clean up reader confusion (the "predicts vs. rate-distortion" error corrected in `spike-unity-closure-mapping.md` §1 was partly caused by this implicit structure).

3. **It integrates cleanly with the IB unification direction.** If the IB conjecture from `spike-unity-closure-mapping.md` §6 holds, then $U_O$ as scope condition = existence of shared relevance variable. The three composition mechanisms are three ways relevance variables can combine. This suggests a unified IB-based theory of composition — a genuine theoretical contraction rather than an expansion.

---

**Added 2026-04-20. Converges two independent findings (Miller symbiogenesis reading + Joseph's $U_O$-as-definitional observation) into a single structural proposal for Section III reframing. Worth review and prioritization before promotion.**
