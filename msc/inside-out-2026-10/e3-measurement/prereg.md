*KR E.3 ("One of Volume 2's cheap falsifiers is run on a real codebase history"), under objective E ("One quantity is measured on an agent the theory did not construct"). Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." — Joseph, 2026-10-30.*

# E.3 pre-registration: does a source file's remaining life equal its age?

Written by the E.3 agent (Claude Opus 5.5) on 2026-10-30, before any lifetime was extracted from any repository. The only data seen so far is one commit count (redis, 13,393), taken while checking that cloning works. This file is committed before the extraction script runs, and the commit hash is the evidence of that ordering. Anything decided after the data was seen will be listed in the account (`account.md` beside this file) as a departure, with its reason.

## 1. The claim under test

`#der-change-expectation-baseline` derives, under scale ignorance about the lifetime of the system in front of you, $P(T \gt t_0 + u \mid t_0) = t_0/(t_0+u)$ at every age. The median remaining lifetime then equals the current age. Under the hazard-mixture form, the same holds at large age whenever the prior density of the termination hazard is finite and positive at zero. More generally, if the lifetime survival function falls as $t^{-a}$, the median remaining life is $(2^{1/a}-1)\,t_0$. The segment names $a$ as "the single thing an informed analyst would need to know to move the baseline's multiplier". The derivation is exact. As a description of software, it is an empirical prediction (owner review, `owner-review/explorers/part-iii-and-vols-2-4.md` §2.2 and §3.3, item 3), and that prediction is what this tests.

## 2. The population, and what a result here does and does not reach

**Unit.** A source file in the mainline history of a git repository, from the commit that adds it to the commit that deletes it. A rename continues the same life. A file still present at HEAD is right-censored there.

**Why this unit.** File births and deaths are recorded exactly, they are abundant (thousands per history), and censoring at HEAD is administrative: it depends only on when the file was born, not on its fate. A file is a component of a system, and the segment's Discussion applies the baseline to components ("what information justifies $\hat n_{\text{future}} \gt n_{\text{past}}$ for this component?").

**What it does not reach.** The segment's headline is about "a software system". A whole system's lifetime needs a corpus of repositories with observed ends, which this run does not attempt; it stays an open item. I write both halves down now:

- If file lifetimes follow the baseline, that instantiates the scale-free-survival mechanism on components of real systems. It does not confirm the system-level claim.
- If file lifetimes depart from the baseline, the baseline is refuted *as an uninformed default for components*. That is the use the Discussion makes of it, and the one `#der-change-investment` builds on. It does not by itself refute the system-level claim.

**Lifetime is not the feature count.** The segment maps lifetime to feature count only under a uniform feature rate, a step tagged *[Derived (Conditional on uniform feature rate)]* that the Working Notes call the weakest link. The primary test is on lifetime. Section 5's secondary test is on feature counts.

## 3. Repositories, chosen before cloning

**Primary set: ten long-lived, many-author projects, maintained to 2026.** Maintenance matters because it makes HEAD a censoring point rather than a death. The set spans languages, domains and VCS ancestry (several were converted from CVS or Subversion with their dates kept):

- git/git (2005)
- python/cpython (1990)
- postgres/postgres (1996)
- django/django (2005)
- rails/rails (2004)
- ruby/ruby (1998)
- Perl/perl5 (1987)
- redis/redis (2009)
- nodejs/node (2009)
- vim/vim (2004)

All are cloned from GitHub at their default branch's HEAD on 2026-10-30, and RUNS.md records each HEAD sha.

**Secondary set: young histories.** openai/codex, google-gemini/gemini-cli, platers/obsidian-linter and vadimdemedes/ink. Two of them are squash-merged. Squash merging distorts inter-commit time gaps, which is why the TST lane's elapsed-time study excluded these histories. It does not move the dates on which a file is added or deleted on the mainline, so they are usable here. They reach only small ages.

A repository is dropped only if extraction fails for a technical reason, and the reason is recorded.

## 4. Extraction rules, fixed in advance

- **History.** The mainline only: `git log --first-parent -m -M --name-status`, oldest first. Merges are diffed against their first parent, so each file event is dated by the commit that brought it into the mainline. Dates are committer dates. Where a mainline commit's date precedes its parent's, the running maximum is used, and the count of such commits is reported.
- **Lives.** A file is born at an `A` and dies at a `D`. An `R` record (git's default similarity threshold, 50%) carries the life to the new path. A path re-added after deletion starts a new life. `M` and `T` records do not affect a life.
- **Left truncation.** Files added by the repository's first mainline commit are excluded: their birth precedes the history.
- **Sensitivities, reported beside the primary numbers.** (i) Without rename following (`--no-renames`), where a rename is a death and a birth. (ii) Excluding lives born in commits that add more than 1,000 files, which are imports and vendoring whose files have a history elsewhere.
- **Clocks.**
  - *Calendar:* days of committer time.
  - *Commit:* the number of mainline commits elapsed, which measures the project's own activity.

  The theory's lifetime claim is clock-free, so each clock is a test of it. Where the two disagree, the disagreement shows how much a non-uniform development rate matters.

## 5. Estimands, estimators and inference

**Survival.** $Q(t)$ is the Kaplan–Meier estimate of a file's survival as a function of age $t$ since birth. Censoring is at HEAD.

**Local exponent: the primary estimand.**

$$c(t_0) = \frac{Q(2t_0)}{Q(t_0)}, \qquad a(t_0) = -\log_2 c(t_0).$$

$c(t_0)$ is the probability that a file alive at age $t_0$ survives as long again. Read against the hypotheses:

- **The baseline, at every age:** $c(t_0) = 1/2$, so $a(t_0) = 1$ at every $t_0$.
- **The hazard form:** $a(t_0) \to 1$ at large $t_0$.
- **A tail $t^{-a}$:** $a(t_0) \to a$.
- **Exponential lifetimes (no Lindy effect):** $a(t_0) = k\,t_0/\ln 2$, which grows in proportion to age.

**Grids.**

- *Calendar:* $t_0 \in$ {30, 90, 180, 365, 730, 1461, 2922, 5844} days.
- *Commit:* $t_0 \in$ {30, 100, 300, 1000, 3000, 10000, 30000} mainline commits.

$a(t_0)$ is reported only where at least 50 lives are at risk at $2t_0$.

**Large-age summary per repository.** $\bar a_r$ is the mean of $a(t_0)$ over the estimable calendar ages $t_0 \ge 365$ days. In the commit clock it is the mean over $t_0 \ge 1000$ commits.

**Tail slope (secondary).** The least-squares slope of $\log Q$ on $\log t$ over the range from 1 year to the largest age with at least 50 lives at risk. The commit clock uses the range from 1,000 commits up.

**Inference.** A cluster bootstrap that resamples directories: the parent directory of the file at birth, so lives born together in one directory travel together. Deletions cluster by directory (moves, purges), and an i.i.d. bootstrap over files would understate the uncertainty, as the TST lane found with author-days. The bootstrap uses 1,000 replicates with percentile 95% intervals. The seed is keyed per repository and clock: the first 8 hex digits of `sha256("E3:<repo>:<clock>")`, read as an integer. RUNS.md records the seeds.

**Secondary: feature counts.** At calendar cuts at 1/3 and 1/2 of each repository's history span, take the files alive at the cut with $n_{\text{past}} \ge 5$ mainline commits touching them (the birth commit included), and ask whether they receive at least $n_{\text{past}}$ more. The lower bound $L$ is the share that does so by HEAD. The upper bound $U$ is 1 minus the share deleted before doing so. The baseline predicts $P(n_{\text{future}} \ge n_{\text{past}}) = 1/2$. Files still alive at HEAD without reaching $n_{\text{past}}$ more are undetermined, which is why only bounds are given.

## 6. What would count for and against: decision rules, primary set, per clock

The decision-relevant quantity is the median multiplier $2^{1/a}-1$. A factor of two either way changes a structural-investment decision. So the band $[1/2, 2]$ on the multiplier, which is $a \in [0.63, 1.71]$, is the line between "a different constant" and "a different law".

| Outcome | Rule (on $\bar a_r$ and its 95% interval, over the ten primary repositories) | Reading |
|---|---|---|
| **Consistent** | The interval contains 1 in at least 7 of 10 | The baseline is instantiated for file lifetimes in this clock |
| **Narrowed** | Neither row above nor row below | Lindy-form survival with a population-specific multiplier: the measured range of $\bar a_r$ is what the segment should carry, and the ignorance premise ($f(0)$ finite, positive) does not fit files exactly |
| **Against** | The interval lies wholly outside $[0.63, 1.71]$ in at least 7 of 10, all on the same side | The baseline is refuted as an uninformed default for software components, in the stated direction (above: files die sooner than their age predicts; below: they outlive it) |
| **No Lindy effect** | In at least 7 of 10, $a(t_0)$ at the largest estimable age is at least 3 times $a(365\ \text{days})$, rising with age | Lifetimes are closer to exponential than to any power law. This refutes the mechanism, not only the multiplier |

**"At every age" versus "at large age".** The same rules are applied separately to $\bar a_r^{\text{young}}$, the mean of $a(t_0)$ over $t_0 \in$ {30, 90, 180} days (commit clock: {30, 100, 300}). If the young-age reading differs from the large-age one, that separates the segment's two forms: the young ages bear on the every-age form, and the large ages on the hazard form.

**Feature counts (secondary).** If $U \lt 1/2$ in at least 7 of 10 repositories at both cuts, that counts against the count form. If $L \gt 1/2$ in at least 7 of 10, that counts against it in the other direction. Otherwise the result is undecided at this follow-up, and $[L, U]$ is reported.

**The secondary set** is reported descriptively. Its ages are too short for the large-age rules.

## 7. My own expectation, so a reader can see my bias

I expect files to outlive the baseline at large ages: few files in a long-lived project are ever deleted, and a deletion hazard that falls with age suggests $a \lt 1$, perhaps around 0.5. At young ages I expect early churn and $a$ nearer to or above 1. In the commit clock I expect a lower $a$ than in the calendar clock in projects whose commit rate has grown. For the count form I expect $L$ well below $1/2$, because a file's changes come mostly early in its life, and $U$ near 1, so the result there will be undecided. I hold these loosely, and they are not the prediction under test: the segment's is.

## 8. Where results go

- The run is registered as `empirica/software-file-lifetimes/`: the MANIFEST, the script, and RUNS.md with HEAD shas, seeds and an output digest.
- The account goes in `msc/inside-out-2026-10/e3-measurement/account.md`.
- The finding goes where the theory carries it: an *[Empirical Claim]* in `#der-change-expectation-baseline`'s Epistemic Status, citing `empirica:software-file-lifetimes`, whichever way it comes out, and a vsect check or item on the segment. `status: exact` describes the computation and is not touched by this.
