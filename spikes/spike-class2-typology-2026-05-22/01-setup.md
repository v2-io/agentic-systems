# 1. Setup — The Structural Question and the Canon Position

## 1.1 What the canon currently says

From `#der-directed-separation`:

- **Class 1 (Separated).** $f_M(M_{\tau^-}, e_\tau)$ — no $G_t$ argument. Directed separation holds by construction.
- **Class 3 (Coupled).** A single mechanism handles both epistemic and strategic processing; $G_t$ is causally upstream of every belief-update computation. Directed separation fails by construction.
- **Class 2 (Partial).** Some shared infrastructure, some separate pathways. Approximated by the scalar diagnostic

$$\kappa_{\text{processing}} = \frac{I(G_t \,;\, M_{\tau^+} \mid e_\tau,\, M_{\tau^-})}{H(G_t \mid e_\tau,\, M_{\tau^-})} \in (0, 1).$$

The scalar is explicitly *distribution-dependent* per `#der-directed-separation` §"Distribution dependence": the same Class 2 architecture exhibits low $\kappa$ on familiar tasks (modular stages dominate) and high $\kappa$ on novel tasks (goal-conditioned downstream reasoning dominates).

## 1.2 What the scalar hides

A single number on $[0, 1]$ cannot distinguish:

(a) Which **stage** of $f_M$ the coupling lives at. An agent that uses goals to *select observations* but processes them goal-blind has the same $\kappa$ behavioral signature as an agent that processes goal-blind observations but applies goal-shaped likelihood weights — yet only the second is a Class 2 deviation per the formal scope condition (per `#der-directed-separation` §"Scope Condition (directed-separation-scope)": "the directed separation is about the processing of events, not the selection of events").

(b) Which **source** within $G_t = (O_t, \Sigma_t)$ does the coupling. Identity-binding (objective-driven motivated belief) and sunk-cost commitment (strategy-driven belief-foreclosure) both raise $\kappa$, but they have structurally different dynamical signatures and admit different repairs (named in `#disc-adversarial-coupling-pressure` as distinct adversarial mechanisms, but not yet recognized as a *typology of Class 2*).

(c) The **form** of the dependency. Additive bias (the agent's belief shifts toward goal-preferred by a measurable offset) and multiplicative entanglement (the agent's belief-update *function class* changes with the goal, not just its output) are not interchangeable: the first is wrappable by post-hoc debiasing, the second is not.

(d) Where the coupling **propagates** through the rest of $f_M$. A featurization-stage coupling contaminates everything downstream; a consolidation-stage coupling does not.

## 1.3 What already exists in canon that gestures at the sub-typology

The framework has scattered pieces that *should* compose into a sub-typology but haven't been recognized as such:

1. **`#disc-adversarial-coupling-pressure` mechanism table.** Three distinct $G_t \to M_t$ pathways:
   - Identity-binding: $O_t \to M_t$ (objective leaks into belief via identity-binding).
   - Affect/urgency: bypass of the orient cascade temporally (not strictly $G_t \to f_M$ at all; rather a *prevents-$f_M$-from-running-cleanly* mechanism).
   - Sunk-cost engineering: $\Sigma_t \to M_t$ (strategy commitment forecloses belief-revision).

   Presented as adversarial mechanisms (the externally-driven leg of the M4 modularity-state-dynamics triad), not as a *Class 2 typology*. But they are structurally three distinct cells of the (source × stage) parameterization this spike develops.

2. **`#der-directed-separation` Class-1-by-structure vs Class-1-by-behavior refinement.** Inside the Class 1 cell, two sub-types are recognized:
   - *Structure:* the belief-update query has no $G$ argument; structural separation by type signature.
   - *Behavior:* the query passes $G$ but the component is instructed not to use it; separation by compliance.

   This is exactly the content/process distinction applied at the wrapper level. A symmetric refinement *within Class 2* has not been written.

3. **`#der-interaction-channel-classification` four-regime carve.** The recipient-side classification of incoming events (informative-update / magnitude-shock / structural-shock / ambient-erosion) is structurally analogous to what this spike proposes on the goal-coupling side. The move — name what kinds of information sit where in the architecture — has been performed on the signal-side but not yet on the goal-source side.

4. **`#def-agent-spectrum` Working Note (2026-05-18).** Identifies that the *dangerous* $G_t \to f_M$ leakage concentrates "in the inference about the unobserved present" — the free-prior step. Identified as a "where-in-the-inference localization" candidate finer-grained companion to the architectural classification.

5. **`spikes/spike-leakage-locus-2026-05-18.md` Leakage Locus Lemma.** Formalizes (4): goal contamination can move belief only along the *Fisher null space* $\ker\mathcal I_\tau$ of the observation given the current latent state. This localizes *where in state-space* the leakage acts, regardless of which stage of $f_M$ the coupling enters. Composes with (but does not subsume) the stage typology this spike develops — the two answer complementary questions ("through what stage does the coupling enter" vs "in what subspace does its effect live").

6. **W₀/W₁/W₂ wrapping regime** (`#der-class-coercion-via-wrapping`). The wrapping construction classifies *coercion regimes* at the wrapper level: W₀ (no wrapping), W₁ (strict wrapping — no $G$ in the belief-update query), W₂ (partial wrapping — $G$ in the query but typed output structuring). These are *downstream* of the Class 2 sub-type: which wrapping regime is sufficient depends on the form of coupling in the un-wrapped agent.

## 1.4 The question pushed back to first principles

Following Joseph's pointer ("what constitutes fully-entangled should give some clues as to what can be partially detangled"):

What is the structural content of "Class 3 (fully Coupled)"?

Per `#der-directed-separation` (transformer LLM example): a single mechanism handles both epistemic and strategic processing; goals are causally upstream of *every* computation; attention processes goals and observations together. The "fully" is doing real work — it means:

- Goals enter at *every stage* of belief-update processing (no stage runs goal-blind).
- The form of dependency is *process-level* — the function class changes with the goal, not just the output.
- The architectural channels are *all available sources* — both $O_t$ and $\Sigma_t$ can act on belief-update.

Each of these is a **separable degree of freedom**. The Class 1 limit is the opposite: no stage couples, no source acts, form is irrelevant (there is no dependency). Class 2 is everything between: *some* stages couple, *some* sources act, the form *may* be content or process.

This gives the parameterization the rest of the spike develops.

## 1.5 What the spike does not claim

- It does not claim that the (stage × source × form) parameterization is the *only* useful refinement of Class 2. Other axes (e.g., temporal grain — does coupling act on every event vs only on goal-relevant events — or the magnitude axis $\kappa_{\text{processing}}$ already captures) are valid orthogonal refinements; the parameterization here is the one that comes out of pushing on Joseph's "what kinds of information are used where" question.
- It does not claim each cell of the parameterization is empirically distinguishable in current AAT machinery. Some cells (e.g., source-only differences) may require an extended behavioral estimator that probes counter-factual goals beyond the current $\hat\kappa_{\text{processing}}$.
- It does not derive the typology from `#der-directed-separation`'s canonical conditional-independence statement alone; the stage-decomposition is a *new structural apparatus* posited on top, made honest by the formal definitions in §2.
- It does not address Class 3 → Class 2 *coercion* (that is the wrapping construction's territory). It addresses *what Class 2 is*, not how to *reach* Class 2 from Class 3.
