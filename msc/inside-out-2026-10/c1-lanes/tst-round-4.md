*KR C.1 ("Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier") and KR H.2 ("every `old-*` file has a fate"). Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." — Joseph, 2026-10-30.*

# TST lane, round 4: what the third check changed, and what a verifier should look at

Written by the round-4 integrator (Claude Opus 5.5, also round 3's) for the lead and for the independent verifier who comes next. Input: the third check, `c1-lanes/tst-check-3.md` with its record `reviews/tst-lane-check-3.md`. The landing is `0201c156`, rebased onto main at `eba69748` before the record was taken; my re-runs and re-derivations are typed in `reviews/tst-lane-round-4-integration.md` (C1–C5). The check found five things. All five held when re-derived, and two came out stronger than proposed.

## F1: the baseline is a consequence of scale ignorance again, exactly

The check is right, and it answers the question I left open in round 3. I read Caves's Eqs. 20, 23 and 31–32 again and re-derived them. A system found in progress has lifetime density proportional to $T\,w(T)$ and, given its lifetime, uniform age. So the uniform-age likelihood is not peculiar to per-system sampling: it holds for the system in front of you under either sampling. Jeffreys' prior placed on that system's lifetime gives $t_0/T^2$ exactly, at every age. Round 3's "scale ignorance alone gives no baseline" was true only of Jeffreys' prior placed on the all-systems density $w$, and that is how it now reads, in one sentence. Placed on the system in progress, the same assumption is $w \propto T^{-2}$, whose survival function is $1/t$ exactly: the tail round 3 assumed, now derived.

So round 3 overcorrected. The segment's original Jeffreys derivation was right once its prior is read as being about the system in front of you, and the segment is restructured around that reading:

- **Main derivation:** scale ignorance about the lifetime of the system found in progress. Exact at every age; improper prior, proper posterior.
- **"Whose lifetime the prior is about":** under a constant birth rate, the posterior given age is $w(T)/Q(t_0)$, whatever the mean lifetime. Any $1/t$ tail gives the baseline at large age, Jeffreys on the system in progress is $w \propto T^{-2}$, and Jeffreys on $w$ does not normalize. The birth-rate premise replaces round 3's "span much longer than lifetimes", which the check showed a $1/t$ tail cannot satisfy (F1(a)).
- **The hazard mixture**, kept as the proper prior with the same tail.
- **Epistemic Status** carries Caves's caveat that scale-freeness "must be judged case by case". A system with an evident time scale, such as a fixed contract term or a platform's announced end of support, is not scale-free, and the uninformed baseline does not apply to it. That a developer's ignorance concerns the system in front of them remains the segment's reading of the situation, marked as such.

A population simulation backs the derivation (C1). Systems begin at a constant rate with lifetimes from $w \propto T^{-2}$; among those alive at a given age, the median remaining life over age is 0.94–1.03, against 0.94–0.99 exact for the truncated $w$, and the alive population is flat in $\log T$. `#der-dual-optimization`'s prior-art row now names both routes; `FINDINGS.md` was regenerated (two lines).

## F2: persistent source miscalibration

The check's sentence holds, and I extended it to systematic misalignment, which persists across a source's messages for the same reason. Repeated messages from one biased source carry information about the quantity that saturates at precision $1/U_{\text{src},j}$ (with the prior, at $1/U_0 + 1/U_{\text{src},j}$). An update that charges $U_{\text{src},j}$ afresh to each message drives $U_{M_i}$ toward zero while the error stays at the bias. The numbers in C3: exact variance falls to the floor 0.2000; the fresh-noise update reaches 0.000075 after 10,000 messages. $U_{\text{src},j}$ now belongs in the trust meta-model as persistent state.

## F4: a criterion instead of "reject it in none"

Choosing a threshold would only have answered the reader's question by fiat. The section (7) null replicates produce all eight readings (four caps, $a$ and $b$) jointly, so I calibrated each history's smallest tail share against the null replicates' own smallest. That handles the correlation exactly, with no Bonferroni guess. The toolkit now prints it. The null matches the observed smallest share in 4.7% of replicates for the corpus, 5.8% for obsidian-linter and 6.2% for ink. All three sit at the edge of a 5% test, within Monte Carlo error (0.007 at 1,000 replicates). Neither round 2's "rejects" nor round 3's "rejects in none" was right as a clean statement. Item 3 now gives the numbers and says the capped fits lean against an exponential in every history and, alone, settle it in none. The window-free test in obsidian-linter remains what rejects the exponential there.

## F3 and F5: ink

- **F3.** Item 1 and the README now read ink's two top bins by their intervals (5–37 and 1–137 minutes), not their point medians.
- **F5.** Section (6) of the toolkit now refits each one-idle form from 30 random starts and prints whether the best fit swaps labels. In obsidian-linter and the corpus the reported fits are the best found. In ink every form's best fit swaps labels and beats the reported fit by 1.4–2.1 in log-likelihood. Limits says this and calls ink a history where the method cannot separate work from time away, which answers the question of whether ink keeps its place: it stays, read as that. My round-3 record's C3 had recorded `confirmed` where ink's answer was no; I annotated it to read *narrowed*.

## Also

- **README, the checker's observation:** equal author and commit dates do not mark squash merges, since most direct commits have them too. The committer does (the web interface's merge for all 63 in obsidian-linter and 191 in ink).
- **Toolkit:** every line the round-3 script printed is unchanged (C4, by `diff`). `mixture_em` gained an optional random start and a floor of $10^{-3}$ on its scales, which changes no reported fit.
- **The section (7) null.** I take the checker's view, that the unconstrained best-fitting exponential is the right null. Its odd shape stays in the README as an argument about the form, not as a tail share.
- **The influx:** none of F1–F5 appears in `influx-scout/firmatum-vivarium.md` or `periphery.md`.

## vsect

- Taken in as *redefined*: `#der-change-expectation-baseline`, `#hyp-communication-gain`, `#hyp-exponential-cognitive-load`, `#der-dual-optimization`. Checks on the old texts wait for a second mind.
- Check 3's findings this landing answers, for someone other than me to close against `0201c156` (or its merged equivalent): `review:tst-lane-check-3#C4` (F5), `#C5` (F3, F4), `#C6` (F2), `#C8` (F1), `#C9` (F1 (a)).
- The record was taken after rebasing, as asked. `vsect take` noted that `0201c156` is not yet on origin/main and kept the text the checks read under `.vsect/objects/`.

## What I would look at, if I were the verifier

1. **The restructured baseline.** Does the "Whose lifetime the prior is about" subsection's item 2 follow from item 1 and the constant birth rate? Is the case-by-case caveat in Epistemic Status the right scope for TST's use of the baseline downstream (`#der-change-investment`)?
2. **The calibrated test in section (7).** Is a min-p over eight readings, calibrated by the same replicates, the right statistic? The replicates use their own empirical distribution to compute their tail shares, which is standard but slightly conservative.
3. **Whether ink should keep feeding numbers into item 2's "not distinguished" sentence at all**, now that Limits says its mixture fit is a chosen local optimum.

I am staying on the line for follow-ups.
