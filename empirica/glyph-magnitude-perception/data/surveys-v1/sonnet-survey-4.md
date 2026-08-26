# Perception survey — sequences.md (append-only)

First-instinct pass. Notation per item: sequence, ↑/↓ direction of increasing magnitude, strength (1-5, my confidence a pairwise "which is more" would recover this order), immediacy (PERCEPT = magnitude visible in the shape itself without reading a symbol; SYMBOLIC = arrives via digit/letter lookup even though the glyphs are visually uniform in size), and a note on what "more" means.

---

## Pane: U+2460–U+24FF (Enclosed Alphanumerics)

- `①②③④⑤⑥⑦⑧⑨⑩` ↑ strength 5, SYMBOLIC. Textbook ordinal count. No shape growth at all — every circle is the same size — so the magnitude is 100% digit-lookup. Good baseline contrast case for the immediacy question: extremely strong ordering, zero immediacy.
- `⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽` ↑ strength 5, SYMBOLIC. Same as above, parenthesized instead of circled. No perceptual difference in strength from the circled set — confirms the ordering is carried entirely by the digit, not the enclosure style.
- `Ⓐ Ⓑ Ⓒ … Ⓩ` — NOT included as a magnitude sequence. Alphabetic order reads as "next," not "more." I don't feel a magnitude ladder here, just succession. Worth noting as a *negative* example: sequence/ordering ≠ magnitude. I'll flag other purely-alphabetic or purely-sequential (non-quantity) cases the same way rather than listing them as hits.
- `⓪①②③④⑤⑥⑦⑧⑨⑩` ↑ strength 5, SYMBOLIC, including zero this time — the ⓪ (circled zero) plugged in front feels exactly as expected, no discontinuity.
- `⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾` (double-circled digits) ↑ strength 5, SYMBOLIC — same phenomenon, doubled ring doesn't add a "more" feeling, it just reads as a distinguishing style for a second series of 1-10 (so if placed adjacent to the single-circled 1-10 series I do NOT get a combined magnitude-20 ladder; I get two resets to 1). Interesting: enclosure-style changes do not stack as magnitude, only the digit does.
- `⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴` (negative/inverse-circled 11-20) ↑ strength 4, SYMBOLIC, mild extra friction because the black-disc "negative" rendering first reads as "different category" before I settle into continuing the ordinal count from 10.

**Immediacy note for this whole pane:** none of these are percept-immediate. Every item here is the same visual size/weight; the magnitude signal is 100% routed through recognizing the numeral. This is the clearest possible contrast case against fill/size-based sequences below — good to keep as an anchor.

---

## Pane: U+2580–U+259F (Block Elements)

- `▁▂▃▄▅▆▇█` ↑ strength 5, PERCEPT (maximally so). This is the paradigm case of what Joseph's "immediacy" distinction is pointing at — the magnitude literally *is* the height of black ink; there is no symbol to look up, the ordering is read by the eye as directly as a bar chart. This feels categorically different in kind from every Enclosed-Alphanumerics entry above, not just different in strength. I'd bet this is the single strongest "immediate" sequence I encounter in this whole survey; it's basically a native sparkline.
- `▔█▁` — the eighth-block set actually starts at U+2581 (LOWER ONE EIGHTH) and U+2580 is UPPER HALF, off to the side; ignoring that oddity, the 1/8-through-8/8 ladder above is clean.
- `░▒▓█` ↑ strength 5, PERCEPT. Shading density instead of height — equally immediate, arguably even more purely "amount of ink per unit area" than the bar-height version since there's no directional/height metaphor riding along, just fill density. I notice this one and the bar-height one feel like two flavors of the same underlying axis (density) rather than fully independent finds.
- `▏▎▍▌▋▊▉█` ↑ strength 5, PERCEPT. Same ramp, left-aligned/width-based instead of bottom-aligned/height-based. Confirms the immediacy is about "proportion of the glyph cell filled," independent of which edge it grows from.
- Quadrant blocks (`▖▗▘▝` single corner → `▚▞` two opposite corners → `▙▛▜▟` three corners) — I do sense a rough ↑ ordering by corner-count (1→2→3), PERCEPT, but strength only ~2: the two-corner cases (▚ ▞, diagonal) and (there's no adjacent-two-corner glyph in this block) don't sit as unambiguously "between" 1 and 3 the way the bar/shade ramps do, and I could see a pairwise judge going either way on some pairs. Noting it as a weak/partial find rather than a strong one.

---

## Pane: U+25A0–U+25FF (Geometric Shapes)

- `○◔◑◕●` ↑ strength 5, PERCEPT — WHITE CIRCLE / quarter-black / half-black / three-quarter-black / BLACK CIRCLE. This is exactly a "pie chart" fill ramp — I read it as immediately and physically as the block-height bars. Scattered codepoints (U+25CB, U+25D4, U+25D1, U+25D5, U+25CF) but the ordering leaps out instantly, arguably my favorite find so far because it's circular/pie rather than rectangular, so it's a genuinely different "shape family" carrying the same immediate-fill semantics as the Block Elements pane. This is very likely one of the "concentric circle" things Joseph was anticipating.
- `◌○◍◎●` — a looser variant using DOTTED CIRCLE → WHITE CIRCLE → CIRCLE WITH VERTICAL FILL → BULLSEYE → BLACK CIRCLE. ↑ strength ~2-3 only: ◍ (vertical-fill) and ◎ (bullseye, a ring) don't slot cleanly into a fill-amount ladder the way the quadrant set does — bullseye in particular reads as "circle-in-circle," a different concept (nestedness) more than fill amount, so it fights the ordering. Noting as a weaker/messier neighbor to the strong ◔◑◕ find above, worth keeping separate.
- `▪ ■ ◻ ◼` mixed differently — actually the cleanest same-shape-different-size square set is `▫ ▪` (small) vs `◽ ◾` (medium-small) vs `□ ■` (plain) vs `◻ ◼` (medium) — size ordering ↑ strength 4, PERCEPT for magnitude-by-area, but I have to hold color (white/black) constant to feel it, and Unicode doesn't give me a clean single ladder of "white square, 4 sizes" — I had to intermix names to build one. So: real perceived size ordering exists (small square < medium square < big square), PERCEPT, strength 4, but it's a hand-assembled subset rather than a naturally contiguous run — worth flagging that codepoint-adjacency and semantic-ladder-cleanliness are somewhat independent axes here.
- `▱▰` (white/black parallelogram) — only 2 points, not a real sequence.
- `▵▴` and `▹▸` and `▿▾` and `◃◂` (small triangle white→black, four directions) — I do NOT get a magnitude feel from white→black fill on a *single*, already-small glyph; it reads as a state toggle (off/on, unselected/selected) rather than "more." Negative finding — contrast with the circle/square cases: fill-toggle on a *constant-size* shape does not read as magnitude to me, only fill-*ramp* (multiple intermediate steps) or size-change does.
- `▵▴▷▸▶` (small white triangle → small black triangle → white right-pointing small → black right-pointing small → big black right-pointing) — attempted combining size+fill+rotation into one ladder and it falls apart; too many simultaneously-varying dimensions, no clean order. Negative finding, not including.
- Corner-quadrant sets `◰◱◲◳` (single quadrant, 4 rotations) — no magnitude, purely positional/rotational, explicitly NOT a magnitude sequence (a case worth naming since it superficially resembles the pie-slice fill sequence above but isn't one — same "1 quadrant filled" amount at every step, just rotated).

---

## Pane: U+2600–U+26FF (Miscellaneous Symbols)

- `⚀⚁⚂⚃⚄⚅` ↑ strength 5, mixed immediacy — this is the one Joseph flagged as expected, and I do get it strongly, but I want to register a real distinction on the immediacy axis: 1-3 pips (⚀⚁⚂) I read by subitizing, genuinely percept-immediate, no counting; 4-5-6 (⚃⚄⚅) I have to actually *count* dots for a beat, which is a slower, more effortful process than reading a fill-bar height. So this sequence is NOT uniformly immediate across its own length — the first half feels like the pie-fill case above, the second half feels closer to symbolic. Worth flagging as an internally-mixed case rather than lumping it as pure PERCEPT.
- `☰☱☲☳☴☵☶☷` (the eight trigrams) — this is the other one Joseph anticipated. I do NOT get a monotonic magnitude feeling from this sequence in codepoint order. Trigram value depends on a binary encoding (solid=1/broken=0 read bottom-to-top or top-to-bottom depending on convention) that I cannot subitize — I'd have to consciously decode each glyph's three lines as a 3-bit number. So my honest first-instinct report is: NOT a strong monotonic magnitude sequence for me as given (Unicode's own ordering isn't the binary-value ordering anyway — I checked ☰=111 heaven, ☷=000 earth, they're first/last as expected, but the middle six are not in binary order). I could construct a binary-value-sorted rearrangement that *would* feel monotonic once decoded, but that's re-imposing an order, not perceiving one — noting this as a clear negative/mixed finding since Joseph explicitly bet I'd see it.
- `⚌⚍⚎⚏` (digrams for greater yang / lesser yin / lesser yang / greater yin) — similar issue, non-monotonic naming and no immediate line-count cue since each digram is 2 lines of some solid/broken combination; no magnitude feel, negative finding.
- `⚊⚋` (monogram yang/yin, single solid vs single broken line) — just 2 items, reads as binary state not magnitude.
- `⚆⚇` (white circle, one dot vs two dots) and `⚈⚉` (black circle, one white dot vs two) — dot-count ↑ within each color pair, strength 3, borderline PERCEPT/SYMBOLIC (2-dot subitizing is nearly immediate but I notice a flicker of "counting," so calling it soft-PERCEPT). But the two colors don't chain together (white-circle-2-dots vs black-circle-1-dot don't compare cleanly), so only within-pair, not as one 4-long sequence.
- `⚪⚫` and `⚬` (medium white circle, medium black circle, medium-*small* white circle) — the size difference (medium vs medium-small) does register as a real size cue, but combined with the black/white flip it's confounded (can't tell if "more" means bigger or blacker); not including as a clean find.
- `♩♪♫♬` (quarter note → eighth note → beamed eighth notes → beamed sixteenth notes) ↑ strength 3, semantic ladder rather than visual — "more notes/faster subdivision" is a real conceptual ordering I recognize, and beam-count does increase visually (0→0→1→2 beams... actually eighth-note single has 1 flag, quarter has none, beamed-eighth has 2 notes+1 beam, beamed-sixteenth has 2 notes+2 beams) so there IS a genuine visual "more ink/more beams" component — calling this PERCEPT-leaning-SYMBOLIC (you need to know musical notation to interpret it as "faster," but you can see "more beams" without training). Moderate confidence.
- Recycling numbers `♳♴♵♶♷♸♹` (plastics type 1-7) ↑ strength 4, SYMBOLIC — pure digit-in-triangle lookup, no visual growth (all triangles look nearly identical), close cousin of the Enclosed-Alphanumerics digit case above.
## Pane: U+2150–U+218F (Number Forms) — brief, mostly negative

- `ⅠⅡⅢ` ↑ strength 3, PERCEPT (stroke-count subitizing, genuinely immediate for 1-3) — but `Ⅳ` breaks the immediacy hard: it's visually *shorter* than Ⅲ despite being "more," a real perceptual anti-cue (you have to know the subtractive convention). So `ⅠⅡⅢⅣⅤ` as a whole: strength drops to ~2, and the immediacy is genuinely mixed within the sequence — worth keeping as a named example of "PERCEPT for a prefix, then flips to SYMBOLIC/anti-cue partway through," a texture I haven't seen elsewhere yet.
- `ⅠⅤⅩⅬⅭⅮⅯ` (1,5,10,50,100,500,1000 numerals) — pure SYMBOLIC/LEARNED, no shape-scaling at all (Ⅽ isn't bigger than Ⅹ), strength 4 only if you know Roman numerals.
- Vulgar fractions (`⅛ ⅕ ¼-ish-absent ⅓ ⅜ ½-absent ⅗ ⅔ ¾-absent ⅘ ⅚ ⅞`) — I can construct a numeric-value ordering but it requires doing the division in my head for each glyph (e.g. is ⅖ more or less than ⅜?); zero shape-based cue since all fraction glyphs are roughly the same visual size/complexity. SYMBOLIC, strength only ~2 because several pairs (⅖ vs ⅜, ⅗ vs ⅔) I genuinely have to compute rather than just "know," so a pairwise judge would likely be slow/inconsistent on the close ones. Not a strong find.

(Note: the chess/draughts-piece finding belongs with the Misc Symbols pane above — appended there out of order the first time; leaving this note rather than reshuffling, per the append-only preference.)

- Chess/draughts pieces (`♙♘♗♖♕♔` pawn→knight→bishop→rook→queen→king) — real semantic value ladder (game value: 1,3,3,5,9,∞) that a chess player would recognize instantly, strength 4 *for someone who knows chess*, but strength ~1 for a naive viewer since nothing in the shapes themselves signals "more" — pure learned/domain-semantic ordering, zero visual cue. Flagging as the clearest example so far of a sequence whose monotonicity is 100% acquired-knowledge-dependent, not perceptual at all — a third category beyond PERCEPT/SYMBOLIC-numeral: call it SEMANTIC/LEARNED.

---

## Pane: U+2190–U+21FF (Arrows)

- `→⇒⇛` (single, double, triple rightwards arrow) ↑ strength 5, PERCEPT — line-count is directly visible (1 vs 2 vs 3 shaft-strokes), reads like an intensity gauge on the arrow itself, no lookup needed. Genuinely nice scattered-codepoint find (U+2192, U+21D2, U+21DB); feels closely related in kind to the block-fill family even though the shape is totally different — "more strokes = more."
- `⇉` (rightwards paired arrows, 2 parallel full arrows) sitting conceptually between → and ⇒ — I do NOT cleanly rank ⇉ vs ⇒ against each other; both clearly read as "more than →" but "which is more between them" is genuinely ambiguous (parallel-count vs stroke-thickness are different magnitude metaphors that don't reduce to each other for me). Flagging as an honest ambiguity rather than forcing an order.
- `←↚` then `⇍` (arrow, arrow-with-stroke, double-arrow-with-stroke) — no clean magnitude feeling; the stroke reads as a negation marker ("not left"), not an amount, so it doesn't compose with the double-arrow the way the plain-arrow family does. Negative/mixed finding.
- `↑⇑` (single vs double upward arrow) — same PERCEPT double-stroke cue as the rightwards pair, strength 4 standing alone, but only 2 points here (no triple-up in this block) so weaker as a full "sequence" than the → ⇒ ⇛ case.

---

## Pane: U+2200–U+22FF (Mathematical Operators)

- `∫∬∭` (integral, double integral, triple integral) ↑ strength 5, PERCEPT — count of the ∫ strokes is directly visible and immediately subitizable at 1-3, no symbol lookup needed to see "more of the same mark stacked." Same family feeling as → ⇒ ⇛.
- `∮∯∰` (contour integral, surface integral, volume integral — same as above but with the circle) ↑ strength 5, PERCEPT, same mechanism.
- `≤≦` and `≪⋘` (less-than vs less-than-or-equal; much-less-than vs its doubled/tripled form `≪` then `⋘` reading as "even more much-less-than") — `≪` (much less than, 2 chevrons) vs a single `<` reads as a real "more extreme" PERCEPT cue (2 chevrons stacked = more emphatic than 1), strength 4. But I could not find a clean tripled-chevron glyph in this block to extend it to 3 — `⋘` is actually VERY MUCH LESS-THAN with 3 chevrons, U+22D8, so `<`(1) → `≪`(2) → `⋘`(3) IS a real chevron-count ladder ↑ strength 5, PERCEPT, scattered codepoints (U+003C ordinary ASCII, U+226A, U+22D8) — this is a nice cross-block find since it starts in ASCII.
- `√∛∜` (square root, cube root, fourth root) — the tiny index digit (absent/3/4) sitting in the radical's notch is small and I have to consciously read it; NOT strongly immediate, calling it SYMBOLIC, strength 3 (I know mathematically higher root = smaller result for x>1, which actually inverts naive "more"! so I'm ordering by root-*degree*, not by "output magnitude," and I want to flag that "more" is ambiguous here in a way that's instructive: even once you fix the shape-ladder, which real-world quantity it maps to can flip the felt direction). Interesting edge case for the "more is whatever the sequence makes obvious" instruction — here it's genuinely NOT obvious which of two real quantities (index vs. output size) is intended.
- `⊂⊆⊊` (subset, subset-or-equal, proper-subset — actually ⊊ already means proper/strict) — no clean magnitude feel; these read as different logical relations to me, not points on a "more" scale. Negative finding.
- `∀∃` (for-all, there-exists) — no magnitude at all, purely logical quantifiers; noting as a clear non-example since they sit right at the top of this block and someone might reach for them.

---

## Pane: U+2800–U+28FF (Braille Patterns)

- `⠀⠁⠃⠇⠏⠟⠿⣿` (blank → dots-1 → dots-12 → dots-123 → dots-1234 → dots-12345 → dots-123456 → all-8-dots) ↑ strength 5, PERCEPT — this is a genuine dot-count fill ramp, essentially a "braille sparkline" cousin of the block-element bar ramp: the amount of visible ink increases monotonically and I read it instantly as a density gauge, no need to know braille encoding at all. I like this one because it's a real find *within* a block Joseph explicitly told me to consider (he called out Braille isn't excluded), and it's scattered by literal bit-pattern arithmetic (2^0-1 through 2^8-1) rather than sequential codepoints in a human-curated table — the codepoints themselves are contiguous here (2801, 2803, 2807, 280F, 281F, 283F, 287F is actually dots-1234567=127 not 63... let me not overclaim the exact intermediate codepoints, the visual ramp is what I'm reporting, not a verified byte-exact list) — I'm flagging medium confidence on the *exact* codepoints I typed above vs. high confidence on the *phenomenon* (braille dot-count as a percept-immediate density ramp exists and is strong).
- Random/scattered braille patterns with the same dot-*count* but different dot-*positions* (e.g. dots-14 vs dots-23, both 2 dots) — no ordering between them at all, purely positional variety; important negative case since it shows the ramp above only works when you deliberately choose a monotonically-growing dot subset, not any two braille glyphs.

---

## Pane: U+2300–U+23FF (Miscellaneous Technical)

- `⏑ ⏗ ⏘ ⏙` (METRICAL BREVE, TRISEME, TETRASEME, PENTASEME — 1, 3, 4, 5 morae in classical prosody notation) ↑ strength 3, borderline PERCEPT — each glyph literally has that many little arcs/humps drawn side by side, so the count is visible without knowing what "mora" means, but I have to actually count small humps rather than instantly gauge a fill level, so it's slower than the block/braille cases. Calling it PERCEPT-leaning-SYMBOLIC. Nice scattered/obscure find though (U+23D1, U+23D7, U+23D8, U+23D9) — not something I'd have found without going pane-by-pane.
- `⏴ ⏵ ⏶ ⏷` (medium triangles, 4 directions) — no magnitude, purely directional (media transport buttons), explicit non-example.
- `⏩ ⏪` (double-triangle fast-forward/rewind) vs a hypothetical single-triangle play `▶` from the Geometric Shapes pane — I do get "double triangle = faster/more" as a real semantic-visual cue (2 triangles clearly reads as "2x speed" in UI convention), strength 3, SEMANTIC-leaning (you need the media-player convention, but the doubling itself is visually obvious once you have it). Cross-block sequence: ▶(1x) ⏩(2x, this block) — didn't find a clean 3x glyph nearby.
- Horizontal scan lines `⎺⎻⎼⎽` (scan-line 1, 3, 7, 9 of a 13-row character cell) — these encode vertical *position* within a cell (near top vs near bottom), not amount; tempting to read as a "descending" ladder but it's really about where a line sits, not how much of something there is. Marking as ambiguous/likely-negative — I don't trust my own instinct here enough to call it a strong magnitude finding.

---

## Pane: U+1F030–U+1F09F (Domino Tiles)

- `🀱🀲🀳🀴🀵🀶🀷` (domino 0-0, 0-1, 0-2, 0-3, 0-4, 0-5, 0-6 — one half fixed at blank/zero, other half's pip-count climbing) ↑ strength 4, mixed immediacy like the dice case: 0-1-2 pips subitize instantly (PERCEPT), 3-6 need actual counting (drifts SYMBOLIC). Same texture as ⚀-⚅ — I'm now fairly confident this "subitize-then-count" split at ~3 pips is a real recurring boundary in my own perception, not a one-off, so I'll treat it as a general pattern rather than re-deriving it per pane going forward.
- Full domino double-ladder `🀱(0-0) 🀹(1-1) 🁁(2-2) 🁉... (3-3) ...` (the diagonal doubles, total pips 0,2,4,6,...) — total-pip-count ↑ strength 3, but each tile has to be visually parsed as two separate halves and summed, which is a step slower than the single-half ramp above; noting as a weaker cousin.

---

## Pane: U+2700–U+27BF (Dingbats)

- `✶ ✴ ✹` (six-pointed black star, eight-pointed black star, twelve-pointed black star) ↑ strength 3, PERCEPT-leaning but not fully immediate — point-count is visually present and I can tell "more spiky" at a glance without deliberate counting, closer to a gestalt "spikiness/density" read than exact subitizing; I'd call this softer than the block-fill ramps but distinctly stronger than reading a digit. Scattered codepoints (U+2736, U+2734, U+2739) — didn't jump out until I went hunting for "star" names specifically.
- `✩ ✫ ✬ ✭ ✮` (stress-outlined, open-centre, black-centre-white, outlined-black, heavy-outlined star) — these vary in *style* (outline weight, fill pattern) rather than any count or size I can point to; I don't get any magnitude feel from this run despite it looking like a natural "star gallery." Negative finding, worth naming because on first glance it looks like exactly the kind of run the brief is asking for.
- Heavy/weight-graded arrows `➙ ➔ ➡` (regular heavy rightwards arrow vs. wide-headed vs. solid black) — I get a weak "boldness/weight" ordering (thin→thick→solid reads as "more emphatic"), PERCEPT-ish, strength 2 — genuinely unsure a pairwise judge would be consistent since "wide-headed" vs "black filled" trade off two different visual dimensions.

---

## Pane: U+1F311–U+1F31D (Moon Phase symbols, Supplemental Symbols and Pictographs neighborhood)

- `🌑🌒🌓🌔🌕` (new moon → waxing crescent → first quarter → waxing gibbous → full moon) ↑ strength 5, PERCEPT, maximally so — this is almost certainly one of the "concentric circle" families Joseph was anticipating, and it's the strongest circular fill-ramp I've found, arguably even more natural than the ◔◑◕ geometric-shapes version because it's a real physical phenomenon everyone has directly observed, so the "more" (illuminated fraction) is both visually obvious AND semantically pre-loaded. Contiguous codepoints too (U+1F311-U+1F315), which is a nice contrast with most of my other finds being scattered.
- Continuing to `🌖🌗🌘` (waning gibbous, last quarter, waning crescent) back toward new — I want to flag explicitly that the FULL 8-phase cycle 🌑→🌕→🌑 is NOT monotonic (it's a cycle, goes up then back down), only the first half (new→full) is a clean monotonic ramp. Worth naming since "moon phases" might get proposed as a full-cycle answer by a less careful pass and that would be wrong per the brief's own monotonicity requirement.

---

## Closing reflections (first-pass, unrevised)

Stopping this pass here — I've covered Enclosed Alphanumerics, Block Elements, Geometric Shapes, Misc Symbols, Number Forms, Arrows, Mathematical Operators, Braille, Misc Technical, Domino Tiles, Dingbats, and Moon Phases. Plenty of panes remain unexplored (Supplemental Arrows-A/B/C, Supplemental Math Symbols A/B, Misc Symbols and Arrows U+2B00, Playing Cards, Mahjong, CJK punctuation, Mathematical Alphanumeric Symbols, and more of Supplemental Symbols and Pictographs) — flagging that explicitly rather than implying completeness.

The biggest thing that surprised me: the immediacy question turned out to cut across shape-*families* more than I expected going in. My strongest PERCEPT finds (block-height bars, shading density, pie-slice circles, moon phases, chevron-count `<`≪⋘, arrow stroke-count) all share one mechanism — "amount of ink/lines visible" — regardless of whether the underlying shape is a bar, a circle, a triangle, or a real celestial phenomenon. Meanwhile digit/numeral-based sequences (circled numbers, Roman numerals, subscripts, recycling codes) are strong *orderings* but never immediate, no matter how visually clean the enclosing shape is. Dice and dominoes sit right on the boundary and split internally (1-3 pips subitize, 4-6 need counting) — that was not something I anticipated before actually looking, and I now think that 3-pip subitizing ceiling is a real, generalizable boundary rather than a fluke of any one glyph set.

The other thing worth flagging: several sequences I expected to feel monotonic on the strength of their names/history (the eight trigrams, chess pieces by "value," subset relations) turned out to carry no real perceptual "more" for me at all — the ordering exists only if you already hold outside knowledge, and even then for trigrams the binary value and the Unicode codepoint order don't even agree. I tried to be honest about the difference between "I can construct a valid ordering" and "this reads as monotonic to me on sight," per the brief's actual ask.
