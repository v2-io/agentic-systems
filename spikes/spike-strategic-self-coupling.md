---
spike: strategic-self-coupling
date: 2026-05-09
status: scope-defined; investigation pending
related_segments:
  - der-directed-separation
  - disc-adversarial-coupling-pressure
  - def-strategy-dag
  - norm-explicit-strategy-condition
  - der-deliberation-cost
  - post-composition-consistency
related_gaps:
  - fixed-action-set assumption (surfaced in #disc-adversarial-coupling-pressure §"Scope: implicit assumptions")
---

# Spike: Strategic Self-Coupling — Coupling-as-Enabling

**Status.** Scope-defined; investigation pending. This spike establishes the research direction, prior-art landscape, and structural extension required for a sister segment to `#disc-adversarial-coupling-pressure` covering the *enabling* polarity of coupling. The spike does *not* contain investigation results — those land when the spike is taken up. Spike form follows the corpus convention: motivation, gap identification, prior art landscape, structural extension, candidate landings, open questions.

**Motivation.** `#disc-adversarial-coupling-pressure` treats coupling as *vulnerability* — an architectural state that adversaries strategically drive opponents toward because coupling expands attack surface. That segment surfaces (in §"Scope: implicit assumptions and the polarity of coupling") that the framework's fixed action space $\mathcal{A}$ implicitly assumes coupling is cost-only: actions available to the agent do not depend on $\kappa_{\text{processing}}$. In practice some actions exist *only* under coupling. Schelling-style commitment devices are credible only because retreat is foreclosed. The salesperson whose sincere conviction enables persuasion cannot match that performance from a modular position where she knows the product is mediocre — the conviction *is* the action's enabler. The marathoner who runs the race to its conclusion is differently the same agent as the marathoner with backup plans. Religious practice, identity-coupled coordination, public commitment, vow-taking, oath-swearing — all are operations where an agent *deliberately decreases its own modularity* in exchange for access to actions otherwise unavailable.

The framework currently has no machinery for this. Coupling appears only as the failure mode of directed separation (Class 2 architectures, motivated reasoning) or as adversarially-driven pressure (`#disc-adversarial-coupling-pressure`). The *self-driven, action-enabling* polarity is the third operation in the three-operation modularity-state-dynamics picture (the table in `#disc-adversarial-coupling-pressure` §"Scope") and is missing from the framework.

**Spike scope.** This spike does three things:
1. Specifies the structural extension required (coupling-dependent action space $\mathcal{A}(\kappa_{\text{processing}})$, with strategy-DAG edges that include "couple to enable $a^\ast$" as a strategic move).
2. Surveys prior art for direct adoption per AAT's prior-art-integration discipline (no orphaned positioning documents; concepts adopted as first-class theory components with original names and citations).
3. Names candidate segment products and the dependency-DAG additions they require.

---

## 1. The Gap

### 1.1 Where the framework treats coupling

Three current loci:

- **`#der-directed-separation`** — coupling as architectural property. Class 1 modular / Class 2 fully merged / Class 3 partially modular. The classification is presented as static-architectural; it does not model deliberate *transitions* between classes as strategic moves.
- **`#disc-adversarial-coupling-pressure`** — coupling as adversarially-driven vulnerability. External pressure drives the target's $\kappa_{\text{processing}}$ upward; the target loses defensive perimeter.
- **§"Defensive scaffolding as composition"** (in `#disc-adversarial-coupling-pressure`) — coupling-restoration via composite-agent construction (truthification operation).

None of these loci treats coupling as a *strategic resource the agent itself acquires for offensive reach*.

### 1.2 What an enabling-polarity treatment requires

Three structural moves:

**(M1) Coupling-dependent action space.** The framework's policy $\pi(M_t, G_t) \to a_t$ selects from a fixed $\mathcal{A}$. A more honest specification: $\pi: (M_t, G_t, \kappa_t) \to a_t$ where $\kappa_t$ is the agent's coupling state and $\mathcal{A}(\kappa_t) \supsetneq \mathcal{A}(0)$ for some range — additional actions become available as the agent's coupling state increases.

**(M2) Coupling as strategic move.** $\Sigma_t$ — the strategy DAG (`#def-strategy-dag`) — currently has edges representing causal-pathway choices to objective. An enabling-polarity treatment needs strategy edges that represent "couple yourself to enable downstream action $a^\ast$" — a meta-strategic move that modifies the action space available to subsequent strategy execution. Schelling's commitment devices are exactly this: a strategy node whose effect is *not* directly toward the objective but is *enabling of* a credibility-dependent strategy further down the DAG.

**(M3) Reversibility cost.** Self-coupling is typically asymmetrically reversible: easier to couple than to uncouple (sunk costs, identity formation, public commitments). A formalization needs an *uncoupling-cost* function — typically much larger than the coupling-cost, since the coupling's strategic value depends on its credibility, which depends on uncoupling being costly. (This is Schelling's own observation about commitment devices: their value is exactly the credible costliness of reversal.)

These three moves are interdependent. (M1) without (M2) gives coupling-dependent actions but no way for the strategy to acquire them. (M1)+(M2) without (M3) makes self-coupling free and trivializes the strategic question. All three are needed for the formalization to track what the prior-art literature calls "commitment device."

---

## 2. Prior Art Landscape

The phenomenon is rich in prior literature. AAT's contribution would be *integration* (per the prior-art-integration discipline): adopt the concepts directly with citations and original names, and surface what AAT adds.

### 2.1 Direct adoption candidates

**Schelling 1960 — *The Strategy of Conflict*; 1966 — *Arms and Influence*.** The foundational work on commitment devices. Schelling's treatment names: (a) the credibility paradox (a threat is credible only if costly to retract), (b) burning bridges as a strategic move (deliberately removing one's own options), (c) the role of irrationality as commitment (an opponent who is genuinely unhinged has more credibility than a calculating one), (d) precommitment-via-mechanism (delegating to a sub-agent or device that cannot be revoked). Direct adoption: Schelling's commitment-device framework as the canonical example of (M2)+(M3); cite under original name "commitment device."

**Ainslie 1992 — *Picoeconomics*; 2001 — *Breakdown of Will*.** Intertemporal bargaining, hyperbolic discounting, willpower as the agent's strategic move against future selves. Ainslie treats the agent as a population of temporally-displaced sub-agents who bargain; *resolutions* are precommitment moves (fixing one's later behavior by present arrangements). Closer to (M3) than Schelling's external-facing version: the coupling is internal-temporal (current self couples future self by commitment now). Direct adoption: intertemporal-bargaining vocabulary; willpower as a structural rather than virtuous concept.

**Akerlof & Kranton 2000 — "Economics and Identity"; 2010 — *Identity Economics*.** Identity as utility argument: agents derive utility from acting in accordance with internalized identity. Once identity is coupled to behavior, certain actions become available (in-group cooperation, costly signaling) and others become unavailable (defection, deviation from norm). Direct adoption: identity-coupling as a specific instantiation of (M1); Akerlof-Kranton's identity-utility-term as the formal hook.

**Frank 1988 — *Passions Within Reason*.** Emotions as commitment devices — the rational agent benefits from emotional dispositions because they pre-commit responses (anger pre-commits retaliation, love pre-commits loyalty) in ways that calculating self-interest cannot. Direct adoption: emotion-as-commitment-device framing; useful complement to Schelling for the *internal*-affective coupling case.

**Elster 1979 — *Ulysses and the Sirens*; 2000 — *Ulysses Unbound*.** Survey treatment of self-binding strategies across psychology, politics, and law. Catalogs forms of precommitment. Useful for *taxonomy* of self-coupling moves rather than for formal extension.

**Skyrms 1996 — *Evolution of the Social Contract*; 2004 — *The Stag Hunt and the Evolution of Social Structure*.** Evolutionary game-theoretic treatment of cooperation-supporting commitment, including the role of correlated devices. Useful for the population-dynamics layer when self-coupling becomes a population-level phenomenon (norms, institutions).

### 2.2 Adjacent literatures requiring positioning rather than direct adoption

- **Game-theoretic commitment value** (Stackelberg leadership, mechanism design with commitment) — formal results on the value of being able to commit. Useful for the (M3) reversibility-cost formalization.
- **Behavioral economics on hot-cold empathy gaps and self-control** (Loewenstein, Thaler-Sunstein on choice architecture) — empirical instantiations of the temporal-bargaining structure Ainslie formalizes.
- **Ritual studies / religious commitment literature** (Atran, Sosis on costly-signaling-as-commitment) — ethnographic and evolutionary evidence that commitment-via-coupling is a recurrent human cultural pattern, not a marginal phenomenon.
- **Cult-formation literature** (Lifton, Singer) — the pathological / coercive end of self-coupling, where the line between strategic-self-coupling and adversarial-coupling-pressure blurs. Useful for understanding the boundary between the second and third modularity-state operations.

### 2.3 Anticipated novelty positioning

The phenomena are well-documented; the contribution is structural placement in AAT's machinery. Specifically: (i) recognizing self-coupling as a third operation on modularity state distinct from both adversarial pressure and architectural class; (ii) the formalization $\mathcal{A}(\kappa_{\text{processing}})$ as a coupling-dependent action space; (iii) the relationship between self-coupling and adversarial-coupling-pressure as opposite-valence operations on the same architectural state. Novelty is *recognition* + *integration* per the FORMAT.md schema, not invention.

A targeted prior-art search before promotion should query: (a) whether any prior synthesis names commitment-device / identity-coupling / willpower as instances of the *same structural operation* under formal nomenclature; (b) whether the action-space-as-coupling-state-dependent formalization $\mathcal{A}(\kappa)$ has been written down (active-inference and bounded-rationality literatures are the most likely homes); (c) whether the three-operation modularity-state framing has appeared as a meta-pattern.

---

## 3. Structural Extension Required

### 3.1 Action space generalization

Replace $\pi: (M_t, G_t) \to a_t$ with:

$$\pi: (M_t, G_t, \kappa_t) \to a_t, \quad a_t \in \mathcal{A}(\kappa_t)$$

where $\kappa_t$ is the agent's coupling state (operationalized via `#der-directed-separation`'s $\kappa_{\text{processing}}$) and $\mathcal{A}(\kappa_t)$ is non-decreasing in $\kappa_t$ over a relevant range — additional actions become available as the agent's processing becomes more coupled.

**Open: domain of $\kappa_t$ for which $\mathcal{A}$ is non-decreasing.** It is not the case that more coupling always enables more actions. Past some threshold, coupling-induced bias destroys the agent's ability to act usefully at all (a fully captured / cult-bound agent loses access to actions that require any external-reality contact). The function $\mathcal{A}(\kappa_t)$ is plausibly non-monotone — initial coupling enables credibility-dependent actions; sustained over-coupling forecloses reality-dependent actions. The shape of $\mathcal{A}(\kappa_t)$ is the empirical question this segment would frame.

### 3.2 Strategy DAG: enabling moves

`#def-strategy-dag`'s edges represent causal-pathway claims about how an action affects an objective-relevant outcome. An *enabling* edge would represent: action $a$ has the effect of *increasing $\kappa_t$ in a way that subsequently makes $a^\ast$ available*. This is a meta-strategic move — it does not directly advance toward the objective; it modifies the agent's own action space so that a later strategy node becomes feasible.

Formally this requires extending the strategy DAG's node semantics: nodes whose outcome variable is the agent's own coupling state, not an environmental quantity. This is structurally similar to the agent's $M_t$-self-modeling that `#scope-agent-identity` already permits, but at the strategy layer rather than the model layer.

### 3.3 Reversibility cost

The strategic value of self-coupling depends on its irreversibility. A formalization needs:

$$c_{\text{couple}}(\kappa_0 \to \kappa_1) \ll c_{\text{uncouple}}(\kappa_1 \to \kappa_0)$$

with the asymmetry's magnitude as the parameter that determines coupling's credibility. The Schelling observation: a commitment is credible exactly to the extent that uncoupling is costly. This may import directly from the cost-of-deliberation segment (`#der-deliberation-cost`) or may require its own appendix.

---

## 4. Connection to Existing Machinery

- **`#der-directed-separation`** — supplies $\kappa_{\text{processing}}$ as the coupling-state variable. The (M1) extension uses this directly.
- **`#def-strategy-dag`** — supplies the DAG that the (M2) enabling-edge extension modifies. Strategy DAG already has confidence-weighted edges (`#deriv-edge-credence-dynamics`); enabling edges are a new edge-type, not a new graph.
- **`#disc-adversarial-coupling-pressure`** — the *opposite-valence* operation. Naming the symmetry between the two segments (self-driven vs externally-driven; enabling vs vulnerability) is the load-bearing recognition.
- **`#post-composition-consistency`** — self-coupling at the individual level may be analyzed as a composition move (couple sub-self to other sub-self, where Ainslie's intertemporal-bargaining picture applies). The connection is real but oblique; do not over-promise it before the formalization is in hand.
- **`#der-deliberation-cost`** — supplies the think-vs-act cost framework that the (M3) reversibility-cost extension may build on.

---

## 5. Candidate Segment Products

In rough order of likelihood:

**(P1) `disc-strategic-self-coupling` — the primary segment.** Discussion-grade meta-segment naming the enabling polarity of coupling-as-property, articulating the three structural moves (M1)–(M3), instantiating the prior-art-adopted concepts (Schelling commitment devices; Ainslie willpower / intertemporal bargaining; Akerlof-Kranton identity coupling; Frank emotions-as-commitment) as worked examples, and naming the dual relationship to `#disc-adversarial-coupling-pressure`. *Probable form*: structurally parallel to `#disc-adversarial-coupling-pressure` (mechanism table at the top; sections on enabling, strategic value, reversibility cost, asymmetric advantage; defensive-scaffolding analog as the truthification operation).

**(P2) `def-coupling-dependent-action-space` (or similar) — formalization appendix.** The (M1) formalization in segment form: $\mathcal{A}(\kappa_t)$ definition, monotonicity over relevant range, relationship to the architecture classification, examples drawn from the prior-art literature.

**(P3) `disc-modularity-state-dynamics` — the meta-segment.** Once both polarity-instantiations exist (this spike's product + the existing adversarial-pressure segment) and truthification has its own segment, the three-operation pattern lands as a meta-architectural piece alongside `#disc-separability-pattern` and `#disc-identifiability-floor`. This is downstream of (P1) and not in this spike's primary scope.

**(P4) Possibly an appendix segment formalizing the reversibility-cost asymmetry** — only if the formalization grounds substantive results (e.g., a derived condition for when self-coupling is rational under given action-space and cost asymmetry parameters). May not be needed if the discussion-grade treatment in (P1) carries the load.

---

## 6. Open Questions

1. **Shape of $\mathcal{A}(\kappa_t)$.** Plausibly non-monotone — initial coupling enables, sustained over-coupling forecloses. What governs the inflection? Empirical question with structural implications.
2. **Self-coupling vs adversarial-coupling-pressure boundary.** The cult-formation literature suggests these blur in practice — what starts as adversarial pressure can be internalized as identity-coupling, after which the agent perceives it as self-driven. A formalization needs to handle the boundary or scope it out.
3. **Self-coupling under repeated interaction.** If two agents both have access to self-coupling moves, does the equilibrium structure of strategic interaction change? Likely yes — Schelling's whole framework is about strategic interaction with commitment moves available.
4. **Composition consistency.** Does self-coupling within a sub-agent break or preserve composite-level directed separation? Plausibly breaks — a sub-agent that has coupled itself to enable a strategic move now has $O_t \to M_t$ pathways internal to it, which makes the composite's directed separation depend on aggregation specifics.
5. **Relationship to `#scope-agent-identity`.** Self-coupling that crosses thresholds may modify what `#scope-agent-identity` recognizes as "the same agent" — Ainslie's intertemporal bargaining and Akerlof-Kranton's identity transitions both push at this. Out of scope for the initial segment but worth noting.

---

## 7. Investigation Roadmap (when this spike is taken up)

1. **Targeted prior-art search.** Confirm the novelty positioning: search for prior synthesis under the names "commitment device + identity economics + willpower + emotions-as-commitment" as instances of one structural operation; search for $\mathcal{A}(\kappa)$ formalizations in active-inference and bounded-rationality literatures.
2. **Read the Schelling primary text** and confirm the (M1)–(M3) extensions track Schelling's intuitions rather than diverging unintentionally.
3. **Draft (P1).** Discussion-grade segment parallel to `#disc-adversarial-coupling-pressure`. Mechanism table. Polarity-symmetry recognition. Prior-art integration with Schelling/Ainslie/Akerlof-Kranton/Frank as adopted concepts.
4. **Determine whether (P2) is needed independently** or whether the formalization fits inside (P1)'s body.
5. **Defer (P3) and (P4) until (P1) lands.** The three-operation meta-segment is most legible when each operation has a primary segment; the reversibility-cost formalization is most useful if it grounds a derived result, which requires (P1) to know what would be derived.

---

## Cross-references

- Spawns from `#disc-adversarial-coupling-pressure` §"Scope: implicit assumptions and the polarity of coupling" (the fixed-$\mathcal{A}$ assumption surfacing).
- Sister to `#disc-adversarial-coupling-pressure` (opposite-polarity operation on the same architectural state).
- Will register in `spikes/INDEX.md` under a 2026-05-09 coupling-polarity entry.
