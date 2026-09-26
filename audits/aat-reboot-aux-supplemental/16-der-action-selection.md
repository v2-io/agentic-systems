# Supplemental 16 — `der-action-selection`

*Finder, 2026-09-25. The companion to `~/src/aat-reboot/scratch/aux/16-der-action-selection.md`. Each note is tagged with the slugs it bears on. Paths are relative to `~/src/arch/asf/` unless absolute; line numbers are as of `875e1ac3`.*

## History

- `[der-action-selection]` The commit trail (`git log --follow`):
  - `af4d958c` (2026-03-11): TF-07 migrated into ACT.
  - `9f47f406` (2026-04-01): the "praxis" gloss was planted.
  - `f9a5b49d` (2026-04-06): temporal optimality moved to TST, and the formal dependency was dropped, leaving the parenthetical at :53.
  - `75030010` (2026-04-02): Gate-1 `deps-verified`.
  - `3e87f594` (2026-04-25): AF-4, the hybrid lift. The full body is worth reading: it rejects pure $\pi(X_t)$ because it "requires introducing $X_t$ before its formulation segment, inverting deps", and rejects a pointer-only fix as merely a labeling fix.
  - `df416564` (2026-04-29): the TF-07 lineage moved to the Working Notes. It was later collapsed by the 471203 supplement (`.integrated/audit-471203-SUPPLEMENT-phase-2.md:193`).
  - `13ac20ca` (2026-05-21): the 4-paragraph summary sweep. This is why the opening duplicates the Discussion.
  - `34a16b56` (2026-05-28): Section→Part.
  - `b46c07a2` (2026-05-30): the gold lift.
- `[der-action-selection]` The TFT original, `.archive/old-tf-07-action-selection.md`, is near-verbatim with today's body. What it had that the body now lacks:
  - $\pi_M$ notation (:13);
  - the Level-3 retrospective paragraph (:39–41), since moved to `def-pearl-causal-hierarchy.md:63`;
  - the cost-of-evaluation definition of fluency (:53);
  - "Decide is context-dependent" (:72);
  - the Science and Immune rows (:86–87).
  - TF-07 also grounded the tempo advantage directly in TST T-01 (:57). The 2026-04-06 move replaced this with the persistence condition, which is where FINDER-OBSERVED (b) in the aux bites. Temporal optimality says "same outcomes, prefer faster". That is goal-side. The persistence condition is epistemic.

## Audit disposition trail

- `[der-action-selection, form-complete-agent-state]` The $\pi(M_t)$ scope overclaim was raised three times, in 742613 F5, 613842 Fresh-4 and 526815 (as a candidate). All three were resolved by AF-4 (see `audits/.integrated/ADJUDICATION-WORKING-628401/adjudication.md:320`; `audit-findings-742613.md:596` verified it first-hand). 613842 Fresh-4 (:229, :360) left one "light editorial check" deferred: does the Formal Expression carry the forward pointer? It does (:35). **Please add to the Working Notes of `der-action-selection`: checked 613842 Fresh-4's deferred forward-pointer question against the current Formal Expression :35; holds (the Part II lift paragraph cites `#form-complete-agent-state`).**
- `[der-action-selection, der-deliberation-cost]` The fluency-quantity mismatch has four sources:
  - 526815 and 742613 gold (conditional);
  - 742613 Fresh-1 (research-seed, deferred: `audit-findings-742613.md:620`);
  - 731548 xliv (raised at 18:6, certified at 27:4).

  Absent from the 731548 FINAL. The aux carries it as UNINTEGRATED 1.
- `[der-action-selection]` 731548 xlv (the goal-absorption clause) and xlvi (the compilation-cost axis). xlvi reached FINAL §D(3); xlv didn't reach the FINAL at all.
- `[der-action-selection]` Enthusiasm with no findings attached: 849201 (:353, "mathematically sound and conceptually elegant"; this is the uncritical-celebration pattern 731548 :12 names), 963715 (:291, :323), 471203 FINAL (:300, "Keep, cite as AAD-distinctive"). The prior-art analysis (`ref/prior-art-analysis/16-action-fluency.md`) cuts against "possibly novel" for fluency itself. Its novelty claim is for `#der-deliberation-cost`'s drift/gain form. Beyond that it claims only the *fluency-vs-sufficiency distinction* as "AAT-native", and that distinction is close to model-based vs model-free arbitration in the RL literature, so I'd call that claim soft.
- `[der-action-selection]` Unintegrated working dirs that touch this segment but add nothing beyond the gold: 374162 batch 4 (quiz: `04-batch-mismatch-gain-quiz-answers.md:20, :47`), 451729 batch-04 (:105, a useful watch item: "It shouldn't appear in Formal Expressions, only in Discussion". It hasn't, downstream), 527914/17 (naming: "protect `action fluency`… it names a degree, not a binary mode"), 472913 (the "derived, not chosen" test; aux 08/09 cover it).

## Passed checks (for Working Notes)

- `[der-action-selection]` **Please add to the Working Notes of `der-action-selection`: checked the Kahneman/Boyd/MCTS/MPC mapping against the prior-art pillar list (`ref/prior-art-analysis/16-action-fluency.md`); the mappings are standard; holds (but uncited, see aux UNINTEGRATED 4).**
- `[der-action-selection, der-deliberation-cost]` **Please add to the Working Notes of `der-action-selection`: checked that no downstream Formal Expression uses fluency as a derived property (451729's watch item); holds. The only formal-adjacent use is `der-deliberation-cost.md:66` (Discussion).**
- `[der-action-selection]` **Please add to the Working Notes of `der-action-selection`: checked the terminology entry `praxis.md` against the segment; consistent ($a_t = \pi(M_t)$ / $\pi(M_t, G_t)$).** Note that entry calls praxis "the fifth phase" (prolepsis, aisthesis, aporia, epistrophe, praxis). The reboot's `the-cycle.md` has four moves and drops aisthesis. That's a lexicon question for the coordinator and Joseph, tagged `[the-cycle]`.

## Worries about what the coordinator might miss

- `[der-action-selection, def-value-object, def-model-sufficiency]` The *deterministic* display (:27) is the form `def-model-sufficiency.md:45` calls "standard in AAT". Aux 11 already told him it violates positivity (C1). The same fact bears on fluency, and I left it out of the aux as speculative. A fully compiled, deterministic habit never takes the alternatives, so it holds no interventional data about them. Its "deliberation" (Level-2 simulation over candidates) would run on extrapolated predictions. Compilation erodes the evidential basis for later decompilation. That's a candidate *mechanism* for 731548's compilation cost (FINAL §D(3)), and it also matches Keramati's finding that a reversal re-engages deliberation (Fig. 7). *Unverified; a hypothesis for whoever writes the Part II version.*
- `[der-action-selection, def-causal-information-yield]` CIY's policy-induced reference $q = \pi(\cdot \mid M)$ (`def-causal-information-yield.md:76`) degenerates to a point mass under deterministic $\pi$. The CIY finder may want this.
- `[der-action-selection, scope-adaptive-system]` :25 attributes "$M_t$ is the entire internal state" to `#scope-adaptive-system`. Aux 05 already surfaced this, so I didn't repeat it.
- `[der-action-selection]` Stochastic policies: asf never says where $\pi$'s randomness comes from. If it persists across steps (a seed), then $a_t \perp \text{past} \mid M_t$ fails unless the seed sits in $M_t$. The reboot's "randomness recorded in the history" (`the-loop.md:32, :34`) covers it. No action is needed; I'm noting it only so nobody reintroduces a persistent seed.

## Notes for other finders

- `[der-deliberation-cost]` FINDER-OBSERVED (b) in my aux (not-acting ≠ not-updating) applies directly to its derivation, step 2 (:44, "the agent pauses … during the pause, mismatch has grown"). The pause is a pause of *praxis* (:15). Whether epistrophe also pauses is never stated. 731548 27:8 and 471203 raised the related baseline looseness ($\rho_{\text{delib}}\Delta\tau$ vs forgone correction $\mathcal T_0\lVert\delta\rVert\Delta\tau$). Also for that finder: Keramati 2011 (p. 3, p. 5) is the closest published analog of the threshold's *shape*, and it isn't cited. The prior-art analysis's "pure mathematical novelty" claim (:48) should be weighed against it.
- `[the-loop, held-still-and-moving]` The reboot's "every action both pursues and probes" (`~/src/aat-reboot/src/the-loop.md:66`, OUTLINE :39) conflicts with LQG's absence of a dual effect, per Bar-Shalom & Tse themselves as I recall them. Not verified at the primary (paywalled). Relata also holds `tse-1975-generalized` and `barshalom-1976-caution` if anyone fetches PDFs.
- `[def-pearl-causal-hierarchy]` :63 is now the canonical home of the TF-07 Level-3 deliberation paragraph.

## Process feedback

- The brief worked well. The line "unintegrated = not reflected in this segment" did the most work here: the one real defect (xliv) was certified in *another* segment's reflection and absent from the FINAL. Only a grep across the working dirs finds that.
- relata's conversion queue can sit behind a 572-page book (`shalizi-1999-computational`, ETA about 1.5 h). For a single short paper, `pdftotext` on the `ref/` copy was faster. Page-number citations stand in for markdown line ranges in the aux. Suggestion: finders could `relata prep <key>` the papers they expect at the *start* of a run, or the queue could prioritize short documents.
- The relata `search` verb isn't in the top of `relata --help`, but it works, and it was the quickest route to a bibkey.
- `memorata-search --joseph` returns agent text that was pasted into user turns (e.g. the 2026-04-02 Gate-2 review). Joseph-intent searches need a manual check of who actually spoke.
