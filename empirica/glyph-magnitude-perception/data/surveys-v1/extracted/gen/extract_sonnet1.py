#!/usr/bin/env python3
# Pass-1 migration: sonnet-survey-1.md -> extracted/sonnet-survey-1.jsonl
# note_verbatim is sliced from the source file by line range (1-based, inclusive),
# so the primary text is carried mechanically, never retyped.
import hashlib, json, unicodedata, os

BASE = "/Users/josephwecker-v2/src/arch/asf/empirica/glyph-magnitude-perception/data/surveys-v1"
SRC = os.path.join(BASE, "sonnet-survey-1.md")
OUT = os.path.join(BASE, "extracted", "sonnet-survey-1.jsonl")
SURVEYOR = "sonnet-survey-1"

lines = open(SRC, encoding="utf-8").read().split("\n")

def span_text(span):
    a, b = (span.split("-") + [span])[:2] if "-" in span else (span, span)
    return "\n".join(lines[int(a)-1:int(b)])

def cps(glyphs):
    return ["U+%04X" % ord(c) for c in unicodedata.normalize("NFC", glyphs) if not c.isspace()]

def rid(span):
    return hashlib.sha256(("survey-rec|%s|%s" % (SURVEYOR, span)).encode()).hexdigest()[:16]

def rec(type_, span, **kw):
    r = {
        "schema_version": kw.pop("schema_version", "0.7"),
        "id_recipe": "sha256(\"survey-rec|\" + <file-basename-without-extension> + \"|\" + source_span) hex, first 16 chars",
        "id": rid(span),
        "type": type_,
        "surveyor": SURVEYOR,
        "source_file": "sonnet-survey-1.md",
        "source_span": span,
        "epistemic_class": "interactive-guided-survey-anecdote",
        "lineage": kw.pop("lineage", "unprompted"),
        "note_verbatim": span_text(kw.pop("note_span", span)),
        "felt_strength_verbatim": kw.pop("felt", "unstated"),
        "basis": kw.pop("basis", "unstated"),
        "transcription_confidence": kw.pop("tc", "clear"),
    }
    if "felt_immediacy_verbatim" in kw:
        r["lineage"] = "brief-steered"
    g = kw.pop("glyphs", None)
    if g is not None:
        r["glyphs"] = g
        r["codepoints"] = cps(g)
    for k in ("direction_note", "axis", "predicted_generalization", "marked_speculative",
              "constructed", "negative_kind", "migrator_notes", "open",
              "felt_immediacy_verbatim", "tie_groups", "roles", "meta_kind", "lineage",
              "revises", "schema_version"):
        if k in kw:
            r[k] = kw.pop(k)
    assert not kw, kw
    return r

R = []

# --- Preamble: surveyor's own calibration vocabulary (meta) ---
R.append(rec("meta", "1-11", lineage="brief-steered",
    axis="surveyor defines two axes for the whole survey: 'Strength = my honest confidence that a pairwise \"which is more?\" would recover this order' and 'immediacy: does the magnitude arrive in the percept itself ... or does it require a symbol lookup'",
    migrator_notes="Extraction-wide conventions: (1) sub-span disambiguation — where one source section yields N records, each record's source_span is the precise line(s) of its own chain/claim (e.g. 40 vs 41), a deterministic sub-line marker per schema v0.6; note_verbatim still carries the whole section. (2) lineage: findings are unprompted; the immediacy AXIS was supplied by the surveyor's brief, so records that EXERCISE the brief-installed immediacy axis (the two immediacy-register metas plus every record carrying felt_immediacy_verbatim) are lineage brief-steered per the ratified survey-2 precedent; pure glyph-findings without immediacy content stay unprompted. The glyph finding itself is unprompted even in brief-steered records — lineage scopes the record; sequence independence is the harness's to measure. This preamble defines the strength+immediacy vocabulary every subsequent record uses; it is the key to reading felt_strength_verbatim fields in this file. Immediacy closely parallels the schema's `basis` enum (perceived-directly vs semantic-knowledge) but as a graded, per-item axis — flagged as a schema question."))

# --- Geometric Shapes ---
R.append(rec("sequence", "16-27", glyphs="○◔◑◕●",
    direction_note="○ → ◔ → ◑ → ◕ → ●",
    axis="literal pie-chart / battery-level gauge; how much of the disc is filled",
    felt="Strength: very high, this would survive almost any pairwise ordering task",
    felt_immediacy_verbatim="Immediacy: very high — I don't decode a symbol, I just *see* how much of the disc is filled, the same way I'd read a loading spinner",
    basis="perceived-directly", constructed=False,
    predicted_generalization="would survive almost any pairwise ordering task"))

R.append(rec("equivalence", "24-27", glyphs="◐◑", note_span="16-27",
    axis="same magnitude (50%) with different orientation; 'my magnitude sense is insensitive to which side is filled, only how much'",
    felt="I don't feel an ordering between them, they're a tie",
    basis="perceived-directly", constructed=False,
    migrator_notes="Seen, not assumed — surveyor explicitly probed the pair. Embedded inside the circle-fill-ramp section; note_verbatim is the whole section."))

R.append(rec("sequence", "29-37", glyphs="◌○◎◉●",
    direction_note="◌ → ○ → ◎ → ◉ → ●",
    axis="density/solidity increasing; blending 'how much ink' with 'how continuous the ink is'",
    felt="Strength: medium-high",
    felt_immediacy_verbatim="Immediacy: high but slightly more effortful than the fill ramp — I'm integrating over ink-density rather than reading a single clean gauge",
    basis="perceived-directly", constructed=False))

R.append(rec("sequence", "40", glyphs="▫◽◻□", note_span="39-44",
    direction_note="▫ → ◽ → ◻ → □ (white, small → small → medium → full-size)",
    axis="pure size/area magnitude; 'which glyph looks bigger'",
    felt="Strength: high",
    felt_immediacy_verbatim="extremely immediate — literally 'which glyph looks bigger' ... about as close to a physical-magnitude percept as text gets",
    basis="perceived-directly", constructed=False,
    migrator_notes="Section 39-44 carries two parallel ladders (white/black); split into two records with the chain's own line as span so ids stay distinct; note_verbatim is the whole section for both."))

R.append(rec("sequence", "41", glyphs="▪◾◼■", note_span="39-44",
    direction_note="▪ → ◾ → ◼ → ■ (black, same size ladder)",
    axis="pure size/area magnitude; 'which glyph looks bigger'",
    felt="Strength: high",
    felt_immediacy_verbatim="extremely immediate",
    basis="perceived-directly", constructed=False,
    migrator_notes="Black twin of the white square size ladder (span 40); see that record's note."))

R.append(rec("sequence", "47", glyphs="▵△", note_span="46-51",
    direction_note="▵ → △ (white small-up-triangle → white up-triangle)",
    axis="same size-magnitude logic as squares, just two rungs instead of four",
    felt="Strength: high but shorter ladder = less impressive as a sequence",
    felt_immediacy_verbatim="Immediacy: high",
    basis="perceived-directly", constructed=False,
    migrator_notes="Section 46-51 carries two parallel two-rung ladders; split as with the squares."))

R.append(rec("sequence", "48", glyphs="▴▲", note_span="46-51",
    direction_note="▴ → ▲ (black small → black)",
    axis="same size-magnitude logic as squares",
    felt="Strength: high but shorter ladder = less impressive as a sequence",
    felt_immediacy_verbatim="Immediacy: high",
    basis="perceived-directly", constructed=False))

R.append(rec("sequence", "53-63", glyphs="□▤▦◫▩■",
    direction_note="□ → ▤ (or ▥, tied) → ▦ → ◫(bisected, ~50%, tie-ish with ▦) → ▩ → ■",
    tie_groups=[["▤","▥"],["◫","▦"]],
    axis="ink density; 'composite/soft feel, more \"ink density\" than a clean percept'",
    felt="Strength: medium-low, this is a composite/soft feel. 'Flagging low confidence rather than omitting.' 'This one I'm *not* confident about as a magnitude ladder.'",
    basis="perceived-directly", constructed=True, marked_speculative=True, tc="interpreted",
    migrator_notes="Surveyor assembled the claimed ladder (including ◫ from outside the strict ▤-▩ run) after rejecting the raw series as monotonic — hence constructed=true. glyphs field takes one representative of each tie group per the surveyor's own chain; tie structure is in direction_note and the ▤/▥ equivalence record (span 57-60).",
    open="Internal ties (▤/▥; ◫ 'tie-ish' with ▦) make this a partial order, not a chain; ▧▨ appear in the section header but not in the claimed ladder."))

R.append(rec("equivalence", "57-60", glyphs="▤▥", note_span="53-63",
    axis="'the two single-direction hatches (▤ vs ▥) don't order against each other, they're a tie (orientation, not magnitude, differs)'",
    felt="they don't order against each other, they're a tie",
    basis="perceived-directly", constructed=False,
    migrator_notes="Seen (probed), not assumed. Embedded in the fill-pattern section."))

# --- Miscellaneous Symbols ---
R.append(rec("sequence", "69-78", glyphs="⚀⚁⚂⚃⚄⚅",
    direction_note="⚀ → ⚁ → ⚂ → ⚃ → ⚄ → ⚅",
    axis="count magnitude via subitizing pips; 'the dots are literally countable objects in the glyph, not an arbitrary shape that denotes a number by convention'",
    felt="Strength: very high, essentially unimpeachable",
    felt_immediacy_verbatim="Immediacy: very high — I see the dot count directly, no lookup",
    basis="perceived-directly", constructed=False,
    migrator_notes="Note references the brief's framing twice ('Exactly the one Joseph predicted I'd predict'; 'the immediacy distinction Joseph asked me to watch for') — these refer to the one-shot brief, not a mid-survey intervention, so lineage stays unprompted."))

R.append(rec("negative", "80-85", glyphs="☽☾",
    axis="moon phase (first/last quarter) — as a pair alone, no felt ordering",
    felt="strength low (not really an 'ordering,' just two shapes); 'a weak ladder here'",
    basis="perceived-directly", negative_kind="not-felt", constructed=False,
    migrator_notes="Borderline typing (verifier-prompted retype from sequence): surveyor frames the section as a candidate ladder but reports no asserted order and gives no direction — 'not really an ordering, just two shapes' reads as an absence-of-feel report for the pair, so negative/not-felt.",
    open="Surveyor deliberately did not chase the fuller moon-phase set in other blocks this pass ('possibly in Miscellaneous Symbols and Pictographs')."))

R.append(rec("sequence", "88", glyphs="⚆⚇", note_span="87-95",
    direction_note="⚆ (white, 1 dot) → ⚇ (white, 2 dots)",
    axis="dot-count ordering within the white pair (subitizing)",
    felt="feels real and immediate ... Strength: medium for the two 2-item sub-ladders",
    basis="perceived-directly", constructed=False))

R.append(rec("sequence", "89", glyphs="⚈⚉", note_span="87-95",
    direction_note="⚈ (black, 1 dot) → ⚉ (black, 2 dots)",
    axis="dot-count ordering within the black pair (subitizing)",
    felt="feels real and immediate ... Strength: medium for the two 2-item sub-ladders",
    basis="perceived-directly", constructed=False))

R.append(rec("negative", "87-95", glyphs="⚆⚇⚈⚉",
    axis="no unified 4-item chain: 'fill-color and dot-count are pulling in ways that don't resolve to one axis'",
    felt="I don't get a clean feel for whether ⚇ (white, 2 dots) is 'more' or 'less' than ⚈ (black, 1 dot); Strength: ... low/absent for a unified 4-item chain",
    basis="perceived-directly", negative_kind="verified-absent", constructed=False,
    migrator_notes="verified-absent: surveyor actively tried to fuse the sub-ladders and reported the failure, not a passing impression."))

R.append(rec("negative", "97-108", glyphs="⚊⚋⚌⚍⚎⚏",
    axis="digrams encode a genuine philosophical intensity ordering (greater > lesser) but 'that ordering does not arrive in the percept'; monograms are 'a binary, not a magnitude'",
    felt="Strength (of the semantic ordering, if you already know the convention): medium; strength of *perceptual* ordering without that knowledge: near zero",
    felt_immediacy_verbatim="Immediacy: low, this is a pure symbol-lookup case, a useful contrast item precisely *because* it fails the immediacy test despite having a real denoted magnitude",
    basis="semantic-knowledge", negative_kind="verified-absent", constructed=False,
    predicted_generalization="I'd guess this is a case Joseph specifically wants flagged as a negative/contrast example",
    migrator_notes="Surveyor volunteers this as a negative/contrast example for perceptual magnitude while affirming the semantic ordering — a two-layer record: real denoted magnitude, absent percept. The dual strength report (semantic medium / perceptual near zero) is kept whole in felt_strength_verbatim."))

R.append(rec("sequence", "110-118", roles=["sequence","contrast-case"], glyphs="♙♘♗♖♕♔",
    direction_note="Pawn < knight≈bishop < rook < queen < king by conventional piece value [white set; surveyor gives black set ♟♞♝♜♛♚ with the same rank]",
    tie_groups=[["♘","♗"]],
    axis="conventional chess piece value; 'not a clean single-file chain — it's more a partial order'",
    felt="Strength: medium for someone who knows chess, ~zero otherwise — flagging as another good immediacy-contrast case",
    felt_immediacy_verbatim="Immediacy: low, entirely dependent on knowing chess piece values, nothing in the glyph shapes themselves suggests relative worth",
    basis="semantic-knowledge", constructed=True, tc="interpreted",
    migrator_notes="constructed=true: ladder assembled from piece-value knowledge, not a visual family order. Surveyor gives both color sets; glyphs field carries the white set, black set in direction_note. Caution for mechanical consumers: the glyphs string linearizes ♘ before ♗ though the surveyor asserts knight≈bishop as a TIE — the string over-asserts a chain the surveyor refused; direction_note/open carry the true partial order.",
    open="knight/bishop tie (~3) breaks single-file ordering; 'nothing in the glyph shapes themselves suggests relative worth'."))

R.append(rec("sequence", "120-124", glyphs="⚬⚪⚫",
    direction_note="If I had to force an order by size alone: ⚬ → ⚪/⚫(tie)",
    tie_groups=[["⚪","⚫"]],
    axis="size only; ⚪ vs ⚫ is 'fill-only distinction, no magnitude order I can feel — tie'",
    felt="Weak, only two real size rungs",
    basis="perceived-directly", constructed=True, marked_speculative=True,
    migrator_notes="'If I had to force an order' — surveyor-assembled under protest; the ⚪/⚫ tie is an embedded equivalence kept here rather than split out, since the whole record is only three glyphs."))

# --- Block Elements ---
R.append(rec("sequence", "130-139", glyphs="▁▂▃▄▅▆▇█", note_span="130-145",
    direction_note="▁ → ▂ → ▃ → ▄ → ▅ → ▆ → ▇ → █",
    axis="bar-height percept, eighths of a block, bottom-anchored; 'the most direct \"more\" available in text' — 'reads exactly like a tiny bar chart because it functionally is one'",
    felt="Strength: about as close to certain as anything in this survey",
    felt_immediacy_verbatim="Immediacy: maximal — there's no decoding step whatsoever, it reads exactly like a tiny bar chart because it functionally is one",
    basis="perceived-directly", constructed=False,
    predicted_generalization="I'd expect this to survive not just pairwise but n-way sorting by a fresh viewer with zero explanation",
    schema_version="0.9",
    revises=[{"id": rid("16-27"), "revises_span": "16-27", "revision_kind": "refinement"}],
    migrator_notes="Surveyor ranks this 'the single best find of the whole pass so far' — [revision link migrator-inferred: the circle-fill record (span 16-27) had claimed 'the strongest single find so far'; this later append supersedes that title. The surveyor never references the earlier claim directly; both 'so far' markers are his own self-scoping, so read as refinement, not contradiction]."))

R.append(rec("sequence", "140-145", glyphs="▏▎▍▌▋▊▉█", note_span="130-145",
    direction_note="▏ → ▎ → ▍ → ▌ → ▋ → ▊ → ▉ → █ (mirror set on the left-anchor axis, filling left-to-right instead of bottom-to-top)",
    axis="fill direction rather than height; 'same strength, same immediacy'",
    felt="same strength [as the vertical bar set]",
    felt_immediacy_verbatim="same immediacy [as the vertical bar set]",
    basis="perceived-directly", constructed=False,
    open="Surveyor observation: both ladders share endpoint █ — 'the 8/8 rung of one axis is identical to the 8/8 rung of the other; they aren't in tension with each other perceptually.'"))

R.append(rec("sequence", "147-152", glyphs="░▒▓█",
    direction_note="░ → ▒ → ▓ → █ (light shade → medium shade → dark shade → full)",
    axis="fill-density via stipple density rather than geometric fraction; 'reads like a grayscale/opacity gradient'",
    felt="Strength: very high, only four rungs so less impressive as a sequence but I have no hesitation about the order",
    felt_immediacy_verbatim="Immediacy: very high, reads like a grayscale/opacity gradient",
    basis="perceived-directly", constructed=False))

R.append(rec("sequence", "154-168", roles=["sequence","contrast-case"], glyphs="▘▖▝▗▙▛▜▟",
    direction_note="1-corner(tie) → 3-corner(tie) is the only ladder-like feel I get, by popcount",
    tie_groups=[["▘","▖","▝","▗"],["▙","▛","▜","▟"]],
    axis="popcount of filled quadrants; underlying structure is 'combinatorial (position) rather than scalar (amount)'",
    felt="Strength: low-medium",
    felt_immediacy_verbatim="soft because I have to consciously count corners rather than perceiving 'more' pre-attentively — closer to symbol-lookup than the linear bars above",
    basis="perceived-directly", constructed=True, marked_speculative=True, tc="interpreted",
    migrator_notes="Surveyor frames this primarily as a contrast case ('fails to be a clean magnitude') yet claims a soft two-tier popcount ladder — recorded as sequence with the failure carried in axis/open; borderline sequence-vs-negative typing flagged back as a schema question. glyphs = the two tie groups (1-corner then 3-corner) in the surveyor's order; ▚▞ deemed ambiguous and excluded from the claimed ladder.",
    open="▚▞ (2 opposite corners) 'ambiguous against ones with 2 adjacent corners (there are none of those alone in this set)'; ties within each popcount tier (extracted as equivalence records at spans 157 and 160-161)."))

R.append(rec("equivalence", "157", glyphs="▘▖▝▗", note_span="154-168",
    axis="'Ones with 1 filled corner (▘▖▝▗) feel like a tied group'",
    felt="feel like a tied group",
    basis="perceived-directly", constructed=False,
    migrator_notes="Seen, not assumed — surveyor probed the whole quadrant set. Extracted from within the quadrant-popcount section (verifier-prompted, for consistency with the other probed-tie equivalence records); note_verbatim is the whole section."))

R.append(rec("equivalence", "160-161", glyphs="▙▛▜▟", note_span="154-168",
    axis="'ones with 3 filled corners (▙▛▜▟) feel like a tied \"almost full\" group'",
    felt="feel like a tied 'almost full' group",
    basis="perceived-directly", constructed=False,
    migrator_notes="Seen, not assumed. Companion to the 1-corner tie group (span 157)."))

# --- Superscripts and Subscripts ---
R.append(rec("sequence", "174-184", roles=["sequence","contrast-case"], glyphs="⁰⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉",
    direction_note="0 < 4 < 5 < ... < 9 [superscript run as present in block]; 'the subscript run is complete 0-9'",
    axis="memorized digit denotation; 'symbol-lookup, full stop' — 'nothing in the *shape* of ⁷ that is bigger, fuller, or more-of-anything than ⁴'",
    felt="Strength of the recovered order: very high (nobody would get 4 and 7 backwards)",
    felt_immediacy_verbatim="Immediacy: low. It is symbol-lookup, full stop, same cognitive move as reading normal-sized digits, just rendered smaller/raised",
    basis="semantic-knowledge", constructed=False, tc="interpreted",
    migrator_notes="Surveyor flags this explicitly as 'the clean negative/contrast case for immediacy' while the order itself is very high strength — typed sequence (an order IS asserted and recoverable), with the contrast role verbatim in axis. Two scripts (super+sub) kept as one record because the surveyor treats them as one verdict; superscript ¹²³ live outside this block and are absent from his listed run.",
    open="Good paired contrast against die faces / bar ramps: 'same strength of recoverable order, opposite mechanism.'"))

# --- Number Forms ---
R.append(rec("sequence", "190-203", roles=["sequence","contrast-case"], glyphs="ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ",
    direction_note="Ⅰ → Ⅱ → Ⅲ | Ⅳ ... Ⅻ [the '|' is the surveyor's own header notation, marking his mechanism break]",
    axis="stroke-count subitizing for Ⅰ-Ⅲ ('similar mechanism to the die faces, just less iconic'), then 'a hard transition to pure symbol/convention lookup' from Ⅳ on — 'a genuinely interesting immediacy cliff within a single family'",
    felt="Strength of the overall semantic order I→XII: high (if you know Roman numerals)",
    felt_immediacy_verbatim="Immediacy: high for I-III, then drops off a cliff — flagging the cliff itself as the interesting datum, more than either segment alone",
    basis="semantic-knowledge", constructed=False,
    migrator_notes="basis is semantic-knowledge for the full chain per the surveyor's own analysis; the Ⅰ-Ⅲ prefix alone is perceived-directly (stroke subitizing). The cliff observation doubles as a meta finding; kept in this record rather than split since the sequence IS the evidence.",
    open="Post-cliff portion 'would actively mislead a naive stroke-counter (Ⅳ has fewer marks than Ⅲ despite being more)' — a pre-made adversarial validation item."))

R.append(rec("sequence", "205-215", roles=["sequence","contrast-case"], glyphs="⅒⅑⅛⅐⅙⅕⅓⅖⅗⅔¾⅘⅚⅞",
    direction_note="as magnitudes: 1/10 < 1/9 < 1/8 < 1/7 < 1/6 < 1/5 < 1/3 < 2/5 < 3/5 < 2/3 < 3/4 < 4/5 < 5/6 < 7/8 [surveyor marks 1/4 and 1/2 'not present'; < signs are his]",
    axis="purely semantic/arithmetic fraction value; 'you must read a two-part symbol AND perform an inversion'",
    felt="Strength (given full arithmetic competence): high but effortful, not 'felt.'",
    felt_immediacy_verbatim="Immediacy: very low, arguably the least immediate item in this survey — you must read a two-part symbol AND perform an inversion",
    basis="semantic-knowledge", constructed=True, tc="ambiguous",
    migrator_notes="Surveyor gave the order as fraction VALUES, not glyphs; glyphs field is my reconstruction. Ambiguities passed back: (1) he lists 3/4 as present, but U+2153-215E has no 3/4 — vulgar 3/4 is U+00BE ¾ in Latin-1, outside the Number Forms block he was surveying; transcribed as ¾ provisionally. (2) His value list omits 3/8 ⅜ and 5/8 ⅝ which ARE in the block, without marking them not-present. Also his own inline correction '⅛(wait, reorder)' is preserved in note_verbatim.",
    open="3/4 presence and the omitted ⅜/⅝ need adjudication; see migrator_notes."))

# --- Arrows ---
R.append(rec("sequence", "221-229", glyphs="→⇉⇶",
    direction_note="→ (1 arrow) → ⇉ (2 paired rightwards) → ⇶ (3 rightwards arrows)",
    axis="count/multiplicity of repeated icons; 'more insistence / more flow — like a repeated-icon intensity cue (think !!! or stacked chevrons on a fast-forward button)'",
    felt="Strength: high for 1→2→3",
    felt_immediacy_verbatim="Immediacy: high, I subitize the arrow count without needing to think about what it denotes",
    basis="perceived-directly", constructed=False,
    open="Direction-locked: 'this specific triple only exists for rightwards in this block (I didn't spot a leftwards/up/down triple)'."))

R.append(rec("sequence", "231-241", glyphs="→⇒⇛",
    direction_note="→ (single line arrow) → ⇒ (double line) → ⇛ (triple arrow)",
    axis="stroke-multiplicity *within one arrow glyph* (shaft count); conventionally 'stronger implication' in logic notation, 'but that convention is learned, not seen'",
    felt="Strength: medium, and mostly familiar to people with a math/logic background",
    felt_immediacy_verbatim="Immediacy: medium (the visual 'thickening/doubling' does suggest emphasis fairly directly, more than pure symbol lookup, but less than a fill or count ramp)",
    basis="perceived-directly", constructed=False,
    migrator_notes="basis judgment call: surveyor places this BETWEEN percept and convention (immediacy: medium); the visual doubling itself is seen, the 'stronger implication' reading is semantic — recorded perceived-directly with this caveat. A graded-basis case for the schema question list."))

R.append(rec("sequence", "243-249", glyphs="⇷⇺",
    direction_note="1 stroke (⇷⇸) vs 2 strokes (⇺⇻) as 'more blocked / more strongly negated' [↚ ↛ appear in his header as the plain-negation baseline]",
    axis="strokes-through-the-shaft count as graded negation intensity",
    felt="Strength: low, flagging as attempted-and-mostly-failed rather than omitting per the 'strength of feel, even if low' spirit of the brief. 'I can feel a weak ordering ... but it's a stretch'",
    basis="perceived-directly", constructed=True, marked_speculative=True, tc="interpreted",
    migrator_notes="glyphs = one representative per stroke-count tier (rightward pair); surveyor listed direction pairs ⇷⇸ / ⇺⇻ as the tiers. Surveyor himself doubts most viewers would expect graded negation ('a boolean').",
    open="Is graded negation ever perceived, or is negation boolean for typical viewers?"))

# --- Enclosed Alphanumerics ---
R.append(rec("sequence", "255-260", glyphs="①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳",
    direction_note="① ② ③ ... ⑳ — codepoint order and semantic order coincide perfectly",
    axis="digit-recognition-in-a-badge; 'the circle decoration adds nothing perceptual to the ordering'",
    felt="strength: high (order is unambiguous once you can read digits)",
    felt_immediacy_verbatim="Immediacy: low (symbol lookup); same immediacy verdict as plain digits",
    basis="semantic-knowledge", constructed=False,
    migrator_notes="Surveyor elided ④-⑲ with '...'; full run reconstructed from '① ② ③ ... ⑳' — mechanical, but noted."))

# --- Summary metas ---
R.append(rec("meta", "264-287",
    axis="surveyor's own confidence ranking of strongest finds (sparkline bars > shade ramp > circle fill > die faces > size ladders > outline density) plus a curated list of 'best immediacy-cliff / contrast finds'",
    felt="ranked by my confidence",
    basis="unstated",
    schema_version="0.9",
    revises=[{"id": rid("16-27"), "revises_span": "16-27", "revision_kind": "refinement"},
             {"id": rid("69-78"), "revises_span": "69-78", "revision_kind": "confirmation"}],
    migrator_notes="Pure index/ranking over records already extracted above — no new sequences; valuable as the surveyor's native strength ordering, i.e. calibration data for pass-2 strength normalization. [Revision links migrator-inferred: this retrospective ranks circle-fill #3 behind sparkline/shade, completing the supersession of its 'strongest single find so far' claim — It also endorses/strengthens the die-faces register ('Strength: very high' at span 69-78 → 'confirmed as maximally strong and maximally immediate' here) — carried as the second revises entry, revision_kind confirmation (v0.9). The earlier records' felt-reports stand untouched — true as reports when written.]"))

R.append(rec("meta", "289-293", lineage="brief-steered",
    axis="'immediacy is really a property of the *specific comparison*, not of a symbol *set*, and some sets straddle both regimes' — the within-family immediacy cliff (Roman numerals) surprised the surveyor",
    felt="What surprised me most",
    basis="unstated",
    migrator_notes="A stated generalization about the space; implied falsifier: a set where immediacy is uniform across all pairwise comparisons despite mechanism change. Surveyor tested one instance (Roman numerals)."))

R.append(rec("meta", "295-302", meta_kind="coverage-gap",
    axis="coverage/scope statement: blocks covered this pass (Geometric Shapes, Block Elements, Misc Symbols, Arrows, Super/Subscripts, Number Forms, Enclosed Alphanumerics) and blocks left open (Mathematical Operators, Misc Technical, Dingbats, Spacing Modifier Letters, supplemental math/arrow blocks)",
    felt="noting the honest scope so it's clear what this pass did and didn't reach",
    basis="unstated",
    migrator_notes="Negative-space observation about the survey itself, not the glyph space; kept as meta so pass-2 knows uncovered blocks are unexamined, not empty."))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
ids = [r["id"] for r in R]
assert len(ids) == len(set(ids)), "id collision"
with open(OUT, "w", encoding="utf-8") as f:
    for r in R:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"{len(R)} records -> {OUT}")
from collections import Counter
print(Counter(r["type"] for r in R))
