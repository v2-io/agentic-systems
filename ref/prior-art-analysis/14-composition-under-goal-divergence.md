# Prior-Art Analysis: Composition Under Goal Divergence (Strategic Composition)

> [!note]
> **Refreshed 2026-05-21.** The analysis was already aligned with the load-bearing segment `#deriv-strategic-composition`. This refresh adds (a) the **prompt-segment tension on Class 2 vs Class 3** — the prompt overclaims as Class-3 Coupled; the actual segment result is Class 2 (Partial); this is a Joseph-reserved question per the strengthen-before-soften discipline — (b) the (SC-1)/(SC-2)/(SC-3) three-question decomposition, (c) the sub-scope $\alpha'/\beta'$ partition with the honest set-convergence-only scope limit for $\beta'$, (d) the (C-iv) strategic-equilibrium route to scope-satisfaction (cross-row 08), (e) the mechanism-design-impossibility status (Gibbard-Satterthwaite arm tested and routed to `#disc-separability-pattern`; Myerson-Satterthwaite + Arrow remain Joseph-reserved), and (f) the relationship to the wrapping segments for composition of W₁-wrapped components under goal divergence (cross-row 05).

**Target Claim:**
When two or more AAT agents interact through a shared environment with **partially-opposing objectives** $\{O_t^{(i)}\}$, the composition-level question is *not* "does the trajectory contract to zero closure-defect?" but "does the coupled best-response dynamics admit an equilibrium and converge to it?" Contraction to shared truth is a $U_O = 1$ special case; strategic composition is the $U_O < 1$ companion regime in which the correct primitive is **fixed-point existence and stability**, not Lyapunov contraction on a shared state. AAT names three composition-level questions distinctively:
- **(SC-1) Existence of equilibrium** — fixed-point question;
- **(SC-2) Stability of equilibrium** — local-stability question;
- **(SC-3) Convergence from interior** — reachability question.

None is a Lyapunov contraction question on a shared state variable.

**Two sub-scopes carry progressively weaker conditions.**
- **Sub-scope $\alpha'$ (potential / monotone games).** Under Monderer-Shapley (1996) potential-game or Rosen (1965) monotone-game conditions, the **sector-persistence template transfers to the gradient of the joint potential** (resp. to a weighted-norm variational inequality on the joint Jacobian's symmetric part). AAT's persistence machinery recovers at the equilibrium layer with state variable $\xi = \pi - \pi^\ast$ (deviation from Nash) and sector constant $\alpha_{\text{joint}}$ living at the *joint potential's curvature* rather than at any individual sub-agent's $\alpha$.
- **Sub-scope $\beta'$ (non-potential non-monotone games).** Only **set-convergence to coarse correlated equilibria** is available (Hart & Mas-Colell 2000 under no-regret dynamics, rate $O(1/\sqrt T)$). The macro-state of a strategic composite is a *distribution* on joint strategy space rather than a state-space point. Sub-scope $\beta'$ gives AAT substantially weaker predictive power than $\alpha'$ — an honest scope limit shared with game theory itself, not a defect of AAT.

**Architectural consequence — Class 2 (Partial) composite-from-Class-1 (Separated) sub-agents.** Composites of Class 1 sub-agents with partially-opposing objectives produce **Class 2 (Partial) composites** (per the post-2026-05-09 GUC vocabulary): within-agent processing stays Separated, but composite $(M_c, G_c)$ acquires intrinsic across-agent coupling through each sub-agent's model of the others' policies. This is *bounded* coupling — within-agent separation is preserved — placing the composite in Partial (Class 2), *not* fully Coupled (Class 3).

> [!warning]
> **Prompt-segment tension (open question for Joseph).** The prompt file `14-strategic-composition-and-mechanism-design.md` states "the composite is necessarily *Class-3 Coupled*" and asserts *"modular safety architectures fail by construction under goal divergence between safety modules and the central planner — the composite acquires Class-3 dynamics regardless of each component's nominal modularity."* The load-bearing segment `#deriv-strategic-composition` defends the **Class 2 (Partial)** result with explicit justification: across-agent coupling is bounded because within-agent $f_M^{(i)}$ remains goal-blind. Two readings:
> - **(A) The segment is correct; the prompt overclaims.** The Class 2 (Partial) framing is the truthified result. "Modular safety architectures fail by construction" overstates the failure: they degrade to Partial (bounded coupling), not to Coupled.
> - **(B) The prompt's stronger claim is recoverable.** Per the strengthen-before-soften discipline, one should attempt to derive the Class 3 (Coupled) result under tightened assumptions before accepting the softer Class 2 (Partial) reading. Open question: under what additional structural conditions (deeply intertwined cross-agent observation? mutual policy inference at fast timescales? wrapped-component composition where each component is W₁-wrapped but their composition reintroduces query-content goal-leakage?) would the result actually be Class 3?
>
> Pending resolution: the analysis defends what the segment says (Class 2 Partial), notes the inconsistency, and flags this as Joseph-reserved.

---

## 1. State of the Field & Scientific Precedence

The Undermind search reveals that analyzing the convergence of independent, selfish agents to a joint equilibrium is the central pursuit of continuous game theory, networked control, and multi-agent learning. The mathematical boundaries are highly formalized.

### Pillar 1: Potential Games and Monotone Games
AAT explicitly anchors its convergence sub-scopes on two foundational game theory results:
- **Monderer and Shapley (1996)** formalized *Potential Games*, where the incentives of all players perfectly align with a single global scalar potential function. If a game has a potential function, gradient-based play naturally converges to a Nash equilibrium.
- **Rosen (1965)** defined *Diagonally Strictly Concave* (monotone) games, proving that a unique Nash equilibrium exists and gradient play converges to it if the symmetric part of the joint Jacobian is negative-definite.
AAT explicitly imports these as its "Sub-scope $\alpha'$" conditions.

### Pillar 2: Uncoupled Dynamics and Impossibility
AAT's claim that goal-divergent composition inherently breaks down (without specific structural guarantees like potential functions) is deeply precedented by impossibility theorems in game dynamics.
- **Hart and Mas-Colell (2003)** in *Uncoupled Dynamics Do Not Lead to Nash Equilibrium* proved a sweeping negative result: if agents do not know the utility functions of other agents (uncoupled dynamics), there is no general learning algorithm guaranteed to converge to Nash equilibrium. 
- **Milionis et al. (2023)** expanded on this, showing that Nash existence proofs are non-constructive and that natural game dynamics fundamentally fail to converge in general games, leading to chaotic or cycling behavior (e.g., **Mertikopoulos et al., 2017** on *Cycles in adversarial regularized learning*).

### Pillar 3: Passivity and Dissipativity in Nash Seeking
The control theory community has actively worked to solve these non-convergence issues by applying physical stability concepts to game theory.
- **Fox and Shamma (2012)** and **Arcak and Martins (2020)** mapped population games onto passive input-output systems. They used dissipativity theory to prove that if the learning dynamics are passive and the game itself is "stable" (a generalization of monotone), the system converges to a Nash equilibrium.
- **Gadjov and Pavel (2019, 2023)** and **Belgioioso and Grammatico (2018)** applied monotone operator theory to distributed Nash equilibrium seeking, showing that proximal-point algorithms and Laplacian feedback can guarantee convergence even in partially observable or hypomonotone regimes.

---

## 2. Key Anchor Papers (Available in `/ref`)

1. **Monderer, D., & Shapley, L. (1996). Potential Games.**
   *Significance:* The foundational paper proving that when player incentives align with a global potential, best-response dynamics converge; explicitly used by AAT to define its $\alpha'$ sub-scope.
2. **Hart, S., & Mas-Colell, A. (2003). Uncoupled Dynamics Do Not Lead to Nash Equilibrium.**
   *Significance:* Proves the fundamental impossibility of guaranteed convergence when agents act independently without knowing others' payoffs, validating AAT's focus on the breakdown of Class 1 composition under divergence.
3. **Fox, M. J., & Shamma, J. (2012). Population games, stable games, and passivity.**
   *Significance:* Pioneers the use of control-theoretic passivity to analyze game theoretic convergence, strongly mirroring AAT's transfer of the sector-persistence condition to the equilibrium layer.
4. **Arcak, M., & Martins, N. C. (2020). Dissipativity Tools for Convergence to Nash Equilibria in Population Games.**
   *Significance:* Uses dissipativity and contractivity to guarantee global asymptotic stability of Nash equilibria, directly paralleling AAT's use of Lyapunov persistence in strategic composition.

---

## 3. Conclusion on Novelty & Overlap

The mathematical primitives of AAT's strategic composition—Potential Games, Monotone Games, and the use of control-theoretic tools (passivity/dissipativity) to prove convergence to Nash equilibria—are canonical, active areas of research. AAT explicitly acknowledges Monderer-Shapley and Rosen as the source of its theorems.

**Where AAT actually contributes:**

1. **The framing move — contraction → equilibrium convergence (architectural-methodological invention).** Standard composition analyses ask "does the trajectory contract to a shared state?" — a Lyapunov question. Strategic composition (with $U_O < 1$) is *not* a Lyapunov-contraction question on a shared state variable; it is a fixed-point / stability / reachability question on best-response dynamics. AAT's contribution is recognizing that the right primitive shifts under goal divergence, with the (SC-1)/(SC-2)/(SC-3) three-question decomposition explicit. The contraction framing in `#form-composition-closure` / `#deriv-critical-mass-composition` is recovered as the $U_O = 1$ special case.

2. **The (C-iv) strategic-equilibrium route to scope-satisfaction (architectural novelty; cross-row 08).** `#scope-composite-agent` admits four disjunctive routes for a multi-agent system to be a valid composite: (C-i) shared-objective alignment, (C-ii) hierarchical derivation, (C-iii) mutual benefit, plus (C-iv) **strategic-equilibrium route**. The (C-iv) route does *not* require shared objectives, hierarchical derivation, or mutual benefit — only structural convergence of the strategic interaction in the game-theoretic sense (Nash, correlated, or coarse correlated equilibria). Composites satisfying (C-iv) are **strategic composites**, distinguished from alignment composites (C-i, C-ii) and mutual-benefit composites (C-iii). This is an AAT-native methodological invention extending the scope condition.

3. **Sector-persistence template transfer to equilibrium layer (theorem-grade math).** Under sub-scope $\alpha'$ (potential / monotone games), the sector-persistence template transfers with state variable $\xi = \pi - \pi^\ast$ (deviation from Nash), sector constant $\alpha_{\text{joint}}$ inheriting from the joint potential's curvature (Monderer-Shapley) or the symmetric part of the joint Jacobian (Rosen) — *not* from any individual sub-agent's $\alpha$. The Cournot duopoly worked example in `#deriv-strategic-composition` exhibits this with $\alpha_{\text{joint}} = b$ (the demand-side curvature), an economic interpretation rather than ad-hoc parametrization. Nash-style derivation: new result using established Monderer-Shapley / Rosen / sector-persistence-template machinery in an AAT-internal composition setting.

4. **The Class 1 → Class 2 (Partial) result (architectural novelty + theorem-grade math).** Strategic composition is the canonical Class-1-sub-agents → Class-2-composite case, structurally distinct from within-agent failures in `#der-directed-separation`. The composite-level directed separation fails because composite $(M_c, G_c)$ acquires intrinsic coupling through sub-agents' observations of each other — but the coupling is *bounded* (within-agent $f_M^{(i)}$ remains goal-blind), placing the composite in Partial (Class 2) rather than fully Coupled (Class 3). **The prompt-segment tension on whether the result should be Class 3 Coupled is Joseph-reserved (see warning box).**

5. **Sub-scope $\beta'$ honest scope limit (CS-norm scope-precision-is-valuable invention).** AAT does *not* claim to predict equilibrium selection under multiple Nash, short-run dynamics in cyclic games (rock-paper-scissors), or convergence rates better than $O(1/\sqrt T)$ in $\beta'$. The macro-state of a strategic composite in $\beta'$ is a *distribution* on joint strategy space, not a state-space point. This is a genuine scope limit, shared with game theory as a whole — not a defect of AAT. The named partition makes the limit precise.

6. **Mechanism-design impossibility as scope marker (Joseph-reserved boundary work).** Gibbard-Satterthwaite 1973–75 (no dominant-strategy non-dictatorial Pareto-efficient voting mechanism for ≥3 alternatives); Myerson-Satterthwaite 1983 (no efficient, individually-rational, incentive-compatible bilateral-trade mechanism without subsidies); Arrow 1951 (no social welfare function satisfying unrestricted-domain + Pareto-efficient + IIA + non-dictatorial). These are candidate identifiability-floor instances. The Gibbard-Satterthwaite arm was tested in `spike-4th-identifiability-floor-instance-2026-05-20` §4 §"Strengthen-first check" with three reframings discarded; **routed to `#disc-separability-pattern` strategic-composition ladder general-open tier rather than M1 floor**, on the grounds that the actor-under-the-no-go (a *designer* implementing under IC constraint) and the kind-of-remedy (Bayes-Nash IC, preference-domain restriction, randomization, subsidies — not currently AAT machinery) differ from M1 Instances 1–3. Myerson-Satterthwaite and Arrow remain in the cluster as candidates for a sibling meta-segment ("Implementation Impossibility") if mechanism design becomes a first-class framework concern.

7. **The effects-spiral as joint-Jacobian eigenvalue condition (theorem-grade content; cross-row 10).** The symmetric coupled formulation in `#deriv-strategic-composition` upgrades the asymmetric `#der-adversarial-destabilization` effects spiral from `discussion-grade` to derivation-grade: the spiral exists iff $\max_{\pi^\ast} \mathrm{Re}(\lambda_{\max}(\nabla F(\pi^\ast))) > 0$, where $F$ is the joint best-response field. This condition specializes monotone-game failure (Jacobian's symmetric part fails to be negative-definite at equilibrium).

8. **Composition of W₁-wrapped components under goal divergence (cross-row 05).** When the "modular safety architectures" of the prompt are W₁-wrapped LLM agents (each individually Class 1 by structural commitment of goal-blind belief-update queries, per `#der-class-coercion-via-wrapping`), the strategic-composition machinery applies and the composite is bounded Class 2 (Partial) — *not* Class 3 (Coupled) unless the wrapping itself fails behaviorally. The leakage rate $\kappa_{W_1}$ at the component level (bounded by pretraining-distribution mutual information) plus the across-agent coupling at the composite level combine, but each is bounded. This is the strict reading; whether the prompt's stronger Class 3 reading can be derived under additional assumptions is the Joseph-reserved question.

**AAT-native methodological inventions on this row:**
- The (SC-1)/(SC-2)/(SC-3) three-question decomposition for strategic composition.
- The sub-scope $\alpha'/\beta'$ partition with named conditions and honest scope limits.
- The (C-iv) strategic-equilibrium route in `#scope-composite-agent`.
- The placement of strategic composition as Class 1 → Class 2 (Partial) (with the Joseph-reserved Class 3 question).
- The effects-spiral-as-joint-Jacobian-eigenvalue-condition derivation (upgrading row 10's `discussion-grade` to derivation-grade).
- The mechanism-design-impossibility routing to `#disc-separability-pattern` general-open tier.

**Where AAT does *not* claim novelty:**
- Potential games (Monderer-Shapley 1996).
- Monotone / strictly-diagonally-concave games (Rosen 1965).
- Uncoupled-dynamics impossibility (Hart-Mas-Colell 2003).
- Cycle phenomena in adversarial regularized learning (Mertikopoulos et al. 2017).
- Population games + passivity (Fox-Shamma 2012, Arcak-Martins 2020).
- Distributed Nash-equilibrium seeking (Gadjov-Pavel 2019/2023, Belgioioso-Grammatico 2018).
- Coarse correlated equilibria (Hart-Mas-Colell 2000).
- Variational-inequality formulation of game-theoretic equilibria (Facchinei-Pang 2003).
- The mechanism-design impossibility theorems themselves (Arrow 1951, Gibbard-Satterthwaite 1973–75, Myerson-Satterthwaite 1983).

**Epistemic status of the load-bearing segment.** `#deriv-strategic-composition` is `status: conditional`. The A2'-analog under potential-game condition is *exact* (Monderer-Shapley transcribed). Under monotone-game / strict-diagonal-concavity is *derived* (Rosen transcribed). Equilibrium-existence-via-VI is *derived* (Facchinei-Pang). Regret-minimization CCE convergence is *derived* (Hart-Mas-Colell). The Class 1 → Class 2 (Partial) result is *derived (scope-structural)*. The effects-spiral eigenvalue condition is *sketch* at the discussion level (specific AAT instantiations open). The Cournot worked example is *exact* (within the stated setup).

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **Some.** Sector-persistence template transfer to equilibrium layer (Nash-style); $\alpha_{\text{joint}}$ inheritance at joint potential curvature; effects-spiral eigenvalue condition. Multiple substantive theorem-grade derivations transcribed from established game-theory machinery into AAT-internal composition settings.
- *Arch Novelty:* **High.** Framing move (contraction → equilibrium); (SC-1)/(SC-2)/(SC-3) decomposition; $\alpha'/\beta'$ partition; (C-iv) scope route; Class 1 → Class 2 architectural result.
- *Synth Novelty:* **Medium.** Bridges potential / monotone games, control-theoretic passivity, distributed Nash-seeking, and uncoupled-dynamics impossibility under the sector-persistence template at the equilibrium layer.
- *Appl Novelty:* **None at the row level.** Mechanism design implications are flagged for a sibling meta-segment, not landed here.
- *Impact:* **Medium-to-High.** Modular safety architectures composing under goal divergence is a live concern in AI safety. The Class 1 → Class 2 (Partial) result is the structurally honest reading; the stronger Class 3 (Coupled) reading the prompt asserts is Joseph-reserved. The framework's honest scope limit on $\beta'$ (set-convergence-only) is itself a useful contribution to a literature that sometimes overclaims convergence guarantees.