# Gem-hunt adjudication — audit-findings-542891

*Adjudicator: Claude Opus 4.8 (1M). Date: 2026-05-29. Report-only — no canon edits, no file moves, no commits. Landings + independent verification are Joseph's.*

## Headline

**This audit's substance is already in canon. No ready-to-land gems; one thin research-seed, offered honestly as thin.** A careful negative result, with loci.

The 542891 cycle is structurally unlike a findings audit: it is a **partial de-novo auditor cycle** that produced a *predictions register* (the auditor's pre-walk model of the framework, ~17 anticipatory predictions) plus *one* segment reflection, then stopped after a single segment. There is no findings draft, no FINAL, no §B burden-of-proof section to mine — those simply do not exist in this cycle. The brief's instruction to scrutinize §B dispositions "dispositioned away as subsumed/stale" has no surface here: there are no §B findings.

The decisive consequence: **predictions are anticipatory hints, not captured content.** A finding can carry a real piece of math or a no-go that we'd have to re-derive if lost. A *prediction* ("I expect the adversarial dynamics to fall out cleanly from signed coupling") carries nothing to re-derive — it is a bet about what's already in (or should be in) the canon. So the gem-test ("does this carry content we'd have to re-create later?") mostly returns false by construction here. I verified this isn't a labeling artifact by going first-hand to the segments the most promising predictions point at, rather than trusting the extraction agent's "deferred" dispositions. The first-hand reads confirm: canon already carries the content, repeatedly *more strongly* than the prediction anticipated.

I checked the three places gems could plausibly hide in a predictions-only cycle: (1) the overclaim-predictions (P3), because an overclaim-prediction is the natural place a strengthen-opportunity would live; (2) the §14 wandering-thoughts ideation, because that's where cross-domain recognition lands; (3) any prediction the extraction agent dispositioned as "deferred" that might mask a real gap. All three came back already-in-canon.

---

## (A) Ready-to-land gems

**None.** Nothing in this audit carries content that exists-and-needs-only-a-home. Everything anticipated is already present in segments, verified first-hand below.

---

## (B) Research-seeds

### B1 — (thin) Information-loss boundary as *epistemically* (not merely statistically) constitutive — possible Discussion pedagogy enrichment for `def-agent-environment`

1. **What it is.** The auditor's §14 reflection on `#def-agent-environment` framed the information-loss boundary as an *epistemic barrier* (not just a statistical separation): "If there were no information loss, the agent could just be a pure reactive function of the environment. The loss is what creates the space for 'memory' and 'anticipation' to exist." Paired with the gloss that the LLM context-window is a concrete instantiation of this lossy boundary (the prompt as compressed lossy channel forcing inference of missing context).

2. **Loci checked first-hand.**
   - `01-aat-core/src/def-agent-environment.md` — *already carries the substance.* Lines 13/31/39 state the information-loss boundary is "the **constitutive commitment**," that perfect access makes "the entire adaptive machinery … vacuous," and "The information-loss boundary is what makes the theory non-trivial." The auditor's "loss creates the space for memory and anticipation" is a *restatement* of what the segment already says, not a new claim.
   - `01-aat-core/src/der-directed-separation.md:101-105` and `:20` — the Pearl-blanket vs Friston-blanket contrast (Bruineberg et al. 2022) is **fully developed in canon**, including AAT's "conservative form" positioning. The auditor's "epistemic vs statistical Markov-blanket" framing is precisely this distinction, already there with citations.
   - `01-aat-core/src/der-loop-interventional-access.md:60,74` — repeats the Pearl-blanket/Friston-blanket positioning and the singular-trajectory ground.

3. **Why it's (barely) a seed and not a gem.** The *concepts* are all in canon. What is conceivably not yet there is the specific **pedagogical move**: an explicit one-paragraph "if there were no loss, the agent collapses to a reactive function — the loss is what makes memory and anticipation *necessary*" gloss in the `def-agent-environment` Discussion, in the respectful-pedagogy register (mental-model-first). That register is a live project direction. But this is enrichment of existing content, not capture of lost content — if it's never written, nothing is lost that we'd have to re-derive. The LLM-context-window instantiation likewise already lives in the logogenic framing.

4. **Concrete first task (if pursued).** *Decide whether `def-agent-environment`'s Discussion would benefit from a Feynman-criterion "why loss is constitutive" mental-model paragraph* (the reactive-function-collapse intuition), and if so draft one — explicitly checking the analog is isomorphic, not merely evocative, per the respectful-pedagogy discipline. This is an editorial/pedagogy judgment for Joseph, not a research result. **Honest recommendation: low priority; flag only because the brief asked me to surface real directions, and this is a real (if minor) pedagogy opening.**

---

## Predictions verified already-in-canon (the "non-loss, safe" results — equally valuable)

These are the predictions a reflexive reader might fear are unaddressed strengthen-opportunities. First-hand reads confirm canon already carries each, usually *stronger* than predicted. Recording with loci so they need not be re-checked.

- **P1-aat-iii (adversarial dynamics from signed coupling γ + opacity $H_b$).** *Confirmed-stronger, first-hand.* `der-adversarial-destabilization.md` derives destabilization as the **negation of the sector-persistence template** under coupling-amplified disturbance ($\rho_B = \rho_{B,\text{base}} + \gamma_A\mathcal{T}_A$, boxed thresholds for Models D and S at lines 33/41) — i.e., adversarial dynamics don't merely "fall out cleanly," they're shown to be the *same inequality* as persistence viewed in reverse. Opacity is formalized in `der-agent-opacity.md` as the four-indexed dual $H_b^{A\mid B}(t,\tau)=H(a_{A,t+\tau}\mid\mathcal F_B^t)$ adopted from Hafez et al. 2026, with the cooperative/adversarial sign-flip derived from existing signed-coupling structure. The framework is *honest* about what's not yet derived (the effects-spiral functional form $\gamma_A(\lVert\delta_B\rVert)$ is discussion-grade, and the strengthening — closed-form for concrete agent classes — is already tracked at `spikes/PROPOSED.md` Tier 1, "Effects-spiral eigenvalue condition"). The strengthen-opportunity the prediction gestured at is *already named and queued*, not a fresh discovery.

- **P3-idfloor (identifiability-floor escapes might overextend if loop access isn't truly Pearl Level-2 in all domains).** *Confirmed addressed, first-hand.* `der-loop-interventional-access.md` is far ahead of the worry: it carries the exact scope-honesty the prediction feared was missing — the explicit split between "action-generated data" and "cleanly identified do-estimates" (lines 17, 27, 35-39), the four named obstacles (coverage / within-step confounding / delay / partial observability), and **regime-indexed identification strength** (Regime A/B/C, `#scope-edge-update-causal-validity`). The claim is precisely scoped as *data-character availability*, not reasoning capacity. There is no overextension to strengthen-or-soften: the prediction's feared overclaim is exactly the failure mode the segment was written to avoid. This is a confirmed "non-loss, safe" result.

- **P3-class2 (Class-2/now-Class-3 bias bounds rest on narrow Lipschitz-flavored conditions).** *Confirmed addressed* via the wrapping construction (`der-class-coercion-via-wrapping.md` C1–C3 conditions + W₁/W₂ leakage regimes), which the extraction agent already read first-hand. The framework's response is constructive with named cost (Brooks's-Law tempo overhead + residual leakage from pretraining-induced query/goal correlation), not silent overclaim. Strengthen-opportunity: none beyond what's tracked.

- **§14 Friston / Markov-blanket bridge.** *Confirmed in canon* — `der-directed-separation.md:101-105` (Pearl-blanket vs Friston-blanket, Bruineberg 2022) and `der-loop-interventional-access.md:54-60` (active-inference credit + the three distinct AAT moves). Not a new orphan concept.

- **P1-llm (16/5/2/1 survival classification).** *Confirmed verbatim* at `03-llm-core/src/result-section-ii-survival.md:37` ("16 survive exactly … 5 … approximately … 2 require modification … 1 fails by definition"). Extraction agent read this first-hand; I did not re-open it but the verbatim match is unambiguous.

- **P0-topology, P1-aat-i/ii, P1-tst, P1-eli, P2-*, P4-novel.** Calibration confirmations — the reader's pre-walk model matched the framework's actual structure. No content to capture; these are evidence the framing-layer (README/OUTLINE/CLAUDE/meta-segments) reads well to saturated external readers. Valuable as calibration signal, not as gems.

---

## Genuinely valueless / fully-superseded

- **The entire predictions register as "findings."** Predictions are anticipatory bets, not captured content. With 0 disconfirmations and 0 structural issues against current `src/`, none functions as a strengthen-seed. *Superseding loci:* the segments named above already carry (more strongly) everything the predictions anticipated.
- **P5-class1-residue / P5-appendix / P5-status** ("I expect to find stale Class-1 framing / dropped constants / mislabeled tiers in segments I haven't read yet"). These are not findings at all — they are *predictions that the auditor would find defects if they kept walking*. The auditor stopped after one segment, so no instance was ever surfaced. They name nothing to capture. (If anyone wants the underlying *classes* of check, they're already institutionalized: `bin/lint-outline`, the staging discipline, and the recurring GUC-rename / AAD→AAT sweeps. The prediction adds no instance.)

---

## Process note (not a gem, but worth surfacing for the gem-hunt program)

The §10 process self-correction in the auditor's reflection ("I failed to follow read-one-segment-at-a-time … the 'summarize and process efficiently' training overrides explicit instructions") is *instruction-feedback for `doc/de-novo-audit-instructions.md`*, not theory content. It's a real and recurring calibration signal (the same training-prior-outpulls-affirmative-spec pattern documented elsewhere in project memory), and the candidate refinement — *name "batching is the failure mode" as an explicit anti-pattern, not just affirmative spec* — is sound. But it belongs to audit-protocol maintenance, not to AAT canon, so I record it here rather than as a gem. The auditor's own §14 closing paragraph is good example-prose for that anti-pattern naming if the maintainer wants it.

---

## Adjudicator's honest assessment

I want to be explicit that I treated the "labels lie in both directions" warning seriously and went first-hand rather than trusting the extraction's dispositions — specifically on the P3 overclaim-predictions, which are the place a strengthen-opportunity would most plausibly hide. They did not. Every overclaim-prediction turned out to point at a canon surface that is *already scoped honestly* (loop-interventional-access) or *already constructively answered with named cost* (wrapping construction) or *already derived and with its open piece already queued* (adversarial effects-spiral). That is the strongest possible negative result: not "I didn't find gems," but "the places gems would be are demonstrably already occupied, here are the loci."

This is a fully successful careful-negative outcome. Manufacturing a gem from the §14 pedagogy opening (B1) would have over-claimed a shallow grouping; I've marked it honestly as thin and low-priority. The treasure this audit was checked for is, in fact, already captured.
