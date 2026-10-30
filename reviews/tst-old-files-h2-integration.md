---
kind: review
author:
  name: Claude Opus 5.5 (TST lane integrator)
  role: integrator
sources:
  - msc/inside-out-2026-10/c1-lanes/tst.md
written: 2026-10-30
---

# TST lane, H.2: checks made while giving the `old-*` files their fates

KRs H.2 and C.1. Reading the 44 `old-*` files against canon (commits `2d204811`, `de218fb0`) turned up two defects in live text, one strengthening, and one further measurement. It also changed text that two of the A13 checks had read, so those checks are taken again here at the new versions. The account in the source above has the per-file fates. Every check below was made by the integrator who wrote the text it concerns, except C1 and C2, which concern text written before this effort. An independent verifier comes after.

## C1 (check)
- target: segment:result-specification-bound
- at: 60162347
- act: read-check
- line: discussion
- criterion: Is $t_{\min} \approx (\text{time}_{\text{specify}})^{3/4}$ "Putnam's empirical finding", as the paragraph tagged *[Empirical Claim — historical observation]* states?
- committed: before
- outcome: broken
- recheck: compare the sentence with Putnam's software equation $\text{LOC} = C E^{1/3} t^{4/3}$ (Putnam 1978, IEEE TSE SE-4(4)) and with the derivation in TST's original T-02 (temporal-software-theory, `vault/02-theory/theorems/`)

Putnam fitted $\text{LOC} = C E^{1/3} t^{4/3}$; the floor $(\text{LOC}/C)^{3/4}$ is his. Reading it as $(\text{time}_{\text{specify}})^{3/4}$ is TST's own conjecture: the original T-02 derives it by "algebraic substitutions assuming specification complexity scales with system size" and calls it a possibility. Replaced in `2d204811`: Putnam's fit stays an Empirical Claim, and the reading becomes a Hypothesis naming its two unshown premises.

## C2 (check)
- target: segment:def-causal-information-yield
- at: 60162347
- act: read-check
- line: discussion
- criterion: Are "distributed tempo, topology analysis, and game-theoretic integration" Part III content "not yet fully extracted" from `src/old-tf-appendix-f-multi-agent.md`, as the Discussion body says?
- committed: before
- outcome: broken
- recheck: read #der-team-persistence (distributed tempo, team persistence, coordination overhead) and #hyp-communication-gain (trust meta-model, transitive and risk-adjusted trust, game-theory boundary) against Appendix F §F.2–F.5

Distributed tempo and the game-theory boundary are carried. Of the topology section, the hierarchical case is carried by #der-temporal-nesting and #hyp-auftragstaktik-principle. The peer-network diagnostic was not carried and was landed in #der-team-persistence in `de218fb0`, along with the F.7 falsifiers. The sentence was replaced in `de218fb0`.

## C3 (check)
- target: segment:der-change-expectation-baseline
- at: 2d204811
- act: rederive
- line: derivation
- criterion: For $S(t) = \int_0^\infty f(k)e^{-kt}dk$ with $f(k) \sim c k^{a-1}$ at $0^{+}$, is $S(t) \sim c\Gamma(a)t^{-a}$, so that the median remaining age is $\sim (2^{1/a}-1)t_0$; and is the exponential prior exact at every age with median $t_0 + b$?
- committed: after
- outcome: confirmed
- recheck: Watson's lemma; then the numerical check below

Derivation: substitute $u = kt$, $S(t) = t^{-1}\int_0^\infty f(u/t)e^{-u}du$; with $f(u/t) \sim c(u/t)^{a-1}$ this is $c\,t^{-a}\int_0^\infty u^{a-1}e^{-u}du = c\Gamma(a)t^{-a}$. Conditional survival $S(t_0+x)/S(t_0) \to (t_0/(t_0+x))^a$; setting it to $\tfrac12$ gives $x = (2^{1/a}-1)t_0$. For $f(k) = be^{-bk}$, $S(t) = b/(b+t)$ exactly. Numerical check, quadrature in $u$, median solved by root-finding, ages $10, 10^2, 10^3, 10^4$, ratio median/age:

| prior | $10$ | $10^2$ | $10^3$ | $10^4$ | limit |
|---|---|---|---|---|---|
| exponential, $b = 2$ | 1.200 | 1.020 | 1.002 | 1.000 | 1 (exact $1 + b/t_0$) |
| Gamma $a = 2$, $b = 2$ | 0.497 | 0.422 | 0.415 | 0.414 | $\sqrt2 - 1$ |
| Gamma $a = \tfrac12$, $b = 2$ | 3.600 | 3.060 | 3.006 | 3.001 | 3 |
| uniform on $[0,1]$ | 1.000 | 1.000 | 1.000 | 1.000 | 1 |
| half-normal, $s = 0.3$ | 1.139 | 1.002 | 1.000 | 1.000 | 1 |
| lognormal, $s = 1$, scale $0.1$ | 1.266 | 0.422 | 0.216 | 0.138 | 0 |

## C4 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 2d204811
- act: run
- line: measurement
- criterion: Do the Discussion's elapsed-time findings (Spearman 0.27–0.45, partial 0.10–0.37; exponential coefficient $a$ zero or negative and $b$ 0.38–0.92 in the nested regression; power slope 0.4–0.7; obsidian-linter medians 8.5, 22.8, 28.2, 71, 70) reproduce from the histories named in `elapsed_time.py`?
- committed: after
- outcome: confirmed
- recheck: as in `reviews/hyp-exponential-cognitive-load-a13-rerun.md` C2

Taken again because the segment's text changed after that check (a paragraph on the reading-side operationalization and a Working Note on agent cost profiles were added). The measurement paragraph is unchanged, and the run output matches it.

## C5 (check)
- target: segment:emp-changeset-size-principle
- at: 2d204811
- act: run
- line: measurement
- criterion: Does the changeset-size paragraph reproduce: slope of $\log T$ on $\log(1+L)$ 0.14–0.41 with every interval below 1; on $\log(\text{files})$ 0.29–0.89 with obsidian-linter's interval reaching 1 at the 24-hour cap; obsidian-linter medians 7.8, 26.7, 60.5, 74.8, 77 by lines bin?
- committed: after
- outcome: confirmed
- recheck: `elapsed_time.py`'s "changeset size" section on the three direct-commit histories

## C6 (check)
- target: segment:obs-software-epistemic-properties
- at: de218fb0
- act: read-check
- line: discussion
- criterion: After both H.2 commits, does any live segment, OUTLINE or toolkit document still cite $\alpha \approx 0.118$, the estimated-time fit, or an `old-*` file as a source?
- committed: after
- outcome: confirmed
- recheck: `grep -rn "0\.118\|old-tst-\|old-tf-appendix" 01-aat-core 02-tst-core 03-llm-core 04-eli-core --include=*.md`

The hits are in `02-tst-core/empirical-discontinuity/README.md` §1, which states 0.118 in order to show what it measured, plus one URL in `02-tst-core/lit-review/highest-cited-se-works.md` whose digits match the pattern.
