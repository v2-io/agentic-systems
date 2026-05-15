---
slug: spike-strategic-equilibrium-wording-precision
type: spike
status: working
date: 2026-05-12
related_segments:
  - deriv-strategic-composition
  - scope-composite-agent
  - disc-identifiability-floor
related_findings:
  - codex-audit-2026-05-12 AAD-7
related_spikes:
  - spike-strategic-composition  (2026-04-24; established the α'/β' sub-scope decomposition this spike refines)
---

# Spike: Strategic Equilibrium — Wording Precision Across `#deriv-strategic-composition`

**Status.** Precision-pass spike, openend in response to Codex audit finding AAD-7 (`msc/codex-audit-results-2026-05-12.md`). Outcome: **succeed at claim** — the segment's theoretical apparatus is sound; the imprecision is at the prose layer where headline language elides distinctions the segment makes correctly elsewhere. No new sub-scope, no new theory, no new derivation. A small set of exact edits across three segments closes the gap.

**Trigger.** AAD-7 (audit, line 175):

> The alpha-prime/beta-prime split is strong. Potential and monotone games legitimately transfer sector/Lyapunov machinery. However, the "no equilibrium exists" language for cyclic games can be misleading: finite games generally have mixed Nash equilibria, and no-regret dynamics can converge to correlated or coarse-correlated sets even when pure-strategy dynamics cycle.

Specifically, line 162 of `01-aat-core/src/deriv-strategic-composition.md`:

> **No equilibrium exists** in cyclic games (rock-paper-scissors pure-strategy Nash; mixed-Nash saddle of fictitious play). Strategic composition has no fixed point; ergodic / distributional analysis replaces convergence.

The headline "**No equilibrium exists**" is wrong as stated; the parenthetical partially corrects it ("rock-paper-scissors pure-strategy Nash; mixed-Nash saddle of fictitious play") but reads as if the writer means "no equilibrium that's a state-space fixed point of best-response dynamics" rather than "no equilibrium at all." Nash 1950 covers mixed equilibrium for finite games universally; Hart–Mas-Colell 2000 covers CCE convergence in distribution for any game under no-regret learning. Both are already cited correctly upstream in the same segment (lines 60–68 and 149).

---

## §1 — Map of where the precision holds and where it slips

Reading the segment top-to-bottom, the α'/β' decomposition handles the distinctions cleanly in three places, then drops them in two.

### Where precision holds

- **Line 60–62 (sub-scope β' VI existence).** "Every strategic interaction with continuous strategy spaces and regular payoffs can be reformulated as a **variational inequality** ... When $\mathcal K$ is compact-convex and $F$ is continuous, a solution exists (Hartman–Stampacchia theorem). **Pure-strategy Nash equilibrium existence is therefore guaranteed** for continuous-strategy games with compact convex strategy sets and continuous payoffs. But the VI framework gives *existence* only, not *convergence of any specific dynamic to the solution*; solutions may be non-unique." — Existence vs convergence cleanly distinguished.

- **Line 64–68 (regret-minimization → CCE).** "Under no-regret learning (e.g., Hedge / multiplicative weights, Freund–Schapire 1997), the empirical joint distribution converges to the set of **coarse correlated equilibria** (CCE) at rate $O(1/\sqrt T)$. This requires no structure on the game beyond each sub-agent computing its own regret." — Distributional / empirical-joint convergence, correctly stated, applies to *any* finite game.

- **Line 149 (Epistemic Status §).** "AAD does not claim to predict equilibrium selection under multiple Nash, short-run dynamics in cyclic games (rock-paper-scissors), or convergence rates better than $O(1/\sqrt T)$ in $\beta'$." — This is the careful version: "short-run dynamics in cyclic games" is what's not predicted; existence and distributional convergence are not denied.

### Where precision slips

- **Line 162 (Honest Limits — primary defect).** "**No equilibrium exists** in cyclic games (rock-paper-scissors pure-strategy Nash; mixed-Nash saddle of fictitious play). Strategic composition has no fixed point; ergodic / distributional analysis replaces convergence." — The bolded headline is false-as-stated. Mixed Nash exists for finite games (Nash 1950); CCE always exists and is reachable under no-regret dynamics (Hart–Mas-Colell 2000). What is true is the *parenthetical*: no pure-strategy Nash in some cyclic games (rock-paper-scissors is the canonical example), and the mixed-Nash is a saddle of fictitious play — i.e., not stable under naive best-response. The headline conflates three claims that should be kept separate.

- **`#scope-composite-agent` line 69 (related slip).** "Adversarial pairs that admit Nash / CCE convergence via (C-iv) DO satisfy composition-scope-condition as strategic composites; adversarial pairs in cyclic / non-convergent regimes do not." — Imprecise in the same way. Cyclic games *do* admit CCE convergence under no-regret learning; "cyclic" and "non-convergent" are not synonyms. The category that genuinely fails (C-iv) is something narrower: games where no equilibrium concept whatsoever has reachable support, which is rare to nonexistent in the standard game-theoretic landscape (any finite game has Nash and CCE; any compact-convex continuous game has Nash via Hartman–Stampacchia).

- **`#disc-identifiability-floor` Instance-4 footnote (separate slip, surfaced en route).** Line 137 of `deriv-strategic-composition.md` says "Mechanism-design impossibility as candidate 4th `#disc-identifiability-floor` instance" — but Instance 4 of `disc-identifiability-floor.md` is now occupied by "Universal Information-to-Distance Constant under Non-(PI) Norms" (the bias-bound result from the 2026-04-24 cycle). Mechanism-design impossibility is correctly listed in `disc-identifiability-floor.md` line 120 under "Adjacent Floors (Open Research Directions)" as a candidate, not numbered. The "4th instance" language in `deriv-strategic-composition.md` is stale; it should read "candidate adjacent floor" or "candidate 5th instance" matching the current numbering. This is a stale-cross-reference defect, not a theory defect.

---

## §2 — Strengthening attempt: is there a γ' sub-scope for cyclic-distributional equilibria?

Per project posture (strengthen before soften), the spike attempts the strengthening before falling back to wording-only.

**Attempt.** Define a hypothetical sub-scope γ': games where no pure-strategy Nash exists but mixed Nash and/or CCE do exist, and the strategic composition's macro-state is the *equilibrium distribution* rather than an equilibrium *point*.

**Why this collapses into β'.** Sub-scope β' is already defined (segment lines 58–68) as the regime where the regret-minimization machinery applies and the strongest claim is CCE set-convergence. Cyclic games (rock-paper-scissors and its generalizations) are paradigmatic β' instances: no monotonicity, no potential, but Hart–Mas-Colell 2000 still gives empirical distribution → CCE. Adding γ' as a third sub-scope between α' and β' would create a distinction without a difference — γ' would have the same machinery (regret-min), the same convergence guarantee (CCE), and the same rate ($O(1/\sqrt T)$) as β'. The only "new" content would be naming "the macro-state is the distribution, not a state" — and that's already implicit in CCE being a distributional object.

**What does sharpen the picture (and stays within the existing α'/β' decomposition).** Under β', the macro-state of a strategic composite is the *empirical-play distribution* converging to CCE support, not a state-space point. This is a structural property of β' worth surfacing explicitly — it's currently implicit and the elision is exactly what makes line 162 wrong. The fix is to make β' explicitly about *distributional* equilibrium objects (CCE; mixed Nash where it exists) instead of leaving the type-of-object implicit. No new sub-scope; the existing β' just gets its macro-state type stated.

**Strengthening verdict.** No γ' sub-scope is warranted. β' already covers cyclic games; the precision gap is at the language layer in three specific places (line 162, the `#scope-composite-agent` "cyclic/non-convergent" gloss, and the stale Instance-4 cross-reference). Wording-only repair is the right shape.

A potential *separate* theoretical strengthening — explicitly stating in the segment that **CCE existence is universal for finite games** (Hart 2005 *Adaptive Heuristics* lecture; survey: Hart 2005, *Econometrica* 73:1401) and **mixed-Nash existence is universal for finite-strategy-set games** (Nash 1950) — would tighten the segment's β' framing but isn't a *new* result and shouldn't be promoted as a new sub-scope. Recommend folding the universality observation into β' framing prose, not as a new derived result.

---

## §3 — Recommended edits (segment-voice; no diff voice; future readers as audience)

These are wording recommendations for a follow-on cycle under Joseph's review. The spike does not modify any segment.

### Edit 1: `01-aat-core/src/deriv-strategic-composition.md` line 162 — primary repair

**Current text (line 162):**

> **No equilibrium exists** in cyclic games (rock-paper-scissors pure-strategy Nash; mixed-Nash saddle of fictitious play). Strategic composition has no fixed point; ergodic / distributional analysis replaces convergence.

**Recommended replacement:**

> **No pure-strategy Nash equilibrium** in cyclic games (rock-paper-scissors; matching pennies). Mixed-Nash equilibrium exists universally for finite games (Nash 1950) but is a saddle point of best-response dynamics rather than a basin attractor; fictitious play orbits the mixed-Nash without converging pointwise to it. No-regret dynamics still drive the *empirical joint distribution* to the CCE set at rate $O(1/\sqrt T)$ (Hart–Mas-Colell 2000), so β' machinery applies; the macro-state of a strategic composite in this regime is a distribution over the strategy space, not a state-space point.

**Rationale.** Preserves the honest scope-limit content (no pure-strategy convergence, no state-space fixed point) while removing the false headline. Names mixed-Nash existence explicitly. Locates cyclic games as β' (which they are) rather than as a separate exit. Makes explicit the type-of-object distinction (distribution vs state) that the original elided.

### Edit 2: `01-aat-core/src/deriv-strategic-composition.md` line 137 — stale cross-reference repair

**Current text (line 137, in the "What Is Derived vs. What Is Chosen" table):**

> | Mechanism-design impossibility as candidate 4th `#disc-identifiability-floor` instance | Gibbard-Satterthwaite 1973-75, Arrow 1951, Myerson-Satterthwaite 1983 | Flagged; not derived in this segment |

**Recommended replacement:**

> | Mechanism-design impossibility as candidate adjacent-floor instance in `#disc-identifiability-floor` | Gibbard-Satterthwaite 1973-75, Arrow 1951, Myerson-Satterthwaite 1983 | Flagged; not derived in this segment |

**Same correction in §Discussion (line 177):**

**Current:**

> Impossibility results — Gibbard-Satterthwaite 1973–75 (...); Myerson-Satterthwaite 1983 (...); Arrow 1951 (...) — are **candidate fourth instances of `#disc-identifiability-floor`**: external theorems forbidding design-of-alignment under stated constraints, with AAD machinery (Bayes-Nash relaxation, randomized allocations, subsidy injection) as structural escapes. Flagged for future follow-up spike; not derived in this segment.

**Recommended replacement:**

> Impossibility results — Gibbard-Satterthwaite 1973–75 (...); Myerson-Satterthwaite 1983 (...); Arrow 1951 (...) — are **candidate adjacent-floor instances of `#disc-identifiability-floor`**: external theorems forbidding design-of-alignment under stated constraints, with AAD machinery (Bayes-Nash relaxation, randomized allocations, subsidy injection) as structural escapes. Flagged for future follow-up spike; not derived in this segment.

**Rationale.** Instance 4 of `#disc-identifiability-floor` is currently occupied by "Universal Information-to-Distance Constant under Non-(PI) Norms" (landed in the 2026-04-24 Bias-Bound cycle). Mechanism-design impossibility is correctly listed at `disc-identifiability-floor.md` line 120 in the "Adjacent Floors (Open Research Directions)" section, not numbered. The "4th instance" claim in `deriv-strategic-composition.md` predates the bias-bound landing and is now stale. Using "candidate adjacent-floor instance" matches the current numbering discipline without committing to a specific future ordinal.

### Edit 3: `01-aat-core/src/scope-composite-agent.md` line 69 — companion wording repair

**Current text (line 69, "What fails the scope condition"):**

> **What fails the scope condition:** sub-agents with orthogonal objectives that also fail to admit equilibrium convergence (no shared or derivable $O_c$, no relevance variable providing mutual benefit, no equilibrium structure the strategic dynamics converge to — e.g., cyclic games with no pure Nash), or unclassifiable objective-structure coupling. Such systems remain within #scope-multi-agent but not #scope-composite-agent. Adversarial pairs that admit Nash / CCE convergence via (C-iv) DO satisfy composition-scope-condition as strategic composites; adversarial pairs in cyclic / non-convergent regimes do not.

**Recommended replacement:**

> **What fails the scope condition:** sub-agents with orthogonal objectives that also fail to admit equilibrium convergence — no shared or derivable $O_c$, no relevance variable providing mutual benefit, and no equilibrium concept (pure Nash, mixed Nash, or CCE) whose support the coupled best-response or no-regret dynamics reach — or unclassifiable objective-structure coupling. Such systems remain within #scope-multi-agent but not #scope-composite-agent. Adversarial pairs that admit equilibrium convergence via (C-iv) — whether pure-strategy Nash under α' (potential / monotone games), mixed Nash under β' (Nash 1950 existence for finite games), or CCE in distribution under β' (Hart–Mas-Colell 2000) — DO satisfy composition-scope-condition as strategic composites. Cyclic games (rock-paper-scissors, matching pennies) lack a pure-strategy Nash but admit mixed Nash and CCE convergence; they fall within β' and satisfy (C-iv). The narrow category that fails (C-iv) is games with no equilibrium concept whose support is reachable by any admissible dynamic — a genuinely small class within the standard game-theoretic landscape.

**Rationale.** Removes the false "cyclic / non-convergent" equation. Names which dynamics give which equilibrium concept (clarifies the type-of-object as we go). Acknowledges that the (C-iv)-fails category is narrow — most adversarial and cyclic interactions admit *some* equilibrium convergence and therefore *do* satisfy (C-iv) — which is faithful to the scope condition's intent and removes the implicit overclaim that cyclic = non-composite.

### Optional Edit 4: small β' framing addition in `01-aat-core/src/deriv-strategic-composition.md` around lines 64–68

The current β' description focuses on convergence rate and structural minimality but doesn't name the type-of-object the equilibrium concept is. Adding one sentence to the β' paragraph would make line 162's distributional framing read as a natural continuation rather than a surprise.

**Recommended addition after line 67 (the regret-minimization paragraph):**

> Under β', the macro-state of a strategic composite is a *distribution* on the joint strategy space — the empirical joint play whose support is the CCE — rather than a state-space point. This is the structural shape of "convergence" in the β' regime: distributional convergence, not pointwise. Pure-strategy Nash may or may not exist (cyclic games — rock-paper-scissors, matching pennies — lack pure Nash but retain mixed Nash via Nash 1950 and CCE convergence via Hart–Mas-Colell 2000); the β' machinery's guarantees are at the distributional layer regardless.

**Rationale.** Surfaces the distribution-vs-point type distinction at the place where it's first relevant. Pre-empts the need for the audit-flagged "no equilibrium" headline in Honest Limits by making the type distinction load-bearing in β' framing. The recommendation in Edit 1 then reads as cataloging an example of β' rather than as a separate exit.

This edit is optional in the sense that Edits 1–3 close the audit finding by themselves; Edit 4 is the *strengthening* of the β' framing that makes the whole picture more coherent. Recommend including it.

---

## §4 — What was not changed (and why)

- **No γ' sub-scope.** Strengthening attempt §2 closed: cyclic games are β', not a third sub-scope. The α'/β' decomposition is the right granularity.
- **No new derived result.** The CCE-universality and mixed-Nash-universality observations are imported (Nash 1950; Hart–Mas-Colell 2000) and were already imported at lines 62 and 64–68. The recommendation makes them explicitly framed; no new theorem is derived.
- **No change to the "(SC-1)/(SC-2)/(SC-3)" decomposition.** (SC-1) existence, (SC-2) stability, (SC-3) reachability remain the right three questions. Edit 1 doesn't restructure them.
- **No change to the Cournot worked example or the zero-sum scalar example.** Both are α' instances; the precision issue lives in β' wording and doesn't touch the worked examples.
- **No change to `#disc-identifiability-floor`'s numbered instances.** The stale-cross-reference repair (Edit 2) only updates `deriv-strategic-composition.md`'s references *to* `disc-identifiability-floor.md`, not the latter segment. The "candidate adjacent-floor instance" language matches what `disc-identifiability-floor.md` already says at its line 120.
- **No promotion of mechanism-design impossibility to an actual numbered instance.** That remains future-spike work; this spike only fixes the stale ordinal.

---

## §5 — Completion state and promotion recommendation

**Completion state.** Succeed at claim — wording-only precision pass, three (optionally four) specific edits. The α'/β' decomposition is theoretically sound; the imprecisions are at three specific prose locations where headline language elides distinctions the segment makes correctly elsewhere.

**Strengthening attempted before settling on wording-only.** §2 records the γ'-sub-scope attempt and its collapse into β'. The fallback to wording-only is honest in the sense the working-conventions doc requires.

**Promotion recommendation — exact edits to land in a follow-on cycle under Joseph's review:**

1. **`01-aat-core/src/deriv-strategic-composition.md` line 162** — replace the "no equilibrium exists" Honest-Limit bullet with the precise three-tier statement (no pure-strategy Nash / mixed-Nash exists but saddle / CCE convergence in distribution). Primary fix; closes AAD-7 directly.

2. **`01-aat-core/src/deriv-strategic-composition.md` lines 137 and 177** — update "candidate 4th `#disc-identifiability-floor` instance" → "candidate adjacent-floor instance". Stale-cross-reference cleanup; surfaced en route. Decoupled from AAD-7 in origin but cheap to land in the same pass.

3. **`01-aat-core/src/scope-composite-agent.md` line 69** — rewrite the "What fails the scope condition" paragraph to remove the "cyclic / non-convergent" equation and to name which equilibrium concept each sub-scope provides. Companion repair; the original AAD-7 wording slip propagated here in the route-count-consistency sweep.

4. **(Optional) `01-aat-core/src/deriv-strategic-composition.md` lines 64–68** — add one sentence to the β' paragraph explicitly naming the macro-state-as-distribution structural shape. Strengthens the β' framing so Edit 1 reads as a natural continuation. Recommended.

**No theoretical change.** No new segments, no new derivations, no new sub-scope routes.

**No-op fallback.** If, on Joseph's review, Edit 1's replacement reads as overcorrection (Edit 1 names more equilibrium concepts than the Honest-Limit paragraph wants to carry), a minimal repair would replace just the bolded "**No equilibrium exists**" headline with "**No pure-strategy Nash equilibrium**" and leave the rest unchanged. This is enough to close AAD-7 at minimum. The full Edit 1 is the more thorough version that surfaces the type-of-object distinction explicitly.

---

## Working Notes

- **Audit context.** AAD-7 is one of several findings in the 2026-05-12 Codex audit; the broader audit pass surfaces editorial / status-propagation issues across the four monographs. AAD-7 is unusually clean to dispatch because the segment's apparatus is right and only headline language needs precision. See `msc/codex-audit-results-2026-05-12.md` and the surrounding intake context at the bottom of `TODO.md`.

- **Inheritance from `spike-strategic-composition`.** The α'/β' decomposition this spike refines was established by `spikes/spike-strategic-composition.md` (2026-04-24) and promoted to the current `#deriv-strategic-composition` segment in the 2026-04-24 cycle. This spike inherits that segment's framing and adds only precision to its β' prose; the strengthening attempt for a third sub-scope (§2) is what's new, and it closed negative.

- **Project posture.** Strengthen-before-soften discipline applied at §2 (γ' sub-scope attempted, collapsed into β'). The completion state is "succeed at claim" rather than "succeed beyond claim" precisely because the strengthening attempt closed without yielding new theory — the existing α'/β' decomposition is already as fine-grained as the regret-minimization literature supports.

- **Cross-reference to `#disc-identifiability-floor`.** The "candidate adjacent-floor instance" framing for mechanism-design impossibility is consistent with `disc-identifiability-floor.md` line 120's "Adjacent Floors (Open Research Directions)" section. If mechanism-design impossibility is later promoted to a numbered instance (it would be Instance 5 under the current numbering), this segment's cross-reference would need to be updated again — but at that point the segment that promotes it should sweep all upstream cross-references.

- **What this spike does not establish.** It does not promote any new theorem, does not derive mixed-Nash universality (Nash 1950 is imported), does not derive CCE-universality (Hart–Mas-Colell 2000 is imported), and does not promote mechanism-design impossibility to a numbered floor instance. All four of those are correctly cited as imports / candidates, and the spike's recommendation respects those statuses.

- **Possible follow-on spike.** If `#disc-identifiability-floor` is revisited in a future cycle to promote mechanism-design impossibility from "adjacent floor" to "numbered instance," that spike should also sweep `deriv-strategic-composition.md` Discussion §"Mechanism-design impossibility" and update the cross-reference to the new instance number. This is decoupled from AAD-7 and out of scope for the current spike.
