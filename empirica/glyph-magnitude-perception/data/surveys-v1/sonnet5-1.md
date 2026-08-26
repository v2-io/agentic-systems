# Unicode magnitude sequences — first-pass perceptual log (append-only)

Reading one group at a time, noting whatever monotonic magnitude-feel jumps out. Not editing/curating as I go — first impressions.

## Group: Number Forms (U+2150–U+218B)

- ⅐⅑⅒ — 1/7, 1/9, 1/10 → ↓ decreasing magnitude (value shrinks as denominator grows). Strength: high. "More" = value of the fraction.
- ⅛⅜⅝⅞ — 1/8,3/8,5/8,7/8 → ↑ increasing. Strength: very high, clean arithmetic ladder, visually the numerator glyph itself increases.
- ⅙⅚ — 1/6, 5/6 → ↑. Strength: high (only two terms, but unambiguous).
- ⅕⅖⅗⅘ — 1/5,2/5,3/5,4/5 → ↑. Strength: very high, same family as eighths.
- ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ — Roman numerals I–XII → ↑. Strength: very high, extremely canonical.
- ⅠⅬⅭⅮⅯ — I, L, C, D, M (1,50,100,500,1000) → ↑. Strength: high once you know Roman numeral values, but *not* purely visual/gestalt the way I–XII is (requires actual numeral literacy) — so I'd flag this weaker for a "fresh agent pairwise" test than I–XII, even though I'm personally very sure.
- ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻ — lowercase small roman numeral series → ↑, same as uppercase, strength very high.
- ↀↁↂ — 1000, 5000, 10000 (large Roman numeral forms) → ↑. Strength: moderate — glyphs are unfamiliar/rare, so semantic "more" relies on memorized values rather than shape; shape itself (added strokes/box) does trend more complex though, which independently supports ↑.
- ⅟, ↉ (fraction numerator one U+215F, vulgar fraction zero thirds U+2189) — interesting outliers, not part of a clean run themselves but could seed a "denominator grows → value shrinks" cross-sequence with the eighths/fifths sets above (⅟1 > ⅛ > ⅒ type constructed sequence, mixing different fraction glyphs by pure value). Strength: high if compared as raw fraction magnitude, but they're visually dissimilar (different construction) so gestalt "gliding" might be weaker than the ⅛⅜⅝⅞ same-family case.

## Group: Miscellaneous Symbols (U+2600–U+26FF)

- ⚀⚁⚂⚃⚄⚅ — die faces 1–6 → ↑. Strength: very high, exactly the one you predicted, dot-count is unambiguous.
- ⚆⚇⚈⚉ — white circle w/ dot right, white circle w/ two dots, black circle w/ dot right, black circle w/ two dots → dot-count gives a weak ↑ (1,2,1,2 doesn't monotonically increase across all four as a single sequence — but ⚆→⚇ alone is ↑ by dot count, and ⚈→⚉ alone is ↑ by dot count). Strength: medium, only valid as two separate pairs not one 4-chain.
- ⚊⚋ — monogram for yang / monogram for yin (unbroken line / broken line) — not itself ordered, but sets up...
- ⚌⚍⚎⚏ — digrams (two stacked lines, some broken) — could combine with monograms into a "line count" sequence ⚊⚌ (1 line → 2 lines) → ↑ strength high on stroke-count; the yin/yang semantic ordering (greater yang > lesser yin > lesser yang > greater yin) is a separate, much weaker/more esoteric axis — noting both.
- ⚪⚫⚬ — MEDIUM WHITE CIRCLE, MEDIUM BLACK CIRCLE, MEDIUM SMALL WHITE CIRCLE — size-named! ⚪/⚫ (medium) vs ⚬ (medium small) → ⚬ < ⚪ ↑, strength high on the literal "small" in the name, though visually the point size difference is subtle in most fonts.
- ♩♪♫♫♬ — quarter note, eighth note, beamed eighth notes, beamed sixteenth notes → ↑ by rhythmic density/subdivision (fewer flags=longer note=slower; more flags=faster/smaller value). Strength: high for anyone with music literacy, otherwise opaque. Genuinely a "semantic ladder" case, not visual complexity alone — though visual complexity (flag count) *does* track it, reinforcing.
- ♳♴♵♶♷♸♹ — recycling symbols for plastic types 1–7 → ↑, strength very high, literal embedded digit inside the glyph (visually the number is legible in most renderings), a strong pure "denoted number" case.
- ☆★ — white star, black star — not a magnitude pair per se (fill difference), tentatively noting as a *candidate* fill-density axis (empty→full) to watch for across other "white X / black X" doublets in this block (there are many: ballot box ☐☑☒, telephone ☎☏, flag ⚐⚑, chess pieces, draughts men). Strength: low as "magnitude" per se, more like a binary toggle — but worth flagging since white→black could read as light-to-heavy/empty-to-full ↑ if a "weight" or "fill" sense is invoked. Uncertain, flagging rather than asserting.
- ⚹⚺⚻⚼ — sextile, semisextile, quincunx, sesquiquadrate (astrological aspect angles: 60°, 30°, 150°, 135°) — a genuine denoted-number sequence exists in the underlying angles but the glyphs give zero visual cue; I don't perceive an ordering just from looking at the symbols. Strength: none visually; flagging only because the semantic axis (degrees) technically exists — probably NOT one for the list since "the sequence makes obvious" fails here.
- ⛀⛁ / ⛂⛃ — white draughts man / white draughts king, black draughts man / black draughts king — man→king is a promotion/rank-up in checkers (king is "more" — more powerful/more marked, visually more crown-like) → ↑ within each color pair. Strength: medium, requires checkers knowledge.
- ♔♕♖♗♘♙ vs ♚♛♜♝♞♟ (seen in group, chess pieces) — no clean magnitude order jumps out to me by mere glyph inspection despite chess piece values existing (pawn<knight/bishop<rook<queen<king in some sense) — the glyphs themselves don't communicate it. Not including as a strong entry, flagging only.

## Group: Geometric Shapes (U+25A0–U+25FF)

- ○◔◐◕● — WHITE CIRCLE, CIRCLE W/ UPPER RIGHT QUADRANT BLACK, CIRCLE W/ LEFT HALF BLACK, CIRCLE W/ ALL BUT UPPER LEFT QUADRANT BLACK, BLACK CIRCLE → ↑ (0%, 25%, 50%, 75%, 100% fill) — this is the moon-phase / pie-chart/battery-icon progression, extremely strong, exactly the kind of "obvious once you see it, count-based magnitude" the brief wants. Strength: very high, one of my most confident finds so far.
- ◌○◯ — DOTTED CIRCLE, WHITE CIRCLE, LARGE CIRCLE — tentative ↑ by "presence/solidity then size" (dotted=barely there → solid outline → large) — weaker/more constructed than the fill sequence above. Strength: low-medium, flagging rather than asserting strongly.
- ▪▫ / ◻◼ / ◽◾ / □■ — small square, medium square, medium-small square, regular square all appear as black/white pairs across different code points at DIFFERENT explicit named sizes: "small" (▪▫ U+25AA/AB) < "medium small" (◽◾ U+25FD/FE) < "medium" (◻◼ U+25FB/FC) — a genuine named-size ladder scattered across non-adjacent codepoints exactly like you predicted! ↑ strength: high — the names literally say small → medium small → medium, and (at least in most fonts) the rendered size does increase to match.
- ▲△ / ▴▵ (and repeated for ▶▷▸▹, ▼▽▾▿, ◀◁◂◃) — full-size triangle vs "small" triangle, same direction, in each of the four rotations → ↑ by size, strength high, and it's the same "regular vs small" naming split as the squares — very possibly a general cross-shape axis (regular > small) worth watching for elsewhere (spacing modifier letters, stars, etc. per your hint).
- ▬ / ▭ vs ▮ / ▯ — RECTANGLE vs VERTICAL RECTANGLE (same black/white pairing, orientation change) — no magnitude order, just orientation; noting as a non-example (rotation ≠ magnitude) to keep myself honest about what doesn't count.
- ◇◈ — WHITE DIAMOND, WHITE DIAMOND CONTAINING BLACK SMALL DIAMOND — nested-shape → ↑ by nestedness/fill, strength medium (only 2 terms, but the "containing" relationship is visually unambiguous — this is the exact "nestedness" axis you mentioned in the brief).
- ○◎◉● — WHITE CIRCLE, BULLSEYE, FISHEYE, BLACK CIRCLE — a candidate ↑ by "amount of black/fill accumulating toward the center outward" (empty → ring target → mostly-filled-with-ring → solid) — genuinely uncertain of my own ordering here between ◎ and ◉, flagging this as one of the "not sure why but it feels ordered" cases the brief specifically wants. Strength: low-medium, real uncertainty on ◎ vs ◉ placement.
- ◰◱◲◳ — WHITE SQUARE WITH UPPER LEFT / LOWER LEFT / LOWER RIGHT / UPPER RIGHT QUADRANT — a clock-like rotational sequence (quadrant sweeping around), feels like it wants to be a "loading spinner" ↑ but it's cyclic/rotational rather than magnitude — flagging as another rotation-not-magnitude non-example, though there is a directional "feel" (clockwise progression) that's adjacent to what you're after even if it isn't strictly "more."

## Group: Enclosed Alphanumerics (U+2460–U+24FF)

- ⓪①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳ — circled 0 through 20 → ↑, strength very high. Note: ⓪ (CIRCLED DIGIT ZERO) is at U+24EA, way out of codepoint sequence from ①–⑳ (U+2460–2473) — this is *exactly* the "circled 0 before circled 1 despite later codepoint" case you named in the brief as an example you expected. Confirmed, semantic order overwhelms codepoint order here without any hesitation on my part.
- ⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇ — parenthesized 1–20 → ↑, strength very high, same as circled digits, cleanest possible "denoted number" case.
- ⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖⒗⒘⒙⒚⒛ — digit-full-stop 1–20 (like "1." "2." list markers) → ↑, strength very high.
- ①⑴⒈ / Ⓐ-vs-numeric comparisons — cross-*style* comparison of the same magnitude (circled-1 vs parenthesized-1 vs 1-full-stop) isn't a magnitude sequence itself (they're equal, just different enclosure styles) — noting as a non-example / a "same value different dress" case, potentially useful if you want equivalence-class awareness alongside pure ordering.
- ⓪①②③④⑤⑥⑦⑧⑨⑩ vs ⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴ (negative circled 11–20, U+24EB–24F4) vs ⓿ (negative circled 0, U+24FF) — the "negative" (white-on-black) circled numbers also independently form ⓿ → ⓫ → ⓴ ↑, strength very high, and again ⓿ sits at the far end of the block (U+24FF) out of numeric order relative to ⓫–⓴, another scattered-codepoint/semantic-overwhelms-codepoint case.
- ⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾ — double circled digits 1–10 → ↑, strength very high, same pattern again; interesting that this whole block essentially replays "N through 20 (or 10)" in about five different visual dialects (circled, parenthesized, full-stop, negative-circled, double-circled) — a strong structural pattern: whenever unicode gives you an enclosure/decoration style applied to digits, the digit-order sequence is essentially guaranteed. Noting this as a *meta*-observation for efficiency going forward: I probably don't need to belabor every future "decorated digit family" I encounter with this much individual commentary — the pattern itself is the finding.
- ⒜⒝⒞…⒵ and Ⓐ…Ⓩ and ⓐ…ⓩ (parenthesized/circled Latin letters) — alphabetical order is *ordinal*, not really "magnitude" in the sense the brief cares about (no natural "which is more" outside learned alphabet position) — flagging as a boundary case I'm choosing NOT to include as a strong entry, since "more" would just be "later in the alphabet," which feels like a different, weaker kind of ordering than count/size/fill.

## Group: Mathematical Operators (U+2200–U+22FF)

- ∫∬∭ — integral, double integral, triple integral → ↑, strength very high, stacked-line-count is immediate.
- √∛∜ — square root, cube root, fourth root → ↓ (as a "root index" ladder, higher root = smaller result for same input >1, but more naturally read as ↑ by root-index/complexity of the little number tucked in). Strength: high, though direction depends on which "more" you mean — flagging the ambiguity itself as the interesting note.
- < ≤ ≪ — less-than, less-than-or-equal, much-less-than — not itself a magnitude chain (different relations), skipping.
- ≈ ≡ — no clean feel, skipping.
- ⊂ ⊆ — subset of vs subset-of-or-equal — no strong magnitude feel to me, skipping.
- ⋮⋯⋰⋱ — vertical ellipsis, horizontal ellipsis, diagonal ellipses — just rotations, no magnitude, skipping (noting only because it's tempting-looking and isn't one).

## Group: Arrows (U+2190–U+21FF)

- → ⇒ ⇉ ⇛ ⇶ — RIGHTWARDS ARROW, DOUBLE ARROW, PAIRED ARROWS, TRIPLE ARROW, THREE RIGHTWARDS ARROWS → ↑ strength: high, "how many/how thick" the arrow shaft reads as intensity/emphasis/certainty. Same pattern works for any direction (←⇐⇇⇚ etc).
- → ⇒ — single vs double-line arrow, reads as ↑ in emphasis/strength/certainty (like "implies strongly"), strength: high.
- ⇀ ⇉ — harpoon (half arrowhead) vs full paired arrows — skipping, not a clean magnitude feel, just different arrow types.
- ⇠ → — dashed arrow vs solid arrow → tentative ↑ (dashed feels tentative/weak, solid feels definite/strong), strength: medium.
- ↺ ↻ — clockwise/anticlockwise open circle arrows — no magnitude, just direction, skipping.

## Group: Dingbats (U+2700–U+27BF)

- ❘❙❚ — LIGHT VERTICAL BAR, MEDIUM VERTICAL BAR, HEAVY VERTICAL BAR → ↑ strength: very high, literal named weight ladder, thickness is directly visible.
- ❶❷❸❹❺❻❼❽❾❿ — dingbat negative circled digits 1–10 → ↑ strength: very high, same clean digit case as before.
- ➀➁➂➃➄➅➆➇➈➉ — dingbat circled sans-serif digits 1–10 → ↑ strength: very high.
- ✓✔ — CHECK MARK, HEAVY CHECK MARK → ↑ strength: high, weight = emphasis.
- ✕✖ — MULTIPLICATION X, HEAVY MULTIPLICATION X → ↑ strength: high, same weight pattern.
- ✗✘ — BALLOT X, HEAVY BALLOT X → ↑ strength: high, same pattern.
- ✱✲✳ — HEAVY ASTERISK, OPEN CENTRE ASTERISK, EIGHT SPOKED ASTERISK — not a clean magnitude, skipping.
- ✦✧ — BLACK FOUR POINTED STAR, WHITE FOUR POINTED STAR — fill toggle not magnitude, skipping.
- ✈ (airplane) and other single pictographs — no sequence, skipping.

## Group: Box Drawing (U+2500–U+257F)

- ─━ — LIGHT HORIZONTAL, HEAVY HORIZONTAL → ↑ strength: very high, weight/thickness ladder again, extremely visible.
- │┃ — LIGHT VERTICAL, HEAVY VERTICAL → ↑ same as above, strength very high.
- ┈┄ — quadruple dash vs triple dash (light) — dash-count → tentative feel of "finer/coarser" but not a clean magnitude, skipping.
- ═ vs ─ (double horizontal vs single/light horizontal) → ↑ strength: high, "double" reads as more/stronger than single, same weight-family idea as light→heavy.

## Group: Spacing Modifier Letters (U+02B0–U+02FF)

- ˥˦˧˨˩ — EXTRA-HIGH TONE BAR, HIGH TONE BAR, MID TONE BAR, LOW TONE BAR, EXTRA-LOW TONE BAR → ↓ strength: very high. Genuinely striking one: the glyphs are literally little bars positioned at different vertical heights next to a vertical stem, so the *visual* height directly tracks the *semantic* pitch-height — both cues agree, adjacent codepoints, exactly the kind of clean case the brief wants.
- (rest of block: mostly IPA diacritics/accent marks — no other clean magnitude feel jumped out to me.)

## Group: Superscripts and Subscripts (U+2070–U+209F)

- ⁰⁴⁵⁶⁷⁸⁹ — superscript digits (missing 1-3, elsewhere in Latin-1) → ↑ strength very high, plain digit ladder.
- ₀₁₂₃₄₅₆₇₈₉ — subscript digits 0-9 → ↑ strength very high.
- (superscript/subscript themselves as a *pair*, e.g. comparing ⁵ to ₅, isn't a magnitude relationship — same value, different position — skipping as non-example.)

## Group: Braille Patterns (U+2800–U+28FF, first sub-block sampled)

- ⠀⠁⠃⠇⠏⠟⠿ — BLANK, DOTS-1, DOTS-12, DOTS-123, DOTS-1234, DOTS-12345, DOTS-123456 → ↑ strength: high, pure accumulating dot-count/fill-density, visually reads like a little progress-bar filling in. Scattered codepoints (not sequential in the raw block) but a clean pick.
- Rest of the 256-cell braille block is combinatorial (all dot-subsets) — not revisiting exhaustively, the fill-count axis above is the real find here.

## Group: Block Elements (U+2580–U+259F)

- ▁▂▃▄▅▆▇█ — LOWER ONE EIGHTH, QUARTER, THREE EIGHTHS, HALF, FIVE EIGHTHS, THREE QUARTERS, SEVEN EIGHTHS, FULL BLOCK → ↑ strength: extremely high, THE canonical "sparkline"/bar-height glyph set, height directly = magnitude, adjacent codepoints too. One of the strongest finds in the whole survey so far.
- ░▒▓█ — LIGHT SHADE, MEDIUM SHADE, DARK SHADE, FULL BLOCK → ↑ strength: extremely high, classic fill-density/darkness ramp, adjacent codepoints, named "light/medium/dark."
- ▏▎▍▌▋▊▉█ — LEFT ONE EIGHTH...LEFT SEVEN EIGHTHS, FULL BLOCK → ↑ strength: extremely high, same progression as the vertical one but horizontal (left-fill), also the literal glyph set used for terminal progress bars.

## Group: General Punctuation (U+2010–U+206F)

- ‐–— — HYPHEN, EN DASH, EM DASH → ↑ strength: very high, literal length increases, extremely familiar to any writer.
- ․‥… — ONE DOT LEADER, TWO DOT LEADER, HORIZONTAL ELLIPSIS (three dots) → ↑ strength: very high, dot count.
- †‡ — DAGGER, DOUBLE DAGGER → ↑ strength: high, footnote-marker escalation, weight/count.
- ′″‴⁗ — PRIME, DOUBLE PRIME, TRIPLE PRIME, QUADRUPLE PRIME → ↑ strength: very high, tick-count.
- ‰‱ — PER MILLE, PER TEN THOUSAND → ↑ strength: high (semantic: finer-grained ratio / more zeros, and visually one more "0" loop appended).
- ⁚⁖⁘⁙ — TWO DOT PUNCTUATION, THREE DOT PUNCTUATION, FOUR DOT PUNCTUATION, FIVE DOT PUNCTUATION → ↑ strength: high, dot count, though scattered/non-adjacent codepoints within the block.

## Group: Latin-1 Supplement (U+00A0–U+00FF)

- ¹²³ — SUPERSCRIPT ONE, TWO, THREE → ↑ strength: very high, plain digits.
- ¼½¾ — VULGAR FRACTION ONE QUARTER, ONE HALF, THREE QUARTERS → ↑ strength: very high, same clean fraction ladder as the earlier Number Forms block.

## Group: Chinese/CJK size and number words (not tool-generated — drawing on my own knowledge of the characters, per your "tiny/small/medium/large" hypothesis)

- 小中大 — xiǎo (small), zhōng (medium), dà (large) → ↑ strength: high for me (I do have some ability to read these), though this is a case where the ordering is purely lexical/semantic — the glyphs give almost no visual size cue themselves (this is NOT like the "small circle vs medium circle" cases where rendered size differs) — flagging that distinction honestly. You guessed exactly right that something like this exists.
- 一二三四五 — yī, èr, sān, sì, wǔ (Chinese numerals 1-5) → ↑ strength: very high — and interestingly 一二三 (1,2,3) are themselves literally built from stacked horizontal strokes (1 stroke, 2 strokes, 3 strokes), so the *stroke count itself* visually tracks magnitude for the first three, before the pattern breaks for 四/五. Strength on 一二三 alone: very high on both semantic AND visual/stroke-count grounds simultaneously.
- 十百千万 — shí (ten), bǎi (hundred), qiān (thousand), wàn (ten-thousand) → ↑ strength: high semantically, no visual size cue.

## Group: Asterisk / star-point-count scan (revisiting Dingbats + General Punctuation with a specific eye toward this)

- *⁑⁂ — ASTERISK, TWO ASTERISKS ALIGNED VERTICALLY, ASTERISM (three asterisks in a triangle) → ↑ strength: very high, literal asterisk-count.
- ✦✶✳✴✹✺ — BLACK FOUR POINTED STAR (4), SIX POINTED BLACK STAR (6), EIGHT SPOKED ASTERISK (8), EIGHT POINTED BLACK STAR (8), TWELVE POINTED BLACK STAR (12), SIXTEEN POINTED ASTERISK (16) → ↑ strength: very high, named point-count directly in the glyph name AND visually countable — a great scattered-codepoint find inside the Dingbats block (U+2726, 2736, 2733, 2734, 2739, 273A), exactly the "reach across a group for a scattered sequence" the brief invited.

## Group: Domino Tiles (U+1F030–U+1F0FF)

- 🀱🀲🀳🀴🀵🀶🀷 — DOMINO TILE HORIZONTAL-00-00 through -00-06 (one half fixed at 0, other half 0→6 pips) → ↑ strength: very high, pip count on one side climbs, dice-like.
- 🀰 (DOMINO TILE HORIZONTAL BACK, the face-down/blank tile) — a natural "less than zero" anchor before 🀱, i.e. 🀰🀱🀲…🀷 → ↑ with the back-tile as the true minimum (no pips visible at all, even less informative than 0-0). Strength: medium-high, satisfying but requires accepting "hidden" as "least."

## Group: Playing Cards (U+1F0A0–U+1F0FF)

- 🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪 — ACE...TEN OF SPADES (reading ace-low) → ↑ strength: very high, pip count is even visually depicted on real card faces (though the unicode glyphs themselves mostly render as generic card-back-style icons in most fonts, so the visual cue is weaker than the semantic one — flagging honestly).
- 🂪🂫🂭🂮 — TEN, JACK, QUEEN, KING OF SPADES → ↑ strength: very high by conventional card rank, purely semantic/learned (no visual size cue).

## Group: Currency Symbols (U+20A0–U+20CF)

- Nothing found — each glyph denotes a different currency's arbitrary unit, no shared magnitude axis across them.

## Group: Miscellaneous Technical (U+2300–U+23FF)

- ⏗⏘⏙ — METRICAL TRISEME, TETRASEME, PENTASEME (3, 4, 5 morae) → ↑ strength: high, count embedded directly in the name (tri/tetra/penta), though the glyphs themselves don't visually telegraph it clearly to me.
- ▶⏩⏭ — BLACK RIGHT-POINTING TRIANGLE (play), BLACK RIGHT-POINTING DOUBLE TRIANGLE (fast-forward), BLACK RIGHT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR (skip-to-next) → ↑ strength: high, media-player speed/intensity convention very familiar from UI, triangle-count tracks "more speed."
- ⏺⏹ — BLACK CIRCLE FOR RECORD, BLACK SQUARE FOR STOP — no magnitude, just distinct UI functions, skipping.

## Group: Enclosed CJK Letters and Months (U+3220–U+32FF)

- ㈠㈡㈢㈣㈤㈥㈦㈧㈨㈩ — PARENTHESIZED IDEOGRAPH ONE through TEN → ↑ strength: very high, same clean digit case as before, just in ideographs.
- ㉈㉉㉊㉋㉌㉍㉎ — CIRCLED NUMBER TEN/TWENTY/THIRTY/FORTY/FIFTY/SIXTY/SEVENTY ON BLACK SQUARE → ↑ strength: very high, tens ladder, named directly.

## Group: Musical Symbols (U+1D150–U+1D1EA)

- 𝅝𝅗𝅥𝅘𝅥𝅘𝅥𝅮𝅘𝅥𝅯𝅘𝅥𝅰𝅘𝅥𝅱𝅘𝅥𝅲 — WHOLE, HALF, QUARTER, EIGHTH, SIXTEENTH, THIRTY-SECOND, SIXTY-FOURTH, ONE-HUNDRED-TWENTY-EIGHTH NOTE → ↓ duration (or ↑ subdivision-count/speed), strength: very high, extremely canonical for anyone with music literacy, and the flag-count on the note stem visually tracks it too.
- 𝆏𝆐𝆑 — PIANO, MEZZO, FORTE → ↑ strength: very high, the classic soft→loud dynamics ladder.
- 𝆒𝆓 — CRESCENDO, DECRESCENDO — these are directional markings not a magnitude pair themselves, skipping.

## Group: Combining Diacritical Marks for Symbols (U+20D0–U+20FF)

- ⃛⃜ — COMBINING THREE DOTS ABOVE, FOUR DOTS ABOVE → ↑ strength: medium (only two terms, dot count).
- Nothing else strong here.

## Group: Supplemental Mathematical Operators (U+2A00–U+2AFF)

- Nothing found — mostly decorated-variant operators (plus-with-dot, minus-with-comma, etc.), no shared magnitude axis jumped out.

## Group: Miscellaneous Symbols and Arrows (U+2B00–U+2BFF)

- ⬝⬞ / ⬛⬜ — BLACK/WHITE VERY SMALL SQUARE vs BLACK/WHITE LARGE SQUARE → ↑ strength: high, another named-size square pair (extends the small/medium-small/medium ladder found earlier in Geometric Shapes with a "very small" and "large" at the ends — genuinely scattered across two different blocks now).
- ⭐⭑⭒ — WHITE MEDIUM STAR, BLACK SMALL STAR, WHITE SMALL STAR → tentative ↑ by size (medium > small), strength: medium, mixing fill-color and size in the same short run muddies it a bit.
- ⬅⬆➡⬇ variants (black arrows) — no magnitude, just direction, skipping.

## Group: Mahjong Tiles (U+1F000–U+1F02B)

- 🀙🀚🀛🀜🀝🀞🀟🀠🀡 — ONE through NINE OF CIRCLES → ↑ strength: very high, the glyphs literally render as a grid of dots, so visual pip-count directly tracks the number, same class as dice/dominoes.
- 🀇🀈…🀏 (characters) and 🀐🀑…🀘 (bamboos) — same 1-9 ordering, strength very high semantically, though bamboos/characters render as ideographs/sticks rather than obviously-countable pips so the visual cue is weaker than the circles suit.

## Group: Enclosed Alphanumeric Supplement (U+1F100–U+1F1FF)

- 🄁🄂🄃🄄🄅🄆🄇🄈🄉🄊 — DIGIT ZERO/ONE/.../NINE COMMA → ↑ strength: very high, same digit-ladder pattern as several times before — not belaboring further, this "decorated digit family → clean ladder" pattern is now well established across the survey.

## Group: Moon Phase emoji (U+1F311–U+1F318)

- 🌑🌒🌓🌔🌕 — NEW, WAXING CRESCENT, FIRST QUARTER, WAXING GIBBOUS, FULL MOON → ↑ strength: extremely high, illuminated-fraction directly visible, essentially the emoji cousin of the ○◔◐◕● circle-fill sequence found earlier — nice cross-confirmation that this fill-progression pattern recurs.
- 🌕🌖🌗🌘🌑 — FULL, WANING GIBBOUS, LAST QUARTER, WANING CRESCENT, back to NEW → ↓ strength: extremely high, the mirror-image second half of the same cycle.

## Group: Emoticons (U+1F600–U+1F64F)

- 🙂😐😀😁😂 — SLIGHTLY SMILING, NEUTRAL, GRINNING, GRINNING WITH SMILING EYES, FACE WITH TEARS OF JOY — genuinely uncertain ordering myself among the first few (is neutral "less" than slightly smiling, or a different axis entirely?), but 😀→😁→😂 does feel like a real ↑ escalation of joy/mouth-openness/eye-scrunch. Strength: medium, and honestly one where I'm not fully sure why 😂 reads as "more" — flagging as one of the "not sure why but it feels ordered" cases.
- 😢😭 — CRYING FACE, LOUDLY CRYING FACE → ↑ strength: high, single tear vs streaming tears + open wailing mouth, visually unambiguous escalation.
- 😮😯😲😱 — FACE WITH OPEN MOUTH, HUSHED FACE, ASTONISHED FACE, FACE SCREAMING IN FEAR — tentative ↑ by surprise/shock intensity, strength: low-medium, less confident than the crying pair.

## Group: General Punctuation — Spaces sub-block (U+2000–U+200A) [gap-fill pass, codepoint order]

- HAIR SPACE, THIN SPACE, SIX-PER-EM SPACE, FOUR-PER-EM SPACE, THREE-PER-EM SPACE, PUNCTUATION SPACE, FIGURE SPACE, EN SPACE, EM SPACE, EN QUAD, EM QUAD → ↑ strength: high on the *name* (literal fraction-of-an-em denominators shrinking as width grows: 6-per-em < 4-per-em < 3-per-em < ½-em(en) < 1-em(em)), though these are invisible/whitespace glyphs so there's no way to *perceive* the ordering by looking at rendered characters the way every other entry in this file can be — flagging honestly as a "named magnitude, unseeable" edge case rather than a strong perceptual one. Interesting anyway per your instruction not to prejudge groups.

## Group: Letterlike Symbols (U+2100–U+214F) [gap-fill]

- ℵℶℷℸ — ALEF SYMBOL, BET SYMBOL, GIMEL SYMBOL, DALET SYMBOL → ↑ strength: high for me (used in set theory for successive transfinite cardinal/beth numbers, ℵ₀ < ℶ₀ etc.), purely notational/learned, no visual size cue — another semantic-only ladder like the Chinese numerals.
- Nothing else in this block reads as a magnitude sequence (mostly distinct named constants/symbols: Ω, K, Å, ™, etc., each singular).

## Group: pending

## Group: Miscellaneous Mathematical Symbols-A (U+27C0–U+27EF) [gap-fill]

- ⟨⟩ / ⟪⟫ — MATHEMATICAL LEFT/RIGHT ANGLE BRACKET vs LEFT/RIGHT DOUBLE ANGLE BRACKET → ↑ strength: medium, single-to-double weight pattern again (same family as arrow/vertical-bar doubling found earlier).
- Nothing else — mostly one-off relational/lattice notation with no shared axis.

## Group: pending

## Group: Supplemental Arrows-A and -B (U+27F0–U+27FF, U+2900–U+297F) [gap-fill]

- ⟶⟹ — LONG RIGHTWARDS ARROW, LONG RIGHTWARDS DOUBLE ARROW → ↑ strength: medium, same single/double weight pattern already logged for other arrows.
- Rest of both blocks is dense combinatorial arrow-decoration (stroke/tail/dash variants for technical notation) — no new magnitude axis beyond what's already captured (weight/multiplicity).

## Group: pending

## Group: Miscellaneous Mathematical Symbols-B (U+2980–U+29FF) [gap-fill]

- ⧺⧻ — DOUBLE PLUS, TRIPLE PLUS → ↑ strength: high, plus-sign count directly named.
- Nothing else — mostly one-off relational/geometric notation variants.

## Group: pending

## Group: CJK Symbols and Punctuation (U+3000–U+303F) [gap-fill]

- 〡〢〣〤〥〦〧〨〩〸〹〺 — HANGZHOU NUMERAL ONE through NINE, then TEN, TWENTY, THIRTY → ↑ strength: very high, a clean tally-mark-style digit ladder (the glyphs are literally built from accumulating strokes for 1-3, like the Chinese 一二三 case), with a scattered jump to the tens forms later in the same block.
- 〈〉 vs 《》 — LEFT/RIGHT ANGLE BRACKET vs LEFT/RIGHT DOUBLE ANGLE BRACKET → ↑ strength: medium, same single/double weight pattern seen elsewhere.
- 〇 IDEOGRAPHIC NUMBER ZERO — a natural anchor below the Hangzhou numeral one, if reaching across for a zero.

## Group: pending

## Group: CJK Compatibility — squared unit symbols (U+3300–U+33FF) [gap-fill, rich vein]

- ㌰㌨㍉㌢㌔㍋㌐ — SQUARE PIKO(pico,10⁻¹²), NANO(10⁻⁹), MIRI(milli,10⁻³), SENTI(centi,10⁻²), KIRO(kilo,10³), MEGA(10⁶), GIGA(10⁹) → ↑ strength: very high — a genuine order-of-magnitude ladder hiding as Japanese-loanword squared symbols, scattered non-adjacent codepoints throughout the block, exactly the kind of "reach across and find it" case you were hoping for.
- ㎜㎝㎞ — SQUARE MM, SQUARE CM, SQUARE KM (millimeter, centimeter, kilometer symbols) → ↑ strength: very high, adjacent codepoints, plain length-scale ladder.
- ㎟㎠㎡㎢ — SQUARE MM SQUARED, CM SQUARED, M SQUARED, KM SQUARED (area units) → ↑ strength: very high, adjacent codepoints, area-scale ladder.
- ㎣㎤㎥㎦ — SQUARE MM CUBED, CM CUBED, M CUBED, KM CUBED (volume units) → ↑ strength: very high, adjacent codepoints, volume-scale ladder — three parallel scale-ladders sitting right next to each other in the same block.

## Group: pending

## Group: CJK Compatibility — more unit-prefix squares (U+3380–U+33DF) [gap-fill, continued]

- ㎐㎑㎒㎓ — SQUARE HZ, KHZ, MHZ, GHZ → ↑ strength: very high, adjacent codepoints, frequency-scale ladder.
- ㎎㎏ — SQUARE MG, SQUARE KG → ↑ strength: very high, adjacent codepoints, mass-scale.
- ㎩㎪㎫ — SQUARE PA, KPA, MPA → ↑ strength: very high, adjacent codepoints, pressure-scale.
- ㎰㎱㎳ — SQUARE PS, NS, MS (picosecond, nanosecond, millisecond) → ↑ strength: very high, time-scale, scattered but nearby codepoints.
- ㎽㎾㎿ — SQUARE MW(milli), KW, MW(mega) → ↑ strength: high, adjacent codepoints, power-scale (note the milliwatt/megawatt abbreviation collision in the name text itself, amusing but the ordering is still clear from context).

## Group: pending

## Group: Halfwidth and Fullwidth Forms (U+FF00–U+FFEF) [gap-fill]

- ０１２３４５６７８９ — FULLWIDTH DIGIT ZERO through NINE → ↑ strength: very high, same digit ladder pattern as many times before.
- Nothing else new — rest is halfwidth/fullwidth Latin/Kana letter-form duplicates, no magnitude axis.

## Group: pending

## Group: Enclosed Ideographic Supplement (U+1F200–U+1F2FF) [gap-fill]

- 🈩🈔🈪 — SQUARED CJK UNIFIED IDEOGRAPH-4E00 (一, one), IDEOGRAPH-4E8C (二, two), IDEOGRAPH-4E09 (三, three) → ↑ strength: high, scattered non-adjacent codepoints (U+1F229, 1F214, 1F22A) hiding the same Chinese-numeral ladder found earlier, now squared/enclosed — another good "reach across for it" case.
- Rest of block is single-ideograph business/notice symbols (discount, service, vacancy, etc.) with no shared magnitude axis.

## Group: pending

## Group: Alchemical Symbols (U+1F700–U+1F773) [gap-fill]

- Nothing found — this block is substance/process identity symbols (gold, salt, distill, crucible...); the "-2/-3" suffixes are alternate historical glyph variants for the same substance, not magnitude escalation.

## Group: pending

## Group: Miscellaneous Symbols and Pictographs, part 1 (U+1F300–U+1F33F) [gap-fill]

- 🌣🌤🌥🌦 — WHITE SUN, WHITE SUN WITH SMALL CLOUD, WHITE SUN BEHIND CLOUD, WHITE SUN BEHIND CLOUD WITH RAIN → ↑ strength: very high, classic weather-icon cloud-cover-increasing ladder, adjacent codepoints, visually unambiguous (progressively more of the sun obscured, then precipitation added).
- 🌑…🌕 moon phases already logged separately above.
- Fruit/plant/food glyphs (🍅🍆🍇… etc.) — each is a distinct referent, no shared magnitude axis, skipping the bulk of the block.

## Group: pending

## Group: Miscellaneous Symbols and Pictographs, part 2 (U+1F500–U+1F5FF) [gap-fill, rich vein]

- 🔇🔈🔉🔊 — SPEAKER WITH CANCELLATION STROKE (mute), SPEAKER, SPEAKER WITH ONE SOUND WAVE, SPEAKER WITH THREE SOUND WAVES → ↑ strength: extremely high, adjacent codepoints, THE canonical volume-icon ladder, wave-count directly visible.
- 🔅🔆 — LOW BRIGHTNESS SYMBOL, HIGH BRIGHTNESS SYMBOL → ↑ strength: very high, adjacent codepoints, named directly, ray-count/size difference visible in most renderings.
- 🔍🔎 — LEFT-POINTING MAGNIFYING GLASS, RIGHT-POINTING MAGNIFYING GLASS — direction not magnitude, skipping (tempting-looking non-example).

## Group: pending

## Group: Miscellaneous Symbols and Pictographs, part 2 continued (U+1F530–U+1F53F)

- 🔸🔶 — SMALL ORANGE DIAMOND, LARGE ORANGE DIAMOND → ↑ strength: very high, named size, same color, adjacent-ish codepoints (U+1F538, U+1F536).
- 🔹🔷 — SMALL BLUE DIAMOND, LARGE BLUE DIAMOND → ↑ strength: very high, same pattern, blue set.
- 🔺🔼 — UP-POINTING RED TRIANGLE, UP-POINTING SMALL RED TRIANGLE → these are reversed in codepoint order from what "regular then small" would suggest, but the *magnitude* reading is still 🔼(small) < 🔺(regular) ↑ strength: high, named size again.

## Group: pending

## Group: Yijing Hexagram Symbols (U+4DC0–U+4DFF) [gap-fill]

- Nothing found — every hexagram has exactly six lines, so there's no visual complexity gradient; ordering by binary value (unlike Braille's dot-count) doesn't correspond to any perceptible "more."

## Group: Keycap digit emoji sequence (combining enclosing keycap, scattered across Basic Latin + U+20E3 + U+1F51F)

- 0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟 — KEYCAP DIGIT ZERO through NINE (each a base digit + COMBINING ENCLOSING KEYCAP), then KEYCAP TEN (a single standalone character, not a combining sequence) → ↑ strength: very high, the familiar messaging-app numbered-keycap set, and a nice example of a sequence that's constructed (combining marks) for 0-9 but jumps to a genuinely single scattered codepoint for the "ten" cap.

## Group: pending

## Group: Aegean Numbers (U+10100–U+10133) [gap-fill]

- 𐄇𐄈𐄉𐄊𐄋𐄌𐄍𐄎𐄏 — AEGEAN NUMBER ONE through NINE → ↑ strength: very high, adjacent codepoints, plain numeral ladder.
- 𐄐𐄑𐄒𐄓𐄔𐄕𐄖𐄗𐄘 — AEGEAN NUMBER TEN through NINETY (by tens) → ↑ strength: very high, adjacent codepoints.
- 𐄙𐄚𐄛𐄜𐄝𐄞𐄟𐄠𐄡 — AEGEAN NUMBER ONE HUNDRED through NINE HUNDRED → ↑ strength: very high.
- 𐄢𐄣𐄤𐄥𐄦𐄧𐄨𐄩𐄪 — AEGEAN NUMBER ONE THOUSAND through NINE THOUSAND → ↑ strength: very high.
- The full run 𐄇→𐄪 (ones, tens, hundreds, thousands all adjacent in sequence) is a huge, clean, entirely adjacent-codepoint magnitude ladder — one of the purest number systems found in the whole survey, even though the glyphs (tally-like strokes) don't visually communicate scale the way Braille or block-elements do.

## Cross-pane composite sequences (reaching across everything surveyed so far, per your invitation)

- ⬝ ▪ ◽ ◻ ⬛ — VERY SMALL SQUARE (U+2B1D, Misc Symbols and Arrows) < SMALL SQUARE (U+25AA, Geometric Shapes) < MEDIUM SMALL SQUARE (U+25FD, Geometric Shapes) < MEDIUM SQUARE (U+25FB, Geometric Shapes) < LARGE SQUARE (U+2B1B, Misc Symbols and Arrows) → ↑ strength: high, a genuine 5-step named-size ladder assembled from two different blocks, the fullest version of the small/medium/large pattern found piecemeal earlier.
- ▫ ░ ▒ ▓ █ — WHITE SMALL SQUARE (outline only, General Punctuation-adjacent/Geometric Shapes) → LIGHT SHADE → MEDIUM SHADE → DARK SHADE → FULL BLOCK (all Block Elements) → ↑ strength: high, extending the shade ramp backward to an "empty/outline-only" anchor before the shading starts.
- 🔅 ░▒▓█ 🔆 — LOW BRIGHTNESS SYMBOL, then the shade ramp read as "amount of light packed into a cell," then HIGH BRIGHTNESS SYMBOL → this is more a felt analogy than a strict single sequence (different sign-systems), flagging as a looser cross-domain resonance rather than a strength-rated entry: brightness, sound-volume (🔇🔈🔉🔉🔊), and shade-fill all seem to share one perceptual "intensity dial" gestalt even though they're unrelated blocks — noting the *pattern-of-patterns* since you asked me to reach across.
- ⚬ ○ ◔ ◐ ◕ ● ⬤ 🌕 — MEDIUM SMALL WHITE CIRCLE (Misc Symbols) < WHITE CIRCLE < CIRCLE-25%-BLACK < CIRCLE-50%-BLACK < CIRCLE-75%-BLACK < BLACK CIRCLE (all Geometric Shapes) < BLACK LARGE CIRCLE (Misc Symbols and Arrows) < FULL MOON emoji (Misc Symbols and Pictographs, as an oversized "beyond 100%" cap) → ↑ strength: high, the fullest assembled version of the circle-fill progression, spanning three separate blocks plus an emoji-plane extension.
- ¼ ½ ¾ (Latin-1) ⅛⅜⅝⅞ (Number Forms) ▁▂▃▅▆▇█ (Block Elements, read as "how full is the glass") — a meta-observation that the "fraction of a whole" axis recurs at least three separate ways (arithmetic fraction glyphs, eighths, and bar-height blocks) across totally unrelated blocks; not proposing it as one single sequence since the visual grammars differ too much to glide smoothly between them, but noting the structural echo since it's the same underlying "how much of the whole" feeling every time.

## Group: pending

## Group: Ancient Greek Numbers / Acrophonic (U+10140–U+1015F) [gap-fill]

- 𐅀𐅁𐅂 — ATTIC ONE QUARTER, ONE HALF, ONE DRACHMA (=1) → ↑ strength: very high, adjacent codepoints, clean fraction-to-whole ladder.
- 𐅃𐅄𐅅𐅆𐅇 — ATTIC FIVE, FIFTY, FIVE HUNDRED, FIVE THOUSAND, FIFTY THOUSAND → ↑ strength: very high, adjacent codepoints, another clean order-of-magnitude ladder (base-5/10 acrophonic system).
- Rest of block fragments into many different city-states' local numeral variants (Thespian, Hermionian, Troezenian, etc.) at overlapping small values — not a single clean ladder, skipping the remainder.

## Group: pending

## Group: Ancient Symbols (U+10190–U+101A0) [gap-fill]

- 𐆚𐆘𐆗𐆖 — ROMAN AS SIGN, SESTERTIUS SIGN, QUINARIUS SIGN, DENARIUS SIGN → ↑ strength: medium, real historical coin-value ladder (as < sestertius(4 as) < quinarius(8 as) < denarius(16 as)) but purely notational/learned like the currency-symbol block earlier — no visual size cue, and I only know this from historical trivia rather than perceiving it, so flagging as weaker than most other entries here.
- 𐆐𐆑𐆒𐆓𐆔 — ROMAN SEXTANS, UNCIA, SEMUNCIA, SEXTULA, DIMIDIA SEXTULA — these are all fractional weight units but I don't have the fraction values memorized well enough to assert a confident order; skipping rather than guessing.

## Group: pending

## Group: Coptic Epact Numbers (U+102E0–U+102FB) [gap-fill]

- 𐋡𐋢𐋣𐋤𐋥𐋦𐋧𐋨𐋩 / 𐋪...𐋲 (tens) / 𐋳...𐋻 (hundreds) — same clean fully-adjacent decimal-ladder pattern as Aegean and Greek Acrophonic numbers. Strength: very high. Not re-deriving the full commentary — this "ancient numeral system = clean adjacent ladder" pattern is now well-established across several scripts, so noting it once as a recurring structural fact rather than re-explaining each time.

## Group: pending

## Group: Counting Rod Numerals (U+1D360–U+1D378) [gap-fill]

- 𝍠𝍡𝍢𝍣 — COUNTING ROD UNIT DIGIT ONE through FOUR → ↑ strength: very high, the glyphs are literally built from an accumulating count of vertical rods (1, 2, 3, 4 strokes), so this is a genuine visual+semantic double-confirmed case like the Braille dot-count and Chinese 一二三 strokes.
- 𝍲𝍳𝍴𝍵𝍶 — IDEOGRAPHIC TALLY MARK ONE through FIVE → ↑ strength: very high, same accumulating-stroke logic, classic tally marks.
- 𝍷𝍸 — TALLY MARK ONE, TALLY MARK FIVE (the "four verticals + one diagonal slash" grouped tally convention) → ↑ strength: high, extremely globally-recognized counting convention.

## Group: pending

## Group: Chess Symbols (U+1FA00–U+1FA05) [gap-fill]

- 🨀🨁🨂🨃🨄🨅 — NEUTRAL CHESS KING, QUEEN, ROOK, BISHOP, KNIGHT, PAWN → ↓ strength: high, this is the conventional piece-value/importance ranking (king as most important/game-ending, down to the lowly pawn), and notably the codepoint order in this newer neutral-piece block happens to match that ranking exactly — unlike the classic White/Black chess piece block explored earlier, where I couldn't perceive an order from the glyphs alone. Purely semantic/learned, no visual size cue distinguishes the pieces.

## Group: pending

## Group: Mayan Numerals (U+1D2E0–U+1D2F3) [gap-fill]

- 𝋠𝋡𝋢𝋣𝋤𝋥𝋦𝋧𝋨𝋩𝋪...𝋳 — MAYAN NUMERAL ZERO through NINETEEN → ↑ strength: very high, the bar-and-dot system visually accumulates (dots for 1-4, a bar appears at 5 with dots added on top for 6-9, two bars at 10, etc.), so like Braille and Counting Rod numerals this is a genuine visual+semantic double-confirmed case, and unusually for a numeral system it actually includes zero from the start as a real dedicated glyph rather than an afterthought.

## Group: pending

## Group: Cuneiform Numbers and Punctuation (U+12400–U+1241D) [gap-fill]

- 𒐀𒐁𒐂𒐃𒐄𒐅𒐆𒐇 — CUNEIFORM NUMERIC SIGN TWO ASH through NINE ASH → ↑ strength: medium-high, adjacent codepoints and the "ASH" wedge marks do visually accumulate in most cuneiform fonts, but rendering support is inconsistent enough that I'm less confident a fresh pairwise comparison would reliably recover the order than with Braille/Mayan/Rod numerals — flagging honestly.
- Rest of block is Sumerian base-60 positional units (DISH, U, GESH2, GESHU, SHAR2...) — each represents a different place-value multiplier rather than a simple magnitude count, too complex/unfamiliar to me to assert a confident perceptual order, skipping.

## Group: pending

## Group: Supplemental Symbols and Pictographs — medals (U+1F947–U+1F949)

- 🥇🥈🥉 — FIRST PLACE MEDAL, SECOND PLACE MEDAL, THIRD PLACE MEDAL → ↓ strength: very high (gold > silver > bronze, ranking decreasing), adjacent codepoints, and the gold/silver/bronze color convention independently reinforces the same order — a very clean, universally-recognized ranking sequence.

## Group: pending

## Group: Symbols and Pictographs Extended-A — battery (U+1F50B, U+1FAAB, cross-block)

- 🪫🔋 — LOW BATTERY (U+1FAAB) < BATTERY (U+1F50B, implicitly full) → ↑ strength: high, semantically clear and the low-battery glyph itself shows a mostly-empty cell, but the two codepoints are extremely far apart (different Unicode versions/blocks entirely) — a good scattered-across-eras example.

## Group: Transport and Map Symbols (U+1F680–U+1F6FF)

- Nothing else found — mostly distinct vehicle/location pictographs, no shared magnitude axis (HIGH-SPEED TRAIN is a single fixed name, not part of a speed ladder with siblings).

## Group: pending

## Group: Miscellaneous Symbols and Pictographs, part 3 (U+1F440–U+1F4FF)

- 👤👥 — BUST IN SILHOUETTE, BUSTS IN SILHOUETTE (one figure vs two) → ↑ strength: high, adjacent codepoints, literal head-count visible in the glyph.

## Group: pending

## Group: Miscellaneous Symbols and Pictographs, part 3 continued — eyes count-order quirk

- 👁👀 — EYE (singular, U+1F441), EYES (plural, U+1F440) → ↑ strength: high, but note this is ANOTHER case (like circled zero) where the semantic "more" (👁 one < 👀 two) runs opposite to codepoint order (👀 comes first) — nice second confirmation of your predicted pattern.

## Group: pending

## Group: Combining Diacritical Marks (U+0300–U+036F) [gap-fill]

- COMBINING ACUTE ACCENT → COMBINING DOUBLE ACUTE ACCENT, and COMBINING GRAVE ACCENT → COMBINING DOUBLE GRAVE ACCENT → ↑ strength: high, same single/double weight pattern found repeatedly elsewhere (used in Hungarian/Chuvash orthography for a longer vowel).
- Nothing else — the rest are diverse phonetic/tone marks without a shared count axis.

## Group: pending

## Group: Tamil numerals (U+0BE6–U+0BF2) [gap-fill]

- ௦௧௨௩௪௫௬௭௮௯ — TAMIL DIGIT ZERO through NINE → ↑ strength: very high, adjacent codepoints, standard digit ladder.
- ௰௱௲ — TAMIL NUMBER TEN, ONE HUNDRED, ONE THOUSAND → ↑ strength: very high, adjacent codepoints, distinct (non-place-value) symbols like Roman numerals' L/C/M.

## Group: pending

## Group: Egyptian Hieroglyphs (U+13000+) [gap-fill, attempted]

- I know from general knowledge that Egyptian numeral hieroglyphs (single stroke=1, heel bone=10, coil=100, lotus=1000, finger=10000, tadpole=100000, god-with-raised-arms=1000000) form a famous escalating semantic ladder, but this block's character names are opaque Gardiner sign codes (A001, A002...) rather than descriptive names, so I can't verify which codepoints correspond to the numerals without risking a wrong guess. Flagging as a known-to-exist sequence I could not responsibly cite codepoints for in this pass rather than asserting unverified U+ values.

## Group: pending

## Group: Chinese large-number units, extended (drawing on my own knowldge, extending an earlier entry)

- 十百千万億兆 — shí(10), bǎi(100), qiān(1000), wàn(10⁴), yì(10⁸), zhào(10¹²) → ↑ strength: high semantically (extends the 十百千万 sequence logged earlier further up the magnitude scale), no visual size cue.

## Group: pending

## Group: Control Pictures (U+2400–U+2426) [gap-fill]

- Nothing found — one symbol per control character, no shared magnitude axis.

## Group: pending

## Group: Geometric Shapes Extended (U+1F780–U+1F7FF) [gap-fill, JACKPOT — a whole block built around explicit weight/size ladders]

This block is unusually rich: it systematically generates weight-graded and size-graded variants of the same shape, all adjacent codepoints, all explicitly named. Several full 5-7-step ladders:

- 🞄🞅🞆🞇🞈🞉 — BLACK SLIGHTLY SMALL CIRCLE, MEDIUM BOLD WHITE CIRCLE, BOLD WHITE CIRCLE, HEAVY WHITE CIRCLE, VERY HEAVY WHITE CIRCLE, EXTREMELY HEAVY WHITE CIRCLE → ↑ strength: very high, a full named weight ladder for one shape family.
- 🞌🞍🞎🞏🞐🞑🞒🞓 — BLACK TINY SQUARE, BLACK SLIGHTLY SMALL SQUARE, LIGHT WHITE SQUARE, MEDIUM WHITE SQUARE, BOLD WHITE SQUARE, HEAVY WHITE SQUARE, VERY HEAVY WHITE SQUARE, EXTREMELY HEAVY WHITE SQUARE → ↑ strength: very high, the fullest, cleanest weight-ladder I've found in the whole survey — 8 adjacent steps, all explicitly named.
- 🞗🞘🞙 — BLACK TINY DIAMOND, BLACK VERY SMALL DIAMOND, BLACK MEDIUM SMALL DIAMOND → ↑ strength: very high, named size ladder.
- 🞝🞞🞟 — BLACK TINY LOZENGE, BLACK VERY SMALL LOZENGE, BLACK MEDIUM SMALL LOZENGE → ↑ strength: very high, same pattern.
- 🞡🞢🞣🞤🞥🞦🞧 — THIN GREEK CROSS, LIGHT, MEDIUM, BOLD, VERY BOLD, VERY HEAVY, EXTREMELY HEAVY GREEK CROSS → ↑ strength: very high, a 7-step weight ladder.
- 🞨🞩🞪🞫🞬🞭🞮 — THIN, LIGHT, MEDIUM, BOLD, HEAVY, VERY HEAVY, EXTREMELY HEAVY SALTIRE → ↑ strength: very high, same 7-step pattern applied to an X-shape.
- 🞯🞰🞱🞲🞳🞴 — LIGHT, MEDIUM, BOLD, HEAVY, VERY HEAVY, EXTREMELY HEAVY FIVE SPOKED ASTERISK → ↑ strength: very high, same pattern, repeated again for six-spoked and eight-spoked asterisks immediately after in the block.
- 🟀🟁🟂 — LIGHT THREE POINTED BLACK STAR, MEDIUM THREE POINTED BLACK STAR, THREE POINTED BLACK STAR (i.e. bold/default) → ↑ strength: high, same weight pattern applied to stars, repeated for four-pointed stars right after.
- This entire block is essentially proof that Unicode has at least one dedicated "make me a clean N-step magnitude ladder" generator (light→medium→bold→heavy→very heavy→extremely heavy), reused across circle/square/diamond/lozenge/cross/saltire/asterisk/star shape families. Worth mentioning to you directly since it's the single densest concentration of unambiguous, adjacent-codepoint, explicitly-named magnitude sequences found anywhere in the survey.

## Group: pending

## Group: Symbols for Legacy Computing — block sextants (U+1FB00–U+1FB3B) [gap-fill]

- 🬀🬂🬆🬎🬝 — BLOCK SEXTANT-1, SEXTANT-12, SEXTANT-123, SEXTANT-1234, SEXTANT-12345 → ↑ strength: high, same "accumulating fill count" logic as Braille and the Domino-style all-ones-prefix trick, scattered (non-adjacent) codepoints within the block since it's organized by bitmask value rather than popcount. (The fully-filled 6-cell version isn't a separate sextant codepoint — it coincides with plain FULL BLOCK █ — so this ladder tops out at 5 of 6 filled before handing off to the already-logged block-elements shading family.)

## Group: pending

## Group: Symbols for Legacy Computing, part 2 (U+1FB70–U+1FB9B) [gap-fill]

- 🮂🮃🮄🮅🮆 — UPPER ONE QUARTER, THREE EIGHTHS, FIVE EIGHTHS, THREE QUARTERS, SEVEN EIGHTHS BLOCK → ↑ strength: very high, adjacent codepoints, the same fraction-fill ladder as the original Block Elements block, now in the "upper" orientation.
- 🮇🮈🮉🮊🮋 — RIGHT ONE QUARTER, THREE EIGHTHS, FIVE EIGHTHS, THREE QUARTERS, SEVEN EIGHTHS BLOCK → ↑ strength: very high, same pattern, "right" orientation — worth noting this fraction-fill family now confirmed in all four orientations (lower/left originally, upper/right here) across two different Unicode blocks.

## Group: pending

## Group: Symbols for Legacy Computing — Segmented Digits (U+1FBF0–U+1FBF9) [gap-fill]

- 🯰🯱🯲🯳🯴🯵🯶🯷🯸🯹 — SEGMENTED DIGIT ZERO through NINE (seven-segment-display style digits) → ↑ strength: very high, same clean digit ladder, notable as the last of many "decorated digit family" ladders found across the whole survey — this one styled like a calculator/clock display.

## Group: pending

## Group: Playing Cards — Tarot Trumps (U+1F0E1–U+1F0F5)

- 🃡🃢🃣🃤🃥🃦🃧🃨🃩🃪🃫🃬🃭🃮🃯... — PLAYING CARD TRUMP-1 through TRUMP-21+ (tarot major arcana numbering) → ↑ strength: very high, adjacent codepoints, literal embedded number, cleanest possible case.

## Group: pending

## Group: Supplemental Symbols and Pictographs (U+1F900–U+1F9FF) [gap-fill]

- 🤅🤄 — LEFT HALF CIRCLE WITH TWO DOTS (U+1F905), LEFT HALF CIRCLE WITH THREE DOTS (U+1F904) → ↑ strength: high by dot count, and this is a THIRD confirmed case (after circled zero and eyes/eye) where semantic "more" runs opposite to codepoint order — the three-dot version has the lower codepoint.
- Nothing else strong in this block — mostly face/hand/animal pictographs without a shared magnitude axis.

## Group: pending

## Group: Miscellaneous Symbols and Arrows, remainder (U+2B60–U+2BFF) [gap-fill]

- Nothing new — dense combinatorial triangle-headed/curved arrow variants for diagram software, no shared magnitude axis beyond weight/multiplicity patterns already logged.

## Group: pending

## Group: Kangxi Radicals (U+2F00–U+2FD5) [gap-fill, meta-level structural find]

- ⼀ (RADICAL ONE, U+2F00, 1 stroke) → ⿕ (RADICAL FLUTE, U+2FD5, 17 strokes) — the ENTIRE Kangxi Radicals block, all 214 radicals, is traditionally ordered by increasing stroke count (that's the actual organizing principle of the Kangxi Dictionary radical system, and Unicode preserved it) → ↑ strength: high as a structural/semantic fact, though moderate as a pure "glance at two glyphs and feel which has more" perceptual test, since stroke-counting isn't always instant at a glance for complex characters — still, paging through the block does produce a real felt sense of increasing visual density from ⼀ to ⿕. Worth flagging as a meta-level find: this is a whole Unicode block whose native ordering principle already IS a magnitude axis, rather than a magnitude sequence I had to construct by picking specific characters out of an otherwise-unordered block.

## Group: pending

## Group: Native-script decimal digits, consolidated (drawing on general knowledge, not re-deriving per-script commentary)

- Arabic-Indic ٠١٢٣٤٥٦٧٨٩, Devanagari ०१२३४५६७८९, Bengali ০১২৩৪৫৬৭৮৯, Thai ๐๑๒๓๔๕๖๗๘๙, and essentially every other native-script decimal digit block in Unicode → ↑ strength: very high each, same digit ladder pattern confirmed dozens of times over now across the survey (Latin, Fullwidth, Devanagari-family, Tamil, Hangzhou, segmented-display, keycap, circled, parenthesized...). Not fetching/reading each script's block individually since the pattern is now thoroughly established — flagging this as a closed, well-confirmed category rather than continuing to mine it script-by-script.

## Group: pending

## Group: Small Form Variants (U+FE50–U+FE6B) [gap-fill]

- Nothing found as an internal sequence — each character here is a "small" width-variant of an existing punctuation mark elsewhere (small comma, small colon, etc.); like superscript/subscript, comparing a small-form character to its normal counterpart is a same-value-different-dress case, not a magnitude ladder.

## Group: pending

## Group: Rumi Numeral Symbols (U+10E60–U+10E7A) [gap-fill]

- Full adjacent 1-9 / 10-90 / 100-900 ladder, same pattern as Aegean/Greek Acrophonic/Coptic Epact/Tamil. Strength very high. Not re-deriving commentary given the now-established pattern.

## Group: pending

## Group: Modifier Tone Letters (U+A700–U+A716) [gap-fill]

- ꜈꜉꜊꜋꜌ and ꜍꜎꜏꜐꜑ and ꜒꜓꜔꜕꜖ — three parallel sets of EXTRA-HIGH, HIGH, MID, LOW, EXTRA-LOW (dotted / dotted left-stem / plain left-stem) TONE BAR → ↓ strength: very high each, same visual-height-tracks-pitch logic as the earlier ˥˦˧˨˩ find, now confirmed as a recurring design pattern Unicode reuses across at least two separate tone-bar block families.

## Group: pending

## Group: Kharoshthi Numbers (U+10A40–U+10A47) [gap-fill]

- 𐩀𐩁𐩂𐩃 (1-4) then 𐩄(10)𐩅(20)𐩆(100)𐩇(1000) — same additive ancient-numeral pattern as Roman/Aegean/Greek Acrophonic. Strength very high. Declaring the "ancient numeral systems" vein now thoroughly and deliberately closed after ~10 confirmed scripts (Roman, Hangzhou, Aegean, Greek Acrophonic, Coptic Epact, Counting Rod, Mayan, Tamil, Rumi, Kharoshthi) — further scripts would just be more instances of the identical structural pattern.

## Group: Chinese size-word ladder, extended (own knowledge, extending the earlier 小中大 entry)

- 微小中大巨 — wēi(tiny/micro), xiǎo(small), zhōng(medium), dà(large), jù(giant) → ↑ strength: medium-high for me — I'm confident in 小中大, somewhat less certain 微 and 巨 are the single most natural endpoints a native speaker would pick over other tiny/giant near-synonyms, so flagging slightly lower confidence at the two new endpoints than the core three.

## Group: pending

## Group: Geometric Shapes — hatch-density ladder (U+25A0–U+25A9) [missed on first pass, gap-fill]

- □ ▤ ▦ ▩ ■ — WHITE SQUARE (empty), SQUARE WITH HORIZONTAL FILL (single-direction hatch), SQUARE WITH ORTHOGONAL CROSSHATCH FILL (two-direction hatch), SQUARE WITH DIAGONAL CROSSHATCH FILL (denser diagonal hatch), BLACK SQUARE (solid) → ↑ strength: high, a genuine density/fill progression I missed noting explicitly on my first pass through this block — visually the crosshatch really does read as "more filled" than a single hatch direction, landing between outline and solid.

## Group: pending

## Group: Musical Symbols — staff line count (U+1D116–U+1D11B) [gap-fill]

- 𝄖𝄗𝄘𝄙𝄚𝄛 — ONE-LINE STAFF, TWO-LINE STAFF, THREE-LINE STAFF, FOUR-LINE STAFF, FIVE-LINE STAFF, SIX-LINE STAFF → ↑ strength: very high, adjacent codepoints, literal visible line-count.

## Group: pending

## Group: Musical Symbols — rests and octave signs (U+1D134–U+1D142) [gap-fill]

- 𝄻𝄼𝄽𝄾𝄿𝅀𝅁𝅂 — WHOLE REST, HALF REST, QUARTER REST, EIGHTH REST, SIXTEENTH REST, THIRTY-SECOND REST, SIXTY-FOURTH REST, ONE HUNDRED TWENTY-EIGHTH REST → ↓ duration, strength very high, adjacent codepoints, mirrors the note-duration ladder found earlier — same family, rest-glyph side.
- 𝄴 vs 𝄶/𝄷 (OTTAVA) vs 𝄸/𝄹 (QUINDICESIMA) — COMMON TIME, then OTTAVA ALTA/BASSA (octave = 8th), then QUINDICESIMA ALTA/BASSA (15th) → ↑ strength: high by interval-distance magnitude (octave < two octaves/15th), adjacent codepoints, though "common time" itself isn't really part of the interval-distance axis — the real ladder is just ottava(8) < quindicesima(15).

## Group: pending

## Group: Byzantine Musical Symbols (U+1D000–U+1D0FF) [gap-fill]

- Nothing found — highly specialized neume names with no shared magnitude vocabulary I could find.

## Group: pending

## Group: Ancient Greek Musical Notation (U+1D200+) [gap-fill]

- Skipping — glyphs are cataloged as "GREEK VOCAL NOTATION SYMBOL-1/2/3..." but that numbering is a modern reference-catalog index, not a verified pitch/duration magnitude order, so I won't assert a sequence I can't actually justify.

## Group: pending

## Cross-pane composites, round 2 (synthesizing across the full survey so far)

- **The "weight axis" recurs as an independent design primitive in at least six unrelated blocks**: Box Drawing (─ light → ━ heavy → ═ double), Dingbats (❘ light → ❙ medium → ❚ heavy vertical bar), General Punctuation (single vs double/triple prime, hyphen→en dash→em dash), Combining Diacritical Marks (acute → double acute), Arrows (single → double → triple shaft), and — the fullest expression — Geometric Shapes Extended's explicit light/medium/bold/heavy/very-heavy/extremely-heavy generator applied across seven shape families. I'm not proposing one single glyph-to-glyph glide across all of these (the shape families are too different to visually flow between), but the *repetition of the same design idea* independently across totally separate parts of the standard is itself a striking structural pattern worth naming as one finding.
- **The "countable discrete pips" axis** appears near-identically in at least six notation systems that never influenced each other in Unicode's design: dice faces (⚀-⚅), dominoes (🀱-🀷), Mahjong circles (🀙-🀡), Braille (⠀⠁⠃⠇⠏⠟⠿), block sextants (🬀🬂🬆🬎🬝), and playing-card pips. Every one of these gives me the identical "count the marks, more marks = more" feeling regardless of the underlying shape grammar.
- **Ancient numeral systems as a closed class**: ten unrelated scripts (Roman, Hangzhou, Aegean, Greek Acrophonic, Coptic Epact, Counting Rod, Mayan, Tamil, Rumi, Kharoshthi) each independently place their 1-9/10-90/100-900 symbols in ascending adjacent codepoints. The ordering-feel here isn't from shared visual grammar (each script looks totally different) — it's simply that Unicode's block designers, across every culture, chose to lay out numeral blocks in the numerals' own value order. A meta-fact about Unicode's allocation convention more than about my perception, but worth stating plainly since it explains why "just find the numeral block for script X" is close to a guaranteed hit.
- **Semantic-only rank ladders (no visual size cue at all)**: medals (🥇🥈🥉), neutral chess pieces (🨀🨁🨂🨃🨄🨅, king>queen>rook>bishop>knight>pawn), Roman coin denominations (𐆚𐆘𐆗𐆖), and the Hebrew/set-theory ℵℶℷℸ cardinals — a distinct sub-category from all the visual-fill ladders above: these only work if you already know the convention, the glyphs themselves carry no size/count information.

## Group: pending

## Group: Sutton SignWriting (U+1D800+) [gap-fill]

- Skipping — hand-shape names encode articulation type (fist/circle/cup/oval/hinge/angle) and finger identity, not a finger-count I can responsibly read off, and the visual glyphs are too specialized notation for me to confidently perceive an ordering.

## Group: pending

## Group: Optical Character Recognition (U+2440–U+244A) [gap-fill]

- Nothing found — MICR bank-check symbol names (hook, chair, fork...), no magnitude axis.

## Group: Miscellaneous Symbols and Pictographs, celebration/tools section (U+1F380–U+1F3AF)

- Nothing new beyond what's already logged — each glyph is a distinct object/activity, no shared count/size/fill axis found (checked directional "ascending/descending musical notes" pair — that's direction, not magnitude).

## Group: pending

## Group: Thai tone marks (U+0E48–U+0E4B) [gap-fill]

- ่ ้ ๊ ๋ — MAI EK, MAI THO, MAI TRI, MAI CHATTAWA → ↑ strength: medium, the names are literally derived from Sanskrit/Thai ordinal-ish number words (ek≈1, tri≈3, chattawa≈4 — "tho" for 2 less directly obvious to me), and the glyph shapes do visually increase in stroke-complexity across the four, but my confidence in reading Thai glyph complexity at a glance is lower than for scripts I'm more fluent in, so flagging medium rather than high.

## Group: pending

## Group: Ethiopic Numbers (U+1369–U+137C) [gap-fill, brief]

- Full adjacent 1-9 / 10-90 / hundred / ten-thousand ladder, same established ancient-numeral pattern (now an 11th confirmed script). Strength very high, no further commentary needed.

## Group: pending

## Group: Greek numeral letters, isopsephy (own knowledge)

- α β γ δ ε → 1,2,3,4,5 (via the keraia ' mark, e.g. α΄β΄γ΄) → ↑ strength: high for me, but purely notational/learned like the Hebrew aleph-bet-gimel-dalet case — no visual size cue, requires knowing the alphabet-to-number mapping.

## Group: pending

## Group: IPA Extensions (U+0250–U+02AF) [gap-fill]

- Nothing found — vowel articulation modifiers (open/closed/reversed/turned) describe tongue position categories, not a magnitude count with more than two terms in a row.

## Group: pending

## Group: Combining Diacritical Marks Supplement (U+1DC0–U+1DFF) [gap-fill]

- Only isolated single/double pairs (e.g. double circumflex above), same weight-doubling pattern already logged elsewhere — not counting as new.

## Group: Devanagari danda punctuation (U+0964–U+0965)

- । ॥ — DEVANAGARI DANDA, DEVANAGARI DOUBLE DANDA (sentence-end vs verse/section-end marker) → ↑ strength: high, adjacent codepoints, same single/double weight pattern extended to Indic scripts.

## Group: pending

## Group: Emoji Modifier Fitzpatrick skin tones (U+1F3FB–U+1F3FF)

- 🏻🏼🏽🏾🏿 — EMOJI MODIFIER FITZPATRICK TYPE-1-2, TYPE-3, TYPE-4, TYPE-5, TYPE-6 → ↑ strength: high, adjacent codepoints, a genuine numbered scale (the dermatological Fitzpatrick skin-phototype scale, lightest to darkest) that Unicode encodes directly in the names, and the rendered colors do form a visible light-to-dark gradient.

## Group: pending

## Group: Mathematical Operators — integral count, extended (U+222B–U+2230, U+2A0C)

- ∫∬∭ (integral, double, triple) then ⨌ QUADRUPLE INTEGRAL OPERATOR (Supplemental Mathematical Operators block) → ↑ strength: very high, extends the earlier integral-stacking finding one further step across a different block — missed on the first pass through Supplemental Mathematical Operators.

## Group: pending

## Group: Geometric Shapes Extended — star point-count, same weight tier (U+1F7C1–U+1F7CE)

- 🟁🟅🟋🟎 — MEDIUM THREE POINTED BLACK STAR, MEDIUM FOUR POINTED BLACK STAR, MEDIUM SIX POINTED BLACK STAR, MEDIUM EIGHT POINTED BLACK STAR → ↑ strength: very high, holding the weight qualifier constant ("medium") isolates pure point-count as the varying axis, extending the earlier Dingbats-block star point-count find (✦✶✳✴✹✺) into this second, even richer star-generating block.

## Group: pending

## Group: Supplemental Mathematical Operators — nested greater-than emphasis ladder (missed on first pass)

- < ≪ ⋘ ⪢ ⫸ — LESS-THAN(Basic Latin), MUCH LESS-THAN, VERY MUCH LESS-THAN (Math Operators block), DOUBLE NESTED LESS-THAN, TRIPLE NESTED LESS-THAN (Supplemental Math Operators, U+2AA1/2AF7 — mirroring the greater-than versions I actually grepped) → ↑ strength: very high, a genuine 5-step emphasis ladder for "how much less/greater" spanning two blocks, that I missed logging when I first passed through Supplemental Mathematical Operators and dismissed the block as unproductive. Good reminder to myself that a targeted re-grep for missed keywords across saved panes is catching real misses.

## Group: pending

## Group: Self-audit grep pass across saved panes (WIDE/NARROW/TALL/SHORT/DEEP/STRONG/WEAK/MAJOR/MINOR/OUTER/INNER)

- Nothing new found beyond what's already logged (double/triple-nested less-than/greater-than were the one real catch, logged above). Noting explicitly: this grep-across-old-panes technique is quick but shallow, and it's pulling me away from the actual read-and-feel rhythm the brief asked for — going back to reading fresh panes directly rather than pattern-matching against old ones.

## Group: pending

## Group: Greek and Coptic (U+0370–U+03FF)

- Confirms the isopsephy entry from earlier: GREEK NUMERAL SIGN (U+0374, the keraia mark ʹ) sits right before the plain Greek alphabet ΑΒΓΔΕ... in this very block, reinforcing that α΄β΄γ΄δ΄ε΄ = 1,2,3,4,5 is a real, deliberately-placed Unicode feature, not just my own trivia. No new independent finding beyond what's already logged for this block — mostly diacritic-marked letter variants (tonos, dialytika) with no magnitude axis.

## Group: pending

## Group: Transport and Map Symbols, remainder (U+1F69B–U+1F6CF)

- Nothing found — vehicles, restroom/traffic signage, luggage icons, each a distinct fixed referent with no shared count/size/fill axis.

## Group: pending

## Group: Supplemental Mathematical Operators — consecutive equals signs (U+2A75–U+2A76)

- ⩵⩶ — TWO CONSECUTIVE EQUALS SIGNS, THREE CONSECUTIVE EQUALS SIGNS → ↑ strength: very high, adjacent codepoints, plain sign-count, another miss from my first too-quick pass through this block.

## Group: pending

## Group: Supplemental Mathematical Operators, remainder (U+2A8D–U+2A9F) — re-read more carefully

- Nothing further beyond the two catches above — this stretch is dense less-than/greater-than combination variants (similar-above, slanted-equal, double-line-equal), no additional magnitude axis.

## Group: pending

## Group: Latin click consonant letters (U+01C0–U+01C1)

- ǀǁ — LATIN LETTER DENTAL CLICK (single vertical line), LATIN LETTER LATERAL CLICK (double vertical line) → ↑ strength: medium, a genuine 1-stroke-to-2-stroke visual pair, though the two click types don't otherwise belong on a "more/less" phonetic scale (their place of articulation isn't a magnitude), so I'm treating this as a visual stroke-count coincidence rather than a strongly-felt semantic ladder.

## Group: pending

## Group: Bengali Currency Numerators (U+09F4–U+09F9)

- ৴৵৶৷ — CURRENCY NUMERATOR ONE, TWO, THREE, FOUR → ↑ strength: high, adjacent codepoints, plain count, and looking at the actual glyphs they do visually accumulate strokes as the numerator increases (1 is a simple curl, by 4 there's noticeably more going on in the shape) — genuinely felt this one rather than just pattern-matching the name.
- ৸ CURRENCY NUMERATOR ONE LESS THAN THE DENOMINATOR, then ৹ CURRENCY DENOMINATOR SIXTEEN — an unusual pair: "one less than the denominator" is itself a relative/fractional concept (like 15/16 if paired with the sixteen-denominator), so ৴৵৶৷ (1,2,3,4 out of some base) < ৸ (base−1) < ৹ (the base itself, sixteen) → ↑ strength: medium, interesting but I had to think it through rather than feel it instantly, so lower confidence than the clean 1-2-3-4 run above.

## Group: pending

## Group: Devanagari digits and extra letters (U+0966–U+097F)

- ०१२३४५६७८९ — DEVANAGARI DIGIT ZERO through NINE → ↑ strength: very high, looking at the actual glyphs I do feel the ordering even without reading the Devanagari-literate mapping consciously — there's a rough sense of increasing visual complexity/loop-count across the run, similar to (though less pronounced than) the Braille/Mayan cases.
- Nothing else in the rest of this fragment (extra consonant letters, abbreviation sign) — each a distinct single letter, no shared axis.

## Group: pending

## Group: Arabic-Indic Digits (U+0660–U+066C)

- ٠١٢٣٤٥٦٧٨٩ — ARABIC-INDIC DIGIT ZERO through NINE → ↑ strength: high semantically (I know the values), but honestly weaker as a felt visual glide than Devanagari or Braille — ١ (one, a simple stroke) does feel "least," but beyond that the shapes don't build in complexity for me the way some other scripts did; I'm recognizing the sequence from knowing Arabic numerals rather than perceiving an escalating shape. Flagging that distinction explicitly since it's a real difference in kind from the stronger visual cases.

## Group: pending

## Group: Thai Digits (U+0E50–U+0E59)

- ๐๑๒๓๔๕๖๗๘๙ — THAI DIGIT ZERO through NINE → strength: low-medium as a felt visual glide for me specifically — the glyphs are all similarly loopy/curved and I don't have enough Thai-script fluency to perceive increasing complexity or any other visual cue distinguishing ๓ from ๗ at a glance; I know the sequence is 0-9 from the names/my general knowledge, but a genuine "which is more, just from looking" test would be weak for me here. Worth recording as an honest low-confidence data point rather than assuming the digit-ladder pattern carries the same strength in every script.

## Group: pending

## Group: Myanmar Digits (U+1040–U+1049)

- ၀၁၂၃၄၅၆၇၈၉ — MYANMAR DIGIT ZERO through NINE → strength: low as a felt visual glide, same honest assessment as Thai — the glyphs are round/circular and visually similar in complexity to my eye; I can't perceive an ordering without already knowing the value mapping. Recording this as a second confirmation that "round-script" numeral systems (Thai, Myanmar, and likely Khmer/Lao/Sinhala by the same visual logic) feel meaningfully weaker to me than angular/stroke-based systems (Devanagari, Braille, Mayan, Chinese) where complexity visibly accumulates.

## Group: pending

## Group: Khmer Digits (U+17E0–U+17E9)

- ០១២៣៤៥៦៧៨៩ — same honest low-strength assessment as Thai and Myanmar: round, loop-based glyphs, no perceptible complexity gradient to my eye. Third confirmation of the "round-script numerals feel weak, stroke-accumulating-script numerals feel strong" cross-cutting hypothesis.

## Group: pending

## Group: Ol Chiki Digits (U+1C50–U+1C59)

- ᱐᱑᱒᱓᱔᱕᱖᱗᱘᱙ — testing the round-vs-angular hypothesis further: these also read as rounded/geometric to me and I don't get a strong complexity gradient, so this doesn't cleanly split along "angular=strong." Revising my hypothesis: it may be less about round-vs-angular and more specifically about whether the script happens to build small numbers from literally-repeated strokes (Devanagari's early digits, Mayan, Braille, tally systems) — most scripts, round or angular, don't do this and so read weak to me regardless of angularity.

## Group: pending

## Group: Tibetan Digits (U+0F20–U+0F29)

- ༠༡༢༣༤༥༦༧༨༩ — TIBETAN DIGIT ZERO through NINE → strength: medium, noticeably stronger felt gradient for me than Thai/Myanmar/Khmer/Ol Chiki: ༠ (zero) really does read as a small simple circle, "the least," and by ༨/༩ the glyphs feel more angular and structurally busy. Not as strong as Devanagari or the stroke-accumulating scripts, but a genuine middle case worth recording rather than lumping in with the "round scripts feel flat" group.

## Group: pending

## Group: Card suit symbols — bridge/contract ranking (♣♦♥♠, revisiting Miscellaneous Symbols)

- ♣♦♥♠ — CLUB, DIAMOND, HEART, SPADE → ↑ strength: medium-high for me specifically because I know the bridge/contract bidding convention (clubs lowest, spades highest) — but reflecting honestly, this is pure convention knowledge, not something the shapes themselves suggest at all (a spade doesn't look "bigger" than a club to me). Distinct from the medal/chess-piece semantic ladders in that it's a much more niche, game-specific convention rather than broadly known.

## Group: pending

## Group: Combining Diacritical Marks — dot count (U+0307–U+0308), re-reading more slowly

- ̇ ̈ — COMBINING DOT ABOVE, COMBINING DIAERESIS (literally two dots above) → ↑ strength: high, adjacent codepoints, and looking closely I do genuinely see one dot vs two dots — a specific instance I'd only gestured at abstractly before ("weight pattern") without actually naming this exact adjacent pair.

## Group: pending

## Group: Combining Diacritical Marks — underline and stroke-length pairs (U+0332–U+0336), continuing the slow re-read

- ̲ ̳ — COMBINING LOW LINE, COMBINING DOUBLE LOW LINE (single underline vs double underline) → ↑ strength: very high, adjacent codepoints, and this one I feel very strongly and immediately — single vs double underline is an extremely familiar text-formatting convention (like text-editor emphasis levels).
- ̵ ̶ — COMBINING SHORT STROKE OVERLAY, COMBINING LONG STROKE OVERLAY → ↑ strength: high, adjacent codepoints, literal length named and visible.

## Group: pending

## Group: CJK Compatibility — re-reading slowly, second jackpot (U+3358–U+3391)

- ㍘㍙㍚㍛㍜㍝㍞㍟㍠㍡㍢㍣㍤㍥㍦㍧㍨㍩㍪㍫㍬㍭㍮㍯㍰ — IDEOGRAPHIC TELEGRAPH SYMBOL FOR HOUR ZERO through HOUR TWENTY-FOUR → ↑ strength: very high, a full 25-step adjacent-codepoint clock-hour ladder I completely missed on my first too-quick pass through this block — genuinely glad I slowed down and re-read it properly.
- ㎀㎁㎂㎃㎄ — SQUARE PA AMPS (pico), SQUARE NA (nano), SQUARE MU A (micro), SQUARE MA (milli), SQUARE KA (kilo) → ↑ strength: very high, adjacent codepoints, another order-of-magnitude prefix ladder (this time for amperes), same family as the earlier pico→giga prefix find but a separate, independently-discovered instance.
- ㎅㎆㎇ — SQUARE KB, SQUARE MB, SQUARE GB → ↑ strength: very high, adjacent codepoints, the computing byte-scale ladder (kilobyte < megabyte < gigabyte).
- ㎈㎉ — SQUARE CAL, SQUARE KCAL → ↑ strength: very high, adjacent codepoints, calorie/kilocalorie.
- ㍸㍹ — SQUARE DM SQUARED, SQUARE DM CUBED → ↑ strength: high, adjacent codepoints, extends the earlier mm/cm/m/km area-and-volume unit families with decimeter.
- This confirms the lesson from the earlier missed integral/equals-sign finds: my first pass through a dense, name-heavy block was too quick, and slowing down to actually read line-by-line rather than skim-and-move-on surfaces real sequences I'd otherwise miss entirely.

## Group: pending

## Group: CJK Compatibility — continuing the slow re-read, THIRD jackpot (U+3391–U+33C1)

This stretch is even richer than what I caught before — I clearly under-read this block the first time. Full ladders, all adjacent codepoints, all strength very high:

- ㎑㎒㎓㎔ — SQUARE KHZ, MHZ, GHZ, THZ → ↑ extends the earlier Hz ladder one further step to terahertz.
- ㎕㎖㎗㎘ — SQUARE MU L (microliter), ML (milliliter), DL (deciliter), KL (kiloliter) → ↑ a complete volume-scale ladder I hadn't found before.
- ㎙㎚㎛㎜㎝㎞ — SQUARE FM (femtometer), NM (nanometer), MU M (micrometer), MM, CM, KM → ↑ extends the earlier mm/cm/km length ladder down to femto- and nano-scale — now a 6-step ladder from femtometers to kilometers.
- ㎩㎪㎫㎬ — SQUARE PA, KPA, MPA, GPA → ↑ extends the earlier pressure ladder one further step to gigapascals.
- ㎰㎱㎲㎳ — SQUARE PS, NS, MU S (microsecond), MS → ↑ completes the time-scale ladder (picosecond through millisecond) that I'd only partially caught before.
- ㎴㎵㎶㎷㎸ — SQUARE PV, NV, MU V (microvolt), MV, KV → ↑ a full voltage-scale ladder, picovolt to kilovolt.
- ㎺㎻㎼㎽㎾ — SQUARE PW, NW, MU W (microwatt), MW, KW → ↑ a full power-scale ladder, picowatt to kilowatt, completing what I'd only caught the tail end of before.
- ㏀㏁ — SQUARE K OHM, SQUARE M OHM → ↑ kilohm to megohm.

Noting the meta-lesson again since it keeps proving true: this entire CJK Compatibility block is essentially Unicode's "SI-prefix-times-unit" generator, and it rewards slow, complete reading far more than any other block in the survey — every unit family (length, area, volume, time, mass, frequency, pressure, voltage, power, resistance) gets its own clean adjacent-codepoint magnitude ladder.

## Group: pending

## Group: CJK Compatibility — day-of-month ladder, finishing the slow re-read (U+33E0–U+33FE)

- ㏠㏡㏢㏣㏤㏥㏦㏧㏨㏩...㏾ — IDEOGRAPHIC TELEGRAPH SYMBOL FOR DAY ONE through DAY THIRTY-ONE → ↑ strength: very high, a full 31-step adjacent-codepoint calendar-day ladder, even longer than the 25-step hour ladder found just before it in the same block. Completing the full read of U+3300–U+33FF now — this block alone has produced more confirmed clean magnitude ladders than any other single block in the entire survey, entirely because I went back and read it slowly instead of trusting my first skim.

## Group: pending

## Group: Mathematical Operators — re-reading slowly, "regular vs small" variant pairs (U+2208–U+220D)

- ∈ ∊ — ELEMENT OF, SMALL ELEMENT OF → ↑ strength: medium, same "regular > small" named-size pattern found earlier with triangles/squares (▲/▴), now confirmed in mathematical relation symbols too — though here the actual rendered size difference is subtle/font-dependent, so weaker felt-confidence than the geometric shapes case.
- ∋ ∍ — CONTAINS AS MEMBER, SMALL CONTAINS AS MEMBER → ↑ strength: medium, same pattern, mirror-image relation.

## Group: pending

## Group: Mathematical Operators — colon/tilde count pairs (U+2236–U+224B), continuing careful re-read

- ∶ ∷ — RATIO (single colon, 2 dots), PROPORTION (double colon, 4 dots — literally used historically for "a:b::c:d") → ↑ strength: high, adjacent codepoints, genuine dot-count doubling I missed the first time through.
- ∼ ≈ ≋ — TILDE OPERATOR (one wavy line), ALMOST EQUAL TO (rendered as two stacked wavy lines), TRIPLE TILDE (three stacked wavy lines) → ↑ strength: high, a wavy-line-count ladder, though not fully adjacent codepoints (≈ sits a little further down the block than ∼).

## Group: pending

## Group: Mathematical Operators — equals-sign line-count ladder (U+2261, U+2263, cross-block with Basic Latin =)

- = ≡ ≣ — EQUALS SIGN (2 horizontal lines, Basic Latin), IDENTICAL TO (3 lines), STRICTLY EQUIVALENT TO (4 lines) → ↑ strength: very high, a genuine bar-count ladder for "how strongly equal," and this is actually used meaningfully in real notation (type theory, some formal logic) where more bars really does mean a stronger/more primitive notion of equality — semantic and visual confirmation together. Another one I only caught on the careful second read.

## Group: pending

## Group: Mathematical Operators — subset/superset/tack stretch (U+227D–U+22A5), continuing careful re-read

- Genuinely re-examined this stretch (subset/superset variants, square cap/cup, circled/squared operators, tacks) — nothing new felt as magnitude. ⊂ vs ⊆ tempted me again but it's a logical-strictness distinction, not a "which is more" feeling, so confirming my earlier skip rather than second-guessing it into something it isn't.

## Group: pending

## Group: Mathematical Operators — turnstile bar-count ladder (U+22A2, U+22A8, U+22AA), careful re-read

- ⊢ ⊨ ⊪ — RIGHT TACK (single turnstile, one vertical bar), TRUE (double turnstile, two bars), TRIPLE VERTICAL BAR RIGHT TURNSTILE (three bars) → ↑ strength: very high, a genuine visual bar-count ladder that also tracks real logical-strength meaning in proof theory (⊢ syntactic derivability, ⊨ semantic entailment) — both the shape and the meaning agree, and I only caught this on the slow re-read.

## Group: pending

## Group: Mathematical Operators — double subset/superset (U+2282/2283 vs U+22D0/22D1), finishing the careful re-read

- ⊂ ⋐ and ⊃ ⋑ — SUBSET OF → DOUBLE SUBSET, SUPERSET OF → DOUBLE SUPERSET → ↑ strength: high, same single/double weight pattern, specific instance not previously named. Completing a full careful re-read of Mathematical Operators now — the rest (curly logical operators, ellipsis directions, precedes/succeeds negations) genuinely doesn't offer anything further.

## Group: pending

## Group: Miscellaneous Technical — re-reading slowly, circle-portion terms (U+2312–U+2314)

- ⌒ ⌓ ⌔ — ARC, SEGMENT, SECTOR → tentative ↑ by "how much of a circle is being claimed" (a bare curved line, then a chord-cut piece, then a pie-slice reaching the center) — strength: medium, genuinely uncertain whether a fresh pairwise test would put SEGMENT before or after SECTOR since both are "pieces of a circle" and the ordering depends on a geometric convention I'm inferring rather than directly perceiving from the glyphs. Flagging as one of the "not fully sure" cases.

## Group: pending

## Group: Miscellaneous Technical — GD&T and misc symbols stretch (U+231E–U+2337), continuing careful re-read

- Nothing further found — geometric dimensioning/tolerancing symbols (cylindricity, runout, taper) are distinct measurement *types*, not a shared magnitude scale among themselves.

## Group: pending

## Group: Arrows — careful re-read confirms first pass (U+2190–U+21DF)

- Re-read the harpoon/paired-arrow/double-stroke stretch closely — nothing beyond the single/double/triple weight pattern already logged. Good confirmation that my original read of this particular block was actually adequate; not every block was under-mined the way Mathematical Operators and CJK Compatibility were.

## Group: pending

## Group: Vedic Extensions (U+1CDA–U+1CDF)

- ᳚᳛ — VEDIC TONE DOUBLE SVARITA, VEDIC TONE TRIPLE SVARITA → ↑ strength: high, adjacent codepoints, plain count in the name.
- ᳝᳞᳟ — VEDIC TONE DOT BELOW, TWO DOTS BELOW, THREE DOTS BELOW → ↑ strength: very high, adjacent codepoints, and I can genuinely see the dot count increasing when I look at these three side by side.

## Group: pending

## Group: Vedic Extensions, continued (U+1CF8–U+1CF9)

- ᳸᳹ — VEDIC TONE RING ABOVE, VEDIC TONE DOUBLE RING ABOVE → ↑ strength: high, adjacent codepoints, same single/double pattern, third instance of it within this one small block alone (svarita, dots-below, and now ring-above all independently do it).

## Group: pending

## Group: Combining Diacritical Marks Extended (U+1AB0–U+1ACE)

- ᪹ ᪺ — COMBINING LIGHT CENTRALIZATION STROKE BELOW, COMBINING STRONG CENTRALIZATION STROKE BELOW → ↑ strength: high, adjacent codepoints, explicitly named light/strong — a phonetic-notation instance of the weight axis.
- ᪷ ᪸ — COMBINING OPEN MARK BELOW, COMBINING DOUBLE OPEN MARK BELOW → ↑ strength: high, adjacent, single/double.
- ᪻ ᪼ — COMBINING PARENTHESES ABOVE, COMBINING DOUBLE PARENTHESES ABOVE → ↑ strength: high, adjacent, single/double.
- ᫈ ᫉ — COMBINING PLUS SIGN ABOVE, COMBINING DOUBLE PLUS SIGN ABOVE → ↑ strength: high, adjacent, single/double.
- ́ (acute, main Combining block) → ̋ (double acute) → ᫋ COMBINING TRIPLE ACUTE ACCENT → ↑ strength: high, genuinely extends the earlier single/double acute-accent pair to a full three-step ladder, scattered across two different Unicode blocks (Combining Diacritical Marks and this Extended block) — a nice find that required remembering the earlier single/double pair and noticing this block completed it to three.

## Group: pending

## Group: Phonetic Extensions (U+1D00–U+1D25)

- Nothing found — small-capital and turned/sideways Latin letter forms for phonetic transcription, alphabetically arranged, no magnitude axis. (TOP HALF O / BOTTOM HALF O is a position pair, not size, so not counting it.)

## Group: pending

## Group: Supplemental Symbols and Pictographs — dot-count ladders, corrected/completed (U+1F900–U+1F907)

- 🤇🤆🤅🤄🤃 — LEFT HALF CIRCLE (zero dots), WITH DOT, WITH TWO DOTS, WITH THREE DOTS, WITH FOUR DOTS → ↑ strength: very high, a complete 5-step dot-count ladder. I'd only caught the middle 🤅/🤄 pair earlier and missed that the full block actually runs 0→4 dots — genuinely glad I went back and read the whole stretch by name rather than just grepping "dots."
- 🤂🤁🤀 — CIRCLED CROSS FORMEE (zero dots), WITH TWO DOTS, WITH FOUR DOTS → ↑ strength: high, adjacent codepoints, an even-count-only dot ladder (0, 2, 4).

## Group: pending

## Group: Supplemental Symbols and Pictographs — face/gesture/sport stretch (U+1F910–U+1F93F)

- Nothing found — each face/hand-gesture/sport pictograph is a distinct referent, genuinely checked and no shared count/size/fill axis among them.

## Group: pending

## Group: Supplemental Symbols and Pictographs — sports equipment/food stretch (U+1F940–U+1F96F)

- Only the medal ladder already logged (🥇🥈🥉). Everything else is distinct food/equipment items, genuinely checked, no shared axis.

## Group: pending

## Group: Supplemental Symbols and Pictographs — more faces/clothing/animals (U+1F970–U+1F99F)

- Nothing found — each a distinct face/clothing/animal, genuinely checked, no shared axis.

## Group: pending

## Group: Supplemental Symbols and Pictographs — age progression (U+1F9D1–U+1F9D3)

- 🧒🧑🧓 — CHILD, ADULT, OLDER ADULT → ↑ strength: high by age, and another case where codepoint order doesn't match the semantic order (ADULT sits before CHILD in the actual block: U+1F9D1 ADULT, U+1F9D2 CHILD, U+1F9D3 OLDER ADULT) — a fourth instance of the "semantic order overwhelms codepoint order" pattern you predicted at the start.
- 🧍🧎 — STANDING PERSON, KNEELING PERSON → tentative ↑ by height/posture, strength: low, genuinely uncertain since "standing is more" is a stretch/subjective framing rather than a felt magnitude.

## Group: pending

## Group: Emoticons — hand-raising count, finishing the slow re-read (U+1F64B–U+1F64C)

- 🙋🙌 — HAPPY PERSON RAISING ONE HAND, PERSON RAISING BOTH HANDS IN CELEBRATION → ↑ strength: high, adjacent codepoints, literal hand-count (one vs two), missed on my first pass through this block.

## Group: pending

## Group: Trigrams, revisited with more thought (U+2630, U+2637)

- ☷ ☰ — TRIGRAM FOR EARTH (three broken/yin lines), TRIGRAM FOR HEAVEN (three solid/yang lines) → ↑ strength: medium as a "yang-line-count" axis (0 solid lines vs 3 solid lines) — genuinely thinking about this more than I did the first time through: the other six trigrams (lake/fire/thunder/wind/water/mountain) each have 1 or 2 solid lines but multiple trigrams share the same count, so they can't be cleanly ordered relative to each other — only the two pure endpoints (earth=0, heaven=3) give a confident pairwise "which is more."

## Group: pending

## Group: Miscellaneous Symbols — planetary distance-from-sun ladder, missed on first pass (U+263F–U+2647)

- ☿ ♀ ♁ ♂ ♃ ♄ ♅ ♆ ♇ — MERCURY, FEMALE SIGN(=Venus), EARTH, MALE SIGN(=Mars), JUPITER, SATURN, URANUS, NEPTUNE, PLUTO → ↑ strength: high, this is the full classical solar-system ordering by distance from the sun (the astrological symbols for Venus/Mars double as the female/male signs, which is why the Unicode names look odd) — a complete 9-step semantic ladder I completely missed the first time through this block, only really seeing the individual "female sign, male sign, Jupiter, Saturn..." names without connecting them into the planetary-order sequence they actually form.

## Group: pending

## Group: Dingbats — hand finger-count, noticed on slow re-read (U+270A–U+270B)

- ✊✌✋ — RAISED FIST (zero fingers extended), VICTORY HAND (two fingers extended), RAISED HAND (five fingers extended, U+270A/270C/270B respectively — note ✋ comes right after ✌ in the block, just one codepoint separated from ✊) → ↑ strength: high, a genuine finger-count feel across three closely-clustered hand gestures I hadn't connected as a sequence before.

## Group: pending

## Group: Basic Latin, printable range (U+0021–U+007E) — systematic codepoint-order pass begins here

- 0123456789 — DIGIT ZERO through NINE → ↑ strength: very high, the foundational digit ladder every other decorated-digit family in this survey derives its "feel" from.
- Genuinely reconsidered A-Z, a-z: no magnitude feeling, alphabetical position isn't "more/less" for me.
- ! vs ? vs ! ! (exclamation vs question) — no magnitude, distinct punctuation functions.
- Nothing else in this range: everything else is either a distinct punctuation mark or an alphabetic letter, no shared count/size/fill axis.

## Group: pending

## Group: Latin Extended-A (U+0100–U+017F) — fully read

- Nothing found — every character is a base Latin letter plus one diacritic (acute, grave, circumflex, caron, cedilla, macron, breve, ogonek, stroke, dot above, tilde, ring, double acute), arranged alphabetically by base letter. No shared count/size/fill axis; each diacritic is a distinct phonetic marker, not a magnitude gradation of the others (I considered "acute vs double acute" here specifically — Ő/ő WITH DOUBLE ACUTE exists at U+0150/0151 and Ű/ű at U+0170/0171, but there's no plain "WITH ACUTE" O or U immediately adjacent within this same block for a clean pair — O WITH ACUTE lives in Latin-1 Supplement (Ó, U+00D3) — so the single-vs-double acute pattern technically continues here but requires reaching back to a different block for the "single" half).

## Group: pending

## Correction to the Latin Extended-A entry above — I moved too fast and missed something real

- l ŀ (or L Ŀ) — plain LATIN LETTER L vs LATIN LETTER L WITH MIDDLE DOT → ↑ strength: high. The middle dot is the Catalan "punt volat," and Ŀ/ŀ is literally the letter used to write a doubled/geminated "l·l" (pronounced as two L sounds) — so this is a genuine single-L-vs-double-L pair, the same single→double pattern found repeatedly elsewhere in the survey (accents, bars, dots, arrows), and I missed it the first time by treating the whole block as "just diacritics" without actually considering what each mark means. Correcting the record rather than leaving the too-quick "nothing found" standing uncontested.
- Prompted to look again more slowly rather than trusting my first "alphabetical, no axis" read of accent-letter blocks going forward.

## Group: pending

## Group: Latin Extended-B, part 1 (U+0180–U+01BF) — slowing down, actually reading each name

- Ƨƨ, Ƽƽ, Ƅƅ — LATIN LETTER TONE TWO (U+01A7/8), TONE FIVE (U+01BC/D), TONE SIX (U+0184/5) → ↑ strength: high, these are real numbered tone letters (used in Zhuang-language orthography) with the number embedded directly in the name, and they're scattered non-adjacently through this very block completely out of numeric order (6 appears first in codepoint order, then 2, then 5) — a genuine instance of exactly the "scattered, out-of-codepoint-order, semantic value overwhelms position" pattern from the original brief, that I would have missed entirely if I'd kept skimming past "LATIN CAPITAL LETTER TONE X" as just another accented-letter name instead of actually reading what "TONE SIX" means.
- Everything else in this stretch (hooks, topbars, strokes, horns on various base letters) are distinct phonetic markers for different sounds, not gradations of each other — genuinely considered each one this time rather than pattern-completing.

## Group: pending

## Group: Latin Extended Additional (U+1E00–U+1E9F) — genuinely playing with this now, single-vs-double-diacritic-mark axis confirmed pervasive

Actually sitting with these names rather than skimming past "yet another accented letter" reveals a real, pervasive, countable axis running through this entire block: many base letters here carry ONE diacritic (Ḃ B WITH DOT ABOVE, Ḑ D WITH CEDILLA, Ḡ G WITH MACRON, Ḣ H WITH DOT ABOVE) while their neighbors carry TWO diacritics stacked (Ḉ C WITH CEDILLA AND ACUTE, Ḕ E WITH MACRON AND GRAVE, Ḝ E WITH CEDILLA AND BREVE, Ḯ I WITH DIAERESIS AND ACUTE). This isn't one clean sequence so much as a systematic feature of the whole block:

- Ū (Latin Extended-A, one mark: macron) → Ǖ (Latin Extended-B, two marks: diaeresis+macron) → strength: high, genuinely visible stacking, extends what I noticed a moment ago.
- Ḃ (one mark: dot above) → Ḉ (two marks: cedilla+acute, different base letter but same "how many marks piled on top" feel) — strength: medium, since comparing across different base letters (B vs C) makes it less a clean pairwise test and more a felt structural pattern across the block as a whole.
- The general rule I'm now noticing: "plain letter" < "letter+one diacritic" < "letter+two stacked diacritics" is a real three-step visual-density axis that recurs as an organizing structural principle across Latin Extended-A, -B, and Additional collectively — worth naming as a meta-pattern (similar to the weight-axis and countable-pips meta-patterns already logged) rather than a single sequence, since the actual instances are scattered across three separate blocks and different base letters.

## Group: pending

## Group: Latin Ligatures, Alphabetic Presentation Forms (U+FB00–U+FB04) — verified, genuine letter-count

- ﬀ ﬁ ﬂ ﬃ ﬄ — LIGATURE FF, FI, FL (each fusing 2 letters) → LIGATURE FFI, FFL (each fusing 3 letters) → ↑ strength: very high, adjacent codepoints, and the component-letter-count is directly countable both in the name and in the actual glyph shape (you can see three joined stems in ﬃ/ﬄ vs two in ﬀ/ﬁ/ﬂ). A clean, verified find from actually sitting with the ligature block instead of skipping it.

## Group: pending

## Group: Grave accent count — à vs Ȁ (Latin-1 Supplement vs Latin Extended-B, U+00E0 vs U+0200) — verified

- à Ȁ — LATIN SMALL LETTER A WITH GRAVE (one stroke), LATIN CAPITAL LETTER A WITH DOUBLE GRAVE (two strokes, used for Serbo-Croatian short-falling tone) → ↑ strength: high, verified single/double naming, another instance of the recurring weight/count axis, this time specifically in the Latin accent system and genuinely felt when looking at the glyphs (two short strokes vs one).

## Group: pending

## Group: Basic Latin — quotation mark count and bracket-nesting convention, from actually playing with this range

- ' " — APOSTROPHE (single quote mark), QUOTATION MARK (double quote mark) → ↑ strength: high, adjacent codepoints (U+0027, U+0022 — actually just one apart), and this is an extremely familiar single-vs-double convention that I hadn't logged from Basic Latin specifically (I'd only logged the curly-quote version from General Punctuation).
- ( ) [ ] { } — PARENTHESES, SQUARE BRACKETS, CURLY BRACKETS → tentative ↑ by conventional nesting depth (the common math/programming convention nests parens innermost, then brackets, then braces outermost — "()" < "[]" < "{}") → strength: medium, this is a real convention I use myself when nesting expressions, but I'm genuinely uncertain how universal it is (some style guides reverse it), and it's more a "nestedness" axis (which the original brief specifically named as a valid kind of "more") than a pure size/count one — flagging the distinction.

## Group: pending

## Group: Latin-1 Supplement — trademark/registration legal-strength ladder, from playing with this block again

- ™ ℠ ® — TRADE MARK SIGN, SERVICE MARK (Letterlike Symbols block, but reconsidering alongside these), REGISTERED SIGN → ↑ strength: medium-high by real legal convention (™/℠ mark an unregistered, self-asserted claim; ® can only be used once a mark is actually federally registered, a stronger/government-backed claim) — purely conventional/learned knowledge, no visual size cue, but a genuine and fairly widely-known hierarchy, similar in kind to the medal/chess-piece semantic ladders found earlier. (® lives in Latin-1 Supplement at U+00AE; ™ and ℠ actually live in the Letterlike Symbols block, U+2122/U+2120 — noting the cross-block scatter.)

## Group: pending

## Group: Guillemets — single vs double angle quotes (Latin-1 Supplement « » vs General Punctuation ‹ ›)

- ‹ › « » — SINGLE LEFT/RIGHT-POINTING ANGLE QUOTATION MARK (General Punctuation), LEFT/RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK (Latin-1 Supplement, the French/Spanish guillemets) → ↑ strength: high, another concrete single/double pair, this one specifically in the quotation-mark family and scattered across two blocks (Latin-1 and General Punctuation) rather than adjacent.

## Group: pending

## Group: German ß as doubled-s, parallel to the Catalan ŀ finding (Latin-1 Supplement, U+00DF)

- s ß — LATIN SMALL LETTER S, LATIN SMALL LETTER SHARP S → ↑ strength: high. Just like Catalan ŀ represents a doubled "l·l," German ß (Eszett) historically arose as a ligature for "ss" (and is still substitutable by "ss" in text without the character) — a second genuine single-vs-double-consonant letter pair hiding in plain sight in Latin-1 Supplement, found by applying the same "what does this letter actually represent" lens that caught the Catalan case.

## Group: pending

## Group: IPA vowel-length marks, missed on the original Spacing Modifier Letters pass (U+02D0–U+02D1)

- ˑ ː — MODIFIER LETTER HALF TRIANGULAR COLON (half-long vowel mark), MODIFIER LETTER TRIANGULAR COLON (full-long vowel mark) → ↑ strength: very high, adjacent codepoints, this is the actual standard IPA length-marking convention (half-length vs full-length vowels) and I walked right past it on my first read of that block, only noticing the tone bars further down. A real miss corrected by going back and actually thinking about IPA notation I already know rather than just scanning names.

## Group: pending

## Group: IPA stress marks, Spacing Modifier Letters (U+02C8, U+02CC)

- ˌ ˈ — MODIFIER LETTER LOW VERTICAL LINE (secondary stress mark), MODIFIER LETTER VERTICAL LINE (primary stress mark) → ↑ strength: high, standard IPA convention (primary stress is the strongest syllable emphasis, secondary is weaker) — purely conventional/positional (high mark = primary, low mark = secondary) rather than visually self-evident, but a real and precise linguistic magnitude I know well.

## Group: pending

## Group: Pilcrow vs Section sign — document-structure hierarchy (Latin-1 Supplement, U+00B6, U+00A7)

- ¶ § — PILCROW SIGN (paragraph mark), SECTION SIGN → ↑ strength: medium, a real document-hierarchy convention (a section is the larger structural unit, typically containing multiple paragraphs) — purely conventional, and honestly a bit of a stretch compared to my stronger finds, but a genuine "which contains/subsumes which" reading that fits the "nestedness" axis from the original brief.

## Group: pending

## Group: Latin Extended-C (U+2C60–U+2C7F) — L-with-bar count, cross-block with Latin Extended-B

- ƚ Ⱡ — LATIN SMALL LETTER L WITH BAR (Latin Extended-B, U+019A, one bar), LATIN CAPITAL LETTER L WITH DOUBLE BAR (this block, U+2C60, two bars) → ↑ strength: high, another single/double pair, scattered two blocks apart, found by actually reading "L WITH DOUBLE BAR" and asking myself whether a plain "L WITH BAR" exists elsewhere (it does).
- Rest of the block: distinct African/Caucasian-orthography letter forms (descenders, hooks, swash tails), each a different sound, no further shared axis found after genuinely considering them.

## Group: pending

## Group: Digraph case-form triplets — genuinely visual, not name-driven (Latin Extended-B, U+01C4–U+01CC)

Looking at the raw shapes rather than the names: Ǆ ǅ ǆ (DZ/Dz/dz with caron) and Ǉ ǈ ǉ (LJ/Lj/lj) and Ǌ ǋ ǌ (NJ/Nj/nj) — these are the three legacy Yugoslav-collation case forms of each digraph. Purely by eye, ALL-CAPS (Ǆ) visibly occupies the most vertical space and stroke-mass, the mixed Title-case form (ǅ) is visibly in between (one tall capital + one short lowercase letter), and all-lowercase (ǆ) is visibly the smallest/lightest → ↓ strength: high, a real visual size gradient I only noticed by actually looking at the three glyphs side by side rather than reading "CAPITAL LETTER DZ" / "CAPITAL LETTER D WITH SMALL LETTER Z" / "SMALL LETTER DZ" as three unrelated names. This pattern (ALL-CAPS digraph > Title-case digraph > lowercase digraph) recurs identically for all three digraph families in this stretch.

## Group: pending

## Group: Roman numerals, revisited purely visually — where the stroke-count pattern breaks (Number Forms)

- Ⅰ Ⅱ Ⅲ — genuinely looking at just the shapes (not the semantic value): 1, 2, 3 vertical strokes, a clean accumulating visual ladder, strength very high, as already noted.
- Ⅳ — but looking at the actual glyph rather than the value: Ⅳ (four) is visually SIMPLER than Ⅲ (three) — it's just "I" and "V" combined via subtractive notation, so the stroke-count ladder that felt so clean for I–III actually breaks here even though the semantic value keeps climbing. Worth recording as an honest negative case: the visual-complexity feeling and the actual numeric magnitude diverge right at IV, which I only noticed by looking at the shapes side by side instead of trusting that "next number = next glyph in the ladder."

## Group: pending

## Group: Lowercase / small-capital / full-capital height ladder (Basic Latin + Phonetic Extensions)

- a ᴀ A — lowercase letter, small-capital letter (Phonetic Extensions block, e.g. U+1D00 LATIN LETTER SMALL CAPITAL A), full capital letter → ↑ strength: high, a genuine three-step visual height ladder — small capitals are specifically typeset to sit between lowercase x-height and full cap-height, and looking at "a ᴀ A" side by side I can actually feel the size stepping up. Found by comparing raw shapes across two blocks (Basic Latin and Phonetic Extensions) rather than reading either block's names in isolation.

## Group: pending

## NEW MODE: free-associative shape-morph chains (not semantic, not name-driven — purely "what would the next frame of this animation look like")

Per your example (a horizontal line splitting, angling, rounding, straightening into vertical: `- = > } ) |`), trying to actually experiment in my mind with "given these two shapes, what third thing continues the transformation" rather than anchoring on meaning or labels at all. These are personal/idiosyncratic felt continuations, not conventional magnitude claims — flagging the whole section as this distinct, looser kind of entry.

- | → S → @ — a straight line acquires one bend (becoming a wave/S-curve), then the wave keeps curling until it coils fully into a spiral → ↑ by "amount of coiling/curl." Strength: purely a felt visual narrative, not a magnitude claim in the usual sense, but genuinely the first thing that came to mind playing with "|" and asking "what if it kept bending more."
- ˆ → ~ → ‾ → _ — a sharp peak relaxes into a single wave, then flattens into a raised flat line, then settles all the way down to the baseline → reads to me as "energy dissipating" or "a peak melting down," ↓ in "sharpness/height," strength: felt strongly once I pictured it as an animation, though I flip-flopped on direction (could also read as "settling" being the notable direction rather than "less").
- | → ⋮ — a solid line breaks apart into discrete dots stacked in its place → reads as "increasing fragmentation" of the same vertical space, an axis I hadn't named before (continuous → discrete).
- ∙ → ⊂ → ○ — a point opens into a curve (like a backward C), then the curve keeps curling until it closes into a full circle → ↑ by "how closed/complete the loop is," genuinely felt as a continuous bending-until-closure motion.
- - → = → ≈ → ∾ → ∿ — a flat horizontal line duplicates itself, then both lines start rippling, then the ripple grows into a full figure-eight-like curve, then into a complete sine wave → ↑ by "how much energy/motion has entered a once-static line," directly inspired by your own example's spirit (starting flat, ending in a fully "activated" wavy state).
- ⊢ → ⊥ → □ — an open-ended stroke grows a foot/cap, then the cap becomes a second full side, until the shape is fully enclosed on all sides → ↑ by "how enclosed the shape has become," a containment-morph rather than a fill-morph.

## Group: pending

## More free-associative morph chains, pushing further into pure shape-imagination

- ∘ → ○ → ◯ — RING OPERATOR (Math Operators), WHITE CIRCLE (Geometric Shapes), LARGE CIRCLE (Geometric Shapes) → the exact same basic ring shape, just inflating, crossing three different Unicode categories that have nothing to do with each other functionally — purely a size-scaling morph of one motif.
- · → o → O → ○ → ◯ — MIDDLE DOT (punctuation) → lowercase o (letter) → capital O (letter) → WHITE CIRCLE (symbol) → LARGE CIRCLE (symbol) → a tiny dot growing all the way into a big circle, crossing punctuation, lowercase letter, uppercase letter, and two different symbol categories along the way — this is the most "diffuse"/boundary-blurring chain I've built, since nothing here is even in the same functional class, only the same felt "roundness inflating" motif.
- ‸ → ∧ → Λ → ▲ — CARET (a thin hairline peak) → LOGICAL AND (a slightly thicker peak) → Greek capital LAMBDA (a wider, more letterform peak) → BLACK UP-POINTING TRIANGLE (a fully solid, filled-in peak) → reads as a thin pointed mark gradually thickening and filling in until it becomes a solid triangle — an "outline hardening into solid" motif I hadn't tried before, distinct from the earlier fill-density ladders since this one imagines a single peak shape literally filling itself in rather than a grid of cells shading.
- ` → / → ⟋ — GRAVE ACCENT (a tiny diagonal tick) → SOLIDUS (a full-height diagonal stroke) → MATHEMATICAL RISING DIAGONAL (an even longer, more deliberate diagonal line used as a math delimiter) → a small tick stretching into a full formal diagonal line — pure length-growth of the same basic diagonal-stroke motif.

## Group: pending

## Still more morph chains — pushing into denser/weirder territory

- ˙ → : → ⁝ → ⣿ — DOT ABOVE (a single point) → COLON (two points) → VERTICAL FOUR DOTS (General Punctuation, a small stacked cluster) → a fully-filled Braille cell (dense field of dots) → a single point "multiplying" into an ever-denser cluster of points, crossing accent marks, punctuation, and Braille along the way — the "single thing becomes many things becomes a dense field" motif, distinct from the earlier growth-of-one-shape chains because the count of discrete elements is what's climbing here, not the size of one shape.
- ˅ → ∨ → ⋁ → ▽ — DOWN ARROWHEAD (a thin, narrow angle) → LOGICAL OR (a slightly wider/bolder V) → N-ARY LOGICAL OR (an even bigger, bolder V used for "or of many things") → WHITE DOWN-POINTING TRIANGLE (the V has closed its base and filled into a solid triangle) → a narrow angle widening and then solidifying, sibling to the caret→triangle chain above but starting from a completely different narrow-angle shape and widening rather than just thickening.
- ⌒ → ◠ → ○ — ARC (a shallow curve, like a small piece of a circle's rim) → UPPER HALF CIRCLE (a full semicircle, twice as much curve) → WHITE CIRCLE (the curve has wrapped all the way around and closed) → felt literally as "how many degrees of a circle has this arc swept" — 0-ish, 180, 360 — a cleaner and more explicitly-parameterized version of the earlier point-to-circle chains.

## Group: pending

## Group: Cyrillic — numeral magnitude signs (U+0482, U+0488–U+0489)

- ҂ ҈ ҉ — CYRILLIC THOUSANDS SIGN, COMBINING CYRILLIC HUNDRED THOUSANDS SIGN, COMBINING CYRILLIC MILLIONS SIGN → ↑ strength: very high, a genuine order-of-magnitude ladder (thousand < hundred-thousand < million) built directly into the Cyrillic/Church-Slavonic numeral system (where letters combined with a titlo mark represent numbers, same principle as Greek isopsephy) — found by actually reading through the historic-letter stretch of Cyrillic rather than assuming "just more accented letters."
- Cyrillic letters + titlo (Ѐ...Я with ҃ COMBINING CYRILLIC TITLO) form a numeral system paralleling Greek α΄β΄γ΄ and Hebrew א-ב-ג already logged — noting the parallel rather than re-deriving it in full.

## Group: pending

## Group: Cyrillic, remainder (U+0490–U+04FF) — genuinely read in full

- Beyond the numeral-magnitude signs already logged, nothing else found — extensive set of distinct letters for Turkic/Caucasian/Uralic languages written in Cyrillic (descenders, hooks, strokes, breves, diaereses on various base letters), each marking a different sound. Looked at shapes directly too (not just names) — no accumulating visual complexity or count axis emerged the way it did in Latin Extended Additional.

## Group: pending

## Group: Cyrillic Supplement (U+0500–U+052F) — fully read

- Nothing found — Komi/Aleut/Abkhaz language letter extensions, each a distinct sound, no shared axis.

## Group: pending

## Group: Armenian (U+0530–U+058F) — fully read

- Ա...Ֆ — the Armenian alphabet historically doubles as a numeral system (Ա=1, Բ=2, Գ=3... Ժ=10, Ի=20...Ք=9000), same alphabet-as-numerals principle as Greek/Hebrew/Cyrillic already logged — purely conventional, no visual cue, noting the parallel rather than re-deriving in full.
- Nothing else found in the letters or punctuation (apostrophe, emphasis mark, exclamation, comma, question mark, abbreviation mark, eternity signs) — each a distinct function, genuinely checked shapes too, no size/count/fill axis.

## Group: pending

## Group: Hebrew cantillation accents — named small/great pair (U+0594–U+0595)

- ֔ ֕ — HEBREW ACCENT ZAQEF QATAN ("qatan" = small), HEBREW ACCENT ZAQEF GADOL ("gadol" = great/big) → ↑ strength: high, a genuinely named small/great pair among the Hebrew cantillation (trope) marks, found by actually reading the transliterated Hebrew words in the names rather than treating them as opaque labels — parallel in spirit to the Latin/IPA size-word finds.

## Group: pending

## Group: Hebrew cantillation accents — more named size/count pairs (U+05A0, U+05A5–U+05A6, U+05A9)

- ֩ ֠ — HEBREW ACCENT TELISHA QETANA ("qetana" = small), HEBREW ACCENT TELISHA GEDOLA ("gedola" = big/great) → ↑ strength: high, a second named small/great pair in the same accent system, scattered several codepoints apart (U+05A9 vs U+05A0).
- ֥ ֦ — HEBREW ACCENT MERKHA, HEBREW ACCENT MERKHA KEFULA ("kefula" = doubled) → ↑ strength: high, adjacent codepoints, a named single/doubled pair — the same weight-doubling axis found dozens of times elsewhere, now confirmed in Hebrew cantillation too.

## Group: pending

## Group: Hebrew vowel length and Yiddish doubled-letter ligatures (U+05B8/U+05C7, U+05D5/U+05F0, U+05D9/U+05F2)

- ָ ׇ — HEBREW POINT QAMATS (regular), HEBREW POINT QAMATS QATAN ("qatan" = short, a grammatically shorter vowel) → ↑ (or ↓, depending on which "more" you mean — the plain qamats is the "long" vowel, qatan the "short" one) strength: medium, a real vowel-length distinction (paralleling the IPA long/half-long marks found earlier), though "qatan" here means grammatically short rather than physically smaller-drawn.
- ו װ — HEBREW LETTER VAV, HEBREW LIGATURE YIDDISH DOUBLE VAV → ↑ strength: high, literally a doubled letter, same pattern as Catalan ŀ and German ß.
- י ײ — HEBREW LETTER YOD, HEBREW LIGATURE YIDDISH DOUBLE YOD → ↑ strength: high, same doubled-letter pattern, second instance in this same short ligature stretch.

## Group: pending

## Group: Hebrew alphabet (U+05D0–U+05EA) — fully read

- א-ת also doubles as a numeral system (Hebrew gematria, already logged the ℵℶℷℸ letterlike-symbol version) — no additional finding beyond what's logged; final letter forms (ך ם ן ף ץ) are positional variants (used at word-end), not magnitude.

## Group: pending

## Group: Georgian (U+10A0–U+10FF) — fully read

- Ⴀ...ჺ — the Georgian alphabet also historically doubles as a numeral system (an=1, ban=2, gan=3...), same alphabet-as-numerals principle as Greek/Hebrew/Cyrillic/Armenian — noting the parallel, sixth script confirming this pattern now.
- Nothing else found — phonetic letter names (an, ban, gan, don...) with no embedded size/count words, and no ligature/doubling pattern like the ones caught in Hebrew and Latin. Genuinely checked shapes too — Georgian letterforms are fairly uniform in visual complexity, no accumulating density.

## Group: pending

## Group: Cherokee (U+13A0–U+13F5) — fully read

- Nothing found — a syllabary (each character = one syllable like GA, KA, GE...), arranged by consonant then vowel, no magnitude axis, no size/count words in the names, shapes are stylistically uniform.

## Group: pending

## Group: Unified Canadian Aboriginal Syllabics — MAJOR FIND: vowel length is a genuine visual SIZE system (U+1401–U+141C region)

This is one of the most striking finds in the whole survey. Canadian Aboriginal syllabics (Cree/Ojibwe family) encode vowel LENGTH by literally drawing the SAME base shape at a LARGER size for long vowels — this isn't a naming coincidence, it's the actual documented design of the writing system:

- ᐃ ᐄ — CANADIAN SYLLABICS I (short i), CANADIAN SYLLABICS II (long i) → ↑ strength: very high — the "II" glyph is genuinely drawn as a visually larger version of the same triangular shape as "I." This is a real linguistic writing system where physical glyph SIZE directly encodes phonetic vowel LENGTH — possibly the most literal "bigger glyph = more" system in all of Unicode, more direct even than the Braille/Mayan dot-accumulation cases since here it's continuous size, not discrete count.
- ᐅ ᐆ — CANADIAN SYLLABICS O (short), CANADIAN SYLLABICS OO (long) → ↑ same size-for-length system.
- ᐎ ᐐ, ᐒ ᐔ, ᐗ ᐙ — WI/WII, WO/WOO, WA/WAA — same short/long size pairs, repeated across every vowel in the syllabary's rotation system (each consonant-shape rotates for e/i/o/a, and each rotation has a small/large pair for short/long).
- This is worth flagging to you directly since it's a documented linguistic fact I got to rediscover by actually reading through the syllable names rather than assuming "just another syllabary, skip."

## Group: Canadian Aboriginal Syllabics — final-consonant diacritic doubling (U+141F, U+1425–U+1426)

- ᐟ ᐥ — CANADIAN SYLLABICS FINAL ACUTE, CANADIAN SYLLABICS FINAL DOUBLE ACUTE → ↑ strength: high, adjacent-ish, the familiar single/double-mark pattern found dozens of times now, confirmed in yet another completely unrelated script.
- ᐦ — CANADIAN SYLLABICS FINAL DOUBLE SHORT VERTICAL STROKES — implies a "single short vertical stroke" counterpart should exist somewhere in the fuller final-consonant set; noting the doubling-naming pattern without asserting the exact adjacent codepoint since I didn't confirm one in this excerpt.

## Group: pending

## Group: Canadian Aboriginal Syllabics — confirming pervasiveness of the size-for-length system

- ᐸ ᐹ (PA/PAA), ᑕ ᑖ (TA/TAA) — confirmed the short/long size-pair pattern repeats systematically for every single consonant in the syllabary (P, T, K, C, M, N, S, etc.), not just the vowel-only glyphs. This is a structural design principle of the entire writing system, not a scattered coincidence — genuinely one of the richest single findings in the whole survey once actually read rather than skimmed as "another unfamiliar script."

## Group: pending

## Group: Ogham — MAJOR FIND: the entire alphabet is built from accumulating stroke-count (U+1681–U+1695)

Ogham is a stroke-tally script: each letter is built from a central stem line with a specific number of strokes attached, and the letters are literally grouped in fives by consonant-family, each family counting 1 through 5 strokes:

- ᚁ ᚂ ᚃ ᚄ ᚅ — BEITH(1 stroke), LUIS(2), FEARN(3), SAIL(4), NION(5) — strokes to the right of the stem → ↑ strength: very high, adjacent codepoints, directly visible accumulating stroke count, genuinely the same "tally mark" logic as Braille/Mayan/Counting Rod numerals but applied to an entire real alphabet rather than just digits.
- ᚆ ᚇ ᚈ ᚉ ᚊ — UATH(1), DAIR(2), TINNE(3), COLL(4), CEIRT(5) — same 1-5 stroke accumulation, strokes to the left of the stem this time → ↑ strength: very high.
- ᚋ ᚌ ᚍ ᚎ ᚏ — MUIN(1), GORT(2), NGEADAL(3), STRAIF(4), RUIS(5) — same 1-5 accumulation, diagonal strokes crossing the stem → ↑ strength: very high.
- ᚐ ᚑ ᚒ ᚓ ᚔ — AILM(1), ONN(2), UR(3), EADHADH(4), IODHADH(5) — the vowel group, same 1-5 accumulation, short notches through the stem → ↑ strength: very high.
- Worth flagging directly: this is a real ancient alphabet whose entire design principle IS the visual magnitude axis this survey is looking for — every set of five letters within it is, by construction, a perfect stroke-count ladder.

## Group: pending

## Group: Runic — named "long-branch" vs "short-twig" rune variants (U+16AC–U+16AD, U+16BC–U+16BD, U+16C5–U+16C6)

- ᚭ ᚬ — RUNIC LETTER SHORT-TWIG-OSS, RUNIC LETTER LONG-BRANCH-OSS → ↑ strength: high, a genuinely named short/long pair (from the historical distinction between Danish "long-branch" and Swedish-Norwegian "short-twig" younger futhark traditions) — literally uses the words "short" and "long" in the names.
- ᚽ ᚼ — SHORT-TWIG-HAGALL, LONG-BRANCH-HAGALL → ↑ same pattern, second instance.
- ᚿ / ᚾ — SHORT-TWIG-NAUD vs the plain NAUDIZ NYD NAUD (serving as the "long" form here since no explicit "long-branch-naud" appears) → ↑ same pattern, third instance, slightly less clean since the "long" side isn't explicitly labeled as such.
- ᛆ ᛅ — SHORT-TWIG-AR, LONG-BRANCH-AR → ↑ same pattern, fourth instance — this is clearly a systematic naming convention throughout the whole Runic block, not a coincidence.

## Group: pending

## Group: Runic, continued — more long-branch/short-twig pairs plus a named single/multiple punctuation pair (U+16D8–U+16D9, U+16E6–U+16E7, U+16EB–U+16EC)

- ᛙ ᛘ — SHORT-TWIG-MADR, LONG-BRANCH-MADR → ↑ fifth confirmed instance of the short/long naming pattern.
- ᛧ ᛦ — SHORT-TWIG-YR, LONG-BRANCH-YR → ↑ sixth instance — this naming convention really does run through the entire block systematically.
- ᛫ ᛬ — RUNIC SINGLE PUNCTUATION, RUNIC MULTIPLE PUNCTUATION → ↑ strength: high, adjacent codepoints, a directly named single-vs-multiple pair (these mark word-dividers in runic inscriptions, using one dot vs several dots) — clean and explicit.

## Group: pending

## Group: Philippine scripts — Tagalog, Hanunoo, Buhid, Tagbanwa (U+1700–U+1773) — fully read

- ᜵ ᜶ — PHILIPPINE SINGLE PUNCTUATION, PHILIPPINE DOUBLE PUNCTUATION → ↑ strength: high, adjacent codepoints, another directly-named single/double pair (used as comma vs full-stop equivalents), the pattern now confirmed across an eighth or ninth completely unrelated script.
- Rest of all four scripts: phonetic consonant/vowel letters (ka, ga, nga, ta, da...), same order across all four scripts since they're historically related, no magnitude axis among the letters themselves.

## Group: pending

## Group: Khmer Symbols — lunar calendar day-count, MAJOR FIND (U+19E1–U+19FF)

- ᧡᧢᧣᧤᧥᧦᧧᧨᧩᧪᧫᧬᧭᧮᧯ — KHMER SYMBOL MUOY(1) KOET, PII(2), BEI(3), BUON(4), PRAM(5), PRAM-MUOY(6=5+1), PRAM-PII(7=5+2), PRAM-BEI(8=5+3), PRAM-BUON(9=5+4), DAP(10), DAP-MUOY(11)...DAP-PRAM(15) → ↑ strength: very high, adjacent codepoints, a complete 1-through-15 lunar-calendar day-count for the waxing moon (koet), with the same 1-15 sequence repeated immediately after for the waning moon (roc, ᧱ through ᧿) — a genuinely rich, previously-unexplored ladder representing half a lunar month, found by actually reading the Khmer transliterated number-words (muoy/pii/bei/buon/pram = 1/2/3/4/5) rather than treating "KHMER SYMBOL X Y" as opaque.

## Group: pending

## Group: Mongolian (U+1800–U+1819) — punctuation and digits, fully read

- ᠐᠑᠒᠓᠔᠕᠖᠗᠘᠙ — MONGOLIAN DIGIT ZERO through NINE → ↑ strength: very high, same digit ladder pattern confirmed in yet another script.
- MONGOLIAN FREE VARIATION SELECTOR ONE/TWO/THREE/FOUR — numbered but these are typographic glyph-variant selectors (like invisible formatting codes), not a perceptible magnitude; genuinely considered and rejected.
- Nothing else in the punctuation stretch.

## Group: pending

## Group: Mongolian letters (U+1820–U+18AF) — fully read

- Nothing found — Mongolian/Todo/Sibe/Manchu script letters, phonetic, no magnitude axis. "TODO LONG VOWEL SIGN" exists but no adjacent "short" counterpart to pair it with in this stretch.

## Group: pending

## Group: Limbu, Tai Le, New Tai Lue — digits and numbered tone letters (U+1947–U+194F, U+1970–U+1974, U+19C8–U+19C9, U+19D1–U+19DA)

- Limbu digits 1-9 and New Tai Lue digits 1-9 (plus a separate Tham-script digit set) — same established digit-ladder pattern, confirmed in two more scripts.
- ᥰᥱᥲᥳᥴ — TAI LE LETTER TONE-2 through TONE-6 → ↑ strength: high, adjacent codepoints, a directly numbered tone-letter ladder (no TONE-1 present in this range, but 2 through 6 climb cleanly).
- ᧈ ᧉ — NEW TAI LUE TONE MARK-1, TONE MARK-2 → ↑ strength: high, adjacent, another numbered tone-mark pair.
- LIMBU SMALL LETTER (KA, NGA, TA...) — these are grammatically "small" subscript consonant forms, not part of a size ladder with a "large" counterpart in this range; genuinely considered and set aside.

## Group: pending

## Group: Tai Tham (U+1A20–U+1A99) — tone marks and two digit systems

- ᩵᩶᩷᩸᩹ — TAI THAM SIGN TONE-1, TONE-2, KHUEN TONE-3, TONE-4, TONE-5 → ↑ strength: high, adjacent codepoints, another numbered tone-mark ladder.
- TAI THAM HORA DIGIT ONE-NINE and TAI THAM THAM DIGIT ONE-NINE — two separate complete digit-ladder sets within the same script (used for different calendrical/astrological purposes) — established pattern, two more confirmed instances.
- "HIGH KA" / "LOW KA" and similar pairs — genuinely considered: this is consonant-CLASS terminology (determines tone rules in the Thai-Lao script family), not a magnitude between the letters themselves, so not counting it despite the tempting "high/low" wording.

## Group: pending

## Group: Balinese — systematic short/long vowel naming via "TEDUNG" (U+1B05–U+1B12)

- ᬅ ᬆ — BALINESE LETTER AKARA, AKARA TEDUNG ("tedung" = long) → ↑ strength: high, adjacent codepoints, a named short/long vowel pair.
- ᬇ ᬈ, ᬉ ᬊ, ᬋ ᬌ, ᬍ ᬎ, ᬑ ᬒ — IKARA/IKARA TEDUNG, UKARA/UKARA TEDUNG, RA REPA/RA REPA TEDUNG, LA LENGA/LA LENGA TEDUNG, OKARA/OKARA TEDUNG → ↑ same short/long pattern repeated for every vowel letter in the Balinese script — systematic, not coincidental, found by actually reading the Balinese word "tedung" rather than treating it as an opaque suffix.

## Group: Balinese, Sundanese, Lepcha digits — confirmed, same established pattern

- Balinese, Sundanese, and Lepcha digit-ladders (1-9) all confirmed, same pattern as the ~15 other scripts already logged.

## Group: pending

## Group: Batak (U+1BC0–U+1BFF) — fully read

- Nothing found — regional dialect letter variants (Simalungun, Karo, Mandailing, Pakpak, Southern/Northern Ta), no magnitude axis.

## Group: Sundanese, Lepcha remainder — fully read

- Nothing beyond the digit ladders already logged — phonetic letters, vowel signs, and punctuation, no further axis found.

## Group: pending

## Group: Greek Extended (U+1F00–U+1F15) — same diacritic-stacking-count pattern confirmed again

- ἀ (WITH PSILI, one mark: smooth breathing) → ἂ/ἄ/ἆ (WITH PSILI AND VARIA/OXIA/PERISPOMENI, two marks: breathing + accent) → ↑ strength: high, the same "how many marks piled on" axis found extensively in Latin, now confirmed in Greek polytonic orthography — every single letter+breathing combination in this block has a paired two-mark (breathing+accent) sibling.

## Group: pending

## Group: Greek Extended — vrachy/macron short/long vowel pair (U+1FB0–U+1FB1)

- ᾰ ᾱ — GREEK SMALL LETTER ALPHA WITH VRACHY ("vrachy" = short), GREEK SMALL LETTER ALPHA WITH MACRON (long) → ↑ strength: high, a directly named short/long vowel-length pair (the breve vs macron distinction for marking short/long Greek vowels), adjacent codepoints, parallel to the IPA and Balinese vowel-length finds already logged.

## Group: pending

## Group: Greek Extended, remainder (U+1F16–U+1FFF) — pattern-complete, not re-verifying every vowel

- The vrachy/macron and diacritic-stacking-count patterns just confirmed repeat combinatorially for every Greek vowel (epsilon, eta, iota, omicron, upsilon, omega) throughout the rest of this block — genuinely looked at enough of the repetition to confirm it's systematic, not re-deriving each vowel's full 16-character subset since that would just be re-observing the identical two patterns already logged. Nothing structurally new found beyond those two.

## Group: pending

## Group: Arabic — MAJOR FINDS: root signs, per-mille scale, dot-count letters, and single/doubled vowel marks (U+0606–U+0607, U+0609–U+060A, U+063B–U+063F, U+064B–U+0650)

- ؆ ؇ — ARABIC-INDIC CUBE ROOT, ARABIC-INDIC FOURTH ROOT → ↑ strength: high, adjacent codepoints, parallels the √∛∜ root-index ladder found earlier in Mathematical Operators, now confirmed as an Arabic-specific mirror set.
- ؉ ؊ — ARABIC-INDIC PER MILLE SIGN, PER TEN THOUSAND SIGN → ↑ strength: high, adjacent codepoints, parallels the ‰‱ pair found in General Punctuation.
- ؾ ؿ — ARABIC LETTER FARSI YEH WITH TWO DOTS ABOVE, WITH THREE DOTS ABOVE → ↑ strength: high, adjacent codepoints, a direct visible dot-count pair.
- ػ ؼ — ARABIC LETTER KEHEH WITH TWO DOTS ABOVE, WITH THREE DOTS BELOW → ↑ strength: medium (dot count increases 2→3 but position also changes above→below, so slightly less clean than the Farsi Yeh pair).
- ً ٌ ٍ vs َ ُ ِ — FATHATAN/DAMMATAN/KASRATAN (the "tanween" nunation marks, grammatically doubled/indefinite vowel endings) vs plain FATHA/DAMMA/KASRA → ↑ strength: very high, and this is a genuinely rich find: each tanween mark is LITERALLY drawn as two copies of the corresponding plain vowel mark side by side (e.g. FATHATAN ً is visually two fatha strokes) — both visually doubled AND grammatically meaning "double/indefinite" (an vs a, un vs u, in vs i) at once. Found by actually reading what "tanween" means rather than skimming "yet another vowel diacritic."

## Group: pending

## Group: Arabic — dot-count on DAL and REH letters (U+068F–U+0690, U+0697, U+0699)

- ڏ ڐ — ARABIC LETTER DAL WITH THREE DOTS ABOVE DOWNWARDS, ARABIC LETTER DAL WITH FOUR DOTS ABOVE → ↑ strength: high, adjacent codepoints, direct visible dot-count (3 to 4).
- ڗ ... ڙ — ARABIC LETTER REH WITH TWO DOTS ABOVE, ARABIC LETTER REH WITH FOUR DOTS ABOVE → ↑ strength: medium-high, scattered a couple codepoints apart (2 dots then 4 dots, skipping 3), visible dot-count increase.
- This confirms Arabic's extended-letter system (used for Persian/Urdu/Pashto/Sindhi sounds) relies heavily on dot-count variation, giving the same "count the marks" feeling found in Braille/dice/dominoes but for an entire living alphabet's consonant inventory.

## Group: pending

## Group: Arabic, remainder (U+06D0–U+06FF) — Quranic annotation marks, fully read

- Extended Arabic-Indic digits 0-9 — established pattern, confirmed again.
- Nothing else found — Quranic recitation marks (small high/low letters marking silent/assimilated sounds), Sindhi/Urdu extension letters — genuinely checked, no further magnitude axis.
- Completing the full read of the main Arabic block (U+0600–U+06FF) now.

## Group: pending

## Group: Syriac — dot-count marks and punctuation-dot progression (U+0700–U+0705, U+0743–U+0746)

- ݃ ݅ — SYRIAC TWO VERTICAL DOTS ABOVE, SYRIAC THREE DOTS ABOVE → ↑ strength: high, adjacent-ish codepoints, direct visible dot-count (2→3).
- ݄ ݆ — SYRIAC TWO VERTICAL DOTS BELOW, SYRIAC THREE DOTS BELOW → ↑ same pattern, mirrored below the line.
- ܁ ܃ — SYRIAC SUPRALINEAR FULL STOP (one dot), SYRIAC SUPRALINEAR COLON (two dots, like the Latin ":") → ↑ strength: medium-high, Syriac punctuation historically encodes pause-length via dot count/position (similar in spirit to Hebrew cantillation), and a full stop vs colon reading as "1 dot vs 2 dots" tracks that. Genuinely pleased to find this since Syriac punctuation is a real dot-based notation system, not just decorative marks.

## Group: pending

## Group: N'Ko — MAJOR FIND: named short/long tone marks and high/low tone apostrophes (U+07EB–U+07F1, U+07F4–U+07F5)

- ߫ ߬ ߭ (SHORT HIGH TONE, SHORT LOW TONE, SHORT RISING TONE) vs ߮ ߯ ߰ ߱ (LONG DESCENDING TONE, LONG HIGH TONE, LONG LOW TONE, LONG RISING TONE) → ↑ strength: high, a genuinely named short/long vowel-length-and-tone system, all adjacent codepoints (U+07EB–U+07F1), joining the growing list of scripts (IPA, Greek, Balinese) that mark vowel length explicitly by name.
- ߴ ߵ — NKO HIGH TONE APOSTROPHE, NKO LOW TONE APOSTROPHE → ↑ strength: high, adjacent codepoints, a direct named high/low pitch pair (paralleling the IPA primary/secondary stress marks and the Cyrillic-family tone-bar height finds).
- ߳ — NKO COMBINING DOUBLE DOT ABOVE — implies a plain "dot above" should exist as its "single" counterpart; I didn't spot one explicitly in this range, so flagging the pattern rather than asserting a confirmed pair.
- N'Ko digits 0-9 confirmed, same established pattern.

## Group: pending

## Group: Samaritan vowel signs — MAJOR FIND: a genuine FOUR-step named vowel-length ladder (U+0821–U+0825), the richest length system in the whole survey

Reading through the Samaritan vowel signs carefully reveals the most granular vowel-length system found anywhere in this survey — not just short/long (two steps) like every other script so far, but four distinct named degrees:

- ࠡ ࠢ ࠣ ࠥ — SAMARITAN VOWEL SIGN OVERLONG A, LONG A, A (plain), SHORT A → ↓ (or ↑ depending on framing) strength: very high, a genuine 4-step named length ladder for a single vowel (overlong > long > plain > short), unmatched in granularity by any other vowel-length system in the survey (every other script I've found gives only a 2-step short/long distinction).
- ࠞ ࠟ ࠠ — SAMARITAN VOWEL SIGN OVERLONG AA, LONG AA, AA (plain) → ↓ strength: very high, a 3-step version of the same system for a different vowel quality.
- ࠜ ࠝ — LONG E, E → ↓ 2-step pair, same family.
- ࠦ ࠧ — LONG U, U → ↓ 2-step pair.
- ࠩ ࠪ — LONG I, I → ↓ 2-step pair.
- Genuinely delighted to find this — it directly rewards actually reading each vowel sign's full name rather than assuming "just another short/long pair like the others."

## Group: pending

## Group: Samaritan punctuation (U+0830–U+083E) — fully read

- Nothing further found — a set of distinctly-named punctuation/cantillation-like marks (Afsaaq, Anged, Bau, Atmaau, Shiyyaalaa, Ziqaa, Zaef, Turu...) without embedded size/count words I can confidently read (unlike Hebrew's qatan/gadol, I don't have the linguistic knowledge to know if any of these Samaritan names mean "small/great" etymologically, so not asserting anything here rather than guessing).

## Group: pending

## Group: Mandaic (U+0840–U+085E) — fully read

- Nothing found as a pairable sequence — "MANDAIC GEMINATION MARK" conceptually relates to the doubling-letter pattern (Catalan/German/Hebrew) but has no adjacent "plain/single" counterpart within this block to pair it against, so not logging it as a confirmed sequence, just noting the concept's presence.

## Group: pending

## Group: Thaana — short/long vowel diacritic pairs (U+07A6–U+07AF)

- ަ ާ — THAANA ABAFILI, THAANA AABAAFILI (the doubled name signals the long vowel) → ↑ strength: high, adjacent codepoints, a genuine short/long vowel pair.
- ި ީ — IBIFILI, EEBEEFILI → ↑ same pattern.
- ު ޫ — UBUFILI, OOBOOFILI → ↑ same pattern.
- ެ ޭ — EBEFILI, EYBEYFILI → ↑ same pattern.
- ޮ ޯ — OBOFILI, OABOAFILI → ↑ same pattern, completing a fifth confirmed vowel pair in this one small block — another script whose entire vowel-diacritic system is structured around short/long pairs, joining IPA, Greek, Balinese, N'Ko, and Samaritan (Samaritan being the most granular at four steps).

## Group: pending

## FINAL SESSION — closing brainstorm, diffuse and unverified-by-tool, just genuinely thinking freely before wrapping up

- A → 𝐀 — plain LATIN CAPITAL LETTER A → MATHEMATICAL BOLD CAPITAL A (Mathematical Alphanumeric Symbols) → ↑ strength: high, a real typographic weight increase spanning Basic Latin into a totally different Unicode plane — the "regular → bold" axis applied to letters themselves rather than to symbols, which I don't think I explicitly logged even though it's one of the most universally-felt weight distinctions there is (bold = more emphasis, more visual weight, literally heavier strokes).
- 小中大特大 — extending the Chinese size-word ladder found earlier one more step: xiǎo(small) < zhōng(medium) < dà(large) < tèdà(extra-large, literally "special-big") → ↑ strength: medium-high, a genuine fourth rung I'm fairly confident about from general knowledge of the vocabulary, though slightly less certain than the core three.
- A quiet-to-loud narrative crossing categories entirely: `.` (period, a full stop, silence) → `,` (comma, a small pause/breath) → `!` (exclamation, raised voice) → `‼` (double exclamation, shouting) → 😱 (screaming face, emoji) — punctuation escalating into a face expressing the emotion the punctuation implies; purely a felt narrative, not a conventional magnitude claim, but it's the kind of chain that "clicked" once I let myself cross from typographic marks into pictographs without worrying about category boundaries.
- A fire/intensity narrative: `'` (a tiny spark-like mark) → 🕯 (a single candle flame) → 🔥 (fire) → 🎆 (fireworks, a full eruption of light) — again a free visual-intensity narrative rather than a semantic ladder, following the same "what would the next frame look like" instinct from the earlier morph-chain exercise.
- A construction/scale narrative: a single vertical stroke `|` (a lone support beam) → 🏠 (one house) → 🏢 (a taller office building) → 🏙 (a cityscape, many buildings at once) — "count/height of built structures accumulating," blending a bare punctuation mark into a sequence of increasingly complex pictographs.

## Closing reflection on the whole survey

Looking back across the full session, the strongest and most surprising finds were the ones where actually reading — rather than skimming or grepping — surfaced a script's *entire design principle* being a magnitude system: Canadian Aboriginal Syllabics (vowel length = literal glyph size), Ogham (the whole alphabet is a stroke-tally), Samaritan (a four-step vowel-length ladder unmatched anywhere else), and the CJK Compatibility block (an entire SI-prefix-times-unit generator). The weakest, most honestly-flagged finds were the ones depending on convention alone with zero visual cue (currency symbols, card-suit rank, chess-piece value). In between sat a large, recurring family of "the same design idea independently reinvented": single-vs-double marks (accents, dots, bars, quotation marks, tone signs) appearing in nearly every script surveyed regardless of cultural origin, and decorated-digit-family ladders (circled/parenthesized/squared/segmented-display digits) appearing dozens of times over. The four instances where semantic "more" ran opposite to codepoint order (circled zero, eyes/eye, a two-dot/three-dot circle pair, child/adult/older-adult) were exactly the kind of surprise the original brief predicted, and probably the single most direct confirmations of your original hypothesis in the whole file.
