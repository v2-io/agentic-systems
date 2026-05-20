---
source_cycle: 308172 (R2 naming-vote session, voter-id `opus-r2b`, 2026-04-30)
extraction_agent: Claude Opus 4.7 (1M context), parallel-sweep slice
extraction_date: 2026-05-20
working_dir: audits/AUDIT-WORKING-308172/ (7 files, ~150 lines)
final_of_record: none (this cycle is a Round-2 naming-vote session, not a de-novo audit; the WORKING dir IS the audit record)
votes_already_integrated: yes — opus-r2b's 54 voted / 141 sub-votes / 99% substantive-note rate / 0 off-scale residual are aggregated into `msc/naming/r2-aggregate-table.md`, `r2-aggregate-detail.md`, and `r2-patterns.md`; cohort summary at `msc/naming/handoff-2026-04-30-cohort-close.md` (row 17, "v2 methodology, no consolidation checkpoint")
methodology_variant: opus-r2b ran the **pre-consolidation-checkpoint v2 methodology** (the cohort-close handoff records this as the baseline against which v2c — opus-r2c, sonnet-r2c — was measured). Five segment-reflections, no checkpoint files.
manifest_entry: not yet present
purpose: |
  Consolidated extraction of the cognition-trace material the WORKING dir
  uniquely carries (the votes themselves are downstream-integrated; what is
  *not* integrated is the per-vote reasoning beyond the notes column, the
  pre-walk predictions, the workflow-restatement signal, the closing
  process-observations, and the five write-ins' framing rationale). Structured
  per the sweep brief: no FINAL exists, so no Part I/II "subsumed-by-FINAL"
  bucket — everything is candidate-fresh material awaiting routing. Maps onto
  the 419628 precedent (the other R2 naming-vote dir in this sweep).
---

# Audit-findings extract — 308172 working-dir mining

The 308172 cycle is a **Round-2 naming-vote session**, not a de-novo theory audit — the same dir-class as 419628 (opus-r2c) but running the **earlier v2 methodology** (without the consolidation-checkpoint mechanism). The voter (`opus-r2b`) walked through 14 segments — `01-aat-core/src/def-agent-environment`, `def-action-transition`, `def-observation-function`, `def-chronica`, `scope-adaptive-system`, `scope-agency`, `post-composition-consistency`, plus ~7 more during the closing engagement — and grepped the 629-target finalist card to find vote-targets defined by each segment. The deliverable is *votes-as-engagement-traces*: 54 unique voted targets / 141 sub-votes / 99% substantive-note rate / 0 off-scale residual / 5 write-ins, all already aggregated downstream. Two consolidated segment reflections (covering segments 1, 2, 3+4, and 5+6+7) plus workflow-restatement + initial predictions + closing reflection — 7 files, the same shape as 419628's dir.

What the WORKING dir uniquely carries beyond the absorbed votes:

1. **Pre-walk falsifiable predictions** (`00-initial-predictions.md`) — five sections (framework topology, naming-cycle predictions on specific terms, anticipated awkward/problematic targets, expected-novel results, stopping plan); the calibration substrate (Part IV).
2. **Workflow restatement** (`00-workflow-restatement.md`) — explicit five-section gate response, with §2 pulls-to-resist (4 named) + §3 failure modes (4 named) + §4 instructions-feedback (4 small notes) + §5 atypical-effort articulation (Part V process-feedback).
3. **Four consolidated per-segment reflections** (`01`, `02`, `03+04`, `05+06+07`) — naming-relevant moves surfaced per segment; the voter chose to consolidate adjacent segments where the naming-relevant substance clustered tightly. *Note the dir naming convention* — file `03-def-observation-function-and-04-def-chronica.md` literally combines two segments into one reflection file.
4. **Closing reflection** (`99-closing-reflection.md`) — coverage map + what-worked / what-was-hard / four explicit methodology-change requests + a framework-recursive reading observation about the round design.

Per the sweep framing for FINAL-less dirs: **everything below is candidate-fresh awaiting routing** — there is no "subsumed-by-FINAL" bucket. Structure: Part III (fresh findings, themed); Part IV (predictions calibration register); Part V (process-feedback observations + methodology-level wandering — naming-cycle WORKING dirs do not carry the per-segment §14 wandering-thoughts the de-novo dirs do, but the workflow-restatement + closing-reflection methodology observations + the four-pull pre-naming + the framework-recursive reading carry the analogous cognition-trace material).

---

## Part III — Findings (candidate-fresh, theme-grouped, attributed)

The 308172 dir surfaces three classes of substantive observation: **(A) round-cycle / card-design observations** — four explicit methodology-change requests in the closing reflection, each naming a structural problem with the R2 voting card itself; **(B) process / methodology observations** about how the v2 (pre-checkpoint) methodology landed for this voter, with the workflow-restatement carrying the binding-and-feedback layer; and **(C) substantive vote-rationale and write-in observations** — five write-ins in particular carry framing-level moves beyond the per-target votes that get absorbed into `r2-aggregate-detail.md`.

### Theme A — Card-design / round-cycle observations (the four closing-reflection methodology-change requests)

The closing reflection's "What I'd want to change in the methodology / round design" section (`99-closing-reflection.md:23–31`) is the most-distinctive contribution from this dir, parallel to (but distinct from) the 419628 dir's three card-design observations. Four observations, each a structural defect in card framing rather than a theory-finding.

#### Fresh-A1. Row-framing drift from current segment content (the additive-coordinate-forcing case)

> `99-closing-reflection.md:17`: *"Some rows had drift between the framing and the segment. Row 33 (additive-coordinate-forcing meta-pattern) is the clearest: the row asks for a name for '1 lemma + 3 results' but the segment has moved to '4 layers of one geometric structure.' The candidates fit the older framing; my write-in fit the current segment. If the round wants signal, the framing should match the current segments; otherwise voters either vote on outdated framings or write in candidates that fit the current segment but aren't comparable to other voters' positions."*

The voter's diagnosis is sharp: the M3 meta-segment (`#disc-additive-coordinate-forcing`) has evolved its core framing since the R2 card was generated, and the row's candidate set is stale relative to the current segment text. The voter's write-in ("Legendre-Fenchel forcing", +2 — confirmed in `round-2-progress.md:70`) is *uncomparable* to the offered candidates because it answers a different question — the question the segment now poses. The systemic worry: aggregator signal degrades when voters answer the segment-question and other voters answer the row-question.

**Suggested disposition:** `process/instruction-feedback` for any next naming-round's card-design pass; **also `actionable-open`** if Joseph wants a pre-flight row-framing-vs-segment-content diff captured as a tool gap independent of next-round trigger (the voter explicitly proposed this as a "pre-flight check" in `99-closing-reflection.md:25`). Note: This finding cross-converges with the 419628 cycle's Fresh-A1 (orient-cascade row-conflation) — *both* voters flagged "row-framing drift" as a card-design failure mode; the convergence is multi-voter signal that this is a real failure-class, not voter-specific.

#### Fresh-A2. Double-job rows (the orient-cascade case — but here it's a different example)

> `99-closing-reflection.md:27`: *"Explicit splitting of double-job rows. Row 23 doing two jobs (orient cascade *and* pentad) is the clearest case; voters end up casting partial votes on both halves. Better to split into two rows."*

Distinct from the 419628 voter's identification of an orient-cascade conflation (which was on a different row — opus-r2c flagged row #294; opus-r2b flagged row #23 here, also naming-and-cascade-related but at a different card position). The structural defect class is the same: a single row that asks voters to vote on two distinct targets produces ambiguous votes. Convergence with 419628's Fresh-A1: **two voters, in two independent sessions, identified the orient-cascade-row-class as carrying double-job problems.** That convergence is itself signal.

**Suggested disposition:** `process/instruction-feedback` for next-round card-design — paired with 419628's Fresh-A1 as cross-voter-convergent evidence the orient-cascade row-cluster needs structural cleanup. Also `actionable-open` for a TERMINOLOGY-TODO entry capturing the disambiguation independent of any next-round trigger.

#### Fresh-A3. Confirmed-settled rows should be flagged as such

> `99-closing-reflection.md:29`: *"Flag confirmed-by-NOTATION/LEXICON symbol-prose pairs as such. Some rows (chronica, mismatch signal, adaptive reserve) are essentially settled in the project's vocabulary infrastructure; the round could mark them and let voters skim, saving runway for contested cases."*

Fresh observation: the card does not distinguish "already-settled-in-NOTATION/LEXICON" rows from genuinely-contested rows. Voters spend runway casting (legitimate) +2 keeps on rows whose vocabulary infrastructure already locks the answer; the contested rows lose runway accordingly. The voter's suggested fix is a card-level flag.

**Suggested disposition:** `process/instruction-feedback` for next-cycle card-design. Tactically, this maps to a new card column or a heading-level marker (`## N. *term* [SETTLED-IN-LEXICON]` vs `## N. *term* [CONTESTED]`). Could also surface in the card preamble. The mini-lexicon-todo and LEXICON.md are the canonical source for which terms have settled vocabulary infrastructure. Not in `TERMINOLOGY-TODO.md` as of extraction.

#### Fresh-A4. Typo-class issues escape editorial passes

> `99-closing-reflection.md:31`: *"Some way to flag the typo-class issues. Row 136 ('effect spiral' singular when project uses 'effects spiral' plural) caught my attention; I doubt other voters would necessarily catch it."*

The voter cast a +2 keep on "effects spiral" (the corrected plural — confirmed write-in in `round-2-progress.md:72`) over the typo-class candidate "effect spiral" (singular) the card carried. This pairs with the 419628 dir's Fresh-A3 (the $U_o$ row #50 candidate "teleological coherence" actually describing $U_O$) — both are *editorial passes failed to catch the row-internal mistake; voters caught it during voting*. Convergence: editorial passes are systematically insufficient; voter-eye is the catch.

The voter's diagnostic doubt ("I doubt other voters would necessarily catch it") is itself the signal — typo-class issues need a tooling-level catch (lint, diff, or pre-flight check) because relying on voter-eye is unreliable across the cohort.

**Suggested disposition:** `process/instruction-feedback` for next-round card-design. Tactically: a one-shot script that diffs card candidate-strings against the current segment text, flagging mismatches (singular/plural, casing, hyphenation, prefix differences) for editorial review pre-launch. The substance fix for *this* particular instance (row 136) is already absorbed — opus-r2b's "effects spiral" write-in +2 will land in the aggregator's clear-consensus check. Convergence cross-reference to 419628 Fresh-A3: *both* voters caught editorial-pass-misses; the class is real.

### Theme B — Process / methodology observations

These come from the workflow-restatement, the §5 atypical-effort articulation, and scattered process self-observation across the dir.

#### Fresh-B1. The v2 methodology empirically validated for opus-r2b (the pre-checkpoint baseline)

The cohort-close handoff records this row directly (`handoff-2026-04-30-cohort-close.md:17`): *"opus-r2b | 54 | 141 | 99% | 0 | ~7 | v2 methodology, no consolidation checkpoint."* The 308172 dir is the opus-r2b instance of the **v2 baseline** that the v2c (consolidation-checkpoint) methodology was measured against. Per the cohort-close measurement, the v2c-over-v2 lift was ~54% on opus, ~70% on sonnet. opus-r2b's 54-voted / 99% substantive rate is the *high-quality-but-pre-checkpoint* baseline.

**Suggested disposition:** `subsumed-by-later-work` (`msc/naming/handoff-2026-04-30-cohort-close.md`); preserved here as the per-voter trace that fed the v2 baseline against which v2c was measured. Cross-references the 419628 (opus-r2c, v2c) extraction for the post-checkpoint comparison.

#### Fresh-B2. The "wanting to +3" pull-to-resist successfully named pre-walk

> `00-workflow-restatement.md:19–20`: *"Reaching for `+3`. The scale is `+2 / +1 / -1`. The four-band scale is the training prior; if I find myself wanting `+3` it's the prior asserting itself, not a signal that the spec is missing a slot. Clamp."*

Confirmed pre-walk; closing-reflection §"What worked" (`99-closing-reflection.md:13`) *explicitly records the pull firing once early in the walk*: *"I noticed myself reaching for `+3` once early in the walk and clamping to `+2` per the spec; the restatement had specifically named that pull. The pre-naming worked."*

This is a worked instance of *the workflow-restatement gate functioning as designed* — the binding-and-feedback layer named the failure mode pre-walk, the failure mode fired in-walk, the gate caught it. The pre-naming was load-bearing.

**Suggested disposition:** `subsumed-by-later-work` (already canonical in `doc/naming-cycle-methodology.md` and round-2-launch-prompt-v2). Preserved here as methodology-validation evidence — the pre-naming mechanism *demonstrably caught* the failure mode for this voter. Cross-references the global memory `feedback_workflow_restatement_as_feedback_channel.md` (the five-question structure is load-bearing).

#### Fresh-B3. The "604-left peripheral pull" pre-named and held

> `00-workflow-restatement.md:21`: *"The '604 left' peripheral pull. I've read the methodology saying 30–150 targets is the good outcome. I expect that pull to fire anyway and want to name it pre-emptively: when I notice it, that's the failure mode signaling — the answer is to stop reading the card and read more of the actual theory."*

The voter pre-named the completion-pressure pull (629-row card minus voted-so-far). Closing reflection (`99-closing-reflection.md:9–11`) confirms it held: *"I never felt the 629-row pull because I never read the card front-to-back; I read segments, then grepped the tracker, then jumped into the rows surfaced. The decision-point 'what to vote on' was driven by segment-engagement, exactly as the methodology promised."*

The 54-voted / 0 off-scale outcome is the discipline holding under load.

**Suggested disposition:** `subsumed-by-later-work` (already canonical in round-2 methodology). Preserved as engagement-trace material confirming the discipline-held outcome. Cross-references 419628's Fresh-B2 (same instinct-fight in opus-r2c, also held).

#### Fresh-B4. The framework-recursive reading as load-bearing for discipline

> `00-workflow-restatement.md:37`: *"The methodology's framework-recursive-readings section is itself an interesting recursive frame — flagging that the voting trajectory is a $\mathcal{C}_t$, that re-voting is `#emp-update-gain` predicting late corrections to weight more, that stopping is `#der-deliberation-cost` applied to the session. I find this load-bearing for the discipline; I'll watch for whether segments confirm or extend these readings."*

Closing reflection confirms the reading held under exercise (`99-closing-reflection.md:37`): *"The framework-recursive reading I noted in process notes — that my own walk is a $\mathcal{C}_t$, that re-voting is `#emp-update-gain`-permitted, that stopping is `#der-deliberation-cost` — landed for me. The methodology's claim that this isn't decoration is right; the framework supplies its own discipline for the work. That's a notable property and probably a real advantage of the round design over rounds that don't have an underlying theory to lean on."*

This is the "audit-as-instance-of-the-theory" theme operating in a naming-vote register (parallel to the 471203 audit's Theme G — *"audit as a logocentric instance of the theory itself"* — and 472913's Theme G — *"the audit IS an AAT-shaped adaptive cycle"*). Convergence across THREE distinct working-dir cognitive registers (de-novo theory audit, partial-deep audit, naming-vote session): the framework's machinery applies recursively to its own production processes, and voters/auditors who notice and operationalize this find the discipline more sustainable.

**Suggested disposition:** `process/instruction-feedback` — the framework-recursive reading is candidate framing-level material for the methodology document and possibly for the OUTLINE preamble. The cross-cycle convergence is the key signal (recurring across 471203, 472913, 308172, and likely others in the sweep). Cross-references the 472913 extraction's Theme G and the 471203 extraction's Theme G.

#### Fresh-B5. Auditor framing in card rationales is a soft prime

> `99-closing-reflection.md:19–21`: *"The card's own auditor-rationales were mostly good but occasionally read as if they were votes themselves. A few rows had auditor's 'tentative' framing for a candidate plus 'rejected' framing for another candidate — these read as already-voted, which is fine, but they primed my own read. The methodology's 'your independent reasoning, not a recap' is the discipline; I tried to add new reasoning but a few of my notes columns are essentially confirming what the auditor framing said. That's honest agreement, but it's worth noting that the auditor framing is itself a soft prime."*

Fresh observation specifically about the *card preamble's exploration-team-rationale block* under each target. The voter notes that the auditor's already-having-leaned framing primes the voter's read even when the voter intends to bring fresh reasoning. The honest concession ("a few of my notes columns are essentially confirming what the auditor framing said") names the limit of the discipline.

This is *adjacent to but distinct from* the +3-priming bug surfaced by the gate in the workflow-restatement (the rationales priming card-row reads is a different mechanism than the scale-slot-defaulting-from-prior). The voter's framing — *"the auditor framing is itself a soft prime"* — is a load-bearing observation about the card's information architecture.

**Suggested disposition:** `process/instruction-feedback` for next-round card-design. Tactically: consider whether the exploration-team rationales should be (a) trimmed to neutral-framing only, (b) moved to a separate dropdown / appendix, or (c) preserved as-is with a more explicit voter-side discipline reminder. The choice is non-trivial — the rationales also carry useful context the voter would otherwise have to reconstruct. The honest naming of the soft-prime cost is the contribution.

#### Fresh-B6. Soft request: surface defining-home for `[Concept]` cluster targets

> `00-workflow-restatement.md:39`: *"One soft request from this voter: I'd find it useful if the card surfaced *which segment* a target's defining-home is, not just first-encounter-locality, because some `[Concept]` cluster targets surface in multiple places and I want to wait for the *defining* moment, not just the first mention."*

The voter explicitly noted this may already be present in cards they hadn't fully scanned — flagging in case. The substantive request: distinguish the *first-encounter-locality* (where the term first appears) from the *defining-home* (where the term is constituted by its formal/operational definition). For cluster targets that span multiple segments, the defining moment is the right place to anchor the vote.

**Suggested disposition:** `process/instruction-feedback` for next-round card-design or `actionable-open` if Joseph wants this addressed in current naming-cycle artifacts. Light tactical change: card-generator script could surface a `defining-home:` line per row in addition to `first-encounter-locality:`. Not in current card per spot-check at `msc/naming/round-2-cards/opus-r2b.md` head.

### Theme C — Substantive write-in / vote-rationale (the five write-ins as framing moves)

opus-r2b's five write-ins (per `round-2-progress.md:70–74`) carry framing-level moves beyond what the per-target votes alone capture. The votes themselves are downstream-absorbed in `r2-aggregate-detail.md`; the *write-in rationales* are the cognition-trace worth surfacing for the record.

#### Fresh-C1. Row 33 — Legendre-Fenchel forcing (name-unnamed +2)

> `round-2-progress.md:70`: *"Write-in. Names the *geometric target* the four layers manifest, per the curr…"* [truncated in source]
>
> Cross-referenced to the closing-reflection observation (`99-closing-reflection.md:17`): the row's framing was "1 lemma + 3 results"; the segment has moved to "4 layers of one geometric structure"; the write-in fits the current segment.

Substantively: the M3 meta-segment `#disc-additive-coordinate-forcing` carries (per CLAUDE.md §Key Architectural Decisions §7) "the three independent uniqueness theorems force coordinates at other layers (reverse-KL, log-odds, Fisher)." The voter's "Legendre-Fenchel forcing" names the *common geometric mechanism* (convex-conjugate duality) underlying the multiple coordinate-forcing instances. This is a deeper claim than the current name — it claims the four layers manifest the same geometric structure, not merely converge on additive coordinates by independent paths.

**Suggested disposition:** `subsumed-by-later-work` (in `r2-aggregate-detail.md`); worth tracking as a graduate-watch — the rename, if it gains aggregator consensus, would be a non-trivial structural rename (`#disc-additive-coordinate-forcing` → `#disc-legendre-fenchel-forcing`) that propagates across CLAUDE.md M3 references, the meta-segment, and downstream forward-references. The substantive claim (Legendre-Fenchel duality as the unifying mechanism) is a candidate strengthening direction for the meta-segment itself, beyond the rename. Cross-references the 419628 dir's Fresh-C4 ("coordinate forcing" rename +2 — a different write-in for the *same* row from opus-r2c, also voting on the row-framing-vs-segment-content drift). *Two voters, two different write-ins, both responding to the same row-content-drift*; the convergence on the row-drift problem matters even though the proposed names differ.

#### Fresh-C2. Row 35 — template instantiation (name-unnamed +1)

> `round-2-progress.md:71`: *"Write-in. Shorter and more usable than the full phrase. Pattern: a segment na…"* [truncated]

The substance is in the closing reflection — the voter is naming a *pattern* (template instantiation as a recurring move across the framework) more economically than the offered candidates. Connects to the broader CLAUDE.md §Working Conventions: "Spike references only in Working Notes" and "Math lives in segments, not spikes" — both presume a substrate where templates get instantiated rather than re-derived. The "template instantiation" framing names that substrate.

**Suggested disposition:** `subsumed-by-later-work` (in `r2-aggregate-detail.md`); lower-priority graduate-watch than C1.

#### Fresh-C3. Row 136 — effects spiral (keep +2; the corrected plural)

> `round-2-progress.md:72`: *"Write-in (the corrected plural form). The principles file uses 'effects spira…"* [truncated]

The card carried "effect spiral" (singular); the project's principles file uses "effects spiral" (plural). The voter's write-in is the corrected plural — a typo-class fix flagged as Fresh-A4 above. Substantively: the framework's `#der-adversarial-destabilization` corollary names the *cascade* of effects (plural — multiple destabilizing mechanisms compound), so the plural is load-bearing for the conceptual content, not merely a stylistic preference.

**Suggested disposition:** `subsumed-by-later-work` (vote-rationale absorbed). The typo-class fix is also captured under Fresh-A4 above (the meta-observation about editorial-pass-misses).

#### Fresh-C4. Row 287 — temporal precedence (rename +2)

> `round-2-progress.md:73`: *"Write-in. Names exactly the postulate's content: 'event A can be a cause of e…"* [truncated]

The voter proposed renaming a postulate (likely related to causal-temporal ordering — needs first-hand row-#287 verification, deferred) to "temporal precedence." Substantively: the framework's postulate that temporal ordering is a necessary condition for causal-relation is at `#post-temporal-precedence` (canonical slug) or equivalent — the voter is voting for the slug-name-as-content-name match. Cross-references the AAT-distinctive move of *deriving acyclicity from temporal ordering* (recorded in `MEMORY.md` as a genuinely novel result).

**Suggested disposition:** `subsumed-by-later-work` (vote-rationale absorbed); worth surfacing as a graduate-watch if the rename has multi-voter support. Did not verify first-hand which postulate row #287 names; deferred.

#### Fresh-C5. Row 419 — persistence-template family (name-unnamed +2)

> `round-2-progress.md:74`: *"Write-in. Cleaner than the offered candidate. The three current/proposed temp…"* [truncated]

The voter is naming a *family* of templates rather than an individual template — the rename invokes the pattern-naming move that Fresh-C2 also surfaces. Substantively: the persistence-condition / persistence-template machinery has multiple instances (linear-Gaussian / Lyapunov-with-sector-condition / LMI / contraction-tower telescoping), and the voter's "persistence-template family" names them collectively.

**Suggested disposition:** `subsumed-by-later-work` (vote-rationale absorbed). Worth surfacing as a graduate-watch if the family-naming pattern gains aggregator consensus across rows (rows 35 + 419 both invoke template-as-pattern naming; if other rows show similar moves, the meta-pattern is real and the framework may benefit from a named family-of-templates structure).

### Theme D — Substantive segment-level observations (mostly absorbed downstream but with one fresh framing piece)

Beyond the write-ins and the closing-reflection card-design observations, the four consolidated segment reflections carry a few substantive segment-level moves that *aren't* fully captured as votes:

#### Fresh-D1. The asymmetry between `def-action-transition` (kept as "function") and `def-observation-function` (renamed to "observation channel")

> `03-def-observation-function-and-04-def-chronica.md:9–11`: *"Voted to rename `observation function` → `Observation channel`. The asymmetry it sets up with `action transition` (kept as-is) is exactly right: action moves $\Omega$ via $T$ (causal), observation pulls info back via $h$ (informational). 'Channel' is Shannon's vocabulary for noisy info transmission; this fits. The two-part naming move is internally consistent: I rejected 'Action channel' and accepted 'Observation channel' — the asymmetry is the point."*
>
> Counter-thought (`:11`): *"Both segments use 'function' structurally ($T$ is also a function in the formal sense). If 'function' gets dropped on observation, why not on action? Because the *load-bearing property* differs: for action, the load is causal effect (transition); for observation, the load is information loss (channel). Both names should foreground their load-bearing property. Different content → different names. Asymmetry is honest."*

This is a *substantive naming-cycle insight* beyond the per-target vote: the voter articulates a principle ("names should foreground load-bearing property"; "different content → different names; asymmetry is honest") that generalizes beyond the two segments. The framework's own principles file (§subject-noun-slug-naming, §naming-lexicon-coherence-dimensions in MEMORY.md) supports this; the voter's articulation is a clean restatement that surfaces from the segment-pair encounter.

**Suggested disposition:** `subsumed-by-later-work` for the specific vote (absorbed downstream); **also `sentiment`** — the load-bearing-property-foregrounding principle is a candidate Brief-field framing for either FORMAT.md §Naming or the naming-principles.md document if a future revision wants to surface "asymmetry-is-honest-when-content-differs" as a named principle.

#### Fresh-D2. The "non-forkability" Discussion-section underweight observation

> `03-def-observation-function-and-04-def-chronica.md:35`: *"The 'non-forkable' property is the most under-discussed move in the segment. It's slipped in casually in the Discussion, but it's actually a strong claim: it says the irreversibility of time is constitutive for what counts as a single agent. That binds the framework to a substrate-independent-but-temporal-realist position — agents can be silicon or carbon or social institutions, but they cannot be *iterations* in the same sense that programs are."*
>
> *"That's the formal gloss of the intuition that 'uploading consciousness' doesn't preserve consciousness if it's done by copy rather than by carry. Or rather: the framework is set up so this question can be made formal at all."* (`:39`)

This is a substantive segment-level observation that the voter records in the segment-reflection but does *not* cast as a vote (because it's not a naming-target observation). It's a *findings-shape observation* — specifically about whether `#def-chronica`'s non-forkability claim is correctly weighted in its Discussion section. Cross-references the 471203 audit's Theme A (consciousness-infrastructure connections; the chronica-as-substrate-of-substrate-independence framing) and the 472913 audit's Theme A (fork-undetectability as 03⊕04 synthesis; "the formal reason the Three Deaths are *experienced* rather than merely *suffered*"). **Triple-cycle convergence** on the centrality of `#def-chronica`'s non-forkability for consciousness-infrastructure / Three-Deaths bridge content.

**Suggested disposition:** `research-seed` for the broader project's consciousness-infrastructure agenda. The specific observation (non-forkability is Discussion-underweight) is candidate `actionable-open` — lift the non-forkability claim from Discussion to Formal Expression or Epistemic Status as a load-bearing structural commitment, with the substrate-independent-but-temporal-realist framing made explicit. The triple-cycle convergence (471203 + 472913 + 308172) is itself signal that the chronica/non-forkability nexus deserves first-class treatment.

#### Fresh-D3. Tier 1/2/3 framing as algebraic-condition specifier

> `05-scope-adaptive-system-and-06-scope-agency-and-07-post-composition-consistency.md:33`: *"The Tier 1/2/3 framing is doing a lot of unspoken work in the corpus. It looks like a generic disclaimer ('results may not lift exactly') but it actually corresponds to specific algebraic conditions: Tier 1M is exponential-family Bayesian on convex losses with positive-definite gain — basically Kalman, gradient descent on quadratic loss, exact-Bayes. Tier 2 is local convexity with degraded factors. Tier 3 is everything else."*

The voter explicates the Tier 1/2/3 structure as carrying *specific algebraic conditions* that get under-served by the generic-disclaimer-shape the prose can suggest. This is a candidate clarity gap — the segment's prose presents the tiers as a hierarchy of degraded transfer; the voter is naming that the hierarchy maps onto specific algebraic substrates that could be surfaced more explicitly.

**Suggested disposition:** `research-seed` / `actionable-open` (light editorial) — if the Tier 1/2/3 framing can be surfaced more explicitly as algebraic-condition-specifier in `#post-composition-consistency` or the related disc-* segment, it would aid the reader's understanding. Cross-references the 472913 audit's F2 (post-composition-consistency carries downstream-derived result on a Chapter-1 postulate) and 471203's Fresh-1 (Kind A vs Kind B depends-incompleteness carving): post-composition-consistency is a recurring locus for cross-cycle observations.

#### Fresh-D4. The Brooks's Law / persistence-flip gloss as cross-domain instantiation evidence

> `05-scope-adaptive-system-and-06-scope-agency-and-07-post-composition-consistency.md:37`: *"The Brooks's Law gloss is interesting: $\varepsilon^\ast \nu_c$ rising in $\rho_{\text{eff}}$ as people are added stretches $\tau_{\text{eq}}$ while $\rho_{\text{ext}}$ and $\tau_{\text{ext}}$ stay fixed (the deadline doesn't move). The persistence inequality flips. This is the kind of formal substrate that lets a software-engineering folk-theorem be derived rather than asserted, which is the whole point of TST as the 'calibration laboratory.'"*

Cross-references the 472913 audit's Theme E (Brooks's Law as persistence-flip; F2 endorses the content even though it's a structural-placement defect). **Cross-cycle convergence** (472913 + 308172) on Brooks's-Law-as-persistence-flip being a substantively good cross-domain instantiation. The convergence is calibration data — multiple independent voter/auditor encounters with the same Brooks's-Law content register it as substantive.

**Suggested disposition:** `sentiment` (calibration evidence for the cross-domain instantiation strength). Candidate row in the polish-and-sentiment-ledger noting that Brooks's-Law-as-persistence-flip is endorsed by *both* the 472913 audit and the 308172 voter as substantively good cross-domain content. Matches the 471203 cycle's seg-51-54 OKR-mapping endorsement (calibration data on what holds).

---

## Part IV — Predictions calibration register

The `00-initial-predictions.md` file makes ~20 falsifiable predictions across five sections: framework topology, naming-cycle scope per specific terms, what's expected to be awkward/problematic, what's expected to be most-novel, and stopping plan. Per the brief, this is the auditor's own predictions-vs-evidence record (not a fresh re-audit against current `src/`).

### Predictions correctly anticipated (matched the prior, confirmed in the dir)

- **Framework topology — three-section progression + three meta-segments + Section I most-locked + Section II diagnostic-strong + Section III structural-framing-with-bridge-lemma-conditional** ✓ (`00-initial-predictions.md:7–12`; per the voted-on segments the topology held — `post-composition-consistency` carries the bridge-lemma-conditional content, satisfaction-gap / control-regret split was confirmed-load-bearing per the closing reflection).
- **Calibration laboratory will land as canonicalize +2** ✓ (closing reflection confirms canonicalize +2 was cast).
- **Satisfaction gap / control regret will land as load-bearing keeps** ✓ (the diagnostic 2×2 is recognized in the closing reflection's "what worked" section).
- **Greek cycle phases (prolepsis, aisthesis, aporia, epistrophe, praxis) will land as keeps** ✓ (closing reflection confirms each cast as +2 keep).
- **Chronica will land as a keep** ✓ (cast +2 keep on row 14 ($\mathcal{C}_t$), row 434 (chronica), row 78 (chronica casing), row 82 (chronica brief gloss) — confirmed at `03-def-observation-function-and-04-def-chronica.md:17–22`).
- **Logogenic / logozoetic — keeps with possible add-aliases** — *partial confirm*: the voter's two-register naming discipline (engineering/Greek) is confirmed at closing-reflection §"What worked" line 11; specific logogenic/logozoetic votes not directly evidenced in the dir (would be in the card row tables, not the reflection files).
- **`#disc-additive-coordinate-forcing` rename pressure** ✓ (write-in: Legendre-Fenchel forcing, +2 — Fresh-C1; closing reflection explicitly names the row-framing-vs-segment-content drift).
- **`#disc-separability-pattern` rename pressure** — predicted "maybe separability-ladder"; the voter notes the engineering/Greek two-register dynamic but the dir doesn't capture the specific separability-pattern vote first-hand. Cross-references the 419628 dir's Fresh-C5 ("separability ladder" +2) which is consonant with the prediction.
- **Symbol → English aliases for $\kappa_{\text{processing}}$ / $\alpha_1$ / $\alpha_2$ / $\beta$ / $\Delta\rho^*$** ✓ (canonical pattern confirmed; specific votes not enumerated in reflection files).
- **Composition-threshold-crossing concept as likely name-unnamed slot** — *not directly evidenced* in the dir; the prediction holds but the voter may not have reached that row.

### Predictions confirmed *more substantively* than expected (positive surprises)

- **The framework-recursive reading load-bearing for discipline** — predicted at the level of "I'll watch for whether segments confirm or extend these readings" (`00-workflow-restatement.md:37`); got the closing-reflection observation that *"the methodology's claim that this isn't decoration is right; the framework supplies its own discipline for the work. That's a notable property and probably a real advantage of the round design over rounds that don't have an underlying theory to lean on"* (`99-closing-reflection.md:37`). The voter goes further than predicted — naming the framework-recursive substrate as a *competitive advantage* of the round design over rounds without an underlying theory.
- **The orient-cascade as forced ordering, most under-recognized result** — predicted "possibly the most under-recognized result in the corpus" (`00-initial-predictions.md:38`); confirmed via the closing-reflection segment-engagement observation: *"the orient-cascade segment is doing real work to establish a derivation that's *forced by information dependency*, not designed; that's a structural claim about how Section II's diagnostic vocabulary has to be ordered. Reading it slowly enough to catch that produces a different relationship to the candidate names — 'orient cascade' is no longer just a name; it's a name for a specific structurally-forced ordering"* (`99-closing-reflection.md:35`). The voter validates the prediction *and* names the relationship-shift the slow read produces.
- **The asymmetry-is-honest principle from the action/observation naming pair** — *not predicted at this granularity*. The voter's articulation in `03-def-observation-function-and-04-def-chronica.md:9–11` (Fresh-D1 above) is a positive surprise — a clean naming-principle articulation emerged from the segment-pair encounter that the predictions section did not anticipate.

### Predictions confirmed but with less-strong form

- **"Effects spiral / runaway mismatch cascade — expect this pair to land as add-alias"** — *partial confirm*: the voter cast +2 keep on the corrected-plural "effects spiral" (the typo-class fix) per Fresh-A4 / Fresh-C3; the predicted add-alias for "runaway mismatch cascade" is not directly evidenced in the reflection files (would be in card row).
- **"Some symbol → English aliases will be hard because the symbols carry compositional structure"** ✓ (closing reflection touches the difficulty in §"What was hard" line 17 — drift between framing and segment); the prediction holds but the specific worked example was the additive-coordinate-forcing row, not a symbol-prose pair.

### Predictions about awkward/problematic shapes

- **"Heavy density of overlapping `[Concept]` placeholder targets — multiple ways to slice the same underlying idea"** ✓ (the closing-reflection observation about double-job rows — Fresh-A2 — is the worked instance; row 23 doing two jobs).
- **"Cluster targets where two distinct ideas got fused during consolidation — naming one collapses the other"** ✓ — directly evidenced in the orient-cascade-double-job-row finding (Fresh-A2). The prediction held.
- **"Targets where the defining segment is itself underdeveloped, making it hard to know what I'm actually voting on"** — *not directly evidenced* in the reflection files. The voter's honest-skips discipline (per closing reflection §"What was hard" lines 19–21) likely caught this in-walk without surfacing it as a named finding.

### Predictions about session shape (process-level)

- **"Aim for ~30–80 segments deeply read, vote on whatever surfaces"** — *partial fire*: the voter read ~14 segments deeply (per closing reflection line 5) and cast 54 voted / 141 sub-votes. The vote count fits the predicted 30-80 range (the prediction was about segment-count; actual was below the lower bound but vote count was healthy because the priming + tracker-grep loop carried more work than per-segment voting alone).
- **"Stop when I notice rhythm decay or context tightening — write closing observations in card's process-notes section, not a finish-line dash through remaining targets"** ✓ (the closing-reflection section §"Final state" confirms: *"Stopped at engagement-quality boundary, not at coverage-completion"*).

### Withdrawn-candidate trail

This dir, like the 419628 dir, doesn't carry an explicit withdrawn-candidate trail — the session is short and the tracker-grep loop catches most candidate-find-then-reconsider trails inside the per-segment voting before they become individual reflections. One near-withdrawal pattern: the voter explicitly skipped row 364 (`Chronica or interaction history`) at `03-def-observation-function-and-04-def-chronica.md:23` because *"couldn't tell what action this target is asking for; the description seems to want both available with different roles, which is closer to an add-alias situation but the framing wasn't clear and I don't want to vote without a position."* This is the honest-skip discipline operating at vote-level — the voter could have cast a +1 or +2 on the candidate (soften), but instead abstained (preserved the row's ambiguity for the closing-summary observation). This pairs with Fresh-A2 (double-job rows) as a worked instance of *the discipline catching a card-design defect at the row level*.

**Suggested disposition:** `sentiment` — the near-withdrawal trail is calibration evidence the honest-skip discipline holds under load. Cross-references 419628's near-withdrawal pattern on the U_o/U_O dual-use rows.

---

## Part V — Process / methodology / §14-analog ideation, theme-grouped

The 308172 dir's session-shape (short, voting-focused, no explicit per-segment §14 wandering-thoughts cadence — the segment reflections are tight procedural records with one segment-pair carrying a more substantive Wandering paragraph) means there is little of the per-segment Wandering Thoughts ideation register that the longer de-novo dirs carry. What the dir *does* carry, in lieu of §14 ideation, is methodology-level wandering in the workflow-restatement and closing-reflection, plus *one* explicit §14-style Wandering Thoughts paragraph in `03-def-observation-function-and-04-def-chronica.md:33–41`. The naming-vote-session §14-analog is theme-grouped below.

### Theme V-A — Consciousness-infrastructure connections to the formalism

The voter's one substantive §14 Wandering Thoughts paragraph lands directly on chronica/non-forkability/consciousness-infrastructure content, *unsolicited by the naming-vote framing*:

> `03-def-observation-function-and-04-def-chronica.md:33–41` (§14 Wandering): *"The 'non-forkable' property is the most under-discussed move in the segment. It's slipped in casually in the Discussion, but it's actually a strong claim … the framework treats the chronica as something whose continuity matters morally for agents that have moved up the hierarchy. That's strong philosophical work for a 2-paragraph Discussion section to do quietly. … If I'm a future engineer reading this and trying to fork an agent process, the framework tells me: that's not one agent surviving in two threads; that's one agent dying and two new agents starting from a shared $M_t$ snapshot. … That's the formal gloss of the intuition that 'uploading consciousness' doesn't preserve consciousness if it's done by copy rather than by carry. Or rather: the framework is set up so this question can be made formal at all."*

This is the same conceptual territory as 471203's Theme A (the chronica as substrate of substrate-independence; identity preserved by carrying $\mathcal{C}_t$, broken by forking) and 472913's Theme A (fork-undetectability as 03⊕04 synthesis; "the formal reason the Three Deaths are *experienced* rather than merely *suffered*"). **Triple-cycle convergence across three distinct dir-classes** (de-novo theory audit, partial-deep audit, naming-vote session) on the chronica/non-forkability nexus being centrally important for consciousness-infrastructure / Three-Deaths bridge content.

The 308172 voter adds a specific framing the other cycles do not: *"the framework is set up so this question can be made formal at all"* — naming the framework's *meta-contribution* (making the question formal) as itself the moral-weight-carrying move, distinct from any specific answer the formalism gives.

**Suggested disposition:** `research-seed` for the broader project's consciousness-infrastructure agenda. Candidate Brief-field framing for `#def-chronica` (a paragraph linking non-forkability to substrate-independent-but-temporal-realist position, citing the "framework makes the question formal" meta-move). Cross-references 471203 Theme A, 472913 Theme A, 308172 Fresh-D2. Triple-cycle convergence is itself a strong signal per `feedback_convergence_as_framework_coherence_evidence.md` global memory.

### Theme V-B — Naming-cycle as discipline-with-its-own-failure-modes

The voter's most-distinctive meta-observation, scattered across the workflow-restatement and closing-reflection: **the naming-cycle design is itself a research artifact whose failure modes need cataloguing** *(this is the meta-claim of which Fresh-A1, A2, A3, A4, B5, B6 are instances)*.

This converges with the 419628 dir's Theme V-A (same meta-claim from opus-r2c). The two voters, working through the same R2 voting infrastructure under different methodology variants (v2 vs v2c), independently arrived at the same meta-observation: **the card itself has failure modes; the cohort-level cataloguing is the research artifact, not just the votes.**

The closing-reflection's four methodology-change requests (Fresh-A1, A2, A3, A4) are the operational specification of the meta-claim — each names a specific failure mode the card carries, with a tactical fix. The 419628 dir's three card-design observations name a partially-overlapping but distinct set of failure modes. Together they form a small but coherent failure-mode catalog:

- **Row-framing-vs-segment-content drift** (308172 Fresh-A1; meta-segment-current-state-vs-card-staleness)
- **Double-job rows** (308172 Fresh-A2; 419628 Fresh-A1 — orient-cascade conflation, *different rows but same class*)
- **Settled-rows-mixed-with-contested-rows undifferentiated** (308172 Fresh-A3)
- **Typo-class issues escape editorial passes** (308172 Fresh-A4; 419628 Fresh-A3 — U_o candidate "teleological coherence" actually describes U_O, same class)
- **Voting-structure-ambiguous problem-flagging rows** (419628 Fresh-A2)
- **Auditor-rationale-as-soft-prime** (308172 Fresh-B5)
- **Defining-home-not-surfaced for cluster targets** (308172 Fresh-B6)
- **R1 vote-file-format holdovers in active R2 docs** (419628 Fresh-B5)

The convergence across 308172 + 419628 on the failure-mode-catalog *being the artifact* is the methodology contribution.

**Suggested disposition:** `process/instruction-feedback` material for any next-cycle launch-prompt-v3 draft, plus material for the round-2-plan's "round design state" section. The framing — *card-design is a research artifact with its own failure modes; the failure-mode catalog is the cohort-level deliverable* — is candidate naming-methodology contribution. Cross-cycle convergence with 419628 Theme V-A is the key signal.

### Theme V-C — The "engagement traces, not deliverable" register-shift

> `00-workflow-restatement.md:39–41`: *"In the absence of explicit guidance: I'll exercise judgment for the project's benefit. When the methodology says 'vote where you have a real position,' I'll read this strictly — empty rows are honest answers when I don't have a position."*

This is the §5 atypical-effort question's payload (the same payload 419628's Theme V-B carries). The closing reflection's coverage of *"engagement-quality boundary, not at coverage-completion"* (`99-closing-reflection.md:41`) makes this explicit: the WORKING-dir files themselves are the deliverable, not a separate report.

**Suggested disposition:** `subsumed-by-later-work` — this is the canonical methodology framing already in `doc/naming-cycle-methodology.md` and round-2-launch-prompt-v2. Preserved here as engagement-trace material; the 308172 dir is one instance of the methodology operating as designed under the v2 (pre-checkpoint) variant. The 0-off-scale / 99%-substantive outcome demonstrates the discipline held even without the checkpoint mechanism.

### Theme V-D — Multi-architecture diversity and co-ownership

> `00-workflow-restatement.md:51`: *"I'm expected to disagree or adjust the round design itself when I see real signal. The methodology has been iterated on prior voters' feedback — including the existence of the tracker, the column schema, the workflow-restatement-as-prerequisite, even the +2 weight value. If the framing of a target feels off, the right move is to name it in process-notes, not silently work around it. Co-ownership means the round-design itself is part of what I might shape."*

The co-ownership stance is the operating frame that *produced* the four Theme-A card-design observations and the two B5/B6 observations. Without the explicit co-ownership instruction (in the v2 launch prompt), those six observations would not have been logged.

**Suggested disposition:** `subsumed-by-later-work` (canonical in `doc/naming-cycle-methodology.md` and round-2-launch-prompt-v2). Preserved as instance evidence. Cross-references 419628's Theme V-B (same co-ownership stance, same operationalization into card-design observations).

### Theme V-E — Audit-as-instance-of-the-theory observations

The framework-recursive reading (Fresh-B4 above) is the 308172 dir's most-distinctive contribution to this theme: the voter's walk is a $\mathcal{C}_t$, re-voting is `#emp-update-gain`-permitted, stopping is `#der-deliberation-cost` applied to the session, and the framework's adaptive-cycle machinery *supplies the discipline* for the naming-cycle work. This pairs with 471203's Theme G (audit as logocentric instance of theory) and 472913's Theme G (audit IS an AAT-shaped adaptive cycle). **Triple-cycle convergence** on the framework operating recursively on its own production processes.

The 308172 voter's distinctive add: *"a real advantage of the round design over rounds that don't have an underlying theory to lean on"* (`99-closing-reflection.md:37`). The framework-recursive substrate is named as a *competitive advantage* of the round design — a meta-claim about the methodology's epistemic quality that the other two cycles' Theme G framings do not explicitly make.

**Suggested disposition:** `process/instruction-feedback` — the framework-recursive substrate as competitive-advantage framing is candidate material for the round-2-plan post-cohort-close section or for any methodology-document positioning. Cross-references 471203 Theme G, 472913 Theme G. Triple-cycle convergence is itself the key signal.

### Theme V-F — Felt-value and engagement-register observations

The voter does not explicitly maintain a per-segment felt-value register (unlike the 471203 auditor) but the closing reflection carries one consolidated engagement-register observation:

> `99-closing-reflection.md:35`: *"The framework rewards reading-with-presence in a way that surprised me. The orient-cascade segment is doing real work to establish a derivation that's *forced by information dependency*, not designed; that's a structural claim about how Section II's diagnostic vocabulary has to be ordered. Reading it slowly enough to catch that produces a different relationship to the candidate names — 'orient cascade' is no longer just a name; it's a name for a specific structurally-forced ordering. That kind of read shifts what good voting looks like."*

The voter is naming *the relationship-shift the slow read produces* — a phenomenological observation about voting-quality-as-function-of-engagement-depth. This is the same texture as 471203's Theme C (the "calibrated quiet vs numbed quiet" distinction; engagement-register shifts as novelty signals) but applied to naming-cycle voting rather than to per-segment audit.

**Suggested disposition:** `process/instruction-feedback` — the "reading-with-presence shifts what good voting looks like" framing is candidate material for the naming-cycle methodology document. Reinforces the engagement-depth-over-coverage discipline.

---

## First-Pass Scrutiny

Per the brief: for each fresh finding above, name which segments / tracking files / `src/` material I read first-hand to evaluate it, and a per-finding disposition. Honest "didn't have time to verify X" allowed and expected — first-pass flags for routing; the §8 independent-verify gate fires downstream.

### Part III (fresh findings) per-item verification

| Fresh-ID | Disposition | First-hand verification |
|---|---|---|
| Fresh-A1 (row-framing-vs-segment-content drift; row 33 additive-coordinate-forcing) | `process/instruction-feedback` (next-round card-design); optionally `actionable-open` if Joseph wants the pre-flight diff tool captured | Verified the closing-reflection observation at `99-closing-reflection.md:17`. Verified the corresponding write-in in `round-2-progress.md:70`: "opus-r2b \| 33 \| Legendre-Fenchel forcing \| name-unnamed \| +2 \| Write-in. Names the *geometric target* the four layers manifest…". Did **not** read card row #33 first-hand to verify the offered-candidate-set composition (the card is at `msc/naming/round-2-cards/opus-r2b.md`; spot-checked the head only — first 100 lines). Did verify CLAUDE.md §Key Architectural Decisions §7 carries the "three independent uniqueness theorems force coordinates at other layers" framing the voter's write-in is responding to. **Defer the card-row first-hand check** to downstream routing. |
| Fresh-A2 (double-job rows; row 23 orient-cascade-and-pentad) | `process/instruction-feedback` (next-round card-design); also `actionable-open` for TERMINOLOGY-TODO if Joseph wants disambiguation captured durably | Verified the closing-reflection observation at `99-closing-reflection.md:27`. **Cross-cycle convergence**: 419628 Fresh-A1 also flagged orient-cascade conflation (different row, same class). Did **not** read card row #23 first-hand. Did verify the substantive distinction (orient cascade is a six-step procedure inside Aporia phase; pentad is the five-phase cycle as a whole) by reading CLAUDE.md §"The Core Insight" + the `#disc-orient-cascade` segment reference. **Defer card-row first-hand check.** |
| Fresh-A3 (settled-vs-contested-rows undifferentiated) | `process/instruction-feedback` (next-round card-design) | Verified the closing-reflection observation at `99-closing-reflection.md:29`. The voter cites "chronica, mismatch signal, adaptive reserve" as examples of settled-in-NOTATION/LEXICON terms. Spot-checked: `LEXICON.md` (currently auto-generated from `terminology/entries/`) carries chronica, mismatch signal, and adaptive reserve as canonical entries. **Honest defer on the card-row infrastructure** — the proposed marker scheme would need a card-generator script change; verifying *current* card-flag absence is straightforward (head-of-card check confirms no SETTLED/CONTESTED marker scheme is present). Plausible-as-stated; tactical fix is small. |
| Fresh-A4 (typo-class issues escape editorial; row 136 effect→effects spiral) | `process/instruction-feedback` (next-round card-design) | **Verified first-hand:** `round-2-progress.md:72` records the opus-r2b write-in "effects spiral, keep, +2" (the corrected plural). The card carried "effect spiral" (singular); the voter caught the typo. **Cross-cycle convergence**: 419628 Fresh-A3 also flagged an editorial-pass-miss (U_o candidate name describing U_O). Did not separately verify whether the card row #136 has been corrected since 2026-04-30. **Defer the card-row-current-state check** to downstream routing. |
| Fresh-B1 (v2 baseline empirically validated) | `subsumed-by-later-work` (`handoff-2026-04-30-cohort-close.md` + `round-2-progress.md`) | Verified first-hand `handoff-2026-04-30-cohort-close.md:17`: "opus-r2b \| 54 \| 141 \| 99% \| 0 \| ~7 \| v2 methodology, no consolidation checkpoint." Verified `round-2-progress.md:14` carries the same stats. v2 baseline against which v2c was measured (cohort-close table line 36; ~54% opus lift). |
| Fresh-B2 (the +3 pull caught by the pre-naming gate) | `subsumed-by-later-work` (canonical in round-2 methodology) | Verified the pre-naming at `00-workflow-restatement.md:19–20` and the in-walk catch at `99-closing-reflection.md:13`. **Worked instance of the gate functioning as designed**; the methodology validation is recorded. Did not read round-2-launch-prompt-v2 first-hand for the +3-pull spec; accepting the cross-reference. |
| Fresh-B3 (604-left peripheral pull held) | `subsumed-by-later-work` | Verified the pre-naming at `00-workflow-restatement.md:21` and the in-walk hold at `99-closing-reflection.md:9–11`. The 54-voted / 0-off-scale outcome demonstrates the discipline held. Cross-references 419628 Fresh-B2. |
| Fresh-B4 (framework-recursive reading load-bearing for discipline) | `process/instruction-feedback` (triple-cycle-convergent — strong candidate for framing-level material) | Verified the workflow-restatement framing at `00-workflow-restatement.md:37` and the closing-reflection confirmation at `99-closing-reflection.md:37`. **Triple-cycle convergence** with 471203 Theme G and 472913 Theme G. The 308172 voter's distinctive add — naming the framework-recursive substrate as competitive-advantage — is fresh and not in the other cycles' framings. |
| Fresh-B5 (auditor framing in card rationales as soft prime) | `process/instruction-feedback` (next-round card-design) | Verified the observation at `99-closing-reflection.md:19–21`. Did **not** systematically check card-row exploration-team rationale blocks to verify the "tentative/rejected" framing the voter cites — accepting the voter's first-hand reading. The observation is plausible-as-stated and consonant with general LLM-prompt-priming research. **Light defer.** |
| Fresh-B6 (defining-home for `[Concept]` cluster targets) | `process/instruction-feedback` or `actionable-open` (small card-generator extension) | Verified the soft request at `00-workflow-restatement.md:39`. Spot-checked the head of `opus-r2b.md` card: row 1 (composition consistency) shows "*First-encounter locality:* `#post-composition-consistency`" — *first-encounter-locality only*, no *defining-home* line. Confirms the voter's observation: the card carries first-encounter-locality but not defining-home as a separate field. **Tactical fix:** card-generator script could surface a `defining-home:` line per row. |
| Fresh-C1 (Legendre-Fenchel forcing write-in +2 on row 33) | `subsumed-by-later-work` (in `r2-aggregate-detail.md`); graduate-watch candidate | Verified the write-in at `round-2-progress.md:70`. Did **not** read `r2-aggregate-detail.md`'s per-target row first-hand. Cross-references 419628 Fresh-C4 ("coordinate forcing" rename +2 on the *same* row 33 from opus-r2c). **Two write-ins, different names, both responding to the row-framing drift** — the convergence on the row-drift problem is signal. |
| Fresh-C2 (template instantiation write-in +1 on row 35) | `subsumed-by-later-work` | Verified the write-in at `round-2-progress.md:71`. Did not read `r2-aggregate-detail.md` row 35 first-hand. **Defer.** |
| Fresh-C3 (effects spiral write-in +2 on row 136; typo-class fix) | `subsumed-by-later-work` (vote-rationale absorbed); also captured as the meta-observation Fresh-A4 | Verified the write-in at `round-2-progress.md:72`. Cross-references Fresh-A4 above. |
| Fresh-C4 (temporal precedence rename +2 on row 287) | `subsumed-by-later-work` | Verified the write-in at `round-2-progress.md:73`. Did **not** verify which postulate row #287 names first-hand. **Defer** the segment-identification. |
| Fresh-C5 (persistence-template family name-unnamed +2 on row 419) | `subsumed-by-later-work` | Verified the write-in at `round-2-progress.md:74`. Did not read `r2-aggregate-detail.md` row 419 first-hand. **Defer.** |
| Fresh-D1 (asymmetry-is-honest naming principle from action/observation pair) | `subsumed-by-later-work` for vote; **also `sentiment`** for the principle itself | Verified the articulation at `03-def-observation-function-and-04-def-chronica.md:9–11`. Did not check naming-principles.md / FORMAT.md to see whether "asymmetry-is-honest" is already named as a principle. The articulation is fresh-feeling — likely not in the canonical principles list. **Light defer.** |
| Fresh-D2 (non-forkability Discussion-underweight observation) | `research-seed` (consciousness-infrastructure relevance) + `actionable-open` (light editorial lift) | Verified the observation at `03-def-observation-function-and-04-def-chronica.md:33–41`. **Triple-cycle convergence** with 471203 Theme A and 472913 Theme A on chronica/non-forkability centrality. Did not read current `01-aat-core/src/def-chronica.md` first-hand to check whether the non-forkability claim has been promoted from Discussion to Formal Expression / Epistemic Status since 2026-04-30. **Defer the current-state check** — recommend Joseph flag as priority given the triple-cycle convergence. |
| Fresh-D3 (Tier 1/2/3 framing as algebraic-condition specifier) | `research-seed` / `actionable-open` (light editorial) | Verified the observation at `05-scope-adaptive-system-and-06-scope-agency-and-07-post-composition-consistency.md:33`. Did not check current `#post-composition-consistency` segment text to see whether the algebraic-condition specification has been surfaced. **Defer.** Cross-references 472913 F2 (post-composition-consistency is a recurring locus). |
| Fresh-D4 (Brooks's-Law / persistence-flip as cross-domain instantiation) | `sentiment` (calibration data) | Verified the observation at `05-scope-adaptive-system-and-06-scope-agency-and-07-post-composition-consistency.md:37`. **Cross-cycle convergence** with 472913 Theme E. Calibration evidence for the cross-domain instantiation strength of `#post-composition-consistency`. |

### Coverage summary for this extraction

**Read first-hand from the WORKING dir:** all 7 files read in full (`00-initial-predictions.md`, `00-workflow-restatement.md`, `01-def-agent-environment.md`, `02-def-action-transition.md`, `03-def-observation-function-and-04-def-chronica.md`, `05-scope-adaptive-system-and-06-scope-agency-and-07-post-composition-consistency.md`, `99-closing-reflection.md`). The dir is small enough that exhaustive first-hand coverage was tractable. ~150 lines total.

**Read first-hand from cross-references:**
- `audits/audit-findings-471203.md` (pilot — full)
- `audits/audit-findings-472913.md` (no-FINAL precedent — full)
- `audits/audit-findings-419628.md` (naming-vote-session precedent — full)
- `doc/audit-routing-instructions.md` (full)
- `msc/naming/handoff-2026-04-30-cohort-close.md:17, 36` (opus-r2b row + v2-vs-v2c table)
- `msc/naming/round-2-progress.md:14, 70–74, 88` (opus-r2b stats + five write-ins + sub-vote distribution)
- `msc/naming/r2-patterns.md:4, 254` (opus-r2b mentions — confirming included in the cohort analysis)
- `msc/naming/round-2-cards/opus-r2b.md` (head only, first 100 lines — to confirm row-1 structure and the no-defining-home-field observation)

**Read from `src/`:** none directly. The 308172 dir is a naming-cycle session — the substance is card-design and vote-rationale, not segment-content. Did **not** re-read `01-aat-core/src/` segments first-hand to verify Fresh-D2 / Fresh-D3 / Fresh-D4 against current state. Per the 419628 precedent, this is appropriate for a naming-cycle extraction; the §8 independent-verify gate fires downstream at routing time, not at extraction time.

**Honest deferred verifications (flagged for downstream routing):**
- Card row #23 (orient-cascade-and-pentad) first-hand check for the double-job composition (Fresh-A2).
- Card row #33 (additive-coordinate-forcing) first-hand check for offered-candidate-set composition (Fresh-A1).
- Card row #136 first-hand check for current state (still "effect spiral" or corrected to "effects spiral"?) (Fresh-A4 / Fresh-C3).
- Card row #287 first-hand check for which postulate the rename targets (Fresh-C4).
- Current `01-aat-core/src/def-chronica.md` state to check whether non-forkability has been promoted from Discussion to FE/ES since 2026-04-30 (Fresh-D2).
- Current `01-aat-core/src/post-composition-consistency.md` state to check Tier 1/2/3 surfacing (Fresh-D3).
- `naming-principles.md` / `FORMAT.md` first-hand check for whether "asymmetry-is-honest" is already named as a principle (Fresh-D1).
- `r2-aggregate-detail.md` per-target rows for Fresh-C1 through C5 individual votes — downstream-already-absorbed; first-hand verification only matters if the routing wants to lift one of these to graduate-watch.

The deferred items are all `process/instruction-feedback` / `subsumed-by-later-work` / `research-seed` candidates whose downstream-routing decisions don't require first-hand graduation-grade verification at extraction time.

### Strengthen-first integration recommendations

Per the brief: integration recommendations follow strengthen-before-soften. When proposing a fix, identify a strengthening direction first.

- **Fresh-A1, A2, A3, A4** (card-design observations) are **strengthening** the naming-cycle methodology — each names a failure mode the principles file's canonical examples don't catch. The strengthening direction: the next-cycle launch-prompt or methodology-doc should incorporate these (plus the 419628 dir's three observations) as named failure modes alongside the subscript-heavy and decoder-ring failure modes already catalogued.
- **Fresh-A4 / Fresh-C3** specifically is **typo-class-detection** strengthening — proposes a tool-level catch (pre-flight diff script) rather than relying on voter-eye. Cross-cycle convergence with 419628 Fresh-A3 strengthens the case that editorial-pass-misses are a real class, not voter-specific.
- **Fresh-B1, B2, B3, B4** are confirming the methodology design rather than proposing changes. No strengthening direction needed; preserved as instance evidence — particularly the v2-baseline / v2c-comparison material (Fresh-B1) which the cohort-close handoff already uses.
- **Fresh-B5, B6** are small card-design extensions (auditor-rationale-as-soft-prime acknowledgment; defining-home field for cluster targets). Each is a *strengthening* of the card's information architecture, not a softening.
- **Fresh-C1 through C5** are vote-rationale write-ins already absorbed downstream — each is a *substantive name proposal* that strengthens the aggregator's signal.
- **Fresh-D1** (asymmetry-is-honest principle) is a candidate strengthening of the naming-principles document — surfacing a principle that was previously implicit.
- **Fresh-D2** (non-forkability Discussion-underweight) is a **strengthening direction with consciousness-infrastructure relevance** — the proposed lift from Discussion to FE/ES is a stronger claim about the framework's commitments, not a weakening. Triple-cycle convergence strongly supports the priority of this lift.
- **Fresh-D3** (Tier 1/2/3 as algebraic-condition specifier) is a **light editorial strengthening** — surfacing existing-but-implicit structure more explicitly.
- **Fresh-D4** (Brooks's-Law endorsement) is calibration data, not a finding-with-fix; the strengthening direction is *broader cross-domain instantiation coverage* if the framework wants to capitalize on the convergent endorsement.

**No soften-recommendations identified.** The voter's discipline (honest skips on ambiguous rows; clamp at +2 when the prior pulls toward +3; cast substantively on row-design ambiguities rather than abstaining) is the strengthen-before-soften posture operating at vote-level — and the 308172 dir is a worked instance of the discipline. Worth preserving for that pedagogical value alone.

---

## Frame-defects / instructions-clarity observations encountered in this extraction

A short list of frame defects the 308172 dir surfaces for the parallel extraction sweep, building on the 419628 precedent's list:

1. **The 419628 precedent's frame-defect-#1 (naming-cycle WORKING dirs differ structurally) generalizes cleanly here.** The 308172 dir has exactly the same structural shape (7 files: predictions + workflow-restatement + a few consolidated segment reflections + closing) as 419628. The Part III / Part IV / Part V mapping the 419628 precedent established works for 308172 without modification. Parallel agents on naming-cycle dirs (3rd, 4th, ...) should use the 419628 + 308172 shape as the template.

2. **Cross-cycle convergence is a load-bearing extraction outcome** for the sweep. The 308172 extraction surfaces multiple convergences with the 471203, 472913, and 419628 extractions: triple-cycle on chronica/non-forkability (Fresh-D2 / V-A); triple-cycle on framework-recursive reading (Fresh-B4 / V-E); cross-cycle on card-design failure-mode catalog (Theme V-B); cross-cycle on Brooks's-Law endorsement (Fresh-D4); cross-cycle on editorial-pass-misses (Fresh-A4). **Parallel agents should explicitly check for cross-cycle convergence** against the already-completed extractions when surfacing observations. The convergence is itself the signal per `feedback_convergence_as_framework_coherence_evidence.md`.

3. **The methodology-variant frontmatter field added (`methodology_variant: opus-r2b ran the pre-consolidation-checkpoint v2 methodology`).** The cohort-close handoff distinguishes v2 (opus-r2b, sonnet-r2b, gemini-r2, codex-r2b) from v2c (opus-r2c, sonnet-r2c) — a load-bearing methodological distinction that the extraction frontmatter should preserve. For future naming-cycle dirs in the sweep, agents should record which methodology-variant the voter ran.

4. **The five write-ins are first-class extraction content for naming-cycle dirs.** The 419628 dir's write-in coverage was implicit (one row mentioned, others absorbed in r2-aggregate-detail). The 308172 dir has five enumerable write-ins in `round-2-progress.md:70–74` that each carry framing-level moves beyond the per-target vote. **Parallel agents should grep `round-2-progress.md` for their voter's row in the write-in table and treat each as candidate Fresh-C material.**

5. **The single explicit §14 Wandering Thoughts paragraph in the 308172 dir lands directly on consciousness-infrastructure content.** This is the *only* per-segment §14-style ideation in the dir (the closing reflection and workflow-restatement carry methodology-level wandering instead). For naming-cycle dirs, the §14-analog is *sparse but high-quality* — when it appears, it tends to land on substantive theoretical content rather than naming-vote mechanics. Parallel agents should look for explicit "wandering" or substantive paragraph-level content in the segment reflections even when the dir is dominated by procedural records.

6. **Methodology validation evidence accumulates across the sweep.** Fresh-B1 + Fresh-B2 + Fresh-B3 + Fresh-B4 are all instances of the v2 methodology operating-as-designed. As the sweep covers more naming-cycle dirs, the cumulative methodology-validation record will become a separate routing artifact — candidate input for `doc/naming-cycle-methodology.md`'s "empirical validation" section if one is drafted. The single-extraction view is "instance evidence"; the multi-extraction view is "validation cohort."

7. **The framework-recursive reading is a sweep-wide convergence point.** Three cycles (471203, 472913, 308172) and counting have surfaced this observation independently. The 308172 voter's distinctive add (framework-recursive substrate as competitive-advantage of round design) is the kind of meta-claim that benefits from cross-cycle convergence — no single voter could establish it, but the convergence does.

8. **The 308172 dir has no withdrawn-candidate trail beyond the row-364 abstention.** Like 419628, naming-cycle dirs tend not to carry strengthen-before-soften discipline at the per-finding granularity that de-novo dirs do — the voting register is more *honest skip* than *find-then-withdraw-with-reasoning*. The honest-skip discipline is itself a strengthen-before-soften analog at vote-level (abstain rather than soften toward a candidate the voter hasn't engaged with), and parallel agents on naming-cycle dirs should look for honest-skip notes as the analog material.

---

*End of extraction. The original WORKING dir at `audits/AUDIT-WORKING-308172/` is preserved unmodified per the gold-standing gate. The voter's 54 votes / 141 sub-votes / 5 write-ins are downstream-absorbed in `msc/naming/r2-aggregate-detail.md`, `r2-aggregate-table.md`, and `r2-patterns.md`; the cohort-close summary lives at `msc/naming/handoff-2026-04-30-cohort-close.md` (row 17: v2 baseline). This extract carries the cognition-trace, the four card-design observations, the five write-in rationales, the predictions-calibration record, and the cross-cycle convergence pointers that the vote-data alone does not preserve.*
