## Navigation

### Reading paths

- *Conducting a de-novo audit of the framework?* Please read [`doc/de-novo-audit-instructions.md`](doc/de-novo-audit-instructions.md) first; it documents the recommended posture and the failure modes prior audit cycles surfaced. Use [`README-auditor.md`](README-auditor.md) instead of this file.
- *Academic reader evaluating the framework's claims?* Recommended sequence: this README → [`FINDINGS.md`](FINDINGS.md) (curated novel results with epistemic tiers) → [`01-aad-core/OUTLINE.md`](01-aad-core/OUTLINE.md) (canonical theory outline) → individual segments under `01-aad-core/src/`.
- *Engineer or practitioner?* The [Cross-Domain Joining](#cross-domain-joining) table maps AAD concepts to the domain you likely care about; from there, follow the relevant component OUTLINE.
- *Picking up active work on the framework?* [`TODO.md`](TODO.md) is the navigator for current work items, and [`PROPOSALS.md`](PROPOSALS.md) is the architectural-proposal portfolio.

### Project layout

```
01-aad-core/          AAD mathematical core (Sections I, II, III + Appendices)
  OUTLINE.md          Canonical theory outline (claim by claim)
  src/                Claim segments (one per file, named by slug)
02-tst-core/          Temporal Software Theory (AAD-grounded)
03-logogenic-agents/  Language-constituted agents (framework stage)
04-logozoetic-agents/ Language-living agents (future work)

OUTLINE.md            Top-level assembly index
LEXICON.md            Prose vocabulary (cycle phases, agent classes)
NOTATION.md           Symbol reference
FORMAT.md             Segment file conventions
FINDINGS.md           Curated novel-results catalog (auto-generated)
TODO.md               Active work items
PROPOSALS.md          Architectural-proposal portfolio
CHANGELOG.md          Forward-going cycle record (2026-04-24 onward)
LOG.md                Pre-2026-04-24 cycle archaeology (frozen)
MIGRATION-MAP.md      Prior-work absorption tracking

doc/                  Long-lived process documentation
  de-novo-audit-instructions.md
  naming-principles.md
  readme/             Templates and partials for README generation
msc/                  Working documents, spikes, brainstorms
  SPIKES.md           Spike index
ref/                  Reference papers
bin/                  Build, lint, generation scripts
_obs/                 Superseded materials
```
