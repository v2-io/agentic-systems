# Batch-3 quiz verification

Checked the questions/answers against the six source files directly (`def-model-sufficiency`, `def-model-class-fitness`, `the-cycle-in-motion-intro`, `form-event-driven-dynamics`, `der-recursive-update`, and the appendix `deriv-recursive-update`), including their Working Notes / "Incidental audit gold" sections. Answered cold before reading the provided key, then compared. Also skimmed both prior batch reports first, per the brief.

## (a) Correctness against segment text — one real finding, otherwise clean

**b03-1.2 answer states a discriminator the segment itself flags as unresolved.** The question asks for "the operational rule: which observable pattern tells an agent it is facing a class ceiling rather than (a) still-incomplete learning or (b) an irreducibly noisy world?" The answer supplies a clean three-way split: *"Still-learning ⇒ residuals still improving; noisy-world ⇒ white residuals on the floor; class ceiling ⇒ structured residuals after convergence."*

`def-model-class-fitness`'s Discussion only establishes the *ceiling-vs-noisy-world* half: "persistent systematic mismatch despite adequate learning... is the observable signature — structured residuals, not merely large ones... What distinguishes a class ceiling from a noisy channel is residual structure." It never states what distinguishes *still-learning* from either of the other two cases (nothing about "residuals still improving" as a discriminant is asserted anywhere in the Formal Expression, Epistemic Status, or Discussion). Tellingly, the segment's own Working Notes §4 lists this exact three-way disambiguation as an **open reader question, not a resolved one**: *"How does the agent tell 'low $\mathcal F$' from 'high $\rho$'?... persistent mismatch can mean either an inadequate model class or a highly volatile environment... If both look the same to the agent, how does it know...? Readers want the disentanglement" — all pointing forward to `#result-structural-adaptation-necessity` (Ch.4, out of batch-3 scope) as where a sharp diagnostic should appear.* A second WN item explicitly flags the still-learning/class-ceiling/noise triad as unreliable and risky if guessed at ("A wrong call risks catastrophic thrashing").

So the answer key confidently resolves, in-scope, a distinction the segment self-reports as *not yet resolved in this segment* and defers to later material. This is the same shape as the Gate-2 concern named in the project's own discipline (`feedback_gate2_epistemic_tribunal.md`): a plausible-sounding elaboration that reads as though it follows from the formalism but doesn't actually derive from it. Recommend either (1) narrowing the question to the two-way discriminator the segment actually derives (structured vs. white residuals ⇒ ceiling vs. noise) and dropping the "still-incomplete learning" branch, since that branch isn't answerable from these six segments, or (2) if keeping the three-way framing, marking the still-learning claim explicitly as "not stated in the segment — plausible inference, unresolved per its own Working Notes, deferred to Ch.4."

Everything else checked correctly: 1.1, 1.3–1.6, 2.1–2.7, 3.1, 3.3–3.6 all match segment text (body or explicitly-external-framed WN) with no factual errors found. Worth flagging as a small aside: 2.7's parenthetical "(The segment type for the gain is `empirical`, itself a signal...)" pulls a fact from `emp-update-gain.md`'s frontmatter — a file *not* among the six batch-3 sources. I checked it directly and the claim is accurate (`type: empirical`), so it's not wrong, but it's a minor scope reach beyond the assigned reading list; worth a note if strict in-batch self-containment matters to you.

## (b) WN-bonus tagging discipline — real improvement, one residual miss

This is the thing you specifically asked about, so here's the direct accounting:

**Correctly tagged (policy working):**
- **A b03-3.3** — the external-memory structural point is explicitly marked `(WN bonus — Gemini's reach)`. Exactly the batch-2 model instance generalized correctly.
- **A b03-3.6** — Kuhn-analogy content is WN-sourced (`def-model-class-fitness` WN §2 "Structural inadequacy as a formalized Kuhnian paradigm shift," attributed there to Gemini/AUDIT-WORKING-829314), but the *question itself* frames it as "a prior auditor proposed" and asks you to steelman + name a promotion check — so the WN-provenance is already surfaced at the question level, and no separate answer-tag is needed. Same handling batch-1's 3.2 used successfully.

**Not tagged, though WN-sourced (the batch-2 gap recurs once):**
- **A b03-3.2** — the closing clause *"The real empirical work relocates to determining what $M_t$ actually contains for a given agent and whether it retains enough"* is close paraphrase of `deriv-recursive-update`'s Working Notes "physicist's system-boundary trick" entry: *"the real empirical work is figuring out what $M_t$ actually contains for a given agent, not proving the equation."* The core of the answer (Attack 3's verdict — "the real content is the analytical commitment... commits to Markovian analysis, which then makes #def-model-sufficiency the right quality metric") **is** body content (it's in the main Attacks section, not Working Notes), so most of the answer is properly grounded — but the specific "relocates to... what $M_t$ actually contains" framing that closes the answer is WN phrasing presented as if it were part of the certified Discussion, unflagged.

Net: 1-for-1 correctly tagged, 1-for-1 correctly handled via question-level framing, 1 miss — a real improvement over batch-2's ratio (1 correct / 5 missed), but not yet fully closed. The miss is smaller in stakes than batch-2's (most of 3.2's answer is body-grounded; only the closing clause leaks WN), which may itself be informative: the discipline seems to be holding better for *whole-answer* WN content (3.3) than for a WN-sourced *phrase grafted onto an otherwise-grounded answer* (3.2) — worth watching for in a batch 4, since the latter is the harder case to self-catch.

## (c) Sequential-comprehension design

No forward-knowledge leaks. The one place a forward reference appears mid-answer (2.7's `emp-update-gain` type-check, discussed in (a)) reaches slightly outside the assigned six files but not into their un-derived content — it's a metadata check, not a use of a later derivation. All named forward pointers (`#result-structural-adaptation-necessity`, `#form-consolidation-dynamics`, `#schema-strategy-persistence`, `#def-value-object`, `#der-causal-hierarchy-requirement`) are named as forward pointers within the six segments themselves, and questions ask what the segment says is coming, consistent with batches 1–2.

## (d) Discriminating power — self-experiment (answered cold first)

- **1.1** — strong trap; the false "any adaptive agent" framing is exactly the flattening the segment works hardest against, and the C1/C2-eliminative vs. C3-definitional split is easy to blur without a careful read of the Epistemic Status table.
- **1.3** — clean trap; "sufficiency = correctness" is the natural wrong intuition and the answer key's distinction is crisp.
- **2.4** — good trap; the "external log violates the result" framing sounds right on a skim and requires having actually walked Attack 7's verdict to resolve correctly.
- **2.5** — the strongest discriminator in the batch; catching the MI-is-expected vs. surprise-is-realized mismatch requires noticing a subtlety the segment's own Working Notes call "the most substantively repeated reader-confusion" — a summary-fed reader has essentially no chance here.
- **1.2** — as discussed in (a), this one is currently mis-calibrated rather than a clean discriminator: it's testing confident synthesis of an admittedly-open question, not comprehension of a settled claim.
- **3.2, 3.6** — good implications questions; both require holding the C3-circularity argument's *shape* (definitional-not-eliminative) rather than just its conclusion, which a summary would likely flatten into "the update must be Markovian."

No question struck me as too easy / summary-passable, aside from the calibration issue in 1.2.

## Beyond the quiz — one small theory-framing observation

Nothing wrong in the underlying segments. One texture note carried over from `deriv-recursive-update`'s own WN "Off-ramp (NOT gold)" item: the `exact` (appendix) vs. what used to read as `conditional` (body) status tension is *already resolved* in the current files — `der-recursive-update.md`'s frontmatter now reads `status: exact` and its own Epistemic Status body opens "*Exact, with a partly definitional character*," matching the appendix. So that particular cross-substrate disagreement the WN preserved as "signal" appears to have been landed since the gold-lift; nothing for this batch to flag, just confirming it's not a live discrepancy a future auditor needs to re-raise.

Happy to stay on the line for follow-ups, including taking a pass at whether b03-1.2 is worth revising now versus batching it with other quiz fixes.
