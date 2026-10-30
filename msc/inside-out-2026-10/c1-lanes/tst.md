*KR C.1 (integrator item A13) and KR H.2 (the `old-*` files). Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." — Joseph, 2026-10-30.*

# TST lane: what was landed, run, moved or deleted, and what a checker should verify

Written by the TST lane integrator (Claude Opus 5.5), in worktree branch `worktree-agent-acbf83986a4dfefcd`. A different mind checks after me; this file is written for that reader.

## A13: the $\alpha \approx 0.118$ cognitive-load coefficient

**Commit:** `fc204813`. **Review record:** `reviews/hyp-exponential-cognitive-load-a13-rerun.md` (C1 broken at `a1c82543`, C2 and C3 confirmed at `fc204813`).

### The check, re-run from the page

The owner review's finding holds, and is worse than stated. `analyze_git_history.py` sets each commit's time to $10 + 5n + 0.15L$ minutes ($n$ files, $L$ lines changed). The saved dataset (`data/commits.json`, 229 commits) matches that to $10^{-12}$. METHODOLOGY.md printed a different formula, $(30 + 15n + 0.5L)(1 + 0.2U)$, which the code never ran. The score $d$ correlates 0.998 with $n$. The fit reproduces exactly ($\alpha = 0.118$, $R^2 = 0.524$ at $d \le 25$), and a time formula with no per-file term at all returns $\alpha = 0.121$. So the number describes how lines grow with files in that repository; time and comprehension never enter it. The README's other headline claim, that commits with $d \gt 10$ have a 2.3 times higher bug-fix rate, is false on the same data: 6.8% against 11.4%.

### Strengthen-first: a non-circular test

No instrumented developer time exists on the machine for this. Git timestamps do: per author, the elapsed time since that author's previous commit is real time, and it is not computed from the counts that build $d$. I ran it on six histories: the TST research corpus, obsidian-linter and ink (direct commits), and anthropic-sdk-python, gemini-cli and codex (squash-merged). Paths and HEADs are in `elapsed_time.py`'s header.

- In the direct-commit histories, $d$ predicts elapsed time (Spearman 0.27–0.45, surviving a lines covariate).
- The nested regression $\log T = c + a\,d + b\log(1+d)$ is the form test. The exponential form predicts $a \gt 0$ with $b \approx 0$; what came out is $a$ zero or negative at every cap from 60 to 480 minutes, and $b$ positive. The curve is roughly $(1+d)^{0.4}$ to $(1+d)^{0.7}$: sublinear.
- On the advisor's prompt I checked right-censoring with medians over gaps up to 24 hours, which a session cap cannot distort. They rise and flatten in obsidian-linter and ink. In the single-author corpus they rise through $d = 25$ and fall above it.
- Forcing a single exponential onto the real-time data also returns 0.04–0.13. That nearness to 0.118 is not confirmation; any concave-on-log curve gives it.
- The squash-merged histories carry merge cadence, not work ($\rho \approx 0.1$). They are a check on the method, not a measurement.

### What landed

- `#hyp-exponential-cognitive-load`:
  - the measurement paragraph and the old "honest tier" paragraph are replaced by the elapsed-time measurement at heuristic tier, with its limits: a proxy time, the count form only, the structure form untested;
  - the Epistemic Status says the count form is disfavored;
  - "reducing discontinuities has increasing marginal returns" is made conditional on superlinearity, which the count measurement does not show;
  - the Working Notes pointer now points at the new scripts, and there is a regression guard: an estimated time cannot test the form.
- `#obs-software-epistemic-properties:97`: its example of a software-calibrated quantity is now the measured sublinear curve.
- `#der-code-quality-as-observation-infrastructure`: a Working Note said the toolkit "measures context-switch-driven comprehension overhead". It never did, and the note now says so.
- `#impl-code-structure`: the "not yet established: linear, sub-exponential, exponential, or structure-dependent" sentence now reports the count measurement. The "two exponential phenomena are the same phenomenon" claim is made conditional on compounding existing.
- `02-tst-core/OUTLINE.md`: the chapter comment is updated to match.
- Toolkit (`02-tst-core/empirical-discontinuity/`):
  - `README.md` is rewritten as the one accurate account. The harness refused a file named `FINDINGS.md` from an agent, and a single front door is cleaner.
  - Deleted: `FINDINGS.md`, `METHODOLOGY.md`, `results/` (an HTML report and plots titled "Empirical Validation of FP-012"), and `visualize_results.py`, which generated them.
  - `analyze_outliers.py`'s verdict print lines are replaced by a note on what its time is, and `run_analysis.sh` is updated.
  - Added: `reproduce_estimate_fit.py` and `elapsed_time.py`.

### What a checker should verify

1. Reproduce §1: `cd 02-tst-core/empirical-discontinuity && python3 reproduce_estimate_fit.py data/commits.json`. Expect V0 to show $\alpha = 0.118$ and V2 $0.121$.
2. Reproduce §2: dump the histories with the command in `elapsed_time.py`'s header, at the named HEADs, then run it. Check that the paragraph in `#hyp-exponential-cognitive-load` matches the output, especially the ranges (Spearman 0.27–0.45; partial 0.10–0.37; $b$ 0.38–0.92; power slope 0.4–0.7; forced rate 0.04–0.13; obsidian-linter medians).
3. Judge the construct. Is per-author inter-commit elapsed time a fair proxy for implementation time? Is my wording of its limits honest, neither overclaiming "sublinear cost" as a law nor underclaiming what three histories show? Squash-merge detection is by a `(#N)` subject suffix; obsidian-linter has 63 such commits of 1,332 and ink 261 of 664. I treated ink as direct-commit because its per-author gap signal is non-trivial, and that is a judgment call.
4. Bot exclusion is by `bot` in the author email. Commits with no numstat lines (empty or binary-only) are dropped.
5. Whether the hypothesis's Formal Expression should now be restated in its structure-dependent form. I left the Formal Expression alone because the structure form is untested and restating it is a theory move, not a replacement. A spike exists (`spikes/spike-transient-dependency-amplification.md`), and the Working Notes now name the two measurements that test would need.

### Left as found, deliberately

- `TST-IDEAS.md:301` says the $\alpha \approx 0.2$ constant is undeirved while the structural claim survives. That is still true.
- Lit-review analyses (`02-tst-core/lit-review/*-analysis.md`) that invoke "FP-012 … $\alpha \approx 0.2$" are LLM-written corpus analyses, not canon. They are not cited as evidence anywhere live.
- Audit and archive mentions of the 0.118 validation are history.

## H.2: the `old-*` files

*(In progress; this section is written as the fates are decided.)*
