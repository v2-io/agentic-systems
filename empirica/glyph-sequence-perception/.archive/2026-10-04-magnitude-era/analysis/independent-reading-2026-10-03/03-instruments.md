# 03 — What the instruments can and cannot tell apart

These are the measurement properties of the v1.0 instruments as these data reveal them. Each item names the evidence. None of them says the instruments are useless. They say which questions a given number can answer.

## 1. ⟂ separates "commit" from "decline". It does not separate "not perceived" from "below this judge's threshold".

- **Same stimulus, different judges.** Signa's 30 seam pairs draw ⟂ on 0/30 (sonnet55, sheet) up to 25/30 (both Geminis) (`01-signa.md`). On uniform-random triads every frontier judge is at 0.73–0.99 ⟂. On fresh-seed-local format pairs they are at 0.05–0.24 (`tables/perp-rates.txt`). The ⟂ rate ranks *stimulus classes* consistently across judges, but its level is a judge property.
- **Same model, different condition.** On pilot-replication presentations, sonnet55 as a clean API judge says ⟂ on 0.41 single and 0.47 sheet (dissolution 0.28 and 0.35). As a Claude Code subagent it says ⟂ on 0.76 (dissolution 0.58) (`tables/pilotcond.txt`). That arm ran with the pilot's wording, default effort, 80-item sheet files, and the user's global instruction context loaded. The context includes extensive truth-honoring and anti-confabulation language; that it matters is plausible, not shown. The pilot's own 0.80 came from a condition that also put **both orders of every pair on the same sheet**, answered in one call. v1.0 and the arm both split orders across sheets. The pilot had about 1% mixed pairs; the arm has 14%. Same-sheet pairing can by itself turn inconsistent half-⟂ pairs into consistent-⟂ pairs (verifier §1).
- **What is removed is shared signal, not noise.** Edges that a frontier judge dissolves under ⟂ get the same forced-choice winner from *other-family* frontier judges 83% of the time (3338/4008; chance 50%; for surviving edges 97%) (`tables/manufactured-edges.txt`). So the ⟂ option suppresses a weak ordering that is common across model families. The instruments cannot tell whether that ordering is *felt but faint* or a *shared heuristic construction* (for example "the more complex glyph is more"). Both would look identical here.

## 2. The triad cycle rate cannot distinguish intransitivity from slot preference.

Each orientation set presents AB, BC, CA (or the reverse), a cyclic arrangement. In a cyclic set, the two possible 3-cycles are exactly "the first-shown symbol wins all three" and "the second-shown wins all three". So every counted cycle is a pure position pattern, and a judge that answers by slot produces a cycle every time. sonnet5's 0.17 cycle rate goes with P(first | directed) = 0.33. qwen25's 0.45 goes with 0.72 (`tables/triad-position.txt`). A *high* cycle rate can also come from stimulus-independent answering without any aggregate slot bias: gemma's P(first | dir) is 0.52 and its cycle rate 0.23. So only near-zero rates are cleanly interpretable. Requiring each pair to be consistent across its two orientation sets removes slot effects. On that basis, **0 cycles occur in any judge's fully order-stable triads**: 0/94 opus, 0/87 sonnet55, 0/33 llama, and so on (`tables/triad-transitivity.txt`). The pilot used the same cyclic unit. Its llama run had P(first | dir) 0.763 and cycle rate 0.369, which is the "37%" (verifier). The pilot's 3B-vs-Sonnet contrast is therefore at least partly a slot-preference contrast. Small-model order-stable triads are few (llama 33, gemma 8), so transitivity beyond them is unmeasured.

## 3. Gestalt |τ| over shared glyphs rewards leaving glyphs out, and has no complexity baseline.

- **Exclusion.** τ is computed over the glyphs the judge kept. Moving awkward glyphs to EXTRA raises τ. Examples: signa (τ = 1.00 at coverage 0.55 for opus, both Geminis and grok), the pilot's unfold (opus `|)}> EXTRA -=`, τ = 1.00) and the drain (haiku, trigrams only, τ = 1.00). Coverage, or the partition itself, has to be reported with τ.
- **Generic ordering of arbitrary sets.** On the random noise foils, frontier judges produced an order 36% of the time. Different families often produced the *same* order: noise-2 `᳂𐤨꠶𖪛𒉨` from haiku, sonnet55 and grok, and every frontier answer to noise-3 starts with the ogonek `˛` (`tables/p13.txt`). So any set of glyphs has a weak shared "visual complexity" order. A high τ for an authored sequence is strong evidence only to the extent that it beats what that generic order would give. v1.0 has no such baseline.
- **Partition vs order.** With an EXTRA option, a judge facing a two-family set can split it into one order plus extras, or concatenate the families. τ can't tell these apart. Signa shows judges doing both, sometimes the same judge on different shuffles (sonnet55).

## 4. Value- and ink-correlates are bounded by how they are measured.

- "Ink" is Ghostty/VictorMono `packed_density`, a pixel measure of one terminal's font stack. Judges see code points, never pixels. Where the measure and judges disagree, the measure can be the one that's off. Examples: `◎` has more ink than `◉`, but every judge says `◉` is more. `☷` has less ink than `⚌`, but judges say `☷` is more (line count).
- "Value" is the UCD numeric property. Dice (`⚄`) have none, so dice comparisons count as "ink". `⚄` vs `5` is an equal-value probe only by designer annotation.
- Edge counts behind these correlates are 20–120 per judge. Small-model ink-correlates of 0.28–0.55 come with much unparsed and slot-driven data (P8).

## 5. The answer channel causes missing data that is not missing at random.

- haiku45 can't reproduce `⬤` (U+2B24) and emits neighbouring code points. Every such answer is unparsed, and almost all of them were "⬤ is more", so `⬤`'s apparent rank drops for that judge (`01-signa.md`).
- The small models' unparsed rates are large: phi4mini 0.21–0.27 of format presentations; qwen25 up to 0.40 under tie (239/593). Their "verdict" distributions describe the answerable subset.
- Parser p1.3 is conservative: exactly one answer signal, or unparsed. That is right for not imputing. It means per-judge comparisons partly compare channel competence.

## 6. One presentation per order; provider-default temperature.

Pair instruments ran one rep (conflict ran three for API judges). A within-judge flip can therefore be either sampling noise or a tie resolved by slot. Every flip is "same-slot" by definition, so that can't help. Separating the two needs reps. The conflict battery's three reps show real within-judge variation for some Claude cells: `sub8-vs-3` sonnet5 `3×4 ₈×1 ⟂×1`; `seg-0-vs-7` sonnet5 `🯷×3 🯰×3` (`tables/conflict-items.tsv`).

## 7. Judge identity is confounded with harness and effort.

grok, codex and agy carry 12–14k-token harness preambles. Claude CLI judges see an account note. On signa, Gemini 3.1 Pro used about 2,300 thinking tokens per 40-item sheet (about 58 per item). opus55 reported 0 on 109 of 110 calls and 52 on one, and per-instrument means elsewhere ran from 2.2 (holistic) to 134 (signa gestalt), mostly 20–80. "First instinct" was requested everywhere but not equalized. Sheet vs single was crossed only for sonnet55. There, signa is nearly identical across modes, and format-perp ⟂ (all strata) is 0.38 single vs 0.47 sheet. Family differences such as Gemini's ⟂-readiness or the Sonnet line's per-mille reading can't be separated from these conditions.

## 8. Things that worked as designed and are worth keeping

- **Both-orders presentation** keeps slot preference from masquerading as a directed edge: a slot-driven answer can't produce a consistent-directed pair.
- **Per-item option permutation and the fated stimulus builder.** I found no sign of option-order artifacts in what I examined, though I didn't test this directly.
- **Verbatim raw in the ledger.** Every observation above, including the haiku echo failures, was recoverable only because raw text was kept.
- **The value/ink conflict battery.** Within-judge reps plus both orders make its per-item tallies the most interpretable data in the set.
