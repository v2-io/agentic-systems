# FORMAT.md — Segment File Conventions

How to write and maintain ACT claim segment files.


## Line Wrapping

Do not hard-wrap lines. Let renderers (GitHub, Obsidian, editors) handle wrapping. One sentence or clause per line is fine for diff-friendliness, but do not insert line breaks at a fixed column width.


## File Organization

- **Segment files** live in `src/` — one claim per file.
- **Filename = slug**: `src/{slug}.md`. No numbering in filenames.
- **Canonical ordering** lives in `CURRENT-FULL-THEORY.md`, not in filenames. The ordering will change as the theory develops; the slug is the stable identity.
- **Cross-references** use `#slug-name` — everywhere, always.


## YAML Frontmatter

Every segment file begins with:

```yaml
---
slug: the-slug-name
type: axiom
status: exact
depends:
  - prerequisite-slug-1
  - prerequisite-slug-2
---
```

### `type` — what kind of claim

| Type | Meaning |
|------|---------|
| `axiom` | Tautological or foundational — cannot be derived, only accepted |
| `definition` | Introduces a quantity, object, or notation |
| `scope` | Restricts or broadens the domain under discussion |
| `formulation` | Representational or modeling choice (could be different) |
| `derived` | Logical consequence of prior claims under stated assumptions |
| `theorem` | Formally stated and proved (or proof-sketched) |
| `corollary` | Follows directly from a theorem |
| `hypothesis` | Structurally motivated, needs validation |
| `normative` | Grounded in axioms but requiring a precondition that must be verified |
| `empirical` | Generalization supported by data, not fully derived |
| `observation` | Finding from simulation or empirical investigation |
| `discussion` | Conceptual or normative claim used for interpretation |
| `measurement` | Operationalization of a theoretical quantity |
| `proposed-schema` | Mathematical shape identified, formal content pending |

### `status` — epistemic strength

| Status | Meaning |
|--------|---------|
| `first-principled` | Axiomatic or tautological |
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


## Document Cadence

1. **YAML frontmatter**
2. **Title** — `# Heading`, human-readable form of the slug
3. **One-sentence summary** — plain text, no heading, immediately after title
4. **Formal Expression** — `## Formal Expression`, with equation-level tags
5. **Epistemic Status** — `## Epistemic Status`, what's derived vs hypothesized
6. **Discussion** — `## Discussion`, interpretation, connections — brief

Definition, notation, and scope-narrowing files may use a simpler format than full claims. Corollaries and alternate formulations can live with their parent claim (they reinforce its independence), but anything that could be referenced independently should be its own file.


## Equation-Level Tags

Inline tags before equations mark their epistemic status. These follow TFT conventions (see `src/old-tf-00-notation-conventions.md`):

```
*[Definition (slug-name)]*
*[Derived (slug-name, from ...)]*
*[Derived (Conditional on ...)]*
*[Hypothesis]*
*[Empirical Claim]*
*[Formulation]*
*[Discussion]*
*[Assumption]*
*[Axiom (slug-name)]*
```


## Cross-References

- **In running text**: `#slug-name` — readable, grep-able, meaningful
- **As links from src/ files**: `[#slug-name](slug-name.md)` (relative)
- **As links from root files**: `[#slug-name](src/slug-name.md)`

Both forms work in GitHub and Obsidian. The plain `#slug-name` form is preferred in running prose where clickability is less important than readability.

**Obsidian tag recognition**: Obsidian treats `#word` as a tag only when preceded by a space (or start of line). Always ensure a space before `#slug-name` — write `( #scope-condition)` not `(#scope-condition)`, and `see #update-gain` not `see#update-gain`.


## Math Formatting

ACT uses standard LaTeX math that renders in both GitHub and Obsidian.

- **Inline**: `$...$` — no space after opening `$`, no space before closing `$`
- **Display**: `$$...$$` — on their own lines, blank line before and after

### Compatibility Notes

GitHub's math renderer is stricter than Obsidian's. To keep both working:

- No space immediately after `$` or before closing `$`:
  `$x^2$` not `$ x^2 $`
- Display math delimiters `$$` must be on their own lines
- Use `\begin{aligned}` inside `$$...$$` instead of `\begin{align}`
  (the latter is a top-level environment that conflicts with `$$` wrapping)
- `\text{}` works in both for words inside math
- `\operatorname{}` for multi-letter operators
  (e.g., `$\operatorname{argmin}$`)
- Escape pipes in tables: use `\lvert`/`\rvert` instead of `|` inside
  math that lives within a markdown table cell
- Subscripts/superscripts with multiple characters need braces:
  `$x_{t+1}$` not `$x_t+1$`
- Avoid raw `<` and `>` in math — use `\lt` and `\gt` if needed
  (GitHub can interpret these as HTML tags)


## Notation Conventions

Follow TFT conventions. See `src/old-tf-00-notation-conventions.md` for the complete symbol table, units, and conventions. Key points:

- **Calligraphic** ($\mathcal{M}$, $\mathcal{O}$, $\mathcal{A}$, $\mathcal{C}$, $\mathcal{E}$) for sets and spaces
- **$\mathcal{T}$** for adaptive tempo (calligraphic to distinguish from temperature)
- **$\|\cdot\|$** for norms (mismatch magnitude); **$|\cdot|$** for cardinality
- **Subscript $t$**: discrete time or macroscopic continuous time
- **Subscript $\tau$**: continuous event timestamp (microscopic)
- **Superscript $(k)$**: channel index
- **$\mathcal{C}_t$** for chronica (interaction history) — not $\mathcal{H}$ (avoids collision with entropy)
