# Audit of `audits/fix-adaptive-reserve.md` — the adaptive reserve and the standpoint question

**Date:** 2026-08-12. **Auditor:** second agent, commissioned to verify the repair plan independently. **Scope:** every quoted location, the central structural claim, the git history, the repair options, and the over/under-claim balance.

**Constraints observed.** No canon edited — no segment body, no OUTLINE row, no terminology entry, no `bin/term` invocation. No `AUDIT-WORKING-*` directory processed, moved, or reorganised (read and grepped only, which the gate permits and wants). `01-aat-core/src/deriv-adaptive-gain-dynamics.md` **not opened and not grepped directly**; §8 below assesses the plan's handling of that gate without resolving it. One unavoidable leak, identical to the plan's own, disclosed in §9.

---

## 0. Bottom line

**The plan is substantially sound, and unusually well-cited.** I opened and checked 53 distinct citations. **Fifty-two hold** — most of them verbatim, including every load-bearing one. One sub-claim is false, and it is the kind that would have been expensive: the plan's reason for doubting a substrate attribution is a sampling artifact, and acting on it would have propagated a wrong "fix" across 49 canon sites.

The central finding — that Position B (the agent reads $\Delta\rho^\ast$ per step from its own state) is asserted in exactly three places, is load-bearing for Corollary 2's constructive boundary, and is nowhere derived — **holds**. I tried to break it and could not. The history claims **hold**, to the second. The repair options are sound and honestly costed.

**Three things change the plan materially, and all three make the repair *cheaper and better-founded* than the plan believes:**

1. **The standpoint discipline the plan says is missing is already landed in canon body — for the sibling quantity.** `#def-model-class-fitness` states that $\mathcal{F}(\mathcal{M})$ is *not* agent-computable, names why, and supplies the agent-available proxy. That is Option A's marking, Option D's (U)-axis move, and Option C's substitute-estimator, already worked, one dependency-hop from the reserve, on a quantity that *determines* $R$. §2.2. This is a **missed repair option** — the cheapest and strongest on the honesty/cost frontier — and it re-diagnoses the defect from "missing discipline" to "discipline exists, never applied to the persistence parameters."
2. **§6.1 Obstacle 1's self-model absence is wrong.** The self-model concept is treated in canon in at least four places, one of them an entire segment carrying a *derived no-go about behavioral self-knowledge* with an external theorem — `03-llm-core/src/hyp-behavioral-self-knowledge-insufficiency.md`. §2.3. An Option-C spike briefed on §6.1 as written would not know the single most relevant prior result in the corpus exists.
3. **§3.6's provenance defect reaches the right conclusion by a wrong route.** §2.1.

Two findings are overclaims (§3.1, §3.2); the rest are small. Nothing I found requires the blocked-read gate to lift, and I judge the gate call correct.

---

## 1. Verification ledger — per-claim verdicts

Grouped by plan section. **HOLDS** = quoted text and line reference both correct at the cited location, and the claim it supports follows. Deviations noted inline.

### §3.1 — Position A (third-person capacity)

| Cited location | Verdict |
|---|---|
| `_obs/old-tf-appendix-a-lyapunov.md:141–156` (Prop A.2 origin, statement + interpretation) | **HOLDS.** Verbatim. Statement at :143–148, interpretation at :152–155. |
| `01-aat-core/src/deriv-sector-condition.md:107–122` ("word-for-word identical") | **HOLDS, near-exactly.** The Prop A.2 block is identical in prose. Two immaterial differences: the live version inserts a blank line between the `*[Derived (adaptive-reserve)]*` tag and the display equation, and drops the archaeology's `### Domain Instances` heading. "Word-for-word identical" is fair for the claim it supports. |
| `result-persistence-condition.md:115` | **HOLDS.** Verbatim. And the absence the plan relies on is real: the paragraph names no holder of the quantity. |
| `result-sector-persistence-template.md:47` ("the system," not "the agent") | **HOLDS.** Verbatim, and the wording contrast is exactly as claimed. |
| Template "instantiated across seven segments" | **HOLDS with one correction.** `:57` reads "The template is invoked across seven segments." But the plan's gloss — "seven segments on state variables that are *not* an agent's beliefs" — is wrong for one row: `:61` instantiates on $\delta_t$, "epistemic mismatch," which *is* the agent's beliefs. Six of seven. The argument it supports (a reserve on a composite's state variable cannot be one in-scope agent's local read) survives intact. |
| `deriv-discrete-sector-condition.md:103–111` ("the agent can absorb an additional per-step disturbance of") | **HOLDS.** Verbatim at :105. |
| `der-multi-timescale-stability.md:35` (S4 standing reserve hypothesis) | **HOLDS.** Verbatim, including the parenthetical. |
| `der-adversarial-destabilization.md:35, 51` | **HOLDS.** Both verbatim. |
| `README.md:103` / `README-auditor.md:124` | **HOLDS.** Identical text at both, verbatim. |
| "`#der-agent-opacity`'s targeting arg-max … currently has none" | **HOLDS.** The five-factor arg-max at `der-agent-opacity.md:91` is credence leverage $\times$ plan sensitivity $\times$ edge identifiability $\times$ observability $\times$ targeting fidelity. No reserve term. |

### §3.2 — Position B (the three sites)

| Claim | Verdict |
|---|---|
| `deriv-self-actuation-grounding.md:70` Corollary 2(ii) | **HOLDS.** Verbatim. |
| Same segment `:25` summary restatement | **HOLDS.** Verbatim. |
| `der-orient-cascade` steps 1–2, quoted verbatim | **HOLDS.** Steps span :33–34 and :36–37 (the plan reflows two hard line breaks; no words altered). And the substantive point holds literally: neither step names $\alpha$, $R$, or $\rho$. **But see §3.4 below** — the plan states the citation's emptiness more absolutely than its own §8 permits. |
| "The claim hardened at landing" — spike wording at `spike-wf-class-scoping.md:530–533` | **HOLDS.** Verbatim; the block actually spans :530–534. The hedge *"exactly the kind of finite local quantity the in-scope agent already maintains"* is there as quoted. |
| Commit timing: spike `c63d86f`, segment `e976b94`, "18 minutes later" | **HOLDS, to the second.** `c63d86f` = 2026-05-17 23:37:48 −0600; `e976b94` = 2026-05-17 23:55:57 −0600. 18 min 09 s. `e976b94` added `deriv-self-actuation-grounding.md` (+132 lines) as a new file. |
| "The landed segment reads *is* a finite local read" and "nothing in the interval added evidence" | **HOLDS.** The text at `e976b94` is byte-identical to the current `:70`, so the hardening happened *at* landing and has never been revisited. One calibration note: the spike's parenthetical already asserted unhedged that *"the persistence margin $\Delta\rho^\ast=\alpha R-\rho$ is a finite read, not a Bellman solve."* The delta is narrower than the plan's framing implies — it is the transfer of *"the in-scope agent already maintains"* from "the persistence diagnostic" onto "the reserve," plus the deletion of *"exactly the kind of."* That is still a real hardening, and the plan's diagnosis of *which* clause is unsupported is correct. |
| `CURRENT-VOL1.md:10850` carries the landed wording verbatim | **HOLDS.** Verbatim. |
| `terminology/entries/adaptive-reserve.md:19–20` text; `primary_source` / `first_asf_mention` both `result-persistence-condition.md` | **HOLDS.** Verbatim; frontmatter as stated. |
| Provenance: body text incl. "agents track the reserve" landed in `868f72a` (2026-05-08), a LEXICON-generation commit | **HOLDS — and I can strengthen it.** `868f72a` = Fri May 8 21:52:52 2026, message as quoted, and it *added* the file (+26 lines) with the sentence already present. `git log -S "track the reserve" --all` returns **exactly one commit** — the phrase has never appeared anywhere else in repository history. Further: `git show 868f72a~1:LEXICON.md` shows the pre-migration hand-written row was **`\| **Adaptive reserve** ($\Delta\rho^\ast$) \| Shock tolerance; how much disturbance increase before persistence fails \|`** — which is the `brief:` field. So the body paragraph, *including the tracking clause*, was **newly authored by the migrating sub-agent**, not migrated from anything. The plan's characterization ("an incidental gloss during a terminology migration") is if anything understated. |
| Carried unchanged through `4f1f65d` / `9745397` / `67064c0` (2026-07-14 breadcrumb-lint sweep) | **HOLDS.** Content diffed at each; only `01-aad-core`→`01-aat-core`, a `see_also` rename, and line-unwrapping. |
| Decision record quote: *"C1 clean canonicalize batch, naming-rename-plan.md"* | **HOLDS.** Verbatim; the whole record body is that one line. `action: canonicalize`, `decider: joseph`, `outcome: committed`, 20260510T195801Z. |
| Not in `LEXICON.md`, not in `CURRENT-VOL1.md` | **HOLDS.** `grep -c` returns 0 in both. `LEXICON.md:82` carries only the brief, and `bin/term`'s render confirms the table is frontmatter-driven. |
| `disc-continuity-stance.md:50` (B3) and `:46` (the L1/L2/L3 grain) | **HOLDS.** Both verbatim. `:46` is in Epistemic Status rather than Discussion — immaterial. |
| "the corpus has language for who can *move* the reserve and none for who can *see* it" | **DOES NOT HOLD as a claim about the corpus.** See §2.2. It holds about the *persistence parameters*; it is false about the corpus, which has exactly that language for $\mathcal{F}(\mathcal{M})$. |

### §3.3 / §3.4 / §3.5 — Positions C, D, E

| Cited location | Verdict |
|---|---|
| `detail-operationalization.md:18` (framing), `:32` ($R$ row), `:99` (step 2), `:109` ($\hat R$ estimator), `:135` (reserve estimator), `:194` (bypass $\rho$) | **ALL SIX HOLD.** All verbatim, all at the stated lines. The inversion the plan reports — that this segment is evidence *against* the agent standpoint, not for it — is correct on the text: each of the three inputs requires access outside the agent's on-policy stream. This is the plan's most consequential single move and it is well-founded. (One transcription nit: the plan adds bold to three of these quotes that is not in the source — see §3.6.) |
| `empirica/track-b-nonlinear/sim2_adversarial_coupling.py:609` | **HOLDS.** `reserve_B = alpha_B * R_B - rho_B_base`, computed from `base_params` ground truth. |
| `example-kalman.md:127–129` | **HOLDS.** Verbatim. |
| `obs-growth-vs-drift.md:26`, `:34`, `:60–67` | **ALL HOLD.** Verbatim. The external-monitor register is unambiguous as claimed. |
| `obs-developmental-trajectory.md:21` | **HOLDS.** Verbatim. |
| `deriv-gain-sector.md:293` (Working Notes) and `:303` (audit gold, Claude/584721) | **BOTH HOLD.** Verbatim. |

### §3.6 — the open question and its provenance

| Claim | Verdict |
|---|---|
| `result-sector-condition-stability.md:87` gold line, under `#### 4. Readers often ask / wonder` | **HOLDS.** Verbatim, section placement confirmed. |
| `AUDIT-WORKING-193847/.integrated/21-…:27` | **HOLDS.** Verbatim. |
| `AUDIT-WORKING-829314/.integrated/22-…:17` | **HOLDS.** Verbatim (modulo the disclosed `\ast` normalization). |
| `AUDIT-WORKING-849201/.integrated/25-…:24–25` asks about `#der-gain-sector-bridge` instead | **HOLDS.** Verbatim. |
| The question is not in 849201 | **HOLDS — and I upgrade it from "not found" to "not there."** I searched the entire dir (top level *and* `.integrated/`) for `from the inside`, `its own reserve`, `measure its own`, `know its own`, and bare `reserve`. Two hits total, neither the question (`04-scope-adaptive-system.md:4` uses "reserved" in the ordinary sense; `66-der-interaction-channel-classification.md:20` repeats the II-a/II-b conflation warning). The plan's self-imposed caveat can be discharged: the citation is unsupported. |
| "849201 is attributed to Gemini everywhere else I checked" | **DOES NOT HOLD.** See §2.1. |
| `der-interaction-channel-classification.md:195` all-Gemini attribution | **HOLDS.** Verbatim. |
| `doc/de-novo-audit-instructions.md:680` (two tracks) and `:684` (six gold categories) | **BOTH HOLD.** Verbatim. The routing analysis — that a prompt-#8 curiosity item correctly lands in "readers-often-ask," which is off the findings-adjudication path — is right, and `:684` confirms the six-category sort. |
| No routed finding on reserve measurability anywhere | **HOLDS.** I re-ran it wider than the plan did — `TODO.md`, `PROPOSALS.md`, `FINDINGS.md`, `CHANGELOG.md`, `LOG.md`, `audits/STATUS.md`, every `audit-findings-*.md`, every `pending-findings-*.md`, `spikes/PROPOSED*.md`, `spikes/INDEX.md`. Nothing. |
| `02-tst-core` / `03-llm-core` carry nothing beyond `old-tst-via-tft-simulation-proposals.md:13` | **HOLDS.** Confirmed by independent corpus-wide sweep. |

### §6 / §7 — obstacles, precedent, options

| Claim | Verdict |
|---|---|
| `form-complete-agent-state.md:22` ($X_t = (M_t, G_t)$ with the two glosses) | **HOLDS.** Verbatim. |
| `form-sector-condition.md:32` (existential) and `:56` ("assumed as a per-system empirical claim") | **BOTH HOLD.** Verbatim. |
| `result-persistence-condition.md:111` ($R$ a domain parameter, not a theory output) | **HOLDS.** Verbatim. |
| `def-observation-function.md:33` and `:15` (opacity constitutive) | **BOTH HOLD.** Verbatim. |
| §6.1 Obstacle 1's self-model grep over four foundational segments returning nothing | **The grep HOLDS; the inference does not.** See §2.3. |
| `#disc-identifiability-floor` five-element shape | **HOLDS.** `:16` states it; the elements are as the plan renders them. Instance 2's rank-1 Fisher matrix confirmed at `:76`. |
| "Do not reach for Fano first" — two prior convergent negative verdicts | **HOLDS, well-sourced.** `spike-4th-identifiability-floor-instance-2026-05-20.md` §3 returns Outcome C on Fano ("*This is the textbook bound on prediction given entropy, not a structural no-go*"); `spike-identifiability-floor-instance4-resolution-2026-05-18.md` records "*Fano specifically tested and found inadequate … Fano degenerates to a vacuous bound at $I = 0$*." |
| `spike-escape-standpoint-axis-2026-07-29.md` §8 self-silencing family, quoted | **HOLDS.** Verbatim. |
| Same spike §10: architecturally-known deficit is where the observability argument fails | **HOLDS.** `:163` — "*It **fails** where the deficit is architecturally known — an agent that knows by construction it has no sensor at $v$ can target it.*" The plan's Option D bullet 2 uses this correctly. |
| Same spike §3 / `spikes/PROPOSED.md`: a Tier-1 adversarial spike is queued against two-routes-exhausts | **HOLDS.** `PROPOSED.md:33`, dated 2026-05-28, and cross-referenced at the spike's `:61`. |
| §6.3 precedent: `emp-update-gain.md:50` quoted in full | **HOLDS.** Verbatim, including the pointer to the blocked segment as carrying the proof. |
| `audits/audit-findings-849201.md:66` strengthen-first posture verification, quoted | **HOLDS.** Verbatim. |
| "three architecturally-independent cold reads" | **HOLDS.** `:70` states exactly that; the three are enumerated at `:72–74`. |
| `emp-update-gain.md:93` "Be surprised by your surprises" | **HOLDS.** Verbatim. |
| Option D's reading of Lemma 2's bar | **HOLDS.** `deriv-self-actuation-grounding.md:53` — "*The C3 verdict is a global Bellman optimum, generally intractable … evaluating it is not a finite per-step operation.*" So "the bar to clear is 'not a Bellman solve,' not 'exactly computable'" is a correct reading, and Option D is well-founded. |
| Reverse strengthening: `def-mood.md:44` quoted | **HOLDS.** Verbatim. `#def-mood` did postdate Corollary 2, and `result-persistence-condition.md:202` carries the forward pointer as described. **But see §3.5** for a hazard the plan does not name. |
| §5's severity assessment (Result G′ rests on Lemmas 1–2, untouched by the reserve; Corollary 1 requires *some* object meeting (i)–(iii)) | **HOLDS.** Confirmed against the Formal Expression at `:41–55` and Corollary 1 at `:65`. This is the plan's calibration high point — it declines to inflate the finding into a collapse. |
| §8's three-step argument that the blocked file is load-bearing: `result-persistence-condition.md:79` ($\alpha = \eta^\ast c_{\min}$), `deriv-discrete-sector-condition.md:113` (fluid limit), `emp-update-gain.md:50` (names the segment as carrying the proof) | **ALL THREE HOLD.** Verbatim. The argument is sound and is built only from files the plan read. |

### §9 — secondary findings

| Claim | Verdict |
|---|---|
| §9.1 units gold at `result-sector-condition-stability.md:88` | **HOLDS.** Verbatim. |
| §9.1 "the conflation is committed in the wild, twice" — `quiz-34.answers.md:33`, `quiz-40.answers.md:63` | **Quotes HOLD verbatim; the conflation charge does not.** See §3.1. |
| §9.2 `CURRENT-VOL1.md:1761` "if and only if" vs current `result-sector-condition-stability.md:17` | **HOLDS.** Both verbatim; the snapshot does predate the Lemma-A.1N correction. **Incomplete** — see §3.7. |
| §9.3 stale line ref: `audit-findings-849201.md:66` cites `emp-update-gain.md:44`; it is now `:50` | **HOLDS.** Both confirmed. |
| §9.4 F5 disposition at `audit-findings-193847.md:145` | **Quote HOLDS.** Verbatim. `04-eli-core/src/norm-adaptive-reserve-as-ethical-floor.md` does not exist (`ls` confirms; the only `norm-` segment there is `norm-interiority-default.md`). |
| §9.4 F6 disposition at `:151` | **Quote is HOLDS-but-truncated, and the conclusion does not hold.** See §3.2. |

---

## 2. Findings that change the plan

Ordered by what it would cost to act on the plan without them.

### 2.1 §3.6(ii) is a sampling artifact — and acting on it would corrupt 49 canon sites

The plan writes:

> (ii) The gold attributes the third instance to "Claude, AUDIT-WORKING-849201," but 849201 is attributed to Gemini everywhere else I checked … The practical consequence either way: the convergence-strength of the open question is currently *overstated in canon*, and the honest version — one substrate, twice, plus an unlocated third — is still enough to matter.

Repo-wide, across the four component `src/` trees, the attribution runs the **other** way:

```
  49 (Claude, AUDIT-WORKING-849201
  25 (Gemini, AUDIT-WORKING-849201
```

The two sites the plan happened to check (`der-interaction-channel-classification.md:195`, `def-observation-function.md:63`) are both in the 25. The dominant canon attribution is Claude, and the audit's own extraction record supports it: `audits/audit-findings-849201.md:74` describes the *other* convergent cycle as "**extracted-gemini-2026-04-26-27** — Gemini, separate reading discipline, **separate substrate**," which reads as excluding Gemini for 849201. The dir's own front-matter (`:2`) names no substrate at all — only `extraction_agent: Claude Opus 4.7`, which is the *extractor*, not the auditor. Compare 193847 (`:2` "de-novo, **Gemini** Parts III/IV-focused auditor") and 829314 (`:2` "de-novo, **Gemini** generalist/reasoning model"), both of which *do* name it.

**Why this matters more than a footnote.** The plan surfaces the substrate mismatch as a defect *"worth correcting while the segment is open."* A repairer trusting §3.6(ii) would conclude the 849201-is-Claude attributions are the error, and 49 canon sites say Claude. The actual state is that **849201's substrate is inconsistently attributed in canon and is not verifiable from canon** — and there is a known reason: `emp-update-gain.md:88` states outright that "*Substrate attribution inferred from voice where not explicit.*" This corpus has a standing attribution-reliability problem, independently evidenced by `spike-escape-standpoint-axis-2026-07-29.md` §11 ("*two of my attributions were false*").

**The plan's bottom line survives, by the other route.** The gold line's "three substrates" is still wrong, because the third citation is unsupported *at all* — and I have now searched 849201 exhaustively (§1) rather than partially, so that leg is stronger than the plan could claim. The honest replacement for the gold line is: **the question was raised twice, in two Gemini dirs (193847, 829314); the third citation to 849201 is not locatable in that dir and should be struck.** Say nothing about 849201's substrate.

*Recommended plan edit:* delete §3.6(ii)'s substrate reasoning; keep and strengthen the not-locatable finding; add a one-line warning that 849201's substrate is not canon-determinable so no sweep should "harmonize" it.

### 2.2 The standpoint discipline is not missing — it is landed in canon body, for the quantity that determines $R$

This is the largest thing I found, and it improves the plan.

`#def-model-class-fitness` — a canon segment — does, for $\mathcal{F}(\mathcal{M})$, precisely what the plan says the corpus nowhere does for the persistence parameters. At `:14`:

> An important operational point: **the agent cannot directly compute its class fitness** (that would require searching over all models in $\mathcal{M}$). What it can observe is the *signature* — persistent *systematic* mismatch despite adequate learning (high gain, sufficient data, converged parameters): residuals that stay structured after parametric convergence. Structure is the discriminator, not the mismatch level …

And again, as its own titled Discussion paragraph, at `:38`:

> **Detecting low class fitness.** The agent cannot directly compute $\mathcal{F}(\mathcal{M})$ — it would need to search over all models in the class. Instead, persistent *systematic* mismatch despite adequate learning … is the observable signature — structured residuals, not merely large ones. … What distinguishes a class ceiling from a noisy channel is residual *structure* … The sharp diagnostic lives with the mismatch floor in #result-structural-adaptation-necessity.

The forward pointer discharges: `#result-structural-adaptation-necessity:56–60` lists the three observable symptoms in the body, with `:58` carrying the same discrimination caveat. And its Working Notes at `:106` carry the mechanism, from the *same auditor who raised the reserve question*:

> **The structured-residuals diagnostic — how the agent knows it hit the ceiling without an oracle.** The richest item in this segment's sweep, resolving the "how does the agent detect $\mathcal{F}(\mathcal{M})$ failure from the inside?" question raised at `#def-model-class-fitness` … By checking the *autocorrelation / mutual information of the residual stream $\delta_t$ over time*, an agent distinguishes "the world is noisy" from "my architecture is broken" — **it can detect the capacity ceiling without ever seeing the supremum** (Gemini, AUDIT-WORKING-829314).

**Four consequences.**

**(a) The diagnosis changes.** §2's "the defect is a **missing standpoint discipline** on the persistence parameters" should become: *the discipline exists in canon, is exercised cleanly at `#def-model-class-fitness`, and was never applied to $(\alpha, R, \rho)$.* That is a weaker, cheaper, and more accurate claim, and it converts Option A from "introduce a discipline" into "extend an existing one" — which is a materially different brief.

**(b) §3.2's B3 aside is false as written.** *"The corpus has language for who can move the reserve and none for who can see it"* — the corpus has exactly that language for $\mathcal{F}$, in the segment that supplies half of what $R$ is.

**(c) It challenges §6.2's sharpness.** §6.2's obstacle is *"you cannot estimate $R$ without visiting the neighbourhood of $R$"* — correct about `#detail-operationalization`'s $\hat R$ estimator, which is the estimator the plan checked. But the inference to *"the condition that makes the guarantee hold is the same condition that starves the estimate of the guarantee's margin"* now has a canon-resident counter-candidate: a **different** estimator, on residual *structure* rather than residual *magnitude*, explicitly claimed to detect a capacity ceiling *without visiting the supremum*. $\mathcal{F}(\mathcal{M})$ and $R$ are not the same quantity — but `result-persistence-condition.md:111` says $R$ "*depends on the model class and the correction architecture*," and the segment's own Connections list has class fitness shrinking effective $\alpha$. The relation is real, and the *shape* of the argument is exactly the shape §6.2 says nobody has. §6.2 remains a good hypothesis; it is not as unopposed as it reads, and a spike brief must carry the opposition.

**(d) It is a missed repair option.** See §4.3 — Option F.

### 2.3 §6.1 Obstacle 1: the self-model escape is not unnamed

The plan writes:

> **The escape is available and unnamed:** $M_t$ could carry a self-model. I grepped `#form-agent-model`, `#form-complete-agent-state`, `#def-agent-environment`, and `#def-model-sufficiency` for "self-model / models itself / model of itself" and found **nothing**. That is four foundational segments, not an exhaustive sweep of ~170 — treat it as "not established where it would be constitutive," not as proof of absence.

The self-imposed caveat is exactly right, and I want to credit it — this is the plan doing the discipline properly. But the caveat should now be cashed, because a corpus-wide sweep finds the concept treated in canon in at least four places, and two of them are load-bearing here:

**(i) `03-llm-core/src/hyp-behavioral-self-knowledge-insufficiency.md` — an entire canon segment carrying a derived no-go about agent self-knowledge.** At `:14`:

> An agent that plans a modification to its own mechanisms, using a self-model validated *behaviorally* — introspection, self-prediction, even complete counterfactual self-knowledge — cannot in general predict the outcome of that modification. … Behavioral self-knowledge, however complete, therefore *underdetermines* the outcome of a latent-anchored self-modification. Safe self-modification requires white-box (author-grade, parameterization-level) self-access, or restriction to a specific safe class of edits — not excellent self-prediction.

This is the five-element shape already assembled on the self-knowledge axis: external theorem (`#deriv-mechanism-counterfactual-separation` Results 1 and 4, via Pearl-Bareinboim), no-go, boundary characterization (the safe/unsafe edit taxonomy), strengthened consequence (white-box self-access elevated to structurally required). §6.2 says *"Element 2 (an external theorem) is what a spike would have to supply; the obvious candidates are a support/coverage argument on the stationary distribution, or a Fisher-rank argument in the manner of Instance 2."* Neither candidate is wrong, but there is a third the plan did not see: the corpus already has a self-knowledge floor with a discharged element 2, and its escape (*white-box / architectural self-access*) is the same escape the plan's own boundary menu names third.

**(ii) `disc-continuity-stance.md:32` — inside a segment the plan analysed.** The stance table's first row defines *Indifferent* as "**No self-model of persistence**; whether it continues is not represented in $O_t$," and the same formula recurs at `def-agent-spectrum.md:17` and `:58`. So the five-value continuity axis — the axis whose operational meaningfulness B3 is defending — is *built on* whether the agent has a self-model of persistence. That is a valuation notion, not an epistemic-access notion, so it is not a defense of Position B. But it means the corpus does name the object, in the neighbourhood, twice, and any Obstacle-1 argument has to engage it rather than report absence.

**(iii) `der-agent-opacity.md:78, 83, 129`** carry "**self-model quality**" as a derived *regime boundary* in the emitter-side four-regime classification (E-IV Active-deceive: "*for active-deceive, $A$ must model the observer's model of $A$ well enough to choose actions that exploit it*"). The plan read this segment in full per its §10 ledger.

**(iv) `der-observability-dominance.md:100`** names the escape the plan's §6.2 menu is missing:

> For an ELI, the "unobservable region" analog is a domain where its beliefs aren't grounded in verifiable experience — e.g. a self-model it can't introspect on freezes at the *prior* … the structural shape of truth death. The named defenses are observability investments: explicit uncertainty logging, metacognitive monitoring that surfaces ungrounded confidence, and *relational witness* (**another agent observing what the ELI can't observe about itself**).

The plan's §6.2 escape menu has four entries (exogenous probing / breakdown observation / architectural knowledge / exogenous measurement) and its closing move folds Positions C, D, E in as escapes-being-exercised. The **witness** escape is already named as such in canon — `spike-escape-standpoint-axis-2026-07-29.md` §3 confirms it: "*`#disc-identifiability-floor` already lists the rank-augmentation routes as 'interventional data via the loop, a side channel, **a witness**'.*" That is a fifth escape with an existing canonical name, and it is the one that connects Position D to the floor *by name* rather than by the plan's inference.

*Recommended plan edit:* replace §6.1 Obstacle 1's absence report with the four sites, and add `#hyp-behavioral-self-knowledge-insufficiency` to §7 Option B/C's required reading. An Option-C spike that does not know that segment exists will re-derive a worse version of it.

### 2.4 A fourth load-bearing site the plan classified as ripple-only

The plan's §5 table puts `#disc-value-functional-grounding-floor` in the "Nothing of their own — they restate Result G′ … **Low.** Ripple-only" row. Two corrections, one in each direction.

**The ripple is smaller than stated.** In all three propagation sites, the phrase "agent-available per step" is used *negatively about $V_{O_t}$*, not positively about the reserve — `disc-value-functional-grounding-floor.md:24` ("*no convention-invariant infeasibility verdict is agent-available per step*"), `deriv-reward-channel-learning-no-go.md:97` (column header "*what $V_{O_t}$ is too narrow for*"), `disc-constructive-impossibility-posture.md:42` (same). And the "**agent-side**" label they all carry is defined at `disc-value-functional-grounding-floor.md:103` as being about *who is frustrated by the floor*, not who holds the quantity: "*Both Instance F and Instance G are agent-side (the actor frustrated by the floor is the agent itself).*" So the compressed phrase and the label are both independent of Position B. If a repairer greps for "agent-available per step" expecting to find inherited Position-B claims, they will find three false positives.

**But there is a real dependency the plan missed, and it is sharper than "ripple."** `disc-value-functional-grounding-floor.md:42`:

> **Boundary characterization (the canonical escape).** The terminal grounding invariant must be *off* the objective substrate, on the **adaptive substrate** … The persistence condition is *not* an addition to the value functional; it is on a structurally distinct substrate the framework already requires for agent existence at all. The agent-side terminal grounding is therefore a ***recognition*, not a construction**: the substrate AAT already requires for the agent's existence is precisely the anchor the value functional cannot supply.

"Recognition, not construction" fails exactly if Position B fails. If the reserve is not agent-available per step, then an endogenous estimator has to be *constructed* — which is Option C — and this paragraph's claim, which is the meta-segment's headline framing of Instance F's escape, becomes false. That is a specific, quotable, load-bearing dependency at a fourth site, in a `discussion`-tier meta-segment whose exhaustion claim already has a Tier-1 adversarial spike queued against it.

*Recommended plan edit:* add `#disc-value-functional-grounding-floor:42` as a fourth row in the §5 table, at severity above ripple, with the phrase to repair named ("recognition, not construction"); and correct the grep target for the sweep from "agent-available per step" to `:42` plus the three negative-use sites.

---

## 3. Smaller corrections

### 3.1 §9.1's "committed in the wild, twice" is not established

The plan escalates the units gold from a nit to a load-bearing lubricant on the strength of two quiz answers, quoted verbatim and correctly:

> **Adaptive reserve (b05)**: $\Delta\rho^\ast = \alpha R - \rho$ is nearly exhausted when mismatch rides near $R$ — the agent is fragile …

and concludes: *"The rate reserve $\alpha R - \rho$ is not a function of where mismatch currently sits."*

That is true of the *definition*, but the quiz sentence is an implication, not a definition, and under the reading the theory itself licenses it is **correct**. Mismatch is ultimately bounded by $R^\ast = \rho/\alpha$; sustained mismatch riding near $R$ therefore means $\rho/\alpha \approx R$, hence $\alpha R \approx \rho$, hence $\Delta\rho^\ast \approx 0$. And the quiz's own next clause is in the rate register — "*a modest disturbance shock exceeds the reserve and voids the certificate*" — which is exactly the Prop A.2 shock semantics, not a state-distance reading. So the quiz author appears to have been thinking in rates.

The sentence *is* ambiguous: under a transient-excursion reading it would be a conflation. The plan asserts the strong reading without disambiguating, which is the move the project's own quantifier-disambiguation discipline exists to catch.

**This does not damage the plan's substantive point**, which is independent and good: $R - R^\ast$ (or $R - \lVert\delta_t\rVert$) is nearly agent-observable while $\alpha R - \rho$ needs all three parameters, and that asymmetry makes Option D's third bullet more attractive. Keep that. Drop the "committed in the wild" framing, or state the two readings and mark which one would be a defect.

### 3.2 §9.4's F6 conclusion is wrong; its F6 quote is truncated

The plan reports both 193847 dispositions as "*appear never to have landed*," on the strength of grepping `PROPOSALS.md`, `TODO.md`, `audits/STATUS.md`, and `04-eli-core/`. That grep scope excludes `01-aat-core/`, where F6's content is:

`result-structural-adaptation-necessity.md:107` — "**The IB-vs-structural-reserve tension — 'perfect compression is brittle.'** Aggressive Information-Bottleneck optimization … produces an agent that 'will die at the first structural shock'; survival requires deliberately *not* being perfectly compressed — carrying 'junk DNA / slack' in the model architecture, the structural analog of adaptive reserve. **This sets up a genuine tension with `#form-information-bottleneck` that the segment could name explicitly** (Gemini, AUDIT-WORKING-193847)."

So F6 landed as staged audit gold in a segment Working Note — which is where the gold-lift procedure puts it. It has not been promoted to body and no `disc-ib-vs-structural-reserve` segment exists (I checked `form-information-bottleneck.md` too: no brittleness/structural-adaptation tension paragraph). The honest statement is "**lifted as gold, never promoted**," not "never landed" — a materially different disposition, because the promotion path is already open.

Separately, the plan's quote of F6's disposition drops its second branch. `audit-findings-193847.md:151` reads: "**`architectural` → PROPOSALS candidate** for a `disc-ib-vs-structural-reserve` segment, **or addition to the existing `form-information-bottleneck` Discussion**." The dropped branch is the cheaper one and the live one.

F5 is closer to the plan's characterization: no `norm-adaptive-reserve-as-ethical-floor.md` exists. But its content is partially present — `obs-developmental-trajectory.md:21` carries "High Adaptive Reserve … a large margin for error," and `result-persistence-condition.md:196` carries the crèche/nursery reading from the same auditor.

### 3.3 §3.6's process finding is right, and I can sharpen the check it proposes

The plan recommends adding to the gold-lift procedure a check that a "readers often ask" item is not *answered as a premise* elsewhere in canon. That is correct, cheap, and generalisable — I endorse it without reservation, and it is the single best thing in the file.

Sharpening: as §2.2 shows, the failure mode has a second shape the proposed check misses. The reserve question was not only *answered as a premise* at `#deriv-self-actuation-grounding:70` — it was also **already answered properly, for the neighbouring quantity, in a canon body** at `#def-model-class-fitness:38`. So the check should be two-pronged: does any body *assume* the answer (promote to certified track), **and** does any body *already give* the answer for a structurally adjacent quantity (route as a transfer/apply item, not as new research). The second prong is what would have turned this from a repair plan into a one-paragraph extension.

### 3.4 §3.2(a) and §8 contradict each other

§3.2(a) states flatly: *"Neither step computes, maintains, or references $\alpha$, $R$, or $\rho$. The citation establishes that a per-step adaptive update exists … and is then used to license that the reserve is one of the things it maintains, which does not follow."*

§8 then argues the opposite direction from files the plan read: orient-cascade step 1 cites `#emp-update-gain`; `emp-update-gain.md:50` endogenises $\eta^\ast$ as an agent-maintained state variable; `result-persistence-condition.md:79` gives $\alpha = \eta^\ast c_{\min}$ (per-time form $\alpha = \nu\eta^\ast c_{\min}$ per `result-sector-condition-stability.md:81`). §8's own words: *"Therefore one of the three factors of $\Delta\rho^\ast$ is, per canon, already an agent-maintained endogenous state variable."*

Both are literally true — the *steps* name no parameter, and the *chain through the cited segment* reaches one of three. But §3.2(a)'s "the citation does not support the claim" is stated at a strength §8 withdraws, and the two sections never meet. The accurate version: *the citation supports the claim for at most one of three factors, via a two-hop chain the segment does not state, and supports it not at all for $R$ and $\rho$.* That is still a defect worth repairing — an unstated two-hop chain doing the work of a citation is exactly the plausibility-for-verification substitution — but the repair is "state the chain and scope the claim to $\alpha$," not "the citation is empty."

### 3.5 The reverse-strengthening's best candidate carries a canon-resident hazard the plan does not name

§7's reverse strengthening proposes $\lVert\delta_t\rVert$ as an alternative object satisfying Corollary 1(i)–(iii), calling it "*indisputably agent-available — it is `#def-mismatch-signal`, the thing the agent's whole loop is built on.*"

Available, yes. But the cited segment carries a three-way interpretive no-go on reading it, twice — `def-mismatch-signal.md:18` and again as its own Discussion paragraph at `:52`:

> **The zero-aporia ambiguity.** $\delta_t \approx 0$ does NOT necessarily indicate model adequacy. It may mean: (a) the model genuinely reflects reality — *desirable*; (b) the agent is only observing aspects its model already explains, while remaining ignorant of aspects where the model is wrong — *confirmation bias*; or (c) the observation channel is too noisy to detect model errors — *architectural limitation*. Only (a) is desirable. … silence can mean peace or deafness.

For a *terminal grounding invariant* — an object whose verdict licenses or forbids an objective revision — a quantity whose low readings are three-way ambiguous between "safe," "self-deceived," and "deaf" is a poor candidate on requirement (i), convention-invariance of the *verdict*, even though the number itself is convention-free. The spike should be briefed with this, because it is the obvious first objection and it lives in the segment the plan cites in the candidate's favour.

The same caution applies, more mildly, to the mood candidate: `def-mood.md:46` records that mood's persistence-compatibility rests on four conditions **(MG-1)–(MG-4)**, of which (MG-4) is explicitly conditional — "*a condition stated here because $a_t$'s functional form is deliberately unpinned; any concrete choice should be checked against it*." A mood-as-proxy attempt inherits that discharge obligation.

Related, and worth carrying into the same brief: `spike-escape-standpoint-axis-2026-07-29.md` §4a is a *worked instance of both directions of this argument*. It establishes the self-silencing shape the plan's §6.2 wants ("*calibrating $\sigma_v$ requires ground truth on whether $v$ was achieved, which is exactly what $\sigma_v \approx 0$ withholds*") **and** the counter-move ("*an agent with a calibrated $U_{\text{obs}}$ knows exactly which node is poorly observed — which makes the region targetable … and the segment's central claim false in that case*"). The plan cites §4a for the first half only. The second half is the sharpest available caution against §6.2 landing as cleanly as it reads, and the plan's own "clean resolutions of one's own investigation deserve suspicion" instinct was pointing at it.

### 3.6 §10's transcription ledger overclaims

The ledger states: "*Renders identically; no other character was altered in any quotation in this file.*" Three `#detail-operationalization` quotes add bold emphasis that is not in the source — `**exogenous perturbation channels**` (source `:99` is unemphasised), `**breakdown detection**` (`:32`), `**exogenous environmental change measurements**` (`:194`). The emphasis is cosmetic and the plan's use of the quotes is fair, but a ledger that claims character-level fidelity should either mark the added emphasis or drop the claim. Given how much of this plan's weight rests on its quoting being trustworthy, I would fix the ledger rather than the quotes.

### 3.7 §9.2's staleness finding is incomplete in a way that matters for §3.2(c)

The plan flags `CURRENT-VOL1.md:1761` as predating the Lemma-A.1N correction. True. But the *same* snapshot is also stale on the segment at the centre of this investigation: `CURRENT-VOL1.md:10851` reads

> **(iii) not an AAT objective-functional.** It lives on $M_t$ and the correction machinery; [Discussion 6.5] makes the orthogonality explicit (the persistence machinery acts on $M_t$ and the correction dynamics, **formally independent of $O_t$**).

— which is verbatim the clause `deriv-self-actuation-grounding.md:141` records as **deleted** on 2026-05-30 for self-contradiction. (One elision disclosed: the snapshot renders "Discussion 6.5" as a markdown anchor link into the `disc-continuity-stance` slug; the link target is dropped here so `bin/lint-md`'s Obsidian cross-ref rule does not fire on a quoted generated-file link. No word altered.) So VOL1 carries the *repaired* (ii) alongside the *refuted* (iii), one line apart. This does not weaken §3.2(c)'s exposure point — the hardened (ii) is genuinely reader-facing — but a repairer reading VOL1 to gauge exposure needs to know the snapshot is stale at that exact site, and §9.2 should say so.

### 3.8 §3's enumeration misses two canon sites

Neither is a counterexample; both are Position A. But Option A's sweep needs the complete list, and both are places a marking pass would have to touch.

- **`form-resource-budget.md:65`** — a canon Discussion paragraph (`status: conditional`, `stage: draft`) devoted to the reserve: "*#result-sector-persistence-template's adaptive reserve $\Delta\rho^\ast=\alpha R-\rho$ is a **margin** (how much extra disturbance the agent can absorb at its current rate); $\mathcal B_t$ is a **fuel** … They are independent: an agent can have comfortable margin and an almost-empty pool.*" The plan's §10 ledger lists this segment as read in relevant part, so the omission is from §3, not from the reading.
- **`01-aat-core/src/old-tf-appendix-f-multi-agent.md:221`** — "*Reserve as vulnerability: $\Delta\rho^\ast$ is the target adversaries aim to exhaust and allies aim to preserve.*" Noting it mainly because the file has **no YAML frontmatter** and is not a slug-named segment, yet sits in the live `01-aat-core/src/` tree. That is a separate hygiene item, orthogonal to this plan, but a sweep tool run over `src/*.md` will hit it.

---

## 4. The central structural claim, tested

The plan's structural claim has two halves. I tested both.

### 4.1 Is the partition real, or are some standpoints the same standpoint?

**Partly the latter, and the plan already knows it without saying so.** §1 and §3 present five standpoints as five *actors*. §6.2 then collapses three of them: "*Positions C, D, and E are each an escape being exercised — the analyst has exogenous channels, the ELI monitor has instruments outside the entity, the designer has architectural knowledge.*" Under the (I)-axis — the axis that actually decides the question — C, D, and E are **one** standpoint (off-policy / exogenous access), differing only in which escape they exercise. That is why §7's Option A proposes **three** markers (theory-side / observer-side / agent-side) rather than five: Option A is the honest partition, and §1's five is a presentation device.

I do not think this is a defect so much as an unresolved register clash: §1 asserts five standpoints as the finding, §7 quietly repairs it to three. The plan would be stronger stating the three-marker partition up front and using the five actors as instances beneath the observer-side marker. As it stands, a reader could take "five distinct standpoints" as the structural result, and it is not — the structural result is a three-way split on information regime.

Positions A and B are genuinely distinct from each other and from the observer group: A is an existentially-quantified constant in a certificate (`form-sector-condition.md:32`, and `:56`'s "assumed as a per-system empirical claim" for half the in-scope classes), B is a component of $X_t$. That distinction is real and load-bearing, and it is the one the finding needs.

### 4.2 Is the undefended standpoint defended somewhere the plan did not look?

**For the reserve: no.** I swept every occurrence of "adaptive reserve" and `\Delta\rho` across all four component `src/` trees (78 hits), the `terminology/` tree, `LEXICON.md`, `CURRENT-VOL1.md`, `empirica/`, `msc/`, `spikes/`, and `audits/`. Every site is Position A, C, D, or E — third-person capacity, analyst estimate, external monitor, or designer factorization — except the three the plan names. No derivation, no estimator, no Working Note anywhere claims the agent reads $\Delta\rho^\ast$ from its own state. **"Nowhere derived" holds.**

**For the discipline: yes, and it changes the repair.** §2.2. `#def-model-class-fitness` supplies the marking, the reason, and the proxy for the sibling quantity; `#hyp-behavioral-self-knowledge-insufficiency` supplies a derived self-knowledge no-go with a discharged external theorem; `#disc-identifiability-floor` already names the witness escape. So the correct statement is: **Position B is undefended, and the framework already knows how to state that honestly — it has done so twice, for adjacent quantities, and nobody transferred it.**

That is a better finding than the plan's, because it converts an open research question into an application of settled practice, and it is the reason §4.3 exists.

---

## 5. The history, tested

Both history claims are correct, and one is stronger than the plan claims.

**The phrase change between spike and segment.** Verified to the second (§1). Spike `c63d86f` 23:37:48; segment `e976b94` 23:55:57; 18 min 09 s; the landed text is byte-identical to today's `:70`, so the hardening happened at landing and has never been touched since. The hedge deletion and object substitution are exactly as described. My only refinement is the calibration note in §1: the spike had already asserted, unhedged, that the margin "*is a finite read, not a Bellman solve*" — so the delta is the attachment of "*the in-scope agent already maintains*" to the reserve plus the loss of "*exactly the kind of*," not the whole claim. The plan's identification of *which clause* is unsupported is correct either way.

**The terminology entry's provenance.** Verified and **strengthened**: `git log -S "track the reserve" --all` returns exactly one commit in the repository's entire history, and `git show 868f72a~1:LEXICON.md` shows the pre-migration source row was a one-line table cell carrying only what is now the `brief:` field. So the tracking clause was not migrated — it was **written fresh by the migrating sub-agent while expanding a table row into a paragraph**, and the `primary_source` it points at has never contained it. That is a cleaner instance of the failure than the plan claims, and it is worth stating that way in the repair, because it removes any suggestion that some earlier source said it.

**The near-miss at 2026-05-30.** Verified. `spike-continuity-orthogonality-2026-05-30.md`'s headings and body confirm its subject is the (iii) orthogonality grain throughout; it mentions the reserve twice (`:41` in the parameter read-off, `:130` in the L3-coupling payoff) and never examines (ii). The Working Note at `deriv-self-actuation-grounding.md:141` is verbatim as quoted. The plan's mechanism — "*absent evidence is quieter than contradictory evidence*" — is a fair reading of why one leg of a three-leg corollary got audited and another did not.

---

## 6. Repair options — soundness, costing, and the one that is missing

### 6.1 The five options as written

**Option A (standpoint discipline)** — sound, and its "four debts, one move" accounting verifies: `def-observation-function.md:59` and `:63` and `scope-adaptive-system.md:64` all exist, are all parked candidate-clarifications, and all ask for the analyst/agent split. Costing is honest ("a cross-segment marking sweep"). **Amend:** it should be re-framed as *extending* `#def-model-class-fitness`'s existing discipline rather than introducing one (§2.2), which lowers its cost and raises its defensibility; and its sweep list must add `form-resource-budget.md:65` and the two `result-structural-adaptation-necessity` gold items (§3.8, §3.2).

**Option B (spike the identifiability floor)** — sound, correctly sequenced before C/D per strengthen-first, and the methodology caution is well-sourced (the new-instance four-test spike vs the new-cluster caveat; the Fano double-negative). **Amend:** the brief must carry the §2.2 counter-candidate (structured residuals detecting a ceiling without visiting the supremum) and `#hyp-behavioral-self-knowledge-insufficiency` as prior art, or the spike will land a floor that canon already partially contradicts.

**Option C (endogenous estimator)** — sound, and §6.3's precedent is exactly on point and correctly quoted. The plan's own honesty about the transfer ("*plausible for $\rho$ … prima facie blocked for $R$*") and its named expectation of a split verdict are well-calibrated. **Amend:** the corpus already contains a *worked split verdict* on the adjacent quantity — `#def-model-class-fitness` declares $\mathcal{F}$ non-computable and substitutes a proxy — so Option C's expected outcome has a template, not just a prediction.

**Option D (weakest sufficient burden)** — sound, and the best-costed option in the file. Its reading of Lemma 2's bar is verified verbatim (§1). Its four candidate weaker objects are all real; the conservative-lower-bound bullet is genuinely sharp and I agree it is "*a genuine gift the current phrasing throws away*." I also agree with the plan's own ranking of it first: it is the one place the current text is not merely unsupported but *imprecise about its own requirement*, and that fix is pure gain. **Amend:** bullet 1 ($\lVert\delta_t\rVert$-based objects) inherits the zero-aporia ambiguity (§3.5).

**Option E (minimum honest fallback)** — sound and correctly gated behind B/C/D. The citation correction it names is right and is due regardless of how the substantive question resolves.

**Sequencing (§11)** — I agree with it, including putting Option D first and the process note last-but-cheapest. One change: with Option F in hand (below), the ordering becomes F → D → A → B/C → E, because F is cheaper than A, is not a softening, and makes D's re-reading easier to write.

### 6.2 Is anything overcosted or undercosted?

One undercosting: Option A is described as "*a cross-segment marking sweep. Touches many segments lightly*" — but per §2.2 the marking has a canon precedent to match, which means the sweep is a *transfer* with a fixed target wording rather than a design exercise. That is a real cost reduction the plan does not claim.

One risk the plan does not cost: Option A touches `#result-sector-persistence-template`, whose whole point is parameter-freedom across seven instantiations (one of which is not an agent at all). A standpoint marker introduced there has to survive the composite instantiations — the plan flags this correctly at §3.1 ("*Any repair must survive the template's generality*") but does not carry it into Option A's cost.

### 6.3 The missed option

**Option F — apply `#def-model-class-fitness`'s existing template to the persistence parameters.**

Add to `#result-persistence-condition`, next to the reserve paragraph at `:115`, a short paragraph in the form the framework already uses one segment away:

> The agent cannot directly compute $(\alpha, R, \rho)$ — $\alpha$ is a worst-case infimum over $\mathcal B_R$, $R$ is a model-class capacity the agent does not visit under the guarantee, and $\rho$ is a property of a disturbance process it sees only through $h$. What it can observe is [the named signature]. Estimation from traces, with the exogenous access each estimator requires, is in `#detail-operationalization`.

**Why this is a distinct option and not a variant of A or E.** It is not a sweep (one paragraph, one segment, with a ripple to the terminology entry). It is not a softening: it is a *positive claim*, stated at the same tier and in the same voice as `#def-model-class-fitness:38`, with a canon precedent that fixes the wording. And it makes Position B's repair mechanical rather than judgemental — once `#result-persistence-condition` says the parameters are not directly agent-computable, `#deriv-self-actuation-grounding:70` cannot cite it for the opposite, and the citation defect self-resolves.

**What it costs.** One paragraph, plus one `bin/term decide` on the terminology entry, plus the honest admission that the "named signature" slot is currently empty for the reserve — which is precisely what Options B/C/D would fill. So Option F is not a substitute for the substantive work; it is the *frame* the substantive work lands into, and it is available now, at a cost the plan's cheapest current option does not match.

**Why it is strictly better than Option E.** Option E is the softening, gated behind three attempts. Option F is not gated, because it is not a weakening — it is the same move the framework made for $\mathcal{F}(\mathcal{M})$, which nobody regards as a weakening of `#result-structural-adaptation-necessity`.

---

## 7. Over- and under-claiming

The plan asks to be checked on this, and flags one of its own broken expectations (the `#detail-operationalization` inversion). That flag is genuine and the inversion is real — I verified all six citations behind it and it is the plan's strongest single move.

**It did not flag enough.** Four further expectations broke or should have:

1. **"Missing standpoint discipline"** (§2) — broke against `#def-model-class-fitness`. Unflagged because unlooked-for. §2.2.
2. **"The escape is available and unnamed"** (§6.1) — the caveat was written honestly but the escape *is* named, in four places. §2.3.
3. **"849201 is attributed to Gemini everywhere else I checked"** (§3.6) — a four-word hedge ("everywhere else I checked") doing the work of a repo-wide count that runs 2:1 the other way. §2.1.
4. **"The conflation is committed in the wild, twice"** (§9.1) — an ambiguous sentence read at its strong reading without disambiguation. §3.1.

**Overclaims:** §3.2(a)'s "the citation does not support the claim" (too absolute; §3.4); §9.4's "never landed" (§3.2); §9.1's "in the wild, twice" (§3.1); §10's character-fidelity claim (§3.6); §3.1's "seven segments on state variables that are not an agent's beliefs" (six of seven).

**Underclaims — and there are more of these than overclaims, which is the right direction:**

1. **The terminology provenance is worse than reported.** The tracking clause was authored fresh in a build commit, not migrated; `git log -S` proves it appears nowhere else in history. §5.
2. **The 849201 not-found is stronger than reported.** The plan says "not found where it should be, not does not exist." Having searched the whole dir, I can say it is not there. §1.
3. **`#disc-value-functional-grounding-floor:42` is a fourth load-bearing site**, not a ripple. §2.4.
4. **§8's argument is stronger than §3.2(a) lets it be.** One of three factors is already canon-endogenous. §3.4.
5. **VOL1 is stale at the investigation's own site**, not only at §9.2's. §3.7.
6. **Option A is cheaper than costed**, because the marking has a precedent to copy. §6.2.

**Calibration, overall:** the plan's severity assessment in §5 is its best work — it declines to inflate a real defect into a collapse, correctly locates the loss as "reach, not correctness," and says so plainly. The disposition throughout is strengthen-first rather than soften-first, the negative results are reported as negative results, and the self-flagged inversion is exactly the move the project's discipline asks for. The four unflagged breaks are all of one type — a scoped grep whose scope was not stated as a limit on the conclusion drawn — and that is a fixable habit rather than a judgement problem.

---

## 8. The blocked read — assessment

**The call was right, and it should not be lifted for this plan.** I concur with §8's own recommendation, and nothing in my audit changes it.

**Why the call was right.** §8's load-bearing argument is built entirely from files the plan read, and I verified all three of its steps verbatim (§1). It establishes that the blocked file matters *for Option C's scope only* — whether the estimator is a fresh derivation or a corollary, and whether it reaches one factor or two. That is a scoping question, not a soundness question, and §8's "what is unaffected" paragraph is correct: §6.2's obstacle is about $R$, which is a model-class capacity, and no result about gain dynamics can supply data at radii the agent never visits. Options A, D, E, F, every per-location finding in §3, the whole history in §4, and the severity assessment in §5 all stand without it. Stopping and writing three questions instead of reading was the disciplined move, and it preserved a real measurement at a cost of nothing this plan needed.

**Are the three questions the right ones?** Yes, and Q2 is the sharpest — asking whether the Lyapunov argument presupposes $(\alpha, R)$ as known constants is exactly the circularity test that decides Option C's cheap route, and it is answerable yes/no without any summary. Q1 correctly names both composition factors ($c_{\min}$ and $\nu$), which matters because `result-sector-condition-stability.md:81` records the $\nu$/time-normalization gap as a real defect resolved on 2026-05-30 with the bridge now written $\alpha = \nu\eta^\ast c_{\min}$ — a question that omitted $\nu$ would get a misleading answer. Q3 (does an "endogenise-the-parameter" template transfer, or is it specific to innovation-sequence uncertainty statistics?) is the right generalization probe.

**One question I would add, and it is cheap to answer:**

- **Q4.** Does the segment contain a standpoint marking of the `#def-model-class-fitness` form — an explicit statement that some quantity is *not* directly agent-computable, paired with an agent-observable signature that substitutes for it? Yes/no, plus the quantity's name if yes.

Q4 is worth adding because it is the only question whose answer changes the *cheapest* option rather than the most ambitious one. If yes, Option F's precedent count goes from one to two, the wording to copy is already inside the segment most closely coupled to the reserve, and the repair gets cheaper again. If no, nothing is lost. And like Q1–Q3 it is answerable without a general summary, so it does not widen the leak.

**On lifting the gate:** I see no reason to lift it, and I did not open or grep the file. If Joseph wants Option C briefed before the prediction is scored, the cleanest route is the one §8 already proposes — put Q1–Q4 to the segment (or to the prediction-holder after scoring) rather than an open read.

---

## 9. What I did and did not do

**Read first-hand, in full or in the relevant part, with every line reference opened at the cited line:** all 53 locations in §1's ledger. Where a claim rested on absence, I re-ran the search wider than the plan did and report the scope.

**Independent sweeps I ran that the plan did not:** every occurrence of "adaptive reserve" / `\Delta\rho` across all four component `src/` trees (78 hits, all classified); every canon occurrence of "agent-side" / "agent-available"; every canon occurrence of "self-model" / "models itself" / "model of itself"; repo-wide substrate-attribution counts for `AUDIT-WORKING-849201`; `git log -S "track the reserve" --all`; full-dir keyword search of `AUDIT-WORKING-849201` for the reserve question; `git show <commit>:terminology/entries/adaptive-reserve.md` at all four commits plus `868f72a~1:LEXICON.md`.

**Explicitly not done:**

- `01-aat-core/src/deriv-adaptive-gain-dynamics.md` — not opened, not grepped directly, not read at any commit.
- No mathematics attempted. §2.2's challenge to §6.2 is a located counter-candidate, not a refutation; nobody has done the math on either side.
- No exhaustive read of the other `AUDIT-WORKING-*` dirs (I grepped across all of them and read the hits). 849201 *was* searched exhaustively for the one question at issue.
- No prior-art search outside the repo.
- No canon edited; no `bin/term` run; no `AUDIT-WORKING-*` dir processed, moved, or reorganised.

**One leak, disclosed — identical to the plan's, and unavoidable for this audit.** My corpus-wide sweep for "adaptive reserve" / `\Delta\rho` over `0*/src/*.md` reproduced the plan's §10 observation: `deriv-adaptive-gain-dynamics.md` does not appear in the results, so I know it contains neither string. I did not narrow further and did not open it. If the prediction being scored touches whether that segment mentions the adaptive reserve, this leak is now held by two agents and the prediction-holder should be told; the plan's §10 already flagged it, and I am confirming rather than extending it.

---

## 10. Questions for the plan's author

Offered in the order I would want them, and none of them expensive:

1. §3.6(ii) — was the 849201-is-Gemini read based on a wider check than `der-interaction-channel-classification.md:195` and `def-observation-function.md:63`? I found 49 Claude / 25 Gemini repo-wide and want to be sure I am not missing a manifest that settles it.
2. §9.4 — was `01-aat-core/` deliberately outside the F5/F6 grep scope, or an oversight? The F6 content is at `result-structural-adaptation-necessity.md:107`.
3. §9.1 — did you consider the steady-state reading of the quiz sentence ($\lVert\delta\rVert \to R^\ast$, so mismatch near $R$ implies reserve near zero)? I could not make the conflation charge stick and want to know whether you had a reason I am missing.
4. §6.1 Obstacle 1 — was `03-llm-core/` in the self-model sweep? `#hyp-behavioral-self-knowledge-insufficiency` seems like it should be in Option B/C's required reading either way.
5. §3.2(a) vs §8 — do you agree the citation-emptiness claim should be scoped to $R$ and $\rho$, with the $\alpha$ chain stated rather than denied?
6. Did you see `#def-model-class-fitness:14, :38` at any point and set it aside for a reason? I want to know whether Option F is genuinely new or was considered and rejected.

---

## 11. Summary verdict

**Sound, with one false sub-claim, two missed bodies of canon evidence, and a missed repair option that is cheaper than anything the plan lists.**

- **52 of 53 citations hold**, most verbatim, including every load-bearing one. This is a well-verified document and reads as one.
- **The central finding holds.** Position B is asserted in exactly three places, is load-bearing for Corollary 2's constructive boundary, and is nowhere derived. I tried to break it and could not.
- **The history holds**, to the second, and the terminology provenance is worse than the plan claims.
- **The severity assessment holds** and is well-calibrated in both directions.
- **§3.6(ii) is false** and would have misdirected a fix across 49 canon sites. The conclusion it supports survives by a different route, which I strengthened.
- **§2's diagnosis needs re-framing** from "missing discipline" to "existing discipline never applied," on the strength of `#def-model-class-fitness:14, :38` and `#result-structural-adaptation-necessity:56–60, :106`. This makes every option cheaper and adds **Option F**.
- **§6.1 Obstacle 1's absence report should be replaced** with four canon sites, one of them a whole segment carrying a derived self-knowledge no-go.
- **`#disc-value-functional-grounding-floor:42` is a fourth load-bearing site**, at severity above ripple.
- **§9.1 and §9.4 are overclaims**; §3.4 is an internal inconsistency; §3.6, §3.7, §3.8 are small.
- **The blocked-read gate should not lift**, the call to stop was right, the three questions are well-formed, and I propose one addition (Q4) that could make the repair cheaper still.

The plan's own §11 closing line — *"the reserve's mathematics is untouched and correct … What is in question is who holds the number"* — is the right frame, and after this audit I would add one clause: **the framework already knows how to say who holds a number it cannot compute. It said so about class fitness. Nobody said it about the reserve.**
