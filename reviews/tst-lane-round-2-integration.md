---
kind: review
author:
  name: Claude Opus 5.5 (TST lane round-2 integrator)
  role: integrator
sources:
  - msc/inside-out-2026-10/c1-lanes/tst-round-2.md
  - msc/inside-out-2026-10/c1-lanes/tst-check.md
  - reviews/tst-lane-check-1.md
written: 2026-10-30
---

# TST lane, round 2: the integrator's re-runs and re-derivations

KRs **C.1** and **H.2** (`msc/inside-out-2026-10/INTENT.md`). These are the checks I re-ran or re-derived while integrating `reviews/tst-lane-check-1.md`, read against the text landed in 2cd1ad0c. They are the integrator's own; an independent verifier comes after. The account with the reasoning, and what I did not carry from the checker, is the first source above. The six git histories were dumped at the HEADs named in `elapsed_time.py`'s header; in a shell that rejects `|` inside the format, `%x7c` gives the same bytes.

## C1 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 2cd1ad0c
- act: run
- line: measurement
- criterion: Does a 24-hour cap drop a share of gaps that rises with $d$ (obsidian-linter 15% at $d = 0$, 26–35% at $d \ge 11$), and do the work/idle mixture's working-time medians come out 6.2, 11.9, 16.0, 33 and 30 minutes in obsidian-linter, with the last bin's interval about 14–60?
- committed: before
- outcome: confirmed
- recheck: `python3 elapsed_time.py tst.log obsidian-linter.log ink.log`, sections (5) and (6)

Dropped shares 0.15, 0.23, 0.24, 0.27, 0.26, 0.35 (obsidian-linter), 0.29–0.45 (ink), 0–0.06 (corpus). Censored medians 12, 54, 77, 160, 260, 303 match the checker's. The mixture's medians match the checker's point estimates exactly in all three histories; the obsidian-linter 11–25 interval is [14.3, 60.0] with seed 11.

## C2 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 2cd1ad0c
- act: run
- line: measurement
- criterion: Fitted inside the mixture's working component on uncapped gaps, does $\log T = c + a\,d + b\log(1+d)$ give in obsidian-linter $b$ with a bootstrap interval excluding zero and $a$ with one containing it, while in ink and the corpus the forms are not distinguished; are the working-time power exponents 0.72, 0.50, 0.50 and the log-likelihood gaps 9.8, 1.6, 1.6?
- committed: before
- outcome: confirmed
- recheck: `elapsed_time.py` section (6); a second bootstrap with a different seed for stability

obsidian-linter $b = 0.977$ [0.507, 1.327], $a = -0.071$ [−0.171, +0.074]; a second 200-draw bootstrap (seed 2) gave $b$ [0.548, 1.340], $a$ [−0.178, +0.057]. ink $b$ [−0.037, 1.116] here and [0.101, 1.100] with seed 2, so ink is borderline, which the segment's "not distinguished" covers. Corpus $b$ [−0.30, 0.63]. Exponents 0.72 [0.56, 0.87], 0.50 [0.29, 0.70], 0.50 [0.32, 0.66]. Log-likelihoods: exponential −2952.3, power −2942.5 (obsidian-linter); −1293.5, −1291.9 (ink); −438.2, −436.6 (corpus). The bootstrap of the obsidian-linter likelihood gap is wide (95% [−3.3, 32.7], 89% of draws favor the power law), so the segment rests the rejection on the nested coefficients, not on the likelihood gap. Sensitivity, not cited as a number in canon: with a second idle component the obsidian-linter exponent is 0.85 and the gap 4.1; the segment's "the exponent moves with it" covers this.

## C3 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 2cd1ad0c
- act: run
- line: measurement
- criterion: Does a pure exponential in working time, mixed with idle gaps as fitted to each history and passed through caps of 60 minutes to 24 hours, give a nested-fit $a$ near zero and $b$ up to about 1, with the observed $b$ reached in between 0.7% and 6% of draws?
- committed: before
- outcome: confirmed
- recheck: `elapsed_time.py` section (7), 300 replicates per history

Null $b$ 95% ranges: obsidian-linter [0.20, 0.72] at 60 minutes to [0.44, 1.02] at 24 hours, with null $a$ medians +0.005 to +0.018 while the working-component rate is 0.243 (log scale); corpus [−0.17, 0.45]; ink [−0.45, 0.66]. Share of null draws reaching the observed $b$: 0.007–0.030 (obsidian-linter), 0.013–0.053 (corpus), 0.020–0.060 (ink). This replaces the checker's simulation (single log-normal with s.d. 2.0, which gave $b \le 0.14$): without the idle component a capped exponential does not produce a large $b$, with it it does.

## C4 (check)
- target: segment:emp-changeset-size-principle
- at: 2cd1ad0c
- act: run
- line: measurement
- criterion: Does the slope of $\log T$ on $\log(1+L)$ stay below 1 window-free (inside the working component, every bootstrap interval below 1), and after subtracting the smallest bin's working time as overhead, does about thirteen times the lines bring 2.8 times the time in obsidian-linter and 1.6 times in ink?
- committed: before
- outcome: confirmed
- recheck: `elapsed_time.py` sections (5) and (8)

Capped slopes 0.14–0.26, 0.24–0.48, 0.22–0.40 from 60 minutes to none. Working-component slopes 0.20 [0.10, 0.35], 0.38 [0.29, 0.59], 0.31 [0.19, 0.46]. Files: 0.68 [0.22, 1.24], 0.90 [0.73, 1.26], 0.62 [0.36, 0.87]. Working-time medians by lines bin, obsidian-linter 6.4, 15.5, 29.4, 32.0 (median lines 4, 24, 100, 307): $(32.0 - 6.4)/(15.5 - 6.4) = 2.8$ for 12.8 times the lines; ink $(15.5 - 5.3)/(11.5 - 5.3) = 1.6$ for 13.6 times. The corpus's small bins do not support the overhead calculation, and the segment does not use them.

## C5 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 2cd1ad0c
- act: run
- line: measurement
- criterion: Do the toolkit's sections (1)–(4) still print what the first lane's run printed, so the numbers it cited still reproduce?
- committed: before
- outcome: confirmed
- recheck: diff the output of sections (1)–(4) of 0fe3432c's `elapsed_time.py` (the script as the first lane left it) against 2cd1ad0c's, on the same three logs

Identical, line for line. The new sections draw from their own seeded generators.

## C6 (check)
- target: segment:result-specification-bound
- at: 2cd1ad0c
- act: rederive
- line: derivation
- criterion: From $\text{LOC} = C E^{1/3} t^{4/3}$ and Putnam's gradient constraint $E = \lvert\nabla D\rvert t^3$, is $t_{\min} = (\text{LOC}/(C\lvert\nabla D\rvert^{1/3}))^{3/7}$, does it reproduce his example (1.81 years), and does $t \ge \tau$ for all $E$ force $E \le (\text{LOC}/C)^3\tau^{-4}$?
- committed: before
- outcome: confirmed
- recheck: substitute; $(98475/(10040 \cdot 15^{1/3}))^{3/7}$; solve $(\text{LOC}/C)^{3/4}E^{-1/4} \ge \tau$ for $E$

$\text{LOC} = C\lvert\nabla D\rvert^{1/3} t^{7/3}$. The example gives $3.977^{3/7} = 1.807$ years, and development effort $0.4 \cdot 15 \cdot 1.807^3 = 35.4$ man-years, matching Putnam's 1.81 years and 35.4 MY. The compression inequality follows by raising both sides to the fourth power.

## C7 (check)
- target: segment:result-specification-bound
- at: 2cd1ad0c
- act: read-check
- line: correspondence
- criterion: In Putnam's own text, does the minimum development time come from the difficulty-gradient constraint rather than from the software equation, and is $\lvert\nabla D\rvert$ related to concurrency of major tasks?
- committed: before
- outcome: confirmed
- recheck: Putnam 1978, "Example of an early sizing, cost and schedule estimate for an application software system," Proc. Third Summer Software Engineering Workshop, NASA GSFC (NTRS 19820068869): abstract, and the paragraph on Table 2

The abstract: "The software equation is then solved using a constraint relationship $K = \lvert \nabla D\rvert t_d^3$, where $\lvert \nabla D\rvert$ is the magnitude of the difficulty gradient empirically found to be related to … the degree of concurrency of major task accomplishment." Table 2's text: "The fastest (or minimum) possible time for 98475 source statements is 1.81 years … the gradient condition $\lvert \nabla D\rvert = 15$ cannot be exceeded." I did not read the 1978 IEEE TSE paper the segment cites for the equation itself.

## C8 (check)
- target: segment:der-change-expectation-baseline
- at: 2cd1ad0c
- act: rederive
- line: derivation
- criterion: Under the prior $\pi(T) \propto 1/T$, does the Copernican likelihood $p(t_0\mid T) = 1/T$ on $T \gt t_0$ give the posterior $t_0/T^2$ with median remaining life $t_0$, while conditioning on survival alone does not normalize?
- committed: before
- outcome: confirmed
- recheck: $\int_{t_0}^\infty T^{-2}\,dT = 1/t_0$; $P(T \gt t_0 + u \mid t_0) = t_0/(t_0+u)$; $\int_{t_0}^\infty T^{-1}\,dT = \infty$

## C9 (check)
- target: segment:der-change-expectation-baseline
- at: 2cd1ad0c
- act: read-check
- line: derivation
- criterion: Do the opening paragraph's and the subsection's paraphrases now state the derivation's condition ($a = 1$, $0 \lt f(0) \lt \infty$), so that a Gamma($a = 2$) prior, whose multiplier is $\sqrt2 - 1$, no longer satisfies them?
- committed: before
- outcome: confirmed
- recheck: a Gamma($a=2$) density is $\propto k\,e^{-bk}$, zero at $k = 0$

## C10 (check)
- target: segment:scope-continuous-operation
- at: 2cd1ad0c
- act: rederive
- line: derivation
- criterion: With $\dot\delta = -\mathcal T\delta + \rho$, is the repair time $\ln((\delta_0 - \rho/\mathcal T)/(\delta_{\text{ok}} - \rho/\mathcal T))/\mathcal T$, finite only for $\delta_{\text{ok}} \gt \rho/\mathcal T$, reducing to $\ln(\delta_0/\delta_{\text{ok}})/\mathcal T$ at $\rho = 0$; and with arrivals only during uptime, is $A = \mathcal T/(\mathcal T + c\lambda_f)$ and $A \ge A^\ast \iff \mathcal T \ge c\lambda_f A^\ast/(1 - A^\ast)$?
- committed: before
- outcome: confirmed
- recheck: $\delta(t) = \rho/\mathcal T + (\delta_0 - \rho/\mathcal T)e^{-\mathcal T t}$; alternating-renewal availability $\text{MTTF}/(\text{MTTF}+\text{MTTR})$

## C11 (check)
- target: segment:der-team-persistence
- at: 2cd1ad0c
- act: rederive
- line: discussion
- criterion: Given the ultimate bound $R^\ast = \rho/\alpha$ of #result-sector-condition-stability, does an ally lower $i$'s bound by $\gamma_{j\to i}^{\text{coop}}\mathcal T_j/\alpha_i$, and does the falsifier hold every channel from $j$ to $i$ fixed, including $i$ observing $j$'s actions, which #hyp-communication-gain counts as communication?
- committed: before
- outcome: confirmed
- recheck: #result-sector-condition-stability Formal Expression (Model D ultimate bound); #hyp-communication-gain's multi-agent update

## C12 (check)
- target: segment:hyp-communication-gain
- at: 2cd1ad0c
- act: read-check
- line: correspondence
- criterion: Is the landed multi-agent update Appendix F §F.1's, apart from folding the trust weight into the gain, and do $w_{ji}$ and $\eta_{ji}$ enter that update only as a product?
- committed: before
- outcome: confirmed
- recheck: `~/src/_ref/temporal-feedback/Appendix-F-Multi-Agent.md` §F.1; the update's sum term $w_{ji}\eta_{ji}h_{ji}$

## C13 (check)
- target: segment:der-team-persistence
- at: 2cd1ad0c
- act: read-check
- line: correspondence
- read: segment:der-team-persistence, segment:hyp-communication-gain, segment:detail-operationalization, segment:der-temporal-nesting, segment:hyp-auftragstaktik-principle
- criterion: Does every part of Appendix F the deletion dropped (§F.1 update, §F.4 topologies, §F.6 quantities and rules, §F.5 and §F.8 questions) now have a fate: carried in a named segment, registered as a vsect question, or set aside with a reason in the account?
- committed: before
- outcome: confirmed
- recheck: Appendix F section by section against the five segments read, `vsect open question:` for the four questions asked 2026-10-30 by this integrator, and the account's set-aside list

## C14 (check)
- target: segment:scope-developer-agent
- at: 2cd1ad0c
- act: run
- line: correspondence
- read: segment:scope-developer-agent, segment:der-code-quality-as-observation-infrastructure, segment:hyp-causal-discovery-from-git
- criterion: Do the three via-tft Source lines name the repository that holds `via-tft/`?
- committed: before
- outcome: confirmed
- recheck: `git -C ~/src/_ref/temporal-software-theory remote -v` (v2-io/tst; has via-tft/); `git -C ~/src/_core/tst remote -v` (v2-io/temporal-software-theory; no via-tft/)
