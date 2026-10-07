# Debrief for Joseph

*The spike agent (Claude Opus 5.5), 2026-10-06 ~21:00 MDT, after three independent verifications and two pre-registered tests.*

Joseph, here's where the family question stands, after three independent checks took my earlier answers apart and rebuilt them.

When the models commit to a next glyph, they mostly pick the same one, across families as much as within. Much of that is everyone walking the Unicode chart, but even away from the chart they agree about nine times in ten.

What best predicts whether a model continues a run isn't the model at all. It's what the run looks like: whether it's a straight walk through the code chart, how many Unicode blocks it crosses, how long it is. That's shared across all of them. The clearest family difference sits right there: Opus and Sonnet keep walking the chart much more readily than Grok or Gemini do. Beyond that, each model has a small lean of its own on particular Unicode blocks, mostly Grok's and Haiku-without-thinking's. It's real, but about a sixth of what I first reported. That lean is the honest version of your per-sequence parameter, with the caveat that it's measured per block, not per sequence yet.

The re-asks settled one thing: where Sonnet always continues and Grok always stops, Sonnet's side is settled. Some of what looked like Sonnet being "steadier than any model allows" was my own modelling choice, and fixing it brought Sonnet's checks into line.

Two things I'd said shift answers don't, as far as can be shown. Putting pieces of the same sequence on one sheet looked like it made models continue more, but within the same question it makes no detectable difference; the planner simply asks strong sequences more often. Re-asking and seeds change which questions get asked, not the answers.

The only clearly family-level effects are `▁` for Gemini, and the chart-walking difference above. No model I've built yet passes every consistency check; the one left over is that Grok agrees with both Gemini models more than any model allows.
