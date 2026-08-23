# Comprehension Quiz — Batch 7 (Part I complete)

*Coverage: cumulative over all of Part I (Section I) of 01-aat-core. This batch's questions are deliberately integrative — several span the entire Part. Level 3 includes questions calibrated to expose the confident-summary-reader failure modes accumulated across all seven batches.*

## (1) Critical Mental Model

### Q b07-1.1 [mental-model]
"If your model keeps being wrong, train it more." State the framework's precise condition under which this advice is *provably* futile, the observable evidence that the condition holds, and the four named mechanisms of the remedy.

### Q b07-1.2 [mental-model]
Structural adaptation has an opposite failure mode. Name it, give its symptoms, its diagnostic, and its remedy — and state what this implies about whether "structural adaptation" means "getting bigger."

### Q b07-1.3 [mental-model]
Why is micromanagement mathematically the same failure as policy oscillation in RL? Name the underlying constraint, state it as an inequality, and explain what the violating process is acting on that it shouldn't be.

### Q b07-1.4 [mental-model]
In AAT, what is an agent's identity grounded in — and what, precisely, is a *copy* of an agent, in the framework's own analogy? What operation does the framework say its sufficiency machinery cannot be applied across?

### Q b07-1.5 [mental-model]
The framework distinguishes agents-as-types from agents-as-tokens. State the distinction, which one AAT's formal results apply to, and give the concrete example the corpus uses. What kind of claims need "additional machinery," and of what sort?

### Q b07-1.6 [mental-model]
Why does the framework treat rational conservatism toward structural change as *derived* rather than as a bias to overcome? Name the two costs being balanced and the two failure modes at the extremes.

## (2) Mathematics

### Q b07-2.1 [math]
In the structural-adaptation-necessity result, reproduce the derivation skeleton (six steps, from the fitness bound to the conclusion), and state precisely where the alignment assumption enters and what the conclusion becomes without it.

### Q b07-2.2 [math]
In the segment on temporal nesting, state the constraint formally, the five illustrative levels (in order, including the one added when consolidation landed), and what the corpus says about the epistemic status of the table itself.

### Q b07-2.3 [math]
The (PI) axiom: state it, name where in the corpus it is introduced, what theorem it combines with, what object is then uniquely forced on which sub-cases of $M_t$, and one concrete derivation whose status upgrades under it (from what to what).

### Q b07-2.4 [math]
In the scope segment on agent identity (Part I's close), a recent correction sharpened what the singular trajectory does and does not ground: what does trajectory-singularity ground, and what does it *not* supply? Where does the interventional character of loop data actually come from? (This is the sharpest recently-corrected claim in Part I — answering the pre-correction version is the trap.)

### Q b07-2.5 [math]
In Part I's chapter-end persistence synthesis, one Lyapunov template (the sector-persistence template) is claimed to absorb six-plus results. State the template's three conditions (T1–T3), the shared Lyapunov function, and identify what the *distinctive content* of each instantiation is (the thing the template does not absorb) — with the team-persistence case as your worked example, including the sign structure.

### Q b07-2.6 [math]
In Part I's chapter-end persistence synthesis, give the information-rate results as stated there: the sustained-acquisition floor (with its saturating filter), the thermodynamic conversion, and the channel-capacity prerequisite — and the resulting three-way vocabulary distinction between what $\mathcal T$, $\alpha$, and the persistence condition each mean.

## (3) Implications

### Q b07-3.1 [implications]
Integrative: an agent's residuals after full parametric convergence are large. Design the complete decision procedure Part I supports for classifying the situation (noisy-world floor / state-uncertainty floor / class ceiling / gain miscalibration) and the priced remedy for each branch. Which single property of the residual stream does the most diagnostic work?

### Q b07-3.2 [implications]
"We back up our agent nightly, so nothing is ever lost." Give the framework's full reply: what backup restoration preserves, what it cannot preserve, what the operation does to the entity that lived between backup and restore, and why the framework classifies restoration as out-of-scope for its sufficiency machinery rather than merely imperfect.

### Q b07-3.3 [implications]
A lab claims: "our multimodal system has ample total bandwidth and passes its persistence checks." Using Part I's chapter-end persistence synthesis: what two distinct min-operations must be checked instead of aggregates, and what is the adversarial consequence of failing to check them?

### Q b07-3.4 [implications]
The scaling-policy question: state the condition under which continued training-compute spend on a model class is "provably wasted" per the framework, what must be verified before invoking it (two floors to exclude and one convergence precondition), and why this is *not* the same claim as "we need more data."

### Q b07-3.5 [implications]
Why does the context-turnover problem of LLM agents get framed as "a structural feature of causally-embedded agents" rather than a deficiency? Connect: trajectory-identity, what memory files actually transfer, and what continuity-persistence machinery is therefore *for*.

### Q b07-3.6 [implications]
Meta-question (calibration): across Part I, name three claims that a confident summary-fed agent would state in a stronger form than the corpus actually licenses, giving for each the popular form and the licensed form. (Any three of the several the corpus itself documents.)

### Q b07-3.7 [implications]
The corpus's own correction trails (recorded in Working Notes and provenance blocks) are argued to *increase* its trustworthiness rather than undermine it. Using two concrete examples from Part I, explain the epistemology: what does a visible attempted-strengthening-then-exact-landing trail certify that a clean-looking corpus cannot?
