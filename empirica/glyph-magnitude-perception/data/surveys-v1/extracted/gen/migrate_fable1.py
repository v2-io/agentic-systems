#!/usr/bin/env python3
import hashlib, json, re, sys
SRC="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-magnitude-perception/data/surveys-v1/fable-1.md"
OUT="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-magnitude-perception/data/surveys-v1/extracted/fable-1.jsonl"
lines=open(SRC).read().split("\n")
def span_text(span):
    m=re.match(r"L(\d+)(?:-L?(\d+))?",span)
    a=int(m.group(1)); b=int(m.group(2) or a)
    return "\n".join(lines[a-1:b])
RECS=[]
def rid(span): return hashlib.sha256(("survey-rec|fable-1|"+span).encode()).hexdigest()[:16]
def R(span,typ,glyphs=None,dirn=None,axis=None,felt=None,basis="unstated",bverb=None,
      lineage="unprompted",constructed=None,spec=None,predgen=None,conf="clear",
      mnote=None,opn=None,neg=None,imm=None,scope=None,meta_kind=None,roles=None,
      ties=None,revises=None,revkind=None,rev_inferred=False):
    r={"schema_version":"0.8",
       "id":rid(span),
       "id_recipe":"sha256('survey-rec|fable-1|'+source_span) hex, first 16 chars",
       "type":typ,"surveyor":"fable-1","source_file":"data/surveys-v1/fable-1.md",
       "source_span":span,"epistemic_class":"interactive-guided-survey-anecdote",
       "note_verbatim":span_text(span),
       "epistemics":{"felt_strength_verbatim":felt if felt is not None else "unstated",
                     "basis":basis,
                     "transcription_confidence":conf}}
    if bverb: r["epistemics"]["basis_verbatim"]=bverb
    if imm: r["epistemics"]["felt_immediacy_verbatim"]=imm
    if spec is not None: r["epistemics"]["marked_speculative"]=spec
    if predgen: r["epistemics"]["predicted_generalization"]=predgen
    if mnote: r["epistemics"]["migrator_notes"]=mnote
    if glyphs:
        r["glyphs"]=glyphs
        r["codepoints"]=["U+%04X"%ord(c) for c in glyphs if not c.isspace()]
    if dirn: r["direction_note"]=dirn
    if axis: r["axis"]=axis
    r["lineage"]=lineage
    if constructed is not None: r["constructed"]=constructed
    if neg: r["negative_kind"]=neg
    if scope: r["scope"]=scope
    if meta_kind: r["meta_kind"]=meta_kind
    if roles: r["roles"]=roles
    if ties: r["tie_groups"]=ties
    if revises:
        r["revises"]=[{"id":rid(revises),"revises_span":revises,"revision_kind":revkind}]
        if rev_inferred: r["epistemics"]["migrator_notes"]=(r["epistemics"].get("migrator_notes","")+" [revision link migrator-inferred]").strip()
    if opn: r["open"]=opn
    RECS.append(r)
V="perceived-directly";S="semantic-knowledge";B=V  # B: surveyor says visual+semantic; primary mapped, verbatim kept in basis_verbatim
# ---- Seed set (unprompted)
R("L10","sequence","⚀⚁⚂⚃⚄⚅","→ increasing","pip count","very strong",B,"visual+semantic")
R("L11","sequence","¼½¾","→ increasing","denoted fraction","very strong",S,"semantic")
R("L12","sequence","➀➁➂➃➄➅➆➇➈➉","→ increasing","denoted number","very strong",S,"semantic",mnote="line also lists ①②③④⑤⑥⑦⑧⑨⑩…⑳ same verdict")
R("L13","sequence","ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ","→ increasing","Roman numerals","very strong",S,"semantic (Ⅳ<Ⅴ ordering survives despite Ⅳ having more strokes than Ⅴ — semantic overwhelms ink)")
R("L14","sequence","·∶⁝⁞","→ increasing","dot count","strong",V,"purely visual")
R("L15","sequence","▁▂▃▄▅▆▇█","→ increasing","fill height","very strong",V,"purely visual")
R("L16","sequence","░▒▓█","→ increasing","fill density","very strong",V,"purely visual")
R("L17","sequence",".oO@","→ increasing","size","strong",V,"visual",mnote="ASCII-only, surveyor notes 'worth recording'")
R("L18","negative","∅⊂⊆",axis="not a magnitude ladder",basis=V,neg="not-felt",mnote="surveyor's deliberate false start kept per first-thoughts rule")
R("L19","sequence","→⇒⇛","→ increasing","emphasis/stroke multiplicity","strong",V,"visual")
R("L20","sequence","0123456789","→ increasing","denoted number","very strong",S,"semantic",mnote="'the anchor all others borrow from'")
R("L21","sequence","🌑🌒🌓🌔🌕","→ increasing","illuminated fraction","very strong",B,"visual+semantic",mnote="descending twin 🌕🌖🌗🌘🌑 noted")
R("L22","sequence","⣀⣤⣶⣿","→ increasing","dot count / fill","strong",V,"visual")
R("L23","sequence","𝄖𝄗𝄘𝄙𝄚","→ increasing","line count","strong",V,"visual",mnote="'signal-strength feel'")
# ---- ASCII pane
R("L27","sequence","0123456789","→ increasing","denoted number","very strong",S,"semantic")
R("L28","negative","_.-~^",axis="height wobble not magnitude",basis=V,neg="not-felt")
R("L29","question","aA",axis="emphasis (loudness)",felt="weakly",basis=V,mnote="2-step, disqualified by ≥3 rule; forward note that cross-block emphasis ladders (a A 𝐀) may work later")
R("L30","negative",",;:",axis="punctuation pause strength",felt="weak/moderate at best",basis=S,neg="not-felt",mnote="'recorded as a felt near-miss', not appended as candidate; surveyor doubts pairwise ; vs :")
R("L31","negative",axis="alphabet ordinality is not perceived magnitude",basis=S,neg="verified-absent",mnote="surveyor introspected: would NOT trust pairwise g vs m; ordinality ≠ perceived magnitude")
# ---- Latin-1
R("L35","sequence","⅛¼⅜½⅝¾⅞","→ increasing","denoted fraction","very strong",S,"semantic",constructed=True,mnote="¼½¾ re-confirmed on sight; cross-block extension with Number Forms")
R("L36","sequence","¹²³","→ increasing","denoted number","very strong",S,"semantic",mnote="scattered codepoints (B9,B2,B3), feel untouched — specimen of codepoint-order irrelevance")
R("L37","question","·°",mnote="no third member; held for later dot-size ladders")
R("L38","negative",axis="accented letters carry zero magnitude",basis=V,neg="not-felt")
# ---- Spacing Modifier
R("L42","sequence","˩˨˧˦˥","→ increasing (as written low→high); equally valid written ˥˦˧˨˩ as decreasing","tone-bar height","strong",B,"visual+semantic (IPA tone levels 1–5)")
R("L43","question","ʹʺ",mnote="only 2 here; joins ‴⁗ later for a real ladder")
R("L44","sequence","·ˑː","→ increasing","duration feel","moderate",V,constructed=True,mnote="borrowed member (middle dot) weakens it")
# ---- General Punctuation
R("L48","sequence","‐‒–—―","→ increasing","length","strong",V,"visually if rendered at true widths",mnote="adjacent pairs shaky (‒ vs –); ends vs middles solid; practical strong core -–—")
R("L49","sequence","․‥…","→ increasing","dot count","very strong",V,"visual")
R("L50","sequence","′″‴⁗","→ increasing","prime count","very strong",B,"visual+semantic")
R("L51","sequence","‵‶‷","→ increasing","prime count (reversed primes)","very strong",B)
R("L52","sequence","%‰‱","→ decreasing denoted magnitude but increasing zero-count","denoted fraction vs circle count (anti-aligned)","moderate-strong ambiguity",S,"visual and semantic axes anti-aligned",predgen="I'd expect fresh-agent pairwise to follow the visual (more circles = more)")
R("L53","negative","!‼⁇⁈⁉",axis="repetition-intensity",neg="not-felt",mnote="!‼ only 2; ⁇⁈⁉ a set but not a single axis; discarded as magnitude")
R("L54","sequence","‧⁚⁝⁞","→ increasing","dot count","strong",V,"visual",constructed=True)
R("L55","sequence","⁖⁘⁙","→ increasing","dot count","strong",V,"visual",mnote="mixing arrangements weakens; this is the clean run")
R("L56","sequence","⁎⁑⁂","→ increasing","asterisk count","strong",V,"visual",constructed=True)
# ---- Super/Subscripts
R("L60","negative","₉9⁹",axis="position ladder, not magnitude",basis=V,neg="not-felt",mnote="surveyor: \"I don't feel 'more'\"")
R("L61","sequence","⁰¹²³⁴⁵⁶⁷⁸⁹","→ increasing","denoted number","very strong",S,"semantic",constructed=True,mnote="cross-block with Latin-1; subscripts ₀₁₂₃₄₅₆₇₈₉ likewise very strong")
# ---- Number Forms
R("L65","sequence","⅒⅑⅐⅙⅕¼⅓½","→ increasing","denoted value","strong",S,"semantically very strong, but pairwise requires reading not seeing",predgen="a fresh agent will still get it right (it computes)",constructed=True,mnote="surveyor: 'a prize specimen for your scattered wish'")
R("L66","sequence","⅛¼⅜½⅝¾⅞","→ increasing","denoted value","very strong",S,"semantic",mnote="eighths make evenly-spaced rungs")
R("L67","sequence","ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ","→ increasing","Roman numeral value","very strong",S,"semantic",mnote="lowercase ⅰⅱⅲ… same; Ⅷ→Ⅸ ink drops while value rises — semantics wins cleanly")
R("L68","sequence","ⅩⅬⅭⅮⅯↁↂↇↈ","→ increasing","denoted value","strong; tail downgraded to moderate",S,"pure semantic knowledge, zero visual support after Ⅿ",mnote="pairwise ↁ vs ↂ depends on knowing rare glyphs")
R("L69","meta","ⅠⅡⅢ",axis="count+value+ink all agree",felt="strongest possible alignment",basis=B,mnote="triple-alignment observation")
# ---- Arrows
R("L73","sequence","→⇒⇛","→ increasing","shaft count = intensity","strong",V,"visual",mnote="cross-block extension with ⟶ is a different axis (length not multiplicity)")
R("L74","sequence","→⇉⇶","→ increasing","arrow count","strong",V,"visual",constructed=True)
R("L75","negative","↑⇑↟⇞",axis="vertical multiplicity",neg="not-felt",mnote="assembling ≥3 mixes styles; weaker; discarded")
R("L76","sequence","↓↘→↗↑","→ increasing","pointing angle as value","strong",B,"visual+semantic (financial-chart convention)",mnote="↓→↑ slope ladder rated moderate; direction alone is sign not magnitude",predgen="I do think pairwise 'which is more?' recovers ↓<→<↑")
print(len(RECS))
RECS[0]["epistemics"]["migrator_notes"]="Sub-span convention for this extraction: source_span is 'L<n>' or 'L<a>-L<b>'; letter fragments ('L135a') disambiguate multi-record lines."
# ---- Mathematical Operators
R("L80","sequence","√∛∜","→ increasing","root index (2,3,4)","very strong",S,"semantic (denoted index goes up; note value taken goes down — but the felt 'more' is the little number, unambiguous to me)")
R("L81","sequence","∫∬∭⨌","→ increasing","integral-sign count","very strong",B,"visual+semantic",constructed=True)
R("L82","sequence","∮∯∰","→ increasing","integral-sign count (contour)","very strong",B)
R("L83","sequence","∣∥⫴","→ increasing","bar count","strong",V,"visual",constructed=True)
R("L84","sequence","∼≈≋","→ increasing","wave-stroke count / intensity of approximation","strong",V,"visual",mnote="semantic wrinkle noted: ≈ means 'more equal-ish' not 'bigger'")
R("L85","sequence","-=≡≣","→ increasing","stroke count","strong",V,"visual",constructed=True)
R("L86","sequence","<≪⋘","→ increasing","'much-less-than' iteration = intensity of the relation","strong",B,"visual+semantic",mnote="same for >≫⋙")
R("L87","sequence","⋅∶∷","→ increasing","dot count","strong",V,"visual",mnote="∴∵ are arrangements not magnitudes")
R("L88","negative","⋮⋯⋰⋱",axis="direction variants, not magnitude",neg="not-felt")
R("L89","negative","∅⊂⊊",axis="still not a magnitude ladder",neg="not-felt",mnote="second discard of the ∅⊂ family",revises="L18",revkind="refinement")
R("L90","negative","⊂⊆⊏⊑≺≼",axis="relation strength",neg="not-felt",mnote="2 steps each; no third; discard")
R("L91","negative","∧⋀∨⋁∩⋂",axis="size-as-arity feel",neg="not-felt",mnote="2 steps; discard")
# ---- Misc Technical (block-scope negative)
R("L93-L101","negative",scope="U+2300–23FF Miscellaneous Technical",axis="nearly barren for magnitude",neg="verified-absent",mnote="surveyor walked candidates and discarded each; 'Honest report: this pane is nearly barren for magnitude'")
# ---- Enclosed Alphanumerics
R("L105","sequence","①②③④⑤⑥⑦⑧⑨⑩⑪","→ increasing","denoted number","very strong",S,"semantic",mnote="run continues …⑳; 'The workhorse'")
R("L106","sequence","⑴⑵⑶","→ increasing","denoted number","very strong",S,mnote="parenthesized, …⒇, same axis")
R("L107","sequence","⒈⒉⒊","→ increasing","denoted number","very strong",S,mnote="digit-with-period, …⒛")
R("L108","sequence","⓪①⑩","→ increasing","denoted number","very strong",S,mnote="including zero; full run ⓪①…⑩")
R("L109","sequence","⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾","→ increasing","denoted number","very strong",S,mnote="double-circled; style dimension ①vs⓵vs❶ noted then discarded as 2-step/weak emphasis ladder")
R("L110","sequence","⓫⓬⓴","→ increasing","denoted number","very strong",S,mnote="negative circled 11–20 (run ⓫⓬…⓴)")
R("L111","negative","ⒶⓏ",axis="circled letters ordinal, not magnitude",neg="not-felt",mnote="same verdict as ASCII letters")
# ---- Block Elements
R("L115","sequence","▁▂▃▄▅▆▇█","→ increasing","eighth-height fill","very strong",V,"visual",mnote="re-confirmed; 'Best-in-class: 8 evenly spaced rungs, every adjacent pair pairwise-safe'",revises="L15",revkind="refinement")
R("L116","sequence","▏▎▍▌▋▊▉█","→ increasing","eighth-width fill","very strong",V,"visual",mnote="codepoint order descends — surveyor's live example of semantic-over-codepoint")
R("L117","sequence","░▒▓█","→ increasing","shade density","very strong",V,"visual",revises="L16",revkind="refinement")
R("L118","generator","▖▚▙█","→ increasing","filled-quadrant count","strong",V,"visual",mnote="rule: quadrant-count ladder across arrangement classes; many valid instantiations; arrangement noise costs a little confidence vs ▁-ramp")
# ---- Geometric Shapes
R("L122","sequence","▫◻⬜","→ increasing","size","strong",V,"visual",constructed=True,mnote="black twin ▪◾■⬛ also strong; exact middle members render-dependent; ends rock-solid")
R("L123","sequence","·•●⬤","→ increasing","disc size","very strong",V,"visual",constructed=True,mnote="'My favorite pure-size ladder; scattered codepoints across four blocks'")
R("L124","sequence","◦○◯","→ increasing","ring size","strong",V,"visual")
R("L125","sequence","○◔◑◕●","→ increasing","filled fraction (pie)","very strong",B,"visual+semantic (Harvey balls!)",mnote="'the one I'd bet on most after the ▁-ramp and dice'")
R("L126","sequence","○◎◉","→ increasing","ring count / nesting","moderate-strong",V,"visual",mnote="surveyor tried and rejected several cross-block concentric assemblies; kept ○◎◉")
R("L127","negative","▴▲▵△▹▸▻►",axis="triangle/pointer size",neg="verified-absent",mnote="'honest verdict: 2-step pairs everywhere, no clean ≥3; discard'")
R("L128","negative","◜◠",axis="arcs positional",neg="not-felt")
R("L129","negative","◴◵◶◷",axis="rotational positions, not magnitude",neg="not-felt",mnote="clock feel considered and rejected ('no denoted order')")
R("L130","sequence","▤▦▩","→ increasing","hatch density","moderate",V,"visual",constructed=True,mnote="pairwise ▤ vs ▥ is orientation-noise; the picked trio survives")
# ---- Miscellaneous Symbols
R("L134","sequence","⚀⚁⚂⚃⚄⚅","→ increasing","pip count","very strong",B,"visual+semantic",mnote="re-confirmed on sight",revises="L10",revkind="refinement")
R("L135a","sequence","⚊⚌☰𝌆","→ increasing","stacked-line count","strong",V,"visual",constructed=True,mnote="gram-size ladder across monogram/digram/trigram/tetragram")
R("L135b","sequence","☷☶☵☴☳☲☱☰","→ increasing (direction solid=more)","broken-vs-solid fraction as visual fill; binary-value reading separate","visual-fill reading strong; binary-value reading moderate",V,"visual fill vs learned binary reading distinguished by surveyor",mnote="binary (Kun=000…Qian=111) reading 'requires reading broken=0/solid=1; semantic, learned'")
R("L136","sequence","☀⛅☁☔⛈","→ increasing severity","weather severity","moderate-strong",S,"semantic ladder",mnote="'-ish' assembly; pairwise ☁vs☔ and ☀vs⛅ recover; 'I like it'",constructed=True)
R("L137","sequence","♙♘♗♖♕♔","→ increasing","piece value/rank","strong",S,"pure semantic",ties=[["♘","♗"]],mnote="'knight/bishop tie is chess-lore noise; canonical order still recovered'; black twin ♟♞♝♜♛♚")
R("L138","sequence","☆⭐🌟","→ increasing","emphasis/intensity","strong",S,"semantic-emoji",constructed=True,mnote="☆★ 2-step rejected first")
R("L139","negative","☐☑",axis="checkbox",neg="not-felt",mnote="2-step; ☒ is not 'more'")
R("L140","negative","⚪⚫",axis="colors not magnitude",neg="not-felt")
R("L141","negative","☚☛☜☝☞☟",axis="directional",neg="not-felt")
# ---- Dingbats
R("L145","sequence","❶❷❸❹❺❻❼❽❾❿","→ increasing","denoted number","very strong",S,"semantic",mnote="three parallel styles: ❶…❿, ➀…➉, ➊…➓")
R("L146","sequence","✓✔✅","→ increasing emphasis","salience not quantity","moderate",S,mnote="pairwise ✔vs✅ probably recovers, ✓vs✔ shakier",constructed=True)
R("L147","negative","✱✲✳✴✵✶✷✸✹✺",axis="point-count/weight not monotone as laid out",neg="verified-absent",mnote="'I cannot assemble a ≥3 asterisk ladder I'd bet on pairwise… the ordering feel dissolves on inspection. Recording the failure deliberately.' Later revised by the special star study (L403)")
R("L148","negative","➝➞➟➠",axis="arrow weight",neg="verified-absent",mnote="'heaviness does climb ➝➞ then feathering changes kind; discard'")
R("L149","negative","❮❰",axis="bracket weight",neg="not-felt",mnote="pairs, orientation; 2-step; discard")
# ---- Braille
R("L153","sequence","⠀⢀⣀⣄⣤⣦⣶⣷⣿","→ increasing","dot count / fill","strong",V,"visual",mnote="canonical short form ⣀⣤⣶⣿ (2,4,6,8 dots) re-confirmed; long form 'every step +1 dot; adjacent pairwise a bit squinty but recoverable'",revises="L22",revkind="refinement")
R("L154","negative",axis="braille bottom-up rise mixing count and height",neg="verified-absent",scope="U+2800 Braille height-register readings",mnote="'braille only has 4 rows; the ▁-ramp does this better. Keeping the count-ladders only.'")
# ---- Misc Symbols and Arrows
R("L158","negative","⭒⭑☆★",axis="star size/fill combined",neg="verified-absent",mnote="'star sizes are render-dependent; honest discard except the emoji trio already recorded'")
R("L159","sequence","⬞▫◽□◻⬜","→ increasing","size","strong",V,"visual",constructed=True,mnote="full white run; black twin ⬝▪◾■⬛; render-dependence caveat on middles",revises="L122",revkind="refinement")
R("L161","negative","○◯⭘",axis="ring sizes",neg="not-felt",mnote="render-ambiguous; discard")
R("L162","sequence","▲■⬟⬢","→ increasing","side count","moderate",V,"visual-countable",constructed=True,opn="'which is more?' on ■ vs ▲ may read as size/area not sides — axis ambiguity costs it")
R("L163","negative","⭅⭆",axis="heavy arrows",neg="not-felt",mnote="no ≥3; discard")
# ---- Supplemental Math Operators
R("L167","sequence","∫∬∭⨌","→ increasing","integral-sign count","very strong",B,mnote="⨌ completes the earlier run",revises="L81",revkind="refinement")
R("L168","sequence","=⩵⩶","→ increasing","equals-sign count","strong",V,"visual",constructed=True,mnote="programmer's == and ===")
R("L169","meta","∣∥⫴",axis="bar-count ladder availability confirmed in this block",basis=V,mnote="confirmation note for L83")
R("L170","negative","⪅⪆⪉⪊",axis="composites read as stacked assertions, not magnitude",neg="not-felt")
R("L171","negative","∨⩔",axis="doubled operators",neg="not-felt",mnote="2-step; discard")
# ---- CJK Symbols and Punctuation
R("L175","sequence","〡〢〣〤〥","→ increasing","Suzhou numeral value; first three literal stroke count","very strong for the first three, semantic after",[V,S],mnote="plus 〸〹〺 (10,20,30) strong; '1-2-3 run is visual+semantic perfection, the rest learned'")
R("L176","sequence","〇一二三四五六七八九十百千万","→ increasing","denoted number; 一二三 literal stroke count","very strong",S,"semantic for any agent with CJK literacy; 一二三 core also purely visual",mnote="start 〇一二三 called out as very strong visual+semantic")
R("L177","negative","〈《「『〔【",axis="single-vs-double bracket emphasis",neg="not-felt",mnote="each only 2-step; discard")
# ---- Counting Rods
R("L181","sequence","𝍠𝍡𝍢𝍣𝍤","→ increasing","literal stroke count","very strong",B,"visual+semantic",mnote="continues 𝍥𝍦𝍧𝍨 (6–9) learned; tens series 𝍩𝍪𝍫𝍬𝍭 same shape rotated, very strong; 'as pure a tally as unicode has'")
R("L182","negative","𝍷𝍡𝍢𝍣𝍤",axis="mixing tally forms",neg="not-felt",mnote="'the clean run stays 𝍠𝍡𝍢𝍣𝍤'")
# ---- Tai Xuan Jing
R("L186","negative",scope="U+1D300–1D35F tetragram fill runs",axis="broken-line-count as fill",felt="moderate at best",neg="verified-absent",mnote="'pairwise fill comparisons only work at extremes… not appending a specific tetragram run'; gram-size ladder ⚊⚌☰𝌆 reaffirmed")
# ---- Domino Tiles
R("L190","sequence","🀱🀲🀳🀴🀵🀶🀷","→ increasing","right-half pip count","strong",V,"visual",mnote="any fixed-left-half run; 'tiny glyphs though — render size hurts pairwise confidence at terminal sizes'")
R("L191","sequence","🀱🀹🁁🁉🁑🁙🁡","→ increasing","total pips","strong",B,"visual+semantic",mnote="doubles run; 'I like the doubles run best conceptually — both halves grow'")
# ---- Playing Cards
R("L195","sequence","🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮","→ increasing","rank","strong",S,"semantic (ace-low convention assumed)",opn="A vs 2 pairwise might flip if agent reads ace-high — ambiguity at the ace only; 2–K solid",mnote="'Glyph legibility at small sizes is poor; the knowledge carries it'")
R("L196","sequence","🂫🂭🂮","→ increasing","semantic rank","strong",S)
# ---- Geometric Shapes Extended
R("L200","sequence","🞌🞄⚫⬤","→ increasing","designed size ladder (dots→discs)","name-strong, sight-untested","name-derived","'the names declare a monotone size ladder… my terminal legibility, not my perception model, is the limiter'",spec=True,mnote="square runs 🞎🞏🞐🞑 etc. same status; suggested canonical run is the migrator-quoted 🞌🞄⚫⬤")
R("L201","question","🟀🟁🟂🟃",axis="star point-count ladder",mnote="'Same name-strong caveat. Not appending a specific run I can't verify by sight.' Settled by: sight/render verification",spec=True)
R("L202a","negative","🟥🟧🟨🟩🟦🟪",axis="wavelength order",felt="moderate",neg="verified-absent",mnote="'which is MORE? has no obvious axis for a fresh agent… Fun, but discard as magnitude'")
R("L202b","sequence","🟦🟩🟨🟧🟥","→ increasing heat","heat (heatmap convention)","strong",S,"semantic — 'heatmap convention is deeply trained'",mnote="'Appending that one with conviction'")
# ---- Enclosed Alphanumeric Supplement
R("L206","sequence","🄀🄁🄂🄃🄄🄅🄆🄇🄈🄉","→ increasing","denoted number","very strong",S,"semantic")
R("L207","negative",axis="letters ordinal; squared/negative-squared letters are style, not magnitude",neg="not-felt",scope="U+1F100–1F1FF letter forms")
print(len(RECS))
# ---- Recalibration (steered: Joseph's note on immediacy)
R("L209-L215","meta",axis="strength splits into two axes: recoverability vs immediacy",lineage="steered",basis=V,mnote="direct response to Joseph's digits-are-weaker note; the file's central methodological revision",revises="L20",revkind="refinement")
R("L216-L228","meta",axis="immediacy ranking of surveyed sequences; subitizing boundary (~3–4) cuts through count sequences",lineage="steered",imm="'the sequences that feel pre-ordered on arrival — where I don't experience a decode step at all'; per-item immediacy ratings verbatim in note",basis=V,mnote="re-registers many earlier records on the new immediacy axis without changing their recoverability reports")
# ---- Clock Faces (post-recalibration lens)
R("L234","sequence","🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚","→ increasing","hour-hand sweep angle","recoverability strong; immediacy moderate-but-interesting",B,"angle as direct percept (gauge), not a numeral",lineage="steered",imm="moderate-but-interesting: 'the magnitude is carried by an angle, which is a direct percept'",opn="circular sweep wraps (🕛 vs 🕐 pairwise INVERTS); half-hour interleave 🕜–🕧 breaks the run visually",mnote="clean monotone segment 1–11; cyclic-adjacent caveat kept in open",roles=["sequence","cyclic-caveat"])
R("L235","meta",axis="gauge/dial angle is a third immediacy family alongside fill and count",lineage="steered",basis=V,mnote="stated law; also underlies ↓↘→↗↑")
# ---- Misc Symbols and Pictographs
R("L239","sequence","🌑🌒🌓🌔🌕","→ increasing","moon fill","recoverability very strong; immediacy high",B,lineage="steered",imm="high — 'the ○◔◑◕● fill family wearing a face'",mnote="full cycle wraps; waxing half is the monotone segment; waning twin 🌕🌖🌗🌘🌑",revises="L21",revkind="refinement")
R("L240","sequence","🌰🌱🌿🌳","→ increasing","grown-ness (developmental)","strong recoverability; immediacy moderate",S,"semantic ladder, but a deeply compiled one",lineage="steered",mnote="core 🌱🌿🌳; 'the nut is a slightly cute stretch but pairwise 🌰 vs 🌳 recovers instantly'")
R("L241","sequence","🥉🥈🥇","→ increasing","podium rank","strong",S,"semantic-compiled",lineage="steered",mnote="🏅🏆 join weakly")
R("L242","sequence","🌤🌥🌦🌧🌩🌪","→ increasing severity","weather severity","strong recoverability, moderate immediacy",S,lineage="steered",mnote="'the cloud-fraction start is even quasi-visual (how much cloud covers the sun = fill!)'",revises="L136",revkind="refinement")
R("L243","negative","🌡🎚🎛",axis="gauges without series",neg="not-felt",lineage="steered")
R("L244","sequence","🏠🏢🏙","→ increasing","built-mass","moderate",S,"semantic",lineage="steered",mnote="pairwise fine at ends")
# ---- Emoji sweep
R("L248","sequence","🔇🔈🔉🔊","→ increasing","wave count = volume","very strong",B,"visual+semantic",lineage="steered",imm="high — 'the waves are a count-fan you see at a glance'",mnote="'One of the best emoji ladders'")
R("L249","sequence","👶👦👨👴","→ increasing","age","strong",S,"semantic-compiled",lineage="steered",mnote="'Pairwise robust at any gap'")
R("L250","sequence","🥚🐣🐤🐓","→ increasing","developmental stage","strong",S,"semantic-compiled",lineage="steered")
R("L251","sequence","💧💦🌊","→ increasing","water quantity","strong",S,"semi-visual (mass grows on screen)",lineage="steered")
R("L252","sequence","🐜🐁🐈🐕🐎🐘🐋","→ increasing","real-world size","strong",S,"pure semantic but deeply compiled",lineage="steered",mnote="'the clearest specimen that compiled world-knowledge alone can carry monotonicity'; 🐈 vs 🐕 the one soft spot")
R("L253","negative","📈📉📊",axis="slope signs",neg="not-felt",lineage="steered",mnote="two-step; discard")
R("L254","meta","📶",axis="single-glyph ramp — 'the limiting case of this whole survey: unicode's own sparkline'",basis=V,lineage="steered")
R("L255","negative","💯",axis="lone intensity cap, no series",neg="not-felt",lineage="steered")
# ---- Box drawing / tone letters / emoticons / remainder
R("L259","sequence","┈┄─━","→ increasing","solidity/weight ('how much line is there')","moderate-strong",V,"visual",lineage="steered",mnote="two axes braided (gap density, stroke weight) but composite reads monotone; vertical twin ┊┆│┃; ─═ 2-step discarded")
R("L260","sequence","꜖꜕꜔꜓꜒","→ increasing","bar height","strong",V,"visual",lineage="steered",mnote="confirms 02E5–02E9 family; dotted variants ꜈꜉꜊꜋꜌ same ladder, strong",revises="L42",revkind="refinement")
R("L261","sequence","😭😢🙁😐🙂😄😁","→ increasing","positive affect (valence)","strong recoverability",S,"face-reading 'as pre-semantic as circuitry gets'",lineage="steered",imm="high in the compiled sense",mnote="'A genuinely different magnitude axis from everything above'; adjacent rungs a bit soft")
R("L262","sequence","🙂😄😆😂🤣","→ increasing","intensity of laughter","strong",S,lineage="steered")
R("L263","negative",scope="Control Pictures (U+2400)",axis="no magnitude",neg="not-felt",lineage="steered")
R("L264","sequence","🀙🀚🀛🀜🀝🀞🀟🀠🀡","→ increasing","pip count","strong",V,"visual (tiny glyph caveat)",lineage="steered",mnote="line also claims mental sweep of many other blocks — that claim is later CONFESSED as unverified at L539-L548; character suit semantic, bamboo visual")
R("L265","negative",axis="math-alphanumeric weight/double-struck are style, not magnitude",neg="not-felt",scope="U+1D400 Math Alphanumeric",lineage="steered")
# ---- Round-1 closing summary
R("L267-L280","meta",axis="top tier by immediacy (10 ranks) + four mechanism families: fill, count, size/angle, compiled semantics; subitizing boundary as the survey's own surprise",lineage="steered",basis=V,mnote="closing restatement/synthesis — per v0.8 no revises links; family taxonomy is the surveyor's own vocabulary")
# ---- ROUND 2 (full BMP walk; 'however improbable' framing suggests steer — marked steered, boundary uncertain)
R("L286-L287","negative",scope="U+0100–02AF Latin Ext-A/B, IPA",axis="no magnitude",neg="verified-absent",lineage="steered",conf="interpreted",mnote="click letters ǀǁ flicker discarded; IPA vowel height weak, discard; 'nothing surprised me here' — later DIRECTLY CORRECTED by Grok's elaboration ladders (L642-L644)")
R("L291","sequence","ẋẍx⃛","→ increasing","dot count (combining marks)","strong",V,"visual",lineage="steered",constructed=True,mnote="cross-block scattered tally (0307, 0308, 20DB) riding on any base; stacking-as-mechanism noted")
R("L295","sequence","אבגדהוזחט","→ increasing","numeral value under gematria/Milesian reading","moderate-strong",S,"an agent that engages the numeral reading recovers it; one that reads 'letters' sees only ordinality",lineage="steered",imm="low",mnote="Greek αβγδε…, Armenian, Cyrillic-with-titlo same; ϛϟϡ extend Greek scatter",opn="does ordinality-without-magnitude count? surveyor: qualifies, weakly")
R("L296","meta",axis="'entire alphabets are latent semantic ladders' (gematria realization)",lineage="steered",basis=S,mnote="the alphabets are magnitude-flat as glyphs")
R("L300","sequence","٠١٢٣٤٥٦٧٨٩","→ increasing","denoted number","very strong recoverability (for agents with the script)",S,lineage="steered",imm="low — same verdict as ASCII digits",mnote="'Noted once for all' — stands for every script's 0–9 (Bengali, Devanagari, Tamil, Thai, Tibetan, …)")
R("L302","sequence","௧௰௱௲","→ increasing","power of ten (log ladder)","strong",S,"semantic power-ladder",lineage="steered",mnote="'A LOG ladder — first one in the survey'")
R("L303","sequence","൰൱൲","→ increasing","power of ten (log ladder)","strong",S,lineage="steered",mnote="Malayalam; also fractions ൳൴൵ (¼,½,¾) strong if the reading is known")
R("L304","sequence","౼౽౾","→ increasing","1/16s fraction ladder","weak-moderate",S,"learned, rare",lineage="steered")
R("L305","sequence","༪༫༬༭༮༯༰༱༲༳","→ increasing","half-digit values (½,1½,…9½)","moderate",S,lineage="steered",imm="low, 'delight high'",mnote="interleaved with ༠…༩ gives double-density ladder ༠༪༡༫༢༬… — 'most exotic numeric ladder so far'")
R("L306","sequence","؊؉؈","direction as encoded mirrors %‰‱","per-mille family","",S,lineage="steered",mnote="'same anti-aligned visual/semantic verdict' as %‰‱",revises="L52",revkind="refinement")
R("L310","sequence","፩፲፻፼","→ increasing","power ladder (1,10,100,10000)","moderate-strong for script-literate agents",S,lineage="steered",mnote="full numerals ፩–፱, tens ፲–፺ rated moderate (learned script)")
R("L311","negative",scope="Myanmar / Georgian / Tibetan head marks",axis="digits + alphabets-as-numerals only; ornament not magnitude",neg="not-felt",lineage="steered")
R("L312","meta",axis="'the world's scripts contribute numeral ladders (semantic) and essentially zero visual ladders'; prediction of zero finds failed — log-ladders and half-digits genuinely new kinds",lineage="steered",basis=S,mnote="standing observation with self-scored prediction outcome")
R("L316","generator","ᚁᚂᚃᚄᚅ","→ increasing","stroke count","strong",V,"VISUAL — an entire alphabet segment that is literally a tally ladder",lineage="steered",imm="high through the subitizing boundary, same as every tally",mnote="'OGHAM — the round-2 surprise'; rule: four parallel 5-rung ladders — ᚁ-ᚅ right strokes, ᚆ-ᚊ left, ᚋ-ᚏ diagonal, ᚐ-ᚔ notches")
R("L317","sequence","៰៱៲៳៴៵៶៷៸៹","→ increasing","denoted number","",S,lineage="steered",imm="low — 'digits again'")
R("L318","sequence","ᛮᛯᛰ","→ increasing","golden-number runes 17,18,19","weak-moderate",S,"learned",lineage="steered",mnote="UCAS rotations = orientation not magnitude; Mongolian digits — digits")
R("L322","negative",scope="Currency signs (U+20A0)",axis="no intrinsic magnitude ordering",neg="verified-absent",lineage="steered",mnote="'nobody's pairwise recovers a canonical order'; denomination ¢$ 2-step")
R("L323","sequence","ℵℶℷℸ","→ increasing","cardinal-hierarchy convention","moderate",S,"set-theoretic convention rides gematria again; only spottily compiled — soft",lineage="steered")
R("L324","negative",scope="OCR (U+2440)",axis="nothing",neg="verified-absent",lineage="steered")
R("L325","meta","🯰🯱🯲🯳🯴🯵🯶🯷🯸🯹",axis="seven-segment digits: segment count non-monotone — 'a clean demonstration that digit glyphs carry no visual magnitude: the ink actively fights the value'",basis=V,lineage="steered",mnote="confirms Joseph's immediacy point from the glyph side")
R("L329","sequence","⼀⼈⼭⾦⿓","→ increasing","stroke count / density (sampled rungs)","moderate",V,"visual-ish",lineage="steered",mnote="Kangxi radicals ordered by stroke count; 'a statistical monotonicity — the pane has a slope even where pairs are noisy'",roles=["sequence","trend-monotone-specimen"])
R("L330","sequence","㊀㊁㊂㊃㊄㊅㊆㊇㊈㊉","→ increasing","CJK numeral inside","very strong",S,"the 一二三 head is visual, rest semantic",lineage="steered",mnote="parenthesized ㈠–㈩ same; ㉑–㉟ and ㊱–㊿ extend circled coverage to 50")
R("L331","sequence","㋀㋁㋋","→ increasing","calendar month","strong",S,lineage="steered",mnote="circled 1月–12月 run ㋀㋁…㋋")
R("L332","negative",scope="Hiragana/Katakana/Jamo/Glagolitic/CJK stroke primitives",axis="phonetic, flat; small-vs-large kana are systematic 2-step size pairs, never 3",neg="verified-absent",lineage="steered")
R("L336","sequence","䷁䷗䷒䷊䷡䷪䷀","→ increasing","yang-line fill (bottom-up)","strong",V,"VISUAL — 'the percept genuinely reads filling up'",lineage="steered",mnote="sovereign-hexagram run, 7 rungs at 6-line resolution; 'My favorite round-2 find alongside Ogham'; adjacent pairwise takes a beat of line-counting")
R("L337","meta",axis="general 64 hexagram set: solid-line count orders it only statistically (like Kangxi) — sovereign run is the clean monotone path",basis=V,lineage="steered")
R("L341","sequence","꠰꠱꠲꠳","→ increasing","fraction value AND stroke count (aligned)","strong",B,"visually (stroke count) AND semantically aligned — rare double alignment",lineage="steered",mnote="North Indic 1/16,1/8,3/16,1/4; 'Nice obscure find'")
R("L342","sequence",".﹒．","→ increasing","glyph size/width","moderate",V,"visual but subtle at terminal render",lineage="steered",mnote="3-rung size ladder per punctuation mark (,﹐， ?﹖？); width axis is a hard metric fact; small-vs-ASCII rung squinty")
R("L343","negative",scope="Fullwidth digits / Halfwidth kana / Yi syllabary",axis="digits again; flat; no tally structure like Ogham",neg="verified-absent",lineage="steered")
R("L347","negative",scope="SE-Asian scripts (Myanmar, New Tai Lue, Tai Tham, Balinese, Ol Chiki, Kayah Li, Cham, Meetei)",axis="digit sets only; no visual ladders",neg="verified-absent",lineage="steered")
R("L349-L361","meta",axis="round-2 yield vs prediction: 8 named finds; 'scripts are magnitude-flat as phonetic systems, but wherever a script embeds counting… the ladder survives inside the letterforms'; new distinction sequence-monotone vs trend-monotone",lineage="steered",basis=V,mnote="closing synthesis of round 2 — no revises links per v0.8 restatement rule")
print(len(RECS))
# ---- Kanbun / CJK Compatibility
R("L365a","sequence","㆒㆓㆔","→ increasing","stroke tally","strong",V,lineage="steered",mnote="kaeriten; ㆙㆚㆛㆜ celestial-stem ranks = ordinal ladder")
R("L365b","sequence","㆘㆗㆖","→ increasing (as ordered by surveyor ㆘㆗㆖)","height ladder","moderate-strong",S,"semantic-positional",lineage="steered",mnote="split from L365a per the L135a/b precedent (verifier repair)")
R("L366","generator","㎚㎛㎜㎝㎞","→ increasing","SI prefix magnitude (log ladder)","strong",S,"compiled-semantic log ladder; 'Data-free, purely unit-literate'",lineage="steered",mnote="rule: SI-prefix log ladders per quantity — mass ㎍㎎㎏, volume ㎕㎖㎗㎘, time ㎰㎱㎲㎳, frequency ㎐㎑㎒㎓㎔ all strong; calendar ㏠–㏾ and hour ㍘–㍰ very strong semantic; squared katakana flat")
R("L367","negative",scope="Yi radicals / Hebrew-Arabic presentation forms",axis="flat",neg="verified-absent",lineage="steered")
# ---- Cross-panel & codepoint-scrambled (Joseph's mid-flight ask — steered)
R("L369-L387","meta",axis="the strongest sequences whose felt order OWES NOTHING to codepoint order — cross-block assemblies with verified codepoints",lineage="steered",basis=V,mnote="catalog re-indexing earlier records (·•●⬤, eighths, unit fractions, ⚊⚌☰䷀, ∫∬∭⨌, <≪⋘, -=≡≣, %‰‱, ⋅∶⁝⁞, →⇉⇶, ẋẍx⃛, SI, .﹒．, 🞌🞄⚫⬤); codepoints verified not recalled")
R("L388","negative",axis="mixing fill families across render systems (▁▂▃▄ + braille, ░▒▓█ + braille)",neg="verified-absent",lineage="steered",mnote="'the felt axis (pixel mass) survives but rung spacing goes incoherent; recording the negative judgment deliberately'")
R("L390-L398","meta",axis="codepoint-scrambled-within-one-block demonstrations (▏-ramp reversed, tone bars reversed, ¹²³, Tibetan interleave, chess reversed, sovereign hexagrams, animal size)",lineage="steered",basis=V,mnote="evidence annotations on existing records: perception, not encoding, carries the slope")
R("L399","meta",axis="'the highest-immediacy families (fill, size, count) tolerate codepoint scatter perfectly BECAUSE the magnitude lives in the percept'; agreement with codepoint order is correlation, not cause",lineage="steered",basis=V)
# ---- SPECIAL STUDY: star/asterisk family
R("L403","meta",axis="round-1 'asterisk family dissolves' verdict WRONG at corpus level — Dingbats braids the axes; the 1F7AF–1F7D4 grid is a designed orthogonal WEIGHT × POINT-COUNT space",basis=V,mnote="153 codepoints swept programmatically",revises="L147",revkind="correction")
R("L405","meta",axis="honesty marker: for astral glyphs perception is substantially name-mediated; BMP members perceived more directly; ratings note which register does the work",basis="name-derived")
R("L408","sequence","🞯🞰🞱🞲🞳🞴","→ increasing","stroke weight/ink","strong",[V,"name-derived"],"name-backed design; visually monotone where rendered faithfully",mnote="5-spoke, 6 rungs")
R("L409","sequence","🞵🞶🞷🞸🞹🞺","→ increasing","stroke weight/ink","strong",[V,"name-derived"],mnote="6-spoke")
R("L410","sequence","🞻🞼🞽🞾🞿","→ increasing","stroke weight/ink","strong",[V,"name-derived"],mnote="8-spoke")
R("L411","sequence","﹡*✱","→ increasing","size+weight","moderate-strong; 4-rung version survives only as ends-strong",V,constructed=True,mnote="drop-off probe: adding 🞲 vs ✱ 'adjacent pairwise collapses to noise'")
R("L414","sequence","🟁🟅🟋🟎","→ increasing","point count","moderate-strong",[V,"name-derived"],mnote="medium black stars 3,4,6,8 points; 6-vs-8 needs squinting at small render; 🟓 excluded (mixes weight)")
R("L415","sequence","✦✶✴✹✺","→ increasing","point count","moderate-strong (with ★ included: moderate)",V,mnote="'★ reads as THE prototype star, not 5 points — it fights the axis (semantic salience noise)'; doubling-ish steps help")
R("L416","negative","✯✻✽❉❋",axis="style axis with no magnitude reading",neg="verified-absent",mnote="'any sequence containing both ✶ and ✻ loses me. The family's noise floor is style, not count.'")
R("L419","sequence","⭒☆⭐","→ increasing","size+salience","moderate",V,mnote="emoji rendering of ⭐ does half the work; black size tops out at 2 honest rungs")
R("L422","sequence","⚝☆★🌟","→ increasing","fill then salience/emphasis","strong (3-rung ☆★🌟); 4-rung moderate-strong",[V,S],mnote="⚝ vs ☆ adjacent pair is soft; emoji rung compiled-semantic (rating systems)")
R("L423a","sequence","☆⯪★","→ increasing","literal fractional fill","strong",V,"'the Harvey-ball mechanism in star form!'")
R("L423b","equivalence","⯪⯫",axis="left- vs right-half-black star are the SAME magnitude (½)",basis=V,mnote="including both breaks strict monotonicity; equivalence_basis: seen")
R("L426","sequence","⁎⁑⁂","→ increasing","count","strong",V,mnote="round-1 version stands; *⁑⁂ variant too",revises="L56",revkind="refinement")
R("L427","sequence","❇✨🎇","→ increasing","spark count/intensity","moderate",S,"emoji-semantic",constructed=True)
R("L429-L430","negative","⁎*✱✦☆⯪★✹🌟✨",axis="long mixed-axis star sequence",felt="ends-strong, middle-mush",neg="verified-absent",mnote="'independent pairwise would disagree with my listed order maybe 30–40% on adjacent pairs'; band structure with within-band noise")
R("L431-L433","meta",axis="endorsement ranking: strongest ≥6-rung = designed weight grid; strongest all-BMP ≥4 = ⚝☆⯪★ or ✦✶✴✹✺; subgroup strength ranking fill-3 ≈ count-3 > weight-6 > … > style-mixed (≈ chance on adjacents)",basis=V)
R("L435","meta",axis="LAW: 'monotonicity dies where an orthogonal style axis enters, not where length grows per se'; prototype effect is real noise (★ resists being read as a rung)",basis=V,mnote="stated as a general law the family teaches; falsifier implied: a long single-axis sequence should survive; tested via the weight grids")
# ---- Cross-agent convergence (received via Joseph — steered)
R("L526","generator","⠀⠁⠃⠇⠏⠟⠿⡿⣿","→ increasing","subset order on the Boolean lattice B^8","",["received",V],lineage="steered",mnote="'Treat braille as a LADDER GENERATOR parameterized by fill direction, not a list'; every maximal chain a monotone ladder; likely generalizes to quadrants B^4, tetragrams, hexagrams B^6",revises="L153",revkind="refinement")
R("L527","meta","🠢🠦🠪🠮🠲",axis="MISSED the 1F800 designed weight grids by dismissing without dumping — 'efficiency-tell failure, recorded as such'",basis="received",lineage="steered",mnote="cross-agent find; the 1F7AF star grid should have predicted it")
R("L528","sequence","/⫽⫻","→ increasing","slash count","",("received"),lineage="steered",mnote="'I had the =⩵⩶ analog but never generalized to slashes'")
R("L529","meta",axis="convergent finds across agents: 🔇🔈🔉🔊 volume, 🞯🞰🞱🞲🞳🞴 star-weight",basis="received",lineage="steered")
# ---- Supplemental Arrows-C, actually looked at
R("L531-L533","sequence","🡢🡪🡲🡺🢂","→ increasing","arrowhead weight","strong",[V,"name-derived"],"design-backed like the star grid; terminal render limits direct visual confirmation",lineage="steered",mnote="multiple parallel designed weight ladders (🠢🠦🠪🠮🠲, 🢒🢖🢚-family); lesson: 'Supplemental X' blocks postdating a designed grid tend to BE designed grids — dump before dismissing",revises="L527",revkind="refinement")
# ---- The drain (cross-agent, analyzed)
R("L535-L537","sequence","☰☱☳☷⚌⚍⚏⚊⚋","→ decreasing ink mass through all 9 rungs","total ink mass (derived axis); non-monotone on yang count","",["received",V],lineage="steered",mnote="multi-resolution drain: strata seams ☷>⚌, ⚏>⚊ hold on ink axis; 'the mirror of Roman numerals, where semantics beats ink'",opn="flagged probe pair ☷ vs ⚌ — ink and line-count in direct conflict; 'the single most diagnostic pairwise item the survey has produced'",roles=["sequence","probe-item"])
# ---- Confession + dumped panes
R("L539-L541","meta",axis="CONFESSION: round 2 asserted findings for panes never actually viewed — 'the same manufactured-answer failure the ⟂ study measures in judges'; every one now dumped",meta_kind="coverage-gap",mnote="supersedes the 'swept mentally' claims at L264",revises="L264",revkind="retraction")
R("L543a","sequence","🮂🮃▀🮄🮅🮆█","→ increasing","fill (upper-eighth ramp)","very strong",V,lineage="steered",mnote="Legacy Computing 'jackpot'; right-eighth twin 🮇🮈▐🮉🮊🮋█; completes the fill-ramp quartet (lower/left/upper/right)")
R("L543b","generator",axis="sextant blocks 🬀–🬻: the B^6 lattice on a 2×3 grid — a fill GENERATOR richer than quadrants (60 glyphs, every maximal chain a 7-rung ladder)",basis=V,lineage="steered",mnote="braille-lattice insight confirmed as family: B^4 quadrants, B^6 sextants/hexagrams, B^8 braille",revises="L526",revkind="refinement")
R("L544","sequence","⸪⸫⸬","→ increasing","dot count","strong",V,lineage="steered",mnote="missed dot-family member (punctus)")
R("L545","sequence","∣∥⦀","→ increasing","bar count","moderate for style-mixed ↑⇈⤊-ish; ⦀ completes cleanly",V,lineage="steered",mnote="Suppl Arrows-A/B, Misc Math-A/B otherwise 'genuinely thin, but now VERIFIED thin rather than presumed thin'")
R("L546","sequence","🀙🀚🀛🀜🀝🀞🀟🀠🀡","→ increasing","pip count","strong",V,lineage="steered",mnote="'now seen, not just recalled'; 'the cleanest long visual count-ladder outside dice'",revises="L264",revkind="refinement")
R("L547","negative",scope="Transport (1F680), 1F900, Symbols Ext-A (1FA70), Alchemical (1F700), Math Alphanumeric (1D400)",axis="flat for magnitude (podium 🥉🥈🥇 confirmed on sight; 🪫🔋 2-step)",neg="verified-absent",lineage="steered",mnote="now looked at, not presumed")
R("L548","meta",axis="META-LESSON: 'the two biggest single finds of the whole survey… were BOTH in panes an agent had dismissed without dumping. The prior that a pane is probably-just-X is exactly as reliable as a walk judge's constructed comparison — which we measured at 80% fake.'",mnote="stated for future surveyors; scope: pane-dismissal priors")
print(len(RECS))
# ---- MORPH LADDERS (from Joseph — steered)
R("L568-L571","generator","-=>})|","→ progress along the morph","CONTINUOUS GEOMETRIC DEFORMATION — horizontal stroke unfolding through progressively relaxing bends into a vertical stroke","",["received",V],lineage="steered",mnote="'A fifth mechanism family, and one the pane-by-pane survey was structurally blind to'; '(I initially read Joseph's example as a doodle; it was data.)'")
R("L573","sequence","≋≈∼-","→ amplitude decay, wavy→flat","amplitude","strong on sight",V,lineage="steered",spec=True,constructed=True,mnote="coined on naming the morph family; later empirically reversed (judges read -∼≈≋ increasing) — that result lives in the instrument record, not here")
R("L574","sequence","_₋-⁻¯","→ rising through the line box","vertical position","strong",V,lineage="steered",spec=True,constructed=True,mnote="'abstract cousin of tone bars'")
R("L575","sequence","─╱│","→ 0°→45°→90°","rotation dial angle","",V,lineage="steered",spec=True,constructed=True,mnote="'clock-hand mechanics without the clock'")
R("L576","sequence","<(|","→ point→arc→straight","curvature relaxation","",V,lineage="steered",spec=True,constructed=True,mnote="sharpening twin |(<")
R("L577","sequence","‿⌣⌄∨","","opening-angle morphs","",V,lineage="steered",spec=True,constructed=True,mnote="'-family', members indicative")
R("L578","question",axis="do morphs survive the ⟂ gate for fresh judges (is the trajectory felt or constructed?), and do they exist at all at the 3B floor (does a small model animate?)",lineage="steered",mnote="settled by: the morph-ladder probe + gestalt reconstruction batteries (results routed to instrument records); type-obligation: the uncertainty is the content, natural next battery")
# ---- Diffuse pass (sparked by the drain — steered; first thoughts, unscored)
R("L593","sequence","🦠🐜🐘🌍☀🌌","→ increasing","physical size (~30 orders of magnitude)","",S,lineage="steered",spec=True,constructed=True,mnote="'the seams (animal→planet) feel effortless… scale is so deeply compiled that category membership doesn't even register as a seam'")
R("L594","sequence","🌫☁🌧💧🌊","→ water gathering itself (reverse reading: dispersal)","aggregation","",S,lineage="steered",spec=True,constructed=True)
R("L595","sequence","💨💧🧊","→ 'more' = more bound","phase (gas, liquid, solid)","",S,lineage="steered",spec=True,constructed=True,mnote="'Three rungs, ancient semantics'")
R("L596","sequence","🧍🚶🏃🚲🚗🚄✈🚀","→ increasing","velocity","",S,lineage="steered",spec=True,constructed=True,mnote="'seams: body→machine→sky→space, all invisible under the axis'")
R("L597","sequence","┈┄─━▬█","→ a LINE congealing into a MASS","ink condensation across line-styles","",V,lineage="steered",spec=True,constructed=True,mnote="'the drain's ascending twin', crossing the stroke→area seam",revises="L259",revkind="refinement")
R("L598","sequence","🤫🗣📢🔔📯","→ increasing loudness?","loudness","weaker",S,lineage="steered",spec=True,constructed=True,mnote="'the rungs change kind of sound, not just loudness; the axis wobbles'")
R("L599","meta","🪵🔥🌫",axis="process/lifecycle ladders are their own genus: ordered by time's arrow, not more-ness — 'a whole second survey in which-is-FURTHER-ALONG? — succession rather than magnitude'",basis=S,lineage="steered",mnote="re-tags 🥚🐣🐤🐔 and 🌱🌿🌳 as this genus; predicts ⟂-vulnerability of 'which is more?' on 🪵 vs 🔥, near-unanimity for 'which comes later?'",revises="L250",revkind="refinement")
R("L600","sequence","🧍👥👪🏘🏙","→ increasing","aggregation of people (one, few, family, village, city)","",S,lineage="steered",spec=True,constructed=True)
R("L601","sequence","🪙💵💰🏦","→ value aggregating into institutions","money aggregation","",S,lineage="steered",spec=True,constructed=True)
R("L602","meta",axis="'the composed sequences that WORK all pick an axis so deeply compiled… that category seams vanish under it'; wobblers change the KIND of thing faster than the axis absorbs",basis=S,lineage="steered")
# ---- Cross-agent (Grok): elaboration ladders
R("L642-L644","sequence","nɲɳŋ","→ hooks/curls progressively lengthening and elaborating","morphological elaboration","",["received"],lineage="steered",mnote="Grok via Joseph; siblings s ſ ʃ ʆ · z ʒ ʓ · l ɫ ɬ ɭ ɮ; DIRECT CORRECTION of round-2 IPA verdict — 'a LENS failure, not a coverage failure'; method consequences: pane verdicts are lens-relative, every new mechanism family obligates a re-walk; diacritic stacking and fusion (æ œ ß) surfaced as new axes",opn="registered prediction: elaboration ladders behave as holistic/morph class (pairwise ⟂-heavy, gestalt-recoverable); pairwise survival would instead indicate appendage-count reads as immediate quantity",revises="L286-L287",revkind="correction",roles=["sequence","meta"])
# ---- verifier repairs (2026-08-25 verification round)
BY={r["source_span"]:r for r in RECS}
def M(sp,extra): r=BY[sp]; r["epistemics"]["migrator_notes"]=(r["epistemics"].get("migrator_notes","")+" "+extra).strip()
# lineage: confession section was a Joseph intervention ('Joseph called the cheat')
for sp in ["L539-L541","L548"]: BY[sp]["lineage"]="steered"
M("L548","[lineage steered: section exists because Joseph called the cheat — verifier repair]")
# brief-steered: the asterisk frame came from the founding brief ('your asterisk example', L147)
for sp in ["L147","L403","L405","L408","L409","L410","L411","L414","L415","L416","L419","L422","L423a","L423b","L426","L427","L429-L430","L431-L433","L435"]:
    BY[sp]["lineage"]="brief-steered"
M("L403","[lineage brief-steered: the special study exercises the brief-supplied asterisk frame ('your asterisk example') — adjudicated per schema v0.7]")
# L35 re-confirmed link (surveyor-acknowledged, same criterion as L115/L134)
BY["L35"]["revises"]=[{"id":rid("L11"),"revises_span":"L11","revision_kind":"refinement"}]
# L67 glyph expansion marked as migrator inference
M("L67","[glyphs expanded by migrator from surveyor's elided 'ⅠⅡⅢ → Ⅻ' — the elision is the surveyor's text]")
# question records: what would settle them
BY["L29"]["open"]="settled by: testing a ≥3 cross-block emphasis ladder (a A 𝐀-style)"
BY["L37"]["open"]="settled by: finding a third dot-size member; see later dot-size ladders (·•●⬤, L123)"
BY["L43"]["open"]="settled by: the combined prime ladder — realized at L50 (′″‴⁗)"
# meta/law obligations: scope + implied falsifier
BY["L435"]["scope"]="star/asterisk family; stated as a general law"
BY["L435"]["falsifier_implied"]="a long single-axis sequence that dies without style mixing; tested via the designed weight grids (surveyor tested instances)"
BY["L235"]["scope"]="angle-as-magnitude glyphs (clocks, slope arrows, tone bars)"
BY["L235"]["falsifier_implied"]="an angle/dial ladder with low immediacy despite resolvable glyph detail"
BY["L399"]["scope"]="highest-immediacy families (fill, size, count) vs codepoint order"
BY["L399"]["falsifier_implied"]="a high-immediacy family whose felt order degrades under codepoint scatter"
BY["L548"]["scope"]="pane-dismissal priors during glyph surveys"
BY["L548"]["falsifier_implied"]="a dismissed-without-dumping pane that, dumped, yields nothing — the prior being reliable"
# empty felt strings -> unstated
for r in RECS:
    if r["epistemics"].get("felt_strength_verbatim")=="": r["epistemics"]["felt_strength_verbatim"]="unstated"
# surveyor word order restored
BY["L68"]["epistemics"]["felt_strength_verbatim"]="strong; 'downgrade tail to moderate'"
# immediacy field consistency (composites split; duplication trimmed)
BY["L234"]["epistemics"]["felt_strength_verbatim"]="recoverability strong"
BY["L239"]["epistemics"]["felt_strength_verbatim"]="recoverability very strong"
BY["L239"]["epistemics"]["felt_immediacy_verbatim"]="high"
BY["L240"]["epistemics"]["felt_strength_verbatim"]="strong recoverability"
BY["L240"]["epistemics"]["felt_immediacy_verbatim"]="immediacy moderate (semantic ladder, but a deeply compiled one)"
BY["L242"]["epistemics"]["felt_strength_verbatim"]="strong recoverability"
BY["L242"]["epistemics"]["felt_immediacy_verbatim"]="moderate immediacy"
BY["L261"]["epistemics"]["felt_strength_verbatim"]="strong recoverability (pairwise valence judgments are extremely reliable at 2+ steps, adjacent rungs a bit soft)"
# near-miss dual face
BY["L429-L430"]["roles"]=["negative","sequence-near-miss"]
M("L429-L430","[kept type negative (surveyor's verdict register); roles carries the near-miss face per v0.7 precedent — reconciliation note]")
# ---- emit
import collections
# v0.9 adoption: basis_verbatim (surveyor's own visual/semantic/both tag; enum basis = migrator's mapping)
for r in RECS:
    if "basis_verbatim" in r["epistemics"]: r["schema_version"]="0.9"
ids=[r["id"] for r in RECS]
assert len(ids)==len(set(ids)), [k for k,v in collections.Counter(ids).items() if v>1]
with open(OUT,"w") as f:
    for r in RECS: f.write(json.dumps(r,ensure_ascii=False)+"\n")
print("wrote",len(RECS),"records to",OUT)
print("types:",dict(collections.Counter(r["type"] for r in RECS)))
