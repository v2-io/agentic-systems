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

`elapsed_time.py` replaces the estimate with a measured quantity: for each author, the time since that author's previous commit, kept when it is positive and under a session cap of 60, 120, 240 or 480 minutes. This is elapsed wall-clock time, not instrumented working or comprehension time: it includes whatever else the author did, and how much work goes into one commit is the author's choice. It is, however, not computed from the counts that build $d$. The run used six histories (paths and HEADs in the script header): the original corpus, two repositories with direct commits by many authors (obsidian-linter, ink), and three where nearly every commit is a squash-merged pull request (anthropic-sdk-python, gemini-cli, codex). In squash-merged histories the timestamps record merge cadence rather than work, so those three are a check on the method, not a measurement.

**Results, $d \le 25$, direct-commit histories.**

- $d$ predicts elapsed time: Spearman $\rho$ = 0.45 (corpus), 0.38–0.41 (obsidian-linter), 0.27–0.28 (ink), and the association survives partialling out lines changed (0.36, 0.17–0.20, 0.10–0.12).
- The exponential form is not supported. In the nested regression $\log T = c + a\,d + b\log(1+d)$, the exponential form predicts $a \gt 0$ with $b \approx 0$, and a power form the reverse. At every cap, $a$'s bootstrap 95% interval contains zero or lies below it (obsidian-linter, cap 240: $a = -0.075$, interval $[-0.141, -0.003]$), and $b$ is positive: $0.38$–$0.39$, intervals within $[0.11, 0.67]$, in the corpus and $0.72$–$0.92$, intervals within $[0.44, 1.20]$, in obsidian-linter. In ink it is $0.42$–$0.55$, with an interval that reaches zero at two of three caps. The same holds with $\log(1+L)$ added as a covariate.
- Read as a power law, elapsed time grows roughly as $(1+d)^{0.4}$ to $(1+d)^{0.7}$, so more slowly than in proportion to $d$.
- Medians on gaps up to 24 hours, which the session cap cannot distort, rise and then flatten. In minutes, for $d$ = 0, 1–2, 3–5, 6–10, 11–25: obsidian-linter 8.5, 22.8, 28.2, 71.0, 70.0; ink 5.6, 10.4, 21.6, 30.0, 33.4. In the single-author corpus the median keeps rising through $d \le 25$ (3.5, 5.5, 5.9, 9.8, 20.5) and falls above it (11.4 at $d$ = 26–60).
- A single exponential forced onto these data returns a per-discontinuity rate between 0.04 and 0.13, depending on the fitting method and the cap. That number describes the fit, not the data: it is a straight line laid through a curve that is concave on a log scale.

The squash-merged histories show the method's floor: $\rho$ = 0.07–0.12 for gemini-cli and codex, with the nested coefficients pointing the same way as above but weakly. anthropic-sdk-python leaves too few same-author pairs ($N$ = 34–53) for any conclusion.

## 3. What this does and does not bear on

At file and directory granularity, with elapsed time between commits as the time measure, the cost of a changeset rises with the number of boundary crossings, and it rises sublinearly, not by compounding. What this measures is the count model: $d$ counts crossings without regard to whether understanding one change requires understanding another. The hypothesis's central open question, whether nested dependency among the scattered changes produces compounding that independent changes do not, is untested here. Testing it needs a measure of dependency among the changed locations, and a time measure closer to working time than inter-commit gaps. A test of either kind would supersede this one.

## Files and usage

- `analyze_git_history.py`: the original miner (`python analyze_git_history.py --repo <repo> --max-commits N --output data`). It writes `data/commits.json` and `data/analysis.pkl`, including the formula-based `commit_time_estimate` analysed in §1.
- `analyze_outliers.py`: the original multi-form fit over filtering windows, which produced $\alpha = 0.118$; it reads `data/analysis.pkl`.
- `reproduce_estimate_fit.py`: §1. `python3 reproduce_estimate_fit.py data/commits.json`.
- `elapsed_time.py`: §2, on `git log` dumps made with the command in its header. `python3 elapsed_time.py <name>.log ...`.
- `analyze_bug_detection.py`: a commit-message classifier for fix-like commits.
- `src/discontinuity_metrics.py`: a static per-file discontinuity counter. Its "predicted comprehension time" applies the hypothesis with an assumed $\alpha = 0.2$; that number is the hypothesis evaluated, not a measurement.
- `run_analysis.sh`: runs the miner on the parent repository and the original fit.

Dependencies: `requirements.txt` (numpy, scipy; matplotlib for `analyze_outliers.py`'s figure).
