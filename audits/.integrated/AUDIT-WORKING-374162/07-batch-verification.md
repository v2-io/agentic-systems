# Verification — Batch 7 (Part I close)

Ground truth read in full, cold, against the quiz/answers/reflections: `result-structural-adaptation-necessity.md`, `der-temporal-nesting.md`, `scope-agent-identity.md`, `impl-persistence-and-limits.md`. Disclosed boundary (four appendix segments cited by `impl-` — `deriv-persistence-cost`, `result-per-dimension-persistence`, `deriv-matrix-persistence-condition`, `result-sector-persistence-template` — read only at summary level) checked: every answer that draws on those four sources stays within what `impl-persistence-and-limits` itself states (T1–T3, the Lyapunov template, the 72%-overestimate figure, the Landauer conversion, the channel-capacity floor) — no claim overreaches into content that would require having read the appendices directly. The boundary held.

## Verdict on the cross-segment finding

**Confirmed — genuine contradiction, not a misreading.**

`scope-agent-identity` Working Notes, dated 2026-05-30: consequence 3 previously read *"the loop provides Level-2-quality data precisely because the agent is on a singular trajectory"* — explicitly flagged as overstated and corrected. The corrected consequence (body, Formal Expression, and Discussion, all three) now states the interventional *character* comes from the action being the agent's own causally-efficacious move under (C1)–(C3), *not* from trajectory singularity; singularity only grounds *whose* effect a datum is.

`impl-persistence-and-limits` §"Identity, trajectory, and the bridge into Part II" (lines 65–66): *"The loop generates interventional data not because of any architectural property of the agent, but because the agent is on a singular trajectory... Strip the singular-trajectory commitment and the loop's interventional content vanishes."* This is the pre-correction claim, close to verbatim, still standing in a segment whose `depends:` frontmatter explicitly lists `scope-agent-identity` and whose own prose (line 64) cites it by name one paragraph earlier ("what makes it load-bearing is that it is what gives Part II's central result... its structural force"). The stale paragraph sits immediately downstream of the very citation that should have carried the correction.

This is a clean instance of the "recently-added structural move lands in the introducing segment but doesn't propagate" drift class — confidence high, not a close call. The `07` answer key's b07-2.4 already treats this correctly (flags the pre-correction phrasing as "the trap" and cross-references the live drift instance), so the answer key and the finding are mutually consistent; neither needs revision on this point.

## Spot-verification of answers

All seven mental-model answers, all six math answers, and all seven implications answers check out against the segment bodies on direct comparison — no misquotes, no wrong attributions, no fabricated numbers. Notable close checks:

- b07-2.5 (Lyapunov template, T1–T3, team-persistence signed-coupling formula) — matches `impl-` lines 54/58 verbatim in substance, including the sign of the cooperative term.
- b07-2.6 (information-rate floor, Kalman-Bucy saturation, channel prerequisite, three-way $\mathcal T/\alpha$/persistence-condition vocabulary) — matches `impl-` §"Information rate..." exactly, including the corrected Landauer coefficient ($\tfrac12 n\alpha k_BT$, not the earlier flagged $0.35\,n\alpha k_BT$ — the answer key already carries the corrected constant).
- b07-3.2 (backup restoration as out-of-scope, not merely lossy) — matches `scope-agent-identity`'s "such operations are out-of-scope events whose epistemic consequences require separate treatment" precisely; the answer correctly resists the weaker "just lossy" framing.
- b07-1.4 / clone-sibling analogy — verbatim match.

## Third catch-pattern (plausible-but-unstated extrapolation) — one instance found

**A b07-2.3**, describing the (PI)-axiom derivation upgrade in `#der-gain-sector-bridge`, adds: *"...to AAT-internally forced (**native information metric, penalty vanishes**)"* and earlier *"Euclidean transfer paying $\kappa(P^-)$."* Neither $\kappa(P^-)$ nor "penalty vanishes" appears anywhere in `scope-agent-identity` — the segment says only that the relevant derivations move from "theorem-imported" to "AAT-internally-forced," without characterizing the before/after cost structure in those terms. This reads as a plausible, probably-correct extrapolation from what a reader would expect the Euclidean-vs-native-metric tradeoff to look like — sound-shaped, not segment-grounded. It isn't wrong (I'd guess it's accurate, given AAT's Fisher-metric conventions elsewhere), but it's imported from outside this batch's ground truth and should be flagged rather than credited as verified-in-corpus. Worth a light touch on the answer key noting this detail's provenance is `der-gain-sector-bridge` itself, not `scope-agent-identity`.

No other instances of this pattern turned up in this batch — the questions are integrative but the answers mostly stay disciplined about citing the segment that actually carries each claim.

## Cross-run note for the eventual quiz-consumers / a continuation session

Seven batches in, the corpus's most load-bearing property for a downstream reader isn't any single result — it's that **the correction trail is itself the reliability signal**, and this batch is the cleanest demonstration of *why that only works if propagation is finished*. The `scope-agent-identity` retraction is exemplary epistemic hygiene (dated, motivated, the old and new text both preserved for comparison in WN) — but `impl-persistence-and-limits` shows that a correction landing cleanly in its introducing segment is necessary, not sufficient: the same claim quietly persists one hop downstream, in a segment that *cites* the corrected one by name without noticing the citation and the two paragraphs above it disagree. A continuation session (or Joseph) fixing this should treat it as a one-paragraph edit in `impl-persistence-and-limits` (repoint "why the loop is interventional" at `der-loop-interventional-access`'s (C1)–(C3), keep the trajectory-singularity sentence only for the identity-grounding half) — the fix is exactly the shape the reflections file already proposes, and I concur with the effort estimate (editorial, not structural).
