# Findings — Cluster 10: repo-decomposition strategic question (decision brief for Joseph)

*Written 2026-07-07 by a Claude instance (Opus 4.8, 1M context). This is an evidence-gather-and-frame deliverable, **not** a recommendation to execute. Joseph raised the question: agentic-systems is "essentially a big monolithic repo that could easily decompose into many repos but also derives advantage from the proximity and pull toward cohesion." Below: the coupling map (measured), what's cleanly separable, the carve-out history, the cost/benefit of each direction, and the decision framed as options-with-consequences. All counts are from mechanical grep over the current working tree, cross-checked against a slug-to-volume index; I did not audit the mathematics.*

---

## 0. The one-paragraph frame

The word "monolith" is doing two jobs and they need splitting. **(a) Packaging:** the repo is 836M on disk / 225M git-tracked, but the theory content is 8.6M (under 4% — the rest is `ref/` external PDFs 135M, `_obs/` obsolete archive 162M, `mono/` build artifacts 116M mostly un-gitignored). **(b) Coupling:** the four theory volumes are genuinely interpenetrated — not a clean core-and-dependents DAG — with ~470 cross-volume slug references, 15 hard filesystem links, one shared terminology namespace, one shared tool/tracker layer, and at least one load-bearing *reversed* dependency (Volume-1 appendix is the apparatus for a Volume-3 result). The packaging half is a cheap cleanup; the coupling half is the real strategic question, and the measured coupling is dense enough that a full four-repo split would sever load-bearing tissue. **The separable seam that the evidence actually supports is not "decompose the theory" but the pattern already running: derived artifacts (papers, experiments, sims) live in their own repos; the theory core stays cohesive.**

---

## 1. What couples tightly (the cohesion, measured)

### 1.1 Cross-volume slug references — ~470, and *not* a clean DAG

Referencing volume → defining volume, resolved against the 235-slug index:

| from → to | count | reading |
|---|---|---|
| `03-llm-core` → `01-aat-core` | 166 | LLM volume leans hard on the core |
| `04-eli-core` → `01-aat-core` | 152 | ELI volume leans hard on the core |
| `02-tst-core` → `01-aat-core` | 74 | TST leans on the core |
| `01-aat-core` → `03-llm-core` | **42** | **core reaches *down* into LLM** |
| `04-eli-core` → `03-llm-core` | 37 | ELI built on LLM substrate |
| `03-llm-core` → `04-eli-core` | 20 | LLM points forward to ELI |
| `01-aat-core` → `04-eli-core` | **18** | **core reaches down into ELI** |
| `01-aat-core` → `02-tst-core` | **13** | **core reaches down into TST** |
| `02-tst-core` → `03-llm-core` | 6 | |
| `03-llm-core` → `02-tst-core` | 1 | |

The load-bearing observation: **`01-aat-core` back-references into all three derived volumes (42 + 18 + 13 = 73 downward refs).** If the dependency were a clean tree (derived → core only), the core would publish standalone and the others as dependents. It is not. Most of the 73 downward refs are in Discussion / Working Notes / "open question" sections (soft pedagogical pointers — "likely lives in part 03's treatment", "the natural home is `03-llm-core`"), which is the introduced-before-used discipline reaching forward. But at least one is hard (§1.4).

### 1.2 Hard filesystem cross-volume links — 15

15 markdown links of the form `](../../0N-{x}-core/src/{slug}.md)` physically wire one volume's `src/` to another's on the filesystem (8 point at `03-llm-core`, 8 at `01-aat-core`; one file both directions). These are relative paths that **break the moment two volumes become separate repos** — they'd need a submodule layout, a shared-path convention, or rewriting to a citation-style reference. Fifteen is small enough to rewrite by hand but they are the concrete thing a split has to solve first.

### 1.3 Shared terminology namespace — one lexicon, all four volumes

`terminology/entries/` holds 141 term entries; `LEXICON.md` (41K, auto-generated) is the single prose vocabulary for the whole repo; `bin/term` is the append-only, multi-agent-safe CLI. A term means the same thing in Volume 1 and Volume 4 *by construction*. Splitting the repo forces a choice: duplicate the lexicon (drift risk — the exact failure the system was built to prevent), or make it a shared dependency (build-coupling across repos). Term usage is core-weighted (01: 29 files, 02: 8, 03: 1, 04: 3) but the *namespace* is shared.

### 1.4 One load-bearing reversed dependency (the sharp one)

`01-aat-core/src/deriv-observation-ambiguity-bias-bound.md` is, in its own words, "the quantitative apparatus underlying" two `03-llm-core` segments (`#scope-observation-ambiguity-modulation`, `#result-section-ii-survival`), which "retain their client status; the quantitative work moves here." So **the mathematics backing a Volume-3 result physically lives in a Volume-1 appendix**, linked by `../../03-llm-core/src/...` paths. This is not a "see also" — it is the derivation. Any split at the 01/03 seam has to decide where this segment lives and rewire the client links. It is the single clearest piece of evidence that 01 and 03 are not cleanly separable.

### 1.5 Shared build pipeline, tooling, and root trackers

- **Build:** `bin/build-monograph` (Ruby, markdown-first, `VOLUME_REGISTRY` of all four) plus `bin/lib/` (ingest/assemble/typeset) and `mono/{scrbook,kaobook}/`. One pipeline builds any volume. Cross-volume numbered references are handled via persisted `.aux` xr-refs (scrbook) with `\externalref` fallback — see §2.2 for why this actually *reduces* the build-coupling.
- **Tooling:** ~24 `bin/` scripts (align-slug, rename-slug, extract-findings, extract-known-issues, lint-md, lint-outline, build-readme, term, naming-master-*, segment-stats) all operate repo-wide and are maintained once.
- **Root trackers, all cross-volume:** `TODO.md` (117K), `PROPOSALS.md` (115K), `CHANGELOG.md` (379K), `PRACTICA.md`, `FINDINGS.md` (313K, auto-generated from all four volumes' `## Findings`), `NOTATION.md`, `FORMAT.md`. FINDINGS.md in particular is a single generated catalog spanning all four volumes.

### 1.6 Commit-level coupling — real but a minority

Over the last 500 commits, multi-volume commits exist but are not the norm: 13 touched 02+04, 7 touched 01+04, 6 touched **all four** (the AAD→AAT rename sweep + slug-alignment sweeps — see §3.1), 4 touched 03+04, 4 touched 01+03, 3 touched 01+02. Most work is single-volume (01 dominates: touched in 1119 file-instances vs 82/108/105 for 02/03/04). **Reading:** day-to-day authoring is volume-local; the cross-volume commits cluster around *global refactors* (renames, slug sweeps) — which is exactly the operation cohesion makes cheap and decomposition makes expensive (§4).

---

## 2. What is cleanly separable

### 2.1 The derived-artifact repos — already carved, already build-independent (the proven pattern)

The publication/experiment repos — `synthese-paper`, `neurips`, `causal-language`, `behavioral-floor`, `embeddings` — are **already separate repos and already build-independent of agentic-systems.** Their only references to agentic-systems live in *tracking/orientation docs* (README, LOG, STRATEGY, PROGRESS, CLAUDE.md, ORIENTATION.md), never in manuscript source or build files; the manuscripts cite the framework as anonymized "AAD" formal ground. This is the de-facto decomposition process that *is* running, and it works: derived artifacts get their own repo, stay build-independent, and link back by citation + a bridge doc (§2.3). Cluster 06 owns the full census; for this brief the point is that the successful separation boundary in practice is **theory-core vs derived-artifact**, not **volume vs volume**.

### 2.2 Each volume already builds standalone

Every volume has its own `mono-meta.yaml` and `OUTLINE.md`; the root `OUTLINE.md` states "each of which can also be built independently," and `bin/build-monograph aat` builds one volume alone, resolving sibling-volume cross-refs to `\externalref{slug}` (prints the slug as text) rather than failing. So **single-volume PDF output is already supported** — the cohesion is at the *source and reference* layer, not a hard build blocker. Decomposition would not buy standalone-buildability; that already exists.

### 2.3 The bridge-doc pattern (how decoupled-but-linked already works here)

`doc/vivarium.md` ↔ `~/src/vivarium/ASF.md` is a worked two-file bridge between agentic-systems and a separate active repo: each side states what it offers the other, with hypothesis-grade mappings marked. This is the existing mechanism for *cohesion without co-location* — it is what any future cross-repo relationship would use, and it is evidence that Joseph's project neighborhood already knows how to keep separate repos conceptually bound without a monorepo.

### 2.4 Relative separability of the volumes themselves

If a volume-level cut were forced, the evidence ranks the seams:
- **`02-tst-core` is the most separable** (74 refs to 01, only 6 to 03, ≤1 elsewhere; its own framing is "AAT-grounded but independently consequential"). It is the cleanest single cut — but note the core barely reaches back into it (13 refs), so the tissue is thin in both directions.
- **`04-eli-core` is separable-under-cost** (152 refs to 01 + 37 to 03 to rewire) but is the volume with a *non-coupling* reason to separate (§4.3 — sensitivity).
- **`01-aat-core` ↔ `03-llm-core` is the densest, least separable seam** (166 up + 42 down + the §1.4 load-bearing apparatus). Splitting these two is the expensive cut and the evidence argues against it.

---

## 3. Carve-out history (how prior separations went)

### 3.1 agentic-systems itself: never split, renamed twice

First commit 2026-03-09 as **ACT** (Agentic Cycle Theory); 1015 commits total. Renamed ACT→AAD (2026-04-16, welfare-literature collision) and AAD→AAT (2026-05-15, "upgrade to Theory"). The AAD→AAT rename is the most instructive event for this question: it was a **coordinated multi-stage sweep touching all four volumes + `bin/` + `terminology/` + `doc/` + `ref/` + trackers in staged commits** (visible in git log: "Stage 5 terminology", "Stage 6 bin/", "Stage 7a active spikes", "Stage 8 lineage", "Stage 10a mono pipeline"). This is the paradigm case of what cohesion buys — a framework-wide rename executed atomically with cross-volume consistency guaranteed. In a four-repo world this is four coordinated PRs with a consistency window between them.

### 3.2 The sibling repos — all *derived-artifact* carve-outs, all clean

| repo | first commit | origin |
|---|---|---|
| `embeddings` | 2026-01-23 | **predates** agentic-systems; independent origin, not a carve-out |
| `ops` | 2026-04-27 | strategic dossier, own origin |
| `neurips` | 2026-05-05 | "Initial parent shell" |
| `synthese-paper` | 2026-05-08 | **carved from `ops`** — "Synthese paper dossier moved to its own repo" (ops commit 3994623); clean move |
| `causal-language` | 2026-05-13 | AIES paper, own origin |
| `behavioral-floor` | 2026-05-13 | AIES paper, own origin |
| `practica` | 2026-05-18 | public composite-agent sibling |
| `vivarium` | 2026-06-20 | "docs-first repo for ASF-agent simulation game" |
| `vestigia` | 2026-07-04 | membership-inference harness |

**Pattern:** every carve-out is a publication, experiment, sim, or ops artifact — never a piece of the theory core. The one *intra*-repo carve on record (synthese from ops, 2026-05-08) was a clean directory-move of a self-contained dossier and went well. There is **no precedent in this history for splitting the theory itself**, and the theory core has stayed monolithic across two renames and 1015 commits by apparent preference, not oversight. The closest analogue to a paper-extraction discipline is documented in `msc/2026-05-08-three-move-shape-of-paper-extractions.md` — but that is about extracting *papers from* the framework, which sharpens the extracted result (defensive theorem/corollary separation), explicitly a *gain-producing* operation; it is not evidence for decomposing the substrate.

---

## 4. What cohesion buys vs. what decomposition would cost/buy

### 4.1 What cohesion currently buys (the cost of losing it)

1. **Atomic cross-volume refactor** — the AAD→AAT rename, slug-alignment sweeps (`bin/align-slug --all`), and terminology renames all execute across four volumes in one coherent operation with no cross-repo consistency window. This is the biggest concrete benefit and the git history shows it is *exercised regularly*, not hypothetical.
2. **One terminology namespace** — a term is defined once and means the same thing everywhere; `bin/term`'s multi-agent-safety is repo-wide.
3. **One findings/notation/format layer** — `FINDINGS.md` is a single generated catalog across volumes; `NOTATION.md`/`FORMAT.md` govern all four uniformly.
4. **Introduced-before-used discipline across volume boundaries** — the meta-patterns M1–M4 live in Volume 1 and are referenced from Volumes 3/4; the 73 downward refs are the core pedagogically pointing forward to where each abstraction gets instantiated. This is a design virtue that co-location makes free.
5. **Single-grep discoverability** — an agent working any volume greps one tree; the "where does AAT treat X" question has one search surface.
6. **The monograph as one assembled work** — the four-volume monograph with cross-volume numbered references (the `.aux` xr-hyper machinery, aspirational per `mono/scrbook/preamble/segment.tex`) presupposes co-location for the authoritative cross-volume label source.

### 4.2 What full four-repo decomposition would cost

1. Rewire ~470 cross-volume slug references + 15 hard filesystem links to a submodule/registry/citation scheme.
2. Resolve the §1.4 load-bearing reversed dependency (Volume-1 apparatus for a Volume-3 result) — decide its home and rewire client links.
3. Split or shared-dependency-ize the terminology system (drift risk vs build-coupling — no free option).
4. Duplicate or vendor the `bin/` tooling and `mono/` pipeline across repos.
5. Lose atomic refactor; every future framework-wide rename becomes N coordinated PRs with consistency windows.
6. Fragment the trackers (TODO/PROPOSALS/CHANGELOG/FINDINGS) or maintain a super-repo index.

### 4.3 What decomposition would buy (the genuine upside, stated fairly)

1. **Independent maturity/release cadence.** The volumes are at very different stages: Volume 1 (AAT) is preprint-ready; Volume 4 (ELI) is "future work." Separate repos let Volume 1 version and release without Volume 4's churn.
2. **Sensitivity decoupling — the one non-coupling reason with real force.** Volume 4 (ELI, `04-eli-core`) carries the consciousness/moral-status material that the orientation letter and reflection #28 both flag as globally sensitive and 2027-deferred with defensive infrastructure. Separating `04-eli-core` into its own (possibly private) repo would let Volumes 1–3 publish *without* the ELI association visible in the same tree — a defensive-decoupling argument that is about **exposure**, not about code structure. This is the decomposition rationale the evidence most supports as a *distinct* consideration (it survives even though 04→01 coupling is 152 refs, because the driver isn't separability, it's blast-radius isolation).
3. **Lighter agent clones** — but see §0: the theory is 8.6M; the weight is `ref/`+`_obs/`+`mono/`, addressable without any split.
4. **Sharper ownership boundaries** — marginal in a single-author project.

---

## 5. The options, framed (NOT a recommendation)

**Option A — Status quo (keep the monolith).** Consequences: retains all §4.1 benefits; the "feels like it wants to split" tension persists but is mostly the §0 packaging illusion; zero migration cost. The latent question stays latent.

**Option B — Packaging cleanup only (orthogonal to decomposition; likely the cheap win).** Move `ref/` (135M external PDFs) to a submodule or out-of-tree store, retire/relocate `_obs/` (162M), gitignore `mono/` build artifacts (116M). Consequences: repo drops from ~225M tracked toward ~10M of actual content; clones get light; **the theory stays exactly as cohesive.** This is not decomposition — it directly targets what a fresh observer reacts to as "monolithic." Low risk; reversible. *(Flagging as the thing most likely being conflated with the real question.)*

**Option C — Continue the de-facto pattern (extract derived artifacts, keep the core whole).** Consequences: proven, low-risk, already running (§3.2); publications/experiments/sims get their own repos linked by citation + bridge docs; the four-volume theory core remains monolithic. This is the status quo *process*, made explicit as a stated policy rather than an unstated habit.

**Option D — Split `04-eli-core` off (sensitivity-driven, not coupling-driven).** Consequences: isolates the politically-sensitive ELI material so Volumes 1–3 can publish without the association; costs rewiring 152 (04→01) + 37 (04→03) refs and the terminology/tooling-sharing decision; loses atomic refactor *with* the core for that volume. The rationale is exposure-isolation (§4.3.2), and it must be weighed as such — the coupling counts argue *against* it on separability grounds, so this option only makes sense if the sensitivity argument outweighs the coupling cost. **Genuinely Joseph's call** — it trades an engineering cost against a strategic/defensive judgment only he holds.

**Option E — Full four-repo decomposition.** Consequences: the §4.2 cost in full for the §4.3.1/4.3.4 benefits. The measured coupling — especially the dense, load-bearing 01↔03 seam (§1.4, §2.4) — argues this is disproportionately costly. The evidence does not support it as attractive; included for completeness.

---

## 6. Decisions genuinely blocked on Joseph

1. **The whole question is his** — the framing explicitly says gather-and-frame, do-not-decide. The monolith-vs-multi-repo call rests on strategic judgment (publication timing, ELI exposure posture, how much he values atomic refactor) that no agent holds.
2. **Specifically the Option-D sensitivity/exposure trade** — whether isolating `04-eli-core` for defensive-decoupling outweighs its 189-reference coupling cost. This is the one decomposition option with a real, distinct driver, and it is a strategic-exposure call, not an engineering one.
3. **Whether the packaging cleanup (Option B) should proceed regardless** — this is decoupled from the decomposition question and is probably a quick yes, but touching `ref/`/`_obs/`/`mono/` is a repo-shape change worth one confirmation.

---

## 7. Out-of-scope surfacings (passed back, not discarded)

- **The size illusion is itself a meta-process signal.** `mono/` (116M of build artifacts) is largely un-gitignored (only `.build/` is ignored); `_obs/` is 162M of obsolete archive in the live tree; `ref/` is 135M of external PDFs tracked in git. This inflates every clone and every agent's `du`, and is very likely what makes the repo *feel* like it needs decomposition. Belongs to cluster 05 (build/artifact hygiene) and cluster 08 (tracker/msc hygiene) but surfaced here because it directly distorts the decomposition question. **Cheapest high-value cleanup in this whole slice.**
- **`ref/` as a git-tracked 135M of external prior-art PDFs** interacts with the `INTEGRATION-CLEANUP-TODO.md` G2/G3 "ref/ as source-of-truth contradicts prior-art-integration discipline" reconsideration (noted in CLAUDE.md's active-reconsideration banner). Whoever resolves that should also decide whether `ref/` belongs in the git tree at all — a submodule or external store would both fix the size and clarify the "scaffolds are not segment-citable" boundary.
- **The `01-aad-core` name still appears 125× in recent commit *paths*** (git log --name-only over 500 commits) — historical, from before the 2026-05-15 rename; not a live path, but confirms the rename's archaeological footprint for anyone auditing path history.
- **Cluster 06 (cross-project census) should cross-check §2.1** — I characterized the sibling paper repos as build-independent from tracking-doc evidence only; cluster 06 has the full territory and should confirm whether any manuscript build *actually* reaches into agentic-systems (I found none, but I sampled).

---

## 8. Candidate meta-process definitions (raw material for the MECE map)

**MP-10.1 — Derived-artifact extraction (de-facto, healthy).**
- *Trigger:* a result/experiment/sim matures to where it warrants its own publication or codebase.
- *Steps:* create sibling repo → move/author self-contained dossier → reference framework as anonymized formal ground in the manuscript → keep agentic-systems links in tracking docs only → (optionally) add a two-file bridge (`doc/X.md` ↔ `X/ASF.md`).
- *Health:* **healthy and proven** — 8 sibling repos, clean synthese-from-ops precedent, build-independence verified.

**MP-10.2 — Atomic framework-wide refactor (de-facto, healthy, cohesion-dependent).**
- *Trigger:* a rename, slug realignment, or terminology change that must stay consistent across all four volumes + tooling + trackers.
- *Steps:* staged sweep (source → tooling → terminology → docs → regenerate) in coordinated commits within one repo.
- *Health:* **healthy, and the primary thing decomposition would break.** Exercised at scale (AAD→AAT, GUC renumber, slug alignment).

**MP-10.3 — Theory-core cohesion maintenance (de-facto, implicit).**
- *Trigger:* new theory content; cross-volume reference; new term.
- *Steps:* one slug namespace (235 slugs), one lexicon (`bin/term`), one findings/notation/format layer, cross-volume refs via slugs + relative links.
- *Health:* **functioning but with the packaging illusion (§0) obscuring it** — the cohesion works; the repo *weight* makes it look bloated.

**MP-10.4 — Repo-shape governance (aspirational / absent).**
- *Trigger:* the recurring "should this decompose" question (this cluster).
- *Steps:* none currently — there is no stated policy distinguishing "derived artifact → own repo" (running) from "theory volume → own repo" (never done). MP-10.1 runs by habit, not by written rule.
- *Health:* **aspirational** — making MP-10.1's boundary an explicit policy (Option C) would answer most of the felt tension without any migration. This is the low-cost formalization the evidence points at.

---

*End of findings. Measured mechanically; math not audited; framing offered, decision reserved for Joseph.*
