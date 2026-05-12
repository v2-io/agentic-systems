# mono — Monograph build pipeline

Self-published monograph snapshot of the full Agentic Systems framework (AAD + TST + Logogenic + ELI). Output is `agentic-framework-v<semver>[+<sha>].{md,pdf}` — both the assembled markdown and the PDF as first-class artifacts. The `+<sha>` is appended for incremental builds after the release tag.

## Build

```sh
mono/build
```

Reads `VERSION`, walks the root `OUTLINE.md` and component outlines, renders to LaTeX via a custom kramdown subclass, compiles with LuaLaTeX + biber.

## Layout

- `main.tex` — kaobook entrypoint
- `preamble/` — fonts, packages, segment environments, status badges, equation-tag commands
- `front-matter.tex` / `back-matter.tex` — title, copyright, bibliography, index
- `vendor/kaobook/` — vendored class (gitignored, fetched by `mono/setup`)
- `.build/<stem>/` — per-build artifacts (gitignored)

## Aesthetic

Tuftish, after Principia Ars Technica: EB Garamond body, Roboto Light sans heads, STIX Two Math, cream paper, generous right margin for sidenotes (equation-level tags, citations, marginal annotations). Open-source fonts throughout — redistributable for the preprint-server snapshots that will carry DOIs.

## Build variants

- `mono/build` — default, public DOI-snapshot build. Strips `## Working Notes` and `stage` from rendered segments.
- `mono/build --review` — internal review build. Keeps Working Notes and stage badges visible.
