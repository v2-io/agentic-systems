## Navigation

### Reading paths

- *Conducting a de-novo audit of the framework?* Please read [`doc/de-novo-audit-instructions.md`](doc/de-novo-audit-instructions.md) first; it documents the recommended posture and the failure modes prior audit cycles surfaced. Use [`README-auditor.md`](README-auditor.md) instead of this file.
- *Academic reader evaluating the framework's claims?* Recommended sequence: this README → [`FINDINGS.md`](FINDINGS.md) (curated novel results with epistemic tiers) → [`01-aat-core/OUTLINE.md`](01-aat-core/OUTLINE.md) (canonical theory outline) → individual segments under `01-aat-core/src/`.
- *Engineer or practitioner?* The [Cross-Domain Joining](#cross-domain-joining) table maps AAT concepts to the domain you likely care about; from there, follow the relevant component OUTLINE.
- *Picking up active work on the framework?* [`PRACTICA.md`](PRACTICA.md) is the strategic-portfolio navigator — the active areas of work with priority markers, sitting above [`TODO.md`](TODO.md) (tactical work items within each area) and [`PROPOSALS.md`](PROPOSALS.md) (architectural-proposal portfolio cutting across areas). Start at PRACTICA; descend into TODO/PROPOSALS as the work directs.

### Project layout

```
01-aat-core/          AAT mathematical core (Parts I, II, III + Appendices)
  OUTLINE.md          Canonical theory outline (claim by claim)
  src/                Claim segments (one per file, named by slug)
02-tst-core/          Temporal Software Theory (AAT-grounded)
03-llm-core/  Language-constituted agents (framework stage)
04-eli-core/ Language-living agents (future work)

OUTLINE.md            Top-level assembly index
LEXICON.md            Prose vocabulary (cycle phases, agent classes; auto-generated from terminology/)
NOTATION.md           Symbol reference
FORMAT.md             Segment file conventions
FINDINGS.md           Curated novel-results catalog (auto-generated)
PRACTICA.md           Strategic-portfolio navigator (active areas of work)
TODO.md               Tactical work items (sits below PRACTICA)
PROPOSALS.md          Architectural-proposal portfolio
CHANGELOG.md          Forward-going cycle record (2026-04-24 onward)
LOG.md                Pre-2026-04-24 cycle archaeology (frozen)

doc/                  Long-lived process documentation
  de-novo-audit-instructions.md
  naming-principles.md
  readme/             Templates and partials for README generation
terminology/          Source-of-truth for prose vocabulary (LEXICON.md is rendered from here)
  entries/            One file per term (YAML frontmatter + markdown body)
  decisions/          Append-only naming-decision events (per-slug audit trail)
  README.md           Schema and tooling guide for the terminology system
spikes/               Research spikes (reasoning trails)
  INDEX.md            Spike index with per-spike status
  PROPOSED.md         Spike-proposal index (3-perspective; optional, low-friction — not exhaustive)
  PROPOSED-ADVANCED.md  Moonshot / theory-edge proposal detail
  PROPOSED-MISC.md    Residual proposal detail (often near-empty)
audits/               Audit-cycle FINAL outputs + pending-findings + per-cycle working dirs
  AUDIT-WORKING-*/    Per-cycle audit intermediate workspaces
msc/                  Other working artifacts (brainstorms, working notes)
  naming/             Current naming-cycle votes + aggregates + rename plan
  reflections/        Author's philosophical/theoretical journal
ref/                  Reference papers + internal references
  agentic-tft/        Prior-bridge AAT-source materials (Feb 2026)
bin/                  Build, lint, generation scripts
_obs/                 Superseded materials
```
