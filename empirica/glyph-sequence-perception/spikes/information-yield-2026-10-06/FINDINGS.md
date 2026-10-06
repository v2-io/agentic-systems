# Realized information per question: a first measurement

*2026-10-06, the coordinating session (Claude Opus 5.5), asked by Joseph: "what is defensible under the expected information gain criteria? And for that, I would assume we'd need some idea of which questions have been tending toward more information gain / uncertainty loss recently". Script `yield.py`; output `yield-c096-c105.txt` (also `-c096-c101` and `-c102-c105`, run separately). Not independently verified.*

## What was measured

For every quantity a question measures (a continue context's next glyph, an inhibit or cohere verdict, a `choose` preference, a triad's middle, an order set's line, a pick context's pick) and every family, answers are taken in round order. Each round's answers update a Dirichlet over the outcomes seen at that quantity, with prior 1/2 on each, plus one for an unseen outcome. Two numbers per answer:
- **realized information:** the KL divergence of the after-posterior from the before-posterior (Bayesian surprise), whose expectation is exactly the expected information gain;
- **uncertainty loss:** the fall in the posterior predictive entropy.

Both are credited to the question's kind and source, per answer. The planner's own expected information for the same answer is set beside them. Sealed `choose` and `names` answers are dropped first.

## What it shows, rounds c096–c105 [measured]

- **The planner's expected information is roughly calibrated.** Per answer it expects about 0.30 nats on nearly everything; realized ranges 0.24–0.35 by kind. Re-asked contexts realize the least (replicate 0.07, join-replicate 0.14), close to what was expected for them (0.11).
- **Almost every question asked is a first ask, and first asks yield about the same.** Continue questions of every source realize 0.24–0.26 nats per answer: ends, exploration, k\*, lengthening and inside contexts alike (cycle probes 0.28, from 5 answers). Whole-run, `choose`, order and name-only questions realize 0.31–0.35. So expected information about each question's own quantity barely separates the candidates the planner chooses among. What separates them now is relevance, which is a judgment, not information.
- **Surprise is not the same as usefulness.** Pick nulls (random contexts) realize 0.30–0.34 nats per answer, more than real picks (0.23–0.27), because their answers scatter. They reduce predictive uncertainty by almost nothing (0.02, against 0.04 for real picks and about 0.10 for most kinds). Information about a quantity nobody needs counts the same as information about one that matters.

## What follows [inference]

The defensible criterion isn't information about each question's own quantity. It is information about what the catalog reads: whether a run is recognised as a sequence, in what order, and how model-sensitive it is. A question's worth is then how much its answer is expected to move those readings. That puts relevance on the same footing as information, instead of beside it as a judgment.

It also connects to the family-disagreement spike (`spikes/family-disagreement-2026-10-06/`; its verification found the threshold model not yet calibrated, so this connection waits on the strengthening attempt). If its threshold model holds (one threshold per mind and question kind, one shared strength per item), the quantity a record's reading rests on is that shared strength. The information an answer from a given mind carries about it is largest where that mind's predicted chance of committing is near one half. That is the spike's $p(1-p)$, and it would replace both the current information term and much of relevance.

## Limits

- The Dirichlet's categories are the outcomes ever seen at a quantity, so a quantity with many outcomes and one with two are measured on different scales; comparisons across kinds are rough.
- Answers are grouped by round; the drains add answers to old rounds later, and they are credited to the round asked, not the time answered.
- One window of ten rounds, under two planners.
