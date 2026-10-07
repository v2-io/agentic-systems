# Pre-registered test 1: the flat Sonnet-continues / Grok-stops contexts, asked again

*2026-10-06, the coordinating session (Claude Opus 5.5). The prediction (`prereg-flat-splits.json`, written 17:28 by the spike agent from the 16:36 snapshot) was committed at dc42b1cb before the test round existed. Before committing, I checked that none of the 43 contexts had a real answer outside the snapshot: 183 post-snapshot records, all failed calls. Round `p001` (built by `prereg_round.py`) asked each context once more as a plain continue question, one question to a sheet, to `sonnet55` and `grok46`. It was built at 17:34:58 and its first answer came at 17:35:04 (file and ledger times; an earlier version of this file said "about 17:40", an estimate). Scored by `prereg_check.py`.*

## Result [measured]

| mind | pre-registered quantity | observed | predicted median [95%] | |
|---|---|---|---|---|
| grok46 | share stopping again | 29/42 = 0.690 | 0.581 [0.442–0.721] | inside, in the upper part (one-sided $P \approx 0.09$) |
| sonnet55 | share continuing again | 42/43 = 0.977 | 0.814 [0.698–0.907] | **above** |

One Grok answer was "other", and it's left out of the share as the check specifies: `TB` after `㎅㎆㎇` (KB MB GB), the next unit written in letters because the square block has none. That is a commitment and a content split, which the stop/continue coding drops; counted as a commitment, Grok's stop share is 29/43 = 0.674.

**Secondary** (not pre-registered as a test). Each answer scored against its own context's predicted probability:
- Grok's expected count is 24.4 [18–30] against 29 observed. The model's log score is −26.3 nats; a "settled" model, which predicts each mind repeats its earlier answers with probability 0.95 (a value chosen without evidence), scores −40.4.
- Sonnet's expected count is 34.8 [30–39] against 42 observed. The model scores −10.8 and "settled" −5.2.

## Reading [inference; corrected after `de-novo-feedback-2.md`]

Both shares came in high. Grok's 0.69 is inside its band but in its upper part (one-sided $P \approx 0.09$ under the model's per-context probabilities); Sonnet's 0.977 is far above its band ($P \approx 0.0009$). Both point the same way: at these contexts each mind repeats its flat-split answer more often than the calibrated model allows. The pre-registration named a reading only for Grok's share, but both shares were predictions of one model, and its failure on Sonnet is not offset by Grok's landing in band.

The cause shows in the snapshot without p001 (`de-novo-feedback-2.md` §2): the model has no mind × item term, so each mind's stable leaning on an item is counted as noise. Given the other minds' answers, it over-predicts how often a mind disagrees with its own earlier answer, for every mind checked (Sonnet 40 observed against 71 predicted, Grok 163 against 217, Haiku without thinking 222 against 309). Matching cross-mind disagreement with no such term makes each mind noisier than it is. So "flat splits are borderline contexts, partly chance" is not supported for either side. What p001 shows on these 43 contexts is that Sonnet's continuing is settled and Grok's stopping is stable on most of them. A competing model with a per-(item, mind) term (the verifier's `de-novo-2/irtu.py`) fits better held out and scores better on p001, and it is still miscalibrated on within-mind repeats and on some flat-split counts.

## Confounder checked: sheet size

`p001`'s sheets held one question each; ordinary sheets hold 1–5. Every answer record carries `sheet_n`, `sheet_pos`, `soft_target`, `calls_for_sheet`, the prompt's hash and `source.why` (`prereg`), so this can be checked. Raw stop rates on plain continue questions, over mixed contexts:

| mind | sheet of 1 | sheets of 2–5 |
|---|---|---|
| sonnet55 (c096 on) | 73/254 = 0.287 | 0.317–0.331 |
| grok46 (all rounds) | 444/1422 = 0.312 | 0.325–0.350 |

Both minds stop a few points less on one-question sheets, in the direction of Sonnet's excess. The effect is a few points, while Sonnet's departure from the model is about 16 (0.98 against 0.81). Sheet size doesn't account for it, but it is a measurable covariate, and the threshold model doesn't yet include it.

**The prompt changed too, which I missed** (`de-novo-feedback-2.md` §4). Every Grok continue answer the model was fitted on was given under the pre-c096 prompt ("up to 24", the continue option first). p001 used the current one (a soft target of 3–24, option order fated: "none" first on 19 of 43 sheets). Measured within items, the changes are small: Sonnet's prompt change moved nothing on the same items ($+0.000 \pm 0.017$, 86 items), and one-question sheets moved Grok by $-0.005 \pm 0.020$ (220 items). For Grok, the prompt change itself is unmeasured: it needs Grok's answers under both prompts on the same items.

## Open

- Whether Sonnet's steadiness is particular to these 43 contexts (selected because Sonnet continued twice) or general. Selection on two continues already enters the model's posterior, so it isn't a regression-to-the-mean artifact by construction. But it is exactly where a too-noisy model shows up.
- Asking the same contexts of Haiku without thinking, whose flat splits against Grok also exceeded the model (strengthening-1 §1), was not pre-registered and wasn't done.
