---
spike: strategic-composition-class-3-attempt
file: 02-REFRAME-INSIGHT
parent: 00-FRAMING.md
prior: 01-STRENGTHEN-ATTEMPTS.md
---

# §7. The reframe: what strategic composition actually shifts (the missing axis)

The §§2–6 attempts converged on a discovery the original question did not point at: the architectural Class 1/2/3 axis is *type-mismatched* for the strategic-composite case. When two attempts in opposite directions (strengthen-to-Class-3 and verify-the-Class-2-claim) both reveal the same kind of misalignment between the formal criterion and the intuition the segments are trying to capture, the right move per Joseph's brief is to ask whether the *question* is well-posed.

This file works through the type-mismatch and proposes the constructive axis the framework is missing.

## §7.1 The type-mismatch in detail

For an individual agent, $G_t = (O_t, \Sigma_t)$ is a *state*: a particular choice of objective and a particular strategy DAG. It can be perturbed, conditioned on, updated. The mutual-information measure $I(G_t;\, M_{\tau^+} \mid M_{\tau^-},\, e_\tau)$ is well-defined because $G_t$ has the type of a random variable that the agent's processing can or cannot legitimately access.

For an *aligned* composite (routes C-i, C-ii, C-iii of `#scope-composite-agent`), the composite goal $G_t^c = (O_t^c, \Sigma_t^c)$ is structurally the same type — there is a shared composite objective (or a derivable parent of decomposed objectives, or a mutual-benefit relevance variable). The composite $G_t^c$ has the same type as the individual $G_t$. The criterion lifts cleanly.

For a *strategic* composite (route C-iv of `#scope-composite-agent`), `#scope-composite-agent` itself says:

> The composite's macro-state is defined relative to the equilibrium structure $\mathcal E$ rather than relative to a shared target state.

This is *not* a state in the same type-theoretic sense. $\mathcal E$ is a **fixed-point object** — a set (Nash equilibrium support), a distribution (CCE support), or a topological invariant of the joint best-response dynamics. It is not a perturbable state-variable in the way $G_t$ is.

**Trying to plug $\mathcal E$ into the architectural-class criterion runs into a category problem.** Conditioning on $M_{\tau^-}^c$ when $G_t^c = \mathcal E$ asks for the residual mutual information between an equilibrium-structure object and a belief-state update, given a prior belief state. Near equilibrium, $M_{\tau^-}^c$ structurally pins down $\mathcal E$ (rational expectations); the residual entropy in $\mathcal E$ given $M_{\tau^-}^c$ is zero or near-zero. The numerator and denominator of $\kappa^c$ both vanish — the $0/0$ form from §3.

The architectural-class criterion was designed for a state-variable $G_t$ that the agent's processing might or might not legitimately access. For a fixed-point macro-state $\mathcal E$, "processing accessing $\mathcal E$" is not a meaningful question — $\mathcal E$ is the structure the dynamics *converge to*, not a variable the processing operates on. The criterion is asking the wrong question.

## §7.2 The two distinct axes the framework currently conflates

The §§2–6 push surfaces *two* axes that strategic composition does cleanly differ from aligned composition on. They are structurally independent of the architectural-class axis and of each other. The current framework runs them through the Class 1/2/3 partition awkwardly, because no other axis is available.

### Axis A — Architectural class (existing, clean)

What the architectural class describes:

- The *processing topology* of the composite — which causal pathways exist from $G$ to $f_M$ in the composite's joint processing graph (sub-agents + routing).
- Binary at the boundaries (pathway exists / pathway does not exist), continuous in the Class 2 middle (some pathways exist, some do not).
- Lifts cleanly to composites *if* the routing structure $R_t$ and the composite $G_t^c$ both have well-defined types.

**Determinants for a composite:** sub-agent class, routing-structure goal-dependence (Case 1 / Case 2 of `#hyp-directed-separation-under-composition`), and shared-substrate goal-shaping (R4 from §5).

**Strategic composition's contribution to this axis: *none, by itself*.** Strategic composition with goal-blind routing and distinct substrates is Class 1 at the composite level — exactly as the formal criterion gives. Cournot is the canonical witness.

### Axis B — Dynamic regime (missing — proposed here)

What it would describe:

- The *type of joint dynamics* the composite admits — contraction to a shared state, convergence to an equilibrium structure, cyclic distributional behavior in the CCE-support.
- Categorical, not scalar: contraction-regime / equilibrium-regime / cyclic-distributional-regime. Tracks `#deriv-strategic-composition`'s $\alpha' / \beta'$ partition exactly.

**Determinants for a composite:** objective alignment (alignment routes C-i/ii/iii give contraction-regime; strategic route C-iv gives equilibrium-regime), game structure (potential / monotone / general), learning dynamics (best-response / regret-minimization / replicator).

**Strategic composition's contribution to this axis: *everything*.** Strategic composition is exactly the move from contraction-regime to equilibrium-regime (under $\alpha'$) or to cyclic-distributional-regime (under $\beta'$). This is what `#deriv-strategic-composition` derives substantively.

### Axis C — Macro-state type (also missing — the deepest one)

What it would describe:

- The *type* of the composite macro-state $G_t^c$: state-variable (aligned case) vs fixed-point object (strategic case).
- Binary at the composite level: state-variable composites can be analyzed via state-space dynamical-systems machinery; fixed-point-object composites need equilibrium-theoretic machinery.

**Determinants:** the scope route — C-i/ii/iii give state-variable macro-state; C-iv gives fixed-point macro-state.

**Why this matters:** machinery that operates on $G_t^c$ as a state-variable (the bridge lemma in `#form-composition-closure`, the persistence template `#result-sector-persistence-template`, the orient cascade `#der-orient-cascade`) cannot lift to fixed-point macro-state composites without adaptation. The architectural-class criterion is one such piece of machinery — it operates on $G_t^c$ as a perturbable random variable, and fails to type-check for $G^c = \mathcal E$.

### Why the conflation persisted

The current segments — `#deriv-strategic-composition`, `#der-directed-separation`, `#impl-strategic-composition` — all describe strategic composites as having "Class 2" or "Class 3" architecture because they were *trying* to capture the genuine Axis B / Axis C content but had only Axis A vocabulary available. The conflation is honest in motivation — strategic composites genuinely *are* different in important ways — but unfaithful to the formal criterion. The §§2–6 push made the unfaithfulness explicit.

## §7.3 What the reframing buys

If the framework introduces Axes B and C explicitly (or surfaces what is implicit in `#disc-separability-pattern`'s seven-ladder treatment), several things land cleanly that currently float:

**(B1) The contraction-to-equilibrium handoff `#impl-strategic-composition` describes** is the genuine content. Under contraction-regime, `#result-sector-persistence-template` applies; under equilibrium-regime, the A2'-analog transfers to the joint potential's curvature (Monderer-Shapley) or joint Jacobian's symmetric part (Rosen). The regime-change is *the* result. Calling it "Class 3 (Coupled) composite" was a label-error trying to mark the regime-change in architectural vocabulary that does not carry the load.

**(B2) The "modular safety architectures fail under goal divergence" implication** (`#impl-strategic-composition` §"Modular safety architectures fail under goal divergence") survives reframed — but the failure mechanism is *not* architectural-class change. The mechanism is dynamic-regime change: modular safety constructions designed for contraction-regime composites do not transfer to equilibrium-regime composites because equilibrium dynamics admit saddle-points, multi-equilibria, and last-iterate non-convergence that the contraction-regime guarantees rule out.

This is actually a *better* argument than the original Class 3 framing. The Class 3 framing implied "the composite has fully-merged processing" — a strong and structurally hard-to-justify claim. The dynamic-regime framing implies "the composite has equilibrium-shaped dynamics" — exactly what `#deriv-strategic-composition` already derives, and exactly what the modular-safety failure modes (mesa-optimization, constitutional AI red-teaming) instantiate empirically.

**(B3) The Class 3 wrapping construction** (`#der-class-coercion-via-wrapping`) becomes more cleanly scoped. It is a tool for converting Class 3 *components* (logogenic LLMs, motivated cognition) into Class 1 composites at structural-leakage cost. It is *not* a tool for converting strategic composites into aligned composites — the dynamic-regime change between strategic and aligned is *independent* of architectural class. The wrapping construction does not, and cannot, force equilibrium dynamics into contraction dynamics.

**(B4) Three senses of "Class 2" collapse into the architectural sense only.** Per §6, three senses currently circulate:

- Class 2 (Partial) = within-agent mixed pathway, per `#der-directed-separation` formal definition.
- Class 2 (Partial) = composite-level partial coupling via cross-agent belief content, per `#deriv-strategic-composition` and `#der-directed-separation` Composite-level inheritance.
- Class 2 (Partial) = "directed separation holds for identified submodules," per `#disc-separability-pattern` row 3.

Under the reframe, only the first sense survives as architectural Class 2; the second is reclassified as "strategic composite under equilibrium dynamic-regime, structurally Class 1 architecturally" (or, alternatively, dropped from architectural classification entirely); the third needs its own audit (it likely means "structured-repair tier for the Architecture ladder" in the separability-pattern sense, which is meta-pattern vocabulary not architectural classification per se).

**(B5) The architectural-class lift to composites becomes clean.** Per `#hyp-directed-separation-under-composition`:

- Class 1 sub-agents + goal-blind routing + distinct substrates → Class 1 composite.
- Class 1 sub-agents + goal-dependent routing → Class 3 composite (Case 2 mechanism).
- Class 1 sub-agents + shared substrate with $G^c$-dependent allocation → Class 3 composite (R4 mechanism).
- Class 3 sub-agents (any routing) → Class 3 composite.
- Class 2 sub-agents → Class 2 composite (or Class 3, depending on routing and substrate).

This is the clean architectural-axis composite-class-inheritance table. It is independent of objective-alignment (which lives on the dynamic-regime axis).

## §7.4 Why this is a "framing is wrong" answer, not a softening

Joseph's brief: *"if attempts keep yielding neither a strengthening nor a clean no-go, it usually means we're framing the question wrong or are missing some other aspect."*

The four routes (R1)–(R4) of §§2–5 do not yield a strengthening of the Class 2 claim to Class 3 from strategic composition alone. (R1) and (R4) do yield Class 3 from antecedents that are *not* strategic composition. (R2) and (R3) yield no Class 3 derivation at all.

The current "Class 2" claim itself fails on §6 — it conflates belief-content (b) with processing-pathway (a). The formal criterion gives Class 1 (Separated) at the composite level under goal-blind routing.

Both pushes — toward Class 3 and back to Class 2 — converge on the same diagnosis: the architectural-class axis is the wrong axis for what strategic composition genuinely contributes. The reframe is not a softening; it is a *replacement*. The architectural-class claim about strategic composites is **deleted** (per integration-is-replacement); a new axis (Axis B — dynamic regime — or its variant) takes the load the architectural claim was inappropriately carrying.

This is the strengthen-first landing pattern in the visceral form: the original Class 2 claim is *withdrawn*, the strengthening attempt to Class 3 is *refuted with witness* (Cournot), and the no-go is *present truth* — strategic composition does not change architectural class, the dynamic regime is what genuinely shifts. The no-go is on the critical path for re-doing the segments correctly.

## §7.5 Where the framework already has the new axis implicit

The good news for §7's reframe: the framework *already has* most of the dynamic-regime axis implicit, scattered across multiple segments. Surfacing it explicitly is reorganization, not new derivation.

- **`#deriv-strategic-composition` sub-scopes $\alpha'$ and $\beta'$** — the cleanest existing formulation of dynamic-regime classification. $\alpha'$ = potential/monotone (equilibrium-regime with Lyapunov structure transferring), $\beta'$ = non-potential non-monotone (CCE-cyclic-distributional regime). This is Axis B in the language `#deriv-strategic-composition` already uses; what is missing is the *contraction-regime* tier above $\alpha'$ that covers the aligned case (C-i/ii/iii), which would round out the ladder.
- **`#scope-composite-agent` route C-iv** explicitly distinguishes strategic composites from alignment/mutual-benefit composites by macro-state type — Axis C content.
- **`#form-composition-closure`'s contraction-regime presupposition** in `#result-sector-persistence-template` and the bridge lemma — implicit Axis B "contraction-regime tier."
- **`#disc-separability-pattern` Contraction ladder (row 4)** — Tier 1 strong monotonicity / Tier 2 local convexity / Tier 3 domain-specific. This is the *contraction-regime* sub-classification, parallel to but currently not aligned with the dynamic-regime classification.
- **`#impl-strategic-composition`'s "contraction-to-equilibrium hand-off"** language — the framing already exists; what is missing is that this hand-off *is* the dynamic-regime axis transition, not an architectural-class transition.

The reframe is largely a matter of *naming what the framework already does* on the dynamic-regime axis, deleting the awkward architectural-class overflow into that territory, and adding the contraction-regime tier as a peer of $\alpha'/\beta'$.

## §7.6 What the reframe does *not* settle

Three things stay open after the reframe:

**(O1) Whether Axis B and Axis C are genuinely distinct or one collapses into the other.** Axis B (dynamic regime) and Axis C (macro-state type) move together in current AAT: state-variable macro-state ↔ contraction-regime dynamics; fixed-point macro-state ↔ equilibrium/cyclic regime. Whether this is a structural identity or a contingent alignment is open. Mean-field-game limits ($N \to \infty$, `#deriv-strategic-composition` Working Notes) may show distributional fixed-point macro-state with contraction-regime dynamics — would break the alignment if so.

**(O2) Whether Axis B should be a meta-segment like `#disc-separability-pattern` or distributed across the relevant segments.** A meta-segment landing would parallel the existing separability/identifiability/coordinate-forcing meta-architectural pattern segments. A distributed treatment would leave the axis implicit and rely on cross-references. The standalone-paper candidacy in `#disc-separability-pattern` suggests meta-segments are first-class in AAT — Axis B may warrant the same.

**(O3) Whether the architectural-class composite-inheritance table from §7.3 (B5) should land as a new sub-section of `#hyp-directed-separation-under-composition`, a new derivation segment, or stay as Working Notes.** The hypothesis segment currently treats the lift as conditional on routing structure but does not surface the shared-substrate mechanism from (R4). Promoting the table to a derived result requires the (R4) treatment, which has not been done in any current segment.

These three are Joseph-reserved per `99-VERDICT.md`.
