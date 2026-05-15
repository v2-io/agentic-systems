# Naming Principles

Long-lived naming principles for the Agentic Systems Framework. Vocabulary commitments, slug discipline, evaluation criteria, decision categories, naming layers. Tactical voting mechanics (round structure, vote-weight scales, deliverable formats, cold-start discipline) live separately in [`msc/naming/naming-principles-old.md`](../msc/naming/naming-principles-old.md) for as long as the naming cycle's voting apparatus is in active use; that file will be deprecated when the apparatus retires.

The principles below apply to *every* naming decision in the project — whether reached via multi-agent voting, manual curation, an audit-finding, or a single contributor's call.

## Architectural invariants — not subject to per-name decision

Some structural commitments are project-level architecture. They constrain *every* naming move; work within them rather than against them.

### Role-prefix discipline

**Every segment slug takes the form `{type-prefix}-{subject-noun}`.** The type prefix derives mechanically from the segment's `type:` frontmatter (one of FORMAT.md's vocabulary: `postulate`, `definition`, `scope`, `formulation`, `derived`, `result`, `corollary`, `hypothesis`, `normative`, `empirical`, `observation`, `discussion`, `measurement`, `proposed-schema`, `derivation`, `worked-example`, `detail`, `sketch`, `aside`). A small `TYPE_TO_PREFIX` mapping in `bin/align-slug` collapses overly-long type tokens into compact slug prefixes (currently `worked-example → example`; see `CLAUDE.md` §"Slug role-prefix mapping").

The pilot validated this discipline (commits `09ace17`, `3aa9e74`). Role-prefix addition is mechanical — `bin/align-slug --all` sweeps the repo. Naming decisions operate on subject-nouns; prefixes are the script's job.

### Subject-noun-first slug naming

**Slugs name the *thing* the segment defines, not the *role* the segment plays in the argument.** "Condition", "pattern", "framework", "approach" as subject-nouns are placeholders that fail this principle. The subject-noun should be a memorable noun that survives the communal-imagination test (below). Canonical illustration from the pilot: `#scope-condition` named the segment's role (it stated *some condition*); the split into `#scope-adaptive-system` + `#scope-agency` named what each scope actually delimits — adaptive systems and agency, respectively.

### Greek / etymological vocabulary commitment

The framework deliberately uses a coherent Greek-rooted vocabulary for its core nouns: *chronica*, *prolepsis*, *aisthesis*, *aporia*, *epistrophe*, *praxis*, *logogenic*, *logozoetic*. New naming proposals should sit comfortably within this aesthetic register rather than introducing competing registers (clinical-bureaucratic, marketing-feature, mathematical-acronym, etc.). This isn't an absolute prohibition — `directed separation`, `satisfaction gap`, and `control regret` are excellent non-Greek names — but it is a strong preference principle.

### Methodology — separate passes for prefix and subject-noun

Role-prefix addition (mechanical, via `bin/align-slug`) and subject-noun renaming (judgment-heavy, via review + `bin/rename-slug`) execute in separate cycles. Bundling them creates two failure modes: the segment's prose drifts out of step with its new identity, and decision-makers cannot evaluate the noun choice cleanly when the prefix change is entangled with it. The mechanical pass and the judgment pass want different tooling and different review.

## Why naming deserves a deliberate pass

Names are the user interface of a theory. Every reader — every future agent with 100% context turnover, every collaborator returning after months, every external reviewer auditing a section out of context — encounters the concepts through their names before they encounter the mathematics. A good name compresses the key intuition into a few syllables that survive working-memory pressure; a poor name forces the reader to re-derive what the concept means on each encounter, paying compounding interest forever.

Two concrete examples from the project make the stakes visible. *Satisfaction gap* and *control regret* are names that do work for the reader — after one exposure, the 2×2 disambiguation table organizes itself in the reader's head because the axes are evocatively and accurately named. By contrast, the *A2' sub-scope α₁ / α₂ / β partition* captures something load-bearing in the theory, but the name is a sequence of subscripts, primes, and Greek letters that requires a decoder ring on every encounter. The mathematics is the same quality in both cases; the naming is not.

**Memorable names are the substrate of communal imagination.** A community can argue about, extend, and apply *directed separation* more easily than it can argue about a thing with a clinical multi-word label, because the name has enough shape for a group of minds to get purchase on collectively. This matters most for a framework whose value is integrative — the work is done when others can wield the concepts without the original authors in the room.

The question is not "should we rename everything." It is: **which names are doing load-bearing work, which are coasting, which are causing friction, and where are the missing memorable-noun slots that would repay a deliberate act of naming?** Assume most names were first passes that got propagated by assuming they were deliberate when they were incidental.

## Decision categories

Every naming decision falls into exactly one of these categories. The categories carry different downstream actions; getting the category right matters more than getting the specific name perfect.

1. **Rename.** The current name fails (overclaims, underclaims, is hard to remember, collides with another use, doesn't survive the renamed-from-now-sounds-weird test). A replacement subject-noun takes its place.
2. **Keep.** The current name is right and shouldn't be changed. The act of explicitly committing keep — distinct from "no opinion" — protects names whose churn would cost more than it returns.
3. **Canonicalize.** The current concept *has* a name, but prose paraphrases it three different ways across the repo. The canonicalize commitment is: "going forward, always reference this as X — stop paraphrasing." Distinct from keep because keep doesn't address paraphrase drift.
4. **Add-alias.** The current name is fine for one register but a parallel name in another register would help. Most common case: a Greek/symbol name (α₁, α₂, $\Delta\rho^*$) gets an English alias for use in prose ("the derived-gain regime", "the adaptive reserve"). The formal/structural identifier doesn't have to be a symbol — it can be a legacy English term that's structurally precise but lacks an evocative prose handle. Symbol or formal name stays as the structural identifier; alias enters prose. The pair becomes a maintained convention with strictly differentiated roles, not a free-substitution synonym set.
5. **Name-unnamed-thing.** A recurring pattern, region, formula, methodology, or metaphor that the theory uses repeatedly but never named. A memorable-noun name lands on it. These are the highest-value discoveries because the slot is empty — no displacement cost, pure clarity gain.

### Rename vs. Add-alias — the distinction that shapes downstream action

`rename` and `add-alias` for the same proposed name imply different downstream moves; the category determines what *happens* if the decision lands. The choice hinges on whether the framework benefits from one canonical name or from a pair with separated registers:

- Choose **`rename`** when the original is structurally weak, arbitrary, or forces a lookup that doesn't pay off. The original goes away; the new name takes its place wholesale. Example: `GUC Class 1: Separated / GUC Class 2: Partial / GUC Class 3: Coupled` → `goal-entanglement hierarchy` would be a rename — the numbering scheme forces every reader to memorize it; the alternative names what the classes *measure* and replaces the trio. (The GUC rename that landed 2026-05-09 instead adopted the property names *within* the numbered scheme, a canonicalize rather than rename.)

- Choose **`add-alias`** when the original is formally precise or deeply established but the framework needs a separate, evocative prose handle for discussion, framing, and pedagogy. Both terms persist with strictly differentiated roles. Example: `effects spiral` → `runaway mismatch cascade` as add-alias keeps `effects spiral` as the formal phenomenon name while making `runaway mismatch cascade` the canonical phrase for explaining the mechanism in prose.

Articulated by Gemini-3.1-pro-preview in the 2026-04-29 targeted-alternatives round: *"A strong add-alias means I strongly believe the framework is currently suffering in its readability because it lacks a dedicated, evocative prose noun for a concept that already has a formal identifier. It is a vote to officially mint that prose noun."*

### Rename vs. Canonicalize — invented vs. excavated provenance

A second axis worth distinguishing: *where does the proposed name come from?* Both `rename` and `canonicalize` can land a new name on a target, but the source of the candidate carries different epistemic weight.

- Choose **`rename`** when the candidate is the decision-maker's *invention* — coined to fix a perceived weakness in the current name. The proposed name didn't appear in the project's prose before the decision.

- Choose **`canonicalize`** when the candidate is *excavated* from existing segment prose — the author or contributors had already reached for this phrase informally (in Discussion sections, Working Notes, segment titles, footnotes, brief asides), and the decision promotes the prose-use to formal canonical naming. The phrase is "organically native to the text"; the act is for promotion, not coinage. Note this extends the canonicalize semantics beyond "concept has multiple paraphrases, commit to one" — it covers the related case where the formal naming layer hasn't yet caught up to a phrase the prose has already settled into.

Articulated by Gemini-3.1-pro-preview in the 2026-04-29 targeted-alternatives round: *"When I proposed a 'new alternative' and marked it canonicalize, I was saying: 'The best new name for this concept shouldn't be invented from scratch; the best name is actually this specific, powerful phrase already buried in your prose. You should elevate (canonicalize) it to be the official name.'"*

This carries real provenance signal for finalist decisions: a canonicalize-with-organic-provenance call tells you the phrase fits the concept *empirically* — the author's own writing converged on it — not just that it sounds good in isolation. The downstream master-list surfaces this via a `canonicalize_provenance` field that records where in the prose the phrase already appears, so reviewers can see the source attribution alongside the candidate.

## Evaluation criteria

For each name under consideration, weigh these axes. Not every axis needs to be scored explicitly; these are the kinds of considerations a reasoning trail should capture when a decision is non-obvious.

1. **Self-descriptive vs. baggage-carrying.** A name can *describe* its referent from scratch ("information bottleneck") or *adopt* existing baggage from an adjacent field ("sector condition", "Lyapunov function"). Both can be right. Self-descriptive wins when the field lacks prior art; baggage-adoption wins when the prior art's structural intuitions should travel with the name. The worst outcome is a name whose *only* content is baggage when the theory means something subtly different.

2. **Familiarity gradient.** How many seconds of unfamiliarity does a trained reader in the adjacent field experience? Zero (they see "Lyapunov" and know what to expect) is usually good but occasionally dangerous (if the usage differs, the name creates false confidence). High unfamiliarity is usually bad but occasionally good (a novel name signals a novel concept).

3. **Memorable-noun potential.** Does the name render as a *thing* that can be named in discussion without paraphrase? "Chronica" is a thing. "The AAD complete interaction history with temporal ordering" is not. The asymmetry compounds across every conversation the community will ever have.

4. **Overload risk.** Does the word collide with other uses in the same project, or in adjacent AI/ML vocabulary? "Hierarchy" appears in Pearl's causal hierarchy, AAD's convention hierarchy, AAD's correlation hierarchy, and approximation tiering — four distinct uses in one framework, which is likely too many.

5. **Scope honesty.** Does the name over-promise relative to what the concept delivers? If a name suggests more generality, exactness, or novelty than the concept provides, it violates the same scope-honesty commitment that the rest of the framework holds itself to.

   *Special case for meta-segments.* When a segment names a project-wide pattern (the meta-segments under `01-aat-core/src/discussion-*.md`), scope-honesty dominates memorability. A memorable-but-narrow name (e.g., `#cauchy-coordinates` for what is now `#discussion-additive-coordinate-forcing`) is worse than an awkward-but-accurate name (`#discussion-forced-coordinates`) when the narrow name fails to cover one of the four primary instances. The Round-1 lesson: meta-pattern names reach across many segments; over-narrow ones force prose qualifications elsewhere.

6. **Aging potential.** Some names harden into standard vocabulary; some drift into embarrassment; some become locked in by citation velocity even when better options become available. Names that are too cute age poorly; names that are too clinical never attract citation in the first place.

7. **Communal-imagination test.** The integrating test: *could a skilled reader, six months after first encounter, refer to this concept in a conversation without looking it up?* If yes, the name is compounding; if no, it is costing.

8. **Renamed-from-now-sounds-weird test.** Imagine the project six months from now, the proposed name installed and in routine use. Does the *old* name now sound quaint, dated, or naive — clearly inferior, *of course we renamed it*? Or does the *new* name sound forced, pretentious, like a thing someone tried to make happen? Strong renames pass this test in the first direction; weak renames fail it in the second.

9. **Standalone citability.** Could a researcher reading or referencing this name in a context outside the project — in a different paper, a Slack discussion, a search query — unambiguously point at *this* concept, without having to add a project qualifier ("AAD's bias bound", "TST's specification bound") to disambiguate? This test is the *external* counterpart to overload risk (criterion 4): overload risk asks whether the name collides with other uses inside the project; citability asks whether the name still does work *when extracted from project context*. The Googleability variant is a good operational form — search the bare name; do project-flavor results dominate the top page, or does the name melt into the field's noise?

   *Names that pass the test:* *chronica*, *directed separation*, *orient cascade*, *adaptive reserve*, *purposeful substate*. The pair *satisfaction gap* / *control regret* also passes — both halves are individually generic, but the pair structure is unique and load-bearing for the 2×2 diagnostic, so the *pair* travels even when neither word would alone. *Paired vocabulary* is one of the legitimate routes to citability for an otherwise-generic short name.

   *Names that fail the test:* *bias bound* (thousands of bias bounds in statistics, ML fairness, generalization theory), *change distance* (every diff tool and code-metric paper), *specification bound* (formal verification, software contracts), *detection latency* (used in every field), *causal structure* (used pervasively in stats / ML / Pearl literature), *action selection* (RL-domain term used by everyone). These names work *in-context* — the surrounding paragraph carries the meaning — but they don't travel.

   *When a name fails this test, the resolution is one of four moves:*
   - **(a) Add a structural qualifier the segment already implies.** Example: *bias bound* → *Class 3 (Coupled) ambiguity bias bound* — the segment's own title (`#deriv-observation-ambiguity-bias-bound` reads as "Bias-Bound Constant $C$ for Coupled-Agent Observation-Ambiguity Modulation") already carries the longer disambiguated form; the canonical move promotes that to the citation handle.
   - **(b) Pivot to a more distinct sibling concept.** Example: *specification bound* → *communication bottleneck bound* — the segment carries a named corollary that's sharper than the parent; the move promotes the corollary to the canonical name.
   - **(c) Treat the short form as the in-segment shorthand and commit a longer form as the citation handle.** Analogous to the symbol-to-English add-alias pattern but in reverse: instead of giving math symbols English handles, you give short generic prose names disambiguated cross-reference forms. The short form keeps reading naturally inside the segment ("the bias bound shows..."); the long form is what travels in citations and search queries.
   - **(d) Accept the term and discipline first-encounter cite of the prior-art reference.** When the name is a *deliberately adopted standard* from an adjacent field (e.g., *causal structure*, *action selection*, *multi agent*, *equilibrium convergence*, *feature*) and AAD's use is structurally identical to the field's standard meaning, renaming creates NIH friction without adding distinctive content. The fix is at the *segment* level rather than the *name* level: each segment using the term gets a first-encounter cite of the prior-art reference in its Discussion or opening prose (per FORMAT.md §Findings — Related Work). AAD-distinctive content lives in *what AAD does within the term* — the layered machinery — not in re-coining the scope itself. Where (a)/(b)/(c) change the name to fix the citability gap, (d) accepts the gap and changes the segments to mitigate it. Apply (d) only when the segment's prior-art relationship is genuinely structural-identity adoption (the AAD use *is* the field's standard meaning, possibly with a project-internal narrowing), not "the term is convenient and we don't want to think of an alternative."

   The principle is distinct from familiarity gradient (criterion 2), which asks how much trained-reader intuition the name imports. A name can have low unfamiliarity *and* low standalone citability — *bias bound* is highly familiar but uselessly so, because the familiarity points everywhere. Citability is about whether the name *uniquely points back at this concept*, not whether the reader recognizes any of its words.

## Scope of eligible names

Broad. Any named thing — *or* currently-unnamed-but-recurring thing that would benefit from a name — anywhere in the project is eligible.

### Naming layers

Friction often comes from mixing layers. Note explicitly which layer a decision operates on:

- **Slug layer.** Canonical identifiers like `#strategy-dag`, `#discussion-additive-coordinate-forcing`, `#scope-agency`. Subject-nouns are the decision space; prefix is set by `type:`.
- **Prose-symbol layer.** Default English forms used when prose references a symbol (`α₁` → "the derived-gain regime"). Add-alias decisions typically operate here.
- **Framing-vocabulary layer.** The high-level posture words: "scope-honesty-as-architecture", "calibration laboratory", "strengthen-first posture", "integrating framework". These shape how the project presents itself in introductions and abstracts.
- **Public-API layer.** Section header names (`## Formal Expression`, `## Epistemic Status`, `## Discussion`, `## Working Notes`), framework name (`AAD`, `ASF`), document titles. Read more than any individual segment; rename is expensive.

### Eligible categories

- **Segment subject-nouns.** Slug suffix after the role-prefix. (`#discussion-separability-pattern` → the eligible name is `separability-pattern`; the `discussion-` is fixed by type.)
- **Concept names in prose.** Phrases like "satisfaction gap", "adaptive reserve", "directed separation", "orient cascade".
- **Symbol-to-English aliases.** α₁, α₂, β, η*, ρ, U_o, κ_processing, ε*, etc. — eligible via add-alias category.
- **Pattern and region names — including ones that don't yet have names.** The sector-persistence region in parameter space. The cycle-as-a-whole. The inferential-force cascade across the C1/C2/C3 hierarchy. Eligible via name-unnamed-thing category.
- **Top-level document names and their sections.** README.md headings, NOTATION.md entries, FORMAT.md convention names, TODO.md section titles, CLAUDE.md section headers, OUTLINE.md part names.
- **Framework name itself** (AAD, ASF). Renames here are expensive; treat with extreme care. Note that ASF is the *intentional* parent-level name (AAD is Part I, TST is Part II); earlier rounds misread it as debt.
- **Methodologies and principles.** "Strengthen-first posture", "scope-honesty-as-architecture", "calibration-laboratory framing".

### Acronym discipline

Every new acronym carries a maintenance cost: future readers must memorize it; collisions with adjacent literatures must be checked (recall the ACT → AAD rename forced by the AI Consciousness Test collision); tooling must reference it consistently. Coin new acronyms only when (a) the expanded form will be used 10+ times in nearby prose, (b) the acronym survives the communal-imagination test on its own (without expansion), and (c) the AI/ML / control / cognitive-science literatures have been spot-checked for collisions. When in doubt: don't add an acronym; the unrolled phrase compounds less interest than a forgettable initialism.

**Rule of thumb:** if a name (or paraphrase) would be used repeatedly in a conversation about the theory, it's eligible.

## Meta-principle

Naming is irreducibly aesthetic. There is no derivation that settles it; there is only the accumulated judgment of many readers. Be confident where you are; be honest where you are not.
