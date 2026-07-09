# Reflection — cluster 04, governing-doc / memory / SOP integrity

*Written 2026-07-07 by a Claude instance (Opus 4.8, 1M context) mapping the auto-loaded governing layer. Short orientation notes, not a claim segment; overturn freely.*

## Before

My cold prior on a "governing-doc integrity" slice was that I would find the usual entropy: a couple of stale pointers, a banner someone forgot to pull, some memory files drifting from the docs they mirror. The framing question I was handed — "SOP shift complete vs a still-live reconsideration banner: is that a contradiction?" — read like it was pointing me at one such forgotten banner.

## After

Two things reframed it for me.

First, the "contradiction" the task named is not the real one, and finding that out mattered. The banner and the "shift complete" commit are about *two different threads* that share a filename and a rough date-neighborhood — the doc/sop file-consolidation (complete) and the integration-failure recovery (genuinely open). They do not contradict each other. But right next to them sits a contradiction that *is* live and that nobody flagged: the completion plan says "WHOLE SHIFT COMPLETE" including "B3 agents.sop.md slim," while agents.sop.md line 22 still tells every agent that "slimming these into pointers is the remaining Phase B work," and the file was trimmed 20%, not the "roughly halved" the plan set as B3's target. The overclaim is in the *completeness declaration*, not the banner. This is exactly the F6 failure class — a small self-inconsistency in the maximal-blast-radius file — sitting inside the very file that warns about it. That recursion is the finding, not an ornament on it.

Second, this slice is where the whole review's thesis is most literally true. The orientation letters both land on the same claim: the bottleneck is bandwidth and decision-routing, not ideas. In my slice I found the mechanism that is *supposed* to loosen decision-routing already half-built and working — `JOSEPH-TODO.md`, a curated short-list of genuinely-Joseph calls with a real convention for what earns a place. It correctly holds exactly one live item (the bulk-64 wipe). That is the good news and it is concrete: the routing surface Joseph wants is not hypothetical, it exists, it just is not yet wired to catch everything (the deferred global-memory pass fell through it — JOSEPH-TODO says that work "lives in TODO.md," and it does not, anywhere).

What I did not expect: the healthiest layer is the project auto-memory (actively curated, MEMORY.md re-thinned Jul 4), and the *most* stale is the one furthest from the daily working tree — the memorata memory-curation workshop, frozen at exactly 2026-05-12, ~8 weeks, with ~63 planned global detail-files never authored. Staleness tracks distance-from-the-hot-path precisely. Joseph's memory of it as "got somewhere but wasn't done" is exactly right; the HANDOFF.md is an honest, complete account of a pass that stopped mid-arc and was never resumed.

The honest scope of my confidence: I verified file states, sizes, dates, and commit history firsthand. I did *not* read every one of the 97 project-memory files or every SOP body line-by-line — I sampled the load-bearing ones and traced the specific threads the task named. Where I say "de-facto healthy" about project memory, that is from freshness signals and spot-reads, not a full audit of drift between each feedback file and its SOP.
