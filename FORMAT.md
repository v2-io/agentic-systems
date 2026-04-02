# FORMAT.md — Segment File Conventions

How to write and maintain ACT claim segment files.


## Line Wrapping

Do not hard-wrap lines. Let renderers (GitHub, Obsidian, editors) handle wrapping. One sentence or clause per line is fine for diff-friendliness, but do not insert line breaks at a fixed column width.


## File Organization

- **Segment files** live in `src/` — one claim per file.
- **Filename = slug**: `src/{slug}.md`. No numbering in filenames.
- **Canonical ordering** lives in each component's `OUTLINE.md` (e.g., `01-act-core/OUTLINE.md`), not in filenames. The ordering will change as the theory develops; the slug is the stable identity.
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

Do NOT use "Solid," "Confident," or "Plausible" as tier labels — these are not ACT terms.

### `depends` — prerequisite slugs

List the slugs this claim directly depends on. The type of each dependency (definition import vs logical antecedent vs scope assumption) is derivable from the referenced file's own `type` field — no typed edges needed.

### `stage` — development process state

Orthogonal to epistemic status. Tracks where the segment is in our working process, not how strong the claim is.

Stage is recorded in segment frontmatter (e.g., `stage: draft`) and in the OUTLINE.md index table. A script can verify consistency between the two.

| Stage | Meaning | Gate to advance |
|-------|---------|-----------------|
| `missing` | No segment file exists yet | — |
| `old` | Content exists only as `old-*` source material, not yet converted | Write ACT-formatted version |
| `draft` | First ACT-formatted version written, not yet reviewed | — |
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

### Gate 4: Working Notes disposition → `candidate`

Every item in `## Working Notes` must be explicitly resolved:

- **Resolved.** The answer is now incorporated into the segment's Formal Expression or Discussion. Delete the note.
- **Deferred.** The question is real but out of scope for this segment. Move it to `WORKBENCH.md` or a relevant spike document with rationale. Delete the note from the segment.
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

The `## Working Notes` section is for active development: open questions about the claim, sketches of how ACT machinery might strengthen or weaken it, unresolved issues, things to check. This is *our* working space — what we're thinking about, not what we're asserting. It should be removed or emptied when the segment reaches `candidate` stage. Unlike the Discussion section (which is part of the published theory), Working Notes are process artifacts.


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

**Obsidian tag recognition**: Obsidian treats `#word` as a tag only when preceded by a space (or start of line). Always ensure a space before `#slug-name` — write `( #scope-condition)` not `( #scope-condition)`, and `see #update-gain` not `see#update-gain`.


## Math Formatting

ACT uses standard LaTeX math that renders in both GitHub and Obsidian.

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

Follow TFT conventions. See `notation.md` for ACT's symbol reference. The original TFT conventions are in `_obs/old-tf-00-notation-conventions.md`. Key points:

- **Calligraphic** ($\mathcal{M}$, $\mathcal{O}$, $\mathcal{A}$, $\mathcal{C}$, $\mathcal{E}$) for sets and spaces
- **$\mathcal{T}$** for adaptive tempo (calligraphic to distinguish from temperature)
- **$\lVert\cdot\rVert$** for norms (mismatch magnitude); **$\lvert\cdot\rvert$** for cardinality
- **Subscript $t$**: discrete time or macroscopic continuous time
- **Subscript $\tau$**: continuous event timestamp (microscopic)
- **Superscript $(k)$**: channel index
- **$\mathcal C_t$** for chronica (interaction history) — not $\mathcal{H}$ (avoids collision with entropy)
