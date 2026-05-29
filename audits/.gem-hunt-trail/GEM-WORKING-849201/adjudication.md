# Gem-hunt adjudication — audit-findings-849201

*Gem-hunt cycle 2026-05-29. Report-only; no canon edits/moves/commits. Landings + verification are Joseph's.*

## Orientation and the key structural fact about this file

`audits/audit-findings-849201.md` is **not a raw audit** — it is a 2026-05-20 *extraction-and-adjudication* of the `AUDIT-WORKING-849201/` dir, written by a prior sweep agent who already dispositioned every numbered finding against the 2026-05-16 MANIFEST (Cluster D). So Part I (F1-trail … F2-TST) and Part II (BP1-BP19) are **fully pre-routed** — every item is `subsumed-by-FINAL`/`subsumed-by-MANIFEST`, soft → ledger S16/S17. I re-checked those dispositions; the two with first-hand load-bearing landings (F1 opacity-gain; Fresh-2 score-sign) are confirmed correct against current `src/` (see below). Those are not the gem-hunt target.

The **un-captured remainder** is Part III ("Fresh material the FINALs didn't carry forward," Fresh-1…Fresh-12) and the Part V methodology themes. Critically: the Fresh-N items carry *suggested dispositions* inside this file, but **none of them were actually landed** anywhere — the ledger carries only S16/S17 (the two sentiment rows), and the MANIFEST carries only F1/F2 cohort rows. The Fresh-N "research-seed / soft-polish" suggestions never reached `TODO.md`, `PROPOSALS.md`, or the ledger. So the remainder is genuinely open for adjudication, and the extraction's own suggestions are themselves *stale hints* to test against current canon — which is exactly the gem-hunt frame.

Decisive test applied first-hand throughout: open the actual segment, grep/read, confirm with named loci. Several of the extraction's "research-seed" suggestions turned out **already resolved in canon** (often more richly than the seed proposed) — those are non-losses, not gems. A few are real un-captured slivers.

---

## (A) Ready-to-land

Nothing in this remainder is a drop-in canon edit. The two items closest to "ready" are documentation-of-status corrections (the stale Fresh-5 disposition; the confirmed-landed F1/Fresh-2), and one genuinely-small soft-polish (Fresh-9). I am listing the soft-polish here and the status-corrections under "already-routed-but-now-wrong"; everything substantive is a research-seed.

### A1. Fresh-9 — user-time vs developer-time exchange-rate is implicit at 1:1 (soft-polish, real, un-captured)

1. **What it is, actionably.** TST's continuous-operation extension treats developer-time and user-time as fungible and simply additive (a 1:1 exchange rate). `#scope-continuous-operation` says "downtime is lost time … the temporal optimality postulate therefore applies to operational time as well as development time" and `#def-system-availability` says "from the user's perspective, downtime is lost time" — both *add* user-time to developer-time with no stated conversion factor. For business instantiations the exchange rate is rarely 1:1 (one developer-hour is priced very differently from one user-hour). A half-sentence in `#scope-continuous-operation` Discussion stating that the unification operates at a fixed exchange rate (default 1:1) and that domain instantiations are responsible for stating their own conversion factor would close the implicit-assumption gap.
2. **Loci checked.** `02-tst-core/src/scope-continuous-operation.md:27`; `02-tst-core/src/def-system-availability.md:11,23,27`. The 1:1 fungibility is present and load-bearing; the conversion-factor caveat is **not** present in either. (No `post-temporal-optimality` slug exists; the postulate it refers to is `#post-temporal-optimality`, cross-referenced from these segments.)
3. **Why a gem — wisdom.** Scope-honesty: the framework's pattern is to name its scope assumptions explicitly (the CLAUDE.md "scope precision is the contribution" CS-norm). An unstated unit-conversion baked into an additive objective is precisely the kind of silent assumption the framework otherwise surfaces. Low-effort, raises honesty.
4. **Recommended home.** One clarifying sentence in `#scope-continuous-operation` Epistemic Status or Discussion. Not graduation-blocking. (This is the only Fresh-N item I'd call "ready" in the soft-polish sense; verify the wording against the postulate's own conventions before landing.)

---

## (B) Research-seeds

Ranked by my judgment of value to the theory. Each names the concrete first task.

### B1. Fresh-10 — substrate-dependent functional form of the cognitive-load penalty (AI hard-limit vs human soft-decay) — *the strongest genuinely-un-captured seed*

1. **What it is, actionably.** `#hyp-exponential-cognitive-load` models implementation time as $k^{\text{discontinuities}}$ ($k \gt 1$ compounding per context switch), validated empirically for file-level crossings at $k \approx 1.118$. The entire segment is framed on a **human working-memory substrate** — soft, compounding decay as the developer holds more contexts. An AI agent's context window is structurally different: a *hard* token limit with *perfect* recall inside it. The functional form for an AI substrate may therefore be **step-shaped** (near-zero penalty until tokens exceed the window, then catastrophic) rather than smoothly exponential. This is a substrate-dependence the segment does not name at all.
2. **Loci checked.** `02-tst-core/src/hyp-exponential-cognitive-load.md` (full grep for `substrate|AI|context|token|human|memory`): the segment discusses context-switching, nested dependency, the empirical $k\approx1.118$ — all human-substrate. No AI-vs-human functional-form distinction. Cross-checked `03-llm-core/src/` (`obs-context-turnover`, `disc-m-preservation`, `der-turnover-information-recursion`): these treat *inter-session* model loss at context-window boundaries, **not** the *intra-task* discontinuity-penalty functional form. So the seed is not captured on either side.
3. **Why a gem — strength + wisdom.** AAT's cross-domain generalization claim is one of its load-bearing contributions; a *named, substrate-specific functional-form difference* sharpens that claim rather than weakening it (CS-norm: a more precise scope is more valuable). The step-vs-exponential contrast is also concretely falsifiable — the `empirical-discontinuity/` toolkit already measures the human $k$; an analogous AI-agent measurement would test the step hypothesis directly.
4. **Recommended home.** A Discussion extension in `#hyp-exponential-cognitive-load` (or a short `disc-*`/`hyp-*` in `03-llm-core/`) naming the substrate-dependent functional form. **First task:** decide which component owns it (TST segment Discussion vs a logogenic-side segment), then state the step-shaped-vs-exponential contrast at `hypothesis` tier with the AI-measurement falsification criterion. Pairs naturally with B2.

### B2. Fresh-6 — explicit cognitive-cost ordering across the four opacity regimes (strengthening opportunity)

1. **What it is, actionably.** `#der-agent-opacity` classifies opacity into E-I Broadcast / E-II Selective-signal / E-III Information-hide / E-IV Active-deceive. The segment *already* names that E-IV "requires $A$ to model $B$'s model of $A$" and is "formally reachable only when $A$'s GUC architecture admits modeling another agent's model — typically Class 3 (Coupled) or Class 2 (Partial)" (lines 61, 110). What is **not** stated is the implied **cost ordering across all four regimes**: active deception carries a theory-of-mind infrastructure cost that the other three do not, so the regimes admit a partial cost-ordering (E-IV strictly more expensive; E-III/E-II requiring selective filtration; E-I free). Surfacing that ordering connects opacity-regime choice to the GUC architecture class and to the deliberation-cost machinery.
2. **Loci checked.** `01-aat-core/src/der-agent-opacity.md:20,61,88,110,121`. The modeling-the-observer's-model cost is named *for E-IV specifically* (line 110) and an effects-spiral row exists (line 88, sketch-tier), and line 121 already proposes an opacity ladder for `#disc-separability-pattern`. But the *cross-regime cognitive-cost ordering as such* is not stated. So this is a partial-capture: the hardest piece (E-IV's recursion cost) is in canon; the systematizing ordering is the un-captured sliver.
3. **Why a gem — strength.** Converts a scattered observation (E-IV is expensive) into a structural claim (the four regimes form a cost-ordered lattice tied to GUC class), which is the kind of decomposition CLAUDE.md flags as AAT-native apparatus rather than mere synthesis. It also ties three existing structures together (opacity regimes ↔ GUC class ↔ deliberation cost).
4. **Recommended home.** A short Discussion paragraph or Findings-Brief addition in `#der-agent-opacity`, possibly feeding the proposed opacity-ladder for `#disc-separability-pattern` (line 121). **First task:** state the partial cost-ordering of the four regimes and tie E-IV's theory-of-mind cost to the Class 2/3 reachability already named at line 110, at `discussion-grade`.

### B3. Fresh-5 — Gibbard-Satterthwaite / mechanism-design as a 4th identifiability-floor instance — **SEED IS RESOLVED; flag belongs under "already-routed-but-now-wrong," noted here because the extraction filed it as an open research-seed**

See the "already-routed-but-now-wrong" section. This is the single most important drift-correction in this audit: the extraction file (2026-05-20) suggested `research-seed — new candidate for 4th identifiability-floor instance`. As of current canon it is **fully resolved** — and resolved *better* than the seed proposed. Not an open seed.

### B4. Fresh-11 — Sybil-attack specialization of the transitive-trust limitation (narrow sliver; mostly already captured)

1. **What it is, actionably.** The extraction proposed an adversarial-poisoning extension of `#hyp-communication-gain` (e.g., a Sybil attack where an adversary controls many low-trust sources to manipulate the transitive-trust update). On first-hand read, the segment **already** carries the general gap extensively: line 19 ("the additive model captures the *defender's* response … it does not model the *attacker's* optimization over the defender's trust dynamics"), line 39 (same, in Epistemic Status), line 51–55 (the Bayesian-mixture transitive-trust model), and Working Notes line 61 ("the adversary's strategy … creates a meta-game on trust estimation") and line 63 (the proposed $U_{\text{src}}$/$U_{\text{align}}$ split into estimation-vs-strategic tracks). The **only** un-captured sliver is the *specific Sybil instance* — the structured attack on the *transitive*-trust phase via sock-puppet sources — as a concrete worked instance of the already-named general gap.
2. **Loci checked.** `01-aat-core/src/hyp-communication-gain.md:13,15,17,19,30,33,39,47,49,51,55,61,63`. The general adversarial-trust-poisoning gap and the transitive-trust mechanism are both in canon; the Sybil-specific instance is not named.
3. **Why a gem — modest, wisdom.** Worth recording only as a named example under the existing limitation, not as new machinery. The substance (game-theoretic equilibrium analysis is external to AAT; AAT supplies the state variables) is already correctly scoped.
4. **Recommended home.** At most a one-clause example in `#hyp-communication-gain` Working Notes line 61's meta-game discussion ("…e.g., Sybil/sock-puppet manipulation of the transitive-trust phase"). **First task:** confirm with Joseph whether this is worth even the clause; the general gap is honestly captured already, so this is near the floor of gem-worthiness.

### B5. Fresh-12 — infinite-horizon $V_{O_t}$ vs finite-compute agents (likely already handled; verify)

1. **What it is, actionably.** The extraction flagged that `#form-objective-functional` defines $O_t$ over potentially-infinite trajectories without saying how a finite-compute agent approximates the full infinite-horizon $V_{O_t}$.
2. **Loci checked.** `01-aat-core/src/form-objective-functional.md:62` defers the horizon machinery to `#def-value-object` ("$V_O$, $Q_O$ with horizon and continuation policy"). The C1/C2/C3 receding-horizon convention referenced in the extraction lives there, not in `form-objective-functional`. I did **not** open `#def-value-object` first-hand to confirm the finite-compute approximation is stated there.
3. **Why possibly-a-gem / why possibly-a-non-loss.** If `#def-value-object` already carries the receding-horizon convention as the finite-compute approximation (very likely from the cross-reference), this is a confirmed non-loss and needs no action. If it states the horizon machinery without explicitly tying it to *finite-compute approximation of the infinite-horizon ideal*, a one-sentence Discussion note would close it.
4. **Recommended home / first task.** **First task is a verification, not an edit:** open `01-aat-core/src/def-value-object.md`, confirm whether the C1/C2/C3 convention is explicitly framed as the finite-compute approximation of the infinite-horizon $V_{O_t}$. If yes → confirmed non-loss. If no → one clarifying sentence there. Low priority.

### B6. Methodology seeds (Part V, Themes A/B/E/F) — audit-process material, not theory

1. **What it is, actionably.** The extraction's Part V proposes several additions to `doc/de-novo-audit-instructions.md`: the four-volume continuous-reading discipline (Theme A), watchpoint-discipline-without-defect-promotion as the confirmation-class signature (Theme B), confirmation-class vs detective-class reading-disciplines being *complementary* (Theme E — the canonical evidence is 849201 *not* catching the Model-S ever-exit and the score-sign error that 742613/613842 *did* catch), and running-outline-as-forward-synthesis-scaffold (Theme F).
2. **Loci checked.** These are audit-methodology, not canon segments. The complementary-reading-disciplines point (Theme E) is the most valuable and is *already* partially captured in the 2026-05-29 gem-hunt's own P-block (per STATUS.md "audit-methodology → ledger P-block"). I did not re-read the P-block to confirm whether the confirmation-vs-detective complementarity is already there.
3. **Why a gem — wisdom (process).** Theme E in particular is a real methodological insight: audit-cohort coverage is *jointly* held by multiple reading-disciplines, and a confirmation-class read praising the math is not evidence the math is correct (849201 praised both the Model-S bound and the score-sign formula, both of which carried bugs caught elsewhere). That is load-bearing for how Joseph weights future audit verdicts.
4. **Recommended home.** `audits/polish-and-sentiment-ledger.md` P-block (audit-methodology) and/or `doc/de-novo-audit-instructions.md`. **First task:** check whether the P-block from the 2026-05-29 cycle already records "confirmation-class praise ≠ correctness; detective-class reading is complementary and necessary"; if not, add it citing the 849201 Fresh-1/Fresh-2 negative-space data as the worked example.

---

## Already-routed-but-now-wrong dispositions

### W1. Fresh-5 (Gibbard-Satterthwaite as candidate 4th identifiability-floor instance) — extraction said `research-seed (open)`; current canon = **fully resolved, and resolved better**

This is the headline drift-correction. The extraction file (2026-05-20) dispositioned Fresh-5 as `research-seed — new candidate for 4th identifiability-floor instance, parallel to 471203 Fresh-5 (Fano)`. Against **current** canon that is stale and wrong:

- The mechanism-design impossibility cluster (Gibbard-Satterthwaite 1973-75; Myerson-Satterthwaite 1983; Arrow 1951) was **tested against the five-element shape and resolved**, via `spikes/.integrated/spike-4th-identifiability-floor-instance-2026-05-20.md §4`.
- It landed **not** as a 4th instance of `#disc-identifiability-floor`, but as a **sister meta-pattern** `#disc-implementation-impossibility` carrying three charter instances: `#deriv-strategy-proofness-impossibility` (GS), `#deriv-bilateral-trade-impossibility` (MS), `#deriv-social-welfare-aggregation-impossibility` (Arrow).
- The resolution is *more sophisticated* than the seed proposed: the **actor-positioning distinction** (agent-frustrated/agent-escaping via information-augmentation → `-floor`; designer-frustrated/design-constraint-relaxation, combinatorial-topological mechanism per Reny 2001 → `-impossibility`) is the reason it is a peer sister-pattern rather than a nested 4th instance. The agent-side/designer-side suffix discipline (`-floor` vs `-impossibility`) tracks the distinction at canon naming-pattern depth.
- **Loci (first-hand):** `01-aat-core/src/disc-identifiability-floor.md:143-145` (the explicit "Mechanism-Design Impossibility (landed in `#disc-implementation-impossibility`, not an Instance here)" subsection) and line 181 (the methodology's candidate-future-floor list still *names* "mechanism-design impossibility" — that line is itself slightly stale now that it has landed as a sister pattern, worth a glance).
- **Recommendation:** retire Fresh-5 as a research-seed. It is a **non-loss / confirmed-resolved**. The hard-constraint test ("would we have to re-derive this later?") passes — the content is in canon. The only residual: `disc-identifiability-floor.md:181`'s Brief still lists "mechanism-design impossibility" among *candidate future floors*, which now reads as not-yet-done when it is done-as-sister-pattern; a one-word tightening there would remove the false-openness, but it's cosmetic.

### W2. Fresh-8 (AI-substrate truncated-search vs human-stress failure mode) — extraction said `research-seed`; current canon = **already captured in canon Working Notes**

The extraction filed Fresh-8 as an open research-seed (substrate-dependent failure modes in the TST vicious/virtuous bifurcation). Current canon already carries it: `02-tst-core/src/der-code-quality-as-observation-infrastructure.md:136` Working Notes state verbatim — *"A skilled developer under time pressure may produce lower-quality code, but an AI agent under time pressure might not — it has no fatigue, no shortcuts-from-stress. The vicious cycle may be more human-specific than the formalism suggests."* That is precisely the Fresh-8 insight. **Non-loss / confirmed-captured.** (The deeper bifurcation formalization — 2D dynamical model with a separatrix — is separately and correctly tracked at `spikes/PROPOSED.md` Tier 3 per line 135, so the *strengthening* direction is also already routed.)

### W3. BP16 / Fresh-cluster (Auftragstaktik AI-inversion: $B_M$ cheap for AI, $B_O$ hard) — extraction preserved as bigger-picture; current canon = **already captured**

`01-aat-core/src/hyp-auftragstaktik-principle.md:60` Working Notes already state: *"The principle may need qualification for AI agent teams where model synchronization is cheap (shared vector databases, persistent memory) but objective alignment is hard (prompt engineering, RLHF). The cost structure differs from human organizations."* Confirmed non-loss.

---

## Confirmed non-losses (already in canon, with loci) — F1/Fresh-2 and the dispositioned trail

The extraction's own first-hand verifications, re-confirmed against current `src/`:

- **F1 (Opacity-Gain Tension) — resolved by strengthening; in canon.** `01-aat-core/src/emp-update-gain.md:17,50` carry the "Resolving Epistemic Opacity" resolution (gain as endogenous state variable; agent estimates $U_o$/$U_M$ from its own innovations; proof in `#deriv-adaptive-gain-dynamics`). This is the strengthen-first third-option (neither bridging-hypothesis nor axiom-softening, which were the audit's two recommendations) — confirmed correct disposition, durable worked example.
- **Fresh-2 (score-sign error) — fixed; in canon.** `01-aat-core/src/def-mismatch-signal.md:14,40` carry $\tilde\delta_t = \nabla_M \log P(\dots)$ with **no** minus sign, plus prose ("points in the direction the model should move to increase the likelihood"). The 742613-F1 fix landed; the 849201 auditor's *not-catching* (it praised the pre-fix minus-sign form) is correctly preserved as confirmation-class negative-space data.
- **All Part I (F1-trail … F2-TST) and Part II (BP1-BP19)** — `subsumed-by-FINAL`/`subsumed-by-MANIFEST`, soft → ledger S16/S17. These are confirmation-class structural-triumph ratifications, not defects; correctly routed in the 2026-05-16 Cluster D MANIFEST. I spot-verified the dispositions are internally consistent and did not re-open every cited segment (the burden-of-proof rows were explicitly *not* exhaustively re-grepped, consistent with the gem-hunt scope).
- **Fresh-1 (Model-S ever-exit not caught)** — the underlying Model-S issue resolved by strengthen-then-no-go (Cor A.1S.1 + `#deriv-stochastic-non-exit`) per Cluster B; the 849201 not-catching is negative-space methodology data, correctly preserved.
- **Fresh-3 (biological-sleep analogy)** — cross-cycle re-ratification of 471203 Theme E; not fresh.
- **Fresh-4 (action-fluency marker)** — convergence with 742613 Fresh-1; same segment-element, both framings partially right; already tracked there.
- **Fresh-7 (sufficient-statistics-span)** — lives in the segment's own Working Notes per the auditor's reading; not new fresh material.

---

## Valueless / superseded

- **Fresh-5's original framing** (GS as a *4th instance of the identifiability floor*) is superseded by the actor-positioning resolution that made it a *sister pattern* (`#disc-implementation-impossibility`). The original framing would have been a category error (it conflates agent-side data-inference floors with designer-side construction impossibilities); canon correctly distinguishes them. Locus: `disc-identifiability-floor.md:143-145`.
- **Part IV (predictions calibration register)** — cognition-flow data, not findings; the calibrated-high value-feeling distribution is already integrated at cohort-sentiment level (ledger S16). No extraction needed.
- **Theme D (structural-triumph catalog as methodology artifact)** — subsumed by the honesty-as-architecture framing (ledger S10) + S16/S17. No fresh content.

---

## Coverage summary and honest limits

**Read first-hand from `src/` this cycle:** `01-aat-core/src/disc-identifiability-floor.md` (full — the W1 drift-correction); `emp-update-gain.md:17,50`; `def-mismatch-signal.md:14,40`; `der-agent-opacity.md` (grep + key lines); `hyp-communication-gain.md` (full grep); `der-code-quality-as-observation-infrastructure.md:136` (Fresh-8 W2); `hyp-auftragstaktik-principle.md:60` (W3); `hyp-exponential-cognitive-load.md` (full grep — B1/Fresh-10); `scope-continuous-operation.md` + `def-system-availability.md` (Fresh-9/A1); `form-objective-functional.md:62` (Fresh-12 pointer). Cross-checked `03-llm-core/src/` for cognitive-load/turnover overlap.

**Read first-hand from `audits/`:** the full `audit-findings-849201.md` (both pages); `STATUS.md`; `polish-and-sentiment-ledger.md` (S16/S17 grep); `.integrated/MANIFEST.md` (Cluster D grep).

**Honest deferrals (would change disposition for at most B5):**
- `01-aat-core/src/def-value-object.md` — not opened; B5 (Fresh-12) hinges on whether it frames C1/C2/C3 as the finite-compute approximation. Stated as a verification first-task, not an edit.
- `01-aat-core/src/deriv-adaptive-gain-dynamics.md` proof contents — accepted the body-text reference + MANIFEST disposition for F1 (consistent with the extraction's own scope).
- The 2026-05-29 P-block was not re-read to confirm whether Theme E (confirmation-vs-detective complementarity) is already recorded (B6).

**Bottom line.** This file was already mined to the MANIFEST level, so the gem yield is thin-by-design (confirmation-class cycle). The genuinely un-captured remainder is small but real: **B1 (substrate-dependent cognitive-load functional form)** is the one I'd most want landed — a falsifiable sharpening of AAT's cross-domain claim that exists nowhere in canon. **A1 (exchange-rate caveat)** and **B2 (opacity-regime cost ordering)** are honest scope/structure improvements. **W1 (Fresh-5 now resolved as a sister meta-pattern)** is the most important *correction* — an extraction-time research-seed that current canon has overtaken, exactly the drift the gem-hunt frame predicts. No gem was manufactured; the bulk of Part III turned out to be already-captured non-losses, which I have documented with loci rather than dressed up as findings.
