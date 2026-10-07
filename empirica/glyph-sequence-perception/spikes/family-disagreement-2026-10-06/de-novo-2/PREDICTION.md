# A competing prediction for round p001, written before reading any p001 answer

*2026-10-06 17:46 MDT (`date`), the second de novo verifier (Claude Opus 5.5). Written before I opened `data/rounds/p001/raw/` or `data/answers/p001.jsonl`; this file is not edited after that. The full report is `../de-novo-feedback-2.md`.*

**Why a competitor.** The spike's 2PL mixture with familiarity (`irt.py`, variant `2mf`) fits cross-mind disagreement, but it under-predicts how consistent each mind is with itself: given only the other minds' answers, it predicts more disagreement between a mind's own first two answers (different rounds) than occurs, for every mind with data: Sonnet 40 observed against 71 predicted (1,255 items), Grok 163 against 217 (1,517), Haiku without thinking 222 against 309 (1,150) (`a6.py`, `a7.py`). That is the signature of a stable mind x item propensity, which the model has no term for, and it is exactly what a flat split's next answer depends on.

**The competitor** (`irtu.py`): `2mf` plus a per-(item, mind) random intercept in the graded class, $\tau_m u_{im}$ with $u_{im} \sim N(0, 1)$; $\tau = 0$ is `2mf`. Fitted on the same snapshot by EM: log-likelihood $-36{,}155.4$ against $-36{,}186.4$ for `2mf` (7 extra parameters); $\tau$: Sonnet 1.35, Grok 1.61, Haiku without thinking 2.20, others 0.8 to 1.2. Held-out comparison running at the time of writing.

**Its prediction for p001** (per-context probabilities in `tau-pred.json`; `a9.py`):

| | `2mf` (pre-registered) | `2mf` + mind x item intercept |
|---|---|---|
| Grok's answer stops again | 0.58 [0.44, 0.72] | 0.72 [0.58, 0.86] |
| Sonnet's answer continues again | 0.81 [0.70, 0.91] | 0.89 [0.79, 0.98] |

**How I will read the result** (`a10.py`): by the likelihood ratio between the two models' Poisson-binomial distributions over the count, not by the inside/outside of one band. For Grok the two are equally likely at 28 stops of 43; each stop beyond 28 multiplies the ratio by about 2 in the competitor's favour, each one below by about 2 against. For Sonnet the crossover is at 37 continues of 43. If fewer than 43 are answered, the same computation over the answered contexts.

**Caveat on both predictions** [measured, `a2.py`/`a4.py` in the scratchpad, summarised in the report]: Grok has never answered a continue question under the c096+ prompt (soft target "around N or fewer", fated option order), which p001 uses; every one of its continue answers, and so both fits, is from the earlier prompt. Sonnet's stop rate did not change across that prompt change on the same items ($+0.000 \pm 0.017$, 86 items), and single-question sheets shift Sonnet $-0.025 \pm 0.013$ and Grok $-0.005 \pm 0.020$ within items. So the confound is probably small, but for Grok it is unmeasured.
