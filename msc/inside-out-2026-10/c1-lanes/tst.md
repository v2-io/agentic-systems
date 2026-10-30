*KR C.1 (integrator item A13) and KR H.2 (the `old-*` files). Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." — Joseph, 2026-10-30.*

# TST lane: what was landed, run, moved or deleted, and what a checker should verify

Written by the TST lane integrator (Claude Opus 5.5) in worktree branch `worktree-agent-acbf83986a4dfefcd`, for the mind that checks it. Commits, in order:

- `fc204813`: A13 landing.
- `10925103`: A13 review record.
- `60162347`: A13 follow-through, a missed carrier and the changeset-size measurement.
- `2d204811`: H.2, TST.
- `de218fb0`: H.2, Part III.
- The commit carrying this file: H.2 review record and vsect questions.

Review records: `reviews/hyp-exponential-cognitive-load-a13-rerun.md` and `reviews/tst-old-files-h2-integration.md`.

## A13: the $\alpha \approx 0.118$ cognitive-load coefficient

### The check, re-run from the page

The owner review's finding holds, and is worse than it says. `analyze_git_history.py` set each commit's "time" to $10 + 5n + 0.15L$ minutes, with $n$ files and $L$ lines changed. The saved 229-commit dataset matches that to $10^{-12}$; the former METHODOLOGY.md printed a different formula, which the code never ran. The score $d$ correlates 0.998 with $n$. The fit reproduces exactly ($\alpha = 0.118$, $R^2 = 0.524$ at $d \le 25$), and a time formula with no per-file term at all still returns $\alpha = 0.121$. The number describes how lines grow with files in that repository; neither time nor comprehension enters it. The README's other headline, that commits with $d \gt 10$ have a 2.3 times higher bug-fix rate, is false on the same data: 6.8% against 11.4%.

### Strengthen-first: a non-circular test

No instrumented developer time exists on the machine for this, but git timestamps do. For each author, the elapsed time since that author's previous commit is real time, and it is not computed from the counts that build $d$. The test ran on six histories (paths and HEADs in `elapsed_time.py`): the TST research corpus; obsidian-linter and ink, which use direct commits; and anthropic-sdk-python, gemini-cli and codex, which are squash-merged. The squash-merged ones record merge cadence, not work, so they bound the method rather than measure anything.

- $d$ predicts elapsed time (Spearman 0.27–0.45), and the association survives a lines covariate.
- **The form test rejects the exponential.** In $\log T = c + a\,d + b\log(1+d)$, the exponential form predicts $a \gt 0$ with $b \approx 0$. What came out is $a$ zero or negative at every session cap from 60 to 480 minutes, with $b$ positive: roughly $(1+d)^{0.4}$ to $(1+d)^{0.7}$, sublinear.
- **Censoring checked.** Medians over gaps up to 24 hours, which the cap cannot distort, rise and flatten in obsidian-linter and ink. In the single-author corpus they rise through $d = 25$ and fall above it.
- **A forced exponential is not evidence.** Forcing one onto the real-time data returns 0.04–0.13. That this sits near 0.118 confirms nothing: any curve that is concave on a log scale gives a number like it.
- **Changeset size, same instrument.** The test bears on `#emp-changeset-size-principle`'s $t \propto \lvert\text{changeset}\rvert$. The log-log slope on lines changed is 0.14–0.41, with every interval below 1; on files touched it is 0.29–0.89. The proxy includes comprehension, so the result is that the claim and its comprehension corollary cannot both hold.
- The original TST authors named their own falsifier (old `general-discussion`): "if empirical studies show comprehension time grows linearly rather than exponentially with discontinuities, the framework would need revision." At count level the measurement finds growth sublinear.

### What landed

- `#hyp-exponential-cognitive-load`:
  - the measurement paragraph is replaced by the elapsed-time result at heuristic tier;
  - Epistemic Status says the count form is disfavored and the structure form untested;
  - "increasing marginal returns" is made conditional;
  - FP-012's reading-side operationalization (comprehension searches) is named as different and unmeasured;
  - Working Notes carry a regression guard (estimated time cannot test the form) and the species-specific AI hypothesis.
- Carriers drained:
  - `#obs-software-epistemic-properties:97`;
  - `#der-code-quality-as-observation-infrastructure`'s Working Note;
  - `#impl-code-structure` (count form measured; the two-exponentials parallel made conditional);
  - `02-tst-core/OUTLINE.md`'s chapter comment;
  - `#der-dual-optimization:58`, a carrier my first grep missed because it never named the number;
  - `#der-principled-decision-integration`'s "possibly exponential".
- `#emp-changeset-size-principle`: the measurement replaces the invitation to make it, plus one Epistemic Status sentence. The Formal Expression is unchanged, because the claim is about $t_{\text{impl}}$ alone, which the proxy cannot isolate.
- Toolkit `02-tst-core/empirical-discontinuity/`:
  - `README.md` is the one accurate account.
  - Deleted: `FINDINGS.md`, `METHODOLOGY.md`, `results/` (a report and plots titled "Empirical Validation of FP-012") and `visualize_results.py`.
  - Added: `reproduce_estimate_fit.py` and `elapsed_time.py`.

### What a checker should verify

1. **The circular fit.** `cd 02-tst-core/empirical-discontinuity && python3 reproduce_estimate_fit.py data/commits.json`. Expect V0 $\alpha = 0.118$ and V2 $0.121$.
2. **The elapsed-time results.** Dump the histories with the command in `elapsed_time.py`'s header, at the named HEADs, and run it. Compare against `#hyp-exponential-cognitive-load` and `#emp-changeset-size-principle`.
3. **The construct.** Is per-author inter-commit time a fair proxy for implementation time? Are the stated limits honest in both directions? Two judgment calls are mine: ink is treated as direct-commit (261 of 664 subjects carry a `(#N)` suffix), and bots are excluded by `bot` in the email.
4. **The Formal Expression.** It was left as the count form, since the structure form is untested. Restating it would be a theory move rather than a replacement. A vsect question now holds the structure test.

## H.2: the 44 `old-*` files

Each file was read whole and compared with the live segment(s) named here, which a checker should read to confirm. "Carried" means the live segment states the file's substantive content, usually more carefully. "Landed" means content that was not carried and went into the named segment at its tier. Every original remains in git and in the `temporal-software-theory` repository (`vault/02-theory/`, `via-tft/`, `meta-analysis/`) or the `temporal-feedback` repository (Appendix F); `diff` against the via-tft and Appendix F originals shows formatting differences only. vsect never held these files as records (`.vsect/kinds.yaml` excludes `0*/src/old-*.md`).

| File | Fate | Read against / landed in |
|---|---|---|
| `old-tst-d01-feature` | carried, deleted | `#def-feature` |
| `old-tst-d02-atomic-change-set` | carried, deleted | `#def-atomic-changeset` |
| `old-tst-d03-comprehension-time` | carried, deleted | `#def-comprehension-time` |
| `old-tst-d04-implementation-time` | carried, deleted | `#def-implementation-time` |
| `old-tst-d05-change-distance` | carried, deleted | `#def-discontinuity-distance` |
| `old-tst-d06-system-coupling` | carried, deleted | `#def-system-coupling` |
| `old-tst-d07-system-coherence` | carried, deleted | `#def-system-coherence` |
| `old-tst-d08-system-availability` | carried, deleted | `#def-system-availability` |
| `old-tst-t01-time-optimality` | carried, deleted | `#post-temporal-optimality` |
| `old-tst-t02-implementation-time-lower-bound` | carried (strengthened by S1–S2); a mislabel corrected, lineage landed; deleted | `#result-specification-bound`: Putnam's fit vs TST's $3/4$ conjecture; Kushilevitz & Nisan for S1. Its generalization-bound "support" (Wang & Mao; Chu & Raginsky) is an analogy, not landed |
| `old-tst-t03-evolving-systems-scope` | carried; scope examples landed; deleted | `#scope-evolving-software` |
| `old-tst-t04-change-expectation-baseline` | carried (median correction); rewrite-as-information landed; deleted | `#der-change-expectation-baseline` |
| `old-tst-t05-dual-optimization` | carried, deleted | `#der-dual-optimization` |
| `old-tst-t06-change-investment` | carried; undiscounted-time scope landed; deleted | `#der-change-investment` |
| `old-tst-t07-conceptual-alignment` | carried; coordination = overlap definition and Conway landed; deleted | `#hyp-conceptual-alignment` |
| `old-tst-t08-domain-tracking` | carried; vocabulary-coverage measure landed; deleted | `#hyp-conceptual-alignment` |
| `old-tst-t09-change-set-size` | carried, deleted | `#emp-changeset-size-principle` |
| `old-tst-t10-change-proximity` | carried, deleted | `#der-change-proximity-principle` |
| `old-tst-t11-coherence-coupling-measure` | carried, deleted | `#meas-coherence-coupling` |
| `old-tst-t12-comprehension-proximity-correlation` | had no carrier; landed at Hypothesis; deleted | `#der-change-proximity-principle` ("Reading locality") |
| `old-tst-t13-comprehension-continuity` | carried; its reading-side operationalization named; deleted | `#hyp-exponential-cognitive-load`. Its "studies show 20–30%" and "2–5× faster" are unsourced and not landed |
| `old-tst-t14-principled-decision-integration` | carried, deleted | `#der-principled-decision-integration` |
| `old-tst-t15-continuous-operation-under-perturbation` | carried, deleted | `#scope-continuous-operation` |
| `old-tst-appendix-a-version-mapping` | moved, extended with live slugs; deleted | `02-tst-core/lit-review/README.md` (11 lit-review files cite FP-labels) |
| `old-tst-software-first-principles` (v0.1) | earlier version of the T-files; FP-001's probabilistic form landed; deleted | `#post-temporal-optimality` |
| `old-tst-synthesis-theoretical-foundations` | 14-theorem compendium of the same; deleted | its "Empirical Validation" figures carry footnotes that do not support them (system age doubling attributed to a debt-allocation paper, among others): not landed, flagged below |
| `old-tst-synthesis-executive-summary` | summary of the 2025 literature syntheses; deleted | syntheses remain in `02-tst-core/lit-review/result-synthesis*.md` |
| `old-tst-comprehensive-synthesis` | as above; four verified pieces landed; deleted | Lehman et al. 1997 → `#scope-evolving-software`; METR 2025 → `#def-implementation-time`; real options (Baldwin & Clark 2000; Sullivan et al. 2001) → `#der-change-investment`; species-specific AI form → `#hyp-exponential-cognitive-load` WN |
| `old-tst-960-analysis-synthesis` | corpus generalizations; Tufano anchor landed; deleted | "debt is created at birth" verified against Tufano et al. 2015 → `#scope-evolving-software`; the rest is triaged in `TST-IDEAS.md` §5 and the 2026-05-21 mining |
| `old-tst-research-findings-top-100` | arithmetic on assumed constants ("Beauty = 3640×" is $(1.2)^{50}/(1.2)^{5}$); deleted | — |
| `old-tst-meta-analysis-priority-rankings` | corpus metadata (scores by "excitement indicators"); deleted | original in `temporal-software-theory/meta-analysis/` |
| `old-tst-meta-analysis-topology` | corpus metadata (cluster map); deleted | as above |
| `old-tst-general-discussion` | carried, deleted | `#der-principled-decision-integration` (humanistic convergence); the epistemic framing by `#obs-software-epistemic-properties` and `#post-temporal-optimality` |
| `old-tst-ai-specification-limit` | core carried; remainder ungrounded formulas; deleted | `#result-specification-bound`, `#def-implementation-time` |
| `old-tst-lindy-foundations` | strengthening landed; deleted | `#der-change-expectation-baseline`: hazard-mixture form (Derived, exact asymptotically), Gott 1993 and Ord 2023 lineage |
| `old-tst-lindy-math-foundations` | duplicate of the above without its header; deleted | as above |
| `old-tst-via-tft-readme` | index of the via-tft set; its open questions answered by the segments below; deleted | `#der-code-quality-as-observation-infrastructure`, `#obs-context-turnover`, `#obs-software-epistemic-properties` |
| `old-tst-via-tft-mapping` | carried; symptom mapping and team trust landed; deleted | `#scope-developer-agent`, `#der-code-quality-as-observation-infrastructure`; source lines repointed |
| `old-tst-via-tft-causal-extensions` | carried, deleted | `#hyp-causal-discovery-from-git`, `#obs-software-epistemic-properties` (P2, P3); source line repointed |
| `old-tst-via-tft-reformulated-sketch` | the blueprint the live TST was built from; availability link landed; deleted | `#scope-continuous-operation`. Its integral investment form was not landed: its units do not close |
| `old-tst-via-tft-simulation-proposals` | Sims 1–2 carried by AAT's sector and adversarial machinery; Sims 3–6 registered as questions; deleted | `vsect open` (three questions below) |
| `old-tst-proximity-coherence-for-ai` | a pasted transcript snippet, no content; deleted | — |
| `old-tst-exemplar-analyses` | empty (0 bytes); deleted | — |
| `old-tf-appendix-f-multi-agent` | carried; falsifiers and disagreement diagnostic landed; deleted | `#hyp-communication-gain`, `#der-team-persistence`, `#der-temporal-nesting`, `#hyp-auftragstaktik-principle` |

### Defects found while reading

- **`#result-specification-bound`** labeled TST's own conjecture as Putnam's empirical finding. It is replaced, and recorded broken in C1 of the H.2 review.
- **`#def-causal-information-yield:55` (body)** said Part III content was "not yet fully extracted" from the Appendix F file. That was false, and it is replaced (C2).
- **`#impl-foundations-features`** called the change-expectation baseline "the turnover multiplier"; that multiplier is $k$. It also said $\hat n_{\text{future}} \to \infty$ under context turnover. Restated.
- **Two Working Notes** cited the wrong old T-labels: the perturbation taxonomy is T-15, not T-12, and the expanded form is T-14, not T-11. Corrected.

### Registered as questions (`vsect open`)

- An LLM agent's per-observation model shift over a session (Sim 6). This is an objective-E candidate.
- Agent replay of historical features: changeset size against model quality, and alternative architectures (Sims 3–4). Also an objective-E candidate.
- The dependency-structure form of the cognitive-load hypothesis.

### For F.3 (citation fidelity), not acted on here

The 2025 synthesis documents carry footnoted figures whose citations do not support them: "36% of time wasted on debt", "refactoring ROI 200–400%", "40–60% higher future-change probability", "system age 5.14 → 10.69 years". None of them is in canon. If anyone wants one, the primary source has to be read first. I could not find Suelmann 2014 (cited against Putnam), so it is not cited.

### What a checker should verify

1. **Absorption, on a sample.** Pick rows from the table, read the original (git: `git show de218fb0^:01-aat-core/src/old-tf-appendix-f-multi-agent.md`, `git show 2d204811^:02-tst-core/src/<file>`), then the live segment named. Is anything substantive missing that I called carried?
2. **The hazard-mixture derivation.** Check it in `#der-change-expectation-baseline`, and check the numerical table in the H.2 review's C3.
3. **Each landed paragraph against its source.** Look especially at tier labels and citations: METR 2025, Lehman et al. 1997, Tufano et al. 2015, Baldwin & Clark 2000, Sullivan et al. 2001, Kushilevitz & Nisan 1997, Gott 1993, Ord 2023, Liu et al. 2024, Conway 1968 and Putnam 1978. Each was checked against a bibliographic record or abstract, not the full text.
4. **The availability formulation** in `#scope-continuous-operation`: its assumptions and algebra.
5. **The Part III falsifiers.** Are they faithful to Appendix F §F.7, and stated in each segment's own notation?

### Left as found, deliberately

- `TST-IDEAS.md:301` says the $\alpha \approx 0.2$ constant is underived while the structural claim survives. That is still true.
- The lit-review analyses quote FP-012's $\alpha \approx 0.2$. They are research inputs; the new README says so and points to the measured treatment.
- `bin/segment-stats` still lists `old-tst-`/`old-tf-` among its archive prefixes. It is harmless now that no such files exist.
- lint-outline counts `old-*` files as segment files, so `01-aat-core`'s entry and file counts matched only while the old-tf file existed. They now read 173 entries against 172 files. The one linked row without a file is `#worked-example-cam`; its stage cell says `missing`, and `TODO.md` tracks it as AAT-9. That is an honest mark under H.2, but `bin/lint-outline` does not report it.
