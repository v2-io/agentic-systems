#!/usr/bin/env python3
# Pass-1 migration of sonnet-survey-2.md -> extracted/sonnet-survey-2.jsonl
# note_verbatim is pulled directly from the source file by line span so it cannot drift.
import hashlib, json, os

BASE = "/Users/josephwecker-v2/src/arch/asf/empirica/glyph-magnitude-perception/data/surveys-v1"
SRC = os.path.join(BASE, "sonnet-survey-2.md")
OUT = os.path.join(BASE, "extracted", "sonnet-survey-2.jsonl")
SURVEYOR = "sonnet-survey-2"

lines = open(SRC, encoding="utf-8").read().split("\n")

def span_text(a, b):
    return "\n".join(lines[a-1:b])

def rid(span):
    return hashlib.sha256(f"survey-rec|{SURVEYOR}|{span}".encode()).hexdigest()[:16]

records = []

def rec(a, b, type_, **kw):
    span = f"L{a}-L{b}"
    r = {
        "schema_version": "0.7",
        "id_recipe": "sha256(\"survey-rec|\" + <file-basename-without-extension> + \"|\" + source_span)[:16] hex (schema v0.7)",
        "id": rid(span),
        "type": type_,
        "surveyor": SURVEYOR,
        "source_file": "sonnet-survey-2.md",
        "source_span": span,
        "lineage": "unprompted",
        "epistemics": {
            "epistemic_class": "interactive-guided-survey-anecdote",
            "felt_strength_verbatim": kw.pop("felt", "unstated"),
            "basis": kw.pop("basis", "unstated"),
            "transcription_confidence": kw.pop("tc", "clear"),
        },
    }
    rv = kw.pop("revises", None)
    if rv is not None:
        r["revises"] = rv
        r["revision_kind"] = kw.pop("revision_kind")
        r["schema_version"] = "0.8"
    bl = kw.pop("basis_list", None)
    if bl is not None:
        r["epistemics"]["basis"] = bl
    lin = kw.pop("lineage_override", None)
    if lin is not None:
        r["lineage"] = lin
    mk = kw.pop("meta_kind", None)
    if mk is not None:
        r["meta_kind"] = mk
    imm = kw.pop("immediacy_verbatim", None)
    if imm is not None:
        r["epistemics"]["felt_immediacy_verbatim"] = imm
        r["lineage"] = "brief-steered"
    for k in ("marked_speculative", "predicted_generalization", "migrator_notes", "negative_kind", "equivalence_basis", "rule_confidence", "example_chain_confidence", "scope", "tested_instance", "falsifier_implied"):
        v = kw.pop(k, None)
        if v is not None:
            r["epistemics"][k] = v
    r.update(kw)  # glyphs, codepoints, direction_note, axis, constructed, immediacy_verbatim, open, etc.
    r["note_verbatim"] = span_text(a, b)
    return records.append(r)

ARROW = "→ [migrator reading: ascending, per the surveyor's stated per-entry format L7-L9 ('sequence → direction arrow') and each glyph listing running low-to-high; the arrow itself may be only the format separator — direction is an inference, not a surveyor assertion]"

# --- meta: methodology / format definition (defines the surveyor's own vocabulary) ---
rec(1, 10, "meta",
    axis="survey methodology + per-entry format: 'strength (how confident a pairwise \"which is more\" would recover this order)' and 'immediacy note (percept-level vs symbol-lookup)' — the surveyor's own two-axis vocabulary, needed to interpret every record below",
    felt="unstated", basis="unstated",
    lineage_override="brief-steered",
    migrator_notes="Format's immediacy axis was brief-supplied (prompts/sonnet-surveyor-brief.md). Not a perceptual observation; recorded because it DEFINES this surveyor's strength/immediacy vocabulary and confirms method (append-only, one pane at a time, no prior corpus read — lineage evidence).")

# --- Enclosed Alphanumerics ---
rec(15, 23, "sequence",
    glyphs="⓪①②③④⑤⑥⑦⑧⑨⑩",
    codepoints=["U+24EA"] + [f"U+{0x2460+i:04X}" for i in range(10)],
    direction_note=ARROW,
    axis="denoted count/number",
    felt="strength: very high",
    basis="semantic-knowledge",
    immediacy_verbatim="NOT immediate — this is digit-lookup, pure symbol decoding, exactly like reading \"0,1,2...\". No fill-ramp, no size change. I had to consciously read each glyph's numeral.",
    constructed=False,
    migrator_notes="Surveyor manually moved ⓪ (U+24EA, far end of block) to the FRONT — 'semantic magnitude fully overrides codepoint order here, no hesitation at all.' Natural family, surveyor-reordered.")

rec(24, 29, "sequence",
    glyphs="⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽",
    codepoints=[f"U+{0x2474+i:04X}" for i in range(10)],
    direction_note=ARROW,
    axis="denoted count/number ('same shape as above')",
    felt="same strength [as circled digits: very high]; 'Notably *weaker feeling of magnitude* than the circled or negative-circled versions to me — the parens read more like \"footnote marker\" than \"quantity,\" even though the ordering is still perfectly recoverable.'",
    basis="semantic-knowledge",
    immediacy_verbatim="same non-immediacy [as circled digits]",
    constructed=False,
    tc="interpreted",
    migrator_notes="Strength/immediacy inherited via the surveyor's 'same shape as above' phrasing rather than restated — bracketed interpolation, hence interpreted.")

rec(31, 35, "negative",
    glyphs="Ⓐ Ⓑ Ⓒ ... Ⓩ / ⓐ ⓑ ⓒ ... ⓩ / ⒜ ⒝ ⒞ ... ⒵",
    codepoints=["U+24B6..U+24CF", "U+24D0..U+24E9", "U+249C..U+24B5"],
    axis="alphabetic, not magnitude — no sense of 'more,' just sequence identity (list-item ordering, not quantity ordering)",
    felt="no sense of 'more'",
    basis="perceived-directly",
    negative_kind="not-felt",
    migrator_notes="Also functions as an explicit scope exclusion ('Excluding from magnitude set'), but grounded in reported perception, not policy alone — so classed not-felt rather than declared-out-of-scope. Surveyor volunteers that Joseph may want alphabetic-ordering distinguished as an adjacent class.",
    tc="interpreted")

rec(37, 43, "sequence",
    glyphs="①②③...⑨⑩⑪⑫...⑳",
    codepoints=["U+2460..U+2473"],
    direction_note=ARROW,
    axis="denoted count/number (digit-lookup)",
    felt="strength: very high",
    basis="semantic-knowledge",
    immediacy_verbatim="NOT immediate; it is 100% symbolic/numeral decoding, not perceptual magnitude. 'Flagging this because it's the paradigm case of \"confident order, zero immediacy.\"'",
    constructed=False)

rec(45, 50, "sequence",
    glyphs="⓫⓬⓭...⓴",
    codepoints=["U+24EB..U+24F4"],
    direction_note=ARROW,
    axis="denoted count/number (digit-lookup); separately, filled-disc-vs-outline is 'itself binary and immediate, but doesn't establish a *graded* magnitude by itself'",
    felt="same digit-lookup mechanism [as circled: very high]",
    basis="semantic-knowledge",
    immediacy_verbatim="black-fill disc gives an *extra*, separate, immediate signal (binary, not graded); the ordering itself remains digit-lookup",
    constructed=False,
    tc="interpreted",
    migrator_notes="Strength inherited by the surveyor's 'same ... mechanism' phrasing rather than restated; the binary filled-vs-outline contrast observation is kept inside this record rather than split out.")

rec(52, 54, "sequence",
    glyphs="⓵⓶⓷⓸⓹",
    codepoints=[f"U+{0x24F5+i:04X}" for i in range(5)],
    direction_note=ARROW,
    axis="denoted count/number ('digit lookup again'); double-ring container 'a fixed decoration, no graded feel'",
    felt="'Same category as above' [digit-lookup, very high ordering confidence]",
    basis="semantic-knowledge",
    immediacy_verbatim="no graded feel [non-immediate]",
    constructed=False, tc="interpreted")

# --- Geometric Shapes ---
rec(60, 71, "sequence",
    glyphs="○◔◑◕●",
    codepoints=["U+25CB", "U+25D4", "U+25D1", "U+25D5", "U+25CF"],
    direction_note=ARROW,
    axis="filled-area ('which has more fill'); 'battery/signal-strength/pie-chart meter: empty, quarter, half, three-quarter, full'",
    felt="STRENGTH: very high — 'I'd bet heavily a pairwise \"which has more fill\" would recover this order.' 'strongest, most immediate find so far'",
    basis="perceived-directly",
    immediacy_verbatim="'this is the paradigm *immediate* case — the magnitude is perceived directly as filled-area, no symbol decoding at all'",
    constructed=False,
    migrator_notes="Surveyor flags scattered codepoints (CB, D4, D1, D5, CF) — 'pure semantic/visual assembly, codepoint adjacency gives no help here at all.'")

rec(72, 74, "equivalence",
    glyphs="◐ ◑",
    codepoints=["U+25D0", "U+25D1"],
    axis="same fill amount, no magnitude difference between them, just orientation",
    felt="unstated",
    basis="perceived-directly",
    equivalence_basis="seen",
    migrator_notes="Surveyor-volunteered as an excluded magnitude pair — a tie-structure prior (half-fill orientation variants).")

rec(76, 84, "sequence",
    glyphs="▪◽◻■",
    codepoints=["U+25AA", "U+25FD", "U+25FB", "U+25A0"],
    direction_note=ARROW,
    axis="size (small → medium-small → medium → large)",
    felt="strength: moderate-high for the *size* dimension alone, but muddied because color (black/white) is inconsistently mixed into the sample I picked",
    basis="perceived-directly",
    immediacy_verbatim="IMMEDIATE: yes, pure size perception, no lookup",
    constructed=False)

rec(81, 84, "sequence",
    revises=rid("L76-L84"), revision_kind="refinement",
    glyphs="▫◽◻□",
    codepoints=["U+25AB", "U+25FD", "U+25FB", "U+25A1"],
    direction_note=ARROW,
    axis="size, fill held constant (white-only ramp)",
    felt="'this one I trust more' [than the mixed black/white ramp]",
    basis="perceived-directly",
    immediacy_verbatim="[inherits] pure size perception, no lookup",
    constructed=True,
    migrator_notes="[revises link v0.8: same-entry refinement of the muddied ▪◽◻■ sample — surveyor-acknowledged ('this one I trust more'), so not migrator-inferred.] Surveyor-assembled repair of the previous record's confound: reordered 'for a pure test I'd want to hold fill constant.' □ noted as 'large/default — visually the biggest.'",
    tc="interpreted")

rec(86, 91, "sequence",
    glyphs="▵▴ (small) → △▲ (large)",
    codepoints=["U+25B5", "U+25B4", "U+25B3", "U+25B2"],
    direction_note=ARROW,
    axis="size ramp (small<large)",
    felt="strength high for small<large",
    basis="perceived-directly",
    immediacy_verbatim="size ramp, immediate",
    constructed=False,
    migrator_notes="Two-level size ramp given as white/black pairs at each size — the surveyor asserts small<large ONLY (2 levels); the flat 4-item codepoint list is NOT a 4-step ramp (black/white alternate within it). Fill is explicitly a separate non-magnitude axis (see companion negative record for the same span).",
    tc="interpreted")

rec(88, 91, "negative",
    glyphs="△ vs ▲ (white vs black triangle)",
    codepoints=["U+25B3", "U+25B2"],
    axis="fill (white/black) is a separate, non-magnitude axis here — 'I don't perceive black-vs-white triangle as \"more,\" just as a different category/state, unlike the circle fill ramp above where partial fill genuinely read as partial magnitude'",
    felt="not perceived as 'more'",
    basis="perceived-directly",
    negative_kind="verified-absent",
    migrator_notes="Classed verified-absent: surveyor attended to the axis and compared it against the circle fill ramp where the same dimension DOES read as magnitude.")

rec(93, 103, "sequence",
    glyphs="□▤▨▩■",
    codepoints=["U+25A1", "U+25A4", "U+25A8", "U+25A9", "U+25A0"],
    direction_note=ARROW,
    axis="fill density: empty → sparse fill → hatch → crosshatch → solid ('which reads as more filled')",
    felt="strength: moderate. Endpoints unambiguous; middle members (single hatch vs crosshatch) required a half-second of deliberation",
    basis="perceived-directly",
    immediacy_verbatim="'a *medium*-strength, still fairly immediate case, one tier below the circle ramp' — fill-density perception present but weaker/slower than the circle version",
    constructed=False)

rec(105, 108, "negative",
    glyphs="◯ vs ● (and vs ○)",
    codepoints=["U+25EF", "U+25CF", "U+25CB"],
    axis="size-of-glyph and fill are separate axes here, don't conflate — LARGE CIRCLE reads as 'big empty circle,' not smaller than WHITE CIRCLE",
    felt="'noting only as a caution'",
    basis="perceived-directly",
    negative_kind="not-felt",
    migrator_notes="An orthogonality caution against a tempting conflation (glyph size vs fill) rather than a tested-and-rejected sequence — 'noting only as a caution' reports no feel-test, so classed not-felt (verified-absent reserved for records where the surveyor reports attending to and testing the feel, e.g. the triangle-fill record).",
    tc="interpreted")

# --- Block Elements ---
rec(114, 123, "sequence",
    glyphs="▁▂▃▄▅▆▇█",
    codepoints=[f"U+{0x2581+i:04X}" for i in range(8)],
    direction_note=ARROW,
    axis="rising-bar height ('how tall is the black region') — lower N-eighths block, 1/8 → full",
    felt="STRENGTH: maximum — 'this is a literal bar-chart glyph set (sparkline characters), I'd stake everything on the ordering'",
    basis="perceived-directly",
    immediacy_verbatim="'the single most immediate sequence encountered — pure rising-bar height, reads instantly and pre-attentively, faster even than the circle-fill ramp (no shape-decoding at all)'",
    constructed=False,
    migrator_notes="Surveyor flags: 'the one case so far where codepoint order and perceptual order coincide exactly.' Nominated as THE canonical example of 'magnitude arrives in the percept itself.'")

rec(125, 131, "sequence",
    glyphs="░▒▓█",
    codepoints=["U+2591", "U+2592", "U+2593", "U+2588"],
    direction_note=ARROW,
    axis="density-of-dither ('how dense is this stipple') — light shade → medium → dark → full block",
    felt="strength: very high",
    basis="perceived-directly",
    immediacy_verbatim="immediacy: very high (density-of-dither reads instantly), though maybe a half-notch below the bar-height ramp — stipple density 'takes marginally more visual integration' than bar height; still squarely immediate/perceptual, not symbolic",
    constructed=False)

rec(133, 143, "sequence",
    glyphs="▏▎▍▌▋▊▉█",
    codepoints=["U+258F", "U+258E", "U+258D", "U+258C", "U+258B", "U+258A", "U+2589", "U+2588"],
    direction_note=ARROW,
    axis="horizontal (leftward) fill, 1/8 → full",
    felt="unstated",
    basis="perceived-directly",
    immediacy_verbatim="'Immediacy: same as the lower-block ramp — instant, pre-attentive, horizontal fill instead of vertical'",
    constructed=False,
    migrator_notes="No explicit strength rating in this entry (immediacy stated, strength not) — recorded unstated rather than inherited. The note contains a live self-correcting codepoint calculation; the surveyor's FINAL claim is that codepoint DESCENDS as fill ascends within this subrange — monotonic perceptual magnitude riding on reversed codepoint order, flagged 'per Joseph's interest in scattered/reversed-codepoint cases.'",
    tc="interpreted")

rec(145, 147, "equivalence",
    glyphs="▀/▄ and ▐/▌",
    codepoints=["U+2580", "U+2584", "U+2590", "U+258C"],
    axis="orientation variants of 'half,' not magnitude-distinct; excluded from ramps",
    felt="unstated",
    basis="perceived-directly",
    equivalence_basis="seen",
    tc="interpreted",
    migrator_notes="'noted only as orientation variants' — tie-structure prior at the half-fill point, parallel to the ◐/◑ record.")

# --- Dice ---
rec(150, 160, "sequence",
    glyphs="⚀⚁⚂⚃⚄⚅",
    codepoints=[f"U+{0x2680+i:04X}" for i in range(6)],
    direction_note=ARROW,
    axis="pip count",
    felt="strength: very high, contiguous codepoints matching pip count exactly",
    basis="perceived-directly",
    immediacy_verbatim="'IMMEDIACY: high but graded within itself' — 1-3 pips subitized instantly (true percept-level magnitude); 4-6 pips 'a tiny extra beat of \"count the dots\"' (5 and 6 recognized as *pattern*); 'mostly immediate, degrading slightly at the high end'",
    constructed=False,
    migrator_notes="Surveyor nominates this as a 'graceful degradation of immediacy' example alongside braille — immediacy as a gradient within one sequence, not a binary immediate/symbolic split.")

# --- Braille ---
rec(162, 174, "sequence",
    glyphs="⠀⠁⠃⠇⠏⠟⠿⣿",
    codepoints=["U+2800", "U+2801", "U+2803", "U+2807", "U+280F", "U+281F", "U+283F", "U+28FF"],
    direction_note=ARROW,
    axis="dot count / cumulative cell fill ('how much of the cell is dark')",
    felt="STRENGTH: high for the *chosen* members",
    basis="perceived-directly",
    immediacy_verbatim="'the clearest \"graceful degradation\" case I've found' — 0/1/2 dots subitized instantly (pure percept), 3-4 take a beat, 5-6-8 essentially density-estimation like the block-shade ramp; 'braille slides from immediate(low end) to density-estimation(high end) within one sequence'",
    constructed=True,
    migrator_notes="'hand-picked non-contiguous subsequence out of the 256-glyph bitfield block' — cherry-picked cumulative-fill diagonal; surveyor is explicit the strength claim scopes to the chosen members only.")

rec(166, 169, "negative",
    glyphs="Braille Patterns block U+2800–U+28FF generally (excluding the hand-picked diagonal)",
    codepoints=["U+2800..U+28FF"],
    axis="'codepoints are a bitmask, not remotely magnitude-ordered in general — most of this block has NO monotonic feel'",
    felt="most of this block has NO monotonic feel",
    basis="perceived-directly",
    negative_kind="not-felt",
    scope="the Braille block as a whole, in codepoint order",
    migrator_notes="Block-level negative-space observation (the schema's expected 'entire blocks' breaker) — recorded as a negative over a block rather than a glyph list; see report question.",
    tc="interpreted")

# --- Math Operators ---
rec(178, 190, "sequence",
    glyphs="< ≪ ⋘",
    codepoints=["U+003C", "U+226A", "U+22D8"],
    direction_note=ARROW,
    axis="chevron-doubling 'much' ramp — 'visual repetition-as-intensity (same mechanism as \"!!!\" for emphasis)': one wedge vs two nested vs three nested reads as 'how much' without decoding the mathematical meaning",
    felt="strength: high",
    basis="perceived-directly",
    immediacy_verbatim="'genuinely IMMEDIATE — the glyph doubles/triples its chevron the same way ▁▂▃ doubles bar height'",
    constructed=True,
    migrator_notes="Surveyor-assembled across THREE blocks (ASCII + Math Operators + ~150-codepoint gap within it): 'no adjacency at all ... and still holds together perceptually' — flagged per Joseph's scattered-codepoint interest. Classed constructed=True (assembled across families) though the semantic family is standard notation.")

rec(189, 190, "sequence",
    glyphs="> ≫ ⋙",
    codepoints=["U+003E", "U+226B", "U+22D9"],
    direction_note=ARROW,
    axis="mirror ramp on the greater-than side [of the chevron-doubling 'much' ramp]",
    felt="unstated",
    basis="perceived-directly",
    constructed=True,
    tc="interpreted",
    migrator_notes="Asserted as the mirror of the < ≪ ⋘ ramp in one line; not separately examined in the note, so strength recorded unstated rather than inherited.")

# --- Geometric Shapes Extended ---
rec(194, 211, "sequence",
    glyphs="\U0001f784 \U0001f785 \U0001f786 \U0001f787 \U0001f788 \U0001f789",
    codepoints=["U+1F784", "U+1F785", "U+1F786", "U+1F787", "U+1F788", "U+1F789"],
    direction_note=ARROW,
    axis="stroke weight/boldness increasing (Unicode names: slightly small → medium bold → bold → heavy → very heavy → extremely heavy)",
    basis_list=["perceived-directly", "name-derived"],
    felt="'immediate at a glance though the top 2-3 members (very heavy vs extremely heavy) are close enough in my rendering that I underweight my own confidence slightly for that specific adjacent pair even though the ordering overall is obvious'",
    basis="perceived-directly",
    immediacy_verbatim="immediate at a glance",
    constructed=False,
    migrator_notes="Basis is primarily perceptual with an explicit name-derived CONFIRMATION layer: 'the one place in the whole survey where Unicode's own NAMES spell out a magnitude adjective ladder — strong external confirmation that my perceptual ordering isn't just me projecting.' basis is the v0.7 ordered list [perceived-directly, name-derived]: perceptual primary, Unicode-name ladder as explicit confirmation layer.")

rec(207, 211, "generator",
    glyphs="\U0001f78c\U0001f78d\U0001f78e\U0001f78f\U0001f790\U0001f791\U0001f792\U0001f793 (squares); diamonds/lozenges analogues in the same block",
    codepoints=["U+1F78C..U+1F793", "diamond/lozenge ranges following in U+1F780-U+1F7FF"],
    axis="rule: per-shape weight ramp, tiny → extremely heavy — 'same pattern repeats' across circle/square/diamond/lozenge; 'the circle version is representative and I'd rate it strongest since round targets read fill/weight most cleanly'",
    felt="rule asserted confidently ('same pattern repeats'); members not individually examined",
    basis="perceived-directly",
    rule_confidence="stated plainly, from having seen the circle instance and the block layout",
    example_chain_confidence="lower — 'I'm treating these as one family rather than transcribing all three'; square/diamond chains not individually verified",
    tc="interpreted",
    migrator_notes="Family/generator record extracted from the tail of the circle-ramp entry; the circle instance is its own sequence record (L196-L211).")

# --- Closing self-notes ---
rec(216, 224, "meta",
    axis="stated law: strength and immediacy are orthogonal axes — 'strength answers \"would pairwise compare recover the order,\" immediacy answers \"does it recover it before I've consciously read anything\"'",
    felt="'clearly orthogonal in my experience'",
    basis="perceived-directly",
    scope="the panes surveyed in this pass; anchored by the two extremes (block-element fill ramps = maximally immediate; circled/parenthesized digits = maximally non-immediate with equal ordering confidence)",
    tested_instance="yes — multiple instances at both extremes within this survey",
    lineage_override="brief-steered",
    falsifier_implied="a sequence-population where high immediacy forces high strength or vice versa across the board (i.e., the axes co-vary)",
    migrator_notes="Lineage brief-steered: the immediacy axis this law is about was supplied by the surveyor's brief (prompts/sonnet-surveyor-brief.md, 'Joseph later added a distinction worth holding from the start'), though the orthogonality observation itself is the surveyor's own.")

rec(225, 228, "meta",
    axis="stated observation: semantic magnitude overrides codepoint order — 'happened twice cleanly': ⓪ slotting to front of ①②③..., and fill ascending while codepoint descends inside ▏▎▍▌▋▊▉█",
    felt="'twice cleanly'",
    basis="perceived-directly",
    scope="two instances in this survey; no generalization claimed beyond them",
    tested_instance="yes — the two named instances")

rec(229, 232, "meta",
    axis="'the chevron-doubling find (< ≪ ⋘) is the strongest \"scattered codepoint, strong semantic ramp\" case I found' — spanning ASCII and two separate math blocks via pure glyph-repetition-as-intensity, 'the same visual grammar as \"!!!\" or exclamation stacking'",
    felt="strongest ... I found [surveyor's own within-survey ranking]",
    basis="perceived-directly",
    scope="within this survey pass only",
    migrator_notes="Superlative kept as the surveyor's phenomenal within-pass ranking, not a corpus-level claim.")

rec(233, 237, "meta",
    revises=rid("L150-L160"), revision_kind="contradiction",
    meta_kind="coverage-gap",
    axis="honest coverage gap: dice/trigram/hexagram-adjacent territory not reached — 'flagging that as an honest gap in coverage rather than implying I checked and found nothing'; ran out of budgeted passes before Yijing hexagrams, Tai Xuan Jing, arrows, misc-technical, or a full geometric-shapes-extended pass",
    felt="explicitly flagged as unchecked, not negative",
    basis="unstated",
    scope="named unvisited blocks: Yijing hexagrams, Tai Xuan Jing, arrows, misc-technical, geometric-shapes-extended (full pass)",
    migrator_notes="Anti-record: marks absence-of-survey, NOT absence-of-feel — must not be read as negative evidence about those blocks. (Surveyor wrote 'I did not encounter the dice ... sequences yet' although a dice section exists above at L150-L160 — likely the summary was drafted before that pane or refers to trigrams/hexagrams; kept verbatim, flagged here.) [revises link v0.8: migrator-inferred — the surveyor never acknowledged the earlier dice entry when writing 'I did not encounter the dice ... sequences yet'; contradiction stands unrepaired, both records kept in full.]",
    tc="interpreted")

rec(238, 240, "meta",
    axis="methodology purity declaration: 'I deliberately did NOT read any prior survey work or other unicode material in msc/ per the brief; everything above is genuinely first-instinct'",
    felt="unstated",
    basis="unstated",
    migrator_notes="Lineage evidence supporting lineage=unprompted for every record in this file.")

with open(OUT, "w", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"{len(records)} records -> {OUT}")
ids = [r["id"] for r in records]
assert len(set(ids)) == len(ids), "id collision!"
for r in records:
    print(r["id"], r["source_span"], r["type"], (r.get("glyphs") or r.get("axis"))[:60])
