# Magnitude-perception survey — first-instinct pass

Append-only. Working notes for myself interleaved with sequences; unicode-group
tool used to pull one pane at a time, no other corpus/prior-survey material
read before this pass.

Format per entry: sequence → direction arrow, strength (how confident a
pairwise "which is more" would recover this order), what "more" means,
immediacy note (percept-level vs symbol-lookup), free notes.

---

## Pane: Enclosed Alphanumerics U+2460–24FF

⓪①②③④⑤⑥⑦⑧⑨⑩
→ strength: very high. "more" = denoted count/number. NOT immediate — this
is digit-lookup, pure symbol decoding, exactly like reading "0,1,2...". No
fill-ramp, no size change. I had to consciously read each glyph's numeral.
Interesting: had to manually put ⓪ (U+24EA, circled digit zero) at the
FRONT even though its codepoint is near the far end of the block (after ⑳
and all the parenthesized/lettered ranges) — semantic magnitude fully
overrides codepoint order here, no hesitation at all.

⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽
→ same shape as above (parenthesized digits), same strength, same
non-immediacy — just a different container glyph around the same digit
lookup. Notably *weaker feeling of magnitude* than the circled or negative-
circled versions to me — the parens read more like "footnote marker" than
"quantity," even though the ordering is still perfectly recoverable.

Ⓐ Ⓑ Ⓒ ... Ⓩ / ⓐ ⓑ ⓒ ... ⓩ / ⒜ ⒝ ⒞ ... ⒵
→ alphabetic, not magnitude — no sense of "more," just sequence identity
(list-item ordering, not quantity ordering). Excluding from magnitude set;
noting because it's adjacent and Joseph might want the alphabetic-ordering
class distinguished from magnitude-ordering.

①②③...⑨⑩⑪⑫...⑳ (circled 1-20, no zero variant needed)
→ strength: very high, same digit-lookup character as above. The circle
container itself doesn't visually grow or fill with more dots/mass as the
number increases — it's a fixed-size circle around an increasingly complex
glyph. So despite "high confidence in the ordering," it is NOT immediate;
it is 100% symbolic/numeral decoding, not perceptual magnitude. Flagging
this because it's the paradigm case of "confident order, zero immediacy."

⓫⓬⓭...⓴ (NEGATIVE CIRCLED NUMBER 11-20 — white digits on black disc)
→ same digit-lookup mechanism, but the black-fill disc gives an *extra*,
separate, immediate signal: solid black circle vs the plain circled series'
white/outline circle. That contrast (filled disc vs outline) is itself
binary and immediate, but doesn't establish a *graded* magnitude by itself
since all of 11-20 in this sub-range share the identical filled look.

⓵⓶⓷⓸⓹ (DOUBLE CIRCLED DIGIT ONE-FIVE)
→ digit lookup again, double-ring container is a fixed decoration, no
graded feel. Same category as above.

---

## Pane: Geometric Shapes U+25A0–25FF

### ○ ◔ ◑ ◕ ● (circle fill ramp — pie/moon-phase gauge)
U+25CB WHITE CIRCLE, U+25D4 CIRCLE WITH UPPER RIGHT QUADRANT BLACK,
U+25D1 CIRCLE WITH RIGHT HALF BLACK, U+25D5 CIRCLE WITH ALL BUT UPPER LEFT
QUADRANT BLACK, U+25CF BLACK CIRCLE
→ strongest, most immediate find so far. Feels exactly like a battery/
signal-strength/pie-chart meter: empty, quarter, half, three-quarter, full.
STRENGTH: very high — I'd bet heavily a pairwise "which has more fill"
would recover this order. IMMEDIACY: this is the paradigm *immediate*
case — the magnitude is perceived directly as filled-area, no symbol
decoding at all, unlike the circled-digit case above. Codepoints are
scattered out of visual order (CB, D4, D1, D5, CF) — pure semantic/visual
assembly, codepoint adjacency gives no help here at all.
(Related half-only alt: ◐ left-half black / ◑ right-half black — same
fill amount, no magnitude difference between them, just orientation —
excluding as a magnitude pair.)

### ▪ ◽ ◻ ■ (black/white square, small → medium-small → medium → large)
U+25AA BLACK SMALL SQUARE, U+25FD WHITE MEDIUM SMALL SQUARE,
U+25FB WHITE MEDIUM SQUARE, U+25A0 BLACK SQUARE
→ strength: moderate-high for the *size* dimension alone, but muddied
because color (black/white) is inconsistently mixed into the sample I
picked — reordering for a pure test I'd want to hold fill constant, e.g.
▫(small,white) → ◽(med-small,white) → ◻(med,white) → □(white, but this is
"large/default" — visually the biggest). white-only ramp: ▫ ◽ ◻ □ — this
one I trust more. IMMEDIATE: yes, pure size perception, no lookup.

### ▵ ▴ (small triangle) vs △ ▲ (large triangle)
U+25B5/U+25B4 small, U+25B3/U+25B2 large — size ramp, immediate, strength
high for small<large; fill (white/black) is a separate, non-magnitude
axis here (I don't perceive black-vs-white triangle as "more," just as a
different category/state, unlike the circle fill ramp above where partial
fill genuinely read as partial magnitude).

### □ ▤ ▨ ▩ ■ (square: empty → sparse fill → hatch → crosshatch → solid)
U+25A1 WHITE SQUARE, U+25A4 SQUARE WITH HORIZONTAL FILL, U+25A8 SQUARE
WITH UPPER RIGHT TO LOWER LEFT FILL, U+25A9 SQUARE WITH DIAGONAL
CROSSHATCH FILL, U+25A0 BLACK SQUARE
→ strength: moderate. The endpoints (empty/solid) are unambiguous and
immediate; the middle members (single hatch vs crosshatch) required a
half-second of "which reads as more filled" deliberation — the fill-
density perception is there but weaker/slower than the circle version,
possibly because hatching patterns don't map as cleanly to "percentage
covered" as pie-slice quadrants do. Worth noting as a *medium*-strength,
still fairly immediate case, one tier below the circle ramp.

◯ vs ● (LARGE CIRCLE outline vs BLACK CIRCLE)
→ noting only as a caution: LARGE CIRCLE (U+25EF) reads as "big empty
circle," not smaller than ○ WHITE CIRCLE — size-of-glyph and fill are
separate axes here, don't conflate.

---

## Pane: Block Elements U+2580–259F

### ▁▂▃▄▅▆▇█ (lower N-eighths block, 1/8 → full)
U+2581..U+2588, contiguous codepoints, ALSO contiguous fill order — the one
case so far where codepoint order and perceptual order coincide exactly.
STRENGTH: maximum — this is a literal bar-chart glyph set (sparkline
characters), I'd stake everything on the ordering. IMMEDIACY: the single
most immediate sequence encountered — pure rising-bar height, reads
instantly and pre-attentively, faster even than the circle-fill ramp
(no shape-decoding at all, just "how tall is the black region"). If
Joseph wants ONE canonical example of "magnitude arrives in the percept
itself," this is it.

### ░▒▓█ (light shade → medium shade → dark shade → full block)
U+2591 U+2592 U+2593 U+2588 — contiguous codepoints too.
→ strength: very high, immediacy: very high (density-of-dither reads
instantly), though maybe a half-notch below the bar-height ramp above
because "how dense is this stipple" takes marginally more visual
integration than "how tall is this bar" — still squarely in the
immediate/perceptual category, not symbolic.

### ▏▎▍▌▋▊▉█ (left N-eighths block, 1/8 → full, leftward fill)
U+258F,258E,258D,258C,258B,258A,2589,2588 — codepoints here run in
DESCENDING order for ascending fill (▏ is 258F=1/8 but ▊ is 258A=3/4,
etc.) — actually check: 258F(1/8) 258E(1/4) 258D(3/8) 258C(1/2) 258B(5/8)
258A(3/4) 2589(7/8) 2588(full) — codepoints ascend WITH fill here too
(258F<258E is false — 258F=0x8F=143, 258E=142, so codepoint DEscends as
fill ascends). So this is a case of monotonic *perceptual* magnitude
riding on non-monotonic (reversed) codepoint order within that subrange —
worth flagging per Joseph's interest in scattered/reversed-codepoint
cases. Immediacy: same as the lower-block ramp — instant, pre-attentive,
horizontal fill instead of vertical.

▀ (upper half) / ▐ (right half) — noted only as orientation variants of
"half," not magnitude-distinct from ▄/▌; excluding from ramps.

---

## Dice: ⚀⚁⚂⚃⚄⚅ (Misc Symbols, U+2680–2685)

→ strength: very high, contiguous codepoints matching pip count exactly.
IMMEDIACY: high but graded within itself — ⚀⚁⚂ (1-3 pips) are subitized
instantly, true percept-level magnitude; ⚃⚄⚅ (4-6 pips) I notice a tiny
extra beat of "count the dots" even though the canonical dice arrangement
helps a lot (5 and 6 in particular I'm recognizing the *pattern* rather
than literally not-counting). So: mostly immediate, degrading slightly at
the high end — worth it as a "graceful degradation of immediacy" example
alongside the braille one below, rather than a clean binary
immediate/symbolic split.

## Braille Patterns U+2800–28FF: dot-count subsequence

⠀ (0 dots) ⠁ (1) ⠃ (dots-12, 2) ⠇ (dots-123, 3) ⠏ (dots-1234, 4)
⠟ (dots-12345, 5) ⠿ (dots-123456, 6) ⣿ (all 8 dots, full cell)
→ hand-picked non-contiguous subsequence out of the 256-glyph bitfield
block (codepoints are a bitmask, not remotely magnitude-ordered in
general — most of this block has NO monotonic feel, I'm cherry-picking
the cumulative-fill diagonal). STRENGTH: high for the *chosen* members.
IMMEDIACY: this is the clearest "graceful degradation" case I've found —
0/1/2 dots are subitized instantly (pure percept), 3-4 dots take a beat,
5-6-8 dots I'm essentially estimating "how much of the cell is dark," much
more like the block-shade ramp than like counting. So braille slides from
immediate(low end) to density-estimation(high end) within one sequence.

---

## Math Operators U+2200–22FF: chevron-doubling "much" ramp

< (ordinary less-than, ASCII, not in this block) → ≪ U+226A MUCH LESS-THAN
→ ⋘ U+22D8 VERY MUCH LESS-THAN
→ strength: high, and genuinely IMMEDIATE — the glyph doubles/triples its
chevron the same way ▁▂▃ doubles bar height: one wedge vs two nested
wedges vs three nested wedges reads as "how much" without decoding the
mathematical meaning at all, just visual repetition-as-intensity (same
mechanism as "!!!" for emphasis). Notable per Joseph's interest in
scattered codepoints: U+226A and U+22D8 are ~150 codepoints apart, no
adjacency at all, and < itself is ASCII, so this ramp spans three
completely different blocks and still holds together perceptually. Mirror
ramp on the greater-than side: > ≫ ⋙.

---

## Geometric Shapes Extended U+1F780–1F7FF: explicitly-named weight ramp

🞄 🞅 🞆 🞇 🞈 🞉 (BLACK SLIGHTLY SMALL CIRCLE → MEDIUM BOLD WHITE CIRCLE →
BOLD WHITE CIRCLE → HEAVY WHITE CIRCLE → VERY HEAVY WHITE CIRCLE →
EXTREMELY HEAVY WHITE CIRCLE)
→ this is the one place in the whole survey where Unicode's own NAMES
spell out a magnitude adjective ladder (slightly small → medium → bold →
heavy → very heavy → extremely heavy) — strong external confirmation that
my perceptual ordering isn't just me projecting. Visually it reads as
"stroke weight/boldness increasing," immediate at a glance though the
top 2-3 members (very heavy vs extremely heavy) are close enough in my
rendering that I underweight my own confidence slightly for that specific
adjacent pair even though the ordering overall is obvious.
Same pattern repeats for squares (🞌🞍🞎🞏🞐🞑🞒🞓, tiny→extremely heavy) and
diamonds/lozenges right after it in the same block — I'm treating these
as one family rather than transcribing all three; the circle version is
representative and I'd rate it strongest since round targets read fill/
weight most cleanly.

---

## Closing self-notes (first-pass, not overthought)

- The clearest immediacy/non-immediacy split I found: block-element fill
  ramps (▁▂▃▄▅▆▇█, ░▒▓█) are maximally immediate — true percept, no
  lookup. Circled/parenthesized digit sequences are maximally NON-
  immediate despite equally strong *ordering* confidence — pure symbol
  decoding. Joseph's "immediacy" axis and "strength" axis are clearly
  orthogonal in my experience: strength answers "would pairwise compare
  recover the order," immediacy answers "does it recover it before I've
  consciously read anything."
- Semantic override of codepoint order happened twice cleanly: ⓪ (circled
  zero) slotting to the front of ①②③... despite its codepoint being at the
  far end of the block; and the reversed local ordering inside
  ▏▎▍▌▋▊▉█ (fill ascends as codepoint descends within that subrange).
- The chevron-doubling find (< ≪ ⋘) is the strongest "scattered codepoint,
  strong semantic ramp" case I found — spanning ASCII and two separate
  supplemental-math blocks via pure glyph-repetition-as-intensity, the
  same visual grammar as "!!!" or exclamation stacking.
- I did not encounter the dice/trigram/hexagram sequences yet at the point
  of writing this summary — flagging that as an honest gap in coverage
  rather than implying I checked and found nothing; I ran out of budgeted
  passes on this cycle before I got to Yijing hexagrams or Tai Xuan Jing
  or a full arrows/misc-technical/geometric-shapes-extended pass.
- I deliberately did NOT read any prior survey work or other unicode
  material in msc/ per the brief; everything above is genuinely first-
  instinct.
