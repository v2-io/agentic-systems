"""Shared helpers for the embedding-tendrils spike. Reads only this spike's derived/ files."""
import bisect, collections, json, pathlib, re

SPIKE = pathlib.Path(__file__).resolve().parents[1]
DER = SPIKE / "derived"
BANNED = {"⟂", "⊥", "≈"}

_ucd = None
def ucd():
    global _ucd
    if _ucd is None:
        _ucd = json.load(open(DER / "ucd16.json"))
    return _ucd

def name(g):
    r = ucd().get(g)
    return r[0] if r else None

def ok(g):
    """A single assigned code point of category L/N/P/S (Unicode 16), not a study-banned glyph."""
    if not isinstance(g, str) or len(g) != 1 or g in BANNED:
        return False
    r = ucd().get(g)
    return bool(r) and r[1][0] in "LNPS" and not (0xFE00 <= ord(g) <= 0xFE0F)

_blocks = None
def blocks():
    global _blocks
    if _blocks is None:
        rows = []
        for l in open(DER / "Blocks-16.txt"):
            m = re.match(r"([0-9A-F]+)\.\.([0-9A-F]+); (.+)", l)
            if m:
                rows.append((int(m.group(1), 16), int(m.group(2), 16), m.group(3).strip()))
        _blocks = rows
    return _blocks

def block(g):
    cp = ord(g); bl = blocks()
    i = bisect.bisect_right([b[0] for b in bl], cp) - 1
    return bl[i][2] if i >= 0 and bl[i][0] <= cp <= bl[i][1] else "?"

BIG = ('CJK UNIFIED', 'CJK COMPATIBILITY IDEOGRAPH', 'HANGUL SYLLABLE', 'TANGUT', 'YI SYLLABLE', 'KHITAN', 'NUSHU',
       'EGYPTIAN HIEROGLYPH', 'CUNEIFORM', 'ANATOLIAN HIEROGLYPH', 'BAMUM LETTER PHASE', 'LINEAR B IDEOGRAM',
       'SIGNWRITING', 'GARAY', 'TANGUT COMPONENT', 'KHITAN SMALL SCRIPT')

def universe(extra=()):
    """All ok() glyphs except the large ideographic/syllabic repertoires, plus any glyph in `extra`."""
    u = [g for g, r in ucd().items() if ok(g) and not r[0].startswith(BIG)]
    s = set(u)
    u += [g for g in extra if ok(g) and g not in s]
    return sorted(set(u), key=ord)

def answers(upto="r011"):
    return [json.loads(l) for l in open(DER / f"answers-{upto}.jsonl")]

FAMS = ("claude", "gemini", "grok")   # muse was paused early; kept in counts of minds, not of families
