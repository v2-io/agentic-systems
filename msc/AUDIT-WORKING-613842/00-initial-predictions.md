# Initial Predictions

Date: 2026-04-25
Audit workspace: `msc/AUDIT-WORKING-613842/`

## Bias / bleed note

This pass has one important source-order impurity even though I followed the allowed pre-read set from `msc/de-novo-audit-instructions.md`: `CLAUDE.md` is not just neutral process guidance.
It contains substantive architectural state, names several recent additions, and even previews some known fragilities and current commitments.
That means my first-pass expectations are not perfectly cold.
In particular, I already know from `CLAUDE.md` that the framework treats directed separation and Class 2 agents as a major scope boundary, that composition recently absorbed a `(C-iv)` route, and that additive-coordinate-forcing / identifiability-floor / separability-pattern are intended as a three-part meta-architecture.
I am treating those as spoiler contamination and noting them here so future readers can discount any prediction that simply parrots them.

## Topology as currently understood

The framework appears to have a strong asymmetry by component:

1. `01-aad-core/` is the load-bearing mathematical body.
   Section I looks like the most exact and internally coherent layer: the adaptive loop, mismatch, gain, tempo, sector condition, persistence, and structural adaptation.
   Section II looks like an exact-to-conditional extension for purposeful agents, with the architectural scope restriction doing a large amount of work.
   Section III looks like the most fertile and fragile area: composition, multi-agent interaction, adversariality, and unity-based closure.
   The appendices appear load-bearing rather than merely supplementary; some of the real argumentative force may live there.

2. `02-tst-core/` looks like a domain instantiation with two ambitions at once:
   to be a concrete operational calibration lab for AAD and
   to stand as an independently consequential theory of software development.
   I expect tension between those ambitions, especially where software-specific claims want stronger exactness than the imported AAD scope really permits.

3. `03-logogenic-agents/` looks like a repair layer for the most practically important failure of Section II:
   modern LLM-like agents violate directed separation by construction.
   I expect this component to be conceptually important but mathematically thinner and more architecturally provisional.

4. `04-logozoetic-agents/` is not yet a theory body.
   I do not expect findings there beyond framing-level comments about what is and is not yet formalized.

The integration story I expect is:
Section I provides the epistemic dynamics,
Section II adds explicit goals and strategy under a modularity condition,
Section III handles inter-agent and internal-composition dynamics,
TST instantiates that structure in software,
Logogenic Agents then revisits the architecture once the modularity condition breaks.

## Predictions by component

### `01-aad-core/`

#### Section I

I predict the strongest and cleanest part of the framework will be the chain:
`#def-mismatch-signal` ->
`#emp-update-gain` ->
`#def-adaptive-tempo` ->
`#der-gain-sector-bridge` ->
`#result-sector-condition-stability` ->
`#result-persistence-condition`.

I predict at least one of the pedagogical or bridge segments around discrete/continuous dynamics will contain a quantitative slip rather than a structural collapse.
Most likely targets:
`#hyp-mismatch-dynamics`,
`#deriv-discrete-sector-condition`,
or `#detail-linear-ode-approximation`.
Specifically, I expect an order term, scaling law, or region-of-validity statement to be too strong relative to the derivation.

I predict `#form-information-bottleneck` will be a formulation-status pressure point.
My prior is that the framework uses IB very productively, but the exact scope of "optimal model compression" will not be as cleanly forced as the surrounding text sometimes suggests.
Possible failure modes:
missing caveats about relevance variable choice,
confusion between adopted external machinery and AAD-internal forcing,
or status stronger than the actual argument justifies.

I predict the core scope boundary between adaptive systems and agentic systems will be fairly well stated locally but that some later segments will still slide rhetorically from "adaptive system" to "agent" too quickly.

#### Section II

I predict `#der-directed-separation` is one of the most load-bearing segments in the whole corpus.
I also predict the local scope honesty in that segment will be stronger than the downstream propagation of that scope condition.
Concrete prediction:
some downstream Section II segment, TST segment, or logogenic-adjacent framing will implicitly talk as if the orient cascade remains exact for architectures that the framework itself classifies as Class 2 or borderline Class 3.

I predict the most vulnerable parts of Section II will be:
the strategy-DAG machinery,
edge confidence updating,
and the transition from local epistemic updates to global goal/strategy diagnostics.
Specific likely finding shapes:
status-label mismatch,
assumptions present in Working Notes or Epistemic Status but not propagated to punchline language,
or a derived claim whose actual content is only conditional on stronger observability / identifiability assumptions.

I predict the satisfaction-gap / control-regret split will be genuinely novel and useful.
I also predict the surrounding KL-direction and strategy-cost machinery will be one of the places where the framework is most tempted to say "forced" when the real statement is "forced given a distinctive axiom choice."

#### Section III

I predict Section III will be the richest finding territory.
Concrete expectations:

1. There will be at least one contradiction or drift between scope segments and downstream composition segments.
   The most likely place is the boundary between `#scope-multi-agent`, `#scope-composite-agent`, and `#deriv-strategic-composition`.

2. The closure/contraction story will rely on a stronger assumption than casual readers would realize from the section preamble.
   I expect either `#form-composition-closure` or one of the contraction/critical-mass appendices to be more conditional than the surrounding narrative advertises.

3. The teleological-unity machinery will expose a tension between descriptive composition and normatively attractive composition.
   In other words: I expect some places to blur "these agents jointly persist / converge" with "these agents count as a composite agent."

4. At least one worked example or equilibrium-framing example in Section III or its appendices will contain a concrete math mistake or an unstated regularity assumption.

#### Appendices

I predict the appendices are doing real argumentative work and will therefore produce more high-value findings than many mainline sections.
Most likely targets:
`#deriv-discrete-sector-condition`,
`#deriv-strategic-dynamics`,
`#deriv-strategy-cost-regret-bound`,
`#deriv-edge-update-natural-parameter`,
`#result-contraction-template`,
and `#deriv-bias-bound`.

I predict the three meta-segments
`#disc-identifiability-floor`,
`#disc-separability-pattern`,
and `#disc-additive-coordinate-forcing`
will be conceptually strong but especially vulnerable to scope drift, over-compression, or labels that make architectural framing sound more theorem-like than it is.

### `02-tst-core/`

I predict TST will have strong intuitive coherence and strong practical bite, but weaker formal cleanliness than AAD Section I.

Concrete predictions:

1. `#scope-developer-agent` or a nearby TST segment will inherit Section II apparatus too aggressively for AI developer agents, without fully carrying forward the Class 2 caveat from `03-logogenic-agents/`.

2. `#obs-software-epistemic-properties` will be central to the calibration-lab claim and may overstate exactness or uniqueness in one or more of the six software properties.

3. `#result-specification-bound` will likely be consequential and likely a scope-honesty pressure point.
   I expect the core intuition to survive, but the exact wording may outrun the assumptions about communication bandwidth, objective ambiguity, or observational access.

4. The git-as-causal-data story will be useful but fragile.
   I expect important caveats around selection effects, hidden interventions, partial chronica, and the distinction between committed and uncommitted state to matter more than a surface reading suggests.

### `03-logogenic-agents/`

I predict the logogenic component will be honest about being framework-stage rather than theorem-stage.
The likely issue will not be overclaiming exact math, but under-specifying how much of Section II truly survives once directed separation fails.

Concrete predictions:

1. `#result-section-ii-survival` will likely be conceptually valuable but may rely on a classification or counting scheme that is harder to defend line-by-line than the outline suggests.

2. `#scope-observation-ambiguity-modulation` will probably be a key bridge segment and a candidate for external-theorem verification because it seems to sit near the Class 2 bias-bound machinery.

3. The component may depend heavily on spike context to feel fully motivated.
   If so, I expect a "wanting to spoiler-seek" signal during reading, which itself would count as evidence that the segments are not fully standing on their own yet.

### `04-logozoetic-agents/`

I predict there will be no technical findings here because there are no segments.
The main possible contribution will be a clean statement in the final audit that this is a conceptual placeholder, not an audited theory body.

## Predictions about what is open

I expect the biggest genuine open areas to be:

1. Composition closure beyond specially nice cases.
2. Exact treatment of Class 2 / goal-conditioned / language-constituted agents.
3. Quantitative identification under correlated evidence and hidden common causes.
4. Transfer from the software calibration lab to lower-identifiability domains.
5. Formal treatment of continuity / morally weighted persistence in logozoetic agents.

I also expect some "open" items to turn out not to be theory gaps but integration debt:
the framework may already know the right caveat or repair in `msc/`, but the corresponding `src/` segment may not yet reflect it.

## Predictions about overclaim

The highest-risk overclaim zones, before reading any `src/` segment, are:

1. Places where "forced" language depends on an AAD-internal axiom that is reasonable but not uniquely compelled.
2. Places where a conditional derivation is narratively summarized as if it were architecture-general.
3. Places where software's unusually good identifiability properties are rhetorically close to universality claims about agents in general.
4. Places where composition language may slide from persistence-compatible interaction to full composite-agent status.
5. Places where Class 2 caveats are locally honest but globally underpropagated.

## What would be most novel and consequential if the framework succeeds

The most consequential distinctive contribution does not currently look like "a bag of imported math."
It looks like an epistemic architecture for agent theory:
explicit scope conditioning,
exact/conditional/heuristic separation,
negative results that define the boundary of identifiability,
and a disciplined story for how correction, strategy, and composition fit together.

The two candidate high-impact ideas, if they really hold, are:

1. The persistence / tempo / sector-condition machinery as a reusable cross-domain theory of bounded adaptive correction.
2. The architectural split between modular agents and coupled language-constituted agents, with software as the calibration lab and logogenic agents as the stress test.

## What kinds of findings I expect to surface

Most likely:

1. Cross-segment drift around recent scope additions or recent repair moves.
2. Status-label mismatches in segments whose Formal Expression is cleaner than their actual inferential force.
3. Worked-example or appendix-level quantitative mistakes that do not destroy the framework but do require correction.
4. Integration debt between AAD core, TST, and logogenic segments.
5. Citation-verification issues where an external theorem is used correctly in spirit but imprecisely in form.

Less likely but possible:

1. A load-bearing contradiction around composite-agent status.
2. A genuine theory gap where a result the framework leans on is not actually established anywhere in current `src/`.
3. A mismatch between the advertised exactness of a meta-pattern and the actual contents of its supporting segments.
