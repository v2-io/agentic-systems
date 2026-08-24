# Lit scan for ε-lumpability spike (2026-08-24)

Web scan done via WebSearch/WebFetch, not a database/API search — treat as a first pass, not exhaustive. Marked **[verified]** where I actually pulled abstract/author info from a source; **[training, unverified]** where it's your own prior knowledge or my own recall, not checked here.

## (1) Quantitative "one-step lumping defect δ ⇒ time-t error ≤ f(t,δ)" results

**[verified] Michel & Siegle, "Formal Error Bounds for the State Space Reduction of Markov Chains," arXiv:2403.07618 (Mar 2024, revised Aug 2024), published in *Performance Evaluation* (2024), DOI 10.1016/j.peva.2024.102464.** This looks like close to exactly the result you're asking about and is recent enough that it may not be in training data cleanly. Abstract-level claim: they bound the *stepwise increment* of the error in discrete time and the *rate of growth* of the error in continuous time, for approximating a Markov chain by a reduced/aggregated one, and compare against exact lumpability/aggregatability as the zero-error limit. I was not able to get the PDF's actual math (WebFetch returned raw PDF stream objects, not text — I did not verify the literal bound formula, only the abstract via the arXiv abstract page). **This is the one to pull the actual paper for before citing a specific inequality** — I can't confirm whether it's the min(tδ, δ/(1−contraction)) shape you're expecting or something else (e.g. an L1/TV bound via second-largest singular value, which showed up in a different search hit, unattributed).

Other hits, not run down:
- A ResearchGate/ScienceDirect item "Bounding the lumping error in Markov chain dynamics" — pre-2020, unclear author/year from search snippet; sounds like it could be the Deng/Simon-type result you were recalling, but I did not confirm authorship. **[unverified — worth checking, possibly this is your "Deng, Simon?" memory]**
- "Bounding the coarse graining error in hidden Markov dynamics" arXiv:1104.1025 — older (2011), HMM coarse-graining framing rather than lumpability per se.
- A search-summary line (not a specific paper I opened) mentioned bounds "expressed in terms of the second-largest singular values of the transition probability matrices" — this smells like a real technique (spectral gap → mixing-time-style bound) but I could not attribute it to a specific citation from the search snippet alone. **[unverified attribution]**

Net: I did not find a single canonical "the" theorem of your exact form cited by name the way Kemeny–Snell is; Michel & Siegle 2024 is the strongest, most recent candidate and is worth reading directly rather than trusting my summary.

## (2) Non-uniqueness / multiplicity of minimal lumpable partitions, symmetry actions

**[training/weakly verified]** Confirmed only at the level of "this is a known, named phenomenon" — search summaries state plainly that a chain can have several lumpable partitions, and that symmetry-group actions (wreath products of symmetric groups acting on poset block structures) generate families of lumpings. Specific paper: **Bailey & someone (?), "The lumpability property for a family of Markov chains on poset block structures," ScienceDirect** — ties lumpings to subgroups of generalized wreath products; I did not open this to confirm authorship or check whether it addresses *minimality* or a genuine lattice-failure result. Also surfaced but not opened: "Lumpings of Algebraic Markov Chains Arise from Subquotients," *Journal of Theoretical Probability* (Best/Brightwell? — author not confirmed), which sounds like the right kind of algebraic framing (lumpings as a Galois-type correspondence with subquotients) but I have not verified it addresses multiplicity/lattice-failure explicitly, only that it's algebraic and general.

I did **not** find anything that reads like an explicit "the set of lumpable partitions does not form a lattice" no-go statement, nor anything using that phrase. This may be a genuine gap, or may just be a gap in what surfaces from a shallow web search — I'd treat "nothing found stating a lattice-failure result by name" as the honest result here, not as proof of absence.

## (3) 2024–2026 approximate MDP/agent abstraction tied to mutual-information-style coupling

**[verified, partial]** Delimpaltadakis & Gleizer, arXiv:2512.03977, "An Information Theory of Finite Abstractions and their Fundamental Scalability Limits" — real, recent (posted ~Dec 2025 given the arXiv id), and does exactly the "quantitative accuracy-vs-size tradeoff via rate-distortion theory" move that's adjacent to what you asked, with a fundamental lower bound on abstraction distortion given system dynamics and abstraction size, and distortion tied to trajectory entropy. But per the fetch, this is about **deterministic dynamical systems**, not MDPs/stochastic agents, and does **not** appear (from the abstract) to use a mutual-information coupling measure specifically or address agency/decision-making — so it's adjacent, not a hit on your exact ask.

Other 2024–2025 items surfaced by search but not opened/verified: "Causal Information Prioritization" (ICLR 2025), "Causal Information Bottleneck and Optimal Causal Variable Abstractions" (Simoes et al., 2025), "Causal Abstraction Inference under Lossy Representations" (Xia et al., 2025), "Aligning Graphical and Functional Causal Abstractions" (arXiv:2412.17080). These look like the right neighborhood (causal-information-bottleneck-style abstraction error) but I have not read any of them — **[unverified, names/years only, from search snippets]**.

I did not find anything that explicitly frames MDP-abstraction error as a mutual-information/coupling quantity between full and abstracted agent state in the way you described — closest is the causal-information-bottleneck line, unread.

## (4) "Belief-state factorization uniqueness under interventions" as causal-abstraction-meets-lumpability

**[unverified, names/years only]** Nothing found that directly matches this framing. Adjacent 2024–2025 work surfaced: Geiger et al. (2024/2025) and Sutter et al. (2025) on "abstraction-under-translation"; Garrabrant et al. (2024) "Factored Space Models: Towards Causality Between Levels of Abstraction" (this one sounds like it could be close — factored/level-of-abstraction causal structure — but not opened); Li, Kaba, Ravanbakhsh (2025) on identifiability of causal abstractions (identifiability is adjacent to your uniqueness question). None of these were read past a search snippet, so treat all of §4 as "leads to chase," not results.

## What I did NOT check

- Did not verify any of your training list (Kemeny–Snell, Dynkin, Rogers–Pitman, Desharnais et al., Abate et al., Buchholz, Cardelli/Tribastone/Tschaikowski) against a live source — no reason from this scan to think any of it is stale, but "no reason to doubt" is not the same as "checked."
- Did not get past the abstract for any paper except the two arXiv abstract pages fetched directly (2403.07618, 2512.03977). Everything else is a search-engine snippet, one layer short of even an abstract read.
- Did not check for a 2025/2026 update specifically superseding Michel & Siegle 2024, or citing papers that might state your exact target inequality more cleanly.

## Bottom line for the derivation

The strongest concrete new lead is **Michel & Siegle 2024** (arXiv:2403.07618 / Performance Evaluation) — read the actual paper (not this summary) before deriving, since it's exactly the shape of result you're after and recent enough to plausibly contain something your training doesn't. Everything else above is either "known phenomenon, no single canonical citation surfaced" (§2) or "adjacent literature exists, exact match not found" (§3, §4) — honest gaps, not confirmed absences, given the shallowness of a web-search-only pass.
