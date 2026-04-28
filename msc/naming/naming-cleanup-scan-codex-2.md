# Naming Cleanup Scan (`codex-2`)

This note is a repo-wide naming-debt scan intended to separate actionable cleanup from intentional historical record. It is not itself a rename pass.

## High-Level Read

1. Real live naming debt is concentrated rather than diffuse.
2. The only clear top-level public naming debt is `Agentic Systems Framework (ASF)` in `CLAUDE.md`.
3. The only material slug debt is the lingering `act-agent` pair in TST and Logogenic Agents.
4. The older "richest operationalization domain" wording is largely already retired from live exposition; most remaining hits are explicit contrast language or historical notes.

## Actionable Live Surfaces

| Surface | Current stale form | Why it is real debt | Suggested cleanup |
|---|---|---|---|
| `CLAUDE.md` | `Agentic Systems Framework (ASF)` in title and opening definition | This is the repo's main orientation document; `ASF` competes with `AAD` and `TST` and conflicts with the current "Agentic Systems" naming direction. | Rewrite the title/opening to `Agentic Systems`; keep the ACT -> AAD historical note below. |
| `02-tst-core/src/developer-as-act-agent.md` | file slug and definition label still use `act-agent` while the H1 already says `Developer as AAD Agent` | This creates repeated friction between filename, slug, and displayed title. It is the clearest stale post-rename surface in TST. | Rename the file, frontmatter slug, and formal label together after the alias decision between `aad-agent` and `adaptive-agent`. |
| `02-tst-core/OUTLINE.md` | `[#developer-as-act-agent](src/developer-as-act-agent.md)` | The canonical TST index still advertises the stale slug. | Update the link target and displayed slug after the file rename lands. |
| `02-tst-core/src/software-epistemic-properties.md` | prose refs to `#developer-as-act-agent` | This is a live, reader-facing dependency reference. | Rewrite cross-references when the slug rename lands. |
| `02-tst-core/src/code-quality-as-observation-infrastructure.md` | dependency on `developer-as-act-agent` | Dependency graph will go stale if only the primary file is renamed. | Update dependency/cross-reference in the same change. |
| `02-tst-core/src/causal-discovery-from-git.md` | dependency on `developer-as-act-agent` | Same reason: downstream reference to stale slug. | Update in the same change. |
| `02-tst-core/src/software-scope.md` | working-notes mention of `#developer-as-act-agent` | Lower-priority than canonical links, but still semi-live. | Update if the notes are meant to stay current; otherwise leave as historical commentary. |
| `03-logogenic-agents/src/ai-agent-as-act-agent.md` | file slug and definition label still use `act-agent` while the H1 already says `AI Agent as AAD Agent` | Same pattern as the developer segment, and this one is especially visible because it is the entry point to the section. | Rename the file, frontmatter slug, and formal label together after the alias decision between `aad-agent` and `adaptive-agent`. |
| `03-logogenic-agents/OUTLINE.md` | `[#ai-agent-as-act-agent](src/ai-agent-as-act-agent.md)` | The canonical section outline still points to the stale slug. | Update the link target and displayed slug after the file rename lands. |
| `03-logogenic-agents/src/section-ii-survival.md` | dependency and prose refs to `ai-agent-as-act-agent` | Core cross-reference in a live section result. | Update in the same change. |
| `03-logogenic-agents/src/context-turnover.md` | dependency on `ai-agent-as-act-agent` | Same reason. | Update in the same change. |
| `03-logogenic-agents/src/coupled-update-dynamics.md` | dependency on `ai-agent-as-act-agent` | Same reason. | Update in the same change. |
| `03-logogenic-agents/src/observation-ambiguity-modulation.md` | dependency on `ai-agent-as-act-agent` | Same reason. | Update in the same change. |
| `03-logogenic-agents/src/m-preservation.md` | dependency on `ai-agent-as-act-agent` | Same reason. | Update in the same change. |

## Semi-Live Internal Surfaces

These hits are real, but they behave more like project-management or audit records than reader-facing theory text.

| Surface | Current form | Treatment |
|---|---|---|
| `TODO.md` | open findings still refer to `#developer-as-act-agent`; resolved note quotes the older "richest operationalization domain" framing | Update only if the TODO list is expected to reflect post-rename slugs; otherwise treat as session history. |
| `audits/pending-findings-2026-04-22.md` | audit findings reference `#developer-as-act-agent` and the older software framing | Leave unless the project has a policy of keeping historical findings synchronized with current slugs. |
| `audits/audits-2026-04-22-evening.md` | finding text references `#developer-as-act-agent` | Same: this reads as a historical record, not active surface debt. |
| `audits/analysis-2026-04-06.md` | analysis text lists `developer-as-act-agent` and related surfaces | Treat as historical analysis unless there is a broader cleanup policy for `msc/analysis-*`. |

## Intentional Historical Or Archival Surfaces

These should not be bulk-cleaned by search/replace.

| Surface family | Why it should usually be left alone |
|---|---|
| `msc/naming/name-transition-aad.md` | This is the authoritative record of the ACT -> AAD rename and should preserve the old names explicitly. |
| `LOG.md` | Historical notes such as "ACT -> AAD rename" are part of the chronology, not debt. |
| `_obs/**` | These are older observation / predecessor materials and contain large amounts of pre-rename vocabulary by design. |
| `_obs/2026-03-13-landscape-research/**` and similar dated research notes | These preserve earlier analytical framing and source-era terminology. |
| `env/env-act.tex` | Historical environment/template naming; rename only if there is a deliberate environment cleanup. |
| `spikes/sim-three-way-tradeoff.py` and similar exploratory files | Exploratory code and reasoning trails often preserve source-era naming; only touch if these become active artifacts again. |

## Specific Read On The Software Framing

The older "richest operationalization domain" / "best operationalization domain" wording no longer looks like major live debt.

- `02-tst-core/OUTLINE.md` and `02-tst-core/src/software-epistemic-properties.md` now use the calibration-laboratory framing and mention the older wording only as a rejected contrast.
- `CLAUDE.md` also already uses the calibration-laboratory framing correctly.
- Remaining hits are mostly in TODO / audit / analysis material documenting the change.

So the software-framing cleanup is largely complete; the `act-agent` slug cleanup is not.

## Recommended Cleanup Order

1. Decide the destination slug family for the two `act-agent` segments: `aad-agent` or `adaptive-agent`.
2. Rename the two primary segment files, their frontmatter slugs, and their formal definition labels in one pass.
3. Update the two section outlines and all direct downstream dependencies in the same commit.
4. Separately clean `CLAUDE.md` to remove `ASF` from the repo's main orientation surface.
5. Leave historical and audit material alone unless there is an explicit archival-normalization project.
