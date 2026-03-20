# TODO — Deferred Organizational Items

## Project Structure

- **Root-level assembly index.** A root OUTLINE.md or INDEX.md that assembles the full "Agentic Systems book" — covering all sections including ACT core, composition, software, logogenic agents, and framework-level content. Deferred until there is organized AS content beyond ACT to assemble.

- **`framework/` directory.** For structured non-mathematical content: architectural guidance, engineering patterns, philosophical foundations (emergence conditions, identity sufficiency, constitutive choice). Currently this material lives informally in msc/ and msc/reflections/. Create when enough content warrants organization.

- **Multiple index support.** The `bin/build` tool can already assemble any outline file. Future indexes for specific outputs: a paper (Sections I+II), a preprint, a monograph, topical selections. Each would be its own OUTLINE file selecting and ordering a subset of segments.

## Content

- **~~Absorb agentic-tft content.~~** Done (2026-03-20). Eight design-relevant documents moved to `msc/agentic-tft-*.md` with origin notes and relevance pointers. Five superseded documents moved to `_obs/agentic-tft-*`. References updated in `03-logogenic-agents/OUTLINE.md` (source material table), `04-logozoetic-agents/OUTLINE.md`, `WORKBENCH.md`, and `CLAUDE.md`. The documents are *sources* for logogenic/logozoetic work, not yet distilled into segments — that distillation should happen when the scope of `03-logogenic-agents/` is decided.

- **Section IV standalone paper outline.** Fastest path to external credibility — no theoretical blockers, high internal coherence (84% self-contained dependencies). Draft outline exists at `msc/2026-03-14-section-iv-paper-outline.md`.

- **Promote segments past draft.** 89 segments at `draft`, zero past it. The 15-20 strongest segments in Sections I+II should be promoted to `candidate` stage.

## Tooling

- **Lint-md directory arguments.** Currently accepts file paths; could accept directory paths to lint all .md files within. Low priority.
