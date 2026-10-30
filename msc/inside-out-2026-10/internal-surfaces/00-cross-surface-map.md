# Internal surfaces — the cross-surface map

*KR3.2 of `../INTENT.md`, written 2026-10-30 by the internal-surfaces agent (Claude Opus 5.5), drawing on six sibling maps written the same morning by forks of me. HEAD moved from `4ee2b895` to about `7ad5cd34` while they worked; other agents were committing in parallel. Feeds KR3.3 (integrate at honest tier or set aside with reason) most directly, then O1, KR2.1/2.2/2.4, KR4.1 and O5. Section 2 is flagged for O1, as the coordinator asked: it is the live theory that would change the arc.*

## Proposed revisions to `INTENT.md` (bottom-up, from what the internal surfaces show)

Offered for the give-and-take Joseph asked for. Each names the section of this map that grounds it.

1. **Reframe KR3.2:** "Live theory stranded inside asf is mapped *and joined by slug, with each item's verify-state*." The map is only useful if an integrator can go from a segment to everything bearing on it, and know which claims were checked today. Done in prose here (the slug tables); a re-runnable form is the tooling in §8.
2. **Split KR3.3 by what blocks it.** The surfaces show that the stall is downstream of verification: verified, integration-ready work orders exist and nobody runs them (§4, §8).
   - KR3.3a: the small exact landings with written work orders are landed (§4, first list).
   - KR3.3b: each heavy landing has an assigned integrator distinct from its spiker and verifier, and lands or is set aside with a recorded reason (§4, second list).
   - KR3.3c: the Joseph-gated backlog released today is dispositioned, by default where a lead recommendation exists (§4, third list).
3. **Add KR3.4, the volumes' own completeness.** Every OUTLINE row has a file or is honestly marked or removed. The 44 legacy `old-*` files under `src/` are mapped to live segments, candidates, or deliberate retirement. TST (29 segments; theory several times its canon) and 03/04 (20 rows with no file) are where most is stranded, and no current KR names them (§1, §5).
4. **Add KR5.5, Working Notes classified, not drained.** Every WN item carries a kind and a status, so the open frontier, the correctness backlog and the owed research become visible. This replaces the stuck "WN drain" policy question (§8).
5. **Sharpen KR5.2 with one mechanical check:** a disposition or routing target that does not resolve (a slug with no file, a backlog no tracker holds) is a defect a tool catches. Five strandings here had that shape (§8).
6. **Widen KR4.3 to hand-written front surfaces.** `01-aat-core/INTRODUCTION.md`, `HISTORICAL-CONTEXT.md` and the README partials carry claims canon does not hold, and have no staleness signal (§2.6, §8).
7. **Inputs for O1.** §2 offers six clusters as candidates for KR1.3's placement work beyond the strategy-DAG specimen. Directed separation (§2.1) and the standpoint of the persistence condition (§2.2) are the two where the answer to "universal, for which class?" is already partly written.
8. **Measurement:** KR4.1's "290 segments" should read 246 (§1).

**Who reads this.** The coordinator first, then the goal-setting with Joseph and the owner review (Section 2 is written for them), then integration agents (Sections 3–7 and the six per-surface maps' slug tables are for them).

**How far to trust it.** Each claim below names its source map. "Verified" means a fork, or I, checked it against `src/` or git today; anything else is a relayed claim. I spot-checked four cross-surface claims myself (marked *coordinator-verified*). No fork read every file on its surface; each says what it did not read, and those gaps are listed in Section 10.

## 0. The seven files and what each is best for

| File | Surface | Best for |
|---|---|---|
| `00-cross-surface-map.md` (this) | all | the joins across surfaces, ranking, what to skip |
| `working-notes.md` | `## Working Notes` in every segment | the open frontier per slug; off-ramp correctness findings; WN-only math; Joseph's own hypotheses; a 235-row slug table |
| `audits-working-dirs.md` | `AUDIT-WORKING-*`, ADJUDICATION, `.gem-hunt-trail` | what auditors found that was never lifted; verbatim whole-theory statements (§4); missing-theorem candidates |
| `audits-top-level.md` | top-level `audits/*.md`, `aat-reboot-aux-supplemental/`, `audits/.integrated/` | the standpoint thread; the 2026-09-25 per-segment findings; the polish-ledger research seeds |
| `spikes.md` | `spikes/` | which spike results are spike-only, with ready integration plans; the `.integrated/` check |
| `msc.md` | `msc/` | the no-go re-carve; the era-artifact contributions; the agent-classification conflict; process self-diagnosis |
| `trackers-and-peripheral.md` | root trackers, decision briefs, `ref/`, TST lit-review, `empirica/`, OUTLINE GAP rows | the decision backlog; TST's stranded theory; missing-file rows; the external-research lists |

Two tools came out of the mapping and are on disk here: `audit-gold-status.py` (which audit material bears on a slug, and has it been lifted) and `wn-ledger-seed/` (four scripts that split all Working Notes into items with blame dates and kind tags). Both are prototypes; Section 8 says what they could become.

## 1. Corrections to this morning's measurements

These change numbers in `../README.md` and `../INTENT.md`.

- **246 segments, not 290.** 44 files under `*/src/` are legacy documents in no OUTLINE: 43 `02-tst-core/src/old-tst-*.md` (7,739 lines) and `01-aat-core/src/old-tf-appendix-f-multi-agent.md`. TST has **29** segments, not 72. Four live segments still cite `old-*` files. (trackers §2, verified.)
- **Recent motion is one study.** 377 of the 437 commits since 2026-08-24 touch only `empirica/glyph-sequence-perception/`, a halted notation-perception study whose MANIFEST says "No claims … Consumers: None". Outside it, theory work after late August is the 2026-08-24 decomposition cluster, the 2026-09-23 honest-activation spike, and the 2026-09-25 aux findings; the rest moved to `~/src/aat-refactored/` and `~/src/aat-v3/`. (trackers §2, verified.)
- **No Working Notes line has changed since 2026-08-24**, and no commit touches the four `*-core/` trees, `NOTATION.md` or `terminology/` after that date. (working-notes §1; audits-top-level §1.3; both verified.)
- **The 2026-05-30 gold-lift is real and covers half the corpus.** 119–120 segments carry lifted gold, all in `01-aat-core`, sweep batches A1–A17. TST, LLM, ELI and AAT batches A18–A21 were never swept. The July audits (731548, 374162, 628417) postdate the sweep and are almost entirely unlifted. (working-notes §1, audits-working-dirs §1–2; measured.) One filing record is false because of this: `audits/.integrated/MANIFEST.md` (2026-08-22) says 374162's batches were "lifted 2026-05-30", seven weeks before 374162 existed.
- **`spikes/INDEX.md` drift is confirmed.** The two freshest spike dirs and `meta-agi-sgi-etc.md` have no row; three rows are stale. (spikes, "The instruments themselves".)

## 2. For O1: stranded material that would change the arc

These are clusters, not single items. Each was reached by more than one surface or more than one independent reader, and each bears on what the theory claims, about which agents. Ordered by how much of the arc each would reshape.

### 2.1 What belief and goal *are*, why separating them matters, and what it costs

This is the most coherent piece of unlanded theory in asf, spread across four surfaces, and it reads as one story nobody has told.

- **What they are.** The 2026-08-24 decomposition-uniqueness cluster (spikes) defines belief counterfactually, relative to goal-interventions, and shows that this is the *unique completion* of directed separation. Only the pathwise core is in canon (`#deriv-decomposition-uniqueness`, verified by audit 592047). The distributional lift (Theorem D), the noise-privacy representation theorem, the genericity results (generic exact goal-coupling annihilates the belief object; splintering is forced by symmetry; inequivalence needs tuning), and the $\varepsilon$-programme (the disciplined picture returns at a tolerance equal to the agent's own coupling, with error linear in it) are spike-only. Two of the four spike files are unverified.
- **Why separation matters.** Joseph's own reframe in `#def-agent-spectrum` WN items 81–85 (2026-05-18…30): belief and intended reality are "99% the same" object, so wishful thinking is the default collapse, and "the entire content of agency is the protected 1%." Beside it, a sharpening the note itself calls genuinely new: goal leakage into $f_M$ concentrates in inference about the *unobserved present*, the only step with a free prior. (working-notes §2d.) `spike-leakage-locus-2026-05-18.md` holds the corresponding lemma; its consequence is used in the body of `#disc-partial-coupling-pathways`, but the lemma has no segment home (spikes).
- **What it costs.** Audit 731548 named a missing theorem: IB-optimal compression is policy-relative, so a strictly goal-blind $\phi$ is generically compression-suboptimal, and there may be an optimal coupling $\kappa^\ast \gt 0$. That would complicate "Class 1 is the clean case." It has no home anywhere; the 2026-09-25 aux 10 re-raised it with Still 2009 as a lead. (audits-working-dirs §3.3, audits-top-level §1.4.)
- **Where it fails for LLMs.** The frozen-LLM-with-KV-cache violation of $(C2')$ (TODO Tier 1), the $(C2')$-realization over-claim in `#def-auxilia-hierarchy` (`spike-c2prime-realization-spectrum`), and the goal-flow duality (trackers §5.2, spikes).

*Why it is arc-level:* directed separation is the theory's central architectural claim. This material says what it means, proves it is forced, prices it, and says how it degrades in coupled agents. None of that synthesis is in a segment body or an OUTLINE preamble.

### 2.2 The theory's first sentence: what an agent is uncertain about, and whose number each quantity is

Two independent threads, each reached several times, both about the root definitions.

- **The typed epistemic target (SP-30).** The broadest scope, `#scope-adaptive-system`, excludes zero-state-entropy systems as solved, which wrongly excludes standard RL (full observation, unknown kernel). The repair gives law-content $\theta$ its own slot beside state, $S_t = (\Omega_t, \theta)$. It was reached from the audit side (731548 B-3, 2026-07-03), the spike side (`spikes/epistemic-target-ontology/`, verification clean, with a forced sharpening: $\theta_h$ must be an observation kernel), and independently from the tool-interface side (`msc/era-artifact-asf-contributions-2026-07-04.md` C2, the "law stratum": a tool interaction mutates state, reveals state, or teaches law). The two documents do not cite each other. The decision package has been complete since 2026-07-04, gated only on Joseph. (spikes, audits-top-level §1.2, msc A2, trackers §3.)
- **The standpoint discipline.** Canon almost never says whose quantity something is: the theory's, an analyst's, a monitor's, a designer's, or the agent's. Five arrivals: `audits/fix-adaptive-reserve.md` plus its independent audit (2026-08-12/13, 52 of 53 citations checked), ledger row S35, gold in two segments' WN, and aux 03. The worked instance is live in canon: `#deriv-self-actuation-grounding:25,:70` asserts the agent reads its own adaptive reserve each step, underived, and that premise carries the constructive boundary of the self-actuation no-go. The audit found a cheap fix already modelled in canon: `#def-model-class-fitness` says its quantity is not agent-computable and gives a proxy. Both repair files are referenced by no tracker. (audits-top-level §1.1, verified.)
- **What "agent" means.** Three non-equivalent Adaptive→Agentic boundaries: `#scope-agency` (Pearl L2 contrast), LEXICON's `agentic-system` entry (unchanged at `LEXICON.md:20`), and the 2026-05-04 proposal's argmax-versus-regulation cut, which starts from the fact that PID *is* a Pearl intervention. Page 1 of Vol 1 uses three senses of "agent". (msc A3, audits-top-level §1.3, both verified.)

*Why it is arc-level:* these decide the class of systems every later result is about, and whether the persistence condition is a certificate an analyst checks or a quantity an agent steers by. Joseph's KR1.3 questions ("universal for which class?") cannot be answered for any result until these settle.

### 2.3 The strategy DAG: Joseph's specimen, answered from material that already exists

- **Proven sufficient, not necessary.** `#deriv-graph-structure-uniqueness` says so in its body (line 224: it "proves the DAG structure is *sufficient* … but explicitly flags *necessity*"), while its slug says "uniqueness" and `01-aat-core/OUTLINE.md:79` lists "the graph-structure uniqueness argument" among Part II's distinctive results. *Coordinator-verified.* (msc A1, working-notes §3.)
- **AND/OR is chosen, not derived, and misclassifies $k$-of-$n$.** (WN off-ramp in `#scope-and-or`, three substrates; ledger S24.)
- **Whether $O_t/\Sigma_t$ is a literal inspectable pair or an ascribed decomposition is unresolved**, and that decides which agents the DAG results are about. It lives in one gold follow-up in `#def-strategy-dimension`. (working-notes §3.)
- **Every optimality question is open, in Working Notes:** optimal topology (asked in two segments under two metrics), no compression price for strategy, mixed AND/OR interference, topology discovery. (working-notes §3.)
- **Commitment state has been open across three surfaces and three seasons:** audit 471203 (April, Missing 3), `#def-strategy-dimension` WN, PROPOSALS SP-12, and the 2026-10-07 agent-core strategy-DAG work. (audits-working-dirs §3.5.)
- **Readers notice the gap.** The Strategy Dynamics chapter intro is a `--GAP--` row (`01-aat-core/OUTLINE.md`, verified). The summary walk found the reader carries $\Sigma_t$ as an undefined slot for about three chapters. No auditor who walked the whole theory states what the DAG claims universally. (msc C2, audits-working-dirs §4.)

The Working Notes, read together, already give the honest statement the cluster lacks: one well-grounded representation (acyclic and Markov by theorem under causal sufficiency, AND/OR by choice), with diagnostics derived over it; the universality class and the optimality theory are the open frontier. The spikes map suggests the decomposition-uniqueness sequence (conjecture, refutation, forcing condition, quantify off the ideal) as a template for asking the necessity question.

### 2.4 The impossibility spine, re-carved

- `msc/nogo-structure-read-2026-07-29.md` (de novo, Joseph's hypothesis withheld) finds a single proof shape behind every floor: a witness pair, two systems that look identical to the agent but disagree on the target. The plurality M1 claims lives one layer down, in the obstruction. It names two families canon lacks. **Escape-set exhaustion** covers results whose content is a count of channels; `#der-compensation-channel-uniqueness` is cited by no `disc-*` segment (re-verified). **Self-silencing floors** are states where the repair signal vanishes. If the general statement holds, the open terminal forms of the continuity and truth deaths (`TODO.md:156(c)`) are *predicted*, not separately derived. It also identifies a free existence-to-genericity upgrade for M1 Instances 3 and 4, and separates reachability caps from information floors. None of it is in canon, and no tracker drives it. (msc A1.)
- M1's actor-positioning self-description does not pick out its own instance set: two agents independently found that "agent-side" does two jobs. (spikes, escape-standpoint row.)
- Open architecture questions from whole-theory readers, tracked nowhere: do floors compose (628417, ledger S5, WN gold); is "general open" infectious across the separability ladders; is the exponential-family geometry forced; do the three certificate obstructions exhaust. (audits-working-dirs §3.4.)

*Why it is arc-level:* the forcing-bound results are the spine (`TODO-big-picture.md`). A better account of why they share a shape changes how the theory explains itself, and family $\beta$ links Vol 1 to the deaths.

### 2.5 Vol 4 has a spine waiting in Vol 1, and its own rows are empty

- **The shadow catalogue:** ten Part I theorems whose Vol 4 readings inherit Part I's tier. Audit 731548 judged it would "arguably do more for the ELI program's defensibility than most direct Volume-4 writing." It is staged in `#impl-persistence-and-limits` WN and listed at `TODO.md:523`, but unwritten. (audits-top-level §1.4, audits-working-dirs §3.2.)
- **Honest activation** fills the `missing` row `#norm-honest-activation`. The spike is twice de-novo verified and proposes ten landings across 01 and 04; none has landed, and the spike is not in INDEX. (spikes.)
- **04-eli-core has 13 OUTLINE slugs with no file**, and 03-llm-core has 7, including what the prefaces lean on (substrate independence). 165 gold items are labelled "Belongs elsewhere" (about 51 aimed at 04, 21 at 03, 7 at TST), and none has arrived, because the lift never reached those volumes. (trackers §6, working-notes §2h.)
- **C5, intelligence–empathy convergence,** a direct contest with Bostrom's orthogonality thesis, is "the largest gap between conviction and derivation in the corpus" (reflection 29). Its hosts have no files. (msc A2.)

### 2.6 What the volume says it proves: no single answer

- There is no single answer in the repo to "what are the three to five things this volume proves?". The introduction's four anchors, README's four, the external-reader consensus, a proposed fifth anchor, and the Part II preface's "16/24" all differ. (aux 00, via audits-top-level §1.3.) The strategy DAG is not among `releases/v0.4.0.md`'s four. (trackers §7.5.)
- A front-surface claim canon does not hold: "active inference recoverable under three explicit restrictions" appears in `INTRODUCTION.md`, `HISTORICAL-CONTEXT.md` and the README partial, but only as a candidate hypothesis in an `.integrated` spike that recommends against promoting it. (audits-top-level §1.3.)
- Verbatim one-line statements of what AAT is, from readers who walked all of it, are collected in audits-working-dirs §4. These are inputs for KR1.2, not verdicts. Treat the Gemini auditors' "flawless / proves" register as enthusiasm, not verification, and note the ADJUDICATION record of seven primed cycles agreeing the contribution is "not mathematical", which is the deflation Joseph corrected on 2026-05-21.
- The meta-process review (2026-07-07) marks *coherence stewardship*, the role that keeps the arc legible, as `:health absent` in its process map. That is the process-side name for O1's pain. (msc C1.)

## 3. Live canon defects (KR2.1, KR2.2)

Each was checked against `src/` today by the named map, or by me. These are statement-layer defects, mostly on correct algebra, which is the species 731548, the reserve plan and the aux findings all describe.

| Site | Defect | Source; check |
|---|---|---|
| `#deriv-sector-condition:284` (also :18, :221, :274), `#deriv-stochastic-non-exit:105` | assert structural adaptation is a "generic eventual necessity"; `#sketch-structural-adaptation-genericity:14` calls the same hand-off "plausibly a mild overclaim", bridge not derived | 374162 batch 08; *coordinator-verified* |
| `#deriv-graph-structure-uniqueness`, `01-aat-core/OUTLINE.md:79` | slug and headline say uniqueness; body proves sufficiency | nogo-structure-read; *coordinator-verified* |
| `#deriv-strategic-composition:22, :50` | sub-scope $\alpha'$ transfers the sector template from potential-game structure alone; the off-ramp (F234–F236) says that gives neither a sector inequality nor uniqueness nor a basin. The R0/R1/R2 regime axis rests on it | working-notes §2b verified; I confirmed the display is present, not the full argument |
| `#deriv-self-actuation-grounding:25, :70`; `terminology/entries/adaptive-reserve.md:20` | agent reads its own reserve per step, underived | audits-top-level §1.1, verified |
| `#der-architecture-noidentifiability` | names `rho-decomposition`, a segment that never existed | spikes; *coordinator-verified* no file |
| `#deriv-variational-sector-condition:18` | headline factor $\sqrt{1-r^2}$; $r$ undefined, factor underived | audits-working-dirs §3.1, verified |
| `#emp-update-gain` | `depends:` missing two appendices; `\Vert` renders the conditioning bar as a double bar; `type: empirical` though derived | audits-working-dirs §3.1, msc A4, verified |
| `NOTATION.md:260` GA-2S; `:263` GA-5 | GA-2S does three inequivalent jobs (731548 item lxiii, never carried forward); GA-5 listed live though closed | audits-top-level §1.3, verified |
| `#deriv-recursive-update`, `#example-kalman` | stochastic $f$ breaks "$M_t$ is a function of $\mathcal C_t$"; flagship example is pure active perception with an off-by-one action index | aux 02/03/07/09, relayed |
| `#der-interaction-channel-classification`, `#deriv-recursive-update` | 526815 F204 and F75 still unfixed | aux 09/14, relayed |
| Front surfaces | active-inference claim; three senses of "agent"; LEXICON vs `#scope-agency` | Section 2.2, 2.6 |
| `#def-mood:50`, `#der-captured-objective-dynamics:44` | canon body cites an `msc/` memo (D-1 violation); the mood memo is also stale against canon's $\sqrt{\tau_{\text{env}}}$ law | msc E, A5 |
| Body-resident unverified citations | `[^bg2-2026-05-21]` in `#deriv-regime-marginal-indistinguishability` (8), `#disc-identifiability-floor`, `#disc-dynamic-regime-axis`; `[^cat-2026-05-22]` in `#der-directed-separation` (3), `#form-composition-closure` (3), `#der-class-coercion-via-wrapping` (1) | working-notes §2e, spikes, verified present |

Already fixed, listed so nobody re-opens them: the three-floor "reducible" label, the Regime-III "zero" contradiction, `#def-unity-dimensions` F146 (still listed open at `TODO.md:46`), `#der-chain-confidence-decay`'s monotonicity wording. (audits-working-dirs §3.1, working-notes §2b.)

## 4. Ready to land (KR3.3), sorted by weight, not date

**Small and exact; work orders already written.**
- `#schema-strategy-persistence` hard-ceiling convention (verdict B; `spike-strategic-persistence-hard-ceiling-convention`). INTENT already has this as F72 under KR2.3.
- The operator sector condition $\alpha_{\text{op}}$ into `#deriv-sector-condition`, with the operator-layer no-go reaching `#disc-identifiability-floor` (regression-cleared 2026-05-17; ROUTING warns that folding it in as "already Instance 2" is a replacement failure).
- The Ch.3 moves: dogmatism/nihilism into `#disc-anti-collapse`; the gullibility dual; `#emp-update-gain`'s `type:`. (msc A4.)
- Three `.integrated` spikes whose landing is WN-only: the symbiogenesis saddle-node threshold, the compositional-coordinate conclusion, and the Mori–Zwanzig "lower bound does not close" result. (spikes.)
- The 2026-09-25 aux "please add to Working Notes" checks and slug-tagged notes, 17 files covering Part I's front. (audits-top-level §1.3.)

**Heavy; each changes the theory's shape.** The decomposition cluster plus the $\varepsilon$-programme (2.1); SP-30 (2.2); the standpoint discipline with the reserve repair, whose blocked read of `#deriv-adaptive-gain-dynamics` is now unblocked (2.2); honest activation (2.5); the no-go re-carve (2.4); CL-1 `#dissipativity-template`, one coupled landing of three spikes; the additive-variance theorem (needs `#rho-decomposition`); language-as-causal-substrate Theorem 1 with the C2★ gap; the VCG strengthening of the alignment-impossibility spike; the floor-routing diagnostic segment (five arrivals in 731548) and the shadow catalogue; the attention postulate question.

**Joseph-gated, now released.** ROUTING's "Joseph batch" (spikes); the decision briefs, which the trackers map sorts into theory-substantive and process (trackers §3); TST-IDEAS §9's five segment-ready candidates, gated on "go-ahead on placement" (Section 5). The trackers map's suggestion: treat every brief with a lead recommendation as decided-by-default, and spend Joseph's attention on SP-30, C5, the 04-eli repo question and naming.

## 5. The two most stranded volumes

**TST.** 29 real segments. Around them: TST-IDEAS §9 (2026-05-21) declares five candidates segment-ready, including the theorem-grade wrapper-level persistence inequality, which has no file and no OUTLINE row; the two OUTLINE GAP rows have candidates the spikes resolved; the 2026-07-04 independent-derivations spike (21 TST-naive essays converge on a knowledge-persistence/enforcement theory TST lacks); the 2026-07-28 partition-isolation spike (TST's unit of analysis is a single developer, and concurrent writers are untreated); a 15k-line April literature review canon reaches only through `old-tst-*` files; 43 `old-tst-*` files whose claims nobody has mapped to live segments; and unlifted TST gold in three audit dirs. (trackers §1, §5.4, §7.1; spikes; audits-working-dirs §3.6.) The trackers map's judgment: TST's actual theory is several times larger than its canon.

**03-llm and 04-eli.** 20 OUTLINE slugs with no file. Their Working Notes are scaffolds whose named "canonical sources" are mostly outside asf (firmatum, ennaos, zoetica, `_self`) or are `msc/reflections/*` and AUDIT-WORKING-193847 §14 quotes. No audit gold was lifted. TODO's 2026-05-01 Parts III–IV list carries eleven promotion candidates and six new-segment candidates. (working-notes §2k, §5; trackers §5.2, §6.)

## 6. External research to integrate (KR2.4; Joseph's "list in there somewhere")

There is no single list. There are at least eight, each now indexed in one place:

- **The main lists:** trackers §4, table E1–E8. It covers the 2026-08-22 landscape letter, the layer-3 search (already integrated), the 21 prior-art analyses and catalogs, the enrichment candidates (§3–§4 untouched), the TST `next-research*` files, the Undermind novelty-defense documents still cited from canon, Alan Walton's Deutsch pointer (0 mentions), and the `PROPOSED.md` `ext:` rows.
- **Spike-held queues:** spikes, "External research to integrate". It covers the five `ext:` rows (none started; Virgo & Baltieri marked *unread*), the PROPOSED-ADVANCED literature rows, and about nine prior-art or novelty searches queued inside spikes and never run.
- **Per-segment debts:** working-notes §2e. 40 owed searches or verifications across 33 segments, plus the Findings Search Logs.
- **Audit-side debts:** audits-top-level §2 and audits-working-dirs §7. These include a "Phase-3 citation verification backlog" that no tracker holds, Miehling 2025 missing from relata and every bib, and a by-slug table of uncited prior art found 2026-09-25 (Still 2009, Richens 2025, the past-future IB papers, Bar-Shalom & Tse, and others).
- **msc lists:** msc, "External research". The 20 prior-art search prompts of 2026-05-20, the domain-transfer questions, the separability-ladder prior-art map, the mood-science references.
- **Outside asf, for the influx scout:** `~/src/.moved-and-integrated/relata/IMPORT-ASF-TODO.md`.

The Findings Search Logs are themselves a per-segment owed-research record, in canon. My own tally takes the first depth word in each of the 47 segments carrying a Search Log: 18 `intuition-only`, 14 `targeted`, 14 `comprehensive`. The Working Notes fork counts 30 segments declaring `intuition-only` somewhere in Findings. The difference is method (first word versus any occurrence); a segment can carry several dated entries.

**What to read first.** The body-resident unverified citations (Section 3, last row) and the bg2 footnotes a softening rests on, flagged three times since 2026-05-21; the decomposition-cluster novelty search ("required before any external novelty claim"); Michel & Siegle 2024 before the $\varepsilon$-programme lands; the landscape letter's Richens and Virgo & Baltieri items, the nearest published neighbours of `#form-agent-model` and `#der-directed-separation`.

## 7. What integration agents can skip, and what they must re-check

**Skip:**
- `spikes/.integrated/`, apart from the three WN-only landings in Section 4;
- `audits/.integrated/`, provided you follow the homes it points to ("graduated" means every finding has a home, not that the content is in canon);
- `spikes/.archived/`, `spikes/.routing-trail/`, `ADJUDICATION-WORKING-218564`, `.gem-hunt-trail/` (except `gold-lift-sweep-2026-05-30.md`, the live plan for the unrun wave 5);
- the `msc/` residue in msc §D, several of whose status lines are now false;
- `empirica/glyph-sequence-perception/`, which is not agency theory;
- `CHANGELOG.md` and the `.integrated` dirs as integration sources (Joseph's red herring).

**Re-check against the segment body, every time:**
- Working Notes off-ramp findings (state mixed, item by item);
- tracker items (several list fixed defects as open, and `TODO.md:153` lists a mostly-landed workshop as high priority);
- April audit items (canon moved a great deal between April and August);
- the 526815 F-ledger ("stale" is not "resolved": F75 and F204 are still live);
- gold items, some of which aux 03 found stale or wrong.

## 8. The system (O5): what all six maps saw

Each map wrote its own system observations. These are the ones at least two maps reached independently.

- **The spike and audit stages work; the integration stage does not run.** The late spikes separate spiker, verifier and integrator, write integration plans, and pass de-novo verification. Then nothing integrates them. The repair plan in `audits/fix-adaptive-reserve.md` is the best-verified document in its surface, and no tracker points to it. (spikes, audits-top-level, msc.)
- **"Routed" meant "a destination was written", never "the destination exists and gets read".** The phantom Phase-3 backlog, the dangling `#rho-decomposition`, 731548's item lxiii, the false MANIFEST line, the no-go read reachable only through one INDEX row: all have this shape. (audits-top-level §6, msc, spikes, audits-working-dirs.)
- **Gate words became the stall.** "Joseph-reserved", "awaiting go-ahead on placement" and "external-eye gate" parked SP-30, TST §9, C5, the hard ceiling and the ROUTING batch for three to five months. Today's lift releases all of it; the SOPs should say what replaces those words. (trackers §8, spikes.)
- **Working Notes became the theory's unresolved-state database without being designed as one.** They hold the open frontier, correctness backlog, owed research, influx index, pedagogy reservoir, regression memory and process history, in prose, without status or owner, at about 500k tokens. The designed drain (Gate 4 at `candidate`) never fired, and Joseph ignores `stage:`. "WN drain" is stuck because it was framed as moving text; the real need is to classify items first. Each class has a different destination. (working-notes §5, msc C1, trackers §5.5.)
- **The gold-lift cuts both ways.** It brought resolved findings back as texture, carries some wrong gold, and primes every later de-novo reader (731548 and 374162 both say so). Batch and whole-walk audits never fit the per-segment rule, so the strongest recent readings are the unlifted ones. (audits-top-level §6, audits-working-dirs §6.)
- **Every tracker is indexed by provenance and date; nothing is indexed by what the theory claims.** That is Joseph's lost clarity, mirrored in the machinery. A question-keyed index ("which class of agents does this hold for, and what would test it?") does not exist anywhere. (trackers §8.)
- **Front surfaces have no staleness signal.** The introduction has no slug or `depends:`, so B-1, SP-24 and lxiii each left it stale silently. (audits-top-level §6.)
- **The project has a comprehension instrument and does not use it.** The 374162 quiz corpus plus `msc/quiz-responses/` is the only measurement of whether an agent's grasp is real or performed. It is the natural candidate for KR4.2, and could also gate integration agents. (audits-working-dirs §5, msc C2.)

**Tooling seeds, all small, all suggested by more than one map.** Each turns a manual join into a command an integration agent can run per slug, and makes the next pass measurable.
- A `wn-ledger` that classifies WN items by kind and status, re-runnable so that "is the frontier shrinking?" becomes a number (seed in `wn-ledger-seed/`).
- An audit-gold join per slug (`audit-gold-status.py`).
- A check that every slug and path named in a tracker or disposition resolves, and flags items whose segments moved since the item's date.
- A generated, slug-keyed spike index replacing the narrative INDEX.

## 9. Calls that are Joseph's even today

- **Privacy:** `msc/joseph-working-notes.md` is gitignored and never committed, yet `#def-eli-cohort` WN, both 03/04 OUTLINE source lists and `LOG.md:72` cite it. It holds the 2026-04-28 Gemini 3.1 Pro audit conversation and a note on naming. Commit, move, or remove the citations? (msc E.)
- **Wording the honest-activation plan reserves for him:** "not a virtue commitment" and "absolute", each with a small no-go attached, plus a Crèche graduation-criterion change. (spikes.)
- SP-30's root-ontology choice and C5 are theory calls the trackers map would still put to him, even under a decided-by-default rule.

## 10. Method, limits, and feedback on the brief

- **Method.** Six forks of me, one per surface. Each inherited this conversation and wrote its own map, and none could spawn subagents (fork constraint), so "Sonnet for mechanical sweeps" did not happen. Each read its theory-bearing documents in full and sampled the rest; each map's opening states its coverage. I read all six maps in full, ran the date census and the Search Log tally, and spot-checked four cross-surface claims against `src/` (Section 3).
- **Not read by anyone today:**
  - the bodies of six earlier audit dirs (451729, 963715, 613842, 849201, 742613, 584721), 731548 reflections 01–25, and the 526815 running outline;
  - 16 of the 17 aux supplements beyond their note bullets;
  - the `old-tst-*` files, the TST lit-review bodies, and `ref/agentic-tft/`;
  - most of `msc/reflections/` and `summary-attempt/`;
  - the gold blocks beyond sampling.

  The ranking above is therefore strongest for the April–September material the forks read in full, and weakest for the TST and pre-May corpus.
- **Not done:** no re-derivation of any offered result; no verification of the unverified spikes; no canon edits.
- **Feedback on the brief.** It was clear, and the four "what makes this useful" points served every fork. Three things would have helped up front:
  - that `*/src/` contains non-segments;
  - that Joseph ignores `stage:` (several documents argue from stage gates);
  - that forks cannot spawn subagents.

  The brief's own framing ("what live theory is stranded, and how much does it matter to what the theory is") held up and was used by every fork.
