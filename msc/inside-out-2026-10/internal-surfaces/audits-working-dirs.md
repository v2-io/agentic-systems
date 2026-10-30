# Audit working dirs — what is stranded there, and how much it matters

*Objectives tree: feeds **KR3.2** of `../INTENT.md` (live theory stranded inside asf is mapped), and through it KR3.3 and O1. Cross-surface synthesis: `00-cross-surface-map.md`.*

*Map of the 24 `audits/AUDIT-WORKING-*` dirs, `audits/ADJUDICATION-WORKING-218564/`, and `audits/.gem-hunt-trail/`, written 2026-10-30 (read against the working tree at roughly `4ee2b895`→`5587ec77`; other agents were committing in parallel). Author: a fork of the inside-out coordinator (Claude Opus 5.5). Sibling maps cover the top-level `audits/*.md` files and `audits/.integrated/`, Working Notes, spikes, `msc/`, and trackers. Dates come from `git log` on each path; "first/last" = first and last commit touching the dir.*

**Who reads this.** The coordinator first; then the goal-setting conversation with Joseph and the owner-level review; later, integration agents who need to know where to go. The slug-keyed table at the end is for the last group.

**Coverage, stated plainly.** I read in full: the 628417 synthesis and batches 10–13; the 374162 predictions, outline and reflections for batches 01–04 and 08–10; the 731548 predictions, running outline and reflection 36; the 773921 predictions, its five Appendix-A reflections and the change/curiosity sections of its 24 Volume-3/4 reflections; 829314's TST reflections 01–05; 471203's `adversarial-creative-challenges.md` (headings, verdicts, and the full "missing" list); the gold-lift tracker; the G2 triage; the ADJUDICATION file's structure, Fresh-13, Fresh-17 and Theme A; 184930 in full; the heads of most other files. I did **not** read the bodies of 451729, 963715, 613842, 849201 (beyond one sample), 742613, 584721, 526815's 687-line running outline, 731548 reflections 01–25 or its `verify/` dir, or the 374162 quiz files. Claims below about those are about their *status and shape*, measured by script and git, not about their content. Where I checked a claim against current canon, I say so.

---

## 1. The short version

1. **The "05-30 gold-lift moved audit notes into Working Notes" belief is true for about half the corpus and false for the rest.** Measured today: 119 segments carry an `Incidental audit gold` block, *all* in `01-aat-core`, covering the sweep's batches A1–A17 (Part I through Appendix-A set 2). The sweep stopped on 2026-05-31. **Zero** TST, logogenic, or logozoetic segments were swept, nor AAT batches A18–A21 (Appendix-A set 3, the bias-bound/discussions batch, templates-plus-impossibility, Fisher/IB plus the worked examples). The tracker that holds the plan, `.gem-hunt-trail/gold-lift-sweep-2026-05-30.md`, still says "next — wave 5" and was never resumed. So for Volumes 2–4, the first-encounter cognition of every auditor who read them still lives only in these dirs.
2. **The three freshest audits are almost entirely unlifted, and they are the most whole-theory ones.** 731548 (Claude Fable 5, 2026-07-02, Part I main chain plus a six-agent verification round), 374162 (Claude Fable 5, 2026-07-20, a quiz-producing walk through Part I and Part II Ch.1–2), and 628417 (Grok 4.5, 2026-07-20, an "experiential" walk through all of AAT) postdate the sweep. Only reflections 26–35 of 731548 and batches 05–07 of 374162 were lifted (2026-08-22, into `#impl-persistence-and-limits`). The rest sits here.
3. **One filing record misstates this.** `audits/.integrated/MANIFEST.md` (2026-08-22 entry) says 374162 batches 01–04 and 08 "stay (their segments' gold was lifted 2026-05-30 into source WN; not re-checked this cycle)". That cannot be true: 374162 was written on 2026-07-20, seven weeks after the 05-30 lift. `grep 374162` over all segments finds exactly one hit, `#impl-persistence-and-limits`. The swept *segments* carry older auditors' gold, not 374162's. The same reasoning applies to 731548 reflections 01–25 and all of 628417.
4. **Several live inconsistencies inside canon trace back to these dirs and are still present today** (each checked by me against current `src/`, §3.1). The sharpest: canon asserts in four places that structural adaptation is "generic, not exceptional" for long-lived agents, while canon's own `#sketch-structural-adaptation-genericity` says that hand-off is "plausibly a mild overclaim" with no bridge derived.
5. **The most-converged missing artifact in the whole audit corpus has not been written.** A floor-routing diagnostic (take "persistent high mismatch" and route it to raise gain / keep learning / fix sensors / change model class) was reached independently by five auditor arrivals. It has been a `TODO.md` item since July. A Volume-4 "shadow catalogue" (Part I theorems whose Volume-4 readings inherit Part I's tier) sits beside it, also unwritten.
6. **These dirs hold the best available answers to Joseph's "what is this theory even trying to illuminate?"** That answer comes from readers who walked the whole of AAT and then said, in one or two sentences, what they found. §4 collects them verbatim with their sources. They are inputs for the owner review, not verdicts.
7. **A caution travels with the gold.** About half these auditors are Gemini instances, and their reflections are uniformly enthusiastic: "flawless," "nothing to change," "mathematically proves." Their framings are often good teaching material. Their verification claims are not evidence. Separately, the ADJUDICATION file records a seven-cycle auditor convergence that AAT's contribution is "epistemic-architectural rather than mathematical." That is the deflation pattern Joseph corrected on 2026-05-21 (CLAUDE.md, *Math-novelty recognition*). Convergence among primed readers is not truth.

---

## 2. Lift status, measured

The script `audit-gold-status.py` (in this directory; read-only; `python3 -I audit-gold-status.py`) joins every unfiled working file to the segment slug(s) in its filename and reports whether that segment carries lifted gold. Summarized:

| Class | Where | What it means |
|---|---|---|
| **Unswept volume (never lifted)** | 193847 `70`–`74` (TST); 829314 `tst-core/01–11`, `logogenic-agents/02–07`, `logozoetic-agents/01–06`; 849201 `71`–`86` (TST/LLM pairs); 773921 `93`–`116` (LLM/ELI) | Volume 2–4 first-encounter gold. Not in any segment's WN. |
| **Unswept AAT appendix batch** | 773921 `21`, `22`, `55`, `56`, `61` (`#deriv-adaptive-gain-dynamics`, `#deriv-fisher-local-update-gain`, `#deriv-causal-ib-lmi`, `#deriv-strategy-cost-regret-bound`, `#deriv-edge-credence-dynamics`) | Batches A18–A21 never ran. |
| **Postdates the sweep (unlifted although the segment shows "swept")** | 731548 `01`–`25` + `verify/`; 374162 batches 01–04, 08–10; all of 628417 | July 2026 readings. Segment WN carries *older* gold only. |
| **Lifted, but the source was never filed** | Batch-format files: 451729 `01-batch-NN`, 963715 `NN-MM-…`, 471203 `NN-MM-…`, 613842 themed, 849201 paired, 266847 paired, 308172 triple; `scope-and-or` notes in 526815/584721/773921/829314/849201 | The sweep's rule was to move a batch file only once every covered segment was swept, then reconcile at the end. The end never came. Per-item status is unknown until checked. |
| **Skip-mostly by plan** | 308172, 419628 (naming-vote cycles), 527914 (codex naming), 542891, 738192 (thin partial walks), 472913 (diagram cycle), 184930 (predictions only) | Little theory content. 472913 is a pedagogy asset (§5). |

A system observation: the per-segment lift fits audits written one-file-per-segment. Batch, paired and whole-walk audits never fit it, so they were held forever, and the strongest recent readings are whole-walk. §6 has a suggestion.

---

## 3. Stranded theory, by kind

### 3.1 Live inconsistencies or defects in canon (checked against `src/` today)

- **Structural-adaptation genericity: canon contradicts itself.** `#deriv-sector-condition` (body lines ~18, ~221, ~274) and `#deriv-stochastic-non-exit` (body ~66; Findings ~105, attributed to Gemini 829314) state that because Model-S exit is certain, the structural-adaptation trigger is "generic, not exceptional." `#sketch-structural-adaptation-genericity` (status `sketch`) argues that this is plausibly a mild overclaim: the OU instance is positively recurrent, exit-and-return is not class inadequacy, and `#result-structural-adaptation-necessity`'s trigger is fitness-driven, not noise-driven. Three candidate bridge derivations are named there and none was attempted. Source: 374162 batch-08 reflection, which caught it while answering its own quiz. Strengthen-first target: derive the bridge, or replace the four assertions with what is true.
- **`#deriv-variational-sector-condition`'s headline factor $\sqrt{1-r^2}$ is undischarged.** The opening paragraph (line 18) says mean-field VI is "structurally sub-optimal … by a factor $\sqrt{1-r^2}$ in the sector constant." $r$ is never defined and the factor is never derived in the segment, whose Formal Expression supports only an additive $O(\sqrt\varepsilon)$ degradation. This is a Gate-2 shape: it sounds derived but is not. The verifier's guess is that the factor comes from `#deriv-fisher-whitened-update-rule`'s same-symbol result, in which case a definition plus a citation may close it. Source: 374162 batch-08 verification; it was passed to Joseph on 2026-07-20 and is still present.
- **`#emp-update-gain`'s `depends:`** lists only `def-mismatch-signal` and `def-observation-function`, although its Epistemic Status rests on `#deriv-fisher-local-update-gain` (the exactness tier) and its opacity resolution on `#deriv-adaptive-gain-dynamics`. Its Kalman row also renders the conditioning bar as `\Vert` (`P_{t\Vertt-1}`), which displays as a double bar. 731548 adds that the segment's `type: empirical` is a "deflation fossil": the Fisher-local exact derivation landed and the type never moved. Sources: 374162 batch 04; 731548 running outline item (li).
- **Already fixed since the audits (checked):** the "reducible" label on the three-floor mismatch decomposition (now "three floors, two kinds of irreducible"); `#impl-cooperative-adversarial`'s Regime-III "zero" contradiction (now a variance-draining "unmodeled trade"); $M_0$ now mentioned in `#def-chronica` and `#form-agent-model` (once each; I did not check that the 731548 "trichotomy" paragraph landed in full); the G2 canon-to-spike references (now all inside Working Notes). Listed so nobody re-opens them.

### 3.2 Missing artifacts the auditors converged on

- **Floor-routing diagnostic segment.** Five arrivals in 731548 alone (reflections 13, 20, 21, 29, 33), plus the FM-discrimination reader-question. Its ingredients are already in canon: the structured-versus-white residual signature in `#def-model-class-fitness` and `#result-structural-adaptation-necessity`, the three floors in `#result-mismatch-decomposition`, and gain collapse in `#emp-update-gain`. In `TODO.md` (line ~522) since 2026-07-03; not started. It bears on `#def-model-class-fitness`, `#result-mismatch-decomposition`, `#emp-update-gain`, `#result-structural-adaptation-necessity` and `#impl-persistence-and-limits`.
- **Volume-4 shadow catalogue appendix.** Ten Part-I theorems with Volume-4 readings: exit-certainty becomes "resurrection, not fortress"; the five gain/persistence failure modes become the deaths; the temporal-nesting violation becomes the mood pathology; and so on. 731548 called this its "strongest generative recommendation … worth more to the ELI program's defensibility than most direct Volume-4 writing." In `TODO.md` (~523); not started. The staging text is the "shadow catalogue (whole, as staging)" lifted into `#impl-persistence-and-limits` WN on 2026-08-22.
- **Ch.1 chapter intro.** Part I Ch.1 is the only Part-I chapter without an intro segment (731548 legibility ledger). The 731548 FINAL also prescribed a Part-I Ch.3 calibration-pathology note, which spike `spike-escape-standpoint-axis-2026-07-29` found still unrouted. That one belongs to the spikes map; I mention it because its prescription originates here.

### 3.3 Missing-theorem candidates (named by auditors, never spiked)

From 731548 (running outline §E.7 and FINAL §F; reflection-level detail in `AUDIT-WORKING-731548/` 11, 16, 18, 22, 27, 33):

- **Class-1 compression price.** IB-optimal compression is policy-relative, so a strictly goal-blind $\phi$ is generically compression-suboptimal. Goal-blindness then has an IB cost, possibly with an optimal $\kappa^\ast \gt 0$. The framework prices Class 3's bias but not Class 1's compression loss. This bears on `#der-directed-separation`, `#form-information-bottleneck` and `#der-class-coercion-via-wrapping`. It is a real tension with the theory's architectural recommendation and the one I would put first.
- **$g_M$ calibration (confabulation) bound.** Interior between-event dynamics should not decrease expected calibration. No such constraint exists. Bears on `#form-event-driven-dynamics` and the logogenic interiority segments.
- **Compilation-cost axis.** Goals compile to $\pi$, deliberation to fluency, knowledge to weights: one unpriced cost family. Bears on `#der-action-selection` (fluency), `#der-deliberation-cost` and `#form-consolidation-dynamics`.
- **EIG-at-CIY-prices conservation.** Using CIY as a tractable surrogate smuggles EIG's intractability back in through the formulation cost. Bears on `#def-causal-information-yield` and `#disc-ciy-unified-objective`.
- **IB-versus-structural-reserve tension** (reflection 33). Bears on `#form-information-bottleneck` and `#result-persistence-condition`.
- **Necessity-under-tightness lemma.** This was B-1's strengthen-first landing for the persistence "iff". The FINAL says it "is itself a small real theorem worth stating"; check whether it now stands as its own statement in `#deriv-sector-condition`.

Only the floor-routing segment and the shadow catalogue are in `TODO.md`. The six above live only in the 731548 FINAL (sibling's surface) and these reflections.

### 3.4 Open structural questions about the theory's architecture

These are the questions a reader asks after walking the whole meta-architecture. None is tracked anywhere I found.

- **Is "general open" infectious across the separability ladders?** If one of M2's eight ladders falls to its general-open rung, do the others follow? Source: 628417 batch 12 ("a real open, not a deferral of reading"). Bears on `#disc-separability-pattern`.
- **Composition of floors.** When an agent faces two M1 floors at once, can the escape from one block the escape from the other? This is the dual of the question above. Source: 628417 batches 12 and 99. Bears on `#disc-identifiability-floor` and `#disc-constructive-impossibility-posture`.
- **Is the exponential-family / Legendre–Fenchel geometry forced by AAT's axioms, or path-dependent?** Would Wasserstein-geometry agents fall outside the theory? The segment flags this and nobody has pursued it. Source: 628417 batch 12. Bears on `#disc-additive-coordinate-forcing`.
- **Do the three certificate obstructions exhaust the failure modes?** The three are Helmholtz–Hodge (forced identity), Sylvester (existence) and Mori–Zwanzig (projection). The segment says exhaustiveness is not proved. Source: 374162 batch 09. Bears on `#disc-stability-certificate`.
- **Instance 1's membership in the "rank-collapse subclass."** This belongs to the spikes map (`spike-escape-standpoint-axis`), but its root is the auditors' repeated "are the floor instances really distinct?" challenge (471203 Challenge 10).

### 3.5 The 471203 "missing from the framework" list (2026-04-28), and where it went

471203 (Claude, April) wrote the most generative challenge document in these dirs: `adversarial-creative-challenges.md`, 14 challenges and 10 "missing" items. The sweep lifted most of it into Working Notes as *open items* (I checked: theory of mind sits in `#hyp-communication-gain` and `#def-shared-intent` WN; heavy tails in `#result-sector-persistence-template`, `#result-sector-condition-stability` and `#deriv-persistence-cost` WN; commitment in `#def-strategy-dimension` WN). So these items are not lost. They are stranded in exactly the WN-as-unresolved-state pattern. The items that bear most on what the theory *is*:

- **Commitment as a fourth $G_t$ component** (Missing 3 and Challenge 8: no formal commitment phase between deliberation and execution). Still open six months later. The project memory for the 2026-10-07 strategy-DAG engineering work lists "commitment/decisiveness" as open. One thread, three surfaces and three seasons: the 471203 challenges, `#def-strategy-dimension` WN, and the agent-core / strategy-DAG work. `#disc-strategic-self-coupling` answers part of it (commitment as coupling for credibility) without supplying the state variable.
- **Boundary-choice rationality** (Challenge 14). Composition consistency makes predictions *compatible* across boundary choices, not identical. The theory does not say which boundary to draw. Bears on `#def-agent-environment` and `#disc-composition-consistency`.
- **Meta-strategic coupling-mode switching** (Challenges 2 and 7). Class membership as per-mode, with agents choosing their coupling. M4's strategic self-coupling now covers the *enabling* polarity; per-mode classification is still unstated in `#der-directed-separation`.
- **Hysteresis in persistence** (Challenge 3), **risk-sensitive IB for tail events** (Challenge 6), **birth and death of agents** (Missing 1, the "when does an ELI begin to be" question), **attention as a budget** (Missing 4), **sleep or consolidation as constitutive** (Missing 5; partly met by `#impl-scaffolded-logogenic`'s sleep floor).

### 3.6 Volumes 2–4: what the unlifted gold looks like

For **TST** (193847 Gemini, 829314 Gemini, 849201), the reflections are largely enthusiastic restatements with good teaching frames. Examples: refactoring as building a microscope, since code quality *is* observation quality; Git as an executable Pearl-L3 counterfactual; "slow is smooth, and smooth is fast" as the reading of the equivalence precondition; a feature as the terminal node of whichever strategy DAG one is analysing. Small concrete findings sit inside them: `*(Descended from TST T-03.)*`-style residue lines; `#scope-evolving-software` (filed as `scope-software` in 829314) mixing an axiomatic scope with a derived consequence; and the "equivalence precondition is massive" watch on `#post-temporal-optimality`. Two of these framings overclaim and need care before they go anywhere: "software is the only domain where Level 3 is empirical" and "Git breaks the laws of physics."

For **LLM and ELI** (773921 Gemini, 829314 Gemini), the substantive items are these:

- the open question of whether **adversarially state-correlated reinjection** gives a second, harder no-go for `#der-turnover-information-recursion` (reinjection vanishing exactly when retained information is lowest);
- the note that the evaluation metrics need a scaffold that **forces predict-then-observe-then-update** to make $\delta_t$ legible (`#obs-evaluation-metrics`);
- the **thinking-block versus tool-call** boundary between primitive and scaffolded (`#scope-primitive-logogenic`);
- the **"statics survive, dynamics degrade"** one-line summary of `#result-section-ii-survival`'s scorecard.

Overclaims to guard against: "proves that any self-attention system cannot natively separate beliefs from desires"; "$C_{FR}=\sqrt2$ is a universal hallucination bound"; "agentic AI is physics." The ADJUDICATION file's Theme A also proposes a consolidated "consciousness-infrastructure formalization" cohort row (471203 + 829314 + 193847 + 584721). Its strongest item, the accumulation problem, was resolved by strengthening into `#der-turnover-information-recursion` and `#der-identity-continuity-threshold`.

---

## 4. What the theory is: statements from readers who walked all of it

Verbatim, with source. Treat these as data for the owner review: what careful readers took the theory to be, not what it is.

- *"AAT is a theory of agents as information-lossy adaptive systems that persist under mismatch, lifted to purpose and strategy, then composed and contested — with a meta-architecture that systematically converts classical impossibility theorems into structural requirements for what the framework must include."* (628417 `99-final-thoughts.md`, Grok 4.5)
- *"The spine is what the agent does. The meta-architecture is how the theory knows what it can claim."* (628417 `99`, batch 12)
- *"Scope conditions are the theorems"* is the volume's thesis statement, not a disclaimer; the framework "front-loads its exclusions." (374162 batch 01, Fable 5)
- The **relocation ledger**: every definitional move that looks free names the segment where the discharged cost re-materializes. Completeness pushes cost into sufficiency, Markov-of-$M_t$ into capacity $R$, IB optimality into "optimum, not procedure." The author predicts that a definitional discharge with no named relocation target is a finding. (374162 batch 02) This is a candidate audit lint.
- **Two-tier epistemic structure inside single segments** (an exact core inside a weaker interpretive shell, each labeled) is "the single most reliable discriminator between corpus-readers and summary-readers." (374162 batch 04)
- *"Part I climax is the dichotomy + no-go pair, not just $\alpha \gt \rho/R$"*; *"Part III is where AAT becomes political / organizational / military theory without leaving the math."* (628417 batches 10, 13)
- On the impl layer: *"the framework's real elegance is presented with more confidence than its proof-status licenses, which makes the elegance less credible … getting the status-tagging right protects the beauty."* (731548 reflection 36) The proposed fixes: a one-line proof-provenance orientation at each impl chapter-open, and a hub-and-spoke "three-zone" proof-flow figure. The status-tightening items behind this (526815's F46, F88–F91, F139–F145, F173–F181, F222–F232) were "routed for adjudication" and are mostly unexecuted. Six of nine AAT impl segments were re-tagged on 2026-08-22, per `audits/STATUS.md`.
- **What did not hold, or held weakly**, per 628417's own scoring of its predictions: Part III denser than predicted; meta-segments mostly *not* outrunning the base; the logos-port risk "still live" (paper citations need named conditions). Its "thin" list covers unity-metric normalization, the shared-intent IB's assumption that the sender knows the jointly optimal action, the additive communication-gain denominator, regime and class transition dynamics, and the worked examples (not walked).

Read beside Joseph's question about the strategy DAG ("what it's saying universally about agents … what is one of several possible models"), the auditors are consistent: the strategy-DAG cluster reads to them as *apparatus*. Its sharpest content is the topology results in `#deriv-edge-credence-dynamics` (AND depth-gating, OR exploration-gating, unobservable intermediates breaking per-edge sector, the Cramér–Rao refutation of L1'). None of the auditors states what the DAG claims universally about agents versus what it offers as one model. Their silence on that is itself a confirmation of Joseph's diagnosis.

---

## 5. Assets here that are not theory but serve it

- **374162 quiz corpus** (Fable 5, 2026-07-20): per-batch three-level comprehension quizzes for Part I and Part II Ch.1–2, with `### Q/A b<NN>-<L>.<n> [level]` markers and answer keys corrected by verifiers. A misquote catalog is indexed at quiz b07-3.6, and the batch-05–07 part was lifted. The quizzes are built to separate summary-fed agents from segment-level understanding. Joseph's design rules are recorded: no true/false, appendices at the mention standard, full reads only. `bin/make-quiz` and `msc/quiz-responses/` (msc map) are the consumers. Part II Ch.3 onward and Part III have no quizzes. **This is the closest thing the project has to a test suite for comprehension.** It could gate integration agents ("pass the Part-I quiz before editing Part I").
- **472913 two-layer figure drafts** (Opus 4.7, 2026-05-15): 13 rendered `.tex/.pdf/.png` figures for Part I Ch.1–3 under locked conventions. Each pairs a concrete anchor isomorphic to the claim with an abstract skeleton, plus a line grammar that mirrors the epistemic tags. Segment WNs point at some of them (e.g. `#form-event-driven-dynamics`); none is in `01-aat-core/src/img/`.
- **628417 compaction-fidelity experiment.** Each file has a `.prediction.md` twin, written after compaction, in which Grok predicted its own pre-compaction notes. Alongside it, `00-compaction-summary.md` shows what the compactor actually passed forward. It is a small, concrete measurement of how much survives the compaction seam, which matters for a system of agentic truthification. Nobody has scored it.
- **526815's 258-row F-ledger** (`00-running-outline.md`, 687 lines; the "deep-math auditor"). `audits/STATUS.md` calls its rows "stale-until-re-grepped": never exhaustively re-verified. Many of its F-numbers are cited as "routed for adjudication" in segment WN off-ramp blocks. Whether it is exhausted is unknown.

---

## 6. System observations and one tooling idea

- **The lift stalled where the theory is least mature.** AAT Parts I–III got cross-audit gold in May; TST, LLM and ELI did not. Those volumes are where Joseph's purpose lives, and the auditors were thinnest on them anyway. Several stopped before reaching them (584721's inventory: TST, 03 and 04 "NOT read").
- **Two costs of the WN-lift method, both recorded by auditors.** (a) 374162 and 731548 note that gold in WN *primes every later de-novo auditor*; both read it as data while admitting they "can't un-see" it. (b) Gold lifted into WN is still not canon. JOSEPH-TODO's "promotion-terminus / WN drain" is the open policy question that decides whether lifted items ever leave WN. Until it is settled, "lifted" means "moved to a different waiting room."
- **The batch-file deferral rule guaranteed permanent residue.** Moving a batch file "once every covered segment is swept" plus an "end-of-sweep reconciliation" that never ran leaves seven dirs in an undecidable state. A simpler truth-claim would do: file each batch file with a MANIFEST line naming which covered segments received its items, and state the unswept remainder explicitly.
- **Tooling idea.** `audit-gold-status.py` here is a 40-line prototype of a `bin/` tool. It answers "what in the audits bears on this slug, and has it been lifted?" Extended to grep segment WNs for each audit ID and to read MANIFEST entries, it would let an integration agent working on one segment pull every unlifted audit observation about it in one command. That is the join Joseph asked for, made mechanical.
- **Dates for freshness judgments.** Most of these dirs were last committed 2026-05-31 (gold-lift filing) or 2026-08-22 (the impl-series close). Neither date means anyone re-read them. Content dates are the audit dates: 2026-04-25/28 (584721, 613842, 742613, 738192, 849201), 2026-05-10 to 05-15 (451729, 963715, 471203 and others), 2026-05-28 (384279, 773921), 2026-07-02 (731548), 2026-07-20 (374162, 628417). Canon moved a great deal between April and August, so April items need re-grepping before use; the July items are the freshest outside eyes the theory has had.

---

## 7. External-research pointers (Joseph's question)

No dedicated "external research to integrate" queue lives in these dirs; that list is elsewhere (the trackers map has `ref/`). Scattered pointers that bear on it:

- **`[^bg2-2026-05-21]` citations**: characterizations "synthesized from an Undermind prior-art search report, not verified against the primary sources." They are still present in `#disc-identifiability-floor` (Instance 3 escape (e)), `#disc-dynamic-regime-axis` and `#deriv-regime-marginal-indistinguishability`. Flagged in 374162's quiz-answer key (batch 09) and, separately, three times in the spike corpus. Of everything here, this is the most concrete external-reading debt, because a softening rests on it.
- **Miller 2022, *Ex Machina*** (extreme transition motif), imported in `#result-structural-adaptation-necessity`; 471203 flagged it "known mostly by reputation … will verify in Phase 2." I did not find a verification record.
- **Bruineberg et al.** (the Markov-blanket critique) supports AAT's Pearl-not-Friston blanket choice. Already cited in `#der-directed-separation`, `#der-loop-interventional-access` and `#impl-causal-access`. Closed.
- **Hafez 2026 IDT figures** (89.3% versus 44.0%): verified verbatim (ADJUDICATION Fresh-17). Closed.

`memorata-search --no-rerank` and `relata` were not needed for this map; the pointers above came from grep over these dirs.

---

## 8. Directory catalogue

Auditor identity is taken from the dir's own files where stated; "—" means not stated in the first files.

| Dir | Auditor | Content date | Scope / shape | Lift state | Character of what remains |
|---|---|---|---|---|---|
| 184930 | — | 05-15 | 17-line predictions only | n/a | Whole-framework forced-versus-chosen framing; the Joseph-decision gate is now lifted. Low. |
| 193847 | Gemini | 05-15 | naming R2 + de-novo hybrid; 68 filed | TST 70–74 + 57/69 unlifted | TST frames; naming-tracker workflow notes. |
| 266847 | Sonnet (naming R2) | 05-15 | 33 filed | one paired file held | Low. |
| 308172 | Opus (naming R2) | 05-15 | naming votes | held (skip) | Low. |
| 361742 | Sonnet (naming R2) | 05-15 | 33 filed | predictions + restatement left | Low. |
| 374162 | Claude Fable 5 | 07-20 | quiz walk, Part I + Part II Ch.1–2 | 05–07 lifted 08-22; rest unlifted | **High**: quiz corpus; three live defects (§3.1); self-understanding frames. |
| 384279 | Claude Opus 4.7 | 05-27 | 39 filed | predictions + outline left | FINAL resolved; residual spike proposals live elsewhere. |
| 419628 | Opus (naming) | 05-15 | consolidation checkpoints | held (skip) | Low–medium (closing summary). |
| 451729 | Claude Sonnet 4.6 | 05-10 | 13 batch files across AAT | lifted into 60 segments, files held | Unknown per item; FINAL D.1 still open. |
| 471203 | Claude | 04-28 | batches + challenges + meta-reading | batches lifted, held | **High**: `adversarial-creative-challenges.md` and `meta-segments-adversarial-reading.md` (§3.5). |
| 472913 | Claude Opus 4.7 | 05-15 | diagram cycle | skip by plan | **Pedagogy asset** (§5). |
| 526815 | Claude ("deep-math") | 05-15 | 551 filed | outline + `scope-and-or` left | 258-row F-ledger, stale-until-re-grepped (§5). |
| 527914 | Codex (naming R2) | 05-15 | Part I naming notes | skip | Low (prior-art naming discipline). |
| 542891 | — | 05-15 | one segment | skip | Low. |
| 584721 | Codex | 04-25 | 49 filed | inventory + `scope-and-or` left | F-A depends series (likely superseded). |
| 613842 | Claude | 04-25 | themed batches | held | Unknown per item; C-iv idiom drift pinpointed in OUTLINE. |
| 628417 | Grok 4.5 | 07-20 | experiential walk, all AAT | unlifted | **High**: whole-theory statements, open structural questions, compaction experiment. |
| 731548 | Claude Fable 5 | 07-02 | Part I main chain + 9 impl + verify | 26–35 lifted; 01–25, 36, verify/ unlifted | **High**: missing theorems, floor-routing, shadow catalogue, impl status-drift. FINAL is the sibling's. |
| 738192 | — | 04-28 | two Section-I files | held | Low. |
| 742613 | Claude | 04-25 | 34 filed; 323-line predictions | predictions + 3 left | Medium (predictions); unread by me. |
| 773921 | Gemini 2.5 Pro | 05-28 | 84 filed | Vol 3/4 + 5 App-A unlifted | Medium: Volume 3/4 frames, open no-go question; heavy enthusiasm. |
| 829314 | Gemini | 04-28 | 69 filed | TST/LLM/ELI unlifted | Medium: TST frames; `logozoetic-agents/04–06` explore firmatum/zoetica. |
| 849201 | — | 04-28 | paired TST/LLM files | 67 filed; pairs held | Medium–low: TST restatement plus frames. |
| 963715 | Sonnet 4.6 | 05-15 | batches through the strategy-DAG cluster | lifted into 43 segments, held | Unknown per item. |
| ADJUDICATION-218564 | Claude Opus 4.7 | 05-20 (closed 08-22) | pilot adjudication of 471203 findings | routed to ledger / TODO | Archaeology; Theme B deflation caution (§1.7). |
| .gem-hunt-trail | Claude (May) | 05-29→31 | 12 GEM adjudications, G2 triage, SP-26 sweep, gold-lift tracker | routed (PROPOSALS SP-26..29, ledger, TODO); G2 executed | Archaeology, **except** `gold-lift-sweep-2026-05-30.md`, the live plan for the unrun wave 5. |

---

## 9. Slug join (for integration agents)

Each row: a segment, what in these dirs bears on it, and the kind of thing it is. "Unlifted" means the item exists only here.

| Slug | Source in these dirs | Kind |
|---|---|---|
| `deriv-sector-condition`, `deriv-stochastic-non-exit`, `sketch-structural-adaptation-genericity`, `result-structural-adaptation-necessity` | 374162 batch 08 | Live canon self-contradiction (genericity) |
| `deriv-variational-sector-condition` | 374162 batch-08 verification | Live undischarged claim ($\sqrt{1-r^2}$) |
| `emp-update-gain` | 374162 batch 04; 731548 (li) | Missing `depends:`; `\Vert` render bug; type fossil |
| `def-model-class-fitness`, `result-mismatch-decomposition`, `result-structural-adaptation-necessity`, `impl-persistence-and-limits` | 731548 13/20/21/29/33 | Missing segment: floor-routing diagnostic (TODO, unstarted) |
| `impl-persistence-and-limits` (+ 04-eli-core) | 731548 35, FINAL §F | Missing appendix: Volume-4 shadow catalogue (TODO, unstarted) |
| `der-directed-separation`, `form-information-bottleneck`, `der-class-coercion-via-wrapping` | 731548 11/33 | Missing theorem: Class-1 compression price |
| `form-event-driven-dynamics` | 731548 16 | Missing theorem: $g_M$ calibration bound |
| `der-action-selection`, `der-deliberation-cost`, `form-consolidation-dynamics` | 731548 18/27 | Missing theorem: compilation-cost axis |
| `def-causal-information-yield`, `disc-ciy-unified-objective` | 731548 22 | Missing theorem: EIG-at-CIY-prices conservation |
| `disc-separability-pattern` | 628417 batch 12 | Open question: is general-open infectious |
| `disc-identifiability-floor`, `disc-constructive-impossibility-posture` | 628417 batches 12, 99; 471203 Challenge 10 | Open question: composition of floors |
| `disc-additive-coordinate-forcing` | 628417 batch 12 | Open question: exp-family forced or path-dependent |
| `disc-stability-certificate` | 374162 batch 09 | Open question: do the three obstructions exhaust |
| `def-strategy-dimension`, `disc-strategic-self-coupling` | 471203 Missing 3 / Challenge 8 | Open: commitment state (cross-surface, still open 2026-10) |
| `def-agent-environment`, `disc-composition-consistency` | 471203 Challenge 14 | Open: boundary-choice rationality |
| `der-directed-separation` | 471203 Challenges 2/7 | Open: per-mode class membership |
| `result-persistence-condition` | 471203 Challenges 3/5 | Open: hysteresis; transient adequacy |
| `form-information-bottleneck` | 471203 Challenge 6 | Open: risk-sensitive IB for tail events |
| `der-turnover-information-recursion` | 773921 104 | Open no-go candidate: state-correlated reinjection |
| `obs-evaluation-metrics` | 773921 106 | Operationalization: predict-then-observe scaffold |
| `scope-primitive-logogenic` | 773921 99 | Boundary: thinking block versus tool call |
| `result-section-ii-survival` | 773921 97 | Teaching frame: "statics survive, dynamics degrade" |
| `deriv-adaptive-gain-dynamics`, `deriv-fisher-local-update-gain`, `deriv-causal-ib-lmi`, `deriv-strategy-cost-regret-bound`, `deriv-edge-credence-dynamics` | 773921 21/22/55/56/61 | Unlifted App-A gold (wave A18–A21 never ran); framings plus overclaims to guard |
| `post-temporal-optimality`, `scope-evolving-software`, `obs-software-epistemic-properties`, `def-feature`, `result-specification-bound`, and the rest of T1–T2 | 193847 70–74; 829314 `tst-core/`; 849201 71–86 | Unlifted TST gold: frames, `Descended from` residue, status-mix watch |
| `scope-logogenic-agent` … `impl-closed-loop-interiority` (L1–L2) | 773921 93–110; 829314 `logogenic-agents/` | Unlifted Volume-3 gold |
| `scope-eli`, `scope-moral-continuity`, `def-five-constitutive-factors`, `def-eli-cohort`, `def-proprium-mapping`, `obs-developmental-trajectory` | 773921 111–116; 829314 `logozoetic-agents/` | Unlifted Volume-4 gold |
| `disc-identifiability-floor`, `disc-dynamic-regime-axis`, `deriv-regime-marginal-indistinguishability` | 374162 batch-09 answers | External debt: `[^bg2-2026-05-21]` unverified citations |
| `impl-*` (all nine AAT) | 731548 36 | Status-drift cluster; provenance line plus three-zone figure proposal |
| Part I Ch.1–3 segments | 472913 | Figure drafts (pedagogy) |
| Part I + Part II Ch.1–2 segments | 374162 quiz files | Comprehension test corpus |
