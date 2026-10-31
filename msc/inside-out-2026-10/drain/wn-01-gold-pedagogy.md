# Drain: the pedagogy categories of the 01-aat-core audit gold

*Serves **I.9** (each backlog surface drained, one disposition per source item), and through it I.5 (the gold leaves Working Notes) and the pedagogy home (`item:pedagogy-home-for-lifted-audit-gold`). Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." This is a fork's part of the gold-lift drain, merged into `wn-01-gold.md`. Checked against the working tree at asf `6b794d51`, 2026-10-30, after the four integration lanes merged.*

## What was read, and how

**Read whole:**
- the 202 Candidate Brief items (scratchpad `cat-brief.md`);
- the 263 Candidate Discussion items (`cat-discussion.md`), including the 2026-08-22 "teaching frames" bullets of `#impl-strategy-structure`;
- the 99 Candidate figure items (`cat-figures.md`);
- the "Teaching frames and implications (audit gold, lifted 2026-08-22)" block of `#impl-persistence-and-limits` (Working Notes lines 104–136; 19 bullets). The extractor missed it because it is not under an `Incidental audit gold` heading.

**Checked against the bodies (Working Notes excluded):**
- About 75 distinctive phrases from the gold were grepped over every segment body in the four volumes (the script is `ped-bodygrep.py` in the scratchpad). Each hit was taken as a candidate "landed" and read at the line where it mattered.
- A claim-level check was made, at the cited line, for every item listed in (a) and (b) below.

**What this does not establish:**
- A grep miss means the wording did not land. The idea may have landed in other words.
- Items not named in (a), (b) or (c) were read but not individually checked against their segment's body. Their disposition is the category default: they go to the pedagogy home, unverified.
- The "Readers often ask" items are the sibling fork's (`wn-01-gold-readers.md`). The Belongs-elsewhere items are the other fork's (`wn-01-gold-belongs.md`).

## (a) Pedagogy that rides on a claim canon has since corrected

These must be rewritten or dropped before they teach anything. All were raised as one event on `item:pedagogy-home-for-lifted-audit-gold`. Line numbers are the Working Notes lines in the scratchpad extraction.

| item (segment, WN line) | what it says | what canon now says (at `6b794d51`) |
|---|---|---|
| brief#74 (`der-tempo-composition`, 148) | $C_{\text{coord}} = \sum_i \mathcal T_i - \mathcal T_c$ as a first-law "conservation" | $C_{\text{coord}} := \mathcal T_{\text{joint}} - \mathcal T_c$ (line 39); the unconditional $\mathcal T_c \le \sum_i \mathcal T_i$ is retired (WN 128 regression guard) |
| discussion#88 (`der-team-persistence`, 136) | "the additive-tempo upper bound under channel independence" | the additive form is exact under independence only; the upper-bound reading is refuted (`#deriv-tempo-additivity`; misquotation catalog item 6 in `#impl-persistence-and-limits`) |
| figures#39 (`der-tempo-composition`, 165) | draws $\sum_i \mathcal T_i$ as the inflow that $C_{\text{coord}}$ diverts | same: the inflow is $\mathcal T_{\text{joint}}$ |
| figures#4 (`def-adaptive-tempo`, 93) | subtract-CMI-overlap stage | already annotated in place as refuted (no-go N1); keep the annotation |
| brief#86 (`deriv-sector-condition`, 419) | past $R$, "$\dot V$ goes permanently positive"; "a hard threshold" | below threshold the certificate is lost; escape is certified only in radially tight cases (Lemma A.1N; misquotation catalog item 3) |
| brief#173 (`result-sector-condition-stability`, 73) | "they all failed because $\alpha \lt \rho/R$" | same; failing the condition is loss of the guarantee, not a demonstrated cause |
| discussion#93 (`deriv-critical-mass-composition`, 233) | $C \gt \alpha$ "guarantees structural collapse" | same; also the implication map's "settled" voice (`item:todo-impl-series-status-tagging-pass-b-4-rema-11e6`) |
| discussion#72 (`der-gain-sector-bridge`, 158) | beyond the basin "the gradient reverses, the agent goes insane" | the basin-boundary regression guard in `#impl-persistence-and-limits`'s teaching block names this gloss as an overclaim: beyond $R$ maladaptation is permitted, not implied |
| brief#57 (`der-directed-separation`, 289) | $\kappa \approx 1$: "a pure ideologue (or a transformer)… beliefs are downstream projections of goals" | goal-dependence is not distortion: allocation is permitted, distortion forbidden (`#der-directed-separation`:58–59; the estimator measures goal-dependence, not distortion, :106) |
| discussion#68 (`der-directed-separation`, 293) | "$\kappa_{\text{processing}} \gt 0$ is the formal definition of motivated reasoning / sycophancy" | motivated reasoning is a tilt with $\lambda \gt 0$ (`#scope-observation-ambiguity-modulation`:96), a distortion; $\kappa \gt 0$ alone is not it |
| discussion#155, #157 (`form-complete-agent-state`, 92, 94) | goal-driven attention means $f_M$ "is conditioned on $G_t$: motivated perception"; leakage = sycophancy | same distinction. #157 also has the gain backwards ("$\alpha \to 0$ as $U_M \to \infty$"; $\eta^\ast = U_M/(U_M+U_o)$ rises with $U_M$) |
| discussion#259 (`scope-multi-agent`, 101) | goal-dependent routing makes the organization "a Class 3 (Coupled) agent" with "institutional confirmation bias" | Case 2 of `#hyp-directed-separation-under-composition` gives a Class 2 composite, and dependence is not distortion |
| brief#147, discussion#192 (`impl-orient-cascade`, 92, 96) | scaffolding is "structurally necessary" and "recovers the Lyapunov persistence guarantees" | `item:the-scaffolding-overclaim-in-volume-3-its-origin`; brief#147 is already annotated in place |
| discussion#96 (`deriv-discrete-sector-condition`, 217) | latency forces lower $\eta^\ast$ "even when the model is perfectly certain ($U_M \approx 0$)" | a certain model already has low gain; the intended case is reliable observation ($U_o \approx 0$) |
| discussion#13 (`def-chronica`, 79) | "the Three Deaths" | retired name; "the deaths" (`#def-death-as-factor-loss`) |

Riders where canon has an open item, raised there:
- brief#125, the stability-plasticity "vise", rests on the undefined upper bound: `item:todo-stability-upper-bound-for-form-consolida-be13`.
- brief#126, "boredom and surprise", reads $\mathcal I(e_\tau)$ as a realized quantity: `item:expected-vs-realized-information-symbol`.
- brief#167 and #168 and discussion#219, "survival is a `min()`", presuppose the conjunctive boundary: `item:weakest-link-needs-conjunctive-failure-boundary`.
- brief#178, $\varepsilon_x = 0$ "regardless of $U_M$", omits F154's invariance hypothesis: `item:todo-def-unity-dimensions-a13-f146-u-m-i-h-no-6bb8`.
- brief#123, "a society is a valid macroscopic entity iff …", takes the region-fit condition (`#form-composition-closure`:147) for the whole composite criterion: `item:todo-der-class-coercion-in-composition-a12-f1-4890`.

Overreach that is not wrong, which a test reader should see flagged: brief#53 ("proves why markets consistently outperform bureaucracies"), brief#135 ("proves why micromanagement fails"; the segment is a hypothesis and F162 is open), and discussion#189 and #215 (squared law read as "initiative is decisive" and "monopoly formation"; coupling-dominant class only, `item:readers-ask-result-adversarial-tempo-advantage`).

## (b) Theory or defects filed as pedagogy

| source | content | disposition |
|---|---|---|
| discussion#13, figures#9 (`def-chronica`) | fork-undetectability: lossy $\phi$ ∘ non-forkable $\mathcal C_t$ ⇒ a fork is not detectable from $M_t$; with a drafted figure | **true, not in canon** (no body states it) → raised on *existing* `item:proposals-surfaced-2026-05-29-qualitative-gem-hunt-14e1` (SP-27) |
| `impl-persistence-and-limits` teaching block, shadow catalogue + five-failure-modes-as-deaths | eleven Part-I/Volume-4 pairs | → raised on *existing* `item:todo-volume-4-shadow-catalogue-appendix-final-50be` (G.0) |
| same block, "environment selection as the unnamed zeroth strategy" | agents choose $\rho$ by choosing worlds | **not in canon** → `item:environment-selection-as-adaptive-strategy` (C.4) |
| same block, "mood as a surrogate-objective bridge" | `#der-mood-timescale` optimizes tracking MSE, a surrogate, without saying so | **present** → `item:mood-timescale-optimizes-a-surrogate` (C.1) |
| same block, self-modification slowest loop; graded commitments over hard rules | Volume 3–4 readings | → raised on `item:eli-reach-from-01-audit-gold` |
| same block, session-bounded deliberation | thinking-token budgets as $\Delta\tau^\ast$ | → raised on `item:llm-instantiations-from-01-audit-gold` |
| same block, the rate-ladder notation box | $\eta^\ast$ → $\mathcal T$ → $\alpha_{\text{time}}$ | already in `item:readers-ask-result-persistence-condition` |
| same block, basin-boundary regression guard | "goes insane" overclaims | **regression guard**: keep at I.5; it is the reason discussion#72 is a rider |
| discussion#2 (`def-action-transition`) | $\Omega$-side Markov augmentation is free, $M_t$-side meets the capacity wall | **not stated** (line 49 states the $\Omega$ commitment only) → raised on `item:readers-ask-def-action-transition` |
| discussion#124 (`disc-additive-coordinate-forcing`) | escapes cost framework-wide commitments | → raised on `item:identifiability-floor-escapes-compose-and-cost` |
| discussion#232 (`result-structural-adaptation-necessity`) | IB vs structural reserve, "perfect compression is brittle" | → raised on *existing* `item:ib-target-horizon-vs-structural-reserve` |
| discussion#38, #175, #201, #258 | five/six-mechanism shallow-plan convergence | → raised on `item:assemble-plan-depth-penalty-convergence` |
| discussion#123 (`disc-additive-coordinate-forcing`) | "the only coherent geometry respecting additivity and invariance" | speculative; the question it asks is *existing* `question:coordinate-forcing-geometry-forced-or-path-dependent` (not raised: `raise` takes items) |
| discussion#22 (`def-model-sufficiency`) | exploration shatters sufficiency (a conservative policy gets $S=1$ trivially) | consistent with policy-relative $S$; pedagogy |
| discussion#227 (`result-sector-condition-stability`) | increasing $R$ often depresses $\alpha$ | an empirical-tendency claim with no canon home; pedagogy, flagged as unverified |
| discussion#241 (`schema-strategy-persistence`) | "learning-rate annealing is fatal for long-lived agents" | the forgetting prerequisite is canon (:17–19); the annealing phrasing is NeurIPS Paper 2's, cited only in Working Notes; pedagogy, with the non-stationarity scope stated |
| figures#33, #42, #49, #69, #71, #93 | figures drawn to carry an off-ramp finding (precedence flow, $\alpha'/\beta'$ fork, residual fan-out, ambient supergraph, type-check gate, attempt-vs-success typing) | pedagogy whose guardrail is the finding; each finding is in the ledger via the main file's Off-ramp and Follow-up tables |

## (c) What has already reached a body

Found in a body at `6b794d51`, by phrase grep plus a read at the line:

- **Briefs:**
  - "perpetual experiment" (`#der-loop-interventional-access`)
  - "outrun a bad observation channel" (`#def-adaptive-tempo`)
  - "peace or deafness" (`#def-mismatch-signal`, `#hyp-solicitable-escape`)
  - the AND/OR "same magnitude, opposite signs" (`#def-strategy-dag`)
  - "mathematics of panic" and the consultant/employee distinction (`#cooperative-adversarial-intro`)
  - the Brooks inequality $\Delta\varepsilon^\ast\nu_c/\lVert\delta_{\text{critical}}\rVert \gt \Delta\mathcal T_i$ (`#der-tempo-composition`:98)
  - Commander's Intent (`#def-shared-intent`)
  - System 1 and fluency, and the chess gloss (`#der-action-selection`)
  - the sibling analogy (`#scope-agent-identity`)
  - "survival is a `min()`" (`#impl-persistence-and-limits` body)
  - "infinite memory" (`#schema-strategy-persistence`)
  - the bathtub (`#persistence-and-limits-intro`)
  - the gain-times-spread factorization (`#impl-orient-cascade`:52, now as the fixed-gain hypothesis)
  - $\delta_s$ versus $\delta_{\text{strategic}}$ (`#def-strategic-calibration`:54)
- **Discussion:**
  - "tragedy of agency" (`#causal-access-intro`)
  - `git checkout` as Level 3 (`#def-pearl-causal-hierarchy`)
  - Clausewitz's three gaps (`#def-unity-dimensions`)
  - micromanagement as a Tikhonov violation (`#der-temporal-nesting`)
  - OKRs (`#disc-credit-assignment-boundary`)
  - Maxwell's demon (`#deriv-persistence-cost`)
  - the echo chamber (`#deriv-tempo-additivity`, `#der-team-persistence`)
  - Kuhn (`#result-structural-adaptation-necessity`)
  - the paperclip and cancer contrast (`#der-bounded-objective-as-sanity-criterion`)
  - the dark room (`#def-satisfaction-gap`, `#disc-ciy-unified-objective`)
  - the structured-residuals diagnostic (`#result-structural-adaptation-necessity`:17)
  - matched versus forced coordinates (`#disc-additive-coordinate-forcing`:20, :72)
  - diagnosis as a fourth activity (`#disc-exploit-explore-deliberate`)
  - the innovator's dilemma (`#impl-strategy-structure`, `#deriv-update-detection-latency`)
  - discussion#196–203 (`#impl-strategy-structure`'s own teaching frames, each annotated "in the body")
  - discussion#217 and #243 (annotated landed 2026-10-30)

Recorded "in the body" by the gold but not found at HEAD by phrase: "acts but never wonders" (brief#2), and "the loop compensates for architectural limitations" (brief#62, still Working-Notes-only). The latter is a theory-headline promotion candidate (Level-2 access comes from the loop, not the architecture). It goes to the pedagogy home flagged for promotion.

Not found in any body, and among the most-converged items. These are the ones a test reader would see first:
- "a deterministic button: high CIY, zero EIG" (brief#11)
- "Markov is a boundary you draw around the agent" (brief#69, #84)
- "ignorance is cheap; epistemology is expensive" (brief#82)
- bureaucracy versus market (brief#53, with its overreach flag)
- the noisy-TV problem (discussion#250)
- Hume's is–ought in the state vector (discussion#155, *a rider*; only its non-distortion half is usable)
- Planck's "one funeral at a time" (discussion#238; isomorphism unchecked)
- the servant-leader / chatty-manager corollary (discussion#87)
- phishing as Regime-I poisoning (discussion#73)
- Prigogine (discussion#105, #221)
- apophenia (brief#166)

## Disposition of everything else

The remaining Brief, Discussion and figure items are pedagogy candidates, sorted by segment in the Working Notes where they sit. Each goes to the pedagogy home as an entry carrying its attribution and the flags above. None is a ledger item: they are content, not owed work. Joseph has not yet test-read any of them. The figures include rendered drafts in `audits/AUDIT-WORKING-472913/` and `AUDIT-WORKING-526815/`. Those sources are the audits drain's; it cites the pedagogy-home item for them.

Counts: 202 Briefs, 263 Discussion items and 99 figures were read. Of these, about 24 are riders (a): 17 in the table and 7 raised on open items. About 18 have a theory or defect disposition (b), and about 40 have landed (c); the counts are approximate where one bullet carries several glosses. The rest, roughly 480, go to the pedagogy home. The 19 teaching-frame bullets of `#impl-persistence-and-limits` split as: misquotation catalog (3) to the home; shadow catalogue (1) raised; Candidate Discussion (12) as in (b), with the rest going to the home; figures (2) to the home.

## Where the pedagogy home should be

What the material is: in-order first-encounter reflections, and that sequence is what makes them pedagogically sound (project memory `project_pedagogy_reflection_gold_mechanism.md`). Counting the sibling fork's readers-ask items, it is about 750 items. About 4% of the Briefs, Discussion items and figures now teach something canon has corrected. Most are glosses keyed to one segment, a few are chapter-scale frames, and about 100 are figure proposals.

My proposal:

1. **One file per chapter, in OUTLINE order:** `pedagogy/<volume>/<chapter-intro-slug>.md`, with a section per segment headed by its slug. The chapter is the unit a human reader actually reads in order, and the unit Joseph can test. A slug section survives refactors because slugs are the stable identity; OUTLINE order can be regenerated.
2. **Entries are the gold moved verbatim, not rewritten.** Each keeps its auditor and substrate attribution and its kind (brief, discussion, figure, readers-ask, teaching frame), and has one status line:
   - test-read by Joseph: not yet / helped / did not help;
   - landed: `#slug:line`;
   - rides on a corrected claim: the item that corrected it.

   Rewriting at move time would turn reflection into commissioned prose. The memory names that as the thing that fails.
3. **Order of the first pages.** Each Part file opens with the misquotation catalog from `#impl-persistence-and-limits` (Part I) and the riders in (a). They are the comprehension seams and the traps, and a reader-tester should meet them first.
4. **The test with Joseph runs one chapter at a time.** He reads the chapter, then its pedagogy file, and marks entries. A helpful entry that passes the isomorphism check reaches a body through an in-order walk by an agent reading the chapter cold, not by a commissioned intro. That walk is H.3's "fresh readers, before and after".
5. **Reachability without a new pointer surface.** The monograph build (`bin/build-monograph`) can emit a reader's companion per chapter from these files. Segments need no pointer; the chapter file is found by chapter. The status lines are content fields. The file is not a tracker, so I.8 holds.
6. **aat-refactored as a second source**, entered in the same files under its own source tag. Each entry is checked against canon at HEAD before Joseph sees it, because of the ~50 Chapter 1–2 defects (`influx-scout/rewrites.md` §9). The rate in (a) (about 4% of the audit gold, all of it from claims canon later corrected) suggests a check-at-entry rule for both sources, not trust in either.
7. **The sources stay where they are.** The AUDIT-WORKING §14 originals are the in-order record, so the home can always be rebuilt from them. Once an entry is in the home, the Working-Notes copy can go (I.5).

Not recommended:
- segment Working Notes, which is the status quo the correction rejects;
- `impl-*` segments, which are canon and carry claims; the 2026-08-22 lift put teaching frames there and the misquotation catalog shows why that register is fragile;
- the vsect ledger, because this is content, not work.
