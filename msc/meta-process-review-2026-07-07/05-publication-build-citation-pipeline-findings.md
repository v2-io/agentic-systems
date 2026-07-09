# 05 — Publication / Build / Citation Pipeline — Findings

*Cluster 05 of the 2026-07-07 meta-process review. Scope: the path from segments to published artifacts — the markdown-first monograph build (`mono/`, `bin/build-monograph`, four volumes), FORMAT-TODO workstreams A (citation) / B (cross-refs, footnotes, sidenotes) / C (discipline + structural distinctions), the relata bibliography partnership + BIBLIOGRAPHY-TODO, Zenodo/CITATION.cff/.zenodo.json archival readiness, committed build-artifact hygiene, and the figure/illustration pipeline.*

*Method note: everything below is verified firsthand (git log/show, grep counts, a live `relata emit`, a bounded `bin/build-monograph aat` run, Ruby `-c` syntax checks) unless explicitly marked as relayed from a tracking doc. Where a tracker's claim and the working tree disagree, both are stated — the disagreement is itself part of the map.*

---

## 0. Firsthand health signal (verified 2026-07-07)

A bounded `bin/build-monograph aat` run (scrbook, review variant) got through:

```
[aat/scrbook] ingesting (variant: review)…
[aat/scrbook] assembling + typesetting (toc: on)…
  rendered=163 missing=1 gaps=9 errors=0
[aat/scrbook] emitting references…
  references=9   0 missing
[aat/scrbook] compiling aat-v0.3.0s…   <- still running when my 90s bound killed it
```

- **Stages 1–2 + reference-emit: GREEN firsthand.** 163 segments rendered, 0 render errors, 1 missing segment, 9 gaps (expected — these are declared `--GAP--`/missing rows), 9 citation keys resolved with 0 missing.
- **Stage 3 (LuaLaTeX compile): not verified to completion.** The 650-page compile was progressing normally at the 90s cutoff; the `IOError: stream closed` in the output is my timeout killing the subprocess mid-read, *not* a build defect. Last-known-green full compile is per commit history / the figure memo (2026-05-18, "651 pp, exit 0") and the `8815345` (2026-06-05) citation wiring.
- **All five pipeline modules parse** (`ruby -c` OK): `ingest.rb`, `assemble.rb`, `typeset.rb`, `segment_renderer.rb`, `outline_walker.rb`.
- **`relata` is live**: on PATH via mise (`~/.local/share/mise/.../bin/relata`), sees **2077 entries** (trackers say 2038 on 2026-06-04 / 355 in an older note — trackers lag, corpus grew).

Net: the build spine is healthy. The gaps in this slice are in the *conventions and citation-migration layer on top of it*, not the machine.

---

## (a) De-facto processes actually running

1. **Markdown-first volume build** — `bin/build-monograph <slug> [--target scrbook|kaobook] [--public] [--all]`. Three stages: ingest (`OUTLINE.md`+`src/` → `mono/.build-<target>/<slug>/chunks/` + `index.md`), assemble (chunks → assembled volume markdown, cross-refs resolved), typeset (kramdown `AsfLatex`/`AsfVolumeLatex` converter → LuaLaTeX → PDF). scrbook is the **authoritative** target (per FORMAT-TODO 2026-06-05); kaobook present but not optimized. Runs manually; no CI. **Health: de-facto, functional.**

2. **Citation emit into the build** — `bin/build-monograph` writes Stage-2 assembled markdown to a temp `citation-scan/src/<slug>.md`, calls `relata emit` to produce `references.bib`, fails loudly on missing keys, runs LuaLaTeX→biber→LuaLaTeX→LuaLaTeX, copies `mono/<slug>-v<sem>.references.bib`. Verified working (9 entries, 0 missing). **Health: de-facto, functional — but consuming almost no cites (see below).**

3. **Figure embedding (AAT only)** — Obsidian embed `![[src/img/<name>.pdf]]` + `{#fig-<slug> caption="…"}`; resolver in `ingest.rb` compiles a sibling `.tex` (TikZ) → PDF via lualatex when newer, includes via `\includegraphics` (the `\includestandalone` route was found structurally incompatible, 2026-05-18). Figures are first-class `#fig-` cross-ref atoms. **Health: de-facto for Vol 1; dormant elsewhere (§d).**

4. **Committed-artifact refresh (ad hoc)** — `CURRENT-VOL1.md` + `CURRENT-VOL1.pdf` at repo root are hand-copied assembled Vol-1 outputs, re-committed episodically ("Update monograph after lots of the most recent changes", "Rebuild current-vol1 md and pdf…"). This is a **discoverability workaround**: `mono/*.md` and `mono/*.pdf` are gitignored (`mono/.gitignore`: "Track … only when it's a tagged release worth pinning"), so the assembled markdown has no committed home *except* this manual root copy. **Health: de-facto but inconsistent — the two artifacts drift (§d).**

5. **relata bibliography curation** — done relata-side (2077 entries, 20 Undermind catalogs ingested, PDFs externalized under `RELATA_PDFS_DIR`). ASF consumes via `relata search/show/emit/verify`. **Health: de-facto healthy on the relata side; the ASF-consumption side barely started (§b/§d).**

## (b) Aspirational processes the docs/SOPs intend

FORMAT-TODO decomposes the on-top-of-build work into three workstreams. Landed vs open, verified against the tree:

**Workstream A — Citation system.** Infra *landed*: relata as canonical DB (A1), hybrid discipline ratified 2026-06-05 (A2), `relata emit` wired into build (A4), `citation_status` schema (C13). **Open and barely-started:** A3 segment migration (~270 Vol-1 + ~70 Vols 2–4 prose references → formal cites), A5 `applicable_anonymity` conditional rendering, W-2 `ref/`↔relata reconciliation.

**Workstream B — cross-refs / footnotes / sidenotes / margin-notes. Almost entirely UNSTARTED.** B6 (`[[#^anchor]]` atom-level cross-refs) open; B7 (`\label{atom:<name>}` LaTeX emission — author-side parsing exists, LaTeX side doesn't; **blocks C15**) open; B8 (footnote convention — **zero footnote usage anywhere in the corpus**) open; B9 (sidenote, pending Open-Q3) open; B10 (general margin-note — only equation-tag `\marginnote` exists) open; B11 (`xr-hyper` cross-volume refs, pending Open-Q4) open.

**Workstream C — discipline + structural distinctions. Mostly open.** C12 (imported-vs-AAT-native marking, pending Open-Q2) open; C13 (citation_status schema) **landed**; C14 (Discussion-segment schema split in FORMAT.md) open; C15 (auto-cross-ref formula sweep, gated on B7) open; C16 (FORMAT.md doc sweep) open; C17 (chapter groupings for Parts II/III/IV — "Joseph chooses") open; C18 (FORMAT-compliance linter sweep, "~200+ findings") open.

**Archival-publication readiness (aspirational).** CITATION.cff + .zenodo.json exist, wired to a real Zenodo concept DOI (`10.5281/zenodo.19986312`). The *intent* is versioned re-release on milestones; in practice it ran once (§d).

## (c) Emergent patterns from git history

- **Build pipeline = a compressed, disciplined burst then maintenance.** The whole markdown-first pipeline landed in a tight sequence over ~2026-05-11→13 (`5f949d0` plan → `be33269` Stage 1 → `62b2e1e` Stage 2 → `610b549`/`c448a00`/`e84cd80` Stage 3 → render refinements), with the scrbook target following (`18e0604`→`f33c110`). Staged, each-commit-buildable, exactly as the design doc's migration plan prescribed. This is a healthy, plan-then-execute meta-process that *worked*.
- **Citation work is a thin recent seam, not a sweep.** The entire formal-citation footprint in canon arrived in a single day: discipline decided + build wired (`8815345`, 2026-06-05) and the first cites added (`dcb1974` "Add Pearl causal-access citations", 2026-06-05). A second small cluster rode in later with the multi-timescale-stability promotion. **Total formal-cite reach today: 5 segment files, ~9 keys** (Pearl+Bareinboim; Friston, Chen-Goldenfeld-Oono, Haken, Kokotović, Saberi-Khalil, Tikhonov). The other ~340 prose references are untouched.
- **Figure work is a single autonomous burst, never repeated.** `36879bd` (pipeline) + the 2026-05-18 `msc/figure-pipeline-buildout` memo wired **5 figures into Vol 1** in one AFK-sanctioned session, catalogued the rest "for Joseph's editorial eye," and then the cadence stopped. No figure has been wired since; Vols 2–4 have zero figures.
- **Naming-rename discipline is visible and thorough.** The AAD→AAT sweep (`df0101c`→`e7263d8`, 2026-05-15) touched publication metadata, dirs, slugs, bin scripts, dep-graphs in staged commits — but left two keyword residues (§d).
- **Trackers are updated conscientiously but still lag the tree** — BIBLIOGRAPHY-TODO says "27 ref/ PDFs" (actual: **80**), "355 relata entries" then "2038" (actual: **2077**), "effectively 0 formal cites" (actual: **9 keys**). Expected drift; noting it because staleness-of-trackers is part of what this review maps.

## (d) Stale / broken / abandoned — concretely

1. **Archival metadata frozen two months + several minor versions behind.** `CITATION.cff` and `.zenodo.json` both last touched 2026-05-15 (the rename commit), both declare `version: 0.1.0`, `date-released: 2026-05-02`. But `mono-meta.yaml` versions are now **AAT 0.3.0, TST 0.2.0, LLM 0.1.0, ELI 0.1.0**. Only **one Zenodo release ever cut** (`v0.1.0` tag, 2026-05-02). The citing/archival record points at a snapshot that predates most of the last two months of work.
2. **Committed `references.bib` snapshot is stale.** `mono/aat-v0.3.0.references.bib` (committed) holds **2 entries** (Pearl + Bareinboim). A live `relata emit` from current `01-aat-core` src yields **9** — the committed snapshot predates the multi-timescale-stability citation landing. The build regenerates it correctly; the committed artifact is out of date.
3. **`CURRENT-VOL1.pdf` is a stale committed generated artifact.** `.md` rebuilt 2026-06-11 (`ac7d07c`); `.pdf` last rebuilt 2026-05-25 (`25546d2`) — the committed PDF is ~17 days and one full deaths-taxonomy restructure behind its own sibling markdown. Both (3.0 MB + 5.1 MB) are generated output committed at repo root, contradicting `mono/.gitignore`'s own stated policy (track only tagged releases; `CURRENT-VOL1` is neither tagged nor version-named). Referenced only from CHANGELOG.
4. **G3 citation debt still live in 9 segments.** `ref/Novelty_defense_and_integration.md` is cited as source-of-truth in **9 segment files** (`der-directed-separation`, `der-causal-insufficiency-detection`, `deriv-causal-ib-exploration`, `deriv-causal-ib-lmi`, and 5 more across AAT+TST). The CLAUDE.md sanction that magnified this was excised 2026-05-30, but the segment-level citations remain — INTEGRATION-CLEANUP-TODO §G3 tracks it as "~15+"; actual is 9.
5. **`ref/`↔relata reconciliation (W-2) unstarted.** 80 PDFs in `ref/`; no committed reconciliation of which back which relata entry, which are orphans, which entries are PDF-less.
6. **Vols 2–4 have zero figures**; the figure "scattering" pass covered only AAT. `sector-cone.tex` and ~14 SVG-only diagrams remain catalogued-not-wired in AAT itself.
7. **Two AAD keyword residues** survive the rename in `CITATION.cff:29` and `.zenodo.json` keywords ("adaptation and actuation dynamics"). Low-stakes — the phrase is deliberately vacated-for-reuse, but as a *keyword* on the AAT record it's arguably wrong.

## (e) Decisions genuinely blocked on Joseph

These are the routing-worthy ones — each a short ask, each unblocking downstream work:

1. **Cut a fresh archival release?** Bump `CITATION.cff`/`.zenodo.json` to reflect AAT 0.3.0 (+ sibling versions), mint a new Zenodo version DOI, tag it. Publication act; irreversible-ish (a DOI is permanent). *Context he needs:* "metadata says v0.1.0 / 2026-05-02; volumes are now 0.3/0.2; one release ever cut."
2. **`CURRENT-VOL1` committed-artifact policy.** Keep hand-committing 8 MB of generated output at root for discoverability, or gitignore it and rely on release tags / a stable `mono/` release path? Taste call with a real discoverability tradeoff *he* set up. *(If kept, at minimum the `.pdf` needs a rebuild — it's a restructure behind the `.md`.)*
3. **Imported-vs-AAT-native marking** (FORMAT-TODO Open-Q2 / C12): frontmatter `origin:` field + render cue ($\alpha$) vs distinct segment type ($\beta$) vs convention-only ($\gamma$). Blocks C12. Authoring-voice call.
4. **Sidenote source-side convention** (Open-Q3): pandoc `^[…]` vs mark+def vs magic-comment. Blocks B9.
5. **Cross-volume xr-ref fallback form** (Open-Q4): bibliography-form vs placeholder vs soft-ref. Blocks B11. Needs each volume's canonical citation form declared in `mono-meta.yaml`.
6. **Chapter groupings for AAT Parts II/III/IV + TST/LLM/ELI** (C17): "Joseph chooses chapter groupings (with build-side dependency-cluster help)."
7. **The bulk citation migration (A3/W-3) is author-judgment by design** — relata-side explicitly *declines* to auto-rewrite prose→`\cite{}` (voice territory). So the ~340-reference job is Joseph, or Joseph-with-an-agent, per volume. Not a decision so much as a large owner-gated task; flagged because it's the single biggest deferred publication-critical item and won't move without him.

## (f) Candidate meta-process definitions

| # | Process | Trigger | Steps | Health |
|---|---|---|---|---|
| P1 | **Volume build** | source/OUTLINE change; release prep | `build-monograph` ingest → assemble → typeset (scrbook auth., kaobook 2nd) | **de-facto** — green through Stage 2 + emit (verified); Stage 3 last-green 2026-06-05; manual, no CI |
| P2 | **Citation migration** (prose → `\cite` via relata) | segment promotion / publication prep | look up in relata → `add` if missing → formal natbib cite + locator → `relata verify` event | **emergent / stalled** — discipline+infra landed 2026-06-05; ~5 segments / 9 keys done; ~340 refs open |
| P3 | **Bibliography reconciliation** (`ref/`↔relata) | pre-publication | match PDFs↔entries (sha/pdfinfo); classify orphans; acquire PDF-less | **aspirational** — unstarted (W-2) |
| P4 | **Figure production + editorial placement** | segment needs a diagram; audit "gold" surfaces a candidate figure | author `.tex` → embed convention → **verify-against-canon** → wire (Joseph's eye) | **mixed** — de-facto for AAT (5 wired, one 2026-05-18 burst); **abandoned** for Vols 2–4 |
| P5 | **Archival release** (Zenodo + CITATION.cff/.zenodo.json + tag) | version milestone | bump metadata → mint version DOI → tag | **stale** — ran once (v0.1.0, 2026-05-02); not repeated despite version bumps |
| P6 | **Committed-artifact refresh** (`CURRENT-VOL1.*`) | "lots of recent changes" (ad hoc) | rebuild → hand-copy to root → commit | **broken/anti-pattern** — `.md` and `.pdf` drift; contradicts repo's own gitignore policy |
| P7 | **FORMAT-compliance sweep** (lint-md/lint-outline) | pre-promotion; convention change | `bin/lint-md`/`lint-outline` → fix | **partial** — linters exist and run per-file; the corpus-wide C18 sweep (~200+ findings) never executed |

## Out-of-scope surfacings (passed back deliberately)

- **⚠ Commercial font family committed to a CC-BY public repo.** `mono/scrbook/fonts/garamond/` = 37 `.otf` files, ~35 MB, a full **Garamond Premier Pro** family (Adobe commercial). Committing these to a public GitHub repo (`v2-io/agentic-systems`, CC-BY-4.0) is a plausible licensing violation / redistribution landmine — distinct from any hygiene concern. Worth a deliberate look before the repo goes (or is) public. (Inter / FiraCode alongside are open-licensed; Garamond Premier Pro is the exposure.)
- **Repo-root binary bloat.** `abstract-d.svg` (21 MB), `abstract-dl.png` (6 MB), `msc-as-logo.svg` (8.5 MB) tracked at root; `_obs/` holds far worse (`abstract-agentic-b.svg` **96 MB**, `-normalized.svg` 18 MB, `.png` 7 MB). These inflate every clone. Outside citation/build scope but squarely publication-hygiene.
- **`mono/` holds committed non-release PDFs against its own policy** — `aat-v0.2.0s.pdf`, `aat-v0.3.0s.pdf`, `eli-v0.1.0*.pdf`, `tst-v0.*.pdf` etc. (several MB each) are present in the working tree; most appear untracked-but-present (gitignored `*-v*.pdf`), but a `git ls-files` shows the bib snapshot and metadata are the tracked bits — worth confirming none of the multi-MB PDFs slipped past the ignore during the rename churn.
- **The relata partnership is a genuine cross-project dependency worth naming at the portfolio level**: ASF's publication-citation critical path runs through a *separate repo* (`~/src/relata/`) with its own tracker (`TODO-ingest.md`). The joint plan is split across `BIBLIOGRAPHY-TODO.md` (ASF) + `TODO-ingest.md` (relata). Healthy, but a coordination seam a portfolio-level view should hold.

---

*Files cited: `FORMAT-TODO.md`, `BIBLIOGRAPHY-TODO.md`, `INTEGRATION-CLEANUP-TODO.md` §G3, `JOSEPH-TODO.md`, `NEXT-UP.md`, `PRACTICA.md`, `CITATION.cff`, `.zenodo.json`, `CURRENT-VOL1.{md,pdf}`, `mono/aat-v0.3.0.references.bib`, `mono/.gitignore`, `msc/figure-pipeline-buildout-2026-05-18.md`, `msc/markdown-first-pipeline.md`, `bin/build-monograph`, `bin/lib/*.rb`, `01-aat-core/src/img/*.tex`, `mono/scrbook/fonts/garamond/`. Commits: `dcb1974`, `8815345`, `36879bd`, `df0101c`, `be33269`→`e84cd80` (pipeline), `f903f7d`/`ac7d07c`/`25546d2` (CURRENT-VOL1).*
