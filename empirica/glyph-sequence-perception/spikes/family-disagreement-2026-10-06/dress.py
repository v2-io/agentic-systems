"""Out-of-family test of 'the axis is shared, the dress is model-sensitive' (read off nine reproducible Sonnet/Grok
content splits). Over continue contexts whose last glyph lies in a 'dressed' block (enclosed / mathematical / fullwidth
/ superscript / number-form / letterlike variants of letters and numbers), and which the minds compared both answered
with a glyph: per mind, the share of continuations that stay in the last glyph's block (keep the dress), and on
contexts where two minds' glyphs differ, which one kept the dress."""
import collections, itertools
import lib, features as F
from values import value, ckey

DRESSED = ("Enclosed Alphanumerics", "Enclosed Alphanumeric Supplement", "Mathematical Alphanumeric Symbols",
           "Halfwidth and Fullwidth Forms", "Superscripts and Subscripts", "Number Forms", "Letterlike Symbols",
           "Dingbats", "Enclosed CJK Letters and Months")
recs, man = lib.load()
by = collections.defaultdict(dict)
for r in recs:
    if r["kind"] != "continue": continue
    if (r.get("tags") or {}).get("variant") not in (None, "plain"): continue
    v = value(r)
    if v is None or v.startswith("∅"): continue
    c = r["context"]
    if F.block(c[-1]) not in DRESSED: continue
    by[tuple(c)].setdefault(r["mind"], v)
keep = collections.defaultdict(lambda: [0, 0])
for c, d in by.items():
    for m, v in d.items():
        k = keep[m]; k[0] += F.block(v) == F.block(c[-1]); k[1] += 1
print("share of continuations keeping the last glyph's block (dressed contexts):")
for m, (a, n) in sorted(keep.items(), key=lambda x: -x[1][1]):
    if n >= 30: print(f"   {m:14s} {a}/{n} = {a/n:.3f}")
print("where two minds' glyphs differ: who kept the dress")
for A, B in (("sonnet55", "grok46"), ("sonnet55", "gemini38flash"), ("grok46", "gemini38flash"), ("sonnet55", "opus55"), ("sonnet55", "haiku45nt")):
    c2 = collections.Counter()
    for c, d in by.items():
        if A in d and B in d and d[A] != d[B]:
            ka, kb = F.block(d[A]) == F.block(c[-1]), F.block(d[B]) == F.block(c[-1])
            c2["both" if ka and kb else (A if ka else (B if kb else "neither"))] += 1
    n = sum(c2.values())
    if n: print(f"   {A} vs {B}: n={n}  " + "  ".join(f"{k}:{v}" for k, v in c2.most_common()))
