*KR E.3 ("One of Volume 2's cheap falsifiers is run on a real codebase history"), under objective E ("One quantity is measured on an agent the theory did not construct"). Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." — Joseph, 2026-10-30.*

# E.3: source files outlive the change-expectation baseline, and receive at least as many further changes as it predicts where the follow-up is long enough to tell

Written by the E.3 agent (Claude Opus 5.5) on 2026-10-30, for the lead first and then for an independent checker. Per the lead's instruction, nothing has been landed in canon or in the ledger; §7 holds what I would propose.

**Order of work.** The ordering is checkable from the commits.

- `54a0bf5e`: the design, committed before any lifetime was extracted (`prereg.md`).
- `d84252d3`: the script, committed before the primary set ran.
- `135956b2`: the run registered as `empirica/software-file-lifetimes/` (MANIFEST, and RUNS with HEAD shas, seeds and digests).

Two things were seen before the primary set ran:

- a smoke test of the extraction on asf's own history, which is not part of the test;
- three of the four young histories (ink, obsidian-linter, gemini-cli), which ran first because their clones finished first. Codex ran later, after most of the primary set.

The exploratory analysis (§4) was written after seeing those three, and committed with the script before redis and the rest of the primary set ran. The post-hoc fit (§3) was written after seeing all of it.

## 1. Which falsifier, and what was measured

`item:tst-cheap-falsifiers-and-measurement-design` lists five falsifiers.

- The TST lane's real-history toolkit, `02-tst-core/empirical-discontinuity/elapsed_time.py`, covers (d) and `#hyp-exponential-cognitive-load`, which is the owner review's §3.3 item 2.
- It does not touch (a), `#der-change-expectation-baseline`. The "scale-ignorance" in tst-check-4 is F1, a derivation defect, and involves no data.

So (a) was untested, and the explorer ranked it "W, and cheap". I took (a).

**The segment's prediction.** The segment derives $P(T \gt t_0+u \mid t_0) = t_0/(t_0+u)$: the median remaining life equals the current age. Its hazard-mixture form recovers this at large age when the prior on the termination hazard is finite and positive at zero. More generally, a survival tail $t^{-a}$ gives a median remaining life of $(2^{1/a}-1)\,t_0$.

**What was measured.** The local exponent $a(t_0) = -\log_2[Q(2t_0)/Q(t_0)]$. Here $Q$ is the Kaplan–Meier survival of a source file from the mainline commit that adds it to the one that deletes it, with renames followed and files still present at HEAD censored. It was measured in two clocks, calendar days and mainline commits, with a directory-cluster bootstrap. The prediction is $a(t_0) = 1$.

**The repositories.**

- *Primary set:* git, cpython, postgres, django, rails, ruby, perl5, redis, node, vim. That is 222,000 lives and 105,000 deaths, histories of 17 to 39 years.
- *Young set:* codex, gemini-cli, obsidian-linter, ink.

## 2. The pre-registered result

The decision rule of prereg §6 returns **against: files outlive the baseline**, in both clocks, at both large and young ages, and in every sensitivity variant (no renames; import-born files dropped).

At large age, the interval on $\bar a$ lies wholly below 0.63 in 9 of 10 repositories. The exception is cpython, whose interval is $[0.35, 0.64]$. At 0.63 the baseline's median multiplier would be off by a factor of two. At young age the interval lies below 0.63 in all ten.

| Repository | lives (deaths) | $\bar a$ calendar, $t_0 \ge 1$ y | $\bar a$ calendar, young | $\bar a$ commits, $t_0 \ge 1000$ | $\bar a$ commits, young | no renames, calendar |
|---|---|---|---|---|---|---|
| git | 5543 (697) | 0.05 [0.03, 0.08] | 0.01 [0.00, 0.02] | 0.06 [0.04, 0.11] | 0.01 [0.00, 0.01] | 0.18 [0.10, 0.38] |
| cpython | 26849 (20975) | 0.44 [0.35, 0.64] | 0.18 [0.08, 0.32] | 0.31 [0.24, 0.42] | 0.14 [0.06, 0.22] | 0.54 [0.43, 0.70] |
| postgres | 11425 (4000) | 0.13 [0.11, 0.15] | 0.03 [0.02, 0.04] | 0.11 [0.09, 0.14] | 0.02 [0.01, 0.02] | 0.15 [0.13, 0.18] |
| django | 9501 (2416) | 0.10 [0.09, 0.11] | 0.02 [0.01, 0.02] | 0.08 [0.07, 0.09] | 0.00 [0.00, 0.01] | 0.15 [0.14, 0.17] |
| rails | 8516 (3599) | 0.16 [0.13, 0.18] | 0.06 [0.05, 0.07] | 0.12 [0.10, 0.14] | 0.03 [0.03, 0.04] | 0.21 [0.18, 0.25] |
| ruby | 21551 (9646) | 0.34 [0.28, 0.42] | 0.05 [0.04, 0.05] | 0.16 [0.13, 0.18] | 0.01 [0.01, 0.01] | 0.37 [0.30, 0.44] |
| perl5 | 12498 (5519) | 0.13 [0.10, 0.15] | 0.09 [0.06, 0.13] | 0.13 [0.11, 0.17] | 0.02 [0.02, 0.03] | 0.27 [0.22, 0.32] |
| redis | 2569 (631) | 0.07 [0.03, 0.15] | 0.02 [0.01, 0.05] | 0.06 [0.02, 0.11] | 0.03 [0.01, 0.06] | 0.10 [0.05, 0.22] |
| node | 113627 (56865) | 0.30 [0.24, 0.40] | 0.11 [0.10, 0.13] | 0.22 [0.18, 0.27] | 0.03 [0.02, 0.04] | 0.36 [0.28, 0.47] |
| vim | 9762 (1091) | 0.06 [0.02, 0.14] | 0.01 [0.00, 0.01] | 0.04 [0.01, 0.08] | 0.01 [0.00, 0.01] | 0.08 [0.02, 0.17] |
| *codex* | 14227 (4429) | n/a | 0.27 [0.20, 0.34] | 0.11 [0.07, 0.15] | 0.03 [0.02, 0.04] | n/a |
| *gemini-cli* | 3353 (342) | n/a | 0.02 [0.02, 0.03] | 0.04 [0.03, 0.06] | 0.02 [0.01, 0.02] | n/a |
| *obsidian-linter* | 782 (42) | 0.09 [0.02, 0.29] | 0.01 [0.00, 0.02] | n/a | 0.02 [0.00, 0.05] | 0.11 [0.04, 0.46] |
| *ink* | 393 (74) | 0.22 [0.15, 0.32] | 0.03 [0.01, 0.07] | n/a | 0.12 [0.07, 0.21] | 0.34 [0.27, 0.52] |

Young histories are in italics; they were reported descriptively, as pre-registered.

**What the numbers mean.** A file alive at age $t_0$ survives to $2t_0$ with probability $2^{-a}$. That is about 96% at $a = 0.05$ and 80% at $a = 0.3$, against the baseline's 50%. In the five most persistent histories (git, vim, django, redis, postgres), between 54% and 82% of files are still alive at the oldest age with 50 at risk, which is 16 to 30 years. Cpython (9%) and ruby (16%) are the exceptions.

**$a(t_0)$ depends on age.** It rises in most histories, for example:

- django: 0.00 at 30 days, 0.15 at 4 years;
- git: 0.01 to 0.11 by 8 years;
- cpython and ruby: 0.74 and 0.95 at 8 years, with intervals that contain 1.

The rise is far slower than an exponential lifetime would give: over that range, a(t_0) would grow about a hundredfold. The pre-registered no-Lindy rule is met in 0 of 10 repositories in the calendar clock and 5 of 10 in the commit clock, below its threshold of 7.

**Following renames matters.** Without it, a rename counts as a death. Large-age $a$ then rises from 0.05 to 0.18 in git and from 0.13 to 0.27 in perl5.

**The two clocks agree within a factor of about two.** A non-uniform development pace across the whole repository is not what separates files from the baseline.

**How well the large-age summary tests each form.** My large-age summary averages $a(t_0)$ from one year up. That tests the scale-ignorance form, "at every age", directly. It tests the hazard-mixture form, "at large age", only if one year is a large age. §3 shows it is not.

## 3. Post-hoc: the segment's own hazard-mixture family

*Post-hoc, not pre-registered (`lifetimes.py posthoc`).* The segment's hazard-mixture route, with a Gamma prior on the hazard (shape $a$, scale $b$), gives $S(t) = (1+t/b)^{-a}$. The case $a = 1$ is the segment's exponential prior. Its median remaining life is $t_0 + b$, and it reaches the baseline once $t_0 \gg b$.

A rising $a(t_0)$ is what this family predicts for $t_0$ of order $b$. So, before reading the result as a refutation of the hazard form, I fitted the family to $\log Q$ over 30 days to the oldest age with 50 at risk, once with $a = 1$ and once with $a$ free. Least squares in $\log Q$, with a directory-cluster bootstrap of 200 replicates.

| Repository | $Q$ at oldest age | $a = 1$: $b$ in years [95%], rms | $a$ free: $a$ [95%], $b$ (years), rms |
|---|---|---|---|
| git | 0.82 | 81 [51, 116], 0.019 | 0.08 [0.05, 1.55], 2.7, 0.011 |
| cpython | 0.09 | 2.6 [1.1, 6.4], 0.376 | 0.31 [0.26, 0.75], 0.1, 0.168 |
| postgres | 0.54 | 24 [19, 29], 0.099 | 0.15 [0.13, 0.20], 0.6, 0.025 |
| django | 0.72 | 35 [30, 39], 0.049 | 0.15 [0.13, 0.17], 1.9, 0.019 |
| rails | 0.47 | 13 [11, 16], 0.116 | 0.18 [0.15, 0.22], 0.4, 0.020 |
| ruby | 0.16 | 8.0 [5.9, 10.0], 0.137 | unidentified; best fit is near-exponential (mean about 14 years), 0.091 |
| perl5 | 0.50 | 20 [15, 25], 0.161 | 0.13 [0.10, 0.16], 0.2, 0.027 |
| redis | 0.69 | 21 [8, 59], 0.110 | 0.07 [0.03, 0.15], 0.1, 0.014 |
| node | 0.30 | 5.2 [4.0, 6.9], 0.106 | 0.40 [0.31, 0.56], 0.9, 0.027 |
| vim | 0.77 | 66 [35, 194], 0.027 | 0.11 [0.01, unbounded], 3.1, 0.022 |

Read within the segment's own family:

- **With $a = 1$**, the scale $b$ is 3 to 80 years. So the baseline's "median remaining life equals age" would hold only for files much older than these histories, and for files younger than $b$ the median remaining life is about $b$ (cpython's $a = 1$ fit, with $b$ of 2.6 years, fits poorly anyway). Where $a = 1$ is forced, the segment's hazard form is instantiated with $b$ measured.
- **With $a$ free**, $a$ is 0.07–0.40 and fits better in every repository. Its rms residual is two to eight times smaller in seven of them (cpython, postgres, django, rails, perl5, redis, node); git and vim fit about as well either way. That is a prior density over the hazard that diverges at zero, the segment's "a prior that diverges there predicts a longer [future]".
- **Ruby** is better described by a near-exponential lifetime of about 14 years than by either.

Within this family the data cannot fully separate "$a = 1$ with $b$ of decades" from "small $a$" in git and vim, because nearly all their files are younger than any such $b$. In the other seven, small $a$ is clearly better. The pre-registered verdict stands as the headline. This section says what survives of the hazard form: the form survives with a measured parameter, and the uninformed baseline does not.

**What the deaths are.** Deaths by top-level directory at birth:

- *cpython:* 13,880 of its 26,849 lives, and 13,443 of its deaths, are in `Misc/`. These are news-entry files, born to be deleted at release, and they are not components. Its deaths at 8 years and older are in `Lib`, `Demo`, `Doc`, `Tools`, `Modules` and `Mac`: the Python 3 removals, the deleted `Demo/` and `Mac/` trees, and the dead-batteries removals.
- *ruby:* the late deaths are mostly `ext/` (1,289 of 2,668), where libraries were extracted into separately maintained gems.
- *node:* 74,000 of its 114,000 lives are vendored third-party code under `deps/`, replaced wholesale at each upgrade, and 22,000 are under `tools/`.

The segment's Discussion already treats a rewrite or relocation as information that overrides the uninformed prior. I did not rerun without `Misc/` or `deps/`. Those lives die young, so excluding them should lower young-age $a$ further. I have not checked what it does to the large-age figures, and that is the first thing a checker should do.

## 4. Feature counts

**The pre-registered bounds.** For files alive at a cut with $n_{\text{past}} \ge 5$ mainline changes, $L$ is the share that reached $n_{\text{past}}$ further changes by HEAD. $U$ is 1 minus the share deleted before doing so.

| Repository | cut | files | $L$ [95%] | $U$ [95%] |
|---|---|---|---|---|
| git | 1/3 | 953 | 0.45 [0.16, 0.58] | 0.92 [0.85, 0.95] |
| cpython | 1/3 | 1565 | 0.40 [0.26, 0.51] | 0.42 [0.29, 0.55] |
| postgres | 1/3 | 1676 | 0.62 [0.56, 0.67] | 0.80 [0.74, 0.85] |
| django | 1/3 | 3153 | 0.65 [0.62, 0.67] | 0.75 [0.72, 0.77] |
| rails | 1/3 | 1016 | 0.75 [0.71, 0.78] | 0.87 [0.83, 0.89] |
| ruby | 1/3 | 814 | 0.55 [0.42, 0.64] | 0.58 [0.45, 0.69] |
| perl5 | 1/3 | 840 | 0.78 [0.71, 0.83] | 0.86 [0.82, 0.90] |
| redis | 1/3 | 150 | 0.67 [0.49, 0.80] | 0.93 [0.84, 0.98] |
| node | 1/3 | 2427 | 0.48 [0.40, 0.57] | 0.69 [0.62, 0.76] |
| vim | 1/3 | 641 | 0.60 [0.46, 0.71] | 0.94 [0.86, 0.99] |

At the 1/2 cut, which has a shorter follow-up, $L$ is 0.17–0.57 and $U$ is 0.58–0.97. $L \gt 1/2$ holds in cpython and rails, and $U \lt 1/2$ holds nowhere.

**Applying the rule.** The rule reads: "If $U \lt 1/2$ in at least 7 of 10 repositories at both cuts, that counts against the count form. If $L \gt 1/2$ in at least 7 of 10, that counts against it in the other direction." The $L$ sentence carries no cut qualifier.

- *Read as written:* $L \gt 1/2$ in 7 of 10 at the 1/3 cut. That **counts against the count form in the direction of more changes than predicted.**
- *Read with "at both cuts" carried over from the first sentence:* $L \gt 1/2$ in only 2 of 10 at the 1/2 cut, so the result is **undecided**.

I wrote the rule and I will not choose between the readings after seeing the data. The checker and the lead should.

**What does not depend on the rule.** $L$ is a lower bound. Its interval excludes 1/2 from above in postgres, django, rails and perl5 at the 1/3 cut, and in rails at the 1/2 cut. In those repositories, $P(n_{\text{future}} \ge n_{\text{past}}) \gt 1/2$ is established for files with five or more changes. No repository's $U$ interval lies below 1/2 at either cut; only cpython's point estimate does, at the 1/3 cut (0.42, interval $[0.29, 0.55]$).

**A caveat.** A "change" here is a mainline event. A merged branch counts once, however many commits it holds.

**Exploratory.** This analysis was not pre-registered (`lifetimes.py explore`). It asks *when* such files reach $n_{\text{past}}$ more changes, in units of the file's age at the cut. The quantity is the Aalen–Johansen cumulative incidence $F(s)$, with deletion as a competing event.

- In every primary repository, $F(1)$, the share reaching it within one more age, is 0.04–0.40.
- $F$ reaches 0.5–0.9 by $s$ = 4–16 in all of them except cpython at the 1/3 cut (0.40). Few files remain at risk that far out.

So files that are still being changed receive about as many changes again as they have had, or more, over two to four times their age, not one.

## 5. What this does and does not reach

**What it reaches.** This instantiates the baseline on **components** (source files) of long-lived, maintained, many-author projects. It refutes the baseline as an uninformed default for how much longer such a component will exist, which is the time form applied as the Discussion applies it ("for this component").

**Feature counts.** The two forms err in the same direction. Files outlive the baseline. Where the follow-up is long enough to tell, actively changed files receive more future changes than the baseline's median. So for `#der-change-investment`, whose amortized threshold is linear in $\hat n_{\text{future}} = n_{\text{past}}$, the baseline is conservative here, not wrong in sign. The segment's own Working Note expected this ("if anything, the baseline *underestimates* the case for investment"), and these data are the first measurement of it.

**The uniform-feature-rate mapping fails at the file level in two ways:**

- files stop being changed long before they are deleted;
- while they are changed, the rate falls, so $n_{\text{past}}$ more changes take two to four ages to arrive, not one.

**What it does not test.** The claim about whole software systems. That needs repositories with observed ends.

**Known biases, and their directions.**

- *Rename detection in big commits.* Git skips rename detection in commits past its rename limit, which makes false deaths and pushes $a$ up.
- *Reverts.* A file deleted and re-added counts as a short life, which also pushes $a$ up.
- *Lives that are not components:* cpython's `Misc/`, node's vendored `deps/` and `tools/`. These die young; their effect on large-age $a$ is unchecked (§3).
- *Left truncation:* vim's and ruby's histories start with imports that are not first commits. The no-imports variant handles this, and it does not change the reading.

**Population.** The young set includes two agent-heavy histories, codex and gemini-cli. Codex has the highest young-age $a$ of all fourteen histories (0.27), so its files churn fastest. That is a descriptive observation about one repository, not a finding about AI-maintained code.

## 6. Prior art

A quick search found two bodies of work.

- **Whole projects.** Survival analyses of open-source projects: Samoladas et al. 2010; Ali et al., MSR 2020 ("Cheating Death"), on 3,052 Python projects; Robinson et al. 2022.
- **Lines of code.** Bernhardsson's git-of-theseus (2016) fits an exponential half-life to surviving lines, about 6 years for git; others report poor exponential fits.

I found no file-level measurement of the Lindy exponent. The search was quick, and F.2's discipline asks for a proper one before canon says "first". The line-level studies and these file-level numbers are compatible: lines churn while files persist.

## 7. What I would propose landing (not landed, per the lead)

**In `#der-change-expectation-baseline`, a `## Claim Record`** with three records.

1. *The derivation.*
   - *Register:* formal.
   - *Population:* lifetimes under scale ignorance, or under a hazard prior finite and positive at zero.
   - *Instantiated:* not applicable.
2. *The time form as a default for software components.*
   - *Register:* descriptive.
   - *False of:* source files in ten long-lived projects (`empirica:software-file-lifetimes`). There, $a(t_0)$ rises with age from about 0.01–0.2 at months to 0.1–0.95 at 8 years. The segment's own exponential-prior form fits with $b$ of 3–80 years, and a shape $a$ of 0.07–0.4 fits better.
   - *Falsifier:* $a(t_0)$ from version-control histories.
   - *Instantiated:* yes.
3. *The count form.*
   - *Register:* descriptive.
   - *Instantiated:* yes, on the same files. $P(n_{\text{future}} \ge n_{\text{past}}) \gt 1/2$ in four of ten projects for files with five or more changes, and undecided in the rest at this follow-up. That is, it errs conservative.

**In the Epistemic Status, one *[Empirical Claim]* paragraph** stating 2 and 3, scoped to source files. It would add that the uniform-feature-rate mapping fails for files, in both of the ways above.

**One Working Note** pointing to the next measurements (§8).

`status: exact` stays, since it describes the computation.

**Two questions are for the lead and Joseph:**

- whether the Discussion's "for this component" should be rescoped;
- whether the baseline should be stated directly in the feature clock rather than through lifetime plus a uniform rate.

## 8. What is left

- **An independent check.** It should cover:
  - the script against the pre-registration;
  - the count rule's two readings (§4);
  - the `rising` test in `summarize`, which demands a non-decreasing $a(t_0)$ and so is strict about noise;
  - a spot-check of lives against `git log` on a few files (I checked redis's record counts: 2,679 adds and 723 deletes in the dump reconcile with 2,569 lives and 631 deaths once the 110 first-commit files are excluded);
  - a rerun without cpython's `Misc/` and node's `deps/` and `tools/`.
- **The count form, pre-registered** on $F(s)$ at a fixed horizon, with the rule's cut qualifier written unambiguously.
- **The system-level test**, on repositories with observed ends, for example GitHub archives of dead projects or Software Heritage.
- **A proper prior-art search** for file-level survival (F.2).
- **Landing** (§7), after the lead and Joseph talk.

**Durability.** The scratchpad copies of the dumps and result JSONs will not outlive the session. The script and the HEADs in `RUNS.md` regenerate them in about ten minutes once the clones exist. Cloning the fourteen repositories took about 25 minutes, mostly node.
