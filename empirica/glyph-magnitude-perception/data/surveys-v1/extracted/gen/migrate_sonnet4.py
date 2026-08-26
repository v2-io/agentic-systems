#!/usr/bin/env python3
# Pass-1 migration of sonnet-survey-4.md -> extracted/sonnet-survey-4.jsonl
# Verbatim notes are sliced from the source file by line span (source is primary; records index into it).
import hashlib, json, unicodedata, os

BASE = "/Users/josephwecker-v2/src/arch/asf/empirica/glyph-magnitude-perception/data/surveys-v1"
SRC = os.path.join(BASE, "sonnet-survey-4.md")
OUT = os.path.join(BASE, "extracted", "sonnet-survey-4.jsonl")
SURVEYOR = "sonnet-survey-4"

lines = open(SRC, encoding="utf-8").read().split("\n")

def span_text(a, b=None):
    b = b or a
    return "\n".join(lines[a-1:b]).strip()

def cps(glyphs):
    s = unicodedata.normalize("NFC", glyphs.replace(" ", "").replace("/", ""))
    return ["U+%04X" % ord(c) for c in s]

def rid(span):
    return hashlib.sha256(("survey-rec|sonnet-survey-4|" + span).encode()).hexdigest()[:16]

records = []

def rec(a, b=None, type=None, glyphs=None, direction=None, axis=None,
        strength=None, immediacy=None, basis="unstated", tc="clear",
        mnotes=None, constructed=False, spec=False, predgen=None,
        negkind=None, scope=None, falsifier=None, tested=None,
        settle=None, open_=None, extra=None, lineage="unprompted",
        revises=None, revision_kind=None):
    b = b or a
    span = f"L{a}" if a == b else f"L{a}-L{b}"
    r = {
        "id": rid(span),
        "id_recipe": 'sha256("survey-rec|" + file-basename-without-extension + "|" + source_span) hex, first 16 chars',
        "schema_version": "0.9" if revises else "0.7",
        "record_type": type,
        "surveyor": SURVEYOR,
        "source_file": "sonnet-survey-4.md",
        "source_span": span,
        "lineage": lineage,
        "note_verbatim": span_text(a, b),
    }
    if glyphs is not None:
        r["glyphs"] = glyphs
        r["codepoints"] = cps(glyphs)
    if direction is not None: r["direction_note"] = direction
    if axis is not None: r["axis"] = axis
    r["constructed"] = constructed
    ep = {
        "epistemic_class": "interactive-guided-survey-anecdote",
        "felt_strength_verbatim": strength if strength is not None else "unstated",
        "basis": basis,
        "marked_speculative": spec,
    }
    if immediacy is not None: ep["felt_immediacy_verbatim"] = immediacy
    # This surveyor SELF-DEFINED strength 1-5 as predicted pairwise-judge recoverability (preamble, L3),
    # so their strength scale is natively in the prediction register (v0.7 adjudication): populate both.
    pg = []
    if strength is not None and "strength" in strength.lower():
        pg.append(strength + " — the surveyor's strength scale, self-defined (L3) as confidence a pairwise "
                             "'which is more' judge would recover the order; prediction register by their own definition")
    if predgen is not None:
        pg.append(predgen)
    if pg: ep["predicted_generalization"] = " | ".join(pg)
    ep["transcription_confidence"] = tc
    if mnotes: ep["migrator_notes"] = mnotes
    r["epistemics"] = ep
    if revises:  # v0.9: list of {"id", "revision_kind", "revises_span"}
        r["revises"] = [{"id": rid(sp), "revision_kind": k, "revises_span": sp} for sp, k in revises]
    if negkind: r["negative_kind"] = negkind
    if scope: r["scope"] = scope
    if falsifier: r["falsifier_implied"] = falsifier
    if tested is not None: r["tested_instance"] = tested
    if settle: r["what_would_settle_it"] = settle
    if open_: r["open"] = open_
    if extra: r.update(extra)
    records.append(r)

JN = ("This item was anticipated/flagged in the one-shot brief (surveyor references Joseph's expectation) — "
      "lineage 'brief-steered' per schema v0.7 (brief-supplied priming, not mid-survey steering).")
IMM = ("Surveyor uses a two-axis calibration vocabulary: numeric strength 1-5 (defined in their preamble as "
       "confidence a pairwise 'which is more' judge would recover the order) plus an immediacy axis "
       "(PERCEPT/SYMBOLIC with graded intermediates). Immediacy kept verbatim in immediacy_verbatim; "
       "basis is the migrator's conservative mapping of it.")

# --- Preamble / methodology ---
rec(3, type="meta", axis=None, tc="clear",
    scope="whole survey — surveyor's own notation and calibration definitions",
    mnotes="Surveyor's self-defined calibration system: strength 1-5 = predicted pairwise-judge recoverability "
           "(natively the prediction register — per v0.7 adjudication, records carry it verbatim AND in predicted_generalization); "
           "immediacy PERCEPT/SYMBOLIC = whether magnitude is visible in shape vs arrives via digit/letter lookup (felt_immediacy_verbatim).")

# --- Enclosed Alphanumerics ---
rec(9, type="sequence", glyphs="①②③④⑤⑥⑦⑧⑨⑩", direction="↑", axis="Textbook ordinal count; magnitude is 100% digit-lookup",
    strength="strength 5", immediacy="SYMBOLIC", basis="semantic-knowledge", mnotes=IMM)
rec(10, type="sequence", glyphs="⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽", direction="↑", axis="Same as circled set, parenthesized; ordering carried entirely by the digit, not the enclosure style",
    strength="strength 5", immediacy="SYMBOLIC", basis="semantic-knowledge",
    open_="Carries an equivalence observation (no perceptual difference in strength from the circled set) inside a sequence record.")
rec(11, type="negative", glyphs="ⒶⒷⒸⓏ", axis="Alphabetic order reads as 'next,' not 'more' — sequence/ordering ≠ magnitude",
    strength="unstated (\"I don't feel a magnitude ladder here\")", basis="perceived-directly", negkind="verified-absent",
    mnotes="Glyphs field abbreviates the surveyor's 'Ⓐ Ⓑ Ⓒ … Ⓩ' (ellipsis in original). Also states a policy: "
           "purely-alphabetic/sequential non-quantity cases will be flagged as negatives rather than listed as hits.",
    tc="clear")
rec(12, type="sequence", glyphs="⓪①②③④⑤⑥⑦⑧⑨⑩", direction="↑", axis="[ordinal count, migrator gloss] the ⓪ (circled zero) plugged in front feels exactly as expected, no discontinuity",
    strength="strength 5", immediacy="SYMBOLIC", basis="semantic-knowledge")
rec(13, type="sequence", glyphs="⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾", direction="↑", axis="Same phenomenon; doubled ring reads as a distinguishing style for a second 1-10 series, not 'more'",
    strength="strength 5", immediacy="SYMBOLIC", basis="semantic-knowledge",
    open_="Embedded negative/meta observation: enclosure-style changes do not stack as magnitude (adjacent single- and double-circled series give two resets to 1, not a magnitude-20 ladder).")
rec(14, type="sequence", glyphs="⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴", direction="↑", axis="[ordinal count continuing 11-20, migrator gloss] the black-disc 'negative' rendering first reads as 'different category' before settling into continuing the ordinal count from 10",
    strength="strength 4, mild extra friction", immediacy="SYMBOLIC", basis="semantic-knowledge")
rec(16, type="meta", scope="U+2460–U+24FF Enclosed Alphanumerics pane, all entries",
    axis="None percept-immediate; magnitude signal 100% routed through recognizing the numeral",
    strength="unstated", tested=True,
    mnotes="Surveyor designates this pane as an anchor/contrast case: extremely strong ordering, zero immediacy.")

# --- Block Elements ---
rec(22, type="sequence", glyphs="▁▂▃▄▅▆▇█", direction="↑", axis="Height of black ink — magnitude literally is the bar height, read as directly as a bar chart",
    strength="strength 5", immediacy="PERCEPT (maximally so)", basis="perceived-directly",
    predgen="\"I'd bet this is the single strongest 'immediate' sequence I encounter in this whole survey\"")
rec(23, type="meta", scope="eighth-block set codepoint layout",
    axis="Codepoint-order oddity: ladder starts at U+2581, U+2580 UPPER HALF sits off to the side",
    strength="unstated", tested=True, tc="clear",
    revises=[("L22", "refinement")],
    mnotes="Glyphs '▔█▁' in the original line illustrate the oddity rather than a proposed sequence; recorded as meta not sequence. "
           "[Revision link migrator-inferred: 'the 1/8-through-8/8 ladder above is clean' explicitly qualifies the L22 record's ladder — a codepoint-layout caveat, not a change to its felt report.]")
rec(24, type="sequence", glyphs="░▒▓█", direction="↑", axis="Shading density — 'amount of ink per unit area', no height metaphor riding along",
    strength="strength 5", immediacy="PERCEPT", basis="perceived-directly",
    open_="Surveyor notes this and the bar-height ramp feel like two flavors of the same underlying axis (density) rather than independent finds.")
rec(25, type="sequence", glyphs="▏▎▍▌▋▊▉█", direction="↑", axis="Width-based fill (left-aligned); immediacy is about 'proportion of the glyph cell filled', independent of growth edge",
    strength="strength 5", immediacy="PERCEPT", basis="perceived-directly")
rec(26, type="sequence", glyphs="▖▗▘▝▚▞▙▛▜▟", direction="↑ by corner-count (1→2→3)", axis="Rough ordering by filled-corner count",
    strength="strength only ~2", immediacy="PERCEPT", basis="perceived-directly", spec=True,
    predgen="\"I could see a pairwise judge going either way on some pairs\"",
    mnotes="Glyphs list the three corner-count tiers the surveyor named; they note the two-corner diagonal cases don't sit unambiguously between 1 and 3. Noted by surveyor as a weak/partial find.")

# --- Geometric Shapes ---
rec(32, type="sequence", glyphs="○◔◑◕●", direction="↑", axis="Pie-chart fill ramp — circular fill fraction",
    strength="strength 5", immediacy="PERCEPT", basis="perceived-directly", lineage="brief-steered",
    mnotes=JN + " Scattered codepoints noted by surveyor (U+25CB, U+25D4, U+25D1, U+25D5, U+25CF).")
rec(33, type="sequence", glyphs="◌○◍◎●", direction="↑", axis="Looser fill-amount ladder; ◎ reads as 'circle-in-circle' (nestedness), a different concept fighting the ordering",
    strength="strength ~2-3 only", basis="perceived-directly",
    mnotes="Surveyor frames this as a weaker/messier neighbor of ○◔◑◕●, worth keeping separate. No immediacy label stated on this line; "
           "migrator inference (not transcription): the note reads as an implicit PERCEPT attempt.")
rec(34, type="sequence", glyphs="▫▪◽◾□■◻◼", direction="↑ by size (holding white/black color constant within each size tier)",
    axis="Magnitude-by-area: same-shape-different-size squares",
    strength="strength 4", immediacy="PERCEPT", basis="perceived-directly", constructed=True,
    tc="interpreted",
    mnotes="Hand-assembled by the surveyor from intermixed names (not a contiguous run); they flag that codepoint-adjacency "
           "and semantic-ladder-cleanliness are somewhat independent axes. Glyph ordering here follows their small→medium-small→plain→medium listing.")
rec(35, type="negative", glyphs="▱▰", axis="White/black parallelogram — only 2 points, not a real sequence",
    strength="unstated", basis="perceived-directly", negkind="declared-out-of-scope", tc="interpreted",
    mnotes="Exclusion reason is structural (too few points), not a felt-absence report — negative_kind is the migrator's nearest fit.")
rec(36, type="negative", glyphs="▵▴▹▸▿▾◃◂", axis="White→black fill on a single, already-small glyph reads as a state toggle (off/on), not 'more'",
    strength="unstated", basis="perceived-directly", negkind="verified-absent",
    open_="Contains a stated contrast law: fill-toggle on a constant-size shape does not read as magnitude; only fill-ramp (multiple intermediate steps) or size-change does.")
rec(37, type="negative", glyphs="▵▴▷▸▶", axis="Attempted size+fill+rotation combined ladder falls apart — too many simultaneously-varying dimensions, no clean order",
    strength="unstated", basis="constructed", negkind="verified-absent", constructed=True)
rec(38, type="cyclic", glyphs="◰◱◲◳", axis="Purely positional/rotational — same '1 quadrant filled' amount at every step, just rotated",
    strength="unstated", basis="perceived-directly",
    mnotes="Surveyor explicitly marks NOT a magnitude sequence and names it as a case superficially resembling the pie-slice fill sequence. Seen (not assumed).",
    extra={"equivalence_basis": "seen"})

# --- Miscellaneous Symbols ---
rec(44, type="sequence", glyphs="⚀⚁⚂⚃⚄⚅", direction="↑", axis="Pip count; internally-mixed immediacy — 1-3 pips subitize (percept-immediate), 4-6 require counting",
    strength="strength 5", immediacy="mixed immediacy", basis="perceived-directly", lineage="brief-steered",
    mnotes=JN)
rec(45, type="negative", glyphs="☰☱☲☳☴☵☶☷", axis="No monotonic magnitude feeling in codepoint order; trigram value needs conscious 3-bit decoding, and Unicode order isn't binary-value order anyway",
    strength="unstated (\"NOT a strong monotonic magnitude sequence for me as given\")",
    basis=["perceived-directly", "semantic-knowledge"],
    negkind="verified-absent", tested=True, lineage="brief-steered",
    mnotes=JN + " Surveyor checked ☰=111/☷=000 endpoints and the non-binary middle ordering. "
           "Ordered basis list (v0.7): the negative report is direct perception failing, first; the decoding that WOULD order it is semantic-knowledge, second.",
    open_="Surveyor notes a binary-value-sorted rearrangement would feel monotonic once decoded, but that would be re-imposing an order, not perceiving one.")
rec(46, type="negative", glyphs="⚌⚍⚎⚏", axis="Digrams: non-monotonic naming, no immediate line-count cue; no magnitude feel",
    strength="unstated", basis="perceived-directly", negkind="verified-absent")
rec(47, type="negative", glyphs="⚊⚋", axis="Monogram yang/yin — reads as binary state, not magnitude; just 2 items",
    strength="unstated", basis="perceived-directly", negkind="not-felt")
rec(48, type="sequence", glyphs="⚆⚇⚈⚉", direction="↑ dot-count within each color pair", axis="Dot-count within pair; the two colors don't chain (white-2-dots vs black-1-dot don't compare cleanly)",
    strength="strength 3", immediacy="borderline PERCEPT/SYMBOLIC ... calling it soft-PERCEPT", basis="perceived-directly",
    mnotes="Two 2-glyph sub-sequences (⚆⚇ and ⚈⚉), recorded together per the surveyor's within-pair framing; NOT one 4-long sequence.")
rec(49, type="negative", glyphs="⚪⚫⚬", axis="Size cue real but confounded with black/white flip — can't tell if 'more' means bigger or blacker",
    strength="unstated", basis="perceived-directly", negkind="verified-absent")
rec(50, type="sequence", glyphs="♩♪♫♬", direction="↑", axis="'More notes/faster subdivision' — semantic ladder with a genuine visual 'more ink/more beams' component",
    strength="strength 3 ... Moderate confidence", immediacy="PERCEPT-leaning-SYMBOLIC",
    basis=["semantic-knowledge", "perceived-directly"],
    mnotes="Ordered basis list (v0.7), explicitly mixed in source: musical-notation literacy needed for 'faster' (primary), beam-count visible without training (secondary).")
rec(51, type="sequence", glyphs="♳♴♵♶♷♸♹", direction="↑", axis="Plastics type 1-7 — pure digit-in-triangle lookup, no visual growth",
    strength="strength 4", immediacy="SYMBOLIC", basis="semantic-knowledge")

# --- Number Forms ---
rec(54, type="sequence", glyphs="ⅠⅡⅢⅣⅤ", direction="↑", axis="Stroke-count subitizing for Ⅰ-Ⅲ; Ⅳ breaks immediacy hard (visually shorter than Ⅲ despite being 'more' — a real perceptual anti-cue)",
    strength="strength 3 (Ⅰ-Ⅲ alone); as a whole strength drops to ~2", immediacy="PERCEPT for a prefix, then flips to SYMBOLIC/anti-cue partway through",
    basis=["perceived-directly", "semantic-knowledge"],
    mnotes="Ordered basis list (v0.7): perceived-directly for the Ⅰ-Ⅲ prefix, semantic-knowledge for the subtractive convention from Ⅳ on — "
           "the 'immediacy cliff' case; per-position variation noted here per v0.6.",
    open_="Surveyor names this a texture not seen elsewhere: percept-for-a-prefix sequences.")
rec(55, type="sequence", glyphs="ⅠⅤⅩⅬⅭⅮⅯ", direction="↑", axis="Roman numeral values 1-1000; no shape-scaling at all (Ⅽ isn't bigger than Ⅹ)",
    strength="strength 4 only if you know Roman numerals", immediacy="pure SYMBOLIC/LEARNED", basis="semantic-knowledge")
rec(56, type="sequence", glyphs="⅛⅕⅓⅜⅗⅔⅘⅚⅞", axis="Numeric-value ordering requiring per-glyph division; zero shape-based cue",
    strength="strength only ~2", immediacy="SYMBOLIC", basis="semantic-knowledge", constructed=True,
    predgen="\"a pairwise judge would likely be slow/inconsistent on the close ones\"",
    tc="interpreted",
    mnotes="Glyphs list the fraction glyphs the surveyor named as present; their line also inventories absent vulgar fractions (¼, ½, ¾ noted 'absent'). "
           "No direction arrow stated on the line; ascending-by-numeric-value ordering is the migrator's reading of 'I can construct a numeric-value ordering'. Not a strong find, per surveyor.")
rec(58, type="meta", scope="survey file structure / surveying practice",
    axis="Append-only working policy stated: chess finding belongs with the Misc Symbols pane but was appended out of order; note left rather than reshuffling",
    strength="unstated", tc="clear")
rec(60, type="sequence", glyphs="♙♘♗♖♕♔", axis="Learned/domain-semantic value ladder (game value: 1,3,3,5,9,∞); nothing in the shapes signals 'more'",
    strength="strength 4 for someone who knows chess, ~1 for a naive viewer", immediacy="SEMANTIC/LEARNED",
    basis="semantic-knowledge",
    mnotes="Surveyor coins a third immediacy category here (SEMANTIC/LEARNED, beyond PERCEPT/SYMBOLIC-numeral) — kept verbatim in felt_immediacy_verbatim per v0.7 (unification is pass-2). "
           "No direction arrow stated on the line; pawn→king listing order is ascending by the game values the surveyor gives (migrator reading).")

# --- Arrows ---
rec(66, type="sequence", glyphs="→⇒⇛", direction="↑", axis="Shaft-stroke count directly visible (1/2/3) — 'more strokes = more', like an intensity gauge",
    strength="strength 5", immediacy="PERCEPT", basis="perceived-directly",
    mnotes="Surveyor notes kinship with the block-fill family despite different shape; scattered codepoints U+2192, U+21D2, U+21DB.")
rec(67, type="question", glyphs="⇉⇒", axis="Both read as 'more than →', but which is more between them is genuinely ambiguous (parallel-count vs stroke-thickness are different magnitude metaphors that don't reduce to each other)",
    strength="genuinely ambiguous — flagging as an honest ambiguity rather than forcing an order", basis="perceived-directly",
    settle="(migrator inference, not surveyor-stated) A pairwise 'which is more' comparison of ⇉ vs ⇒ across fresh judges would settle whether one metaphor dominates.")
rec(68, type="negative", glyphs="←↚⇍", axis="Stroke reads as a negation marker ('not left'), not an amount; doesn't compose with the double-arrow",
    strength="unstated", basis="perceived-directly", negkind="verified-absent")
rec(69, type="sequence", glyphs="↑⇑", direction="↑", axis="Same PERCEPT double-stroke cue as the rightwards pair",
    strength="strength 4 standing alone, but only 2 points here", immediacy="PERCEPT", basis="perceived-directly",
    open_="No triple-up glyph in this block; weaker as a full sequence than →⇒⇛.")

# --- Mathematical Operators ---
rec(75, type="sequence", glyphs="∫∬∭", direction="↑", axis="Count of ∫ strokes directly visible and subitizable at 1-3 — 'more of the same mark stacked'",
    strength="strength 5", immediacy="PERCEPT", basis="perceived-directly")
rec(76, type="sequence", glyphs="∮∯∰", direction="↑", axis="Same mechanism as ∫∬∭, with the circle",
    strength="strength 5", immediacy="PERCEPT", basis="perceived-directly")
rec(77, type="sequence", glyphs="<≪⋘", direction="↑", axis="Chevron-count ladder (1/2/3) — 'more extreme'; cross-block find starting in ASCII",
    strength="strength 4 (for the 2-chevron ≪ vs single < stage), then strength 5 for the full <(1)→≪(2)→⋘(3) ladder", immediacy="PERCEPT", basis="perceived-directly",
    mnotes="Surveyor's line narrates discovery in two stages; both stated strengths carried. Codepoints U+003C, U+226A, U+22D8. "
           "The line also opens by mentioning the pair ≤≦, which the surveyor never returns to with any ordering claim — it has no record of its own; this note is its addressable trace.")
rec(78, type="sequence", glyphs="√∛∜", direction="↑ by root-degree (index digit)", axis="Root index — but 'more' is genuinely ambiguous: higher root-degree means smaller output for x>1, so which real quantity is intended can flip the felt direction",
    strength="strength 3", immediacy="NOT strongly immediate, calling it SYMBOLIC", basis="semantic-knowledge",
    open_="Surveyor flags this as an instructive edge case for the 'more is whatever the sequence makes obvious' instruction — here it is genuinely NOT obvious which of two real quantities (index vs output size) is intended.")
rec(79, type="negative", glyphs="⊂⊆⊊", axis="Read as different logical relations, not points on a 'more' scale",
    strength="unstated", basis="semantic-knowledge", negkind="verified-absent")
rec(80, type="negative", glyphs="∀∃", axis="No magnitude at all, purely logical quantifiers",
    strength="unstated", basis="semantic-knowledge", negkind="not-felt",
    mnotes="Volunteered as a preemptive non-example: 'someone might reach for them'.")

# --- Braille ---
rec(86, type="sequence", glyphs="⠀⠁⠃⠇⠏⠟⠿⣿", direction="↑", axis="Dot-count fill ramp — a 'braille sparkline'; amount of visible ink increases monotonically, read as a density gauge with no braille literacy needed",
    strength="strength 5", immediacy="PERCEPT", basis="perceived-directly",
    tc="clear", lineage="brief-steered",
    mnotes=JN + " Surveyor self-flags: medium confidence on the EXACT intermediate codepoints typed vs high confidence on the phenomenon "
           "('let me not overclaim the exact intermediate codepoints, the visual ramp is what I'm reporting'). Codepoints here are of the glyphs as typed in the survey, not a verified byte-exact ladder.",
    extra={"rule_confidence_note": "high confidence on the phenomenon (dot-count as percept-immediate density ramp); medium confidence on the exact example chain — surveyor's own split."})
rec(87, type="negative", axis="Same dot-count, different dot-positions (e.g. dots-14 vs dots-23): no ordering at all, purely positional variety",
    strength="unstated", basis="perceived-directly", negkind="verified-absent",
    mnotes="No concrete glyphs given in the note (described by dot-pattern names). Important negative per surveyor: the ramp only works with a deliberately monotonically-growing dot subset.")

# --- Miscellaneous Technical ---
rec(93, type="sequence", glyphs="⏑⏗⏘⏙", direction="↑", axis="Visible arc/hump count (1,3,4,5 morae) — count visible without knowing 'mora', but requires counting rather than gauging a fill level",
    strength="strength 3", immediacy="borderline PERCEPT ... PERCEPT-leaning-SYMBOLIC", basis="perceived-directly",
    mnotes="Surveyor highlights it as a scattered/obscure find (U+23D1, U+23D7, U+23D8, U+23D9) found only by going pane-by-pane.")
rec(94, type="cyclic", glyphs="⏴⏵⏶⏷", axis="Purely directional (media transport buttons) — explicit non-example",
    strength="unstated", basis="perceived-directly",
    extra={"equivalence_basis": "seen"},
    mnotes="Typed cyclic (directional-without-magnitude) per schema type 4; surveyor's own label is 'explicit non-example'.")
rec(95, type="sequence", glyphs="▶⏩", axis="'double triangle = faster/more' via UI convention (2x speed) [▶(1x)→⏩(2x) ascending per the surveyor's own labeling; no arrow stated — migrator reading]",
    strength="strength 3", immediacy="SEMANTIC-leaning (you need the media-player convention, but the doubling itself is visually obvious once you have it)",
    basis="semantic-knowledge", constructed=True,
    open_="Cross-block construction (▶ from Geometric Shapes, ⏩ this block); no clean 3x glyph found nearby.")
rec(96, type="negative", glyphs="⎺⎻⎼⎽", axis="Encodes vertical position within a cell, not amount — tempting to read as a descending ladder but it's about where a line sits",
    strength="\"I don't trust my own instinct here enough to call it a strong magnitude finding\"", basis="perceived-directly",
    negkind="not-felt", spec=True, tc="interpreted",
    mnotes="Surveyor marks it 'ambiguous/likely-negative' — a hedged negative, not a verified one. Borderline question-type record (the surveyor's distrust of their own instinct is part of the content); typed negative per their own lean — adjudication welcome.")

# --- Domino Tiles ---
rec(102, type="sequence", glyphs="🀱🀲🀳🀴🀵🀶🀷", direction="↑", axis="One half fixed at blank, other half's pip-count climbing; mixed immediacy like dice (0-2 pips subitize, 3-6 need counting)",
    strength="strength 4", immediacy="mixed immediacy like the dice case", basis="perceived-directly",
    predgen="\"I'm now fairly confident this 'subitize-then-count' split at ~3 pips is a real recurring boundary in my own perception, not a one-off\"",
    revises=[("L44", "confirmation")],
    open_="Contains a stated generalization the surveyor adopts going forward (treating the ~3-pip subitizing boundary as a general pattern rather than re-deriving per pane) — meta content inside a sequence record. "
          "[Revision link migrator-inferred from 'Same texture as ⚀-⚅'. Kind is a judgment call: dominant relation is confirmation (the dice split replicated in a second glyph family), with a refinement tint — the replication is what licenses the surveyor's promotion from one-off to recurring boundary.]")
rec(103, type="sequence", glyphs="🀱🀹🁁", direction="↑ by total pip count (0,2,4,6,...)", axis="Diagonal doubles ladder; each tile must be parsed as two halves and summed — a step slower than the single-half ramp",
    strength="strength 3", basis="perceived-directly",
    tc="interpreted",
    mnotes="Surveyor's line gives '🀱(0-0) 🀹(1-1) 🁁(2-2) 🁉... (3-3) ...' with ellipses; glyphs field carries the concretely-typed prefix only. Noted by surveyor as a weaker cousin. "
           "No immediacy label stated; migrator inference (not transcription): the 'step slower' remark implies slower-than-PERCEPT.")

# --- Dingbats ---
rec(109, type="sequence", glyphs="✶✴✹", direction="↑", axis="Point-count / gestalt 'spikiness/density' read — 'more spiky' at a glance without deliberate counting",
    strength="strength 3", immediacy="PERCEPT-leaning but not fully immediate", basis="perceived-directly",
    mnotes="Scattered codepoints (U+2736, U+2734, U+2739); surveyor found them only by hunting 'star' names specifically — a name-search discovery path, though the ordering feel itself is visual.")
rec(110, type="negative", glyphs="✩✫✬✭✮", axis="Variation is in style (outline weight, fill pattern), not any count or size — no magnitude feel despite looking like a natural 'star gallery'",
    strength="unstated", basis="perceived-directly", negkind="verified-absent",
    mnotes="Surveyor names it worth flagging because on first glance it looks like exactly the kind of run the brief asks for.")
rec(111, type="sequence", glyphs="➙➔➡", direction="↑", axis="Boldness/weight ordering (thin→thick→solid reads as 'more emphatic')",
    strength="strength 2 — genuinely unsure a pairwise judge would be consistent", immediacy="PERCEPT-ish", basis="perceived-directly", spec=True,
    predgen="\"genuinely unsure a pairwise judge would be consistent since 'wide-headed' vs 'black filled' trade off two different visual dimensions\"")

# --- Moon Phases ---
rec(117, type="sequence", glyphs="🌑🌒🌓🌔🌕", direction="↑", axis="Illuminated fraction — visually obvious AND semantically pre-loaded (real physical phenomenon everyone has observed)",
    strength="strength 5", immediacy="PERCEPT, maximally so", basis="perceived-directly", lineage="brief-steered",
    mnotes=JN + " Surveyor notes contiguous codepoints U+1F311-U+1F315, a contrast with most of their other finds being scattered.")
rec(118, type="cyclic", glyphs="🌖🌗🌘", axis="Full 8-phase cycle 🌑→🌕→🌑 is NOT monotonic — goes up then back down; only the new→full half is a clean monotonic ramp",
    strength="unstated", basis="perceived-directly",
    extra={"equivalence_basis": "seen"},
    mnotes="Glyphs field carries only the waning trio typed on this line; the record's subject is the full 8-phase cycle formed with rec L117's 🌑-🌕. "
           "Explicit warning record: 'moon phases' proposed as a full-cycle answer would be wrong per the brief's monotonicity requirement.")

# --- Closing reflections ---
rec(124, type="meta", scope="survey coverage",
    axis="Explicit incompleteness declaration: panes covered enumerated; unexplored panes named (Supplemental Arrows-A/B/C, Supplemental Math A/B, Misc Symbols and Arrows, Playing Cards, Mahjong, CJK punctuation, Mathematical Alphanumeric Symbols, more Supplemental Symbols and Pictographs)",
    strength="unstated")
rec(126, type="meta", scope="all PERCEPT-strong finds in this survey (block bars, shading, pie circles, moon phases, chevron-count, arrow stroke-count); all digit/numeral-based sequences; dice and dominoes",
    axis="Stated laws: (1) strongest PERCEPT finds share one mechanism — 'amount of ink/lines visible' — regardless of shape family; (2) digit/numeral sequences are strong orderings but never immediate, no matter how visually clean the enclosure; (3) the ~3-pip subitizing ceiling is a real, generalizable boundary rather than a fluke of any one glyph set",
    strength="\"I now think that 3-pip subitizing ceiling is a real, generalizable boundary\"", tested=True,
    falsifier="A digit-based sequence that reads as percept-immediate, or an ink-amount ramp that fails to; a pip/dot set where subitizing extends well past 3 or fails below it.",
    revises=[("L102", "refinement")],
    mnotes="The surveyor's own cross-pane synthesis; the immediacy question 'cut across shape-families more than I expected going in'. "
           "[Revision link migrator-inferred: third and strongest statement of the subitizing-boundary arc (L44 observation → L102 confirmed recurring pattern → here 'a real, generalizable boundary rather than a fluke of any one glyph set'). "
           "Kind refinement, not confirmation: no new replication data here — it consolidates and generalizes the already-confirmed pattern.]")
rec(128, type="meta", scope="name/history-suggested sequences (eight trigrams, chess pieces by value, subset relations)",
    axis="Stated distinction the surveyor held to: 'I can construct a valid ordering' vs 'this reads as monotonic to me on sight' — knowledge-only orderings carried no perceptual 'more' despite expectation",
    strength="unstated", tested=True)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"{len(records)} records -> {OUT}")
from collections import Counter
print(Counter(r["record_type"] for r in records))
