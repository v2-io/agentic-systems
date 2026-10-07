# Pre-registered test 2: third minds on the 43 flat contexts

*2026-10-06, the coordinating session (Claude Opus 5.5); reading corrected after `de-novo-feedback-3.md`. Times are from git and file timestamps. The prediction (`prereg-third-minds.json`, written 19:18 by the spike agent from the snapshot plus round p001) was committed alone at 19:28:03 (1a998f00); before committing, I checked that none of the 43 contexts had an answer from these minds outside the snapshot. Round `p002` (`prereg_round.py p002 prereg-third-minds.json opus55 haiku45nt haiku45`) was built at 19:28:15. Each context was asked once as a plain continue question, one question to a sheet; the ledgers were complete at 19:31:37, and the answers first recorded at 19:31:43. The scorer, `prereg2_check.py`, applies the reading fixed in the prediction file. It was committed with the round (f4e1d956, 19:28:46), before any answer was recorded.*

## Result [measured]

| mind | stops of 43 | `2mf` expected [95%], log score | `irtu` | block-set model (`lnb`) | by the fixed rule |
|---|---|---|---|---|---|
| Opus | 6 | 9.5 [5–15], −16.52 | 6.9 [3–11], −14.95 | 8.0 [4–13], −14.25 | not discriminating (best `lnb` by 0.70 nats) |
| Haiku without thinking | 12 | 20.3 [14–27], −29.63 | 12.1 [7–18], −20.60 | 13.0 [8–19], −21.20 | not discriminating (best `irtu` by 0.60 nats) |
| Haiku with thinking | 6 | 21.9 [16–28], −29.03 | 20.4 [14–27], −27.10 | 19.9 [14–26], −26.28 | not discriminating (best `lnb` by 0.81 nats) |

Every answer was a continuation or "none"; none was left out.

**The fixed rule couldn't report what the test found** (`de-novo-feedback-3.md` §1). A model "wins" only by beating *each* other model by $\log 10$, and `irtu` and `lnb` nearly coincide by construction, as the prediction file itself says. So the rule could only ever return "not discriminating" or a win for `2mf`. The pairwise ratios, which the file also asks for, carry the information:

- on Haiku without thinking, `2mf` (no mind × item term) loses to `irtu` by 9.0 nats and to `lnb` by 8.4, likelihood ratios of about 8,000 and 4,600 to 1;
- Haiku with thinking's 6 stops fall far below every model's band.

**A naive baseline beats all three models** (the verifier's, written at 19:31:19 before any p002 answer was recorded; file times and its word attest the order). It gives each mind its own stop rate pooled over the 43 contexts, with nothing fitted. Summed log score: baseline −56.24, `lnb` −61.73, `irtu` −62.65, `2mf` −75.18. The whole margin is Haiku with thinking (by 9.4 nats). The baseline loses Opus to `lnb` by 2.1 and Haiku without thinking to `irtu` by 2.4.

## Reading [inference]

- **The test discriminated where it was built to.** On Haiku without thinking, the model with no mind × item term is decisively worse. The two interaction models can't be told apart.
- **Haiku with thinking failed every model, and its own record on these contexts does *not* explain it.** It had earlier answers on only 13 of the 43 (13 continuations of 14). The failure sits on the other 30, where it had none: there it stopped 3 times, and the models expected about 14. What the models lack is the *kind* of context. 34 of the 43 flat contexts are contiguous chart walks, 8 monotone runs and 1 other. No model sees chart class, and Haiku with thinking stops on 0.195 of contiguous contexts in the snapshot against 0.34 overall. At a flat context the models put the item's shared position where Grok's stops (2 or 3 of 3 at every context) pull it, then apply Haiku's global threshold. Its stop rates by chart class bring the expectation from about 20 to about 12. The other half of the miss (12 against 6) is unexplained (verifier 3 §1; a reading, not a fitted test).
- An earlier version of this file said the models pulled Haiku with thinking "through the second dimension (the Haiku axis)". None of the three models has a second dimension, so that mechanism was not available to them. The spike's two-factor model, run afterwards by the verifier, still expects 18.1 stops.
- So the better-supported statement for p002 is narrower than "a mind's own record predicts its next answer". A mind's behaviour on a *kind of context* (here, chart walks) isn't carried by a one-dimensional item position. Sonnet's steadiness in p001 is the case where the mind's own record on the same contexts was the evidence.

## Confounders checked

Every answer record carries `sheet_n`, `sheet_pos`, `soft_target`, `calls_for_sheet`, the prompt hash and `source.why` (`prereg`). Raw stop rates on plain continue questions, over mixed contexts:

| mind | before c096, sheet of 1 | before c096, sheets of 2–5 | c096 on, sheet of 1 | c096 on, sheets of 2–5 |
|---|---|---|---|---|
| Haiku with thinking | 0.295 (325) | 0.341 (4,242) | 0.448 (58) | 0.496 (973) |
| Haiku without thinking | 0.391 (1,356) | 0.362 (18,201) | 0.525 (379) | 0.474 (4,888) |
| Opus | 0.137 (277) | 0.228 (3,893) | 0.390 (82) | 0.325 (1,008) |

Neither one-question sheets nor the current prompt lowers Haiku-with-thinking's stopping; on the current prompt it stops more. These are raw rates over different context mixes (the planner changed what it asks), so they rule out a large protocol effect, not a small one.

## For the next pre-registration (verifier 3's suggestions, which I'd adopt)

- Pairwise likelihood ratios as the verdict.
- A stated reading for every band.
- A naive reference model alongside the fitted ones, so that "every model fails" can be told apart from "no model discriminates".
