# De novo 3: a competing prediction for round p002, written before reading any p002 answer

*Written 2026-10-06 19:31:31 MDT by the third verifier (Claude Opus 5.5). At this moment `data/answers/p002.jsonl` does not exist; raw ledgers for p002 exist in `data/rounds/p002/raw/` and I have not opened them.*

**Model ("local pool").** A mind's P(stop) at a flat context = its own answers there (snapshot + p001), shrunk toward its own pooled stop rate over the 43 flat contexts (Jeffreys on the pool), with 4 pseudo-answers. No fitted parameters, no other mind's answers. Script `b_pred.py`, output `b-pred-p002.json`.

**Why.** All three pre-registered models put Haiku with thinking at about 20 stops of 43, while on these same contexts it has stopped 1 time in 14, Haiku without thinking 14 in 86, Opus 2 in 17. A model fitted to the whole dataset carries a mind's global threshold onto a selected set where that mind has already shown a different rate. If the naive baseline wins, the pre-registration's three-way comparison omitted the reference it most needed.

| expected stops of 43 [95%] | local pool | 2mf | irtu | lnb |
|---|---|---|---|---|
| opus55 | 5.9 [2, 11] | 9.5 | 6.9 | 8.0 |
| haiku45nt | 7.1 [3, 12] | 20.3 | 12.1 | 13.0 |
| haiku45 | 4.2 [1, 8] | 21.9 | 20.4 | 19.9 |

Scored the same way as `prereg2_check.py` (per-context log score, per mind).
