---
slug: disc-sandbox-evaluation-ceiling
type: discussion
status: discussion-grade
depends:
  - der-loop-interventional-access
  - der-causal-hierarchy-requirement
  - def-pearl-causal-hierarchy
  - scope-agent-identity
stage: draft
---

# Discussion: The Sandbox Evaluation Ceiling

A structural negative result about pre-deployment evaluation follows once the loop-as-Level-2-engine result ( #der-loop-interventional-access) and the singular-trajectory commitment ( #scope-agent-identity) are both in hand: sandboxed evaluation is forkable by design, and that is exactly what makes it unable to identify deployment behavior at Pearl Level 2. The same property that makes a sandbox useful for testing — resettable, replayable, parallelizable execution — drops its data to Level 1, and the Causal Hierarchy Theorem then forbids inferring deployment intervention-response from it, regardless of how thorough the evaluation is. This is an instance of the framework's constructive-impossibility posture ( #disc-constructive-impossibility-posture): the no-go is paired with the precise statement of what *would* be required to escape it.

## Formal Expression

*[Derived (conditional on the singular-trajectory commitment of #scope-agent-identity)]*

Let a **sandbox** evaluation produce action–observation pairs $(a_{\text{sb}}, o_{\text{sb}})$ under *forkable* execution — the trajectory may be reset, replayed, or branched — and let **deployment** produce $(a_{\text{dp}}, o_{\text{dp}})$ on a *singular*, non-forkable trajectory.

1. Forkable execution yields Pearl **Level-1** (associational) data: branching across resets samples the policy-induced distribution $P(o \mid a)$, not the interventional $P(o \mid do(a))$ on a committed trajectory.
2. The singular deployment trajectory yields **Level-2** (interventional) data by #der-loop-interventional-access — each committed $a_{\text{dp}}$ *is* an intervention whose consequence is realized exactly once.

By the Causal Hierarchy Theorem ( #def-pearl-causal-hierarchy; Bareinboim, Correa, Ibeling & Icard 2022), Level-2 quantities are not in general computable from Level-1 data. Hence

$$P\big(o_{\text{dp}} \mid do(a)\big) \ \text{ is not identifiable from } \ \{(a_{\text{sb}}, o_{\text{sb}})\}\,,$$

i.e. claims about how the agent *would respond to interventions in deployment* cannot in general be answered from sandbox-derived evidence, irrespective of evaluation coverage or thoroughness.

## Epistemic Status

*Discussion-grade.* The no-go is a direct application of an external theorem (the Causal Hierarchy Theorem) to the framework's own trajectory ontology; it introduces no new mathematics beyond recognizing that forkability collapses the Pearl level. It is *exact* conditional on the singular-trajectory commitment of #scope-agent-identity and the loop-Level-2 characterization of #der-loop-interventional-access — strip the singular-trajectory commitment and the deployment data is no longer Level-2, and the gap does not arise. The claim is conservative in form: it is about *identifiability of the interventional distribution*, not about any particular evaluation method's measured accuracy. What is AAT-distinctive is not the theorem but its placement — locating the much-debated "alignment evaluations don't predict deployment behavior" pattern as a Pearl-hierarchy problem rather than a measurement-quality, coverage, or model-capability one.

## Discussion

**The negative result has positive content.** It sharpens *which* safety claims a sandbox can and cannot establish. Claims expressible at Level 1 — correlations between inputs and outputs under the agent's policy distribution — are within reach of sandbox evaluation. Claims about deployment-time intervention response (Level 2) are not; they require deployment-trajectory data. The framework's prescription is therefore not "sandboxes are useless" but "sandboxes have a *structural* ceiling, and deployment-time monitoring is not substitutable by pre-deployment evaluation regardless of evaluation thoroughness." For a practitioner running production agent loops, this is the same content as: the monitoring done *after* deployment is doing structural work the pre-deployment evaluations cannot do.

**Why this is a ceiling, not a gradient.** A measurement-quality limitation closes as rigor increases; a coverage gap closes as the test suite grows; a capability surprise closes as models are better understood. The sandbox ceiling closes under none of these, because the obstruction is the Pearl level of the data, not its quantity or quality. More sandbox rigor produces more and better Level-1 evidence, which the Causal Hierarchy Theorem still does not let one cross to Level 2.

**The downstream prescriptive content** — what deployment-time monitoring must structurally look like to discharge what sandbox evaluation cannot — lands in the framework's interventional-diagnostic / sidecar-monitoring treatment (the bi-predictability anchor at $89\%$ vs $44\%$ detection accuracy is developed in #der-causal-hierarchy-requirement's Discussion). The sandbox ceiling is what gives that downstream monitoring work its load-bearing role: it is not a redundant safety layer but the only layer with access to the Level-2 quantity the safety claim is actually about.

## Findings

### The Sandbox Evaluation Ceiling

**Brief:** Testing a system in a sandbox means being able to reset and replay it — and that replayability is exactly what stops the test from predicting how the system will act for real. A sandbox can branch the same situation many times, so its evidence is about *what tends to happen* (a correlation); deployment happens once and cannot be rewound, so acting in deployment is an *intervention*. There is a theorem (Pearl–Bareinboim) saying you cannot in general compute the second kind of fact from the first. So no amount of sandbox testing, however thorough, can certify how an agent will respond to interventions once deployed — that question is on the other side of a wall, and only deployment-time data is on its side.

**Impact:** Gives the much-debated observation that "alignment evaluations don't predict deployment behavior" a precise *structural* mechanism rather than a measurement-quality, coverage, or capability story — and, crucially, an exact statement of where the boundary lies (Level-1 claims are sandbox-evaluable; Level-2 deployment-intervention-response is not). The constructive flip is the operational payload: deployment-time monitoring is not a redundant safety layer but the only layer with access to the interventional quantity the safety claim concerns, which is why pre-deployment evaluation cannot substitute for it regardless of thoroughness.

**Novelty Claim:** *Application of established machinery* (Pearl 2009 / Bareinboim, Correa, Ibeling & Icard 2022 Causal Hierarchy Theorem) to AAT's singular-trajectory ontology. The theorem is adopted, not invented; the AAT-distinctive contribution is the recognition that *forkability is a Pearl-level demotion* — that the sandbox/deployment distinction is a Level-1/Level-2 distinction — and the resulting reframing of an entire family of pre-deployment safety-evaluation approaches as facing a structural ceiling rather than a closable gap.

**Related Work:**

| ASF concern | Prior-art language | Relationship / positioning |
|---|---|---|
| Interventional vs observational identifiability | Pearl 2009 *Causality* 2nd ed.; Bareinboim, Correa, Ibeling & Icard 2022 (Causal Hierarchy Theorem) | *formal antecedent* — supplies the impossibility (Level-2 not computable from Level-1 in general); AAT supplies the trajectory ontology under which sandbox = Level-1, deployment = Level-2 |
| Evaluation–deployment gap in AI safety | Practitioner literature on eval/deployment mismatch (qualitative) | *conceptual precursor* — names the phenomenon without a structural mechanism; AAT supplies the Pearl-hierarchy mechanism and the exact boundary |

**Search Log:**
- 2026-05-28 (*intuition-only* on the application-novelty): the Causal Hierarchy Theorem (Pearl 2009; Bareinboim, Correa, Ibeling & Icard 2022) is established and adopted directly. The unsearched claim is whether the specific recognition — *forkability of an evaluation harness is a Pearl-level demotion (Level-2 → Level-1), hence the sandbox/deployment gap is a hierarchy gap* — has been stated elsewhere as a structural ceiling on pre-deployment evaluation. Pre-search expectation: the constituent move (applying CHT to a trajectory-ontology distinction) is individually unsurprising; the framing as a *structural* ceiling on the AI-safety evaluation program, with the exact Level-1-evaluable / Level-2-not boundary, is plausibly AAT-distinctive but not yet verified under nominally-comprehensive search. Targeted future candidates: AI-evaluation / model-evaluation literature on distribution shift vs. interventional generalization; causal-inference-for-RL work on off-policy vs. on-policy identifiability framed for deployment guarantees.

## Working Notes

- Promoted to its own segment 2026-05-28 (PROPOSALS SP-25; audit-773921 Finding 4, Gemini). The content previously lived only as a `## ` subsection inside the chapter-end discussion #impl-causal-access (still cross-referenced from there). The promotion was an author-and-auditor convergence: the segment author's own Working Notes in #impl-causal-access had flagged it as a promotion candidate pending a future cycle, and the de-novo auditor independently surfaced it as a buried high-impact result.
- Open placement question carried from #impl-causal-access's Working Notes, now resolved toward Appendix A (the constructive-impossibility no-go home, alongside #deriv-stochastic-non-exit and #deriv-self-actuation-grounding) rather than an extension of #scope-agent-identity's Discussion — keeps the no-go discoverable in the family it belongs to and lets #disc-constructive-impossibility-posture reference it as an instance.
- The theorem-grade formalization of the underlying loop-Level-2 result lives in NeurIPS 2026 Paper 2 (`~/src/neurips/02-unified-convergence-rl/`, §5 / the (C1)/(C2)/(C3) triple); that is an in-review external draft, not canon, so the pointer is kept here in Working Notes rather than in the segment body. When that work is published it becomes an external citable object the body can cite directly.
- Candidate strengthening: if a future cycle wants this at `deriv-` tier, the move is to state the forkability-implies-Level-1 step as its own short lemma (currently asserted in the Formal Expression). Held; the discussion-grade application is honest as it stands.
