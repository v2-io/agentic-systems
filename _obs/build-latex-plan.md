# Plan: LaTeX Build Script

## Goal
Create `bin/build-tex` that reads the same OUTLINE.md files and segment sources as `bin/build`, but produces LaTeX output suitable for arXiv publication.

## Key Decisions Needed
1. **LaTeX vs ConTeXt?** — LaTeX is standard for arXiv. ConTeXt is more powerful but less common. Recommend LaTeX.
2. **Document class** — `article` for a single paper, `amsart` for math-heavy, or `revtex4-2` for physics-style. Given the math + control theory audience, `amsart` seems right.
3. **One file or multi-file?** — Could produce a single .tex or a main.tex + \input{} per segment. Single file is simpler for arXiv submission.
4. **What to do with Working Notes** — Strip them (like `--strip-working-notes`).
5. **Math conversion** — The markdown already uses LaTeX math (`$...$` and `$$...$$`). Main work is converting the markdown prose formatting to LaTeX.
6. **Cross-references** — Convert `#slug-name` tags to `\ref{slug}` or `\cref{slug}`.
7. **Equation-level tags** — Convert `*[Definition (slug-name)]*` to appropriate LaTeX environments.
8. **Tables** — Convert markdown tables to LaTeX tabular.
9. **Epistemic status sections** — Keep as paragraphs or use a custom environment?

## Implementation Phases

### Phase 1: Core markdown-to-LaTeX converter
- Strip YAML frontmatter (reuse logic)
- Convert `# Heading` → `\section{}`, etc.
- Convert `$...$` → pass through (already LaTeX)
- Convert `$$...$$` → `\begin{equation}` or `\[...\]`
- Convert `**bold**` → `\textbf{}`
- Convert `*italic*` → `\textit{}`
- Convert markdown lists → `\begin{itemize}`
- Convert markdown tables → `\begin{tabular}`
- Convert blockquotes → custom environment or `\begin{quote}`

### Phase 2: Academic structure
- Segment numbering (Definition I.1, etc.) → LaTeX theorem-like environments
- Cross-reference rewriting → `\label{}/\ref{}`
- Table of contents → automatic via LaTeX
- Preamble with notation macros from NOTATION.md

### Phase 3: Polish
- Custom theorem environments matching the type system
- Proper equation numbering
- Bibliography support (if needed)
- arXiv compliance check

## Architecture
- Reuse `bin/build`'s outline parsing, segment resolution, and numbering logic
- Add a markdown-to-LaTeX conversion layer
- Add LaTeX document wrapper (preamble, begin/end document)
