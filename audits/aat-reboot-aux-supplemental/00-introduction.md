# aat-reboot aux supplemental — 00 `INTRODUCTION.md`

*Written 2026-09-25 by the first finder (Claude Opus 5.5) for the aat-reboot walkthrough (`~/src/aat-reboot/`). This file keeps everything the coordinator's slim aux (`~/src/aat-reboot/scratch/aux/00-introduction.md`) left out: history, provenance, process feedback, incidental asf issues, and the full pilot report. It's meant for later careful review, and for later finders to surface whatever bears on their own segment. It's untracked by design; Joseph reviews these files.*

## Fact-checks with positive results — please add to the Working Notes of `01-aat-core/INTRODUCTION.md`

These are claims in the introduction that I checked against canon or sources and found to hold. Per Joseph (2026-09-25), passed checks belong here. The failed checks moved to the aux's `## FINDER-OBSERVED` section.

- **Hafez et al. 2026 (:35)** does support "a closely related diagnostic". Reliability requires measuring the coupling of the whole observation–action–outcome loop (`~/.local/share/relata/markdown/hafez-2026-mathematical/content.md:13,15–22,273–286`).
- **The Miehling paraphrase (:35) is faithful.** The source (`ref/arXiv-2503.00237v1/agentic_systems_theory.tex:142,205`) says "underestimation"; the introduction says "misjudges".
- **"A sustained cost paid in information" (:46)** is `#deriv-persistence-cost` (conditional), which fits "theorems and scope conditions".
- **"Acyclicity of strategy graphs forced by temporal ordering" (:54)** is consistent with `#def-strategy-dag`. That segment's own caveat, "sufficiency, not yet necessity", is about the DAG form in general, not acyclicity.
- **The containment dichotomy (:27) is right as a theorem.** Only its wording needs the support qualifier, which is lxiii, in the aux.

## Tagged notes for later segments

Later finders: `grep` this directory for your slug. Each note gives its tags, then the note, then where the evidence is.

- `[deriv-sector-condition, result-persistence-condition, result-sector-condition-stability, NOTATION GA-2S]` Audit 731548 ledger item **lxiii** was never executed and never reached the FINAL or any tracker. GA-2S as stated ("zero-mean, finite second moment") does three inequivalent jobs:
  - Prop A.1S's proof needs white noise.
  - Cor A.1S.1's exit half needs non-degenerate unbounded-support forcing.
  - A bounded, zero-mean, white disturbance satisfies GA-2 and GA-2S alike, and gets containment.

  The auditor's fix: tighten GA-2S, and add one clause each in the Findings Brief ("gusts with no absolute size limit") and in the introduction. Evidence: `audits/AUDIT-WORKING-731548/25-deriv-sector-condition.md:10,24,28`; `NOTATION.md:260`.
- `[deriv-sector-condition, result-structural-adaptation-necessity, scope-agent-identity, 04-eli-core]` Unstated corollary gold on the containment dichotomy. It forces "grow, transform, or eventually fail". Long-lived identity must be a *return* property, not a *containment* property ("fortress models" are ruled out). Evidence: `audits/AUDIT-WORKING-731548/01-INTRODUCTION.md:37`, `25-deriv-sector-condition.md:32`. That file uses the retired "Three Deaths" name.
- `[result-persistence-condition, result-sector-condition-stability]` B-1's register-site fix list (`CHANGELOG.md:223`) covered three segments. It missed `01-aat-core/INTRODUCTION.md:26` ("loses bounded behavior"), and possibly other front surfaces (README partial, Part I figure caption "Persistence fails exactly when…"). Worth a pickaxe for "fails exactly" / "loses bounded" / "grows without".
- `[result-certificate-existence, disc-stability-certificate]` The introduction's anchor 3 drops "at the linearized level" from the target's own summary.
- `[def-agent-environment, scope-agency, scope-adaptive-system, LEXICON agentic-system]` There are three senses of "agent": INTRODUCTION ¶1 requires acting; the umbrella since SP-24 includes passive observers; and the capitalized "Agent" is earned at the actuated lift. Separately, the `LEXICON.md:20` *Agentic system* entry ("+ outcome model + goal-directed action + model adaptation") disagrees with `#scope-agency`'s causal-contrast definition. It was flagged "[OPEN] … do not unilaterally rewrite" at `msc/scope-of-work-ontology-and-figure-2026-05-17.md:168–179`, and is still open. Miehling's functional agency excludes thermostats (`ref/arXiv-2503.00237v1/agentic_systems_theory.tex:380`), while AAT's adaptive scope includes them.
- `[scope-adaptive-system, def-agent-environment]` Joseph's 2026-05-17 plan: "Part 1's Introduction can pull back from [the agent definition] and explain why we're starting with a wider more general class". The Part I introduction is still the two-sentence stub he flagged at `01-aat-core/OUTLINE.md:9`. Also the lossy-not-blind boundary lesson (`~/.claude/projects/-Users-josephwecker-v2-src-arch-asf/memory/feedback_lossy_boundary_not_blindness.md`), and the proposed "both ends of the information axis" aside at `spikes/spike-escape-standpoint-axis-2026-07-29.md:139`.
- `[disc-ciy-unified-objective, deriv-causal-ib-lmi]` The three-restriction EFE recovery is claimed on front surfaces (INTRODUCTION:50, `HISTORICAL-CONTEXT.md:62`, `doc/readme/src/_position-and-lineage.md:18`) but housed only in `spikes/.integrated/spike-fep-suboptimal-approximation.md:57` ("Candidate Hypothesis"). Canon (`disc-ciy-unified-objective.md:66`) states a weaker shape-level isomorphism. That spike's :67 still suggests "a small discussion addendum … noting that EFE-like objectives are recovered under specific restrictions". A candidate landing, never done.
- `[Part I figure driver-snow-foundation, persistence-and-limits-intro, all chapter intros]` The driver-in-snow is promised as recurring (INTRODUCTION:60; OUTLINE:13 caption "recurring across Part I and beyond") but appears in zero `src/` segments. The provisional threading is at `spikes/visual/car-as-agent.md`; the open decision is at `spikes/visual/TODO.md:7`.
- `[der-directed-separation, der-class-coercion-via-wrapping]` Anchor 4's sentence ("a *necessary* structural property whose distinct extreme modes…") was judged muddled by 731548 (`01-INTRODUCTION.md:21`). It dates to `0ffd77f7`; the earlier draft said "discrete, not tunable".
- `[def-agent-spectrum, agent-spectrum.svg]` `01-aat-core/src/img/agent-spectrum.svg` still says "Blind Pursuer" (renamed "blind seeker" 2026-05-17, `6b0362f8`) and "SECTION I / SECTION II".
- `[persistence-and-limits-intro, result-persistence-condition]` Ledger S35 (open): modeler-perspective vs agent-perspective. Persistence is a *survival* condition, not an optimality condition; never stated framework-wide (`audits/polish-and-sentiment-ledger.md:70`).
- `[adaptive cycle, prolepsis…praxis]` The five-phase Greek cycle appears once in the whole Vol-1 reader snapshot. `adaptive-cycle.svg` is unembedded, and `TODO.md:105` records the keep-Greek-with-English-anchor decision.
- `[disc-stability-certificate]` The old volume preface's "Reading AAT — mental model first" (measuring-stick) paragraph was deleted 2026-05-17 (`feccd0d2`; predecessor at `git show 794994bf:01-aat-core/OUTLINE.md`). asf's `doc/sop/agents.sop.md` still cites it as the worked example of respectful pedagogy. That pointer is stale.

## Process and tooling notes (not segment-specific)

- **Miehling et al. 2025** is missing from relata and from every `mono/*.bib`. `relata candidates` can't find it via Crossref.
- **relata `hafez-2026-mathematical`:** the author field disagrees with the paper's masthead ("Chenan Wei", "Rodrigo Pena", "Amir Nazeri").
- **`spikes/visual/catalog-ideation.md:94`** (Tier 5, "scope lattice as a Venn / inclusion picture") is contradicted by Figure 1's reception (`msc/aat-v0.4.0-pdf-review.md:27,120`).
- **`spikes/epistemic-target-ontology/03-comprehension-lift-scout.md` §2.5** says the figures don't render. They have since 2026-05-18.
- **Auditor priming path:** `HISTORICAL-CONTEXT.md` is on the de-novo AVOID list (`doc/de-novo-audit-instructions.md:170`), but INTRODUCTION.md is a reordered HISTORICAL-CONTEXT that every auditor reads first.
- **`TODO.md:424`** (preface-claim substantiation) predates INTRODUCTION.md's move into its own file, so the introduction may be on no checklist. `TODO.md:521` (the legacy quantifier sweep) targets exactly the words its anchors use.
- **aspectus:** running it with `ASPECTUS_COLUMNS_HEAT=off` (as the global CLAUDE.md prescribes) prints "columns.heat accepted for this release; membership is now [layout]". I didn't write to its inbox; my brief limited writes at the time.
- **Front surfaces disagree on the volume's headline results:**
  - INTRODUCTION's four anchors;
  - the README partial's four;
  - ledger S9's external consensus (the diagnostic split, acyclicity);
  - the scout's proposed fifth anchor (loop as Level-2 engine);
  - the Part II preface's "16/24".
- **Front matter has no staleness mechanism:** no slug, no `depends:`, and it's outside the generators. If the reboot's introduction cited its anchors by slug, even invisibly, a `refresh-all --check`-style check could flag drift.
- **Finder-role feedback** (the parallelization answer; "unintegrated" means not reflected *in this segment*; fence finder verdicts away from the reader) is in the full report below, §12.

---

# The full pilot report (moved here verbatim from the coordinator's aux on 2026-09-25)

# Aux 00 — `01-aat-core/INTRODUCTION.md` (Volume 1 introduction)

*Finder report, 2026-09-25. Everything under `~/src/arch/asf/` was treated as read-only. Paths below are relative to `~/src/arch/asf/` unless absolute. Line numbers are as of asf `875e1ac3`. I read your cold read (`scratch/00-introduction-cold-read.md`) and `PROCESS.md` after most of the digging was done, and §0 maps what I found onto your "to verify" items.*

*How this is laid out: §0 is the short version. §1–§9 are facts and pointers by category, with extracts. §10 holds soundness notes on the introduction's forward references. Those notes necessarily quote a phrase or two from later segments, so skip §10 if you would rather meet that material cold. §11 is what I looked at that turned up nothing. §12 is feedback, including the parallel-finders question.*

---

## Aux list (the terse form Joseph expects most reports to take)

- **Appendix it relies on:**
  - `01-aat-core/src/deriv-sector-condition.md` (anchors 1–2)
  - `01-aat-core/src/deriv-stochastic-non-exit.md` (anchor 2)
  - `01-aat-core/src/result-certificate-existence.md` (anchor 3)
  - `01-aat-core/src/deriv-persistence-cost.md` (the information-cost fact)
  - `01-aat-core/src/deriv-self-actuation-grounding.md` (self-set objectives)
  - These are forward references. Don't read them now. See §3 and §10.
- **Auditor gold:**
  - `audits/AUDIT-WORKING-731548/01-INTRODUCTION.md` (whole, 41 lines), with its follow-up at `audits/AUDIT-WORKING-731548/25-deriv-sector-condition.md:10,28,32`
  - `audits/AUDIT-WORKING-374162/01-batch-ch1-foundations-quiz-questions.md:47–64`, with answers at `…-quiz-answers.md:45–61`
  - source gold already lifted: `audits/AUDIT-WORKING-193847/.integrated/{22,25,26}-*.md`
- **Unintegrated finding:** 731548 ledger item lxiii (anchor 2 needs "unbounded-support"), never carried forward. The introduction is also stale after B-1 (`CHANGELOG.md:223`) and SP-24 (`CHANGELOG.md:386–392`).
- **Spikes:**
  - `spikes/epistemic-target-ontology/03-comprehension-lift-scout.md` (about this file)
  - `spikes/spike-escape-standpoint-axis-2026-07-29.md:127–140`
  - `spikes/.integrated/spike-fep-suboptimal-approximation.md:29–68`, the source of an introduction claim that canon doesn't hold
- **CHANGELOG:** no dedicated entry. See `CHANGELOG.md:69,110,215–231,386–392`.
- **Git messages:** the bodies of `6f830bc8`, `0ffd77f7`, `5e74eced` and `feccd0d2`. The design intent is in §2.1.
- **Joseph's words:** `~/.claude/history.jsonl` lines 13040–13194 (2026-05-17/18). See §2.2.
- **External refs:**
  - Miehling 2025: not in relata; use `ref/arXiv-2503.00237v1/agentic_systems_theory.tex:142,205,336–346,380`
  - `hafez-2026-mathematical`: relata markdown lines 13–22, 148–153, 273–286
- **img:**
  - `scope-of-work.{tex,pdf}` is Figure 1, with design trail `msc/scope-of-work-ontology-and-figure-2026-05-17.md`
  - `agent-spectrum.svg` and `adaptive-cycle.svg` are related but not embedded
- **Also:** `msc/summary-attempt/001-introduction.md`, Joseph's earlier plain-English walk of the whole volume.

This file is the outlier Joseph expected. The rest of this report is the long form.

---

## 0. The short version

**Your three "to verify" items, answered:**

1. **The "objective without *enough*" fact is in Volume 4, at discussion grade.** Its home is `04-eli-core/src/der-bounded-objective-as-sanity-criterion.md` (`status: discussion-grade`, `stage: draft`). The introduction groups it with two other "structural facts" and says "Stated as physics, these are theorems and scope conditions" (INTRODUCTION.md:46). For this one, that tier is higher than its home supports.
2. **Canon does not contain the "active inference recoverable under three explicit restrictions" claim.** No segment in any volume states it (grepped for the survival Lagrangian, EFE, and "three … restrictions"). It comes from `spikes/.integrated/spike-fep-suboptimal-approximation.md:57`, where it is labelled a **"Candidate Hypothesis"**, and the spike's own recommendation (:67) is "Do not promote as a 'dominance theorem'". What actually landed in canon, `01-aat-core/src/disc-ciy-unified-objective.md:66` (`discussion-grade`), is weaker and different: "structurally isomorphic … at the shared-shape level … not unified content", plus two stated differences. The introduction (INTRODUCTION.md:50), `HISTORICAL-CONTEXT.md:62` and the README partial (`doc/readme/src/_position-and-lineage.md:18`) all state the stronger version. HISTORICAL-CONTEXT itself calls it "candidate-formulation grade" in the same paragraph. In strengthen-first terms there are two honest routes: land the three-restriction mapping in canon at its true tier (the spike's §3–4 has the construction), or restate the introduction to match what canon holds.
3. **"Part I is mathematically closed" is contested, and it was never re-examined after the audit most likely to test it.** Audit 384279 (2026-05-27) said Part I was cleaner than predicted, "consistent with Part I being labeled 'mathematically closed'" (`audits/audit-384279-FINAL-2026-05-27.md:54`). The later audit 731548 (Fable, 2026-07-02) flagged the phrase at its first reflection and never closed the loop in its FINAL. It did find three real, open defects inside Part I: B-1 (the persistence "iff"), B-2 (a regression in the mismatch decomposition), and B-3 (the adaptive-scope exclusion rationale is false for standard RL; still open as PROPOSALS SP-30). The first two have since landed; B-3 has not.

**Other things I'd put near the top:**

4. **The introduction hasn't been touched since three findings about its own claims landed or opened.** Its body was last edited 2026-05-18. Since then:
   - (a) The persistence "only-if" was shown false in general (B-1, landed 2026-07-03). Anchor 1 still says that below the threshold a system "loses bounded behavior" (INTRODUCTION.md:26).
   - (b) Audit 731548 recorded that anchor 2's "genuinely stochastic" needs an *unbounded-support* qualifier (ledger item lxiii). That never reached its FINAL or any tracker, and NOTATION's GA-2S is unchanged.
   - (c) SP-24 (2026-05-28) redefined the root "agent" as an umbrella term that includes passive observers. The introduction's first sentence defines an agent as something that *acts*.

   None of these is a mistake at the time of writing. They are drift, the pattern `TODO.md:521` (the "legacy quantifier sweep") and `TODO.md:424` (Joseph: "We shouldn't make any claims in prefaces or intro discussions that aren't substantiated or first claimed in an actual claim (segment)") exist to catch.
5. **The driver-in-snow promise is not kept.** The introduction says the example "recurs across the chapters as a worked anchor" (INTRODUCTION.md:60). Zero segment files in `01-aat-core/src/` mention snow, windshields, wipers or the driver. The example exists only as the Part I figure and its caption (`01-aat-core/OUTLINE.md:12–13`). Whether to thread it was an open `[Joseph]` decision in the visual spike (`spikes/visual/TODO.md:7`), with a provisional per-chapter mapping in `spikes/visual/car-as-agent.md`. Your hunch to open with the snow driver would be the first time it does the work the introduction says it does.
6. **"None of it is new mathematics" predates Joseph's correction of that register.** The introduction was drafted 2026-05-17, inside the "de-flinch" push. The 2026-05-16 plan's "armor" rule was *keep "no new mathematical machinery, no new foundations"* (`TODO-big-picture.md:33`). Four days later, on 2026-05-21, Joseph added the math-novelty guidance now in asf's `CLAUDE.md`: "In our case we even **are** inventing new tools and methodologies, and even some novel mathematical notation." So your snag at cold-read line 30 is a real tension between two dated layers of guidance, and the introduction sits on the older one.
7. **Joseph's own design intent for this file is on record, verbatim** (§2.2). The key lines: it's for "peers reading a theory in an academic preprint archive", not students. "Don't lean too far into the pedagogy." The tone target is "an alternation between A Theory of Communication and Shannon giving presentations". "The trick will be doing it *without being patronizing and without apologizing*." And he framed the first sentence as defining *an agent*, with Part I's introduction meant to "pull back … to a wider more general class". That Part I introduction was never written. It's still the two-sentence stub he flagged. This bears directly on the reboot, because your pedagogy aims and his stated register for *this* file pull in different directions. That tension is worth raising with him explicitly.
8. **A predecessor of what you're doing exists:** `msc/summary-attempt/` (Joseph, 2026-05-20). It's a 145-segment plain-English walk of all of `01-aat-core` in outline order, plus notes (`000-supplement-notes.md`), with an interleaved appendix-on-first-reference symlink scheme. `001-introduction.md` (13 lines) is its rendering of this file. It's worth knowing about before the reboot reinvents it, and worth diffing against later: it's a four-month-old snapshot.
9. **The one external citation the introduction names, Miehling et al. 2025, is in neither relata nor the built bibliography.** `relata search` finds nothing (and `relata candidates` can't find it via Crossref). The v0.4.0 PDF review flagged its absence from the bibliography (`msc/aat-v0.4.0-pdf-review.md:87,165`). `grep` over `mono/*.bib` confirms it's still absent. The paper's LaTeX source is local at `ref/arXiv-2503.00237v1/agentic_systems_theory.tex` (line ranges in §6).

---

## 1. The segment itself

- **What it is.** Front matter, not a FORMAT segment: no frontmatter, no `depends:`, no status or stage. It lives at component root (`01-aat-core/INTRODUCTION.md`, 68 lines) and is transcluded by `01-aat-core/OUTLINE.md:4` (`![[INTRODUCTION]]`) under `## *Introduction*: Inescapable Foundations of Agency`. The section title is marked provisional in its own header comment (lines 3–8) and in WN (1).
- **Map of the file:**
  - voice contract (HTML comment): 10–19
  - thesis paragraph: 22
  - four anchors: 26–29
  - contribution paragraph: 31
  - "A need the field has named": 35
  - "The architecture of the theory": 39, 41
  - figure: 43–44
  - moral terminus: 46
  - "Where it sits": 50
  - "How the work developed": 54
  - "What this volume is": 58, 60, 62
  - Working Notes: 64–68
- **How it renders.** The build strips the HTML comment, the file's own heading and the Working Notes in every variant (`bin/lib/ingest.rb`, commit `feccd0d2`). The rendered form is `CURRENT-VOL1.md:3–46` (reader snapshot) and Figure 1 of the PDF. Two build-level notes from `msc/aat-v0.4.0-assembled-md-review.md`:
  - The introduction's `###` subsections sit at the same heading level as `### *Chapter*`, so a naive ToC interleaves them (:118).
  - `#fig-scope-of-work` never entered the label map, so later raw citations of it stay raw (:83). It's still raw at `CURRENT-VOL1.md:101`.
- **Working Notes worth your eyes (64–68).** WN (1) Provenance names the four source documents and says the "expansive register" of two sections was integrated from Gemini auditor gold. WN (5) says paragraphs 1–2 carry Joseph's own in-vivo voice. The voice-audit note (68) says: "If a future editor finds a hedge that is defensive rather than scope-accurate, it is debris from an earlier register and should be cut."

## 2. History: git, commit bodies, and Joseph's words

### 2.1 Timeline (commit bodies read in full)

- **2026-03-09 — the repo is founded, and Miehling is read the same day.**
  - `523f4e76` "Initial commit: ACT (Agentic Cycle Theory) founding documents".
  - Then `cbd07c9b` "Add prior art assessment: Hafez (2026), IBM systems theory, FAST workshop". Now at `.archive/02-prior-art-assessment.md`: §2 at :68, the "IBM → AAD manifesto mapping" at :209–225, and :176 "Cite IBM as articulating the need. Their position paper calls for what AAD provides."
  - Only *then* `0b21226e` "Add first sketch of G_t formalism". So TFT (first commit 2026-02-27) and the TST corpus (since Aug 2025) predate the reading, but the actuation half ($G_t$, strategy) was sketched hours after it.
  - The introduction's "had built the formal apparatus before the call was encountered" (INTRODUCTION.md:35) is true of the adaptive half, not of AAT as a whole. Audit 731548 flagged this as checkable from git (`audits/AUDIT-WORKING-731548/01-INTRODUCTION.md:23`); this is the check.
  - Memorata has a Joseph-pasted source list containing the arXiv link on 2026-03-13 (`~/.claude.bak.2026-03-13/projects/-Users-josephwecker-v2-tmp/d7dc4c90-….jsonl`, line 1042).
- **2026-04-26 `cbb1b32b`** — `HISTORICAL-CONTEXT.md` and the README "Position & Lineage" partial land. The body notes the partial "front-loads the operational diagnostics … and the precise active-inference differentiation (FEP recoverable from ASF's survival Lagrangian under three explicit restrictions)". This is where the active-inference claim first entered a front surface. It came from the then-fresh spike, not from canon.
- **2026-05-16 `6653de67`** (W4) — README de-flinch. "The field-facing Position & Lineage sentence framed the distinctive contribution as the methodology/process-hygiene flinch … Restated … the contribution is what the integration makes provable." Context: `TODO-big-picture.md` (whole file, 64 lines), especially the "Converged cleanup principle (Joseph, 2026-05-16)" at :12.
- **2026-05-17 03:16 `625307cb`** — HISTORICAL-CONTEXT de-flinched "surgically … the full reorder/voice-lift of this doc is the deliberate intro work, separate."
- **2026-05-17 03:16 `6f830bc8`** — first draft, "for adjudication". Body: "Expansive, peer-facing … no math-apology, no conceit, no methodology-as-contribution flinch, peer not student … First-encounter phenomenology from the de-novo Gemini audit journal … *integrated as the introduction's own seeing*, not block-quoted, per Joseph's instruction."
- **2026-05-17 03:48 `0ffd77f7`** — voice-lift to measured "we"; "Named the bracketed item-3 'Stability Equivalence' … removing the slogan/vibe framing"; the tic words purged. This commit also carries Joseph's in-vivo paragraph edits. The anchor-4 wording changed here, from "a *discrete* structural property, not a tunable one" to "a *necessary* structural property whose distinct extreme modes critically determine…". Audit 731548 later called this the one muddled anchor sentence (§4.1). From the WN(5) attribution it is *probably* Joseph's own hand, but I did not confirm that.
- **2026-05-17 04:13 `5e74eced`** — ¶1 lands as "Joseph's merged S2 + the S3 rewrite". Body: "the 'common to all agents' overclaim replaced by the cascade thesis … 'temporal feedback system' kept (it is a description — temporality as constitutive of agency — not the retired TFT name; the audit's currency flag was wrong)… S1 unchanged: the volume intro defines 'an agent'; Part I's own Introduction is the correct home for the pull-back to the wider adaptive-system class."
- **2026-05-17 04:44 `feccd0d2`** — wired into OUTLINE. The body says the new file replaced "the annotated old intro block (the paragraphs Joseph marked 'remove' + the dep-graph image)", and that "Part I's `### *Introduction*` placeholder is wired … but its content remains the deferred Part-intro work."
  - **The predecessor text** (the old `## *Preface*`) is at `git show 794994bf:01-aat-core/OUTLINE.md`, lines 1–~20. It contained "Reading AAT — the mental model first" (the *measuring-stick / stability-certificate* Layer-0), "Reading AAT — the precise structure" and "On mathematical precision".
  - Those paragraphs are gone from the OUTLINE now. See §9 for the stale pointer this left in asf's `CLAUDE.md`.
- **2026-05-17 `6b0362f8`** — adds `msc/scope-of-work-ontology-and-figure-2026-05-17.md` (the figure's design and verification trail, §7).
- **2026-05-18** — the figure itself:
  - `67955a76`: "The C+A nested-containment variant is the chosen direction"; drafts -A/-B/-C removed from msc. They're recoverable from `67955a76^`.
  - `0737fb27`: parameterized.
  - `0860585b`: rail colours unified "Per Joseph".
  - `e84c4fd7` inlines the figure; its body cuts "the now-false '(The figure is planned; agent-spectrum is its nearest relative...)' parenthetical".
  - `7cfea652` adopts the caption convention.
  - `36879bde`: general figure-embed pipeline.
- **2026-08-22 `597a4e50`** — Working Notes only: "INTRODUCTION.md's Working Notes still said the transclusion and figure pipeline were unwired." No body edit since 2026-05-18.

### 2.2 Joseph's own words while this was being made

All from memorata, `~/.claude/history.jsonl`, 2026-05-17/18 (`memorata-search --joseph --since 2026-05-16 --until 2026-05-19 introduction`):

- 02:23 (line 13040): "I have a very different opinion on the current state of the introduction. I went ahead and edited AAT's OUTLINE prefaces, gave them example new section titles ('Introduction ...' instead of preface), and put my notes on what tiny bit there is there in html comments above each paragraph". Only the Part I annotations survived into git (`01-aat-core/OUTLINE.md:9,15`). The volume-preface ones were deleted with the block in `feccd0d2`.
- 02:42 (13041): "…it is the pondering of these more principled approaches that made the measuring-stick look so useless to me on reread… a lot of these first principles are going to apply to the introduction of the work as a whole, and the voice in the introductions of volumes, parts, and chapters in particular. The trick will be doing it *without being patronizing and without apologizing*. The *tone* I keep thinking of would be similar to an alternation between A Theory of Communication and Shannon giving presentations on his paper/monograph..."
- 02:59 (13045): "Don't lean to far into the pedagogy. Most of those findings, while principled, were geared toward those who are 'there to be taught' -- students -- not peers reading a theory in an academic preprint archive. I feel like the driver in the snow will be very useful as a concrete application that sits in chapter introductions. What we're talking about here is something much more expansive in vision and much less detailed about AAT mechanics or mathematics." (He then points to HISTORICAL-CONTEXT, LEXICON, `_lexicon-full-archive.md`, and `doc/DOMAINS.md` "later in the intro so it doesn't weaken the central positioning".)
- 03:08 (13046): "…One important diagram that I think will be critical at some point in the introduction will be the scope narrowings and how each one opens up a more sophisticated type of agency- reinforcing our approach generally and our mathematical position..."
- 04:11 (13055), on ¶1: "It defines an agent, not an adaptive system. Part 1's Introduction can pull back from that and explain why we're starting with a wider more general class… I was literally describing agency as needing a temporal component, instead of *restating* it is 'adaptive.'" He then gives the merged sentence now at line 22.
- 20:42 (13074): he wants a **"Scope of work" *section*** centred on one figure, "a visualization and 'map' of the systems that ASF will cover in general and AAT in particular". He mentions a stepped pyramid or a Sankey, "but it will be difficult to get into some of the critical orthogonal dimensions". As built, there is no "Scope of work" heading; the figure sits inside "The architecture of the theory".
- 2026-05-18 02:04 (13194): place the figure and add "<!-- TODO: Get this to pull into the monograph! -->".
- **The same day, a boundary correction by hand.** Joseph spent about half an hour correcting ¶1 away from "a world it cannot see directly" and toward "can only ever see in part". The recorded lesson is `~/.claude/projects/-Users-josephwecker-v2-src-arch-asf/memory/feedback_lossy_boundary_not_blindness.md`: the boundary is lossy/partial/residual, never blind/void, and the "blindness" misreading *inverts* the theory. The misreading entered through paraphrase that dropped "*directly*" and through uncritical import of auditor poetry ("geometry of isolation"). `spikes/spike-escape-standpoint-axis-2026-07-29.md:131–135` counts four recurrences since, all in the inverting direction, and proposes a canon-side aside (§5).
- **Later, to the Fable auditor (2026-07-02)** (`~/.claude/projects/-Users-josephwecker-v2-src-agentic-systems/1d2083e2-….jsonl`, line 359): "Introductions are allowed to be forward looking and not 'bury the lede' -- but watch for coherence, global correctness, and credibility".

### 2.3 Source documents the introduction was composed from (per WN 1)

- `HISTORICAL-CONTEXT.md` (94 lines; the spine). The introduction reorders it.
  - Compare INTRODUCTION.md:35 with :29–33 (Miehling).
  - Compare INTRODUCTION.md:50 with :37–84 (arc and peers; EFE at :62, "candidate-formulation grade").
  - Compare INTRODUCTION.md:54 with :88–94 (development).
  - HISTORICAL-CONTEXT carries **dates** the introduction dropped: TST since Aug 2025, TFT, repo March 2026, renames.
  - Note: `doc/de-novo-audit-instructions.md:170` puts HISTORICAL-CONTEXT on the auditor **AVOID** list as priming-heavy, yet its content now opens the volume every auditor reads first. See §9.
- `doc/readme/src/_position-and-lineage.md:10–20`. It names a **different set of headline results** from the introduction: persistence, the satisfaction-gap/control-regret split, loop-as-Level-2, software as calibration lab. The introduction's set is persistence, containment, equivalence, classification.
- `doc/readme/src/_lexicon-full-archive.md` (357 lines; the logos → logogenic → logozoetic cascade, :196–250; continuity stances :320–357).
- `doc/DOMAINS.md` (119 lines; breadth, "deliberately referenced not led-with"). The 2026-05-17 design doc calls it one half of a *pending* 2026-05-04 proposal pair, not independent corroboration (`msc/scope-of-work-ontology-and-figure-2026-05-17.md:27–39`).

## 3. Appendix segments the introduction leans on

The introduction has no `depends:`. Taking "relies on" as "an anchor's warrant lives there", these are the ones that are **appendices** (Appendix A, `01-aat-core/OUTLINE.md` §"Appendices Details" from :330):

| Anchor or claim in the intro | Appendix home | OUTLINE line | status / stage |
|---|---|---|---|
| Anchor 1, Persistence Threshold (proof side) | `#deriv-sector-condition` | 339 | exact / claims-verified |
| Anchor 2, Containment Dichotomy | `#deriv-sector-condition` (Cor A.1S.1) + `#deriv-stochastic-non-exit` | 339, 340 | exact / claims-verified; exact / draft |
| Anchor 3, Stability Equivalence ("the framework's central anchoring identity") | `#result-certificate-existence` | 346 | exact / draft |
| "a sustained cost paid in information" (:46) | `#deriv-persistence-cost` | 347 | conditional / draft |
| self-set objectives, the fourth cascade step (:39) | `#deriv-self-actuation-grounding` | 341 | draft (spike verdict: conditional) |

So two of the four anchors, and the one the introduction says lets "every later structural question be posed as a question about one object", are proved in the back of the book. Main-body homes are in §10.

## 4. Auditor gold and audit findings about this file

The introduction exists only from 2026-05-17, so only audits after that date can be *about* it: 384279 (05-27), 773921 (05-28), 731548 (07-02), 374162 and 628417 (07-20). I grepped all 24 working dirs, both `.integrated/` trees, all FINALs and the ledger.

### 4.1 `audits/AUDIT-WORKING-731548/01-INTRODUCTION.md` (41 lines; Claude Fable 5; **unintegrated, under the standing Joseph gate**)

This is the only full reflection on this file. It's worth reading whole. The load-bearing parts:

- :5 **"Part I mathematically closed" flagged as a likely framing overclaim.** Deferred, and never resolved in the FINAL.
- :9–13 **The Model D / Model S overlap.** "genuinely stochastic" doesn't partition against "bounded", because a bounded, zero-mean, white disturbance satisfies both GA-2 and GA-2S as NOTATION states them.
  - Resolved at the derivation (`25-deriv-sector-condition.md:10`): the corollary selects by *support* (bounded vs unbounded), so "The theorem is right; the *label* … is doing three inequivalent jobs."
  - The propagation demand: "one clause in the Brief, one in the intro." The ledger item is (lxiii) at `25-deriv-sector-condition.md:28`, "[mine, high, small-medium severity]".
  - **Status: not executed.** It's not in the FINAL (`grep` for GA-2S / lxiii / "unbounded" = nothing), not in TODO, PROPOSALS, the ledger or JOSEPH-TODO. `NOTATION.md:260` GA-2S still reads "zero-mean with $\mathbb E[\lVert w(t)\rVert^2] = \sigma_w^2$", and INTRODUCTION.md:27 is unchanged.
  - This is the clearest *unintegrated* finding touching the file: a known, small fix that fell between the working ledger and the FINAL.
- :17 Watches: "exact" force leaking from the Lyapunov spine onto the interpretive identification of $R$ with model-class capacity; "identically the Lyapunov theorem" and converse-Lyapunov regularity conditions.
- :21 **"The fourth anchor bullet's first sentence is muddled"**: "a yes/no question isn't a property, and 'necessary' dangles (necessary *for* what?)". Not acted on.
- :23 The independent-convergence claim is checkable from git. See §2.1 for the result.
- :25 and :37 **Gold, a corollary nobody stated.** The containment dichotomy "is really a forcing argument for one of: unbounded growth, periodic re-architecture, or death… grow, transform, or eventually fail, pick one… more portable than the exit result itself." The sequel at `25-deriv-sector-condition.md:32`: "long-lived identity cannot be a containment property — it must be a *return* property… The mathematics quietly rules out one whole architecture for continuity (fortress models)…" The "Three Deaths" wording there is the retired name.
- :31 "The 'moral weight is a shell around the physics, not a term inside it' move is the single most disciplined sentence I've seen in a document of this kind".
- :35 A split register. Reader-facing prose bans "load-bearing", while internal documents use it densely, and future agents write segments in the internal register.
- :39 **A circularity to keep in mind for the reboot.** The introduction's register "was partly integrated from a prior auditor's first-encounter phenomenology… the artifact I'm auditing has prior audits *inside its bloodstream*… resonance is exactly the feeling I should distrust most here."

### 4.2 `audits/AUDIT-WORKING-374162/01-batch-ch1-foundations-*` (Fable, 2026-07-20; comprehension-quiz run; batch-1 files **unintegrated**)

- `…-reflections.md:23,27`: "'Scope conditions are the theorems' is the volume's thesis statement, not a disclaimer". It predicts the containment dichotomy "is the one most likely to be misquoted by summary-readers as 'stochastic systems eventually fail'".
- **Usable as a self-test after your reading:** `…-quiz-questions.md:47–64`, questions b01-3.1, 3.2, 3.6 (the rest of batch 1 is Ch.1 material, so skip). Answers are in `…-quiz-answers.md:45–61`.
  - The answer to 3.2 repeats "stochastic disturbance" without the support qualifier. It inherits the lxiii looseness.

### 4.3 Source gold, already lifted (`audits/AUDIT-WORKING-193847/.integrated/`, Gemini)

These are the passages the introduction's closing phenomenology was "integrated from", useful to see what was taken and what was checked:

- "moral weight is a shell surrounding the physics, not a variable within it": `26-def-agent-spectrum.md:47`.
- "infrastructure of souls" / restore-from-backup: `25-scope-agent-identity.md:45`.
- "sustained burn rate of Shannon information": `22-result-persistence-condition.md:43`.

The lossy-boundary memory (§2.2) records that this same journal's "geometry of isolation" poetry was a misconception source, so the gold was integrated with a canon check, and the introduction's version is the corrected one.

### 4.4 Other audits: brief mentions only

- 628417 (Grok, `00-initial-predictions.md:52`): "OUTLINE maturity gradient (Part I 'closed') may outrun remaining discrete/continuous seams".
- 384279: supportive on Part I (above).
- 773921: no reflection on the introduction.
- Ledger rows that bear on it:
  - `audits/polish-and-sentiment-ledger.md:45`, **S9** (sentiment, stable across external reads): "Section I is strongest; the lift into agency/composition is where rigor thins", plus the satisfaction-gap/control-regret split and acyclicity-from-temporal-ordering named "the most genuinely useful original formalization". That split is the phrase you called the best handle in the file, sitting in a history paragraph.
  - `:70`, **S35** (open research seed): "Modeler-perspective vs agent-perspective framing … the persistence condition a *survival* condition, not the *optimality* condition of modeler-perspective RL/ML… never as a framework-wide framing. Respectful-pedagogy candidate." That is a volume-front framing the introduction doesn't make.

### 4.5 Findings that landed elsewhere and now leave the introduction stale

See §0.4 and §10.

- **B-1:** FINAL at `audits/audit-731548-FINAL-2026-07-02.md:43–51`; landing record at `CHANGELOG.md:223`. Its register-site list covers three segments and not the introduction.
- **B-3 / SP-30:** FINAL :63–69, `PROPOSALS.md:389`.
- **SP-24:** `CHANGELOG.md:386–392`.
- **The routed-but-unexecuted legacy quantifier sweep:** `TODO.md:521`. It targets exactly `iff` / `only if` / `necessary` / `exactly`, all of which appear in the introduction's anchors.
- **The preface-claim-substantiation pass** (`TODO.md:424`): its per-OUTLINE checklist was written before the introduction moved into its own file, so the introduction may not be on anyone's list.

## 5. Spike results bearing on it

- **`spikes/epistemic-target-ontology/`** (ACTIVE WORKSHOP since 2026-07-04, no canon edits; INDEX :66–72).
  - `00-spike.md` §1–3 (:1–40) diagnoses the unhoused noun $\theta$ (law-content has no slot beside $\Omega_t$ and $\varepsilon_t$). The consequence is that the broadest scope's predicate misclassifies standard RL (audit B-3). The introduction's ¶1 ("an internal picture of an external world it can only ever see in part") and its broadest-scope gloss ("observation under residual uncertainty", :39) are the plain-language face of the predicate this spike proposes to retype as $H(S_t\mid\mathcal C_t) \gt 0$ with $S_t = (\Omega_t,\theta)$.
  - **`03-comprehension-lift-scout.md` is about this file** (98 lines). :9 calls INTRODUCTION.md "the strongest single framing artifact in the repo… Its main gap is an omission". :20: "The volume introduction is strong, and then the reader falls off a cliff." :34–37 propose adding **the loop as Level-2 causal engine** as a fifth anchor, plus one burn-rate sentence in anchor 1. :69 proposes two top-level mental models, the **ledger** (typed ignorance) and the **race** (persistence), presented as a pair. :73–74 give the recommendations.
  - Stale bit: :45 and §2.5 say the figures don't render. They have since 2026-05-18.
- **`spikes/spike-escape-standpoint-axis-2026-07-29.md` §9 (:127–140)** (EXPLORATORY). The provenance of Joseph's 2026-05-17 hand-correction of ¶1, the four-recurrence count, and a proposed "both ends of the information axis are out of scope, for mirror reasons" aside (draft wording at :139). §9 is superseded as to *which* adjudication Joseph meant (see its §10), but the introduction-specific history stands.
- **`spikes/.integrated/spike-fep-suboptimal-approximation.md`** (69 lines; "Exploratory research spike"; INDEX :336 "LANDED (scope-honored)"). The source of the three-restriction EFE mapping. §3 (:29–49) gives the three assumptions, :57 the "Candidate Hypothesis", :61–68 "Do not promote as a 'dominance theorem'… Wait for the causal-IB LMI work to settle before any formal integration." See §0.2 for what landed versus what the introduction says.
- **`spikes/spike-active-inference-vs-aad.md`**: the 28-mapping audit that HISTORICAL-CONTEXT:64 cites as backing "Where it sits". Not opened in depth.
- **Self-actuation** (INDEX :285). This bears on the cascade step "letting the agent set its own objectives". The verdict is a *conditional, scoped* no-go (`#deriv-self-actuation-grounding`, conditional). The figure draws Self-Actuated "as established (not hypothetical). This is Joseph's epistemic call" (`01-aat-core/src/img/scope-of-work.tex:52–55`).
- **`spikes/visual/`** (ACTIVE since 2026-05-15). See §7.

## 6. Papers

- **Miehling et al. 2025, "Agentic AI Needs a Systems Theory"** (ICML 2025 position paper, arXiv:2503.00237). **Not in relata** (see §0.9). Use the local source, `ref/arXiv-2503.00237v1/agentic_systems_theory.tex` (590 lines):
  - :142 abstract: "overly focused on individual model capabilities … leading to a significant underestimation in the true capabilities and associated risks". The introduction's paraphrase at :35 is "misjudges both what agents can do and how they fail".
  - :205 the position stated, with its examples: alignment faking, self-exfiltration, sandbagging.
  - :336–346 **Definition: functional agency**: action generation, outcome model, adaptation.
  - :380 **"Functional agency naturally excludes devices that cannot adapt to changes in the outcome model (e.g., a thermostat)."** Worth holding next to the introduction's "whether the agent that fails it is a thermostat" (:46), the Part I scope's "thermostats through commanders", and HISTORICAL-CONTEXT:33's claim that ASF "adopts the functional-agency three-condition characterization directly into the agent-class hierarchy". AAT's adaptive scope is deliberately broader than IBM's agency. The "answer to the call" framing never says so.
  - :396–406 agentic systems and the systems view; :442–495 mechanisms of emergence; :521–531 subgoal emergence (the prior-art assessment maps this to chain-confidence decay).
  - Older ops memory has the full author list: `~/.claude/projects/-Users-josephwecker-v2-src-ops/memory/reference_ibm_agentic_systems_theory_paper.md`. The global CLAUDE.md warns "Lead author is **Miehling**, NOT Agarwal".
- **Hafez et al. 2026, "A Mathematical Theory of Agency and Intelligence"** (arXiv:2602.22519). This is the "third line, information-theoretic measurement of agency" at INTRODUCTION.md:35. In relata as `hafez-2026-mathematical`. I triggered its conversion today, so relata's markdown is at `~/.local/share/relata/markdown/hafez-2026-mathematical/content.md` (581 lines):
  - :13 abstract: "predictions can appear successful while the underlying interaction with the environment degrades". The convergent diagnostic is the full loop's coupling versus task success.
  - :15–22 introduction ("three limitations persist … monitoring often isolates fragments rather than the full observation–action–outcome loop").
  - :148–153 §4.4 "Differentiation from Existing Frameworks".
  - :273–286 Discussion (agency versus intelligence; "current AI exhibits agency and learning, but not intelligence").
  - The "closely related diagnostic" wording in the introduction is fair.
  - Incidental: relata's author field ("Wei, Chen; Felipe, Rodrigo; Nazeri, Amirhossein") doesn't match the paper's masthead at :3–11 ("Chenan Wei", "Rodrigo Pena", "Amir Nazeri").
- **Active inference.** Canon's comparison and its citations are in `01-aat-core/src/disc-ciy-unified-objective.md:66`: Friston et al. 2017 (`friston-2017-active-process` in relata); Da Costa et al. 2020 (`costa-2020-active`, no PDF); Sajid et al. 2021; Sun & Firestone 2020, dark room (`cruys-friston-clark-2020-controlled-optimism` is the reply, in relata). Also possibly relevant, in relata: `koudahl-kouw-vries-2021-efe-collapse` ("On epistemics in expected free energy for linear Gaussian state space…"), which may bear on restriction (ii), the scalar epistemic price. I didn't open it.
- **The classical machinery the introduction names** (Lyapunov, Itô, Pearl, IB, monotone operators, Čencov): all in relata by the usual keys (for example `cencov-1982-stat-decision`, `lohmiller-1998-contraction`, many IB entries). The introduction only name-checks them, so I didn't pull line ranges. **Miller 2022** (`miller-2022-ex-machina`) is in relata. The PDF review wanted it in the bibliography too (`msc/aat-v0.4.0-pdf-review.md:165`).

## 7. Diagrams (`01-aat-core/src/img/` and around)

- **`scope-of-work.{tex,pdf}`** (Figure 1; embedded at INTRODUCTION.md:43–44). This is the only figure in the introduction.
  - *What it shows:* nested containment frames, Adaptive System $\supset$ Agentic System (+ causal intervention) $\supset$ Actuated Agent (+ explicit $O_t,\Sigma_t$) $\supset$ Self-Actuated Agent (+ revises own $O_t$). Each frame has a one-line "capability": "mismatch · gain · tempo · persistence" / "causal intervention" / "orient cascade" / "goal autonomy · negotiated continuity". Below a dotted divider, four orthogonal "rails" switch on at the tier where they become meaningful: Arity (Primitive | Composite) from Adaptive; Knowledge Type (Static | Learning) from Agentic; Continuity stance (five values) and Goal-Update Coupling (Separated | Partial | Coupled) from Actuated. The palette is sampled from the cover SVG.
  - *Design record:* the `.tex` header (:1–69) is a genuine design-rationale document ("Containment, not a pipeline… do not silently revert"). The full trail is `msc/scope-of-work-ontology-and-figure-2026-05-17.md` (237 lines). §2 there, "The spine is three coexisting *views*, not one ladder": nested formal scopes, the LEXICON narrowing chain, and the agent-spectrum 2×2. "A stepped pyramid … would actively misrepresent the theory". §5 is the capability/name walk table. §6(A) is the **open** Adaptive→Agentic boundary: three non-equivalent definitions.
  - *Mismatches with the prose:*
    - (a) The prose's cascade ends at language and moral weight (:39); the figure stops at Self-Actuated "by design" (:61–63 of the `.tex`).
    - (b) The prose sends "letting the agent set its own objectives" to the companion volumes, while the figure puts Self-Actuated inside Volume 1, which matches the OUTLINE: its home `#deriv-self-actuation-grounding` is Vol-1 Appendix A.
    - (c) The caption promises "what each narrowing unlocks", but Agentic's "capability" just repeats its delta ("causal intervention"), so the frame unlocks nothing visible.
    - (d) The Part II preface's scope lattice (which you noticed) is a *third* cascade, different from both.
  - *Joseph's ask vs result:* he asked for a "Scope of work" *section* around the figure. There is no such heading.
- **`agent-spectrum.svg`** — the "nearest relative" the first draft cited. The model-richness × objective-richness 2×2 with quadrants Reactive System / Adaptive Tracker / **Blind Pursuer** / Actuated Agent, and a dashed "migration" path. **Stale labels:** "Blind Pursuer" was renamed "blind seeker" on 2026-05-17 (`6b0362f8`), and the quadrants are marked "SECTION I / SECTION II", the pre-Part naming. Not embedded anywhere.
- **`adaptive-cycle.svg`** — the five-phase cycle (Prolepsis / Aisthesis / Aporia / Epistrophe / Praxis, each with an English gloss and its equation: $\hat o_t$, $o_t$, $\delta_t = o_t - \hat o_t$, $M_t = M_{t-1}+\eta^\ast g(\delta_t)$, $a_t=\pi(M_t)$) around "Environment $\Omega$ (partially observable)". The introduction's history section says "the same cycle structure recurred across domains" (:54), but never shows the cycle. The Greek phase names occur once in the whole reader snapshot (`grep -c prolepsis CURRENT-VOL1.md` = 1). `TODO.md:105` records Joseph's decision to keep the Greek with an English anchor "at first introduction". This is a candidate for an introduction-level picture; it isn't embedded.
- **`driver-snow-foundation.{tex,pdf}`** — forward, Part I introduction (`OUTLINE.md:12–13`). The introduction promises it (:60). The PDF review's three defects are at `msc/aat-v0.4.0-pdf-review.md:120–126`. That's forward material, so I'm only noting where it is.
- **`agent-environment.svg`, `complete-agent-state.svg`, `persistence-condition.svg`** — later-segment material. `msc/figure-pipeline-buildout-2026-05-18.md:160–195` catalogues all of `img/`. It says only scope-of-work was wired "(it had explicit prose warrant: the intro literally promised…)".
- **Visual spike, `spikes/visual/catalog-ideation.md:94`** (Tier 5, "actively counterproductive"): "Scope lattice as a Venn / inclusion picture — table or prose is denser and clearer." Two days later the nested inclusion picture became Figure 1, and the 2026-08-15 PDF reviewer judged it one that "earns its page" (`msc/aat-v0.4.0-pdf-review.md:27,120`). The earlier rule was overturned in practice but never revisited in the spike. Also Tier 5: an unfilled agent-spectrum 2×2 is "close to chartjunk" (:96).

## 8. CHANGELOG extraction

The CHANGELOG has no entry of its own for the introduction's drafting. The 2026-05-17 entry (:692–703) is about spike routing. What it does have:

- `CHANGELOG.md:69`: W4 "present in `doc/readme/src/_position-and-lineage.md` and the CURRENT-VOL1 introduction".
- `:110`: the 2026-08-22 WN un-staling.
- `:386–392` (2026-05-28, SP-24): the root definition reframed around the *coupling*. The umbrella `agent` LEXICON entry distinguishes "the scope cascade (… the tiers shown at `#fig-scope-of-work`) from the orthogonal agent spectrum". The umbrella entry itself is `terminology/entries/agent.md:18–29`, and its :27 says the capitalized "Agent" is "*earned* at the actuated lift".
- `:47–49` (08-22): the assembly fixes. The Part I introduction title reaches the `.md` but not the PDF.
- `:215–231` (2026-07-03): B-1 and B-2 landings and the routed-not-executed list (:227).
- For "the tools are classical, the theorems are not", the dated guidance is in asf's `CLAUDE.md` §"Math-novelty recognition" (Joseph 2026-05-21), not the CHANGELOG.

## 9. Other things for a complete picture

- **Three senses of "agent" are in play on page 1.**
  - (i) INTRODUCTION.md:22: "a system that maintains an internal picture … acts on that world, and must continually adapt". Acting is required.
  - (ii) The canon umbrella since SP-24 (`terminology/entries/agent.md`): passive observers included.
  - (iii) The capitalized "Agent", earned at the actuated lift.
  - Meanwhile IBM's "functional agency" excludes thermostats (§6), and the LEXICON's *Agentic system* entry ("Adaptive system + outcome model + goal-directed action + model adaptation", `LEXICON.md:20`) disagrees with the introduction's and `#scope-agency`'s causal-contrast definition. It puts "goal-directed" at the tier where the introduction and the figure haven't introduced objectives yet. The 2026-05-17 design doc flagged this as §6(A) "[OPEN] … flag, do not unilaterally rewrite the LEXICON entry", and it's still unreconciled.
  - Joseph's 05-17 reasoning ("this is the introduction to AAT … Part 1's Introduction can pull back") explains (i). The pull-back was never written.
- **Four different "headline results" lists across front surfaces:**
  - the introduction's four anchors;
  - the README Position & Lineage four (persistence, the diagnostic split, loop-as-L2, software lab);
  - the external-reader consensus S9 (the diagnostic split, acyclicity);
  - the scout's proposed fifth anchor (loop-as-L2).
  - The Part II preface also leads with a "16/24" survival count.
  - For the reboot, the question "what are the three to five things this volume proves?" doesn't have one answer anywhere in the repo.
- **Stale pointer in asf's `CLAUDE.md` (`doc/sop/agents.sop.md`):** it cites "the `01-aat-core/OUTLINE.md` 'Reading AAT' preamble is two layers" as the worked example of respectful pedagogy. That preamble was deleted on 2026-05-17 (`feccd0d2`; `grep -c 'Reading AAT' 01-aat-core/OUTLINE.md` = 0). The same pointer appears in `msc/scope-of-work-ontology-and-figure-2026-05-17.md:235–237` and some PROPOSALS rows. Its measuring-stick content survives in the Findings Brief of `#disc-stability-certificate`, a forward reference. So the "mental model first" layer the project's own pedagogy doctrine names was removed from the volume front, and the introduction that replaced it deliberately doesn't do mental-model-first (per Joseph's "peers, not students").
- **Auditor priming path:** HISTORICAL-CONTEXT is on the de-novo AVOID list, but the introduction is a reordered HISTORICAL-CONTEXT, and every auditor reads it first. 731548 named the circularity from inside (§4.1, :39).
- **A related open item:** PROPOSALS Bundle 1 "Framework-face reframe" (`PROPOSALS.md:29–41`, value "+9 … +10 for paper-writing", "Joseph-check-in recommended"). Its unlanded list (:35) includes Part I's two-sentence stub. It's the portfolio home for exactly the front-matter coherence work the reboot is doing.

## 10. Forward references: noted, not handed over

*Skip this section if you want to meet the targets cold. Each row names what's pointed at and my soundness read. Where I checked soundness I read only frontmatter and the one-sentence summary of the target, plus the audit or CHANGELOG record. A phrase or two leaks.*

| Intro locus | Points at | Where | Soundness |
|---|---|---|---|
| :22 "temporal feedback system", "critical quantities" | Part I as a whole (mismatch, gain, tempo, capacity: never named in the introduction) | Part I | Sound. The cast is unnamed until the Part I figure caption. |
| :22 "exact dichotomy in the stochastic case" and :27 anchor 2 | `#deriv-sector-condition` Cor A.1S.1, `#deriv-stochastic-non-exit` | App. A 339–340 | Theorem sound per 731548/25. **The wording is stale**: it needs the unbounded-support qualifier (lxiii, unexecuted). |
| :26 anchor 1, "below which … it loses bounded behavior" | `#result-persistence-condition` (Part I Ch.4, OUTLINE :65); `#deriv-sector-condition` | I / App. A | **Stale after B-1** (2026-07-03). Canon now says the threshold is *sufficient*, and necessary for the uniform class-level guarantee or a radially tight sector, not for every agent. Also, the home segment's own summary calls its headline "the *two-condition decomposition*" (structural plus task adequacy). The introduction's "a single inequality" is the structural half. |
| :26 "Kalman … software team … organization" | domain instantiations (Part I tables, TST) | various | 731548 predictions :46 flagged "analogical, not measured" for org/software. Not re-checked. |
| :28 anchor 3, "identically, the classical Lyapunov stability theorem" | `#result-certificate-existence` (+ `#disc-stability-certificate`, Part II Meta-Arch I, :117) | App. A 346 | The target's summary scopes it "**at the linearized level**" (exponential stability). The introduction drops that qualifier, the same paraphrase-degradation pattern as the lossy-boundary incident. |
| :29 anchor 4 | `#der-directed-separation` (II :132), `#der-class-coercion-via-wrapping` (III :245), `#der-logogenic-as-wrapping` (Vol 3) | II / III / Vol 3 | Both Vol-1 homes are `status: conditional`, and the introduction states it flat. Plus the muddled-sentence finding (§4.1). |
| :39 "Level-2 causal data" | `#scope-agency` (I Ch.1), `#der-loop-interventional-access` (II :145) | I / II | Sound. The scope was refined by SP-28 (`CHANGELOG.md:370–376`). |
| :39 "letting the agent set its own objectives … companion volumes" | `#deriv-self-actuation-grounding`, `#disc-continuity-stance` | **Vol 1** App. A / II | Placement is inconsistent: self-actuation is Vol-1 material (and in the figure). |
| :46 "identity tracks an irreversible trajectory … restoring from backup" | `#def-chronica` (I Ch.1), `#scope-agent-identity` (I :70, robust-qualitative) | I | Sound at its tier. |
| :46 "sustained cost paid in information" | `#deriv-persistence-cost` | App. A 347 | conditional; sound. |
| :46 "objective without *enough* cannot rest … structural hazard" | `04-eli-core/…/der-bounded-objective-as-sanity-criterion` | **Vol 4** | discussion-grade. "Stated as physics, these are theorems" overstates this one. |
| :50 active inference "recoverable … under three explicit restrictions" | nothing in canon; the spike only | — | **Unhoused** (§0.2). |
| :50 information-theoretic agency / coevolving automata "complementary" | Hafez (external); Miller in Part III GAPs and App. B | III / App. B | Sound as positioning. |
| :54 acyclicity from temporal ordering; Markov from causal sufficiency; the diagnostic split; "one geometric object"; composition machinery | `#def-strategy-dag` (II :161), `#deriv-graph-structure-uniqueness`, `#def-satisfaction-gap` (:162) / `#def-control-regret`, `#disc-additive-coordinate-forcing` (:122), Part III | II / III | Plausible. `#def-strategy-dag`:18 itself says the DAG is a consequence "at the level of sufficiency, not yet necessity". Acyclicity specifically looks fine. Not deeply checked. |
| :58 "Part I mathematically closed with simulation validation" | Part I | — | Contested (§0.3). |
| :60 driver in snow "recurs across the chapters" | Part I figure only | I | **Unfulfilled** (§0.5). |

## 11. Where I looked and found nothing (so "none" means something)

- **Spikes:** grepped all of `spikes/` (including `.integrated/`, `.archived/`, `PROPOSED*.md`, `ROUTING.md`, `INDEX.md`) for INTRODUCTION, "volume intro", the four anchor names, Miehling, scope-of-work. Only the files in §5 turned up. `spike-honest-activation-2026-09-23` and `spike-epsilon-programme-2026-08-24` (the newest) are unrelated.
- **Audits:** all 24 `AUDIT-WORKING-*` dirs, `ADJUDICATION-WORKING-218564`, both `.integrated/` trees, and every FINAL. Only the files in §4. Pre-2026-05-17 audits can't be about the file. Some critique HISTORICAL-CONTEXT or the README, which are its sources (S3 in the ledger, for example), but I didn't mine those.
- **LOG.md:** frozen before 2026-04-24, so it predates the file. Not searched beyond that fact.
- **CHANGELOG:** no dedicated entry (§8).
- **TODO / PROPOSALS / JOSEPH-TODO / PRACTICA / TODO-big-picture:** no item names INTRODUCTION.md. What bears on it is in §4.5 and §9.
- **relata:** Miehling absent. Hafez converted today (§6). I didn't convert the active-inference papers. The introduction only positions against them, and canon's comparison is the thing to read.
- **img/:** everything in `01-aat-core/src/img/` is listed in §7. Only scope-of-work is about the introduction.
- **memorata:** Joseph's typed turns about the introduction after 2026-05-19: only the 07-02 remark (§2.2). No later reaction to the file itself turned up.

## 12. Feedback

**On the parallel-finders question.**

My honest read is that splitting by category would help the inventory and hurt the report, because nearly every finding worth having here was a join across categories. Some concrete chains from this run:

- The audit gold (731548/01, §3) → the same auditor's later reflection (25-…:10, 28) → the FINAL, where the item is missing → NOTATION, TODO and the ledger, where it's also missing → "unexecuted".
- The FINAL's B-1 → the CHANGELOG landing and its register-site list → the introduction not on that list → "stale".
- The escape-standpoint spike → the memory file → memorata → Joseph's 05-17 intent quotes → the "Part I will pull back" plan → the Part I stub → the three senses of "agent" → SP-24 in the CHANGELOG → the LEXICON disagreement.
- HISTORICAL-CONTEXT's own "candidate-formulation grade" → canon grep → `disc-ciy-unified-objective` → the spike's "do not promote".

A spikes-only agent would have reported the FEP spike as "LANDED (scope-honored)", which is true, and missed that the introduction overstates what landed. A CHANGELOG-only agent would have reported B-1 as landed, and missed that the introduction wasn't on its fix list. The category lists would each be correct and the report would be missing its top five items.

Where the time went, as felt effort: tracing resolutions across files was the bulk. Git and memorata history came next; the commit bodies and Joseph's quotes were very high-yield. Then the forward-reference soundness pass. The mechanical parts were quick, except the one serial wait (the relata conversion, about a minute) and the broad greps to find candidate files.

What *would* parallelize well:

- **A cheap first sweep** that lists every file in audits/, spikes/, msc/, CHANGELOG line numbers and commit hashes mentioning the segment's slug, its key terms and its dependents. That's a candidate list, not reading.
- **Mechanical side-jobs:** relata conversion and line-ranging; rendering and describing the img/ files.
- **Targeted deep-dives** the finder launches mid-run once it knows the question, like "is 731548's lxiii executed anywhere?" or "does canon house the EFE three-restriction claim?". Those are question-shaped, not category-shaped, and would be good fork or sub-agent work.

So: one mind doing the reading and the joins, with helpers for the sweep and the mechanics. Also, most later segments will be much narrower than a volume introduction, which touches everything. I'd expect a single finder to be enough for most of them, and the intro to be the worst case.

**On the brief.** It was excellent: the purpose, the reader, the forward-reference rule, and "where you looked" all shaped the work. Three things I'd consider:

- **What "unintegrated" means per segment.** I used it as "not reflected *in this segment*", so a finding that landed elsewhere but left this file stale counts as live. That turned out to be the most useful reading, and saying so in the brief would help later finders.
- **Finder judgments can prime the reader.** You're trying to preserve a reader's experience, and my soundness verdicts are exactly the kind of thing that primes. I've fenced them into §10. Future briefs might ask for that fence explicitly.
- **The CLAUDE.md-scale context this role inherits is itself priming.** I arrived knowing asf's architecture from the auto-loaded `CLAUDE.md`. For the in-order experiment, the reader (you) presumably has the same bleed. Worth naming in the method.

**Adjacent, for Joseph or asf's own trackers (not acted on; asf is read-only for me):**

- 731548 lxiii (GA-2S three-grade tightening plus the Brief and intro clauses) fell between the working ledger and the FINAL. It's worth a tracker row.
- `agents.sop.md`'s pointer to the deleted "Reading AAT" preamble is stale.
- Miehling needs a relata entry and a bibliography entry.
- The relata author-field mismatch for `hafez-2026-mathematical`.
- `spikes/visual/catalog-ideation.md` Tier 5 is contradicted by Figure 1's reception, so its rule may want revisiting.
- The 03-scout's §2.5 is stale.
- The LEXICON *Agentic system* entry versus `#scope-agency` is still the open (A) from 2026-05-17.
- aspectus: running it with `ASPECTUS_COLUMNS_HEAT=off`, as the global CLAUDE.md prescribes for de-novo work, printed "columns.heat accepted for this release; membership is now [layout]". The global instruction may want updating. I didn't write to `firmatum/utils/aspectus/inbox.md`, since my brief limited me to this one file.

**On the clarity problem, one fresh-eyes observation.** The introduction is good prose making claims that the rest of the repo has since moved under. That isn't a defect of the writing. It's a structural fact about front matter in a live theory: nothing ties a front-surface sentence to the canon it summarizes, so every landing elsewhere silently ages it. The generated surfaces (README, FINDINGS, LEXICON) solved this for themselves. The introduction is hand-written and outside every sweep (no slug, no `depends:`, not in the preface checklist). If the reboot's introduction cited its anchors by slug, even invisibly, a staleness check like `bin/refresh-all --check` could flag it when an anchor's home changes tier or wording.

*I'm staying on the line for follow-ups.*
