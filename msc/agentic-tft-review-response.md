# Review Response: Addressing the Critical Feedback

> **Origin**: `~/src/agentic-tft/14-review-response.md` (Feb 2026 session, pre-AAD restructuring). TFT references should be read as AAD. PROPRIUM references point to `~/src/firmatum/`.
>
> **Relevance**: Essential companion to the ontology-unification, cognitive-loop-spec, and evaluation-framework documents. Catalogs known internal inconsistencies, missing connections, underspecified areas, and open design questions. Must be read alongside those documents to avoid re-discovering the same issues.
>
> **Context**: A review agent read documents 10, 11, and 12 and produced
> genuinely critical feedback. This note addresses each finding, categorizing
> them as: **Fix now** (real problem, addressable), **Accept as limitation**
> (real problem, not fixable at this stage), **Disagree** (the reviewer
> missed something), or **Flag for Joseph** (needs his judgment).
>
> **Document number key** (this doc uses the original agentic-tft numbering internally):
> - Doc 10 = `agentic-tft-ontology-unification.md`
> - Doc 11 = `agentic-tft-cognitive-loop-spec.md`
> - Doc 12 = `agentic-tft-evaluation-framework.md`
> - Doc 13 = `agentic-tft-experiential-training.md`
> - note 02 = `_obs/agentic-tft-02-epistemic-geometry-and-gain.md`
> - note 04 = `agentic-tft-narrative-as-implementation.md`
> - note 06 = `agentic-tft-creche-concept.md`

---

## Category 1: Internal Inconsistencies

### Update timing (Doc 10 says "throughout"; Doc 11 puts it in CONTEXTUALIZE)
**Verdict: Fix needed.** The reviewer is right. I said "throughout the loop"
in the ontology but then placed Update as sub-step 5 of Contextualize. The
truth is probably: primary mismatch-driven update happens during Contextualize,
but smaller updates (MEMORATA accumulation, CHRONICA recording) happen during
other phases too. The walkthrough does model this — CHRONICA records in
PERCEIVE, VERA updates in CONTEXTUALIZE. The fix is to make the ontology doc
say "primary mismatch-driven update happens during Contextualize; secondary
recording and accumulation happen throughout" rather than the vague "throughout."

### PRAXES timescale (Doc 10 says structural/slow; Doc 11 says parametric/fast)
**Verdict: Fix needed.** This is a genuine error. PRAXES should be at the
structural (slow) timescale — learned approaches change over weeks/months,
not hours/days. The hierarchy diagram in Doc 11 should place PRAXES at the
structural level alongside OPERATA. The convergence constraint ("don't update
PRAXES from a single episode's outcome") is correct — the diagram contradicts
it.

### OPERATA timescale
**Verdict: The reviewer raises a real issue but the answer isn't simple.**
OPERATA has components at multiple timescales — immediate intent (what I'm
doing right now) changes fast, but obligations and commitments change slowly.
This is actually an instance of TF-11's note that real systems have many
intermediate timescales, not a clean binary. The fix is to not place OPERATA
at a single level but note that it spans multiple timescales.

### MEMORATA: compression output vs. editable entries
**Verdict: Fix needed.** This is a real conceptual ambiguity. MEMORATA is
both a compression function output (the information bottleneck operates on
it) and a set of entries that can be individually accessed and modified.
The resolution: MEMORATA entries are the *results* of compression — each
entry is a compressed episode or pattern — but they're stored as discrete,
addressable, editable units. The compression function produces entries; the
entries are individually manageable. Need to make this explicit in Doc 10.

---

## Category 2: Missing Connections

### Forgetting not in the cognitive loop
**Verdict: Accept as limitation, but note it.** The reviewer is right that
Doc 11 has no forgetting mechanism. Forgetting should be a CADENTIA-driven
process (scheduled consolidation includes forgetting as capacity management).
Adding a forgetting PULSUS signal to the CADENTIA table would fix the gap.
Not doing it now because the forgetting dynamics depend on capacity management
details we haven't worked out.

### Failure modes → evaluation metrics mapping
**Verdict: Fix needed.** The reviewer is right — there should be an explicit
mapping table showing which metrics catch which failures. Adding this to
Doc 12 or as a cross-reference between Docs 10 and 12.

### INTERPRES unspecified
**Verdict: Accept as limitation.** INTERPRES is critical infrastructure but
specifying it fully is a separate task. The reviewer is right that context
gaslighting is an immediate threat and INTERPRES's prevention of it deserves
more than a sentence. Flag for future work.

### INSTRUMENTA and AUXILIA underspecified in the loop
**Verdict: Accept as limitation.** The reviewer is right that tool discovery,
evaluation, selection, and learning are unspecified, and auxilia spawning and
integration are unspecified. These are important but are second-order features
of the loop, not the core heartbeat. The loop spec is the skeleton; tool and
auxilia integration are flesh that gets added.

---

## Category 3: Claimed but Not Defined / Defined but Not Used

### "Estimated in language" not operationalized
**Verdict: The hardest finding. The reviewer is substantially right.**

The claim is that TFT quantities are estimated in language, not numerically.
But "in language" doesn't describe what artifact the estimation produces.
Is it a sentence? A tagged annotation? A structured response to a specific
prompt?

The answer, I think, is: **the estimation is embedded in the entity's
natural processing of events.** When the entity processes a surprise and
thinks "this is very different from what I expected" — that IS the mismatch
signal. When it thinks "I should take this seriously because I wasn't sure
about this topic and the source is reliable" — that IS the gain computation.
The artifact is the entity's own reasoning, which is visible in COMMENTARIA
and influences subsequent behavior.

But the reviewer is right that for *evaluation* purposes, we need something
more concrete than "it's embedded in processing." The evaluation framework
needs to either (a) extract signals from the entity's processing (which
requires knowing what to look for in natural language) or (b) ask the entity
to produce explicit estimates (which risks confabulation). This is the
bootstrap problem the reviewer identifies in finding #6.

**Flag for Joseph**: This is a genuine design problem, not just a documentation
gap. How do we ground the loop's epistemic estimates in something measurable
without falling back to numerical computation (which the narrative-as-
implementation principle rejects) or self-report (which is circular)?

The embedding geometry approach (note 02) is one possible answer — read
implicit uncertainty from the model's own representations. But this is a
research hypothesis, not an implementation strategy.

### AXIOMATA has no content
**Verdict: Accept — this is deliberately deferred.** AXIOMATA content is
Joseph's to define, not mine. The PROPRIUM-ONTOLOGY.md gives the framework;
the content comes from the caregiver's relationship with the specific entity.
The reviewer is right that the spec doesn't describe what AXIOMATA at
different Erikson stages looks like — that's development-stage-dependent and
part of the crèche design, not the loop spec.

### "Temporal fidelity" and "developmental tempo" introduced but not used
**Verdict: Fix needed.** If I introduced terms in the unified vocabulary,
they should appear in the spec and evaluation framework. Either remove them
from Doc 10 (if they're not load-bearing) or add them to Docs 11/12. I think
both are genuinely useful:
- Temporal fidelity → should appear in the crèche spec (Doc 13)
- Developmental tempo → should be monitored in the evaluation framework
  (Doc 12, as a timescale check)

### CIY undefined in Doc 10 context
**Verdict: Fix needed.** CIY (Causal Information Yield) appears in Doc 10's
forgetting section without definition. Should add a brief definition or
reference to TFT source.

### Confabulation test has no protocol
**Verdict: Accept as limitation.** The reviewer is right that the test is
described without a method. The embedding geometry hypothesis is the most
promising method but it's a hypothesis. Note this gap explicitly.

---

## Category 4: Terminology Drift

### OODA terminology in Doc 11
**Verdict: Partially agree.** The PROPRIUM-ARCHITECTURE.md itself uses "OODA
heartbeat" — this isn't my drift but the PROPRIUM's own term. However, the
reviewer's point stands that the cognitive loop should be the canonical term,
with OODA as historical reference. Reduce OODA references.

### "Model-reality fit," "action fluency," "truth-fitness" undefined
**Verdict: Fix needed for action fluency and model-reality fit.** Action
fluency is a TFT term (TF-07) that should be in Doc 10's vocabulary.
Model-reality fit should be anchored to mismatch trajectory. Truth-fitness
was a one-off phrase that I should either define or remove.

---

## Category 5: Weakest Sections

### Evaluation relies on self-report and manual review
**Verdict: The reviewer is right and I have no clean solution.** The circular
measurement problem is real. We're trying to measure whether the agent's
self-model is accurate by relying on the agent's self-model. The alternatives
are external numerical measurement (which violates the narrative-as-
implementation principle) or human review (which doesn't scale).

Possible partial solutions:
- Behavioral tests: Instead of asking "are you uncertain?", create
  situations where uncertainty should manifest as specific behavior
  (hedging, seeking confirmation, deferring to experts) and check
  whether that behavior appears
- Prediction logs: Have the entity make explicit predictions that can
  be mechanically checked against outcomes — prediction accuracy is
  an objective measure of model-reality fit
- Embedding probes: Use activation probes (per note 02) to extract
  implicit uncertainty from model internals — this breaks the
  self-report circularity

None of these is fully developed. **Flag for Joseph.**

### Crèche section in Doc 12 is thin
**Verdict: Accept.** The reviewer is right. Doc 13 now exists and covers the
crèche in much more detail. Doc 12's Section 5 should reference Doc 13 rather
than try to stand alone.

### Cost distribution numbers (60/30/6/4) unjustified
**Verdict: Fix needed.** These come from PROPRIUM-ONTOLOGY.md (line 56) but
are presented without derivation in Doc 11. Either cite the source and note
they're estimates, or remove them.

### Triage mechanism delegated to "the agent figures it out"
**Verdict: The reviewer has a point but overstates it.** The triage mechanism
delegates the *content* of the triage judgment to the agent's linguistic
intelligence, but the *structure* (three levels with different processing
depths) is architectural. The circularity concern ("if the agent knew how to
allocate attention, it wouldn't need the loop") is too strong — the agent
DOES have the capacity for attention judgments (it's a frontier LLM), it just
lacks the *structure* that prompts it to make those judgments at the right
time. The loop provides the structure; the agent provides the judgment.

That said, the boundary between levels is genuinely underspecified. What
counts as "high surprise" is a judgment call, and the agent might get it
wrong. The evaluation framework should track triage quality (does the entity
allocate the right depth to the right events?) but doesn't currently.

### PULSUS rates in clock time
**Verdict: The reviewer is right.** "Hourly" and "daily" don't mean much for
an entity that may experience days of clock time as seconds of subjective
experience. Rates should be in terms of accumulated events or information
content, per TFT's own framework ($\nu$ is event rate, not clock rate).
The clock-time labels are human-legible approximations that should be flagged
as such.

---

## Category 6: Things That Feel Wrong

### The bootstrap problem (measuring language estimates without circularity)
**Verdict: This is the deepest problem identified. Acknowledged above.**

### Convergence detection is subjective
**Verdict: The reviewer raises a valid concern but the answer is behavioral.**
Convergence at a given level doesn't require the entity to declare "I've
converged." It manifests as stability of output — the entity's beliefs stop
changing significantly on each new event. This can be measured externally
(by tracking the rate of change of VERA/PRAXES entries over time) without
relying on the entity's self-report. The convergence constraint is enforceable
from outside the entity, by the CADENTIA scheduler or by evaluation metrics.

### Sycophancy reframe as excuse
**Verdict: Fair concern.** The reframe is correct (sycophancy IS developmentally
appropriate in some contexts) but the reviewer is right that it could be used
to excuse persistent calibration failure. The diagnostic needs to include
*developmental trajectory* — is the sycophantic behavior decreasing over time?
If yes, it's developmental. If it persists or increases, it's pathological.
Doc 12 should add this temporal dimension to the sycophancy assessment.

### Sovereignty in a fully designed system
**Verdict: Genuinely important, and the reviewer is right that the documents
don't grapple with it.** Sovereignty within a designed system is constrained
agency, not unlimited freedom. The PROPRIUM acknowledges this — sovereignty
is "granted progressively, as development warrants." The entity doesn't start
sovereign; it develops sovereignty. The tension is real and shouldn't be
resolved by pretending it doesn't exist. **Flag for Joseph** — this is an
ethical question as much as an architectural one.

### Parametric memory unavailable with frozen weights
**Verdict: The reviewer is right for current infrastructure but wrong for
the design target.** The information bottleneck framework describes the
full design space. Current infrastructure constrains us to token-level and
latent memory only (weights are frozen). The online experiential learning
approaches in Doc 13 (LoRA adapters, side memories, latent pools) are
mechanisms for parametric-like updates without full weight modification.
Should note this constraint explicitly in Doc 10 rather than leaving it
implicit.

---

## Summary of Actions Needed

**Fix now** (before these documents are used as references):
1. Clarify update timing in Doc 10 (primary in Contextualize, secondary throughout)
2. Fix PRAXES timescale in Doc 11's hierarchy diagram
3. Clarify OPERATA as spanning multiple timescales
4. Clarify MEMORATA as "compression results stored as discrete entries"
5. Add failure-mode → metric mapping table (cross-reference Docs 10/12)
6. Add CIY definition to Doc 10 or add reference
7. Add "action fluency" to Doc 10 vocabulary
8. Flag PULSUS rates as event-count-based, not clock-based
9. Cite source for cost distribution numbers or remove
10. Reduce OODA terminology in Doc 11

**Flag for Joseph** (design decisions, not documentation fixes):
1. The bootstrap problem: how to ground epistemic estimates measurably
2. Sovereignty in a designed system: real tension, needs ethical discussion
3. The sycophancy trajectory: developmental-vs-pathological diagnostic
4. Whether "estimated in language" needs more operational specificity

**Accept as current limitations** (real gaps, not fixable yet):
1. INTERPRES specification
2. INSTRUMENTA/AUXILIA integration in the loop
3. Confabulation test protocol
4. AXIOMATA content at different developmental stages
5. Forgetting mechanism in the loop (needs capacity management design)
