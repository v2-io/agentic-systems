# I.10 method: where is something written about a claim, and how much must a cold agent read?

*KR **I.10** of `../INTENT.md`, under objective I ("The system keeps it true"). Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." (Joseph, 2026-10-30). The aim, Joseph's: future agents should not spend hours working out whether a change supersedes what was written elsewhere, or was made in ignorance of it.*

This file says what the numbers mean, so a later measurement is comparable. The numbers themselves are in dated files beside it.

## Rerun

From this directory (Python 3, standard library only; reads git and disk, writes only `data/`):

```
python3 -I measure.py pre-integration-2026-10-30 <new-sha> --label sample-<date>
python3 -I measure.py pre-integration-2026-10-30 <new-sha> --all --label census-<date>
python3 -I summarize.py data/sample-<date>
python3 -I summarize.py data/census-<date>
```

A run takes under a minute. Always re-measure the tag in the same run: the influx is read from disk at run time and used for every ref in the run (see *Influx*), so a tag number from an earlier run is not comparable with a new HEAD number. Keep `sample.tsv` and `influx-roots.txt` fixed. If either has to change, re-measure the tag with the new version and say so. `make-sample.py` drew the sample once and is kept for provenance; running it again with the same seed and ref reproduces `sample.tsv`.

## The sample

`sample.tsv` holds 46 claims. The population is the 244 segment slugs (no `old-*` legacy files) that exist under the same slug and volume at both `pre-integration-2026-10-30` (`4ee2b895`) and `5eee086c`. Two slugs renamed in between (`deriv-graph-structure`, `deriv-evidence-allocation-ceiling`) and one new segment are outside it.

- **Random, 30 claims** (seed `"I.10 2026-10-30"`): Volume 1 gets 20, split 7/7/6 across terciles of Working-Notes size at the tag (WN size is the obvious noise proxy, so the sample is not allowed to miss either end), and Volumes 2, 3 and 4 get 4, 3 and 3. This is the KR's fixed sample.
- **Purposive, 16 claims**: the canon targets of `../influx-scout/MAP.md` §3 that exist at both refs. It is labelled and reported separately because it is where the drains looked hardest.
- **Census**: `--all` runs the same measure on every claim in the population. It tests whether the sample represents the whole. On 2026-10-30 it did: the random sample's signal shares were within 0.02 of the census's on every row.

## What counts as a mention

A file mentions claim $c$ if the slug occurs with no letter, digit, `_` or `-` immediately on either side. That matches `#slug`, `segment:slug`, `src/slug.md` and bare `slug`, and it does not match a longer slug that contains this one. Matching is by slug only. Paraphrases, old slugs and material that developed a result without naming it are invisible to this measure (see the account's *What the measure gets wrong*).

Files read: tracked `.md`, `.markdown`, `.tex` and `.udon` files at the ref, read from git, not from a checkout, so untracked files and other worktrees never enter. Excluded: `.vsect/` (it stores copies of segment text) and this directory. `.txt` is excluded everywhere because, on the drive, it is mostly tooling data (file lists, dumps) whose slug hits say nothing about a claim.

## The claim's home (signal)

- **Body**: the segment file minus its `## Working Notes` section (that heading to the next level-2 heading).
- **Ledger**: every record under `items/`, `questions/` and `reviews/` that mentions $c$. A record is *keyed* when its frontmatter `concerns:` names `segment:c`. A keyed record is costed whole. An unkeyed one is costed only where it mentions $c$ (the unit below). `vsect open` shows only keyed, open records, so this is wider than the tool's view: it is what a grep finds.

Signal words = body + ledger.

## Places, and their classes

A **place** is a file, other than the claim's home, that mentions $c$, with one exception: a mention in another segment's Working Notes is the place "that segment's WN". The claim's own Working Notes are always a place. Places are classed by path (`i10lib.classify`):

| class | paths | counted as noise? |
|---|---|---|
| own-wn | the claim's own `## Working Notes` | yes, always must-read (it is in the file a reader opens) |
| other-wn | another segment's Working Notes | yes |
| spikes, audits | `spikes/`, `audits/` | yes |
| msc-effort | `msc/inside-out-2026-10/` (this effort's own residue: drain accounts, lane files, maps, reviews) | yes, reported separately |
| msc | the rest of `msc/` | yes |
| trackers | `TODO.md`, `PRACTICA.md` and the retired tracker names | yes |
| root-docs | other root `.md` (e.g. `HISTORICAL-CONTEXT.md`, `TST-IDEAS.md`, `NOTATION.md`) | yes |
| doc, ref, component-other | `doc/` (except README partials), `ref/`, non-front files under a volume dir | yes |
| influx | text files under `influx-roots.txt`, outside asf | yes |
| other-body | another segment's body | no: canon cross-reference (reported) |
| front | `README*`, `FINDINGS.md`, `LEXICON.md`, `OUTLINE.md`, `INTRODUCTION.md`, `CURRENT-VOL*`, `doc/readme/src/` | no: generated or front matter (reported) |
| history | `CHANGELOG.md`, `LOG.md` | no: the history layer (reported) |
| archived, influx-archived | any `.integrated/`, `.archived/`, `.archive/`, `.super-archive/` path | no: retired by location (reported) |
| vocab | `terminology/` | no (reported) |

The "no" rows are judgments, not facts. They exclude canon, generated surfaces and the places the project's own conventions mark as retired. The per-class counts for every row are in `data/*-claims.tsv` (`n:<class>`, `b:<class>`, `s:<class>`), so a reader who draws the line elsewhere can re-add them. For example, A.2's concern (front surfaces restating bodies) lives in the `front` and `other-body` columns.

## Reading cost

For each place, two units, both in whitespace-separated words (words survive md-press's unwrapping and its Unicode-to-LaTeX pass, and lines and characters do not):

- **block** (lower bound): the smallest readable unit holding each mention, unioned. That is a paragraph, a list item (its marker line to the next marker), or a table row; a mention in a heading takes the heading plus the block under it. Add the file's preamble (first heading plus first block, capped at 150 words), which is what a reader needs in order to know what the file is.
- **section** (upper bound): the leaf heading-delimited section holding each mention, unioned (the whole file when it has no headings).

Neither unit has been calibrated against what a cold agent actually reads (see the account). The two differ by roughly a factor of four to six, so a conclusion is reported only where it holds in both units.

## Accounted: does anything tell the reader what this place is to the claim?

Each noise place other than own-wn gets one state, first match wins:

- **L**: a ledger record about $c$ names the place. That means a keyed record anywhere in its text, or an unkeyed record in a section where it mentions $c$. For other-wn: such a record names the host segment and says "Working Note".
- **D**: a drain account (`msc/inside-out-2026-10/drain/*.md`) names the place. A drain account never accounts for itself or for another drain account, since reading it is the cost of this route. For other-wn: a drain account names the host segment.
- **H**: the claim's own segment file (body or WN) names the place.
- **U**: nothing names it.

"Names" means the text contains the place's path (with or without extension), its directory (when the directory is specific, not `spikes/` or `audits/`), its file stem (when that stem is unique across everything read), or, for audits, the six-digit audit id the drains use. This matches records at the granularity they cite. It is lenient on purpose. **Named is not the same as disposed.** A drain naming `AUDIT-WORKING-628417/` says that audit was walked, not what it says about this claim. So L and D measure findability of a disposition record, which is an upper bound on how many places a reader can safely skip.

**Must-read** for a claim = own WN + the reading cost of every noise place not discounted, in two variants:

- **strict**: only L discounts. The ledger is the designated, durable record (I.3).
- **with drain**: L and D discount. This counts the drain accounts' dispositions as available, which holds only while those files exist.

H does not discount. A pointer from the segment to a spike says nothing about whether the spike supersedes the segment or is superseded by it.

**Signal share** = signal / (signal + must-read). **Total reading** = signal + must-read. Total reading is the better single figure, because signal share rises when the ledger or the bodies simply get longer.

## Influx

`influx-roots.txt` lists the regions of `../influx-scout/README.md`, read from disk at run time and used unchanged for every ref in a run, so the influx contributes the same places to both snapshots. Only their *accounted* state changes, as the ledger and drains come to name them. Nothing outside asf has a `pre-integration` tag, and the drains did not edit those repos.

- **Included**: the unscouted `aisi-eoi` and `notability-extracts`. Only slug counts and paths are taken from them; nothing from them is read into a report.
- **Excluded**: `~/src/overarching` (private, Joseph-gated) and `~/src/vestigia` (private).
- **Excluded as projections or tooling data**: asf itself, `AISI-responses/extract/` (a generated projection of canon), udon's `recall-floor/` and md-press `model/`, and VCS, build and tool-state dirs (`.git`, `.claude`, `.vsect`, `node_modules`, `target`, virtualenvs).
- **Skipped**: files over 2 MB.

## Output files

`data/<label>-claims.tsv` has one row per claim per ref, with every quantity above and per-class columns. `data/<label>-places.tsv` has one row per place: ref, slug, class, path, mention count, block and section words, whole-file words, and state. The census places file (about 6 MB) is not committed. It regenerates in under a minute.
