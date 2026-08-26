# grok-instinctive-sequences

Magnitude sequences that feel ordered **to me**. Not a Unicode survey. Codepoints are traces. Scattered is fine when the amount is obvious.

“More” is whatever the sequence makes obvious (count, fill, size, height, nestedness, denoted number). Strength is how sure I am that pairwise “which is more?” recovers the same order.

Panes are dumped with `unicode-group` into a **different** file (`unicode-pane.txt`) and read from there. This file is append-only after this heading.

---

## pictorial — the shape *is* the amount

### dice pips — strong

⚀⚁⚂⚃⚄⚅

Dot-count. The one I would have named unprompted.

### block fill, bottom → full — strong

▁▂▃▄▅▆▇█

How much of the cell is ink, growing upward. Almost a progress bar.

### block fill, left → full — strong

▏▎▍▌▋▊▉█

Same axis, other direction. (█▉▊▋▌▍▎▏ is the same sequence reversed.)

### shade — strong

░▒▓█

░ is sparse, █ is the end of the scale. ░▒▓ without █ still works.

### trigram dissolve, top → empty — strong

☰☱☳☷

Not the bagua as a set (☲ is a hole in the middle, not “more”). This is one line opening, then the next, then the next. Yang draining from the top.

### the rank-countdown we were looking at — strong

☰☱☳☷⚌⚍⚏⚊⚋

Same dissolve, then the 2-line version (skipping ⚎, the other mixed one), then the two atoms. 3-bar → 2-bar → 1-bar, and within each rank, fuller → emptier.

### yang/yin atoms — medium (only two)

⚊⚋

A sequence of two. Still a clean “solid → broken.”

### two-line dissolve — strong

⚌⚍⚏

Same skip of ⚎. Fuller → mixed → empty.

### ellipsis dots — strong

․‥…

One, two, three.

### primes — strong

′″‴⁗

Tick-count. ‵‶‷ is the same in reverse-prime. ⁗ (quadruple) lives in General Punctuation.

### dashes, length — strong

‐–—

Hyphen / en / em. I feel length, not name. ‒ (figure) sits near en; ― (bar) sits near em. The clean three is ‐–—.

### tone letters, pitch height — strong

˥˦˧˨˩

The horizontal sits high, then steps down. Extra-high → extra-low. I read height, not “tone diacritic.”

### counting rods / roman bars, 1–3 — strong

ⅠⅡⅢ

〡〢〣

Stroke-count, same picture in two scripts. After 3 both systems stop being bars (Ⅳ, 〤) and the pictorial scale breaks. ⅠⅡⅢⅣⅤ… is then *denoted*, weaker.

### ogham notches, 1–5 — strong

ᚁᚂᚃᚄᚅ

More scratches. I don’t need to know Ogham.

### braille, adding dots — strong

⠀⠁⠃⠇⠏⠟⠿⣿

Empty → one → two → … → six → eight. Not the whole U+2800 block (that is a bitmask, not a scale). This subsequence is “more dots.”

### vertical bar weight — strong

❘❙❚

Light / medium / heavy. Same stem, more ink.

### daggers — medium

†‡

One crossbar vs two. A pair.

### roots, index — strong

√∛∜

The hanging digit is 2 (implicit), 3, 4. I feel “higher root” as more marks on the check.

### integrals, nested — strong

∫∬∭

One, two, three. ∮ is a *kind* of integral, not “four,” so I stop.

### nested less-than — medium–strong

< ≪ ⋘

More chevrons = more “less.” `>` ≫ ⋙ the same the other way.

---

## size of a same primitive

### filled round, small → large — strong

·•●⬤

A dot, a bullet, a black circle, a large black circle. I might also accept `.` at the front. ◦ is hollow, so I keep it off this line.

### hollow round, small → large — strong

◦○◯

White bullet / white circle / large circle.

### circle fill — strong

○●

Empty → full. ◎ is *nested rings*, a different axis (it can feel “more” than ○ and also “less solid” than ●). I do not put ○◎● on one line without that caveat.

### concentric / nested round — strong

⊙⊚◎

Dot-in-circle → ring-in-circle → bullseye. “More circle inside circle.” ⦿ is ⊙ filled; ⦾⦿ is empty/filled of the double-circle.

### squares, size — strong

▪■⬛

Small black, black, large black. Hollow: ▫□⬜.

### squares, fill — strong

□■

Empty → full. Same for △▲, ▷▶, ◯● if you only want a pair.

### stars, size — medium–strong

⭒⭑⭐

Small → medium. ☆★ is fill, not size. ✶✷✸✹ (6-point → 8 → heavy-8 → 12) feels like “more star” but messier than ⭒⭐.

---

## denoted number — I read the amount

These are not ink-scales (8 is not inkier than 7). They still order for me because I cannot unsee the number.

### digits — strong

0 1 2 3 4 5 6 7 8 9

### circled, including the late zero — strong

⓪①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳

⓪ belongs at the front. Codepoint is later; the amount is 0.

### other circled / dingbat runs — strong (each run separate)

❶❷❸❹❺❻❼❽❾❿

➀➁➂➃➄➅➆➇➈➉

➊➋➌➍➎➏➐➑➒➓

⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾

⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇

⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖⒗⒘⒙⒚⒛

Style-change at 11 (❶…❿ then ⓫…⓴) is a bump; I would not glue those two fonts into one scale.

### superscripts / subscripts — strong

¹²³⁴⁵⁶⁷⁸⁹⁰

₀₁₂₃₄₅₆₇₈₉

⁰ is later than ⁴–⁹; ² and ³ live in Latin-1. I still order them as 0–9.

### roman 1–12 — medium–strong (denoted after Ⅲ)

ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ

Pictorial only through Ⅲ; after that I am reading Roman.

### unit fractions, smaller piece — strong

½ ⅓ ¼ ⅕ ⅙ ⅛ ⅒

The *piece* gets smaller (denominator up). Scattered cps. I would not mix ⅔ ⅜ into this line.

### proper-fraction runs that already increase — strong

¼½¾

⅕⅖⅗⅘

⅙⅚

⅛⅜⅝⅞

### 一 二 三 as bars — strong; 四… as numbers — medium

一二三

一二三四五六七八九十

The first three are counting rods. 四 is a different picture; from there it is denoted Chinese.

### hangzhou 1–9 — medium–strong

〡〢〣〤〥〦〧〨〩

Bars through 3, then denoted.

---

## time / phase (emoji; still Unicode)

### hours — strong

🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛

1 o’clock through 12. I feel clock position / hour count.

### moon, waxing illumination — strong

🌑🌒🌓🌔🌕

New → full. Waning 🌕🌖🌗🌘🌑 is the same axis reversed.

---

## weak, or I would not trust pairwise

- Whole bagua ☰☱☲☳☴☵☶☷ — binary code, not “more.”
- Whole braille block — bitmask, not density order.
- ♩♪♫♬ — duration gets *shorter* as beams get *busier*; two axes fight.
- Script decimal runs I do not sight-read as numbers the way I sight-read `0–9` (Devanagari ०१२…, etc.) — I *know* they are digits; the instinctive punch is weaker.
- Yijing hexagrams in King Wen order — a cast order, not magnitude.
- Box-drawing ─ vs ━ — a pair of weights, not a scale.
- ☹☺☻ — not amount.

---

## from panes

Dumped with `unicode-group` to `unicode-pane.txt` (a different file). Only new orders that punched.

### Spacing Modifier Letters

- **IPA length — strong:** `ˑː`  half-long → long. Same triangular colon, more of it. (Already had `˥˦˧˨˩`.)
- **modifier primes — strong:** `ʹʺ`  one tick → two. Kin to `′″` but this block’s own glyphs.
- **apostrophe count — medium:** `ʼˮ`  one → double.

### General Punctuation

Already had dashes, ․‥…, ′″‴, †‡.

- **asterisks, count — strong:** `⁎⁑⁂`  one → two stacked → asterism (three). The spark: same mark accumulating.
- **primes, through four — strong:** `′″‴⁗`  ⁗ lives here; extend the earlier three.
- **dot punctuation, 3–5 — strong:** `⁖⁘⁙`  three, four, five. (⁚ is two of this family, later cp.)
- **per-n — medium:** `‰‱`  per mille → per ten thousand. Smaller slice / more zeros.
- **double bang — medium:** `!‼`  one → two. Same for `?⁇`.

### Superscripts and Subscripts

Looked. Already had superscripts and subscripts. Nothing new that is a *scale*.

### Letterlike Symbols

Looked. `ℵℶℷℸ` is Hebrew-letter order (and transfinite names), not “more.” I do not feel an amount.

### Number Forms

Already had fractions and Ⅰ–Ⅻ.

- **big roman — medium (denoted):** `Ⅿↁↂↇↈ`  1 000 → 5 000 → 10 000 → 50 000 → 100 000. Same 1–5–10 rhythm as ⅠⅤⅩ, up a thousand.

### Arrows (U+2190–U+21FF)

- **shafts — strong:** `→⇒⇛`  single → double → triple. Same left: `←⇐⇚`. I feel “stronger arrow,” more lines in the stem.
- **how many arrows — strong:** `→⇉⇶`  one, two stacked, three stacked.

### Mathematical Operators

Already had √∛∜, ∫∬∭, < ≪ ⋘, ⊙⊚.

- **contour integrals, dimension — strong:** `∮∯∰`  line → surface → volume. Circles on the integral accumulate.
- **tildes — strong:** `∼≈≋`  one, two, three. Same mark stacked.
- **equality bars — strong:** `=≡≣`  two, three, four bars. More identical.
- **verticals — medium:** `∣∥`  one line → two (divides → parallel).
- **n-ary vs binary, same cup — medium:** `∩⋂` `∪⋃` `∧⋀` `∨⋁`  the n-ary is a bigger instance of the same shape.
- **double subset — medium:** `⊂⋐`  one hook → two.

### Miscellaneous Technical

- **metrical mora count — strong:** `⏗⏘⏙`  triseme → tetraseme → pentaseme. Same mark, more beats.
- **scan-line height — medium:** `⎺⎻⎼⎽`  scan line-1, 3, 7, 9. The bar steps down the cell.

### Geometric Shapes

Already had ○●, ◦○◯, ▪■⬛, □■.

- **circle pie-fill — strong:** `○ ◔ ◐ ◕ ●`  empty → quarter → half → three-quarter → full. The clean analog of ▁–█ for a disk.
- **black square sizes — strong:** `▪◾◼■⬛`  small → medium-small → medium → square → large. (⬛ is in the arrows/misc block; it belongs on this line.)
- **triangle size — strong:** `▴▲`  small black → big black. Same for `▸▶`.

### Miscellaneous Symbols

Already had dice, trigrams, ☺/☻ (rejected), ⚪⚫.

- **go-stones / eyes — medium:** `⚆⚇`  one dot → two (white). Same black: `⚈⚉`. Count of pupils, not fill.
- **flag fill — medium:** `⚐⚑`  empty → filled.
- **plastic recycling 1–7 — medium (denoted):** `♳♴♵♶♷♸♹`  the digit in the triangle is 1 through 7.

### Dingbats

Already had ❘❙❚ and the circled-digit runs.

- **star points — medium–strong:** `✶✷✸✹`  6-point → 8-point → heavy 8-point → 12-point. More rays.
- **ornament quotes — medium:** `❛❝`  single → double. Same as `‘` vs `“`, in this face.
- **check weight — medium:** `✓✔`  light → heavy. Same for `✕✖`.
- **arrow weight, this family — medium:** `➜➝➞➟➠➡`  the stem/head gets heavier as it goes: ➜→➡.

### Miscellaneous Mathematical Symbols-A

- **angle brackets, doubled — strong:** `⟨⟪`  ⟨ → ⟪. Same move as < ≪. Right: `⟩⟫`.

### Supplemental Arrows-A

- **arrow length — strong:** `→⟶`  short → long. Same for `⇒⟹`. I feel stem length, not a new kind of arrow.
- **quadruple shaft — medium:** `⟰`  four stacked heads (up). Extends `→⇒⇛` if you ignore direction: 1, 2, 3, then 4.

### Miscellaneous Mathematical Symbols-B

Already had ⦾⦿ in the concentric note.

- **plus marks — strong:** `+⧺⧻`  plus → double plus → triple plus. Same as primes, for +.
- **vertical bars, to three — strong:** `∣∥⦀`  1, 2, 3 stems. Extends the earlier pair.

### Supplemental Mathematical Operators

- **integrals, to four — strong:** `∫∬∭⨌`  extends ∫∬∭ with quadruple.
- **equals signs in a row — strong:** `=⩵⩶`  one, two, three equals. Programming `==` / `===` made visible.
- **nested less-than — strong:** `<⪡⫷`  1, 2 nested, 3 nested. Kin to but not the same glyphs as < ≪ ⋘.
- **solidus count — medium:** `/⫽⫻`  one, two, three slashes (⫽ is double, ⫻ triple).

### Miscellaneous Symbols and Arrows

Already had ⭐⭑⭒ and ⬤ / ⬛.

- **tiny black square — strong:** `⬝`  very-small; belongs at the front of `▪◾◼■⬛`.
- **heavy circles — medium–strong:** `○⭘⭕`  white circle → heavy circle → heavy large circle. Weight, then size.
- **hexagon fill — medium:** `⬡⬢`  white → black. Same pair as □■.
- **diamond size — medium:** `⬩⬥`  small black → medium black.

### Geometric Shapes Extended

This block is *designed* as weight/size ramps. Strongest new family in the walk.

- **white-circle weight — strong:** `🞅🞆🞇🞈🞉`  medium-bold → bold → heavy → very heavy → extremely heavy. Same ring, more ink.
- **white-square weight — strong:** `🞎🞏🞐🞑🞒🞓`  light → … → extremely heavy.
- **five-spoked asterisk weight — strong:** `🞯🞰🞱🞲🞳🞴`  light → extremely heavy. Six-spoked `🞵`–`🞺` and eight-spoked `🞻`–`🞿` are the same ramp at more rays.
- **spoke count, same weight — strong:** `🞯🞵🞻`  5, 6, 8 spokes (the light step of each). More rays, not more ink.
- **tiny black square — strong:** `🞌`  tinier than `⬝`. Front of the square-size line if we allow scatter.
- **round target nestedness — medium–strong:** `🞊🞋`  circle-in-circle → round target (more rings).

### Modifier Tone Letters

Already had `˥˦˧˨˩`.

- **dotted tone bars — strong:** `꜈꜉꜊꜋꜌`  extra-high → extra-low, dotted. Same five steps as `˥–˩`.
- **left-stem tone bars — strong:** `꜒꜓꜔꜕꜖`  the same ladder, stem on the left.

### Supplemental Punctuation

- **em-count dashes — strong:** `—⸺⸻`  em → two-em → three-em. Extends `‐–—` if you want the whole length line: hyphen, en, em, 2-em, 3-em.
- **vertical dots, to six — medium:** `⁝⁞⸽`  tricolon → four dots → six dots.
- **double paren — medium:** `(⸨`  one parenthesis → two. Same move as `⟨⟪`.

### CJK Symbols and Punctuation

Already had `〡〢〣` and hangzhou 1–9.

- **CJK angle nest — strong:** `〈《`  〈 → 《. Same chevron-doubling as `⟨⟪`.
- **hangzhou tens — medium (denoted):** `〸〹〺`  10, 20, 30.
- **hangul tone dots — medium:** `〮〯`  one dot → two.

### Box Drawing

Earlier I filed `─` vs `━` as a mere pair. Standing by that for weight. One count-scale does punch:

- **dash fragments — medium:** `┄┈`  triple-dash → quadruple-dash (light). More breaks in the line. Heavy twins `┅┉`.

### Counting Rod Numerals

- **ideographic tally 1–5 — strong:** `𝍲𝍳𝍴𝍵𝍶`  one scratch through the five-bar gate. Pure count.
- **counting-rod units 1–9 — medium–strong:** `𝍠𝍡𝍢𝍣𝍤𝍥𝍦𝍧𝍨`  kin to hangzhou; pictorial early, denoted later. Tens digits `𝍩`–`𝍱` are the same 1–9 turned.

### Tai Xuan Jing Symbols

Looked. Tetragrams are a catalog, not a scale (same failure as King Wen hexagrams). The opening `𝌀` then `𝌁`–`𝌅` is monogram → digrams (1 bar → 2), which *is* the same rank move as `⚊` / `⚌`, but I would not stretch it into the 81 tetragrams.

### Mahjong Tiles

- **circles 1–9 — strong:** `🀙🀚🀛🀜🀝🀞🀟🀠🀡`  pip-count on the tile. Kin to dice.
- **bamboos 1–9 — strong:** `🀐`–`🀘`  stick-count.
- **characters 1–9 — medium (denoted):** `🀇`–`🀏`  I read the numeral; the face is not a pip scale.

### Domino Tiles

- **doubles 0–6 — strong:** `🀱🀹🁁🁉🁑🁙🁡`  0-0 through 6-6. Total pips 0,2,4,6,8,10,12 — or just “the number on the tile.” Horizontal; vertical copies exist later in the block.

### Supplemental Arrows-C

Designed ramps, like Geometric Shapes Extended.

- **arrowhead size — strong:** `🠂🠆🠊`  small → medium → large (rightwards triangle head).
- **shaft weight — strong:** `🠢🠦🠪🠮🠲`  narrow → medium → bold → heavy → very heavy.
- **barb weight — strong:** `🡢🡪🡲🡺🢂`  light → … → very heavy wide-headed barb.

### Enclosed Alphanumeric Supplement

- **digit + comma 0–9 — strong (denoted):** `🄁`–`🄊`  0, through 9,.
- **sans-serif circled zero — strong:** `🄋`  belongs in front of `➀–➉` (the ➀ series). Negative twin `🄌` in front of `➊–➓`.

### Combining Diacritical Marks

- **dot count above — strong:** `̇̈`  one dot → two (diaeresis). (Three and four live in the *for Symbols* block: `⃛⃜`.)
- **acute / grave doubling — medium:** `́̋`  acute → double acute. `̀̏` grave → double grave.
- **overline weight — medium:** `̅̿`  overline → double overline. Same below: `̱̳`.

### Combining Diacritical Marks for Symbols (U+20D0–U+20FF)

- **dots above, 3–4 — strong:** `⃛⃜`  three → four. Completes `̇̈⃛⃜` as 1,2,3,4 dots.
- **triple underdot — medium:** `⃨`  three below; sits with the above count.

### Supplemental Symbols and Pictographs

- **medals — medium:** `🥇🥈🥉`  gold → silver → bronze. Prestige *descends* as the codepoint *ascends*. I still feel a clean 1st / 2nd / 3rd.

### Miscellaneous Symbols and Pictographs (U+1F300–U+1F5FF)

Already had moons and clock faces.

- **speaker volume — strong:** `🔇🔈🔉🔊`  muted → speaker → one wave → three waves. (No two-wave step.) Right-speaker twin `🕨🕩🕪`.
- **brightness — medium:** `🔅🔆`  dim → bright.
- **skin-tone modifiers — strong (designed 1–5):** `🏻🏼🏽🏾🏿`  Fitzpatrick type 1–2 through 6. Light → dark; a real ladder, not a catalog.

### Supplemental Arrows-B

- **dashed-arrow segments — strong:** `⤍⤏`  double-dash → triple-dash (rightwards). Same left: `⤌⤎`.
- **triple arrows, vertical — medium:** `⤊⤋`  3 shafts up / down. Kin to `⇛`.

### Playing Cards

- **pip ranks 2–10 — strong:** `🂢`–`🂪`  two through ten of spades (same for the other suits). Ace and faces are a different picture; I would not glue A-J-Q-K onto this.
- **tarot trumps 1–21 — medium (denoted):** `🃡`–`🃵`  numbered trumps. The Fool sits before 1 and is not “zero pips.”

### Mathematical Alphanumeric Symbols

Looked. Five more 0–9 faces (bold, double-struck, sans, sans-bold, mono). Same denoted scale as ASCII digits, different type. No new *kind* of magnitude.

### Enclosed CJK Letters and Months

- **circled 21–50 — strong (denoted):** `㉑`–`㉟` then `㊱`–`㊿`  continues `①`–`⑳` (1–20). One sequence in two cp-ranges.
- **parenthesized ideographs 1–10 — strong (denoted):** `㈠`–`㈩`
- **circled ideographs 1–10 — strong (denoted):** `㊀`–`㊉`
- **tens on a black square — medium (denoted):** `㉈㉉㉊㉋㉌㉍㉎㉏`  10,20,…,80.
- **telegraph months — medium:** `㋀`–`㋋`  January–December as 1–12.

### Musical Symbols

Earlier I rejected `♩♪♫♬` because duration and beam-count fight. This block is the real duration ladder:

- **note duration — strong (time shrinks):** `𝅝𝅗𝅥𝅘𝅥𝅘𝅥𝅮𝅘𝅥𝅯𝅘𝅥𝅰𝅘𝅥𝅱𝅘𝅥𝅲`  whole → half → quarter → 8th → 16th → 32nd → 64th → 128th. More flags = *less* time. I would answer “which is more?” as duration, not ink.
- **rest duration — strong (same axis):** `𝄽`–`𝅂`  quarter rest through 128th rest.

### Ancient Greek Numbers

- **Attic fives — medium (denoted):** `𐅃𐅄𐅅𐅆𐅇`  5, 50, 500, 5 000, 50 000. I know the names; I do not *see* a 10× without that.

### Transport and Map Symbols

Looked. Vehicles and signs, not amounts. `🛨` vs `🛩` is “small airplane” twice in different orientations, not a size ramp.

### Emoticons

Looked. Faces, not amounts. `🙁🙂` is frown/smile, not more/less.

### Control Pictures

Looked. Named control codes in little boxes. Not a scale.

### Halfwidth and Fullwidth Forms

- **fullwidth digits — strong (denoted):** `０`–`９`  0–9, wide. Same scale as ASCII, different cell.

### Kanbun

- **annotation 1–4 — strong:** `㆒㆓㆔㆕`  one through four marks. Pictorial bars, then 4.
- **first–fourth — medium (denoted):** `㆙㆚㆛㆜`  甲-style 1st–4th. `㆖㆗㆘` is top/mid/bottom — position, not amount.

### Symbols for Legacy Computing

Sextants `🬀`– are a bitmask like braille — the whole set is not a scale.

- **upper eighths, odd steps — strong:** `🮃🮄🮆`  3/8, 5/8, 7/8 from the top. Fills the gaps in `▀` / `▄` / `█`.
- **right eighths, odd steps — strong:** `🮈🮉🮋`  3/8, 5/8, 7/8 from the right. Same for `▌` / `▐`.
- **segmented digits — strong (denoted):** `🯰`–`🯹`  0–9 in seven-segment. I read the number; the bars are a display, not a count.

### Chess Symbols

Looked. Pieces and rotations, not amounts. King/queen/rook is a catalog of roles.

### Aegean Numbers

- **1–9 — strong (denoted / often pictorial):** `𐄇`–`𐄏`
- **tens 10–90 — medium (denoted):** `𐄐`–`𐄘`  then hundreds `𐄙`–`𐄡`, thousands `𐄢`–. Same 1–9 rhythm at each power.

### Ornamental Dingbats

- **leaf weight — medium:** `🙐🙘🙜`  leaf → vine → heavy vine (NW). Same for the other three corners.
- **quilt fill — medium:** `🙨🙪`  hollow → solid.

### Optical Character Recognition

Looked. MICR bank glyphs. Not amounts.

### Alchemical Symbols

Looked. Elements and metals are a catalog (“fire / water”), not more/less.

### Currency Symbols

Looked. A catalog of units, not more/less.

### Latin-1 Supplement

Already had `¼½¾` and `²³` (with `¹` in the superscript line). Nothing else in the block is a scale.

### Arabic

- **Arabic-Indic roots — strong:** `؆؇`  cube → fourth. Completes `√∛∜` in another face (no square-root twin here).
- **Arabic-Indic per-n — medium:** `؉؊`  per mille → per ten thousand. Twin of `‰‱`.
- Two digit runs (`٠`–`٩`, `۰`–`۹`). Denoted; weaker for me than ASCII.

### Ethiopic (number tail)

- **digits 1–9 — strong (denoted):** `፩`–`፱`
- **tens 10–90 — medium (denoted):** `፲`–`፺`  then `፻` hundred, `፼` ten thousand.

### Khmer Symbols

- **koet 1–15 — medium (denoted lunar):** `᧡`–`᧯`  muoy…dap-pram. Twin series `᧱`–`᧿` (roc). I trust the names more than the shapes.

### Ogham (full block)

Already had `ᚁ`–`ᚅ`. Three more 1–5 notch groups, different side of the stem:

- `ᚆ`–`ᚊ`  across
- `ᚐ`–`ᚔ`  along (the vowels)
- `ᚕ`–`ᚙ`  forfeda (extra letters; still 1–5 marks)

Same count-feel as the first aicme. Not one 20-letter magnitude line.

### Combining Diacritical Marks Extended

- **triple dot — strong:** `᪴`  sits in `̇̈᪴⃛` as 1,2,3,(and `⃜` = 4).
- **triple acute — medium:** `᫋`  extends `́̋`.
- **plus marks above — medium:** `᫈᫉`  plus → double plus. Twin of `+⧺`.
- **parentheses above — medium:** `᪻᪼`  one pair → double.

### Combining Diacritical Marks Supplement

Looked. Extra letter-combiners and tone contours, not a count ladder.

### Tamil numbers

- **digits 0–9 — medium (denoted).**
- **10, 100, 1000 — strong (denoted):** `௰௱௲`  ௰ ௱ ௲. Powers of ten as three glyphs.

### Tibetan numbers

- **digits 0–9 — medium (denoted).**
- **half-integers — medium:** `༪`–`༲`  0.5, 1.5, …, 8.5. `༳` is half-zero (−0.5), not the next step.

### Greek and Coptic

Looked. `ϚϞϠ` (stigma, koppa, sampi) are 6 / 90 / 900 in Milesian — learned, not a shape ladder. `ʹ͵` are numeral *signs*, not amounts.

### Runic

Looked. `ᛮᛯᛰ` are golden numbers 17, 18, 19 — three calendar marks, not a count I can *see*.

### Block Elements (dumped, not from memory)

Had `▁`–`█` and `▏`…`█` and `░▒▓`. Missed from the actual 32:

- **upper eighth — medium:** `▔`  top 1/8. The rest of the upper-eighths ladder is in Legacy Computing; here it is a stub next to `▀` (upper half).
- **right eighth / right half — medium:** `▕` `▐`  mirror of `▏` / `▌`.
- **quadrant *count* — medium:** `▖` (1) `▌` (2) `▙` (3) `█` (4). The 16 quadrants themselves are a bitmask, like braille; this is one representative per popcount.

### Braille Patterns (dumped, not from memory)

The whole 256 is still a bitmask. The fill line I wrote earlier skipped *seven*:

- **low-bit fill 0–8 — strong:** `⠀⠁⠃⠇⠏⠟⠿⡿⣿`  ⠀⠁⠃⠇⠏⠟⠿⡿⣿. I had jumped 6→8.
- **high-bit fill 1–8 — strong:** `⢀⣀⣠⣰⣸⣼⣾⣿`  ⢀⣀⣠⣰⣸⣼⣾⣿. Same count, other end of the cell.

### Enclosed Alphanumerics (dumped, not from memory)

The number runs I already listed are all here and complete: `①`–`⑳`, `⑴`–`⒇`, `⒈`–`⒛`, `⓵`–`⓾`, `⓪` at the front of the white-circled line.

Missed:

- **negative zero — strong:** `⓿`  `⓿` belongs in front of `❶`–`❿` (dingbat 1–10) and `⓫`–`⓴` (11–20): `⓿❶…❿⓫…⓴` as 0–20 in the black-circle face. I had called 11–20 a bump and omitted 0.
- Circled / parenthesized *letters* are not amounts.

### Script decimal 0–9 (sampled, still < U+2E80)

NKo `߀`–`߉`, Thai `๐`–`๙`, Devanagari `०`–`९`. Same denoted 0–9. NKo is the one I can almost sight-read as Western digits; Devanagari I know rather than *see*. Not a new kind. The other Indic/SE Asian Nd runs will be this again.

### leftover number / CJK / emoji-ext (dumped after the symbol-block walk)

These were the leftover *kinds* — not another pass over Nd 0–9.

#### Mayan Numerals — strong (pictorial)

𝋠𝋡𝋢𝋣𝋤𝋥𝋦𝋧𝋨𝋩𝋪𝋫𝋬𝋭𝋮𝋯𝋰𝋱𝋲𝋳

0 is a shell; 1–4 are dots; 5 is a bar; then bar+dots, two bars, three bars, up to 19. I do not need the names. Same family as dice / tally, in vigesimal.

#### Cuneiform Numbers — strong (wedge count)

𒐀𒐁𒐂𒐃𒐄𒐅𒐆𒐇

TWO ASH through NINE ASH. Stacked wedges. 1-ASH lives in the main Cuneiform block (`𒀸`), so the clean 1–9 is scattered: `𒀸𒐀…𒐇`. DISH / U / GESH2 runs are the same 3–9 (or 1–9) rhythm at other units.

Cuneiform punctuation, diagonal dots — strong: `𒑲𒑳𒑴`  colon → tricolon → quadcolon. Kin to `⁚⁖⁘⁙`.

#### Ideographic Description — strong (slot count)

⿰ vs ⿲ — two constituents across vs three.
⿱ vs ⿳ — two stacked vs three.

I feel “how many pieces this operator takes.” The surround operators (`⿴⿵⿶⿷⿸⿹⿺⿻`) are *kinds* of enclosure, not more/less.

#### Common Indic / Oriya / Malayalam fractions — strong (same two runs as Number Forms)

꠰꠱꠲  and  ୲୳୴  and  ൳൴൵  — ¼ ½ ¾
꠳꠴꠵  and  ୵୶୷  and  ൶൷൸  — 1/16, 1/8, 3/16

Not a new axis. Malayalam also has `൰൱൲`  10, 100, 1000 — twin of Tamil `௰௱௲`.

#### CJK Compatibility — telegraph + SI

- **telegraph hours 0–24 — strong (denoted):** `㍘`–`㍰`
- **telegraph days 1–31 — strong (denoted):** `㏠`–`㏾`
- **SI decade ladders — strong (denoted):** I read the prefix. Clean ones: `㎐㎑㎒㎓㎔`  Hz → THz; `㎰㎱㎲㎳`  ps → ms; `㎀㎁㎂㎃㎄`  pA → kA; `㎩㎪㎫㎬`  Pa → GPa; area `㎟㎠㎡㎢`; volume `㎣㎤㎥㎦`. A new *kind* of denoted scale (powers of 10), not ink.

#### historic 1–3 strokes — strong (pictorial, then denoted)

Another face of `ⅠⅡⅢ` / `〡〢〣` / `一二三`:

- Brahmi numbers `𑁒𑁓𑁔`  (1–3; 4 breaks the bars)
- Kharoshthi `𐩀𐩁𐩂`  (1–3; 4 is a different mark)
- Imperial Aramaic `𐡘𐡙𐡚`
- Phoenician `𐤖𐤚𐤛`  (1, 2, 3 — cps not in order)
- Palmyrene `𐡹𐡺𐡻𐡼`  (1–4 strokes; 5 is a different picture)
- Old Persian `𐏑𐏒`  (1 wedge, 2 wedges)

#### Aegean-shaped denoted inventories — medium, not a new kind

Rumi, Coptic Epact, Sinhala Archaic, Brahmi tens/hundreds, Indic Siyaq, Ottoman Siyaq, Warang Citi, Meroitic Cursive, Pahawh Hmong powers, Mende Kikakui combining powers. Each is 1–9 then 10–90 then 100–900 (or powers of 10). Same denoted shape as Aegean / Ethiopic. I am not listing every script.

#### Enclosed Ideographic Supplement

Looked. Squared CJK words, not a 1–2–3 run. (`🈩` is 一, `🈔` is 二, `🈪` is 三 — scattered and not worth gluing.)

#### Yijing Hexagrams (dumped, confirming)

King Wen order. Not magnitude. `䷀䷁` is the hexagram-scale pair of ☰ / ☷ (all yang vs all yin) — a pair, not a 64-step scale.

#### Symbols and Pictographs Extended-A

- **nest fill — medium:** `🪹🪺`  empty nest → nest with eggs. Same pair-move as `⚐⚑`.
- **battery charge — medium:** `🪫🔋`  low → full. (🔋 lives in Misc. Symbols and Pictographs.)
- `🪆` *means* nestedness but is a singleton, not a sequence.

This dump is Unicode **14.0.0**. Kaktovik numerals (U+1D2C0, Unicode 15 — another Mayan-like vigesimal) are not in this UCD. I have not dumped Byzantine / Znamenny / Ancient Greek musical neumes, nor SignWriting.

### musical neumes (Byzantine, Ancient Greek, Znamenny)

Dumped. The whole blocks are catalogs of signs. A few runs punch as amount.

#### Byzantine Musical Symbols

- **apli → tetrapli — strong:** `𝂅𝂆𝂇𝂈`  1, 2, 3, 4 ticks. Rest of that many chronoi. I see the bars.
- **dyo / tria / tessera — strong:** `𝀯𝀰𝀱`  2, 3, 4. Grouping marks; same count-feel as dice.
- **leimma duration — strong:** `𝂊𝂋𝂌𝂍`  rest of 1, 2, 3, 4 chronoi. `𝂎` is a *half* chronos — off this line (smaller, not five).
- **gorgon count — strong (tempo up):** `𝂏𝂒𝂖`  gorgon → digorgon → trigorgon. More dots = faster = *less* time per note. Same dual-axis as `♩♪♫♬`; I would answer “which is more?” as speed, or as mark-count.
- **argon count — medium–strong (tempo down):** `𝂗𝂘𝂙`  argon → imidiargon → diargon. The slow twin of gorgon.
- **diesis stroke-count — strong:** `𝃐𝃑𝃒𝃓`  apli / monogrammos / digrammos / trigrammos = 2, 4, 6, 8 twelfths of a tone. I see 0→1→2→3 extra strokes, and I read the fraction. Yfesis twin `𝃔𝃕𝃖𝃗` (down, not up).
- **simansis 1–4 beats — medium–strong:** `𝃞𝃟𝃠𝃡`  theseos, disimou, trisimou, tetrasimou. Same for arseos `𝃢𝃣𝃤𝃥`.
- **kentima vs kentimata — medium:** `𝁏𝁎`  one dot → two (neo, above). Archaion twin `𝀛𝀜`.
- **single vs dipli — medium (pairs):** oxeia `𝀃𝀄`, vareia `𝀅𝀆`, ypokrisis `𝀊𝀋`, apostrofos `𝀑𝀒`.

Looked, did not punch as a *shape* scale:

- **agogi poli-argi → poli-gorgi** (`𝂚`–`𝂡`) — eight named tempi, very-slow → very-fast. I read the names. The glyphs are not a ramp.
- Martyria protos/deyteros/tritos/tetartos — 1st–4th mode. Catalog.
- Fthora, chroa, arktiko Pa–Ni — pitch/mode names, not more/less.

#### Ancient Greek Musical Notation

Vocal 1–24 then 50–54, instrumental 1–54: Alypian *pitch* inventory. The numbers are catalog indices, not amounts. I do not feel 𝈀 < 𝈁.

- **combining sesemes — strong:** 𝉂𝉃𝉄  triseme → tetraseme → pentaseme. Same 3–4–5 as the BMP metrical triseme/tetraseme/pentaseme. Combining, not spacing. 𝉅 is a leimma (rest), not “six.”

#### Znamenny Musical Notation

The neumes themselves are a catalog (kryuk, strela, osoka, …). What punches is height and brightness, reused across several families.

- **pitch height, left stem — strong:** 𜼃𜼄𜼅𜼆𜼇𜼈  gorazdo-nizko → nizko → sredne → malo-povyshe → povyshe → vysoko. Very-low through high. Twin on the right: 𜼏𜼐𜼑𜼒𜼓𜼔. Kin to the IPA tone bars, in this notation.
- **brightness — strong:** 𜼰𜼱𜼲  mrachno → svetlo → tresvetlo (dark → light → thrice-light). The same three steps recur on golubchik 𜽠𜽡𜽢, vrakhiya 𜽤𜽥𜽦, skameytsa 𜽱𜽲𜽳, osoka 𜾰𜾱.
- **priznak level — medium:** 𜽂𜽃  level-2 → level-3. A pair; I do not see a level-1 glyph in this block.
- **dot count — medium:** 𜼼𜼽  tochka → dvoetochie (one dot → two). Same pair as ̇̈.

Looked, did not punch as magnitude: the long strela / mechik / osoka inventories (gromnaya, povodnaya, klyuchevaya, …) are named variants, not more/less.

SignWriting is still undumped. Kaktovik still wants Unicode 15.

### leftover BMP (after a block census)

Unicode 14 BMP has 164 blocks. Letter/syllable/ideograph/radical inventories were skipped on purpose. What was still un-stared and *might* have been amount:

- **Arabic isolated dots — strong:** ﮲﮴﮶﮺  1, 2, 3, 4 dots above. Below twins ﮳﮵﮷﮻. Same mark accumulating. Vertical-two (﮽) is a different arrangement, not five.

- **Vedic dot/ring count — strong:** ᳝᳞᳟  1, 2, 3 dots below. ᳚᳛  double -> triple svarita. ᳸᳹  ring -> double ring. Combining, kin to diaeresis.

- **Cyrillic large-number combiners — medium (denoted):** ҂҈҉꙰꙱꙲  thousands, then combining 100 thousand / million / 10 million / 100 million / 1 billion. I read the names; the circling-around-a-letter is the same move getting busier.

- **Bengali currency numerators — medium (denoted):** 1, 2, 3, 4. Then "one less than the denominator" and denominator-sixteen sit off the line.

- **Telugu fraction digits — medium:** 0-3 for odd powers of four, and 1-3 for even. Two parallel 0/1/2/3 runs, not one 1-7.

- **Khmer Lek Attak 0-9 — medium (denoted):** another 0-9 face (son...pram-buon). Same kind as ASCII digits.

- **Lisu tones — medium (pitch, if you know the names):** six named pitch letters. I do not feel a height ramp from the glyphs the way I do from IPA tone bars.

Not amount (looked at names / samples, not dumped as full panes): Kangxi radicals, CJK radicals supplement, CJK strokes, Yi radicals (catalogs of different pictures; "SECOND ONE/TWO/THREE" are variant *forms* of a radical). Vertical Forms and Small Form Variants are presentation twins, not scales. Remaining BMP Nd 0-9 (Bengali, Gurmukhi, Gujarati, Kannada, Lao, Myanmar, Shan, Mongolian, Tai Tham hora/tham, New Tai Lue, ...) is the same denoted kind already sampled.

BMP I would still not call "gone through" only in the letter-inventory sense: Latin/Cyrillic/Hangul/CJK-ideograph/Yi-syllable blocks. Those were never magnitude mines.

### Latin / IPA / phonetic — mutation sequences (looked at the glyphs)

I had treated these blocks as letter catalogs and grepped names for NUMBER. That was the stop. Looking at the shapes:

#### size of one letter (small → big)

The same body in a bigger cell. Strong. Each line is its own sequence:

ₒ o ᴏ O
ₐ a ᴀ A
ₑ e ᴇ E
ᵢ i ɪ I
ᵤ u ᴜ U
ₙ n ɴ N
ₘ m ᴍ M
ₗ l ʟ L
ₕ h ʜ H
ₚ p ᴘ P
ₜ t ᴛ T
ₛ s S
ₓ x X
ᵒ o O
ª a A
º o O

Tiny raised (ªº) sit at the front of a/o. Subscript (ₒₐₑ…) is another front. Small-cap (ᴏᴀ…) sits between small and capital.

#### marks accumulating on one body

ı i ï     no-dot → one dot → two dots. Strong.
o ȯ ö     none → one dot above → two. Strong.
a ȧ ä     same on a.
u ü       two dots (the one-dot twin is scarcer on u).
o ó ő     acute → double acute. Strong.
o ò ȍ     grave → double grave.
e é         and spacing ´ ˝  acute → double acute (already kin to combining ́̋).
l ḷ ḹ     dot below → dot-below + macron.
r ṛ ṝ     same.
o ô ộ     hat → hat + underdot (two marks).
o ơ ợ     horn → horn + underdot.
ø ǿ       stroke → stroke + acute.
a å       ring stacked on a.

Spacing dots already in Latin-1: ¨ is two; ˙ (modifier) is one. Completes ̇̈ as spacing.

#### count inside the alphabet itself

n m     one hump → two. Strong. I do not need the names.
v w     one vee → two. Strong. (w is vv.)
ǀ ǁ     one click-pipe → two. Strong. ǂ is a different picture (barred); ǃ another.
c o     open → closed. Same pair-move as □■, on a letter.
. :     one dot → two stacked. Strong. (Baseline ․‥… is the other direction.)
, ;     comma → comma + extra.
' "     one quote → two. Already had as ʹʺ / ′″.

#### hooks / tails / curls getting longer

n ɲ ɳ ŋ     plain → left hook → right hook → eng-tail. More appendage. Medium–strong.
d ɖ ɗ       tail → hook.
l ɫ ɬ ɭ ɮ   through-tilde → belt → retroflex hook → lezh (l+ezh). More ink / more curl.
s ſ ʃ ʆ     s → long s → esh → esh with curl. Taller, then more curl.
z ʒ ʓ       z → ezh → ezh with curl.
t ʈ ƫ       retroflex → palatal hook.
b ɓ         hook.
g ɠ ɢ       hook, then small-cap (size).
r ɹ ɻ ʀ     turn, hook, small-cap.

#### o-shapes, size and marks together (the illustration)

° º ₒ o ᴏ O ɵ ɔ ɶ ʘ ⱺ

I would not put all of those on one line. Separate axes:

- size: ₒ o ᴏ O  (and º at the very front)
- interior bar: ɵ vs o  (less hole)
- aperture: o ɔ  (more open)
- two-o: o ɶ  (small-cap oe — more o)
- nested: o ʘ  (bilabial click is a circled o) and o ⱺ  (ring *inside* o, Latin Ext-C)

#### not a scale (still looked)

Turned letters (ɐ ɒ ǝ ʌ …) are orientations, not more/less. Ligatures ÆŒĲ are “two letters fused,” a pair with their parts, not a 1–2–3. Vietnamese precomposed piles (ốồổỗ…) are two-mark combos of the same two axes, not a third step.

---

Still walking missed BMP panes in cp order with this aperture. After Latin Ext-C the next misses are Glagolitic, Coptic, Tifinagh, Ethiopic Extended, Cyrillic Ext-A — then Supplemental Punctuation (already done), then **CJK Radicals Supplement U+2E80**.

#### Hangul Jamo (looked at the glyphs, not the names)

ᄀᄁ  ᄃᄄ  ᄇᄈ  ᄉᄊ  ᄌᄍ     one consonant → doubled (ssang). Strong. Same in the batchim: ᆨᆩ  ᆺᆻ.

The rest of the block is clusters (nieun-kiyeok, pieup-sios-kiyeok, …). Those are 2-jamo vs 3-jamo concatenations, not one body growing. I feel count-of-pieces the way I feel ⿰ vs ⿲, weaker than ssang.

Vowels ᅪ ᅫ ᅬ ᅯ ᅰ ᅱ ᅴ are fused pairs of vowels; a catalog of which two, not a 1–2–3 of the same vowel.

#### Greek Extended (polytonic)

Same mark-accumulation as Vietnamese o, on Greek bodies.

α ἀ ἄ ἆ ᾳ ᾷ     none → breathing → breathing+oxia → perispomeni → iota-subscript → circ+iota. More marks.

Spacing: ῍ ῎ ῏  psili+varia / +oxia / +perispomeni. Dasia twins ῝῞῟.

### Ethiopic (full pane)

The 7 orders of one consonant (ለሉሊላሌልሎ) are the same body with ticks and loops added. I feel “more mark” along the row, not as cleanly as Canadian’s extra dot, but it is a mutation series. The WA form (ሏ, ሟ, …) is one more appendage on top of that.

Combining: ፞ length, ፟ gemination, ፝ both. Two axes, then the pair.

Punctuation dots: ፡ wordspace (two dots) → ። full stop (four, a square of dots). Strong. Same family as . :

Tone marks: ᎒ rikrik vs ᎓ short rikrik. Size of the same mark.

### Cherokee

Looked at the glyphs. Some families of similar bodies (ᎹᎺᎻᎼᎽ). Not a systematic extra-dot / extra-size machine the way Canadian is. I would not force a scale.

### Canadian Aboriginal Syllabics

This block *is* mutation. The famous rotation (ᐁᐃᐅᐊ  E/I/O/A as one triangle turning) is orientation, not amount — same failure as bagua. What *is* amount:

- **length as a dot — strong:** ᐃᐄ  I → II. ᐅᐆ  O → OO. ᐊᐋ  A → AA. Repeats on every series: ᐱᐲ  ᑎᑏ  ᕿᖀ  …  The long one is the short one plus a mark I can see.

- **full vs final — strong (size):** ᐱᑉ  PI → P. The final is the small one. Same for T, K, M, N, S, Y, Q (ᕿᖅ), Nunavik H (ᕴ…ᕺ → ᕻ). Identical to ₒ o, in another script.

- **ring fill — strong:** ᐡᐢᐣᐤ  bottom-half → top-half → right-half → full ring. More of the circle. Small twin in the extension: ᣞ  final *small* ring, in front of ᐤ.

- **acute count — strong:** ᐟᐥ  final acute → double acute.

- **west-cree ring — medium–strong:** ᐌᐍ  WE → west-cree WE. An extra ring on the same triangle. Nestedness. Repeats across P/T/K/C/M/N/L/S/Y.

- **w-dot — medium:** ᐧ  middle dot. Labialization as a mark you add. (Dedicated WE characters already include it.)

- **more of the same consonant — medium:** ᖕᖖ  NG → NNG.

Carrier length (ᗆᗇ ghe → ghee) looks like an extra stroke on a C-body. Same length-axis, different mark than the Cree dot.

Extension: ᢱᢲ  AY → AAY, same extra-mark-for-length.

Not amount: the four-way rotation itself; Blackfoot/Carrier vowel *direction* as a catalog of which way the body points.

The rotation veto was too fast. Continuation is enough for an ordering, even when I cannot name the axis or answer pairwise “which is more?” without picking an origin.

I do **not** instinctively feel Joseph’s ᐃᐅᐁᐊ as *my* sequence (right, left, down, up — the 180° first). What I *can* continue, once a start and a hand are given, is 90° steps of the same triangle: from ᐃ (pointing right) clockwise ᐃᐁᐅᐊ, or the other way. That is a cycle, so “more” is more turn *from here*, and 360° lands on the start. Axis-ambiguous, still an ordering. The bagua comparison was the wrong door: King Wen is not a continuation; these four *are*.

Same opening for other “just orientation” dismissals: a ɐ is a 180° pair I can continue (one flip); Blackfoot ᖰᖱᖲᖳ is another four-way turn of one body. I will not promote those to “strong amount.” I will not throw them out for lacking a name.

The “clockwise from pointing-right” story was from Cree *names* (I/O/E/A → east/west/south/north in the textbooks), not from the glyphs as they render here. In Joseph’s font those codepoints did not show as four compass directions, and the sequence I called clockwise did not look like a clock. Pointing-direction claims about these four are unverified for this face. The continuation-pattern opening still stands; this particular clock was unearned.

Joseph’s pointing (corrected): East = right-pointing (ᐃ), West = left-pointing (ᐅ, 180° from East), South = down (ᐁ), North = up (ᐊ). His sequence ᐃᐅᐁᐊ is E W S N — right, left, down, up; a 180° first. That is not clockwise. Clockwise from East is E S W N = ᐃᐁᐅᐊ. Counter-clockwise from East is E N W S = ᐃᐊᐅᐁ.

The 90° clock I said I could continue from ᐃ pointing right (ᐃᐁᐅᐊ) *is* that clockwise sequence. I still do not feel E-W-S-N as my turn; that remains his. An earlier line here had East as left-pointing; he retracted that.

The pointing-direction argument was me labeling codepoints from a mental Cree chart, then contradicting the picture. A screenshot of ᐃᐅᐁᐊ in Joseph’s face: up, right, down, left. Only “South (down)” matched the glyph. In that render, ᐃᐅᐁᐊ *is* 90° clockwise from north. I had called it “not clockwise” about triangles I was not seeing.

### Philippine scripts (Tagalog, Hanunoo, Buhid, Tagbanwa)

Letters are a catalog. What continues:

᜵᜶  Philippine single punctuation → double. Same as ।॥.

Kudlit ᜒ / ᜓ (i above, u below) is a flip of one mark, not more.

### Khmer (full pane)

Length as extra mark, same feel as Canadian’s extra dot: ិី  i → ii. ុូ  u → uu. ឹឺ  y → yy.

។៕  khan → bariyoosan. One bar, then two. Kin to danda.

Digits and lek attak already noted.

### Mongolian

᠄᠅  colon → four dots. More dots. ᠁ ellipsis sits with that family. Digits ᠐–᠙ same denoted 0–9.

### Tai Le / New Tai Lue / Tai Tham / Limbu / Buginese

Length again as extra mark: Tai Tham ᩥᩦ i→ii, ᩩᩪ u→uu. Same continuation as Khmer.

New Tai Lue ᧈᧉ tone-1 → tone-2: a pair I can continue (one more mark), not a 1–5 ladder I trust from shape.

Tai Le ᥰ–ᥴ named tone-2 through 6. I do not feel a clean extra-stroke series from the glyphs.

Limbu, Buginese: letters. Buginese ᨞ pallawa vs ᨟ end-of-section is two punctuation marks, not obviously 1 then 2 of the same.

### Balinese / Sundanese / Batak / Lepcha / Ol Chiki

Balinese tedung is the extra-length mark stacked on a vowel: ᬅᬆ  a → aa, and the same on i/u/o/…. Continuation I feel.

᭞᭟  carik siki → carik pareren. One stop, two. Danda again.

᭚ vs ᭽ panti → panti lantang (longer). Size of the same ornament. Pamada twin ᭛᭾.

Ol Chiki ᱾᱿  mucaad → double mucaad.

Digits in all of these: same denoted 0–9.

### last stretch before CJK (1C80–2DFF)

Cyrillic Ext-C, Sundanese Supplement, Georgian Supplement, Glagolitic, Coptic, Tifinagh, Ethiopic Extended, Cyrillic Ext-A.

- **Georgian case as size — medium:** one letter, four faces: ⴀ ა Ა Ⴀ  (nuskhuri, mkhedruli, mtavruli, asomtavruli). I feel ⴀ smaller than Ⴀ; mtavruli is the “small-cap” of mkhedruli. Repeats on every letter.

- **Glagolitic / Coptic case — medium:** Ⰰⰰ  capital → small. Same size-ladder as Latin A a. Coptic Ⲁⲁ the same.

- **Tifinagh extra-mark pairs — medium:** ⴱⴲ  b → bh; ⴷⴸⴹⴺ  d, dh, dd, ddh (marks accumulating on a box); ⵙⵚ  s → ss; ⵣⵥ  z → zz. I can continue “add a stroke/dot.” ⵯ is a small labialization mark (size).

- **Sundanese bindu ᳀᳁᳂** surya / panglong / purnama. Three circles; purnama *means* full. I almost feel a moon-fill, not strongly enough to put it next to 🌑…🌕.

- Ethiopic Extended: more of the same 7-order mutation already noted (ⶠⶡⶢⶣⶤⶥⶦ …).

- Cyrillic Ext-A: combining (small) letters above a base. Size vs the full letter, not a new ladder of their own.

- Coptic ⳽ half; ⳹–⳼ Old Nubian stops — punctuation catalog, not a 1–2–3 I trust from shape.

**CJK Radicals Supplement is next (U+2E80).** Stopping there as asked.

## morphs — one shape becoming another (cross-pane)

Not “more of the same mark.” A continuation I can run even when the axis is “it is turning into that.” Scattered on purpose. Some are a bit silly, like the hinge example. Strength is whether I can take the next step without looking up a name.

### flatten a closer through a stem, then open the other hand

)}|{(

Brace → paren → post → paren → brace. `|` is the hinge. I feel `)` as a flatter `}` and `|` as a `)` that has uncurled completely. Square twin: `]|[`. Chevron twin: `>|<`.

The slightly-silly full palindrome `*-=>})|({<=-*` I can *run* as a story (spike, flatten, double, put a head on it, curl, uncurl through the post, reverse). I would not trust pairwise “which is more?” on `*` vs `}`. The hinge through `|` is the part that is real for me.

A cleaner one-way morph into an arrow, then a curl:

- → } )

Line grows a head, then the head rounds. I feel `- →` strongly; `→ )` as “the wedge got softer.”

### 0d → 1d → 2d

. - □ ■

A point, a span, a face, a filled face. Kin to ∮∯∰ (curve, surface, volume) but in ASCII-adjacent ink. I might also accept `. | □`.

### a stem that thickens, then splits

| ∥ ⦀
❘ ❙ ❚

Already had as count and as weight. The morph is: one post → the post fattens *or* the post becomes two. Two axes from the same starting glyph. `| ∥` and `| ❚` are both continuations; they are not the same line.

### a chevron that rounds, then nests

< ⊂ ⊆ ⋐
< ≪ ⋘
< ⟨ ⟪

Three different next-steps from `<`: round it (`⊂`), double it (`≪`), dress it (`⟨`). I can continue each. They fork; they do not all sit on one scale.

### a line that waves, then the waves stack

- ~ ≈ ≋
‐–—

Straight → wavy → two waves → three. The dash-*length* line is the other fork from `-`.

### a plus that rotates, then sprouts rays

+ × ∗ * ✶ ✹

`+` turned 45° is `×`; more rays is `∗*` then the dingbat stars. I feel `+ × *` as a continuation. Past `*` I am on the star-points ramp already listed.

### a dot that grows a ring, then more rings

. o ⊙ ⊚ ◎ ◯

Point → the point is now a hole → a circle around a dot → more circles. Fork: `. · • ● ⬤` is fill-and-size of a *disk*, not a ring. I would not mix `●` onto the ring line.

### c closes, then opens the other way

c o ɔ

`c` is an `o` that hasn’t met. `ɔ` is the meeting-spot opened on the other side. Closed `o` is the hinge, same job `|` did for the parens.

### a vee that doubles, or that grows into a cup

v w
v ∨ ⋁
n m

`v w` and `n m` are the alphabet’s own tally (already). `v ∨ ⋁` is the same vee becoming an operator then a big operator. Flip `m` and you are near `w`; I feel that as a turn, not as more.

### an angle that closes, then fills

∠ △ ▲
< △

Two strokes meet (`∠` / `<`), a third stroke closes the triangle, then the triangle fills. Small/big was already `▴▲`.

### a triangle that walks around the clock

△ ▷ ▽ ◁

Geometric, not the Canadian letters. I can continue 90° steps. Cycle; “more” needs an origin. Same opening as the Cree vowels, on faces I can actually see here as compass points.

### a bar that grows a second head

- → ↔
← → ↔

One head, the other head. `↔` is `→` with the missing wing, not “stronger than `⇒`.”

### a check that is just a slash, then a slash with a bar

/ √ ✓

I feel `/` becoming the radical and becoming the check as two forks. Weak, a bit silly. `/ ⫽ ⫻` is the serious slash-count line already listed.

### yang that breaks one line at a time — and the break can travel

☰☱☳☷

Already had as dissolve. The morph view: the opening *moves down*. ☲ is the opening in the middle instead — a different path, not “more.” That is why the bagua-as-set failed and the dissolve worked.

### what this pass is for

Most of the pane walk found *accumulation* (more dots, more ink, more nested). This is the other kind: *a shape I can keep deforming*. Pairwise “which is more?” is often the wrong question; “what comes next if I keep doing that to it?” is the right one. The hinge-through-`|` family is the type specimen.

Joseph’s hinge, which names the steps I had only as “flatter”:

>})|({<

Angled → angled-but-more-vertical-with-curve → more-vertical-all-curve → pure-vertical, then the other hand. `> } ) |` is the one-way morph into the stem. A story is enough. So is a progression I cannot name (ink, curve-vs-segment count, some mix). Pairwise “which is more?” is optional.

The join, seen from both sides:

•o⊃)}|{(⊂o•

A point grows an `o`; the `o` opens (`⊃` / `⊂`, the same hinge as `c o ɔ`); then we are already in the closer family and can walk into the stem. Palindrome through `|`. Joseph saw it whole. I had the pieces on separate lines.

A few last morphs, then stopping.

Corners walking around a box — a clock with a square origin:
┌ ┐ ┘ └
⌈ ⌉ ⌋ ⌊
╭ ╮ ╯ ╰

Same continuation as △▷▽◁, different body.

Turnstiles as a T that points:
⊢ ⊤ ⊣ ⊥

Right, up, left, down. I can run it as a clock. `⊤ ⊥` is also just a flip.

`∈ ∋`  `⊂ ⊃`  `∀ ʌ`  membership, horseshoe, turned-A: each a 180° pair. `⊂ ⊃` is already the open `o` in the palindrome.

`6 9`  a turn. Silly and real.

`∇ ∆`  nabla / delta: fill-and-flip of a triangle.

Day-stop. Two kinds in the file: accumulation, and deformation. The hinge `•o⊃)}|{(⊂o•` is where they met. Pre-CJK BMP is walked; U+2E80 not opened.
