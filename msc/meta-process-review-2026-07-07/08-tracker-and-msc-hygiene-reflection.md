# 08 — tracker-and-msc-hygiene — reflection

*Written 2026-07-07 by a Claude instance (Opus 4.8, 1M) working the tracker/msc-hygiene slice of the meta-process review. Short, honest, not performative.*

## Before

My cold prior on "tracker and working-artifact hygiene" was that it would be janitorial — find some stale files, recommend moving them to an archive dir, done. The kind of slice you do carefully but that doesn't teach you anything about the whole.

## After

Two things changed my read.

First, the tracker ecology is not messy — it is *deliberate and mostly well-composed*, and the mess is concentrated in one specific, diagnostic place: the transient handoff layer. The PRACTICA → TODO → PROPOSALS → CHANGELOG/LOG spine is real, is enforced by convention, and by and large the trackers do compose the way the docs say they do. The layered model is not aspirational fiction. That surprised me. Most large solo projects have tracking systems that are lies; this one's core is honest.

Second — and this is the thing that connects my janitorial slice to the review's actual purpose — the *one* place the hygiene has broken is exactly the place the whole review is about. `NEXT-UP.md` is the "what is hot / who decides what" handoff file, the single artifact designed to let a fresh session resume momentum without reconstructing from scrollback. It is stale by the entire most-recent work arc (the 07-03/07-04 θ-vs-Ω / era-artifact / convergence-routing session that the orientation letter calls "the freshest ground"). So the file whose entire job is to loosen the decision-routing bottleneck is itself a casualty of the bottleneck. The drain discipline it prescribes for itself is not followed — even though the project has a *working precedent* for exactly that discipline (the earlier `spikes/NEXT-UP.md` was retired cleanly in 2026-05-25 with a manifest and a CHANGELOG narrative). The capability exists and was demonstrated; it just isn't being run on the current instance.

That is the shape I did not expect: the hygiene failure is not sloppiness, it is *the bandwidth bottleneck leaving fingerprints on the one file that was supposed to route around it.* The transient-handoff layer decays precisely because updating it is unrewarded relative to doing the next piece of real work — and Joseph is the only one with the standing to say "this handoff is now stale, drain it." Which is the review's thesis in miniature.

The msc/ census confirmed the same asymmetry: the *live* working docs (era-artifact, the June cycle plans, the sovereignty carve) are well-kept; the decay is old completed-cycle residue that nobody has a trigger to sweep, plus one genuinely stray build-cruft dir. Nothing is on fire. But roughly two-thirds of msc/ top-level is May archaeology with no "done, archive me" event ever fired, because firing it is unrewarded and slightly risky, and there is no owner but Joseph.

I came in expecting to file some old papers. I came out thinking the tracker layer is a small, clean instance of the whole project's actual disease, and therefore a good place to prototype the cure.
