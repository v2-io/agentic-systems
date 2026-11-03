**KR I.3 / I.4.** Part of `README.md`'s set.

# The reinforcement loop, measured

Joseph's conjecture: a wrong integrator after a verification pass with a new mind, repeated, made "almost half of our 'fixed' claims claims that were only generated in that same sprint." Reflection 31 traced ten corrected sites against the tag and found about half were same-day sentences. The trail lets the loop be measured four ways rather than sampled.

## The loop

check (new mind) → findings → integrator revises → the revise lapses the check and every check downstream → next round checks the revised text → findings → …

Its gain is above one when a round adds more text than the next round's checks can clear. Four readings of the trail:

**1. Where the findings landed.** Of 313 findings, 269 were placed on a version of the segment written during the sprint, 44 on segments never revised. That is a floor of 86%, with the caveats in `02-measures.md` §12: version-level, and the earliest versions vsect saw were themselves often post-tag. Of 488 checks, at least 328 (67%) were on sprint-written versions.

**2. Yield per round did not fall.** Broken-or-narrowed outcomes over checks, by review, in round order:

| Lane | Rounds (found / checks) |
|---|---|
| `scope-adaptive-system` | reread 2/5 · check-4 2/7 · check-5 2/12 · check-6 2/9 · check-7 2/10 · check-8 3/11 |
| Volume 4 | check-1 9/11 · check-2 9/11 · check-3 10/15 |
| TST | check-1 8/13 · check-2 7/18 · check-3 5/12 · check-4 4/9 |
| Part I | round-2 2/17 · round-3 0/16 · round-4 0/8 (findings 18, 5, 8) |

Three of four lanes found something at a flat rate through every round. Part I's checks went to zero by round 3 while its findings continued: those were restatements elsewhere (Briefs, OUTLINE cells, neighbours), which is reflection 31's first correction (bind restatements to their source). So Part I converged on the mathematics and not on the surfaces; the other three lanes did not converge on either within the day.

**3. Edit mass per round grew.** Words in the hashed text, from `vsect read --at` on each revise pair:

| Segment | Versions | Words, first → last | Added / removed per revise |
|---|---|---|---|
| `scope-adaptive-system` | 8 | 3,177 → 6,878 | +1382, +46, +1252, +48, +339, +455, +887, +25 |
| `deriv-sector-condition` | 5 | 5,757 → 14,477 | +397, +5651, +1495, +529, +1712 (the last a Claim Record) |
| `def-value-object` | 5 | 3,445 → 6,250 | +379, +1934, +59, +1499, +67 |
| `hyp-exponential-cognitive-load` | 5 | 1,506 → 2,243 | +76, +431, +342, +7, +175 |

No round removed more than it added. Each revise lapsed between 5 and 17 checks on the old text. The retrospective's convergence condition ("each round shrinks the set of places a claim is restated") was not met on any of the four; the segments grew 1.5x to 2.5x.

**4. Who found what.** Integrator-recorded re-derivations: 116 confirmed, 0 broken, 0 narrowed. Independent: 88 / 22 / 43. The integrator's own check after landing never found a defect in the integrator's own landing; the next mind found one 43% of the time. So the loop's information came entirely from the new mind each round, and the new mind's edits (reflection 31: strengthenings landed inside the loop, P4, the window, the third term) were themselves unchecked text for the following round.

## What this does and does not say

It does not say the checks were waste. The Fable assessment re-derived the largest changes and found them right, and checks 6 and 8 on the scope found real defects (the fresh-noise independence; the wrong-kernel counterexample). The flat yield is consistent with both "the rounds kept finding real things" and "the rounds kept making things to find"; reading 3 is what separates them, and it says the rounds were adding text faster than they were settling it.

Counterexamples to the reading that the loop is the tool's fault: the tool recorded every lapse honestly, and the 257 own-text lapses are the loop made visible. Without vsect the same rounds would have run with no record that round 5's text was unchecked. The gain above one came from the process (a new integrator each round, strengthenings landed in-loop, no edit-mass budget), and the tool's contribution is that this can now be measured at all.

What would make the reading wrong: if the flat yield is checker diversity rather than text churn (each round was a differently-framed bare brief), the right test is a round in which the integrator lands only the findings and adds nothing, followed by one more check; if that check's yield is still a quarter, the text had the defects all along. That test was never run. It costs one round.

## The measure to print

Edit mass per round, per segment, beside the lapse count it caused, is the convergence signal and is one `vsect read --at` diff away. A round whose added words exceed its removed words, on a segment already checked, is the loop running; the lead should see that number before launching the next checker, not after.
