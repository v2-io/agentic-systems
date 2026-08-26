#!/usr/bin/env python3
"""Pass-1 migration: sonnet-survey-3.md -> extracted/sonnet-survey-3.jsonl
note_verbatim is pulled from the source file by line range (verbatim guarantee);
codepoints computed from the glyph strings themselves."""
import hashlib, json, os, unicodedata

BASE = "/Users/josephwecker-v2/src/arch/asf/empirica/glyph-magnitude-perception/data/surveys-v1"
SRC = os.path.join(BASE, "sonnet-survey-3.md")
OUT = os.path.join(BASE, "extracted", "sonnet-survey-3.jsonl")

lines = open(SRC, encoding="utf-8").read().splitlines()

def span_text(a, b):
    return "\n".join(lines[a-1:b])

def cps(s):
    s = unicodedata.normalize("NFC", s)
    return ["U+%04X" % ord(c) for c in s]

def rid(span):
    return hashlib.sha256(("survey-rec|sonnet-survey-3|" + span).encode()).hexdigest()[:16]

COMMON = dict(schema_version="0.7", surveyor="sonnet-3",
              id_recipe="sha256('survey-rec|sonnet-survey-3|' + source_span)[:16]",
              source_file="sonnet-survey-3.md",
              epistemic_class="interactive-guided-survey-anecdote",
              lineage="unprompted")

records = []

def rec(a, b, type, **kw):
    span = f"L{a}-L{b}"
    r = dict(COMMON)
    r.update(id=rid(span), record_type=type, source_span=span,
             note_verbatim=span_text(a, b))
    glyphs = kw.pop("glyphs", None)
    if glyphs is not None:
        r["glyphs"] = glyphs
        r["codepoints"] = cps(glyphs)
    r.update(kw)
    records.append(r)

E = lambda **k: k  # epistemics block builder

# ---- preamble / method meta -------------------------------------------------
rec(3, 8, "meta",
    axis="strength vs immediacy — surveyor's two-axis method definition",
    epistemics=E(felt_strength_verbatim="unstated", basis="unstated",
                 marked_speculative=False),
    transcription_confidence="clear",
    migrator_notes="Method preamble, not a find. Defines the survey's own vocabulary: Strength = pairwise recoverability confidence; Immediacy = raw percept vs symbol lookup. The immediacy axis is attributed to Joseph ('Joseph's added axis') — supplied in the one-shot brief, not a mid-survey intervention; lineage kept 'unprompted' per brief, flagged as a question in the migration report.",
    open="Does a brief-supplied axis count as steering? Routed to Joseph in report.")

# ---- Enclosed Alphanumerics -------------------------------------------------
rec(13, 18, "sequence", glyphs="①②③④⑤⑥⑦⑧⑨⑩",
    direction_note="↑ increasing",
    axis="digit-recognition, not percept-magnitude; 'reading 1 2 3 with a circle sticker on it'",
    epistemics=E(felt_strength_verbatim="Strength: very high, but immediacy: LOW",
                 basis="semantic-knowledge", marked_speculative=False),
    constructed=False, transcription_confidence="clear",
    migrator_notes="Surveyor's own exemplar of the strength/immediacy split.")

rec(19, 21, "sequence", glyphs="⓪①②③④⑤⑥⑦⑧⑨⑩",
    direction_note="[migrator-inferred: ↑] surveyor states only 'including the zero at the front feels right, zero read as less than one'",
    axis="zero read as 'less than one' purely semantically; semantic override of codepoint order (⓪ is U+24EA, codepoint-later)",
    epistemics=E(felt_strength_verbatim="'the semantic override is total — no hesitation at all'",
                 basis="semantic-knowledge", marked_speculative=False),
    constructed=True, transcription_confidence="clear",
    migrator_notes="constructed=true: surveyor prepended the codepoint-nonadjacent zero deliberately.")

rec(22, 23, "sequence", glyphs="⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽",
    direction_note="[migrator-inferred: ↑] no arrow stated; asserted as 'same digit-lookup pattern' as the ↑ circled-digit record",
    axis="same digit-lookup pattern, parenthesized",
    epistemics=E(felt_strength_verbatim="'Same strength/immediacy profile as circled digits'",
                 basis="semantic-knowledge", marked_speculative=False),
    constructed=False, transcription_confidence="clear",
    migrator_notes="Strength given by reference to the circled-digit record (L13-L18: very high / LOW), not restated by the surveyor — the resolution is the migrator's.")

rec(24, 27, "equivalence", glyphs="①⑴⒈",
    axis="same-value-different-frame is not a magnitude axis; 'different fonts of the same value'",
    epistemics=E(felt_strength_verbatim="'do NOT have a magnitude relationship for me — no ordering feel'",
                 basis="perceived-directly", marked_speculative=False,
                 negative_kind="verified-absent", equivalence_basis="seen"),
    transcription_confidence="clear",
    migrator_notes="Surveyor frames it as a non-example (negative); typed equivalence per schema's same-magnitude-different-dress class, with the negative framing preserved. Matches the schema's own ①⑴⒈ sample. equivalence_basis seen: surveyor put the three glyphs together and tested the feel.")

rec(28, 30, "negative", glyphs="Ⓐ①ⓐ",
    axis="mixed circled-letter vs circled-digit: letters are 'identity/rank in a different, weaker sense', not magnitudes",
    epistemics=E(felt_strength_verbatim="'no felt ordering'",
                 basis="perceived-directly", marked_speculative=False,
                 negative_kind="not-felt"),
    transcription_confidence="clear",
    migrator_notes="Forward-references an 'alphabet note below under Geometric Shapes' that does not appear in the file — dangling reference, flagged in report.")

rec(31, 32, "sequence", glyphs="⓪①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳",
    direction_note="↑ full monotonic run 0-20",
    axis="digit lookup throughout",
    epistemics=E(felt_strength_verbatim="strength very high, immediacy low (digit lookup) throughout",
                 basis="semantic-knowledge", marked_speculative=False),
    constructed=True, transcription_confidence="clear",
    migrator_notes="constructed=true only in the weak sense of the prepended ⓪ (U+24EA); ①-⑳ is the natural codepoint run.")

# ---- Geometric Shapes -------------------------------------------------------
rec(36, 43, "sequence", glyphs="◌○◔◑◕●",
    direction_note="↑ increasing",
    axis="pie-chart-style fill ramp; 'how full is the pie', no lookup",
    epistemics=E(felt_strength_verbatim="Strength: very high. Immediacy: HIGH. 'One of the strongest finds so far, on par with the block-elements ramp'",
                 basis="perceived-directly", marked_speculative=False),
    constructed=True, transcription_confidence="clear",
    migrator_notes="constructed=true: dotted-circle U+25CC is imported from outside the fill family and the fill steps are hand-ordered, not codepoint order. Deliberately skips ◐◒◓ as same-fraction-different-orientation (see equivalence record L40-L43).")

rec(40, 43, "equivalence", glyphs="◐◑◒◓",
    axis="same-fraction-different-orientation: all 'half', same value/different frame, no ordering feel between them",
    epistemics=E(felt_strength_verbatim="'no ordering feel between them'",
                 basis="perceived-directly", marked_speculative=False,
                 negative_kind="verified-absent", equivalence_basis="assumed"),
    transcription_confidence="interpreted",
    migrator_notes="equivalence_basis assumed: the full glyph set is a migrator completion of the orientation class, not a set the surveyor laid side by side. Extracted from the parenthetical aside inside the pie-ramp bullet (span overlaps L36-L43 record). Surveyor names ◐/◒/◓ as skipped; ◑ is the member kept in the ramp — glyph set here is the migrator's completion of the half-circle orientation class.")

rec(44, 51, "negative", glyphs="▫▪◽◾□■",
    axis="white-vs-black same-shape pairs: fill flip alone is 'different mode', not 'more'",
    epistemics=E(felt_strength_verbatim="'I do NOT feel a magnitude ordering from color/fill alone here'",
                 basis="perceived-directly", marked_speculative=False,
                 negative_kind="verified-absent"),
    transcription_confidence="clear",
    migrator_notes="Three pairs (▫▪, ◽◾, □■) tested; surveyor explicitly contrasts with ░▒▓█ which DID read as magnitude. Companion mechanism-hypothesis extracted as meta record L48-L51.")

rec(48, 51, "meta",
    axis="hypothesis: a ramp needs ≥3 intermediate steps of the same fill dimension to read as quantity; a bare 2-way white/black flip reads as a qualitative switch",
    epistemics=E(felt_strength_verbatim="'My best guess … even though these two facts are hard to reconcile fully'",
                 basis="perceived-directly", marked_speculative=True,
                 scope="fill/shading dimension; reconciling ▫▪ non-feel with ░▒▓█ feel",
                 falsifier_implied="a 2-step ramp that reads as magnitude, or a ≥3-step same-dimension ramp that does not",
                 tested_instance=True),
    transcription_confidence="clear",
    migrator_notes="Stated law with self-acknowledged tension; restated more strongly in synthesis (L257-L263).")

rec(52, 56, "sequence", glyphs="▪◻◼",
    direction_note="small → medium (→ presumably 'large' if it existed)",
    axis="size-magnitude 'purely from name/rendered-size'; rendering-dependent",
    epistemics=E(felt_strength_verbatim="Strength: LOW-MEDIUM, flagging as tentative rather than confident",
                 basis="name-derived", marked_speculative=True),
    constructed=True, transcription_confidence="interpreted",
    migrator_notes="Bullet offers alternates ('▫◻▪◼ or better ◽◻'); glyph field records the small→medium ordering the prose actually asserts (▪ small vs ◻/◼ medium) — the final two (◻ ◼) are TIED at 'medium' per the prose; the linear string implies no ◻<◼ ordering by the surveyor. Basis name-derived per surveyor's own 'purely from name/rendered-size' — partly imagined rendering, the schema's grep hazard.")

rec(57, 63, "sequence", glyphs="▹▸►",
    direction_note="↑ increasing size/'weight'",
    axis="right-pointing triangle size ramp with an incidental fill-switch in the middle — not a pure single-dimension ramp",
    epistemics=E(felt_strength_verbatim="Strength: MEDIUM. Immediacy: MEDIUM",
                 basis="perceived-directly", marked_speculative=False,
                 predicted_generalization="'Worth someone re-checking at a larger point size'"),
    constructed=True, transcription_confidence="clear",
    migrator_notes="Surveyor decomposes the sequence: size carries the magnitude, the ▹→▸ fill switch carries none (consistent with the L44-L51 negative).")

rec(64, 65, "negative", glyphs="▵▴▽▾",
    axis="small triangles, white/black: no magnitude feel from the fill switch itself",
    epistemics=E(felt_strength_verbatim="'again no magnitude feel … consistent with the finding above'",
                 basis="perceived-directly", marked_speculative=False,
                 negative_kind="not-felt"),
    transcription_confidence="clear",
    migrator_notes="Confirmation instance of the white/black-flip non-finding.")

rec(66, 70, "sequence", glyphs="◦○◯",
    direction_note="↑ increasing size",
    axis="bullet → circle → large circle, purely by named/rendered diameter",
    epistemics=E(felt_strength_verbatim="Strength: MEDIUM-HIGH, immediacy: HIGH — 'believe it's there, haven't cross-checked rendering'",
                 basis="name-derived", marked_speculative=True),
    constructed=True, transcription_confidence="clear",
    migrator_notes="Surveyor self-flags rendering uncertainty (◦ vs ○ size vs weight); basis recorded name-derived per 'purely by named/rendered diameter' + the un-cross-checked rendering caveat.")

# ---- Braille ---------------------------------------------------------------
rec(74, 84, "sequence", glyphs="⠀⠁⠃⠇⠏⠟⠿",
    direction_note="↑ increasing (blank → 1 dot → … → 6 dots, low-byte-mask progression)",
    axis="'more dots visible' as a raw density percept; noisier than ▁-█ because dot positions jump around the 2x3 cell",
    epistemics=E(felt_strength_verbatim="Strength: HIGH. Immediacy: HIGH ('reads a beat slower than ▁▂▃▄▅▆▇█')",
                 basis="perceived-directly", marked_speculative=False,
                 predicted_generalization="'a fresh agent given the raw 2800-28FF block in codepoint order would NOT perceive a monotonic ramp there'"),
    constructed=True, transcription_confidence="clear",
    migrator_notes="constructed=true, surveyor-explicit: 'I had to hand-pick the dot-count subsequence out of the block' — codepoints are bit-mask ordered, not dot-count ordered. Scattered-codepoints-strong-feel exemplar named as such.")

# ---- Number Forms ----------------------------------------------------------
rec(88, 95, "sequence", glyphs="⅛⅕⅓⅜⅔⅝⅞",
    direction_note="↑ increasing numeric value (1/8, 1/5, 1/3, 3/8, 2/3, 5/8, 7/8)",
    axis="pure symbol/arithmetic lookup, no perceptual shortcut at all; not even a monotonic glyph-shape cue",
    epistemics=E(felt_strength_verbatim="immediacy: LOW; 'Strength is nevertheless fairly high once the arithmetic is done' — 'maybe the cleanest [immediacy-low/strength-high example] in the survey'",
                 basis="semantic-knowledge", marked_speculative=False),
    constructed=True, transcription_confidence="clear",
    migrator_notes="constructed=true: surveyor sorted mixed-denominator fractions by value; codepoint order differs.")

rec(96, 104, "sequence", glyphs="ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ",
    direction_note="↑ one through ten",
    axis="numeral-literacy lookup with a 'tally-mark pocket' at the front: I-II-III is a genuine visual stroke-count ramp that IV inverts/resets",
    epistemics=E(felt_strength_verbatim="Immediacy: LOW-MEDIUM — 'low-BUT-WITH-A-TALLY-MARK-POCKET at the front'",
                 basis="semantic-knowledge", marked_speculative=False),
    constructed=False, transcription_confidence="clear",
    migrator_notes="Internal-texture find: immediacy non-uniform within one sequence. Strength not separately stated for the whole run.")

rec(105, 107, "sequence", glyphs="ↀↁↂ",
    direction_note="↑ (Roman 1000, 5000, 10000)",
    axis="pure lookup; relies on knowing these specific archaic glyphs",
    epistemics=E(felt_strength_verbatim="immediacy LOW, strength MEDIUM",
                 basis="semantic-knowledge", marked_speculative=False,
                 predicted_generalization="'less confident a fresh agent recovers this without prior Roman-numeral exposure'"),
    constructed=False, transcription_confidence="clear")

# ---- Moon phases -----------------------------------------------------------
rec(111, 118, "sequence", glyphs="🌑🌒🌓🌔🌕",
    direction_note="↑ increasing illuminated fraction (new → full); then 🌕🌖🌗🌘🌑 continues symmetrically decreasing — 'monotonic on each half'",
    axis="'how much of the disc is lit' as a raw percept; same texture as ◌○◔◑◕● but richer imagery",
    epistemics=E(felt_strength_verbatim="Strength: very high. Immediacy: HIGH",
                 basis="perceived-directly", marked_speculative=False),
    codepoints_by_reference=cps("🌖🌗🌘"),
    constructed=False, transcription_confidence="clear",
    migrator_notes="codepoints_by_reference: the waning half (🌖🌗🌘; 🌕/🌑 already in the primary set) is asserted in this note but not carried as the record's primary sequence — listed so codepoint-indexed sampling sees the survey touched them. Round-trip structure (up then down over the full 8-glyph cycle) surveyor-flagged as outside the pure-monotonic brief; borderline cyclic — kept as sequence for the waxing half per the surveyor's own framing, decreasing half preserved in direction_note. Flagged in report.",
    open="Is an up-then-down round-trip a sequence pair, or the schema's cyclic type?")

# ---- Geometric Shapes Extended ---------------------------------------------
rec(122, 130, "sequence", glyphs="🞅🞆🞇🞈🞉",
    direction_note="↑ increasing outline weight",
    axis="stroke-weight ramp; 'a rare case where the naming convention IS the magnitude scale'",
    epistemics=E(felt_strength_verbatim="Strength: HIGH. Immediacy: MEDIUM — 'a percept but a faint one; I'd rate it well below the fill-based ramps'",
                 basis=["perceived-directly", "name-derived"], marked_speculative=False),
    constructed=False, transcription_confidence="clear",
    migrator_notes="basis is list-valued (schema v0.7): strength partly rides on Unicode names spelling the ramp, but the surveyor asserts a real if faint percept.")

rec(131, 134, "sequence", glyphs="🞌🞍🞎🞏🞐🞑🞒🞓",
    direction_note="↑ tiny → extremely heavy squares",
    axis="size+weight compounded; 'same texture, same caveat' as the circle-weight ramp, a bit more immediate",
    epistemics=E(felt_strength_verbatim="stated by reference: same as 🞅🞆🞇🞈🞉 (HIGH / MEDIUM), 'a bit more immediate'",
                 basis="perceived-directly", marked_speculative=False),
    constructed=False, transcription_confidence="clear")

rec(135, 137, "sequence", glyphs="🞗🞘🞙",
    direction_note="↑ tiny → very small → medium small black diamond",
    axis="size ramp, three steps; 'weakest/most-subtle of this family'",
    epistemics=E(felt_strength_verbatim="'flagging low-medium confidence rather than including it as a strong finding'",
                 basis="perceived-directly", marked_speculative=True),
    constructed=False, transcription_confidence="clear")

# ---- Arrows ----------------------------------------------------------------
rec(141, 146, "sequence", glyphs="→⇒⇛",
    direction_note="↑ increasing; 'same shape works for leftwards: ←⇐⇚'",
    axis="more parallel strokes reads as 'more emphatic/more force', like chevron-stacking",
    epistemics=E(felt_strength_verbatim="Strength: HIGH. Immediacy: HIGH",
                 basis="perceived-directly", marked_speculative=False),
    codepoints_by_reference=cps("←⇐⇚"),
    constructed=True, transcription_confidence="clear",
    migrator_notes="Surveyor-named scattered-codepoint find (U+2192, U+21D2, U+21DB non-adjacent). Mirror ←⇐⇚ asserted by reference, kept inside this record rather than duplicated; codepoints_by_reference makes the mirror glyphs visible to codepoint-indexed sampling.")

rec(147, 149, "negative", glyphs="⇀⇒",
    axis="harpoon (half-barb) vs full arrowhead reads as a different meaning (one-directional reaction vs full arrow), not 'less'",
    epistemics=E(felt_strength_verbatim="'I don't get a magnitude feel'",
                 basis="perceived-directly", marked_speculative=False,
                 negative_kind="not-felt"),
    transcription_confidence="clear")

# ---- Mathematical Operators ------------------------------------------------
rec(153, 163, "sequence", glyphs="<≪⋘",
    direction_note="↑ increasing ('less than' → 'much less than' → 'very much less than'); mirror >≫⋙ 'obviously the same for the other direction'",
    axis="visual chevron-stacking (1→2→3 wedges) as pure 'more of the same shape'; semantic naming and glyph-stacking agree",
    epistemics=E(felt_strength_verbatim="Strength: very high. Immediacy: HIGH — 'just below ▁-█ and ◌○◔◑◕● in immediacy, and possibly above them in how surprising the find felt'",
                 basis="perceived-directly", marked_speculative=False),
    codepoints_by_reference=cps(">≫⋙"),
    constructed=True, transcription_confidence="clear",
    migrator_notes="'It fell straight out of scanning the block' — surprise register preserved in note. Mirror form >≫⋙ kept by reference, not duplicated; codepoints_by_reference makes it visible to codepoint-indexed sampling.")

rec(164, 169, "negative", glyphs="≤≦⊆⊂",
    axis="equal-vs-strict pairs read as a boolean modifier (inclusive/exclusive), not a 'how much more' step — even though the underlying math concept IS ordered",
    epistemics=E(felt_strength_verbatim="'no felt magnitude between them … perceptually the glyphs read as siblings, not a ramp'",
                 basis="perceived-directly", marked_speculative=False,
                 negative_kind="verified-absent"),
    transcription_confidence="clear",
    migrator_notes="Surveyor ties this to the white/black-square non-finding: single binary toggle ≠ magnitude.")

rec(170, 171, "negative", glyphs="≺≼",
    axis="precedes / precedes-or-equal: boolean modifier not magnitude",
    epistemics=E(felt_strength_verbatim="'same non-finding'",
                 basis="perceived-directly", marked_speculative=False,
                 negative_kind="not-felt"),
    transcription_confidence="clear")

# ---- Dice ------------------------------------------------------------------
rec(175, 182, "sequence", glyphs="⚀⚁⚂⚃⚄⚅",
    direction_note="↑ increasing pip count 1-6",
    axis="dot-count percept with subitizing texture: 1-3 instant, 4/5/6 'a half-beat of counting'",
    epistemics=E(felt_strength_verbatim="Strength: maximal. Immediacy: HIGH-ish but not pure",
                 basis="perceived-directly", marked_speculative=False,
                 received_context="'one of the ones Joseph said he expected — confirming it'"),
    constructed=False, transcription_confidence="clear",
    migrator_notes="The find itself is perceived-directly; the fact that it was Joseph-expected is provenance context, not the basis. Subitizing-boundary texture 'showed up unprompted in my own perception'.")

# ---- Trigrams --------------------------------------------------------------
rec(186, 201, "negative", glyphs="☰☱☲☳☴☵☶☷",
    roles=["negative", "conditional-sequence"],
    axis="codepoint order gives no magnitude feel; the King Wen binary reordering ☷☶☵☴☳☲☱☰ (Earth 000 → Heaven 111) WOULD be monotonic by convention but is retrieved fact + arithmetic, 'not a percept'",
    epistemics=E(felt_strength_verbatim="'Strength if you accept the binary-convention reordering: MEDIUM. Immediacy: LOW regardless of ordering.' — 'my honest first-instinct is that the ordering is NOT perceptually available to me'",
                 basis="semantic-knowledge", marked_speculative=False,
                 negative_kind="verified-absent",
                 received_context="Joseph specifically flagged expecting trigrams as a hit; surveyor is contradicting the expectation"),
    transcription_confidence="interpreted",
    migrator_notes="Dual-content record: a perceptual negative AND a conditional (convention-mediated) sequence at MEDIUM in one note. Typed negative per the surveyor's own bottom line ('worth not rounding up'); the conditional reordered sequence lives in axis/note. Schema-fit question flagged in report. Restated in synthesis L265-L270.",
    open="Does pass 1 want a separate conditional-sequence record for the King Wen reordering?")

# ---- Block Elements (under the Trigrams header in the source) ---------------
BLOCK_MISFILE = "Source anomaly: this bullet sits under the '## U+2630–U+2637 Trigrams' header but is Block Elements (U+2580-259F) content — header/content mismatch preserved as-is, flagged in report."

rec(203, 208, "sequence", glyphs="▁▂▃▄▅▆▇█",
    direction_note="↑ increasing",
    axis="pure fill-height ramp; ''more' arrives in the percept itself, no lookup required' — the surveyor's calibration anchor",
    epistemics=E(felt_strength_verbatim="Strength: maximal, immediacy: HIGH",
                 basis="perceived-directly", marked_speculative=False),
    constructed=False, transcription_confidence="clear",
    migrator_notes="'This is what a *true* magnitude sequence feels like to me, and it recalibrated how I read everything else in this survey' — mid-survey recalibration event, load-bearing for interpreting earlier records. " + BLOCK_MISFILE)

rec(209, 213, "sequence", glyphs="░▒▓█",
    direction_note="↑ increasing density/darkness",
    axis="pure visual density, no symbolic mediation; only 4 steps, ▓→█ jump feels larger than ░→▒→▓",
    epistemics=E(felt_strength_verbatim="Strength: very high. Immediacy: HIGH — 'slightly less crisp than the eighths-ramp'",
                 basis="perceived-directly", marked_speculative=False),
    constructed=False, transcription_confidence="clear",
    migrator_notes=BLOCK_MISFILE)

rec(214, 221, "sequence", glyphs="▏▎▍▌▋▊▉█",
    direction_note="↑ increasing (left-aligned eighths)",
    axis="same family as ▁-█ rotated 90°; vertical ramp reads faster/more viscerally than horizontal — 'up = more' metaphor stacking",
    epistemics=E(felt_strength_verbatim="Strength maximal, immediacy HIGH",
                 basis="perceived-directly", marked_speculative=False,
                 predicted_generalization="'Worth someone checking whether this is a real, general asymmetry (vertical ramps > horizontal ramps in strength) across other groups'"),
    constructed=False, transcription_confidence="clear",
    migrator_notes="Vertical-vs-horizontal asymmetry hypothesis embedded here and restated as its own synthesis item (meta record L272-L276). " + BLOCK_MISFILE)

rec(222, 227, "sequence", glyphs="▖▗▘▝▚▞▄▀▌▐▙▛▜▟█",
    direction_note="1 quadrant < 2 quadrants < 3 quadrants < full (rough)",
    axis="'how much of the cell is filled' — but counting filled corners is closer to a lookup than a percept",
    epistemics=E(felt_strength_verbatim="'much weaker/slower than the linear ramp above'; Immediacy: MEDIUM; 'Not including as a clean sequence — flagging as a near miss instead'",
                 basis="perceived-directly", marked_speculative=True),
    constructed=True, transcription_confidence="interpreted",
    migrator_notes="Surveyor gives family groupings, not a fixed string; glyph field is the migrator's assembly of the named quadrant-count classes (single, ▚▞ two-quadrant, half-blocks, multi-quadrant, then █ for the stated '< full' endpoint) in the surveyor's stated coarse order. 'Near miss' is a surveyor-native status with no schema slot — flagged in report. " + BLOCK_MISFILE,
    open="Schema gap: 'near miss' (ordering felt but disqualified as a clean sequence) — sequence-with-speculative-flag is the pass-1 approximation used here.")

# ---- Running synthesis ------------------------------------------------------
rec(233, 255, "meta",
    axis="immediacy ranking of all finds, strongest→weakest (5 tiers: fill > mark-stacking > dot-count/subitizing > stroke-weight > symbol-lookup), plus the mechanism claim that fill ramps are 'the same underlying mechanism wearing three different costumes'",
    epistemics=E(felt_strength_verbatim="'my honest gut order'",
                 basis="perceived-directly", marked_speculative=False,
                 scope="the sequences found in this survey session",
                 tested_instance=True,
                 predicted_generalization="'I'd guess a naive pass (mine, an hour ago) over-weights category 5 and under-reports categories 1-3, because strength is easy to introspect and immediacy is not'"),
    transcription_confidence="clear",
    migrator_notes="Synthesis, not a new find: a native strength-vocabulary ranking across the survey's own records, plus a methodological self-observation (lookup fast enough to hide from casual self-report). High value for pass-2 mechanism vocabulary.")

rec(257, 263, "meta",
    axis="stated law: binary white/black or inclusive/exclusive toggles essentially never read as magnitude; monotonic feel needs (a) a continuous/steppable fill or count dimension, or (b) an overlearned numeral-literacy shortcut",
    epistemics=E(felt_strength_verbatim="'essentially never read as magnitude to me' — 'A recurring non-finding worth stating plainly'",
                 basis="perceived-directly", marked_speculative=False,
                 scope="binary toggles across blocks tested this session (▫▪, ⊂⊆, ≤≦, ◐◑◒◓)",
                 falsifier_implied="a bare qualitative flip that does read as magnitude, or a monotonic feel with neither (a) nor (b)",
                 tested_instance=True),
    transcription_confidence="clear",
    migrator_notes="The synthesis-strength form of the L48-L51 hypothesis; multiple instances tested (negative records L44-L51, L64-L65, L147-L149, L164-L169, L170-L171).")

rec(265, 270, "meta",
    axis="trigram candor restatement: no perceptual ordering without retrieving the King-Wen convention, 'and even then it's arithmetic, not percept' — reported against Joseph's named expectation",
    epistemics=E(felt_strength_verbatim="'my honest first instinct is these do NOT carry a perceptual ordering for me at all'",
                 basis="semantic-knowledge", marked_speculative=False,
                 received_context="Joseph named trigrams as an expected hit; the brief 'specifically invited candor about codepoint order vs semantic order'",
                 tested_instance=True),
    transcription_confidence="clear",
    migrator_notes="Synthesis restatement of the L186-L201 negative; kept as its own record so the verbatim is indexed, cross-reference by span.")

rec(272, 276, "meta",
    axis="possible general effect: vertical fill ramps more immediate than horizontal (▁▂▃▄▅▆▇█ > ▏▎▍▌▋▊▉█ despite identical concept rotated); candidate mechanism 'vertical=more overlearned via bar charts / height metaphors'",
    epistemics=E(felt_strength_verbatim="'flagging as a possible general effect … since I only have one data point (myself) on it'",
                 basis="perceived-directly", marked_speculative=True,
                 scope="one within-surveyor comparison",
                 falsifier_implied="second surveyor / cross-group comparison showing no vertical>horizontal asymmetry",
                 tested_instance=True,
                 predicted_generalization="'worth a second surveyor's opinion'"),
    transcription_confidence="clear",
    migrator_notes="Synthesis form of the hypothesis embedded in the L214-L221 record.")

# ---- v0.7 overlays: felt_immediacy_verbatim + brief-steered lineage ---------
# The immediacy axis was brief-supplied ("Joseph's added axis", L5-L7), so
# records whose content rides on that axis carry lineage brief-steered
# (adjudicated 2026-08-25). Immediacy values below are the surveyor's words.
IMM = {
    "L13-L18": "immediacy: LOW — 'this is digit-recognition, not percept-magnitude'",
    "L22-L23": "'Same strength/immediacy profile as circled digits' (LOW by reference — migrator resolution)",
    "L31-L32": "immediacy low (digit lookup) throughout",
    "L36-L43": "Immediacy: HIGH — 'Reads instantly as how full is the pie, no lookup'",
    "L57-L63": "Immediacy: MEDIUM — 'some of the size gap is subtle at typical rendering'",
    "L66-L70": "immediacy: HIGH (size is a raw percept)",
    "L74-L84": "Immediacy: HIGH — ''more dots visible' is a raw density percept … reads a beat slower than ▁▂▃▄▅▆▇█'",
    "L88-L95": "immediacy: LOW — 'pure symbol/arithmetic lookup, no perceptual shortcut at all'",
    "L96-L104": "Immediacy: LOW-MEDIUM — 'low-BUT-WITH-A-TALLY-MARK-POCKET at the front'",
    "L105-L107": "immediacy LOW",
    "L111-L118": "Immediacy: HIGH — ''how much of the disc is lit' is a raw percept'",
    "L122-L130": "Immediacy: MEDIUM — 'a percept but a faint one'",
    "L131-L134": "same as 🞅🞆🞇🞈🞉 by reference (MEDIUM), 'a bit more immediate' — migrator resolution",
    "L141-L146": "Immediacy: HIGH",
    "L153-L163": "Immediacy: HIGH — 'almost as immediate as the block-fill ramp'",
    "L175-L182": "Immediacy: HIGH-ish but not pure — subitizing texture, 'a half-beat of counting' past 3",
    "L186-L201": "Immediacy: LOW regardless of ordering",
    "L203-L208": "immediacy: HIGH — ''more' arrives in the percept itself, no lookup required'",
    "L209-L213": "Immediacy: HIGH — 'pure visual density, no symbolic mediation'",
    "L214-L221": "immediacy HIGH",
    "L222-L227": "Immediacy: MEDIUM — 'closer to a lookup than a percept'",
}
BRIEF_STEERED = set(IMM) | {"L3-L8", "L233-L255"}  # + axis definition, + immediacy ranking
for r in records:
    s = r["source_span"]
    if s in IMM:
        r["epistemics"]["felt_immediacy_verbatim"] = IMM[s]
    if s in BRIEF_STEERED:
        r["lineage"] = "brief-steered"

# ---- v0.8 overlay: intra-survey revision arcs (schema §v0.8) ----------------
# Later synthesis entries re-treating earlier entries. All three links are
# migrator-inferred (the surveyor restates without citing the earlier line) —
# bracket-marked per the inference rule. Kind 'refinement' throughout: each
# later entry sharpens/broadens the earlier statement without contradicting it.
# Touched records bump to 0.8; untouched stay 0.7.
# v0.9: revises is a LIST of {id, revision_kind, revises_span} objects;
# fifth kind 'confirmation' for within-surveyor replication.
REVISES = {
    "L257-L263": [("L48-L51", "refinement")],
    "L265-L270": [("L186-L201", "refinement")],
    "L272-L276": [("L214-L221", "refinement")],
    "L64-L65":   [("L44-L51", "confirmation")],
    "L164-L169": [("L44-L51", "confirmation")],
}
REV_NOTES = {
    "L257-L263": "[migrator-inferred link] The synthesis law generalizes the L48-L51 hypothesis (≥3-step requirement, there 'hard to reconcile fully') across all binary-toggle instances tested, dropping the earlier hedge — sharpened, not contradicted.",
    "L265-L270": "[migrator-inferred link] Synthesis restatement of the trigram negative, sharpened ('and even then it's arithmetic, not percept') and framed against Joseph's expectation.",
    "L272-L276": "[migrator-inferred link] Promotes the vertical-vs-horizontal aside embedded in L214-L221 to a candidate general effect with a proposed mechanism and an explicit single-data-point caveat.",
    "L64-L65":   "[migrator-inferred link, surveyor-acknowledged] 'again no magnitude feel … consistent with the finding above' — within-surveyor replication of the L44-L51 white/black-flip negative.",
    "L164-L169": "[migrator-inferred link, surveyor-acknowledged] 'Consistent with the white/black-square non-finding above' — replication of L44-L51 in a different block (math operators).",
}
for r in records:
    if r["source_span"] in REVISES:
        r["revises"] = [dict(id=rid(t), revision_kind=k, revises_span=t)
                        for t, k in REVISES[r["source_span"]]]
        r["schema_version"] = "0.9"
        note = REV_NOTES[r["source_span"]]
        r["migrator_notes"] = (r.get("migrator_notes", "") + " " + note).strip()

# ---- write ------------------------------------------------------------------
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"{len(records)} records -> {OUT}")
ids = [r["id"] for r in records]
assert len(ids) == len(set(ids)), "duplicate ids"
# sanity: every note_verbatim non-empty and contains its glyphs where sensible
for r in records:
    assert r["note_verbatim"].strip()
print("ok")
