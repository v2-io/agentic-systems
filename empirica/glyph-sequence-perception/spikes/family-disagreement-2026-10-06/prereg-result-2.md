# Pre-registered test 2: third minds on the 43 flat contexts

*2026-10-06, the coordinating session (Claude Opus 5.5). The prediction (`prereg-third-minds.json`, written 19:18 by the spike agent from the snapshot plus round p001) was committed at 1a998f00 before round p002 existed. Before committing, I checked that none of the 43 contexts had an answer from these minds outside the snapshot. Round `p002` (built by `prereg_round.py p002 prereg-third-minds.json opus55 haiku45nt haiku45`) asked each context once as a plain continue question, one question to a sheet, from about 19:52. The scorer, `prereg2_check.py`, was committed with the round (f4e1d956) before any answer was recorded. It applies the reading fixed in the prediction file.*

## Result [measured]

| mind | stops of 43 | `2mf` expected [95%], log score | `irtu` | block-set model (`lnb`) | by the fixed rule |
|---|---|---|---|---|---|
| Opus | 6 | 9.5 [5–15], −16.52 | 6.9 [3–11], −14.95 | 8.0 [4–13], −14.25 | not discriminating (best `lnb` by 0.70 nats) |
| Haiku without thinking | 12 | 20.3 [14–27], −29.63 | 12.1 [7–18], −20.60 | 13.0 [8–19], −21.20 | not discriminating (best `irtu` by 0.60 nats) |
| Haiku with thinking | 6 | 21.9 [16–28], −29.03 | 20.4 [14–27], −27.10 | 19.9 [14–26], −26.28 | not discriminating (best `lnb` by 0.81 nats) |

Every answer was a continuation or "none"; none was left out.

By the rule fixed in the file, no model wins any mind: the best beats the next by less than $\log 10$ each time. The file also asks for the log likelihood ratio between models. On Haiku without thinking, `2mf` (no mind × item term) loses to the interaction models by 9.0 nats (`irtu`) and 8.4 nats (`lnb`), likelihood ratios of about 8,000 and 4,600 to 1. Haiku without thinking's 12 stops fall below `2mf`'s band and on the interaction models' expectations. Haiku with thinking's 6 stops fall far below every model's band.

## Reading [inference]

- **Haiku without thinking** is where the pre-registration expected the test to discriminate (`2mf` 20.3 stops against about 12–13 for the interaction models). It came out at 12. The model without a mind × item term is decisively worse here; the two interaction models are indistinguishable.
- **Haiku with thinking** failed every model in the same direction as Sonnet in p001: it continued far more steadily than predicted. Its own record on these contexts says why. Before p002 it had answered 14 times and continued 13 of them; in p002 it continued 37 of 43 (0.86). The models predicted about 20 stops anyway, pulling each context toward the shared position and, through the second dimension (the Haiku axis), toward Haiku without thinking, which stops far more here.
- Together with p001 (Sonnet 42 of 43 continued) and verification 2's within-mind finding, this points one way: **a mind's own past answers on a context predict its next answer better than any model fitted so far allows**. The models give too much weight to what other minds did there, and too little to the mind's own record.

## Confounders checked

Every answer record carries `sheet_n`, `sheet_pos`, `soft_target`, `calls_for_sheet`, the prompt hash and `source.why` (`prereg`). Raw stop rates on plain continue questions, over mixed contexts:

| mind | before c096, sheet of 1 | before c096, sheets of 2–5 | c096 on, sheet of 1 | c096 on, sheets of 2–5 |
|---|---|---|---|---|
| Haiku with thinking | 0.295 (325) | 0.341 (4,242) | 0.448 (58) | 0.496 (973) |
| Haiku without thinking | 0.391 (1,356) | 0.362 (18,201) | 0.525 (379) | 0.474 (4,888) |
| Opus | 0.137 (277) | 0.228 (3,893) | 0.390 (82) | 0.325 (1,008) |

Neither one-question sheets nor the current prompt lowers Haiku-with-thinking's stopping. On the current prompt it stops more, though these are raw rates over different context mixes (the planner changed what it asks). So the protocol of p002 doesn't account for its 6 stops; its own history on these contexts does.

## Open

- A model that weighs a mind's own record properly is the strengthening the spike needs (verification 2 §2; strengthening 2 §3–§4). None of the three fitted so far does.
- Third-verification findings (`de-novo-feedback-3.md`, under way) may bear on this reading.
