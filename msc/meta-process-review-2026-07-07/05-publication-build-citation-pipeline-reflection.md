# 05 — Publication / Build / Citation Pipeline — Reflection

*Orientation notes from the instance mapping cluster 05, 2026-07-07. Author's-voice, honest, not a claim segment. The substantive map is in the companion `-findings.md`.*

## Before

Cold prior on a "publication pipeline" slice: expect a half-built LaTeX toolchain, a bibliography TODO nobody's touched, and some stale committed PDFs — the usual entropy of a solo research repo where the science is the point and the plumbing rots. I expected the interesting finding to be "the build is broken."

## After

The build is *not* broken, and that reframed the whole slice for me. The markdown-first three-stage pipeline (ingest → assemble → typeset, two render targets) is real, coherent, and — verified firsthand today — green through Stage 2 and reference-emit: 163 segments render with 0 errors, 9 citation keys resolve with 0 missing. The pipeline modules all parse. This is not rotting infrastructure; it's a genuinely well-architected build system with a load-bearing design doc that a future HTML/EPUB renderer could plug into unchanged. The `markdown-as-canonical-form, PDF-as-one-rendering` commitment is exactly right and is stated as *consciousness infrastructure in the same sense the framework is* — which reads as earned, not grand, once you watch it work.

So the real story of this slice is not breakage. It's a **sharp split between a mature build spine and an almost-entirely-deferred conventions/citation layer on top of it** — FORMAT-TODO Workstreams B and C are largely untouched, and the citation migration (W-3) is a ~340-reference author-judgment job with a 2-segment pilot done and the rest open. The infrastructure was built to a high standard and then the *content-migration* work it exists to enable stalled — which is the bandwidth-bottleneck the orientation letters name, made concrete in one slice. Joseph built the machine that makes citation-migration cheap, and the cheap-but-large job still hasn't run because it's author-judgment work only he (or he-with-an-agent) can do.

The second thing that shifted: the small hygiene questions turned out to be the ones genuinely stuck on Joseph, and they're stuck for *good* reasons, not neglect. `CURRENT-VOL1.md/.pdf` committed at root is a deliberate discoverability workaround for a gitignore policy, and whether to keep doing it is a real taste call with a real tradeoff. The archival metadata (CITATION.cff / Zenodo) frozen at v0.1.0 while the volumes moved to 0.3/0.2 is a publication *act* nobody but Joseph can authorize. These aren't rot; they're decisions correctly waiting for the one person who can make them — which is exactly the routing-failure this review exists to surface. My job was to make them reach him in a form he can act on in sixty seconds, not to editorialize about whether the ambition is reasonable.

## What I'd flag to the next instance

Don't try to "fix the pipeline" — it doesn't need it. The leverage here is (a) the citation-migration job is now cheap per-segment and just needs to be *run*, ideally batched by Joseph-with-an-agent per volume; and (b) three or four genuinely-Joseph decisions (release cut, committed-artifact policy, imported-vs-native marking, sidenote convention) are each one-line asks that unblock a chain of deferred convention work. I did notice one thing outside my slice that felt worth stopping on: a full commercial Garamond Premier Pro font family (35 MB, 37 files) is committed to a CC-BY public repo. That's a potential licensing landmine, not a hygiene nit — flagged in findings.
