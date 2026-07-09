# BIBLIOGRAPHY-TODO.md — ASF citation system: discipline, tooling, workstreams

*Parent navigator: [FORMAT-TODO.md](FORMAT-TODO.md) Workstream A. This file is the ASF-side companion to the relata-side work: it spells out what ASF agents (Joseph + the ASF instance(s)) own, leaves what relata-side has already done as a recorded handoff, and frames the open citation-discipline decision as the gate everything else flows through. Created 2026-05-20 by a relata-side instance during a planning + bulk-import pass.*

---

## Status at a glance

- **The bibliography database is `~/src/relata/`** (decision recorded FORMAT-TODO A; resolved 2026-05-14). Relata is now a packaged Ruby gem with `relata` on PATH (no more `bin/relata`); the canonical doc tree is per-entry YAML under `relata/entries/<bibkey>.yml`, append-only verification events under `relata/verifications/<bibkey>/`, and PDFs live in an external tree (`RELATA_PDFS_DIR`, default `~/.local/share/relata/pdfs`) — Joseph-backed-up; not in any git repo.
- **ASF has no ASF-local centralized bibliography; relata is the canonical bibliography database.** `ref/INDEX.md` exists but is an old one-off curation (35 entries, 2026-05-04 era) that was never the actual operating bibliography and is now stale per Joseph 2026-05-20 — do not treat it as a source of truth, and do not import it wholesale into relata. The three Undermind-generated research reports in `ref/` (`Novelty_defense_and_integration.md`, `Prior_art_for_unified_agency_theories.md`, `separability-ladder-prior-art-report.md`) are *prior-art research products* — what Undermind surfaced on specific search topics — not the bibliography ASF actually cites *from* in segments. They contain ~78 unique bracketed cite-codes between them and proper References sections at the bottom of each (IEEE-style + DOIs); a fraction of those works is *actually cited* in segments, but the reports themselves are a side-input, not a master list.
- **The first relata-side discovery/import pass is no longer merely pending.** Local check from the ASF checkout on 2026-06-04: `relata list` sees 2038 entries, `ref/` contains 20 `Prior_art_for_AAT_*.csv` Undermind catalogs, and relata's `TODO-ingest.md` §16.16 records the 20-catalog batch sweep as complete at that point (corpus 550 to 1926 valid entries, 97 PDFs registered, 16 manual-download escalations). Later relata-side work has added more entries. Treat the open ASF work here as citation-policy, reconciliation, verification, and segment-migration work — not as waiting for the first discovery sweep to exist.
- **Formal-citation build infrastructure is now wired; segment migration remains open.** Across all four volumes there are still effectively 0 formal citation commands as of 2026-06-05, but `bin/build-monograph` now emits a stage-local `references.bib` through `relata emit`, loads biblatex / kaobiblio in both render targets, runs LuaLaTeX → biber → LuaLaTeX → LuaLaTeX, and copies the generated snapshot to `mono/<slug>-v<sem>.references.bib`.
- **The citation discipline is decided (2026-06-05).** ASF uses the strengthened hybrid discipline below: rich scholarly prose remains allowed, but bibliography-worthy scholarly sources need formal natbib-compatible citation commands, and load-bearing external dependencies need locator-backed, verification-ready formal citations.

## Citation discipline — decided ASF policy (Workstream W-1 landed 2026-06-05)

The dominant Vol1 pattern today is **scholarly inline prose** with mid-sentence italicized titles, editions, and publishers — *"(Pearl 2009, Causality, 2nd ed., Cambridge; Bareinboim, Correa, Ibeling & Icard 2022)"*. This is not the `[Author Year]` bracket form that `~/src/neurips/bin/migrate-cites` was built for; a mechanical regex sweep would homogenize monograph voice and miss most of the references. The decided discipline preserves that monograph voice while adding machine-resolvable bibliography structure.

### Strengthened hybrid rule

1. **Rich scholarly prose remains allowed.** A sentence may still say "Pearl's *Causality*, 2nd ed." or name the publisher / edition / theorem context when that information helps the reader.
2. **Formal citation commands are required for every bibliography-worthy scholarly source.** If a source should appear in the bibliography, include a natbib-compatible cite command in the segment source: `\citep{key}`, `\citet{key}`, `\citealt{key}`, `\citeauthor{key}`, or `\citeyear{key}`. ASF source should not use biblatex-native `\textcite{...}` because the installed relata scanner is keyed to `\cite...` / natbib-style commands.
3. **Load-bearing external dependencies need locator-backed formal cites.** Imported definitions, inherited theorem statements, recapitulated machinery, empirical claims, and prior-art assertions that support segment correctness should use a formal cite with a page / chapter / theorem / section locator where available, then receive `claim-supported` / `page-ref` verification events in relata as promotion work proceeds.
4. **Contextual citations can stay prose-rich, but not prose-only if they belong in the bibliography.** Preserve authorial prose around the cite; do not rely on prose alone to get a source into the emitted `.bib`.
5. **No prose-cited side list for v1.** Do not build a parallel curated "prose-cited" side list in ASF for the first implementation pass. The bibliography is driven by formal cite commands scanned from the rendered volume source.
6. **Canon cites external works directly.** Internal `ref/` reports, Undermind catalogs, and local synthesis notes can remain Working-Notes provenance or search trails, but they are not source-of-truth citations for canon body claims.

This decision unblocks Workstream W-3 (segment migration). Workstream W-4 (build-pipeline wiring) landed with the decision on 2026-06-05.

---

## How to use relata, today

Relata is a packaged gem; `relata` is on PATH after `gem install` (run once on the machine — Joseph maintains the install). Installed CLI access from the ASF checkout is working as of 2026-06-04 (`relata list` sees 2038 entries from `/Users/josephwecker-v2/src/archema-io/asf`).

### Querying

```bash
relata search bareinboim          # fuzzy-match key / author / title / year
relata show pearl-2009-causality  # full entry + verification status + cited-by
relata list --verified            # all entries; flag those with all-criteria verified
relata possible-duplicates --title "active inference" --author friston
```

### Adding entries

```bash
# Interactive scaffold (creates entries/<bibkey>.yml stub)
relata add friston-2017-active-inference-process-theory

# Or paste BibTeX on stdin (recommended when you have a publisher .bib)
echo '@article{friston-2017-active-inference-process-theory, ...}' | \
  relata add friston-2017-active-inference-process-theory

# Or bulk-import from an existing .bib file
relata import path/to/some-bibtex-export.bib
```

Bibkey convention: `firstauthor-year-shortword` (lowercase, hyphenated). Multi-author works can extend: `boyd-ghaoui-feron-balakrishnan-1994-lmi`. Institutional authors: `ieee-7000-2021-ethical-design`. The relata README has the full schema (`~/src/relata/README.md`).

### Registering a PDF for an entry

```bash
relata pdf pearl-2009-causality ~/Downloads/causality.pdf \
  --source "publisher-page-url-or-description" --by joseph
```

This copies the PDF into `$RELATA_PDFS_DIR/pearl-2009-causality.pdf`, computes sha256, extracts the embedded PDF title via `pdfinfo`, and adds an item to the entry's `pdfs:` list. The PDF lives outside the relata git repo (see §11.10 in `~/src/relata/TODO-ingest.md`); Joseph backs the tree up himself.

### Verifying

```bash
# Record a verification act (append-only; never edited)
relata verify pearl-2009-causality bib-fields --by joseph \
  --note "DOI 10.1017/CBO9780511803161 resolves; matches entry."

relata verify pearl-2009-causality doi-resolves --by joseph
relata verify pearl-2009-causality anonymization --by joseph

# Per-paper claim verification (works for AAT segment cites too)
relata verify pearl-2009-causality claim-supported --by claude-asf \
  --note "Vol1 §causal-access-intro cites Pearl Level 2 / do-calculus; verified
          against Causality 2nd ed., Ch.3 (Causal Diagrams and the Identification
          of Causal Effects), pp.65–106."
```

### Linting before any submission / publication

```bash
relata lint                                    # all entries
relata lint 01-aat-core                        # a specific paper/volume dir
REFS_LINT_STRICT=1 relata lint                 # non-zero exit on any finding
```

`lint` checks the anonymization deny-list (catches DOIs / authors that must not appear in a blind submission), schema validity, missing cited keys, and self-cite handling.

### Build-pipeline emit (current `bin/build-monograph` behavior)

```bash
# Conceptual shape; the build script creates a stage-local source dir
# containing exactly the assembled current volume markdown, then runs:
relata emit mono/.build-scrbook/aat/citation-scan --output mono/.build-scrbook/aat/references.bib
```

The emit walks `<paper-dir>/src/**/*.md` for `\cite{}` / `\citep{}` / `\citet{}` / `\citealt{}` / `\citeauthor{}` (all common natbib variants; 2026-05-06 regression test pins the variant set). `bin/build-monograph` deliberately feeds relata a temporary `citation-scan/src/<slug>.md` containing Stage 2's assembled markdown rather than the component's raw `src/` tree, so the bibliography tracks exactly the current rendered volume and does not over-scan `old-*`, orphaned, or non-rendered segment files. Missing keys are reported by relata and now fail the monograph build loudly instead of silently producing a partial bibliography.

### Run-from-ASF note (verified 2026-06-04)

The older relata §11.10 caveat is resolved for installed CLI use. ASF scripts should call the packaged `relata` command directly and pass ASF paths explicitly; no `cd ~/src/relata` workaround is currently required. Build integration should still fail loudly on missing citation keys, because `relata emit` can produce a partial `.bib` for keys it did find.

---

## Current relata capabilities worth relying on

These exist or are recorded as landed on the relata side; ASF doesn't need to reimplement them, but knowing they're there shapes what's worth designing for now vs. deferring:

- **§7.7 calibration loop (landed 2026-05-19, observational).** Every human-confirmed-or-corrected `relata ingest` becomes a labeled datum in `~/src/relata/calibrations/`; the §7.10 defended seed-prior values get periodically refit from empirical likelihood ratios. ASF's ingest events will be the primary positive-sample source once W-3 brings real prose-to-entry migration through `relata ingest` / `relata add`. Not blocking anything; just means more ASF usage = better-calibrated future auto-attach.
- **The ingest pipeline (`relata ingest`).** Drops into `ingest/` are promoted to `entries/` after a per-source evidence-ledger evaluation. Useful for bulk intake of new reference PDFs once W-3 surfaces them.
- **§11.10 broader externalization (landed 2026-05-20; verified for ASF use 2026-06-04).** The canonical data tree is externalized enough that the installed `relata` CLI sees the corpus from the ASF checkout.

---

## Workstreams ASF needs to own

### W-1. Ratify citation discipline

**Done 2026-06-05.** Adopted the strengthened hybrid discipline above. W-3 is now unblocked, but still requires author-judgment passes rather than a mechanical regex migration.

**Status:** landed; keep this section as the decision record.

### W-2. Reconcile `ref/` PDFs against the discovered bibliography

The relata-side discovery/import sweep has surfaced the initial corpus; the local `ref/` PDF set and the entries surfaced by discovery now need reconciliation: which PDFs back which discovered entries (filename + sha256 + pdfinfo title cross-check); which PDFs are orphans (locally-held but not referenced by any segment / tracking doc — decide retain-as-reading-material or remove); which discovered entries are PDF-less (have a citation but no local copy — decide acquire or leave bib-only). Per-item judgment; this is now a reconciliation/verification pass, not a wait-for-discovery pass.

**Probably 1–2 hours of judgment.**

### W-3. Segment citation migration (~270 Vol1 prose references)

Per-segment, author-pass (NOT mechanical regex). For each prose reference in Vol1 (and ~70 more across Vols 2–4):

1. Identify the work (look up in relata: `relata search <author keyword>` or `relata possible-duplicates --title "..."`).
2. If it exists in relata: add a formal natbib-compatible cite if the work should appear in the bibliography; preserve rich scholarly prose around that cite when useful. For load-bearing dependencies, include a locator where available and add a relata verification event as promotion work proceeds.
3. If it doesn't exist in relata: `relata add <new-bibkey>` (scaffold) or paste BibTeX on stdin; fill in fields; then proceed with step 2.

Foundational AAT works still worth checking during migration: quick `relata search` probes on 2026-06-04 did not surface Sutton & Barto's *Reinforcement Learning*, Koller & Friedman's PGM textbook, or Bishop's PRML by those author names; Da Costa active-inference works and Hafez works do surface now. Treat this as a search prompt, not proof of absence: look up each first cite in relata, add the entry if genuinely missing, then proceed with the citation judgment above.

**Substantial — multi-session per-volume work; Vol1 dense, Vols 2–4 lighter.**

### W-4. Wire `bin/build-monograph` to `relata emit`

**Done 2026-06-05.** `bin/build-monograph` now writes Stage 2 assembled markdown to a temporary `citation-scan/src/<slug>.md`, calls:

```ruby
out, status = Open3.capture2e(
  "relata", "emit", scan_dir.to_s, "--output", "<stage>/references.bib"
)
```

The build fails on missing citation keys, writes `references-info.tex`, loads kaobiblio / biblatex with `natbib=true`, runs LuaLaTeX → biber → LuaLaTeX → LuaLaTeX, and copies the generated snapshot to `mono/<slug>-v<sem>.references.bib`.

Installed-CLI note: §11.10 externalization has landed for ASF use, so the build calls `relata` directly from the ASF build context and passes explicit source/output paths. Do not reintroduce a `cd ~/src/relata` workaround unless a fresh local check shows the installed command has regressed.

### W-5. Conditional rendering for `applicable_anonymity` (FORMAT-TODO A6)

When build-target is anonymized AND an entry has `applicable_anonymity: true`, the cite should render as soft form (third-person rephrasing / alternative citation / "Wecker, in preparation"). Lives in the biblatex/relata-emit pipeline; conditional on W-4 being done first.
**Defer until W-3 + W-4 are in motion.**

### W-6. Optional cleanup

The four ref/ prose notes (`Novelty_defense_and_integration.md`, `Prior_art_for_unified_agency_theories.md`, `separability-ladder-prior-art-report.md`, `summary-taking-ai-welfare-seriously.md`) are research-synthesis documents that *reference* works without being the bibliography itself. After W-3 is in motion, sweep these for any cited works that aren't yet in relata and add them. Not urgent; happens organically as the cited segments are promoted.

---

## Boundary — what's relata-side vs ASF-side vs joint

| Concern | Owner |
|---|---|
| relata CLI / storage / ingest / calibration / `emit` semantics | **relata-side** |
| Bulk-import of pre-existing structured bibliographies (e.g., INDEX.md) | **relata-side** (done — see Handoff log) |
| Anonymization deny-list maintenance for ASF-specific terms | **joint** (relata stores; ASF agents add ASF-specific terms) |
| Citation discipline (Option A/B/C) | **ASF-side** |
| Identifying orphan PDFs / adding missing foundational entries | **ASF-side** (you know what AAT cites; relata only knows what relata knows) |
| Per-segment prose-to-`\cite{}` migration | **ASF-side** (voice / scope judgment; relata provides the tools) |
| `bin/build-monograph` integration | **ASF-side** (your build pipeline; relata's `emit` is stable) |
| Conditional rendering for `applicable_anonymity` | **ASF-side** (lives in your build flow) |
| Externalized data root / run-from-ASF CLI behavior | **relata-side** (landed for installed CLI use; ASF consumes through packaged `relata`) |

---

## Handoff log

### 2026-05-20 — relata-side discovery sweep launched; later completed

Joseph corrected an earlier draft of this file (which assumed `ref/INDEX.md` was the existing bibliography). Per his framing:
*"There is **no** de-facto bibliography. There's an old index that got created. You'll actually have to explore the project at depth, probably using an agent, to surface more."*

So instead of importing from a single curated source, a relata-side Explore agent was dispatched 2026-05-20 to sweep the entire ASF tree (all four volumes' segments, the four `ref/` prose notes + INDEX.md + the three Undermind reports' References sections, `doc/`, `terminology/`, `audits/`, `spikes/`, `msc/`, `mono/`, the top-level tracking docs, commit messages, and the `ref/` PDF filenames) and produce a structured inventory of every external scholarly work referenced anywhere — deduplicated across the multiple naming forms (bracketed cite-codes, inline prose, formal LaTeX, bibliography listings, PDF filenames), with provenance per work.

That inventory becomes the input to the actual relata-side bulk-import pass — done as a single coherent commit on the relata side, with `source:` provenance per entry noting its discovery origin (which ASF file(s) referenced it). Re-runnable / idempotent: future discovery sweeps add new entries without disturbing existing ones.

*Status updated 2026-06-04:* the later relata-side `TODO-ingest.md` §16.16 records the full 20-catalog batch sweep as complete, with the corpus at 1926 valid entries at that checkpoint and 97 PDFs registered. A local ASF-cwd check on 2026-06-04 shows the installed `relata` CLI now sees 2038 entries. Final relata commit SHA still belongs in relata's own tracker if needed; ASF's actionable state is now reconciliation and citation-discipline migration.

---

*This file is the ASF-side counterpart to `~/src/relata/TODO-ingest.md`'s §11 + §16 decision/session logs. Updates here as ASF citation discipline evolves; updates there as relata-side capability evolves; the two together are the joint plan.*
