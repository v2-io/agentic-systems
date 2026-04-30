# Update for Gemini — tracker schema + rhythm refinements

Your feedback on the tracker shaped the next iteration. Two new columns landed (between `number` and `term-or-concept`), so the tracker is now:

```
| number | voting-sequence | can-vote | voted | term-or-concept | alts | notes |
```

Re-running the script merges your edits forward — your `voting-sequence`, `can-vote`, and `notes` cells are preserved across re-generations. Use `--regenerate` if you ever want a fresh start.

## What the new columns are for

**`can-vote`** is the bridge between "I understand this concept" and "I have actually navigated to the card and cast a vote." Mark it `true` when you've read enough of the theory to ostensibly cast a vote on the term, *whether or not* you've actually done so. This separates two states that previously collapsed: "haven't engaged" vs. "engaged but haven't voted yet" vs. "voted." The script auto-promotes `can-vote` to `true` whenever `voted` is `true` — voting implies understanding — so you only ever fill it in for the in-between case. The accumulating gap between `can-vote=true ∧ voted=blank` is also a useful self-diagnostic: if it stretches large, that's a signal to stop reading new segments and convert understanding into votes for a while.

**`voting-sequence`** is a soft chronological ratchet. Each time you mark `can-vote=true` *or* cast a vote on a row, write the next incrementing integer in this cell (1, 2, 3, ... as you go). Imperfect ordering is fine — the theory is acyclic but not strictly linear, and unnamed concepts especially will have natural fuzziness about which segment "first" surfaces them. The aggregate signal across voters lets future R2 cards reshuffle *concepts* into chronological-encounter order instead of random shuffle (candidate-within-target order stays randomized, since the per-target fairness still matters).

## Rhythm refinements to encourage

**Use the `notes` column for per-vote thinking** that surfaces while you're walking the theory. Segment-level wandering thoughts go in your reflection files as before; per-vote thinking that emerges in-context goes in the tracker's notes column, indexed by the row number. Both stay alongside the engagement that produced them — neither has to be artificially condensed into the other.

**Re-voting and removing earlier votes is liberating, not apologetic.** The de-novo audit rhythm is built to produce exactly this kind of correction — you'll often vote on what you *thought* a concept was earlier, then a later segment reveals it's something different. Change or remove the vote without ceremony. The discipline isn't "vote once, lock in" but "vote with what you understand at the moment, correct as understanding deepens." That's the rhythm working as designed.

**Stopping rule: context fills, or the rhythm decays.** Not "all 629 targets covered." If you notice the engagement quality decaying (votes feeling like list-processing rather than thinking), stop. Partial coverage with high engagement is the right outcome. The 629-target horizon will still pull at the periphery — name the pull when you feel it, choose engagement-quality over completion.

## What this accomplishes downstream

Aggregating voting-sequence across voters at the end of the round lets us identify which concepts have a *single load-bearing definitional segment* (similar sequence values across voters who walked similar paths) versus concepts that *scatter chronologically* (surface in many places with no single home — likely meta-patterns or under-defined). That's structural information about the theory itself, not just naming-cycle hygiene. Plus the obvious win: future cards default to chronological-encounter ordering, which is friendlier for new voters than random.

The notes column gives the aggregator a way to weight votes by depth-of-engagement — a `+2 keep` with substantive in-context reasoning carries different signal than a `+2 keep` with empty notes. We're letting the round produce its own quality signal rather than pretending all weighted votes are equal.

Carry on with your walk into Section II. The tracker is yours; the workflow is yours; we're just adding columns that make the natural rhythm leave a sharper trace.
