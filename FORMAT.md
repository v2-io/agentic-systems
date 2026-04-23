# FORMAT.md — Segment File Conventions

How to write and maintain AAD claim segment files.


## Line Wrapping

Do not hard-wrap lines. Let renderers (GitHub, Obsidian, editors) handle wrapping. One sentence or clause per line is fine for diff-friendliness, but do not insert line breaks at a fixed column width.


## File Organization

- **Segment files** live in `src/` — one claim per file.
- **Filename = slug**: `src/{slug}.md`. No numbering in filenames.
- **Canonical ordering** lives in each component's `OUTLINE.md` (e.g., `01-aad-core/OUTLINE.md`), not in filenames. The ordering will change as the theory develops; the slug is the stable identity.
- **Cross-references** use `#slug-name` — everywhere, always.


## YAML Frontmatter

Every segment file begins with:

```yaml
---
slug: the-slug-name
type: postulate
status: exact
depends:
  - prerequisite-slug-1
  - prerequisite-slug-2
---
```

### `type` — what kind of claim

| Type | Meaning |
|------|---------|
| `postulate` | Tautological or foundational — cannot be derived, only accepted |
| `definition` | Introduces a quantity, object, or notation |
| `scope` | Restricts or broadens the domain under discussion |
| `formulation` | Representational or modeling choice (could be different) |
| `derived` | Logical consequence of prior claims under stated assumptions |
| `result` | Formally stated with a detailed derivation |
| `corollary` | Follows directly from a theorem |
| `hypothesis` | Structurally motivated, needs validation |
| `normative` | Grounded in axioms but requiring a precondition that must be verified |
| `empirical` | Generalization supported by data, not fully derived |
| `observation` | Finding from simulation or empirical investigation |
| `discussion` | Conceptual or normative claim used for interpretation |
| `measurement` | Operationalization of a theoretical quantity |
| `proposed-schema` | Mathematical shape identified, formal content pending |
| `derivation` | Complete formal derivation backing a result or derived claim |
| `worked-example` | End-to-end domain instantiation validating the theory chain |
| `detail` | Extended operational or technical material supporting other claims |
| `sketch` | Outlines an approach or framework; direction identified, rigor pending |
| `aside` | Tangential observation or connection; informative but not load-bearing |

**Why these labels.** The terminology emphasizes that AAD is a *theoretical framework* using existing mathematics, not a pure-mathematics unification project. `postulate` (not `axiom`), `result` (not `theorem`), and `derivation` (not `proof`) avoid the framing that AAD claims foundational mathematical originality where it does not. References to external theorems keep their original names — Cox's theorem, Causal Hierarchy Theorem, Tikhonov's theorem — these are other authors' terms and renaming them would obscure provenance. Segment headings follow suit: `### Derivation`, not `### Proof Sketch`. Equation-level tags use `*[Postulate (slug)]*` and `*[Result (slug)]*`. Historical files (`_obs/`, `msc/`) are not retroactively updated — they preserve the terminology of their era.

### `status` — epistemic strength

| Status | Meaning |
|--------|---------|
| `axiomatic` | Foundational or tautological |
| `exact` | Mathematically validated under stated assumptions |
| `robust-qualitative` | Survives across assumptions; specific form approximate |
| `heuristic` | Useful approximation; quantitative form may not hold |
| `conditional` | Depends on explicitly named local assumptions |
| `empirical` | Supported by data or simulation, not fully derived |
| `discussion-grade` | Argued qualitatively or by analogy, not derived |
| `sketch` | Direction identified but formalization incomplete |

Do NOT use "Solid," "Confident," or "Plausible" as tier labels — these are not AAD terms.

### `depends` — prerequisite slugs

List the slugs this claim directly depends on. The type of each dependency (definition import vs logical antecedent vs scope assumption) is derivable from the referenced file's own `type` field — no typed edges needed.

### `stage` — development process state

Orthogonal to epistemic status. Tracks where the segment is in our working process, not how strong the claim is.

Stage is recorded in segment frontmatter (e.g., `stage: draft`) and in the OUTLINE.md index table. A script can verify consistency between the two.

| Stage | Meaning | Gate to advance |
|-------|---------|-----------------|
| `missing` | No segment file exists yet | — |
| `old` | Content exists only as `old-*` source material, not yet converted | Write AAD-formatted version |
| `draft` | First AAD-formatted version written, not yet reviewed | — |
| `deps-verified` | All dependencies audited | Dependency audit (see below) |
| `claims-verified` | Content reviewed: derivations valid, labels accurate | Content review (see below) |
| `format-clean` | Mechanical review passed | Mechanical review (see below) |
| `candidate` | Ready for external challenge; Working Notes resolved | Working Notes disposition (see below) |

Stages are ordered: a segment at `claims-verified` has also passed `deps-verified`. A segment can be downgraded (e.g., `candidate` → `draft`) when a dependency changes, an error is found, or the claim's scope shifts.


## Promotion Workflow

Segments advance through stages by passing named gates. Each gate has a specific completion criterion — advancement encodes *what has been verified*, not how many times someone has looked at it.

### Ordering: promote in topological order

Compute the dependency DAG from `depends:` fields. Promote leaves first, then their dependents. A segment should not reach `claims-verified` while any of its dependencies is still at `draft` — you cannot verify a derivation whose premises have not been checked.

Group segments into promotion batches by DAG depth. Process all segments in a batch before advancing to the next. Within a batch, segments are independent and can be reviewed in parallel.

### Gate 1: Dependency audit → `deps-verified`

For each entry in `depends:`:

1. The referenced slug exists as a segment file
2. The dependency is genuine — this segment uses the referenced segment's definitions, results, or scope conditions (not merely "related" or "mentioned in Discussion")
3. The referenced segment is itself at `deps-verified` or higher
4. No missing dependencies — if the Formal Expression uses a quantity defined elsewhere, that slug appears in `depends:`

**Completion criterion:** all dependencies verified, no missing dependencies identified.

### Gate 2: Content review → `claims-verified`

The substantive gate. For each segment, answer the three epistemic triage questions:

1. **What prior objects make this claim well-typed?** → Verify `depends:` is complete (should already be, from Gate 1)
2. **What competing formulation would also fit the prior objects?** → Verify `type:` is correct. If only one form fits the priors, it should be `derived` or `result`, not `formulation`. If several forms work and this is the most useful, it should be `formulation`. If it depends on the world, it should be `empirical` or `hypothesis`.
3. **What observation would falsify this claim in practice?** → Verify `status:` is correct. If unfalsifiable and not a definition, something is wrong.

Additionally:

- **Derivation check.** For segments with type `derived`, `result`, or `corollary`: trace each derivation step. Does each step follow from stated premises? Are all premises either in `depends:` or stated as local assumptions with equation-level tags?
- **Label audit.** Does the `status:` field match the actual epistemic strength? Common errors: labeling a formulation choice as `exact`, labeling a hypothesis as `derived`, labeling a conditional result as `exact` without flagging the condition.
- **Formal expression check.** Are equations well-typed? Do quantities have consistent units? Do boundary cases behave correctly?

**Completion criterion:** derivations valid, all labels accurate, no known issues with formal expressions. If the review reveals a mismatch, the segment returns to `draft` with a specific note about what is wrong.

### Gate 3: Mechanical review → `format-clean`

Separate from content review — different cognitive mode.

- Linter passes (`bin/lint-md`)
- Cross-references (`#slug-name`) resolve to existing files
- Notation matches `NOTATION.md`
- Math renders correctly in GitHub and Obsidian (check the compatibility notes above)
- Document cadence matches the template (frontmatter → title → summary → formal expression → epistemic status → discussion → working notes)
- Equation-level tags are present and correct

**Completion criterion:** all mechanical checks pass.

### Spike-segment reverse check (apply at any gate)

For each segment that was promoted from a spike in `msc/`, ask: *what did the spike establish that the segment does not say?* Not every difference is a bug — spike content is exploratory and rightly compressed during promotion — but the direction of compression should be inspected. Flag any claims where the spike's strongest or cleanest form was weakened during promotion, and judge whether the weakening reflects honest editorial compression (keep as-is), a lost promotion-blocking condition (restore to the segment), or a deferred concern that should be explicit in Working Notes.

This is a standing check rather than a gate because spike→segment compression can only be evaluated relative to the source spike, which is a historical artifact. Run the check when touching a segment for other reasons, or when a new finding surfaces the segment's derivation chain.

### Math lives in segments, not spikes

Math derived in a spike must land in a segment — never reside only in `msc/spike-*.md`. Two destinations:

1. **An existing segment**, if the new math tightens, replaces, or extends that segment's content.
2. **A new appendix segment** (more likely for novel derivations with their own claim identity) — added to `01-aad-core/src/` (typically `appendix-*` or a similarly named slug) and recorded in `01-aad-core/OUTLINE.md` under the appendix section.

Spikes record the *attempt*, the *failed branches*, the *reasoning trail*, and pointers to where the resulting math lives. They are not the home for load-bearing derivations. The project's canonical form is the segment set: future agents and reviewers find results by looking at segments, not by archaeology through spikes; math that stays only in a spike cannot be cross-referenced, is not validated by `bin/lint-outline`, does not appear in OUTLINE.md, and is invisible to the theory.

When briefing a spike-agent, include an explicit deliverable: *"if any novel math is derived, land it in segment X (edit existing) or create appendix segment Y (new slug, added to OUTLINE.md)."* When reviewing a spike's output, verify the math has a segment destination — if it lives only in the spike, the work is not yet done.

Appendix segments are the right home for: regret-bound derivations, Fisher-information calculations, sector-condition algebra specific to a result, Cramér-Rao floor calculations, and similar derivation-heavy content that supports a main-section claim.

### Gate 4: Working Notes disposition → `candidate`

Every item in `## Working Notes` must be explicitly resolved:

- **Resolved.** The answer is now incorporated into the segment's Formal Expression or Discussion. Delete the note.
- **Deferred.** The question is real but out of scope for this segment. Move it to `TODO.md` (if it's concrete open work) or a relevant spike document in `msc/` (if it's exploratory), with rationale. Delete the note from the segment.
- **Promoted.** The question warrants its own segment or is a known gap in the outline. Add cross-reference, delete the note.

A segment with unresolved Working Notes is not a candidate. The `## Working Notes` section should be empty or absent at `candidate` stage.

**Completion criterion:** Working Notes section empty or absent. The segment says what it means to say.

### When to downgrade

A segment at any stage can be downgraded to `draft` when:

- A dependency is revised in a way that affects this segment's claims
- An error is discovered in a derivation or formal expression
- The segment's scope changes (e.g., a scope condition is added or removed upstream)
- External review identifies an issue not caught in the original promotion

Downgrade to `draft`, not to an intermediate stage — the segment needs full re-review from the dependency audit forward, since the issue may have cascading effects.


## Document Cadence

1. **YAML frontmatter**
2. **Title** — `# Heading`, human-readable form of the slug
3. **One-sentence summary** — plain text, no heading, immediately after title
4. **Formal Expression** — `## Formal Expression`, with equation-level tags
5. **Epistemic Status** — `## Epistemic Status`, what's derived vs hypothesized
6. **Discussion** — `## Discussion`, interpretation, connections — brief
7. **Working Notes** — `## Working Notes` *(optional)*, internal development notes

Definition, notation, and scope-narrowing files may use a simpler format than full claims. Corollaries and alternate formulations can live with their parent claim (they reinforce its independence), but anything that could be referenced independently should be its own file.

### Working Notes

The `## Working Notes` section is for active development: open questions about the claim, sketches of how AAD machinery might strengthen or weaken it, unresolved issues, things to check. This is *our* working space — what we're thinking about, not what we're asserting. It should be removed or emptied when the segment reaches `candidate` stage. Unlike the Discussion section (which is part of the published theory), Working Notes are process artifacts.

### Voice and provenance

**Segment voice, not diff voice.** Formal Expression, Epistemic Status, and Discussion present the current state of the theory. Avoid phrasing like "landed 2026-04-23", "the prior version of this segment treated X as...", "the msc/spike-Y.md cycle lifted...", or "promoted from spike Z" in those sections — that voice positions the content *against* the theory rather than presenting the segment *as* the theory. State what the theory **is**, not what changed: "Instance 3 of #discussion-identifiability-floor derives..." rather than "Instance 3 (landed 2026-04-23 from spike X) derives..."; "the four instances of the meta-pattern..." rather than "the meta-pattern was extended to four instances after the 2026-04-23 cycle...".

A segment is read by future agents and reviewers who have no context for the chronicle of changes; diff voice forces them to imagine the prior state in order to parse the new state, dates the segment, and positions the content as contingent. Date / commit / spike references belong only in `## Working Notes`.

**Spike references only in Working Notes, only for unfinished work.** Once promoted, a derivation's validity is established by the segment's own argument, not by "see spike X for the full derivation." No spike-X citations in Formal Expression / Epistemic Status / Discussion. If a derivation is promoted, state the derivation; if a result has Monte Carlo verification, state the verification's parameters and outcome in the segment itself.

Spike references in `## Working Notes` are permitted in two narrow forms:

1. **Pointer to unfinished follow-on work.** "The N-agent scaling is unresolved; framing lives in `msc/spike-composition-scaling-N.md`." Once the follow-on lands, the Working Note is replaced by segment content and the spike reference comes out with it.
2. **Brief landing-context provenance.** "Derived in the 2026-04 Gap-cycle work trail (`spike-X.md`)." Permissible, but preferred lean over verbose — the segment's `depends` list and citations carry most of what a future reviewer needs.

Cross-references between segments (`#other-segment`) are unrestricted in any section — they are the normal way segments interoperate. The rule is specifically about spike references, which are transient artifacts. The test: a reader with no knowledge of which spike produced which segment should be able to read any segment as a coherent piece of theory; spike files can vanish without invalidating it.

### Derivation-audit table *(optional; recommended for derivation-type segments)*

Derivation segments, and any segment that carries multiple claims at distinct epistemic strengths, benefit from an executive-summary table that makes each claim's source and tier visible at a glance. The convention is modelled on `#graph-structure-uniqueness`'s "What Is Derived vs. What Is Chosen" table. It pre-empts the "is X derived or chosen?" ambiguity that fresh readers repeatedly stumble on, and serves as the segment-level counterpart to the claim-level equation tags (`*[Derived]*`, `*[Formulation]*`, etc.).

**Location.** Near the end of `## Formal Expression`, before `## Epistemic Status`, under a `### What Is Derived vs. What Is Chosen` heading (exact title may vary — e.g., `### Derivation Audit`, `### Derived vs. Chosen vs. Assumed` — as long as the three columns are the same).

**Format.** Three columns:

| Property | Source | Strength |
|---|---|---|
| *(what the segment claims or defines)* | *(postulate, prior segment, external theorem, or formulation choice)* | *(tier label; see vocabulary below)* |

**Strength vocabulary.** Prefer the TFT tier words already in use for equation-level tags (see §Equation-Level Tags below) so the table aligns with the Epistemic Status paragraph:

- **Proved** — derived from stated priors with a closed-form argument in this segment. Reserve for clean theorem-like claims. Equivalent to *exact*-tier.
- **Derived** — follows from priors, possibly under stated conditions. If conditions are load-bearing, use "Derived (conditional on *X*)".
- **Robust qualitative** — the qualitative claim survives across modeling choices, though a specific functional form is approximate.
- **Heuristic** — the claim is useful operational guidance; a formal tier is not in hand.
- **Formulation choice** — a representational selection motivated by parsimony / domain fit / downstream tractability, not mathematical necessity.
- **Hypothesis** — a claim offered for test, not yet derived.
- **Discussion-grade** — a positional observation, not a derivation.
- **Empirical** — the claim is about the world and awaits validation.

**When to use the table.** Required by review practice only for `type: derivation` segments with three or more claims of mixed strength. Strongly recommended for appendix segments with load-bearing derivations that multiple downstream segments cite. Optional for other segments; a short Epistemic Status paragraph may suffice when only one or two claims are load-bearing.

**What the table is not.** It is not a substitute for the `## Epistemic Status` paragraph. The paragraph explains *why* each claim sits at its tier and names the max attainable status; the table gives the reader a one-screen executive summary of the same content. Both should co-exist on derivation segments; each does work the other cannot.

**Companion convention (C-BP4, if adopted).** Claim-level statuses inside equation tags (e.g., `*[Derived, status: exact]*`) would serve as the inline implementation; the derivation-audit table is the segment-level executive summary. The two compose — table is reader-facing overview; tags are proximate to the math.


## Epistemic Triage

Three questions to ask when writing or reviewing any segment. These determine the segment's honest `type` and `status` — and, critically, its **maximum attainable status** (the strongest epistemic category it could ever occupy, regardless of additional work).

### The three questions

1. **What prior objects make this claim well-typed?** Which definitions, axioms, or derived results must exist for this claim to even be statable? If the answer is "none" or "only standard math," the claim may be foundational. If it requires many prior objects, it sits later in the dependency chain.

2. **What competing formulation would also fit the prior objects?** If the answer is "none — this is the only form compatible with the priors," the claim may be a theorem candidate (mathematical inevitability). If several forms work and you're choosing the most useful one, it's a formulation or design principle. Be honest: most claims have alternatives.

3. **What observation would falsify this claim in practice?** If a concrete falsifier exists, the claim is empirical or hypothesis. If no observation could distinguish it from alternatives, it may be a definition or tautology, not a testable claim. If it's unfalsifiable *and* not a definition, something is wrong.

### Diagnostic

| If... | Then the segment is probably... |
|-------|--------------------------------|
| Only one form fits the priors | Theorem candidate (derived, exact) |
| Several forms fit; this is the cleanest | Formulation (canonical choice) |
| Depends on the world, not the formalism | Empirical or hypothesis |
| No falsifier and not a definition | Tautology or under-specified — revisit |

### Max attainable status

Each segment has a ceiling — the strongest epistemic status it could ever reach, no matter how much work is invested. A segment whose functional form is inherently empirical (e.g., #conceptual-alignment) will never become `exact`; investing effort to "prove" it is wasted. A segment that's discussion-grade because it hasn't been worked yet (e.g., a sketch with a clear proof path) may have `exact` as its ceiling.

When the ceiling is clear, note it in the segment's Epistemic Status paragraph: *"Max attainable: [status]. Currently [status] because [reason]."* This prevents wasted effort and focuses energy where promotion is possible.

### Three rings of segment content

The triage above classifies individual segments; applied across the theory, it produces a coarse structure of three concentric rings. Knowing which ring a segment sits in determines how to review it, what to invest in, and when to stop pushing.

**Inevitability core (~15 segments).** Segments where the goal is "given the prior objects, this is the *only* compatible form." Mathematical inevitability is the ceiling. Review focus: tightening the derivation until no alternative formulation escapes.

The current inevitability-core members, with why inevitability is plausible:

| Segment | Why inevitability is plausible |
|---------|-------------------------------|
| #recursive-update + #recursive-update-derivation | Three constraints → unique recursive form. Strongest result in the theory. |
| #mismatch-decomposition | Bias-variance decomposition: mathematical identity once mismatch is defined. |
| #chain-confidence-decay | log(product) = sum(logs). Pure algebraic identity. |
| #persistence-condition | Given sector conditions, the threshold follows by Lyapunov. |
| #sector-condition-stability + #sector-condition-derivation | Lyapunov stability result applied to mismatch dynamics. |
| #sector-persistence-template | Abstract Lyapunov argument; six AAD results instantiate it. |
| #structural-adaptation-necessity | Parametric update converges within model class; wrong class forces structural change. |
| #orient-cascade | Resolution order forced by information dependency ( $M_t$ before $\Sigma_t$ before $O_t$ ). |
| #satisfaction-gap / #control-regret | Arithmetic once $V_{\text{ideal}}, A_O, V_{\text{current}}$ are defined. Diagnostic value is the insight. |
| #causal-hierarchy-requirement | Application of Bareinboim et al.'s causal hierarchy result to $Q_O$ evaluation. |
| #loop-interventional-access | Feedback loop generates interventional data by construction. |
| #directed-separation | $f_M$ independence from $G_t$ follows from the update structure, given scope condition. |
| #deliberation-cost | Think-vs-act threshold from information-theoretic argument. |
| #composition-consistency | If scope condition doesn't restrict level, predictions at different levels must be compatible. |
| #graph-structure-uniqueness | Four operational postulates + causal sufficiency force a Markov-factorized DAG (Cox-analog). |

**Canonical formulations (second ring).** Good representational choices that are motivated but not forced. Triage question 2 ("what competing formulation would also fit?") answers "at least one alternative exists." Review focus: explaining the choice, noting alternatives, and guarding against drift toward inevitability claims that aren't there.

Current members include: #complete-agent-state, #objective-functional, #value-object, #strategy-dimension, #strategy-dag, #and-or-scope, #agent-model, #information-bottleneck, #event-driven-dynamics, #adaptive-tempo, #structural-change-as-parametric-limit, #explicit-strategy-condition (normative, not derived), #composition-closure (operationalizes #composition-consistency but is one formulation among several possible ones), most definitions.

**Empirical, heuristic, discussion (third ring).** Claims whose ceiling is empirical or heuristic — testable against the world but not derivable from the formalism. This is *not* a demotion: these are where AAD becomes falsifiable and useful. Review focus: stating falsifiable predictions, connecting to validation, resisting the temptation to dress empirical claims as derivations.

Current members include: #update-gain, #mismatch-dynamics, #edge-update-via-gain, #strategic-calibration, #communication-gain, #conceptual-alignment, #exponential-cognitive-load, #changeset-size-principle, most TST and logogenic-agent segments, simulation observations.

**Usage.** When developing or reviewing a segment, first locate its ring. If it's inevitability-core, the goal is tightening the proof. If it's a canonical formulation, the goal is explaining the choice and noting alternatives. If it's empirical/heuristic, the goal is stating falsifiable predictions and connecting to validation. Don't push segments upward beyond their ceiling; don't leave core segments at sketch status when a proof is within reach. The ring assignment is not part of segment frontmatter — it's an analytical stance the reviewer takes.


## Equation-Level Tags

Inline tags before equations mark their epistemic status. These follow TFT conventions (see `notation.md` and `_obs/old-tf-00-notation-conventions.md`):

```
*[Definition (slug-name)]*
*[Derived (slug-name, from ...)]*
*[Derived (Conditional on ...)]*
*[Hypothesis]*
*[Empirical Claim]*
*[Formulation]*
*[Discussion]*
*[Assumption]*
*[Postulate (slug-name)]*
```


## Cross-References

- **In running text**: `#slug-name` — readable, grep-able, meaningful
- **As links from src/ files**: `[#slug-name](slug-name.md)` (relative)
- **As links from root files**: `[#slug-name](src/slug-name.md)`

Both forms work in GitHub and Obsidian. The plain `#slug-name` form is preferred in running prose where clickability is less important than readability.

**Forward references are expected.** Segments routinely reference not-yet-written segments via `#slug-name`. These are intentional dependency markers — they document the claim's connections within the theory even before the target segment exists. Do not treat them as broken links or remove them.

**Obsidian tag recognition**: Obsidian treats `#word` as a tag only when preceded by a space (or start of line). Always ensure a space before `#slug-name` — write `( #scope-agency)` not `( #scope-agency)`, and `see #update-gain` not `see#update-gain`.


## Math Formatting

AAD uses standard LaTeX math that renders in both GitHub and Obsidian.

- **Inline**: `$...$` — no space after opening `$`, no space before closing `$`
- **Display**: `$$...$$` — on their own lines, blank line before and after

### Compatibility Notes

GitHub's math renderer is stricter than Obsidian's. To keep both working:

- No space immediately after `$` or before closing `$`:
  `$x^2$` not `$ x^2 $`
- Display math delimiters `$$` must be on their own lines
- Use `\begin{aligned}` inside `$$...$$` instead of `\begin{align}` (the latter is a top-level environment that conflicts with `$$` wrapping)
- `\text{}` works in both for words inside math
- `\operatorname{}` for multi-letter operators (e.g., `$\operatorname{argmin}$`)
- **Vertical bars**: use `\vert` (not `|`) for single bars and `\Vert` (not `\|`) for double bars, everywhere in math — not just in tables. Raw `|` is ambiguous (conditional? delimiter? absolute value?) and breaks inside markdown table cells; `\|` has inconsistent rendering. For matched delimiters (absolute value, norms, set-builder notation), prefer `\lvert`/`\rvert` and `\lVert`/`\rVert` respectively
- Subscripts/superscripts with multiple characters need braces:
  `$x_{t+1}$` not `$x_t+1$`
- Avoid raw `<` and `>` in math — use `\lt` and `\gt` (GitHub can interpret these as HTML tags, breaking the math span and corrupting everything after the `>`)
- **Asterisks in inline math**: use `\ast` instead of bare `*` inside `$...$`. Markdown's italic/bold parser runs before the math renderer, so `$\eta^*$` can be parsed as `$\eta^` + italic start, destroying the expression. Write `$\eta^\ast$` or `$\eta^{\ast}$`. Display math (`$$...$$` on own lines) is unaffected
- **Underscores and emphasis interference**: when multiple inline `$...$` spans on the same line contain `_` after a non-alphanumeric character (like `}`), GitHub's emphasis parser can match the `_` characters as italic delimiters *across* math spans, breaking all affected expressions. Fix: remove optional braces from single-character command arguments before `_` — write `$\hat P_\Sigma$` not `$\hat{P}_\Sigma$`, and `$\mathcal T_c$` not `$\mathcal{T}_c$`. The braces are optional for single-char arguments and removing them places an alpha character before `_`, which disables GFM emphasis. For nested commands like `$\hat{\mathcal{T}}_t$` where braces can't be removed, restructure the line so only one subscript-bearing expression appears per line. The linter's `--fix` mode handles the brace-removal cases automatically
- **Underscores in `\text{}`**: bare `_` inside `\text{}` can break GitHub rendering (the `_` triggers subscript in math mode and emphasis in markdown). Use `-` instead: `$\mathcal{T}_{\text{obs-noise}}$` not `$\mathcal{T}_{\text{obs_noise}}$`. The linter auto-fixes `_` → `-` inside `\text{}`


## Notation Conventions

Follow TFT conventions. See `notation.md` for AAD's symbol reference. The original TFT conventions are in `_obs/old-tf-00-notation-conventions.md`. Key points:

- **Calligraphic** ($\mathcal{M}$, $\mathcal{O}$, $\mathcal{A}$, $\mathcal{C}$, $\mathcal{E}$) for sets and spaces
- **$\mathcal{T}$** for adaptive tempo (calligraphic to distinguish from temperature)
- **$\lVert\cdot\rVert$** for norms (mismatch magnitude); **$\lvert\cdot\rvert$** for cardinality
- **Subscript $t$**: discrete time or macroscopic continuous time
- **Subscript $\tau$**: continuous event timestamp (microscopic)
- **Superscript $(k)$**: channel index
- **$\mathcal C_t$** for chronica (interaction history) — not $\mathcal{H}$ (avoids collision with entropy)
