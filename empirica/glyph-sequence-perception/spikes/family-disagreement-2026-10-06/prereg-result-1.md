# Pre-registered test 1: the flat Sonnet-continues / Grok-stops contexts, asked again

*2026-10-06, the coordinating session (Claude Opus 5.5). The prediction (`prereg-flat-splits.json`, written 17:28 by the spike agent from the 16:36 snapshot) was committed at dc42b1cb before the test round existed. Before committing, I checked that none of the 43 contexts had a real answer outside the snapshot: 183 post-snapshot records, all failed calls. Round `p001` (built by `prereg_round.py`) asked each context once more as a plain continue question, one question to a sheet, to `sonnet55` and `grok46`, from about 17:40. Scored by `prereg_check.py`.*

## Result [measured]

| mind | pre-registered quantity | observed | predicted median [95%] | |
|---|---|---|---|---|
| grok46 | share stopping again | 29/42 = 0.690 | 0.581 [0.442–0.721] | inside, near the top |
| sonnet55 | share continuing again | 42/43 = 0.977 | 0.814 [0.698–0.907] | **above** |

One Grok answer was "other" (`㎅㎆㎇`), and it's left out of the share as the check specifies.

**Secondary** (not pre-registered as a test). Each answer scored against its own context's predicted probability:
- Grok's expected count is 24.4 [18–30] against 29 observed. The model's log score is −26.3 nats; a "settled" model, which predicts each mind repeats its earlier answers with probability 0.95 (a value chosen without evidence), scores −40.4.
- Sonnet's expected count is 34.8 [30–39] against 42 observed. The model scores −10.8 and "settled" −5.2.

## Reading [inference]

The pre-registration named one failure: a Grok share near 1, meaning the split is settled and the model misses an interaction. That didn't happen. Grok's stops at these contexts are partly chance, as the model says, though its share sits near the top of the band. Sonnet's side failed in the opposite direction from Grok's: it continued at these contexts more steadily than the model allows, and a "Sonnet repeats itself" model beats the calibrated one on its answers. The pre-registration didn't say in advance what that outcome would mean. My reading: the model's within-mind noise is too large for Sonnet at these contexts, which is a mind × context departure on Sonnet's side, not Grok's. So "flat splits are ordinary borderline contexts" holds for one side of the pair. As a statement about the pair it is not supported.

## Confounder checked: sheet size

`p001`'s sheets held one question each; ordinary sheets hold 1–5. Every answer record carries `sheet_n`, `sheet_pos`, `soft_target`, `calls_for_sheet`, the prompt's hash and `source.why` (`prereg`), so this can be checked. Raw stop rates on plain continue questions, over mixed contexts:

| mind | sheet of 1 | sheets of 2–5 |
|---|---|---|
| sonnet55 (c096 on) | 73/254 = 0.287 | 0.317–0.331 |
| grok46 (all rounds) | 444/1422 = 0.312 | 0.325–0.350 |

Both minds stop a few points less on one-question sheets, in the direction of Sonnet's excess. The effect is a few points, while Sonnet's departure from the model is about 16 (0.98 against 0.81). Sheet size doesn't account for it, but it is a measurable covariate, and the threshold model doesn't yet include it.

## Open

- Whether Sonnet's steadiness is particular to these 43 contexts (selected because Sonnet continued twice) or general. Selection on two continues already enters the model's posterior, so it isn't a regression-to-the-mean artifact by construction. But it is exactly where a too-noisy model shows up.
- Asking the same contexts of Haiku without thinking, whose flat splits against Grok also exceeded the model (strengthening-1 §1), was not pre-registered and wasn't done.
