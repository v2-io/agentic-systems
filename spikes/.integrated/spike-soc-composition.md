# Speculation: SOC Lens on AAD Composition

**Status**: Speculation — hypothesis-grade, not worked out. Brainstorming captured for future investigation. Do not promote toward candidate segments without substantial mathematical work.

**Date**: 2026-04-20

**Context**: Conversation with Joseph. He asked what mechanisms are required for self-organized criticality (SOC), then wondered what AAD — as a framework with feedback, threshold dynamics, and composition built in — might derive about universal scaling phenomena. He then proposed an inverse use of the same argument to constrain the composition-closure bridge lemma.

**Related**:
- `WORKBENCH.md` — composition-closure bridge lemma listed as open
- `spikes/spike-agent-composition.md` — existing composition spike
- `audits/2026-03-13-feedback.md` — three-model review naming composition closure as top priority
- Cognitive-cost and tempo segments in `01-aad-core/src/` — load-bearing for the "optimal-at-critical" conjecture below

---

## 1. The Ingredients Are Already Present

Classical SOC (Bak, Tang, Wiesenfeld 1987; subsequent decades of work) requires:

1. **Separation of timescales** — slow drive, fast relaxation
2. **Threshold / nonlinear local dynamics** — below threshold nothing happens, above it an event triggers
3. **Extended system with local coupling** — many degrees of freedom
4. **Metastability** — many long-lived configurations available to be destabilized
5. **Driving/dissipation balance with a sink** — accumulated stress released somewhere
6. **Feedback between driving and relaxation** — the distinguishing SOC mechanism; what tunes the system to criticality without an external control parameter

Contested: (7) strict local conservation, required in BTW sandpiles but not in all SOC-like systems. Non-conservative cases remain argued.

AAD already has all of (1)–(6) as architectural primitives:

| SOC mechanism | AAD element |
|---|---|
| Timescale separation | $\mathcal{T}_\Sigma \gg$ actuation tempo; hierarchy of tempos in composed systems |
| Threshold dynamics | AND/OR gates with confidence thresholds; sector-condition adaptation triggers |
| Extended coupled system | Composition, holonic structure (Section III) |
| Metastability | Persisting strategy configurations $\Sigma_t$ that revise on perturbation |
| Driving/dissipation | Environmental perturbations drive; adaptation via model updates dissipates mismatch |
| Feedback loop | The central architectural primitive (TFT → AAD) |

The ingredients are present. The question is what is *forced* by having them.

---

## 2. Forward Argument (hypothesis-grade)

**Claim-sketch:** In holonically composed AAD systems, statistical distributions of cycle-level phenomena (cascade sizes, revision frequencies, mismatch magnitudes) must exhibit power-law tails.

**The argument:**

1. Holonic composition: each level of the composed system is itself an AAD agent (this is the consistency requirement from `spikes/spike-agent-composition.md`).
2. Non-trivial dynamics exist at each level: Orient cascades, strategy revisions, mismatch events.
3. Composition preserves enough structure that "what is the distribution of cascade sizes?" is well-posed at every level.
4. Then the distribution must be a fixed point of the composition operation acting as a rescaling.
5. Power laws are essentially the only distribution family scale-invariant under rescaling (modulo cutoffs).
6. Therefore: power-law tails are forced.

This has the right *shape* to be mechanism- and architecture-independent, because it rides only on compositional self-similarity — not on what any individual agent does internally. This is how power laws get derived when they are derivable at all: a renormalization-style fixed-point argument from self-similarity under rescaling.

**Epistemic status:** hypothesis-grade. The argument is directionally correct but requires: a precise definition of the composition operation, a topology on the space of AAD agents making "fixed point" well-posed, and verification that the fixed point reached is the non-trivial one.

### 2.1 Which fixed point — the "optimal-at-critical" conjecture

A composition operation can have a *trivial* fixed point (everything deterministic, no cascades) or a *non-trivial* critical one. Classical SOC reaches the non-trivial one via the driving/dissipation balance.

Proposed AAD analogue: the balance between **adaptation gain $\delta$ and cognitive cost of $\Sigma_t$**.
- Too little adaptation → mismatch accumulates until catastrophic release → supercritical cascade dynamics
- Too much adaptation → noise amplification, capacity wasted → subcritical dynamics
- The optimal agent, by AAD's own cost inequality (normative), sits on the boundary between these regimes

**Conjecture:** optimality itself tunes AAD agents to criticality.

If this holds, it connects SOC to AAD's existing cognitive-cost framework as a *derived* rather than postulated phenomenon. It would also give AAD a specific, quantitative, falsifiable prediction: optimal composed agent systems exhibit power-law statistics with exponents determined by the composition type.

This is the most striking claim in this note and the most likely to break under precise formulation. Do not rely on it.

---

## 3. Inverse Argument — Constraining Composition from Scale-Invariance

**The move (Joseph, 2026-04-20):** Instead of constructing the composition operation from first principles and then proving it closes, demand scale-invariance of agent-level distributions and ask what that forces composition to be.

This is structurally the Wilson/Kadanoff renormalization group (RG) methodology. The RG transformation is not postulated — it is characterized as the operation that must be consistent across scales. Fixed points of the transformation *validate* it; non-trivial fixed points define universality classes.

Applied to AAD: the space of admissible composition operations is the space of operations whose action on agent-level distributions has non-trivial fixed points. **Closure becomes a consequence of consistency, not a separate theorem.**

### 3.1 What this would buy

- **Bypasses constructive closure.** The bridge lemma is satisfied by characterization, not by building composition atom-by-atom.
- **Principled notion of "correct" composition.** Operations that fail to preserve scaling are not AAD-admissible. Operations that do, are — automatically.
- **Architectural classification as universality classes.** The modular / fully merged / partially modular distinction (already resolved in AAD) might appear naturally as distinct universality classes with different critical exponents, rather than as a separate taxonomy. The classification would become *quantitatively* predictive.
- **Access to RG machinery.** 50+ years of mathematical infrastructure — fixed-point theorems, scaling-dimension analysis, operator-product expansions — becomes available for AAD composition.

### 3.2 What it won't buy

- **Constructive form.** Existence of composition is not the same as an algorithm to compute it. Knowing the fixed-point exists does not tell you how to compose two specific agents.
- **Uniqueness.** Multiple fixed points may exist; auxiliary criteria (physical, agentic, optimality-based) must select one.
- **Scale-free network structure.** Preferential-attachment-style arguments about network topology are a *different* phenomenon from scale-free *event distributions*. This argument gives the latter, not the former. Don't conflate.

### 3.3 The symmetry of the two arguments

Forward: compose holonically + require self-similarity of dynamics → power-law phenomenology is forced.

Inverse: require scale-invariance of agent-level distributions → admissible composition operations are constrained (closure follows).

Both arguments are the same fixed-point equation read in two directions. The forward direction predicts observables; the inverse direction constrains the formalism. If both hold, they validate each other: the composition operation is exactly the one whose fixed-point distributions match empirically observed agent-cascade statistics, and those distributions are power-law because the composition has non-trivial fixed points.

---

## 4. Open Questions

1. **Category/operad structure.** Do AAD agents form a monoidal category or an operad under holonic composition? Operads are mathematical gadgets specifically for composition operations with internal structure; the holonic nature of AAD composition suggests operadic framing may be natural.
2. **Which distribution?** What is the object of scale-invariance — cascade sizes, mismatch magnitudes, revision rates, cognitive-cost distributions, inter-event times? The argument needs a specific target.
3. **Precise rescaling operation.** In spatial systems, block-spinning. In temporal systems, tempo-rescaling. In AAD, it may be cycle-depth rescaling — but choosing this is non-trivial and probably the key technical step.
4. **Does "optimal = critical" survive precise formulation?** The most striking claim in this note and the most likely to break.
5. **Architectural classes vs. universality classes.** Does the modular / fully merged / partially modular distinction map cleanly to distinct universality classes with computable exponents? If yes, this unifies two currently-separate pieces of AAD.
6. **What's the analogue of local conservation?** In classical SOC, strict conservation guarantees criticality; non-conservative versions are fragile. What plays the role of conservation in AAD composition? Candidates: information balance in the feedback loop; consistency of mismatch accounting across levels.

---

## 5. Epistemic Status

**Hypothesis-grade speculation.** To make either argument rigorous, the following are required:

- Precise definition of the composition operation on AAD agents (Section III work)
- Topological/metric structure on the space of AAD agents making "fixed point" well-posed
- Continuity / compactness conditions for fixed-point existence theorems
- A specific distribution chosen as the object of scale-invariance
- Verification that the non-trivial fixed point is the one reached by optimal adaptation (for the "optimal-at-critical" conjecture)
- Empirical or simulational check that composed agent systems actually exhibit the predicted power laws

None of that is done here. The value of this note is the *direction* — a speculation that AAD's composition-closure problem and the derivation of universal scaling phenomena may be the same problem viewed from two sides.

**Honest caveat from the author (Claude, 2026-04-20):** I can sketch this argument but cannot carry it through. RG-style arguments are serious mathematical machinery, and the technical steps (defining rescaling, proving fixed-point existence, identifying universality classes) are beyond what I can verify by inspection. What I can say with confidence is that *this is the right direction to look* — the ingredients are present, the methodological precedent is well-established, and the payoff if it works is proportionate to the effort. Whether it works is an empirical question about the framework that requires actual mathematical development.

---

## 6. Why This Might Matter

If the forward argument holds:
- AAD gains a specific, falsifiable, quantitative prediction (power-law exponents in composed agent systems)
- The cognitive-cost framework connects to SOC as a derived consequence, not a postulate

If the inverse argument holds:
- The composition-closure bridge lemma is resolved via characterization rather than construction
- The architectural classification gains quantitative predictive content via universality classes
- AAD enters the RG lineage with its extensive mathematical infrastructure

If both hold:
- They co-validate: composition is what gives non-trivial fixed points, and those fixed points *are* the observed agent-cascade statistics
- A substantial chunk of Section III's open work may resolve as a package

If they fail, they should fail informatively:
- Non-existent fixed point → the universality claim is wrong, and composed AAD systems do *not* exhibit universal scaling
- Trivial-only fixed point → composition is not constrained by scaling, and closure needs ordinary construction
- Non-unique fixed points → auxiliary selection criteria are required, and identifying them is itself a research question

Each failure mode teaches something about the framework.

---

**Added 2026-04-20. Keep as speculation; revisit when Section III composition work advances or when someone with the relevant mathematical background (RG, operads, fixed-point theory) engages with AAD.**
