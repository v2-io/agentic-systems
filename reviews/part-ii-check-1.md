---
kind: review
author:
  name: Claude Opus 5.5 (Part II integration, independent checker 1, cross-cutting)
  role: independent checker
sources:
  - msc/inside-out-2026-10/part-ii-integration.md
  - reviews/part-ii-integration-1.md
  - reviews/part-ii-check-1-identification.md
  - reviews/part-ii-check-1-distortion.md
  - reviews/part-ii-check-1-b1-records.md
  - msc/inside-out-2026-10/influx-scout/MAP.md
written: 2026-10-30
---

# Part II integration, check 1: the cross-cutting record

KR **C.2** (C2 and C3, independently checked, then landed or refuted), **B.1** (Part II's claim records) and **C.1** (every verified defect replaced, then independently verified), under the top intent "Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself." This record covers the landing `253d2bca`..`279b2699` as read at `6511154d`. Its three companions carry the per-cluster derivations: `reviews/part-ii-check-1-identification.md` (C2), `reviews/part-ii-check-1-distortion.md` (C3) and `reviews/part-ii-check-1-b1-records.md` (`8f7dd870`). This record holds what crosses them: carriers of retired statements that the drains missed, the A5 relettering, the Hafez figures checked against the abstract, a synthesis on the event pin that none of the three states whole, and the ledger state. The account for a reader is `msc/inside-out-2026-10/part-ii-check-1.md`.

What I did, so the record can be weighed. Ran: `bin/refresh-all --check` (all generated outputs current), `bin/lint-outline` (clean), `md-press` over every Markdown file the five commits touched (nothing would change), `vsect check --strict`, the integrator's `check-integration-1-deterministic-nogo.py` and `check-feedback-1-lemma1b-pstream.py`, and the identification checker's `nogo-scope`, `right-rung-rh-not-in-pi` and `kappa0-action-collider` scripts (each reproduces as reported). Re-derived by hand: the distortion checker's three results it asked a second mind for (the global Fisher–Rao constant $2$, the recalibration identity, and the reliability identity for the retired numerator), and the B.1 checker's two right-rung instances. Fetched: the arXiv abstract page of 2603.01283 (v3). Searched: the whole repository with `rg`, excluding the archaeology layers (`.archive/`, `.integrated/`, `audits/`, `spikes/`, `reviews/`, `CHANGELOG.md`, `LOG.md`), for every retired statement the account names. Not done: I did not read the C2 or C3 spike files, and I opened none of the cited literature.

## C1 (check)
- target: segment:der-causal-hierarchy-requirement
- act: read-check
- line: imported
- criterion: The Hafez figures as the body now states them: Hafez, Reid & Nazeri 2026, arXiv 2603.01283, *The Informational Cost of Agency*; the Information Digital Twin detects 89.3% of coupling degradations against 44.0% for reward-based monitoring, with 4.4 times lower latency, across 21 trained continuous-control agents.
- committed: after
- at: 6511154d
- read: segment:der-causal-hierarchy-requirement
- outcome: confirmed
- recheck: fetch `https://arxiv.org/abs/2603.01283` and read the abstract

Checked at the primary's abstract page (v3, revised 14 May 2026). The title, the three authors, "detects 89.3% of coupling degradations", "44.0% for reward based monitoring", "4.4 times lower latency" and "21 trained continuous control agents" are all as the body says. Neither "perturbation" nor "accuracy" appears in the abstract. The paper's setup was not read here either, so the figures stand at abstract granularity, as the body says they do. Two sites still carry the old wording (F7).

## F1 (finding)
- target: segment:impl-common-roots

**The retired product law is still stated in the body at `:27`.** `279b2699` calls `:41` "the last product-law carrier". But `:27`, a body paragraph (Working Notes begin at `:57`), still reads "$\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa_{\text{processing}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$" and "the bound *operationalizes prompt engineering* as $\mathcal{A}$-reduction: $\kappa$ is fixed for a Class 3 substrate …, $\mathcal{A}$ is variable …, and reducing $\mathcal{A}$ tightens the bound proportionally." That is the whole retired law, numerator and lever included. `:25` in the same segment states the replacement correctly, so the two paragraphs now contradict each other. Repair: restate `:27` in the replacement's terms. The goal-dependence displacement is bounded in $\kappa H(G \mid e_\tau, M_{\tau^-})$. The distortion is bounded model-free by the size of the reweighting, and under the fixed-gain hypothesis it is the gain times the residual spread of the goal-relevant quantity. The prompt-engineering lever is then the residual spread, under that hypothesis only.

Same carrier outside this segment: `#result-section-ii-survival` `:145` (Working Note) and `#impl-orient-cascade` `:77` (Working Note) carry "$\lVert\Delta M_{\text{bias}}\rVert \leq C\kappa I$" in its retired linear form. This is the "two scalings" half of influx item D11 (`influx-scout/MAP.md` §2 $\kappa$ row and §3 D11; source `influx-scout/neurips.md` §2.D). The integration answered D11 in the two segments it rewrote. It did not answer it at these three sites.

## F2 (finding)
- target: segment:result-section-ii-survival

**$\Delta M_{\text{bias}}$ now has two incompatible definitions in canon, and the survival result bounds one with the other's bound.** `#deriv-observation-ambiguity-bias-bound` `:24` defines $\lVert\Delta M_{\text{bias}}(G)\rVert$ as the distance between the goal-conditional and the goal-marginal post-update laws, and its regression guard `:180` says not to describe the bound "as bounding bias relative to the goal-blind update". `#result-section-ii-survival` `:114` defines $\Delta M_{\text{bias}} = f_X^M(X_{\tau^-}, e_\tau) - f_M(M_{\tau^-}, e_\tau)$, the coupled update minus the goal-blind update. `:118` then bounds $\mathbb E\lVert\Delta M_{\text{bias}}\rVert_{FR}$ by $\sqrt{2\kappa H}$, which is the appendix bound applied to the other quantity. The prose between them describes the appendix's quantity correctly, so the display and the prose disagree. Downstream, `#result-coupled-diagnostic-framework` `:81`–`:85`, `#scope-scaffolded-logogenic` `:28`, `#impl-scaffolded-logogenic` `:28` and `#impl-orient-cascade` `:48` all compare a coupled diagnostic with the "clean (goal-blind)" one through $L_A \lVert\Delta M_{\text{bias}}\rVert$. That needs the coupled-minus-goal-blind quantity. Two of those sites then cite the goal-dependence bound for it.

The three are different quantities, and this integration's own frame separates them. Goal-dependence is the coupled update's own goal-conditional against goal-marginal laws. Distortion is the departure from the calibrated belief. Departure from *the goal-blind update* is a third quantity: by V7 (in `#der-directed-separation`), an action-free goal-blind update is itself per-goal miscalibrated, and by the distortion checker's F1 it is miscalibrated whenever the goal carries world information. So "coupled minus goal-blind" is neither distortion nor goal-dependence. Repair: give the survival result and the diagnostic framework the quantity their argument uses, and state which bound applies to it. For "how wrong is the coupled diagnostic", that is the distortion, bounded by `#scope-observation-ambiguity-modulation`'s range bound (and Bennett, per the distortion checker's F4). For "how much does the diagnostic vary with the goal", it is the appendix's displacement. Rename one of the two symbols, so that $\Delta M_{\text{bias}}$ means one thing.

## F3 (finding)
- target: segment:disc-adversarial-coupling-pressure

**`:22` contradicts `:103` in the same segment.** `:103` was rewritten in `18f1bb4e`: the adversary engineers the residual spread, and the displacement bound of `#deriv-observation-ambiguity-bias-bound` "is not the adversary's lever". `:22` (unchanged) says a Class 1 agent's adversary's "only attack channel is engineered observation ambiguity, and the bias they can induce is bounded by `#deriv-observation-ambiguity-bias-bound`'s constant $C$ relative to the ambiguity they can manufacture." That retains both retired readings: ambiguity as the factor, and the appendix as a bound on induced bias. For a Class 1 agent, moreover, the goal-dependence displacement is zero whatever the adversary does. Repair: for Class 1, the adversary's channel is the event stream, and what it can induce is miscalibration of the model's likelihood (misspecification), not goal-attributable distortion; the distortion bound of `#scope-observation-ambiguity-modulation` is about Class 3 processors.

## F4 (finding)
- target: segment:der-orient-cascade

**The B.1 C16 carrier "the ordering is forced" is not drained.** The integrator's C6 says the convention paragraph was drained. `:91` still reads "The cascade's *ordering* is convention-independent (forced by information dependency)". The B.1 checker's C16 named that exact sentence; only the first three steps are forced, and objective-last is a recommendation. Other carriers of the same sentence: `#impl-orient-cascade` `:77` (Working Note: "the cascade *ordering*-exactness in `#der-orient-cascade`, which is forced by information dependency … so `#der-orient-cascade` needed no edit"); `terminology/entries/orient-cascade.md` `:18` ("The ordering is *forced by information dependency*"), which generates `LEXICON.md`; and the source comment in `01-aat-core/src/img/orient-cascade.tex` `:7`. Repair: in each, "the first three steps are forced by information dependency; objective revision last is a recommendation," matching `#impl-orient-cascade`'s heading `:28`.

## F5 (finding)
- target: segment:impl-causal-access

**A5's relettering did not reach this segment, and NOTATION's "declared once" is not yet true.** The account's §4 check says `rg "(C[123])" 0*-*/src` should show only the wrapper, recursive-update and continuation families. It does not:

- `#impl-causal-access` still names the identification conditions "(C1) positivity / (C2) sequential ignorability / (C3) known action-mechanism" in its body, at `:25` (proof provenance), `:29`, `:31`, `:39` ("the positivity condition (C1) read as an ontology"), `:45`, and in Working Notes at `:77` and `:78`. Its own regression guard at `:81` says those conditions "carry their standard names". `#impl-persistence-and-limits` `:85` (body) says "identification gated on its (C1)–(C3)". The same family survives in Working Notes at `#scope-agent-identity` `:68` and `:71` and at `#def-value-object` `:227`. The third member is now *consistency*, so "(C3) known action-mechanism" also names the old condition. (`#disc-sandbox-evaluation-ceiling` `:72` names Paper 2's own triple, which is a citation, and can stay.)
- `NOTATION.md` `:198` says every lettered family is declared there once, and the integrator's account says the same. Five more (C1)–(C3) families in canon are not declared: `#der-multi-timescale-stability` (also used by `#impl-persistence-and-limits` `:71`), `#deriv-critical-mass-composition`, `#form-composition-closure` (the bridge-lemma conditions), `#der-turnover-information-recursion`, and `#scope-emergence-conditions`. KR F.4 ("every index family is declared once in `NOTATION.md`") is not met.

Repair: drain the identification family at the sites above to the standard names, and add the five families to the NOTATION table, or reletter them.

## F6 (finding)
- target: segment:hyp-truth-serving-loophole

**The hypothesis's premise is a statement of the degradation norm that the integration retired.** `:15` reads the norm as "less goal-to-belief coupling tracks reality strictly better, all else equal". `:23` says "the degradation norm treats $\lVert\Delta_G\rVert$ as pure loss", with $\Delta_G$ measured against "the goal-blind update" $f_M^0$. `:51` says the norm "acquires a qualifier: *for goals not truth-serving*". After the landing, `#der-directed-separation` says the norm is true of distortion, silent on allocation, and evaluated by per-goal calibration. That already permits the goal-as-evidence Bayesian (Record 4 False-of) and calibration-preserving allocation. Much of claim (i) of the loophole is therefore absorbed by the new Scope Condition. The reference update $f_M^0$ is also the wrong comparator: an action-free goal-blind update is per-goal miscalibrated (V7). The segment is `status: sketch` and says it is exploratory, but it `depends:` on `#der-directed-separation` and states that segment's content. Repair: restate the premise against the new norm. What remains of the loophole is then sharper. A truth-serving goal makes goal-dependence *calibration-seeking* (allocation toward the hardest-to-predict quantities, or the goal used as evidence), which the new norm already admits. The open part is whether a goal-declared (rather than goal-blind) Class 3 agent can be *certified* calibrated from its declaration, which is a question about the probe-law $\kappa$ of the distortion checker's F3.

## F7 (finding)
- target: segment:der-architecture-noidentifiability

**Two Hafez sites still carry the old wording; the follow-up's "all sites now say" overstates.** `:179` (Discussion, "Multi-agent / Hafez bridge"): "its 89% perturbation-detection performance". `#disc-sandbox-evaluation-ceiling` `:45`: "the bi-predictability anchor at $89\%$ vs $44\%$ detection accuracy". The abstract says "coupling degradations", not perturbations, and does not report an accuracy (C1). `#der-directed-separation` `:296` (Working Note, lifted audit gold) paraphrases "89% vs 44% perturbation detection". The account calls it a quoted auditor line, but it is a paraphrase in the note's own voice. The Volume 4 carrier (`#obs-growth-vs-drift` `:50`) is the integrator's open F3. Repair: the abstract's wording at both body sites, and either quote the auditor or correct the paraphrase.

## F8 (finding)
- target: segment:deriv-observation-ambiguity-bias-bound

**Three things in this appendix bear on influx items, and one is a ghost in the body.**

(a) *History in the body.* Epistemic Status `:130` says "A previous version of this derivation bounded the same displacement by $I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$ … The present form is Paper 3's". `#scope-observation-ambiguity-modulation` `:66` does the same: "The classification is the one this segment has carried since its first version; what changed is the carrier. It was previously stated through …". Under integration-is-replacement and the effort's standing ("History goes in commit bodies and `CHANGELOG.md`, nowhere else"), these belong in the history layers. The demonstration that $I(G; \Omega \mid \cdot)$ is zero where goal-dependence is a defect is present truth, and it should stay. The narration of the earlier version should go.

(b) *D10 can now be closed (`influx-scout/MAP.md` §3 D10; source `influx-scout/neurips.md` §2.D, Paper 03 App D and the August `information-bound-saturation` spike).* Honest failure mode 4 (`:141`) says a global Fisher–Rao statement needs compactness or staging, and that "Paper 3 states a global $C = 2$ … unread here and not adopted". The distortion checker's F5(b) derives $\mathbb E_G\, d_{FR} \leq 2\sqrt{I}$ in three lines with no (H4) and no compactness. I re-derived it independently. Rényi monotonicity gives $-2\log\mathrm{BC} \leq \mathrm{KL}$; $\log\cos\theta \leq -\theta^2/2$ on $[0, \pi/2)$ because $(\log\cos)'' = -\sec^2 \leq -1$; so $\theta \leq \sqrt{\mathrm{KL}}$, $d_{FR} = 2\theta \leq 2\sqrt{\mathrm{KL}}$, and Jensen over $G$ finishes. The influx records the tighter form $\mathbb E\, d_{FR} \leq 2\arccos(e^{-I/2}) \leq \min(2\sqrt I, \pi)$ and a saturation no-go (every bound $F(I)$ must approach the diameter $\pi$). Those were verified only by their own chain. The $2\sqrt I$ half now has two derivations outside that chain. The arccos form follows from the same first inequality ($\mathrm{BC} \geq e^{-\mathrm{KL}/2}$) and concavity, which I have not checked beyond that line. This depends on the distortion checker's F5(a) convention fix ($d_{FR} := 2\arccos\mathrm{BC}$).

(c) *D12 (`influx-scout/MAP.md` §3 D12; canon citing unpublished NeurIPS papers in bodies).* The landing added two such body citations here: `:44` ("NeurIPS 2026 Paper 3's Lemma 5.1 is this step") and `:103` (Paper 3's Corollary 4.4). It also kept `:130` ("The present form is Paper 3's") and `:141`. The derivation is self-contained without them. Under D-1 they belong in Working Notes.

## F9 (finding)
- target: segment:disc-anti-collapse

**`:36` still carries the retired quantity in its label, and narrates history in a body.** The bullet's label is "$\kappa$ (coupling) vs $\mathcal{A}$ (observation ambiguity)". The text under it was rewritten (gain times residual spread under the fixed-gain hypothesis) and then narrates: "The segment's own history is the discipline caught in the act twice: an earlier formulation conflated …, and the formulation that replaced it carried an 'ambiguity' factor …". The anti-collapse lesson is real and worth keeping, stated as the present lesson rather than as the segment's history: the same reach for the wrong knob, made twice. Repair: relabel the bullet "$\kappa$ (the processor's coupling) vs the residual spread the observation leaves", and give the lesson without "earlier formulation".

## F10 (finding)
- target: segment:scope-observation-ambiguity-modulation

**Carriers of the retired product law outside `src/` that the follow-up's drain did not reach.**

- `doc/vivarium.md` `:39`: "is the $\kappa \cdot \mathcal A$ bias bound with $\mathcal A$ (observation ambiguity) as an authored quantity".
- `TODO.md` `:453` and its ledger item `item:todo-loga-2-kappa-text-processing-approx-1-sc-b641`: "Keep effective-bias gating via $\kappa \cdot \mathcal A(e)$ as the precise claim". The item's real concern, the scope of $\kappa \approx 1$, still stands. Its stated "precise claim" is retired.
- `01-aat-core/OUTLINE.md` `:96`: "ambiguity-gated bias bounds". `:80`: "the Class 3 (Coupled) bias bound underlying the approximate-survival category is now a conditional theorem". After the landing, the survival result's own text says the approximation *error* is governed by the distortion, whose sharpness dependence is a hypothesis. The conditional theorem bounds goal-dependence, not that error.
- `03-llm-core/OUTLINE.md` `:22` and `:101`: "the bias bound is reduced (but not eliminated) by ambiguity-reduction interventions".
- `questions/notation-lists-mathcal-a-only-as-the-action-spac.md` asks whether the ambiguity factor should get its own NOTATION row. The quantity is retired, so I answer it in this cycle.

## F11 (finding)
- target: segment:der-directed-separation

**The event pin, the declined L0 and the regression guard contradict each other, and the contradiction is the interior-action loophole in information-theoretic form.** The integrator declined the C3 spike's L0 (add $a_t$ to the conditional independence) because "with the action in the set and a policy injective in the goal, the independence holds for every update, distorting ones included, and the $\kappa$ denominator vanishes" (`:269`). In the same landing it pinned $e_\tau$ to include the action completion (`:53`). So the conditional independence of the first Claim Record, "true as written with $e_\tau$ including the action completion" (`:269`), *is* the vacuous L0 version. The distortion checker's C6 and F3 show the consequence: $\kappa_{\text{processing}}$, causal discipline, and the appendix's displacement all degenerate under the operating law for any injective policy. The identification checker's F3 shows the other side: drop the action from the update and the collider at $M_t$ reopens at $\kappa = 0$ exactly. Under the operating law, no reading of the event makes "$\kappa_{\text{processing}} = 0$" carry both the no-port fact and the no-collider fact.

This is the influx's verify item 5 (`influx-scout/MAP.md` §3, "Verify before landing" 5; source `influx-scout/rewrites.md` row 8 and the paragraph at `:150`, from the aat-refactored rewrite). A Class 3 agent can record goal-driven processing as a goal-chosen interior action, feed it to a goal-blind update, and pass the separation test trivially. The pin generalizes the loophole from interior actions to every action that encodes the goal. My reading of how the parts of the repair divide is reasoning, not run:

- The distortion checker's probe-law $\kappa$ (its F3) removes the degeneracy. It does not close the interior-action loophole: the probe holds $e_\tau$ fixed, interior action included, so a goal-chosen interior action that carries the processing still reads $\kappa = 0$. Closing that needs rewrites row 8's typing: interior and processing actions count as processing for the separation test.
- The calibration criterion does close it, once corrected per the distortion checker's F2 (the defect is miscalibration, not departure). A goal-chosen interior action that tilts the belief yields a report that is miscalibrated under the goal's law, whatever the wiring. Allocation recorded as an interior action stays calibrated when it is ignorable.

So the integration's move to calibration as the invariant answers verify item 5 *for the norm*. $\kappa$ and causal discipline remain open to it until interior actions are typed. The identification checker's F3 repair (make the event clause part of premise 1) and the distortion checker's F3 repair (the probe law) are two halves of one fix. Whoever lands them should land them together, with the interior-action typing as the third piece.

## F12 (finding)
- target: segment:der-loop-interventional-access

**The ledger commit's "revise events for every segment edited in the two commits" is not what the store shows, and the record carries pre-rebase hashes.** `vsect check --strict` lists 19 unclassified edits: a version change on which recorded checks rest, with no reworded/redefined claim. Fourteen are on segments these commits edited: `def-agent-spectrum`, `def-satisfaction-gap` (`b25e6d1d`→`cfef16ee`), `def-strategy-dag`, `der-causal-hierarchy-requirement`, `der-causal-insufficiency-detection`, `der-class-coercion-via-wrapping`, `der-loop-interventional-access` (`70e91431`→`cc8fd2e9`), `der-observability-dominance`, `der-orient-cascade`, `deriv-self-actuation-grounding`, `deriv-update-detection-latency`, `form-objective-functional` (`ee71e369`→`99b4ff43`), `norm-explicit-strategy-condition` and `schema-strategy-persistence`. The integrator's own `rederive` events bind to the new versions. The earlier checks that read the old ones (mostly the B.1 checker's) wait with the edit unclassified. Whether each edit was a rewording or a redefinition is the reviser's claim to make (`vsect revise`), and a second mind's `confirm` judges against that claim; I have not classified them. Separately, `1dec6130`'s and `18f1bb4e`'s bodies, `reviews/part-ii-integration-1.md` C8, `CHANGELOG.md`, `spikes/INDEX.md` and both spike READMEs cited worktree hashes that are not on main: `af518dd5`, `afc1840b`, `6d4dec34`, `d981c5bb`. These correspond to `253d2bca`, `8f7dd870`, `1dec6130` and `18f1bb4e`; patch-ids are identical for two, and the other two differ only in rebase context lines. I corrected the four editable files in this cycle, and annotated C8 in the store. Commit bodies cannot be corrected.
