# Empirical discontinuity analysis

This toolkit tests the functional form in `#hyp-exponential-cognitive-load`: whether the time to make a change grows as $T = T_{\text{base}}(1+\alpha)^d$ in the number $d$ of boundary crossings in the changeset. The discontinuity score throughout is the toolkit's own, $d = (\text{file transitions}) + 2\cdot(\text{directory transitions})$, counted over a commit's changed paths in git's order.

## 1. The original fit measured the time estimator, not time

`analyze_git_history.py` assigns each commit a time `commit_time_estimate` $= 10 + 5n + 0.15L$ minutes, where $n$ is files changed and $L$ is lines changed. The saved dataset (`data/commits.json`, 229 commits of `~/src/_core/tst` from 2025-08-25 to 2025-08-29, one author) matches that formula to $10^{-12}$ minutes. The score $d$ is built from the same paths: over these commits $\operatorname{corr}(d, n) = 0.998$. Regressing the estimate on $d$ therefore fits the analyst's formula against a near-copy of one of its inputs.

`reproduce_estimate_fit.py` reproduces the original result exactly ($\alpha = 0.118$, $R^2 = 0.524$ at $d \le 25$, $N = 205$) and then changes the formula. Every variant returns an "exponential penalty" of about the same size, including formulas with no per-file term at all:

| Time formula (minutes) | $\alpha$ at $d \le 25$ | exponential $R^2$ | linear $R^2$ |
|---|---|---|---|
| $10 + 5n + 0.15L$ (what the code ran) | 0.118 | 0.524 | 0.453 |
| $(30 + 15n + 0.5L)(1 + 0.2U)$, $U$ = directories | 0.131 | 0.617 | 0.532 |
| $10 + 0.15L$ (lines only) | 0.121 | 0.488 | 0.410 |
| $10 + 5n + 1.5L$ | 0.125 | 0.491 | 0.414 |
| $10 + 5n$ (files only) | 0.073 | 0.842 | 0.877 |

The $\alpha \approx 0.12$ is a property of how lines changed grow with files changed in that repository. No time and no comprehension enters it. When the estimate is exactly linear in $n$ (last row), an exponential fit still returns $\alpha = 0.07$ while fitting worse than a line: a single-form fit cannot test the form. The same dataset also does not support the claim that high-$d$ commits are fix-prone: commits with $d \gt 10$ carry a fix-like message 6.8% of the time against 11.4% for $d \le 10$.

## 2. Elapsed time between commits

`elapsed_time.py` replaces the estimate with a measured quantity: for each author, the time since that author's previous commit. This is elapsed wall-clock time, not instrumented working or comprehension time: it includes whatever else the author did, and how much work goes into one commit is the author's choice. It is, however, not computed from the counts that build $d$. The run used six histories (paths and HEADs in the script header): the original corpus, two repositories with direct commits by many authors (obsidian-linter, ink), and three where nearly every commit is a squash-merged pull request (anthropic-sdk-python, gemini-cli, codex). In squash-merged histories the timestamps record merge cadence rather than work, so those three are a check on the method, not a measurement.

**Long gaps.** A gap between two commits can hold hours or days away from the work, so how long gaps are treated decides what is measured. Dropping gaps above a session cap is not neutral: the share dropped grows with $d$. Over 24 hours it is 0.15, 0.23, 0.24, 0.27, 0.26 and 0.35 in obsidian-linter for $d$ = 0, 1–2, 3–5, 6–10, 11–25 and 26–60, and 0.29–0.45 in ink; in the single-author corpus it is 0–0.06. Counting the long gaps as censored instead puts the time away into the median (obsidian-linter: 12, 54, 77, 160, 260 and 303 minutes). The script reports two treatments. Sections (1)–(5) keep gaps under caps from 60 minutes to none. Sections (6)–(8) keep every gap and fit a two-component log-normal mixture to $\log T$: a working component whose mean carries the form in $d$ (or in changeset size) and an idle component, with the working share free in each bin. The mixture is a modelling choice, and its numbers move with it.

**Results, $d \le 25$, direct-commit histories.**

- $d$ predicts elapsed time: under caps of 60–240 minutes, Spearman $\rho$ = 0.45 (corpus), 0.38–0.41 (obsidian-linter), 0.27–0.28 (ink), and the association survives partialling out lines changed (0.36–0.37, 0.17–0.20, 0.10–0.12). The mixture's working-time medians rise with $d$, in minutes for $d$ = 0, 1–2, 3–5, 6–10, 11–25: obsidian-linter 6.2, 11.9, 16.0, 33.1, 29.7 (last interval 14–60); ink 5.4, 8.3, 15.0, 15.0, 15.5; corpus 3.1, 5.4, 5.6, 8.5, 16.4. The top bins' intervals are wide.
- The form, window-free (section 6). In the nested form $\log T = c + a\,d + b\log(1+d)$, the exponential predicts $a \gt 0$ with $b \approx 0$ and a power law the reverse. Inside the working component, obsidian-linter gives $b = 0.98$ $[0.51, 1.33]$ and $a = -0.07$ $[-0.17, +0.07]$: a pure exponential is rejected. Ink gives $b = 0.55$ $[-0.04, 1.12]$, the corpus $b = 0.32$ $[-0.30, 0.63]$ and $a = +0.04$ $[-0.01, +0.28]$: not distinguished. The working-time power exponent is 0.72 $[0.56, 0.87]$, 0.50 $[0.29, 0.70]$ and 0.50 $[0.32, 0.66]$; the power law's log-likelihood exceeds the exponential's by 9.8, 1.6 and 1.6.
- The form, capped (sections 2 and 5). At caps of 60 minutes to 24 hours, $a$ is near zero or negative and $b$ is 0.38–0.39 (corpus), 0.72–1.01 (obsidian-linter) and 0.42–0.67 (ink). Without a cap, the corpus gives $a = +0.078$ $[-0.002, +0.155]$ and ink's coefficients are uninformative. The capped pattern is weaker evidence than it looks: a pure exponential in working time, mixed with idle gaps as fitted and passed through the same cap, also gives $a$ near zero and $b$ up to about 1. Section 7 reports how often that null's $b$ reaches the observed: 0.007–0.06 across histories and caps.
- The pure power slope of $\log T$ on $\log(1+d)$ is 0.39–0.75 under caps of 60 minutes to 24 hours, and reaches 0.86 in obsidian-linter with a one-week cap or none (section 5).
- A single exponential forced onto these data returns a per-discontinuity rate between 0.04 and 0.16 depending on the fitting method and the cap, and 0.10–0.28 inside the working component. That number describes the fit, not the data.

The squash-merged histories show the method's floor: $\rho$ = 0.07–0.12 for gemini-cli and codex, with the nested coefficients pointing the same way as above but weakly. anthropic-sdk-python leaves too few same-author pairs ($N$ = 34–53) for any conclusion.

**Changeset size.** The same instrument tests `#emp-changeset-size-principle`'s $t \propto \lvert\text{changeset}\rvert$, which predicts a log-log slope of 1. The slope of $\log T$ on $\log(1+L)$ is 0.14–0.26 (corpus), 0.24–0.48 (obsidian-linter) and 0.22–0.40 (ink) as the cap goes from 60 minutes to none, and 0.20 $[0.10, 0.35]$, 0.38 $[0.29, 0.59]$ and 0.31 $[0.19, 0.46]$ inside the working component (section 8). On files touched the working-component slope is 0.68 $[0.22, 1.24]$, 0.90 $[0.73, 1.26]$ and 0.62 $[0.36, 0.87]$. Working-time medians by lines changed, obsidian-linter: 6.4, 15.5, 29.4, 32.0, 12.6 minutes for 0–10, 11–50, 51–200, 201–1000, over 1000 lines (median 4, 24, 100, 307, 2137 lines).

## 3. What this does and does not bear on

At file and directory granularity, with elapsed time between commits as the time measure, the cost of a changeset rises with the number of boundary crossings without compounding. In obsidian-linter a pure exponential is rejected for a power law with exponent about 0.7; in ink and the corpus the forms cannot be told apart. What this measures is the count model: $d$ counts crossings without regard to whether understanding one change requires understanding another. The hypothesis's central open question, whether nested dependency among the scattered changes produces compounding that independent changes do not, is untested here. Testing it needs a measure of dependency among the changed locations, and a time measure closer to working time than inter-commit gaps. A test of either kind would supersede this one.

## Files and usage

- `analyze_git_history.py`: the original miner (`python analyze_git_history.py --repo <repo> --max-commits N --output data`). It writes `data/commits.json` and `data/analysis.pkl`, including the formula-based `commit_time_estimate` analyzed in §1.
- `analyze_outliers.py`: the original multi-form fit over filtering windows, which produced $\alpha = 0.118$; it reads `data/analysis.pkl`.
- `reproduce_estimate_fit.py`: §1. `python3 reproduce_estimate_fit.py data/commits.json`.
- `elapsed_time.py`: §2, on `git log` dumps made with the command in its header. `python3 elapsed_time.py <name>.log ...`. Its sections (1)–(8) are described in its docstring; every number in §2 is printed by one of them.
- `analyze_bug_detection.py`: a commit-message classifier for fix-like commits.
- `src/discontinuity_metrics.py`: a static per-file discontinuity counter. Its "predicted comprehension time" applies the hypothesis with an assumed $\alpha = 0.2$; that number is the hypothesis evaluated, not a measurement.
- `run_analysis.sh`: reproduces §1 from the saved dataset, which it never overwrites; given a repository path, it also mines that history into `rerun/`.

Dependencies: `requirements.txt` (numpy, scipy; matplotlib for `analyze_outliers.py`'s figure).
