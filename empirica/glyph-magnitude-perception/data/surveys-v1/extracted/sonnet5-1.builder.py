#!/usr/bin/env python3
# Pass-1 migration builder: sonnet5-1.md -> extracted/sonnet5-1.jsonl
# The verbatim note is the primary; each record is an index into it.
import hashlib, json, sys, unicodedata

SRC = "/Users/josephwecker-v2/src/arch/asf/empirica/glyph-magnitude-perception/data/surveys-v1/sonnet5-1.md"
OUT = "/Users/josephwecker-v2/src/arch/asf/empirica/glyph-magnitude-perception/data/surveys-v1/extracted/sonnet5-1.jsonl"
LINES = open(SRC, encoding="utf-8").read().split("\n")

RECORDS = []
def R(a, b=None, typ="sequence", g=None, d=None, ax=None, st="unstated", bas="unstated",
      conf="clear", mn=None, lin="unprompted", con=False, spec=False, neg=None, pg=None, op=None):
    RECORDS.append(dict(a=a, b=b or a, typ=typ, g=g, d=d, ax=ax, st=st, bas=bas, conf=conf,
                        mn=mn, lin=lin, con=con, spec=spec, neg=neg, pg=pg, op=op))


# v0.8 revision arcs (append-only survey: later entries correcting earlier ones are structural, not anomalies).
# Targets are migrator-inferred from the surveyor's own supersession language; bracket-marked as such in emit.

# v0.9 revision arcs: span -> list of (target_span, revision_kind, link_migrator_inferred).
# Both records always kept whole; earlier felt-reports untouched. Relation vs link marked separately
# where they diverge (relation surveyor-stated, link target migrator-drawn).
REVISES = {
 "L945": [("L939","correction",False)],     # "Correcting the record rather than leaving the too-quick 'nothing found' standing"
 "L874": [("L483","correction",False)],     # header: "corrected/completed"
 "L644": [("L56","contradiction",True)],    # miss acknowledged by surveyor; target record migrator-drawn
 "L668": [("L173","contradiction",True)],   # "another miss from my first too-quick pass"; block-level target inferred
 "L803": [("L57","contradiction",True)],    # silent vs earlier "≈ ≡ — no clean feel" skip
 "L797": [("L57","contradiction",True)],
 "L724": [("L712","refinement",True)],      # "Revising my hypothesis"; target inferred
 "L1006":[("L91","contradiction",True)],    # "walked right past it"; target inferred
 "L1012":[("L91","contradiction",True)],
 "L742": [("L410","refinement",True)],      # "a specific instance I'd only gestured at abstractly before" — refines the gesture, retargeted from L411 (v0.9 re-read)
 "L748": [("L411","contradiction",True)],
 "L749": [("L411","contradiction",True)],
 # v0.9 confirmations (surveyor-acknowledged replication/endorsement of an earlier skip or read)
 "L809": [("L58","confirmation",False)],    # "confirming my earlier skip rather than second-guessing it"
 "L839": [("L63","confirmation",True)],     # "careful re-read confirms first pass" — block-level, representative target inferred
 # v0.9 explicit-extension refinements ("extends/completes the earlier X" in the surveyor's own words)
 "L632": [("L54","refinement",False)],
 "L638": [("L133","refinement",False)],
 "L177": [("L35","refinement",False)],
 "L530": [("L126","refinement",False)],
 "L430": [("L128","refinement",False)],
 "L862": [("L410","refinement",False)],
 "L766-L768": [("L252","refinement",False)],
 "L770": [("L244","refinement",False)],
 "L771": [("L254","refinement",False)],
 "L772": [("L255","refinement",False)],
 "L774": [("L256","refinement",False)],
 "L759": [("L245","refinement",False),("L246","refinement",False)],
}
# v0.7 list-form basis (ordered, surveyor's emphasis first) for double-confirmed records
BASIS_LISTS = {
 "L8": ["semantic-knowledge","perceived-directly"], "L14": ["semantic-knowledge","perceived-directly"],
 "L24": ["semantic-knowledge","perceived-directly"], "L90": ["perceived-directly","semantic-knowledge"],
 "L116": ["semantic-knowledge","perceived-directly"], "L127": ["semantic-knowledge","perceived-directly"],
 "L133": ["perceived-directly","name-derived"], "L162": ["semantic-knowledge","perceived-directly"],
 "L235": ["semantic-knowledge","perceived-directly"], "L355": ["perceived-directly","semantic-knowledge"],
 "L369": ["perceived-directly","semantic-knowledge"], "L626": ["name-derived","perceived-directly"],
 "L686": ["perceived-directly","name-derived"], "L803": ["perceived-directly","semantic-knowledge"],
 "L815": ["perceived-directly","semantic-knowledge"], "L1146-L1148": ["perceived-directly","semantic-knowledge"],
 "L1284": ["perceived-directly","semantic-knowledge"],
}
# v0.9 vein closures (sampling-stopped-by-policy) and dual-face roles
META_KIND = {"L49b":"vein-closed", "L502":"vein-closed", "L569":"vein-closed"}
ROLES = {"L49b":["meta","law"], "L502":["meta","generator"], "L526":["sequence","vein-closed"],
         "L188":["sequence","vein-closed"], "L1274":["negative","vein-closed"]}
IMMEDIACY = {  # span -> surveyor's immediacy-register words, verbatim
 "L54": "stacked-line-count is immediate",
 "L748": "this one I feel very strongly and immediately",
 "L687": "I had to think it through rather than feel it instantly",
 "L1052": "genuinely the first thing that came to mind",
}

def emit():
    out = []
    seen = set()
    for r in RECORDS:
        span = f"L{r['a']}" if r['a'] == r['b'] else f"L{r['a']}-L{r['b']}"
        base = span
        n = 2
        frag="abcdefgh"
        while span in seen:
            span = f"{base}{frag[n-1]}"; n += 1
        seen.add(span)
        rid = hashlib.sha256(("survey-rec|sonnet5-1|" + span).encode()).hexdigest()[:16]
        note = "\n".join(LINES[r['a']-1:r['b']])
        rec = {
            "id": rid,
            "schema_version": "0.8",
            "type": r['typ'],
            "epistemic_class": "interactive-guided-survey-anecdote",
            "surveyor": "sonnet5-1",
            "source_file": "data/surveys-v1/sonnet5-1.md",
            "source_span": span,
            "id_recipe": "sha256(\"survey-rec|\" + file-basename-without-extension + \"|\" + source_span)[:16] hex; letter fragments (L49b) disambiguate multi-record lines",
            "note_verbatim": note,
            "lineage": r['lin'],
            "constructed": r['con'],
            "epistemics": {
                "felt_strength_verbatim": r['st'],
                "basis": r['bas'],
                "marked_speculative": r['spec'],
                "transcription_confidence": r['conf'],
            },
        }
        if r['g'] is not None:
            glyphs = r['g']
            rec["glyphs"] = glyphs
            rec["codepoints"] = ["U+%04X" % ord(c) for c in unicodedata.normalize("NFC", glyphs) if c != " "]
        if r['d'] is not None: rec["direction_note"] = r['d']
        if r['ax'] is not None: rec["axis"] = r['ax']
        if r['pg'] is not None: rec["epistemics"]["predicted_generalization"] = r['pg']
        if r['neg'] is not None: rec["epistemics"]["negative_kind"] = r['neg']
        if r['mn'] is not None: rec["epistemics"]["migrator_notes"] = r['mn']
        if r['op'] is not None: rec["open"] = r['op']
        if span in IMMEDIACY:
            rec["epistemics"]["felt_immediacy_verbatim"] = IMMEDIACY[span]
        deltas = []
        if span in BASIS_LISTS:
            rec["epistemics"]["basis"] = BASIS_LISTS[span]
            deltas.append("basis widened to ordered list (v0.7 ratification, double-confirmed case)")
        if span in META_KIND:
            rec["meta_kind"] = META_KIND[span]
            deltas.append("meta_kind: vein-closed (v0.9 — closed-by-policy, not unexamined, not negative)")
        if span in ROLES:
            rec["roles"] = ROLES[span]
            deltas.append("roles added for dual-face content (v0.6)")
        if span in REVISES:
            rec["revises"] = []
            for tgt, kind, inferred in REVISES[span]:
                entry = {"id": hashlib.sha256(("survey-rec|sonnet5-1|" + tgt).encode()).hexdigest()[:16],
                         "revision_kind": kind, "revises_span": tgt}
                if inferred: entry["id"] = "[migrator-inferred] " + entry["id"]
                rec["revises"].append(entry)
            deltas.append("revises migrated to v0.9 list form (+arc sweep: extensions/confirmations)")
        if deltas or "v0.8->0.9 delta" in (rec["epistemics"].get("migrator_notes") or ""):
            rec["schema_version"] = "0.9"
            note = "v0.8->0.9 delta: " + "; ".join(deltas)
            mn = rec["epistemics"].get("migrator_notes")
            rec["epistemics"]["migrator_notes"] = (mn + ". " + note) if mn else note
        out.append(json.dumps(rec, ensure_ascii=False))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"{len(out)} records -> {OUT}")

# ---- records appended below ----
# Number Forms
R(7, mn="Extraction conventions (stated once, per schema v0.6): multi-record lines disambiguated by letter fragment appended to span (L49b); glyph linearization preserves the surveyor's written order (including ↓ ladders) rather than schema's canonical-ascending — verbatim wins; block-intro framing prose included in the first record's span where a record leans on it", g="⅐⅑⅒", d="↓ decreasing magnitude (value shrinks as denominator grows)", ax="\"More\" = value of the fraction", st="high", bas="semantic-knowledge")
R(8, g="⅛⅜⅝⅞", d="↑ increasing", ax="fraction value; clean arithmetic ladder", st="very high", bas="semantic-knowledge", mn="dual basis: surveyor also notes 'visually the numerator glyph itself increases'")
R(9, g="⅙⅚", d="↑", ax="fraction value", st="high (only two terms, but unambiguous)", bas="semantic-knowledge")
R(10, g="⅕⅖⅗⅘", d="↑", ax="fraction value, same family as eighths", st="very high", bas="semantic-knowledge")
R(11, g="ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ", d="↑", ax="Roman numerals I–XII", st="very high, extremely canonical", bas="semantic-knowledge")
R(12, g="ⅠⅬⅭⅮⅯ", d="↑", ax="Roman numeral values 1,50,100,500,1000", st="high once you know Roman numeral values", bas="semantic-knowledge", pg="I'd flag this weaker for a 'fresh agent pairwise' test than I–XII, even though I'm personally very sure")
R(13, g="ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻ", d="↑, same as uppercase", ax="lowercase small roman numeral series", st="very high", bas="semantic-knowledge")
R(14, g="ↀↁↂ", d="↑", ax="large Roman numeral values 1000,5000,10000", st="moderate", bas="semantic-knowledge", mn="surveyor notes shape complexity independently supports ↑")
R(15, g="⅟↉", typ="sequence", ax="denominator grows → value shrinks (constructed cross-sequence seed)", st="high if compared as raw fraction magnitude", bas="semantic-knowledge", con=True, spec=True, op="surveyor flags gestalt 'gliding' likely weaker than same-family fraction sets")
# Miscellaneous Symbols
R(19, g="⚀⚁⚂⚃⚄⚅", d="↑", ax="dot-count (die faces 1–6)", st="very high", bas="perceived-directly", lin="brief-steered")
R(20, g="⚆⚇⚈⚉", d="weak ↑ by dot count; only valid as two separate pairs not one 4-chain", ax="dot count", st="medium", bas="perceived-directly")
R(21, 22, g="⚊⚌", d="↑", ax="line/stroke count (monogram → digram); yin/yang semantic ordering a separate much weaker axis", st="high on stroke-count", bas="perceived-directly", con=True, mn="two axes reported in one note: stroke-count (high) and esoteric yin/yang semantic (much weaker)")
R(23, g="⚬⚪", d="⚬ < ⚪ ↑", ax="named size (medium small vs medium)", st="high on the literal 'small' in the name", bas="name-derived", mn="surveyor: 'visually the point size difference is subtle in most fonts'")
R(24, g="♩♪♫♬", d="↑", ax="rhythmic density/subdivision", st="high for anyone with music literacy, otherwise opaque", bas="semantic-knowledge", mn="dual: flag count visually tracks it, reinforcing. SOURCE ANOMALY (unrepaired in raw): the note's glyph run doubles ♫ (♩♪♫♫♬); glyph field reads it as the 4-step ladder")
R(25, g="♳♴♵♶♷♸♹", d="↑", ax="denoted number (plastic types 1–7, embedded digit)", st="very high", bas="perceived-directly")
R(26, g="☆★", typ="question", ax="candidate fill-density axis (empty→full)", st="low as 'magnitude' per se", bas="perceived-directly", spec=True, op="watch for white/black doublets across the block; 'uncertain, flagging rather than asserting'")
R(27, g="⚹⚺⚻⚼", typ="negative", ax="underlying astrological angles exist but glyphs give zero visual cue", st="none visually", bas="semantic-knowledge", neg="verified-absent")
R(28, g="⛀⛁", d="↑ within each color pair", ax="man→king promotion/rank-up", st="medium, requires checkers knowledge", bas="semantic-knowledge")
R(29, g="♔♕♖♗♘♙", typ="negative", ax="chess piece values exist but the glyphs themselves don't communicate it", st="flagging only", bas="semantic-knowledge", neg="verified-absent")
# Geometric Shapes
R(33, g="○◔◐◕●", d="↑ (0%,25%,50%,75%,100% fill)", ax="fill fraction (moon-phase/pie-chart/battery progression)", st="very high, one of my most confident finds so far", bas="perceived-directly")
R(34, g="◌○◯", d="tentative ↑", ax="presence/solidity then size", st="low-medium, flagging rather than asserting strongly", bas="perceived-directly", spec=True, con=True)
R(35, g="▪◽◻", d="↑", ax="named-size ladder: small < medium small < medium", st="high", bas="name-derived", mn="black/white pairs at each size (▪▫ ◽◾ ◻◼); surveyor notes rendered size does increase to match", lin="brief-steered")
R(36, g="▴▲", d="↑ by size", ax="'regular vs small' naming split, per rotation direction", st="high", bas="name-derived", op="surveyor: 'very possibly a general cross-shape axis (regular > small) worth watching for elsewhere'", lin="brief-steered")
R(37, g="▬▮", typ="negative", ax="orientation change only — rotation ≠ magnitude", neg="verified-absent", mn="surveyor-volunteered non-example 'to keep myself honest'")
R(38, g="◇◈", d="↑", ax="nestedness/fill ('containing' relationship)", st="medium (only 2 terms)", bas="perceived-directly", lin="brief-steered")
R(39, g="○◎◉●", typ="question", d="candidate ↑", ax="amount of black/fill accumulating toward the center outward", st="low-medium, real uncertainty on ◎ vs ◉ placement", bas="perceived-directly", spec=True, op="what would settle it: internal ordering of ◎ vs ◉ — a pre-made validation-battery item", lin="brief-steered")
R(40, g="◰◱◲◳", typ="cyclic", ax="clock-like rotational sweep; directional 'feel' (clockwise) adjacent to magnitude but not 'more'", bas="perceived-directly")
# Enclosed Alphanumerics
R(44, g="⓪①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳", d="↑", ax="circled 0–20", st="very high", bas="semantic-knowledge", mn="semantic order overwhelms codepoint order (⓪ at U+24EA)", lin="brief-steered")
R(45, g="⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇", d="↑", ax="parenthesized 1–20, denoted number", st="very high", bas="semantic-knowledge")
R(46, g="⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖⒗⒘⒙⒚⒛", d="↑", ax="digit-full-stop 1–20", st="very high", bas="semantic-knowledge")
R(47, g="①⑴⒈", typ="equivalence", ax="same value, different enclosure dress", bas="semantic-knowledge", mn="seen (surveyor compared the styles directly)")
R(48, g="⓿⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴", d="⓿ → ⓫ → ⓴ ↑", ax="negative (white-on-black) circled numbers", st="very high", bas="semantic-knowledge", mn="⓿ at U+24FF out of numeric order — second scattered-codepoint case", lin="brief-steered")
R(49, g="⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾", d="↑", ax="double circled digits 1–10", st="very high", bas="semantic-knowledge")
R(49, typ="meta", ax="stated law: whenever unicode gives an enclosure/decoration style applied to digits, the digit-order sequence is essentially guaranteed", bas="perceived-directly", mn="scope: decorated-digit families; surveyor tested five visual dialects in this block; also a meta-efficiency note ('I probably don't need to belabor every future decorated digit family')", op="implied falsifier: a decorated-digit family whose order does not follow digit order")
R(50, g="⒜Ⓐⓐ", typ="negative", ax="alphabetical order is ordinal, not magnitude", neg="declared-out-of-scope", mn="boundary case surveyor chose NOT to include; 'later in the alphabet' felt like a different, weaker kind of ordering")
# Mathematical Operators (first pass)
R(54, g="∫∬∭", d="↑", ax="stacked-line-count (integral count)", st="very high", bas="perceived-directly")
R(55, g="√∛∜", d="↓ as root-value / ↑ by root-index — direction depends on which 'more' you mean", ax="root index / complexity of the little number", st="high", bas="semantic-knowledge", op="surveyor flags the direction ambiguity itself as the interesting note")
R(56, g="<≤≪", typ="negative", ax="different relations, not a magnitude chain", neg="not-felt", mn="later partially superseded: the <≪⋘⪢⫸ emphasis ladder found at L644")
R(57, g="≈≡", typ="negative", ax="no clean feel", neg="not-felt", mn="later revisited: =≡≣ bar-count ladder found at L803, ∼≈≋ at L797")
R(58, g="⊂⊆", typ="negative", ax="no strong magnitude feel", neg="not-felt", mn="skip re-confirmed on careful re-read at L809")
R(59, g="⋮⋯⋰⋱", typ="negative", ax="just rotations, no magnitude; tempting-looking non-example", neg="verified-absent")
# Arrows
R(63, g="→⇒⇉⇛⇶", d="↑", ax="how many/how thick the arrow shaft — intensity/emphasis/certainty", st="high", bas="perceived-directly", op="surveyor: same pattern works for any direction (←⇐⇇⇚ etc)")
R(64, g="→⇒", d="↑ in emphasis/strength/certainty", ax="single vs double-line arrow ('implies strongly')", st="high", bas="perceived-directly")
R(65, g="⇀⇉", typ="negative", ax="different arrow types, not a clean magnitude feel", neg="not-felt")
R(66, g="⇠→", d="tentative ↑", ax="dashed feels tentative/weak, solid feels definite/strong", st="medium", bas="perceived-directly", spec=True)
R(67, g="↺↻", typ="negative", ax="direction only, no magnitude", neg="not-felt")
# Dingbats
R(71, g="❘❙❚", d="↑", ax="named weight ladder, thickness directly visible", st="very high", bas="perceived-directly")
R(72, g="❶❷❸❹❺❻❼❽❾❿", d="↑", ax="negative circled digits 1–10", st="very high", bas="semantic-knowledge")
R(73, g="➀➁➂➃➄➅➆➇➈➉", d="↑", ax="circled sans-serif digits 1–10", st="very high", bas="semantic-knowledge")
R(74, g="✓✔", d="↑", ax="weight = emphasis", st="high", bas="perceived-directly")
R(75, g="✕✖", d="↑", ax="weight", st="high", bas="perceived-directly")
R(76, g="✗✘", d="↑", ax="weight", st="high", bas="perceived-directly")
R(77, g="✱✲✳", typ="negative", ax="not a clean magnitude", neg="not-felt")
R(78, g="✦✧", typ="negative", ax="fill toggle not magnitude", neg="not-felt")
R(79, typ="negative", ax="single pictographs, no sequence", neg="not-felt")
# Box Drawing
R(83, g="─━", d="↑", ax="weight/thickness", st="very high", bas="perceived-directly")
R(84, g="│┃", d="↑", ax="weight/thickness", st="very high", bas="perceived-directly")
R(85, g="┈┄", typ="negative", ax="dash-count gives tentative 'finer/coarser' feel but not clean magnitude", neg="not-felt")
R(86, g="─═", d="↑", ax="'double' reads as more/stronger than single, same weight-family", st="high", bas="perceived-directly")
# Spacing Modifier Letters
R(90, g="˥˦˧˨˩", d="↓", ax="visual height directly tracks semantic pitch-height — both cues agree", st="very high", bas="perceived-directly")
R(91, typ="negative", ax="rest of block (IPA diacritics/accents): no other clean magnitude feel", neg="not-felt", mn="later corrected: ˑː vowel-length pair (L1006) and ˌˈ stress marks (L1012) found on re-visit")
# Superscripts and Subscripts
R(95, g="⁰⁴⁵⁶⁷⁸⁹", d="↑", ax="plain digit ladder", st="very high", bas="semantic-knowledge")
R(96, g="₀₁₂₃₄₅₆₇₈₉", d="↑", ax="digit ladder", st="very high", bas="semantic-knowledge")
R(97, g="⁵₅", typ="equivalence", ax="same value, different position — not a magnitude relationship", bas="semantic-knowledge")
# Braille
R(101, g="⠀⠁⠃⠇⠏⠟⠿", d="↑", ax="accumulating dot-count/fill-density — reads like a progress-bar filling in", st="high", bas="perceived-directly", con=True, mn="scattered codepoints, sequence assembled by surveyor")
R(102, typ="meta", ax="rest of 256-cell braille block is combinatorial (all dot-subsets); the fill-count axis is the real find", bas="perceived-directly")
# Block Elements
R(106, g="▁▂▃▄▅▆▇█", d="↑", ax="bar height directly = magnitude (canonical sparkline set)", st="extremely high", bas="perceived-directly")
R(107, g="░▒▓█", d="↑", ax="fill-density/darkness ramp, named light/medium/dark", st="extremely high", bas="perceived-directly")
R(108, g="▏▎▍▌▋▊▉█", d="↑", ax="left-fill fraction (terminal progress bars)", st="extremely high", bas="perceived-directly")
# General Punctuation
R(112, g="‐–—", d="↑", ax="literal length increases", st="very high", bas="perceived-directly")
R(113, g="․‥…", d="↑", ax="dot count", st="very high", bas="perceived-directly")
R(114, g="†‡", d="↑", ax="footnote-marker escalation, weight/count", st="high", bas="perceived-directly")
R(115, g="′″‴⁗", d="↑", ax="tick-count", st="very high", bas="perceived-directly")
R(116, g="‰‱", d="↑", ax="finer-grained ratio / more zeros; one more '0' loop appended", st="high", bas="semantic-knowledge", mn="dual: visual loop-count also cited")
R(117, g="⁚⁖⁘⁙", d="↑", ax="dot count", st="high", bas="perceived-directly", mn="scattered/non-adjacent codepoints within the block")
# Latin-1 Supplement
R(121, g="¹²³", d="↑", ax="plain digits", st="very high", bas="semantic-knowledge")
R(122, g="¼½¾", d="↑", ax="fraction ladder", st="very high", bas="semantic-knowledge")
# CJK size/number words (steered: Joseph's "tiny/small/medium/large" hypothesis named in header L124)
R(126, g="小中大", d="↑", ax="lexical size words small/medium/large — purely lexical/semantic, glyphs give almost no visual size cue", st="high for me", bas="semantic-knowledge", lin="brief-steered", mn="header L124: 'per your tiny/small/medium/large hypothesis' — Joseph-steered section; surveyor flags the visual/lexical distinction honestly")
R(127, g="一二三四五", d="↑", ax="Chinese numerals 1–5; 一二三 stroke count itself visually tracks magnitude before breaking at 四", st="very high (一二三 alone: very high on both semantic AND visual/stroke-count grounds)", bas="semantic-knowledge", lin="brief-steered", mn="dual basis explicitly stated for the first three")
R(128, g="十百千万", d="↑", ax="powers of ten words", st="high semantically, no visual size cue", bas="semantic-knowledge", lin="brief-steered")
# Asterisk/star point-count scan (self-directed revisit)
R(132, g="*⁑⁂", d="↑", ax="literal asterisk-count", st="very high", bas="perceived-directly")
R(133, g="✦✶✳✴✹✺", d="↑", ax="named point-count, AND visually countable", st="very high", bas="perceived-directly", con=True, mn="scattered-codepoint sequence assembled within Dingbats", lin="brief-steered")
# Domino Tiles
R(137, g="🀱🀲🀳🀴🀵🀶🀷", d="↑", ax="pip count on one side climbs, dice-like", st="very high", bas="perceived-directly")
R(138, g="🀰🀱", d="↑ with the back-tile as the true minimum", ax="hidden < zero pips ('less than zero' anchor)", st="medium-high, satisfying but requires accepting 'hidden' as 'least'", bas="perceived-directly", con=True)
# Playing Cards
R(142, g="🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪", d="↑ (reading ace-low)", ax="pip count", st="very high", bas="semantic-knowledge", mn="surveyor flags: unicode glyphs mostly render as generic card icons, so visual cue weaker than semantic")
R(143, g="🂪🂫🂭🂮", d="↑", ax="conventional card rank, purely semantic/learned", st="very high", bas="semantic-knowledge")
# Currency Symbols
R(147, typ="negative", ax="each glyph denotes a different currency's arbitrary unit, no shared magnitude axis", neg="verified-absent")
# Miscellaneous Technical
R(151, g="⏗⏘⏙", d="↑", ax="count embedded in the name (tri/tetra/penta-seme)", st="high", bas="name-derived", mn="surveyor: glyphs themselves don't visually telegraph it clearly")
R(152, g="▶⏩⏭", d="↑", ax="media-player speed/intensity convention; triangle-count tracks 'more speed'", st="high", bas="semantic-knowledge")
R(153, g="⏺⏹", typ="negative", ax="distinct UI functions, no magnitude", neg="not-felt")
# Enclosed CJK
R(157, g="㈠㈡㈢㈣㈤㈥㈦㈧㈨㈩", d="↑", ax="parenthesized ideograph 1–10", st="very high", bas="semantic-knowledge")
R(158, g="㉈㉉㉊㉋㉌㉍㉎", d="↑", ax="tens ladder, named directly", st="very high", bas="name-derived")
# Musical Symbols
R(162, g="𝅝𝅗𝅥𝅘𝅥𝅘𝅥𝅮𝅘𝅥𝅯𝅘𝅥𝅰𝅘𝅥𝅱𝅘𝅥𝅲", d="↓ duration (or ↑ subdivision-count/speed)", ax="note duration ladder", st="very high, extremely canonical for anyone with music literacy", bas="semantic-knowledge", mn="dual: flag-count on stem visually tracks it; glyphs include combining sequences")
R(163, g="𝆏𝆐𝆑", d="↑", ax="soft→loud dynamics ladder", st="very high", bas="semantic-knowledge")
R(164, g="𝆒𝆓", typ="negative", ax="directional markings, not a magnitude pair", neg="not-felt")
# Combining Diacritical Marks for Symbols
R(168, g="⃛⃜", d="↑", ax="dot count", st="medium (only two terms)", bas="perceived-directly")
R(169, typ="negative", ax="nothing else strong here", neg="not-felt")
# Supplemental Mathematical Operators (first pass — later heavily corrected)
R(173, typ="negative", ax="mostly decorated-variant operators, no shared magnitude axis jumped out", neg="not-felt", mn="superseded in part by later finds: ⧺⧻ (L228), ⋘-nesting (L644), ⩵⩶ (L668) — surveyor self-documents the first pass as too quick")
# Miscellaneous Symbols and Arrows
R(177, g="⬝⬛", d="↑", ax="named size: very small vs large square (extends the small/medium ladder across two blocks)", st="high", bas="name-derived", con=True)
R(178, g="⭑⭐", d="tentative ↑ by size", ax="medium > small; mixing fill-color and size muddies it", st="medium", bas="name-derived", spec=True)
R(179, g="⬅⬆➡⬇", typ="negative", ax="direction only", neg="not-felt")
# Mahjong Tiles
R(183, g="🀙🀚🀛🀜🀝🀞🀟🀠🀡", d="↑", ax="visual pip-count (grid of dots), same class as dice/dominoes", st="very high", bas="perceived-directly")
R(184, g="🀇🀐", d="↑ (1–9 in each suit)", ax="characters/bamboos suits, same ordering", st="very high semantically", bas="semantic-knowledge", mn="surveyor: visual cue weaker than the circles suit")
# Enclosed Alphanumeric Supplement
R(188, g="🄁🄂🄃🄄🄅🄆🄇🄈🄉🄊", d="↑", ax="digit-comma ladder", st="very high", bas="semantic-knowledge", mn="carries a meta-efficiency note: 'not belaboring further, the decorated-digit pattern is now well established'")
# Moon phases
R(192, g="🌑🌒🌓🌔🌕", d="↑", ax="illuminated-fraction directly visible", st="extremely high", bas="perceived-directly", mn="surveyor links it as emoji cousin of ○◔◐◕● — cross-confirmation of fill-progression")
R(193, g="🌕🌖🌗🌘🌑", d="↓", ax="waning half of the same cycle", st="extremely high", bas="perceived-directly")
# Emoticons
R(197, g="😀😁😂", d="↑ escalation of joy/mouth-openness/eye-scrunch", ax="joy escalation", st="medium", bas="perceived-directly", spec=True, op="surveyor genuinely uncertain about 🙂😐 placement and 'not fully sure why 😂 reads as more' — self-flagged 'not sure why but it feels ordered' case", lin="brief-steered")
R(198, g="😢😭", d="↑", ax="single tear vs streaming tears + wailing mouth", st="high", bas="perceived-directly")
R(199, g="😮😯😲😱", d="tentative ↑ by surprise/shock intensity", ax="shock intensity", st="low-medium, less confident than the crying pair", bas="perceived-directly", spec=True)
# Spaces sub-block
R(203, typ="sequence", ax="named width ladder (fraction-of-em); invisible glyphs — 'named magnitude, unseeable' edge case", st="high on the name", bas="name-derived", op="no way to perceive the ordering by looking at rendered characters — edge case the schema may want a flag for", lin="brief-steered")
# Letterlike Symbols
R(207, g="ℵℶℷℸ", d="↑", ax="transfinite cardinal notation, purely notational/learned", st="high for me", bas="semantic-knowledge")
R(208, typ="negative", ax="rest of block: distinct named constants, each singular", neg="verified-absent")
# Misc Math Symbols-A
R(214, g="⟨⟪", d="↑", ax="single-to-double weight pattern", st="medium", bas="perceived-directly")
R(215, typ="negative", ax="one-off relational/lattice notation, no shared axis", neg="not-felt")
# Supplemental Arrows
R(221, g="⟶⟹", d="↑", ax="single/double weight", st="medium", bas="perceived-directly")
R(222, typ="negative", ax="dense combinatorial arrow-decoration, no new axis beyond weight/multiplicity", neg="verified-absent")
# Misc Math Symbols-B
R(228, g="⧺⧻", d="↑", ax="plus-sign count directly named", st="high", bas="perceived-directly")
R(229, typ="negative", ax="one-off relational/geometric notation variants", neg="not-felt")
# CJK Symbols and Punctuation
R(235, g="〡〢〣〤〥〦〧〨〩〸〹〺", d="↑", ax="Hangzhou numerals — tally-mark-style ladder, strokes accumulate for 1-3", st="very high", bas="semantic-knowledge", mn="dual: visual stroke-accumulation cited for 1-3")
R(236, g="〈《", d="↑", ax="single/double weight", st="medium", bas="perceived-directly")
R(237, g="〇〡", typ="sequence", ax="ideographic zero as natural anchor below Hangzhou one", bas="semantic-knowledge", con=True)
# CJK Compatibility squared units (first pass)
R(243, g="㌰㌨㍉㌢㌔㍋㌐", d="↑", ax="order-of-magnitude SI-prefix ladder (pico→giga) hiding as squared loanwords", st="very high", bas="name-derived", con=True, mn="scattered non-adjacent codepoints, assembled by surveyor", lin="brief-steered")
R(244, g="㎜㎝㎞", d="↑", ax="length-scale ladder", st="very high", bas="semantic-knowledge")
R(245, g="㎟㎠㎡㎢", d="↑", ax="area-scale ladder", st="very high", bas="semantic-knowledge")
R(246, g="㎣㎤㎥㎦", d="↑", ax="volume-scale ladder", st="very high", bas="semantic-knowledge")
R(252, g="㎐㎑㎒㎓", d="↑", ax="frequency-scale", st="very high", bas="semantic-knowledge")
R(253, g="㎎㎏", d="↑", ax="mass-scale", st="very high", bas="semantic-knowledge")
R(254, g="㎩㎪㎫", d="↑", ax="pressure-scale", st="very high", bas="semantic-knowledge")
R(255, g="㎰㎱㎳", d="↑", ax="time-scale", st="very high", bas="semantic-knowledge")
R(256, g="㎽㎾㎿", d="↑", ax="power-scale", st="high", bas="semantic-knowledge", mn="surveyor notes the mW/MW abbreviation collision, ordering still clear from context")
# Halfwidth/Fullwidth
R(262, g="０１２３４５６７８９", d="↑", ax="fullwidth digit ladder", st="very high", bas="semantic-knowledge")
R(263, typ="negative", ax="rest is letter-form duplicates, no magnitude axis", neg="verified-absent")
# Enclosed Ideographic Supplement
R(269, g="🈩🈔🈪", d="↑", ax="squared Chinese numerals 1,2,3 — scattered codepoints hiding the ladder", st="high", bas="semantic-knowledge", con=True)
R(270, typ="negative", ax="single-ideograph business/notice symbols, no shared axis", neg="verified-absent")
# Alchemical
R(276, typ="negative", ax="substance/process identity symbols; -2/-3 suffixes are historical variants, not magnitude", neg="verified-absent")
# Misc Symbols and Pictographs part 1
R(282, g="🌣🌤🌥🌦", d="↑", ax="cloud-cover-increasing weather ladder", st="very high", bas="perceived-directly")
R(284, typ="negative", ax="fruit/plant/food glyphs: distinct referents, no shared axis", neg="not-felt")
# part 2
R(290, g="🔇🔈🔉🔊", d="↑", ax="THE canonical volume-icon ladder, wave-count directly visible", st="extremely high", bas="perceived-directly")
R(291, g="🔅🔆", d="↑", ax="low/high brightness, named directly", st="very high", bas="perceived-directly")
R(292, g="🔍🔎", typ="negative", ax="direction not magnitude — tempting-looking non-example", neg="verified-absent")
R(298, g="🔸🔶", d="↑", ax="named size, same color", st="very high", bas="name-derived")
R(299, g="🔹🔷", d="↑", ax="named size, blue set", st="very high", bas="name-derived")
R(300, g="🔼🔺", d="🔼(small) < 🔺(regular) ↑", ax="named size; reversed in codepoint order", st="high", bas="name-derived")
# Yijing
R(306, typ="negative", ax="every hexagram has exactly six lines — no visual complexity gradient; binary-value order corresponds to no perceptible 'more'", neg="verified-absent")
# Keycaps
R(310, g="0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟", d="↑", ax="keycap digits, then single scattered codepoint for ten", st="very high", bas="semantic-knowledge", mn="combining sequences for 0-9 (digit+VS16+U+20E3), single codepoint for 🔟")
# Aegean
R(316, g="𐄇𐄈𐄉𐄊𐄋𐄌𐄍𐄎𐄏", d="↑", ax="Aegean 1–9", st="very high", bas="name-derived")
R(317, g="𐄐𐄑𐄒𐄓𐄔𐄕𐄖𐄗𐄘", d="↑", ax="tens", st="very high", bas="name-derived")
R(318, g="𐄙𐄚𐄛𐄜𐄝𐄞𐄟𐄠𐄡", d="↑", ax="hundreds", st="very high", bas="name-derived")
R(319, g="𐄢𐄣𐄤𐄥𐄦𐄧𐄨𐄩𐄪", d="↑", ax="thousands", st="very high", bas="name-derived")
R(320, typ="meta", ax="the full run 𐄇→𐄪 is a huge entirely adjacent-codepoint ladder — purest number system found, though glyphs don't visually communicate scale", bas="name-derived")
# Cross-pane composites round 1 (steered: header L322 'per your invitation')
R(324, g="⬝▪◽◻⬛", d="↑", ax="5-step named-size square ladder assembled from two blocks", st="high", bas="name-derived", con=True, lin="brief-steered")
R(325, g="▫░▒▓█", d="↑", ax="shade ramp extended backward to an empty/outline-only anchor", st="high", bas="perceived-directly", con=True, lin="brief-steered")
R(326, g="🔅░▒▓█🔆", typ="meta", ax="looser cross-domain resonance: brightness, sound-volume, shade-fill share one perceptual 'intensity dial' gestalt", bas="perceived-directly", con=True, lin="brief-steered", mn="surveyor explicitly declines a strength rating — 'more a felt analogy than a strict single sequence'. SOURCE ANOMALY: note doubles 🔉 in its volume-run aside (🔇🔈🔉🔉🔊)")
R(327, g="⚬○◔◐◕●⬤🌕", d="↑", ax="fullest assembled circle-fill progression, three blocks plus emoji plane", st="high", bas="perceived-directly", con=True, lin="brief-steered")
R(328, typ="meta", ax="'fraction of a whole' axis recurs at least three separate ways; structural echo, not one glidable sequence", bas="perceived-directly", lin="brief-steered")
# Greek Acrophonic
R(334, g="𐅀𐅁𐅂", d="↑", ax="fraction-to-whole ladder", st="very high", bas="name-derived")
R(335, g="𐅃𐅄𐅅𐅆𐅇", d="↑", ax="order-of-magnitude ladder (base-5/10 acrophonic)", st="very high", bas="name-derived")
R(336, typ="negative", ax="rest fragments into city-state variants at overlapping values — no single clean ladder", neg="verified-absent")
# Ancient Symbols
R(342, g="𐆚𐆘𐆗𐆖", d="↑", ax="Roman coin-value ladder, purely notational/learned", st="medium", bas="semantic-knowledge", mn="surveyor: 'I only know this from historical trivia rather than perceiving it'")
R(343, g="𐆐𐆑𐆒𐆓𐆔", typ="negative", ax="fractional weight units; values not memorized well enough to assert order — skipping rather than guessing", neg="declared-out-of-scope", mn="abstention from insufficient knowledge, not a perceptual absence")
# Coptic Epact
R(349, typ="sequence", g="𐋡𐋢𐋣𐋤𐋥𐋦𐋧𐋨𐋩", d="↑", ax="decimal ladder (ones/tens/hundreds), same pattern as Aegean/Greek", st="very high", bas="name-derived", mn="record covers the whole three-tier system; surveyor notes the 'ancient numeral system = clean adjacent ladder' recurring structural fact once rather than re-explaining")
# Counting Rods
R(355, g="𝍠𝍡𝍢𝍣", d="↑", ax="accumulating count of vertical rods — visual+semantic double-confirmed", st="very high", bas="perceived-directly")
R(356, g="𝍲𝍳𝍴𝍵𝍶", d="↑", ax="classic tally marks, accumulating strokes", st="very high", bas="perceived-directly")
R(357, g="𝍷𝍸", d="↑", ax="tally one vs grouped tally five", st="high", bas="perceived-directly")
# Chess Symbols (neutral)
R(363, g="🨀🨁🨂🨃🨄🨅", d="↓", ax="conventional piece-value/importance ranking; codepoint order happens to match", st="high", bas="semantic-knowledge", mn="purely semantic/learned, no visual size cue — contrast with classic chess block where no order was perceived")
# Mayan
R(369, g="𝋠𝋡𝋢𝋣𝋤𝋥𝋦𝋧𝋨𝋩𝋪𝋫𝋬𝋭𝋮𝋯𝋰𝋱𝋲𝋳", d="↑", ax="bar-and-dot system visually accumulates — visual+semantic double-confirmed; includes a real zero glyph", st="very high", bas="perceived-directly")
# Cuneiform
R(375, g="𒐀𒐁𒐂𒐃𒐄𒐅𒐆𒐇", d="↑", ax="ASH wedge marks visually accumulate", st="medium-high", bas="perceived-directly", pg="rendering support inconsistent enough that 'I'm less confident a fresh pairwise comparison would reliably recover the order'")
R(376, typ="negative", ax="Sumerian base-60 positional units: place-value multipliers, too complex/unfamiliar to assert a perceptual order", neg="declared-out-of-scope")
# Medals
R(382, g="🥇🥈🥉", d="↓ (ranking decreasing)", ax="gold>silver>bronze; color convention independently reinforces", st="very high", bas="semantic-knowledge")
# Battery
R(388, g="🪫🔋", d="↑", ax="low vs (implicitly full) battery; low glyph shows mostly-empty cell", st="high", bas="perceived-directly", mn="codepoints extremely far apart — scattered-across-Unicode-eras example")
# Transport
R(392, typ="negative", ax="distinct vehicle/location pictographs, no shared magnitude axis", neg="verified-absent")
# Busts
R(398, g="👤👥", d="↑", ax="literal head-count visible in glyph", st="high", bas="perceived-directly")
R(404, g="👁👀", d="↑", ax="one eye vs two — semantic 'more' runs opposite codepoint order", st="high", bas="perceived-directly", lin="brief-steered")
# Combining Diacritical Marks
R(410, g="́̋", typ="sequence", d="↑", ax="single vs double accent (acute→double acute, grave→double grave)", st="high", bas="perceived-directly", mn="glyph field carries acute + double acute as representatives; note covers both the acute and grave families")
R(411, typ="negative", ax="diverse phonetic/tone marks without a shared count axis", neg="not-felt", mn="partially superseded: low line/double low line (L748) and stroke overlays (L749) found on slow re-read contradict this; the dot-above/diaeresis find (L742) refines the L410 gesture rather than this record")
# Tamil
R(417, g="௦௧௨௩௪௫௬௭௮௯", d="↑", ax="digit ladder", st="very high", bas="semantic-knowledge")
R(418, g="௰௱௲", d="↑", ax="ten/hundred/thousand distinct symbols", st="very high", bas="name-derived")
# Egyptian
R(424, typ="question", ax="Egyptian numeral hieroglyphs form a famous escalating ladder, but Gardiner-code names make codepoints unverifiable in this pass", bas="semantic-knowledge", op="what would settle it: mapping Gardiner sign codes to the numeral glyphs; surveyor refused to assert unverified U+ values")
# Chinese large numbers
R(430, g="十百千万億兆", d="↑", ax="powers of ten extended to 10^12", st="high semantically", bas="semantic-knowledge")
# Control Pictures
R(436, typ="negative", ax="one symbol per control character, no shared axis", neg="verified-absent")
# Geometric Shapes Extended (block intro L440-442 folded into per-ladder records)
R(442, 444, g="🞄🞅🞆🞇🞈🞉", d="↑", ax="full named weight ladder for one shape family (circle)", st="very high", bas="name-derived")
R(445, g="🞌🞍🞎🞏🞐🞑🞒🞓", d="↑", ax="8-step named weight ladder — 'the fullest, cleanest weight-ladder I've found in the whole survey'", st="very high", bas="name-derived")
R(446, g="🞗🞘🞙", d="↑", ax="named size ladder (diamond)", st="very high", bas="name-derived")
R(447, g="🞝🞞🞟", d="↑", ax="named size ladder (lozenge)", st="very high", bas="name-derived")
R(448, g="🞡🞢🞣🞤🞥🞦🞧", d="↑", ax="7-step weight ladder (Greek cross)", st="very high", bas="name-derived")
R(449, g="🞨🞩🞪🞫🞬🞭🞮", d="↑", ax="7-step weight ladder (saltire)", st="very high", bas="name-derived")
R(450, g="🞯🞰🞱🞲🞳🞴", d="↑", ax="weight ladder (five-spoked asterisk; repeated for six- and eight-spoked)", st="very high", bas="name-derived")
R(451, g="🟀🟁🟂", d="↑", ax="weight ladder applied to stars, repeated for four-pointed", st="high", bas="name-derived")
R(452, typ="generator", ax="Unicode has a dedicated 'make me a clean N-step magnitude ladder' generator (light→medium→bold→heavy→very heavy→extremely heavy) reused across seven shape families", bas="name-derived", mn="rule-confidence: high (7 instantiations observed in-block); densest concentration of unambiguous ladders in the survey per surveyor")
# Legacy Computing sextants
R(458, g="🬀🬂🬆🬎🬝", d="↑", ax="accumulating fill count (Braille-like)", st="high", bas="perceived-directly", con=True, mn="scattered codepoints (bitmask order, not popcount); ladder tops out at 5/6 — full cell coincides with █")
R(464, g="🮂🮃🮄🮅🮆", d="↑", ax="fraction-fill ladder, 'upper' orientation", st="very high", bas="perceived-directly")
R(465, g="🮇🮈🮉🮊🮋", d="↑", ax="fraction-fill, 'right' orientation — family now confirmed in all four orientations", st="very high", bas="perceived-directly")
R(471, g="🯰🯱🯲🯳🯴🯵🯶🯷🯸🯹", d="↑", ax="seven-segment-display digit ladder", st="very high", bas="semantic-knowledge")
# Tarot
R(477, g="🃡🃢🃣🃤🃥🃦🃧🃨🃩🃪🃫🃬🃭🃮🃯", d="↑", ax="trump numbering, literal embedded number", st="very high", bas="perceived-directly")
# Supplemental Symbols and Pictographs
R(483, g="🤅🤄", d="↑", ax="dot count; THIRD case where semantic 'more' runs opposite codepoint order", st="high", bas="perceived-directly", mn="superseded/completed by the full 0-4 dot ladder at L874", lin="brief-steered")
R(484, typ="negative", ax="mostly face/hand/animal pictographs without shared axis", neg="not-felt")
R(490, typ="negative", ax="combinatorial arrow variants, nothing beyond weight/multiplicity already logged", neg="verified-absent")
# Kangxi Radicals
R(496, g="⼀⿕", typ="meta", d="↑", ax="entire 214-radical block natively ordered by increasing stroke count — a whole block whose ordering principle already IS a magnitude axis", st="high as a structural/semantic fact, though moderate as a pure glance-perceptual test", bas="semantic-knowledge", mn="glyphs are the two endpoints; felt sense of increasing visual density reported when paging through")
# Native-script digits consolidated
R(502, typ="meta", g="٠١٢٣٤٥٦٧٨٩", ax="rule: essentially every native-script decimal digit block forms a ↑ digit ladder — declared a closed, well-confirmed category", st="very high each", bas="semantic-knowledge", mn="glyphs are the Arabic-Indic instance as representative; example chains: Devanagari, Bengali, Thai etc. named in note; per-script felt-strength later differentiated (L693-730) — see those records")
# Small Form Variants
R(508, typ="equivalence", ax="each character a 'small' width-variant of punctuation elsewhere — same-value-different-dress, not a magnitude ladder", bas="name-derived", mn="assumed (pattern-level, not per-pair inspection)")
# Rumi
R(514, typ="sequence", d="↑", ax="full adjacent 1-9/10-90/100-900 ladder, established ancient-numeral pattern", st="very high", bas="name-derived", mn="no glyphs transcribed by surveyor — pattern-level confirmation")
# Modifier Tone Letters
R(520, g="꜈꜉꜊꜋꜌", d="↓", ax="visual height tracks pitch, same logic as ˥˦˧˨˩ — three parallel sets confirmed", st="very high each", bas="perceived-directly")
# Kharoshthi + vein closure
R(526, g="𐩀𐩁𐩂𐩃𐩄𐩅𐩆𐩇", d="↑", ax="additive ancient-numeral pattern", st="very high", bas="name-derived", mn="carries the explicit vein-closure declaration: 'ancient numeral systems' deliberately closed after ~10 confirmed scripts")
# Chinese size ladder extended
R(530, g="微小中大巨", d="↑", ax="tiny/small/medium/large/giant size words", st="medium-high for me — confident in 小中大, less certain 微 and 巨 are the most natural endpoints", bas="semantic-knowledge")
# Hatch density
R(536, g="□▤▦▩■", d="↑", ax="hatch-density/fill progression", st="high", bas="perceived-directly", mn="self-identified miss on first pass through Geometric Shapes")
# Staff lines
R(542, g="𝄖𝄗𝄘𝄙𝄚𝄛", d="↑", ax="literal visible line-count", st="very high", bas="perceived-directly")
# Rests / octave signs
R(548, g="𝄻𝄼𝄽𝄾𝄿𝅀𝅁𝅂", d="↓ duration", ax="rest-duration ladder, mirrors note-duration", st="very high", bas="semantic-knowledge")
R(549, g="𝄶𝄸", typ="sequence", d="↑ by interval-distance", ax="ottava(8) < quindicesima(15)", st="high", bas="semantic-knowledge", mn="surveyor excludes COMMON TIME from the axis; glyphs = ottava alta, quindicesima alta as representatives")
# Byzantine / Ancient Greek music
R(555, typ="negative", ax="highly specialized neume names with no shared magnitude vocabulary found", neg="verified-absent")
R(561, typ="negative", ax="catalog numbering is a modern reference index, not a verified pitch/duration order — won't assert an unjustifiable sequence", neg="declared-out-of-scope")
# Cross-pane composites round 2 (meta synthesis)
R(567, typ="meta", ax="the 'weight axis' recurs as an independent design primitive in at least six unrelated blocks — repetition of the same design idea is itself one finding", bas="perceived-directly", mn="scope: six named blocks; explicitly NOT proposing one glyph-to-glyph glide across them")
R(568, typ="meta", ax="the 'countable discrete pips' axis appears near-identically in at least six unrelated notation systems — identical 'count the marks' feeling regardless of shape grammar", bas="perceived-directly")
R(569, typ="meta", ax="ancient numeral systems as a closed class: ten unrelated scripts each lay numerals in ascending adjacent codepoints — a meta-fact about Unicode allocation convention more than perception; explains why numeral blocks are near-guaranteed hits", bas="semantic-knowledge")
R(570, typ="meta", ax="semantic-only rank ladders (no visual size cue at all) named as a distinct sub-category: medals, neutral chess, Roman coins, alephs — only work if you already know the convention", bas="semantic-knowledge")
# SignWriting / OCR / celebration
R(576, typ="negative", ax="hand-shape names encode articulation, not a countable axis; too specialized to perceive an ordering", neg="declared-out-of-scope")
R(582, typ="negative", ax="MICR symbols, no magnitude axis", neg="verified-absent")
R(586, typ="negative", ax="distinct objects/activities; ascending/descending notes pair is direction, not magnitude", neg="verified-absent")
# Thai tone marks
R(592, g="่้๊๋", d="↑", ax="names derived from ordinal-ish number words; shapes increase in stroke-complexity", st="medium", bas="name-derived", mn="surveyor's confidence in reading Thai glyph complexity at a glance self-flagged lower")
# Ethiopic
R(598, typ="sequence", d="↑", ax="full adjacent 1-9/10-90/hundred/ten-thousand ladder (11th confirmed script)", st="very high", bas="name-derived", mn="no glyphs transcribed by surveyor")
# Greek isopsephy
R(604, g="αβγδε", d="↑", ax="alphabet-as-numerals via keraia, purely notational/learned", st="high for me", bas="semantic-knowledge")
# IPA Extensions / Combining Supplement
R(610, typ="negative", ax="articulation categories, not a magnitude count with 3+ terms", neg="verified-absent")
R(616, typ="negative", ax="only isolated single/double pairs of the already-logged weight-doubling pattern — not counted as new", neg="not-felt")
# Danda
R(620, g="।॥", d="↑", ax="single/double danda (sentence vs verse-end)", st="high", bas="perceived-directly")
# Fitzpatrick
R(626, g="🏻🏼🏽🏾🏿", d="↑", ax="numbered dermatological scale, lightest to darkest; rendered colors form a visible gradient", st="high", bas="name-derived", mn="dual: visible light-to-dark gradient also cited")
# Integral extended
R(632, g="∫∬∭⨌", d="↑", ax="integral-stacking extended cross-block to quadruple", st="very high", bas="perceived-directly")
# Star point-count, medium tier
R(638, g="🟁🟅🟋🟎", d="↑", ax="holding weight constant ('medium') isolates pure point-count", st="very high", bas="name-derived", con=True)
# Nested less-than ladder
R(644, g="<≪⋘⪢⫸", d="↑", ax="5-step emphasis ladder for 'how much less/greater', spanning two blocks", st="very high", bas="name-derived", con=True, conf="ambiguous", mn="DISCREPANCY passed back: the surveyor's typed glyphs ⪢/⫸ are DOUBLE/TRIPLE NESTED GREATER-THAN (U+2AA2/U+2AF8) but the prose asserts LESS-THAN forms and cites U+2AA1/2AF7; glyphs transcribed as typed, so derived codepoints contradict the surveyor's asserted ones. Also: greps the greater-than versions and mirrors; supersedes the L56 skip")
# Self-audit grep pass
R(650, typ="meta", ax="grep-across-old-panes technique is quick but shallow and pulls away from the read-and-feel rhythm — returning to reading fresh panes directly", bas="unstated", mn="method self-observation")
# Greek and Coptic
R(656, typ="meta", ax="GREEK NUMERAL SIGN placement confirms isopsephy is a deliberately-placed Unicode feature, not surveyor trivia; no new independent finding in block", bas="name-derived")
R(662, typ="negative", ax="vehicles/signage/luggage — distinct fixed referents", neg="verified-absent")
# Consecutive equals
R(668, g="⩵⩶", d="↑", ax="plain sign-count", st="very high", bas="perceived-directly", mn="another self-acknowledged miss from the first pass")
R(674, typ="negative", ax="dense less/greater combination variants, no additional axis", neg="verified-absent")
# Clicks
R(680, g="ǀǁ", d="↑", ax="1-stroke vs 2-stroke visual pair; click types otherwise not a magnitude scale", st="medium", bas="perceived-directly", mn="surveyor treats it as a visual stroke-count coincidence, not a felt semantic ladder")
# Bengali currency numerators
R(686, g="৴৵৶৷", d="↑", ax="numerator count; glyphs visually accumulate strokes", st="high", bas="perceived-directly", mn="'genuinely felt this one rather than just pattern-matching the name'")
R(687, g="৴৸৹", d="↑", ax="1..4 < (base−1) < base(sixteen)", st="medium", bas="semantic-knowledge", con=True, mn="'I had to think it through rather than feel it instantly'")
# Per-script digit felt-strength differentiation
R(693, g="०१२३४५६७८९", d="↑", ax="felt ordering even without conscious mapping — rough sense of increasing visual complexity/loop-count", st="very high", bas="perceived-directly")
R(694, typ="negative", ax="rest of fragment: distinct letters, no shared axis", neg="verified-absent")
R(700, g="٠١٢٣٤٥٦٧٨٩", d="↑", ax="known values; honestly weaker as felt visual glide — recognition, not perception", st="high semantically", bas="semantic-knowledge", mn="surveyor explicitly distinguishes this in kind from the stronger visual cases")
R(706, g="๐๑๒๓๔๕๖๗๘๙", d="↑ (known)", ax="all similarly loopy/curved — no felt visual cue distinguishing digits at a glance", st="low-medium as a felt visual glide for me specifically", bas="semantic-knowledge", mn="honest low-confidence data point: digit-ladder strength does NOT carry equally across scripts")
R(712, g="၀၁၂၃၄၅၆၇၈၉", d="↑ (known)", ax="round/circular glyphs, visually similar complexity — can't perceive ordering without knowing values", st="low as a felt visual glide", bas="semantic-knowledge", op="surveyor's working hypothesis here: round-script numerals feel weak vs angular/stroke-based systems")
R(718, g="០១២៣៤៥៦៧៨៩", d="↑ (known)", ax="round, loop-based glyphs, no perceptible complexity gradient", st="low (same honest assessment as Thai and Myanmar)", bas="semantic-knowledge")
R(724, g="᱐᱑᱒᱓᱔᱕᱖᱗᱘᱙", d="↑ (known)", ax="rounded/geometric, no strong complexity gradient — hypothesis test case", st="not strong (no clean split along 'angular=strong')", bas="semantic-knowledge", op="hypothesis revised: it's whether the script builds small numbers from literally-repeated strokes, not round-vs-angular")
R(730, g="༠༡༢༣༤༥༦༧༨༩", d="↑", ax="noticeably stronger felt gradient — zero reads as 'the least', later digits more structurally busy", st="medium — a genuine middle case", bas="perceived-directly")
# Card suits
R(736, g="♣♦♥♠", d="↑", ax="bridge/contract bidding convention — pure convention knowledge, shapes suggest nothing", st="medium-high for me specifically", bas="semantic-knowledge", mn="surveyor distinguishes: niche game-specific convention vs broadly-known semantic ladders")
# Combining marks slow re-read
R(742, g="̇̈", typ="sequence", d="↑", ax="one dot vs two dots (dot above vs diaeresis)", st="high", bas="perceived-directly", mn="glyph transcription hazard: combining chars; codepoints intended U+0307,U+0308 — see note_verbatim", conf="interpreted")
R(748, g="̲̳", d="↑", ax="single vs double underline — extremely familiar text-formatting convention", st="very high", bas="perceived-directly")
R(749, g="̵̶", d="↑", ax="short vs long stroke overlay — length named and visible", st="high", bas="perceived-directly")
# CJK Compat second jackpot
R(755, g="㍘㍙㍚㍛㍜㍝㍞㍟㍠㍡㍢㍣㍤㍥㍦㍧㍨㍩㍪㍫㍬㍭㍮㍯㍰", d="↑", ax="25-step adjacent clock-hour ladder", st="very high", bas="name-derived", mn="missed on first pass; caught on deliberate slow re-read")
R(756, g="㎀㎁㎂㎃㎄", d="↑", ax="SI-prefix ladder for amperes", st="very high", bas="name-derived")
R(757, g="㎅㎆㎇", d="↑", ax="byte-scale ladder", st="very high", bas="semantic-knowledge")
R(758, g="㎈㎉", d="↑", ax="calorie/kilocalorie", st="very high", bas="semantic-knowledge")
R(759, g="㍸㍹", d="↑", ax="dm² vs dm³ extends area/volume families", st="high", bas="semantic-knowledge")
R(760, typ="meta", ax="lesson: first pass through a dense name-heavy block was too quick; slowing to line-by-line reading surfaces real sequences otherwise missed entirely", bas="unstated")
# Third jackpot
R(766, 768, g="㎑㎒㎓㎔", d="↑", ax="frequency ladder extended to THz", st="very high", bas="semantic-knowledge")
R(769, g="㎕㎖㎗㎘", d="↑", ax="volume-scale ladder", st="very high", bas="semantic-knowledge")
R(770, g="㎙㎚㎛㎜㎝㎞", d="↑", ax="length ladder femtometer→kilometer", st="very high", bas="semantic-knowledge")
R(771, g="㎩㎪㎫㎬", d="↑", ax="pressure ladder to GPa", st="very high", bas="semantic-knowledge")
R(772, g="㎰㎱㎲㎳", d="↑", ax="time-scale ps→ms", st="very high", bas="semantic-knowledge")
R(773, g="㎴㎵㎶㎷㎸", d="↑", ax="voltage ladder pV→kV", st="very high", bas="semantic-knowledge")
R(774, g="㎺㎻㎼㎽㎾", d="↑", ax="power ladder pW→kW", st="very high", bas="semantic-knowledge")
R(775, g="㏀㏁", d="↑", ax="kilohm→megohm", st="very high", bas="semantic-knowledge")
R(777, typ="meta", ax="the CJK Compatibility block is Unicode's 'SI-prefix-times-unit' generator; rewards slow complete reading more than any other block", bas="name-derived")
R(783, g="㏠㏡㏢㏣㏤㏥㏦㏧㏨㏩", d="↑", ax="31-step calendar-day ladder (glyphs: first ten as representatives)", st="very high", bas="name-derived", mn="full run ㏠..㏾ per note; block declared fully read")
# Math Operators slow re-read
R(789, g="∈∊", d="↑", ax="'regular > small' named-size in relation symbols; rendered difference subtle/font-dependent", st="medium", bas="name-derived")
R(790, g="∋∍", d="↑", ax="same pattern, mirror relation", st="medium", bas="name-derived")
R(796, g="∶∷", d="↑", ax="dot-count doubling (ratio vs proportion)", st="high", bas="perceived-directly")
R(797, g="∼≈≋", d="↑", ax="wavy-line-count ladder", st="high", bas="perceived-directly")
R(803, g="=≡≣", d="↑", ax="bar-count for 'how strongly equal' — semantic and visual confirmation together", st="very high", bas="perceived-directly")
R(809, typ="negative", ax="re-examined subset/superset/tack stretch — ⊂ vs ⊆ is logical strictness, not a 'which is more' feeling; earlier skip confirmed", neg="verified-absent")
R(815, g="⊢⊨⊪", d="↑", ax="turnstile bar-count that also tracks logical strength — shape and meaning agree", st="very high", bas="perceived-directly")
R(821, g="⊂⋐", d="↑", ax="single/double weight (also ⊃⋑)", st="high", bas="perceived-directly")
# Misc Technical re-read
R(827, g="⌒⌓⌔", typ="question", d="tentative ↑", ax="how much of a circle is being claimed", st="medium, genuinely uncertain", bas="semantic-knowledge", spec=True, op="would a fresh pairwise test put SEGMENT before or after SECTOR? ordering inferred from geometric convention, not perceived")
R(833, typ="negative", ax="GD&T symbols are distinct measurement types, not a shared scale", neg="verified-absent")
R(839, typ="negative", ax="arrows re-read confirms first pass adequate — nothing beyond single/double/triple weight", neg="verified-absent", mn="explicit confirmation that not every block was under-mined")
# Vedic Extensions
R(845, g="᳚᳛", d="↑", ax="double vs triple svarita — plain count in the name", st="high", bas="name-derived")
R(846, g="᳝᳞᳟", d="↑", ax="dot count below, genuinely visible side by side", st="very high", bas="perceived-directly")
R(852, g="᳸᳹", d="↑", ax="single/double ring above — third single/double instance in this one block", st="high", bas="name-derived")
# Combining Extended
R(858, g="᪹᪺", d="↑", ax="explicitly named light/strong centralization stroke", st="high", bas="name-derived")
R(859, g="᪷᪸", d="↑", ax="single/double open mark", st="high", bas="name-derived")
R(860, g="᪻᪼", d="↑", ax="single/double parentheses above", st="high", bas="name-derived")
R(861, g="᫈᫉", d="↑", ax="single/double plus sign above", st="high", bas="name-derived")
R(862, g="́̋᫋", d="↑", ax="acute → double acute → triple acute, three-step ladder scattered across two blocks", st="high", bas="name-derived", con=True)
# Phonetic Extensions
R(868, typ="negative", ax="small-capital/turned letter forms, alphabetical, no magnitude axis; TOP/BOTTOM HALF O is position not size", neg="verified-absent")
# Supplemental dot ladders corrected
R(874, g="🤇🤆🤅🤄🤃", d="↑", ax="complete 5-step dot-count ladder 0→4", st="very high", bas="perceived-directly", mn="corrects/completes L483 which caught only the middle pair; caught by reading the whole stretch by name rather than grepping 'dots'")
R(875, g="🤂🤁🤀", d="↑", ax="even-count-only dot ladder (0,2,4)", st="high", bas="perceived-directly")
R(881, typ="negative", ax="face/gesture/sport pictographs — genuinely checked, no shared axis", neg="verified-absent")
R(887, typ="negative", ax="only the medal ladder; rest distinct food/equipment", neg="verified-absent")
R(893, typ="negative", ax="distinct face/clothing/animal", neg="verified-absent")
# Age progression
R(899, g="🧒🧑🧓", d="↑ by age", ax="age; fourth 'semantic order overwhelms codepoint order' instance", st="high", bas="semantic-knowledge", lin="brief-steered")
R(900, g="🧍🧎", d="tentative ↑ by height/posture", ax="'standing is more' — a stretch/subjective framing", st="low, genuinely uncertain", bas="perceived-directly", spec=True)
R(906, g="🙋🙌", d="↑", ax="literal hand-count (one vs two)", st="high", bas="perceived-directly")
# Trigrams
R(912, g="☷☰", d="↑", ax="yang-line-count endpoints (0 vs 3 solid lines); middle trigrams share counts and can't be ordered", st="medium", bas="perceived-directly")
# Planets
R(918, g="☿♀♁♂♃♄♅♆♇", d="↑", ax="classical solar-system ordering by distance from the sun", st="high", bas="semantic-knowledge", mn="missed on first pass; names alone obscure the planetary sequence")
# Hands
R(924, g="✊✌✋", d="↑", ax="finger-count feel across clustered hand gestures", st="high", bas="perceived-directly")
# Basic Latin systematic pass
R(930, g="0123456789", d="↑", ax="the foundational digit ladder every decorated-digit family derives its feel from", st="very high", bas="semantic-knowledge")
R(931, typ="negative", ax="A-Z, a-z genuinely reconsidered: no magnitude feeling, alphabetical position isn't more/less", neg="verified-absent")
R(932, typ="negative", ax="! vs ?: distinct punctuation functions, no magnitude", neg="verified-absent")
R(933, typ="negative", ax="rest of printable range: distinct punctuation or letters", neg="verified-absent")
# Latin Extended-A
R(939, typ="negative", ax="letter+one-diacritic forms arranged alphabetically; single-vs-double acute continues only by reaching to another block", neg="verified-absent", mn="corrected two entries later (L945, ŀ) — surveyor left the correction as its own record rather than editing")
R(945, g="lŀ", d="↑", ax="Catalan punt volat: single-L vs geminated l·l — genuine single/double consonant pair", st="high", bas="semantic-knowledge", mn="explicit correction of the L939 'nothing found'; found by asking what the mark means")
R(946, typ="meta", ax="'Prompted to look again more slowly rather than trusting my first alphabetical-no-axis read of accent-letter blocks going forward'", bas="unstated", lin="steered", conf="clear", mn="Adjudicated STEERED (Joseph, 2026-08-25): 'I noticed that it was discounting anything alphabet-like instead of looking for meaningful progressions or something like that. I didn't prompt with the actual pattern at all (which isn't the case with several other steers in the longer ones, where I know they copied down my steering examples verbatim as a sequence).' — a FRAME-steer (attention redirected, no example content supplied), unlike the example-steers elsewhere; frame-vs-example stays fuzzy by design under the interactive-anecdote ceiling. v0.8->0.9 delta: lineage unknown->steered, confidence ambiguous->clear, per adjudication")
# Latin Extended-B
R(952, g="ƧƽƄ", typ="sequence", d="↑", ax="numbered tone letters (TONE TWO/FIVE/SIX) scattered out of numeric order — semantic value overwhelms position", st="high", bas="name-derived", con=True, mn="glyphs: capital tone-two, small tone-five, capital tone-six as representatives; codepoint order in block is 6,2,5")
R(953, typ="negative", ax="hooks/topbars/strokes are distinct phonetic markers, not gradations — genuinely considered each this time", neg="verified-absent")
# Latin Extended Additional stacking
R(959, 961, g="ŪǕ", d="↑", ax="one mark (macron) → two stacked marks (diaeresis+macron)", st="high", bas="perceived-directly")
R(962, g="ḂḈ", d="↑", ax="'how many marks piled on top' across different base letters", st="medium", bas="perceived-directly", mn="cross-base-letter comparison — less a clean pairwise test, more a felt structural pattern")
R(963, typ="generator", ax="rule: plain letter < letter+one diacritic < letter+two stacked diacritics — a three-step visual-density axis recurring across Latin Extended-A/-B/Additional collectively", bas="perceived-directly", mn="named by surveyor as a meta-pattern rather than a single sequence; instances scattered across three blocks")
# Ligatures
R(969, g="ﬀﬁﬂﬃﬄ", d="↑", ax="component-letter-count (2 vs 3), countable in name and glyph", st="very high", bas="perceived-directly")
# Double grave
R(975, g="àȀ", d="↑", ax="one grave stroke vs two — verified single/double naming, genuinely felt", st="high", bas="perceived-directly")
# Quotes and brackets
R(981, g="'\"", d="↑", ax="single vs double quote mark, extremely familiar convention", st="high", bas="perceived-directly")
R(982, g="()[]{}", d="tentative ↑ by conventional nesting depth", ax="nesting convention parens<brackets<braces; genuinely uncertain how universal", st="medium", bas="semantic-knowledge", spec=True, lin="brief-steered")
# Trademark ladder
R(988, g="™℠®", d="↑", ax="legal-strength hierarchy (self-asserted vs registered) — purely conventional, no visual cue", st="medium-high", bas="semantic-knowledge", mn="cross-block scatter noted (® Latin-1, ™/℠ Letterlike)")
# Guillemets
R(994, g="‹›«»", d="↑", ax="single vs double angle quotation marks, scattered across two blocks", st="high", bas="perceived-directly")
# Eszett
R(1000, g="sß", d="↑", ax="ß as historical ss ligature — single-vs-double consonant, parallel to Catalan ŀ", st="high", bas="semantic-knowledge")
# IPA length and stress
R(1006, g="ˑː", d="↑", ax="half-long vs full-long vowel mark — standard IPA length convention", st="very high", bas="semantic-knowledge", mn="self-acknowledged miss on original Spacing Modifier pass")
R(1012, g="ˌˈ", d="↑", ax="secondary vs primary stress — conventional/positional, not visually self-evident", st="high", bas="semantic-knowledge")
# Pilcrow/section
R(1018, g="¶§", d="↑", ax="document-hierarchy containment (section contains paragraphs) — 'honestly a bit of a stretch'", st="medium", bas="semantic-knowledge", spec=True, lin="brief-steered")
# L with bar
R(1024, g="ƚⱠ", d="↑", ax="one bar vs double bar, scattered two blocks apart", st="high", bas="name-derived")
R(1025, typ="negative", ax="rest of Latin Extended-C: distinct African/Caucasian-orthography letter forms, no further shared axis found after genuinely considering them", neg="verified-absent")
# Digraph case triplets
R(1031, g="Ǆǅǆ", d="↓", ax="ALL-CAPS > Title-case > lowercase — visual size/stroke-mass gradient, purely by eye", st="high", bas="perceived-directly", mn="recurs identically for LJ and NJ families")
# Roman numerals visual break
R(1037, g="ⅠⅡⅢ", d="↑", ax="pure shape: 1,2,3 vertical strokes accumulating", st="very high", bas="perceived-directly")
R(1038, g="ⅢⅣ", typ="negative", ax="visual-complexity feeling and numeric magnitude diverge at Ⅳ — subtractive notation makes four visually SIMPLER than three", neg="verified-absent", mn="surveyor-volunteered honest negative case; first-class tempting-but-false datum")
# Case-height ladder
R(1044, g="aᴀA", d="↑", ax="three-step visual height ladder (x-height < small-cap < cap-height)", st="high", bas="perceived-directly", con=True)
# NEW MODE: free-associative morph chains — explicit Joseph steering ("Per your example", L1050)
R(1048, 1050, typ="meta", ax="mode shift: free-associative shape-morph chains, not semantic/name-driven — 'personal/idiosyncratic felt continuations, not conventional magnitude claims'", bas="unstated", lin="steered", mn="LINEAGE BOUNDARY: Joseph supplied a morph example ('- = > } ) |'); all records L1052-L1074 are steered and flagged by the surveyor as a distinct, looser kind of entry")
R(1052, g="|S@", d="↑ by 'amount of coiling/curl'", ax="straight line → wave → spiral", st="purely a felt visual narrative, not a magnitude claim in the usual sense", bas="constructed", lin="steered", con=True, spec=True)
R(1053, g="ˆ~‾_", d="↓ in 'sharpness/height' (direction flip-flopped: could read as 'settling')", ax="a peak melting down / energy dissipating", st="felt strongly once pictured as an animation", bas="constructed", lin="steered", con=True, spec=True, op="surveyor flip-flopped on direction")
R(1054, g="|⋮", d="↑", ax="increasing fragmentation of the same vertical space (continuous → discrete) — an axis not named before", bas="constructed", lin="steered", con=True, spec=True)
R(1055, g="∙⊂○", d="↑ by 'how closed/complete the loop is'", ax="point opens into curve, curls closed into circle", st="genuinely felt as continuous bending-until-closure", bas="constructed", lin="steered", con=True, spec=True)
R(1056, g="-=≈∾∿", d="↑ by 'how much energy/motion has entered a once-static line'", ax="flat line duplicates, ripples, becomes full sine wave", bas="constructed", lin="steered", con=True, spec=True)
R(1057, g="⊢⊥□", d="↑ by 'how enclosed the shape has become'", ax="containment-morph rather than fill-morph", bas="constructed", lin="steered", con=True, spec=True)
R(1063, g="∘○◯", d="↑", ax="same ring shape inflating across three unrelated Unicode categories — pure size-scaling morph", bas="constructed", lin="steered", con=True)
R(1064, g="·oO○◯", d="↑", ax="tiny dot growing into big circle across functional classes — most 'diffuse'/boundary-blurring chain built; only the felt 'roundness inflating' motif is shared", bas="constructed", lin="steered", con=True, spec=True)
R(1065, g="‸∧Λ▲", d="↑", ax="thin pointed mark thickening/filling into solid triangle — 'outline hardening into solid' motif", bas="constructed", lin="steered", con=True, spec=True)
R(1066, g="`/⟋", d="↑", ax="tiny tick stretching into full formal diagonal — pure length-growth of one motif", bas="constructed", lin="steered", con=True, spec=True)
R(1072, g="˙:⁝⣿", d="↑", ax="single point multiplying into a dense field — count of discrete elements climbing, not size of one shape", bas="constructed", lin="steered", con=True, spec=True)
R(1073, g="˅∨⋁▽", d="↑", ax="narrow angle widening then solidifying — sibling of caret→triangle chain", bas="constructed", lin="steered", con=True, spec=True)
R(1074, g="⌒◠○", d="↑", ax="degrees of circle swept (0-ish, 180, 360) — explicitly parameterized point-to-circle chain", bas="constructed", lin="steered", con=True)
# Cyrillic
R(1080, g="҂҈҉", d="↑", ax="thousand < hundred-thousand < million, built into Church-Slavonic numerals", st="very high", bas="name-derived")
R(1081, typ="meta", ax="Cyrillic letters+titlo parallel Greek isopsephy and Hebrew gematria — parallel noted rather than re-derived", bas="semantic-knowledge")
R(1087, typ="negative", ax="Cyrillic remainder genuinely read in full: distinct letters, shapes checked too, no accumulating axis", neg="verified-absent")
R(1093, typ="negative", ax="Cyrillic Supplement: distinct sounds, no shared axis", neg="verified-absent")
# Armenian
R(1099, typ="meta", ax="Armenian alphabet doubles as numeral system — same alphabet-as-numerals principle, parallel noted", bas="semantic-knowledge")
R(1100, typ="negative", ax="letters and punctuation each distinct, shapes checked, no axis", neg="verified-absent")
# Hebrew cantillation
R(1106, g="֔֕", d="↑", ax="zaqef qatan (small) vs gadol (great) — named small/great pair, found by reading the Hebrew words", st="high", bas="name-derived")
R(1112, g="֩֠", d="↑", ax="telisha qetana/gedola — second named small/great pair, scattered", st="high", bas="name-derived")
R(1113, g="֥֦", d="↑", ax="merkha vs merkha kefula (doubled)", st="high", bas="name-derived")
R(1119, g="ָׇ", d="↑ (or ↓, depending on which 'more' you mean)", ax="qamats vs qamats qatan — grammatical vowel length, not physically smaller-drawn", st="medium", bas="semantic-knowledge", op="direction ambiguity flagged by surveyor")
R(1120, g="וװ", d="↑", ax="literally a doubled letter (Yiddish double vav)", st="high", bas="perceived-directly")
R(1121, g="יײ", d="↑", ax="doubled yod", st="high", bas="perceived-directly")
R(1127, typ="negative", ax="Hebrew alphabet: gematria already logged; final forms are positional variants, not magnitude", neg="verified-absent")
# Georgian / Cherokee
R(1133, typ="meta", ax="Georgian alphabet-as-numerals — sixth script confirming the pattern", bas="semantic-knowledge")
R(1134, typ="negative", ax="phonetic names, uniform letterform complexity, no axis — shapes checked", neg="verified-absent")
R(1140, typ="negative", ax="Cherokee syllabary: consonant-vowel arrangement, uniform style, no axis", neg="verified-absent")
# Canadian Aboriginal Syllabics — MAJOR FIND
R(1146, 1148, g="ᐃᐄ", d="↑", ax="physical glyph SIZE directly encodes vowel LENGTH — documented design of the writing system; 'possibly the most literal bigger-glyph=more system in all of Unicode', continuous size not discrete count", st="very high", bas="perceived-directly", mn="block intro L1146 carries the framing: 'one of the most striking finds in the whole survey'")
R(1149, g="ᐅᐆ", d="↑", ax="same size-for-length system (O/OO)", bas="perceived-directly")
R(1150, g="ᐎᐐᐒᐔᐗᐙ", d="↑ within each pair", ax="short/long size pairs repeated across every vowel of the rotation system", bas="perceived-directly")
R(1151, typ="meta", ax="flagged directly: a documented linguistic fact rediscovered by reading syllable names rather than assuming 'just another syllabary, skip'", bas="semantic-knowledge")
R(1155, g="ᐟᐥ", d="↑", ax="final acute vs double acute — single/double confirmed in another unrelated script", st="high", bas="name-derived")
R(1156, g="ᐦ", typ="question", ax="FINAL DOUBLE SHORT VERTICAL STROKES implies a single-stroke counterpart exists", bas="name-derived", op="what would settle it: confirming the adjacent single-stroke final codepoint — surveyor declined to assert it unconfirmed")
R(1162, typ="generator", g="ᐸᐹᑕᑖ", ax="rule: short/long size-pair repeats systematically for every consonant in the syllabary — structural design principle of the entire writing system, not scattered coincidence", bas="perceived-directly", mn="rule-confidence high (confirmed across consonants); example chains PA/PAA, TA/TAA")
# Ogham — MAJOR FIND
R(1168, 1170, g="ᚁᚂᚃᚄᚅ", d="↑", ax="1-5 strokes right of stem — tally-mark logic applied to a real alphabet", st="very high", bas="perceived-directly", mn="block intro L1166-1168: Ogham is a stroke-tally script, letters grouped in fives")
R(1171, g="ᚆᚇᚈᚉᚊ", d="↑", ax="1-5 strokes left of stem", st="very high", bas="perceived-directly")
R(1172, g="ᚋᚌᚍᚎᚏ", d="↑", ax="1-5 diagonal strokes crossing stem", st="very high", bas="perceived-directly")
R(1173, g="ᚐᚑᚒᚓᚔ", d="↑", ax="1-5 vowel notches through stem", st="very high", bas="perceived-directly")
R(1174, typ="meta", ax="a real ancient alphabet whose entire design principle IS the visual magnitude axis — every set of five letters is by construction a perfect stroke-count ladder", bas="perceived-directly")
# Runic
R(1180, g="ᚭᚬ", d="↑", ax="named short-twig vs long-branch", st="high", bas="name-derived")
R(1181, g="ᚽᚼ", d="↑", ax="same pattern, second instance", bas="name-derived")
R(1182, g="ᚿᚾ", d="↑", ax="short-twig-naud vs plain naud serving as 'long' — slightly less clean, 'long' side not explicitly labeled", bas="name-derived", mn="surveyor flags reduced cleanness")
R(1183, g="ᛆᛅ", d="↑", ax="fourth instance — clearly a systematic naming convention through the whole block", bas="name-derived")
R(1189, g="ᛙᛘ", d="↑", ax="fifth instance", bas="name-derived")
R(1190, g="ᛧᛦ", d="↑", ax="sixth instance", bas="name-derived")
R(1191, g="᛫᛬", d="↑", ax="single vs multiple punctuation (one dot vs several)", st="high", bas="name-derived")
# Philippine scripts
R(1197, g="᜵᜶", d="↑", ax="single vs double punctuation", st="high", bas="name-derived")
R(1198, typ="negative", ax="phonetic letters across all four related scripts, no axis among letters", neg="verified-absent")
# Khmer lunar
R(1204, g="᧡᧢᧣᧤᧥᧦᧧᧨᧩᧪᧫᧬᧭᧮᧯", d="↑", ax="complete 1-15 lunar day-count (waxing), repeated for waning — found by reading Khmer number-words", st="very high", bas="name-derived")
# Mongolian
R(1210, g="᠐᠑᠒᠓᠔᠕᠖᠗᠘᠙", d="↑", ax="digit ladder", st="very high", bas="semantic-knowledge")
R(1211, typ="negative", ax="numbered variation selectors are invisible formatting codes — considered and rejected", neg="verified-absent")
R(1212, typ="negative", ax="nothing else in punctuation stretch", neg="not-felt")
R(1218, typ="negative", ax="Mongolian letters phonetic; TODO LONG VOWEL SIGN has no short counterpart in stretch", neg="verified-absent")
# Limbu / Tai Le / New Tai Lue
R(1224, typ="sequence", d="↑", ax="Limbu and New Tai Lue digit ladders (plus Tham set) — established pattern, two more scripts", st="unstated (established pattern)", bas="semantic-knowledge", mn="no glyphs transcribed by surveyor")
R(1225, g="ᥰᥱᥲᥳᥴ", d="↑", ax="numbered tone letters 2-6 (no TONE-1 in range)", st="high", bas="name-derived")
R(1226, g="ᧈᧉ", d="↑", ax="tone mark 1 vs 2", st="high", bas="name-derived")
R(1227, typ="negative", ax="Limbu 'small letters' are subscript grammatical forms with no large counterpart — considered and set aside", neg="verified-absent")
# Tai Tham
R(1233, g="᩵᩶᩷᩸᩹", d="↑", ax="numbered tone ladder 1-5", st="high", bas="name-derived")
R(1234, typ="sequence", d="↑", ax="two separate complete digit sets (hora and tham) in one script", bas="name-derived", mn="no glyphs transcribed")
R(1235, typ="negative", ax="HIGH KA / LOW KA is consonant-class terminology, not magnitude — rejected despite tempting wording", neg="verified-absent")
# Balinese
R(1241, g="ᬅᬆ", d="↑", ax="named short/long vowel pair (tedung = long)", st="high", bas="name-derived")
R(1242, g="ᬇᬈᬉᬊᬋᬌᬍᬎᬑᬒ", d="↑ per pair", ax="tedung pattern repeated for every vowel letter — systematic, not coincidental", bas="name-derived")
R(1246, typ="sequence", d="↑", ax="Balinese, Sundanese, Lepcha digit ladders confirmed", bas="semantic-knowledge", mn="no glyphs transcribed; pattern-level")
R(1252, typ="negative", ax="Batak: regional dialect variants, no axis", neg="verified-absent")
R(1256, typ="negative", ax="Sundanese/Lepcha remainder: phonetic letters/vowel signs/punctuation only", neg="verified-absent")
# Greek Extended
R(1262, g="ἀἄ", d="↑", ax="diacritic-stacking count (breathing vs breathing+accent) confirmed in Greek polytonic", st="high", bas="perceived-directly")
R(1268, g="ᾰᾱ", d="↑", ax="vrachy (short) vs macron (long) — named vowel-length pair", st="high", bas="name-derived")
R(1274, typ="negative", ax="remainder: the two confirmed patterns repeat combinatorially for every vowel; enough repetition checked to confirm systematic; nothing structurally new", neg="verified-absent", mn="pattern-complete sampling, not exhaustive re-verification — surveyor states this openly")
# Arabic — MAJOR FINDS
R(1280, g="؆؇", d="↑", ax="cube vs fourth root — Arabic mirror of √∛∜", st="high", bas="name-derived")
R(1281, g="؉؊", d="↑", ax="per-mille vs per-ten-thousand", st="high", bas="name-derived")
R(1282, g="ؾؿ", d="↑", ax="two vs three dots above — direct visible dot-count", st="high", bas="perceived-directly")
R(1283, g="ػؼ", d="↑", ax="dot count 2→3 but position changes above→below — slightly less clean", st="medium", bas="perceived-directly")
R(1284, g="ًٌٍَُِ", d="↑", ax="tanween marks LITERALLY drawn as two copies of the plain vowel mark — visually doubled AND grammatically meaning double/indefinite at once", st="very high", bas="perceived-directly", mn="dual visual+semantic; found by reading what 'tanween' means")
R(1290, g="ڏڐ", d="↑", ax="dal dot-count 3→4", st="high", bas="perceived-directly")
R(1291, g="ڗڙ", d="↑", ax="reh dot-count 2→4 (skipping 3)", st="medium-high", bas="perceived-directly")
R(1292, typ="meta", ax="Arabic's extended-letter system relies heavily on dot-count variation — 'count the marks' feeling for a living alphabet's consonant inventory", bas="perceived-directly")
R(1298, typ="sequence", d="↑", ax="Extended Arabic-Indic digits 0-9 — established pattern confirmed again", bas="semantic-knowledge", mn="no glyphs transcribed")
R(1299, typ="negative", ax="Quranic recitation marks and Sindhi/Urdu extensions — genuinely checked, no further axis", neg="verified-absent")
# Syriac
R(1306, g="݃݅", d="↑", ax="two vs three dots above", st="high", bas="perceived-directly")
R(1307, g="݄݆", d="↑", ax="same, mirrored below", bas="perceived-directly")
R(1308, g="܁܃", d="↑", ax="1 dot vs 2 dots tracking pause-length in Syriac punctuation", st="medium-high", bas="semantic-knowledge")
# N'Ko
R(1314, g="߫߮", typ="sequence", d="↑", ax="named SHORT vs LONG tone marks (3 short, 4 long, all adjacent)", st="high", bas="name-derived", mn="glyphs: short high tone + long descending tone as representatives of the two sets")
R(1315, g="ߴߵ", d="↑", ax="high vs low tone apostrophe", st="high", bas="name-derived")
R(1316, g="߳", typ="question", ax="COMBINING DOUBLE DOT ABOVE implies a plain single-dot counterpart", bas="name-derived", op="single counterpart not spotted in range — pattern flagged, pair not asserted")
R(1317, typ="sequence", d="↑", ax="N'Ko digits 0-9 confirmed", bas="semantic-knowledge", mn="no glyphs transcribed")
# Samaritan — MAJOR FIND
R(1323, 1325, g="ࠡࠢࠣࠥ", d="↓ (or ↑ depending on framing)", ax="FOUR named degrees of vowel length: overlong > long > plain > short — the most granular length system in the survey", st="very high", bas="name-derived", mn="block intro L1321-1323 carries the framing; every other script found gives only 2 steps")
R(1326, g="ࠞࠟࠠ", d="↓", ax="3-step version for AA", st="very high", bas="name-derived")
R(1327, g="ࠜࠝ", d="↓", ax="long E vs E", bas="name-derived")
R(1328, g="ࠦࠧ", d="↓", ax="long U vs U", bas="name-derived")
R(1329, g="ࠩࠪ", d="↓", ax="long I vs I", bas="name-derived")
R(1330, typ="meta", ax="'genuinely delighted' — directly rewards reading each vowel sign's full name rather than assuming another short/long pair", bas="unstated")
R(1336, typ="negative", ax="Samaritan punctuation: no linguistic knowledge to read size/count etymology in the names — not asserting rather than guessing", neg="declared-out-of-scope")
R(1342, typ="negative", ax="Mandaic GEMINATION MARK relates conceptually to doubling but has no plain counterpart to pair — concept noted, no sequence logged", neg="verified-absent")
# Thaana
R(1348, g="ަާ", d="↑", ax="short/long vowel pair (doubled name signals long)", st="high", bas="name-derived")
R(1349, g="ިީ", d="↑", ax="same pattern", bas="name-derived")
R(1350, g="ުޫ", d="↑", ax="same pattern", bas="name-derived")
R(1351, g="ެޭ", d="↑", ax="same pattern", bas="name-derived")
R(1352, g="ޮޯ", d="↑", ax="fifth pair — entire vowel-diacritic system structured around short/long, joining IPA/Greek/Balinese/N'Ko/Samaritan", bas="name-derived")
# FINAL SESSION closing brainstorm
R(1358, g="A𝐀", d="↑", ax="regular → bold typographic weight applied to letters themselves — 'one of the most universally-felt weight distinctions'", st="high", bas="perceived-directly")
R(1359, g="小中大特大", d="↑", ax="size-word ladder extended with tèdà (extra-large)", st="medium-high", bas="semantic-knowledge")
R(1360, g=".,!‼😱", d="↑", ax="quiet-to-loud narrative crossing categories — punctuation escalating into a face; 'purely a felt narrative, not a conventional magnitude claim'", bas="constructed", con=True, spec=True, lin="steered", mn="continues the morph-chain mode Joseph seeded at L1048")
R(1361, g="'🕯🔥🎆", d="↑", ax="fire/intensity narrative — spark → candle → fire → fireworks", bas="constructed", con=True, spec=True, lin="steered")
R(1362, g="|🏠🏢🏙", d="↑", ax="construction/scale narrative — count/height of built structures accumulating", bas="constructed", con=True, spec=True, lin="steered")
# Closing reflection
R(1364, 1366, typ="meta", ax="survey retrospective: strongest finds where a script's entire design principle is a magnitude system; weakest were convention-only; recurring single-vs-double family; the four semantic-vs-codepoint-order reversals called the most direct confirmations of the original hypothesis", bas="unstated", mn="surveyor's own calibration summary over the whole corpus — likely valuable for pass-2 weighting")

emit()
