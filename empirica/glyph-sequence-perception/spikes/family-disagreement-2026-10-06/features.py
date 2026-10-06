"""Features of a run of glyphs, from the glyphs alone (never from any mind's answers): chart shape, Unicode block
group, general category, blocks spanned, token familiarity (tok.py)."""
import bisect, pathlib, unicodedata as U
import tok

ROOT = pathlib.Path(__file__).resolve().parents[2]
_B = []
for line in open(ROOT / "data" / "unicode" / "Blocks-16.0.0.txt"):
    line = line.split("#")[0].strip()
    if not line: continue
    rng, name = line.split(";"); a, b = rng.split("..")
    _B.append((int(a, 16), int(b, 16), name.strip()))
_S = [x[0] for x in _B]

def block(g):
    i = bisect.bisect_right(_S, ord(g)) - 1
    return _B[i][2] if i >= 0 and _B[i][0] <= ord(g) <= _B[i][1] else "No_Block"

GROUPS = [
    ("latin", ("Basic Latin", "Latin-1 Supplement", "Latin Extended", "IPA Extensions", "Spacing Modifier", "Latin Extended Additional", "Combining Diacritical")),
    ("alphabets", ("Greek", "Cyrillic", "Armenian", "Hebrew", "Arabic", "Georgian", "Runic", "Hangul Jamo")),
    ("cjk-kana", ("CJK", "Hiragana", "Katakana", "Kanbun", "Bopomofo", "Hangul Syllables", "Kangxi", "Ideographic", "Enclosed CJK", "Enclosed Ideographic")),
    ("enclosed-num", ("Enclosed Alphanumeric", "Number Forms", "Dingbats", "Superscripts and Subscripts")),
    ("math-alnum", ("Mathematical Alphanumeric", "Letterlike")),
    ("arrows", ("Arrows", "Supplemental Arrows", "Miscellaneous Symbols and Arrows")),
    ("math-ops", ("Mathematical Operators", "Supplemental Mathematical", "Miscellaneous Mathematical")),
    ("box-block-geom", ("Box Drawing", "Block Elements", "Geometric Shapes", "Symbols for Legacy Computing", "Braille")),
    ("emoji-pict", ("Emoticons", "Miscellaneous Symbols and Pictographs", "Supplemental Symbols and Pictographs", "Transport", "Symbols and Pictographs Extended", "Playing Cards", "Mahjong", "Domino", "Alchemical", "Chess")),
    ("misc-symbols", ("Miscellaneous Symbols", "Miscellaneous Technical", "Control Pictures", "Optical Character", "General Punctuation", "Currency", "Supplemental Punctuation", "Letterlike")),
]
def group(g):
    b = block(g)
    for name, keys in GROUPS:
        if any(b.startswith(k) for k in keys):
            return name
    return "other-scripts-symbols"

def chart_class(g):
    d = [ord(b) - ord(a) for a, b in zip(g, g[1:])]
    if d and (all(x == 1 for x in d) or all(x == -1 for x in d)): return "contiguous"
    if d and (all(x > 0 for x in d) or all(x < 0 for x in d)): return "monotone"
    return "other"

def majority(xs):
    from collections import Counter
    return Counter(xs).most_common(1)[0][0]

def feats(g):
    g = list(g)
    toks = [min(tok.QWEN.ntok(x), tok.CLAUDE23.ntok(x)) for x in g]
    return {
        "chart": chart_class(g),
        "group": majority([group(x) for x in g]),
        "cat": majority([U.category(x)[0] for x in g]),
        "blocks": min(len({block(x) for x in g}), 3),
        "familiar": "1tok-all" if all(t == 1 for t in toks) else ("1tok-some" if any(t == 1 for t in toks) else "multi-all"),
        "len": min(len(g), 9),
    }
