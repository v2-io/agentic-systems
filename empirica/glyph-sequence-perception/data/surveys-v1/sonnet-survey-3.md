# Magnitude-monotonicity survey — Sonnet, fresh pass (session 3)

First-instinct pass. Appending as I go through one unicode-group at a time. Not
reading prior surveys until after this file is done. Strength = how confident
a stochastic pairwise "which is more" would recover this order. Immediacy =
does the magnitude land as raw percept (fill/size/density) or does it require
a symbol lookup (recognizing a digit/glyph shape) first — Joseph's added axis.

---

## U+2460–U+24FF Enclosed Alphanumerics

- `①②③④⑤⑥⑦⑧⑨⑩` — ↑ increasing. Strength: very high, but **immediacy: LOW**
  — this is digit-recognition, not percept-magnitude. The circle is constant;
  only the enclosed glyph changes. Feels exactly like reading "1 2 3" with a
  circle sticker on it. Good example of the immediacy/strength split Joseph
  flagged: strong pairwise recoverability, but the "more" arrives via symbol
  lookup, not the shape itself.
- `⓪①②③④⑤⑥⑦⑧⑨⑩` — including the zero at the front feels right, zero read
  as "less than one" purely semantically (circled-zero is codepoint-later,
  U+24EA, but the semantic override is total — no hesitation at all).
- `⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽` — same digit-lookup pattern, parenthesized. Same
  strength/immediacy profile as circled digits.
- `①⑴⒈` — three different enclosure styles of "1" together do NOT have a
  magnitude relationship for me — no ordering feel, just different fonts of
  the same value. Worth noting as a non-example: same-value-different-frame is
  not a magnitude axis.
- `Ⓐ①ⓐ` type mixed circled-letter vs circled-digit: no felt ordering (letters
  aren't magnitudes to me pre-attached, they're identity/rank in a different,
  weaker sense — see alphabet note below under Geometric Shapes).
- `⓪①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳` — full monotonic run 0-20, strength very high,
  immediacy low (digit lookup) throughout.

## U+25A0–U+25FF Geometric Shapes

- `◌○◔◑◕●` — ↑ increasing. Strength: **very high**. Immediacy: **HIGH** —
  a pie-chart-style fill ramp (dotted/empty → outline → quarter → half →
  three-quarter → solid). One of the strongest finds so far, on par with the
  block-elements ramp. Reads instantly as "how full is the pie," no lookup.
  (Skipping ◐/◒/◓ — those are same-fraction-different-orientation, i.e. all
  "half," so they don't add a magnitude step; they're a case like the
  circled-letter one, same value/different frame, no ordering feel between
  them.)
- `▫▪` and `◽◾` and `□■` — white-vs-black same-shape pairs: I do NOT feel a
  magnitude ordering from color/fill alone here (unlike the pie-circle
  above) — black square doesn't read as "more" than white square, just
  "different mode." Interesting contrast with the block-elements shading
  ramp (░▒▓█ DID feel like increasing darkness=more). My best guess: the
  ramp needs ≥3 intermediate steps of the *same* fill dimension to read as
  quantity; a bare 2-way white/black flip reads as a qualitative switch
  instead, even though these two facts are hard to reconcile fully.
- `▫◻▪◼` or better `◽◻` size families — `▪` (small) vs `◻`/`◼` (medium) —
  I feel a weak size-magnitude sense purely from name/rendered-size (small →
  medium → presumably "large" if it existed), but rendering-dependent; at
  the font sizes I'm imagining, size differences among these symbols are
  subtle. Strength: LOW-MEDIUM, flagging as tentative rather than confident.
- `▹▸►` — right-pointing arrow/triangle size ramp: small-white-triangle →
  small-black-triangle → black-pointer(larger). ↑ increasing size/"weight."
  Strength: MEDIUM. Immediacy: MEDIUM — some of the size gap is subtle at
  typical rendering, and the white→black switch (▹→▸) doesn't itself carry
  magnitude (per the point above) so the sequence is really "size ramp with
  an incidental fill-switch in the middle," not a pure single-dimension
  ramp. Worth someone re-checking at a larger point size.
- `▵▴` and `▽▾` (small triangles, white/black) — again no magnitude feel
  from the fill switch itself, consistent with the finding above.
- `◦○◯` — bullet → circle → large circle: ↑ increasing size, purely by
  named/rendered diameter. Strength: MEDIUM-HIGH, immediacy: HIGH (size is a
  raw percept) — but I'm slightly unsure ◦ vs ○ actually render at visibly
  different sizes vs. just different weight in every font; flagging as a
  "believe it's there, haven't cross-checked rendering" item.

## U+2800–U+28FF Braille Patterns

- `⠀⠁⠃⠇⠏⠟⠿` — ↑ increasing (blank → 1 dot → 2 dots → 3 dots → 4 dots → 5
  dots → 6 dots, using the low-byte-mask progression so each step adds one
  more filled dot-position). Strength: HIGH. Immediacy: **HIGH** — the "more
  dots visible" is a raw density percept, not unlike the block-shading ramp,
  though slightly noisier because the dot *positions* jump around the 2x3
  cell rather than filling a consistent direction, so it reads a beat slower
  than ▁▂▃▄▅▆▇█ despite being the same "count" idea. Good candidate for the
  "scattered codepoints, strong feel" ask in the brief — codepoints here are
  bit-mask ordered, not dot-count ordered, so I had to hand-pick the dot-count
  subsequence out of the block; a fresh agent given the raw 2800-28FF block in
  codepoint order would NOT perceive a monotonic ramp there.

## U+2150–U+218F Number Forms

- `⅛⅕⅓⅜⅔⅝⅞` (mixed-denominator fractions, sorted by value: 1/8, 1/5,
  1/3, 3/8, 2/3, 5/8, 7/8) — ↑ increasing numeric value, but immediacy:
  **LOW** — this requires doing the division in my head for each glyph, it's
  pure symbol/arithmetic lookup, no perceptual shortcut at all (unlike the
  circled-digit case, there isn't even a monotonic glyph-shape cue). Strength
  is nevertheless fairly high once the arithmetic is done, since fraction
  values are unambiguous. Flagging as a clear immediacy-low/strength-high
  example, maybe the cleanest one in the survey.
- `ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ` — Roman numerals one through ten. Immediacy: LOW-MEDIUM.
  Interesting internal texture: I-II-III is a genuine visual stroke-count
  ramp (immediate, like tally marks) but IV breaks it — four strokes would be
  "IIII" but subtractive notation shows only two glyphs "IV", so the
  perceptual stroke-count ramp actually inverts/resets right at 4 before the
  symbolic (numeral-literacy) reading takes back over for V-X. I notice this
  matters for the brief's request for internal texture notes — this sequence
  is not uniformly immediacy-low, it's low-BUT-WITH-A-TALLY-MARK-POCKET at
  the front.
- `ↀↁↂ` (Roman 1000, 5000, 10000) — pure lookup, immediacy LOW, strength
  MEDIUM (relies on knowing these specific archaic glyphs, less confident a
  fresh agent recovers this without prior Roman-numeral exposure).

## U+1F311–U+1F318 Moon Phases (Supplemental Symbols and Pictographs neighborhood)

- `🌑🌒🌓🌔🌕` — ↑ increasing illuminated fraction (new → waxing crescent →
  first quarter → waxing gibbous → full). Strength: very high. Immediacy:
  **HIGH** — same texture as the pie-fill circle ramp (◌○◔◑◕●) above, but
  richer/more recognizable imagery; "how much of the disc is lit" is a raw
  percept. Then `🌕🌖🌗🌘🌑` continues symmetrically decreasing back to new —
  a case with a genuine round-trip (up then down) rather than a pure
  monotonic ramp, worth flagging since the brief was about monotonic
  sequences and this one is only monotonic on each half.

## U+1F780–U+1F7FF Geometric Shapes Extended — stroke-weight ramps, named as such

- `🞅🞆🞇🞈🞉` (MEDIUM BOLD WHITE CIRCLE → BOLD → HEAVY → VERY HEAVY → EXTREMELY
  HEAVY, all "white circle") — ↑ increasing outline weight. Strength: HIGH —
  and unusually, Unicode's own names spell out the exact ramp
  (medium-bold/bold/heavy/very-heavy/extremely-heavy), so this is a rare case
  where the naming convention IS the magnitude scale, not just a coincidental
  semantic ladder. Immediacy: MEDIUM — outline-thickness differences are
  real but subtle at typical rendering sizes, so it's a percept but a faint
  one; I'd rate it well below the fill-based ramps in how forcefully "more"
  arrives.
- `🞌🞍🞎🞏🞐🞑🞒🞓` (tiny→slightly small→light→medium→bold→heavy→very heavy→
  extremely heavy squares) — same texture, same caveat, size+weight
  compounded which makes it a bit more immediate than the circle-weight one
  above.
- `🞗🞘🞙` (tiny→very small→medium small black diamond) — a size ramp, three
  steps, feels like the weakest/most-subtle of this family — flagging
  low-medium confidence rather than including it as a strong finding.

## U+2190–U+21FF Arrows

- `→⇒⇛` (single, double, triple-line rightwards arrow) — ↑ increasing.
  Strength: HIGH. Immediacy: **HIGH** — more parallel strokes reads as "more
  emphatic/more force" almost like the ≪/⋘ chevron-stacking below; this is a
  genuinely scattered-codepoint find (U+2192, U+21D2, U+21DB — not adjacent)
  that still feels strongly monotonic, which is exactly the kind of thing
  Joseph asked for by name. Same shape works for leftwards: `←⇐⇚`.
- `⇀⇒` type half-vs-full-headed arrows: I don't get a magnitude feel from
  harpoon (half-barb) vs full arrowhead — reads as a different *meaning*
  (one-directional reaction vs full arrow), not "less."

## U+2200–U+22FF Mathematical Operators

- `<≪⋘` — ↑ increasing ("less than" → "much less than" → "very much less
  than"). Strength: **very high**, and this one is explicitly named in
  Unicode itself as a magnitude ladder (the names literally say "much" /
  "very much"), so it's a case where semantic naming and glyph-stacking
  agree. Immediacy: **HIGH** — the visual chevron-stacking (1 wedge → 2
  wedges → 3 wedges) reads as pure "more of the same shape," almost as
  immediate as the block-fill ramp; I'd rank it just below ▁-█ and
  ◌○◔◑◕● in immediacy, and possibly above them in how surprising the find
  felt (I hadn't consciously known Unicode had a "very much less than," it
  fell straight out of scanning the block). Mirror form `>≫⋙` obviously
  the same for the other direction.
- `≤≦` / `⊆⊂`-type equal-vs-strict pairs: no felt magnitude between them —
  reads as a boolean modifier (inclusive/exclusive), not a "how much more"
  step. Consistent with the white/black-square non-finding above: a single
  binary toggle doesn't read as magnitude even when the underlying math
  concept clearly IS ordered (⊆ is technically weaker/more-permissive than
  ⊂, but perceptually the glyphs read as siblings, not a ramp).
- `≺≼` (precedes / precedes-or-equal) — same non-finding, boolean modifier
  not magnitude.

## U+2680–U+2685 Dice (Miscellaneous Symbols block)

- `⚀⚁⚂⚃⚄⚅` — ↑ increasing pip count 1-6. Strength: **maximal**. Immediacy:
  **HIGH-ish but not pure** — I subitize 1, 2, 3 instantly as raw dot-count
  percept, same texture as the braille ramp above, but 4/5/6 I feel myself
  doing a half-beat of counting rather than instant subitizing (this matches
  the general human subitizing-limit-around-4 finding, worth noting since it
  showed up unprompted in my own perception here). This is one of the ones
  Joseph said he expected — confirming it, plus the subitizing-boundary
  texture as the thing I'd add beyond "yes obviously monotonic."

## U+2630–U+2637 Trigrams (I Ching, Miscellaneous Symbols block)

- `☰☱☲☳☴☵☶☷` (Heaven, Lake, Fire, Thunder, Wind, Water, Mountain, Earth) —
  codepoint order does NOT give me a magnitude feel at all on first look —
  I don't have an overlearned "which trigram is more" mapping the way I do
  for digits or dot-counts. If I map to the standard King Wen binary-line
  reading (unbroken=1/broken=0, read as 3-bit binary low-to-high) I get a
  reordering: `☷☶☵☴☳☲☱☰` (Earth 000 → Heaven 111) which WOULD be monotonic
  by that convention — but that's a fact I'm retrieving, not something I
  perceive directly by looking at the broken/unbroken line patterns; even
  after retrieving the convention, counting broken-vs-solid lines per glyph
  to place it is real cognitive work, not a percept. Strength if you accept
  the binary-convention reordering: MEDIUM. Immediacy: LOW regardless of
  ordering. I'm noting this because Joseph specifically flagged expecting
  it, and my honest first-instinct is that the ordering is NOT perceptually
  available to me the way the dice or block-ramp are — this is a
  strength/immediacy split worth taking seriously rather than a case I can
  round up to "yes, monotonic."

- `▁▂▃▄▅▆▇█` — ↑ increasing. Strength: **maximal**, and immediacy: **HIGH** —
  this is the one where "more" arrives in the percept itself, no lookup
  required. Pure fill-height ramp. This is what a "true" magnitude sequence
  feels like to me, and it recalibrated how I read everything else in this
  survey: I now treat "would I need to look something up" as the load-bearing
  test Joseph is pointing at.
- `░▒▓█` — ↑ increasing density/darkness. Strength: very high. Immediacy:
  HIGH — pure visual density, no symbolic mediation. Slightly less crisp
  than the eighths-ramp above because there are only 4 discrete steps and the
  jump from ▓ to █ feels a bit larger than ░→▒→▓, but the direction is
  unambiguous.
- `▏▎▍▌▋▊▉█` — ↑ increasing (left-aligned eighths). Strength maximal,
  immediacy HIGH. Same family as the ▁-▇ ramp, rotated 90°. Note for later:
  I find the *vertical* (▁▂▃▄▅▆▇█) ramp reads faster/more viscerally than the
  *horizontal* (▏▎▍▌▋▊▉█) one — plausibly because "up = more" is an
  overlearned metaphor stacking with the fill percept, whereas "rightward
  fill = more" doesn't get that same metaphor boost. Worth someone checking
  whether this is a real, general asymmetry (vertical ramps > horizontal
  ramps in strength) across other groups.
- Quadrant blocks (▖▗▘▝ single-quadrant vs ▙▚▛▜▞▟ multi-quadrant vs ▄▀▌▐
  half-blocks) — I can feel a rough "how much of the cell is filled"
  ordering (1 quadrant < 2 quadrants < 3 quadrants < full) but it's much
  weaker/slower than the linear ramp above — I have to count filled corners,
  which is closer to a lookup than a percept. Immediacy: MEDIUM. Not
  including as a clean sequence — flagging as a "near miss" instead.

---

## Running synthesis (first-pass, will not overthink this further per the brief's own warning)

**The immediacy axis, ranked by feel, strongest→weakest (my honest gut order):**

1. `▁▂▃▄▅▆▇█` (block fill) and `◌○◔◑◕●` / `🌑🌒🌓🌔🌕` (pie/disc fill) —
   percept arrives with zero lookup, these feel like the same underlying
   mechanism (area/fill fraction) wearing three different costumes.
2. `<≪⋘` (chevron-stacking) and `→⇒⇛` (stroke-stacking arrows) — "more
   copies of the same mark" reading as "more of the concept," still very
   immediate, one notch below pure fill because it's a count-of-strokes
   rather than continuous area.
3. `⚀⚁⚂⚃⚄⚅` (dice) and `⠀⠁⠃⠇⠏⠟⠿` (braille dots) — dot-count/subitizing;
   immediate for small counts, a hair slower once past ~4.
4. Stroke-weight ramps (🞅🞆🞇🞈🞉) — real percept, subtle at rendering scale.
5. `①②③④⑤⑥⑦⑧⑨⑩`-style enclosed/circled/parenthesized digits, Roman
   numerals, fractions — strong strength, but immediacy is essentially
   ZERO: these are digit/symbol lookups wearing a decorative shape. This
   was the biggest recalibration for me mid-survey: I initially wanted to
   report these as my top finds because the pairwise-recoverability
   confidence is so high, and only after hitting the block-elements ramp
   did I feel the qualitative difference Joseph's immediacy question is
   pointing at. I'd guess a naive pass (mine, an hour ago) over-weights
   category 5 and under-reports categories 1-3, because strength is easy
   to introspect and immediacy is not — you have to catch yourself doing
   the lookup, which is fast enough to hide from casual self-report.

**A recurring non-finding worth stating plainly:** binary white/black or
inclusive/exclusive toggles (▫▪, ⊂⊆, ≤≦, ◐/◑/◒/◓ same-fraction-different-
orientation) essentially never read as magnitude to me, even when the
underlying semantics are technically ordered. Monotonic *feel* seems to need
either (a) a continuous/steppable fill or count dimension, or (b) an
overlearned numeral-literacy shortcut (digits, Roman numerals) — a bare
qualitative flip doesn't supply either.

**Trigrams**, which Joseph named as an expected hit: my honest first
instinct is these do NOT carry a perceptual ordering for me at all without
retrieving the King-Wen binary convention, and even then it's arithmetic,
not percept. Reporting this because the brief specifically invited candor
about codepoint order vs semantic order, and this felt like a case worth
not rounding up.

**Vertical vs horizontal fill ramps:** ▁▂▃▄▅▆▇█ felt more immediate to me
than ▏▎▍▌▋▊▉█ despite being the identical concept rotated — flagging as a
possible general effect (vertical=more overlearned via bar charts / height
metaphors) worth a second surveyor's opinion, since I only have one data
point (myself) on it.

