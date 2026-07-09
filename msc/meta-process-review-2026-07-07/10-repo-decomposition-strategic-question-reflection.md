# Reflection — Cluster 10, repo-decomposition strategic question

*Written 2026-07-07 by a Claude instance (Opus 4.8, 1M context) assigned the monolith-vs-multi-repo slice of the meta-process review. Orientation notes, not a claim segment. Honest before/after.*

## Before

I came in with the cluster's framing as Joseph stated it — "essentially a big monolithic repo that could easily decompose into many repos but also derives advantage from proximity and pull toward cohesion" — and a cold prior that this would be a straightforward layered-DAG story: one mathematical core (`01-aat-core`), three volumes hanging off it, obvious clean cut lines. My expectation was that the interesting question would be *governance* (independent release cadence, who-owns-what) rather than *feasibility*, because I assumed the dependency structure was a tidy tree.

## After

Two things overturned the cold prior, both from measuring rather than assuming.

First, **the dependency is not a clean DAG.** The core (`01-aat-core`) reaches *down* into the derived volumes — 42 references into `03-llm-core`, 18 into `04-eli-core`, 13 into `02-tst-core` — and at least one of those is load-bearing, not a "see also": the quantitative apparatus behind a Volume-3 result physically lives in a Volume-1 appendix (`deriv-observation-ambiguity-bias-bound.md`, with the Volume-3 segments explicitly holding "client status"). So the four volumes are not stacked; they interpenetrate. That single fact reframes the whole question from "where do we cut" to "is there a cut at all that doesn't sever load-bearing tissue."

Second, and this is the correction I most want to hand forward: **the "big monolithic repo" intuition is largely a size illusion.** The repo is 836M on disk and 225M git-tracked — but the actual theory content (all four volumes' `src/`) is 8.6M, under 4% of the tracked weight. The bulk is `ref/` (135M of external prior-art PDFs), `_obs/` (162M of obsolete archive), and `mono/` (116M of build artifacts, mostly *not* gitignored). So "the repo feels monolithic and heavy" and "the theory is a monolith that should decompose" are two different claims, and the evidence only supports the first as a *packaging* problem, not the second as a *theory-structure* problem. The cheap intervention (move `ref/` and `_obs/` out, gitignore `mono/`) is not the decomposition question at all — but it is almost certainly what a fresh observer is *reacting to* when the repo feels like it wants to split.

The thing I'd flag for the synthesis agent: the honest brief has to keep those two questions apart, or Joseph will be handed a heavyweight architectural decision (rewire ~470 cross-volume references, split the terminology system, lose atomic refactor) as the answer to what may actually be a lightweight packaging annoyance. My job was to frame, not decide, and the most useful framing move I found was disaggregating "monolith" into its packaging half and its coupling half.

I did not verify the internal mathematics; my coupling counts are from grep over slugs and cross-volume markdown links, cross-checked against a slug-to-volume index I built, and I hold them as measured-mechanically, not audited-for-meaning. Where a count is load-bearing to an option's cost I say so and point at the file.
