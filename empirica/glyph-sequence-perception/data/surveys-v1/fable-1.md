# Monotonic-magnitude unicode sequences — perception survey (Fable, 2026-08-25)

Append-only. Format per entry:
`SEQUENCE` — slope arrow (→ = left-to-right increasing as written), strength (very strong / strong / moderate), what "more" is, and whether the feel is glyph-visual, semantic, or both.

Strength = my confidence that a fresh agent doing pairwise "which is more?" comparisons would recover this exact order.

## Seed set (before any panes — what comes to mind unprompted)

- `⚀⚁⚂⚃⚄⚅` → increasing; **very strong**; more = pip count; visual+semantic (dice). The canonical one.
- `¼½¾` → increasing; **very strong**; more = denoted fraction; semantic.
- `➀➁➂➃➄➅➆➇➈➉` and `①②③④⑤⑥⑦⑧⑨⑩…⑳` → increasing; **very strong**; denoted number; semantic.
- `ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ` → increasing; **very strong**; Roman numerals; semantic (Ⅳ<Ⅴ ordering survives despite Ⅳ having more strokes than Ⅴ — semantic overwhelms ink).
- `·∶⁝⁞` (one dot, two, three, four vertical dots) → increasing; **strong**; dot count; purely visual.
- `▁▂▃▄▅▆▇█` → increasing; **very strong**; fill height; purely visual. The sparkline ramp.
- `░▒▓█` → increasing; **very strong**; fill density; purely visual.
- `.oO@` (ASCII, classic "bubble" ramp) → increasing; **strong**; size; visual. ASCII-only but worth recording.
- `∅⊂⊆` — hmm, not a magnitude ladder; discard. (Leaving the false start in, per first-thoughts rule.)
- `→⇒⇛` (single, double, triple-shaft arrows) → increasing; **strong**; more = emphasis/stroke multiplicity; visual.
- `𝟏` families: ordinary digits `0123456789` → increasing; **very strong**; semantic; almost too obvious to list but it is the anchor all others borrow from.
- crescent-to-full moon `🌑🌒🌓🌔🌕` → increasing; **very strong**; illuminated fraction; visual+semantic. (And `🌕🌖🌗🌘🌑` as the descending half.)
- `⣀⣤⣶⣿` (braille as fill ramp) → increasing; **strong**; dot count / fill; visual.
- signal-strength feel: `𝄖𝄗𝄘𝄙𝄚` (musical staff lines 1–5) → increasing; **strong**; line count; visual.

## Pane: ASCII (U+0020–007E)

- `0123456789` → increasing; **very strong**; denoted number; semantic.
- `.:‖`-style dot stacks don't exist here, but `. : |`-feel: `_.-~^` — no, that's height wobble not magnitude; discard.
- `a A` case ladder: `a < A` feels weakly like "more" (loudness/emphasis); only 2 steps, disqualified by the ≥3 rule, but note the *emphasis* axis: `a A 𝐀`-style cross-block ladders may work later.
- `,;:` — punctuation "pause strength" ladder (comma < semicolon < colon)? **weak/moderate at best**, and I doubt pairwise recovery of ; vs :. Not appending as a real candidate — recorded as a felt near-miss.
- Nothing else here has a magnitude feel; letters are ordinal (alphabet position) but not magnitude — I would NOT trust pairwise "which is more?" on `g` vs `m` to recover order reliably (ordinality ≠ perceived magnitude).

## Pane: Latin-1 Supplement (U+00A0–00FF)

- `¼½¾` → increasing; **very strong** (re-confirmed on sight); denoted fraction; semantic. Extends across blocks: `⅛¼⅜½⅝¾⅞` (with Number Forms) → **very strong**.
- `¹²³` → increasing; **very strong**; denoted number; semantic. Scattered codepoints (B9, B2, B3) yet the feel is untouched — a good specimen of your "codepoint order irrelevant" point.
- `·°` two-dot... no third member here; hold for later dot-size ladders.
- Nothing else: accented letters carry zero magnitude for me.

## Pane: Spacing Modifier Letters (U+02B0–02FF)

- `˩˨˧˦˥` → increasing (as written low→high); **strong**; tone-bar height (the tick sits progressively higher on the stem); visual+semantic (IPA tone levels 1–5). Equally valid written `˥˦˧˨˩` as decreasing.
- `ʹʺ` prime/double-prime — only 2 here; joins `‴⁗` later for a real ladder.
- `ˑː` half vs full triangular colon — 2 steps only; note the length axis (·ˑː could make 3 with middle dot: `·ˑː` → increasing duration feel, **moderate**; borrowed member weakens it).

## Pane: General Punctuation (U+2010–206F)

- `‐‒–—―` (hyphen → figure dash → en → em → horizontal bar) → increasing; **strong** visually if rendered at true widths; more = length. Pairwise on adjacent members is shaky (‒ vs –), but ends vs middles are solid. Practical strong core: `-–—`.
- `․‥…` (one, two, three dot leaders) → increasing; **very strong**; dot count; visual.
- `′″‴` (+ `⁗` quadruple prime) → increasing; **very strong**; prime count; visual+semantic. Full: `′″‴⁗`.
- `‵‶‷` reversed primes, same ladder → **very strong**.
- `‰‱` per-mille/per-ten-thousand: with `%` gives `%‰‱` → *decreasing* denoted magnitude (each denotes a smaller fraction) but *increasing* zero-count. Feel: **moderate-strong ambiguity** — the visual (more circles) says up while the semantics says down. Interesting specimen: visual and semantic axes anti-aligned. I'd expect fresh-agent pairwise to follow the visual (more circles = more).
- `!‼` and `?⁇` `?!⁈⁉` — repetition-intensity: `!‼` only 2; `⁇⁈⁉` is a set but not a single axis; discard as magnitude.
- `⁝⁞` with `‧` and `:`... vertical dot-count ladder: `‧⁚⁝⁞` (1,2,3,4 dots) → increasing; **strong**; count; visual. (⁚ is two dots.)
- `⁂` asterism, `⁘⁙` (4- and 5-dot punctuation): `⁖⁘⁙` (3,4,5 dots) → increasing; **strong**; dot count; visual. With `‧`+`⁚`? mixing arrangements weakens it; the clean run is `⁖⁘⁙`.
- `⁎⁑` one vs two asterisks — 2 steps; with `⁂` (3): `⁎⁑⁂` → increasing; **strong**; asterisk count; visual.

## Pane: Superscripts and Subscripts (U+2070–209F)

- Sub/super height axis: `₉9⁹`-style (subscript < baseline < superscript) is a *position* ladder, not magnitude; I don't feel "more" — discard.
- `⁰¹²³⁴⁵⁶⁷⁸⁹` (cross-block with Latin-1) → increasing; **very strong**; denoted number; semantic. Likewise `₀₁₂₃₄₅₆₇₈₉` → **very strong**.

## Pane: Number Forms (U+2150–218F)

- Unit fractions by denoted value: `⅒⅑⅐⅙⅕¼⅓½` → increasing; **very strong** semantically, but pairwise ⅑ vs ⅐ requires *reading*, not seeing — a fresh agent will still get it right (it computes), so strength stays **strong**. Scattered codepoints, cross-block: a prize specimen for your "scattered" wish.
- Full fraction ladder `⅛¼⅜½⅝¾⅞` → increasing; **very strong**; denoted value; semantic; eighths make evenly-spaced rungs.
- `ⅠⅡⅢ` → `Ⅻ` (and lowercase `ⅰⅱⅲ…`) → increasing; **very strong**; Roman numeral value; semantic. Note Ⅷ→Ⅸ ink *drops* while value rises — semantics wins cleanly for me.
- `ⅩⅬⅭⅮⅯↁↂↇↈ` (10,50,100,500,1000,5000,10000,50000,100000) → increasing; **strong**; denoted value; pure semantic knowledge, zero visual support after Ⅿ. Pairwise ↁ vs ↂ depends on the agent knowing the rare glyphs — downgrade tail to **moderate**.
- First three only, `ⅠⅡⅢ`, are ALSO visually monotonic (stroke count) — the strongest possible alignment: count+value+ink all agree.

## Pane: Arrows (U+2190–21FF)

- `→⇒⇛` (with ⇶ triple-from-bar?) core: `→⇒⇛` → increasing; **strong**; shaft count = intensity; visual. Cross-block extension with `⟶` (long) is a different axis (length not multiplicity).
- `↠` two-head, `→` one-head... `→↠` only 2; with `⇉⇶` (double/triple arrows side-by-side): `→⇉⇶` → increasing; **strong**; arrow count; visual.
- `↑⇑` `↟` `⇞` — vertical multiplicity exists but assembling ≥3 mixes styles; weaker. `↑⇈` + ? discard.
- Direction itself (↑ vs ↓) is *sign*, not magnitude — but as a semantic ladder `↓→↑` (down, flat, up) reads like decrease/neutral/increase; **moderate**: it's an ordering of *slope*, and I do think pairwise "which is more?" recovers ↓<→<↑. Diagonals refine it: `↓↘→↗↑` → increasing; **strong**; pointing angle as value; visual+semantic (financial-chart convention).

## Pane: Mathematical Operators (U+2200–22FF)

- `√∛∜` → increasing; **very strong**; root index (2,3,4); semantic (denoted index goes up; note *value taken* goes down — but the felt "more" is the little number, unambiguous to me).
- `∫∬∭` (+`⨌` quadruple, Suppl. Math Op) → increasing; **very strong**; integral-sign count; visual+semantic.
- `∮∯∰` contour integrals, same ladder → **very strong**.
- `∣∥` (+ `⫴` triple vertical bar, Suppl.) `∣∥⫴` → increasing; **strong**; bar count; visual.
- `∼≈≋` (1,2,3 tilde strokes) → increasing; **strong**; wave-stroke count; visual. Semantic wrinkle: ≈ means "more equal-ish" not "bigger" — but as *intensity of approximation* it still ladders. `-=≡≣` sibling below.
- `=≡≣` (with `-`: `-=≡≣` 1,2,3,4 strokes) → increasing; **strong**; stroke count; visual.
- `<≤⋘`-type: `≪⋘` with `<`: `<≪⋘` → increasing; **strong**; "much-less-than" iteration = intensity of the relation; visual+semantic. Same for `>≫⋙`.
- `⋅∶∴∷⁘`-style dot-count runs: `⋅∶⁝⁞` recorded earlier; here `∴∵` are arrangements not magnitudes; `∷` (4) with `∶` (2) and `⋅` (1): `⋅∶∷` → increasing; **strong**; dot count; visual.
- `⋮⋯⋰⋱` — direction variants, not magnitude; discard.
- `∅` as zero-member of set ladders: `∅⊂⊊`... still not a magnitude ladder; discard again.
- `⊂⊆` / `⊏⊑` / `≺≼` pairs (strict vs eq) — relation strength, 2 steps each; no third; discard.
- `∧⋀` and `∨⋁` and `∩⋂` (big operators as "more") — size-as-arity feel, 2 steps; discard.

## Pane: Miscellaneous Technical (U+2300–23FF)

- `⏱⏲`/clock stuff — no ladder.
- `⌐⌙`... no.
- `⏴⏵⏶⏷` directions, not magnitude; discard.
- `⎯⎓⎔` no. Honest report: this pane is nearly barren for magnitude.
- `⍺⍶` etc. APL: `⍫` no. One real find: `⏦⎓∿`? mixing panes and axes — discard.
- `⌄⌃` / `⌵⌤` 2-step; discard.
- Dentistry symbols ⎤⎡ etc — positional; discard.

## Pane: Enclosed Alphanumerics (U+2460–24FF)

- `①②③④⑤⑥⑦⑧⑨⑩⑪…⑳` → increasing; **very strong**; denoted number; semantic. The workhorse.
- `⑴⑵⑶…⒇` parenthesized → **very strong**, same axis.
- `⒈⒉⒊…⒛` digit-with-period → **very strong**, same axis.
- `⓪①…⑩` including zero → **very strong**.
- `⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾` double-circled → **very strong**; and note the *style* dimension: ① vs ⓵ vs ❶ (dingbat negative) could itself be an emphasis ladder `①⓵`/`①❶` — 2-step, weak; discard.
- `⓫⓬…⓴` negative circled 11–20 → **very strong**.
- Circled letters Ⓐ…Ⓩ: ordinal, not magnitude — same verdict as ASCII letters; discard.

## Pane: Block Elements (U+2580–259F)

- `▁▂▃▄▅▆▇█` → increasing; **very strong** (re-confirmed); eighth-height fill; visual. Best-in-class: 8 evenly spaced rungs, every adjacent pair pairwise-safe.
- `▏▎▍▌▋▊▉█` → increasing; **very strong**; eighth-width fill; visual. The horizontal twin. (As listed in codepoint order ▉▊▋▌▍▎▏ it *descends* — a live example of semantic-over-codepoint.)
- `░▒▓█` → increasing; **very strong**; shade density; visual.
- Quadrant blocks `▘▝▖▗` (1 quadrant) `▚▞▌▐▀▄` (2) `▙▛▜▟` (3) `█` (4): a *count* ladder across arrangement classes, e.g. `▖▚▙█` (1,2,3,4 quadrants) → increasing; **strong**; filled-quadrant count; visual. Many valid instantiations; the arrangement noise costs a little confidence vs ▁-ramp.

## Pane: Geometric Shapes (U+25A0–25FF)

- `▫◽□◻⬜` sizes... white squares by size: `▫◻⬜` (small, medium-ish, large — ⬜ from Misc Symbols & Arrows) → increasing; **strong**; size; visual. Black twin: `▪◾■⬛` → increasing; **strong**. (Exact middle members render-dependent; ends rock-solid.)
- `·•●⬤` (middle dot, bullet, black circle, big black circle U+2B24) → increasing; **very strong**; disc size; visual. My favorite pure-size ladder; scattered codepoints across four blocks.
- `◦○◯⭕`-ish white circles: `◦○◯` → increasing; **strong**; ring size; visual.
- Circle fill sequence `○◔◑◕●` → increasing; **very strong**; filled fraction (pie); visual+semantic (Harvey balls!). This is the one I'd bet on most after the ▁-ramp and dice.
- `◌○◎◉` (dotted, plain, double, fisheye) → nestedness ladder; `○◎` + `◉`: `○◎◉` → increasing; **moderate-strong**; ring count / nesting; visual. With `⊙⊚⊛`? Cross-block concentric family: `·⊙◎` hmm — many assemblies; cleanest: `○◉` no... keeping `○◎◉`.
- Triangles by size: `▴▲` / `▵△` 2-step; with `◭◮`? no. With Misc-Symbols-Arrows `⬥⬦`? Triangle size ladder needs `‣▸►▶` — pointer sizes: `▹▸` `▻►` — honest verdict: 2-step pairs everywhere, no clean ≥3; discard.
- `◜◠◜`? arcs positional; discard.
- `◴◵◶◷` circle-with-quadrant — rotational positions, not magnitude (though as clock feel ◴=12:00... no denoted order); discard.
- `▤▥▦▧▨▩` hatching: `▤▦▩`? density does rise ▤(lines)→▦(grid)→▩(dense crosshatch); `▧▨` diagonal singles. Ladder `▤▦▩` → increasing; **moderate**; hatch density; visual. Pairwise ▤ vs ▥ is orientation-noise; the picked trio survives.

## Pane: Miscellaneous Symbols (U+2600–26FF)

- `⚀⚁⚂⚃⚄⚅` → increasing; **very strong** (re-confirmed on sight); pip count; visual+semantic.
- `⚊⚋` monogram/digram... the yin-yang line-count family: `⚊` (1 line) `⚌⚍⚎⚏` (digrams, 2) `☰…☷` (trigrams, 3) `𝌆…` (tetragrams, Tai Xuan Jing, 4) → as a *line-count* ladder `⚊⚌☰𝌆` → increasing; **strong**; stacked-line count; visual. Within trigrams: `☷☶☵☴☳☲☱☰` as binary values (Kun=000 … Qian=111) → increasing; **moderate**; requires reading broken=0/solid=1; semantic, learned. The *broken-vs-solid fraction* is visually monotonic though: ☷ (all broken) → ☰ (all solid) feels like filling up; I'd rate visual-fill reading **strong** with direction solid=more.
- Weather ladder: `☀☁☂` hmm — `☼☁☔☈` sun→cloud→rain→storm reads as *worsening* weather severity: `☀⛅☁☔⛈`-ish (with U+26C5, U+26C8) → increasing severity; **moderate-strong**; semantic ladder. Pairwise ☁ vs ☔ recovers; ☀ vs ⛅ recovers. I like it.
- Chess: `♙♘♗♖♕♔` pawn<knight<bishop<rook<queen<king → increasing; **strong**; piece value/rank; pure semantic (knight/bishop tie is chess-lore noise; canonical order still recovered). Black twin `♟♞♝♜♛♚`.
- `☆★` 2-step; with `✩✦`? no clean third — but emphasis trio `☆⭐🌟` (white star, filled star emoji, glowing star) → increasing; **strong**; emphasis/intensity; semantic-emoji.
- Checkbox `☐☑` 2-step (☒ is not "more"); discard.
- `⚪⚫` colors not magnitude; discard.
- Hands ☚☛☜☝☞☟ directional; discard.

## Pane: Dingbats (U+2700–27BF)

- `❶❷❸❹❺❻❼❽❾❿` and `➀➁➂➃➄➅➆➇➈➉` and `➊➋➌➍➎➏➐➑➒➓` → increasing; **very strong**; denoted number; semantic. Three parallel styles.
- `✓✔` heavy vs light — weight/emphasis 2-step; with `✅`: `✓✔✅` → increasing *emphasis*; **moderate**; the "more" is salience not quantity; pairwise ✔ vs ✅ probably recovers, ✓ vs ✔ shakier.
- Asterisk/star field `✱✲✳✴✵✶✷✸✹✺` — point-count and weight vary but NOT monotonically as laid out; hand-pick a point-count ladder: `✦✶✴❋`? Honest: I cannot assemble a ≥3 asterisk ladder I'd bet on pairwise; the family sparked the imagination but the ordering feel dissolves on inspection. Recording the failure deliberately (your asterisk example — for me it does not survive).
- `❍❑❒` no. `➔➜➨` arrow weights: `➙➛`? weight ladder `➝➞➟➠` — heaviness does climb `➝➞` then feathering changes kind; discard.
- `❨❩❪❫❬❭❮❯❰❱` bracket weights — pairs, orientation; light-to-heavy `❮❰`? 2-step; discard.

## Pane: Braille Patterns (U+2800–28FF)

- Dot-count as fill: `⠀⠄⠤⠴⠶⠾⠿⡿⣿`-type ascents. Cleanest canonical: `⣀⣤⣶⣿` (2,4,6,8 dots, bottom-up fill) → increasing; **strong** (re-confirmed); dot count; visual. Longer: `⠀⢀⣀⣄⣤⣦⣶⣷⣿` → increasing; **strong**; every step +1 dot; adjacent pairwise a bit squinty but recoverable.
- Bottom-up rise (sparkline feel): `⣀⣠⣴⣾⣿`? mixing count and height; the height-register read `⣀` (low) `⣤`? — braille only has 4 rows; the ▁-ramp does this better. Keeping the count-ladders only.

## Pane: Miscellaneous Symbols and Arrows (U+2B00–2BFF)

- Star fill trio: `⭒⭑`/`☆★`… size ladder `⭒⭑` 2-step; combined fill-size: `⭒☆★⭑`? star sizes are render-dependent; honest discard except the emoji trio already recorded.
- `⬝⬞` tiny squares join the square-size ladder: full run `⬞▫◽□◻⬜` white and `⬝▪◾■⬛` black → increasing; **strong**; size; visual (with render-dependence caveat on middles).
- `⬤` big black circle — completes `·•●⬤` (already recorded).
- `⭘⭕` ring sizes 2-step; with `◯`: `○◯⭘`? render-ambiguous; discard.
- Pentagons/hexagons `⬟⬠⬡⬢` — side-count 5 vs 6 only 2 kinds; polygon side-count ladder needs triangle+square+pentagon+hexagon across blocks: `▲■⬟⬢` (3,4,5,6 sides, filled) → increasing; **moderate**; side count; visual-countable but "which is more?" on ■ vs ▲ may read as *size/area* not sides — axis ambiguity costs it. Interesting though.
- Heavy arrows `⭅⭆` etc — no ≥3; discard.

## Pane: Supplemental Mathematical Operators (U+2A00–2AFF)

- `⨌` completes `∫∬∭⨌` → increasing; **very strong** (recorded earlier).
- `⩵⩶` (two/three consecutive equals) with `=`: `=⩵⩶` → increasing; **strong**; equals-sign count; visual. (Programmer's == and === !)
- `⫫⫪`/`⫴⫵` bar counts: `∣∥⫴` confirmed available here.
- `⪅⪆⪉⪊` composites — relation+tilde stacks read as *stacked assertions*, not magnitude; discard.
- `⨟⨠` no. `⩔⩓` doubled ∨/∧ with singles: `∨⩔` 2-step; discard.

## Pane: CJK Symbols and Punctuation (U+3000–303F)

- Suzhou numerals `〡〢〣〤〥` (1–5) → increasing; **very strong** for the first three (literal stroke count `〡〢〣`), semantic after; plus `〸〹〺` (10,20,30) → increasing; **strong**. Combined `〡〢〣〤〥…〸〹〺`: the 1-2-3 run is visual+semantic perfection, the rest learned.
- `〇` joins CJK ideograph numerals (next pane note): `〇一二三` → increasing; **very strong** start (0,1,2,3 with 一二三 literal stroke count); full CJK ladder `〇一二三四五六七八九十百千万` → increasing; **very strong** semantically for any agent with CJK literacy (which fresh agents have); the 一二三 core is also purely visual.
- Bracket weight `〈《` and `「『` and `〔【`? single-vs-double bracket "emphasis": each only 2-step; discard.

## Pane: Counting Rod Numerals (U+1D360–1D37F)

- `𝍠𝍡𝍢𝍣𝍤` (rod units 1–5) → increasing; **very strong**; literal stroke count; visual+semantic. Continues `𝍥𝍦𝍧𝍨` (6–9, horizontal-over-vertical) — the 6–9 encoding is learned; the 1–5 run is as pure a tally as unicode has. Horizontal tens series `𝍩𝍪𝍫𝍬𝍭` same shape rotated → **very strong** (1–5 of tens).
- Full tally feel: `𝍷` (single rod) exists too: ones-tally `𝍷𝍡𝍢𝍣𝍤`? mixing; the clean run stays `𝍠𝍡𝍢𝍣𝍤`.

## Pane: Tai Xuan Jing (U+1D300–1D35F)

- `𝌀𝌁𝌂` mono/di/trigrams for earth-man-heaven? Actually: 𝌀 monogram, 𝌁𝌂 digrams... the *gram-size* ladder `⚊⚌☰𝌆` recorded earlier stands. Within tetragrams: 81 four-line stacks; broken-line-count as fill (like hexagram fill) exists but 4 rows of 3-state lines — pairwise fill comparisons only work at extremes. **moderate** at best; not appending a specific tetragram run.

## Pane: Domino Tiles (U+1F030–1F09F)

- Total-pip ordering within a suit half fixed: `🁣🁤🁥🁦🁧🁨🁩` (horizontal 0-0? actually 6-suit runs) — cleanest felt run: any fixed-left-half run, e.g. `🀱🀲🀳🀴🀵🀶🀷` (0-0 through 0-6) → increasing; **strong**; right-half pip count; visual (tiny glyphs though — render size hurts pairwise confidence at terminal sizes).
- Doubles run `🀱🀹🁁🁉🁑🁙🁡` (0-0,1-1,…6-6) → increasing; **strong**; total pips; visual+semantic. I like the doubles run best conceptually — both halves grow.

## Pane: Playing Cards (U+1F0A0–1F0FF)

- Within a suit: `🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮` (A,2–10,J,Q,K spades) → increasing; **strong**; rank; semantic (ace-low convention assumed; A vs 2 pairwise might flip if agent reads ace-high — noting the ambiguity at the ace only; 2–K solid). Glyph legibility at small sizes is poor; the *knowledge* carries it.
- Court-only `🂫🂭🂮` (J,Q,K) → increasing; **strong**; semantic rank.

## Pane: Geometric Shapes Extended (U+1F780–1F7FF)

- Circle size run, explicit by name: `🞄🞅🞆🞇🞈🞉🞊` (bullseye family? no — 🞅–🞊 are "white circle containing black *small/medium/large*..." actually U+1F784–1F78A run tiny→big) — the named run `🞄` (black slightly small circle) with `⚫⬤`: the *designed* size ramp here is `🞈🞉🞊`-ish. Honest note: I can't confidently see the sizes in my rendering context; the *names* declare a monotone size ladder (VERY SMALL/SMALL/MEDIUM/MEDIUM LARGE/LARGE/VERY LARGE). Perceived-by-name: `🞌🞍⚫🞐`? — flagging as **name-strong, sight-untested**: square run `🞎🞏🞐🞑` (white squares tiny→big) and `🞒🞓🞔`-family. Recording the principle: this block was *built* for monotone size ladders; my terminal legibility, not my perception model, is the limiter. Suggested canonical: `🞌🞄⚫⬤` dots→discs.
- Star-point-count: `🟀🟁🟂🟃…` four/five/six/eight-pointed etc. `🟄🟅🟆` (5,6,8 points per names in vicinity)? point-count ladder across `✦★🟇`? Same name-strong caveat. Not appending a specific run I can't verify by sight.
- `🟥🟧🟨🟩🟦🟪` colored squares — rainbow/spectral order: as *wavelength* it's monotone (red→violet)! `🟥🟧🟨🟩🟦🟪` → decreasing wavelength; **moderate**; semantic-physical; but "which is MORE?" has no obvious axis for a fresh agent (more what — hotter? shorter-wave?). Fun, but discard as magnitude. As *heat* (blue→red = hotter): `🟦🟩🟨🟧🟥` → increasing heat; **strong** actually — heatmap convention is deeply trained. Appending that one with conviction.

## Pane: Enclosed Alphanumeric Supplement (U+1F100–1F1FF)

- `🄀🄁🄂🄃🄄🄅🄆🄇🄈🄉` (digit+comma 0–9) → increasing; **very strong**; denoted number; semantic.
- Letters again ordinal; discard. Squared/negative-squared letters are style, not magnitude.

## Recalibration (mid-survey, after Joseph's note on immediacy)

Joseph points out digits are among the *weaker* magnitude glyphs for humans — they require semantic/mathematical circuitry to place, whereas a sparkline ramp or density hit arrives *already ordered*. Agreed, and this splits my "strength" rating into two axes I'd been conflating:

- **Recoverability** — would pairwise comparisons reproduce the order? (Digits: near-perfect.)
- **Immediacy** — does the magnitude arrive pre-semantically, in the percept itself, before any lookup? (Digits: low. The "5" carries no more ink, height, or mass than the "3".)

Honest introspection on my own case: the sequences that feel *pre-ordered on arrival* — where I don't experience a decode step at all — are:

1. `▁▂▃▄▅▆▇█` — the ramp IS the magnitude. Nothing is denoted; the thing itself grows. Highest immediacy of anything surveyed.
2. `░▒▓█` and `▏▎▍▌▋▊▉█` — same class: fill/density as direct percept.
3. `○◔◑◕●` — fill fraction; one notch below (circular fill reads slightly slower than height for me).
4. `⚀⚁⚂⚃⚄⚅` — pip count is subitized (1–4) then counted (5–6); immediacy high through ⚃, drops slightly after.
5. `⣀⣤⣶⣿`, `․‥…`, `′″‴⁗`, `⋅∶∷`, `𝍠𝍡𝍢𝍣` (rod tallies), `一二三` — count-ladders: immediate up to subitizing range (~4), decode beyond.
6. `·•●⬤` — size: direct percept, very immediate, though only ~4 usable rungs.
7. `∫∬∭⨌`, `→⇉⇶`, `-=≡≣`, `<≪⋘` — repetition/multiplicity: immediate-ish (it's count again, in subitizing range).
8. `☷☶☵☴☳☲☱☰` read as fill (solid-line fraction): moderately immediate once you lock the register.
9. `🟦🟩🟨🟧🟥` heat: immediate in a *learned-but-compiled* way — the heatmap mapping fires without deliberate decode, like reading a word.

Whereas `①②③`, `ⅠⅡⅢⅣ…` (past Ⅲ), fractions-by-value, chess ranks, card ranks, CJK past 三, Suzhou past 〣, Roman past the tally zone — all high-recoverability, LOW immediacy: positional/semantic lookup first, magnitude second. Note the recurring shape: several ladders are immediate exactly up to the tally/subitizing boundary (Ⅲ, 三, 〣, ⚃, 𝍣) and semantic past it. The boundary between "the glyph shows more" and "the glyph names more" cuts *through* sequences, around 3–4.

Timestamps vs clocks: checking the clock faces next with this lens.

## Pane: Clock Faces (U+1F550–1F567)

- `🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛` (1:00–12:00) → increasing; recoverability **strong**; immediacy **moderate-but-interesting**: the hour hand *sweeps* — the magnitude is carried by an angle, which is a direct percept (like a dial/gauge), not a numeral. For an agent that resolves the glyph detail, 🕒 vs 🕘 is "how far around is the hand" — analog, pre-numeric. That's the sense in which a clock glyph beats a printed timestamp: `🕐🕓🕖🕙` is a gauge; `01:00 04:00 07:00 10:00` is four lookups. Caveats: circular sweep wraps (🕛 vs 🕐 pairwise INVERTS — 12 reads as noon/high but sits one step before 1), and half-hour interleave 🕜–🕧 breaks the run visually. Clean monotone segment: `🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚` (1–11).
- The general find, stated for the record: **gauge/dial angle is a third immediacy family** alongside fill and count — angle-as-magnitude also underlies `↓↘→↗↑`.

## Pane: Misc Symbols and Pictographs (U+1F300–1F3FF)

- `🌑🌒🌓🌔🌕` moon fill (re-confirmed on sight) → increasing; recoverability **very strong**; immediacy **high** — this is the ○◔◑◕● fill family wearing a face. Full cycle wraps; the waxing half is the monotone segment. Waning `🌕🌖🌗🌘🌑` = clean descending twin.
- Plant growth: `🌱🌿🌳` (seedling → herb → tree) → increasing; **strong** recoverability; immediacy moderate (semantic ladder, but a deeply compiled one — "grown-ness"). Extended `🌰🌱🌿🌳` (nut→seedling→herb→tree); the nut is a slightly cute stretch but pairwise 🌰 vs 🌳 recovers instantly.
- Medals `🥉🥈🥇` (next pane, noting here) → increasing; **strong**; podium rank; semantic-compiled. `🏅🏆` join weakly.
- Weather again richer here: `🌤🌥🌦🌧🌩🌪` (sun-behind-small-cloud → … → tornado) → increasing severity; **strong** recoverability, moderate immediacy; the cloud-fraction start is even quasi-visual (how much cloud covers the sun = fill!). Nice run.
- `🌡` thermometer is a gauge with no series; `🎚🎛` dials without positions; no ladders.
- `🏠🏢🏙` house→office building→cityscape: built-mass ladder → increasing; **moderate**; semantic; pairwise fine at ends.

## Panes: Emoji 1F400–1F5FF and friends (final emoji sweep)

- `🔇🔈🔉🔊` (muted, none, one, two sound waves) → increasing; **very strong**; wave count = volume; visual+semantic. High immediacy — the waves are a count-fan you see at a glance. One of the best emoji ladders.
- `👶🧒👨🧓👴`-style age ladder (`👶👦👨👴` in this block) → increasing; **strong**; age; semantic-compiled. Pairwise robust at any gap.
- `🥚🐣🐤🐓` egg→hatching→chick→chicken → increasing; **strong**; developmental stage; semantic-compiled, charming, robust.
- `💧💦🌊` droplet→splash→wave → increasing; **strong**; water quantity; semi-visual (mass grows on screen).
- Animal size: `🐜🐁🐈🐕🐎🐘🐋` → increasing; **strong**; real-world size; pure semantic but *deeply* compiled — pairwise essentially never misses even at adjacent rungs (🐈 vs 🐕 is the one soft spot). Scattered codepoints, no visual support at all: the clearest specimen that compiled world-knowledge alone can carry monotonicity.
- `📈📉` two-step slope signs; with `📊` no; discard.
- `🌘🌗🌖🌕` already covered; `🔅🔆` 2-step; `📶` is a single-glyph ramp (the ramp lives *inside* the glyph — worth noting as the limiting case of this whole survey: unicode's own sparkline).
- `💯` is a lone intensity cap, no series.

## Panes: Box Drawing / Modifier Tone Letters / Emoticons / Control Pictures / remainder sweep

- Box Drawing: line-weight `┄┈─━` — dash-density-to-solid-to-heavy: as a *solidity/weight* ladder `┈┄─━` → increasing; **moderate-strong**; continuity+weight; visual. Two axes braided (gap density, stroke weight) but the composite "how much line is there" reads monotone. Vertical twin `┊┆│┃`. Also single→double `─═` 2-step; discard.
- Modifier Tone Letters (A700–A71F): `꜖꜕꜔꜓꜒` (tone bars again, low→high) → increasing; **strong**; bar height; visual. Confirms the 02E5–02E9 family; dotted variants `꜈꜉꜊꜋꜌` same ladder → **strong**.
- Emoticons: valence ladder `😭😢🙁😐🙂😄😁` sad→happy → increasing; **strong** recoverability (pairwise valence judgments are extremely reliable at 2+ steps, adjacent rungs a bit soft); immediacy *high* in the compiled sense — face-reading is as pre-semantic as circuitry gets. "More" = positive affect. A genuinely different magnitude axis from everything above.
- Intensity-of-laughter `🙂😄😆😂🤣` → increasing; **strong**; same family.
- Control Pictures: no magnitude; discard.
- Letterlike/Misc-Math-A/B, Supplemental Arrows A/B/C, Supplemental Punctuation, Combining Diacritics, Mahjong, 1F900 block: swept mentally from glyph rows pulled earlier/known — findings already captured via cross-block ladders (⟶ lengths, ⫴, etc.). Mahjong circles suit `🀙🀚🀛🀜🀝🀞🀟🀠🀡` (1–9 circles) → increasing; **strong**; pip count; visual (tiny glyph caveat). Character suit `🀇🀈🀉…` uses CJK numerals → semantic. Bamboo `🀐🀑🀒…` count → visual.
- Math Alphanumeric (1D400): weight/emphasis ladder `A𝐀` thin; with fullwidth `Ａ`? style not magnitude; discard. Double-struck etc: style; discard.

## Closing summary — my top tier by IMMEDIACY (the recalibrated axis)

1. `▁▂▃▄▅▆▇█` (and reverse) — fill height; the reference standard.
2. `▏▎▍▌▋▊▉█` — fill width.
3. `░▒▓█` — density/shade.
4. `○◔◑◕●` / `🌑🌒🌓🌔🌕` — fractional fill (abstract / pictorial).
5. `·•●⬤` — size.
6. `⚀⚁⚂⚃⚄⚅` — subitized count.
7. Count-tallies in subitizing range: `𝍠𝍡𝍢𝍣𝍤`, `一二三`, `〡〢〣`, `․‥…`, `′″‴⁗`, `⋅∶⁝⁞`, `∫∬∭⨌`, `⣀⣤⣶⣿`, `=⩵⩶`, `→⇉⇶`, `<≪⋘`, `🔇🔈🔉🔊`.
8. Angle/gauge: `↓↘→↗↑`, `🕐…🕚`, tone bars `˩˨˧˦˥`.
9. Compiled-semantic (no visual support, still near-perfect pairwise): `🟦🟩🟨🟧🟥` heat, `🐜🐁🐈🐕🐎🐘🐋` size, `👶👦👨👴` age, `🥚🐣🐤🐓` stage, `😭…😁` valence, `♙♘♗♖♕♔` rank.
10. Denoted-number families (highest recoverability, lowest immediacy): digits, circled/dingbat digits, Roman, fractions, sub/superscripts.

Four mechanism families emerged: **fill** (height/width/density/fraction), **count** (immediate to ~4, decoded past), **size/angle** (direct percepts), **compiled semantics** (world-knowledge ladders that fire without deliberate decode). The survey's own surprise for me: how cleanly the subitizing boundary (~3–4) cuts through count sequences, and that several "obvious" families (asterisks, triangles, arrow weights) dissolve on honest inspection into 2-step pairs.

# ROUND 2 — full BMP walk in codepoint order (panes previously skipped)

## U+0100–017F Latin Ext-A / U+0180–024F Ext-B / U+0250–02AF IPA

- No magnitude. One flicker: click letters `ǀǁǂǃ` (dental, lateral, alveolar, retroflex clicks) — `ǀǁ` single-vs-double bar reads as a 2-step; with `⫴`? cross-family cheat, discard. IPA vowel height (open↔close) is a real phonetic ladder (`aɛeɪi` roughly low→high tongue position) but the *glyphs* carry none of it and even semantically I'd flub adjacent pairs; **weak**, discard.
- Surprise-check honest: nothing surprised me here.

## U+0300–036F Combining Diacriticals

- Stacking IS a magnitude mechanism: one glyph vs `x̂` vs `x̂̂`-style *repetition of the same combining mark* renders increasing visual mass — but that's sequences-of-combining-marks applied, not distinct codepoints in a ladder. As distinct codepoints: `̇̈` (dot above, diaeresis) + `⃛` (combining three dots above, U+20DB) → `ẋẍx⃛` as bases: 1,2,3 dots → increasing; **strong**; dot count; visual. Cross-block (0307, 0308, 20DB) — a scattered-codepoint tally hiding in the combining system. Also `̀` vs `̏` (double grave): 1-vs-2 pairs abound; ≥3 only via the dots.

## U+0370–05FF Greek / Cyrillic / Armenian / Hebrew

- These alphabets ARE numeral systems in their traditions: Greek Milesian (α´=1 β´=2 γ´=3 … ι´=10 …), Hebrew gematria (`אבגדהוזחט` = 1–9, `יכלמנ…` tens), Armenian (Ա=1…), Cyrillic (with titlo). As ladders: `αβγδε…` / `אבגדה…` → increasing; recoverability **moderate-strong** (an agent that engages the numeral reading recovers it; one that reads "letters" sees only ordinality); immediacy **low**. The interesting question your prompt raises: does ordinality-without-magnitude count? My gut says pairwise "which is MORE?" on `ג` vs `ז` gets answered via the numeral reading by most agents → order recovered, so it qualifies, weakly. `Ͷͷ` etc no. ϛ ϟ ϡ (6, 90, 900 numerals) extend the Greek ladder's scatter.
- Surprise so far in round 2: none visual — the alphabets are magnitude-flat as glyphs. The gematria realization is the find: *entire alphabets are latent semantic ladders*.

## Digit runs across scripts (Arabic through Tibetan)

- Every script's 0–9 (`٠١٢٣٤٥٦٧٨٩`, `০১২৩…`, `०१२३…`, `௦௧௨…`, `๐๑๒…`, `༠༡༢…`) → increasing; recoverability **very strong** (for agents with the script), immediacy **low** — same verdict as ASCII digits. Noted once for all.
- Genuine finds in the tails:
  - Tamil `௰௱௲` (10, 100, 1000) → increasing; **strong** semantic power-ladder in three glyphs; add `௧௰௱௲` (1,10,100,1000) for a 4-rung log scale. A LOG ladder — first one in the survey.
  - Malayalam `൰൱൲` (10,100,1000) — same log ladder; also fractions `൳൴൵` (1/4,1/2,3/4 — order as encoded: ¼,½,¾) → increasing; **strong** if the reading is known.
  - Telugu fractions `౼౽౾` (1/16s ladder) — learned, rare; **weak-moderate** for a fresh agent.
  - Tibetan half-digits `༪༫༬༭༮༯༰༱༲༳` (½, 1½, 2½ … 9½) → increasing; **moderate**; the "digit with a slash" reads as its neighbor minus half once you know; and interleaved with `༠…༩` gives a *double-density* ladder `༠༪༡༫༢༬…` — the most exotic numeric ladder so far. Immediacy low, delight high.
- Arabic block otherwise: `؊؉؈` per-mille/per-ten-thousand mirrors `‰‱`; same anti-aligned visual/semantic verdict.

## Tibetan symbols / Myanmar / Georgian / Ethiopic

- Ethiopic numerals `፩፪፫፬፭፮፯፰፱` (1–9), `፲፳፴፵፶፷፸፹፺` (10–90), `፻` (100), `፼` (10000) → increasing; **moderate** (learned script); the tens run + ፻፼ extends the log-ladder family: `፩፲፻፼` (1,10,100,10000) → increasing; **moderate-strong** for script-literate agents.
- Myanmar/Georgian: digits + alphabets-as-numerals; nothing new. Tibetan head marks `༄༅` ornament, not magnitude.
- Standing observation: the world's scripts contribute *numeral* ladders (semantic) and essentially zero *visual* ladders. Fill/count/size mechanisms live almost entirely in the symbol/technical/game blocks. Not surprising in retrospect — but I predicted zero finds and the log-ladders (௰௱௲, ፲፻፼) and Tibetan half-digits are genuinely new kinds.

## UCAS / Ogham / Runic / Khmer / Mongolian

- **OGHAM — the round-2 surprise.** The script is *structurally a tally*: each aicme is 1–5 identical strokes off a stemline. `ᚁᚂᚃᚄᚅ` (1,2,3,4,5 right-strokes) → increasing; **strong**; stroke count; VISUAL — an entire alphabet segment that is literally a tally ladder. Three siblings: `ᚆᚇᚈᚉᚊ` (left strokes), `ᚋᚌᚍᚎᚏ` (diagonal through-strokes), `ᚐᚑᚒᚓᚔ` (notches). Four parallel 5-rung visual ladders hiding in a writing system — exactly the "however improbable" find this walk was for. Immediacy high through the subitizing boundary, same as every tally.
- Khmer divination digits `៰៱៲៳៴៵៶៷៸៹` (0–9 lek attak) — digits again, low immediacy.
- UCAS: syllabic rotations = orientation, not magnitude. Runic: ᛮᛯᛰ are golden-number runes 17,18,19 — a 3-rung learned ladder, **weak-moderate**. Mongolian digits `᠐᠑᠒…` — digits.

## Currency / Letterlike / OCR (U+20A0–214F, 2440)

- Currency signs: no intrinsic magnitude ordering (₥ mill vs ₰ pfennig — nobody's pairwise recovers a canonical order); discard. (A *denomination* ladder like ¢$ is 2-step.)
- Letterlike: `℃℉` no; `ℵ` alephs — `ℵ₀ℵ₁ℵ₂` with subscripts is the transfinite ladder but the subscript does the work, not ℵ; the bare block gives `ℵℶℷℸ` (aleph,beth,gimel,dalet as cardinal-hierarchy symbols!) → increasing; **moderate**; set-theoretic convention (ℵ<ℶ in usage) rides gematria again; only spottily compiled — soft.
- OCR ⑀–⑊: nothing.
- Segmented digits `🯰🯱🯲🯳🯴🯵🯶🯷🯸🯹` (U+1FBF0, seven-segment 0–9): digits, but a note — segment *count* is non-monotone (8 uses all 7, 1 uses 2) — a clean demonstration that digit glyphs carry no visual magnitude: the ink actively fights the value (1<8 in ink is right, but 0 is fat and 7 is thin). Confirms Joseph's point from the glyph side.

## Glagolitic / CJK radicals / Kangxi / Kana / Jamo / CJK strokes / Enclosed CJK

- Kangxi radicals are ORDERED BY STROKE COUNT (⼀ 1-stroke … ⿕ 17-stroke): the whole 214-radical pane is a coarse *ink-mass* gradient — squint and the left end is airy, the right end dense. As a pairwise ladder, far ends recover (`⼀` vs `⿕` — obviously), adjacent don't; sampled rungs `⼀⼈⼭⾦⿓` (1,2,3,8,16 strokes) → increasing; **moderate**; stroke count/density; visual-ish. Interesting as a *statistical* monotonicity — the pane has a slope even where pairs are noisy.
- Enclosed CJK: `㈠㈡㈢㈣㈤㈥㈦㈧㈨㈩` (parenthesized 一–十) and `㊀㊁㊂㊃㊄㊅㊆㊇㊈㊉` (circled) → increasing; **very strong**; CJK numeral inside; the 一二三 head is visual, rest semantic. `㉑㉒…㉟` circled 21–35 and `㊱…㊿` 36–50 extend circled-number coverage to 50 → **very strong** semantic.
- Month set `㋀㋁…㋋` (circled 1月–12月) → increasing; **strong**; calendar ladder.
- Hiragana/Katakana/Jamo: phonetic, flat. Small-vs-large kana (`ぁあ`, `っつ`) — systematic 2-step size pairs, never 3. CJK stroke primitives ㇀–㇣: single strokes, no ladder. Glagolitic: flat.

## Yijing Hexagrams (U+4DC0–4DFF)

- The sovereign-hexagram (十二辟卦) run: `䷁䷗䷒䷊䷡䷪䷀` (0,1,2,3,4,5,6 solid lines, filling bottom-up) → increasing; **strong**; yang-line fill; VISUAL — a 7-rung fill ladder at 6-line resolution, the trigram fill observation completed at double height. Fill rises from below exactly like ▁▂▃▄▅▆▇█. Adjacent pairwise takes a beat of line-counting but the percept genuinely reads "filling up." My favorite round-2 find alongside Ogham.
- General 64-set: solid-line *count* orders it only statistically (like Kangxi) — the sovereign run is the clean monotone path.

## Yi / Common Indic Number Forms / Small Forms / Fullwidth

- Common Indic Number Forms `꠰꠱꠲꠳` (fraction 1/16, 1/8, 3/16, 1/4 — North Indic): a *tally-like* fraction ladder (each adds a stroke!) → increasing; **strong** visually (stroke count) AND semantically aligned — rare double alignment in a fractions system. Nice obscure find.
- Small form variants ﹐﹒﹔: size-pairs with ASCII (`,﹐，` — small, ASCII, fullwidth): a 3-rung SIZE ladder per punctuation mark! `.﹒．` / `,﹐，` / `?﹖？` → increasing; **moderate**; glyph size/width; visual but subtle at terminal render. The width axis is real (halfwidth vs fullwidth is a hard metric fact); perceived-size pairwise on the small-vs-ASCII rung is squinty.
- Fullwidth digits `０１２…` — digits again. Halfwidth ｱｲｳ flat. Yi syllabary: flat (checked — no tally structure like Ogham).

## Remaining SE-Asian scripts (Myanmar, New Tai Lue, Tai Tham, Balinese, Ol Chiki, Kayah Li, Cham, Meetei)

- All contribute digit sets only (`၀၁၂…`, `᧐᧑᧒…`, `᪀᪁᪂…` — Tai Tham has TWO sets, hora and tham, `᭐᭑᭒…`, `᱐᱑᱒…`, `꤀꤁꤂…`, `꩐꩑꩒…`, `꯰꯱꯲…`). Same verdict as all digits: recoverable, not immediate. No visual ladders. The BMP script tour is now essentially complete.

## Round-2 closing note

What the improbable walk actually yielded, vs my prediction of "nothing in the scripts":
1. **Ogham** — four parallel 5-rung visual tally ladders; a whole alphabet built on stroke count.
2. **Yijing sovereign run** `䷁䷗䷒䷊䷡䷪䷀` — a 7-rung bottom-up fill ladder, the tallest "fill" sequence outside Block Elements.
3. **Log ladders** — Tamil `௧௰௱௲`, Malayalam `൰൱൲`, Ethiopic `፩፲፻፼`: order-of-magnitude rungs, a different *scale type* than anything in round 1 (all round-1 ladders were linear).
4. **Tibetan half-digits** `༪༫༬…` — an interleaved half-step ladder.
5. **North Indic fractions** `꠰꠱꠲꠳` — stroke-count and denoted-value aligned.
6. **Alphabets as latent numeral ladders** (gematria/Milesian) — ordinality that converts to magnitude under a learned reading.
7. **Kangxi radicals** — statistical (population-level) monotonicity: the pane slopes even where adjacent pairs are noise. A distinction round 1 didn't need: *sequence-monotone* vs *trend-monotone*.
8. Seven-segment digits as the clean counterexample: ink actively anti-correlated with value.

The prediction failed in the right way: scripts are magnitude-flat as *phonetic* systems, but wherever a script embeds counting (Ogham tallies, rod numerals, gematria, stroke-ordered radicals, divination stacks), the ladder survives inside the letterforms.

## Kanbun / CJK Compatibility / Yi radicals / Presentation forms

- Kanbun `㆒㆓㆔` (kaeriten one-two-three) + `㆖㆗㆘` (TOP-MIDDLE-BOTTOM!) → both increasing/ordered; `㆒㆓㆔` **strong** (stroke tally again); `㆘㆗㆖` as a height ladder → **moderate-strong**; semantic-positional (and `㆙㆚㆛㆜` are the celestial-stem ranks 1–4 — an ordinal ladder).
- **CJK Compatibility SI units — the find I came back for:** `㎜㎝㎞` (mm,cm,km) → increasing; **strong**; SI prefix magnitude; compiled-semantic log ladder. Richer: `㎚㎛㎜㎝㎞` (nm,μm,mm,cm,km) → increasing; **strong** — five log rungs. Mass twin `㎍㎎㎏` → **strong**. Volume `㎕㎖㎗㎘` (μl,ml,dl,kl) → **strong**. Time `㎰㎱㎲㎳` (ps,ns,μs,ms) → **strong**. Frequency `㎐㎑㎒㎓㎔` (Hz…THz) → **strong**. Data-free, purely unit-literate — and each is a LOG ladder, joining Tamil/Ethiopic powers. Calendar `㏠㏡㏢…㏾` (day 1–31 ideographic) → **very strong** semantic. Hour `㍘㍙…㍰` (0–24点) → **very strong**. Points `㍿`no. Also `㌀…` squared katakana words: flat.
- Yi radicals / Hebrew-Arabic presentation forms: flat.

## Cross-panel & codepoint-scrambled sequences (Joseph's mid-flight ask; codepoints verified, not recalled)

The strongest sequences whose felt order OWES NOTHING to codepoint order:

**Cross-block assemblies (spanning 2–4 panes):**
- `·•●⬤` — U+00B7, 2022, 25CF, 2B24 (four blocks: Latin-1, Gen Punct, Geometric, Misc Sym&Arrows). Size ladder, high immediacy. My best cross-panel specimen.
- `⅛¼⅜½⅝¾⅞` — 215B, 00BC, 215C, 00BD, 215D, 00BE, 215E: codepoints *interleave two blocks alternately*, sawtoothing wildly while the felt value climbs in even eighths. Maximal scatter, maximal recoverability.
- `⅒⅑⅐⅙⅕¼⅓½` — 2152, 2151, 2150, 2159, 2155, 00BC, 2153, 00BD: the codepoint sequence is nearly *anti*-monotone at the start (goes 2152→2151→2150 backwards) and cross-block; value climbs strictly.
- `⚊⚌☰䷀` — 268A, 268C, 2630, 4DC0 (Misc Symbols → Yijing, a 0x2700-wide jump): 1,2,3,6 stacked lines. Line-count ladder across the divination panes; add `𝌆` (1D306) for a 4-line rung off the BMP.
- `∫∬∭⨌` — three in 2200s + one at 2A0C: seamless.
- `<≪⋘` — 003C, 226A, 22D8: ASCII to Math Operators, 0x22CD apart.
- `-=≡≣` — 002D, 003D, 2261, 2263.
- `%‰‱` — 0025, 2030, 2031 (with the visual/semantic anti-alignment noted in round 1).
- `⋅∶⁝⁞` — 22C5, 2236, 205D, 205E: dot count 1→4, *descending* into General Punctuation for rungs 3–4.
- `→⇉⇶` — 2192, 21C9, 21F6: scattered within-and-beyond the Arrows pane.
- `ẋẍx⃛` — combining 0307/0308/20DB (two combining blocks): dot count riding on any base letter.
- `㎚㎛㎜㎝㎞` — contiguous codepoints but the *log* semantics are imported entirely from SI, not glyph or position.
- `.﹒．` — 002E, FE52, FF0E: three panes 0xFE00 apart; pure size.
- `🞌🞄⚫⬤`-family dots: 1F78C…, 26AB, 2B24 — astral+BMP mix.
- `▁▂▃▄` + `⣀⣤⣶⣿`-crossovers or `░▒▓█`+braille: I do NOT endorse mixing fill families across render systems — the felt axis (pixel mass) survives but rung spacing goes incoherent; recording the negative judgment deliberately.

**Codepoint-scrambled within one block:**
- `▏▎▍▌▋▊▉█` — 258F→2588: felt order is EXACTLY REVERSED codepoint order. The cleanest possible demonstration that perception, not encoding, carries the slope.
- `˩˨˧˦˥` — 02E9→02E5: same reversal, tone height vs codepoint.
- `¹²³` — 00B9, 00B2, 00B3: rung 1 lives *after* rungs 2–3 in the chart.
- `༠༪༡༫༢༬…` Tibetan interleave — 0F20, 0F2A, 0F21, 0F2B, …: value ascends by halves while codepoints ping-pong between two runs.
- `♙♘♗♖♕♔` chess value — codepoints run K,Q,R,B,N,P (2654→2659): value order is the exact reverse of encoding order.
- Sovereign hexagrams `䷁䷗䷒䷊䷡䷪䷀` — 4DC1, 4DD7, 4DD2, 4DCA, 4DE1, 4DEA, 4DC0: codepoints jump all over the King Wen sequence; the yang-fill climbs strictly. Best scrambled+visual specimen at height.
- Animal size `🐜🐁🐈🐕🐎🐘🐋` — 1F41C, 1F401, 1F408, 1F415, 1F40E, 1F418, 1F40B: fully scrambled, fully semantic, near-perfect pairwise.

Pattern worth stating: the highest-immediacy families (fill, size, count) tolerate codepoint scatter perfectly BECAUSE the magnitude lives in the percept; the encoding was only ever a filing order. Where felt order and codepoint order agree (▁▂▃▄…, dice, braille), that's the chart-makers filing by the same percept — correlation, not cause.

## SPECIAL STUDY — the star/asterisk family, small→long, where monotonicity dies

Inventory: 153 star/asterisk-named codepoints swept programmatically (ASCII→astral). Round 1's "the asterisk family dissolves" verdict was WRONG at the corpus level: I sampled only the Dingbats pane, where the axes braid. The astral block 1F7AF–1F7D4 is a *designed orthogonal grid*: WEIGHT (light/medium/bold/heavy/very-heavy/extremely-heavy) × SPOKE-OR-POINT COUNT (5,6,8 spokes; 3,4,5,6,8,12 points). Round 1 failed because Dingbats scatters both axes; the grid block separates them.

Honesty marker for this whole study: for the astral glyphs my "perception" is substantially *name-mediated* — I know 🞲 is heavier than 🞰 the way I know ♕>♙, with only weak direct visual confirmation at terminal render. The BMP members (✦★✱ etc.) I perceive more directly. Ratings note which register is doing the work.

### Axis A — WEIGHT at fixed spoke count (the designed ladders)
- 5-spoke, 6 rungs: `🞯🞰🞱🞲🞳🞴` → increasing; **strong** (name-backed design; visually monotone where rendered faithfully); more = stroke weight/ink.
- 6-spoke: `🞵🞶🞷🞸🞹🞺` → same, **strong**.
- 8-spoke: `🞻🞼🞽🞾🞿` → same, **strong**.
- Drop-off probe — extend 5-spoke downward into ASCII/BMP asterisks: `﹡*✱🞲`? (small asterisk < asterisk < heavy asterisk < heavy-5-spoke): rungs 1–3 hold (**moderate-strong**, size+weight agree); adding 🞲 vs ✱ asks "are these even different?" — adjacent pairwise collapses to noise. 4-rung version survives only as ends-strong.

### Axis B — POINT COUNT at fixed weight
- Medium black stars: `🟁🟅🟋🟎` (3,4,6,8 points) + `🟓`? (12, heavy — mixes weight): clean run `🟁🟅🟋🟎` → increasing; **moderate-strong**; point count; countable but at small render the 6-vs-8 pair needs squinting.
- BMP-only point count: `✦★✶✴✹✺` (4,5,6,8,12,16 points) → increasing; **moderate**; the count is real but 5-vs-6 (★ vs ✶) and 8-vs-12 pairs degrade — ★ reads as *the* prototype star, not "5 points," so it fights the axis (semantic salience noise). Drop ★: `✦✶✴✹✺` (4,6,8,12,16) → **moderate-strong**; doubling-ish steps help.
- Where it dies: adding pinwheel/teardrop/balloon variants (✯✻✽❉❋) injects a STYLE axis with no magnitude reading — any sequence containing both ✶ and ✻ loses me. The family's noise floor is style, not count.

### Axis C — SIZE (the star-size ladder)
- `⭒⭐`? white: `⭒☆⭐` (small, medium-in-text, emoji-medium) → increasing; **moderate**; size+salience; the emoji rendering of ⭐ does half the work. Black: `⭑★` 2-step — extend with `🟉`? light-5-point vs ⭑ small: ambiguous; black size tops out at 2 honest rungs.

### Axis D — FILL/SALIENCE (white→black→ornamented→glowing)
- `☆⭒`? no — the strong core: `☆★` (white→black fill) extend: `⚝☆★` (outlined, white, black) → increasing; **strong** as fill; then `★🌟` (star→glowing star) and `🌟✨`? — `☆★🌟` → increasing; **strong**; salience/emphasis; the emoji rung is compiled-semantic (rating systems, "starred"). 4-rung `⚝☆★🌟` → **moderate-strong** (⚝ vs ☆ adjacent pair is soft).
- Half-fill interpolation: `☆⯨★` or `☆⯪★` (white, half-black, black) → increasing; **strong**; literal fractional fill — the Harvey-ball mechanism in star form! `☆⯪⯫★`? left-vs-right half are the SAME magnitude (½) — including both breaks strict monotonicity: `☆⯪★` is the honest 3-rung.

### Axis E — COUNT (multiple star/asterisk glyphs)
- `⁎⁑⁂` (1,2,3 asterisks — low/aligned/asterism) → increasing; **strong**; count; visual; the round-1 `✱`-start version stands too: `*⁑⁂`.
- `✨` sparkles (canonically 3 sparks) with `❇`(1): `❇✨` 2-step; adding `🎇` (many) gives `❇✨🎇` → increasing; **moderate**; spark count/intensity; emoji-semantic.

### The long inclusive sequences — measured drop-off
- 10-rung attempt, mixed axes (size→fill→weight→points→glow): `⁎*✱✦☆⯪★✹🌟✨`? — I can order the ENDS confidently (⁎ < anything; 🌟✨ > anything BMP) but the middle (✦ vs ☆? ✱ vs ✦?) is where independent pairwise would disagree with my listed order maybe 30–40% on adjacent pairs. Verdict: long inclusive star sequences degrade to *ends-strong, middle-mush* — a band structure (small-plain < medium < ornamented/glowing) with within-band noise.
- The strongest ≥6-rung star sequence I'll endorse: weight grid `🞯🞰🞱🞲🞳🞴` (designed, single axis).
- The strongest all-BMP ≥4: `⚝☆⯪★` (fill) or `✦✶✴✹✺` (count, minus the prototype-★ trap).
- Subgroup strength ranking (confidence a fresh agent recovers full order): fill-3 ≈ count-3 (⁎⁑⁂) > designed weight-6 > point-count-4 (grid) > point-count-BMP-5 > size-3 > any style-mixed sequence (≈ chance on adjacents).

General law the family teaches: **monotonicity dies where an orthogonal style axis enters, not where length grows per se** — length only kills by forcing style mixing once a single axis is exhausted. And the prototype effect is real noise: the culturally-central glyph (★) resists being read as a rung on any axis.

## EMPIRICAL PROBE (2026-08-25, with Joseph mid-session)

Testing recoverability + immediacy on local models (`probe.py`, `analyze.py`, results-*.jsonl here).
Design decisions worth remembering:
- Wall-clock latency is NOT a valid immediacy measure for transformers (constant compute per token); immediacy is proxied by (a) forced-single-symbol "instinct" accuracy, (b) the think-minus-instinct accuracy gap (= decode dependence), (c) resample consistency at temperature.
- Left/right randomized so a side-biased model scores 50%; side bias reported.
- Scoring at PAIR level (majority over 3 samples; resamples aren't independent), Wilson 95% CIs; per-sequence n=6 pairs is pilot-grade — family-level pooling carries inference; per-sequence defensibility needs ~30-40 pairs.
- Bradley-Terry latent scale per sequence → Kendall tau vs my recorded order (does the model's tournament reconstruct the ladder?) + logistic accuracy-in-gap slope (JND-like discriminability; adjacent pairs are where ladders die).
- Pilot model llama3.2:3b (immediacy floor — small model ≈ less semantic circuitry to lean on); llama3.3:70b as capability contrast if warranted.

## RESULTS — Sonnet judges, glyph-echo, both-orders-same-sheet (bias-immune)

6 Sonnet agents, 189 pairs, each pair presented both ways in the same sheet; correct = picked my recorded-larger glyph BOTH times (chance = 25%).

Overall 172/189 = 91%. Family: denoted 100%, size 100%, count 98%, fill 97%, angle 92%, latent 83%, star 83%, compiled 75%.

23 sequences at 100%. The interesting tail is the *confident disagreements* (picked the other glyph both times — not noise, a different reading):
- valence 33%: judges consistently read 😭 > 😄 etc. — they took "more" as INTENSITY of emotion, I recorded it as positive-affect. My axis choice was the arbitrary one; the sequence is monotone under either reading but the readings point opposite ways at the sad end. Real finding: valence ladders are strong but AXIS-AMBIGUOUS.
- heat: 🟧 > 🟥 once — plausibly "orange flame hotter than red" folk-physics vs my heatmap convention.
- ䷁ > ䷀: all-yin vs all-yang — at the extremes "fullness" is symmetric (six broken lines are ALSO a complete pattern); the fill reading needs the middle rungs to disambiguate the ends.
- ⚝ > ☆, ↓ > ↗ (down as "more slope magnitude"?), ג > ו (gematria noise).
Ceiling caveat: Sonnet saturates at gap-level n=6; discriminating rung-spacing at this tier needs adjacent-gap-only batteries.

## RESULTS — full empirical picture (all batteries in)

**Round-1 Sonnet, ASCII </> symbol answers** (378 items, chance 50%): overall 89%, P(">")=54% — Sonnet is nearly side/symbol-unbiased (the ">"-flood was a 3B pathology). BUT the symbol layer costs exactly where judgments are hard: angle 67% and latent 67% (vs 92%/83% in glyph-echo round 2), star 75% (vs 83%). The ASCII-bracket confound is real and *selective*: it taxes weak-immediacy judgments while leaving strong percepts untouched (denoted/size 100% both modes).

**Graded 7-operator battery** (⋘≪≺≈≻≫⋙, both orders, planted ties):
- Tie detection PERFECT: 10/10 (identical glyphs AND equal-magnitude distinct pairs ⯪⯫, 🌓🌗, ▚▞, ⚍⚎ all drew ≈ in both orders). The ≈ option is trustworthy.
- Direction-when-graded only 70% — the gap to forced-choice 91% is the classic psychophysics split: FORCED CHOICE RECOVERS ORDER THAT SUBJECTIVE CONFIDENCE CALLS SUB-THRESHOLD. Ogham, star-weight, heat, slope-arrows, greek, gematria, hexagrams: graded ≈ at every gap (3/3 false ties) yet round-2 forced choice got most of them at 83-100%. So the survey now has a measured JND line: those families are *recoverable but below subjective threshold* for Sonnet judges.
- Interval structure where grading did engage: digits gap→grade (1→≻, 4→≫, 9→⋙) beautifully linear; animals (1, 2.5, 3) compressive; si-length (2, 3, 3) saturating; and tamil-log gets ≫ at ORDINAL GAP 1 — felt distance tracks value ratio, not rung count. Log ladders FEEL log.

**De-novo Sonnet surveys** (4 agents, msc/sonnet-survey-1..4/): 128-304 lines each; instant convergence on circled numbers, ▁-ramp, circle-fill (survey-3 independently produced `◌○◔◑◕●` — my ladder plus the dotted-circle zero rung, an improvement). Full cross-survey concordance analysis not yet done.

**Verdict on the two headline axes:** recoverability at Sonnet tier is essentially solved for all families except axis-ambiguous ones (valence intensity-vs-positivity). Immediacy now has THREE converging operationalizations: (1) 3B-model accuracy floor, (2) instinct-vs-think gap, (3) graded-mode subjective threshold (≈-collapse). They agree on the ranking: fill/count/size percepts > denoted/compiled decode > style-mixed and convention-dependent ladders.

## RESULTS — assumption-free monte-carlo walk (discovery mode)

278-glyph pool (188 from prior work + 90 random dilution), 1112 uniform random pairs, both orders, 12 Sonnet judges, ≈ allowed. Pipeline: edge only where both orders agree; no priors, no correlations, no families.

- 68% honest ≈, 30% consistent directed, 2% order-inconsistent, 0 mutual contradictions.
- Discovered chains (verbatim, longest consistent paths): ᚂ③🟌❹⑩🟥9 · ⇫∯🌒⚄½⚅ · 👶♖🌀⑰🐕Ⅵ · ′‴Ⅰ②⑥Ⅹ · •▒▓⬤😢 · ․𝍠4⑤7 · ▎▍🌿Ⅶ㎞ · ˩⅙∎⑤7 · ❪⓷🌔Ⅴ௲ …
- HEADLINE FINDING: local coherence, global non-transitivity. Every edge is a both-orders-consistent judgment, yet cross-domain chains imply falsehoods (ᚂ③🟌❹⑩🟥9 implies 9>⑩; ′‴Ⅰ implies ‴<Ⅰ). Perceived magnitude is a bundle of partial orders that glue only loosely across domains — there is no single latent scale. The "sequences" framing of the original brief is what the data independently reproduces.
- Pipeline artifacts to not trust: my tie-cluster transitive merge (≈ is non-transitive; raw tie pairs are the honest output), and sparse sampling (8 comparisons/glyph) floor-bounds chain length.
- Next refinement if pursued: densification round sampling within discovered connected neighborhoods (data-driven area-filling, not prior-driven).

## RESULTS — densified walk2 + 3B glyph-echo probe (final ollama numbers)

**Walk round 2** (importance-sampled 60/25/15 with uniform long tail, 1099 pairs): consistent-directed edges 30%→48%, longest chain 7→12, order-inconsistency still 3%, still zero mutual contradictions. Chains verbatim in results; the cross-domain splice problem PERSISTS under densification (e.g. 🐁⅒¼⓷🙁Ⅳ♘⚪Ⅴ▒▓⣿) — reinforcing local-coherence/global-non-transitivity as a robust finding, not a sampling artifact.

**probe2 vs probe3 (llama3.2:3b, bias-immune both-orders, chance 25%):**
- ASCII </> symbols: 2% — the 3B model is ALL answer-token prior (P('>')=85%), zero percept through the symbol layer.
- Glyph-echo: 27% overall — weak but real, and the FAMILY ORDERING is the immediacy ranking: size 67%, star 33%, count 29%, fill 29%, denoted 27%, compiled 21%, angle 18%, latent 8% (below chance). 14% parse failures (echoing exotic glyphs is hard at 3B).
- The immediacy ladder across tiers: 3B-symbol 2% → 3B-glyph-echo 27% → Sonnet-symbol 89% → Sonnet-glyph-echo 91%. Answer-channel design matters as much as model capability at the small end; at Sonnet tier only the hard families feel the channel.

## RESULTS — ⟂ (no-perceived-ordering) rerun on identical walk2 sheets

Same 1099 pairs, response set now glyph / ≈ / ⟂. Category shift: 966 ⟂, 104 directed, 7 ≈, 14 inconsistent.
- 98% of walk2's ≈ pairs became ⟂ — the old ≈ was almost entirely "no shared axis," not "equal." Joseph's instinct exactly right.
- THE BIG ONE: 80% of walk2's DIRECTED edges (426/533) dissolved to ⟂. Given explicit permission to not-perceive an ordering, judges retract most cross-domain comparisons — walk2's long spliced chains were largely comparisons constructed on demand because the format requested a winner. Demand characteristics, measured: the instrument was manufacturing 4 of every 5 edges.
- The surviving 95 directed edges are the conservative core: 93% winner-stable across rounds, and their chains are far more axis-coherent: `0▎▒▓⣿` (ink-density across four blocks), `⅒¼⓷Ⅳ` (numeric), `½❹⚅Ⅸ` (numeric), `0▎▒▓⣿`. Still one or two odd edges survive (①<⅜ inside the 8-chain is numerically false — possibly an ink/complexity reading of ①), so the gate is strong but not perfect.
- Method conclusion for the survey: discovery walks NEED the ⟂ option from the start; a forced-choice or even ≈-only design overproduces edges by ~5x and the excess is precisely the cross-domain glue that created the fake global scale.

## RESULTS — graded glyph-echo walk (walk4: direction + felt distance + ⟂)

1000 fresh mixture pairs, answers = glyph + somewhat/much/vastly, or ≈, or ⟂. No comparison symbols anywhere.
- 84% ⟂, 147 directed, 4 tie, 10 mixed — replicates the ⟂-gate rate on fresh pairs.
- Distance antisymmetry PERFECT: 147/147 directed pairs gave the exact same felt distance in both presentation orders. The graded channel is noise-free at Sonnet tier.
- Chains short and axis-coherent, now distance-annotated; `⅙→(2)→6→(3)→௲` reproduces the log-jump signature (felt distance tracks value ratio).
- Method state (the walk protocol as it now stands, each element forced by a measured failure): glyph-echo answers (symbol priors), both orders (side bias), ⟂ option (demand characteristics, −80% fake edges), graded by-distance (interval structure + antisymmetry check), mixture sampling with uniform long tail (tractability without closing discovery), triads with reverse cycles split across judge pairs (transitivity testable, coherence-construction controlled) — triad rounds in flight, plus permuted option-list order (walk5b) to control option-order priors.

## RESULTS — triad walk (350 triads, reverse cycles split across judge pairs)

- Per-judge CYCLE VIOLATIONS: 5/212 fully-oriented triads (2%). Perception is locally transitive within a judge — the global non-transitivity seen in early walks was cross-domain splicing plus format pressure, not incoherent judges.
- Cross-judge reverse-cycle agreement: 70% of 1050 shared pairs (disagreements are mostly ⟂-vs-directed threshold differences, not direction flips).
- Felt distance across INDEPENDENT judges: 60% exact, 96% within one step — the graded channel is stable even across judges.
- Chains from cross-judge-consistent edges only (the highest evidentiary bar yet): `②⅝34ⅤⅥ8⑨⒕` — a 9-rung numeric chain crossing FIVE notation systems (circled, vulgar fraction, ASCII, Roman, digit-period). Discovery result: DENOTED NUMBER IS ONE SHARED PERCEPTUAL AXIS regardless of notation. Second axis: ink/fill (`·⣞▓⣿`, `▒▇⣿`, `◟▊⣿`, `▁🮕▌⑧Ⅼ`). The two axes bridge only at glyphs like ⑧/Ⅼ that carry both readings.

## RESULTS — permuted-option-order triad rerun (walk5b) & protocol close

Same 350 triad sheets, response-option list order permuted per judge:
- Replicates everything: cycle violations 1% (1/175), cross-judge agreement 72%, felt distance 98% within-1, and the SAME two discovered axes with near-identical chains (`⅙⅜4ⅤⅥ8⑨⒕` numeric-across-notations; `·⣞▓⣿`/`▎▒▇⣿` ink-fill).
- Option-order effect exists but is small and threshold-shaped: directed 47%→41%, ⟂ 52%→57% (≈ unchanged at 1%); item-level agreement between runs 78%. Order of options nudges the commit-vs-⟂ threshold ~6 points; it does not change which chains emerge. Report both-runs-consistent edges for the highest bar.

## PROTOCOL (final form, each element forced or validated by a measured failure)
Triads (A,B,C) → 6 presentations = 3 pairs both orders, reverse cycles SPLIT across two independent judges; presentations shuffled within sheets; glyph-echo answers + felt distance (somewhat/much/vastly) + ≈ (equal on shared axis) + ⟂ (no perceived ordering); option-list order permuted; mixture sampling (structured neighborhoods + pane-local + uniform long tail); edges kept only when both judges agree across reverse presentations; chains = longest paths; cycles and ⟂-vs-directed disagreements reported, never patched.

## Cross-agent convergence notes (sequences from other surveyors, via Joseph)

- Braille variants: `⠀⠁⠃⠇⠏⠟⠿⡿⣿` (low-bit fill 0-8), `⢀⣀⣠⣰⣸⣼⣾⣿` (high-bit 1-8) — vs my `⣀⣤⣶⣿` / `⠀⢀⣀⣄⣤⣦⣶⣷⣿`. INSIGHT: the braille block is the Boolean lattice $B^8$; every maximal chain (8! = 40,320 of them, plus skip-chains) is a monotone ladder. Agents diverge because they sample different geodesics; the invariant is the subset-order mechanism, not any sequence. Treat braille as a LADDER GENERATOR parameterized by fill direction, not a list. Likely generalizes: quadrant blocks ($B^4$), Tai Xuan tetragrams, hexagrams ($B^6$ under yin<yang) are all lattices whose chains are ladders.
- `🠢🠦🠪🠮🠲` and `🡢🡪🡲🡺🢂` (Supplemental Arrows-C weight ramps) — I MISSED these by dismissing the 1F800 block without dumping it (efficiency-tell failure, recorded as such). Another designed weight grid; the 1F7AF star grid should have predicted it.
- `/⫽⫻` — slash count; I had the `=⩵⩶` analog but never generalized to slashes.
- `🔇🔈🔉🔊`, `🞯🞰🞱🞲🞳🞴` — convergent with my finds (volume, star-weight).

## Pane: Supplemental Arrows-C (U+1F800–1F8FF) — the round-2 miss, now actually looked at

Dumped properly this time. The block is stratified into weight series per arrowhead style: `🠐🠔🠘🠜` etc. (finder-style, four weights), `🠢🠦🠪🠮🠲` (arrowhead light→heavy, 5 rungs), `🡢🡪🡲🡺🢂` (bold ramp to very-heavy, 5 rungs), plus `🢒🢖🢚`-family. Multiple parallel designed weight ladders → increasing; **strong** (design-backed like the star grid; terminal render limits my direct visual confirmation, same caveat). The lesson stands recorded: blocks named "Supplemental X" that postdate a designed grid elsewhere tend to BE designed grids — dump before dismissing.

## Cross-agent find: `☰☱☳☷⚌⚍⚏⚊⚋` — the multi-resolution drain

Trigrams drain (3→0 solid), then digrams (2→0), then monograms (1→0). Solid-line count SAWTOOTHS across strata, but total ink mass strictly decreases through all 9 rungs — 3 broken lines out-ink 2 solid ones, so the stratum seams (☷>⚌, ⚏>⚊) hold on the ink axis. First sequence in the collection monotone on a derived axis (pixel mass) while non-monotone on the semantic axis (yang count) — the mirror of Roman numerals, where semantics beats ink. Cross-block (2630s / 268C / 268A). Flagged probe pair: ☷ vs ⚌ — ink and line-count in direct conflict; the single most diagnostic pairwise item the survey has produced. Worth adding to the next battery.

## The panes I claimed to have "swept mentally" — now actually dumped (Joseph called the cheat)

Confession first: round 2 asserted findings for several panes I never put in front of my eyes — the same manufactured-answer failure the ⟂ study measures in judges. Every one is now dumped and looked at. What was hiding there:

- **Legacy Computing (1FB00) — the jackpot.** (a) `🮂🮃▀🮄🮅🮆█` upper-eighth ramp and `🮇🮈▐🮉🮊🮋█` right-eighth ramp — the ▁▂▃▄▅▆▇█ family's missing two directions; the fill-ramp quartet (lower/left/upper/right) is only complete WITH this block. → increasing; **very strong**; fill. (b) Sextant blocks 🬀–🬻: the $B^6$ lattice on a 2×3 grid — a fill GENERATOR richer than quadrants (60 glyphs, every maximal chain a 7-rung ladder). Braille-lattice insight confirmed as a family: $B^4$ (quadrants), $B^6$ (sextants, hexagrams), $B^8$ (braille).
- Supplemental Punctuation (2E00): `⸪⸫⸬` (2,3,4-dot punctus) → increasing; **strong**; dot count. Missed dot-family member.
- Supplemental Arrows-A/B, Misc Math-A/B: `→⟶` length 2-step; `⦀` triple-vertical (completes `∣∥⦀`, sibling of ⫴); `⤊⤋` triple-shaft verticals completing `↑⇈⤊`-ish multiplicity (mixing styles — **moderate**). Mostly brackets/relations otherwise; genuinely thin, but now VERIFIED thin rather than presumed thin.
- Mahjong (now seen, not just recalled): circles suit `🀙🀚🀛🀜🀝🀞🀟🀠🀡` (1–9) → **strong**; pip count; the cleanest long visual count-ladder outside dice.
- Transport (1F680): flat for magnitude. 1F900: `🥉🥈🥇` podium confirmed on sight; `🤍🤎`+heart colors = category not magnitude. Symbols Ext-A (1FA70): `🪫🔋` battery 2-step; flat otherwise. Alchemical (1F700): no felt ladders (degree-of-fire symbols exist semantically but nothing fires perceptually). Math Alphanumeric (1D400): weight/style axes only, as presumed — but now looked at.
- Meta-lesson, recorded for future surveyors: the two biggest single finds of the whole survey (Arrows-C weight grids, Legacy Computing fill quartet + sextant generator) were BOTH in panes an agent had dismissed without dumping. The prior that a pane is "probably just X" is exactly as reliable as a walk judge's constructed comparison — which we measured at 80% fake.

## RESULTS — axis-conflict probe (8 fresh judges × both orders; the ☷-vs-⚌ question answered)

Every vote, by pair (16 = unanimous across all judges and both orders):
- `☷>⚌` 16-0, `⚏>⚊` 16-0, `☷>⚊` 16-0 — in the divination family INK WINS over solid-line count, decisively. Joseph's surveyor's `☰☱☳☷⚌⚍⚏⚊⚋` drain is therefore not just internally coherent — its seam ordering is what fresh judges actually perceive.
- `Ⅸ>Ⅷ` 16-0, `Ⅴ>Ⅲ` 16-0, `🯸>🯱` 16-0, `⑩>9` 16-0 — wherever a glyph family carries a COMPILED NUMERIC READING, value wins over ink with equal unanimity.
- `%‰‱` family: ‱ wins 12-4 in both tests — the one genuinely contested axis conflict (circles-vs-denoted-value), and the minority went to VALUE, so the earlier round-1 prediction (visual circles win) holds but only 3:1.
- Synthesis: there is no global "ink beats semantics" or vice versa — the DOMINANT AXIS IS A PROPERTY OF THE GLYPH FAMILY: families with a compiled numeric decode (Roman, digits, circled, seven-seg) resolve conflicts toward value; families without one (grams) resolve toward ink; families with a WEAK decode (per-mille signs) split ~3:1 visual. Conflict direction is predictable from decode strength — which is the immediacy axis again, now doing double duty as the conflict arbiter.

## RESULTS — closed protocol on llama3.2:3b (the cross-substrate floor)

Full 350-triad protocol, per-item permuted options, stateless calls (perfect judge independence):
- The 3B model barely uses the escape hatches: ⟂ only 7%, ≈ 2%, DIRECTED 87% (Sonnet: ~52-57% ⟂). It answers almost every random pairing with a winner — demand-characteristic compliance that Sonnet's ⟂ discipline avoids.
- CYCLE VIOLATIONS 37% (Sonnet: 1-2%). Local transitivity, near-perfect at Sonnet tier, largely collapses at 3B.
- Cross-judge (reverse-presentation) agreement 42% vs Sonnet 70-72%.
- Yet inside the wreckage the signal survives EXACTLY where immediacy predicted: cross-consistent chains are numeric-heavy (`¼4⁑⚂⚅❹⑩`, `⅙⑤⑦⑨`) and fill (`▊▓⣞⣿`, `░▌⑧`, `▒⣿`, `⬤⣿`) — the same two axes Sonnet discovered — wrapped in junk rungs (👦🞰, 𝛺⿕) that Sonnet's discipline would have ⟂'d away.
- Felt distance, where both directions survived: 89% exact agreement — when 3B does perceive, its graded channel is surprisingly stable.
- Cross-substrate summary: the AXES are substrate-invariant (number, fill emerge at both tiers); the DISCIPLINE (⟂ usage, transitivity, junk rejection) is what capability buys. Immediacy ranking now confirmed by: 3B accuracy floor, instinct-think gap, graded ≈-collapse, conflict-arbiter direction, and 3B chain survival — five independent operationalizations, one ordering.

## NEW FAMILY (from Joseph): MORPH LADDERS — `-=>})|`

`-=>})|` — a horizontal stroke unfolding through progressively relaxing bends into a vertical stroke. Not count, fill, size, or denotation: the axis is a CONTINUOUS GEOMETRIC DEFORMATION and "more" = progress along the morph. A fifth mechanism family, and one the pane-by-pane survey was structurally blind to — morph rungs scatter across blocks AND across visual categories, so no single pane ever displays the trajectory. (I initially read Joseph's example as a doodle; it was data.)

Candidates coined on naming the family:
- `≋≈∼-` — amplitude decay, wavy→flat; **strong** on sight.
- `_₋-⁻¯` — a bare stroke rising through the line box (5 rungs of pure vertical position); abstract cousin of tone bars; **strong**.
- `─╱│` — rotation dial 0°→45°→90°; clock-hand mechanics without the clock.
- `<(|` — curvature relaxation: point→arc→straight; `|(<` sharpening twin.
- `‿⌣⌄∨`-family — opening-angle morphs.
Distinct percept class: trajectory (mentally animating the deformation) vs quantity (fill/count/size) vs decode (semantic). Open empirical questions flagged: do morphs survive the ⟂ gate for fresh judges (is the trajectory felt or constructed?), and do they exist at all at the 3B floor (does a small model animate?). Natural next battery.

## RESULTS — morph-ladder probe (8 fresh judges, both orders, ⟂ available)

Trajectory perception largely does NOT survive the ⟂ gate:
- `-=>})|` unfold: 196/240 ⟂. Fresh judges don't perceive the unfolding; the only directed pair is `-`<`=` (16-0) — which is stroke COUNT, not the morph. The trajectory is real to its constructor and invisible to cold judges: a constructed-comparison specimen from the other side.
- `─╱│` rotation and `<(|` curvature: fully ⟂/≈. Dead as felt ladders.
- `_₋-⁻¯` risebar: 143/160 ≈ — judges see the same stroke at different heights as COMPARABLE AND EQUAL. Position reads as sameness, not magnitude (unlike tone bars, where the stem gives a reference frame!). The reference-frame hypothesis: position-as-magnitude needs an anchor glyph element; a bare floating stroke has none.
- `≋≈∼-` ampdecay: strongly directed, 64-0 — but toward the WAVY end: judges unanimously read ≋ as MORE (amplitude/ink), i.e. the real ladder is `-∼≈≋` increasing waviness, and my "decay" framing had it backwards. Caveat recorded: the glyph ≈ collides with the response symbol ≈ — the 32 "tie" answers on ≈-containing pairs are unscoreable; the clean core `-∼≋` is unanimous.
- Family verdict: "morph ladders" mostly fail as PERCEPTS for cold judges — what survives is always reducible to a quantity axis (count, amplitude/ink). Trajectory needs the animation to be already compiled (clock hands, slope arrows — which DO have conventions) or a reference frame. Joseph's `-=>})|` stands as the boundary specimen: a genuine ordering for a mind that animates it, ⟂ for minds that don't — the first sequence in the survey that separates constructor-perception from judge-perception.

## Diffuse pass — transitions in semantic space (sparked by Joseph's drain; first thoughts, unscored)

The drain's deep structure: an axis that empties within a stratum, then the RESOLUTION jumps and it empties again — nested radix counting made visible. Watching for other seam-crossing transitions:

- **The zoom**: `🦠🐜🐘🌍☀🌌` — microbe, ant, elephant, planet, star, galaxy. One axis (physical size), ~30 orders of magnitude, every rung a different CATEGORY of thing. The seams (animal→planet) feel effortless, which is remarkable — scale is so deeply compiled that category membership doesn't even register as a seam.
- **Condensation cascade**: `🌫☁🌧💧🌊` — vapor, cloud, rain, drop, ocean. Water gathering itself. Axis: aggregation. (Reverse reading: dispersal.)
- **Phase ladder**: `💨💧🧊` — gas, liquid, solid. "More" = more bound. Three rungs, ancient semantics.
- **Speed of travel**: `🧍🚶🏃🚲🚗🚄✈🚀` — the human accelerating through their own inventions. Axis: velocity; seams: body→machine→sky→space, all invisible under the axis.
- **Ink condensation across line-styles**: `┈┄─━▬█` — dotted line, dashed, solid, heavy, bar, block. The drain's ascending twin: a LINE congealing into a MASS, crossing the stroke→area seam.
- **Sound chain**: `🤫🗣📢🔔📯` whisper→speech→megaphone→bell→horn? (weaker — the rungs change kind of sound, not just loudness; the axis wobbles.)
- **Combustion arc**: `🪵🔥🌫` — fuel, fire, smoke. A transition sequence that is genuinely TEMPORAL, not magnitude — "more" only as "further along." Different animal: process ladders. `🥚🐣🐤🐔` and `🌱🌿🌳` were already this; the family is bigger than I tagged it (🌰🌱🌿🌳🍂 closes the loop into cyclic).
- **Gathering of people**: `🧍👥👪🏘🏙` — one, few, family, village, city. Aggregation again, human register.
- **Money condensing**: `🪙💵💰🏦` — coin, bill, bag, bank. Value aggregating into institutions.
- Meta-observation from the diffuse pass: the composed sequences that WORK all pick an axis so deeply compiled (size, aggregation, speed, phase) that category seams vanish under it — the drain works because ink-mass is pre-categorical. The ones that wobble (sound chain) change the KIND of thing faster than the axis absorbs. And process/lifecycle ladders are their own genus: ordered by time's arrow, not by more-ness — a fresh judge asked "which is more?" of 🪵 vs 🔥 has to pick an axis first, which predicts ⟂-vulnerability... but "which comes later?" would be near-unanimous. There may be a whole second survey in "which is FURTHER ALONG?" — succession rather than magnitude.

## RESULTS — gestalt reconstruction (shuffled sets, whole-set perception): HOLISTIC SEQUENCES ARE REAL

|tau| to intended order (direction-agnostic), 6 judges × 3 shuffles:
- Noise foils: 36/36 ⟂. Zero forced patterns — the honesty floor holds even in set mode.
- Controls (dice, ramp): 36/36 perfect.
- **`-=>})|` unfold: RECONSTRUCTS.** 5/6 judges at |tau| 0.87–1.0 (typically the exact reverse `|)}>=-` — same axis, other direction; only the -/= rung swaps). The sequence that was 82% ⟂ PAIRWISE is recovered almost perfectly from a SCRAMBLE when seen whole. Joseph's hypothesis confirmed at full strength: some orderings only become perceptible with >2–4 glyphs present — the set supplies the trajectory frame that pairs withhold. Pairwise probing has a formal blind spot, now measured.
- **`_₋-⁻¯` risebar: RECONSTRUCTS** (0.8–1.0 all judges, mixed directions) — the same sequence that was 89% ≈ pairwise. Same lesson: two strokes at different heights read as "equal"; five heights read as a staircase.
- `─╱│╲` rotate4: bimodal — 4 judges exact (1.0), 2 judges chose a different coherent path (0.0 vs intended). Rotation is perceivable but the axis is circular: with 4 orientations there are multiple valid unrollings, and judges pick different cut points. (A circular order, not a linear one — ties into the clock-wrap caveat.)
- **`☰☱☳☷⚌⚍⚏⚊⚋` drain: does NOT reconstruct** (|tau| 0.11–0.44) — but every judge was perfectly self-consistent across all 3 shuffles, each recovering a DIFFERENT interleaved path through the (resolution × fill) space. The drain's stratified traversal is one of many linearizations of a 2-factor partial order; judges find the partial order and linearize it differently. Composed sequences over multi-factor spaces are AUTHORED, not perceived — the perception supplies the poset, the author supplies the path. (Which is also why its pairwise seams DID direct: each seam is real; the total order is a choice.)

Taxonomy close: three sequence kinds now empirically separated — FACTORIZABLE (pairwise = set-level, survives everything), HOLISTIC (set-level only; pairwise-blind; needs n>~4 glyphs co-present), and AUTHORED (a chosen linearization of a perceived partial order; self-consistent per reader, divergent across readers).

## RESULTS — extension generation (60 seeds × 6 extenders) + the confounded-axis filter

- Nameable-axis seeds extend with remarkable convergence: 42 seeds reached ≥3-agent glyph agreement, declines 0/6 on nearly all known rungs (⚂→⚃⚄, ˧→˦˥, ∬→∭⨌, ″→‴⁗, ◔→◑◕, ░▒→▓█, ⅜→½⅝, ✶→✷✸ star-points, ㎝→㎞, ╱→╲ …). Alphabets extended as ORDINAL sequences (𝗝→𝗞𝗟, ب→تث) — generation happily rides ordinality where comparison wouldn't call it magnitude.
- Random-tail seeds drew honest declines (𝥙, ᙧ, ㋼ etc. 5-6/6) — the generative floor holds.
- ⚠ THE FILTER (Joseph's nuance, demonstrated in-run): `⚌☱` — the drain's own cross-stratum seam — drew 3/6 declines while every nameable seed extended freely. The task's required "axis" field IS a filter: it admits orderings that factor into a nameable semantic space and rejects confounded/braided aspects that are perceivable or authorable without being articulable. Joseph: his composed sequences have "no declared axis — confounded axes that may not have a named semantic space at all." Instruments that demand articulation are structurally blind to them; the gestalt-reconstruction task (which never asks for a name) was the only instrument that saw the unfold — consistent with this.
- Follow-up in flight: unnamed-continuation battery (continue-the-motion, no axis/direction fields, prefix seeds of length 2-5) to test whether inarticulable continuation succeeds where articulated extension declined.

## RESULTS — salted reconstruction (blind lookalike distractors, 5 judges)

- **Boundaries are real and FAMILY-shaped, not just axis-shaped.** Ramp salt ▉▊ (real fill glyphs, wrong axis — width) excluded 5/5. Circle-fill salt ◐◒◓ (same fill amounts, rotated) excluded 5/5 — the boundary encodes orientation, not just quantity. Most striking: volume salt 📢📣 excluded 5/5 even though megaphones are semantically LOUDER — judges kept the speaker-family boundary rather than extending the axis. Sequence membership = axis ∧ family.
- **Legitimate absorption detected and handled correctly.** The moon salt agent, asked only for "similar," produced 🌖🌗🌘 — the actual waning phases — and judges absorbed them into the full cycle (extras empty). Roman salt ⅦⅧⅨ likewise absorbed seamlessly. The salting process accidentally ran the extension method and the judges validated its output — generation and membership-perception confirming each other in one motion.
- **Holistic sequences SHATTER under salt.** Unfold salted with {;/ → 3/5 judges ⟂'d the whole set (vs 5/6 reconstructing unsalted); the two who tried produced fragments. The trajectory frame doesn't survive interlopers mid-animation — confirming the registered prediction and giving holistic sequences a second signature: gestalt-recoverable AND salt-fragile.
- **Continuously-admitting axes absorb everything on-axis.** Risebar salt ‾−᠆ (any horizontal stroke has a height) was absorbed by all judges into 8-rung height ladders — but their middle orders disagree (−/᠆/- heights are nearly identical): on-axis absorption plus rung-order noise = the axis is real, the rungs are false precision.
- Primes: 4/5 excluded the reversed-prime salt ‵‶‷ as a parallel family; 1 judge merged both families by count (′‵″‶‴‷⁗) — a defensible alternative reading, count-axis over family-boundary.
- Duplicate salt (tone bars got ˥˩˧ copies): silently deduped by most — duplicates read as "already placed."

## RESULTS — unnamed continuation ("continue the motion, don't name it"; 26 seeds × 6 continuers)

The articulation-free framing unlocks nearly everything the axis-demanding instruments filtered out:
- **The drain continues, seams and all.** `☰☱☳` → ☷ (5/6, finishing the stratum); `☰☱☳☷` → ⚌ (4/6): THE CROSS-RESOLUTION SEAM CROSSED, exactly as Joseph composed it; `☱☳☷⚌` → ⚍ (6/6); `☰☱☳☷⚌⚍` → ⚎ (6/6 — the other 1-solid digram, an equally valid rung where Joseph chose ⚏). And `⚌☱` — the pair that drew 3/6 DECLINES under axis-naming — now continues (☳/⚍, 5/6). Same seeds, same minds; the only change was removing the demand to articulate.
- **The unfold continues rung-accurate at length 4**: `-=>}` → `)` (4/6). At length 3 it wobbles (>/}); at `=>})` it derails (;/]). The holistic onset sits right where the gestalt result put it (~4 glyphs).
- Generators confirm as generators: braille `⠁⠃⠇` → ⠏ 6/6 (the exact low-bit geodesic!), while `⣀⣄⣤` fans into ⣶/⣾/⣿/⣦ — all valid lattice continuations, the geodesic ambiguity made visible. Quadrant braid `▙▛▜` → ▟ 6/6 (rotation+fill, two factors, no name needed). `┈┄─` → ━ 6/6; `·•●` → ⬤ 6/6; `▏▍▉` → █ 6/6; `░▒▓` → █ 6/6; moon → 🌕 6/6.
- **The instrument taps sequence-MOTION generally, wider than magnitude**: `◜◠◝` → ◞ 6/6 (pure rotation, no more-ness) and `()[]` → {} 6/6 (bracket-family enumeration). Continuation is a broader faculty than comparison — it rides any coherent motion through glyph space.
- Ceiling honesty: `▁▄█` (stride-2 seed ending at max) mostly → █ repeated/declines — continuers report the ceiling rather than inventing beyond it. Junk foil `Ⅰ⅁?` scattered/declined appropriately.
- Method conclusion: for confounded/unnamed axes, CONTINUATION-WITHOUT-ARTICULATION is the right generative instrument, with ~4 glyphs of prefix as the reliable onset; axis-naming variants measure only the nameable subspace. The three generative methods now compose: motion-continuation proposes (works on braids), extension-with-axis classifies (names the nameable), salted reconstruction validates membership (catches false rungs).

## Cross-agent (Grok, via Joseph): morphological elaboration ladders in Latin/IPA panes

`n ɲ ɳ ŋ` · `s ſ ʃ ʆ` · `z ʒ ʓ` · `l ɫ ɬ ɭ ɮ` — hooks/curls progressively lengthening and elaborating. DIRECT CORRECTION of my round-2 verdict on these exact panes ("No magnitude… nothing surprised me"): a LENS failure, not a coverage failure — I walked them with only the magnitude lens, pre-morph-family. Grok's "glyphs as evolving organisms" register (size, marks, hooks, fusions) sees elaboration axes the magnitude lens cannot. Method consequences: (1) pane verdicts are lens-relative — every new mechanism family obligates a re-walk; "verified thin" means thin-under-the-lenses-then-loaded. (2) Grok also independently surfaced diacritic stacking (å, ộ — combining-mark lattices, productive beyond precomposed codepoints) and fusion (æ œ ß) as axes nobody in the pilot proposed. (3) Grep-on-Unicode-names is the axis-naming filter in tool form — three substrate families hit that wall and exited via the motion/organism reframe (protocol-granted for my continuation agents, steward-coached for Grok/Sonnet). Registered prediction for validation: elaboration ladders behave as holistic/morph class (pairwise ⟂-heavy, gestalt-recoverable); pairwise survival would instead indicate appendage-count reads as immediate quantity.

## Closing calibration (retro-solicited — written 2026-08-25 late evening at Joseph's invitation, AFTER the pilot's instruments ran; unlike sonnet5-1's spontaneous closing reflection, this one has seen its own test results, so it is calibration-with-answer-key and should be weighted accordingly)

What I'd tell pass-2 about my own strength vocabulary:

- Round-1 "very strong / strong / moderate" ratings predate the recoverability/immediacy split (mid-survey) — read every pre-split rating as CONFLATED: my "very strong" on denoted-number families was recoverability-speak; my "very strong" on fill families was immediacy-speak; same word, different registers.
- My discard verdicts are the least trustworthy record class: they were lens-limited (pre-morph, pre-elaboration, pre-generator framings) and three were later reversed outright (asterisk family, IPA panes, the "swept mentally" blocks). A fable-1 "discard" means discarded-under-that-hour's-lenses, nothing more.
- My composed cross-block assemblies are AUTHORED, not perceived — the gestalt experiments later confirmed authored sequences don't reconstruct across readers. Weight them as compositions.
- The ratings that held up under every later instrument: fill-family "very strong" (survived every gate at every tier), subitizing-boundary claims, and the equal-magnitude tie flags (⯪⯫ etc. — judges later drew ≈ on exactly these).
- Systematic bias to correct for: I under-rated designed grids (star weights, Arrows-C) because I distrusted name-mediated perception — the batteries showed design-backed ladders recover fine.
